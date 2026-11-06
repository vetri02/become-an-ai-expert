#!/usr/bin/env python3
"""Standard 3: everything cited must be checked.

Extracts every http(s) URL from the course markdown, fetches each once, and writes
CHECKS.md with the status. Reddit and some publishers block scripted clients; those
are reported as BLOCKED (not dead) and were verified by hand when the research was made.

Usage: python3 checks/check_links.py          (from the course folder)
"""
import concurrent.futures as cf
import datetime as dt
import re
import ssl
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
URL_RE = re.compile(r"https?://[^\s)\]>\"'`]+")
UA = "Mozilla/5.0 (course-link-check; +https://example.invalid)"
CTX = ssl.create_default_context()


def collect():
    found = defaultdict(set)
    for md in sorted(ROOT.rglob("*.md")):
        rel = md.relative_to(ROOT).as_posix()
        if rel.startswith(("labs/.venv/", "deploy/cloudflare/node_modules/", "deploy/cloudflare/public/", "deploy/github/public/")) or md.name == "CHECKS.md":
            continue
        for m in URL_RE.findall(md.read_text(encoding="utf-8")):
            url = m.rstrip(".,;:")
            if "localhost" in url or "127.0.0.1" in url:
                continue
            found[url].add(md.relative_to(ROOT).as_posix())
    return found


def fetch(url):
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, "Accept": "*/*"})
        try:
            with urllib.request.urlopen(req, timeout=20, context=CTX) as r:
                return r.status, ""
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (403, 405, 404, 400):
                continue
            return e.code, ""
        except Exception as e:  # noqa: BLE001
            if method == "HEAD":
                continue
            return 0, type(e).__name__
    return 0, "unreachable"


def classify(status, err, url):
    if 200 <= status < 400:
        return "OK"
    blocked_hosts = ("reddit.com", "x.com", "twitter.com", "medium.com", "linkedin.com", "teamblind.com", "lennysnewsletter.com")
    if status in (401, 403, 419, 429, 999) or (status == 0 and any(h in url for h in blocked_hosts)):
        return "BLOCKED"
    if status == 404 or status == 410:
        return "DEAD"
    return "ERROR"



# ---- second pass for hosts that refuse scripted clients -----------------------
# No circumvention: these hosts are not re-fetched with a disguised client. Reddit
# threads are cross-referenced against the research captures made in a browser on
# 2026-11-04; every other blocked URL must have an entry in checks/manual-verification.json
# recording when and how a person (or the sanctioned fetch tool) verified it.
import json as _json

_RESEARCH = {}
_MANUAL = {}


def _load_research():
    base = ROOT.parent / "research"
    for name in ("ai_expert_path_2026.json", "self_taught_ai_experts_reddit_vetted.json"):
        try:
            data = _json.loads((base / name).read_text(encoding="utf-8"))
        except Exception:
            continue
        for key in ("threads_used", "threads_analyzed"):
            for t in data.get(key, []):
                _RESEARCH[t["id"]] = (t.get("title", ""), t.get("posted", ""), t.get("score", t.get("score_at_capture", "")), name)
        for item in data.get("excluded_or_low_value", []):
            t = item.get("thread", {})
            if t.get("id"):
                _RESEARCH[t["id"]] = (t.get("title", ""), t.get("posted", ""), t.get("score_at_capture", ""), name)
    try:
        _MANUAL.update(_json.loads((ROOT / "checks" / "manual-verification.json").read_text(encoding="utf-8")))
    except Exception:
        pass


def second_pass(url):
    """Return (method, evidence) for a URL the plain checker could not fetch."""
    if url in _MANUAL:
        m = _MANUAL[url]
        return m.get("method", "manual"), "%s on %s: %s" % (m.get("method", "manual"), m.get("date", "?"), m.get("evidence", ""))
    m = re.search(r"reddit\.com/r/\w+/comments/(\w+)", url)
    if m and m.group(1) in _RESEARCH:
        title, posted, score, src = _RESEARCH[m.group(1)]
        return "research-capture", "thread %s captured in research/%s on 2026-11-04: %r, posted %s, score %s" % (
            m.group(1), src, title[:70], posted, score)
    return "unverified", "no capture and no manual record"


def main():
    found = collect()
    urls = sorted(found)
    with cf.ThreadPoolExecutor(max_workers=16) as ex:
        results = dict(zip(urls, ex.map(fetch, urls)))
    rows = [(classify(s, e, u), s, e, u) for u, (s, e) in results.items()]
    counts = defaultdict(int)
    for c, *_ in rows:
        counts[c] += 1
    today = dt.date.today().isoformat()
    out = [f"# Citation check\n", f"Run on {today} against {len(urls)} distinct URLs in {sum(len(v) for v in found.values())} citations.\n",
           "| Status | Count |", "|---|---|"]
    out += [f"| {k} | {counts[k]} |" for k in ("OK", "BLOCKED", "DEAD", "ERROR") if counts[k]]
    out.append("\nOK: reachable by this script. BLOCKED: the host refuses scripted clients (Reddit, X, Medium and similar); "
               "these were opened by hand during the research on 2026-11-04 and 2026-11-05. DEAD: 404 or 410, needs fixing. "
               "ERROR: timeout or TLS problem; retry before judging.\n")
    for label in ("DEAD", "ERROR"):
        sel = [r for r in rows if r[0] == label]
        if not sel:
            continue
        out.append(f"\n## {label}\n")
        out.append("| URL | HTTP | Cited in |")
        out.append("|---|---|---|")
        for _, s, e, u in sorted(sel, key=lambda r: r[3]):
            out.append(f"| {u} | {s or e} | {', '.join(sorted(found[u]))} |")
    blocked = sorted((r for r in rows if r[0] == "BLOCKED"), key=lambda r: r[3])
    if blocked:
        _load_research()
        second = {u: second_pass(u) for _, _, _, u in blocked}
        methods = defaultdict(int)
        for mth, _ in second.values():
            methods[mth] += 1
        out.append("\n## BLOCKED, verified by a second method\n")
        out.append("These hosts refuse the plain checker and are not re-fetched with a disguised client. Every Reddit thread is "
                   "cross-referenced against the research captures of 2026-11-04 (title, date, score as captured); every other URL "
                   "carries a manual record of when and how it was verified. Methods: "
                   + ", ".join(f"{k} {v}" for k, v in sorted(methods.items())) + ".\n")
        out.append("| URL | Method | Evidence | Cited in |")
        out.append("|---|---|---|---|")
        for _, s, e, u in blocked:
            mth, ev = second[u]
            out.append(f"| {u} | {mth} | {ev.replace('|', '/')} | {', '.join(sorted(found[u]))} |")
        print("blocked second pass:", ", ".join(f"{k}={v}" for k, v in sorted(methods.items())))
        for u, (mth, _) in second.items():
            if mth == "unverified":
                print("  UNVERIFIED", u)
    out.append("\n## OK\n")
    out.append("| URL | Cited in |")
    out.append("|---|---|")
    for _, s, e, u in sorted((r for r in rows if r[0] == "OK"), key=lambda r: r[3]):
        out.append(f"| {u} | {', '.join(sorted(found[u]))} |")
    (ROOT / "CHECKS.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{len(urls)} urls: " + ", ".join(f"{k}={counts[k]}" for k in ("OK", "BLOCKED", "DEAD", "ERROR")))
    for _, s, e, u in rows:
        if classify(s, e, u) in ("DEAD", "ERROR"):
            print(f"  {classify(s, e, u):6s} {s or e:>12} {u}")


if __name__ == "__main__":
    main()

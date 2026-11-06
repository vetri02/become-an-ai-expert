#!/usr/bin/env python3
"""Standard 6: one primary resource per module.

Every module must carry exactly one "**Primary resource:**" line, that line must
name exactly one URL, and that URL must also appear in the module's own
"Primary-source reading" list. Exit 1 on any violation.

Run from the course root:  python3 checks/check_primary.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
bad = 0
for f in sorted((ROOT / "modules").glob("[0-9][0-9]-*.md")):
    text = f.read_text(encoding="utf-8")
    lines = [l for l in text.splitlines() if l.startswith("**Primary resource:**")]
    urls = re.findall(r"https?://[^\s)]+", lines[0]) if lines else []
    reading = text[text.index("## Primary-source reading"):] if "## Primary-source reading" in text else ""
    ok = len(lines) == 1 and len(urls) == 1 and urls[0].rstrip("/") in reading.replace("/)", ")").replace("/\n", "\n") + reading
    print("%s %s: %d line(s), %d url(s)%s" % ("OK  " if ok else "FAIL", f.name[:2], len(lines), len(urls),
          "" if ok else "; url not in the module's reading list" if lines and urls else ""))
    bad += not ok
print("%d module(s) violate standard 6" % bad)
sys.exit(1 if bad else 0)

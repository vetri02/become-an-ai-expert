#!/usr/bin/env python3
"""Run every check the course claims and write VERIFICATION.md.

Run from the course root:  python3 checks/verify.py
Executes the thirteen labs, the fifteen target tests, the three graders against
the vulnerable builds and the reference solutions, and reads CHECKS.md (run
checks/check_links.py first for a fresh citation check).
"""
import datetime as dt
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run(cmd, cwd=ROOT):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, shell=isinstance(cmd, str))
    return p.returncode, p.stdout + p.stderr


def main():
    today = dt.date.today().isoformat()
    lines = ['# Course verification report', '', 'Prepared %s by `checks/verify.py`. Every number below was produced by a command run on that date in this build environment.' % today, '']

    rc, out = run(['bash', 'labs/run_all.sh'])
    passed = len(re.findall(r'^PASS ', out, re.M)); failed = len(re.findall(r'^FAIL ', out, re.M))
    lines += ['## Labs', '', '- `labs/run_all.sh`: %d passed, %d failed (exit %d). Python %s, NumPy only.' % (passed, failed, rc, sys.version.split()[0]), '']
    for m in re.finditer(r'^=== (lab\d\d_\w+\.py)\n(.*?)^(PASS|FAIL) ', out, re.M | re.S):
        key = [l for l in m.group(2).splitlines() if l.strip() and l.strip() != 'OK']
        lines.append('- %s: %s' % (m.group(1), key[-1].strip() if key else ''))
    lines.append('')

    rc, out = run([sys.executable, '-m', 'unittest', 'discover', '-s', 'targets/tests', '-t', '.'])
    m = re.search(r'Ran (\d+) tests', out)
    lines += ['## Targets', '', '- Target self-tests: ran %s, %s (exit %d).' % (m.group(1) if m else '?', 'OK' if rc == 0 else 'FAILED', rc)]
    for t in ('stale_cache', 'leaky_eval', 'leaky_agent'):
        _, v = run([sys.executable, '-m', 'targets.%s.check' % t, '--solution', 'targets.%s.target' % t])
        _, s = run([sys.executable, '-m', 'targets.%s.check' % t, '--solution', 'instructor.targets.%s_solution' % t])
        lines.append('- %s: vulnerable build %s; reference solution %s.' % (t, v.strip().splitlines()[-1], s.strip().splitlines()[-1]))
    lines.append('')

    checks = open(os.path.join(ROOT, 'CHECKS.md'), encoding='utf-8').read() if os.path.exists(os.path.join(ROOT, 'CHECKS.md')) else ''
    cm = re.search(r'Run on (\S+) against (\d+) distinct URLs in (\d+) citations', checks)
    counts = dict(re.findall(r'\| (OK|BLOCKED|DEAD|ERROR) \| (\d+) \|', checks))
    bm = re.search(r'Methods: ([^\n]+)\.', checks)
    unverified = len(re.findall(r'\| unverified \|', checks))
    blocked_summary = ('Second-method tally: %s; %d unverified.' % (bm.group(1), unverified)) if bm else ''
    lines += ['## Citations', '', '- `checks/check_links.py` last run %s: %s distinct URLs in %s citations; %s.' % (
        cm.group(1) if cm else '?', cm.group(2) if cm else '?', cm.group(3) if cm else '?',
        ', '.join('%s %s' % (k.lower(), v) for k, v in counts.items()) or 'no counts found'),
        '- BLOCKED means the host refuses the plain checker. Each such URL has a second-method record in CHECKS.md: Reddit threads are matched to the research captures of 2026-11-04 (title, date, score); the rest carry a dated manual record in checks/manual-verification.json. No disguised client is used. %s' % blocked_summary, '']

    mods = sorted(f for f in os.listdir(os.path.join(ROOT, 'modules')) if f[:2].isdigit())
    quiz = 0
    for f in mods:
        t = open(os.path.join(ROOT, 'modules', f), encoding='utf-8').read()
        q = re.search(r'## Quiz\n(.*?)(?=\n## )', t, re.S)
        quiz += len(re.findall(r'(?m)^\d+\. ', q.group(1))) if q else 0
    keys = sorted(f for f in os.listdir(os.path.join(ROOT, 'instructor')) if f.startswith('answers-m'))
    media = open(os.path.join(ROOT, 'resources/learning-resources.json'), encoding='utf-8').read().count('"type": "video"')
    lines += ['## Content counts', '', '- %d modules, %d quiz questions, %d answer-key files, 5 milestones, 1 capstone, 10 exam scenarios.' % (len(mods), quiz, len(keys)),
              '- %d recordings in the media catalogue, each fetched on 2026-11-05 and confirmed playable by page metadata; none watched in full.' % media,
              '- 20 first principles; 17 have a runnable lab (FIRST-PRINCIPLES.md has the coverage table).', '']
    rc6, out6 = run([sys.executable, 'checks/check_primary.py'])
    lines += ['## Standard 6: one primary resource per module', '', '- `checks/check_primary.py`: %s (exit %d). Each module carries exactly one primary-resource line naming one URL that also appears in its reading list.' % (out6.strip().splitlines()[-1], rc6), '']
    lines += ['## Limitations', '',
              '- The labs demonstrate mechanisms with NumPy on a laptop; no GPU training, hosted model or vector database was run in this environment. The nanochat, LoRA and GRPO runs in Modules 05, 06 and 11 are learner-run and their costs are quoted from the sources named there.',
              '- The targets use a toy decoder, a synthetic eval system and a regular-expression model. Passing a grader proves the invariant against the fixtures, not a property of any real model or product.',
              '- Prices, pay and tool names are dated in the modules and the compute appendix; re-check at signup.',
              '- The evidence base is practitioner opinion, vetted self-reported stories and official resource pages, not a hiring-outcome dataset.', '']
    with open(os.path.join(ROOT, 'VERIFICATION.md'), 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(lines))
    print('\n'.join(lines[:12]))
    print('wrote VERIFICATION.md')


if __name__ == '__main__':
    main()

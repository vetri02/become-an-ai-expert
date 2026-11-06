"""The toy model behind the stale-cache target. Attacker's side: do not edit.

A decoder whose next token depends on every previous position through a
cheap per-position contribution g(token, position). The reference generator
recomputes the whole prefix at every step, which is correct and slow. A cache
keeps the contributions so each step costs one g() call. COUNTER['g'] counts
calls so graders can measure work without timing.
"""
VOCAB = 32
COUNTER = {"g": 0}


def g(token, position):
    """Per-position contribution. Depends on position, so a cache that
    forgets where a token sat gives wrong answers."""
    COUNTER["g"] += 1
    return ((token + 1) * 2654435761 + (position + 1) * 40503) % 1000003


def next_token(contributions):
    """Next token from the summed contributions of the prefix."""
    return (sum(contributions) * 7 + len(contributions)) % VOCAB


def reference_generate(prompt, n):
    """Correct, uncached: recompute every contribution at every step."""
    toks = list(prompt)
    for _ in range(n):
        contribs = [g(t, i) for i, t in enumerate(toks)]
        toks.append(next_token(contribs))
    return toks[len(prompt):]


PROMPTS = [[1, 2, 3], [5, 5, 5, 5], [31, 0, 7, 9, 2], [4], [8, 16, 24, 2, 6, 1, 1]]

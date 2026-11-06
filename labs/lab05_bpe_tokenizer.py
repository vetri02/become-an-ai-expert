"""Lab 05: byte-pair encoding from scratch (Module 03, or A4 on the Novice track; Principle 2).

Trains a tiny BPE tokenizer on a text, encodes and decodes, and shows that
vocabulary size trades off against sequence length (and therefore cost).

Run: python lab05_bpe_tokenizer.py
"""
from collections import Counter

TEXT = (
    "the model predicts the next token. the next token depends on the previous tokens. "
    "tokens are not words; the tokenizer decides what a token is. "
) * 20


def get_pairs(ids):
    return Counter(zip(ids, ids[1:]))


def merge(ids, pair, new_id):
    out, i = [], 0
    while i < len(ids):
        if i < len(ids) - 1 and (ids[i], ids[i + 1]) == pair:
            out.append(new_id); i += 2
        else:
            out.append(ids[i]); i += 1
    return out


def train(text, n_merges):
    ids = list(text.encode("utf-8"))
    merges = {}
    for j in range(n_merges):
        pairs = get_pairs(ids)
        if not pairs:
            break
        pair = max(pairs, key=pairs.get)
        new_id = 256 + j
        ids = merge(ids, pair, new_id)
        merges[pair] = new_id
    return merges


def encode(text, merges):
    ids = list(text.encode("utf-8"))
    for pair, new_id in merges.items():  # apply merges in training order
        ids = merge(ids, pair, new_id)
    return ids


def decode(ids, merges):
    vocab = {i: bytes([i]) for i in range(256)}
    for (a, b), new_id in merges.items():
        vocab[new_id] = vocab[a] + vocab[b]
    return b"".join(vocab[i] for i in ids).decode("utf-8", errors="replace")


if __name__ == "__main__":
    sample = "the next token depends on the tokenizer."
    base = len(sample.encode("utf-8"))
    print(f"sample text: {sample!r}  ({base} bytes)")
    prev = base
    for n in (0, 10, 40, 100):
        m = train(TEXT, n)
        ids = encode(sample, m)
        assert decode(ids, m) == sample, "round trip failed"
        print(f"  {n:3d} merges -> vocab {256+len(m):4d}, sequence length {len(ids):3d}  ({base/len(ids):.1f} bytes/token)")
        assert len(ids) <= prev
        prev = len(ids)
    m = train(TEXT, 40)
    longest = max(m.values(), key=lambda i: len(decode([i], m)))
    print(f"longest learned token after 40 merges: {decode([longest], m)!r}")
    print("OK")

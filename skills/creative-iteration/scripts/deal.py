"""Deal random slices of a numbered pool, so the lead never picks who sees what.

Entries are dealt from a shuffled pool; when it runs out, a fresh shuffle
starts, so slices overlap only when the hands outnumber the pool. No hand
gets the same entry twice.

    deal.py --pool 82 --hands g1:15 g2:15 g3:15 g4:15 control:15 wild:5
"""
import argparse
import json
import secrets

rng = secrets.SystemRandom()


def deal(pool, hands):
    stack, out = [], {}
    for name, size in hands:
        hand = []
        while len(hand) < min(size, pool):
            if not stack:
                stack = rng.sample(range(1, pool + 1), pool)
            n = stack.pop()
            if n not in hand:
                hand.append(n)
        out[name] = sorted(hand)
    return out


def hand(spec):
    name, size = spec.split(":")
    return name, int(size)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--pool", type=int, required=True, help="number of entries in pool.md")
    p.add_argument("--hands", type=hand, nargs="+", required=True, help="name:size")
    a = p.parse_args()
    print(json.dumps(deal(a.pool, a.hands)))

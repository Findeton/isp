#!/usr/bin/env python3
"""Exact small-system covariant-readout receipt for construction-order gauge."""

from fractions import Fraction as F
from itertools import combinations, permutations

checks = []


def check(label, ok, detail=""):
    checks.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" — {detail}" if detail else ""))


def closure(n, edges):
    r = [[False] * n for _ in range(n)]
    for a, b in edges:
        r[a][b] = True
    for k in range(n):
        for i in range(n):
            if r[i][k]:
                for j in range(n):
                    r[i][j] = r[i][j] or r[k][j]
    return tuple(tuple(row) for row in r)


def permute_rel(rel, p):
    n = len(rel)
    out = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if rel[i][j]:
                out[p[i]][p[j]] = True
    return tuple(tuple(row) for row in out)


def code(rel):
    return ''.join('1' if x else '0' for row in rel for x in row)


def canonical(rel):
    n = len(rel)
    return min(code(permute_rel(rel, p)) for p in permutations(range(n)))


def is_downset(rel, subset):
    S = set(subset)
    for x in S:
        for y in range(len(rel)):
            if rel[y][x] and y not in S:
                return False
    return True


def induced(rel, subset):
    sub = list(subset)
    return tuple(tuple(rel[i][j] for j in sub) for i in sub)


def stem_signature(rel):
    sig = []
    n = len(rel)
    for k in range(1, n + 1):
        vals = set()
        for S in combinations(range(n), k):
            if is_downset(rel, S):
                vals.add(canonical(induced(rel, S)))
        sig.append(tuple(sorted(vals)))
    return tuple(sig)


def relabel_by_linear_extension(rel, ext):
    # Old element ext[position] receives construction label position.
    p = [0] * len(ext)
    for position, old in enumerate(ext):
        p[old] = position
    return permute_rel(rel, tuple(p))


print("[cg3 — exact covariant click census]")

# A five-event order with multiple linear extensions.
rel = closure(5, {(0, 2), (1, 2), (2, 4), (3, 4)})
exts = [p for p in permutations(range(5))
        if all(not rel[p[j]][p[i]] for i in range(5) for j in range(i + 1, 5))]
codes = {canonical(relabel_by_linear_extension(rel, p)) for p in exts}
sigs = {stem_signature(relabel_by_linear_extension(rel, p)) for p in exts}
check("S0 construction labels vary but unlabeled order/stems do not",
      len(exts) > 1 and len(codes) == 1 and len(sigs) == 1,
      f"linear extensions={len(exts)}")

# Exact path weights: local addition factors depend only on the new event's ancestor set.
ancestor_sets = [{}, {}, {0, 1}, {}, {0, 1, 2, 3}]


def event_factor(old):
    a = ancestor_sets[old]
    return F(len(a) + 1, len(a) + 2)


weights = {p: __import__('functools').reduce(lambda x, y: x * y,
                                             (event_factor(v) for v in p), F(1))
           for p in exts}
check("S1 alternate linear extensions have exact equal total weight",
      len(set(weights.values())) == 1, f"weight={next(iter(weights.values()))}")

# A real influence edge changes covariant finite stems; a label swap does not.
base = closure(4, {(0, 2), (1, 2)})
influenced = closure(4, {(0, 2), (1, 2), (2, 3)})
base_swap = permute_rel(base, (1, 0, 2, 3))
check("S2 influence is stem-readable; scheduler label is not",
      stem_signature(base) != stem_signature(influenced)
      and stem_signature(base) == stem_signature(base_swap))

# Reduced round-48 audit: deposit snapshot, then global directed leak.
def leak(x, v, r, g=F(1, 4)):
    y = list(x)
    moved = g * y[v]
    y[v] -= moved
    y[r] += moved
    return tuple(y)


def reduced_builder(schedule):
    x = (F(0), F(0), F(0))
    snapshots = []
    for c in schedule:
        y = list(x)
        y[c] += 1
        x = tuple(y)
        snapshots.append(x[c])
        # Same global post-commit leak each step, as in the class being audited.
        x = leak(x, 0, 1)
    # The old two-clock rule on the snapshots: construction index + scalar content.
    edges = set()
    for i in range(len(schedule)):
        for j in range(i + 1, len(schedule)):
            if snapshots[i] <= snapshots[j]:
                edges.add((i, j))
    return tuple(snapshots), closure(len(schedule), edges)


sa, ra = reduced_builder((0, 2, 1, 2))
sb, rb = reduced_builder((2, 0, 1, 2))
audit_diff = sa != sb
cov_diff = canonical(ra) != canonical(rb) or stem_signature(ra) != stem_signature(rb)
print(f"[INFO] S3 reduced round-48 alternate schedulers: snapshots {sa} vs {sb}; "
      f"covariant-order-difference={cov_diff}")
check("S3 current-builder scheduler audit executed and classified", audit_diff,
      "scheduler survives content; covariant survival printed, not pre-assumed")

print(f"CHECKS PASSED: {sum(checks)}/{len(checks)}")
raise SystemExit(0 if all(checks) else 1)


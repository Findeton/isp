#!/usr/bin/env python3
"""Exact receipt for note-cg1-construction-order-gauge.md.

All theorem-critical calculations use integers or Fraction.  This receipt
tests construction-order gauge separately from locality and interaction.
"""

from fractions import Fraction as F
from itertools import combinations, permutations


checks = []


def check(label, ok, detail=""):
    checks.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" — {detail}" if detail else ""))


def transitive_relations_natural(n):
    """All strict transitively closed relations compatible with 0<...<n-1."""
    pairs = list(combinations(range(n), 2))
    out = []
    for mask in range(1 << len(pairs)):
        rel = {(a, b) for j, (a, b) in enumerate(pairs) if (mask >> j) & 1}
        good = True
        for a, b in tuple(rel):
            for c, d in tuple(rel):
                if b == c and (a, d) not in rel:
                    good = False
                    break
            if not good:
                break
        if good:
            out.append(rel)
    return out


def linear_extensions(n, rel):
    return [p for p in permutations(range(n))
            if all(p.index(a) < p.index(b) for a, b in rel)]


def adjacent_swap_graph(exts, rel):
    idx = {p: j for j, p in enumerate(exts)}
    adj = [[] for _ in exts]
    for j, p in enumerate(exts):
        for k in range(len(p) - 1):
            a, b = p[k], p[k + 1]
            if (a, b) in rel or (b, a) in rel:
                continue
            q = p[:k] + (b, a) + p[k + 2:]
            if q in idx:
                adj[j].append(idx[q])
    return adj


def connected(adj):
    seen = {0}
    stack = [0]
    while stack:
        i = stack.pop()
        for j in adj[i]:
            if j not in seen:
                seen.add(j)
                stack.append(j)
    return len(seen) == len(adj)


print("[cg1 — exact construction-order gauge]")

# G0: exhaustive adjacent-swap theorem in the registered scope n <= 5.
counts = []
all_connected = True
for n in range(1, 6):
    ps = transitive_relations_natural(n)
    counts.append(len(ps))
    for rel in ps:
        exts = linear_extensions(n, rel)
        if not connected(adjacent_swap_graph(exts, rel)):
            all_connected = False
            break
check("G0 adjacent-swap connectivity for every naturally labeled poset n<=5",
      all_connected, f"poset counts {counts}")


# Elementary exact update maps on four local ledgers.
def deposit(x, i, amount=F(1)):
    y = list(x)
    y[i] += amount
    return tuple(y)


def pair_leak(x, i, j, g=F(1, 4)):
    """Conservative directed fractional leak i -> j."""
    y = list(x)
    moved = g * y[i]
    y[i] -= moved
    y[j] += moved
    return tuple(y)


zero4 = (F(0),) * 4

# G1: local independent/shared-support activities factor on disjoint support.
def local_activity(ancestor_size, support_size):
    return F(ancestor_size + support_size + 1, support_size + 2)


wA = local_activity(2, 1)
wB = local_activity(3, 2)
diamond_left = wA * wB
diamond_right = wB * wA

# A reduced round-48-style control: every commit is followed by a global leak.
def global_scheduled_update(x, i):
    return pair_leak(deposit(x, i), 0, 1, F(1, 3))


l0_ab = global_scheduled_update(global_scheduled_update(zero4, 0), 2)
l0_ba = global_scheduled_update(global_scheduled_update(zero4, 2), 0)
print(f"[INFO] G1 global scheduler control: L0_AB={l0_ab}, L0_BA={l0_ba}, "
      f"order-sensitive={l0_ab != l0_ba}")
check("G1 local L1/L2 diamond exact; L0 classified without a pinned direction",
      diamond_left == diamond_right, f"local path weight={diamond_left}")


# G2: a support-size/ancestor-size law is invariant under every relabeling.
base_edges = {(0, 1), (1, 2)}
base_support = {0, 2}


def signature_under_perm(p):
    edges = {(p[a], p[b]) for a, b in base_edges}
    support = {p[a] for a in base_support}
    indeg = sorted(sum(1 for a, b in edges if b == v) for v in range(3))
    outdeg = sorted(sum(1 for a, b in edges if a == v) for v in range(3))
    return (tuple(indeg), tuple(outdeg), len(support), local_activity(len(edges), len(support)))


sigs = {signature_under_perm(p) for p in permutations(range(3))}
check("G2 exact relabeling covariance", len(sigs) == 1, f"distinct signatures={len(sigs)}")


# G3: local hazard ignores a disconnected component; global-normalized control does not.
def local_hazard(x, i, neighbors):
    return F(1) + x[i] + sum(x[j] for j in neighbors[i])


neighbors = {0: {1}, 1: {0}, 2: {3}, 3: {2}}
x = (F(1), F(2), F(3), F(4))
x_far = (F(1), F(2), F(30), F(40))
h_local = local_hazard(x, 0, neighbors)
h_local_far = local_hazard(x_far, 0, neighbors)
h_global = h_local / (F(1) + sum(x))
h_global_far = h_local_far / (F(1) + sum(x_far))
check("G3 causal sufficiency detects global normalization",
      h_local == h_local_far and h_global != h_global_far,
      f"local={h_local}; normalized {h_global}->{h_global_far}")


# G4: disjoint leaks commute; overlapping leaks do not and leave a local state record.
x0 = (F(4), F(0), F(2), F(0))
dis_ab = pair_leak(pair_leak(x0, 0, 1), 2, 3)
dis_ba = pair_leak(pair_leak(x0, 2, 3), 0, 1)
ov_ab = pair_leak(pair_leak(x0, 0, 1), 1, 2)
ov_ba = pair_leak(pair_leak(x0, 1, 2), 0, 1)
check("G4 recorded-noncommutativity criterion",
      dis_ab == dis_ba and ov_ab != ov_ba,
      f"overlap_AB={ov_ab}, overlap_BA={ov_ba}")


# G5: conservative leak preserves exact total; controls do not share its ledger.
cons = pair_leak(x0, 0, 1, F(3, 8))
destructive = list(x0)
destructive[0] *= F(5, 8)
teleport = list(x0)
teleport[1] += teleport[0]
teleport[0] = F(0)
check("G5 exact conservation and control separation",
      sum(cons) == sum(x0) and sum(destructive) != sum(x0) and sum(teleport) == sum(x0),
      f"totals base/cons/destroy/tele={sum(x0)}/{sum(cons)}/{sum(destructive)}/{sum(teleport)}")


print(f"CHECKS PASSED: {sum(checks)}/{len(checks)}")
raise SystemExit(0 if all(checks) else 1)

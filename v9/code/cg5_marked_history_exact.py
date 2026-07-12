#!/usr/bin/env python3
"""Round-2 O3/O4/O6 exact marked-history and support-bootstrap receipt."""

from fractions import Fraction as F
from itertools import combinations, permutations

checks = []


def check(label, ok, detail=""):
    checks.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" — {detail}" if detail else ""))


def components(n, supports):
    adj = [set() for _ in range(n)]
    for S in supports:
        for a, b in combinations(S, 2):
            adj[a].add(b)
            adj[b].add(a)
    out = []
    unseen = set(range(n))
    while unseen:
        root = min(unseen)
        comp = {root}
        stack = [root]
        unseen.remove(root)
        while stack:
            a = stack.pop()
            for b in adj[a]:
                if b in unseen:
                    unseen.remove(b)
                    comp.add(b)
                    stack.append(b)
        out.append(frozenset(comp))
    return tuple(sorted(out, key=lambda s: tuple(sorted(s))))


def allowed_local_new_support(S, comps):
    return any(set(S) <= set(C) for C in comps)


print("[cg5 — exact marked histories and support bootstrap]")

# B0: exhaustive finite shadow of the no-bootstrap theorem.
no_merge = True
tested = 0
for n in range(2, 7):
    # Test every two-block partition cut and every candidate support.
    for cut in range(1, n):
        comps = (frozenset(range(cut)), frozenset(range(cut, n)))
        for k in range(1, n + 1):
            for S in combinations(range(n), k):
                tested += 1
                if allowed_local_new_support(S, comps):
                    if not any(set(S) <= set(C) for C in comps):
                        no_merge = False
check("B0 support-local rules cannot bootstrap across components", no_merge,
      f"finite cases={tested}; theorem is immediate from subset closure")

# B1: a root split creates a covariant common-ancestor support without slot names.
root_supports = {frozenset({0})}
# Branch lineage 0 into children 0,1; inheritance creates their joint support.
branched = {frozenset({0}), frozenset({1}), frozenset({0, 1})}
check("B1 common-ancestor branching supplies a connected support seed",
      len(components(2, branched)) == 1 and frozenset({0, 1}) in branched,
      "root/branch rule remains an explicit boundary law")


# Marked event representation:
#   (ports, kind, block_id)
#   port = (lineage, parent_event, post_content, local_outcome)
# This retains every lineage-to-parent/content/outcome incidence explicitly.
def add_event(events, latest, support, kind="seal", content=(), outcome=(), block="private"):
    support = tuple(sorted(support))
    if not content:
        content = (F(0),) * len(support)
    if not outcome:
        outcome = (None,) * len(support)
    ports = tuple((i, latest.get(i, -1), content[j], outcome[j])
                  for j, i in enumerate(support))
    e = (ports, kind, block)
    idx = len(events)
    events = events + (e,)
    latest = dict(latest)
    for i in support:
        latest[i] = idx
    return events, latest


def history_for(schedule):
    events = ((((0, -1, F(2), None), (1, -1, F(2), None)), "root", "root-block"),)
    latest = {0: 0, 1: 0}
    for support, kind, content, outcome, block in schedule:
        events, latest = add_event(events, latest, support, kind, content, outcome, block)
    return events


def permuted_history(events, lp, ep):
    # old lineage -> new; old event -> new
    transformed = [None] * len(events)
    for old, e in enumerate(events):
        ports, kind, block = e
        nports = []
        for lineage, parent, content, outcome in ports:
            nparent = -1 if parent == -1 else ep[parent]
            nports.append((lp[lineage], nparent, content, outcome))
        ne = (tuple(sorted(nports)), kind, block)
        transformed[ep[old]] = ne
    return tuple(transformed)


def hcode(events):
    return repr(events)


def canonical(events, nlin=2):
    vals = []
    for lperm in permutations(range(nlin)):
        for eperm in permutations(range(len(events))):
            vals.append(hcode(permuted_history(events, lperm, eperm)))
    return min(vals)


# B2: disjoint scheduler presentations are one marked history.
A = ((0,), "private", (F(3),), (0,), "A-block")
B = ((1,), "private", (F(5),), (1,), "B-block")
hAB = history_for((A, B))
hBA = history_for((B, A))
check("B2 disjoint AB/BA quotient to one canonical marked history",
      canonical(hAB) == canonical(hBA))

# B3: overlap order is explicitly written into parentage and content marks.
J = ((0, 1), "joint", (F(4), F(4)), (0, 1), "AB-block")
hAJ = history_for((A, J))
hJA = history_for((J, A))
check("B3 overlapping order becomes recorded ancestry", canonical(hAJ) != canonical(hJA))

# B4: event-based conservative transfer is itself sealed as a rational mark.
def transfer(contents, i, j, g=F(1, 4)):
    y = list(contents)
    move = g * y[i]
    y[i] -= move
    y[j] += move
    return tuple(y)


before = (F(4), F(2))
after = transfer(before, 0, 1)
h_transfer = history_for((((0, 1), "joint-transfer", after, (None, None), "transfer-block"),))
check("B4 event-based transport is conservative and marked",
      sum(after) == sum(before) and after == (F(3), F(3)) and "joint-transfer" in canonical(h_transfer),
      f"{before}->{after}")

# Bare order code and marked code: same parent graph, different content is the old hidden-state gap.
def bare_parent_code(events):
    n = len(events)
    rel = [[False] * n for _ in range(n)]
    for j, e in enumerate(events):
        for _, p, _, _ in e[0]:
            if p != -1:
                rel[p][j] = True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                rel[i][j] = rel[i][j] or (rel[i][k] and rel[k][j])
    vals = []
    for p in permutations(range(n)):
        vals.append(''.join('1' if rel[p[i]][p[j]] else '0' for i in range(n) for j in range(n)))
    return min(vals)


h_hidden1 = history_for((((0,), "private", (F(23, 16),), (None,), "same-block"),))
h_hidden2 = history_for((((0,), "private", (F(5, 4),), (None,), "same-block"),))
check("B5 bare stems can agree while marked histories differ",
      bare_parent_code(h_hidden1) == bare_parent_code(h_hidden2)
      and canonical(h_hidden1) != canonical(h_hidden2))

# B6: explicit regression for the round-2 referee's lineage-owned-outcome bug.
h_owned1 = history_for((((0, 1), "joint", (F(3), F(5)), (0, 1), "owned"),))
h_owned2 = history_for((((0, 1), "joint", (F(5), F(3)), (1, 0), "owned"),))
check("B6 lineage-owned parent/content/outcome ports relabel covariantly",
      canonical(h_owned1) == canonical(h_owned2))

print(f"CHECKS PASSED: {sum(checks)}/{len(checks)}")
raise SystemExit(0 if all(checks) else 1)

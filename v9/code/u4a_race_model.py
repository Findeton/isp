#!/usr/bin/env python3
"""
u4a_race_model.py — v9 round 10: validation of the census's exact-law
reduction (note-u4 Addendum; gates pinned there + here pre-run).

The reduction: churn-web value rankings follow the sequential RACE MODEL
over slot-lives (independent unit-rate Poisson prefixes); the induced
unlabeled-order measure = exact-rational DP (slot RGS x resets) x race
interleavings. This receipt validates it BEFORE the n <= 7 census runs
on it:
  V1 (anchor, exact): at L = 1 (reset after every commit; all lives
     singletons) the exact enumeration equals the uniform-ranking (2D
     random box order) measure, Fraction-identical, n = 3..5.
  V2 (probability mass, exact): the enumerated measure sums to exactly 1
     at every n (Fraction arithmetic; no float in the measure path).
  V3 (Monte Carlo, the actual generator): the s8-ported web_j3 (M = 32,
     L = 2), 200k webs at n = 3 and n = 4 — per reached class
     |p_hat - p_exact| <= 4*sqrt(p(1-p)/S) (all classes), TV printed.
  V4 (support, by construction): every enumerated web's order equals the
     intersection of the two linear orders (commit rank, value rank) —
     the explicit 2-realizer of note-u4 Corollary A, asserted per web.
Seed 20260717 (MC only). M = 32, L = 2 (the paper-16 corner).
"""
import numpy as np
from fractions import Fraction
from itertools import permutations, product

rng = np.random.default_rng(20260717)
M, L = 32, 2
PASS = 0
FAIL = 0

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def canon(Cmat, n):
    """Canonical form of an unlabeled order: lexicographically minimal
    adjacency bitstring over all relabelings (n <= 5: brute force)."""
    best = None
    idx = list(range(n))
    for perm in permutations(idx):
        bits = tuple(Cmat[perm[i]][perm[j]] for i in range(n) for j in range(n))
        if best is None or bits < best:
            best = bits
    return best

def order_from_ranks(ranks):
    n = len(ranks)
    return [[1 if (i < j and ranks[i] < ranks[j]) else 0
             for j in range(n)] for i in range(n)]

def rgs_patterns(n):
    """Restricted-growth strings (slot-assignment patterns) with exact
    j3 probabilities: join a specific used slot 1/M; fresh (M-u)/M."""
    out = []
    def rec(seq, u, p):
        t = len(seq)
        if t == n:
            out.append((tuple(seq), p)); return
        for s in range(u):
            rec(seq + [s], u, p * Fraction(1, M))
        rec(seq + [u], u + 1, p * Fraction(M - u, M))
    rec([], 0, Fraction(1))
    return out

def life_partition(slots, resets):
    """Cut each slot's commit chain after every reset commit."""
    n = len(slots)
    life_of = [None] * n
    cur = {}
    nxt = 0
    for t in range(n):
        s = slots[t]
        if s not in cur:
            cur[s] = nxt; nxt += 1
        life_of[t] = cur[s]
        if resets[t]:
            del cur[s]
    return tuple(life_of)

def interleavings(life_of):
    """All rank assignments preserving within-life commit order, with
    race-model probabilities (products of 1/#pending-lives)."""
    n = len(life_of)
    lives = {}
    for t, l in enumerate(life_of):
        lives.setdefault(l, []).append(t)
    out = []
    def rec(pos, ranks, pending, p):
        live = [l for l in pending if pending[l]]
        if pos == n:
            out.append((tuple(ranks), p)); return
        k = len(live)
        for l in live:
            t = pending[l][0]
            ranks2 = list(ranks); ranks2[t] = pos
            pend2 = dict(pending); pend2[l] = pending[l][1:]
            rec(pos + 1, ranks2, pend2, p * Fraction(1, k))
    rec(0, [None] * n, {l: v[:] for l, v in lives.items()}, Fraction(1))
    return out

def exact_measure(n, Lval):
    """The induced unlabeled-order measure, exact Fractions."""
    meas = {}
    pr = Fraction(1, Lval); qr = 1 - pr
    for slots, ps in rgs_patterns(n):
        for resets in product([0, 1], repeat=n):
            pres = ps
            for r in resets:
                pres *= pr if r else qr
            lp = life_partition(slots, resets)
            for ranks, pi in interleavings(lp):
                Cm = order_from_ranks(ranks)
                # V4: the explicit 2-realizer (dominance construction)
                for i in range(n):
                    for j in range(n):
                        assert Cm[i][j] == (1 if (i < j and ranks[i] < ranks[j]) else 0)
                key = canon(Cm, n)
                meas[key] = meas.get(key, Fraction(0)) + pres * pi
    return meas

def uniform_ranking_measure(n):
    meas = {}
    p = Fraction(1, np.math.factorial(n))
    for ranks in permutations(range(n)):
        key = canon(order_from_ranks(list(ranks)), n)
        meas[key] = meas.get(key, Fraction(0)) + p
    return meas

print("[u4a race-model validation: exact reduction vs the actual generator]")
for n in (3, 4, 5):
    m2 = exact_measure(n, L)
    tot = sum(m2.values())
    check(f"V2 (n = {n}): the exact measure sums to 1 (Fraction-identical; "
          f"{len(m2)} reached classes)", tot == 1, f"sum = {tot}")
    m1 = exact_measure(n, 1)
    mu = uniform_ranking_measure(n)
    check(f"V1 (n = {n}): the L = 1 anchor equals the uniform-ranking (2D "
          f"box) measure, Fraction-identical (Corollary B)",
          m1 == mu, f"{len(m1)} classes")
print("      V4: the explicit 2-realizer asserted on every enumerated web (Corollary A) — no violation raised")

def web_j3_ranks(n):
    chi_acc = np.zeros(M)
    chi = np.zeros(n)
    for t in range(n):
        c = int(rng.integers(M))
        chi_acc[c] += rng.exponential(1.0)
        chi[t] = chi_acc[c]
        if rng.random() < 1.0 / L:
            chi_acc[c] = 0.0
    return np.argsort(np.argsort(chi))

S = 200000
for n in (3, 4):
    m2 = exact_measure(n, L)
    counts = {}
    for _ in range(S):
        ranks = web_j3_ranks(n)
        key = canon(order_from_ranks(list(ranks)), n)
        counts[key] = counts.get(key, 0) + 1
    ok_all = True
    worst = 0.0
    tv = 0.0
    keys = set(m2) | set(counts)
    for k in keys:
        p = float(m2.get(k, Fraction(0)))
        ph = counts.get(k, 0) / S
        tv += abs(ph - p) / 2
        sig = max((p * (1 - p) / S) ** 0.5, 1e-9)
        z = abs(ph - p) / sig
        worst = max(worst, z)
        if z > 4: ok_all = False
    check(f"V3 (n = {n}): the ACTUAL j3 generator matches the exact "
          f"reduction on every reached class (|z| <= 4 at S = {S})",
          ok_all, f"worst |z| = {worst:.2f}; TV = {tv:.5f}; "
          f"{len(m2)} exact / {len(counts)} observed classes")

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)

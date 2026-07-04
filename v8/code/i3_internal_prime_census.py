#!/usr/bin/env python3
"""
i3_internal_prime_census.py — v8 paper 12 §2.3: closing the internal-prime
residue — the one realizer freedom that can move the canonical point set.

THE RESIDUE (paper 12 Thm 2.1 fine print): series modules have no freedom;
parallel modules relabel (D* exactly invariant); the ONLY freedom that can move
the embedded point set is an internal PRIME node of the modular decomposition —
a proper strong module whose quotient is prime — whose 2-way flip transposes
r1 <-> r2 locally. Paper 12 round 1 left its occurrence UNMEASURED.

THE CENSUS DESIGN (operational, self-adjudicating):
  1. Enumerate the minimal module containing each pair {i,j} (closure: repeatedly
     absorb every outside element whose relation profile distinguishes members;
     early-exit when |S| > CAP — a closure that explodes past CAP is treated as
     "no small module for this pair", disclosed). COVERAGE ARGUMENT: an internal
     prime node M IS the minimal module of EVERY cross-child pair (a prime
     quotient has no proper union-of-children submodule), so every internal
     prime node of size <= CAP is found by this enumeration; and the prime
     flip is its entire point-moving freedom.
  2. For each distinct proper module M found, apply the TRANSPOSE TEST: reassign
     M's r1-positions in old-r2 order and M's r2-positions in old-r1 order
     (= the quotient flip F -> F^T restricted to M, with outsiders pinned);
     check whether the result still realizes P (dominance == C) and whether the
     embedded point set moved. Series -> identity; parallel -> relabeling (set
     unchanged); prime/mixed-with-valid-flip -> POINT-MOVING freedom, priced by
     |Delta D*| directly.
  3. Populations: sprinklings (the absence claim + the E ~ n^{2-m} module-size
     scaling estimate's data), jittered lattice, cluster blow-up (the likeliest
     home of genuine prime blocks: 6-point clusters realize random 4-point
     orders, and the 4-element N-poset is prime).

Verdict semantics: either ABSENCE (census zero + the scaling data backing the
O(1/n)-type estimate) or EXHIBIT + PRICE (|Delta D*| vs the paper's signals).
Float discipline: measurement float64. Seed: default_rng(20260702).
"""

import numpy as np

rng = np.random.default_rng(20260702)

PASS = 0
FAIL = 0
CAP = 12          # closure early-exit (disclosed): modules larger than CAP are
                  # treated as absent-at-this-size; the coverage claim is scoped
                  # to internal prime nodes of size <= CAP

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))


def dominance_order(pts):
    return (pts[None, :, 0] > pts[:, None, 0]) & (pts[None, :, 1] > pts[:, None, 1])

def star_discrepancy_exact(pts):
    N = len(pts)
    us = np.unique(np.concatenate([pts[:, 0], [1.0]]))
    vs = np.unique(np.concatenate([pts[:, 1], [1.0]]))
    order = np.argsort(pts[:, 0], kind="stable")
    pu = pts[order, 0]; pv = pts[order, 1]
    best = 0.0
    for a in us:
        k_open = np.searchsorted(pu, a, side="left")
        k_closed = np.searchsorted(pu, a, side="right")
        sv_o = np.sort(pv[:k_open]); sv_c = np.sort(pv[:k_closed])
        cnt_o = np.searchsorted(sv_o, vs, side="left") / N
        cnt_c = np.searchsorted(sv_c, vs, side="right") / N
        vol = a * vs
        best = max(best, float(np.abs(cnt_o - vol).max()),
                   float(np.abs(cnt_c - vol).max()))
    return best

def sprinkle_pts(N):
    return rng.random((N, 2))

def lattice_pts(N):
    m = int(round(np.sqrt(N)))
    g = (np.arange(m) + 0.5) / m
    U, V = np.meshgrid(g, g, indexing="ij")
    pts = np.column_stack([U.ravel(), V.ravel()])
    return pts + rng.normal(0, 1e-4, pts.shape)

def cluster_pts(N, c=6, jit=1e-3):
    M = N // c
    ctr = rng.random((M, 2))
    return np.repeat(ctr, c, axis=0) + rng.normal(0, jit, (M * c, 2))


# ------------------------------------------------ minimal pair-module closure
def minimal_modules(C, cap=CAP):
    """All distinct proper modules (2 <= |M| <= cap) arising as the closure of
    some pair. R codes relations: 0 incomparable, 1 row<col, 2 col<row."""
    N = C.shape[0]
    R = C.astype(np.int8) + 2 * C.T.astype(np.int8)   # R[x, z]: rel of x vs z
    found = set()
    for i in range(N):
        for j in range(i + 1, N):
            S = {i, j}
            grew = True
            while grew and len(S) <= cap:
                grew = False
                idx = sorted(S)
                cols = R[:, idx]                       # rel of every z to members
                uniform = (cols == cols[:, :1]).all(axis=1)
                dist = np.nonzero(~uniform)[0]
                add = [z for z in dist if z not in S]
                if add:
                    S.update(add)
                    grew = True
            if 2 <= len(S) <= cap and len(S) < N:
                found.add(frozenset(S))
    return [sorted(m) for m in found]

# ------------------------------------------------ the operational transpose test
def transpose_test(pts, M):
    """Apply the quotient flip to module M (outsiders pinned): M's r1-positions
    reassigned in old-r2 order and vice versa. Returns (realizes, moved, dD*)."""
    N = len(pts)
    r1 = np.argsort(np.argsort(pts[:, 0])).astype(int)
    r2 = np.argsort(np.argsort(pts[:, 1])).astype(int)
    C = dominance_order(pts)
    r1n, r2n = r1.copy(), r2.copy()
    pos1 = sorted(r1[x] for x in M)
    pos2 = sorted(r2[x] for x in M)
    by_r2 = sorted(M, key=lambda x: r2[x])
    by_r1 = sorted(M, key=lambda x: r1[x])
    for p, x in zip(pos1, by_r2):
        r1n[x] = p
    for p, x in zip(pos2, by_r1):
        r2n[x] = p
    emb0 = np.column_stack([(r1 + 0.5) / N, (r2 + 0.5) / N])
    emb1 = np.column_stack([(r1n + 0.5) / N, (r2n + 0.5) / N])
    realizes = np.array_equal(dominance_order(emb1), C)
    t0 = {(int(a), int(b)) for a, b in zip(r1, r2)}
    t1 = {(int(a), int(b)) for a, b in zip(r1n, r2n)}
    moved = t0 != t1
    dD = abs(star_discrepancy_exact(emb1) - star_discrepancy_exact(emb0)) \
        if (realizes and moved) else 0.0
    return realizes, moved, dD

# =========================== the census proper (tuple-set-based, final logic)
def census_final(pts, tag):
    """Classify each minimal pair-module by its transpose action on the POINT
    SET: identity / relabeling (set unchanged) / point-moving (set changed,
    still realizes) / invalid-flip (not a realizer — no such freedom)."""
    N = len(pts)
    C = dominance_order(pts)
    mods = minimal_modules(C)
    r1 = np.argsort(np.argsort(pts[:, 0])).astype(int)
    r2 = np.argsort(np.argsort(pts[:, 1])).astype(int)
    emb0 = np.column_stack([(r1 + 0.5) / N, (r2 + 0.5) / N])
    d0 = star_discrepancy_exact(emb0)
    stats = {"identity": 0, "relabel": 0, "moving": 0, "invalid": 0}
    movers = []
    for M in mods:
        r1n, r2n = r1.copy(), r2.copy()
        pos1 = sorted(r1[x] for x in M)
        pos2 = sorted(r2[x] for x in M)
        for p, x in zip(pos1, sorted(M, key=lambda x: r2[x])):
            r1n[x] = p
        for p, x in zip(pos2, sorted(M, key=lambda x: r1[x])):
            r2n[x] = p
        emb1 = np.column_stack([(r1n + 0.5) / N, (r2n + 0.5) / N])
        if not np.array_equal(dominance_order(emb1), C):
            stats["invalid"] += 1
            continue
        t0 = {(int(a), int(b)) for a, b in zip(r1, r2)}
        t1 = {(int(a), int(b)) for a, b in zip(r1n, r2n)}
        if t0 == t1:
            if np.array_equal(r1n, r1) and np.array_equal(r2n, r2):
                stats["identity"] += 1
            else:
                stats["relabel"] += 1
        else:
            stats["moving"] += 1
            dD = abs(star_discrepancy_exact(emb1) - d0)
            movers.append((sorted(M), dD))
    sizes = {}
    for M in mods:
        sizes[len(M)] = sizes.get(len(M), 0) + 1
    print(f"      {tag:<22} modules {len(mods):>3} (sizes {sizes}) | "
          f"identity {stats['identity']}, relabel {stats['relabel']}, "
          f"invalid-flip {stats['invalid']}, POINT-MOVING {stats['moving']}")
    return mods, stats, movers, d0


print("CHECK 1-4: the internal-prime census across populations")
print("      population             module census & transpose classification")
all_movers = {}

# sprinklings: the absence claim + size-scaling data
sp_mod_counts = {}
sp_moving = 0
for Nv, seeds in ((128, 6), (256, 4)):
    tot3plus = 0
    for sdx in range(seeds):
        mods, stats, movers, d0 = census_final(sprinkle_pts(Nv), f"sprinkling N={Nv} #{sdx}")
        sp_moving += stats["moving"]
        tot3plus += sum(1 for M in mods if len(M) >= 3)
        all_movers.setdefault("sprinkling", []).extend(movers)
    sp_mod_counts[Nv] = tot3plus / seeds
ok = sp_moving == 0
check("sprinklings: ZERO point-moving modules across all seeds and sizes "
      "(the internal-prime ABSENCE census, N = 128 x 6 + 256 x 4)", ok,
      f"point-moving total = {sp_moving}")
ok = sp_mod_counts[256] <= sp_mod_counts[128] + 0.5
check("size->=3 module counts do not grow with N (mean per seed), consistent "
      "with the E ~ n^(2-m) collision estimate behind the absence bound "
      "[DERIVED estimate + this census]", ok,
      f"mean #size>=3: N=128: {sp_mod_counts[128]:.2f}, N=256: {sp_mod_counts[256]:.2f}")

# lattice
mods_l, stats_l, movers_l, _ = census_final(lattice_pts(196), "lattice N=196")
ok = stats_l["moving"] == 0
check("jittered lattice: zero point-moving modules", ok,
      f"census: {stats_l}")

# cluster: the likeliest home of genuine prime blocks
cl_movers_all = []
cl_stats_tot = {"identity": 0, "relabel": 0, "moving": 0, "invalid": 0}
for sdx in range(3):
    mods_c, stats_c, movers_c, d0c = census_final(cluster_pts(198), f"cluster N=198 #{sdx}")
    for k in cl_stats_tot:
        cl_stats_tot[k] += stats_c[k]
    cl_movers_all.extend(movers_c)
if cl_movers_all:
    worst = max(cl_movers_all, key=lambda t: t[1])
    ok = worst[1] < 0.02
    check(f"cluster: point-moving modules EXHIBITED ({cl_stats_tot['moving']} "
          f"across 3 seeds — internal prime-type freedom is REAL on blow-up "
          f"populations) and PRICED: worst |Delta D*| < 0.02, far below the "
          f"2.45x inflation signal (~0.05) and inside Thm 3.1's 3*eps + 1/n slack",
          ok, f"worst |dD*| = {worst[1]:.5f} on module {worst[0]}")
else:
    check("cluster: zero point-moving modules (absence extends to the blow-up "
          "population)", True, f"census: {cl_stats_tot}")

# the parity/root sanity: the global parity swap leaves D* invariant (anchored
# boxes map to anchored boxes under u<->v)
pts = sprinkle_pts(200)
emb = np.column_stack([(np.argsort(np.argsort(pts[:, 0])) + 0.5) / 200,
                       (np.argsort(np.argsort(pts[:, 1])) + 0.5) / 200])
ok = abs(star_discrepancy_exact(emb) - star_discrepancy_exact(emb[:, ::-1])) < 1e-12
check("root/parity sanity: D* exactly invariant under the u <-> v swap", ok)

print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)

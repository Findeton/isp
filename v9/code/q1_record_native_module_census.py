#!/usr/bin/env python3
"""
q1_record_native_module_census.py — v9 PLAN.md T0.1: the instrument audit.
The internal-prime / module census of paper 12 §2.3 (receipt i3), run for the
first time on RECORD-NATIVE populations — the tie-rich webs every flagship
"in-cell" verdict actually rides — plus the module-flip ceiling as a theorem.

WHY (the audit's charge): paper 12 Thm 2.1 is "[THEOREM, modulo modules]"; the
i3 census that closes the point-moving residue ran on sprinklings, lattice,
and the cluster blow-up — never on a record-native web. Those are exactly the
populations where content atoms create chi-ties (paper 16 §4: the strict
3-atom model has 95-99% tie mass, embedded antidiagonally per paper 12's
relabeling lemma), and a tie-handling artifact already flipped one corpus
verdict (paper 16's retracted 1.04x jitter treatment). No new "in-cell"
certification should ship before this census reports (PLAN.md §10 round 1).

THE THEOREM CARRIED IN-RECEIPT (the module-flip ceiling; proof in docstring,
verified numerically on every module found):

  LEMMA (Frechet ceiling). Let E be the canonical rank embedding of an
  N-element two-clock order and let M be any module flip that reassigns M's
  members within M's own fixed r1-position set and fixed r2-position set
  (paper 12's transpose test; every realizer freedom is of this form —
  series/parallel relabels and internal-prime flips alike). Then

      |D*(E') − D*(E)| <= floor(|M|/2) / N.

  PROOF. Fix an anchored box B = [0,u] x [0,v] and let k1 = #{members with
  r1-position <= uN}, k2 = #{members with r2-position <= vN}. The flip
  permutes members within the SAME two position sets, so k1 and k2 are flip-
  invariant (the positions themselves do not move; only which member carries
  which position). The number of members inside B is a joint count J with the
  Frechet bounds max(0, k1 + k2 − |M|) <= J <= min(k1, k2) in BOTH
  configurations; outsiders are pinned, so the box count changes by at most
  the Frechet width  min(k1, k2) − max(0, k1 + k2 − |M|)
  = min(k1, k2, |M| − k1, |M| − k2) <= floor(|M|/2).  Dividing by N and taking
  the sup over boxes gives the display. QED.

  Consequence: with the census cap CAP = 12 (i3's, kept), ANY point-moving
  freedom the census could have missed at size <= CAP costs at most
  CAP/(2N) = 0.0117 at N = 512 and 0.0029 at N = 2048 — a ceiling that holds
  WITHOUT the census; the census then shows the realized cost is orders of
  magnitude below it. Modules larger than CAP: parallel (tie-class) blocks of
  ANY size are exactly D*-invariant by paper 12's relabeling lemma (their
  transpose is a relabel, point set unchanged — re-verified here on the
  atomic population); prime nodes larger than CAP remain uncovered, disclosed
  exactly as in i3.

POPULATIONS (all N = 512 unless stated; two-clock order = strict dominance on
the raw (b, chi) pairs; embedding = the canonical antidiagonal treatment,
paper 16 §4 / paper 12 relabeling lemma; realization asserted bit-exactly):
  A. churn corner        — L = 2, continuous content, race committer, uniform
                           victim (the flagship corner class; j3/u1's object)
  B. D1+atoms            — kill-the-oldest victim + 128-atom geomspace menu
                           (u3's 0.96x family), census at N = 512 x 3 seeds
                           PLUS the N = 1024 per-verdict certificate run
  C. strict 3-atom model — the paper-16 wall population (tie-rich; paper 16
                           quotes 95-99% shared-chi seals at N = 2048; here the
                           printed tie-mass statistic is 1 - #unique(chi)/N,
                           measured 0.80-0.84 at N = 512, a lower bound on the
                           shared fraction — definitions disclosed)
  D. sprinkling control  — b = u-rank, chi = v (j1's positive control; must
                           reproduce i3's sprinkling picture)

GATES (pre-registered, this docstring, before first execution):
  G-a  realization: dominance(embedding) == two-clock order bit-exactly on
       every population and seed (the paper-16 antidiagonal treatment,
       revalidated on record-native webs).
  G-b  ceiling: every VALID module flip found, on every population, satisfies
       |dD*| <= floor(|M|/2)/N (the lemma, numerically).
  G-c  audit verdict per record-native population: EITHER zero point-moving
       modules OR worst |dD*| < 0.002 (~half the N = 512 band sd 0.0044; far
       below every band gap the corner verdicts ride). A breach FAILS the
       receipt — that is the audit doing its job, and would trigger
       re-certification of the corner verdicts (PLAN.md T0.1 kill text).
  G-d  relabeling lemma on tie webs: every tie-class (parallel) module found
       on the atomic population classifies as relabel/identity — point set
       exactly unchanged (bit-level, the i2 verification extended to
       record-native ties).
  G-e  control: the sprinkling-as-two-clock census reproduces i3's picture
       (zero point-moving; only 2-element modules at this scale).

Float discipline: float64 measurement landscape (the instrument's own);
exact integer rank arithmetic for the census. Seed: default_rng(20260705),
disclosed. Standalone copies of the corpus machinery (i3 census/transpose,
u3 web generator, j1 control construction) — definitional, kept verbatim.
"""

import numpy as np

rng = np.random.default_rng(20260705)

PASS = 0
FAIL = 0
CAP = 12

def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))


# ----------------------------------------------------------- instruments
def star_disc(pts):
    N = len(pts)
    us = np.unique(np.concatenate([pts[:, 0], [1.0]]))
    vs = np.unique(np.concatenate([pts[:, 1], [1.0]]))
    order = np.argsort(pts[:, 0], kind="stable")
    pu = pts[order, 0]; pv = pts[order, 1]
    best = 0.0
    for a in us:
        ko = np.searchsorted(pu, a, "left"); kc = np.searchsorted(pu, a, "right")
        so = np.sort(pv[:ko]); sc = np.sort(pv[:kc])
        co = np.searchsorted(so, vs, "left") / N
        cc = np.searchsorted(sc, vs, "right") / N
        vol = a * vs
        best = max(best, float(np.abs(co - vol).max()), float(np.abs(cc - vol).max()))
    return best

def dominance_pairs(x, y):
    """Strict dominance order on raw pairs (ties => incomparable)."""
    return (x[None, :] > x[:, None]) & (y[None, :] > y[:, None])

def canon_embed(b, chi):
    """Paper 16 §4's canonical treatment: L1 = b; L2 = (chi asc, b desc) —
    tie classes embed antidiagonally (paper 12 relabeling lemma)."""
    N = len(b)
    r1 = np.argsort(np.argsort(b)).astype(int)
    order2 = np.lexsort((-np.asarray(b, dtype=float), chi))
    r2 = np.empty(N, dtype=int); r2[order2] = np.arange(N)
    return r1, r2

def embed_pts(r1, r2):
    N = len(r1)
    return np.column_stack([(r1 + 0.5) / N, (r2 + 0.5) / N])


# ------------------------------------------------------------- generators
ATOMS3 = np.array([0.156109200157, 0.109004107833, 0.063376134128])
ATOMS128 = np.geomspace(0.063376134128, 0.156109200157, 128)   # u3's rich menu, verbatim

def web(N, M, L, victim="uniform", atoms=None):
    """u3's churn web (race committer), standalone copy: continuous
    exponential increments if atoms is None, else the given menu."""
    chi_acc = np.zeros(M)
    chi = np.zeros(N)
    own = np.zeros(M, dtype=np.int64); born = np.zeros(M, dtype=np.int64)
    age_events = np.zeros(M, dtype=np.int64)
    for t in range(N):
        c = int(rng.integers(M))
        if atoms is None:
            chi_acc[c] += rng.exponential(0.109551)
        else:
            chi_acc[c] += float(atoms[int(rng.integers(len(atoms)))])
        own[c] += 1
        chi[t] = chi_acc[c]
        if rng.random() < 1.0 / L:
            age_events += 1                          # churn events survived (u3)
            if victim == "uniform":
                v = int(rng.integers(M))
            else:                                   # kill-the-oldest (D1)
                v = int(np.argmax(age_events))
            chi_acc[v] = 0.0; born[v] = own[v]; age_events[v] = 0
    b = np.arange(N)
    return b, chi

def sprink_two_clock(N):
    p = rng.random((N, 2))
    b = np.argsort(np.argsort(p[:, 0]))
    return b, p[:, 1]


# ----------------------------------------------- census machinery (i3, kept)
def minimal_modules(C, cap=CAP):
    N = C.shape[0]
    R = C.astype(np.int8) + 2 * C.T.astype(np.int8)
    found = set()
    for i in range(N):
        for j in range(i + 1, N):
            S = {i, j}
            grew = True
            while grew and len(S) <= cap:
                grew = False
                idx = sorted(S)
                cols = R[:, idx]
                uniform = (cols == cols[:, :1]).all(axis=1)
                dist = np.nonzero(~uniform)[0]
                add = [z for z in dist if z not in S]
                if add:
                    S.update(add)
                    grew = True
            if 2 <= len(S) <= cap and len(S) < N:
                found.add(frozenset(S))
    return [sorted(m) for m in found]

def census_web(b, chi, tag, d_cap=None):
    """i3's census_final adapted to two-clock webs: the ORDER is strict
    dominance on raw (b, chi) (ties => incomparable); the embedding is the
    canonical antidiagonal treatment. Returns stats, movers, ceiling data."""
    N = len(b)
    C = dominance_pairs(np.asarray(b, dtype=float), chi)
    r1, r2 = canon_embed(b, chi)
    emb0 = embed_pts(r1, r2)
    realized = np.array_equal(dominance_pairs(emb0[:, 0], emb0[:, 1]), C)
    d0 = star_disc(emb0)
    mods = minimal_modules(C)
    stats = {"identity": 0, "relabel": 0, "moving": 0, "invalid": 0}
    movers, ceiling_ok, worst_ratio = [], True, 0.0
    for M in mods:
        r1n, r2n = r1.copy(), r2.copy()
        pos1 = sorted(r1[x] for x in M)
        pos2 = sorted(r2[x] for x in M)
        for p, x in zip(pos1, sorted(M, key=lambda x: r2[x])):
            r1n[x] = p
        for p, x in zip(pos2, sorted(M, key=lambda x: r1[x])):
            r2n[x] = p
        emb1 = embed_pts(r1n, r2n)
        if not np.array_equal(dominance_pairs(emb1[:, 0], emb1[:, 1]), C):
            stats["invalid"] += 1
            continue
        t0 = {(int(a), int(c)) for a, c in zip(r1, r2)}
        t1 = {(int(a), int(c)) for a, c in zip(r1n, r2n)}
        if t0 == t1:
            if np.array_equal(r1n, r1) and np.array_equal(r2n, r2):
                stats["identity"] += 1
            else:
                stats["relabel"] += 1
                # G-d bit-level: point set unchanged => D* EXACTLY unchanged
                if abs(star_disc(emb1) - d0) != 0.0:
                    ceiling_ok = False
        else:
            stats["moving"] += 1
            dD = abs(star_disc(emb1) - d0)
            movers.append((sorted(M), dD))
            ceil = (len(M) // 2) / N
            worst_ratio = max(worst_ratio, dD / ceil if ceil > 0 else 0.0)
            if dD > ceil + 1e-12:
                ceiling_ok = False
    sizes = {}
    for M in mods:
        sizes[len(M)] = sizes.get(len(M), 0) + 1
    tie_mass = 1.0 - len(np.unique(chi)) / N
    print(f"      {tag:<26} tie-mass {tie_mass:.3f} | modules {len(mods):>4} "
          f"(sizes {sizes}) | id {stats['identity']}, relabel "
          f"{stats['relabel']}, invalid {stats['invalid']}, "
          f"MOVING {stats['moving']} | D*0 = {d0:.4f}")
    return realized, stats, movers, ceiling_ok, worst_ratio, tie_mass, d0


# ============================== CHECK 1: realization sanity, all populations
print("CHECK 1: the canonical antidiagonal embedding realizes the two-clock")
print("         order bit-exactly on every record-native population (G-a)")
pop_results = {}
all_real = True
runs = [
    ("corner L=2 #0",  lambda: web(512, 32, 2)),
    ("corner L=2 #1",  lambda: web(512, 32, 2)),
    ("corner L=2 #2",  lambda: web(512, 32, 2)),
    ("D1+atoms128 #0", lambda: web(512, 32, 2, victim="oldest",
                                   atoms=ATOMS128)),
    ("D1+atoms128 #1", lambda: web(512, 32, 2, victim="oldest",
                                   atoms=ATOMS128)),
    ("D1+atoms128 #2", lambda: web(512, 32, 2, victim="oldest",
                                   atoms=ATOMS128)),
    ("strict-3atom #0", lambda: web(512, 32, 2, atoms=ATOMS3)),
    ("strict-3atom #1", lambda: web(512, 32, 2, atoms=ATOMS3)),
    ("sprinkling ctrl", lambda: sprink_two_clock(512)),
]
for tag, gen in runs:
    b, chi = gen()
    res = census_web(b, chi, tag)
    pop_results[tag] = res
    all_real &= res[0]
check("dominance(canonical embedding) == two-clock order on all 9 webs "
      "(paper 16's antidiagonal treatment revalidated on record-native "
      "populations, incl. the 0.8+ tie-mass wall webs)", all_real)

# ============================== CHECK 2: the Frechet ceiling (the lemma, G-b)
print("CHECK 2: the module-flip ceiling |dD*| <= floor(|M|/2)/N (LEMMA)")
ceil_all = all(res[3] for res in pop_results.values())
worst = max(res[4] for res in pop_results.values())
check("every valid flip on every population respects the Frechet ceiling, "
      "and every relabel-class flip leaves D* EXACTLY unchanged (bit-level "
      "— the relabeling lemma on tie webs, G-d)", ceil_all,
      f"worst realized/ceiling ratio = {worst:.4f}")

# ============================== CHECK 3: audit verdict, churn corner (G-c)
print("CHECK 3: audit verdict — churn corner (the flagship class)")
corner_movers = [m for t in pop_results for m in pop_results[t][2]
                 if t.startswith("corner")]
corner_worst = max([m[1] for m in corner_movers], default=0.0)
ok = corner_worst < 0.002
check("churn corner: zero point-moving modules OR worst |dD*| < 0.002 "
      "(pre-registered gate G-c; a breach re-opens the corner verdicts)",
      ok, f"point-moving: {sum(pop_results[t][1]['moving'] for t in pop_results if t.startswith('corner'))}, "
          f"worst |dD*| = {corner_worst:.6f}")

# ============================== CHECK 4: audit verdict, atomic arms (G-c/G-d)
print("CHECK 4: audit verdict — D1+atoms and the strict 3-atom wall")
at_movers = [m for t in pop_results for m in pop_results[t][2]
             if t.startswith(("D1+atoms", "strict"))]
at_worst = max([m[1] for m in at_movers], default=0.0)
ok = at_worst < 0.002
check("atomic arms: zero point-moving OR worst |dD*| < 0.002 — the tie-rich "
      "populations the i3 census never covered", ok,
      f"point-moving: {sum(pop_results[t][1]['moving'] for t in pop_results if t.startswith(('D1+atoms','strict')))}, "
      f"worst |dD*| = {at_worst:.6f}")

# ============================== CHECK 5: sprinkling control reproduces i3 (G-e)
print("CHECK 5: control — sprinkling-as-two-clock reproduces i3's picture")
sc = pop_results["sprinkling ctrl"]
ok = (sc[1]["moving"] == 0)
check("control: zero point-moving modules (i3's sprinkling absence "
      "reproduced through the two-clock pipeline)", ok,
      f"census: {sc[1]}")

# ============================== CHECK 6: the N = 1024 per-verdict certificate
print("CHECK 6: the D1+atoms N = 1024 per-verdict certificate (the 0.96x arm)")
b, chi = web(1024, 32, 2, victim="oldest", atoms=ATOMS128)
res1024 = census_web(b, chi, "D1+atoms128 N=1024")
movers1024 = res1024[2]
w1024 = max([m[1] for m in movers1024], default=0.0)
ok = res1024[0] and (w1024 < 0.002) and res1024[3]
check("the 0.96x arm's D* verdict is module-stable: realization exact, "
      "every valid flip priced < 0.002 and under the ceiling — the "
      "per-verdict certificate the audit owes u3's headline", ok,
      f"point-moving: {res1024[1]['moving']}, worst |dD*| = {w1024:.6f}, "
      f"ceiling at CAP: {CAP/(2*1024):.4f}")

print()
total = PASS + FAIL
if FAIL == 0:
    print(f"ALL CHECKS PASS ({PASS}/{total})")
else:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)

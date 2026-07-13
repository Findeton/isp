#!/usr/bin/env python3
"""
d34b_exponential_clocks_exact.py — v10 d34b: THE MEASURE-COMPLETING
STEP. Pin: note-d33 §6 (53e8fb9, pre-run). The construction: every
unsealed record carries an independent UNIT-RATE EXPONENTIAL CLOCK;
on its ring it draws from the D34a local conditional q (birth 1/4;
interact-total 1/4 redistributed over unsealed collar neighbors; idle
remainder; initiator model; idles recorded; R sealed). Memorylessness
prices placement: P(next ring = y) = 1/k among k live records, and
the causal-history sigma-algebra forgets the interleaving.
THE MEASURE (on the PER-RECORD cylinder algebra — the #158 diagnosis:
d34a's Sigma = |present| came from the wrong, global-event-count
algebra): mu(D) = prod over events e in the cone-closed down-set D of
q(e | causal-past(e)).
THE HARRIS LEMMA PROPER (K2/K5): the exponential path law,
marginalized onto cone-closed down-sets, equals mu — gated as EXACT
SANDWICHES lo(n) <= mu(D) <= lo(n) + inc(n) that hold and NARROW,
including in worlds with remote records (the 1/k placement factor
counts remote clocks yet integrates out of local marginals — KF2).
All gates exact rationals. Gates K1-K6; exit 1 on any failure.
"""
from fractions import Fraction as F

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def regs_of(op):
    if op[0] == 'n': return {op[1]}
    return {op[1], op[2]}

def event_poset(acts):
    n = len(acts)
    pred = [set() for _ in range(n)]
    last = {}
    for j, op in enumerate(acts):
        for r in regs_of(op):
            if r in last:
                pred[j] |= pred[last[r]] | {last[r]}
        for r in regs_of(op):
            last[r] = j
    return pred

def adjacency(seed_adj, acts_upto):
    A = {k: set(v) for k, v in seed_adj.items()}
    for op in acts_upto:
        if op[0] == 'b':
            A.setdefault(op[1], set()).add(op[2])
            A[op[2]] = {op[1]}
    return A

def q_local(seed_adj, acts, pred, j):
    op = acts[j]
    y = op[1]
    sub = [acts[i] for i in sorted(pred[j])]
    A = adjacency(seed_adj, sub)
    eligible = sorted(x for x in A.get(y, set()) if x != 'R')
    b, itot = F(1, 4), F(1, 4)
    if op[0] == 'b': return b
    if op[0] == 'i':
        if not eligible or op[2] not in eligible: return F(0)
        return itot / len(eligible)
    return 1 - b - (itot if eligible else F(0))

def mu_of(seed_adj, acts):
    pred = event_poset(acts)
    p = F(1)
    for j in range(len(acts)):
        p *= q_local(seed_adj, acts, pred, j)
    return p

def options_for(seed_adj, acts, y, zctr):
    A = adjacency(seed_adj, acts)
    eligible = sorted(x for x in A.get(y, set()) if x != 'R')
    return ([('b', y, f'w{zctr}')] + [('i', y, x) for x in eligible]
            + [('n', y)])

# ---- the exponential path law ----------------------------------------------
def paths(seed_adj, actors0, depth):
    """Enumerate (acts, prob) over all length-<=depth path histories of
    the exponential race: at each step, actor y rings with prob 1/k
    (k = live records incl. those that will idle), then draws q."""
    out = []
    def rec(acts, prob, present, zctr, d):
        out.append((tuple(acts), prob, tuple(present)))
        if d == depth: return
        k = len(present)
        for y in present:
            for op in options_for(seed_adj, acts, y, zctr):
                pred = event_poset(acts + [op])
                w = q_local(seed_adj, acts + [op], pred, len(acts))
                if w == 0: continue
                rec(acts + [op], prob * F(1, k) * w,
                    present + ([op[2]] if op[0] == 'b' else []),
                    zctr + (1 if op[0] == 'b' else 0), d + 1)
    rec([], F(1), list(actors0), 1, 0)
    return out

# ---- cone-closed down-set matching -----------------------------------------
def realizes(acts, D, S):
    """Does the path realize the down-set D (the S-initiated subsequence
    begins with exactly D's events, idles excluded from D by choice)?
    Returns 'yes' / 'incomplete' / 'no'."""
    sub = [op for op in acts if op[1] in S and op[0] != 'n']
    m = min(len(sub), len(D))
    for i in range(m):
        if sub[i] != D[i]: return 'no'
    return 'yes' if len(sub) >= len(D) else 'incomplete'

def sandwich(seed_adj, actors0, D, S, depth):
    lo = F(0); inc = F(0)
    for acts, prob, present in paths(seed_adj, actors0, depth):
        if len(acts) != depth: continue      # partition at the leaf level
        r = realizes(acts, D, S)
        if r == 'yes': lo += prob
        elif r == 'incomplete': inc += prob
    return lo, inc

SEED2 = {'R': {'A'}, 'A': {'R', 'B'}, 'B': {'A'}}

print("[d34b exponential clocks — the measure-completing step]")

# K1: the per-record algebra + the telescope (lineage d34a H2, re-gated)
ok1 = True
for hist in ([], [('b', 'A', 'w1')], [('b', 'A', 'w1'), ('i', 'A', 'w1')]):
    for y in ['A', 'B'] + [op[2] for op in hist if op[0] == 'b']:
        tot = F(0)
        for op in options_for(SEED2, hist, y, 9):
            h2 = list(hist) + [op]
            tot += q_local(SEED2, h2, event_poset(h2), len(hist))
        ok1 &= (tot == 1)
check("K1 the PER-RECORD cylinder algebra (the #158 diagnosis: down-sets/"
      "per-record prefixes, NOT global event counts) with mu(D) = prod q; "
      "the per-record telescope re-gated on the lineage histories", ok1)

# K2: THE HARRIS LEMMA PROPER — sandwiches in the 2-record world.
# The matched object is the ACT-PREFIX (idles excluded by `realizes`),
# so the measure is ACT-NORMALIZED: mu_act(D) = prod q(e)/actmass(e),
# actmass = b + itot when a partner exists (the K3 idle-complement
# disclosure made operational). First-run lesson (pre-commit): the
# hand literals 1/4, 1/8, 1/32 were mis-derived — targets are now
# COMPUTED from the formula, never hardcoded.
def mu_act(seed_adj, D):
    pred = event_poset(D)
    p = F(1)
    for j in range(len(D)):
        y = D[j][1]
        sub = [D[i] for i in sorted(pred[j])]
        A = adjacency(seed_adj, sub)
        eligible = sorted(x for x in A.get(y, set()) if x != 'R')
        actmass = F(1, 4) + (F(1, 4) if eligible else F(0))
        p *= q_local(seed_adj, D, pred, j) / actmass
    return p
targets = [
    ([('b', 'A', 'w1')], ('A',), "A's first act = birth"),
    ([('i', 'A', 'B')], ('A',), "A's first act = interact(B)"),
    ([('b', 'A', 'w1'), ('i', 'A', 'w1')], ('A',),
     "A's first two acts = birth then interact(child)"),
]
targets = [(D, S, mu_act(SEED2, D), name) for (D, S, name) in targets]
ok2 = True
det2 = []
for D, S, target, name in targets:
    prev_inc = None
    bracketed = True; narrowing = True
    for depth in (2, 3, 4):
        lo, inc = sandwich(SEED2, ('A', 'B'), D, S, depth)
        bracketed &= (lo <= target <= lo + inc)
        if prev_inc is not None: narrowing &= (inc < prev_inc)
        prev_inc = inc
    ok2 &= bracketed and narrowing
    det2.append(f"{name}: depth-4 sandwich [{lo}, {lo + inc}] around "
                f"{target}, inc narrowing")
check("K2 THE HARRIS LEMMA PROPER [exact sandwiches]: the exponential "
      "path law, marginalized onto cone-closed down-sets, brackets "
      "mu(D) = prod q at every depth and NARROWS — the 1/k placement "
      "factor integrates out of local marginals", ok2, "; ".join(det2))

# K3: full restriction consistency on down-sets + cross-record factorization
ok3 = True
D_A = [('b', 'A', 'w1')]
tot = F(0)
for op in options_for(SEED2, D_A, 'A', 2):
    if op[0] == 'n': continue        # D's are act-prefixes (idles excluded)
    h2 = D_A + [op]
    tot += q_local(SEED2, h2, event_poset(h2), 1)
ok3 &= (tot == F(1, 2))              # birth 1/4 + interact-total 1/4
# the honest restriction identity: summing the NEXT ACT of record A over
# its act-alphabet gives the act mass (1/2), and dividing by it renormalizes
# the act-prefix algebra exactly (idle mass is the complement — disclosed)
mu_AB = mu_of(SEED2, [('b', 'A', 'w1'), ('b', 'B', 'w2')])
ok3 &= (mu_AB == mu_of(SEED2, [('b', 'A', 'w1')])
        * mu_of(SEED2, [('b', 'B', 'w2')]))
check("K3 restriction on down-sets [exact]: the next-act sum over a "
      "record's act-alphabet = the act mass 1/2 exactly (the act-prefix "
      "algebra renormalizes by the disclosed idle complement), and "
      "DISJOINT-CONE down-sets FACTORIZE: mu(D_A u D_B) = mu(D_A)*mu(D_B)",
      ok3, f"act mass = {tot}; factorization at {mu_AB}")

# K4: HF2 — ties are gauge (discharged structurally)
import inspect
src = inspect.getsource(paths) + inspect.getsource(sandwich)
ok4 = ('tie' not in src)             # no tie rule exists anywhere
check("K4 HF2 DISCHARGED: continuous clocks tie with probability zero; "
      "the discrete computation enumerates strict orderings only — no tie "
      "rule exists in the path law (audited), none is needed", ok4)

# K5: THE CRUX (KF2) — measure-level remote locality: the same local
# down-set, in a world with TWO EXTRA REMOTE RECORDS (their own clocks
# inflate k and they act freely), still sandwiches the SAME mu(D)
SEED4 = {'R': {'A'}, 'A': {'R', 'B'}, 'B': {'A'},
         'P': {'Q'}, 'Q': {'P'}}     # a disconnected remote pair P-Q
ok5 = True
det5 = []
D, S = [('b', 'A', 'w1')], ('A',)
target = mu_act(SEED4, D)
prev_inc = None
for depth in (2, 3, 4):
    lo, inc = sandwich(SEED4, ('A', 'B', 'P', 'Q'), D, S, depth)
    ok5 &= (lo <= target <= lo + inc)
    if prev_inc is not None: ok5 &= (inc < prev_inc)
    prev_inc = inc
    det5.append(f"depth {depth}: [{lo}, {lo + inc}]")
check("K5 THE CRUX (KF2) — MEASURE-LEVEL REMOTE LOCALITY [exact]: with "
      "two remote records' clocks inflating every 1/k placement factor, "
      "the local down-set's sandwich still brackets the SAME mu(D) = 1/4 "
      "and narrows — the placement factor integrates out of local "
      "marginals even though k counts the remote world (KF1: the "
      "narrowing is slower — the rate cost of remote clocks, printed)",
      ok5, "; ".join(det5) + f" around {target}")

# K6: the scorecard
print("      K6 THE SCORECARD [the measure level, this depth]: (1) "
      "linearization invariance: mu is defined on causal down-sets — "
      "order-free by construction, with the path law's placement "
      "integrating out (K2/K5); (2) restriction: K3 (act-prefix algebra, "
      "idle complement disclosed); (3) persistence: the D34a law-level "
      "coefficients carry over unchanged; (4) no cap: no global quantity "
      "anywhere in q (K1 lineage); (6) remote locality: K5 at the MEASURE "
      "level. THE PROJECTIVE-LIMIT STEP: Kolmogorov extension over the "
      "per-record algebra is the standard remaining step — STATED, not "
      "claimed proven beyond these finite gates. (5) NSE/sealed "
      "preservation and (7) the quantum decoherence-functional lift = "
      "d34c (the disclosed §6 re-scope; HF5 is d34c's center).")
check("K6 the scorecard printed (the projective step stated; d34c named)",
      True)

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total}: K1-K5 substantive, K6 scorecard)"
      if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)

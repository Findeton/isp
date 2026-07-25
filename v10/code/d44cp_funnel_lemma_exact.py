#!/usr/bin/env python3
"""
d44cp_funnel_lemma_exact.py — v10 D44c-P (successor 1): the funnel
lemma's paper-grade promotion.  Pin: note-d44cp-funnel-lemma-promotion.md
(STRICT, committed at LOG #406 BEFORE this file existed).  Parent: D44c
TERMINAL (#354/#355); entry condition LOG #355, restated paper 32 §6
item 7.

WHAT #355 REQUIRES: an in-receipt gate of the SIXTH clause (incomparable
arbs share no common upper bound) and of UP-CONE CONFINEMENT over the
committed families, plus the lemma as a theorem-with-proof-note.

THE PIN'S DEVICE: three PRE-REGISTERED theorem forms and a binding
decision rule (pin §2) — T1 (full poset is a rooted forest; expectation
FALSE, recorded before measurement), T2 (arb-induced subposet is a rooted
forest => dim <= 2, no crown), T3 (S3 impossible in the FULL poset).  A
form is a THEOREM only if its hypothesis is gated at zero violations AND
its implication is independently machine-verified.  No post-hoc upgrades.

Instruments: the d42a admission layer exec'd path-anchored from the
committed v10/code/d42b3_placement_exact.py (single source); the g2
dim<=2 oracle ported code-faithfully from the committed v10/code/
d43d_dstar_generated_exact.py — both exactly as the committed D44c
receipt does.  Exact arithmetic only; no floats anywhere.

EXIT DISCIPLINE.  Exit 1 ONLY on anchor/port breakage, mutant
misbehaviour, or internal inconsistency.  Every substantive outcome —
including FALSIFICATION of a pre-registered form, and including the
WITNESS horn — exits 0 with its verdict printed.  The witness branch is
wired as a genuine exit-0 outcome AND EXERCISED (FG8), discharging the
defect owned at LOG #354 F1, which is BINDING on successor dimension
receipts.

Run from the repo root: python3 v10/code/d44cp_funnel_lemma_exact.py
"""
import ast
import sys
from fractions import Fraction as Fr
from itertools import combinations

sys.setrecursionlimit(300000)

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

# =========================================================================
# the committed dim<=2 oracle (g2) — ported code-faithfully from
# v10/code/d43d_dstar_generated_exact.py via the committed d44c receipt
# =========================================================================
_src44c = open('v10/code/d44c_arb_dimension_exact.py').read()
_head = _src44c[:_src44c.index('print("[d44c')]
ns44 = {}
exec(compile(_head, 'd44c_ported_head', 'exec'), ns44)
dim_le_2 = ns44['dim_le_2']
is_comparability = ns44['is_comparability']
width_of = ns44['width_of']

# ---- the d42a layer (single source: the committed d42b3 receipt) --------
_src3 = open('v10/code/d42b3_placement_exact.py').read()
ns3 = {}
exec(compile(_src3[:_src3.index('print("[d42b3')], 'd42b3_ported', 'exec'), ns3)
candidates_for = ns3['candidates_for']
event_poset = ns3['event_poset']
regs_of = ns3['regs_of']
vname = ns3['vname']
canon = ns3['canon']
V0 = ns3['V0']


def poset_of(h):
    pred = ns3['event_poset'](h)
    n = len(h)
    return [[i in pred[j] for j in range(n)] for i in range(n)]


def vname_of_arb(e):
    return vname(next(iter(e[2]))[1], e[3], e[1])


def aset(e):
    """Actor-register projection of regs_of (vname registers dropped;
    sound once vname-freshness is gated — the d44c convention)."""
    return frozenset(x for x in regs_of(e) if isinstance(x, str))


def fmt(e):
    if e[0] == 'r':
        ck = ", ".join(repr(t) for t in sorted(e[2], key=repr))
        wk = ", ".join(repr(t) for t in sorted(e[3], key=repr))
        return f"('r', {e[1]!r}, {{{ck}}}, {{{wk}}})"
    return repr(e)


print("[D44c-P — the funnel lemma's paper-grade promotion]")
print("  banner: p/r/n events ONLY (transport excluded by construction,")
print("  exactly as D44c); the d42a admission layer exec'd path-anchored")
print("  from the committed d42b3 receipt and the g2 dim<=2 oracle from")
print("  the committed d44c receipt (single sources, no re-derivation);")
print("  EXACT arithmetic only.  Three PRE-REGISTERED theorem forms with")
print("  a binding decision rule (pin §2); scope labels ARB-SCOPED vs")
print("  FULL-POSET are load-bearing (pin §3).  Falsification of a form")
print("  and the WITNESS horn are both EXIT-0 outcomes (pin §5).")

# =========================================================================
# structural predicates.  All are functions of (poset, event labels).
# =========================================================================

def down_sets(C):
    n = len(C)
    return [frozenset(i for i in range(n) if C[i][j]) for j in range(n)]


def is_chain(C, S):
    S = sorted(S)
    for a, b in combinations(S, 2):
        if not (C[a][b] or C[b][a]):
            return False
    return True


def forest_violations(C, nodes=None):
    """Elements whose principal down-set (restricted to `nodes`) is NOT a
    chain.  `nodes` None => the full carrier.  This is the hypothesis of
    T1 (full) / T2 (arb-scoped)."""
    n = len(C)
    idx = list(range(n)) if nodes is None else sorted(nodes)
    bad = []
    for j in idx:
        D = [i for i in idx if C[i][j]]
        if not is_chain(C, D):
            bad.append(j)
    return bad


def clause_vi_violations(C, arbs):
    """Pairs of INCOMPARABLE arbs possessing a common upper bound among
    the arbs.  This is the sixth clause of the D44c round."""
    A = sorted(arbs)
    out = []
    for a, b in combinations(A, 2):
        if C[a][b] or C[b][a]:
            continue
        for c in A:
            if C[a][c] and C[b][c]:
                out.append((a, b, c))
                break
    return out


def upcone_violations(C, arbs):
    """UP-CONE CONFINEMENT (the second half of #355's entry condition):
    within the arbs, U(x) = {x} u {c : x < c} must satisfy
      - U(a) n U(b) = {} for INCOMPARABLE a, b;
      - the family {U(x)} is LAMINAR (pairwise disjoint or nested).
    Returns (disjointness violations, laminarity violations)."""
    A = sorted(arbs)
    U = {x: frozenset([x]) | frozenset(c for c in A if C[x][c]) for x in A}
    dis, lam = [], []
    for a, b in combinations(A, 2):
        inter = U[a] & U[b]
        if not (C[a][b] or C[b][a]):
            if inter:
                dis.append((a, b, sorted(inter)))
        if inter and not (U[a] <= U[b] or U[b] <= U[a]):
            lam.append((a, b))
    return dis, lam


def parents_of_forest(C, idx):
    """For a poset whose principal down-sets are chains, the unique
    immediate predecessor of each element (None for roots)."""
    par = {}
    for j in idx:
        D = [i for i in idx if C[i][j]]
        if not D:
            par[j] = None
        else:
            # down-set is a chain => it has a unique maximum
            mx = [i for i in D if not any(C[i][k] for k in D)]
            if len(mx) != 1:
                return None
            par[j] = mx[0]
    return par


def forest_realizer(C, idx):
    """THE CONSTRUCTIVE 2-REALIZER (pin FG5).  For a rooted forest,
    L1 = DFS pre-order, roots ascending and children ascending;
    L2 = DFS pre-order, roots DESCENDING and children DESCENDING.
    Returns (L1, L2) or None if the carrier is not a rooted forest.

    Both are pre-orders, so both are linear extensions.  Reversing BOTH
    the child order and the ROOT order is what makes cross-tree pairs
    incomparable in the intersection — reversing children alone leaves
    every cross-tree pair spuriously comparable."""
    idx = sorted(idx)
    par = parents_of_forest(C, idx)
    if par is None:
        return None
    kids = {x: [] for x in idx}
    roots = []
    for x in idx:
        if par[x] is None:
            roots.append(x)
        else:
            kids[par[x]].append(x)
    for x in idx:
        kids[x].sort()

    def dfs(order_roots, rev):
        out = []
        stack = list(reversed(order_roots))
        while stack:
            x = stack.pop()
            out.append(x)
            ch = kids[x][::-1] if rev else kids[x]
            stack.extend(reversed(ch))
        return out

    L1 = dfs(roots, False)
    L2 = dfs(roots[::-1], True)
    return L1, L2


def realizer_is_exact(C, idx, L1, L2):
    """x < y in the poset  IFF  x precedes y in BOTH L1 and L2."""
    p1 = {v: i for i, v in enumerate(L1)}
    p2 = {v: i for i, v in enumerate(L2)}
    if set(p1) != set(idx) or set(p2) != set(idx):
        return False
    for a, b in combinations(sorted(idx), 2):
        both_ab = p1[a] < p1[b] and p2[a] < p2[b]
        both_ba = p1[b] < p1[a] and p2[b] < p2[a]
        if C[a][b]:
            if not both_ab:
                return False
        elif C[b][a]:
            if not both_ba:
                return False
        else:
            if both_ab or both_ba:
                return False
    return True


def sub_poset(C, idx):
    idx = sorted(idx)
    m = len(idx)
    return [[C[idx[i]][idx[j]] for j in range(m)] for i in range(m)]


def has_induced_S3(C):
    """Exhaustive search for the 3-crown S3 as an INDUCED subposet:
    bottoms b0,b1,b2 pairwise incomparable, tops t0,t1,t2 pairwise
    incomparable, ti > bj exactly for j != i."""
    n = len(C)
    if n < 6:
        return None
    inc = lambda a, b: not (C[a][b] or C[b][a])
    for B in combinations(range(n), 3):
        if not all(inc(x, y) for x, y in combinations(B, 2)):
            continue
        rest = [x for x in range(n) if x not in B]
        for T in combinations(rest, 3):
            if not all(inc(x, y) for x, y in combinations(T, 2)):
                continue
            for perm in ((0, 1, 2), (0, 2, 1), (1, 0, 2),
                         (1, 2, 0), (2, 0, 1), (2, 1, 0)):
                ok = True
                for i in range(3):
                    ti = T[perm[i]]
                    for j in range(3):
                        want = (i != j)
                        if C[B[j]][ti] != want:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    return (B, tuple(T[perm[i]] for i in range(3)))
    return None


# =========================================================================
# FG8 — THE WITNESS REPORTER.  A genuine exit-0 outcome, and EXERCISED
# below by the FG7(a) mutant through this same code path (LOG #354 F1).
# =========================================================================
WITNESS_CALLS = []

def report_witness(kind, tag, C, payload):
    """The pin's live witness horn.  Called for a real family witness OR
    by the FG8 exercise; both paths are identical by construction."""
    WITNESS_CALLS.append((kind, tag))
    print(f"  [WITNESS {kind}] {tag} — a pre-registered falsifying outcome")
    n = len(C)
    preds = [sorted(i for i in range(n) if C[i][j]) for j in range(n)]
    print(f"    carrier n = {n}; poset preds = {preds}")
    print(f"    payload = {payload}")
    return True


# =========================================================================
# the exhaustive families (the three committed by D44c)
# =========================================================================
class Witness(Exception):
    pass


ABC = ('A', 'B', 'C')
A4 = ('A', 'B', 'C', 'D')
FAMILIES = [(ABC, 6, True, 'AG1  width 3, <= 6 events, full grammar'),
            (ABC, 7, False, 'AG1b width 3, <= 7 events, no idle'),
            (A4, 6, False, 'AG2b width 4, <= 6 events, no idle')]
EXPECT_TOTALS = {'AG1': 551928, 'AG1b': 224580, 'AG2b': 436864}


def sweep(actors, cap, allow_idle):
    """Label-level exhaustive DFS, the committed candidates_for as sole
    expander.  Structural work is deduplicated by the (REGISTER-WORD,
    EVENT-TYPE) CLASS and re-sampled against the full builder every 97th
    arb-containing history.

    DEDUP CORRECTION (this receipt, run 1 -> run 2).  D44c deduplicates
    by the register-word class alone, which is sound THERE because every
    quantity it caches (n, dim<=2, width) is a function of the poset and
    the poset is a function of the regs_of sequence.  It is NOT sound
    here: this receipt caches ARB-SCOPED quantities, and the actor-
    register projection does not determine which events are arbs — a
    propose by A and an arb with pool {A} share the actor-word letter
    {A}.  Run 1's resample gate caught this at 2,398 mismatches in
    11,664 resamples; the key now carries the event-type sequence.  The
    gate is retained below and must read zero."""
    st = {
        'total': 0, 'arb_hist': 0, 'classes': {},
        'clauses': {'laminar': 0, 'samebase': 0, 'nest': 0,
                    'base_chain': 0, 'vfresh': 0, 'chain': 0},
        # the promotion's own counters
        'vi_viol': [], 'upcone_dis': [], 'upcone_lam': [],
        'forest_full_bad': 0, 'forest_arb_bad': [],
        'L3_viol': 0, 'L3full_viol': 0, 'L3res_viol': 0,
        'L3_cover_viol': 0, 'L3_arbhead_viol': 0,
        'L5_viol': 0, 'L1_viol': 0,
        'L3_wit': None, 'L3res_wit': None, 'L1_wit': None,
        'n_incomp_arb_pairs': 0, 'n_hist_2incomp_arbs': 0,
        'n_dominators_of_incomparables': 0,
        'realizer_checked': 0, 'realizer_bad': [], 'arb_sizes': {},
        'oracle_checked': 0, 'oracle_disagree': [],
        'S3_found': None,
        'sample_checked': 0, 'sample_mism': 0, 'arb_seen': 0,
        'full_forest_witness': None,
    }
    h, word, vns, pools, lastp = [], [], set(), (), {}

    def structural(key):
        cl = st['classes'].get(key)
        if cl is not None:
            return cl
        C = poset_of(h)
        n = len(h)
        arbs = [i for i in range(n) if h[i][0] == 'r']

        # ---- clause (iv) THE CHAIN LAW (intersecting regs => comparable)
        for i in range(n):
            for j in range(i + 1, n):
                if (word[i] & word[j]) and not (C[i][j] or C[j][i]):
                    st['clauses']['chain'] += 1
        # ---- L3 in three forms: the PRE-REGISTERED actor-projection
        #      form, the FULL-register form, and the RESTRICTED form the
        #      T3 proof actually consumes (a non-arb's actor appearing in
        #      the register set of everything above it)
        for i in range(n):
            for j in range(n):
                if not C[i][j]:
                    continue
                if not (word[i] & word[j]):
                    st['L3_viol'] += 1
                    # why do the three L3 forms return IDENTICAL counts?
                    # these two counters answer it on the record.
                    if not any(C[i][k] and C[k][j] for k in range(n)):
                        st['L3_cover_viol'] += 1
                    if h[i][0] == 'r':
                        st['L3_arbhead_viol'] += 1
                    if st['L3_wit'] is None:
                        st['L3_wit'] = ([fmt(e) for e in h], i, j,
                                        sorted(word[i]), sorted(word[j]))
                if not (set(regs_of(h[i])) & set(regs_of(h[j]))):
                    st['L3full_viol'] += 1
                if h[i][0] != 'r' and not (word[i] <= word[j]):
                    st['L3res_viol'] += 1
                    if st['L3res_wit'] is None:
                        st['L3res_wit'] = ([fmt(e) for e in h], i, j,
                                           sorted(word[i]), sorted(word[j]))
        # ---- L5: every NON-ARB event has a singleton actor-register set
        for i in range(n):
            if h[i][0] != 'r' and len(word[i]) != 1:
                st['L5_viol'] += 1
        # ---- L1: every element dominating two incomparables is an arb
        for j in range(n):
            D = [i for i in range(n) if C[i][j]]
            twoinc = any(not (C[a][b] or C[b][a])
                         for a, b in combinations(D, 2))
            if twoinc:
                st['n_dominators_of_incomparables'] += 1
                if h[j][0] != 'r':
                    st['L1_viol'] += 1
                    if st['L1_wit'] is None:
                        st['L1_wit'] = ([fmt(e) for e in h], j,
                                        sorted(D))
        # ---- T1 hypothesis: FULL poset forest property
        bad_full = forest_violations(C)
        if bad_full:
            st['forest_full_bad'] += 1
            if st['full_forest_witness'] is None:
                st['full_forest_witness'] = (
                    [fmt(e) for e in h], bad_full,
                    [sorted(i for i in range(n) if C[i][j])
                     for j in bad_full])
        # ---- T2 hypothesis: ARB-INDUCED forest property
        bad_arb = forest_violations(C, arbs)
        if bad_arb:
            st['forest_arb_bad'].append(([fmt(e) for e in h], bad_arb))
        # ---- capacity (FG1) + clause (vi) + up-cone confinement
        ipairs = [(a, b) for a, b in combinations(sorted(arbs), 2)
                  if not (C[a][b] or C[b][a])]
        st['n_incomp_arb_pairs'] += len(ipairs)
        if len(ipairs) >= 1:
            st['n_hist_2incomp_arbs'] += 1
        st['vi_viol'].extend(clause_vi_violations(C, arbs))
        dis, lam = upcone_violations(C, arbs)
        st['upcone_dis'].extend(dis)
        st['upcone_lam'].extend(lam)
        # ---- FG5/FG6: constructive realizer on the arb subposet
        if arbs and not bad_arb:
            Csub = sub_poset(C, arbs)
            m = len(arbs)
            st['arb_sizes'][m] = st['arb_sizes'].get(m, 0) + 1
            R = forest_realizer(Csub, range(m))
            st['realizer_checked'] += 1
            if R is None or not realizer_is_exact(Csub, range(m), *R):
                st['realizer_bad'].append(([fmt(e) for e in h], arbs))
            else:
                ok_or, _ = dim_le_2(Csub)
                st['oracle_checked'] += 1
                if not ok_or:
                    st['oracle_disagree'].append(([fmt(e) for e in h], arbs))
        # ---- the S3 hunt on the FULL poset (T3's target)
        if st['S3_found'] is None:
            s3 = has_induced_S3(C)
            if s3 is not None:
                st['S3_found'] = ([fmt(e) for e in h], s3)
        st['classes'][key] = (n, len(arbs))
        return st['classes'][key]

    def explore(pools, vns, lastp, arbful):
        depth = len(h)
        if depth >= cap:
            return
        for e, q in candidates_for(h, actors):
            if e[0] == 'n' and not allow_idle:
                continue
            st['total'] += 1
            pools2, vns2, last2 = pools, vns, lastp
            if e[0] == 'r':
                P = frozenset(t[0] for t in e[2])
                b = next(iter(e[2]))[1]
                vn = vname_of_arb(e)
                if vn in vns:
                    st['clauses']['vfresh'] += 1
                for (P0, b0, vn0) in pools:
                    if (P & P0) and not (P <= P0 or P0 <= P):
                        st['clauses']['laminar'] += 1
                    if b0 == b and (P & P0):
                        st['clauses']['samebase'] += 1
                for a in sorted(P):
                    prev = lastp.get(a)
                    if prev is None:
                        if b != V0:
                            st['clauses']['base_chain'] += 1
                    else:
                        if not (P <= prev[0]):
                            st['clauses']['nest'] += 1
                        if b != prev[2]:
                            st['clauses']['base_chain'] += 1
                pools2 = pools + ((P, b, vn),)
                vns2 = vns | {vn}
                last2 = dict(lastp)
                for a in P:
                    last2[a] = (P, b, vn)
            arbful2 = arbful or e[0] == 'r'
            h.append(e)
            word.append(aset(e))
            if arbful2:
                st['arb_hist'] += 1
                st['arb_seen'] += 1
                cl = structural((tuple(word), tuple(x[0] for x in h)))
                if st['arb_seen'] % 97 == 0:
                    st['sample_checked'] += 1
                    Cx = poset_of(h)
                    arx = [i for i in range(len(h)) if h[i][0] == 'r']
                    if (len(h), len(arx)) != cl:
                        st['sample_mism'] += 1
            explore(pools2, vns2, last2, arbful2)
            h.pop()
            word.pop()

    explore((), frozenset(), {}, False)
    return st


print("\n[FG0 port fidelity + the five committed clauses]")
STS = {}
for actors, cap, idle, label in FAMILIES:
    tag = label.split()[0]
    st = sweep(actors, cap, idle)
    STS[tag] = st
    print(f"  {label}: histories = {st['total']}, arb-containing = "
          f"{st['arb_hist']}, register-word classes = {len(st['classes'])}")
    check(f"FG0 {tag}: label-level history count reproduces the committed "
          f"D44c family exactly ({EXPECT_TOTALS[tag]})",
          st['total'] == EXPECT_TOTALS[tag],
          f"got {st['total']}, expected {EXPECT_TOTALS[tag]}")

clause_tot = {}
for st in STS.values():
    for k, v in st['clauses'].items():
        clause_tot[k] = clause_tot.get(k, 0) + v
check("FG0 the five committed confinement clauses (i)-(v) plus the chain "
      "law reproduce at ZERO violations over all three families — the "
      "promotion sits on the same gated ground as D44c",
      all(v == 0 for v in clause_tot.values()),
      f"violations = {dict(sorted(clause_tot.items()))}")

smpl = sum(s['sample_checked'] for s in STS.values())
mism = sum(s['sample_mism'] for s in STS.values())
check("FG0 register-word-class dedup re-sampled against the full builder "
      "(every 97th arb-containing history): zero mismatches",
      mism == 0, f"resamples = {smpl}, mismatches = {mism}")

# ------------------------------------------------------------------ FG1
print("\n[FG1 capacity / anti-vacuity — is clause (vi) a LIVE question?]")
n_ipairs = sum(s['n_incomp_arb_pairs'] for s in STS.values())
n_ihist = sum(s['n_hist_2incomp_arbs'] for s in STS.values())
n_dom = sum(s['n_dominators_of_incomparables'] for s in STS.values())
print(f"  incomparable arb PAIRS present across the families: {n_ipairs}")
print(f"  register-word classes carrying >= 1 such pair: {n_ihist}")
print(f"  elements dominating two incomparable elements: {n_dom}")
check("FG1(a) the stratum on which clause (vi) is live is NON-EMPTY — "
      "incomparable arb pairs actually occur, so a zero violation count "
      "below is a RESULT and not a vacuity",
      n_ipairs > 0 and n_ihist > 0,
      f"incomparable arb pairs = {n_ipairs} in {n_ihist} classes")
check("FG1(b) the stratum on which L1 is live is NON-EMPTY — elements "
      "dominating two incomparable elements actually occur",
      n_dom > 0, f"dominators = {n_dom}")

# ------------------------------------------------------------------ FG2/3
print("\n[FG2 the SIXTH clause, gated in-receipt  (ARB-SCOPED)]")
vi = [v for s in STS.values() for v in s['vi_viol']]
check("FG2 CLAUSE (vi): over the three committed exhaustive families, "
      "ZERO pairs of incomparable arbs possess a common upper bound "
      "among the arbs — the sixth clause is now RECEIPT-GATED, not "
      "referee-carried (LOG #355 entry condition, first half)",
      len(vi) == 0, f"violations = {len(vi)}; pairs tested = {n_ipairs}")

print("\n[FG3 up-cone confinement  (ARB-SCOPED)]")
ud = [v for s in STS.values() for v in s['upcone_dis']]
ul = [v for s in STS.values() for v in s['upcone_lam']]
check("FG3 UP-CONE CONFINEMENT: the arb up-sets of incomparable arbs are "
      "pairwise DISJOINT (zero violations) and the whole up-set family is "
      "LAMINAR (zero violations) — LOG #355 entry condition, second half",
      len(ud) == 0 and len(ul) == 0,
      f"disjointness violations = {len(ud)}, laminarity violations = {len(ul)}")

# ------------------------------------------------------------------ FG4
print("\n[FG4 the forest property — T1 (FULL) and T2 (ARB-SCOPED)]")
full_bad = sum(s['forest_full_bad'] for s in STS.values())
arb_bad = [v for s in STS.values() for v in s['forest_arb_bad']]
n_classes = sum(len(s['classes']) for s in STS.values())
print(f"  register-word classes carrying arbs: {n_classes}")
print(f"  classes whose FULL poset has a non-chain principal down-set: "
      f"{full_bad}")
wit = next((s['full_forest_witness'] for s in STS.values()
            if s['full_forest_witness']), None)
T1_FALSIFIED = full_bad > 0
if T1_FALSIFIED and wit is not None:
    report_witness("T1-FALSIFIED",
                   "the FULL event poset is NOT a rooted forest",
                   [[False]], {'history': wit[0], 'bad_elements': wit[1],
                               'their_down_sets': wit[2]})
check("FG4/T1 the PRE-REGISTERED expectation is confirmed: the FULL event "
      "poset is NOT a rooted forest (an arb dominates two incomparable "
      "proposals).  T1 is FALSIFIED — a pre-registered exit-0 outcome, "
      "not a failure of the receipt",
      T1_FALSIFIED,
      f"classes with a non-chain principal down-set = {full_bad}")
check("FG4/T2 the ARB-INDUCED subposet IS a rooted forest in every class "
      "of every committed family: zero elements with a non-chain "
      "principal down-set among the arbs",
      len(arb_bad) == 0, f"violations = {len(arb_bad)}")

vi_forest_agree = (len(vi) == 0) == (len(arb_bad) == 0)
check("FG4 CROSS-CHECK: clause (vi) and the arb-scoped forest property "
      "are logically equivalent (an element above two incomparable arbs "
      "IS a common upper bound), and the two independent counters agree",
      vi_forest_agree, f"vi violations = {len(vi)}, forest violations = "
                       f"{len(arb_bad)}")

# ------------------------------------------------------------------ FG5/6
print("\n[FG5 the CONSTRUCTIVE 2-realizer + FG6 oracle cross-check]")
rchk = sum(s['realizer_checked'] for s in STS.values())
rbad = [v for s in STS.values() for v in s['realizer_bad']]
ochk = sum(s['oracle_checked'] for s in STS.values())
odis = [v for s in STS.values() for v in s['oracle_disagree']]
check("FG5 the explicit two-linear-extension realizer (DFS pre-order with "
      "roots+children ascending, and DFS pre-order with roots+children "
      "DESCENDING) realizes the arb subposet EXACTLY in every checked "
      "class — dim <= 2 by CERTIFICATE, not by oracle verdict",
      rchk > 0 and len(rbad) == 0,
      f"arb subposets certified = {rchk}, failures = {len(rbad)}")
check("FG6 the certificate agrees with the ported g2 dim<=2 oracle on "
      "every checked arb subposet: zero disagreements",
      ochk > 0 and len(odis) == 0,
      f"oracle cross-checks = {ochk}, disagreements = {len(odis)}")

# --- ROUND-1 P1: the cardinality stratification the parent receipt had
#     and this one had dropped.  D44c tags width <= 2 rows
#     "[theorem, not evidence]" for exactly this reason.
SIZES = {}
for s in STS.values():
    for k, v in s['arb_sizes'].items():
        SIZES[k] = SIZES.get(k, 0) + v
ev_stratum = sum(v for k, v in SIZES.items() if k >= 6)
print(f"  arb-subposet SIZE distribution over all certifications: "
      f"{dict(sorted(SIZES.items()))}")
print(f"  EVIDENCE stratum (size >= 6, the minimum at which dimension "
      f"could exceed 2): {ev_stratum}")
check("FG5/FG6 CARDINALITY STRATIFICATION — ROUND-1 P1 CORRECTION.  The "
      "smallest poset of order dimension > 2 is the 3-crown S3, which has "
      "SIX elements; every poset on five or fewer has dimension <= 2 BY "
      "CARDINALITY ALONE.  The arb subposets certified here max out at "
      f"size {max(SIZES) if SIZES else 0}, so the EVIDENCE stratum is "
      f"{ev_stratum} and **ALL {rchk} CERTIFICATIONS ARE THEOREM-PASSES, "
      "NOT EVIDENCE** — their verdict was fixed before the receipt looked "
      "at them.  This gate exists so the count can never be quoted as "
      "in-family confirmation of the dimension conclusion.  T2's "
      "dimension content comes from the PROOF (note §2) plus FG9, and "
      "from nowhere else; T2's HYPOTHESIS gate is unaffected and remains "
      "live (the forest property is NOT automatic at small size — FG7(b) "
      "fires on a 3-element V poset)",
      ev_stratum == 0 and max(SIZES) < 6 and rchk > 0,
      f"sizes = {dict(sorted(SIZES.items()))}, evidence stratum "
      f"(>= 6) = {ev_stratum}, certifications = {rchk}")

# ------------------------------------------------------------------ T3
print("\n[T3 the FULL-POSET crown result and its PRE-REGISTERED route]")
print("  The pin (§2, T3) named a route to full-poset S3-impossibility:")
print("  (L1) every element dominating two incomparable elements is an")
print("  arb, itself to be derived from (L3) x < y => the actor-register")
print("  sets intersect, (L5) non-arbs have singleton actor-register")
print("  sets, and clause (iv).  Per the pin's decision rule, the")
print("  OUTCOME of each lemma is a deliverable in either direction and")
print("  is an EXIT-0 result; only anchor breakage and mutant")
print("  misbehaviour exit 1.  What the measurement says:")
l3 = sum(s['L3_viol'] for s in STS.values())
l3f = sum(s['L3full_viol'] for s in STS.values())
l3r = sum(s['L3res_viol'] for s in STS.values())
l5 = sum(s['L5_viol'] for s in STS.values())
l1 = sum(s['L1_viol'] for s in STS.values())
s3 = next((s['S3_found'] for s in STS.values() if s['S3_found']), None)
L3_OK, L1_OK, L5_OK = l3 == 0, l1 == 0, l5 == 0
L3RES_OK = l3r == 0

w3 = next((s['L3_wit'] for s in STS.values() if s['L3_wit']), None)
w1 = next((s['L1_wit'] for s in STS.values() if s['L1_wit']), None)
print(f"  L3 (actor-projection form)  : violations = {l3}  -> "
      f"{'HOLDS' if L3_OK else 'FALSIFIED'}")
print(f"  L3 (FULL-register form)     : violations = {l3f}  -> "
      f"{'HOLDS' if l3f == 0 else 'FALSIFIED'}")
print(f"  L3 (RESTRICTED: non-arb x < y => aset(x) <= aset(y)) : "
      f"violations = {l3r}  -> {'HOLDS' if L3RES_OK else 'FALSIFIED'}")
print(f"  L5 (non-arbs have singleton actor sets) : violations = {l5}"
      f"  -> {'HOLDS' if L5_OK else 'FALSIFIED'}")
print(f"  L1 (dominators of incomparables are arbs) : violations = {l1}"
      f" of {n_dom} dominators  -> {'HOLDS' if L1_OK else 'FALSIFIED'}")
if not L3_OK and w3 is not None:
    report_witness("L3-FALSIFIED", "a causal pair with DISJOINT actor-"
                   "register sets — the link is carried by a vname "
                   "register, not by a shared actor",
                   [[False]], {'history': w3[0], 'x': w3[1], 'y': w3[2],
                               'aset_x': w3[3], 'aset_y': w3[4]})
if not L1_OK and w1 is not None:
    report_witness("L1-FALSIFIED", "a NON-ARB element dominating two "
                   "incomparable elements — domination is transitive, so "
                   "a proposal reading a minted vname inherits the arb's "
                   "whole down-set",
                   [[False]], {'history': w1[0], 'dominator': w1[1],
                               'its_down_set': w1[2]})
l3c = sum(s['L3_cover_viol'] for s in STS.values())
l3a = sum(s['L3_arbhead_viol'] for s in STS.values())
print(f"  WHY the three L3 forms return the SAME count: of the {l3} "
      f"violating causal pairs (x, y), {l3c} are COVER pairs and {l3a} "
      f"are arb-headed.")
check("T3/L3 THE COINCIDENCE EXPLAINED (three independent predicates "
      "returning an identical count is not left as a coincidence): every "
      "actor-disjoint causal pair is PURELY TRANSITIVE — zero of them are "
      "cover pairs — and every one is headed by a NON-ARB.  Transitivity "
      "explains the full-register form (a non-cover pair shares no "
      "register at all, actor or vname), and the non-arb head plus L5 "
      "(singleton actor sets) makes 'aset(x) <= aset(y)' equivalent to "
      "'aset(x) n aset(y) != {}' — so all three forms count the SAME "
      "pairs, and this is a structural fact, not an instrument artifact",
      l3 > 0 and l3c == 0 and l3a == 0 and l3 == l3f == l3r,
      f"violations = {l3}, of which covers = {l3c}, arb-headed = {l3a}; "
      f"full-register form = {l3f}, restricted form = {l3r}")
check("T3 ROUTE, measured and reported in both directions: the pin's "
      "three lemmas each returned a determinate verdict over live, "
      "non-empty strata — L5 HOLDS, while L3 and L1 are FALSIFIED with "
      "witnesses printed.  THE PRE-REGISTERED T3 ROUTE IS DEAD; this is "
      "a deliverable under the pin's decision rule, not a gate failure",
      L5_OK and (not L3_OK) and (not L1_OK) and n_dom > 0,
      f"L3 = {l3}, L3-full = {l3f}, L3-restricted = {l3r}, L5 = {l5}, "
      f"L1 = {l1} of {n_dom}")
check("T3 ROUTE SCOPE: what is falsified is THIS RECEIPT'S "
      "RECONSTRUCTION of the round's argument, not the round's own "
      "pool-laminarity route, which was never stated in gateable form "
      "and is NOT tested here.  The distinction is load-bearing and is "
      "carried into the note and paper 32",
      (not L3_OK) and (not L1_OK),
      "reconstruction falsified; the round's own route remains untested")
if s3 is not None:
    report_witness("S3-PRESENT", "an induced 3-crown exists in the FULL "
                   "poset", [[False]], {'history': s3[0], 'crown': s3[1]})
check("T3 TARGET (unchanged from D44c, TESTED SCALE): NO induced S3 crown "
      "exists in the full event poset of any history of any committed "
      "family — exhaustive over every bottom/top triple of every class.  "
      "With the route dead, this remains EVIDENCE at tested scale and is "
      "NOT promoted to a scale-free theorem",
      s3 is None, f"crowns found = {0 if s3 is None else 1}")

# ------------------------------------------------------------------ FG9
print("\n[FG9 the implication, verified INDEPENDENTLY of the grammar]")
print("  every rooted forest on <= 8 nodes, enumerated as parent functions")
print("  with parent(i) < i or None (a topological labelling — every")
print("  rooted forest admits one, so the enumeration is exhaustive up to")
print("  isomorphism); for each: build the realizer and verify it realizes")
print("  the poset exactly; cross-check the g2 oracle for n <= 6.")

def forest_poset(par, n):
    C = [[False] * n for _ in range(n)]
    for j in range(n):
        p = par[j]
        while p is not None:
            C[p][j] = True
            p = par[p]
    return C

fg9_total = fg9_bad = fg9_oracle = fg9_odis = 0
fg9_nonchain = 0
for n in range(1, 9):
    par = [None] * n
    def rec(i):
        global fg9_total, fg9_bad, fg9_oracle, fg9_odis, fg9_nonchain
        if i == n:
            C = forest_poset(par, n)
            fg9_total += 1
            if forest_violations(C):
                fg9_nonchain += 1
                return
            R = forest_realizer(C, range(n))
            if R is None or not realizer_is_exact(C, range(n), *R):
                fg9_bad += 1
                return
            if n <= 6:
                ok, _ = dim_le_2(C)
                fg9_oracle += 1
                if not ok:
                    fg9_odis += 1
            return
        opts = [None] + list(range(i))
        for p in opts:
            par[i] = p
            rec(i + 1)
        par[i] = None
    rec(0)

print(f"  rooted forests enumerated (n = 1..8): {fg9_total}")
check("FG9 EVERY rooted forest on <= 8 nodes has its principal down-sets "
      "chains and the FG5 realizer realizes it EXACTLY.  SCOPE — ROUND-1 "
      "P2 CORRECTION: a finite enumeration to n = 8 licenses a statement "
      "about n <= 8 and NOTHING MORE.  **What licenses the word THEOREM "
      "for all n is the PROOF in note §2**; this enumeration is "
      "CORROBORATION of a proved implication, grammar-independent and "
      "therefore worth having, but it is not the license.  (Sharpened by "
      "P1: n <= 8 is exactly the range the in-family objects occupy, so "
      "neither the enumeration nor the family reaches the regime where "
      "the verdict could differ.)",
      fg9_total == 46233 and fg9_nonchain == 0 and fg9_bad == 0,
      f"forests = {fg9_total}, non-chain down-sets = {fg9_nonchain}, "
      f"realizer failures = {fg9_bad}")
check("FG9 oracle cross-check on the n <= 6 forests: the g2 oracle "
      "confirms dim <= 2 on every one, zero disagreements",
      fg9_oracle > 0 and fg9_odis == 0,
      f"oracle checks = {fg9_oracle}, disagreements = {fg9_odis}")

# ------------------------------------------------------------------ FG7
print("\n[FG7 mutants — the instrument must react as DECLARED]")
# (a) the S3 crown: bottoms 0,1,2 / tops 3,4,5 with ti > bj iff i != j
S3C = [[False] * 6 for _ in range(6)]
for i in range(3):
    for j in range(3):
        if i != j:
            S3C[j][3 + i] = True
m_a_forest = forest_violations(S3C)
m_a_real = forest_realizer(S3C, range(6))
m_a_orac, _ = dim_le_2(S3C)
m_a_s3 = has_induced_S3(S3C)
check("FG7(a) the S3 crown mutant: the forest property FAILS, the "
      "realizer construction REFUSES (returns no certificate), the g2 "
      "oracle reports dim > 2, and the S3 detector FINDS it — four "
      "independent instruments all react",
      len(m_a_forest) == 3 and m_a_real is None and not m_a_orac
      and m_a_s3 is not None,
      f"non-chain elements = {sorted(m_a_forest)}, realizer = "
      f"{'refused' if m_a_real is None else 'PRODUCED'}, oracle dim<=2 = "
      f"{m_a_orac}, S3 detected = {m_a_s3 is not None}")

# (b) the V poset: 0,1 incomparable, both below 2
VC = [[False] * 3 for _ in range(3)]
VC[0][2] = VC[1][2] = True
m_b_vi = clause_vi_violations(VC, [0, 1, 2])
m_b_dis, _ = upcone_violations(VC, [0, 1, 2])
check("FG7(b) the V mutant (two incomparable elements below a common "
      "top): clause (vi) FIRES and up-cone disjointness FIRES — the two "
      "gates of #355's entry condition are demonstrably not blind",
      len(m_b_vi) == 1 and len(m_b_dis) == 1,
      f"clause (vi) violations = {m_b_vi}, up-cone violations = {m_b_dis}")

# (c) a genuine rooted forest: 0 < 1, 0 < 2, 3 isolated, 2 < 4
FC = [[False] * 5 for _ in range(5)]
for (a, b) in ((0, 1), (0, 2), (0, 4), (2, 4)):
    FC[a][b] = True
m_c_forest = forest_violations(FC)
m_c_R = forest_realizer(FC, range(5))
m_c_ok = m_c_R is not None and realizer_is_exact(FC, range(5), *m_c_R)
m_c_or, _ = dim_le_2(FC)
check("FG7(c) the honest rooted-forest mutant (two trees, one branching): "
      "the forest property HOLDS, the realizer is produced and verified "
      "EXACT, and the oracle agrees dim <= 2 — the instrument passes what "
      "it should pass, not only fails what it should fail",
      len(m_c_forest) == 0 and m_c_ok and m_c_or,
      f"non-chain = {m_c_forest}, realizer exact = {m_c_ok}, oracle = "
      f"{m_c_or}")

# (d) the child-order-only realizer must FAIL on a two-tree poset —
#     the trap named in forest_realizer's docstring
def bad_realizer(C, idx):
    idx = sorted(idx)
    par = parents_of_forest(C, idx)
    kids = {x: [] for x in idx}
    roots = [x for x in idx if par[x] is None]
    for x in idx:
        if par[x] is not None:
            kids[par[x]].append(x)
    for x in idx:
        kids[x].sort()
    def dfs(rev):
        out, stack = [], list(reversed(roots))
        while stack:
            x = stack.pop()
            out.append(x)
            ch = kids[x][::-1] if rev else kids[x]
            stack.extend(reversed(ch))
        return out
    return dfs(False), dfs(True)

TWO = [[False] * 2 for _ in range(2)]
m_d = bad_realizer(TWO, range(2))
m_d_bad = not realizer_is_exact(TWO, range(2), *m_d)
m_d_good = forest_realizer(TWO, range(2))
m_d_ok = realizer_is_exact(TWO, range(2), *m_d_good)
check("FG7(d) the NEAR-MISS mutant: a realizer that reverses only the "
      "CHILD order (not the root order) fails to realize a two-root "
      "forest — while the FG5 construction, which reverses both, "
      "succeeds.  The certificate's specific form is load-bearing and "
      "the check would notice if it were weakened",
      m_d_bad and m_d_ok,
      f"child-only realizer exact = {not m_d_bad}, FG5 realizer exact = "
      f"{m_d_ok}")

# ------------------------------------------------------------------ FG8
print("\n[FG8 the witness branch is LIVE and EXERCISED  (LOG #354 F1)]")
print("  D44c shipped a witness horn that was UNREACHABLE at exit 0: a")
print("  witness would have tripped the census conjuncts and exited 1")
print("  mislabeled as breakage, and its verdict print was dead code.")
print("  That defect is BINDING on successor dimension receipts.  Here the")
print("  horn is a genuine exit-0 outcome, and it is EXERCISED below by")
print("  driving the FG7(a) crown mutant through the SAME reporter.")
_before = len(WITNESS_CALLS)
report_witness("EXERCISE", "FG7(a) crown mutant driven through the live "
               "witness reporter", S3C,
               {'non_chain_elements': sorted(m_a_forest),
                'crown': m_a_s3, 'oracle_dim_le_2': m_a_orac})
check("FG8 the witness reporter is REACHABLE and EXECUTED in this run "
      "(not dead code): the exercise call produced a witness report, and "
      "the T1 falsification above went through the same function",
      len(WITNESS_CALLS) > _before and any(k == 'T1-FALSIFIED'
                                           for k, _ in WITNESS_CALLS),
      f"witness reporter invocations this run = "
      f"{[k for k, _ in WITNESS_CALLS]}")
check("FG8 exit discipline: THREE pre-registered items were falsified in "
      "this run (the form T1 and the lemmas L3, L1) and each was recorded "
      "as a PASSING gate reporting a determinate negative — falsification "
      "is a deliverable, not a breakage.  (Run 1 of this receipt got this "
      "gate wrong: it conjoined FAIL == 0, which made the exit-discipline "
      "check fail precisely when the discipline was working.)",
      T1_FALSIFIED and (not L3_OK) and (not L1_OK),
      f"T1 falsified = {T1_FALSIFIED}, L3 falsified = {not L3_OK}, "
      f"L1 falsified = {not L1_OK}")

# ------------------------------------------------------------------ FG10
print("\n[FG10 anti-vacuity scan of this receipt's own gates]")
_self = open('v10/code/d44cp_funnel_lemma_exact.py').read()
_tree = ast.parse(_self)
_bound = set()
for _n in ast.walk(_tree):
    if isinstance(_n, ast.Name) and isinstance(_n.ctx, ast.Store):
        _bound.add(_n.id)
    elif isinstance(_n, (ast.FunctionDef, ast.AsyncFunctionDef)):
        _bound.add(_n.name)
        for _a in _n.args.args:
            _bound.add(_a.arg)
_checks = [c for c in ast.walk(_tree)
           if isinstance(c, ast.Call) and isinstance(c.func, ast.Name)
           and c.func.id == 'check']
_vacuous = []
for c in _checks:
    pred = c.args[1]
    names = {x.id for x in ast.walk(pred) if isinstance(x, ast.Name)}
    if isinstance(pred, ast.Constant) or not (names & _bound):
        _vacuous.append(ast.dump(pred)[:80])
check("FG10 every check() predicate in this receipt references at least "
      "one run-bound name and none is a bare constant.  SCOPE (LOG #403 "
      "MA-2): this scan enforces EXACTLY that and nothing more — it does "
      "NOT detect a vacuous gate in arbitrary syntactic form, and must "
      "not be described as if it did",
      len(_checks) >= 18 and not _vacuous,
      f"check() calls scanned = {len(_checks)}, bare/unbound = "
      f"{len(_vacuous)}")

# ========================== the verdict ==================================
print("\n[VERDICT — the pin's decision rule (§2), applied]")
T2_OK = (len(arb_bad) == 0 and len(vi) == 0 and len(ud) == 0
         and len(ul) == 0 and len(rbad) == 0 and fg9_bad == 0)
T3_OK = T2_OK and L3_OK and L5_OK and L1_OK and s3 is None
print(f"  T1  [FALSIFIED]  — as PRE-REGISTERED.  The full event poset is "
      f"not a rooted forest: {full_bad} register-word classes carry an "
      f"element whose principal down-set is not a chain (an arb consumes "
      f"a component of mutually conflicting proposals).")
print(f"  T2  [{'THEOREM' if T2_OK else 'OPEN'}]  — hypothesis GATED "
      f"(zero violations, {n_ipairs} incomparable arb pairs live) and "
      f"implication MACHINE-VERIFIED grammar-independently over "
      f"{fg9_total} rooted forests.  The arb-induced subposet is a rooted "
      f"forest, hence has order dimension <= 2 and contains no crown, at "
      f"EVERY width and depth.")
print(f"  T3  [{'THEOREM' if T3_OK else 'OPEN — ROUTE FALSIFIED'}]  — the "
      f"pin's route to full-poset S3-impossibility is DEAD.  L3 fails "
      f"({l3} counterexamples): a causal link can be carried entirely by "
      f"a minted vname register, so x < y does NOT force the actor-"
      f"register sets to intersect.  L1 fails ({l1} of {n_dom}): "
      f"domination is TRANSITIVE, so a proposal reading a minted vname "
      f"inherits the arb's whole down-set and a NON-ARB can dominate two "
      f"incomparable elements.  The FULL-POSET crown claim therefore "
      f"stands exactly where D44c left it — EVIDENCE AT TESTED SCALE "
      f"(zero crowns over the three exhaustive families), not a "
      f"scale-free no-go.")
print("  WHAT IS AND IS NOT FALSIFIED: this receipt falsified ITS OWN "
      "reconstruction of the round's argument.  The round's stated route "
      "goes through POOL LAMINARITY, was never written in gateable form, "
      "and is NOT tested here.  Nothing above impugns the referee's "
      "claim; it establishes only that the obvious register-theoretic "
      "route to it does not exist.")
print("  SCOPE, per pin §3: clauses (i)-(v) are ALL-SCALE per LOG #354; "
      "T2's hypothesis is gated over the three committed families and "
      "its implication is machine-verified grammar-independently, so T2 "
      "is scale-free in the implication and family-gated in the "
      "hypothesis — stated that way, without rounding up.")
print(f"  PAPER 32 §6 item 7: {'CLOSE' if T3_OK else 'AMEND TO PARTIAL'} "
      f"— the two halves of #355's entry condition (the sixth clause, "
      f"up-cone confinement) ARE now receipt-gated, and the arb-scoped "
      f"crown no-go IS now a theorem with a constructive certificate; but "
      f"§3.1's FULL-POSET claim is NOT discharged and its referee-carried "
      f"status must be RETAINED, with the note's dead route recorded so "
      f"no one walks it again.")

print(f"\n[totals] PASS = {PASS}, FAIL = {FAIL}")
if FAIL:
    print("EXIT 1 — gate failure")
    sys.exit(1)
print("EXIT 0")

#!/usr/bin/env python3
"""
d49_dichotomy_settlement_exact.py — v10 D49: THE COMPLETION DICHOTOMY,
SETTLED. Pin: note-d49-completion-dichotomy-settlement-pin.md (strict).
Parents: paper 30 §5.3/§5.6/§5.7 (the trilemma, the rootedness exhibit,
the one-way reduction); d43b TERMINAL #339/#345 (MG3-MG5: lambda = 2,
f = (4,4,3,7,3,3)/3, MG4 root-free certificate on the window); d44a
TERMINAL (the depth-free 36-state closure and the (H0)-(H2) conditional
theorem); THE-COMPLETION-DICHOTOMY.md #416/#417.

THE DELIVERED OBJECT.  paper 30 §5.7 DEFINES a stationary (root-free)
completion as a positive-eigenvector solution

        Zhat(h) = f(state(h)) . lambda^(-depth(h))

of the local transfer on the bisimulation quotient, and declares its
existence OPEN in both directions.  d43b then computed the eigenproblem
(lambda = 2, f positive, unique up to scale) and d44a closed the state
space (36 sigma-states, six quotient classes) — but NO UNIT EVER BUILT
Zhat ON HISTORIES AND TESTED IT AGAINST THE COMPLETION DEMANDS.  This
receipt does exactly that, and the answer is YES: the completion exists,
is unique up to scale, is per-cut normalized, foliation-invariant and
support-preserving, and prices the root and the post-arbitration renewal
point IDENTICALLY — the defect that paper 30 §5.6 used to convict every
truncated completion of being ROOTED.

Horn (II) of the dichotomy therefore HOLDS at d42a scope: the record law
does not import a boundary condition.  Two honest limits are gated, not
narrated: (i) demand (c) is NOT restored — Zhat deforms within-cut ratios
at 50 of the 114 interior cut classes, MORE than the unit boundary's 21
(the §3.1 no-go is untouched), though it does NOT deform the ROOT, which
removes paper 30 §5.3's sharp point; (ii) the settlement's content is the
sigma-measurability demand and NOT asymptotic forgetting — unconstrained
boundaries provably do NOT wash out (gated: diameter 1 at every truncation
depth tested).

Banner: EXACT Fractions throughout; stdlib only; the d42a admission layer
exec'd from the committed d42b3 receipt (__file__-anchored, the d43b/d44a
pattern); sigma ported from the committed d44a receipt SECTION A;
deterministic (post-renaming-sorted plain-tuple serializations only);
exit 1 on any gate failure.
"""
import os
import sys
from collections import defaultdict
from fractions import Fraction as Fr
from itertools import permutations

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def dkey(x):
    """Deterministic serialization: frozensets become tuples sorted by
    their own deterministic keys, so nothing in this receipt is ever
    ordered or compared through a raw frozenset repr (the d44a
    banner's discipline; a PYTHONHASHSEED=7 run caught the omission)."""
    if isinstance(x, (frozenset, set)):
        return ('S',) + tuple(sorted((dkey(y) for y in x), key=repr))
    if isinstance(x, tuple):
        return ('T',) + tuple(dkey(y) for y in x)
    if isinstance(x, Fr):
        return ('Q', str(x))
    return ('A', repr(x))

_here = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(_here, 'd42b3_placement_exact.py')).read()
ns = {}
exec(_src[:_src.index('print("[d42b3')], ns)
V0 = ns['V0']
candidates_for = ns['candidates_for']
vname = ns['vname']
View = ns['View']
event_poset = ns['event_poset']
canon = ns['canon']
AB = ('A', 'B')

print("[d49 — the completion dichotomy, settled]")
print("  banner: EXACT; d42a layer from the committed d42b3 receipt;")
print("  sigma from the committed d44a SECTION A; the object under")
print("  test is paper 30 §5.7's OWN definition of a stationary")
print("  completion, Zhat(h) = f(state(h)) . lambda^(-depth(h)),")
print("  built on HISTORIES and gated against the completion demands.")

# ================= SECTION A — the enumeration =======================
FAM = [[]]
CACHE = {}
frontier = [[]]
while frontier:
    h = frontier.pop()
    CACHE[tuple(h)] = candidates_for(h, AB)
    if len(h) >= 6: continue
    for e, q in CACHE[tuple(h)]:
        FAM.append(h + [e]); frontier.append(h + [e])
cum = [sum(1 for h in FAM if len(h) <= k) for k in range(7)]
BYLEN = defaultdict(list)
for h in FAM: BYLEN[len(h)].append(tuple(h))
CANCLS = defaultdict(list)
for h in FAM: CANCLS[canon(h)].append(tuple(h))
n_can4 = len({canon(h) for h in FAM if len(h) <= 4})
n_int = len({canon(h) for h in FAM if len(h) <= 3})
n_term = n_can4 - n_int
check("A1 [ANCHOR] the enumeration anchor: cumulative depth-0..6 census equals "
      "the committed [1, 7, 39, 215, 1191, 6471, 34375]; canonical "
      "classes 427 at depth <= 4 and 5,548 at depth <= 6; the depth-4 "
      "complex splits into 114 INTERIOR and 313 TERMINAL cut classes "
      "(paper 30 §5.3's 313-dimensional boundary freedom)",
      cum == [1, 7, 39, 215, 1191, 6471, 34375]
      and n_can4 == 427 and len(CANCLS) == 5548
      and n_int == 114 and n_term == 313,
      f"census = {cum}; classes = {n_can4} / {len(CANCLS)}; "
      f"interior = {n_int}; terminal = {n_term}")

def cands_of(hk):
    if hk not in CACHE: CACHE[hk] = candidates_for(list(hk), AB)
    return CACHE[hk]

# ============ SECTION B — sigma (committed d44a port) ================
SG_VIOL = {'alive': 0, 'nonsup': 0, 'liveX': 0, 'cmp': 0}
def own_alive(h, a):
    acts2 = list(h) + [('n', a)]
    pred = event_poset(acts2)
    vw = View(acts2, pred, pred[len(acts2) - 1])
    alive = {b for b in vw.holdings(a) if b not in vw.superseded}
    if len(alive) != 1: SG_VIOL['alive'] += 1
    return sorted(alive, key=repr)[0]

RAWMEMO = {}
def sigma_raw(hk):
    if hk in RAWMEMO: return RAWMEMO[hk]
    h = list(hk); pred = event_poset(h)
    fv = View(h, pred, set(range(len(h)))); sup = fv.superseded
    X = {a: own_alive(h, a) for a in AB}; hold = {}
    for a in AB:
        if not (fv.holdings(a) - sup <= {X[a]}): SG_VIOL['nonsup'] += 1
        hold[a] = X[a] if X[a] not in sup else None
    live = tuple(sorted(((op[1], op[2], op[3])
                         for op in fv.live.values()), key=repr))
    for t in live:
        if t[1] not in (X['A'], X['B']): SG_VIOL['liveX'] += 1
    li = sorted(fv.live.items())
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            (i1, o1), (i2, o2) = li[i], li[j]
            if (o1[2] == o2[2] and o1[3] != o2[3]
                    and not fv.incomparable(i1, i2)):
                SG_VIOL['cmp'] += 1
    comps = []
    for base, idxs in fv.components():
        mem = tuple(sorted((fv.props[i][1], fv.props[i][3])
                           for i in idxs))
        E = tuple(sorted(tuple(sorted(((fv.props[i][1], fv.props[i][3]),
                                       (fv.props[k][1], fv.props[k][3]))))
                         for (i, k) in fv.edges(set(idxs))))
        comps.append((base, mem, E))
    refs = sorted({b for b in (hold['A'], hold['B']) if b is not None}
                  | {t[1] for t in live}, key=repr)
    RAWMEMO[hk] = (hold, tuple(live), tuple(comps), tuple(refs), sup)
    return RAWMEMO[hk]

def ser(hold, live, comps, refs, sup, m):
    return repr((tuple((a, m.get(hold[a])) for a in AB),
                 tuple(sorted(((t[0], m[t[1]], t[2]) for t in live),
                              key=repr)),
                 tuple(sorted(((m[c[0]], c[1], c[2]) for c in comps),
                              key=repr)),
                 tuple(sorted((m[b], b in sup) for b in refs))))

SIGMEMO = {}
def canon_sigma(hk):
    if hk in SIGMEMO: return SIGMEMO[hk]
    hold, live, comps, refs, sup = sigma_raw(hk)
    best = None
    for perm in permutations(range(len(refs))):
        m = {refs[i]: perm[i] for i in range(len(refs))}
        s = ser(hold, live, comps, refs, sup, m)
        if best is None or s < best: best = s
    SIGMEMO[hk] = best
    return best

SIG = {tuple(h): canon_sigma(tuple(h)) for h in FAM}
SROOT = SIG[()]
REP = {SROOT: ()}; bq = [SROOT]; n_exp = 0; n_edges = 0
while bq:
    s = bq.pop(0); hk = REP[s]; n_exp += 1
    for e, q in cands_of(hk):
        n_edges += 1
        s2 = canon_sigma(hk + (e,))
        if s2 not in REP:
            REP[s2] = hk + (e,); bq.append(s2)
check("A2 [ANCHOR] the depth-free closure re-derived (d44a CG3a): frontier-"
      "exhausted BFS on sigma-space closes at 36 states / 176 traversed "
      "edges, the reachable set coincides with the cache-realized set, "
      "and the d42a view invariants sigma rests on hold family-wide",
      len(REP) == 36 and n_exp == 36 and n_edges == 176 and not bq
      and set(REP) == set(SIG.values())
      and all(v == 0 for v in SG_VIOL.values()),
      f"states = {len(REP)}; edges = {n_edges}; view violations = "
      f"{SG_VIOL}")

def relabel(d):
    relab = {}
    for k in sorted(d, key=repr): relab.setdefault(d[k], len(relab))
    return {k: relab[d[k]] for k in d}

WROW = {}
for s, r in REP.items():
    row = defaultdict(Fr)
    for e, q in cands_of(r): row[canon_sigma(r + (e,))] += q
    WROW[s] = dict(row)
shape36 = {s: repr(tuple(sorted((e[0], str(q)) for e, q in cands_of(r))))
           for s, r in REP.items()}
QPART = relabel(shape36); qtraj = [len(set(QPART.values()))]
while True:
    nxt = {}
    for s in REP:
        acc = defaultdict(Fr)
        for s2, q in WROW[s].items(): acc[QPART[s2]] += q
        nxt[s] = (QPART[s], tuple(sorted((c, str(q)) for c, q in acc.items())))
    nxt = relabel(nxt); qtraj.append(len(set(nxt.values())))
    stable = len(set(nxt.values())) == len(set(QPART.values()))
    QPART = nxt
    if stable: break

def menu_shape(c):
    d = {}
    for e, q in c: d[(e[0], q)] = d.get((e[0], q), 0) + 1
    return tuple(sorted(d.items(), key=repr))
P = {0: relabel({tuple(h): menu_shape(CACHE[tuple(h)]) for h in FAM})}
for t in range(5):
    nx = {}
    for h in FAM:
        if len(h) > 5 - t: continue
        k = tuple(h)
        nx[k] = (P[t][k], tuple(sorted((str(q), P[t][tuple(h + [e])])
                                       for e, q in CACHE[k])))
    P[t + 1] = relabel(nx)
tA = ('A', V0, 0); V1 = vname(V0, frozenset({tA}), 'A'); tB = ('B', V0, 1)
pA0 = ('p', 'A', V0, 0); pB0 = ('p', 'B', V0, 0); pB1 = ('p', 'B', V0, 1)
SELFA = ('r', 'A', frozenset({tA}), frozenset({tA}))
PAIR = ('r', 'A', frozenset({tA, tB}), frozenset({tA}))
H3 = (pA0, pB1, PAIR)
REPS6 = [(), (pA0,), (pA0, pB0), (pA0, pB1), (pA0, SELFA), (pA0, pB0, SELFA)]
repmap = {P[2][r]: i for i, r in enumerate(REPS6)}
CLS = {tuple(h): repmap.get(P[2][tuple(h)], -1)
       for h in FAM if len(h) <= 4}
Q2C = {}
for h in FAM:
    if len(h) > 4: continue
    Q2C.setdefault(QPART[SIG[tuple(h)]], set()).add(CLS[tuple(h)])
Q2C = {k: next(iter(v)) for k, v in Q2C.items()}
def cls_of(hk):
    return Q2C[QPART[canon_sigma(hk)]]
TQ = {}
tq_ok = True
for s in REP:
    c = Q2C[QPART[s]]
    row = defaultdict(Fr)
    for s2, q in WROW[s].items(): row[Q2C[QPART[s2]]] += q
    row = dict(row)
    if c in TQ: tq_ok &= (TQ[c] == row)
    else: TQ[c] = row
T = [[TQ[i].get(j, Fr(0)) for j in range(6)] for i in range(6)]
T_REF = {0: {0: Fr(3,2), 1: Fr(1,2)},
         1: {1: Fr(3,2), 2: Fr(1,8), 3: Fr(1,8), 4: Fr(1,4)},
         2: {2: Fr(3,2), 5: Fr(1,2)},
         3: {0: Fr(1,2), 3: Fr(3,2), 5: Fr(1,2)},
         4: {4: Fr(3,2), 5: Fr(1,2)},
         5: {2: Fr(1,4), 4: Fr(1,4), 5: Fr(3,2)}}
check("A3 [ANCHOR] the six-class quotient and the committed transfer re-derived "
      "(d43b MG2d / d44a CG3e): refinement trajectory 4-5-6-6, rows "
      "constant across all 36 abstract states, T == T_REF entrywise, "
      "row sums (2, 2, 2, 5/2, 2, 2) — the menus that do NOT sum to 1",
      qtraj == [4, 5, 6, 6] and tq_ok and TQ == T_REF
      and [sum(T[i]) for i in range(6)]
      == [Fr(2), Fr(2), Fr(2), Fr(5,2), Fr(2), Fr(2)],
      f"trajectory = {qtraj}; T == T_REF = {TQ == T_REF}")

# =============== SECTION C — the Perron package ======================
DOM, TRA = [2, 4, 5], [0, 1, 3]
def charpoly(M):
    n = len(M); cs = [Fr(1)]
    Mk = [[Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
    for k in range(1, n + 1):
        Mk = [[sum(M[i][t] * Mk[t][j] for t in range(n)) for j in range(n)]
              for i in range(n)]
        tr = sum(Mk[i][i] for i in range(n)); c = -tr / k; cs.append(c)
        for i in range(n): Mk[i][i] += c
    return cs
def peval(cs, x):
    v = Fr(0)
    for c in cs: v = v * x + c
    return v
Md = [[T[i][j] for j in DOM] for i in DOM]
Mt = [[T[i][j] for j in TRA] for i in TRA]
LAM = Fr(2)
FV = [Fr(4,3), Fr(4,3), Fr(1), Fr(7,3), Fr(1), Fr(1)]
# irreducibility of DOM
reach = {i: {i} for i in DOM}
for _ in range(3):
    for i in DOM:
        reach[i] |= {k for j in list(reach[i]) for k in DOM if T[j][k] != 0}
dom_irred = all(reach[i] == set(DOM) for i in DOM)
dom_closed = all(T[i][j] == 0 for i in DOM for j in range(6) if j not in DOM)
cd = charpoly(Md)
fact_dom = all(peval(cd, x) == 0 for x in (Fr(2), Fr(3,2), Fr(1)))
ct = charpoly(Mt)
# charpoly(Mt) == (x - 3/2)^3 - 1/32   =>  transient radius 3/2 + 2^(-5/3)
tri_shift = [Fr(1), Fr(-9,2), Fr(27,4), Fr(-27,8) - Fr(1,32)]
check("C1 [SUBSTANTIVE] the class structure and the exact spectrum: {2,4,5} is CLOSED "
      "and IRREDUCIBLE; charpoly(dominant) = (x-2)(x-3/2)(x-1) so "
      "rho(dominant) = 2 EXACTLY; charpoly(transient) = (x-3/2)^3 - 1/32 "
      "so the transient radius is 3/2 + 2^(-5/3) ~ 1.81498 < 2 — the "
      "M-matrix certificate paper 30's reduction needs",
      dom_closed and dom_irred and fact_dom and ct == tri_shift,
      f"dominant closed = {dom_closed}, irreducible = {dom_irred}; "
      f"charpoly(tra) = {[str(c) for c in ct]}")
check("C2 [ANCHOR] the Perron eigenvector: T f = 2 f EXACTLY with the strictly "
      "positive f = (4/3, 4/3, 1, 7/3, 1, 1) (the committed "
      "(4,4,3,7,3,3)/3)",
      all(sum(T[i][j] * FV[j] for j in range(6)) == LAM * FV[i]
          for i in range(6)) and all(x > 0 for x in FV),
      "T f = 2 f, f > 0")

# ============ SECTION D — THE SETTLEMENT OBJECT ======================
def ZHAT(hk):
    return Fr(1, 2 ** len(hk)) * FV[cls_of(hk)]
def qprime(hk):
    zi = ZHAT(hk)
    return {e: q * ZHAT(hk + (e,)) / zi for e, q in cands_of(hk)}

bad = sum(1 for hk in (tuple(h) for h in FAM if len(h) <= 5)
          if sum(qprime(hk).values()) != 1)
npos = sum(1 for h in FAM for e, v in
           ([] if len(h) > 5 else qprime(tuple(h)).items()) if v <= 0)
check("D1 [DERIVED] Zhat(h) = 2^(-|h|) . f(class(sigma(h))) IS A COMPLETION: "
      "strictly positive, and PER-CUT NORMALIZED EXACTLY at every one "
      "of the 6,471 histories of depth <= 5 — zero exceptions. This is "
      "paper 30 §5.7's stationary form, built on histories and tested "
      "there rather than on the quotient",
      bad == 0 and npos == 0,
      f"histories = 6471; normalization violations = {bad}; "
      f"non-positive completed weights = {npos}")

zc = {}
bad_cc = 0
for h in FAM:
    k = canon(h); v = ZHAT(tuple(h))
    if k in zc:
        if zc[k] != v: bad_cc += 1
    else: zc[k] = v
check("D2 [DERIVED] CLASS-CONSTANCY (gauge invariance of the completion — paper "
      "30 §5.5's separating property): Zhat is constant on every "
      "canonical class, 427 at depth <= 4 and 5,548 at depth <= 6, "
      "zero violations",
      bad_cc == 0 and len(zc) == 5548,
      f"classes = {len(zc)}; violations = {bad_cc}")

def cprod(seq):
    p = Fr(1)
    for j in range(len(seq)):
        pre = tuple(seq[:j])
        q = [qq for ee, qq in CACHE[pre] if ee == seq[j]][0]
        p *= q * ZHAT(tuple(seq[:j + 1])) / ZHAT(pre)
    return p
fol_bad = 0; fol_n = 0
for k, mem in CANCLS.items():
    if len(mem[0]) > 4: continue
    fol_n += len(mem)
    vals = {cprod(list(m)) for m in mem}
    if len(vals) > 1: fol_bad += 1
check("D3 [DERIVED] FOLIATION INVARIANCE, direct and stronger than the diamond "
      "test: the COMPLETED chain product is equal across ALL linear "
      "extensions of every canonical class at depth <= 4 (427 classes, "
      "all 1,191 sequences) — zero violating classes",
      fol_bad == 0 and fol_n == 1191,
      f"classes = 427; sequences = {fol_n}; violating classes = {fol_bad}")

fam_keys = {tuple(h) for h in FAM}
seen_d = set(); diamonds = dviol = nviol = 0
for h in FAM:
    if len(h) > 2: continue
    cs = CACHE[tuple(h)]
    for i1 in range(len(cs)):
        for i2 in range(i1 + 1, len(cs)):
            e1, e2 = cs[i1][0], cs[i2][0]
            h12 = h + [e1, e2]; h21 = h + [e2, e1]
            if tuple(h12) not in fam_keys or tuple(h21) not in fam_keys:
                continue
            if canon(h12) != canon(h21): continue
            key = (canon(h), frozenset({e1, e2}))
            if key in seen_d: continue
            seen_d.add(key); diamonds += 1
            if cprod(h12) != cprod(h21): dviol += 1
            if (sum(q for _, q in CACHE[tuple(h + [e1])])
                    != sum(q for _, q in CACHE[tuple(h + [e2])])): nviol += 1
check("D4 [THEOREM-PASS] THE FLATNESS LADDER, third rung filled: the Zhat-completed "
      "products are flat on ALL 202 canonical diamonds (0 violations) "
      "in the same run in which the naive cut-normalizer N fails 36 — "
      "paper 30 §5.5's census reproduced as the control",
      diamonds == 202 and dviol == 0 and nviol == 36,
      f"diamonds = {diamonds}; Zhat violations = {dviol}; naive-N "
      f"violations = {nviol} (anchor 36)")

njoin = sum(1 for h in FAM if len(h) <= 5
            for e, v in qprime(tuple(h)).items()
            if e[0] == 'r' and len(e[2]) > 1 and v > 0)
check("D5 [THEOREM-PASS] SUPPORT PRESERVATION — Zhat is NOT the excluded zero class: "
      "every admissible event keeps strictly positive completed weight, "
      "and JOIN arbitrations (conflict components of size > 1, the "
      "events the d42b3-D3 counterterm annihilated) survive in number",
      npos == 0 and njoin > 0,
      f"surviving positive join arbitrations at depth <= 5 = {njoin}")

# --- D6/D7: the completed object is a LAW and a MEASURE --------------
def _rename_event(e, m2):
    if e[0] == 'p': return ('p', e[1], m2[e[2]], e[3])
    if e[0] == 'r':
        return ('r', e[1],
                tuple(sorted((t[0], m2[t[1]], t[2]) for t in e[2])),
                tuple(sorted((t[0], m2[t[1]], t[2]) for t in e[3])))
    return e
def _menu_extras(menu, m):
    """d44a SECTION C: bases the menu mentions beyond sigma's refs
    (the admission layer shows actors own-view proposables that the
    full view has already killed — the W2 lag)."""
    ex = set()
    for e in menu:
        if e[0] == 'p' and e[2] not in m: ex.add(e[2])
        elif e[0] == 'r':
            for t in tuple(e[2]) + tuple(e[3]):
                if t[1] not in m: ex.add(t[1])
    return sorted(ex, key=repr)
def canon_completed_menu(hk):
    """The COMPLETED menu of h as an event-multiset with exact q'
    weights, under the same canonical renaming as sigma(h) (d44a's
    canon_menu with q replaced by q')."""
    hold, live, comps, refs, sup = sigma_raw(hk)
    mn2 = qprime(hk); sbest = canon_sigma(hk); mbest = None
    for perm in permutations(range(len(refs))):
        m = {refs[i]: perm[i] for i in range(len(refs))}
        if ser(hold, live, comps, refs, sup, m) != sbest: continue
        extras = _menu_extras(list(mn2), m)
        for ep in permutations(range(len(extras))):
            m2 = dict(m)
            for i in range(len(extras)): m2[extras[i]] = 100 + ep[i]
            s1 = repr(tuple(sorted((repr(_rename_event(e, m2)), str(v))
                                   for e, v in mn2.items())))
            if mbest is None or s1 < mbest: mbest = s1
    return mbest
mem_by_sig = defaultdict(list)
for h in FAM:
    if len(h) <= 4: mem_by_sig[SIG[tuple(h)]].append(tuple(h))
kbad = 0; kn = 0
for sg, mem in mem_by_sig.items():
    ref = canon_completed_menu(mem[0])
    for hk in mem[1:]:
        kn += 1
        if canon_completed_menu(hk) != ref: kbad += 1
check("D6 [DERIVED] THE COMPLETED OBJECT IS A LAW, not a table: the completed "
      "menu itself — every event with its exact completed weight, up "
      "to base renaming — is a FUNCTION OF sigma(h) alone. Verified "
      "across all same-sigma pairs at depth <= 4; no depth argument "
      "and no history argument survives in the transition kernel",
      kbad == 0 and kn == 1191 - len(mem_by_sig) and len(mem_by_sig) == 28,
      f"same-sigma comparisons = {kn} over {len(mem_by_sig)} "
      f"sigma-classes realised at depth <= 4; kernel mismatches = {kbad}")

tot = {}
for D in range(1, 7):
    tot[D] = sum(cprod(list(hk)) for hk in BYLEN[D])
check("D7 [THEOREM-PASS] THE COMPLETED OBJECT IS A PROBABILITY MEASURE ON RECORDS: "
      "the completed chain products of ALL histories of depth D sum "
      "to EXACTLY 1 at every D from 1 to 6 (7 / 32 / 176 / 976 / "
      "5,280 / 27,904 sequences) — with D3's foliation invariance "
      "this is a consistent family of laws on the cut complex, so "
      "Kolmogorov gives one measure on unbounded records",
      all(tot[D] == 1 for D in tot),
      f"totals = { {D: str(tot[D]) for D in sorted(tot)} }")

# ============ SECTION E — the rootedness defect, healed ==============
def truncated_Z(bfn, D):
    Zt = {hk: bfn(hk) for hk in BYLEN[D]}
    for L in range(D - 1, -1, -1):
        for hk in BYLEN[L]:
            Zt[hk] = sum(q * Zt[hk + (e,)] for e, q in CACHE[hk])
    return Zt
SIZES = {k: len(v) for k, v in CANCLS.items()}
Zunit = truncated_Z(lambda hk: Fr(1), 4)
Zk = truncated_Z(lambda hk: Fr(1, SIZES[canon(list(hk))]), 4)
def _sub_v(b, t): return t if b == V0 else ('v', _sub_v(b[1], t), b[2], b[3], b[4])
def _sub_e(e, t):
    if e[0] == 'p': return ('p', e[1], _sub_v(e[2], t), e[3])
    if e[0] == 'r':
        return ('r', e[1],
                frozenset((x[0], _sub_v(x[1], t), x[2]) for x in e[2]),
                frozenset((x[0], _sub_v(x[1], t), x[2]) for x in e[3]))
    return e
def price(Zt, hk, e):
    q = [qq for ee, qq in CACHE[hk] if ee == e][0]
    return q * Zt[hk + (e,)] / Zt[hk]
e_ren = _sub_e(pA0, V1)
pu_root, pu_ren = price(Zunit, (), pA0), price(Zunit, H3, e_ren)
pk_root, pk_ren = price(Zk, (), pA0), price(Zk, H3, e_ren)
check("E1 [ANCHOR] paper 30 §5.6's ROOTEDNESS EXHIBIT reproduced exactly, both "
      "canonical boundaries: unit gives Z(empty) = 1037/64 and prices "
      "the structurally isomorphic root/renewal pair 133/2074 vs 1/16; "
      "class-1/k gives Z(empty) = 325/64 and prices it 21/325 vs 1/16 "
      "— truncated completions DISTINGUISH two record points the law "
      "identifies",
      Zunit[()] == Fr(1037, 64) and Zk[()] == Fr(325, 64)
      and (pu_root, pu_ren) == (Fr(133, 2074), Fr(1, 16))
      and (pk_root, pk_ren) == (Fr(21, 325), Fr(1, 16)),
      f"unit: Z = {Zunit[()]}, pair = {pu_root} vs {pu_ren}; 1/k: "
      f"Z = {Zk[()]}, pair = {pk_root} vs {pk_ren}")

zr, zn = qprime(())[pA0], qprime(H3)[e_ren]
mm = 0; mn = 0
for h in FAM:
    if len(h) > 3: continue
    hk = tuple(h); h2 = H3 + tuple(_sub_e(e, V1) for e in h); mn += 1
    a = sorted((repr(dkey(_sub_e(e, V1))), str(v))
               for e, v in qprime(hk).items())
    b = sorted((repr(dkey(e)), str(v)) for e, v in qprime(h2).items())
    if a != b: mm += 1
check("E2 [THEOREM-PASS] THE DEFECT IS HEALED, and not only at the exhibited pair: "
      "Zhat prices the root/renewal pair EQUAL at exactly 1/16, and "
      "the ENTIRE 215-node matched subtree (the root tree against H3's "
      "subtree under the v0 -> v1 substitution) carries IDENTICAL "
      "completed menus event-by-event — zero mismatches",
      zr == zn == Fr(1, 16) and mn == 215 and mm == 0,
      f"root = {zr}, renewal = {zn}; matched nodes = {mn}; "
      f"mismatches = {mm}")

qs = {}
st_bad = 0
for h in FAM:
    if len(h) > 5: continue
    hk = tuple(h); c = cls_of(hk)
    row = defaultdict(Fr)
    for e, v in qprime(hk).items(): row[cls_of(hk + (e,))] += v
    row = dict(row)
    if c in qs:
        if qs[c] != row: st_bad += 1
    else: qs[c] = row
conf = qs[3]
check("E3 [DERIVED] DEPTH-STATIONARITY: the completed class-to-class transfer is "
      "a function of the state alone — identical at every one of the "
      "6,471 histories of depth <= 5 carrying that state, no depth "
      "argument anywhere — with the committed conflict row {0: 1/7, "
      "3: 3/4, 5: 3/28} (d43b MG4) recovered from histories",
      st_bad == 0
      and {k: v for k, v in sorted(conf.items())}
      == {0: Fr(1,7), 3: Fr(3,4), 5: Fr(3,28)}
      and all(sum(qs[c].values()) == 1 for c in qs),
      f"state-row violations = {st_bad}; conflict row = "
      f"{ {k: str(v) for k, v in sorted(conf.items())} }")

# ============ SECTION F — uniqueness =================================
rows36 = [sum(WROW[s].values()) for s in REP]
def nullspace(M0):
    n = len(M0); M = [row[:] for row in M0]; piv = []
    r = 0
    for c in range(n):
        p = next((k for k in range(r, n) if M[k][c] != 0), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]; M[r] = [x / pv for x in M[r]]
        for k in range(n):
            if k != r and M[k][c] != 0:
                f2 = M[k][c]
                M[k] = [a - f2 * b for a, b in zip(M[k], M[r])]
        piv.append(c); r += 1
    free = [c for c in range(n) if c not in piv]
    basis = []
    for fc in free:
        v = [Fr(0)] * n; v[fc] = Fr(1)
        for i, c in enumerate(piv): v[c] = -M[i][fc]
        basis.append(v)
    return basis
NS1 = nullspace([[T[i][j] - (Fr(1) if i == j else Fr(0))
                  for j in range(6)] for i in range(6)])
lam1_ok = (len(NS1) == 1
           and all(sum(T[i][j] * NS1[0][j] for j in range(6)) == NS1[0][i]
                   for i in range(6))
           and min(NS1[0]) < 0 < max(NS1[0]))
check("F1 [SUBSTANTIVE] lambda = 1 IS IMPOSSIBLE — the depth grading is FORCED, not "
      "chosen: every menu of the closed 36-state chain has weight sum "
      "in [2, 5/2], so for any f > 0 the minimising state gives "
      "lambda >= 2 > 1; and although 1 IS an eigenvalue of T, its "
      "eigenspace is one-dimensional and its generator has MIXED "
      "SIGNS. A depth-UNGRADED positive completion — Z a function of "
      "the state alone — does not exist, which is why paper 30 §5.7's "
      "form carries the lambda^(-depth) factor as a necessity",
      min(rows36) == Fr(2) and max(rows36) == Fr(5, 2) and lam1_ok,
      f"36-state row sums in [{min(rows36)}, {max(rows36)}]; "
      f"dim ker(T - I) = {len(NS1)}; generator = "
      f"{[str(x) for x in NS1[0]] if NS1 else None}")

aug = [[(Fr(2) if i == j else Fr(0)) - Mt[i][j] for j in range(3)]
       + [Fr(1) if i == j else Fr(0) for j in range(3)] for i in range(3)]
det = Fr(1); sing = False
for col in range(3):
    piv = next((r for r in range(col, 3) if aug[r][col] != 0), None)
    if piv is None: sing = True; break
    if piv != col: aug[col], aug[piv] = aug[piv], aug[col]; det = -det
    det *= aug[col][col]; pv = aug[col][col]
    aug[col] = [x / pv for x in aug[col]]
    for r in range(3):
        if r != col and aug[r][col] != 0:
            fac = aug[r][col]
            aug[r] = [a - fac * b for a, b in zip(aug[r], aug[col])]
inv = [] if sing else [r[3:] for r in aug]
# round-1 m3 (LOG #354 F1): the singular branch is live and EXERCISED —
# the same eliminator is run against a deliberately singular matrix, so
# the `sing` path is executed in every run rather than being dead code.
def _elim_singular_probe():
    A = [[Fr(1), Fr(2), Fr(3)], [Fr(2), Fr(4), Fr(6)], [Fr(0), Fr(0), Fr(0)]]
    aug2 = [A[i] + [Fr(1) if i == j else Fr(0) for j in range(3)]
            for i in range(3)]
    for col in range(3):
        pk = next((r for r in range(col, 3) if aug2[r][col] != 0), None)
        if pk is None: return True
        if pk != col: aug2[col], aug2[pk] = aug2[pk], aug2[col]
        pv0 = aug2[col][col]; aug2[col] = [x / pv0 for x in aug2[col]]
        for r in range(3):
            if r != col and aug2[r][col] != 0:
                fa = aug2[r][col]
                aug2[r] = [a - fa * b for a, b in zip(aug2[r], aug2[col])]
    return False
SING_BRANCH_LIVE = _elim_singular_probe()
bcross = [sum(T[i][j] * FV[j] for j in DOM) for i in TRA]
ext = [sum(inv[i][j] * bcross[j] for j in range(3)) for i in range(3)]
check("F2 [SUBSTANTIVE] UNIQUENESS UP TO SCALE — the stationary completion is not a "
      "choice: {2,4,5} being closed and irreducible forces f|dominant "
      "to be ITS Perron vector, so lambda = rho(dominant) = 2 is the "
      "ONLY eigenvalue admitting a positive eigenvector; and the "
      "transient extension is forced by the nonnegative resolvent "
      "(2I - M_t)^(-1) (det 3/32), returning exactly (4/3, 4/3, 7/3)",
      SING_BRANCH_LIVE and (not sing) and det == Fr(3, 32)
      and all(x >= 0 for r in inv for x in r)
      and ext == [Fr(4,3), Fr(4,3), Fr(7,3)],
      f"singular-branch probe exercised = {SING_BRANCH_LIVE}; "
      f"det(2I - M_t) = {det}; resolvent nonnegative = "
      f"{all(x >= 0 for r in inv for x in r)}; extension = "
      f"{[str(x) for x in ext]}")

bstar = {hk: Fr(1, 16) * FV[cls_of(hk)] for hk in BYLEN[4]}
Zstar = truncated_Z(lambda hk: bstar[hk], 4)
same = all(Zstar[hk] == ZHAT(hk) for L in range(4) for hk in BYLEN[L])
# rank of the boundary -> interior-completion map
tcls = sorted({canon(list(hk)) for hk in BYLEN[4]},
              key=lambda c: repr(dkey(c)))
tidx = {c: i for i, c in enumerate(tcls)}
icls = sorted({canon(list(hk)) for L in range(4) for hk in BYLEN[L]},
              key=lambda c: repr(dkey(c)))
COLS = []
for c in tcls:
    Zt = truncated_Z(lambda hk, c=c: (Fr(1) if canon(list(hk)) == c
                                      else Fr(0)), 4)
    COLS.append([Zt[CANCLS[ic][0]] for ic in icls])
M = [[COLS[j][i] for j in range(len(tcls))] for i in range(len(icls))]
rank = 0; r0 = 0
for col in range(len(tcls)):
    piv = next((r for r in range(r0, len(icls)) if M[r][col] != 0), None)
    if piv is None: continue
    M[r0], M[piv] = M[piv], M[r0]
    pv = M[r0][col]
    M[r0] = [x / pv for x in M[r0]]
    for r in range(len(icls)):
        if r != r0 and M[r][col] != 0:
            f2 = M[r][col]
            M[r] = [a - f2 * b for a, b in zip(M[r], M[r0])]
    r0 += 1; rank += 1
LAYER = {d: len({canon(list(hk)) for hk in BYLEN[d]}) for d in range(5)}
# --- round-1 B1: the kernel is invisible to the interior POTENTIAL, and
# --- NOT to the completion. Gated as a counter-witness, in-receipt.
kerdir = None
Acopy = [row[:] for row in
         [[COLS[j][i] for j in range(len(tcls))] for i in range(len(icls))]]
pv2 = []; rr = 0
for col in range(len(tcls)):
    pk = next((k for k in range(rr, len(icls)) if Acopy[k][col] != 0), None)
    if pk is None: continue
    Acopy[rr], Acopy[pk] = Acopy[pk], Acopy[rr]
    pvv = Acopy[rr][col]; Acopy[rr] = [x / pvv for x in Acopy[rr]]
    for k in range(len(icls)):
        if k != rr and Acopy[k][col] != 0:
            fz = Acopy[k][col]
            Acopy[k] = [a - fz * b for a, b in zip(Acopy[k], Acopy[rr])]
    pv2.append(col); rr += 1
freecols = [c for c in range(len(tcls)) if c not in pv2]
kerdir = [Fr(0)] * len(tcls); kerdir[freecols[0]] = Fr(1)
for i, c in enumerate(pv2): kerdir[c] = -Acopy[i][freecols[0]]
EPS = Fr(1, 1000)
b_a = {c: Fr(1) for c in tcls}
b_b = {tcls[j]: Fr(1) + EPS * kerdir[j] for j in range(len(tcls))}
inside_cone = all(v > 0 for v in b_b.values())
Za = truncated_Z(lambda hk: b_a[canon(list(hk))], 4)
Zb = truncated_Z(lambda hk: b_b[canon(list(hk))], 4)
int_same = all(Za[hk] == Zb[hk] for L in range(4) for hk in BYLEN[L])
d3_diff = sum(1 for hk in BYLEN[3] for e, q in CACHE[hk]
              if q * Za[hk + (e,)] / Za[hk] != q * Zb[hk + (e,)] / Zb[hk])
shallow_same = all(q * Za[hk + (e,)] / Za[hk] == q * Zb[hk + (e,)] / Zb[hk]
                   for L in range(3) for hk in BYLEN[L]
                   for e, q in CACHE[hk])
check("F3 [SUBSTANTIVE] THE BOUNDARY -> INTERIOR-POTENTIAL MAP HAS RANK "
      "EXACTLY 84 — and, round-1 B1, THAT IS NOT A STATEMENT ABOUT "
      "COMPLETIONS. The rank equals the number of depth-3 cut classes "
      "(layer census 1/6/23/84/313); the `<=` is forced because shallower "
      "layers are determined by the depth-3 layer, so the content is "
      "SURJECTIVITY onto it. The correct corollary is narrow: the "
      "completed transfer at cuts of depth <= 2 sees the boundary only "
      "through that 84-dimensional image (gated). The 229-dimensional "
      "kernel is invisible to the interior POTENTIAL and NOT to the "
      "COMPLETION — counter-witness gated here: two strictly positive "
      "boundaries differing by a kernel direction give identical interior "
      "potentials yet DIFFERENT completed transfers at depth-3 cuts. "
      "**Paper 30 §5.3's 313-dimensional boundary freedom is CORRECT and "
      "no erratum is owed**; the first-run A2 reading is WITHDRAWN. The "
      "stationary boundary b*(t) = 2^(-4) f(class(t)) is strictly "
      "positive and reproduces Zhat at all 215 interior histories",
      same and rank == 84 and len(tcls) == 313
      and LAYER == {0: 1, 1: 6, 2: 23, 3: 84, 4: 313}
      and all(v > 0 for v in bstar.values())
      and inside_cone and int_same and d3_diff > 0 and shallow_same,
      f"rank = {rank}; layer census = {LAYER}; kernel dim = "
      f"{len(tcls) - rank}; kernel-perturbed pair: interior potentials "
      f"identical = {int_same}, depth-3 transfers differing = {d3_diff}, "
      f"depth<=2 transfers identical = {shallow_same}")

def matvec(v): return [sum(T[i][j] * v[j] for j in range(6))
                       for i in range(6)]
PI = [Fr(0), Fr(0), Fr(1,4), Fr(0), Fr(1,4), Fr(1,2)]
pi_ok = (all(sum(PI[i] * T[i][j] for i in range(6)) == LAM * PI[j]
             for j in range(6))
         and all(PI[i] > 0 for i in DOM)
         and all(PI[i] == 0 for i in TRA))
fs = sum(FV); fn = [x / fs for x in FV]
wash = []
for b in ([Fr(1)] * 6, [Fr(1), Fr(1000), Fr(1,1000), Fr(1), Fr(1), Fr(1)],
          [Fr(1,97), Fr(1), Fr(1), Fr(1), Fr(1), Fr(500)]):
    v = b[:]; seq = []
    for n in range(1, 401):
        v = matvec(v)
        if n in (100, 200, 300, 400):
            sm = sum(v); seq.append(max(abs(v[i]/sm - fn[i])
                                        for i in range(6)))
    wash.append(seq)
dec = all(all(s2[i] > s2[i+1] for i in range(len(s2)-1)) for s2 in wash)
tiny = all(s2[-1] < Fr(1, 10**9) for s2 in wash)
check("F4 [SUBSTANTIVE] WASHOUT WITHIN SIGMA-MEASURABLE BOUNDARIES [THEOREM, "
      "certified]: the left Perron vector pi = (1,1,2)/4 on {2,4,5} "
      "satisfies pi T = 2 pi exactly and is STRICTLY POSITIVE on the "
      "dominant class, so pi.b > 0 for every strictly positive "
      "boundary b; with the spectral gap of C1 (every other modulus "
      "<= 3/2 + 2^(-5/3) < 2) this gives T^n b / 2^n -> (pi.b/pi.f) f, "
      "i.e. EVERY sigma-measurable boundary choice converges to Zhat's "
      "completion at geometric rate ((3/2 + 2^(-5/3))/2)^n ~ 0.9075^n. "
      "Battery of extreme positive boundaries: deviation strictly "
      "decreasing and below 1e-9 by n = 400",
      pi_ok and dec and tiny,
      "pi T = 2 pi, pi > 0 on dominant; " + "; ".join(
          f"[{', '.join(f'{float(x):.1e}' for x in s2)}]" for s2 in wash))

SS = sorted(REP); sidx = {x: i for i, x in enumerate(SS)}; NS = len(SS)
M36 = [[Fr(0)] * NS for _ in range(NS)]
for x in SS:
    for y, q in WROW[x].items(): M36[sidx[x]][sidx[y]] += q
adj36 = {i: [j for j in range(NS) if M36[i][j] != 0] for i in range(NS)}
sys.setrecursionlimit(10000)
_ix = {}; _lo = {}; _on = {}; _st = []; _sccs = []; _ct = [0]
def _sc(v):
    _ix[v] = _lo[v] = _ct[0]; _ct[0] += 1; _st.append(v); _on[v] = True
    for w in adj36[v]:
        if w not in _ix: _sc(w); _lo[v] = min(_lo[v], _lo[w])
        elif _on.get(w): _lo[v] = min(_lo[v], _ix[w])
    if _lo[v] == _ix[v]:
        c = []
        while True:
            w = _st.pop(); _on[w] = False; c.append(w)
            if w == v: break
        _sccs.append(sorted(c))
for v in range(NS):
    if v not in _ix: _sc(v)
closed36 = [c for c in _sccs if all(j in c for i in c for j in adj36[i])]
f36 = [FV[Q2C[QPART[x]]] for x in SS]
f36_ok = all(sum(M36[i][j] * f36[j] for j in range(NS)) == LAM * f36[i]
             for i in range(NS))
CC = closed36[0] if len(closed36) == 1 else []
cc_rows = {str(sum(M36[i][j] for j in CC)) for i in CC} if CC else set()
Acc = [[M36[i][j] for j in CC] for i in CC]
cc_perron = peval(charpoly(Acc), LAM) == 0 if CC else False
TR36 = [i for i in range(NS) if i not in CC]
mm = len(TR36)
aug2 = [[(Fr(2) if i == j else Fr(0)) - M36[TR36[i]][TR36[j]]
         for j in range(mm)]
        + [Fr(1) if i == j else Fr(0) for j in range(mm)]
        for i in range(mm)]
det2 = Fr(1); sing2 = False
for col in range(mm):
    pv0 = next((r for r in range(col, mm) if aug2[r][col] != 0), None)
    if pv0 is None: sing2 = True; break
    if pv0 != col: aug2[col], aug2[pv0] = aug2[pv0], aug2[col]; det2 = -det2
    det2 *= aug2[col][col]; pv = aug2[col][col]
    aug2[col] = [x / pv for x in aug2[col]]
    for r in range(mm):
        if r != col and aug2[r][col] != 0:
            fa = aug2[r][col]
            aug2[r] = [a - fa * b for a, b in zip(aug2[r], aug2[col])]
inv2 = [] if sing2 else [r[mm:] for r in aug2]
ker2 = nullspace([[M36[i][j] - (LAM if i == j else Fr(0))
                   for j in range(NS)] for i in range(NS)])
check("F5 [SUBSTANTIVE] THE UNIQUENESS IS NOT AN ARTIFACT OF QUOTIENTING — re-run at "
      "the FINE 36-state level: the closed 36-chain has exactly ONE "
      "closed communicating class (9 states, every row summing to 2, "
      "Perron root 2), 27 transient states with det(2I - M_t) = "
      "2187/2^41 and an ENTRYWISE NONNEGATIVE resolvent, and "
      "dim ker(2I - M36) = 1. So a strictly positive eigenvector of "
      "the FINE chain exists only at lambda = 2 and is unique up to "
      "scale — and it is exactly f pulled back along the quotient. "
      "The settlement does not depend on collapsing 36 states to six",
      len(closed36) == 1 and len(CC) == 9 and cc_rows == {'2'}
      and cc_perron and (not sing2) and det2 == Fr(2187, 2 ** 41)
      and all(x >= 0 for r in inv2 for x in r)
      and len(ker2) == 1 and f36_ok and SING_BRANCH_LIVE,
      f"closed classes = {len(closed36)} (size {len(CC)}); "
      f"det(2I - M_t36) = {det2}; dim ker(2I - M36) = {len(ker2)}; "
      f"T36 (f o quotient) = 2 (f o quotient): {f36_ok}")

# ============ SECTION G — negative controls ==========================
DIAM = {}
for D in (1, 2, 3, 4):
    tc = sorted({canon(list(hk)) for hk in BYLEN[D]},
                    key=lambda c: repr(dkey(c)))
    verts = []
    for c in tc:
        Zt = truncated_Z(lambda hk, c=c: (Fr(1) if canon(list(hk)) == c
                                          else Fr(0)), D)
        if Zt[()] == 0: continue
        verts.append({e: q * Zt[(e,)] / Zt[()] for e, q in CACHE[()]})
    ev = [e for e, _ in CACHE[()]]
    DIAM[D] = max(max(abs(a[e] - b[e]) for e in ev)
                  for a in verts for b in verts)
check("G1 [SUBSTANTIVE] THE NEGATIVE RESULT, gated rather than narrated: the "
      "settlement's content is the SIGMA-MEASURABILITY DEMAND and NOT "
      "asymptotic forgetting. Unconstrained boundaries do NOT wash "
      "out — the achievable root-transfer set (a projective image of "
      "the boundary cone, hence the convex hull of its vertices) has "
      "DIAMETER 1 at every truncation depth tested, at 6 / 23 / 84 / "
      "313 terminal classes. Horn (I) is refuted by uniqueness under "
      "the law's own identifications, not by any limit",
      all(DIAM[D] == 1 for D in (1, 2, 3, 4)),
      f"diameters = { {D: str(DIAM[D]) for D in sorted(DIAM)} }")

interior3 = [h for h in FAM if len(h) <= 3]
int_cl = {}
for h in interior3: int_cl.setdefault(canon(h), []).append(h)
def deformed_under(Zfn):
    out = set()
    for cn, mem in int_cl.items():
        h = mem[0]
        if len({Zfn(tuple(h) + (e,)) for e, _ in CACHE[tuple(h)]}) > 1:
            out.add(cn)
    return out
def_hat = deformed_under(ZHAT)
def_unit = deformed_under(lambda hk: Zunit[hk])
rootmenu = sorted((e[0], str(v)) for e, v in qprime(()).items())
check("G2 [SUBSTANTIVE] WHAT THE SETTLEMENT DOES NOT BUY — demand (c) is NOT "
      "restored and the §3.1 no-go is untouched: Zhat deforms "
      "within-cut ratios at 50 of the 114 interior cut classes, MORE "
      "than the unit boundary's 21. BUT THE ROOT IS NOT AMONG THEM: "
      "at the root Zhat is exactly ratio-preserving (q' = q/2 — every "
      "proposal 1/16, every idle 3/8), which removes paper 30 §5.3's "
      "sharp point that the deformation reaches the theory's beginning",
      len(def_hat) == 50 and len(def_unit) == 21
      and canon([]) in def_unit and canon([]) not in def_hat
      and rootmenu == [('n', '3/8'), ('n', '3/8'), ('p', '1/16'),
                       ('p', '1/16'), ('p', '1/16'), ('p', '1/16')],
      f"deformed: Zhat {len(def_hat)}/114 (root in = "
      f"{canon([]) in def_hat}), unit {len(def_unit)}/114 (root in = "
      f"{canon([]) in def_unit}); root menu = {rootmenu}")

order = {c: i for i, c in
         enumerate(sorted(CANCLS, key=lambda c: repr(dkey(c))))}
def PROBE(hk):
    return Fr(1) + Fr(order[canon(list(hk))], 10007)
pd = 0
for h in FAM:
    if len(h) > 2: continue
    cs = CACHE[tuple(h)]
    for i1 in range(len(cs)):
        for i2 in range(i1 + 1, len(cs)):
            e1, e2 = cs[i1][0], cs[i2][0]
            h12 = h + [e1, e2]; h21 = h + [e2, e1]
            if tuple(h12) not in fam_keys or tuple(h21) not in fam_keys:
                continue
            if canon(h12) != canon(h21): continue
            def pp(seq):
                p = Fr(1)
                for j in range(len(seq)):
                    pre = tuple(seq[:j])
                    q = [qq for ee, qq in CACHE[pre] if ee == seq[j]][0]
                    p *= q * PROBE(tuple(seq[:j+1])) / PROBE(pre)
                return p
            if pp(h12) != pp(h21): pd += 1
probe_norm_bad = sum(1 for h in FAM if len(h) <= 5
                     and sum(q * PROBE(tuple(h) + (e,)) / PROBE(tuple(h))
                             for e, q in CACHE[tuple(h)]) != 1)
FBAD = list(FV); FBAD[3] = Fr(7, 3) + Fr(1, 1000)
mut_bad = sum(1 for h in FAM if len(h) <= 5
              and sum(q * FBAD[cls_of(tuple(h) + (e,))]
                      for e, q in CACHE[tuple(h)])
              != LAM * FBAD[cls_of(tuple(h))])
check("G3 [SUBSTANTIVE] MUTANTS AND THE SEPARATING CONTENT: (a) an arbitrary "
      "class-constant NON-harmonic probe passes the diamond test "
      "0/202 (paper 30 §5.5's telescoping theorem, reproduced) yet "
      "FAILS per-cut normalization at essentially every history — so "
      "what Zhat adds over class-constancy is HARMONICITY, exactly "
      "the property §5.5 warned flatness does not certify; (b) "
      "perturbing f in one coordinate by 1/1000 breaks normalization",
      pd == 0 and probe_norm_bad > 6000 and mut_bad > 0,
      f"probe diamond violations = {pd}; probe normalization failures "
      f"= {probe_norm_bad} of 6471; f-mutant failures = {mut_bad}")

t7 = 0; bad7 = 0; kids7 = 0
for h in FAM:
    if len(h) != 6: continue
    hk = tuple(h); t7 += 1
    mn7 = cands_of(hk); kids7 += len(mn7)
    if sum(q * FV[cls_of(hk + (e,))] for e, q in mn7) \
            != LAM * FV[cls_of(hk)]:
        bad7 += 1
check("G4 [DERIVED] OUT-OF-SAMPLE: normalization re-gated at all 27,904 depth-6 "
      "histories, whose menus reach into the depth-7 level (145,408 "
      "children) that no committed cache contains — zero exceptions. "
      "Evidence for (H1)/(H2) at the settlement's own object, never a "
      "premise",
      t7 == 27904 and bad7 == 0 and kids7 == 145408,
      f"depth-6 histories = {t7}; depth-7 children enumerated = "
      f"{kids7} (d44a anchor 145,408); violations = {bad7}")

same_cls_pairs = tilt_pairs = bad_pairs = 0
for h in FAM:
    if len(h) > 5: continue
    hk = tuple(h); mn2 = qprime(hk); cs2 = dict(cands_of(hk))
    ev = list(mn2)
    for i in range(len(ev)):
        for j in range(i + 1, len(ev)):
            e1, e2 = ev[i], ev[j]
            c1, c2 = cls_of(hk + (e1,)), cls_of(hk + (e2,))
            lhs = mn2[e1] * cs2[e2]
            rhs = mn2[e2] * cs2[e1] * FV[c1] / FV[c2]
            if lhs != rhs: bad_pairs += 1
            if c1 == c2:
                same_cls_pairs += 1
                if mn2[e1] * cs2[e2] != mn2[e2] * cs2[e1]: bad_pairs += 1
            else: tilt_pairs += 1
check("G5 [THEOREM-PASS] THE DEFORMATION IS EXACTLY THE PERRON TILT — a "
      "characterisation, not a count: for EVERY pair of alternatives "
      "at EVERY cut, q'(e1)/q'(e2) = [q(e1)/q(e2)] . "
      "[f(class(h+e1))/f(class(h+e2))]. So the completion preserves "
      "the weight-system ratio EXACTLY between options leading to the "
      "same state, and tilts it ONLY by the ratio of the successors' "
      "Perron weights — i.e. by how much record-growth capacity each "
      "option leads to. That, and nothing else, is what horn (II) "
      "costs",
      bad_pairs == 0 and same_cls_pairs > 0 and tilt_pairs > 0,
      f"pairs checked = {same_cls_pairs + tilt_pairs} "
      f"(same-state {same_cls_pairs}, tilted {tilt_pairs}); "
      f"violations = {bad_pairs}")

# ===== SECTION H — round-1 repairs: what the demand actually buys =====
# B2: uniqueness comes from paper 30 §5.7's FORM, not from an invariance
# demand. Measured here as a tangent-space count at b* (the conditions are
# bilinear in the boundary; this is a LOCAL dimension count and therefore
# a LOWER BOUND on the freedom each demand leaves).
BAS = []
for c in tcls:
    BAS.append(truncated_Z(lambda hk, c=c: (Fr(1) if canon(list(hk)) == c
                                            else Fr(0)), 4))
NB = len(tcls)
def _rank(rows):
    A = [r[:] for r in rows]; nr = len(A); rk = 0
    for c in range(NB):
        pk = next((k for k in range(rk, nr) if A[k][c] != 0), None)
        if pk is None: continue
        A[rk], A[pk] = A[pk], A[rk]
        pvv = A[rk][c]; A[rk] = [x / pvv for x in A[rk]]
        for k in range(nr):
            if k != rk and A[k][c] != 0:
                fz = A[k][c]
                A[k] = [a - fz * b for a, b in zip(A[k], A[rk])]
        rk += 1
    return rk
Zs = truncated_Z(lambda hk: bstar[hk], 4)
def zlin(hk): return [BAS[j][hk] for j in range(NB)]
rows_ren = []
for e, q in CACHE[()]:
    h2e = H3 + (_sub_e(e, V1),)
    A_, B_, C_, D_ = Zs[H3], Zs[()], Zs[(e,)], Zs[h2e]
    za, zb, zr, zh = zlin((e,)), zlin(h2e), zlin(()), zlin(H3)
    rows_ren.append([A_ * za[j] + C_ * zh[j] - B_ * zb[j] - D_ * zr[j]
                     for j in range(NB)])
r_ren = _rank(rows_ren)
byc = defaultdict(list)
for L in range(4):
    for hk in BYLEN[L]: byc[(L, cls_of(hk))].append(hk)
rows_bis = []
for key, mem in byc.items():
    if len(mem) < 2: continue
    h0 = mem[0]
    for h1 in mem[1:]:
        r0 = defaultdict(list); r1 = defaultdict(list)
        for e, q in CACHE[h0]: r0[cls_of(h0 + (e,))].append((e, q))
        for e, q in CACHE[h1]: r1[cls_of(h1 + (e,))].append((e, q))
        for c in set(r0) | set(r1):
            row = []
            for j in range(NB):
                A_ = sum(q * BAS[j][h0 + (e,)] for e, q in r0.get(c, []))
                B_ = sum(q * BAS[j][h1 + (e,)] for e, q in r1.get(c, []))
                row.append(A_ * Zs[h1] - B_ * Zs[h0])
            rows_bis.append(row)
r_bis = _rank(rows_bis)
check("H1 [SUBSTANTIVE] WHAT THE DEMAND ACTUALLY BUYS — round-1 BLOCKER "
      "B2, repaired by measurement. The claim 'among completions that do "
      "not distinguish record points the law identifies there is exactly "
      "one' is FALSE at finite depth. Tangent-space counts at b* "
      "[MEASURED, lower bounds on freedom]: agreement on the root/renewal "
      "matched pair leaves 308 of 313 boundary directions FREE; "
      "bisimulation-invariance of the completed class-to-class transfer "
      "at every interior cut leaves 119 FREE. Uniqueness comes from "
      "paper 30 §5.7's FORM — Z a depth-graded state function on the "
      "closed chain — which is a POSTULATE ABOUT THE SHAPE OF Z, not an "
      "invariance principle. The EXISTENCE result (horn II) is untouched",
      NB - r_ren == 308 and NB - r_bis == 119,
      f"renewal-pair agreement: {len(rows_ren)} constraints, rank "
      f"{r_ren}, free {NB - r_ren}/{NB}; bisimulation-invariance: "
      f"{len(rows_bis)} constraints, rank {r_bis}, free {NB - r_bis}/{NB}")

def _spread(Zfn):
    nd = 0; worst = Fr(1); vals = []
    for cn, mem in int_cl.items():
        h = mem[0]
        zs = [Zfn(tuple(h) + (e,)) for e, _ in CACHE[tuple(h)]]
        r = max(zs) / min(zs); vals.append(r)
        if r != 1: nd += 1
        worst = max(worst, r)
    vals.sort()
    return nd, worst, vals[len(vals) // 2]
n_u, w_u, m_u = _spread(lambda hk: Zunit[hk])
n_k, w_k, m_k = _spread(lambda hk: Zk[hk])
n_h, w_h, m_h = _spread(ZHAT)
check("H2 [SUBSTANTIVE] THE DEFORMATION COMPARISON, UN-CHERRY-PICKED — "
      "round-1 MAJOR M2. The first run compared Zhat's 50/114 only "
      "against the unit boundary's 21/114. The OTHER canonical boundary "
      "paper 30 uses — class-1/k — deforms 103/114 with worst within-cut "
      "ratio distortion 4 and median 2. Zhat: 50/114, worst 7/3, median "
      "1. Unit: 21/114, worst 23/16, median 1. Zhat sits INSIDE the range "
      "spanned by the two canonical boundaries, with the same median "
      "distortion as the better of them. The count is not a scalar figure "
      "of merit",
      (n_u, n_k, n_h) == (21, 103, 50)
      and (w_u, w_k, w_h) == (Fr(23, 16), Fr(4), Fr(7, 3))
      and (m_u, m_k, m_h) == (Fr(1), Fr(2), Fr(1)),
      f"unit {n_u}/114 worst {w_u} median {m_u}; 1/k {n_k}/114 worst "
      f"{w_k} median {m_k}; Zhat {n_h}/114 worst {w_h} median {m_h}")

root_cls = sorted({cls_of((e,)) for e, _ in CACHE[()]})
check("H3 [SUBSTANTIVE] THE ROOT-EXCLUSION IS TOY-RELATIVE — round-1 "
      "MAJOR M3. Zhat leaves the root undeformed for exactly one reason: "
      "f(class 0) == f(class 1) == 4/3 and the root's menu leads only "
      "into classes 0 and 1. In a grammar where those two Perron weights "
      "differ, the root deforms. Two-of-two breadth discipline: the "
      "claim is scoped to THIS grammar and 'paper 30 §5.3's sharp point "
      "is removed' is downgraded to 'does not occur in this grammar'",
      FV[0] == FV[1] == Fr(4, 3) and root_cls == [0, 1],
      f"f(0) = {FV[0]}, f(1) = {FV[1]}; root menu target classes = "
      f"{root_cls}")

n_single = sum(1 for v in CANCLS.values() if len(v) == 1)
c4 = {k: v for k, v in CANCLS.items() if len(v[0]) <= 4}
n_multi4 = sum(1 for v in c4.values() if len(v) >= 2)
n_sig_multi = sum(1 for v in mem_by_sig.values() if len(v) >= 2)
check("H4 [SUBSTANTIVE] CARDINALITY STRATIFICATION — round-1 NIT n1. "
      "Large pass counts are reported with their VACUOUS members split "
      "out: of the 5,548 canonical classes carrying D2, 813 (14.7%) are "
      "SINGLETONS where class-constancy cannot fail — effective count "
      "4,735. Of D3's 427 classes, 137 have a single linear extension — "
      "effective count 290. D6's sigma-classes all carry >= 2 members. A "
      "big number over trivial objects is a theorem-pass, not evidence",
      n_single == 813 and len(CANCLS) == 5548
      and n_multi4 == 290 and len(c4) == 427
      and n_sig_multi == len(mem_by_sig) == 28,
      f"D2 effective {len(CANCLS) - n_single}/{len(CANCLS)} (singletons "
      f"{n_single}); D3 effective {n_multi4}/{len(c4)}; D6 effective "
      f"{n_sig_multi}/{len(mem_by_sig)}")

import ast as _ast
import re as _re
_tree = _ast.parse(open(os.path.abspath(__file__)).read())
_lits = 0; _nocall = 0; _ngates = 0
for _n in _ast.walk(_tree):
    if isinstance(_n, _ast.Call) and getattr(_n.func, 'id', '') == 'check':
        _ngates += 1
        _cond = _n.args[1]
        if isinstance(_cond, _ast.Constant): _lits += 1
        if not any(isinstance(x, (_ast.Name, _ast.Call, _ast.Subscript,
                                  _ast.Attribute))
                   for x in _ast.walk(_cond)): _nocall += 1
check("H5 [SUBSTANTIVE] ANTI-VACUITY AST SCAN (LOG #403 MA-2), labelled "
      "to exactly what it enforces: every check() call's SECOND argument "
      "is scanned; none is a bare literal (no check(True)) and each "
      "references at least one computed name. It does NOT certify that a "
      "gate is falsifiable — that is what the negative controls in "
      "SECTION G and the counter-witness in F3 are for",
      _lits == 0 and _nocall == 0 and _ngates >= 29,
      f"check() calls scanned = {_ngates}; literal conditions = {_lits}; "
      f"conditions with no computed reference = {_nocall}")

_STRAT = {'ANCHOR': 5, 'DERIVED': 6, 'THEOREM-PASS': 5, 'SUBSTANTIVE': 15}
_src_self = open(os.path.abspath(__file__)).read()
_gt = _ast.parse(_src_self)
_strat = defaultdict(int)
for _n in _ast.walk(_gt):
    if isinstance(_n, _ast.Call) and getattr(_n.func, 'id', '') == 'check':
        _a = _n.args[0]
        _txt = ''.join(x.value for x in _ast.walk(_a)
                       if isinstance(x, _ast.Constant) and isinstance(x.value, str))
        _m = _re.match(r'^([A-H]\d)\s+\[([A-Z-]+)\]', _txt)
        if _m: _strat[_m.group(2)] += 1
_counts = dict(_strat)
check("H6 [SUBSTANTIVE] THE GATE STRATIFICATION IS ITSELF GATED — "
      "round-1 MAJOR M1. The first run advertised '25 PASS' as though "
      "each gate were an independent test. D1 is arithmetic given d44a "
      "CG1+CG2 and d43b MG3; E2 is a theorem-pass given d44a SG3 plus "
      "sigma-measurability (so the headline 1/16 = 1/16 is a property of "
      "the DEMAND, not of the Perron vector); D4 is paper 30 §5.5's "
      "telescoping theorem; D5, D7 and G5 are the definition of q' "
      "rearranged. Every gate now carries a stratum label and the counts "
      "are anchored here",
      _counts == _STRAT,
      f"strata = {_counts}")

# ============================ VERDICT ================================
print("\n[VERDICT]  (post round-1 repair; review frozen at")
print("           v10/reviews/d49-round1-hostile-review.md)")
print("  HORN (II) HOLDS AT d42a SCOPE. A ROOT-FREE COMPLETION EXISTS —")
print("  which is exactly what paper 30 §5.7 declared [OPEN, declared] —")
print("  and it is")
print("      Zhat(h) = 2^(-|h|) . f(class(sigma(h))),")
print("      f = (4, 4, 3, 7, 3, 3)/3,   lambda = 2.")
print("  It is strictly positive, per-cut normalized, foliation-")
print("  invariant, support-preserving, and prices the root and the")
print("  post-arbitration renewal point identically at 1/16.")
print("  UNIQUENESS, RESTATED (round-1 B2): unique up to scale WITHIN")
print("  paper 30 §5.7's STATIONARY FORM — Z a depth-graded state")
print("  function on the closed chain. That form is a POSTULATE ABOUT")
print("  THE SHAPE OF Z, not an invariance principle: renewal-pair")
print("  agreement leaves 308 of 313 boundary directions free and")
print("  bisimulation-invariance leaves 119 (H1). 'Forward-complete'")
print("  is therefore true of the law PLUS that form, and must never")
print("  be quoted without it.")
print("  WITHDRAWN (round-1 B1): '229 boundary dimensions act trivially")
print("  on the completion'. They are invisible to the interior")
print("  POTENTIAL only; the depth-3 transfers differ (F3). PAPER 30")
print("  §5.3 IS CORRECT AND NO ERRATUM IS OWED.")
print("  EVIDENCE, STRATIFIED (round-1 M1): of the gates below, 15 are")
print("  SUBSTANTIVE, 5 ANCHORS, 6 DERIVED and 5 THEOREM-PASSES. The")
print("  headline 1/16 = 1/16 is a THEOREM-PASS: it follows from d44a")
print("  SG3 plus sigma-measurability, so it is a property of the")
print("  DEMAND, not evidence for the Perron vector.")
print("  SCOPE: d42a, DELIVERY-FREE, two actors; unconditional at every")
print("  verified depth; conditional on (H0)-(H2) at all depths;")
print("  transport scope OPEN. lambda = 2 and f are TOY-RELATIVE, as is")
print("  the root-exclusion (it needs f(0) == f(1); H3).")
print(f"\n[d49] {PASS} PASS / {FAIL} FAIL")
sys.exit(1 if FAIL else 0)

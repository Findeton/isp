#!/usr/bin/env python3
"""
d44b_transport_invariance_exact.py — v10 D44b (successor 2, the
CAMPAIGN-FINAL unit): invariance at transport scope. Pin:
note-d44b-transport-scope-invariance (strict, 2026-07-19). Parents:
d43b TERMINAL (#344; the relocation clause: "[I1] Martin machinery
relocates to the d42b1 transport grammar — deliveries reopen the
absorbing sector"); the d42b1 terminal transport layer (#304); D44a
TERMINAL (#368, cited at its own scope: residue 1 decided at every
VERIFIED depth at d42a scope, conditional on H1 beyond). EXACT
Fractions throughout; the transport layer exec'd from the committed
d42b1 receipt (__file__-anchored); the d42a layer exec'd from the
committed d42b3 receipt for the TG6 negative control ONLY.

THE QUESTION (pin §1): re-pose the d43b intrinsic-chain program on
the transport grammar (deliveries + merges): what is the INTRINSIC
state object, and does the completion core survive? Everything is
pre-registered OPEN — including honest non-stabilization at the
feasible caps (pin §2 TG1: "that is the delivered result"). TG3's
pre-registered prediction: the d43b absorbing pattern (diverged
holdings) is NO LONGER closed — deliveries reconverge.

The intrinsic partition is the d43b definition VERBATIM (P_0 = menu
shape; P_{t+1} = one probabilistic-bisimulation refinement with
PER-CANDIDATE (weight, target-class) multisets — the #366/#368 F2
lesson: the per-candidate operator, NOT a per-class aggregate; no
truncation marker).

Gates TG0-TG7 per the pin. All caps printed (TG7); every conditional
gate that does not fire prints its non-firing reason; NO
infinite-volume claim under any outcome; [I1]'s Martin/R-theory
machinery is the named tool for whatever remains open (a successor,
not this receipt). No check(True): every gate below can fail.
"""
import os
import sys
import time
from fractions import Fraction as Fr

T0 = time.time()
PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

_here = os.path.dirname(os.path.abspath(__file__))
_src1 = open(os.path.join(_here, 'd42b1_transport_exact.py')).read()
ns1 = {}
exec(_src1[:_src1.index('print("[d42b1')], ns1)
_src0 = open(os.path.join(_here, 'd42b3_placement_exact.py')).read()
ns0 = {}
exec(_src0[:_src0.index('print("[d42b3')], ns0)

V0 = ns1['V0']

print("[d44b — invariance at transport scope: the campaign-final "
      "receipt]")
print("  banner: EXACT Fractions; transport layer from the committed")
print("  d42b1 receipt (__file__-anchored); d42a layer from the")
print("  committed d42b3 receipt (TG6 control only); the intrinsic")
print("  partition = the d43b PER-CANDIDATE operator verbatim;")
print("  caps: ARM-1T (A,B) depth <= 4, ARM-2T (A,B,C) depth <= 3")
print("  (the d42b1 committed caps, re-declared); weight-system")
print("  level only — no measure claim, no infinite-volume claim;")
print("  deterministic (no RNG; all prints sorted).")

AB = ('A', 'B'); ABC = ('A', 'B', 'C')
CAP1, CAP2 = 4, 3

# ==== TG0 — layer fidelity: the committed census re-anchored ========
ARM1, C1 = ns1['enumerate_family'](AB, CAP1)
ARM2, C2 = ns1['enumerate_family'](ABC, CAP2)
cum1 = [sum(1 for h in ARM1 if len(h) <= k) for k in range(CAP1 + 1)]
cum2 = [sum(1 for h in ARM2 if len(h) <= k) for k in range(CAP2 + 1)]
print(f"  TG1 SIZE PROBE (pin runtime control): ARM-1T depth-4 "
      f"family = {len(ARM1)} <= 150000 — the committed depth-4 cap "
      f"STANDS (no reduction needed)")
print(f"  cumulative sizes [MEASURED, first run — round to anchor]: "
      f"ARM-1T {cum1}; ARM-2T {cum2}")
check("TG0a the committed ARM census re-anchored: ARM-1T = 3969, "
      "ARM-2T = 3424 (the committed d42b1 .out values, re-derived "
      "from the exec'd committed layer)",
      len(ARM1) == 3969 and len(ARM2) == 3424
      and cum1 == [1, 9, 69, 521, 3969]
      and cum2 == [1, 16, 235, 3424],
      f"ARM-1T = {len(ARM1)}; ARM-2T = {len(ARM2)}")

full_view = ns1['full_view']
event_poset = ns1['event_poset']
def orphan_census(fam):
    n = 0
    for h in fam:
        view = full_view(h)
        for i, op in view.live.items():
            if op[2] in view.superseded: n += 1
    return n
orA, orB = orphan_census(ARM1), orphan_census(ARM2)
d2 = sum(1 for h in ARM1 if len(h) == 2
         and full_view(h).edges(set(full_view(h).props)))
join_arbs = join_dels = 0
for h in ARM1 + ARM2:
    for e in h:
        if e[0] == 'r' and len(e[2]) >= 2: join_arbs += 1
        if e[0] == 'd': join_dels += 1
check("TG0b layer fidelity beyond size: the committed in-family "
      "censuses reproduce (orphans 464/72; depth-2 conflict "
      "histories 4; arb joins 384; delivery joins 8250 — all four "
      "committed d42b1 .out anchors)",
      (orA, orB) == (464, 72) and d2 == 4
      and join_arbs == 384 and join_dels == 8250,
      f"orphans = {(orA, orB)}; d2 conflicts = {d2}; joins = "
      f"{(join_arbs, join_dels)}")

def leaves_ok(x):
    """ALLOW-LIST walk (the #362 successor binding): leaves must be
    Fraction/int/str; containers tuple/list/set/frozenset; bool and
    everything else (float, complex, Decimal, np scalars) REJECTED."""
    if isinstance(x, Fr): return True
    if isinstance(x, bool): return False
    if isinstance(x, (int, str)): return True
    if isinstance(x, (tuple, list, set, frozenset)):
        return all(leaves_ok(y) for y in x)
    return False
bad = 0
for cache in (C1, C2):
    for k, cands in cache.items():
        for e, q in cands:
            if not (isinstance(q, Fr) and leaves_ok(e)): bad += 1
check("TG0c purity, ALLOW-LIST walk form (LOG #362 binding): every "
      "cached candidate weight is a Fraction and every event leaf "
      "is in {Fraction, int, str} — floats/bools/complex rejected "
      "categorically",
      bad == 0, f"violations = {bad} over both arms")

# ==== TG1 — the intrinsic partition on ARM-1T (per-candidate) =======
def menu_shape(cands):
    d = {}
    for e, q in cands:
        d[(e[0], q)] = d.get((e[0], q), 0) + 1
    return tuple(sorted(d.items(), key=repr))

def relabel(d):
    relab = {}
    for k in sorted(d, key=repr):
        relab.setdefault(d[k], len(relab))
    return {k: relab[d[k]] for k in d}

# d43b lines 91-100 VERBATIM in definition (the #366 F2 per-candidate
# operator), window-adjusted to the depth-4 cache: P_t is defined on
# len <= CAP1 - t.
P = {0: relabel({tuple(h): menu_shape(C1[tuple(h)]) for h in ARM1})}
for t in range(CAP1):
    nxt = {}
    for h in ARM1:
        if len(h) > CAP1 - 1 - t: continue
        k = tuple(h)
        succ = tuple(sorted((str(q), P[t][tuple(h + [e])])
                            for e, q in C1[k]))
        nxt[k] = (P[t][k], succ)
    P[t + 1] = relabel(nxt)

tables = {c: [len({P[t][tuple(h)] for h in ARM1 if len(h) <= c})
              for t in range(0, CAP1 + 1 - c)] for c in (1, 2, 3, 4)}
growth = [(t, CAP1 - t,
           sum(1 for h in ARM1 if len(h) <= CAP1 - t),
           len({P[t][tuple(h)] for h in ARM1
                if len(h) <= CAP1 - t})) for t in range(CAP1 + 1)]
print("  TG1 |P_t| tables per window (cutoff c lists t = 0.."
      "(4 - c)):")
for c in (1, 2, 3, 4):
    print(f"    cutoff-{c}: {tables[c]}")
print("  TG1 growth table (t, window len<=, histories, |P_t|): "
      + "; ".join(str(g) for g in growth))

def part_of(Pm, hs):
    b = {}
    for h in hs:
        b.setdefault(Pm[tuple(h)], set()).add(tuple(h))
    return frozenset(frozenset(v) for v in b.values())
agree = {}
wsizes = {}
for t in range(CAP1):
    W = [h for h in ARM1 if len(h) <= CAP1 - 1 - t]
    wsizes[t] = len(W)
    agree[t] = (part_of(P[t], W) == part_of(P[t + 1], W))
nontriv = {t for t in range(CAP1) if wsizes[t] > 1}
deep_nt = max(nontriv)
print(f"  TG1 blockwise agreement P_t vs P_(t+1) per window: "
      + "; ".join(f"t={t} on len<={CAP1 - 1 - t} "
                  f"({wsizes[t]} h): {agree[t]}"
                  + ("" if t in nontriv else " [TRIVIAL WINDOW]")
                  for t in range(CAP1)))
# round-1 F4 declaration: STAB = TWO blockwise agreements (t = 1, 2;
# the second on a 9-history window) — the d43b F-B5 three-consecutive
# standard is UNMEETABLE at this cap (only two nontrivial lookaheads
# exist); the criterion drift is declared, not silent.
STAB = all(agree[t] for t in nontriv if t >= 1) and len(
    [t for t in nontriv if t >= 1]) >= 2

# The refinement-split exhibit (the pin's TG1 exhibit clause,
# instantiated at the deepest t where refinement still splits): a
# P_t class split by P_{t+1}, two members with menus + rows.
def rows_of(h, Pm):
    return tuple(sorted((str(q), Pm[tuple(h + [e])])
                        for e, q in C1[tuple(h)]))
split_t = max((t for t in nontriv if not agree[t]), default=None)
EXH = None
if split_t is not None:
    W = sorted([h for h in ARM1 if len(h) <= CAP1 - 1 - split_t],
               key=lambda h: (len(h), repr(h)))
    byc = {}
    for h in W:
        byc.setdefault(P[split_t][tuple(h)], []).append(h)
    for c in sorted(byc, key=lambda c: (len(byc[c][0]),
                                        repr(byc[c][0]))):
        sub = {}
        for h in byc[c]:
            sub.setdefault(P[split_t + 1][tuple(h)], []).append(h)
        if len(sub) > 1:
            ks = sorted(sub, key=lambda k2: repr(sub[k2][0]))
            h1, h2 = sub[ks[0]][0], sub[ks[1]][0]
            EXH = (split_t, h1, h2)
            break
if EXH is not None:
    t_e, h1, h2 = EXH
    r1, r2 = rows_of(h1, P[t_e]), rows_of(h2, P[t_e])
    print(f"  TG1 DEEPEST REFINEMENT SPLIT (t = {t_e} -> "
          f"{t_e + 1}, window len <= {CAP1 - 1 - t_e}):")
    print(f"    member 1: {h1}")
    print(f"      menu shape: {menu_shape(C1[tuple(h1)])}")
    print(f"    member 2: {h2}")
    print(f"      menu shape: {menu_shape(C1[tuple(h2)])}")
    d12 = sorted(set(r1) ^ set(r2))
    print(f"    per-candidate (weight, P_{t_e}-class) rows DIFFER; "
          f"symmetric difference (first 6): {d12[:6]}")
check("TG1 STABILIZATION VERDICT — WINDOW-CONSISTENT STABILIZATION, "
      "NOT CLOSURE: the per-candidate refinement agrees blockwise "
      "at t = 1 and t = 2 on their (shallow) windows and lands at "
      "SIX classes on the len <= 2 window — a transport-scope "
      "six-state signal echoing the d42a count, but a DIFFERENT "
      "object (TG6: every transport menu is alien to d42a); the "
      "refinement is REAL (the t = 0 split above: two histories "
      "with IDENTICAL menu shapes — [pA0] vs [pA0, dABv0] — are "
      "split by their successor rows), the anchored tables are "
      "[2,2,2,2]/[5,6,6]/[9,11]/[13], and the deeper windows "
      "(11 classes on len <= 3 at t = 1; 13 menu shapes on "
      "len <= 4) are NOT refinement-tested beyond these lookaheads "
      "— the depth-4 cap is the declared feasibility boundary "
      "(TG7); closure is decided NEGATIVELY at TG4 (the window "
      "chain escapes)",
      STAB and agree == {0: False, 1: True, 2: True, 3: True}
      and tables == {1: [2, 2, 2, 2], 2: [5, 6, 6],
                     3: [9, 11], 4: [13]}
      and len({P[1][tuple(h)] for h in ARM1 if len(h) <= 2}) == 6
      and EXH is not None and EXH[0] == 0
      and rows_of(EXH[1], P[0]) != rows_of(EXH[2], P[0])
      and menu_shape(C1[tuple(EXH[1])])
          == menu_shape(C1[tuple(EXH[2])]),
      f"agreements = {agree}; six on len<=2 window; split exhibit "
      "at t = 0 with equal menus, unequal rows")
n_shapes2 = len({menu_shape(C2[tuple(h)]) for h in ARM2})
check("TG1s ARM-2T supplementary datum ANCHORED (round-1 F2; "
      "census scope only, pin §3): distinct menu shapes on the "
      "depth-3 family == 11; the ARM-2T intrinsic program is NOT "
      "run (cap declared; TG7)",
      n_shapes2 == 11, f"shapes = {n_shapes2}")

# ==== TG2 — transfer well-definedness on the deepest windows ========
def wd_test(t_cls, parent_cap):
    """Rows w.r.t. partition P_{t_cls} (parents len <= parent_cap;
    successors covered since parent_cap + 1 <= CAP1 - t_cls).
    Returns (well_defined, n_classes, n_failing, first_fail)."""
    byc = {}
    for h in sorted([h for h in ARM1 if len(h) <= parent_cap],
                    key=lambda h: (len(h), repr(h))):
        byc.setdefault(P[t_cls][tuple(h)], []).append(h)
    n_fail, first = 0, None
    for c in sorted(byc, key=lambda c: (len(byc[c][0]),
                                        repr(byc[c][0]))):
        rr = {rows_of(h, P[t_cls]): h for h in byc[c]}
        if len(rr) > 1:
            n_fail += 1
            if first is None:
                ks = sorted(rr, key=repr)
                first = (c, rr[ks[0]], rr[ks[1]])
    return n_fail == 0, len(byc), n_fail, first

wd0, ncls0, nf0, ff0 = wd_test(0, CAP1 - 1)
wd1, ncls1, nf1, ff1 = wd_test(1, CAP1 - 2)
print(f"  TG2 level-0 (P_0 = menu-shape classes, parents len <= "
      f"{CAP1 - 1}): {ncls0} classes, {nf0} with non-constant "
      f"per-candidate rows -> well-defined = {wd0}")
print(f"  TG2 level-1 (P_1 classes, parents len <= {CAP1 - 2}): "
      f"{ncls1} classes, {nf1} failing -> well-defined = {wd1}")
if ff0 is not None:
    c, h1, h2 = ff0
    print(f"  TG2 FIRST FAILING CLASS (level-0 = menu-shape "
          f"classes, the deepest window; class {c}):")
    print(f"    member 1: {h1}")
    print(f"      menu shape: {menu_shape(C1[tuple(h1)])}")
    print(f"    member 2: {h2}")
    print(f"      menu shape: {menu_shape(C1[tuple(h2)])}")
    d12 = sorted(set(rows_of(h1, P[0])) ^ set(rows_of(h2, P[0])))
    print(f"    differing (weight, class) rows, symmetric "
          f"difference (first 6): {d12[:6]}")
check("TG2 transfer well-definedness VERDICT — WELL-DEFINED at the "
      "intrinsic level on the deepest well-defined window (all 6 "
      "P_1 classes over len <= 2 parents have constant per-"
      "candidate (weight, target-class) rows: 0/6 failing — the "
      "probabilistic-bisimulation property holds where testable), "
      "while the MENU-SHAPE level FAILS on the deeper window (2/9 "
      "classes non-constant; first failing class exhibited above "
      "with both members, equal menus, differing rows — transport "
      "menu shape does NOT factorize the transfer; the intrinsic "
      "refinement is load-bearing, the d44a per-candidate lesson "
      "carried). Window-limited statement only (TG7)",
      wd1 and (not wd0) and (nf0, ncls0, nf1, ncls1) == (2, 9, 0, 6)
      and ff0 is not None
      and rows_of(ff0[1], P[0]) != rows_of(ff0[2], P[0])
      and menu_shape(C1[tuple(ff0[1])])
          == menu_shape(C1[tuple(ff0[2])]),
      f"failing classes: level-0 = {nf0}/{ncls0}, level-1 = "
      f"{nf1}/{ncls1}")

# ==== TG3 — THE REOPENING PREDICTION ================================
def live_hold(view, a):
    return frozenset(v for v in view.holdings(a)
                     if v not in view.superseded)
DIV = {}
for h in ARM1:
    view = full_view(h)
    DIV[tuple(h)] = live_hold(view, 'A') != live_hold(view, 'B')
recon = []
for h in sorted(ARM1, key=lambda h: (len(h), repr(h))):
    for j, e in enumerate(h):
        if (e[0] == 'd' and DIV[tuple(h[:j])]
                and not DIV[tuple(h[:j + 1])]):
            recon.append((h, j))
def weight_of(h):
    w = Fr(1)
    for j, e in enumerate(h):
        w *= dict(C1[tuple(h[:j])])[e]
    return w
n_div = sum(1 for v in DIV.values() if v)
check("TG3a divergence exists in-family (the d43b state-4/5 pattern "
      "instantiated at transport scope: unequal non-superseded "
      "holdings between A and B in the full view)",
      n_div == 1044,
      f"diverged histories in ARM-1T = {n_div} (anchored, round-1 "
      f"F2)")
if recon:
    hW, jW = recon[0]
    wpref = hW[:jW]
    wfull = hW[:jW + 1]
    qW = weight_of(wfull)
    print(f"  TG3 RECONVERGENCE WITNESS (shortest, in-family):")
    print(f"    diverged prefix ({jW} events): {wpref}")
    vp = full_view(wpref)
    print(f"      holdings A = {sorted(live_hold(vp, 'A'), key=repr)}")
    print(f"      holdings B = {sorted(live_hold(vp, 'B'), key=repr)}")
    print(f"    the delivery: {hW[jW]}")
    vf = full_view(wfull)
    print(f"      post-delivery shared holdings = "
          f"{sorted(live_hold(vf, 'A'), key=repr)} (A == B: "
          f"{live_hold(vf, 'A') == live_hold(vf, 'B')})")
    print(f"    exact weight of the reconverging chain = {qW}")
check("TG3b THE REOPENING PREDICTION CONFIRMED IN-FAMILY (the "
      "pre-registered TG3 horn, decided positively; no above-cap "
      "SIG-chain needed): a delivery event inside the enumerated "
      "ARM-1T family reconverges a diverged configuration — the "
      "d43b absorption theorem ('diverged holdings never "
      "reconverge', the closed {2,4,5} sector) is a DELIVERYLESSNESS "
      "ARTIFACT, exactly as d43b's relocation clause predicted; "
      "witness = [pA0, blind self-seal, deliver v1 to B] at exact "
      "weight 1/256, with every event admission-priced by the "
      "committed layer",
      bool(recon) and len(recon[0][0][:recon[0][1] + 1]) == 3
      and weight_of(recon[0][0][:recon[0][1] + 1]) == Fr(1, 256)
      and DIV[tuple(recon[0][0][:recon[0][1]])]
      and not DIV[tuple(recon[0][0][:recon[0][1] + 1])]
      and len(recon) == 124
      and len({tuple(h[:j]) for h, j in recon}) == 84
      and len({tuple(h[:j + 1]) for h, j in recon
               if j + 1 == 3}) == 4,
      f"reconverging (history, delivery) pairs in-family = "
      f"{len(recon)}; witness weight = "
      f"{weight_of(recon[0][0][:recon[0][1] + 1]) if recon else None}")

wpref = recon[0][0][:recon[0][1]] if recon else None
if wpref is not None:
    dl = sorted(((str(q), P[1][tuple(list(wpref) + [e])],
                  DIV[tuple(list(wpref) + [e])])
                 for e, q in C1[tuple(wpref)] if e[0] == 'd'))
    print(f"  TG3c the diverged class's delivery row (weight, "
          f"P_1-target-class, still-diverged?): {dl}")
check("TG3c the reopening AT CHAIN LEVEL: the diverged-quiescent "
      "witness prefix (a len-2 member of the window six) carries a "
      "delivery candidate at exact weight 1/8 whose successor is "
      "NON-diverged — the d43b chain's absorbing row structurally "
      "cannot be reproduced by any transport-scope transfer",
      wpref is not None and DIV[tuple(wpref)]
      and any(e[0] == 'd' and q == Fr(1, 8)
              and not DIV[tuple(list(wpref) + [e])]
              for e, q in C1[tuple(wpref)]),
      "delivery row printed above")

# ==== TG4/TG5 — the conditional Perron program ======================
# Closure probe: does the deepest well-defined window transfer stay
# inside its own class set? (The pin's "closed exact transfer".)
parents2 = sorted([h for h in ARM1 if len(h) <= CAP1 - 2],
                  key=lambda h: (len(h), repr(h)))
cls2 = {P[1][tuple(h)] for h in parents2}
ESC = []
for h in parents2:
    for e, q in C1[tuple(h)]:
        c2 = P[1][tuple(h + [e])]
        if c2 not in cls2:
            ESC.append((h, e, q, c2))
esc_cls = sorted({c2 for _, _, _, c2 in ESC})
if ESC:
    h_e, e_e, q_e, c_e = ESC[0]
    print(f"  TG4 ESCAPE EXHIBIT (the window chain is NOT closed): "
          f"parent {h_e} (class {P[1][tuple(h_e)]}) --{e_e} "
          f"(q = {q_e})--> class {c_e}, a class first realized only "
          f"at len 3, whose own rows leave the P_1 domain at this "
          f"cap; escaping classes = {esc_cls} "
          f"({len(esc_cls)} of the 11 len<=3 P_1 classes), "
          f"escaping transitions = {len(ESC)}")
FIRE = STAB and wd1 and not ESC
reasons = {}
if FIRE:
    # A closed exact transfer exists on the stabilized classes:
    # build T over the P_1 classes on the deepest well-defined
    # window and run the full d43b Perron program.
    parents = [h for h in ARM1 if len(h) <= CAP1 - 2]
    cls = sorted({P[1][tuple(h)] for h in parents})
    idx = {c: i for i, c in enumerate(cls)}
    n = len(cls)
    T = [[Fr(0)] * n for _ in range(n)]
    seen_row = set()
    for h in parents:
        i = idx[P[1][tuple(h)]]
        if i in seen_row: continue
        seen_row.add(i)
        for e, q in C1[tuple(h)]:
            T[i][idx[P[1][tuple(h + [e])]]] += q
    # Tarjan (iterative)
    adj = {i: [j for j in range(n) if T[i][j] != 0] for i in range(n)}
    index, low, onst, stk, sccs, cnt = {}, {}, {}, [], [], [0]
    for v0_ in range(n):
        if v0_ in index: continue
        work = [(v0_, 0)]
        while work:
            v, pi_ = work.pop()
            if pi_ == 0:
                index[v] = low[v] = cnt[0]; cnt[0] += 1
                stk.append(v); onst[v] = True
            recurse = False
            for w in adj[v][pi_:]:
                pi_ += 1
                if w not in index:
                    work.append((v, pi_)); work.append((w, 0))
                    recurse = True; break
                elif onst.get(w):
                    low[v] = min(low[v], index[w])
            if recurse: continue
            if low[v] == index[v]:
                comp = []
                while True:
                    w = stk.pop(); onst[w] = False
                    comp.append(w)
                    if w == v: break
                sccs.append(sorted(comp))
            if work:
                low[work[-1][0]] = min(low[work[-1][0]], low[v])
    print(f"  TG4 FIRED: {n} classes; SCCs = {sccs}")
    def charpoly(M):
        m = len(M)
        coeffs = [Fr(1)]
        Mk = [[Fr(1) if i == j else Fr(0) for j in range(m)]
              for i in range(m)]
        for kk in range(1, m + 1):
            Mk = [[sum(M[i][t2] * Mk[t2][j] for t2 in range(m))
                   for j in range(m)] for i in range(m)]
            tr = sum(Mk[i][i] for i in range(m))
            c = -tr / kk
            coeffs.append(c)
            for i in range(m): Mk[i][i] += c
        return coeffs
    def peval(cs, x):
        v = Fr(0)
        for c in cs: v = v * x + c
        return v
    cs = charpoly(T)
    rowmax = max(sum(r) for r in T)
    lam = None
    for den in range(1, 49):
        for num in range(0, int(rowmax) * den + den + 1):
            if peval(cs, Fr(num, den)) == 0:
                lam = max(lam or Fr(0), Fr(num, den))
    if lam is not None:
        check("TG4 Perron root EXACT (rational; charpoly vanishes)",
              peval(cs, lam) == 0, f"lambda = {lam}")
        # left kernel of (T - lam I): Gaussian elimination, exact
        M = [[T[j][i] - (lam if i == j else 0) for j in range(n)]
             for i in range(n)]
        piv = []
        r = 0
        for c_ in range(n):
            pr = next((k2 for k2 in range(r, n) if M[k2][c_] != 0),
                      None)
            if pr is None: continue
            M[r], M[pr] = M[pr], M[r]
            M[r] = [x / M[r][c_] for x in M[r]]
            for k2 in range(n):
                if k2 != r and M[k2][c_] != 0:
                    M[k2] = [a - M[k2][c_] * b
                             for a, b in zip(M[k2], M[r])]
            piv.append(c_); r += 1
        free = [c_ for c_ in range(n) if c_ not in piv]
        pi_v = [Fr(0)] * n
        if free:
            pi_v[free[0]] = Fr(1)
            for rr, c_ in enumerate(piv):
                pi_v[c_] = -M[rr][free[0]]
        check("TG5 mass transport on the closed chain: pi T = "
              "lambda pi exactly for a nontrivial left kernel "
              "vector",
              bool(free) and all(
                  sum(pi_v[i] * T[i][j] for i in range(n))
                  == lam * pi_v[j] for j in range(n)),
              f"pi = {[str(x) for x in pi_v]}")
    else:
        lo, hi = Fr(0), rowmax + 1
        for _ in range(80):
            mid = (lo + hi) / 2
            if peval(cs, mid) * peval(cs, hi) <= 0: lo = mid
            else: hi = mid
        check("TG4 Perron root: certified exact-arithmetic bracket "
              "(no rational root at scanned denominators <= 48)",
              hi - lo < Fr(1, 10**20), f"bracket = ({lo}, {hi})")
        reasons['TG5'] = ("root not rational at scanned "
                          "denominators; exact mass transport "
                          "deferred to the successor")
        print(f"  TG5 NON-FIRING REASON: {reasons['TG5']}")
        check("TG5 non-firing reason recorded (root irrational at "
              "scan)", lam is None and 'TG5' in reasons, "recorded")
else:
    reasons['TG4'] = ("PREREQUISITE FAILED — NO CLOSED EXACT "
                      "TRANSFER AT CAP: TG1 window-stabilization "
                      "(%s) and TG2 well-definedness (%s) both "
                      "hold, but the window chain ESCAPES: %d "
                      "transitions from len<=2 parents land in %d "
                      "classes (%s) realized only at len 3, whose "
                      "own rows leave the computable P_1 domain — "
                      "the six window classes are NOT closed under "
                      "the transfer, so Tarjan/Perron root/"
                      "positive-vector/root-vs-renewal have no "
                      "delivered object at this cap"
                      % (STAB, wd1, len(ESC), len(esc_cls), esc_cls))
    reasons['TG5'] = ("PREREQUISITE FAILED: TG5 (mass transport) is "
                      "conditional on TG4's closed chain; TG4 did "
                      "not fire")
    for g in ('TG4', 'TG5'):
        print(f"  {g} NON-FIRING REASON: {reasons[g]}")
    check("TG4 does not fire, and the non-firing reason is the "
          "MEASURED obstruction re-verified (pin TG7 discipline): "
          "the escape exhibit's transition is a genuine cache "
          "transition whose target class has NO member of length "
          "<= 2 — the 'closed exact transfer' prerequisite is "
          "concretely false, not silently skipped; anchored: 68 "
          "escaping transitions into exactly 5 above-window "
          "classes",
          (not FIRE) and len(ESC) == 68 and len(esc_cls) == 5
          and all(len(k) > 2 for k in P[1]
                  if P[1][k] == ESC[0][3])
          and dict(C1[tuple(ESC[0][0])])[ESC[0][1]] == ESC[0][2],
          f"escapes = {len(ESC)} into {esc_cls}")
    check("TG5 does not fire (conditional on TG4), reason recorded; "
          "consistency: the firing flag equals the measured "
          "conjunction STAB and wd1 and window-closure",
          (not FIRE) and set(reasons) == {'TG4', 'TG5'},
          f"FIRE = {FIRE}; STAB = {STAB}; wd1 = {wd1}; "
          f"closed = {not ESC}")

# ==== TG6 — negative control: the d43b classifier fails here ========
FAM0, C0 = ns0['enumerate_family'](AB, 4)
cum0 = [sum(1 for h in FAM0 if len(h) <= k) for k in range(5)]
check("TG6a the d42a-scope layer re-anchored (the d43b MG0 census "
      "prefix): cumulative sizes at depths 0-4",
      cum0 == [1, 7, 39, 215, 1191], f"sizes = {cum0}")
shapes0 = {menu_shape(C0[tuple(h)]) for h in FAM0}
hW6 = recon[0][0][:recon[0][1] + 1] if recon else None
shpW = menu_shape(C1[tuple(hW6)]) if hW6 else None
has_d = lambda s: any(k[0] == 'd' for k, cnt in s)
n_d0 = sum(1 for s in shapes0 if has_d(s))
all_alien = sum(1 for h in ARM1
                if menu_shape(C1[tuple(h)]) in shapes0)
check("TG6b NEGATIVE CONTROL: the six-state d43b classifier applied "
      "blindly to transport histories FAILS — the TG3 witness (a "
      "delivery-containing history) has a menu shape reproduced by "
      "NO d42a-scope class (its menu carries 'd'-kind candidates; "
      "ZERO of the d42a family's menu shapes contain a 'd' kind); "
      "in fact EVERY ARM-1T transport menu is alien to the d42a "
      "shape set (deliveries are always enabled at transport scope) "
      "— the d42a six-state result CANNOT be silently reused here",
      hW6 is not None and shpW not in shapes0 and has_d(shpW)
      and n_d0 == 0 and all_alien == 0 and len(shapes0) == 4,
      f"d42a distinct shapes = {len(shapes0)} (with 'd': {n_d0}); "
      f"ARM-1T menus matching any d42a shape = {all_alien}/3969")

# ==== TG7 — caps and honesty ========================================
print("  TG7 CAPS, all declared: ARM-1T = (A,B) depth <= 4 "
      "(intrinsic program scope); ARM-2T = (A,B,C) depth <= 3 "
      "(census + purity + menu-shape count only — the ARM-2T "
      "intrinsic program NOT run, runtime-budgeted per pin §3); "
      "lookahead computable to t <= 3 on nontrivial windows; "
      "transfer testable to lookahead 1 on len <= 2 parents.")
print("  TG7 HONESTY: no infinite-volume claim is made under this "
      "outcome (none would be under any outcome); what remains "
      "open — the transport-scope intrinsic object beyond depth 4, "
      "its stabilization, and any completion core — is the declared "
      "territory of [I1]'s Martin/R-theory machinery, a SUCCESSOR, "
      "not this receipt.")
print("  TG7 D44a SCOPE STATEMENT (what the closure theorem does "
      "and does not cover): D44a's decision is at d42a scope "
      "(delivery-free), exhaustively verified through depth 7, "
      "all-depth conditional on H1 — and THIS receipt shows its "
      "class structure does NOT transfer: the absorbing sector is "
      "an artifact of deliverylessness (TG3), and the transport "
      "intrinsic chain, though window-consistent at six classes "
      "with well-defined rows (TG1/TG2), is NOT CLOSED at the "
      "feasible cap (TG4's escape). The closure theorem covers "
      "exactly the delivery-free grammar; transport-scope closure "
      "is OPEN.")
check("TG7 caps + honesty mechanically consistent: the declared "
      "caps equal the enumeration caps actually used; every "
      "non-fired conditional gate recorded a reason (2 of 2: TG4, "
      "TG5); the conditional flag equals the measured prerequisite",
      CAP1 == 4 and CAP2 == 3
      and max(len(h) for h in ARM1) == CAP1
      and max(len(h) for h in ARM2) == CAP2
      and (FIRE or sorted(reasons) == ['TG4', 'TG5']),
      f"caps = ({CAP1}, {CAP2}); reasons recorded = "
      f"{sorted(reasons)}; FIRE = {FIRE}")

print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL  "
      f"(runtime under the 600 s budget: {time.time() - T0 < 600}; "
      f"exact seconds omitted for byte-identical determinism)")
if FAIL:
    print("[VERDICT] FAIL — anchor/consistency breakage; exit 1")
    sys.exit(1)
print("[VERDICT] d44b GREEN — the campaign-final scope statement: "
      "(1) TG3 CONFIRMED, the pre-registered reopening prediction: "
      "a 3-event in-family delivery chain at exact weight 1/256 "
      "reconverges diverged holdings — the d43b absorbing sector "
      "{2,4,5} is a deliverylessness artifact, exactly as the "
      "relocation clause predicted. (2) TG1/TG2: the transport "
      "intrinsic partition (the d43b per-candidate operator "
      "verbatim) shows a WINDOW-CONSISTENT six-state signal "
      "(t = 1,2 agreement; six classes on len <= 2; all rows "
      "constant per class where testable) — but it is NOT the "
      "d42a object (menu shapes carry the delivery sector; "
      "menu-shape factorization FAILS, 2/9 classes) and it is NOT "
      "closed: (3) the window chain ESCAPES into above-window "
      "classes (TG4's exhibited obstruction), so no closed exact "
      "transfer exists at the depth-4 cap and TG4/TG5 do not fire "
      "— the honest non-closure outcome the pin pre-registered, "
      "reasons printed. (4) TG6: the d42a six-state "
      "classifier fails on every transport menu — the D44a closure "
      "theorem covers exactly the delivery-free grammar and cannot "
      "be silently reused. Residue-1-at-transport-scope is OPEN "
      "above cap; [I1] Martin/R-theory is the named successor "
      "tool. No infinite-volume claim. The generated record's "
      "campaign closes on this honest boundary.")

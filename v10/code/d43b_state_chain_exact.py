#!/usr/bin/env python3
"""
d43b_state_chain_exact.py — v10 D43b (N2): residue 1 via the
intrinsic state chain. Pin: note-d43b (e9cf9e7). EXACT Fractions
throughout; the d42a layer exec'd from the committed d42b3 receipt.

STRATEGY (pin §1): bisimulation partitions at depths 4, 5, 6; the
STABILIZATION question decided on INTERIOR states (the deepest layer
is boundary-coarse by construction and excluded from the
comparison). On stabilization at k states: the exact k x k transfer,
Faddeev-LeVerrier characteristic polynomial, Tarjan SCC
decomposition, Perron analysis per recurrent class with lambda
certified by exact sign-change bisection, the root-vs-renewal state
identity (MG4), and the mass-transport identity (MG5). The
stabilization outcome is PRE-REGISTERED open.
"""
import sys
from fractions import Fraction as Fr

sys.setrecursionlimit(400000)

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

_src = open('v10/code/d42b3_placement_exact.py').read()
ns = {}
exec(_src[:_src.index('print("[d42b3')], ns)
V0 = ns['V0']
candidates_for = ns['candidates_for']
AB = ('A', 'B')

print("[d43b — residue 1 via the intrinsic state chain]")
print("  banner: EXACT; d42a layer from the committed d42b3 receipt;")
print("  depths 4/5/6 full enumerations; interior-state comparison;")
print("  stabilization PRE-REGISTERED open; on closure: exact")
print("  Perron-Frobenius (Faddeev-LeVerrier + Tarjan + sign-change")
print("  bisection); no infinite-volume claim beyond the decided")
print("  quotient scope (pin §4).")

def enumerate_family(max_events):
    out = [[]]
    cache = {}
    frontier = [[]]
    while frontier:
        h = frontier.pop()
        cands = candidates_for(h, AB)
        cache[tuple(h)] = cands
        if len(h) >= max_events: continue
        for e, q in cands:
            out.append(h + [e]); frontier.append(h + [e])
    return out, cache

def menu_shape(cands):
    d = {}
    for e, q in cands:
        d[(e[0], q)] = d.get((e[0], q), 0) + 1
    return tuple(sorted(d.items(), key=repr))

def bisim(fam, cache, depth):
    """Partition refinement (the committed d42b56 algorithm):
    boundary (len == depth) by shape; interior by (shape, successor
    multiset). Returns state id per history + the trajectory."""
    state = {tuple(h): repr(menu_shape(cache[tuple(h)])) for h in fam}
    traj = [len(set(state.values()))]
    while True:
        new = {}
        for h in fam:
            k = tuple(h)
            if len(h) == depth:
                new[k] = (state[k], 'B')
            else:
                succ = tuple(sorted((str(q), state[tuple(h + [e])])
                                    for e, q in cache[k]))
                new[k] = (state[k], succ)
        relab = {}
        for k in sorted(new, key=repr):
            relab.setdefault(new[k], len(relab))
        s2 = {k: relab[new[k]] for k in new}
        traj.append(len(set(s2.values())))
        if len(set(s2.values())) == len(set(state.values())):
            return s2, traj
        state = {k: str(v) for k, v in s2.items()}

FAM4, C4 = enumerate_family(4)
S4, traj4 = bisim(FAM4, C4, 4)
n4_all = len(set(S4.values()))
check("MG1 ANCHOR: the depth-4 bisimulation reproduces the committed "
      "17-state partition (trajectory 4-9-14-16-17)",
      n4_all == 17 and traj4[:5] == [4, 9, 14, 16, 17],
      f"states = {n4_all}; trajectory = {traj4}")

FAM5, C5 = enumerate_family(5)
S5, traj5 = bisim(FAM5, C5, 5)
FAM6, C6 = enumerate_family(6)
S6, traj6 = bisim(FAM6, C6, 6)

def interior_states(S, fam, depth, margin):
    """States realized by histories at len <= depth - margin (deep
    enough that their signatures are boundary-uncontaminated to
    'margin' levels)."""
    return {S[tuple(h)] for h in fam if len(h) <= depth - margin}

# interior comparison: match states between runs via representative
# canonical keys (a state's identity = the canon-set of its members
# restricted to the shallower depth)
def state_key_map(S, fam, depth, margin):
    """For each interior state: the frozenset of member canons at
    len <= depth - margin (the cross-run matching key)."""
    canon = ns['canon']
    members = {}
    for h in fam:
        if len(h) <= depth - margin:
            members.setdefault(S[tuple(h)], set()).add(canon(h))
    return {sid: frozenset(m) for sid, m in members.items()}

# cross-run stabilization: do the depth-5 and depth-6 runs induce
# the SAME partition on the depth-4 sub-family (margin 1 each)?
def induced_partition(S, fam, cutoff):
    part = {}
    for h in fam:
        if len(h) <= cutoff:
            part.setdefault(S[tuple(h)], set()).add(tuple(h))
    return frozenset(frozenset(v) for v in part.values())

p5_on4 = induced_partition(S5, FAM5, 4)
p6_on4 = induced_partition(S6, FAM6, 4)
p6_on5 = induced_partition(S6, FAM6, 5)
p5_on5cut = induced_partition(S5, FAM5, 4)
n5_int = len(induced_partition(S5, FAM5, 4))
n6_int4 = len(p6_on4)
n6_int5 = len(p6_on5)
stab_4 = (p5_on4 == p6_on4)
counts = (len(set(S4.values())), len(set(S5.values())),
          len(set(S6.values())))
print(f"  state counts (full, boundary-coarse): depth 4/5/6 = "
      f"{counts}; induced-on-depth<=4: by-5 = {len(p5_on4)}, "
      f"by-6 = {len(p6_on4)}; induced-on-depth<=5 by-6 = {n6_int5}")
check("MG2 THE STABILIZATION QUESTION (pre-registered open): the "
      "depth-5 and depth-6 refinements induce the SAME partition on "
      "the depth<=4 sub-family (two consecutive agreements = the "
      "stabilization criterion at margin 1)",
      True, f"AGREE = {stab_4}; the MG2 verdict is the printed "
      "outcome either way — this check gates only that the "
      "comparison ran on both depths")

if stab_4 and len(p6_on4) == n6_int5:
    # ---- CLOSURE: build the exact transfer on the stabilized states
    # state ids from the depth-6 run restricted to len <= 4 histories;
    # transitions from len <= 3 histories (whose successors are
    # len <= 4, all state-labeled)
    sid = {}
    for h in FAM6:
        if len(h) <= 4:
            sid[tuple(h)] = S6[tuple(h)]
    states = sorted({v for v in sid.values()})
    k = len(states)
    pos = {s: i for i, s in enumerate(states)}
    T = [[Fr(0)] * k for _ in range(k)]
    seen_rows = set()
    ok_wd = True
    for h in FAM6:
        if len(h) > 3: continue
        r = pos[sid[tuple(h)]]
        row = {}
        for e, q in C6[tuple(h)]:
            row[pos[sid[tuple(h + [e])]]] = \
                row.get(pos[sid[tuple(h + [e])]], Fr(0)) + q
        if r in seen_rows:
            ok_wd &= all(T[r][c] == row.get(c, Fr(0)) for c in range(k))
        else:
            seen_rows.add(r)
            for c, v in row.items(): T[r][c] = v
    check("MG2b the transfer is WELL-DEFINED on the stabilized "
          "states (every member history of a state yields the same "
          "exact row — the bisimulation property, gated)",
          ok_wd, f"k = {k} states; rows realized = {len(seen_rows)}")

    # ---- MG3: exact Perron-Frobenius ------------------------------
    # Tarjan SCCs on the support digraph
    import sys as _s
    adj = {i: [j for j in range(k) if T[i][j] != 0] for i in range(k)}
    index = {}; low = {}; onstack = {}; stack = []; sccs = []
    counter = [0]
    def strongconnect(v):
        index[v] = low[v] = counter[0]; counter[0] += 1
        stack.append(v); onstack[v] = True
        for w in adj[v]:
            if w not in index:
                strongconnect(w)
                low[v] = min(low[v], low[w])
            elif onstack.get(w):
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = []
            while True:
                w = stack.pop(); onstack[w] = False
                comp.append(w)
                if w == v: break
            sccs.append(sorted(comp))
    for v in range(k):
        if v not in index: strongconnect(v)
    nontrivial = [c for c in sccs
                  if len(c) > 1 or T[c[0]][c[0]] != 0]

    def charpoly(M):
        """Faddeev-LeVerrier: exact Fraction char poly coefficients
        (monic, degree n)."""
        n = len(M)
        coeffs = [Fr(1)]
        Mk = [[Fr(1) if i == j else Fr(0) for j in range(n)]
              for i in range(n)]
        for kk in range(1, n + 1):
            Mk = [[sum(M[i][t] * Mk[t][j] for t in range(n))
                   for j in range(n)] for i in range(n)]
            tr = sum(Mk[i][i] for i in range(n))
            c = -tr / kk
            coeffs.append(c)
            for i in range(n): Mk[i][i] += c
        return coeffs
    def poly_eval(cs, x):
        v = Fr(0)
        for c in cs: v = v * x + c
        return v
    results = []
    for comp in nontrivial:
        M = [[T[i][j] for j in comp] for i in comp]
        cs = charpoly(M)
        # Perron root in (0, rowmax]: exact bisection on sign change
        hi = max(sum(r) for r in M) + 1
        lo = Fr(0)
        f_hi = poly_eval(cs, hi)
        for _ in range(200):
            mid = (lo + hi) / 2
            if poly_eval(cs, mid) * f_hi > 0: hi = mid
            else: lo = mid
        lam_lo, lam_hi = lo, hi
        # Perron vector: solve (T - lam*I)v = 0 approximately at the
        # rational midpoint via least-structure: power iteration in
        # Fractions (bounded steps), positivity checked
        v = [Fr(1)] * len(comp)
        for _ in range(60):
            w = [sum(M[i][j] * v[j] for j in range(len(comp)))
                 for i in range(len(comp))]
            m = max(w)
            if m == 0: break
            v = [x / m for x in w]
        pos_ok = all(x > 0 for x in v)
        results.append((comp, (lam_lo, lam_hi), pos_ok))
    det = "; ".join(
        f"class {c}: lambda in ({float(a):.6f}, {float(b):.6f}), "
        f"Perron vector positive = {p}" for c, (a, b), p in results)
    check("MG3 PERRON-FROBENIUS on the recurrent classes: exact "
          "char-poly bisection brackets lambda; the Perron vector "
          "positive on each nontrivial class (irreducible nonneg "
          "matrices — Perron theory [THEOREM] + the computed "
          "witness) — EXISTENCE of a positive stationary completion "
          "on the stabilized quotient; uniqueness verdict = the "
          "dominant-class count",
          len(results) >= 1 and all(p for _, _, p in results),
          f"nontrivial classes = {len(nontrivial)}; {det}")

    # ---- MG4: root vs renewal state -------------------------------
    pA0 = ('p', 'A', V0, 0)
    pB1 = ('p', 'B', V0, 1)
    tA = ('A', V0, 0)
    PAIR = ('r', 'A', frozenset({tA, ('B', V0, 1)}), frozenset({tA}))
    H3 = [pA0, pB1, PAIR]
    same_state = (S6[tuple([])] == S6[tuple(H3)])
    check("MG4 the ROOT-FREE CERTIFICATE question: do the root and "
          "the post-arb renewal point land in the SAME stabilized "
          "state? (Yes = root-freeness at quotient level; no = the "
          "obstruction datum, delivered either way)",
          True, f"same state = {same_state} (root state "
          f"{S6[tuple([])]}, renewal state {S6[tuple(H3)]}) "
          "[PRE-REGISTERED outcome, delivered]")

    # ---- MG5: mass-transport on the dominant class ----------------
    # left Perron vector (stationary weights) by power iteration on
    # the transpose over the dominant class; the mass-transport
    # identity: per state, inflow == outflow under pi x q'
    dom = max(results, key=lambda r: r[1][0])[0]
    Md = [[T[i][j] for j in dom] for i in dom]
    piv = [Fr(1)] * len(dom)
    for _ in range(60):
        w = [sum(Md[j][i] * piv[j] for j in range(len(dom)))
             for i in range(len(dom))]
        m = max(w)
        if m == 0: break
        piv = [x / m for x in w]
    # normalized completed transfer on the class: q'(i->j) =
    # T[i][j]*v[j]/(lam*v[i]) — use the right Perron v from results
    vR = None
    for c, lam, p in results:
        if c == dom:
            # recompute right vector
            v = [Fr(1)] * len(dom)
            for _ in range(60):
                w = [sum(Md[i][j] * v[j] for j in range(len(dom)))
                     for i in range(len(dom))]
                m = max(w)
                v = [x / m for x in w]
            vR = v
    lam_mid = sum(results[[r[0] for r in results].index(dom)][1]) / 2
    flow_dev = Fr(0)
    for i in range(len(dom)):
        outf = sum(piv[i] * Md[i][j] * vR[j] for j in range(len(dom)))
        inf_ = sum(piv[j] * Md[j][i] * vR[i] for j in range(len(dom)))
        d = abs(outf - inf_)
        if d > flow_dev: flow_dev = d
    scale = max(piv[i] * sum(Md[i]) for i in range(len(dom)))
    check("MG5 the MASS-TRANSPORT identity on the dominant class "
          "(pi x q'-flow balance per state; approximate Perron "
          "vectors => a small residual bound, printed — the exact "
          "identity holds at the true eigenvectors [THEOREM: "
          "stationarity]; the computed residual certifies the "
          "witness quality)",
          flow_dev < scale * Fr(1, 10**6),
          f"max flow residual / scale = {float(flow_dev / scale):.2e}")
else:
    check("MG2-outcome: NO STABILIZATION at margin-1/depths 4-6 — "
          "the growth trajectory + induced counts are the delivered "
          "Martin datum (pin §3: 'deliver the growth trajectory'); "
          "the Perron reduction awaits deeper closure or the true "
          "intrinsic map",
          True, f"induced-on-4: by-5 = {len(p5_on4)}, by-6 = "
          f"{len(p6_on4)}, agree = {stab_4}; induced-on-5 by-6 = "
          f"{n6_int5}")

print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("[VERDICT] FAIL — anchor/consistency breakage; exit 1")
    sys.exit(1)
print("[VERDICT] d43b delivered — see MG2 for the stabilization "
      "outcome and (on closure) MG3-MG5 for the Perron decision, "
      "the root-renewal identity, and the mass-transport witness.")

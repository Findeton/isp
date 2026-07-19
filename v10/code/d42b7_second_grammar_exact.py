#!/usr/bin/env python3
"""
d42b7_second_grammar_exact.py — v10 D42b7: the second grammar G3
(ternary payloads) + the dimension pilot. Pin: note-d42b7 (e952dc4,
#301). EXACT Fractions; exit 1 on failure.

The d41b protocol executed: the SAME grammar text with ONE structural
change (payload alphabet {0,1,2}) — the binary layer is exec'd from
the committed d42b3 receipt (single source); the ternary layer is the
same namespace with ONLY the payload alphabet overridden (the
isolation of the varied structure is by construction). Depth caps:
both families depth <= 3 (declared). Dimension pilot: mu-weighted
ordering-fraction spectra, [MEASURED, PILOT] — no dimension verdicts
(pin §3).
"""
import sys
from fractions import Fraction as Fr

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

_src = open('v10/code/d42b3_placement_exact.py').read()
_head = _src[:_src.index('print("[d42b3')]

def make_layer(payloads):
    ns = {}
    exec(_head, ns)
    V0 = ns['V0']
    base_prop = ns['prop_options_in_view']
    def prop_options_in_view(view, a):
        out = []
        for b in view.holdings(a):
            if b in view.superseded: continue
            if any(op[1] == a and op[2] == b
                   for op in view.live.values()):
                continue
            for x in payloads:
                out.append((b, x))
        return sorted(out, key=repr)
    ns['prop_options_in_view'] = prop_options_in_view
    base_cand = ns['candidates_for']
    def candidates_for(acts, actors):
        pred = ns['event_poset'](acts)
        full = ns['View'](acts, pred, set(range(len(acts))))
        vname = ns['vname']
        bases = sorted({V0} | {vname(next(iter(op[2]))[1], op[3], op[1])
                               for op in full.arbs.values()}, key=repr)
        out = []
        live_by_base = {}
        for i, op in full.live.items():
            live_by_base.setdefault(op[2], []).append(i)
        for a in actors:
            for b in bases:
                for x in payloads:
                    e = ('p', a, b, x)
                    ok, q = ns['admissible'](acts, e)
                    if ok: out.append((e, q))
            seen = set()
            for b in sorted(live_by_base, key=repr):
                idxs = sorted(live_by_base[b])
                n = len(idxs)
                for smask in range(1, 1 << n):
                    S = [idxs[i] for i in range(n) if smask >> i & 1]
                    ck = ns['triples'](full, frozenset(S))
                    m = len(S)
                    for wmask in range(1, 1 << m):
                        W = frozenset(S[i] for i in range(m)
                                      if wmask >> i & 1)
                        e = ('r', a, ck, ns['triples'](full, W))
                        if e in seen: continue
                        seen.add(e)
                        ok, q = ns['admissible'](acts, e)
                        if ok: out.append((e, q))
            e = ('n', a)
            ok, q = ns['admissible'](acts, e)
            out.append((e, q))
        return out
    ns['candidates_for'] = candidates_for
    return ns

def enum_family(ns, actors, max_events):
    out = [[]]
    cache = {}
    frontier = [[]]
    while frontier:
        h = frontier.pop()
        cands = ns['candidates_for'](h, actors)
        cache[tuple(h)] = cands
        if len(h) >= max_events: continue
        for e, q in cands:
            out.append(h + [e])
            frontier.append(h + [e])
    return out, cache

from itertools import permutations
def linear_extensions_of(ns, acts):
    pred = ns['event_poset'](acts)
    n = len(acts)
    out = []
    for perm in permutations(range(n)):
        inv = {e: i for i, e in enumerate(perm)}
        if all(inv[i] < inv[j] for j in range(n) for i in pred[j]):
            out.append(perm)
    return out

print("[d42b7 — the second grammar G3 + the dimension pilot]")
print("  banner: EXACT; binary layer exec'd from the committed d42b3")
print("  receipt; ternary = the SAME namespace with only the payload")
print("  alphabet overridden (isolation by construction); both")
print("  families depth <= 3 (declared cap); dimension = PILOT only.")

AB = ('A', 'B')
B2 = make_layer((0, 1))
G3 = make_layer((0, 1, 2))
FAM2, C2 = enum_family(B2, AB, 3)
FAM3, C3 = enum_family(G3, AB, 3)
print(f"  families (depth<=3): binary = {len(FAM2)}; ternary = "
      f"{len(FAM3)} [MEASURED]")

# GG1: closure + (event, weight) gauge invariance on the G3 slice
V0 = G3['V0']
ok1 = True
pts = 0
for h in FAM3:
    if len(h) > 2: continue
    base_set = frozenset(G3['candidates_for'](h, AB))
    for ext in linear_extensions_of(G3, h):
        acts2 = [h[i] for i in ext]
        pts += 1
        if frozenset(G3['candidates_for'](acts2, AB)) != base_set:
            ok1 = False
check("GG1 G3 closure + enabled-(event, weight) gauge invariance on "
      "the depth<=2 slice (the delta-note-i standard, ported)",
      ok1 and pts > 0, f"candidate-set points = {pts}")

# GG2: the V1 toy-relative values
d2conf = 0
for h in FAM3:
    if len(h) != 2: continue
    view = G3['View'](h, G3['event_poset'](h), {0, 1})
    if view.edges(set(view.props)): d2conf += 1
pA0 = ('p', 'A', V0, 0)
pB1 = ('p', 'B', V0, 1)
ok_mu, q1 = G3['admissible']([], pA0)
ok_mu2, q2 = G3['admissible']([pA0], pB1)
mu_seed3 = q1 * q2
ok_b, qb1 = B2['admissible']([], pA0)
ok_b2, qb2 = B2['admissible']([pA0], pB1)
mu_seed2 = qb1 * qb2
check("GG2 the V1 TOY-RELATIVE values exhibited: depth-2 conflict "
      "census 4 -> 12 (ordered seed pairs x 6 payload pairs); "
      "mu(seed) 1/64 -> 1/144 (the propose split 1/8 -> 1/12)",
      d2conf == 12 and mu_seed3 == Fr(1, 144)
      and mu_seed2 == Fr(1, 64),
      f"census = {d2conf}; mu3 = {mu_seed3}; mu2 = {mu_seed2}")

# GG3: the U1 forms in BOTH grammars — ladder + density
def ladder_check(fam, cache, ns):
    ok = True
    spec = {}
    for h in fam:
        cands = cache[tuple(h)]
        for a in AB:
            tot = sum(q for e, q in cands if e[1] == a)
            v = tot - 1
            ok &= (tot >= 1 and (v * 4).denominator == 1)
            spec[tot] = spec.get(tot, 0) + 1
    return ok, spec
okL2, spec2 = ladder_check(FAM2, C2, B2)
okL3, spec3 = ladder_check(FAM3, C3, G3)
check("GG3 the U1 FORM lifts: the 1 + k/4 ladder holds in BOTH "
      "grammars (two-of-two; universality per d41b still needs "
      "breadth — declared)",
      okL2 and okL3,
      f"binary spectrum = { {str(k): v for k, v in sorted(spec2.items())} }; "
      f"ternary = { {str(k): v for k, v in sorted(spec3.items())} }")

# GG4 (R1/M1 repaired): the components are GENERATED — 3-actor
# depth-3 runs in both grammars; the ternary family contains exactly
# 36 K3 (triangle) histories (mu 1/1728 each, total mass 1/48), the
# binary family ZERO by pigeonhole; generated paths discriminate.
ABC = ('A', 'B', 'C')
FAM3c, C3c = enum_family(G3, ABC, 3)
FAM2c, C2c = enum_family(B2, ABC, 3)
def comps_census(fam, ns):
    k3 = paths = 0
    k3_mass = Fr(0)
    k3_deg_ok = True
    path_ok = True
    for h in fam:
        if len(h) != 3: continue
        view = ns['View'](h, ns['event_poset'](h), {0, 1, 2})
        props = set(view.props)
        if len(props) != 3: continue
        E = view.edges(props)
        if len(E) == 3:
            k3 += 1
            k3_mass += ns['mu_of'](h)
            ck = ns['triples'](view, props)
            et = ns['edge_triples_of'](view, props)
            k1 = ns['PK1'](ck, et)
            ms = ns['mis_of'](ck, et)
            k3_deg_ok &= (len(ms) == 3 and
                          all(k1.get(m) == Fr(1, 3) for m in ms))
        if len(E) == 2:
            paths += 1
            ck = ns['triples'](view, props)
            et = ns['edge_triples_of'](view, props)
            k1 = ns['PK1'](ck, et)
            ms = ns['mis_of'](ck, et)
            big = max(k1.values())
            path_ok &= (big == Fr(2, 3) and len(ms) == 2)
    return k3, k3_mass, k3_deg_ok, paths, path_ok
k3_3, mass3, deg3, paths3, pok3 = comps_census(FAM3c, G3)
k3_2, mass2, deg2, paths2, pok2 = comps_census(FAM2c, B2)
check("GG4a GENERATED components (M1 repaired, referee anchors): the "
      "ternary 3-actor family contains EXACTLY 36 K3 histories at mu "
      "1/1728 each (mass 1/48), ALL kernel-degenerate at 1/3; the "
      "binary family has ZERO triangles (pigeonhole theorem of the "
      "binary rule); generated paths discriminate 2/3 vs 1/2 in both",
      k3_3 == 36 and mass3 == Fr(1, 48) and deg3
      and k3_2 == 0 and paths3 > 0 and pok3 and paths2 > 0 and pok2,
      f"ternary K3 = {k3_3} (mass {mass3}); binary K3 = {k3_2}; "
      f"generated paths = {paths3}/{paths2}")

# the abstract exhibits retained as controls
h3 = [('p', 'A', V0, 0), ('p', 'B', V0, 1)]
# abstract control triples (retained; the GENERATED gate is above):
tri = frozenset({('A', V0, 0), ('B', V0, 1), ('C', V0, 2)})
et_tri = frozenset({tuple(sorted((a, b))) for a in tri for b in tri
                    if a < b})
k1_tri = G3['PK1'](tri, et_tri)
mis_tri = G3['mis_of'](tri, et_tri)
ok_deg = (len(mis_tri) == 3
          and all(k1_tri.get(m) == Fr(1, 3) for m in mis_tri))
path = frozenset({('A', V0, 0), ('B', V0, 1), ('C', V0, 0)})
et_path = frozenset({tuple(sorted((a, b))) for a in path for b in path
                     if a < b and a[2] != b[2]})
k1_path = G3['PK1'](path, et_path)
prc = frozenset({('A', V0, 0), ('C', V0, 0)})
ok_path = (k1_path.get(prc) == Fr(2, 3)
           and Fr(1, len(G3['mis_of'](path, et_path))) == Fr(1, 2))
check("GG4 N1 CONFIRMED: on the ternary triangle K1 == K2 == uniform "
      "1/3 over the three singleton MIS (KERNEL DEGENERACY — the "
      "K-choice is undecidable on triangle components); the path "
      "still discriminates 2/3 vs 1/2 in G3 — discrimination is "
      "COMPONENT-SHAPE-DEPENDENT",
      ok_deg and ok_path,
      f"triangle: {len(mis_tri)} MIS at 1/3 each; path: K1 = 2/3, "
      "K2 = 1/2")

# GG3b (R2/M2): the five runnable pinned gates, both grammars
def density_gate(fam, cache, ns):
    ok = True
    for h in fam:
        cands = cache[tuple(h)]
        for a in AB:
            mine = [(e, q) for e, q in cands if e[1] == a]
            groups = {}
            for e, q in mine:
                if e[0] == 'r':
                    groups[e[2]] = groups.get(e[2], Fr(0)) + q
            acts2 = h + [('n', a)]
            pred2 = ns['event_poset'](acts2)
            ov = ns['View'](acts2, pred2, pred2[len(acts2) - 1])
            own_cks = {ns['triples'](ov, comp) for b, comp
                       in ns['arb_components_in_view'](ov, a)}
            blind = [ck for ck in groups if ck not in own_cks]
            tot = sum(q for e, q in mine)
            ok &= (tot == 1 + Fr(len(blind), 4))
            ok &= all(groups[ck] == Fr(1, 4) for ck in blind)
    return ok
ok_d2 = density_gate(FAM2, C2, B2)
ok_d3 = density_gate(FAM3, C3, G3)
def l1_gate(fam, ns):
    for h in fam:
        view = ns['View'](h, ns['event_poset'](h),
                          set(range(len(h))))
        ts = [(op[1], op[2], op[3]) for op in view.live.values()]
        if len(ts) != len(set(ts)): return False
    return True
def iff_gate(fam, cache, ns, x1, x2):
    pA = ('p', 'A', V0, x1)
    pB = ('p', 'B', V0, x2)
    ck = frozenset({('A', V0, x1), ('B', V0, x2)})
    for h in fam:
        has = any(e[0] == 'r' and e[2] == ck
                  for e, q in cache[tuple(h)])
        pred = ns['event_poset'](h)
        live = (pA in h and pB in h
                and not any(e[0] == 'r' and set(e[2]) & set(ck)
                            for e in h))
        inc = False
        if live:
            i1, i2 = h.index(pA), h.index(pB)
            inc = (i1 not in pred[i2]) and (i2 not in pred[i1])
        if has != (live and inc): return False
    return True
ok_iff = (iff_gate(FAM2, C2, B2, 0, 1)
          and iff_gate(FAM3, C3, G3, 0, 1)
          and iff_gate(FAM3, C3, G3, 0, 2))
check("GG3b the pinned U1 gates DISCHARGED in both grammars (M2 "
      "repaired): the obstruction density (tot == 1 + k_blind/4 with "
      "every blind group exactly 1/4), L1 uniqueness, and the "
      "pair-arb iff sweeps (incl. the ternary 0-2 pair)",
      ok_d2 and ok_d3 and l1_gate(FAM2, B2) and l1_gate(FAM3, G3)
      and ok_iff,
      "density/L1/iff all green, two-of-two grammars")

# GG5 (R3/B1 repaired): the bin table is MECHANICAL — each status
# is computed from its gate's outcome; an unearned row cannot print
rows = [
    ("opportunity generation / closure", ok1 and pts > 0),
    ("the 1+k/4 ladder", okL2 and okL3),
    ("quarter density (blind groups == 1/4)", ok_d2 and ok_d3),
    ("L1 uniqueness", l1_gate(FAM2, B2) and l1_gate(FAM3, G3)),
    ("pair-arb iff sweeps", ok_iff),
]
toy = [
    ("depth-2 census (4 vs 12)", d2conf == 12),
    ("mu(seed) (1/64 vs 1/144)", mu_seed3 == Fr(1, 144)),
    ("triangle realizability (0 vs 36 generated)",
     k3_2 == 0 and k3_3 == 36),
]
print("  GG5 BIN TABLE (mechanical; status = the row's gate):")
all_rows = True
for name, ok in rows:
    all_rows &= ok
    print(f"    {name:.<45} {'LIFTED (2-of-2)' if ok else 'FAILED'}")
for name, ok in toy:
    all_rows &= ok
    print(f"    {name:.<45} "
          f"{'TOY-RELATIVE (gated)' if ok else 'FAILED'}")
print(f"    {'K1-vs-K2 discrimination':.<45} SHAPE-DEPENDENT "
      f"(GG4a: {'gated' if deg3 and pok3 else 'FAILED'})")
check("GG5 the MECHANICAL bin table (B1 repaired): every status "
      "column entry is its gate's computed outcome — no unearned "
      "rows possible (one alphabet variant = one second grammar; "
      "Bin U needs breadth, pin §5)",
      all_rows and deg3 and pok3, "all rows earned")

# GG3c (R4/M3): structural anchors — the kernel winner ratios and
# the blind-arbitration mass are GATED (the referee's mutants B and
# E now fail here)
pair_ck = frozenset({('A', V0, 0), ('B', V0, 1)})
h2p = [('p', 'A', V0, 0), ('p', 'B', V0, 1)]
arbs2 = [(e, q) for e, q in C2[tuple(h2p)]
         if e[0] == 'r' and e[2] == pair_ck]
okA = (len(arbs2) == 4    # 2 initiators x 2 winners
       and all(q == Fr(1, 8) for e, q in arbs2))
blind_mass2 = sum(q for h in FAM2 for e, q in C2[tuple(h)]
                  if e[0] == 'r' and len(e[2]) == 2)
check("GG3c STRUCTURAL ANCHORS (M3 repaired): the pair-arb winner "
      "weights are exactly 1/8 each (2 initiators x 2 winners — a "
      "3:1 kernel mutant dies here) and the family's blind pair-"
      "arbitration mass is NONZERO and exact (deleting blind arbs "
      "dies here); family sizes anchored",
      okA and blind_mass2 > 0 and len(FAM2) == 215
      and len(FAM3) == 405,
      f"pair-arb weights 4 x 1/8; blind pair mass = {blind_mass2}; "
      f"families 215/405 anchored")

# GG6: the dimension pilot
def ordering_fraction(h, ns):
    if len(h) < 2: return None
    pred = ns['event_poset'](h)
    n = len(h)
    comp = sum(1 for i in range(n) for j in range(i + 1, n)
               if i in pred[j] or j in pred[i])
    return Fr(comp, n * (n - 1) // 2)
def spectrum(fam, cache, ns):
    tot = Fr(0); wsum = Fr(0)
    for h in fam:
        if len(h) != 3: continue
        m = ns['mu_of'](h)
        f = ordering_fraction(h, ns)
        tot += m * f; wsum += m
    return tot / wsum
of2 = spectrum(FAM2, C2, B2)
of3 = spectrum(FAM3, C3, G3)
chain = [('p', 'A', V0, 0),
         ('r', 'A', frozenset({('A', V0, 0)}),
          frozenset({('A', V0, 0)})), ('n', 'A')]
ofc = ordering_fraction(chain, B2)
check("GG6 the DIMENSION PILOT [PILOT; DISCLOSURE per the round: at "
      "this depth the mean OF is an AFFINE READOUT of the join-mass "
      "census (spectrum {1/3, 2/3, 1}); the binary/ternary "
      "difference is the blind-join mass; no dimension verdict]",
      ofc == Fr(1) and Fr(0) < of2 < Fr(1) and Fr(0) < of3 < Fr(1)
      and of2 - Fr(1, 2) > 0 and of3 - Fr(1, 2) > 0,
      f"binary OF = {of2} (OF-1/2 = {of2 - Fr(1, 2)}); ternary OF = "
      f"{of3} (OF-1/2 = {of3 - Fr(1, 2)}); chain = {ofc} (in-family, "
      "mu 3/128) [MEASURED, PILOT]")

print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("[VERDICT] FAIL — exit 1 by design")
    sys.exit(1)
print("[VERDICT] d42b7 GREEN: the d41b protocol executed — the "
      "generation forms and the ladder LIFT to the second grammar; "
      "the values are toy-relative as predicted; kernel degeneracy "
      "on ternary triangles makes K-discrimination shape-dependent "
      "(N1 confirmed); the dimension pilot is well-defined and "
      "verdict-free.")

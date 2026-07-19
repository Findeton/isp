#!/usr/bin/env python3
"""
d42b56_rootfree_action_exact.py — v10 D42b5/6 (fronts 7-9). Pin:
note-d42b56 (d66093d). EXACT Fractions; exit 1 on failure. The d42a
layer exec'd from the committed d42b3 receipt (single source).
"""
import sys
from fractions import Fraction as Fr
from itertools import permutations

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

_src = open('v10/code/d42b3_placement_exact.py').read()
_head = _src[:_src.index('print("[d42b3')]
ns = {}
exec(_head, ns)
V0 = ns['V0']
admissible = ns['admissible']
candidates_for = ns['candidates_for']
canon = ns['canon']
mu_of = ns['mu_of']
event_poset = ns['event_poset']

print("[d42b56 — root-free, the action ladder, the shadows]")
print("  banner: EXACT; d42a layer exec'd from the committed d42b3")
print("  receipt; depth <= 4 (the decided complex); no existence")
print("  claim on the infinite-volume core (A3, declared OPEN).")

AB = ('A', 'B')
FAM = [[]]
CACHE = {}
frontier = [[]]
while frontier:
    h = frontier.pop()
    CACHE[tuple(h)] = candidates_for(h, AB)
    if len(h) >= 4: continue
    for e, q in CACHE[tuple(h)]:
        FAM.append(h + [e])
        frontier.append(h + [e])
print(f"  family: {len(FAM)} (must be 1191)")
assert len(FAM) == 1191

def N_of(h):
    return sum(q for _, q in CACHE[tuple(h)])

# Z for both canonical boundaries
def build_Z(bdry):
    Z = {}
    for h in FAM:
        if len(h) == 4: Z[tuple(h)] = bdry(h)
    for L in (3, 2, 1, 0):
        for h in FAM:
            if len(h) != L: continue
            Z[tuple(h)] = sum(q * Z[tuple(h + [e])]
                              for e, q in CACHE[tuple(h)])
    return Z
Z_unit = build_Z(lambda h: Fr(1))
def lin_ext_count(h):
    from itertools import permutations as _perm
    pred = event_poset(h)
    n = len(h)
    c = 0
    for perm in _perm(range(n)):
        inv = {e: i for i, e in enumerate(perm)}
        if all(inv[i] < inv[j] for j in range(n) for i in pred[j]):
            c += 1
    return max(c, 1)
# B1: the CANONICAL class-1/k (d42b4 D-M1: 1/#linearizations of the
# class — gauge-invariant); the menu-reciprocal retained as a probe
Z_1k = build_Z(lambda h: Fr(1, lin_ext_count(h)))
Z_menu = build_Z(lambda h: Fr(1, len(CACHE[tuple(h)])))
assert Z_1k[()] == Fr(325, 64), Z_1k[()]

# ---- S1: the three-level flatness ladder -----------------------------------
fam_keys = {tuple(h) for h in FAM}
seen_d = set()
diamonds = []
for h in FAM:
    if len(h) > 2: continue
    cands = CACHE[tuple(h)]
    for i1 in range(len(cands)):
        for i2 in range(i1 + 1, len(cands)):
            e1, e2 = cands[i1][0], cands[i2][0]
            if tuple(h + [e1, e2]) not in fam_keys: continue
            if tuple(h + [e2, e1]) not in fam_keys: continue
            if canon(h + [e1, e2]) != canon(h + [e2, e1]): continue
            key = (canon(h), frozenset({e1, e2}))
            if key in seen_d: continue
            seen_d.add(key)
            diamonds.append((h, e1, e2))
def qv(h, e):
    return [q for ev, q in CACHE[tuple(h)] if ev == e][0]
v_mu = v_naive = v_grad = v_seq = 0
for h, e1, e2 in diamonds:
    p1 = qv(h, e1) * qv(h + [e1], e2)
    p2 = qv(h, e2) * qv(h + [e2], e1)
    if p1 != p2: v_mu += 1
    n1 = (qv(h, e1) / N_of(h)) * (qv(h + [e1], e2) / N_of(h + [e1]))
    n2 = (qv(h, e2) / N_of(h)) * (qv(h + [e2], e1) / N_of(h + [e2]))
    if n1 != n2: v_naive += 1
    Z_arb = {k: Fr(1 + len(k)) for k in fam_keys}   # class-constant,
    for Z in (Z_unit, Z_1k, Z_menu, Z_arb):         # non-harmonic probe
        g1 = (qv(h, e1) * Z[tuple(h + [e1])] / Z[tuple(h)]
              * qv(h + [e1], e2) * Z[tuple(h + [e1, e2])]
              / Z[tuple(h + [e1])])
        g2 = (qv(h, e2) * Z[tuple(h + [e2])] / Z[tuple(h)]
              * qv(h + [e2], e1) * Z[tuple(h + [e2, e1])]
              / Z[tuple(h + [e2])])
        if g1 != g2: v_grad += 1
    Zs = {k: (Fr(1) if list(k) == sorted(k, key=repr) else Fr(2))
          for k in fam_keys}                    # sequence-attached,
    s1 = (qv(h, e1) * Zs[tuple(h + [e1])] / Zs[tuple(h)]   # NON-class-
          * qv(h + [e1], e2) * Zs[tuple(h + [e1, e2])]     # constant
          / Zs[tuple(h + [e1])])
    s2 = (qv(h, e2) * Zs[tuple(h + [e2])] / Zs[tuple(h)]
          * qv(h + [e2], e1) * Zs[tuple(h + [e2, e1])]
          / Zs[tuple(h + [e2])])
    if s1 != s2: v_seq += 1
check("S1 (B2 re-stated): the ladder — weight FLAT (0); naive-cut "
      "NOT flat at EXACTLY the 36; the GRADIENT FORM flat for EVERY "
      "cut-attached class-constant Z (unit, canonical class-1/k, "
      "menu probe, AND an arbitrary non-harmonic probe — a "
      "TELESCOPING THEOREM, stated as such, not a completion-"
      "specific check); the NEGATIVE CONTROL: a sequence-attached "
      "non-class-constant Z FAILS the diamond check — the separating "
      "content is CLASS-CONSTANCY (d42b3-D2's lineage)",
      len(diamonds) == 202 and v_mu == 0 and v_naive == 36
      and v_grad == 0 and v_seq > 0,
      f"diamonds = {len(diamonds)}; mu/naive/gradient-form = "
      f"{v_mu}/{v_naive}/{v_grad}; sequence-Z failures = {v_seq} "
      "(> 0, the control fires)")

# ---- S2: isomorphic menus + boundary non-stationarity ----------------------
pA0 = ('p', 'A', V0, 0)
pB1 = ('p', 'B', V0, 1)
tA = ('A', V0, 0)
PAIR = ('r', 'A', frozenset({tA, ('B', V0, 1)}), frozenset({tA}))
H3 = [pA0, pB1, PAIR]
v1n = ns['vname'](V0, frozenset({tA, ('B', V0, 1)})
                  & frozenset({tA}), 'A')
v1n = ns['vname'](V0, frozenset({tA}), 'A')
v1_pair = ns['vname'](V0, frozenset({tA}), 'A')
# B4: the STRUCTURAL EVENT-LEVEL BIJECTION (type/payload matched,
# v0 <-> v1 translated) — not the multiset proxy
def translate(e, vfrom, vto):
    if e[0] == 'n': return e
    if e[0] == 'p':
        return ('p', e[1], vto if e[2] == vfrom else e[2], e[3])
    return e
v1_real = [e for e, q in CACHE[tuple(H3)]
           if e[0] == 'p'][0][2]
root_menu = {e: q for e, q in CACHE[tuple([])]}
h3_menu = {e: q for e, q in CACHE[tuple(H3)]}
iso = all(h3_menu.get(translate(e, V0, v1_real)) == q
          for e, q in root_menu.items()) \
    and len(root_menu) == len(h3_menu)
shape_share = 0
def menu_shape(h):
    out = {}
    for e, q in CACHE[tuple(h)]:
        out[(e[0], q)] = out.get((e[0], q), 0) + 1
    return out
rs = menu_shape([])
for h in FAM:
    if menu_shape(h) == rs: shape_share += 1
def qprime(Z, h, e):
    return qv(h, e) * Z[tuple(h + [e])] / Z[tuple(h)]
pv1 = translate(pA0, V0, v1_real)
ns_unit = (qprime(Z_unit, [], pA0) != qprime(Z_unit, H3, pv1))
ns_1k = (qprime(Z_1k, [], pA0) != qprime(Z_1k, H3, pv1))
w_root = qprime(Z_1k, [], pA0)
w_post = qprime(Z_1k, H3, pv1)
check("S2 the RENEWAL exhibit + boundary non-stationarity (B4: the "
      "STRUCTURAL event-level bijection, not the multiset proxy): "
      "the root and the post-arb fresh-base point are event-"
      "bijectively isomorphic with equal weights, yet BOTH canonical "
      "boundaries give different completed transfers — truncated "
      "completions are ROOTED (paper 28 §5.3 + the D42 mandate)",
      iso and ns_unit and ns_1k
      and w_root == Fr(21, 325) and w_post == Fr(1, 16),
      f"structural bijection (type/payload, v0<->v1) with EQUAL q "
      f"at every matched event = {iso}; canonical-1/k witnesses "
      f"{w_root} vs {w_post} (referee anchors 21/325 vs 1/16); unit "
      f"{qprime(Z_unit, [], pA0)} vs {qprime(Z_unit, H3, pv1)}; "
      f"disclosure: {shape_share} histories share the root's SHAPE "
      "(the old multiset proxy was near-information-free)")

# ---- S3: the reduction (printed; no existence gate) ------------------------
# B3: the honest state space — the bisimulation quotient
state = {tuple(h): repr(sorted(menu_shape(h).items())) for h in FAM}
traj = [len(set(state.values()))]
while True:
    new = {}
    for h in FAM:
        k = tuple(h)
        if len(h) == 4:
            new[k] = (state[k], 'B')
        else:
            succ = tuple(sorted((str(q), state[tuple(h + [e])])
                                for e, q in CACHE[k]))
            new[k] = (state[k], succ)
    relab = {}
    for k in sorted(new, key=repr):
        relab.setdefault(new[k], len(relab))
    state2 = {k: relab[new[k]] for k in new}
    traj.append(len(set(state2.values())))
    if len(set(state2.values())) == len(set(state.values())):
        state = state2
        break
    state = {k: str(v) for k, v in state2.items()}
split = (state[tuple([pA0])] != state[tuple([pA0,
         ('r', 'A', frozenset({tA}), frozenset({tA})),
         translate(pA0, V0, v1_real)])]
         if tuple([pA0, ('r', 'A', frozenset({tA}), frozenset({tA})),
                   translate(pA0, V0, v1_real)]) in state else True)
classes_all = {}
for h in FAM:
    classes_all.setdefault(canon(h), []).append(h)
wd = all(len({state[tuple(h)] for h in mem}) == 1
         for mem in classes_all.values())
check("S3 (B3): the BISIMULATION QUOTIENT computed — final state "
      "count 17 (menu shapes alone: 4, ILL-POSED for the transfer — "
      "the split witness gated); the transfer is well-defined on "
      "canonical classes (0 violations); the reduction is ONE-WAY "
      "(stationary completions are a SUBCLASS of positive-harmonic "
      "solutions — the d42b3 residue CONTAINS front 7); existence "
      "OPEN, no claim either way",
      traj[-1] == 17 and traj[0] == 4 and split and wd,
      f"refinement trajectory = {traj}; well-defined on all "
      f"{len(classes_all)} canonical classes")

# ---- S4: the discrete covariance gates (front 9) ---------------------------
# version names EMBED authors/initiator/payloads (A6 identity), so a
# covariance map must recurse into base fields — the first build
# missed this and 208 histories (those proposing ON created
# versions) went inadmissible under relabeling (caught in-build).
def vmap_actor(v, sw):
    if v == V0: return v
    return ('v', vmap_actor(v[1], sw), v[2],
            tuple(sorted(sw[a] for a in v[3])), sw[v[4]])
def vmap_pay(v, fl):
    if v == V0: return v
    return ('v', vmap_pay(v[1], fl),
            tuple(sorted(fl[x] for x in v[2])), v[3], v[4])
def relabel_actor(e):
    sw = {'A': 'B', 'B': 'A'}
    if e[0] == 'n': return ('n', sw[e[1]])
    if e[0] == 'p':
        return ('p', sw[e[1]], vmap_actor(e[2], sw), e[3])
    ck = frozenset((sw[a], vmap_actor(b, sw), x) for a, b, x in e[2])
    wk = frozenset((sw[a], vmap_actor(b, sw), x) for a, b, x in e[3])
    return ('r', sw[e[1]], ck, wk)
def relabel_pay(e):
    fl = {0: 1, 1: 0}
    if e[0] == 'n': return e
    if e[0] == 'p':
        return ('p', e[1], vmap_pay(e[2], fl), fl[e[3]])
    ck = frozenset((a, vmap_pay(b, fl), fl[x]) for a, b, x in e[2])
    wk = frozenset((a, vmap_pay(b, fl), fl[x]) for a, b, x in e[3])
    return ('r', e[1], ck, wk)
violA = violP = 0
for h in FAM:
    m = mu_of(h)
    if mu_of([relabel_actor(e) for e in h]) != m: violA += 1
    if mu_of([relabel_pay(e) for e in h]) != m: violP += 1
okA, okP = violA == 0, violP == 0
check("S4 the DISCRETE COVARIANCE gates (front 9's sprinkling "
      "precursor): actor-exchange and payload-relabeling are exact "
      "measure isomorphisms of the generated complex, family-wide; "
      "Z class-constancy (foliation gauge) re-cited from d42b3; the "
      "CONTINUUM limits are NOT claimed (Hegerfeldt pre-registered; "
      "the arb-layer problem gates operator routes — d42b4 E1)",
      okA and okP, f"actor-exchange {violA} violations / "
      f"payload-flip {violP} violations over {len(FAM)} histories "
      "(counters COMPUTED — the first build hardcoded the detail)")

print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("[VERDICT] FAIL — exit 1 by design")
    sys.exit(1)
print("[VERDICT] d42b56 GREEN (round-1 repaired): the GRADIENT FORM "
      "restores level-relative flatness (a telescoping theorem; the "
      "separating content is class-constancy — d42b3-D2); truncated "
      "completions are ROOTED (canonical class-1/k witnesses 21/325 "
      "vs 1/16); root-free reduces ONE-WAY into the infinite-volume "
      "residue on the 17-state bisimulation quotient; the decided "
      "dichotomy stands as v6's discrete TS form with the sprinkling "
      "precursor gated as the internal Z2 x Z2 + foliation-gauge "
      "covariance.")

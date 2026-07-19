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
def kcount(h):
    cands = candidates_for(h, AB) if tuple(h) not in CACHE \
        else CACHE[tuple(h)]
    return Fr(1)
Z_1k = build_Z(lambda h: Fr(1, max(1, len(CACHE[tuple(h)]))))

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
v_mu = v_naive = v_grad = 0
for h, e1, e2 in diamonds:
    p1 = qv(h, e1) * qv(h + [e1], e2)
    p2 = qv(h, e2) * qv(h + [e2], e1)
    if p1 != p2: v_mu += 1
    n1 = (qv(h, e1) / N_of(h)) * (qv(h + [e1], e2) / N_of(h + [e1]))
    n2 = (qv(h, e2) / N_of(h)) * (qv(h + [e2], e1) / N_of(h + [e2]))
    if n1 != n2: v_naive += 1
    for Z in (Z_unit, Z_1k):
        g1 = (qv(h, e1) * Z[tuple(h + [e1])] / Z[tuple(h)]
              * qv(h + [e1], e2) * Z[tuple(h + [e1, e2])]
              / Z[tuple(h + [e1])])
        g2 = (qv(h, e2) * Z[tuple(h + [e2])] / Z[tuple(h)]
              * qv(h + [e2], e1) * Z[tuple(h + [e2, e1])]
              / Z[tuple(h + [e2])])
        if g1 != g2: v_grad += 1
check("S1 the THREE-LEVEL FLATNESS LADDER on all 202 diamonds: the "
      "weight level FLAT (0), the naive cut-normalized level NOT "
      "flat at EXACTLY the 36, the gradient-completed level FLAT "
      "again under BOTH boundaries (0) — completion RESTORES the "
      "action-level check; flatness is level-relative (paper 29's "
      "lesson on our object)",
      len(diamonds) == 202 and v_mu == 0 and v_naive == 36
      and v_grad == 0,
      f"diamonds = {len(diamonds)}; violations mu/naive/gradient = "
      f"{v_mu}/{v_naive}/{v_grad}")

# ---- S2: isomorphic menus + boundary non-stationarity ----------------------
pA0 = ('p', 'A', V0, 0)
pB1 = ('p', 'B', V0, 1)
tA = ('A', V0, 0)
PAIR = ('r', 'A', frozenset({tA, ('B', V0, 1)}), frozenset({tA}))
H3 = [pA0, pB1, PAIR]
def menu_shape(h):
    out = {}
    for e, q in CACHE[tuple(h)]:
        out[(e[0], q)] = out.get((e[0], q), 0) + 1
    return out
iso = menu_shape([]) == menu_shape(H3)
def qprime(Z, h, e):
    return qv(h, e) * Z[tuple(h + [e])] / Z[tuple(h)]
v1n = ns['vname'](V0, frozenset({tA}), 'A')
pv1 = [e for e, q in CACHE[tuple(H3)] if e[0] == 'p'][0]
ns_unit = (qprime(Z_unit, [], pA0) != qprime(Z_unit, H3, pv1))
ns_1k = (qprime(Z_1k, [], pA0) != qprime(Z_1k, H3, pv1))
check("S2 the RENEWAL exhibit + boundary non-stationarity: the root "
      "and the post-arb fresh-base point have ISOMORPHIC menus (event "
      "shapes x weights as multisets), yet BOTH canonical boundaries "
      "give different completed transfers there — the truncated "
      "completions are ROOTED (paper 28's uniform-rooting theorem "
      "anticipated this)",
      iso and ns_unit and ns_1k,
      f"menus equal = {iso}; q'(root) = {qprime(Z_unit, [], pA0)} vs "
      f"q'(post-arb) = {qprime(Z_unit, H3, pv1)} (unit); "
      f"{qprime(Z_1k, [], pA0)} vs {qprime(Z_1k, H3, pv1)} (1/k)")

# ---- S3: the reduction (printed; no existence gate) ------------------------
print("  S3 THE REDUCTION (A3, declared): a root-free/stationary")
print("  completion is a positive eigenvector of the local transfer")
print("  on menu-isomorphism states, Z(h) = f(state)*lambda^{-depth};")
print("  at finite depth the boundary-free constraint system is")
print("  underdetermined, and existence IS d42b3's infinite-volume")
print("  positive-harmonic residue — front 7 and that residue are ONE")
print("  open core. No existence claim either way at this scope.")
check("S3 the reduction stated; OPEN status declared (== the d42b3 "
      "residue; one core, not two)", True and iso,
      "conditional on the S2 renewal exhibit above")

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
print("[VERDICT] d42b56 GREEN: completion restores level-relative "
      "flatness (the action check); truncated completions are rooted "
      "and the root-free question reduces to the ONE infinite-volume "
      "residue; the decided dichotomy stands as v6's discrete TS "
      "form with the sprinkling precursor gated as exact symmetry "
      "covariance.")

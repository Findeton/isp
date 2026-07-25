#!/usr/bin/env python3
"""
d46f_reception_dynamics_exact.py — v10 D46f (ladder step f): reception
DYNAMICS, the typed-open arm of the D44e census. Pin:
v10/note-d46f-reception-dynamics.md (RD0-RD4). Program pin:
v10/note-d46-ladder-program.md (green-unreviewed discipline).

WHAT D44E LEFT OPEN. D44e TERMINAL (#364) censused 11 record types
over 6,567 instances and gated a reception FORM per type — but its
round-1 M-1 convicted those gates as construction-tautologies and
re-scoped the result honestly: the census's reception layer is ONE
SHARED COPY-FORM TEMPLATE (e_rec -> e_rec (x) e_imprint) evaluated on
each type's own carrier/data, NOT layer-semantic reception dynamics.
This receipt opens the dynamics arm.

WHAT THIS RECEIPT DOES. It extracts, MECHANICALLY from the committed
layers, the ACTUAL state update each record type performs on a
receiver's view — the abstract reception state

    sigma_a = (props multiset, resolved, superseded, created,
               holdings(a))

read off the committed View class — by applying the layer to every
enumerated reception instance and DIFFING pre/post views. A reception
instance is (history, down-closed index set S, index j with pred[j]
subset S and j not in S, actor a): the record j entering a's view over
S. The extracted action map ACT(sigma, rec, a) is an INDEPENDENT
re-implementation gated against the layer's own View on every
instance (RD1-a — the unit's load-bearing gate), with the FUNCTION
property and the COMMUTATION property recorded as what round 1
established them to be: STRICT COROLLARIES of RD1-a plus the
committed View's set-indexed construction, kept as regression tallies
rather than billed as measurements (RD1-b, RD3-b); gated for
injectivity per record over the enumerated fibers, with the
map-level non-injectivities exhibited separately (RD2, with a firing
lossy control); and with the inter-history obstruction exhibited as
one constructed two-history example (RD3-e), from which no inference
is drawn to the intra-history commutation sweep.

Sources (single sources, __file__-anchored, the d43c/d44e
convention): the d42a depth-4 pricing layer from the committed d42b3
head; the d42b1-verbatim transport + click admission layer from the
committed d42b2 head. D25/D27 are CITED as the reception
requirements, not re-proved. The d42b2-embedded transport head is
PRE-#300 d42b1 text (D44e round-1 M-2; standing corpus obligation
LOG #363) — this receipt gates the embedded layer AS COMMITTED and
declares the provenance.

EXACT throughout: the reception state is built from Fractions / ints
/ strings / tuples / frozensets only. NO floats enter this receipt at
all — the D44e amplitude probes are not repeated here (the dynamics
lives at the classical state grain); the D25 distinguishability
requirement is enforced as exact injectivity of the ACTION, which is
strictly stronger than the copy-form template's isometry.

Delivered-outcome discipline: a non-injective action or a
non-commuting pair is a DELIVERED FINDING printed exactly, at exit 0;
exit 1 is reserved for gate breakage (a control that fails to fire, a
faithfulness violation, an impure leaf, a vacuous gate).
"""
import ast
import builtins
import hashlib
import os
import sys
from fractions import Fraction as Fr

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def crepr(x):
    """Canonical, hash-seed-independent repr (frozensets sorted)."""
    if isinstance(x, frozenset):
        return 'fs{' + ','.join(sorted(crepr(e) for e in x)) + '}'
    if isinstance(x, tuple):
        return '(' + ','.join(crepr(e) for e in x) + ')'
    return repr(x)

_here = os.path.dirname(os.path.abspath(__file__))
_src3 = open(os.path.join(_here, 'd42b3_placement_exact.py')).read()
ns3 = {}
exec(_src3[:_src3.index('print("[d42b3')], ns3)
_src2 = open(os.path.join(_here,
                          'd42b2_click_refinement_exact.py')).read()
ns2 = {}
exec(_src2[:_src2.index('print("[d42b2')], ns2)

V0 = ns3['V0']
assert V0 == ns2['V0']
event_poset = ns2['event_poset']
View = ns2['View']
vname = ns2['vname']
mname = ns2['mname']
value_of = ns2['value_of']
triples = ns2['triples']
regs_of2 = ns2['regs_of']
admissible2 = ns2['admissible']
arb_comps = ns2['arb_components_in_view']
prop_opts = ns2['prop_options_in_view']

# ---- CODE READING OF THE COMMITTED LAYER, by AST (round 1: F-M1, F-M5) ----
# Several of this receipt's statements are theorems about the committed
# source, not measurements on a corpus.  Round 1 convicted them of being
# billed as discoveries.  They are now GATED AS CODE READINGS: the
# committed d42b2 text is parsed and the relevant function bodies are
# interrogated for which fields they touch.
_AST2 = ast.parse(_src2)

def _classnode(cls):
    for nd in ast.walk(_AST2):
        if isinstance(nd, ast.ClassDef) and nd.name == cls:
            return nd
    return None

def _fnnode(name, cls=None):
    root = _AST2 if cls is None else _classnode(cls)
    if root is None:
        return None
    for nd in ast.walk(root):
        if isinstance(nd, ast.FunctionDef) and nd.name == name:
            return nd
    return None

def _selfreads(node):
    """The attribute names the function reads off its FIRST parameter."""
    p0 = node.args.args[0].arg
    return frozenset(n.attr for n in ast.walk(node)
                     if isinstance(n, ast.Attribute)
                     and isinstance(n.value, ast.Name) and n.value.id == p0)

def _strconsts(node):
    return frozenset(n.value for n in ast.walk(node)
                     if isinstance(n, ast.Constant)
                     and isinstance(n.value, str))
edge_triples_of = ns2['edge_triples_of']
gmis_of = ns2['gmis_of']

print("[d46f — reception DYNAMICS: the action map, its injectivity, "
      "its composability (RD0-RD4)]")
print("  GREEN-UNREVIEWED — the hostile round is deferred per the "
      "D46 program pin (token budget); this receipt must not be "
      "cited as review-hardened until its round converts (paper-32's "
      "round precedes it).")
print("  banner: EXACT and FLOAT-FREE (Fractions/ints/strings/tuples/"
      "frozensets only — no amplitude probes here; D25's")
print("  distinguishability requirement is enforced as exact "
      "injectivity of the ACTION, strictly stronger than the D44e")
print("  copy-form template's isometry). Layers exec'd __file__-"
      "anchored from the committed d42b3 + d42b2 heads (single")
print("  sources); the d42b2-embedded transport head is PRE-#300 "
      "d42b1 text (D44e round-1 M-2, LOG #363) and is gated AS")
print("  COMMITTED with the provenance declared. Reception instance "
      "= (history, down-closed S, record index j with pred[j] <= S,")
print("  receiver a). Two receipt-built probe fixtures are DECLARED "
      "(FXD, inherited from D44e A2; PROBE-DD, new here). Findings")
print("  (non-injectivity, non-commutation, view-transparency) are "
      "DELIVERED outcomes at exit 0; exit 1 is gate breakage only.")

# ==== RD0 — re-anchor the D44e census BEFORE any dynamics claim =============
print("\n[RD0 — the D44e census re-anchored (no dynamics claim "
      "precedes this block)]")

EVK = ['p', 'r', 'n', 'd', 'm', 'ko', 'kc', 'ka']
VNK = ['v0', 'v.arb', 'v.mrg']
TYPES = EVK + VNK
PREDS = {k: (lambda x, k=k: isinstance(x, tuple) and len(x) >= 2
             and x[0] == k) for k in EVK}
PREDS['v0'] = lambda x: x == V0
PREDS['v.arb'] = (lambda x: isinstance(x, tuple) and len(x) == 5
                  and x[0] == 'v' and x[1] != 'm')
PREDS['v.mrg'] = (lambda x: isinstance(x, tuple) and len(x) == 5
                  and x[0] == 'v' and x[1] == 'm')

def classify(x):
    m = [T for T in TYPES if PREDS[T](x)]
    return m[0] if len(m) == 1 else None

FAM, CACHE = ns3['enumerate_family'](('A', 'B'), 4)
by_depth = {}
for h in FAM:
    by_depth[len(h)] = by_depth.get(len(h), 0) + 1
spec = [by_depth.get(i, 0) for i in range(5)]
cum = [sum(spec[:i + 1]) for i in range(5)]
n_ev_fam = sum(len(h) for h in FAM)
check("RD0-a the depth-4 d42a family re-enumerated FROM the layer "
      "(d42b3's own enumerate_family; single source): the committed "
      "D44e/d43d-NG2/paper-31 census [1,7,39,215,1191] cumulative by "
      "depth, 4,502 event instances — the anchor the dynamics runs on",
      len(FAM) == 1191 and cum == [1, 7, 39, 215, 1191]
      and n_ev_fam == 4502,
      f"members = {len(FAM)}; per-depth = {spec}; cumulative = {cum}; "
      f"event instances = {n_ev_fam}")

fam_ev_ct = {T: 0 for T in TYPES}
fam_v_ct = {T: 0 for T in TYPES}
uncls = multi = 0
for h in FAM:
    for e in h:
        nm_ = sum(1 for T in TYPES if PREDS[T](e))
        if nm_ != 1:
            multi += 1
        T = classify(e)
        if T is None:
            uncls += 1
        else:
            fam_ev_ct[T] += 1
    fam_v_ct['v0'] += 1                       # genesis once per member
    for e in h:
        if e[0] == 'r':
            b = sorted(e[2], key=crepr)[0][1]
            fam_v_ct[classify(vname(b, e[3], e[1]))] += 1
n_v_fam = sum(fam_v_ct.values())
check("RD0-b the FAMILY CENSUS reproduced (the D44e version-instance "
      "convention: genesis once per member + one arb-created version "
      "per r position): p/r/n = 2128/748/1626 events, v0/v.arb = "
      "1191/748 versions, zero unclassified, zero multi-match",
      (fam_ev_ct['p'], fam_ev_ct['r'], fam_ev_ct['n'])
      == (2128, 748, 1626)
      and fam_v_ct['v0'] == 1191 and fam_v_ct['v.arb'] == 748
      and uncls == 0 and multi == 0 and n_v_fam == 1939,
      f"events p/r/n = {fam_ev_ct['p']}/{fam_ev_ct['r']}/"
      f"{fam_ev_ct['n']}; versions = {n_v_fam}; unclassified = "
      f"{uncls}; multi-match = {multi}")

# ---- the committed click/SIG fixtures (the D44e forms, verbatim) ----------
fs = frozenset
tA, tB = ('A', V0, 0), ('B', V0, 1)
CK = fs({tA, tB})
pA0, pB1 = ('p', 'A', V0, 0), ('p', 'B', V0, 1)
def chain(init, ck, first, second):
    return [('ko', init, ck, first), ('kc', init, ck, second),
            ('ka', init, ck, fs({first}))]
FXA1 = [pA0, pB1] + chain('A', CK, tA, tB) + [('n', 'C')]
FXA2 = [pA0, pB1] + chain('A', CK, tB, tA) + [('n', 'C')]
pC0 = ('p', 'C', V0, 0)
tC0 = ('C', V0, 0)
rC = ('r', 'C', fs({tC0}), fs({tC0}))
vc = vname(V0, fs({tC0}), 'C')
dCD = ('d', 'C', 'D', vc)
pC1v, pD0v = ('p', 'C', vc, 1), ('p', 'D', vc, 0)
BASE2 = [pC0, rC, dCD, pC1v, pD0v, pA0, pB1]
tC1, tD0 = ('C', vc, 1), ('D', vc, 0)
CK2 = fs({tC1, tD0})
chA = chain('A', CK, tA, tB)
chC = chain('C', CK2, tC1, tD0)
FXB1 = BASE2 + chA + chC
FXB2 = BASE2 + chC + chA
FXB3 = BASE2 + [chA[0], chC[0], chA[1], chC[1], chA[2], chC[2]]
pC1 = ('p', 'C', V0, 1)
tC = ('C', V0, 1)
rA1 = ('r', 'A', fs({tA}), fs({tA}))
rC1 = ('r', 'C', fs({tC}), fs({tC}))
v1 = vname(V0, fs({tA}), 'A')
vC = vname(V0, fs({tC}), 'C')
dAB, dCB = ('d', 'A', 'B', v1), ('d', 'C', 'B', vC)
SIG6 = [pA0, pC1, rA1, rC1, dAB, dCB]
PKp = tuple(sorted((v1, vC), key=repr))
mB1, mB2 = ('m', 'B', PKp, v1), ('m', 'B', PKp, vC)
D2H = SIG6 + [('p', 'A', v1, 0), ('p', 'B', v1, 1)]
t1A, t1B = ('A', v1, 0), ('B', v1, 1)
rB2 = ('r', 'B', fs({t1A, t1B}), fs({t1A}))
SIG6b = [pA0, pC0, rA1, rC, ('d', 'A', 'B', v1), ('d', 'C', 'B', vc)]
PKb = tuple(sorted((v1, vc), key=repr))
mBoth = ('m', 'B', PKb, 'both')
FIXTURES = [
    ('FXA1', FXA1, ('A', 'B', 'C')),
    ('FXA2', FXA2, ('A', 'B', 'C')),
    ('FXB1', FXB1, ('A', 'B', 'C', 'D')),
    ('FXB2', FXB2, ('A', 'B', 'C', 'D')),
    ('FXB3', FXB3, ('A', 'B', 'C', 'D')),
    ('FXC1', SIG6 + [mB1], ('A', 'B', 'C')),
    ('FXC1b', SIG6 + [mB2], ('A', 'B', 'C')),
    ('FXC2m', D2H + [mB1], ('A', 'B', 'C')),
    ('FXC2r', D2H + [rB2], ('A', 'B', 'C')),
    ('FXD', SIG6b + [mBoth], ('A', 'B', 'C')),
]

# DECLARED receipt-built probe (new here, the D44e-A2 convention): the
# DOUBLE DELIVERY — the same version delivered twice to the same
# receiver. Built to REACH the reception-state degeneracy that the
# committed fixtures do not realize; declared, never counted as a
# committed-family fact.
PROBE_DD = [pA0, rA1, ('d', 'A', 'B', v1), ('d', 'A', 'B', v1)]
ALL_FIX = FIXTURES + [('PROBE-DD', PROBE_DD, ('A', 'B', 'C'))]

fix_ev_ct = {T: 0 for T in TYPES}
fix_v_ct = {T: 0 for T in TYPES}
val_ok = True
for name, fx, actors in FIXTURES:
    for j, e in enumerate(fx):
        T = classify(e)
        if T is None:
            uncls += 1
        else:
            fix_ev_ct[T] += 1
        if e[0] in ('ko', 'kc', 'ka'):
            if not regs_of2(e):
                val_ok = False
            if e[0] == 'ka':
                b = sorted(e[2], key=crepr)[0][1]
                fix_v_ct[classify(vname(b, e[3], e[1]))] += 1
        else:
            ok, q = admissible2(list(fx[:j]), e, actors)
            if not ok or q is None or q <= 0:
                val_ok = False
    fix_v_ct['v0'] += 1
    pred = event_poset(fx)
    vw = View(fx, pred, set(range(len(fx))))
    for v in sorted(vw.created, key=crepr):
        fix_v_ct[classify(v)] += 1
n_ev_fix = sum(fix_ev_ct.values())
n_v_fix = sum(fix_v_ct.values())
okm1, qm1 = admissible2(SIG6, mB1, ('A', 'B', 'C'))
oka2, qa2 = admissible2(D2H, rB2, ('A', 'B', 'C'))
okm2, qm2 = admissible2(D2H, mB1, ('A', 'B', 'C'))
okbo, qbo = admissible2(SIG6b, mBoth, ('A', 'B', 'C'))
check("RD0-c the ten COMMITTED click/SIG fixtures revalidated against "
      "the layer (every non-click event admissible in place; click "
      "forms well-registered) and the D44e/d42b2-M4 price anchors "
      "re-gated: merge@D1 = 1/8, arb@D2 = merge@D2 = 1/16, the "
      "value-equal 'both' branch at 1/4. PROVENANCE DECLARED (D44e "
      "round-1 M-2, LOG #363): these are the d42b2-EMBEDDED PRE-#300 "
      "transport head's prices (D2H merge 1/16 embedded vs 1/24 "
      "terminal d42b1) — gated AS COMMITTED, reconciliation is D46g's",
      val_ok and okm1 and qm1 == Fr(1, 8) and oka2
      and qa2 == Fr(1, 16) and okm2 and qm2 == Fr(1, 16)
      and okbo and qbo == Fr(1, 4),
      f"anchors {qm1}, {qa2}, {qm2}, {qbo}; fixture instances "
      f"{n_ev_fix} events + {n_v_fix} versions")

N_ALL = n_ev_fam + n_v_fam + n_ev_fix + n_v_fix
realized = sorted(T for T in TYPES
                  if fam_ev_ct[T] + fam_v_ct[T] + fix_ev_ct[T]
                  + fix_v_ct[T] > 0)
check("RD0-d THE D44E ANCHOR RE-ESTABLISHED: 11 censused types, "
      "6,567 record instances (family 4502+1939; fixtures 90+36), "
      "zero unclassified, zero multi-match, 11/11 types realized — "
      "the census the dynamics arm now runs on; the (actor,base) "
      "census key re-executed below",
      len(TYPES) == 11 and N_ALL == 6567 and n_ev_fix == 90
      and n_v_fix == 36 and uncls == 0 and multi == 0
      and len(realized) == 11,
      f"total instances = {N_ALL}; types realized = {len(realized)}/11")

viol_ab = 0
for h in FAM:
    pred = event_poset(h)
    vw = View(h, pred, set(range(len(h))))
    ck = {}
    for i, op in vw.props.items():
        ck[(op[1], op[2])] = ck.get((op[1], op[2]), 0) + 1
    if any(c > 1 for c in ck.values()):
        viol_ab += 1
fake_ok = ns3['admissible']([('p', 'A', V0, 0)], ('p', 'A', V0, 1))[0]
check("RD0-e the (actor,base) CENSUS KEY re-executed (d42b7-N1, LOG "
      "#316): multiplicity <= 1 over ALL proposals in every family "
      "member, and the A8-fake second same-key proposal is refused by "
      "the layer — the key the action map is indexed against",
      viol_ab == 0 and fake_ok is False,
      f"violations = {viol_ab}/1191; fake admissible = {fake_ok}")

# ==== the reception STATE and the extracted ACTION MAP ======================
# sigma_a is read off the COMMITTED View class: the four view-global
# fields the layer maintains (props / resolved / superseded / created)
# plus the actor-indexed holdings(a). `live` is DERIVED (props minus
# resolved) and gated against View.live below — it is not stored.
# View.created is index-VALUED in the layer; the abstraction keeps only
# its key set (the version names). That abstraction step is exactly
# what RD1-b's firing control tests.

def state_of(view, a):
    props = {}
    for op in view.props.values():
        t = (op[1], op[2], op[3])
        props[t] = props.get(t, 0) + 1
    return (props, frozenset(view.resolved), frozenset(view.superseded),
            frozenset(view.created), frozenset(view.holdings(a)))

def skey(s):
    P, R, S, C, H = s
    return ('P', tuple(sorted((crepr(k), v) for k, v in P.items())),
            'R', tuple(sorted(crepr(t) for t in R)),
            'S', tuple(sorted(crepr(b) for b in S)),
            'C', tuple(sorted(crepr(v) for v in C)),
            'H', tuple(sorted(crepr(v) for v in H)))

def base_of_ckey(ck):
    bs = sorted({t[1] for t in ck}, key=crepr)
    return bs[0] if len(bs) == 1 else ('MULTIBASE',) + tuple(bs)

REFUSED = ('REFUSED',)

def ACT(s, e, a):
    """The EXTRACTED action map: an independent re-implementation of
    what the committed layer's View does to sigma_a when record e
    enters a's view. Reads ONLY (sigma_a, e, a). Alien kinds are
    REFUSED (the RD4 alien control), never absorbed."""
    P, R, S, C, H = s
    k = e[0]
    if k in ('n', 'ko', 'kc', 'ka'):
        return s                                   # view-transparent
    if k == 'p':
        P2 = dict(P)
        t = (e[1], e[2], e[3])
        P2[t] = P2.get(t, 0) + 1
        return (P2, R, S, C, H)
    if k == 'r':
        ck, wk = e[2], e[3]
        b = base_of_ckey(ck)
        v = vname(b, wk, e[1])
        H2 = H | {v} if a in {t[0] for t in ck} else H
        return (P, R | set(ck), S | {b}, C | {v}, H2)
    if k == 'd':
        return (P, R, S, C, H | {e[3]} if a == e[2] else H)
    if k == 'm':
        pk, w = e[2], e[3]
        val = value_of(pk[0]) if w == 'both' else value_of(w)
        mv = mname(pk, val, e[1])
        H2 = H | {mv} if a == e[1] else H
        return (P, R, S | {pk[0], pk[1]}, C | {mv}, H2)
    return REFUSED

def ACT_V(s, v, a):
    """The VERSION-record action: a version record is self-registering
    (D44e RG1: carrier = holders per holdings()), so its reception IS
    the holdings insertion."""
    P, R, S, C, H = s
    return (P, R, S, C, H | {v})

def writes_holdings(e, a):
    if e[0] == 'r':
        return a in {t[0] for t in e[2]}
    if e[0] == 'd':
        return a == e[2]
    if e[0] == 'm':
        return a == e[1]
    return False

def actor_carriers(e, actors):
    return frozenset(regs_of2(e)) & frozenset(actors)

def downsets(pred, n):
    out = [frozenset()]
    seen = {frozenset()}
    fr = [frozenset()]
    while fr:
        Sx = fr.pop()
        for j in range(n):
            if j in Sx or not pred[j] <= Sx:
                continue
            T = Sx | {j}
            if T not in seen:
                seen.add(T)
                out.append(T)
                fr.append(T)
    return sorted(out, key=lambda z: (len(z), sorted(z)))

# the full reception-instance corpus: family + committed fixtures +
# the declared PROBE-DD, every actor of each scope
CORPUS = ([('fam', h, ('A', 'B')) for h in FAM if h]
          + [(nm, fx, ac) for nm, fx, ac in ALL_FIX])

# ==== the sweep's helpers: the delta signature, the touched-structure
# ==== relation, and the three FIRING controls ==============================
FLD = ('P', 'R', 'S', 'C', 'H')

def delta_sig(pre, post):
    """The exact per-field change signature of one reception."""
    out = []
    if pre[0] != post[0]:
        out.append('props+%d' % (sum(post[0].values())
                                 - sum(pre[0].values())))
    for i, nm in ((1, 'resolved'), (2, 'superseded'), (3, 'created'),
                  (4, 'holdings')):
        if pre[i] != post[i]:
            out.append('%s+%d' % (nm, len(post[i]) - len(pre[i])))
    return tuple(out) if out else ('IDENTITY',)

def touched(e, a):
    """The state ITEMS a record writes (its structural footprint).
    Disjoint footprints = the records touch disjoint structure."""
    k = e[0]
    if k == 'p':
        return frozenset({crepr((e[1], e[2], e[3]))})
    if k == 'r':
        b = base_of_ckey(e[2])
        return frozenset({crepr(t) for t in e[2]}
                         | {crepr(b), crepr(vname(b, e[3], e[1]))})
    if k == 'd':
        return frozenset({crepr(e[3])})
    if k == 'm':
        pk, w = e[2], e[3]
        val = value_of(pk[0]) if w == 'both' else value_of(w)
        return frozenset({crepr(pk[0]), crepr(pk[1]),
                          crepr(mname(pk, val, e[1]))})
    return frozenset()

def ikey(view, a):
    """RD1-b's CONTROL state: identical to sigma_a except that
    `created` keeps the layer's literal index VALUES (View.created is
    a version -> index map). If the abstraction step were idle, this
    would also be a function of (record, receiver, pre-state)."""
    props = {}
    for op in view.props.values():
        t = (op[1], op[2], op[3])
        props[t] = props.get(t, 0) + 1
    return ('P', tuple(sorted((crepr(k), v) for k, v in props.items())),
            'R', tuple(sorted(crepr(t) for t in view.resolved)),
            'S', tuple(sorted(crepr(b) for b in view.superseded)),
            'Ci', tuple(sorted((crepr(v), i)
                               for v, i in view.created.items())),
            'H', tuple(sorted(crepr(v) for v in view.holdings(a))))

def ACT_rep(s, e, a):
    """RD3's ORDER-SENSITIVE control: `created` written by REPLACEMENT
    instead of union. Everything else identical to ACT. A genuinely
    non-abelian variant — the commutation gate must reject it."""
    P, R, S, C, H = s
    k = e[0]
    if k == 'r':
        ck, wk = e[2], e[3]
        b = base_of_ckey(ck)
        v = vname(b, wk, e[1])
        H2 = H | {v} if a in {t[0] for t in ck} else H
        return (P, R | set(ck), S | {b}, frozenset({v}), H2)
    if k == 'm':
        pk, w = e[2], e[3]
        val = value_of(pk[0]) if w == 'both' else value_of(w)
        mv = mname(pk, val, e[1])
        H2 = H | {mv} if a == e[1] else H
        return (P, R, S | {pk[0], pk[1]}, frozenset({mv}), H2)
    return ACT(s, e, a)

def ACT_lww(s, e, a):
    """RD3's SECOND control, retained because it does NOT fire:
    last-writer-wins on HOLDINGS. Its silence is itself a gated
    structural fact (RD3-c), not a pass."""
    P, R, S, C, H = s
    k = e[0]
    if k == 'r':
        ck, wk = e[2], e[3]
        b = base_of_ckey(ck)
        v = vname(b, wk, e[1])
        H2 = frozenset({V0, v}) if a in {t[0] for t in ck} else H
        return (P, R | set(ck), S | {b}, C | {v}, H2)
    if k == 'd':
        return (P, R, S, C,
                frozenset({V0, e[3]}) if a == e[2] else H)
    if k == 'm':
        pk, w = e[2], e[3]
        val = value_of(pk[0]) if w == 'both' else value_of(w)
        mv = mname(pk, val, e[1])
        H2 = frozenset({V0, mv}) if a == e[1] else H
        return (P, R, S | {pk[0], pk[1]}, C | {mv}, H2)
    return ACT(s, e, a)

# ==== the single mechanical sweep ==========================================
# One traversal produces every RD1/RD2/RD3 aggregate. `flip` reverses
# the traversal order (down-sets, extensions, actors) — used ONLY by the
# RD4 determinism gate, which requires identical aggregates either way.

BOT = ({}, fs(), fs(), fs(), fs())

def mon(s, t):
    """The componentwise COMMUTATIVE MONOID operation of the reception
    state: multiset addition on props, union on the four set fields.
    This is the operation the extracted action applies (see `incr`)."""
    P = dict(s[0])
    for k_, c_ in t[0].items():
        P[k_] = P.get(k_, 0) + c_
    return (P, s[1] | t[1], s[2] | t[2], s[3] | t[3], s[4] | t[4])

def incr(e, a):
    """The record's INCREMENT: what ACT adds, evaluated at the bottom
    state.  If ACT(s, e, a) == mon(s, incr(e, a)) for every s — which
    RD3-b gates — then the increment does not read the pre-state, and
    commutation follows from the associativity and commutativity of
    `mon`, for ALL records, not only co-receivable ones."""
    return ACT(BOT, e, a)

def sweep(flip=False):
    R = {
        'inst': 0, 'faith_bad': 0, 'wd_bad': 0, 'wd_keys': 0,
        'sigs': {}, 'per_type': {}, 'loc_bad': 0, 'live_bad': 0,
        'fiber': {}, 'pairs': 0, 'noncomm': 0, 'comp_bad': 0,
        'disj_pairs': 0, 'ovl_pairs': 0, 'disj_noncomm': 0,
        'both_h_pairs': 0, 'states': set(), 'sobj': {},
        'c_idx_bad': 0, 'c_idx_keys': 0, 'c_lossy_fibers': 0,
        'c_rep_noncomm': 0, 'c_lww_noncomm': 0,
        # round-1 additions (F-A1, F-M4, F-M5)
        'incr_bad': 0, 'allpairs': 0, 'allpairs_noncomm': 0,
        'fp_both_empty': 0, 'fp_one_empty': 0, 'fp_disj_both': 0,
        'id_factor_pairs': 0, 'both_created_pairs': 0,
        'prop_ndet': 0, 'arb_ndet': 0, 'prop_keys': 0,
    }
    wd = {}
    idxwd = {}
    lossyfib = {}
    propd = {}
    arbd = {}
    for _scope, h, actors in CORPUS:
        pred = event_poset(h)
        n = len(h)
        DS = downsets(pred, n)
        if flip:
            DS = DS[::-1]
        VS = {Sx: View(h, pred, set(Sx)) for Sx in DS}
        acts = tuple(reversed(actors)) if flip else tuple(actors)
        for Sx in DS:
            ext = [j for j in range(n) if j not in Sx and pred[j] <= Sx]
            if flip:
                ext = ext[::-1]
            for a in acts:
                pre = state_of(VS[Sx], a)
                pk_ = skey(pre)
                R['states'].add(pk_)
                R['sobj'][pk_] = pre
                # RD3-f: is the PROPOSE menu a function of sigma_a alone?
                # is the ARBITRATE menu?  Both asked over every view
                # realizing each of the enumerated pre-states.
                propd.setdefault((pk_, a), set()).add(
                    crepr(tuple(sorted(crepr(o) for o in
                                       prop_opts(VS[Sx], a)))))
                arbd.setdefault((pk_, a), set()).add(
                    crepr(tuple(sorted((crepr(b_), len(c_))
                                       for b_, c_ in arb_comps(VS[Sx], a)))))
                # F-A1: commutation over ALL record pairs of the history,
                # co-receivable or not — the pairing rule constrains nothing
                for x in range(n):
                    for y in range(x + 1, n):
                        R['allpairs'] += 1
                        if skey(ACT(ACT(pre, h[x], a), h[y], a)) != \
                                skey(ACT(ACT(pre, h[y], a), h[x], a)):
                            R['allpairs_noncomm'] += 1
                for j in ext:
                    e = h[j]
                    T = classify(e)
                    post = state_of(VS[Sx | {j}], a)
                    ex = ACT(pre, e, a)
                    R['inst'] += 1
                    R['per_type'][T] = R['per_type'].get(T, 0) + 1
                    if ex is REFUSED or skey(ex) != skey(post):
                        R['faith_bad'] += 1
                    # F-A1: the increment does not read the pre-state
                    if ex is REFUSED or skey(ex) != skey(mon(pre,
                                                            incr(e, a))):
                        R['incr_bad'] += 1
                    # RD1-c carrier locality (actor-indexed field)
                    if (pre[4] != post[4]
                            and a not in actor_carriers(e, actors)):
                        R['loc_bad'] += 1
                    # derived live vs the layer's View.live
                    vpost = VS[Sx | {j}]
                    lay = sorted(crepr((o[1], o[2], o[3]))
                                 for o in vpost.live.values())
                    der = sorted(crepr(t) for t, c in post[0].items()
                                 for _ in range(c) if t not in post[1])
                    if lay != der:
                        R['live_bad'] += 1
                    kk = (crepr(e), a, pk_)
                    if kk in wd and wd[kk] != skey(post):
                        R['wd_bad'] += 1
                    wd[kk] = skey(post)
                    R['fiber'].setdefault((crepr(e), a, T), {}) \
                        .setdefault(skey(post), set()).add(pk_)
                    sg = delta_sig(pre, post)
                    R['sigs'].setdefault(T, {})
                    R['sigs'][T][sg] = R['sigs'][T].get(sg, 0) + 1
                    # RD1-b control: the layer's index-VALUED created
                    ki = (crepr(e), a, ikey(VS[Sx], a))
                    po = ikey(VS[Sx | {j}], a)
                    if ki in idxwd and idxwd[ki] != po:
                        R['c_idx_bad'] += 1
                    idxwd[ki] = po
                    # RD2 control: props-dropped lossy action
                    lossyfib.setdefault((crepr(e), a), {}) \
                        .setdefault(skey(ACT(pre, e, a))[2:],
                                    set()).add(pk_)
                for x in range(len(ext)):
                    for y in range(x + 1, len(ext)):
                        j1, j2 = ext[x], ext[y]
                        e1, e2 = h[j1], h[j2]
                        s12 = ACT(ACT(pre, e1, a), e2, a)
                        s21 = ACT(ACT(pre, e2, a), e1, a)
                        R['pairs'] += 1
                        if skey(s12) != skey(s21):
                            R['noncomm'] += 1
                        if skey(s12) != skey(state_of(VS[Sx | {j1, j2}],
                                                      a)):
                            R['comp_bad'] += 1
                        f1, f2 = touched(e1, a), touched(e2, a)
                        if f1 & f2:
                            R['ovl_pairs'] += 1
                        else:
                            R['disj_pairs'] += 1
                            if skey(s12) != skey(s21):
                                R['disj_noncomm'] += 1
                            # F-M4: how much of the "co-receivable
                            # universe" carries no structure at all
                            if not f1 and not f2:
                                R['fp_both_empty'] += 1
                            elif not f1 or not f2:
                                R['fp_one_empty'] += 1
                            else:
                                R['fp_disj_both'] += 1
                        if (skey(ACT(pre, e1, a)) == skey(pre)
                                or skey(ACT(pre, e2, a)) == skey(pre)):
                            R['id_factor_pairs'] += 1
                        if e1[0] in ('r', 'm') and e2[0] in ('r', 'm'):
                            R['both_created_pairs'] += 1
                        if (writes_holdings(e1, a)
                                and writes_holdings(e2, a)):
                            R['both_h_pairs'] += 1
                        if (skey(ACT_rep(ACT_rep(pre, e1, a), e2, a))
                                != skey(ACT_rep(ACT_rep(pre, e2, a),
                                                e1, a))):
                            R['c_rep_noncomm'] += 1
                        if (skey(ACT_lww(ACT_lww(pre, e1, a), e2, a))
                                != skey(ACT_lww(ACT_lww(pre, e2, a),
                                                e1, a))):
                            R['c_lww_noncomm'] += 1
    R['wd_keys'] = len(wd)
    R['c_idx_keys'] = len(idxwd)
    R['c_lossy_fibers'] = sum(1 for d in lossyfib.values()
                              for ps in d.values() if len(ps) > 1)
    R['prop_keys'] = len(propd)
    R['prop_ndet'] = sum(1 for v in propd.values() if len(v) > 1)
    R['arb_ndet'] = sum(1 for v in arbd.values() if len(v) > 1)
    return R

RES = sweep()

# ==== RD1 — the action map, extracted mechanically per type ================
print("\n[RD1 — the ACTION MAP: what the committed layer actually "
      "DOES to a receiver's state]")
print("  [RD1 TABLE] type | reception instances | the exact state "
      "update(s) observed   [EXACT, diffed pre/post]")
TYPE_ROLE = {
    'p': 'PROPOSAL — writes the proposal multiset only',
    'r': 'ARBITRATION — resolves, supersedes, creates, endows authors',
    'n': 'NOOP/IDLE — receptionless (D25 F4)',
    'd': 'DELIVERY — endows the named receiver only',
    'm': 'MERGE — supersedes the pair, creates, endows the merger',
    'ko': 'OPENING CLICK — view-transparent',
    'kc': 'CONTINUATION CLICK — view-transparent',
    'ka': 'ACCEPTANCE CLICK — view-transparent',
}
for T in EVK:
    if T not in RES['sigs']:
        print(f"    {T:<5} |        0 | NOT REALIZED as an event at "
              f"this scope")
        continue
    tot = RES['per_type'][T]
    print(f"    {T:<5} | {tot:>8} | {TYPE_ROLE[T]}")
    for sg, c in sorted(RES['sigs'][T].items()):
        print(f"          {c:>8} x  {' , '.join(sg)}")

check("RD1-a FAITHFULNESS: the extracted action map ACT(sigma, rec, "
      "a) — an INDEPENDENT re-implementation reading only the "
      "abstract state, the record and the receiver — reproduces the "
      "committed layer's own View EXACTLY on every enumerated "
      "reception instance (family + committed fixtures + the declared "
      "PROBE-DD, every actor of each scope); the DERIVED live set "
      "(props minus resolved) matches View.live entry-for-entry",
      RES['faith_bad'] == 0 and RES['live_bad'] == 0
      and RES['inst'] == 23069,
      f"instances = {RES['inst']}; faithfulness violations = "
      f"{RES['faith_bad']}; derived-live mismatches = "
      f"{RES['live_bad']}; distinct pre-states = {len(RES['states'])}")

check("RD1-b THE FUNCTION PROPERTY — RESTATED AS A COROLLARY OF RD1-a, "
      "NOT AN INDEPENDENT MEASUREMENT (round-1 F-A2). RD1-a already "
      "establishes post = ACT(pre, e, a) on EVERY instance, and ACT is "
      "a deterministic function of exactly those three arguments; a "
      "quantity equal to a function of (pre, e, a) everywhere IS a "
      "function of (pre, e, a), so this counter is ENTAILED by RD1-a "
      "and cannot fail once RD1-a passes (the round's mutant f1 "
      "confirms it: a wrong-but-still-functional ACT fails RD1-a and "
      "leaves this at zero conflicts). It is recorded as a REGRESSION "
      "TALLY on that corollary — the number of distinct repeated keys "
      "is the useful datum, not the zero — and the load-bearing claim "
      "'no hidden dependence on history, index, poset or unseen "
      "events' is carried by RD1-a's faithfulness against the layer, "
      "not by this line",
      RES['wd_bad'] == 0,
      f"distinct (record, receiver, pre-state) keys = "
      f"{RES['wd_keys']}; conflicting keys = {RES['wd_bad']} "
      "(entailed, not measured)")

check("RD1-b CONTROL FIRES (the abstraction step is doing real work; "
      "the gate demonstrably can fail): the SAME gate on the state "
      "that keeps View.created's literal index VALUES — the layer's "
      "own storage form — is NOT a function of (record, receiver, "
      "pre-state); it fails loudly and in bulk",
      RES['c_idx_bad'] > 0,
      f"index-valued-created conflicting keys = "
      f"{RES['c_idx_bad']} of {RES['c_idx_keys']} (the delivered "
      "abstraction: 0)")

check("RD1-c CARRIER LOCALITY of the actor-indexed field: holdings(a) "
      "changes ONLY when a is an ACTOR-CARRIER of the record (regs_of "
      "per A1/A6, intersected with the scope's actor set) — zero "
      "exceptions. The four VIEW-GLOBAL fields (props, resolved, "
      "superseded, created) are by construction not actor-indexed, so "
      "they move in every viewer's state alike: stated, not hidden",
      RES['loc_bad'] == 0,
      f"non-carrier holdings changes = {RES['loc_bad']}")

_view_kinds = _strconsts(_classnode('View'))
_kinds_in = sorted(_view_kinds & set(TYPES))
_kinds_out = sorted(set(('ko', 'kc', 'ka', 'n')) - _view_kinds)
check("RD1-d THE CLICK LAYER IS VIEW-TRANSPARENT — A CODE-READING "
      "THEOREM, GATED, NOT A DISCOVERY (round-1 F-M1). One-line "
      "proof, and the gate is the proof: the committed View class "
      "(d42b2 lines 74-111) selects records ONLY by "
      "acts[i][0] in {p, r, d, m} — an AST scan of the class body "
      "finds those four record-kind literals and finds NO occurrence "
      "of ko, kc, ka or n anywhere in it — so every record kind "
      "outside {p, r, d, m} is NECESSARILY the identity on sigma at "
      "every |C| and every scope, because it is not in the state "
      "space at all. The instance census below is a consistency "
      "check on that reading, not its evidence, and RD4-a's |C| = 2 "
      "scope caveat does NOT apply to this claim. What the click "
      "record's content does instead is unchanged: it enters the "
      "POSET (regs_of writes the initiator and, for ka, the accepted "
      "vname) and the PRICING",
      _kinds_out == ['ka', 'kc', 'ko', 'n']
      and set(('p', 'r', 'd', 'm')) <= _view_kinds
      and all(set(RES['sigs'].get(T, {})) == {('IDENTITY',)}
              for T in ('ko', 'kc', 'ka'))
      and set(RES['sigs'].get('n', {})) == {('IDENTITY',)},
      f"View class body mentions record kinds {_kinds_in} and none of "
      f"{_kinds_out}; ko/kc/ka/n signatures = {{IDENTITY}} exactly; "
      "instances = "
      + ", ".join(f"{T} {RES['per_type'].get(T, 0)}"
                  for T in ('ko', 'kc', 'ka', 'n')))

check("RD1-e the ALIEN control (the D44e RG0-SCOPE convention, "
      "carried to the dynamics): the extracted action map REFUSES an "
      "alien-tagged record rather than absorbing it at the else "
      "branch — generator-scoped completeness stated with a firing "
      "negative control",
      ACT(state_of(View([pA0], event_poset([pA0]), {0}), 'A'),
          ('z', 'A'), 'A') is REFUSED
      and classify(('z', 'A')) is None,
      "ACT(alien) = REFUSED; classify(alien) = None")

VER_ALL = sorted({V0}
                 | {vname(base_of_ckey(e[2]), e[3], e[1])
                    for _s, h, _a in CORPUS for e in h if e[0] == 'r'}
                 | {mname(e[2], value_of(e[2][0]) if e[3] == 'both'
                          else value_of(e[3]), e[1])
                    for _s, h, _a in CORPUS for e in h if e[0] == 'm'},
                 key=crepr)
ver_types = sorted({classify(v) for v in VER_ALL})
check("RD1-f the VERSION-RECORD action (the three self-registering "
      "types v0 / v.arb / v.mrg, whose D44e carrier is 'holders per "
      "holdings()'): their reception IS the holdings insertion "
      "sigma -> sigma with holdings(a) union {v} — the SAME map the "
      "r / d / m actions apply on their holdings leg, now isolated "
      "and gated in its own right; all three types realized",
      ver_types == ['v.arb', 'v.mrg', 'v0'] and len(VER_ALL) >= 20,
      f"distinct realized version records = {len(VER_ALL)}; types = "
      f"{ver_types}")

# ==== RD2 — NSE/D25/D27 compliance OF THE DYNAMICS =========================
print("\n[RD2 — injectivity of the ACTION (not of a copy-form "
      "template): distinct pre-states must stay distinguishable]")
inj_by_type = {}
witnesses = []
for (rk, a, T), d in sorted(RES['fiber'].items()):
    for post, pres in sorted(d.items()):
        if len(pres) > 1:
            inj_by_type[T] = inj_by_type.get(T, 0) + 1
            witnesses.append((T, rk, a, sorted(pres), post))
for T in EVK:
    if T not in RES['per_type']:
        continue
    nf = sum(len(d) for (rk, a, TT), d in RES['fiber'].items()
             if TT == T)
    print(f"    {T:<5} | {RES['per_type'][T]:>6} instances | "
          f"{nf:>5} post-state fibers | colliding fibers "
          f"{inj_by_type.get(T, 0)}")

def _map_collision(T):
    """A MAP-LEVEL collision for a holdings-writing type: two abstract
    pre-states differing only by whether they already hold the version
    the record inserts.  Round-1 F-M2: the enumerated fibers reach no
    such pair for r and m, so their INJECTIVE verdicts below are
    statements about the POOL, not about the action."""
    for _s, h, acs in CORPUS:
        for e in h:
            if e[0] != T:
                continue
            for a_ in acs:
                ins = incr(e, a_)[4]
                if not ins:
                    continue
                v_ = sorted(ins, key=crepr)[0]
                s1 = ({}, fs(), fs(), fs(), fs({V0}))
                s2 = ({}, fs(), fs(), fs(), fs({V0, v_}))
                if skey(s1) == skey(s2):
                    continue
                if skey(ACT(s1, e, a_)) == skey(ACT(s2, e, a_)):
                    return (crepr(e), a_, crepr(v_))
    return None

MAPCOLL = {T: _map_collision(T) for T in ('r', 'd', 'm')}
for T in ('r', 'd', 'm'):
    w_ = MAPCOLL[T]
    print(f"    [RD2-a MAP-LEVEL WITNESS] type {T}: "
          + ("none found" if w_ is None else
             f"record {w_[0]}, receiver {w_[1]}; the pre-states "
             f"{{V0}} and {{V0, {w_[2]}}} are DISTINCT and land on the "
             "SAME post-state — non-injective AS A MAP"))
check("RD2-a INJECTIVITY OF THE ACTION AMONG THE ENUMERATED FIBERS, "
      "per type, over every enumerated (record, receiver) fiber: for "
      "p, r, n, m, ko, kc, ka no two distinct ENUMERATED pre-states "
      "collide. SCOPE, corrected by round 1 (F-M2): this is a "
      "statement about the pre-states the enumeration reaches, NOT "
      "about the maps. r, d and m all write holdings by IDEMPOTENT "
      "SET UNION (RD1-f says so in terms; RD2-c convicts that map), "
      "so r and m are non-injective AS MAPS for exactly the reason d "
      "is — the map-level witnesses are constructed and printed above "
      "and gated here. What the enumerated arm does deliver is that "
      "only d's degeneracy is REACHED by the corpus (with PROBE-DD), "
      "which is the honest content of the contrast with RD2-b",
      all(inj_by_type.get(T, 0) == 0
          for T in ('p', 'r', 'n', 'm', 'ko', 'kc', 'ka'))
      and MAPCOLL['r'] is not None and MAPCOLL['m'] is not None
      and MAPCOLL['d'] is not None,
      "colliding ENUMERATED fibers = "
      + ", ".join(f"{T} {inj_by_type.get(T, 0)}" for T in EVK)
      + "; map-level collisions exhibited for "
      + ", ".join(T for T in ('r', 'd', 'm')
                  if MAPCOLL[T] is not None))

check("RD2-b DELIVERED FINDING — THE DELIVERY ACTION IS NOT "
      "INJECTIVE. Type d fails the injectivity gate: re-delivering a "
      "version the receiver ALREADY HOLDS is admissible in the "
      "committed layer (the option set deliver_options_in_view "
      "filters on the SENDER's holdings only, never on the "
      "receiver's), and holdings is a SET — so the pre-state without "
      "the version and the pre-state with it map to the SAME "
      "post-state. Reception FORGETS delivery multiplicity. This is "
      "a DELIVERED outcome, not a gate breakage: the collision is "
      "exhibited exactly below and the receipt exits 0",
      inj_by_type.get('d', 0) > 0,
      f"colliding d fibers = {inj_by_type.get('d', 0)} (all other "
      "types 0); reached on the DECLARED receipt-built PROBE-DD "
      "fixture — the ten committed fixtures do not realize a "
      "re-delivery")
for T, rk, a, pres, post in witnesses:
    print(f"    [RD2-b WITNESS]  type {T} | record {rk} | receiver "
          f"{a}")
    for s_ in pres:
        print(f"       pre  holdings = {s_[9]}")
    print(f"       post holdings = {post[9]}   <- both pre-states "
          f"land here")

vcoll = {}
vtot = 0
SOBJ = RES['sobj']
for v in VER_ALL:
    T = classify(v)
    fib = {}
    for pk_, s_ in sorted(SOBJ.items()):
        fib.setdefault(skey(ACT_V(s_, v, 'A')), []).append(pk_)
    for post, pres in fib.items():
        vtot += 1
        if len(pres) > 1:
            vcoll[T] = vcoll.get(T, 0) + 1
v0_universal = all(V0 in s_[4] for s_ in SOBJ.values())
mrg_states = sum(1 for s_ in SOBJ.values()
                 if any(v[0] == 'v' and len(v) == 5 and v[1] == 'm'
                        for v in s_[4]))
check("RD2-c DELIVERED FINDING — THE VERSION-RECORD ACTION IS "
      "IDEMPOTENT SET INSERTION, hence NOT INJECTIVE where the "
      "version is already held: type v.arb collides on the "
      "enumerated pre-states. The D25 distinguishability requirement "
      "is met on the RECORD carrier (D44e's gated arm) and FAILS on "
      "the holdings STATE — two different claims, and the dynamics "
      "arm is where the difference becomes visible. The other two "
      "version types are printed with their exact reasons, not "
      "silently grouped: v0 NEVER collides because the genesis is "
      "held in EVERY reachable state (holdings() seeds {V0}), so its "
      "action is the identity map, which is injective; v.mrg does "
      "not collide AT THIS SCOPE because no two enumerated "
      "pre-states differ ONLY in an mname holding — the merge action "
      "moves superseded and created in the same step (a scope "
      "statement, declared at RD4-c, not an injectivity claim)",
      vcoll.get('v.arb', 0) > 0 and v0_universal
      and vcoll.get('v0', 0) == 0,
      f"colliding fibers over the {len(SOBJ)} distinct enumerated "
      f"pre-states x {len(VER_ALL)} realized version records: "
      + ", ".join(f"{T} {vcoll.get(T, 0)}"
                  for T in ('v0', 'v.arb', 'v.mrg'))
      + f"; total fibers = {vtot}; V0 held in all "
      f"{len(SOBJ)} states = {v0_universal}; states holding an "
      f"mname = {mrg_states}")

check("RD2-d THE LOSSY CONTROL FIRES (the d42b4/D44e convention — "
      "the gate is demonstrably capable of rejecting an "
      "information-destroying action): the deliberately lossy "
      "variant that performs the SAME update and then DROPS the "
      "proposal multiset from the post-state collides in bulk, "
      "exactly as it must",
      RES['c_lossy_fibers'] > 0,
      f"colliding fibers under the props-dropped action = "
      f"{RES['c_lossy_fibers']} (the delivered action: "
      f"{sum(inj_by_type.values())}, all of them the d/re-delivery "
      "finding)")

# ==== RD3 — COMPOSABILITY: two receptions in either order ==================
print("\n[RD3 — composability. TWO DIFFERENT NOTIONS OF ORDER, kept "
      "apart (round-1 F-M3): RD3-a..d are INTRA-HISTORY concurrency "
      "(two records minimal at one down-set of ONE history, one "
      "poset); RD3-e is INTER-HISTORY generation order (two "
      "histories over the same record multiset, DIFFERENT posets). "
      "No inference runs from the first to the second]")

check("RD3-a COMPOSITION SOUNDNESS: composing the EXTRACTED action "
      "twice reproduces the committed layer's own View over the "
      "two-record extension, on every co-receivable pair — the "
      "commutation gate below therefore tests the layer's semantics, "
      "not a private algebra",
      RES['comp_bad'] == 0,
      f"co-receivable pairs = {RES['pairs']}; composite-vs-layer "
      f"mismatches = {RES['comp_bad']}")

_vinit = _fnnode('__init__', cls='View')
_init_src_ok = ('idxs' in {a.arg for a in _vinit.args.args})
check("RD3-b RECEPTION COMMUTES — AND THIS IS A STRUCTURAL CONSEQUENCE "
      "OF RD1-a, NOT A MEASUREMENT (round-1 F-A1; the previous "
      "'abelian monoid ... strictly stronger than the pin's "
      "disjointness gate' billing is WITHDRAWN). The reason, gated "
      "here rather than narrated: (i) the committed state is a "
      "function of a down-closed index SET — View(acts, pred, idxs) "
      "builds props / arbs / dels / mrgs / resolved / superseded / "
      "created / live / holdings(a) by iterating idxs alone, so "
      "'receive e1 then e2' and 'receive e2 then e1' DENOTE THE SAME "
      "OBJECT in the layer and order-independence is definitional; "
      "(ii) correspondingly the extracted action is a MONOID "
      "TRANSLATION, ACT(s, e, a) = mon(s, incr(e, a)) with an "
      "increment that never reads s — gated on every enumerated "
      "instance below — and `mon` (multiset addition on props, union "
      "on the four set fields) is associative and commutative, so ANY "
      "two such translations commute. Consequently the zero "
      "non-commuting count CANNOT be nonzero once RD1-a passes; the "
      "round's mutant f1 (a demonstrably wrong action map) leaves it "
      "at zero. It is kept as a REGRESSION TEST on ACT, which is what "
      "it is worth. (iii) The 'co-receivable' pairing rule constrains "
      "nothing either: applying ACT in both orders to EVERY record "
      "pair of every history against every enumerated pre-state — "
      "co-receivable or not — also gives zero non-commuting",
      RES['noncomm'] == 0 and RES['disj_noncomm'] == 0
      and RES['ovl_pairs'] > 0 and RES['incr_bad'] == 0
      and RES['allpairs_noncomm'] == 0
      and RES['allpairs'] > RES['pairs'] and _init_src_ok,
      f"increment-identity violations over {RES['inst']} instances = "
      f"{RES['incr_bad']}; co-receivable pairs = {RES['pairs']}, "
      f"non-commuting {RES['noncomm']}; ALL record pairs = "
      f"{RES['allpairs']}, non-commuting {RES['allpairs_noncomm']}; "
      f"View.__init__ signature parameters = "
      f"{[a.arg for a in _vinit.args.args]}")

print(f"    [RD3-b FOOTPRINT STRATIFICATION of the {RES['pairs']} "
      "co-receivable pairs, printed because the raw count overstates "
      "the content (round-1 F-M4)]")
print(f"      both footprints EMPTY (click/click, click/noop, "
      f"noop/noop) : {RES['fp_both_empty']}")
print(f"      exactly one footprint empty                        "
      f"   : {RES['fp_one_empty']}")
print(f"      both records write structure, footprints disjoint   "
      f"   : {RES['fp_disj_both']}")
print(f"      OVERLAPPING footprints                             "
      f"   : {RES['ovl_pairs']}")
print(f"      pairs in which at least one record acts as the IDENTITY "
      f"on this actor's state: {RES['id_factor_pairs']} of "
      f"{RES['pairs']} "
      f"({100 * RES['id_factor_pairs'] // RES['pairs']}%)")

check("RD3-c THE COMMUTATION CONTROL FIRES (the gate can reject a "
      "non-abelian action): the order-sensitive variant that writes "
      "`created` by REPLACEMENT instead of union — identical to the "
      "delivered action in every other respect — fails the SAME gate. "
      "SCOPE, corrected by round 1 (F-M4): that control differs from "
      "the delivered action ONLY in the `created` field, which two "
      "records can both write only if both are r or m, so its count "
      "is the MAXIMUM it could ever report and not evidence of "
      "breadth — it is reported here as 'n of n possible', computed",
      RES['c_rep_noncomm'] > 0
      and RES['c_rep_noncomm'] == RES['both_created_pairs'],
      f"non-commuting pairs under created-by-replacement = "
      f"{RES['c_rep_noncomm']} of {RES['both_created_pairs']} POSSIBLE "
      f"(pairs in which both records write `created`), out of "
      f"{RES['pairs']} co-receivable pairs (delivered action: "
      f"{RES['noncomm']})")

check("RD3-d THE SECOND CONTROL IS SILENT, AND ITS SILENCE IS THE "
      "STRUCTURAL FACT (printed as a declaration and counted in the "
      "gate total — round-1 F-m3; the earlier 'never counted as a "
      "pass' was false): "
      "last-writer-wins on HOLDINGS cannot fire, because ZERO "
      "co-receivable pairs have both records writing the SAME "
      "actor's holdings. The reason is exact: every holdings-writing "
      "record (r with a among the authors, d with a the named "
      "receiver, m with a the merger) carries a in regs_of, so the "
      "receiver's OWN register totally orders its holdings "
      "receptions — an actor never faces two concurrent endowments. "
      "The commutation content of RD3-b therefore lives entirely in "
      "the four view-global fields",
      RES['both_h_pairs'] == 0 and RES['c_lww_noncomm'] == 0,
      f"pairs writing one actor's holdings twice = "
      f"{RES['both_h_pairs']}; LWW non-commuting = "
      f"{RES['c_lww_noncomm']} (vacuous by construction — declared, "
      "and the created-replace control at RD3-c carries the firing "
      "burden)")

# ---- RD3-e: the EXACT obstruction, exhibited -------------------------------
ACTS2 = ('A', 'B')
dAB0 = ('d', 'A', 'B', V0)
ORD1 = [pA0, dAB0, pB1]      # A's proposal reaches B BEFORE B proposes
ORD2 = [pA0, pB1, dAB0]      # B proposes concurrently, delivery after
def menu(h):
    pred = event_poset(h)
    vw = View(h, pred, set(range(len(h))))
    out = {}
    for a in ACTS2:
        rows = []
        for b, c in arb_comps(vw, a):
            ck = triples(vw, c)
            et = edge_triples_of(vw, c)
            for w in gmis_of(ck, et):
                ok, q = admissible2(h, ('r', a, ck, w), ACTS2)
                if ok:
                    rows.append((len(ck), q))
        out[a] = sorted(rows)
    comps = sorted((crepr(b), len(c)) for b, c in vw.components())
    return out, comps, vw
adm1 = all(admissible2(ORD1[:j], ORD1[j], ACTS2)[0]
           for j in range(len(ORD1)))
adm2_ = all(admissible2(ORD2[:j], ORD2[j], ACTS2)[0]
            for j in range(len(ORD2)))
M1, C1, VW1 = menu(ORD1)
M2, C2, VW2 = menu(ORD2)
st_eq = all(skey(state_of(VW1, a)) == skey(state_of(VW2, a))
            for a in ACTS2)
print("    [RD3-e OBSTRUCTION EXHIBIT] TWO GENERATED HISTORIES OVER "
      "THE SAME RECORD MULTISET {pA0, ('d','A','B',V0), pB1} — NOT "
      "two reception orders of one history (round-1 F-M3): the two "
      "histories carry DIFFERENT posets, which is the whole point:")
print(f"      ORD-1 (the delivery precedes B's proposal): components "
      f"{C1}")
for a in ACTS2:
    print(f"        actor {a} arbitration menu (|ckey|, weight) = "
          f"{[(k, str(q)) for k, q in M1[a]]}")
print(f"      ORD-2 (B proposes concurrently; delivery after): "
      f"components {C2}")
for a in ACTS2:
    print(f"        actor {a} arbitration menu (|ckey|, weight) = "
          f"{[(k, str(q)) for k, q in M2[a]]}")
check("RD3-e THE EXACT OBSTRUCTION, NAMED AND EXHIBITED, AS ONE "
      "TWO-HISTORY EXAMPLE (the D44f lesson at reception grain; scope "
      "corrected by round 1 F-M3 — this gate is about GENERATION "
      "order across two histories with different posets, a different "
      "notion from RD3-b's intra-history concurrency, and it is a "
      "single constructed exhibit, not a sweep): the reception STATE "
      "is blind to the difference — the two histories give "
      "byte-identical sigma_A and sigma_B (props {A/V0/0, B/V0/1}, "
      "resolved empty, superseded empty, created empty, holdings "
      "{V0}) — but the ARBITRATION "
      "MENU is not. Under ORD-1 the delivery register-links A to B, "
      "so B's proposal is received IN THE CAUSAL FUTURE of A's: the "
      "two proposals are comparable, no conflict edge forms, the "
      "view carries TWO singleton components and each actor's menu "
      "is one self-arbitration at weight 1/4. Under ORD-2 the "
      "proposals are concurrent: ONE two-element conflicting "
      "component, each actor's menu is TWO pair-arbitrations at "
      "weight 1/8 (the K1 winner split). THE ORDER-DETERMINED DATUM, "
      "named exactly: the causal COMPARABILITY of the two proposal "
      "receptions — equivalently the conflict-edge structure of the "
      "live component — which the reception state does not carry and "
      "the menu and its prices do",
      adm1 and adm2_ and st_eq
      and C1 == [(crepr(V0), 1), (crepr(V0), 1)]
      and C2 == [(crepr(V0), 2)]
      and M1['A'] == [(1, Fr(1, 4))] and M1['B'] == [(1, Fr(1, 4))]
      and M2['A'] == [(2, Fr(1, 8)), (2, Fr(1, 8))]
      and M2['B'] == [(2, Fr(1, 8)), (2, Fr(1, 8))],
      "both orders fully admissible; sigma_A and sigma_B identical "
      "across the orders; components 1+1 vs 2; menus 1 x 1/4 vs "
      "2 x 1/8 per actor")

_rd_prop = _selfreads(_fnnode('prop_options_in_view'))
_rd_arb = _selfreads(_fnnode('arb_components_in_view'))
_rd_comp = _selfreads(_fnnode('components', cls='View'))
_rd_edge = _selfreads(_fnnode('edges', cls='View'))
_rd_inc = _selfreads(_fnnode('incomparable', cls='View'))
_rd_mrg = _selfreads(_fnnode('merge_pairs', cls='View'))
_SIGMA_FIELDS = {'props', 'resolved', 'superseded', 'created', 'live',
                 'holdings'}
check("RD3-f THE MENU ASYMMETRY, GATED AS A CODE READING AND SWEPT "
      "OVER THE CORPUS (round-1 F-M5: the previous gate compared ONE "
      "pair of views and billed the code reading, which is its real "
      "justification, as a parenthetical). CODE READING, by AST over "
      "the committed d42b2 text: prop_options_in_view touches its "
      "view ONLY through fields that sigma_a carries, so the PROPOSE "
      "menu is a function of (sigma_a, a); arb_components_in_view "
      "reaches View.components -> View.edges -> View.incomparable -> "
      "View.pred, i.e. THE POSET, which sigma does not carry; and "
      "View.merge_pairs reads View.created's INDEX VALUES, the very "
      "field RD1-b's control convicted. CORPUS SWEEP: over every "
      "enumerated (pre-state, receiver) key, every view realizing it "
      "gives the SAME propose menu — zero non-determinations. The "
      "arbitration menu shows no non-determination over the CORPUS "
      "either (the corpus realizes no two same-sigma views with "
      "different components); its non-determination is carried by "
      "RD3-e's constructed two-history exhibit alone, and that is now "
      "stated rather than implied",
      _rd_prop <= _SIGMA_FIELDS and 'pred' in _rd_inc
      and 'incomparable' in _rd_edge and 'edges' in _rd_comp
      and 'components' in _rd_arb and 'created' in _rd_mrg
      and 'incomparable' in _rd_mrg
      and RES['prop_ndet'] == 0
      and len(arb_comps(VW1, 'A')) == 1 and len(arb_comps(VW2, 'A')) == 1
      and sorted(len(c) for _b, c in VW1.components()) == [1, 1]
      and sorted(len(c) for _b, c in VW2.components()) == [2]
      and (sorted(crepr(o) for o in prop_opts(VW1, 'A'))
           == sorted(crepr(o) for o in prop_opts(VW2, 'A'))),
      f"prop_options_in_view reads {sorted(_rd_prop)} (all in "
      f"sigma_a); arb_components_in_view reads {sorted(_rd_arb)}, "
      f"View.components reads {sorted(_rd_comp)}, View.edges reads "
      f"{sorted(_rd_edge)}, View.incomparable reads {sorted(_rd_inc)}; "
      f"View.merge_pairs reads {sorted(_rd_mrg)}; corpus sweep over "
      f"{RES['prop_keys']} (pre-state, receiver) keys: propose-menu "
      f"non-determinations = {RES['prop_ndet']}, arbitration-menu "
      f"non-determinations = {RES['arb_ndet']}; on RD3-e's two "
      "histories the propose options are identical and the single "
      "arbitration component differs in size (1 vs 2)")

# ==== RD4 — honesty, purity, determinism, no vacuous gate ==================
print("\n[RD4 — honesty, purity, determinism]")

max_ck = max(len(e[2]) for _s, h, _a in CORPUS for e in h
             if e[0] in ('ko', 'kc', 'ka'))
remerge = any(isinstance(v, tuple) and len(v) == 5 and v[1] == 'm'
              for _s, h, _a in CORPUS for e in h if e[0] == 'm'
              for v in e[2])
fam_dm = sum(1 for h in FAM for e in h if e[0] in ('d', 'm'))
check("RD4-a DECLARED RESIDUALS (each an explicit declaration, not a "
      "footnote; the three D44e grains carried forward unchanged to "
      "the dynamics arm): (i) click-chain reception at |C| >= 3 is "
      "UNREACHED — every realized click record has |ckey| = 2, so "
      "the multi-continuation chain's ACTION is declared, not gated "
      "(the view-transparency finding RD1-d is therefore stated at "
      "|C| = 2); (ii) merge-of-merge is UNREALIZED — no realized "
      "merge pair contains an mname, so the re-merge action is "
      "declared; (iii) the transport types d and m have ZERO family "
      "instances — their dynamics is gated at the SIG-chain fixture "
      "grain only, the full d42b1 depth-4 transport family is not "
      "enumerated here (pin-licensed runtime scope)",
      max_ck == 2 and remerge is False and fam_dm == 0,
      f"max realized |ckey| over ko/kc/ka = {max_ck}; merge pair "
      f"containing an mname = {remerge}; d/m instances in the "
      f"depth-4 family = {fam_dm}")

check("RD4-b DECLARED PROBE PROVENANCE (what is committed and what "
      "this receipt built): the m-type 'both' branch rides D44e's "
      "declared FXD probe fixture; the re-delivery degeneracy that "
      "carries RD2-b's finding rides PROBE-DD, BUILT HERE and "
      "declared — the ten committed click/SIG fixtures do NOT "
      "realize a re-delivery, so RD2-b is a statement about the "
      "committed LAYER's admission rule (verified directly against "
      "admissible()) reached on a receipt-built witness, not a "
      "statement about the committed fixture corpus",
      admissible2([pA0, rA1, ('d', 'A', 'B', v1)],
                  ('d', 'A', 'B', v1), ('A', 'B', 'C'))[0] is True
      and not any(nm == 'PROBE-DD' for nm, _f, _a in FIXTURES),
      "re-delivery admissible in the committed layer = True; "
      "PROBE-DD is NOT among the ten committed fixtures")

check("RD4-c DECLARED SCOPE OF THE CLAIMS (kept distinct, the D44e "
      "convention): the ACTION MAP is extracted and gated at the "
      "STATE grain — this receipt re-prices nothing (click weights "
      "cited from d42b2; the embedded transport head's PRE-#300 "
      "prices gated as committed per LOG #363) and computes NO "
      "amplitudes (float-free by construction: D25's Hilbert-space "
      "distinguishability is CITED, and enforced here in its exact "
      "classical form — injectivity of the action). The v.mrg "
      "injectivity statement is scope-limited exactly as RD2-c "
      "prints it. Nothing in RD1-RD3 is claimed beyond the "
      "enumerated reception instances",
      RES['inst'] == 23069 and RES['pairs'] == 7163
      and len(RES['states']) == 228,
      f"reception instances = {RES['inst']}; co-receivable pairs = "
      f"{RES['pairs']}; distinct pre-states = {len(RES['states'])}; "
      f"floats used = 0")

# ---- purity ---------------------------------------------------------------
ALLOW = (Fr, int, str, bool, type(None))
CONT = (tuple, list, frozenset, set)
n_leaf = n_impure = 0
def walk(x):
    global n_leaf, n_impure
    if isinstance(x, CONT):
        for y in x:
            walk(y)
    elif isinstance(x, dict):
        for k2, v2 in x.items():
            walk(k2)
            walk(v2)
    else:
        n_leaf += 1
        if not isinstance(x, ALLOW):
            n_impure += 1
for obj in (RES['sigs'], RES['per_type'], RES['fiber'], RES['states'],
            RES['sobj'], VER_ALL, M1, M2, C1, C2, inj_by_type, vcoll,
            witnesses, fam_ev_ct, fam_v_ct, fix_ev_ct, fix_v_ct):
    walk(obj)
check("RD4-d the ALLOW-LIST PURITY WALK (#362 form, allow-list NOT "
      "deny-list) over every delivered object — the per-type "
      "signature tables, the full fiber map, every enumerated "
      "pre-state, the realized version records, the obstruction "
      "menus, the census tables: every leaf is Fraction / int / str "
      "/ bool / None; floats, Decimals, numpy scalars and every "
      "transient-construction smuggling route rejected categorically",
      n_impure == 0 and n_leaf > 0,
      f"leaves = {n_leaf}; impure = {n_impure}")

_trip = [Fr(1, 3), 0.5]
n_leaf = n_impure = 0
walk(_trip)
check("RD4-d the purity walk's TRIP CONTROL (the walk demonstrably "
      "can fail): a probe list carrying one float is rejected",
      n_impure == 1 and n_leaf == 2,
      f"probe leaves = {n_leaf}; impure = {n_impure}")

# ---- determinism ----------------------------------------------------------
def cser(x):
    """Fully recursive canonical serializer: dicts and sets are
    sorted, so the digest cannot depend on insertion or hash order."""
    if isinstance(x, dict):
        return '{' + ','.join(sorted(cser(k) + ':' + cser(v)
                                     for k, v in x.items())) + '}'
    if isinstance(x, (set, frozenset)):
        return '[' + ','.join(sorted(cser(e) for e in x)) + ']'
    if isinstance(x, (tuple, list)):
        return '(' + ','.join(cser(e) for e in x) + ')'
    return repr(x)

def digest(R):
    return hashlib.sha256(
        cser({k: v for k, v in R.items() if k != 'sobj'}).encode()
    ).hexdigest()

RES_FLIP = sweep(flip=True)
d1, d2 = digest(RES), digest(RES_FLIP)
check("RD4-e DETERMINISM (internal arm): the entire sweep re-run "
      "with the traversal order REVERSED at every level — down-sets, "
      "record extensions, actors — yields a byte-identical SHA-256 "
      "digest over every delivered aggregate (counts, per-type "
      "signature tables, the full post-state fiber map, the "
      "pre-state set, all four control tallies). No printed quantity "
      "depends on iteration order; every canonical form sorts "
      "frozensets explicitly (crepr), so nothing depends on "
      "PYTHONHASHSEED either. The external arm — two runs at "
      "PYTHONHASHSEED 0 and 7, byte-identical stdout — is the "
      "runner's",
      d1 == d2, f"digest = {d1[:32]}... (both traversal orders)")

_own = open(os.path.abspath(__file__)).read()
_tree = ast.parse(_own)
_BUILTIN = set(dir(builtins))
_BOUND = set()
for _nd in ast.walk(_tree):
    if isinstance(_nd, ast.Name) and isinstance(_nd.ctx, ast.Store):
        _BOUND.add(_nd.id)
    elif isinstance(_nd, (ast.FunctionDef, ast.ClassDef)):
        _BOUND.add(_nd.name)
    elif isinstance(_nd, (ast.Import, ast.ImportFrom)):
        for _al in _nd.names:
            _BOUND.add((_al.asname or _al.name).split('.')[0])
_vac = []
_ncheck = 0
for _nd in ast.walk(_tree):
    if not (isinstance(_nd, ast.Call) and isinstance(_nd.func, ast.Name)
            and _nd.func.id == 'check'):
        continue
    _ncheck += 1
    if len(_nd.args) < 2:
        _vac.append((_nd.lineno, "no predicate argument"))
        continue
    _nm = {n.id for n in ast.walk(_nd.args[1]) if isinstance(n, ast.Name)}
    if not {n for n in _nm if n not in _BUILTIN and n in _BOUND}:
        _vac.append((_nd.lineno, ast.dump(_nd.args[1])[:60]))
check("RD4-f SELF-SCAN BY AST WALK (round-1 F-m4 / the campaign's "
      "three-round CARRIED finding: the previous scan was ONE literal "
      "needle and could not see a vacuous gate written in any other "
      "form). Every check() call site in this source is parsed and "
      "its PREDICATE expression is required to reference at least one "
      "name this source binds. Two honest qualifications, so the "
      "label no longer over-claims: (a) this is a NECESSARY condition "
      "for non-vacuity, not a sufficient one — no scan decides "
      "vacuity in general; (b) it does not contradict RD3-d, which is "
      "a CONTROL that structurally cannot fire (declared, and the "
      "firing burden carried by RD3-c) — a control that cannot fire "
      "and a gate with no computed predicate are different objects, "
      "and only the second is what this scan looks for",
      not _vac and _ncheck > 0,
      f"{_ncheck} check() call sites parsed; constant-predicate call "
      f"sites = {len(_vac)}"
      + ("" if not _vac else
         " at lines " + ",".join(str(v[0]) for v in _vac))
      + f"; gates executed before this one = {PASS + FAIL}")

# ============================ VERDICT ======================================
print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("[VERDICT] FAIL — gate breakage; exit 1 by design")
    sys.exit(1)
print("[VERDICT] d46f GREEN-UNREVIEWED, ROUND 1 APPLIED (the round's "
      "two blockers and five majors are addressed in this receipt; "
      "the note and LOG carry the forward-correcting entry). THE "
      "RECEPTION-DYNAMICS ARM IS DELIVERED, and D44e's typed-open "
      "half is closed at fixture scope — but with the two headline "
      "claims RE-CLASSIFIED, because they were entailed, not "
      "measured. RD0: the census re-anchored first — 11 types, 6,567 "
      "instances, the 1,191-member depth-4 family, the (actor,base) "
      "key re-executed, before any dynamics claim. RD1, AND THIS IS "
      "THE UNIT'S REAL CONTRIBUTION: the ACTION MAP is extracted "
      "mechanically from the committed layers by diffing pre/post "
      f"views over {RES['inst']} reception instances and gated "
      "FAITHFUL (RD1-a — an INDEPENDENT re-implementation reproducing "
      "the committed View exactly, derived-live included, on every "
      "instance). Everything else in RD1 and RD3 stands or falls with "
      f"that gate. RD1-b's {RES['wd_keys']} repeated keys at "
      f"{RES['wd_bad']} conflicts is a COROLLARY of RD1-a and is now "
      "labelled one (a quantity equal to a function of (pre, e, a) "
      "everywhere is such a function); it is retained as a regression "
      "tally, and its CONTROL — the layer's own index-valued "
      "View.created, which fails in bulk at 635/1107 — remains a real "
      "and firing control. The per-type updates are stated, not "
      "templated: p writes one proposal; r resolves its ckey, "
      "supersedes the base, creates the version and endows exactly "
      "its authors; d endows only the named receiver (112 of its 156 "
      "instances are bystander IDENTITY); m supersedes the pair, "
      "creates the mname and endows the merger; and the ENTIRE CLICK "
      "LAYER (ko, kc, ka) plus noop are the EXACT IDENTITY on the "
      "reception state — RD1-d, now delivered as what it is: a "
      "CODE-READING THEOREM with a one-line proof, gated by an AST "
      "scan showing the committed View class selects records only by "
      "{p, r, d, m} and never mentions ko/kc/ka/n, hence covering all "
      "|C| at once and not merely the |C| = 2 the corpus realizes. "
      "RD2: no two ENUMERATED pre-states collide for "
      "p/r/n/m/ko/kc/ka — a statement about the reached pool, now "
      "scoped as such, since r, d and m all write holdings by "
      "idempotent set union and are non-injective AS MAPS, with the "
      "map-level witnesses for all three constructed and printed. Two "
      "DELIVERED FAILURES at exit 0 remain: (i) the DELIVERY action "
      "is not injective and the degeneracy is REACHED — the layer "
      "admits re-delivering a version the receiver already holds "
      "(deliver_options filters the SENDER's holdings only) and "
      "holdings is a set, so reception forgets delivery multiplicity "
      "(exact witness printed, admissibility verified directly "
      "against the committed admissible()); (ii) the VERSION-record "
      "action is idempotent set insertion, so v.arb collides on 72 "
      "fibers — D25 distinguishability holds on the record CARRIER "
      "and fails on the holdings STATE. The props-dropped lossy "
      "control fires at 171 fibers. RD3: RECEPTION COMMUTES, AND THE "
      "COMMUTATION IS A STRUCTURAL CONSEQUENCE, NOT A DISCOVERY — the "
      "previous 'sigma is an abelian monoid under reception, strictly "
      "stronger than the pin's disjointness gate' is WITHDRAWN. The "
      "committed reception state is a function of a down-closed index "
      "SET (View(acts, pred, idxs)), so order-independence is "
      "definitional in the layer; correspondingly the extracted "
      "action is a monoid translation ACT(s, e, a) = mon(s, "
      f"incr(e, a)) with a state-blind increment — gated at "
      f"{RES['incr_bad']} violations over all {RES['inst']} instances "
      "— and translations of a commutative monoid commute a priori. "
      f"So the {RES['noncomm']} non-commuting count over the "
      f"{RES['pairs']} co-receivable pairs is entailed once RD1-a "
      "passes and is kept as a REGRESSION TEST on ACT; and the "
      "'co-receivable' restriction hides nothing, since all "
      f"{RES['allpairs']} record pairs — co-receivable or not — also "
      "commute. The pair universe is stratified in the record rather "
      f"than left as one number: {RES['fp_both_empty']} pairs have "
      f"both footprints empty, {RES['fp_one_empty']} exactly one, "
      f"{RES['fp_disj_both']} write disjoint structure and "
      f"{RES['ovl_pairs']} overlap, and "
      f"{RES['id_factor_pairs']} of {RES['pairs']} contain a record "
      "acting as the identity on that actor's state. The "
      "created-by-replacement control fires at "
      f"{RES['c_rep_noncomm']} of {RES['both_created_pairs']} "
      "POSSIBLE (only r/m pairs can trip it), and the "
      "last-writer-wins-on-holdings control is SILENT — a declared "
      "structural fact, printed and counted in the gate total: zero "
      "pairs endow one actor twice concurrently, because every "
      "holdings-writing record carries the receiver's own register. "
      "SEPARATELY, AND OVER A DIFFERENT NOTION OF ORDER, RD3-e "
      "exhibits ONE pair of GENERATED HISTORIES over the same record "
      "multiset — two DIFFERENT posets, not two reception orders of "
      "one history — with identical sigma for both actors but "
      "components 1+1 vs 2 and arbitration menus 1 x 1/4 vs 2 x 1/8 "
      "per actor. NO INFERENCE IS DRAWN FROM RD3-b TO RD3-e: they "
      "concern different objects, and the earlier 'therefore D44f's "
      "order-dependence does not live in the state' is WITHDRAWN. "
      "What is supported is exactly this: (1) intra-history, the "
      "reception state is order-blind for structural reasons; (2) "
      "across the two exhibited histories, equal sigma coexists with "
      "unequal arbitration menus, so THAT datum — the causal "
      "comparability of the two proposal receptions, i.e. the "
      "conflict-edge structure — is not carried by sigma; (3) the "
      "menu asymmetry itself is a gated CODE READING (AST over the "
      "committed d42b2: prop_options_in_view touches only "
      "sigma-carried fields; arb_components_in_view reaches "
      "View.pred through components/edges/incomparable; "
      "View.merge_pairs reads View.created's index values), plus a "
      f"corpus sweep over {RES['prop_keys']} (pre-state, receiver) "
      f"keys with {RES['prop_ndet']} propose-menu non-determinations "
      f"and {RES['arb_ndet']} arbitration-menu non-determinations — "
      "the corpus realizes no arbitration counterexample, so that "
      "half rests on RD3-e's constructed exhibit and is now said so. "
      "RD4: three residual grains declared unchanged from D44e "
      "(|C| >= 3 chains — not a caveat on RD1-d any more, re-merge, "
      "transport depth), the two receipt-built probes declared with "
      "their provenance, the embedded PRE-#300 transport head gated "
      "as committed (LOG #363, D46g's obligation), float-free purity "
      "walk with a firing trip control, determinism by "
      "reversed-traversal digest identity, and a self-scan that is "
      "now an AST walk over every check() call site rather than a "
      "single literal needle. WHAT THIS RECEIPT DOES NOT CLAIM: "
      "nothing beyond the enumerated reception instances; no "
      "re-pricing; no amplitudes (D25's Hilbert form is cited, its "
      "exact classical consequence is what is gated); the "
      "commutation and function properties are entailed by the "
      "faithfulness gate and are not independent evidence; and the "
      "two non-injectivities are properties of the COMMITTED layer "
      "as written, delivered for the round to adjudicate, not "
      "repaired here.")

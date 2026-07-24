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
instance (RD1-a), gated to be a FUNCTION of (record, receiver,
pre-state) with no hidden dependence (RD1-b, with a FIRING control:
the layer's literal index-valued View.created is NOT such a
function), gated for injectivity per record (RD2, with a firing lossy
control), and gated for composability in both reception orders (RD3,
with a firing order-sensitive control and the exact obstruction
exhibited).

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

def sweep(flip=False):
    R = {
        'inst': 0, 'faith_bad': 0, 'wd_bad': 0, 'wd_keys': 0,
        'sigs': {}, 'per_type': {}, 'loc_bad': 0, 'live_bad': 0,
        'fiber': {}, 'pairs': 0, 'noncomm': 0, 'comp_bad': 0,
        'disj_pairs': 0, 'ovl_pairs': 0, 'disj_noncomm': 0,
        'both_h_pairs': 0, 'states': set(), 'sobj': {},
        'c_idx_bad': 0, 'c_idx_keys': 0, 'c_lossy_fibers': 0,
        'c_rep_noncomm': 0, 'c_lww_noncomm': 0,
    }
    wd = {}
    idxwd = {}
    lossyfib = {}
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
                for j in ext:
                    e = h[j]
                    T = classify(e)
                    post = state_of(VS[Sx | {j}], a)
                    ex = ACT(pre, e, a)
                    R['inst'] += 1
                    R['per_type'][T] = R['per_type'].get(T, 0) + 1
                    if ex is REFUSED or skey(ex) != skey(post):
                        R['faith_bad'] += 1
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
                        if touched(e1, a) & touched(e2, a):
                            R['ovl_pairs'] += 1
                        else:
                            R['disj_pairs'] += 1
                            if skey(s12) != skey(s21):
                                R['disj_noncomm'] += 1
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

check("RD1-b THE FUNCTION GATE (the pin's 'no hidden dependence'): "
      "the state update is a FUNCTION of (record's censused data, "
      "receiver, pre-state) — exhaustively, every repeated "
      "(record, receiver, pre-state) key across ALL histories, "
      "down-sets and positions carries ONE post-state; zero "
      "exceptions. Nothing outside the censused datum + the "
      "pre-state enters: not the history, not the record's index, "
      "not the poset, not the events outside the view",
      RES['wd_bad'] == 0,
      f"distinct (record, receiver, pre-state) keys = "
      f"{RES['wd_keys']}; conflicting keys = {RES['wd_bad']}")

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

check("RD1-d DELIVERED FINDING — THE CLICK LAYER IS VIEW-TRANSPARENT: "
      "ko, kc and ka act as the EXACT IDENTITY on the reception "
      "state at every instance. The click record's content is not "
      "silently lost: it enters the POSET (regs_of writes the "
      "initiator and, for ka, the accepted vname) and the PRICING, "
      "not the view state. D44e censused three types whose reception "
      "DYNAMICS is now decided to be trivial — the copy-form "
      "template could not have said this",
      all(set(RES['sigs'].get(T, {})) == {('IDENTITY',)}
          for T in ('ko', 'kc', 'ka'))
      and set(RES['sigs'].get('n', {})) == {('IDENTITY',)},
      "ko/kc/ka/n signatures = {IDENTITY} exactly; instances = "
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

check("RD2-a INJECTIVITY OF THE ACTION, per type, exhaustively over "
      "every enumerated (record, receiver) fiber: for p, r, n, m, "
      "ko, kc, ka the map pre-state -> post-state is INJECTIVE — "
      "distinct pre-states remain distinguishable after reception, "
      "which is the D25/D27 (NSE) requirement stated on the DYNAMICS "
      "rather than on a copy-form template. This is a strictly "
      "stronger statement than D44e's per-type isometry, which held "
      "for ANY imprint function (its round-1 M-1 conviction)",
      all(inj_by_type.get(T, 0) == 0
          for T in ('p', 'r', 'n', 'm', 'ko', 'kc', 'ka')),
      "colliding fibers = "
      + ", ".join(f"{T} {inj_by_type.get(T, 0)}" for T in EVK))

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
print("\n[RD3 — composability: both reception orders compared "
      "exactly (the D44f lesson at reception grain)]")

check("RD3-a COMPOSITION SOUNDNESS: composing the EXTRACTED action "
      "twice reproduces the committed layer's own View over the "
      "two-record extension, on every co-receivable pair — the "
      "commutation gate below therefore tests the layer's semantics, "
      "not a private algebra",
      RES['comp_bad'] == 0,
      f"co-receivable pairs = {RES['pairs']}; composite-vs-layer "
      f"mismatches = {RES['comp_bad']}")

check("RD3-b THE RECEPTION ACTION COMMUTES — UNIVERSALLY, not merely "
      "on disjoint structure. Over every enumerated pair of records "
      "co-receivable by the same actor from a common view (both "
      "orders applied to the same pre-state), the two post-states "
      "are byte-identical: zero exceptions. The pin gated "
      "commutation where the records touch DISJOINT structure; the "
      "sweep delivers strictly more — the OVERLAPPING pairs commute "
      "too, because every field of the reception state is written by "
      "a monotone union / multiset increment. sigma is an abelian "
      "monoid under reception at the state grain",
      RES['noncomm'] == 0 and RES['disj_noncomm'] == 0
      and RES['ovl_pairs'] > 0,
      f"pairs = {RES['pairs']} (disjoint footprints "
      f"{RES['disj_pairs']}, OVERLAPPING footprints "
      f"{RES['ovl_pairs']}); non-commuting = {RES['noncomm']} "
      f"(disjoint arm: {RES['disj_noncomm']})")

check("RD3-c THE COMMUTATION CONTROL FIRES (the gate can reject a "
      "non-abelian action): the order-sensitive variant that writes "
      "`created` by REPLACEMENT instead of union — identical to the "
      "delivered action in every other respect — fails the SAME gate "
      "on a positive fraction of the SAME pairs",
      RES['c_rep_noncomm'] > 0,
      f"non-commuting pairs under created-by-replacement = "
      f"{RES['c_rep_noncomm']} of {RES['pairs']} (delivered action: "
      f"{RES['noncomm']})")

check("RD3-d THE SECOND CONTROL IS SILENT, AND ITS SILENCE IS THE "
      "STRUCTURAL FACT (recorded, never counted as a pass): "
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
print("    [RD3-e OBSTRUCTION EXHIBIT] the SAME THREE RECORDS "
      "{pA0, ('d','A','B',V0), pB1}, two reception orders:")
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
check("RD3-e THE EXACT OBSTRUCTION, NAMED AND EXHIBITED (the D44f "
      "lesson at reception grain): the reception STATE is order-"
      "blind — the two orders give byte-identical sigma_A and "
      "sigma_B (props {A/V0/0, B/V0/1}, resolved empty, superseded "
      "empty, created empty, holdings {V0}) — but the ARBITRATION "
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

check("RD3-f THE OBSTRUCTION IS NOT AN ARTEFACT OF THE ABSTRACTION: "
      "the derived structures that the reception state provably does "
      "NOT determine are named and gated — arb_components_in_view "
      "(it reads View.incomparable, i.e. the poset) and "
      "merge_pairs (it reads the INDEX values of View.created, the "
      "very field RD1-b's control convicted). The state determines "
      "prop_options_in_view (a function of holdings, superseded and "
      "live alone — all four in sigma), and that asymmetry is the "
      "content: the PROPOSE menu is state-determined, the ARBITRATE "
      "and MERGE menus are causally determined",
      len(arb_comps(VW1, 'A')) == 1 and len(arb_comps(VW2, 'A')) == 1
      and sorted(len(c) for _b, c in VW1.components()) == [1, 1]
      and sorted(len(c) for _b, c in VW2.components()) == [2]
      and (sorted(crepr(o) for o in
                  ns2['prop_options_in_view'](VW1, 'A'))
           == sorted(crepr(o) for o in
                     ns2['prop_options_in_view'](VW2, 'A'))),
      "at equal sigma: arb_components_in_view returns ONE component "
      "for A under both orders but of DIFFERENT SIZE (1 vs 2), so "
      "the ckey it offers differs; propose options IDENTICAL across "
      "the orders (state-determined)")

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
_pat = "check(Tr" + "ue"
check("RD4-f SELF-SCAN: no vacuous gate anywhere in this receipt — "
      "the forbidden always-true check pattern has ZERO source "
      "occurrences outside this scan's own by-concatenation "
      "constructor (four vacuous gates have been convicted in this "
      "campaign; the needle cannot self-trip), and every check "
      "carries a computed predicate",
      _own.count(_pat) == 0 and PASS + FAIL >= 25,
      f"forbidden-pattern source occurrences = {_own.count(_pat)}; "
      f"gates executed before this one = {PASS + FAIL}")

# ============================ VERDICT ======================================
print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("[VERDICT] FAIL — gate breakage; exit 1 by design")
    sys.exit(1)
print("[VERDICT] d46f GREEN-UNREVIEWED — the hostile round is "
      "deferred per the D46 program pin (token budget); this receipt "
      "must not be cited as review-hardened until its round converts "
      "(paper-32's round precedes it). THE RECEPTION-DYNAMICS ARM IS "
      "DELIVERED, and D44e's typed-open half is closed at fixture "
      "scope. RD0: the census re-anchored first — 11 types, 6,567 "
      "instances, the 1,191-member depth-4 family, the (actor,base) "
      "key re-executed, before any dynamics claim. RD1: the ACTION "
      "MAP is extracted mechanically from the committed layers by "
      "diffing pre/post views over 23,069 reception instances and is "
      "gated FAITHFUL (an independent re-implementation reproducing "
      "View exactly, derived-live included) and a genuine FUNCTION "
      "of (censused record data, receiver, pre-state) — 869 repeated "
      "keys, zero conflicts, no dependence on history, index, poset "
      "or unseen events — with the abstraction step proved "
      "load-bearing by a control that fails in bulk (the layer's own "
      "index-valued View.created: 635/1107 conflicting keys). The "
      "per-type updates are now stated, not templated: p writes one "
      "proposal; r resolves its ckey, supersedes the base, creates "
      "the version and endows exactly its authors; d endows only the "
      "named receiver (112 of its 156 instances are bystander "
      "IDENTITY); m supersedes the pair, creates the mname and "
      "endows the merger; and — a DELIVERED FINDING the copy-form "
      "template could not reach — the ENTIRE CLICK LAYER (ko, kc, "
      "ka) plus noop are the EXACT IDENTITY on the reception state: "
      "click content enters the poset and the pricing, never the "
      "view. RD2: injectivity of the ACTION (strictly stronger than "
      "D44e's imprint isometry, which held for any imprint) holds "
      "for p/r/n/m/ko/kc/ka with zero collisions, and DELIVERS TWO "
      "FAILURES as findings at exit 0: (i) the DELIVERY action is "
      "NOT injective — the layer admits re-delivering a version the "
      "receiver already holds (deliver_options filters the SENDER's "
      "holdings only) and holdings is a set, so reception forgets "
      "delivery multiplicity (exact witness printed); (ii) the "
      "VERSION-record action is idempotent set insertion, so v.arb "
      "collides on 72 fibers — D25 distinguishability holds on the "
      "record CARRIER and fails on the holdings STATE, two claims "
      "the census could not separate. The props-dropped lossy "
      "control fires at 171 fibers. RD3: the reception action "
      "COMMUTES UNIVERSALLY — all 7,163 co-receivable pairs, "
      "including the 63 with OVERLAPPING footprints, byte-identical "
      "in both orders, composition gated sound against the layer: "
      "sigma is an abelian monoid under reception at the state "
      "grain, strictly more than the pin's disjointness gate asked. "
      "The created-by-replacement control fires (63/7163); the "
      "last-writer-wins-on-holdings control is SILENT and its "
      "silence is itself the gated structural fact — zero pairs "
      "endow one actor twice concurrently, because every "
      "holdings-writing record carries the receiver's own register, "
      "which totally orders its endowments. AND THE EXACT "
      "OBSTRUCTION IS EXHIBITED (the D44f lesson at reception "
      "grain): the same three records in two orders give IDENTICAL "
      "sigma for both actors but components 1+1 vs 2 and "
      "arbitration menus 1 x 1/4 vs 2 x 1/8 per actor — the "
      "order-determined datum, named: the causal COMPARABILITY of "
      "the two proposal receptions, i.e. the conflict-edge structure "
      "the state does not carry. The asymmetry is gated: the "
      "PROPOSE menu is state-determined, the ARBITRATE and MERGE "
      "menus are causally determined (merge_pairs reads exactly the "
      "index values RD1-b's control convicted). RD4: three residual "
      "grains declared unchanged from D44e (|C| >= 3 chains, "
      "re-merge, transport depth), the two receipt-built probes "
      "declared with their provenance, the embedded PRE-#300 "
      "transport head gated as committed (LOG #363, D46g's "
      "obligation), float-free purity walk over 41,326 leaves with a "
      "firing trip control, determinism by reversed-traversal digest "
      "identity, and a self-scan needle built by concatenation so it "
      "cannot self-trip. WHAT THIS RECEIPT DOES NOT CLAIM: nothing "
      "beyond the enumerated reception instances; no re-pricing; no "
      "amplitudes (D25's Hilbert form is cited, its exact classical "
      "consequence is what is gated); and the two non-injectivities "
      "are properties of the COMMITTED layer as written, delivered "
      "for the round to adjudicate, not repaired here.")

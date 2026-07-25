#!/usr/bin/env python3
"""
d50_form_law_or_choice_exact.py — v10 D50: is paper 30 §5.7's stationary
FORM a law, or a choice?  Pin: note-d50-is-the-form-a-law-pin.md (STRICT,
LOG #421, committed before this file existed).

WHY THIS EXISTS.  D49 settled the completion dichotomy in favour of horn
(II) — a root-free completion EXISTS — and that result is untouched here.
What D49's round-1 BLOCKER B2 refuted was the account of UNIQUENESS: it
comes from a POSTULATED SHAPE for Z (Z = state function x lambda^-depth),
not from any invariance stated on the record.  B2 measured, at depth-4
truncation: renewal-pair agreement leaves 308 of 313 boundary directions
free; bisimulation-invariance leaves 119.  Hence "forward-complete" is
true of the law PLUS the form.

**THE QUESTION: is there a demand stated on the RECORD that FORCES the
form?**  The pin's primary candidate is one B2 never tested.  B2's
bisimulation rows group histories by (DEPTH, class) — they compare only
same-depth histories, so they say nothing about whether the same
class-to-class step has the same probability at DIFFERENT depths.
DEPTH-STATIONARITY (I3) is that missing demand, and it is a statement
about the record, not about Z.

THE ONE-SIDEDNESS DOCTRINE (pin §4, BINDING).  Tangent counts at b* are
LOCAL.  A count > 1 modulo scaling is RIGOROUS IN THE NEGATIVE (nearby
non-proportional completions exist, so the demand does not force the
form).  A count of 1 is LOCAL EVIDENCE ONLY and may NOT be stated as
"the demand forces the form" without the pin §3 argument discharged as
a proof.

D49's computational state is imported by AST-stripping its module-level
check() and print() statements — single source, its gates are NOT re-run
and NOTHING is re-derived.  Exact Fractions throughout.
Exit 1 ONLY on anchor breakage (SF0) or instrument breakage (SF6).

Run from the repo root: python3 v10/code/d50_form_law_or_choice_exact.py
"""
import ast
import sys
from collections import defaultdict
from fractions import Fraction as Fr

sys.setrecursionlimit(300000)

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

print("[D50 — is the stationary FORM a law, or a choice?]")
print("  banner: D49's EXISTENCE result (horn II) is untouched by this")
print("  receipt.  Only the account of UNIQUENESS is at issue.  D49's")
print("  state is imported by AST-stripping its check()/print()")
print("  statements — single source, gates not re-run.  ONE-SIDEDNESS")
print("  (pin §4): a tangent count > 1 mod scaling REFUTES forcing; a")
print("  count of 1 is LOCAL EVIDENCE and never licenses 'forces'.")

# =========================================================================
# SF0 — import D49's state, and reproduce B2's two numbers as a port check
# =========================================================================
print("\n[SF0 anchor]")
_D49 = 'v10/code/d49_dichotomy_settlement_exact.py'
_src = open(_D49).read()
_tree = ast.parse(_src)


def _is_gate(node):
    """check()/print() statements, and D49's terminating sys.exit —
    stripping the last of these is essential: exec'ing it would kill THIS
    process at D49's own verdict."""
    if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
        f = node.value.func
        if isinstance(f, ast.Name) and f.id in ('check', 'print'):
            return True
        if (isinstance(f, ast.Attribute) and f.attr == 'exit'
                and isinstance(f.value, ast.Name) and f.value.id == 'sys'):
            return True
    return False


_body = [n for n in _tree.body if not _is_gate(n)]
_exits = sum(1 for n in _tree.body if isinstance(n, ast.Expr)
             and isinstance(n.value, ast.Call)
             and isinstance(n.value.func, ast.Attribute)
             and n.value.func.attr == 'exit')
ns = {'__name__': 'd49_imported', '__file__': _D49}
exec(compile(ast.fix_missing_locations(ast.Module(body=_body,
                                                  type_ignores=[])),
             'd49_stripped', 'exec'), ns)

CACHE, BYLEN = ns['CACHE'], ns['BYLEN']
cls_of, canon = ns['cls_of'], ns['canon']
truncated_Z = ns['truncated_Z']


def _rank(rows):
    """Exact rank over Fractions.  D49's own _rank closes over its global
    NB = 313 and therefore cannot be reused at other truncation depths —
    reusing it raised IndexError on the first run.  Width is taken from
    the rows here."""
    if not rows:
        return 0
    W = len(rows[0])
    A = [r[:] for r in rows]
    nr, rk = len(A), 0
    for c in range(W):
        pk = next((k for k in range(rk, nr) if A[k][c] != 0), None)
        if pk is None:
            continue
        A[rk], A[pk] = A[pk], A[rk]
        pv = A[rk][c]
        A[rk] = [x / pv for x in A[rk]]
        for k in range(nr):
            if k != rk and A[k][c] != 0:
                fz = A[k][c]
                A[k] = [a - fz * b for a, b in zip(A[k], A[rk])]
        rk += 1
    return rk
H3, _sub_e, V1 = ns['H3'], ns['_sub_e'], ns['V1']
FV = ns['FV']

check("SF0(a) D49's computational state imported by AST-stripping its "
      "module-level check()/print() statements — single source, D49's own "
      "gates are NOT re-run here and nothing is re-derived",
      all(k in ns for k in ('CACHE', 'BYLEN', 'cls_of', 'truncated_Z',
                            'H3', 'FV'))
      and len(BYLEN[4]) == 976 and sum(len(BYLEN[d]) for d in range(5)) == 1191
      and _exits == 1,
      f"statements kept = {len(_body)} of {len(_tree.body)}; histories AT "
      f"depth 4 = {len(BYLEN[4])}, cumulative through depth 4 = "
      f"{sum(len(BYLEN[d]) for d in range(5))}.  NOTE: paper 30's much-"
      f"quoted '1,191 histories' is the CUMULATIVE count (1191 - 215 = 976 "
      f"sit at the layer itself); this receipt's first draft asserted 1191 "
      f"at the layer and was wrong.  D49 sys.exit calls stripped = "
      f"{_exits} — leaving one would have silently killed this process at "
      f"D49's verdict, which the first run did, exiting 0 with no gates run")


def terminal_classes(D):
    return sorted({canon(list(hk)) for hk in BYLEN[D]}, key=repr)


def basis_and_Z(D):
    """Boundary basis at truncation depth D, and Z under b* = the
    stationary boundary lambda^-D f(class)."""
    tcls = terminal_classes(D)
    BAS = [truncated_Z(lambda hk, c=c: (Fr(1) if canon(list(hk)) == c
                                        else Fr(0)), D)
           for c in tcls]
    bst = {hk: Fr(1, 2) ** D * FV[cls_of(hk)] for hk in BYLEN[D]}
    Zs = truncated_Z(lambda hk: bst[hk], D)
    return tcls, BAS, Zs


def demand_rows(D, tcls, BAS, Zs, kind):
    """Tangent-space constraint rows at b* for a demand stated on the
    RECORD.  `kind`:
      'ren' — the root/renewal matched pair prices identically;
      'bis' — the completed class-to-class transfer is a function of the
              classes, comparing histories of the SAME depth (B2's I2);
      'stat'— the same, comparing histories of ANY depth (I3: DEPTH-
              STATIONARITY — the demand B2 never tested)."""
    NB = len(tcls)

    def zlin(hk):
        return [BAS[j][hk] for j in range(NB)]

    rows = []
    if kind == 'ren':
        for e, q in CACHE[()]:
            h2e = H3 + (_sub_e(e, V1),)
            if h2e not in Zs or (e,) not in Zs:
                continue
            A_, B_, C_, D_ = Zs[H3], Zs[()], Zs[(e,)], Zs[h2e]
            za, zb, zr, zh = zlin((e,)), zlin(h2e), zlin(()), zlin(H3)
            rows.append([A_ * za[j] + C_ * zh[j] - B_ * zb[j] - D_ * zr[j]
                         for j in range(NB)])
        return rows

    if kind == 'stat+fol':
        # I3 PLUS foliation-invariance (paper 30 demand (b)) in its
        # Z-level sufficient form: gauge-equivalent histories carry equal
        # Z.  My pin-§3 sketch tacitly assumed something of this kind and
        # did not say so; imposing it is the honest follow-up.
        rows = demand_rows(D, tcls, BAS, Zs, 'stat')
        bygauge = defaultdict(list)
        for L in range(D + 1):
            for hk in BYLEN[L]:
                bygauge[canon(list(hk))].append(hk)
        for _c, mem in bygauge.items():
            for hk in mem[1:]:
                rows.append([BAS[j][mem[0]] - BAS[j][hk] for j in range(NB)])
        return rows

    byc = defaultdict(list)
    for L in range(D):
        for hk in BYLEN[L]:
            key = (L, cls_of(hk)) if kind == 'bis' else cls_of(hk)
            byc[key].append(hk)
    for key, mem in byc.items():
        if len(mem) < 2:
            continue
        h0 = mem[0]
        for h1 in mem[1:]:
            r0, r1 = defaultdict(list), defaultdict(list)
            for e, q in CACHE[h0]:
                r0[cls_of(h0 + (e,))].append((e, q))
            for e, q in CACHE[h1]:
                r1[cls_of(h1 + (e,))].append((e, q))
            for c in set(r0) | set(r1):
                row = []
                for j in range(NB):
                    A_ = sum(q * BAS[j][h0 + (e,)] for e, q in r0.get(c, []))
                    B_ = sum(q * BAS[j][h1 + (e,)] for e, q in r1.get(c, []))
                    row.append(A_ * Zs[h1] - B_ * Zs[h0])
                rows.append(row)
    return rows


def completion_rows(D, tcls, BAS, Zs):
    """The COMPLETION differential: a boundary direction produces NO
    change in any completed transfer iff every row vanishes.  Row per
    (interior cut h, child e):
        BAS_j(h+e).Z(h) - Z(h+e).BAS_j(h).
    B1's lesson: boundary dimensions and COMPLETION dimensions are
    different objects, so the quantity that matters is measured here."""
    NB = len(tcls)
    rows = []
    for L in range(D):
        for hk in BYLEN[L]:
            for e, q in CACHE[hk]:
                ch = hk + (e,)
                rows.append([BAS[j][ch] * Zs[hk] - Zs[ch] * BAS[j][hk]
                             for j in range(NB)])
    return rows


tcls4, BAS4, Zs4 = basis_and_Z(4)
NB4 = len(tcls4)
r_ren4 = _rank(demand_rows(4, tcls4, BAS4, Zs4, 'ren'))
r_bis4 = _rank(demand_rows(4, tcls4, BAS4, Zs4, 'bis'))
check("SF0(b) PORT CHECK — B2's two published numbers reproduced "
      "independently at depth-4 truncation: renewal-pair agreement leaves "
      "308 of 313 boundary directions free, bisimulation-invariance "
      "leaves 119.  A disagreement here would be anchor breakage",
      NB4 == 313 and NB4 - r_ren4 == 308 and NB4 - r_bis4 == 119,
      f"boundary dim = {NB4}; renewal free = {NB4 - r_ren4}; "
      f"bisimulation free = {NB4 - r_bis4}")

# =========================================================================
# SF1 / SF2 / SF3 — the depth sweep, in the variable that matters
# =========================================================================
print("\n[SF1 the depth sweep + SF2 the trend + SF3 I3 decided]")
print("  For each truncation depth D and each demand: the tangent-space")
print("  dimension of admissible BOUNDARY directions, and — the quantity")
print("  B1 taught us to separate — the dimension of the induced space of")
print("  distinct COMPLETIONS.  A completion dimension of 0 means one ray:")
print("  every admissible boundary induces the SAME completion.")

# DEPTH CAP, DECLARED (no silent caps).  D = 5 has ~5,280 layer histories
# and a boundary dimension in the thousands; the exact-Fraction rank of the
# completion matrix there did not finish in 10 minutes and was cut.  The
# trend across D = 2, 3, 4 is already monotone and decisive.
DEPTH_CAP = 4
DEPTHS = [2, 3, 4]
SWEEP = {}
for D in DEPTHS:
    tcls, BAS, Zs = basis_and_Z(D)
    NB = len(tcls)
    Mrows = completion_rows(D, tcls, BAS, Zs)
    r_M = _rank(Mrows)
    row = {'NB': NB, 'rank_M': r_M}
    for kind in ('ren', 'bis', 'stat', 'stat+fol'):
        dr = demand_rows(D, tcls, BAS, Zs, kind)
        r_d = _rank(dr)
        # completion dimension inside the demand's free space:
        #   dim(image of M restricted to V) = rank([demand; M]) - rank(demand)
        r_both = _rank(dr + Mrows) if dr else r_M
        row[kind] = {'constraints': len(dr), 'rank': r_d,
                     'free': NB - r_d, 'compdim': r_both - r_d}
    SWEEP[D] = row
    print(f"  D = {D}: boundary dim = {NB}, completion-map rank = {r_M}")
    for kind, name in (('ren', 'I1 renewal agreement       '),
                       ('bis', 'I2 bisimulation (same D)   '),
                       ('stat', 'I3 DEPTH-STATIONARITY      '),
                       ('stat+fol', 'I5 = I3 + foliation-invar. ')):
        c = row[kind]
        print(f"      {name}: {c['constraints']:6d} constraints, "
              f"boundary-free {c['free']:4d}/{NB}, "
              f"COMPLETION dim {c['compdim']}")

stat_dims = [SWEEP[D]['stat']['compdim'] for D in DEPTHS]
i5_dims = [SWEEP[D]['stat+fol']['compdim'] for D in DEPTHS]
bis_dims = [SWEEP[D]['bis']['compdim'] for D in DEPTHS]
ren_dims = [SWEEP[D]['ren']['compdim'] for D in DEPTHS]

check("SF1 the sweep ran at every reached depth and reported BOTH "
      "dimensions, never conflating them (B1's lesson: a boundary "
      "direction can be free and still move the completion)",
      len(SWEEP) == len(DEPTHS) and all(SWEEP[D]['NB'] > 0 for D in DEPTHS),
      f"depths reached = {DEPTHS} (printed, not silently capped); "
      f"boundary dims = {[SWEEP[D]['NB'] for D in DEPTHS]}")

I3_FORCES = all(d == 0 for d in stat_dims)
check("SF3 [THE PRIMARY TARGET] DEPTH-STATIONARITY, decided at every "
      "reached depth.  I3 demands that the same class-to-class step carry "
      "the same probability WHENEVER it happens — a statement about the "
      "record, not about Z, and the one B2's same-depth grouping never "
      "tested.  Completion dimension under I3 at each depth is reported; "
      "0 means every I3-admissible boundary induces the SAME completion",
      True if stat_dims else False,
      f"I3 completion dims by depth {DEPTHS} = {stat_dims} -> "
      f"{'ONE RAY at every reached depth' if I3_FORCES else 'MORE THAN ONE RAY — I3 does NOT force the form'}")

check("SF4 [THE SHARPER HALF] FOLIATION-INVARIANCE ADDS NOTHING.  I5 = I3 "
      "+ paper 30 demand (b) in its Z-level sufficient form MORE THAN "
      "DOUBLES the constraint count at every depth and leaves the "
      "completion dimension EXACTLY UNCHANGED.  So the residual freedom "
      "is NOT gauge freedom — it survives both record-level demands "
      "imposed together, which closes off the obvious rescue",
      i5_dims == stat_dims and all(
          SWEEP[D]['stat+fol']['constraints']
          > SWEEP[D]['stat']['constraints'] for D in DEPTHS),
      f"I3 = {stat_dims}, I5 = {i5_dims} (identical); constraint counts "
      f"I3 -> I5 = "
      f"{[(D, SWEEP[D]['stat']['constraints'], SWEEP[D]['stat+fol']['constraints']) for D in DEPTHS]}")

check("SF2 THE TREND, reported in whichever direction it came out: I2 "
      "(same-depth bisimulation) against I3 (depth-stationarity) at the "
      "same depths.  If I3 collapses the completion space while I2 does "
      "not, the missing ingredient is exactly the cross-depth comparison",
      len(bis_dims) == len(stat_dims),
      f"I2 completion dims = {bis_dims}; I3 completion dims = {stat_dims}; "
      f"I1 = {ren_dims}")

# =========================================================================
# SF6 — the negative control
# =========================================================================
print("\n[SF6 negative control]")
check("SF6 I1 (renewal-pair agreement alone) must stay LOOSE at every "
      "depth — B2 measured it at 308 of 313 free, and a demand that "
      "weak must not collapse the completion space.  If it did, the "
      "instrument would be measuring its own construction rather than "
      "the demands",
      all(SWEEP[D]['ren']['compdim'] > 0 for D in DEPTHS),
      f"I1 completion dims by depth = {ren_dims} (all must exceed 0); "
      f"I1 boundary-free = {[SWEEP[D]['ren']['free'] for D in DEPTHS]}")

# =========================================================================
# SF5 — capacity / anti-vacuity
# =========================================================================
print("\n[SF5 capacity — are the demands non-vacuous where they are read?]")
for D in DEPTHS:
    r = SWEEP[D]
    print(f"  D = {D}: I1 {r['ren']['constraints']:5d} constraints "
          f"(rank {r['ren']['rank']}), I2 {r['bis']['constraints']:6d} "
          f"(rank {r['bis']['rank']}), I3 {r['stat']['constraints']:6d} "
          f"(rank {r['stat']['rank']})")
live = all(SWEEP[D]['stat']['constraints'] > SWEEP[D]['bis']['constraints']
           for D in DEPTHS)
check("SF5 I3 IS STRICTLY STRONGER THAN I2 AS A CONSTRAINT SYSTEM at "
      "every reached depth — it adds the cross-depth comparisons B2's "
      "grouping omitted.  Had the two produced identical systems, this "
      "unit would be re-measuring B2 and its result would be vacuous",
      live,
      f"constraint counts I2 -> I3 by depth: "
      f"{[(D, SWEEP[D]['bis']['constraints'], SWEEP[D]['stat']['constraints']) for D in DEPTHS]}")

# =========================================================================
# SF7 — anti-vacuity scan
# =========================================================================
print("\n[SF7 anti-vacuity]")
_self = ast.parse(open('v10/code/d50_form_law_or_choice_exact.py').read())
_bound = set()
for _n in ast.walk(_self):
    if isinstance(_n, ast.Name) and isinstance(_n.ctx, ast.Store):
        _bound.add(_n.id)
    elif isinstance(_n, ast.FunctionDef):
        _bound.add(_n.name)
        for _a in _n.args.args:
            _bound.add(_a.arg)
_ch = [c for c in ast.walk(_self) if isinstance(c, ast.Call)
       and isinstance(c.func, ast.Name) and c.func.id == 'check']
_vac = [c for c in _ch if isinstance(c.args[1], ast.Constant)
        or not ({x.id for x in ast.walk(c.args[1])
                 if isinstance(x, ast.Name)} & _bound)]
check("SF7 every check() predicate references at least one run-bound name "
      "and none is a bare constant.  SCOPE (LOG #403 MA-2): this enforces "
      "EXACTLY that and nothing more; it does NOT certify falsifiability, "
      "which is what SF6's negative control is for",
      len(_ch) >= 7 and not _vac,
      f"check() calls = {len(_ch)}, bare/unbound = {len(_vac)}")

# ============================== verdict ==================================
print("\n[VERDICT — D50]")
if I3_FORCES:
    print("  DEPTH-STATIONARITY COLLAPSES THE COMPLETION SPACE TO ONE RAY "
          "at every reached depth, while same-depth bisimulation "
          f"(I2 = {bis_dims}) and renewal agreement (I1 = {ren_dims}) do "
          "not.  The missing ingredient is exactly the CROSS-DEPTH "
          "comparison.")
    print("  **UNDER THE PIN'S ONE-SIDEDNESS DOCTRINE THIS IS LOCAL "
          "EVIDENCE, NOT A PROOF.**  A tangent count of one ray does not "
          "establish global uniqueness, and this receipt therefore does "
          "NOT state that I3 forces the form.  What it states is: the "
          "pin's §3 argument now has its measurement, and discharging "
          "that argument as a written proof is the remaining step.")
    print("  IF discharged, B2's restriction LIFTS: the form would be a "
          "consequence of a record-level demand rather than a postulate "
          "about the shape of Z, and D49's settlement would stop being "
          "conditional on a modelling choice.")
else:
    print("  DEPTH-STATIONARITY DOES **NOT** FORCE THE FORM: the "
          f"completion space retains dimension {stat_dims} at the reached "
          "depths.  Under the pin's one-sidedness doctrine this direction "
          "is RIGOROUS — nearby non-proportional completions satisfy I3 — "
          "so **the form is a genuine CHOICE, B2's restriction is "
          "PERMANENT, and every citation of D49 must carry it.**")
    print(f"  AND FOLIATION-INVARIANCE DOES NOT HELP: I5 = I3 + demand (b) "
          f"more than doubles the constraints and leaves the completion "
          f"dimension identical ({i5_dims}).  The residual freedom is not "
          f"gauge freedom.")
    print("  WHY THE PIN'S §3 SKETCH FAILED, diagnosed: it assumed the "
          "demand forces Z(h+e)/Z(h) to be a function of the two classes "
          "EVENT BY EVENT.  The record-level demand is AGGREGATED — it "
          "equates the class-to-class transfer SUMMED over events — so it "
          "constrains sums, not individual ratios, and the "
          "path-consistency step never gets its hypothesis.  The "
          "aggregated reading is the CORRECT one: what is observable is "
          "the probability of moving from class s to class s'; a "
          "per-event version would be a demand on unobservable labels, "
          "which is exactly what B2 disqualified.")
print("  UNTOUCHED EITHER WAY: D49's EXISTENCE result.  A root-free "
      "completion exists; horn (II) holds.  Nothing here bears on it.")
print("  SCOPE: d42a, delivery-free, two actors.  Transport scope remains "
      "open regardless.")

print(f"\n[d50] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("EXIT 1")
    sys.exit(1)
print("EXIT 0")

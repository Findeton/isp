#!/usr/bin/env python3
"""
d50_form_law_or_choice_exact.py — v10 D50: is paper 30 §5.7's stationary
FORM a law, or a choice?  Pin: note-d50-is-the-form-a-law-pin.md (STRICT,
LOG #421, committed before this file existed).

**ROUND-1 REVIEWED AND REPAIRED (2026-07-26).**  Independent hostile
review `v10/reviews/batch-round1-d50-to-d60.md` — REVISE, 1 BLOCKER /
1 MAJOR / 5 MINOR / 2 NIT.  The AST surgery is sound, the sweep runs, the
trend is real, and the unit's headline — depth-stationarity does not force
the form; the form is a choice; B2's restriction is permanent — survives
everything and is STRONGER than the first draft claimed.  What did not
survive is the arithmetic of the quantity the headline is stated in:

  * BLOCKER 1 — THE I2/I3/I5 CONSTRAINT ROWS WERE NOT THE DEMAND'S
    DIFFERENTIAL.  The demand F_c(b) = A_c(b)·Z_h1(b) − B_c(b)·Z_h0(b) is
    QUADRATIC in b; its differential needs the product rule in full, and
    the committed rows carried only the first and third terms.  (The same
    file got it right in the 'ren' branch — one demand was linearized
    correctly and the other was not.)  Corrected here, with an
    EXACT-IN-t certificate: F is quadratic, so (F(b*+v) − F(b*−v))/2 IS
    dF/dt|0 exactly, over Fractions, with no numerics.  **I3 completion
    dimensions are 12 / 32 / 125, not 10 / 28 / 107**, and **D49/B2's
    published bisimulation-free figure 119 becomes 137.**  SF0(b) is
    restated: it reproduces D49's 119 EXACTLY under D49's own
    linearization — which is why a port check could not catch this — and
    reports 137 as the corrected value.
  * MAJOR 1 — SF6, the negative control, was VACUOUS at two of its three
    depths: I1 imposes 0 constraints below depth 4, so `compdim > 0` was
    a theorem-pass there.  Restated to report exactly that: the
    instrument is validated at ONE depth, not three.
  * MINOR 1 — "MORE THAN DOUBLES" is false at two of the three depths
    (1.56x, 1.93x, 2.25x).  Restated to what the gate actually tests.
  * MINOR 2 — the one-sidedness doctrine was applied conservatively; the
    negative is CONSTRUCTIVE, not doctrinal.  SF3b exhibits an exact LINE
    of strictly-positive, genuinely different completions inside the I3
    variety.
  * MINOR 3 — SF3, the primary target, had a predicate that cannot fail;
    it is labelled a REPORTING gate and the falsifiable content moved to
    SF3b.
  * MINOR 4 — the pin's "non-optional" PYTHONHASHSEED determinism gate
    was never built.  SF8 builds it: this receipt re-runs ITSELF in probe
    mode under seeds 0/7/61/999 and compares.
  * MINOR 5 — the AST strip is now gated to bind no names.
  * NIT 1 — the depth-5 cap is now a measured artefact (the per-depth
    rank timings are printed), not a comment.
  * NIT 2 — rank(M) = NB − 1 at every depth and the 1-dimensional kernel
    IS the overall-scaling direction; stated and gated (SF9).

WHY THIS EXISTS.  D49 settled the completion dichotomy in favour of horn
(II) — a root-free completion EXISTS — and that result is untouched here.
What D49's round-1 BLOCKER B2 refuted was the account of UNIQUENESS: it
comes from a POSTULATED SHAPE for Z, not from any invariance stated on
the record.

THE ONE-SIDEDNESS DOCTRINE (pin §4, BINDING).  Tangent counts at b* are
LOCAL.  A count of 1 is LOCAL EVIDENCE ONLY.  A count > 1 modulo scaling
was declared "RIGOROUS in the negative"; round 1 pointed out that this is
not automatic at a singular point of the (quadratic) variety — and then
certified the stronger fact constructively.  SF3b carries that.

D49's computational state is imported by AST-stripping its module-level
check() and print() statements — single source, its gates are NOT re-run
and NOTHING is re-derived.  Exact Fractions throughout.
Exit 1 ONLY on anchor breakage (SF0) or instrument breakage (SF6/SF8).

Run from the repo root: python3 v10/code/d50_form_law_or_choice_exact.py
"""
import ast
import os
import subprocess
import sys
import time
from collections import defaultdict
from fractions import Fraction as Fr

sys.setrecursionlimit(300000)

PROBE = os.environ.get('D50_PROBE') == '1'
PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

if not PROBE:
    print("[D50 — is the stationary FORM a law, or a choice?  ROUND-1 "
          "REPAIRED]")
    print("  banner: D49's EXISTENCE result (horn II) is untouched by this")
    print("  receipt.  Only the account of UNIQUENESS is at issue.  **The")
    print("  I2/I3/I5 rows are CORRECTED: the committed linearization")
    print("  dropped half the product rule, so 10/28/107 becomes 12/32/125")
    print("  and B2's ported 119 becomes 137.**  D49's state is imported by")
    print("  AST-stripping its check()/print() statements — single source,")
    print("  gates not re-run.  ONE-SIDEDNESS (pin §4): a tangent count of")
    print("  1 is LOCAL EVIDENCE and never licenses 'forces'; the negative")
    print("  direction is carried CONSTRUCTIVELY by SF3b, not by doctrine.")

# =========================================================================
# SF0 — import D49's state, and reproduce B2's two numbers as a port check
# =========================================================================
if not PROBE:
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
_stripped = [n for n in _tree.body if _is_gate(n)]
def _module_binds(node):
    """Names a statement binds IN THE ENCLOSING SCOPE.  Comprehension
    and lambda bodies have their own scope in Python 3 and cannot leak,
    so they are not descended into; everything else is."""
    out, stack = [], [node]
    while stack:
        n = stack.pop()
        if isinstance(n, (ast.ListComp, ast.SetComp, ast.DictComp,
                          ast.GeneratorExp, ast.Lambda)):
            continue
        if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store):
            out.append(n.id)
        stack.extend(ast.iter_child_nodes(n))
    return out


_strip_binds = [n for n in _stripped if _module_binds(n)]
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


def _rref(rows, W):
    """Exact reduced row echelon form over Fractions.  Returns
    (A, pivots, rank).  D49's own _rank closes over its global NB = 313
    and therefore cannot be reused at other truncation depths."""
    A = [r[:] for r in rows]
    nr, rk, piv = len(A), 0, []
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
        piv.append(c)
        rk += 1
    return A, piv, rk


def _rank(rows):
    if not rows:
        return 0
    return _rref(rows, len(rows[0]))[2]


def _nullspace(rows, W):
    """Exact basis of {v : rows.v = 0}."""
    if not rows:
        return [[Fr(1) if j == i else Fr(0) for j in range(W)]
                for i in range(W)]
    A, piv, rk = _rref(rows, W)
    free = [c for c in range(W) if c not in set(piv)]
    out = []
    for f in free:
        v = [Fr(0)] * W
        v[f] = Fr(1)
        for i, c in enumerate(piv):
            v[c] = -A[i][f]
        out.append(v)
    return out


H3, _sub_e, V1 = ns['H3'], ns['_sub_e'], ns['V1']
FV = ns['FV']

if not PROBE:
    check("SF0(a) D49's computational state imported by AST-stripping its "
          "module-level check()/print() statements — single source, D49's "
          "own gates are NOT re-run here and nothing is re-derived.  "
          "ROUND-1 MINOR 5: the strip is now GATED to bind no "
          "ENCLOSING-SCOPE names (comprehension and lambda scopes cannot "
          "leak in Python 3 and are excluded), so the surgery provably "
          "cannot have removed a side effect the imported state depends on",
          all(k in ns for k in ('CACHE', 'BYLEN', 'cls_of', 'truncated_Z',
                                'H3', 'FV'))
          and len(BYLEN[4]) == 976
          and sum(len(BYLEN[d]) for d in range(5)) == 1191
          and _exits == 1 and not _strip_binds,
          f"statements kept = {len(_body)} of {len(_tree.body)}, stripped "
          f"= {len(_stripped)}, stripped statements that BIND a name = "
          f"{len(_strip_binds)}; histories AT depth 4 = {len(BYLEN[4])}, "
          f"cumulative through depth 4 = "
          f"{sum(len(BYLEN[d]) for d in range(5))}.  NOTE: paper 30's "
          f"much-quoted '1,191 histories' is the CUMULATIVE count "
          f"(1191 - 215 = 976 sit at the layer itself); this receipt's "
          f"first draft asserted 1191 at the layer and was wrong.  D49 "
          f"sys.exit calls stripped = {_exits}")


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
    return tcls, BAS, Zs, bst


def _groups(D, kind):
    """The (key -> member histories) grouping the bisimulation demands
    compare over.  'bis' groups by (DEPTH, class) — B2's I2, same-depth
    only; 'stat' by class alone — I3, DEPTH-STATIONARITY."""
    byc = defaultdict(list)
    for L in range(D):
        for hk in BYLEN[L]:
            key = (L, cls_of(hk)) if kind == 'bis' else cls_of(hk)
            byc[key].append(hk)
    return byc


def demand_rows(D, tcls, BAS, Zs, kind, lin='full'):
    """Tangent-space constraint rows at b* for a demand stated on the
    RECORD.  `kind`:
      'ren' — the root/renewal matched pair prices identically;
      'bis' — the completed class-to-class transfer is a function of the
              classes, comparing histories of the SAME depth (B2's I2);
      'stat'— the same, comparing histories of ANY depth (I3: DEPTH-
              STATIONARITY — the demand B2 never tested).
    `lin`:
      'full' — the CORRECT differential (round-1 BLOCKER 1);
      'd50'  — the committed linearization, kept so the published
               numbers can be reproduced and the error exhibited."""
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
        # Z.
        rows = demand_rows(D, tcls, BAS, Zs, 'stat', lin)
        bygauge = defaultdict(list)
        for L in range(D + 1):
            for hk in BYLEN[L]:
                bygauge[canon(list(hk))].append(hk)
        for _c, mem in bygauge.items():
            for hk in mem[1:]:
                rows.append([BAS[j][mem[0]] - BAS[j][hk] for j in range(NB)])
        return rows

    for key, mem in _groups(D, kind).items():
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
                # F_c(b) = A_c(b)·Z_h1(b) - B_c(b)·Z_h0(b),  QUADRATIC.
                # dF_c[v] = A_c(v)·Z_h1(b*) + A_c(b*)·Z_h1(v)
                #         - B_c(v)·Z_h0(b*) - B_c(b*)·Z_h0(v)
                Astar = sum((q * Zs[h0 + (e,)] for e, q in r0.get(c, [])),
                            Fr(0))
                Bstar = sum((q * Zs[h1 + (e,)] for e, q in r1.get(c, [])),
                            Fr(0))
                row = []
                for j in range(NB):
                    A_ = sum((q * BAS[j][h0 + (e,)]
                              for e, q in r0.get(c, [])), Fr(0))
                    B_ = sum((q * BAS[j][h1 + (e,)]
                              for e, q in r1.get(c, [])), Fr(0))
                    val = A_ * Zs[h1] - B_ * Zs[h0]
                    if lin == 'full':
                        val += Astar * BAS[j][h1] - Bstar * BAS[j][h0]
                    row.append(val)
                rows.append(row)
    return rows


def demand_residuals(D, Zd, kind='stat'):
    """The demand ITSELF (not its differential) evaluated at a boundary
    whose induced Z is `Zd`.  Used for the exact-in-t certificate and for
    SF3b's line-inside-the-variety test."""
    out = []
    for key, mem in _groups(D, kind).items():
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
                A_ = sum((q * Zd[h0 + (e,)] for e, q in r0.get(c, [])),
                         Fr(0))
                B_ = sum((q * Zd[h1 + (e,)] for e, q in r1.get(c, [])),
                         Fr(0))
                out.append(A_ * Zd[h1] - B_ * Zd[h0])
    return out


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


def perturbed_Z(D, bst, tcls, coeffs, t):
    """Z at the boundary b* + t.v, computed by truncated_Z on the
    perturbed boundary function (NOT by assuming linearity — SF3b gates
    the linearity separately)."""
    idx = {c: j for j, c in enumerate(tcls)}

    def bfun(hk):
        return bst[hk] + t * coeffs[idx[canon(list(hk))]]
    return truncated_Z(bfun, D)


# ---- the depth-2 objects, shared by the probe and the full run ---------
tcls2, BAS2, Zs2, bst2 = basis_and_Z(2)
rows2_full = demand_rows(2, tcls2, BAS2, Zs2, 'stat', 'full')
rows2_d50 = demand_rows(2, tcls2, BAS2, Zs2, 'stat', 'd50')
_probe_line = (f"NB2={len(tcls2)} tcls={repr(tcls2)[:0]}"
               f"{len(set(map(repr, tcls2)))} "
               f"rank_full={_rank(rows2_full)} "
               f"rank_d50={_rank(rows2_d50)} nrows={len(rows2_full)} "
               f"Zsum={sum(Zs2.values())} "
               f"Zdigest={sum(k * v for k, v in enumerate(Zs2[h] for h in sorted(Zs2, key=repr)))}")
if PROBE:
    print(_probe_line)
    sys.exit(0)

tcls4, BAS4, Zs4, bst4 = basis_and_Z(4)
NB4 = len(tcls4)
r_ren4 = _rank(demand_rows(4, tcls4, BAS4, Zs4, 'ren'))
r_bis4_d50 = _rank(demand_rows(4, tcls4, BAS4, Zs4, 'bis', 'd50'))
r_bis4_full = _rank(demand_rows(4, tcls4, BAS4, Zs4, 'bis', 'full'))
check("SF0(b) PORT CHECK, RESTATED BY ROUND 1.  B2's two published "
      "numbers are reproduced independently at depth-4 truncation — "
      "renewal-pair agreement leaves 308 of 313 boundary directions free, "
      "and bisimulation-invariance leaves 119 **under D49's own "
      "linearization**.  That reproduction is exact, and it is exactly "
      "why the port check could not catch BLOCKER 1: porting D49's "
      "METHOD ports its product-rule error with it, so the anchor "
      "CERTIFIES the error instead of detecting one.  **Under the "
      "corrected differential the same quantity is 137, and 137 is the "
      "number D49/B2's 119 must be forward-corrected to wherever it is "
      "quoted**",
      NB4 == 313 and NB4 - r_ren4 == 308
      and NB4 - r_bis4_d50 == 119 and NB4 - r_bis4_full == 137,
      f"boundary dim = {NB4}; renewal free = {NB4 - r_ren4}; "
      f"bisimulation free under D49's linearization = "
      f"{NB4 - r_bis4_d50} (= B2's published 119); under the CORRECTED "
      f"differential = {NB4 - r_bis4_full}")

# =========================================================================
# SF0(c) — the exact-in-t certificate for BLOCKER 1
# =========================================================================
print("\n[SF0(c) the EXACT-IN-t certificate — which linearization is the "
      "demand's differential?]")
print("  F_c is QUADRATIC in b, so along b* + t.v the function t -> F_c")
print("  is a quadratic polynomial and (F(b*+v) - F(b*-v))/2 IS dF/dt|0")
print("  EXACTLY, over Fractions, with no numerics.  Compare each")
print("  linearization's row, dotted with v, against that exact value.")
_s = 20260726
_dir = []
for _ in range(len(tcls2)):
    _s = (1103515245 * _s + 12345) % (1 << 31)
    _dir.append(Fr((_s % 13) - 6, 1 + (_s >> 8) % 5))
Zp = perturbed_Z(2, bst2, tcls2, _dir, Fr(1))
Zm = perturbed_Z(2, bst2, tcls2, _dir, Fr(-1))
_lin_check = all(Zp[hk] - Zs2[hk] == sum(_dir[j] * BAS2[j][hk]
                                         for j in range(len(tcls2)))
                 for hk in Zs2)
res_p = demand_residuals(2, Zp)
res_m = demand_residuals(2, Zm)
exact_dF = [(a - b) / 2 for a, b in zip(res_p, res_m)]
dot_full = [sum(r[j] * _dir[j] for j in range(len(tcls2)))
            for r in rows2_full]
dot_d50 = [sum(r[j] * _dir[j] for j in range(len(tcls2)))
           for r in rows2_d50]
m_full = sum(1 for a, b in zip(dot_full, exact_dF) if a == b)
m_d50 = sum(1 for a, b in zip(dot_d50, exact_dF) if a == b)
res0 = demand_residuals(2, Zs2)
off_variety = sum(1 for x in res0 if x != 0)
print(f"  rows tested = {len(exact_dF)};  b* OFF the demand variety "
      f"(residual != 0) in {off_variety}")
print(f"  d50's row . v  == dF/dt|0  in  {m_d50}/{len(exact_dF)}")
print(f"  FULL  row . v  == dF/dt|0  in  {m_full}/{len(exact_dF)}")
check("SF0(c) [THE CERTIFICATE FOR BLOCKER 1] The committed rows are NOT "
      "the demand's differential and the corrected rows ARE, decided "
      "exactly and not by inspection.  b* sits EXACTLY on the demand "
      "variety (residual 0 at every row), so the tangent-space framing "
      "is legitimate; only the tangent was miscomputed.  The 'ren' "
      "branch of the same function was always correct — one demand was "
      "linearized correctly and the other was not, in the same file",
      m_full == len(exact_dF) and m_d50 < m_full and off_variety == 0
      and _lin_check,
      f"rows tested = {len(exact_dF)}; FULL matches {m_full}, committed "
      f"matches {m_d50}; b* off-variety rows = {off_variety}; "
      f"truncated_Z linear in the boundary = {_lin_check}")

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
# and a boundary dimension in the thousands; round-1 NIT 1 asked for the
# cap to be a measured artefact rather than a comment, so the per-depth
# rank cost is timed and printed below and the extrapolation is on the
# record.
DEPTH_CAP = 4
DEPTHS = [2, 3, 4]
SWEEP = {}
TIMING = {}
BASES = {}
for D in DEPTHS:
    t0 = time.time()
    tcls, BAS, Zs, bst = basis_and_Z(D)
    BASES[D] = (tcls, BAS, Zs, bst)
    NB = len(tcls)
    Mrows = completion_rows(D, tcls, BAS, Zs)
    r_M = _rank(Mrows)
    row = {'NB': NB, 'rank_M': r_M, 'nM': len(Mrows)}
    for kind in ('ren', 'bis', 'stat', 'stat+fol'):
        dr = demand_rows(D, tcls, BAS, Zs, kind, 'full')
        r_d = _rank(dr)
        # dim(image of M restricted to V) = rank([demand; M]) - rank(demand)
        r_both = _rank(dr + Mrows) if dr else r_M
        row[kind] = {'constraints': len(dr), 'rank': r_d,
                     'free': NB - r_d, 'compdim': r_both - r_d}
    for kind in ('bis', 'stat'):
        dr = demand_rows(D, tcls, BAS, Zs, kind, 'd50')
        r_d = _rank(dr)
        r_both = _rank(dr + Mrows) if (dr and kind == 'stat') else None
        row[kind + '@d50'] = {
            'constraints': len(dr), 'rank': r_d, 'free': NB - r_d,
            'compdim': (r_both - r_d) if r_both is not None else None}
    SWEEP[D] = row
    TIMING[D] = time.time() - t0
    print(f"  D = {D}: boundary dim = {NB}, completion-map rank = {r_M} "
          f"(= NB - 1: the 1-dimensional kernel is the overall-scaling "
          f"direction, SF9), rows in M = {len(Mrows)}   "
          f"[{TIMING[D]:.1f}s]")
    for kind, name in (('ren', 'I1 renewal agreement       '),
                       ('bis', 'I2 bisimulation (same D)   '),
                       ('stat', 'I3 DEPTH-STATIONARITY      '),
                       ('stat+fol', 'I5 = I3 + foliation-invar. ')):
        c = row[kind]
        print(f"      {name}: {c['constraints']:6d} constraints, "
              f"boundary-free {c['free']:4d}/{NB}, "
              f"COMPLETION dim {c['compdim']}")

print("\n  THE CORRECTION TABLE (round-1 BLOCKER 1) — committed "
      "linearization vs the demand's actual differential:")
print("   D   NB rankM | kind   d50rank d50free d50comp |  FULLrank "
      "FULLfree FULLcomp")
for D in DEPTHS:
    r = SWEEP[D]
    for kind in ('bis', 'stat'):
        a, b = r[kind + '@d50'], r[kind]
        print(f"  {D:2d} {r['NB']:4d} {r['rank_M']:4d} | {kind:5s} "
              f"{a['rank']:7d} {a['free']:7d} "
              f"{('%d' % a['compdim']) if a['compdim'] is not None else '  -':>7} "
              f"| {b['rank']:9d} {b['free']:8d} {b['compdim']:8d}")

stat_dims = [SWEEP[D]['stat']['compdim'] for D in DEPTHS]
stat_dims_d50 = [SWEEP[D]['stat@d50']['compdim'] for D in DEPTHS]
i5_dims = [SWEEP[D]['stat+fol']['compdim'] for D in DEPTHS]
bis_dims = [SWEEP[D]['bis']['compdim'] for D in DEPTHS]
ren_dims = [SWEEP[D]['ren']['compdim'] for D in DEPTHS]

check("SF1 the sweep ran at every reached depth and reported BOTH "
      "dimensions, never conflating them (B1's lesson: a boundary "
      "direction can be free and still move the completion).  ROUND-1 "
      "NIT 1: the depth cap is now a MEASURED artefact — the per-depth "
      "cost is printed, and D = 5 (5,280 layer histories, boundary "
      "dimension in the thousands) is cut against that measured trend, "
      "not against a comment",
      len(SWEEP) == len(DEPTHS) and all(SWEEP[D]['NB'] > 0 for D in DEPTHS),
      f"depths reached = {DEPTHS} (printed, not silently capped); "
      f"boundary dims = {[SWEEP[D]['NB'] for D in DEPTHS]}; wall-clock "
      f"per depth = {[f'{TIMING[D]:.1f}s' for D in DEPTHS]}; declared "
      f"cap = {DEPTH_CAP}")

I3_FORCES = all(d == 0 for d in stat_dims)
check("SF3 [THE PRIMARY TARGET — REPORTING GATE, labelled per round-1 "
      "MINOR 3] DEPTH-STATIONARITY, decided at every reached depth.  I3 "
      "demands that the same class-to-class step carry the same "
      "probability WHENEVER it happens — a statement about the record, "
      "not about Z, and the one B2's same-depth grouping never tested.  "
      "This gate REPORTS the completion dimension in whichever direction "
      "it came out; its predicate is `stat_dims is non-empty` and cannot "
      "fail, which is legitimate under the pin's exit-0-either-way "
      "falsifier but is now SAID.  **The falsifiable content lives in "
      "SF3b.**  ROUND-1 BLOCKER 1: the published dims were 10/28/107 "
      "under the defective linearization",
      True if stat_dims else False,
      f"I3 completion dims by depth {DEPTHS} = {stat_dims} (committed, "
      f"defective linearization: {stat_dims_d50}) -> "
      f"{'ONE RAY at every reached depth' if I3_FORCES else 'MORE THAN ONE RAY — I3 does NOT force the form'}")

# =========================================================================
# SF3b — the CONSTRUCTIVE negative (round-1 MINOR 2)
# =========================================================================
print("\n[SF3b the negative, CONSTRUCTIVELY — round-1 MINOR 2]")
print("  The pin declared a completion count > 1 'RIGOROUS in the")
print("  negative'.  That is not automatic: a kernel of the")
print("  linearization exhibits a nearby SOLUTION only at a regular")
print("  point of the (quadratic) variety, and the receipt never argued")
print("  regularity.  The stronger fact is true and cheap, and is")
print("  certified here: SOME kernel directions generate an exact LINE")
print("  inside the variety — and not all do, which is precisely round")
print("  1's point.  Along b* + t.v with v in the kernel, F(b*+t.v) =")
print("  t^2.Q(v), so the line lies in the variety iff Q(v) = 0; the")
print("  kernel basis is SEARCHED for such a v.  The COUNT of qualifying")
print("  basis vectors is BASIS-DEPENDENT (the RREF basis follows the")
print("  terminal-class ordering) and is deliberately not reported as a")
print("  number; the two facts below are basis-free.")
print("  Vanishing at four distinct t (0, 1, 1/3, 2) then makes the")
print("  quadratic identically zero — no numerics, no regularity")
print("  assumption.")
LINE = {}
for D in (2, 3):
    tcls, BAS, Zs, bst = BASES[D]
    NB = len(tcls)
    dr = demand_rows(D, tcls, BAS, Zs, 'stat', 'full')
    Mrows = completion_rows(D, tcls, BAS, Zs)
    nres = len(demand_residuals(D, Zs))
    kern = _nullspace(dr, NB)
    # F(b* + t.v) = F(b*) + t.dF[v] + t^2.Q(v) = t^2.Q(v) for v in the
    # kernel, so the line lies in the variety iff Q(v) = 0.  Two
    # BASIS-FREE facts are extracted: (i) such a v EXISTS and moves the
    # completion; (ii) Q is NOT identically zero on the kernel, i.e. not
    # every tangent direction integrates — which is exactly round-1
    # MINOR 2's objection, conceded and then answered.  The COUNT of
    # qualifying basis vectors is basis-dependent (the RREF basis depends
    # on the terminal-class ordering) and is deliberately NOT reported as
    # a number.
    wit, Qnonzero = None, False
    for v in kern:
        Zt = perturbed_Z(D, bst, tcls, v, Fr(1))
        zero = all(x == 0 for x in demand_residuals(D, Zt))
        if not zero:
            Qnonzero = True
        elif wit is None and any(sum(r[j] * v[j] for j in range(NB)) != 0
                                 for r in Mrows):
            wit = v
    hits = []
    for t in (Fr(1), Fr(1, 3), Fr(2)):
        Zt = perturbed_Z(D, bst, tcls, wit, t)
        hits.append((t, sum(1 for x in demand_residuals(D, Zt) if x != 0)))
    # the perturbation scale is chosen from a DECLARED descending list,
    # the first at which Z stays strictly positive; printed, never silent
    tsmall, Zsm, pos = None, None, False
    for t in (Fr(1, 10), Fr(1, 50), Fr(1, 200), Fr(1, 1000)):
        Zc = perturbed_Z(D, bst, tcls, wit, t)
        if all(z > 0 for z in Zc.values()):
            tsmall, Zsm, pos = t, Zc, True
            break
    diff = pos and any(Zsm[hk + (e,)] * Zs[hk] != Zs[hk + (e,)] * Zsm[hk]
                       for L in range(D) for hk in BYLEN[L]
                       for e, q in CACHE[hk])
    LINE[D] = (len(kern), hits, nres, tsmall, pos, diff, Qnonzero)
    print(f"  D={D}: nullspace dim={len(kern)}; a kernel direction that "
          f"MOVES the completion AND generates an exact line EXISTS = "
          f"{wit is not None}; Q not identically zero on the kernel (so "
          f"NOT every tangent direction integrates) = {Qnonzero}")
    print(f"        EXACT I3 residual on b*+t.v : "
          + ",  ".join(f"t={t}: {bad}/{nres} violated" for t, bad in hits))
    print(f"        at t={tsmall} (first of the declared list 1/10, 1/50, "
          f"1/200, 1/1000 keeping Z > 0): Z > 0 everywhere = {pos}; "
          f"completion DIFFERS from b* = {diff}")
_line_ok = all(all(bad == 0 for _, bad in LINE[D][1]) and LINE[D][4]
               and LINE[D][5] for D in (2, 3))
check("SF3b [THE FALSIFIABLE HALF OF THE PRIMARY TARGET] THE NEGATIVE IS "
      "CONSTRUCTIVE, NOT DOCTRINAL.  There is an exact one-parameter "
      "family of STRICTLY POSITIVE, GENUINELY DIFFERENT completions "
      "satisfying depth-stationarity: a kernel direction of the "
      "corrected rows generates a line on which every I3 residual "
      "vanishes at four distinct parameter values, hence identically "
      "(F is quadratic along the line).  This is materially stronger "
      "than a tangent count and it is what the unit is entitled to.  A "
      "receipt whose I3 variety really were a single ray would fail this "
      "gate",
      _line_ok and LINE[2][6] and LINE[3][6],
      f"D=2: kernel dim {LINE[2][0]}; residual 0 at t in "
      f"{[str(t) for t, _ in LINE[2][1]]} over {LINE[2][2]} rows, "
      f"strictly positive and distinct at t={LINE[2][3]}; Q not "
      f"identically zero on the kernel = {LINE[2][6]}.  D=3: kernel dim "
      f"{LINE[3][0]}; 0 over {LINE[3][2]} rows, strictly positive and "
      f"distinct at t={LINE[3][3]}; Q not identically zero = "
      f"{LINE[3][6]}")

_ratios = [Fr(SWEEP[D]['stat+fol']['constraints'],
              SWEEP[D]['stat']['constraints']) for D in DEPTHS]
check("SF4 [THE SHARPER HALF] FOLIATION-INVARIANCE ADDS NOTHING.  I5 = "
      "I3 + paper 30 demand (b) in its Z-level sufficient form STRICTLY "
      "INCREASES the constraint count at every depth and leaves the "
      "completion dimension EXACTLY UNCHANGED — under BOTH "
      "linearizations, so the conclusion is linearization-independent.  "
      "ROUND-1 MINOR 1: the committed label said 'MORE THAN DOUBLES', "
      "which is false at two of the three depths (the true factors are "
      f"{[f'{float(x):.2f}x' for x in _ratios]}); the gate's predicate "
      "was always the correct one",
      i5_dims == stat_dims and all(
          SWEEP[D]['stat+fol']['constraints']
          > SWEEP[D]['stat']['constraints'] for D in DEPTHS),
      f"I3 = {stat_dims}, I5 = {i5_dims} (identical); constraint counts "
      f"I3 -> I5 = "
      f"{[(D, SWEEP[D]['stat']['constraints'], SWEEP[D]['stat+fol']['constraints']) for D in DEPTHS]}"
      f"; factors {[f'{float(x):.2f}' for x in _ratios]}")

check("SF2 THE TREND, reported in whichever direction it came out: I2 "
      "(same-depth bisimulation) against I3 (depth-stationarity) at the "
      "same depths.  If I3 collapses the completion space while I2 does "
      "not, the missing ingredient is exactly the cross-depth comparison",
      len(bis_dims) == len(stat_dims),
      f"I2 completion dims = {bis_dims}; I3 completion dims = "
      f"{stat_dims}; I1 = {ren_dims}")

# =========================================================================
# SF6 — the negative control
# =========================================================================
print("\n[SF6 negative control]")
_i1_live = [D for D in DEPTHS if SWEEP[D]['ren']['constraints'] > 0]
check("SF6 [RESTATED BY ROUND 1 — MAJOR 1: THE CONTROL IS VACUOUS AT TWO "
      "OF ITS THREE DEPTHS] I1 (renewal-pair agreement alone) must stay "
      "LOOSE where it is a constraint at all — B2 measured it at 308 of "
      "313 free, and a demand that weak must not collapse the completion "
      "space.  **I1 imposes ZERO constraints below depth 4** (the "
      "renewal pair H3/h2e does not exist in a depth-2 or depth-3 "
      "truncation), so at D = 2 and D = 3 `compdim = rank(M) = NB - 1` "
      "is FORCED and the committed gate was a theorem-pass there.  The "
      "instrument is validated at ONE depth, and the predicate now says "
      "so by testing only the depths where I1 is live",
      len(_i1_live) > 0
      and all(SWEEP[D]['ren']['compdim'] > 0 for D in _i1_live),
      f"I1 constraint counts by depth = "
      f"{[(D, SWEEP[D]['ren']['constraints']) for D in DEPTHS]}; depths "
      f"where I1 is LIVE = {_i1_live}; I1 completion dims = {ren_dims}; "
      f"I1 boundary-free = {[SWEEP[D]['ren']['free'] for D in DEPTHS]}; "
      f"at the vacuous depths compdim = rank(M) = NB - 1 = "
      f"{[SWEEP[D]['NB'] - 1 for D in DEPTHS if D not in _i1_live]}")

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
      "grouping omitted, and its RANK is strictly higher too under both "
      "linearizations.  Had the two produced identical systems, this "
      "unit would be re-measuring B2 and its result would be vacuous",
      live and all(SWEEP[D]['stat']['rank'] > SWEEP[D]['bis']['rank']
                   for D in DEPTHS),
      f"constraint counts I2 -> I3 by depth: "
      f"{[(D, SWEEP[D]['bis']['constraints'], SWEEP[D]['stat']['constraints']) for D in DEPTHS]}"
      f"; ranks I2 -> I3: "
      f"{[(D, SWEEP[D]['bis']['rank'], SWEEP[D]['stat']['rank']) for D in DEPTHS]}")

# =========================================================================
# SF9 — what rank(M) = NB - 1 means (round-1 NIT 2)
# =========================================================================
print("\n[SF9 the completion-map rank, and what its kernel IS]")
tcls, BAS, Zs, bst = BASES[2]
Mk = _nullspace(completion_rows(2, tcls, BAS, Zs), len(tcls))
_kerZ = None
if len(Mk) == 1:
    V = {hk: sum(Mk[0][j] * BAS[j][hk] for j in range(len(tcls)))
         for hk in Zs}
    keys = sorted(Zs, key=repr)
    _kerZ = all(V[a] * Zs[b] == V[b] * Zs[a] for a, b in
                zip(keys, keys[1:]))
print(f"  rank(M) = NB - 1 at every depth: "
      f"{[(D, SWEEP[D]['rank_M'], SWEEP[D]['NB'] - 1) for D in DEPTHS]}")
print(f"  at D = 2 the kernel is 1-dimensional and its induced Z-field is "
      f"PROPORTIONAL to Z(b*): {_kerZ}")
check("SF9 [ROUND-1 NIT 2 — the reading the receipt relied on and never "
      "stated] rank(M) = NB - 1 at every depth, so the completion map "
      "has a 1-dimensional kernel, and that kernel is EXACTLY the "
      "overall-scaling direction (its induced Z-field is proportional to "
      "Z(b*) pointwise).  That is WHY 'compdim = 0 <=> one ray' is the "
      "right reading of the quantity the headline is stated in",
      all(SWEEP[D]['rank_M'] == SWEEP[D]['NB'] - 1 for D in DEPTHS)
      and len(Mk) == 1 and _kerZ,
      f"(D, rank M, NB-1) = "
      f"{[(D, SWEEP[D]['rank_M'], SWEEP[D]['NB'] - 1) for D in DEPTHS]}; "
      f"kernel dim at D=2 = {len(Mk)}; kernel is the scaling direction = "
      f"{_kerZ}")

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
      "which is what SF6's negative control and SF3b are for.  SF3's "
      "predicate is run-bound and still cannot fail — which is why it is "
      "LABELLED a reporting gate (round-1 MINOR 3), the scan's declared "
      "blind spot",
      len(_ch) >= 9 and not _vac,
      f"check() calls = {len(_ch)}, bare/unbound = {len(_vac)}")

# =========================================================================
# SF8 — the pinned determinism gate (round-1 MINOR 4)
# =========================================================================
print("\n[SF8 determinism across PYTHONHASHSEED — the pin's "
      "'non-optional' clause, built]")
SEEDS = ('0', '7', '61', '999')
_env = dict(os.environ)
_env['D50_PROBE'] = '1'
_procs = []
for s in SEEDS:
    e = dict(_env)
    e['PYTHONHASHSEED'] = s
    _procs.append((s, subprocess.Popen(
        [sys.executable, 'v10/code/d50_form_law_or_choice_exact.py'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=e)))
_out = {}
for s, p in _procs:
    o, _e = p.communicate()
    _out[s] = (p.returncode, o.decode().strip())
for s in SEEDS:
    print(f"  PYTHONHASHSEED={s:>3}: rc={_out[s][0]}  {_out[s][1]}")
_det = len({_out[s][1] for s in SEEDS}) == 1 and all(
    _out[s][0] == 0 for s in SEEDS)
check("SF8 DETERMINISM GATED ACROSS PYTHONHASHSEED 0/7/61/999 — the pin "
      "§5 SF7 clause marked NON-OPTIONAL (D49's own A4 defect, where raw "
      "frozenset reprs were hash-order dependent, is what makes it so) "
      "and silently dropped from the committed receipt.  This receipt "
      "re-runs ITSELF in probe mode under each seed and compares the "
      "depth-2 boundary dimension, both linearizations' ranks, the row "
      "count and the exact sum of Z",
      _det,
      f"seeds {list(SEEDS)}; distinct probe outputs = "
      f"{len({_out[s][1] for s in SEEDS})}; all rc 0 = "
      f"{all(_out[s][0] == 0 for s in SEEDS)}")

# ============================== verdict ==================================
print("\n[VERDICT — D50, ROUND-1 REPAIRED]")
if I3_FORCES:
    print("  DEPTH-STATIONARITY COLLAPSES THE COMPLETION SPACE TO ONE RAY "
          "at every reached depth, while same-depth bisimulation "
          f"(I2 = {bis_dims}) and renewal agreement (I1 = {ren_dims}) do "
          "not.  The missing ingredient is exactly the CROSS-DEPTH "
          "comparison.")
    print("  **UNDER THE PIN'S ONE-SIDEDNESS DOCTRINE THIS IS LOCAL "
          "EVIDENCE, NOT A PROOF.**")
else:
    print("  DEPTH-STATIONARITY DOES **NOT** FORCE THE FORM: the "
          f"completion space retains dimension {stat_dims} at the reached "
          "depths.  **The direction is not merely 'rigorous by doctrine': "
          "SF3b exhibits an EXACT LINE of strictly positive, genuinely "
          "different completions inside the I3 variety.**  So **the form "
          "is a genuine CHOICE, B2's restriction is PERMANENT, and every "
          "citation of D49 must carry it.**")
    print(f"  THE NUMBERS, CORRECTED BY ROUND 1: I3 completion dimensions "
          f"are {stat_dims}, not the published {stat_dims_d50}; D49/B2's "
          f"bisimulation-free figure at depth 4 is "
          f"{SWEEP[4]['bis']['free']}, not the published "
          f"{SWEEP[4]['bis@d50']['free']}, and that correction must be "
          f"carried wherever 119 is quoted.  The corrected dimensions are "
          f"LARGER, still monotone, still far from 0 — so the conclusion "
          f"STRENGTHENS: I3 fails to force the form more freely than the "
          f"first draft reported.")
    print(f"  AND FOLIATION-INVARIANCE DOES NOT HELP: I5 = I3 + demand (b) "
          f"strictly increases the constraints and leaves the completion "
          f"dimension identical ({i5_dims}), under both linearizations.  "
          f"The residual freedom is not gauge freedom.")
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

#!/usr/bin/env python3
"""
d58_atlas_instrument_exact.py — v10 D58: the atlas instrument.
Pin: note-d58-atlas-instrument-pin.md (STRICT, LOG #438, before code).

**ROUND-1 REVIEWED AND REPAIRED (2026-07-26).**  Independent hostile
review `v10/reviews/batch-round1-d50-to-d60.md` — REVISE, 1 BLOCKER /
2 MAJOR / 5 MINOR / 3 NIT.  The entire atlas was rebuilt independently
and every committed number reproduced exactly.  A2's homogeneity gap
survives every correction and is the unit's durable content.  The overlap
half does not survive as published:

  * BLOCKER 1 — THE M^{3+1} CONTROL WAS NOT A SPRINKLING.  `latt4` drew
    from an LCG's low bits; at box = 32 the committed control was **32
    distinct points wearing 120 labels**, 8 spatial values per axis, mean
    chart width 15.0 against 3.3-5.2 for genuine records.  The control is
    rebuilt here on the repaired generator (single source: d55c), and the
    flagged "FINDING CANDIDATE" (M21 0.12 vs M31 0.54) **REVERSES**:
    against genuine M^{3+1} at the same N the mean overlap is BELOW
    M21's.  The residue is closed, with the sign flipped, and the density
    diagnosis was wrong.
  * MAJOR 1 — the pin's premise "for a cover pair the two chart sets live
    at the SAME height layer" is FALSE: it holds iff h[e'] - h[e] = 1,
    and 61% of M21's measured cover pairs have gap >= 2 and contribute a
    STRUCTURAL ZERO.  The gap census is now reported and the statistic is
    reported both unconditioned and conditioned on gap 1.
  * MAJOR 2 — omega is not a two-way overlap.  A1b proves and verifies
    the CONTAINMENT THEOREM: at gap 1 the successor chart is CONTAINED in
    the source chart, otherwise the intersection is empty.  So omega is a
    CHART-SIZE RATIO along covers, the Jaccard index equals it
    identically, and "the transition is the identity on their
    intersection" has nothing to act on.  omega systematically favours
    THIN-charted records — which is the D60 asymmetry.
  * MINOR 1 — the |D| >= 4 column was computed at every record and never
    compared.  A4 compares it; it is the column that qualifies D60.
  * MINOR 2 — the overlap population is conditioned on the SOURCE chart
    only; sample sizes now annotate every mean (WALK's 1.00 is 2 pairs).
  * MINOR 3 — A2's predicate could not fail; it now gates the
    pre-registered comparison itself.
  * MINOR 4 — the "sprinkling homogeneity floor 0.64" was a two-point
    floor over two records, one of them invalid.  It is now a measured
    BAND over eleven genuine configurations.
  * MINOR 5 — no result note; `note-d58-atlas-instrument-result.md`
    written with this repair.
  * NIT 1 / NIT 2 — every reported figure now carries its exact Fraction;
    the floor-rounded percentages that became D60's hard-coded
    comparators are gone (D60 imports the Fractions from here).

Charts = SKY-B(d) direction sets; homogeneity profile over all events;
overlap on cover pairs, reported with its gap census.  Controls
(sprinklings) validated BEFORE grammar records.  Exit 1 only on anchor
breakage.
"""
import ast, sys
from collections import defaultdict, Counter
from fractions import Fraction as Fr
from itertools import combinations, permutations, product
sys.setrecursionlimit(300000)
PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

print("[D58 — the atlas instrument, ROUND-1 REPAIRED]")
print("  banner: omega(e,e') = |D_e(d) & D_e'(d-1)| / |D_e(d)| on cover")
print("  pairs; homogeneity = the |D_e(d)| profile.  Round 1 showed the")
print("  M^{3+1} control was a degenerate point set and that omega is a")
print("  CHART-SIZE RATIO (containment theorem, A1b), not a two-way")
print("  overlap; both are carried below.  Controls first (a failing")
print("  control convicts the INSTRUMENT).  Exact Fractions; orderings")
print("  reported whichever way they land.")

def extract(path, marker, names, extra=None):
    t = ast.parse(open(path).read())
    keep = [n for n in t.body if isinstance(n, (ast.FunctionDef,
            ast.ClassDef)) or (isinstance(n, ast.Assign)
            and any(isinstance(x, ast.Name) and x.id in names
                    for x in n.targets))]
    g = {'Fr': Fr, 'combinations': combinations,
         'permutations': permutations, 'product': product,
         'defaultdict': defaultdict, 'sys': sys}
    if extra:
        g.update(extra)
    exec(compile(ast.fix_missing_locations(ast.Module(body=keep,
         type_ignores=[])), marker, 'exec'), g)
    return g

g47 = extract('v10/code/d47a_sky_instrument_exact.py', 'd47a',
              ('CYCLIC_CAP', 'SKYB_DEPTH'))
sky, mink3, latt3 = g47['sky'], g47['mink_order'], g47['lattice_points']
heights = g47['heights']
g55c = extract('v10/code/d55c_m31_control_exact.py', 'd55c', ())
mink4, latt = g55c['mink4'], g55c['latt']
latt4_committed = g55c['latt4_committed']

_st = open('v10/code/d42b1_transport_exact.py').read()
nst = {}
exec(_st[:_st.index('print("[d42b1')], nst)
candidates_for, event_poset, V0 = (nst['candidates_for'],
                                   nst['event_poset'], nst['V0'])
g55 = extract('v10/code/d55_shatter5_exact.py', 'd55', (),
              extra={'candidates_for': candidates_for,
                     'event_poset': event_poset, 'V0': V0})
build = g55['build']
poset_of = g55['poset_of']

check("A0 anchors: sky/mink3/heights from committed d47a; mink4 and the "
      "ROUND-1 REPAIRED sprinkling generator `latt` from d55c (single "
      "source for the generator fix — the committed low-bit draw is also "
      "imported, as `latt4_committed`, so the degeneracy can be "
      "EXHIBITED rather than asserted); the general builder from "
      "committed d55; the transport layer from committed d42b1 — all "
      "single sources via AST extraction",
      all(callable(f) for f in (sky, mink3, mink4, latt,
                                latt4_committed, build)),
      "extractions loaded")


def covers(C):
    n = len(C)
    out = []
    for i in range(n):
        for j in range(n):
            if C[i][j] and not any(C[i][k] and C[k][j] for k in range(n)):
                out.append((i, j))
    return out


def atlas(C, name, quiet=False):
    """Per depth d: the chart-width profile, and the overlap statistic
    with its HEIGHT-GAP census (round-1 MAJOR 1) and the containment /
    Jaccard checks (round-1 MAJOR 2).  Every mean is reported with the
    size of the population it is a mean over (round-1 MINOR 2)."""
    n = len(C)
    cov = covers(C)
    h = heights(C)
    res = {}
    for d in (2, 3):
        widths = []
        DIRS = {}
        for e in range(n):
            dirs, _ = sky(C, e, 'B', d)
            DIRS[e] = set(dirs)
            widths.append(len(dirs))
        om, om1 = [], []
        gaps = Counter()
        cont_ok = jac_ok = True
        for (e, e2) in cov:
            if len(DIRS[e]) < 2:
                continue
            gap = h[e2] - h[e]
            gaps[gap] += 1
            d2, _ = sky(C, e2, 'B', d - 1)
            S2 = set(d2)
            inter = DIRS[e] & S2
            union = DIRS[e] | S2
            om.append(Fr(len(inter), len(DIRS[e])))
            if union and Fr(len(inter), len(union)) != om[-1]:
                jac_ok = False
            if gap == 1:
                if not S2 <= DIRS[e]:
                    cont_ok = False
                om1.append(Fr(len(inter), len(DIRS[e])))
            elif inter:
                cont_ok = False
        w2 = sum(1 for w in widths if w >= 2)
        w4 = sum(1 for w in widths if w >= 4)
        mo = (sum(om) / len(om)) if om else None
        mo1 = (sum(om1) / len(om1)) if om1 else None
        res[d] = {'n': n, 'w2': w2, 'w4': w4, 'h2': Fr(w2, n),
                  'h4': Fr(w4, n), 'max': max(widths),
                  'mean': Fr(sum(widths), n), 'pairs': len(om),
                  'om': mo, 'pairs1': len(om1), 'om1': mo1,
                  'gaps': dict(sorted(gaps.items())),
                  'cont': cont_ok, 'jac': jac_ok}
        if not quiet:
            r = res[d]
            print(f"  {name} d={d}: events={n}, |D|>=2 at {w2} "
                  f"({r['h2']} = {float(r['h2']):.4f}), |D|>=4 at {w4} "
                  f"({r['h4']} = {float(r['h4']):.4f}), mean|D|="
                  f"{float(r['mean']):.2f}, max={r['max']}")
            print(f"      cover pairs measured={len(om)}, mean omega="
                  f"{mo} (~{float(mo):.4f})" if mo is not None
                  else f"      cover pairs measured=0")
            if mo is not None:
                print(f"      height-gap census {r['gaps']}; GAP-1 ONLY: "
                      f"{len(om1)} pairs, mean omega={mo1} "
                      f"(~{float(mo1):.4f}); structural-zero share "
                      f"{Fr(len(om) - len(om1), len(om))} "
                      f"(~{float(Fr(len(om) - len(om1), len(om))):.4f})")
    return res


# ------------------------------------------------------- controls first
print("\n[controls first — sprinklings.  BLOCKER 1: the committed "
      "M^{3+1} control is rebuilt on the repaired generator]")
R = {}
C21 = mink3(latt3(120, box=60))
R['M21'] = atlas(C21, 'M21 N=120 box=60 (committed, 2+1)')
C31D = mink4(latt4_committed(120, 32, 8))
_dgen = len(set(latt4_committed(120, 32, 8)))
print(f"  --- the COMMITTED M^{{3+1}} control, kept only as an exhibit: "
      f"{_dgen} distinct points wearing 120 labels ---")
R['M31DEGEN'] = atlas(C31D, 'M31 N=120 box=32 [DEGENERATE]')
C31 = mink4(latt(120, 3, 40, 8))
R['M31'] = atlas(C31, 'M31 N=120 box=40 (REPAIRED, 3+1)')

print("\n[the corrected sprinkling family — round-1 MINOR 4: the "
      "homogeneity 'floor' was a two-point floor over two records, one "
      "of them invalid.  Eleven genuine configurations:]")
FAMILY = {}
for box in (30, 40, 60, 90):
    FAMILY[('M21', box)] = atlas(mink4(latt(120, 2, box, 8)),
                                 f'M21 box={box}', quiet=True)
for box in (20, 24, 40, 48, 60, 90):
    FAMILY[('M31', box)] = atlas(mink4(latt(120, 3, box, 8)),
                                 f'M31 box={box}', quiet=True)
FAMILY[('M21', 'd47a')] = R['M21']
for k in sorted(FAMILY, key=repr):
    r = FAMILY[k][2]
    print(f"    {k[0]} box={k[1]:>5}: homog {float(r['h2']):.4f} "
          f"(|D|>=4 {float(r['h4']):.4f}), mean|D| {float(r['mean']):.2f}"
          f", max {r['max']:2d}, mean omega {float(r['om']):.4f} "
          f"over {r['pairs']} pairs")
HOM = sorted(FAMILY[k][2]['h2'] for k in FAMILY)
OMS = sorted(FAMILY[k][2]['om'] for k in FAMILY)
OM31 = sorted(FAMILY[k][2]['om'] for k in FAMILY if k[0] == 'M31')
SPR_LO, SPR_HI = HOM[0], HOM[-1]
print(f"  sprinkling homogeneity BAND = [{SPR_LO} , {SPR_HI}] = "
      f"[{float(SPR_LO):.4f}, {float(SPR_HI):.4f}] over "
      f"{len(FAMILY)} genuine configurations")

_ctrl_ok = all(FAMILY[k][2]['h2'] >= Fr(1, 2) for k in FAMILY)
_reversal = max(OM31) < R['M21'][2]['om']
check("A1 CONTROL VALIDATION, and THE FLAGGED FINDING CANDIDATE IS "
      "RESOLVED — NEGATIVELY (round-1 BLOCKER 1).  Homogeneity: every "
      "one of the genuine configurations clears the >= 1/2 bar, so the "
      "instrument IS validated on controls.  Overlap: the committed "
      "'striking M21-vs-M31 difference (0.12 vs 0.54)' was an artefact "
      "of a control that was 32 distinct points wearing 120 labels — "
      "against GENUINE M^{3+1} sprinklings at the same N the mean "
      "overlap is BELOW M21's, so the difference is real, is in the "
      "OPPOSITE direction, and is NOT density-confounded.  The committed "
      "density diagnosis is withdrawn along with the number",
      _ctrl_ok and _reversal,
      f"homogeneity band [{float(SPR_LO):.3f}, {float(SPR_HI):.3f}], all "
      f">= 1/2; M21 (committed record) mean omega = {R['M21'][2]['om']} "
      f"(~{float(R['M21'][2]['om']):.4f}); genuine M^{{3+1}} mean omega "
      f"range [{float(min(OM31)):.4f}, {float(max(OM31)):.4f}]; the "
      f"DEGENERATE committed control read "
      f"{float(R['M31DEGEN'][2]['om']):.4f} with mean chart width "
      f"{float(R['M31DEGEN'][2]['mean']):.2f} against "
      f"{float(R['M31'][2]['mean']):.2f} genuine")

# ------------------------------------------------------------------ A1b
print("\n[A1b WHAT omega IS — the containment theorem, round-1 MAJOR 2]")
print("  THEOREM (of the committed SKY-B definition).  For a cover pair")
print("  e < e':  if h[e'] - h[e] = 1 then D_e'(d-1) SUBSET D_e(d), so")
print("  omega(e,e') = |D_e'(d-1)| / |D_e(d)|; otherwise the two sets are")
print("  DISJOINT and omega = 0 identically.")
print("  Proof.  D_e(d) = {f : e < f, h[f] = h[e]+d} and D_e'(d-1) =")
print("  {f : e' < f, h[f] = h[e']+d-1}.  If h[e'] = h[e]+1 the height")
print("  conditions coincide and e < e' < f implies e < f; otherwise the")
print("  height conditions are incompatible.  []")
print("  CONSEQUENCES, both against the pin's framing: the intersection")
print("  is ALWAYS the whole successor chart, so 'the transition is the")
print("  identity on their intersection' has nothing to act on; and")
print("  omega is a CHART-SIZE RATIO along covers, which systematically")
print("  favours THIN-charted records (a 2-direction chart reaches high")
print("  omega when a neighbour retains 2; a 15-direction chart needs 15).")
_cont_all = all(FAMILY[k][d]['cont'] for k in FAMILY for d in (2, 3))
_jac_all = all(FAMILY[k][d]['jac'] for k in FAMILY for d in (2, 3))
_pairs_all = sum(FAMILY[k][d]['pairs'] for k in FAMILY for d in (2, 3))
check("A1b [THEOREM, verified] omega IS A CHART-SIZE RATIO, NOT AN "
      "OVERLAP.  Both clauses of the containment theorem hold with ZERO "
      "violations over every cover pair of every record measured here, "
      "and — independently — the Jaccard index |A&B|/|A|B| equals omega "
      "to the last Fraction on all of them, which is only possible under "
      "containment.  The instrument's second leg must be described as "
      "what it is",
      _cont_all and _jac_all and _pairs_all > 0,
      f"cover pairs checked = {_pairs_all}; containment violations = 0; "
      f"Jaccard-vs-omega disagreements = 0")

# ------------------------------------------------------------------ A1c
print("\n[A1c THE HEIGHT-GAP CENSUS — round-1 MAJOR 1: the pin's "
      "'same height layer' premise is FALSE]")
m21 = R['M21'][2]
m31 = R['M31'][2]
zero_share = Fr(m21['pairs'] - m21['pairs1'], m21['pairs'])
print(f"  M21: gaps {m21['gaps']}; {m21['pairs'] - m21['pairs1']} of "
      f"{m21['pairs']} measured pairs ({float(zero_share):.4f}) have gap "
      f">= 2 and are STRUCTURAL ZEROS, not measurements of poor charting")
print(f"  M31 (repaired): gaps {m31['gaps']}; structural-zero share "
      f"{float(Fr(m31['pairs'] - m31['pairs1'], m31['pairs'])):.4f}")
print(f"  CONDITIONED on gap 1 the ordering is the SAME REVERSAL by an "
      f"independent route: M21 {float(m21['om1']):.4f} vs genuine M31 "
      + ", ".join(f"box {k[1]}: {float(FAMILY[k][2]['om1']):.4f}"
                  for k in sorted(FAMILY, key=repr) if k[0] == 'M31'))
_gap1_rev = all(FAMILY[k][2]['om1'] < m21['om1']
                for k in FAMILY if k[0] == 'M31')
check("A1c THE REPORTED omega IS LARGELY A MEASUREMENT OF HOW CHAIN-LIKE "
      "THE POSET IS.  A cover pair's two chart sets share a height layer "
      "IFF the height gap is 1, which a cover does NOT guarantee; 61% of "
      "M21's measured pairs are structural zeros.  Restricted to gap-1 "
      "pairs the M21-vs-M31 ordering is the same reversal A1 found, "
      "reached by an independent route.  Both the unconditioned and the "
      "conditioned statistic are reported for every record",
      zero_share > Fr(1, 2) and _gap1_rev,
      f"M21 structural-zero share = {zero_share} "
      f"(~{float(zero_share):.4f}); gap-1 means: M21 {float(m21['om1']):.4f}"
      f", genuine M31 "
      f"[{min(float(FAMILY[k][2]['om1']) for k in FAMILY if k[0] == 'M31'):.4f}"
      f", {max(float(FAMILY[k][2]['om1']) for k in FAMILY if k[0] == 'M31'):.4f}]")

# --------------------------------------------------- the grammar records
print("\n[the grammar's records]")
b4, E4, D4, *_ = build(4)
R['SH4'] = atlas(poset_of(b4.H), 'shatter-4 record')
b5, E5, D5, *_ = build(5)
R['SH5'] = atlas(poset_of(b5.H), 'shatter-5 record')


def walk2(depth, seed):
    s = seed
    h = []
    for _ in range(depth):
        cand = candidates_for(h, ('A', 'B'))
        if not cand:
            break
        s = (1103515245 * s + 12345) % (1 << 31)
        h = h + [cand[s % len(cand)][0]]
    return h
R['WALK'] = atlas(poset_of(walk2(30, 4242)), 'generic 2-actor walk d30')

eng_homog = max(R['SH4'][2]['h2'], R['SH5'][2]['h2'])
check("A2 THE ATLAS GAP — the pre-registered comparison is now the "
      "PREDICATE, not the detail string (round-1 MINOR 3: the committed "
      "A2 gated `all(k in R for k in ...)`, true by construction three "
      "lines after the assignments).  Pre-registered: engineered records "
      "PATHOLOGICAL as atlases — built to shatter, not to tile.  The "
      "comparison is against the CORRECTED sprinkling family's measured "
      "BAND, not a two-point floor.  **This gate survives every "
      "correction in the round and is the unit's durable content**",
      eng_homog < SPR_LO,
      f"sprinkling homogeneity band = [{SPR_LO}, {SPR_HI}] "
      f"(~[{float(SPR_LO):.3f}, {float(SPR_HI):.3f}]) over {len(FAMILY)} "
      f"genuine configurations; engineered ceiling = {eng_homog} "
      f"(~{float(eng_homog):.3f}); generic walk = {R['WALK'][2]['h2']} "
      f"(~{float(R['WALK'][2]['h2']):.3f}) -> "
      + ("GAP CONFIRMED: the grammar's records are the opposite of "
         "atlases" if eng_homog < SPR_LO else
         "PRE-REGISTRATION REFUTED: engineered records are at least as "
         "homogeneous"))

check("A3 [REPORTING GATE, labelled] mean-overlap comparison at d = 2, "
      "each mean annotated with the population it is a mean over "
      "(round-1 MINOR 2: the committed table reported means from 2 pairs "
      "and 2,108 pairs side by side with no sample sizes, and WALK's "
      "1.00 — the highest value in the whole table — rests on TWO pairs)",
      R['M21'][2]['om'] is not None and R['WALK'][2]['om'] is not None,
      "; ".join(f"{k} = {float(R[k][2]['om']):.4f} over "
                f"{R[k][2]['pairs']} pairs"
                for k in ('M21', 'M31', 'M31DEGEN', 'SH4', 'SH5', 'WALK')))

print("\n[A4 THE CHART-WIDTH COLUMN — round-1 MINOR 1: |D| >= 4 was "
      "computed at every record and never compared]")
for k in ('M21', 'M31', 'M31DEGEN', 'SH4', 'SH5', 'WALK'):
    r = R[k][2]
    print(f"    {k:9s}: |D|>=2 {float(r['h2']):.4f}  |D|>=4 "
          f"{float(r['h4']):.4f}  mean|D| {float(r['mean']):.2f}  max|D| "
          f"{r['max']}")
W4LO = min(FAMILY[k][2]['h4'] for k in FAMILY)
W4HI = max(FAMILY[k][2]['h4'] for k in FAMILY)
check("A4 CHART WIDTH IS A THIRD, EQUALLY NATURAL METRIC, and it is "
      "reported here because it is the one that qualifies the successor "
      "unit's verdict (D60 MAJOR 3): genuine sprinklings carry "
      "4-direction charts at a substantial fraction of their events, and "
      "any record claimed to be 'sprinkling-grade' must be placed beside "
      "this column, not only beside |D| >= 2",
      W4HI > W4LO > 0,
      f"genuine sprinkling |D|>=4 band = [{W4LO}, {W4HI}] "
      f"(~[{float(W4LO):.3f}, {float(W4HI):.3f}]); engineered records "
      f"{float(R['SH4'][2]['h4']):.3f} / {float(R['SH5'][2]['h4']):.3f}; "
      f"generic walk {float(R['WALK'][2]['h4']):.3f}")

# the exact comparators D60 must import rather than re-type (NIT 1/NIT 2)
COMPARATORS = {
    'SPRINKLE_HOMOG_LO': SPR_LO, 'SPRINKLE_HOMOG_HI': SPR_HI,
    'ENGINEERED_CEIL': eng_homog, 'WALK_HOMOG': R['WALK'][2]['h2'],
    'M21_OMEGA': R['M21'][2]['om'],
    'M31_OMEGA_LO': min(OM31), 'M31_OMEGA_HI': max(OM31),
    'SPRINKLE_W4_LO': W4LO, 'SPRINKLE_W4_HI': W4HI,
}
print("\n[COMPARATORS, exact Fractions — D60 imports these by AST "
      "extraction rather than re-typing floor-rounded percentages "
      "(round-1 NIT 1/NIT 2 and D60 MINOR 1)]")
for k in sorted(COMPARATORS):
    print(f"    {k} = {COMPARATORS[k]}  (~{float(COMPARATORS[k]):.4f})")

_ch = [c for c in ast.walk(ast.parse(open(
    'v10/code/d58_atlas_instrument_exact.py').read()))
    if isinstance(c, ast.Call) and isinstance(c.func, ast.Name)
    and c.func.id == 'check']
_vac = [c for c in _ch if isinstance(c.args[1], ast.Constant)]
check("A5 AST anti-vacuity (no bare-constant predicates; #403 MA-2 "
      "scope) — NOTE: A3's predicate is near-vacuous by design (it is a "
      "REPORTING gate) and is labelled as such; A2, which round 1 found "
      "unlabelled AND unfalsifiable, now carries the falsifiable "
      "comparison",
      len(_ch) >= 6 and len(_vac) == 0,
      f"check() calls = {len(_ch)}, bare = {len(_vac)}")

print("\n[VERDICT — D58, ROUND-1 REPAIRED]")
print("  WHAT STANDS: the homogeneity leg.  The instrument is validated")
print("  on eleven genuine sprinkling configurations (band "
      f"[{float(SPR_LO):.3f}, {float(SPR_HI):.3f}]), and the grammar's")
print("  shatter records sit far below it — the pre-registered gap, "
      "unmoved by any correction in the round.")
print("  WHAT IS WITHDRAWN: every M^{3+1} number of the committed run")
print("  (73% / 0.54 / 0.94), the 'FINDING CANDIDATE' framing, and the")
print("  density diagnosis.  The comparison, run against genuine")
print("  sprinklings, RESOLVES the flagged residue with the sign flipped.")
print("  WHAT IS RESTATED: omega is a CHART-SIZE RATIO along covers")
print("  (A1b's containment theorem), reported with its height-gap")
print("  census (A1c); the pin's 'same height layer' premise holds only")
print("  at gap 1, and the atlas/cocycle language must not outrun it.")
print(f"\n[d58] {PASS} PASS / {FAIL} FAIL")
sys.exit(1 if FAIL else 0)

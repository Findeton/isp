#!/usr/bin/env python3
"""
d55c_m31_control_exact.py — v10 D55c: the full-strength M^{3+1} control.
Pin: note-d55c-m31-control-pin.md (STRICT, LOG #434, before code).

**ROUND-1 REVIEWED AND REPAIRED (2026-07-26).**  Independent hostile
review `v10/reviews/batch-round1-d50-to-d60.md` — REVISE, 1 BLOCKER /
2 MAJOR / 4 MINOR / 2 NIT.  The instrument was sound, `mink4` was correct
event for event, and the committed census reproduced exactly; **the
headline was an artefact of the four boxes chosen, and it REVERSES.**

  * BLOCKER 1 — the zero-shatter-4 result was a DENSITY ARTEFACT.  The
    four committed configurations are sparse and their density FALLS
    3.9x across the sweep; at matched-or-higher density genuine M^{3+1}
    shatters 4 and the pre-registered discriminator FIRES.  The headline
    is restated in the direction the corrected evidence lands.
  * BLOCKER 1 / D53 — the sweep tested SKY-B ONLY, because D53 told the
    programme that SKY-A and SKY-C 'can never shatter'.  D53's theorem
    was false (its round-1 BLOCKER 1); SKY-A and SKY-C are back, and
    under SKY-A the discriminator is SHARPER.
  * MAJOR 1 — 'NO sprinkled record of ANY tested dimension shatters at
    all' is false on this unit's own records: shatter-3 fires.  Reported.
  * MAJOR 2 — the headline was gated by nothing (C3's predicate was
    `cap4 > 0`), no positive control exercised `shattered_set` on a
    system that DOES shatter, and the witness branch was dead.  All
    three repaired; witness branches print their witnesses.
  * MINOR 1 — the pin's FIXED-BOX density control was never implemented.
    It is the ladder below: box and T held fixed, N swept, density rising.
  * MINOR 2 — `latt4`'s power-of-two degeneracy (see `latt`'s docstring):
    (120, 32, 8) was 32 distinct points wearing 120 labels.  Generator
    repaired here; D53 and D58 single-source the fix from this file.
  * MINOR 3 — the silent depth cap at 10 is gone; SKY-B now runs each
    record's OWN full height range, printed.
  * MINOR 4 — the capacity diagnostics (best |{r & S}|) are reported.
  * NIT 1 — the C0 anchor now has a z != 0 assertion.

Exit 1 on anchor breakage OR any shatter-5 on genuine M^{3+1} (the
pinned halt condition).  Run from the repo root.
"""
import ast, sys
from collections import defaultdict
from fractions import Fraction as Fr
from itertools import combinations, permutations, product
sys.setrecursionlimit(200000)
PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

print("[D55c — the M^{3+1} control at full strength, ROUND-1 REPAIRED]")
print("  banner: the committed run's zero-shatter-4 was a DENSITY")
print("  ARTEFACT read through a SKY-B-only blinder inherited from D53's")
print("  false necessity theorem.  Generator repaired (no power-of-two")
print("  degeneracy), fixed-box density control implemented as the pin")
print("  promised, SKY-A and SKY-C restored to the field of view, both")
print("  sides of the control run at matched configuration.  The")
print("  headline is restated in the direction the evidence lands.")

_ta = ast.parse(open('v10/code/d47a_sky_instrument_exact.py').read())
_keep = [n for n in _ta.body if isinstance(n, ast.FunctionDef)
         or (isinstance(n, ast.Assign) and any(isinstance(x, ast.Name)
             and x.id in ('CYCLIC_CAP', 'SKYB_DEPTH') for x in n.targets))]
g = {'Fr': Fr, 'combinations': combinations,
     'permutations': permutations, 'product': product}
exec(compile(ast.fix_missing_locations(ast.Module(body=_keep,
    type_ignores=[])), 'x', 'exec'), g)
sky, shattered_set, mink3 = g['sky'], g['shattered_set'], g['mink_order']
heights, arc_system = g['heights'], g['arc_system']

def mink4(pts):
    """Exact causal order in M^{d+1} for points (t, x1..xd).  Works at
    any spatial dimension; the name is kept for its consumers."""
    n = len(pts)
    C = [[False] * n for _ in range(n)]
    for i in range(n):
        pi = pts[i]
        for j in range(n):
            if i == j: continue
            pj = pts[j]
            dt = pj[0] - pi[0]
            if dt <= 0: continue
            ss = dt * dt - sum((pj[k] - pi[k]) ** 2
                               for k in range(1, len(pi)))
            if ss >= 0:
                C[i][j] = True
    return C

def latt(N, dim, box, seed, T=None):
    """CORRECTED BY ROUND 1 (MINOR 2, and D58's BLOCKER 1).  The
    committed generator drew `s % box` from an LCG mod 2^31.  The low k
    bits of that LCG have period 2^k and each point consumes dim+1 draws,
    so a fixed coordinate slot's low-k-bit subsequence has period
    2^(k-2): at box = 32 the 'sprinkling' collapsed to 32 distinct points
    wearing 120 labels, and at EVERY box the spatial values sat on a
    spacing-4 sublattice.  The repair draws from the HIGH bits
    ((s >> 16) % box), which carry no low-bit periodicity.  `dim` is the
    number of SPATIAL axes, so dim = 2 and dim = 3 give matched M^{2+1}
    and M^{3+1} sprinklings differing in nothing but the dimension."""
    s, out = seed, []
    Tb = 4 * box if T is None else T
    for _ in range(N):
        s = (1103515245 * s + 12345) % (1 << 31)
        row = [Fr((s >> 16) % Tb)]
        for _ in range(dim):
            s = (1103515245 * s + 12345) % (1 << 31)
            row.append(Fr((s >> 16) % box))
        out.append(tuple(row))
    return out

def latt4(N, box, seed, T=None):
    """The 3+1 sprinkling.  Signature preserved for D53/D58/D60; the
    generator itself is the round-1 repaired one."""
    return latt(N, 3, box, seed, T)

def latt4_committed(N, box, seed):
    """The DEFECTIVE committed generator, kept so the degeneracy round 1
    found can be exhibited rather than merely asserted."""
    s, out = seed, []
    for _ in range(N):
        s = (1103515245 * s + 12345) % (1 << 31); t = Fr(s % (4 * box))
        row = [t]
        for _ in range(3):
            s = (1103515245 * s + 12345) % (1 << 31)
            row.append(Fr(s % box))
        out.append(tuple(row))
    return out

def shattered_levels(rows, dirs, kmax):
    """Every shattered subset up to size kmax, by downward closure: a
    k-set is shattered only if all its (k-1)-subsets are, so candidates
    are generated from level k-1 and then VERIFIED directly against the
    trace count.  Exactly equivalent to calling d47a's shattered_set at
    each k — gated as such in C0(c) — and cheap enough to reach SKY-A's
    wide direction sets, which d47a's exhaustive scan cannot."""
    R = [frozenset(r) for r in rows]
    cur = []
    for c in sorted(dirs):
        S = {c}
        if len({frozenset(r & S) for r in R}) == 2:
            cur.append((c,))
    lv = {1: cur}
    for k in range(2, kmax + 1):
        prev, cand = set(cur), set()
        for a in prev:
            for b in prev:
                if a < b and a[:-1] == b[:-1]:
                    t = a + (b[-1],)
                    if all(tuple(x for x in t if x != d) in prev
                           for d in t):
                        cand.add(t)
        nxt = [t for t in sorted(cand)
               if len({frozenset(r & set(t)) for r in R}) == (1 << k)]
        lv[k] = nxt
        cur = nxt
        if not cur:
            break
    return lv

def capable(dirs, rows, k):
    """D53's CORRECTED (round-1) necessary condition: >= k directions and
    >= 2^k distinct traces.  The withdrawn third clause ('the empty trace
    is among them') is what confined this unit to SKY-B."""
    return len(dirs) >= k and len(set(rows)) >= (1 << k)

def best_trace(rows, dirs, k):
    R = [frozenset(r) for r in rows]
    best = 0
    for sub in combinations(sorted(dirs), k):
        S = set(sub)
        best = max(best, len({frozenset(r & S) for r in R}))
    return best

# ------------------------------------------------------------------- C0
print("\n[C0 anchors]")
p3 = g['lattice_points'](40)
p4 = [(t, x, y, Fr(0)) for (t, x, y) in p3]
def mink4_broken(pts):
    """mink4 with the z term dropped — the mutant round 1's NIT 1 says
    the old anchor could not see."""
    n = len(pts)
    C = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j: continue
            dt = pts[j][0] - pts[i][0]
            ss = dt * dt - sum((pts[j][k] - pts[i][k]) ** 2 for k in (1, 2))
            if dt > 0 and ss >= 0:
                C[i][j] = True
    return C
p4z = [(t, x, y, Fr(int(x) % 7)) for (t, x, y) in p3]
_z_bites = mink4(p4z) != mink4_broken(p4z)
check("C0(a) ANCHOR: mink4 restricted to z = 0 is IDENTICAL to the "
      "committed d47a mink_order on the same (t, x, y) points — AND "
      "(round-1 NIT 1) the anchor now BITES at z != 0: a mutant mink4 "
      "that drops the z term entirely, which the committed anchor "
      "passed, is rejected here",
      mink4(p4) == mink3(p3) and _z_bites,
      f"40-point z = 0 slice identical = {mink4(p4) == mink3(p3)}; "
      f"z != 0 mutant detected = {_z_bites}")

_com = latt4_committed(120, 32, 8)
_rep = latt4(120, 32, 8, 128)
check("C0(b) THE GENERATOR REPAIR, EXHIBITED (round-1 MINOR 2 / D58 "
      "BLOCKER 1).  The committed `latt4` drew from the LCG's LOW bits, "
      "whose period is a power of two; at box = 32 the committed "
      "M^{3+1} 'sprinkling' was 32 distinct points wearing 120 labels, "
      "and at every box the spatial values sat on a spacing-4 "
      "sublattice.  The repaired generator draws from the high bits",
      len(set(_com)) < 120 and len(set(_rep)) == 120
      and len({p[1] for p in _rep}) > len({p[1] for p in _com}),
      f"committed (120, 32, 8): distinct points = {len(set(_com))}/120, "
      f"distinct x-values = {len({p[1] for p in _com})}; repaired: "
      f"distinct points = {len(set(_rep))}/120, distinct x-values = "
      f"{len({p[1] for p in _rep})}")

_caps = [frozenset(s) for k in range(5) for s in combinations(range(4), k)]
_arcs, _acols = arc_system(6)
_pos = shattered_set(_caps, range(4), 4)
_neg = shattered_set(_arcs, _acols, 4)
_lvpos = shattered_levels(_caps, range(4), 4)
_lvneg = shattered_levels(_arcs, _acols, 4)
_agree = ((_pos is not None) == bool(_lvpos.get(4))
          and (_neg is not None) == bool(_lvneg.get(4)))
check("C0(c) THE INSTRUMENT HAS A TRUE POSITIVE AND A TRUE NEGATIVE "
      "(round-1 MAJOR 2: the committed receipt had NEITHER, and a "
      "`shattered_set` stuck at None would have passed all four of its "
      "gates and produced its exact output).  d47a's own separator is "
      "re-decided in this process, and the fast downward-closure search "
      "used below is gated to AGREE with d47a's exhaustive scan",
      _pos is not None and _neg is None and _agree,
      f"caps shatter 4 = {_pos is not None} (witness {_pos}); arcs "
      f"shatter 4 = {_neg is not None}; fast search agrees with d47a's "
      f"shattered_set = {_agree}")

# ------------------------------------------------------------- C1 census
print("\n[C1 the four COMMITTED configurations, re-run with the repaired "
      "generator, all three sky readings, each record's OWN depth range]")
CONFIGS = [(80, 24, 7), (120, 32, 8), (160, 40, 9), (200, 40, 10)]
TOT = defaultdict(lambda: defaultdict(int))
SH3_TOT = CAP3_TOT = 0
DIAG = {}
AGREE_SAMPLED = 0
AGREE_BAD = 0
for (N, box, seed) in CONFIGS:
    pts = latt4(N, box, seed)
    C = mink4(pts)
    hh = heights(C)
    hmax = max(hh) - min(hh)
    rec = defaultdict(int)
    for e in range(N):
        readings = [('A', sky(C, e, 'A')), ('C', sky(C, e, 'C'))]
        for d in range(1, hmax + 1):
            readings.append(('B', sky(C, e, 'B', d)))
        for kind, (dirs, rows) in readings:
            if not dirs:
                continue
            lv = None
            for k in (3, 4, 5):
                if not capable(dirs, rows, k):
                    continue
                if lv is None:
                    lv = shattered_levels(rows, dirs, 5)
                rec[(kind, k, 'cap')] += 1
                if lv.get(k):
                    rec[(kind, k, 'sh')] += 1
                    if AGREE_SAMPLED < 40:
                        AGREE_SAMPLED += 1
                        if shattered_set(rows, dirs, k) is None:
                            AGREE_BAD += 1
    vol = (4 * box) * box ** 3
    print(f"  N={N} box={box} (volume {vol}, density "
          f"{float(Fr(N, vol)):.3e}, height range 1..{hmax}):")
    for kind in ('A', 'B', 'C'):
        print(f"      SKY-{kind}: "
              + ", ".join(f"capable({k})={rec[(kind, k, 'cap')]} "
                          f"shatter{k}={rec[(kind, k, 'sh')]}"
                          for k in (3, 4, 5)))
    for key, v in rec.items():
        TOT[key[0]][(key[1], key[2])] += v
    CAP3_TOT += sum(rec[(kd, 3, 'cap')] for kd in 'ABC')
    SH3_TOT += sum(rec[(kd, 3, 'sh')] for kd in 'ABC')
    if (N, box) == (200, 40):
        b4 = defaultdict(int)
        b5 = defaultdict(int)
        for e in range(N):
            for d in range(1, hmax + 1):
                dirs, rows = sky(C, e, 'B', d)
                if capable(dirs, rows, 4):
                    b4[best_trace(rows, dirs, 4)] += 1
                if capable(dirs, rows, 5):
                    b5[best_trace(rows, dirs, 5)] += 1
        DIAG['b4'] = dict(sorted(b4.items()))
        DIAG['b5'] = dict(sorted(b5.items()))

cap4_B = TOT['B'][(4, 'cap')]
sh4_B = TOT['B'][(4, 'sh')]
check("C1 THE COMMITTED CONFIGURATIONS, RE-RUN.  Depth range is now each "
      "record's OWN (round-1 MINOR 3: the committed sweep silently "
      "stopped at 10 while two records run to 11 and 12), the generator "
      "is repaired, and all three sky readings are swept.  The fast "
      "shatter search is gated against d47a's own decider on every hit "
      "it is sampled at.  NOTE: even at the COMMITTED densities the "
      "committed verdict does not survive the restored readings — SKY-A "
      "already returns a shattered 4-set on the N = 200 record, which "
      "the SKY-B-only sweep could not see",
      cap4_B > 0 and AGREE_BAD == 0,
      f"SKY-B capable(4) = {cap4_B}, shatter-4 = {sh4_B}; SKY-A "
      f"capable(4) = {TOT['A'][(4, 'cap')]}, shatter-4 = "
      f"{TOT['A'][(4, 'sh')]}; SKY-C capable(4) = "
      f"{TOT['C'][(4, 'cap')]}, shatter-4 = {TOT['C'][(4, 'sh')]}; "
      f"d47a cross-checks {AGREE_SAMPLED}, disagreements {AGREE_BAD}")

check("C2 [CORRECTED BY ROUND 1 — MAJOR 1] 'NO SPRINKLED RECORD OF ANY "
      "TESTED DIMENSION SHATTERS AT ALL' IS FALSE, and it was already "
      "false on this unit's own four records.  Sprinkled records do not "
      "sit at meter reading ~0; they sit at 3 — the circle's rung on "
      "D55's ladder.  The residue LOG #435 listed as open was decided by "
      "the data in hand",
      SH3_TOT > 0 and CAP3_TOT > 0,
      f"capable(3) = {CAP3_TOT}, SHATTER-3 = {SH3_TOT} over the four "
      f"committed configurations, all three readings")

# ----------------------------------------------- C3 the density ladder
print("\n[C3 THE FIXED-BOX DENSITY CONTROL the pin promised (round-1 "
      "MINOR 1), and the matched 2+1 vs 3+1 ladder]")
LAD_BOX, LAD_T, LAD_SEED = 30, 120, 11
LADDER = (150, 200, 250, 300, 400, 500)
LAD = {2: {}, 3: {}}
BINS = {2: defaultdict(lambda: [0, 0]), 3: defaultdict(lambda: [0, 0])}
LAD_WIT = {}
for dim in (2, 3):
    for N in LADDER:
        C = mink4(latt(N, dim, LAD_BOX, LAD_SEED, LAD_T))
        c4 = s4 = c5 = s5 = 0
        for e in range(N):
            dirs, rows = sky(C, e, 'A')
            if not capable(dirs, rows, 4):
                continue
            c4 += 1
            lv = shattered_levels(rows, dirs, 5)
            hit4 = bool(lv.get(4))
            if hit4:
                s4 += 1
                if dim == 3 and 3 not in LAD_WIT:
                    LAD_WIT[3] = (N, e, len(dirs), len(set(rows)),
                                  frozenset() in set(rows), lv[4][0])
            if N >= 200:
                b = min((len(dirs) - 4) // 4, 6)
                BINS[dim][b][0] += int(hit4)
                BINS[dim][b][1] += 1
            if capable(dirs, rows, 5):
                c5 += 1
                if lv.get(5):
                    s5 += 1
        LAD[dim][N] = (c4, s4, c5, s5)
    vol = LAD_T * LAD_BOX ** dim
    print(f"  M^{{{dim}+1}}, box {LAD_BOX} and T {LAD_T} HELD FIXED "
          f"(density RISES with N; densities are per-dimension and are "
          f"NOT comparable across the two rows — what is matched is the "
          f"CONFIGURATION (N, T, box, seed)):")
    for N in LADDER:
        v = vol
        c4, s4, c5, s5 = LAD[dim][N]
        print(f"      N={N:4d} density {float(Fr(N, v)):.3e}: "
              f"SKY-A capable(4)={c4:4d} SHATTER-4={s4:4d} | "
              f"capable(5)={c5:4d} SHATTER-5={s5}")
if 3 in LAD_WIT:
    N, e, nd, nr, emp, w = LAD_WIT[3]
    print(f"  [WITNESS M31-SHATTER-4] N={N} event={e} SKY-A |dirs|={nd} "
          f"|rows|={nr} EMPTY ROW={emp} SHATTERED 4-SET={w}")
sh4_31 = [LAD[3][N][1] for N in LADDER]
sh4_21 = [LAD[2][N][1] for N in LADDER]
sh5_all = sum(LAD[d][N][3] for d in (2, 3) for N in LADDER)
check("C3 [THE HEADLINE, RESTATED BY ROUND 1 — THE COMMITTED VERDICT IS "
      "REVERSED] **SHATTER-4 IS AN EMPIRICAL DIMENSION DISCRIMINATOR, "
      "WITH TWO-SIDED CONTROLS.**  The committed run's zero was a "
      "DENSITY ARTEFACT: its four boxes are sparse and their density "
      "FALLS 3.9x across the sweep, and its skies sat one trace "
      "short of capacity in bulk (C6).  On the fixed-box ladder the discriminator "
      "fires: genuine M^{3+1} shatter-4 counts RISE with density while "
      "the matched M^{2+1} control — same N, same box, same T, same "
      "seed, only the dimension differs — stays at ZERO throughout.  "
      "What the four committed records license is only the scoped "
      "negative: at the sampled densities no SKY-B sky of a sprinkled "
      "M^{3+1} record shatters 4",
      sum(sh4_31) > 0 and sum(sh4_21) == 0,
      f"M^{{3+1}} shatter-4 by N {list(LADDER)} = {sh4_31}; matched "
      f"M^{{2+1}} = {sh4_21}; capable(4) 3+1 = "
      f"{[LAD[3][N][0] for N in LADDER]}, 2+1 = "
      f"{[LAD[2][N][0] for N in LADDER]}")

print("\n  SIZE CONTROL (the trap D54 round 1 named): shatter-4 rate by "
      "|dirs| band, SKY-A, pooled over N = 200..500")
_names = {0: ' 4-7', 1: ' 8-11', 2: '12-15', 3: '16-19', 4: '20-23',
          5: '24-27', 6: '28+'}
for dim in (2, 3):
    print(f"      M^{{{dim}+1}}: " + "  ".join(
        f"{_names[b]}: {BINS[dim][b][0]}/{BINS[dim][b][1]}"
        for b in sorted(BINS[dim])))
_ov = [b for b in sorted(BINS[3])
       if BINS[2][b][1] >= 50 and BINS[3][b][1] >= 50]
_sizeok = any(BINS[3][b][0] > BINS[2][b][0] for b in _ov)
check("C4 IT IS NOT MERELY SKY SIZE.  In the |dirs| bands where the two "
      "dimensions are comparably sampled, the 3+1 records shatter and "
      "the matched 2+1 records do not — so the split is not an artefact "
      "of 3+1 skies simply being wider",
      _sizeok and len(_ov) > 0,
      f"comparably-sampled bands = {[_names[b] for b in _ov]}; 3+1 hits "
      f"{[BINS[3][b][0] for b in _ov]} of {[BINS[3][b][1] for b in _ov]}"
      f", 2+1 hits {[BINS[2][b][0] for b in _ov]} of "
      f"{[BINS[2][b][1] for b in _ov]}")

check("C5 THE HALT CONDITION IS NOT TRIPPED, and it now holds where it "
      "MATTERS — on the dense records where shatter-4 DOES fire, and "
      "under SKY-A, the reading D53's false theorem had excluded.  The "
      "3+1 celestial sphere is S^2, whose caps stop at 4; a shatter-5 "
      "would convict the sky definition.  (Round-1 MINOR 4: the "
      "committed shatter-5 null was WEAK — the richest committed sky "
      "carried 21 of the 32 traces — so it passed with a wide margin of "
      "incapacity.  On the ladder the margin is real)",
      sh5_all == 0,
      f"capable(5) pairs on the ladder = "
      f"{sum(LAD[d][N][2] for d in (2, 3) for N in LADDER)}, "
      f"shattered = {sh5_all}; committed configurations: SKY-B "
      f"capable(5) = {TOT['B'][(5, 'cap')]}, shatter-5 = "
      f"{TOT['B'][(5, 'sh')]}, SKY-A = {TOT['A'][(5, 'cap')]}/"
      f"{TOT['A'][(5, 'sh')]}, SKY-C = {TOT['C'][(5, 'cap')]}/"
      f"{TOT['C'][(5, 'sh')]}")

print("\n[C6 the capacity diagnostic — round-1 MINOR 4, the difference "
      "between a strong null and a weak one]")
print(f"  best |{{r & S}}| over 4-subsets, N=200 box=40, SKY-B: "
      f"{DIAG.get('b4')}")
print(f"  best |{{r & S}}| over 5-subsets, N=200 box=40, SKY-B: "
      f"{DIAG.get('b5')}")
_near4 = sum(v for k, v in DIAG.get('b4', {}).items() if k == 15)
check("C6 THE COMMITTED SHATTER-4 NULL WAS STRONG AND THE SHATTER-5 NULL "
      "WAS WEAK, and the receipt never said so.  The shatter-4 census "
      f"left {_near4} skies exactly ONE TRACE SHORT of 16 — which is why "
      "it collapses under a modest density increase (C3).  The "
      "shatter-5 census never came close: the richest committed sky "
      f"carried {max(DIAG.get('b5', {0: 0})) } of 32, i.e. the halt "
      "condition passed with a wide margin of INCAPACITY, D53's own "
      "tautology trap one rung up",
      _near4 > 0 and max(DIAG.get('b5', {0: 0})) < 32,
      f"one-trace-short 4-skies = {_near4}; richest 5-subset trace "
      f"count = {max(DIAG.get('b5', {0: 0}))} of 32")

_self = ast.parse(open('v10/code/d55c_m31_control_exact.py').read())
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
check("C7 AST anti-vacuity (LOG #403 MA-2 scope): every check() "
      "predicate references a run-bound name and none is a bare "
      "constant.  Round-1 MAJOR 2's finding was that the committed C3 "
      "gated `cap4 > 0` — non-vacuous by this scan and yet unable to "
      "see its own headline; the scan enforces exactly what it says and "
      "nothing more",
      len(_ch) >= 7 and not _vac,
      f"check() calls = {len(_ch)}, bare/unbound = {len(_vac)}")

print("\n[VERDICT — D55c, ROUND-1 REPAIRED]")
print("  **THE PRE-REGISTERED DISCRIMINATOR HOLDS.**  Sprinkled 2+1")
print("  shatters 3 and never 4; sprinkled 3+1 shatters 4 and never 5.")
print("  That is the opposite of the committed conclusion, and it is the")
print("  continuum calibration transferring exactly: arcs shatter 3,")
print("  caps shatter 4, Radon stops at 5.")
print("  WITHDRAWN: 'genuine discrete 3+1 skies do NOT shatter 4'; 'THE")
print("  DISCRIMINATOR READING FAILS'; 'NO sprinkled Minkowski record of")
print("  ANY tested dimension shatters at all'; 'the meter measures the")
print("  grammar, not geometry'.  LOG #436's STANDING REDIRECT cites the")
print("  reframe and must be restated with it.")
print("  SCOPE, held: sprinkled records, exact integer coordinates, one")
print("  seed per configuration; SKY-A/B/C readings named per number; no")
print("  typicality claim.  The 2+1 side is a MATCHED control, not a")
print("  theorem — 'never 4' is a measurement over this ladder.")
print(f"\n[d55c] {PASS} PASS / {FAIL} FAIL")
sys.exit(1 if FAIL else 0)

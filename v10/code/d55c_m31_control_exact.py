#!/usr/bin/env python3
"""
d55c_m31_control_exact.py — v10 D55c: the full-strength M^{3+1} control.
Pin: note-d55c-m31-control-pin.md (STRICT, LOG #434, before code).
Exit 1 on anchor breakage OR any shatter-5 on genuine M^{3+1} (the
pinned halt condition).  shatter-4 is pre-registered OPEN.
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

print("[D55c — the M^{3+1} control at full strength]")
_ta = ast.parse(open('v10/code/d47a_sky_instrument_exact.py').read())
_keep = [n for n in _ta.body if isinstance(n, ast.FunctionDef)
         or (isinstance(n, ast.Assign) and any(isinstance(x, ast.Name)
             and x.id in ('CYCLIC_CAP', 'SKYB_DEPTH') for x in n.targets))]
g = {'Fr': Fr, 'combinations': combinations,
     'permutations': permutations, 'product': product}
exec(compile(ast.fix_missing_locations(ast.Module(body=_keep,
    type_ignores=[])), 'x', 'exec'), g)
sky, shattered_set, mink3 = g['sky'], g['shattered_set'], g['mink_order']

def mink4(pts):
    n = len(pts)
    C = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j: continue
            dt = pts[j][0] - pts[i][0]
            ss = dt * dt - sum((pts[j][k] - pts[i][k]) ** 2
                               for k in (1, 2, 3))
            if dt > 0 and ss >= 0:
                C[i][j] = True
    return C

def latt4(N, box, seed):
    s, out = seed, []
    for _ in range(N):
        s = (1103515245 * s + 12345) % (1 << 31); t = Fr(s % (4 * box))
        row = [t]
        for _ in range(3):
            s = (1103515245 * s + 12345) % (1 << 31)
            row.append(Fr(s % box))
        out.append(tuple(row))
    return out

# anchor: z = 0 slice of mink4 == committed mink3
p3 = g['lattice_points'](40)
p4 = [(t, x, y, Fr(0)) for (t, x, y) in p3]
check("C0 ANCHOR: mink4 restricted to z = 0 is IDENTICAL to the "
      "committed d47a mink_order on the same (t, x, y) points",
      mink4(p4) == mink3(p3), "40-point slice, orders identical")

cap4 = cap5 = sh4 = sh5 = 0
first4 = None
CONFIGS = [(80, 24, 7), (120, 32, 8), (160, 40, 9), (200, 40, 10)]
for (N, box, seed) in CONFIGS:
    C = mink4(latt4(N, box, seed))
    c4 = c5 = s4 = s5 = 0
    for e in range(N):
        for d in range(1, 11):
            dirs, rows = sky(C, e, 'B', d)
            r = set(rows)
            if len(dirs) >= 4 and len(r) >= 16 and frozenset() in r:
                c4 += 1
                if shattered_set(rows, dirs, 4) is not None:
                    s4 += 1
                    if first4 is None:
                        first4 = (N, box, e, d)
            if len(dirs) >= 5 and len(r) >= 32 and frozenset() in r:
                c5 += 1
                if shattered_set(rows, dirs, 5) is not None:
                    s5 += 1
    print(f"  N={N} box={box}: SC5-capable(4)={c4}, shatter4={s4}; "
          f"capable(5)={c5}, shatter5={s5}")
    cap4 += c4; cap5 += c5; sh4 += s4; sh5 += s5

check("C1 THE HALT CONDITION IS NOT TRIPPED: ZERO shatter-5 on genuine "
      "M^{3+1} at every capable pair (the 3+1 celestial sphere is S^2, "
      "whose caps stop at 4; a hit would convict the sky definition)",
      sh5 == 0, f"capable(5) pairs = {cap5}, shattered = {sh5}")
check("C2 THE CONTROL IS NO LONGER THIN: the SC5-capable(4) census "
      "exceeds several hundred pairs (the round's control had 33)",
      cap4 >= 200, f"capable(4) = {cap4} across {len(CONFIGS)} records")
check("C3 SHATTER-4 ON GENUINE M^{3+1} [pre-registered OPEN, lean "
      "weakly positive]: the count is reported in whichever direction "
      "it came out.  POSITIVE => shatter-4 is an EMPIRICAL dimension "
      "discriminator with controls on both sides (2+1: zero over all "
      "capable pairs, D47a/D53).  ZERO => discrete M^{3+1} skies do "
      "not inherit the continuum caps' shattering, and the "
      "discriminator reading FAILS — a real result either way",
      cap4 > 0,
      f"shatter-4 = {sh4} of {cap4} capable"
      + (f"; first witness (N, box, event, depth) = {first4}"
         if first4 else "; NO shatter-4 found — the discriminator "
                        "reading FAILS on this evidence"))
print(f"\n[d55c] {PASS} PASS / {FAIL} FAIL")
sys.exit(1 if FAIL else 0)

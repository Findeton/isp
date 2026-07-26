#!/usr/bin/env python3
"""
d55b_sphere_calibration_exact.py — v10 D55 A2: the sphere calibrations.
Pin: note-d55-dimension-meter-pin.md §3 (STRICT, LOG #430).

A2a: the m = 4 family (all of B4) realized EXACTLY by caps on S^2 —
     16 exact rational halfspace certificates on d47a's own rational
     tetrahedron.  Upgrades D54's record to SPHERE-COMPATIBLE.
A2b: [THEOREM, certificated] no five points admit cap shattering on
     S^2: five points in R^3 are affinely dependent; the dependence is
     a Radon partition; the positive side is separated by no halfspace.
     Exact certificates on two concrete rational configurations.
A2c: the m = 5 family (all of B5) realized by caps on S^3 — five exact
     rational unit vectors in R^4, 32 exact certificates by grid
     search (grid declared; NOT-FOUND would be reported as such, never
     as impossibility).

All arithmetic exact Fractions.  Exit 1 only on instrument breakage.
Run from the repo root: python3 v10/code/d55b_sphere_calibration_exact.py
"""
import ast
import sys
from fractions import Fraction as Fr
from itertools import combinations, product

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

print("[D55 A2 — the sphere calibrations]")
print("  banner: exact rational certificates only; grid ranges declared;")
print("  a failed search is NOT-FOUND, never impossibility (one-")
print("  sidedness); the impossibility direction (A2b) is carried by an")
print("  exact Radon certificate, not by search.")


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


# ------------------------------------------------------------------ A2a
print("\n[A2a — the m = 4 family on S^2]")
SPH = [(Fr(1), Fr(0), Fr(0)),
       (Fr(-1, 3), Fr(2, 3), Fr(2, 3)),
       (Fr(-1, 3), Fr(-2, 3), Fr(2, 3)),
       (Fr(-1, 3), Fr(2, 3), Fr(-2, 3))]
check("A2a-0 the four points are EXACTLY on the unit sphere (d47a's "
      "own rational tetrahedron, re-verified here)",
      all(dot(p, p) == 1 for p in SPH), "norms all exactly 1")

GRID3 = [Fr(a) for a in range(-2, 3)]
certs4 = {}
for k in range(5):
    for sub in combinations(range(4), k):
        S = set(sub)
        found = None
        for u in product(GRID3, repeat=3):
            if u == (0, 0, 0):
                continue
            ds = [dot(u, p) for p in SPH]
            ins = [ds[i] for i in range(4) if i in S]
            outs = [ds[i] for i in range(4) if i not in S]
            if not ins:
                found = (u, max(ds) + 1); break
            if not outs:
                found = (u, min(ds) - 1); break
            if min(ins) > max(outs):
                found = (u, (min(ins) + max(outs)) / 2); break
        if found:
            certs4[frozenset(S)] = found
ver4 = all(
    {i for i in range(4) if dot(u, SPH[i]) >= t} == set(S)
    for S, (u, t) in certs4.items())
check("A2a **THE m = 4 FAMILY IS SPHERE-COMPATIBLE**: all 16 subsets "
      "of the tetrahedron realized by exact rational caps, each "
      "certificate re-verified by Fraction dot products.  D54's record "
      "— whose SKY-B family IS all of B4 — is therefore realizable as "
      "a cap system on S^2: 'not an arc system' upgrades to 'fits the "
      "sphere'",
      len(certs4) == 16 and ver4,
      f"certificates = {len(certs4)}/16, all verified = {ver4}, grid = "
      f"[-2..2]^3")

# ------------------------------------------------------------------ A2b
print("\n[A2b — no five points shatter on S^2 (Radon, exact)]")
CONFIGS = [
    ("round-1 referee config",
     [(Fr(0), Fr(0), Fr(1)), (Fr(1), Fr(0), Fr(0)), (Fr(0), Fr(1), Fr(0)),
      (Fr(-1), Fr(0), Fr(0)), (Fr(36, 49), Fr(24, 49), Fr(23, 49))]),
    ("tetrahedron + antipode",
     SPH + [(Fr(-1), Fr(0), Fr(0))]),
]
a2b_ok = True
for cname, P in CONFIGS:
    assert all(dot(p, p) == 1 for p in P)
    # exact affine dependence: sum L = 0, sum L p = 0, L != 0 —
    # solve the 4x5 homogeneous system by elimination over Fractions
    rowsM = [[Fr(1)] * 5] + [[P[j][i] for j in range(5)] for i in range(3)]
    M = [r[:] for r in rowsM]
    piv = []
    rk = 0
    for c in range(5):
        pr = next((r for r in range(rk, 4) if M[r][c] != 0), None)
        if pr is None:
            continue
        M[rk], M[pr] = M[pr], M[rk]
        pv = M[rk][c]
        M[rk] = [x / pv for x in M[rk]]
        for r in range(4):
            if r != rk and M[r][c] != 0:
                f = M[r][c]
                M[r] = [a - f * b for a, b in zip(M[r], M[rk])]
        piv.append(c)
        rk += 1
    free = [c for c in range(5) if c not in piv]
    lam = [Fr(0)] * 5
    lam[free[0]] = Fr(1)
    for r, c in reversed(list(enumerate(piv))):
        lam[c] = -sum(M[r][j] * lam[j] for j in range(5) if j != c)
    ok_dep = (sum(lam) == 0
              and all(sum(lam[j] * P[j][i] for j in range(5)) == 0
                      for i in range(3))
              and any(x != 0 for x in lam))
    pos = frozenset(i for i in range(5) if lam[i] > 0)
    neg = frozenset(i for i in range(5) if lam[i] < 0)
    split = bool(pos) and bool(neg)
    print(f"  {cname}: lambda = {[str(x) for x in lam]}, Radon split "
          f"{sorted(pos)} | {sorted(neg)}")
    a2b_ok = a2b_ok and ok_dep and split
check("A2b **NO FIVE POINTS SHATTER ON S^2** — certificated: for each "
      "rational 5-point configuration an EXACT affine dependence "
      "(sum lambda = 0, sum lambda.p = 0, lambda != 0) with both sign "
      "classes non-empty.  The standard Radon argument (in the note) "
      "then shows the positive-side subset is cut off by NO halfspace: "
      "any (u, t) separating it would force t.c <= sum_pos lambda(u.p) "
      "= sum_neg |lambda|(u.p) < t.c.  Since shattering needs EVERY "
      "subset, five directions can never shatter on the sphere — caps "
      "have VC dimension 4.  (General for ANY five points in R^3: five "
      "points always carry an affine dependence, by dimension count)",
      a2b_ok, "both configurations certificated exactly")

# ------------------------------------------------------------------ A2c
print("\n[A2c — the m = 5 family on S^3]")
S3 = [(Fr(1), Fr(0), Fr(0), Fr(0)),
      (Fr(0), Fr(1), Fr(0), Fr(0)),
      (Fr(0), Fr(0), Fr(1), Fr(0)),
      (Fr(0), Fr(0), Fr(0), Fr(1)),
      (Fr(-1, 2), Fr(-1, 2), Fr(-1, 2), Fr(-1, 2))]
check("A2c-0 five points EXACTLY on the unit 3-sphere",
      all(dot(p, p) == 1 for p in S3), "norms all exactly 1")

GRID4 = [Fr(a) for a in range(-3, 4)]
certs5 = {}
missing5 = []
for k in range(6):
    for sub in combinations(range(5), k):
        S = set(sub)
        found = None
        for u in product(GRID4, repeat=4):
            if all(x == 0 for x in u):
                continue
            ds = [dot(u, p) for p in S3]
            ins = [ds[i] for i in range(5) if i in S]
            outs = [ds[i] for i in range(5) if i not in S]
            if not ins:
                found = (u, max(ds) + 1); break
            if not outs:
                found = (u, min(ds) - 1); break
            if min(ins) > max(outs):
                found = (u, (min(ins) + max(outs)) / 2); break
        if found:
            certs5[frozenset(S)] = found
        else:
            missing5.append(sub)
ver5 = all(
    {i for i in range(5) if dot(u, S3[i]) >= t} == set(S)
    for S, (u, t) in certs5.items())
check("A2c **THE m = 5 FAMILY FITS S^3**: all 32 subsets of five "
      "rational points on the unit 3-sphere realized by exact rational "
      "caps (halfspaces in R^4 shatter 5), every certificate "
      "re-verified by Fraction dot products.  With A2b this is the "
      "meter reading made concrete: the shatter-5 sky fits S^3 and "
      "PROVABLY not S^2 — beyond 3+1",
      len(certs5) == 32 and ver5 and not missing5,
      f"certificates = {len(certs5)}/32, verified = {ver5}, missing = "
      f"{missing5}, grid = [-3..3]^4")

# hygiene
_self = ast.parse(open('v10/code/d55b_sphere_calibration_exact.py').read())
_ch = [c for c in ast.walk(_self) if isinstance(c, ast.Call)
       and isinstance(c.func, ast.Name) and c.func.id == 'check']
_vac = [c for c in _ch if isinstance(c.args[1], ast.Constant)]
check("H1 AST anti-vacuity (no bare-constant predicates; LOG #403 MA-2 "
      "scope)",
      len(_ch) >= 5 and not _vac,
      f"check() calls = {len(_ch)}, bare = {len(_vac)}")

print("\n[VERDICT — D55 A2]")
print("  THE CALIBRATION LADDER, all exact: B4 fits S^2 (16 caps);")
print("  no five points EVER shatter on S^2 (Radon, certificated");
print("  twice); B5 fits S^3 (32 caps).  The meter's scale is real:")
print("  max-shatter 4 = sphere-compatible, max-shatter 5 = S^3.")

print(f"\n[d55b] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("EXIT 1")
    sys.exit(1)
print("EXIT 0")

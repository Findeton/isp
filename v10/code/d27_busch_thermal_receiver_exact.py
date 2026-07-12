#!/usr/bin/env python3
"""
d27_busch_thermal_receiver_exact.py — v10 D27: the Busch closure of the
reception theorem. Pin: note-d27-busch-closure-of-the-reception-theorem.md
(committed pre-run). Stdlib only; exact rationals; real symmetric states.
Gates B0-B4 per the pin; exit 1 on any failure.
"""
from fractions import Fraction as F
from math import isqrt

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def zeros(n): return [[F(0)]*n for _ in range(n)]
def mmul(A, B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def mtr(A): return sum(A[i][i] for i in range(len(A)))

def ratsqrt(x):
    if x < 0: return None
    n, d = x.numerator, x.denominator
    rn, rd = isqrt(n), isqrt(d)
    return F(rn, rd) if rn*rn == n and rd*rd == d else None

def tdist(A, B):
    """Exact trace distance; certificate: Delta diagonal, or Delta^3 = c*Delta
    (spectrum in {0, +sqrt(c), -sqrt(c)}). None if uncertified."""
    n = len(A)
    D = [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]
    if all(D[i][j] == 0 for i in range(n) for j in range(n)):
        return F(0)
    if all(D[i][j] == 0 for i in range(n) for j in range(n) if i != j):
        return sum(abs(D[i][i]) for i in range(n)) / 2
    D2 = mmul(D, D); D3 = mmul(D2, D)
    c = None
    for i in range(n):
        for j in range(n):
            if D[i][j] != 0:
                c = D3[i][j] / D[i][j]; break
        if c is not None: break
    if c is None or c <= 0: return None
    if any(D3[i][j] != c*D[i][j] for i in range(n) for j in range(n)):
        return None
    r = ratsqrt(c)
    if r is None: return None
    return mtr(D2) / r / 2          # ||Delta||_1 = tr(Delta^2)/sqrt(c)

def rho_eta(eta):
    r = zeros(8); r[0][0] = r[7][7] = F(1,2); r[0][7] = r[7][0] = eta/2
    return r
def rho_diag(p):
    r = zeros(8); r[0][0] = p; r[7][7] = 1 - p
    return r
ETAS = [F(0), F(1,4), F(1,2), F(3,4), F(1)]
EPAIRS = [(a, b) for i, a in enumerate(ETAS) for b in ETAS[i+1:]]
P1, P2 = F(16,25), F(144,169)

def bitA(i): return (i >> 2) & 1

# closures from D25 (re-implemented; D25's file is the pinned original)
def U_mat():
    c, s = F(3,5), F(4,5)
    U = zeros(8)
    for col in range(8):
        a, b, cc = (col >> 2) & 1, (col >> 1) & 1, col & 1
        if a == 0: U[col][col] = F(1)
        else:
            for bn in (0, 1):
                row = (a << 2) | (bn << 1) | cc
                U[row][col] += (c if bn == b else (s if bn == 1 else -s))
    return U
UM = U_mat()
def clo_U(r): return mmul(mmul(UM, r), [list(x) for x in zip(*UM)])
def clo_Qdisp(r):
    out = zeros(16)
    for i1 in range(8):
        for i2 in range(8):
            if r[i1][i2] != 0:
                out[2*i1 + bitA(i1)][2*i2 + bitA(i2)] = r[i1][i2]
    return out
def clo_Cbare(r):
    return [[r[i][j] if bitA(i) == bitA(j) else F(0) for j in range(8)] for i in range(8)]
def clo_Chalf(r):
    cb = clo_Cbare(r)
    return [[r[i][j]/2 + cb[i][j]/2 for j in range(8)] for i in range(8)]
def clo_Rcl(r):
    out = zeros(16)
    for i1 in range(8):
        for i2 in range(8):
            if r[i1][i2] != 0 and bitA(i1) == bitA(i2):
                s = bitA(i1)
                out[2*i1 + s][2*i2 + s] = r[i1][i2]
    return out

# the thermal receiver: T(rho) = U(rho (x) I/2)U†, U = CNOT(A->E)
# = 1/2 V0 rho V0† + 1/2 V1 rho V1†, V_e: |x> -> |x>|e XOR bitA(x)>
def V_iso(e):
    V = [[F(0)]*8 for _ in range(16)]
    for x in range(8):
        V[2*x + (e ^ bitA(x))][x] = F(1)
    return V
V0, V1 = V_iso(0), V_iso(1)
def clo_T(r):
    out = zeros(16)
    for e, V in ((0, V0), (1, V1)):
        for i1 in range(8):
            for i2 in range(8):
                if r[i1][i2] != 0:
                    out[2*i1 + (e ^ bitA(i1))][2*i2 + (e ^ bitA(i2))] += r[i1][i2] / 2
    return out
def marg_E(r16):
    return [[sum(r16[2*i+e1][2*i+e2] for i in range(8)) for e2 in range(2)] for e1 in range(2)]

print("[d27 Busch closure — exact]")

# B0: instrument upgrade, backward-compatible with D25's verdicts
ok0 = True
for clo, expect in ((clo_U, lambda d: d), (clo_Qdisp, lambda d: d),
                    (clo_Cbare, lambda d: F(0)), (clo_Chalf, lambda d: d/2),
                    (clo_Rcl, lambda d: F(0))):
    for a, b in EPAIRS:
        ok0 &= tdist(clo(rho_eta(a)), clo(rho_eta(b))) == expect(abs(a-b)/2)
ok0 &= tdist(rho_eta(F(1)), rho_eta(F(1,2))) == F(1,4)
check("B0 upgraded certificate (Delta^3 = c*Delta): all D25 verdicts "
      "reproduced exactly", ok0)

# B1: the thermal receiver preserves every declared pair distance
ok1 = all(tdist(clo_T(rho_eta(a)), clo_T(rho_eta(b))) == abs(a-b)/2 for a, b in EPAIRS)
ok1 &= tdist(clo_T(rho_diag(P1)), clo_T(rho_diag(P2))) == abs(P1-P2)
check("B1 thermal receiver T(rho) = U(rho x I/2)U†: every pairwise trace "
      "distance preserved EXACTLY", ok1)

# B2: T is no single isometry (pure -> mixed), yet is exactly Busch form
pure_in = rho_eta(F(1))
out = clo_T(pure_in)
purity = mtr(mmul(out, out))
ok2 = (purity == F(1,2))
rebuilt = zeros(16)
for e, V in ((0, V0), (1, V1)):
    Vr = [[sum(V[i][k]*pure_in[k][j] for k in range(8)) for j in range(8)] for i in range(16)]
    VrVt = [[sum(Vr[i][k]*V[j][k] for k in range(8)) for j in range(16)] for i in range(16)]
    rebuilt = [[rebuilt[i][j] + VrVt[i][j]/2 for j in range(16)] for i in range(16)]
ok2 &= (rebuilt == out)
vtv0 = [[sum(V0[k][i]*V0[k][j] for k in range(16)) for j in range(8)] for i in range(8)]
vtv1 = [[sum(V1[k][i]*V1[k][j] for k in range(16)) for j in range(8)] for i in range(8)]
cross = [[sum(V0[k][i]*V1[k][j] for k in range(16)) for j in range(8)] for i in range(8)]
I8 = [[F(1) if i == j else F(0) for j in range(8)] for i in range(8)]
ok2 &= vtv0 == I8 and vtv1 == I8 and all(cross[i][j] == 0 for i in range(8) for j in range(8))
check("B2 T is NO single isometry (pure GHZ -> purity exactly 1/2) yet is "
      "exactly Busch form: 1/2 V0 rho V0† + 1/2 V1 rho V1†, isometries with "
      "mutually orthogonal ranges (V0†V1 = 0, V†V = I, verified)", ok2)
print("      => D25's characterization sentence ('= exactly the isometric")
print("      dilations') is refuted by exhibit; the Busch class (mixtures of")
print("      isometries with orthogonal ranges) is the correct one. All D25")
print("      EXCLUSIONS stand (B0/B4); only the characterization is corrected.")

# B3: the classical flag receives nothing
ok3 = True
for prep in [rho_eta(e) for e in ETAS] + [rho_diag(P1), rho_diag(P2)]:
    o = clo_T(prep)
    for e, V in ((0, V0), (1, V1)):
        # branch weight = tr(Pi_e T(rho)) with Pi_e = V_e V_e†
        w = sum(sum(V[i][k]*V[j][k] for k in range(8)) * o[j][i]
                for i in range(16) for j in range(16))
        ok3 &= (w == F(1,2))
em = [marg_E(clo_T(rho_eta(e))) for e in ETAS]
ok3 &= all(m == em[0] for m in em)
check("B3 the flag receives nothing: branch weights (1/2, 1/2) for EVERY "
      "preparation; the E-flag marginal is preparation-independent", ok3)

# B4: full verdict table under the upgraded instrument
ok4 = True
for clo, preserves in ((clo_U, True), (clo_Qdisp, True), (clo_T, True),
                       (clo_Cbare, False), (clo_Chalf, False), (clo_Rcl, False)):
    pres = all(tdist(clo(rho_eta(a)), clo(rho_eta(b))) == abs(a-b)/2 for a, b in EPAIRS)
    ok4 &= (pres == preserves)
check("B4 the admitted class is the Busch class: U, Q_disp, T preserve; "
      "C_bare, C_half, R_cl contract — every D25 exclusion unchanged", ok4)

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total}: 5 substantive gates)"
      if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)

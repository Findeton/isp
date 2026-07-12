#!/usr/bin/env python3
"""
d25_reception_theorem_exact.py — v10 D25: the reception theorem (F1).
Pin: note-d25-reception-theorem.md (committed pre-run).
Stdlib only; exact rationals; all states/operators real symmetric.
Gates R1-R7 per the pin; exit 1 on any failure.
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
def madd(A, B, x=F(1)): return [[A[i][j] + x*B[i][j] for j in range(len(A))] for i in range(len(A))]
def mmul(A, B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def mtr(A): return sum(A[i][i] for i in range(len(A)))

def ratsqrt(x):
    """Exact sqrt of a nonnegative Fraction; None if not a perfect square."""
    if x < 0: return None
    n, d = x.numerator, x.denominator
    rn, rd = isqrt(n), isqrt(d)
    return F(rn, rd) if rn*rn == n and rd*rd == d else None

def tdist(A, B):
    """Exact trace distance for the verified structures; None if unverified."""
    n = len(A)
    D = madd(A, B, F(-1))
    if all(D[i][j] == 0 for i in range(n) for j in range(n)):
        return F(0)
    if all(D[i][j] == 0 for i in range(n) for j in range(n) if i != j):
        return sum(abs(D[i][i]) for i in range(n)) / 2
    D2 = mmul(D, D); D3 = mmul(D2, D); D4 = mmul(D2, D2)
    if mtr(D) == 0 and mtr(D3) == 0 and mtr(D2)**2 == 2*mtr(D4):
        r = ratsqrt(mtr(D2)/2)          # spectrum is {+x, -x}: ||D||_1 = 2|x|
        return r
    return None

# ---- the declared family ------------------------------------------------
def rho_eta(eta):
    r = zeros(8)
    r[0][0] = r[7][7] = F(1,2)
    r[0][7] = r[7][0] = eta/2
    return r

def rho_diag(p):
    r = zeros(8); r[0][0] = p; r[7][7] = 1 - p
    return r

ETAS = [F(0), F(1,4), F(1,2), F(3,4), F(1)]
EPAIRS = [(a, b) for i, a in enumerate(ETAS) for b in ETAS[i+1:]]

# ---- the closures --------------------------------------------------------
def bitA(i, n=3): return (i >> (n-1)) & 1

def U_mat():
    """Nontrivial unitary representative: controlled-Ry(A->B), (c,s)=(3/5,4/5)."""
    c, s = F(3,5), F(4,5)
    U = zeros(8)
    for col in range(8):
        a, b, cc = (col >> 2) & 1, (col >> 1) & 1, col & 1
        if a == 0:
            U[col][col] = F(1)
        else:
            for bn in (0, 1):
                row = (a << 2) | (bn << 1) | cc
                U[row][col] += (c if bn == b else (s if bn == 1 else -s))
    return U
UM = U_mat()
def clo_U(r): return mmul(mmul(UM, r), [list(x) for x in zip(*UM)])

def clo_Qdisp(r):
    """Isometry: append E in |0>, CNOT(A->E). 8 -> 16, permutation j = 2i + bitA(i)."""
    out = zeros(16)
    for i1 in range(8):
        for i2 in range(8):
            if r[i1][i2] != 0:
                out[2*i1 + bitA(i1)][2*i2 + bitA(i2)] = r[i1][i2]
    return out

def clo_Cbare(r):
    return [[r[i][j] if bitA(i) == bitA(j) else F(0) for j in range(8)] for i in range(8)]

def clo_Chalf(r):
    return madd([[x/2 for x in row] for row in r],
                [[x/2 for x in row] for row in clo_Cbare(r)])

def clo_Rcl(r):
    """Measure A, record classically: sum_s (P_s r P_s) (x) |s><s|_R. 8 -> 16."""
    out = zeros(16)
    for i1 in range(8):
        for i2 in range(8):
            if r[i1][i2] != 0 and bitA(i1) == bitA(i2):
                s = bitA(i1)
                out[2*i1 + s][2*i2 + s] = r[i1][i2]
    return out

def marg_S(r16):
    return [[r16[2*i1][2*i2] + r16[2*i1+1][2*i2+1] for i2 in range(8)] for i1 in range(8)]
def marg_E(r16):
    return [[sum(r16[2*i+e1][2*i+e2] for i in range(8)) for e2 in range(2)] for e1 in range(2)]

print("[d25 reception theorem — exact]")

# R1: family + input distances
ok1 = all(tdist(rho_eta(a), rho_eta(b)) == abs(a-b)/2 for a, b in EPAIRS)
p1, p2 = F(16,25), F(144,169)
ok1 &= tdist(rho_diag(p1), rho_diag(p2)) == abs(p1-p2)
check("R1 inputs: block structures verified; D(rho_eta, rho_eta') = |d eta|/2, "
      "D(diag p, diag p') = |d p| exactly", ok1)

# R2: THE INVARIANT TABLE
ok2 = True
verdicts = []
for name, clo, expect in (("U       (unitary)          ", clo_U,     lambda d: d),
                          ("Q_disp  (quantum receiver) ", clo_Qdisp, lambda d: d),
                          ("C_bare  (hard seal)        ", clo_Cbare, lambda d: F(0)),
                          ("C_half  (weak collapse)    ", clo_Chalf, lambda d: d/2),
                          ("R_cl    (classical receiver)", clo_Rcl,  lambda d: F(0))):
    row_ok = True
    for a, b in EPAIRS:
        din = abs(a-b)/2
        dout = tdist(clo(rho_eta(a)), clo(rho_eta(b)))
        row_ok &= (dout is not None) and dout == expect(din)
    ok2 &= row_ok
    verdicts.append((name, row_ok))
print("      invariant table (eta-pairs):  U: D_out = D_in;  Q_disp: D_out = D_in;")
print("      C_bare: D_out = 0;  C_half: D_out = D_in/2 (STRICT contraction yet")
print("      INJECTIVE — the ensemble-injectivity formalization FAILS to exclude")
print("      it, as pre-registered);  R_cl: D_out = 0.")
check("R2 the invariant: dispersal preserves total distinguishability exactly; "
      "C-class, weak collapse and classical receivers strictly contract", ok2)

# R3: mimicry — Q_disp's system marginal == C_bare output
ok3 = all(marg_S(clo_Qdisp(rho_eta(e))) == clo_Cbare(rho_eta(e)) for e in ETAS)
check("R3 mimicry: Q_disp system marginal == C_bare output at every eta "
      "(proper shadows identical; only the receiver separates them)", ok3)

# R4: receiver necessity + the correlation subtlety
ok4 = True
for a, b in EPAIRS:
    ok4 &= marg_S(clo_Qdisp(rho_eta(a))) == marg_S(clo_Qdisp(rho_eta(b)))
def xxxx_expect(r16):
    return sum(r16[i ^ 0b1111][i] for i in range(16))
ok4 &= all(xxxx_expect(clo_Qdisp(rho_eta(e))) == e for e in ETAS)
emarg_const = all(marg_E(clo_Qdisp(rho_eta(e))) == marg_E(clo_Qdisp(rho_eta(F(0)))) for e in ETAS)
ok4 &= emarg_const
print("      R4 subtlety: E's own marginal is eta-INDEPENDENT (verified) —")
print("      reception is carried by S-E correlations, not the receiver marginal.")
check("R4 receiver necessity: S-only algebra fails to separate; the E-inclusive "
      "witness <XXXX> = eta exactly; E marginal eta-free", ok4)

# R5: the value/content split on the classical receiver
d_val_in = tdist(rho_diag(p1), rho_diag(p2))
d_val_out = tdist(clo_Rcl(rho_diag(p1)), clo_Rcl(rho_diag(p2)))
ok5 = (d_val_out == d_val_in)
for a, b in EPAIRS:
    if a != b:
        ok5 &= tdist(clo_Rcl(rho_eta(a)), clo_Rcl(rho_eta(b))) == 0
check("R5 value/content split: R_cl preserves the diagonal (value) distance "
      "exactly and sends every eta (content) distance to zero — classical "
      "receivers are silent erasure with a middleman, theorem-grade", ok5)

# R6: on-family Kadison/Molnar — isometric <=> distance-preserving
iso = {"U": True, "Q_disp": True, "C_bare": False, "C_half": False, "R_cl": False}
ok6 = True
for name, clo in (("U", clo_U), ("Q_disp", clo_Qdisp), ("C_bare", clo_Cbare),
                  ("C_half", clo_Chalf), ("R_cl", clo_Rcl)):
    preserves = all(tdist(clo(rho_eta(a)), clo(rho_eta(b))) == abs(a-b)/2 for a, b in EPAIRS)
    preserves &= tdist(clo(rho_diag(p1)), clo(rho_diag(p2))) == abs(p1-p2)
    ok6 &= (preserves == iso[name])
check("R6 Kadison/Molnar on-family: a closure preserves all declared pair "
      "distances iff it is an isometric dilation [general theorem cited, "
      "LITERATURE; verified member by member here]", ok6)

# R7: the ledger identity (print)
a, b = F(1), F(1,2)
dS = tdist(marg_S(clo_Qdisp(rho_eta(a))), marg_S(clo_Qdisp(rho_eta(b))))
dT = tdist(clo_Qdisp(rho_eta(a)), clo_Qdisp(rho_eta(b)))
print(f"      R7 ledger: eta pair (1, 1/2) under Q_disp — marginal-S distance "
      f"{dS}, total distance {dT} = D_in {abs(a-b)/2}:")
print("      the entire subalgebra loss is exactly the correlation content with")
print("      the declared receiver (data processing balances the ledger).")
check("R7 ledger identity printed (marginal loss = receiver correlation, "
      "total preserved)", dS == 0 and dT == abs(a-b)/2)

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total}: 6 substantive gates + 1 print gate)"
      if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)

#!/usr/bin/env python3
"""
d44d_slab_kappa_exact.py — v10 D44d (successor 4): the slab smeared
theorem, exact kappa(m) with its zero crossing, and the interacting
cross-check. Pin: note-d44d-slab-smeared-theorem-kappa-m.md (strict).
Parents: d43a TERMINAL (#340; the machinery below is the committed
d43a exact-series arithmetic, ported verbatim — s_mul/m_mul/
exp_series/gamma_series/m_neumann_inv, the Dirac fixture builders,
the tau/D identification); the v2 p1 SS5/SS7 continuum identification
(log-smeared finite-slab construction); the root validator
`validate_minimal_interacting_gauge_matter_benchmark.py` (READ-ONLY
conventions source for the KG3 interacting fixture).

Phases: SG0 regression at ORD=12 (the d43a anchors, same code path,
re-anchored); KG1 slabs at ORD=4 (both slab readings of the pin, the
test weights pinned in the banner BEFORE verdicts); KG2 exact
kappa(m) on a 28-point rational mass grid with exact ansatz
identification; KG3 the bracket-level interacting comparison at the
validator's committed (m, g) point. SG4 precision honesty; SG5
determinism (no RNG, no wall clock — rerun byte-identical).

ORD reduction (KG1/KG2/KG3 at ORD=4) is EXACT, not an approximation:
the Delta^p coefficient of any product/inverse of truncated power
series depends only on input orders <= p (Cauchy lower-triangular
structure), and every extracted object here is a J coefficient at
Delta^2 (EXC) or Delta^4 (LT); gated in KG1 by an entrywise ORD-12
vs ORD-4 comparison and by the singleton kappa anchors.

Exit 1 ONLY on anchor/extraction breakage. KG1 w-dependence, a KG2
non-fit, and every KG3 verdict are pre-registered DELIVERED outcomes
at exit 0.

Conventions verbatim (v1 p1 / v2 p1 / d43a): periodic lattice,
2-component spinors, alpha = sigma_x, beta = sigma_z, a = 1;
H_D = sum m*beta_n + sum k_{n+1/2}; for a region R: C_R =
sum_{n in R} m*beta_n + sum_{bonds meeting R} k; B_R = H_D - C_R.
EXC: U = exp(-i D B_R). LT: U = exp(-i D B_R) exp(-i D C_R).
Gamma(U) = |U|^2 entrywise; J_R = Gamma(U_R) Gamma(U_free)^-1.
"""
import sys
import math
from fractions import Fraction as Fr
from mpmath import mp, mpf, mpc, fabs, chop, nstr

mp.dps = 50
TOL = mpf(10) ** (-30)
ORD = 12          # phase-set: 12 for SG0, 4 for KG1/KG2/KG3
L = 12
DIM = 2 * L
SX = [[0, 1], [1, 0]]

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def set_phase(ord_, l_=None, dim_=None):
    global ORD, L, DIM
    ORD = ord_
    if l_ is not None:
        L, DIM = l_, 2 * l_
    if dim_ is not None:
        DIM = dim_

def idx(n, s): return 2 * (n % L) + s

# ---- series scalars (ported verbatim from d43a) ----------------------------
def s_zero(): return [mpc(0)] * (ORD + 1)
def s_const(c):
    v = s_zero(); v[0] = mpc(c); return v
def s_add(a, b): return [a[k] + b[k] for k in range(ORD + 1)]
def s_mul(a, b):
    out = s_zero()
    for i in range(ORD + 1):
        ai = a[i]
        if ai == 0: continue
        for j in range(ORD + 1 - i):
            bj = b[j]
            if bj == 0: continue
            out[i + j] += ai * bj
    return out
def s_conj(a): return [mpc(x.real, -x.imag) for x in a]

# ---- series matrices (ported verbatim from d43a) ---------------------------
def m_mul(A, B):
    cols = {}
    for (i, j), s in B.items():
        cols.setdefault(i, []).append((j, s))
    out = {}
    for (i, k), a in A.items():
        for (j, s) in cols.get(k, []):
            prod = s_mul(a, s)
            key = (i, j)
            if key in out: out[key] = s_add(out[key], prod)
            else: out[key] = prod
    return out
def m_add(A, B):
    out = dict(A)
    for k, s in B.items():
        out[k] = s_add(out[k], s) if k in out else s
    return out
def m_identity():
    return {(i, i): s_const(1) for i in range(DIM)}
def m_neumann_inv(M):
    """Inverse of M = I + N with N constant-free: sum (-N)^j."""
    N = {}
    for (i, j), s in M.items():
        t = list(s)
        if i == j: t[0] = t[0] - 1
        if any(x != 0 for x in t): N[(i, j)] = t
    out = m_identity()
    term = m_identity()
    minusN = {k: [-x for x in v] for k, v in N.items()}
    for _ in range(ORD // 2 + 1):
        term = m_mul(term, minusN)
        if not term: break
        out = m_add(out, term)
    return out

def build_H(m, lam=None, n0=None):
    """Numeric H as {(i,j): mpc}; collar of {n0} scaled by (1-lam)."""
    H = {}
    def addH(i, j, v):
        H[(i, j)] = H.get((i, j), mpc(0)) + v
    for n in range(L):
        wm = 1 - lam if (lam is not None and n == n0) else mpf(1)
        addH(idx(n, 0), idx(n, 0), m * wm)
        addH(idx(n, 1), idx(n, 1), -m * wm)
    for n in range(L):
        wb = (1 - lam if (lam is not None and
                          (n == n0 or (n + 1) % L == n0)) else mpf(1))
        for s in range(2):
            for sp in range(2):
                if SX[sp][s] == 0: continue
                addH(idx(n + 1, sp), idx(n, s), mpc(0, -mpf(1) / 2) * wb)
                addH(idx(n, s), idx(n + 1, sp), mpc(0, mpf(1) / 2) * wb)
    return {k: v for k, v in H.items() if v != 0}

def build_H_R(m, Rset, lam):
    """d44d: the same collar construction generalized to a region set —
    sites in Rset and bonds meeting Rset carry weight (1-lam). Gated
    below against build_H on singletons (port fidelity)."""
    H = {}
    def addH(i, j, v):
        H[(i, j)] = H.get((i, j), mpc(0)) + v
    for n in range(L):
        wm = 1 - lam if (n % L) in Rset else mpf(1)
        addH(idx(n, 0), idx(n, 0), m * wm)
        addH(idx(n, 1), idx(n, 1), -m * wm)
    for n in range(L):
        wb = (1 - lam if ((n % L) in Rset or ((n + 1) % L) in Rset)
              else mpf(1))
        for s in range(2):
            for sp in range(2):
                if SX[sp][s] == 0: continue
                addH(idx(n + 1, sp), idx(n, s), mpc(0, -mpf(1) / 2) * wb)
                addH(idx(n, s), idx(n + 1, sp), mpc(0, mpf(1) / 2) * wb)
    return {k: v for k, v in H.items() if v != 0}

def num_mul(A, B):
    cols = {}
    for (i, j), v in B.items():
        cols.setdefault(i, []).append((j, v))
    out = {}
    for (i, k), a in A.items():
        for (j, v) in cols.get(k, []):
            out[(i, j)] = out.get((i, j), mpc(0)) + a * v
    return out

def exp_series(H):
    """U(Delta) = sum_k (-i Delta)^k H^k / k! as a series matrix."""
    out = {(i, i): s_const(1) for i in range(DIM)}
    P = {(i, i): mpc(1) for i in range(DIM)}
    fact = mpf(1)
    for k in range(1, ORD + 1):
        P = num_mul(P, H)
        fact *= k
        coeff = (mpc(0, -1) ** k) / fact
        for (i, j), v in P.items():
            s = out.get((i, j), s_zero())
            s = list(s)
            s[k] = s[k] + coeff * v
            out[(i, j)] = s
    return out

def gamma_series(U):
    return {k: s_mul(v, s_conj(v)) for k, v in U.items()}

def J_series(H_loc, Gfree_inv):
    return m_mul(gamma_series(exp_series(H_loc)), Gfree_inv)

def E_series(JR, JS):
    return m_mul(m_mul(m_mul(JR, JS), m_neumann_inv(JR)),
                 m_neumann_inv(JS))

def coeff_matrix(M, p):
    return {k: v[p] for k, v in M.items() if v[p] != 0}

def mnorm(D):
    return max((fabs(v) for v in D.values()), default=mpf(0))

def comm_num(X, Y):
    """[X, Y] on numeric coefficient matrices (the d43a T4 commutator;
    same 1e-45 dust drop)."""
    XY = {}
    for (i, k), a in X.items():
        for (kk, j), b in Y.items():
            if k != kk: continue
            XY[(i, j)] = XY.get((i, j), mpc(0)) + a * b
    for (i, k), a in Y.items():
        for (kk, j), b in X.items():
            if k != kk: continue
            XY[(i, j)] = XY.get((i, j), mpc(0)) - a * b
    return {k: v for k, v in XY.items() if fabs(v) > mpf(10) ** (-45)}

def tau_D_pairs(A_at, rs):
    """The d43a tau/D first-moment identification, ported verbatim with
    the base object and separation list parameterized:
    tau(delta,s,s') = sum_{r in rs} r * sum_i [A(0), A(r)]_{(i,s),(i+delta,s')}
    D(s,s') = sum_delta delta * tau(delta,s,s')."""
    A0 = A_at(0)
    tau = {}
    for r in rs:
        Ar = A_at(r)
        XY = comm_num(A0, Ar)
        for (i, j), v in XY.items():
            if fabs(v) < TOL: continue
            si = i // 2
            sj = j // 2
            delta_ = (sj - si) % L
            if delta_ > L // 2: delta_ -= L
            key = (delta_, i % 2, j % 2)
            tau[key] = tau.get(key, mpc(0)) + r * v
    D = {}
    for (delta_, a_, b_), v in tau.items():
        D[(a_, b_)] = D.get((a_, b_), mpc(0)) + delta_ * v
    return tau, D

def A_region(m, Rset, rule, Gfi, full):
    """Leading J coefficient of the region excision: EXC at Delta^2,
    LT at Delta^4 (with sub-onset validity gated by the caller)."""
    B = build_H_R(m, Rset, mpf(1))
    if rule == 'EXC':
        return coeff_matrix(m_mul(gamma_series(exp_series(B)), Gfi), 2)
    C = {}
    for k in set(full) | set(B):
        v = full.get(k, mpc(0)) - B.get(k, mpc(0))
        if v != 0: C[k] = v
    U = m_mul(exp_series(B), exp_series(C))
    return coeff_matrix(m_mul(gamma_series(U), Gfi), 4)

def J_orders_region(m, Rset, rule, Gfi, full, orders):
    """Norms of J coefficients at the given orders (sub-onset gates)."""
    B = build_H_R(m, Rset, mpf(1))
    if rule == 'EXC':
        J = m_mul(gamma_series(exp_series(B)), Gfi)
    else:
        C = {}
        for k in set(full) | set(B):
            v = full.get(k, mpc(0)) - B.get(k, mpc(0))
            if v != 0: C[k] = v
        J = m_mul(gamma_series(m_mul(exp_series(B), exp_series(C))), Gfi)
    return [mnorm(coeff_matrix(J, p)) for p in orders]

# ---- exact-rational recognition (SG4-declared float entry point 2) ---------
def to_fr_exact(x):
    """Exact Fraction of the binary dps-50 value (no rounding)."""
    sign, man, exp, bc = x._mpf_
    if man == 0: return Fr(0)
    v = Fr(int(man), 1)
    v = v * (2 ** exp) if exp >= 0 else v / (2 ** (-exp))
    return -v if sign else v

DEN_CAP = 10 ** 15
REC_MAXERR = [mpf(0)]
REC_MAXDEN = [1]
def recognize(x):
    """dps-50 real -> Fraction via best bounded-denominator approximation
    (continued-fraction limit_denominator, cap 10^15); gated at 1e-30."""
    fr = to_fr_exact(x).limit_denominator(DEN_CAP)
    err = fabs(x - mpf(fr.numerator) / fr.denominator)
    if err < TOL:
        if err > REC_MAXERR[0]: REC_MAXERR[0] = err
        if fr.denominator > REC_MAXDEN[0]: REC_MAXDEN[0] = fr.denominator
        return fr
    return None

def fr2mp(fr): return mpf(fr.numerator) / fr.denominator

KAPPA_REF = {0.5: Fr(13, 2304), 1.0: Fr(-1, 72)}

# ============================================================================
print("[d44d — the slab smeared theorem, exact kappa(m), the interacting cross-check]")
print("  banner: exact truncated-series arithmetic (the d43a machinery, ported")
print("  verbatim); mp.dps = 50; threshold 1e-30; SG0 at ORD = 12 / L = 12 (the")
print("  d43a code path, re-anchored); KG1/KG2/KG3 at ORD = 4 (EXACT truncation:")
print("  a Delta^p coefficient of series products/inverses depends only on input")
print("  orders <= p; gated below at 1e-40 entrywise and on the kappa anchors).")
print("  Exit 1 ONLY on anchor/extraction breakage; KG1 w-dependence, KG2 non-fit,")
print("  and every KG3 verdict are pre-registered DELIVERED outcomes at exit 0.")
print("  Deterministic: no RNG, no wall clock; rerun byte-identical (SG5).")
print()
print("  PINNED TEST-WEIGHT FAMILY (KG1; declared BEFORE any verdict):")
print("  log-uniform site weights over the slab: for width w, phi_j =")
print("  (1/(j+1)) / H_w at site base+j, j = 0..w-1, H_w = sum_{k=1..w} 1/k.")
print("  Exact values: w=1: (1); w=2: (2/3, 1/3); w=3: (6/11, 3/11, 2/11);")
print("  w=4: (12/25, 6/25, 4/25, 3/25).")
print("  The weights enter as the v2 p1 SS7 log-smeared slab observable read at")
print("  leading coefficient order (log J_n = Delta^p A_n + h.o., so the SS7")
print("  log-smear IS the phi-weighted singleton-coefficient sum at this order):")
print("    COMPOSITE arm:  Abar_w(b) = sum_{j<w} phi_j A^rule_{{b+j}}.")
print("  The pin's literal 'regions R = contiguous blocks' reading is run as the")
print("    BLOCK arm:      A^rule_{R_w(b)},  R_w(b) = {b..b+w-1},")
print("                    C_R = sum_{n in R} m beta_n + sum_{bonds meeting R} k.")
print("  Identification (both arms): the d43a tau first-moment construction on")
print("  the pair at bases (0, r): tau(delta,s,s') = sum_{r=1..rmax} r *")
print("  sum_i [A(0), A(r)]_{(i,s),(i+delta,s')}; D(s,s') = sum_delta delta*tau;")
print("  rmax = w+1 (EXC) / w+3 (LT) = the exact kernel-support bound; the")
print("  rmax+1 completeness slot is gated ZERO on every wrap-clean cell.")
print("  Declared: by translation covariance the phi-weighted mean pair")
print("  separation equals the base separation r exactly, so on wrap-clean")
print("  lattices the composite-arm collapse constant is weight-family")
print("  independent (the cancellation-order content of the conversion note);")
print("  the log-uniform family is the pinned instance run here.")
print()
print("  WRAP CENSUS (support lemma, declared BEFORE verdicts): the LT defect")
print("  kernel of either arm spans sites [b-2, b+w+1]; the pair at separation r")
print("  is seam-free iff r <= w+3 (front bound) and r < L-(w+3) (back bound).")
print("  At L=12 these overlap for w in {3,4}: the LT cells (L=12, w=3|4,")
print("  COMPOSITE|BLOCK) are WRAP-CONTAMINATED — excluded from the theorem")
print("  gate, delivered with flag WRAP, with the L=16 twins carrying the clean")
print("  statement. All EXC cells (kernel [b-1, b+w], rmax = w+1) and all L=16")
print("  cells are seam-free.")
print()
print("  SG4 FLOAT ENTRY POINTS (enumerated): (1) all series arithmetic is")
print("  mpmath binary at dps 50 (rational inputs with non-power-of-2")
print("  denominators are 1e-50-rounded on entry; hence gates at 1e-30, never")
print("  equality on mpf); (2) kappa/constant recognition: exact binary value ->")
print("  Fraction via continued-fraction best approximation, denominator cap")
print("  1e15, gated |x - p/q| < 1e-30 (max residual and max denominator")
print("  reported in SG4); downstream ansatz solve/verify runs in EXACT Fraction")
print("  arithmetic with ZERO tolerance on the recognized rationals; (3) the KG3")
print("  fixture constants (7/10, 1/2, 9/10, -2/5, 11/10, 1/5) enter as dps-50")
print("  mpf. No other float entry points exist.")

# ============================================================================
print("\n[SG0 — regression at ORD 12, L 12: the d43a anchors, same code path]")
print("  (SG0 re-runs the d43a ANCHORS; the d43a T2/T4 verdict deliveries are")
print("   committed results and are not re-delivered here.)")
set_phase(12, 12)

m_a = mpf(1) / 2
n0 = 3
H_full = build_H(m_a)
Gfree_inv = m_neumann_inv(gamma_series(exp_series(H_full)))

# port-fidelity: the generalized region builder reproduces build_H on singletons
pf_ok = True
for lamv in (mpf(1), mpf(1) / 2):
    Ha = build_H(m_a, lam=lamv, n0=n0)
    Hb = build_H_R(m_a, {n0}, lamv)
    pf_ok &= set(Ha) == set(Hb) and all(
        fabs(Ha[k] - Hb[k]) == 0 for k in Ha)
check("SG0-PF the generalized region collar builder == the d43a singleton "
      "builder entrywise (lam = 1 and 1/2), exact", pf_ok)

# ---- AN1: the EXC singleton A(1) -------------------------------------------
J_exc = J_series(build_H(m_a, lam=mpf(1), n0=n0), Gfree_inv)
A1 = coeff_matrix(J_exc, 2)
okA = (fabs(A1.get((idx(n0, 0), idx(n0, 0)), 0) - mpf(1) / 2) < TOL
       and fabs(A1.get((idx(n0, 1), idx(n0, 1)), 0) - mpf(1) / 2) < TOL)
for pm in (-1, 1):
    for s in range(2):
        okA &= fabs(A1.get((idx(n0 + pm, 1 - s), idx(n0, s)), 0)
                    + mpf(1) / 4) < TOL
        okA &= fabs(A1.get((idx(n0 + pm, s), idx(n0 + pm, s)), 0)
                    - mpf(1) / 4) < TOL
        okA &= fabs(A1.get((idx(n0 + pm, s), idx(n0, s)), 0)) < TOL
colsum = sum(A1.get((i, idx(n0, 0)), mpc(0)) for i in range(DIM))
okA &= fabs(colsum) < TOL
check("AN1 the EXC singleton A(1): diag 1/2 at n0, 1/4 at n0+-1, "
      "-1/4 spin-flip off-diagonals, same-spin zero, columns sum "
      "zero (v2 p1 exact entries)", okA, "exact at 1e-30")

# ---- AN4: lambda scaling ----------------------------------------------------
lam = mpf(1) / 2
c_lam = lam * (2 - lam)
A1l = coeff_matrix(J_series(build_H(m_a, lam=lam, n0=n0), Gfree_inv), 2)
ok4 = all(fabs(A1l.get(k, 0) - c_lam * A1.get(k, 0)) < TOL
          for k in set(A1) | set(A1l))
check("AN4 the lambda family at lam = 1/2: A(1)_lam = (3/4) A(1) "
      "entrywise (c_lam = lam(2-lam))", ok4, "all entries")

# ---- AN2: the documented d = 1 defect --------------------------------------
JR1 = J_series(build_H(m_a, lam=mpf(1), n0=0), Gfree_inv)
JS1 = J_series(build_H(m_a, lam=mpf(1), n0=1), Gfree_inv)
E1 = E_series(JR1, JS1)
B14 = coeff_matrix(E1, 4)
okB = (fabs(B14.get((idx(0, 0), idx(1, 1)), 0) + mpf(1) / 8) < TOL
       and fabs(B14.get((idx(1, 1), idx(0, 0)), 0) - mpf(1) / 8) < TOL
       and fabs(B14.get((idx(0, 0), idx(1, 0)), 0)) < TOL)
check("AN2 the documented d = 1 EXC defect: Delta^4 entry "
      "((0,up),(1,dn)) = -1/8 exactly, transpose +1/8, same-spin 0 "
      "(v1 p1's worked case)", okB,
      f"entry = {chop(B14.get((idx(0, 0), idx(1, 1)), 0))}")

# ---- AN3: the LT onset law + completeness (El orders only; the d43a T2/T4
# ---- verdict deliveries are committed, not re-run) --------------------------
ok3 = True
base = 3
for m in (mpf(1) / 2, mpf(1)):
    Hm = build_H(m)
    Gfi = m_neumann_inv(gamma_series(exp_series(Hm)))
    def lt_J(nn):
        B = build_H(m, lam=mpf(1), n0=nn)
        C = {}
        full = build_H(m)
        for k in set(full) | set(B):
            v = full.get(k, mpc(0)) - B.get(k, mpc(0))
            if v != 0: C[k] = v
        U = m_mul(exp_series(B), exp_series(C))
        return m_mul(gamma_series(U), Gfi)
    for d in (2, 3):
        p_lt = 2 * max(4, d)
        El = E_series(lt_J(base), lt_J(base + d))
        for p in (4, 6):
            if p < p_lt:
                ok3 &= mnorm(coeff_matrix(El, p)) < TOL
        for p_ in (3, 5, 7):
            ok3 &= mnorm(coeff_matrix(El, p_)) < TOL
off_ok = all(fabs(v) < TOL for (i, j), v in A1.items()
             if abs(i // 2 - n0) > 1 or abs(j // 2 - n0) > 1)
check("AN3 the LT onset law + completeness: E^LT orders 3-7 below onset "
      "vanish exactly at every (m, d in {2,3}); A(1) vanishes off the "
      "collar support", ok3 and off_ok,
      "sub-onset, odd-order, and off-support all zero at 1e-30")

# ---- T5 anchors: singleton tau/D, kappa refs, signed tables, delta-odd -----
REF_LT = {0.5: {(1, 'flip'): Fr(1, 9216), (-1, 'flip'): Fr(-1, 9216),
                (2, 'same'): Fr(-23, 9216), (-2, 'same'): Fr(23, 9216),
                (3, 'flip'): Fr(-1, 1024), (-3, 'flip'): Fr(1, 1024),
                (4, 'same'): Fr(1, 512), (-4, 'same'): Fr(-1, 512)},
          1.0: {(1, 'flip'): Fr(-19, 1152), (-1, 'flip'): Fr(19, 1152),
                (2, 'same'): Fr(-17, 2304), (-2, 'same'): Fr(17, 2304),
                (3, 'flip'): Fr(1, 128), (-3, 'flip'): Fr(-1, 128),
                (4, 'same'): Fr(1, 512), (-4, 'same'): Fr(-1, 512)}}

def tau_D_sg0(m, rule):
    Hm = build_H(m)
    Gfi = m_neumann_inv(gamma_series(exp_series(Hm)))
    full = build_H(m)
    def A_at(nn):
        return A_region(m, {nn % L}, rule, Gfi, full)
    return tau_D_pairs(A_at, (1, 2, 3, 4))

A_LT_ORD12 = None      # stashed for the KG1 truncation gate
t5_ok = True
t5_det = []
for m in (mpf(1) / 2, mpf(1)):
    tauE, DE = tau_D_sg0(m, 'EXC')
    tauL, DL = tau_D_sg0(m, 'LT')
    okE = (fabs(DE.get((0, 0), 0) - 1) < TOL
           and fabs(DE.get((1, 1), 0) - 1) < TOL
           and fabs(DE.get((0, 1), 0) + 1) < TOL
           and fabs(DE.get((1, 0), 0) + 1) < TOL)
    kref = KAPPA_REF[float(m)]
    okL = all(fabs(DL.get((a_, b_), 0)
                   - fr2mp(kref) * (1 if a_ == b_ else -1)) < TOL
              for a_ in (0, 1) for b_ in (0, 1))
    okT = True
    got_ch = {}
    for (delta_, a_, b_), v in tauL.items():
        ch = 'flip' if a_ != b_ else 'same'
        if (a_, b_) in ((0, 1), (0, 0)) and fabs(v) > TOL:
            got_ch[(delta_, ch)] = v
    ref = REF_LT[float(m)]
    okT &= set(got_ch) == set(ref)
    for k, rv in ref.items():
        okT &= fabs(got_ch.get(k, mpc(0)) - fr2mp(rv)) < TOL
    # delta-odd, explicit (B6): tau(-delta,s,s') = -tau(delta,s,s') per channel
    okO = True
    for tt in (tauE, tauL):
        for (delta_, a_, b_), v in tt.items():
            okO &= fabs(v + tt.get((-delta_, a_, b_), mpc(0))) < TOL
    t5_ok &= okE and okL and okT and okO
    t5_det.append(f"m={float(m)}: EXC D=(I-sx) {okE}; LT D={kref}*(I-sx) "
                  f"{okL}; table {okT}; delta-odd {okO}")
sign_flip = (KAPPA_REF[0.5] > 0) and (KAPPA_REF[1.0] < 0)
check("T5 anchors re-run: EXC D = 1*(I - sigma_x) exactly; LT D = "
      "kappa(m)*(I - sigma_x) with kappa(1/2) = 13/2304, kappa(1) = -1/72 "
      "(sign flip); the LT tau tables match the committed signed channel "
      "values; delta-odd verified in every channel of both rules",
      t5_ok and sign_flip, "; ".join(t5_det))

# stash the ORD-12 LT singleton coefficient for the truncation gate
A_LT_ORD12 = A_region(mpf(1) / 2, {n0}, 'LT', Gfree_inv, H_full)

# ============================================================================
print("\n[KG1 — slabs at ORD 4: both arms, w in {1,2,3,4}, L in {12,16}]")
print("  (L = 16 RUN: exact-series cost at ORD 4 permits it — declared.)")
set_phase(4, 12)
H_full4 = build_H(m_a)
Gfi4 = m_neumann_inv(gamma_series(exp_series(H_full4)))
A_LT_ORD4 = A_region(m_a, {n0}, 'LT', Gfi4, H_full4)
tr_dev = mnorm({k: A_LT_ORD4.get(k, mpc(0)) - A_LT_ORD12.get(k, mpc(0))
                for k in set(A_LT_ORD4) | set(A_LT_ORD12)})
check("KG1-T the ORD-reduction is exact: A^LT (m=1/2, n0=3, L=12) at "
      "ORD 12 == at ORD 4 entrywise", tr_dev < mpf(10) ** (-40),
      f"max dev = {nstr(tr_dev, 3)} (gate 1e-40)")

PHI = {w: [Fr(1, j + 1) for j in range(w)] for w in (1, 2, 3, 4)}
for w in PHI:
    hs = sum(PHI[w])
    PHI[w] = [p / hs for p in PHI[w]]
RMAX = {'EXC': (lambda w: w + 1), 'LT': (lambda w: w + 3)}

def wrapped(rule, Lv, w):
    rmax = RMAX[rule](w)
    span = (w + 3) if rule == 'LT' else (w + 1)
    return rmax >= Lv - span      # back-contact reaches the r-sum

cells = []                        # (L, m, w, arm, rule, cfr, ray, slot, wflag)
kg1_extract_ok = True
kg1_rec_ok = True
kg1_anchor_ok = True
kg1_subonset_ok = True
for Lv in (12, 16):
    set_phase(4, Lv)
    for mval in (mpf(1) / 2, mpf(1)):
        full = build_H(mval)
        Gfi = m_neumann_inv(gamma_series(exp_series(full)))
        singA = {}
        for rule in ('EXC', 'LT'):
            for nn in range(Lv):
                singA[(rule, nn)] = A_region(mval, {nn}, rule, Gfi, full)
        # LT sub-onset validity on a representative singleton and on every
        # block width (extraction-class gates)
        zs = J_orders_region(mval, {0}, 'LT', Gfi, full, (1, 2, 3))
        kg1_subonset_ok &= all(z < TOL for z in zs)
        for w in (2, 3, 4):
            zb = J_orders_region(mval, {j for j in range(w)}, 'LT', Gfi,
                                 full, (1, 2, 3))
            kg1_subonset_ok &= all(z < TOL for z in zb)
        kref = KAPPA_REF[float(mval)]
        for w in (1, 2, 3, 4):
            phif = [fr2mp(p) for p in PHI[w]]
            def A_comp(b, rule):
                out = {}
                for j in range(w):
                    for k, v in singA[(rule, (b + j) % Lv)].items():
                        out[k] = out.get(k, mpc(0)) + phif[j] * v
                return out
            def A_blk(b, rule):
                return A_region(mval, {(b + j) % Lv for j in range(w)},
                                rule, Gfi, full)
            arms = (('COMPOSITE', A_comp),) if w == 1 else \
                   (('COMPOSITE', A_comp), ('BLOCK', A_blk))
            for arm, A_of in arms:
                for rule in ('EXC', 'LT'):
                    rmax = RMAX[rule](w)
                    tau, D = tau_D_pairs(lambda r: A_of(r, rule),
                                         tuple(range(1, rmax + 1)))
                    slot = mnorm(comm_num(A_of(0, rule),
                                          A_of(rmax + 1, rule)))
                    d00 = D.get((0, 0), mpc(0))
                    ray = (fabs(d00 - D.get((1, 1), mpc(0))) < TOL
                           and fabs(D.get((0, 1), mpc(0))
                                    - D.get((1, 0), mpc(0))) < TOL
                           and fabs(d00 + D.get((0, 1), mpc(0))) < TOL
                           and fabs(d00.imag) < TOL)
                    wflag = wrapped(rule, Lv, w)
                    cfr = recognize(d00.real)
                    cells.append((Lv, float(mval), w, arm, rule, cfr,
                                  ray, slot, wflag))
                    if not wflag:
                        kg1_extract_ok &= ray and slot < TOL
                        if cfr is None: kg1_rec_ok = False
                    if w == 1:
                        want = Fr(1) if rule == 'EXC' else kref
                        kg1_anchor_ok &= (
                            fabs(d00.real - fr2mp(want)) < TOL and ray)
                    tag = "WRAP" if wflag else "clean"
                    cstr = str(cfr) if cfr is not None else nstr(d00.real, 30)
                    print(f"  L={Lv} m={float(mval)} w={w} "
                          f"{arm:9s} {rule}: c = {cstr:>12s}  ray={'T' if ray else 'F'}"
                          f"  slot(r={rmax+1}) = {nstr(slot, 3)}  [{tag}]")
check("KG1-A the w = 1 cells reproduce the singleton anchors at both L "
      "(EXC: 1; LT: 13/2304 at m=1/2, -1/72 at m=1)", kg1_anchor_ok,
      "exact at 1e-30")
check("KG1-B LT sub-onset validity at slab scope: J^LT orders 1-3 vanish "
      "for singletons and every block width at both L, both masses",
      kg1_subonset_ok, "all below 1e-30")
check("KG1-C extraction complete: every wrap-clean cell has exact ray "
      "collapse D = c*(I - sigma_x) and a ZERO completeness slot; every "
      "clean constant recognized as an exact rational",
      kg1_extract_ok and kg1_rec_ok and len(cells) == 56,
      f"{len(cells)} cells (48 clean + 8 declared WRAP)")

# the delivered theorem verdicts (NOT exit-gating; the pin's gate content)
comp_exc = sorted({str(c[5]) for c in cells
                   if c[3] == 'COMPOSITE' and c[4] == 'EXC' and not c[8]})
comp_lt_ok = all(c[5] == KAPPA_REF[c[1]] for c in cells
                 if c[3] == 'COMPOSITE' and c[4] == 'LT' and not c[8])
blk_lt_ok = all(c[5] == KAPPA_REF[c[1]] for c in cells
                if c[3] == 'BLOCK' and c[4] == 'LT' and not c[8])
blk_exc = {}
for c in cells:
    if c[3] == 'BLOCK' and c[4] == 'EXC' and not c[8]:
        blk_exc.setdefault(c[2], set()).add(c[5])
blk_exc_law = all(len(v) == 1 and next(iter(v)) == Fr(w + 1, 2) ** 2
                  for w, v in blk_exc.items())
comp_green = (comp_exc == ['1'] and comp_lt_ok)
kg1_v1 = ("HOLDS: COMPOSITE (the SS7 log-smeared slab): every wrap-clean "
          "cell collapses to the SINGLETON ray and constant — EXC = 1 and "
          "LT = kappa(m) at ALL w in {1,2,3,4} (all w at L=16; w <= 2 plus "
          "all EXC at L=12): slab-width INDEPENDENCE"
          if comp_green else "FAILED at composite cells (see table)")
kg1_v2 = (("LT = kappa(m) w-INDEPENDENT at every clean cell; EXC = "
           "((w+1)/2)^2 exactly (1, 9/4, 4, 25/4; mass- and L-independent) "
           "— DELIVERED FINDING: the literal block-region EXC normalization "
           "carries the collar-length square while its ray is unchanged and "
           "the LT constant is untouched")
          if (blk_lt_ok and blk_exc_law) else
          f"BLOCK cells: LT w-indep = {blk_lt_ok}; EXC constants "
          f"{sorted((w, sorted(map(str, v))) for w, v in blk_exc.items())}")
print(f"  [KG1 THEOREM] composite arm: {kg1_v1}")
print(f"  [KG1 BLOCK ARM] {kg1_v2}")
wrap_cells = [(c[0], c[1], c[2], c[3],
               str(c[5]) if c[5] is not None else "unrecognized")
              for c in cells if c[8]]
print("  [KG1 WRAP RECORD] the 8 declared L=12 LT wrap cells (finite-seam "
      "artifacts, not theorem statements; their L=16 twins are clean and "
      "collapse exactly): " + "; ".join(
          f"(L={a},m={b},w={ww},{ar}): {cs}" for a, b, ww, ar, cs in wrap_cells))

# ============================================================================
print("\n[KG2 — exact kappa(m) at ORD 4, L 12: 28 rational masses on (0, 2]]")
set_phase(4, 12)
MGRID = [Fr(1, 16), Fr(1, 8), Fr(3, 16), Fr(1, 4), Fr(3, 8), Fr(7, 16),
         Fr(1, 2), Fr(13, 24), Fr(9, 16), Fr(5, 8), Fr(11, 16), Fr(17, 24),
         Fr(3, 4), Fr(19, 24), Fr(13, 16), Fr(7, 8), Fr(15, 16), Fr(23, 24),
         Fr(1), Fr(17, 16), Fr(9, 8), Fr(5, 4), Fr(11, 8), Fr(3, 2),
         Fr(13, 8), Fr(7, 4), Fr(15, 8), Fr(2)]

def kappa_pipeline(mfr):
    """Both rules' singleton tau/D at mass mfr; returns (kappaLT_mpf,
    rayLT, excD00, rayEXC)."""
    mv = fr2mp(mfr)
    full = build_H(mv)
    Gfi = m_neumann_inv(gamma_series(exp_series(full)))
    out = {}
    for rule in ('EXC', 'LT'):
        cache = {}
        def A_at(r):
            if r not in cache:
                cache[r] = A_region(mv, {r % L}, rule, Gfi, full)
            return cache[r]
        tau, D = tau_D_pairs(A_at, (1, 2, 3, 4))
        d00 = D.get((0, 0), mpc(0))
        ray = (fabs(d00 - D.get((1, 1), mpc(0))) < TOL
               and fabs(D.get((0, 1), mpc(0)) - D.get((1, 0), mpc(0))) < TOL
               and fabs(d00 + D.get((0, 1), mpc(0))) < TOL
               and fabs(d00.imag) < TOL)
        out[rule] = (d00.real, ray)
    return out['LT'][0], out['LT'][1], out['EXC'][0], out['EXC'][1]

kg2_ray_ok = True
kg2_exc_ok = True
kg2_rec_ok = True
KTAB = {}
print("  m        kappa(m) (recognized exact)        kappa(m) (dps-50)")
for mfr in MGRID:
    kv, rayL, ev, rayE = kappa_pipeline(mfr)
    kg2_ray_ok &= rayL and rayE
    kg2_exc_ok &= fabs(ev - 1) < TOL
    fr = recognize(kv)
    if fr is None: kg2_rec_ok = False
    KTAB[mfr] = fr
    print(f"  {str(mfr):7s}  {str(fr):>22s}  {nstr(kv, 30)}")
check("KG2-A the anchor masses reproduce the committed singleton kappas "
      "exactly: kappa(1/2) = 13/2304, kappa(1) = -1/72",
      KTAB[Fr(1, 2)] == Fr(13, 2304) and KTAB[Fr(1)] == Fr(-1, 72))
check("KG2-B ray collapse D = kappa*(I - sigma_x) at EVERY grid mass, "
      "both rules; EXC constant = 1 at EVERY grid mass (the EXC side is "
      "mass-blind)", kg2_ray_ok and kg2_exc_ok, "all 28 masses at 1e-30")
check("KG2-C every grid kappa recognized as an exact rational "
      "(denominator cap 1e15, residual gate 1e-30)", kg2_rec_ok,
      f"max residual {nstr(REC_MAXERR[0], 3)}, max den {REC_MAXDEN[0]}")

# ---- exact ansatz identification (Fraction arithmetic, zero tolerance) -----
def solve_lin_fr(Amat, bvec):
    n = len(bvec)
    M = [row[:] + [bvec[i]] for i, row in enumerate(Amat)]
    for c in range(n):
        piv = None
        for r in range(c, n):
            if M[r][c] != 0: piv = r; break
        if piv is None: return None
        M[c], M[piv] = M[piv], M[c]
        pv = M[c][c]
        M[c] = [e / pv for e in M[c]]
        for r in range(n):
            if r == c: continue
            f = M[r][c]
            if f:
                M[r] = [M[r][k] - f * M[c][k] for k in range(n + 1)]
    return [M[r][n] for r in range(n)]

pts_x = [(m * m, k) for m, k in KTAB.items()] if kg2_rec_ok else []
pts_m = [(m, k) for m, k in KTAB.items()] if kg2_rec_ok else []
NPTS = len(pts_x)
census = []
hit = None
# scan order (declared): polynomials in x = m^2, deg 0..7; polynomials in m,
# deg 0..13; rationals P/Q in x then in m, den deg 1..6, num deg 0..6,
# ordered by total degree — every candidate must satisfy the >= 2x
# overdetermination bound NPTS >= 2*(#unknowns); first exact hit stops.
def try_poly(pts, deg):
    sub = pts[:deg + 1]
    A = [[x ** p for p in range(deg + 1)] for x, _ in sub]
    co = solve_lin_fr(A, [k for _, k in sub])
    if co is None: return None
    if all(sum(c * x ** p for p, c in enumerate(co)) == k for x, k in pts):
        return co
    return None

def try_rat(pts, dn, dd):
    nun = dn + dd + 1
    sub = pts[:nun]
    A = [[x ** p for p in range(dn + 1)] + [-k * x ** q
         for q in range(1, dd + 1)] for x, k in sub]
    co = solve_lin_fr(A, [k for _, k in sub])
    if co is None: return None
    P = co[:dn + 1]
    Q = [Fr(1)] + co[dn + 1:]
    for x, k in pts:
        qv = sum(c * x ** p for p, c in enumerate(Q))
        pv = sum(c * x ** p for p, c in enumerate(P))
        if qv == 0 or pv != k * qv: return None
    return (P, Q)

for deg in range(0, 8):
    if not kg2_rec_ok: break
    if NPTS < 2 * (deg + 1):
        census.append(f"x-poly[{deg}]: skipped (overdetermination < 2x)")
        continue
    co = try_poly(pts_x, deg)
    if co is not None:
        hit = ('poly-x', deg, co)
        census.append(f"x-poly[{deg}]: EXACT on all {NPTS} points")
        break
    census.append(f"x-poly[{deg}]: no")
if hit is None and kg2_rec_ok:
    for deg in range(0, 14):
        if NPTS < 2 * (deg + 1):
            census.append(f"m-poly[{deg}]: skipped"); continue
        co = try_poly(pts_m, deg)
        if co is not None:
            hit = ('poly-m', deg, co)
            census.append(f"m-poly[{deg}]: EXACT on all {NPTS} points")
            break
        census.append(f"m-poly[{deg}]: no")
if hit is None and kg2_rec_ok:
    for tot in range(1, 13):
        if hit: break
        for dd in range(1, 7):
            dn = tot - dd
            if dn < 0 or dn > 6: continue
            if NPTS < 2 * (dn + dd + 1):
                census.append(f"x-rat[{dn}/{dd}]: skipped"); continue
            pq = try_rat(pts_x, dn, dd)
            if pq is not None:
                hit = ('rat-x', (dn, dd), pq)
                census.append(f"x-rat[{dn}/{dd}]: EXACT on all {NPTS} points")
                break
            census.append(f"x-rat[{dn}/{dd}]: no")
if hit is None and kg2_rec_ok:
    for tot in range(1, 13):
        if hit: break
        for dd in range(1, 7):
            dn = tot - dd
            if dn < 0 or dn > 6: continue
            if NPTS < 2 * (dn + dd + 1):
                census.append(f"m-rat[{dn}/{dd}]: skipped"); continue
            pq = try_rat(pts_m, dn, dd)
            if pq is not None:
                hit = ('rat-m', (dn, dd), pq)
                census.append(f"m-rat[{dn}/{dd}]: EXACT on all {NPTS} points")
                break
            census.append(f"m-rat[{dn}/{dd}]: no")
print("  ansatz census (scan order declared above): " + "; ".join(census))

def isqrt_exact(n):
    """Integer square root if n is a perfect square, else None."""
    if n < 0: return None
    r = math.isqrt(int(n))
    return r if r * r == n else None

def bracket_64(xstar):
    """The width-1/64 rational bracket around m* = sqrt(xstar), xstar a
    positive Fraction: floor(64 m*) = isqrt(floor(4096 p / q)) exactly."""
    p, q = xstar.numerator, xstar.denominator
    k = math.isqrt(4096 * p // q)
    if Fr(k, 64) ** 2 == xstar or Fr(k + 1, 64) ** 2 == xstar:
        return None          # crossing on the 1/64 grid — widen by hand
    return (Fr(k, 64), Fr(k + 1, 64))

kg2_verdict = ""
kg2_cross_ok = True
cross_brackets = []
if hit is not None and hit[0] == 'poly-x':
    deg, co = hit[1], hit[2]
    lcm = 1
    for c in co:
        lcm = lcm * c.denominator // math.gcd(lcm, c.denominator)
    ic = [int(c * lcm) for c in co]     # integer poly in x, ascending
    print(f"  IDENTIFIED (delivered): kappa(m) = "
          + " + ".join(f"({c})*m^{2*p}" for p, c in enumerate(co) if c != 0))
    print(f"  integer numerator polynomial N(x), x = m^2 (denominator {lcm}): "
          + " + ".join(f"({c})*x^{p}" for p, c in enumerate(ic) if c != 0))
    # overdetermination statement
    print(f"  overdetermination: {NPTS} points / {deg + 1} coefficients = "
          f"{Fr(NPTS, deg + 1)}x (>= 2x pinned); solved from the first "
          f"{deg + 1} grid points, verified with ZERO tolerance on the "
          f"remaining {NPTS - deg - 1}")
    # exact roots (degree-2 case: full closed form)
    if deg == 2:
        a2, a1, a0 = ic[2], ic[1], ic[0]
        disc = a1 * a1 - 4 * a2 * a0
        sq = isqrt_exact(disc)
        if sq is not None:
            x1 = Fr(-a1 - sq, 2 * a2)
            x2 = Fr(-a1 + sq, 2 * a2)
            xlo, xhi = (x1, x2) if x1 < x2 else (x2, x1)
            print(f"  discriminant = {disc} = {sq}^2 (perfect square): "
                  f"N(x) has EXACT RATIONAL roots x = {xlo}, {xhi}")
            print(f"  factorization check: N(x) == {a2}*(x - ({xlo}))*"
                  f"(x - ({xhi})) : "
                  + str([a2 * 1, -a2 * (xlo + xhi), a2 * xlo * xhi] ==
                        [Fr(ic[2]), Fr(ic[1]), Fr(ic[0])]))
            def sgn(c): return f"- {abs(c)}" if c < 0 else f"+ {c}"
            kg2_verdict = (f"kappa(m) = ({ic[2]}*m^4 {sgn(ic[1])}*m^2 "
                           f"{sgn(ic[0])})/{lcm} with EXACT zero crossings "
                           f"at m^2 = {xlo} and m^2 = {xhi}, i.e. m = "
                           f"sqrt({xlo}) and m = sqrt({xhi})")
            if a2 == xlo.denominator * xhi.denominator:
                f1 = (xlo.denominator, xlo.numerator)
                f2 = (xhi.denominator, xhi.numerator)
                fac_ok = ([f1[0] * f2[0], -(f1[0] * f2[1] + f2[0] * f1[1]),
                           f1[1] * f2[1]] == [ic[2], ic[1], ic[0]])
                print(f"  equivalently {lcm}*kappa(m) = "
                      f"({f1[0]}*m^2 - {f1[1]})*({f2[0]}*m^2 - {f2[1]}) "
                      f"(exact expansion check: {fac_ok})")
            print("  crossings as reals: m*1 = sqrt(" + str(xlo) + ") = "
                  + nstr(mp.sqrt(fr2mp(xlo)), 25) + "; m*2 = sqrt("
                  + str(xhi) + ") = " + nstr(mp.sqrt(fr2mp(xhi)), 25))
            # the pinned bracket (1/2, 1): which crossing lands inside
            inb = [x for x in (xlo, xhi) if Fr(1, 4) < x < Fr(1)]
            oth = [x for x in (xlo, xhi) if x not in inb]
            print(f"  the pinned sign-change bracket (1/2, 1) in m "
                  f"(<-> (1/4, 1) in x) contains m^2 = "
                  + (str(inb[0]) if inb else "NONE")
                  + ("; the other crossing (m^2 = "
                     + ", ".join(map(str, oth)) + ") lies outside the "
                     "pinned bracket — delivered" if oth else ""))
            cross_brackets = [bracket_64(x) for x in (xlo, xhi)
                              if x > 0 and bracket_64(x) is not None]
        else:
            kg2_verdict = (f"kappa(m) = N(m^2)/{lcm}, N as printed; "
                           f"discriminant {disc} not a perfect square — "
                           "crossing = quadratic surd (exact radical form); "
                           "root isolation via the direct bisection below")
    else:
        kg2_verdict = "identified polynomial in m^2 of degree " + str(deg)

def direct_bisect_64():
    """Fit-independent: refine every adjacent-grid sign change to width
    <= 1/64 by exact bisection on DIRECTLY computed kappas."""
    out = []
    for i in range(len(MGRID) - 1):
        ka, kb = KTAB[MGRID[i]], KTAB[MGRID[i + 1]]
        if ka is None or kb is None or ka * kb >= 0: continue
        a, b, fa = MGRID[i], MGRID[i + 1], ka
        while b - a > Fr(1, 64):
            mid = (a + b) / 2
            km, _, _, _ = kappa_pipeline(mid)
            fm = recognize(km)
            if fm is None: return None
            if fm == 0: a, b = mid, mid; break
            if fa * fm < 0: b = mid
            else: a, fa = mid, fm
        out.append((a, b))
    return out

if kg2_rec_ok and hit is not None and cross_brackets:
    # fit-independent confirmation: direct sign flip on the derived
    # width-1/64 brackets around each identified root
    for (a, b) in cross_brackets:
        ka, _, _, _ = kappa_pipeline(a)
        kb, _, _, _ = kappa_pipeline(b)
        fa, fb = recognize(ka), recognize(kb)
        flip = fa is not None and fb is not None and fa * fb < 0
        kg2_cross_ok &= flip
        print(f"  direct sign bracket [{a}, {b}] (width 1/64, derived from "
              f"the identified root, evaluated by the PIPELINE not the "
              f"fit): kappa = {fa} -> {fb}  sign flip: {flip}")
    check("KG2-D the identified form verified exactly on the full grid; "
          "every zero crossing confirmed by DIRECT pipeline evaluation on "
          "a derived 1/64-wide rational bracket", kg2_cross_ok, kg2_verdict)
elif kg2_rec_ok:
    # pre-registered non-fit (or non-rational-root) branch: census +
    # exact bisection of every grid sign change to width <= 1/64
    if hit is not None:
        print(f"  IDENTIFIED (form outside the rational-root fast path): "
              f"{hit[0]} {hit[1]}")
    brs = direct_bisect_64()
    ok_nb = brs is not None and len(brs) >= 1 and all(
        b - a <= Fr(1, 64) for a, b in brs)
    check("KG2-D delivered: census printed; every grid sign change refined "
          "to a bracket of width <= 1/64 by exact bisection on computed "
          "kappas", ok_nb,
          "brackets: " + "; ".join(f"({a}, {b})" for a, b in (brs or [])))
    if not kg2_verdict:
        kg2_verdict = ((f"identified form {hit[0]} {hit[1]}; " if hit
                        is not None else "no scanned form fits; ")
                       + "crossings in "
                       + "; ".join(f"({a}, {b})" for a, b in (brs or [])))
else:
    check("KG2-D ansatz scan not run: kappa recognition breakage", False)

# ============================================================================
print("\n[KG3 — the interacting cross-check at ORD 4 (pre-registered open)]")
print("  fixture: the root validator's minimal interacting gauge-matter")
print("  occupation Hamiltonian, 4 sites, open chain, committed point")
print("  (m, g) = (7/10, 1/2), t = 1, lambdas = (9/10, -2/5, 11/10, 1/5);")
print("  basis = the validator's particle_basis order (site 0 = MSB);")
print("  H = sum_n m*(-1)^n n_n - g * sum_n lambda_n * prod_{s<=n}(-1)^{n_s}")
print("      - t * sum_bonds hop  (conventions read from the validator).")
print("  region collar (declared): C_{n0} = the site's mass term + the")
print("  electric term of INDEX n0 (the gauge string through n0) + the")
print("  hopping bonds incident to n0; B = H - C. Pairs (declared):")
print("  d=1: R={1}, S={2}; d=2: R={1}, S={3}. STRUCTURED (declared) =")
print("  proportional within every particle-number sector block with")
print("  per-sector constants; DIVERGENT = some sector non-proportional.")
NS_INT = 4
basis_int = [tuple((st >> sh) & 1 for sh in range(NS_INT - 1, -1, -1))
             for st in range(2 ** NS_INT)]
index_int = {st: i for i, st in enumerate(basis_int)}
BONDS_INT = [(0, 1), (1, 2), (2, 3)]
T_INT = mpf(1)
M_INT = mpf(7) / 10
G_INT = mpf(1) / 2
LAMB_INT = [mpf(9) / 10, -mpf(2) / 5, mpf(11) / 10, mpf(1) / 5]

def build_H_int(site_w, bond_w):
    Hm = {}
    for i, st in enumerate(basis_int):
        dv = mpf(0)
        prefix = 1
        for site, occ in enumerate(st):
            prefix *= -1 if occ else 1
            dv += site_w[site] * (M_INT * ((-1) ** site) * occ
                                  - G_INT * LAMB_INT[site] * prefix)
        if dv != 0: Hm[(i, i)] = mpc(dv)
        for bi, (lft, rgt) in enumerate(BONDS_INT):
            if bond_w[bi] == 0: continue
            if st[lft] == st[rgt]: continue
            mv = list(st)
            mv[lft], mv[rgt] = mv[rgt], mv[lft]
            key = (index_int[tuple(mv)], i)
            Hm[key] = Hm.get(key, mpc(0)) - T_INT * bond_w[bi]
    return {k: v for k, v in Hm.items() if v != 0}

set_phase(4, dim_=16)
H_int = build_H_int([1] * 4, [1] * 3)
herm = max(fabs(H_int.get((i, j), mpc(0))
                - H_int.get((j, i), mpc(0)).conjugate())
           for i in range(16) for j in range(16))
check("KG3-A the interacting H is Hermitian (real symmetric) as built",
      herm < TOL, f"max dev {nstr(herm, 3)}")
Gfi_int = m_neumann_inv(gamma_series(exp_series(H_int)))
NPART = [sum(st) for st in basis_int]

def A_int(n0, rule):
    site_w = [0 if n == n0 else 1 for n in range(NS_INT)]
    bond_w = [0 if (n0 in BONDS_INT[bi]) else 1 for bi in range(3)]
    B = build_H_int(site_w, bond_w)
    C = {}
    for k in set(H_int) | set(B):
        v = H_int.get(k, mpc(0)) - B.get(k, mpc(0))
        if v != 0: C[k] = v
    if rule == 'EXC':
        J = m_mul(gamma_series(exp_series(B)), Gfi_int)
        sub = mnorm(coeff_matrix(J, 1))
        return coeff_matrix(J, 2), sub
    U = m_mul(exp_series(B), exp_series(C))
    J = m_mul(gamma_series(U), Gfi_int)
    sub = max(mnorm(coeff_matrix(J, p)) for p in (1, 2, 3))
    return coeff_matrix(J, 4), sub

def classify_int(Ce, Cl):
    ne, nl = mnorm(Ce), mnorm(Cl)
    if ne < TOL and nl < TOL: return "BOTH-ZERO", None
    if ne < TOL: return "SUPPORT-MISMATCH(EXC-zero)", None
    if nl < TOL: return "SUPPORT-MISMATCH(LT-zero)", None
    bi = max(sorted(Ce), key=lambda k: fabs(Ce[k]))
    kap = Cl.get(bi, mpc(0)) / Ce[bi]
    dev = mnorm({k: Cl.get(k, mpc(0)) - kap * Ce.get(k, mpc(0))
                 for k in set(Ce) | set(Cl)}) / nl
    if dev < TOL: return "PROPORTIONAL", ('all', kap, dev)
    secs = {}
    okall = True
    for N in range(NS_INT + 1):
        keys = [k for k in set(Ce) | set(Cl)
                if NPART[k[0]] == N and NPART[k[1]] == N]
        Se = {k: Ce[k] for k in keys if k in Ce}
        Sl = {k: Cl[k] for k in keys if k in Cl}
        nse, nsl = mnorm(Se), mnorm(Sl)
        if nse < TOL and nsl < TOL: continue
        if nse < TOL or nsl < TOL:
            secs[N] = "sector-support-mismatch"; okall = False; continue
        bs = max(sorted(Se), key=lambda k: fabs(Se[k]))
        ks = Sl.get(bs, mpc(0)) / Se[bs]
        sdev = mnorm({k: Sl.get(k, mpc(0)) - ks * Se.get(k, mpc(0))
                      for k in keys}) / nsl
        secs[N] = (ks, sdev)
        if sdev >= TOL: okall = False
    if okall and secs: return "STRUCTURED", secs
    return "DIVERGENT", secs

kg3_sub_ok = True
kg3_block_ok = True
kg3_verdicts = []
for (r0, s0, dlab) in ((1, 2, 1), (1, 3, 2)):
    Ae_R, se1 = A_int(r0, 'EXC')
    Ae_S, se2 = A_int(s0, 'EXC')
    Al_R, sl1 = A_int(r0, 'LT')
    Al_S, sl2 = A_int(s0, 'LT')
    kg3_sub_ok &= max(se1, se2, sl1, sl2) < TOL
    offb = max([fabs(v) for AA in (Ae_R, Ae_S, Al_R, Al_S)
                for (i, j), v in AA.items() if NPART[i] != NPART[j]],
               default=mpf(0))
    kg3_block_ok &= offb < TOL
    Ce = comm_num(Ae_R, Ae_S)
    Cl = comm_num(Al_R, Al_S)
    ver, det = classify_int(Ce, Cl)
    kg3_verdicts.append((dlab, ver))
    print(f"  d={dlab} (R={{{r0}}}, S={{{s0}}}): {ver}   "
          f"|C^exc| = {nstr(mnorm(Ce), 8)}, |C^LT| = {nstr(mnorm(Cl), 8)}, "
          f"off-N-block max = {nstr(offb, 3)}")
    if isinstance(det, dict):
        for N, v in sorted(det.items()):
            if isinstance(v, tuple):
                print(f"    sector N={N}: ref kappa = "
                      f"{nstr(v[0].real, 25)}, rel dev = {nstr(v[1], 6)}")
            else:
                print(f"    sector N={N}: {v}")
    elif isinstance(det, tuple):
        print(f"    kappa = {nstr(det[1].real, 30)}, rel dev = "
              f"{nstr(det[2], 3)}")
check("KG3-B extraction validity: sub-onset J orders vanish (EXC order 1; "
      "LT orders 1-3) and all four leading coefficients are exactly "
      "N-block-diagonal", kg3_sub_ok and kg3_block_ok, "at 1e-30")
check("KG3-C the pre-registered verdict delivered at both cells "
      "(any of PROPORTIONAL/STRUCTURED/DIVERGENT/SUPPORT-MISMATCH/"
      "BOTH-ZERO is a delivered outcome)", len(kg3_verdicts) == 2,
      "; ".join(f"d={d}: {v}" for d, v in kg3_verdicts))

# ============================================================================
print("\n[SG4 — precision honesty]")
print(f"  mp.dps = {mp.dps}; gate threshold 1e-30; commutator dust drop "
      f"1e-45 (d43a-ported); truncation gate 1e-40.")
print(f"  recognition census over ALL recognized rationals (KG1 constants "
      f"+ KG2 kappas + sign brackets): max residual = "
      f"{nstr(REC_MAXERR[0], 3)}, max denominator = {REC_MAXDEN[0]} "
      f"(cap {DEN_CAP}).")
print("  float entry points: as enumerated in the banner (dps-50 series "
      "arithmetic; recognition layer; KG3 decimal fixture constants). The "
      "ansatz solve/verify layer is EXACT Fraction arithmetic end-to-end.")

print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("[VERDICT] FAIL — anchor/extraction breakage; exit 1")
    sys.exit(1)
print("[KG1 VERDICT] the log-smeared finite-slab theorem at fixture scale: "
      + kg1_v1 + ". Block arm: " + kg1_v2 + ".")
sign_note = ""
if cross_brackets:
    sign_note = (" On the grid hull [1/16, 2]: kappa > 0 below the first "
                 "crossing, kappa < 0 between the crossings, kappa > 0 "
                 "above the second — the d43a sign flip (13/2304 at m=1/2 "
                 "vs -1/72 at m=1) is the two-crossing structure of an "
                 "exact quartic. No claim outside the hull.")
print("[KG2 VERDICT] " + kg2_verdict + "." + sign_note)
kg3_arrive = all(v == "PROPORTIONAL" for _, v in kg3_verdicts)
print("[KG3 VERDICT] " + "; ".join(f"d={d}: {v}" for d, v in kg3_verdicts)
      + " — at the raw singleton-bracket grain the free-core bracket-ray "
      "universality " + ("ARRIVES at" if kg3_arrive else "does NOT arrive "
      "at") + " the interacting fixture (pre-registered open; the smeared "
      "interacting identification remains the declared successor, not "
      "attempted here).")
kg1_short = ("GREEN on every wrap-clean cell in BOTH slab readings"
             if (comp_green and blk_lt_ok and blk_exc_law)
             else "delivered with deviations as printed")
print("[VERDICT] d44d delivered: SG0 anchors re-run green; KG1 slab-width "
      "independence " + kg1_short + " (with the block-arm EXC "
      "((w+1)/2)^2 normalization law and the 8 declared L=12 LT wrap "
      "cells as recorded findings); KG2 " + kg2_verdict + "; KG3 "
      + ", ".join(f"d={d}: {v}" for d, v in kg3_verdicts) + ".")

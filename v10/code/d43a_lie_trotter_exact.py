#!/usr/bin/env python3
"""
d43a_lie_trotter_exact.py — v10 D43a (N1): the Lie-Trotter
rule-independence test. Pin: note-d43a (8c2a191). SERIES REVISION:
the first build extracted coefficients by even-power FITS whose
truncation floor (~1e-13) broke the 1e-40 anchors; this revision
computes E(Delta) as an EXACT truncated power series (order 12) —
matrix exponentials as polynomial matrices, Gamma entrywise
|series|^2, inverses by Neumann series (no constant-free tails) —
so every coefficient is exact to working precision. mp.dps = 50;
threshold 1e-30. Exit 1 ONLY on anchor/extraction breakage; the T2
verdict is pre-registered (delivered, not judged).

Conventions verbatim (v1 p1 / v2 p1 / the root validator): L = 12
periodic, 2-component spinors, alpha = sigma_x, beta = sigma_z,
a = 1; H_D = sum m*beta_n + sum k_{n+1/2}; C_{n0} = m*beta_{n0} +
k_{n0-1/2} + k_{n0+1/2}; B = H - C. Gamma(U) = |U|^2 entrywise;
J = Gamma(U_loc)*Gamma(U_free)^-1; E = J_R J_S J_R^-1 J_S^-1.
EXC: U = exp(-i D B). LT: U = exp(-i D B) exp(-i D C).
lambda family: U = exp(-i D (H - lam C)), c_lam = lam(2-lam).
"""
import sys
from mpmath import mp, mpf, mpc, fabs, chop

mp.dps = 50
TOL = mpf(10) ** (-30)
ORD = 12          # series order in Delta
L = 12
DIM = 2 * L
SX = [[0, 1], [1, 0]]

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def idx(n, s): return 2 * (n % L) + s

# ---- series scalars: lists of mpc, length ORD+1 ----------------------------
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

# ---- series matrices: dict {(i,j): series}, absent = zero ------------------
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
def m_scale_series(A, s):
    return {k: s_mul(v, s) for k, v in A.items()}
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

print("[d43a — the Lie-Trotter rule-independence test (SERIES)]")
print("  banner: exact order-12 series arithmetic (no fits; the")
print("  first build's fit floor broke the anchors — replaced);")
print("  mp.dps = 50; threshold 1e-30; L = 12. The T2 verdict is")
print("  PRE-REGISTERED; exit 1 only on anchor/extraction breakage.")

m_a = mpf(1) / 2
n0 = 3
H_full = build_H(m_a)
Gfree_inv = m_neumann_inv(gamma_series(exp_series(H_full)))

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

# ---- the rule cells ---------------------------------------------------------
def strip_split(D, base, d):
    Rside = {(base - 1) % L, base % L, (base + 1) % L}
    Sside = {(base + d - 1) % L, (base + d) % L, (base + d + 1) % L}
    strip, inter = {}, {}
    for (i, j), v in D.items():
        si, sj = i // 2, j // 2
        if (si in Rside and sj in Sside) or (si in Sside and sj in Rside):
            strip[(i, j)] = v
        else:
            inter[(i, j)] = v
    return strip, inter

verdicts = []
ok3 = True
base = 3
for m in (mpf(1) / 2, mpf(1)):
    Hm = build_H(m)
    Gfi = m_neumann_inv(gamma_series(exp_series(Hm)))
    for d in (2, 3):
        p_exc, p_lt = 2 * d, 2 * max(4, d)
        CRl, CSl = (mpf(1), base), (mpf(1), base + d)
        JR_e = J_series(build_H(m, lam=mpf(1), n0=base), Gfi)
        JS_e = J_series(build_H(m, lam=mpf(1), n0=base + d), Gfi)
        Ee = E_series(JR_e, JS_e)
        # LT: U = exp(-iD B) * exp(-iD C); C as its own numeric matrix
        def lt_J(nn):
            B = build_H(m, lam=mpf(1), n0=nn)
            C = {}
            full = build_H(m)
            for k in set(full) | set(B):
                v = full.get(k, mpc(0)) - B.get(k, mpc(0))
                if v != 0: C[k] = v
            U = m_mul(exp_series(B), exp_series(C))
            return m_mul(gamma_series(U), Gfi)
        El = E_series(lt_J(base), lt_J(base + d))
        for p in (4, 6):
            if p < p_lt:
                ok3 &= mnorm(coeff_matrix(El, p)) < TOL
        Be = coeff_matrix(Ee, p_exc)
        Bl = coeff_matrix(El, p_lt)
        ne, nl = mnorm(Be), mnorm(Bl)
        if ne < TOL or nl < TOL:
            verdicts.append((float(m), d, "EXTRACTION-EMPTY", None, None))
            continue
        bi = max(Be, key=lambda k: fabs(Be[k]))
        kappa = Bl.get(bi, mpc(0)) / Be[bi]
        dev = mnorm({k: Bl.get(k, mpc(0)) - kappa * Be.get(k, mpc(0))
                     for k in set(Be) | set(Bl)}) / nl
        if dev < TOL:
            verdicts.append((float(m), d, "PROPORTIONAL", kappa, None))
            continue
        Se, _ = strip_split(Be, base, d)
        Sl, _ = strip_split(Bl, base, d)
        sver = None
        if Se and Sl:
            bs = max(Se, key=lambda k: fabs(Se[k]))
            ks = Sl.get(bs, mpc(0)) / Se[bs]
            sdev = mnorm({k: Sl.get(k, mpc(0)) - ks * Se.get(k, mpc(0))
                          for k in set(Se) | set(Sl)}) / mnorm(Sl)
            if sdev < TOL:
                verdicts.append((float(m), d, "STRUCTURED", ks, None))
                continue
            sver = sdev
        verdicts.append((float(m), d, "DIVERGENT", kappa, sver))
check("AN3 the LT onset law: orders 4 and 6 vanish exactly for all "
      "(m, d) (E^LT - I = O(Delta^8), the committed law)",
      ok3, "sub-onset coefficients zero at 1e-30")

# ---- T4 (pin §6): the pure BRACKET comparison ------------------------------
t4 = []
for m in (mpf(1) / 2, mpf(1)):
    Hm = build_H(m)
    Gfi = m_neumann_inv(gamma_series(exp_series(Hm)))
    def A_of(nn, rule):
        if rule == 'EXC':
            J = J_series(build_H(m, lam=mpf(1), n0=nn), Gfi)
            return coeff_matrix(J, 2)
        B = build_H(m, lam=mpf(1), n0=nn)
        C = {}
        full = build_H(m)
        for k in set(full) | set(B):
            v = full.get(k, mpc(0)) - B.get(k, mpc(0))
            if v != 0: C[k] = v
        U = m_mul(exp_series(B), exp_series(C))
        J = m_mul(gamma_series(U), Gfi)
        return coeff_matrix(J, 4)
    for d in (1, 2, 3):
        Ce = {}
        Ae_R, Ae_S = A_of(base, 'EXC'), A_of(base + d, 'EXC')
        Al_R, Al_S = A_of(base, 'LT'), A_of(base + d, 'LT')
        def comm(X, Y):
            XY = {}
            for (i, k), a in X.items():
                for (kk, j), b in Y.items():
                    if k != kk: continue
                    XY[(i, j)] = XY.get((i, j), mpc(0)) + a * b
            YX = {}
            for (i, k), a in Y.items():
                for (kk, j), b in X.items():
                    if k != kk: continue
                    YX[(i, j)] = YX.get((i, j), mpc(0)) + a * b
            out = {}
            for k in set(XY) | set(YX):
                v = XY.get(k, mpc(0)) - YX.get(k, mpc(0))
                if fabs(v) > mpf(10) ** (-45): out[k] = v
            return out
        Ce = comm(Ae_R, Ae_S)
        Cl = comm(Al_R, Al_S)
        ne, nl = mnorm(Ce), mnorm(Cl)
        if ne < TOL and nl < TOL:
            t4.append((float(m), d, "BOTH-ZERO", None)); continue
        if ne < TOL or nl < TOL:
            # the strongest divergence mode: one rule's bracket
            # vanishes where the other's does not (support-width
            # mismatch between onset classes) — a delivered verdict
            t4.append((float(m), d,
                       "SUPPORT-MISMATCH(EXC-zero)" if ne < TOL
                       else "SUPPORT-MISMATCH(LT-zero)", None))
            continue
        bi = max(Ce, key=lambda k: fabs(Ce[k]))
        kap = Cl.get(bi, mpc(0)) / Ce[bi]
        dev = mnorm({k: Cl.get(k, mpc(0)) - kap * Ce.get(k, mpc(0))
                     for k in set(Ce) | set(Cl)}) / nl
        t4.append((float(m), d,
                   "PROPORTIONAL" if dev < TOL else "DIVERGENT", kap))
t4str = "; ".join(f"(m={v[0]}, d={v[1]}): {v[2]}"
                  + (f", kappa = {chop(v[3])}" if v[3] is not None else "")
                  for v in t4)
check("T4 THE BRACKET-LEVEL TEST (pin §6 — the orphan's actual "
      "question): [A^LT_R, A^LT_S] vs [A^exc_R, A^exc_S] per (m, d); "
      "every outcome incl. SUPPORT-MISMATCH is a delivered verdict",
      len(t4) == 6, t4str)

extraction_ok = all(v[2] != "EXTRACTION-EMPTY" for v in verdicts)
vstr = "; ".join(
    f"(m={v[0]}, d={v[1]}): {v[2]}"
    + (f", kappa = {chop(v[3])}" if v[3] is not None else "")
    + (f", strip-dev = {chop(v[4])}" if v[4] is not None else "")
    for v in verdicts)
check("T1/T2 the pre-registered verdict delivered exactly at every "
      "(m, d) cell", extraction_ok and len(verdicts) == 4, vstr)

print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("[VERDICT] FAIL — anchor/extraction breakage; exit 1")
    sys.exit(1)
uniq = sorted({v[2] for v in verdicts})
uniq4 = sorted({v[2] for v in t4})
print(f"[VERDICT] d43a delivered: T2 (raw defect) = {uniq}; "
      f"T4 (pure bracket) = {uniq4} — T4 decides the orphan "
      "interpretation per pin §4 (PROPORTIONAL = rule-independence "
      "certificate; STRUCTURED = the p8-class refinement; DIVERGENT "
      "= the foundation alarm, quantified by the printed kappa and "
      "strip deviations).")

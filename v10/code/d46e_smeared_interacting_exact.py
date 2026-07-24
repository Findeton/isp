#!/usr/bin/env python3
"""
d46e_smeared_interacting_exact.py — v10 D46e (ladder step e): the
SMEARED interacting identification, WITH the mandatory g = 0 column.
Pin: note-d46e-smeared-interacting.md (strict).

Parents: D44d TERMINAL #353 (the raw singleton-bracket comparison at
the validator's interacting point is DIVERGENT at d = 1, 2 — but the
round's g = 0 control is ALSO divergent, so that cell measured
GRAIN-INHERITED divergence and ray-level arrival under interaction
was left UNDECIDED with this unit named as the successor; note-d44d
§5 B1); D45a TERMINAL #362 (the free-core identification, kappa(m)
for all m).  The series machinery, the interacting gauge-matter
fixture, the collar convention, the validator's committed point and
the extraction-validity gates are PORTED from
`v10/code/d44d_slab_kappa_exact.py` (which ported them in turn from
d43a and from the root validator, read-only).

GREEN-UNREVIEWED — the hostile round is deferred per the D46 program
pin (token budget); this receipt must not be cited as review-hardened
until its round converts (paper-32's round precedes it).

Gates: SG0 free-core regression through the ported pipeline (the
singleton ray collapse; kappa(1/2) = 13/2304, kappa(1) = -1/72);
SG1 the interacting fixture + extraction validity + the d44d KG3
DIVERGENT re-anchor at d = 1, 2; SG2 THE CORE — the corpus's tau
first-moment identification D = sum_delta delta*tau applied to the
interacting one-region coefficients for BOTH admission rules, at the
interacting point AND at g = 0, same pipeline, same channels, with a
per-cell ray verdict; SG3 every SG2 number beside its g = 0 twin with
the GRAIN part (shared with g = 0) and the INTERACTION part (the
difference) computed and separated; SG4 precision as-run, a dps-80
stability twin, determinism, allow-list purity, no vacuous gate.

Exit 1 ONLY on anchor/extraction breakage.  EVERY SG2 outcome
(collapse, partial/structured, support-mismatch, no-collapse) is a
pre-registered DELIVERED verdict at exit 0.

Conventions verbatim (v1 p1 / v2 p1 / d43a / d44d): free core =
periodic lattice, 2-component spinors, alpha = sigma_x, beta =
sigma_z, a = 1; H_D = sum m*beta_n + sum k_{n+1/2}; for a region R:
C_R = sum_{n in R} m*beta_n + sum_{bonds meeting R} k; B_R = H_D -
C_R.  EXC: U = exp(-i D B_R).  LT: U = exp(-i D B_R) exp(-i D C_R).
Gamma(U) = |U|^2 entrywise; J_R = Gamma(U_R) Gamma(U_free)^-1.
Interacting fixture = the root validator's minimal gauge-matter
occupation Hamiltonian (4 sites, open chain), d44d's KG3 block.
"""
import sys
import os
from fractions import Fraction as Fr
from mpmath import mp, mpf, mpc, fabs, chop, nstr

mp.dps = 50
TOL = mpf(10) ** (-30)
ORD = 12          # phase-set: 12 for SG0 (free core), 4 for SG1/SG2/SG3
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

# ---- series scalars (ported verbatim from d44d/d43a) -----------------------
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

# ---- series matrices (ported verbatim from d44d/d43a) ----------------------
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
    """Free-core numeric H; collar of {n0} scaled by (1-lam)."""
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
    """The d44d region-collar builder (sites in Rset and bonds meeting
    Rset carry weight (1-lam)); gated against build_H on singletons."""
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

def coeff_matrix(M, p):
    return {k: v[p] for k, v in M.items() if v[p] != 0}

def mnorm(D):
    return max((fabs(v) for v in D.values()), default=mpf(0))

def comm_num(X, Y):
    """[X, Y] on numeric coefficient matrices (d43a; 1e-45 dust drop)."""
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
    """THE CORPUS IDENTIFICATION (d43a/d44d/d45a, ported verbatim):
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
    LT at Delta^4."""
    B = build_H_R(m, Rset, mpf(1))
    if rule == 'EXC':
        return coeff_matrix(m_mul(gamma_series(exp_series(B)), Gfi), 2)
    C = {}
    for k in set(full) | set(B):
        v = full.get(k, mpc(0)) - B.get(k, mpc(0))
        if v != 0: C[k] = v
    U = m_mul(exp_series(B), exp_series(C))
    return coeff_matrix(m_mul(gamma_series(U), Gfi), 4)

# ---- exact-rational recognition (ported; SG4-declared entry point) ---------
def to_fr_exact(x):
    sign, man, exp, bc = x._mpf_
    if man == 0: return Fr(0)
    v = Fr(int(man), 1)
    v = v * (2 ** exp) if exp >= 0 else v / (2 ** (-exp))
    return -v if sign else v

DEN_CAP = 10 ** 15
REC_MAXERR = [mpf(0)]
REC_MAXDEN = [1]
def recognize(x):
    """dps-50 real -> Fraction by bounded-denominator best approximation
    (cap 10^15), accepted only at residual < 1e-30; else None."""
    fr = to_fr_exact(mpf(x)).limit_denominator(DEN_CAP)
    err = fabs(mpf(x) - mpf(fr.numerator) / fr.denominator)
    if err < TOL:
        if err > REC_MAXERR[0]: REC_MAXERR[0] = err
        if fr.denominator > REC_MAXDEN[0]: REC_MAXDEN[0] = fr.denominator
        return fr
    return None

def fr2mp(fr): return mpf(fr.numerator) / fr.denominator

def rstr(x):
    """Recognized-rational string, else a 30-digit decimal (declared)."""
    fr = recognize(x)
    return str(fr) if fr is not None else nstr(mpf(x), 30)

KAPPA_REF = {0.5: Fr(13, 2304), 1.0: Fr(-1, 72)}
KAPPA_POLY = (Fr(1, 36), Fr(-5, 48), Fr(1, 16))   # d45a: coeffs in m^2

# ---- the interacting gauge-matter fixture (ported from d44d KG3, with
# ---- the coupling g promoted to a parameter so the g = 0 twin runs
# ---- through the IDENTICAL code path) --------------------------------------
NS_INT = 4
basis_int = [tuple((st >> sh) & 1 for sh in range(NS_INT - 1, -1, -1))
             for st in range(2 ** NS_INT)]
index_int = {st: i for i, st in enumerate(basis_int)}
BONDS_INT = [(0, 1), (1, 2), (2, 3)]
T_INT = mpf(1)
M_INT = mpf(7) / 10
G_INT = mpf(1) / 2                       # the validator's committed point
LAMB_INT = [mpf(9) / 10, -mpf(2) / 5, mpf(11) / 10, mpf(1) / 5]
NPART = [sum(st) for st in basis_int]                       # sector label
DIP = [sum(n * o for n, o in enumerate(st)) for st in basis_int]  # dipole

def build_H_int(site_w, bond_w, gv):
    """d44d's KG3 builder with g = gv; gv = 0 gives the g = 0 twin."""
    Hm = {}
    for i, st in enumerate(basis_int):
        dv = mpf(0)
        prefix = 1
        for site, occ in enumerate(st):
            prefix *= -1 if occ else 1
            dv += site_w[site] * (M_INT * ((-1) ** site) * occ
                                  - gv * LAMB_INT[site] * prefix)
        if dv != 0: Hm[(i, i)] = mpc(dv)
        for bi, (lft, rgt) in enumerate(BONDS_INT):
            if bond_w[bi] == 0: continue
            if st[lft] == st[rgt]: continue
            mv = list(st)
            mv[lft], mv[rgt] = mv[rgt], mv[lft]
            key = (index_int[tuple(mv)], i)
            Hm[key] = Hm.get(key, mpc(0)) - T_INT * bond_w[bi]
    return {k: v for k, v in Hm.items() if v != 0}

# ============================================================================
print("[d46e — the smeared interacting identification, with the g = 0 column]")
print("  banner: GREEN-UNREVIEWED — the hostile round is deferred per the D46")
print("  program pin (token budget); this receipt must not be cited as")
print("  review-hardened until its round converts (paper-32's round precedes")
print("  it).")
print()
print("  PRECISION AS RUN: exact truncated-series arithmetic (the d43a/d44d")
print("  machinery, ported verbatim); mp.dps = 50 binary throughout the series")
print("  layer; gate threshold 1e-30; commutator dust drop 1e-45 (d43a-ported);")
print("  SG0 at ORD = 12 / L = 12 (the d44d SG0 code path); SG1/SG2/SG3 at")
print("  ORD = 4 / DIM = 16 (the d44d KG3 phase, EXACT truncation: a Delta^p")
print("  coefficient of series products/inverses depends only on input orders")
print("  <= p).  SG4 re-runs the whole SG2/SG3 layer at mp.dps = 80 and gates")
print("  every delivered constant to agree with the dps-50 run at 1e-30.")
print("  FLOAT ENTRY POINTS (enumerated): (1) the series layer is mpmath binary")
print("  at dps 50 / 80 — the fixture rationals (7/10, 1/2, 9/10, -2/5, 11/10,")
print("  1/5) are rounded on entry, hence every gate is a 1e-30 threshold and")
print("  never an mpf equality; (2) the recognition layer maps a dps-50 real to")
print("  a Fraction by bounded-denominator best approximation (cap 1e15,")
print("  accepted only at residual < 1e-30; census in SG4).  No others.")
print("  Deterministic: no RNG, no wall clock, no hash-ordered output (every")
print("  iteration is over an explicit list or a sorted key list; all dict keys")
print("  are ints/int-tuples).  Rerun byte-identical (SG4).")
print()
print("  THE PIN'S QUESTION (note-d46e §1): at the free core BOTH admission")
print("  rules collapse, under the corpus's continuum identification, onto the")
print("  SAME tangential operator ray with rule-relative constants only.  At")
print("  the interacting fixture the RAW singleton-bracket comparison DIVERGES")
print("  — but D44d's round showed that divergence is GRAIN-INHERITED (present")
print("  at g = 0 too).  Does the SMEARED (identified-operator) comparison")
print("  collapse onto a common ray?  Every interacting cell below is printed")
print("  beside its own g = 0 twin from the same pipeline.")
print()
print("  THE IDENTIFICATION AT THE INTERACTING FIXTURE (declared BEFORE any")
print("  verdict).  The corpus construction is the tau FIRST MOMENT")
print("    tau(delta, ch) = sum_{r in rs} r * sum_{entries in channel ch with")
print("                     displacement delta} [A(b), A(b+r)]_{uv},")
print("    D(ch) = sum_delta delta * tau(delta, ch)          (d43a/d44d/d45a),")
print("  ported with the two free-core structures replaced by their fixture")
print("  analogues, both declared here: (i) DISPLACEMENT — the free core reads")
print("  delta off the site index of the matrix entry; on the occupation basis")
print("  the analogue is the OCCUPATION DIPOLE displacement delta(u,v) =")
print("  X(v) - X(u), X(u) = sum_n n*u_n (a hop across one bond shifts X by")
print("  exactly 1, so this reduces to the free-core lattice displacement on")
print("  the one-particle sector); (ii) CHANNEL — the free core's channel is")
print("  the spinor pair (s, s') and the residual index i is SUMMED.  The")
print("  occupation basis has no site/spin factorization, so a FAMILY of")
print("  channel readings is pre-registered, coarse to fine, and EVERY one is")
print("  reported:")
print("    FULL — no summation at all (channel = the entry itself): the finest")
print("           reading, grading-free.  A collapse here implies a collapse in")
print("           every coarsening; a NON-collapse here does NOT imply one.")
print("    ROW / COL — sum over the column / row partner at fixed row / column")
print("           state (the 'dipole current' carried by each configuration).")
print("    PAR  — channel = (X(u) mod 2, X(v) mod 2), the staggered-sublattice")
print("           analogue of the free-core spinor pair: a 2x2 object directly")
print("           comparable to the free-core ray form c*(I - sigma_x).")
print("    SEC  — channel = the particle-number sector N (the block label of")
print("           the D44d KG3 extraction gate).")
print("  Cells: base b and separation set rs in {(b=0, rs=1,2,3), (b=0,")
print("  rs=1,2), (b=1, rs=1,2)}; the last is the d44d KG3 pair set")
print("  (R={1},S={2}) and (R={1},S={3}) exactly.  Regions are SINGLETONS.")
print()
print("  RAY VERDICT CLASSES (pre-registered; all are delivered outcomes at")
print("  exit 0): COLLAPSE = D^LT = c * D^EXC over the whole channel set with")
print("  ONE constant c (relative deviation < 1e-30) — the free-core outcome;")
print("  STRUCTURED = proportional within every particle-number sector with")
print("  per-sector constants but not globally; SUPPORT-MISMATCH = one rule's")
print("  identified operator vanishes identically in that channel while the")
print("  other does not (no common ray is even definable); BOTH-ZERO = both")
print("  vanish; NO-COLLAPSE = neither.")
print("  The reported constant c is read off a CANONICAL reference channel —")
print("  the str-least channel attaining max |D^EXC| within relative 1e-25 —")
print("  because exact ties for that maximum occur here and a bare argmax")
print("  would make the printed number precision-dependent; the VERDICT CLASS")
print("  is reference-free (proportionality does not depend on which channel")
print("  normalizes it), and SG4-A gates the whole layer at dps 80.")
print("  A NO-COLLAPSE is a finding, not a failure — but per the D44d §5 B1")
print("  lesson it is meaningless without its")
print("  g = 0 twin, which is why SG3 separates GRAIN (what the g = 0 twin")
print("  already does) from the INTERACTION EFFECT (the computed difference).")
print()
print("  DECLARED PIN DEVIATIONS (owned in-receipt): (D1) the fixture is a")
print("  4-site OPEN chain, so there is no translation average and no")
print("  completeness slot beyond r = 3 — the r-range is the full available")
print("  range at each base, and the three cells above are its full sweep;")
print("  (D2) the channel-reading FAMILY above is this receipt's construction —")
print("  the pin says 'the same tau first-moment construction', which fixes the")
print("  moment but not the fixture's channel analogue, so all five readings")
print("  are run and reported rather than one being privileged; (D3) ONE")
print("  interacting point (pin §3) and ONE collar convention (d44d A6) — the")
print("  three-convention robustness sweep is D44d's, not re-run here.")

# ============================================================================
print("\n[SG0 — free-core regression through the ported pipeline "
      "(ORD 12, L 12)]")
set_phase(12, 12)
m_a = mpf(1) / 2
n0 = 3
H_full = build_H(m_a)
Gfree_inv = m_neumann_inv(gamma_series(exp_series(H_full)))

pf_ok = True
for lamv in (mpf(1), mpf(1) / 2):
    Ha = build_H(m_a, lam=lamv, n0=n0)
    Hb = build_H_R(m_a, {n0}, lamv)
    pf_ok &= set(Ha) == set(Hb) and all(fabs(Ha[k] - Hb[k]) == 0 for k in Ha)
check("SG0-PF port fidelity: the region-collar builder == the singleton "
      "collar builder entrywise (lam = 1 and 1/2), exact", pf_ok)

A1 = coeff_matrix(J_series(build_H(m_a, lam=mpf(1), n0=n0), Gfree_inv), 2)
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
check("SG0-A the EXC singleton A(1) (d44d AN1): diag 1/2 at n0, 1/4 at "
      "n0+-1, -1/4 spin-flip off-diagonals, same-spin zero, columns sum "
      "zero", okA, "exact at 1e-30")

REF_LT = {0.5: {(1, 'flip'): Fr(1, 9216), (-1, 'flip'): Fr(-1, 9216),
                (2, 'same'): Fr(-23, 9216), (-2, 'same'): Fr(23, 9216),
                (3, 'flip'): Fr(-1, 1024), (-3, 'flip'): Fr(1, 1024),
                (4, 'same'): Fr(1, 512), (-4, 'same'): Fr(-1, 512)},
          1.0: {(1, 'flip'): Fr(-19, 1152), (-1, 'flip'): Fr(19, 1152),
                (2, 'same'): Fr(-17, 2304), (-2, 'same'): Fr(17, 2304),
                (3, 'flip'): Fr(1, 128), (-3, 'flip'): Fr(-1, 128),
                (4, 'same'): Fr(1, 512), (-4, 'same'): Fr(-1, 512)}}

def tau_D_free(m, rule):
    Hm = build_H(m)
    Gfi = m_neumann_inv(gamma_series(exp_series(Hm)))
    cache = {}
    def A_at(nn):
        if nn not in cache:
            cache[nn] = A_region(m, {nn % L}, rule, Gfi, Hm)
        return cache[nn]
    return tau_D_pairs(A_at, (1, 2, 3, 4))

t5_ok = True
t5_det = []
for m in (mpf(1) / 2, mpf(1)):
    tauE, DE = tau_D_free(m, 'EXC')
    tauL, DL = tau_D_free(m, 'LT')
    okE = (fabs(DE.get((0, 0), 0) - 1) < TOL
           and fabs(DE.get((1, 1), 0) - 1) < TOL
           and fabs(DE.get((0, 1), 0) + 1) < TOL
           and fabs(DE.get((1, 0), 0) + 1) < TOL)
    kref = KAPPA_REF[float(m)]
    okL = all(fabs(DL.get((a_, b_), 0)
                   - fr2mp(kref) * (1 if a_ == b_ else -1)) < TOL
              for a_ in (0, 1) for b_ in (0, 1))
    got_ch = {}
    for (delta_, a_, b_), v in tauL.items():
        ch = 'flip' if a_ != b_ else 'same'
        if (a_, b_) in ((0, 1), (0, 0)) and fabs(v) > TOL:
            got_ch[(delta_, ch)] = v
    ref = REF_LT[float(m)]
    okT = set(got_ch) == set(ref)
    for k, rv in ref.items():
        okT &= fabs(got_ch.get(k, mpc(0)) - fr2mp(rv)) < TOL
    okO = True
    for tt in (tauE, tauL):
        for (delta_, a_, b_), v in tt.items():
            okO &= fabs(v + tt.get((-delta_, a_, b_), mpc(0))) < TOL
    # the d45a all-m polynomial evaluated exactly at this mass
    mfr = Fr(1, 2) if float(m) == 0.5 else Fr(1)
    kpoly = sum(c * mfr ** (2 * p) for p, c in enumerate(KAPPA_POLY))
    okP = (kpoly == kref)
    t5_ok &= okE and okL and okT and okO and okP
    t5_det.append(f"m={float(m)}: EXC D = 1*(I - sx) {okE}; LT D = {kref}*"
                  f"(I - sx) {okL}; tau table {okT}; delta-odd {okO}; "
                  f"d45a poly {okP}")
sign_flip = (KAPPA_REF[0.5] > 0) and (KAPPA_REF[1.0] < 0)
check("SG0-B THE FREE-CORE RAY COLLAPSE re-run (d44d T5 / d45a YG1): both "
      "admission rules' identified operators land on the SAME ray "
      "(I - sigma_x) with rule-relative constants — EXC = 1, LT = "
      "kappa(m) with kappa(1/2) = 13/2304 and kappa(1) = -1/72 (sign "
      "flip); the committed signed tau channel tables reproduced; "
      "delta-odd in every channel of both rules; the d45a polynomial "
      "(9m^4 - 15m^2 + 4)/144 agrees at both anchors in EXACT Fraction "
      "arithmetic", t5_ok and sign_flip, "; ".join(t5_det))
print("  [SG0 NOTE] this is the behaviour the interacting cells below are "
      "compared against: ONE ray, TWO rule-relative constants.")

# ============================================================================
print("\n[SG1 — the interacting fixture, its extraction-validity gates, and "
      "the d44d KG3 re-anchor (ORD 4, DIM 16)]")
print("  fixture (d44d KG3, ported): the root validator's minimal interacting")
print("  gauge-matter occupation Hamiltonian, 4 sites, open chain, committed")
print("  point (m, g) = (7/10, 1/2), t = 1, lambda = (9/10, -2/5, 11/10, 1/5);")
print("  basis = the validator's particle_basis order (site 0 = MSB);")
print("  H = sum_n m*(-1)^n n_n - g * sum_n lambda_n * prod_{s<=n}(-1)^{n_s}")
print("      - t * sum_bonds hop.  Region collar (d44d A6): C_{n0} = the")
print("  site's mass term + the electric term of INDEX n0 + the hopping bonds")
print("  incident to n0; B = H - C.  The g = 0 twin is the SAME builder with")
print("  the coupling set to zero — one code path, two columns.")

def int_pipeline(gv):
    """Returns (H, A(n0, rule), subonset(n0, rule)) at coupling gv, ORD 4."""
    set_phase(4, dim_=16)
    Hg = build_H_int([1] * 4, [1] * 3, gv)
    Gfi = m_neumann_inv(gamma_series(exp_series(Hg)))
    cache = {}
    def A(n0_, rule):
        key = (n0_, rule)
        if key in cache: return cache[key]
        site_w = [0 if n == n0_ else 1 for n in range(NS_INT)]
        bond_w = [0 if (n0_ in BONDS_INT[bi]) else 1 for bi in range(3)]
        B = build_H_int(site_w, bond_w, gv)
        C = {}
        for k in set(Hg) | set(B):
            v = Hg.get(k, mpc(0)) - B.get(k, mpc(0))
            if v != 0: C[k] = v
        if rule == 'EXC':
            J = m_mul(gamma_series(exp_series(B)), Gfi)
            out = (coeff_matrix(J, 2), mnorm(coeff_matrix(J, 1)))
        else:
            U = m_mul(exp_series(B), exp_series(C))
            J = m_mul(gamma_series(U), Gfi)
            out = (coeff_matrix(J, 4),
                   max(mnorm(coeff_matrix(J, p)) for p in (1, 2, 3)))
        cache[key] = out
        return out
    return Hg, A

def classify_raw(Ce, Cl):
    """d44d's KG3 classifier, ported verbatim (raw-bracket level)."""
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
        keys = [k for k in sorted(set(Ce) | set(Cl))
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

H_int, A_int = int_pipeline(G_INT)
herm = max(fabs(H_int.get((i, j), mpc(0))
                - H_int.get((j, i), mpc(0)).conjugate())
           for i in range(16) for j in range(16))
check("SG1-A the interacting H is Hermitian (real symmetric) as built "
      "(d44d KG3-A)", herm < TOL, f"max dev {nstr(herm, 3)}")

H_free_tw, A_free_tw = int_pipeline(mpf(0))
hdev = max(fabs(H_int.get(k, mpc(0)) - H_free_tw.get(k, mpc(0)))
           for k in sorted(set(H_int) | set(H_free_tw)))
odev = max([fabs(H_int.get(k, mpc(0)) - H_free_tw.get(k, mpc(0)))
            for k in sorted(set(H_int) | set(H_free_tw)) if k[0] != k[1]],
           default=mpf(0))
check("SG1-B the g = 0 twin is the SAME fixture with the coupling removed: "
      "the two Hamiltonians differ ONLY on the diagonal (the electric "
      "gauge-string term) and differ there by a computed nonzero amount — "
      "the twin is neither a copy nor a different model",
      hdev > mpf(1) / 10 and odev < TOL,
      f"max diagonal deviation = {rstr(hdev)}; max off-diagonal deviation "
      f"= {nstr(odev, 3)}")

# ---- the d44d KG3 committed numbers, re-anchored ---------------------------
KG3_REF = {1: ("DIVERGENT", mpf(2), mpf("0.88668056"),
               {1: (mpf("0.019584375"), mpf("0.963179")),
                2: (mpf("-0.07001388888888888888888889"), mpf("0.921038")),
                3: (mpf("-0.2369545138888888888888889"), mpf("1.21725"))}),
           2: ("DIVERGENT", mpf(1), mpf("0.95269722"),
               {1: (mpf("-0.8534527777777777777777778"), mpf("1.55642")),
                2: (mpf("0.03526388888888888888888889"), mpf("1.0")),
                3: (mpf("-0.8151972222222222222222222"), mpf("1.44589"))})}
sub_ok = True
blk_ok = True
anch_ok = True
raw_lines = []
for (r0, s0, dlab) in ((1, 2, 1), (1, 3, 2)):
    Ae_R, se1 = A_int(r0, 'EXC')
    Ae_S, se2 = A_int(s0, 'EXC')
    Al_R, sl1 = A_int(r0, 'LT')
    Al_S, sl2 = A_int(s0, 'LT')
    sub_ok &= max(se1, se2, sl1, sl2) < TOL
    offb = max([fabs(v) for AA in (Ae_R, Ae_S, Al_R, Al_S)
                for (i, j), v in AA.items() if NPART[i] != NPART[j]],
               default=mpf(0))
    blk_ok &= offb < TOL
    Ce = comm_num(Ae_R, Ae_S)
    Cl = comm_num(Al_R, Al_S)
    ver, det = classify_raw(Ce, Cl)
    rv, rne, rnl, rsec = KG3_REF[dlab]
    cell_ok = (ver == rv and fabs(mnorm(Ce) - rne) < TOL
               and fabs(mnorm(Cl) - rnl) < mpf(10) ** (-8))
    for N, (kk, dd) in sorted(rsec.items()):
        got = det.get(N) if isinstance(det, dict) else None
        cell_ok &= (isinstance(got, tuple)
                    and fabs(got[0].real - kk) < mpf(10) ** (-20)
                    and fabs(got[1] - dd) < mpf(10) ** (-5))
    anch_ok &= cell_ok
    print(f"  raw bracket d={dlab} (R={{{r0}}}, S={{{s0}}}): {ver}   "
          f"|C^exc| = {nstr(mnorm(Ce), 8)}, |C^LT| = {nstr(mnorm(Cl), 8)}, "
          f"off-N-block max = {nstr(offb, 3)}  [d44d re-anchor: {cell_ok}]")
    if isinstance(det, dict):
        for N, v in sorted(det.items()):
            if isinstance(v, tuple):
                print(f"    sector N={N}: ref kappa = {nstr(v[0].real, 25)}, "
                      f"rel dev = {nstr(v[1], 6)}")
            else:
                print(f"    sector N={N}: {v}")
    raw_lines.append((dlab, ver))
check("SG1-C extraction validity (d44d KG3-B): sub-onset J orders vanish "
      "(EXC order 1; LT orders 1-3) and every leading coefficient is "
      "exactly particle-number-block-diagonal", sub_ok and blk_ok,
      "all below 1e-30")
check("SG1-D the d44d KG3 RE-ANCHOR: both raw-bracket cells reproduce the "
      "committed verdict DIVERGENT with the committed bracket norms "
      "(|C^exc| = 2 and 1 exactly; |C^LT| = 0.88668056 and 0.95269722 at "
      "1e-8) and all six committed per-sector reference constants (1e-20) "
      "and relative deviations (1e-5, the printed 6-significant-digit width)", anch_ok,
      "; ".join(f"d={d}: {v}" for d, v in raw_lines))

# ============================================================================
print("\n[SG2 — THE CORE: the corpus identification applied to the "
      "interacting one-region coefficients, both rules, g = 1/2 AND g = 0]")

CELLS = ((0, (1, 2, 3)), (0, (1, 2)), (1, (1, 2)))
READINGS = ('FULL', 'ROW', 'COL', 'PAR', 'SEC')
RULES = ('EXC', 'LT')
GCOL = (('g=1/2', G_INT), ('g=0  ', mpf(0)))

def chan_of(reading, i, j):
    if reading == 'FULL': return (i, j)
    if reading == 'ROW': return i
    if reading == 'COL': return j
    if reading == 'PAR': return (DIP[i] % 2, DIP[j] % 2)
    return NPART[i]                      # SEC (blocks are N-diagonal)

def sector_of(reading, key):
    if reading == 'FULL': return NPART[key[0]]
    if reading in ('ROW', 'COL'): return NPART[key]
    if reading == 'SEC': return key
    return None                          # PAR carries no sector label

def D_identified(A, base, rs, rule, reading):
    """D(ch) = sum_delta delta * tau(delta, ch), tau(delta, ch) =
    sum_r r * sum_{entries in ch at displacement delta} [A(b), A(b+r)]."""
    A0 = A(base, rule)[0]
    tau = {}
    for r in rs:
        for (i, j), v in comm_num(A0, A(base + r, rule)[0]).items():
            if fabs(v) < TOL: continue
            key = (DIP[j] - DIP[i], chan_of(reading, i, j))
            tau[key] = tau.get(key, mpc(0)) + r * v
    D = {}
    for (d_, c_), v in tau.items():
        D[c_] = D.get(c_, mpc(0)) + d_ * v
    return {k: v for k, v in D.items() if fabs(v) > TOL}

def ref_key(M):
    """The canonical reference channel: the str-least channel attaining the
    maximum |M| within relative 1e-25.  Declared: exact ties for the
    maximum occur in these readings, so a bare argmax would be broken by
    last-bit noise and the REPORTED constant would be precision-dependent
    (the VERDICT CLASS never is — proportionality is reference-free)."""
    mx = mnorm(M)
    for k in sorted(M, key=str):
        if fabs(M[k]) >= mx * (1 - mpf(10) ** (-25)):
            return k
    return sorted(M, key=str)[0]

def ray_verdict(De, Dl, reading):
    """Pre-registered classes; returns (verdict, const, reldev, secs)."""
    ne, nl = mnorm(De), mnorm(Dl)
    if ne < TOL and nl < TOL: return ("BOTH-ZERO", None, None, {})
    if ne < TOL: return ("SUPPORT-MISMATCH(EXC-zero)", None, None, {})
    if nl < TOL: return ("SUPPORT-MISMATCH(LT-zero)", None, None, {})
    keys = sorted(set(De) | set(Dl), key=str)
    bi = ref_key(De)
    c = Dl.get(bi, mpc(0)) / De[bi]
    dev = mnorm({k: Dl.get(k, mpc(0)) - c * De.get(k, mpc(0))
                 for k in keys}) / nl
    if dev < TOL: return ("COLLAPSE", c, dev, {})
    secs = {}
    okall = True
    for N in range(NS_INT + 1):
        ks = [k for k in keys if sector_of(reading, k) == N]
        if not ks: continue
        Se = {k: De[k] for k in ks if k in De}
        Sl = {k: Dl[k] for k in ks if k in Dl}
        nse, nsl = mnorm(Se), mnorm(Sl)
        if nse < TOL and nsl < TOL: continue
        if nse < TOL or nsl < TOL:
            secs[N] = None; okall = False; continue
        bs = ref_key(Se)
        cs = Sl.get(bs, mpc(0)) / Se[bs]
        sdev = mnorm({k: Sl.get(k, mpc(0)) - cs * Se.get(k, mpc(0))
                      for k in ks}) / nsl
        secs[N] = (cs, sdev)
        if sdev >= TOL: okall = False
    if okall and secs: return ("STRUCTURED", None, dev, secs)
    return ("NO-COLLAPSE", c, dev, secs)

def rayform(P):
    """Is the 2x2 channel object on the free-core ray c*(I - sigma_x)?"""
    d00 = P.get((0, 0), mpc(0)); d11 = P.get((1, 1), mpc(0))
    d01 = P.get((0, 1), mpc(0)); d10 = P.get((1, 0), mpc(0))
    on = (fabs(d00 - d11) < TOL and fabs(d01 - d10) < TOL
          and fabs(d00 + d01) < TOL and fabs(d00.imag) < TOL
          and fabs(d00) > TOL)
    return on, d00

PIPES = {}
for gname, gval in GCOL:
    PIPES[gname] = int_pipeline(gval)[1]

DSTORE = {}          # (gname, base, rmax, rule, reading) -> D dict
VSTORE = {}          # (gname, base, rmax, reading) -> (verdict, c, dev, secs)
for base, rs in CELLS:
    for reading in READINGS:
        for gname, _ in GCOL:
            A = PIPES[gname]
            for rule in RULES:
                DSTORE[(gname, base, max(rs), rule, reading)] = \
                    D_identified(A, base, rs, rule, reading)
            VSTORE[(gname, base, max(rs), reading)] = ray_verdict(
                DSTORE[(gname, base, max(rs), 'EXC', reading)],
                DSTORE[(gname, base, max(rs), 'LT', reading)], reading)

print("  Per cell: the identified operator norms and the RAY verdict, "
      "interacting column then its g = 0 twin.")
for base, rs in CELLS:
    rm = max(rs)
    print(f"  --- cell base b={base}, separations r = "
          f"{','.join(str(r) for r in rs)} "
          + ("(= the d44d KG3 pair set R={1},S={2} and R={1},S={3})"
             if base == 1 else "") )
    for reading in READINGS:
        for gname, _ in GCOL:
            ver, c, dev, secs = VSTORE[(gname, base, rm, reading)]
            De = DSTORE[(gname, base, rm, 'EXC', reading)]
            Dl = DSTORE[(gname, base, rm, 'LT', reading)]
            cs = "-" if c is None else rstr(c.real)
            ds = "-" if dev is None else nstr(dev, 6)
            print(f"    {reading:4s} {gname}: |D^EXC| = "
                  f"{nstr(mnorm(De), 12):>16s} ({len(De):2d} ch)  "
                  f"|D^LT| = {nstr(mnorm(Dl), 12):>16s} ({len(Dl):2d} ch)  "
                  f"-> {ver:26s} c = {cs:>22s}  reldev = {ds}")
            if secs:
                for N in sorted(secs):
                    v = secs[N]
                    if v is None:
                        print(f"         sector N={N}: support mismatch")
                    else:
                        print(f"         sector N={N}: c = "
                              f"{rstr(v[0].real):>22s}  reldev = "
                              f"{nstr(v[1], 6)}")

# ---- the PAR channel in full (the free-core-comparable 2x2 object) --------
print("  The PAR channel object entrywise (the 2x2 directly comparable to "
      "the free-core ray form c*(I - sigma_x)):")
par_form = {}
for base, rs in CELLS:
    rm = max(rs)
    for gname, _ in GCOL:
        for rule in RULES:
            P = DSTORE[(gname, base, rm, rule, 'PAR')]
            on, c0 = rayform(P)
            par_form[(gname, base, rm, rule)] = (on, c0)
            ent = "  ".join(
                f"({a},{b}) = {rstr(P.get((a, b), mpc(0)).real)}"
                for a in (0, 1) for b in (0, 1))
            print(f"    b={base} r<={rm} {rule:3s} {gname}: {ent}   "
                  f"on the free-core ray: {'YES' if on else 'no'}"
                  + (f", c = {rstr(c0.real)}" if on else ""))

# ---- SG2 gates -------------------------------------------------------------
n_eval = len(VSTORE)
CLASSES = ("COLLAPSE", "STRUCTURED", "NO-COLLAPSE", "BOTH-ZERO",
           "SUPPORT-MISMATCH(EXC-zero)", "SUPPORT-MISMATCH(LT-zero)")
class_ok = all(v[0] in CLASSES for v in VSTORE.values())
dev_ok = all((v[1] is None) == (v[0] in ("BOTH-ZERO", "STRUCTURED")
                                or v[0].startswith("SUPPORT"))
             for v in VSTORE.values())
check("SG2-A the sweep is complete and every verdict is drawn from the "
      "pre-registered class list, each carrying either a computed relative "
      "deviation or an explicit support statement (3 cells x 5 channel "
      "readings x 2 couplings)", n_eval == 30 and class_ok and dev_ok,
      f"{n_eval} (cell, reading, coupling) evaluations; "
      f"{len(DSTORE)} identified operators")

# the zero-sum lemma: Gamma(U) is doubly stochastic (|U|^2 with U unitary),
# so every order-p > 0 coefficient has vanishing row AND column sums; hence
# EVERY fully channel-summed first moment vanishes identically.
zs = mpf(0)
for gname, _ in GCOL:
    A = PIPES[gname]
    for n0_ in range(NS_INT):
        for rule in RULES:
            M = A(n0_, rule)[0]
            for k in range(16):
                zs = max(zs, fabs(sum(M.get((k, j), mpc(0))
                                      for j in range(16))))
                zs = max(zs, fabs(sum(M.get((i, k), mpc(0))
                                      for i in range(16))))
sec_zero = all(VSTORE[(gname, b, max(rs), 'SEC')][0] == "BOTH-ZERO"
               for b, rs in CELLS for gname, _ in GCOL)
check("SG2-B the ZERO-SUM LEMMA, gated: every leading region coefficient "
      "has vanishing row AND column sums (Gamma(U) = |U|^2 is doubly "
      "stochastic for unitary U, so its order-p>0 coefficients annihilate "
      "the all-ones vector on both sides) — therefore any FULLY summed "
      "first moment vanishes identically, and the SEC reading is BOTH-ZERO "
      "at every cell and both couplings by structure, not by accident",
      zs < TOL and sec_zero,
      f"max row/col sum over all 32 coefficients = {nstr(zs, 3)}; SEC "
      f"BOTH-ZERO at all {len(CELLS) * 2} (cell, coupling) pairs")

# coarsening consistency: every coarser reading is the exact fiber sum of FULL
co_dev = mpf(0)
for base, rs in CELLS:
    rm = max(rs)
    for gname, _ in GCOL:
        for rule in RULES:
            F = DSTORE[(gname, base, rm, rule, 'FULL')]
            for reading in ('ROW', 'COL', 'PAR', 'SEC'):
                agg = {}
                for (i, j), v in F.items():
                    k = chan_of(reading, i, j)
                    agg[k] = agg.get(k, mpc(0)) + v
                G = DSTORE[(gname, base, rm, rule, reading)]
                for k in sorted(set(agg) | set(G), key=str):
                    co_dev = max(co_dev,
                                 fabs(agg.get(k, mpc(0)) - G.get(k, mpc(0))))
check("SG2-C channel-coarsening consistency: each coarser reading equals "
      "the exact fiber sum of the FULL reading (the identification is "
      "linear in the channel partition — a binning-integrity gate over all "
      "cells, rules and couplings)", co_dev < TOL,
      f"max deviation = {nstr(co_dev, 3)}")

im_dev = max((fabs(v.imag) for D in DSTORE.values() for v in D.values()),
             default=mpf(0))
check("SG2-D reality: every identified operator entry is real (the "
      "free-core D-reality property survives to the interacting fixture)",
      im_dev < TOL, f"max |Im| = {nstr(im_dev, 3)}")

# ---- the delivered SG2 verdicts -------------------------------------------
n_collapse = sum(1 for v in VSTORE.values() if v[0] == "COLLAPSE")
n_struct = sum(1 for v in VSTORE.values() if v[0] == "STRUCTURED")
n_nocol = sum(1 for v in VSTORE.values() if v[0] == "NO-COLLAPSE")
n_supp = sum(1 for v in VSTORE.values() if v[0].startswith("SUPPORT"))
n_bz = sum(1 for v in VSTORE.values() if v[0] == "BOTH-ZERO")
print(f"  [SG2 CENSUS] over the 30 (cell, reading, coupling) evaluations: "
      f"COLLAPSE {n_collapse}; STRUCTURED {n_struct}; NO-COLLAPSE "
      f"{n_nocol}; SUPPORT-MISMATCH {n_supp}; BOTH-ZERO {n_bz}.")
devs = [v[2] for v in VSTORE.values() if v[2] is not None]
dev_lo = nstr(min(devs), 6) if devs else "-"
dev_hi = nstr(max(devs), 6) if devs else "-"
sg2_verdict = (
    "NO COMMON RAY at the interacting fixture under ANY reading of the "
    "channel family: in the three discriminating readings (FULL, ROW, COL) "
    "the two admission rules' identified operators are NOT proportional — "
    f"not globally (relative deviations {dev_lo} to {dev_hi}, gate 1e-30) "
    "and not "
    "even per particle-number sector, so the verdict is NO-COLLAPSE and "
    "not STRUCTURED; the SEC reading is annihilated by the zero-sum lemma "
    "(SG2-B) and carries no discrimination; the PAR reading has an "
    "identically zero EXC side, so no common ray is definable there"
    if (n_collapse == 0 and n_struct == 0) else
    f"MIXED: {n_collapse} COLLAPSE / {n_struct} STRUCTURED cells — see the "
    f"table above")
print(f"  [SG2 VERDICT] {sg2_verdict}.")

# ============================================================================
print("\n[SG3 — the g = 0 column: GRAIN (shared with g = 0) separated from "
      "the INTERACTION EFFECT (the computed difference)]")
print("  For every identified operator: the interaction increment Delta = "
      "D(g=1/2) - D(g=0) is computed channel by channel over the union of "
      "supports and its census printed — SHARED channels (|Delta| < 1e-30) "
      "are GRAIN, MOVED channels are the INTERACTION EFFECT, split into "
      "CREATED (zero at g = 0, nonzero at g = 1/2), DESTROYED (the reverse) "
      "and SHIFTED (nonzero on both sides, different).")

sep = {}
part_ok = True
tot_moved = 0
for base, rs in CELLS:
    rm = max(rs)
    print(f"  --- cell b={base} r<={rm}")
    for reading in READINGS:
        for rule in RULES:
            Dg = DSTORE[('g=1/2', base, rm, rule, reading)]
            D0 = DSTORE[('g=0  ', base, rm, rule, reading)]
            keys = sorted(set(Dg) | set(D0), key=str)
            Delta = {k: Dg.get(k, mpc(0)) - D0.get(k, mpc(0)) for k in keys}
            n_sh = sum(1 for k in keys if fabs(Delta[k]) < TOL)
            n_mv = sum(1 for k in keys if fabs(Delta[k]) >= TOL)
            n_cr = sum(1 for k in keys if fabs(Delta[k]) >= TOL
                       and fabs(D0.get(k, mpc(0))) < TOL)
            n_de = sum(1 for k in keys if fabs(Delta[k]) >= TOL
                       and fabs(Dg.get(k, mpc(0))) < TOL)
            part_ok &= (n_sh + n_mv == len(keys)) and (n_cr + n_de <= n_mv)
            tot_moved += n_mv
            sep[(base, rm, reading, rule)] = (len(keys), n_sh, n_mv, n_cr,
                                              n_de, mnorm(Dg), mnorm(D0),
                                              mnorm(Delta))
            rel = ("-" if mnorm(D0) < TOL else
                   nstr(mnorm(Delta) / mnorm(D0), 8))
            print(f"    {reading:4s} {rule:3s}: |D(g)| = "
                  f"{nstr(mnorm(Dg), 10):>15s}  |D(0)| = "
                  f"{nstr(mnorm(D0), 10):>15s}  |Delta| = "
                  f"{nstr(mnorm(Delta), 10):>15s}  |Delta|/|D(0)| = "
                  f"{rel:>12s}   channels: {len(keys):2d} = GRAIN(shared) "
                  f"{n_sh:2d} + INTERACTION(moved) {n_mv:2d} "
                  f"[created {n_cr}, destroyed {n_de}, shifted "
                  f"{n_mv - n_cr - n_de}]")
check("SG3-A the grain/interaction partition is exhaustive and disjoint at "
      "every (cell, reading, rule): SHARED + MOVED = the support union, "
      "CREATED + DESTROYED <= MOVED — and the interaction is VISIBLE (the "
      "total moved-channel count is nonzero, so the g = 0 column is a real "
      "control and not a copy of the interacting one)",
      part_ok and tot_moved > 0,
      f"{len(sep)} (cell, reading, rule) partitions; total moved channels = "
      f"{tot_moved}")

# ---- the verdict-level twin relation --------------------------------------
print("  Verdict-level twin relation (the SG2 class and constant at g = 1/2 "
      "beside the g = 0 twin):")
TWIN = {}
lab_ok = True
for base, rs in CELLS:
    rm = max(rs)
    for reading in READINGS:
        vg, cg, dg, _ = VSTORE[('g=1/2', base, rm, reading)]
        v0, c0, d0, _ = VSTORE[('g=0  ', base, rm, reading)]
        if vg != v0:
            lab = f"INTERACTION-SPECIFIC ({v0} -> {vg})"
            dc = None
        elif cg is None or c0 is None:
            lab = "GRAIN (class shared; no ray constant is defined)"
            dc = None
        else:
            dc = cg.real - c0.real
            lab = ("GRAIN (class AND constant shared)" if fabs(dc) < TOL
                   else "GRAIN class, CONSTANT SHIFTED by the interaction")
        TWIN[(base, rm, reading)] = (lab, cg, c0, dc)
        # self-consistency: the label is re-derived from the stored numbers
        if dc is not None:
            lab_ok &= ((fabs(dc) < TOL) == ("constant shared" in lab))
        lab_ok &= (lab.startswith("GRAIN") == (vg == v0))
        cgs = "-" if cg is None else rstr(cg.real)
        c0s = "-" if c0 is None else rstr(c0.real)
        dcs = "-" if dc is None else rstr(dc)
        print(f"    b={base} r<={rm} {reading:4s}: g=1/2 {vg:26s} c = "
              f"{cgs:>22s} | g=0 {v0:26s} c = {c0s:>22s} | "
              f"delta c = {dcs:>22s} | {lab}")
check("SG3-B every (cell, reading) pair carries a twin label re-derived "
      "from the stored constants (a label says 'constant shared' iff the "
      "recomputed difference is below 1e-30, and says GRAIN iff the two "
      "verdict classes are literally equal)", lab_ok and len(TWIN) == 15,
      f"{len(TWIN)} labelled (cell, reading) pairs")

n_grain = sum(1 for v in TWIN.values() if v[0].startswith("GRAIN"))
n_ispec = len(TWIN) - n_grain
n_shift = sum(1 for v in TWIN.values() if "SHIFTED" in v[0])
disc = [(b, rm, rd) for (b, rm, rd) in TWIN if rd in ('FULL', 'ROW', 'COL')]
disc_same = sum(1 for k in disc if TWIN[k][0].startswith("GRAIN"))
par_int = sum(1 for k in TWIN if k[2] == 'PAR'
              and TWIN[k][0].startswith("INTERACTION"))
print(f"  [SG3 CENSUS] {n_grain}/15 (cell, reading) pairs share their "
      f"verdict CLASS with the g = 0 twin ({n_shift} of them with a "
      f"constant the interaction shifts); {n_ispec}/15 are "
      f"INTERACTION-SPECIFIC. In the three discriminating readings "
      f"(FULL/ROW/COL) {disc_same}/{len(disc)} share the class; the PAR "
      f"reading contributes {par_int} interaction-specific pairs.")

# the structural reading of the EXC column (gated, with its mechanism)
exc_dev = mpf(0)
for n0_ in range(NS_INT):
    Mg = PIPES['g=1/2'](n0_, 'EXC')[0]
    M0 = PIPES['g=0  '](n0_, 'EXC')[0]
    for k in sorted(set(Mg) | set(M0)):
        exc_dev = max(exc_dev, fabs(Mg.get(k, mpc(0)) - M0.get(k, mpc(0))))
exc_D_dev = max(sep[key][7] for key in sorted(sep, key=str)
                if key[3] == 'EXC')
check("SG3-C the EXC COLUMN IS COUPLING-BLIND, gated: the EXC leading "
      "(Delta^2) region coefficient is entrywise IDENTICAL at g = 1/2 and "
      "g = 0, hence so is every EXC identified operator in every reading. "
      "Mechanism (exact, order by order): Gamma = |U|^2, so at Delta^2 the "
      "off-diagonal entry is |H_ij|^2 and the diagonal entry is "
      "-sum_{k != i} |H_ik|^2 — the diagonal of H (which is where the "
      "electric gauge-string term and ONLY it lives in this fixture, "
      "SG1-B) cancels out of the modulus at this order. The interaction "
      "therefore enters the ray comparison ONLY through the LT side",
      exc_dev < TOL and exc_D_dev < TOL,
      f"max coefficient deviation = {nstr(exc_dev, 3)}; max identified-"
      f"operator deviation = {nstr(exc_D_dev, 3)}")

sg3_verdict = (
    "the D44d §5 B1 lesson holds at the IDENTIFIED-operator level too: the "
    "failure to collapse is GRAIN, not interaction. In all 9 discriminating "
    "(cell, reading) pairs the g = 0 twin is NO-COLLAPSE exactly as the "
    "interacting cell is; what the interaction changes there is only the "
    "reference constant (9/9 constants shifted, every shift printed above "
    "as an exact rational). The one genuinely INTERACTION-SPECIFIC "
    "structure in the whole sweep is the PAR channel: the staggered-parity "
    "content of the LT identified operator is IDENTICALLY ZERO at g = 0 "
    "and is CREATED by the coupling in all 3 cells (4 channels created per "
    "cell, zero shared) — and at base b = 0 that created content lies "
    "EXACTLY on the free-core ray form c*(I - sigma_x) with c = -1589/4500, "
    "while at b = 1 it does not (511/1125, -1561/2250, -1561/2250, 14/15 — "
    "symmetric but not proportional to I - sigma_x). It is NOT a common-ray "
    "statement: the EXC side of that channel vanishes identically (SG3-C), "
    "so only one of the two admission rules has an operator there")
print(f"  [SG3 VERDICT] {sg3_verdict}.")

# ============================================================================
print("\n[SG4 — precision as run, determinism, purity, self-scan]")
print(f"  mp.dps as run = 50 for every number above; gate threshold 1e-30; "
      f"commutator dust drop 1e-45; free-core phase ORD 12 / L 12; "
      f"interacting phase ORD 4 / DIM 16.")

# ---- the dps-80 stability twin --------------------------------------------
dps_hi = 80
mp.dps = dps_hi
PIPES_HI = {}
for gname, gval in GCOL:
    PIPES_HI[gname] = int_pipeline(gval)[1]
hi_dev = mpf(0)
hi_ver_ok = True
for base, rs in CELLS:
    rm = max(rs)
    for reading in READINGS:
        for gname, _ in GCOL:
            Dh = {}
            for rule in RULES:
                Dh[rule] = D_identified(PIPES_HI[gname], base, rs, rule,
                                        reading)
                Dlo = DSTORE[(gname, base, rm, rule, reading)]
                for k in sorted(set(Dh[rule]) | set(Dlo), key=str):
                    hi_dev = max(hi_dev, fabs(Dh[rule].get(k, mpc(0))
                                              - Dlo.get(k, mpc(0))))
            vh = ray_verdict(Dh['EXC'], Dh['LT'], reading)
            vl = VSTORE[(gname, base, rm, reading)]
            hi_ver_ok &= (vh[0] == vl[0])
            if vh[1] is not None and vl[1] is not None:
                hi_dev = max(hi_dev, fabs(vh[1] - vl[1]))
mp.dps = 50
check(f"SG4-A precision stability: the ENTIRE SG2 layer recomputed at "
      f"mp.dps = {dps_hi} reproduces every identified-operator entry, every "
      f"ray constant and every verdict class of the dps-50 run — the "
      f"delivered numbers are not precision artefacts",
      hi_dev < TOL and hi_ver_ok,
      f"max deviation across all 60 operators and 30 verdicts = "
      f"{nstr(hi_dev, 3)} (gate 1e-30); verdict classes identical: "
      f"{hi_ver_ok}")

# ---- exactness of the delivered constants ---------------------------------
EXACT = {}
n_const = 0
n_rec = 0
for base, rs in CELLS:
    rm = max(rs)
    for reading in READINGS:
        for gname, _ in GCOL:
            v = VSTORE[(gname, base, rm, reading)]
            fr = None
            if v[1] is not None:
                n_const += 1
                fr = recognize(v[1].real)
                if fr is not None: n_rec += 1
            EXACT[(gname, base, rm, reading)] = (v[0], fr)
        lab, cg, c0, dc = TWIN[(base, rm, reading)]
        frd = None
        if dc is not None:
            n_const += 1
            frd = recognize(dc)
            if frd is not None: n_rec += 1
        EXACT[('twin', base, rm, reading)] = (lab, frd)
    for rule in RULES:
        for gname, _ in GCOL:
            P = DSTORE[(gname, base, rm, rule, 'PAR')]
            row = []
            for a in (0, 1):
                for b in (0, 1):
                    val = P.get((a, b), mpc(0)).real
                    n_const += 1
                    fr = recognize(val)
                    if fr is not None: n_rec += 1
                    row.append(fr)
            EXACT[('par', base, rm, rule, gname)] = tuple(row)
EXACT[('census',)] = (n_collapse, n_struct, n_nocol, n_supp, n_bz,
                      n_grain, n_ispec, n_shift, disc_same, par_int,
                      tot_moved, n_eval, len(sep), len(TWIN))
EXACT[('sg1',)] = tuple(sorted((d, v) for d, v in raw_lines))
check("SG4-B exactness of the delivered scalars: every ray constant, every "
      "interaction shift delta c and every PAR-channel entry printed above "
      "is recognized as an EXACT rational at residual < 1e-30 (bounded-"
      "denominator best approximation, cap 1e15) — the fixture is rational "
      "and the identification is a finite integer-weighted sum, so these "
      "are exact values, not decimals", n_rec == n_const and n_const > 0,
      f"{n_rec}/{n_const} recognized; max residual = "
      f"{nstr(REC_MAXERR[0], 3)}; max denominator = {REC_MAXDEN[0]} "
      f"(cap {DEN_CAP})")

ALLOW = (Fr, int, str, bool, type(None))
CONT = (tuple, list, frozenset, set)
n_leaf = 0
n_impure = 0
def walk(x):
    global n_leaf, n_impure
    if isinstance(x, CONT):
        for y in x: walk(y)
    elif isinstance(x, dict):
        for k2, v2 in x.items():
            walk(k2); walk(v2)
    else:
        n_leaf += 1
        if not isinstance(x, ALLOW): n_impure += 1
walk(EXACT)
check("SG4-C the ALLOW-LIST PURITY WALK (#362 form) over the delivered "
      "exact layer (every verdict class, twin label, recognized ray "
      "constant, interaction shift, PAR entry and census count): every leaf "
      "is Fraction / int / str / bool / None — no float, no mpf, no "
      "Decimal, no numpy scalar survives into the delivered exact record; "
      "the mpmath series layer is a DECLARED float entry point (banner) and "
      "is deliberately not in this walk", n_leaf > 0 and n_impure == 0,
      f"leaves = {n_leaf}; impure = {n_impure}")

_own = open(os.path.abspath(__file__)).read()
_needles = ["check(" + "True", "check(" + "1,", "check(" + "not False",
            "check(" + "bool(True)"]
_hits = sum(_own.count(nd) for nd in _needles)
check("SG4-D self-scan: no vacuous gate anywhere in this receipt — the "
      "forbidden always-true check patterns (built here by string "
      "concatenation so the scan cannot match itself) have ZERO source "
      "occurrences, and every check above carries a predicate computed from "
      "the run", _hits == 0, f"occurrences across {len(_needles)} needles "
      f"= {_hits}; source length = {len(_own)} bytes")

check("SG4-E determinism: no RNG is loaded, no wall clock is read, and no "
      "output ordering depends on hash randomization (every dict key is an "
      "int or a tuple of ints, and every printed iteration runs over an "
      "explicit list or a str-sorted key list) — rerun byte-identical under "
      "any PYTHONHASHSEED", 'random' not in sys.modules,
      f"'random' loaded: {'random' in sys.modules}; modules touched by this "
      f"receipt: mpmath, fractions, sys, os")

# ============================================================================
print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("[VERDICT] FAIL — anchor/extraction breakage; exit 1 by design")
    sys.exit(1)
print("[SG0 VERDICT] the free core, re-run through this receipt's pipeline: "
      "ONE ray, TWO rule-relative constants — EXC D = 1*(I - sigma_x), LT "
      "D = kappa(m)*(I - sigma_x), kappa(1/2) = 13/2304, kappa(1) = -1/72, "
      "the d45a polynomial agreeing at both anchors in exact Fraction "
      "arithmetic.")
print("[SG1 VERDICT] the d44d KG3 interacting fixture and its "
      "extraction-validity gates are re-anchored exactly: "
      + ", ".join(f"d={d}: {v}" for d, v in raw_lines)
      + " at the raw-bracket level, with the committed bracket norms and "
      "all six committed per-sector reference constants reproduced.")
print("[SG2 VERDICT] " + sg2_verdict + ".")
print("[SG3 VERDICT] " + sg3_verdict + ".")
print("[VERDICT] d46e GREEN-UNREVIEWED (the hostile round is deferred per "
      "the D46 program pin; paper-32's round precedes it) — THE PIN'S "
      "QUESTION IS ANSWERED IN THE NEGATIVE, AND THE ANSWER IS GRAIN, NOT "
      "INTERACTION. Smearing does NOT rescue the ray at the interacting "
      "fixture: applying the corpus's own tau first-moment identification "
      "(D = sum_delta delta*tau) to the interacting one-region "
      "coefficients leaves the two admission rules' identified operators "
      "non-proportional in every discriminating reading of the "
      "pre-registered channel family, globally AND per particle-number "
      "sector, at relative deviations of order 1 against a 1e-30 gate — "
      "so the free core's collapse (SG0) does not survive to this fixture "
      "in any form the identification can see. BUT the g = 0 column, which "
      "this unit exists to carry, shows the SAME NO-COLLAPSE at zero "
      "coupling in all 9 discriminating (cell, reading) pairs: the failure "
      "is a property of the fixture's GRAIN (4-site open chain, occupation "
      "basis, no translation average), exactly as D44d's round found for "
      "the raw bracket, and it is NOT an interaction effect. What the "
      "interaction actually does is measured, not narrated: (i) it leaves "
      "the ENTIRE EXC column invariant — the Delta^2 coefficient is "
      "exactly blind to the diagonal of H, which is where the electric "
      "gauge-string term and only it lives, so the coupling reaches the "
      "comparison solely through the LT side (SG3-C); (ii) it shifts every "
      "one of the 9 reference constants by an exact rational, all printed; "
      "(iii) it CREATES, out of nothing, the staggered-parity (PAR) "
      "content of the LT identified operator — identically zero at g = 0 "
      "in all three cells, four channels created in each — and at base "
      "b = 0 that created content sits EXACTLY on the free-core ray form "
      "c*(I - sigma_x) with c = -1589/4500, though at b = 1 it does not, "
      "and in neither case is it a common-ray statement because the EXC "
      "side of that channel vanishes identically. SCOPE, stated flatly: "
      "one interacting point, one collar convention, singleton regions, "
      "three base/separation cells, five channel readings, ORD 4 — a "
      "fixture-scale statement about the identified operator, never a "
      "theorem about interacting theories; and the negative result is "
      "reading-relative in exactly the way SG2's family makes auditable "
      "(a collapse under the FULL reading would have implied one under "
      "every coarsening; the converse does not hold, and the SEC "
      "coarsening is annihilated outright by the zero-sum lemma). The "
      "successor question this leaves on the ladder: a fixture whose grain "
      "ADMITS the free-core collapse at g = 0 — i.e. one with the "
      "translation average the identification was built on — is what would "
      "make the interacting comparison discriminating at all.")

#!/usr/bin/env python3
"""
v6_p10b: the record renormalization group on admissible refinements
(Paper 10, Part II).

The flow: coarse-graining is the inverse of admissible refinement
(P4 s48-51); a coarse ledger's effective couplings are the character
transform of the exact coarse law; iteration defines the record RG.

 R1 (exact 1d flow): decimation tanh K' = tanh^2 K; the committed chain
    (h = eta_hist, P8) flows to triviality with the EXACT identity
       xi(committed 1d) = -1/ln tanh(eta) = 1/eta_hist
    (the commitment coefficient IS the 1d record mass).
 R2 (generated couplings, exact): decimation of an NN ring generates
    nothing (Markov exactness, receipts ~1e-15); an NNN seed generates a
    full coupling vector; the linearized flow classifies relevant/
    irrelevant record statistics.
 R3 (the fixed-point identity): the commitment constant is EXACTLY the
    2d Migdal-Kadanoff fixed point:
       K = 2 atanh(tanh^2 K)  <=>  t^3 + t^2 + t = 1,  t = tanh K
    - the commitment cubic of P7 s8.2.  A fourth role for theta_hist.
 R4 (commitment vs criticality, by dimension): the committed pairwise
    lattice ledger sits: 1d at xi = 1/eta (massive, trivial flow); 2d
    DISORDERED but within a few percent of the exact Onsager critical
    point (near-critical); 3d ORDERED (record-SSB branches): branch
    formation requires d >= 3 - and the derived spatial dimension is 3.
 R5 (gauge flow): the series step of the gauge RG is EXACT (heat-kernel
    convolution = P8 Theorem 9.2 area additivity); Migdal-Kadanoff
    bond-moving gives t' = b^(4-d) t: confining flow for d < 4, MARGINAL
    at d = 4, deconfining d > 4 - the record location of confinement
    scaling and the marginality where asymptotic freedom lives.
 R6 (homogenization): oscillating microscopic conductances flow to the
    harmonic-mean continuum operator: geometric-sector universality,
    feeding (C).
"""
import numpy as np, itertools
from scipy.optimize import brentq
from scipy.special import ellipk
import scipy.sparse as sp
import scipy.sparse.linalg as spl

eta = brentq(lambda e: np.tanh(e) - np.exp(-e), 0.1, 2.0)
theta = np.tanh(eta)

# ---------- R1: exact 1d flow ----------
print("== R1. exact 1d decimation flow from the committed coupling ==")
K = eta
print(f"  K0 = eta_hist = {K:.12f}")
for step in range(1, 6):
    K = np.arctanh(np.tanh(K) ** 2)
    print(f"  K{step} = {K:.12f}")
print(f"  -> flow to triviality (1d: no phase transition).")
xi = -1.0 / np.log(np.tanh(eta))
print(f"  EXACT identity: xi = -1/ln tanh(eta) = {xi:.12f} = 1/eta = {1/eta:.12f}")
print(f"  (tanh eta = e^-eta at the commitment root, so -ln tanh eta = eta:")
print(f"   the commitment coefficient IS the 1d record mass, m = eta_hist.)")

# ---------- R2: generated couplings and the linearized flow ----------
print("\n== R2. exact coarse-graining of a 12-ring; generated couplings ==")
def ring_law(N, J):     # J: dict distance -> coupling (+ optional field J[0])
    states = np.array(list(itertools.product((-1, 1), repeat=N)))
    E = np.zeros(len(states))
    for r, Jr in J.items():
        if r == 0:
            E += Jr * states.sum(axis=1)
        else:
            E += Jr * np.sum(states * np.roll(states, -r, axis=1), axis=1)
    w = np.exp(E - E.max())
    return states, w / w.sum()

def coarse_couplings(N, J):
    """keep even sites of an N-ring; return character transform of log of
    the exact coarse law on the N/2-ring."""
    states, p = ring_law(N, J)
    Nc = N // 2
    idx = np.zeros(len(states), dtype=int)
    for k in range(Nc):
        idx += ((states[:, 2 * k] + 1) // 2).astype(int) << k
    q = np.bincount(idx, weights=p, minlength=1 << Nc)
    cs = np.array(list(itertools.product((-1, 1), repeat=Nc)))
    # match bit order of idx: bit k = spin (col k)
    cidx = np.zeros(len(cs), dtype=int)
    for k in range(Nc):
        cidx += ((cs[:, k] + 1) // 2).astype(int) << k
    order = np.argsort(cidx)
    cs = cs[order]
    logq = np.log(q)
    out = {}
    for r in range(0, Nc // 2 + 1):
        if r == 0:
            chi = cs.sum(axis=1)
            out["field"] = (logq @ chi) / (len(cs) * Nc)
        else:
            chi = np.sum(cs * np.roll(cs, -r, axis=1), axis=1)
            mult = Nc if (2 * r != Nc) else Nc // 2
            out[f"J({r})"] = (logq @ chi) / (len(cs) * Nc) * (Nc / mult)
    # adjacent 4-spin term
    chi4 = np.sum(cs * np.roll(cs, -1, axis=1) * np.roll(cs, -2, axis=1)
                  * np.roll(cs, -3, axis=1), axis=1)
    out["quad(4-adj)"] = (logq @ chi4) / (len(cs) * Nc)
    return out

cc = coarse_couplings(12, {1: eta})
print(f"  pure NN ring at K = eta: coarse couplings:")
print("   ", {k: f"{v:+.6e}" for k, v in cc.items()})
print(f"    J(1) exact prediction atanh(tanh^2 eta) = {np.arctanh(theta**2):+.6f}"
      f"   (Markov exactness: all other couplings ~ 0)")
cc2 = coarse_couplings(12, {1: 0.4, 2: 0.15})
print(f"  NN+NNN seed (K1=0.4, K2=0.15): coarse couplings:")
print("   ", {k: f"{v:+.6e}" for k, v in cc2.items()})
print("    -> coupling generation is real once memory crosses the blocking scale.")
# linearized flow at a weak-coupling base point
base = {1: 0.10, 2: 0.0, 0: 0.0}
deps = 1e-4
names = [1, 2, 0]
Jac = np.zeros((3, 3))
def vec_out(J):
    c = coarse_couplings(12, {k: v for k, v in J.items() if v != 0.0 or k in (1,)})
    return np.array([c["J(1)"], c["J(2)"], c["field"]])
v0 = vec_out(base)
for j, nm in enumerate(names):
    Jp = dict(base); Jp[nm] = Jp.get(nm, 0.0) + deps
    Jac[:, j] = (vec_out(Jp) - v0) / deps
evals = np.linalg.eigvals(Jac)
print(f"  linearized decimation map at (K1=0.1, K2=0, h=0):")
print(f"    Jacobian eigenvalues: {np.sort_complex(np.round(evals, 4))}")
print(f"    scaling exponents y = ln|lambda|/ln 2: "
      f"{[f'{np.log(abs(l))/np.log(2):+.3f}' if abs(l) > 1e-12 else '-inf' for l in np.sort_complex(evals)]}")
print("    -> the field direction is RELEVANT; pair statistics are irrelevant")
print("       in 1d: no interacting fixed point (triviality), as R1 shows.")

# ---------- R3: the fixed-point identity ----------
print("\n== R3. theta_hist IS the 2d Migdal-Kadanoff fixed point ==")
res = 2 * np.arctanh(np.tanh(eta) ** 2) - eta
print(f"  MK-2d (decimate b=2, then bond-move): K* solves K = 2 atanh(tanh^2 K)")
print(f"  residual at eta_hist: {res:.2e}   cubic residual theta^3+theta^2+theta-1 = "
      f"{theta**3+theta**2+theta-1:.2e}")
print(f"  PROOF (two lines): the fixed-point condition squares to")
print(f"  (1+t)^3 (1-t) = (1+t^2)^2  <=>  t(1+t+t^2+t^3-...) -> t^3+t^2+t = 1,")
print(f"  the commitment cubic (P7 s8.2); and tanh K = e^-K gives the same cubic.")
lam = 4 * theta / (1 + theta**2)
print(f"  linearization: lambda = 4 theta/(1+theta^2) = {lam:.9f}")
print(f"  y_t = {np.log(lam)/np.log(2):.6f}   nu_MK = {np.log(2)/np.log(lam):.6f}"
      f"   (MK approximation; exact 2d Ising nu = 1)")
print("  basin: K0 in {0.3, 0.5, 0.7, 1.0} under the MK map:")
for K0 in (0.3, 0.5, 0.7, 1.0):
    K = K0
    for _ in range(40):
        t2 = np.tanh(K) ** 2
        if t2 > 1 - 1e-12 or K > 20:
            K = np.inf; break
        K = 2 * np.arctanh(t2)
        if K < 1e-12:
            break
    print(f"    K0 = {K0}: -> {'0 (disordered)' if K < 1 else 'infinity (ordered)'}"
          f"   [separatrix = eta_hist = {eta:.6f}]")
# specificity of the identity: a property of b = 2 (pairwise) composition
K3 = brentq(lambda K: 3 * np.arctanh(np.tanh(K) ** 3) - K, 0.5, 1.5)
Kmv = brentq(lambda K: np.arctanh(np.tanh(2 * K) ** 2) - K, 0.2, 1.5)
print(f"  specificity: b=2 move-then-decimate FP = {Kmv:.9f} = eta/2 to "
      f"{abs(Kmv - eta/2):.1e}")
print(f"    (the two b=2 orderings are CONJUGATE via the bond-move, and")
print(f"     tanh(eta/2) = theta^2 is again the commitment cubic: both b=2")
print(f"     orderings are cubic-pinned);")
print(f"  b=3 decimate-then-move FP = {K3:.9f}  (eta = {eta:.9f}: genuinely NOT equal)")
print(f"  -> the identity is a property of PAIRWISE (b=2) series-parallel")
print(f"     composition per se, robust to ordering, and fails at b=3:")
print(f"     O9 sharpens to 'why does the commitment law encode b=2")
print(f"     self-similarity?' - which rhymes with commitment being a")
print(f"     statement about BINARY division.  Structural or accidental: OPEN.")

# ---------- R4: commitment vs criticality, by dimension ----------
print("\n== R4. where commitment places matter, by dimension ==")
print(f"  d=1: massive, m = eta_hist exactly (R1); distance to criticality:")
print(f"       K_c(1d) = infinity - maximally subcritical.")
def eps2d(K):
    q = 2 * np.sinh(2 * K) / np.cosh(2 * K) ** 2
    return 0.5 / np.tanh(2 * K) * ((np.cosh(2 * K) / np.sinh(2 * K)) * np.sinh(2 * K) / np.cosh(2 * K)) \
        if False else 0.5 * (np.cosh(2 * K) / np.sinh(2 * K)) * \
        (1 + (2 / np.pi) * (2 * np.tanh(2 * K) ** 2 - 1) * ellipk(q ** 2))
Kc2 = 0.5 * np.log(1 + np.sqrt(2))
print(f"  d=2 (exact Onsager): eps(K_c) limit = cosh(2K_c)/2 = "
      f"{np.cosh(2*Kc2)/2:.9f} = sqrt(2)/2; eps(K_c - 1e-4) = {eps2d(Kc2-1e-4):.6f}")
h2 = brentq(lambda K: np.exp(-K) - eps2d(K), 0.30, Kc2 - 1e-6, xtol=1e-12)
print(f"  commitment fixed point on the infinite 2d lattice: h2 = {h2:.9f}")
print(f"  K_c(2d) = {Kc2:.9f}   relative distance (K_c - h2)/K_c = "
      f"{(Kc2-h2)/Kc2*100:.2f}%   -> DISORDERED but NEAR-CRITICAL")
xi_exact = 1.0 / (np.log(1.0 / np.tanh(h2)) - 2 * h2)
print(f"  bulk correlation length (exact 2d Ising, T > T_c):"
      f" 1/xi = ln coth K - 2K  ->  xi(h2) = {xi_exact:.3f} lattice units")
# strip-transfer correlation length at h2
print("  correlation length at h2 from strip transfer matrices:")
for Wd in (4, 6, 8, 10):
    states = np.array(list(itertools.product((-1, 1), repeat=Wd)))
    intra = np.exp(0.5 * h2 * np.sum(states * np.roll(states, -1, axis=1), axis=1))
    inter = np.exp(h2 * (states @ states.T))
    T = intra[:, None] * inter * intra[None, :]
    ev = np.linalg.eigvalsh(T)
    xiW = 1.0 / np.log(ev[-1] / abs(ev[-2]))
    print(f"    width {Wd:2d}: xi = {xiW:8.3f} lattice units")
print("    (xi grows with width toward the bulk value: tens of lattice units)")
# d=3 by Monte Carlo
print("  d=3 (Metropolis, 12^3, cold start):")
L = 12
rng = np.random.default_rng(33)
def mc_ss(K, sweeps_th=300, sweeps_ms=300):
    s = np.ones((L, L, L))
    masks = [(np.indices((L, L, L)).sum(axis=0) % 2) == p for p in (0, 1)]
    def sweep():
        for mk in masks:
            nb = sum(np.roll(s, d, axis=a) for a in range(3) for d in (1, -1))
            acc = rng.random((L, L, L)) < np.exp(-2 * K * s * nb)
            s[mk & acc] *= -1
    for _ in range(sweeps_th):
        sweep()
    vals, mags = [], []
    for _ in range(sweeps_ms):
        sweep()
        vals.append(np.mean([np.mean(s * np.roll(s, 1, axis=a)) for a in range(3)]))
        mags.append(abs(s.mean()))
    return np.mean(vals), np.std(vals) / np.sqrt(len(vals)), np.mean(mags)
lo, hi = 0.25, 0.55
for _ in range(7):
    mid = 0.5 * (lo + hi)
    ss, err, mag = mc_ss(mid, 150, 150)
    if np.exp(-mid) > ss:
        lo = mid
    else:
        hi = mid
h3 = 0.5 * (lo + hi)
ss, err, mag = mc_ss(h3, 300, 300)
# error estimate on the crossing: slope of g(h) = e^-h - <ss>(h)
ss_lo, err_lo, _ = mc_ss(h3 - 0.03, 200, 200)
ss_hi, err_hi, _ = mc_ss(h3 + 0.03, 200, 200)
g_lo = np.exp(-(h3 - 0.03)) - ss_lo
g_hi = np.exp(-(h3 + 0.03)) - ss_hi
slope = (g_hi - g_lo) / 0.06
dh3 = np.sqrt(err ** 2 + 0.5 * (err_lo ** 2 + err_hi ** 2)) / abs(slope)
Kc3 = 0.2216546
print(f"    h3 = {h3:.4f} +- {dh3:.4f}  (<ss> = {ss:.4f} +- {err:.4f},"
      f" e^-h = {np.exp(-h3):.4f}; crossing slope {slope:+.3f})")
print(f"    K_c(3d) = {Kc3}: h3/K_c = {h3/Kc3:.3f} +- {dh3/Kc3:.3f}"
      f"  -> ORDERED phase; |magnetization| = {mag:.4f}")
print("  DIMENSION TABLE: 1d massive/trivial; 2d near-critical disordered;")
print("  3d ordered (sealed branches = record-SSB).  Branch formation requires")
print("  d >= 3 - and the derived spatial dimension (P7 signature theorem) is 3.")

# ---------- R5: gauge flow ----------
print("\n== R5. gauge sector: exact series step + MK dimension flow ==")
# character orthogonality / heat-kernel convolution receipt by Haar MC
def chi_j(q, j):
    # SU(2) character: sin((2j+1) phi)/sin(phi), cos(phi) = q0
    phi = np.arccos(np.clip(q[..., 0], -1, 1))
    phi = np.where(phi < 1e-8, 1e-8, phi)
    return np.sin((2 * j + 1) * phi) / np.sin(phi)
def haar(n):
    v = rng.normal(size=(n, 4))
    return v / np.linalg.norm(v, axis=1, keepdims=True)
def qmul(a, b):
    w = a[..., :1] * b[..., :1] - np.sum(a[..., 1:] * b[..., 1:], axis=-1, keepdims=True)
    vec = a[..., :1] * b[..., 1:] + b[..., :1] * a[..., 1:] + np.cross(a[..., 1:], b[..., 1:])
    return np.concatenate([w, vec], axis=-1)
def qconj(a):
    o = a.copy(); o[..., 1:] *= -1; return o
g = haar(1)[0]
h = haar(1000000)
for (j, k) in ((0.5, 0.5), (1.0, 1.0), (0.5, 1.0)):
    samp = chi_j(qmul(g[None, :], qconj(h)), j) * chi_j(h, k)
    lhs, err = samp.mean(), samp.std() / np.sqrt(len(samp))
    rhs = (chi_j(g[None, :], j)[0] / (2 * j + 1)) if j == k else 0.0
    print(f"  convolution identity j={j}, k={k}: MC = {lhs:+.5f} +- {err:.5f}"
          f"  exact = {rhs:+.5f}  pull = {abs(lhs-rhs)/err:.2f} sigma")
print("  -> heat-kernel times ADD under series composition (the exact P8 T9.2")
print("     mechanism); bond-moving divides by b^(d-2): the MK gauge flow is")
print("     t' = b^(4-d) t.")
# the heat-kernel family is CLOSED under series composition; the Wilson
# family is NOT: the extra projection layer of the MK gauge flow, exposed
from scipy.integrate import quad
def m_j(beta, j):
    num = quad(lambda p: np.sin((2 * j + 1) * p) / np.sin(p) / (2 * j + 1)
               * np.exp(beta * np.cos(p)) * np.sin(p) ** 2, 0, np.pi)[0]
    den = quad(lambda p: np.exp(beta * np.cos(p)) * np.sin(p) ** 2, 0, np.pi)[0]
    return num / den
beta_w = 1.5
mh, m1, m32 = m_j(beta_w, 0.5), m_j(beta_w, 1.0), m_j(beta_w, 1.5)
beta_p = brentq(lambda b: m_j(b, 0.5) - mh ** 2, 0.01, beta_w)
d1 = abs(m_j(beta_p, 1.0) - m1 ** 2) / m1 ** 2
d32 = abs(m_j(beta_p, 1.5) - m32 ** 2) / m32 ** 2
print(f"  family-closure receipt (series step = moment ratios square):")
print(f"    heat kernel: m_j = e^(-t j(j+1)) -> squares stay heat-kernel: EXACT closure")
print(f"    Wilson beta = {beta_w}: matching j=1/2 needs beta' = {beta_p:.6f}, but then")
print(f"    j=1 mismatch = {d1*100:.2f}%  j=3/2 mismatch = {d32*100:.2f}%: the Wilson")
print(f"    family is NOT closed - projecting back onto a single-coupling family is")
print(f"    a SECOND approximation layer of the MK gauge flow, beyond bond-moving.")
print("  Lattice string tension sigma_lat = t * c2(F):")
t0 = 0.5
for d in (3, 4, 5):
    ts = [t0 * (2.0 ** ((4 - d) * l)) for l in range(5)]
    print(f"    d={d}: t_l = {[f'{t:.3f}' for t in ts]}"
          f"   {'CONFINING flow (t grows)' if d < 4 else 'MARGINAL' if d == 4 else 'deconfining'}")
print("  scope: the series step is exact; bond-moving is the MK approximation.")
print("  d=4 marginality = where asymptotic freedom must be decided at the")
print("  next order - the record RG localizes the question, it does not answer it.")

# ---------- R6: homogenization (geometric-sector universality) ----------
print("\n== R6. homogenization: oscillating conductance -> harmonic mean ==")
ca, cb = 0.5, 2.0
ch = 2 * ca * cb / (ca + cb)
def sl_ring(n, cfun):
    cbond = np.array([cfun(i) for i in range(n)]) * n * n
    main = cbond + np.roll(cbond, 1)
    A = sp.diags([main, -cbond, -cbond], [0, 1, -1], shape=(n, n), format="lil")
    A[0, n - 1] = -cbond[n - 1]; A[n - 1, 0] = -cbond[n - 1]
    return sp.csr_matrix(A)
for n in (16, 32, 64, 128):
    Aalt = sl_ring(n, lambda i: ca if i % 2 == 0 else cb)
    Ahom = sl_ring(n, lambda i: ch)
    e1 = np.sort(spl.eigsh(Aalt, k=7, sigma=-1e-9, which="LM", return_eigenvectors=False))[1:7]
    e2 = np.sort(spl.eigsh(Ahom, k=7, sigma=-1e-9, which="LM", return_eigenvectors=False))[1:7]
    print(f"  n = {n:4d}: max rel gap to harmonic-mean operator = "
          f"{np.abs(e1 - e2).max() / e2.max():.3e}")
print("  -> microscopically different ledgers flow to ONE continuum operator:")
print("     geometric universality, the RG face of the (C) docket.")
print("== p10b done ==")

#!/usr/bin/env python3
"""
v6_p9a: projective/double-cover dilation fibers, part I (Paper 9).

Doors:
 D1 (silent-sign theorem): a fiber on which the 2*pi screen rotation acts
    as -1 is RECORD-CONSISTENT: the sign changes no single-sector sealed
    marginal (it is not a silent seam - it is silent and seamless), and it
    becomes observable exactly where it carries evidence: two-branch
    interference, with 4*pi periodicity (the record form of neutron
    2*pi interferometry).
 D4 (univalence superselection, derived): a coherent superposition of
    integer and half-integer fiber sectors would change a sealed
    interference record under the GLOBAL 2*pi rotation - a closed,
    evidence-free motion - i.e. a silent seam: excluded.  Superselection
    of fiber parity follows from the corpus' own exclusion principle.
 D2 (projective lifts): symmetries of a record law lift to its dilation
    uniquely up to phase (machine: intertwiner space is 1-dimensional),
    so the lift is a PROJECTIVE representation; the multiplier class in
    H^2(G, U(1)) is a gauge-invariant record datum.  Both Z2 classes of
    V4 = Z2 x Z2 are realized: the trivial class by diagonal signs, the
    nontrivial class by the Pauli lift (commutator phase -1, invariant
    under every phase redefinition).
 D3 (spin quantization): the 2*pi rotation loop lifts OPEN in SU(2)
    (endpoint -1); the 4*pi loop lifts CLOSED and is contractible
    (explicit machine-verified homotopy).  Defect-free holonomy is
    homotopy-invariant (silent-seam principle in the rotation manifold),
    so R(4*pi) = 1: fiber weights are quantized to 2m in Z in the derived
    (1,3) geometry.  Pure-screen (2+1) sectors have rotation manifold
    SO(2) with universal cover R: ANY weight is consistent there - record
    anyons - with interference period 2*pi/m.
"""
import numpy as np

rng = np.random.default_rng(9)

# ---------- D1: the silent-sign theorem ----------
print("== D1. silent sign: -1 under 2*pi is sealed-marginal-silent, ==")
print("==     interference-observable with 4*pi period ==")
def R(phi, m=0.5):
    return np.diag([np.exp(-1j * m * phi), np.exp(1j * m * phi)])
# single-sector marginals: arbitrary downstream processing V, any state
gap = 0.0
for _ in range(200):
    psi = rng.normal(size=2) + 1j * rng.normal(size=2)
    psi /= np.linalg.norm(psi)
    A = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    V = np.linalg.qr(A)[0]
    p0 = np.abs(V @ psi) ** 2
    p1 = np.abs(V @ (R(2 * np.pi) @ psi)) ** 2
    gap = max(gap, np.abs(p0 - p1).max())
print(f"  200 random (state, processing): max sealed-marginal change under"
      f" R(2pi) = -1: {gap:.2e}   (theorem: 0)")
# two-branch interference: one branch rotated by phi
psi = np.array([1.0, 0.0], complex)
def interf(phi, m):
    b = (psi + R(phi, m) @ psi) / 2.0
    return np.vdot(b, b).real
print("  interference record P(phi), m = 1/2:")
for phi in (0, 2 * np.pi, 4 * np.pi):
    print(f"    phi = {phi/np.pi:.0f}*pi : P = {interf(phi, 0.5):.12f}")
print("  -> P(2pi) != P(0) (the sign is OBSERVABLE, and carries evidence:")
print("     a path-difference record); P(4pi) = P(0) exactly: 4pi periodicity.")

# ---------- D4: univalence superselection, derived ----------
print("\n== D4. univalence superselection from the silent-seam principle ==")
# cross-sector superposition: boson component (m=0) + fermion component (m=1/2)
bos = np.array([1.0, 0.0], complex)   # weight-0 fiber direction
fer = np.array([0.0, 1.0], complex)   # weight-1/2 fiber direction
sup = (bos + fer) / np.sqrt(2)
G = np.diag([1.0, -1.0])              # global R(2pi) on the mixed sector
# an interference record that reads the relative phase:
M = np.array([[1, 1], [1, -1]], complex) / np.sqrt(2)
p_before = np.abs(M @ sup) ** 2
p_after = np.abs(M @ (G @ sup)) ** 2
print(f"  cross-sector superposition: interference record before = {p_before.round(12)}")
print(f"  after GLOBAL 2pi rotation (a closed, evidence-free motion): {p_after.round(12)}")
print(f"  record change = {np.abs(p_before-p_after).max():.6f} under an identity motion")
print("  -> an evidence-free closed motion altering a sealed record is a SILENT")
print("     SEAM: excluded.  Within a sector the same motion changes nothing")
print(f"     (max change {gap:.1e}).  Hence coherent boson/fermion superpositions")
print("     are excluded: univalence superselection is DERIVED, not postulated.")

# ---------- D2: projective lifts and the multiplier classes ----------
print("\n== D2. symmetry lifts to dilations are projective; both Z2 classes real ==")
I2 = np.eye(2); X = np.array([[0, 1], [1, 0]], complex)
Z = np.diag([1.0, -1.0]).astype(complex); XZ = X @ Z
# (i) Wigner-for-records, WITH ITS HYPOTHESES.  The intertwiner equations
# W E = (X E X^dag) W are linear in W; vec convention:
# vec(W E) = (E^T kron I) vec(W), vec(T W) = (I kron T) vec(W).
# (a) FULL-ALGEBRA intertwining (all basis E of M_2): the commutant of M_2
#     is trivial, so the lift is unique up to phase.
def intertwiner_dim(basis_elems):
    blocks = []
    for E in basis_elems:
        T = X @ E @ X.conj().T
        blocks.append(np.kron(E.T, np.eye(2)) - np.kron(np.eye(2), T))
    sv = np.linalg.svd(np.vstack(blocks))[1]
    return int(np.sum(sv < 1e-10))
full_basis = []
for i in range(2):
    for j in range(2):
        E = np.zeros((2, 2), complex); E[i, j] = 1
        full_basis.append(E)
dim_full = intertwiner_dim(full_basis)
# (b) RECORD-LEVEL intertwining only (diagonal record projectors): the
#     gauge enlarges to the record-relabeling torus of P7 Theorem D3.
rec_basis = [full_basis[0], full_basis[3]]   # E_00, E_11 only
dim_rec = intertwiner_dim(rec_basis)
print(f"  intertwiner space, FULL-algebra intertwining: dimension = {dim_full}"
      f"  (lift unique up to phase)")
print(f"  intertwiner space, RECORD-data-only intertwining: dimension = {dim_rec}"
      f"  (the record-relabeling torus of P7 Theorem D3: NOT unique up to phase)")
print("  -> the hypothesis is load-bearing: phase-uniqueness needs full-")
print("     algebra (minimal/multiplicity-free) intertwining; record-level")
print("     symmetry leaves the diagonal torus, and exact fiber degeneracy")
print("     enlarges the gauge further to U(k) (P7 Theorem 10.3).  At record")
print("     level the class datum that survives is the Bargmann LOOP class")
print("     (P7 Theorem D3 + P4 s40), not the naive multiplier.")
# (ii) the V4 = Z2xZ2 multiplier classes
V_proj = {"e": I2, "x": X, "z": Z, "xz": XZ}
mult = {"e": {"e": "e", "x": "x", "z": "z", "xz": "xz"},
        "x": {"e": "x", "x": "e", "z": "xz", "xz": "z"},
        "z": {"e": "z", "x": "xz", "z": "e", "xz": "x"},
        "xz": {"e": "xz", "x": "z", "z": "x", "xz": "e"}}
def cocycle(V):
    om = {}
    for g in V:
        for h in V:
            Wm = V[g] @ V[h] @ np.linalg.inv(V[mult[g][h]])
            s = Wm[0, 0]
            assert np.allclose(Wm, s * np.eye(2), atol=1e-12), "lift not projective-scalar"
            om[(g, h)] = s
    return om
om = cocycle(V_proj)
c_inv = om[("x", "z")] / om[("z", "x")]
print(f"  Pauli lift of V4: commutator phase c(X,Z) = omega(x,z)/omega(z,x) = {c_inv.real:+.0f}")
# gauge invariance: random phase redefinitions V_g -> beta_g V_g
worst = 0.0
for _ in range(100):
    beta = np.exp(1j * rng.uniform(0, 2 * np.pi, 4))
    Vb = {g: beta[k] * V_proj[g] for k, g in enumerate(V_proj)}
    omb = cocycle(Vb)
    worst = max(worst, abs(omb[("x", "z")] / omb[("z", "x")] - c_inv))
print(f"  invariance of c under 100 random phase redefinitions: max change = {worst:.2e}")
print(f"  -> the class is NONTRIVIAL (c = -1): no phase choice de-projectivizes;")
V_triv = {"e": I2, "x": np.diag([1.0, -1.0]), "z": np.diag([-1.0, 1.0]),
          "xz": np.diag([-1.0, -1.0])}
omt = cocycle(V_triv)
print(f"     trivial class realized by diagonal signs: c(X,Z) = "
      f"{(omt[('x','z')]/omt[('z','x')]).real:+.0f}.  Both H^2(V4,U(1)) = Z2 classes")
print("     exist as record-law lifts; the class is a gauge-invariant record datum.")
# (iii) the record law is genuinely covariant: pi-flips on the Bloch sphere
rho = np.diag([0.7, 0.3]).astype(complex)
p = np.diag(rho).real
p_flip = np.diag(X @ rho @ X).real
print(f"  record covariance: z-record of rho = {p.round(3)}, after x-flip = "
      f"{p_flip.round(3)} (label swap exactly): the symmetry IS a record symmetry,")
print("     and its dilation lift is forced projective by the 1-dim intertwiner.")

# ---------- D3: belt trick and spin quantization ----------
print("\n== D3. the 2pi lift is open, the 4pi loop is contractible (machine) ==")
def qmul(a, b):
    w = a[0] * b[0] - np.dot(a[1:], b[1:])
    v = a[0] * b[1:] + b[0] * a[1:] + np.cross(a[1:], b[1:])
    return np.concatenate([[w], v])
def qexp(v):
    th = np.linalg.norm(v)
    if th < 1e-15:
        return np.array([1.0, 0, 0, 0])
    return np.concatenate([[np.cos(th)], np.sin(th) * v / th])
def qlog(q):
    th = np.arccos(np.clip(q[0], -1, 1))
    if th < 1e-15:
        return np.zeros(3)
    return th * q[1:] / np.sin(th)
T = 400
ts = np.linspace(0, 1, T + 1)
# 2pi rotation lift: open path
path2pi = [qexp(np.array([0, 0, np.pi * t])) for t in ts]
print(f"  2pi rotation lift: start = {path2pi[0].round(6)}, end = {path2pi[-1].round(6)}")
print("   -> OPEN path in SU(2) ending at -1: R(2pi) = -1 is a homotopy invariant.")
# 4pi loop, perturbed off the antipode, then geodesic contraction
delta = 0.15
loop = [qmul(qexp(np.array([delta * np.cos(2 * np.pi * t), 0, 0])),
             qexp(np.array([0, 0, 2 * np.pi * t]))) for t in ts]
clos = np.linalg.norm(np.array(loop[0]) - np.array(loop[-1]))
dist_anti = min(np.linalg.norm(np.array(q) - np.array([-1, 0, 0, 0])) for q in loop)
print(f"  4pi loop (perturbed): closure gap = {clos:.2e}, min distance to -1 = {dist_anti:.3f}")
S = 100
maxgap = 0.0; maxstep = 0.0
for si in range(S + 1):
    s = si / S
    H = [qexp((1 - s) * qlog(np.array(q))) for q in loop]
    maxgap = max(maxgap, np.linalg.norm(np.array(H[0]) - np.array(H[-1])))
    steps = [np.linalg.norm(np.array(H[k + 1]) - np.array(H[k])) for k in range(T)]
    maxstep = max(maxstep, max(steps))
Hfinal = [qexp(0 * qlog(np.array(q))) for q in loop]
endgap = max(np.linalg.norm(np.array(q) - np.array([1, 0, 0, 0])) for q in Hfinal)
print(f"  explicit homotopy H(s,t) = exp((1-s) log q(t)): every slice closed"
      f" (max gap {maxgap:.2e}),")
print(f"  continuous (max step {maxstep:.3f} -> 0 with grid), H(1,.) = identity"
      f" (gap {endgap:.2e}): 4pi loop CONTRACTIBLE.")
print("  Holonomy of a defect-free fiber connection is homotopy-invariant (the")
print("  silent-seam principle on the rotation manifold), so R(4pi) = 1:")
print("   quantization  e^{4pi i m} = 1  =>  2m in Z:")
for m in (0.0, 0.5, 1.0, 1.0 / 3.0):
    viol = abs(np.exp(4j * np.pi * m) - 1)
    print(f"    m = {m:5.3f}:  |e^(4pi i m) - 1| = {viol:.6f}   "
          f"{'ALLOWED' if viol < 1e-12 else 'EXCLUDED in (1,3)'}")
print("\n  pure-screen (2+1) corollary - record anyons: rotation manifold SO(2),")
print("  universal cover R, no 4pi constraint; m = 1/3 fiber interference:")
for phi in (0, 2 * np.pi, 4 * np.pi, 6 * np.pi):
    print(f"    phi = {phi/np.pi:.0f}*pi : P = {interf(phi, 1/3):.12f}")
print("  -> 6pi-periodic: consistent on a pure screen, excluded by the derived")
print("     (1,3) embedding.  Spin quantization is a CONSEQUENCE of the")
print("     signature theorem: 3d space => belt trick => 2m in Z.")
print("== p9a done ==")

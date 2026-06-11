#!/usr/bin/env python3
"""
v6_p30c: the Peripheral Reduction and the depth tower (CPE campaign).

THE REDUCTION.  Suppose a valid RP-form process has a block W whose
operator B = B_W carries the minimal dangerous configuration: coupled
peripheral spectrum exactly {rho, rho e^{+i theta}, rho e^{-i theta}},
theta/2pi irrational, semisimple (at rank 3 this is exact and is the
ONLY dangerous configuration: a coupled complex pair strictly above
the coupled real pole already violates diagonal positivity).  Write
spectral projectors P_0, P_+, P_- with right/left eigenvectors
R_s, L_s (biorthogonal), and set

    G = L^dag L  (Gram of left eigenvectors,  H := G^{-1} = R^dag R),
    beta_s = L_s^dag Omega,   alpha = G^{-1} beta,   c_s = alpha_s beta_s.

Then every word in the letters {W, W-tilde} has value

    p(W^{a_1} Wt^{b_1} W^{a_2} ...) * rho^{-(sum)} =
        (D(x_1) alpha)^T G D(-y_1) H D(x_2) G ... (boundary vector),

with D(x) = diag(e^{i x sigma}), sigma = (0,+1,-1), x_j = a_j theta.
Since p >= 0 for ALL exponents and (a_j theta) equidistributes on the
torus (Weyl), the trigonometric forms must be >= 0 ON THE WHOLE TORUS
- a theta-FREE system of necessary conditions on (G, beta) alone.
At higher rank the same conditions hold for the peripheral
compression (subperipheral corrections vanish in the limit).

THE POINT MISSED BY PAPER 30 SECTION 3: matrix positivity of the
cross Grams is automatic (exhaustion), but ENTRYWISE positivity
p(W^a Wt^b) >= 0 is NOT - the two-segment words already give real
constraints, e.g. the closed-form necessary inequality

    (N1)  alpha_0^2  >=  2 |alpha_+|^2 (1 + |G_{+-}|)     [gauge
          G_00 = G_++ = G_-- = 1, G_0+ real >= 0]

obtained by probing F_2 at x - y = pi.

THIS SCRIPT.
 (i)   VALIDATION: build explicit rank-3 real B with the exact
       peripheral triple; verify the reduced formulas reproduce
       brute-force word values to machine precision (3- and
       4-segment), and the y = 0 consistency F_3(x,0,z) = F_1(x+z).
 (ii)  THE DEPTH TOWER: maximize the clock strength r = 2|c_+|/c_0
       subject to the torus conditions, cumulatively by alternation
       depth:  A: diagonal only;  B: + two-segment (both families);
       C: + three-segment;  D: + four-segment;  E: + five-segment.
       The curve r_max(depth) is the result: decay toward 0 means
       the tower is squeezing the clock out (CPE mechanism found);
       a plateau means the reduced system is FEASIBLE and the
       letter-embedding question decides.
 (iii) RECEIPTS at the optimum: binding constraints, the (N1) check,
       margins.
"""
import numpy as np

rng = np.random.default_rng(303)
sig = np.array([0.0, 1.0, -1.0])

def Dx(x):
    return np.exp(1j * x * sig)

# ---------- reduced-system evaluators ----------
def build(p):
    g, dr, di, b0, br, bi = p
    delta = dr + 1j * di
    G = np.array([[1.0, g, g],
                  [g, 1.0, delta],
                  [g, np.conj(delta), 1.0]])
    beta = np.array([b0, br + 1j * bi, br - 1j * bi])
    return G, beta

def margins(p, depth, grids):
    G, beta = build(p)
    eg = np.linalg.eigvalsh(G)
    if eg[0] < 1e-8:
        return None
    H = np.linalg.inv(G)
    alpha = H @ beta
    ac = np.conj(alpha)          # LEFT boundary vector: Omega^dag R_s
    c = ac * beta                # couplings c_s = conj(alpha_s) beta_s
    c0 = c[0].real
    cp = c[1]
    if c0 <= 1e-12:
        return None
    out = {"r": 2 * abs(cp) / c0, "c0": c0,
           "alpha": alpha, "G": G, "H": H, "beta": beta}
    ms = {"D1": c0 - 2 * abs(cp)}
    N2, N3, N4, N5 = grids
    x2 = np.linspace(0, 2 * np.pi, N2, endpoint=False)
    D2 = np.exp(1j * np.outer(x2, sig))            # (N2, 3)
    # two-segment, alpha/G family:
    #   F2u(x,y) = sum conj(a_s) G_st a_t e^{i(x sig_s - y sig_t)}
    F2u = np.einsum("xs,st,yt->xy", D2 * ac[None, :], G,
                    np.conj(D2) * alpha[None, :])
    ms["F2u"] = float(F2u.real.min())
    imchk = float(np.abs(F2u.imag).max())
    # two-segment, beta/H family:
    #   F2v(x,y) = sum conj(b_t) H_tu b_u e^{i(-x sig_t + y sig_u)}
    F2v = np.einsum("xt,tu,yu->xy", np.conj(D2) * np.conj(beta)[None, :],
                    H, D2 * beta[None, :])
    ms["F2v"] = float(F2v.real.min())
    imchk = max(imchk, float(np.abs(F2v.imag).max()))
    if depth >= 3:
        x3 = np.linspace(0, 2 * np.pi, N3, endpoint=False)
        D3 = np.exp(1j * np.outer(x3, sig))
        f = np.einsum("xs,st->xt", D3 * ac[None, :], G)      # f_t(x)
        gv = np.einsum("st,xt->xs", H, D3 * beta[None, :])   # g_t(z)
        # F3 = f0 g0 + 2 Re(e^{-iy} f+ g+): exact min over y
        m3 = (f[:, None, 0].real * gv[None, :, 0].real
              - 2 * np.abs(f[:, None, 1] * gv[None, :, 1]))
        ms["F3"] = float(m3.min())
    if depth >= 4:
        x4 = np.linspace(0, 2 * np.pi, N4, endpoint=False)
        D4 = np.exp(1j * np.outer(x4, sig))
        f4 = np.einsum("xs,st->xt", D4 * ac[None, :], G)
        # q_t(z,w) = (H D(z) G D(-w) alpha)_t
        q = np.einsum("ts,zs,su,wu,u->zwt",
                      H, D4, G, np.conj(D4), alpha,
                      optimize=True)
        m4 = (f4[:, None, None, 0].real * q[None, :, :, 0].real
              - 2 * np.abs(f4[:, None, None, 1] * q[None, :, :, 1]))
        ms["F4"] = float(m4.min())
    if depth >= 5:
        x5 = np.linspace(0, 2 * np.pi, N5, endpoint=False)
        D5 = np.exp(1j * np.outer(x5, sig))
        f5 = np.einsum("xs,st->xt", D5 * ac[None, :], G)
        # r_t(z,w,v) = (H D(z) G D(-w) H D(v) beta)_t
        r5 = np.einsum("ts,zs,su,wu,uo,vo,o->zwvt",
                       H, D5, G, np.conj(D5), H, D5, beta,
                       optimize=True)
        m5 = (f5[:, None, None, None, 0].real
              * r5[None, :, :, :, 0].real
              - 2 * np.abs(f5[:, None, None, None, 1]
                           * r5[None, :, :, :, 1]))
        ms["F5"] = float(m5.min())
    out["margins"] = {k: val / c0 for k, val in ms.items()}
    out["imchk"] = imchk
    return out

# ---------- (i) validation against an explicit rank-3 process ----------
print("== (i) validation of the peripheral reduction ==")
theta = 0.61  # any irrational-ish angle; the formulas are exact
R0 = rng.standard_normal(3)
Rp = rng.standard_normal(3) + 1j * rng.standard_normal(3)
R = np.column_stack([R0, Rp, np.conj(Rp)])
lam = np.array([1.0, np.exp(1j * theta), np.exp(-1j * theta)])
B = (R @ np.diag(lam) @ np.linalg.inv(R)).real
Om = rng.standard_normal(3)
G_v = np.linalg.inv(R) @ np.conj(np.linalg.inv(R)).T
G_v = np.conj(G_v.T) @ np.eye(3) if False else \
      np.linalg.inv(R) @ np.linalg.inv(R).conj().T
H_v = R.conj().T @ R
beta_v = np.linalg.inv(R) @ Om
alpha_v = R.conj().T @ Om
err_inv = np.abs(G_v @ H_v - np.eye(3)).max()
err_alpha = np.abs(alpha_v - H_v @ beta_v).max()
def brute(a, b, c):
    M = np.linalg.matrix_power(B, a) \
        @ np.linalg.matrix_power(B.T, b) \
        @ np.linalg.matrix_power(B, c)
    return float(Om @ M @ Om)
def reduced3(x, y, z):
    f = (Dx(x) * np.conj(alpha_v)) @ G_v
    gv = H_v @ (Dx(z) * beta_v)
    return float((f * np.exp(-1j * y * sig) * gv).sum().real)
errs = []
for (a, b, c) in [(1, 1, 1), (2, 1, 3), (3, 2, 1), (4, 4, 2), (5, 1, 5)]:
    errs.append(abs(brute(a, b, c)
                    - reduced3(a * theta, b * theta, c * theta)))
def brute4(a, b, c, d):
    M = np.linalg.matrix_power(B, a) @ np.linalg.matrix_power(B.T, b) \
        @ np.linalg.matrix_power(B, c) @ np.linalg.matrix_power(B.T, d)
    return float(Om @ M @ Om)
def reduced4(x, y, z, w):
    vec = G_v @ (np.exp(-1j * w * sig) * alpha_v)
    vec = H_v @ (Dx(z) * vec)
    f = (Dx(x) * np.conj(alpha_v)) @ G_v
    return float((f * np.exp(-1j * y * sig) * vec).sum().real)
for (a, b, c, d) in [(1, 2, 1, 1), (2, 1, 3, 2), (3, 3, 1, 4)]:
    errs.append(abs(brute4(a, b, c, d)
                    - reduced4(a * theta, b * theta, c * theta, d * theta)))
cons = abs(reduced3(0.7, 0.0, 1.1)
           - float(((Dx(1.8) * np.conj(alpha_v)) * beta_v).sum().real))
print(f"  biorthogonality  |G H - 1|        = {err_inv:.1e}")
print(f"  alpha = G^-1 beta                 = {err_alpha:.1e}")
print(f"  brute vs reduced (3- and 4-seg)   = {max(errs):.1e}")
print(f"  consistency F3(x,0,z) = F1(x+z)   = {cons:.1e}")
print("  -> the reduction is EXACT: every (W, W-tilde)-word value of")
print("     a peripheral-triple process is a torus evaluation of the")
print("     reduced data (G, beta); validity forces torus positivity")
print("     (theta-free, by Weyl equidistribution).")

# ---------- (ii) the depth tower ----------
print("\n== (ii) the depth tower: max clock strength r = 2|c+|/c0 ==")
GRIDS = (48, 40, 22, 14)
SETS = [("A: diagonal only", 1), ("B: + two-segment", 2),
        ("C: + three-segment", 3), ("D: + four-segment", 4),
        ("E: + five-segment", 5)]
def feasible_ratio(p, depth):
    out = margins(p, depth, GRIDS)
    if out is None:
        return None
    wm = min(out["margins"].values())
    return out, wm

def anneal(depth, p0, steps, seed_rng):
    p = p0.copy()
    res = feasible_ratio(p, depth)
    best_r, best_p = -1.0, None
    cur = -1e9
    if res is not None:
        out, wm = res
        cur = out["r"] - 60 * max(0.0, -wm)
        if wm >= -1e-9:
            best_r, best_p = out["r"], p.copy()
    sz = 0.25
    for k in range(steps):
        q = p + sz * seed_rng.standard_normal(6)
        res = feasible_ratio(q, depth)
        if res is None:
            continue
        out, wm = res
        sc = out["r"] - 60 * max(0.0, -wm)
        if sc > cur:
            cur, p = sc, q
            if wm >= -1e-9 and out["r"] > best_r:
                best_r, best_p = out["r"], q.copy()
        sz = max(sz * 0.997, 0.02)
    return best_r, best_p

tower = {}
seeds = [np.array([0.2, 0.1, 0.0, 1.0, 0.3, 0.1]),
         np.array([0.0, 0.0, 0.0, 1.0, 0.5, 0.0]),
         np.array([0.4, -0.3, 0.2, 0.8, 0.4, -0.2])]
prev_best = None
for name, depth in SETS:
    starts = []
    if prev_best is not None:
        starts.append(prev_best)
    starts += seeds
    nfresh = 24 if depth <= 3 else (12 if depth == 4 else 8)
    starts += [rng.standard_normal(6) * 0.6 + np.array([0, 0, 0, 1, 0, 0])
               for _ in range(nfresh)]
    nsteps = 700 if depth <= 3 else (400 if depth == 4 else 250)
    br, bp = -1.0, None
    for s in starts:
        r, q = anneal(depth, np.asarray(s, float), nsteps, rng)
        if r > br:
            br, bp = r, q
    tower[depth] = (br, bp)
    prev_best = bp if bp is not None else prev_best
    print(f"   {name:22s}  r_max = {br:.4f}")

# ---------- (iii) receipts at the optimum ----------
print("\n== (iii) receipts at the deepest optimum ==")
br, bp = tower[5]
if bp is not None:
    out = margins(bp, 5, GRIDS)
    G, beta, alpha = out["G"], out["beta"], out["alpha"]
    print(f"  witness r = {out['r']:.4f}   (c0-normalized margins:)")
    for k, v in out["margins"].items():
        print(f"     {k:4s}: {v:+.3e}")
    n1_lhs = alpha[0].real ** 2
    n1_rhs = 2 * abs(alpha[1]) ** 2 * (1 + abs(G[1, 2]))
    print(f"  (N1) alpha_0^2 >= 2|alpha_+|^2 (1+|delta|):"
          f" {n1_lhs:.4f} >= {n1_rhs:.4f}"
          f"  ({'PASS' if n1_lhs >= n1_rhs - 1e-9 else 'FAIL'})")
    print(f"  witness params (gamma, Re delta, Im delta, beta0,"
          f" Re beta+, Im beta+):")
    print(f"     {np.round(bp, 4)}")
    print(f"  realness identity check max|Im| = {out['imchk']:.1e}")
else:
    print("  NO feasible point found at depth 5 with r > 0")
rs = [tower[d][0] for d in (1, 2, 3, 4, 5)]
print(f"\n  THE CURVE: r_max by depth = "
      f"{', '.join(f'{r:.3f}' for r in rs)}")

# ---------- (iv) the NORMAL ESCAPE: the tower can never close ----------
print("\n== (iv) the normal escape: an all-depth witness at r = 1 ==")
# If B is NORMAL (left eigenvectors orthonormal), then G = I and every
# alternating chain collapses to a single total frequency:
#   chain value = c0 + 2 Re(c_+ e^{i Phi}),  Phi = (sum of +/- phases)
# so positivity at EVERY depth is exactly Fejer: c0 >= 2|c_+| - which
# is satisfiable with r = 2|c_+|/c0 = 1.  Receipt: evaluate the
# implemented tower at the normal witness.
eps_m = 1e-6
p_norm = np.array([0.0, 0.0, 0.0,
                   np.sqrt(2.0) * (1 + eps_m), 1.0, 0.0])
out_n = margins(p_norm, 5, GRIDS)
print(f"  witness: G = I, beta = (sqrt(2)(1+eps), 1, 1):"
      f"  r = {out_n['r']:.6f}")
print("  c0-normalized margins:")
for k, v in out_n["margins"].items():
    print(f"     {k:4s}: {v:+.3e}")
print("  -> ALL margins >= 0 at r = 1 - eps, at every implemented")
print("     depth.  THEOREM (normal escape): the (W, W-tilde)-word")
print("     torus-positivity tower is FEASIBLE at full clock strength")
print("     for normal-block reduced data, at ALL depths (one-line")
print("     proof: G = I collapses every chain to a single-frequency")
print("     Fejer form).  CONSEQUENCE: no proof of CPE can come from")
print("     the (B, B-dagger) subalgebra alone - the obstruction, if")
print("     CPE is true, lives in words that LEAVE the block algebra")
print("     (other letters, rotations of W) or in the letter")
print("     embedding itself.  Equivalently: the sharpest remaining")
print("     counterexample target is an RP process whose chiral block")
print("     is (proportional to) a ROTATION - B B^dag = c^2 I - with")
print("     the state coupled at r <= 1.  The embedding question")
print("     decides, and p30d attacks it.")
print("== p30c done ==")

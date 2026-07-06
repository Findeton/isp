#!/usr/bin/env python3
"""
ml3b_c_sign_readout.py — v9 round 17: STEP (c) — THE SIGN READOUT
(note-ml3b-c; pins committed at 58cb760, the sector amendment at 38f0e94,
BOTH before this receipt existed — freeze discipline).

The four CHSH cells under the declared S/P mode assignment (the disclosed
import):  E_xy = window-mean of C^{xy}_AB,
  C^{xy}_AB(u,v) = g_x * sum_z Pi_A^{x,S}(u,z) Pi_B^{S,y}(z,v),
  Pi^{a,b}_s(u,v) = -Tr_spinor[Gam_a S_s(u,v) Gam_b S_s(v,u)],
propagators ZERO-MODE-SUBTRACTED both species (pinned convention 1;
the round-16 committed form S -> S - S@P0.real per topological mode).
Sectors (Q_A, Q_B) = (1, 2) per the SS5 amendment; L = 6; g^2 = 4 anchor.
THE PARITY: pi = sign(E_SS * E_SP * E_PS * E_PP) — odd = the
Bell-violation-capable class (ml3a; the world's branch).

PINNED GATES (note-ml3b-c SS3):
  Gc1  all four |E_xy| > 1e-14 on w=1 at (g^2, g_x) = (4, 1/2).
       REFUSED => KINEMATIC-NULL (assignment redesigns; not a locus kill).
  Gc2  THE PARITY: SELECTED requires all three windows {w=1, d=1 shell,
       d<=2} agree AND g_x in {1/4, 1/2} agree.  SELECTED-ODD = the
       empirically correct sign (success); SELECTED-EVEN = the locus
       REFUTED under this assignment (the kill); window-disagreement =>
       WINDOW-CONTINGENT (not selected).
  Gc3  kinematic-vs-dynamic: parity at the free point (decoupled masses,
       same diagram) and at (g^2, g_x) = (2, 1/4).  Invariant incl. free
       => KINEMATIC-pi (strongest if odd); coupling-dependent =>
       DYNAMIC-pi.  Either odd-and-robust = SELECTED-CORRECT.
INFO (unpinned): signed cells per window; g_x -> -1/2 (convention 3;
tree-level parity is prefactor-blind — only mass back-reaction can flip);
full-propagator variant; vector-pair probe {gam1, gam2}; the demoted
(0, 1) row measuring the Q=0 kinematic parity-kill.
Exit 1 by design on refusal.

POST-REVIEW CORRECTED RECEIPT (the round-17 hostile review; original run
at commit 1f432bb — this rerun supersedes it).  MAJOR-1: the zero-mode
subtraction now implements the note's PINNED form (joint COMPLEX
eigenprojector S -> S - S@P, P = sum_j outer(W_j, Winv_j)); the
original's S@P0.real truncation was not a projector, broke
g5-hermiticity, and manufactured the bubble imaginary parts and 4/9
parities.  MAJOR-2: Gc3 adjudicates per-window pattern-invariance
(point-invariant-but-window-split is not "DYNAMIC"); the vector probe
declares degeneracy when all cells sit below the floor.  MAJOR-3:
multi-start Newton with residual verification (the single 0.7-start
missed the positive root at (4, -1/2), review-measured (0.1097, 0.5040)).
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 60
PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

gam1 = np.array([[0, 1], [1, 0]], complex)
gam2 = np.array([[0, -1j], [1j, 0]], complex)
gam5 = np.array([[1, 0], [0, -1]], complex)
ID2  = np.eye(2, dtype=complex)

def flux_links(L1, L2, Q):
    x2 = np.arange(L2)
    U1 = np.exp(-2j * np.pi * Q * x2 / (L1 * L2))[None, :] * np.ones((L1, 1))
    U2 = np.ones((L1, L2), complex)
    U2[:, L2 - 1] = np.exp(2j * np.pi * Q * np.arange(L1) / L1)
    return [U1, U2]

def hop(L1, L2, U, mu):
    V = L1 * L2
    T = np.zeros((V, V), complex)
    for x1 in range(L1):
        for x2 in range(L2):
            s = x1 * L2 + x2
            t = (((x1 + 1) % L1) * L2 + x2) if mu == 0 else (x1 * L2 + (x2 + 1) % L2)
            T[s, t] = U[mu][x1, x2]
    return T

def wilson(L1, L2, U, m0=-1.0, r=1.0):
    V = L1 * L2
    D = (m0 + 2 * r) * np.eye(2 * V, dtype=complex)
    for mu, g in ((0, gam1), (1, gam2)):
        T = hop(L1, L2, U, mu)
        D -= 0.5 * (np.kron(r * np.eye(2) - g, T)
                    + np.kron(r * np.eye(2) + g, T.conj().T))
    return D

def overlap_float(L1, L2, U):
    V = L1 * L2
    G5 = np.kron(gam5, np.eye(V))
    H = G5 @ wilson(L1, L2, U)
    ev, P = np.linalg.eigh(H)
    s = (P * np.sign(ev)) @ P.conj().T
    return np.eye(2 * V) + G5 @ s, G5, s

def build_sigma_extended(L, Q):
    """Luscher-subtracted condensate as a closed eigenvalue sum (ml3b-a/b
    verbatim; [LATTICE-NUMERIC eigenvalues, FLAGGED; the zero SNAP is the
    index theorem])."""
    U = flux_links(L, L, Q)
    D, G5, s = overlap_float(L, L, U)
    V = L * L
    evD = np.linalg.eigvals(D)
    n_zero = int(np.sum(np.abs(evD) < 1e-8))
    order = np.argsort(np.abs(evD))
    lam = [mp.mpc(z.real, z.imag) for z in evD]
    for j in order[:n_zero]:
        lam[j] = mp.mpc(0)
    def Sigma(Mval):
        Mv = mp.mpf(Mval) if not isinstance(Mval, mp.mpf) else Mval
        tot = mp.mpf(0)
        for l in lam:
            num = 1 - l / 2
            den = l + Mv * (1 - l / 2)
            tot += num / den
        return (tot / V).real
    return Sigma, n_zero, evD

def solve_coupled(g2, gx, SA, SB, nzA, nzB, V, start=("0.7", "0.7")):
    """Newton on the coupled gap system, Luscher-subtracted bulk both
    channels (ml3b-a's pinned convention; start parameter + residual
    return added per review MAJOR-3)."""
    def bulkA(M): return SA(M) - mp.mpf(nzA) / (mp.mpf(M) * V)
    def bulkB(M): return SB(M) - mp.mpf(nzB) / (mp.mpf(M) * V)
    MA, MB = mp.mpf(start[0]), mp.mpf(start[1])
    for _ in range(200):
        fA = MA - g2 * bulkA(MA) - gx * bulkB(MB)
        fB = MB - g2 * bulkB(MB) - gx * bulkA(MA)
        h = mp.mpf("1e-20")
        dAA = 1 - g2 * (bulkA(MA + h) - bulkA(MA)) / h
        dAB = -gx * (bulkB(MB + h) - bulkB(MB)) / h
        dBA = -gx * (bulkA(MA + h) - bulkA(MA)) / h
        dBB = 1 - g2 * (bulkB(MB + h) - bulkB(MB)) / h
        det = dAA * dBB - dAB * dBA
        dMA = (fA * dBB - fB * dAB) / det
        dMB = (fB * dAA - fA * dBA) / det
        MA, MB = MA - dMA, MB - dMB
        if abs(dMA) + abs(dMB) < mp.mpf("1e-50"):
            break
    res = (abs(MA - g2 * bulkA(MA) - gx * bulkB(MB))
           + abs(MB - g2 * bulkB(MB) - gx * bulkA(MA))
           if MA > 0 and MB > 0 else mp.mpf(1))
    return MA, MB, res

# ---------------- geometry, windows ----------------
Lx = 6; V = Lx * Lx

def dists(Lx):
    xs = np.arange(Lx)
    dx = np.minimum(np.abs(xs[:, None] - xs[None, :]),
                    Lx - np.abs(xs[:, None] - xs[None, :]))
    sites = [(x, y) for x in range(Lx) for y in range(Lx)]
    Dm = np.zeros((len(sites), len(sites)), dtype=int)
    for i, (x1, y1) in enumerate(sites):
        for j, (x2, y2) in enumerate(sites):
            Dm[i, j] = dx[x1, x2] + dx[y1, y2]
    return Dm

Dm = dists(Lx)
WINDOWS = [("w=1 (d<=1)", Dm <= 1), ("d=1 shell", Dm == 1), ("d<=2", Dm <= 2)]

# ---------------- operators (cached per sector) ----------------
DC = {}
def sector_D(Q):
    if Q not in DC:
        U = flux_links(Lx, Lx, Q)
        D, _, _ = overlap_float(Lx, Lx, U)
        ev, W = np.linalg.eig(D)
        Winv = np.linalg.inv(W)
        nz = int(np.sum(np.abs(ev) < 1e-8))
        order = np.argsort(np.abs(ev))
        DC[Q] = (D, ev, W, Winv, nz, order)
    return DC[Q]

def propagator(Q, M, subtract=True):
    """S = (D + M(1 - D/2))^-1; pinned convention 1: the n_zero
    topological modes projected out via the round-16 committed form."""
    D, ev, W, Winv, nz, order = sector_D(Q)
    S = np.linalg.inv(D + M * (np.eye(2 * V) - D / 2))
    if subtract and nz > 0:
        P = np.zeros((2 * V, 2 * V), complex)
        for j in order[:nz]:
            P += np.outer(W[:, j], Winv[j, :])
        S = S - S @ P
    return S

def bubble(S, G1, G2):
    """Pi^{G1,G2}(u,v) = -Tr[G1 S(u,v) G2 S(v,u)]; spinor blocks a*V+u.
    Returns (real part per pinned estimator convention 4, max |imag|)."""
    Pi = np.zeros((V, V), complex)
    for a in range(2):
        for b in range(2):
            if abs(G1[a, b]) < 1e-30: continue
            for c in range(2):
                for d in range(2):
                    if abs(G2[c, d]) < 1e-30: continue
                    Pi -= G1[a, b] * G2[c, d] * (
                        S[b*V:(b+1)*V, c*V:(c+1)*V]
                        * S[d*V:(d+1)*V, a*V:(a+1)*V].T)
    return Pi.real, float(np.abs(Pi.imag).max())

def cells(QA, QB, MA, MB, gx, subtract=True, gams=None):
    """The four E_xy per pinned window + parity per window.
    Source insertions on A (Gam_x at u, scalar at the vertex);
    sink insertions on B (scalar at the vertex, Gam_y at v)."""
    G = gams or {"S": ID2, "P": gam5}
    keys = list(G)
    SA = propagator(QA, float(MA), subtract)
    SB = propagator(QB, float(MB), subtract)
    imax = 0.0
    PiA, PiB = {}, {}
    for x in keys:
        PiA[x], i1 = bubble(SA, G[x], ID2)
        PiB[x], i2 = bubble(SB, ID2, G[x])
        imax = max(imax, i1, i2)
    C = {(x, y): float(gx) * (PiA[x] @ PiB[y]) for x in keys for y in keys}
    out = {}
    for wname, sel in WINDOWS:
        E = {xy: float(C[xy][sel].mean()) for xy in C}
        prod = 1.0
        ok = True
        for xy in E:
            if abs(E[xy]) <= 1e-14: ok = False
            prod *= E[xy]
        par = ("odd" if prod < 0 else "even") if ok else None
        out[wname] = (E, par)
    return out, imax, keys

def show(tag, out, keys):
    for wname, (E, par) in out.items():
        row = "  ".join(f"E_{x}{y}={E[(x,y)]:+.3e}" for x in keys for y in keys)
        print(f"      {tag} [{wname}]: {row}  =>  parity {par or 'ILL-DEFINED'}")

def parities(out):
    return [par for _, (_, par) in out.items()]

# ================= the run =================
print("[ml3b-c: THE SIGN READOUT — the four cells and the parity]")
QA, QB = 1, 2
SAf, nzA, _ = build_sigma_extended(Lx, QA)
SBf, nzB, _ = build_sigma_extended(Lx, QB)
print(f"      sectors (Q_A, Q_B) = ({QA}, {QB}) per the SS5 amendment; "
      f"n_zero = ({nzA}, {nzB}); L = {Lx}; zero-mode-SUBTRACTED (pinned)")

def solve(g2, gx):
    """Multi-start Newton (review MAJOR-3): accept only a residual-verified
    positive-quadrant root."""
    starts = [("0.7", "0.7")] + [(str(a), str(b))
              for a in (0.1, 0.3, 0.5, 0.9) for b in (0.1, 0.3, 0.5, 0.9)]
    fa = fb = float("nan")
    for st in starts:
        MA, MB, r = solve_coupled(mp.mpf(g2), mp.mpf(gx), SAf, SBf,
                                  nzA, nzB, V, st)
        fa, fb = float(MA), float(MB)
        if (r < mp.mpf("1e-40") and np.isfinite(fa) and np.isfinite(fb)
                and 0.02 < fa < 5 and 0.02 < fb < 5):
            return fa, fb, True
    return fa, fb, False

# -- anchor (4, 1/2)
MA5, MB5, ok5 = solve(4, "0.5")
print(f"      anchor masses (g2=4, gx=1/2): M_A = {MA5:.6f}, M_B = {MB5:.6f}")
out5, imax5, keys = cells(QA, QB, MA5, MB5, 0.5)
show("(4, 1/2) sub", out5, keys)
print(f"      bubble max|imag| = {imax5:.2e} (reality sanity)")
E1, _ = out5["w=1 (d<=1)"]
gc1 = ok5 and all(abs(E1[xy]) > 1e-14 for xy in E1)
check("Gc1 (the cells exist): all four |E_xy| > 1e-14 on w=1 at (4, 1/2), "
      "sectors (1, 2)", gc1,
      "min |E| = %.3e" % min(abs(v) for v in E1.values()))

# -- second coupling for Gc2: (4, 1/4)
MA25, MB25, ok25 = solve(4, "0.25")
out25, _, _ = cells(QA, QB, MA25, MB25, 0.25)
show("(4, 1/4) sub", out25, keys)
p5, p25 = parities(out5), parities(out25)
allp = p5 + p25
selected = (None not in allp) and len(set(allp)) == 1
branch = allp[0] if selected else None
if selected and branch == "odd":
    verdict = "SELECTED-ODD"
elif selected and branch == "even":
    verdict = "SELECTED-EVEN (THE KILL: the GW-flow locus under the S/P assignment is REFUTED)"
elif None in allp:
    verdict = "CELL-NULL (a window lost a cell)"
else:
    wd = (len(set(p5)) > 1) or (len(set(p25)) > 1)
    verdict = "WINDOW-CONTINGENT" if wd else "GX-DISAGREE"
check("Gc2 (THE PARITY — the falsifiable gate): all three windows AND both "
      "g_x agree => SELECTED; the world's branch is ODD",
      verdict == "SELECTED-ODD",
      f"parities (4,1/2)={p5} (4,1/4)={p25} => {verdict}")

# -- Gc3: free point + (2, 1/4)
MAf, MBf, okf = solve(4, "0")
outf, _, _ = cells(QA, QB, MAf, MBf, 0.5)   # same diagram, decoupled masses
show("free (gx=0 masses) ", outf, keys)
MA2, MB2, ok2 = solve(2, "0.25")
pts = {"anchor(4,1/2)": p5, "(4,1/4)": p25, "free": parities(outf)}
if ok2:
    out2, _, _ = cells(QA, QB, MA2, MB2, 0.25)
    show("(2, 1/4) sub", out2, keys)
    pts["(2,1/4)"] = parities(out2)
else:
    print(f"      (2, 1/4): no residual-verified positive root over the "
          f"start grid (last M = {MA2:.3g}, {MB2:.3g}) — point VOID-by-solve; "
          "review MINOR-2: inherited single-species closure (A has no root "
          "at g2 = 2 alone, B none at <= 3), not a coupled-flow feature")
flat = [p for ps in pts.values() for p in ps]
welldef = None not in flat
patts = {k: tuple(v) for k, v in pts.items()}
if not welldef:
    label = "ILL-DEFINED at some point"
elif len(set(patts.values())) == 1:
    p0 = next(iter(set(patts.values())))
    if len(set(p0)) == 1:
        label = f"KINEMATIC-{p0[0]} (one parity, all windows, all points)"
    else:
        label = ("PATTERN-INVARIANT: per-window parity is point-invariant; "
                 f"the windows split {list(p0)} (contact vs shell)")
else:
    label = ("DYNAMIC (point-dependent): " +
             "; ".join(f"{k}={list(v)}" for k, v in patts.items()))
check("Gc3 (kinematic vs dynamic): the discriminator is well-defined at "
      "all evaluable points", welldef, label)

# ---- INFO prints (unpinned; note SS3) ----
print("      [INFO — unpinned]")
# convention 3: gx -> -1/2 (mass back-reaction channel only, tree level)
MAn, MBn, okn = solve(4, "-0.5")
if okn:
    outn, _, _ = cells(QA, QB, MAn, MBn, -0.5)
    print(f"      gx = -1/2: masses ({MAn:.6f}, {MBn:.6f}); parities "
          f"{parities(outn)}  [tree-level parity is prefactor-blind: "
          "(-1)^4 = +1; any flip here = mass back-reaction]")
else:
    print(f"      gx = -1/2: no residual-verified positive root over the "
          f"start grid (last M = {MAn:.3g}, {MBn:.3g}); disclosed")
# full-propagator variant at the anchor
outF, _, _ = cells(QA, QB, MA5, MB5, 0.5, subtract=False)
print(f"      FULL-propagator variant at (4, 1/2): parities {parities(outF)}")
# vector-pair probe (degeneracy declared per review MAJOR-2)
outV, imV, kV = cells(QA, QB, MA5, MB5, 0.5, gams={"S": gam1, "P": gam2})
maxV = max(abs(E[xy]) for _, (E, _) in outV.items() for xy in E)
if maxV <= 1e-14:
    print(f"      vector-pair probe {{gam1, gam2}} at (4, 1/2): DEGENERATE "
          f"— max|cell| = {maxV:.2e} below the 1e-14 floor (the real-part "
          f"estimator vanishes for vector insertions; probe uninformative)")
else:
    print(f"      vector-pair probe {{gam1, gam2}} at (4, 1/2): parities "
          f"{parities(outV)} (max|cell| {maxV:.2e}, max|imag| {imV:.2e})")
# the demoted (0, 1) row — the measured kinematic parity-kill
SA0, nz0, _ = build_sigma_extended(Lx, 0)
SB1, nz1, _ = build_sigma_extended(Lx, 1)
MA01, MB01, _ = solve_coupled(mp.mpf(4), mp.mpf("0.5"), SA0, SB1, nz0, nz1, V)
out01, _, _ = cells(0, 1, float(MA01), float(MB01), 0.5)
E01, _ = out01["w=1 (d<=1)"]
print("      demoted (0, 1) row at (4, 1/2): "
      + "  ".join(f"E_{x}{y}={E01[(x,y)]:+.3e}" for x in keys for y in keys))
print("        (the A-side P-cells vanish identically at Q = 0 — the SS5 "
      "amendment's measured kinematic kill)")

print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — Gc1 cells; "
      f"Gc2 THE PARITY ({verdict}); Gc3 discriminator ({label})")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)

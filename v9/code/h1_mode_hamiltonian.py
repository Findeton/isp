#!/usr/bin/env python3
"""
h1_mode_hamiltonian.py — v9 round 22: THE HAMILTONIAN ROUTE'S ONE SHOT
(note-h1; pin committed at 165ca47 strictly before this receipt).

The orbit-splitting reduction (note SS2, derived): gauge invariance on the
ml3a manifold makes PI E_xy the FIRST orbit discriminator; equal
magnitudes are forced, so the two orbits differ only through the quartic
term, whose coefficient is -cum4 of the four global cell charges
q_xy = sum_z O^A_x(z) O^B_y(z); Gamma-minimization then selects
  cum4 > 0 => EVEN;  cum4 < 0 => ODD.
Pinned object: kappa_box = the box-x-box topology of cum4 — both species'
closed 4-insertion loops sharing all four seal sites, ALL 6 x 6 cyclic
orderings (loop signs cancel, (+1)); legs K = (1 - D/2) S at the FULL
propagator (the standing principled content); one exact number per point.

PINNED (note-h1 SS4):
  Gh1  wiring: L = 3 brute-force Wick (explicit site loops, independent
       code path) vs the einsum network, relative < 1e-10.
  Gh2  |kappa_box| > 1e-14 at all six points {L 6,8,10} x {gx 1/4,1/2}.
  Gh3  THE SELECTION (one shot): sign(kappa_box) unanimous over the six
       points => SELECTED-ODD-H (kappa < 0) / SELECTED-EVEN-H
       (kappa > 0); any split => FAILS-AT-H-LEADING.
INFO: per-point kappa; aligned (sigma = tau) share; imag sanity; the
gx = 0 decoupled row.  Exit 1 by design on refusal.
"""
import itertools
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

def K_legs(L, Q, M):
    """Improved leg K = (1 - D/2) S, FULL propagator, as (2, V, 2, V)."""
    U = flux_links(L, L, Q)
    D, _, _ = overlap_float(L, L, U)
    V = L * L
    S = np.linalg.inv(D + M * (np.eye(2 * V) - D / 2))
    K = (np.eye(2 * V) - D / 2) @ S
    return K.reshape(2, V, 2, V)

# cell labels 0..3 = (SS, SP, PS, PP); A-side gammas by x, B-side by y
GA = [ID2, ID2, gam5, gam5]
GB = [ID2, gam5, ID2, gam5]
ORDS = [(0,) + p for p in itertools.permutations((1, 2, 3))]  # 6 necklaces
SLET = {1: "x", 2: "y", 3: "z"}          # site letters (label 0 batched)

def gk(Ka, G):
    """GK[l] = Gamma_l . K in spinor space, per insertion label."""
    return [np.einsum("st,tzuw->szuw", G[l], Ka) for l in range(4)]

def cycle_tensor(GK, perm, z0, spins):
    """Einsum operands+subscripts for one species' cycle at fixed z0
    (site label 0 sliced); returns (ops, sublist) with output 'xyz'."""
    ops, subs = [], []
    for k in range(4):
        lbl, nxt = perm[k], perm[(k + 1) % 4]
        T = GK[lbl]
        sub = [spins[k], None, spins[(k + 1) % 4], None]
        if lbl == 0:
            T = T[:, z0]
            sub = [sub[0], sub[2], None]
            sub[2] = SLET[nxt] if nxt != 0 else None
        else:
            sub[1] = SLET[lbl]
            if nxt == 0:
                T = T[:, :, :, z0]
                sub = sub[:3]
            else:
                sub[3] = SLET[nxt]
        ops.append(T)
        subs.append("".join(s for s in sub if s))
    return ops, subs

def kappa_box(L, KaA, KaB):
    """All 36 ordering pairs, batched over the site-0 position."""
    V = L * L
    GKA, GKB = gk(KaA, GA), gk(KaB, GB)
    tot = 0.0 + 0.0j
    aligned = 0.0 + 0.0j
    for z0 in range(V):
        A3 = {}
        B3 = {}
        for perm in ORDS:
            opsA, subA = cycle_tensor(GKA, perm, z0, "abcd")
            A3[perm] = np.einsum(",".join(subA) + "->xyz", *opsA, optimize=True)
            opsB, subB = cycle_tensor(GKB, perm, z0, "ijkl")
            B3[perm] = np.einsum(",".join(subB) + "->xyz", *opsB, optimize=True)
        for sA in ORDS:
            for sB in ORDS:
                v = np.einsum("xyz,xyz->", A3[sA], B3[sB])
                tot += v
                if sA == sB:
                    aligned += v
    return tot, aligned

def kappa_brute(L, KaA, KaB):
    """Independent code path: explicit site loops, python 2x2 chains."""
    V = L * L
    tot = 0.0 + 0.0j
    for zt in itertools.product(range(V), repeat=4):
        trA = {}
        trB = {}
        for perm in ORDS:
            m = np.eye(2, dtype=complex)
            for k in range(4):
                lbl, nxt = perm[k], perm[(k + 1) % 4]
                m = m @ GA[lbl] @ KaA[:, zt[lbl], :, zt[nxt]]
            trA[perm] = np.trace(m)
            m = np.eye(2, dtype=complex)
            for k in range(4):
                lbl, nxt = perm[k], perm[(k + 1) % 4]
                m = m @ GB[lbl] @ KaB[:, zt[lbl], :, zt[nxt]]
            trB[perm] = np.trace(m)
        tot += sum(trA[a] * trB[b] for a in ORDS for b in ORDS)
    return tot

print("[h1: THE HAMILTONIAN ROUTE — sign(kappa_box) selects the orbit]")
QA, QB = 1, 2
SIG = {}
def masses(L, gx):
    if L not in SIG:
        SIG[L] = (build_sigma_extended(L, QA), build_sigma_extended(L, QB))
    (SA, nzA, _), (SB, nzB, _) = SIG[L]
    V = L * L
    starts = [("0.7", "0.7")] + [(str(a), str(b))
              for a in (0.1, 0.3, 0.5, 0.9) for b in (0.1, 0.3, 0.5, 0.9)]
    for st in starts:
        MA, MB, r = solve_coupled(mp.mpf(4), mp.mpf(gx), SA, SB, nzA, nzB, V, st)
        fa, fb = float(MA), float(MB)
        if r < mp.mpf("1e-40") and 0.02 < fa < 5 and 0.02 < fb < 5:
            return fa, fb
    raise SystemExit(f"no root at L={L} gx={gx}")

# Gh1: wiring at L = 3
MA3, MB3 = masses(3, "0.5")
Ka3A, Ka3B = K_legs(3, QA, MA3), K_legs(3, QB, MB3)
kb_net, _ = kappa_box(3, Ka3A, Ka3B)
kb_bru = kappa_brute(3, Ka3A, Ka3B)
rel = abs(kb_net - kb_bru) / max(abs(kb_bru), 1e-300)
check("Gh1 (wiring): L = 3 einsum network vs independent brute-force "
      "Wick, relative < 1e-10", rel < 1e-10,
      f"net {kb_net:.6e}, brute {kb_bru:.6e}, rel {rel:.2e}")

# the grid
results = {}
for L in (6, 8, 10):
    for gxs in ("0.5", "0.25"):
        MA, MB = masses(L, gxs)
        KaA, KaB = K_legs(L, QA, MA), K_legs(L, QB, MB)
        kb, al = kappa_box(L, KaA, KaB)
        results[(L, gxs)] = (kb, al)
        print(f"      L={L} gx={gxs}: masses {MA:.6f}/{MB:.6f}; "
              f"kappa_box = {kb.real:+.6e} (imag {abs(kb.imag):.1e}; "
              f"aligned share {al.real/kb.real if abs(kb.real)>0 else 0:+.3f})")

gh2 = all(abs(kb.real) > 1e-14 for kb, _ in results.values())
check("Gh2 (existence): |kappa_box| > 1e-14 at all six grid points", gh2,
      "min |kappa| = %.3e" % min(abs(kb.real) for kb, _ in results.values()))

signs = [np.sign(kb.real) for kb, _ in results.values()]
if gh2 and len(set(signs)) == 1:
    verdict = ("SELECTED-ODD-H (kappa < 0: Gamma-minimization selects "
               "PI E < 0 — the Bell-capable orbit)" if signs[0] < 0 else
               "SELECTED-EVEN-H (kappa > 0: the even orbit — the locus "
               "refuted at the Hamiltonian object)")
else:
    verdict = "SIGN-SPLIT — FAILS-AT-H-LEADING"
check("Gh3 (THE SELECTION — this route's one shot): sign(kappa_box) "
      "unanimous over {L 6,8,10} x {gx 1/4,1/2}; ODD <=> kappa < 0",
      gh2 and len(set(signs)) == 1 and signs[0] < 0,
      f"signs {[f'{int(s):+d}' for s in signs]} => {verdict}")

# INFO: gx = 0 decoupled row
MA0, MB0 = masses(6, "0")
K0A, K0B = K_legs(6, QA, MA0), K_legs(6, QB, MB0)
kb0, _ = kappa_box(6, K0A, K0B)
print(f"      INFO gx = 0 (L = 6, decoupled masses {MA0:.6f}/{MB0:.6f}): "
      f"kappa_box = {kb0.real:+.6e}")

print()
print(f"PRE-REGISTERED GATE LEDGER: "
      f"{'ALL HELD' if FAIL == 0 else 'REFUSALS PRESENT'} — Gh1 wiring; "
      f"Gh2 existence; Gh3 ({verdict})")
print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total})" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)

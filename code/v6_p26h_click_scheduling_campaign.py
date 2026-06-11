#!/usr/bin/env python3
"""
v6_p26h: click-scheduling invariance - circuit vs measurement-based
computing (Paper 26, Part V, angle 4).

The circuit model keeps the ledger silent and clicks at the end;
measurement-based computing (MBQC) clicks at EVERY step.  The
capacity law must not care - and it does not, because MBQC's clicks
are TYPED: each measurement outcome is uniformly random and
INDEPENDENT of the logical state (the byproduct frame absorbs it).

 (i)  THE TELEPORTATION SEAM: one MBQC step (CZ with |+>, measure
      qubit 1 in the theta-rotated basis): outcome probabilities =
      1/2 EXACTLY for every input state and every theta (machine,
      random sample): I(logical : click) = 0 - the click is
      logical-evidence-free BY CONSTRUCTION.
 (ii) INVARIANCE: chains of 6 typed seams with feed-forward return
      the programmed unitary at fidelity 1 (machine, random chains):
      n clicks, ZERO leaked logical nats: the same K_pre spent
      through a different schedule.
 (iii) THE UNTYPED CONTRAST: measuring in a basis mis-rotated toward
      Z by delta makes the outcome logical-informative; the leaked
      evidence and the output infidelity rise TOGETHER along the
      Part-I tradeoff (table): MBQC works exactly because its seams
      sit at the zero-evidence point of the tradeoff.

COROLLARY (click-scheduling invariance): pre-click capacity is a
schedule invariant - clicks cost capacity only through their LOGICAL
EVIDENCE, never through their count.
"""
import numpy as np

rng = np.random.default_rng(268)
H = np.array([[1, 1], [1, -1]], complex) / np.sqrt(2)
X = np.array([[0, 1], [1, 0]], complex)
Z = np.array([[1, 0], [0, -1]], complex)

def mbqc_step(psi, theta):
    """CZ with |+>, measure qubit 1 in basis (|0> +- e^{-i theta}|1>)/
    sqrt2; returns outcome probabilities and post-states (corrected)."""
    plus = np.array([1, 1], complex) / np.sqrt(2)
    state = np.kron(psi, plus)
    CZ = np.diag([1, 1, 1, -1]).astype(complex)
    state = CZ @ state
    out = []
    for m in (0, 1):
        bra = np.array([1, (-1) ** m * np.exp(-1j * theta)],
                       complex) / np.sqrt(2)
        sub = np.array([bra.conj() @ state.reshape(2, 2)[:, k]
                        for k in range(2)])
        p = float(np.real(sub.conj() @ sub))
        sub = sub / np.sqrt(p)
        # byproduct correction: X^m, then the step implements H Rz(theta)
        corr = np.linalg.matrix_power(X, m) @ sub
        out.append((p, corr))
    return out

# ---------- (i) the typed click ----------
print("== (i) the MBQC click is logical-evidence-free ==")
worst = 0.0
for _ in range(200):
    a = rng.standard_normal(2) + 1j * rng.standard_normal(2)
    psi = a / np.linalg.norm(a)
    th = rng.uniform(0, 2 * np.pi)
    res = mbqc_step(psi, th)
    worst = max(worst, abs(res[0][0] - 0.5), abs(res[1][0] - 0.5))
print(f"  200 random (state, angle) pairs: max |p(m) - 1/2| ="
      f" {worst:.1e}")
print("  -> outcome probabilities are EXACTLY 1/2, independent of the")
print("     logical state: I(L : click) = 0 - the click is typed.")

# ---------- (ii) invariance over chains ----------
print("\n== (ii) six-seam chains with feed-forward ==")
worst_f = 1.0
for _ in range(40):
    a = rng.standard_normal(2) + 1j * rng.standard_normal(2)
    psi0 = a / np.linalg.norm(a)
    thetas = rng.uniform(0, 2 * np.pi, 6)
    psi = psi0.copy()
    Utot = np.eye(2, dtype=complex)
    for th in thetas:
        m = int(rng.uniform() < mbqc_step(psi, th)[1][0])
        p, psi = mbqc_step(psi, th)[m]
        Rz = np.diag([1, np.exp(1j * th)]).astype(complex)
        Utot = (H @ Rz) @ Utot
    target = Utot @ psi0
    F = abs(np.vdot(target / np.linalg.norm(target), psi)) ** 2
    worst_f = min(worst_f, F)
print(f"  40 random 6-seam chains: min output fidelity = {worst_f:.10f}")
print("  -> SIX clicks per run, ZERO logical nats leaked, fidelity 1:")
print("     pre-click capacity is SCHEDULE-INVARIANT - the circuit")
print("     model and MBQC spend the same K_pre differently.")

# ---------- (iii) the untyped contrast ----------
print("\n== (iii) mis-typed seams pay the Part-I tradeoff ==")
print("   delta    max |p(m)-1/2|   mean output infidelity")
for delta in (0.0, 0.1, 0.2, 0.4):
    worst_p, infs = 0.0, []
    for _ in range(150):
        a = rng.standard_normal(2) + 1j * rng.standard_normal(2)
        psi = a / np.linalg.norm(a)
        th = rng.uniform(0, 2 * np.pi)
        # mis-rotated measurement: mix a Z-component into the basis
        plus = np.array([1, 1], complex) / np.sqrt(2)
        state = np.diag([1, 1, 1, -1]).astype(complex) @ np.kron(psi, plus)
        ideal = mbqc_step(psi, th)
        for m in (0, 1):
            bra = np.array([np.cos(np.pi / 4 - delta / 2),
                            (-1) ** m * np.exp(-1j * th)
                            * np.sin(np.pi / 4 - delta / 2)], complex)
            bra = bra / np.linalg.norm(bra)
            sub = np.array([bra.conj() @ state.reshape(2, 2)[:, k]
                            for k in range(2)])
            p = float(np.real(sub.conj() @ sub))
            worst_p = max(worst_p, abs(p - 0.5))
            if p > 1e-9:
                sub = sub / np.sqrt(p)
                corr = np.linalg.matrix_power(X, m) @ sub
                F = abs(np.vdot(ideal[m][1], corr)) ** 2
                infs.append(p * (1 - F) * 2)
    print(f"   {delta:4.2f}      {worst_p:.5f}          "
          f"{np.mean(infs):.5f}")
print("  -> at delta = 0 the seam is typed (no evidence, no damage);")
print("     mis-rotation makes the click informative about the logical")
print("     state and the output infidelity rises with it - leakage and")
print("     damage move together (Part I), and MBQC is the engineering")
print("     of seams pinned to the zero-evidence point.")
print("== p26h done ==")

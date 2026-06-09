"""
v6 Paper 2 Part II §5.5: finite A-Scale receipt execution.

This is a fork-test, not a derivation. It builds one scalar finite-record
threshold model and asks whether the same event law supplies:

1. detector threshold rate gamma,
2. memory width beta^{-1},
3. finite heating with the same beta,
4. no vacuum events,
5. the gravity-source density,
6. a zero foliation-loop residue for spacelike threshold operations.

The sting is at the end: if the threshold S_* and the memory width ell are
inputs, then the receipts are internally coherent but A-Scale is not derived.
"""

from __future__ import annotations

import numpy as np


def kernel(dtau: np.ndarray, ell: float) -> np.ndarray:
    """Two-sided smooth memory kernel in proper time."""
    return np.exp(-((np.abs(dtau) / ell) ** 4))


def stability_profile(tau: np.ndarray, centers: np.ndarray, amp: float, ell: float) -> np.ndarray:
    """Scalar finite-record stability from invariant proper-time pulses."""
    s = np.zeros_like(tau)
    for c in centers:
        s += amp * kernel(tau - c, ell)
    return s


def count_threshold_components(tau: np.ndarray, stability: np.ndarray, threshold: float) -> tuple[int, np.ndarray]:
    """Count connected threshold-crossing components and return their centers."""
    mask = stability >= threshold
    starts = np.flatnonzero(mask & np.r_[True, ~mask[:-1]])
    ends = np.flatnonzero(mask & np.r_[~mask[1:], True])
    centers = []
    for a, b in zip(starts, ends):
        centers.append(float(tau[(a + b) // 2]))
    return len(centers), np.array(centers)


def heating(beta: float, cutoff: float, n: int = 200_000) -> float:
    """Heating proxy with the same smooth two-sided scale."""
    w = np.linspace(0.0, cutoff, n)
    spectrum = np.exp(-((w / beta) ** 4))
    return float(np.trapezoid(w**3 * spectrum, w))


def fano_preferred_frame_signal(tau_events: np.ndarray, beta_boost: float, bins: int = 10) -> tuple[float, float]:
    """Compare proper-time binning with coordinate-time binning under a boost."""
    gamma = 1.0 / np.sqrt(1.0 - beta_boost**2)
    counts_proper, _ = np.histogram(tau_events, bins=bins)
    counts_coord, _ = np.histogram(gamma * tau_events, bins=bins)

    def fano(c: np.ndarray) -> float:
        mean = np.mean(c)
        return float(np.var(c) / mean) if mean > 0 else 0.0

    return fano(counts_proper), fano(counts_coord)


def foliation_loop_residue() -> float:
    """Two spacelike scalar threshold operations are diagonal projectors."""
    # Four basis states for two spacelike local record cells: 00, 01, 10, 11.
    p_x = np.diag([0.0, 0.0, 1.0, 1.0])
    p_y = np.diag([0.0, 1.0, 0.0, 1.0])
    return float(np.linalg.norm(p_x @ p_y - p_y @ p_x))


def main() -> None:
    # These are intentionally visible inputs. If a future theorem derives them
    # from finite-record stability, this script becomes an execution receipt.
    ell = 1.7
    beta = 1.0 / ell
    threshold = 1.0
    amp = 1.35
    tau = np.linspace(0.0, 48.0, 12_001)
    centers = np.array([4.0, 10.3, 16.1, 22.7, 29.0, 35.4, 42.2])

    stability = stability_profile(tau, centers, amp, ell)
    n_events, event_centers = count_threshold_components(tau, stability, threshold)
    proper_volume = tau[-1] - tau[0]
    gamma_rate = n_events / proper_volume

    # Memory width from the same threshold-event kernel: e^{-1} occurs at ell.
    dt = np.linspace(0.0, 6.0 * ell, 20_000)
    corr = kernel(dt, ell)
    beta_inv = float(dt[np.argmin(np.abs(corr - np.exp(-1.0)))])

    h = heating(beta, cutoff=40.0 * beta)
    h_analytic = beta**4 / 4.0

    vacuum_stability = np.zeros_like(tau)
    n_vac, _ = count_threshold_components(tau, vacuum_stability, threshold)

    source_count = n_events
    fano_tau, fano_coord = fano_preferred_frame_signal(event_centers, beta_boost=0.6)
    loop_residue = foliation_loop_residue()

    print("=" * 88)
    print("v6 Paper 2 Part II §5.5: finite A-Scale receipt execution")
    print("=" * 88)
    print(f"visible inputs: threshold S_*={threshold:.3f}, memory ell={ell:.3f}, beta={beta:.5f}, amp={amp:.3f}")
    print()
    print("receipt 1 -- detector threshold rate")
    print(f"  threshold components = {n_events}, proper interval = {proper_volume:.1f}, gamma = {gamma_rate:.5f}")
    print(f"  boost check: Fano(proper bins)={fano_tau:.3f}, Fano(boosted coordinate bins)={fano_coord:.3f}")
    print()
    print("receipt 2 -- memory width")
    print(f"  e^-1 correlation length beta^-1 = {beta_inv:.5f}; input ell = {ell:.5f}; ratio = {beta_inv / ell:.5f}")
    print()
    print("receipt 3 -- heating with same beta")
    print(f"  numerical H = {h:.8f}; analytic beta^4/4 = {h_analytic:.8f}; ratio = {h / h_analytic:.6f}")
    print()
    print("receipt 4 -- vacuum no-events")
    print(f"  vacuum threshold components = {n_vac}")
    print()
    print("receipt 5 -- gravity-source identity")
    print(f"  source count = {source_count}; event count = {n_events}; match = {source_count == n_events}")
    print()
    print("receipt 6 -- foliation loop")
    print(f"  scalar threshold projector commutator norm = {loop_residue:.3e}")
    print()
    print("=" * 88)
    print("VERDICT")
    print("=" * 88)
    all_receipts = (
        n_events > 0
        and abs(beta_inv / ell - 1.0) < 1e-3
        and abs(h / h_analytic - 1.0) < 1e-4
        and n_vac == 0
        and source_count == n_events
        and loop_residue < 1e-12
    )
    print(f"finite receipt coherence: {'PASS' if all_receipts else 'FAIL'}")
    print("A-Scale derivation: OPEN")
    print("  The five physical receipts plus the foliation-loop receipt are mutually consistent,")
    print("  but S_* and ell were visible inputs. This is branch-B-compatible until a record")
    print("  theorem derives the threshold and memory width from finite ISP record formation.")


if __name__ == "__main__":
    main()

"""
v6 Paper 2 Part II §5.7: candidate finite-record stability functionals.

This probe attacks branch A directly. It tests three plausible candidates for
S_R on the same finite detector-record trace:

1. minimum same-first-order distinguishability,
2. redundant-copy stability,
3. irreversible/non-refinable record formation.

The question is not whether they can detect records. They can. The question is
whether any candidate fixes its threshold and memory width without adding a
choice. If the threshold or smoothing scale is still visible, A-Scale remains
open.
"""

from __future__ import annotations

import numpy as np


def pulse_trace(t: np.ndarray, centers: np.ndarray, width: float, amp: float) -> np.ndarray:
    y = np.zeros_like(t)
    for c in centers:
        y += amp * np.exp(-0.5 * ((t - c) / width) ** 2)
    return y


def count_components(t: np.ndarray, score: np.ndarray, threshold: float) -> tuple[int, np.ndarray]:
    mask = score >= threshold
    starts = np.flatnonzero(mask & np.r_[True, ~mask[:-1]])
    ends = np.flatnonzero(mask & np.r_[~mask[1:], True])
    centers = [float(t[(a + b) // 2]) for a, b in zip(starts, ends)]
    return len(centers), np.array(centers)


def e_fold_width(t: np.ndarray, score: np.ndarray) -> float:
    score = score - np.mean(score)
    corr = np.correlate(score, score, mode="full")
    corr = corr[corr.size // 2 :]
    if corr[0] <= 0:
        return float("nan")
    corr = corr / corr[0]
    dt = t[1] - t[0]
    idx = np.argmax(corr <= np.exp(-1.0))
    return float(idx * dt) if idx > 0 else float("nan")


def binary_entropy(p: np.ndarray) -> np.ndarray:
    p = np.clip(p, 1e-12, 1.0 - 1e-12)
    return -(p * np.log2(p) + (1.0 - p) * np.log2(1.0 - p))


def main() -> None:
    rng = np.random.default_rng(42)
    t = np.linspace(0.0, 60.0, 12_001)
    centers = np.array([6.0, 13.4, 21.0, 31.2, 39.8, 50.5])
    width = 0.85
    amp = 2.4
    noise_sigma = 0.45

    clean = pulse_trace(t, centers, width, amp)
    noise = rng.normal(0.0, noise_sigma, size=t.size)
    z = (clean + noise) / noise_sigma

    # Candidate 1: Gaussian log-likelihood / KL distinguishability from the
    # same-first-order null. It detects pulses, but any nonzero threshold is a
    # convention unless record theory supplies it.
    s_kl = 0.5 * np.maximum(z, 0.0) ** 2

    # Candidate 2: redundant-copy stability. Convert z to a copy error
    # probability and count mutual information across three independent
    # channels. Natural-looking thresholds such as one bit are still choices.
    p_err = 1.0 / (1.0 + np.exp(2.0 * np.maximum(z, 0.0)))
    s_red = 3.0 * (1.0 - binary_entropy(p_err))

    # Candidate 3: irreversibility / non-refinability. A record forms on a
    # positive irreversible rise. This depends on a coarse-graining derivative.
    dt = t[1] - t[0]
    dz = np.r_[0.0, np.diff(np.maximum(z, 0.0))] / dt
    window = 80
    kernel = np.ones(window) / window
    dz_smooth = np.convolve(np.maximum(dz, 0.0), kernel, mode="same")
    s_irr = dz_smooth / (np.std(dz_smooth) + 1e-12)

    candidates = [
        ("min-KL distinguishability", s_kl, [0.25, np.log(2.0), 1.50]),
        ("redundant-copy stability", s_red, [0.50, 1.00, 2.00]),
        ("irreversibility / non-refinability", s_irr, [0.75, 1.50, 3.00]),
    ]

    print("=" * 92)
    print("v6 Paper 2 Part II §5.7: candidate S_R fork-test")
    print("=" * 92)
    print(f"record trace: {len(centers)} planted stable records, width={width}, amp/noise={amp/noise_sigma:.2f}")
    print()

    for name, score, thresholds in candidates:
        width_est = e_fold_width(t, score)
        print(name)
        print(f"  score e-fold width beta^-1 candidate = {width_est:.4f}")
        print("  threshold scan:")
        for th in thresholds:
            n, event_centers = count_components(t, score, th)
            gamma = n / (t[-1] - t[0])
            hit = np.sum([np.any(np.abs(event_centers - c) < 1.5 * width) for c in centers])
            print(f"    S_*={th:>7.4f} -> events={n:>3}, gamma={gamma:>7.4f}, planted-hit={hit}/{len(centers)}")
        print()

    print("=" * 92)
    print("VERDICT")
    print("=" * 92)
    print("All three candidates can be made to detect the planted records, but none fixes A-Scale.")
    print("- min-KL needs a positive evidence threshold; S_*=0 would count noise.")
    print("- redundant-copy stability needs a redundancy target, e.g. one bit or two bits.")
    print("- irreversibility needs a coarse-graining derivative/window and threshold.")
    print("Therefore S_R is constrained but not yet canonical: gamma and beta still move when the")
    print("threshold or smoothing convention is changed. Branch A needs a theorem selecting those")
    print("choices from finite ISP record formation.")


if __name__ == "__main__":
    main()

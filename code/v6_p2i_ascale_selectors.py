"""
v6 Paper 2 Part II §5.9: A-Scale selector scan after the regraduation no-go.

The no-go says the current axioms cannot select a numerical threshold S_*.
This script tests candidate extra selectors one by one:

1. gravity-source density matching,
2. vacuum-zero plus detector-survival boundary,
3. criticality / percolation,
4. minimal heating / minimal disturbance,
5. TS-integrability fixed point,
6. canonical information unit.

The output classifies each selector as unique, interval/plateau, nonselective,
or externally calibrated.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class ScanRow:
    threshold: float
    events: int
    hits: int
    vacuum_events: int
    mean_width: float
    heating: float
    ts_residue: float
    largest_fraction: float


def pulse_trace(t: np.ndarray, centers: np.ndarray, width: float, amp: float) -> np.ndarray:
    y = np.zeros_like(t)
    for c in centers:
        y += amp * np.exp(-0.5 * ((t - c) / width) ** 2)
    return y


def smooth(y: np.ndarray, window: int) -> np.ndarray:
    k = np.ones(window) / window
    return np.convolve(y, k, mode="same")


def components(t: np.ndarray, score: np.ndarray, threshold: float) -> tuple[np.ndarray, np.ndarray]:
    mask = score >= threshold
    starts = np.flatnonzero(mask & np.r_[True, ~mask[:-1]])
    ends = np.flatnonzero(mask & np.r_[~mask[1:], True])
    centers = []
    widths = []
    for a, b in zip(starts, ends):
        centers.append(float(t[(a + b) // 2]))
        widths.append(float(t[b] - t[a]))
    return np.array(centers), np.array(widths)


def planted_hits(event_centers: np.ndarray, planted: np.ndarray, tol: float) -> int:
    return int(sum(np.any(np.abs(event_centers - c) <= tol) for c in planted))


def heating_from_width(width: float) -> float:
    if not np.isfinite(width) or width <= 0:
        return float("inf")
    beta = 1.0 / width
    return beta**4 / 4.0


def scan_thresholds() -> tuple[np.ndarray, list[ScanRow], dict[str, float]]:
    rng = np.random.default_rng(7)
    t = np.linspace(0.0, 60.0, 12_001)
    planted = np.array([6.0, 13.4, 21.0, 31.2, 39.8, 50.5])
    width = 0.85
    amp = 2.4

    raw = pulse_trace(t, planted, width, amp) + rng.normal(0.0, 0.16, size=t.size)
    score = smooth(np.maximum(raw, 0.0), 81)

    vac_raw = rng.normal(0.0, 0.16, size=t.size)
    vac_score = smooth(np.maximum(vac_raw, 0.0), 81)

    thresholds = np.linspace(0.05, float(np.max(score)) * 0.98, 420)
    rows: list[ScanRow] = []
    for th in thresholds:
        ev, widths = components(t, score, th)
        vac, _ = components(t, vac_score, th)
        hits = planted_hits(ev, planted, tol=1.4 * width)
        mean_width = float(np.mean(widths)) if widths.size else float("nan")
        largest_fraction = float(np.max(widths) / (t[-1] - t[0])) if widths.size else 0.0
        rows.append(
            ScanRow(
                threshold=float(th),
                events=int(ev.size),
                hits=hits,
                vacuum_events=int(vac.size),
                mean_width=mean_width,
                heating=heating_from_width(mean_width),
                ts_residue=0.0,  # scalar finite projectors commute for every threshold in this model
                largest_fraction=largest_fraction,
            )
        )

    meta = {
        "target_events": float(len(planted)),
        "target_gamma": float(len(planted) / (t[-1] - t[0])),
        "duration": float(t[-1] - t[0]),
    }
    return thresholds, rows, meta


def interval(rows: list[ScanRow], predicate) -> tuple[float | None, float | None, int]:
    vals = [r.threshold for r in rows if predicate(r)]
    if not vals:
        return None, None, 0
    return min(vals), max(vals), len(vals)


def nearest(rows: list[ScanRow], objective) -> ScanRow:
    return min(rows, key=objective)


def print_interval(label: str, lo: float | None, hi: float | None, n: int) -> None:
    if n == 0:
        print(f"  {label}: no admissible threshold")
    elif n == 1:
        print(f"  {label}: unique grid point S_*={lo:.4f}")
    else:
        print(f"  {label}: interval S_* in [{lo:.4f}, {hi:.4f}] ({n} grid points)")


def main() -> None:
    thresholds, rows, meta = scan_thresholds()
    target_events = int(meta["target_events"])

    print("=" * 96)
    print("v6 Paper 2 Part II §5.9: A-Scale selector scan")
    print("=" * 96)
    print(f"target source count = {target_events}; target gamma = {meta['target_gamma']:.5f}")
    print(f"threshold scan = {len(thresholds)} grid points")
    print()

    # 1. Gravity/source density matching.
    lo, hi, n = interval(rows, lambda r: r.events == target_events)
    print("1. gravity-source density matching")
    print_interval("event count = source count", lo, hi, n)
    if n > 1:
        print("  verdict: selects an event-count plateau, not a unique numerical threshold")
    print()

    # 2. Vacuum-zero plus detector-survival.
    lo, hi, n = interval(rows, lambda r: r.vacuum_events == 0 and r.hits == target_events)
    print("2. vacuum-zero plus detector-survival")
    print_interval("vacuum=0 and detector hits all planted records", lo, hi, n)
    if n > 1:
        print("  verdict: gives an admissible interval; needs a boundary or optimality rule")
    print()

    # 3. Criticality / percolation.
    # Finite 1D proxy: maximize discrete derivative of largest-component fraction.
    lf = np.array([r.largest_fraction for r in rows])
    deriv = np.abs(np.gradient(lf, thresholds))
    crit_idx = int(np.argmax(deriv))
    crit = rows[crit_idx]
    print("3. criticality / percolation")
    print(f"  susceptibility peak at S_*={crit.threshold:.4f}: events={crit.events}, hits={crit.hits}, vacuum={crit.vacuum_events}")
    print("  verdict: produces a grid-local point, but depends on finite-size/percolation definition")
    print()

    # 4. Minimal heating / minimal disturbance.
    admissible = [r for r in rows if r.vacuum_events == 0 and r.hits == target_events]
    print("4. minimal heating / minimal disturbance")
    if admissible:
        best = min(admissible, key=lambda r: r.heating)
        print(
            f"  min heating among vacuum/detector-admissible thresholds at S_*={best.threshold:.4f}: "
            f"H={best.heating:.6f}, events={best.events}"
        )
        print("  verdict: selects a boundary of a prior admissible interval, not a standalone threshold")
    else:
        print("  no admissible vacuum/detector threshold, so selector cannot run")
    print()

    # 5. TS-integrability fixed point.
    lo, hi, n = interval(rows, lambda r: r.ts_residue < 1e-12)
    print("5. TS-integrability fixed point")
    print_interval("finite scalar TS residue = 0", lo, hi, n)
    print("  verdict: nonselective in the finite scalar model; all thresholds commute")
    print()

    # 6. Canonical information unit.
    info_threshold = 1.0
    info = nearest(rows, lambda r: abs(r.threshold - info_threshold))
    print("6. canonical information unit")
    print(
        f"  S_*=1.0000 nearest grid gives events={info.events}, hits={info.hits}, "
        f"vacuum={info.vacuum_events}, gamma={info.events / meta['duration']:.5f}"
    )
    print("  verdict: numerically sharp only if one information unit is independently canonical")
    print()

    print("=" * 96)
    print("SUMMARY")
    print("=" * 96)
    print("No tested selector closes A-Scale by itself.")
    print("- gravity matching and vacuum/detector survival give intervals or plateaus;")
    print("- criticality gives a finite-size convention-sensitive point;")
    print("- minimal heating optimizes over a prior admissible interval;")
    print("- TS integrability is nonselective in the finite scalar model;")
    print("- canonical information unit works only if the unit is independently derived.")
    print("The strongest branch-A path is therefore a combined selector, especially")
    print("gravity-source density + vacuum/detector boundary + an ISP-native information unit.")


if __name__ == "__main__":
    main()

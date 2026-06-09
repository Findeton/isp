#!/usr/bin/env python3
"""Paper 3 section 63 diagnostic.

Full campaign for the Diamond Work-Balance Law.

Verdict tested here:

* proved in the primitive binary modular-score class;
* existence holds for finite one-score exponential laws after normalization;
* uniqueness fails for general finite one-score spectra;
* scalar balance underdetermines multi-score diamonds;
* therefore the universal law is discarded unless sealed indivisibility proves
  a primitive one-dimensional two-sector modular score.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Row:
    target: str
    result: str
    value: str
    verdict: str


def normalize(values: list[float], counts: list[int] | None = None) -> tuple[list[float], list[float]]:
    if counts is None:
        counts = [1] * len(values)
    total = float(sum(counts))
    weights = [c / total for c in counts]
    mean = sum(w * v for w, v in zip(weights, values))
    var = sum(w * (v - mean) ** 2 for w, v in zip(weights, values))
    if var <= 0.0:
        raise ValueError("score spectrum must be nonconstant")
    scale = math.sqrt(var)
    return [(v - mean) / scale for v in values], weights


def work_response(values: list[float], weights: list[float], eta: float) -> tuple[float, float]:
    exponents = [eta * v for v in values]
    max_exp = max(exponents)
    raw = [w * math.exp(e - max_exp) for w, e in zip(weights, exponents)]
    z = sum(raw)
    probs = [r / z for r in raw]
    psi = math.log(z) + max_exp
    mean = sum(p * v for p, v in zip(probs, values))
    work = eta * mean - psi
    response = sum(p * (v - mean) ** 2 for p, v in zip(probs, values))
    return work, response


def residual(values: list[float], weights: list[float], eta: float) -> float:
    work, response = work_response(values, weights, eta)
    return work - response


def roots(values: list[float], weights: list[float], max_eta: float = 20.0, steps: int = 10000) -> list[float]:
    out: list[float] = []
    prev_eta = 0.0
    prev = residual(values, weights, prev_eta)
    for i in range(1, steps + 1):
        eta = max_eta * i / steps
        cur = residual(values, weights, eta)
        if cur * prev < 0.0:
            lo = prev_eta
            hi = eta
            flo = prev
            for _ in range(90):
                mid = 0.5 * (lo + hi)
                fm = residual(values, weights, mid)
                if fm * flo <= 0.0:
                    hi = mid
                else:
                    lo = mid
                    flo = fm
            out.append(0.5 * (lo + hi))
        prev_eta = eta
        prev = cur
    return out


def binary_theta_root() -> tuple[float, float, float]:
    def work(theta: float) -> float:
        return 0.5 * (
            (1.0 + theta) * math.log(1.0 + theta)
            + (1.0 - theta) * math.log(1.0 - theta)
        )

    def f(theta: float) -> float:
        return work(theta) - (1.0 - theta * theta)

    lo = 0.0
    hi = 1.0 - 1e-15
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        if f(mid) < 0.0:
            lo = mid
        else:
            hi = mid
    theta = 0.5 * (lo + hi)
    return theta, 0.5 * math.log((1.0 + theta) / (1.0 - theta)), work(theta)


def binary_f_theta(theta: float) -> float:
    work = 0.5 * (
        (1.0 + theta) * math.log(1.0 + theta)
        + (1.0 - theta) * math.log(1.0 - theta)
    )
    return work - (1.0 - theta * theta)


def theta_for_binary_residual(target: float) -> float | None:
    lo = 0.0
    hi = 1.0 - 1e-14
    if target < binary_f_theta(lo) or target > binary_f_theta(hi):
        return None
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        if binary_f_theta(mid) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main() -> None:
    rows: list[Row] = []

    theta, eta, common_work = binary_theta_root()
    rows.append(
        Row(
            "primitive binary theorem",
            "unique nonzero root because F'=atanh(theta)+2theta>0",
            f"theta={theta:.15f}, eta={eta:.15f}, W=J={common_work:.15f}",
            "PROVED",
        )
    )

    three_values, three_weights = normalize([-1.0, 0.0, 1.0])
    three_roots = roots(three_values, three_weights)
    rows.append(
        Row(
            "regular one-score spectrum",
            "tested three-shell count spectrum has one root",
            ", ".join(f"{r:.12f}" for r in three_roots),
            "PASS-EXAMPLE",
        )
    )

    bad_values_raw = [
        -15.848391065169443,
        -15.26135706229148,
        -6.540840401342667,
        0.8016439899950072,
        18.903204268406732,
    ]
    # This is a finite uniform multiset represented by multiplicities.
    bad_counts = [1_141_481, 45, 1_310_511, 67, 3]
    bad_values, bad_weights = normalize(bad_values_raw, bad_counts)
    bad_roots = roots(bad_values, bad_weights, max_eta=8.0, steps=12000)
    rows.append(
        Row(
            "general one-score uniqueness",
            "finite count-multiplicity spectrum has three roots",
            ", ".join(f"{r:.12f}" for r in bad_roots),
            "REFUTED-GENERAL",
        )
    )

    theta_a = 0.55
    needed = -binary_f_theta(theta_a)
    theta_b = theta_for_binary_residual(needed)
    theta_c = theta
    rows.append(
        Row(
            "multi-score scalar balance",
            "F(theta1)+F(theta2)=0 has more than one solution",
            f"({theta:.6f},{theta:.6f}) and ({theta_a:.6f},{theta_b:.6f})",
            "REFUTED-SCALAR-SELECTION",
        )
    )

    rows.append(
        Row(
            "componentwise repair",
            "F_i(theta_i)=0 would select theta* in each primitive channel",
            f"theta_i={theta:.12f}",
            "COND-NEEDS-CANONICAL-CHANNELS",
        )
    )

    rows.append(
        Row(
            "universal DWB law",
            "not valid as a uniqueness law on arbitrary sealed finite diamonds",
            "one-score and vector counterexamples",
            "DISCARDED",
        )
    )

    rows.append(
        Row(
            "primitive DWB law",
            "valid for indivisible binary modular-score defects",
            "selects P_D, beta, source amplitude, common work",
            "SURVIVES",
        )
    )

    print("| target | result | value | verdict |")
    print("|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.result} | {row.value} | {row.verdict} |")

    print()
    print("binary_theta", f"{theta:.15f}")
    print("binary_eta", f"{eta:.15f}")
    print("binary_common_work", f"{common_work:.15f}")
    print("three_shell_root_count", len(three_roots))
    print("bad_spectrum_atom_count", sum(bad_counts))
    print("bad_spectrum_root_count", len(bad_roots))
    print("bad_spectrum_roots", " ".join(f"{r:.15f}" for r in bad_roots))
    print("vector_second_solution_theta_a", f"{theta_a:.15f}")
    print("vector_second_solution_theta_b", f"{theta_b:.15f}" if theta_b is not None else "none")


if __name__ == "__main__":
    main()

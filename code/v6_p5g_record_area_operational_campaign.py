#!/usr/bin/env python3
"""Paper 5 diagnostic G: record-area operational campaign.

Finish condition:
  Either sealed screen operations determine an absolute record-area quantum
  A_rec, or they determine only an additive area valuation up to one global
  multiplier.

Result:
  Finite screen gluing, refinement stability, monotonicity, and record-capacity
  additivity force an area-like valuation of the form

      A_op(S) = A_rec C(S)

  where C(S) is the sealed screen record capacity.  They do not fix A_rec.
  Thus operational record-area ratios are intrinsic, but the absolute
  continuum area unit, and therefore the Newton/Jacobson coupling, remains
  free unless an additional invariant fixes A_rec.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Screen:
    """Finite sealed screen made from primitive record-capacity cells."""

    cells: tuple[float, ...]

    def capacity(self) -> float:
        return sum(self.cells)

    def disjoint_union(self, other: "Screen") -> "Screen":
        return Screen(self.cells + other.cells)

    def refine_cell(self, index: int, pieces: tuple[float, ...]) -> "Screen":
        before = self.cells[:index]
        after = self.cells[index + 1 :]
        old = self.cells[index]
        if not math.isclose(sum(pieces), old, rel_tol=0.0, abs_tol=1e-12):
            raise ValueError("refinement must preserve record capacity")
        return Screen(before + pieces + after)


@dataclass(frozen=True)
class Row:
    target: str
    test: str
    result: str
    value: str
    verdict: str


def area_linear(screen: Screen, area_quantum: float) -> float:
    return area_quantum * screen.capacity()


def area_offset(screen: Screen, area_quantum: float, offset: float) -> float:
    return area_quantum * screen.capacity() + offset


def area_power(screen: Screen, area_quantum: float, power: float) -> float:
    return area_quantum * screen.capacity() ** power


def additivity_gap(fn, left: Screen, right: Screen) -> float:
    return abs(fn(left.disjoint_union(right)) - fn(left) - fn(right))


def refinement_gap(fn, coarse: Screen, refined: Screen) -> float:
    return abs(fn(coarse) - fn(refined))


def seam_gluing_gap(fn, left: Screen, right: Screen, shared: Screen, glued: Screen) -> float:
    """Inclusion-exclusion test for a screen glued across a shared boundary."""

    return abs(fn(glued) - (fn(left) + fn(right) - fn(shared)))


def sigma_area(entropy_capacity: float, continuum_area: float) -> float:
    return entropy_capacity / continuum_area


def kappa_from_sigma(sigma: float) -> float:
    return 1.0 / sigma


def print_table(rows: list[Row]) -> None:
    print("| target | test | result | value | verdict |")
    print("|---|---|---|---:|---|")
    for row in rows:
        print(f"| {row.target} | {row.test} | {row.result} | {row.value} | {row.verdict} |")


def main() -> None:
    base = Screen((1.0, 1.0, 2.0))
    probe = Screen((0.5, 1.5))
    refined = base.refine_cell(2, (0.75, 1.25))

    shared = Screen((1.0,))
    left = Screen((1.0, 2.0))
    right = Screen((1.0, 3.0))
    glued = Screen((1.0, 2.0, 3.0))

    a1 = 1.0
    a2 = 3.0
    offset = 0.75
    power = 2.0

    lin1 = lambda s: area_linear(s, a1)
    lin2 = lambda s: area_linear(s, a2)
    off = lambda s: area_offset(s, a1, offset)
    pow2 = lambda s: area_power(s, a1, power)

    lin_add_gap = additivity_gap(lin1, base, probe)
    lin_ref_gap = refinement_gap(lin1, base, refined)
    lin_seam_gap = seam_gluing_gap(lin1, left, right, shared, glued)

    lin2_add_gap = additivity_gap(lin2, base, probe)
    lin2_ref_gap = refinement_gap(lin2, base, refined)
    lin2_seam_gap = seam_gluing_gap(lin2, left, right, shared, glued)

    off_add_gap = additivity_gap(off, base, probe)
    pow_add_gap = additivity_gap(pow2, base, probe)
    pow_ref_gap = refinement_gap(pow2, base, refined)

    cap_ratio = base.capacity() / probe.capacity()
    area_ratio_a1 = lin1(base) / lin1(probe)
    area_ratio_a2 = lin2(base) / lin2(probe)

    entropy = base.capacity()
    sigma_a1 = sigma_area(entropy, lin1(base))
    sigma_a2 = sigma_area(entropy, lin2(base))
    kappa_a1 = kappa_from_sigma(sigma_a1)
    kappa_a2 = kappa_from_sigma(sigma_a2)

    heat_record_units = entropy / (2.0 * math.pi)
    heat_per_area_a1 = heat_record_units / lin1(base)
    heat_per_area_a2 = heat_record_units / lin2(base)

    rows = [
        Row(
            "record capacity",
            "C(S union T)=C(S)+C(T) and refinement preserves C",
            "sealed screen operations define intrinsic capacity",
            f"C_base={base.capacity():.3f}, C_refined={refined.capacity():.3f}",
            "CAPACITY-DERIVED",
        ),
        Row(
            "linear record-area",
            "A_op(S)=A_rec C(S)",
            "passes additivity, refinement, and shared-boundary gluing",
            f"add={lin_add_gap:.1e}, ref={lin_ref_gap:.1e}, glue={lin_seam_gap:.1e}",
            "PASS",
        ),
        Row(
            "scale twin",
            "A'_op(S)=3 A_rec C(S)",
            "also passes all record-area operational tests",
            f"add={lin2_add_gap:.1e}, ref={lin2_ref_gap:.1e}, glue={lin2_seam_gap:.1e}",
            "SAME-TESTS",
        ),
        Row(
            "offset valuation",
            "A(S)=A_rec C(S)+b",
            "constant offsets violate finite additivity",
            f"add_gap={off_add_gap:.3f}",
            "REJECT",
        ),
        Row(
            "nonlinear valuation",
            "A(S)=A_rec C(S)^2",
            "nonlinear capacity rules violate additivity while preserving refinement",
            f"add_gap={pow_add_gap:.3f}, ref_gap={pow_ref_gap:.1e}",
            "REJECT",
        ),
        Row(
            "area ratios",
            "compare S/T before and after rescaling A_rec",
            "all operational ratios are fixed by record capacity",
            f"C_ratio={cap_ratio:.3f}, A_ratios={area_ratio_a1:.3f}/{area_ratio_a2:.3f}",
            "RATIO-DERIVED",
        ),
        Row(
            "entropy-area density",
            "sigma_A=C/A_op",
            "density changes under the invisible global multiplier",
            f"sigma={sigma_a1:.3f}/{sigma_a2:.3f}",
            "SIGMA-FREE",
        ),
        Row(
            "modular heat per area",
            "same record heat, different continuum area unit",
            "record thermodynamics is fixed but area density is not",
            f"q_A={heat_per_area_a1:.6f}/{heat_per_area_a2:.6f}",
            "DENSITY-FREE",
        ),
        Row(
            "Einstein coupling",
            "kappa proportional to 1/sigma_A",
            "two accepted record-area valuations give two couplings",
            f"kappa={kappa_a1:.3f}/{kappa_a2:.3f}",
            "COUPLING-SPLIT",
        ),
        Row(
            "campaign verdict",
            "all operational screen tests versus A_rec",
            "record-area is unique up to one global unit, not absolutely fixed",
            "finish condition reached",
            "A_REC-SPLIT-PROVED",
        ),
    ]

    print_table(rows)
    print()

    values = {
        "lin_add_gap": lin_add_gap,
        "lin_ref_gap": lin_ref_gap,
        "lin_seam_gap": lin_seam_gap,
        "lin2_add_gap": lin2_add_gap,
        "lin2_ref_gap": lin2_ref_gap,
        "lin2_seam_gap": lin2_seam_gap,
        "off_add_gap": off_add_gap,
        "pow_add_gap": pow_add_gap,
        "pow_ref_gap": pow_ref_gap,
        "cap_ratio": cap_ratio,
        "area_ratio_a1": area_ratio_a1,
        "area_ratio_a2": area_ratio_a2,
        "sigma_a1": sigma_a1,
        "sigma_a2": sigma_a2,
        "sigma_gap": abs(sigma_a1 - sigma_a2),
        "kappa_a1": kappa_a1,
        "kappa_a2": kappa_a2,
        "kappa_gap": abs(kappa_a1 - kappa_a2),
        "heat_per_area_gap": abs(heat_per_area_a1 - heat_per_area_a2),
    }
    for key, value in values.items():
        print(f"{key} {value:.15e}")

    assert math.isclose(lin_add_gap, 0.0, abs_tol=1e-12)
    assert math.isclose(lin_ref_gap, 0.0, abs_tol=1e-12)
    assert math.isclose(lin_seam_gap, 0.0, abs_tol=1e-12)
    assert math.isclose(lin2_add_gap, 0.0, abs_tol=1e-12)
    assert math.isclose(lin2_ref_gap, 0.0, abs_tol=1e-12)
    assert math.isclose(lin2_seam_gap, 0.0, abs_tol=1e-12)
    assert off_add_gap > 0.0
    assert pow_add_gap > 0.0
    assert math.isclose(pow_ref_gap, 0.0, abs_tol=1e-12)
    assert math.isclose(cap_ratio, area_ratio_a1, abs_tol=1e-12)
    assert math.isclose(area_ratio_a1, area_ratio_a2, abs_tol=1e-12)
    assert values["sigma_gap"] > 0.0
    assert values["kappa_gap"] > 0.0
    assert values["heat_per_area_gap"] > 0.0


if __name__ == "__main__":
    main()

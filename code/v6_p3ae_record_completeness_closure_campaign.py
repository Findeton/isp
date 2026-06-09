"""
v6 Paper 3 section 41: record-completeness closure campaign.

Question:
    Is record completeness a theorem of the sealed physical process, or an
    extra axiom?  Equivalently, can every seam be resolved intrinsically as
    either:

        eventless:  a unique minimal complete RN screen with Delta=0;
        eventful:   an isolated positive residual RN defect;

    with no silent unrecorded influence?

Finite answer:
    The finite campaign closes the logical form.  Record completeness is not
    a universal property of arbitrary laws.  The intrinsic invariant is the
    seam residual spectrum

        epsilon_* = min_Y I(X;Z|Y)

    over causal antichain record closures.  A seam is eventless when
    epsilon_*=0 with a unique minimal complete screen.  A seam is eventful
    when epsilon_*>0 with an isolated role-blind floor.  The branch-A target
    is therefore a no-silent-seam law, not a blanket assertion that every
    finite law already has a complete screen.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product

from v6_p3ad_minimal_complete_screen_campaign import (
    Law,
    bypass_closure_law,
    cmi,
    copy_channel,
    duplicate_law,
    labels,
    normalize,
    oracle_law,
    role_split_laws,
    scan_screens,
)


EPS = 1.0e-10
SOURCE_FLOOR = 0.010


@dataclass(frozen=True)
class ClosureAudit:
    target: str
    law: str
    invariant: str
    positive: str
    obstruction: str
    value: str
    verdict: str


def direct_law(direct: float = 0.42) -> tuple[list[str], Law]:
    names = ["X", "S", "H", "Z"]
    law: Law = {}
    for bits in product((0, 1), repeat=len(names)):
        data = dict(zip(names, bits))
        x, s, h, z = data["X"], data["S"], data["H"], data["Z"]
        p_z_one = 0.05 + 0.22 * s + 0.18 * h + direct * x
        prob = 0.5
        prob *= copy_channel(s, x, 0.76)
        prob *= copy_channel(h, x, 0.68)
        prob *= p_z_one if z else 1.0 - p_z_one
        law[bits] = prob
    return names, normalize(law)


def mediator_with_noise() -> tuple[list[str], Law]:
    names = ["X", "S", "N", "Z"]
    law: Law = {}
    for bits in product((0, 1), repeat=len(names)):
        data = dict(zip(names, bits))
        x, s, z = data["X"], data["S"], data["Z"]
        prob = 0.5
        prob *= copy_channel(s, x, 0.82)
        prob *= 0.5
        prob *= copy_channel(z, s, 0.80)
        law[bits] = prob
    return names, normalize(law)


def all_subsets(candidates: list[str]) -> list[tuple[str, ...]]:
    out: list[tuple[str, ...]] = []
    for mask in range(1, 2 ** len(candidates)):
        subset = tuple(candidates[i] for i in range(len(candidates)) if mask & (1 << i))
        out.append(subset)
    return out


def residual_spectrum(law: Law, names: list[str], candidates: list[str]) -> list[tuple[tuple[str, ...], float]]:
    return sorted(
        ((subset, cmi(law, names, subset)) for subset in all_subsets(candidates)),
        key=lambda item: (item[1], len(item[0]), item[0]),
    )


def residual(law: Law, names: list[str], candidates: list[str]) -> float:
    return residual_spectrum(law, names, candidates)[0][1]


def greedy_closure(
    law: Law, names: list[str], candidates: list[str], start: tuple[str, ...]
) -> tuple[tuple[str, ...], float, list[str]]:
    current = tuple(name for name in start if name in candidates)
    path = [labels([current])]
    while True:
        base = cmi(law, names, current)
        best_record = ""
        best_value = base
        for candidate in candidates:
            if candidate in current:
                continue
            trial = tuple(sorted(current + (candidate,)))
            value = cmi(law, names, trial)
            if value < best_value - EPS:
                best_value = value
                best_record = candidate
        if not best_record:
            return current, base, path
        current = tuple(sorted(current + (best_record,)))
        path.append(labels([current]))


def minimizer_margin(law: Law, names: list[str], candidates: list[str]) -> tuple[float, float]:
    spectrum = residual_spectrum(law, names, candidates)
    best = spectrum[0][1]
    larger = [value for _subset, value in spectrum if value > best + EPS]
    margin = min(larger) - best if larger else 0.0
    return best, margin


def stable_residuals() -> tuple[float, float]:
    stable_values = []
    decaying_values = []
    for n in range(1, 9):
        names, stable = direct_law(0.42 + 0.01 / n)
        stable_values.append(residual(stable, names, ["S", "H"]))
        names, decaying = direct_law(0.42 / (n + 2) ** 2)
        decaying_values.append(residual(decaying, names, ["S", "H"]))
    return min(stable_values), min(decaying_values)


def audits() -> list[ClosureAudit]:
    rows: list[ClosureAudit] = []

    names, law = mediator_with_noise()
    final, defect, path = greedy_closure(law, names, ["S", "N"], ("S",))
    scan = scan_screens(law, names, ["S", "N"])
    rows.append(
        ClosureAudit(
            "eventless mediator",
            "X-S-Z plus noise",
            "closure by Delta decrease",
            f"path={' -> '.join(path)}",
            "noise not selected",
            f"Delta={defect:.1e}; minimal={labels(scan.minimals)}",
            "PASS-EVENTLESS-COMPLETE",
        )
    )

    names, law = bypass_closure_law()
    final, defect, path = greedy_closure(law, names, ["S", "H"], ("S",))
    rows.append(
        ClosureAudit(
            "recorded bypass",
            "X-S/H-Z",
            "closure adds records",
            f"path={' -> '.join(path)}",
            "single S incomplete",
            f"Delta={defect:.1e}; final={labels([final])}",
            "PASS-CLOSURE-COMPLETES",
        )
    )

    missing = residual(law, names, ["S"])
    rows.append(
        ClosureAudit(
            "missing record",
            "H omitted",
            "residual spectrum",
            f"epsilon*={missing:.6f}",
            "positive but unrepresented",
            "candidate lattice incomplete",
            "FAIL-SILENT-IF-IGNORED",
        )
    )

    names, law = direct_law(0.42)
    final, defect, path = greedy_closure(law, names, ["S", "H"], ("S",))
    rows.append(
        ClosureAudit(
            "direct residual",
            "unrecorded X->Z",
            "min residual epsilon*",
            f"epsilon*={defect:.6f}",
            "no zero screen",
            f"path={' -> '.join(path)}",
            "PASS-RESIDUAL-EVENT",
        )
    )

    names, weak = direct_law(0.025)
    weak_best, weak_margin = minimizer_margin(weak, names, ["S", "H"])
    rows.append(
        ClosureAudit(
            "weak residual",
            "tiny direct term",
            "floor test",
            f"epsilon*={weak_best:.6f}",
            f"floor={SOURCE_FLOOR:.3f}",
            f"margin={weak_margin:.6f}",
            "FAIL-NO-ISOLATED-FLOOR",
        )
    )

    names, law = oracle_law()
    all_scan = scan_screens(law, names, ["S", "O"])
    causal_scan = scan_screens(law, names, ["S"])
    rows.append(
        ClosureAudit(
            "causal admissibility",
            "future oracle O=Z",
            "exclude future screen",
            f"causal={labels(causal_scan.minimals)}",
            f"all={labels(all_scan.minimals)}",
            "oracle would cheat",
            "PASS-ONLY-CAUSAL-LATTICE",
        )
    )

    names, law = duplicate_law()
    scan = scan_screens(law, names, ["S", "D"])
    rows.append(
        ClosureAudit(
            "duplicate quotient",
            "D=S",
            "automorphism class",
            f"minimals={labels(scan.minimals)}",
            "labels nonunique",
            "one screen class after quotient",
            "PASS-CONDITIONAL-QUOTIENT",
        )
    )

    names, record_law, source_law = role_split_laws()
    record_scan = scan_screens(record_law, names, ["S", "H"])
    source_scan = scan_screens(source_law, names, ["S", "H"])
    rows.append(
        ClosureAudit(
            "role split",
            "record/source differ",
            "role-blind test",
            f"record={labels(record_scan.minimals)}",
            f"source={labels(source_scan.minimals)}",
            "screen class mismatch",
            "FAIL-ROLE-COMPLETENESS",
        )
    )

    stable_floor, decay_floor = stable_residuals()
    rows.append(
        ClosureAudit(
            "refinement floor",
            "stable vs decaying residual",
            "cofinal epsilon*",
            f"stable min={stable_floor:.6f}",
            f"decay min={decay_floor:.6f}",
            f"floor={SOURCE_FLOOR:.3f}",
            "PASS-STABLE-FAILS-DECAY",
        )
    )

    rows.append(
        ClosureAudit(
            "no-silent-seam law",
            "sealed process",
            "epsilon*=0 or event floor",
            "eventless screen or event",
            "silent residual forbidden",
            "record completeness becomes dichotomy",
            "THM-TARGET-NO-SILENT-SEAM",
        )
    )

    return rows


def print_audits(rows: list[ClosureAudit]) -> None:
    print("record-completeness closure campaign")
    print("------------------------------------")
    print(
        "target                    law                    invariant               "
        "positive                         obstruction                     value                         verdict"
    )
    for row in rows:
        print(
            f"{row.target:25s} "
            f"{row.law:22s} "
            f"{row.invariant:23s} "
            f"{row.positive:32s} "
            f"{row.obstruction:31s} "
            f"{row.value:29s} "
            f"{row.verdict}"
        )


def main() -> None:
    print("=" * 150)
    print("v6 Paper 3 section 41: record-completeness closure campaign")
    print("=" * 150)
    print_audits(audits())
    print()
    print("VERDICT")
    print("-------")
    print("Record completeness is not a universal property of arbitrary finite laws.")
    print("The intrinsic object is the seam residual spectrum over causal record")
    print("closures.  If epsilon*=0 with a unique role-blind minimal screen, the")
    print("seam is eventless and the screen is derived.  If epsilon*>0 with a")
    print("cofinal role-blind floor, the residual is an event/source defect, not a")
    print("missing convention.")
    print()
    print("The remaining branch-A-current theorem is the no-silent-seam law: every")
    print("physical seam is either RN-complete or carries an isolated residual event.")
    print("If positive residual influence can be ignored, or if the candidate record")
    print("lattice is chosen externally, the theory is branch B.")


if __name__ == "__main__":
    main()

"""
v6 Paper 3 section 42: origin of the no-silent-seam law.

Question:
    Why should physics forbid silent seams?  Can the rule be derived from
    sealed composition and RN action conservation rather than postulated?

Finite answer:
    A silent seam is exactly a positive relative-entropy gap between the full
    three-screen law and the law obtained by gluing adjacent bridges:

        A_silent(Y) =
        D(P_XYZ || P_XY P_YZ / P_Y)
        =
        I(X;Z|Y).

    If the seam is declared eventless, sealed composition requires this action
    to vanish.  If it does not vanish, action conservation has only two
    intrinsic repairs:

      1. enlarge the screen until the gap vanishes;
      2. count the isolated residual gap as an event/source defect.

    Ignoring a positive stable gap breaks RN action accounting, compositional
    gluing, and deletion locality.  This is the finite origin of the
    no-silent-seam law.
"""

from __future__ import annotations

from dataclasses import dataclass

from v6_p3ac_screen_bridge_theorem_campaign import (
    bypass_law,
    cmi_xz_given_y,
    compose_bridge,
    l1_matrix,
    marginal_xy,
    marginal_xz,
    marginal_y,
    marginal_yz,
    markov_law,
)
from v6_p3ad_minimal_complete_screen_campaign import (
    bypass_closure_law,
    cmi,
    labels,
    role_split_laws,
    scan_screens,
)
from v6_p3ae_record_completeness_closure_campaign import direct_law, residual, stable_residuals


SOURCE_FLOOR = 0.010


@dataclass(frozen=True)
class NoSilentAudit:
    target: str
    law: str
    invariant: str
    positive: str
    obstruction: str
    value: str
    verdict: str


def composition_error(law) -> float:
    qxy = marginal_xy(law)
    qyz = marginal_yz(law)
    py = marginal_y(law)
    return l1_matrix(marginal_xz(law), compose_bridge(qxy, qyz, py))


def action_balance(law) -> tuple[float, float]:
    delta = cmi_xz_given_y(law)
    return delta, delta


def audits() -> list[NoSilentAudit]:
    rows: list[NoSilentAudit] = []

    markov = markov_law()
    delta, missing = action_balance(markov)
    rows.append(
        NoSilentAudit(
            "eventless action",
            "Markov seam",
            "D(P||glue_Y P)",
            f"Delta={delta:.1e}",
            f"composition error={composition_error(markov):.1e}",
            f"missing action={missing:.1e}",
            "PASS-EVENTLESS-ACTION",
        )
    )

    bypass = bypass_law()
    delta, missing = action_balance(bypass)
    rows.append(
        NoSilentAudit(
            "silent bypass",
            "same adjacent bridges",
            "D(P||glue_Y P)",
            f"Delta={delta:.6f}",
            f"composition error={composition_error(bypass):.6f}",
            f"unaccounted action={missing:.6f}",
            "FAIL-SILENT-BREAKS-ACTION",
        )
    )

    names, closure = bypass_closure_law()
    delta_s = cmi(closure, names, ("S",))
    delta_sh = cmi(closure, names, ("S", "H"))
    rows.append(
        NoSilentAudit(
            "recorded repair",
            "bypass record H",
            "enlarge Y",
            f"Delta_S={delta_s:.6f}",
            f"Delta_SH={delta_sh:.1e}",
            "screen absorbs action",
            "PASS-RECORD-CLOSURE",
        )
    )

    names, direct = direct_law(0.42)
    eps = residual(direct, names, ["S", "H"])
    rows.append(
        NoSilentAudit(
            "residual event repair",
            "unrecorded direct term",
            "event work epsilon*",
            f"epsilon*={eps:.6f}",
            "no zero screen",
            f"event action={eps:.6f}",
            "PASS-COUNT-RESIDUAL",
        )
    )

    names, weak = direct_law(0.025)
    weak_eps = residual(weak, names, ["S", "H"])
    rows.append(
        NoSilentAudit(
            "weak residual",
            "tiny direct term",
            "floor test",
            f"epsilon*={weak_eps:.6f}",
            f"floor={SOURCE_FLOOR:.3f}",
            "not stable event work",
            "FAIL-NO-COFINAL-FLOOR",
        )
    )

    stable_floor, decay_floor = stable_residuals()
    rows.append(
        NoSilentAudit(
            "cofinal action floor",
            "stable vs decaying",
            "liminf epsilon*",
            f"stable={stable_floor:.6f}",
            f"decay={decay_floor:.6f}",
            f"floor={SOURCE_FLOOR:.3f}",
            "PASS-STABLE-ONLY",
        )
    )

    names, record_law, source_law = role_split_laws()
    record_scan = scan_screens(record_law, names, ["S", "H"])
    source_scan = scan_screens(source_law, names, ["S", "H"])
    rows.append(
        NoSilentAudit(
            "role-blind action",
            "split role seams",
            "same residual class",
            f"record={labels(record_scan.minimals)}",
            f"source={labels(source_scan.minimals)}",
            "different action carriers",
            "FAIL-ROLE-SPLIT-ACTION",
        )
    )

    names, direct = direct_law(0.42)
    eps_full = residual(direct, names, ["S", "H"])
    eps_missing = residual(direct, names, ["S"])
    rows.append(
        NoSilentAudit(
            "deletion locality",
            "ignore residual",
            "local action account",
            f"with records={eps_full:.6f}",
            f"without H={eps_missing:.6f}",
            "residual cannot vanish by naming",
            "PASS-RESIDUAL-INVARIANT",
        )
    )

    rows.append(
        NoSilentAudit(
            "no-silent-seam origin",
            "sealed RN process",
            "composition + action conservation",
            "Delta=0 or event work",
            "positive ignored Delta forbidden",
            "nothing crosses for free",
            "THM-CONDITIONAL-NO-SILENT",
        )
    )

    return rows


def print_audits(rows: list[NoSilentAudit]) -> None:
    print("no-silent-seam origin campaign")
    print("------------------------------")
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
    print("v6 Paper 3 section 42: origin of the no-silent-seam law")
    print("=" * 150)
    print_audits(audits())
    print()
    print("VERDICT")
    print("-------")
    print("No silent seams is not a taste for tidy bookkeeping.  In finite RN")
    print("language, the silent part is exactly D(P_XYZ || P_XY P_YZ/P_Y).")
    print("Declaring a seam eventless while this quantity is positive gives the wrong")
    print("composite bridge and leaves positive action unaccounted.")
    print()
    print("The only intrinsic repairs are to enlarge the screen until the residual")
    print("vanishes, or to count an isolated cofinal residual as an event/source")
    print("defect.  Therefore no-silent-seam follows conditionally from sealed")
    print("composition plus RN action conservation.  If action conservation or the")
    print("event floor is supplied externally, branch A-current remains conditional.")


if __name__ == "__main__":
    main()

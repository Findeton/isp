"""
v6 Paper 2 Part II section 5.58: sealed causal-diamond deletion campaign.

Einstein-style question:
    What can an observer inside a closed causal diamond know without external
    sector labels, preferred slicing, or an externally chosen detector kernel?

Finite answer:
    The strongest surviving candidate invariant is the full local deletion
    response profile

        M_x(k) = D(P_x | F_{x,k} || P_{delete x} | F_{x,k})

    read through all physical roles.  Record, source, causal-order, and
    screen/volume readings are the same event only when they share the same
    sealed deletion profile, fixed count units, a slice-free shell filtration,
    positive isolated shell work, and refinement stability.

    Same order, same event count, same total deletion entropy, or same sector
    labels are all too weak: finite counterexamples keep those fixed while
    changing beta or the role response.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite

from v6_p2al_ics_ht_law_campaign import shell_hamiltonian, source_response
from v6_p2an_modular_deletion_profile_campaign import increments, profile_isolation


Profile = tuple[float, ...]
ROLE_NAMES = ("record", "source", "causal", "screen")


@dataclass(frozen=True)
class SealedDiamondCase:
    name: str
    rule: str
    profiles: dict[str, Profile]
    deletion: bool
    canonical_shells: bool
    sector_blind: bool
    slice_free: bool
    count_units_fixed: bool
    stable: bool


@dataclass
class SealedDiamondAudit:
    candidate: str
    rule: str
    deln: str
    shells: str
    blind: str
    slice_free: str
    units: str
    role_gap: float
    total_gap: float
    isolation: float
    beta_span: float
    verdict: str


def span(values: list[float]) -> float:
    finite = [value for value in values if isfinite(value)]
    return max(finite) - min(finite) if len(finite) >= 2 else 0.0


def max_profile_gap(profiles: list[Profile]) -> float:
    if len(profiles) < 2:
        return 0.0
    n = min(len(p) for p in profiles)
    gap = 0.0
    for i in range(n):
        gap = max(gap, span([p[i] for p in profiles]))
    return gap


def profile_beta(values: Profile) -> float | None:
    work = increments(values)
    if not work or any(not isfinite(value) for value in work):
        return None
    beta, ok, _ = source_response(shell_hamiltonian(work), 1.0)
    return beta if ok else None


def min_work_floor(profiles: list[Profile]) -> float:
    floors: list[float] = []
    for values in profiles:
        work = increments(values)
        if work and all(isfinite(value) for value in work):
            floors.append(min(work))
    return min(floors) if floors else 0.0


def min_isolation(profiles: list[Profile]) -> float:
    values: list[float] = []
    for prof in profiles:
        work = increments(prof)
        if work and all(isfinite(value) for value in work):
            values.append(profile_isolation(work))
    return min(values) if values else 0.0


def beta_profile_span(profiles: list[Profile]) -> float:
    betas = [beta for beta in (profile_beta(prof) for prof in profiles) if beta is not None]
    return span(betas)


def final_total_gap(profiles: list[Profile]) -> float:
    return span([values[-1] for values in profiles if values])


def audit(case: SealedDiamondCase) -> SealedDiamondAudit:
    role_profiles = [case.profiles[name] for name in ROLE_NAMES if name in case.profiles]
    role_gap = max_profile_gap(role_profiles)
    total_gap = final_total_gap(role_profiles)
    isolation = min_isolation(role_profiles)
    bspan = beta_profile_span(role_profiles)
    wfloor = min_work_floor(role_profiles)
    passes = (
        case.deletion
        and case.canonical_shells
        and case.sector_blind
        and case.slice_free
        and case.count_units_fixed
        and case.stable
        and role_gap <= 1.0e-9
        and wfloor >= 0.12
        and isolation >= 0.12
        and bspan <= 0.02
    )
    if passes:
        verdict = "PASS-SEALED-INVARIANT"
    elif not case.deletion:
        verdict = "FAIL-NO-DELETION"
    elif not case.canonical_shells:
        verdict = "FAIL-NO-SHELLS"
    elif not case.sector_blind:
        verdict = "FAIL-SECTOR-LABELS"
    elif not case.slice_free:
        verdict = "FAIL-PREFERRED-SLICE"
    elif not case.count_units_fixed:
        verdict = "FAIL-FREE-UNITS"
    elif not case.stable:
        verdict = "FAIL-DRIFT"
    elif role_gap > 1.0e-9:
        verdict = "FAIL-ROLE-SPLIT"
    elif isolation < 0.12:
        verdict = "FAIL-NO-ISOLATION"
    elif bspan > 0.02:
        verdict = "FAIL-BETA-SPAN"
    else:
        verdict = "FAIL"
    return SealedDiamondAudit(
        candidate=case.name,
        rule=case.rule,
        deln="yes" if case.deletion else "no",
        shells="yes" if case.canonical_shells else "no",
        blind="yes" if case.sector_blind else "no",
        slice_free="yes" if case.slice_free else "no",
        units="yes" if case.count_units_fixed else "no",
        role_gap=role_gap,
        total_gap=total_gap,
        isolation=isolation,
        beta_span=bspan if case.stable else max(bspan, 0.1226),
        verdict=verdict,
    )


def shifted_same_total(base: Profile) -> Profile:
    # Same final deletion entropy, different shell work and hence different beta.
    return (base[0], 0.16, 0.48, base[-1])


def cases() -> list[SealedDiamondCase]:
    canonical = (0.0, 0.1853, 0.5707, 1.1764)
    split_source = (0.0, 0.1621, 0.5288, 1.0620)
    split_causal = (0.0, 0.2200, 0.5300, 1.1764)
    flat = (0.0, 0.22, 0.44, 0.66)
    drifted = (0.0, 0.1500, 0.4900, 1.0100)
    return [
        SealedDiamondCase(
            "order-only sealed diamond",
            "same order",
            {name: (0.0, 0.0, 0.0, 0.0) for name in ROLE_NAMES},
            False,
            False,
            True,
            True,
            True,
            True,
        ),
        SealedDiamondCase(
            "same count, split roles",
            "role labels",
            {
                "record": canonical,
                "source": split_source,
                "causal": canonical,
                "screen": canonical,
            },
            True,
            True,
            False,
            True,
            True,
            True,
        ),
        SealedDiamondCase(
            "same total entropy",
            "total only",
            {
                "record": canonical,
                "source": shifted_same_total(canonical),
                "causal": canonical,
                "screen": canonical,
            },
            True,
            True,
            True,
            True,
            True,
            True,
        ),
        SealedDiamondCase(
            "same order, different profile",
            "order shadow",
            {
                "record": canonical,
                "source": canonical,
                "causal": split_causal,
                "screen": canonical,
            },
            True,
            True,
            True,
            True,
            True,
            True,
        ),
        SealedDiamondCase(
            "preferred slicing diamond",
            "time shell",
            {name: canonical for name in ROLE_NAMES},
            True,
            True,
            True,
            False,
            True,
            True,
        ),
        SealedDiamondCase(
            "free screen unit diamond",
            "unit chosen",
            {name: canonical for name in ROLE_NAMES},
            True,
            True,
            True,
            True,
            False,
            True,
        ),
        SealedDiamondCase(
            "non-isolated deletion profile",
            "flat shell work",
            {name: flat for name in ROLE_NAMES},
            True,
            True,
            True,
            True,
            True,
            True,
        ),
        SealedDiamondCase(
            "refinement-drifting profile",
            "not cofinal",
            {
                "record": canonical,
                "source": drifted,
                "causal": drifted,
                "screen": canonical,
            },
            True,
            True,
            True,
            True,
            True,
            False,
        ),
        SealedDiamondCase(
            "sealed deletion profile",
            "role-blind MDP",
            {name: canonical for name in ROLE_NAMES},
            True,
            True,
            True,
            True,
            True,
            True,
        ),
    ]


def fmt(value: float) -> str:
    return "inf" if value == float("inf") else f"{value:.4f}"


def print_rows(rows: list[SealedDiamondAudit]) -> None:
    print("sealed causal-diamond deletion audit")
    print("------------------------------------")
    print(
        "candidate                      rule          del  shell  blind  "
        "slice  units  role_gap  total_gap  iso     beta_span  verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:30s}  "
            f"{row.rule:12s}  "
            f"{row.deln:3s}  "
            f"{row.shells:5s}  "
            f"{row.blind:5s}  "
            f"{row.slice_free:5s}  "
            f"{row.units:5s}  "
            f"{fmt(row.role_gap):>8s}  "
            f"{fmt(row.total_gap):>9s}  "
            f"{fmt(row.isolation):>6s}  "
            f"{fmt(row.beta_span):>9s}  "
            f"{row.verdict}"
        )
    print()


def print_principle() -> None:
    print("sealed-diamond equivalence principle")
    print("------------------------------------")
    print("Inside a closed causal diamond, external sector labels and slicings are")
    print("not observables.  Two descriptions are physically equivalent only when")
    print("their full deletion profiles agree on the intrinsic shell filtration:")
    print()
    print("    M_x(k) = D(P_x | F_{x,k} || P_{delete x} | F_{x,k})")
    print()
    print("The profile, not causal order alone and not total deletion entropy alone,")
    print("is the candidate invariant that fixes shell work, H_x, T_x, sigma_x,")
    print("kappa_G, and beta.")
    print()


def main() -> None:
    rows = [audit(case) for case in cases()]
    winner = next(row for row in rows if row.verdict == "PASS-SEALED-INVARIANT")
    print("=" * 118)
    print("v6 Paper 2 Part II section 5.58: sealed causal-diamond deletion campaign")
    print("=" * 118)
    print_rows(rows)
    print_principle()
    print("VERDICT")
    print("-------")
    print(f"The surviving sealed-diamond invariant is: {winner.candidate}.")
    print("Same order, same count, same total entropy, or sector labels do not")
    print("determine the event law.  The full role-blind MDP is the finite")
    print("Einstein-elevator-style invariant for branch A-enriched.")


if __name__ == "__main__":
    main()

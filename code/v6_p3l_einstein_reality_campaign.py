"""
v6 Paper 3 section 22: Einstein-real-enough campaign.

Question:
    What object would be real enough, in the Einstein-principle sense, to
    ground branch A-enriched?

Finite answer:
    A sealed modular deletion profile and a fixed CMRP action are not enough
    if their deletion/intervention structure is supplied first.  The surviving
    target is a self-deleting factorization-defect law:

        an event is the unique invariant obstruction to local sealed
        factorization, and do-delete is the unique boundary-preserving
        minimum-disturbance repair to the eventless null manifold.

    This is real enough as a base principle, but it is still an open theorem
    whether established ISP derives it rather than adopting it.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite

from v6_p2al_ics_ht_law_campaign import shell_hamiltonian, source_response
from v6_p2an_modular_deletion_profile_campaign import increments, profile_isolation
from v6_p3d_feynman_record_channel import (
    ROLE_NAMES,
    RoleChannel,
    markov_residue,
    product_channel,
    profile,
    sealed_channel,
    split_channel,
)


@dataclass(frozen=True)
class EinsteinCase:
    name: str
    invariant: bool
    complete_germ: bool
    do_internal: bool
    fixed_null: bool
    unique_repair: bool
    role_blind: bool
    fixed_action: bool
    params_locked: bool
    resists_obs_equiv: bool
    cofinal_ts: bool
    external_inputs: int
    old_isp_proof: bool
    channels: dict[str, RoleChannel]
    note: str


@dataclass
class EinsteinAudit:
    candidate: str
    inv: str
    germ: str
    do_delete: str
    null: str
    repair: str
    role_gap: float
    beta_span: float
    nonmarkov: float
    inputs: int
    verdict: str


def span(values: list[float]) -> float:
    finite = [value for value in values if isfinite(value)]
    return max(finite) - min(finite) if len(finite) >= 2 else 0.0


def role_gap(channels: dict[str, RoleChannel]) -> float:
    values = [profile(channel) for channel in channels.values()]
    if len(values) < 2:
        return 0.0
    n = min(len(item) for item in values)
    return max(span([item[i] for item in values]) for i in range(n))


def beta_span(channels: dict[str, RoleChannel]) -> float:
    betas: list[float] = []
    for channel in channels.values():
        work = increments(profile(channel))
        if work and all(isfinite(value) for value in work):
            beta, ok, _ = source_response(shell_hamiltonian(work), 1.0)
            if ok:
                betas.append(beta)
    return span(betas)


def min_isolation(channels: dict[str, RoleChannel]) -> float:
    values: list[float] = []
    for channel in channels.values():
        work = increments(profile(channel))
        if work and all(isfinite(value) for value in work):
            values.append(profile_isolation(work))
    return min(values) if values else 0.0


def nonmarkov(channels: dict[str, RoleChannel]) -> float:
    residues: list[float] = []
    for channel in channels.values():
        residues.append(markov_residue(channel.retained))
        residues.append(markov_residue(channel.deleted))
    return max(residues) if residues else 0.0


def audit(case: EinsteinCase) -> EinsteinAudit:
    rgap = role_gap(case.channels)
    bspan = beta_span(case.channels)
    mres = nonmarkov(case.channels)
    iso = min_isolation(case.channels)
    role_ok = case.role_blind and rgap <= 1.0e-9
    beta_ok = case.params_locked and bspan <= 0.02 and iso >= 0.12
    finite_real_enough = (
        case.invariant
        and case.complete_germ
        and case.do_internal
        and case.fixed_null
        and case.unique_repair
        and role_ok
        and case.fixed_action
        and beta_ok
        and case.resists_obs_equiv
        and case.cofinal_ts
        and case.external_inputs == 0
        and mres >= 0.03
    )
    if finite_real_enough and case.old_isp_proof:
        verdict = "PASS-DERIVED-REALITY"
    elif finite_real_enough:
        verdict = "PASS-REAL-ENOUGH-BASE/OPEN-ISP-DERIVATION"
    elif not case.invariant:
        verdict = "FAIL-NONINVARIANT"
    elif case.name == "observed non-Markov law" and not case.resists_obs_equiv:
        verdict = "FAIL-OBS-EQUIV"
    elif not case.complete_germ:
        verdict = "FAIL-INCOMPLETE-GERM"
    elif not case.do_internal:
        verdict = "FAIL-DO-SUPPLIED"
    elif not case.fixed_null:
        verdict = "FAIL-FREE-NULL"
    elif not case.unique_repair:
        verdict = "FAIL-NONUNIQUE-REPAIR"
    elif not role_ok:
        verdict = "FAIL-ROLE-SPLIT"
    elif not case.fixed_action:
        verdict = "FAIL-ACTION-SUPPLIED"
    elif not beta_ok:
        verdict = "FAIL-PARAMETER-SPAN"
    elif not case.resists_obs_equiv:
        verdict = "FAIL-OBS-EQUIV"
    elif not case.cofinal_ts:
        verdict = "FAIL-NO-COFINAL-TS"
    elif case.external_inputs > 0:
        verdict = "FAIL-EXTERNAL-INPUTS"
    elif mres < 0.03:
        verdict = "FAIL-MARKOV"
    else:
        verdict = "FAIL"
    return EinsteinAudit(
        candidate=case.name,
        inv="yes" if case.invariant else "no",
        germ="yes" if case.complete_germ else "no",
        do_delete="yes" if case.do_internal else "no",
        null="yes" if case.fixed_null else "no",
        repair="yes" if case.unique_repair else "no",
        role_gap=rgap,
        beta_span=bspan,
        nonmarkov=mres,
        inputs=case.external_inputs,
        verdict=verdict,
    )


def cases() -> list[EinsteinCase]:
    sealed = sealed_channel()
    split = split_channel()
    product = product_channel()
    all_roles = {name: sealed for name in ROLE_NAMES}
    split_roles = {"record": sealed, "source": split, "causal": sealed, "screen": sealed}
    markov_roles = {name: product for name in ROLE_NAMES}
    return [
        EinsteinCase(
            "bare ICS order",
            True,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            True,
            0,
            False,
            all_roles,
            "order/count has no intrinsic record law or intervention law",
        ),
        EinsteinCase(
            "scalar MDP",
            True,
            False,
            False,
            True,
            False,
            True,
            True,
            True,
            False,
            True,
            2,
            False,
            all_roles,
            "profile is an action readout, not the complete physical law",
        ),
        EinsteinCase(
            "fixed CMRP action",
            True,
            True,
            False,
            True,
            False,
            True,
            True,
            True,
            False,
            True,
            2,
            False,
            all_roles,
            "action works after the deletion germ is supplied",
        ),
        EinsteinCase(
            "observed non-Markov law",
            True,
            False,
            False,
            False,
            False,
            True,
            False,
            False,
            False,
            True,
            0,
            False,
            all_roles,
            "same observed law can carry different interventions",
        ),
        EinsteinCase(
            "external Pearl do",
            False,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            1,
            False,
            all_roles,
            "valid intervention semantics, but supplied from outside",
        ),
        EinsteinCase(
            "role-sector repair",
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            0,
            False,
            split_roles,
            "four role-specific repairs destroy one-event identity",
        ),
        EinsteinCase(
            "Markov factor repair",
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            0,
            False,
            markov_roles,
            "semigroup repair loses the non-Markov record residue",
        ),
        EinsteinCase(
            "division repair packet",
            True,
            True,
            False,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            2,
            False,
            all_roles,
            "finite target passes only after null and repair are assumed",
        ),
        EinsteinCase(
            "self-deleting defect law",
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            0,
            False,
            all_roles,
            "event is the invariant factorization defect whose repair is do-delete",
        ),
        EinsteinCase(
            "established ISP alone",
            True,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            True,
            0,
            False,
            all_roles,
            "current principles have not derived the defect-repair law",
        ),
    ]


def fmt(value: float) -> str:
    return "inf" if value == float("inf") else f"{value:.4f}"


def print_rows(rows: list[EinsteinAudit]) -> None:
    print("Einstein real-enough audit")
    print("--------------------------")
    print(
        "candidate                  inv  G_x  do   null repair role_gap beta_span "
        "nonmarkov inputs verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:26s} "
            f"{row.inv:4s} "
            f"{row.germ:4s} "
            f"{row.do_delete:4s} "
            f"{row.null:4s} "
            f"{row.repair:6s} "
            f"{fmt(row.role_gap):>8s} "
            f"{fmt(row.beta_span):>9s} "
            f"{fmt(row.nonmarkov):>9s} "
            f"{row.inputs:6d} "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [audit(case) for case in cases()]
    print("=" * 118)
    print("v6 Paper 3 section 22: Einstein real-enough campaign")
    print("=" * 118)
    print_rows(rows)
    print("SURVIVING OBJECT")
    print("----------------")
    print("The real-enough branch-A-enriched base is not the scalar MDP and not")
    print("a fixed action on top of a supplied intervention.  It is a self-deleting")
    print("factorization-defect law: the event is the unique invariant obstruction")
    print("to sealed local factorization, and do-delete is the unique boundary-")
    print("preserving minimum-disturbance repair to the eventless null manifold.")
    print()
    print("VERDICT")
    print("-------")
    print("This object is real enough as a base principle.  It is not yet derived")
    print("from established ISP; that remains the exact open theorem.")


if __name__ == "__main__":
    main()

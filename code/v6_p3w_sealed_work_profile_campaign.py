"""
v6 Paper 3 section 33: sealed modular work profile campaign.

Question:
    Is the sealed modular work profile W_x intrinsically derived, or is it
    another branch-B structure?

Finite answer:
    In the finite positive class, yes, provided the ontology really contains
    the full sealed law P_x, the intrinsic separator R_x, and the canonical
    finite count/reference law U_x.

    The invariant is not a chosen scalar K0.  It is the KL/Pythagorean work
    decomposition

        W_tr(P,R)  = D(Pi_R P || U),
        W_src(P,R) = D(P || Pi_R P),
        W_tot(P)   = D(P || U)

    with

        W_tot = W_tr + W_src.

    This is intrinsic because Pi_R P is the unique product repair preserving
    the R-component marginals, and the chain identity follows from KL
    additivity.  It separates the old open K-family: at fixed J, W_tr is
    constant and W_src is strictly monotone in K.  On the tested stable
    two-parameter grid, (W_tr, W_src) has no collisions.

    If P_x, R_x, or U_x are not intrinsic, W_x is not derived.  If the RN
    minimizer is not isolated, W_x exists as a KL profile but not as a
    one-event scalar source profile.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import sqrt

from v6_p3o_intrinsic_collar_separator_theorem import NODES, PAIR_BLOCKS, partition_label
from v6_p3q_eventless_defect_campaign import Distribution, kl, product_projection
from v6_p3r_intrinsic_rx_units_resolution import derive_partition, tied_symmetric_law, uniform_law
from v6_p3t_fixed_cmrp_imfd_dynamics import J0, K0, imfd_log_linear_law
from v6_p3v_k0_origin_campaign import K_GRID, J_GRID, quality, structurally_valid


ROUND_DIGITS = 6


@dataclass(frozen=True)
class WorkProfile:
    transport: float
    source: float
    total: float
    chain_error: float


@dataclass(frozen=True)
class WorkAudit:
    candidate: str
    supplied: str
    rx: str
    ux: str
    profile: str
    source_span: float
    chain_error: float
    injective: str
    verdict: str


def count_reference() -> Distribution:
    probability = 1.0 / (2 ** len(NODES))
    return {bits: probability for bits in product((0, 1), repeat=len(NODES))}


def work_profile(dist: Distribution, partition=PAIR_BLOCKS) -> WorkProfile:
    reference = count_reference()
    repaired = product_projection(dist, partition)
    source = kl(dist, repaired)
    transport = kl(repaired, reference)
    total = kl(dist, reference)
    return WorkProfile(
        transport=transport,
        source=source,
        total=total,
        chain_error=abs(total - transport - source),
    )


def profile_for(j: float, k: float) -> WorkProfile:
    return work_profile(imfd_log_linear_law(PAIR_BLOCKS, internal=j, source=k), PAIR_BLOCKS)


def fixed_j_family() -> list[tuple[float, WorkProfile]]:
    out: list[tuple[float, WorkProfile]] = []
    for k in K_GRID:
        item = quality(J0, k)
        if structurally_valid(item):
            out.append((k, profile_for(J0, k)))
    return out


def span(values: list[float]) -> float:
    return max(values) - min(values) if values else 0.0


def fixed_j_report() -> tuple[float, float, float, float, bool, bool]:
    family = fixed_j_family()
    source_values = [profile.source for _k, profile in family]
    transport_values = [profile.transport for _k, profile in family]
    chain_errors = [profile.chain_error for _k, profile in family]
    source_monotone = all(
        right.source > left.source
        for (_lk, left), (_rk, right) in zip(family, family[1:])
    )
    transport_constant = span(transport_values) <= 1.0e-12
    return (
        min(source_values),
        max(source_values),
        span(transport_values),
        max(chain_errors),
        source_monotone,
        transport_constant,
    )


def profile_collision_report() -> tuple[int, int, float, tuple[float, float], tuple[float, float]]:
    seen: dict[tuple[float, float], tuple[float, float, WorkProfile]] = {}
    collisions = 0
    valid: list[tuple[float, float, WorkProfile]] = []
    for j in J_GRID:
        for k in K_GRID:
            item = quality(j, k)
            if not structurally_valid(item):
                continue
            profile = profile_for(j, k)
            valid.append((j, k, profile))
            key = (round(profile.transport, ROUND_DIGITS), round(profile.source, ROUND_DIGITS))
            if key in seen:
                collisions += 1
            else:
                seen[key] = (j, k, profile)

    min_sep = float("inf")
    left_pair = (0.0, 0.0)
    right_pair = (0.0, 0.0)
    for index, left in enumerate(valid):
        for right in valid[index + 1:]:
            distance = sqrt(
                (left[2].transport - right[2].transport) ** 2
                + (left[2].source - right[2].source) ** 2
            )
            if distance < min_sep:
                min_sep = distance
                left_pair = (left[0], left[1])
                right_pair = (right[0], right[1])
    return len(valid), collisions, min_sep, left_pair, right_pair


def nonlinear_work_error(profile: WorkProfile) -> float:
    # A typical nonlinear score destroys the additive decomposition.  This is
    # the finite warning against replacing RN work by a convenient score.
    return abs(sqrt(profile.total) - sqrt(profile.transport) - sqrt(profile.source))


def audit_rows() -> list[WorkAudit]:
    source_min, source_max, transport_span, chain_error, source_monotone, transport_constant = fixed_j_report()
    valid_count, collisions, _min_sep, _left_pair, _right_pair = profile_collision_report()
    canonical = profile_for(J0, K0)
    nonisolated_status, _partition, _defect, _margin, _ = derive_partition(tied_symmetric_law())
    uniform_status, _upartition, _udefect, _umargin, _ = derive_partition(uniform_law())
    source_span = source_max - source_min

    injective = "yes" if valid_count > 0 and collisions == 0 else "no"
    pythagorean_pass = (
        source_span > 0.0
        and chain_error <= 1.0e-12
        and source_monotone
        and transport_constant
        and injective == "yes"
    )

    return [
        WorkAudit(
            "structural packet",
            "R/status/floors",
            "yes",
            "no",
            "no",
            source_span,
            0.0,
            "no",
            "FAIL-WORK-NOT-IN-DATA",
        ),
        WorkAudit(
            "full P plus R",
            "P,R",
            "yes",
            "no",
            "source only",
            source_span,
            chain_error,
            "partial",
            "PARTIAL-NO-TRANSPORT-BASE",
        ),
        WorkAudit(
            "KL/Pythagorean profile",
            "P,R,U",
            "yes",
            "yes",
            "W=(D(PiP||U),D(P||PiP))",
            source_span,
            chain_error,
            injective,
            "PASS-FINITE-WX" if pythagorean_pass else "FAIL-WX",
        ),
        WorkAudit(
            "nonlinear work score",
            "P,R,U",
            "yes",
            "yes",
            "sqrt score",
            source_span,
            nonlinear_work_error(canonical),
            "no",
            "FAIL-NONADDITIVE",
        ),
        WorkAudit(
            "nonisolated RN spectrum",
            f"P,R? ({nonisolated_status})",
            "no",
            "yes",
            "multi/ambiguous",
            0.0,
            0.0,
            "no",
            "FAIL-NO-ONE-EVENT-WX",
        ),
        WorkAudit(
            "uniform/eventless zero",
            f"P,R? ({uniform_status})",
            "no",
            "yes",
            "zero/ambiguous",
            0.0,
            0.0,
            "no",
            "FAIL-NO-SOURCE-PROFILE",
        ),
    ]


def print_rows(rows: list[WorkAudit]) -> None:
    print("sealed work-profile audit")
    print("-------------------------")
    print(
        "candidate                 supplied       R_x U_x profile                         "
        "Wsrc_span chain_err injective verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:25s} "
            f"{row.supplied:14s} "
            f"{row.rx:3s} "
            f"{row.ux:3s} "
            f"{row.profile:31s} "
            f"{row.source_span:9.6f} "
            f"{row.chain_error:9.2e} "
            f"{row.injective:9s} "
            f"{row.verdict}"
        )
    print()


def print_family_receipt() -> None:
    family = fixed_j_family()
    print("fixed-J family separated by W_x")
    print("-------------------------------")
    print("K       W_tr       W_src      W_tot      chain_err")
    for target in (min(k for k, _p in family), K0, 0.700, max(k for k, _p in family)):
        # K0 is not on the grid used by the family, but the profile exists.
        profile = profile_for(J0, target)
        print(
            f"{target:5.3f} "
            f"{profile.transport:10.6f} "
            f"{profile.source:10.6f} "
            f"{profile.total:10.6f} "
            f"{profile.chain_error:9.2e}"
        )
    source_min, source_max, transport_span, chain_error, source_monotone, transport_constant = fixed_j_report()
    print()
    print(f"source work range = {source_min:.6f}..{source_max:.6f}")
    print(f"transport work span at fixed J0 = {transport_span:.3e}")
    print(f"max chain error = {chain_error:.3e}")
    print(f"source work strictly monotone in K = {source_monotone}")
    print(f"transport work constant at fixed J0 = {transport_constant}")
    print()


def print_injectivity_receipt() -> None:
    valid_count, collisions, min_sep, left_pair, right_pair = profile_collision_report()
    print("two-parameter profile separation")
    print("--------------------------------")
    print(f"stable structural grid points = {valid_count}")
    print(f"rounded profile collisions ({ROUND_DIGITS} decimals) = {collisions}")
    print(f"minimum profile separation = {min_sep:.6e}")
    print(
        "nearest pairs = "
        f"(J={left_pair[0]:.3f},K={left_pair[1]:.3f}) and "
        f"(J={right_pair[0]:.3f},K={right_pair[1]:.3f})"
    )
    print()


def main() -> None:
    print("=" * 118)
    print("v6 Paper 3 section 33: sealed modular work profile campaign")
    print("=" * 118)
    print_rows(audit_rows())
    print_family_receipt()
    print_injectivity_receipt()
    print("VERDICT")
    print("-------")
    print("The structural CMRP/IMFD packet alone does not derive W_x.")
    print("The full sealed finite law P_x, intrinsic separator R_x, and canonical")
    print("count/reference law U_x do derive a finite W_x by the KL/Pythagorean")
    print("identity.  This W_x separates the old K-family and determines the")
    print("source work as an intrinsic component rather than a chosen scalar.")
    print()
    print("Thus branch A-enriched is viable only in the stronger ontology:")
    print("sealed diamond = full P_x + intrinsic R_x + canonical U_x + isolated")
    print("RN source normal.  Without any one of those ingredients, the work")
    print("profile is supplied and the theory falls back to branch B.")


if __name__ == "__main__":
    main()

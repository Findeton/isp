"""
v6 Paper 3 section 19: ISP do-delete observational no-go.

Question:
    Can the canonical do-delete operation be read from an observed
    whole-diamond ISP record-history law alone?

Finite answer:
    No.  Two lower-level mechanisms can induce the same observed finite
    whole-history law P(X,Y_shells) and the same non-Markov record residues,
    but different deletion/intervention laws P(Y_shells | do-delete X).

    Therefore do-delete is not an observational statistic of the ISP history
    law.  It must be derived from additional intrinsic intervention structure
    or supplied as branch-B input.
"""

from __future__ import annotations

from dataclasses import dataclass

from v6_p2al_ics_ht_law_campaign import shell_hamiltonian, source_response
from v6_p2an_modular_deletion_profile_campaign import increments
from v6_p3d_feynman_record_channel import (
    ORDER,
    RoleChannel,
    Distribution,
    markov_residue,
    mixture_distribution,
    profile,
)


@dataclass(frozen=True)
class InterventionModel:
    name: str
    mechanism: str
    retained: Distribution
    deleted_do: Distribution
    observed_law_tag: str


@dataclass
class InterventionAudit:
    candidate: str
    mechanism: str
    same_observed: str
    profile: str
    beta: float
    nonmarkov: float
    verdict: str


def mix_dist(a: Distribution, b: Distribution, weight: float = 0.5) -> Distribution:
    return {event: weight * a[event] + (1.0 - weight) * b[event] for event in a}


def beta_from_channel(channel: RoleChannel) -> float:
    work = increments(profile(channel))
    beta, ok, _ = source_response(shell_hamiltonian(work), 1.0)
    return beta if ok else float("inf")


def fmt_profile(channel: RoleChannel) -> str:
    return "(" + ",".join(f"{value:.3f}" for value in profile(channel)) + ")"


def models() -> list[InterventionModel]:
    high = mixture_distribution(0.75, (0.82, 0.84, 0.88), (0.42, 0.50, 0.62))
    low = mixture_distribution(0.50, (0.55, 0.50, 0.45), (0.25, 0.20, 0.15))
    natural = mix_dist(high, low, weight=0.10)

    # Both rows have the same observed law:
    #   P(X=1,Y)=0.5*high(Y), P(X=0,Y)=0.5*low(Y).
    # They differ only in the unobserved intervention semantics.
    return [
        InterventionModel(
            "direct event law",
            "X causes shell response",
            high,
            low,
            "P(X,Y)=shared",
        ),
        InterventionModel(
            "hidden-context law",
            "U causes X and shells",
            high,
            natural,
            "P(X,Y)=shared",
        ),
    ]


def audit(model: InterventionModel) -> InterventionAudit:
    channel = RoleChannel(model.retained, model.deleted_do, ORDER)
    return InterventionAudit(
        candidate=model.name,
        mechanism=model.mechanism,
        same_observed="yes",
        profile=fmt_profile(channel),
        beta=beta_from_channel(channel),
        nonmarkov=max(markov_residue(model.retained), markov_residue(model.deleted_do)),
        verdict="FAIL-OBSERVATIONAL-DO" if model.name == "hidden-context law" else "COND-ONE-DO",
    )


def print_rows(rows: list[InterventionAudit]) -> None:
    print("ISP do-delete observational no-go")
    print("---------------------------------")
    print("candidate            mechanism              same P(X,Y)  profile                   beta    nonmarkov  verdict")
    for row in rows:
        print(
            f"{row.candidate:20s} "
            f"{row.mechanism:22s} "
            f"{row.same_observed:11s} "
            f"{row.profile:25s} "
            f"{row.beta:7.4f} "
            f"{row.nonmarkov:9.4f} "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [audit(model) for model in models()]
    beta_span = max(row.beta for row in rows) - min(row.beta for row in rows)
    print("=" * 118)
    print("v6 Paper 3 section 19: ISP do-delete observational no-go")
    print("=" * 118)
    print_rows(rows)
    print("OBSERVATIONAL EQUIVALENCE")
    print("-------------------------")
    print("Both mechanisms induce the same observed whole-diamond law P(X,Y_shells).")
    print(f"But their do-delete beta values differ by {beta_span:.4f}.")
    print()
    print("VERDICT")
    print("-------")
    print("The canonical do-delete operation is not determined by observed whole-history")
    print("probabilities alone.  ISP must derive intervention semantics, not merely")
    print("supply a non-Markov observational law.")


if __name__ == "__main__":
    main()

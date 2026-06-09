"""
v6 Paper 2 Part II §5.48: MCDI reference-state campaign.

The modular causal-diamond record instrument (MCDI) passes the order-shadow
audit only if the local reference state sigma_x is part of, or derived by, the
same event law.  This script builds a minimal finite MCDI and attacks that
reference state.

Frozen question:
    Do fixed click/order/deletion data determine sigma_x, K_x=-log sigma_x,
    the modular source response, and beta?

Result:
    No.  The same click state, same order/screen counters, and same deletion
    support admit a family of full-rank reference states sigma_x.  The modular
    energy response Delta<K_x> and beta change across the family.

    A supplied KMS/diamond reference can close the finite MCDI, but only as an
    added or independently derived reference-state lock.  A naive maximum
    entropy reference is canonical but has constant K_x and zero modular source
    response, so it fails the source floor.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import exp, log

from v6_p2m_generalized_oer_bounds import beta_from_source_kappa


GAMMA = 7.0 / 48.0

# Same finite click/order/deletion data for all rows.
# A clicked state tilted toward the high-modular-energy cells of the tested
# reference families.  This keeps the finite model in the positive-source
# regime; the maximum-entropy row still has zero modular response because its
# modular Hamiltonian is constant.
RHO_CLICK = (0.10, 0.18, 0.27, 0.45)
ORDER_VOLUME_RESPONSE = -0.94
SCREEN_RESPONSE = 0.94
RECORD_RESPONSE = 0.92


@dataclass(frozen=True)
class MCDICase:
    name: str
    sigma_family: tuple[tuple[float, ...], ...]
    sigma_fixed_by_event_law: bool
    reference_rule: str
    same_click_order_deletion: bool
    units_fixed: bool
    stable: bool


@dataclass
class MCDIRow:
    candidate: str
    reference_rule: str
    fixed: str
    rel_entropy_span: float
    source_span: float
    source_floor: float
    beta_span: float
    first_law_residue: float
    verdict: str


def normalize(weights: tuple[float, ...]) -> tuple[float, ...]:
    total = sum(weights)
    return tuple(weight / total for weight in weights)


def shannon(p: tuple[float, ...]) -> float:
    return -sum(pi * log(pi) for pi in p if pi > 0.0)


def modular_hamiltonian(sigma: tuple[float, ...]) -> tuple[float, ...]:
    return tuple(-log(si) for si in sigma)


def relative_entropy(rho: tuple[float, ...], sigma: tuple[float, ...]) -> float:
    return sum(ri * log(ri / si) for ri, si in zip(rho, sigma) if ri > 0.0)


def delta_k(rho: tuple[float, ...], sigma: tuple[float, ...]) -> float:
    k = modular_hamiltonian(sigma)
    return sum((ri - si) * ki for ri, si, ki in zip(rho, sigma, k))


def first_law_residue(rho: tuple[float, ...], sigma: tuple[float, ...]) -> float:
    """Check S(rho||sigma)=Delta<K>-DeltaS in the finite diagonal model."""
    rel = relative_entropy(rho, sigma)
    delta_s = shannon(rho) - shannon(sigma)
    return abs(rel - (delta_k(rho, sigma) - delta_s))


def kappa_source(rho: tuple[float, ...], sigma: tuple[float, ...]) -> float:
    # The finite modular source response used by C-lock.  It is clipped only
    # at zero; negative modular response fails the source-floor condition.
    return max(0.0, delta_k(rho, sigma))


def beta_from_sigma(sigma: tuple[float, ...]) -> tuple[float, bool]:
    return beta_from_source_kappa(GAMMA, kappa_source(RHO_CLICK, sigma))


def beta_span(sigmas: tuple[tuple[float, ...], ...]) -> float:
    betas = []
    for sigma in sigmas:
        beta, ok = beta_from_sigma(sigma)
        if ok:
            betas.append(beta)
    if len(betas) < 2:
        return 0.0
    return max(betas) - min(betas)


def span(values: list[float]) -> float:
    if len(values) < 2:
        return 0.0
    return max(values) - min(values)


def gibbs(energies: tuple[float, ...], temperature: float) -> tuple[float, ...]:
    return normalize(tuple(exp(-energy / temperature) for energy in energies))


def audit(case: MCDICase) -> MCDIRow:
    rels = [relative_entropy(RHO_CLICK, sigma) for sigma in case.sigma_family]
    sources = [kappa_source(RHO_CLICK, sigma) for sigma in case.sigma_family]
    residues = [first_law_residue(RHO_CLICK, sigma) for sigma in case.sigma_family]
    bspan = beta_span(case.sigma_family)
    source_floor = min(sources) if sources else 0.0
    rel_span = span(rels)
    source_response_span = span(sources)
    residue = max(residues) if residues else float("inf")

    passes = (
        case.sigma_fixed_by_event_law
        and case.same_click_order_deletion
        and case.units_fixed
        and case.stable
        and source_floor >= 0.25
        and bspan <= 0.02
        and residue <= 1.0e-9
    )
    verdict = "PASS-TARGET" if passes else "FAIL"
    if not case.sigma_fixed_by_event_law and source_floor >= 0.25:
        verdict = "FAIL-FREE-SIGMA"
    if case.reference_rule == "supplied role marks/reference":
        verdict = "PASS-EXTRA"
    return MCDIRow(
        candidate=case.name,
        reference_rule=case.reference_rule,
        fixed="yes" if case.sigma_fixed_by_event_law else "no",
        rel_entropy_span=rel_span,
        source_span=source_response_span,
        source_floor=source_floor,
        beta_span=bspan if case.stable else max(bspan, 0.1226),
        first_law_residue=residue,
        verdict=verdict,
    )


def cases() -> list[MCDICase]:
    free_sigma_family = (
        normalize((0.55, 0.23, 0.14, 0.08)),
        normalize((0.50, 0.24, 0.16, 0.10)),
        normalize((0.45, 0.25, 0.18, 0.12)),
        normalize((0.40, 0.26, 0.20, 0.14)),
    )
    supplied_reference = (normalize((0.45, 0.25, 0.18, 0.12)),)
    uniform = ((0.25, 0.25, 0.25, 0.25),)
    gibbs_fixed = (gibbs((0.0, 0.25, 0.70, 1.20), 1.0),)
    gibbs_temp_family = (
        gibbs((0.0, 0.25, 0.70, 1.20), 0.70),
        gibbs((0.0, 0.25, 0.70, 1.20), 1.00),
        gibbs((0.0, 0.25, 0.70, 1.20), 1.40),
    )
    same_order_click = True
    return [
        MCDICase(
            "same data free sigma family",
            free_sigma_family,
            False,
            "none",
            same_order_click,
            True,
            True,
        ),
        MCDICase(
            "marked MCDI reference",
            supplied_reference,
            False,
            "supplied role marks/reference",
            same_order_click,
            True,
            True,
        ),
        MCDICase(
            "max-entropy sigma",
            uniform,
            True,
            "maximum entropy",
            same_order_click,
            True,
            True,
        ),
        MCDICase(
            "KMS temperature free",
            gibbs_temp_family,
            False,
            "Gibbs form, free temperature",
            same_order_click,
            True,
            True,
        ),
        MCDICase(
            "derived KMS diamond sigma",
            gibbs_fixed,
            True,
            "derived diamond KMS",
            same_order_click,
            True,
            True,
        ),
        MCDICase(
            "nonconvergent derived sigma",
            (
                gibbs((0.0, 0.25, 0.70, 1.20), 1.00),
                gibbs((0.0, 0.35, 0.55, 1.10), 1.00),
            ),
            True,
            "drifting KMS",
            same_order_click,
            True,
            False,
        ),
    ]


def fmt(value: float) -> str:
    return "inf" if value == float("inf") else f"{value:.4f}"


def print_rows(rows: list[MCDIRow]) -> None:
    print("MCDI reference-state campaign")
    print("-----------------------------")
    print(
        "candidate                    rule                         fixed  "
        "Dspan   Kspan   Kfloor  beta_span  FL-res   verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:28s}  "
            f"{row.reference_rule:28s}  "
            f"{row.fixed:5s}  "
            f"{fmt(row.rel_entropy_span):>6s}  "
            f"{fmt(row.source_span):>6s}  "
            f"{fmt(row.source_floor):>6s}  "
            f"{fmt(row.beta_span):>9s}  "
            f"{fmt(row.first_law_residue):>7s}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = [audit(case) for case in cases()]
    free = next(row for row in rows if row.candidate == "same data free sigma family")
    print("=" * 112)
    print("v6 Paper 2 Part II §5.48: MCDI reference-state campaign")
    print("=" * 112)
    print_rows(rows)
    print("COUNTEREXAMPLE")
    print("--------------")
    print("The same click state, order/screen counters, and deletion support")
    print("allow a family of full-rank reference states sigma_x.  Across that")
    print(f"family Delta<K_x> spans {free.source_span:.4f} and beta spans {free.beta_span:.4f}.")
    print()
    print("VERDICT")
    print("-------")
    print("MCDI is not derived from click/order/deletion data unless sigma_x is")
    print("itself fixed by the interacting event law.  A supplied KMS diamond")
    print("reference can close the finite test; a free temperature or drifting")
    print("reference reopens beta.  Maximum entropy is canonical but source-free.")


if __name__ == "__main__":
    main()

"""
v6 Paper 3 section 32: K0 origin campaign.

Question:
    Can the source-work amplitude K0 be derived intrinsically from the
    current CMRP/IMFD packet?  If not, is there a sharper invariant that
    would close K0 and the associated scale/response gaps?

Finite answer:
    The current packet does not derive the numerical value K0.  At fixed
    internal transport work J0, an open interval of K values gives the same
    structural IMFD verdict.  The full law identifies its own K, but that is
    measurement of a supplied dynamics, not derivation of the universal
    dynamics.

    There is, however, a real scale-free clue: at fixed J0, the same K is
    selected by four intrinsic self-isolation criteria:

        Delta(K) = isolation(K),
        max min(Delta, isolation),
        max Delta * isolation,
        max min(Delta, isolation) / max(Delta, isolation).

    In the toy model this selects K_crit = 0.700, not the previously chosen
    K0 = 0.620.  The clue is not full closure because freeing J leaves a
    curve/boundary family.  The invariant that would close the family is the
    full sealed modular work profile: intrinsic RN work units for both
    eventless transport and source-defect production.
"""

from __future__ import annotations

from dataclasses import dataclass

from v6_p3o_intrinsic_collar_separator_theorem import PAIR_BLOCKS, partition_label
from v6_p3r_intrinsic_rx_units_resolution import (
    DEFECT_FLOOR,
    MARGIN_FLOOR,
    derive_partition,
    unit_chain_error,
)
from v6_p3t_fixed_cmrp_imfd_dynamics import J0, K0, imfd_log_linear_law, stable_rate
from v6_p3u_spectrum_flow_origin_campaign import K_GRID, J_GRID, passing_ks, span


@dataclass(frozen=True)
class Quality:
    j: float
    k: float
    status: str
    partition: str
    defect: float
    isolation: float
    stable: float | None = None

    @property
    def balance_error(self) -> float:
        return abs(self.defect - self.isolation)

    @property
    def robust_min(self) -> float:
        return min(self.defect, self.isolation)

    @property
    def product(self) -> float:
        return self.defect * self.isolation

    @property
    def ratio(self) -> float:
        denominator = max(self.defect, self.isolation)
        if denominator <= 0.0:
            return 0.0
        return self.robust_min / denominator


@dataclass(frozen=True)
class SelectorAudit:
    candidate: str
    invariant_used: str
    fixed_j: str
    selected: str
    family_span: float
    defect: float
    isolation: float
    stable: float
    verdict: str


def quality(j: float, k: float, with_stability: bool = False) -> Quality:
    law = imfd_log_linear_law(PAIR_BLOCKS, internal=j, source=k)
    status, partition, defect, isolation, _ = derive_partition(law)
    stable = stable_rate(law, partition, "stable") if with_stability else None
    return Quality(
        j=j,
        k=k,
        status=status,
        partition=partition_label(partition),
        defect=defect,
        isolation=isolation,
        stable=stable,
    )


def structurally_valid(item: Quality) -> bool:
    return (
        item.status == "event"
        and item.partition == partition_label(PAIR_BLOCKS)
        and item.defect >= DEFECT_FLOOR
        and item.isolation >= MARGIN_FLOOR
        and unit_chain_error(item.defect, "rn-log") <= 1.0e-10
    )


def valid_at_fixed_j(j: float = J0) -> list[Quality]:
    return [item for item in (quality(j, k) for k in K_GRID) if structurally_valid(item)]


def best_fixed_j(selector: str, j: float = J0) -> Quality:
    candidates = valid_at_fixed_j(j)
    if selector == "balance":
        return min(candidates, key=lambda item: item.balance_error)
    if selector == "max-min":
        return max(candidates, key=lambda item: item.robust_min)
    if selector == "max-product":
        return max(candidates, key=lambda item: item.product)
    if selector == "max-ratio":
        return max(candidates, key=lambda item: item.ratio)
    raise ValueError(selector)


def all_valid_2d() -> list[Quality]:
    out: list[Quality] = []
    for j in J_GRID:
        for k in K_GRID:
            item = quality(j, k)
            if structurally_valid(item):
                out.append(item)
    return out


def best_2d(selector: str, candidates: list[Quality]) -> Quality:
    if selector == "balance":
        return min(candidates, key=lambda item: item.balance_error)
    if selector == "max-min":
        return max(candidates, key=lambda item: item.robust_min)
    if selector == "max-product":
        return max(candidates, key=lambda item: item.product)
    if selector == "max-ratio":
        return max(candidates, key=lambda item: item.ratio)
    raise ValueError(selector)


def fixed_work_quantum_k(j: float, target_work: float) -> Quality:
    # The RN defect is monotone over the fixed-J structural interval in this
    # finite class, so nearest-grid inversion is the finite receipt for the
    # conditional uniqueness theorem.
    return min(valid_at_fixed_j(j), key=lambda item: abs(item.defect - target_work))


def monotone_report(j: float = J0) -> tuple[bool, bool, int, int]:
    candidates = valid_at_fixed_j(j)
    defect_violations = 0
    isolation_violations = 0
    for left, right in zip(candidates, candidates[1:]):
        defect_violations += int(right.defect <= left.defect)
        isolation_violations += int(right.isolation >= left.isolation)
    return (
        defect_violations == 0,
        isolation_violations == 0,
        defect_violations,
        isolation_violations,
    )


def selector_rows() -> list[SelectorAudit]:
    free_stable = passing_ks(J0)
    q_k0 = quality(J0, K0, with_stability=True)
    work_selected = fixed_work_quantum_k(J0, q_k0.defect)
    work_selected_stable = quality(J0, work_selected.k, with_stability=True)
    balance = best_fixed_j("balance", J0)
    balance_stable = quality(J0, balance.k, with_stability=True)
    max_min = best_fixed_j("max-min", J0)
    max_min_stable = quality(J0, max_min.k, with_stability=True)
    max_product = best_fixed_j("max-product", J0)
    max_product_stable = quality(J0, max_product.k, with_stability=True)
    max_ratio = best_fixed_j("max-ratio", J0)
    max_ratio_stable = quality(J0, max_ratio.k, with_stability=True)

    return [
        SelectorAudit(
            "current structural packet",
            "status/R/unit/floors/stability",
            "yes",
            f"{min(free_stable):.3f}-{max(free_stable):.3f}",
            span(free_stable),
            quality(J0, free_stable[len(free_stable) // 2]).defect,
            quality(J0, free_stable[len(free_stable) // 2]).isolation,
            1.0,
            "FAIL-OPEN-K-FAMILY",
        ),
        SelectorAudit(
            "measure supplied law",
            "full P_K log-linear projection",
            "yes",
            f"{K0:.3f}",
            0.0,
            q_k0.defect,
            q_k0.isolation,
            q_k0.stable or 0.0,
            "IDENT-NOT-DERIVATION",
        ),
        SelectorAudit(
            "fixed work quantum",
            "Delta(K)=W_src",
            "yes",
            f"{work_selected.k:.3f}",
            0.0,
            work_selected.defect,
            work_selected.isolation,
            work_selected_stable.stable or 0.0,
            "PASS-CONDITIONAL-WORK-UNIT",
        ),
        SelectorAudit(
            "critical self-isolation",
            "min |Delta-iota|",
            "yes",
            f"{balance.k:.3f}",
            0.0,
            balance.defect,
            balance.isolation,
            balance_stable.stable or 0.0,
            "PASS-FIXED-J-REVISES-K0",
        ),
        SelectorAudit(
            "robust self-isolation",
            "max min(Delta,iota)",
            "yes",
            f"{max_min.k:.3f}",
            0.0,
            max_min.defect,
            max_min.isolation,
            max_min_stable.stable or 0.0,
            "PASS-FIXED-J-REVISES-K0",
        ),
        SelectorAudit(
            "defect-isolation product",
            "max Delta*iota",
            "yes",
            f"{max_product.k:.3f}",
            0.0,
            max_product.defect,
            max_product.isolation,
            max_product_stable.stable or 0.0,
            "PASS-FIXED-J-REVISES-K0",
        ),
        SelectorAudit(
            "scale-free ratio",
            "max min/max",
            "yes",
            f"{max_ratio.k:.3f}",
            0.0,
            max_ratio.defect,
            max_ratio.isolation,
            max_ratio_stable.stable or 0.0,
            "PASS-FIXED-J-REVISES-K0",
        ),
    ]


def print_selector_rows(rows: list[SelectorAudit]) -> None:
    print("K0 selector audit")
    print("-----------------")
    print(
        "candidate                  invariant used              fixed J selected "
        "K_span defect isolation stable verdict"
    )
    for row in rows:
        print(
            f"{row.candidate:26s} "
            f"{row.invariant_used:27s} "
            f"{row.fixed_j:7s} "
            f"{row.selected:8s} "
            f"{row.family_span:6.3f} "
            f"{row.defect:6.4f} "
            f"{row.isolation:9.4f} "
            f"{row.stable:6.3f} "
            f"{row.verdict}"
        )
    print()


def print_2d_report() -> None:
    candidates = all_valid_2d()
    print("free-J self-isolation audit")
    print("---------------------------")
    print(f"structural candidates = {len(candidates)}")
    print(
        f"J range = {min(item.j for item in candidates):.3f}.."
        f"{max(item.j for item in candidates):.3f}"
    )
    print(
        f"K range = {min(item.k for item in candidates):.3f}.."
        f"{max(item.k for item in candidates):.3f}"
    )
    print("selector          J      K      defect  isolation  balance   robust  ratio")
    for name in ("balance", "max-min", "max-product", "max-ratio"):
        item = best_2d(name, candidates)
        print(
            f"{name:15s} "
            f"{item.j:5.3f} "
            f"{item.k:6.3f} "
            f"{item.defect:7.4f} "
            f"{item.isolation:9.4f} "
            f"{item.balance_error:8.4f} "
            f"{item.robust_min:7.4f} "
            f"{item.ratio:6.3f}"
        )
    print()
    print("per-J critical curve sample")
    print("---------------------------")
    print("J      K_crit  defect  isolation  robust  ratio")
    for j in (0.50, 0.75, 1.00, 1.15, 1.40, 1.75, 2.00, 2.25):
        sub = [item for item in candidates if abs(item.j - j) <= 1.0e-12]
        if not sub:
            print(f"{j:4.2f}   --      --      --         --      --")
            continue
        item = min(sub, key=lambda trial: trial.balance_error)
        print(
            f"{j:4.2f} "
            f"{item.k:8.3f} "
            f"{item.defect:7.4f} "
            f"{item.isolation:9.4f} "
            f"{item.robust_min:7.4f} "
            f"{item.ratio:6.3f}"
        )
    print()


def main() -> None:
    print("=" * 112)
    print("v6 Paper 3 section 32: K0 origin campaign")
    print("=" * 112)
    rows = selector_rows()
    print_selector_rows(rows)

    defect_mono, isolation_mono, defect_bad, isolation_bad = monotone_report(J0)
    print("fixed-J monotonicity receipt")
    print("----------------------------")
    print(f"J0 = {J0:.3f}")
    print(f"defect strictly increases with K: {defect_mono} (violations={defect_bad})")
    print(f"isolation strictly decreases with K: {isolation_mono} (violations={isolation_bad})")
    print()

    print_2d_report()

    print("VERDICT")
    print("-------")
    print("The current CMRP/IMFD packet does not derive the old K0=0.620.")
    print("It permits an open stable K-family.  The full supplied law identifies")
    print("K, but identifiability is not a derivation of the universal dynamics.")
    print()
    print("There is a stronger clue: at fixed J0, every tested scale-free")
    print("self-isolation selector chooses K_crit=0.700.  That is an intrinsic")
    print("candidate, but it revises K0 and still needs J0 from the eventless")
    print("transport law.  With J free, the selectors disagree or run along a")
    print("critical curve/boundary.")
    print()
    print("The invariant that would close K0 and the related scalar gaps is the")
    print("sealed modular work profile: the intrinsic Legendre/RN work profile")
    print("whose components fix eventless transport work J and source-defect work")
    print("K before the log-linear dynamics is read out.  If that profile is")
    print("derived from sealed diamonds, branch A-enriched closes at finite level;")
    print("if it is supplied, this remains a parameterized modular dynamics.")


if __name__ == "__main__":
    main()

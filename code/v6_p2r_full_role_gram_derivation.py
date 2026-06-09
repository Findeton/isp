"""
v6 Paper 2 Part II §5.30: full role-Gram derivation gate.

This diagnostic implements the next gate after §5.29.

Canonical finite roles in a local collar:
    record     = stable detector-record likelihood contrast;
    source     = one-event stress/source deletion response;
    causal     = causal-collar incidence/deletion response;
    antichain  = antichain-density deletion response.

A candidate event law passes only if all four role statistics are produced
before thresholding by the same local law, so that the full response Gram

    J_n = Cov(T_record, T_source, T_causal, T_antichain | click)

is internal to the law.  If source is absent or post-selected, the script
prints the explicit extension freedom: the same support and non-source role
data admit multiple source rows and hence multiple beta values.
"""

from __future__ import annotations

from dataclasses import dataclass

from v6_p2j_lr_decisive_tests import acv_actual_event_law_audit
from v6_p2m_generalized_oer_bounds import beta_from_source_kappa, deletion_vector


ROLE_ORDER = ["record", "source", "causal", "antichain"]
NON_SOURCE = ["record", "causal", "antichain"]
SOURCE_INDEX = 1
GAMMA = 7.0 / 48.0


@dataclass
class LawInstance:
    rows: dict[str, list[float]]
    source_stage: str
    support_id: str = "seven-click-support"
    internal_coupling: float = 0.015


@dataclass
class LawAudit:
    candidate: str
    pre_roles: str
    source_stage: str
    full_gram: bool
    acv: bool
    gram_span: float
    kappa_min: float
    beta_span: float
    extension_beta_span: float
    verdict: str


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def role_rows(instance: LawInstance, roles: list[str]) -> list[list[float]]:
    return [instance.rows[role] for role in roles]


def gram(rows: list[list[float]]) -> list[list[float]]:
    return [[dot(row_i, row_j) for row_j in rows] for row_i in rows]


def matrix_span(mats: list[list[list[float]]]) -> float:
    if not mats:
        return float("inf")
    out = 0.0
    for i in range(len(mats[0])):
        for j in range(len(mats[0][0])):
            values = [mat[i][j] for mat in mats]
            out = max(out, max(values) - min(values))
    return out


def beta_from_gram(j: list[list[float]], coupling: float) -> tuple[float, float, bool]:
    _, _, _, _, _, eps_j, _, _, acv_passes = acv_actual_event_law_audit(
        j,
        0.80,
        coupling,
    )
    d = deletion_vector(j)
    source_kappa = d[SOURCE_INDEX] - 4.0 * eps_j
    beta, cost_passes = beta_from_source_kappa(GAMMA, source_kappa)
    return source_kappa, beta, acv_passes and cost_passes and source_kappa > 0.0


def base_role_rows(source_strength: float = 0.95) -> dict[str, list[float]]:
    return {
        "record": [0.95, 0.05, 0.02, 0.00],
        "source": [0.08, source_strength, 0.05, 0.02],
        "causal": [0.03, 0.06, 0.96, 0.04],
        "antichain": [0.02, 0.04, 0.08, 0.98],
    }


def convergent_role_rows(step: float) -> dict[str, list[float]]:
    return {
        "record": [0.95 + 0.02 * step, 0.05, 0.02, 0.00],
        "source": [0.08, 0.92 + 0.03 * step, 0.05, 0.02],
        "causal": [0.03, 0.06, 0.96 + 0.01 * step, 0.04],
        "antichain": [0.02, 0.04, 0.08, 0.98 + 0.01 * step],
    }


def weak_source_rows(strength: float) -> dict[str, list[float]]:
    rows = base_role_rows(0.95)
    rows["source"] = [0.02, strength, 0.01, 0.00]
    return rows


def omit(rows: dict[str, list[float]], roles: list[str]) -> dict[str, list[float]]:
    return {role: rows[role] for role in roles}


def extension_beta_span(instances: list[LawInstance]) -> float:
    """Beta freedom when source is not a pre-threshold role.

    Keep the non-source rows and support fixed.  Add a family of source rows
    after the fact.  If beta moves, the original law could not have derived it.
    """
    if not instances:
        return float("inf")
    template = instances[-1].rows
    if not all(role in template for role in NON_SOURCE):
        # With fewer than the three non-source roles the no-go is only stronger.
        template = base_role_rows(0.95)
    betas = []
    for strength in [0.55, 0.75, 0.95, 1.15]:
        rows = {
            "record": template["record"],
            "source": base_role_rows(strength)["source"],
            "causal": template["causal"],
            "antichain": template["antichain"],
        }
        j = gram(role_rows(LawInstance(rows, "pre"), ROLE_ORDER))
        _, beta, ok = beta_from_gram(j, instances[-1].internal_coupling)
        if ok:
            betas.append(beta)
    if len(betas) < 2:
        return float("inf")
    return max(betas) - min(betas)


def audit(candidate: str, instances: list[LawInstance]) -> LawAudit:
    pre_roles = sorted(set.intersection(*(set(i.rows) for i in instances)))
    has_full_pre_roles = all(role in pre_roles for role in ROLE_ORDER)
    source_stage = instances[-1].source_stage if instances else "absent"
    source_pre = source_stage == "pre"
    full_gram = has_full_pre_roles and source_pre

    grams = []
    kappas = []
    betas = []
    acv_flags = []
    if full_gram:
        for instance in instances:
            j = gram(role_rows(instance, ROLE_ORDER))
            kappa, beta, ok = beta_from_gram(j, instance.internal_coupling)
            grams.append(j)
            kappas.append(kappa)
            betas.append(beta)
            acv_flags.append(ok)

    gram_span = matrix_span(grams) if grams else float("inf")
    kappa_min = min(kappas) if kappas else 0.0
    beta_span = max(betas) - min(betas) if betas else float("inf")
    acv = all(acv_flags) if acv_flags else False
    ext_span = 0.0 if full_gram else extension_beta_span(instances)

    passes = (
        full_gram
        and acv
        and kappa_min > 0.0
        and gram_span <= 0.07
        and beta_span <= 0.02
    )

    return LawAudit(
        candidate=candidate,
        pre_roles=",".join(pre_roles) if pre_roles else "none",
        source_stage=source_stage,
        full_gram=full_gram,
        acv=acv,
        gram_span=gram_span,
        kappa_min=kappa_min,
        beta_span=beta_span,
        extension_beta_span=ext_span,
        verdict="PASS" if passes else "FAIL",
    )


def candidate_laws() -> list[tuple[str, list[LawInstance]]]:
    convergent_full = [
        LawInstance(convergent_role_rows(step), "pre")
        for step in [1.00, 0.50, 0.25, 0.00]
    ]
    exact_full = [LawInstance(base_role_rows(0.95), "pre") for _ in range(4)]
    support_only = [LawInstance({}, "absent") for _ in range(4)]
    record_only = [
        LawInstance(omit(base_role_rows(0.95), ["record"]), "absent")
        for _ in range(4)
    ]
    geometry_three = [
        LawInstance(omit(base_role_rows(0.95), NON_SOURCE), "absent")
        for _ in range(4)
    ]
    post_source = [
        LawInstance(base_role_rows(strength), "post")
        for strength in [0.55, 0.75, 0.95, 1.15]
    ]
    nonconvergent_full = [
        LawInstance(base_role_rows(strength), "pre")
        for strength in [0.55, 1.15, 0.65, 1.05]
    ]
    weak_full = [
        LawInstance(weak_source_rows(strength), "pre")
        for strength in [0.04, 0.05, 0.06, 0.05]
    ]
    return [
        ("full LR/OER Gram", convergent_full),
        ("exact full Gram", exact_full),
        ("support only", support_only),
        ("record only LR", record_only),
        ("geometry three-role", geometry_three),
        ("post-selected source", post_source),
        ("nonconvergent full", nonconvergent_full),
        ("weak full source", weak_full),
    ]


def print_audits(rows: list[LawAudit]) -> None:
    print("full role-Gram derivation gate")
    print("------------------------------")
    print(
        "candidate              source  fullJ  ACV   J_span  kappa_min  "
        "beta_span  ext_beta_span  verdict"
    )
    for row in rows:
        j_span = "inf" if row.gram_span == float("inf") else f"{row.gram_span:7.4f}"
        b_span = "inf" if row.beta_span == float("inf") else f"{row.beta_span:9.4f}"
        e_span = (
            "inf"
            if row.extension_beta_span == float("inf")
            else f"{row.extension_beta_span:13.4f}"
        )
        print(
            f"{row.candidate:22s}  "
            f"{row.source_stage:6s}  "
            f"{('yes' if row.full_gram else 'no'):5s}  "
            f"{('PASS' if row.acv else 'FAIL'):4s}  "
            f"{j_span:>7s}  "
            f"{row.kappa_min:9.4f}  "
            f"{b_span:>9s}  "
            f"{e_span:>13s}  "
            f"{row.verdict}"
        )
    print()


def no_source_nogo_receipt() -> tuple[float, float]:
    instances = [
        LawInstance(omit(base_role_rows(0.95), NON_SOURCE), "absent")
        for _ in range(4)
    ]
    beta_span = extension_beta_span(instances)
    kappas = []
    for strength in [0.55, 0.75, 0.95, 1.15]:
        rows = base_role_rows(strength)
        j = gram(role_rows(LawInstance(rows, "pre"), ROLE_ORDER))
        kappa, _, ok = beta_from_gram(j, 0.015)
        if ok:
            kappas.append(kappa)
    return max(kappas) - min(kappas), beta_span


def main() -> None:
    rows = [audit(name, instances) for name, instances in candidate_laws()]
    print("=" * 104)
    print("v6 Paper 2 Part II §5.30: full role-Gram derivation gate")
    print("=" * 104)
    print_audits(rows)
    kappa_span, beta_span = no_source_nogo_receipt()
    print("NO-SOURCE NO-GO RECEIPT")
    print("-----------------------")
    print(f"same non-source roles, source extension kappa span = {kappa_span:.4f}")
    print(f"same non-source roles, source extension beta span  = {beta_span:.4f}")
    print()
    print("VERDICT")
    print("-------")
    print("Only a law that produces record, source, causal, and antichain")
    print("statistics before thresholding derives the full Gram J_n.  If")
    print("source is absent or post-selected, the same reduced data admit")
    print("source extensions with different beta values.")


if __name__ == "__main__":
    main()

"""
v6 Paper 2 Part II §5.28: full role-generator audit.

This diagnostic tests the next A-full question:

Can source response be derived from one local role-complete generator, or can
the source row vary while record, causal, and antichain roles are fixed?

Finite model:
- a clicked local generator has latent feature vector Z with Cov(Z)=I;
- the four role sufficient statistics are T=A Z;
- the full role response law is J=Cov(T)=A A^T.

If A is part of the event law, J and d_source are fixed. If only the support
and the other three role rows are fixed, the source row can move.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt

from v6_p2j_lr_decisive_tests import acv_actual_event_law_audit
from v6_p2m_generalized_oer_bounds import beta_from_source_kappa, deletion_vector


ROLE_COUNT = 4


@dataclass
class GeneratorInstance:
    source_strength: float
    support_id: str
    role_complete: bool
    rows: list[list[float]]
    internal_coupling: float


@dataclass
class GeneratorAudit:
    case: str
    same_three_roles: bool
    same_full_generator: bool
    role_complete: bool
    acv: bool
    source_row_span: float
    kappa_span: float
    beta_span: float
    verdict: str


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def response_jacobian(rows: list[list[float]]) -> list[list[float]]:
    return [[dot(row_i, row_j) for row_j in rows] for row_i in rows]


def matrix_fingerprint(matrix: list[list[float]]) -> tuple[tuple[float, ...], ...]:
    return tuple(tuple(round(x, 12) for x in row) for row in matrix)


def three_role_fingerprint(instance: GeneratorInstance) -> tuple[tuple[float, ...], ...]:
    # record, causal, antichain; source row omitted.
    return matrix_fingerprint([instance.rows[0], instance.rows[2], instance.rows[3]])


def full_generator_fingerprint(instance: GeneratorInstance) -> tuple[tuple[float, ...], ...] | None:
    if not instance.role_complete:
        return None
    return matrix_fingerprint(instance.rows)


def source_kappa_beta_acv(instance: GeneratorInstance) -> tuple[float, float, bool]:
    jacobian = response_jacobian(instance.rows)
    _, _, _, _, _, eps_j, _, _, acv_passes = acv_actual_event_law_audit(
        jacobian,
        0.80,
        instance.internal_coupling,
    )
    d = deletion_vector(jacobian)
    source_kappa = d[1] - 4.0 * eps_j
    beta, cost_passes = beta_from_source_kappa(7.0 / 48.0, source_kappa)
    return source_kappa, beta, acv_passes and cost_passes and source_kappa > 0.0


def base_rows(source_strength: float) -> list[list[float]]:
    return [
        [0.95, 0.05, 0.02, 0.00],
        [0.08, source_strength, 0.05, 0.02],
        [0.03, 0.06, 0.96, 0.04],
        [0.02, 0.04, 0.08, 0.98],
    ]


def convergent_rows(step: float) -> list[list[float]]:
    return [
        [0.95 + 0.02 * step, 0.05, 0.02, 0.00],
        [0.08, 0.92 + 0.03 * step, 0.05, 0.02],
        [0.03, 0.06, 0.96 + 0.01 * step, 0.04],
        [0.02, 0.04, 0.08, 0.98 + 0.01 * step],
    ]


def audit(case: str, instances: list[GeneratorInstance]) -> GeneratorAudit:
    three_ids = {three_role_fingerprint(instance) for instance in instances}
    full_ids = {full_generator_fingerprint(instance) for instance in instances}
    source_strengths = [instance.source_strength for instance in instances]
    kappas = []
    betas = []
    acv_flags = []
    for instance in instances:
        kappa, beta, acv = source_kappa_beta_acv(instance)
        kappas.append(kappa)
        betas.append(beta)
        acv_flags.append(acv)
    same_three = len(three_ids) == 1
    same_full = None not in full_ids and len(full_ids) == 1
    role_complete = all(instance.role_complete for instance in instances)
    source_span = max(source_strengths) - min(source_strengths)
    kappa_span = max(kappas) - min(kappas)
    beta_span = max(betas) - min(betas)
    acv = all(acv_flags)
    passes = role_complete and acv and (
        (same_full and beta_span <= 1e-12)
        or (not same_three and kappa_span <= 0.05 and beta_span <= 0.02)
    )
    return GeneratorAudit(
        case=case,
        same_three_roles=same_three,
        same_full_generator=same_full,
        role_complete=role_complete,
        acv=acv,
        source_row_span=source_span,
        kappa_span=kappa_span,
        beta_span=beta_span,
        verdict="PASS" if passes else "FAIL",
    )


def instance(
    strength: float,
    role_complete: bool = True,
    rows: list[list[float]] | None = None,
    support_id: str = "seven-click-support",
    coupling: float = 0.015,
) -> GeneratorInstance:
    return GeneratorInstance(
        source_strength=strength,
        support_id=support_id,
        role_complete=role_complete,
        rows=rows if rows is not None else base_rows(strength),
        internal_coupling=coupling,
    )


def audits() -> list[GeneratorAudit]:
    strengths = [0.55, 0.75, 0.95, 1.15]
    full = [instance(0.95) for _ in strengths]
    three_role_sweep = [instance(strength) for strength in strengths]
    hidden = [instance(strength, role_complete=False) for strength in strengths]
    convergent = [
        instance(0.92 + 0.03 * step, rows=convergent_rows(step))
        for step in [1.00, 0.50, 0.25, 0.00]
    ]
    return [
        audit("same full generator", full),
        audit("three-role source sweep", three_role_sweep),
        audit("hidden source row", hidden),
        audit("convergent generator", convergent),
    ]


def print_audits(rows: list[GeneratorAudit]) -> None:
    print("full role-generator audit")
    print("-------------------------")
    print(
        "case                     same3  full_gen  role_full  ACV   "
        "src_span  kappa_span  beta_span  verdict"
    )
    for row in rows:
        print(
            f"{row.case:24s}  "
            f"{('yes' if row.same_three_roles else 'no'):5s}  "
            f"{('yes' if row.same_full_generator else 'no'):8s}  "
            f"{('yes' if row.role_complete else 'no'):9s}  "
            f"{('PASS' if row.acv else 'FAIL'):4s}  "
            f"{row.source_row_span:8.4f}  "
            f"{row.kappa_span:10.4f}  "
            f"{row.beta_span:9.4f}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    rows = audits()
    print("=" * 104)
    print("v6 Paper 2 Part II §5.28: full role-generator audit")
    print("=" * 104)
    print_audits(rows)
    print("VERDICT")
    print("-------")
    print("One full generator fixes the source row and beta. Holding only the")
    print("other three role rows fixed does not derive source response. A-full")
    print("therefore requires the source row to be part of the local generator,")
    print("not an extension after the event support is selected.")


if __name__ == "__main__":
    main()

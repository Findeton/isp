"""
v6 Paper 2 Part II §5.36: construction exhaustion audit.

After the finite gates in §5.30-§5.35, Branch A has one remaining object:

    one local microcausal linear operator family
    -> full pre-threshold four-role Gram
    -> positive source response
    -> beta
    -> the physical receipts.

This script asks whether the known construction classes actually produce that
object, or only a proper subobject that must be completed by hand.  It also
prints two finite extension no-go receipts:

1. fixed record/source local-operator data plus variable geometry rows;
2. fixed non-source role data plus variable source rows.

If either extension is allowed, the full Gram and beta are not functions of
the reduced law.  The result is a conditional no-go for all fixed-background
or coupled-source constructions that do not generate all four rows before
thresholding.
"""

from __future__ import annotations

from dataclasses import dataclass

from v6_p2r_full_role_gram_derivation import (
    ROLE_ORDER,
    LawInstance,
    base_role_rows,
    beta_from_gram,
    gram,
    matrix_span,
    no_source_nogo_receipt,
    role_rows,
)


@dataclass
class ConstructionClass:
    name: str
    record_source: bool
    geometry: bool
    one_operator: bool
    microcausal: bool
    linear_prethreshold: bool
    full_gram_derived: bool
    external_input: str
    verdict: str


@dataclass
class ExtensionAudit:
    family: str
    reduced_data_fixed: str
    extensions: int
    gram_span: float
    kappa_span: float
    beta_span: float
    verdict: str


def geometry_extension_rows(causal_diag: float, anti_diag: float) -> dict[str, list[float]]:
    """Keep record/source rows fixed while varying geometry readouts.

    This models a fixed-background local operator law that gives record/source
    statistics, while causal/antichain readouts are attached as an external
    geometry completion.
    """
    rows = base_role_rows(0.95)
    rows["causal"] = [0.03, 0.02 + 0.05 * causal_diag, causal_diag, 0.04]
    rows["antichain"] = [0.02, 0.01 + 0.04 * anti_diag, 0.08, anti_diag]
    return rows


def full_gram_values(rows: dict[str, list[float]]) -> tuple[list[list[float]], float, float, bool]:
    j = gram(role_rows(LawInstance(rows, "pre"), ROLE_ORDER))
    kappa, beta, ok = beta_from_gram(j, 0.015)
    return j, kappa, beta, ok


def geometry_extension_no_go() -> ExtensionAudit:
    grams = []
    kappas = []
    betas = []
    for causal_diag, anti_diag in [
        (0.82, 0.86),
        (0.90, 0.92),
        (0.96, 0.98),
        (1.04, 1.06),
    ]:
        j, kappa, beta, ok = full_gram_values(
            geometry_extension_rows(causal_diag, anti_diag)
        )
        if ok:
            grams.append(j)
            kappas.append(kappa)
            betas.append(beta)

    return ExtensionAudit(
        family="geometry extension",
        reduced_data_fixed="record/source local operator",
        extensions=len(betas),
        gram_span=matrix_span(grams),
        kappa_span=max(kappas) - min(kappas),
        beta_span=max(betas) - min(betas),
        verdict="FAIL" if len(betas) >= 2 and matrix_span(grams) > 0.0 else "PASS",
    )


def source_extension_no_go() -> ExtensionAudit:
    kappa_span, beta_span = no_source_nogo_receipt()
    return ExtensionAudit(
        family="source extension",
        reduced_data_fixed="record/causal/antichain roles",
        extensions=4,
        gram_span=float("inf"),
        kappa_span=kappa_span,
        beta_span=beta_span,
        verdict="FAIL" if beta_span > 0.0 else "PASS",
    )


def construction_classes() -> list[ConstructionClass]:
    return [
        ConstructionClass(
            "fixed-background QFT scalar",
            True,
            False,
            True,
            True,
            True,
            False,
            "geometry rows",
            "FAIL",
        ),
        ConstructionClass(
            "stress/RCE locally covariant QFT",
            True,
            False,
            True,
            True,
            True,
            False,
            "background metric/geometry",
            "FAIL",
        ),
        ConstructionClass(
            "relativistic collapse/flash",
            True,
            False,
            False,
            True,
            False,
            False,
            "stochastic source law",
            "FAIL",
        ),
        ConstructionClass(
            "causal-set geometry first",
            False,
            True,
            False,
            True,
            True,
            False,
            "source/operator rows",
            "FAIL",
        ),
        ConstructionClass(
            "coupled source + geometry",
            True,
            True,
            False,
            True,
            True,
            False,
            "operator identity",
            "FAIL",
        ),
        ConstructionClass(
            "A-full finite ansatz",
            True,
            True,
            True,
            True,
            True,
            True,
            "interacting derivation",
            "COND",
        ),
        ConstructionClass(
            "unknown interacting ISP theorem",
            True,
            True,
            True,
            True,
            True,
            False,
            "not yet proved",
            "OPEN",
        ),
    ]


def yn(flag: bool) -> str:
    return "yes" if flag else "no"


def fmt(value: float) -> str:
    return "inf" if value == float("inf") else f"{value:.4f}"


def print_construction_classes(rows: list[ConstructionClass]) -> None:
    print("construction-class audit")
    print("------------------------")
    print(
        "candidate                         rec/src  geom  oneO  micro  linear  "
        "fullJ  missing input             verdict"
    )
    for row in rows:
        print(
            f"{row.name:32s}  "
            f"{yn(row.record_source):7s}  "
            f"{yn(row.geometry):4s}  "
            f"{yn(row.one_operator):4s}  "
            f"{yn(row.microcausal):5s}  "
            f"{yn(row.linear_prethreshold):6s}  "
            f"{yn(row.full_gram_derived):5s}  "
            f"{row.external_input:23s}  "
            f"{row.verdict}"
        )
    print()


def print_extension_audits(rows: list[ExtensionAudit]) -> None:
    print("extension no-go receipts")
    print("------------------------")
    print(
        "family              fixed reduced data             ext  "
        "J_span  kappa_span  beta_span  verdict"
    )
    for row in rows:
        print(
            f"{row.family:18s}  "
            f"{row.reduced_data_fixed:28s}  "
            f"{row.extensions:3d}  "
            f"{fmt(row.gram_span):>7s}  "
            f"{fmt(row.kappa_span):>10s}  "
            f"{fmt(row.beta_span):>9s}  "
            f"{row.verdict}"
        )
    print()


def main() -> None:
    construction_rows = construction_classes()
    extension_rows = [geometry_extension_no_go(), source_extension_no_go()]

    print("=" * 104)
    print("v6 Paper 2 Part II §5.36: construction exhaustion audit")
    print("=" * 104)
    print_construction_classes(construction_rows)
    print_extension_audits(extension_rows)
    print("VERDICT")
    print("-------")
    print("Known local-QFT, collapse/flash, causal-set, and coupled-source")
    print("construction classes do not derive the Branch-A object unless the")
    print("full four-role Gram is supplied as an ansatz.  The finite extension")
    print("receipts show why: record/source data do not determine geometry rows,")
    print("and geometry/record data do not determine the source row or beta.")
    print("Thus Branch A is impossible for fixed-background or coupled-source")
    print("classes under the current assumptions.  The only live route is a new")
    print("interacting ISP theorem deriving the full Gram from one local")
    print("microcausal linear operator family before thresholding.")


if __name__ == "__main__":
    main()

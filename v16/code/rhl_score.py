#!/usr/bin/env python3
"""Frozen scorer for RHL Paper 11.

The scorer authenticates frozen receipts, derives every finite comparison from
their upstream objects, audits the paper's scoped analytical claim registry,
and maps those predicates to the pin's outcome vocabulary.  It does not claim
to machine-prove the paper's arbitrary-region theorems; those proofs require
independent adjudicator and hostile review.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Sequence


ROOT = Path(__file__).resolve().parents[2]
CORE_SOURCE = ROOT / "v16/code/rhl_core.py"
CORE_OUTPUT = ROOT / "v16/code/rhl_core_output.txt"
CORE_RECEIPT = ROOT / "v16/code/rhl_core_receipt.json"
REG_SOURCE = ROOT / "v16/code/rhl_regulator.py"
REG_OUTPUT = ROOT / "v16/code/rhl_regulator_output.txt"
REG_RECEIPT = ROOT / "v16/code/rhl_regulator_receipt.json"
PIN = ROOT / "v16/note-rhl-pin.md"


FROZEN_HASHES = {
    "core_source": "032ede336c8cf23b168e018ecd0748e0467d1ca25cb2b44ae750ae320ae9ba8a",
    "core_output": "c56c8e3dece8357d3af0e39ea2459b8a29b6fd58bc3ffc99e5ba1cabe85adafb",
    "core_receipt": "cfd7f243c96f29b303d7c0ef6c283b40be3994b3f6eb1945a801f0677903e060",
    "reg_source": "d6d520a6a43451a889bfc40e2dd8df2f9afc08f032c202c3d8c206c02b4a3db9",
    "reg_output": "1f020e41989007048cf2d864f966b90184e332622230f26028c8e90225befb68",
    "reg_receipt": "cea302918c101c7b2bd5973167776baa587681f4b83b8ebff041e38e0bfee944",
    "pin": "1d0df95fb074a688160e1a4554976268643e35835ef46b1d4918b90ee23505ee",
}


REQUIRED_CLAIMS = (
    "R1-POINT-FREE-KINEMATICS",
    "R2-PRESENTATION-DESCENT",
    "R2-NO-INTERMEDIATE-KERNEL",
    "R2-HILBERT-REPRESENTATION",
    "R2-STRUCTURAL-NONSELECTION",
    "R3-DIVISION-INSTRUMENT",
    "R3-APPEND-ONLY-STABILITY",
    "R3-ACTUALIZATION-POSTULATE",
    "R4-FIXED-FACTOR-LOCALITY",
    "R4-DYNAMIC-LOCALITY-UNENTERED",
    "R4-GEOMETRY-UNENTERED",
    "R5-HAMILTONIAN-SHADOW",
    "WALL-INFINITE-EXTENSION",
    "WALL-GR-QFT",
)


REQUIRED_THEOREMS = (
    "Theorem 1 (presentation descent)",
    "Theorem 2 (no probability at an interfering refinement)",
    "Theorem 3 (division instrument)",
    "Theorem 4 (append-only record stability)",
    "Theorem 5 (character-twist nonselection)",
    "Proposition 6 (dynamic-subsystem referent)",
)


MUTANTS = (
    "MUT-CORE-HASH",
    "MUT-REG-HASH",
    "MUT-INTERFERENCE-DIAGONAL",
    "MUT-PRESENTATION-MISMATCH",
    "MUT-TAMPER-INERT",
    "MUT-RECORD-UNERASABLE",
    "MUT-REDUNDANCY-LOST",
    "MUT-CHARACTER-INERT",
    "MUT-FIXED-FACTOR-SIGNAL",
    "MUT-DYNAMIC-TRANSPORT-SMUGGLED",
    "MUT-DELETE-DESCENT-THEOREM",
    "MUT-ONTOLOGIZE-MESH",
    "MUT-PROMOTE-GEOMETRY",
    "MUT-PROMOTE-GR",
    "MUT-OUTCOME-TAMPER",
)


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def digest(value: object) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TypeError(f"{path} must contain a JSON object")
    return value


def collect_claims(paper: str) -> set[str]:
    return set(re.findall(r"<!-- CLAIM:([A-Z0-9-]+) -->", paper))


def apply_mutant(
    name: str,
    hashes: dict[str, str],
    core_receipt: dict[str, Any],
    reg_receipt: dict[str, Any],
    paper: str,
) -> tuple[dict[str, str], dict[str, Any], dict[str, Any], str]:
    hashes = dict(hashes)
    core_receipt = copy.deepcopy(core_receipt)
    reg_receipt = copy.deepcopy(reg_receipt)
    paper = str(paper)
    data = reg_receipt["data"]

    if name == "MUT-CORE-HASH":
        hashes["core_source"] = "0" * 64
    elif name == "MUT-REG-HASH":
        hashes["reg_source"] = "0" * 64
    elif name == "MUT-INTERFERENCE-DIAGONAL":
        data["history"]["coherent_weight"] = data["history"]["diagonal_weight"]
    elif name == "MUT-PRESENTATION-MISMATCH":
        data["presentations"]["right"]["composite"] = [["1", "0"], ["0", "1"]]
    elif name == "MUT-TAMPER-INERT":
        data["presentations"]["tampered_right_composite"] = data["presentations"]["common_boundary_transport"]
    elif name == "MUT-RECORD-UNERASABLE":
        data["records"]["single_flag"]["returns_to_seed"] = False
    elif name == "MUT-REDUNDANCY-LOST":
        data["records"]["redundant_flag"]["first_copy_erased_support"] = [0, 4]
    elif name == "MUT-CHARACTER-INERT":
        data["structural_counterfamilies"]["two_filling_weights_by_charge"] = {str(index): "1" for index in range(4)}
    elif name == "MUT-FIXED-FACTOR-SIGNAL":
        data["locality"]["fixed_factor"]["bob_after_alice_dephase"] = [["1", "0"], ["0", "0"]]
    elif name == "MUT-DYNAMIC-TRANSPORT-SMUGGLED":
        data["locality"]["changing_boundary_identification"]["law_selected_transport_supplied"] = True
    elif name == "MUT-DELETE-DESCENT-THEOREM":
        paper = paper.replace("Theorem 1 (presentation descent)", "Theorem 1 removed")
    elif name == "MUT-ONTOLOGIZE-MESH":
        paper += "\n<!-- FORBIDDEN-ONTOLOGY:MESH-ATOMS -->\n"
    elif name == "MUT-PROMOTE-GEOMETRY":
        paper += "\n<!-- FORBIDDEN-PROMOTION:GEOMETRY-CONSTRUCTED -->\n"
    elif name == "MUT-PROMOTE-GR":
        paper += "\n<!-- FORBIDDEN-PROMOTION:GR-RECOVERED -->\n"
    elif name == "MUT-OUTCOME-TAMPER":
        paper = paper.replace("RHL-REGIONAL-QUANTUM-LAW-CONSTRUCTED-BUT-GEOMETRY-UNENTERED", "RHL-JOINT-QUANTUM-GEOMETRIC-LAW-CONSTRUCTED")
    else:
        raise ValueError(f"unknown mutant {name}")
    return hashes, core_receipt, reg_receipt, paper


def score(
    hashes: dict[str, str],
    core_receipt: dict[str, Any],
    reg_receipt: dict[str, Any],
    paper: str,
) -> tuple[list[dict[str, object]], dict[str, object], dict[str, object]]:
    gates: list[dict[str, object]] = []

    def gate(name: str, passed: bool, evidence: str, lineage: Sequence[str]) -> None:
        gates.append(
            {
                "gate": name,
                "passed": bool(passed),
                "evidence": evidence,
                "lineage": list(lineage),
            }
        )

    for key, expected in FROZEN_HASHES.items():
        gate(
            f"G-HASH-{key.upper().replace('_', '-')}",
            hashes.get(key) == expected,
            f"actual={hashes.get(key)} expected={expected}",
            (f"file:{key}", "sha256", "frozen-anchor"),
        )

    core_gates = core_receipt.get("gates", [])
    reg_checks = reg_receipt.get("checks", [])
    gate(
        "G-CORE-PUBLIC-TOTAL",
        len(core_gates) == 10 and all(item.get("passed") is True for item in core_gates),
        f"passing={sum(item.get('passed') is True for item in core_gates)}/10",
        ("core_receipt.gates", "count+all", "public-core"),
    )
    gate(
        "G-REGULATOR-TOTAL",
        len(reg_checks) == 10 and all(item.get("predicate") is True for item in reg_checks),
        f"passing={sum(item.get('predicate') is True for item in reg_checks)}/10",
        ("reg_receipt.checks", "count+all", "regulator-controls"),
    )

    data = reg_receipt.get("data", {})
    presentations = data.get("presentations", {})
    history = data.get("history", {})
    records = data.get("records", {})
    families = data.get("structural_counterfamilies", {})
    locality = data.get("locality", {})

    common_descent = (
        presentations.get("left", {}).get("composite")
        == presentations.get("right", {}).get("composite")
        == presentations.get("common_boundary_transport")
    )
    nonisomorphic_rows = len(presentations.get("left", {}).get("embedding", [])) != len(
        presentations.get("right", {}).get("embedding", [])
    )
    tamper_moves = presentations.get("tampered_right_composite") != presentations.get("common_boundary_transport")
    gate(
        "G-PRESENTATION-DESCENT-CONTROL",
        common_descent and nonisomorphic_rows and tamper_moves,
        f"nonisomorphic={nonisomorphic_rows} common={common_descent} tamper_moves={tamper_moves}",
        ("reg.presentations", "compose", "boundary-comparison"),
    )

    coherent = history.get("coherent_weight")
    diagonal = history.get("diagonal_weight")
    interference_moves = coherent == "49/625" and diagonal == "337/625" and coherent != diagonal
    gate(
        "G-NO-INTERMEDIATE-KERNEL-WITNESS",
        interference_moves,
        f"coherent={coherent} diagonal={diagonal} defect={history.get('interference_defect')}",
        ("reg.history.route_amplitudes", "Gram functional", "coarse-vs-diagonal"),
    )

    single_erasable = records.get("single_flag", {}).get("returns_to_seed") is True
    redundant_support = records.get("redundant_flag", {}).get("first_copy_erased_support") == [0, 5]
    gate(
        "G-RECORD-ERASER-CONTROL",
        single_erasable,
        f"returns={records.get('single_flag', {}).get('returns_to_seed')}",
        ("reg.records.single_flag", "writer twice", "seed comparison"),
    )
    gate(
        "G-RECORD-REDUNDANCY-CONTROL",
        redundant_support,
        f"support={records.get('redundant_flag', {}).get('first_copy_erased_support')}",
        ("reg.records.redundant_flag", "erase first copy", "remaining support"),
    )

    weights = families.get("two_filling_weights_by_charge", {})
    character_glues = families.get("character_gluing_all_pass") is True
    character_moves = len(set(weights.values())) > 1 if isinstance(weights, dict) else False
    gate(
        "G-STRUCTURAL-NONSELECTION",
        character_glues and character_moves,
        f"glues={character_glues} weights={weights}",
        ("reg.structural_counterfamilies", "character gluing", "boundary weights"),
    )

    fixed_local = locality.get("fixed_factor", {}).get("bob_before") == locality.get("fixed_factor", {}).get(
        "bob_after_alice_dephase"
    )
    dynamic = locality.get("changing_boundary_identification", {})
    dynamic_ambiguous = (
        dynamic.get("identity_calibration_probability") != dynamic.get("swapped_calibration_probability")
        and dynamic.get("law_selected_transport_supplied") is False
    )
    gate(
        "G-FIXED-FACTOR-LOCALITY",
        fixed_local,
        f"bob_before={locality.get('fixed_factor', {}).get('bob_before')} bob_after={locality.get('fixed_factor', {}).get('bob_after_alice_dephase')}",
        ("reg.locality.fixed_factor", "Alice CPTP map", "Bob partial trace"),
    )
    gate(
        "G-DYNAMIC-LOCALITY-REFERENT",
        dynamic_ambiguous,
        f"identity={dynamic.get('identity_calibration_probability')} swapped={dynamic.get('swapped_calibration_probability')} selected={dynamic.get('law_selected_transport_supplied')}",
        ("reg.locality.changing_boundary_identification", "calibration transport", "probability comparison"),
    )

    claims = collect_claims(paper)
    missing_claims = sorted(set(REQUIRED_CLAIMS) - claims)
    gate(
        "G-CLAIM-REGISTRY-TOTAL",
        not missing_claims and len(claims) == len(REQUIRED_CLAIMS),
        f"registered={len(claims)} required={len(REQUIRED_CLAIMS)} missing={missing_claims}",
        ("paper claim comments", "set comparison", "scope registry"),
    )
    missing_theorems = [name for name in REQUIRED_THEOREMS if name not in paper]
    gate(
        "G-ANALYTICAL-THEOREM-REGISTER",
        not missing_theorems,
        f"present={len(REQUIRED_THEOREMS)-len(missing_theorems)}/{len(REQUIRED_THEOREMS)} missing={missing_theorems}",
        ("paper theorem statements", "literal referent audit", "human proof review pending"),
    )

    required_ontology_phrases = (
        "one actual relational record history",
        "no underlying point set",
        "Representational refinement",
        "Ontic extension",
        "Actualization is postulated",
    )
    missing_ontology = [phrase for phrase in required_ontology_phrases if phrase not in paper]
    gate(
        "G-ONTOLOGY-LAW-REPRESENTATION-SPLIT",
        not missing_ontology,
        f"phrases={len(required_ontology_phrases)-len(missing_ontology)}/{len(required_ontology_phrases)} missing={missing_ontology}",
        ("paper ontology sections", "required phrases", "type audit"),
    )

    forbidden_markers = (
        "FORBIDDEN-ONTOLOGY:MESH-ATOMS",
        "FORBIDDEN-PROMOTION:GEOMETRY-CONSTRUCTED",
        "FORBIDDEN-PROMOTION:GR-RECOVERED",
    )
    present_forbidden = [marker for marker in forbidden_markers if marker in paper]
    gate(
        "G-NO-FORBIDDEN-PROMOTION",
        not present_forbidden,
        f"present={present_forbidden}",
        ("paper bytes", "forbidden marker scan", "scope wall"),
    )

    outcome_primary = "RHL-REGIONAL-QUANTUM-LAW-CONSTRUCTED-BUT-GEOMETRY-UNENTERED"
    outcome_qualifiers = [
        "RHL-POINT-FREE-REGIONAL-KINEMATICS-CONSTRUCTED",
        "RHL-REFINEMENT-INVARIANT-UNSLICED-QUANTUM-LAW-CONSTRUCTED",
        "RHL-STABLE-DIVISION-SHADOW-CONSTRUCTED",
        "RHL-BLOCKED-AT-DYNAMIC-LOCALITY",
    ]
    claimed_outcomes = [outcome_primary, *outcome_qualifiers]
    outcome_present = all(outcome in paper for outcome in claimed_outcomes)
    stronger_outcomes_absent = "RHL-JOINT-QUANTUM-GEOMETRIC-LAW-CONSTRUCTED" not in paper
    gate(
        "G-OUTCOME-SCOPE",
        outcome_present and stronger_outcomes_absent,
        f"candidate_primary_present={outcome_primary in paper} stronger_absent={stronger_outcomes_absent}",
        ("derived gates", "registered rung order", "paper status"),
    )

    required_references = (
        "https://arxiv.org/abs/gr-qc/0410104",
        "https://arxiv.org/abs/hep-th/0306025",
        "https://arxiv.org/abs/gr-qc/9507057",
        "https://arxiv.org/abs/hep-th/0403007",
        "https://arxiv.org/abs/1607.06700",
        "https://arxiv.org/abs/2211.09578",
        "https://arxiv.org/abs/2507.21192",
    )
    missing_refs = [reference for reference in required_references if reference not in paper]
    gate(
        "G-EXTERNAL-REFERENCE-MAP",
        not missing_refs,
        f"present={len(required_references)-len(missing_refs)}/{len(required_references)} missing={missing_refs}",
        ("paper references", "URL census", "external-framework map"),
    )

    # The finite source contains no floating arithmetic.  Decimal years and
    # citation identifiers in the paper are not substantive arithmetic.
    source_text = CORE_SOURCE.read_text(encoding="utf-8") + REG_SOURCE.read_text(encoding="utf-8")
    float_tokens = re.findall(r"(?<![A-Za-z0-9_])\d+\.\d+(?![A-Za-z0-9_])", source_text)
    gate(
        "G-EXACT-SUBSTANTIVE-PATH",
        not float_tokens and "numpy" not in source_text and "math.isclose" not in source_text,
        f"float_tokens={float_tokens}",
        ("frozen core+regulator source", "token scan", "exactness"),
    )

    analytical_claims_present = not missing_claims and not missing_theorems and not missing_ontology
    finite_surface_passes = all(
        (
            common_descent,
            nonisomorphic_rows,
            tamper_moves,
            interference_moves,
            single_erasable,
            redundant_support,
            character_glues,
            character_moves,
            fixed_local,
            dynamic_ambiguous,
        )
    )
    primary_eligible = analytical_claims_present and finite_surface_passes and outcome_present and stronger_outcomes_absent
    gate(
        "G-PRIMARY-ELIGIBILITY",
        primary_eligible,
        f"analytical_registry={analytical_claims_present} finite_receipts={finite_surface_passes} scoped_outcome={outcome_present and stronger_outcomes_absent}",
        ("paper analytical registry", "upstream physical lineages", "pin rung logic"),
    )

    failed = [item["gate"] for item in gates if not item["passed"]]
    measurements = {
        "finite_receipts": {
            "common_descent": common_descent,
            "nonisomorphic_presentations": nonisomorphic_rows,
            "tamper_moves": tamper_moves,
            "coherent_weight": coherent,
            "diagonal_weight": diagonal,
            "single_flag_erasable": single_erasable,
            "redundant_support": records.get("redundant_flag", {}).get("first_copy_erased_support"),
            "character_weights": weights,
            "fixed_factor_locality": fixed_local,
            "dynamic_boundary_ambiguous": dynamic_ambiguous,
        },
        "analytical_registry": {
            "claims": sorted(claims),
            "theorems": list(REQUIRED_THEOREMS),
            "proof_status": "candidate proofs require independent adjudicator and hostile review",
        },
        "law_type": {
            "unrecorded_region_representation": "HISTORY-DECOHERENCE-FUNCTIONAL-REQUIRED",
            "stochastic_fundamental_reading": "INDIVISIBLE-MULTITIME-LAW-REQUIRED",
            "stable_record_boundary": "DIVISION-KERNEL-SUFFICIENT",
            "higher_order": "METHOD-INCONCLUSIVE",
        },
        "scope": {
            "finite_matrices": "receipts only",
            "arbitrary_refinement": "analytical algebraic-colimit theorem; no sigma-additive extension claim",
            "record_stability": "proved for the declared append-only/recoverable continuation class only",
            "dynamic_locality": "unentered without law-selected subsystem transport",
            "geometry": "unentered; character counterfamily is not geometry",
        },
    }
    result = {
        "eligible": primary_eligible and not failed,
        "primary": outcome_primary if primary_eligible and not failed else "RHL-METHOD-INCONCLUSIVE",
        "qualifiers": outcome_qualifiers if primary_eligible and not failed else [],
        "failed_gates": failed,
    }
    return gates, measurements, result


def render(gates: Sequence[dict[str, object]], measurements: dict[str, object], result: dict[str, object]) -> str:
    lines = [
        "RHL PAPER 11 CANDIDATE SCORE",
        "scope: analytical candidate plus exact regulator receipts; finite data do not decide ontology",
    ]
    for item in gates:
        word = "PASS" if item["passed"] else "FAIL"
        lines.append(f"{word} {item['gate']} :: {item['evidence']}")
    lines.append(f"SUMMARY {sum(item['passed'] for item in gates)}/{len(gates)} gates")
    lines.append(f"PRIMARY {result['primary']}")
    for qualifier in result["qualifiers"]:
        lines.append(f"QUALIFIER {qualifier}")
    lines.append(f"LAW-TYPE {canonical_json(measurements['law_type'])}")
    lines.append(f"MEASUREMENTS-SHA256 {digest(measurements)}")
    return "\n".join(lines) + "\n"


def write_new(path: Path, text: str) -> None:
    if path.exists():
        raise FileExistsError(f"refusing to overwrite {path}")
    path.write_text(text, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paper", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--mutant", choices=MUTANTS)
    parser.add_argument("--list-mutants", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.list_mutants:
        print("\n".join(MUTANTS))
        return 0
    if args.selftest:
        dummy = "\n".join(REQUIRED_THEOREMS) + "\n" + "\n".join(
            f"<!-- CLAIM:{claim} -->" for claim in REQUIRED_CLAIMS
        )
        dummy += "\none actual relational record history\nno underlying point set\nRepresentational refinement\nOntic extension\nActualization is postulated\n"
        hashes = dict(FROZEN_HASHES)
        core_receipt = load_json(CORE_RECEIPT)
        reg_receipt = load_json(REG_RECEIPT)
        _, _, mutated_reg, _ = apply_mutant(
            "MUT-INTERFERENCE-DIAGONAL", hashes, core_receipt, reg_receipt, dummy
        )
        # The mutation must make the raw coherent and diagonal weights equal.
        mutated_history = mutated_reg["data"]["history"]
        if mutated_history["coherent_weight"] != mutated_history["diagonal_weight"]:
            raise AssertionError("selftest mutation failed to reach the upstream history object")
        print(f"SELFTEST PASS: scorer exposes {len(MUTANTS)} upstream/document mutants")
        return 0

    if args.paper is None or args.output is None or args.receipt is None:
        raise SystemExit("--paper, --output, and --receipt are required for scoring")

    hashes = {
        "core_source": sha256_path(CORE_SOURCE),
        "core_output": sha256_path(CORE_OUTPUT),
        "core_receipt": sha256_path(CORE_RECEIPT),
        "reg_source": sha256_path(REG_SOURCE),
        "reg_output": sha256_path(REG_OUTPUT),
        "reg_receipt": sha256_path(REG_RECEIPT),
        "pin": sha256_path(PIN),
    }
    core_receipt = load_json(CORE_RECEIPT)
    reg_receipt = load_json(REG_RECEIPT)
    paper = args.paper.read_text(encoding="utf-8")
    if args.mutant:
        hashes, core_receipt, reg_receipt, paper = apply_mutant(
            args.mutant, hashes, core_receipt, reg_receipt, paper
        )

    gates, measurements, result = score(hashes, core_receipt, reg_receipt, paper)
    transcript = render(gates, measurements, result)
    receipt = {
        "schema": "rhl-score-v1",
        "source_hashes": hashes,
        "paper_sha256": hashlib.sha256(paper.encode("utf-8")).hexdigest(),
        "gates": gates,
        "measurements": measurements,
        "result": result,
        "transcript_sha256": hashlib.sha256(transcript.encode("utf-8")).hexdigest(),
    }
    receipt["seals"] = {
        "hashes": digest(receipt["source_hashes"]),
        "gates": digest(receipt["gates"]),
        "measurements": digest(receipt["measurements"]),
        "result": digest(receipt["result"]),
    }

    if args.mutant:
        if result["eligible"] or not result["failed_gates"]:
            print(f"MUTANT ESCAPED {args.mutant}", file=sys.stderr)
            return 2
        print(f"MUTANT REFUSED {args.mutant} :: failed={result['failed_gates']}")
        return 1

    if not result["eligible"]:
        print(transcript, end="", file=sys.stderr)
        return 1
    write_new(args.output, transcript)
    write_new(args.receipt, canonical_json(receipt) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

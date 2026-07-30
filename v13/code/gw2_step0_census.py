#!/usr/bin/env python3
"""GW2 STEP-0 referent census.

This is an exact, standard-library-only type/provenance audit.  It does not
write a regional descent condition.  A substantive negative is a successful
run; only a broken corpus anchor or a failed self-check exits nonzero.
"""

from __future__ import annotations

import ast
import hashlib
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]
AUDITED_BASE = "e89a2e7c972ce3ff6c3a9d4fe5792bf0dac621b2"

LOCKS: Dict[str, Tuple[str, str]] = {
    "GW2 pin": (
        "v13/note-gw2-regional-descent-census-pin.md",
        "48d35ea00c1388c9f67ac06ac12b729b9ad14d64359e704197acbe930957d462",
    ),
    "W3 receipt": (
        "v12/code/w3p_records_exact.py",
        "8dffcc46a96f13c2876453a4765d0dcb29c811b0a18741a0f29dfa65ad2f68db",
    ),
    "W6 receipt": (
        "v12/code/w6_coreference_exact.py",
        "73e99090becb78b6ff39bac4a39a7c182de04fb6e0c36612081d51e59075a66e",
    ),
    "W3 note": (
        "v12/note-w3p-records-kill-defect.md",
        "44936e0abe53cbbbfacf29566f7d83557f323ddbf84dcb5f0c09c6fad6ad970c",
    ),
    "W6 note": (
        "v12/note-w6-record-coreference.md",
        "2f18e863c1930ef2bfd52cf448a8baadd8ceac47696d80e6e4ae2ccf802d37c3",
    ),
    "Paper 2": (
        "v12/paper2-record-coreference.md",
        "d6af0e6513fc7088407dc5a26c513ecc4e9e45b5a5ae71ffa8a9571f274ad670",
    ),
    "v10 D37 receipt": (
        "v10/code/d37_regional_history_specification_exact.py",
        "b15e577bfdf03e1bc78628d9d934bab1e604da9f4b62f7c6372fa61dca7fcbd9",
    ),
    "v10 D38b receipt": (
        "v10/code/d38b_record_closed_specification_exact.py",
        "c48e317189a160d445af374346deb3199caed0ae222430260a55e2a6ef731eeb",
    ),
    "v10 D37 note": (
        "v10/note-d37-regional-history-specifications.md",
        "cfa58b302deb63beec47d45901652055c33147111ea6565f6019e082aa15c15f",
    ),
    "v10 D38 note": (
        "v10/note-d38-record-closed-regional-specifications.md",
        "1a8a7d86908114a4c365c51a509bcdee9b9b5432ab7dee988ab3f894732214f4",
    ),
    "v10 Paper 26": (
        "v10/relativistic-isp-v10-paper26-admissible-regional-history-specifications.md",
        "8a3517aa9138ab9eec1cad04286a990ef84e52cd778a4dcce31ee9cadab67bb4",
    ),
}


class Receipts:
    def __init__(self, mutant: bool = False) -> None:
        self.rows = []
        self.mutant = mutant

    def check(self, label: str, computed: object, expected: object) -> None:
        if self.mutant and label == "live Barandes Region class is present":
            expected = True
            print("[MUTANT] deliberately asserting that a Region class exists")
        ok = computed == expected
        self.rows.append((label, computed, expected, ok))
        print(f"[{'PASS' if ok else 'FAIL'}] {label}: {computed!r}")

    def finish(self) -> int:
        failures = [row for row in self.rows if not row[3]]
        print("-" * 78)
        print(
            f"{len(self.rows)} checks: "
            f"{len(self.rows) - len(failures)} pass, {len(failures)} fail"
        )
        return len(failures)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(command: Sequence[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        tuple(command),
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def python_symbols(relative: str) -> Tuple[Tuple[str, ...], Tuple[str, ...]]:
    tree = ast.parse((ROOT / relative).read_text())
    classes = tuple(sorted(node.name for node in tree.body if isinstance(node, ast.ClassDef)))
    functions = tuple(sorted(node.name for node in tree.body if isinstance(node, ast.FunctionDef)))
    return classes, functions


def init_parameters(relative: str, class_name: str) -> Tuple[str, ...]:
    tree = ast.parse((ROOT / relative).read_text())
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and item.name == "__init__":
                    return tuple(arg.arg for arg in item.args.args if arg.arg != "self")
    raise ValueError(f"missing {class_name}.__init__ in {relative}")


def git_grep(pattern: str) -> Tuple[str, ...]:
    result = run(
        (
            "/usr/bin/git",
            "grep",
            "-l",
            "-E",
            pattern,
            AUDITED_BASE,
            "--",
            "*.py",
        )
    )
    if result.returncode not in (0, 1):
        raise RuntimeError(result.stdout)
    prefix = AUDITED_BASE + ":"
    return tuple(
        sorted(
            line[len(prefix) :] if line.startswith(prefix) else line
            for line in result.stdout.splitlines()
            if line
        )
    )


@dataclass(frozen=True)
class CensusRow:
    number: int
    required_type: str
    barandes_status: str
    old_v10_antecedent: str


def print_census(rows: Iterable[CensusRow]) -> None:
    print("\nSEVEN-OBJECT TYPE CENSUS")
    for row in rows:
        print(
            f"  {row.number}. {row.required_type}: {row.barandes_status}; "
            f"v10={row.old_v10_antecedent}"
        )


def main() -> int:
    receipts = Receipts(mutant="--mutant" in sys.argv[1:])
    print("=" * 78)
    print("v13 GW2 -- REGIONAL DESCENT STEP-0 REFERENT CENSUS")
    print("Exact type/provenance audit; no descent condition is posed")
    print("=" * 78)

    ancestor = run(("/usr/bin/git", "merge-base", "--is-ancestor", AUDITED_BASE, "HEAD"))
    receipts.check("audited programme checkpoint is an ancestor of HEAD", ancestor.returncode, 0)

    locked = tuple((name, sha256(ROOT / relative), expected) for name, (relative, expected) in LOCKS.items())
    receipts.check(
        "all inspected antecedent blobs match their locks",
        tuple((name, actual == expected) for name, actual, expected in locked),
        tuple((name, True) for name, _actual, _expected in locked),
    )

    print("\nANTECEDENT RECEIPTS")
    antecedents = (
        (
            "W3",
            "v12/code/w3p_records_exact.py",
            "gates: 129 run, 129 pass, 0 fail",
        ),
        (
            "W6",
            "v12/code/w6_coreference_exact.py",
            "120 rows (16 ANCHOR, 104 GATE) : 120 pass, 0 fail",
        ),
        (
            "v10 D37",
            "v10/code/d37_regional_history_specification_exact.py",
            "PASS 9/9",
        ),
        (
            "v10 D38b",
            "v10/code/d38b_record_closed_specification_exact.py",
            "PASS 9/9",
        ),
    )
    for name, relative, marker in antecedents:
        result = run((sys.executable, relative))
        receipts.check(f"{name} antecedent exits zero", result.returncode, 0)
        receipts.check(f"{name} antecedent verdict marker", marker in result.stdout, True)

    w3_classes, w3_functions = python_symbols("v12/code/w3p_records_exact.py")
    w6_classes, _w6_functions = python_symbols("v12/code/w6_coreference_exact.py")
    chart_parameters = init_parameters("v12/code/w6_coreference_exact.py", "Chart")
    d37_classes, d37_functions = python_symbols(
        "v10/code/d37_regional_history_specification_exact.py"
    )

    print("\nTYPED LINEAGE SPLIT")
    receipts.check("W3 carries the H-corr decision function", "h_corr" in w3_functions, True)
    receipts.check("W3 carries the H-avail decision function", "h_avail" in w3_functions, True)
    receipts.check("W6 carries a chart type", "Chart" in w6_classes, True)
    live_region_present = "Region" in w3_classes or "Region" in w6_classes
    receipts.check("live Barandes Region class is present", live_region_present, False)
    receipts.check(
        "W6 Chart constructor is process/configuration typed, not region typed",
        chart_parameters,
        ("name", "K", "n", "legs", "j0", "tokens", "note"),
    )
    live_source = "\n".join(
        (ROOT / relative).read_text()
        for relative in (
            "v12/code/w3p_records_exact.py",
            "v12/code/w6_coreference_exact.py",
        )
    )
    regional_identifiers = tuple(
        identifier
        for identifier in ("class Region", "def regions", "gamma_D", "Gamma_D", "r_E_D", "A_R")
        if identifier in live_source
    )
    receipts.check(
        "live W3/W6 code exports no regional constructor/restriction identifier",
        regional_identifiers,
        (),
    )
    receipts.check("v10 carries an oriented-cell type", "OrientedCell" in d37_classes, True)
    receipts.check("v10 carries finite-region enumeration", "regions" in d37_functions, True)
    receipts.check("v10 carries a regional history constructor", "build_typed_history" in d37_functions, True)
    receipts.check("v10 does not carry W3 H-corr", "h_corr" in d37_functions, False)
    receipts.check("v10 does not carry W3 H-avail", "h_avail" in d37_functions, False)

    d37_note = (ROOT / "v10/note-d37-regional-history-specifications.md").read_text()
    d38_note = (ROOT / "v10/note-d38-record-closed-regional-specifications.md").read_text()
    paper26 = (
        ROOT / "v10/relativistic-isp-v10-paper26-admissible-regional-history-specifications.md"
    ).read_text()
    paper2 = (ROOT / "v12/paper2-record-coreference.md").read_text()
    receipts.check(
        "v10 D37 explicitly remains classical",
        "D37 and Paper 26 remain classical." in d37_note,
        True,
    )
    receipts.check(
        "v10 D37 explicitly defers a quantum lift",
        "A future quantum lift must use" in d37_note,
        True,
    )
    receipts.check(
        "v10 D38 explicitly leaves quantum joins open",
        "quantum joins remain open" in d38_note,
        True,
    )
    receipts.check(
        "v10 Paper 26 says its carrier is supplied",
        "The word “supplied” is load-bearing." in paper26,
        True,
    )
    receipts.check(
        "Paper 2 disclaims construction of a universal event set",
        "It does not construct a global present, a universal event set" in paper2,
        True,
    )
    receipts.check(
        "Paper 2 disclaims derivation of token stability",
        "does not itself prove that any declared token is a stable physical record" in paper2,
        True,
    )

    regional_files = set(git_grep(r"gamma_D|def regions|SELECTION_CLICK"))
    barandes_files = set(git_grep(r"h_avail|h_corr|class Chart"))
    adapter_hits = tuple(sorted(regional_files & barandes_files))
    receipts.check(
        "no committed Python file co-locates the v10 regional and W3/W6 interfaces",
        adapter_hits,
        (),
    )

    rows = (
        CensusRow(
            1,
            "finite region D",
            "BLOCKED -- W3/W6 exports Chart, not a spacetime region",
            "LOCATED only on a supplied classical opportunity carrier",
        ),
        CensusRow(
            2,
            "local process P_D",
            "NOT REACHED -- no live D on which to index it",
            "gamma_D / Gamma_D exist at the old classical type",
        ),
        CensusRow(
            3,
            "W3-grade stable-record algebra A_R(D)",
            "SPLIT -- R_a exists chart-locally, not region-indexed",
            "durable clicks are not an H-corr/H-avail adapter",
        ),
        CensusRow(
            4,
            "physical overlap/common access",
            "SPLIT -- W6 overlap is chart-to-chart only",
            "set overlap inherits supplied carrier identities",
        ),
        CensusRow(
            5,
            "restriction/comparison maps",
            "SPLIT -- no maps between live regional record algebras",
            "r_E,D exists only in the old specification",
        ),
        CensusRow(
            6,
            "declared gauge",
            "SPLIT -- W6 configuration relabelling is not regional transport",
            "construction-order gauge exists separately",
        ),
        CensusRow(
            7,
            "insertion discriminator",
            "LOCATED -- W6 five-valued discriminator applies",
            "it rejects promoting old labels into physical identity",
        ),
    )
    print_census(rows)

    computed_verdict = "GW2-BLOCKED-AT-1" if not live_region_present else "GW2-CENSUS-COMPLETE"
    receipts.check("pre-registered GW2 verdict", computed_verdict, "GW2-BLOCKED-AT-1")

    print("\nVERDICT")
    print("  GW2-BLOCKED-AT-1")
    print("  Missing object: a finite region in the live Barandes/W3-W6 record lineage.")
    print("  v10 supplies a classical regional-specification antecedent, not that object.")
    print("  No regional descent condition is written; Z_D remains candidate notation.")

    failures = receipts.finish()
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

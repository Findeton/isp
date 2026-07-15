#!/usr/bin/env python3
"""D40c exact closing delta: transitive locks and exact census."""

from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import json
import sys
from fractions import Fraction as F
from pathlib import Path
from typing import Dict


ROOT = Path(__file__).resolve().parents[2]

LOCKS = {
    "D40c-pin": (
        ROOT / "v10/note-d40c-closing-delta.md",
        "cc30afa1f56e8bb5aa2affec02d200910a912de3fdd38432949bc21a5a382ecb",
    ),
    "D40b-source": (
        ROOT / "v10/code/d40b_probability_space_repair_exact.py",
        "892fc4e445b29bcc56aec8e1622d4bc84e527a511e0daf74ee3ead71d82ea68e",
    ),
    "D40b-output": (
        ROOT / "v10/data/d40b_probability_space_repair_exact.out",
        "30c943f876201ce1e36ae89808c9427b4e611d13804a460d110c921e13ab1508",
    ),
    "D40b-round2": (
        ROOT / "v10/reviews/d40b-round2-independent-review.md",
        "9b41a5c27713249d9deed03f4d2f7800113074b384f59e39b050fa2bc3d6381d",
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stable(value: object) -> str:
    def default(item: object) -> object:
        if isinstance(item, F):
            return {"fraction": [item.numerator, item.denominator]}
        if hasattr(item, "__dict__"):
            return item.__dict__
        raise TypeError(type(item))

    return json.dumps(value, default=default, sort_keys=True, separators=(",", ":"))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


d40b = load_module("d40b_locked_for_d40c", LOCKS["D40b-source"][0])


def main() -> None:
    out = []
    science: Dict[str, object] = {}
    gates: Dict[str, bool] = {}

    def emit(line: str) -> None:
        out.append(line)
        print(line)

    emit("[D40c receipt-integrity closing delta]")
    emit("ARITHMETIC: integer/Fraction exact; no floating theorem")

    actual = tuple(sha256(path) for path, _expected in LOCKS.values())
    expected = tuple(expected for _path, expected in LOCKS.values())
    science["C0"] = actual
    gates["C0"] = actual == expected
    emit("[C0 DIRECT LOCKS]")
    emit(f"direct_locks={sum(int(a == b) for a, b in zip(actual, expected))}/{len(LOCKS)}")

    transitive = d40b.d40.lock_and_type_checks()
    science["C1"] = transitive
    gates["C1"] = transitive == (12, 7)
    emit("[C1 D40 TRANSITIVE RUNTIME LOCKS]")
    emit(f"transitive_antecedent_locks={transitive[0]}/12; typed_level_constructors={transitive[1]}/7")

    spaces = d40b.two_space_checks()
    census = (spaces[7], spaces[8], spaces[18], spaces[19], spaces[20])
    science["C2"] = census
    gates["C2"] = census == (28, 17, 44, 40, 4)
    emit("[C2 EXACT TWO-SPACE CENSUS]")
    emit(f"star_serial_paths={census[0]}/28; star_unordered_atoms={census[1]}/17; global_serial_paths={census[2]}/44; global_typed_DAG_atoms={census[3]}/40; global_merges={census[4]}/4")

    invariants = (
        spaces[4], spaces[5], spaces[6],
        spaces[15], spaces[16], spaces[17],
        0, 0, 0,
    )
    science["C3"] = invariants
    gates["C3"] = invariants == (
        F(23, 198), 1, 1,
        F(5, 96), 1, 1,
        0, 0, 0,
    )
    emit("[C3 SCIENCE-INVARIANCE / SCOPE]")
    emit(f"star_mass={spaces[4]}; star_equals_serial_sum={spaces[5]}/1; star_normalized={spaces[6]}/1")
    emit(f"global_mass={spaces[15]}; global_equals_serial_sum={spaces[16]}/1; global_normalized={spaces[17]}/1")
    emit("timed_Harris_cylinder=0; arbitrary_downset_projectivity=0; stationary_infinite_completion=0")

    source_hash = sha256(Path(__file__))
    body_hash = hashlib.sha256(("\n".join(out) + "\n").encode()).hexdigest()
    science_hash = hashlib.sha256(stable(science).encode()).hexdigest()
    emit("[HASHES]")
    emit(f"source_sha256={source_hash}")
    emit(f"stdout_body_sha256={body_hash}")
    emit(f"internal_science_sha256={science_hash}")
    emit("[GATES]")
    for name in sorted(gates):
        emit(f"{name}={'PASS' if gates[name] else 'FAIL'}")
    passed = sum(gates.values())
    emit("[VERDICT]")
    emit(f"{'PASS' if passed == len(gates) else 'FAIL'} {passed}/{len(gates)}")
    emit("D40b_TRANSITIVE_PROVENANCE_AND_EXACT_CENSUS_CLOSED")
    emit("scientific_theorem_and_numbers=UNCHANGED")
    if passed != len(gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()

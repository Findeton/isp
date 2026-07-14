#!/usr/bin/env python3
"""Independent two-process replay/integrity gate for D36 and D36b."""

from __future__ import annotations

import hashlib
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CASES = (
    (
        ROOT / "v10/code/d36_birth_coordination_exact.py",
        ROOT / "v10/data/d36_birth_coordination_exact.out",
        "dad183c2e303b0315fa7f452ab1c197569d6983332696421d70f04ba5b3d0743",
    ),
    (
        ROOT / "v10/code/d36b_actor_record_refinement_exact.py",
        ROOT / "v10/data/d36b_actor_record_refinement_exact.out",
        "5813304446d267dc3d08f520f4db991bf6bdb94ae45b1f96a5e0cc2a094996ba",
    ),
)
SEEDS = ("17", "104729")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    checks = 0
    print("[D36 independent replay/integrity receipt]")
    for source, receipt, expected_source in CASES:
        source_hash = sha256(source.read_bytes())
        if source_hash != expected_source:
            raise AssertionError((source.name, source_hash, expected_source))
        committed = receipt.read_bytes()
        outputs = []
        for seed in SEEDS:
            environment = dict(os.environ)
            environment["PYTHONHASHSEED"] = seed
            completed = subprocess.run(
                [sys.executable, str(source)],
                cwd=ROOT,
                env=environment,
                check=True,
                capture_output=True,
            )
            if completed.stderr:
                raise AssertionError((source.name, seed, completed.stderr.decode()))
            outputs.append(completed.stdout)
            checks += 1
        if outputs[0] != outputs[1] or outputs[0] != committed:
            raise AssertionError((source.name, "replay mismatch"))
        checks += 2
        print(
            f"{source.name}: source_sha256={source_hash}; "
            f"stdout_sha256={sha256(committed)}; seeds={SEEDS}; byte_identical=1"
        )
    print(f"PASS {checks}/{checks}")


if __name__ == "__main__":
    main()

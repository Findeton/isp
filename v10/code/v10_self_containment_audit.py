#!/usr/bin/env python3
"""Location/import audit for every v10 investigation executable."""

from __future__ import annotations

import ast
import importlib.util
import sys
import sysconfig
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
V10 = ROOT / "v10"
CODE = V10 / "code"
SOURCES = tuple(sorted(CODE.glob("*.py")))

DECLARED_EXTERNAL = {
    CODE / "d9_drift_matched_dimension.py": {"numpy"},
    CODE / "d9_frozen_packet_geometry.py": {"numpy"},
    CODE / "d11_generated_history_geometry.py": {"numpy"},
    CODE / "d13_local_action_family_exact.py": {"sympy"},
}


def import_roots(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    roots: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            roots.add(node.module.split(".")[0])
    return roots


def is_stdlib(root: str) -> bool:
    declared = getattr(sys, "stdlib_module_names", None)
    if declared is not None:
        return root in declared
    if root in sys.builtin_module_names:
        return True
    spec = importlib.util.find_spec(root)
    if spec is None or spec.origin is None:
        return False
    if spec.origin in {"built-in", "frozen"}:
        return True
    origin = Path(spec.origin).resolve()
    stdlib = Path(sysconfig.get_paths()["stdlib"]).resolve()
    return str(origin).startswith(str(stdlib)) and "site-packages" not in origin.parts


def main() -> None:
    assert all(path.is_file() and path.parent == CODE for path in SOURCES)
    expected_names = {path.name for path in SOURCES}
    duplicates = []
    for path in ROOT.rglob("*.py"):
        if ".git" in path.parts:
            continue
        if path.name in expected_names and path.resolve() not in SOURCES:
            duplicates.append(path)
    assert duplicates == [], duplicates

    undeclared_nonstdlib = {}
    local_modules = {path.stem for path in SOURCES}
    for path in SOURCES:
        allowed = DECLARED_EXTERNAL.get(path, set())
        bad = sorted(
            root
            for root in import_roots(path)
            if root != "__future__"
            and root not in local_modules
            and not is_stdlib(root)
            and root not in allowed
        )
        if bad:
            undeclared_nonstdlib[path.name] = bad
    assert undeclared_nonstdlib == {}, undeclared_nonstdlib

    generated = tuple(V10.rglob("*.pyc"))
    assert generated == (), generated

    print("PASS: all v10 investigation executables reside in v10/code")
    print("PASS: no duplicate investigation source exists outside v10/code")
    print("PASS: imports are standard-library, local v10 modules, or explicitly declared numpy/sympy runtimes")
    print("PASS: no .pyc cache artifact exists under v10")
    print("RECEIPT: 4/4 self-containment checks passed")


if __name__ == "__main__":
    main()

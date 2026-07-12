#!/usr/bin/env python3
"""Deterministic V1--V10 census of action-level claims for D13.

This is an inventory, not an interpretation engine.  It makes the corpus
boundary auditable: every Markdown file is hashed and every file containing
an action-level term is listed with category counts and scope-guard lines.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "v10" / "data" / "d13-corpus-action-inventory.json"
EXPECTED_FILES = 522
EXPECTED_RELEVANT = 499
EXPECTED_CORPUS_SHA256 = "bc95bed456aca8d8e65af121ac2f4f5069bcd70b4bd6685e5d02a32b242d0c91"

CATEGORIES = {
    "action": r"\b(action|lagrangian|variational|stationary action)\b",
    "amplitude": r"\b(amplitude|path integral|sum over histories|class operator)\b",
    "hamiltonian": r"\b(hamiltonian|unitary|kraus|instrument kernel)\b",
    "history_law": r"\b(history law|path measure|whole-history|decoherence functional|process tensor)\b",
    "diamond_gluing": r"\b(diamond|gluing|composition|boundary|screen|collar)\b",
    "information": r"\b(Radon.Nikodym|\bRN\b|KL|Fisher|evidence|maximum entropy|maximum caliber)\b",
    "gravity": r"\b(Einstein.Hilbert|Benincasa.Dowker|Regge|Lovelock|gravity|gravitational)\b",
    "selector": r"\b(unique|uniqueness|select|derive|forced|primitive|postulat|free parameter)\b",
}

SCOPE = re.compile(
    r"(does not|do not claim|not derived|not derive|not fundamental|"
    r"conditional|open|free parameter|postulat|primitive|fails|refut|"
    r"scope guard|scope note)",
    re.IGNORECASE,
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    paths = []
    for version in range(1, 11):
        paths.extend((ROOT / f"v{version}").rglob("*.md"))
    # Freeze the audited antecedent corpus.  D13's own notes, paper, and
    # reviews must not make the V1--D12 census move while D13 is written.
    def antecedent(path):
        rel = path.relative_to(ROOT).as_posix()
        if not rel.startswith("v10/"):
            return True
        if rel in {"v10/PLAN.md", "v10/LOG.md"}:
            return False
        name = path.name.lower()
        return "d13" not in name and "paper14-the-action-behind" not in name

    paths = sorted({p for p in paths if antecedent(p)},
                   key=lambda p: p.relative_to(ROOT).as_posix())

    compiled = {name: re.compile(pattern, re.IGNORECASE) for name, pattern in CATEGORIES.items()}
    relevant = []
    corpus_hash = hashlib.sha256()
    category_file_counts = {name: 0 for name in CATEGORIES}
    category_hit_counts = {name: 0 for name in CATEGORIES}

    for path in paths:
        data = path.read_bytes()
        rel = path.relative_to(ROOT).as_posix()
        corpus_hash.update(rel.encode("utf-8") + b"\0" + data + b"\0")
        text = data.decode("utf-8", errors="replace")
        lines = text.splitlines()
        hits = {name: len(regex.findall(text)) for name, regex in compiled.items()}
        if not any(hits.values()):
            continue
        for name, count in hits.items():
            if count:
                category_file_counts[name] += 1
                category_hit_counts[name] += count
        guards = [
            {"line": number, "text": line.strip()[:500]}
            for number, line in enumerate(lines, 1)
            if SCOPE.search(line)
        ]
        headings = [line.strip()[:300] for line in lines if line.startswith("#")]
        relevant.append(
            {
                "path": rel,
                "sha256": digest(data),
                "lines": len(lines),
                "hits": {name: count for name, count in hits.items() if count},
                "headings": headings,
                "scope_guards": guards,
            }
        )

    corpus_sha = corpus_hash.hexdigest()
    if EXPECTED_FILES is not None and len(paths) != EXPECTED_FILES:
        raise AssertionError((len(paths), EXPECTED_FILES))
    if EXPECTED_RELEVANT is not None and len(relevant) != EXPECTED_RELEVANT:
        raise AssertionError((len(relevant), EXPECTED_RELEVANT))
    if EXPECTED_CORPUS_SHA256 is not None and corpus_sha != EXPECTED_CORPUS_SHA256:
        raise AssertionError((corpus_sha, EXPECTED_CORPUS_SHA256))
    if sum(category_file_counts.values()) < len(relevant):
        raise AssertionError("category accounting cannot cover relevant files")
    if any(not item["hits"] for item in relevant):
        raise AssertionError("relevant file without a category hit")

    packet = {
        "schema": "d13-antecedent-corpus-action-inventory-v2",
        "versions": [f"v{i}" for i in range(1, 11)],
        "boundary": "V1 through V10 D12; D13 self-files and mutable V10 PLAN/LOG excluded",
        "markdown_files_scanned": len(paths),
        "action_relevant_files": len(relevant),
        "category_file_counts": category_file_counts,
        "category_hit_counts": category_hit_counts,
        "corpus_stream_sha256": corpus_sha,
        "inventory_source_sha256": digest(Path(__file__).read_bytes()),
        "files": relevant,
    }
    payload = json.dumps(packet, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(payload, encoding="utf-8")
    print(f"MARKDOWN FILES SCANNED: {len(paths)}")
    print(f"ACTION-RELEVANT FILES: {len(relevant)}")
    print(f"CORPUS STREAM SHA256: {packet['corpus_stream_sha256']}")
    print(f"INVENTORY SHA256: {digest(payload.encode('utf-8'))}")
    print("PASS 1: antecedent boundary excludes D13 self-inclusion")
    print("PASS 2: every relevant file has a nonempty category ledger")
    print("PASS 3: category accounting covers the relevant file set")
    print("PASS 4: full headings and scope guards retained without first-24 truncation")
    print("PASS 5: frozen count/hash gates agree")
    print("CHECKS PASSED: 5/5")


if __name__ == "__main__":
    main()

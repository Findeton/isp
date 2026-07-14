#!/usr/bin/env python3
"""Deterministic pre-D35 census for the timeless next-click investigation.

The program inventories every V1--V10 paper/note artifact existing before
D35, retaining path, content hash, line count, first heading, category hits
and scope-guard count.  It interprets nothing.  The D35 note performs the
scientific routing.
"""

from __future__ import annotations

import hashlib
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CUTOFF_COMMIT = "fc074b9ec4f2c9ecdef28b61c623d89d08e76432"

# Filled after the first deterministic census and then frozen.
EXPECTED_FILES = 441
EXPECTED_RELEVANT = 427
EXPECTED_CORPUS_SHA256 = (
    "b0e4c7e0be1c8587b5f3b35e36a834fa8f485cf4bd7cfbb61331017bcd1541b7"
)

CATEGORIES = {
    "causal_order": re.compile(
        r"\b(causal(?:ity| order| relation| chain| past| future| set)?|"
        r"ancestor|ancestry|predecessor|successor|spacelike|timelike)\b",
        re.IGNORECASE,
    ),
    "next_click": re.compile(
        r"\b(next click|next-click|click law|record click|wire event|"
        r"stopping time|first passage|first arrival)\b",
        re.IGNORECASE,
    ),
    "time_clock": re.compile(
        r"\b(proper time|local time|global time|construction time|clock|"
        r"timeless|time-free|elapsed time|Poisson)\b",
        re.IGNORECASE,
    ),
    "birth_support": re.compile(
        r"\b(birth kernel|record birth|support birth|newborn|new register|"
        r"carrier birth|nucleation|root law|opportunity kernel|extension support)\b",
        re.IGNORECASE,
    ),
    "history_measure": re.compile(
        r"\b(history law|history measure|path measure|whole-history|"
        r"completed histor|sum over histories|decoherence functional|"
        r"cylinder probability|cylinder measure)\b",
        re.IGNORECASE,
    ),
    "diamond_holonomy": re.compile(
        r"\b(diamond|holonomy|Radon.Nikodym|\bRN\b|cocycle|amalgamation|gluing)\b",
        re.IGNORECASE,
    ),
    "gauge_projective": re.compile(
        r"\b(construction-order gauge|discrete general covariance|"
        r"linear extension|projectiv|profinite|stem spectrum|inverse limit|"
        r"bonding map|restriction naturality)\b",
        re.IGNORECASE,
    ),
    "local_boundary": re.compile(
        r"\b(locality|local|collar|boundary|screen|separator|component|"
        r"actor|distributed|message)\b",
        re.IGNORECASE,
    ),
    "memory_markov": re.compile(
        r"\b(Markov|non-Markov|memory|predictive state|sufficient carrier|"
        r"causal state|lumpab)\b",
        re.IGNORECASE,
    ),
    "simulation": re.compile(
        r"\b(simulat|generative|generator|algorithm|Monte Carlo|Gillespie|"
        r"event loop|scheduler|executable|reference implementation)\b",
        re.IGNORECASE,
    ),
    "quantum_reception": re.compile(
        r"\b(isometr|reception|No Silent Erasure|NSE|instrument|Kraus|"
        r"controlled rotation|controlled-Ry|Born)\b",
        re.IGNORECASE,
    ),
}

SCOPE = re.compile(
    r"(does not|do not claim|not derived|not derive|not fundamental|"
    r"conditional|open|free data|free parameter|postulat|primitive|"
    r"fails|refut|scope guard|scope note|supplied|retract|supersed)",
    re.IGNORECASE,
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def primary_artifact(path: Path) -> bool:
    """Select papers and notes, excluding reviews/code/data and D35 self."""
    if any(part in {"reviews", "code", "data", "audit"} for part in path.parts):
        return False
    name = path.name.lower()
    if "d35" in name:
        return False
    is_paper = name.startswith("relativistic-isp-") and "paper" in name
    is_note = name.startswith("note-") or name.startswith("design-note-")
    return (is_paper or is_note) and path.suffix.lower() in {".md", ".tex"}


def clean_field(value: str, limit: int = 180) -> str:
    return " ".join(value.strip().split())[:limit].rstrip().replace("|", "/")


def cutoff_manifest() -> list[Path]:
    """Read the exact pre-D35 path boundary from the pinned repository tree."""
    raw = subprocess.check_output(
        [
            "git",
            "ls-tree",
            "-r",
            "--name-only",
            CUTOFF_COMMIT,
            "--",
            *(f"v{version}" for version in range(1, 11)),
        ],
        cwd=ROOT,
        text=True,
    )
    return sorted(
        (
            ROOT / rel
            for rel in raw.splitlines()
            if rel and primary_artifact(ROOT / rel)
        ),
        key=lambda path: path.relative_to(ROOT).as_posix(),
    )


def cutoff_bytes(path: Path) -> bytes:
    """Read content from the pinned tree, never from the live working tree."""
    rel = path.relative_to(ROOT).as_posix()
    return subprocess.check_output(
        ["git", "cat-file", "blob", f"{CUTOFF_COMMIT}:{rel}"],
        cwd=ROOT,
    )


def main() -> None:
    paths = cutoff_manifest()

    stream = hashlib.sha256()
    rows = []
    category_files = {name: 0 for name in CATEGORIES}
    category_hits = {name: 0 for name in CATEGORIES}
    relevant = 0

    for path in paths:
        data = cutoff_bytes(path)
        rel = path.relative_to(ROOT).as_posix()
        stream.update(rel.encode("utf-8") + b"\0" + data + b"\0")
        text = data.decode("utf-8", errors="replace")
        lines = text.splitlines()
        hits = {name: len(regex.findall(text)) for name, regex in CATEGORIES.items()}
        nonzero = {name: count for name, count in hits.items() if count}
        if nonzero:
            relevant += 1
        for name, count in nonzero.items():
            category_files[name] += 1
            category_hits[name] += count
        headings = [clean_field(line.lstrip("#")) for line in lines if line.startswith("#")]
        title = headings[0] if headings else clean_field(path.stem)
        scope_count = sum(1 for line in lines if SCOPE.search(line))
        rows.append((rel, sha256(data), len(lines), title, nonzero, scope_count))

    corpus_hash = stream.hexdigest()
    if EXPECTED_FILES is not None and len(paths) != EXPECTED_FILES:
        raise AssertionError((len(paths), EXPECTED_FILES))
    if EXPECTED_RELEVANT is not None and relevant != EXPECTED_RELEVANT:
        raise AssertionError((relevant, EXPECTED_RELEVANT))
    if EXPECTED_CORPUS_SHA256 is not None and corpus_hash != EXPECTED_CORPUS_SHA256:
        raise AssertionError((corpus_hash, EXPECTED_CORPUS_SHA256))

    print("[d35 pre-investigation causal/birth/time corpus inventory]")
    print(f"PRIMARY FILES: {len(paths)}")
    print(f"CATEGORY-RELEVANT FILES: {relevant}")
    print(f"PRE-D35 CUTOFF COMMIT: {CUTOFF_COMMIT}")
    print(f"CORPUS STREAM SHA256: {corpus_hash}")
    print(f"INVENTORY SOURCE SHA256: {sha256(Path(__file__).read_bytes())}")
    for name in CATEGORIES:
        print(
            f"CATEGORY {name}: files={category_files[name]} hits={category_hits[name]}"
        )
    print("[FILES]")
    for rel, digest, line_count, title, hits, scope_count in rows:
        hit_text = ",".join(f"{name}:{count}" for name, count in sorted(hits.items()))
        print(
            f"{rel} | sha256={digest} | lines={line_count} | "
            f"scope={scope_count} | cats={hit_text or '-'} | title={title}"
        )
    print("[GATES]")
    print("PASS 1: every selected pre-D35 paper/note is content-hashed")
    print("PASS 2: every category records file and hit counts")
    print("PASS 3: every file retains title, line count and scope-guard count")
    print("PASS 4: reviews/code/data are excluded from the primary-artifact census")
    print("PASS 5: D35 self-files are excluded from the antecedent stream")
    print("PASS 6: later papers/notes are excluded by the pinned pre-D35 tree")
    print("VERDICT: PASS 6/6")


if __name__ == "__main__":
    main()

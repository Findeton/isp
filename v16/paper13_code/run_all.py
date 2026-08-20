#!/usr/bin/env python3
"""Authenticate and replay the exact Paper 13 construction bundle.

This runner contains no scientific implementation.  It authenticates the
frozen evaluator and artifacts, validates the paper-to-receipt map, asks the
frozen evaluator to regenerate the fresh case and official artifacts in a
temporary directory, and compares the resulting bytes.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from typing import Any, Iterable


BUNDLE_DIR = Path(__file__).resolve().parent
ROOT = BUNDLE_DIR.parent.parent
MANIFEST_PATH = BUNDLE_DIR / "manifest.json"
TABLE_PATH = BUNDLE_DIR / "receipts_table.json"


class BundleFailure(RuntimeError):
    """Raised for a failed authentication, coverage, or replay check."""


def fail(message: str) -> None:
    raise BundleFailure(message)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("ascii")


def canonical_hash(value: Any) -> str:
    return sha256_bytes(canonical_json_bytes(value))


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        fail(f"cannot read canonical JSON {path}: {error}")


def relative_path(raw: str) -> Path:
    if type(raw) is not str or not raw:
        fail("manifest path is empty or non-text")
    candidate = Path(raw)
    if candidate.is_absolute() or ".." in candidate.parts:
        fail(f"manifest path escapes the repository: {raw}")
    return ROOT / candidate


def verify_file(row: dict[str, Any]) -> dict[str, Any]:
    expected_keys = {"path", "role", "sha256", "size"}
    if type(row) is not dict or set(row) != expected_keys:
        fail("manifest file row has the wrong schema")
    path = relative_path(row["path"])
    try:
        data = path.read_bytes()
    except OSError as error:
        fail(f"cannot read bound file {row['path']}: {error}")
    observed = sha256_bytes(data)
    if observed != row["sha256"]:
        fail(f"hash mismatch for {row['path']}: {observed}")
    if len(data) != row["size"]:
        fail(f"size mismatch for {row['path']}")
    return {
        "path": row["path"],
        "role": row["role"],
        "sha256": observed,
        "size": len(data),
    }


def verify_manifest() -> tuple[dict[str, Any], tuple[dict[str, Any], ...]]:
    manifest = load_json(MANIFEST_PATH)
    expected_keys = {
        "schema",
        "normalized_payload_sha256",
        "source_freeze_commit",
        "construction_commit",
        "nonce_hex",
        "files",
        "replay",
    }
    if type(manifest) is not dict or set(manifest) != expected_keys:
        fail("manifest has the wrong top-level schema")
    if manifest["schema"] != "p13-paper-bundle-manifest-v1":
        fail("manifest schema is not recognized")
    payload = dict(manifest)
    claimed = payload.pop("normalized_payload_sha256")
    observed = canonical_hash(payload)
    if claimed != observed:
        fail(f"manifest normalized hash mismatch: {observed}")
    if not re.fullmatch(r"[0-9a-f]{64}", manifest["nonce_hex"]):
        fail("manifest nonce is malformed")
    files = manifest["files"]
    if type(files) is not list or not files:
        fail("manifest file list is empty")
    paths = [row.get("path") for row in files if type(row) is dict]
    if len(paths) != len(files) or len(set(paths)) != len(paths):
        fail("manifest paths are missing or duplicated")
    verified = tuple(verify_file(row) for row in files)
    return manifest, verified


def json_pointer(document: Any, pointer: str) -> Any:
    if type(pointer) is not str or not pointer.startswith("/"):
        fail(f"receipt pointer is malformed: {pointer!r}")
    current = document
    for raw in pointer.split("/")[1:]:
        token = raw.replace("~1", "/").replace("~0", "~")
        if type(current) is dict and token in current:
            current = current[token]
        elif type(current) is list and token.isdigit() and int(token) < len(current):
            current = current[int(token)]
        else:
            fail(f"receipt pointer is absent: {pointer}")
    return current


CLAIM_START = re.compile(r"<!-- CLAIM:([A-Z_]+):START -->")
CLAIM_END = re.compile(r"<!-- CLAIM:([A-Z_]+):END -->")
NUMBER = re.compile(r"(?<![A-Za-z_])\d+")
URL = re.compile(r"https?://[^\s)>]+")
RESULT_LABEL = re.compile(r"^### Result ([A-Z])\b", re.MULTILINE)


def mask_urls(text: str) -> str:
    return URL.sub(lambda match: " " * len(match.group(0)), text)


def extract_claim_blocks(text: str) -> dict[str, tuple[int, int, str]]:
    starts = list(CLAIM_START.finditer(text))
    ends = list(CLAIM_END.finditer(text))
    if len(starts) != len(ends):
        fail("paper claim markers are unbalanced")
    blocks: dict[str, tuple[int, int, str]] = {}
    for start, end in zip(starts, ends, strict=True):
        if start.group(1) != end.group(1) or end.start() <= start.end():
            fail("paper claim markers are crossed or mismatched")
        claim_id = start.group(1)
        if claim_id in blocks:
            fail(f"paper claim marker is duplicated: {claim_id}")
        body_start = start.end()
        body_end = end.start()
        blocks[claim_id] = (body_start, body_end, text[body_start:body_end])
    return blocks


def number_multiset_hash(text: str) -> tuple[int, str]:
    tokens = NUMBER.findall(mask_urls(text))
    multiset = tuple(sorted(collections.Counter(tokens).items()))
    return len(tokens), canonical_hash(multiset)


def verify_number_coverage(
    paper: str, blocks: dict[str, tuple[int, int, str]]
) -> int:
    masked = mask_urls(paper)
    count = 0
    spans = tuple((start, end, claim_id) for claim_id, (start, end, _) in blocks.items())
    for match in NUMBER.finditer(masked):
        owners = [claim_id for start, end, claim_id in spans if start <= match.start() < end]
        if len(owners) != 1:
            fail(
                "paper numeric token is not covered exactly once: "
                f"{match.group(0)!r} at offset {match.start()}"
            )
        count += 1
    return count


def verify_forbidden_tokens(paper: str) -> None:
    forbidden = (
        r"\bW[1-7]\b",
        r"\bGW\b",
        r"\bBC\b",
        r"\bU\d+\b",
        r"\bT\d+\b",
        r"\bLOG\b",
        r"\bledger\b",
        r"\bpin\b",
        r"\bhostile\b",
        r"\bterminal\b",
        r"\bgreen-unreviewed\b",
        r"\bISP\b",
        r"\bSHARD\b",
        r"\bv\d+\b",
    )
    masked = mask_urls(paper)
    hits = [pattern for pattern in forbidden if re.search(pattern, masked, re.IGNORECASE)]
    if hits:
        fail(f"paper contains forbidden internal tokens: {hits}")


def math_spans(text: str) -> tuple[tuple[int, int, bool], ...]:
    spans: list[tuple[int, int, bool]] = []
    index = 0
    while index < len(text):
        if text.startswith("$$", index):
            end = text.find("$$", index + 2)
            if end < 0:
                fail("unclosed display-math span")
            spans.append((index, end + 2, True))
            index = end + 2
        elif text[index] == "$":
            end = text.find("$", index + 1)
            if end < 0:
                fail("unclosed inline-math span")
            spans.append((index, end + 1, False))
            index = end + 1
        else:
            index += 1
    return tuple(spans)


def verify_markdown_math(paper: str) -> dict[str, int]:
    spans = math_spans(paper)
    for start, end, display in spans:
        body = paper[start + (2 if display else 1) : end - (2 if display else 1)]
        if not display and (r"\\" in body or "&" in body):
            fail("structured TeX appears in inline math")
        if "psmallmatrix" in body:
            fail("psmallmatrix is forbidden")
    covered = [False] * len(paper)
    for start, end, _ in spans:
        for index in range(start, end):
            covered[index] = True
    for match in re.finditer(r"\\", paper):
        if not covered[match.start()]:
            fail(f"backslash appears outside math at offset {match.start()}")
    for token in (r"\emph", r"\textbf", r"\cite", r"\ref"):
        if token in paper:
            fail(f"text-mode LaTeX token is forbidden: {token}")
    return {
        "display_spans": sum(int(display) for _, _, display in spans),
        "inline_spans": sum(int(not display) for _, _, display in spans),
    }


def verify_receipts_table(
    manifest: dict[str, Any]
) -> tuple[dict[str, Any], dict[str, Any]]:
    table = load_json(TABLE_PATH)
    expected_keys = {
        "schema",
        "paper",
        "receipt",
        "claim_order",
        "claims",
        "external_references",
    }
    if type(table) is not dict or set(table) != expected_keys:
        fail("receipts table has the wrong top-level schema")
    if table["schema"] != "p13-paper-receipts-table-v1":
        fail("receipts table schema is not recognized")

    paper_path = relative_path(table["paper"]["path"])
    receipt_path = relative_path(table["receipt"]["path"])
    paper_bytes = paper_path.read_bytes()
    receipt_bytes = receipt_path.read_bytes()
    if sha256_bytes(paper_bytes) != table["paper"]["sha256"]:
        fail("receipts table paper hash is stale")
    if sha256_bytes(receipt_bytes) != table["receipt"]["sha256"]:
        fail("receipts table receipt hash is stale")
    paper = paper_bytes.decode("utf-8")
    receipt = json.loads(receipt_bytes)

    blocks = extract_claim_blocks(paper)
    claim_order = table["claim_order"]
    claims = table["claims"]
    if type(claim_order) is not list or type(claims) is not dict:
        fail("receipts table claim registry is malformed")
    if claim_order != list(blocks) or set(claim_order) != set(claims):
        fail("paper and receipts table claim keys differ")

    binding_count = 0
    result_labels: list[str] = []
    for claim_id in claim_order:
        row = claims[claim_id]
        expected_row_keys = {
            "kind",
            "scope",
            "block_sha256",
            "number_token_count",
            "number_multiset_sha256",
            "receipt_bindings",
            "result_labels",
        }
        if type(row) is not dict or set(row) != expected_row_keys:
            fail(f"claim row has the wrong schema: {claim_id}")
        block = blocks[claim_id][2]
        if sha256_bytes(block.encode("utf-8")) != row["block_sha256"]:
            fail(f"claim block hash mismatch: {claim_id}")
        token_count, token_hash = number_multiset_hash(block)
        if token_count != row["number_token_count"]:
            fail(f"claim numeric token count mismatch: {claim_id}")
        if token_hash != row["number_multiset_sha256"]:
            fail(f"claim numeric multiset mismatch: {claim_id}")
        bindings = row["receipt_bindings"]
        if type(bindings) is not list:
            fail(f"claim bindings are malformed: {claim_id}")
        if row["kind"] != "external" and not bindings:
            fail(f"scientific claim has no receipt binding: {claim_id}")
        for binding in bindings:
            if type(binding) is not dict or set(binding) != {
                "pointer",
                "value_sha256",
            }:
                fail(f"receipt binding schema is malformed: {claim_id}")
            value = json_pointer(receipt, binding["pointer"])
            if canonical_hash(value) != binding["value_sha256"]:
                fail(f"receipt value hash mismatch: {claim_id} {binding['pointer']}")
            binding_count += 1
        if type(row["result_labels"]) is not list:
            fail(f"result-label list is malformed: {claim_id}")
        for label in row["result_labels"]:
            if block.count(f"### Result {label}") != 1:
                fail(f"result label is absent or duplicated: {label}")
            result_labels.append(label)

    observed_results = RESULT_LABEL.findall(paper)
    if observed_results != result_labels:
        fail("result labels are not consecutive or table-complete")
    if result_labels != [chr(ord("A") + index) for index in range(len(result_labels))]:
        fail("result labels are not consecutive")

    numeric_count = verify_number_coverage(paper, blocks)
    verify_forbidden_tokens(paper)
    math_counts = verify_markdown_math(paper)

    references = table["external_references"]
    if type(references) is not list or not references:
        fail("external reference registry is empty")
    reference_block = blocks.get("REFERENCES", (0, 0, ""))[2]
    body_before_references = paper[: blocks["REFERENCES"][0]]
    for row in references:
        if type(row) is not dict or set(row) != {"author_token", "source_url"}:
            fail("external reference row is malformed")
        if row["author_token"] not in body_before_references:
            fail(f"external reference is not cited in the body: {row['author_token']}")
        if row["author_token"] not in reference_block or row["source_url"] not in reference_block:
            fail(f"external reference entry is incomplete: {row['author_token']}")

    return table, {
        "claim_count": len(claims),
        "receipt_binding_count": binding_count,
        "numeric_token_count": numeric_count,
        "result_labels": result_labels,
        "math": math_counts,
        "fenced_claim_comparison": "RAW-BLOCK-NUMERIC-MULTISET",
    }


def run_command(command: list[str]) -> subprocess.CompletedProcess[bytes]:
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=300,
            check=False,
        )
    except subprocess.TimeoutExpired:
        fail(f"replay command exceeded 300 seconds: {command[1:3]}")
    if completed.returncode != 0:
        tail = completed.stderr.decode("utf-8", errors="replace")[-2000:]
        fail(f"replay command failed ({completed.returncode}): {tail}")
    return completed


def compare_bytes(observed_path: Path, expected_path: Path, label: str) -> str:
    observed = observed_path.read_bytes()
    expected = expected_path.read_bytes()
    if observed != expected:
        fail(
            f"regenerated {label} differs: "
            f"{sha256_bytes(observed)} != {sha256_bytes(expected)}"
        )
    return sha256_bytes(observed)


def replay(manifest: dict[str, Any]) -> dict[str, Any]:
    replay_spec = manifest["replay"]
    expected_keys = {"source", "fresh", "output", "receipt"}
    if type(replay_spec) is not dict or set(replay_spec) != expected_keys:
        fail("manifest replay specification is malformed")
    source = relative_path(replay_spec["source"])
    expected_fresh = relative_path(replay_spec["fresh"])
    expected_output = relative_path(replay_spec["output"])
    expected_receipt = relative_path(replay_spec["receipt"])
    source_hash = sha256_bytes(source.read_bytes())

    with tempfile.TemporaryDirectory(prefix="p13-paper-replay-") as raw_temp:
        temp = Path(raw_temp)
        fresh = temp / expected_fresh.name
        output = temp / expected_output.name
        receipt = temp / expected_receipt.name
        generate = [
            sys.executable,
            str(source),
            "--generate-fresh",
            "--nonce",
            manifest["nonce_hex"],
            "--source-sha",
            source_hash,
            "--fresh-out",
            str(fresh),
        ]
        run_command(generate)
        fresh_hash = compare_bytes(fresh, expected_fresh, "fresh case")

        construct = [
            sys.executable,
            str(source),
            "--run",
            "--fresh",
            str(fresh),
            "--output",
            str(output),
            "--receipt",
            str(receipt),
        ]
        run_command(construct)
        output_hash = compare_bytes(output, expected_output, "output")
        receipt_hash = compare_bytes(receipt, expected_receipt, "receipt")

    return {
        "fresh_sha256": fresh_hash,
        "output_sha256": output_hash,
        "receipt_sha256": receipt_hash,
        "temporary_destinations_removed": not temp.exists(),
    }


def selftest_failure_path(manifest: dict[str, Any]) -> bool:
    first = dict(manifest["files"][0])
    changed = "0" * 64 if first["sha256"] != "0" * 64 else "1" * 64
    first["sha256"] = changed
    try:
        verify_file(first)
    except BundleFailure:
        return True
    return False


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Authenticate and replay the one-Gamma paper bundle"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--verify-only",
        action="store_true",
        help="authenticate artifacts and paper coverage without scientific replay",
    )
    group.add_argument(
        "--selftest",
        action="store_true",
        help="run fast authentication and a deliberate in-memory anchor failure",
    )
    return parser.parse_args(list(argv))


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        manifest, verified_files = verify_manifest()
        _, coverage = verify_receipts_table(manifest)
        result: dict[str, Any] = {
            "schema": "p13-paper-bundle-run-v1",
            "manifest_normalized_payload_sha256": manifest[
                "normalized_payload_sha256"
            ],
            "verified_file_count": len(verified_files),
            "verified_files": verified_files,
            "paper_coverage": coverage,
            "self_anchor_failure": selftest_failure_path(manifest),
            "mode": "selftest" if args.selftest else "verify-only" if args.verify_only else "replay",
        }
        if not result["self_anchor_failure"]:
            fail("deliberate anchor corruption did not fail")
        if not args.selftest and not args.verify_only:
            result["replay"] = replay(manifest)
        print(canonical_json_bytes(result).decode("ascii"))
        return 0
    except BundleFailure as error:
        print(f"BUNDLE-FAILURE: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

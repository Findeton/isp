#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""ERA TEMPLATE — reference implementations for the nine disease families.

v14 TPL (the #267 template sweep), chartered at ledger #371 per #362.
Specification: v14/TEMPLATE.md.  Exposure census: v14/tpl_census.md.

WHAT THIS IS.  Nine families of instrument defect recurred across the v14
panels often enough that four K3 seats independently ruled them
TEMPLATE-SHAPED rather than unit-shaped (LOR #267, NDEP #344, SEC #357,
SEC-2 #361).  This module is the shared cure: one reference implementation
per family, each with a named check that a unit's instrument can adopt, and
each with a positive control demonstrating its own kill.

WHAT THIS IS NOT.  It is not a physics unit, it computes no measurement, it
reads no repository object, and it writes nothing anywhere in the tree.  The
only bytes it ever writes are staged artifacts inside a temporary directory
created by --selfdemo and deleted before exit.

SELF-HOSTING.  `python3.13 v14/code/era_template.py --selfdemo` runs, for
every one of the nine families, a CLEAN control that must pass and one or
more POSITIVE controls (the disease, injected by the panels' own published
recipes) that must die at that family's NAMED check.  A positive control
that passes, or a clean control that dies, fails the demo (exit 1).  Nothing
in the demo is a typed count: every numeral in the demo transcript is
interpolated from the live run.

EXACTNESS.  No floats anywhere; counts are ints and ratios are Fractions.

CLI (#82).  --selfdemo | --selftest | --list-families | --list-checks
Anything else exits 2.  No mode writes into the repository.
"""

from __future__ import annotations

import ast
import collections
import hashlib
import inspect
import io
import json
import os
import re
import sys
import tempfile
from fractions import Fraction

# ---------------------------------------------------------------------------
# 0.  PRIMITIVES
# ---------------------------------------------------------------------------

FAMILIES = (
    ("a", "SEAL-INTEGRITY", "T-SEAL-PROMOTION"),
    ("b", "TRANSCRIPT-BOUND-TO-THE-LEDGER", "T-TRANSCRIPT-BOUND"),
    ("c", "SEMANTIC-WALLS", "T-WALL-SEMANTIC"),
    ("d", "VERBATIM-ANCHORS-CONSUMED", "T-ANCHOR-CONSUMED"),
    ("e", "CLAIMS-BY-EQUALITY-TWO-WAY-TABLE-SIGHTED", "T-CLAIMS-EQUAL"),
    ("f", "SENTENCE-LEVEL-REFERENT-BINDING", "T-REFERENT-BOUND"),
    ("g", "NO-TYPED-COUNTS", "T-NO-TYPED-COUNTS"),
    ("h", "FALSIFIERS-POISON-MEASUREMENTS", "T-FALSIFIER-POISONS"),
    ("i", "READ-SETS-AT-THE-I-O-ACCESSOR", "T-READ-SET"),
)


class CheckFail(Exception):
    """Raised by every reference check.  `check` names the family's gate."""

    def __init__(self, check: str, detail: str):
        super().__init__("%s :: %s" % (check, detail))
        self.check = check
        self.detail = detail


def digest(obj) -> str:
    """Canonical digest of any JSON-able object, 12 hex chars."""
    blob = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:12]


def bytes_digest(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:12]


_MD_PREFIX = re.compile(r"^[ \t]*(?:>[ \t]?|[-*+][ \t]+|\d+\.[ \t]+)+", re.M)


def canon(text: str, fold_case: bool = True) -> str:
    """#125 normalisation, plus the case fold SEC-2 MAJOR-10 bought.

    Whitespace folded, markdown blockquote/list prefixes stripped, emphasis
    markers dropped, and — unless a caller explicitly opts out — case folded,
    so that a negation capitalised as a sentence opener cannot hide.
    """
    t = _MD_PREFIX.sub(" ", text)
    t = t.replace("`", " ").replace("*", " ").replace("_", " ")
    t = re.sub(r"\s+", " ", t)
    if fold_case:
        t = t.casefold()
    return t.strip()


class Ledger:
    """A chained ledger.  Every gate is a row; every row digests its
    predecessor, so a row cannot be inserted, dropped or reordered after the
    fact without moving the head."""

    def __init__(self):
        self.rows: list[dict] = []
        self.head = "0" * 16

    def gate(self, gid: str, statement: str, ok: bool, evidence: str) -> None:
        row = {
            "n": len(self.rows) + 1,
            "gate": gid,
            "statement": statement,
            "evidence": evidence,
            "passed": bool(ok),
        }
        row["prev"] = self.head
        row["row_digest"] = digest(row)
        self.head = hashlib.sha256(
            (self.head + row["row_digest"]).encode("utf-8")
        ).hexdigest()[:16]
        self.rows.append(row)
        if not ok:
            raise CheckFail(gid, evidence)

    def names(self) -> list[str]:
        return [r["gate"] for r in self.rows]

    def pass_rows(self) -> collections.Counter:
        return collections.Counter((r["gate"], r["passed"]) for r in self.rows)

    def recompute_chain(self) -> str:
        head = "0" * 16
        for r in self.rows:
            body = {k: r[k] for k in ("n", "gate", "statement", "evidence", "passed")}
            body["prev"] = head
            if digest(body) != r["row_digest"]:
                raise CheckFail("T-LEDGER-CHAIN", "row %d digest moved" % r["n"])
            head = hashlib.sha256((head + r["row_digest"]).encode("utf-8")).hexdigest()[:16]
        return head


# ---------------------------------------------------------------------------
# (a)  SEAL INTEGRITY  —  T-SEAL-PROMOTION
#
# Evidence: SEC-2 K3 MAJOR-1 (both forms, "the ACT disease"); SPC K3 MAJOR-1
# (post-seal add survives); EPR K3 MAJOR-5 (add + declared-unsealed forgery +
# a seal naming a gate that never ran); NDEP K3 MAJOR-1 (forged key on disk
# at exit 0 under a gate reporting "the manifest is TOTAL"); POT K3 MAJOR-6
# (the twenty declared-unsealed keys forgeable); SEC K3 MAJOR-4 (the
# gate-to-disk seal published but never verified).  Doctrine: RUNBOOK #119 +
# the #148 totality addendum + the #348 amendment adopted at
# note-spc-adjudication.md §9 ("A SEAL MANIFEST IS TOTAL ONLY IF TOTALITY IS
# RECOMPUTED AT PROMOTION TIME"), plus EPR #359's third form (post-close
# edit).
# ---------------------------------------------------------------------------


class Seal:
    """Gate-time seals, verified at promotion, then verified again after it.

    The three lethal forms, all killed here:
      ADD   — a top-level key created after the seal gate (SPC/EPR/NDEP);
      EDIT  — a sealed value mutated after its gate (SEC-2/SEC);
      CLOSE — a sealed value edited after close, between read-back and
              os.replace (EPR #359's third form, EPR K3 MINOR-8's TOCTOU).
    Plus two partition defects: a measured key re-declared unsealed
    (SEC-2 MINOR-1), and a seal naming a gate that never ran (EPR MAJOR-5c).
    """

    CHECK = "T-SEAL-PROMOTION"

    def __init__(self):
        self.seals: dict[str, dict] = {}      # key -> {digest, gate}
        self.unsealed: dict[str, str] = {}    # key -> reason
        self.measured: set[str] = set()       # keys produced by a measurement
        self.closed = False

    # -- gate time ---------------------------------------------------------
    def seal(self, key: str, value, gate: str, measured: bool = True) -> None:
        if self.closed:
            raise CheckFail(self.CHECK, "seal taken after close: %s" % key)
        if key in self.unsealed:
            raise CheckFail(self.CHECK, "key both sealed and declared unsealed: %s" % key)
        self.seals[key] = {"digest": digest(value), "gate": gate}
        if measured:
            self.measured.add(key)

    def declare_unsealed(self, key: str, reason: str) -> None:
        if key in self.seals:
            raise CheckFail(self.CHECK, "key both sealed and declared unsealed: %s" % key)
        if key in self.measured:
            raise CheckFail(
                self.CHECK, "measured key re-declared unsealed: %s" % key
            )
        if not reason.strip():
            raise CheckFail(self.CHECK, "unsealed key with no reason: %s" % key)
        self.unsealed[key] = reason

    def manifest(self) -> dict:
        return {
            "sealed": {k: v["digest"] for k, v in sorted(self.seals.items())},
            "sealed_at_gate": {k: v["gate"] for k, v in sorted(self.seals.items())},
            "declared_unsealed": dict(sorted(self.unsealed.items())),
        }

    # -- promotion time ----------------------------------------------------
    def verify_at_promotion(self, payload: dict, ledger: Ledger, manifest_key: str) -> None:
        """The whole of the #348 amendment, executed at the door.

        Never a re-derivation from the payload: each sealed key is compared
        against the digest taken WHEN ITS GATE PASSED, and totality is
        RECOMPUTED from the payload's live key set rather than read off a
        snapshot taken earlier.
        """
        moved = [
            k for k, s in self.seals.items()
            if k not in payload or digest(payload[k]) != s["digest"]
        ]
        if moved:
            raise CheckFail(self.CHECK, "sealed values moved after their gate: %s" % moved)

        gates = set(ledger.names())
        phantom = sorted(k for k, s in self.seals.items() if s["gate"] not in gates)
        if phantom:
            raise CheckFail(self.CHECK, "seal names a gate that never ran: %s" % phantom)

        covered = set(self.seals) | set(self.unsealed) | {manifest_key}
        published = set(payload)
        undeclared = sorted(published - covered)
        absent = sorted(set(self.seals) - published)
        if undeclared:
            raise CheckFail(self.CHECK, "keys published but neither sealed nor declared: %s" % undeclared)
        if absent:
            raise CheckFail(self.CHECK, "sealed key absent from the payload: %s" % absent)

    def close(self) -> None:
        self.closed = True

    def verify_after_promotion(self, paths: dict[str, str], manifest_key: str) -> None:
        """Re-read the promoted receipt FROM DISK and re-verify every seal.

        This is the leg EPR K3 MINOR-8 showed missing: a corruption landed
        between the read-back and os.replace promotes clean without it.
        """
        with open(paths["receipt"], "rb") as fh:
            on_disk = json.loads(fh.read().decode("utf-8"))
        moved = [
            k for k, s in self.seals.items()
            if k not in on_disk or digest(on_disk[k]) != s["digest"]
        ]
        if moved:
            raise CheckFail(self.CHECK, "post-close edit reached disk: %s" % moved)
        covered = set(self.seals) | set(self.unsealed) | {manifest_key}
        undeclared = sorted(set(on_disk) - covered)
        if undeclared:
            raise CheckFail(self.CHECK, "post-close add reached disk: %s" % undeclared)


def promote(seal: Seal, ledger: Ledger, payload: dict, side_text: str,
            receipt_path: str, side_path: str, manifest_key: str = "seal_manifest",
            tamper=None) -> dict:
    """Stage, verify against the GATE-TIME seals, promote, re-verify from disk.

    `side_text`/`side_path` are the run's second artifact — the transcript in
    most units, the rendered census in this one.  `tamper` is the demo's hook
    for injecting a post-close edit between the read-back and os.replace;
    production instruments pass None.
    """
    seal.verify_at_promotion(payload, ledger, manifest_key)
    seal.close()

    body = dict(payload)
    body[manifest_key] = seal.manifest()
    blob = json.dumps(body, sort_keys=True, indent=1, ensure_ascii=False).encode("utf-8")
    ttxt = side_text.encode("utf-8")

    tmp_r, tmp_t = receipt_path + ".tmp", side_path + ".tmp"
    try:
        with open(tmp_r, "wb") as fh:
            fh.write(blob)
        with open(tmp_t, "wb") as fh:
            fh.write(ttxt)
        with open(tmp_r, "rb") as fh:
            back_r = fh.read()
        with open(tmp_t, "rb") as fh:
            back_t = fh.read()
        if back_r != blob or back_t != ttxt:
            raise CheckFail(Seal.CHECK, "staged bytes differ from the sealed render")
        if tamper is not None:                       # the demo's post-close edit
            tamper(tmp_r)
        os.replace(tmp_r, receipt_path)
        os.replace(tmp_t, side_path)
    finally:
        for p in (tmp_r, tmp_t):
            if os.path.exists(p):
                os.unlink(p)                          # POT MAJOR-10: no residue
    seal.verify_after_promotion({"receipt": receipt_path}, manifest_key)
    return {"receipt": bytes_digest(blob), "side": bytes_digest(ttxt)}


# ---------------------------------------------------------------------------
# (b)  TRANSCRIPT BOUND TO THE LEDGER  —  T-TRANSCRIPT-BOUND
#
# Evidence: SEC-2 K3 MAJOR-9 (forged PASS line, forged measured number and an
# invented gate row all survive; 42 published rows against 45 fired gates);
# NDEP K3 MAJOR-2 (the rendered evidence is free — the transcript says 99
# where the receipt says 45); EPR K3 MAJOR-6 (a forged staged line promoted
# beside a byte-perfect receipt; the "gate-time seal" recomputed at
# promotion); POT K3 MAJOR-7 (a PASS line for a gate that does not exist);
# LOR K3 MAJOR-5 (transcript integrity 40/221).
# ---------------------------------------------------------------------------


class Transcript:
    """Human-readable transcript, bound to the ledger BY CONTENT.

    Every `[PASS]`/`[FAIL]` line is parsed back out of the finished text and
    reconciled with the ledger as a MULTISET, evidence included; the row
    count is reconciled with the gates fired; and the whole transcript — not
    a 40-line prefix — is digested at close and that digest is what the
    promoted bytes are compared against.
    """

    CHECK = "T-TRANSCRIPT-BOUND"
    LINE = re.compile(r"^\s*\[(PASS|FAIL)\] (\S+) :: (.*)$")

    def __init__(self):
        self.lines: list[str] = []

    def say(self, text: str) -> None:
        self.lines.append(text)

    def row(self, gid: str, ok: bool, evidence: str) -> None:
        self.lines.append("  [%s] %s :: %s" % ("PASS" if ok else "FAIL", gid, evidence))

    def text(self) -> str:
        return "\n".join(self.lines) + "\n"

    def parse(self, text: str | None = None) -> collections.Counter:
        src = self.text() if text is None else text
        out = collections.Counter()
        for line in src.splitlines():
            m = self.LINE.match(line)
            if m:
                out[(m.group(2), m.group(1) == "PASS", m.group(3))] += 1
        return out

    def bind(self, ledger: Ledger, text: str | None = None) -> str:
        want = collections.Counter(
            (r["gate"], r["passed"], r["evidence"]) for r in ledger.rows
        )
        got = self.parse(text)
        missing = sorted(k[0] for k in (want - got).elements())
        stray = sorted(k[0] for k in (got - want).elements())
        if missing or stray:
            raise CheckFail(
                self.CHECK,
                "transcript rows not the ledger's: missing %s stray %s" % (missing, stray),
            )
        if sum(got.values()) != len(ledger.rows):
            raise CheckFail(
                self.CHECK,
                "transcript carries %d gate lines against %d ledger rows"
                % (sum(got.values()), len(ledger.rows)),
            )
        return bytes_digest((self.text() if text is None else text).encode("utf-8"))


# ---------------------------------------------------------------------------
# (c)  SEMANTIC WALLS  —  T-WALL-SEMANTIC
#
# Evidence: EPR K3 MAJOR-7 (a seven-string blacklist defeated by re-voicing;
# the paper may delete its own wall sentence and pass); NDEP K3 MAJOR-6 (4 of
# 5 natural violations pass literal-phrase traps) and m6 (polarity negatives
# the same species); POT K3 MAJOR-1/2 (the licence wall licenses itself; a
# licensed-looking sentence with wrong values passes); SEC-2 K3 MAJOR-10
# (case-sensitive polarity) and MAJOR-8 (walls pass vacuously on empty text);
# LOR K3 MAJOR-1 + #269's caveat (the three reading walls never scan the
# paper; a green sweep is not evidence a wall holds).
# ---------------------------------------------------------------------------


class SemanticWall:
    """A wall with four legs, all of which must hold.

      NEGATIVE  — voice-normalised REGEX patterns, not literal strings, run
                  against the case-folded paper (the active voice, the
                  paraphrase and the capitalised negation all match).
      POSITIVE  — sentences the paper MUST carry: deleting the wall's own
                  standing verdict is itself a violation.
      SELF-SEAL — the pattern list and the positive legs are published and
                  digested, so a wall cannot be silently narrowed.
      NON-VACUOUS — empty or absent text FAILS; it never passes by default.

    Licence walls additionally take `licence_of`: the policed word may not
    license itself (POT MAJOR-1), and the licence must be a rendered claim
    string rather than a bare token (POT MAJOR-2).
    """

    CHECK = "T-WALL-SEMANTIC"

    def __init__(self, name: str, negative: list[str], positive: list[str],
                 policed: tuple[str, ...] = (), licences: tuple[str, ...] = ()):
        self.name = name
        self.negative = list(negative)
        self.positive = list(positive)
        self.policed = tuple(policed)
        self.licences = tuple(licences)
        for pat in self.negative + self.positive:
            re.compile(pat)                    # a wall pattern must compile
        bad = [t for t in self.licences
               if any(w in t.casefold() for w in self.policed)]
        if bad:
            raise CheckFail(self.CHECK, "self-licensing token set: %s" % bad)

    def seal_value(self) -> dict:
        return {"name": self.name, "negative": self.negative,
                "positive": self.positive, "licences": list(self.licences)}

    def scan(self, paper_text: str, claims: list[str] | None = None) -> None:
        if not paper_text or not paper_text.strip():
            raise CheckFail(self.CHECK, "%s scanned no text (vacuous pass)" % self.name)
        hay = canon(paper_text)
        hits = [p for p in self.negative if re.search(p, hay)]
        if hits:
            raise CheckFail(self.CHECK, "%s: banned pattern matched %s" % (self.name, hits))
        gone = [p for p in self.positive if not re.search(p, hay)]
        if gone:
            raise CheckFail(self.CHECK, "%s: required standing sentence absent %s" % (self.name, gone))
        if self.policed:
            self._licence_leg(paper_text, claims or [])

    def _licence_leg(self, paper_text: str, claims: list[str]) -> None:
        cclaims = [canon(c) for c in claims]
        for sentence in re.split(r"(?<=[.!?])\s+", paper_text):
            s = canon(sentence)
            if not any(re.search(r"\b%s" % w, s) for w in self.policed):
                continue
            if not any(c and c in s for c in cclaims):
                raise CheckFail(
                    self.CHECK,
                    "%s: policed sentence carries no rendered claim :: %s"
                    % (self.name, sentence.strip()[:90]),
                )


# ---------------------------------------------------------------------------
# (d)  VERBATIM ANCHORS CONSUMED  —  T-ANCHOR-CONSUMED
#
# Evidence: POT K3 MAJOR-9 (0 of 15 verbatim anchors consumed by their named
# gate; `vb` never subscripted); NDEP K3 MAJOR-4 (all six phantom, proven by
# a 3-leaf receipt diff — no measured quantity moves); EPR K3 probe 6
# (`consumed_by` written once and never read again in 3,511 lines); SEC-2 K3
# MINOR-3/4 (a fabricated consumer name passes; 7 of 8 anchors discarded);
# SEC K3 MAJOR-5 (five anchors verified on the wrong side).
# ---------------------------------------------------------------------------


class Anchor:
    def __init__(self, name: str, needle: str, source: str, consumer: str,
                 floor: int = 40):
        self.name = name
        self.needle = needle
        self.source = source
        self.consumer = consumer
        self.floor = floor
        self.text: str | None = None
        self.read_by: set[str] = set()


class AnchorSet:
    """Anchors located in their source AND in the paper, then CONSUMED.

    `read()` is the only accessor, and it records who read what.  An anchor
    whose declared consumer never subscripted it is a phantom consumer and
    dies here — the panels' recurring finding that anchors are matched and
    then nothing they were matched for consumes them.
    """

    CHECK = "T-ANCHOR-CONSUMED"

    def __init__(self, anchors: list[Anchor]):
        self.by_name = {a.name: a for a in anchors}

    def locate(self, sources: dict[str, str], paper_text: str | None = None) -> None:
        for a in self.by_name.values():
            if len(a.needle) < a.floor:
                raise CheckFail(self.CHECK, "%s: needle under the %d-char floor" % (a.name, a.floor))
            hay = canon(sources[a.source])
            hits = hay.count(canon(a.needle))
            if hits != 1:
                raise CheckFail(self.CHECK, "%s: %d occurrences in %s, want 1" % (a.name, hits, a.source))
            if paper_text is not None:
                # SEC MAJOR-5: the paper's rendering is the other side of the gate
                if canon(a.needle) not in canon(paper_text):
                    raise CheckFail(self.CHECK, "%s: quoted in the paper with different words" % a.name)
            a.text = a.needle

    def read(self, name: str, by_gate: str) -> str:
        a = self.by_name[name]
        if a.text is None:
            raise CheckFail(self.CHECK, "%s read before it was located" % name)
        a.read_by.add(by_gate)
        return a.text

    def verify_consumption(self, ledger: Ledger) -> None:
        gates = set(ledger.names())
        phantom_name = sorted(a.name for a in self.by_name.values() if a.consumer not in gates)
        if phantom_name:
            raise CheckFail(self.CHECK, "consumer gate does not exist: %s" % phantom_name)
        unconsumed = sorted(
            a.name for a in self.by_name.values() if a.consumer not in a.read_by
        )
        if unconsumed:
            raise CheckFail(
                self.CHECK, "declared consumer never subscripted the anchor: %s" % unconsumed
            )


# ---------------------------------------------------------------------------
# (e)  CLAIMS BY EQUALITY, TWO-WAY, TABLE-SIGHTED  —  T-CLAIMS-EQUAL
#
# Evidence: SEC-2 K3 MAJOR-3 (table-blind and one-way: two header swaps and
# two row transplants at exit 0) and MAJOR-4 (E-22 met by containment: a
# ninth fence passes and deleting §9's four fences passes); POT K3 MAJOR-4
# (`hits >= need` with need == 1 while 13 of 39 claims occur 2–3 times) and
# MAJOR-5 (table cells unbound); EPR K3 MAJOR-1 (a table never rendered),
# MAJOR-2 (fences matched zero times), MAJOR-3 (duplicated claims forgeable),
# MINOR-6 (rendered tables containment-gated); NDEP K3 MAJOR-5 (5 of 23 rows
# unbound) and MAJOR-9 (a forged extra fence admitted); SEC K3 MAJOR-1 (12
# forgeries at 37/37); LOR K3 MAJOR-2 (27/40 rows unrendered).  Doctrine:
# RUNBOOK E-22, #20-with-fenced-blocks.
# ---------------------------------------------------------------------------


class Claims:
    """Claims, tables and fences gated by EQUALITY in BOTH directions.

    Rows are keyed BY TABLE, so a row transplanted from one table into
    another is stray in its new home and missing from its old one.  Headers
    are claims like any other row.  Prose claims are gated at their EXACT
    occurrence count, computed from the licensed rendering rather than
    floored at one.  Fenced blocks are gated by multiset equality with a
    declared multiplicity, so both a ninth fence and a deleted fence block
    die.
    """

    CHECK = "T-CLAIMS-EQUAL"
    FENCE = re.compile(r"```[^\n]*\n(.*?)```", re.S)
    ROW = re.compile(r"^\s*\|(.+)\|\s*$", re.M)

    def __init__(self):
        self.rows: list[tuple[str, str, tuple[str, ...]]] = []   # (table, kind, cells)
        self.prose: collections.Counter = collections.Counter()  # canon text -> multiplicity
        self.fences: collections.Counter = collections.Counter()

    # -- rendering ---------------------------------------------------------
    def table(self, table_id: str, header: tuple, rows: list[tuple]) -> str:
        self.rows.append((table_id, "header", tuple(str(c) for c in header)))
        out = ["| " + " | ".join(str(c) for c in header) + " |",
               "|" + "---|" * len(header)]
        for r in rows:
            cells = tuple(str(c) for c in r)
            self.rows.append((table_id, "data", cells))
            out.append("| " + " | ".join(cells) + " |")
        return "\n".join(out)

    def claim(self, text: str, times: int = 1) -> str:
        self.prose[canon(text)] += times
        return text

    def fence(self, text: str, times: int = 1) -> str:
        self.fences[canon(text)] += times
        return "```\n%s\n```" % text

    # -- gating ------------------------------------------------------------
    def gate(self, paper_text: str) -> dict:
        if not paper_text.strip():
            raise CheckFail(self.CHECK, "no paper text (vacuous pass)")
        self._gate_tables(paper_text)
        self._gate_prose(paper_text)
        self._gate_fences(paper_text)
        return {"rows": len(self.rows), "prose": sum(self.prose.values()),
                "fences": sum(self.fences.values())}

    def _paper_tables(self, paper_text: str) -> collections.Counter:
        """Every markdown row in the paper, keyed by the table it sits in."""
        got = collections.Counter()
        tid, kind = 0, "header"
        prev_blank = True
        for line in paper_text.splitlines():
            m = self.ROW.match(line)
            if not m:
                prev_blank = True
                continue
            cells = tuple(c.strip() for c in m.group(1).split("|"))
            if set("".join(cells)) <= set("-: "):
                continue                                   # separator row
            if prev_blank:
                tid += 1
                kind = "header"
                prev_blank = False
            else:
                kind = "data"
            got[(tid, kind, cells)] += 1
        return got

    def _gate_tables(self, paper_text: str) -> None:
        got = self._paper_tables(paper_text)
        want_sets = collections.defaultdict(collections.Counter)
        for t, kind, cells in self.rows:
            want_sets[t][(kind, cells)] += 1
        got_sets = collections.defaultdict(collections.Counter)
        for (tid, kind, cells), n in got.items():
            got_sets[tid][(kind, cells)] += n

        # Match each rendered table to the paper table carrying its header.
        used, problems = set(), []
        for t, want in want_sets.items():
            header = [k for k in want if k[0] == "header"]
            found = None
            for tid, cand in got_sets.items():
                if tid in used:
                    continue
                if header and header[0] in cand:
                    found = tid
                    break
            if found is None:
                problems.append("table %s: header not found in the paper" % t)
                continue
            used.add(found)
            cand = got_sets[found]
            missing = sorted(str(k) for k in (want - cand).elements())
            stray = sorted(str(k) for k in (cand - want).elements())
            if missing or stray:
                problems.append("table %s: missing %s stray %s" % (t, missing, stray))
        loose = sorted(str(tid) for tid in got_sets if tid not in used)
        if loose:
            problems.append("paper tables bound by nothing: %s" % loose)
        if problems:
            raise CheckFail(self.CHECK, "; ".join(problems))

    def _gate_prose(self, paper_text: str) -> None:
        hay = canon(paper_text)
        wrong = []
        for text, need in sorted(self.prose.items()):
            got = hay.count(text)
            if got != need:
                wrong.append("%r occurs %d, licensed %d" % (text[:52], got, need))
        if wrong:
            raise CheckFail(self.CHECK, "claim occurrence counts are not exact: %s" % wrong)

    def _gate_fences(self, paper_text: str) -> None:
        got = collections.Counter(canon(b) for b in self.FENCE.findall(paper_text))
        missing = sorted(k[:44] for k in (self.fences - got).elements())
        stray = sorted(k[:44] for k in (got - self.fences).elements())
        if missing or stray:
            raise CheckFail(
                self.CHECK, "fenced blocks not a multiset match: missing %s stray %s"
                % (missing, stray))


# ---------------------------------------------------------------------------
# (f)  SENTENCE-LEVEL REFERENT BINDING  —  T-REFERENT-BOUND
#
# Evidence: SEC-2 K3 MAJOR-12 (one global registry: "the kernel is 455"
# passes); SPC K3 MAJOR-2 ("156 of 220" delivers green, and a §4 headline
# inversion carried through a full delivery); NDEP K3 MAJOR-7 (the bindings
# are satisfied INSIDE the machine-derived fences — an aggregate predicate
# per #87); POT K3 probe 9 and the residual published at ledger #363; SEC K3
# probe 9 (four numerals from four universes composed into one false
# sentence); EPR K3 MINOR-7 (membership, not truth).
# ---------------------------------------------------------------------------


class ReferentRegistry:
    """Numerals bound to the universe their sentence is about.

    Three properties the panels showed missing:
      PER OCCURRENCE — every occurrence is checked, never `any(...)`, so a
                       correct occurrence elsewhere cannot satisfy a wrong
                       one (#87 for prose);
      PROSE ONLY     — fenced blocks are STRIPPED before the scan, so the
                       run's own verdict fences cannot satisfy the paper's
                       obligations;
      PAIRED         — an "A of B" fraction must be a pair the run actually
                       measured in that universe, not two members of it.
    """

    CHECK = "T-REFERENT-BOUND"
    NOF = re.compile(r"([\d][\d,]*)\s+(?:of|in|out of)\s+([\d][\d,]*)", re.I)
    NUM = re.compile(r"(?<![\w.,/-])(\d[\d,]*)(?![\w/])")

    def __init__(self):
        self.universes: dict[str, dict] = {}

    def universe(self, name: str, nouns: list[str], values: set[int],
                 pairs: set[tuple[int, int]] | None = None) -> None:
        self.universes[name] = {
            "nouns": [n.casefold() for n in nouns],
            "values": set(values),
            "pairs": set(pairs or ()),
        }

    def seal_value(self) -> dict:
        return {n: {"nouns": u["nouns"], "values": sorted(u["values"]),
                    "pairs": sorted(u["pairs"])}
                for n, u in sorted(self.universes.items())}

    @staticmethod
    def prose_only(paper_text: str) -> str:
        return Claims.FENCE.sub(" ", paper_text)

    def _universe_of(self, sentence: str) -> str | None:
        s = canon(sentence)
        for name, u in self.universes.items():
            if any(re.search(r"\b%s" % re.escape(n), s) for n in u["nouns"]):
                return name
        return None

    def gate(self, paper_text: str) -> dict:
        prose = self.prose_only(paper_text)
        checked, offences = 0, []
        for sentence in re.split(r"(?<=[.!?])\s+", prose):
            uname = self._universe_of(sentence)
            if uname is None:
                continue
            u = self.universes[uname]
            for m in self.NOF.finditer(sentence):
                a, b = (int(x.replace(",", "")) for x in m.groups())
                checked += 1
                if (a, b) not in u["pairs"]:
                    offences.append("(%d of %d) is not a measured pair of %s" % (a, b, uname))
            spans = [m.span() for m in self.NOF.finditer(sentence)]
            for m in self.NUM.finditer(sentence):
                if any(s <= m.start() < e for s, e in spans):
                    continue
                v = int(m.group(1).replace(",", ""))
                checked += 1
                if v not in u["values"]:
                    offences.append("%d is not a value of %s" % (v, uname))
        if offences:
            raise CheckFail(self.CHECK, "; ".join(sorted(set(offences))))
        return {"occurrences_checked": checked}


# ---------------------------------------------------------------------------
# (g)  NO TYPED COUNTS  —  T-NO-TYPED-COUNTS
#
# Evidence: SEC-2 K3 MAJOR-13 (`union_min = 1`, a typed constant published as
# a measurement and the whole of criterion 3) and MINOR-9/10 (typed counts
# inside sealed gate statements); LOR K3 MAJOR-3 (three false published
# counts, typed, ungated, self-contradicted); EPR K3 MINOR-5 ("Fifteen
# claims" beside evidence `claims 16`); POT K3 MINOR-5 (nine typed headers);
# SEC K3 MINOR-3/4 (typed head literals, a typed product published in the
# head).  REALIZED HARM: SEC-2's §4.2 declaration-fiber column, typed 27/9
# and false, repaired to the computed 24/8 at ledger #362/#368 — the era's
# only false delivered numerals.  Registered residuals: PER-R's six claim
# templates (#353), EPR's two typed testimony leaves (#359).
# ---------------------------------------------------------------------------


class CountRegistry:
    """Every numeral in a published statement interpolated from a live count.

    `stmt()` refuses a template that types a numeral at all; the numerals
    arrive by name from the registry, which holds only values a measurement
    put there.  `measured()` is how a value enters: a constant that was never
    measured cannot be published as a measurement.
    """

    CHECK = "T-NO-TYPED-COUNTS"
    DIGITS = re.compile(r"(?<![\w])\d+(?![\w])")

    def __init__(self):
        self.values: dict[str, object] = {}
        self.provenance: dict[str, str] = {}
        self.exempt: dict[str, str] = {}

    def measured(self, name: str, value, how: str):
        if not how.strip():
            raise CheckFail(self.CHECK, "%s published with no provenance" % name)
        self.values[name] = value
        self.provenance[name] = how
        return value

    def exempt_token(self, token: str, reason: str) -> None:
        """A declared literal that is not a count (a paper id, a year)."""
        self.exempt[token] = reason

    def stmt(self, template: str, **names) -> str:
        probe = template
        for tok in self.exempt:
            probe = probe.replace(tok, " ")
        probe = re.sub(r"\{[^{}]*\}", " ", probe)
        typed = self.DIGITS.findall(probe)
        if typed:
            raise CheckFail(
                self.CHECK, "typed numeral %s in a published statement: %r" % (typed, template[:64])
            )
        unknown = sorted(k for k in names if k not in self.values)
        if unknown:
            raise CheckFail(self.CHECK, "statement cites unmeasured names: %s" % unknown)
        return template.format(**{k: self.values[k] for k in names})

    def audit_module(self, source: str, statement_callers: tuple[str, ...]) -> list[str]:
        """AST leg: any string literal handed to a gate/statement builder that
        types a numeral is an offender, whatever it says about itself."""
        tree = ast.parse(source)
        out = []
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            fname = getattr(node.func, "attr", None) or getattr(node.func, "id", None)
            if fname not in statement_callers:
                continue
            for arg in node.args:
                if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                    if self.DIGITS.search(arg.value):
                        out.append("line %d: %r" % (node.lineno, arg.value[:56]))
        return out


# ---------------------------------------------------------------------------
# (h)  FALSIFIERS POISON MEASUREMENTS  —  T-FALSIFIER-POISONS
#
# Evidence: SEC-2 K3 MAJOR-7 (six sentinel-shaped falsifiers — `same[0] =
# False`, `floats + ["injected"]` — whose descriptions name a corruption the
# code never performs) and MAJOR-6 (four gates with no falsifier at all;
# G-COVERAGE exempts itself by a snapshot); NDEP K3 MAJOR-10 (`MUT-TABLE`
# description inverted; `MUT-SEAL-GATE` a constant injection; `MUT-SEAL-DROP`
# exempts the leg it should exercise); EPR K3 MAJOR-4 (descriptions never
# matched against behaviour; MUT-REFERENT appends a sentinel); SEC K3 MAJOR-6
# (six untrue waiver forcings — five falsifiers die at an EARLIER gate and
# never reach the gate they are said to falsify) and MINOR-6; POT K3 minors
# 2/3/4; LOR #269's caveat of record.  Doctrine: RUNBOOK E-23, #34
# reachability.
# ---------------------------------------------------------------------------


class Falsifier:
    def __init__(self, name: str, gate: str, description: str, target: str, apply):
        self.name = name
        self.gate = gate
        self.description = description
        self.target = target      # the MEASURED key this recipe must move
        self.apply = apply


class FalsifierHarness:
    """A falsifier is honest only if it moved the measurement it names.

    Each run digests the declared target BEFORE and AFTER the recipe.  A
    recipe that leaves the target byte-identical has poisoned a verdict
    variable rather than a measurement, and dies here — whatever colour its
    badge is.  Death must also occur AT the declared gate (never earlier),
    which is what makes a waiver forcing true.
    """

    CHECK = "T-FALSIFIER-POISONS"

    def __init__(self, falsifiers: list[Falsifier]):
        self.rows = list(falsifiers)

    def run_one(self, f: Falsifier, build) -> dict:
        payload, ledger = build()
        if f.target not in payload:
            raise CheckFail(self.CHECK, "%s names a target the run does not measure: %s"
                            % (f.name, f.target))
        before = digest(payload[f.target])
        died_at, order_before = None, len(ledger.rows)
        try:
            f.apply(payload, ledger)
            after = digest(payload[f.target])
        except CheckFail as exc:
            after = digest(payload[f.target])
            died_at = exc.check
        if after == before:
            raise CheckFail(
                self.CHECK,
                "%s did not move its declared target %s (sentinel-shaped)" % (f.name, f.target),
            )
        if died_at is None:
            try:
                build_gate = getattr(payload, "_gate", None)
                if build_gate:
                    build_gate(payload, ledger)
            except CheckFail as exc:
                died_at = exc.check
        if died_at != f.gate:
            raise CheckFail(
                self.CHECK,
                "%s died at %s, declared %s" % (f.name, died_at, f.gate),
            )
        return {"mutant": f.name, "died_at": died_at, "target_moved": True,
                "gates_before_death": order_before}

    def audit_descriptions(self, source: str) -> list[str]:
        """AST leg for E-23: a hook whose body only assigns a constant to a
        flag, or appends a constant to a list, is a sentinel."""
        tree = ast.parse(source)
        offenders = []
        for node in ast.walk(tree):
            if not isinstance(node, ast.If):
                continue
            test = ast.dump(node.test)
            if "mut" not in test and "MUT-" not in test:
                continue
            for st in node.body:
                if isinstance(st, ast.Assign) and isinstance(st.value, ast.Constant) \
                        and isinstance(st.value.value, bool):
                    offenders.append("line %d: constant-boolean sentinel" % st.lineno)
                if isinstance(st, ast.Expr) and isinstance(st.value, ast.Call):
                    fn = getattr(st.value.func, "attr", "")
                    if fn == "append" and st.value.args and \
                            isinstance(st.value.args[0], ast.Constant):
                        offenders.append("line %d: constant-append sentinel" % st.lineno)
        return offenders

    def coverage(self, ledger: Ledger, waivers: dict[str, str],
                 forcings: dict[str, bool]) -> dict:
        """The denominator is every gate that fired, THIS GATE INCLUDED.

        SEC-2 MAJOR-6's mechanism was a gate list snapshotted before the
        coverage gate appended itself; here the denominator is taken after
        the fact and the coverage gate is inside it.
        """
        targeted = {f.gate for f in self.rows}
        fired = set(ledger.names()) | {"T-FALSIFIER-COVERAGE"}
        uncovered = sorted(g for g in fired if g not in targeted and g not in waivers)
        unforced = sorted(g for g in waivers if not forcings.get(g, False))
        if uncovered:
            raise CheckFail(self.CHECK, "gates with neither falsifier nor waiver: %s" % uncovered)
        if unforced:
            raise CheckFail(self.CHECK, "waivers with no machine-checked forcing: %s" % unforced)
        return {"gates": len(fired), "falsified": len(targeted), "waived": len(waivers)}


# ---------------------------------------------------------------------------
# (i)  READ SETS AT THE I/O ACCESSOR  —  T-READ-SET
#
# Evidence: SEC-2 K3 MAJOR-2 (READLOG appended in a helper; the gate fires
# once, before the anchor loop; a raw open() of the pin's own prohibited file
# walks in; three READLOG.pop() calls quietly remove reads) and MAJOR-8 (two
# declared modes pass vacuously: --verify-paper on an empty file prints PASS);
# SEC K3 MAJOR-3 (the read set is self-declared — `reads` built inside the
# loop over SOURCES, so the comparison is true by construction; injection
# CINJ-B reads the very file the unit abstains from at exit 0); LOR K3
# MAJOR-4 (G-READS-DECLARED positionally vacuous).  Doctrine: RUNBOOK #91.
# ---------------------------------------------------------------------------


class ReadSet:
    """Every read recorded where reads actually happen.

    A `sys.addaudithook` on the `open` event sees a raw `open()` that never
    passes through the instrument's helper — the route two seats walked
    through.  The comparison is order-insensitive (a multiset of relative
    paths) and is taken at the LAST gate, not the first; exemptions are
    declared and must be USED, never popped silently.
    """

    CHECK = "T-READ-SET"

    def __init__(self, root: str):
        self.root = os.path.abspath(root)
        self.log: list[str] = []
        self.active = False
        self.exemptions: dict[str, str] = {}
        self._installed = False

    def install(self) -> None:
        if self._installed:
            return

        def hook(event, args):
            if event == "open" and self.active:
                try:
                    path = os.path.abspath(str(args[0]))
                except Exception:
                    return
                if path.startswith(self.root):
                    self.log.append(os.path.relpath(path, self.root))

        sys.addaudithook(hook)
        self._installed = True

    def exempt(self, rel: str, reason: str) -> None:
        self.exemptions[rel] = reason

    def gate_at_close(self, declared: list[str]) -> dict:
        seen = collections.Counter(
            p for p in self.log if p not in self.exemptions and not p.endswith(".tmp")
        )
        want = collections.Counter(declared)
        stray = sorted(set(seen) - set(want))
        never = sorted(set(want) - set(seen))
        unused = sorted(e for e in self.exemptions if e not in set(self.log))
        if stray:
            raise CheckFail(self.CHECK, "read but not declared: %s" % stray)
        if never:
            raise CheckFail(self.CHECK, "declared but never read: %s" % never)
        if unused:
            raise CheckFail(self.CHECK, "exemption carried and never used: %s" % unused)
        return {"reads": sum(seen.values()), "distinct": len(seen)}


def require_object(mode: str, path: str | None, text: str | None) -> None:
    """No declared mode may pass on an absent or empty object.

    SEC-2 MAJOR-8: `--verify-paper` on an empty file printed PASS and every
    wall passed vacuously on "".
    """
    if path is None or not os.path.exists(path):
        raise CheckFail(ReadSet.CHECK, "%s ran with no object present" % mode)
    if text is None or not text.strip():
        raise CheckFail(ReadSet.CHECK, "%s ran on empty text (vacuous pass)" % mode)


# ---------------------------------------------------------------------------
# THE SELF-DEMO — every family's positive control dies at its named check
# ---------------------------------------------------------------------------


class Demo:
    """Holds the tiny synthetic unit the demo builds and corrupts.

    The 'measurement' is deliberately trivial (a census of three colours over
    nine cells) so the demo is about the perimeter, which is what the nine
    families are about.  Every numeral in the demo transcript is computed
    here and interpolated — none is typed.
    """

    def __init__(self):
        self.cells = tuple(range(9))
        self.colours = {c: ("red", "blue", "green")[c % 3] for c in self.cells}

    # the measurement
    def census(self) -> dict:
        tally = collections.Counter(self.colours.values())
        return {"cells": len(self.cells),
                "tally": {k: tally[k] for k in sorted(tally)},
                "distinct": len(tally)}

    def payload(self) -> dict:
        cen = self.census()
        return {"census": cen,
                "verdict": {"word": "DEMO-CENSUS-EVEN",
                            "distinct": cen["distinct"]}}


def _mk_ledger_and_seal(dm: Demo):
    led, seal = Ledger(), Seal()
    payload = dm.payload()
    seal.seal("census", payload["census"], "G-CENSUS")
    led.gate("G-CENSUS", "the census is taken over every cell", True,
             "cells %d distinct %d" % (payload["census"]["cells"],
                                       payload["census"]["distinct"]))
    seal.seal("verdict", payload["verdict"], "G-VERDICT")
    led.gate("G-VERDICT", "the verdict is derived from the census", True,
             "word %s" % payload["verdict"]["word"])
    return payload, led, seal


def _demo_seal(rec: list) -> None:
    """(a) T-SEAL-PROMOTION: clean promotion, then ADD / EDIT / POST-CLOSE."""
    dm = Demo()
    tmp = tempfile.mkdtemp(prefix="era_template_selfdemo_")
    rpath, tpath = os.path.join(tmp, "receipt.json"), os.path.join(tmp, "output.txt")
    try:
        payload, led, seal = _mk_ledger_and_seal(dm)
        tr = Transcript()
        for r in led.rows:
            tr.row(r["gate"], r["passed"], r["evidence"])
        d = promote(seal, led, payload, tr.text(), rpath, tpath)
        _record(rec, "a", "CLEAN", "clean promotion", True,
                "receipt %s side artifact %s" % (d["receipt"], d["side"]))

        # ADD — SPC MAJOR-1 / NDEP MAJOR-1 / EPR MAJOR-5a
        payload, led, seal = _mk_ledger_and_seal(dm)
        payload["forged_finding"] = {"DEMO": "5-OF-5", "smuggled": 999}
        _expect(rec, "a", "ADD", "a top-level key added after the seal gate",
                Seal.CHECK, lambda: promote(seal, led, payload, "x\n", rpath, tpath))

        # EDIT — SEC-2 MAJOR-1 / SEC MAJOR-4
        payload, led, seal = _mk_ledger_and_seal(dm)
        payload["census"]["tally"]["red"] = 424242
        _expect(rec, "a", "EDIT", "a sealed value mutated after its gate",
                Seal.CHECK, lambda: promote(seal, led, payload, "x\n", rpath, tpath))

        # POST-CLOSE EDIT — EPR #359's third form / EPR K3 MINOR-8
        payload, led, seal = _mk_ledger_and_seal(dm)

        def tamper(staged_path):
            with open(staged_path, "rb") as fh:
                body = json.loads(fh.read().decode("utf-8"))
            body["census"]["cells"] = 4242
            with open(staged_path, "wb") as fh:
                fh.write(json.dumps(body, sort_keys=True, indent=1).encode("utf-8"))

        _expect(rec, "a", "POST-CLOSE", "a sealed value edited between read-back and os.replace",
                Seal.CHECK,
                lambda: promote(seal, led, payload, "x\n", rpath, tpath, tamper=tamper))

        # DE-SEAL — SEC-2 MINOR-1
        payload, led, seal = _mk_ledger_and_seal(dm)
        _expect(rec, "a", "DE-SEAL", "a measured key re-declared unsealed",
                Seal.CHECK,
                lambda: seal.declare_unsealed("census", "forged reason: measured elsewhere"))

        # PHANTOM SEAL GATE — EPR MAJOR-5c
        payload, led, seal = _mk_ledger_and_seal(dm)
        seal.seals["verdict"]["gate"] = "G-A-GATE-THAT-NEVER-RAN"
        _expect(rec, "a", "PHANTOM-GATE", "a seal naming a gate that never ran",
                Seal.CHECK, lambda: promote(seal, led, payload, "x\n", rpath, tpath))
    finally:
        for p in (rpath, tpath, rpath + ".tmp", tpath + ".tmp"):
            if os.path.exists(p):
                os.unlink(p)
        os.rmdir(tmp)


def _demo_transcript(rec: list) -> None:
    """(b) T-TRANSCRIPT-BOUND."""
    dm = Demo()
    payload, led, seal = _mk_ledger_and_seal(dm)
    tr = Transcript()
    for r in led.rows:
        tr.row(r["gate"], r["passed"], r["evidence"])
    _record(rec, "b", "CLEAN", "transcript reconciles with the ledger", True,
            "digest %s over %d rows" % (tr.bind(led), len(led.rows)))

    forged = tr.text().replace("[PASS] G-VERDICT", "[FAIL] G-VERDICT")
    _expect(rec, "b", "FORGED-VERDICT-WORD", "a PASS line rewritten to FAIL",
            Transcript.CHECK, lambda: tr.bind(led, forged))

    number = tr.text().replace("distinct %d" % payload["census"]["distinct"],
                               "distinct 99")
    _expect(rec, "b", "FORGED-EVIDENCE", "a measured number changed in the transcript only",
            Transcript.CHECK, lambda: tr.bind(led, number))

    invented = tr.text() + "  [PASS] G-A-GATE-THAT-NEVER-RAN :: forged\n"
    _expect(rec, "b", "INVENTED-ROW", "a wholly invented gate row appended",
            Transcript.CHECK, lambda: tr.bind(led, invented))

    dropped = "\n".join(l for l in tr.text().splitlines()
                        if "G-CENSUS" not in l) + "\n"
    _expect(rec, "b", "DROPPED-ROW", "a gate row deleted from the transcript",
            Transcript.CHECK, lambda: tr.bind(led, dropped))


WALL = SemanticWall(
    "DEMO-WALL",
    negative=[r"restor\w*\s+(?:\w+\s+){0,3}local realism",
              r"local realism\s+(?:\w+\s+){0,3}(?:is\s+)?restor\w*",
              r"evad\w*\s+(?:the\s+)?bell", r"bell\s+(?:\w+\s+){0,3}evad\w*",
              r"local hidden[- ]variable",
              r"does not apply to this (?:corpus|arena)"],
    positive=[r"this arena is bell-nonlocal"],
)

LICENCE_WALL = SemanticWall(
    "DEMO-LICENCE-WALL",
    negative=[],
    positive=[],
    policed=("confines", "deconfines"),
    licences=("the census carries 3 distinct colours",),
)


def _demo_walls(rec: list) -> None:
    """(c) T-WALL-SEMANTIC."""
    clean = ("The census is taken over nine cells. This arena is Bell-nonlocal, "
             "and no reading here evades that.")
    WALL.scan(clean)
    _record(rec, "c", "CLEAN", "a compliant paper", True,
            "patterns %d positive legs %d" % (len(WALL.negative), len(WALL.positive)))

    _expect(rec, "c", "RE-VOICED", "the active voice the blacklist misses (EPR B1)",
            SemanticWall.CHECK,
            lambda: WALL.scan(clean + " On the measured arms this restores local realism."))
    _expect(rec, "c", "PARAPHRASE", "a Bell-evasion paraphrase (EPR B3)",
            SemanticWall.CHECK,
            lambda: WALL.scan(clean + " The Bell theorem does not apply to this corpus."))
    _expect(rec, "c", "DELETED-LEG", "the paper's own standing sentence deleted (EPR B5)",
            SemanticWall.CHECK,
            lambda: WALL.scan("The census is taken over nine cells."))
    _expect(rec, "c", "EMPTY", "the wall run on empty text (SEC-2 MAJOR-8)",
            SemanticWall.CHECK, lambda: WALL.scan(""))
    _expect(rec, "c", "CAPITALISED", "a negation capitalised as a sentence opener (SEC-2 MAJOR-10)",
            SemanticWall.CHECK,
            lambda: WALL.scan(clean + " Local realism is fully restored on this arena."))

    lic_clean = "The theory confines here, since the census carries 3 distinct colours."
    LICENCE_WALL.scan(lic_clean, claims=["the census carries 3 distinct colours"])
    _record(rec, "c", "CLEAN-LICENCE", "a policed sentence carrying its rendered claim", True,
            "policed words %d" % len(LICENCE_WALL.policed))
    _expect(rec, "c", "SELF-LICENCE", "the policed word licensing itself (POT MAJOR-1)",
            SemanticWall.CHECK,
            lambda: LICENCE_WALL.scan("The theory confines at strong coupling.",
                                      claims=["the census carries 3 distinct colours"]))
    _expect(rec, "c", "SELF-LICENSING-SET", "a licence set containing the policed word",
            SemanticWall.CHECK,
            lambda: SemanticWall("BAD", [], [], policed=("confines",),
                                 licences=("CONFINES", "DECONFINES")))


def _demo_anchors(rec: list) -> None:
    """(d) T-ANCHOR-CONSUMED."""
    needle = ("the record's co-division incidence is carried onto the site "
              "assignments and never into them")
    src = {"parent": "Preamble. " + needle + " And so on."}
    paper = "As the parent has it: " + needle + ". The census follows."

    def build(consumer="G-CENSUS"):
        return AnchorSet([Anchor("A-DEMO", needle, "parent", consumer)])

    aset = build()
    aset.locate(src, paper)
    led = Ledger()
    led.gate("G-CENSUS", "the census reads its anchor", True,
             "anchor chars %d" % len(aset.read("A-DEMO", "G-CENSUS")))
    aset.verify_consumption(led)
    _record(rec, "d", "CLEAN", "an anchor located and consumed by its named gate", True,
            "anchors %d floor %d" % (len(aset.by_name), aset.by_name["A-DEMO"].floor))

    aset = build()
    aset.locate(src, paper)
    led2 = Ledger()
    led2.gate("G-CENSUS", "the gate names the anchor and never reads it", True, "-")
    _expect(rec, "d", "PHANTOM-CONSUMER", "the named gate never subscripts the anchor (POT MAJOR-9)",
            AnchorSet.CHECK, lambda: aset.verify_consumption(led2))

    aset = build("G-A-GATE-THAT-DOES-NOT-EXIST")
    aset.locate(src, paper)
    led3 = Ledger()
    led3.gate("G-CENSUS", "-", True, "-")
    _expect(rec, "d", "FABRICATED-CONSUMER", "a consumer naming no real gate (SEC-2 MINOR-3)",
            AnchorSet.CHECK, lambda: aset.verify_consumption(led3))

    aset = build()
    _expect(rec, "d", "WRONG-SIDE", "the paper's rendering inverted (SEC MAJOR-5)",
            AnchorSet.CHECK,
            lambda: aset.locate(src, paper.replace("onto", "into")))


def _build_claims(dm: Demo):
    cen = dm.census()
    cl = Claims()
    t1 = cl.table("T-TALLY", ("colour", "cells"),
                  [(k, v) for k, v in sorted(cen["tally"].items())])
    t2 = cl.table("T-TOTALS", ("quantity", "value"),
                  [("cells", cen["cells"]), ("distinct", cen["distinct"])])
    c1 = cl.claim("The census runs over %d cells." % cen["cells"], times=2)
    f1 = cl.fence("DEMO-CENSUS<CELLS=%d;DISTINCT=%d>" % (cen["cells"], cen["distinct"]),
                  times=2)
    paper = "\n\n".join([t1, t2, c1, f1, c1, f1])
    return cl, paper


def _demo_claims(rec: list) -> None:
    """(e) T-CLAIMS-EQUAL."""
    dm = Demo()
    cl, paper = _build_claims(dm)
    ev = cl.gate(paper)
    _record(rec, "e", "CLEAN", "tables, claims and fences all bound", True,
            "rows %d claims %d fences %d" % (ev["rows"], ev["prose"], ev["fences"]))

    def fresh():
        return _build_claims(Demo())

    cl, paper = fresh()
    swapped = paper.replace("| colour | cells |", "| quantity | value |", 1)
    _expect(rec, "e", "HEADER-SWAP", "two published tables' headers swapped (SEC-2 MAJOR-3)",
            Claims.CHECK, lambda: cl.gate(swapped))

    cl, paper = fresh()
    row = [l for l in paper.splitlines() if l.startswith("| cells |")][0]
    lines = paper.splitlines()
    lines.insert(lines.index("| red | 3 |") + 1, row)
    _expect(rec, "e", "ROW-TRANSPLANT", "a row moved from one table into another (SEC-2 MAJOR-3)",
            Claims.CHECK, lambda: cl.gate("\n".join(lines)))

    cl, paper = fresh()
    lines = paper.splitlines()
    lines.insert(lines.index("| red | 3 |") + 1, "| red | 3 |")
    _expect(rec, "e", "DUPLICATED-ROW", "a legitimate row duplicated (SEC-2 MAJOR-3)",
            Claims.CHECK, lambda: cl.gate("\n".join(lines)))

    cl, paper = fresh()
    _expect(rec, "e", "TWIN-FORGERY", "one of two copies of a claim corrupted (POT MAJOR-4)",
            Claims.CHECK,
            lambda: cl.gate(paper.replace("The census runs over 9 cells.",
                                          "The census runs over 4 cells.", 1)))

    cl, paper = fresh()
    extra = paper + "\n\n```\nDEMO-EXTRA<CELLS=9;DISTINCT=3>\n```\n"
    _expect(rec, "e", "EXTRA-FENCE", "a fabricated ninth fence (SEC-2 MAJOR-4, NDEP MAJOR-9)",
            Claims.CHECK, lambda: cl.gate(extra))

    cl, paper = fresh()
    first = paper.index("```")
    cut = paper[:first] + paper[paper.index("```", paper.index("```", first) + 3) + 3:]
    _expect(rec, "e", "DELETED-FENCE", "a verdict fence block deleted (SEC-2 MAJOR-4)",
            Claims.CHECK, lambda: cl.gate(cut))

    cl, paper = fresh()
    _expect(rec, "e", "UNRENDERED-TABLE", "a table the instrument never rendered (EPR MAJOR-1)",
            Claims.CHECK,
            lambda: cl.gate(paper + "\n\n| desideratum | verdict |\n|---|---|\n| E1 | met |\n"))


def _mk_referents(dm: Demo) -> ReferentRegistry:
    cen = dm.census()
    rr = ReferentRegistry()
    rr.universe("CELLS", ["cell", "cells"], {cen["cells"]},
                pairs={(cen["cells"], cen["cells"])})
    rr.universe("COLOURS", ["colour", "colours", "distinct"],
                set(cen["tally"].values()) | {cen["distinct"]},
                pairs={(cen["distinct"], cen["distinct"])})
    return rr


def _demo_referents(rec: list) -> None:
    """(f) T-REFERENT-BOUND."""
    dm = Demo()
    rr = _mk_referents(dm)
    clean = ("The census runs over 9 cells. It finds 3 distinct colours, "
             "and 3 of 3 colours are realized.\n\n```\nDEMO<CELLS=9>\n```\n")
    ev = rr.gate(clean)
    _record(rec, "f", "CLEAN", "every occurrence bound to its own universe", True,
            "occurrences checked %d universes %d" % (ev["occurrences_checked"],
                                                     len(rr.universes)))

    _expect(rec, "f", "CROSS-UNIVERSE", "a colour count used as a cell count (SEC-2 MAJOR-12)",
            ReferentRegistry.CHECK,
            lambda: rr.gate(clean.replace("over 9 cells", "over 3 cells")))
    _expect(rec, "f", "WRONG-PAIR", "an in-universe pair the run never measured (EPR MINOR-7)",
            ReferentRegistry.CHECK,
            lambda: rr.gate(clean.replace("3 of 3 colours", "9 of 3 colours")))
    _expect(rec, "f", "FENCE-SATISFIED", "prose corrupted while a fence carries the truth (NDEP MAJOR-7)",
            ReferentRegistry.CHECK,
            lambda: rr.gate(clean.replace("It finds 3 distinct colours",
                                          "It finds 42 distinct colours")))


def _demo_typed(rec: list) -> None:
    """(g) T-NO-TYPED-COUNTS."""
    dm = Demo()
    cen = dm.census()
    reg = CountRegistry()
    reg.measured("cells", cen["cells"], "len(self.cells)")
    reg.measured("distinct", cen["distinct"], "len(Counter(colours))")
    reg.exempt_token("E-22", "a runbook engraving id, not a count")
    s = reg.stmt("the census runs over {cells} cells and finds {distinct} colours "
                 "(E-22 applies)", cells=1, distinct=1)
    _record(rec, "g", "CLEAN", "a gate statement interpolated from live counts", True,
            "statement %r" % s)

    _expect(rec, "g", "TYPED-STATEMENT", "a numeral typed into a sealed gate statement (SEC-2 MINOR-10)",
            CountRegistry.CHECK,
            lambda: reg.stmt("the census runs over 9 cells", ))
    _expect(rec, "g", "UNMEASURED-NAME", "a statement citing a name no measurement produced",
            CountRegistry.CHECK,
            lambda: reg.stmt("the union minimum is {union_min}", union_min=1))
    _expect(rec, "g", "NO-PROVENANCE", "a constant published as a measurement (SEC-2 MAJOR-13)",
            CountRegistry.CHECK, lambda: reg.measured("union_min", 1, ""))

    src = ("def f(led):\n"
           "    led.gate('G-X', 'at 216 of the 288 seam-spanning groups', True, 'x')\n")
    offenders = reg.audit_module(src, statement_callers=("gate",))
    _record(rec, "g", "AST-AUDIT", "the AST leg finds typed numerals in gate statements",
            len(offenders) > 0, "offenders %d :: %s" % (len(offenders), offenders))
    if not offenders:
        raise CheckFail(CountRegistry.CHECK, "the AST leg found nothing to find")


def _demo_falsifiers(rec: list) -> None:
    """(h) T-FALSIFIER-POISONS."""
    dm = Demo()

    def build():
        payload, led, seal = _mk_ledger_and_seal(dm)
        return payload, led

    def honest(payload, led):
        payload["census"]["tally"]["red"] = payload["census"]["tally"]["red"] + 1
        raise CheckFail("G-CENSUS", "tally no longer sums to the cell count")

    def sentinel(payload, led):
        # SEC-2 MAJOR-7's shape: the verdict variable is poisoned, not the object
        same = False
        raise CheckFail("G-CENSUS", "same %s" % same)

    def early(payload, led):
        payload["census"]["cells"] = payload["census"]["cells"] + 1
        raise CheckFail("G-EARLIER-GATE", "died before reaching its declared gate")

    h = FalsifierHarness([Falsifier("MUT-TALLY", "G-CENSUS",
                                    "one colour's tally is moved", "census", honest)])
    row = h.run_one(h.rows[0], build)
    _record(rec, "h", "CLEAN", "a falsifier that moves its declared target", True,
            "mutant %s died at %s" % (row["mutant"], row["died_at"]))

    hs = FalsifierHarness([Falsifier("MUT-SENTINEL", "G-CENSUS",
                                     "the census is corrupted", "census", sentinel)])
    _expect(rec, "h", "SENTINEL", "a falsifier poisoning a verdict variable (SEC-2 MAJOR-7)",
            FalsifierHarness.CHECK, lambda: hs.run_one(hs.rows[0], build))

    he = FalsifierHarness([Falsifier("MUT-EARLY", "G-CENSUS",
                                     "the census is corrupted", "census", early)])
    _expect(rec, "h", "UNREACHED-GATE", "a falsifier dying at an earlier gate (SEC MAJOR-6)",
            FalsifierHarness.CHECK, lambda: he.run_one(he.rows[0], build))

    hm = FalsifierHarness([Falsifier("MUT-ABSENT", "G-CENSUS",
                                     "-", "no_such_key", honest)])
    _expect(rec, "h", "ABSENT-TARGET", "a falsifier naming a target the run never measures",
            FalsifierHarness.CHECK, lambda: hm.run_one(hm.rows[0], build))

    payload, led = build()
    _expect(rec, "h", "UNCOVERED-GATE", "a gate carrying neither falsifier nor waiver (SEC-2 MAJOR-6)",
            FalsifierHarness.CHECK, lambda: h.coverage(led, waivers={}, forcings={}))
    _expect(rec, "h", "UNFORCED-WAIVER", "a waiver with no machine-checked forcing (SEC MAJOR-6)",
            FalsifierHarness.CHECK,
            lambda: h.coverage(led, waivers={"G-VERDICT": "checked elsewhere",
                                             "T-FALSIFIER-COVERAGE": "self"},
                               forcings={"T-FALSIFIER-COVERAGE": True}))
    ev = h.coverage(led, waivers={"G-VERDICT": "derived from the census",
                                  "T-FALSIFIER-COVERAGE": "its own denominator"},
                    forcings={"G-VERDICT": True, "T-FALSIFIER-COVERAGE": True})
    _record(rec, "h", "CLEAN-COVERAGE", "the coverage gate inside its own denominator", True,
            "gates %d falsified %d waived %d" % (ev["gates"], ev["falsified"], ev["waived"]))

    sentinel_src = inspect.getsource(_sentinel_sample)
    offenders = h.audit_descriptions(sentinel_src)
    _record(rec, "h", "AST-AUDIT", "the AST leg finds sentinel-shaped hooks",
            len(offenders) > 0, "offenders %d :: %s" % (len(offenders), offenders))
    if not offenders:
        raise CheckFail(FalsifierHarness.CHECK, "the AST leg found nothing to find")


def _sentinel_sample(mut, same, floats):
    """The two sentinel shapes SEC-2 MAJOR-7 and NDEP MAJOR-10 measured."""
    if mut("MUT-VERDICT"):
        same = False
    if mut("MUT-EXACT-FLOAT"):
        floats.append("injected")
    return same, floats


def _demo_readset(rec: list) -> None:
    """(i) T-READ-SET."""
    tmp = tempfile.mkdtemp(prefix="era_template_reads_")
    declared_path = os.path.join(tmp, "declared.txt")
    forbidden_path = os.path.join(tmp, "forbidden.txt")
    try:
        for p, body in ((declared_path, "declared source\n"),
                        (forbidden_path, "the file the pin forbids\n")):
            with open(p, "w", encoding="utf-8") as fh:
                fh.write(body)

        rs = ReadSet(tmp)
        rs.install()
        rs.active = True
        with open(declared_path, "rb") as fh:      # a raw open, not a helper
            fh.read()
        ev = rs.gate_at_close(["declared.txt"])
        _record(rec, "i", "CLEAN", "the read set recorded at the accessor", True,
                "reads %d distinct %d" % (ev["reads"], ev["distinct"]))

        rs2 = ReadSet(tmp)
        rs2.install()
        rs2.active = True
        with open(declared_path, "rb") as fh:
            fh.read()
        with open(forbidden_path, "rb") as fh:     # SEC CINJ-B / SEC-2 MAJOR-2
            fh.read()
        _expect(rec, "i", "RAW-OPEN", "a raw open() of a forbidden file (SEC MAJOR-3)",
                ReadSet.CHECK, lambda: rs2.gate_at_close(["declared.txt"]))

        rs3 = ReadSet(tmp)
        rs3.install()
        rs3.active = True
        _expect(rec, "i", "DECLARED-NEVER-READ", "a declared source never actually read",
                ReadSet.CHECK, lambda: rs3.gate_at_close(["declared.txt"]))

        rs4 = ReadSet(tmp)
        rs4.install()
        rs4.active = True
        rs4.exempt("never_touched.txt", "carried for a mode this run did not take")
        with open(declared_path, "rb") as fh:
            fh.read()
        _expect(rec, "i", "UNUSED-EXEMPTION", "an exemption carried and never used",
                ReadSet.CHECK, lambda: rs4.gate_at_close(["declared.txt"]))

        empty = os.path.join(tmp, "empty.md")
        with open(empty, "w", encoding="utf-8") as fh:
            fh.write("")
        _expect(rec, "i", "VACUOUS-MODE", "--verify-paper on an empty file (SEC-2 MAJOR-8)",
                ReadSet.CHECK, lambda: require_object("--verify-paper", empty, ""))
        _expect(rec, "i", "ABSENT-OBJECT", "a declared mode run with the paper deleted",
                ReadSet.CHECK,
                lambda: require_object("--no-write", os.path.join(tmp, "gone.md"), "text"))
        rs.active = rs2.active = rs3.active = rs4.active = False
    finally:
        for name in os.listdir(tmp):
            os.unlink(os.path.join(tmp, name))
        os.rmdir(tmp)


# -- demo bookkeeping -------------------------------------------------------


def _record(rec: list, fam: str, tag: str, what: str, ok: bool, evidence: str) -> None:
    rec.append({"family": fam, "control": tag, "kind": "CLEAN" if tag.startswith("CLEAN")
                or tag == "AST-AUDIT" else "POSITIVE",
                "what": what, "ok": bool(ok), "evidence": evidence})


def _expect(rec: list, fam: str, tag: str, what: str, check: str, fn) -> None:
    """A positive control MUST die, and die at its NAMED check."""
    try:
        fn()
    except CheckFail as exc:
        if exc.check != check:
            rec.append({"family": fam, "control": tag, "kind": "POSITIVE", "what": what,
                        "ok": False,
                        "evidence": "died at %s, owed %s" % (exc.check, check)})
            return
        rec.append({"family": fam, "control": tag, "kind": "POSITIVE", "what": what,
                    "ok": True, "evidence": "died at %s :: %s" % (exc.check, exc.detail[:88])})
        return
    rec.append({"family": fam, "control": tag, "kind": "POSITIVE", "what": what,
                "ok": False, "evidence": "SURVIVED — no kill at %s" % check})


DEMOS = {
    "a": _demo_seal, "b": _demo_transcript, "c": _demo_walls, "d": _demo_anchors,
    "e": _demo_claims, "f": _demo_referents, "g": _demo_typed,
    "h": _demo_falsifiers, "i": _demo_readset,
}


def selfdemo(out=sys.stdout) -> int:
    rec: list = []
    for key, _name, _check in FAMILIES:
        DEMOS[key](rec)

    by_family = collections.defaultdict(list)
    for r in rec:
        by_family[r["family"]].append(r)

    out.write("ERA TEMPLATE — SELF-DEMO (v14 TPL, the #267 template sweep)\n")
    out.write("=" * 72 + "\n")
    for key, name, check in FAMILIES:
        rows = by_family[key]
        pos = [r for r in rows if r["kind"] == "POSITIVE"]
        cle = [r for r in rows if r["kind"] == "CLEAN"]
        out.write("\n(%s) %s  —  %s\n" % (key, name, check))
        out.write("    clean controls %d/%d pass; positive controls %d/%d die at the named check\n"
                  % (sum(1 for r in cle if r["ok"]), len(cle),
                     sum(1 for r in pos if r["ok"]), len(pos)))
        for r in rows:
            out.write("      [%s] %-22s %s\n"
                      % ("OK " if r["ok"] else "BAD", r["control"], r["what"]))
            out.write("           %s\n" % r["evidence"])

    total = len(rec)
    good = sum(1 for r in rec if r["ok"])
    pos = sum(1 for r in rec if r["kind"] == "POSITIVE")
    fams = len({r["family"] for r in rec})
    out.write("\n" + "=" * 72 + "\n")
    out.write("families demonstrated %d of %d; controls %d, of which positive %d; "
              "on target %d\n" % (fams, len(FAMILIES), total, pos, good))
    frac = Fraction(good, total)
    out.write("on-target fraction %s (%s)\n"
              % (frac, "COMPLETE" if frac == 1 else "INCOMPLETE"))
    if good != total or fams != len(FAMILIES):
        out.write("SELF-DEMO FAILED\n")
        return 1
    out.write("SELF-DEMO COMPLETE — every family's positive control died at its named check\n")
    return 0


# Each entry disables exactly one family's enforcement.  A renamed CHECK
# constant is NOT a valid corruption — the demo compares against the same
# constant, so both sides move together and nothing is learned (the twinned
# comparator, measured in this instrument's own first selftest run and kept
# here as the reason the corruption is of the ENFORCER, not of its name).
_DISABLERS = {
    "a": (Seal, "verify_at_promotion", lambda self, *a, **k: None),
    "b": (Transcript, "bind", lambda self, ledger, text=None: "disabled"),
    "c": (SemanticWall, "scan", lambda self, *a, **k: None),
    "d": (AnchorSet, "verify_consumption", lambda self, *a, **k: None),
    "e": (Claims, "gate", lambda self, *a, **k: {"rows": 0, "prose": 0, "fences": 0}),
    "f": (ReferentRegistry, "gate", lambda self, *a, **k: {"occurrences_checked": 0}),
    "g": (CountRegistry, "stmt", lambda self, template, **names: template),
    "h": (FalsifierHarness, "run_one", lambda self, f, build: {"mutant": f.name,
                                                              "died_at": f.gate}),
    "i": (ReadSet, "gate_at_close", lambda self, *a, **k: {"reads": 0, "distinct": 0}),
}


def selftest(out=sys.stdout) -> int:
    """Disable each family's enforcement in turn; the demo must go red.

    This is the #34 reachability leg at the template's own hands: a check
    nobody's positive control depends on would survive its own removal.
    Nothing is written outside a temporary directory.
    """
    results = []
    for key, name, check in FAMILIES:
        cls, attr, stub = _DISABLERS[key]
        saved = getattr(cls, attr)
        try:
            setattr(cls, attr, stub)
            try:
                rc = selfdemo(out=io.StringIO())
                how = "rc %d" % rc
                noticed = rc != 0
            except Exception as exc:                     # a crash is also a notice
                how = "raised %s" % type(exc).__name__
                noticed = True
        finally:
            setattr(cls, attr, saved)
        results.append((key, name, check, noticed, how))
        out.write("  [%s] (%s) %-46s %s disabled -> %s\n"
                  % ("OK " if noticed else "BAD", key, name, attr, how))
    rc2 = selfdemo(out=io.StringIO())
    out.write("SELFTEST: restored; the demo %s (rc %d)\n"
              % ("passes" if rc2 == 0 else "FAILS", rc2))
    good = sum(1 for r in results if r[3])
    out.write("SELFTEST: %d of %d enforcements are load-bearing\n"
              % (good, len(results)))
    return 0 if (good == len(results) and rc2 == 0) else 1


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        sys.stderr.write("usage: era_template.py "
                         "--selfdemo|--selftest|--list-families|--list-checks\n")
        return 2
    mode = argv[1]
    if mode == "--selfdemo":
        return selfdemo()
    if mode == "--selftest":
        return selftest()
    if mode == "--list-families":
        for key, name, check in FAMILIES:
            print("(%s) %-46s %s" % (key, name, check))
        return 0
    if mode == "--list-checks":
        for key, name, check in FAMILIES:
            print(check)
        return 0
    sys.stderr.write("unknown argument: %r\n" % mode)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))

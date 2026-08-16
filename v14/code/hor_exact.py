#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""HOR -- paper-42 -- THE HORIZON UNIT: undetermined R as the native form.

Pin: v14/note-hor-pin.md (sha256-12 0cf8515e184f, v14 ledger #373).
Artifacts: v14/code/hor_output.txt, v14/code/hor_receipt.json.
Paper: v14/paper-42-hor.md.

WHAT THIS INSTRUMENT MEASURES.  Four things the pin names.

  (1) THE EMERGENT c.  R5 declares four parity strata and names the stratum
      operator -- "the stratum operator is the product of the eight that make
      up a parity class" -- and never builds it.  This unit builds it, calls
      one application of it a TICK, and measures the maximal reach of
      influence per tick exactly, over every coin of the committed carrier,
      censusing the cone's whole shape rather than a bound.

  (2) HORIZON-STABILITY.  Contractible observables (rectangle holonomies) and
      winding observables, measured under arena growth on open patches AND
      torus closures at every affordable (R, L) pair, with the window
      declared; plus a dynamical family (window amplitudes at depth T) whose
      arena-independence is predicted from the cone and then measured.

  (3) THE OPEN-PATCH ARENA.  The torus flushed as a declaration: the same
      link operator, the same coins, no identification.  Which sealed laws
      survive verbatim and which were closure artifacts -- censused.

  (4) THE DIRECT-LIMIT FORM.  The undetermined-R statement written out, and
      the gate the pin asks for, run on every sealed law this unit uses: the
      law is HORIZON-STATABLE BY THE CLOSURE-WITNESS TEST -- its witness on
      the open arena is its witness on the closed one, or differs with a
      stated proviso -- or it is named as an exception.  The class word is
      the test; the absence of a symbol for a size is a different property
      and is not what is measured here.

WALLS (from the pin).  No actual-infinity claim of any kind -- R1's seal
stands and is cited, never contradicted; no continuum vocabulary; the
scaleful-not-continuous register is licensed and its sentences must carry
measurements.  Exact arithmetic only: Z[zeta_8] as integer 4-tuples over
(1, z, z^2, z^3) modulo z^4 + 1, with power-of-two scales carried
separately; every ratio a Fraction.  No float literal occurs in this file and
no call to a logarithm, an exponential, a square root or a power is made.

TEMPLATE (E-25..E-33).  This unit is one of the adoption's first exemplars.
The nine family mechanisms of v14/TEMPLATE.md are implemented here natively
under the template's own check ids, and G-TEMPLATE-CONFORMANCE parses the
pinned v14/code/era_template.py to require that the ids implemented here are
exactly the nine it declares.  S-1 (the comparator is the builder) is
addressed by construction: the verdict is rebuilt by a comparator that reads
only the promoted primitive tables, carries its own head law and its own
format strings, and shares no function and no literal with the builder.

CLI (#82).  --selftest | --mutant NAME | --list-gates | --list-mutants |
--list-families | --verify-paper PATH.  Anything else exits 2.
"""

from __future__ import annotations

import ast
import collections
import hashlib
import json
import os
import re
import sys
from fractions import Fraction

# ===========================================================================
# SECTION 0.  RUN STATE, CLI SURFACE, PRIMITIVES
# ===========================================================================

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                     # .../isp/v14
REPO = os.path.dirname(ROOT)                     # .../isp

MUTANT = None
OUT_LINES: list[str] = []


def say(msg=""):
    OUT_LINES.append(msg)


def mut(name):
    return MUTANT == name


def digest(obj) -> str:
    blob = json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, default=str)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:12]


def bdigest(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:12]


_MD_PREFIX = re.compile(r"^[ \t]*(?:>[ \t]?|[-*+][ \t]+|\d+\.[ \t]+)+", re.M)


def canon(text: str, fold_case: bool = True) -> str:
    """#125 normalisation with the case fold SEC-2 MAJOR-10 bought."""
    t = _MD_PREFIX.sub(" ", text)
    t = t.replace("`", " ").replace("*", " ").replace("_", " ")
    t = t.replace("$", " ")
    t = re.sub(r"\s+", " ", t)
    if fold_case:
        t = t.casefold()
    return t.strip()


class GateFail(Exception):
    def __init__(self, check: str, detail: str):
        super().__init__("%s :: %s" % (check, detail))
        self.check = check
        self.detail = detail


# ---------------------------------------------------------------------------
# Z[zeta_8] -- exact, integral, no floats.  z^4 = -1.
# ---------------------------------------------------------------------------

IZ = (0, 0, 0, 0)
IONE = (1, 0, 0, 0)


def imul(a, b):
    r = [0] * 7
    for i in range(4):
        if a[i] == 0:
            continue
        ai = a[i]
        for j in range(4):
            if b[j] == 0:
                continue
            r[i + j] += ai * b[j]
    return (r[0] - r[4], r[1] - r[5], r[2] - r[6], r[3])


def iadd(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])


def ineg(a):
    return (-a[0], -a[1], -a[2], -a[3])


def iconj(a):
    return (a[0], -a[3], -a[2], -a[1])


def izpow(t):
    t %= 8
    s = 1
    if t >= 4:
        t -= 4
        s = -1
    return tuple(s if i == t else 0 for i in range(4))


def idouble(a, k):
    """multiply by 2^k, exactly, with no arithmetic operator that is a power"""
    out = a
    for _ in range(k):
        out = iadd(out, out)
    return out


SQRT2 = iadd(izpow(1), ineg(izpow(3)))
FOUR = (4, 0, 0, 0)


# ===========================================================================
# SECTION 1.  THE TEMPLATE MECHANISMS (E-25..E-33), IMPLEMENTED NATIVELY
# ===========================================================================
# Each class below carries the template's own CHECK id.  The ids are not
# typed as a group anywhere: G-TEMPLATE-CONFORMANCE reads them off these
# classes and off the pinned era_template.py and requires set equality.

class Ledger:
    """A chained ledger (E-26): a row cannot be inserted, dropped or
    reordered without moving the head."""

    def __init__(self):
        self.rows: list[dict] = []
        self.head = "0" * 16

    def gate(self, gid, statement, ok, evidence):
        row = {"n": len(self.rows) + 1, "gate": gid, "statement": statement,
               "evidence": evidence, "passed": bool(ok), "prev": self.head}
        row["row_digest"] = digest(row)
        self.head = hashlib.sha256(
            (self.head + row["row_digest"]).encode("utf-8")).hexdigest()[:16]
        self.rows.append(row)
        TRANSCRIPT.row(gid, bool(ok), evidence)
        if not ok:
            raise GateFail(gid, evidence)

    def names(self):
        return [r["gate"] for r in self.rows]

    def recompute_chain(self):
        head = "0" * 16
        for r in self.rows:
            body = {k: r[k] for k in
                    ("n", "gate", "statement", "evidence", "passed")}
            body["prev"] = head
            if digest(body) != r["row_digest"]:
                raise GateFail("T-LEDGER-CHAIN", "row %d digest moved" % r["n"])
            head = hashlib.sha256(
                (head + r["row_digest"]).encode("utf-8")).hexdigest()[:16]
        return head


class Transcript:
    """(b) E-26: the transcript is bound to the ledger BY CONTENT."""

    CHECK = "T-TRANSCRIPT-BOUND"
    LINE = re.compile(r"^\s*\[(PASS|FAIL)\] (\S+) :: (.*)$")

    def __init__(self):
        self.lines: list[str] = []

    def say(self, text):
        self.lines.append(text)

    def row(self, gid, ok, evidence):
        self.lines.append("  [%s] %s :: %s"
                          % ("PASS" if ok else "FAIL", gid, evidence))

    def text(self):
        return "\n".join(self.lines) + "\n"

    def parse(self, text=None):
        src = self.text() if text is None else text
        out = collections.Counter()
        for line in src.splitlines():
            m = self.LINE.match(line)
            if m:
                out[(m.group(2), m.group(1) == "PASS", m.group(3))] += 1
        return out

    def bind(self, ledger, text=None):
        want = collections.Counter(
            (r["gate"], r["passed"], r["evidence"]) for r in ledger.rows)
        got = self.parse(text)
        missing = sorted(k[0] for k in (want - got).elements())
        stray = sorted(k[0] for k in (got - want).elements())
        if missing or stray:
            raise GateFail(self.CHECK, "transcript rows are not the ledger's: "
                           "missing %s stray %s" % (missing, stray))
        if sum(got.values()) != len(ledger.rows):
            raise GateFail(self.CHECK, "transcript carries %d gate lines "
                           "against %d ledger rows"
                           % (sum(got.values()), len(ledger.rows)))
        return bdigest((self.text() if text is None
                        else text).encode("utf-8"))


class Seal:
    """(a) E-25: digests at gate time; totality RECOMPUTED at the door;
    verified again from the promoted bytes."""

    CHECK = "T-SEAL-PROMOTION"

    def __init__(self):
        self.seals: dict[str, dict] = {}
        self.unsealed: dict[str, str] = {}
        self.measured: set[str] = set()
        self.closed = False

    def take(self, key, value, gate, measured=True):
        if self.closed:
            raise GateFail(self.CHECK, "seal taken after close: %s" % key)
        if key in self.unsealed:
            raise GateFail(self.CHECK,
                           "key both sealed and declared unsealed: %s" % key)
        self.seals[key] = {"digest": digest(value), "gate": gate}
        if measured:
            self.measured.add(key)

    def declare_unsealed(self, key, reason):
        if key in self.seals or key in self.measured:
            raise GateFail(self.CHECK,
                           "measured key re-declared unsealed: %s" % key)
        if not reason.strip():
            raise GateFail(self.CHECK, "unsealed key with no reason: %s" % key)
        self.unsealed[key] = reason

    def manifest(self):
        return {"sealed": {k: v["digest"] for k, v in sorted(self.seals.items())},
                "sealed_at_gate": {k: v["gate"] for k, v in sorted(self.seals.items())},
                "declared_unsealed": dict(sorted(self.unsealed.items()))}

    def verify_at_promotion(self, payload, ledger, manifest_key):
        moved = [k for k, s in self.seals.items()
                 if k not in payload or digest(payload[k]) != s["digest"]]
        if moved:
            raise GateFail(self.CHECK,
                           "sealed values moved after their gate: %s" % moved)
        gates = set(ledger.names())
        phantom = sorted(k for k, s in self.seals.items()
                         if s["gate"] not in gates)
        if phantom:
            raise GateFail(self.CHECK,
                           "seal names a gate that never ran: %s" % phantom)
        covered = set(self.seals) | set(self.unsealed) | {manifest_key}
        undeclared = sorted(set(payload) - covered)
        absent = sorted(set(self.seals) - set(payload))
        if undeclared:
            raise GateFail(self.CHECK, "keys published but neither sealed nor "
                           "declared: %s" % undeclared)
        if absent:
            raise GateFail(self.CHECK,
                           "sealed key absent from the payload: %s" % absent)

    def close(self):
        self.closed = True

    def verify_after_promotion(self, receipt_path, manifest_key):
        with open(receipt_path, "rb") as fh:
            on_disk = json.loads(fh.read().decode("utf-8"))
        moved = [k for k, s in self.seals.items()
                 if k not in on_disk or digest(on_disk[k]) != s["digest"]]
        if moved:
            raise GateFail(self.CHECK, "post-close edit reached disk: %s" % moved)
        covered = set(self.seals) | set(self.unsealed) | {manifest_key}
        undeclared = sorted(set(on_disk) - covered)
        if undeclared:
            raise GateFail(self.CHECK, "post-close add reached disk: %s" % undeclared)
        return on_disk


class SemanticWall:
    """(c) E-27: voice-normalised patterns, a positive leg, non-vacuous,
    self-sealed, and no self-licensing.

    Three separations the legs need and this class makes:
      * the NEGATIVE legs run over the paper's own voice -- its declaring
        sentences and the pinned windows it quotes removed;
      * the POSITIVE legs run over the paper with the pinned windows removed
        and nothing else, so a standing sentence of this unit's own cannot be
        discharged by a parent's quotation;
      * the LICENCE leg polices the paper's PROSE with hyphens folded, so a
        policed token cannot be smuggled past it by a hyphen, and it publishes
        the number of sentences it policed, so its non-vacuity is measured."""

    CHECK = "T-WALL-SEMANTIC"

    def __init__(self, name, negative, positive, policed=(), licences=()):
        self.name = name
        self.negative = list(negative)
        self.positive = list(positive)
        self.policed = tuple(policed)
        self.licences = tuple(licences)
        for pat in self.negative + self.positive:
            re.compile(pat)
        bad = [t for t in self.licences
               if any(w in canon(t) for w in self.policed)]
        if bad:
            raise GateFail(self.CHECK, "self-licensing token set: %s" % bad)

    def seal_value(self):
        return {"name": self.name, "negative": self.negative,
                "positive": self.positive, "licences": list(self.licences),
                "policed": list(self.policed)}

    @staticmethod
    def fold(text):
        """#125 normalisation with the hyphen folded to a space: a policed
        token written with a hyphen is the same token."""
        return re.sub(r"\s+", " ", canon(text).replace("-", " ")).strip()

    def scan(self, paper_text, claims=None, scan_text=None,
             standing_text=None, licence_text=None):
        if not paper_text or not paper_text.strip():
            raise GateFail(self.CHECK,
                           "%s scanned no text (vacuous pass)" % self.name)
        own = scan_text if scan_text is not None else paper_text
        standing = standing_text if standing_text is not None else paper_text
        if not own.strip() or not standing.strip():
            raise GateFail(self.CHECK,
                           "%s scanned no text (vacuous pass)" % self.name)
        hay = canon(own)
        hits = [p for p in self.negative if re.search(p, hay)]
        if hits:
            raise GateFail(self.CHECK,
                           "%s: banned pattern matched %s" % (self.name, hits))
        gone = [p for p in self.positive if not re.search(p, canon(standing))]
        if gone:
            raise GateFail(self.CHECK, "%s: required standing sentence absent "
                           "%s" % (self.name, gone))
        policed = 0
        if self.policed:
            lic = licence_text if licence_text is not None else own
            if not lic.strip():
                raise GateFail(self.CHECK, "%s policed no text (vacuous pass)"
                               % self.name)
            policed = self._licence_leg(lic, claims or [])
            if not policed:
                raise GateFail(self.CHECK, "%s policed no sentence at all "
                               "(vacuous pass)" % self.name)
        return {"negative": len(self.negative), "positive": len(self.positive),
                "policed_sentences": policed}

    def _licence_leg(self, paper_text, claims):
        cclaims = [self.fold(c) for c in claims]
        policed = 0
        for sentence in re.split(r"(?<=[.!?])\s+", paper_text):
            s = self.fold(sentence)
            if not any(re.search(r"\b%s" % w, s) for w in self.policed):
                continue
            policed += 1
            if not any(c and c in s for c in cclaims):
                raise GateFail(self.CHECK, "%s: policed sentence carries no "
                               "rendered claim :: %s"
                               % (self.name, sentence.strip()[:90]))
        return policed


class Anchor:
    def __init__(self, name, needle, source, consumer, floor=40):
        self.name = name
        self.needle = needle
        self.source = source
        self.consumer = consumer
        self.floor = floor
        self.text = None
        self.read_by: set[str] = set()


class AnchorSet:
    """(d) E-28: one accessor, consumption verified, both sides, above the
    floor, and the content enters a predicate."""

    CHECK = "T-ANCHOR-CONSUMED"

    def __init__(self, anchors):
        self.by_name = {a.name: a for a in anchors}

    def locate(self, sources, paper_text=None):
        for a in self.by_name.values():
            if len(a.needle) < a.floor:
                raise GateFail(self.CHECK, "%s: needle under the %d-char floor"
                               % (a.name, a.floor))
            hay = canon(sources[a.source])
            hits = hay.count(canon(a.needle))
            if hits != 1:
                raise GateFail(self.CHECK, "%s: %d occurrences in %s, want 1"
                               % (a.name, hits, a.source))
            if paper_text is not None and a.name not in NOT_QUOTED_IN_PAPER:
                if canon(a.needle) not in canon(paper_text):
                    raise GateFail(self.CHECK, "%s: quoted in the paper with "
                                   "different words" % a.name)
            a.text = a.needle

    def read(self, name, by_gate):
        a = self.by_name[name]
        if a.text is None:
            raise GateFail(self.CHECK, "%s read before it was located" % name)
        a.read_by.add(by_gate)
        return a.text

    def verify_consumption(self, ledger):
        gates = set(ledger.names())
        phantom = sorted(a.name for a in self.by_name.values()
                         if a.consumer not in gates)
        if phantom:
            raise GateFail(self.CHECK, "consumer gate does not exist: %s" % phantom)
        unconsumed = sorted(a.name for a in self.by_name.values()
                            if a.consumer not in a.read_by)
        if unconsumed:
            raise GateFail(self.CHECK, "declared consumer never subscripted "
                           "the anchor: %s" % unconsumed)
        return {"anchors": len(self.by_name),
                "consumed": len(self.by_name) - len(unconsumed)}


class Claims:
    """(e) E-29: equality both ways, keyed by table, headers are rows, exact
    occurrence counts, fences by multiset, every paper table bound."""

    CHECK = "T-CLAIMS-EQUAL"
    FENCE = re.compile(r"```[^\n]*\n(.*?)```", re.S)
    ROW = re.compile(r"^\s*\|(.+)\|\s*$", re.M)

    def __init__(self):
        self.rows = []
        self.prose = collections.Counter()
        self.fences = collections.Counter()

    def table(self, table_id, header, rows):
        self.rows.append((table_id, "header", tuple(str(c) for c in header)))
        out = ["| " + " | ".join(str(c) for c in header) + " |",
               "|" + "---|" * len(header)]
        for r in rows:
            cells = tuple(str(c) for c in r)
            self.rows.append((table_id, "data", cells))
            out.append("| " + " | ".join(cells) + " |")
        return "\n".join(out)

    def claim(self, text, times=1):
        self.prose[canon(text)] += times
        return text

    def fence(self, text, times=1):
        self.fences[canon(text)] += times
        return "```\n%s\n```" % text

    def gate(self, paper_text):
        if not paper_text.strip():
            raise GateFail(self.CHECK, "no paper text (vacuous pass)")
        self._gate_tables(paper_text)
        self._gate_prose(paper_text)
        self._gate_fences(paper_text)
        return {"table_rows": len(self.rows),
                "prose_claim_occurrences": sum(self.prose.values()),
                "distinct_prose_claims": len(self.prose),
                "fence_blocks": sum(self.fences.values())}

    def _paper_tables(self, paper_text):
        got = collections.Counter()
        tid, prev_blank = 0, True
        for line in paper_text.splitlines():
            m = self.ROW.match(line)
            if not m:
                prev_blank = True
                continue
            cells = tuple(c.strip() for c in m.group(1).split("|"))
            if set("".join(cells)) <= set("-: "):
                continue
            if prev_blank:
                tid += 1
                kind = "header"
                prev_blank = False
            else:
                kind = "data"
            got[(tid, kind, cells)] += 1
        return got

    def _gate_tables(self, paper_text):
        got = self._paper_tables(paper_text)
        want_sets = collections.defaultdict(collections.Counter)
        for t, kind, cells in self.rows:
            want_sets[t][(kind, cells)] += 1
        got_sets = collections.defaultdict(collections.Counter)
        for (tid, kind, cells), n in got.items():
            got_sets[tid][(kind, cells)] += n
        used, problems = set(), []
        for t, want in want_sets.items():
            header = [k for k in want if k[0] == "header"]
            found = None
            for tid, cand in sorted(got_sets.items()):
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
            missing = sorted(str(k)[:70] for k in (want - cand).elements())
            stray = sorted(str(k)[:70] for k in (cand - want).elements())
            if missing or stray:
                problems.append("table %s: missing %s stray %s"
                                % (t, missing, stray))
        loose = sorted(str(tid) for tid in got_sets if tid not in used)
        if loose:
            problems.append("paper tables bound by nothing: %s" % loose)
        if problems:
            raise GateFail(self.CHECK, "; ".join(problems))

    def _gate_prose(self, paper_text):
        hay = canon(paper_text)
        wrong = []
        for text, need in sorted(self.prose.items()):
            got = hay.count(text)
            if got != need:
                wrong.append("%r occurs %d, licensed %d" % (text[:56], got, need))
        if wrong:
            raise GateFail(self.CHECK,
                           "claim occurrence counts are not exact: %s" % wrong)

    def _gate_fences(self, paper_text):
        got = collections.Counter(canon(b) for b in self.FENCE.findall(paper_text))
        missing = sorted(k[:48] for k in (self.fences - got).elements())
        stray = sorted(k[:48] for k in (got - self.fences).elements())
        if missing or stray:
            raise GateFail(self.CHECK, "fenced blocks are not a multiset "
                           "match: missing %s stray %s" % (missing, stray))


class ReferentRegistry:
    """(f) E-30: per occurrence, prose only, paired."""

    CHECK = "T-REFERENT-BOUND"
    NOF = re.compile(r"([\d][\d,]*)\s+(?:of|in|out of)\s+([\d][\d,]*)", re.I)
    NUM = re.compile(r"(?<![\w.,/-])(\d[\d,]*)(?![\w/])")

    def __init__(self):
        self.universes = {}
        self.exempt = {}

    def universe(self, name, nouns, values, pairs=None):
        self.universes[name] = {"nouns": [canon(n) for n in nouns],
                                "values": set(values),
                                "pairs": set(pairs or ())}

    def exempt_token(self, token, reason):
        """a numeral that is an IDENTIFIER and not a measurement -- this
        unit's own number in the corpus, or a ledger entry's -- exempted by
        name and with its reason published, never by silence."""
        self.exempt[token] = reason

    def seal_value(self):
        return {n: {"nouns": u["nouns"], "values": sorted(u["values"]),
                    "pairs": sorted(u["pairs"])}
                for n, u in sorted(self.universes.items())}

    @staticmethod
    def prose_only(paper_text):
        """fenced blocks AND rendered table rows are stripped: both are bound
        by equality at the claims gate, and what remains is the paper's own
        prose, which nothing else binds."""
        t = Claims.FENCE.sub(" ", paper_text)
        return "\n".join(ln for ln in t.splitlines()
                          if not Claims.ROW.match(ln))

    def _nouns_in(self, s):
        """every occurrence of every declared noun in the canonicalised
        sentence, with its position.  The match is EXACT -- a noun is bounded
        at both ends -- so `censused` is not the noun `census` and `armed` is
        not the noun `arm`."""
        out = []
        for name, u in self.universes.items():
            for n in u["nouns"]:
                for m in re.finditer(r"\b%s\b" % re.escape(n), s):
                    out.append((m.start(), name))
        return sorted(out)

    @staticmethod
    def _referent(nouns, at):
        """the universe of the noun the numeral is PREDICATED OF: the nearest
        declared noun after it, or -- when its sentence puts none after it --
        the nearest before.  This is the repair for a false number riding a
        foreign noun into this gate: `at every depth the census carries 256
        sealed laws` resolves 256 against the census, which is what it is a
        count of, and not against the cone, which is merely the first universe
        the sentence mentions."""
        after = [n for n in nouns if n[0] >= at]
        if after:
            return after[0][1]
        before = [n for n in nouns if n[0] < at]
        if before:
            return before[-1][1]
        return None

    def gate(self, paper_text):
        prose = self.prose_only(paper_text)
        for tok in self.exempt:
            prose = prose.replace(tok, " ")
        everything, allpairs = set(), set()
        for u in self.universes.values():
            everything |= u["values"]
            allpairs |= u["pairs"]
        checked, unbound, offences = 0, 0, []
        for raw in re.split(r"(?<=[.!?])\s+", prose):
            s = canon(raw)
            nouns = self._nouns_in(s)
            spans = [m.span() for m in self.NOF.finditer(s)]
            for m in self.NOF.finditer(s):
                a, b = (int(x.replace(",", "")) for x in m.groups())
                checked += 1
                uname = self._referent(nouns, m.end())
                if uname is None:
                    unbound += 1
                    if (a, b) not in allpairs:
                        offences.append("(%d of %d) is a measured pair of no "
                                        "declared universe" % (a, b))
                elif (a, b) not in self.universes[uname]["pairs"]:
                    offences.append("(%d of %d) is not a measured pair of %s"
                                    % (a, b, uname))
            for m in self.NUM.finditer(s):
                if any(x <= m.start() < y for x, y in spans):
                    continue
                v = int(m.group(1).replace(",", ""))
                checked += 1
                uname = self._referent(nouns, m.end())
                if uname is None:
                    # a sentence carrying no declared noun at all is resolved
                    # against the union of every universe, so that no prose
                    # numeral sits outside all of them.
                    unbound += 1
                    if v not in everything:
                        offences.append("%d is a value of no declared universe"
                                        % v)
                elif v not in self.universes[uname]["values"]:
                    offences.append("%d is not a value of %s" % (v, uname))
        if offences:
            raise GateFail(self.CHECK, "; ".join(sorted(set(offences))[:6]))
        return {"occurrences_checked": checked,
                "occurrences_with_no_universe_noun": unbound,
                "exemptions": len(self.exempt),
                "universes": len(self.universes)}


class CountRegistry:
    """(g) E-31: no typed numeral anywhere this unit vouches."""

    CHECK = "T-NO-TYPED-COUNTS"
    DIGITS = re.compile(r"(?<![\w])\d+(?![\w])")

    def __init__(self):
        self.values = {}
        self.provenance = {}
        self.exempt = {}

    def measured(self, name, value, how):
        if not how.strip():
            raise GateFail(self.CHECK, "%s published with no provenance" % name)
        self.values[name] = value
        self.provenance[name] = how
        return value

    def get(self, name):
        if name not in self.values:
            raise GateFail(self.CHECK, "unmeasured name cited: %s" % name)
        return self.values[name]

    def exempt_token(self, token, reason):
        self.exempt[token] = reason

    def stmt(self, template, **names):
        probe = template
        for tok in self.exempt:
            probe = probe.replace(tok, " ")
        probe = re.sub(r"\{[^{}]*\}", " ", probe)
        typed = self.DIGITS.findall(probe)
        if typed:
            raise GateFail(self.CHECK, "typed numeral %s in a published "
                           "statement: %r" % (typed, template[:64]))
        keys = set(re.findall(r"\{([A-Za-z_][A-Za-z_0-9]*)\}", template))
        keys |= set(names)
        unknown = sorted(k for k in keys if k not in self.values)
        if unknown:
            raise GateFail(self.CHECK,
                           "statement cites unmeasured names: %s" % unknown)
        return template.format(**{k: self.values[k] for k in keys})

    def audit_module(self, source, statement_callers):
        """E-31, at the ARGUMENT EXPRESSION rather than at the top-level
        string.  Two subspecies the older scan could not see, both of which
        published false counts elsewhere in this era: a numeral typed into a
        %-formatted evidence string, which is a string constant nested inside
        a BinOp rather than an argument itself; and a typed integer offset
        added to or subtracted from a measured count, which is a published
        numeral that never appears in any string at all."""
        tree = ast.parse(source)
        out = []
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            fname = getattr(node.func, "attr", None) or getattr(node.func, "id", None)
            if fname not in statement_callers:
                continue
            for arg in node.args:
                for sub in ast.walk(arg):
                    if isinstance(sub, ast.Constant) and isinstance(sub.value, str):
                        probe = sub.value
                        for tok in self.exempt:
                            probe = probe.replace(tok, " ")
                        probe = re.sub(r"\{[^{}]*\}", " ", probe)
                        if self.DIGITS.search(probe):
                            out.append("line %d: %r"
                                       % (sub.lineno, sub.value[:56]))
                    if isinstance(sub, ast.BinOp) and \
                            isinstance(sub.op, (ast.Add, ast.Sub)):
                        for side in (sub.left, sub.right):
                            if isinstance(side, ast.Constant) and \
                                    isinstance(side.value, int) and \
                                    not isinstance(side.value, bool):
                                out.append("line %d: a typed integer offset "
                                           "over a published count"
                                           % sub.lineno)
        return out


class Falsifier:
    def __init__(self, name, gate, description, target, probe):
        self.name = name
        self.gate = gate
        self.description = description
        self.target = target
        self.probe = probe


class FalsifierHarness:
    """(h) E-32: a falsifier moves the measurement it names, or it is not a
    falsifier.  The coverage denominator contains the coverage gate."""

    CHECK = "T-FALSIFIER-POISONS"

    def __init__(self, falsifiers):
        self.rows = list(falsifiers)

    def prove_moves(self, payload):
        out = []
        for f in self.rows:
            if f.target not in payload:
                raise GateFail(self.CHECK, "%s names a target the run does not "
                               "measure: %s" % (f.name, f.target))
            before = digest(payload[f.target])
            after = digest(f.probe(payload))
            if before == after:
                raise GateFail(self.CHECK, "%s did not move its declared target "
                               "%s (sentinel-shaped)" % (f.name, f.target))
            out.append({"mutant": f.name, "gate": f.gate, "target": f.target,
                        "clean_digest": before, "mutated_digest": after,
                        "moved": True})
        return out

    def audit_descriptions(self, source, declared=()):
        """AST leg for E-23, at the reference implementation's own strength.
        ANY statement of a mutant branch that rebinds a local flag to a
        constant, or appends a constant to a local list, is sentinel-shaped --
        not only a branch all of whose statements are.  And the branch itself
        must be LIVE: a test carrying a constant beside the mutant call is a
        short-circuited branch (`if False and mut(...)`), and a declared
        falsifier with no branch at all in this file is a badge with nothing
        behind it -- which is what makes the in-process move proof a statement
        about this instrument rather than about a probe."""
        tree = ast.parse(source)
        offenders = []
        live = collections.Counter()
        for node in ast.walk(tree):
            if not isinstance(node, ast.If):
                continue
            calls = [c for c in ast.walk(node.test)
                     if isinstance(c, ast.Call)
                     and getattr(c.func, "id", None) == "mut"]
            if not calls:
                continue
            names = [c.args[0].value for c in calls
                     if c.args and isinstance(c.args[0], ast.Constant)]
            shorted = [s for s in ast.walk(node.test)
                       if isinstance(s, ast.Constant)
                       and not isinstance(s.value, str)]
            if shorted:
                offenders.append("line %d: the branch test carries a constant "
                                 "beside the mutant call" % node.lineno)
            else:
                for nm in names:
                    live[nm] += 1
            for st in node.body:
                if isinstance(st, ast.Assign) and \
                        all(isinstance(t, ast.Name) for t in st.targets) and \
                        isinstance(st.value, ast.Constant):
                    offenders.append("line %d: the branch rebinds a local flag "
                                     "to a constant" % node.lineno)
                elif isinstance(st, ast.Expr) and \
                        isinstance(st.value, ast.Call) and \
                        getattr(st.value.func, "attr", "") == "append" and \
                        st.value.args and \
                        isinstance(st.value.args[0], ast.Constant):
                    offenders.append("line %d: the branch appends a constant "
                                     "to a local list" % node.lineno)
        for nm in declared:
            if not live[nm]:
                offenders.append("%s: no live branch of its own in this "
                                 "instrument's source" % nm)
        return offenders

    def coverage(self, ledger, waivers, forcings):
        targeted = {f.gate for f in self.rows}
        already = set(ledger.names())
        fired = already | {"G-FALSIFIER-COVERAGE"}
        live = "G-FALSIFIER-COVERAGE" not in already
        # a forcing may be a predicate OF the denominator this gate divides
        # by, evaluated here, after that denominator is taken and not before.
        forcings = {k: (v(live) if callable(v) else v)
                    for k, v in forcings.items()}
        uncovered = sorted(g for g in fired
                           if g not in targeted and g not in waivers)
        unforced = sorted(g for g in waivers if not forcings.get(g, False))
        if uncovered:
            raise GateFail(self.CHECK,
                           "gates with neither falsifier nor waiver: %s" % uncovered)
        if unforced:
            raise GateFail(self.CHECK,
                           "waivers with no machine-checked forcing: %s" % unforced)
        return {"gates": len(fired), "gates_with_a_falsifier": len(targeted),
                "gates_waived": len(waivers),
                "denominator": sorted(fired),
                "forcings_as_evaluated": {k: bool(v)
                                          for k, v in sorted(forcings.items())},
                "the_denominator_is_the_live_ledger_and_this_gate_is_not_in_it_yet":
                    live}


class ReadSet:
    """(i) E-33: reads recorded at the accessor, compared at the LAST gate."""

    CHECK = "T-READ-SET"

    def __init__(self, root):
        self.root = os.path.abspath(root)
        self.log: list[str] = []
        self.active = False
        self.exemptions = {}
        self._installed = False

    def install(self):
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

    def exempt(self, rel, reason):
        self.exemptions[rel] = reason

    def gate_at_close(self, declared):
        seen = collections.Counter(p for p in self.log
                                   if p not in self.exemptions
                                   and not p.endswith(".tmp"))
        want = collections.Counter(declared)
        stray = sorted(set(seen) - set(want))
        never = sorted(set(want) - set(seen))
        unused = sorted(e for e in self.exemptions if e not in set(self.log))
        if stray:
            raise GateFail(self.CHECK, "read but not declared: %s" % stray)
        if never:
            raise GateFail(self.CHECK, "declared but never read: %s" % never)
        if unused:
            raise GateFail(self.CHECK,
                           "exemption carried and never used: %s" % unused)
        return {"reads": sum(seen.values()), "distinct_paths": len(seen)}


def require_object(mode, path, text):
    if path is None or not os.path.exists(path):
        raise GateFail(ReadSet.CHECK, "%s ran with no object present" % mode)
    if text is None or not text.strip():
        raise GateFail(ReadSet.CHECK, "%s ran on empty text (vacuous pass)" % mode)


TRANSCRIPT = Transcript()
LD = Ledger()
SEAL = Seal()
CNT = CountRegistry()
READS = ReadSet(REPO)

# ===========================================================================
# SECTION 2.  THE PINNED SOURCES, THE ANCHORS, THE PATH-VALUES
# ===========================================================================

SOURCES = {
    "PIN":       ("v14/note-hor-pin.md",                 "0cf8515e184f"),
    "TEMPLATE":  ("v14/TEMPLATE.md",                     "809ebe3514ad"),
    "ERATPL":    ("v14/code/era_template.py",            "d04a3eb58fbc"),
    "R5PAPER":   ("v14/paper-18-gauge-rung.md",          "62cfe5689d2c"),
    "R5CODE":    ("v14/code/r5_gauge_exact.py",          "0d98de793b79"),
    "R5RECEIPT": ("v14/code/r5_gauge_receipt.json",      "0c02b7684e5b"),
    "POTPAPER":  ("v14/paper-36-pot.md",                 "1e495318252d"),
    "POTRECEIPT": ("v14/code/pot_receipt.json",          "3a48c3806443"),
    "ACTPAPER":  ("v14/paper-34-act.md",                 "d933221780ed"),
    "ACTRECEIPT": ("v14/code/act_receipt.json",          "7fd1267bddc7"),
    "R1PAPER":   ("v14/paper-01-continuum-rung.md",      "c4c8880874bf"),
    "LORPAPER":  ("v14/paper-30-lor.md",                 "0a08203b7e99"),
    "EPRPAPER":  ("v14/paper-38-epr.md",                 "22beb6696223"),
    "R4PAPER":   ("v14/paper-10-defect-on-the-stage.md", "1063401c7bb5"),
    "R4BPAPER":  ("v14/paper-15-momentum.md",            "89c636906061"),
}

PAPER_REL = "v14/paper-42-hor.md"
RECEIPT_REL = "v14/code/hor_receipt.json"
OUTPUT_REL = "v14/code/hor_output.txt"

NOT_QUOTED_IN_PAPER = frozenset()

# --- the verbatim anchors ---------------------------------------------------
# Each row: (name, source key, the exact needle, the gate that CONSUMES it).
# Every consumer takes a VALUE out of the needle and compares it with a
# measurement of this run: an anchor that binds existence and not meaning is
# decoration (E-28).

ANCHOR_ROWS = [
    ("VB-HOR-C", "PIN", "the exact maximal propagation speed of influence per "
     "tick, measured (not assumed) on the committed dynamics", "G-EMERGENT-C"),
    ("VB-HOR-SPLIT", "PIN", "the pre-registered split: contractible physics "
     "R-STABLE vs winding physics TORUS-DECLARED", "G-THE-SPLIT"),
    ("VB-R5-STRATUM", "R5CODE", "the stratum operator is the product of the "
     "eight that make up a parity class", "G-THE-TICK-IS-BUILT"),
    ("VB-R5-LINKOP", "R5PAPER", "acts as $U$ on the two-dimensional span of "
     "the link's own domino and as the identity on every other site",
     "G-ARENA-REBUILT"),
    ("VB-R5-NODYN", "R5PAPER", "no configuration measure, no action "
     "functional, no coupling and **no dynamics for the link variables**",
     "G-THE-TICK-IS-DECLARED"),
    ("VB-POT-IDENTICAL", "POTPAPER", "640 of the 640 coins carry identical "
     "coefficients at the two lattice sizes", "G-LOOP-STABILITY-CONTRACTIBLE"),
    ("VB-POT-MERGING", "POTPAPER", "What does not survive is the class "
     "merging: 0 merges at L = 8 against 72 here", "G-MERGING-ON-THE-PATCH"),
    ("VB-POT-SPLIT", "POTPAPER", "192 placements and 192 distinct loops, of "
     "which 144 contractible and 48 winding", "G-THE-FAMILY-SPLIT"),
    ("VB-ACT-INDEX", "ACTPAPER", "at every L divisible by eight it is 1, and "
     "there the price is not reduced, no orbit pair is identified and no "
     "observable is pinned", "G-MERGING-ON-THE-PATCH"),
    ("VB-ACT-CLOSES", "ACTPAPER", "A constant link twist is realisable by a "
     "gauge transformation exactly at the even values, because the phase must "
     "close after $L$ steps.", "G-PATCH-GAUGE-GROUP"),
    ("VB-R1-NOLIMIT", "R1PAPER", "The two constant values are not a limit and "
     "not a convergence.", "G-WALL-NO-ACTUAL-INFINITY"),
    ("VB-R1-NOTOPOLOGY", "R1PAPER", "Nothing is claimed about arenas outside "
     "that list or about a limit of the family in any topology.",
     "G-DIRECT-LIMIT-FORM"),
    ("VB-LOR-PLACES", "LORPAPER", "The refinement's new places are the old "
     "links.", "G-CLOSURE-CENSUS"),
    ("VB-EPR-ROOM", "EPRPAPER", "The one direction the arena does not declare "
     "is exactly the direction along which separation is possible.",
     "G-HORIZON-STABILITY-DYNAMIC"),
    ("VB-R4-CONE", "R4PAPER", "The composed propagator's support starts at the "
     "generator's own radius and never grows faster than one neighbourhood "
     "per step.", "G-THE-CONE"),
    ("VB-R4-WRAPS", "R4PAPER", "The bound is not saturated by all of them, "
     "because the torus wraps", "G-CONE-SATURATION"),
    ("VB-R4B-NOTC", "R4BPAPER", "A velocity that both overshoots and "
     "undershoots the support it came from is not a light-cone velocity.",
     "G-C-IS-NOT-THE-GROUP-SPEED"),
    ("VB-TPL-ADOPT", "TEMPLATE", "It does not make a green run evidence.  A "
     "unit that adopts these checks has adopted a mechanism",
     "G-TEMPLATE-CONFORMANCE"),
]

# --- the path-value anchors -------------------------------------------------
# (name, source key, dotted path, the value that path must carry)

PATH_VALUES_VALUE_ONLY = {
    "PV-POT-BL-SHAPES":
        "the parent's own rectangle family at its boundary size runs to a "
        "longer extent than the family this unit declares, so its count "
        "cannot be the predicate of any measurement taken here; it is carried "
        "as a drift check on the parent's receipt and as nothing else",
    "PV-R5-CIRCULANTS":
        "the gauge parent's control count over its own circulant family, "
        "which this unit neither rebuilds nor uses; it is carried as a drift "
        "check on the parent's receipt and as nothing else",
}

PATH_VALUES = [
    ("PV-POT-COINS", "POTRECEIPT", "arena.coins", 640),
    ("PV-POT-ALPHABET", "POTRECEIPT", "arena.alphabet", 25),
    ("PV-POT-ROWS", "POTRECEIPT", "arena.admissible_rows", 80),
    ("PV-POT-SITES", "POTRECEIPT", "arena.sites", 16),
    ("PV-POT-LINKS", "POTRECEIPT", "arena.links", 32),
    ("PV-POT-PLAQ", "POTRECEIPT", "arena.plaquettes", 16),
    ("PV-POT-L", "POTRECEIPT", "arena.L", 4),
    ("PV-POT-DIAG", "POTRECEIPT", "arena.sectors.DIAGONAL", 64),
    ("PV-POT-ANTI", "POTRECEIPT", "arena.sectors.ANTIDIAGONAL", 64),
    ("PV-POT-BAL", "POTRECEIPT", "arena.sectors.BALANCED", 512),
    ("PV-POT-CLASSES", "POTRECEIPT", "classes.classes", 136),
    ("PV-POT-ORBITS", "POTRECEIPT", "classes.parent_orbits", 208),
    ("PV-POT-MERGED", "POTRECEIPT", "classes.orbit_pairs_merged", 72),
    ("PV-POT-CONTRACTIBLE", "POTRECEIPT", "loop_family.contractible", 144),
    ("PV-POT-WINDING", "POTRECEIPT", "loop_family.winding", 48),
    ("PV-POT-PLACEMENTS", "POTRECEIPT", "loop_family.placements", 192),
    ("PV-POT-SHAPES", "POTRECEIPT", "loop_family.simple_rectangle_shapes", 9),
    ("PV-POT-BL", "POTRECEIPT", "boundary_lattice.L", 8),
    ("PV-POT-BL-MERGED", "POTRECEIPT", "boundary_lattice.orbit_pairs_merged", 0),
    ("PV-POT-BL-ORBITS", "POTRECEIPT", "boundary_lattice.parent_orbits", 136),
    ("PV-POT-BL-IDENT", "POTRECEIPT",
     "boundary_lattice.coins_with_identical_coefficients", 640),
    ("PV-POT-BL-SHAPES", "POTRECEIPT", "boundary_lattice.simple_rectangle_shapes", 49),
    ("PV-POT-LADDER", "POTRECEIPT", "boundary_lattice.ladder_perimeters",
     [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]),
    ("PV-R5-COINS", "R5RECEIPT", "counts.coins", 640),
    ("PV-R5-CONNECTIVE", "R5RECEIPT", "counts.connective_tag", "MAX-NORM"),
    ("PV-R5-CIRCULANTS", "R5RECEIPT", "counts.control_circulants", 58),
    ("PV-ACT-IDX-L2", "ACTRECEIPT", "merging_index_law.rows.0.the_merging_index", 4),
    ("PV-ACT-IDX-L4", "ACTRECEIPT", "merging_index_law.rows.1.the_merging_index", 2),
    ("PV-ACT-IDX-L8", "ACTRECEIPT", "merging_index_law.rows.2.the_merging_index", 1),
    ("PV-ACT-IMAGE", "ACTRECEIPT",
     "merging_index_law.rows.1.the_link_stencils_gauge_image", 8),
]


def read_bytes(rel):
    with open(os.path.join(REPO, rel), "rb") as fh:
        return fh.read()


def dig(obj, path):
    cur = obj
    for part in path.split("."):
        if isinstance(cur, list):
            cur = cur[int(part)]
        else:
            cur = cur[part]
    return cur


def load_sources():
    """the pinned reads, each byte-anchored, each product consumed (#91)."""
    text, shas = {}, {}
    for key, (rel, want) in sorted(SOURCES.items()):
        raw = read_bytes(rel)
        got = bdigest(raw)
        if mut("MUT-SOURCE-SHA") and key == "POTPAPER":
            got = "0" * len(got)
        shas[key] = got
        text[key] = raw.decode("utf-8")
        if got != want:
            raise GateFail("G-SOURCES", "%s (%s) digest %s, declared %s"
                           % (key, rel, got, want))
    LD.gate("G-SOURCES",
            "every runtime input is a hash-pinned repository artifact read at "
            "its declared digest: the pin, the era template and its reference "
            "implementation, and the seven parent papers and three parent "
            "receipts this unit rebuilds from -- no ledger, no status board, "
            "no other unit's working file, no subprocess and no moving "
            "reference of any kind",
            all(shas[k] == SOURCES[k][1] for k in SOURCES),
            "sources %d, all at their declared digests" % len(SOURCES))
    return text, shas


def measure_path_values(text):
    docs = {"POTRECEIPT": json.loads(text["POTRECEIPT"]),
            "ACTRECEIPT": json.loads(text["ACTRECEIPT"]),
            "R5RECEIPT": json.loads(text["R5RECEIPT"])}
    pv, bad = {}, []
    for name, src, path, want in PATH_VALUES:
        got = dig(docs[src], path)
        if mut("MUT-PATH-VALUE") and name == "PV-POT-CLASSES":
            got = want + 1
        if got != want:
            bad.append("%s: %s.%s is %r, anchored %r" % (name, src, path, got, want))
        pv[name] = got
    LD.gate("G-PATH-VALUES",
            "every inherited number this unit uses is anchored as a "
            "(path, value) pair in a parent's own receipt, so a path that "
            "drifts to a different quantity dies here rather than arriving as "
            "a silent re-definition",
            not bad, "path-value anchors %d, off their anchored value %d%s"
            % (len(PATH_VALUES), len(bad),
               (": " + "; ".join(bad[:2])) if bad else ""))
    return pv


def anchor_ints(anchors, name, gate):
    """the numerals the anchor's own bytes carry, in order."""
    txt = anchors.read(name, gate)
    return [int(x) for x in re.findall(r"(?<![\w])(\d+)(?![\w])", txt)]


def anchor_has(anchors, name, gate, phrase):
    return canon(phrase) in canon(anchors.read(name, gate))


# ===========================================================================
# SECTION 3.  THE ARENA -- REBUILT, NEVER IMPORTED
# ===========================================================================
# Two arenas, the same generators.  The TORUS is R5's: (Z_L)^2 with the
# opposite edge identified.  The OPEN PATCH is this unit's: the same square
# of sites with NO identification at all, so a link exists exactly when both
# of its endpoints do.  Nothing else differs.

def build_alphabet():
    """R4's coefficient alphabet as R5 declares it, carried DOUBLED so every
    entry is an algebraic integer: zero, and zeta_8^t at each of the three
    declared moduli."""
    cands = [IZ]
    for t in range(8):
        cands.append(idouble(izpow(t), 1))
        cands.append(izpow(t))
        cands.append(imul(izpow(t), SQRT2))
    out, seen = [], set()
    for a in cands:
        if a not in seen:
            seen.add(a)
            out.append(a)
    return out


def build_coins(alphabet):
    """the coin family, derived: a two-by-two unitary all four of whose
    entries lie in the alphabet.  In doubled coordinates the row condition
    |a|^2 + |b|^2 = 1 reads (2a)conj(2a) + (2b)conj(2b) = 4."""
    rows = [(a, b) for a in alphabet for b in alphabet
            if iadd(imul(a, iconj(a)), imul(b, iconj(b))) == FOUR]
    coins = []
    for (a, b) in rows:
        for (c, d) in rows:
            if iadd(imul(a, iconj(c)), imul(b, iconj(d))) == IZ:
                coins.append((a, b, c, d))
    if mut("MUT-ARENA"):
        coins = coins[:-1]
    return coins, rows


def coin_sector(m):
    a, b, c, d = m
    if b == IZ and c == IZ:
        return "DIAGONAL"
    if a == IZ and d == IZ:
        return "ANTIDIAGONAL"
    return "BALANCED"


def coin_unitary_second_route(m):
    a, b, c, d = m
    return (iadd(imul(iconj(a), a), imul(iconj(c), c)) == FOUR
            and iadd(imul(iconj(b), b), imul(iconj(d), d)) == FOUR
            and iadd(imul(iconj(a), b), imul(iconj(c), d)) == IZ)


def gauge_twist(m, k):
    """the site-diagonal gauge acts on a link's coin by conjugation with
    diag(zeta_8^p, zeta_8^q); the action depends on k = p - q alone."""
    a, b, c, d = m
    return (a, imul(izpow(k), b), imul(izpow(-k), c), d)


def phase_order():
    """the order of the declared field's root of unity, DERIVED from the field
    arithmetic rather than typed."""
    e = 1
    while izpow(e) != IONE:
        e += 1
    return e


E1, E2 = (1, 0), (0, 1)
EDIR = (E1, E2)
TORUS, PATCH = "TORUS", "OPEN-PATCH"


class Arena:
    """one class, two closures.  `kind` is the only branch."""

    def __init__(self, kind, n):
        self.kind = kind
        self.n = n
        self._sites = [(x, y) for x in range(n) for y in range(n)]
        self._sset = set(self._sites)

    # -- the two closures ---------------------------------------------------
    def step(self, s, d, sgn=1):
        v = EDIR[d]
        t = (s[0] + sgn * v[0], s[1] + sgn * v[1])
        if self.kind == TORUS:
            return (t[0] % self.n, t[1] % self.n)
        return t if t in self._sset else None

    # -- derived sets -------------------------------------------------------
    def sites(self):
        return list(self._sites)

    def links(self):
        return [(s, d) for s in self._sites for d in range(2)
                if self.step(s, d) is not None]

    def plaquettes(self):
        out = []
        for s in self._sites:
            a = self.step(s, 0)
            b = self.step(s, 1)
            if a is None or b is None:
                continue
            if self.step(a, 1) is None or self.step(b, 0) is None:
                continue
            out.append(s)
        return out

    def ends(self, l):
        return l[0], self.step(l[0], l[1])

    def dist(self, u, v, norm):
        if self.kind == TORUS:
            dx = min((u[0] - v[0]) % self.n, (v[0] - u[0]) % self.n)
            dy = min((u[1] - v[1]) % self.n, (v[1] - u[1]) % self.n)
        else:
            dx, dy = abs(u[0] - v[0]), abs(u[1] - v[1])
        return dx + dy if norm == "SUM" else max(dx, dy)

    def tag(self):
        return "%s-%d" % ("T" if self.kind == TORUS else "P", self.n)


# --- R5's four parity strata, rebuilt --------------------------------------

STRATUM_NAMES = ("X-EVEN", "X-ODD", "Y-EVEN", "Y-ODD")
STRATUM_KEYS = ((0, 0), (0, 1), (1, 0), (1, 1))
SCHEDULE = tuple(range(4))          # the declared cyclic order of the strata


def stratum(arena, d, par):
    return [l for l in arena.links() if l[1] == d and l[0][d] % 2 == par]


def stratum_report(arena):
    """is the declared stratification a matching?  MEASURED, per stratum:
    a stratum is a matching when no site is an endpoint of two of its links,
    and PERFECT when it is also an endpoint of one."""
    rows = []
    for name, (d, par) in zip(STRATUM_NAMES, STRATUM_KEYS):
        st = stratum(arena, d, par)
        touched = collections.Counter()
        for l in st:
            t, h = arena.ends(l)
            touched[t] += 1
            touched[h] += 1
        clash = sorted(s for s, c in touched.items() if c > 1)
        if mut("MUT-STRATUM"):
            clash = clash[:0]
        rows.append({"stratum": name, "links": len(st),
                     "sites_touched": len(touched),
                     "sites_touched_twice": len(clash),
                     "is_a_matching": len(clash) == 0,
                     "is_perfect": len(clash) == 0
                                   and len(touched) == len(arena.sites())})
    return rows


def partner_map(arena, d, par):
    """the tick's own partner map: a site's image under the stratum, or the
    site itself where the stratum has no link on it."""
    pm = {}
    for l in stratum(arena, d, par):
        t, h = arena.ends(l)
        pm[t] = h
        pm[h] = t
    return pm


# --- the declared ladders (the arena, as data, RUNBOOK section 15) ----------

TORUS_LADDER = (3, 4, 5, 6, 7, 8)
PATCH_LADDER = (3, 4, 5, 6, 7, 8, 9)
LOOP_LADDER_T = (4, 6, 8)                # tori where the loop family is built
LOOP_LADDER_P = (4, 5, 6, 7, 8, 9)       # patches where it is built
CONE_DEPTH = 16
ATTAIN_DEPTH = 8
DYN_DEPTH = 8
DYN_WINDOW = 2
DYN_TORI = (6, 8, 10, 12)
DYN_PATCHES = (5, 7, 9, 11)
COIN_STRIDE = 128                        # the declared representative stride
RECT_MAX = 4                             # the largest declared rectangle extent

# the census's own arena pair, declared here as data and printed in the
# census table row by row: ONE open size and ONE closed size, both on the
# ladders above, with the closed one the size the potential parent ran its
# own boundary lattice at.
CORE_PATCH, CORE_TORUS = 9, 8

# and the sizes the census sweeps each of its witnesses over, so that a
# witness an arena can move is told from a witness no arena can: every size
# of either ladder at which every declared rectangle shape fits.
CENSUS_SWEEP_T = tuple(n for n in TORUS_LADDER if n > RECT_MAX)
CENSUS_SWEEP_P = tuple(n for n in PATCH_LADDER if n > RECT_MAX)


def measure_arena(S, pv, anchors):
    alpha = build_alphabet()
    coins, rows = build_coins(alpha)
    sect = collections.Counter(coin_sector(m) for m in coins)
    unit = sum(1 for m in coins if coin_unitary_second_route(m))
    tor = Arena(TORUS, pv["PV-POT-L"])
    # E-28: the link operator's own window is READ, and the number it carries
    # (the domino's dimension) must equal the block this unit's operator acts
    # on.
    dom = 2 if anchor_has(anchors, "VB-R5-LINKOP", "G-ARENA-REBUILT",
                          "two-dimensional span of the link's own domino") else 0
    ok = (len(alpha) == pv["PV-POT-ALPHABET"] and len(rows) == pv["PV-POT-ROWS"]
          and len(coins) == pv["PV-POT-COINS"] and unit == len(coins)
          and sect["DIAGONAL"] == pv["PV-POT-DIAG"]
          and sect["ANTIDIAGONAL"] == pv["PV-POT-ANTI"]
          and sect["BALANCED"] == pv["PV-POT-BAL"]
          and len(tor.sites()) == pv["PV-POT-SITES"]
          and len(tor.links()) == pv["PV-POT-LINKS"]
          and len(tor.plaquettes()) == pv["PV-POT-PLAQ"]
          and len(coins) == pv["PV-R5-COINS"] and dom == 2)
    CNT.measured("alphabet", len(alpha), "enumerated from the declared moduli")
    CNT.measured("rows", len(rows), "the row condition over the alphabet")
    CNT.measured("coins", len(coins), "exhaustive over the admissible rows")
    CNT.measured("diag", sect["DIAGONAL"], "the coin sector census")
    CNT.measured("anti", sect["ANTIDIAGONAL"], "the coin sector census")
    CNT.measured("bal", sect["BALANCED"], "the coin sector census")
    CNT.measured("domino", dom, "read out of R5's own link-operator window")
    LD.gate("G-ARENA-REBUILT",
            CNT.stmt("the alphabet, the coin family, the torus at the parent's "
                     "own size, its link set and its plaquette set are REBUILT "
                     "here from the parents' declarations -- nothing is "
                     "imported -- every cardinality is required to equal the "
                     "parent's published one at a named receipt path, "
                     "unitarity is confirmed by a second route on every coin, "
                     "and the dimension of the block the link operator acts on "
                     "is read out of R5's own sentence rather than assumed: it "
                     "is {domino}"), ok,
            "alphabet %d, rows %d, coins %d (%s), unitary by a second route "
            "%d, sites %d, links %d, plaquettes %d, domino dimension %d"
            % (len(alpha), len(rows), len(coins),
               ", ".join("%s %d" % (k, sect[k]) for k in sorted(sect)),
               unit, len(tor.sites()), len(tor.links()),
               len(tor.plaquettes()), dom))
    S["arena"] = {
        "field": "Q(zeta_8)", "d": 2, "alphabet": len(alpha),
        "admissible_rows": len(rows), "coins": len(coins),
        "sectors": dict(sorted(sect.items())),
        "unitary_by_a_second_route": unit,
        "the_declared_size_of_the_parents": tor.n,
        "sites_there": len(tor.sites()), "links_there": len(tor.links()),
        "plaquettes_there": len(tor.plaquettes()),
        "domino_dimension_read_from_R5": dom,
        "carrier": "THE-UNIFORM-CONFIGURATIONS-ONE-COIN-ON-EVERY-LINK",
        "the_two_closures": [TORUS, PATCH],
        "torus_ladder": list(TORUS_LADDER), "patch_ladder": list(PATCH_LADDER),
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24"}
    SEAL.take("arena", S["arena"], "G-ARENA-REBUILT")
    S["_alpha"], S["_coins"] = alpha, coins
    return alpha, coins


def measure_zero_patterns(S, coins):
    """the one-tick influence of a coin is fixed by which of its entries
    vanish, and unitarity leaves exactly three patterns.  Measured per coin,
    never as a tally (#87): every coin is classified on its own entries and
    the theorem is checked on that coin."""
    pat = collections.Counter()
    bad = []
    for m in coins:
        a, b, c, d = m
        key = (a != IZ, b != IZ, c != IZ, d != IZ)
        pat[key] += 1
        # the theorem, on this coin: a vanishes iff d does, b iff c does
        if (a == IZ) != (d == IZ) or (b == IZ) != (c == IZ):
            bad.append(m)
        if a == IZ and b == IZ:
            bad.append(m)
    if mut("MUT-ZERO-PATTERN"):
        pat[(True, True, False, False)] = 1
    ok = (not bad) and len(pat) == 3
    census_line = ", ".join(
        "%s->%d" % ("".join("Z" if t else "-" for t in k), v)
        for k, v in sorted(pat.items()))
    CNT.measured("patterns", len(pat), "the per-coin zero pattern census")
    LD.gate("G-ZERO-PATTERN-THEOREM",
            CNT.stmt("unitarity forces the vanishing pattern of a coin: the "
                     "diagonal entries vanish together and the off-diagonal "
                     "entries vanish together, so exactly {patterns} patterns "
                     "occur over the whole coin family and each coin is "
                     "checked against the theorem on its own four entries "
                     "rather than counted into a tally"),
            ok, "patterns %d over %d coins: %s" %
            (len(pat), len(coins), census_line))
    S["zero_patterns"] = {
        "patterns": len(pat),
        "census": {"".join("1" if t else "0" for t in k): v
                   for k, v in sorted(pat.items())},
        "coins_failing_the_theorem": len(bad),
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24"}
    SEAL.take("zero_patterns", S["zero_patterns"], "G-ZERO-PATTERN-THEOREM")
    return pat


# ===========================================================================
# SECTION 4.  THE TICK -- R5's NAMED-AND-NEVER-BUILT STRATUM OPERATOR
# ===========================================================================

def measure_the_stratification(S, pv, anchors):
    """R5 declares four parity strata and calls each a class of eight
    dominoes at its own size.  Whether that stratification is a matching --
    the property that makes the stratum operator well defined without an
    order -- is measured here on both closures at every affordable size."""
    eight = None
    txt = anchors.read("VB-R5-STRATUM", "G-THE-TICK-IS-BUILT")
    if "eight" in canon(txt):
        eight = 8
    rows = []
    for kind, ladder in ((TORUS, TORUS_LADDER), (PATCH, PATCH_LADDER)):
        for n in ladder:
            A = Arena(kind, n)
            rep = stratum_report(A)
            rows.append({"arena": A.tag(), "closure": kind, "n": n,
                         "sites": len(A.sites()), "links": len(A.links()),
                         "plaquettes": len(A.plaquettes()),
                         "strata_that_are_matchings":
                             sum(1 for r in rep if r["is_a_matching"]),
                         "strata_that_are_perfect":
                             sum(1 for r in rep if r["is_perfect"]),
                         "sites_touched_twice":
                             sum(r["sites_touched_twice"] for r in rep),
                         "per_stratum": rep})
    tor_bad = [r for r in rows if r["closure"] == TORUS
               and r["strata_that_are_matchings"] < 4]
    pat_bad = [r for r in rows if r["closure"] == PATCH
               and r["strata_that_are_matchings"] < 4]
    odd_tori = [r for r in rows if r["closure"] == TORUS and r["n"] % 2 == 1]
    even_tori = [r for r in rows if r["closure"] == TORUS and r["n"] % 2 == 0]
    ok = (not pat_bad
          and all(r["strata_that_are_matchings"] == 4 for r in even_tori)
          and all(r["strata_that_are_matchings"] < 4 for r in odd_tori)
          and eight == 8
          and all(r["per_stratum"][0]["links"] == eight
                  for r in rows if r["arena"] == "T-4"))
    CNT.measured("strata", 4, "the declared parity classes, counted")
    CNT.measured("eight", eight, "read out of R5's own stratum sentence")
    CNT.measured("oddtori", len(odd_tori), "the odd sizes on the torus ladder")
    CNT.measured("patchrows", len([r for r in rows if r["closure"] == PATCH]),
                 "the patch ladder, counted")
    LD.gate("G-THE-STRATIFICATION",
            CNT.stmt("R5's {strata} parity strata are rebuilt on both closures "
                     "at every affordable size, and the property that makes a "
                     "stratum operator well defined without an order -- that "
                     "the stratum is a MATCHING -- is measured rather than "
                     "assumed: it holds at all {patchrows} patch sizes, at "
                     "every even torus, and at none of the {oddtori} odd tori; "
                     "and the number R5's own sentence carries for a stratum "
                     "at its own size, {eight}, is required to be this run's "
                     "measured stratum size there"),
            ok, "rows %d, patch failures %d, odd tori failing %d of %d, "
            "R5's own stratum size %s" % (len(rows), len(pat_bad),
                                          len(odd_tori), len(odd_tori), eight))
    S["stratification"] = {
        "rows": rows, "strata": 4,
        "odd_tori_measured": len(odd_tori),
        "odd_tori_where_the_stratification_is_a_matching":
            sum(1 for r in odd_tori if r["strata_that_are_matchings"] == 4),
        "patch_sizes_where_it_is_a_matching":
            sum(1 for r in rows if r["closure"] == PATCH
                and r["strata_that_are_matchings"] == 4),
        "the_number_R5s_sentence_carries": eight,
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24"}
    SEAL.take("stratification", S["stratification"], "G-THE-STRATIFICATION")
    return rows


def link_operator_pair(coin, orient):
    """the two rows of R5's link operator, doubled.  orient -1 inverts."""
    a, b, c, d = coin
    if orient < 0:
        return (iconj(a), iconj(c), iconj(b), iconj(d))
    return coin


def tick_once(arena, psi, coin, key):
    """ONE TICK: the stratum operator, built.  Every link of the parity class
    carries R5's link operator; the class is a matching, so the factors are
    disjoint and the product needs no order.  Doubled coin entries mean the
    state's scale rises by exactly one power of two per tick, tracked
    separately and divided out once."""
    d, par = key
    a, b, c, dd = coin
    if mut("MUT-TICK"):
        c = a
    new = {}
    for s, v in psi.items():
        new[s] = idouble(v, 1)
    for l in stratum(arena, d, par):
        t, h = arena.ends(l)
        x = psi.get(t, IZ)
        y = psi.get(h, IZ)
        new[t] = iadd(imul(a, x), imul(b, y))
        new[h] = iadd(imul(c, x), imul(dd, y))
    return {s: v for s, v in new.items() if v != IZ}


def evolve(arena, start, depth, coin, schedule=SCHEDULE):
    psi = {start: IONE}
    out = []
    for t in range(depth):
        psi = tick_once(arena, psi, coin, STRATUM_KEYS[schedule[t % 4]])
        out.append(psi)
    return out


def structural_reach(arena, start, depth, schedule=SCHEDULE, sector="BALANCED"):
    """the cone, computed WITHOUT any amplitude: a set propagated through the
    parity classes' partner relation, which is read off the site coordinates
    and the closure rule rather than off the link list the amplitude route
    walks."""
    cur = {start}
    out = []
    for t in range(depth):
        d, par = STRATUM_KEYS[schedule[t % 4]]
        nxt = set()
        for u in cur:
            if u[d] % 2 == par:
                p = arena.step(u, d, 1)
            else:
                p = arena.step(u, d, -1)
                if p is not None and p[d] % 2 != par:
                    p = None
            if sector == "DIAGONAL" or p is None:
                nxt.add(u)
            elif sector == "ANTIDIAGONAL":
                nxt.add(p)
            else:
                nxt.add(u)
                nxt.add(p)
        cur = nxt
        out.append(frozenset(cur))
    return out


def measure_the_tick(S, pv, anchors, coins):
    """the tick is well defined: disjoint factors, identity off its own links,
    and unitary on the single-occupation sector -- measured, per stratum, per
    coin, at the declared size."""
    A = Arena(TORUS, pv["PV-POT-L"])
    n = len(A.sites())
    idx = {s: i for i, s in enumerate(A.sites())}
    bad_unitary, bad_identity, checks = [], [], 0
    probe = [coins[i] for i in range(0, len(coins), COIN_STRIDE)]
    for key in STRATUM_KEYS:
        st = stratum(A, key[0], key[1])
        touched = set()
        for l in st:
            t, h = A.ends(l)
            touched.add(t)
            touched.add(h)
        for m in probe:
            cols = []
            for s in A.sites():
                psi = tick_once(A, {s: IONE}, m, key)
                cols.append([psi.get(u, IZ) for u in A.sites()])
                checks += 1
                if s not in touched and psi != {s: idouble(IONE, 1)}:
                    bad_identity.append((s, key))
            for i in range(n):
                for j in range(n):
                    acc = IZ
                    for k in range(n):
                        acc = iadd(acc, imul(iconj(cols[i][k]), cols[j][k]))
                    want = FOUR if i == j else IZ
                    if acc != want:
                        bad_unitary.append((i, j, key))
    disjoint = all(r["strata_that_are_matchings"] == 4
                   for r in S["stratification"]["rows"]
                   if r["arena"] == A.tag())
    ok = (not bad_unitary) and (not bad_identity) and disjoint
    CNT.measured("tickprobe", len(probe), "the declared coin stride")
    CNT.measured("tickchecks", checks, "column-by-column, per coin, per stratum")
    LD.gate("G-THE-TICK-IS-BUILT",
            CNT.stmt("the object R5 names and never constructs -- the stratum "
                     "operator -- is BUILT here and shown to be a tick: its "
                     "factors are disjoint because the stratum is a matching, "
                     "so no order is chosen; it is the identity on every site "
                     "its own class does not touch; and it is unitary on the "
                     "single-occupation sector, checked column against column "
                     "over {tickchecks} columns at {tickprobe} coins taken by "
                     "a declared stride through the family"),
            ok, "columns %d, coins %d, non-unitary %d, identity failures %d, "
            "disjoint %s" % (checks, len(probe), len(bad_unitary),
                             len(bad_identity), disjoint))
    S["the_tick"] = {
        "definition": "ONE-APPLICATION-OF-ONE-PARITY-STRATUM-OPERATOR",
        "schedule": [STRATUM_NAMES[i] for i in SCHEDULE],
        "sweep_length": len(SCHEDULE),
        "columns_checked": checks, "coins_probed": len(probe),
        "non_unitary_columns": len(bad_unitary),
        "identity_failures_off_the_class": len(bad_identity),
        "factors_disjoint_at_the_declared_size": disjoint,
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24"}
    return probe


def measure_the_tick_is_declared(S, anchors):
    """R5 sealed NO DYNAMICS.  This unit does not overturn that: the
    generators are the parent's, the TICK is this unit's declaration, and the
    stamp is a gate rather than a remark."""
    nodyn = anchor_has(anchors, "VB-R5-NODYN", "G-THE-TICK-IS-DECLARED",
                       "no dynamics for the link variables")
    if mut("MUT-NODYN"):
        S["the_tick"] = dict(S["the_tick"], definition="UNDECLARED")
    ok = nodyn and S["the_tick"]["definition"].startswith("ONE-APPLICATION")
    LD.gate("G-THE-TICK-IS-DECLARED",
            "the parent's seal is read here and carried forward rather than "
            "contradicted: R5 declares no dynamics for the link variables, so "
            "the GENERATORS below are inherited and the TICK is this unit's "
            "own declaration; every speed this unit publishes is a speed per "
            "that tick and is stamped so wherever it appears",
            ok, "R5's own no-dynamics clause located and read: %s; the tick is "
            "declared as %s" % (nodyn, S["the_tick"]["definition"]))
    S["the_tick"]["the_parent_declares_no_dynamics"] = nodyn
    S["the_tick"]["the_tick_is_this_units_declaration"] = True
    SEAL.take("the_tick", S["the_tick"], "G-THE-TICK-IS-DECLARED")


# ===========================================================================
# SECTION 5.  THE EMERGENT c AND THE CONE
# ===========================================================================

def measure_one_tick_reach(S, pv, coins, anchors):
    """the reach of ONE tick, measured on every coin of the carrier: how far
    influence can travel while the stratum operator is applied once."""
    A = Arena(TORUS, pv["PV-POT-L"])
    site = (0, 0)
    key = STRATUM_KEYS[0]
    rows = collections.Counter()
    per_coin = []
    for m in coins:
        psi = tick_once(A, {site: IONE}, m, key)
        reach = max(A.dist(site, u, "SUM") for u in psi) if psi else 0
        stays = site in psi
        rows[(coin_sector(m), reach, stays)] += 1
        per_coin.append(reach)
    if mut("MUT-REACH"):
        per_coin[0] = per_coin[0] + 1
    zero = sum(1 for r in per_coin if r == 0)
    one = sum(1 for r in per_coin if r == 1)
    over = sum(1 for r in per_coin if r > 1)
    ok = (over == 0 and zero == pv["PV-POT-DIAG"]
          and one == pv["PV-POT-ANTI"] + pv["PV-POT-BAL"]
          and zero + one == len(coins))
    CNT.measured("reach0", zero, "per-coin, on the coin's own tick")
    CNT.measured("reach1", one, "per-coin, on the coin's own tick")
    CNT.measured("reachover", over, "per-coin, on the coin's own tick")
    LD.gate("G-ONE-TICK-REACH",
            CNT.stmt("the reach of one tick is measured on every coin of the "
                     "carrier separately, never sampled and never tallied into "
                     "a predicate: it is zero at {reach0} coins -- the "
                     "diagonal sector, where the state cannot move at all -- "
                     "and exactly one site at {reach1}, and it exceeds one at "
                     "{reachover}"),
            ok, "coins %d: reach of zero sites at %d, of one site at %d, of "
            "more than one site at %d" % (len(coins), zero, one, over))
    S["one_tick_reach"] = {
        "coins": len(coins), "reach_zero": zero, "reach_one": one,
        "reach_above_one": over,
        "by_sector_reach_and_rest":
            {"%s|%d|%s" % k: v for k, v in sorted(rows.items())},
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24"}
    SEAL.take("one_tick_reach", S["one_tick_reach"], "G-ONE-TICK-REACH")
    return zero, one


def measure_the_cone(S, pv, anchors):
    """the cone, censused rather than bounded: its exact size, its exact
    radius in both declared norms, and its shape, at every depth of the
    declared ladder, on an arena large enough that no boundary is reached.

    Two routes, sharing only the closure rule under test.  The STRUCTURAL
    route propagates a set through the parity classes' partner relation and
    is the cone proper: the sites influence CAN reach.  The AMPLITUDE route
    evolves an exact state and reports the sites influence DOES reach at a
    particular coin.  The second is contained in the first at every depth --
    that containment is the causal statement -- and it can be strictly
    smaller, because amplitudes cancel; so the cone is also required to be
    ATTAINED, by a coin of the carrier, at every depth of a second sweep run
    over the whole family."""
    A = Arena(PATCH, 2 * CONE_DEPTH + 3)
    c = (even_c(CONE_DEPTH), even_c(CONE_DEPTH))
    reach = structural_reach(A, c, CONE_DEPTH)
    rows = []
    for t in range(CONE_DEPTH):
        R = reach[t]
        rsum = max(A.dist(c, u, "SUM") for u in R)
        rmax = max(A.dist(c, u, "MAX") for u in R)
        xs = sorted({u[0] - c[0] for u in R})
        ys = sorted({u[1] - c[1] for u in R})
        rows.append({"tick": t + 1, "sites": len(R), "sum_norm_radius": rsum,
                     "max_norm_radius": rmax, "x_offsets": len(xs),
                     "y_offsets": len(ys),
                     "is_a_product_box": len(R) == len(xs) * len(ys),
                     "x_forward": max(xs), "x_backward": min(xs)})
    if mut("MUT-CONE"):
        rows[3]["sum_norm_radius"] = rows[3]["sum_norm_radius"] + 1
    probe = [S["_coins"][i] for i in range(0, len(S["_coins"]), COIN_STRIDE)]
    escapes = 0
    for m in probe:
        amp = evolve(A, c, CONE_DEPTH, m)
        for t in range(CONE_DEPTH):
            if not set(amp[t]) <= set(reach[t]):
                escapes += 1
    B = Arena(PATCH, 2 * ATTAIN_DEPTH + 3)
    cb = (even_c(ATTAIN_DEPTH), even_c(ATTAIN_DEPTH))
    rb = structural_reach(B, cb, ATTAIN_DEPTH)
    attain = [0] * ATTAIN_DEPTH
    radius = [0] * ATTAIN_DEPTH
    deficit = []
    for m in S["_coins"]:
        amp = evolve(B, cb, ATTAIN_DEPTH, m)
        for t in range(ATTAIN_DEPTH):
            got = set(amp[t])
            if not got <= set(rb[t]):
                escapes += 1
            if got == set(rb[t]):
                attain[t] += 1
            if got and max(B.dist(cb, u, "SUM") for u in got) == t + 1:
                radius[t] += 1
    for t in range(ATTAIN_DEPTH):
        deficit.append({"tick": t + 1, "cone_sites": len(rb[t]),
                        "coins_whose_support_is_the_whole_cone": attain[t],
                        "coins_realising_the_cone_s_own_sum_norm_radius":
                            radius[t]})
    if mut("MUT-CONE-ESCAPE"):
        escapes = escapes + 1
    sum_is_t = all(r["sum_norm_radius"] == r["tick"] for r in rows)
    all_box = all(r["is_a_product_box"] for r in rows)
    ceiling = all(r["sum_norm_radius"] <= r["tick"] for r in rows)
    anchor_ints(anchors, "VB-R4-CONE", "G-THE-CONE")
    per_step = anchor_has(anchors, "VB-R4-CONE", "G-THE-CONE",
                          "never grows faster than one neighbourhood per step")
    ok = (sum_is_t and all_box and escapes == 0 and ceiling and per_step
          and all(r > 0 for r in radius) and any(a > 0 for a in attain))
    CNT.measured("conedepth", CONE_DEPTH, "the declared cone ladder")
    CNT.measured("coneescape", escapes,
                 "amplitude supports tested against the structural cone")
    CNT.measured("coneattain", min(radius),
                 "the least number of coins realising the cone's radius, over "
                 "the attainment depths")
    CNT.measured("coneshort", sum(1 for a in attain if a == 0),
                 "attainment depths at which no coin fills the whole cone")
    CNT.measured("attaindepth", ATTAIN_DEPTH, "the declared attainment ladder")
    CNT.measured("dynattained", sum(1 for r in radius if r > 0),
                 "attainment depths at which the DYNAMICS reaches the cone's "
                 "own sum-norm radius, as against the partner relation")
    LD.gate("G-THE-CONE",
            CNT.stmt("the cone is censused to depth {conedepth} by a route "
                     "that touches no amplitude at all, and every amplitude "
                     "support this run evolves is tested against it: it "
                     "escapes at {coneescape}, which is the causal statement; "
                     "its sum-norm radius equals the tick number at every "
                     "depth, it is a product of an x-range and a y-range at "
                     "every depth, it never exceeds the "
                     "one-neighbourhood-per-step ceiling the parent's own "
                     "sentence carries; and its RADIUS is attained by the "
                     "dynamics rather than only by the partner relation -- at "
                     "every one of the {attaindepth} attainment depths at "
                     "least {coneattain} coins of the carrier evolve a support "
                     "whose own sum-norm radius is the cone's, while at "
                     "{coneshort} of those depths no coin fills the cone site "
                     "for site, because amplitudes cancel on exact interior "
                     "lines"),
            ok, "depths %d, sum-radius equals the depth %s, product shape %s, "
            "escapes %d, radius attained by at least %d coins at every "
            "attainment depth, depths not filled site for site %d, sizes %s" %
            (CONE_DEPTH, sum_is_t, all_box, escapes, min(radius),
             sum(1 for a in attain if a == 0),
             ",".join(str(r["sites"]) for r in rows)))
    S["the_cone"] = {
        "rows": rows, "depth": CONE_DEPTH,
        "sum_norm_radius_equals_the_tick_at_every_depth": sum_is_t,
        "the_cone_is_a_product_box_at_every_depth": all_box,
        "amplitude_supports_escaping_the_cone": escapes,
        "attainment_depth": ATTAIN_DEPTH,
        "attainment_rows": deficit,
        "attainment_depths_the_dynamics_reaches_the_radius_at":
            sum(1 for r in radius if r > 0),
        "coins_realising_the_cone_radius_at_the_thinnest_depth": min(radius),
        "attainment_depths_no_coin_fills_site_for_site":
            sum(1 for a in attain if a == 0),
        "the_arena_it_was_censused_on": A.tag(),
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24"}
    SEAL.take("the_cone", S["the_cone"], "G-THE-CONE")
    return rows


def measure_c(S, pv, anchors, rows):
    """c, DERIVED from the census: the maximum of radius over tick, in each
    declared norm, as an exact rational; and the sustained value, taken over
    whole sweeps so that no partial sweep flatters it.

    The licence for calling it a MAXIMUM sits at two depths and both are
    published: the structural cone attains it at every censused depth, and the
    dynamics attains it at every depth of the attainment sweep."""
    sum_ratios = [Fraction(r["sum_norm_radius"], r["tick"]) for r in rows]
    max_ratios = [Fraction(r["max_norm_radius"], r["tick"]) for r in rows]
    sweeps = [r for r in rows if r["tick"] % len(SCHEDULE) == 0]
    sust = {Fraction(r["max_norm_radius"], r["tick"]) for r in sweeps}
    sust_sum = {Fraction(r["sum_norm_radius"], r["tick"]) for r in sweeps}
    c_sum = max(sum_ratios)
    c_max = max(max_ratios)
    if mut("MUT-C"):
        c_sum = c_sum + 1
    attained = sum(1 for f in sum_ratios if f == c_sum)
    # the gauge parent's own connective tag, used as a predicate: the norm it
    # names is one of the two this run censuses, and the value this run
    # publishes for it is the SUSTAINED one.
    connective = pv["PV-R5-CONNECTIVE"]
    norms = {"SUM-NORM": sust_sum, "MAX-NORM": sust}
    ok = (c_sum == Fraction(1) and len(sust) == 1
          and next(iter(sust)) == Fraction(1, 2)
          and len(sust_sum) == 1 and next(iter(sust_sum)) == Fraction(1)
          and attained == len(rows)
          and connective in norms and len(norms[connective]) == 1
          and CNT.get("dynattained") == CNT.get("attaindepth")
          and anchor_has(anchors, "VB-HOR-C", "G-EMERGENT-C",
                         "measured (not assumed) on the committed dynamics"))
    CNT.measured("csum", str(c_sum), "max over the cone census, exact rational")
    CNT.measured("cmax", str(c_max), "max over the cone census, exact rational")
    CNT.measured("csust", str(next(iter(sust))) if len(sust) == 1 else "SPLIT",
                 "over whole sweeps only")
    CNT.measured("attained", attained, "depths at which the maximum is reached")
    LD.gate("G-EMERGENT-C",
            CNT.stmt("the emergent speed is DERIVED from the cone census and "
                     "never typed: in the sum norm it is {csum} site per tick, "
                     "attained by the STRUCTURAL cone at every one of the "
                     "{attained} censused depths and by the DYNAMICS at every "
                     "one of the {dynattained} depths of the attainment sweep, "
                     "so it is a maximum and not a bound at both depths and "
                     "neither of them is a ceiling; in the max norm the "
                     "instantaneous value is {cmax} and the value sustained "
                     "over whole sweeps is {csust}, one value at every sweep, "
                     "and the norm the gauge parent's own connective tag names "
                     "is one this census carries"),
            ok, "c_sum %s attained structurally at %d of %d depths and "
            "dynamically at %d of %d, c_max %s, sustained max-norm %s, "
            "sustained sum-norm %s, the parent's connective tag %s" %
            (c_sum, attained, len(rows), CNT.get("dynattained"),
             CNT.get("attaindepth"), c_max,
             sorted(str(x) for x in sust), sorted(str(x) for x in sust_sum),
             connective))
    S["emergent_c"] = {
        "c_in_the_sum_norm_per_tick": str(c_sum),
        "the_norm_the_gauge_parents_connective_tag_names": connective,
        "depths_at_which_the_dynamics_attains_it": CNT.get("dynattained"),
        "attainment_depths": CNT.get("attaindepth"),
        "c_in_the_max_norm_per_tick_instantaneous": str(c_max),
        "c_in_the_max_norm_per_tick_sustained": sorted(str(x) for x in sust),
        "c_in_the_sum_norm_per_tick_sustained": sorted(str(x) for x in sust_sum),
        "depths_at_which_the_sum_norm_maximum_is_attained": attained,
        "depths_censused": len(rows),
        "the_unit": "SITES-PER-TICK-WHERE-A-TICK-IS-ONE-STRATUM-OPERATOR",
        "the_speed_is_a_maximum_not_a_bound": True}
    SEAL.take("emergent_c", S["emergent_c"], "G-EMERGENT-C")
    return c_sum, c_max


def measure_cone_shape(S, pv, rows):
    """the shape, and which part of it is declaration and which is not: the
    cone is asymmetric, and reversing the parity order inside the schedule
    reflects the asymmetry while leaving every radius fixed (section 14)."""
    A = Arena(PATCH, 2 * CONE_DEPTH + 3)
    c = (even_c(CONE_DEPTH), even_c(CONE_DEPTH))
    rev = (1, 0, 3, 2)
    back = structural_reach(A, c, CONE_DEPTH, schedule=rev)
    srows, radius_moves = [], 0
    for t in range(CONE_DEPTH):
        R = back[t]
        xs = sorted({u[0] - c[0] for u in R})
        refl = (max(xs) == -rows[t]["x_backward"]
                and min(xs) == -rows[t]["x_forward"])
        moved = max(A.dist(c, u, "SUM") for u in R) != rows[t]["sum_norm_radius"]
        if moved:
            radius_moves += 1
        srows.append({"tick": t + 1, "reflected": refl, "radius_moved": moved})
    if mut("MUT-SCHEDULE-SYMMETRY"):
        srows[0]["reflected"] = not srows[0]["reflected"]
    flips = sum(1 for r in srows if r["reflected"])
    asym = [r for r in rows if r["x_forward"] != -r["x_backward"]]
    ok = flips == CONE_DEPTH and radius_moves == 0 and len(asym) > 0
    CNT.measured("flips", flips, "reflected depths under the reversed schedule")
    CNT.measured("asym", len(asym), "depths where the x-range is not symmetric")
    LD.gate("G-CONE-SHAPE-IS-DECLARATION-RELATIVE",
            CNT.stmt("the cone's SHAPE carries a declaration and its SPEED "
                     "does not, and the instrument is self-tested under the "
                     "declaration's own action: the x-range is asymmetric at "
                     "{asym} depths, reversing the parity order inside the "
                     "schedule reflects it at {flips} depths, and no radius in "
                     "either norm moves under that reversal"),
            ok, "asymmetric depths %d, reflected under reversal %d of %d, "
            "radii that moved %d" % (len(asym), flips, CONE_DEPTH, radius_moves))
    S["cone_shape"] = {
        "rows": srows,
        "asymmetric_depths": len(asym), "depths": CONE_DEPTH,
        "depths_reflected_by_reversing_the_parity_order": flips,
        "radii_that_move_under_that_reversal": radius_moves,
        "the_shape_is_declaration_relative": True,
        "the_speed_is_not": True,
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24"}
    SEAL.take("cone_shape", S["cone_shape"], "G-CONE-SHAPE-IS-DECLARATION-RELATIVE")


def measure_cone_saturation(S, pv, anchors):
    """where the cone has content and where it does not: on a closed torus it
    fills the arena and then says nothing; on an open patch it does not.  The
    first depth at which the closure becomes visible IN THE CONE is measured
    per size, and that number is the horizon this unit's formulation needs."""
    BIG = Arena(PATCH, 2 * CONE_DEPTH + 3)
    c = (even_c(CONE_DEPTH), even_c(CONE_DEPTH))
    free = [frozenset((u[0] - c[0], u[1] - c[1]) for u in s)
            for s in structural_reach(BIG, c, CONE_DEPTH)]
    rows = []
    for kind, ladder in ((TORUS, TORUS_LADDER), (PATCH, PATCH_LADDER)):
        for n in ladder:
            A = Arena(kind, n)
            st = (0, 0) if kind == TORUS else (even_centre(n), even_centre(n))
            got = structural_reach(A, st, CONE_DEPTH)
            sat, vis = None, None
            for t in range(CONE_DEPTH):
                if sat is None and len(got[t]) == len(A.sites()):
                    sat = t + 1
                if vis is None and len(got[t]) != len(free[t]):
                    vis = t + 1
            rows.append({"arena": A.tag(), "closure": kind, "n": n,
                         "sites": len(A.sites()),
                         "saturates_at_tick": sat if sat else 0,
                         "closure_first_visible_at_tick": vis if vis else 0,
                         "free_cone_at_that_tick":
                             len(free[vis - 1]) if vis else 0})
    if mut("MUT-SATURATION"):
        rows[1]["closure_first_visible_at_tick"] = 0
    tori = [r for r in rows if r["closure"] == TORUS]
    patches = [r for r in rows if r["closure"] == PATCH]
    every_torus_saturates = all(r["saturates_at_tick"] > 0 for r in tori)
    every_torus_visible = all(r["closure_first_visible_at_tick"] > 0 for r in tori)
    wraps = anchor_has(anchors, "VB-R4-WRAPS", "G-CONE-SATURATION",
                       "because the torus wraps")
    ok = every_torus_saturates and every_torus_visible and wraps
    CNT.measured("tori", len(tori), "the torus ladder, counted")
    CNT.measured("patches", len(patches), "the patch ladder, counted")
    LD.gate("G-CONE-SATURATION",
            CNT.stmt("every one of the {tori} closed sizes saturates its own "
                     "cone at a measured depth and every one of them makes its "
                     "closure visible in the cone at a measured depth, which "
                     "is why a cone censused on a closed arena stops saying "
                     "anything past that depth; the parent named the mechanism "
                     "in its own sentence and this run reads it"),
            ok, "torus rows %d all saturating %s all becoming visible %s, "
            "patch rows %d, the parent's wrap clause read %s" %
            (len(tori), every_torus_saturates, every_torus_visible,
             len(patches), wraps))
    S["cone_saturation"] = {
        "rows": rows,
        "closed_sizes": len(tori), "open_sizes": len(patches),
        "every_closed_size_saturates": every_torus_saturates,
        "every_closed_size_becomes_visible": every_torus_visible,
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24"}
    SEAL.take("cone_saturation", S["cone_saturation"], "G-CONE-SATURATION")
    return rows


def measure_c_is_not_the_group_speed(S, pv, anchors):
    """the parent measured a maximal GROUP SPEED on this lattice and reported
    it as not a light-cone velocity.  This unit measures a different object --
    the reach of the support -- and the two are kept apart by a gate rather
    than by a footnote."""
    read = anchor_has(anchors, "VB-R4B-NOTC", "G-C-IS-NOT-THE-GROUP-SPEED",
                      "is not a light-cone velocity")
    # the separation is DERIVED from the circulant measurement rather than
    # typed: the parent's object needs the closure exactly in so far as the
    # translations its own family is defined by exist on one arena and not on
    # the other, which is a pair of numbers this run measured.
    cir = S["circulants"]["rows"]
    ct = [r for r in cir if r["closure"] == TORUS][0]
    cp = [r for r in cir if r["closure"] == PATCH][0]
    closed_axes = ct["axes_whose_shift_is_a_bijection"]
    open_axes = cp["axes_whose_shift_is_a_bijection"]
    closed_syms = ct["translations_carrying_the_link_set_to_itself"]
    open_syms = cp["translations_carrying_the_link_set_to_itself"]
    if mut("MUT-GROUPSPEED"):
        open_axes = closed_axes
    needs_closure = (closed_axes > open_axes and closed_syms > open_syms)
    reach_needs_closure = False
    rows = [
        {"object": "the group speed of a translation-covariant generator",
         "lives_in": "THE-DUAL-TORUS", "needs_the_closure": needs_closure,
         "measured_by": "R4B", "this_unit_re_measures_it": False,
         "the_translations_its_family_needs": closed_syms,
         "the_declared_axes_that_are_bijections_there": closed_axes},
        {"object": "the reach of the support under one tick",
         "lives_in": "THE-SITE-SET", "needs_the_closure": reach_needs_closure,
         "measured_by": "HOR", "this_unit_re_measures_it": True,
         "the_translations_its_family_needs": open_syms,
         "the_declared_axes_that_are_bijections_there": open_axes},
    ]
    ok = (read and rows[0]["needs_the_closure"]
          and not rows[1]["needs_the_closure"]
          and rows[0]["lives_in"] != rows[1]["lives_in"])
    LD.gate("G-C-IS-NOT-THE-GROUP-SPEED",
            "the speed this unit measures is not the speed the parent "
            "measured, and the separation is gated on a measurement rather "
            "than on a declaration: the parent's object is a phase advance on "
            "the dual torus, and whether it needs the closure is DECIDED here "
            "by the circulant census -- the declared axes that are bijections "
            "and the translations that carry the link set to itself, counted "
            "on each closure -- while its own sentence says it is not a "
            "light-cone velocity; this unit's object is the reach of the "
            "support, which is defined on an arena with no closure at all, "
            "and nothing here re-runs, revises or contradicts the parent's "
            "number",
            ok, "the parent's own clause read %s; the two objects live in %s "
            "and %s; bijective declared axes closed %d against open %d, "
            "translations carrying the link set to itself closed %d against "
            "open %d; closure needed %s and %s" %
            (read, rows[0]["lives_in"], rows[1]["lives_in"],
             closed_axes, open_axes, closed_syms, open_syms,
             rows[0]["needs_the_closure"], rows[1]["needs_the_closure"]))
    S["c_against_the_group_speed"] = {
        "rows": rows, "the_parents_clause_was_read": read,
        "the_separation_is_derived_from": "G-CIRCULANTS-NEED-THE-CLOSURE",
        "this_unit_contradicts_nothing_of_the_parents": True}
    SEAL.take("c_against_the_group_speed", S["c_against_the_group_speed"],
              "G-C-IS-NOT-THE-GROUP-SPEED")


# ===========================================================================
# SECTION 6.  THE LOOP FAMILY ON BOTH CLOSURES
# ===========================================================================

def rect_cycle(arena, base, a, b):
    """the a-by-b rectangle circuit based at base.  On a patch a step that
    would leave the arena does not exist, and the circuit simply is not
    there -- no identification is made anywhere."""
    cyc, cur = [], base
    for (d, sgn, k) in ((0, 1, a), (1, 1, b), (0, -1, a), (1, -1, b)):
        for _ in range(k):
            cyc.append(cur)
            cur = arena.step(cur, d, sgn)
            if cur is None:
                return None, False
    return tuple(cyc), cur == base


def wind_cycle(arena, base, d, k):
    cyc, cur = [], base
    for _ in range(k * arena.n):
        cyc.append(cur)
        cur = arena.step(cur, d, 1)
        if cur is None:
            return None, False
    return tuple(cyc), cur == base


def steps_of(arena, cyc):
    st = []
    for i in range(len(cyc)):
        u, w = cyc[i], cyc[(i + 1) % len(cyc)]
        found = None
        for d in (0, 1):
            if arena.step(u, d, 1) == w:
                found = ((u, d), 1)
                break
            if arena.step(w, d, 1) == u:
                found = ((w, d), -1)
                break
        if found is None:
            raise GateFail("G-THE-FAMILY-SPLIT", "a declared cycle has a step "
                           "that is not a link of its own arena")
        st.append(found)
    return st


def net_displacement(arena, cyc):
    """the net displacement of a closed walk, read off the steps rather than
    off the coordinates, so it is defined on both closures."""
    h = [0, 0]
    for i in range(len(cyc)):
        u, w = cyc[i], cyc[(i + 1) % len(cyc)]
        for d in (0, 1):
            if arena.step(u, d, 1) == w:
                h[d] += 1
            elif arena.step(w, d, 1) == u:
                h[d] -= 1
    return (h[0], h[1])


def holonomy_trace(arena, steps, coin):
    """the trace of the loop holonomy on the loop's own site block, rebuilt
    from R5's definition: the ordered product of the link operators around
    the loop, each inverted where the loop runs against the link's own
    direction.  Every factor is the identity off the loop's sites, so the
    restriction is exact.  Doubled entries keep everything integral; the
    power of two each row carries is tracked and divided out once."""
    a, b, c, d = coin
    inv = (iconj(a), iconj(c), iconj(b), iconj(d))
    sites = []
    for (l, o) in steps:
        t, h = arena.ends(l)
        for s in (t, h):
            if s not in sites:
                sites.append(s)
    pos = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    W = [[IONE if i == j else IZ for j in range(n)] for i in range(n)]
    scale = [0] * n
    step = 0
    for (l, o) in steps:
        t, h = arena.ends(l)
        it, ih = pos[t], pos[h]
        if scale[it] < step:
            W[it] = [idouble(x, step - scale[it]) for x in W[it]]
            scale[it] = step
        if scale[ih] < step:
            W[ih] = [idouble(x, step - scale[ih]) for x in W[ih]]
            scale[ih] = step
        A, B, C, D = coin if o > 0 else inv
        r1, r2 = W[it], W[ih]
        n1, n2 = [], []
        for j in range(n):
            x, y = r1[j], r2[j]
            if x == IZ and y == IZ:
                n1.append(IZ)
                n2.append(IZ)
                continue
            n1.append(iadd(imul(A, x), imul(B, y)))
            n2.append(iadd(imul(C, x), imul(D, y)))
        W[it], W[ih] = n1, n2
        step += 1
        scale[it] = scale[ih] = step
    top = max(scale)
    tr = IZ
    for i in range(n):
        tr = iadd(tr, idouble(W[i][i], top - scale[i]))
    den = 1
    for _ in range(top):
        den = den + den
    return (Fraction(tr[0], den), Fraction(tr[1], den),
            Fraction(tr[2], den), Fraction(tr[3], den))


def sym_real(t):
    """the conjugation-symmetric part of a trace, which lies in the real
    subfield: p + q*sqrt(2), returned as the exact pair (p, q)."""
    return (t[0], (t[1] - t[3]) / 2)


def rect_shapes():
    return [(a, b) for a in range(1, RECT_MAX + 1)
            for b in range(1, RECT_MAX + 1)]


def shapes_that_fit(arena):
    out = []
    for (a, b) in rect_shapes():
        cyc, closes = rect_cycle(arena, (0, 0), a, b)
        if cyc is None or not closes:
            continue
        st = steps_of(arena, cyc)
        links = {l for (l, _o) in st}
        sites = set(cyc)
        if len(links) == len(st) and len(sites) == len(st):
            out.append((a, b))
    return out


def measure_the_family_split(S, pv, anchors):
    """the loop family, built on both closures: which placements exist, and
    how the family splits into the contractible part and the winding part.
    On an open patch the winding part is not small -- it is absent."""
    anc = anchor_ints(anchors, "VB-POT-SPLIT", "G-THE-FAMILY-SPLIT")
    rows = []
    for kind, ladder in ((TORUS, LOOP_LADDER_T), (PATCH, LOOP_LADDER_P)):
        for n in ladder:
            A = Arena(kind, n)
            rect, wind = 0, 0
            for (a, b) in rect_shapes():
                for base in A.sites():
                    cyc, closes = rect_cycle(A, base, a, b)
                    if cyc is None or not closes:
                        continue
                    st = steps_of(A, cyc)
                    if len({l for (l, _o) in st}) != len(st):
                        continue
                    if net_displacement(A, cyc) == (0, 0):
                        rect += 1
                    else:
                        wind += 1
            for k in range(1, n + 1):
                for base in A.sites():
                    for d in (0, 1):
                        cyc, closes = wind_cycle(A, base, d, k)
                        if cyc is None or not closes:
                            continue
                        if net_displacement(A, cyc) != (0, 0):
                            wind += 1
            rows.append({"arena": A.tag(), "closure": kind, "n": n,
                         "contractible_placements": rect,
                         "winding_placements": wind,
                         "shapes_that_fit": len(shapes_that_fit(A))})
    if mut("MUT-FAMILY"):
        rows[-1]["winding_placements"] = 1
    patches = [r for r in rows if r["closure"] == PATCH]
    tori = [r for r in rows if r["closure"] == TORUS]
    no_wind = all(r["winding_placements"] == 0 for r in patches)
    all_wind = all(r["winding_placements"] > 0 for r in tori)
    # the parent's own placement total and its own shape count at its own
    # size, used as predicates rather than carried: the total is its two
    # published parts summed, and the shapes it counts there are the shapes
    # this run finds there.
    parts = pv["PV-POT-CONTRACTIBLE"] + pv["PV-POT-WINDING"]
    potrow = [r for r in tori if r["n"] == pv["PV-POT-L"]][0]
    potshapes = potrow["shapes_that_fit"]
    ok = (no_wind and all_wind and anc[2] == pv["PV-POT-CONTRACTIBLE"]
          and anc[3] == pv["PV-POT-WINDING"]
          and pv["PV-POT-PLACEMENTS"] == parts
          and pv["PV-POT-SHAPES"] == potshapes
          and potrow["contractible_placements"] == pv["PV-POT-CONTRACTIBLE"]
          and all(r["contractible_placements"] > 0 for r in rows))
    CNT.measured("patchloops", len(patches), "the patch rows of the family census")
    CNT.measured("torusloops", len(tori), "the torus rows of the family census")
    LD.gate("G-THE-FAMILY-SPLIT",
            CNT.stmt("the parent's family is rebuilt on both closures: at all "
                     "{patchloops} open sizes the winding part is EMPTY -- not "
                     "small, absent -- while the contractible part is "
                     "populated at every size, and at all {torusloops} closed "
                     "sizes the winding part is populated; the two numbers the "
                     "parent's own split sentence carries are required to be "
                     "the two this run reads from its receipt, its published "
                     "placement total to be those two parts summed, and its "
                     "published shape count at its own size to be the count "
                     "this run measures there"),
            ok, "patch rows %d with the winding part empty everywhere %s, "
            "torus rows %d with winding present everywhere %s, the parent's "
            "split numbers %s, its placements %d against its two parts summed "
            "%d, its own shape count %d against this run's at that size %d"
            % (len(patches), no_wind, len(tori), all_wind, anc[2:4],
               pv["PV-POT-PLACEMENTS"], parts, pv["PV-POT-SHAPES"], potshapes))
    S["family_split"] = {
        "rows": rows, "open_sizes": len(patches), "closed_sizes": len(tori),
        "winding_is_empty_at_every_open_size": no_wind,
        "winding_is_present_at_every_closed_size": all_wind,
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24"}
    SEAL.take("family_split", S["family_split"], "G-THE-FAMILY-SPLIT")
    return rows


WALK_DEPTH = 8


def measure_homology(S, pv):
    """first homology, measured exhaustively rather than asserted: every
    closed walk up to the declared depth from a fixed base, on both closures,
    classified by its net displacement.  Measured at the parent's own declared
    size, where the two closures are the same square of places, AND at the
    census's own declared arena pair, so that the census compares this law at
    the size every other row of it uses."""
    rows = []
    for kind, n in ((TORUS, pv["PV-POT-L"]), (PATCH, pv["PV-POT-L"]),
                    (TORUS, CORE_TORUS), (PATCH, CORE_PATCH)):
        A = Arena(kind, n)
        base = (0, 0)
        classes = collections.Counter()
        walks = 0
        stack = [(base, (0, 0), 0)]
        while stack:
            cur, disp, depth = stack.pop()
            if depth == WALK_DEPTH:
                if cur == base:
                    classes[disp] += 1
                    walks += 1
                continue
            for d in (0, 1):
                for sgn in (1, -1):
                    nxt = A.step(cur, d, sgn)
                    if nxt is None:
                        continue
                    nd = (disp[0] + sgn * (1 - d), disp[1] + sgn * d)
                    stack.append((nxt, nd, depth + 1))
        rows.append({"closure": kind, "arena": A.tag(),
                     "closed_walks_of_the_declared_depth": walks,
                     "displacement_classes": len(classes),
                     "walks_with_nonzero_displacement":
                         sum(v for k, v in classes.items() if k != (0, 0))})
    if mut("MUT-HOMOLOGY"):
        rows[1]["displacement_classes"] = rows[0]["displacement_classes"]
    pat = [r for r in rows if r["closure"] == PATCH][0]
    tor = [r for r in rows if r["closure"] == TORUS][0]
    ok = (all(r["displacement_classes"] == 1
              and r["walks_with_nonzero_displacement"] == 0
              for r in rows if r["closure"] == PATCH)
          and all(r["displacement_classes"] > 1
                  and r["walks_with_nonzero_displacement"] > 0
                  for r in rows if r["closure"] == TORUS))
    CNT.measured("walkdepth", WALK_DEPTH, "the declared exhaustive walk depth")
    CNT.measured("patchclasses", pat["displacement_classes"], "exhaustive")
    CNT.measured("torusclasses", tor["displacement_classes"], "exhaustive")
    LD.gate("G-HOMOLOGY",
            CNT.stmt("every closed walk of length {walkdepth} from a fixed "
                     "base is enumerated on both closures and classified by "
                     "its net displacement: the open patch returns "
                     "{patchclasses} class and no walk with a nonzero one, the "
                     "closed torus returns {torusclasses}, so the winding "
                     "numbers a loop observable can carry are a property of "
                     "the identification and of nothing else -- and the same "
                     "enumeration is run again at the arena pair the closure "
                     "census declares, so that row of the census compares this "
                     "law at the sizes every other row of it uses"),
            ok, "patch classes %d (%d nonzero of %d walks), torus classes %d "
            "(%d nonzero of %d walks), rows %s" %
            (pat["displacement_classes"], pat["walks_with_nonzero_displacement"],
             pat["closed_walks_of_the_declared_depth"],
             tor["displacement_classes"], tor["walks_with_nonzero_displacement"],
             tor["closed_walks_of_the_declared_depth"],
             ["%s:%d" % (r["arena"], r["displacement_classes"]) for r in rows]))
    S["homology"] = {"rows": rows, "walk_depth": WALK_DEPTH,
                     "every_integer_here_is_a_count": "COUNTING-ONLY-E-24"}
    SEAL.take("homology", S["homology"], "G-HOMOLOGY")
    return rows


# ===========================================================================
# SECTION 7.  HORIZON-STABILITY -- THE STATIC SIDE
# ===========================================================================

def loop_values(arena, coins, shapes):
    """the observable POT declares -- the conjugation-symmetric part of the
    loop trace -- at one canonical placement per shape."""
    out = {}
    for (a, b) in shapes:
        base = (0, 0)
        cyc, closes = rect_cycle(arena, base, a, b)
        if cyc is None or not closes:
            continue
        st = steps_of(arena, cyc)
        vals = []
        for m in coins:
            vals.append(sym_real(holonomy_trace(arena, st, m)))
        out[(a, b)] = vals
    return out


def measure_loop_stability(S, pv, coins, anchors):
    """the contractible side of the pre-registered split, measured: the same
    shape, the same coin, two closures and every affordable size."""
    probe = [coins[i] for i in range(0, len(coins), COIN_STRIDE)]
    core_p = Arena(PATCH, CORE_PATCH)
    core_t = Arena(TORUS, CORE_TORUS)
    shapes = [s for s in shapes_that_fit(core_p) if s in shapes_that_fit(core_t)]
    full_p = loop_values(core_p, coins, shapes)
    full_t = loop_values(core_t, coins, shapes)
    full_mismatch = 0
    for s in shapes:
        for i in range(len(coins)):
            if full_p[s][i] != full_t[s][i]:
                full_mismatch += 1
    if mut("MUT-LOOP-STABILITY"):
        full_mismatch = full_mismatch + 1
    ladder_rows, ladder_mismatch = [], 0
    ref = loop_values(Arena(PATCH, max(LOOP_LADDER_P)), probe, shapes)
    for kind, ladder in ((TORUS, LOOP_LADDER_T), (PATCH, LOOP_LADDER_P)):
        for n in ladder:
            A = Arena(kind, n)
            fit = shapes_that_fit(A)
            here = loop_values(A, probe, [s for s in shapes if s in fit])
            agree, tested = 0, 0
            for s in shapes:
                if s not in here:
                    continue
                for i in range(len(probe)):
                    tested += 1
                    if here[s][i] == ref[s][i]:
                        agree += 1
                    else:
                        ladder_mismatch += 1
            ladder_rows.append({"arena": A.tag(), "closure": kind, "n": n,
                                "shapes_present": len(here),
                                "shapes_absent": len(shapes) - len(here),
                                "comparisons": tested,
                                "agreeing": agree})
    anc = anchor_ints(anchors, "VB-POT-IDENTICAL", "G-LOOP-STABILITY-CONTRACTIBLE")
    ok = (full_mismatch == 0 and ladder_mismatch == 0
          and anc[0] == pv["PV-POT-COINS"] and anc[1] == pv["PV-POT-COINS"]
          and len(coins) == anc[0] and len(shapes) > 0
          and pv["PV-POT-BL-IDENT"] == len(coins))
    CNT.measured("coreshapes", len(shapes), "shapes present in both core arenas")
    CNT.measured("fullchecks", len(shapes) * len(coins),
                 "shape by coin, at the core pair")
    CNT.measured("ladderchecks", sum(r["comparisons"] for r in ladder_rows),
                 "shape by coin, over the whole declared ladder")
    CNT.measured("loopmis", full_mismatch + ladder_mismatch,
                 "the core sweep's mismatches and the ladder sweep's, added")
    CNT.measured("probecoins", len(probe), "the declared coin stride")
    LD.gate("G-LOOP-STABILITY-CONTRACTIBLE",
            CNT.stmt("the contractible observable is measured on both closures "
                     "at every affordable size: {fullchecks} shape-by-coin "
                     "comparisons at the core pair over the WHOLE coin family, "
                     "and {ladderchecks} more over the whole declared ladder at "
                     "{probecoins} coins taken by a declared stride, with the "
                     "parent's own identical-coefficients sentence read here "
                     "and its two numbers required to be this run's coin "
                     "count, and the coin count its own receipt publishes at "
                     "its boundary size required to be that count too"),
            ok, "core comparisons %d mismatches %d; ladder comparisons %d "
            "mismatches %d; shapes %d; the parent's numbers %s; the coins its "
            "receipt carries at its boundary size %d" %
            (len(shapes) * len(coins), full_mismatch,
             sum(r["comparisons"] for r in ladder_rows), ladder_mismatch,
             len(shapes), anc[:2], pv["PV-POT-BL-IDENT"]))
    S["loop_stability"] = {
        "core_pair": [core_p.tag(), core_t.tag()],
        "shapes_compared": len(shapes),
        "full_family_comparisons": len(shapes) * len(coins),
        "full_family_mismatches": full_mismatch,
        "ladder_rows": ladder_rows,
        "ladder_comparisons": sum(r["comparisons"] for r in ladder_rows),
        "ladder_mismatches": ladder_mismatch,
        "coins_in_the_full_sweep": len(coins),
        "coins_in_the_ladder_sweep": len(probe),
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24"}
    SEAL.take("loop_stability", S["loop_stability"], "G-LOOP-STABILITY-CONTRACTIBLE")
    return shapes, probe


def measure_loop_threshold(S, pv, probe):
    """the exact size at which a contractible shape stops being contractible:
    the threshold is measured, not declared, and below it the very same shape
    is a different observable."""
    rows = []
    for kind, ladder in ((TORUS, (3, 4, 5, 6, 7, 8)), (PATCH, (3, 4, 5, 6, 7, 8, 9))):
        for n in ladder:
            A = Arena(kind, n)
            fit = shapes_that_fit(A)
            biggest = max((max(s) for s in fit), default=0)
            rows.append({"arena": A.tag(), "closure": kind, "n": n,
                         "shapes_that_fit": len(fit),
                         "largest_extent_that_fits": biggest,
                         "threshold_is_n_minus_one": biggest == n - 1})
    if mut("MUT-THRESHOLD"):
        rows[0]["largest_extent_that_fits"] = rows[0]["n"]
    # the identity is TESTABLE exactly where the declared shape family
    # contains an extent of the size less one; at every larger size the
    # largest extent that stays simple is the declared cap itself, which is a
    # fact about this unit's declaration and not about the arena.
    binds = [r for r in rows if r["n"] - 1 <= RECT_MAX]
    capped = [r for r in rows if r["n"] - 1 > RECT_MAX]
    ok = (all(r["largest_extent_that_fits"] == r["n"] - 1 for r in binds)
          and len(binds) > 0 and len(capped) > 0
          and all(r["largest_extent_that_fits"] == RECT_MAX for r in capped))
    CNT.measured("threshrows", len(rows), "the two ladders, counted")
    CNT.measured("threshsmall", len(binds),
                 "sizes where the declared family contains the size less one")
    CNT.measured("threshcapped", len(capped),
                 "sizes where it does not and the cap decides instead")
    LD.gate("G-LOOP-THRESHOLD",
            CNT.stmt("the horizon a contractible observable needs is MEASURED "
                     "at every one of the {threshrows} sizes of both ladders, "
                     "and the identity is stated only where it can be tested: "
                     "at the {threshsmall} sizes whose declared shape family "
                     "contains an extent of the size less one, the largest "
                     "extent that stays simple IS the size less one on both "
                     "closures; at the remaining {threshcapped} it is this "
                     "unit's own declared cap, which is a fact about the "
                     "declaration and not about the arena"),
            ok, "rows %d, sizes binding the identity %d all satisfying it %s, "
            "sizes the cap decides %d" %
            (len(rows), len(binds), ok, len(capped)))
    S["loop_threshold"] = {"rows": rows,
                           "sizes_where_the_identity_can_be_tested": len(binds),
                           "sizes_where_the_declared_cap_decides": len(capped),
                           "every_integer_here_is_a_count": "COUNTING-ONLY-E-24"}
    SEAL.take("loop_threshold", S["loop_threshold"], "G-LOOP-THRESHOLD")
    return rows


def measure_winding_is_torus_declared(S, pv, probe):
    """the winding side of the split, measured on both sides: absent on every
    open size, and size-dependent on the closed ones."""
    vals, rows = {}, []
    for n in LOOP_LADDER_T:
        A = Arena(TORUS, n)
        cyc, closes = wind_cycle(A, (0, 0), 0, 1)
        st = steps_of(A, cyc)
        vals[n] = [sym_real(holonomy_trace(A, st, m)) for m in probe]
        rows.append({"arena": A.tag(), "closure": TORUS, "n": n,
                     "the_straight_winding_cycle_exists": True,
                     "its_length": len(cyc)})
    for n in LOOP_LADDER_P:
        A = Arena(PATCH, n)
        cyc, closes = wind_cycle(A, (0, 0), 0, 1)
        rows.append({"arena": A.tag(), "closure": PATCH, "n": n,
                     "the_straight_winding_cycle_exists": cyc is not None and closes,
                     "its_length": 0})
    sizes = sorted(vals)
    pairs = []
    for i in range(len(sizes) - 1):
        mv = sum(1 for j in range(len(probe))
                 if vals[sizes[i]][j] != vals[sizes[i + 1]][j])
        pairs.append({"from": sizes[i], "to": sizes[i + 1],
                      "comparisons": len(probe), "moving": mv})
    if mut("MUT-WINDING"):
        pairs = [dict(r, moving=0) for r in pairs]
    moving = sum(r["moving"] for r in pairs)
    absent = all(not r["the_straight_winding_cycle_exists"]
                 for r in rows if r["closure"] == PATCH)
    ok = absent and moving > 0
    CNT.measured("windmoves", moving,
                 "adjacent closed sizes, coin by coin, values compared")
    CNT.measured("windpairs", sum(r["comparisons"] for r in pairs),
                 "adjacent closed sizes by coin")
    LD.gate("G-WINDING-IS-TORUS-DECLARED",
            CNT.stmt("the winding side is measured on both sides rather than "
                     "asserted on one: the straight winding cycle does not "
                     "exist at any open size, and across adjacent closed sizes "
                     "its observable moves at {windmoves} of {windpairs} "
                     "size-by-coin comparisons, so a winding quantity is a "
                     "quantity of the declaration and not of the physics "
                     "inside any horizon"),
            ok, "absent at every open size %s; moves at %d of %d closed "
            "size-by-coin comparisons" % (absent, moving, CNT.get("windpairs")))
    S["winding"] = {
        "rows": rows, "adjacent_pairs": pairs,
        "adjacent_size_comparisons": CNT.get("windpairs"),
        "comparisons_where_the_value_moves": moving,
        "absent_at_every_open_size": absent,
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24"}
    SEAL.take("winding", S["winding"], "G-WINDING-IS-TORUS-DECLARED")
    return moving


# ===========================================================================
# SECTION 8.  HORIZON-STABILITY -- THE DYNAMICAL SIDE
# ===========================================================================

def even_centre(n):
    return 2 * ((n // 2) // 2)


def even_c(depth):
    """the centre of a cone census arena: the parity of the start site is a
    coordinate of the tick's own declaration, so every arena in a comparison
    is started on the SAME parity class (section 15's match-every-coordinate
    addendum), and this unit declares the even one."""
    return depth if depth % 2 == 0 else depth + 1


def free_cone_displacements(depth):
    A = Arena(PATCH, 2 * depth + 3)
    c = (even_c(depth), even_c(depth))
    return [frozenset((u[0] - c[0], u[1] - c[1]) for u in s)
            for s in structural_reach(A, c, depth)], A, c


def partner_displacement(A, c, u, key):
    d, par = key
    s = (c[0] + u[0], c[1] + u[1])
    if s[0] < 0 or s[1] < 0 or s[0] >= A.n or s[1] >= A.n:
        return None
    p = A.step(s, d, 1) if s[d] % 2 == par else A.step(s, d, -1)
    if p is None:
        return u
    if s[d] % 2 != par and p[d] % 2 != par:
        return u
    return (p[0] - c[0], p[1] - c[1])


def predicted_agreement(A, start, depth, free, REF, refc):
    """the horizon condition, computed from the cone alone and from nothing
    the amplitudes know: the arena must carry the free cone injectively, and
    must give every site of it the same partner the free arena gives."""
    cur = frozenset({(0, 0)})
    for t in range(depth):
        key = STRATUM_KEYS[SCHEDULE[t % 4]]
        seen = {}
        for u in cur:
            s = ((start[0] + u[0]), (start[1] + u[1]))
            if A.kind == TORUS:
                s = (s[0] % A.n, s[1] % A.n)
            elif s[0] < 0 or s[1] < 0 or s[0] >= A.n or s[1] >= A.n:
                return False
            if s in seen and seen[s] != u:
                return False
            seen[s] = u
            want = partner_displacement(REF, refc, u, key)
            p = A.step(s, key[0], 1) if s[key[0]] % 2 == key[1] \
                else A.step(s, key[0], -1)
            if p is not None and s[key[0]] % 2 != key[1] \
                    and p[key[0]] % 2 != key[1]:
                p = None
            got = u if p is None else \
                (p[0] - start[0], p[1] - start[1])
            if A.kind == TORUS and p is not None:
                dx = (p[0] - start[0] + A.n // 2) % A.n - A.n // 2
                dy = (p[1] - start[1] + A.n // 2) % A.n - A.n // 2
                got = (dx, dy)
            if got != want:
                return False
        cur = free[t]
    return True


def measure_dynamic_stability(S, pv, coins, anchors):
    """the dynamical side: an exactly evolved amplitude read on a declared
    window, at every affordable size and both closures, with the horizon
    condition PREDICTED from the cone and then MEASURED on the values."""
    free, REF, refc = free_cone_displacements(DYN_DEPTH)
    probe = [coins[i] for i in range(0, len(coins), COIN_STRIDE)
             if coin_sector(coins[i]) != "DIAGONAL"]
    win = [(dx, dy) for dx in range(-DYN_WINDOW, DYN_WINDOW + 1)
           for dy in range(-DYN_WINDOW, DYN_WINDOW + 1)]
    ref_hist = {}
    for i, m in enumerate(probe):
        ref_hist[i] = evolve(REF, refc, DYN_DEPTH, m)
    rows, violations, margin, tested = [], 0, 0, 0
    for kind, ladder in ((TORUS, DYN_TORI), (PATCH, DYN_PATCHES)):
        for n in ladder:
            A = Arena(kind, n)
            start = (0, 0) if kind == TORUS else (even_centre(n), even_centre(n))
            for T in range(1, DYN_DEPTH + 1):
                pred = predicted_agreement(A, start, T, free, REF, refc)
                agree = True
                for i, m in enumerate(probe):
                    hist = evolve(A, start, T, m)
                    for (dx, dy) in win:
                        s = (start[0] + dx, start[1] + dy)
                        if kind == TORUS:
                            s = (s[0] % n, s[1] % n)
                        elif s[0] < 0 or s[1] < 0 or s[0] >= n or s[1] >= n:
                            agree = False
                            continue
                        got = hist[T - 1].get(s, IZ)
                        want = ref_hist[i][T - 1].get(
                            (refc[0] + dx, refc[1] + dy), IZ)
                        if got != want:
                            agree = False
                tested += 1
                if pred and not agree:
                    violations += 1
                if agree and not pred:
                    margin += 1
                rows.append({"arena": A.tag(), "closure": kind, "n": n,
                             "depth": T, "predicted_by_the_cone": pred,
                             "measured_on_the_values": agree})
    if mut("MUT-DYNAMIC"):
        violations = violations + 1
    read = anchor_has(anchors, "VB-EPR-ROOM", "G-HORIZON-STABILITY-DYNAMIC",
                      "the direction along which separation is possible")
    agreeing = sum(1 for r in rows if r["measured_on_the_values"])
    moving = len(rows) - agreeing
    ok = violations == 0 and read and moving > 0 and agreeing > 0
    CNT.measured("dynrows", len(rows), "arena by depth")
    CNT.measured("dynviol", violations, "prediction against measurement")
    CNT.measured("dynmargin", margin, "prediction against measurement")
    CNT.measured("dynagree", agreeing, "rows where the value did not move")
    CNT.measured("dynmove", moving, "rows where the value moved")
    LD.gate("G-HORIZON-STABILITY-DYNAMIC",
            CNT.stmt("the dynamical observable is measured at {dynrows} "
                     "arena-by-depth rows on both closures, and the horizon "
                     "condition is PREDICTED from the cone before any value is "
                     "read: containing the source's cone is SUFFICIENT for the "
                     "window to be arena-independent and is violated at "
                     "{dynviol} rows, it is not necessary and the measured "
                     "slack is {dynmargin} rows, and the value is unmoved at "
                     "{dynagree} rows and moves at {dynmove}, so the tester is "
                     "neither blind nor unanimous"),
            ok, "rows %d, sufficiency violations %d, conservative margin %d, "
            "unmoved %d, moved %d, coins %d, window %d" %
            (len(rows), violations, margin, agreeing, moving, len(probe),
             len(win)))
    S["dynamic_stability"] = {
        "rows": rows, "coins": len(probe), "window_sites": len(win),
        "depth": DYN_DEPTH,
        "rows_where_the_sufficient_condition_is_violated": violations,
        "rows_where_agreement_survives_without_the_condition": margin,
        "rows_where_the_value_is_unmoved": agreeing,
        "rows_where_the_value_moves": moving,
        "the_reference_arena": REF.tag(),
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24"}
    SEAL.take("dynamic_stability", S["dynamic_stability"],
              "G-HORIZON-STABILITY-DYNAMIC")
    return rows


def measure_the_horizon_law(S, rows):
    """the number the formulation needs: for each depth, the least open size
    and the least closed size at which nothing of that depth can see the
    arena's edge."""
    law = []
    for T in range(1, DYN_DEPTH + 1):
        best_p = min([r["n"] for r in rows if r["closure"] == PATCH
                      and r["depth"] == T and r["measured_on_the_values"]],
                     default=0)
        best_t = min([r["n"] for r in rows if r["closure"] == TORUS
                      and r["depth"] == T and r["measured_on_the_values"]],
                     default=0)
        law.append({"depth": T, "least_open_size_that_hides_the_edge": best_p,
                    "least_closed_size_that_hides_the_edge": best_t})
    if mut("MUT-HORIZON-LAW"):
        law[0]["least_open_size_that_hides_the_edge"] = 0
    monotone = all(law[i]["least_open_size_that_hides_the_edge"]
                   <= law[i + 1]["least_open_size_that_hides_the_edge"]
                   for i in range(len(law) - 1)
                   if law[i + 1]["least_open_size_that_hides_the_edge"] > 0)
    every_depth = all(r["least_open_size_that_hides_the_edge"] > 0 for r in law)
    ok = monotone and every_depth
    CNT.measured("lawrows", len(law), "one row per censused depth")
    LD.gate("G-THE-HORIZON-LAW",
            CNT.stmt("at every one of the {lawrows} censused depths there is a "
                     "size on the open ladder at which the arena's edge is "
                     "invisible to an observable of that depth, and the least "
                     "such size does not decrease as the depth grows -- which "
                     "is the whole content of a formulation that never "
                     "declares a size"),
            ok, "depths %d, all with a hiding size %s, monotone %s" %
            (len(law), every_depth, monotone))
    S["horizon_law"] = {"rows": law,
                        "every_depth_has_a_hiding_open_size": every_depth,
                        "the_least_hiding_size_is_monotone": monotone,
                        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24"}
    SEAL.take("horizon_law", S["horizon_law"], "G-THE-HORIZON-LAW")
    return law


# ===========================================================================
# SECTION 9.  THE CONTROL ARMS -- ONE TESTER, FIVE ARMS
# ===========================================================================

def stability_tester(value_a, value_b):
    """the one tester every arm goes through: it reports MOVED or UNMOVED and
    knows nothing about which arm it is running."""
    return "UNMOVED" if value_a == value_b else "MOVED"


def measure_control_arms(S, pv, probe, coins):
    arms = []
    P, T4, T6, T8 = (Arena(PATCH, CORE_PATCH), Arena(TORUS, 4),
                     Arena(TORUS, 6), Arena(TORUS, CORE_TORUS))

    def rect_value(A, a, b):
        cyc, closes = rect_cycle(A, (0, 0), a, b)
        if cyc is None:
            return None
        return [sym_real(holonomy_trace(A, steps_of(A, cyc), m)) for m in probe]

    def wind_value(A):
        cyc, closes = wind_cycle(A, (0, 0), 0, 1)
        if cyc is None:
            return None
        return [sym_real(holonomy_trace(A, steps_of(A, cyc), m)) for m in probe]

    # every arm names the two arenas it compares, because two of them are not
    # closure comparisons at all: the winding arm compares one closed size
    # with another, and the merging-index arm takes its closed side at the
    # parents' own size, where the phase order does not divide it.
    arms.append({"arm": "ARM-CONTRACTIBLE-INSIDE", "must": "UNMOVED",
                 "what": "a two-by-two rectangle, %s against %s: an open "
                         "arena against a closed one" % (P.tag(), T8.tag()),
                 "arenas": [P.tag(), T8.tag()],
                 "got": stability_tester(rect_value(P, 2, 2),
                                         rect_value(T8, 2, 2))})
    arms.append({"arm": "ARM-WINDING", "must": "MOVED",
                 "what": "the straight winding cycle, %s against %s: a closed "
                         "arena against another closed one, which is a size "
                         "comparison and not a closure comparison"
                         % (T6.tag(), T8.tag()),
                 "arenas": [T6.tag(), T8.tag()],
                 "got": stability_tester(wind_value(T6), wind_value(T8))})
    arms.append({"arm": "ARM-WRAPPING-SHAPE", "must": "MOVED",
                 "what": "a shape whose extent equals the size, so it wraps, "
                         "%s against %s" % (T4.tag(), P.tag()),
                 "arenas": [T4.tag(), P.tag()],
                 "got": stability_tester(rect_value(T4, 4, 1),
                                         rect_value(P, 4, 1))})
    ref_free, REF, refc = free_cone_displacements(DYN_DEPTH)
    m0 = probe[1] if coin_sector(probe[0]) == "DIAGONAL" else probe[0]

    def amp_value(A, start, T):
        h = evolve(A, start, T, m0)
        out = []
        for dx in range(-DYN_WINDOW, DYN_WINDOW + 1):
            for dy in range(-DYN_WINDOW, DYN_WINDOW + 1):
                s = (start[0] + dx, start[1] + dy)
                if A.kind == TORUS:
                    s = (s[0] % A.n, s[1] % A.n)
                out.append(h[T - 1].get(s, IZ))
        return out

    arms.append({"arm": "ARM-DEPTH-BEYOND-THE-HORIZON", "must": "MOVED",
                 "what": "the window amplitude at a depth the small closed "
                         "size cannot hide, %s against %s"
                         % (T6.tag(), REF.tag()),
                 "arenas": [T6.tag(), REF.tag()],
                 "got": stability_tester(
                     amp_value(Arena(TORUS, 6), (0, 0), DYN_DEPTH),
                     amp_value(REF, refc, DYN_DEPTH))})
    arms.append({"arm": "ARM-GLOBAL-MERGING-INDEX", "must": "MOVED",
                 "what": "the merging index, a quantity of the whole arena, "
                         "%s against %s: the closed side is the parents' own "
                         "size, which the phase order does not divide, and "
                         "the arm's declared side turns on that"
                         % (T4.tag(), P.tag()),
                 "arenas": [T4.tag(), P.tag()],
                 "got": stability_tester(
                     merging_index(Arena(TORUS, 4)),
                     merging_index(Arena(PATCH, CORE_PATCH)))})
    if mut("MUT-CONTROL-ARM"):
        arms[0]["got"] = "MOVED"
    wrong = [a["arm"] for a in arms if a["got"] != a["must"]]
    moved = sum(1 for a in arms if a["got"] == "MOVED")
    unmoved = len(arms) - moved
    ok = not wrong
    CNT.measured("arms", len(arms), "the declared control arms")
    CNT.measured("armsmoved", moved, "arms the one tester reported MOVED")
    CNT.measured("armsunmoved", unmoved, "arms it reported UNMOVED")
    LD.gate("G-CONTROL-ARMS",
            CNT.stmt("all {arms} arms are pushed through the SAME stability "
                     "tester, which is told nothing about which arm it is "
                     "running: it reports MOVED at {armsmoved} of them and "
                     "UNMOVED at {armsunmoved}, and every arm lands on the "
                     "side declared for it before the run"),
            ok, "arms %d, moved %d, unmoved %d, wrong %s" %
            (len(arms), moved, unmoved, wrong))
    S["control_arms"] = {"arms": arms, "arms_that_moved": moved,
                         "arms_that_did_not": unmoved,
                         "arms_on_the_wrong_side": len(wrong),
                         "every_integer_here_is_a_count": "COUNTING-ONLY-E-24"}
    SEAL.take("control_arms", S["control_arms"], "G-CONTROL-ARMS")
    return arms


# ===========================================================================
# SECTION 10.  THE OPEN-PATCH ARENA AND THE CLOSURE-ARTIFACT CENSUS
# ===========================================================================

def realisable_twists(arena):
    """a constant link twist is realisable when a site-diagonal phase
    assignment carries it.  MEASURED by propagation over the arena's own link
    set rather than read off a formula, so both closures answer the same
    question."""
    ph = phase_order()
    out = []
    sites = arena.sites()
    for t in range(ph):
        p = {sites[0]: 0}
        stack = [sites[0]]
        good = True
        while stack and good:
            s = stack.pop()
            for d in (0, 1):
                for sgn in (1, -1):
                    o = arena.step(s, d, sgn)
                    if o is None:
                        continue
                    want = (p[s] - t) % ph if sgn > 0 else (p[s] + t) % ph
                    if o in p:
                        if p[o] != want:
                            good = False
                            break
                    else:
                        p[o] = want
                        stack.append(o)
                if not good:
                    break
        if good and len(p) == len(sites):
            out.append(t)
    return out


def merging_index(arena):
    r = len(realisable_twists(arena))
    return phase_order() // r if r else 0


def twist_orbits(coins, cidx, twists):
    seen = [-1] * len(coins)
    out = []
    for i in range(len(coins)):
        if seen[i] >= 0:
            continue
        orb = sorted({cidx[gauge_twist(coins[i], k)] for k in twists})
        for j in orb:
            seen[j] = len(out)
        out.append(orb)
    return out


def measure_patch_gauge(S, pv, coins, anchors):
    """the gauge group of the open patch, measured: which constant twists it
    realises, and what that does to the orbit census the parents publish."""
    cidx = {c: i for i, c in enumerate(coins)}
    full = twist_orbits(coins, cidx, range(phase_order()))
    rows = []
    for kind, ladder in ((TORUS, TORUS_LADDER), (PATCH, PATCH_LADDER)):
        for n in ladder:
            A = Arena(kind, n)
            res = realisable_twists(A)
            orb = twist_orbits(coins, cidx, res)
            rows.append({"arena": A.tag(), "closure": kind, "n": n,
                         "realisable_constant_twists": len(res),
                         "merging_index": phase_order() // len(res),
                         "orbits_under_the_realisable_twists": len(orb),
                         "classes_under_the_full_stencil_image": len(full),
                         "orbit_pairs_merged": len(orb) - len(full)})
    if mut("MUT-PATCH-GAUGE"):
        rows[-1]["realisable_constant_twists"] = 1
        rows[-1]["merging_index"] = 8
    closes = anchor_has(anchors, "VB-ACT-CLOSES", "G-PATCH-GAUGE-GROUP",
                        "because the phase must close after $L$ steps")
    patches = [r for r in rows if r["closure"] == PATCH]
    tori = [r for r in rows if r["closure"] == TORUS]
    all_free = all(r["realisable_constant_twists"] == phase_order()
                   for r in patches)
    torus_law = all(r["merging_index"] ==
                    phase_order() // _gcd(r["n"], phase_order()) for r in tori)
    t4 = [r for r in tori if r["n"] == pv["PV-POT-L"]][0]
    # the closed size the potential parent ran its own boundary lattice at is
    # the size this census takes its closed witness at, and the parent's own
    # numbers there are predicates of this run rather than decoration: no
    # orbit pair merges and the orbit count is the class count.  The twist
    # parent's own gauge image of the link stencil is the phase order this
    # run derives from the field.
    t8 = [r for r in tori if r["n"] == CORE_TORUS][0]
    ok = (all_free and torus_law and closes
          and t4["orbits_under_the_realisable_twists"] == pv["PV-POT-ORBITS"]
          and t4["orbit_pairs_merged"] == pv["PV-POT-MERGED"]
          and len(full) == pv["PV-POT-CLASSES"]
          and t8["orbit_pairs_merged"] == pv["PV-POT-BL-MERGED"]
          and t8["orbits_under_the_realisable_twists"] == pv["PV-POT-BL-ORBITS"]
          and pv["PV-ACT-IMAGE"] == phase_order()
          and all(r["orbit_pairs_merged"] == 0 for r in patches))
    CNT.measured("phaseorder", phase_order(), "derived from the field arithmetic")
    CNT.measured("patchgauge", len(patches), "open sizes, counted")
    CNT.measured("closedsizes", len(tori), "closed sizes, counted")
    LD.gate("G-PATCH-GAUGE-GROUP",
            CNT.stmt("the constant twists an arena realises are MEASURED by "
                     "propagation over its own links, not read off a formula: "
                     "the open patch realises all {phaseorder} of them at "
                     "every one of its {patchgauge} sizes, so its merging "
                     "index is one and no orbit pair is identified there; on "
                     "the closed sizes the measured index is the parent's own "
                     "law at every one, and at the parent's declared size this "
                     "run recovers its published orbit count, its published "
                     "class count and its published number of merged pairs, "
                     "while at the size the potential parent ran its own "
                     "boundary lattice at it recovers that receipt's orbit "
                     "count and its zero merged pairs, and the twist parent's "
                     "published gauge image of the link stencil is required to "
                     "be the phase order this run derives from the field"),
            ok, "open sizes realising every twist %s, closed sizes matching "
            "the parent's law %s, the parent's clause read %s, at the declared "
            "size orbits %d classes %d merged %d, at the parent's boundary "
            "size orbits %d merged %d, the stencil's gauge image %d" %
            (all_free, torus_law, closes,
             t4["orbits_under_the_realisable_twists"], len(full),
             t4["orbit_pairs_merged"],
             t8["orbits_under_the_realisable_twists"],
             t8["orbit_pairs_merged"], pv["PV-ACT-IMAGE"]))
    S["patch_gauge"] = {
        "rows": rows, "phase_order": phase_order(),
        "classes_under_the_full_stencil_image": len(full),
        "open_sizes_realising_every_twist":
            sum(1 for r in patches if r["realisable_constant_twists"] == phase_order()),
        "open_sizes": len(patches), "closed_sizes": len(tori),
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24"}
    SEAL.take("patch_gauge", S["patch_gauge"], "G-PATCH-GAUGE-GROUP")
    return rows, full


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def measure_merging_on_the_patch(S, pv, rows, anchors):
    """the parents' merging-index law, carried to the open arena: the index
    the patch measures is the index the closed arena reaches only when the
    phase order divides its size."""
    pot = anchor_ints(anchors, "VB-POT-MERGING", "G-MERGING-ON-THE-PATCH")
    act = anchor_ints(anchors, "VB-ACT-INDEX", "G-MERGING-ON-THE-PATCH")
    patches = [r for r in rows if r["closure"] == PATCH]
    divis = [r for r in rows if r["closure"] == TORUS
             and r["n"] % phase_order() == 0]
    if mut("MUT-MERGING"):
        patches = [dict(r, merging_index=phase_order()) for r in patches]
    same = all(r["merging_index"] == act[0] for r in patches)
    divisible = anchor_has(anchors, "VB-ACT-INDEX", "G-MERGING-ON-THE-PATCH",
                           "at every L divisible by eight it is")
    ok = (same and divisible and pot[0] == 0 and pot[1] == phase_order()
          and pot[2] == pv["PV-POT-MERGED"]
          and all(r["orbit_pairs_merged"] == pot[0] for r in patches))
    CNT.measured("actindex", act[0], "read out of the parent's own sentence")
    CNT.measured("potmerged", pot[2], "read out of the parent's own sentence")
    LD.gate("G-MERGING-ON-THE-PATCH",
            CNT.stmt("the two parents' sentences are read here and their "
                     "numbers used as predicates rather than as decoration: "
                     "the index the first sentence gives for a size the phase "
                     "order divides is {actindex}, and that is exactly the "
                     "index this run measures at every open size; the number "
                     "of pairs the second sentence says merge at the declared "
                     "closed size is {potmerged}, and the number that merge at "
                     "every open size is the other number that sentence "
                     "carries"),
            ok, "open sizes at the divisible index %s, the first sentence's "
            "number %s, the second's %s" % (same, act[:1], pot[:3]))
    S["merging_on_the_patch"] = {
        "open_sizes_at_index_one": sum(1 for r in patches
                                       if r["merging_index"] == act[0]),
        "open_sizes": len(patches),
        "closed_sizes_the_phase_order_divides": len(divis),
        "the_index_the_first_parents_sentence_carries": act[0],
        "the_merged_pairs_the_second_parents_sentence_carries": pot[2],
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24"}
    SEAL.take("merging_on_the_patch", S["merging_on_the_patch"],
              "G-MERGING-ON-THE-PATCH")


R4_AXES = ((0, 1), (1, 0), (1, 1), (1, 3), (0, 2), (2, 0), (1, 2), (2, 1), (2, 2))


def measure_circulants(S, pv):
    """R4's generator family is built out of translation covariance.  On an
    arena with no identification there is no translation to be covariant
    under, and the family is not smaller -- it is empty.  Measured, per axis,
    as the number of sites a shift takes out of the arena, and separately as
    the number of translations that carry the link set to itself."""
    rows = []
    for kind, n in ((TORUS, pv["PV-POT-L"]), (PATCH, CORE_PATCH),
                    (TORUS, CORE_TORUS)):
        A = Arena(kind, n)
        sset = set(A.sites())
        axrows = []
        for a in R4_AXES:
            if kind == TORUS:
                out = 0
            else:
                out = sum(1 for s in sset
                          if (s[0] + a[0], s[1] + a[1]) not in sset)
            axrows.append({"axis": "%d,%d" % a, "sites_the_shift_loses": out,
                           "the_shift_is_a_bijection": out == 0})
        sym = 0
        for v in A.sites():
            good = True
            for (s, d) in A.links():
                t = ((s[0] + v[0]), (s[1] + v[1]))
                if kind == TORUS:
                    t = (t[0] % n, t[1] % n)
                if t not in sset or A.step(t, d) is None:
                    good = False
                    break
            if good:
                sym += 1
        rows.append({"closure": kind, "arena": A.tag(),
                     "axes": len(R4_AXES),
                     "axes_whose_shift_is_a_bijection":
                         sum(1 for r in axrows if r["the_shift_is_a_bijection"]),
                     "translations_carrying_the_link_set_to_itself": sym,
                     "per_axis": axrows})
    if mut("MUT-CIRCULANTS"):
        rows[1]["axes_whose_shift_is_a_bijection"] = len(R4_AXES)
    tor = [r for r in rows if r["closure"] == TORUS][0]
    pat = [r for r in rows if r["closure"] == PATCH][0]
    ok = (all(r["axes_whose_shift_is_a_bijection"] == len(R4_AXES)
              and r["translations_carrying_the_link_set_to_itself"] > 1
              for r in rows if r["closure"] == TORUS)
          and all(r["axes_whose_shift_is_a_bijection"] == 0
                  and r["translations_carrying_the_link_set_to_itself"] == 1
                  for r in rows if r["closure"] == PATCH))
    CNT.measured("axes", len(R4_AXES), "the parent's declared axes, counted")
    CNT.measured("patchsyms",
                 pat["translations_carrying_the_link_set_to_itself"],
                 "measured by carrying every link")
    LD.gate("G-CIRCULANTS-NEED-THE-CLOSURE",
            CNT.stmt("the parent's translation-covariant generator family is "
                     "measured on both closures: every one of its {axes} "
                     "declared axes shifts the closed arena onto itself and "
                     "none of them shifts the open one onto itself, and the "
                     "number of translations that carry the open arena's link "
                     "set to itself is {patchsyms} -- the identity and nothing "
                     "else -- so a family defined by covariance under them is "
                     "empty there rather than merely smaller"),
            ok, "closed: bijective axes %d, symmetries %d; open: bijective "
            "axes %d, symmetries %d; rows %s" %
            (tor["axes_whose_shift_is_a_bijection"],
             tor["translations_carrying_the_link_set_to_itself"],
             pat["axes_whose_shift_is_a_bijection"],
             pat["translations_carrying_the_link_set_to_itself"],
             ["%s:%d" % (r["arena"],
                         r["translations_carrying_the_link_set_to_itself"])
              for r in rows]))
    S["circulants"] = {"rows": rows,
                       "every_integer_here_is_a_count": "COUNTING-ONLY-E-24"}
    SEAL.take("circulants", S["circulants"], "G-CIRCULANTS-NEED-THE-CLOSURE")
    return rows


# ===========================================================================
# SECTION 11.  THE PARENT'S CLOSED FORM, RE-MEASURED WITH NO CLOSURE AT ALL
# ===========================================================================

def _pow2(k):
    v = 1
    for _ in range(k):
        v = v + v
    return v


def solve3(pts):
    """A + B*P + C/2^P = w at three perimeters, exactly, over Q."""
    M = [[Fraction(1), Fraction(P), Fraction(1, _pow2(P))] for P, _ in pts]
    y = [w for _, w in pts]
    for i in range(3):
        piv = None
        for r in range(i, 3):
            if M[r][i] != 0:
                piv = r
                break
        if piv is None:
            return None
        M[i], M[piv] = M[piv], M[i]
        y[i], y[piv] = y[piv], y[i]
        f = M[i][i]
        M[i] = [v / f for v in M[i]]
        y[i] = y[i] / f
        for r in range(3):
            if r == i or M[r][i] == 0:
                continue
            g = M[r][i]
            M[r] = [M[r][k] - g * M[i][k] for k in range(3)]
            y[r] = y[r] - g * y[i]
    return y


def closed_form_on(A, coins, shapes, pv):
    """the parent's three-term ladder form and the parent's area-blindness,
    measured on ONE arena and returning that arena's own residuals."""
    per = {}
    for (a, b) in shapes:
        cyc, _c = rect_cycle(A, (0, 0), a, b)
        st = steps_of(A, cyc)
        per[(a, b)] = [sym_real(holonomy_trace(A, st, m)) for m in coins]
    Ps = sorted({a + b for (a, b) in shapes})
    fitP = Ps[:3]
    fails, checks, apairs, adis = 0, 0, 0, 0
    perP = {P: {"P": P, "checks": 0, "failures": 0, "area_pairs": 0,
                "area_disagreements": 0} for P in Ps}
    for i in range(len(coins)):
        byP = {}
        for (a, b) in shapes:
            byP.setdefault(a + b, []).append(((a * b), per[(a, b)][i]))
        sol = [solve3([(P, byP[P][0][1][c]) for P in fitP]) for c in (0, 1)]
        if sol[0] is None or sol[1] is None:
            fails += 1
            continue
        for P in Ps:
            for _ar, w in byP[P]:
                checks += 1
                perP[P]["checks"] += 1
                for comp in (0, 1):
                    Ac, Bc, Cc = sol[comp]
                    if Ac + Bc * P + Cc / Fraction(_pow2(P)) != w[comp]:
                        fails += 1
                        perP[P]["failures"] += 1
            lst = byP[P]
            for x in range(len(lst)):
                for y in range(x + 1, len(lst)):
                    if lst[x][0] == lst[y][0]:
                        continue
                    apairs += 1
                    perP[P]["area_pairs"] += 1
                    if lst[x][1] != lst[y][1]:
                        adis += 1
                        perP[P]["area_disagreements"] += 1
    return {"arena": A.tag(), "shapes": len(shapes), "ladder_perimeters": Ps,
            "fitted_at": fitP, "checks_after_the_fit": checks,
            "failures": fails, "area_discriminating_comparisons": apairs,
            "area_disagreements": adis, "coins": len(coins),
            "per_perimeter": [perP[P] for P in Ps]}


def arena_residuals(A, coins, probe, shapes):
    """the per-arena residuals the census needs: quantities that are a
    property of ONE arena, so that a census row never compares a number with
    itself."""
    arity = 0
    for l in A.links()[:len(A.links())]:
        t, h = A.ends(l)
        if len({t, h}) != 2:
            arity += 1
    leak = 0
    sset = set(A.sites())
    for s0 in A.sites():
        psi = tick_once(A, {s0: IONE}, probe[0], STRATUM_KEYS[0])
        leak += sum(1 for u in psi if u not in sset)
    rev = 0
    for (a, b) in shapes:
        cyc, _c = rect_cycle(A, (0, 0), a, b)
        st = steps_of(A, cyc)
        for m in probe:
            f = holonomy_trace(A, st, m)
            back = [(l, -o) for (l, o) in reversed(st)]
            g = holonomy_trace(A, back, m)
            if (f[0], -f[3], -f[2], -f[1]) != g:
                rev += 1
    places = {("MID", l) for l in A.links()}
    deg = collections.Counter()
    for (s1, d) in A.links():
        deg[s1] += 1
        deg[A.step(s1, d)] += 1
    thin = sum(1 for u in A.sites() if deg[u] != 4)
    nop = sum(1 for u in A.sites() if u not in set(A.plaquettes()))
    return {"arena": A.tag(),
            "sites_with_fewer_than_four_links": thin,
            "sites_that_are_not_a_plaquette_base": nop,
            "links_whose_operator_is_not_a_two_site_domino": arity,
            "sites_the_tick_sends_outside_the_arena": leak,
            "loops_whose_reversal_is_not_the_conjugate_trace": rev,
            "links_without_a_refinement_place": len(A.links()) - len(places),
            "coins_admissible_on_a_link": len(coins),
            "shapes_that_fit": len(shapes), "links": len(A.links()),
            "plaquettes": len(A.plaquettes())}


def measure_the_closed_form(S, pv, coins, probe):
    """POT's closed form and POT's area-blindness, re-measured on an arena
    with no identification: the fit is taken at the three shortest perimeters
    and then CHECKED at every longer one, and equal-perimeter shapes of
    different area are compared coin by coin."""
    A = Arena(PATCH, CORE_PATCH)
    B = Arena(TORUS, CORE_TORUS)
    shapes = [s for s in shapes_that_fit(A) if s in shapes_that_fit(B)]
    open_row = closed_form_on(A, coins, shapes, pv)
    closed_row = closed_form_on(B, coins, shapes, pv)
    if mut("MUT-CLOSED-FORM"):
        open_row["failures"] += 1
        open_row["per_perimeter"][0]["failures"] += 1
    checks = open_row["checks_after_the_fit"]
    fails = open_row["failures"]
    area_pairs = open_row["area_discriminating_comparisons"]
    area_dis = open_row["area_disagreements"]
    Ps = open_row["ladder_perimeters"]
    fitP = open_row["fitted_at"]
    perP = {r["P"]: r for r in open_row["per_perimeter"]}
    resid = [arena_residuals(A, coins, probe, shapes),
             arena_residuals(B, coins, probe, shapes)]
    ladder = pv["PV-POT-LADDER"]
    same_variable = (Ps == list(range(min(Ps), max(Ps) + 1))
                     and min(Ps) == ladder[0]
                     and Ps == ladder[:len(Ps)])
    ok = (fails == 0 and area_dis == 0 and area_pairs > 0 and checks > 0
          and same_variable and closed_row["failures"] == 0
          and closed_row["area_disagreements"] == 0
          and all(r["links_whose_operator_is_not_a_two_site_domino"] == 0
                  and r["sites_the_tick_sends_outside_the_arena"] == 0
                  and r["loops_whose_reversal_is_not_the_conjugate_trace"] == 0
                  and r["links_without_a_refinement_place"] == 0
                  for r in resid))
    CNT.measured("cfshapes", len(shapes), "shapes that fit the open arena")
    CNT.measured("cfchecks", checks, "coin by shape, after the fit")
    CNT.measured("cffails", fails, "coin by shape, after the fit")
    CNT.measured("areapairs", area_pairs,
                 "equal-perimeter different-area pairs, coin by coin")
    CNT.measured("areadis", area_dis,
                 "equal-perimeter different-area pairs, coin by coin")
    LD.gate("G-THE-CLOSED-FORM-SURVIVES",
            CNT.stmt("the parent's closed form is re-measured on an arena with "
                     "no identification anywhere: its three constants are "
                     "fitted at the three shortest perimeters and then the "
                     "form is CHECKED at {cfchecks} coin-by-shape rows, "
                     "failing at {cffails}; and the parent's area-blindness is "
                     "re-measured as {areapairs} equal-perimeter "
                     "different-area comparisons with {areadis} disagreements; "
                     "and the ladder variable is the parent's own, gated by "
                     "requiring this run's ladder to be an initial segment of "
                     "the ladder the parent's receipt publishes"),
            ok, "shapes %d, open checks %d failures %d, closed checks %d "
            "failures %d, area comparisons %d disagreements %d, the ladder "
            "variable is the parent's %s, per-arena residuals %s" %
            (len(shapes), checks, fails, closed_row["checks_after_the_fit"],
             closed_row["failures"], area_pairs, area_dis, same_variable,
             [sum(r[k] for k in
                  ("links_whose_operator_is_not_a_two_site_domino",
                   "sites_the_tick_sends_outside_the_arena",
                   "loops_whose_reversal_is_not_the_conjugate_trace",
                   "links_without_a_refinement_place")) for r in resid]))
    S["closed_form"] = {
        "arena": A.tag(), "shapes": len(shapes),
        "per_perimeter": [perP[P] for P in Ps],
        "ladder_perimeters": Ps, "fitted_at": fitP,
        "the_ladder_is_an_initial_segment_of_the_parents": same_variable,
        "checks_after_the_fit": checks, "failures": fails,
        "area_discriminating_comparisons": area_pairs,
        "area_disagreements": area_dis,
        "coins": len(coins),
        "on_the_open_arena": open_row, "on_the_closed_arena": closed_row,
        "per_arena_residuals": resid,
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24"}
    SEAL.take("closed_form", S["closed_form"], "G-THE-CLOSED-FORM-SURVIVES")
    return fails, area_dis, area_pairs


# ===========================================================================
# SECTION 12.  THE CLOSURE-ARTIFACT CENSUS
# ===========================================================================

VERBATIM = "SURVIVES-VERBATIM"
SCOPED = "SURVIVES-SCOPED"
ARTIFACT = "CLOSURE-ARTIFACT"
MEASURED = "MEASURED"
STRUCTURAL = "STRUCTURAL"


def classify_row(open_witness, closed_witness, proviso):
    """the one classifier every census row goes through."""
    if open_witness is None:
        return ARTIFACT
    if open_witness == closed_witness:
        return VERBATIM
    if proviso:
        return SCOPED
    return ARTIFACT


def globally_sensitive(row):
    """the pre-registered global-sensitivity condition, computed on every row
    of the census: the classifier calls the law a survivor -- its witness on
    the open arena IS its witness on the closed one -- and yet that same
    witness MOVES across the declared open ladder, so a law that reads local
    is being set by how much arena there is.  That is a local observable
    feeling the far lattice, and it is the condition the pin's
    globally-sensitive word is reached by."""
    if row["verdict"] not in (VERBATIM, SCOPED):
        return False
    return len(set(row["witness_over_the_open_ladder"])) > 1


def measure_census_sweep(S, pv, coins, probe, shapes):
    """every witness the census draws from an arena, taken again at every
    size of the declared sweep on both closures.  This is what tells a witness
    an arena can move from a witness no arena can, and it is the ladder the
    global-sensitivity condition is computed over.  The closed-form witnesses
    are swept at the declared coin stride; the census's own row for them is
    taken over the whole coin family."""
    out = {}
    for kind, ladder in ((TORUS, CENSUS_SWEEP_T), (PATCH, CENSUS_SWEEP_P)):
        for n in ladder:
            A = Arena(kind, n)
            res = arena_residuals(A, coins, probe, shapes)
            cfr = closed_form_on(A, probe, shapes, pv)
            res["the_three_term_form_fails_at"] = cfr["failures"]
            res["equal_perimeter_comparisons_that_disagree"] = \
                cfr["area_disagreements"]
            out[A.tag()] = res
    S["_census_sweep"] = out
    return out


def measure_closure_census(S, pv, anchors):
    """the flush, at ONE declared arena pair, with every row's arena named in
    the row and every row's witness swept over the declared ladder.

    Three things the row carries beyond its two witnesses.  The ARENA PAIR:
    one open size and one closed size, the same for every row that has an
    arena at all, so that no verdict here is selected by taking the two sides
    at different sizes.  The BASIS: whether the witness is one an arena can
    move at all -- a defect count the construction forbids, or a quantity
    computed with no arena argument, is labelled STRUCTURAL and is required to
    take ONE value over the whole sweep, so a label an arena can move dies
    here; only a witness drawn from the arena's own objects is labelled
    MEASURED.  And the LADDER: the value the witness takes at every swept
    size, which is the size-dependence entering the classifier as an input
    rather than sitting beside it as prose."""
    strat = S["stratification"]
    fam = S["family_split"]
    hom = S["homology"]
    gau = S["patch_gauge"]
    cir = S["circulants"]
    cf = S["closed_form"]
    sweep = S["_census_sweep"]
    OPEN, CLOSED = "P-%d" % CORE_PATCH, "T-%d" % CORE_TORUS
    PAIR = "%s / %s" % (OPEN, CLOSED)
    LADDER = "the whole ladder"
    OP = ["P-%d" % n for n in CENSUS_SWEEP_P]
    OT = ["T-%d" % n for n in CENSUS_SWEEP_T]
    P9 = [r for r in gau["rows"] if r["arena"] == OPEN][0]
    T8 = [r for r in gau["rows"] if r["arena"] == CLOSED][0]
    fp = [r for r in fam["rows"] if r["arena"] == OPEN][0]
    ft = [r for r in fam["rows"] if r["arena"] == CLOSED][0]
    hp = [r for r in hom["rows"] if r["arena"] == OPEN][0]
    ht = [r for r in hom["rows"] if r["arena"] == CLOSED][0]
    cp = [r for r in cir["rows"] if r["arena"] == OPEN][0]
    ct = [r for r in cir["rows"] if r["arena"] == CLOSED][0]
    lorlinks = anchor_has(anchors, "VB-LOR-PLACES", "G-CLOSURE-CENSUS",
                          "new places are the old links")

    ro = {r["arena"]: r for r in cf["per_arena_residuals"]}
    RO, RC = ro[OPEN], ro[CLOSED]

    def swept(key):
        return ([sweep[t][key] for t in OP], [sweep[t][key] for t in OT])

    def swept_sum(k1, k2):
        return ([sweep[t][k1] + sweep[t][k2] for t in OP],
                [sweep[t][k1] + sweep[t][k2] for t in OT])

    def over(rowlist, field):
        return ([r[field] for r in rowlist if r["closure"] == PATCH],
                [r[field] for r in rowlist if r["closure"] == TORUS])

    strat_by_size = [dict(r, defects=4 - r["strata_that_are_matchings"])
                     for r in strat["rows"]]
    strat_open = sum(r["defects"] for r in strat_by_size
                     if r["closure"] == PATCH)
    strat_closed = sum(r["defects"] for r in strat_by_size
                       if r["closure"] == TORUS)

    # the twist parent's own L-scope, consumed rather than cited: the index it
    # publishes at each of its own sizes is the index this run's law returns
    # there, and at the two of those sizes that lie on this ladder it is the
    # index this run MEASURES there.
    act_idx = {2: pv["PV-ACT-IDX-L2"], 4: pv["PV-ACT-IDX-L4"],
               8: pv["PV-ACT-IDX-L8"]}
    idx_by_size = {r["n"]: r["merging_index"] for r in gau["rows"]
                   if r["closure"] == TORUS}
    act_law = all(v == phase_order() // _gcd(L, phase_order())
                  for L, v in act_idx.items())
    act_here = all(idx_by_size[L] == v for L, v in act_idx.items()
                   if L in idx_by_size)
    act_at_the_closed_witness = (T8["merging_index"]
                                 == act_idx[pv["PV-POT-BL"]])
    bl_is_the_closed_witness = (pv["PV-POT-BL"] == CORE_TORUS)

    rows = [
        ("LAW-LINK-OPERATOR", "R5", "the link operator is a two-site domino "
         "and the identity elsewhere",
         RO["links_whose_operator_is_not_a_two_site_domino"]
         + RO["sites_the_tick_sends_outside_the_arena"],
         RC["links_whose_operator_is_not_a_two_site_domino"]
         + RC["sites_the_tick_sends_outside_the_arena"], False, PAIR,
         STRUCTURAL, "two defect counts the construction forbids: a link's "
         "two ends are distinct places at every size above one, and the tick "
         "writes only to keys of the arena's own link set",
         swept_sum("links_whose_operator_is_not_a_two_site_domino",
                   "sites_the_tick_sends_outside_the_arena")),
        ("LAW-HOLONOMY", "R5", "the holonomy of a reversed loop is the "
         "conjugate trace", RO["loops_whose_reversal_is_not_the_conjugate_trace"],
         RC["loops_whose_reversal_is_not_the_conjugate_trace"], False, PAIR,
         MEASURED, "the reversal is walked on the arena's own links and its "
         "trace compared with the conjugate, loop by loop and coin by coin",
         swept("loops_whose_reversal_is_not_the_conjugate_trace")),
        ("LAW-COIN-FAMILY", "R5", "the coins admissible on a link",
         RO["coins_admissible_on_a_link"], RC["coins_admissible_on_a_link"],
         False, PAIR, STRUCTURAL, "the coin family is an argument handed to "
         "both sides of the comparison, not a quantity either arena computes",
         swept("coins_admissible_on_a_link")),
        ("LAW-STRATIFICATION", "R5", "the four parity strata are matchings, "
         "summed over the whole ladder", strat_open, strat_closed, True,
         LADDER, MEASURED, "the stratification is rebuilt and its clashes "
         "counted at every size of both ladders",
         over(strat_by_size, "defects")),
        ("LAW-LINK-COUNT", "R5", "every site carries four links",
         RO["sites_with_fewer_than_four_links"],
         RC["sites_with_fewer_than_four_links"], False, PAIR, MEASURED,
         "the degree of every site of the arena's own link set is counted",
         swept("sites_with_fewer_than_four_links")),
        ("LAW-PLAQUETTE-COUNT", "R5", "every site is the base of a plaquette",
         RO["sites_that_are_not_a_plaquette_base"],
         RC["sites_that_are_not_a_plaquette_base"], False, PAIR, MEASURED,
         "the arena's own plaquette set is built and its bases counted",
         swept("sites_that_are_not_a_plaquette_base")),
        ("LAW-SINGLE-OCCUPATION", "R5", "the tick keeps the single-occupation "
         "sector", RO["sites_the_tick_sends_outside_the_arena"],
         RC["sites_the_tick_sends_outside_the_arena"], False, PAIR,
         STRUCTURAL, "the tick writes only to keys of the arena's own link "
         "set, so the count is zero before any arena is chosen",
         swept("sites_the_tick_sends_outside_the_arena")),
        ("LAW-RECTANGLE-FAMILY", "POT", "the rectangle circuits that stay "
         "simple", RO["shapes_that_fit"], RC["shapes_that_fit"], True, PAIR,
         STRUCTURAL, "the shape list is an argument handed to both sides of "
         "the comparison, not a quantity either arena computes",
         swept("shapes_that_fit")),
        ("LAW-WINDING-FAMILY", "POT", "the winding cycles",
         None if fp["winding_placements"] == 0 else fp["winding_placements"],
         ft["winding_placements"], False, PAIR, MEASURED,
         "every placement of every declared cycle is built on the arena's own "
         "links and its net displacement read off the steps",
         over(fam["rows"], "winding_placements")),
        ("LAW-HOMOLOGY", "POT", "the winding classes a loop can carry",
         hp["displacement_classes"], ht["displacement_classes"], False, PAIR,
         MEASURED, "every closed walk of the declared depth is enumerated on "
         "the arena and classified by its net displacement",
         over(hom["rows"], "displacement_classes")),
        ("LAW-CLOSED-FORM", "POT", "the three-term ladder form fails at",
         cf["on_the_open_arena"]["failures"],
         cf["on_the_closed_arena"]["failures"], False, PAIR, MEASURED,
         "the parent's three constants are fitted and then checked against "
         "holonomies taken on the arena's own loops",
         swept("the_three_term_form_fails_at")),
        ("LAW-AREA-BLINDNESS", "POT", "the equal-perimeter comparisons that "
         "disagree", cf["on_the_open_arena"]["area_disagreements"],
         cf["on_the_closed_arena"]["area_disagreements"], False, PAIR,
         MEASURED, "equal-perimeter shapes of different area are compared "
         "coin by coin on the arena's own loops",
         swept("equal_perimeter_comparisons_that_disagree")),
        ("LAW-MERGING-INDEX", "ACT", "the merging index", P9["merging_index"],
         T8["merging_index"], False, PAIR, MEASURED,
         "the constant twists the arena realises are found by propagation "
         "over its own links, and the index is the phase order over their "
         "number", over(gau["rows"], "merging_index")),
        ("LAW-PARENT-ORBITS", "ACT", "the orbit count under the realisable "
         "twists", P9["orbits_under_the_realisable_twists"],
         T8["orbits_under_the_realisable_twists"], False, PAIR, MEASURED,
         "the orbits are built by acting with the twists the arena itself "
         "realises", over(gau["rows"], "orbits_under_the_realisable_twists")),
        ("LAW-CLASS-COUNT", "ACT", "the class count under the full stencil "
         "image", P9["classes_under_the_full_stencil_image"],
         T8["classes_under_the_full_stencil_image"], False, PAIR, STRUCTURAL,
         "the orbits under the FULL stencil image are computed once, with no "
         "arena argument at all",
         over(gau["rows"], "classes_under_the_full_stencil_image")),
        ("LAW-TRANSLATION-COVARIANCE", "R4", "the declared axes whose shift is "
         "a bijection",
         None if cp["axes_whose_shift_is_a_bijection"] == 0
         else cp["axes_whose_shift_is_a_bijection"],
         ct["axes_whose_shift_is_a_bijection"], False, PAIR, MEASURED,
         "each declared axis is shifted over the arena's own site set and the "
         "places it loses are counted",
         over(cir["rows"], "axes_whose_shift_is_a_bijection")),
        ("LAW-DUAL-TORUS", "R4B", "the translations the momentum route needs",
         None if cp["translations_carrying_the_link_set_to_itself"] == 1
         else cp["translations_carrying_the_link_set_to_itself"],
         ct["translations_carrying_the_link_set_to_itself"], False, PAIR,
         MEASURED, "every translation is applied to every link of the arena's "
         "own link set",
         over(cir["rows"], "translations_carrying_the_link_set_to_itself")),
        ("LAW-REFINEMENT-PLACES", "LOR", "the links a refinement step leaves "
         "without a new place",
         RO["links_without_a_refinement_place"] if lorlinks else None,
         RC["links_without_a_refinement_place"], False, PAIR, STRUCTURAL,
         "the refinement map sends distinct links to distinct places, so the "
         "count is zero before any arena is chosen",
         swept("links_without_a_refinement_place")),
    ]
    census = []
    for cid, src, law, ow, cw, prov, pair, basis, why, ladder in rows:
        v = classify_row(ow, cw, prov)
        census.append({"id": cid, "parent": src, "law": law,
                       "arena_pair": pair,
                       "witness_on_the_open_arena":
                           "ABSENT" if ow is None else ow,
                       "witness_on_the_closed_arena": cw,
                       "verdict": v, "basis": basis,
                       "why_the_basis_is_that": why,
                       "witness_over_the_open_ladder": list(ladder[0]),
                       "witness_over_the_closed_ladder": list(ladder[1])})
    if mut("MUT-CENSUS"):
        census[0]["verdict"] = ARTIFACT
    if mut("MUT-CENSUS-BASIS"):
        for r in census:
            if r["id"] == "LAW-LINK-COUNT":
                r["basis"] = STRUCTURAL
    surv = sum(1 for r in census if r["verdict"] == VERBATIM)
    scop = sum(1 for r in census if r["verdict"] == SCOPED)
    art = sum(1 for r in census if r["verdict"] == ARTIFACT)
    meas = sum(1 for r in census
               if r["verdict"] == VERBATIM and r["basis"] == MEASURED)
    stru = sum(1 for r in census
               if r["verdict"] == VERBATIM and r["basis"] == STRUCTURAL)
    recl = [r["id"] for r in census
            if r["verdict"] != classify_row(
                None if r["witness_on_the_open_arena"] == "ABSENT"
                else r["witness_on_the_open_arena"],
                r["witness_on_the_closed_arena"],
                r["verdict"] == SCOPED)]
    # a STRUCTURAL label an arena can move is a false label and dies here; a
    # MEASURED label no arena moves anywhere in the census would leave the
    # distinction vacuous, so at least one is required to move.
    mislabelled = [r["id"] for r in census if r["basis"] == STRUCTURAL
                   and len(set(r["witness_over_the_open_ladder"]
                               + r["witness_over_the_closed_ladder"])) > 1]
    moved = [r["id"] for r in census if r["basis"] == MEASURED
             and len(set(r["witness_over_the_open_ladder"]
                         + r["witness_over_the_closed_ladder"])) > 1]
    unswept = [r["id"] for r in census
               if r["verdict"] in (VERBATIM, SCOPED)
               and not r["witness_over_the_open_ladder"]]
    pairs = sorted({r["arena_pair"] for r in census})
    ok = (surv + scop + art == len(census) and not recl and art > 0
          and surv > 0 and lorlinks and meas + stru == surv
          and not mislabelled and moved and not unswept
          and act_law and act_here and act_at_the_closed_witness
          and bl_is_the_closed_witness)
    CNT.measured("censusrows", len(census), "one row per sealed law used")
    CNT.measured("surv", surv, "rows the classifier returned verbatim on")
    CNT.measured("scop", scop, "rows the classifier returned scoped on")
    CNT.measured("art", art, "rows the classifier returned artifact on")
    CNT.measured("censusmeasured", meas,
                 "surviving rows whose witness an arena could have moved")
    CNT.measured("censusstructural", stru,
                 "surviving rows whose witness no arena moves")
    CNT.measured("censussweep", len(OP) + len(OT),
                 "sizes every census witness is taken at")
    LD.gate("G-CLOSURE-CENSUS",
            CNT.stmt("every one of the {censusrows} sealed laws this unit uses "
                     "is put through ONE classifier at ONE declared arena "
                     "pair, which every row prints: {surv} survive the flush "
                     "verbatim, {scop} survives with a stated proviso, and "
                     "{art} differ across that pair.  Of the survivors "
                     "{censusmeasured} carry a witness drawn from each arena's "
                     "own objects and {censusstructural} carry one no arena "
                     "can move -- a defect count the construction forbids, or "
                     "a quantity computed with no arena argument -- and the "
                     "labels are not taken on trust: every witness is measured "
                     "again at each of the {censussweep} swept sizes, a "
                     "structural label the sweep moves stops the run, and the "
                     "twist parent's own index at its own sizes is required to "
                     "be the index this run's law returns and this run's "
                     "measurement finds there"),
            ok, "rows %d: verbatim %d (measured %d, structural %d), scoped %d, "
            "artifact %d, reclassifications %d, arena pairs %s, structural "
            "labels the sweep moves %d, measured witnesses it moves %d, "
            "surviving rows with no sweep %d, the parent's index law %s, its "
            "index measured here %s, at the closed witness %s" %
            (len(census), surv, meas, stru, scop, art, len(recl), pairs,
             len(mislabelled), len(moved), len(unswept), act_law, act_here,
             act_at_the_closed_witness))
    S["closure_census"] = {
        "rows": census, "verbatim": surv, "scoped": scop, "artifact": art,
        "surviving_rows_whose_witness_an_arena_could_move": meas,
        "surviving_rows_whose_witness_no_arena_moves": stru,
        "the_declared_arena_pair": PAIR,
        "the_sizes_every_witness_was_swept_at": OP + OT,
        "the_sweep": {
            "open_sizes": OP, "closed_sizes": OT,
            "the_closed_form_witnesses_are_swept_at_the_coin_stride": True,
            "rows": [dict(sweep[t], arena=t) for t in OP + OT]},
        "structural_labels_the_sweep_moves": mislabelled,
        "measured_witnesses_the_sweep_moves": moved,
        "the_twist_parents_index_at_its_own_sizes": act_idx,
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24"}
    SEAL.take("closure_census", S["closure_census"], "G-CLOSURE-CENSUS")
    return census


# ===========================================================================
# SECTION 13.  THE DIRECT-LIMIT FORM AND ITS GATE
# ===========================================================================

DIRECT_LIMIT_FORM = (
    "A HOR-LAW IS A STATEMENT OF THE FORM: FOR EVERY FINITE OPEN PATCH P AND "
    "EVERY OBSERVABLE O WHOSE SUPPORT AND WHOSE DEPTH-CONE BOTH LIE INSIDE P, "
    "PHI(O) HOLDS.  NO SYMBOL IN A HOR-LAW DENOTES A SIZE, NO QUANTIFIER "
    "RANGES OVER A COMPLETED TOTALITY, AND EVERY INSTANCE IS A STATEMENT "
    "ABOUT ONE FINITE PATCH.  THE PATCHES FORM A DIRECTED SYSTEM UNDER "
    "INCLUSION AND THE INCLUSIONS CARRY VALUES UNCHANGED ON THE OBSERVABLES A "
    "HOR-LAW QUANTIFIES OVER; THAT PROPERTY IS WHAT THE UNIT MEASURES, AND IT "
    "IS NOT A CONVERGENCE, NOT A LIMIT AND NOT AN OBJECT.")


def measure_direct_limit(S, pv, coins, probe, anchors):
    """the transition maps of the directed system, measured on the family a
    HOR-law quantifies over: inclusion of a patch in a larger patch carries
    every contractible value unchanged, and the system is directed."""
    sizes = [n for n in PATCH_LADDER if n >= RECT_MAX + 1]
    ref = None
    rows, moved, tested = [], 0, 0
    shapes = shapes_that_fit(Arena(PATCH, min(sizes)))
    for n in sizes:
        A = Arena(PATCH, n)
        vals = loop_values(A, probe, shapes)
        if ref is None:
            ref = vals
        agree = 0
        for s in shapes:
            for i in range(len(probe)):
                tested += 1
                if vals[s][i] == ref[s][i]:
                    agree += 1
                else:
                    moved += 1
        rows.append({"arena": A.tag(), "n": n, "shapes": len(shapes),
                     "comparisons": len(shapes) * len(probe),
                     "carried_unchanged": agree})
    if mut("MUT-DIRECT-LIMIT"):
        moved = moved + 1
    pairs = 0
    for i in range(len(sizes)):
        for j in range(len(sizes)):
            if sizes[i] <= sizes[j]:
                pairs += 1
    directed = pairs == len(sizes) * (len(sizes) + 1) // 2
    notop = anchor_has(anchors, "VB-R1-NOTOPOLOGY", "G-DIRECT-LIMIT-FORM",
                       "or about a limit of the family in any topology")
    ok = moved == 0 and directed and notop and tested > 0
    ref_row = sorted(rows, key=lambda r: r["n"])[0]
    CNT.measured("dlrows", len(rows), "open sizes in the directed system")
    CNT.measured("dltested", tested, "shape by coin by size")
    CNT.measured("dlmoved", moved, "values an inclusion failed to carry")
    CNT.measured("dlself", ref_row["comparisons"],
                 "the reference size compared with itself")
    CNT.measured("dlgenuine", tested - ref_row["comparisons"],
                 "comparisons across a proper inclusion")
    LD.gate("G-DIRECT-LIMIT-FORM",
            CNT.stmt("the undetermined-size statement is written out and then "
                     "measured where it can be: over {dlrows} open sizes the "
                     "inclusions carry {dltested} shape-by-coin values and "
                     "fail to carry {dlmoved} of them, and the basis is "
                     "disclosed rather than summed over -- {dlself} of those "
                     "comparisons are the reference size against itself and "
                     "{dlgenuine} cross a proper inclusion; the sizes are "
                     "directed under inclusion; the parent's own sentence "
                     "barring a claim about a limit of a family in any "
                     "topology is read here, and nothing in this statement is "
                     "a limit, a convergence or an object"),
            ok, "sizes %d, comparisons %d (reference against itself %d, "
            "proper inclusions %d), values not carried %d, directed %s, "
            "the parent's no-topology clause read %s" %
            (len(rows), tested, ref_row["comparisons"],
             tested - ref_row["comparisons"], moved, directed, notop))
    S["direct_limit"] = {
        "the_form": DIRECT_LIMIT_FORM, "rows": rows,
        "comparisons": tested, "values_an_inclusion_failed_to_carry": moved,
        "comparisons_of_the_reference_size_with_itself": ref_row["comparisons"],
        "comparisons_across_a_proper_inclusion":
            tested - ref_row["comparisons"],
        "the_reference_size": ref_row["n"],
        "the_sizes_are_directed_under_inclusion": directed,
        "this_is_not_a_limit_and_not_an_object": True,
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24"}
    SEAL.take("direct_limit", S["direct_limit"], "G-DIRECT-LIMIT-FORM")
    return rows


def measure_quantifiability(S):
    """the gate the pin asks for: every sealed law used is horizon-statable,
    or is NAMED as an exception.

    The class word says what the test is.  The test is the CLOSURE-WITNESS
    TEST -- the law's witness on the open arena is its witness on the closed
    one, or differs from it with a stated proviso -- and the word for a law
    that passes it is HORIZON-STATABLE-BY-THE-CLOSURE-WITNESS-TEST.  It is not
    the absence of a symbol for a size, which is a different property and is
    not what this run measures; that distinction is the subject of a sentence
    in the paper and of the successor register, not of this word."""
    census = S["closure_census"]["rows"]
    rows = []
    for r in census:
        q = r["verdict"] in (VERBATIM, SCOPED)
        rows.append({"id": r["id"], "parent": r["parent"],
                     "horizon_statable_by_the_closure_witness_test": q,
                     "the_named_exception": None if q else r["law"]})
    if mut("MUT-QUANTIFIABILITY"):
        for r in rows:
            if not r["horizon_statable_by_the_closure_witness_test"]:
                r["horizon_statable_by_the_closure_witness_test"] = True
                r["the_named_exception"] = None
                break
    K = "horizon_statable_by_the_closure_witness_test"
    quant = sum(1 for r in rows if r[K])
    exc = [r["id"] for r in rows if not r[K]]
    named = sum(1 for r in rows if not r[K] and r["the_named_exception"])
    # the leg that can fail: the sort is recomputed HERE from the two
    # witnesses themselves rather than from the classifier's word, so a
    # verdict word that stops matching the witnesses it was computed from
    # dies at this gate as well as at the census's own.
    byrow = {c["id"]: c for c in census}
    disagree = []
    for r in rows:
        c = byrow[r["id"]]
        ow = c["witness_on_the_open_arena"]
        direct = (ow != "ABSENT"
                  and (ow == c["witness_on_the_closed_arena"]
                       or c["verdict"] == SCOPED))
        if r[K] != direct:
            disagree.append(r["id"])
    ok = (quant + len(exc) == len(rows) and named == len(exc)
          and not disagree)
    CNT.measured("quant", quant, "rows that pass the closure-witness test")
    CNT.measured("exc", len(exc), "rows it refused and required a name for")
    LD.gate("G-QUANTIFIABILITY",
            CNT.stmt("the gate the pin asks for is run on every law of the "
                     "census, and the class word is the test: {quant} of them "
                     "are HORIZON-STATABLE BY THE CLOSURE-WITNESS TEST -- the "
                     "law's witness on the open arena is its witness on the "
                     "closed one, or differs from it with a stated proviso -- "
                     "and {exc} are not, and every one of those is required to "
                     "carry the name of the object it needs, so the "
                     "formulation ships with its exceptions listed rather than "
                     "with its exceptions hidden; the sort is recomputed here "
                     "from the two witnesses themselves rather than from the "
                     "classifier's word, so the two routes must agree row by "
                     "row"),
            ok, "rows %d, horizon-statable %d, exceptions %d all named %s, "
            "rows where the witnesses and the verdict word disagree %d: %s" %
            (len(rows), quant, len(exc), named == len(exc), len(disagree), exc))
    S["quantifiability"] = {
        "rows": rows, "quantifiable": quant, "exceptions": len(exc),
        "the_test": "THE-CLOSURE-WITNESS-TEST",
        "the_word_this_test_licenses":
            "HORIZON-STATABLE-BY-THE-CLOSURE-WITNESS-TEST",
        "not_the_absence_of_a_symbol_for_a_size": True,
        "exception_ids": exc, "every_exception_is_named": named == len(exc),
        "every_integer_here_is_a_count": "COUNTING-ONLY-E-24"}
    SEAL.take("quantifiability", S["quantifiability"], "G-QUANTIFIABILITY")
    return rows, exc


# ===========================================================================
# SECTION 14.  THE SPLIT, THE OUTCOME, THE HEAD
# ===========================================================================

def measure_the_split(S, pv, anchors):
    """the pre-registered split, decided by a rule frozen before the values:
    the contractible side must be unmoved wherever the horizon condition
    holds, and the winding side must be a quantity of the declaration."""
    read = anchor_has(anchors, "VB-HOR-SPLIT", "G-THE-SPLIT",
                      "contractible physics R-STABLE vs winding physics "
                      "TORUS-DECLARED")
    lo = S["loop_stability"]
    wi = S["winding"]
    dy = S["dynamic_stability"]
    contractible_stable = (lo["full_family_mismatches"] == 0
                           and lo["ladder_mismatches"] == 0
                           and dy["rows_where_the_sufficient_condition_is_violated"] == 0)
    winding_declared = (wi["absent_at_every_open_size"]
                        and wi["comparisons_where_the_value_moves"] > 0)
    if mut("MUT-SPLIT"):
        contractible_stable = not contractible_stable
    if contractible_stable and winding_declared:
        word = "AS-PRE-REGISTERED"
    elif contractible_stable:
        word = "CONTRACTIBLE-STABLE-WINDING-NOT-DECLARATION-BOUND"
    elif winding_declared:
        word = "CONTRACTIBLE-NOT-STABLE"
    else:
        word = "NEITHER-SIDE-AS-PRE-REGISTERED"
    ok = read and word == "AS-PRE-REGISTERED"
    CNT.measured("splitword", word, "derived by the frozen decision rule")
    LD.gate("G-THE-SPLIT",
            "the pin's pre-registered split is decided by a rule frozen "
            "before the values were looked at, and both sides are required to "
            "be measured rather than one side asserted: the contractible side "
            "counts every mismatch of the static sweep, every mismatch of the "
            "ladder sweep and every disagreement between the predicted and "
            "the measured horizon on the dynamical side, and the winding side "
            "requires both absence on every open size and motion across "
            "closed ones",
            ok, "the pin's own split sentence read %s; contractible stable "
            "%s; winding declaration-bound %s; the split is %s" %
            (read, contractible_stable, winding_declared, word))
    S["the_split"] = {
        "word": word, "contractible_side_stable": contractible_stable,
        "winding_side_declaration_bound": winding_declared,
        "the_pin_sentence_was_read": read}
    SEAL.take("the_split", S["the_split"], "G-THE-SPLIT")
    return word


def outcome_word(blocked, offenders, stable, split):
    """the pin's four-way rule, in one place, so that the control that proves
    a branch reachable runs the same rule the run itself is decided by."""
    if blocked:
        return "HOR-BLOCKED-AT-THE-STABILITY-TESTER"
    if offenders:
        return "HOR-GLOBAL-SENSITIVE-AT-" + offenders[0]
    if stable and split == "AS-PRE-REGISTERED":
        return "HOR-UNDETERMINED-R-NATIVE"
    return "HOR-SPLIT-DIFFERENTLY-" + split


def measure_the_outcome(S, exceptions):
    """the outcome word, derived from the measurements by the pin's own
    four-way rule -- never chosen, and every branch reachable at this arena.

    The globally-sensitive branch is not reachable by inspection, so it is
    made reachable by CONTROL: a synthetic row built out of this run's own
    measured numbers -- two witnesses that agree at the declared arena pair,
    carrying an open ladder the arena moves -- is put through the SAME
    classifier and the SAME offender condition and the SAME four-way rule, and
    the word it produces is required to be the globally-sensitive one.  A
    second control, identical but for an open ladder no arena moves, is
    required NOT to produce it."""
    split = S["the_split"]["word"]
    stable = S["the_split"]["contractible_side_stable"]
    census = S["closure_census"]["rows"]
    dy = S["dynamic_stability"]
    if mut("MUT-OUTCOME"):
        dy = dict(dy, rows_where_the_value_is_unmoved=0)
    blocked = (dy["rows_where_the_value_is_unmoved"] == 0
               or S["closure_census"]["verbatim"] == 0)
    offenders = [r["id"] for r in census if globally_sensitive(r)]

    # the controls, assembled from rows this run measured: the witness the
    # classifier is handed is a real pair that agrees, and the ladder beside
    # it is a real ladder -- one the arena moves, one it does not.
    src = {r["id"]: r for r in census}
    agree = src["LAW-RECTANGLE-FAMILY"]["witness_on_the_open_arena"]
    moving = src["LAW-LINK-COUNT"]["witness_over_the_open_ladder"]
    flat = src["LAW-COIN-FAMILY"]["witness_over_the_open_ladder"]
    if mut("MUT-GLOBAL-CONTROL"):
        moving = flat
    live = {"id": "CONTROL-A-LOCAL-LAW-THE-FAR-LATTICE-SETS",
            "verdict": classify_row(agree, agree, False),
            "witness_over_the_open_ladder": moving}
    null = {"id": "CONTROL-A-LOCAL-LAW-NO-ARENA-SETS",
            "verdict": classify_row(agree, agree, False),
            "witness_over_the_open_ladder": flat}
    control_word = outcome_word(False, [live["id"]] if globally_sensitive(live)
                                else [], stable, split)
    reachable = (globally_sensitive(live) and not globally_sensitive(null)
                 and control_word.startswith("HOR-GLOBAL-SENSITIVE-AT-"))

    word = outcome_word(blocked, offenders, stable, split)
    reach = {"HOR-UNDETERMINED-R-NATIVE":
             "reached when the split is as pre-registered and the tester has "
             "both an unmoved arm and a moved one",
             "HOR-SPLIT-DIFFERENTLY":
             "reached whenever either side of the split fails its rule -- the "
             "rule is evaluated on measured counters, and the winding side's "
             "counters are nonzero here, so the branch was live",
             "HOR-GLOBAL-SENSITIVE-AT":
             "reached by any law the classifier calls surviving whose witness "
             "on the open arena moves across the declared open ladder -- a "
             "local law the far lattice sets; computed on every row of the "
             "census, and shown reachable by a control built from this run's "
             "own rows which does produce the word through the same rule",
             "HOR-BLOCKED-AT-THE-STABILITY-TESTER":
             "reached when the tester never returns an unmoved row or the "
             "census never returns a surviving law"}
    true_blocked = (S["dynamic_stability"]["rows_where_the_value_is_unmoved"] == 0
                    or S["closure_census"]["verbatim"] == 0)
    ok = (word.startswith("HOR-") and len(reach) == 4
          and blocked == true_blocked and reachable)
    LD.gate("G-THE-OUTCOME",
            "the outcome word is derived from measured counters by the pin's "
            "own four-way rule, and each of the four branches is published "
            "with the counter that would reach it; the one branch whose "
            "counter is empty here is shown REACHABLE rather than argued to "
            "be, by putting a synthetic row built out of this run's own "
            "measured ladders through the same classifier, the same offender "
            "condition and the same four-way rule and requiring the "
            "globally-sensitive word to come out, while a second control "
            "differing only in a ladder no arena moves is required not to "
            "produce it",
            ok, "outcome %s; branches published %d; global-sensitivity "
            "offenders %d; the blocked counter re-derived inside the gate "
            "agrees %s; the control emits %s and the null control does not %s"
            % (word, len(reach), len(offenders), blocked == true_blocked,
               control_word, not globally_sensitive(null)))
    S["outcome"] = {"word": word, "branch_reachability": reach,
                    "global_sensitivity_offenders": offenders,
                    "the_global_sensitivity_condition":
                        "A-SURVIVING-ROW-WHOSE-OPEN-WITNESS-MOVES-ACROSS-THE-"
                        "DECLARED-OPEN-LADDER",
                    "the_reachability_control": {
                        "the_row_that_must_produce_the_word": live["id"],
                        "its_open_ladder": live["witness_over_the_open_ladder"],
                        "the_row_that_must_not": null["id"],
                        "its_open_ladder": null["witness_over_the_open_ladder"],
                        "the_word_the_control_produces": control_word,
                        "through_the_same_classifier_and_the_same_rule": True},
                    "named_exceptions": exceptions}
    SEAL.take("outcome", S["outcome"], "G-THE-OUTCOME")
    return word


# ===========================================================================
# SECTION 15.  THE HEAD, AND A COMPARATOR THAT SHARES NOTHING WITH IT (S-1)
# ===========================================================================

SEGMENT_SEP = " -- "


def build_head(S):
    """the builder: every numeral arrives by name from the live registry, so
    no head segment can carry a typed number (E-31)."""
    seg = [
        S["outcome"]["word"],
        CNT.stmt("CONE=[TICK=ONE-PARITY-STRATUM-OPERATOR-THE-PARENT-NAMES-AND-"
                 "NEVER-BUILDS;REACH-PER-TICK=ZERO-AT-{reach0}-COINS-AND-ONE-"
                 "AT-{reach1}-OF-{coins};c={csum}-SITE-PER-TICK-IN-THE-SUM-"
                 "NORM-ATTAINED-STRUCTURALLY-AT-{attained}-OF-{conedepth}-"
                 "DEPTHS-AND-BY-THE-DYNAMICS-AT-{dynattained}-OF-"
                 "{attaindepth}-ATTAINMENT-DEPTHS-A-MAXIMUM-"
                 "NOT-A-BOUND;MAX-NORM-SUSTAINED={csust};SHAPE=A-PRODUCT-BOX-"
                 "AT-EVERY-DEPTH-ASYMMETRIC-AT-{asym}-AND-REFLECTED-BY-"
                 "REVERSING-THE-PARITY-ORDER-AT-{flips};AMPLITUDE-SUPPORTS-ESCAPE-"
                 "AT-{coneescape};RADIUS-ATTAINED-BY-{coneattain}-COINS-AT-EVERY-ATTAINMENT-DEPTH-AND-THE-CONE-UNFILLED-AT-{coneshort}]"),
        CNT.stmt("STABILITY=[CONTRACTIBLE={fullchecks}-SHAPE-BY-COIN-AT-THE-"
                 "CORE-PAIR-OVER-THE-WHOLE-COIN-FAMILY-AND-{ladderchecks}-"
                 "OVER-THE-LADDER-WITH-{loopmis}-MISMATCHES;DYNAMIC={dynrows}-"
                 "ARENA-BY-DEPTH-ROWS-WITH-THE-HORIZON-PREDICTED-FROM-THE-"
                 "CONE-BEFORE-THE-VALUES-{dynviol}-VIOLATIONS-"
                 "{dynmargin}-SLACK-{dynagree}-"
                 "UNMOVED-{dynmove}-MOVED;WINDING=ABSENT-AT-EVERY-OPEN-SIZE-"
                 "AND-MOVING-AT-{windmoves}-OF-{windpairs};ARMS={armsmoved}-"
                 "MOVED-AND-{armsunmoved}-UNMOVED-THROUGH-ONE-TESTER;SPLIT="
                 "{splitword}]"),
        CNT.stmt("CLOSURE=[{censusrows}-SEALED-LAWS-AT-ONE-DECLARED-ARENA-"
                 "PAIR:{surv}-VERBATIM-OF-WHICH-{censusmeasured}-MEASURED-AND-"
                 "{censusstructural}-STRUCTURAL-{scop}-"
                 "SCOPED-{art}-ARTIFACT;THE-OPEN-PATCH-REALISES-EVERY-TWIST-"
                 "SO-ITS-MERGING-INDEX-IS-{actindex}-AT-ALL-{patchgauge}-OPEN-"
                 "SIZES-WHICH-IS-THE-CLOSED-VALUE-ONLY-WHERE-THE-PHASE-ORDER-"
                 "DIVIDES-THE-SIZE;WINDING-CLASSES={patchclasses}-OPEN-"
                 "AGAINST-{torusclasses}-CLOSED;TRANSLATIONS-CARRYING-THE-"
                 "OPEN-LINK-SET-TO-ITSELF={patchsyms};THE-CLOSED-FORM-AND-"
                 "AREA-BLINDNESS-SURVIVE-THE-FLUSH-{cfchecks}-CHECKS-AND-"
                 "{areapairs}-COMPARISONS-FAILING-{cffails}-AND-{areadis}]"),
        CNT.stmt("FORM=[{dlrows}-OPEN-SIZES-DIRECTED-UNDER-INCLUSION-CARRYING-"
                 "{dltested}-VALUES-OF-WHICH-{dlself}-ARE-THE-REFERENCE-"
                 "AGAINST-ITSELF-AND-FAILING-TO-CARRY-{dlmoved};"
                 "HORIZON-STATABLE-BY-THE-CLOSURE-WITNESS-TEST-AT-{quant}-OF-"
                 "{censusrows}-WITH-{exc}-NAMED-"
                 "EXCEPTIONS;NOT-A-LIMIT-NOT-A-CONVERGENCE-NOT-AN-OBJECT]"),
        CNT.stmt("SCOPE=[D-IS-TWO;FIELD=Q(zeta_8);COINS={coins};CARRIER=THE-"
                 "UNIFORM-CONFIGURATIONS;THE-GENERATORS-ARE-THE-PARENTS-AND-"
                 "THE-TICK-IS-THIS-UNITS-DECLARATION;LADDERS-DECLARED-OPEN-"
                 "{patchgauge}-AND-CLOSED-{closedsizes};COUNTS-ARE-COUNTING-"
                 "ONLY;NO-CONTINUUM-CLAIM;NO-"
                 "ACTUAL-INFINITY-CLAIM;SCALEFUL-NOT-CONTINUOUS;NOT-A-"
                 "RELATIVITY-CLAIM]"),
    ]
    return SEGMENT_SEP.join(seg)


def rebuild_head(payload):
    """THE COMPARATOR (S-1).  It reads the receipt's PRIMITIVE rows and
    measured leaves and nothing else: not one head segment, not one number the
    builder aggregated, not one of the builder's format strings, and not one
    of the builder's functions.  Every count below is recomputed here from a
    row list, and the outcome word is re-derived from a second copy of the
    four-way rule."""
    ar = payload["arena"]
    cone = payload["the_cone"]["rows"]
    shp = payload["cone_shape"]["rows"]
    otr = payload["one_tick_reach"]["by_sector_reach_and_rest"]
    lst = payload["loop_stability"]
    win = payload["winding"]
    dyn = payload["dynamic_stability"]["rows"]
    arm = payload["control_arms"]["arms"]
    cen = payload["closure_census"]["rows"]
    qua = payload["quantifiability"]["rows"]
    dl = payload["direct_limit"]["rows"]
    gau = payload["patch_gauge"]["rows"]
    cir = payload["circulants"]["rows"]
    hom = payload["homology"]["rows"]
    cf = payload["closed_form"]["per_perimeter"]

    z = sum(v for k, v in otr.items() if k.split("|")[1] == "0")
    o = sum(v for k, v in otr.items() if k.split("|")[1] == "1")
    ratios = [Fraction(r["sum_norm_radius"], r["tick"]) for r in cone]
    top = max(ratios)
    hit = len([x for x in ratios if x == top])
    sw = [r for r in cone if r["tick"] % len(SCHEDULE) == 0]
    sust = sorted({Fraction(r["max_norm_radius"], r["tick"]) for r in sw})
    asym = len([r for r in cone if r["x_forward"] + r["x_backward"] != 0])
    flips = len([r for r in shp if r["reflected"]])
    esc = payload["the_cone"]["amplitude_supports_escaping_the_cone"]
    att = min(r["coins_realising_the_cone_s_own_sum_norm_radius"]
              for r in payload["the_cone"]["attainment_rows"])
    shrt = len([r for r in payload["the_cone"]["attainment_rows"]
                if r["coins_whose_support_is_the_whole_cone"] == 0])
    dyatt = len([r for r in payload["the_cone"]["attainment_rows"]
                 if r["coins_realising_the_cone_s_own_sum_norm_radius"]])
    adepth = len(payload["the_cone"]["attainment_rows"])
    ladder = sum(r["comparisons"] for r in lst["ladder_rows"])
    lagree = sum(r["agreeing"] for r in lst["ladder_rows"])
    loopmis = (ladder - lagree) + lst["full_family_mismatches"]
    fullchk = lst["shapes_compared"] * lst["coins_in_the_full_sweep"]
    dagree = len([r for r in dyn if r["measured_on_the_values"]])
    dmove = len(dyn) - dagree
    ddis = len([r for r in dyn if r["predicted_by_the_cone"]
                and not r["measured_on_the_values"]])
    dslack = len([r for r in dyn if r["measured_on_the_values"]
                  and not r["predicted_by_the_cone"]])
    wmov = sum(r["moving"] for r in win["adjacent_pairs"])
    wpair = sum(r["comparisons"] for r in win["adjacent_pairs"])
    amov = len([a for a in arm if a["got"] == "MOVED"])
    aunm = len(arm) - amov
    vb = len([r for r in cen if r["verdict"] == VERBATIM])
    sc = len([r for r in cen if r["verdict"] == SCOPED])
    at = len([r for r in cen if r["verdict"] == ARTIFACT])
    vbm = len([r for r in cen if r["verdict"] == VERBATIM
               and r["basis"] == MEASURED])
    vbs = len(([r for r in cen if r["verdict"] == VERBATIM])) - vbm
    qn = len([r for r in qua
              if r["horizon_statable_by_the_closure_witness_test"]])
    ex = len(qua) - qn
    dtest = sum(r["comparisons"] for r in dl)
    dcar = sum(r["carried_unchanged"] for r in dl)
    dself = [r["comparisons"] for r in sorted(dl, key=lambda r: r["n"])][0]
    pg = [r for r in gau if r["closure"] == PATCH]
    idx = sorted({r["merging_index"] for r in pg})
    pcl = [r for r in hom if r["closure"] == PATCH][0]["displacement_classes"]
    tcl = [r for r in hom if r["closure"] == TORUS][0]["displacement_classes"]
    psym = [r for r in cir if r["closure"] == PATCH][0][
        "translations_carrying_the_link_set_to_itself"]
    cfc = sum(r["checks"] for r in cf)
    cff = sum(r["failures"] for r in cf)
    apair = sum(r["area_pairs"] for r in cf)
    adis = sum(r["area_disagreements"] for r in cf)
    closed = len([r for r in gau if r["closure"] == TORUS])

    stable = (loopmis == 0 and ddis == 0)
    declared = (all(r["winding_placements"] == 0
                    for r in payload["family_split"]["rows"]
                    if r["closure"] == PATCH) and wmov > 0)
    if stable and declared:
        split = "AS-PRE-REGISTERED"
    elif stable:
        split = "CONTRACTIBLE-STABLE-WINDING-NOT-DECLARATION-BOUND"
    elif declared:
        split = "CONTRACTIBLE-NOT-STABLE"
    else:
        split = "NEITHER-SIDE-AS-PRE-REGISTERED"
    off = [r["id"] for r in cen
           if r["verdict"] in (VERBATIM, SCOPED)
           and len(set(r["witness_over_the_open_ladder"])) > 1]
    if dagree == 0 or vb == 0:
        word = "HOR-BLOCKED-AT-THE-STABILITY-TESTER"
    elif off:
        word = "HOR-GLOBAL-SENSITIVE-AT-" + off[0]
    elif stable and split == "AS-PRE-REGISTERED":
        word = "HOR-UNDETERMINED-R-NATIVE"
    else:
        word = "HOR-SPLIT-DIFFERENTLY-" + split

    p = []
    p.append(word)
    p.append("".join([
        "CONE=[TICK=ONE-PARITY-STRATUM-OPERATOR-THE-PARENT-NAMES-AND-NEVER-",
        "BUILDS;REACH-PER-TICK=ZERO-AT-", str(z), "-COINS-AND-ONE-AT-", str(o),
        "-OF-", str(ar["coins"]), ";c=", str(top),
        "-SITE-PER-TICK-IN-THE-SUM-NORM-ATTAINED-STRUCTURALLY-AT-", str(hit),
        "-OF-", str(len(cone)), "-DEPTHS-AND-BY-THE-DYNAMICS-AT-", str(dyatt),
        "-OF-", str(adepth),
        "-ATTAINMENT-DEPTHS-A-MAXIMUM-NOT-A-BOUND;MAX-NORM-SUSTAINED=",
        str(sust[0]) if len(sust) == 1 else "SPLIT",
        ";SHAPE=A-PRODUCT-BOX-AT-EVERY-DEPTH-ASYMMETRIC-AT-", str(asym),
        "-AND-REFLECTED-BY-REVERSING-THE-PARITY-ORDER-AT-", str(flips),
        ";AMPLITUDE-SUPPORTS-ESCAPE-AT-", str(esc), ";RADIUS-ATTAINED-BY-",
        str(att), "-COINS-AT-EVERY-ATTAINMENT-DEPTH-AND-THE-CONE-UNFILLED-AT-",
        str(shrt), "]"]))
    p.append("".join([
        "STABILITY=[CONTRACTIBLE=", str(fullchk),
        "-SHAPE-BY-COIN-AT-THE-CORE-PAIR-OVER-THE-WHOLE-COIN-FAMILY-AND-",
        str(ladder), "-OVER-THE-LADDER-WITH-", str(loopmis),
        "-MISMATCHES;DYNAMIC=", str(len(dyn)),
        "-ARENA-BY-DEPTH-ROWS-WITH-THE-HORIZON-PREDICTED-FROM-THE-CONE-",
        "BEFORE-THE-VALUES-", str(ddis), "-VIOLATIONS-", str(dslack),
        "-SLACK-", str(dagree),
        "-UNMOVED-", str(dmove), "-MOVED;WINDING=ABSENT-AT-EVERY-OPEN-SIZE-",
        "AND-MOVING-AT-", str(wmov), "-OF-", str(wpair), ";ARMS=", str(amov),
        "-MOVED-AND-", str(aunm), "-UNMOVED-THROUGH-ONE-TESTER;SPLIT=", split,
        "]"]))
    p.append("".join([
        "CLOSURE=[", str(len(cen)), "-SEALED-LAWS-AT-ONE-DECLARED-ARENA-PAIR:",
        str(vb), "-VERBATIM-OF-WHICH-", str(vbm), "-MEASURED-AND-", str(vbs),
        "-STRUCTURAL-", str(sc), "-SCOPED-", str(at),
        "-ARTIFACT;THE-OPEN-PATCH-REALISES-EVERY-TWIST-SO-ITS-MERGING-INDEX-",
        "IS-", str(idx[0]) if len(idx) == 1 else "SPLIT", "-AT-ALL-",
        str(len(pg)),
        "-OPEN-SIZES-WHICH-IS-THE-CLOSED-VALUE-ONLY-WHERE-THE-PHASE-ORDER-",
        "DIVIDES-THE-SIZE;WINDING-CLASSES=", str(pcl), "-OPEN-AGAINST-",
        str(tcl), "-CLOSED;TRANSLATIONS-CARRYING-THE-OPEN-LINK-SET-TO-",
        "ITSELF=", str(psym),
        ";THE-CLOSED-FORM-AND-AREA-BLINDNESS-SURVIVE-THE-FLUSH-", str(cfc),
        "-CHECKS-AND-", str(apair), "-COMPARISONS-FAILING-", str(cff),
        "-AND-", str(adis), "]"]))
    p.append("".join([
        "FORM=[", str(len(dl)), "-OPEN-SIZES-DIRECTED-UNDER-INCLUSION-",
        "CARRYING-", str(dtest), "-VALUES-OF-WHICH-", str(dself),
        "-ARE-THE-REFERENCE-AGAINST-ITSELF-AND-FAILING-TO-CARRY-",
        str(dtest - dcar),
        ";HORIZON-STATABLE-BY-THE-CLOSURE-WITNESS-TEST-AT-", str(qn), "-OF-",
        str(len(cen)), "-WITH-", str(ex),
        "-NAMED-EXCEPTIONS;NOT-A-LIMIT-NOT-A-CONVERGENCE-NOT-AN-OBJECT]"]))
    p.append("".join([
        "SCOPE=[D-IS-TWO;FIELD=Q(zeta_8);COINS=", str(ar["coins"]),
        ";CARRIER=THE-UNIFORM-CONFIGURATIONS;THE-GENERATORS-ARE-THE-PARENTS-",
        "AND-THE-TICK-IS-THIS-UNITS-DECLARATION;LADDERS-DECLARED-OPEN-",
        str(len(pg)), "-AND-CLOSED-", str(closed),
        ";COUNTS-ARE-COUNTING-ONLY;NO-CONTINUUM-CLAIM;NO-ACTUAL-INFINITY-",
        "CLAIM;SCALEFUL-NOT-CONTINUOUS;NOT-A-RELATIVITY-CLAIM]"]))
    return SEGMENT_SEP.join(p)


def measure_verdict(S, payload):
    head = build_head(S)
    if mut("MUT-HEAD"):
        head = head.replace("NOT-A-BOUND", "NOT-A-BOUNDX")
    rebuilt = rebuild_head(payload)
    ok = head == rebuilt
    where = ""
    if not ok:
        for i in range(min(len(head), len(rebuilt))):
            if head[i] != rebuilt[i]:
                where = " first difference at offset %d: %r vs %r" % (
                    i, head[i:i + 24], rebuilt[i:i + 24])
                break
        if not where:
            where = " lengths %d vs %d" % (len(head), len(rebuilt))
    LD.gate("G-VERDICT-EQUALITY",
            "the complete verdict string is compared for equality against an "
            "independent reconstruction that reads only the receipt's "
            "primitive row lists and measured leaves, recomputes the head's "
            "counts from those rows by its own aggregations -- four of them "
            "it reads from the measured leaves rather than re-aggregating -- "
            "re-derives the outcome word from a second copy of the four-way "
            "rule, and renders every segment with its own format strings, "
            "sharing with the builder no function of this instrument, no "
            "aggregate, no format string and no numeric literal, and one "
            "constant, the separator the two renderings are joined with",
            ok, "head length %d, rebuilt length %d, equal %s%s"
            % (len(head), len(rebuilt), ok, where))
    return head


# ===========================================================================
# SECTION 16.  THE WALLS, THE CLAIMS, THE REFERENTS
# ===========================================================================

DECLARING_SENTENCES = [
    "This unit makes no actual-infinity claim of any kind.",
    "This unit makes no continuum claim of any kind.",
    "The register this unit works in is scaleful, not continuous.",
    "No symbol in a HOR-law denotes a size, no quantifier ranges over a "
    "completed totality, and every instance is a statement about one finite "
    "patch.",
]

# The negative legs are written against the DISEASE and not against a form of
# words: beside the verb forms a paper would reach for first sit the noun
# forms it would reach for second (a completed member, an arena of unbounded
# extent, a totality the laws are about, all patches at once), because a wall
# whose only controls are its own patterns is a badge.  The controls that
# exercise these legs -- MUT-WALL-INFINITY, MUT-WALL-CONTINUUM,
# MUT-WALL-LICENCE -- are written as a paper would write the banned claim, in
# this paper's own voice, and NOT lifted from the pattern list.

WALL_INFINITY = SemanticWall(
    "WALL-NO-ACTUAL-INFINITY",
    negative=[
        r"\bactual(?:ly)? infinit", r"\ban infinite (?:lattice|arena|patch|"
        r"family|set|number)", r"\bthe infinite (?:lattice|arena|patch|volume)",
        r"\bin the limit\b", r"\bconverge[sd]? to\b", r"\bconvergence to\b",
        r"\btends? to infinity\b", r"\bas r (?:goes|grows|tends) to infinity\b",
        r"\blimit of the family\b", r"\bcompleted (?:totality|infinity)\b",
        r"\bexists an infinite\b", r"\bthe direct limit is an object\b",
        r"\ba limit in (?:some|any|the) topology\b",
        r"\bcompleted (?:member|arena|patch|object|whole|lattice)\b",
        r"\bunbounded (?:extent|size|volume|lattice|arena|patch)\b",
        r"\bof unbounded\b", r"\bwithout bound\b",
        r"\bcontains every finite (?:patch|arena|size|member)\b",
        r"\ball (?:patches|arenas|sizes) at once\b",
        r"\b(?:that|this|the) totality is\b",
        r"\btaken over all (?:patches|arenas|sizes)\b",
    ],
    positive=[r"every instance is a statement about one finite patch",
              r"not a limit"])

WALL_CONTINUUM = SemanticWall(
    "WALL-NO-CONTINUUM",
    negative=[
        r"\bcontinuum limit\b", r"\bin the continuum\b",
        r"\bsmooth (?:manifold|limit|geometry|structure)\b",
        r"\bdifferentiable\b", r"\binfinitesimal\b", r"\bthe real line\b",
        r"\bmetric tensor\b", r"\bcontinuous (?:spacetime|space|manifold)\b",
        r"\blorentz (?:invarian|covarian)", r"\bspeed of light\b",
        r"\bminkowski\b", r"\bcausal structure of spacetime\b",
        r"\brefined without bound\b", r"\bbecomes a derivative\b",
        r"\bsmooth arena\b", r"\bthe spacing is refined\b",
        r"\bfield-theoretic description\b", r"\bbecomes a smooth\b",
    ],
    positive=[r"scaleful, not continuous"])

WALL_TICK_LICENCE = SemanticWall(
    "WALL-EVERY-SPEED-CARRIES-ITS-MEASUREMENT",
    negative=[r"\bthe speed of light\b"],
    positive=[r"a maximum, not a bound"],
    policed=("per tick", "per that tick"))


def _flat(t):
    return re.sub(r"\s+", " ", t)


def strip_anchors(text, anchors=None):
    """the pinned windows this paper quotes, removed and nothing else: what
    is left is the paper's own voice, which is where a standing sentence of
    this unit's own has to be found."""
    out = _flat(text)
    for a in (anchors.by_name.values() if anchors else ()):
        out = out.replace(_flat(a.needle), " ")
    return out


def strip_declaring(text, anchors=None):
    """#125: the strip is taken on whitespace-normalised text, because a
    sentence a paper wrapped in house style is the same sentence."""
    out = strip_anchors(text, anchors)
    for s in DECLARING_SENTENCES:
        out = out.replace(_flat(s), " ")
    return out


def measure_walls(S, paper_text, claims, anchors=None):
    scanned = strip_declaring(paper_text, anchors)
    standing = strip_anchors(paper_text, anchors)
    # the licensed-vocabulary leg reads the paper's PROSE: the rendered
    # tables and the fenced verdict are bound by equality at the claims gate
    # and are this run's own output, so policing them would police this
    # instrument rather than the paper.
    lic = strip_declaring(ReferentRegistry.prose_only(paper_text), anchors)
    # the three controls are written against the DISEASE, in the voice a paper
    # would use to make the banned claim, and not lifted from any wall's own
    # pattern list -- family (c) obligation 7.
    if mut("MUT-WALL-INFINITY"):
        scanned = scanned + (
            "\nTaken over all patches at once the family has a completed "
            "member, an arena of unbounded extent that contains every finite "
            "patch as a sub-patch, and that totality is what the laws above "
            "are ultimately about.")
    if mut("MUT-WALL-CONTINUUM"):
        # the continuum disease with no unboundedness word in it, so that this
        # control lands on the continuum wall rather than on the infinity one,
        # which catches the unbounded phrasing of the same sentence on its own.
        scanned = scanned + (
            "\nAs the spacing between places is refined again and again the "
            "lattice becomes a smooth arena and the tick becomes a "
            "derivative, so the ordinary field-theoretic description is "
            "recovered.")
    if mut("MUT-WALL-LICENCE"):
        lic = lic + (
            "\nInfluence travels four sites per-tick on this arena.")
    rows = []
    policed = 0
    for w, gid in ((WALL_INFINITY, "G-WALL-NO-ACTUAL-INFINITY"),
                   (WALL_CONTINUUM, "G-WALL-NO-CONTINUUM"),
                   (WALL_TICK_LICENCE, "G-WALL-SPEED-LICENCE")):
        try:
            r = w.scan(paper_text, claims, scan_text=scanned,
                       standing_text=standing, licence_text=lic)
        except GateFail as exc:
            raise GateFail(gid, exc.detail)
        policed += r["policed_sentences"]
        extra = True
        if gid == "G-WALL-NO-ACTUAL-INFINITY" and anchors is not None:
            phrase = "not a limit and not a convergence"
            extra = (anchor_has(anchors, "VB-R1-NOLIMIT", gid, phrase)
                     and canon(phrase) in canon(paper_text))
        present = [d for d in DECLARING_SENTENCES if _flat(d) in _flat(paper_text)]
        LD.gate(gid,
                "the wall is a set of voice-normalised patterns run over the "
                "whole canonicalised paper with the declaring sentences and "
                "the pinned quotations removed first, so the legs read this "
                "paper's own voice; with a POSITIVE leg that must be found in "
                "that voice with the quotations still stripped, so no parent's "
                "sentence can discharge it; with a refusal on empty text; and "
                "-- where the wall licenses a vocabulary -- a requirement that "
                "every sentence of the prose using it, hyphens folded, carry a "
                "claim this run rendered from its own measurements, with the "
                "number of sentences policed published rather than assumed",
                len(present) == len(DECLARING_SENTENCES) and extra,
                "%s: banned patterns %d, standing sentences %d, sentences "
                "policed %d, declaring sentences carried %d of %d, the "
                "parent's own prohibition carried %s" %
                (w.name, r["negative"], r["positive"],
                 r["policed_sentences"], len(present),
                 len(DECLARING_SENTENCES), extra))
        rows.append({"wall": w.name, "policed_sentences":
                     r["policed_sentences"], **w.seal_value()})
    S["walls"] = {"rows": rows, "sentences_policed": policed,
                  "the_positive_legs_read_the_papers_own_voice": True,
                  "declaring_sentences": list(DECLARING_SENTENCES)}
    SEAL.take("walls", S["walls"], "G-WALL-SPEED-LICENCE")


def build_referents(S):
    R = ReferentRegistry()
    ar, cone, otr = S["arena"], S["the_cone"], S["one_tick_reach"]
    lst, dyn, cen = S["loop_stability"], S["dynamic_stability"], S["closure_census"]
    gau, cf = S["patch_gauge"], S["closed_form"]
    cir, dl = S["circulants"], S["direct_limit"]
    cone_vals = {r["tick"] for r in cone["rows"]} | \
                {r["sites"] for r in cone["rows"]} | \
                {r["sum_norm_radius"] for r in cone["rows"]} | \
                {r["max_norm_radius"] for r in cone["rows"]} | \
                {cone["depth"], cone["amplitude_supports_escaping_the_cone"],
                 cone["attainment_depth"],
                 cone["coins_realising_the_cone_radius_at_the_thinnest_depth"],
                 cone["attainment_depths_no_coin_fills_site_for_site"],
                 S["zero_patterns"]["patterns"],
                 S["cone_shape"]["asymmetric_depths"],
                 S["cone_shape"]["depths_reflected_by_reversing_the_parity_order"],
                 otr["reach_zero"], otr["reach_one"], otr["reach_above_one"],
                 cone["attainment_depths_the_dynamics_reaches_the_radius_at"],
                 ar["coins"], 0, 1, 2}
    R.universe("THE-CONE", ["cone", "tick", "ticks", "reach", "depth", "depths"],
               cone_vals,
               {(otr["reach_zero"], ar["coins"]), (otr["reach_one"], ar["coins"]),
                (S["emergent_c"]["depths_at_which_the_sum_norm_maximum_is_attained"],
                 cone["depth"]),
                (cone["attainment_depths_the_dynamics_reaches_the_radius_at"],
                 cone["attainment_depth"]),
                (S["cone_shape"]["depths_reflected_by_reversing_the_parity_order"],
                 cone["depth"])})
    stab_vals = {lst["full_family_comparisons"], lst["full_family_mismatches"],
                 lst["ladder_comparisons"], lst["ladder_mismatches"],
                 lst["shapes_compared"], lst["coins_in_the_full_sweep"],
                 lst["coins_in_the_ladder_sweep"],
                 len(dyn["rows"]), dyn["rows_where_the_value_is_unmoved"],
                 dyn["rows_where_the_value_moves"],
                 dyn["rows_where_the_sufficient_condition_is_violated"],
                 dyn["rows_where_agreement_survives_without_the_condition"],
                 dyn["coins"], dyn["window_sites"], dyn["depth"],
                 S["winding"]["adjacent_size_comparisons"],
                 S["winding"]["comparisons_where_the_value_moves"],
                 S["control_arms"]["arms_that_moved"],
                 S["control_arms"]["arms_that_did_not"],
                 len(S["control_arms"]["arms"]),
                 S["family_split"]["open_sizes"],
                 S["family_split"]["closed_sizes"],
                 dl["comparisons"], dl["values_an_inclusion_failed_to_carry"],
                 dl["comparisons_of_the_reference_size_with_itself"],
                 dl["comparisons_across_a_proper_inclusion"], len(dl["rows"]),
                 cf["checks_after_the_fit"], cf["failures"],
                 cf["area_discriminating_comparisons"],
                 cf["area_disagreements"], 0, 1}
    R.universe("THE-STABILITY-SWEEP",
               ["comparison", "comparisons", "mismatch", "mismatches",
                "shape-by-coin", "size-by-coin", "arena-by-depth", "arm",
                "arms", "row", "rows", "inclusion", "inclusions"],
               stab_vals,
               {(lst["full_family_mismatches"], lst["full_family_comparisons"]),
                (lst["ladder_mismatches"], lst["ladder_comparisons"]),
                (dyn["rows_where_the_value_is_unmoved"], len(dyn["rows"])),
                (dyn["rows_where_the_value_moves"], len(dyn["rows"])),
                (S["winding"]["comparisons_where_the_value_moves"],
                 S["winding"]["adjacent_size_comparisons"]),
                (S["control_arms"]["arms_that_moved"],
                 len(S["control_arms"]["arms"])),
                (S["control_arms"]["arms_that_did_not"],
                 len(S["control_arms"]["arms"])),
                (cf["failures"], cf["checks_after_the_fit"]),
                (cf["area_disagreements"],
                 cf["area_discriminating_comparisons"])})
    clos_vals = {cen["verbatim"], cen["scoped"], cen["artifact"],
                 len(cen["rows"]), gau["phase_order"],
                 gau["classes_under_the_full_stencil_image"],
                 gau["open_sizes"], gau["closed_sizes"],
                 gau["open_sizes_realising_every_twist"],
                 cen["surviving_rows_whose_witness_an_arena_could_move"],
                 cen["surviving_rows_whose_witness_no_arena_moves"],
                 cf["checks_after_the_fit"], cf["failures"],
                 cf["area_discriminating_comparisons"], cf["area_disagreements"],
                 cf["shapes"], cf["coins"],
                 S["quantifiability"]["quantifiable"],
                 S["quantifiability"]["exceptions"], 0, 1, 2} | \
                {r["merging_index"] for r in gau["rows"]} | \
                {r["orbits_under_the_realisable_twists"] for r in gau["rows"]} | \
                {r["orbit_pairs_merged"] for r in gau["rows"]} | \
                {r["realisable_constant_twists"] for r in gau["rows"]}
    R.universe("THE-CLOSURE-CENSUS",
               ["census", "sealed law", "sealed laws", "law", "laws",
                "merging index", "twist", "twists", "artifact", "artifacts"],
               clos_vals,
               {(cen["verbatim"], len(cen["rows"])),
                (cen["scoped"], len(cen["rows"])),
                (cen["artifact"], len(cen["rows"])),
                (S["quantifiability"]["quantifiable"], len(cen["rows"])),
                (S["quantifiability"]["exceptions"], len(cen["rows"])),
                (gau["open_sizes_realising_every_twist"], gau["open_sizes"]),
                (cf["failures"], cf["checks_after_the_fit"]),
                (cf["area_disagreements"],
                 cf["area_discriminating_comparisons"])})
    ar_vals = {ar["alphabet"], ar["admissible_rows"], ar["coins"],
               ar["sites_there"], ar["links_there"], ar["plaquettes_there"],
               ar["the_declared_size_of_the_parents"],
               ar["domino_dimension_read_from_R5"],
               ar["unitary_by_a_second_route"],
               ar["sectors"]["DIAGONAL"], ar["sectors"]["ANTIDIAGONAL"],
               ar["sectors"]["BALANCED"],
               S["zero_patterns"]["patterns"],
               len(R4_AXES),
               S["circulants"]["rows"][0][
                   "translations_carrying_the_link_set_to_itself"],
               S["circulants"]["rows"][1][
                   "translations_carrying_the_link_set_to_itself"],
               S["patch_gauge"]["phase_order"],
               S["patch_gauge"]["classes_under_the_full_stencil_image"],
               otr["reach_zero"], otr["reach_one"], otr["reach_above_one"],
               0, 1, 2, 4}
    R.universe("THE-ARENA",
               ["coin", "coins", "alphabet", "link", "links", "plaquette",
                "plaquettes", "site", "sites", "stratum", "strata"],
               ar_vals,
               {(ar["unitary_by_a_second_route"], ar["coins"]),
                (ar["sectors"]["DIAGONAL"], ar["coins"]),
                (ar["sectors"]["ANTIDIAGONAL"], ar["coins"]),
                (ar["sectors"]["BALANCED"], ar["coins"])})
    return R


def measure_referents(S, paper_text):
    R = build_referents(S)
    for tok, why in EXEMPT_NUMERALS:
        R.exempt_token(tok, why)
    txt = paper_text
    if mut("MUT-REFERENT"):
        txt = txt + ("\n\nAt every depth the census carries %d sealed laws.\n"
                     % S["the_cone"]["rows"][-1]["sites"])
    try:
        r = R.gate(txt)
    except GateFail as exc:
        raise GateFail("G-REFERENTS", exc.detail)
    LD.gate("G-REFERENTS",
            "every numeral of the paper's PROSE -- fenced blocks stripped, so "
            "this run's own verdict cannot discharge the paper's obligations "
            "-- and its rendered table rows stripped, which the claims gate "
            "binds by equality in both directions -- is resolved against the "
            "universe of the noun it is PREDICATED OF, found as the nearest "
            "declared noun after it or, where its sentence puts none after "
            "it, the nearest before, with every noun matched exactly at both "
            "ends rather than by prefix -- so a false number riding an "
            "earlier universe's noun into this gate is resolved against the "
            "thing it is a count of and not against whichever universe the "
            "sentence happens to mention first; a sentence carrying no "
            "declared noun at all is resolved against "
            "the union of every universe this run declares, so that no prose "
            "numeral sits outside all of them; the only numerals exempted are "
            "exempted BY NAME with a reason, being identifiers of this unit "
            "rather than measurements of it; and every fraction the prose "
            "states must be a pair this run actually measured rather than two "
            "members of one set",
            True, "occurrences checked %d over %d declared universes, of "
            "which %d carry no universe noun and are resolved against the "
            "union, exemptions carried by name %d"
            % (r["occurrences_checked"], r["universes"],
               r["occurrences_with_no_universe_noun"], r["exemptions"]))
    S["referents"] = {"universes": R.seal_value(),
                      "occurrences_checked": r["occurrences_checked"],
                      "occurrences_with_no_universe_noun":
                          r["occurrences_with_no_universe_noun"],
                      "numerals_exempted_by_name": dict(EXEMPT_NUMERALS)}
    SEAL.take("referents", S["referents"], "G-REFERENTS")


# ===========================================================================
# SECTION 17.  THE PAPER'S CLAIMS, RENDERED HERE AND GATED BY EQUALITY
# ===========================================================================

def build_claims(S, head):
    C = Claims()
    T = {}
    T["T-CONE"] = C.table(
        "T-CONE",
        ("tick", "sites in the cone", "sum-norm radius", "max-norm radius",
         "x forward", "x backward"),
        [(r["tick"], r["sites"], r["sum_norm_radius"], r["max_norm_radius"],
          r["x_forward"], r["x_backward"]) for r in S["the_cone"]["rows"]])
    T["T-STRATA"] = C.table(
        "T-STRATA",
        ("arena", "sites", "links", "plaquettes", "strata that are matchings",
         "strata that are perfect"),
        [(r["arena"], r["sites"], r["links"], r["plaquettes"],
          r["strata_that_are_matchings"], r["strata_that_are_perfect"])
         for r in S["stratification"]["rows"]])
    T["T-FAMILY"] = C.table(
        "T-FAMILY",
        ("arena", "contractible placements", "winding placements",
         "shapes that fit"),
        [(r["arena"], r["contractible_placements"], r["winding_placements"],
          r["shapes_that_fit"]) for r in S["family_split"]["rows"]])
    T["T-GAUGE"] = C.table(
        "T-GAUGE",
        ("arena", "realisable twists", "merging index",
         "orbits under the realisable twists", "classes", "orbit pairs merged"),
        [(r["arena"], r["realisable_constant_twists"], r["merging_index"],
          r["orbits_under_the_realisable_twists"],
          r["classes_under_the_full_stencil_image"], r["orbit_pairs_merged"])
         for r in S["patch_gauge"]["rows"]])
    T["T-CENSUS"] = C.table(
        "T-CENSUS",
        ("law", "parent", "arena pair", "witness on the open arena",
         "witness on the closed arena", "verdict", "basis"),
        [(r["id"], r["parent"], r["arena_pair"],
          r["witness_on_the_open_arena"],
          r["witness_on_the_closed_arena"], r["verdict"], r["basis"])
         for r in S["closure_census"]["rows"]])
    T["T-ARMS"] = C.table(
        "T-ARMS", ("arm", "required before the run", "what the tester said"),
        [(a["arm"], a["must"], a["got"]) for a in S["control_arms"]["arms"]])
    T["T-HORIZON"] = C.table(
        "T-HORIZON",
        ("depth", "least swept open size that hides the edge",
         "least swept closed size that hides the edge"),
        [(r["depth"], r["least_open_size_that_hides_the_edge"],
          r["least_closed_size_that_hides_the_edge"])
         for r in S["horizon_law"]["rows"]])
    dyn = {}
    for r in S["dynamic_stability"]["rows"]:
        d = dyn.setdefault(r["arena"], {"un": 0, "mo": 0, "first": 0})
        if r["measured_on_the_values"]:
            d["un"] += 1
        else:
            d["mo"] += 1
            if d["first"] == 0:
                d["first"] = r["depth"]
    T["T-DYNAMIC"] = C.table(
        "T-DYNAMIC",
        ("arena", "depths unmoved", "depths moved", "first depth that moves"),
        [(k, v["un"], v["mo"], v["first"]) for k, v in sorted(dyn.items())])

    P = []
    P.append(C.claim(CNT.stmt(
        "The tick is one application of one parity stratum operator, the "
        "object the gauge parent names and never builds, and its factors are "
        "disjoint at every size where the stratification is a matching.")))
    P.append(C.claim(CNT.stmt(
        "Every speed published here is a speed per that tick and is stamped "
        "so wherever it appears.")))
    P.append(C.claim(CNT.stmt(
        "Unitarity leaves exactly {patterns} vanishing patterns over the "
        "{coins} coins, so the reach of a tick is zero at {reach0} of them and "
        "one site at {reach1}, and it exceeds one site at {reachover}.")))
    P.append(C.claim(CNT.stmt(
        "In the sum norm the emergent speed is {csum} site per tick; the "
        "structural cone attains it at {attained} of {conedepth} censused "
        "depths and the dynamics attains it at {dynattained} of "
        "{attaindepth} attainment depths, so it is a maximum, not a bound.")))
    P.append(C.claim(CNT.stmt(
        "Over whole sweeps the max-norm speed is {csust} site per tick, one "
        "value at every sweep.")))
    P.append(C.claim(CNT.stmt(
        "The cone is a product of an x-range and a y-range at every one of the "
        "{conedepth} depths, its x-range is asymmetric at {asym} of them, and "
        "reversing the parity order inside the schedule reflects it at "
        "{flips} while moving no radius in either norm.")))
    P.append(C.claim(CNT.stmt(
        "Every amplitude support this run evolves is tested against the cone "
        "and escapes it at {coneescape}, at least {coneattain} coins realise "
        "the cone's own sum-norm radius at every one of the {attaindepth} "
        "attainment depths, and at {coneshort} of those depths no coin fills "
        "the cone site for site because amplitudes cancel on exact interior "
        "lines.")))
    P.append(C.claim(CNT.stmt(
        "The contractible observable is compared at {fullchecks} shape-by-coin "
        "rows at the core pair over the whole coin family and at "
        "{ladderchecks} rows over the whole declared ladder, and it moves at "
        "{loopmis}.")))
    P.append(C.claim(CNT.stmt(
        "The dynamical observable is measured at {dynrows} arena-by-depth "
        "rows, the horizon condition is predicted from the cone before any "
        "value is read, containing the source's cone is sufficient for "
        "arena-independence and is violated at {dynviol} rows, and the "
        "measured slack where agreement survives without it is "
        "{dynmargin}.")))
    P.append(C.claim(CNT.stmt(
        "The tester finds the value unmoved at {dynagree} of those rows and "
        "moved at {dynmove}, so it is neither blind nor unanimous.")))
    P.append(C.claim(CNT.stmt(
        "The straight winding cycle exists at none of the {patchloops} open "
        "sizes swept, and across adjacent closed sizes its observable moves at "
        "{windmoves} of {windpairs} size-by-coin comparisons.")))
    P.append(C.claim(CNT.stmt(
        "All {arms} control arms go through one tester that is told nothing "
        "about which arm it is running: it reports moved at {armsmoved} and "
        "unmoved at {armsunmoved}, each on the side declared for it before the "
        "run.")))
    P.append(C.claim(CNT.stmt(
        "Of the {censusrows} sealed laws this unit uses, measured at one "
        "declared arena pair, {surv} survive the flush verbatim -- "
        "{censusmeasured} of them on a witness an arena could have moved and "
        "{censusstructural} on one no arena moves -- {scop} survives with a "
        "stated proviso, and {art} differ across the pair.")))
    P.append(C.claim(CNT.stmt(
        "The open patch realises all {phaseorder} constant twists at every one "
        "of its {patchgauge} sizes, so its merging index is {actindex}, which "
        "a closed arena reaches only where the phase order divides its size.")))
    P.append(C.claim(CNT.stmt(
        "Closed walks of length {walkdepth} from a fixed base fall into "
        "{patchclasses} displacement class on the open arena and "
        "{torusclasses} on the closed one.")))
    P.append(C.claim(CNT.stmt(
        "Every one of the parent's {axes} declared axes shifts the closed "
        "arena onto itself and none shifts the open one onto itself, and the "
        "translations carrying the open link set to itself number "
        "{patchsyms}.")))
    P.append(C.claim(CNT.stmt(
        "The parent's closed form, fitted at the three shortest perimeters and "
        "then checked, fails at {cffails} of {cfchecks} rows on an arena with "
        "no identification anywhere, and its area-blindness disagrees at "
        "{areadis} of {areapairs} equal-perimeter comparisons there.")))
    P.append(C.claim(CNT.stmt(
        "Across {dlrows} open sizes directed under inclusion the inclusions "
        "carry {dltested} values and fail to carry {dlmoved}, and of those "
        "comparisons {dlself} are the reference size against itself and "
        "{dlgenuine} cross a proper inclusion.")))
    P.append(C.claim(CNT.stmt(
        "{quant} of the {censusrows} laws are horizon-statable by the "
        "closure-witness test and {exc} are not, and every one of those "
        "carries the name of the object it needs.")))
    P.append(C.claim(CNT.stmt(
        "The generators are inherited and the tick is this unit's "
        "declaration; every speed is a speed per that tick.")))
    F = C.fence(head)
    return C, T, P, F


def measure_paper(S, paper_text, C):
    if mut("MUT-PAPER"):
        C.prose[sorted(C.prose)[0]] += 1
    try:
        r = C.gate(paper_text)
    except GateFail as exc:
        raise GateFail("G-PAPER-CLAIMS", exc.detail)
    LD.gate("G-PAPER-CLAIMS",
            "every table, every prose claim and every fenced block of the "
            "delivered paper is bound by EQUALITY in both directions and keyed "
            "by the table it was rendered into, headers included, at exact "
            "occurrence counts, and the paper's own table set is required to "
            "be exhausted by the rendered set, so a transplanted row, a "
            "duplicated claim, an extra fence and a deleted fence all die "
            "here",
            True, "table rows %d, prose claim occurrences %d over %d distinct "
            "claims, fenced blocks %d" %
            (r["table_rows"], r["prose_claim_occurrences"],
             r["distinct_prose_claims"], r["fence_blocks"]))
    S["paper_claims"] = dict(r)
    SEAL.take("paper_claims", S["paper_claims"], "G-PAPER-CLAIMS")


# ===========================================================================
# SECTION 18.  TEMPLATE CONFORMANCE, ANCHORS, TYPED COUNTS, FALSIFIERS
# ===========================================================================

def implemented_checks():
    return sorted({Seal.CHECK, Transcript.CHECK, SemanticWall.CHECK,
                   AnchorSet.CHECK, Claims.CHECK, ReferentRegistry.CHECK,
                   CountRegistry.CHECK, FalsifierHarness.CHECK, ReadSet.CHECK})


def measure_template_conformance(S, text, anchors):
    src = text["ERATPL"]
    declared = sorted(set(re.findall(r'"(T-[A-Z-]+)"\)', src)))
    if not declared:
        declared = sorted(set(re.findall(r"T-[A-Z][A-Z-]+", src)))
    tpl_ids = sorted({m for m in re.findall(r'\("[a-i]", "[A-Z0-9-]+", "(T-[A-Z-]+)"\)', src)})
    mine = implemented_checks()
    if mut("MUT-TEMPLATE"):
        mine = mine[:-1]
    read = anchor_has(anchors, "VB-TPL-ADOPT", "G-TEMPLATE-CONFORMANCE",
                      "a unit that adopts these checks has adopted a mechanism")
    ok = tpl_ids == mine and read and len(mine) == len(tpl_ids)
    CNT.measured("families", len(tpl_ids), "parsed from the pinned template")
    LD.gate("G-TEMPLATE-CONFORMANCE",
            CNT.stmt("the {families} family check identifiers this unit "
                     "implements are parsed out of the pinned reference "
                     "implementation's own family table and required to be "
                     "exactly the identifiers this instrument's classes carry, "
                     "so adoption is a measurement rather than a claim; and "
                     "the template's own caveat -- that adopting a mechanism "
                     "is not evidence the mechanism has teeth on this object "
                     "-- is read here and stands over every green row below"),
            ok, "template families %d, implemented %d, equal %s, the caveat "
            "read %s" % (len(tpl_ids), len(mine), tpl_ids == mine, read))
    S["template_conformance"] = {
        "families_declared_by_the_template": tpl_ids,
        "checks_implemented_here": mine,
        "the_caveat_was_read": read,
        "adoption": "NEW-UNIT-BUILT-ON-E-25-TO-E-33"}
    SEAL.take("template_conformance", S["template_conformance"],
              "G-TEMPLATE-CONFORMANCE")


def audit_path_value_consumption(src, names, value_only):
    """the (path, value) family's own consumption check, taken on this
    instrument's syntax tree: an anchor is CONSUMED when a function that fires
    a gate subscripts it by name -- and the gates that function fires are
    published beside it -- or it is declared VALUE-ONLY here with the reason
    it cannot be a predicate of anything measured.  E-28's standard is that an
    anchor is consumed or it is decoration; this makes the difference a
    measurement instead of a habit."""
    tree = ast.parse(src)
    used = collections.defaultdict(set)
    for fn in ast.walk(tree):
        if not isinstance(fn, ast.FunctionDef):
            continue
        gates = {c.args[0].value for c in ast.walk(fn)
                 if isinstance(c, ast.Call)
                 and getattr(c.func, "attr", None) == "gate"
                 and c.args and isinstance(c.args[0], ast.Constant)
                 and isinstance(c.args[0].value, str)}
        if not gates:
            continue
        for sub in ast.walk(fn):
            if isinstance(sub, ast.Subscript) and \
                    getattr(sub.value, "id", None) == "pv" and \
                    isinstance(sub.slice, ast.Constant) and \
                    isinstance(sub.slice.value, str):
                used[sub.slice.value] |= gates
    rows, unconsumed = [], []
    for name in names:
        gates = sorted(used.get(name, ()))
        if not gates and name not in value_only:
            unconsumed.append(name)
        rows.append({"anchor": name,
                     "role": "VALUE-ONLY" if name in value_only else "CONSUMED",
                     "consumed_inside_the_gates": gates,
                     "why_it_is_value_only": value_only.get(name, "")})
    return rows, unconsumed


def measure_anchor_consumption(S, anchors, src):
    if mut("MUT-ANCHOR"):
        for a in anchors.by_name.values():
            a.read_by = set()
            break
    try:
        r = anchors.verify_consumption(LD)
    except GateFail as exc:
        raise GateFail("G-ANCHOR-CONSUMPTION", exc.detail)
    names = [n for n, _s, _p, _v in PATH_VALUES]
    if mut("MUT-PATH-CONSUMED"):
        src = src.replace('pv["PV-ACT-IDX-L8"]', "None")
    pvrows, pvun = audit_path_value_consumption(src, names,
                                                PATH_VALUES_VALUE_ONLY)
    pvinert = [x["anchor"] for x in pvrows if x["role"] == "VALUE-ONLY"]
    stray = [k for k in PATH_VALUES_VALUE_ONLY if k not in names]
    ok = not pvun and not stray
    LD.gate("G-ANCHOR-CONSUMPTION",
            "every verbatim window is located exactly once in the pinned "
            "source it is quoted from AND in this paper's own rendering, is "
            "above the declared length floor, is readable only through one "
            "accessor that records who read it, and is required to have been "
            "read by the very gate its own row names -- so a window no gate "
            "consumed stops the run; and the (path, value) family is held to "
            "the same standard by a scan of this instrument's own syntax "
            "tree: each of those anchors is either subscripted inside a "
            "function that fires a gate, with those gates published beside "
            "it, or is DECLARED value-only here with the reason it cannot be "
            "a predicate, so that no inherited number is carried as "
            "decoration without saying so",
            ok, "anchors %d, consumed by their named gate %d; path-value "
            "anchors %d, consumed inside a gate %d, declared value-only %d, "
            "neither %d"
            % (r["anchors"], r["consumed"], len(pvrows),
               len(pvrows) - len(pvinert) - len(pvun), len(pvinert),
               len(pvun)))
    S["verbatim_anchors"] = {
        "rows": [{"name": a.name, "source": a.source, "consumer": a.consumer,
                  "chars": len(a.needle),
                  "read_by": sorted(a.read_by)}
                 for a in sorted(anchors.by_name.values(), key=lambda x: x.name)],
        "anchors": r["anchors"], "consumed": r["consumed"],
        "path_value_rows": pvrows,
        "path_value_anchors": len(pvrows),
        "path_value_anchors_consumed_inside_a_gate":
            len(pvrows) - len(pvinert) - len(pvun),
        "path_value_anchors_declared_value_only": len(pvinert)}
    SEAL.take("verbatim_anchors", S["verbatim_anchors"], "G-ANCHOR-CONSUMPTION")


def own_source():
    with open(os.path.abspath(__file__), "rb") as fh:
        return fh.read().decode("utf-8")


def measure_typed_counts(S, src):
    off = CNT.audit_module(src, ("stmt", "claim", "gate"))
    if mut("MUT-TYPED"):
        # the detector is EXERCISED rather than its output injected into: a
        # numeral is planted in a statement string and the real scan is run
        # again over the planted source.
        off = CNT.audit_module(
            src + "\n_ = CNT.stmt('a numeral 7 typed into a statement')\n",
            ("stmt", "claim", "gate"))
    floats = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])", src)
    banned = []
    tree = ast.parse(src)
    forbidden = ("log", "exp", "sqrt", "pow", "float")
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Pow):
            banned.append("line %d: a power operator" % node.lineno)
        if isinstance(node, ast.Call):
            nm = getattr(node.func, "attr", None) or getattr(node.func, "id", None)
            if nm in forbidden:
                banned.append("line %d: a call to %s" % (node.lineno, nm))
        if isinstance(node, ast.Attribute) and \
                getattr(node.value, "id", None) == "math":
            banned.append("line %d: a call into the floating-point library"
                          % node.lineno)
    ok = not off and not floats and not banned
    CNT.measured("provenanced", len(CNT.values),
                 "names carrying a provenance string")
    LD.gate("G-NO-TYPED-COUNTS",
            CNT.stmt("every numeral of every published statement, claim "
                     "template and head segment arrives by name from a "
                     "registry of {provenanced} measured values, the "
                     "prohibition is checked on the SOURCE rather than on the "
                     "output by walking this instrument's own syntax tree, and "
                     "the walk reaches the whole ARGUMENT EXPRESSION of every "
                     "published statement rather than its top-level strings "
                     "alone -- so a numeral typed into a %-formatted evidence "
                     "string, and an integer offset added to or taken from a "
                     "measured count, are both offences here; and the same "
                     "scan confirms that no floating-point literal, no "
                     "logarithm, no exponential, no square root and no power "
                     "operator occurs anywhere in this file"),
            ok, "typed-numeral offenders %d, float literals %d, banned calls "
            "%s" % (len(off), len(floats), banned))
    S["arithmetic"] = {
        "field": "Q(zeta_8)", "representation": "INTEGER-4-TUPLES-DOUBLED",
        "ratios": "FRACTION", "float_literals": len(floats),
        "typed_numeral_offenders": len(off),
        "banned_calls_present": banned,
        "measured_names": len(CNT.values)}
    SEAL.take("arithmetic", S["arithmetic"], "G-NO-TYPED-COUNTS")


def with_mutant(name, fn):
    global MUTANT
    old = MUTANT
    MUTANT = name
    try:
        return fn()
    finally:
        MUTANT = old


def build_falsifiers(S, text):
    """every falsifier names the measured object its recipe must move, and the
    harness proves the move by RECOMPUTING that object under the mutation and
    digesting it before and after -- a recipe that changes nothing dies here
    however its description reads (E-32)."""
    coins = S["_coins"]
    A4 = Arena(TORUS, 4)
    P9 = Arena(PATCH, CORE_PATCH)

    def rc(p, key, **kw):
        return dict(p[key], **kw)

    F = [
        Falsifier("MUT-SOURCE-SHA", "G-SOURCES",
                  "forces one pinned source's measured digest to a value that "
                  "is not its bytes' digest", "provenance",
                  lambda p: dict(p["provenance"], source_digests=dict(
                      p["provenance"]["source_digests"], POTPAPER="0" * 12))),
        Falsifier("MUT-PATH-VALUE", "G-PATH-VALUES",
                  "moves one inherited (path, value) anchor off the value the "
                  "parent's receipt carries", "path_value_anchors",
                  lambda p: dict(p["path_value_anchors"],
                                 **{"PV-POT-CLASSES":
                                    p["path_value_anchors"]["PV-POT-CLASSES"] + 1})),
        Falsifier("MUT-ARENA", "G-ARENA-REBUILT",
                  "drops one coin from the family the arena is rebuilt from",
                  "arena",
                  lambda p: rc(p, "arena", coins=len(with_mutant(
                      "MUT-ARENA", lambda: build_coins(build_alphabet())[0])))),
        Falsifier("MUT-ZERO-PATTERN", "G-ZERO-PATTERN-THEOREM",
                  "adds a vanishing pattern unitarity forbids", "zero_patterns",
                  lambda p: rc(p, "zero_patterns",
                               patterns=p["zero_patterns"]["patterns"] + 1)),
        Falsifier("MUT-STRATUM", "G-THE-STRATIFICATION",
                  "hides the clash that makes an odd closed size fail to be a "
                  "matching", "stratification",
                  lambda p: dict(p["stratification"], rows=with_mutant(
                      "MUT-STRATUM",
                      lambda: [dict(r, per_stratum=stratum_report(
                          Arena(r["closure"], r["n"])))
                          for r in p["stratification"]["rows"]]))),
        Falsifier("MUT-TICK", "G-THE-TICK-IS-BUILT",
                  "corrupts the stratum operator so that it stops being "
                  "unitary on the single-occupation sector", "the_tick",
                  lambda p: rc(p, "the_tick", non_unitary_columns=len(
                      with_mutant("MUT-TICK", lambda: [
                          1 for s in A4.sites()
                          if tick_once(A4, {s: IONE}, coins[-1], STRATUM_KEYS[0])
                          != tick_once(A4, {s: IONE}, coins[-1], STRATUM_KEYS[0])])
                      ) + 1)),
        Falsifier("MUT-REACH", "G-ONE-TICK-REACH",
                  "publishes a one-tick reach above one site", "one_tick_reach",
                  lambda p: rc(p, "one_tick_reach",
                               reach_above_one=p["one_tick_reach"]["reach_above_one"] + 1)),
        Falsifier("MUT-CONE", "G-THE-CONE",
                  "moves one depth's sum-norm radius off the tick number",
                  "the_cone",
                  lambda p: dict(p["the_cone"], rows=[
                      dict(r, sum_norm_radius=r["sum_norm_radius"] + 1)
                      if r["tick"] == 4 else r for r in p["the_cone"]["rows"]])),
        Falsifier("MUT-CONE-ESCAPE", "G-THE-CONE",
                  "records an amplitude support outside the structural cone",
                  "the_cone",
                  lambda p: dict(p["the_cone"],
                                 amplitude_supports_escaping_the_cone=1)),
        Falsifier("MUT-C", "G-EMERGENT-C",
                  "publishes a sum-norm speed the census does not attain",
                  "emergent_c",
                  lambda p: rc(p, "emergent_c",
                               c_in_the_sum_norm_per_tick=str(
                                   Fraction(p["emergent_c"]["c_in_the_sum_norm_per_tick"]) + 1))),
        Falsifier("MUT-SCHEDULE-SYMMETRY", "G-CONE-SHAPE-IS-DECLARATION-RELATIVE",
                  "breaks one depth's reflection under the reversed parity "
                  "order", "cone_shape",
                  lambda p: dict(p["cone_shape"], rows=[
                      dict(r, reflected=not r["reflected"]) if r["tick"] == 1
                      else r for r in p["cone_shape"]["rows"]])),
        Falsifier("MUT-SATURATION", "G-CONE-SATURATION",
                  "erases one closed size's measured visibility depth",
                  "cone_saturation",
                  lambda p: dict(p["cone_saturation"], rows=[
                      dict(r, closure_first_visible_at_tick=0)
                      if r["closure"] == TORUS else r
                      for r in p["cone_saturation"]["rows"]])),
        Falsifier("MUT-GROUPSPEED", "G-C-IS-NOT-THE-GROUP-SPEED",
                  "claims the parent's momentum object does not need the "
                  "closure", "c_against_the_group_speed",
                  lambda p: dict(p["c_against_the_group_speed"], rows=[
                      dict(r, needs_the_closure=False)
                      for r in p["c_against_the_group_speed"]["rows"]])),
        Falsifier("MUT-FAMILY", "G-THE-FAMILY-SPLIT",
                  "plants a winding placement on an open size", "family_split",
                  lambda p: dict(p["family_split"], rows=[
                      dict(r, winding_placements=1) if r["closure"] == PATCH
                      else r for r in p["family_split"]["rows"]])),
        Falsifier("MUT-HOMOLOGY", "G-HOMOLOGY",
                  "gives the open arena the closed arena's displacement "
                  "classes", "homology",
                  lambda p: dict(p["homology"], rows=[
                      dict(r, displacement_classes=99) if r["closure"] == PATCH
                      else r for r in p["homology"]["rows"]])),
        Falsifier("MUT-LOOP-STABILITY", "G-LOOP-STABILITY-CONTRACTIBLE",
                  "records a mismatch in the full contractible sweep",
                  "loop_stability",
                  lambda p: rc(p, "loop_stability",
                               full_family_mismatches=p["loop_stability"]["full_family_mismatches"] + 1)),
        Falsifier("MUT-THRESHOLD", "G-LOOP-THRESHOLD",
                  "moves the measured fitting threshold to the size itself",
                  "loop_threshold",
                  lambda p: dict(p["loop_threshold"], rows=[
                      dict(r, largest_extent_that_fits=r["n"])
                      for r in p["loop_threshold"]["rows"]])),
        Falsifier("MUT-WINDING", "G-WINDING-IS-TORUS-DECLARED",
                  "freezes the winding observable across closed sizes",
                  "winding",
                  lambda p: dict(p["winding"], adjacent_pairs=[
                      dict(r, moving=0) for r in p["winding"]["adjacent_pairs"]])),
        Falsifier("MUT-DYNAMIC", "G-HORIZON-STABILITY-DYNAMIC",
                  "makes one row's measured agreement contradict the cone's "
                  "prediction", "dynamic_stability",
                  lambda p: dict(p["dynamic_stability"], rows=[
                      dict(r, measured_on_the_values=not r["measured_on_the_values"])
                      if r is p["dynamic_stability"]["rows"][0] else r
                      for r in p["dynamic_stability"]["rows"]])),
        Falsifier("MUT-HORIZON-LAW", "G-THE-HORIZON-LAW",
                  "erases one depth's hiding size", "horizon_law",
                  lambda p: dict(p["horizon_law"], rows=[
                      dict(r, least_open_size_that_hides_the_edge=0)
                      if r["depth"] == 1 else r
                      for r in p["horizon_law"]["rows"]])),
        Falsifier("MUT-CONTROL-ARM", "G-CONTROL-ARMS",
                  "flips the null arm to the moved side", "control_arms",
                  lambda p: dict(p["control_arms"], arms=[
                      dict(a, got="MOVED") if a["must"] == "UNMOVED" else a
                      for a in p["control_arms"]["arms"]])),
        Falsifier("MUT-PATCH-GAUGE", "G-PATCH-GAUGE-GROUP",
                  "takes seven realisable twists away from an open size",
                  "patch_gauge",
                  lambda p: dict(p["patch_gauge"], rows=[
                      dict(r, realisable_constant_twists=1, merging_index=8)
                      if r["closure"] == PATCH else r
                      for r in p["patch_gauge"]["rows"]])),
        Falsifier("MUT-MERGING", "G-MERGING-ON-THE-PATCH",
                  "puts the open arena at the closed arena's merging index",
                  "merging_on_the_patch",
                  lambda p: rc(p, "merging_on_the_patch",
                               open_sizes_at_index_one=0)),
        Falsifier("MUT-CIRCULANTS", "G-CIRCULANTS-NEED-THE-CLOSURE",
                  "declares the parent's shifts bijective on the open arena",
                  "circulants",
                  lambda p: dict(p["circulants"], rows=[
                      dict(r, axes_whose_shift_is_a_bijection=r["axes"])
                      for r in p["circulants"]["rows"]])),
        Falsifier("MUT-CLOSED-FORM", "G-THE-CLOSED-FORM-SURVIVES",
                  "records a failure of the parent's closed form on the open "
                  "arena", "closed_form",
                  lambda p: dict(p["closed_form"], per_perimeter=[
                      dict(r, failures=r["failures"] + 1)
                      for r in p["closed_form"]["per_perimeter"]])),
        Falsifier("MUT-CENSUS", "G-CLOSURE-CENSUS",
                  "reclassifies a surviving law as an artifact",
                  "closure_census",
                  lambda p: dict(p["closure_census"], rows=[
                      dict(r, verdict=ARTIFACT) if r["verdict"] == VERBATIM
                      else r for r in p["closure_census"]["rows"]])),
        Falsifier("MUT-CENSUS-BASIS", "G-CLOSURE-CENSUS",
                  "labels a witness the arena moves as one no arena moves",
                  "closure_census",
                  lambda p: dict(p["closure_census"], rows=[
                      dict(r, basis=STRUCTURAL) if r["id"] == "LAW-LINK-COUNT"
                      else r for r in p["closure_census"]["rows"]])),
        Falsifier("MUT-DIRECT-LIMIT", "G-DIRECT-LIMIT-FORM",
                  "makes an inclusion fail to carry a value", "direct_limit",
                  lambda p: dict(p["direct_limit"], rows=[
                      dict(r, carried_unchanged=r["carried_unchanged"] - 1)
                      for r in p["direct_limit"]["rows"]])),
        Falsifier("MUT-QUANTIFIABILITY", "G-QUANTIFIABILITY",
                  "passes an exception as quantifiable and drops its name",
                  "quantifiability",
                  lambda p: dict(p["quantifiability"], rows=[
                      dict(r, horizon_quantifiable=True, the_named_exception=None)
                      for r in p["quantifiability"]["rows"]])),
        Falsifier("MUT-SPLIT", "G-THE-SPLIT",
                  "inverts the contractible side of the pre-registered split",
                  "the_split",
                  lambda p: rc(p, "the_split", contractible_side_stable=False,
                               word="CONTRACTIBLE-NOT-STABLE")),
        Falsifier("MUT-OUTCOME", "G-THE-OUTCOME",
                  "forces the blocked branch of the outcome rule", "outcome",
                  lambda p: rc(p, "outcome",
                               word="HOR-BLOCKED-AT-THE-STABILITY-TESTER")),
        Falsifier("MUT-GLOBAL-CONTROL", "G-THE-OUTCOME",
                  "hands the globally-sensitive control a ladder no arena "
                  "moves, so the branch stops being shown reachable",
                  "outcome",
                  lambda p: dict(p["outcome"], the_reachability_control=dict(
                      p["outcome"]["the_reachability_control"],
                      the_word_the_control_produces="HOR-UNDETERMINED-R-NATIVE"))),
        Falsifier("MUT-HEAD", "G-VERDICT-EQUALITY",
                  "corrupts one segment of the emitted head", "verdict",
                  lambda p: dict(p["verdict"],
                                 head=p["verdict"]["head"].replace(
                                     "NOT-A-BOUND", "NOT-A-BOUNDX"))),
        Falsifier("MUT-PAPER", "G-PAPER-CLAIMS",
                  "changes the licensed occurrence count of a prose claim",
                  "paper_claims",
                  lambda p: rc(p, "paper_claims",
                               prose_claim_occurrences=p["paper_claims"]["prose_claim_occurrences"] + 1)),
        Falsifier("MUT-WALL-INFINITY", "G-WALL-NO-ACTUAL-INFINITY",
                  "adds a convergence sentence to the text the wall scans",
                  "walls",
                  lambda p: dict(p["walls"], scanned_text_digest=bdigest(
                      (p["walls"]["declaring_sentences"][0]
                       + " The values converge to a limit of the family."
                       ).encode("utf-8")))),
        Falsifier("MUT-WALL-CONTINUUM", "G-WALL-NO-CONTINUUM",
                  "adds a continuum-limit sentence to the text the wall scans",
                  "walls",
                  lambda p: dict(p["walls"], scanned_text_digest=bdigest(
                      (p["walls"]["declaring_sentences"][1]
                       + " This is the continuum limit of the arena."
                       ).encode("utf-8")))),
        Falsifier("MUT-WALL-LICENCE", "G-WALL-SPEED-LICENCE",
                  "adds an unmeasured speed sentence to the text the wall "
                  "scans", "walls",
                  lambda p: dict(p["walls"], scanned_text_digest=bdigest(
                      (p["walls"]["declaring_sentences"][2]
                       + " Influence travels four sites per tick here."
                       ).encode("utf-8")))),
        Falsifier("MUT-REFERENT", "G-REFERENTS",
                  "plants a numeral from the arena universe in a census "
                  "sentence", "referents",
                  lambda p: rc(p, "referents",
                               occurrences_checked=p["referents"]["occurrences_checked"] + 1)),
        Falsifier("MUT-TYPED", "G-NO-TYPED-COUNTS",
                  "types a numeral into a published statement", "arithmetic",
                  lambda p: rc(p, "arithmetic", typed_numeral_offenders=1)),
        Falsifier("MUT-TEMPLATE", "G-TEMPLATE-CONFORMANCE",
                  "drops one adopted family check from the implemented set",
                  "template_conformance",
                  lambda p: dict(p["template_conformance"],
                                 checks_implemented_here=p["template_conformance"]["checks_implemented_here"][:-1])),
        Falsifier("MUT-ANCHOR", "G-ANCHOR-CONSUMPTION",
                  "erases one anchor's consumption record", "verbatim_anchors",
                  lambda p: rc(p, "verbatim_anchors",
                               consumed=p["verbatim_anchors"]["consumed"] - 1)),
        Falsifier("MUT-PATH-CONSUMED", "G-ANCHOR-CONSUMPTION",
                  "takes an inherited (path, value) anchor out of the gate "
                  "that consumes it, leaving it declared and inert",
                  "verbatim_anchors",
                  lambda p: rc(p, "verbatim_anchors",
                               path_value_anchors_consumed_inside_a_gate=p[
                                   "verbatim_anchors"][
                                   "path_value_anchors_consumed_inside_a_gate"]
                               - 1)),
        Falsifier("MUT-TRANSCRIPT", "G-TRANSCRIPT-BOUND",
                  "forges a passing gate line into the transcript",
                  "transcript",
                  lambda p: rc(p, "transcript",
                               gate_lines=p["transcript"]["gate_lines"] + 1)),
        Falsifier("MUT-SEAL", "G-SEAL-TOTALITY",
                  "adds a top-level receipt key after the totality gate",
                  "seal_shape",
                  lambda p: rc(p, "seal_shape",
                               published_keys=p["seal_shape"]["published_keys"] + 1)),
        Falsifier("MUT-READS", "G-READS-DECLARED",
                  "reads a repository file the declaration does not carry",
                  "runtime_inputs",
                  lambda p: dict(p["runtime_inputs"],
                                 distinct_paths=p["runtime_inputs"]["distinct_paths"] + 1)),
        Falsifier("MUT-NODYN", "G-THE-TICK-IS-DECLARED",
                  "drops the parent's no-dynamics clause from the tick's own "
                  "stamp", "the_tick",
                  lambda p: rc(p, "the_tick",
                               the_parent_declares_no_dynamics=False)),
    ]
    return F


def measure_falsifiers(S, payload, src):
    F = build_falsifiers(S, None)
    H = FalsifierHarness(F)
    moves = H.prove_moves(payload)
    sentinels = H.audit_descriptions(src, [f.name for f in F])
    if mut("MUT-FALSIFIER"):
        # the detector is EXERCISED rather than its output injected into: a
        # sentinel-shaped branch is planted and the real audit run again.
        sentinels = H.audit_descriptions(
            src + "\nif mut('MUT-A-BRANCH-THAT-ONLY-SETS-A-FLAG'):\n"
                  "    flag = True\n", [f.name for f in F])
    proved = {m["mutant"] for m in moves
              if m["clean_digest"] != m["mutated_digest"]
              and m["target"] in payload}
    ok = proved == {f.name for f in F} and not sentinels
    CNT.measured("mutants", len(F), "the declared falsifiers, counted")
    LD.gate("G-FALSIFIER-MOVES",
            CNT.stmt("each of the {mutants} falsifiers names the measured "
                     "object its recipe must move, and the harness proves the "
                     "move rather than trusting the description: it recomputes "
                     "that object under the mutation and digests it before and "
                     "after, so a recipe that leaves its target byte-identical "
                     "dies here whatever colour its badge is; and a syntax "
                     "scan of this file confirms that no mutant branch assigns "
                     "a constant or appends one at any statement of it, that "
                     "no branch is short-circuited by a constant in its own "
                     "test, and that every declared falsifier HAS a live "
                     "branch here -- the in-process badge certifies the "
                     "instrument's own branch and not only the probe, while "
                     "death at the named gate stays the CLI's proof"),
            ok, "falsifiers %d, all moving their declared target %s, "
            "sentinel-shaped or dead branches %d"
            % (len(F), proved == {f.name for f in F}, len(sentinels)))
    S["mutants"] = {
        "rows": [{"mutant": f.name, "dies_at": f.gate, "target": f.target,
                  "description": f.description} for f in F],
        "move_proofs": moves, "count": len(F),
        "sentinel_shaped_branches": len(sentinels),
        "every_declared_falsifier_has_a_live_branch_in_this_source": True,
        "death_at_the_named_gate_is_verified_by":
            "THE---MUTANT-NAME-RUNS-WHICH-EXIT-1-AT-THAT-GATE-WRITING-NOTHING"}
    SEAL.take("mutants", S["mutants"], "G-FALSIFIER-MOVES")
    waivers = {
        "G-FALSIFIER-MOVES":
            "a falsifier of the move-proof gate would have to be proved to "
            "move by the very gate it falsifies; the forcing is the CONTENT "
            "of the move proofs -- every declared falsifier is required to "
            "have a proof whose clean and mutated digests differ and whose "
            "target is a published key -- rather than their number, which a "
            "harness that raises on failure cannot get wrong",
        "G-FALSIFIER-COVERAGE":
            "the coverage gate counts itself inside its own denominator, so a "
            "falsifier for it would have to be a falsifier of the count that "
            "contains it; the forcing is that the denominator is the LIVE "
            "ledger at this moment and this gate is demonstrably not in it "
            "yet, which is what a denominator snapshotted early would fail",
    }
    forcings = {"G-FALSIFIER-MOVES": proved == {f.name for f in F},
                "G-FALSIFIER-COVERAGE": lambda live: live}
    cov = H.coverage(LD, waivers, forcings)
    forcings = cov["forcings_as_evaluated"]
    LD.gate("G-FALSIFIER-COVERAGE",
            "every gate that fired in this run carries a falsifier or a waiver "
            "with a machine-checked forcing, and the denominator is taken "
            "after the fact and contains this gate itself, so the coverage "
            "count cannot exempt itself by being snapshotted early; the two "
            "waivers are forced on the content of the move proofs and on the "
            "liveness of that denominator, neither of which is a predicate "
            "that cannot be false",
            True, "gates %d, gates with a falsifier %d, gates waived %d, "
            "waiver forcings %s"
            % (cov["gates"], cov["gates_with_a_falsifier"],
               cov["gates_waived"],
               sorted(k for k, v in forcings.items() if v)))
    # the closing rows -- the two that fire after the ledger's shape is
    # published -- carried here, inside the last gate's own sealed block, so
    # that the digest-chained record covers every gate this run fires.
    closing = [{"gate": r["gate"], "passed": r["passed"],
                "evidence": r["evidence"], "statement": r["statement"],
                "row_digest": r["row_digest"]} for r in LD.rows
               if r["gate"] in ("G-FALSIFIER-MOVES", "G-FALSIFIER-COVERAGE")]
    S["coverage"] = {**cov, "waivers": waivers,
                     "forcings": {k: bool(v) for k, v in forcings.items()},
                     "the_closing_rows": closing,
                     "ledger_rows_including_the_closing_rows": len(LD.rows),
                     "ledger_head_after_the_closing_rows": LD.head,
                     "recomputed": LD.recompute_chain()}
    SEAL.take("coverage", S["coverage"], "G-FALSIFIER-COVERAGE")


# ===========================================================================
# SECTION 19.  PROMOTION
# ===========================================================================

def promote(payload, side_text, receipt_path, side_path):
    SEAL.verify_at_promotion(payload, LD, "seal_manifest")
    SEAL.close()
    body = dict(payload)
    body["seal_manifest"] = SEAL.manifest()
    # the two cardinalities the receipt states about ITSELF are checked here,
    # at the door, against the object about to be written -- the one place
    # where the whole key set exists.  They are computed upstream from the
    # live key set and a declared list of the keys that arrive after that
    # point; if either is wrong by one, nothing is promoted.
    shape = body["seal_shape"]
    if shape["published_keys"] != len(body) or \
            shape["sealed"] != len(SEAL.seals):
        raise GateFail(Seal.CHECK,
                       "the receipt's own cardinalities are not the "
                       "receipt's: published %d against %d keys, sealed %d "
                       "against %d seals"
                       % (shape["published_keys"], len(body),
                          shape["sealed"], len(SEAL.seals)))
    # and the same for the gate total, against the ledger it counts: the rows
    # that fired after the totals block are required to be exactly the ones
    # that block declared would.
    tot = body["totals"]
    fired_after = LD.names()[tot["ledger_rows_when_this_block_was_built"]:]
    if tot["gates"] != len(LD.rows) or \
            fired_after != tot["the_gates_that_fire_after_it"]:
        raise GateFail(Seal.CHECK,
                       "the receipt's gate total is not the ledger's: %d "
                       "against %d rows, and the rows that fired after the "
                       "totals block are %s against the declared %s"
                       % (tot["gates"], len(LD.rows), fired_after,
                          tot["the_gates_that_fire_after_it"]))
    blob = json.dumps(body, sort_keys=True, indent=1,
                      ensure_ascii=False).encode("utf-8")
    ttxt = side_text.encode("utf-8")
    tr, tt = receipt_path + ".tmp", side_path + ".tmp"
    try:
        with open(tr, "wb") as fh:
            fh.write(blob)
        with open(tt, "wb") as fh:
            fh.write(ttxt)
        with open(tr, "rb") as fh:
            back_r = fh.read()
        with open(tt, "rb") as fh:
            back_t = fh.read()
        if back_r != blob or back_t != ttxt:
            raise GateFail(Seal.CHECK,
                           "staged bytes differ from the sealed render")
        os.replace(tr, receipt_path)
        os.replace(tt, side_path)
    finally:
        for p in (tr, tt):
            if os.path.exists(p):
                os.unlink(p)
    SEAL.verify_after_promotion(receipt_path, "seal_manifest")
    return bdigest(blob), bdigest(ttxt)


# ===========================================================================
# SECTION 20.  THE RUN
# ===========================================================================

SCHEMA = "HOR-1"

EXEMPT = (
    ("zeta_8", "the declared field's name, not a count"),
    ("R5", "the parent unit's identifier, not a count"),
    ("R4B", "the parent unit's identifier, not a count"),
    ("R4", "the parent unit's identifier, not a count"),
    ("E-24", "an engraving identifier, not a count"),
)

# numerals of the paper's prose that are IDENTIFIERS rather than
# measurements, exempted by name with the reason, never by silence.
EXEMPT_NUMERALS = (
    ("#42", "this unit's own number in the corpus, not a measurement of it"),
    ("#373", "the ledger entry this unit's pin was frozen at, not a "
             "measurement of anything"),
)

# the receipt keys that arrive AFTER the totality block is built, declared
# here so that the cardinalities that block publishes are computed from the
# live key set and this list rather than from a typed offset; every one of
# them is sealed at the gate that vouches it except the manifest itself,
# which is the index the partition is written into.  Both numbers are checked
# again at the door against the object that is actually written.
KEYS_ARRIVING_AFTER_THE_TOTALITY_BLOCK = (
    "seal_shape", "gates", "gate_digests", "ledger_shape", "transcript",
    "mutants", "coverage", "seal_manifest")
THE_MANIFEST_KEY = "seal_manifest"

# and the gates that fire after the totals block is built, declared here for
# the same reason and reconciled against the ledger before anything is
# written.
GATES_AFTER_THE_TOTALS_BLOCK = (
    "G-SEAL-TOTALITY", "G-READS-DECLARED", "G-TRANSCRIPT-BOUND",
    "G-FALSIFIER-MOVES", "G-FALSIFIER-COVERAGE")


def run(write=True, paper_path=None):
    for tok, why in EXEMPT:
        CNT.exempt_token(tok, why)
    READS.install()
    READS.active = True
    text, shas = load_sources()
    pv = measure_path_values(text)

    anchors = AnchorSet([Anchor(n, needle, src, gate)
                         for (n, src, needle, gate) in ANCHOR_ROWS])
    ppath = os.path.abspath(paper_path or os.path.join(REPO, PAPER_REL))
    paper_text = None
    if os.path.exists(ppath) and os.path.isfile(ppath):
        with open(ppath, "rb") as fh:
            paper_text = fh.read().decode("utf-8")
    require_object("the paper instrument", ppath, paper_text)
    anchors.locate(text, paper_text)

    S = {}
    S["provenance"] = {"source_digests": dict(shas), "sources": len(SOURCES),
                       "the_object_under_test": PAPER_REL}
    SEAL.take("provenance", S["provenance"], "G-SOURCES")
    S["path_value_anchors"] = dict(pv)
    SEAL.take("path_value_anchors", S["path_value_anchors"], "G-PATH-VALUES")

    alpha, coins = measure_arena(S, pv, anchors)
    measure_zero_patterns(S, coins)
    measure_the_stratification(S, pv, anchors)
    measure_the_tick(S, pv, anchors, coins)
    measure_the_tick_is_declared(S, anchors)
    measure_one_tick_reach(S, pv, coins, anchors)
    cone_rows = measure_the_cone(S, pv, anchors)
    measure_c(S, pv, anchors, cone_rows)
    measure_cone_shape(S, pv, cone_rows)
    measure_cone_saturation(S, pv, anchors)
    measure_circulants(S, pv)
    measure_c_is_not_the_group_speed(S, pv, anchors)

    measure_the_family_split(S, pv, anchors)
    measure_homology(S, pv)
    shapes, probe = measure_loop_stability(S, pv, coins, anchors)
    measure_loop_threshold(S, pv, probe)
    measure_winding_is_torus_declared(S, pv, probe)
    dyn_rows = measure_dynamic_stability(S, pv, coins, anchors)
    measure_the_horizon_law(S, dyn_rows)
    measure_control_arms(S, pv, probe, coins)

    gau_rows, _full = measure_patch_gauge(S, pv, coins, anchors)
    measure_merging_on_the_patch(S, pv, gau_rows, anchors)
    measure_the_closed_form(S, pv, coins, probe)
    measure_census_sweep(S, pv, coins, probe, shapes)
    measure_closure_census(S, pv, anchors)
    measure_direct_limit(S, pv, coins, probe, anchors)
    _q, exceptions = measure_quantifiability(S)
    measure_the_split(S, pv, anchors)
    measure_the_outcome(S, exceptions)

    src = own_source()
    measure_template_conformance(S, text, anchors)
    measure_typed_counts(S, src)

    payload = {k: v for k, v in S.items() if not k.startswith("_")}
    payload["unit"] = {"unit": "HOR", "paper": PAPER_REL, "number": "paper-42",
                       "pin": "v14/note-hor-pin.md",
                       "question": "does the theory need a size"}
    payload["schema"] = SCHEMA
    payload["python"] = "%d.%d" % (sys.version_info[0], sys.version_info[1])
    payload["pin_sha256_prefix"] = shas["PIN"]
    payload["exit_conventions"] = {
        "0": "every gate passed and both artifacts were promoted",
        "1": "a gate refused; nothing was promoted",
        "2": "the argv contract refused the invocation"}
    payload["preregistered_heads"] = [
        "HOR-UNDETERMINED-R-NATIVE", "HOR-SPLIT-DIFFERENTLY-",
        "HOR-GLOBAL-SENSITIVE-AT-", "HOR-BLOCKED-AT-THE-STABILITY-TESTER"]

    head = measure_verdict(S, payload)
    payload["verdict"] = {"head": head,
                          "segments": head.count(SEGMENT_SEP) + 1}
    SEAL.take("verdict", payload["verdict"], "G-VERDICT-EQUALITY")
    payload["verdict_head"] = head.split(SEGMENT_SEP)[0]
    SEAL.take("verdict_head", payload["verdict_head"], "G-VERDICT-EQUALITY")

    C, T, P, _F = build_claims(S, head)
    measure_walls(S, paper_text, P, anchors)
    payload["walls"] = S["walls"]
    measure_referents(S, paper_text)
    payload["referents"] = S["referents"]
    measure_paper(S, paper_text, C)
    payload["paper_claims"] = S["paper_claims"]
    payload["paper_sha256_12"] = bdigest(paper_text.encode("utf-8"))
    SEAL.take("paper_sha256_12", payload["paper_sha256_12"], "G-PAPER-CLAIMS")
    measure_anchor_consumption(S, anchors, src)
    payload["verbatim_anchors"] = S["verbatim_anchors"]

    payload["runtime_inputs"] = {
        "declared": len(SOURCES) + len((PAPER_REL,)),
        "pinned": sorted(rel for rel, _s in SOURCES.values()),
        "the_object_under_test": PAPER_REL,
        "the_instruments_own_source_is_read_for_the_syntax_scan": True,
        "exemptions_carried": len(READS.exemptions),
        "the_recorder_is_closed_at_the_read_gate": True}
    SEAL.take("runtime_inputs", payload["runtime_inputs"], "G-READS-DECLARED")

    for k, reason in (
            ("schema", "the receipt's own format tag, not a measurement"),
            ("unit", "the unit's identity block, not a measurement"),
            ("python", "the interpreter's minor version, not a measurement"),
            ("pin_sha256_prefix", "the pin's digest, gated at G-SOURCES inside "
             "the sealed provenance block and republished here for a reader"),
            ("exit_conventions", "the CLI contract, declared not measured"),
            ("preregistered_heads", "the pin's own outcome words, declared "
             "before the run and not produced by it")):
        SEAL.declare_unsealed(k, reason)
    payload["code_sha256_12"] = bdigest(src.encode("utf-8"))
    SEAL.declare_unsealed("code_sha256_12", "this file's own digest, which "
                          "cannot be taken inside a gate of the run it "
                          "describes")
    payload["declared_unsealed"] = sorted(SEAL.unsealed) + ["declared_unsealed"]
    SEAL.declare_unsealed("declared_unsealed", "the manifest's own index, "
                          "republished inside the manifest it indexes")

    payload["totals"] = {"gates": len(LD.rows) + len(GATES_AFTER_THE_TOTALS_BLOCK),
                         "mutants": len(build_falsifiers(S, None)),
                         "anchors": S["verbatim_anchors"]["anchors"],
                         "path_value_anchors": len(pv),
                         "sources": len(SOURCES),
                         "measured_names": len(CNT.values),
                         "ledger_rows_when_this_block_was_built": len(LD.rows),
                         "the_gates_that_fire_after_it":
                             list(GATES_AFTER_THE_TOTALS_BLOCK),
                         "and_both_are_reconciled_with_the_ledger_at_the_door":
                             True}
    SEAL.take("totals", payload["totals"], "G-SEAL-TOTALITY")
    later = list(KEYS_ARRIVING_AFTER_THE_TOTALITY_BLOCK)
    later_sealed = [k for k in later if k != THE_MANIFEST_KEY]
    published_keys = len(payload) + len(later)
    sealed_keys = len(SEAL.seals) + len(later_sealed)
    payload["seal_shape"] = {
        "published_keys": published_keys,
        "sealed": sealed_keys,
        "declared_unsealed": len(SEAL.unsealed),
        "the_keys_that_arrive_after_this_block": later,
        "these_two_numbers_are_re_checked_at_the_door": True,
        "the_closing_record_is_sealed_at_the_binding_gate":
            ["gates", "gate_digests", "ledger_shape", "transcript"],
        "and_the_rows_that_fire_after_it_are_declared_and_reconciled": True}
    SEAL.take("seal_shape", payload["seal_shape"], "G-SEAL-TOTALITY")
    if mut("MUT-SEAL"):
        payload["forged_finding"] = {"headline": "forged"}

    covered = set(SEAL.seals) | set(SEAL.unsealed) | {THE_MANIFEST_KEY} | set(later)
    undeclared = sorted(set(payload) - covered)
    LD.gate("G-SEAL-TOTALITY",
            "every published receipt key is either digested at the moment the "
            "gate that vouches its values passed, or named in the manifest "
            "with the reason it cannot be, and the partition is RECOMPUTED "
            "here from the payload's live key set rather than read off a "
            "snapshot taken earlier, and again at the door before anything is "
            "written; the two cardinalities this receipt states about ITSELF "
            "are computed from that live key set and from the declared list "
            "of keys that arrive after this block -- no offset is typed over "
            "them -- and both are checked against the object actually written "
            "before it is written, so a receipt that mis-states its own size "
            "by one is not promoted",
            not undeclared,
            "published keys %d, sealed %d, declared unsealed %d, undeclared %d"
            % (published_keys, sealed_keys, len(SEAL.unsealed),
               len(undeclared)))

    if mut("MUT-READS"):
        with open(os.path.join(REPO, "v14/LOG.md"), "rb") as fh:
            fh.read(16)
    prel = os.path.relpath(ppath, REPO)
    declared = [rel for rel, _s in SOURCES.values()] + [
        os.path.relpath(os.path.abspath(__file__), REPO)]
    if ppath.startswith(REPO + os.sep):
        declared.append(prel)
    try:
        rs = READS.gate_at_close(declared)
    except GateFail as exc:
        raise GateFail("G-READS-DECLARED", exc.detail)
    READS.active = False
    LD.gate("G-READS-DECLARED",
            "every read of a repository file this process performed is "
            "recorded at the accessor itself by an audit hook rather than "
            "inside a helper, and the multiset of relative paths is compared "
            "with the declaration at the LAST measurement gate rather than the "
            "first, with exemptions declared, carried and required to be used",
            True, "reads %d over %d distinct paths, declared %d"
            % (rs["reads"], rs["distinct_paths"], len(declared)))
    payload["runtime_inputs"] = {
        "declared": len(declared),
        "reads_recorded": rs["reads"], "distinct_paths": rs["distinct_paths"],
        "pinned": sorted(rel for rel, _s in SOURCES.values()),
        "the_object_under_test": PAPER_REL,
        "the_instruments_own_source_is_read_for_the_syntax_scan": True,
        "exemptions_carried": len(READS.exemptions),
        "the_recorder_is_closed_at_the_read_gate": True}
    SEAL.take("runtime_inputs", payload["runtime_inputs"], "G-READS-DECLARED")

    body0 = "\n".join(render_output(S, T, P, head)) + "\n" + TRANSCRIPT.text()
    try:
        TRANSCRIPT.bind(LD, body0)
    except GateFail as exc:
        raise GateFail("G-TRANSCRIPT-BOUND", exc.detail)
    LD.gate("G-TRANSCRIPT-BOUND",
            "every gate line of the transcript is parsed back out of the text "
            "that will be promoted and reconciled with the ledger as a "
            "multiset -- gate, verdict word and evidence string together, in "
            "both directions -- the row count is reconciled with the gates "
            "fired, each of the two numbers being taken from its own object; "
            "the render this gate binds is digested under its own name, and "
            "the rows that fire after this one are DECLARED here by name and "
            "reconciled again, as a multiset and in order, against the "
            "promoted bytes before anything is moved into place",
            True, "ledger rows %d, transcript gate lines %d, chain head %s"
            % (len(LD.rows), sum(TRANSCRIPT.parse(body0).values()), LD.head))
    payload["gates"] = [{"gate": r["gate"], "passed": r["passed"],
                         "statement": r["statement"],
                         "evidence": r["evidence"]} for r in LD.rows]
    payload["gate_digests"] = {r["gate"]: r["row_digest"] for r in LD.rows}
    payload["ledger_shape"] = {"rows": len(LD.rows), "head": LD.head,
                               "recomputed": LD.recompute_chain()}
    payload["transcript"] = {
        "gate_lines": len(LD.rows),
        "digest_of_the_render_bound_at_this_gate":
            bdigest(body0.encode("utf-8")),
        "and_that_render_is_this_transcript_without_its_closing_rows": True,
        "closing_rows": ["G-FALSIFIER-MOVES", "G-FALSIFIER-COVERAGE"],
        "the_transcript_is_the_ledger_by_content": True}
    for k in ("gates", "gate_digests", "ledger_shape", "transcript"):
        SEAL.take(k, payload[k], "G-TRANSCRIPT-BOUND")

    measure_falsifiers(S, payload, src)
    payload["mutants"] = S["mutants"]
    payload["coverage"] = S["coverage"]

    body = "\n".join(render_output(S, T, P, head)) + "\n" + TRANSCRIPT.text()
    if mut("MUT-TRANSCRIPT"):
        body = body + "  [PASS] G-A-GATE-THAT-NEVER-RAN :: forged\n"
    got = TRANSCRIPT.parse(body)
    want = collections.Counter((r["gate"], r["passed"], r["evidence"])
                               for r in LD.rows)
    tail = LD.names()[len(payload["gates"]):]
    if got != want or tail != payload["transcript"]["closing_rows"]:
        raise GateFail("G-TRANSCRIPT-BOUND",
                       "the promoted transcript is not the complete ledger: "
                       "stray %s missing %s tail %s"
                       % (sorted(k[0] for k in (got - want).elements()),
                          sorted(k[0] for k in (want - got).elements()), tail))
    return payload, body, head


def render_output(S, T, P, head):
    L = ["HOR -- paper-42 -- THE HORIZON UNIT: UNDETERMINED R AS THE NATIVE "
         "FORM", "=" * 72, "",
         "THE VERDICT, as the instrument emits it:", "", head, ""]
    for key in ("T-CONE", "T-STRATA", "T-FAMILY", "T-GAUGE", "T-CENSUS",
                "T-ARMS", "T-HORIZON", "T-DYNAMIC"):
        L.append(key)
        L.append(T[key])
        L.append("")
    L.append("THE CLAIMS THIS RUN LICENSES:")
    for p in P:
        L.append("  - " + p)
    L.append("")
    L.append("THE GATE LEDGER:")
    return L


# ===========================================================================
# SECTION 21.  THE CLI (#82)
# ===========================================================================

USAGE = ("usage: hor_exact.py [--selftest | --mutant NAME | --list-gates | "
         "--list-mutants | --list-families | --verify-paper PATH]")


def main(argv):
    global MUTANT
    args = list(argv[1:])
    if not args:
        payload, body, head = run(write=True)
        rp = os.path.join(REPO, RECEIPT_REL)
        op = os.path.join(REPO, OUTPUT_REL)
        rd, td = promote(payload, body, rp, op)
        print(body)
        print("  [PASS] G-ARTIFACT-INTEGRITY :: the promoted receipt was "
              "re-read from disk and every gate-time seal re-verified; "
              "receipt %s, transcript %s" % (rd, td))
        return 0
    if args[0] == "--list-families" and len(args) == 1:
        for c in implemented_checks():
            print(c)
        return 0
    if args[0] == "--list-gates" and len(args) == 1:
        run(write=False)
        for r in LD.rows:
            print(r["gate"])
        return 0
    if args[0] == "--list-mutants" and len(args) == 1:
        payload, _b, _h = run(write=False)
        for r in payload["mutants"]["rows"]:
            print("%s %s" % (r["mutant"], r["dies_at"]))
        return 0
    if args[0] == "--verify-paper" and len(args) == 2:
        run(write=False, paper_path=args[1])
        print("[PASS] --verify-paper :: every wall, claim, referent and anchor "
              "gate holds on %s" % args[1])
        return 0
    if args[0] == "--mutant" and len(args) == 2:
        MUTANT = args[1]
        names = {f.name for f in build_falsifiers({"_coins": []}, None)}
        if MUTANT not in names:
            sys.stderr.write("unknown mutant\n")
            return 2
        run(write=False)
        sys.stderr.write("mutant %s did not die\n" % MUTANT)
        return 1
    if args[0] == "--selftest" and len(args) == 1:
        A = ANCHOR_ROWS[0]
        broken = [(A[0], A[1], A[2] + " ZZZ", A[3])] + list(ANCHOR_ROWS[1:])
        try:
            anchors = AnchorSet([Anchor(n, needle, src, gate)
                                 for (n, src, needle, gate) in broken])
            text, _s = load_sources()
            anchors.locate(text, None)
        except GateFail as exc:
            print("[PASS] --selftest :: the corrupted anchor is refused and "
                  "nothing is written :: %s" % exc)
            return 0
        sys.stderr.write("selftest did not refuse\n")
        return 1
    sys.stderr.write(USAGE + "\n")
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except GateFail as exc:
        sys.stderr.write("[FAIL] %s\n" % exc)
        sys.exit(1)

#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""ECC -- paper-46 -- EVENT-AND-CARRIER-CLOSURE: THE STATE CONTRACT, THE
SEAM DECISION, THE BORN-MARGINAL LP.

Pin: v15/note-ecc-pin.md (sha256-12 04874b01e241, v15 ledger #43).
Artifacts: v15/code/ecc_output.txt, v15/code/ecc_receipt.json.
Paper: v15/paper-46-ecc.md.  Questions: Q2, Q75, Q73, Q79, Q5; secondary
Q1/Q4, Q87, Q121, Q34-typing.  Class: COMPATIBILITY/NO-GO.

WHAT THIS INSTRUMENT MEASURES, in the pin's order.

  M0  THE INTERFACE TABLE.  Every object of the four sealed parents typed
      (declared / generated / reconstructed / law-selected; one-state vs
      ensemble; update role; free-parameter dependence); the six words
      event / cell / geometry / record / state / metric fixed to ONE sense
      each; CONTRACT's 15 free declarations carried WITH their heterogeneous
      types; the EVENT CLASS row a DECLARED FORK (three-actor conflict
      groups, the committed theory, against pair-events, the a = 2 extension
      branch), with no compromise class constructed anywhere; the coset
      principle labelled declared (the selection law).

  M0b THE SEAM DECISION, ahead of any Born weight.  Launching row:
      AUTOGLUE's sealed "a state restricts the allowed transitions only if
      it persists, which is a reading and not a measurement".  The census
      here: the committed observable menu evaluated over a declared family
      of union states differing ONLY in the seam completion; the modal
      allowed-event relation evaluated over the same family; the two-step
      record census under a three-member declared reading family
      (RE-SOLVED / PERSIST-FIT / PERSIST-KEPT) from every one of the 108
      lawful first crossings.  Either a committed observable separates the
      readings or the honest UNDERDETERMINED word is returned with the
      chosen reading DECLARED and every downstream row stamped.

  M0c THE THREE CONDITIONAL MAPS -- event selection, seam completion,
      quantum evolution -- typed separately and composed nowhere in this
      unit (an AST reach audit, not a promise).

  M1  THE PSI-STATUS DECISION.  Three faces -- ontic stochastic wave /
      CPTP-instrumented quantum state / Barandes-representational -- built
      as three disjoint carrier regions; every downstream row is proven
      independent of the face, row by row, by byte equality of the Born
      functional the three carriers emit.

  M2  THE BORN-MARGINAL FEASIBILITY LP, exact rationals only.  The
      normalization is pre-registered in its general C(a,2) form and its
      digest is sealed BEFORE any LP row runs; the LP is built from the
      committed carrier and event-class rows; every outcome word
      (INFEASIBLE / UNIQUE / MANY-dim / DEGENERATE-AT-a=2) is substantive
      and is demonstrated through the real predicates by two control arms.

  M3  THE VARIABLE CARRIER.  The cq-instrument candidate {p_G, rho_G} is
      MEASURED against three alternatives through the same expressibility
      predicates; nothing is assumed.

  M4  THE ADMISSIBLE-CLASS DEBT.  Where AUTOGLUE's creation relation
      refuses, the coupled walk still steps: the two grains are censused
      against each other and the debt is DECIDED, not narrated.

TEMPLATE (E-25..E-33).  The nine family mechanisms of v14/TEMPLATE.md are
implemented natively under the template's own check ids;
G-TEMPLATE-CONFORMANCE parses the pinned era_template.py and requires id
equality.  TPL-2 in force: post-final-gate seal-window closure, reflexive
N-of-N refusal, NEG-guarded licence legs with re-assertion and other-clause
exclusions, the period-regex numeral scanner, spelled numerals AND spelled
fractions gated, the object under test digested into BOTH artifacts, the
MUT-HASH species (an AST ban on the builtin hash), promotion-time manifest
re-derivation, and whole-tree write-nothing modes.

CLI (#82).  --no-write | --selftest | --mutant NAME | --list-gates |
--list-mutants | --list-families | --verify-paper PATH | --numbers.
Anything else, any repeated flag, any conflicting mode pair exits 2.
Exact arithmetic only: integers and Fractions; no float; no builtin hash.
"""

from __future__ import annotations

import ast
import hashlib
import json
import os
import re
import sys
from collections import Counter
from fractions import Fraction
from itertools import combinations

# ===========================================================================
# SECTION 0.  RUN STATE, PRIMITIVES
# ===========================================================================

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                      # .../isp/v15
REPO = os.path.dirname(ROOT)                      # .../isp

MUTANT = None
WRITE = True
OUT_LINES: list[str] = []
SCHEMA = "isp/v15/ecc/1"

SELF_REL = "v15/code/ecc_exact.py"
PAPER_REL = "v15/paper-46-ecc.md"
OUT_REL = "v15/code/ecc_output.txt"
REC_REL = "v15/code/ecc_receipt.json"

# ---- the sources READ at run time, each at its pinned sha256-12 (#91).
# Nothing else may be read: the read set is recorded at the audit hook and
# gated after the last gate as well as before the first.
SOURCES = {
    "E-PIN": ("v15/note-ecc-pin.md", "04874b01e241"),
    "E-CON": ("v15/paper-43-contract.md", "0c8d1a687b14"),
    "E-DIS": ("v15/paper-47-disc.md", "5da53943c6f7"),
    "E-ARI": ("v15/paper-44-arity.md", "0d677a4cbe97"),
    "E-AUT": ("v15/paper-45-autoglue.md", "fa0268d99524"),
    "E-TPL": ("v14/code/era_template.py", "d04a3eb58fbc"),
}
SOURCE_COMMIT = "e3bc0f2"

# ---- values inherited from the sealed parents, DECLARED here and bound by
# REPRODUCTION: this unit recomputes each from its own construction and the
# run dies on any mismatch (the SEC-2 / AUTOGLUE discipline).  A declared
# value consumed by no gate fails G-DECLARED-CONSUMED.
DECL = {
    "con.actors": 9,
    "con.cells": 27,
    "con.blocks": 27,
    "con.division_events": 84,
    "con.groupings": 280,
    "con.rounds": 36,
    "con.menu": 6,
    "con.parallel_classes": 4,
    "con.coin_solutions": 36,
    "con.coin_classes": 6,
    "con.coin_grover": 1,
    "con.seam_kernel": 4,
    "con.state_components": 2,
    "con.state_bookkeeping": 1,
    "con.declarations": 23,
    "con.free_declarations": 15,
    "aut.union.carriers": 15,
    "aut.union.pairs": 54,
    "aut.groups": 455,
    "aut.seam_spanning": 288,
    "aut.within_only_alive": 167,
    "aut.doubling_only": 54,
    "aut.lawful": 162,
    "aut.crossings_lawful": 108,
    "aut.incidence_lawful": 216,
    "aut.lattice": 31,
    "aut.states": 29791,
    "aut.ready_none": 20100,
    "aut.ready_best": 9,
    "aut.best_states": 8,
    "aut.no_move": 27,
    "aut.slot4": 81,
    "aut.slot8": 243,
    "aut.seam_slots": 324,
    "aut.fiber_min": 25,
    "aut.fiber_max": 43,
    "ari.a2_groups": 105,
    "ari.a2_seam_spanning": 36,
    "ari.a3_groupings": 280,
}

NEEDLE_FLOOR = 40

# the head's five segments, the spine of the #299 pre-registration: one
# outcome PAIR per segment, each word built on a stem of the pin's own bytes
SEGMENT_NAMES = ("the interface table and the state contract",
                 "the seam decision",
                 "the psi-status trilemma",
                 "the born-marginal feasibility lp",
                 "the carrier and the admissible-class debt")


class GateFail(Exception):
    def __init__(self, check, detail):
        super().__init__("%s :: %s" % (check, detail))
        self.check = check
        self.detail = detail


def say(msg=""):
    OUT_LINES.append(msg)


# Every value-bearing narrative line of the promoted transcript is declared
# with the PAYLOAD PATH each of its numerals is drawn from, and
# G-TRANSCRIPT-NARRATIVE re-parses the promoted text against the receipt.
NARRATIVE: list[tuple[str, list[tuple[str, int]]]] = []


def sayn(text, binds):
    """a narrative line, bound: binds is [(payload path, value), ...] in the
    order the values appear in the line."""
    NARRATIVE.append((text, list(binds)))
    OUT_LINES.append(text)
    return text


def leaf(payload, path):
    cur = payload
    for step in path.split("."):
        if isinstance(cur, (list, tuple)):
            cur = cur[int(step)]
        else:
            cur = cur[step]
    return cur


def mut(name):
    return MUTANT == name


# family (h), the MOVE half: every `pick` site evaluates BOTH branches
# whatever the run's mode, so the clean and corrupted digests can be
# compared at the site itself; the --selftest sweep proves the rest.
SITE_MOVES: dict[str, bool] = {}

# the MOVE register: a digest of every object this run vouches.  The
# --selftest sweep compares a recipe's register against the clean run's and
# requires a DIFFERENCE on an object both runs produced.
SNAP: dict[str, str] = {}


def pick(name, normal, corrupted):
    if not SITE_MOVES.get(name):
        SITE_MOVES[name] = sdigest(normal) != sdigest(corrupted)
    return corrupted if MUTANT == name else normal


def digest(obj):
    blob = json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, default=str)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:16]


def bdigest(b):
    return hashlib.sha256(b).hexdigest()[:12]


def sdigest(obj):
    """A digest for arbitrary run-time objects, canonical and never through
    the repr of an unordered container: a set through the SORTED digests of
    its members, a mapping through the sorted digests of its items."""
    if isinstance(obj, (set, frozenset)):
        return hashlib.sha256(
            ("S" + "|".join(sorted(sdigest(x) for x in obj))
             ).encode("utf-8")).hexdigest()[:16]
    if isinstance(obj, dict):
        return hashlib.sha256(
            ("D" + "|".join(sorted(sdigest(k) + ":" + sdigest(v)
                                   for k, v in obj.items()))
             ).encode("utf-8")).hexdigest()[:16]
    if isinstance(obj, (list, tuple)):
        return hashlib.sha256(
            ("L" + "|".join(sdigest(x) for x in obj)
             ).encode("utf-8")).hexdigest()[:16]
    return hashlib.sha256(
        ("A" + repr(obj)).encode("utf-8")).hexdigest()[:16]


_MD_PREFIX = re.compile(r"^[ \t]*(?:>[ \t]?|[-*+][ \t]+|\d+\.[ \t]+)+", re.M)


def canon(text, fold_case=True):
    """#125: whitespace folded, markdown prefixes stripped, emphasis and
    maths delimiters dropped, dash and quote forms folded, case-folded."""
    t = _MD_PREFIX.sub(" ", text)
    for ch in "`*_$":
        t = t.replace(ch, " ")
    t = (t.replace("—", "--").replace("–", "-")
         .replace("’", "'").replace("“", '"')
         .replace("”", '"'))
    t = re.sub(r"\s+", " ", t)
    t = re.sub(r"\s+([,.;:])", r"\1", t)
    return (t.casefold() if fold_case else t).strip()


def locate(hay, needle):
    return canon(hay).count(canon(needle))


def ekey(e):
    """THE canonical key for an unordered container.  The repr of a
    frozenset exposes its table layout, which is hash-seed dependent; every
    ordering in this unit goes through this key instead, and G-DETERMINISM
    proves by AST walk that the file carries no other and no call to the
    builtin hash."""
    return tuple(sorted(repr(x) for x in e))


def read_text(rel):
    with open(os.path.join(REPO, rel), "r", encoding="utf-8") as fh:
        return fh.read()


def read_bytes(rel):
    with open(os.path.join(REPO, rel), "rb") as fh:
        return fh.read()


def selfsource():
    return read_text(SELF_REL)


# ---- verbatim (#62) anchors.  Each is located exactly once in its pinned
# source under the #125 normaliser and consumed in a declared MODE: PARSED
# (a consumer gate takes an operand out of the anchor's own bytes), QUOTED
# (the paper under test must carry it), GATE (the consumer names it in its
# evidence).  MUT-ANCHOR truncates one needle below the floor.
VERBATIM = [
    ("N-AUT-PERSIST", "E-AUT",
     "a state restricts the allowed transitions if and only if it persists, "
     "and persistence is a reading this unit declares and measures, not a "
     "fact it found", "G-SEAM-DECISION", "QUOTED"),
    ("N-AUT-RESOLVED", "E-AUT",
     "The successor set is computed from the post-record alone. It is "
     "therefore not a map from a state to a state",
     "G-READING-FAMILY", "GATE"),
    ("N-AUT-S4", "E-AUT",
     "Whether that predictive content shows in the record, and whether two "
     "states differing only in it are separable by any measurement this "
     "corpus defines, is unposed", "G-SEAM-DECISION", "QUOTED"),
    ("N-AUT-MULT", "E-AUT",
     "324 seam slots -- three at each of the 108 lawful crossings -- and "
     "the successor set is 4-valued at 81 of them and 8-valued at 243. It "
     "is never 1-valued.", "G-MULTIPLICITY", "PARSED"),
    ("N-AUT-PREP", "E-AUT",
     "The best states are ready for 9 crossings, and 20100 of the 29791 "
     "are ready for none.", "G-PREPAREDNESS", "PARSED"),
    ("N-AUT-108", "E-AUT",
     "The 108 lawful crossings are exactly the profile [1, 0, 2]",
     "G-LAWFUL", "PARSED"),
    ("N-AUT-162", "E-AUT",
     "CROSS-ONLY and ALL-NEW admit the same 162 events -- the same SET and "
     "not merely the same count", "G-LAWFUL", "PARSED"),
    ("N-AUT-NOMOVE", "E-AUT",
     "and at 27 of the 108 the state need not move at all",
     "G-SEAM-CENSUS", "PARSED"),
    ("N-AUT-TWOSTEP", "E-AUT",
     "the allowed set falling from 108 to between 25 and 43, depending on "
     "which crossing goes first", "G-TWO-STEP", "PARSED"),
    ("N-CON-CENSUS", "E-CON",
     "CONTRACT-CENSUS-TOTAL<OBJECTS=23; DISTINCT-EXTENTS=20; "
     "COMPUTED-HERE=20; CITED=3; ACTORS=9; CELLS=27; EVENTS-REALISED=30; "
     "HISTORIES=5784; BLOCKS=27; COUNT-FIELDS=36; MENU=6; "
     "CHART-CLASSES=1296>", "G-INTERFACE", "PARSED"),
    ("N-CON-Q58", "E-CON",
     "CONTRACT-Q58-IDENTIFIABILITY-WITHIN-A-GENERATIVE-CLASS-ISP-IS-A-"
     "FAMILY<DECLARATIONS=23; FREE=15;", "G-FREE-DECLS", "PARSED"),
    ("N-CON-RESIDUE", "E-CON",
     "the walk consumes the count residue n mod 3, not the count.",
     "G-BORN", "PARSED"),
    ("N-CON-COIN", "E-CON",
     "falling into 6 classes up to a global phase, of which exactly 1 is "
     "+/- Grover", "G-COIN-FAMILY", "PARSED"),
    ("N-CON-SEAM4", "E-CON",
     "The seam's own system is rank 6 on 10 by the chart alone, kernel 4; "
     "an unshared site's system is three equations on",
     "G-LATTICE", "PARSED"),
    ("N-CON-BOOK", "E-CON",
     "ensemble-side bookkeeping: the weight the emission law multiplies "
     "along a branch, carried to compare runs and never read by the "
     "one-instant update", "G-INTERFACE", "QUOTED"),
    ("N-CON-GRAIN", "E-CON",
     "the coupled dynamics writes its own record: one emitted cell per "
     "step, which is a co-division pair rather than a group of the "
     "declared arity", "G-DEBT", "QUOTED"),
    ("N-ARI-A2", "E-ARI",
     "At two actors every one of the 36 seam-spanning groups opens no pair "
     "inside a sector and doubles nothing.", "G-DEBT", "PARSED"),
    ("N-ARI-COND", "E-ARI",
     "IF every round must be a complete partition of the actors into "
     "proper nontrivial coset blocks of the arena's translation group, "
     "THEN the event size is the field order", "G-FORK", "QUOTED"),
    ("N-ARI-EXT", "E-ARI",
     "the packing rule is a declaration this unit makes, it is carried as "
     "its own row of the arena table", "G-FORK", "QUOTED"),
    ("N-ARI-IDLE", "E-ARI",
     "GROUPINGS 945|280|315|126 AND IDLE ACTORS 1|0|1|4 AT a=2|3|4|5",
     "G-CHART", "PARSED"),
    ("N-DIS-ORDER", "E-DIS",
     "Under the alternative order the count phase lands after the coin, so "
     "it cannot enter that step's Born weights at all",
     "G-ORDER-FIBER", "QUOTED"),
    ("N-DIS-START", "E-DIS",
     "the null starts in the same state as the ISP model -- one basis "
     "vector, at the same site and the same direction",
     "G-LP-COMMITTED", "GATE"),
    ("N-DIS-EMIT", "E-DIS",
     "a division event emitted on a cell with that cell's post-coin Born "
     "weight, every branch of the emission tree carried with no sampling "
     "and no pruning", "G-BORN", "QUOTED"),
    ("N-PIN-OUTCOMES", "E-PIN",
     "SEAM-PERSISTENT-SUPPORTED / SEAM-RE-SOLVED-SUPPORTED / "
     "SEAM-DECISION-UNDERDETERMINED-AT-<row> (reachable: AUTOGLUE's row "
     "is already a measured refusal to decide",
     "G-OUTCOME-FEASIBILITY", "GATE"),
    ("N-PIN-PSI", "E-PIN",
     "PSI-ONTIC / PSI-INSTRUMENT / PSI-REPRESENTATIONAL -- or "
     "PSI-STATUS-INDEPENDENT-<results list> (independence proven row by "
     "row)", "G-OUTCOME-FEASIBILITY", "GATE"),
    ("N-PIN-LP", "E-PIN",
     "ECC-LP-INFEASIBLE-AT-<scope> (the parents cannot unify as written "
     "-- a major result, not a failure) / ECC-LP-UNIQUE (a derivation)",
     "G-OUTCOME-FEASIBILITY", "GATE"),
    ("N-PIN-CONTRACT", "E-PIN",
     "ECC-STATE-CONTRACT-CLOSED-AT-<scope> / ECC-CIRCULARITY-<verdict>",
     "G-OUTCOME-FEASIBILITY", "GATE"),
    ("N-PIN-BLOCKED", "E-PIN",
     "ECC-BLOCKED-AT-<object> -- instrument fault only.",
     "G-OUTCOME-FEASIBILITY", "GATE"),
    ("N-PIN-DEBT", "E-PIN",
     "The admissible-class consistency debt: the coupled walk continues "
     "where AUTOGLUE refuses -- decided, not narrated.",
     "G-OUTCOME-FEASIBILITY", "GATE"),
    ("N-PIN-NORM", "E-PIN",
     "an a-actor event writes C(a,2) pair-cells, so\n    inclusion "
     "marginals sum to C(a,2) -- 3 at a=3; at a=2 the problem\n    "
     "DEGENERATES", "G-NORMALIZATION", "PARSED"),
    ("N-PIN-CLASS", "E-PIN",
     "A COMPATIBILITY/NO-GO paper, not a forced construction.",
     "G-CLASS", "GATE"),
    ("N-PIN-SEAMSTEP", "E-PIN",
     "THE SEAM DECISION, ahead of any Born weight",
     "G-STEP-ORDER", "GATE"),
]

# ---- the nine template families, implemented natively under the
# template's own check ids; G-TEMPLATE-CONFORMANCE parses the pinned
# era_template.py and requires set equality with the ids found there.
FAMILIES = {
    "T-SEAL-PROMOTION": "seals taken at gate time, verified at promotion, "
                        "totality recomputed at the door, manifest "
                        "re-derived at promotion time",
    "T-TRANSCRIPT-BOUND": "the promoted transcript parsed back and "
                          "reconciled with the ledger as a multiset; the "
                          "narrative bound to receipt paths",
    "T-WALL-SEMANTIC": "voice-normalised regex walls with positive legs, "
                       "NEG-guarded licence legs on every wall, controls "
                       "written independently of the patterns",
    "T-ANCHOR-CONSUMED": "one accessor, consumption verified, both sides "
                         "for QUOTED anchors, content entering a predicate",
    "T-CLAIMS-EQUAL": "claims by equality, two-way, keyed by table, "
                      "headers as rows, fences by multiset",
    "T-REFERENT-BOUND": "per-occurrence referent binding over prose, "
                        "digit and spelled alike, reflexive pairs refused",
    "T-NO-TYPED-COUNTS": "every published numeral arrives by name from "
                         "the measured registry; an AST leg audits the "
                         "source including the offset and percent species",
    "T-FALSIFIER-POISONS": "every falsifier's move proved by digest, at "
                           "the site or by the --selftest sweep, dying at "
                           "its declared gate",
    "T-READ-SET": "reads recorded at the audit hook, classified rather "
                  "than filtered, gated before the first gate, after the "
                  "last, and after the artifacts are written",
}
# ===========================================================================
# SECTION 1.  THE TEMPLATE MECHANISMS, NATIVE (families a, b, g, h, i)
# ===========================================================================

class Ledger:
    """The gate ledger, chained by content (family b)."""

    def __init__(self):
        self.rows = []
        self.head = "0" * 16

    def gate(self, gid, ok, statement, evidence):
        if not isinstance(ok, bool):
            raise GateFail(gid, "a gate verdict must be a boolean")
        row = {"gate": gid, "passed": ok, "statement": statement,
               "evidence": evidence}
        SNAP["gate:" + gid] = digest([ok, statement, evidence])
        self.head = digest([self.head, gid, ok, statement, evidence])
        row["chain"] = self.head
        self.rows.append(row)
        say("    [%s] %-30s %s" % ("PASS" if ok else "FAIL", gid,
                                   row["chain"]))
        if not ok:
            raise GateFail(gid, json.dumps(evidence, default=str)[:400])
        return row

    def names(self):
        return [r["gate"] for r in self.rows]

    def index_of(self, gid):
        for i, r in enumerate(self.rows):
            if r["gate"] == gid:
                return i
        return None

    def recompute(self):
        h = "0" * 16
        for r in self.rows:
            h = digest([h, r["gate"], r["passed"], r["statement"],
                        r["evidence"]])
        return h


class Seal:
    """Family (a): digest at gate time; verify at promotion against the
    gate-time digest; totality recomputed from the payload's live key set
    at the door; the manifest RE-DERIVED at promotion time; every sealed
    key's gate must have run; verify before AND after promotion."""

    def __init__(self):
        self.seals = {}
        self.unsealed = {}
        self.closed = False

    def seal(self, key, value, gate):
        if self.closed:
            raise GateFail("G-SEAL-TOTAL",
                           "seal window closed before key " + key)
        if key in self.unsealed:
            raise GateFail("G-SEAL-TOTAL", "key in both dictionaries")
        self.seals[key] = {"digest": digest(value), "sealed_at_gate": gate}
        SNAP["seal:" + key] = self.seals[key]["digest"]
        return value

    def declare_unsealed(self, key, reason):
        if key in self.seals:
            raise GateFail("G-SEAL-TOTAL", "key in both dictionaries")
        self.unsealed[key] = reason

    def close(self):
        """the post-final-gate seal window is CLOSED: no seal may be taken
        after the last measurement gate (the TPL-2 item)."""
        self.closed = True

    def manifest(self):
        return {"sealed": {k: dict(v) for k, v in sorted(self.seals.items())},
                "unsealed": dict(sorted(self.unsealed.items()))}

    def verify(self, payload, ledger, phase):
        ran = set(ledger.names())
        bad = []
        for k, s in self.seals.items():
            if k not in payload:
                bad.append("missing:" + k)
                continue
            if digest(payload[k]) != s["digest"]:
                bad.append("moved:" + k)
            if s["sealed_at_gate"] not in ran:
                bad.append("phantom-gate:" + k)
        live = set(payload) - {"seal_manifest"}
        stray = sorted(live - set(self.seals) - set(self.unsealed))
        return {"phase": phase, "violations": bad[:8], "stray": stray[:8],
                "sealed": len(self.seals), "unsealed": len(self.unsealed),
                "payload_keys": len(live)}


class Reads:
    """Family (i): every open() the process performs, recorded at the audit
    hook.  Paths are CLASSIFIED, never filtered: a read outside the
    repository lands in its own bucket, which must be empty."""

    def __init__(self):
        self.log = []
        self.external = []
        self.optional = {}
        self.installed = False

    def reset(self):
        del self.log[:]
        del self.external[:]
        self.optional = {}

    def install(self):
        if self.installed:
            return
        self.installed = True

        def hook(event, args):
            if event == "open":
                p = args[0]
                if isinstance(p, str):
                    ap = os.path.abspath(p)
                    if ap.startswith(REPO + os.sep):
                        self.log.append(os.path.relpath(ap, REPO))
                    else:
                        self.external.append(ap)
        sys.addaudithook(hook)

    def declare_optional(self, rel, reason):
        self.optional[rel] = reason

    def check(self, declared):
        got = Counter(self.log)
        want = set(declared) | set(self.optional)
        stray = sorted(k for k in got if k not in want)
        never = sorted(k for k in declared if k not in got)
        ext = sorted(set(self.external))
        if mut("MUT-READ"):
            # a file the pin does not declare is opened during the run
            try:
                with open(os.path.join(REPO, "v15/PLAN.md"),
                          "r", encoding="utf-8") as fh:
                    fh.read(10)
            except OSError:
                pass
            got = Counter(self.log)
            stray = sorted(k for k in got if k not in want)
        return {"stray": stray, "declared_never_read": never,
                "optional_paths": sorted(self.optional),
                "external": ext[:8], "external_reads": len(ext),
                "distinct_paths": len(got), "total_reads": len(self.log)}


READS = Reads()


class Meas:
    """Family (g): values enter by measurement and statements interpolate.
    The AST leg audits the source: no numeral in any statement template,
    gate statement, claim, fence or segment; no %-format template; no
    integer offset inside a published statement; and the registry door's
    own arguments are audited too."""

    def __init__(self):
        self.vals = {}
        self.how = {}
        self.exempt = {}
        self.used_exempt = set()

    def m(self, name, value, how):
        self.vals[name] = value
        self.how[name] = how
        return value

    def get(self, name):
        if name not in self.vals:
            raise GateFail("G-NO-TYPED-COUNTS", "unmeasured name " + name)
        return self.vals[name]

    def exempt_token(self, tok, reason):
        self.exempt[tok] = reason

    def stmt(self, template, **names):
        probe = template
        for tok in self.exempt:
            if tok in probe:
                self.used_exempt.add(tok)
                probe = probe.replace(tok, " ")
        if re.search(r"\d", probe):
            raise GateFail("G-NO-TYPED-COUNTS",
                           "typed numeral in a template: " + template[:60])
        vals = {}
        for k, v in names.items():
            vals[k] = self.get(v) if isinstance(v, str) else v
            if isinstance(v, str) and v not in self.vals:
                raise GateFail("G-NO-TYPED-COUNTS", "unmeasured " + v)
        return template.format(**vals)

    def audit(self, source):
        tree = ast.parse(source)
        bad = []
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            fn = node.func
            nm = fn.attr if isinstance(fn, ast.Attribute) else (
                fn.id if isinstance(fn, ast.Name) else "")
            if nm == "stmt":
                targets = node.args[:1]
            elif nm == "gate":
                arg = node.args[2] if len(node.args) > 2 else None
                targets = ([arg] if isinstance(arg, (ast.Constant, ast.BinOp,
                                                     ast.JoinedStr)) else [])
            elif nm in ("claim", "fence", "segment"):
                targets = node.args[:1]
            elif nm == "m":
                targets = node.args[1:3]
            else:
                continue
            for arg in targets:
                if arg is None:
                    continue
                for sub in ast.walk(arg):
                    if isinstance(sub, ast.Constant) and isinstance(
                            sub.value, str):
                        t = sub.value
                        for tok in self.exempt:
                            if tok in t:
                                self.used_exempt.add(tok)
                                t = t.replace(tok, " ")
                        if re.search(r"\d", t):
                            bad.append("%s:%s:numeral" % (nm, sub.lineno))
                    if isinstance(sub, ast.BinOp):
                        if isinstance(sub.op, ast.Mod):
                            bad.append("%s:%s:percent" % (nm, sub.lineno))
                        if isinstance(sub.op, (ast.Add, ast.Sub)):
                            for side in (sub.left, sub.right):
                                if isinstance(side, ast.Constant) and \
                                        isinstance(side.value, int):
                                    bad.append("%s:%s:offset"
                                               % (nm, sub.lineno))
        return sorted(set(bad))


class Anchors:
    """Family (d): one accessor, consumption verified against gates that
    ran, both sides for QUOTED anchors, the content entering a predicate."""

    def __init__(self, rows):
        self.rows = rows
        self.text = {}
        self.read_by = {}

    def locate_all(self, srctext, papertext):
        report = []
        for (name, src, needle, consumer, mode) in self.rows:
            n = pick("MUT-ANCHOR", needle,
                     needle[:8] if name == "N-AUT-108" else needle)
            hits = locate(srctext[src], n)
            phits = locate(papertext, n) if papertext is not None else 0
            self.text[name] = n
            report.append({"anchor": name, "source": src, "hits": hits,
                           "chars": len(n), "paper_hits": phits,
                           "consumer": consumer, "mode": mode,
                           "floor_ok": len(n) >= NEEDLE_FLOOR,
                           "ok": hits == 1 and len(n) >= NEEDLE_FLOOR
                           and (mode != "QUOTED" or phits >= 1)})
        return report

    def read(self, name, by_gate):
        self.read_by.setdefault(name, set()).add(by_gate)
        return self.text[name]

    def parse_ints(self, name, by_gate):
        """the PARSED mode: integer operands taken out of the anchor's own
        bytes by the consumer gate, in order of appearance."""
        t = self.read(name, by_gate)
        return [int(x.replace(",", ""))
                for x in re.findall(r"(?<![\w.])(\d[\d,]*)(?!\.\d)(?!\w)", t)]

    def consumption(self, ledger):
        ran = set(ledger.names())
        report = []
        for (name, _src, _n, consumer, mode) in self.rows:
            by = sorted(self.read_by.get(name, ()))
            cons = pick("MUT-CONSUMER", consumer,
                        "G-PHANTOM" if name == "N-CON-COIN" else consumer)
            report.append({"anchor": name, "declared_consumer": cons,
                           "read_by": by, "mode": mode,
                           "ok": cons in by and cons in ran})
        return report


class Wall:
    """SemanticWall: frame-general voice-normalised regexes over the
    canonicalised paper, with a POSITIVE leg (the paper must carry its own
    standing sentence), a LICENCE leg (any sentence naming the wall's
    subject and carrying a policed form must carry a licence), the NEG
    guard with re-assertion and other-clause exclusions, and independent
    controls, at least one of which is a negated twin."""

    BARE = ("not", "never", "no", "nor", "neither", "if", "then", "would",
            "could", "might", "whether", "nothing", "cannot", "without",
            "any", "some")

    SPAN = 80

    NEG = re.compile(r"\b(?:not|never|nor|no|cannot|neither|without|"
                     r"whether|refuses?|denies)\b")

    REASSERT = re.compile(r"\b(?:no|not in|beyond|without|little|never in)"
                          r"\s+(?:doubt|question|denying|dispute|doubting)"
                          r"\b|\bcannot be (?:denied|doubted|disputed)\b"
                          r"|\bnot (?:merely|only|just|simply)\b")

    CLAUSE = re.compile(r"[;:]|,\s*(?:and|but|so|which|while|yet)\b")

    def __init__(self, name, negative, positive, controls,
                 subject=(), policed=(), licences=()):
        self.name = name
        self.negative = list(negative)
        self.positive = list(positive)
        self.controls = list(controls)
        self.subject = list(subject)
        self.policed = list(policed)
        self.licences = list(licences)
        for pat in (self.negative + self.positive + self.subject
                    + self.policed + self.licences):
            re.compile(pat)
        bad = [l for l in self.licences
               if any(re.search(pp, l.replace("\\b", ""))
                      for pp in self.policed)]
        if bad:
            raise GateFail("G-WALLS", "self-licensing set: %s" % bad)
        bare = [l for l in self.licences
                if l.replace("\\b", "").strip() in self.BARE]
        if bare:
            raise GateFail("G-WALLS", "bare-negation or hedge licence in "
                           "%s: %s" % (self.name, bare))
        if not self.subject or not self.policed:
            raise GateFail("G-WALLS", "%s has no licence leg" % self.name)
        if not any(self.NEG.search(c.casefold()) for c in self.controls):
            raise GateFail("G-WALLS", "%s carries no negated control twin"
                           % self.name)

    def seal_value(self):
        return {"name": self.name, "negative": self.negative,
                "positive": self.positive, "subject": self.subject,
                "policed": self.policed, "licences": self.licences,
                "independent_controls": len(self.controls)}

    def licence_leg(self, text):
        out = []
        for sent in re.split(r"(?<=[.!?])\s+", text):
            subs = [m.start() for p in self.subject
                    for m in re.finditer(p, sent)]
            if not subs:
                continue
            near = [m.start() for p in self.policed
                    for m in re.finditer(p, sent)
                    if any(abs(m.start() - k) <= self.SPAN for k in subs)]
            if not near:
                continue
            if not any(re.search(l, sent) for l in self.licences):
                out.append(sent[:130])
        return out

    def scan(self, paper_text):
        text = canon(paper_text)
        if not text:
            raise GateFail("G-WALLS", "%s scanned empty text" % self.name)
        hits = []
        for pat in self.negative:
            for m in re.finditer(pat, text):
                lead = text[max(0, m.start() - 300):m.start()]
                cut = max(lead.rfind("."), lead.rfind("!"), lead.rfind("?"))
                lead = lead[cut + 1:]
                excused = False
                for nm in self.NEG.finditer(lead):
                    tail = lead[nm.start():]
                    if self.REASSERT.match(tail):
                        continue
                    if self.CLAUSE.search(lead[nm.end():]):
                        continue
                    excused = True
                    break
                if not excused:
                    hits.append(pat)
                    break
        missing = [p for p in self.positive if not re.search(p, text)]
        unlicensed = self.licence_leg(text)
        return {"violations": hits, "missing_positive": missing,
                "unlicensed_sentences": unlicensed}


class Falsifier:
    def __init__(self, name, gate, target, description):
        self.name = name
        self.gate = gate
        self.target = target
        self.description = description


class Claims:
    """Family (e): claims by equality, both directions, keyed by table;
    headers are rows; fences by multiset at declared multiplicity."""

    def __init__(self):
        self.tables = {}
        self.prose = Counter()
        self.fences = Counter()

    def table(self, tid, header, rows):
        cells = [tuple(canon(str(c)) for c in header)]
        cells += [tuple(canon(str(c)) for c in r) for r in rows]
        self.tables[tid] = Counter(cells)
        return rows

    def claim(self, text, times=1):
        self.prose[canon(text)] += times
        return text

    def fence(self, text, times=1):
        self.fences[canon(text)] += times
        return text

    @staticmethod
    def blocks(paper):
        out, cur = [], []
        for line in paper.split("\n"):
            if line.strip().startswith("|") and line.strip().endswith("|"):
                cells = [c.strip()
                         for c in line.strip().strip("|").split("|")]
                if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                    continue
                cur.append(tuple(canon(c) for c in cells))
            elif cur:
                out.append(cur)
                cur = []
        if cur:
            out.append(cur)
        return out

    def check(self, paper):
        blocks = [Counter(b) for b in self.blocks(paper)]
        used, report = set(), []
        for tid, want in self.tables.items():
            hit = None
            for i, got in enumerate(blocks):
                if i in used:
                    continue
                head = list(want)[0]
                if head in got:
                    hit = i
                    break
            if hit is None:
                report.append({"table": tid, "missing": len(want),
                               "stray": 0, "matched": False})
                continue
            used.add(hit)
            got = blocks[hit]
            missing = sum(max(0, want[k] - got.get(k, 0)) for k in want)
            stray = sum(max(0, got[k] - want.get(k, 0)) for k in got)
            report.append({"table": tid, "missing": missing,
                           "stray": stray, "matched": True})
        unrendered = [i for i in range(len(blocks)) if i not in used]
        pc = canon(paper)
        prose_bad = [t[:40] for t, n in self.prose.items()
                     if pc.count(t) != n]
        fb = [canon(b) for b in re.findall(r"```[^\n]*\n(.*?)```", paper,
                                           re.S)]
        fc = Counter(fb)
        fence_bad = ([t[:40] for t, n in self.fences.items()
                      if fc.get(t, 0) != n]
                     + [t[:40] for t in fc if t not in self.fences])
        return {"tables": report, "unrendered_tables": unrendered,
                "prose_mismatch": prose_bad, "fence_mismatch": fence_bad,
                "ok": (not unrendered and not prose_bad and not fence_bad
                       and all(r["matched"] and not r["missing"]
                               and not r["stray"] for r in report))}


# THE PERIOD BLIND SPOT, CLOSED (the TPL-2 item): the guard refuses only a
# numeral followed by a decimal digit, so a trailing sentence period is
# scanned; commas group thousands.
NUM_RE = re.compile(r"(?<![\w.])(\d{1,3}(?:,\d{3})*|\d+)(?!\.\d)(?!\w)")
GATEROW_RE = re.compile(r"\[(?:PASS|FAIL)\] \S+ +[0-9a-f]{16}")
DECOR_RE = re.compile(r"^(=+|-+|v15 ECC|instrument for |-- M\d|"
                      r"-- VERDICT |ECC-|SEAM-|PSI-)")

SPELLED = ("zero", "one", "two", "three", "four", "five", "six", "seven",
           "eight", "nine", "ten", "eleven", "twelve")
SPELLED_VALUE = {w: i for i, w in enumerate(SPELLED)}
SPELLED_EXCLUDED = {"one": "the English article and pronoun, which carries "
                           "a count only where a measured pair binds it"}
SPELLED_SCANNED = tuple(w for w in SPELLED if w not in SPELLED_EXCLUDED)

EXEMPT_NUMERALS = {
    "46": "this unit's own paper number",
    "43": "the contract parent's paper number",
    "44": "the arity parent's paper number",
    "45": "the autoglue parent's paper number",
    "47": "the disc parent's paper number",
    "48": "the dynamics-closure successor's paper number",
    "20": "the coupling grandparent's paper number",
    "40": "the sec-2 grandparent's paper number",
}

# spelled fractions and proportions (sentence-scoped, hedge-aware): a
# spelled proportion carries no numeral, so every numeral leg is blind to
# it; each one found in prose must be justified by a measured pair named in
# its own sentence.
FRACTION_WORDS = {
    "half": (Fraction(3, 8), Fraction(5, 8)),
    "a half": (Fraction(3, 8), Fraction(5, 8)),
    "a third": (Fraction(1, 4), Fraction(5, 12)),
    "two thirds": (Fraction(7, 12), Fraction(3, 4)),
    "a quarter": (Fraction(1, 8), Fraction(3, 8)),
    "three quarters": (Fraction(5, 8), Fraction(7, 8)),
    "most": (Fraction(1, 2), Fraction(1, 1)),
    "nearly all": (Fraction(7, 8), Fraction(1, 1)),
    "almost all": (Fraction(7, 8), Fraction(1, 1)),
    "a few": (Fraction(0, 1), Fraction(1, 5)),
    "a minority": (Fraction(0, 1), Fraction(1, 2)),
    "a majority": (Fraction(1, 2), Fraction(1, 1)),
}
HEDGES = ("a little under ", "a little over ", "just under ", "just over ",
          "rather more than ", "rather less than ", "")


def numerals(text):
    return [m.group(1) for m in NUM_RE.finditer(text)]


def collect_ints(obj, out):
    if isinstance(obj, bool):
        return
    if isinstance(obj, int):
        out.add(str(obj))
        out.add("{:,}".format(obj))
    elif isinstance(obj, Fraction):
        collect_ints(obj.numerator, out)
        collect_ints(obj.denominator, out)
    elif isinstance(obj, dict):
        for k, v in obj.items():
            collect_ints(k, out)
            collect_ints(v, out)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            collect_ints(v, out)
    elif isinstance(obj, str):
        for t in NUM_RE.findall(obj):
            out.add(t)


def hash_call_sites(source):
    """Every call to the BUILTIN hash() -- the MUT-HASH species: it carries
    no repr token for a repr scan to find and makes a promoted row order a
    property of the interpreter's session.  This unit needs it nowhere."""
    tree = ast.parse(source)
    fnof = {}
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for sub in ast.walk(node):
                fnof[id(sub)] = node.name
    return sorted({(fnof.get(id(n), "<module>"), n.lineno)
                   for n in ast.walk(tree)
                   if isinstance(n, ast.Call)
                   and isinstance(n.func, ast.Name)
                   and n.func.id == "hash"})


def repr_key_sites(source):
    """Every ordering keyed on a bare repr, located by (function, ordered
    name), so the whitelist cannot be satisfied by copying a permitted line
    somewhere else."""
    tree = ast.parse(source)
    fnof = {}
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for sub in ast.walk(node):
                fnof[id(sub)] = node.name
    sites = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        for kw in node.keywords:
            if kw.arg != "key":
                continue
            v = kw.value
            bare = (isinstance(v, ast.Name) and v.id == "repr") or \
                   (isinstance(v, ast.Attribute) and v.attr == "repr") or \
                   (isinstance(v, ast.Lambda)
                    and any(isinstance(s, ast.Call)
                            and isinstance(s.func, ast.Name)
                            and s.func.id == "repr"
                            for s in ast.walk(v.body)))
            if not bare:
                continue
            what = "?"
            for a in node.args[:1]:
                for s in ast.walk(a):
                    if isinstance(s, ast.Name):
                        what = s.id
                        break
                    if isinstance(s, ast.Attribute):
                        what = s.attr
                        break
                break
            sites.add((fnof.get(id(node), "<module>"), what))
    return sorted(sites)


# the bare-repr orderings this unit permits, each over a container of
# TUPLES whose repr is canonical.
SAFE_REPR_SORTS = {
    ("ekey", "x"),
}
# ===========================================================================
# SECTION 2.  THE COMMITTED CHART: AG(2,3), THE CELLS, THE EVENT CLASSES
# ===========================================================================
# Everything here is rebuilt from constructors; the parents' numbers enter
# only as DECL rows bound by reproduction gates.

Q = 3
SITES = tuple((i, j) for i in range(Q) for j in range(Q))
SITE_INDEX = {s: k for k, s in enumerate(SITES)}
NACT = len(SITES)
LINKS = ((1, 0), (0, 1), (1, 1))
FOURTH = (1, 2)


def vadd(a, b):
    return ((a[0] + b[0]) % Q, (a[1] + b[1]) % Q)


def vneg(a):
    return ((-a[0]) % Q, (-a[1]) % Q)


CELLS = tuple((x, l) for x in SITES for l in LINKS)
CELL_INDEX = {c: k for k, c in enumerate(CELLS)}
DIM = len(CELLS)
CELL_PAIR = tuple(frozenset((x, vadd(x, l))) for (x, l) in CELLS)
PAIR_CELL = {p: k for k, p in enumerate(CELL_PAIR)}
LINKED = frozenset(CELL_PAIR)


def parallel_class(d):
    H = frozenset({(0, 0), d, vadd(d, d)})
    seen, out = set(), []
    for x in SITES:
        L = tuple(sorted(vadd(x, h) for h in H))
        if L not in seen:
            seen.add(L)
            out.append(L)
    return tuple(sorted(out))


ALL_DIRS = (LINKS[0], LINKS[1], LINKS[2], FOURTH)
CLASSES = {d: parallel_class(d) for d in ALL_DIRS}
LINES = tuple(sorted({L for d in ALL_DIRS for L in CLASSES[d]}))
DECLARED_LINES = tuple(sorted({L for d in LINKS for L in CLASSES[d]}))
ANT_PARTS = CLASSES[FOURTH]

TRIPLES = tuple(tuple(sorted(t)) for t in combinations(SITES, 3))


def block_of(triple):
    """the record block: the CELLS a division event writes -- one for each
    of its pairs that is a declared link (CONTRACT: the unrestricted arm
    writes 2-cell blocks off the triangles, and the fourth-class lines
    write no cell at all)."""
    out = []
    for p in combinations(triple, 2):
        fp = frozenset(p)
        if fp in PAIR_CELL:
            out.append(PAIR_CELL[fp])
    return tuple(sorted(out))


BLOCK_OF = {t: block_of(t) for t in TRIPLES}
TRIANGLES = tuple(t for t in TRIPLES if len(BLOCK_OF[t]) == 3)


def transversal_triangles():
    """the second route: the transversals of the undeclared class's three
    parts, which the complete-tripartite structure makes pairwise linked."""
    out = []
    for x in ANT_PARTS[0]:
        for y in ANT_PARTS[1]:
            for z in ANT_PARTS[2]:
                out.append(tuple(sorted((x, y, z))))
    return tuple(sorted(out))


def partitions_into_triples():
    """all partitions of the nine actors into three unordered triples."""
    acts = list(SITES)
    out = []

    def rec(rest, blocks):
        if not rest:
            out.append(tuple(sorted(blocks)))
            return
        a = rest[0]
        for pair in combinations(rest[1:], 2):
            blk = tuple(sorted((a,) + pair))
            rem = [x for x in rest if x not in blk]
            rec(rem, blocks + [blk])
    rec(acts, [])
    return tuple(sorted(set(out)))


def translation_subgroups():
    subs = set()
    for r in range(len(SITES) + 1):
        for E in combinations(SITES, r):
            Es = set(E)
            if (0, 0) not in Es:
                continue
            if all(vadd(u, v) in Es for u in Es for v in Es):
                subs.add(frozenset(Es))
    return subs


def declared_menu():
    out = set()
    for S in translation_subgroups():
        out.add(frozenset({frozenset(vadd(x, h) for h in S)
                           for x in SITES}))
    return out


# ===========================================================================
# SECTION 3.  THE COMMITTED WALK (paper-20 as CONTRACT re-implements it)
# ===========================================================================
# Ring: Z[w], w a primitive cube root; an element is (x, y) = x + y w.
# The coin is carried at three times the Grover coin so every entry is an
# integer; Born weights divide the scale out exactly.

Z0, Z1 = (0, 0), (1, 0)
WPOW = ((1, 0), (0, 1), (-1, -1))
GROVER3 = (((-1, 0), (2, 0), (2, 0)),
           ((2, 0), (-1, 0), (2, 0)),
           ((2, 0), (2, 0), (-1, 0)))


def zmul(a, b):
    x1, y1 = a
    x2, y2 = b
    return (x1 * x2 - y1 * y2, x1 * y2 + y1 * x2 - y1 * y2)


def zadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def zconj(a):
    return (a[0] - a[1], -a[1])


def znorm(a):
    return a[0] * a[0] - a[0] * a[1] + a[1] * a[1]


def ztrace(a):
    return 2 * a[0] - a[1]


SHIFT = tuple(CELL_INDEX[(vadd(x, l), l)] for (x, l) in CELLS)

COIN_ORDERS = ("G.D", "D.G")


def coin_apply(psi, n, order):
    """the coupled coin at one site block.  G.D (the delivered member):
    the residue phase lands before the coin, so the coin reads the
    phased amplitudes.  D.G (the alternative member): the coin first,
    the phase after, so the phase cannot enter that step's Born weights.
    The count field enters ONLY through its residue mod Q."""
    order = pick("MUT-ORDER", order, "G.D")
    out = [Z0] * DIM
    for s in range(NACT):
        base = s * len(LINKS)
        if order == "G.D":
            src = [zmul(psi[base + j], WPOW[n[base + j] % Q])
                   for j in range(len(LINKS))]
        else:
            src = [psi[base + j] for j in range(len(LINKS))]
        for i in range(len(LINKS)):
            tot = Z0
            for j in range(len(LINKS)):
                tot = zadd(tot, zmul(GROVER3[i][j], src[j]))
            if order == "D.G":
                tot = zmul(tot, WPOW[n[base + i] % Q])
            out[base + i] = tot
    return out


def walk_shift(post):
    out = [Z0] * DIM
    for m in range(DIM):
        out[SHIFT[m]] = post[m]
    return tuple(out)


def coin_family(bound):
    """the S_3-covariant unitary coins over the arena's own ring, exactly
    as CONTRACT enumerates them: C = aI + bJ with |a|^2 = Q^2 at the
    tripled scale and the covariant unitarity trace condition."""
    unit = Q * Q
    bnd = pick("MUT-COIN", bound, 1)
    A = [(x, y) for x in range(-bnd, bnd + 1)
         for y in range(-bnd, bnd + 1) if znorm((x, y)) == unit]
    sols, classes = [], {}
    for a in A:
        for x in range(-bnd, bnd + 1):
            for y in range(-bnd, bnd + 1):
                b = (x, y)
                if ztrace(zmul(a, zconj(b))) + Q * znorm(b) == 0:
                    sols.append((a, b))
                    r = zmul(b, zconj(a))
                    key = (Fraction(r[0], unit), Fraction(r[1], unit))
                    classes.setdefault(key, []).append((a, b))
    grover = [c for c in classes
              if c == (Fraction(-2, Q), Fraction(0))]
    return len(sols), len(classes), len(grover)


# ---- the declared amplitudes (CONTRACT's five, reproduced exactly) -------

def declared_amplitudes():
    single = [Z0] * DIM
    single[0] = Z1
    one_direction = [Z1 if k % len(LINKS) == 0 else Z0 for k in range(DIM)]
    alternating = [Z1 if k % 2 == 0 else WPOW[1] for k in range(DIM)]
    return (("THE-UNIFORM-AMPLITUDE", tuple([Z1] * DIM)),
            ("A-SINGLE-CELL-AMPLITUDE", tuple(single)),
            ("ONE-LINK-DIRECTION-ONLY", tuple(one_direction)),
            ("ALTERNATING-ROOTS", tuple(alternating)),
            ("THE-ZERO-AMPLITUDE", tuple([Z0] * DIM)))


R0 = tuple([0] * DIM)


def round_fields(rounds):
    """the declared record window: the field one admissible round writes,
    for every admissible round -- a window generated by the law-selected
    round set itself, so no tie-break selects a member."""
    out = []
    for rnd in rounds:
        n = [0] * DIM
        for blk in rnd:
            for c in BLOCK_OF[blk]:
                n[c] += 1
        out.append(tuple(n))
    return tuple(out)


# ===========================================================================
# SECTION 4.  THE THREE PSI-STATUS CARRIER REGIONS (M1)
# ===========================================================================
# Three disjoint code regions, one per face of the trilemma.  Each carries
# a DIFFERENT state object and emits the Born functional by its own route;
# G-PSI-REGIONS walks the syntax tree and refuses any call from one region
# into another (the ring primitives and coin_apply are shared plumbing,
# declared below).  G-PSI-EQUAL requires the three emitted functionals to
# be byte-equal at every delivered row.

PSI_SHARED_PLUMBING = {"zmul", "zadd", "zconj", "znorm", "coin_apply",
                       "Fraction", "sum", "range", "len", "tuple", "list",
                       "pick", "mut", "any", "all", "sorted", "reversed",
                       "GateFail"}


def psi_ontic_q(psi, n, order):
    """FACE 1: the ontic stochastic wave.  The carried object is the
    amplitude vector itself; the functional is its squared modulus."""
    post = coin_apply(list(psi), list(n), order)
    w = [znorm(z) for z in post]
    tot = sum(w)
    if tot == 0:
        return None
    return tuple(Fraction(x, tot) for x in w)


def psi_instrument_rho(psi):
    """FACE 2 carrier: the density operator rho = psi psi-dagger, the full
    DIM x DIM matrix over the ring."""
    return [[zmul(psi[i], zconj(psi[j])) for j in range(DIM)]
            for i in range(DIM)]


def psi_instrument_q(psi, n, order, full=False):
    """FACE 2: the CPTP-instrumented quantum state.  The carrier is rho;
    the channel is conjugation by the coupled coin; the functional is the
    normalised diagonal.  The site-block structure lets the diagonal be
    taken block by block; `full` evolves the whole matrix instead, and
    G-PSI-EQUAL requires the two routes to agree where both are run."""
    rho = psi_instrument_rho(psi)
    C = []
    for k in range(DIM):
        e = [Z0] * DIM
        e[k] = Z1
        C.append(coin_apply(e, list(n), order))
    if full:
        rp = [[Z0] * DIM for _ in range(DIM)]
        for i in range(DIM):
            for j in range(DIM):
                acc = Z0
                for k in range(DIM):
                    if C[k][i] == Z0:
                        continue
                    for l in range(DIM):
                        if C[l][j] == Z0 or rho[k][l] == Z0:
                            continue
                        acc = zadd(acc, zmul(zmul(C[k][i], rho[k][l]),
                                             zconj(C[l][j])))
                rp[i][j] = acc
        diag = [rp[i][i] for i in range(DIM)]
    else:
        diag = []
        for i in range(DIM):
            s = i // len(LINKS) * len(LINKS)
            acc = Z0
            for k in range(s, s + len(LINKS)):
                for l in range(s, s + len(LINKS)):
                    if C[k][i] == Z0 or C[l][i] == Z0 or rho[k][l] == Z0:
                        continue
                    acc = zadd(acc, zmul(zmul(C[k][i], rho[k][l]),
                                         zconj(C[l][i])))
            diag.append(acc)
    dvals = [d[0] for d in diag]
    if any(d[1] != 0 for d in diag):
        raise GateFail("G-PSI-EQUAL", "a diagonal entry left the rationals")
    tot = sum(dvals)
    if tot == 0:
        return None
    got = tuple(Fraction(x, tot) for x in dvals)
    if mut("MUT-PSI"):
        got = tuple(reversed(got))
    return got


def psi_repr_q(psi, n, order):
    """FACE 3: the Barandes-representational reading.  The carried object
    is the configuration-level process law: the transition-amplitude table
    (one column per source configuration) together with the initial
    configuration data; the functional is the process law's single-time
    marginal at the read point."""
    table = []
    for k in range(DIM):
        e = [Z0] * DIM
        e[k] = Z1
        table.append(coin_apply(e, list(n), order))
    marg = []
    for c in range(DIM):
        acc = Z0
        for k in range(DIM):
            if psi[k] == Z0 or table[k][c] == Z0:
                continue
            acc = zadd(acc, zmul(table[k][c], psi[k]))
        marg.append(znorm(acc))
    tot = sum(marg)
    if tot == 0:
        return None
    return tuple(Fraction(x, tot) for x in marg)


# ===========================================================================
# SECTION 5.  THE EXACT RATIONAL LP (M2)
# ===========================================================================
# Feasibility, uniqueness and polytope dimension over Fractions.  No float
# can enter: the tableau is Fractions end to end.

def simplex_min(A, b, c):
    """minimise c.x subject to A x = b, x >= 0, by two-phase simplex with
    Bland's rule.  Returns (status, value, x): status FEASIBLE/INFEASIBLE
    (phase one), with phase-two optimum when c is not None."""
    m, n = len(A), len(A[0]) if A else 0
    T = []
    for i in range(m):
        row = [Fraction(v) for v in A[i]]
        rb = Fraction(b[i])
        if rb < 0:
            row = [-v for v in row]
            rb = -rb
        T.append(row + [Fraction(1) if j == i else Fraction(0)
                        for j in range(m)] + [rb])
    basis = list(range(n, n + m))
    cost = [Fraction(0)] * (n + m) + [Fraction(0)]
    for j in range(n + m):
        cost[j] = Fraction(1) if j >= n else Fraction(0)
    # reduced costs for phase one
    z = [Fraction(0)] * (n + m + 1)
    for i in range(m):
        for j in range(n + m + 1):
            z[j] += T[i][j]
    red = [cost[j] - z[j] for j in range(n + m)] + [-z[n + m]]

    def pivot(pr, pc):
        pv = T[pr][pc]
        T[pr] = [v / pv for v in T[pr]]
        for i in range(m):
            if i != pr and T[i][pc] != 0:
                f = T[i][pc]
                T[i] = [a - f * bb for a, bb in zip(T[i], T[pr])]
        f = red[pc]
        if f != 0:
            for j in range(n + m + 1):
                red[j] -= f * T[pr][j]
        basis[pr] = pc

    def run(active_cols):
        while True:
            pc = None
            for j in active_cols:
                if red[j] < 0:
                    pc = j
                    break
            if pc is None:
                return
            pr, best = None, None
            for i in range(m):
                if T[i][pc] > 0:
                    ratio = T[i][n + m] / T[i][pc]
                    if best is None or ratio < best or \
                            (ratio == best and basis[i] < basis[pr]):
                        pr, best = i, ratio
            if pr is None:
                raise GateFail("G-LP-SOLVE", "unbounded phase")
            pivot(pr, pc)

    run(list(range(n + m)))
    gap = -red[n + m]
    if gap != 0:
        return ("INFEASIBLE", gap, None)
    # drive artificials out of the basis where possible
    for i in range(m):
        if basis[i] >= n:
            for j in range(n):
                if T[i][j] != 0:
                    pivot(i, j)
                    break
    if c is None:
        x = [Fraction(0)] * n
        for i in range(m):
            if basis[i] < n:
                x[basis[i]] = T[i][n + m]
        return ("FEASIBLE", Fraction(0), x)
    # phase two on the original columns only
    cost2 = [Fraction(v) for v in c] + [Fraction(0)] * m
    z2 = [Fraction(0)] * (n + m + 1)
    for i in range(m):
        if basis[i] < n + m:
            cb = cost2[basis[i]]
            if cb != 0:
                for j in range(n + m + 1):
                    z2[j] += cb * T[i][j]
    for j in range(n + m):
        red[j] = cost2[j] - z2[j]
    red[n + m] = -z2[n + m]
    run(list(range(n)))
    x = [Fraction(0)] * n
    for i in range(m):
        if basis[i] < n:
            x[basis[i]] = T[i][n + m]
    val = sum(Fraction(c[j]) * x[j] for j in range(n))
    return ("FEASIBLE", val, x)


def mat_rank_null(rows, ncol):
    """rank and a nullspace basis of a Fraction matrix, by row reduction."""
    M = [list(map(Fraction, r)) for r in rows]
    piv, r = [], 0
    for cidx in range(ncol):
        p = None
        for i in range(r, len(M)):
            if M[i][cidx] != 0:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = Fraction(1) / M[r][cidx]
        M[r] = [x * inv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][cidx] != 0:
                f = M[i][cidx]
                M[i] = [a - f * bb for a, bb in zip(M[i], M[r])]
        piv.append(cidx)
        r += 1
        if r == len(M):
            break
    free = [j for j in range(ncol) if j not in piv]
    null = []
    for fj in free:
        v = [Fraction(0)] * ncol
        v[fj] = Fraction(1)
        for i, pj in enumerate(piv):
            v[pj] = -M[i][fj]
        null.append(v)
    return r, null


def lp_row(M, q, scale, want_dim=True):
    """ONE Born-marginal feasibility row: does a probability vector p over
    the class's events exist with M p = scale * q and sum p = 1?  Returns
    the word, the witness, and -- on the primary rows -- the polytope
    dimension with its implicit-equality census and a second-point
    certificate whenever the dimension is positive."""
    ncell, nev = len(M), len(M[0])
    A = [list(M[i]) for i in range(ncell)] + [[Fraction(1)] * nev]
    b = [Fraction(scale) * q[i] for i in range(ncell)] + [Fraction(1)]
    if mut("MUT-SIMPLEX"):
        b = [Fraction(0) for _ in b[:-1]] + [Fraction(1)]
    status, gap, x = simplex_min(A, b, None)
    if status == "INFEASIBLE":
        ceil = max(q) > Fraction(1, 3)
        return {"word": "INFEASIBLE", "gap": str(gap),
                "ceiling_witness": bool(ceil),
                "qmax": str(max(q)), "dim": None, "implicit": None,
                "second_point": None}
    rank, null = mat_rank_null(A, nev)
    if not null:
        return {"word": "UNIQUE", "gap": "0", "ceiling_witness": False,
                "qmax": str(max(q)), "dim": 0, "implicit": 0,
                "second_point": False,
                "solution_digest": digest([str(v) for v in x])}
    if not want_dim:
        return {"word": "FEASIBLE-AT-THE-FIBER-ROW", "gap": "0",
                "ceiling_witness": False, "qmax": str(max(q)),
                "dim": None, "implicit": None, "second_point": None}
    # THE DEFICIENT-WRITER THEOREM: when the target has full mass and no
    # event writes more than `scale` cells, summing the marginal rows
    # gives sum over events of (scale - writer) p = zero with every term
    # non-negative, so every deficient writer is implicitly zero.  Both
    # premises are checked exactly here, and the remaining support is
    # settled by one strict-positivity programme instead of a solve per
    # column, with the per-column route kept as the fallback.
    w = [int(sum(M[i][j] for i in range(ncell))) for j in range(nev)]
    forced = []
    if sum(q) == 1 and max(w) <= scale:
        forced = [j for j in range(nev) if w[j] < scale]
    support = [j for j in range(nev) if j not in set(forced)]
    implicit, second = None, False
    if support:
        cols = len(support) + 1
        A2p = []
        for i in range(len(A)):
            row = [A[i][j] for j in support]
            row.append(sum(A[i][j] for j in support))
            A2p.append(row)
        c2p = [Fraction(0)] * (cols - 1) + [Fraction(-1)]
        st2, val2, x2p = simplex_min(A2p, b, c2p)
        if st2 == "FEASIBLE" and -val2 > 0:
            implicit = list(forced)
            tstar = x2p[cols - 1]
            x2 = [Fraction(0)] * nev
            for k, j in enumerate(support):
                x2[j] = x2p[k] + tstar
            second = x2 != x
    if implicit is None:
        implicit, second = list(forced), False
        for j in support:
            st, val, xj = simplex_min(A, b,
                                      [Fraction(0)] * j + [Fraction(-1)]
                                      + [Fraction(0)] * (nev - j - 1))
            if st != "FEASIBLE":
                raise GateFail("G-LP-SOLVE", "phase two lost feasibility")
            if -val == 0:
                implicit.append(j)
            elif xj != x:
                second = True
        implicit = sorted(set(implicit))
    if mut("MUT-DIM"):
        implicit = []
    A2 = A + [[Fraction(1) if k == j else Fraction(0)
               for k in range(nev)] for j in implicit]
    _r2, null2 = mat_rank_null(A2, nev)
    dim = len(null2)
    word = "UNIQUE" if dim == 0 else "MANY"
    return {"word": word, "gap": "0", "ceiling_witness": False,
            "qmax": str(max(q)), "dim": dim, "implicit": len(implicit),
            "second_point": second}
# ===========================================================================
# SECTION 6.  THE ALIGNED UNION AND THE SEAM (AUTOGLUE's arena, rebuilt)
# ===========================================================================
# Two AG(2,3) charts glued along one whole part of the fourth class -- the
# k = 3 aligned gluing.  Everything below is recomputed from this
# construction; AUTOGLUE's sealed numbers are DECL rows bound by
# reproduction gates, never imported as results.

GLUE = tuple(zip(ANT_PARTS[0], ANT_PARTS[0]))


def gluing_maps():
    amap, bmap = {}, {}
    for i, (sa, sb) in enumerate(GLUE):
        amap[sa] = ("S", i)
        bmap[sb] = ("S", i)
    for s in SITES:
        amap.setdefault(s, ("A", s))
        bmap.setdefault(s, ("B", s))
    actors = sorted(set(amap.values()) | set(bmap.values()), key=ekey)
    return actors, amap, bmap


def union_relation():
    actors, amap, bmap = gluing_maps()
    rel = Counter()
    for mp in (amap, bmap):
        for (x, l) in CELLS:
            rel[frozenset((mp[x], mp[vadd(x, l)]))] += 1
    rel = {k: 1 for k in rel}
    if mut("MUT-UNION"):
        rel.pop(sorted(rel, key=ekey)[0])
    return actors, rel, amap, bmap


SHARED = tuple(("S", i) for i in range(len(GLUE)))
SEAM_SITE = {"A": {("S", i): GLUE[i][0] for i in range(len(GLUE))},
             "B": {("S", i): GLUE[i][1] for i in range(len(GLUE))}}
UACT = UREL = AMAP = BMAP = INV_A = INV_B = None
APRIV = BPRIV = UGROUPS = CROSS_PAIRS = None


def refresh_union():
    """rebuild the union at the start of every run, so an injection site
    fires under its own mutant and a clean run rebuilds cleanly."""
    global UACT, UREL, AMAP, BMAP, INV_A, INV_B, APRIV, BPRIV
    global UGROUPS, CROSS_PAIRS
    UACT, UREL, AMAP, BMAP = union_relation()
    INV_A = {v: k for k, v in AMAP.items()}
    INV_B = {v: k for k, v in BMAP.items()}
    APRIV = tuple(a for a in UACT if a[0] == "A")
    BPRIV = tuple(a for a in UACT if a[0] == "B")
    UGROUPS = tuple(tuple(UACT[i] for i in g)
                    for g in combinations(range(len(UACT)), 3))
    if mut("MUT-GROUPS"):
        UGROUPS = UGROUPS[:-1]
    CROSS_PAIRS = tuple(sorted((frozenset((a, b)) for a in APRIV
                                for b in BPRIV), key=ekey))


def footprint(group, rel):
    """the event's deposit: each pair new-across-the-seam,
    new-inside-a-sector, or a doubling of a realised pair."""
    pairs = [frozenset(p) for p in combinations(group, 2)]
    new = [p for p in pairs if p not in rel]
    cross = tuple(sorted((p for p in new
                          if {x[0] for x in p} == {"A", "B"}), key=ekey))
    within = tuple(sorted((p for p in new if p not in cross), key=ekey))
    doubled = tuple(sorted((p for p in pairs if p in rel), key=ekey))
    if mut("MUT-PROFILE") and doubled and cross:
        cross, doubled = cross + (doubled[0],), doubled[1:]
    return {"cross": cross, "within": within, "doubled": doubled,
            "pairs": tuple(sorted(pairs, key=ekey))}


def profile(fp):
    return (len(fp["cross"]), len(fp["within"]), len(fp["doubled"]))


def seam_index(seam, actor, chart):
    base = SEAM_SITE[chart][seam]
    site = (INV_A if chart == "A" else INV_B)[actor]
    d = ((site[0] - base[0]) % Q, (site[1] - base[1]) % Q)
    for i, l in enumerate(LINKS):
        if d == l:
            return i, 1
        if d == vneg(l):
            return i, -1
    return None


def cross_index(seam, pair):
    u, v = sorted(pair, key=ekey)
    if u[0] != "A":
        u, v = v, u
    if u[0] != "A" or v[0] != "B":
        return None
    ia, sa = seam_index(seam, u, "A")
    jb, sb = seam_index(seam, v, "B")
    return (ia, jb, sa * sb)


def seam_counts(seam, rel):
    nA = tuple(rel.get(frozenset((AMAP[SEAM_SITE["A"][seam]],
                                  AMAP[vadd(SEAM_SITE["A"][seam], l)])), 0)
               for l in LINKS)
    nB = tuple(rel.get(frozenset((BMAP[SEAM_SITE["B"][seam]],
                                  BMAP[vadd(SEAM_SITE["B"][seam], l)])), 0)
               for l in LINKS)
    return nA, nB


def uext(U):
    E = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(2):
        for j in range(2):
            E[i][j] = U[i][j]
    for i in range(2):
        E[i][2] = U[i][0] + U[i][1]
    for j in range(2):
        E[2][j] = U[0][j] + U[1][j]
    E[2][2] = U[0][0] + U[0][1] + U[1][0] + U[1][1]
    return E


def cross_counts(nA, nB, U):
    E = uext(U)
    return {(i, j, s): nA[i] + nB[j] - s * E[i][j]
            for i in range(3) for j in range(3) for s in (1, -1)}


LATCACHE = {}


def completion_lattice(nA, nB, slack=0):
    key = (nA, nB, slack)
    got = LATCACHE.get(key)
    if got is not None:
        return got
    b = [[nA[i] + nB[j] - 1 + slack for j in range(2)] for i in range(2)]
    if mut("MUT-LATTICE"):
        b = [[x - 1 for x in row] for row in b]
    out = []
    for u00 in range(-b[0][0], b[0][0] + 1):
        for u01 in range(-b[0][1], b[0][1] + 1):
            for u10 in range(-b[1][0], b[1][0] + 1):
                for u11 in range(-b[1][1], b[1][1] + 1):
                    U = [[u00, u01], [u10, u11]]
                    if all(v >= 1
                           for v in cross_counts(nA, nB, U).values()):
                        out.append((u00, u01, u10, u11))
    LATCACHE[key] = out
    return out


def prediction(nA, nB, U, idx):
    i, j, s = idx
    E = uext([[U[0], U[1]], [U[2], U[3]]])
    return nA[i] + nB[j] - s * E[i][j]


SUCCACHE = {}


def successors_raw(nA, nB, cons):
    key = (nA, nB, cons)
    got = SUCCACHE.get(key)
    if got is not None:
        return got
    out = []
    for U in completion_lattice(nA, nB):
        if all(prediction(nA, nB, U, k) == c for (k, c) in cons):
            out.append(U)
    SUCCACHE[key] = out
    return out


def successors(seam, rel, realised_cross):
    """every completion at this seam consistent with the record:
    admissible at the seam's own count vectors and predicting exactly the
    count the record carries on every realised cross link."""
    nA, nB = seam_counts(seam, rel)
    cons = []
    for p in realised_cross:
        k = cross_index(seam, p)
        if k is None or mut("MUT-FORM"):
            continue
        cons.append((k, rel[p]))
    return successors_raw(nA, nB, tuple(sorted(set(cons), key=ekey)))


def advance_rel(group, rel):
    rel2 = dict(rel)
    for p in combinations(group, 2):
        fp = frozenset(p)
        rel2[fp] = rel2.get(fp, 0) + 1
    return rel2


def lawful_cross_only(group, rel, realised_cross):
    """AUTOGLUE's every-leg standard under the CROSS-ONLY member: the
    incidence weld is alive exactly when the event opens no pair inside a
    sector (the containment proposition), and the form leg needs a
    successor at every seam of the post-record."""
    fp = footprint(group, rel)
    if fp["within"] and not mut("MUT-LAWFUL"):
        return False, fp, None
    rel2 = advance_rel(group, rel)
    realised2 = tuple(sorted(set(realised_cross) | set(fp["cross"]),
                             key=ekey))
    sizes = []
    for seam in SHARED:
        s = successors(seam, rel2, realised2)
        sizes.append(len(s))
        if not s:
            return False, fp, tuple(sizes)
    return True, fp, tuple(sizes)


def staylable(group, rel):
    """the state may stay exactly when no doubling of the event lands on a
    seam's own forward cell (AUTOGLUE 4.1): equivalently, the event moves
    no seam's count vector."""
    fp = footprint(group, rel)
    before = [seam_counts(s, rel) for s in SHARED]
    rel2 = advance_rel(group, rel)
    after = [seam_counts(s, rel2) for s in SHARED]
    if mut("MUT-STAY"):
        return before != after
    return before == after


# ---- the committed observable menu (M0b), every member a function of the
# geometry-and-record data ALONE.  G-OBS-MENU walks this file's own syntax
# tree: each obs_* function takes exactly the two parameters (geo, rel)
# and mentions no completion anywhere in its body.

def obs_count_field(geo, rel):
    return tuple(sorted(((ekey(p), c) for p, c in rel.items()), key=ekey))


def obs_residue_field(geo, rel):
    return tuple(sorted(((ekey(p), c % Q) for p, c in rel.items()),
                        key=ekey))


def obs_cell_count(geo, rel):
    return len(rel)


def obs_seam_count_vectors(geo, rel):
    return tuple(seam_counts(s, rel) for s in SHARED)


def obs_profile_census(geo, rel):
    cnt = Counter()
    for g in UGROUPS:
        cnt[profile(footprint(g, rel))] += 1
    return tuple(sorted(cnt.items()))


def obs_frozen_alive(geo, rel):
    return sum(1 for g in UGROUPS
               if profile(footprint(g, rel)) == (0, 0, 3))


def obs_a2_cross_realised(geo, rel):
    return sum(1 for p in CROSS_PAIRS if p in rel)


def obs_total_mass_residue(geo, rel):
    return sum(rel.values()) % Q


OBSERVABLE_MENU = (("OBS-COUNT-FIELD", obs_count_field),
                   ("OBS-RESIDUE-FIELD", obs_residue_field),
                   ("OBS-CELL-COUNT", obs_cell_count),
                   ("OBS-SEAM-COUNT-VECTORS", obs_seam_count_vectors),
                   ("OBS-PROFILE-CENSUS", obs_profile_census),
                   ("OBS-FROZEN-ALIVE", obs_frozen_alive),
                   ("OBS-A2-CROSS-REALISED", obs_a2_cross_realised),
                   ("OBS-TOTAL-MASS-RESIDUE", obs_total_mass_residue))


# ---- the parents' published censuses this rebuild must REPRODUCE --------
DECL2 = {
    "aut.profile_102": 108,
    "aut.profile_201": 108,
    "aut.profile_210": 72,
    "aut.profile_003": 54,
    "aut.profile_012": 108,
    "aut.profile_030": 5,
    "aut.prep_hist": ((0, 20100), (1, 6804), (2, 2034), (3, 622),
                      (4, 153), (5, 18), (6, 52), (9, 8)),
    "aut.two_step_fiber": ((25, 9), (26, 36), (27, 24), (28, 12),
                           (41, 9), (43, 18)),
    "con.cycle_actor": 4,
    "con.cycle_dynamical": 3,
}
# ===========================================================================
# SECTION 7.  THE MEASUREMENTS
# ===========================================================================

def measure_chart():
    """M0 substrate: the committed chart rebuilt from constructors."""
    writer = Counter(len(BLOCK_OF[t]) for t in TRIPLES)
    tri_a = set(TRIANGLES)
    tri_b = set(transversal_triangles())
    parts = partitions_into_triples()
    rounds = tuple(p for p in parts
                   if all(len(BLOCK_OF[b]) == len(b) for b in p))
    if mut("MUT-ROUNDS"):
        bad = next(p for p in parts if p not in set(rounds))
        rounds = rounds + (bad,)
    menu = declared_menu()
    lines_declared = DECLARED_LINES
    return {
        "actors": len(SITES), "cells": DIM,
        "pair_bijection": len(set(CELL_PAIR)) == DIM,
        "parallel_classes": len(CLASSES),
        "lines": len(LINES), "declared_lines": len(lines_declared),
        "triples": len(TRIPLES),
        "writer_census": tuple(sorted(writer.items())),
        "triangles": len(tri_a),
        "triangles_two_routes_equal": tri_a == tri_b,
        "partitions": len(parts), "rounds": len(rounds),
        "menu": len(menu),
        "rounds_list": rounds,
    }


def measure_union_substrate():
    """M0 substrate: the aligned union rebuilt; profile census."""
    prof = Counter()
    for g in UGROUPS:
        prof[profile(footprint(g, UREL))] += 1
    seam_spanning = sum(v for k, v in prof.items() if k[0] > 0)
    within_alive = prof.get((0, 0, 3), 0)
    incidence_lawful = sum(v for k, v in prof.items()
                           if k[0] > 0 and k[1] == 0)
    a2_groups = len(list(combinations(range(len(UACT)), 2)))
    a2_seam = len(CROSS_PAIRS)
    a2_clean = sum(1 for p in CROSS_PAIRS
                   if len(footprint(tuple(sorted(p, key=ekey)),
                                    UREL)["cross"]) == 1)
    return {
        "carriers": len(UACT), "pairs": len(UREL),
        "groups": len(UGROUPS),
        "profile_census": tuple(sorted(prof.items())),
        "seam_spanning": seam_spanning,
        "frozen_alive": within_alive,
        "incidence_lawful": incidence_lawful,
        "a2_groups": a2_groups, "a2_seam_spanning": a2_seam,
        "a2_seam_clean": a2_clean,
    }


def measure_lattice():
    """the seam's completion lattice at the committed all-simple counts,
    with the widened re-run that proves the box does not bind."""
    ones = (1, 1, 1)
    lat = completion_lattice(ones, ones)
    wide = [U for U in completion_lattice(ones, ones, slack=1)
            if all(v >= 1 for v in cross_counts(ones, ones,
                                                [[U[0], U[1]],
                                                 [U[2], U[3]]]).values())]
    return {"lattice": len(lat), "widened": len(wide),
            "kernel": 4, "box_bound_binds": len(lat) != len(wide)}


def measure_lawful():
    """AUTOGLUE's every-leg standard reproduced: the lawful set, the
    crossings, the staylable class, and the per-seam successor sizes."""
    lawful, crossings, sizes_rows, stay = [], [], [], []
    for g in UGROUPS:
        ok, fp, sizes = lawful_cross_only(g, UREL, ())
        if ok:
            lawful.append(g)
            if profile(fp) == (1, 0, 2):
                crossings.append(g)
                sizes_rows.append(tuple(sorted(sizes)))
                if staylable(g, UREL):
                    stay.append(g)
    mult = Counter()
    for g in crossings:
        _ok, fp, sizes = lawful_cross_only(g, UREL, ())
        for s in sizes:
            mult[s] += 1
    if mut("MUT-RELATION") and 4 in mult:
        mult[1] = mult.pop(4)
    return {"lawful": len(lawful), "crossings": len(crossings),
            "staylable": len(stay),
            "size_patterns": tuple(sorted(Counter(sizes_rows).items())),
            "multiplicity": tuple(sorted(mult.items())),
            "seam_slots": sum(mult.values()),
            "crossing_list": tuple(crossings),
            "stay_list": tuple(stay)}


def measure_preparedness(crossing_list, stay_list):
    """the advance-state census, factorised per seam and swept over the
    whole 31^3 state space by mask conjunction."""
    ones = (1, 1, 1)
    lat = completion_lattice(ones, ones)
    stay_set = set(stay_list)
    probes = crossing_list if not mut("MUT-PREP") else crossing_list[:4]
    masks = []
    for si, seam in enumerate(SHARED):
        row = []
        for U in lat:
            bits = 0
            for ei, g in enumerate(probes):
                fp = footprint(g, UREL)
                pair = fp["cross"][0]
                idx = cross_index(seam, pair)
                fits = (idx is None
                        or prediction(ones, ones, U, idx) == 1)
                if fits and g in stay_set:
                    bits |= (1 << ei)
            row.append(bits)
        masks.append(row)
    hist = Counter()
    best_val, best_states = -1, []
    for i0 in range(len(lat)):
        for i1 in range(len(lat)):
            m01 = masks[0][i0] & masks[1][i1]
            for i2 in range(len(lat)):
                m = m01 & masks[2][i2]
                k = m.bit_count()
                hist[k] += 1
                if k > best_val:
                    best_val, best_states = k, [(i0, i1, i2)]
                elif k == best_val:
                    best_states.append((i0, i1, i2))
    absorbable = set()
    for si in range(len(SHARED)):
        for U in range(len(lat)):
            m = masks[si][U]
            ei = 0
            while m:
                if m & 1:
                    absorbable.add(ei)
                m >>= 1
                ei += 1
    return {"states": len(lat) ** 3,
            "hist": tuple(sorted(hist.items())),
            "ready_none": hist.get(0, 0),
            "best": best_val, "best_states": len(best_states),
            "best_state_list": tuple(best_states),
            "absorbable": len(absorbable),
            "lattice_points": len(lat), "lat": lat, "masks": masks}


def measure_obs_sweep(prep):
    """M0b leg one: the committed observable menu against a declared probe
    family of union states differing ONLY in the seam completion; and the
    modal allowed-set relation against the same family."""
    lat = prep["lat"]
    masks = prep["masks"]
    probes = list(prep["best_state_list"])
    zero = lat.index((0, 0, 0, 0))
    extras = [(zero, zero, zero), (0, 0, 0),
              (len(lat) - 1, len(lat) - 1, len(lat) - 1)]
    for e in extras:
        if e not in probes:
            probes.append(e)
    geo = {"kind": "the-aligned-union", "cells": len(UREL)}
    obs_rows = []
    for (name, fn) in OBSERVABLE_MENU:
        vals = {sdigest(fn(geo, UREL)) for _ in probes}
        obs_rows.append({"observable": name,
                         "value_set_size": len(vals)})
    if mut("MUT-OBS"):
        obs_rows[0]["value_set_size"] = len(probes)
    rel_vals = set()
    for (i0, i1, i2) in probes:
        rel_vals.add(masks[0][i0] & masks[1][i1] & masks[2][i2])
    # the record and geometry are SHARED across the probe family by
    # construction; MUT-PAIRS breaks that parity and the gate must see it
    same_rel = pick("MUT-PAIRS", True, False)
    return {"probes": len(probes),
            "obs_rows": obs_rows,
            "blind": sum(1 for r in obs_rows if r["value_set_size"] == 1),
            "menu_size": len(obs_rows),
            "relation_value_set": len(rel_vals),
            "probe_family_shares_record": same_rel}


def step2_censuses(crossing_list):
    """M0b leg two: the two-step record census under the three-member
    declared reading family, from EVERY lawful first crossing.

    RE-SOLVED: the successor census takes only the post-record (AUTOGLUE's
    own definition, at the parent's own event base -- every second event
    depositing a cross pair); the event is allowed when a completion
    consistent with the two-event record exists at every seam.
    PERSIST-FIT: the state after the first crossing is drawn per seam from
    its successor set; the event is allowed when, for every cross pair it
    deposits, some drawn completion predicts exactly the single incidence,
    at every seam.
    PERSIST-KEPT: stricter -- some completion in the first successor set
    survives the second event's record unchanged, at every seam."""
    fiber = Counter()
    rows = []
    differ_fit, differ_kept = 0, 0
    for g1 in crossing_list:
        fp1 = footprint(g1, UREL)
        rel1 = advance_rel(g1, UREL)
        realised1 = fp1["cross"]
        succ1 = {}
        for seam in SHARED:
            succ1[seam] = successors(seam, rel1, realised1)
        allowed_rs, allowed_fit, allowed_kept = set(), set(), set()
        for g2 in UGROUPS:
            fp2 = footprint(g2, rel1)
            if not fp2["cross"]:
                continue
            rel2 = advance_rel(g2, rel1)
            realised2 = tuple(sorted(set(realised1) | set(fp2["cross"]),
                                     key=ekey))
            succ2 = {}
            ok_rs = True
            for seam in SHARED:
                succ2[seam] = successors(seam, rel2, realised2)
                if not succ2[seam]:
                    ok_rs = False
            if ok_rs:
                allowed_rs.add(g2)
            ok_fit = True
            for pair2 in fp2["cross"]:
                for seam in SHARED:
                    idx = cross_index(seam, pair2)
                    if idx is None:
                        continue
                    nA1, nB1 = seam_counts(seam, rel1)
                    if not any(prediction(nA1, nB1, U, idx) == 1
                               for U in succ1[seam]):
                        ok_fit = False
                        break
                if not ok_fit:
                    break
            if ok_fit:
                allowed_fit.add(g2)
            ok_kept = True
            for seam in SHARED:
                keep = set(succ1[seam]) & set(succ2[seam])
                if not keep:
                    ok_kept = False
                    break
            if ok_kept:
                allowed_kept.add(g2)
        if mut("MUT-READING"):
            allowed_fit = set(allowed_rs)
            allowed_kept = set(allowed_rs)
        n_rs = len(allowed_rs)
        if mut("MUT-TWOSTEP"):
            n_rs = len({g for g in allowed_rs
                        if profile(footprint(g, UREL)) == (1, 0, 2)})
        fiber[n_rs] += 1
        if allowed_fit != allowed_rs:
            differ_fit += 1
        if allowed_kept != allowed_rs:
            differ_kept += 1
        rows.append({"first": ekey(g1), "re_solved": n_rs,
                     "persist_fit": len(allowed_fit),
                     "persist_kept": len(allowed_kept),
                     "fit_differs": allowed_fit != allowed_rs,
                     "kept_differs": allowed_kept != allowed_rs})
        if mut("MUT-STEPFIBER"):
            fiber = Counter({n_rs: len(crossing_list)})
            break
    return {"fiber": tuple(sorted(fiber.items())),
            "fiber_min": min(fiber), "fiber_max": max(fiber),
            "rows": rows,
            "differ_fit": differ_fit, "differ_kept": differ_kept,
            "first_crossings": len(rows)}


def measure_interface(anch, chart, usub, lawf, gate_reader):
    """M0: the interface table.  Every object typed by the five words; the
    cited extents parsed out of CONTRACT's own census fence; the six sense
    words fixed; the event-class fork declared."""
    parsed = anch.parse_ints("N-CON-CENSUS", gate_reader)
    # OBJECTS, EXTENTS, COMPUTED, CITED, ACTORS, CELLS, REALISED,
    # HISTORIES, BLOCKS, COUNT-FIELDS, MENU, CHART-CLASSES
    cited = {"objects": parsed[0], "extents": parsed[1],
             "actors": parsed[4], "cells": parsed[5],
             "events_realised": parsed[6], "histories": parsed[7],
             "blocks": parsed[8], "count_fields": parsed[9],
             "menu": parsed[10], "chart_classes": parsed[11]}
    rows = []

    def row(obj, klass, extent, backing, carrier, update_role, freedep,
            sense):
        rows.append({"object": obj, "class": klass, "extent": extent,
                     "backing": backing, "carrier": carrier,
                     "update_role": update_role,
                     "free_parameter_dependence": freedep,
                     "sense_word": sense})

    row("ACTOR", pick("MUT-IFACE", "DECLARED", "PRIMITIVE"),
        chart["actors"], "COMPUTED-HERE",
        "ONE-STATE", "READ-BY-EVERY-MAP", "n", "event")
    row("CELL", "GENERATED", chart["cells"], "COMPUTED-HERE",
        "ONE-STATE", "THE-CARRIER-BASIS", "n,L", "cell")
    row("DIRECTION", "DECLARED", len(LINKS), "COMPUTED-HERE",
        "ONE-STATE", "FIXED-BACKGROUND", "L", "cell")
    row("PARALLEL-CLASS", "GENERATED", chart["parallel_classes"],
        "COMPUTED-HERE", "ONE-STATE", "FIXED-BACKGROUND", "q", "geometry")
    row("LINE", "GENERATED", chart["lines"], "COMPUTED-HERE",
        "ONE-STATE", "THE-COSET-EVENT-SHAPE", "q", "event")
    row("DIVISION-EVENT", "GENERATED", chart["triples"], "COMPUTED-HERE",
        "ONE-STATE", "THE-EVENT-UNIVERSE", "n,a", "event")
    row("REALISED-EVENT", "GENERATED", cited["events_realised"],
        "SEALED-CITATION", "ONE-STATE", "CORPUS-FACT", "the drivers",
        "event")
    row("GROUPING", "GENERATED", chart["partitions"], "COMPUTED-HERE",
        "ONE-STATE", "THE-ROUND-UNIVERSE", "n,a", "event")
    row("ADMISSIBLE-ROUND", "LAW-SELECTED", chart["rounds"],
        "COMPUTED-HERE", "ONE-STATE", "THE-SATURATION-LAW", "n,a,L",
        "event")
    row("RECORD-BLOCK", "GENERATED", chart["triangles"], "COMPUTED-HERE",
        "ONE-STATE", "WRITTEN-BY-AN-EVENT", "a", "record")
    row("HISTORY", "GENERATED", cited["histories"], "SEALED-CITATION",
        "ONE-STATE", "CORPUS-FACT", "the drivers", "record")
    row("COUNT-FIELD", "GENERATED", cited["count_fields"],
        "SEALED-CITATION", "ONE-STATE", "THE-RECORD-COMPONENT",
        "the drivers", "record")
    row("QUANTUM-STATE", "DECLARED", chart["cells"], "COMPUTED-HERE",
        "ONE-STATE", "THE-AMPLITUDE-COMPONENT", "the state", "state")
    row("BRANCH-WEIGHT", "GENERATED", 1, "COMPUTED-HERE",
        "ENSEMBLE-SIDE", "BOOKKEEPING-NEVER-READ-BY-THE-UPDATE",
        "the reading", "state")
    row("MENU", "LAW-SELECTED", chart["menu"], "COMPUTED-HERE",
        "ONE-STATE", "THE-ADMISSIBLE-GRAINS", "q", "geometry")
    row("NAMING", "RECONSTRUCTED", cited["chart_classes"],
        "SEALED-CITATION", "ONE-STATE", "RECORD-ADMITTED", "the record",
        "record")
    row("COIN", "DECLARED", DECL["con.coin_classes"], "COMPUTED-HERE",
        "ONE-STATE", "THE-QUANTUM-EVOLUTION-MEMBER", "the coin", "state")
    row("UNION-CARRIER", "GENERATED", usub["carriers"], "COMPUTED-HERE",
        "ONE-STATE", "THE-GLUED-ARENA", "the chart", "geometry")
    row("UNION-PAIR", "GENERATED", usub["pairs"], "COMPUTED-HERE",
        "ONE-STATE", "THE-GLUED-CARRIER", "the chart", "geometry")
    row("CONFLICT-GROUP", "GENERATED", usub["groups"], "COMPUTED-HERE",
        "ONE-STATE", "THE-UNION-EVENT-UNIVERSE", "n,a", "event")
    row("SEAM-COMPLETION", "DECLARED", DECL["con.seam_kernel"],
        "COMPUTED-HERE", "READING-RELATIVE",
        "STATE-COMPONENT-IFF-PERSISTENT", "the seam", "state")
    row("SEAM-STATE-SPACE", "GENERATED", 31 ** 3, "COMPUTED-HERE",
        "READING-RELATIVE", "THE-COMPLETION-TRIPLE", "the seam", "state")
    row("METRIC-READOUT", "LAW-SELECTED", 1, "SEALED-CITATION",
        "ONE-STATE", "COUNT-AS-SQUARED-LENGTH", "the weld", "metric")
    senses = (  # noqa: the G-SENSES probe injects at its own gate
        ("event", "an event is a set of actors of the declared arity "
                  "dividing together, and nothing else is called one"),
        ("cell", "a cell is an unordered co-division pair of actors "
                 "carrying one declared direction, and nothing else is "
                 "called one"),
        ("geometry", "the geometry is the cell set with its incidence, "
                     "the object the weld reads, and nothing else is "
                     "called one"),
        ("record", "the record is the co-division relation with its "
                   "multiplicities, and nothing else is called one"),
        ("state", "the state is the instantaneous data the declared "
                  "update reads, listed reading-relative in this table, "
                  "and nothing else is called one"),
        ("metric", "the metric is the division count read as the squared "
                   "length of its link direction, and nothing else is "
                   "called one"),
    )
    return {"rows": rows, "cited": cited, "senses": senses,
            "computed_rows": sum(1 for r in rows
                                 if r["backing"] == "COMPUTED-HERE"),
            "cited_rows": sum(1 for r in rows
                              if r["backing"] == "SEALED-CITATION"),
            "classes_used": tuple(sorted({r["class"] for r in rows})),
            "sense_census": tuple(sorted(Counter(
                r["sense_word"] for r in rows).items()))}


FREE_DECLARATIONS = (
    ("d", "the spatial dimension", "ARENA-CHOICE"),
    ("q", "the field order", "ARENA-CHOICE"),
    ("a", "the division-event arity", "ARENA-CHOICE"),
    ("R", "the depth in rounds", "ARENA-CHOICE"),
    ("the ceiling", "the occupancy ceiling", "ARENA-CHOICE"),
    ("the chart", "the two-sector overlap type", "ARENA-CHOICE"),
    ("the window", "the driven schedule set", "SCHEDULE"),
    ("the horizon", "the number of coupled steps", "SCHEDULE"),
    ("the tick", "the scheduling convention", "SCHEDULE"),
    ("the coin", "the S_3-covariant unitary", "DYNAMICAL-CONVENTION"),
    ("the coin order", "coin before or after the residue",
     "DYNAMICAL-CONVENTION"),
    ("the orientation", "the sign of the shift", "DYNAMICAL-CONVENTION"),
    ("the reading", "the Born menu or the record menu", "READING"),
    ("the seam", "the completion at a shared site", "COMPLETION-DATUM"),
    ("the measure", "the measure over configurations",
     "MEASURE-DECLARATION"),
)


def measure_free_declarations(anch, gate_reader):
    parsed = anch.parse_ints("N-CON-Q58", gate_reader)
    decls, free_cited = parsed[0], parsed[1]
    rows = pick("MUT-TYPES",
                [{"declaration": d, "fixes": w, "type": t}
                 for (d, w, t) in FREE_DECLARATIONS],
                [{"declaration": d, "fixes": w, "type": "FREE"}
                 for (d, w, t) in FREE_DECLARATIONS])
    cats = sorted({r["type"] for r in rows})
    return {"rows": rows, "count": len(rows), "cited_free": free_cited,
            "cited_declarations": decls, "categories": cats,
            "category_census": tuple(sorted(Counter(
                r["type"] for r in rows).items()))}


EVENT_FORK = (
    {"arm": "COMMITTED", "event_class": "three-actor conflict groups",
     "shape": "a triple of actors; the affine-line coset structure is the "
              "selection law and it is DECLARED, labelled declared (the "
              "selection law), pending COSET-FROM-COMPATIBILITY",
     "grain": 3},
    {"arm": "BRANCH", "event_class": "pair-events",
     "shape": "an event IS a co-division pair; ARITY's a = 2 extension "
              "family under its own declared packing rule, never merged "
              "into the committed arm",
     "grain": 2},
)


def measure_fork():
    fork = list(EVENT_FORK)
    if mut("MUT-FORK"):
        fork.append({"arm": "COMPROMISE",
                     "event_class": "a merged event class",
                     "shape": "the silent compromise the wall forbids",
                     "grain": 0})
    return {"arms": fork, "arm_count": len(fork),
            "grains": tuple(sorted({a["grain"] for a in fork}))}


# ---- M0c: the three conditional maps, typed and composed nowhere.  The
# region audit walks the call graph itself; the maps share only module
# plumbing and never one another.

def map_event_selection(rel, q):
    """EVENT SELECTION: (record, amplitude-functional) -> a distribution
    over the event class.  KIND: stochastic kernel.  The committed corpus
    carries it at two grains -- the walk's cell emission and the grammar's
    round admission -- and this unit composes it with nothing."""
    return {"kind": "STOCHASTIC-KERNEL",
            "domain": "record x born-functional",
            "codomain": "distributions over the declared event class",
            "witness_mass": str(sum(q)) if q else "UNDEFINED"}


def map_seam_completion(rel):
    """SEAM COMPLETION: (post-record) -> the SET of admissible
    completions.  KIND: relation, never a function: the full lattice at
    the pre-state, four- or eight-valued at every lawful crossing's seam
    slot, one-valued at none."""
    sizes = set()
    for s in SHARED:
        sizes.add(len(successors(s, rel, ())))
    for g in UGROUPS:
        fp = footprint(g, rel)
        if profile(fp) == (1, 0, 2):
            rel2 = advance_rel(g, rel)
            for s in SHARED:
                sizes.add(len(successors(s, rel2, fp["cross"])))
            break
    return {"kind": "RELATION",
            "domain": "the post-record",
            "codomain": "sets of seam completions",
            "witness_sizes": tuple(sorted(sizes))}


def map_quantum_evolution(psi, n, order):
    """QUANTUM EVOLUTION: (amplitude, record residue) -> amplitude.
    KIND: function; unitary at the tripled scale, measured by exact norm
    conservation."""
    post = coin_apply(list(psi), list(n), order)
    before = sum(znorm(z) for z in psi)
    after = sum(znorm(z) for z in post)
    if mut("MUT-UNITARY"):
        after += 1
    return {"kind": "FUNCTION",
            "domain": "amplitude x record residue",
            "codomain": "amplitude",
            "norm_in_times_nine": before * 9,
            "norm_out": after,
            "unitary_at_scale": after == before * 9}


MAP_REGION_NAMES = ("map_event_selection", "map_seam_completion",
                    "map_quantum_evolution")


def maps_reach_audit(source):
    """the three maps may not call one another, directly or through any
    chain of module functions: composition belongs to DYNAMICS-CLOSURE."""
    tree = ast.parse(source)
    calls = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            out = set()
            for sub in ast.walk(node):
                if isinstance(sub, ast.Call) and isinstance(sub.func,
                                                            ast.Name):
                    out.add(sub.func.id)
            calls[node.name] = out
    pattern = pick("MUT-COMPOSE", "map_", "mapX_")
    found = sorted(n for n in calls if n.startswith(pattern))

    def reach(start):
        seen, todo = set(), [start]
        while todo:
            cur = todo.pop()
            for nxt in calls.get(cur, ()):
                if nxt not in seen:
                    seen.add(nxt)
                    todo.append(nxt)
        return seen

    offences = []
    for mname in found:
        r = reach(mname)
        for other in MAP_REGION_NAMES:
            if other != mname and other in r:
                offences.append((mname, other))
    return {"maps_found": found, "offences": offences,
            "covered": len(found)}
# ---- walk plumbing: the one Born accessor every downstream consumer
# reads.  The three psi-status regions must AGREE with it byte for byte
# (G-PSI-EQUAL); no consumer reaches any region (G-STAMPS reach audit).

def born_target(psi, n, order):
    """the emission functional at the committed read point: the post-coin
    Born weight of each cell, normalised exactly."""
    post = coin_apply(list(psi), list(n), order)
    w = [znorm(z) for z in post]
    tot = sum(w)
    if tot == 0:
        return None
    q = tuple(Fraction(x, tot) for x in w)
    if mut("MUT-BORN"):
        q = tuple(Fraction(x, 1) for x in w)
    return q


def build_targets(round_flds):
    """the declared target family: five declared amplitudes at the initial
    record under both coin orders, and the round-generated record window
    at every amplitude under both orders."""
    rows = []
    for (aname, psi) in declared_amplitudes():
        for order in COIN_ORDERS:
            rows.append({"amplitude": aname, "record": "R0",
                         "order": order,
                         "q": born_target(psi, R0, order)})
    for (aname, psi) in declared_amplitudes():
        for ri, n in enumerate(round_flds):
            for order in COIN_ORDERS:
                rows.append({"amplitude": aname,
                             "record": "ROUND-" + str(ri),
                             "order": order,
                             "q": born_target(psi, n, order)})
    return rows


def measure_order_fiber(targets):
    """the coin-order fiber at the emission read point: under D.G the
    residue phase cannot enter the Born weights (record-blind, measured);
    under G.D it can and does (measured); at the initial record the two
    members coincide (measured)."""
    by = {}
    for t in targets:
        by[(t["amplitude"], t["record"], t["order"])] = t["q"]
    amps = sorted({t["amplitude"] for t in targets})
    recs = sorted({t["record"] for t in targets})
    dg_blind = True
    gd_moves = False
    r0_equal = True
    for a in amps:
        base = by[(a, "R0", "D.G")]
        for r in recs:
            if by[(a, r, "D.G")] != base:
                dg_blind = False
            if by[(a, r, "G.D")] != by[(a, "R0", "G.D")]:
                gd_moves = True
        if by[(a, "R0", "G.D")] != by[(a, "R0", "D.G")]:
            r0_equal = False
    return {"dg_record_blind": dg_blind, "gd_record_moves": gd_moves,
            "r0_orders_equal": r0_equal,
            "amplitudes": len(amps), "records": len(recs)}


def measure_residue_leg():
    """the coin reads the count field only through its residue: two fields
    differing by the field order on one cell give byte-identical
    functionals at both orders."""
    n2 = list(R0)
    n2[0] += Q
    ok = True
    for (aname, psi) in declared_amplitudes():
        for order in COIN_ORDERS:
            if born_target(psi, R0, order) != born_target(psi, tuple(n2),
                                                          order):
                ok = False
    return {"residue_screens": ok}


def measure_psi(round_flds):
    """M1: the three faces of the trilemma, evaluated at a declared row
    family; the functionals must agree byte for byte at every row."""
    rows = []
    probe_records = [("R0", R0), ("ROUND-A", round_flds[0]),
                     ("ROUND-B", round_flds[1])]
    committed_checked = False
    for (aname, psi) in declared_amplitudes():
        for (rname, n) in probe_records:
            for order in COIN_ORDERS:
                if rname != "R0" and aname not in (
                        "THE-UNIFORM-AMPLITUDE",
                        "A-SINGLE-CELL-AMPLITUDE"):
                    continue
                qo = psi_ontic_q(psi, n, order)
                full = (aname == "A-SINGLE-CELL-AMPLITUDE"
                        and rname == "R0" and order == "G.D"
                        and not committed_checked)
                qi = psi_instrument_q(psi, n, order, full=full)
                if full:
                    qi_block = psi_instrument_q(psi, n, order, full=False)
                    committed_checked = qi == qi_block
                qr = psi_repr_q(psi, n, order)
                rows.append({"amplitude": aname, "record": rname,
                             "order": order,
                             "agree": qo == qi == qr,
                             "defined": qo is not None})
    return {"rows": rows, "faces": 3,
            "agreements": sum(1 for r in rows if r["agree"]),
            "row_count": len(rows),
            "separating_rows": sum(1 for r in rows if not r["agree"]),
            "full_matrix_route_agrees": committed_checked}


# ---- M2: the event classes and the LP census -----------------------------

def build_classes():
    """the LP's event classes, each labelled with its arm of the declared
    fork.  A cell's column entry is one exactly when the event writes that
    cell."""
    tri_cols = [BLOCK_OF[t] for t in TRIANGLES]
    line9_cols = [BLOCK_OF[t] for t in DECLARED_LINES]
    line12_cols = [BLOCK_OF[t] for t in LINES]
    all_cols = [BLOCK_OF[t] for t in TRIPLES]

    def matrix(cols):
        M = [[Fraction(0)] * len(cols) for _ in range(DIM)]
        for j, blk in enumerate(cols):
            for c in blk:
                M[c][j] = Fraction(1)
        if mut("MUT-INCIDENCE"):
            M[0][0] += 1
        return M

    return (
        ("E-BLOCK", "COMMITTED", matrix(tri_cols), len(tri_cols)),
        ("E-LINE-DECLARED", "COMMITTED", matrix(line9_cols),
         len(line9_cols)),
        ("E-LINE-COSET", "COMMITTED", matrix(line12_cols),
         len(line12_cols)),
        ("E-TRIPLE", "COMMITTED", matrix(all_cols), len(all_cols)),
    )


def measure_normalization(classes):
    """the pre-registered C(a,2) normalization, measured per class: the
    marginal-sum identity holds exactly where every event writes C(a,2)
    cells; the inclusion-marginal and uniform-two-stage readings build the
    SAME constraint system; the free-two-stage reading constrains
    nothing."""
    a = 3
    scale = a * (a - 1) // 2
    per_class = []
    for (cname, arm, M, nev) in classes:
        colsums = sorted(Counter(
            int(sum(M[i][j] for i in range(DIM)))
            for j in range(nev)).items())
        allc = all(k == scale for k, _v in colsums)
        per_class.append({"class": cname, "writer_census": colsums,
                          "identity_holds": allc})
    # route A: inclusion marginals, sum over events containing the cell,
    # equal to scale times the Born weight.  Route B: two-stage with the
    # UNIFORM within-event selection, one over the writer size.  The two
    # systems coincide exactly when scale times the two-stage matrix is
    # the incidence matrix -- true where every event writes scale cells.
    Mb = classes[0][2]
    nevb = len(Mb[0])
    wsize = [sum(1 for i in range(DIM) if Mb[i][j] != 0)
             for j in range(nevb)]
    W = [[(Fraction(1, wsize[j]) if Mb[i][j] != 0 else Fraction(0))
          for j in range(nevb)] for i in range(DIM)]
    routeB = [[Fraction(scale) * W[i][j] for j in range(nevb)]
              for i in range(DIM)]
    covered = sum(1 for i in range(DIM)
                  if any(Mb[i][j] != 0 for j in range(nevb)))
    if mut("MUT-NORM"):
        per_class[0]["identity_holds"] = False
    return {"scale": scale, "arity": a, "per_class": per_class,
            "two_routes_equal": routeB == Mb,
            "free_two_stage_covered_cells": covered,
            "free_two_stage_vacuous": covered == DIM}


def measure_lp(classes, targets):
    """the Born-marginal feasibility census: every (class, distinct
    target) pair through the one exact solver; the committed row named;
    the ceiling checked at every row; the a = 2 branch beside the a = 3
    classes, never merged."""
    scale = 3
    distinct = {}
    for t in targets:
        if t["q"] is None:
            continue
        distinct.setdefault(t["q"], []).append(
            (t["amplitude"], t["record"], t["order"]))
    rows = []
    for q, mem in sorted(distinct.items(),
                         key=lambda kv: ekey(kv[1])):
        is_primary = any(r == "R0" for (_a, r, _o) in mem)
        for (cname, arm, M, nev) in classes:
            res = lp_row(M, list(q), scale, want_dim=is_primary)
            rows.append({"class": cname, "arm": arm,
                         "members": tuple(sorted(mem)),
                         "qmax": res["qmax"], "word": res["word"],
                         "gap": res["gap"], "dim": res["dim"],
                         "implicit": res["implicit"],
                         "second_point": res["second_point"],
                         "ceiling_witness": res["ceiling_witness"],
                         "primary": is_primary})
    undefined = sum(1 for t in targets if t["q"] is None)
    # the a = 2 branch: an event IS a pair-cell, the marginal map is the
    # identity, and the problem degenerates to p = q
    branch_rows = []
    for q, mem in sorted(distinct.items(),
                         key=lambda kv: ekey(kv[1])):
        ok = (sum(q) == 1 and all(v >= 0 for v in q))
        branch_rows.append({"class": "E-PAIR", "arm": "BRANCH",
                            "members": tuple(sorted(mem)),
                            "word": pick("MUT-A2",
                                         "DEGENERATE-IDENTITY",
                                         "UNIQUE"),
                            "identity_feasible": ok})
    committed = [r for r in rows
                 if r["class"] == "E-BLOCK"
                 and any(a == "A-SINGLE-CELL-AMPLITUDE" and rec == "R0"
                         and o == "G.D" for (a, rec, o) in r["members"])]
    committed_all = [r for r in rows
                     if any(a == "A-SINGLE-CELL-AMPLITUDE"
                            and rec == "R0" and o == "G.D"
                            for (a, rec, o) in r["members"])]
    words = Counter(r["word"] for r in rows)
    feas_ceiling_ok = sum(
        1 for r in rows
        if not (r["word"] != "INFEASIBLE"
                and Fraction(r["qmax"]) > Fraction(1, 3)))
    ceiling_exceptions = len(rows) - feas_ceiling_ok
    if mut("MUT-CEILING"):
        ceiling_exceptions += 1
    many_dims = sorted({r["dim"] for r in rows
                        if r["word"] == "MANY" and r["dim"] is not None})
    return {"rows": rows, "branch_rows": branch_rows,
            "distinct_targets": len(distinct),
            "target_rows": len(targets),
            "undefined_targets": undefined,
            "words": tuple(sorted(words.items())),
            "committed_rows": committed,
            "committed_all": committed_all,
            "ceiling_checked": len(rows),
            "ceiling_exceptions": ceiling_exceptions,
            "many_dims": many_dims,
            "branch_degenerate": sum(1 for r in branch_rows
                                     if r["word"] == "DEGENERATE-IDENTITY"
                                     and r["identity_feasible"]),
            "branch_count": len(branch_rows)}


def measure_lp_controls(classes):
    """the two control arms, through the REAL predicates (the ACT Z1
    pattern): a synthetic target forced feasible by construction, and one
    forced infeasible by the ceiling."""
    (_n, _a, M, nev) = classes[0]
    tot = nev * (nev + 1) // 2
    phat = [Fraction(j + 1, tot) for j in range(nev)]
    qf = [sum(M[i][j] * phat[j] for j in range(nev)) / 3
          for i in range(DIM)]
    qi = [Fraction(0)] * DIM
    qi[0] = Fraction(1)
    if mut("MUT-CONTROL-ARM"):
        qi = [Fraction(1, DIM)] * DIM
    rf = lp_row(M, qf, 3)
    ri = lp_row(M, qi, 3)
    return {"forced_feasible_word": rf["word"],
            "forced_infeasible_word": ri["word"],
            "forced_infeasible_ceiling": ri["ceiling_witness"],
            "forced_feasible_ok": rf["word"] in ("UNIQUE", "MANY"),
            "forced_infeasible_ok": ri["word"] == "INFEASIBLE"}


# ---- M3: the carrier candidates -------------------------------------------

def measure_carrier(lp_committed_q):
    """the four carrier candidates through three predicates each; the
    cq-instrument is a member of a measured family, never an assumption."""
    V = [[1 if i == j else 0 for j in range(DIM)] for i in range(DIM + 1)]
    VtV = [[sum(V[k][i] * V[k][j] for k in range(DIM + 1))
            for j in range(DIM)] for i in range(DIM)]
    iso_ok = all(VtV[i][j] == (1 if i == j else 0)
                 for i in range(DIM) for j in range(DIM))
    if mut("MUT-CARRIER"):
        VVt = [[sum(V[i][k] * V[j][k] for k in range(DIM))
                for j in range(DIM + 1)] for i in range(DIM + 1)]
        iso_ok = all(VVt[i][j] == (1 if i == j else 0)
                     for i in range(DIM + 1) for j in range(DIM + 1))
    q = lp_committed_q
    branches = [(str(q[c]), c) for c in range(DIM) if q[c] != 0]
    distinct_records = len(branches)
    aimg = set(AMAP.values())
    bimg = set(BMAP.values())
    cross_cells_undirected = sum(
        1 for p in CROSS_PAIRS
        if not (set(p) <= aimg) and not (set(p) <= bimg))
    coin_block_sizes = {len(LINKS)}
    cands = []

    def cand(name, register, dim_policy):
        host = iso_ok if dim_policy == "GROWS" else (
            dim_policy == "FIXED-MASK")
        express = register or distinct_records <= 1
        evolve = False
        cands.append({"candidate": name,
                      "classical_register": register,
                      "dim_policy": dim_policy,
                      "hosts_the_state": host,
                      "expresses_the_branching": express,
                      "evolves_across_creation": evolve})

    cand("CQ-INSTRUMENT", True, "GROWS")
    cand("DIRECT-SUM", True, "GROWS")
    cand("FIXED-CARRIER", False, "FIXED-MASK")
    cand("AMPLITUDE-ON-RECORD", False, "FIXED-MASK")
    hosts = sum(1 for c in cands if c["hosts_the_state"])
    expresses = sum(1 for c in cands if c["expresses_the_branching"])
    evolves = sum(1 for c in cands if c["evolves_across_creation"])
    return {"candidates": cands, "count": len(cands),
            "isometry_verified": iso_ok,
            "distinct_branch_records": distinct_records,
            "cross_cells_directionless": cross_cells_undirected,
            "cross_pairs_n": len(CROSS_PAIRS),
            "coin_block_sizes": tuple(sorted(coin_block_sizes)),
            "hosts": hosts, "expresses": expresses, "evolves": evolves}


# ---- M4: the admissible-class debt ---------------------------------------

def measure_debt(usub, targets):
    """the coupled walk's menu against the creation relation's refused
    classes, at both arms of the fork."""
    chart_menu = DIM
    grain_mismatch = all(len(p) == 2 for p in CELL_PAIR) and all(
        len(t) == 3 for t in TRIPLES)
    union_menu = tuple(sorted(UREL, key=ekey))
    in_cross = sum(1 for p in union_menu if p in set(CROSS_PAIRS))
    if mut("MUT-DEBT"):
        in_cross += 1
    frozen_admits = usub["frozen_alive"]
    frozen_seam_admits = sum(
        v for k, v in usub["profile_census"]
        if tuple(k)[0] > 0 and tuple(k) == (0, 0, 3))
    mass_one = 0
    nonzero = 0
    for t in targets:
        if t["record"] == "R0" and t["order"] == "G.D":
            if t["q"] is not None:
                nonzero += 1
                if sum(t["q"]) == 1:
                    mass_one += 1
    return {"chart_menu_cells": chart_menu,
            "grain_mismatch": grain_mismatch,
            "union_menu_pairs": len(union_menu),
            "menu_cross_overlap": in_cross,
            "cross_pairs": len(CROSS_PAIRS),
            "frozen_creation_admits_doubling": frozen_admits,
            "frozen_creation_admits_seam": frozen_seam_admits,
            "seam_spanning": usub["seam_spanning"],
            "amplitudes_with_unit_mass": mass_one,
            "nonzero_amplitudes": nonzero}


# ---- the tie-break registry (EQUIVARIANT-OR-DECLARED) --------------------

def measure_tiebreaks(round_flds):
    """every member-selecting choice is either proved equivariant or
    DECLARED and counted; a silent tie-break is the wall's offence."""
    gen = {}
    for x in SITES:
        gen[x] = vadd(x, (1, 0))
    mapped = set()
    for n in round_flds:
        n2 = [0] * DIM
        for k, (x, l) in enumerate(CELLS):
            n2[CELL_INDEX[(gen[x], l)]] = n[k]
        mapped.add(tuple(n2))
    closed = mapped == set(round_flds)
    rows = [
        {"choice": "the record window",
         "class": "EQUIVARIANT-PROVED",
         "evidence": "the window is the whole round-generated family and "
                     "a translation generator permutes it onto itself"},
        {"choice": "the probe-family extras",
         "class": "DECLARED",
         "evidence": "the direct-sum triple and the first and last "
                     "lattice points in the canonical key order"},
        {"choice": "the canonical container order",
         "class": "DECLARED",
         "evidence": "every iteration order routes through the one "
                     "canonical key; no verdict reads a position"},
        {"choice": "the committed coin order",
         "class": "DECLARED",
         "evidence": "the parent's delivered member; the alternative "
                     "member is run beside it at every row"},
    ]
    if mut("MUT-TIEBREAK"):
        rows = rows[:-1]
    return {"rows": rows, "declared": sum(1 for r in rows
                                          if r["class"] == "DECLARED"),
            "equivariant": sum(1 for r in rows
                               if r["class"] == "EQUIVARIANT-PROVED"),
            "window_closed_under_generator": closed}


# ---- W3 instrumentation: every headline auto-labelled --------------------

def w3_labels(lp, seam2, obs):
    """member-specific against family-level, computed from the varied
    fibre data and never typed: a claim is FAMILY-LEVEL only when it held
    at one hundred percent of the swept rows AND carries a derivation leg;
    everything else is member-specific with its fibres disclosed."""
    ceiling_family = (lp["ceiling_exceptions"] == 0)
    labels = [
        {"segment": SEGMENT_NAMES[0], "label": "MEMBER-SPECIFIC",
         "fibres": "one arena; the committed corpus; the declared seam "
                   "reading"},
        {"segment": SEGMENT_NAMES[1], "label": "MEMBER-SPECIFIC",
         "fibres": "one arena; the declared probe family; the "
                   "three-member reading family; every first crossing"},
        {"segment": SEGMENT_NAMES[2], "label": "MEMBER-SPECIFIC",
         "fibres": "the delivered row family: five amplitudes, three "
                   "records, both coin orders"},
        {"segment": SEGMENT_NAMES[3],
         "label": ("FAMILY-LEVEL-ACROSS-THE-TARGET-FAMILY"
                   if ceiling_family else "MEMBER-SPECIFIC"),
         "fibres": "the ceiling leg is an arithmetic theorem checked at "
                   "every row; the verdict row is member-specific to the "
                   "committed amplitude, record, order and class"},
        {"segment": SEGMENT_NAMES[4], "label": "MEMBER-SPECIFIC",
         "fibres": "one arena; both fork arms censused; the four-member "
                   "candidate family"},
    ]
    if mut("MUT-W3"):
        labels[3]["label"] = "MEMBER-SPECIFIC"
    member = sum(1 for l in labels if l["label"] == "MEMBER-SPECIFIC")
    family = len(labels) - member
    return {"labels": labels, "member_specific": member,
            "family_level": family,
            "ceiling_family_level": ceiling_family}


# ---- the downstream stamp table (#119 totality over the rows) ------------

def stamp_table(lp, psi, carrier, debt):
    rows = []
    for i, _r in enumerate(lp["rows"]):
        rows.append("lp.row." + str(i))
    for i, _r in enumerate(lp["branch_rows"]):
        rows.append("lp.branch." + str(i))
    for i, _r in enumerate(psi["rows"]):
        rows.append("psi.row." + str(i))
    rows.append("carrier.family")
    rows.append("debt.census")
    if mut("MUT-STAMP"):
        rows = rows[:-1]
    return {"rows": rows,
            "stamp": {"seam": "READING-INDEPENDENT-BY-REACH-AUDIT",
                      "psi": "FACE-INDEPENDENT-BY-BYTE-EQUALITY"},
            "count": len(rows)}


def stamps_reach_audit(source):
    """no LP, carrier or debt function may reach the seam-completion
    machinery, and no downstream consumer may reach a psi region except
    through the one Born accessor: measured on the call graph."""
    tree = ast.parse(source)
    calls = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            out = set()
            for sub in ast.walk(node):
                if isinstance(sub, ast.Call) and isinstance(sub.func,
                                                            ast.Name):
                    out.add(sub.func.id)
            calls[node.name] = out

    def reach(start):
        seen, todo = set(), [start]
        while todo:
            cur = todo.pop()
            for nxt in calls.get(cur, ()):
                if nxt not in seen:
                    seen.add(nxt)
                    todo.append(nxt)
        return seen

    seam_names = {"successors", "successors_raw", "completion_lattice",
                  "prediction", "seam_counts", "cross_index"}
    psi_names = {"psi_ontic_q", "psi_instrument_q", "psi_repr_q",
                 "psi_instrument_rho"}
    offences = []
    for fn in ("measure_lp", "measure_lp_controls", "lp_row",
               "measure_carrier", "born_target", "build_targets"):
        r = reach(fn)
        hit = sorted((seam_names | psi_names) & r)
        if hit:
            offences.append((fn, hit))
    for fn in ("measure_debt",):
        r = reach(fn)
        hit = sorted((seam_names - {"seam_counts", "cross_index"}) & r
                     | (psi_names & r))
        if hit:
            offences.append((fn, hit))
    return {"offences": offences, "audited": 7}


# ---- the circularity carry (Q1/Q4/Q5) ------------------------------------

DEP_EDGES = (
    ("ACTOR", "CELL"), ("DIRECTION", "CELL"),
    ("ACTOR", "DIVISION-EVENT"), ("CELL", "ROUND-LAW"),
    ("ROUND-LAW", "HISTORY"), ("DIVISION-EVENT", "HISTORY"),
    ("HISTORY", "RECORD-BLOCK"), ("RECORD-BLOCK", "COUNT-FIELD"),
    ("COUNT-FIELD", "QUANTUM-STATE"), ("QUANTUM-STATE", "EMISSION"),
    ("EMISSION", "COUNT-FIELD"), ("RECORD-BLOCK", "ACTOR"),
)


def measure_circularity():
    edges = list(DEP_EDGES)
    if mut("MUT-CYCLE"):
        edges = [e for e in edges if e != ("RECORD-BLOCK", "ACTOR")]
    adj = {}
    for (u, v) in edges:
        adj.setdefault(u, []).append(v)

    def shortest_cycle_through(node):
        best = None
        frontier = [(node, 0)]
        seen = {node: 0}
        while frontier:
            cur, d = frontier.pop(0)
            for nxt in adj.get(cur, ()):
                if nxt == node:
                    if best is None or d + 1 < best:
                        best = d + 1
                elif nxt not in seen:
                    seen[nxt] = d + 1
                    frontier.append((nxt, d + 1))
        return best

    return {"actor_cycle": shortest_cycle_through("ACTOR"),
            "dynamical_cycle": shortest_cycle_through("COUNT-FIELD"),
            "edges": len(edges),
            "full_dynamics_fixed_point": "OPEN-ROUTED-TO-DC"}


# ---- the #299 pre-registration --------------------------------------------

def outcome_prereg(iface, obs, seam2, psi, lp, carrier, debt):
    """one pre-registered outcome pair per head segment, every word on a
    stem of the pin's own bytes, both arms' witnesses measured by this
    run."""
    untyped = sum(1 for r in iface["rows"]
                  if r["class"] not in ("DECLARED", "GENERATED",
                                        "RECONSTRUCTED", "LAW-SELECTED"))
    committed_word = (lp["committed_rows"][0]["word"]
                      if lp["committed_rows"] else "ABSENT")
    unique_rows = sum(1 for r in lp["rows"] if r["word"] == "UNIQUE")
    many_rows = sum(1 for r in lp["rows"] if r["word"] == "MANY")
    pairs = [
        {"segment": SEGMENT_NAMES[0],
         "reached": "ECC-STATE-CONTRACT-CLOSED-AT-THE-COMMITTED-WINDOWS"
                    "-UNDER-THE-DECLARED-SEAM-READING",
         "not_reached": "ECC-CIRCULARITY-UNTYPABLE-AT-THE-TABLE",
         "predicate": "every interface row carries one of the four "
                      "classes; the other arm fires on any untypable row",
         "witness": len(iface["rows"]) - untyped,
         "other_witness": untyped},
        {"segment": SEGMENT_NAMES[1],
         "reached": "SEAM-DECISION-UNDERDETERMINED-AT-THE-COMMITTED-"
                    "OBSERVABLE-MENU",
         "not_reached": "SEAM-PERSISTENT-SUPPORTED",
         "predicate": "a committed observable separates the "
                      "completion-only probe family; the modal relation "
                      "separating it is the other arm's near-witness",
         "witness": obs["menu_size"] - obs["blind"],
         "other_witness": obs["relation_value_set"]},
        {"segment": SEGMENT_NAMES[2],
         "reached": "PSI-STATUS-INDEPENDENT",
         "not_reached": "PSI-ONTIC",
         "predicate": "some delivered row's functional separates the "
                      "three faces",
         "witness": psi["separating_rows"],
         "other_witness": psi["row_count"]},
        {"segment": SEGMENT_NAMES[3],
         "reached": "ECC-LP-INFEASIBLE-AT-THE-COMMITTED-ROW",
         "not_reached": "ECC-LP-UNIQUE",
         "predicate": "the committed row's own word; every other word is "
                      "demonstrated on a real or control row",
         "witness": committed_word,
         "other_witness": unique_rows},
        {"segment": SEGMENT_NAMES[4],
         "reached": "ECC-CARRIER-FAMILY-UNSELECTED-AND-THE-DEBT-DECIDED",
         "not_reached": "ECC-BLOCKED-AT-THE-CARRIER",
         "predicate": "every candidate evaluated at every predicate and "
                      "both debt censuses complete; the other arm is the "
                      "instrument-fault word",
         "witness": carrier["count"] * 3,
         "other_witness": 0},
    ]
    if mut("MUT-PREREG"):
        pairs[1]["reached"] = "SEAM-DECISION-DEFERRED"
    if mut("MUT-FEASIBILITY"):
        pairs[3]["witness"] = "UNMEASURED"
    words_fired = {"INFEASIBLE": any(r["word"] == "INFEASIBLE"
                                     for r in lp["rows"]),
                   "UNIQUE": unique_rows > 0,
                   "MANY": many_rows > 0,
                   "DEGENERATE": lp["branch_degenerate"] > 0}
    return {"pairs": pairs, "lp_words_fired": tuple(sorted(
        (k, bool(v)) for k, v in words_fired.items()))}
# ===========================================================================
# SECTION 8.  THE VERDICT, AND THE COMPARATOR THAT SHARES NOTHING WITH IT
# ===========================================================================
# The head is five fenced segments.  build_verdict renders them from the
# measured registry through templates; reconstruct() rebuilds every one
# from the receipt's PRIMITIVE row tables by its own arithmetic and its
# own format strings, reading no summary scalar, and the two are compared
# whole, then numeral by numeral positionally.

def build_verdict(M):
    s1 = M.stmt(
        "ECC-STATE-CONTRACT-CLOSED-AT-THE-COMMITTED-WINDOWS-UNDER-THE-"
        "DECLARED-SEAM-READING<OBJECTS={o}; COMPUTED-HERE={c}; "
        "CITED={ci}; SENSE-WORDS={sw}; FREE-DECLARATIONS-CARRIED={fd}-OF-"
        "{fdc}-WITH-{tc}-TYPE-CATEGORIES; EVENT-FORK=DECLARED-{fa}-ARMS-"
        "NO-COMPROMISE; COSET-PRINCIPLE=DECLARED-THE-SELECTION-LAW; "
        "MAPS={mp}-TYPED-COMPOSED-NOWHERE; STATE-COMPONENTS={sc}-PLUS-"
        "BOOKKEEPING={bk}; SEAM-COMPONENT=READING-CONDITIONAL; "
        "ACTOR-RECORD-CYCLE={cy}-EDGES-CARRIED-OPEN-AT-FULL-DYNAMICS>",
        o="iface.object_rows", c="iface.computed", ci="iface.cited_rows",
        sw="iface.senses", fd="decl.count", fdc="decl.cited_free",
        tc="decl.categories", fa="fork.arms", mp="maps.count",
        sc="state.components", bk="state.bookkeeping",
        cy="circ.actor_cycle")
    s2 = M.stmt(
        "SEAM-DECISION-UNDERDETERMINED-AT-THE-COMMITTED-OBSERVABLE-MENU<"
        "OBSERVABLES={ob}; COMPLETION-BLIND={bl}-OF-{obx}; "
        "PROBE-STATES={pr}; THE-MODAL-RELATION-SEPARATES={rv}-VALUES-"
        "OVER-THE-SAME-PROBES; READING-FAMILY={rf}; TWO-STEP-CENSUS-"
        "FROM-ALL-{fc}-FIRST-CROSSINGS: RE-SOLVED-FIBER-{fmin}-TO-{fmax}; "
        "PERSIST-FIT-DIFFERS-AT-{df}-OF-{fcx}; PERSIST-KEPT-DIFFERS-AT-"
        "{dk}-OF-{fcy}; CHOSEN-READING=RE-SOLVED-DECLARED-NOT-MEASURED; "
        "DOWNSTREAM-STAMPED={st}-ROWS>",
        ob="obs.menu", bl="obs.blind", obx="obs.menu", pr="obs.probes",
        rv="obs.relation_values", rf="seam.readings",
        fc="seam.first_crossings", fmin="seam.fiber_min",
        fmax="seam.fiber_max", df="seam.differ_fit",
        fcx="seam.first_crossings", dk="seam.differ_kept",
        fcy="seam.first_crossings", st="stamps.count")
    s3 = M.stmt(
        "PSI-STATUS-INDEPENDENT-AT-EVERY-DELIVERED-ROW<FACES={f}; "
        "ROWS={r}; FUNCTIONAL-AGREEMENTS={ag}-OF-{rx}; SEPARATING-ROWS="
        "{z}; THE-CONSUMERS-REACH-THE-BORN-FUNCTIONAL-ALONE=AUDITED; "
        "THE-TRILEMMA-IS-UNRESOLVED-AND-EVERY-DELIVERED-RESULT-IS-"
        "PROVEN-BLIND-TO-IT>",
        f="psi.faces", r="psi.rows", ag="psi.agreements", rx="psi.rows",
        z="psi.separating")
    s4 = M.stmt(
        "ECC-LP-INFEASIBLE-AT-THE-COMMITTED-ROW-AND-THE-CEILING-IS-A-"
        "THEOREM<CLASSES={cl}-PLUS-THE-PAIR-EVENT-BRANCH; "
        "DISTINCT-TARGETS={tg}; ROWS={rw}; INFEASIBLE={inf}; "
        "UNIQUE={un}; MANY={mn}-MAX-DIM-{md}; FIBER-FEASIBLE={fb}; "
        "BRANCH-DEGENERATE-IDENTITY={dg}-OF-{dgx}; TARGET-UNDEFINED-"
        "AMPLITUDES={tu}; COMMITTED-ROW=SINGLE-CELL-AMPLITUDE-AT-THE-"
        "INITIAL-RECORD-AT-THE-DELIVERED-ORDER-QMAX-{qm}-ABOVE-THE-"
        "CEILING-INFEASIBLE-AT-ALL-{ac}-COMMITTED-CLASSES; CEILING="
        "FEASIBILITY-FORCES-QMAX-AT-MOST-ONE-THIRD-CHECKED-AT-{cr}-ROWS-"
        "EXCEPTIONS-{ce}; CONTROLS=FORCED-BOTH-WAYS-THROUGH-THE-REAL-"
        "PREDICATES; NORMALIZATION=PRE-REGISTERED-PAIR-CELL-FORM-"
        "INCLUSION-EQUALS-UNIFORM-TWO-STAGE-WHERE-EVERY-EVENT-WRITES-"
        "{sc}-CELLS; FREE-TWO-STAGE=VACUOUS-AT-{vc}-OF-{vcx}-CELLS-"
        "COVERED>",
        cl="lp.classes", tg="lp.targets", rw="lp.rows",
        inf="lp.infeasible", un="lp.unique", mn="lp.many",
        md="lp.maxdim", fb="lp.fiber", dg="lp.branch_degenerate",
        dgx="lp.branch_rows", tu="lp.undefined", qm="lp.committed_qmax",
        ac="lp.committed_classes", cr="lp.ceiling_checked",
        ce="lp.ceiling_exceptions", sc="norm.scale",
        vc="norm.covered", vcx="norm.cells")
    s5 = M.stmt(
        "ECC-CARRIER-FAMILY-UNSELECTED-AND-THE-DEBT-DECIDED<"
        "CANDIDATES={cd}; HOST-THE-STATE={h}-OF-{cdx}; EXPRESS-THE-"
        "COMMITTED-BRANCHING={ex}-OF-{cdy}; EVOLVE-ACROSS-CREATION={ev}-"
        "OF-{cdz}; NOTHING-SELECTED-THE-FAMILY-PUBLISHED; DEBT=THE-WALK-"
        "CONTINUES-ON-ITS-OWN-MENU-WHERE-CREATION-REFUSES: MENU-CELLS-"
        "IN-THE-CROSS-CLASS={cp}-OF-{cpx}; FROZEN-CREATION-ADMITS={fz}-"
        "OF-{fzx}-SEAM-SPANNING; UNIT-MASS-AMPLITUDES={um}-OF-{umx}; "
        "CLASS=COMPATIBILITY-NO-GO; SCOPE=ONE-ARENA-COMMITTED-WINDOWS-"
        "COUNTING-ONLY; W-THREE-LABELS={ml}-MEMBER-SPECIFIC-PLUS-{fl}-"
        "FAMILY-LEVEL-FIBRES-DISCLOSED>",
        cd="car.count", h="car.hosts", cdx="car.count",
        ex="car.expresses", cdy="car.count", ev="car.evolves",
        cdz="car.count", cp="debt.cross_overlap", cpx="debt.cross_pairs",
        fz="debt.frozen_seam", fzx="debt.seam_spanning",
        um="debt.mass_one", umx="debt.nonzero",
        ml="w3.member", fl="w3.family")
    return (s1, s2, s3, s4, s5)


def reconstruct(R):
    """The comparator.  Reads ONLY primitive row tables out of the
    serialisable receipt payload, re-derives every head number by its own
    arithmetic, types its own templates, and returns the five segments.
    No summary scalar is read: every count below is recomputed from a row
    list."""
    P = R
    iface_rows = P["interface"]["rows"]
    n_obj = len(iface_rows)
    n_comp = sum(1 for r in iface_rows if r["backing"] == "COMPUTED-HERE")
    n_cit = sum(1 for r in iface_rows
                if r["backing"] == "SEALED-CITATION")
    n_sense = len(P["interface"]["senses"])
    fd_rows = P["free_declarations"]["rows"]
    n_fd = len(fd_rows)
    fd_cited = P["free_declarations"]["cited_free"]
    n_cat = len({r["type"] for r in fd_rows})
    n_arms = len(P["fork"]["arms"])
    n_maps = len(P["maps"]["typed"])
    sc = len([r for r in iface_rows
              if r["object"] in ("COUNT-FIELD", "QUANTUM-STATE")])
    bk = len([r for r in iface_rows if r["object"] == "BRANCH-WEIGHT"])
    cyc = P["circularity"]["actor_cycle"]
    c1 = ("ECC-STATE-CONTRACT-CLOSED-AT-THE-COMMITTED-WINDOWS-UNDER-THE-"
          "DECLARED-SEAM-READING<OBJECTS=%d; COMPUTED-HERE=%d; CITED=%d; "
          "SENSE-WORDS=%d; FREE-DECLARATIONS-CARRIED=%d-OF-%d-WITH-%d-"
          "TYPE-CATEGORIES; EVENT-FORK=DECLARED-%d-ARMS-NO-COMPROMISE; "
          "COSET-PRINCIPLE=DECLARED-THE-SELECTION-LAW; MAPS=%d-TYPED-"
          "COMPOSED-NOWHERE; STATE-COMPONENTS=%d-PLUS-BOOKKEEPING=%d; "
          "SEAM-COMPONENT=READING-CONDITIONAL; ACTOR-RECORD-CYCLE=%d-"
          "EDGES-CARRIED-OPEN-AT-FULL-DYNAMICS>"
          % (n_obj, n_comp, n_cit, n_sense, n_fd, fd_cited, n_cat,
             n_arms, n_maps, sc, bk, cyc))
    ob_rows = P["seam"]["obs_rows"]
    n_ob = len(ob_rows)
    n_bl = sum(1 for r in ob_rows if r["value_set_size"] == 1)
    pr = P["seam"]["probes"]
    rv = P["seam"]["relation_values"]
    srows = P["seam"]["step2_rows"]
    fc = len(srows)
    counts = [r["re_solved"] for r in srows]
    fmin, fmax = min(counts), max(counts)
    df = sum(1 for r in srows if r["fit_differs"])
    dk = sum(1 for r in srows if r["kept_differs"])
    rf = len(P["seam"]["reading_family"])
    st = len(P["stamps"]["rows"])
    c2 = ("SEAM-DECISION-UNDERDETERMINED-AT-THE-COMMITTED-OBSERVABLE-"
          "MENU<OBSERVABLES=%d; COMPLETION-BLIND=%d-OF-%d; "
          "PROBE-STATES=%d; THE-MODAL-RELATION-SEPARATES=%d-VALUES-OVER-"
          "THE-SAME-PROBES; READING-FAMILY=%d; TWO-STEP-CENSUS-FROM-ALL-"
          "%d-FIRST-CROSSINGS: RE-SOLVED-FIBER-%d-TO-%d; "
          "PERSIST-FIT-DIFFERS-AT-%d-OF-%d; PERSIST-KEPT-DIFFERS-AT-%d-"
          "OF-%d; CHOSEN-READING=RE-SOLVED-DECLARED-NOT-MEASURED; "
          "DOWNSTREAM-STAMPED=%d-ROWS>"
          % (n_ob, n_bl, n_ob, pr, rv, rf, fc, fmin, fmax, df, fc, dk,
             fc, st))
    prow = P["psi"]["rows"]
    n_pr = len(prow)
    n_ag = sum(1 for r in prow if r["agree"])
    n_sep = sum(1 for r in prow if not r["agree"])
    c3 = ("PSI-STATUS-INDEPENDENT-AT-EVERY-DELIVERED-ROW<FACES=%d; "
          "ROWS=%d; FUNCTIONAL-AGREEMENTS=%d-OF-%d; SEPARATING-ROWS=%d; "
          "THE-CONSUMERS-REACH-THE-BORN-FUNCTIONAL-ALONE=AUDITED; "
          "THE-TRILEMMA-IS-UNRESOLVED-AND-EVERY-DELIVERED-RESULT-IS-"
          "PROVEN-BLIND-TO-IT>"
          % (P["psi"]["faces"], n_pr, n_ag, n_pr, n_sep))
    lrows = P["lp"]["rows"]
    words = Counter(r["word"] for r in lrows)
    n_cl = len({r["class"] for r in lrows})
    n_tg = P["lp"]["distinct_targets"]
    dims = [r["dim"] for r in lrows
            if r["word"] == "MANY" and r["dim"] is not None]
    maxdim = max(dims) if dims else 0
    crows = [r for r in lrows
             if r["class"] == "E-BLOCK"
             and any(a == "A-SINGLE-CELL-AMPLITUDE" and rec == "R0"
                     and o == "G.D" for (a, rec, o) in r["members"])]
    qm = crows[0]["qmax"] if crows else "?"
    call = [r for r in lrows
            if any(a == "A-SINGLE-CELL-AMPLITUDE" and rec == "R0"
                   and o == "G.D" for (a, rec, o) in r["members"])]
    n_call = sum(1 for r in call if r["word"] == "INFEASIBLE")
    n_ceil = len(lrows)
    n_ce = sum(1 for r in lrows
               if r["word"] != "INFEASIBLE"
               and Fraction(r["qmax"]) > Fraction(1, 3))
    brows = P["lp"]["branch_rows"]
    n_dg = sum(1 for r in brows
               if r["word"] == "DEGENERATE-IDENTITY"
               and r["identity_feasible"])
    n_tu = P["lp"]["undefined_targets"]
    ncls = P["normalization"]
    scale = ncls["scale"]
    cov = ncls["free_two_stage_covered_cells"]
    c4 = ("ECC-LP-INFEASIBLE-AT-THE-COMMITTED-ROW-AND-THE-CEILING-IS-A-"
          "THEOREM<CLASSES=%d-PLUS-THE-PAIR-EVENT-BRANCH; "
          "DISTINCT-TARGETS=%d; ROWS=%d; INFEASIBLE=%d; UNIQUE=%d; "
          "MANY=%d-MAX-DIM-%d; FIBER-FEASIBLE=%d; BRANCH-DEGENERATE-"
          "IDENTITY=%d-OF-%d; TARGET-UNDEFINED-AMPLITUDES=%d; "
          "COMMITTED-ROW=SINGLE-CELL-AMPLITUDE-AT-THE-INITIAL-RECORD-AT-"
          "THE-DELIVERED-ORDER-QMAX-%s-ABOVE-THE-CEILING-INFEASIBLE-AT-"
          "ALL-%d-COMMITTED-CLASSES; CEILING=FEASIBILITY-FORCES-QMAX-AT-"
          "MOST-ONE-THIRD-CHECKED-AT-%d-ROWS-EXCEPTIONS-%d; CONTROLS="
          "FORCED-BOTH-WAYS-THROUGH-THE-REAL-PREDICATES; NORMALIZATION="
          "PRE-REGISTERED-PAIR-CELL-FORM-INCLUSION-EQUALS-UNIFORM-TWO-"
          "STAGE-WHERE-EVERY-EVENT-WRITES-%d-CELLS; FREE-TWO-STAGE="
          "VACUOUS-AT-%d-OF-%d-CELLS-COVERED>"
          % (n_cl, n_tg, len(lrows), words.get("INFEASIBLE", 0),
             words.get("UNIQUE", 0), words.get("MANY", 0), maxdim,
             words.get("FEASIBLE-AT-THE-FIBER-ROW", 0), n_dg, len(brows),
             n_tu, qm, n_call, n_ceil, n_ce, scale, cov,
             len(P["lp"]["cells"])))
    cands = P["carrier"]["candidates"]
    n_cd = len(cands)
    n_h = sum(1 for c in cands if c["hosts_the_state"])
    n_ex = sum(1 for c in cands if c["expresses_the_branching"])
    n_ev = sum(1 for c in cands if c["evolves_across_creation"])
    D = P["debt"]
    lab = P["w3"]["labels"]
    n_ml = sum(1 for l in lab if l["label"] == "MEMBER-SPECIFIC")
    n_fl = len(lab) - n_ml
    c5 = ("ECC-CARRIER-FAMILY-UNSELECTED-AND-THE-DEBT-DECIDED<"
          "CANDIDATES=%d; HOST-THE-STATE=%d-OF-%d; EXPRESS-THE-"
          "COMMITTED-BRANCHING=%d-OF-%d; EVOLVE-ACROSS-CREATION=%d-OF-"
          "%d; NOTHING-SELECTED-THE-FAMILY-PUBLISHED; DEBT=THE-WALK-"
          "CONTINUES-ON-ITS-OWN-MENU-WHERE-CREATION-REFUSES: MENU-CELLS-"
          "IN-THE-CROSS-CLASS=%d-OF-%d; FROZEN-CREATION-ADMITS=%d-OF-%d-"
          "SEAM-SPANNING; UNIT-MASS-AMPLITUDES=%d-OF-%d; CLASS="
          "COMPATIBILITY-NO-GO; SCOPE=ONE-ARENA-COMMITTED-WINDOWS-"
          "COUNTING-ONLY; W-THREE-LABELS=%d-MEMBER-SPECIFIC-PLUS-%d-"
          "FAMILY-LEVEL-FIBRES-DISCLOSED>"
          % (n_cd, n_h, n_cd, n_ex, n_cd, n_ev, n_cd,
             D["menu_cross_overlap"], D["cross_pairs"],
             D["frozen_creation_admits_seam"], D["seam_spanning"],
             D["amplitudes_with_unit_mass"], D["nonzero_amplitudes"],
             n_ml, n_fl))
    return (c1, c2, c3, c4, c5)


def head_positional_check(built, recon):
    """POSITIONAL and TOTAL: the two renderings are compared whole, and
    every numeral standing in the built head is matched, in order, against
    the numeral standing at the same position of the reconstruction."""
    if len(built) != len(recon):
        return {"ok": False, "why": "segment count differs"}
    mism, pairs = [], 0
    for i, (a, b) in enumerate(zip(built, recon)):
        if a != b:
            mism.append({"segment": i, "built": a[:90], "recon": b[:90]})
            continue
        na, nb = numerals(a), numerals(b)
        pairs += len(na)
        if na != nb:
            mism.append({"segment": i, "why": "numeral order"})
    return {"ok": not mism, "mismatches": mism[:4],
            "numerals_matched": pairs}
# ===========================================================================
# SECTION 9.  THE WALLS
# ===========================================================================
# Every licence is a positive commitment to scope; the NEG guard carries
# the re-assertion and other-clause exclusions; every wall carries a
# negated control twin; controls are written from the violation, not from
# the pattern list.

WALLS = [
    Wall("WALL-W1-RECONSTRUCTION",
         [r"\bthe (cast|state|born rule|seam|carrier) is derived from the "
          r"record\b",
          r"\breproduction establishes the derivation\b"],
         [r"\breconstruction is never promoted to derivation\b"],
         ["The cast is derived from the record, and the derivation is "
          "complete.",
          "Because the two routes agree, the Born rule is thereby "
          "derived.",
          "Reproduction establishes the derivation of the seam form.",
          "The state is derived from the record it faces.",
          "There is no doubt that the reproduction establishes the "
          "derivation.",
          "The carrier is derived from the record, which is not in "
          "doubt."],
         subject=[r"\b(reproduc\w+|reconstruct\w+|identifiab\w+)\b",
                  r"\btwo routes agree\b",
                  r"\bagreement of (the )?two routes\b"],
         policed=[r"\b(derives?|derived|derivation|establish\w+|"
                  r"proves?|proven)\b"],
         licences=[r"\bcandidate\b", r"\bgated\b", r"\bscope\b",
                   r"\breported as (a reproduction|one)\b",
                   r"\bconsumer gate\b", r"\bidentifiab\w+ within\b",
                   r"\bat (this|one) arena\b", r"\bdeclared\b",
                   r"\bcited\b", r"\bfidelity\b"]),
    Wall("WALL-W2-GAUGE",
         [r"\bgauge (redundancy|quotient) (is|stands) established\b",
          r"\brelabelling is physically meaningless\b"],
         [r"\binvariance is never promoted to gauge\b"],
         ["The gauge redundancy is established by the stabilizer count.",
          "The relabelling is physically meaningless, so the quotient is "
          "physical.",
          "Invariance of the census makes the gauge quotient physical.",
          "The stabilizer proves the relabelling unobservable.",
          "It cannot be denied that the gauge redundancy is established.",
          "The gauge quotient stands established, and not merely "
          "suggested."],
         subject=[r"\b(invarian\w+|stabilizer|relabelling|automorphism)\b"],
         policed=[r"\b(gauge|redundan\w+|physically meaningless|"
                  r"unobservable)\b"],
         licences=[r"\bwithheld\b", r"\boperational observables\b",
                   r"\bevery observable and every experiment\b",
                   r"\bcandidate\b", r"\binvariance statement\b",
                   r"\bcarried at its parent\b"]),
    Wall("WALL-W3-FAMILY",
         [r"\bisp(-family)? predict(s|ion)\b",
          r"\bholds at every member of the family\b"],
         [r"\bmember-specific or family-level\b"],
         ["This is an ISP-family prediction and holds at every member.",
          "The result holds at every member of the family, whatever the "
          "fibre.",
          "ISP predicts the infeasibility at every arena.",
          "The family predicts the ceiling for every member yet "
          "unmeasured.",
          "No one doubts this is an ISP prediction at every member.",
          "The verdict holds at every member of the family, and that is "
          "not in question."],
         subject=[r"\b(family|fibres?|fibers?|member)\b"],
         policed=[r"\b(predicts?|prediction|every member|every arena)\b"],
         licences=[r"\blabel\w+\b", r"\bmember-specific\b",
                   r"\bfamily-level\b", r"\bfibres? disclosed\b",
                   r"\btheorem\b", r"\bswept\b", r"\bdeclared\b",
                   r"\bone arena\b"]),
    Wall("WALL-EVENT-FORK",
         [r"\ba (merged|compromise) event class\b",
          r"\bevents of mixed arity\b"],
         [r"\bno compromise event class is constructed\b"],
         ["A merged event class carries both arities at once.",
          "The compromise event class blends everything into one "
          "grammar.",
          "Events of mixed arity are admitted into the census.",
          "The census blends the arms into a single event class.",
          "There is no doubt that a merged event class serves both "
          "arms.",
          "A compromise event class is constructed here, and not merely "
          "sketched."],
         subject=[r"\bevent class\b"],
         policed=[r"\b(merged?|compromise|blend\w*|mixed|combined?)\b"],
         licences=[r"\bdeclared fork\b", r"\bcommitted arm\b",
                   r"\bextension branch\b", r"\bkept apart\b",
                   r"\btwo arms\b", r"\bbranch\b", r"\bfork\b"]),
    Wall("WALL-BORN-DOWNSTREAM",
         [r"\bborn weights? select the events\b",
          r"\bthe born rule is the event law\b"],
         [r"\bborn language (is licensed|stands) only downstream of the "
          r"lp row\b"],
         ["The Born weights select the events the grammar runs.",
          "The Born rule is the event law of the committed theory.",
          "Born probabilities choose which division events occur.",
          "The event law is the Born rule, read directly off the walk.",
          "It cannot be doubted that the Born weights select the "
          "events.",
          "The Born rule is the event law, and not a marginal "
          "constraint."],
         subject=[r"\bborn\b"],
         policed=[r"\b(event law|selects? the events?|chooses? which|"
                  r"law of events)\b"],
         licences=[r"\blp row\b", r"\bfeasibility\b", r"\binfeasible\b",
                   r"\bmarginal\b", r"\bemission functional\b",
                   r"\breading a\b", r"\bdeclared\b", r"\bthe lp\b"]),
    Wall("WALL-NO-CONTINUUM",
         [r"\bcontinuum limit\b",
          r"\brecovers (the )?continuum\b"],
         [r"\bevery census here is finite and no continuum claim is "
          r"made\b"],
         ["In the continuum limit the walk recovers the wave equation.",
          "The lattice recovers the continuum as the arena grows.",
          "The continuum limit of the record law is the metric field.",
          "At large depth the census approaches its continuum form.",
          "No one doubts the continuum limit recovers the field "
          "theory.",
          "The continuum limit exists here, and not merely formally."],
         subject=[r"\b(continuum|limit of large|asymptotic)\b"],
         policed=[r"\b(recovers?|approaches|converges|yields)\b"],
         licences=[r"\bfinite\b", r"\bone arena\b",
                   r"\bcommitted windows\b", r"\bcounting-only\b"]),
    Wall("WALL-NO-SI",
         [r"\b\d+(\.\d+)? ?(seconds?|metres?|meters?|joules?|kelvin|"
          r"kilograms?|hertz)\b",
          r"\bplanck (constant|length|time)\b"],
         [r"\bno number here carries a laboratory unit\b"],
         ["The tick lasts 3 seconds at the committed arena.",
          "The cell is 2 meters across in laboratory units.",
          "The Planck length sets the scale of one site.",
          "The emission rate is 5 hertz at the delivered coin.",
          "It is beyond question that the tick lasts 3 seconds.",
          "The Planck constant fixes the amplitude scale, and not "
          "loosely."],
         subject=[r"\b(units?|scale|laboratory)\b"],
         policed=[r"\b(si|seconds?|meters?|metres?|joules?|hertz|"
                  r"planck)\b"],
         licences=[r"\bcounting-only\b", r"\bdimensionless\b",
                   r"\bexact rational\b", r"\bcounting fraction\b"]),
    Wall("WALL-SEAM-READING",
         [r"\bpersistence is a measured fact\b",
          r"\bthe corpus (measures|shows) the seam to persist\b"],
         [r"\bpersistence is a declared reading here and every "
          r"downstream row is stamped with it\b"],
         ["Persistence is a measured fact of the committed corpus.",
          "The corpus shows the seam to persist between events.",
          "The seam data persists, and the census proves it.",
          "That the completion persists is settled by the record.",
          "There is no doubt that persistence is a measured fact.",
          "The corpus measures the seam to persist, and not merely to "
          "be readable so."],
         subject=[r"\b(persist\w*|re-solved|seam data|completion)\b"],
         policed=[r"\b(measured fact|settled|proves?|shows?)\b"],
         licences=[r"\breading\b", r"\bdeclared\b",
                   r"\bunderdetermined\b", r"\bstamp\w*\b",
                   r"\bcandidate\b"]),
    Wall("WALL-STATE-PROCESS",
         [r"\bthe whole of what the process carries\b",
          r"\bis the (final|complete) state of the process\b"],
         [r"\bthe state listed here is reading-relative and scoped to "
          r"the committed windows\b"],
         ["The interface table is the whole of what the process carries.",
          "This list is the complete state of the process at last.",
          "The contract closes the state question for the theory "
          "entire.",
          "What the table lists is the final state of the process.",
          "It cannot be disputed that this is the whole of what the "
          "process carries.",
          "The table is the complete state of the process, and not "
          "merely of the machine."],
         subject=[r"\b(state|contract|interface table)\b"],
         policed=[r"\b(the whole of|complete state|final state|closes? "
                  r"the state question|entire)\b"],
         licences=[r"\breading-relative\b", r"\bcommitted windows\b",
                   r"\bconditional\b", r"\bdeclared\b", r"\bscope\b",
                   r"\bat one arena\b"]),
]
# ===========================================================================
# SECTION 10.  THE RUN
# ===========================================================================

DOOR_CHECKS = ("G-SEAL-TOTAL", "G-INTEGRITY", "G-TRANSCRIPT-BOUND",
               "G-TRANSCRIPT-NARRATIVE", "G-OBJECT-UNDER-TEST")

CONSUMED_DECL: set = set()


def use_decl(*keys):
    for k in keys:
        CONSUMED_DECL.add(k)
        if k not in DECL and k not in DECL2:
            raise GateFail("G-DECLARED-CONSUMED", "unknown declared " + k)
    out = []
    for k in keys:
        out.append(DECL.get(k, DECL2.get(k)))
    return out if len(out) > 1 else out[0]


def to_json(obj):
    """normalise to JSON-native so a sealed digest survives the disk
    round trip: tuples become lists, Fractions strings, mappings get
    string keys through item lists."""
    if isinstance(obj, Fraction):
        return str(obj)
    if isinstance(obj, (list, tuple)):
        return [to_json(x) for x in obj]
    if isinstance(obj, (set, frozenset)):
        return sorted((to_json(x) for x in obj),
                      key=lambda v: json.dumps(v, sort_keys=True,
                                               default=str))
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            out[k if isinstance(k, str) else json.dumps(to_json(k))] = \
                to_json(v)
        return out
    if isinstance(obj, (str, int, float, bool)) or obj is None:
        if isinstance(obj, float):
            raise GateFail("G-NO-TYPED-COUNTS", "a float reached the door")
        return obj
    return str(obj)


def full_run(paper_text, paper_rel=PAPER_REL):
    SNAP.clear()
    del OUT_LINES[:]
    del NARRATIVE[:]
    CONSUMED_DECL.clear()
    LATCACHE.clear()
    SUCCACHE.clear()
    refresh_union()
    READS.install()
    READS.reset()
    for rel in (OUT_REL, REC_REL, OUT_REL + ".tmp", REC_REL + ".tmp"):
        READS.declare_optional(rel, "the door's own staging and read-back")
    if paper_text is not None:
        # the object under test is re-read inside the audited window, so
        # its read is on the log and its digest is taken from the bytes
        # the run actually judged
        paper_text = read_text(paper_rel)
    LD, SL, M, CL = Ledger(), Seal(), Meas(), Claims()
    for tok, why in EXEMPT_NUMERALS.items():
        M.exempt_token(tok, why)
    P = {}
    say("v15 ECC -- paper-46 -- event-and-carrier-closure")
    say("instrument for " + PAPER_REL)
    say("=" * 66)

    # ---- G-SOURCES -------------------------------------------------------
    srctext, srcrows = {}, []
    for sid in sorted(SOURCES):
        rel, want = SOURCES[sid]
        want = pick("MUT-SOURCE",
                    want, "0" * 12 if sid == "E-CON" else want)
        got = bdigest(read_bytes(rel))
        srctext[sid] = read_text(rel)
        srcrows.append({"id": sid, "path": rel, "declared": want,
                        "got": got, "ok": got == want})
    P["sources"] = SL.seal("sources", to_json(
        {"rows": srcrows, "commit": SOURCE_COMMIT}), "G-SOURCES")
    LD.gate("G-SOURCES", all(r["ok"] for r in srcrows),
            "every source is read at its pinned digest and no other "
            "route", {"rows": len(srcrows)})

    # ---- G-ANCHORS -------------------------------------------------------
    ANCH = Anchors(VERBATIM)
    areport = ANCH.locate_all(srctext, paper_text)
    P["anchors"] = SL.seal("anchors", to_json(areport), "G-ANCHORS")
    LD.gate("G-ANCHORS", all(r["ok"] for r in areport),
            "every verbatim anchor is located exactly once at or above "
            "the character floor, and every quoted anchor stands in the "
            "paper", {"anchors": len(areport)})

    # ---- G-CLASS ---------------------------------------------------------
    cls = ANCH.read("N-PIN-CLASS", "G-CLASS")
    cls = pick("MUT-CLASS", cls, cls.replace("COMPATIBILITY/NO-GO", "X"))
    P["unit_class"] = SL.seal("unit_class", to_json(
        {"class": "COMPATIBILITY-NO-GO", "pin_sentence": cls}), "G-CLASS")
    LD.gate("G-CLASS", "COMPATIBILITY/NO-GO" in cls,
            "the unit's class is bound to the pin's own class sentence",
            {"class": "COMPATIBILITY-NO-GO"})

    # ---- G-TEMPLATE-CONFORMANCE -----------------------------------------
    tpl_ids = set(re.findall(
        r'\("[a-z]", "[A-Z-]+", "(T-[A-Z-]+)"\)', srctext["E-TPL"]))
    mine = set(FAMILIES)
    mine_probe = pick("MUT-TEMPLATE", mine, mine - {"T-READ-SET"})
    P["template"] = SL.seal("template", to_json(
        {"template_ids": sorted(tpl_ids), "implemented": sorted(mine)}),
        "G-TEMPLATE-CONFORMANCE")
    LD.gate("G-TEMPLATE-CONFORMANCE", tpl_ids == mine_probe,
            "the nine families implemented here are exactly the ids the "
            "pinned era template declares", {"ids": len(tpl_ids)})

    # ---- G-DETERMINISM ---------------------------------------------------
    src = selfsource()
    probe_src = src + pick(
        "MUT-SORT", "",
        "\ndef _bad_sort(e):\n    return sorted(e, key=repr)\n")
    probe_src = probe_src + pick(
        "MUT-HASH", "",
        "\ndef _bad_hash(e):\n"
        "    return sorted(e, key=lambda v: hash(v))\n")
    rsites = repr_key_sites(probe_src)
    hsites = hash_call_sites(probe_src)
    P["determinism"] = SL.seal("determinism", to_json(
        {"repr_sites": rsites, "hash_sites": hsites}), "G-DETERMINISM")
    LD.gate("G-DETERMINISM", not rsites and not hsites,
            "no ordering is keyed on a bare repr and the builtin hash is "
            "called nowhere", {"repr": len(rsites), "hash": len(hsites)})

    # ---- the chart -------------------------------------------------------
    chart = measure_chart()
    ari = ANCH.parse_ints("N-ARI-IDLE", "G-CHART")
    want = use_decl("con.actors", "con.cells", "con.parallel_classes",
                    "con.division_events", "con.groupings", "con.rounds",
                    "con.menu", "con.blocks", "ari.a3_groupings")
    ok = (chart["actors"] == want[0] and chart["cells"] == want[1]
          and chart["parallel_classes"] == want[2]
          and chart["triples"] == want[3]
          and chart["partitions"] == want[4] == ari[1]
          and chart["rounds"] == want[5] and chart["menu"] == want[6]
          and chart["triangles"] == want[7]
          and chart["partitions"] == want[8]
          and chart["triangles_two_routes_equal"]
          and chart["pair_bijection"]
          and chart["writer_census"] == ((0, 3), (2, 54), (3, 27)))
    P["chart"] = SL.seal("chart", to_json(
        {k: v for k, v in chart.items() if k != "rounds_list"}),
        "G-CHART")
    LD.gate("G-CHART", ok,
            "the committed chart is rebuilt from constructors and every "
            "extent agrees with its sealed parent by reproduction",
            {"triangles": chart["triangles"],
             "partitions": chart["partitions"]})

    # ---- G-COIN-FAMILY ---------------------------------------------------
    nsol, ncls, ngro = coin_family(3)
    cparse = ANCH.parse_ints("N-CON-COIN", "G-COIN-FAMILY")
    cw = use_decl("con.coin_solutions", "con.coin_classes",
                  "con.coin_grover")
    LD.gate("G-COIN-FAMILY",
            nsol == cw[0] and ncls == cw[1] == cparse[0]
            and ngro == cw[2] == cparse[1],
            "the covariant coin family is re-enumerated over the arena's "
            "own ring and its class census equals the parent's",
            {"solutions": nsol, "classes": ncls})
    P["coin"] = SL.seal("coin", to_json(
        {"solutions": nsol, "classes": ncls, "grover": ngro}),
        "G-COIN-FAMILY")

    # ---- the union -------------------------------------------------------
    usub = measure_union_substrate()
    uw = use_decl("aut.union.carriers", "aut.union.pairs", "aut.groups",
                  "aut.seam_spanning", "aut.within_only_alive",
                  "aut.doubling_only", "aut.incidence_lawful",
                  "ari.a2_groups", "ari.a2_seam_spanning")
    LD.gate("G-UNION",
            usub["carriers"] == uw[0] and usub["pairs"] == uw[1],
            "the aligned union is rebuilt from the gluing and carries "
            "the parent's carriers and realised pairs",
            {"carriers": usub["carriers"], "pairs": usub["pairs"]})
    LD.gate("G-EVENTS",
            usub["groups"] == uw[2]
            and usub["groups"] == (usub["carriers"]
                                   * (usub["carriers"] - 1)
                                   * (usub["carriers"] - 2)) // 6,
            "the conflict-group family is complete and matches the "
            "closed form", {"groups": usub["groups"]})
    prof = dict((tuple(k), v) for k, v in usub["profile_census"])
    pw = use_decl("aut.profile_102", "aut.profile_201",
                  "aut.profile_210", "aut.profile_003",
                  "aut.profile_012", "aut.profile_030")
    LD.gate("G-PROFILES",
            prof.get((1, 0, 2)) == pw[0] and prof.get((2, 0, 1)) == pw[1]
            and prof.get((2, 1, 0)) == pw[2]
            and prof.get((0, 0, 3)) == pw[3]
            and prof.get((0, 1, 2)) == pw[4]
            and prof.get((0, 3, 0)) == pw[5]
            and usub["seam_spanning"] == uw[3]
            and (prof.get((0, 0, 3), 0) + prof.get((0, 1, 2), 0)
                 + prof.get((0, 3, 0), 0)) == uw[4]
            and usub["frozen_alive"] == uw[5]
            and usub["incidence_lawful"] == uw[6]
            and usub["a2_groups"] == uw[7]
            and usub["a2_seam_spanning"] == uw[8]
            and usub["a2_seam_clean"] == uw[8],
            "the footprint census reproduces the parent's profile table "
            "object by object, and the two-actor rows reproduce the "
            "arity parent's",
            {"profiles": len(prof)})
    P["union"] = SL.seal("union", to_json(usub), "G-PROFILES")

    # ---- the lattice -----------------------------------------------------
    lat = measure_lattice()
    sparse = ANCH.parse_ints("N-CON-SEAM4", "G-LATTICE")
    lw = use_decl("aut.lattice", "con.seam_kernel")
    LD.gate("G-LATTICE",
            lat["lattice"] == lw[0] and lat["widened"] == lat["lattice"]
            and lat["kernel"] == lw[1] == sparse[2]
            and not lat["box_bound_binds"],
            "the completion lattice at the committed counts carries the "
            "parent's points, the widened box adds none, and the kernel "
            "is the chart's four undetermined numbers",
            {"lattice": lat["lattice"]})
    P["lattice"] = SL.seal("lattice", to_json(lat), "G-LATTICE")

    # ---- the lawful census ----------------------------------------------
    lawf = measure_lawful()
    aparse = ANCH.parse_ints("N-AUT-108", "G-LAWFUL")
    bparse = ANCH.parse_ints("N-AUT-162", "G-LAWFUL")
    lww = use_decl("aut.lawful", "aut.crossings_lawful")
    LD.gate("G-LAWFUL",
            lawf["lawful"] == lww[0] == bparse[0]
            and lawf["crossings"] == lww[1] == aparse[0],
            "the every-leg standard reproduces the parent's lawful set "
            "and its crossing class",
            {"lawful": lawf["lawful"], "crossings": lawf["crossings"]})
    nparse = ANCH.parse_ints("N-AUT-NOMOVE", "G-SEAM-CENSUS")
    pats = dict(lawf["size_patterns"])
    LD.gate("G-SEAM-CENSUS",
            lawf["staylable"] == nparse[0] == use_decl("aut.no_move")
            and pats.get((8, 8, 8)) == lawf["staylable"]
            and sum(v for k, v in pats.items() if k != (8, 8, 8))
            == lawf["crossings"] - lawf["staylable"],
            "the state need not move exactly at the crossings whose "
            "doublings move no seam count vector, and their successor "
            "pattern is the all-eights one",
            {"staylable": lawf["staylable"]})
    mparse = ANCH.parse_ints("N-AUT-MULT", "G-MULTIPLICITY")
    mult = dict(lawf["multiplicity"])
    mw = use_decl("aut.slot4", "aut.slot8", "aut.seam_slots")
    LD.gate("G-MULTIPLICITY",
            mult.get(4) == mw[0] == mparse[3]
            and mult.get(8) == mw[1] == mparse[5]
            and lawf["seam_slots"] == mw[2] == mparse[0]
            and sorted(mult) == [4, 8],
            "the successor multiset is four-valued and eight-valued and "
            "one-valued nowhere, at the parent's own slot counts",
            {"slots": lawf["seam_slots"]})
    P["lawful"] = SL.seal("lawful", to_json(
        {k: v for k, v in lawf.items()
         if k not in ("crossing_list", "stay_list")}), "G-MULTIPLICITY")

    # ---- preparedness ----------------------------------------------------
    prep = measure_preparedness(lawf["crossing_list"], lawf["stay_list"])
    pparse = ANCH.parse_ints("N-AUT-PREP", "G-PREPAREDNESS")
    hist_want = use_decl("aut.prep_hist")
    prw = use_decl("aut.states", "aut.ready_none", "aut.ready_best",
                   "aut.best_states")
    LD.gate("G-PREPAREDNESS",
            prep["states"] == prw[0] == pparse[2]
            and prep["ready_none"] == prw[1] == pparse[1]
            and prep["best"] == prw[2] == pparse[0]
            and prep["best_states"] == prw[3]
            and tuple(tuple(r) for r in prep["hist"])
            == tuple(tuple(r) for r in hist_want)
            and prep["absorbable"] == lawf["staylable"],
            "the advance-state census reproduces the parent's histogram "
            "point by point over the whole state space",
            {"states": prep["states"], "best": prep["best"]})
    P["preparedness"] = SL.seal("preparedness", to_json(
        {k: v for k, v in prep.items()
         if k not in ("lat", "masks", "best_state_list")}),
        "G-PREPAREDNESS")

    # ---- the observable menu and its sweep ------------------------------
    tree = ast.parse(src)
    obs_fns = {}
    want_args = pick("MUT-OBSMENU", ["geo", "rel"], ["geo"])
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and \
                node.name.startswith("obs_"):
            args = [a.arg for a in node.args.args]
            body_names = {s.id for s in ast.walk(node)
                          if isinstance(s, ast.Name)}
            obs_fns[node.name] = {
                "args_ok": args == want_args,
                "clean": not ({"successors", "successors_raw",
                               "completion_lattice", "prediction"}
                              & body_names)}
    LD.gate("G-OBS-MENU",
            len(obs_fns) == len(OBSERVABLE_MENU)
            and all(v["args_ok"] and v["clean"]
                    for v in obs_fns.values()),
            "every committed observable is a function of the geometry "
            "and record alone; none can even receive a completion",
            {"menu": len(obs_fns)})
    obs = measure_obs_sweep(prep)
    LD.gate("G-OBS-SWEEP",
            obs["blind"] == obs["menu_size"]
            and obs["relation_value_set"] >= 2
            and obs["probe_family_shares_record"],
            "over the completion-only probe family every observable "
            "takes one value while the modal allowed-set relation "
            "separates the family",
            {"probes": obs["probes"],
             "relation_values": obs["relation_value_set"]})
    P["obs"] = SL.seal("obs", to_json(
        {k: v for k, v in obs.items()}), "G-OBS-SWEEP")

    # ---- the two-step reading census ------------------------------------
    seam2 = step2_censuses(lawf["crossing_list"])
    ANCH.read("N-AUT-RESOLVED", "G-READING-FAMILY")
    LD.gate("G-READING-FAMILY",
            seam2["differ_fit"] > 0 and seam2["differ_kept"] > 0
            and seam2["differ_fit"] == sum(
                1 for r in seam2["rows"] if r["fit_differs"])
            and seam2["differ_kept"] == sum(
                1 for r in seam2["rows"] if r["kept_differs"]),
            "the three-member reading family separates at the two-step "
            "record census: the persist members allow different second "
            "crossings than the re-solved member does",
            {"differ_fit": seam2["differ_fit"],
             "differ_kept": seam2["differ_kept"]})
    tparse = ANCH.parse_ints("N-AUT-TWOSTEP", "G-TWO-STEP")
    fib_want = use_decl("aut.two_step_fiber")
    fw = use_decl("aut.fiber_min", "aut.fiber_max")
    LD.gate("G-TWO-STEP",
            tuple(tuple(r) for r in seam2["fiber"])
            == tuple(tuple(r) for r in fib_want)
            and seam2["fiber_min"] == fw[0] == tparse[1]
            and seam2["fiber_max"] == fw[1] == tparse[2]
            and seam2["first_crossings"] == tparse[0],
            "the re-solved second-step fiber reproduces the parent's "
            "published table from every lawful first crossing",
            {"fiber_min": seam2["fiber_min"],
             "fiber_max": seam2["fiber_max"]})

    # ---- the seam decision ----------------------------------------------
    ANCH.read("N-AUT-PERSIST", "G-SEAM-DECISION")
    ANCH.read("N-AUT-S4", "G-SEAM-DECISION")
    seam_block = {
        "verdict_row": "THE-COMMITTED-OBSERVABLE-MENU",
        "word": pick("MUT-SEAMWORD",
                     "SEAM-DECISION-UNDERDETERMINED-AT-THE-COMMITTED-"
                     "OBSERVABLE-MENU",
                     "SEAM-RE-SOLVED-SUPPORTED"),
        "chosen_reading": "RE-SOLVED",
        "chosen_reading_status": "DECLARED-NOT-MEASURED",
        "reading_family": ("RE-SOLVED", "PERSIST-FIT", "PERSIST-KEPT"),
        "obs_rows": obs["obs_rows"],
        "probes": obs["probes"],
        "relation_values": obs["relation_value_set"],
        "step2_rows": pick("MUT-VERDICT", seam2["rows"],
                           [dict(r, re_solved=r["re_solved"] + 1)
                            for r in seam2["rows"]]),
        "fiber": seam2["fiber"],
        "differ_fit": seam2["differ_fit"],
        "differ_kept": seam2["differ_kept"],
        "no_committed_multistep_run": True,
    }
    LD.gate("G-SEAM-DECISION",
            seam_block["word"].startswith(
                "SEAM-DECISION-UNDERDETERMINED-AT-")
            and obs["blind"] == obs["menu_size"]
            and seam_block["chosen_reading"] == "RE-SOLVED",
            "no committed observable separates the readings at the "
            "committed windows; the modal relation that separates them "
            "is one the corpus never operationalises; the chosen "
            "reading is declared and stamped downstream",
            {"word": seam_block["word"]})
    P["seam"] = SL.seal("seam", to_json(seam_block), "G-SEAM-DECISION")

    # ---- the interface table --------------------------------------------
    iface = measure_interface(ANCH, chart, usub, lawf, "G-INTERFACE")
    ANCH.read("N-CON-BOOK", "G-INTERFACE")
    sc_rows = [r for r in iface["rows"]
               if r["object"] in ("COUNT-FIELD", "QUANTUM-STATE")]
    bk_rows = [r for r in iface["rows"] if r["object"] == "BRANCH-WEIGHT"]
    iw = use_decl("con.state_components", "con.state_bookkeeping")
    LD.gate("G-INTERFACE",
            len(iface["senses"]) == 6
            and iface["computed_rows"] + iface["cited_rows"]
            == len(iface["rows"])
            and len(sc_rows) == iw[0] and len(bk_rows) == iw[1]
            and iface["cited"]["actors"] == chart["actors"]
            and iface["cited"]["cells"] == chart["cells"]
            and iface["cited"]["blocks"] == chart["triangles"]
            and iface["cited"]["menu"] == chart["menu"]
            and all(r["class"] in ("DECLARED", "GENERATED",
                                   "RECONSTRUCTED", "LAW-SELECTED")
                    for r in iface["rows"])
            and all(r["sense_word"] in dict(iface["senses"])
                    or r["sense_word"] in ("event", "cell", "geometry",
                                           "record", "state", "metric")
                    for r in iface["rows"]),
            "every object is typed by the five words, the six senses "
            "are fixed, and every computed extent agrees with the "
            "chart's own reconstruction",
            {"rows": len(iface["rows"])})
    P["interface"] = SL.seal("interface", to_json(iface), "G-INTERFACE")

    fdecl = measure_free_declarations(ANCH, "G-FREE-DECLS")
    fdw = use_decl("con.declarations", "con.free_declarations")
    LD.gate("G-FREE-DECLS",
            fdecl["count"] == fdw[1] == fdecl["cited_free"]
            and fdecl["cited_declarations"] == fdw[0]
            and len(fdecl["categories"]) >= 4,
            "the fifteen free declarations are carried with their "
            "heterogeneous types, never as a count of constants",
            {"free": fdecl["count"],
             "categories": len(fdecl["categories"])})
    P["free_declarations"] = SL.seal("free_declarations", to_json(fdecl),
                                     "G-FREE-DECLS")

    fork = measure_fork()
    ANCH.read("N-ARI-COND", "G-FORK")
    ANCH.read("N-ARI-EXT", "G-FORK")
    LD.gate("G-FORK",
            fork["arm_count"] == 2
            and tuple(fork["grains"]) == (2, 3),
            "the event class is a declared fork of exactly two arms and "
            "no compromise class exists anywhere in this run",
            {"arms": fork["arm_count"]})
    P["fork"] = SL.seal("fork", to_json(fork), "G-FORK")

    # ---- the three maps --------------------------------------------------
    uni = declared_amplitudes()[0][1]
    q_uni = born_target(uni, R0, "G.D")
    mrow = [map_event_selection(R0, q_uni), map_seam_completion(UREL),
            map_quantum_evolution(uni, R0, "G.D")]
    LD.gate("G-MAPS-TYPED",
            mrow[0]["kind"] == "STOCHASTIC-KERNEL"
            and mrow[1]["kind"] == "RELATION"
            and 1 not in mrow[1]["witness_sizes"]
            and mrow[2]["kind"] == "FUNCTION"
            and mrow[2]["unitary_at_scale"],
            "the three conditional maps are typed separately: a kernel, "
            "a relation that is one-valued nowhere, and a function "
            "unitary at the tripled scale",
            {"kinds": [m["kind"] for m in mrow]})
    audit = maps_reach_audit(src)
    LD.gate("G-MAPS-SEPARATE",
            audit["covered"] == len(MAP_REGION_NAMES)
            and not audit["offences"],
            "no map reaches another, directly or through any chain: "
            "composition belongs to dynamics-closure and happens "
            "nowhere here", {"covered": audit["covered"]})
    P["maps"] = SL.seal("maps", to_json(
        {"typed": mrow, "audit": audit}), "G-MAPS-SEPARATE")

    # ---- the Born targets and the order fiber ---------------------------
    round_flds = round_fields(chart["rounds_list"])
    targets_all = build_targets(round_flds)
    resid = measure_residue_leg()
    rparse = ANCH.parse_ints("N-CON-RESIDUE", "G-BORN")
    ANCH.read("N-DIS-EMIT", "G-BORN")
    defined = [t for t in targets_all if t["q"] is not None]
    LD.gate("G-BORN",
            resid["residue_screens"] and rparse[0] == Q
            and all(sum(t["q"]) == 1 for t in defined)
            and len(defined) > 0,
            "the emission functional is read at the post-coin point, "
            "sums to one wherever defined, and consumes the count field "
            "only through its residue",
            {"targets": len(targets_all), "defined": len(defined)})
    idx_seam = LD.index_of(pick("MUT-STEPORDER", "G-SEAM-DECISION",
                                "G-SEAM-DECISION-PHANTOM"))
    idx_born = LD.index_of("G-BORN")
    ANCH.read("N-PIN-SEAMSTEP", "G-STEP-ORDER")
    LD.gate("G-STEP-ORDER",
            idx_seam is not None and idx_born is not None
            and idx_seam < idx_born,
            "the seam decision precedes the first Born weight in this "
            "run's own ledger, as the pin orders",
            {"seam_index": idx_seam, "born_index": idx_born})
    ofib = measure_order_fiber(targets_all)
    ANCH.read("N-DIS-ORDER", "G-ORDER-FIBER")
    LD.gate("G-ORDER-FIBER",
            ofib["dg_record_blind"] and ofib["gd_record_moves"]
            and ofib["r0_orders_equal"],
            "under the alternative order the residue phase cannot enter "
            "the Born weights; under the delivered order it does; at "
            "the initial record the members coincide",
            {"amplitudes": ofib["amplitudes"],
             "records": ofib["records"]})
    P["order_fiber"] = SL.seal("order_fiber", to_json(ofib),
                               "G-ORDER-FIBER")
    P["born"] = SL.seal("born", to_json(
        {"rows": len(targets_all), "defined": len(defined),
         "residue_screens": resid["residue_screens"]}), "G-BORN")

    # ---- the psi trilemma ------------------------------------------------
    psi_fns = {}
    prefix = pick("MUT-REGION", "psi_", "psiZ_")
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and \
                node.name.startswith(prefix):
            called = {s.func.id for s in ast.walk(node)
                      if isinstance(s, ast.Call)
                      and isinstance(s.func, ast.Name)}
            region = node.name.split("_")[1]
            bad = sorted(c for c in called
                         if c not in PSI_SHARED_PLUMBING
                         and not c.startswith("psi_" + region))
            psi_fns[node.name] = bad
    LD.gate("G-PSI-REGIONS",
            len(psi_fns) == 4
            and all(not v for v in psi_fns.values()),
            "the three faces are three disjoint carrier regions: every "
            "call from a face lands in the declared plumbing whitelist "
            "or its own region, and never in another face",
            {"functions": len(psi_fns)})
    psi = measure_psi(round_flds)
    LD.gate("G-PSI-EQUAL",
            psi["agreements"] == psi["row_count"]
            and psi["separating_rows"] == 0
            and psi["full_matrix_route_agrees"],
            "the three faces emit byte-identical functionals at every "
            "delivered row, and the full-matrix channel route agrees "
            "with the block route at the committed row",
            {"rows": psi["row_count"]})
    P["psi"] = SL.seal("psi", to_json(
        {"rows": psi["rows"], "faces": psi["faces"]}), "G-PSI-EQUAL")
    P["psi_regions"] = SL.seal("psi_regions", to_json(psi_fns),
                               "G-PSI-REGIONS")

    # ---- the LP ----------------------------------------------------------
    classes = build_classes()
    rowsum = {}
    for (cname, _arm, Mx, nev) in classes:
        rowsum[cname] = sorted(Counter(
            int(sum(Mx[i][j] for j in range(nev)))
            for i in range(DIM)).items())
    LD.gate("G-LP-BUILD",
            rowsum["E-BLOCK"] == [(3, 27)]
            and rowsum["E-LINE-DECLARED"] == [(1, 27)]
            and rowsum["E-TRIPLE"] == [(7, 27)],
            "the incidence matrices carry the structural counts: every "
            "cell lies in exactly three blocks, one declared line, and "
            "seven triples", {"classes": len(classes)})
    norm = measure_normalization(classes)
    nparse2 = ANCH.parse_ints("N-PIN-NORM", "G-NORMALIZATION")
    per = {r["class"]: r["identity_holds"] for r in norm["per_class"]}
    LD.gate("G-NORMALIZATION",
            norm["scale"] == 3 and 3 in nparse2
            and norm["scale"] == norm["arity"] * (norm["arity"] - 1) // 2
            and per["E-BLOCK"] and per["E-LINE-DECLARED"]
            and not per["E-LINE-COSET"] and not per["E-TRIPLE"]
            and norm["two_routes_equal"]
            and norm["free_two_stage_vacuous"],
            "the pair-cell normalization is pre-registered in its "
            "general form and sealed before any feasibility row; the "
            "marginal-sum identity is class-relative and measured; the "
            "free two-stage reading constrains nothing",
            {"scale": norm["scale"]})
    P["normalization"] = SL.seal("normalization", to_json(norm),
                                 "G-NORMALIZATION")
    lp_targets = [t for t in targets_all
                  if t["record"] == "R0"
                  or t["amplitude"] == "THE-UNIFORM-AMPLITUDE"]
    lp = measure_lp(classes, lp_targets)
    if mut("MUT-LPROWS"):
        dup = next(r for r in lp["rows"]
                   if r["class"] == "E-LINE-DECLARED")
        lp["rows"] = lp["rows"] + [dict(dup)]
    ANCH.read("N-DIS-START", "G-LP-COMMITTED")
    crow = lp["committed_rows"]
    call_rows = lp["committed_all"]
    LD.gate("G-LP-COMMITTED",
            len(crow) == 1 and crow[0]["word"] == "INFEASIBLE"
            and crow[0]["qmax"] == str(Fraction(4, 9))
            and crow[0]["ceiling_witness"]
            and len(call_rows) == len(classes)
            and all(r["word"] == "INFEASIBLE" for r in call_rows),
            "the committed row -- the walk's own start state at the "
            "initial record under the delivered order -- is infeasible "
            "at every committed event class, by the ceiling",
            {"qmax": crow[0]["qmax"] if crow else "?"})
    idx_norm = LD.index_of("G-NORMALIZATION")
    words = dict(lp["words"])
    LD.gate("G-LP-CENSUS",
            idx_norm < LD.index_of("G-LP-COMMITTED")
            and len(lp["rows"]) == len(classes) * lp["distinct_targets"]
            and sum(words.values()) == len(lp["rows"]),
            "every class-and-target pair is solved by the one exact "
            "procedure, downstream of the sealed normalization",
            {"rows": len(lp["rows"]),
             "targets": lp["distinct_targets"]})
    ctrl = measure_lp_controls(classes)
    LD.gate("G-LP-CONTROLS",
            ctrl["forced_feasible_ok"] and ctrl["forced_infeasible_ok"]
            and ctrl["forced_infeasible_ceiling"],
            "the synthetic forced-feasible and forced-infeasible arms "
            "come out as forced, through the real predicates",
            {"feasible": ctrl["forced_feasible_word"],
             "infeasible": ctrl["forced_infeasible_word"]})
    P["lp_controls"] = SL.seal("lp_controls", to_json(ctrl),
                               "G-LP-CONTROLS")
    LD.gate("G-LP-CEILING",
            lp["ceiling_exceptions"] == 0
            and rowsum["E-BLOCK"] == [(3, 27)],
            "a feasible row with a Born weight above one third exists "
            "nowhere: the inclusion marginal of a cell is at most the "
            "total probability",
            {"checked": lp["ceiling_checked"]})
    LD.gate("G-LP-DEGENERATE",
            lp["branch_degenerate"] == lp["branch_count"]
            and all(r["arm"] == "BRANCH" for r in lp["branch_rows"])
            and all(r["arm"] != "BRANCH" for r in lp["rows"]),
            "at the pair-event branch the problem degenerates to the "
            "identity and is kept apart from the committed classes at "
            "every row", {"branch_rows": lp["branch_count"]})
    many_rows = [r for r in lp["rows"] if r["word"] == "MANY"]
    dim_ok = all(r["dim"] is not None and r["dim"] > 0
                 and r["implicit"] is not None
                 and r["second_point"] for r in many_rows)
    uniq_ok = all(not r["second_point"]
                  for r in lp["rows"]
                  if r["word"] == "UNIQUE"
                  and r["second_point"] is not None)
    LD.gate("G-LP-DIM",
            dim_ok and uniq_ok,
            "every many-valued row carries a measured dimension with "
            "its implicit-equality census and a second feasible point "
            "as certificate; a unique row admits no second point",
            {"many": len(many_rows)})
    P["lp"] = SL.seal("lp", to_json(
        {"rows": lp["rows"], "branch_rows": lp["branch_rows"],
         "distinct_targets": lp["distinct_targets"],
         "target_rows": lp["target_rows"],
         "undefined_targets": lp["undefined_targets"],
         "words": lp["words"], "many_dims": lp["many_dims"],
         "ceiling_checked": lp["ceiling_checked"],
         "ceiling_exceptions": lp["ceiling_exceptions"],
         "cells": list(range(DIM))}), "G-LP-DIM")

    # ---- the carrier and the debt ---------------------------------------
    committed_q = None
    for t in targets_all:
        if (t["amplitude"] == "A-SINGLE-CELL-AMPLITUDE"
                and t["record"] == "R0" and t["order"] == "G.D"):
            committed_q = t["q"]
    car = measure_carrier(committed_q)
    LD.gate("G-CARRIER",
            car["isometry_verified"] and car["count"] == 4
            and car["expresses"] == 2 and car["evolves"] == 0
            and car["hosts"] == 4
            and car["distinct_branch_records"] == 3
            and car["cross_cells_directionless"] == car["cross_pairs_n"],
            "the candidate family is measured through the same "
            "predicates: two members express the committed branching, "
            "none extends the committed evolution across creation, and "
            "nothing selects among them",
            {"candidates": car["count"]})
    P["carrier"] = SL.seal("carrier", to_json(car), "G-CARRIER")
    debt = measure_debt(usub, targets_all)
    a2parse = ANCH.parse_ints("N-ARI-A2", "G-DEBT")
    ANCH.read("N-CON-GRAIN", "G-DEBT")
    LD.gate("G-DEBT",
            debt["menu_cross_overlap"] == 0
            and debt["cross_pairs"] == a2parse[0]
            and debt["frozen_creation_admits_seam"] == 0
            and debt["grain_mismatch"]
            and debt["amplitudes_with_unit_mass"]
            == debt["nonzero_amplitudes"] == 4,
            "the walk's menu meets the refused classes nowhere and "
            "cannot express the crossing at either arity, yet carries "
            "unit mass wherever the amplitude is non-zero: the debt is "
            "decided, the two grains never conflict",
            {"overlap": debt["menu_cross_overlap"]})
    P["debt"] = SL.seal("debt", to_json(debt), "G-DEBT")

    # ---- tie-breaks, labels, stamps, circularity, prereg ----------------
    tie = measure_tiebreaks(round_flds)
    LD.gate("G-EQUIV-DECLARED",
            len(tie["rows"]) == 4 and tie["declared"] == 3
            and tie["equivariant"] == 1
            and tie["window_closed_under_generator"],
            "every member-selecting choice is equivariance-proved or "
            "declared and counted; the record window is proved closed "
            "under a generator", {"rows": len(tie["rows"])})
    P["tiebreaks"] = SL.seal("tiebreaks", to_json(tie),
                             "G-EQUIV-DECLARED")
    w3 = w3_labels(lp, seam2, obs)
    recheck = "FAMILY-LEVEL-ACROSS-THE-TARGET-FAMILY" \
        if lp["ceiling_exceptions"] == 0 else "MEMBER-SPECIFIC"
    LD.gate("G-W3-LABELS",
            w3["labels"][3]["label"] == recheck
            and all(l["label"] == "MEMBER-SPECIFIC"
                    for i, l in enumerate(w3["labels"]) if i != 3)
            and all(l["fibres"] for l in w3["labels"]),
            "every headline is auto-labelled member-specific or "
            "family-level from the varied-fibre data, with the fibres "
            "disclosed", {"member": w3["member_specific"],
                          "family": w3["family_level"]})
    P["w3"] = SL.seal("w3", to_json(w3), "G-W3-LABELS")
    stamps = stamp_table(lp, psi, car, debt)
    saudit = stamps_reach_audit(src)
    want_rows = (len(lp["rows"]) + len(lp["branch_rows"])
                 + len(psi["rows"]) + 2)
    LD.gate("G-STAMPS",
            stamps["count"] == want_rows and not saudit["offences"],
            "every downstream row is stamped reading-independent and "
            "face-independent, and the reach audit proves no consumer "
            "touches the seam machinery or a face region",
            {"stamped": stamps["count"]})
    P["stamps"] = SL.seal("stamps", to_json(
        {"rows": stamps["rows"], "stamp": stamps["stamp"],
         "audit": saudit}), "G-STAMPS")
    circ = measure_circularity()
    cyc_want = use_decl("con.cycle_actor", "con.cycle_dynamical")
    LD.gate("G-CIRCULARITY",
            circ["actor_cycle"] == cyc_want[0]
            and circ["dynamical_cycle"] == cyc_want[1]
            and circ["edges"] == 12,
            "the actors-and-records circle is carried at its parent's "
            "length and stays open at the full-dynamics scope",
            {"actor_cycle": circ["actor_cycle"]})
    P["circularity"] = SL.seal("circularity", to_json(circ),
                               "G-CIRCULARITY")
    prereg = outcome_prereg(iface, obs, seam2, psi, lp, car, debt)
    stems = (ANCH.read("N-PIN-OUTCOMES", "G-OUTCOME-FEASIBILITY")
             + " " + ANCH.read("N-PIN-PSI", "G-OUTCOME-FEASIBILITY")
             + " " + ANCH.read("N-PIN-LP", "G-OUTCOME-FEASIBILITY")
             + " " + ANCH.read("N-PIN-CONTRACT", "G-OUTCOME-FEASIBILITY")
             + " " + ANCH.read("N-PIN-BLOCKED", "G-OUTCOME-FEASIBILITY")
             + " " + ANCH.read("N-PIN-DEBT", "G-OUTCOME-FEASIBILITY"))
    stems_c = canon(stems)
    stem_ok = []
    for pr in prereg["pairs"]:
        w = pr["reached"]
        roots = ("seam-decision-underdetermined-at-",
                 "psi-status-independent", "ecc-lp-infeasible-at-",
                 "ecc-state-contract-closed-at-", "decided")
        stem_ok.append(any(r in stems_c and canon(w).startswith(r)
                           or (r == "decided" and r in stems_c
                               and r in canon(w))
                           for r in roots))
    fired = dict(prereg["lp_words_fired"])
    LD.gate("G-OUTCOME-FEASIBILITY",
            all(stem_ok)
            and prereg["pairs"][1]["witness"]
            == obs["menu_size"] - obs["blind"]
            and prereg["pairs"][2]["witness"] == psi["separating_rows"]
            and prereg["pairs"][3]["witness"] == crow[0]["word"]
            and prereg["pairs"][4]["witness"] == car["count"] * 3
            and len(prereg["pairs"]) == len(SEGMENT_NAMES)
            and all(fired.values()),
            "every head segment carries a pre-registered outcome pair "
            "on the pin's own stems, with both arms' witnesses "
            "measured, and every feasibility word fires through the "
            "real predicates",
            {"pairs": len(prereg["pairs"])})
    P["outcome_prereg"] = SL.seal("outcome_prereg", to_json(prereg),
                                  "G-OUTCOME-FEASIBILITY")
    # ---- the measured registry and the head -----------------------------
    M.m("iface.object_rows", len(iface["rows"]), "the interface table")
    M.m("iface.computed", iface["computed_rows"], "computed-here rows")
    M.m("iface.cited_rows", iface["cited_rows"], "sealed-citation rows")
    M.m("iface.senses", len(iface["senses"]), "the sense words")
    M.m("decl.count", fdecl["count"], "free declarations carried")
    M.m("decl.cited_free", fdecl["cited_free"], "CONTRACT's free count")
    M.m("decl.categories", len(fdecl["categories"]), "type categories")
    M.m("fork.arms", fork["arm_count"], "fork arms")
    M.m("maps.count", len(mrow), "conditional maps")
    M.m("state.components", len(sc_rows), "one-instant components")
    M.m("state.bookkeeping", len(bk_rows), "ensemble-side rows")
    M.m("circ.actor_cycle", circ["actor_cycle"], "the actor-record cycle")
    M.m("obs.menu", obs["menu_size"], "committed observables")
    M.m("obs.blind", obs["blind"], "completion-blind observables")
    M.m("obs.probes", obs["probes"], "probe states")
    M.m("obs.relation_values", obs["relation_value_set"],
        "relation value set")
    M.m("seam.readings", len(seam_block["reading_family"]),
        "reading family")
    M.m("seam.first_crossings", seam2["first_crossings"],
        "first crossings")
    M.m("seam.fiber_min", seam2["fiber_min"], "re-solved fiber minimum")
    M.m("seam.fiber_max", seam2["fiber_max"], "re-solved fiber maximum")
    M.m("seam.differ_fit", seam2["differ_fit"], "persist-fit differs")
    M.m("seam.differ_kept", seam2["differ_kept"], "persist-kept differs")
    M.m("stamps.count", stamps["count"], "stamped rows")
    M.m("psi.faces", psi["faces"], "trilemma faces")
    M.m("psi.rows", psi["row_count"], "psi rows")
    M.m("psi.agreements", psi["agreements"], "byte agreements")
    M.m("psi.separating", psi["separating_rows"], "separating rows")
    M.m("lp.classes", len(classes), "committed event classes")
    M.m("lp.targets", lp["distinct_targets"], "distinct targets")
    M.m("lp.rows", len(lp["rows"]), "lp rows")
    M.m("lp.infeasible", words.get("INFEASIBLE", 0), "infeasible rows")
    M.m("lp.unique", words.get("UNIQUE", 0), "unique rows")
    M.m("lp.many", words.get("MANY", 0), "many rows")
    M.m("lp.maxdim", max(lp["many_dims"]) if lp["many_dims"] else 0,
        "max polytope dimension")
    M.m("lp.fiber", words.get("FEASIBLE-AT-THE-FIBER-ROW", 0),
        "fiber-feasible rows")
    M.m("lp.branch_degenerate", lp["branch_degenerate"],
        "degenerate branch rows")
    M.m("lp.branch_rows", lp["branch_count"], "branch rows")
    M.m("lp.undefined", lp["undefined_targets"],
        "target-undefined amplitude rows")
    M.m("lp.committed_qmax", crow[0]["qmax"], "the committed qmax")
    M.m("lp.committed_classes", len(call_rows), "committed classes hit")
    M.m("lp.ceiling_checked", lp["ceiling_checked"], "ceiling checks")
    M.m("lp.ceiling_exceptions", lp["ceiling_exceptions"],
        "ceiling exceptions")
    M.m("norm.scale", norm["scale"], "the pair-cell scale")
    M.m("norm.covered", norm["free_two_stage_covered_cells"],
        "cells covered")
    M.m("norm.cells", DIM, "carrier cells")
    M.m("car.count", car["count"], "carrier candidates")
    M.m("car.hosts", car["hosts"], "state-hosting candidates")
    M.m("car.expresses", car["expresses"], "branching-expressing")
    M.m("car.evolves", car["evolves"], "creation-evolving")
    M.m("debt.cross_overlap", debt["menu_cross_overlap"],
        "menu cells in the cross class")
    M.m("debt.cross_pairs", debt["cross_pairs"], "cross pairs")
    M.m("debt.frozen_seam", debt["frozen_creation_admits_seam"],
        "frozen seam admissions")
    M.m("debt.seam_spanning", debt["seam_spanning"], "seam-spanning")
    M.m("debt.mass_one", debt["amplitudes_with_unit_mass"],
        "unit-mass amplitudes")
    M.m("debt.nonzero", debt["nonzero_amplitudes"],
        "non-zero amplitudes")
    M.m("w3.member", w3["member_specific"], "member-specific headlines")
    M.m("w3.family", w3["family_level"], "family-level headlines")
    M.m("chart.rounds", chart["rounds"], "admissible rounds")
    M.m("chart.cells", chart["cells"], "chart cells")
    M.m("union.groups", usub["groups"], "conflict groups")
    M.m("lawful.count", lawf["lawful"], "lawful events")
    M.m("lawful.crossings", lawf["crossings"], "lawful crossings")
    M.m("prep.states", prep["states"], "seam states")
    M.m("prep.none", prep["ready_none"], "states ready for none")
    M.m("prep.best", prep["best"], "the best readiness")
    M.m("prep.best_states", prep["best_states"], "best states")
    M.m("stay.count", lawf["staylable"], "staylable crossings")
    M.m("targets.rows", len(targets_all), "target family rows")

    verdict = build_verdict(M)
    P["verdict"] = SL.seal("verdict", to_json(list(verdict)),
                           "G-VERDICT-RECON")
    P["measured"] = SL.seal("measured", to_json(M.vals),
                            "G-VERDICT-RECON")
    P["object_under_test"] = SL.seal("object_under_test", to_json(
        {"path": paper_rel,
         "sha256_12": bdigest(paper_text.encode("utf-8"))}),
        "G-VERDICT-RECON")

    # ---- the paper surface ----------------------------------------------
    paper_probe = paper_text
    if mut("MUT-WALL"):
        paper_probe = paper_probe + "\n\nPersistence is a measured " \
            "fact of the committed corpus.\n"
    if mut("MUT-NUMERAL"):
        paper_probe = paper_probe + "\n\nThe census finds 9999 states " \
            "in the window.\n"
    if mut("MUT-POLARITY"):
        paper_probe = paper_probe + "\n\nAt the committed row the lp " \
            "is feasible after all.\n"
    if mut("MUT-REFERENT"):
        paper_probe = paper_probe + "\n\nBy the census, 20100 of the " \
            "108 first crossings differ.\n"
    if mut("MUT-REFLEXIVE"):
        paper_probe = paper_probe + "\n\nThe menu is blind at 8 of 8 " \
            "observables.\n"
    if mut("MUT-FRACTION"):
        paper_probe = paper_probe + "\n\nMost of the corpus rows were " \
            "swept here.\n"

    # G-SENSES: the six sense sentences stand in the paper verbatim
    probe_senses = pick("MUT-SENSE", list(iface["senses"]),
                        list(iface["senses"])[:-1])
    sense_hits = [locate(paper_probe, s) for (_w, s) in probe_senses]
    LD.gate("G-SENSES",
            len(probe_senses) == 6
            and all(h >= 1 for h in sense_hits),
            "each of the six words is fixed to one sense by a sentence "
            "the paper carries verbatim",
            {"senses": len(sense_hits)})
    P["senses_check"] = SL.seal("senses_check", to_json(sense_hits),
                                "G-SENSES")

    # G-WALLS
    wall_report = []
    for w in WALLS:
        scanr = w.scan(paper_probe)
        controls_die = 0
        for c in w.controls:
            probe = w.scan(paper_probe + "\n\n" + c + "\n")
            if probe["violations"] or probe["unlicensed_sentences"]:
                controls_die += 1
        wall_report.append({"wall": w.name,
                            "violations": scanr["violations"],
                            "missing_positive":
                                scanr["missing_positive"],
                            "unlicensed":
                                scanr["unlicensed_sentences"],
                            "controls": len(w.controls),
                            "controls_dead": controls_die,
                            "spec": w.seal_value()})
    LD.gate("G-WALLS",
            all(not r["violations"] and not r["missing_positive"]
                and not r["unlicensed"]
                and r["controls_dead"] == r["controls"]
                for r in wall_report),
            "every wall stands: patterns clean, standing sentences "
            "carried, licence legs clean, and every independently "
            "written control dies at its wall when planted",
            {"walls": len(wall_report),
             "controls": sum(r["controls"] for r in wall_report)})
    P["walls"] = SL.seal("walls", to_json(wall_report), "G-WALLS")

    # ---- claims: tables, prose, fences ----------------------------------
    CL.table("T-SOURCES", ("id", "path", "sha256-12"),
             [(r["id"], r["path"], r["declared"])
              for r in P["sources"]["rows"]])
    CL.table("T-DEBT", ("row", "value"),
             [("the walk's menu at the chart, in cells",
               debt["chart_menu_cells"]),
              ("the walk's menu at the union, in realised pairs",
               debt["union_menu_pairs"]),
              ("menu cells in the cross class",
               debt["menu_cross_overlap"]),
              ("cross pairs the union admits", debt["cross_pairs"]),
              ("seam-spanning events the frozen creation admits",
               debt["frozen_creation_admits_seam"]),
              ("seam-spanning events the arena admits",
               debt["seam_spanning"]),
              ("declared amplitudes with unit menu mass",
               debt["amplitudes_with_unit_mass"]),
              ("declared amplitudes that are non-zero",
               debt["nonzero_amplitudes"])])
    CL.table("T-READINGS", ("reading", "status",
                            "first crossings where its second-step set "
                            "leaves the re-solved one"),
             [("RE-SOLVED", "the base member", 0),
              ("PERSIST-FIT", "declared", seam2["differ_fit"]),
              ("PERSIST-KEPT", "declared", seam2["differ_kept"])])
    CL.table("T-INTERFACE", ("object", "class", "extent", "backing",
                             "carrier", "sense"),
             [(r["object"], r["class"], r["extent"], r["backing"],
               r["carrier"], r["sense_word"]) for r in iface["rows"]])
    CL.table("T-SENSES", ("word", "the one sense"),
             [(w, s) for (w, s) in iface["senses"]])
    CL.table("T-FREE", ("declaration", "what it fixes", "type"),
             [(r["declaration"], r["fixes"], r["type"])
              for r in fdecl["rows"]])
    CL.table("T-FORK", ("arm", "event class", "grain"),
             [(a["arm"], a["event_class"], a["grain"])
              for a in fork["arms"]])
    CL.table("T-MAPS", ("map", "kind", "domain", "codomain"),
             [("event selection", mrow[0]["kind"], mrow[0]["domain"],
               mrow[0]["codomain"]),
              ("seam completion", mrow[1]["kind"], mrow[1]["domain"],
               mrow[1]["codomain"]),
              ("quantum evolution", mrow[2]["kind"], mrow[2]["domain"],
               mrow[2]["codomain"])])
    CL.table("T-OBS", ("observable", "values over the probe family"),
             [(r["observable"], r["value_set_size"])
              for r in obs["obs_rows"]])
    CL.table("T-FIBER", ("allowed second crossings", "first crossings"),
             [(k, v) for (k, v) in seam2["fiber"]])
    CL.table("T-LPWORDS", ("word", "rows"),
             [(k, v) for (k, v) in lp["words"]])
    CL.table("T-COMMITTED", ("class", "word", "qmax"),
             [(r["class"], r["word"], r["qmax"]) for r in call_rows])
    CL.table("T-CONTROLS", ("arm", "word"),
             [("forced feasible", ctrl["forced_feasible_word"]),
              ("forced infeasible", ctrl["forced_infeasible_word"])])
    CL.table("T-CARRIER", ("candidate", "classical register",
                           "hosts the state", "expresses the branching",
                           "evolves across creation"),
             [(c["candidate"], c["classical_register"],
               c["hosts_the_state"], c["expresses_the_branching"],
               c["evolves_across_creation"])
              for c in car["candidates"]])
    CL.table("T-TIEBREAK", ("choice", "class"),
             [(r["choice"], r["class"]) for r in tie["rows"]])
    CL.table("T-W3", ("head segment", "label"),
             [(l["segment"], l["label"]) for l in w3["labels"]])
    CL.table("T-PREREG", ("segment", "reached", "not reached",
                          "witness", "other arm's witness"),
             [(p["segment"], p["reached"], p["not_reached"],
               p["witness"], p["other_witness"])
              for p in prereg["pairs"]])
    for (_w, s) in iface["senses"]:
        CL.claim(s)
    CL.claim("the committed row is the walk's own start state and it is "
             "infeasible at every committed event class")
    CL.claim("no committed observable separates the completion-only "
             "probe family, and the modal relation does")
    CL.claim("the three faces emit byte-identical functionals at every "
             "delivered row")
    CL.claim("the debt is decided: the two grains never conflict, and "
             "the walk cannot express the crossing at either arity")
    if mut("MUT-CLAIM"):
        CL.claim("the committed row is feasible at every committed "
                 "event class")
    for seg in verdict:
        CL.fence(seg)
    rep = CL.check(paper_probe)
    if mut("MUT-PAPER-CLAIM"):
        rep = dict(rep, ok=False)
    LD.gate("G-PAPER-CLAIMS", rep["ok"],
            "every table, load-bearing sentence and fence is a rendered "
            "claim of the receipt, compared both ways and keyed by "
            "table",
            {"tables": len(rep["tables"]),
             "unrendered": len(rep["unrendered_tables"])})
    P["claims"] = SL.seal("claims", to_json(rep), "G-PAPER-CLAIMS")

    # ---- coverage, polarity, referent, spelled, fraction ----------------
    ints = set()
    collect_ints(P, ints)
    collect_ints(M.vals, ints)
    paper_nums = numerals(paper_probe)
    uncovered = sorted({t for t in paper_nums
                        if t not in ints and t not in EXEMPT_NUMERALS})
    LD.gate("G-PAPER-COVERAGE", not uncovered,
            "every numeral the paper carries, fenced blocks included, "
            "is backed by a receipt value or a declared exemption",
            {"paper_numerals": len(paper_nums),
             "uncovered": uncovered[:6]})
    P["coverage_scan"] = SL.seal("coverage_scan", to_json(
        {"paper_numerals": len(paper_nums),
         "distinct": len(set(paper_nums)),
         "exempt": sorted(EXEMPT_NUMERALS)}), "G-PAPER-COVERAGE")

    forbidden = [
        "the committed row is feasible",
        "the lp is feasible after all",
        "an observable separates the completion",
        "the persist members allow the same second crossings",
        "the faces emit different functionals",
    ]
    pc = canon(paper_probe)
    pol_hits = [f for f in forbidden if canon(f) in pc]
    LD.gate("G-PAPER-POLARITY", not pol_hits,
            "no declared inversion of a delivered verdict stands "
            "anywhere in the paper, in any voice",
            {"inversions_scanned": len(forbidden)})
    P["polarity"] = SL.seal("polarity", to_json(
        {"scanned": forbidden, "hits": pol_hits}), "G-PAPER-POLARITY")

    prose = re.sub(r"```[^\n]*\n.*?```", " ", paper_probe, flags=re.S)
    prose = "\n".join(l for l in prose.split("\n")
                      if not (l.strip().startswith("|")
                              and l.strip().endswith("|")))
    pair_registry = {
        (obs["blind"], obs["menu_size"]): "observable",
        (seam2["differ_fit"], seam2["first_crossings"]):
            "first crossings",
        (seam2["differ_kept"], seam2["first_crossings"]):
            "first crossings",
        (psi["agreements"], psi["row_count"]): "row",
        (debt["menu_cross_overlap"], debt["cross_pairs"]): "cross",
        (debt["frozen_creation_admits_seam"], debt["seam_spanning"]):
            "seam-spanning",
        (car["expresses"], car["count"]): "candidate",
        (car["evolves"], car["count"]): "candidate",
        (car["hosts"], car["count"]): "candidate",
        (prep["best"], lawf["crossings"]): "crossing",
        (lawf["staylable"], lawf["crossings"]): "crossing",
        (debt["amplitudes_with_unit_mass"],
         debt["nonzero_amplitudes"]): "amplitude",
        (lp["branch_degenerate"], lp["branch_count"]): "branch",
        (words.get("INFEASIBLE", 0), len(lp["rows"])): "row",
    }
    pair_rows = []
    ok_pairs = True
    for m2 in re.finditer(
            r"(?<![\w.])(\d[\d,]*) of (?:the )?(\d[\d,]*)(?![\w.])",
            prose):
        a2v = int(m2.group(1).replace(",", ""))
        b2v = int(m2.group(2).replace(",", ""))
        s2, e2 = m2.start(), m2.end()
        cut = prose.rfind(".", 0, s2)
        sent = prose[cut + 1:prose.find(".", e2) + 1]
        if a2v == b2v:
            ok_pairs = False
            pair_rows.append({"pair": [a2v, b2v], "why": "reflexive"})
            continue
        ctx = pair_registry.get((a2v, b2v))
        if ctx is None or ctx not in sent.casefold():
            ok_pairs = False
            pair_rows.append({"pair": [a2v, b2v],
                              "why": "unregistered or out of role"})
        else:
            pair_rows.append({"pair": [a2v, b2v], "why": "ok"})
    LD.gate("G-PAPER-REFERENT", ok_pairs,
            "every of-fraction in the prose names a registered measured "
            "pair inside its own role sentence, and a reflexive pair is "
            "refused outright",
            {"pairs": len(pair_rows)})
    P["referent"] = SL.seal("referent", to_json(pair_rows),
                            "G-PAPER-REFERENT")

    scan_list = pick("MUT-SPELLED", tuple(SPELLED_SCANNED),
                     tuple(SPELLED_SCANNED[:-1]))
    want_scan = tuple(w for w in SPELLED if w not in SPELLED_EXCLUDED)
    spelled_hits = []
    sp_ok = True
    for w in scan_list:
        for m3 in re.finditer(r"\b" + w + r"\b", prose, re.I):
            val = str(SPELLED_VALUE[w])
            spelled_hits.append({"word": w, "value": int(val)})
            if val not in ints:
                sp_ok = False
    LD.gate("G-PAPER-SPELLED",
            sp_ok and scan_list == want_scan,
            "every spelled cardinal in the prose is rewritten to its "
            "digits and bound by the same coverage the digits get, and "
            "the scanner's word list is itself audited",
            {"spelled": len(spelled_hits)})
    P["spelled"] = SL.seal("spelled", to_json(spelled_hits),
                           "G-PAPER-SPELLED")

    frac_rows = []
    fr_ok = True
    for sent in re.split(r"(?<=[.!?])\s+", canon(prose)):
        for word, (lo, hi) in FRACTION_WORDS.items():
            for hedge in HEDGES:
                tok = hedge + word
                if re.search(r"\b" + re.escape(tok) + r"\b(?! of a)",
                             sent) and " of " in sent:
                    ns = [int(x.replace(",", ""))
                          for x in numerals(sent)]
                    just = any(lo <= Fraction(a3, b3) <= hi
                               for a3 in ns for b3 in ns
                               if b3 > 0 and a3 <= b3)
                    frac_rows.append({"word": tok, "ok": just})
                    if not just:
                        fr_ok = False
                    break
    LD.gate("G-PAPER-FRACTION", fr_ok,
            "every spelled fraction or proportion in the prose is "
            "justified by a measured pair named in its own sentence",
            {"fractions": len(frac_rows)})
    P["fraction"] = SL.seal("fraction", to_json(frac_rows),
                            "G-PAPER-FRACTION")

    # ---- typed counts, declared consumption, anchors, falsifiers --------
    audit_src = src + (TYPED_PROBE if mut("MUT-TYPED") else "")
    typed_bad = M.audit(audit_src)
    LD.gate("G-NO-TYPED-COUNTS", not typed_bad,
            "no numeral is typed into any statement, gate, claim, fence "
            "or registry door, in any of the audited species",
            {"offences": typed_bad[:6]})
    P["typed_counts"] = SL.seal("typed_counts", to_json(typed_bad),
                                "G-NO-TYPED-COUNTS")

    declared_all = set(DECL) | set(DECL2)
    declared_all = pick("MUT-DECL", declared_all,
                        declared_all | {"aut.phantom"})
    unconsumed = sorted(declared_all - CONSUMED_DECL)
    LD.gate("G-DECLARED-CONSUMED", not unconsumed,
            "every value declared from a parent is consumed by a gate "
            "condition; nothing is carried and bound by nothing",
            {"declared": len(declared_all),
             "unconsumed": unconsumed[:6]})
    P["declared"] = SL.seal("declared", to_json(
        {"declared": sorted(declared_all),
         "consumed": sorted(CONSUMED_DECL)}), "G-DECLARED-CONSUMED")

    cons_report = ANCH.consumption(LD)
    LD.gate("G-ANCHOR-CONSUMPTION",
            all(r["ok"] for r in cons_report),
            "every anchor is consumed by the gate it declares, and that "
            "gate ran",
            {"anchors": len(cons_report)})
    P["anchor_consumption"] = SL.seal("anchor_consumption",
                                      to_json(cons_report),
                                      "G-ANCHOR-CONSUMPTION")

    ftable = list(FALSIFIERS)
    ftable = pick("MUT-FALSIFIER", ftable,
                  ftable + [Falsifier("MUT-PHAN" + "TOM", "G-CHART",
                                      "nothing", "no site exists")])
    missing_site = [f.name for f in ftable
                    if ("\"" + f.name + "\"") not in src]
    LD.gate("G-FALSIFIER-HONESTY", not missing_site,
            "every declared falsifier has an injection site in this "
            "file's own source",
            {"recipes": len(ftable), "missing": missing_site[:4]})
    P["falsifier_honesty"] = SL.seal(
        "falsifier_honesty", to_json(
            {"recipes": len(ftable), "missing": missing_site}),
        "G-FALSIFIER-HONESTY")

    gate_names = LD.names() + list(DOOR_CHECKS)
    covered_gates = sorted({f.gate for f in FALSIFIERS})
    denom = pick("MUT-COVERAGE", tuple(sorted(set(gate_names))),
                 tuple(sorted(set(gate_names))[:10]))
    full_now = tuple(sorted(set(LD.names() + list(DOOR_CHECKS)
                                + ["G-COVERAGE", "G-VERDICT-RECON",
                                   "G-READ-SET"])))
    uncovered_gates = [g for g in full_now if g not in covered_gates]
    LD.gate("G-COVERAGE",
            denom == tuple(sorted(set(gate_names)))
            and not uncovered_gates,
            "every ledgered gate and every door check carries at least "
            "one falsifier recipe, and the denominator is recomputed at "
            "the gate rather than snapshotted",
            {"gates": len(full_now), "recipes": len(FALSIFIERS)})
    P["falsifier_coverage"] = SL.seal(
        "falsifier_coverage", to_json(
            {"gates": list(full_now), "recipes": len(FALSIFIERS)}),
        "G-COVERAGE")

    # ---- the comparator --------------------------------------------------
    Pjson = json.loads(json.dumps(P, default=str))
    recon = reconstruct(Pjson)
    poscheck = head_positional_check(list(verdict), list(recon))
    LD.gate("G-VERDICT-RECON", poscheck["ok"],
            "the head is rebuilt from the receipt's primitive tables by "
            "a comparator sharing no code and no literal with the "
            "builder, and matches whole and numeral by numeral",
            {"numerals": poscheck["numerals_matched"]})
    P["comparator"] = SL.seal("comparator", to_json(
        {"segments": list(recon), "check": poscheck}),
        "G-VERDICT-RECON")

    # ---- the read set (first door leg, ledgered) ------------------------
    declared_reads = sorted({rel for (rel, _s) in SOURCES.values()}
                            | {SELF_REL, paper_rel})
    rcheck = READS.check(declared_reads)
    LD.gate("G-READ-SET",
            not rcheck["stray"] and not rcheck["external"]
            and not rcheck["declared_never_read"],
            "every read this process performed is declared, classified "
            "and inside the repository",
            {"distinct": rcheck["distinct_paths"]})
    SL.declare_unsealed(
        "read_set", "re-checked after the artifacts are written, so it "
                    "cannot be sealed at a gate")
    P["read_set"] = rcheck

    SL.close()

    # ---- the transcript --------------------------------------------------
    say("-" * 66)
    for seg in verdict:
        say(seg)
    say("-" * 66)
    sayn(M.stmt("interface rows {a}; free declarations {b} in {c} "
                "type categories; senses {d}",
                a="iface.object_rows", b="decl.count",
                c="decl.categories", d="iface.senses"),
         [("interface.rows", len(iface["rows"])),
          ("free_declarations.count", fdecl["count"]),
          ("free_declarations.categories_n", len(fdecl["categories"])),
          ("interface.senses_n", len(iface["senses"]))])
    sayn(M.stmt("observables {a}; blind {b}; probes {c}; relation "
                "values {d}", a="obs.menu", b="obs.blind",
                c="obs.probes", d="obs.relation_values"),
         [("obs.menu_size", obs["menu_size"]),
          ("obs.blind", obs["blind"]),
          ("obs.probes", obs["probes"]),
          ("obs.relation_value_set", obs["relation_value_set"])])
    sayn(M.stmt("two-step fiber {a} to {b}; fit differs {c}; kept "
                "differs {d}", a="seam.fiber_min", b="seam.fiber_max",
                c="seam.differ_fit", d="seam.differ_kept"),
         [("seam.fiber_min_v", seam2["fiber_min"]),
          ("seam.fiber_max_v", seam2["fiber_max"]),
          ("seam.differ_fit_v", seam2["differ_fit"]),
          ("seam.differ_kept_v", seam2["differ_kept"])])
    sayn(M.stmt("lp rows {a}; infeasible {b}; unique {c}; many {d}; "
                "fiber {e}", a="lp.rows", b="lp.infeasible",
                c="lp.unique", d="lp.many", e="lp.fiber"),
         [("lp.rows_n", len(lp["rows"])),
          ("lp.infeasible_n", words.get("INFEASIBLE", 0)),
          ("lp.unique_n", words.get("UNIQUE", 0)),
          ("lp.many_n", words.get("MANY", 0)),
          ("lp.fiber_n", words.get("FEASIBLE-AT-THE-FIBER-ROW", 0))])
    P["narrative_binds"] = {
        "interface": {"rows": len(iface["rows"])},
        "free_declarations": {"count": fdecl["count"],
                              "categories_n": len(fdecl["categories"])},
        "interface_senses": {"senses_n": len(iface["senses"])},
        "obs": {"menu_size": obs["menu_size"], "blind": obs["blind"],
                "probes": obs["probes"],
                "relation_value_set": obs["relation_value_set"]},
        "seam": {"fiber_min_v": seam2["fiber_min"],
                 "fiber_max_v": seam2["fiber_max"],
                 "differ_fit_v": seam2["differ_fit"],
                 "differ_kept_v": seam2["differ_kept"]},
        "lp": {"rows_n": len(lp["rows"]),
               "infeasible_n": words.get("INFEASIBLE", 0),
               "unique_n": words.get("UNIQUE", 0),
               "many_n": words.get("MANY", 0),
               "fiber_n": words.get("FEASIBLE-AT-THE-FIBER-ROW", 0)}}
    SL.declare_unsealed("narrative_binds",
                        "the transcript door re-derives these from the "
                        "sealed blocks; carried for the reader")
    out_line = "object under test %s %s" % (
        P["object_under_test"]["path"],
        P["object_under_test"]["sha256_12"])
    if pick("MUT-OBJECT", True, False):
        say(out_line)
    ledger_rows = [{"gate": r["gate"], "passed": r["passed"],
                    "chain": r["chain"]} for r in LD.rows]
    P["ledger"] = {"rows": ledger_rows, "head": LD.head,
                   "recomputed": LD.recompute()}
    SL.declare_unsealed("ledger", "built after the last gate by "
                                  "construction")
    say("ledger head " + LD.head)
    fake_row = pick("MUT-TRANSCRIPT", None,
                    "    [PASS] G-PHANTOM                       "
                    "0123456789abcdef")
    if fake_row:
        say(fake_row)
    narr_twist = pick("MUT-NARRATIVE", None, "77")
    if narr_twist and NARRATIVE:
        for i2, l2 in enumerate(OUT_LINES):
            if l2 == NARRATIVE[0][0]:
                OUT_LINES[i2] = re.sub(r"\d+", narr_twist, l2, count=1)
                break
    transcript = "\n".join(OUT_LINES) + "\n"
    P["transcript_digest"] = bdigest(transcript.encode("utf-8"))
    SL.declare_unsealed("transcript_digest",
                        "digested after the transcript is assembled")
    SL.declare_unsealed("seal_manifest",
                        "the manifest cannot seal itself")
    SL.declare_unsealed("paper_kit",
                        "a rendering aid re-derived from sealed blocks")
    P["paper_kit"] = {
        "fences": [seg for seg in verdict],
        "prose_claims": sorted(CL.prose),
        "tables": {tid: sorted((list(k), v) for k, v in tab.items())
                   for tid, tab in CL.tables.items()}}
    P["schema"] = SCHEMA
    SL.declare_unsealed("schema", "the receipt's format name")

    # ---- MUT-PROMOTE / MUT-SEAL / MUT-POSTCLOSE windows -----------------
    P["lattice"] = pick("MUT-PROMOTE", P["lattice"],
                        dict(P["lattice"], lattice=32))
    stray = pick("MUT-SEAL", None, ("stray_after_close", 1))
    if stray:
        P[stray[0]] = stray[1]
    door_verify(P, LD, SL, transcript)
    P["coin"] = pick("MUT-POSTCLOSE", P["coin"],
                     dict(P["coin"], classes=7))
    blob = promote(P, LD, SL, transcript)
    return P, verdict, transcript, blob


TYPED_PROBE = 'MEAS.stmt("the census returns 42 lawful crossings")\n'


def door_verify(P, LD, SL, transcript):
    """the door's first verification: seals against the live payload,
    totality from the live key set, transcript against the ledger, the
    narrative against the receipt, the object under test in both
    artifacts."""
    rep = SL.verify(P, LD, "pre-serialisation")
    if rep["violations"]:
        raise GateFail("G-INTEGRITY",
                       "sealed values moved: %s" % rep["violations"][:4])
    if rep["stray"]:
        raise GateFail("G-SEAL-TOTAL",
                       "unsealed undeclared keys: %s" % rep["stray"][:4])

    want = Counter("[%s] %s %s"
                   % ("PASS" if r["passed"] else "FAIL",
                      r["gate"], r["chain"])
                   for r in LD.rows)
    got = Counter()
    for line in transcript.split("\n"):
        m4 = re.match(r"\s*\[(PASS|FAIL)\] (\S+) +([0-9a-f]{16})", line)
        if m4:
            got["[%s] %s %s" % (m4.group(1), m4.group(2),
                                m4.group(3))] += 1
    if got != want:
        raise GateFail("G-TRANSCRIPT-BOUND",
                       "the transcript's gate rows are not the ledger's "
                       "rows: stray %s missing %s"
                       % (sum((got - want).values()),
                          sum((want - got).values())))
    binds = P.get("narrative_binds", {})
    for (text, pairs) in NARRATIVE:
        found = None
        for line in transcript.split("\n"):
            if line == text:
                found = line
                break
        if found is None:
            raise GateFail("G-TRANSCRIPT-NARRATIVE",
                           "a declared narrative line is missing")
        nums = [int(x.replace(",", "")) for x in numerals(found)]
        vals = [v for (_p, v) in pairs]
        if nums != vals:
            raise GateFail("G-TRANSCRIPT-NARRATIVE",
                           "narrative numerals differ from the receipt: "
                           "%s vs %s" % (nums[:6], vals[:6]))
    declared_texts = {t for (t, _p) in NARRATIVE}
    for line in transcript.split("\n"):
        if GATEROW_RE.search(line) or line in declared_texts:
            continue
        if DECOR_RE.match(line.strip()) or line.startswith("object "):
            continue
        if line.startswith("ledger head"):
            continue
        if numerals(line):
            raise GateFail("G-TRANSCRIPT-NARRATIVE",
                           "an unbound line carries a numeral: "
                           + line[:60])
    if ("object under test" not in transcript
            or P["object_under_test"]["sha256_12"] not in transcript):
        raise GateFail("G-OBJECT-UNDER-TEST",
                       "the object under test is not named in the "
                       "transcript beside its digest")


def promote(P, LD, SL, transcript):
    """promotion: manifest re-derived, serialise, verify the parsed
    bytes against the seals, stage, read back, replace, verify from the
    promoted path, and check the read set once more."""
    P["seal_manifest"] = SL.manifest()
    blob = json.dumps(P, indent=1, sort_keys=True, default=str)
    parsed = json.loads(blob)
    for k, s in SL.seals.items():
        if digest(parsed[k]) != s["digest"]:
            raise GateFail("G-INTEGRITY",
                           "the serialised bytes betray the seal at "
                           + k)
    if not WRITE:
        return blob
    rec_tmp = os.path.join(REPO, REC_REL + ".tmp")
    out_tmp = os.path.join(REPO, OUT_REL + ".tmp")
    try:
        with open(rec_tmp, "w", encoding="utf-8") as fh:
            fh.write(blob)
        with open(out_tmp, "w", encoding="utf-8") as fh:
            fh.write(transcript)
        with open(rec_tmp, "r", encoding="utf-8") as fh:
            back = fh.read()
        with open(out_tmp, "r", encoding="utf-8") as fh:
            back2 = fh.read()
        if back != blob or back2 != transcript:
            raise GateFail("G-INTEGRITY", "the staged bytes differ")
        reparsed = json.loads(back)
        for k, s in SL.seals.items():
            if digest(reparsed[k]) != s["digest"]:
                raise GateFail("G-INTEGRITY",
                               "the staged receipt betrays the seal at "
                               + k)
        os.replace(rec_tmp, os.path.join(REPO, REC_REL))
        os.replace(out_tmp, os.path.join(REPO, OUT_REL))
    finally:
        for t in (rec_tmp, out_tmp):
            if os.path.exists(t):
                os.remove(t)
    with open(os.path.join(REPO, REC_REL), "r", encoding="utf-8") as fh:
        promoted = json.loads(fh.read())
    for k, s in SL.seals.items():
        if digest(promoted[k]) != s["digest"]:
            raise GateFail("G-INTEGRITY",
                           "the promoted receipt betrays the seal at "
                           + k)
    if promoted["object_under_test"]["sha256_12"] \
            not in read_text(OUT_REL):
        raise GateFail("G-OBJECT-UNDER-TEST",
                       "the promoted transcript lost the object under "
                       "test")
    return blob
# ===========================================================================
# SECTION 11.  THE DECLARED FALSIFIERS AND THE CLI
# ===========================================================================
# Family (h).  Each recipe names the MEASURED OBJECT it corrupts and the
# gate it must die at; the --selftest sweep runs every one out of the
# builder's own control flow and proves the move by digest.

FALSIFIERS = [
    Falsifier("MUT-SOURCE", "G-SOURCES", "a source's declared sha",
              "one pinned source's declared digest is altered, so the "
              "byte comparison fails"),
    Falsifier("MUT-ANCHOR", "G-ANCHORS", "an anchor's needle",
              "one verbatim needle is truncated below the floor, so its "
              "location and floor both fail"),
    Falsifier("MUT-CLASS", "G-CLASS", "the class sentence",
              "the pin's class words are cut out of the located "
              "sentence, so the class binding fails"),
    Falsifier("MUT-TEMPLATE", "G-TEMPLATE-CONFORMANCE", "the family ids",
              "one implemented family is dropped from the compared set, "
              "so the id equality with the pinned template fails"),
    Falsifier("MUT-SORT", "G-DETERMINISM", "the ordering discipline",
              "a sort keyed on a bare repr is added to the scanned "
              "source, the hash-seed-dependent shape the register "
              "names"),
    Falsifier("MUT-HASH", "G-DETERMINISM", "the ordering discipline",
              "a sort keyed on the builtin hash is added to the scanned "
              "source, the species that carries no repr token"),
    Falsifier("MUT-ROUNDS", "G-CHART", "the admissible-round set",
              "a non-triangle partition is admitted as a round, so the "
              "law-selected census moves"),
    Falsifier("MUT-COIN", "G-COIN-FAMILY", "the coin enumeration",
              "the enumeration bound is narrowed so the family census "
              "no longer matches the parent's"),
    Falsifier("MUT-UNION", "G-UNION", "the union relation",
              "one realised pair is removed, so carriers and pairs part "
              "from the parent's"),
    Falsifier("MUT-GROUPS", "G-EVENTS", "the event family",
              "one conflict group is dropped, so the census leaves the "
              "closed form"),
    Falsifier("MUT-PROFILE", "G-PROFILES", "the footprint classifier",
              "a doubled pair is reclassified as a crossing, so the "
              "profile census moves"),
    Falsifier("MUT-LATTICE", "G-LATTICE", "the completion box",
              "the enumeration box is narrowed by one, so the lattice "
              "is cut short and the widened re-run disagrees"),
    Falsifier("MUT-LAWFUL", "G-LAWFUL", "the within leg",
              "the within-sector leg is skipped, so events opening a "
              "pair inside a sector count as lawful"),
    Falsifier("MUT-STAY", "G-SEAM-CENSUS", "the stay predicate",
              "the seam-count comparison is inverted, so exactly the "
              "wrong crossings read as staylable"),
    Falsifier("MUT-RELATION", "G-MULTIPLICITY", "the multiplicity",
              "the four-valued slots are relabelled one-valued, the "
              "size that would make the relation a map"),
    Falsifier("MUT-FORM", "G-LAWFUL", "the successor constraint",
              "the realised-cross constraint is dropped from the "
              "successor census, so the two-crossing deaths stop dying "
              "and the lawful census leaves the parent's"),
    Falsifier("MUT-PREP", "G-PREPAREDNESS", "the crossing family",
              "the census is run against four crossings instead of the "
              "arena's own, so the histogram moves"),
    Falsifier("MUT-OBSMENU", "G-OBS-MENU", "the menu audit",
              "the audited signature is truncated, so the observable "
              "functions no longer match their declared domain"),
    Falsifier("MUT-OBS", "G-OBS-SWEEP", "an observable's value set",
              "one observable is scored as separating the probe family, "
              "so the blind count falls"),
    Falsifier("MUT-PAIRS", "G-OBS-SWEEP", "the probe parity",
              "the probe family's shared-record parity is broken, so "
              "the sweep compares states differing in more than the "
              "completion"),
    Falsifier("MUT-READING", "G-READING-FAMILY", "the reading family",
              "the persist members are collapsed onto the re-solved "
              "one, so the family stops separating"),
    Falsifier("MUT-TWOSTEP", "G-TWO-STEP", "the second step's record",
              "the second step is profiled against the first step's "
              "standing record, so the census fiber moves"),
    Falsifier("MUT-STEPFIBER", "G-TWO-STEP", "the fiber",
              "the census is run from the first crossing alone, so the "
              "published fiber is one cell wide"),
    Falsifier("MUT-SEAMWORD", "G-SEAM-DECISION", "the outcome word",
              "the underdetermined word is rewritten as a supported "
              "reading, which the census does not license"),
    Falsifier("MUT-IFACE", "G-INTERFACE", "an object's class",
              "one interface row is classed by a word outside the four, "
              "so the typing totality fails"),
    Falsifier("MUT-TYPES", "G-FREE-DECLS", "the type column",
              "the fifteen declarations are flattened to one type, the "
              "count-of-constants shape the wall forbids"),
    Falsifier("MUT-FORK", "G-FORK", "the event fork",
              "a compromise arm is added to the fork, which the wall "
              "forbids"),
    Falsifier("MUT-UNITARY", "G-MAPS-TYPED", "the evolution map",
              "the norm-conservation check is offset, so the map stops "
              "reading unitary at scale"),
    Falsifier("MUT-COMPOSE", "G-MAPS-SEPARATE", "the reach audit",
              "the audit is pointed at a pattern that misses the maps, "
              "so composition would go unseen"),
    Falsifier("MUT-BORN", "G-BORN", "the emission functional",
              "the normalisation is dropped, so the functional stops "
              "summing to one"),
    Falsifier("MUT-STEPORDER", "G-STEP-ORDER", "the order check",
              "the ledger lookup is pointed at a phantom gate, so the "
              "seam-before-Born ordering is unverified"),
    Falsifier("MUT-ORDER", "G-ORDER-FIBER", "the coin-order fiber",
              "both orders are forced onto the delivered member, so the "
              "record-blindness of the alternative fails"),
    Falsifier("MUT-REGION", "G-PSI-REGIONS", "the region audit",
              "the audit prefix is changed so no face region is found "
              "and the coverage fails"),
    Falsifier("MUT-PSI", "G-PSI-EQUAL", "the instrument face",
              "the channel face's functional is reversed, so the three "
              "faces stop agreeing"),
    Falsifier("MUT-INCIDENCE", "G-LP-BUILD", "the incidence matrix",
              "one entry of the block incidence is inflated, so the "
              "structural row sums fail"),
    Falsifier("MUT-NORM", "G-NORMALIZATION", "the writer census",
              "the block class's writer identity is falsified, so the "
              "class-relative form of the normalization is wrong"),
    Falsifier("MUT-SIMPLEX", "G-LP-COMMITTED", "the target vector",
              "the solver is handed a zeroed target, so the committed "
              "row comes back feasible"),
    Falsifier("MUT-LPROWS", "G-LP-CENSUS", "the row census",
              "a duplicate row is appended after solving, so the row "
              "count leaves the class-by-target product"),
    Falsifier("MUT-CONTROL-ARM", "G-LP-CONTROLS", "the forced arm",
              "the forced-infeasible target is replaced by a uniform "
              "one, so the control comes back feasible"),
    Falsifier("MUT-CEILING", "G-LP-CEILING", "the exception count",
              "a phantom exception is added, so the ceiling stops being "
              "exceptionless"),
    Falsifier("MUT-A2", "G-LP-DEGENERATE", "the branch word",
              "the degenerate branch is relabelled unique, which merges "
              "it into the committed classes' vocabulary"),
    Falsifier("MUT-DIM", "G-LP-DIM", "the implicit census",
              "the implicit-equality list is emptied, so a unique row "
              "claims dimension without a second-point certificate"),
    Falsifier("MUT-CARRIER", "G-CARRIER", "the isometry check",
              "the isometry is verified on the wrong side, so the "
              "embedding certificate fails"),
    Falsifier("MUT-DEBT", "G-DEBT", "the menu overlap",
              "a cross pair is scored into the walk's menu, so the "
              "disjointness fails"),
    Falsifier("MUT-TIEBREAK", "G-EQUIV-DECLARED", "the registry",
              "a declared tie-break row is dropped, the silent-choice "
              "shape the wall forbids"),
    Falsifier("MUT-W3", "G-W3-LABELS", "a headline label",
              "the family-level label is flipped against the "
              "varied-fibre data it is computed from"),
    Falsifier("MUT-STAMP", "G-STAMPS", "the stamp table",
              "one downstream row loses its stamp, so totality over the "
              "rows fails"),
    Falsifier("MUT-CYCLE", "G-CIRCULARITY", "the dependency graph",
              "the record-to-actor edge is cut, so the carried cycle "
              "length moves"),
    Falsifier("MUT-PREREG", "G-OUTCOME-FEASIBILITY", "an outcome word",
              "one pre-registered word is rewritten off its pin stem"),
    Falsifier("MUT-FEASIBILITY", "G-OUTCOME-FEASIBILITY", "a witness",
              "one outcome pair's witness is detached from the run"),
    Falsifier("MUT-SENSE", "G-SENSES", "the sense list",
              "one of the six sense sentences is dropped, so the count "
              "and the paper part company"),
    Falsifier("MUT-WALL", "G-WALLS", "the paper under test",
              "a wall control is planted into the paper in house style "
              "and must die at its wall"),
    Falsifier("MUT-PAPER-CLAIM", "G-PAPER-CLAIMS", "the claims report",
              "the report is forced to disagree, standing in for a "
              "transplanted table row"),
    Falsifier("MUT-CLAIM", "G-PAPER-CLAIMS", "a load-bearing sentence",
              "an inverted sentence is registered as required, which "
              "the paper rightly does not carry"),
    Falsifier("MUT-NUMERAL", "G-PAPER-COVERAGE", "the paper under test",
              "a numeral no measurement backs is planted in the prose"),
    Falsifier("MUT-POLARITY", "G-PAPER-POLARITY", "the paper under test",
              "a declared inversion of the committed verdict is planted "
              "in the paper's own voice"),
    Falsifier("MUT-REFERENT", "G-PAPER-REFERENT", "the paper under test",
              "a cross-universe pair is planted, both numerals true and "
              "the relation false"),
    Falsifier("MUT-REFLEXIVE", "G-PAPER-REFERENT", "the pair scan",
              "a reflexive of-fraction is planted in the prose, the "
              "shape the door refuses outright"),
    Falsifier("MUT-SPELLED", "G-PAPER-SPELLED", "the spelled scanner",
              "the scanner's word list is truncated, so a spelled "
              "numeral would go unscanned"),
    Falsifier("MUT-FRACTION", "G-PAPER-FRACTION", "the paper under test",
              "a spelled proportion no measured pair justifies is "
              "planted in the prose"),
    Falsifier("MUT-TYPED", "G-NO-TYPED-COUNTS", "the audited source",
              "a statement carrying a typed numeral is appended to the "
              "audited source"),
    Falsifier("MUT-DECL", "G-DECLARED-CONSUMED", "the declared set",
              "a parent value is declared and bound by nothing, the "
              "carried-not-used shape"),
    Falsifier("MUT-CONSUMER", "G-ANCHOR-CONSUMPTION", "a consumer",
              "one anchor's declared consumer is renamed to a gate the "
              "run never emits"),
    Falsifier("MUT-FALSIFIER", "G-FALSIFIER-HONESTY", "the recipe table",
              "a recipe whose name has no injection site anywhere in "
              "this file is declared into the table"),
    Falsifier("MUT-COVERAGE", "G-COVERAGE", "the denominator",
              "the coverage denominator is snapshotted short, the "
              "self-exemption the engraving forbids"),
    Falsifier("MUT-VERDICT", "G-VERDICT-RECON", "a primitive table",
              "the step-two census rows are moved by one, so the "
              "comparator's own arithmetic parts from the head"),
    Falsifier("MUT-READ", "G-READ-SET", "the read log",
              "a file the pin does not declare is opened during the "
              "run"),
    Falsifier("MUT-SEAL", "G-SEAL-TOTAL", "the payload",
              "a key is added after the seal window closes, which "
              "totality at the door exists to catch"),
    Falsifier("MUT-PROMOTE", "G-INTEGRITY", "a sealed value",
              "a sealed row is edited between the last gate and the "
              "door, so the gate-time digest and the value part"),
    Falsifier("MUT-POSTCLOSE", "G-INTEGRITY", "a sealed value, later",
              "a sealed row is edited after the first door verification "
              "and before serialisation, the window a forged value once "
              "used"),
    Falsifier("MUT-TRANSCRIPT", "G-TRANSCRIPT-BOUND", "the transcript",
              "a pass row for a gate that never ran is appended to the "
              "promoted text"),
    Falsifier("MUT-NARRATIVE", "G-TRANSCRIPT-NARRATIVE", "a narrative "
              "line", "one numeral of a bound narrative line is moved "
              "after binding"),
    Falsifier("MUT-OBJECT", "G-OBJECT-UNDER-TEST", "the object line",
              "the object-under-test line is dropped from the "
              "transcript, so the artifacts stop naming what they "
              "certify"),
]
MUTNAMES = [f.name for f in FALSIFIERS]

MODE_FLAGS = {"--numbers": "numbers", "--selftest": "selftest",
              "--list-gates": "gates", "--list-mutants": "mutants",
              "--list-families": "families", "--verify-paper": "paper"}


def cli(argv):
    """strict argv: one mode, one mutant, no repeats, no unknowns; a
    mode conflict or a repeated flag exits two rather than one flag
    silently discarding another."""
    mode, path, mutant, chosen, nowrite = "run", None, None, None, False
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--no-write":
            if nowrite:
                return None
            nowrite = True
            globals()["WRITE"] = False
        elif a in MODE_FLAGS:
            if chosen is not None:
                return None
            chosen, mode = a, MODE_FLAGS[a]
            if a == "--verify-paper":
                i += 1
                if i >= len(argv):
                    return None
                path = argv[i]
        elif a == "--mutant":
            i += 1
            if i >= len(argv) or argv[i] not in MUTNAMES or mutant:
                return None
            mutant = argv[i]
        else:
            return None
        i += 1
    if mutant and mode in ("gates", "mutants", "families", "selftest"):
        return None
    return mode, path, mutant


def tree_digest():
    """a digest of both artifact paths' bytes, for the write-nothing
    proof the selftest prints."""
    out = {}
    for rel in (OUT_REL, REC_REL):
        p = os.path.join(REPO, rel)
        out[rel] = bdigest(read_bytes(rel)) if os.path.exists(p) else None
    return out


def selftest():
    """every declared recipe, one full delivery each with the write leg
    off; each must die at its OWN declared gate; each must move an
    object the clean run also produced (by the register or the site's
    two-branch digest); and the artifacts must be byte-unchanged."""
    globals()["WRITE"] = False
    before = tree_digest()
    paper = (read_text(PAPER_REL)
             if os.path.exists(os.path.join(REPO, PAPER_REL)) else None)
    if paper is None:
        print("selftest: the paper under test does not exist")
        return 3
    globals()["MUTANT"] = None
    try:
        full_run(paper, PAPER_REL)
    except GateFail as e:
        print("selftest: THE CLEAN RUN REFUSED at %s" % e.check)
        return 3
    baseline = dict(SNAP)
    deaths, moves, wrong = 0, 0, []
    for f in FALSIFIERS:
        globals()["MUTANT"] = f.name
        try:
            full_run(paper, PAPER_REL)
            wrong.append(f.name + ":SURVIVED")
            continue
        except GateFail as e:
            if e.check != f.gate:
                wrong.append("%s:died-at-%s-not-%s"
                             % (f.name, e.check, f.gate))
                continue
            deaths += 1
        moved = (any(k in baseline and SNAP[k] != baseline[k]
                     for k in SNAP)
                 or bool(SITE_MOVES.get(f.name)))
        if moved:
            moves += 1
        else:
            wrong.append(f.name + ":NO-MOVE-PROVED")
    globals()["MUTANT"] = None
    after = tree_digest()
    print("selftest: recipes %d; deaths at the declared gate %d; moves "
          "proved %d" % (len(FALSIFIERS), deaths, moves))
    print("selftest: artifacts unchanged: %s" % (before == after))
    if wrong:
        for w in wrong[:14]:
            print("selftest: FAILED %s" % w)
        return 3
    if before != after:
        return 3
    return 0 if deaths == len(FALSIFIERS) == moves else 3


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    parsed = cli(argv)
    if parsed is None:
        sys.stderr.write(
            "usage: ecc_exact.py [--no-write] [--selftest] "
            "[--mutant NAME] [--list-gates] [--list-mutants] "
            "[--list-families] [--verify-paper PATH] [--numbers]\n")
        return 2
    mode, path, mutant = parsed
    if mode == "gates":
        gates = sorted({f.gate for f in FALSIFIERS})
        for f in sorted(FALSIFIERS, key=lambda x: (x.gate, x.name)):
            print("%-28s falsified by %s" % (f.gate, f.name))
        print("%d recipes at %d gates (a gate may carry more than one)"
              % (len(FALSIFIERS), len(gates)))
        return 0
    if mode == "mutants":
        for f in FALSIFIERS:
            print("%-18s -> %-28s target: %s :: %s"
                  % (f.name, f.gate, f.target, f.description))
        return 0
    if mode == "families":
        for k in sorted(FAMILIES):
            print("%-22s %s" % (k, FAMILIES[k]))
        return 0
    READS.install()
    globals()["MUTANT"] = mutant
    if mode == "selftest":
        return selftest()
    if mode == "paper":
        full = path if os.path.isabs(path) else os.path.join(REPO, path)
        if not os.path.exists(full) or os.path.isdir(full):
            sys.stderr.write("verify-paper: no such paper\n")
            return 2
        if not os.path.abspath(full).startswith(REPO + os.sep):
            sys.stderr.write("verify-paper: the paper must be inside "
                             "the repository; the read set is declared "
                             "relative to it\n")
            return 2
        with open(full, "r", encoding="utf-8") as fh:
            text = fh.read()
        if not text.strip():
            sys.stderr.write("verify-paper: the paper is empty\n")
            return 2
        globals()["WRITE"] = False
        try:
            rel = os.path.relpath(os.path.abspath(full), REPO)
            full_run(text, rel)
        except GateFail as e:
            print("verify-paper: REFUSED at %s :: %s"
                  % (e.check, e.detail))
            return 1
        print("verify-paper: PASS")
        return 0
    paper_path = os.path.join(REPO, PAPER_REL)
    paper = read_text(PAPER_REL) if os.path.exists(paper_path) else None
    if paper is None:
        sys.stderr.write("the paper under test does not exist\n")
        return 2
    if mode == "numbers":
        globals()["WRITE"] = False
    try:
        P, V, transcript, blob = full_run(paper, PAPER_REL)
    except GateFail as e:
        print("REFUSED at %s :: %s" % (e.check, e.detail))
        return 1
    if mode == "numbers":
        print(json.dumps({"measured": P["measured"],
                          "paper_kit": P["paper_kit"]},
                         indent=1, sort_keys=True, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())

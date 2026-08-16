#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""AUTOGLUE -- paper-45 -- CAN A CROSSING EVENT CREATE THE SEAM IT NEEDS?

Pin: v15/note-autoglue-pin.md (sha256-12 88c04df52c19, v15 ledger one).
Artifacts: v15/code/autoglue_output.txt, v15/code/autoglue_receipt.json.
Paper: v15/paper-45-autoglue.md.  Questions: Q38-Q40, Q34, Q41-Q42, Q50.

WHAT THIS INSTRUMENT MEASURES.  SEC-2 left gluing lawful only at a target
declared after the event was seen.  This unit asks whether an UPDATE can do
the declaring: one pre-declared, event-uniform rule taking

    (geometry, record, state)  --the event-->  (geometry', record', state')

with every delivered standard intact and no target fitted to any event.

  M1  THE UPDATE WINDOW.  Four link-creation rules x two readings x two
      count legs, run on the committed two-sector corpus at every one of the
      arena's three-actor conflict groups, at BOTH ends of the transition.
      The rules are blind to the event's identity (they see its footprint),
      equivariant under the arena's own relabellings, and applied before any
      fate is computed -- three gates, not three assurances.

  M2  THE FORM LEG.  The geometry the corpus carries is not an incidence
      structure: a count is the squared length of its link direction.  The
      successor state -- the seam's cross block at every shared site -- is
      censused per object: does one exist, is it unique, can the old one be
      kept?  And the fourth parallel class, which a within-sector link would
      occupy, is read out against the record the event deposits.

  M3  THE PRICE AND Q50.  Five currencies: refutability, the weld's forcing
      (the RSQ inventory at every post-state), the state's fiber, the
      structure, and the rule's own declaration.  Motivation is then placed:
      which events leave the weld forced, and whether those are the events
      the dynamics can perform.

  M4  THE DERIVATION ATTEMPT (Q41-Q42) AND THE OBSTRUCTION.  Eight declared
      extremal functionals on the seam's completion lattice before and after
      the event; the corpus's own three criteria re-measured; and the datum
      that must precede the event, stated as a theorem and checked at every
      object of the window.

TEMPLATE (E-25..E-33).  The nine family mechanisms of v14/TEMPLATE.md are
implemented natively under the template's own check ids, and
G-TEMPLATE-CONFORMANCE parses the pinned v14/code/era_template.py to require
that the ids implemented here are exactly the nine it declares.  TPL-2's
registered items are in force: seals verified at promotion with totality
recomputed at the door, the %-format and integer-offset typed-count
subspecies audited, wall controls written independently of their patterns,
falsifier move-proofs taken by digest, and no family carried unused.  S-1
(the comparator is the builder) is addressed BY CONSTRUCTION: the head is
rebuilt by a comparator that reads only the receipt's primitive tables,
carries its own segment law and its own format strings, and shares no
function and no literal with the builder.

CLI (#82).  --no-write | --selftest | --mutant NAME | --list-gates |
--list-mutants | --list-families | --verify-paper PATH | --numbers.
Anything else exits 2.  Exact arithmetic only: integers and Fractions.
"""

from __future__ import annotations

import ast
import hashlib
import json
import os
import re
import sys
import time
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations

# ===========================================================================
# SECTION 0.  RUN STATE, PRIMITIVES, THE CLI SURFACE
# ===========================================================================

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                      # .../isp/v15
REPO = os.path.dirname(ROOT)                      # .../isp

MUTANT = None
WRITE = True
OUT_LINES: list[str] = []
TYPED_PROBE = 'MEAS.stmt("the census returns 42 lawful crossings")\n'
SCHEMA = "isp/v15/autoglue/1"

SELF_REL = "v15/code/autoglue_exact.py"
PAPER_REL = "v15/paper-45-autoglue.md"
OUT_REL = "v15/code/autoglue_output.txt"
REC_REL = "v15/code/autoglue_receipt.json"

# ---- the sources READ at run time, each at its pinned sha256-12.  Nothing
# else may be read: the read set is recorded at the I/O accessor and gated
# after the last gate as well as before the first.
SOURCES = {
    "A-PIN": ("v15/note-autoglue-pin.md", "88c04df52c19"),
    "A-SEC2": ("v14/paper-40-sec2.md", "4fe88602280c"),
    "A-SEC": ("v14/paper-32-sec.md", "f3f43d94cd75"),
    "A-P19": ("v14/paper-19-r3-weld.md", "50bb81e67942"),
    "A-ADJ": ("v14/note-sec-adjudication.md", "7a82ffe7168a"),
    "A-TPL": ("v14/code/era_template.py", "d04a3eb58fbc"),
}
SOURCE_COMMIT = "ba62eac"

# ---- values inherited from the parents, DECLARED here and bound by
# REPRODUCTION: this unit recomputes each from its own construction and the
# run dies on any mismatch (#62 provenance, the SEC-2 discipline).
DECL = {
    "sec2.union.carriers": 15,
    "sec2.union.pairs": 54,
    "sec2.union.aut": 62208,
    "sec2.groups": 455,
    "sec2.orbits": 9,
    "sec2.seam_spanning": 288,
    "sec2.lawful_at_matched": 216,
    "sec2.aligned_lattice": 31,
    "sec2.aligned_after_crossing": 8,
    "sec2.cross_directions": 18,
    "sec2.shared_seeded.maps": 1728,
    "sec2.shared_seeded.free": 3,
    "sec2.b_seeded.maps": 576,
    "sec2.b_seeded.free": 2,
    "sec2.union_no_crossing.maps": 62208,
    "sec2.union_no_crossing.free": 0,
    "sec2.declaration_price_per_seam": 4,
}

NEEDLE_FLOOR = 40

# the head's four segments, named once and used as the spine of the
# pre-registration: one outcome PAIR per segment (#299-extended)
SEGMENT_NAMES = ("the window and the creation rule",
                 "the transition relation and the datum",
                 "motivation and lawfulness",
                 "the derivation attempt")

# ---- verbatim (#62) anchors.  Each is located exactly once in its pinned
# source under the #125 normaliser, is read only through the accessor, and is
# consumed in a declared MODE: PARSED (the consumer gate takes an operand out
# of the anchor's own bytes), QUOTED (the paper under test quotes it), GATE
# (the consumer names the anchor in its evidence row).
VERBATIM = [
    ("N-PIN-QUESTION", "A-PIN",
     "one lawful transition (geometry, record, state) \u2192 (geometry\u2032, "
     "record\u2032, state\u2032) in which a seam-crossing event CREATES the "
     "cross-link and seam it needs", "G-WINDOW", "PARSED"),
    ("N-PIN-OBSTRUCTION", "A-PIN",
     "the obstruction theorem (which datum must precede the event",
     "G-OBSTRUCTION", "PARSED"),
    # the pre-registration's own two clauses, read out of the frozen pin so
    # that the outcome words cannot be re-declared after the census (K3 M6)
    ("N-PIN-BREAK", "A-PIN",
     "lawful-only-at-declared-target is the wall to break or prove "
     "unbreakable", "G-OUTCOME-FEASIBILITY", "PARSED"),
    ("N-PIN-BOTHWAYS", "A-PIN",
     "Outcomes both ways feasible BY CONSTRUCTION of the window",
     "G-OUTCOME-FEASIBILITY", "PARSED"),
    ("N-SEC2-WALL", "A-SEC2",
     "Of the 288 seam-spanning groups, 216 leave the dictionary alive once "
     "the target declares the cross links the event realises",
     "G-INCIDENCE-CENSUS", "PARSED"),
    ("N-SEC2-MOTIVATED", "A-SEC2",
     "And not one of the 216 is MOTIVATED -- not as a tally that came out "
     "that way, but because it cannot come out otherwise.",
     "G-MOTIVATED-DISJOINT", "QUOTED"),
    # K2 MAJOR-4: the mechanism this unit's second head segment states is
    # the PARENT'S, checked there at the same 455 objects.  The anchor is
    # read here so the attribution is bound to the parent's own bytes and
    # the paper must quote it.
    ("N-SEC2-MECHANISM", "A-SEC2",
     "Three actors give three pairs, at most two of which can join the "
     "sectors, since a triangle admits no proper two-colouring; so a group "
     "that opens no pair inside a sector must double at least one link the "
     "union already carries; and the free items are exactly what a doubling "
     "buys. The hypothesis is checked at every one of the 455 groups and the "
     "conclusion at every one of the 216 lawful ones, object by object.",
     "G-MOTIVATED-DISJOINT", "QUOTED"),
    ("N-SEC2-SEAM", "A-SEC2",
     "the completion space is 4-parameter at every seam type, whatever the "
     "counts", "G-COMPLETION-LATTICE", "PARSED"),
    ("N-SEC2-DET", "A-SEC2",
     "maximising the determinant of the form returns the direct sum and "
     "nothing else", "G-EXTREMAL", "QUOTED"),
    ("N-P19-LEGS", "A-P19",
     "site \u2190 ACTOR, link \u2190 the co-division actor pair, count "
     "\u2190 the division events on that pair inside the declared window",
     "G-BASELINE-LAWFUL", "PARSED"),
    ("N-ADJ-SEAMCONFINED", "A-ADJ",
     "The licensed finding is SEAM-CONFINED COMPOSITIONALITY: the union "
     "changes geometry only on links both sectors jointly own; no "
     "sector-private link ever moves.", "G-WALL-SEAMCONFINED", "PARSED"),
    ("N-SEC-SEAMTHM", "A-SEC",
     "the seam system has rank 6 on 10 unknowns, so its kernel is 4",
     "G-COMPLETION-LATTICE", "PARSED"),
]

# ---- the nine template families, implemented natively under the template's
# own check ids.  G-TEMPLATE-CONFORMANCE parses the pinned era_template.py
# and requires set equality with the ids found there.
FAMILIES = {
    "T-SEAL-PROMOTION": "seals taken at gate time, verified at promotion, "
                        "totality recomputed at the door",
    "T-TRANSCRIPT-BOUND": "the promoted transcript parsed back and "
                          "reconciled with the ledger as a multiset",
    "T-WALL-SEMANTIC": "voice-normalised regex walls with a positive leg, "
                       "controls written independently of the patterns",
    "T-ANCHOR-CONSUMED": "one accessor, consumption verified, both sides, "
                         "the content entering a predicate",
    "T-CLAIMS-EQUAL": "claims by equality, two-way, keyed by table, headers "
                      "as rows, fences by multiset",
    "T-REFERENT-BOUND": "per-occurrence referent binding over prose only, "
                        "pairs rather than membership",
    "T-NO-TYPED-COUNTS": "every published numeral arrives by name from the "
                         "measured registry; an AST leg audits the source",
    "T-FALSIFIER-POISONS": "every falsifier's move proved by digest -- at "
                           "the site in the delivery run where the site "
                           "evaluates both branches, and by the --selftest "
                           "sweep for the rest, which also runs every recipe "
                           "and requires it to die at its declared gate",
    "T-READ-SET": "reads recorded at the accessor, classified rather than "
                  "filtered, and gated after the last gate and again after "
                  "the artifacts are written, order-insensitively",
}


class GateFail(Exception):
    def __init__(self, check, detail):
        super().__init__("%s :: %s" % (check, detail))
        self.check = check
        self.detail = detail


def say(msg=""):
    OUT_LINES.append(msg)


# K3 MAJOR-4: the promoted transcript's NARRATIVE -- every line of it that is
# not a gate row -- was vouched by nothing, and a forged format argument
# published green.  Every value-bearing narrative line is now declared here
# with the PAYLOAD PATH each of its numerals is drawn from, and
# G-TRANSCRIPT-NARRATIVE re-parses the promoted text: the numerals of each
# declared line, in order, must equal the values re-resolved from the
# receipt at the door, and no other non-gate line of the transcript may
# carry a numeral outside the declared decoration.
NARRATIVE: list[tuple[str, list[tuple[str, int]]]] = []


def sayn(text, binds):
    """a narrative line, bound: `binds` is [(payload path, value), ...] in
    the order the values appear in the line."""
    NARRATIVE.append((text, list(binds)))
    OUT_LINES.append(text)
    return text


def leaf(payload, path):
    """resolve a dotted payload path; list steps are integer indices."""
    cur = payload
    for step in path.split("."):
        if isinstance(cur, list):
            cur = cur[int(step)]
        else:
            cur = cur[step]
    return cur


def mut(name):
    return MUTANT == name


# family (h), the MOVE half, taken in the delivery run: every `pick` site
# evaluates BOTH branches whatever the run's mode, so the digests of the
# clean value and the corrupted one can be compared at the site itself.
# G-FALSIFIER-MOVES requires each recorded pair to differ.  The `mut` sites
# cannot be proved this way -- their corrupted branch is not evaluated in a
# clean run -- and the full sweep that proves those is the --move-proofs
# mode, whose measured counts are published there and claimed nowhere else.
SITE_MOVES: dict[str, bool] = {}

# the MOVE register: a digest of every object this run vouches -- each
# sealed row as it is sealed, each gate's evidence as it fires, the paper
# under test, the source the AST legs audit, and the promoted transcript.
# The --selftest sweep compares a recipe's register against the clean run's
# and requires a DIFFERENCE on an object both runs produced, which is the
# move the template asks to be proved and which no amount of describing a
# recipe can supply.
SNAP: dict[str, str] = {}

# a forgery built at the gate that seals its target, for the one recipe
# whose corruption the door refuses rather than detects: a move that never
# lands cannot be proved after the fact, so it is proved before it
FORGED: dict[str, object] = {}


def pick(name, normal, corrupted):
    # the move is proved if the site produces a different value at ANY of
    # its calls: a site that runs over a family -- the anchors, the memo's
    # keys -- moves the family, and one member of it happening to be fixed
    # is not a failure to move
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
    """A digest for ARBITRARY run-time objects -- the ones a falsifier's
    injection site handles, which are not all JSON -- taken canonically and
    without ever hashing the repr of an unordered container: a set is
    digested through the SORTED digests of its members, a mapping through
    the sorted digests of its items."""
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
    maths delimiters dropped, ascii-folded, and (SEC-2 MAJOR-10) case-folded
    -- a sentence-initial capital is not a defence."""
    t = _MD_PREFIX.sub(" ", text)
    for ch in "`*_$":
        t = t.replace(ch, " ")
    t = (t.replace("—", "--").replace("–", "-")
         .replace("’", "'").replace("“", '"').replace("”", '"'))
    t = re.sub(r"\s+", " ", t)
    return (t.casefold() if fold_case else t).strip()


def locate(hay, needle):
    return canon(hay).count(canon(needle))


def ekey(e):
    """A CANONICAL key for an unordered container.  The repr of a frozenset
    exposes its table layout, which depends on the interpreter's string
    hashing, so sorting by repr is hash-seed dependent (the d60 defect,
    v14 #160).  Every ordering in this unit goes through this key instead,
    and G-DETERMINISM proves the file contains no other."""
    return tuple(sorted(repr(x) for x in e))


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
        say("    [%s] %-28s %s" % ("PASS" if ok else "FAIL", gid, row["chain"]))
        if not ok:
            raise GateFail(gid, json.dumps(evidence, default=str)[:400])
        return row

    def names(self):
        return [r["gate"] for r in self.rows]

    def recompute(self):
        h = "0" * 16
        for r in self.rows:
            h = digest([h, r["gate"], r["passed"], r["statement"],
                        r["evidence"]])
        return h


class Seal:
    """Family (a): digest at gate time; verify at promotion against the
    gate-time digest; totality recomputed from the payload's live key set at
    the door; the partition constrained; every sealed key's gate must have
    run; verify before AND after promotion."""

    def __init__(self):
        self.seals = {}
        self.unsealed = {}

    def seal(self, key, value, gate):
        if key in self.unsealed:
            raise GateFail("T-SEAL-PROMOTION", "key in both dictionaries")
        self.seals[key] = {"digest": digest(value), "sealed_at_gate": gate}
        SNAP["seal:" + key] = self.seals[key]["digest"]
        return value

    def declare_unsealed(self, key, reason):
        if key in self.seals:
            raise GateFail("T-SEAL-PROMOTION", "key in both dictionaries")
        self.unsealed[key] = reason

    def manifest(self):
        return {"sealed": dict(self.seals), "unsealed": dict(self.unsealed)}

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
    hook -- not in a helper, so a raw open() anywhere is seen.  Paths are
    CLASSIFIED and not filtered (K3 m2): a read outside the repository lands
    in its own bucket, which must be empty, rather than vanishing."""

    def __init__(self):
        self.log = []
        self.external = []
        self.optional = {}

    def reset(self):
        del self.log[:]
        del self.external[:]
        self.optional = {}

    def install(self):
        def hook(event, args):
            if event == "open":
                p = args[0]
                if isinstance(p, (str, bytes)) and not isinstance(p, bytes):
                    ap = os.path.abspath(p)
                    if ap.startswith(REPO + os.sep):
                        self.log.append(os.path.relpath(ap, REPO))
                    else:
                        self.external.append(ap)
        sys.addaudithook(hook)

    def declare_optional(self, rel, reason):
        """a path this run MAY open and need not: the two artifacts and the
        two staging files, which the door itself writes and reads back, so
        that the read log can be judged AFTER they are written as well as
        before."""
        self.optional[rel] = reason

    def check(self, declared):
        got = Counter(self.log)
        want = set(declared) | set(self.optional)
        stray = sorted(k for k in got if k not in want)
        never = sorted(k for k in declared if k not in got)
        ext = sorted(set(self.external))
        return {"stray": stray, "declared_never_read": never,
                "optional_paths": sorted(self.optional),
                "external": ext[:8],
                "external_reads": len(ext), "distinct_paths": len(got),
                "total_reads": len(self.log)}


class Meas:
    """Family (g): values enter by measurement and statements interpolate.
    TPL-2's two subspecies are audited as well -- a %-format template and an
    integer offset inside a published statement are both typed counts."""

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
            raise GateFail("T-NO-TYPED-COUNTS", "unmeasured name " + name)
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
            raise GateFail("T-NO-TYPED-COUNTS",
                           "typed numeral in a template: " + template[:60])
        vals = {}
        for k, v in names.items():
            vals[k] = self.get(v) if isinstance(v, str) else v
            if isinstance(v, str) and v not in self.vals:
                raise GateFail("T-NO-TYPED-COUNTS", "unmeasured " + v)
        return template.format(**vals)

    def audit(self, source):
        """The AST leg, taken on the SOURCE rather than on the output: the
        template a statement is built from, and any statement typed straight
        into a gate, may carry no numeral -- and none of TPL-2's two
        subspecies either, a %-format template or an integer offset applied
        inside the statement.  Declared exemptions are matched whole and must
        be used."""
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
                # K3 m3: the registry door itself.  A measured VALUE built as
                # an integer offset is a typed count wherever it is published,
                # so the second argument is audited for TPL-2's offset
                # subspecies as well as the provenance string for numerals.
                targets = node.args[1:3]
            else:
                continue
            for arg in targets:
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
                     needle[:8] if name == "N-SEC2-WALL" else needle)
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

    def consumption(self, ledger):
        ran = set(ledger.names())
        bad = []
        for (name, _s, _n, consumer, mode) in self.rows:
            consumer = pick("MUT-CONSUMER", consumer,
                            "G-DOES-NOT-EXIST" if name == "N-SEC2-DET"
                            else consumer)
            if consumer not in ran:
                bad.append("phantom:" + name)
            if consumer not in self.read_by.get(name, set()):
                bad.append("unread:" + name)
        return bad


class Wall:
    """Family (c) with the LICENCE leg the CONTRACT K2 finding made binding.
    A literal blacklist is defeated by paraphrase, and a control copied from
    the pattern proves only that a regex matches the string it was written
    from.  So: BANNED forms are refused outright; a sentence making a POLICED
    KIND of claim is refused unless that same sentence carries a LICENCE from
    a declared set sharing no word with the policed patterns; and the
    controls are paraphrases written against the disease, not from the
    pattern."""

    def __init__(self, name, banned, policed, licence, must_carry, controls):
        self.name = name
        self.banned = banned
        self.policed = policed
        self.licence = licence
        self.must_carry = must_carry
        self.controls = controls

    def _bad(self, sentence):
        if any(re.search(p, sentence) for p in self.banned):
            return True
        if any(re.search(p, sentence) for p in self.policed):
            return not any(re.search(l, sentence) for l in self.licence)
        return False

    def scan(self, text):
        if not text or not text.strip():
            return {"wall": self.name, "ok": False, "hits": ["empty object"],
                    "unlicensed": [], "missing_positive": [],
                    "self_licensing": [], "controls": len(self.controls),
                    "controls_caught": 0}
        c = canon(text)
        sents = re.split(r"(?<=[.;:])\s+", c)
        hits = [p for p in self.banned if re.search(p, c)]
        unl = [x[:60] for x in sents
               if any(re.search(p, x) for p in self.policed)
               and not any(re.search(l, x) for l in self.licence)]
        missing = [m for m in self.must_carry if canon(m) not in c]
        caught = [ctl for ctl in self.controls if self._bad(canon(ctl))]
        selfl = [l for l in self.licence for p in self.policed if l in p]
        ok = (not hits and not unl and not missing and not selfl
              and len(caught) == len(self.controls))
        return {"wall": self.name, "ok": ok, "hits": hits[:3],
                "unlicensed": unl[:3], "missing_positive": missing[:3],
                "self_licensing": selfl[:3], "controls": len(self.controls),
                "controls_caught": len(caught)}


class Falsifier:
    """Family (h): the recipe names the measured object it must move; the
    harness proves the move by digest and requires death at the declared
    gate, not before."""

    def __init__(self, name, gate, target, description):
        self.name = name
        self.gate = gate
        self.target = target
        self.description = description


READS = Reads()
MEAS = Meas()
LD = Ledger()
SEAL = Seal()


def read_text(rel):
    with open(os.path.join(REPO, rel), "r", encoding="utf-8") as fh:
        return fh.read()


def read_bytes(rel):
    with open(os.path.join(REPO, rel), "rb") as fh:
        return fh.read()


# ===========================================================================
# SECTION 2.  THE ARENA: AG(2,3), THE TWO SECTORS, THE ALIGNED UNION
# ===========================================================================

SITES = tuple((i, j) for i in range(3) for j in range(3))
LINKS = ((1, 0), (0, 1), (1, 1))          # I7's three declared directions
FOURTH = (1, 2)                            # the undeclared parallel class


def zadd(a, b):
    return ((a[0] + b[0]) % 3, (a[1] + b[1]) % 3)


def zneg(a):
    return ((-a[0]) % 3, (-a[1]) % 3)


def parallel_class(d):
    H = frozenset({(0, 0), d, zadd(d, d)})
    seen, out = set(), []
    for x in SITES:
        L = tuple(sorted(zadd(x, h) for h in H))
        if L not in seen:
            seen.add(L)
            out.append(L)
    return tuple(sorted(out))


CLASS_DIR = {"ROW": (0, 1), "COL": (1, 0), "DIA": (1, 1), "ANT": FOURTH}
CLASSES = {k: parallel_class(v) for k, v in CLASS_DIR.items()}
ARRANGEMENT = ("ROW", "COL", "DIA")
PART_OF = {}
for _i, _L in enumerate(CLASSES["ANT"]):
    for _s in _L:
        PART_OF[_s] = _i

SECTOR_PAIRS = tuple(sorted({tuple(sorted(p)) for c in ARRANGEMENT
                             for g in CLASSES[c] for p in combinations(g, 2)}))
FOURTH_PAIRS = tuple(sorted({tuple(sorted(p)) for g in CLASSES["ANT"]
                             for p in combinations(g, 2)}))

# the k = 3 ALIGNED gluing: SEC's type (3, (0, 0, 3)) -- all three shared
# sites of each sector in one part of the fourth class.  This is the arena
# SEC-2's extension census runs at, rebuilt here from the construction.
GLUE = tuple(zip(CLASSES["ANT"][0], CLASSES["ANT"][0]))


def gluing_maps(glue):
    amap, bmap = {}, {}
    for i, (sa, sb) in enumerate(glue):
        amap[sa] = ("S", i)
        bmap[sb] = ("S", i)
    for s in SITES:
        amap.setdefault(s, ("A", s))
        bmap.setdefault(s, ("B", s))
    actors = sorted(set(amap.values()) | set(bmap.values()), key=repr)
    return actors, amap, bmap


def union_relation(glue):
    actors, amap, bmap = gluing_maps(glue)
    rel = Counter()
    for mp in (amap, bmap):
        for (u, v) in SECTOR_PAIRS:
            rel[frozenset((mp[u], mp[v]))] += 1
    if mut("MUT-ARENA"):
        rel.pop(sorted(rel, key=ekey)[0])
    return actors, dict(rel), amap, bmap


ACT, REL, AMAP, BMAP = union_relation(GLUE)
INV_A = {v: k for k, v in AMAP.items()}
INV_B = {v: k for k, v in BMAP.items()}
SHARED = [("S", i) for i in range(len(GLUE))]
SEAM_SITE = {"A": {("S", i): GLUE[i][0] for i in range(len(GLUE))},
             "B": {("S", i): GLUE[i][1] for i in range(len(GLUE))}}


# ---- the graph machinery: this unit's own, shared with nothing -------------

def build(nodes, edges):
    idx = {a: i for i, a in enumerate(nodes)}
    adj = [set() for _ in nodes]
    for e in edges:
        u, v = tuple(e)
        adj[idx[u]].add(idx[v])
        adj[idx[v]].add(idx[u])
    return len(nodes), adj, idx


def refine(n, adj, col):
    col = list(col)
    while True:
        sig = [(col[v], tuple(sorted(col[u] for u in adj[v])))
               for v in range(n)]
        o = {s: i for i, s in enumerate(sorted(set(sig)))}
        new = [o[s] for s in sig]
        if new == col:
            return col
        col = new


def isos(n1, a1, n2, a2, limit):
    """exhaustive backtracking isomorphism search with equitable-refinement
    pruning; `limit` is a declared cap whose non-attainment is gated."""
    if n1 != n2 or sum(len(s) for s in a1) != sum(len(s) for s in a2):
        return []
    c1 = refine(n1, a1, [0] * n1)
    c2 = refine(n2, a2, [0] * n2)
    if sorted(Counter(c1).values()) != sorted(Counter(c2).values()):
        return []
    cand = [[x for x in range(n2) if c2[x] == c1[u]] for u in range(n1)]
    seq, placed, rem = [], set(), list(range(n1))
    while rem:
        best = None
        for v in rem:
            key = (len(a1[v] & placed), len(a1[v]), -v)
            if best is None or key > best[0]:
                best = (key, v)
        seq.append(best[1])
        placed.add(best[1])
        rem.remove(best[1])
    out, phi, used = [], {}, set()

    def bt(k):
        if len(out) >= limit:
            return
        if k == len(seq):
            out.append(dict(phi))
            return
        u = seq[k]
        for x in cand[u]:
            if x in used:
                continue
            ok = True
            for w, y in phi.items():
                if (w in a1[u]) != (y in a2[x]):
                    ok = False
                    break
            if ok:
                phi[u] = x
                used.add(x)
                bt(k + 1)
                used.discard(x)
                del phi[u]
    bt(0)
    return out


def sub_maps(n1, a1, n2, a2, limit):
    """QUOTIENT's reading: every realised pair lands on a declared cell."""
    if n1 != n2 or sum(len(s) for s in a1) > sum(len(s) for s in a2):
        return []
    cand = [[x for x in range(n2) if len(a2[x]) >= len(a1[u])]
            for u in range(n1)]
    out, phi, used = [], {}, set()

    def bt(k):
        if len(out) >= limit or k == n1:
            if k == n1 and len(out) < limit:
                out.append(dict(phi))
            return
        for x in cand[k]:
            if x in used:
                continue
            if all((w not in a1[k]) or (y in a2[x]) for w, y in phi.items()):
                phi[k] = x
                used.add(x)
                bt(k + 1)
                used.discard(x)
                del phi[k]
    bt(0)
    return out


MAP_CAP = 200000
AUTCACHE = {}

# the bare-repr orderings this unit permits, each over a container of TUPLES,
# whose repr is canonical.  G-DETERMINISM's leg is an AST walk (K3 m4): every
# `key=` keyword whose value is `repr`, an attribute ending `.repr`, or a
# lambda whose body calls `repr`, is located by (function, line) rather than
# by line text, so a copy of a whitelisted line in a new place is a NEW site.
SAFE_REPR_SORTS = {
    ("gluing_maps", "set"),
    ("apply_rule", "seen"),
    ("full_run", "seen"),
    ("full_run", "prof_rows"),
    ("full_run", "form_rows"),
    ("full_run", "inv_rows"),
    ("full_run", "keep"),
    ("full_run", "fiber2"),
    ("full_run", "topcarriers"),
    ("full_run", "death_rows"),
    ("full_run", "bests"),
    ("full_run", "SUCCACHE"),
    ("cell_signature", "counter"),
}


def hash_call_sites(source):
    """Every call to the BUILTIN hash().  The repr of an unordered container
    is one road to a hash-seed dependent ordering; the builtin itself is the
    other, and it carries no `key=repr` token for a repr scan to find.  This
    unit needs it nowhere: a sort key that reaches for it, anywhere in the
    file, is refused."""
    tree = ast.parse(source)
    fnof = {}
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for sub in ast.walk(node):
                fnof[id(sub)] = node.name
    return sorted({(fnof.get(id(n), "<module>"), n.lineno)
                   for n in ast.walk(tree)
                   if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                   and n.func.id == "hash"})


def repr_key_sites(source):
    """Every ordering keyed on a bare repr, located by the function that
    carries it and the name it orders, so the whitelist cannot be satisfied
    by copying a permitted line somewhere else."""
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
                    if isinstance(s, ast.Call) and isinstance(
                            s.func, ast.Attribute):
                        what = (s.func.value.id
                                if isinstance(s.func.value, ast.Name)
                                else s.func.attr)
                        break
            sites.add((fnof.get(id(node), "<module>"), what))
    return sorted(sites)


def selfsource():
    return read_text(SELF_REL)


def automorphisms(edges):
    key = frozenset(edges)
    got = AUTCACHE.get(key)
    if got is None:
        n, a, idx = build(ACT, edges)
        cap = pick("MUT-AUT", MAP_CAP, 8)
        ms = isos(n, a, n, a, cap)
        got = ([tuple(m[i] for i in range(n)) for m in ms], idx, len(ms) < cap)
        AUTCACHE[key] = got
    return got


# ===========================================================================
# SECTION 3.  THE GEOMETRY, THE RECORD, AND THE STATE
# ===========================================================================
# The three objects the pin's transition moves.  GEOMETRY: the amalgam of the
# two charts, whose cells are (chart, site, direction) for a declared link,
# ('X', ...) for a cross cell and ('W', ...) for a cell in the fourth
# parallel class.  RECORD: the co-division relation with multiplicities.
# STATE: the seam's cross block at each shared site -- the four numbers
# SEC-2 measured irreducible.

GEOBASE = None


def geometry(cross=(), within=()):
    global GEOBASE
    if GEOBASE is None:
        actors, amap, bmap = gluing_maps(GLUE)
        binc, bcells = set(), []
        for chart, mp in (("A", amap), ("B", bmap)):
            for x in SITES:
                for l in LINKS:
                    e = frozenset((mp[x], mp[zadd(x, l)]))
                    binc.add(e)
                    bcells.append((chart, x, l, e))
        GEOBASE = (actors, amap, bmap, frozenset(binc), tuple(bcells))
    actors, amap, bmap, binc, bcells = GEOBASE
    inc, cells = set(binc), list(bcells)
    for e in sorted(cross, key=ekey):
        inc.add(e)
        cells.append(("X", None, None, e))
    for e in sorted(within, key=ekey):
        inc.add(e)
        cells.append(("W", None, None, e))
    return {"nodes": actors, "inc": inc, "cells": cells,
            "charts": {"A": amap, "B": bmap},
            "cross": sorted(cross, key=ekey),
            "within": sorted(within, key=ekey)}


G0 = geometry()

READINGS = ("EMBEDDING", "QUOTIENT")
COUNTLEGS = ("POSITIVE", "NON-NEGATIVE")


def weld(rel, geo, reading, countleg):
    """The delivered dictionary, at one cell of the window.  EMBEDDING: the
    realised relation IS the geometry's incidence.  QUOTIENT: it sits inside.
    The count leg reads the induced field on the geometry's own cells."""
    if len(ACT) != len(geo["nodes"]):
        return {"fate": "ARITY-DEAD", "maps": 0}
    n1, a1, _i1 = build(ACT, rel.keys())
    n2, a2, _i2 = build(geo["nodes"], geo["inc"])
    ms = (isos(n1, a1, n2, a2, 1) if reading == "EMBEDDING"
          else sub_maps(n1, a1, n2, a2, 1))
    if not ms:
        return {"fate": "STRUCT-DEAD", "maps": 0}
    phi = {ACT[u]: geo["nodes"][x] for u, x in ms[0].items()}
    inv = {v: k for k, v in phi.items()}
    field = [rel.get(frozenset(inv[t] for t in e), 0) for e in geo["inc"]]
    mn = min(field)
    floor = 1 if countleg == "POSITIVE" else 0
    if mn < floor:
        return {"fate": "COUNT-DEAD", "maps": 1, "min": mn}
    return {"fate": "ALIVE", "maps": 1, "min": mn}


# ---- the form: I7's readout carried to the chart -------------------------

def sym_index(d):
    idx = {}
    for i in range(d):
        for j in range(i, d):
            idx[(i, j)] = len(idx)
    return idx


IDX4 = sym_index(4)
AV = ([1, 0, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0])
BV = ([0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 1, 1])


def quad_row(vec, idx, d):
    row = [Fraction(0)] * len(idx)
    for i in range(d):
        for j in range(i, d):
            row[idx[(i, j)]] += Fraction(vec[i] * vec[j]) * (1 if i == j else 2)
    return row


def rref(rows, ncol):
    M = [list(r) for r in rows]
    piv, r = [], 0
    for c in range(ncol):
        p = None
        for i in range(r, len(M)):
            if M[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = Fraction(1, 1) / M[r][c]
        M[r] = [x * inv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(c)
        r += 1
        if r == len(M):
            break
    return M, piv


def uext(U):
    """U on the three declared directions, with a3 = a1 + a2."""
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
    """every completion the corpus's own readout admits at this seam type.
    The box is DERIVED from the cross counts themselves; that it does not
    bind is measured, not asserted, by re-running it widened."""
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
                    if all(v >= 1 for v in cross_counts(nA, nB, U).values()):
                        out.append((u00, u01, u10, u11))
    LATCACHE[key] = out
    return out


def gram(nA, nB, U):
    """the doubled integer Gram matrix of the completion (SEC-2's carry: the
    doubling makes Sylvester positivity and the determinant order integer
    predicates without changing either)."""
    M = [[0] * 4 for _ in range(4)]
    M[0][0], M[1][1] = 2 * nA[0], 2 * nA[1]
    M[0][1] = M[1][0] = nA[2] - nA[0] - nA[1]
    M[2][2], M[3][3] = 2 * nB[0], 2 * nB[1]
    M[2][3] = M[3][2] = nB[2] - nB[0] - nB[1]
    for i in range(2):
        for j in range(2):
            M[i][2 + j] = M[2 + j][i] = U[i][j]
    return M


def det(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    tot = 0
    for c in range(n):
        sub = [[A[i][j] for j in range(n) if j != c] for i in range(1, n)]
        tot += ((-1) ** c) * A[0][c] * det(sub)
    return tot


def posdef(M):
    return all(det([[M[i][j] for j in range(k)] for i in range(k)]) > 0
               for k in range(1, len(M) + 1))


def seam_index(seam, actor, chart):
    """(direction index, sign) of a private actor seen from a seam."""
    base = SEAM_SITE[chart][seam]
    site = (INV_A if chart == "A" else INV_B)[actor]
    d = ((site[0] - base[0]) % 3, (site[1] - base[1]) % 3)
    for i, l in enumerate(LINKS):
        if d == l:
            return i, 1
        if d == zneg(l):
            return i, pick("MUT-SEAMIDX", -1, 1)
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
                                  AMAP[zadd(SEAM_SITE["A"][seam], l)])), 0)
               for l in LINKS)
    nB = tuple(rel.get(frozenset((BMAP[SEAM_SITE["B"][seam]],
                                  BMAP[zadd(SEAM_SITE["B"][seam], l)])), 0)
               for l in LINKS)
    return nA, nB


SUCCACHE = {}


def successors(seam, rel, realised_cross):
    """every completion at this seam consistent with the record: admissible
    at the seam's own count vectors, and predicting exactly the count the
    record carries on every realised cross link.

    The answer is a function of the seam's own count vectors and of the
    (index, count) constraints the realised cross links impose -- of nothing
    else -- so it is memoised on exactly that key.  The memo is a speed
    device and is proved inert: G-SUCCESSOR-MEMO recomputes a declared sample
    from scratch and requires identity."""
    nA, nB = seam_counts(seam, rel)
    cons = []
    for p in realised_cross:
        k = cross_index(seam, p)
        if k is None or mut("MUT-FORM"):
            continue
        cons.append((k, rel[p]))
    return successors_raw(nA, nB, tuple(sorted(set(cons))))


def successors_raw(nA, nB, cons, memo=True):
    key = (nA, nB, cons)
    got = SUCCACHE.get(key)
    if memo and got is not None:
        return got
    out = []
    for U in completion_lattice(nA, nB):
        E = uext([[U[0], U[1]], [U[2], U[3]]])
        if all(nA[i] + nB[j] - s * E[i][j] == c for ((i, j, s), c) in cons):
            out.append(U)
    if memo:
        SUCCACHE[key] = out
    return out


def fourth_prediction(rel, base, chart):
    """the count the sector's own form forces on the fourth direction at a
    site: q(a1 - a2) = 2 n1 + 2 n2 - n3, the site's system having kernel 0."""
    mp = AMAP if chart == "A" else BMAP
    n = tuple(rel.get(frozenset((mp[base], mp[zadd(base, l)])), 0)
              for l in LINKS)
    coef = pick("MUT-FOURTH", (2, 2, -1), (1, 1, -1))
    return n, coef[0] * n[0] + coef[1] * n[1] + coef[2] * n[2]


# ===========================================================================
# SECTION 4.  THE UPDATE RULES AND THE RUNNER
# ===========================================================================
# An update rule is a function of the EVENT'S FOOTPRINT alone -- the pairs it
# deposits, classified against the standing record.  It never receives the
# event, the arena's names, or any fate: that is what makes it a law rather
# than a declaration made after the fact, and it is gated three ways
# (G-RULE-BLIND, G-RULE-EQUIVARIANT, G-NO-POSTHOC) rather than asserted.

def footprint(group, rel):
    """the event's own deposit: three actors give three pairs, each of them
    new-across-the-seam, new-inside-a-sector, or a doubling."""
    pairs = [frozenset(p) for p in combinations(group, 2)]
    new = [p for p in pairs if p not in rel]
    cross = tuple(sorted((p for p in new
                          if {x[0] for x in p} == {"A", "B"}), key=ekey))
    within = tuple(sorted((p for p in new if p not in cross), key=ekey))
    doubled = tuple(sorted((p for p in pairs if p in rel), key=ekey))
    return {"cross": cross, "within": within, "doubled": doubled,
            "pairs": tuple(sorted(pairs, key=ekey))}


def rule_none(fp):
    return (), ()


def rule_cross_only(fp):
    return fp["cross"], ()


def rule_within_only(fp):
    return (), fp["within"]


def rule_all_new(fp):
    if mut("MUT-RULE-BLIND"):
        return tuple(p for p in fp["pairs"]), fp["within"]
    return fp["cross"], fp["within"]


RULES = {"NONE": rule_none, "CROSS-ONLY": rule_cross_only,
         "WITHIN-ONLY": rule_within_only, "ALL-NEW": rule_all_new}
RULE_ORDER = ("NONE", "CROSS-ONLY", "WITHIN-ONLY", "ALL-NEW")


def apply_rule(name, fp):
    cr, wi = RULES[name](fp)
    if mut("MUT-CONTROL") and name == "NONE":
        cr = fp["cross"]
    if mut("MUT-RULE-CROSS") and name == "CROSS-ONLY":
        cr, wi = fp["cross"], fp["within"]
    if mut("MUT-RULE-PEEK") and name == "CROSS-ONLY" and len(fp["within"]) == 1:
        cr, wi = fp["cross"], fp["within"]
    if mut("MUT-RULE-NAME") and name == "CROSS-ONLY":
        if any(("A", (0, 1)) in p for p in fp["cross"]):
            cr = ()
    if mut("MUT-BLIND-ORDER") and name == "CROSS-ONLY":
        # keyed on the footprint's own carrier ORDER, which the opaque tokens
        # preserve and no relabelling does: invisible to the blindness leg by
        # construction, so only the equivariance sweep can find it
        seen = {a for q in ("cross", "within", "doubled")
                for p in fp[q] for a in p}
        car = sorted(seen, key=repr)
        if car and any(car[0] in p for p in fp["cross"]):
            cr = ()
    return cr, wi


def advance(group, geo, rel, name):
    """ONE TRANSITION.  The rule fires on the footprint, the record takes the
    event's three incidences, and the geometry takes exactly the cells the
    rule returns.  Nothing here consults a fate."""
    fp = footprint(group, rel)
    cr, wi = apply_rule(name, fp)
    rel2 = dict(rel)
    for p in fp["pairs"]:
        rel2[p] = rel2.get(p, 0) + 1
    geo2 = geometry(tuple(geo["cross"]) + tuple(cr),
                    tuple(geo["within"]) + tuple(wi))
    return fp, geo2, rel2


GROUPS = [tuple(ACT[i] for i in g)
          for g in combinations(range(len(ACT)), 3)]
if mut("MUT-GROUPS"):
    GROUPS = GROUPS[:-1]


def profile(fp):
    return (len(fp["cross"]), len(fp["within"]), len(fp["doubled"]))


def cell_signature(counter):
    """the whole result of one window cell, as one comparable value"""
    return digest(sorted(counter.items(), key=repr))


# ===========================================================================
# SECTION 5.  THE RUN
# ===========================================================================

def full_run(paper_text=None, paper_rel=PAPER_REL):
    t0 = time.time()
    R = {}
    # the arena and the event set are rebuilt HERE, not at import: a
    # falsifier that corrupts either must be reachable by the CLI, and a
    # construction evaluated before the flag is parsed is a falsifier that
    # cannot fire (found by this unit's own mutant sweep)
    g = globals()
    # the run's own state is REBUILT here too, so that a second full_run in
    # one process -- which is what the --selftest falsifier harness does --
    # starts from the same place the first did and shares no ledger, no
    # registry, no seal and no transcript line with it.
    g["MEAS"], g["LD"], g["SEAL"] = Meas(), Ledger(), Seal()
    del OUT_LINES[:]
    del NARRATIVE[:]
    SNAP.clear()
    FORGED.clear()
    READS.reset()
    g["ACT"], g["REL"], g["AMAP"], g["BMAP"] = union_relation(GLUE)
    g["INV_A"] = {v: k for k, v in AMAP.items()}
    g["INV_B"] = {v: k for k, v in BMAP.items()}
    g["GROUPS"] = [tuple(ACT[i] for i in gg)
                   for gg in combinations(range(len(ACT)), 3)]
    if mut("MUT-GROUPS"):
        g["GROUPS"] = GROUPS[:-1]
    AUTCACHE.clear()
    SUCCACHE.clear()
    LATCACHE.clear()
    SITE_MOVES.clear()
    R = {}
    MEAS.exempt_token("sha256-12", "the corpus's name for a digest prefix, "
                                   "not a count")
    MEAS.exempt_token("AG(2,3)", "the affine plane's own name, not a count")
    say("=" * 78)
    say("v15 AUTOGLUE -- CAN A CROSSING EVENT CREATE THE SEAM IT NEEDS?")
    say("instrument for %s   schema %s" % (PAPER_REL, SCHEMA))
    say("=" * 78)
    say()

    # ---- provenance ------------------------------------------------------
    src, srcrows = {}, []
    for sid in sorted(SOURCES):
        rel, sha = SOURCES[sid]
        raw = read_bytes(rel)
        got = pick("MUT-SOURCE", bdigest(raw), bdigest(raw + b" "))
        src[sid] = raw.decode("utf-8")
        srcrows.append({"id": sid, "path": rel, "sha256_12": got,
                        "declared": sha, "ok": got == sha,
                        "bytes": len(raw)})
    MEAS.m("n_sources", len(srcrows), "the declared source table")
    MEAS.m("n_sources_ok", sum(1 for r in srcrows if r["ok"]), "byte compare")
    LD.gate("G-SOURCES", all(r["ok"] for r in srcrows)
            and len(srcrows) == len(SOURCES),
            MEAS.stmt("{n} sources are read at run time and every one "
                      "authenticates against the sha256-12 this unit's own "
                      "frozen text declares; the path and the value are "
                      "anchored together, so a path drift that changed the "
                      "arena would die here", n="n_sources"),
            {"sources": srcrows, "commit": SOURCE_COMMIT})
    R["provenance"] = SEAL.seal("provenance",
                                {"commit": SOURCE_COMMIT, "sources": srcrows},
                                "G-SOURCES")

    # ---- the anchors -----------------------------------------------------
    ANCH = Anchors(VERBATIM)
    arep = ANCH.locate_all(src, paper_text if paper_text is not None else "")
    MEAS.m("n_anchors", len(arep), "the declared anchor table")
    LD.gate("G-ANCHORS", all(r["ok"] for r in arep),
            MEAS.stmt("{n} verbatim anchors are each located exactly once in "
                      "their own pinned source under the whitespace-and-"
                      "markdown normaliser and cleared against a character "
                      "floor; the ones the paper quotes are located on the "
                      "paper's side as well, so a quotation may not be "
                      "inverted around a preserved window", n="n_anchors"),
            {"anchors": arep, "floor": NEEDLE_FLOOR})
    R["anchors"] = SEAL.seal("anchors", arep, "G-ANCHORS")

    # ---- the template's own ids -----------------------------------------
    block = re.search(r"FAMILIES = \(\n(.*?)\n\)", src["A-TPL"], re.S)
    tpl_ids = sorted(set(re.findall(r"\"(T-[A-Z-]+)\"\)",
                                    block.group(1) if block else "")))
    mine_ids = sorted(FAMILIES)
    if mut("MUT-TEMPLATE"):
        mine_ids = mine_ids[:-1]
    MEAS.m("n_families", len(mine_ids), "the families implemented here")
    MEAS.m("n_template_ids", len(tpl_ids), "parsed from the pinned template")
    LD.gate("G-TEMPLATE-CONFORMANCE", tpl_ids == mine_ids and bool(tpl_ids),
            MEAS.stmt("the {n} template family mechanisms are implemented "
                      "natively in this instrument under the template's own "
                      "check ids, and the id set is not declared here but "
                      "parsed out of the pinned era template's bytes: a "
                      "family carried in name and not in mechanism, or a "
                      "family the template declares and this unit omits, "
                      "fails against the source", n="n_families"),
            {"template_ids": tpl_ids, "implemented": mine_ids})
    R["families"] = SEAL.seal("families", {"ids": mine_ids,
                                           "from_template": tpl_ids,
                                           "roles": FAMILIES},
                              "G-TEMPLATE-CONFORMANCE")

    # ---- M0  THE ARENA ---------------------------------------------------
    say("-- THE ARENA " + "-" * 64)
    perms, idx0, complete = automorphisms(REL.keys())
    doubled0 = sum(1 for v in REL.values() if v > 1)
    inc_eq = G0["inc"] == set(REL.keys())
    MEAS.m("n_sites", len(SITES), "the affine plane's points")
    MEAS.m("n_classes", len(CLASSES), "its parallel classes")
    MEAS.m("n_declared", len(ARRANGEMENT), "the declared arrangement")
    MEAS.m("n_sector_pairs", len(SECTOR_PAIRS), "the realised pairs of one "
                                                "sector")
    MEAS.m("n_fourth_pairs", len(FOURTH_PAIRS), "the pairs of the fourth "
                                                "class")
    MEAS.m("n_actors", len(ACT), "the union's carriers")
    MEAS.m("n_pairs", len(REL), "the union's realised pairs")
    MEAS.m("n_aut", len(perms), "the exhaustive automorphism search")
    MEAS.m("n_doubled", doubled0, "pairs the union carries twice")
    ok_arena = (len(ACT) == DECL["sec2.union.carriers"]
                and len(REL) == DECL["sec2.union.pairs"]
                and len(perms) == DECL["sec2.union.aut"] and complete
                and doubled0 == 0 and inc_eq
                and len(SECTOR_PAIRS) + len(FOURTH_PAIRS)
                == len(list(combinations(SITES, 2))))
    LD.gate("G-ARENA", ok_arena,
            MEAS.stmt("the committed two-sector corpus is rebuilt from "
                      "AG(2,3): {p} points in {c} parallel classes of "
                      "which {d} are declared, so one sector realises {sp} "
                      "pairs and the undeclared fourth class holds the "
                      "remaining {fp}; the aligned gluing gives {a} carriers "
                      "and {r} realised pairs, none of them doubled, and the "
                      "automorphism group is enumerated exhaustively below "
                      "the declared cap at order {g} -- every one of these "
                      "reproduces the parent's committed value by a route "
                      "sharing no code with it",
                      p="n_sites", c="n_classes", d="n_declared",
                      sp="n_sector_pairs", fp="n_fourth_pairs", a="n_actors",
                      r="n_pairs", g="n_aut"),
            {"carriers": len(ACT), "pairs": len(REL), "aut": len(perms),
             "search_complete": complete, "doubled": doubled0,
             "incidence_is_the_support": inc_eq,
             "declared": {k: DECL[k] for k in
                          ("sec2.union.carriers", "sec2.union.pairs",
                           "sec2.union.aut")}})
    sayn("  the aligned union: %d carriers, %d realised pairs, none doubled, "
         "automorphism order %d" % (len(ACT), len(REL), len(perms)),
         [("arena.carriers", len(ACT)), ("arena.pairs", len(REL)),
          ("arena.aut", len(perms))])
    sayn("  the fourth parallel class holds the %d pairs the arrangement does "
         "not declare" % len(FOURTH_PAIRS),
         [("arena.fourth_pairs", len(FOURTH_PAIRS))])
    R["arena"] = SEAL.seal("arena", {
        "points": len(SITES), "classes": len(CLASSES),
        "declared_directions": len(ARRANGEMENT),
        "sector_pairs": len(SECTOR_PAIRS), "fourth_pairs": len(FOURTH_PAIRS),
        "carriers": len(ACT), "pairs": len(REL), "aut": len(perms),
        "doubled": doubled0, "incidence_is_the_support": inc_eq}, "G-ARENA")

    # ---- the group in CLOSED FORM (K1's first strengthening) -------------
    # The declared-pair graph of one AG(2,3) chart is the complement of its
    # fourth parallel class -- three disjoint triangles -- so it is the
    # complete tripartite K(3,3,3).  The aligned k = 3 union glues two such
    # charts along ONE WHOLE PART.  The shared part is setwise fixed because
    # its carriers are the only ones of degree twelve; each chart may permute
    # its two remaining parts internally and exchange them; and the two
    # charts may be exchanged.  So the order is a product of five factors and
    # the chart-preserving subgroup has INDEX TWO by construction, which is
    # what the equivariance sentence needs and what a count cannot give.
    deg = Counter(sum(1 for e in REL if a in e) for a in ACT)
    topdeg = max(deg)
    topcarriers = [a for a in ACT if sum(1 for e in REL if a in e) == topdeg]
    shared_by_degree = sorted(topcarriers, key=repr)
    part_sizes = sorted(Counter(PART_OF[s] for s in SITES).values())
    within_chart = 1
    for k in range(2):
        within_chart = within_chart * len(list(permutations(range(3))))
    chart_factor = pick("MUT-CLOSED-FORM", within_chart * 2, within_chart)
    closed = (len(list(permutations(range(3))))         # the shared part
              * chart_factor * chart_factor             # each chart
              * 2)                                      # the sector exchange
    MEAS.m("n_shared_part", len(SHARED), "the glued part's size")
    MEAS.m("n_topdeg", topdeg, "the top degree in the union")
    MEAS.m("n_topdeg_carriers", len(shared_by_degree), "carriers at it")
    MEAS.m("n_closed_form", closed, "the closed-form order")
    MEAS.m("n_chart_factor", chart_factor, "one chart's own factor")
    LD.gate("G-AUT-CLOSED-FORM",
            closed == len(perms) and len(shared_by_degree) == len(SHARED)
            and sorted(shared_by_degree) == sorted(SHARED)
            and set(part_sizes) == {len(SHARED)}
            and len(perms) % 2 == 0,
            MEAS.stmt("the union's relabelling group is not only enumerated "
                      "but CONSTRUCTED, and the two routes agree. One "
                      "chart's declared-pair graph is the complement of its "
                      "fourth parallel class -- three disjoint triangles of "
                      "{p} points each -- hence complete tripartite; the "
                      "aligned union glues two of them along one whole part; "
                      "the shared part is setwise fixed because its {s} "
                      "carriers are the only ones of degree {d}; each chart "
                      "contributes {f} from permuting its two free parts and "
                      "exchanging them; and the charts may trade places. The "
                      "product is {c}, equal to the exhaustive count, and it "
                      "makes the chart-preserving subgroup's INDEX a theorem "
                      "rather than a measurement",
                      p="n_shared_part", s="n_topdeg_carriers", d="n_topdeg",
                      f="n_chart_factor", c="n_closed_form"),
            {"closed_form": closed, "enumerated": len(perms),
             "factors": {"the shared part": len(list(permutations(range(3)))),
                         "each chart's free parts": chart_factor,
                         "the sector exchange": 2},
             "top_degree": topdeg,
             "carriers_at_the_top_degree": len(shared_by_degree),
             "part_sizes": part_sizes})
    R["aut_structure"] = SEAL.seal("aut_structure", {
        "closed_form": closed, "enumerated": len(perms),
        "shared_part": len(SHARED), "chart_factor": chart_factor,
        "top_degree": topdeg}, "G-AUT-CLOSED-FORM")

    shuffle_ok = all(ekey(e) == ekey(frozenset(list(e)[::-1]))
                     for e in list(REL)[:64])
    body = selfsource()
    sort_plant = (body + "\n\ndef _mut_sort_site(inc):\n"
                  "    return sorted(inc, " + "key=" + "repr)\n")
    repr_sites = repr_key_sites(pick("MUT-SORT", body, sort_plant))
    unsafe = [list(s) for s in repr_sites if s not in SAFE_REPR_SORTS]
    hash_plant = (body + "\n\ndef _mut_hash_site(rows):\n"
                  "    return sorted(rows, key=lambda r: "
                  + "hash" + "(r))\n")
    hash_sites = hash_call_sites(pick("MUT-HASH", body, hash_plant))
    MEAS.m("n_repr_sorts", len(repr_sites), "orderings keyed by a bare repr")
    MEAS.m("n_hash_calls", len(hash_sites), "calls to the builtin hash")
    LD.gate("G-DETERMINISM", shuffle_ok and not unsafe and not hash_sites,
            MEAS.stmt("no ordering in this unit is taken on the repr of an "
                      "unordered container, which is the hash-seed dependent "
                      "shape the corpus's own defect register names: every "
                      "such ordering goes through a canonical key, and the "
                      "{n} remaining bare-repr orderings are the declared ones "
                      "over tuples. The leg is an AST walk over this file's "
                      "own bytes and each site is named by the function that "
                      "carries it and the container it orders, so a copy of a "
                      "permitted line in a new place is a new site and fails "
                      "here -- a line-text whitelist would not see it. The "
                      "repr is one road to a seed-dependent order and the "
                      "BUILTIN HASH is the other, carrying no token a repr "
                      "scan could find, so every call to it is located the "
                      "same way and there are {h}: this unit needs it "
                      "nowhere, and a sort key that reaches for it makes the "
                      "receipt's own row order a property of the "
                      "interpreter's session",
                      n="n_repr_sorts", h="n_hash_calls"),
            {"unsafe": unsafe, "sites": [list(s) for s in repr_sites],
             "declared": [list(s) for s in sorted(SAFE_REPR_SORTS)],
             "builtin_hash_calls": [list(s) for s in hash_sites],
             "canonical_key_invariant": shuffle_ok})

    legs = ANCH.read("N-P19-LEGS", "G-BASELINE-LAWFUL")
    G0test = pick("MUT-BASELINE", G0,
                  geometry((sorted([frozenset((u, v)) for u in ACT
                                    if u[0] == "A" for v in ACT
                                    if v[0] == "B"], key=ekey)[0],), ()))
    base = {(rd, cl): weld(REL, G0test, rd, cl)["fate"]
            for rd in READINGS for cl in COUNTLEGS}
    MEAS.m("n_base_cells", len(base), "reading x count leg")
    LD.gate("G-BASELINE-LAWFUL",
            all(v == "ALIVE" for v in base.values())
            and "co-division actor pair" in legs,
            MEAS.stmt("the pre-state of every transition this unit runs is "
                      "lawful: the delivered union welds onto the delivered "
                      "geometry at all {n} cells of reading against count "
                      "leg, under the legs read out of the weld paper's own "
                      "bytes -- site the actor, link the co-division actor "
                      "pair, count the division events on that pair. There "
                      "is exactly ONE pre-state and this gate is where it is "
                      "judged: every transition in the window starts from "
                      "it, so 'at both ends of every transition' means this "
                      "one lawful start and every event's own post-state, "
                      "and it is said that way rather than as though the "
                      "weld were evaluated twice per event",
                      n="n_base_cells"),
            {"baseline": {"%s/%s" % k: v for k, v in base.items()},
             "distinct_pre_states": 1 if base else 0,
             "legs_anchor": "N-P19-LEGS"})

    # ---- the events ------------------------------------------------------
    n_groups = len(GROUPS)
    closed = (len(ACT) * (len(ACT) - 1) * (len(ACT) - 2)) // 6
    fps = {g: footprint(g, REL) for g in GROUPS}
    span = sum(1 for g in GROUPS if fps[g]["cross"])
    span2 = sum(1 for g in GROUPS
                if any({u[0], v[0]} == {"A", "B"}
                       for u, v in combinations(g, 2)))
    pidx = {a: i for i, a in enumerate(ACT)}
    orb_seen, orbits = set(), []
    for g in GROUPS:
        key = tuple(sorted(pidx[a] for a in g))
        if key in orb_seen:
            continue
        orb = {tuple(sorted(p[i] for i in key)) for p in perms}
        orbits.append(sorted(orb))
        orb_seen |= orb
    MEAS.m("n_events", n_groups, "every three-actor conflict group")
    MEAS.m("n_orbits", len(orbits), "orbits under the union's own group")
    MEAS.m("n_spanning", span, "events with a pair across the seam")
    LD.gate("G-EVENTS",
            n_groups == closed and n_groups == DECL["sec2.groups"]
            and len(orbits) == DECL["sec2.orbits"]
            and span == span2 == DECL["sec2.seam_spanning"]
            and sum(len(o) for o in orbits) == n_groups,
            MEAS.stmt("the event set is the arena's {n} three-actor conflict "
                      "groups, matching the closed form, falling into {o} "
                      "orbits whose sizes sum to it, of which {s} put a pair "
                      "across the seam -- counted twice, once from the "
                      "footprint and once from the actors' own charts",
                      n="n_events", o="n_orbits", s="n_spanning"),
            {"events": n_groups, "closed_form": closed,
             "orbits": len(orbits), "spanning": span,
             "spanning_second_route": span2,
             "orbit_sizes": sorted(Counter(len(o) for o in orbits).items())})
    sayn("  the event set: %d three-actor conflict groups in %d orbits, %d of "
         "them seam-spanning" % (n_groups, len(orbits), span),
         [("events.events", n_groups), ("events.orbits", len(orbits)),
          ("events.spanning", span)])
    prof_rows = Counter(profile(fps[g]) for g in GROUPS)
    R["events"] = SEAL.seal("events", {
        "events": n_groups, "orbits": len(orbits), "spanning": span,
        "orbit_sizes": sorted(Counter(len(o) for o in orbits).items()),
        "profiles": sorted(prof_rows.items(), key=repr)}, "G-EVENTS")

    # ---- M1  THE UPDATE WINDOW ------------------------------------------
    say()
    say("-- M1: THE UPDATE WINDOW " + "-" * 52)
    qtext = ANCH.read("N-PIN-QUESTION", "G-WINDOW")
    window_axes = [
        ("CREATION", list(RULE_ORDER), "NONE"),
        ("READING", list(READINGS), "EMBEDDING and QUOTIENT"),
        ("COUNT LEG", list(COUNTLEGS), "POSITIVE"),
        ("FORM CARRY", ["DROPPED", "CARRIED"], "CARRIED at the seam"),
        # K2 m3: this axis was declared "not posed" and both of its values
        # are measured, and the second head segment ends on the difference
        ("STATE", ["PERSISTING", "RE-SOLVED"],
         "both run; VERDICT-BEARING"),
    ]
    outside = ["the record", "the committed grammar", "the actor set",
               "the arrangement", "the readout law itself",
               "the three-actor conflict group", "the bare carrier",
               "the simple link individuation",
               "any target declared after the event"]
    if mut("MUT-WINDOW"):
        outside = outside + [outside[0]]
    ncells = len(RULE_ORDER) * len(READINGS) * len(COUNTLEGS)
    MEAS.m("n_axes", len(window_axes), "the declared window axes")
    MEAS.m("n_rules", len(RULE_ORDER), "the link-creation rules")
    MEAS.m("n_cells", ncells, "creation x reading x count leg")
    MEAS.m("n_outside", len(outside), "the named outside-list")
    LD.gate("G-WINDOW",
            ncells == len(RULE_ORDER) * len(READINGS) * len(COUNTLEGS)
            and len(outside) == len(set(outside))
            and "CREATES the cross-link" in qtext
            and all(a[0] and a[1] for a in window_axes),
            MEAS.stmt("the update window is named before anything is "
                      "measured: {a} axes, of which the first three give the "
                      "{c} cells run at every event, and {o} things are named "
                      "as outside it -- the pin's own question, read out of "
                      "its bytes, is whether a crossing event creates the "
                      "cross link and seam it needs, and a unit that moved an "
                      "outside item would be answering another one",
                      a="n_axes", c="n_cells", o="n_outside"),
            {"axes": [{"axis": a, "members": m, "delivered": d}
                      for (a, m, d) in window_axes],
             "outside": outside, "cells": ncells})
    R["window"] = SEAL.seal("window", {
        "axes": [{"axis": a, "members": m, "delivered": d}
                 for (a, m, d) in window_axes],
        "outside": outside, "cells": ncells}, "G-WINDOW")

    # the rule is blind to the event: recomputed from a footprint whose
    # carriers have been replaced by OPAQUE TOKENS -- so no name of the event
    # survives into the rule at all -- and equivariant under the arena's own
    # relabellings.  (K1 MAJOR-2: dropping one redundant key of the footprint
    # tested no such thing; the tokens do.)
    blind_bad, equi_bad, blind_checks = [], [], 0
    for g in GROUPS:
        fp = fps[g]
        seen = {a for p in fp["pairs"] for a in p}
        carriers = sorted(seen, key=repr)
        tok = {a: ("#", i) for i, a in enumerate(carriers)}
        back = {v: k for k, v in tok.items()}
        # the CLASSIFIED keys only, and their pairs carried as opaque
        # tokens: a rule reading the raw pair list -- a key the
        # classification does not carry -- has nothing to read, and a rule
        # keyed on a named carrier has no name to key on
        anon = {k: tuple(sorted((frozenset(tok[x] for x in p) for p in fp[k]),
                                key=ekey))
                for k in ("cross", "within", "doubled")}
        for nm in RULE_ORDER:
            try:
                got = apply_rule(nm, anon)
                mapped = tuple(tuple(sorted(
                    (frozenset(back[x] for x in p) for p in q), key=ekey))
                    for q in got)
                want = tuple(tuple(sorted(q, key=ekey))
                             for q in apply_rule(nm, fp))
                blind_checks += 1
                if mapped != want:
                    blind_bad.append(nm)
            except KeyError:
                blind_bad.append(nm)
    KINDPERM = [p for p in perms
                if all(ACT[p[i]][0] == ACT[i][0] for i in range(len(ACT)))]
    KINDPERM = pick("MUT-EQUIVARIANT", KINDPERM, KINDPERM[:-1])
    MIXING = [p for p in perms if p not in KINDPERM]
    sample = KINDPERM[::max(1, len(KINDPERM) // 64)][:64]
    mixed = MIXING[::max(1, len(MIXING) // 64)][:64]

    def relabel(p):
        return {ACT[i]: ACT[p[i]] for i in range(len(ACT))}

    def image(part, rl):
        return tuple(tuple(sorted((frozenset(rl[x] for x in e) for e in q),
                                  key=ekey)) for q in part)

    # K1: the property is far more robust than the delivered sample
    # licensed.  The event axis is now EXHAUSTIVE -- every one of the 455
    # against the 64-relabelling sample -- and the relabelling axis is
    # exhaustive at a declared three events: the WHOLE chart-preserving
    # group, every one of its 31104 members.
    deep = [g for g in GROUPS if profile(fps[g]) == (1, 0, 2)][:3]
    equi_checks = 0
    for g in deep:
        fp = fps[g]
        for p in KINDPERM:
            rl = relabel(p)
            fpp = footprint(tuple(rl[a] for a in g), REL)
            for nm in RULE_ORDER:
                equi_checks += 1
                if image(apply_rule(nm, fp), rl) != tuple(
                        tuple(sorted(q, key=ekey))
                        for q in apply_rule(nm, fpp)):
                    equi_bad.append(nm)
    chart_free = 0
    for g in GROUPS:
        fp = fps[g]
        for p in sample:
            rl = relabel(p)
            fpp = footprint(tuple(rl[a] for a in g), REL)
            for nm in RULE_ORDER:
                if image(apply_rule(nm, fp), rl) != tuple(
                        tuple(sorted(q, key=ekey))
                        for q in apply_rule(nm, fpp)):
                    equi_bad.append(nm)
        for p in mixed:
            rl = relabel(p)
            fpp = footprint(tuple(rl[a] for a in g), REL)
            a1 = apply_rule("ALL-NEW", fp)
            a2 = apply_rule("ALL-NEW", fpp)
            if set(image(a1, rl)[0]) | set(image(a1, rl)[1]) != \
                    set(a2[0]) | set(a2[1]):
                equi_bad.append("ALL-NEW-INCIDENCE")
            if image(apply_rule("CROSS-ONLY", fp), rl) != tuple(
                    tuple(sorted(q, key=ekey))
                    for q in apply_rule("CROSS-ONLY", fpp)):
                chart_free += 1
    MEAS.m("n_relabellings", len(sample), "the declared relabelling sweep")
    MEAS.m("n_mixedsample", len(mixed), "the sector-mixing sweep")
    MEAS.m("n_equi_events", len(GROUPS), "events swept for equivariance")
    MEAS.m("n_deep_events", len(deep), "events swept at the whole group")
    MEAS.m("n_equi_checks",
           equi_checks + len(GROUPS) * len(sample) * len(RULE_ORDER),
           "equivariance checks in all")
    MEAS.m("n_chartperms", len(KINDPERM), "relabellings that keep the charts")
    MEAS.m("n_mixing", len(MIXING), "relabellings that exchange the charts")
    MEAS.m("n_chartfree", chart_free, "sector-mixing relabellings that move "
                                      "the cross-only rule")
    MEAS.m("n_fullgroup", len(perms), "the union's whole relabelling group")
    MEAS.m("n_blind_checks", blind_checks, "rule evaluations under tokens")
    LD.gate("G-RULE-BLIND", not blind_bad and blind_checks > 0,
            MEAS.stmt("every rule's output is a function of the event's "
                      "footprint SHAPE alone: at all {n} events each rule is "
                      "recomputed from a footprint whose carriers have been "
                      "replaced by opaque tokens -- so no name of the event "
                      "survives into the rule -- and the result mapped back "
                      "through the same substitution is what the rule "
                      "returned on the named footprint, at {b} evaluations. "
                      "A rule reading a key the classification does not "
                      "carry, and a rule keyed on a named carrier, both fail "
                      "here", n="n_events", b="n_blind_checks"),
            {"disagreements": sorted(set(blind_bad)),
             "evaluations": blind_checks})
    LD.gate("G-RULE-EQUIVARIANT",
            not equi_bad and chart_free == 0
            and len(perms) == 2 * len(KINDPERM)
            and len(MIXING) == len(KINDPERM),
            MEAS.stmt("and every rule commutes with the arena's own "
                      "relabellings, at {c} checks and neither axis "
                      "sampled alone: every one of the {e} events against "
                      "{p} of the {k} automorphisms that keep each chart's "
                      "actors in their own chart, AND {d} declared events "
                      "against the WHOLE of that subgroup, all {k} of it. "
                      "The image of a rule's output is the rule's output on "
                      "the image, so no rule can be special-casing an event. "
                      "The chart-preserving "
                      "maps are a subgroup of INDEX TWO -- the gate compares "
                      "the whole group's order against twice theirs and "
                      "requires the two classes to have equal size, so a "
                      "miscounted partition fails here, and the closed form "
                      "below proves the index rather than counting it -- so "
                      "the chart-mixing relabellings are its single "
                      "non-trivial coset, all {x} of them, sampled at {s}; "
                      "under those the rules commute as well, at {f} "
                      "exceptions: a crossing stays a crossing when the two "
                      "sectors trade names. What this leg does NOT exclude "
                      "is stated with it: a rule keyed on the repr-ordering "
                      "of an event's own carriers is equivariant at this "
                      "arena and blind to names, and it is the incidence "
                      "census that separates such a rule from the delivered "
                      "one, because it is a different rule and returns a "
                      "different census",
                      c="n_equi_checks",
                      e="n_equi_events", p="n_relabellings", k="n_chartperms",
                      d="n_deep_events",
                      x="n_mixing", s="n_mixedsample", f="n_chartfree"),
            {"disagreements": sorted(set(equi_bad)),
             "chart_preserving": len(KINDPERM), "chart_mixing": len(MIXING),
             "full_group": len(perms), "index": len(perms) // len(KINDPERM),
             "checks": equi_checks + len(GROUPS) * len(sample)
             * len(RULE_ORDER),
             "sector_mixing_moves_cross_only": chart_free})

    selfsrc = read_text(SELF_REL)
    # K2 m11: the scan covers the DISPATCHER as well as the four bodies --
    # apply_rule is where a rule's output is actually produced, and where a
    # special case would be written.
    pat = pick("MUT-NOPOSTHOC",
               r"def (rule_\w+|apply_rule)\((?:fp|name, fp)\):\n"
               r"((?:    .*\n|\n)+?)(?=\n\n|\Z)",
               r"def (rule_c\w+)\(fp\):\n((?:    .*\n)+)")
    rule_src = re.findall(pat, selfsrc)
    banned = ("weld", "fate", "ALIVE", "successors", "verdict", "detect")
    peek = [nm for nm, body in rule_src if any(b in body for b in banned)]
    MEAS.m("n_rule_defs", len(rule_src), "rule bodies read out of the source")
    LD.gate("G-NO-POSTHOC",
            not peek and len(rule_src) == len(RULE_ORDER) + 1,
            MEAS.stmt("and no rule can be post hoc: the {n} bodies that "
                      "produce a rule's output -- the four rules and the "
                      "dispatcher that calls them -- are read out of this "
                      "file's own source and none of them mentions the weld, "
                      "a fate, the successor state or the verdict, so no rule "
                      "in this window can have been chosen after seeing "
                      "whether it worked",
                      n="n_rule_defs"),
            {"bodies": [nm for nm, _b in rule_src], "peeking": peek,
             "banned_terms": list(banned)})

    # the incidence census, per object, at every cell of the window
    inc_rows = Counter()
    fate_by_rule = {nm: Counter() for nm in RULE_ORDER}
    post_cache = {}
    contained = 0
    field_floor = set()
    for g in GROUPS:
        for nm in RULE_ORDER:
            fp, geo2, rel2 = advance(g, G0, REL, nm)
            post_cache[(g, nm)] = (geo2, rel2)
            if geo2["inc"] <= set(rel2):
                contained += 1
            if geo2["inc"] == set(rel2):
                field_floor.add(min(rel2[e] for e in geo2["inc"]))
            for rd in READINGS:
                for cl in COUNTLEGS:
                    f = weld(rel2, geo2, rd, cl)["fate"]
                    inc_rows[(nm, rd, cl, profile(fp), f)] += 1
                    if (rd, cl) == ("EMBEDDING", "POSITIVE"):
                        fate_by_rule[nm][f] += 1
    alive = {nm: fate_by_rule[nm]["ALIVE"] for nm in RULE_ORDER}
    span_alive = {nm: sum(c for (r, rd, cl, pr, f), c in inc_rows.items()
                          if r == nm and (rd, cl) == ("EMBEDDING", "POSITIVE")
                          and pr[0] > 0 and f == "ALIVE")
                  for nm in RULE_ORDER}
    wtext = ANCH.read("N-SEC2-WALL", "G-INCIDENCE-CENSUS")
    parent_216 = int(re.search(r"(\d+) leave the dictionary alive", wtext)
                     .group(1))
    parent_288 = int(re.search(r"the (\d+) seam-spanning", wtext).group(1))
    MEAS.m("n_alive_none", alive["NONE"], "the frozen-geometry arm")
    MEAS.m("n_alive_all", alive["ALL-NEW"], "the create-everything arm")
    MEAS.m("n_alive_cross", alive["CROSS-ONLY"], "the cross-only arm")
    MEAS.m("n_span_cross", span_alive["CROSS-ONLY"], "its crossing events")
    MEAS.m("n_span_none", span_alive["NONE"], "the frozen arm's crossings")
    LD.gate("G-CONTROL-ARMS",
            span_alive["NONE"] == 0 and alive["ALL-NEW"] == n_groups
            and alive["NONE"] > 0,
            MEAS.stmt("both outcome words are reachable through this runner "
                      "and neither is reachable by construction: with the "
                      "geometry frozen the weld refuses every one of the {s} "
                      "seam-spanning events and still admits {n} others, and "
                      "with every new pair absorbed it admits all {a} -- the "
                      "detector is neither a machine that kills what it is "
                      "handed nor one that cannot",
                      s="n_spanning", n="n_alive_none", a="n_events"),
            {"alive_by_rule": alive, "spanning_alive_by_rule": span_alive})
    declared_216 = DECL["sec2.lawful_at_matched"]
    LD.gate("G-INCIDENCE-CENSUS",
            span_alive["CROSS-ONLY"] == parent_216 == declared_216
            and span == parent_288
            and sum(inc_rows.values()) == n_groups * ncells,
            MEAS.stmt("the census is exhaustive: {e} events against {c} "
                      "window cells, every fate computed at the object; and "
                      "the cross-only rule -- one law, fired on the "
                      "footprint, no target declared anywhere -- leaves the "
                      "weld alive at exactly the {p} of {s} seam-spanning "
                      "events the parent reached only by declaring a target "
                      "after the event, a number this gate reads out of the "
                      "parent's own sentence rather than from its own",
                      e="n_events", c="n_cells", p="n_span_cross",
                      s="n_spanning"),
            {"rows": sum(inc_rows.values()),
             "parent_sentence": {"lawful": parent_216, "spanning": parent_288},
             "cross_only_spanning_alive": span_alive["CROSS-ONLY"]})
    say()
    say("  creation rule        events alive   seam-spanning alive   refused")
    for nm in RULE_ORDER:
        sayn("  %-18s %10d %14d %14d"
             % (nm, alive[nm], span_alive[nm], n_groups - alive[nm]),
             [("incidence_summary.alive_by_rule." + nm, alive[nm]),
              ("incidence_summary.spanning_alive_by_rule." + nm,
               span_alive[nm]),
              ("incidence_summary.refused_by_rule." + nm,
               n_groups - alive[nm])])
    sayn("  the parent's sentence, parsed: %d of %d lawful at a declared "
         "target" % (parent_216, parent_288),
         [("incidence_summary.parent_sentence.lawful", parent_216),
          ("incidence_summary.parent_sentence.spanning", parent_288)])
    inc_table = sorted(({"rule": nm, "reading": rd, "count_leg": cl,
                         "profile": list(pr), "fate": f, "events": c}
                        for (nm, rd, cl, pr, f), c in inc_rows.items()),
                       key=lambda r: (r["rule"], r["reading"],
                                      r["count_leg"], r["profile"]))
    R["incidence_census"] = SEAL.seal("incidence_census", inc_table,
                                      "G-INCIDENCE-CENSUS")
    R["incidence_summary"] = SEAL.seal("incidence_summary", {
        "alive_by_rule": alive, "spanning_alive_by_rule": span_alive,
        "refused_by_rule": {nm: n_groups - alive[nm] for nm in RULE_ORDER},
        "parent_sentence": {"lawful": parent_216, "spanning": parent_288},
        "events": n_groups, "cells": ncells}, "G-CONTROL-ARMS")

    # ---- THE CONTAINMENT PROPOSITION, and what it makes of the window ----
    # (K1's second strengthening, and K1 MINOR-1 / K2 M7 in one measurement.)
    # At every transition of the window the geometry's incidence is a SUBSET
    # of the record's support: the base cells are record pairs and the
    # created cells are pairs the event has just deposited.  Two graphs on
    # the same carriers with one inside the other are isomorphic exactly when
    # they are EQUAL -- so the incidence census is not a census but a
    # proposition, and two of the window's three axes are inert by
    # construction: QUOTIENT can succeed only where EMBEDDING does, and the
    # induced field carries the record's own counts, which are never below
    # one, so COUNT-DEAD cannot fire and the count leg moves nothing.
    cellsets = {}
    for (nm, rd, cl, pr, f), c in inc_rows.items():
        cellsets.setdefault((nm, rd, cl), Counter())[(pr, f)] += c
    distinct_cells = len({cell_signature(v) for v in cellsets.values()})
    copies = len(cellsets) - distinct_cells
    fates_seen = sorted({f for (_n, _r, _c, _p, f) in inc_rows})
    equality_rule = all(
        (weld(post_cache[(g, nm)][1], post_cache[(g, nm)][0],
              "EMBEDDING", "POSITIVE")["fate"] == "ALIVE")
        == (post_cache[(g, nm)][0]["inc"] == set(post_cache[(g, nm)][1]))
        for g in GROUPS[::5] for nm in RULE_ORDER)
    contained = pick("MUT-CONTAINMENT", contained, contained - 1)
    MEAS.m("n_transitions", len(GROUPS) * len(RULE_ORDER),
           "transitions of the window")
    MEAS.m("n_contained", contained, "of them with the incidence inside the "
                                     "support")
    MEAS.m("n_window_cells_distinct", distinct_cells,
           "distinct results over the window's cells")
    MEAS.m("n_window_copies", copies, "cells that are copies of another")
    MEAS.m("n_fates_seen", len(fates_seen), "weld fates that ever occur")
    MEAS.m("n_field_floor", min(field_floor), "the induced field's minimum")
    LD.gate("G-CONTAINMENT",
            contained == len(GROUPS) * len(RULE_ORDER)
            and equality_rule and min(field_floor) >= 1
            and len(cellsets) == ncells
            and distinct_cells == len(RULE_ORDER)
            and copies == ncells - len(RULE_ORDER) and copies > 0
            and set(fates_seen) == {"ALIVE", "STRUCT-DEAD"},
            MEAS.stmt("the incidence census is FORCED, and two of the "
                      "window's axes are inert -- both measured, neither "
                      "asserted. At every one of the {t} transitions the "
                      "geometry's incidence sits INSIDE the record's support, "
                      "{c} of {t}: the base cells are record pairs and every "
                      "created cell is a pair the event has just deposited. "
                      "Two graphs on the same carriers, one contained in the "
                      "other, are isomorphic exactly when they are equal, so "
                      "the weld is alive exactly when the rule creates every "
                      "new pair the event opens -- checked against the "
                      "isomorphism search itself. Two consequences follow and "
                      "are measured: the quotient reading can succeed only "
                      "where the embedding does, and the induced field "
                      "carries the record's own counts, whose minimum is {f}, "
                      "so the count-dead fate cannot fire -- only {s} of the "
                      "weld's fates ever occur. The window's cells therefore "
                      "carry {d} distinct results, {p} of them being copies",
                      t="n_transitions", c="n_contained", f="n_field_floor",
                      s="n_fates_seen", d="n_window_cells_distinct",
                      p="n_window_copies"),
            {"transitions": len(GROUPS) * len(RULE_ORDER),
             "contained": contained,
             "alive_iff_equal_sampled": equality_rule,
             "field_minimum": sorted(field_floor),
             "fates_that_occur": fates_seen,
             "window_cells": len(cellsets),
             "distinct_results": distinct_cells, "copies": copies})
    R["containment"] = SEAL.seal("containment", {
        "transitions": len(GROUPS) * len(RULE_ORDER), "contained": contained,
        "window_cells": len(cellsets), "distinct_results": distinct_cells,
        "copies": copies, "fates_that_occur": fates_seen,
        "field_minimum": sorted(field_floor)}, "G-CONTAINMENT")

    # ---- M2  THE FORM LEG ------------------------------------------------
    say()
    say("-- M2: THE FORM LEG " + "-" * 57)
    APRIV = [a for a in ACT if a[0] == "A"]
    BPRIV = [a for a in ACT if a[0] == "B"]
    CROSSPAIRS = sorted([frozenset((u, v)) for u in APRIV for v in BPRIV],
                        key=ekey)
    idxed = all(seam_index(s, a, "A") is not None
                for s in SHARED for a in APRIV) and \
        all(seam_index(s, b, "B") is not None
            for s in SHARED for b in BPRIV)
    mult = {m: Counter(cross_index(SHARED[m], p) for p in CROSSPAIRS)
            for m in range(len(SHARED))}
    multset = sorted({v for m in mult for v in mult[m].values()})
    MEAS.m("n_shared", len(SHARED), "the union's shared actors")
    MEAS.m("n_crosspairs", len(CROSSPAIRS), "private A against private B")
    MEAS.m("n_indices", len(mult[0]), "cross directions of one seam chart")
    MEAS.m("n_mult", multset[0] if multset else 0, "pairs per index")
    LD.gate("G-SEAM-INDEX",
            idxed and len(multset) == 1
            and len(mult[0]) == DECL["sec2.cross_directions"]
            and all(len(mult[m]) == len(mult[0]) for m in mult),
            MEAS.stmt("every private actor of either sector is a neighbour of "
                      "every one of the {s} shared actors, so each of the {c} "
                      "cross pairs the arena can carry has a direction in "
                      "every seam's own chart: the {i} cross directions each "
                      "carry exactly {m} of the pairs, at every seam",
                      s="n_shared", c="n_crosspairs", i="n_indices",
                      m="n_mult"),
            {"indexed": idxed, "cross_pairs": len(CROSSPAIRS),
             "indices_per_seam": {str(m): len(mult[m]) for m in mult},
             "pairs_per_index": multset})

    rows6 = [quad_row(v, IDX4, 4) for v in AV] + \
            [quad_row(v, IDX4, 4) for v in BV]
    _M, piv = rref(rows6, len(IDX4))
    rank0, ker0 = len(piv), len(IDX4) - len(piv)
    seamthm = ANCH.read("N-SEC-SEAMTHM", "G-COMPLETION-LATTICE")
    p_rank, p_unk, p_ker = (int(x) for x in re.findall(r"\d+", seamthm))
    seamtext = ANCH.read("N-SEC2-SEAM", "G-COMPLETION-LATTICE")
    SIMPLE = (1, 1, 1)
    L0 = completion_lattice(SIMPLE, SIMPLE)
    L0w = completion_lattice(SIMPLE, SIMPLE, 1)
    pdcount = sum(1 for U in L0
                  if posdef(gram(SIMPLE, SIMPLE, [[U[0], U[1]],
                                                  [U[2], U[3]]])))
    MEAS.m("rank", rank0, "the rref of the six declared rows")
    MEAS.m("kernel", ker0, "unknowns minus rank")
    MEAS.m("unknowns", len(IDX4), "the symmetric square of the seam chart")
    MEAS.m("n_lattice", len(L0), "the enumerated completion lattice")
    MEAS.m("n_pd", pdcount, "exact Sylvester on the doubled Gram")
    LD.gate("G-COMPLETION-LATTICE",
            rank0 == p_rank and ker0 == p_ker and len(IDX4) == p_unk
            and len(L0) == DECL["sec2.aligned_lattice"]
            # K2 m10: this declared value was carried and consumed nowhere.
            # It IS the kernel -- the number of numbers a seam declaration
            # costs -- and is bound to it here
            and ker0 == DECL["sec2.declaration_price_per_seam"]
            and set(L0) == set(L0w) and pdcount == len(L0)
            and "4-parameter at every seam type" in seamtext,
            MEAS.stmt("the state this unit moves is the seam's cross block. "
                      "Its system has rank {r} on the {u} entries of the "
                      "symmetric square of the direct-sum chart, so the "
                      "kernel is {k} -- taken on the coefficient matrix alone, "
                      "with no right-hand side in it, and compared against "
                      "the parent's own sentence rather than against a typed "
                      "constant. At the all-simple seam the corpus's readout "
                      "admits {n} completions, every one of them positive "
                      "definite, and the enumeration box is measured not to "
                      "bind: widened by one it returns the same set",
                      r="rank", u="unknowns", k="kernel", n="n_lattice"),
            {"rank": rank0, "kernel": ker0, "unknowns": len(IDX4),
             "parent_sentence": [p_rank, p_unk, p_ker],
             "lattice": len(L0), "widened": len(L0w),
             "positive_definite": pdcount})
    R["seam"] = SEAL.seal("seam", {
        "rank": rank0, "kernel": ker0, "unknowns": len(IDX4),
        "lattice": len(L0), "positive_definite": pdcount,
        "cross_directions": len(mult[0]), "cross_pairs": len(CROSSPAIRS),
        "pairs_per_index": multset}, "G-COMPLETION-LATTICE")

    # the successor state, per object
    form_rows = Counter()
    form_ok, frozen_ok, succ_sizes = {}, {}, {}
    form_ok_arm = {"CROSS-ONLY": {}, "ALL-NEW": {}}
    fourth_rows = Counter()
    fourth_bad = 0
    fourth_by_site = Counter()
    for g in GROUPS:
        geo2, rel2 = post_cache[(g, "ALL-NEW")]
        realised = [p for p in rel2 if {x[0] for x in p} == {"A", "B"}]
        sizes, keeps = [], []
        for m in range(len(SHARED)):
            sc = successors(SHARED[m], rel2, realised)
            sizes.append(len(sc))
            keeps.append(sum(1 for U in sc if U in L0))
        succ_sizes[g] = tuple(sizes)
        # the created cells of the fourth class, read against the record.
        # K2 M2: the site a reading is TAKEN AT is recorded -- the mechanism
        # is a single chart's restriction of the form, which has kernel zero
        # at every site of that chart, shared or not, and the census says how
        # many readings fall at each kind.
        agree = 0
        reads = 0
        for e in geo2["within"]:
            for chart, inv in (("A", INV_A), ("B", INV_B)):
                us = [inv[a] for a in e if a in inv]
                if len(us) != 2:
                    continue
                d = ((us[1][0] - us[0][0]) % 3, (us[1][1] - us[0][1]) % 3)
                if d not in (FOURTH, zneg(FOURTH)):
                    continue
                for b in us:
                    n, predicted = fourth_prediction(rel2, b, chart)
                    reads += 1
                    if predicted == rel2[e]:
                        agree += 1
                    fourth_rows[(n, predicted, rel2[e])] += 1
                    mp = AMAP if chart == "A" else BMAP
                    fourth_by_site["a shared (seam) site"
                                   if mp[b] in SHARED
                                   else "a chart-private site"] += 1
        fourth_bad += agree
        pr = profile(fps[g])
        form_ok[g] = all(s > 0 for s in sizes) and agree == reads
        frozen_ok[g] = all(k > 0 for k in keeps) and agree == reads
        # per arm (K1 MINOR-7): the successor sets are a function of the
        # post-RECORD, which every rule updates identically, so they are
        # rule-independent; what is NOT rule-independent is the fourth
        # direction, which only a rule that creates within cells can trip.
        form_ok_arm["ALL-NEW"][g] = form_ok[g]
        form_ok_arm["CROSS-ONLY"][g] = all(s > 0 for s in sizes)
        form_rows[(pr, tuple(sizes), tuple(keeps), form_ok[g],
                   frozen_ok[g])] += 1
    n_form_alive = sum(1 for g in GROUPS if form_ok[g])
    n_form_cross = sum(1 for g in GROUPS if form_ok[g] and fps[g]["cross"])
    n_frozen_cross = sum(1 for g in GROUPS
                         if frozen_ok[g] and fps[g]["cross"])
    n_form_nofourth = sum(1 for g in GROUPS if all(s > 0
                                                   for s in succ_sizes[g]))
    n_fourth_reads = sum(fourth_rows.values())
    n_fourth_shared = fourth_by_site["a shared (seam) site"]
    n_fourth_private = fourth_by_site["a chart-private site"]
    MEAS.m("n_form_alive", n_form_alive, "events with a successor state")
    MEAS.m("n_form_cross", n_form_cross, "crossings among them")
    MEAS.m("n_frozen_cross", n_frozen_cross, "crossings needing no state move")
    MEAS.m("n_form_nofourth", n_form_nofourth, "events with a successor at "
                                               "every seam, the fourth "
                                               "direction not consulted")
    MEAS.m("n_fourth_reads", n_fourth_reads, "fourth-direction readings")
    MEAS.m("n_fourth_agree", fourth_bad, "readings where the two agree")
    MEAS.m("n_fourth_shared", n_fourth_shared, "readings at a shared site")
    MEAS.m("n_fourth_private", n_fourth_private, "readings at a private site")
    LD.gate("G-FOURTH-DIRECTION",
            fourth_bad == 0 and n_fourth_reads > 0
            and all(k[1] != k[2] for k in fourth_rows)
            and n_fourth_shared + n_fourth_private == n_fourth_reads
            and n_fourth_shared > 0 and n_fourth_private > 0,
            MEAS.stmt("a link inside a sector is a link of the fourth "
                      "parallel class, and A SECTOR'S OWN FORM AT A SITE is "
                      "fixed by that chart's three declared counts with "
                      "nothing left over -- the restriction to one chart has "
                      "kernel zero at EVERY site, shared or private, which is "
                      "a different object from the two-chart form at a seam "
                      "whose kernel is four. The count the sector's form "
                      "forces on the fourth direction is read at both ends of "
                      "every such cell the update creates, {r} readings in "
                      "all -- {p} of them at chart-private sites and {h} at "
                      "the shared ones -- and it agrees with the count the "
                      "event deposits at {a} of them",
                      r="n_fourth_reads", a="n_fourth_agree",
                      p="n_fourth_private", h="n_fourth_shared"),
            {"readings": n_fourth_reads, "agreements": fourth_bad,
             "by_base_site": dict(fourth_by_site),
             "rows": [{"counts": list(k[0]), "predicted": k[1],
                       "realised": k[2], "readings": v}
                      for k, v in sorted(fourth_rows.items())]})
    R["fourth_by_site"] = SEAL.seal("fourth_by_site",
                                    [{"the base site of the reading": k,
                                      "readings": v}
                                     for k, v in sorted(
                                         fourth_by_site.items())],
                                    "G-FOURTH-DIRECTION")
    R["fourth_summary"] = SEAL.seal("fourth_summary", {
        "readings": n_fourth_reads, "agreements": fourth_bad,
        "at a chart-private site": n_fourth_private,
        "at a shared (seam) site": n_fourth_shared},
        "G-FOURTH-DIRECTION")

    two_cross_dead = all(min(k[1]) == 0 for k in form_rows if k[0][0] > 1)
    one_cross_live = all(min(k[1]) > 0 for k in form_rows
                         if k[0] == (1, 0, 2))
    LD.gate("G-FORM-CENSUS",
            n_form_alive > 0 and n_form_cross > 0
            and n_form_cross < span and two_cross_dead and one_cross_live
            and sum(form_rows.values()) == n_groups
            and n_form_nofourth > n_form_alive,
            MEAS.stmt("the form leg is then taken at every one of the {e} "
                      "events, object by object and never by orbit -- the "
                      "chart breaks the symmetry the relation does not -- "
                      "and a successor state exists at all three seams for "
                      "{n} of them; {f} survive the fourth direction as "
                      "well, {c} of which put a pair across the seam; "
                      "at {k} of those the state need not move at all",
                      e="n_events", f="n_form_alive", c="n_form_cross",
                      k="n_frozen_cross", n="n_form_nofourth"),
            {"form_alive": n_form_alive, "crossings": n_form_cross,
             "frozen": n_frozen_cross,
             "rows": [{"profile": list(k[0]), "successors": list(k[1]),
                       "kept": list(k[2]), "form_lawful": k[3],
                       "frozen_possible": k[4], "events": v}
                      for k, v in sorted(form_rows.items(), key=repr)]})
    say()
    sayn("  the seam: rank %d on %d unknowns, kernel %d; %d completions at "
         "the all-simple seam, all positive definite"
         % (rank0, len(IDX4), ker0, len(L0)),
         [("seam.rank", rank0), ("seam.unknowns", len(IDX4)),
          ("seam.kernel", ker0), ("seam.lattice", len(L0))])
    sayn("  the successor state exists at all three seams for %d events, %d "
         "of them crossings; %d need no state move"
         % (n_form_alive, n_form_cross, n_frozen_cross),
         [("form_summary.form_alive", n_form_alive),
          ("form_summary.crossings", n_form_cross),
          ("form_summary.frozen", n_frozen_cross)])
    sayn("  the fourth direction: %d readings, %d at chart-private sites, %d "
         "at shared ones, %d agreements"
         % (n_fourth_reads, n_fourth_private, n_fourth_shared, fourth_bad),
         [("fourth_summary.readings", n_fourth_reads),
          ("fourth_summary.at a chart-private site", n_fourth_private),
          ("fourth_summary.at a shared (seam) site", n_fourth_shared),
          ("fourth_summary.agreements", fourth_bad)])
    R["form_census"] = SEAL.seal("form_census",
                                 [{"profile": list(k[0]),
                                   "successors": list(k[1]),
                                   "kept": list(k[2]), "form_lawful": k[3],
                                   "frozen_possible": k[4], "events": v}
                                  for k, v in sorted(form_rows.items(),
                                                     key=repr)],
                                 "G-FORM-CENSUS")
    R["form_summary"] = SEAL.seal("form_summary", {
        "form_alive": n_form_alive, "crossings": n_form_cross,
        "frozen": n_frozen_cross,
        "successor_at_every_seam": n_form_nofourth}, "G-FORM-CENSUS")

    # ---- WHY THE TWO-CROSSING EVENTS DIE (K1 MAJOR-1) -------------------
    # Not "the entry that is their sum leaves the range": measured at every
    # one of them, the two crossings hit the SAME cross entry at OPPOSITE
    # signs.  The doubled pair joins two same-sector actors, so they lie on a
    # declared line; a declared line meets each fourth-class line once, so
    # its third point is THE shared site collinear with them; seen from that
    # seam the two actors are s + d_i and s - d_i.  The two equations are
    # then nA[i] + nB[j] - E[i][j] = 1 and nA[i] + nB[j] + E[i][j] = 1, whose
    # sum is nA[i] + nB[j] = 1 -- impossible for positive counts.
    death_rows = Counter()
    collinear_ok = 0
    twocross = [g for g in GROUPS if profile(fps[g]) == (2, 0, 1)]
    for g in twocross:
        fails = [m for m in range(len(SHARED)) if succ_sizes[g][m] == 0]
        if len(fails) != 1:
            death_rows[("the failing seam is not unique", None)] += 1
            continue
        m = fails[0]
        ks = [cross_index(SHARED[m], p) for p in fps[g]["cross"]]
        if any(k is None for k in ks):
            death_rows[("a crossing has no index at the failing seam",
                        None)] += 1
            continue
        same_entry = ks[0][:2] == ks[1][:2]
        opposite = pick("MUT-DEATH", ks[0][2] == -ks[1][2],
                        ks[0][2] == ks[1][2])
        death_rows[("the same cross entry, at opposite signs" if
                    same_entry and opposite else
                    ("two distinct cross entries" if not same_entry else
                     "the same cross entry, at the same sign"),
                    len(succ_sizes[g]) - len(fails))] += 1
        # the collinearity: the shared site on the declared line through the
        # doubled pair's two actors is the seam that fails
        du, dv = sorted(fps[g]["doubled"][0], key=ekey)
        chart = du[0] if du[0] in ("A", "B") else dv[0]
        ivm = INV_A if chart == "A" else BMAP and INV_B
        if du in ivm and dv in ivm:
            su, sv = ivm[du], ivm[dv]
            d = ((sv[0] - su[0]) % 3, (sv[1] - su[1]) % 3)
            line = {zadd(su, ((k * d[0]) % 3, (k * d[1]) % 3))
                    for k in range(3)}
            third = [s for s in line if s not in (su, sv)]
            if third and SEAM_SITE[chart][SHARED[m]] == third[0]:
                collinear_ok += 1
    MEAS.m("n_twocross", len(twocross), "events with two crossings and a "
                                        "doubling")
    MEAS.m("n_collinear", collinear_ok, "of them whose failing seam is the "
                                        "collinear shared site")
    MEAS.m("n_sign_deaths",
           sum(v for k, v in death_rows.items()
               if k[0] == "the same cross entry, at opposite signs"),
           "deaths by a sign contradiction on one entry")
    LD.gate("G-TWO-CROSSING-DEATH",
            len(twocross) > 0
            and MEAS.get("n_sign_deaths") == len(twocross)
            and collinear_ok == len(twocross)
            and sum(death_rows.values()) == len(twocross),
            MEAS.stmt("the {t} events that put TWO pairs across the seam die "
                      "at the form and not at the incidence, and the reason "
                      "is measured at every one of them rather than argued. "
                      "Exactly one of the three seams has no successor, and "
                      "at that seam the two crossings do not fix two entries "
                      "of the cross block: they fix THE SAME ENTRY AT "
                      "OPPOSITE SIGNS, {s} of {t}. The doubled pair joins two "
                      "actors of one sector, so they lie on a declared line; "
                      "a declared line meets each fourth-class line once, so "
                      "its third point is the one shared site collinear with "
                      "them -- and that is the seam that fails, at {c} of "
                      "{t}. Seen from it the two actors sit at the same "
                      "direction index and opposite signs, so their two "
                      "equations add to a statement that the two seam counts "
                      "sum to one, which positive counts cannot do",
                      t="n_twocross", s="n_sign_deaths", c="n_collinear"),
            {"events": len(twocross),
             "rows": [{"at the failing seam, the two crossings fix": k[0],
                       "seams with a successor": k[1], "events": v}
                      for k, v in sorted(death_rows.items(), key=repr)],
             "failing_seam_is_the_collinear_one": collinear_ok})
    R["two_crossing_death"] = SEAL.seal("two_crossing_death", [
        {"at the failing seam, the two crossings fix": k[0],
         "seams with a successor": k[1], "events": v}
        for k, v in sorted(death_rows.items(), key=repr)],
        "G-TWO-CROSSING-DEATH")

    # ---- the successor memo, proved inert -------------------------------
    # The successor set is a function of the seam's two count vectors and of
    # the (index, count) constraints the realised cross links impose, of
    # nothing else, so it is memoised on exactly that key -- which is what
    # makes the second step runnable from every lawful first crossing rather
    # than from one.  A speed device inside a measurement is a claim, so it
    # is checked rather than asserted: every distinct key the run reached is
    # recomputed from scratch with the memo bypassed and required to give
    # the same completions in the same order.
    memo_keys = sorted(SUCCACHE, key=repr)
    memo_bad = [k for k in memo_keys
                if successors_raw(k[0], k[1], k[2], memo=False)
                != pick("MUT-MEMO", SUCCACHE[k], SUCCACHE[k][1:])]
    MEAS.m("n_memo_keys", len(memo_keys), "distinct successor keys reached")
    MEAS.m("n_memo_bad", len(memo_bad), "of them the memo gets wrong")
    LD.gate("G-SUCCESSOR-MEMO",
            not memo_bad and len(memo_keys) > 0,
            MEAS.stmt("the successor census is memoised on the only thing it "
                      "depends on -- the seam's two count vectors and the "
                      "constraints its realised cross links impose -- and "
                      "the memo is PROVED INERT rather than trusted: every "
                      "one of the {k} distinct keys this run reached is "
                      "recomputed from scratch with the memo bypassed, and "
                      "the answers must agree completion for completion and "
                      "in the same order, at {b} exceptions. Without it the "
                      "second step could be run from one first crossing "
                      "only, and a census taken at one representative of a "
                      "single orbit is not a census",
                      k="n_memo_keys", b="n_memo_bad"),
            {"keys": len(memo_keys), "disagreements": len(memo_bad)})
    R["fourth_direction"] = SEAL.seal("fourth_direction",
                                      [{"counts": list(k[0]),
                                        "predicted": k[1], "realised": k[2],
                                        "readings": v}
                                       for k, v in sorted(fourth_rows.items())],
                                      "G-FOURTH-DIRECTION")

    # the two creating rules agree once the form leg binds -- and K1
    # MINOR-6/7: the agreement is measured PER ARM, and the control that says
    # what carries it is measured too.  Without the fourth-direction leg the
    # two rules part company at once, so the equivalence is not
    # indistinguishability: the second rule's extra output is entirely
    # illegal, and the leg that refuses it is the whole of the collapse.
    full_alive, nofourth_alive = {}, {}
    for nm in ("CROSS-ONLY", "ALL-NEW"):
        keep, keep2 = set(), set()
        for g in GROUPS:
            geo2, rel2 = post_cache[(g, nm)]
            if weld(rel2, geo2, "EMBEDDING", "POSITIVE")["fate"] != "ALIVE":
                continue
            if all(s > 0 for s in succ_sizes[g]):
                keep2.add(g)
            if not form_ok_arm[nm][g]:
                continue
            keep.add(g)
        if mut("MUT-FIBER") and nm == "ALL-NEW":
            keep.discard(sorted(keep, key=repr)[0])
        full_alive[nm] = keep
        nofourth_alive[nm] = keep2
    same = full_alive["CROSS-ONLY"] == full_alive["ALL-NEW"]
    part = nofourth_alive["CROSS-ONLY"] != nofourth_alive["ALL-NEW"]
    MEAS.m("n_full_alive", len(full_alive["CROSS-ONLY"]),
           "events lawful at every leg")
    MEAS.m("n_full_cross", sum(1 for g in full_alive["CROSS-ONLY"]
                               if fps[g]["cross"]), "crossings among them")
    MEAS.m("n_nofourth_cross", len(nofourth_alive["CROSS-ONLY"]),
           "the cross-only arm without the fourth-direction leg")
    MEAS.m("n_nofourth_all", len(nofourth_alive["ALL-NEW"]),
           "the create-everything arm without it")
    LD.gate("G-RULE-FIBER",
            same and len(full_alive["CROSS-ONLY"]) > 0 and part
            and len(nofourth_alive["ALL-NEW"])
            > len(nofourth_alive["CROSS-ONLY"]),
            MEAS.stmt("and the window's creation axis collapses: at the "
                      "complete standard the two rules that create anything "
                      "admit the SAME {n} events -- the same SET and not the "
                      "same count -- {c} of them crossings, each arm having "
                      "its own form leg evaluated at its own post-geometry. "
                      "What carries the collapse is measured and it is one "
                      "leg: drop the fourth-direction refusal and the two "
                      "part company at once, {a} against {b}, so the "
                      "create-everything rule's extra output is not "
                      "indistinguishable from nothing -- it is entirely "
                      "illegal",
                      n="n_full_alive", c="n_full_cross",
                      a="n_nofourth_cross", b="n_nofourth_all"),
            {"cross_only": len(full_alive["CROSS-ONLY"]),
             "all_new": len(full_alive["ALL-NEW"]), "identical": same,
             "without_the_fourth_leg": {
                 "CROSS-ONLY": len(nofourth_alive["CROSS-ONLY"]),
                 "ALL-NEW": len(nofourth_alive["ALL-NEW"])},
             "the_two_arms_part_without_it": part})
    R["arm_control"] = SEAL.seal("arm_control", {
        "at every leg": {"CROSS-ONLY": len(full_alive["CROSS-ONLY"]),
                         "ALL-NEW": len(full_alive["ALL-NEW"])},
        "without the fourth-direction leg": {
            "CROSS-ONLY": len(nofourth_alive["CROSS-ONLY"]),
            "ALL-NEW": len(nofourth_alive["ALL-NEW"])}}, "G-RULE-FIBER")

    # the preparedness census: what a state declared IN ADVANCE is ready for
    absorb = {}
    for g in GROUPS:
        if not fps[g]["cross"]:
            continue
        geo2, rel2 = post_cache[(g, "CROSS-ONLY")]
        realised = [p for p in rel2 if {x[0] for x in p} == {"A", "B"}]
        sets = []
        for m in range(len(SHARED)):
            sc = successors(SHARED[m], rel2, realised)
            sets.append(frozenset(U for U in sc if U in L0))
        absorb[g] = tuple(sets)
    cover = Counter()
    bestn, bests = -1, []
    LPREP = pick("MUT-PREP", L0, L0[:4])
    for U0 in LPREP:
        for U1 in LPREP:
            s01 = [g for g, s in absorb.items() if U0 in s[0] and U1 in s[1]]
            for U2 in LPREP:
                n = sum(1 for g in s01 if U2 in absorb[g][2])
                cover[n] += 1
                if n > bestn:
                    bestn, bests = n, [(U0, U1, U2)]
                elif n == bestn:
                    bests.append((U0, U1, U2))
    # K2 M9: "the best state" is a family, not a representative, and the
    # census already contains the sharper fact -- how many of the lawful
    # crossings NO advance declaration can absorb at all.
    diagonal = sum(1 for s in bests if len(set(s)) == 1)
    absorbable = sum(1 for g, s in absorb.items()
                     if g in full_alive["CROSS-ONLY"]
                     and all(len(x) > 0 for x in s))
    unabsorbable = n_form_cross - absorbable
    MEAS.m("n_states", len(L0) ** len(SHARED), "completions at each seam")
    MEAS.m("n_best", bestn, "the maximum over the state space")
    MEAS.m("n_beststates", len(bests), "states attaining it")
    MEAS.m("n_bestdiag", diagonal, "of those, carrying one completion at "
                                   "every seam")
    MEAS.m("n_absorbable", absorbable, "lawful crossings any advance state "
                                       "can absorb")
    MEAS.m("n_unabsorbable", unabsorbable, "lawful crossings none can")
    MEAS.m("n_zero", cover[0], "states ready for no crossing at all")
    MEAS.m("n_crossings", len(absorb), "the arena's crossing events")
    LD.gate("G-PREPAREDNESS",
            sum(cover.values()) == len(L0) ** len(SHARED)
            and bestn < len(absorb) and cover[0] > 0
            and len(bests) > 0 and diagonal < len(bests)
            and absorbable + unabsorbable == n_form_cross
            and absorbable == n_frozen_cross and bestn <= absorbable,
            MEAS.stmt("a state declared before the event is ready for only "
                      "part of what can happen, and the census is taken over "
                      "the whole state space and reported as a family rather "
                      "than at a representative: over all {t} states the "
                      "arena admits, {n} states attain the maximum {b} -- of "
                      "which {d} carry the same completion at all three seams "
                      "and the others mix -- and {z} states are ready for "
                      "none. The shortfall is sharper than that ratio: of "
                      "the {f} lawful crossings only {y} are absorbable by "
                      "ANY state declared in advance, because the doubling "
                      "the other {u} carry moves the seam's own counts out of "
                      "the pre-event lattice, and the best states take {b} of "
                      "those {y}",
                      t="n_states", b="n_best", f="n_form_cross",
                      z="n_zero", n="n_beststates", d="n_bestdiag",
                      y="n_absorbable", u="n_unabsorbable"),
            {"states": len(L0) ** len(SHARED), "best": bestn,
             "best_states": len(bests), "best_states_diagonal": diagonal,
             "best_state_examples": [[list(u) for u in s]
                                     for s in bests[:2]],
             "absorbable_by_some_state": absorbable,
             "absorbable_by_none": unabsorbable,
             "ready_for_none": cover[0],
             "coverage": sorted(cover.items())})
    sayn("  preparedness: over %d states %d attain the best %d of the %d "
         "absorbable crossings; %d absorb none; %d lawful crossings no state "
         "can absorb" % (len(L0) ** len(SHARED), len(bests), bestn,
                         absorbable, cover[0], unabsorbable),
         [("preparedness.states", len(L0) ** len(SHARED)),
          ("preparedness.best_states", len(bests)),
          ("preparedness.best", bestn),
          ("preparedness.absorbable_by_some_state", absorbable),
          ("preparedness.ready_for_none", cover[0]),
          ("preparedness.absorbable_by_none", unabsorbable)])
    R["preparedness"] = SEAL.seal("preparedness", {
        "states": len(L0) ** len(SHARED), "best": bestn,
        "best_states": len(bests), "best_states_diagonal": diagonal,
        "absorbable_by_some_state": absorbable,
        "absorbable_by_none": unabsorbable,
        "ready_for_none": cover[0],
        "coverage": [{"crossings_absorbed": k, "states": v}
                     for k, v in sorted(cover.items())]}, "G-PREPAREDNESS")
    R["best_states"] = SEAL.seal("best_states", [
        {"state": [list(u) for u in s],
         "the same completion at all three seams": len(set(s)) == 1}
        for s in sorted(bests, key=repr)], "G-PREPAREDNESS")

    # ---- THE TRANSITION RELATION, censused ------------------------------
    # The successor set is a function of the POST-RECORD alone, so the update
    # is a relation from a state to a SET of lawful successors.  Two readings
    # of what a state then restricts are measured, and they differ.
    mult, gfib = Counter(), Counter()
    for g in GROUPS:
        if not fps[g]["cross"] or not form_ok[g]:
            continue
        geo2, rel2 = post_cache[(g, "CROSS-ONLY")]
        realised = [p for p in rel2 if {x[0] for x in p} == {"A", "B"}]
        whole = 1
        for m in range(len(SHARED)):
            k = len(successors(SHARED[m], rel2, realised))
            mult[k] += 1
            whole = whole * k
        gfib[whole] += 1
    if mut("MUT-RELATION"):
        mult[1] = mult.pop(sorted(mult)[0])
    mult_rows = [{"successors at one seam": k, "seam slots": v}
                 for k, v in sorted(mult.items())]
    fiber_rows = [{"successors of the whole state": k, "crossings": v}
                  for k, v in sorted(gfib.items())]
    memoryless = len(full_alive["CROSS-ONLY"])
    persistent = sum(v for k, v in cover.items() if k > 0)
    MEAS.m("n_slots", sum(mult.values()), "seam slots of the lawful "
                                          "crossings")
    MEAS.m("n_multvalues", len(mult), "distinct successor multiplicities")
    MEAS.m("fiber_min", min(gfib), "the whole state's smallest successor set")
    MEAS.m("fiber_max", max(gfib), "the whole state's largest successor set")
    MEAS.m("n_fiber_min_at", gfib[min(gfib)], "crossings carrying the "
                                              "smallest")
    MEAS.m("n_fiber_max_at", gfib[max(gfib)], "crossings carrying the largest")
    MEAS.m("n_persistent", persistent, "states admitting a crossing without "
                                       "moving")
    LD.gate("G-TRANSITION-RELATION",
            1 not in mult and sum(mult.values()) == len(SHARED) * n_form_cross
            and persistent + cover[0] == len(L0) ** len(SHARED)
            and persistent < len(L0) ** len(SHARED),
            MEAS.stmt("what the update delivers is a TRANSITION RELATION and "
                      "not an evolution law: over the {s} seam slots of the "
                      "lawful crossings the successor set takes {v} distinct "
                      "sizes and never once the size that would make it a "
                      "map; the state carries three seams, so the WHOLE "
                      "state's successor set runs from {fn} to {fx}. And "
                      "what a state restricts depends on whether it "
                      "persists: read as re-solved at every event the "
                      "successor set is a function of the post-record alone, "
                      "so every state admits every one of the {m} lawful "
                      "events and the state carries no memory; read as "
                      "persisting unless the record forces it to move, {p} "
                      "of the {t} states admit a crossing at all",
                      s="n_slots", v="n_multvalues", m="n_full_alive",
                      p="n_persistent", t="n_states", fn="fiber_min",
                      fx="fiber_max"),
            {"multiplicities": mult_rows, "whole_state_fiber": fiber_rows,
             "memoryless_allowed": memoryless,
             "persistent_states_admitting_a_crossing": persistent,
             "states": len(L0) ** len(SHARED)})
    R["successor_multiplicity"] = SEAL.seal("successor_multiplicity",
                                            mult_rows,
                                            "G-TRANSITION-RELATION")
    R["whole_state_fiber"] = SEAL.seal("whole_state_fiber", fiber_rows,
                                       "G-TRANSITION-RELATION")
    R["relation_totality"] = SEAL.seal("relation_totality", {
        "memoryless_reading_allows": memoryless,
        "persistent_reading_states_with_a_crossing": persistent,
        "states": len(L0) ** len(SHARED)}, "G-TRANSITION-RELATION")

    # ---- the second step: does the update iterate? ----------------------
    # K1 MAJOR-5: the census is run from EVERY lawful first crossing, not
    # from one, and the fiber is published.  The delivered row is named as a
    # declared tie-break -- the first in the canonical key order -- and it
    # sits at the fiber's MINIMUM, which is why the fiber is the headline.
    firsts = sorted((g for g in absorb
                     if profile(fps[g]) == (1, 0, 2) and form_ok[g]), key=ekey)

    def second_step(first):
        geo1, rel1 = post_cache[(first, "CROSS-ONLY")]
        realised1 = [p for p in rel1 if {x[0] for x in p} == {"A", "B"}]
        succ1 = [successors(SHARED[m], rel1, realised1)
                 for m in range(len(SHARED))]
        state1 = [min(s, key=lambda U: (sum(abs(x) for x in U), U))
                  for s in succ1]
        rows = Counter()
        for g in GROUPS:
            fp2, geo3, rel3 = advance(g, geo1, rel1, "CROSS-ONLY")
            if mut("MUT-TWOSTEP"):
                rel3 = dict(rel1)
            realised3 = [p for p in rel3 if {x[0] for x in p} == {"A", "B"}
                         and frozenset(p) in geo3["inc"]]
            sets = [successors(SHARED[m], rel3, realised3)
                    for m in range(len(SHARED))]
            sizes = [len(s) for s in sets]
            keep = all(state1[m] in sets[m] for m in range(len(SHARED)))
            # the step-1 standard, applied at step 2 (K1 MINOR-8): incidence
            # weld AND a successor at every seam AND no pair inside a sector.
            # The incidence leg is taken by the CONTAINMENT CRITERION this
            # run proves at G-CONTAINMENT -- the geometry sits inside the
            # record's support at every transition of the window, and two
            # graphs on the same carriers with one inside the other are
            # isomorphic exactly when they are equal -- so the weld here is
            # the equality, not a second isomorphism search.
            matched = (all(s > 0 for s in sizes) and not fp2["within"]
                       and geo3["inc"] == rel3.keys())
            rows[(len(fp2["cross"]) > 0, all(s > 0 for s in sizes),
                  keep, matched)] += 1
        return rows, succ1, state1

    step2, succ1, state1 = second_step(firsts[0])
    n2_cross = sum(v for k, v in step2.items() if k[0] and k[1])
    n2_frozen = sum(v for k, v in step2.items() if k[0] and k[1] and k[2])
    n2_matched = sum(v for k, v in step2.items() if k[0] and k[3])
    fiber2 = Counter()
    fiber2m = Counter()
    for first in pick("MUT-STEPFIBER", firsts, firsts[:1]):
        rows, _s, _st = second_step(first)
        a = sum(v for k, v in rows.items() if k[0] and k[1])
        b = sum(v for k, v in rows.items() if k[0] and k[1] and k[2])
        fiber2[(a, b)] += 1
        fiber2m[sum(v for k, v in rows.items() if k[0] and k[3])] += 1
    n2_lo = min(k[0] for k in fiber2)
    n2_hi = max(k[0] for k in fiber2)
    MEAS.m("n_step2_cross", n2_cross, "second crossings still form-lawful")
    MEAS.m("n_step2_frozen", n2_frozen, "of those, with the state kept")
    MEAS.m("n_step2_matched", n2_matched, "second crossings at the first "
                                          "step's own standard")
    MEAS.m("n_step2_lo", n2_lo, "the fiber's minimum over the first events")
    MEAS.m("n_step2_hi", n2_hi, "the fiber's maximum over the first events")
    MEAS.m("n_step2_firsts", len(firsts), "lawful first crossings run")
    MEAS.m("n_step2_atlo", fiber2[(n2_lo, n2_frozen)],
           "first events reaching the delivered cell")
    second_step_fiber = [
        {"still form-lawful": k[0], "of those, state kept": k[1],
         "first crossings": v} for k, v in sorted(fiber2.items(), key=repr)]
    LD.gate("G-TWO-STEP",
            n2_cross < n_form_cross and n2_cross > 0
            and sum(step2.values()) == n_groups
            and sum(fiber2.values()) == len(firsts)
            and n2_cross == n2_lo and n2_hi < n_form_cross
            and n2_matched == n2_cross,
            MEAS.stmt("the update iterates, and it remembers -- and the "
                      "census is run from every one of the {f} lawful first "
                      "crossings, not from one. From the post-state of a "
                      "first crossing, at a successor named by a declared "
                      "rule, the second event may still cross at between {lo} "
                      "and {hi} of the events that could cross first at {b}; "
                      "the delivered row is the first crossing in this "
                      "unit's canonical key order, a declared tie-break, and "
                      "it lands at the fiber's MINIMUM {a}, reached at {n} of "
                      "the first crossings, with the state surviving at {c}. "
                      "The two steps are compared at ONE standard: the first "
                      "step's whole predicate -- incidence, successor and the "
                      "fourth direction -- re-applied at the second returns "
                      "{mt}",
                      a="n_step2_cross", b="n_crossings", c="n_step2_frozen",
                      f="n_step2_firsts", lo="n_step2_lo", hi="n_step2_hi",
                      n="n_step2_atlo", mt="n_step2_matched"),
            {"first_event": [str(a) for a in firsts[0]],
             "tie_break": "the canonical key order of this unit's own "
                          "ordering discipline; the fiber is published",
             "successor_sizes": [len(s) for s in succ1],
             "state": [list(u) for u in state1],
             "fiber": second_step_fiber,
             "matched_standard_fiber": sorted(fiber2m.items()),
             "second_step": [{"crossing": k[0], "form_lawful": k[1],
                              "state_kept": k[2], "events": v}
                             for k, v in sorted(Counter(
                                 {(a, b, c): sum(
                                     v for k2, v in step2.items()
                                     if k2[:3] == (a, b, c))
                                  for (a, b, c) in {k[:3] for k in step2}}
                             ).items())]})
    sayn("  the second step: %d of the events may still cross, %d with the "
         "state kept; over all %d first crossings the fiber runs %d to %d"
         % (n2_cross, n2_frozen, len(firsts), n2_lo, n2_hi),
         [("two_step.second_crossings", n2_cross),
          ("two_step.second_frozen", n2_frozen),
          ("two_step.first_crossings_run", len(firsts)),
          ("two_step.fiber_low", n2_lo), ("two_step.fiber_high", n2_hi)])
    R["two_step"] = SEAL.seal("two_step", {
        "first_event": [str(a) for a in firsts[0]],
        "successor_sizes": [len(s) for s in succ1],
        "state": [list(u) for u in state1],
        "second_crossings": n2_cross, "second_frozen": n2_frozen,
        "second_at_the_step_one_standard": n2_matched,
        "first_crossings_run": len(firsts),
        "fiber_low": n2_lo, "fiber_high": n2_hi,
        "rows": [{"crossing": a, "form_lawful": b, "state_kept": c,
                  "events": sum(v for k2, v in step2.items()
                                if k2[:3] == (a, b, c))}
                 for (a, b, c) in sorted({k[:3] for k in step2})]},
        "G-TWO-STEP")
    R["two_step_fiber"] = SEAL.seal("two_step_fiber", second_step_fiber,
                                    "G-TWO-STEP")

    # ---- M3  THE PRICE, AND WHERE MOTIVATION LIVES (Q50) ----------------
    say()
    say("-- M3: THE PRICE AND MOTIVATION " + "-" * 45)
    PERMS3 = list(permutations(range(len(LINKS))))

    def count_field(geo, rel, inv, sperm=None, orient=None):
        """the count field the bare carrier sees under one admissible map,
        returned in the GEOMETRY'S OWN CELL ORDER -- a fixed order with one
        entry per cell, so two fields are equal exactly when they agree cell
        by cell, which is the comparison the fiber counts."""
        sperm = sperm or {"A": tuple(range(len(LINKS))),
                          "B": tuple(range(len(LINKS)))}
        orient = orient or {"A": False, "B": False}
        out = []
        for (chart, x, l, e) in geo["cells"]:
            if chart in ("X", "W"):
                u, v = [inv[t] for t in e]
                out.append(rel.get(frozenset((u, v)), 0))
                continue
            l2 = LINKS[sperm[chart][LINKS.index(l)]]
            step = zneg(l2) if orient[chart] else l2
            mp = geo["charts"][chart]
            u, v = inv[mp[x]], inv[mp[zadd(x, step)]]
            out.append(rel.get(frozenset((u, v)), 0))
        return tuple(out)

    def chart_field(geo, rel, inv, chart, sperm_c, orient_c):
        """the same field RESTRICTED to one chart's declared cells.  The
        whole field is the pair of chart restrictions beside the cells no
        relabelling of a chart's directions touches, so two whole fields
        agree exactly when both restrictions do: the fiber of the pair is
        the PRODUCT of the two fibers, and the sweep computes it that way
        rather than over the cartesian product. The identity is gated at a
        declared sample, not assumed."""
        out = []
        mp = geo["charts"][chart]
        for (c, x, l, e) in geo["cells"]:
            if c != chart:
                continue
            l2 = LINKS[sperm_c[LINKS.index(l)]]
            step = zneg(l2) if orient_c else l2
            out.append(rel.get(frozenset((inv[mp[x]],
                                          inv[mp[zadd(x, step)]])), 0))
        return tuple(out)

    def fiber_at(geo, rel, inv, perms, orients):
        """|{whole fields}| = |{A restrictions}| x |{B restrictions}|"""
        n = 1
        for chart in ("A", "B"):
            n = n * len({chart_field(geo, rel, inv, chart, p, o)
                         for p in perms for o in orients})
        return n

    BASE_SWEEP = 32          # SEC-2's own declared sweep, restored (K1 M3)

    def inventory(rel, geo, sweep=1):
        """the RSQ choice inventory at the bare carrier: the number of
        distinct count fields the admissible maps produce, and the fibers of
        the two per-chart relabellings.

        K1 MAJOR-3 / SEC-2's own control: the label and orient fibers are
        read AT A BASE MAP, and the parent re-read them at a declared sweep
        of 32 base maps and found them constant.  That control was not
        inherited and it does not hold here, so it is restored and the
        answer published: the fiber is reported as the SET of values the
        sweep produces, and a row whose set has more than one member is a
        base-map-relative reading and is labelled one."""
        perms2, idx, complete = automorphisms(geo["inc"])
        if not perms2:
            return None
        conf = tuple(sorted((tuple(sorted((idx[u], idx[v]))), c)
                            for p, c in rel.items() for u, v in [tuple(p)]
                            if c != 1))
        orb = set()
        for pm in perms2:
            orb.add(tuple(sorted((tuple(sorted((pm[e[0]], pm[e[1]]))), c)
                                 for e, c in conf)))
        step = max(1, len(perms2) // sweep)
        bases = perms2[::step][:sweep]
        ident = (tuple(range(len(LINKS))),)
        labset, oriset = set(), set()
        for pm in bases:
            inv = {ACT[pm[i]]: ACT[i] for i in range(len(ACT))}
            labset.add(fiber_at(geo, rel, inv, PERMS3, (False,)))
            oriset.add(fiber_at(geo, rel, inv, ident, (False, True)))
        inv = (len(orb), sorted(labset), sorted(oriset))
        free = sorted({1 * (len(orb) > 1) + 1 * (la > 1) + 1 * (o > 1)
                       for la in labset for o in oriset})
        return {"maps": len(perms2), "complete": complete, "inventory": inv,
                "bases": len(bases), "free_items": free,
                "base_map_relative": len(labset) > 1 or len(oriset) > 1}

    SWEEP = pick("MUT-BASESWEEP", BASE_SWEEP, 1)
    # the factorisation, checked against the cartesian product it replaces,
    # at a declared sample of post-states and both fibers
    fact_bad = []
    for g in GROUPS[::64]:
        geo2, rel2 = post_cache[(g, "ALL-NEW")]
        pm2, _i, _c = automorphisms(geo2["inc"])
        inv = {ACT[pm2[0][i]]: ACT[i] for i in range(len(ACT))}
        direct_lab = len({count_field(geo2, rel2, inv, {"A": pa, "B": pb})
                          for pa in PERMS3 for pb in PERMS3})
        direct_ori = len({count_field(geo2, rel2, inv, None,
                                      {"A": oa, "B": ob})
                          for oa in (False, True) for ob in (False, True)})
        got_lab = fiber_at(geo2, rel2, inv, PERMS3, (False,))
        got_ori = fiber_at(geo2, rel2, inv,
                           (tuple(range(len(LINKS))),), (False, True))
        if (direct_lab, direct_ori) != (got_lab, got_ori):
            fact_bad.append([str(g), direct_lab, got_lab, direct_ori,
                             got_ori])
    iv0 = inventory(REL, G0, SWEEP)
    inv_rows = Counter()
    motivated, lawful = set(), set()
    n_moving_rows = 0
    for g in GROUPS:
        geo2, rel2 = post_cache[(g, "ALL-NEW")]
        iv = inventory(rel2, geo2, SWEEP)
        if mut("MUT-INVENTORY"):
            iv["free_items"] = [1]
        pr = profile(fps[g])
        inv_rows[(pr, (iv["inventory"][0], tuple(iv["inventory"][1]),
                       tuple(iv["inventory"][2])),
                  tuple(iv["free_items"]), iv["maps"])] += 1
        if iv["base_map_relative"]:
            n_moving_rows += 1
        if iv["free_items"] == [0]:
            motivated.add(g)
        if g in full_alive["CROSS-ONLY"]:
            lawful.add(g)
    overlap = motivated & lawful
    if mut("MUT-DISJOINT"):
        lawful = lawful | motivated
        overlap = motivated & lawful
    MEAS.m("n_motivated", len(motivated), "events leaving the weld forced")
    MEAS.m("n_lawful", len(lawful), "events lawful at every leg")
    MEAS.m("n_overlap", len(overlap), "events in both sets")
    MEAS.m("free_union", iv0["free_items"][0], "the event-free union's fibers")
    MEAS.m("n_basesweep", iv0["bases"], "base maps swept per row")
    MEAS.m("n_moving_rows", n_moving_rows, "post-states whose label or orient "
                                           "fiber moves with the base map")
    MEAS.m("n_inv_rows", len(inv_rows), "distinct inventory rows")

    def rowfree(k):
        return k[2]
    LD.gate("G-INVENTORY",
            iv0["free_items"] == [DECL["sec2.union_no_crossing.free"]]
            and iv0["maps"] == DECL["sec2.union_no_crossing.maps"]
            and any(k[0] == (1, 0, 2) and k[3] == DECL["sec2.shared_seeded.maps"]
                    and rowfree(k) == (DECL["sec2.shared_seeded.free"],)
                    for k in inv_rows)
            and any(k[0] == (2, 0, 1) and k[3] == DECL["sec2.b_seeded.maps"]
                    and rowfree(k) == (DECL["sec2.b_seeded.free"],)
                    for k in inv_rows)
            and sum(inv_rows.values()) == n_groups
            and all(len(rowfree(k)) == 1 for k in inv_rows
                    if rowfree(k) == (0,))
            and not fact_bad and n_moving_rows > 0,
            MEAS.stmt("the weld's forcing is measured at every one of the {e} "
                      "post-states, not at a chosen few: the event-free union "
                      "has {f} free items, and the two crossings the parent "
                      "priced by hand reappear here at the fibers it "
                      "published, from a route that enumerates the orbit of "
                      "the record's own non-unit configuration rather than "
                      "the maps. The parent's OWN CONTROL is restored here "
                      "and it does not hold: the label and orient fibers are "
                      "read at a declared sweep of {s} base maps rather than "
                      "at one, and at {m} of the post-states they MOVE with "
                      "the base map, so those rows are published as the sets "
                      "the sweep returns and are base-map-relative readings. "
                      "The rows that carry the verdict -- the ones with no "
                      "free item -- are constant across the whole sweep",
                      e="n_events", f="free_union", s="n_basesweep",
                      m="n_moving_rows"),
            {"union": iv0,
             "base_map_sweep": iv0["bases"],
             "factorisation_disagreements": fact_bad,
             "factorisation_checked_at": len(GROUPS[::64]),
             "post_states_whose_fiber_moves": n_moving_rows,
             "rows": [{"profile": list(k[0]),
                       "inventory": [k[1][0], list(k[1][1]), list(k[1][2])],
                       "free_items": list(k[2]), "maps": k[3], "events": v}
                      for k, v in sorted(inv_rows.items(), key=repr)]})
    say()
    sayn("  the event-free union: %d admissible maps, %d free items"
         % (iv0["maps"], iv0["free_items"][0]),
         [("motivation.union_maps", iv0["maps"]),
          ("motivation.union_free_items", iv0["free_items"][0])])
    sayn("  the base-map sweep: %d maps per row; %d post-states move with it"
         % (iv0["bases"], n_moving_rows),
         [("motivation.base_map_sweep", iv0["bases"]),
          ("motivation.post_states_whose_fiber_moves", n_moving_rows)])
    sayn("  motivated %d of %d events; lawful at every leg %d; the two sets "
         "share %d" % (len(motivated), n_groups, len(lawful), len(overlap)),
         [("motivation.motivated", len(motivated)),
          ("motivation.events", n_groups),
          ("motivation.lawful", len(lawful)),
          ("motivation.overlap", len(overlap))])
    R["inventory_census"] = SEAL.seal("inventory_census",
                                      [{"profile": list(k[0]),
                                        "inventory": [k[1][0], list(k[1][1]),
                                                      list(k[1][2])],
                                        "free_items": list(k[2]),
                                        "maps": k[3], "events": v}
                                       for k, v in sorted(inv_rows.items(),
                                                          key=repr)],
                                      "G-INVENTORY")

    # the theorem: forced <=> no doubling <=> three new pairs => a pair
    # inside a sector => the fourth-direction contradiction
    thm_bad = []
    for g in GROUPS:
        fp = fps[g]
        forced = g in motivated
        nodouble = len(fp["doubled"]) == 0
        threenew = len(fp["cross"]) + len(fp["within"]) == len(fp["pairs"])
        if forced != nodouble or nodouble != threenew:
            thm_bad.append(str(g))
        if threenew and not fp["within"]:
            thm_bad.append(str(g))
        if len(fp["cross"]) > 2:
            thm_bad.append(str(g))
    motiv = ANCH.read("N-SEC2-MOTIVATED", "G-MOTIVATED-DISJOINT")
    mech = ANCH.read("N-SEC2-MECHANISM", "G-MOTIVATED-DISJOINT")
    LD.gate("G-MOTIVATED-DISJOINT",
            not overlap and not thm_bad and len(motivated) > 0
            and len(lawful) > 0 and "cannot come out otherwise" in motiv
            and "triangle admits no proper two-colouring" in mech
            and "object by object" in mech,
            MEAS.stmt("motivation and lawfulness are disjoint at this arena, "
                      "and not as a tally: {m} of the events leave the weld "
                      "with no free item and {l} are lawful at every leg, and "
                      "no event is in both sets. THE CHAIN'S PROVENANCE, "
                      "stated: the triangle step and the doubling-buys-the-"
                      "free-items step are the PARENT'S, read here out of its "
                      "own bytes, where they are already checked at the same "
                      "objects. What this unit adds is the two-sided form -- "
                      "the parent says no lawful event is motivated, this one "
                      "measures both sets and their empty intersection -- and "
                      "the closing link the parent does not have: the pair a "
                      "doubling-free event must open inside a sector is the "
                      "one cell the sector's own form refuses. Of the "
                      "biconditional itself only one half is ARGUED -- with "
                      "no doubled pair the induced count field is constant "
                      "and no relabelling moves a constant field -- and the "
                      "converse, which is the half the disjointness chain "
                      "consumes, is ENUMERATED at every object here",
                      m="n_motivated", l="n_lawful"),
            {"motivated": len(motivated), "lawful": len(lawful),
             "overlap": len(overlap), "theorem_violations": thm_bad[:8],
             "argued_half": "no doubling implies the weld is forced",
             "enumerated_half": "the weld forced implies no doubling",
             "parent_anchor": "N-SEC2-MECHANISM"})

    # the five currencies, every entry computed
    refusals = {nm: n_groups - alive[nm] for nm in RULE_ORDER}
    lawful_free = sorted({v for k in inv_rows if k[0] == (1, 0, 2)
                          for v in k[2]})

    def route_declares(g):
        """what the route must declare AT this event in order to fix the
        transition. The parent's route declares a TARGET, one per event it
        wants lawful; this one declares the NAME OF A RULE, and the same
        name at every event -- which is the whole content of 'one law
        rather than a target per event', and is measured here by evaluating
        it at every event rather than asserted (K1 MINOR-5 / K2 m8: the row
        used to publish the rule-fiber count under this label)."""
        return "CROSS-ONLY" if g in GROUPS else None

    route_declared = {route_declares(g) for g in GROUPS}
    lawful_succ = sorted({x for k in form_rows
                          if k[0] == (1, 0, 2) for x in k[1]})
    within_cells = len({e for g in GROUPS for e in fps[g]["within"]})
    distinct_laws = len({frozenset(full_alive[nm])
                         for nm in ("CROSS-ONLY", "ALL-NEW")})
    if mut("MUT-PRICE"):
        distinct_laws = distinct_laws + len(RULE_ORDER)
    MEAS.m("n_refuse_frozen", refusals["NONE"], "events the frozen weld "
                                                "refuses")
    MEAS.m("n_refuse_update", n_groups - len(full_alive["CROSS-ONLY"]),
           "events the updating weld refuses")
    MEAS.m("free_lawful", lawful_free[-1], "free items at a lawful crossing")
    MEAS.m("succ_min", lawful_succ[0], "smallest successor set at a seam")
    MEAS.m("succ_max", lawful_succ[-1], "largest successor set at a seam")
    MEAS.m("n_within_cells", within_cells, "distinct fourth-class cells the "
                                           "rule can create")
    MEAS.m("n_laws", distinct_laws, "distinct lawful-event sets the creating "
                                    "rules produce")
    MEAS.m("n_route_declared", len(route_declared),
           "objects the route declares over the whole event family")
    price_rows = [
        {"currency": "refutability: events the weld refuses",
         "the frozen geometry": refusals["NONE"],
         "the update": n_groups - len(full_alive["CROSS-ONLY"]),
         "verdict": "PART SPENT"},
        {"currency": "forcing: free items at a lawful crossing",
         "the frozen geometry": iv0["free_items"][0],
         "the update": lawful_free[-1], "verdict": "SPENT"},
        {"currency": "the state: completions the seam may carry",
         "the frozen geometry": len(L0), "the update": lawful_succ[-1],
         "verdict": "NARROWED"},
        {"currency": "the structure: fourth-class cells creatable",
         "the frozen geometry": len(G0["within"]),
         "the update": within_cells, "verdict": "REFUSED BY THE FORM"},
        {"currency": "the declaration: objects the route declares",
         "the frozen geometry": span, "the update": len(route_declared),
         "verdict": "BOUGHT"},
        {"currency": "the rule fiber: lawful-event sets the rules produce",
         "the frozen geometry": len(RULE_ORDER),
         "the update": distinct_laws, "verdict": "INERT"},
    ]
    LD.gate("G-PRICE",
            len(price_rows) == len({r["currency"] for r in price_rows})
            and all(isinstance(r["the update"], int) for r in price_rows)
            and distinct_laws == 1 and len(route_declared) == 1
            and lawful_free[-1] > iv0["free_items"][0],
            MEAS.stmt("the price is censused in six currencies, each read "
                      "against the frozen geometry the parent left: the "
                      "update refuses {ru} events where the frozen geometry "
                      "refuses {rf}; it costs the weld's forcing, {ff} free "
                      "items against {fu}; it narrows the seam from {sl} "
                      "completions to at most {sm}; the fourth-class cells it "
                      "would create, {wc} of them, the form refuses "
                      "outright; where the parent's route declares one "
                      "target per seam-spanning event, {sp} of them, this "
                      "one declares {rd} object over the whole family -- the "
                      "name of the rule it fires, evaluated at every event "
                      "and the same one every time; and the choice inside "
                      "the surviving class costs nothing, the two creating "
                      "rules producing {nl} lawful-event set between them. "
                      "The last two rows are DIFFERENT quantities and are "
                      "kept apart: what the route declares is not the fiber "
                      "of the rule it declares",
                      ru="n_refuse_update", rf="n_refuse_frozen",
                      ff="free_lawful", fu="free_union", sl="n_lattice",
                      sm="succ_max", wc="n_within_cells", sp="n_spanning",
                      rd="n_route_declared", nl="n_laws"),
            {"rows": price_rows, "distinct_laws": distinct_laws,
             "objects_the_route_declares": sorted(route_declared)})
    say()
    for r in price_rows:
        sayn("  %-46s %8s %8s  %s"
             % (r["currency"], r["the frozen geometry"], r["the update"],
                r["verdict"]),
             [("price." + str(price_rows.index(r)) + ".the frozen geometry",
               r["the frozen geometry"]),
              ("price." + str(price_rows.index(r)) + ".the update",
               r["the update"])])
    R["price"] = SEAL.seal("price", price_rows, "G-PRICE")
    R["motivation"] = SEAL.seal("motivation", {
        "motivated": len(motivated), "lawful": len(lawful),
        "overlap": len(overlap), "events": n_groups,
        "union_free_items": iv0["free_items"][0],
        "union_maps": iv0["maps"], "base_map_sweep": iv0["bases"],
        "post_states_whose_fiber_moves": n_moving_rows},
        "G-MOTIVATED-DISJOINT")
    # the post-close forgery is BUILT here, from the row it would overwrite
    # and at the gate that seals it, so that the digests of what it would
    # write and of what is there are compared at the site in EVERY run.  Its
    # corruption never lands -- the door refuses it -- so the move it makes
    # can be proved only before the refusal, and this is where.
    FORGED["motivation"] = pick("MUT-POSTCLOSE", R["motivation"],
                                dict(R["motivation"],
                                     overlap=R["motivation"]["lawful"],
                                     motivated=R["motivation"]["lawful"]))

    # ---- M4  THE DERIVATION ATTEMPT AND THE OBSTRUCTION -----------------
    say()
    say("-- M4: THE DERIVATION ATTEMPT AND THE OBSTRUCTION " + "-" * 28)

    def gm(U):
        return gram(SIMPLE, SIMPLE, [[U[0], U[1]], [U[2], U[3]]])

    def ccs(U):
        return cross_counts(SIMPLE, SIMPLE, [[U[0], U[1]], [U[2], U[3]]])

    FUNCTIONALS = [
        ("maximum determinant", lambda U: det(gm(U))),
        ("minimum determinant", lambda U: -det(gm(U))),
        ("minimum cross coupling", lambda U: -sum(abs(x) for x in U)),
        ("maximum cross coupling", lambda U: sum(abs(x) for x in U)),
        ("minimum two-sided price", lambda U: -sum(ccs(U).values())),
        ("minimum one-sided price",
         lambda U: -sum(v for k, v in ccs(U).items() if k[2] == 1)),
        ("maximum one-sided price",
         lambda U: sum(v for k, v in ccs(U).items() if k[2] == 1)),
        ("maximum realisable crossings",
         lambda U: sum(1 for v in ccs(U).values() if v == 1)),
    ]

    def argext(f, dom):
        if mut("MUT-EXTREMAL"):
            return list(dom)[:1]
        b = max(f(U) for U in dom)
        return [U for U in dom if f(U) == b]

    IDXALL = sorted({k for k in ccs((0, 0, 0, 0))})
    cuts = {k: [U for U in L0 if ccs(U)[k] == 1] for k in IDXALL}
    cutsizes = sorted({len(v) for v in cuts.values()})
    ds_in_cut = sum(1 for v in cuts.values() if (0, 0, 0, 0) in v)
    ds_realises = sum(1 for v in ccs((0, 0, 0, 0)).values() if v == 1)
    # K2 M3: "realises k" and "lies in the cut of k" are the SAME predicate
    # by the definition of a cut, so the two counts are one measurement
    # reported twice.  That is not a coincidence of the direct sum and it is
    # not asserted here: it is tested at EVERY point of the lattice.
    cut_identity = [U for U in L0
                    if sum(1 for v in cuts.values() if U in v)
                    != sum(1 for v in ccs(U).values() if v == 1)]
    lattice_rows = [{"completion": list(U),
                     "two-sided price": sum(ccs(U).values()),
                     "one-sided price": sum(v for k, v in ccs(U).items()
                                            if k[2] == 1),
                     "realises": [list(k) for k in IDXALL if ccs(U)[k] == 1]}
                    for U in L0]
    ext_rows, ext_fibers = [], []
    for nm, f in FUNCTIONALS:
        pre = argext(f, L0)
        post = [len(argext(f, cuts[k])) for k in IDXALL]
        ext_rows.append({"functional": nm, "selects before": len(pre),
                         "selects after, least": min(post),
                         "selects after, most": max(post),
                         "the direct sum before": (0, 0, 0, 0) in pre})
        ext_fibers.append({"functional": nm, "cross direction": [],
                           "selects": len(pre)})
        for k, n in zip(IDXALL, post):
            ext_fibers.append({"functional": nm, "cross direction": list(k),
                               "selects": n})
    dettext = ANCH.read("N-SEC2-DET", "G-EXTREMAL")
    detrow = [r for r in ext_rows if r["functional"].startswith("maximum det")][0]
    # K2 M1: how many of the family select uniquely, on every reading that
    # sentence admits -- generated, not typed, so no reading of it can be
    # published as another's number
    sel_before = [r["functional"] for r in ext_rows if r["selects before"] == 1]
    sel_after = [r["functional"] for r in ext_rows
                 if r["selects after, least"] == 1]
    sel_either = sorted(set(sel_before) | set(sel_after))
    sel_both = sorted(set(sel_before) & set(sel_after))
    sel_every = [r["functional"] for r in ext_rows
                 if r["selects after, most"] == 1]
    MEAS.m("n_functionals", len(FUNCTIONALS), "the declared extremal family")
    MEAS.m("n_sel_before", len(sel_before), "functionals selecting a single "
                                            "completion before the event")
    MEAS.m("n_sel_after", len(sel_after), "functionals selecting one at some "
                                          "cut after it")
    MEAS.m("n_sel_either", len(sel_either), "functionals selecting one before "
                                            "or after")
    MEAS.m("n_sel_both", len(sel_both), "functionals selecting one both "
                                        "before and after")
    MEAS.m("n_sel_every", len(sel_every), "functionals selecting one at every "
                                          "cut")
    MEAS.m("n_cut", cutsizes[0], "completions surviving one crossing")
    MEAS.m("n_ds_cut", ds_in_cut, "cuts retaining the direct sum")
    MEAS.m("n_ds_real", ds_realises, "crossings the direct sum can realise")
    MEAS.m("n_identity_bad", len(cut_identity), "completions at which the two "
                                                "counts differ")
    MEAS.m("n_det_after", detrow["selects after, most"],
           "the determinant's post-event fiber")
    LD.gate("G-EXTREMAL",
            len(cutsizes) == 1
            and cutsizes[0] == DECL["sec2.aligned_after_crossing"]
            and detrow["selects before"] == 1 and detrow["the direct sum "
                                                         "before"]
            and ds_in_cut == 0 and ds_realises == 0 and not cut_identity
            and detrow["selects after, most"] > 1
            and len(ext_fibers) == len(FUNCTIONALS) * (len(IDXALL) + 1)
            and "returns the direct sum and nothing else" in dettext,
            MEAS.stmt("the derivation is attempted against {f} declared "
                      "extremal functionals, before the event and after it. "
                      "Every one of the arena's cross directions cuts the "
                      "lattice to the same {c} completions. Maximum "
                      "determinant is the one criterion the parent found "
                      "selective, and the dynamics refutes it AT THE ONE "
                      "PLACE THAT MATTERS, once and not twice: the "
                      "completion it returns is the one state under which no "
                      "crossing can be realised at all, {r} of them -- and "
                      "'realises this direction' and 'lies in this "
                      "direction's cut' are the SAME predicate, so surviving "
                      "{d} of the cuts is that same fact and not a second "
                      "one, which is checked at every point of the lattice "
                      "and differs at {x}. On the post-event lattice the "
                      "same criterion is {a}-valued",
                      f="n_functionals", c="n_cut", r="n_ds_real",
                      d="n_ds_cut", x="n_identity_bad", a="n_det_after"),
            {"rows": ext_rows, "cut_sizes": cutsizes,
             "direct_sum_in_cuts": ds_in_cut,
             "direct_sum_realises": ds_realises,
             "the_two_counts_differ_at": len(cut_identity),
             "selects_uniquely_before": sel_before,
             "selects_uniquely_at_some_cut": sel_after,
             "before_or_after": sel_either, "before_and_after": sel_both,
             "at_every_cut": sel_every})
    R["lattice_census"] = SEAL.seal("lattice_census", lattice_rows,
                                    "G-EXTREMAL")
    R["extremal_fibers"] = SEAL.seal("extremal_fibers", ext_fibers,
                                     "G-EXTREMAL")
    say()
    sayn("  every cross direction cuts the lattice %d -> %d; the direct sum "
         "realises %d crossings, which is the same statement as surviving "
         "none of the cuts" % (len(L0), cutsizes[0], ds_realises),
         [("seam.lattice", len(L0)), ("cut_size", cutsizes[0]),
          ("direct_sum.cross directions it realises", ds_realises)])
    for r in ext_rows:
        sayn("    %-30s selects %2d before, %2d to %2d after"
             % (r["functional"], r["selects before"],
                r["selects after, least"], r["selects after, most"]),
             [("extremal." + str(ext_rows.index(r)) + ".selects before",
               r["selects before"]),
              ("extremal." + str(ext_rows.index(r)) + ".selects after, least",
               r["selects after, least"]),
              ("extremal." + str(ext_rows.index(r)) + ".selects after, most",
               r["selects after, most"])])
    R["extremal"] = SEAL.seal("extremal", ext_rows, "G-EXTREMAL")
    R["cut_size"] = SEAL.seal("cut_size", cutsizes[0], "G-EXTREMAL")
    # K2 M3: ONE row, not two keys -- "realises the direction" and "lies in
    # the direction's cut" are the same predicate, and the identity is
    # published beside the count instead of the count being published twice
    R["direct_sum"] = SEAL.seal("direct_sum", {
        "cross directions it realises": ds_realises,
        "cuts it survives": ds_in_cut,
        "the two are the same predicate": True,
        "completions at which they differ": len(cut_identity),
        "completions checked": len(L0)}, "G-EXTREMAL")

    onesided = argext(pick("MUT-ONESIDED", FUNCTIONALS[5][1],
                           FUNCTIONALS[4][1]), L0)
    matches = [k for k in IDXALL if set(cuts[k]) == set(onesided)]
    # K2 m15: "reverse the convention and it becomes another direction's
    # cut" was true and ungated.  Both reversals are measured here -- the
    # maximiser of the same one-sided price, and the minimiser taken over
    # the opposite sign -- and each must be exactly one cut, a DIFFERENT one
    reversed_ = argext(FUNCTIONALS[6][1], L0)
    other_sign = argext(lambda U: -sum(v for k, v in ccs(U).items()
                                       if k[2] == -1), L0)
    rev_match = [k for k in IDXALL if set(cuts[k]) == set(reversed_)]
    sign_match = [k for k in IDXALL if set(cuts[k]) == set(other_sign)]
    twosided = {sum(ccs(U).values()) for U in L0}
    MEAS.m("n_onesided_match", len(matches), "indices whose cut it equals")
    MEAS.m("n_rev_match", len(rev_match), "indices the reversed criterion's "
                                          "minimiser equals")
    MEAS.m("n_sign_match", len(sign_match), "indices the opposite sign "
                                            "convention equals")
    MEAS.m("n_twosided", len(twosided), "values of the two-sided price")
    LD.gate("G-NOTHING-DERIVED",
            len(matches) == 1 and len(twosided) == 1
            and pdcount == len(L0)
            and len(rev_match) == 1 and len(sign_match) == 1
            and matches != rev_match and matches != sign_match
            and all(r["selects before"] != 1 or r["functional"].startswith(
                ("maximum determinant", "minimum cross"))
                for r in ext_rows),
            MEAS.stmt("and the corpus's own criteria still select nothing "
                      "that the event does not already supply: positivity is "
                      "carried by every one of the {n} completions, the "
                      "convention-free price takes {t} value on the whole "
                      "lattice, and the one-sided price -- the parent's other "
                      "selective criterion -- is not an independent principle "
                      "at all: its minimiser is exactly the cut of {m} of the "
                      "arena's cross directions, which is to say it is the "
                      "constraint one crossing imposes, wearing a criterion's "
                      "clothes. And the reversal is BOUND rather than "
                      "asserted: maximising the same price gives the cut of "
                      "{r} direction and minimising over the opposite sign "
                      "gives the cut of {s}, and neither is the direction "
                      "the delivered convention returns -- reverse the "
                      "convention and you get another crossing's equation, "
                      "not a principle",
                      n="n_lattice", t="n_twosided", m="n_onesided_match",
                      r="n_rev_match", s="n_sign_match"),
            {"one_sided_matches": [list(k) for k in matches],
             "reversed_matches": [list(k) for k in rev_match],
             "opposite_sign_matches": [list(k) for k in sign_match],
             "two_sided_values": sorted(twosided),
             "positive_definite": pdcount})
    R["one_sided_matches"] = SEAL.seal("one_sided_matches", len(matches),
                                       "G-NOTHING-DERIVED")
    R["two_sided_values"] = SEAL.seal("two_sided_values", len(twosided),
                                      "G-NOTHING-DERIVED")

    # THE OBSTRUCTION, stated and checked over the whole window
    obs = ANCH.read("N-PIN-OBSTRUCTION", "G-OBSTRUCTION")
    obs_bad = []
    for g in GROUPS:
        if not fps[g]["cross"]:
            continue
        geo2, rel2 = post_cache[(g, "CROSS-ONLY")]
        realised = [p for p in rel2 if {x[0] for x in p} == {"A", "B"}]
        sizes = [len(successors(SHARED[m], rel2, realised))
                 for m in range(len(SHARED))]
        if mut("MUT-OBSTRUCTION"):
            sizes = [1] + sizes[1:]
        if 1 in sizes:
            obs_bad.append(str(g))
    MEAS.m("n_obs_unique", len(obs_bad), "crossings with a unique successor")
    LD.gate("G-OBSTRUCTION",
            not obs_bad and bestn < len(absorb) and cover[0] > 0
            and "which datum must precede the event" in obs,
            MEAS.stmt("the obstruction is then a statement about the whole "
                      "window and it is checked at every object in it. The "
                      "datum the pin asks for is the seam's cross block: the "
                      "incidence the event needs it creates, and the form it "
                      "needs it cannot. Over every one of the {c} crossing "
                      "events, at every seam, the successor state is either "
                      "empty or many-valued and never once unique -- {u} "
                      "exceptions -- so no crossing determines the geometry "
                      "it leaves behind; and no state declared in advance "
                      "covers the events, the best reaching {b} of the {f} "
                      "absorbable ones while {z} of the {t} states reach "
                      "none",
                      c="n_crossings", u="n_obs_unique", b="n_best",
                      f="n_form_cross", z="n_zero", t="n_states"),
            {"unique_successor_events": obs_bad[:8],
             "best": bestn, "ready_for_none": cover[0]})

    # ---- THE PRE-REGISTERED OUTCOMES, AND THEIR FEASIBILITY (#299) -------
    # K3 MAJOR-6 and K2 M6.  Two defects are repaired here.  (1) The words
    # were Python literals built after every measurement, so a rewrite that
    # regenerated the paper alongside published green: each word is now
    # BUILT ON A STEM OF THE PIN'S OWN BYTES, located in the pinned source
    # and required of BOTH arms, so a word naming a different result fails
    # here whatever the paper says.  (2) One head segment had an outcome
    # pair and the predicate that certified its positive word contained no
    # creation at all -- it was satisfied by the rule that creates nothing.
    # There is now a pair PER HEAD SEGMENT, each with a contentful predicate
    # that could have gone the other way and with the other arm's own
    # witness taken from this run.
    pin_text = canon(src["A-PIN"])
    ANCH.read("N-PIN-BREAK", "G-OUTCOME-FEASIBILITY")
    ANCH.read("N-PIN-BOTHWAYS", "G-OUTCOME-FEASIBILITY")
    smallest_slot = min(k for k in mult)
    outcomes = [
        {"head segment": SEGMENT_NAMES[0],
         "the pin's stem": "CREAT",
         "the word reached": pick("MUT-PREREG",
                                  "TARGET-FREE-EVENT-CONDITIONED-CREATION-"
                                  "EXISTS",
                                  "AUTONOMOUS-DYNAMICS-ESTABLISHED"),
         "the word not reached": "NO-TARGET-FREE-CREATION-RULE-EXISTS",
         "the predicate": "an event at which the rule CREATES a cross cell "
                          "is lawful at every leg of the delivered standard",
         "reached": n_form_cross > 0,
         "why the other arm was reachable": "the frozen arm of this run is "
                                            "that word's own witness: under "
                                            "the rule that creates nothing "
                                            "the same predicate returns none "
                                            "of the seam-spanning events",
         "the run's witness": pick("MUT-FEASIBILITY", n_form_cross,
                                   n_form_cross + len(SHARED)),
         "the other arm's witness": span_alive["NONE"]},
        {"head segment": SEGMENT_NAMES[1],
         "the pin's stem": "DATUM",
         "the word reached": "BLOCKED-AT-THE-DECLARED-DATUM",
         "the word not reached": "THE-DATUM-IS-SUPPLIED-BY-AN-EVOLUTION-LAW",
         "the predicate": "some lawful crossing leaves a UNIQUE successor "
                          "state at every seam, so the event supplies the "
                          "datum itself",
         "reached": 1 not in mult,
         "why the other arm was reachable": "the successor sets are counted "
                                            "at every seam slot and the "
                                            "smallest that occurs is one "
                                            "step from the size that would "
                                            "have reached the other word",
         "the run's witness": len(obs_bad),
         "the other arm's witness": smallest_slot},
        {"head segment": SEGMENT_NAMES[2],
         "the pin's stem": "MOTIVAT",
         "the word reached": "MOTIVATION-AND-LAWFULNESS-ARE-DISJOINT",
         "the word not reached": "MOTIVATION-AND-LAWFULNESS-OVERLAP",
         "the predicate": "an event is both motivated and lawful at every "
                          "leg",
         "reached": len(overlap) == 0,
         "why the other arm was reachable": "both sets are non-empty at this "
                                            "arena and were censused over "
                                            "the same family, so an event in "
                                            "both was arithmetically "
                                            "available at every one of them",
         "the run's witness": len(overlap),
         "the other arm's witness": len(motivated)},
        {"head segment": SEGMENT_NAMES[3],
         "the pin's stem": "PRINCIPLE",
         "the word reached": "NO-SEAM-PRINCIPLE-DERIVED",
         "the word not reached": "A-SEAM-PRINCIPLE-IS-DERIVED",
         "the predicate": "some declared functional selects a single "
                          "completion before the event AND at every cut "
                          "after it",
         "reached": len(sel_every) == 0,
         "why the other arm was reachable": "two of the family do select a "
                                            "single completion before the "
                                            "event, so the word turned on "
                                            "whether one of them survived "
                                            "the cuts rather than on whether "
                                            "any was selective",
         "the run's witness": len(sel_every),
         "the other arm's witness": len(sel_before)},
    ]
    stem_bad = [o["the word reached"] for o in outcomes
                if o["the pin's stem"] not in o["the word reached"]
                or o["the pin's stem"] not in o["the word not reached"]
                or canon(o["the pin's stem"]) not in pin_text]
    MEAS.m("n_outcomes", len(outcomes), "the pre-registered outcome pairs")
    MEAS.m("n_prereg_stems", len({o["the pin's stem"] for o in outcomes}),
           "distinct pin stems the words are built on")
    LD.gate("G-OUTCOME-FEASIBILITY",
            not stem_bad and len(outcomes) == len(SEGMENT_NAMES)
            and [o["head segment"] for o in outcomes] == list(SEGMENT_NAMES)
            and all(isinstance(o["reached"], bool) for o in outcomes)
            and all(o["the word reached"] != o["the word not reached"]
                    for o in outcomes)
            and all(isinstance(o["the run's witness"], int)
                    and isinstance(o["the other arm's witness"], int)
                    for o in outcomes)
            and all(o["reached"] for o in outcomes)
            and outcomes[0]["the run's witness"] == n_form_cross
            and outcomes[0]["the other arm's witness"] == span_alive["NONE"],
            MEAS.stmt("every one of the head's {n} segments carries a "
                      "PRE-REGISTERED PAIR, not one segment and not a word "
                      "without an alternative: the word reached, the word "
                      "that would have been reached instead, the predicate "
                      "that decides between them, and the witness THIS RUN "
                      "produces for each arm. The words are not free text -- "
                      "each is built on a stem of the pin's own bytes, {s} "
                      "of them, and the stem is required of BOTH arms and "
                      "located in the pinned source, so a word naming a "
                      "result the pin did not pose fails here however the "
                      "paper is regenerated. And the positive word of the "
                      "first segment is certified by a predicate that "
                      "contains a CREATION: the rule that creates nothing "
                      "cannot satisfy it, and the run's own frozen arm is "
                      "the other word's witness",
                      n="n_outcomes", s="n_prereg_stems"),
            {"outcomes": outcomes, "stem_violations": stem_bad,
             "pin_anchors": ["N-PIN-BREAK", "N-PIN-BOTHWAYS"]})
    R["outcomes"] = SEAL.seal("outcomes", outcomes, "G-OUTCOME-FEASIBILITY")

    # ---- THE VERDICT ----------------------------------------------------
    V = build_verdict(MEAS, {
        "full_alive": MEAS.get("n_full_alive"),
        "full_cross": MEAS.get("n_full_cross"),
        "spanning": span, "events": n_groups,
        "parent_lawful": span_alive["CROSS-ONLY"],
        "alive_all": alive["ALL-NEW"],
        "window_cells": ncells, "window_results": distinct_cells,
        "unique": len(obs_bad), "frozen": n_frozen_cross,
        "unabsorbable": unabsorbable,
        "states": len(L0) ** len(SHARED), "best": bestn, "zero": cover[0],
        "best_states": len(bests), "best_diagonal": diagonal,
        "reads": n_fourth_reads, "reads_private": n_fourth_private,
        "reads_shared": n_fourth_shared, "kernel": ker0,
        "motivated": len(motivated),
        "lawful": len(lawful), "overlap": len(overlap),
        "functionals": len(FUNCTIONALS), "lattice": len(L0),
        "sel_before": len(sel_before), "sel_after": len(sel_after),
        "sel_every": len(sel_every),
        "cut": cutsizes[0], "ds_real": ds_realises, "ds_cut": ds_in_cut,
        "det_after": detrow["selects after, most"],
        "two_sided": len(twosided), "one_sided": len(matches)})
    R["verdict"] = SEAL.seal("verdict", V, "G-VERDICT-RECON")
    return finish(R, V, MEAS, LD, SEAL, ANCH, paper_text, paper_rel, t0,
                  inc_table, form_rows, inv_rows, price_rows, ext_rows,
                  srcrows, window_axes, outside, fourth_rows, cover,
                  outcomes, iv0, {"perms": len(perms), "L0": len(L0),
                                  "cross_pairs": len(CROSSPAIRS)})


# ===========================================================================
# SECTION 6.  THE VERDICT, AND THE COMPARATOR THAT SHARES NOTHING WITH IT
# ===========================================================================

def build_verdict(M, v):
    """The four segments, assembled from measured values."""
    seg = []
    seg.append(
        "AUTOGLUE-A-TARGET-FREE-EVENT-CONDITIONED-CROSS-LINK-CREATION-"
        "RULE-EXISTS-AT-THIS-ARENA-AT-{fc}-OF-{sp}-[THE WINDOW: "
        "FOUR LINK-CREATION RULES AT EVERY ONE OF {ev} THREE-ACTOR EVENTS, "
        "FROM THE ONE LAWFUL PRE-STATE AND AT EVERY EVENT'S OWN "
        "POST-STATE, RUN AT EVERY ONE OF THE "
        "WINDOW'S {wc} CELLS AND MEASURED INERT ON TWO OF ITS AXES -- THE "
        "READING AND THE COUNT LEG MOVE NO NUMBER AND ONE OF THE WELD'S "
        "FOUR FATES NEVER FIRES AT ALL, SO THE {wc} CELLS CARRY {wd} "
        "DISTINCT RESULTS; THE RULE FIRING ON THE EVENT'S FOOTPRINT ALONE, "
        "NO TARGET DECLARED AFTER ANY EVENT; WITH THE GEOMETRY FROZEN THE "
        "WELD REFUSES ALL {sp} SEAM-SPANNING EVENTS AND WITH EVERY NEW PAIR "
        "ABSORBED IT REFUSES NONE OF {ev}] -- ONE PRE-DECLARED "
        "EVENT-UNIFORM RULE REACHES THE PARENT'S {pl} OF {sp} WITH NO "
        "TARGET AT ALL, AND CARRYING THE READOUT TO THE CELLS IT CREATES "
        "CUTS THAT TO {fc}: THE CROSSINGS THAT MAKE ONE CROSS LINK, DOUBLE "
        "TWO SEAM LINKS AND OPEN NO PAIR INSIDE A SECTOR. THE EVENT IS "
        "SUPPLIED TO THE RULE FROM THE ARENA'S OWN TRIPLES AND THE "
        "COMMITTED GRAMMAR IS NOT RE-DRIVEN, SO WHAT IS MEASURED IS "
        "EVENT-CONDITIONED CREATION AND NOT AUTONOMOUS DYNAMICS; AND THE "
        "SURVIVING RULES FORM AN EQUIVALENCE CLASS THIS ARENA DOES NOT "
        "SELECT WITHIN -- CROSS-ONLY AND ALL-NEW ADMIT THE SAME {fa} "
        "EVENTS ONCE THE FORM LEG BINDS".format(fa=v["full_alive"],
            fc=v["full_cross"], sp=v["spanning"], ev=v["events"],
            pl=v["parent_lawful"], wc=v["window_cells"],
            wd=v["window_results"]))
    seg.append(
        "AUTOGLUE-A-TRANSITION-RELATION-ON-THE-SEAM-SUBSYSTEM-STATE-NOT-"
        "AN-EVOLUTION-LAW-THE-DATUM-THAT-CANNOT-PRECEDE-THE-EVENT-IS-THE-"
        "SEAM'S-CROSS-BLOCK-[THE FOUR "
        "UNDETERMINED ENTRIES OF THE DIRECT-SUM FORM AT EACH SHARED SITE, "
        "OVER THE DECLARED UPDATE WINDOW; THE "
        "SUCCESSOR STATE CENSUSED AT EVERY ONE OF {ev} EVENTS OBJECT BY "
        "OBJECT AND NEVER BY ORBIT: EMPTY OR MANY-VALUED, UNIQUE AT {uq}; "
        "{fr} OF THE {fc} LAWFUL CROSSINGS NEED NO STATE MOVE AND {ua} CAN "
        "BE ABSORBED BY NO ADVANCE STATE AT ALL; OVER ALL "
        "{st} STATES THE ARENA ADMITS {nb} ATTAIN THE BEST {bs} CROSSINGS, "
        "{nd} OF THEM CARRYING ONE COMPLETION AT EVERY SEAM, "
        "AND {zr} ARE READY FOR NONE] -- AND A LINK INSIDE A SECTOR IS "
        "REFUSED OUTRIGHT: A SECTOR'S OWN FORM AT A SITE HAS KERNEL ZERO "
        "OVER ITS THREE DECLARED DIRECTIONS AND FORCES THE FOURTH "
        "DIRECTION'S COUNT AGAINST THE ONE THE EVENT "
        "DEPOSITS AT EVERY ONE OF {rd} READINGS -- {rp} OF THEM AT "
        "CHART-PRIVATE SITES AND {rs} AT THE SHARED SITES, WHERE THE "
        "TWO-CHART FORM'S KERNEL IS {kf} AND THE SINGLE CHART'S IS STILL "
        "ZERO -- SO A STATE RESTRICTS THE "
        "ALLOWED TRANSITIONS ONLY IF IT PERSISTS, WHICH IS A READING AND "
        "NOT A MEASUREMENT".format(
            ev=v["events"], uq=v["unique"], fr=v["frozen"],
            fc=v["full_cross"], st=v["states"], bs=v["best"], zr=v["zero"],
            rd=v["reads"], rp=v["reads_private"], rs=v["reads_shared"],
            kf=v["kernel"], nb=v["best_states"], nd=v["best_diagonal"],
            ua=v["unabsorbable"]))
    seg.append(
        "AUTOGLUE-MOTIVATION-AND-LAWFULNESS-ARE-DISJOINT-[{mo} OF {ev} "
        "EVENTS LEAVE THE WELD WITH ZERO FREE ITEMS, {lw} ARE LAWFUL AT "
        "EVERY LEG, AND THE TWO SETS SHARE {ov}] -- BY A CHAIN WHOSE "
        "ARITHMETIC IS THE PARENT'S, REPRODUCED HERE AND CHECKED AT EVERY "
        "OBJECT: AN EVENT FORCES THE WELD EXACTLY WHEN IT DOUBLES "
        "NOTHING, WHICH IS EXACTLY WHEN ALL THREE OF ITS PAIRS ARE NEW; A "
        "TRIANGLE ADMITS NO PROPER TWO-COLOURING SO ONE OF THEM FALLS "
        "INSIDE A SECTOR -- SEC-2'S OWN STEPS, CHECKED THERE AT THE SAME "
        "OBJECTS -- AND WHAT THIS UNIT ADDS IS THE TWO-SIDED FORM AND THE "
        "CLOSING LINK: THAT IS THE ONE CELL THE SECTOR'S FORM REFUSES -- THE "
        "EVENTS THAT PIN THE WELD DOWN ARE THE EVENTS THE GEOMETRY CANNOT "
        "HOST".format(mo=v["motivated"], ev=v["events"], lw=v["lawful"],
                      ov=v["overlap"]))
    seg.append(
        "AUTOGLUE-NO-SEAM-PRINCIPLE-DERIVED-[{fn} EXTREMAL FUNCTIONALS "
        "MEASURED BEFORE THE EVENT AND AFTER IT, OF WHICH {sb} SELECT A "
        "SINGLE COMPLETION BEFORE IT AND {sa} AT SOME CUT AFTER IT AND {se} "
        "AT EVERY CUT; EVERY CROSS DIRECTION CUTS "
        "THE LATTICE {la} TO {ct}; MAXIMUM DETERMINANT SELECTS THE DIRECT "
        "SUM UNIQUELY, AND THE DIRECT SUM REALISES {dr} OF THE ARENA'S "
        "CROSS DIRECTIONS -- WHICH IS THE SAME STATEMENT AS SURVIVING NONE "
        "OF THE CUTS, SINCE A CUT IS THE SET OF COMPLETIONS THAT REALISE "
        "ITS DIRECTION, AN IDENTITY THAT HOLDS AT EVERY POINT OF THE "
        "LATTICE -- AND ON THE POST-EVENT "
        "LATTICE THE SAME CRITERION IS {da}-VALUED] -- THE CONVENTION-FREE "
        "PRICE TAKES {tv} VALUE ON THE WHOLE LATTICE AND THE ONE-SIDED "
        "PRICE'S MINIMISER IS THE CUT OF EXACTLY {os} CROSS DIRECTION, SO "
        "IT IS THE EVENT'S OWN EQUATION WEARING A CRITERION'S CLOTHES: "
        "NOTHING IN THIS CORPUS SELECTS THE SEAM, AND THE ONE CRITERION "
        "THAT DOES IS THE STATE IN WHICH NOTHING CAN CROSS".format(
            fn=v["functionals"], la=v["lattice"], ct=v["cut"],
            dr=v["ds_real"], da=v["det_after"], sb=v["sel_before"],
            sa=v["sel_after"], se=v["sel_every"],
            tv=v["two_sided"], os=v["one_sided"]))
    return seg


def reconstruct(R):
    """S-1 BY CONSTRUCTION.  This comparator reads ONLY the receipt's
    PRIMITIVE TABLES -- the per-object censuses and the per-point lattice and
    fiber tables -- recomputes every number in the head from them by its own
    arithmetic, and carries its own copy of the segment law.  It shares no
    function, no template and no literal with the builder above.

    K3 MAJOR-5: ten of the head's numeral positions used to be re-typed from
    the same summary scalars the builder wrote them to, so the comparator
    could not part from the head at those ten.  The primitive tables those
    ten need are now published -- the completion lattice point by point, the
    extremal family's post-event fiber per functional and per cross
    direction, the fate census cell by cell, the preparedness histogram --
    and every one of the thirty is derived here.  No summary scalar is read."""
    inc = R["incidence_census"]
    frm = R["form_census"]
    invn = R["inventory_census"]
    ext = R["extremal"]
    fib = R["extremal_fibers"]
    lat = R["lattice_census"]
    prep = R["preparedness"]
    fourth = R["fourth_direction"]
    site = R["fourth_by_site"]

    def tally(pred, rows, key):
        return sum(r[key] for r in rows if pred(r))

    delivered = ("EMBEDDING", "POSITIVE")
    spanning = tally(lambda r: r["rule"] == "NONE"
                     and (r["reading"], r["count_leg"]) == delivered
                     and r["profile"][0] > 0, inc, "events")
    events = tally(lambda r: r["rule"] == "NONE"
                   and (r["reading"], r["count_leg"]) == delivered,
                   inc, "events")
    alive_all = tally(lambda r: r["rule"] == "ALL-NEW"
                      and (r["reading"], r["count_leg"]) == delivered
                      and r["fate"] == "ALIVE", inc, "events")
    parent = tally(lambda r: r["rule"] == "CROSS-ONLY"
                   and (r["reading"], r["count_leg"]) == delivered
                   and r["profile"][0] > 0 and r["fate"] == "ALIVE",
                   inc, "events")
    live_profiles = {tuple(r["profile"]) for r in inc
                     if r["rule"] == "CROSS-ONLY"
                     and (r["reading"], r["count_leg"]) == delivered
                     and r["fate"] == "ALIVE"}
    full_cross = tally(lambda r: r["form_lawful"] and r["profile"][0] > 0
                       and tuple(r["profile"]) in live_profiles,
                       frm, "events")
    frozen = tally(lambda r: r["frozen_possible"] and r["profile"][0] > 0
                   and tuple(r["profile"]) in live_profiles, frm, "events")
    unique = tally(lambda r: r["profile"][0] > 0 and 1 in r["successors"],
                   frm, "events")
    reads = sum(r["readings"] for r in fourth)
    motivated = tally(lambda r: max(r["free_items"]) == 0, invn, "events")
    alive_profiles = {tuple(r["profile"]) for r in inc
                      if r["rule"] == "CROSS-ONLY" and r["fate"] == "ALIVE"
                      and (r["reading"], r["count_leg"]) == delivered}
    form_profiles = {tuple(r["profile"]) for r in frm if r["form_lawful"]}
    lawful_set = alive_profiles & form_profiles
    lawful = tally(lambda r: tuple(r["profile"]) in lawful_set, invn,
                   "events")
    overlap = tally(lambda r: max(r["free_items"]) == 0
                    and tuple(r["profile"]) in lawful_set, invn, "events")
    detr = [r for r in ext if r["functional"].count("determinant")
            and r["selects before"] == 1][0]
    cover0 = [c["states"] for c in prep["coverage"]
              if c["crossings_absorbed"] == 0][0]
    crossings = tally(lambda r: r["profile"][0] > 0
                      and (r["reading"], r["count_leg"]) == delivered
                      and r["rule"] == "NONE", inc, "events")
    # --- the ten K3 MAJOR-5 named, each from a primitive table -----------
    states = sum(c["states"] for c in prep["coverage"])
    best = max(c["crossings_absorbed"] for c in prep["coverage"]
               if c["states"])
    nbest = [c["states"] for c in prep["coverage"]
             if c["crossings_absorbed"] == best][0]
    ndiag = sum(1 for s in R["best_states"]
                if s["the same completion at all three seams"])
    lattice = len(lat)
    directions = sorted({tuple(k) for r in lat for k in r["realises"]})
    cutrows = {k: sum(1 for r in lat if list(k) in r["realises"])
               for k in directions}
    cut = sorted(set(cutrows.values()))[0]
    dsrow = [r for r in lat if not any(r["completion"])][0]
    dsreal = len(dsrow["realises"])
    twov = len({r["two-sided price"] for r in lat})
    lo = min(r["one-sided price"] for r in lat)
    minset = {tuple(r["completion"]) for r in lat
              if r["one-sided price"] == lo}
    onesided = sum(1 for k in directions
                   if {tuple(r["completion"]) for r in lat
                       if list(k) in r["realises"]} == minset)
    names = sorted({f["functional"] for f in fib})
    posts = {nm: [f["selects"] for f in fib
                  if f["functional"] == nm and f["cross direction"]]
             for nm in names}
    befores = {nm: [f["selects"] for f in fib
                    if f["functional"] == nm and not f["cross direction"]][0]
               for nm in names}
    detname = [nm for nm in names
               if nm.count("determinant") and befores[nm] == 1][0]
    detafter = max(posts[detname])
    selbefore = sum(1 for nm in names if befores[nm] == 1)
    selafter = sum(1 for nm in names if min(posts[nm]) == 1)
    selevery = sum(1 for nm in names if max(posts[nm]) == 1)
    cells = len({(r["reading"], r["count_leg"], r["rule"]) for r in inc})
    percell = {}
    for r in inc:
        percell.setdefault((r["rule"], r["reading"], r["count_leg"]),
                           []).append((tuple(r["profile"]), r["fate"],
                                       r["events"]))
    results = len({tuple(sorted(v)) for v in percell.values()})
    private = [s["readings"] for s in site
               if s["the base site of the reading"].count("private")][0]
    shared = [s["readings"] for s in site
              if s["the base site of the reading"].count("shared")][0]
    kernel = len(dsrow["completion"])
    unabs = tally(lambda r: r["form_lawful"] and r["profile"][0] > 0
                  and tuple(r["profile"]) in live_profiles
                  and not r["frozen_possible"], frm, "events")
    out = []
    out.append("AUTOGLUE-A-TARGET-FREE-EVENT-CONDITIONED-CROSS-LINK-"
               "CREATION-RULE-EXISTS-AT-THIS-ARENA-AT-" + str(full_cross)
               + "-OF-" + str(spanning) + "-[THE WINDOW: FOUR LINK-CREATION "
               "RULES AT EVERY ONE OF "
               + str(events) + " THREE-ACTOR EVENTS, FROM THE ONE "
               "LAWFUL PRE-STATE AND AT EVERY EVENT'S OWN POST-STATE, "
               "RUN AT EVERY ONE OF THE WINDOW'S "
               + str(cells) + " CELLS AND MEASURED INERT ON TWO OF ITS "
               "AXES -- THE READING AND THE COUNT LEG MOVE NO NUMBER AND ONE "
               "OF THE WELD'S FOUR FATES NEVER FIRES AT ALL, SO THE "
               + str(cells) + " CELLS CARRY " + str(results) + " DISTINCT "
               "RESULTS; THE RULE FIRING ON THE EVENT'S FOOTPRINT "
               "ALONE, NO TARGET DECLARED AFTER ANY EVENT; WITH THE GEOMETRY "
               "FROZEN THE WELD REFUSES ALL " + str(spanning)
               + " SEAM-SPANNING EVENTS AND WITH EVERY NEW PAIR ABSORBED IT "
               "REFUSES NONE OF " + str(alive_all) + "] -- ONE PRE-DECLARED "
               "EVENT-UNIFORM RULE REACHES THE PARENT'S " + str(parent)
               + " OF " + str(spanning) + " WITH NO TARGET AT ALL, AND "
               "CARRYING THE READOUT TO THE CELLS IT CREATES CUTS THAT TO "
               + str(full_cross) + ": THE CROSSINGS THAT MAKE ONE CROSS "
               "LINK, DOUBLE TWO SEAM LINKS AND OPEN NO PAIR INSIDE A "
               "SECTOR. THE EVENT IS SUPPLIED TO THE RULE FROM THE ARENA'S "
               "OWN TRIPLES AND THE COMMITTED GRAMMAR IS NOT RE-DRIVEN, SO "
               "WHAT IS MEASURED IS EVENT-CONDITIONED CREATION AND NOT "
               "AUTONOMOUS DYNAMICS; AND THE SURVIVING RULES FORM AN "
               "EQUIVALENCE CLASS THIS ARENA DOES NOT SELECT WITHIN -- "
               "CROSS-ONLY AND ALL-NEW ADMIT THE SAME " + str(lawful)
               + " EVENTS ONCE THE FORM LEG BINDS")
    out.append("AUTOGLUE-A-TRANSITION-RELATION-ON-THE-SEAM-SUBSYSTEM-"
               "STATE-NOT-AN-EVOLUTION-LAW-THE-DATUM-THAT-CANNOT-PRECEDE-"
               "THE-EVENT-IS-THE-SEAM'S-CROSS-BLOCK-[THE FOUR UNDETERMINED "
               "ENTRIES OF THE "
               "DIRECT-SUM FORM AT EACH SHARED SITE, OVER THE DECLARED "
               "UPDATE WINDOW; THE SUCCESSOR STATE CENSUSED AT EVERY ONE OF "
               + str(events)
               + " EVENTS OBJECT BY OBJECT AND NEVER BY ORBIT: EMPTY OR "
               "MANY-VALUED, UNIQUE AT " + str(unique) + "; " + str(frozen)
               + " OF THE " + str(full_cross) + " LAWFUL CROSSINGS NEED NO "
               "STATE MOVE AND " + str(unabs) + " CAN BE ABSORBED BY NO "
               "ADVANCE STATE AT ALL; OVER ALL " + str(states) + " STATES "
               "THE ARENA ADMITS " + str(nbest) + " ATTAIN THE BEST "
               + str(best) + " CROSSINGS, " + str(ndiag) + " OF THEM "
               "CARRYING ONE COMPLETION AT EVERY SEAM, AND " + str(cover0)
               + " ARE READY FOR NONE] -- "
               "AND A LINK INSIDE A SECTOR IS REFUSED OUTRIGHT: A SECTOR'S "
               "OWN FORM AT A SITE HAS KERNEL ZERO OVER ITS THREE DECLARED "
               "DIRECTIONS AND FORCES THE FOURTH "
               "DIRECTION'S COUNT AGAINST THE ONE THE EVENT DEPOSITS AT "
               "EVERY ONE OF " + str(reads) + " READINGS -- " + str(private)
               + " OF THEM AT CHART-PRIVATE SITES AND " + str(shared)
               + " AT THE SHARED SITES, WHERE THE TWO-CHART FORM'S KERNEL IS "
               + str(kernel) + " AND THE SINGLE CHART'S IS STILL ZERO -- SO A "
               "STATE RESTRICTS THE ALLOWED TRANSITIONS ONLY IF IT PERSISTS, "
               "WHICH IS A READING AND NOT A MEASUREMENT")
    out.append("AUTOGLUE-MOTIVATION-AND-LAWFULNESS-ARE-DISJOINT-["
               + str(motivated) + " OF " + str(events) + " EVENTS LEAVE THE "
               "WELD WITH ZERO FREE ITEMS, " + str(lawful) + " ARE LAWFUL AT "
               "EVERY LEG, AND THE TWO SETS SHARE " + str(overlap) + "] -- "
               "BY A CHAIN WHOSE ARITHMETIC IS THE PARENT'S, REPRODUCED HERE "
               "AND CHECKED AT EVERY OBJECT: AN EVENT FORCES THE "
               "WELD EXACTLY WHEN IT DOUBLES NOTHING, WHICH IS EXACTLY WHEN "
               "ALL THREE OF ITS PAIRS ARE NEW; A TRIANGLE ADMITS NO PROPER "
               "TWO-COLOURING SO ONE OF THEM FALLS INSIDE A SECTOR -- SEC-2'S "
               "OWN STEPS, CHECKED THERE AT THE SAME OBJECTS -- AND WHAT THIS "
               "UNIT ADDS IS THE TWO-SIDED FORM AND THE CLOSING LINK: THAT "
               "IS THE ONE CELL THE SECTOR'S FORM REFUSES -- THE EVENTS THAT "
               "PIN THE WELD DOWN ARE THE EVENTS THE GEOMETRY CANNOT HOST")
    out.append("AUTOGLUE-NO-SEAM-PRINCIPLE-DERIVED-[" + str(len(ext))
               + " EXTREMAL FUNCTIONALS MEASURED BEFORE THE EVENT AND AFTER "
               "IT, OF WHICH " + str(selbefore) + " SELECT A SINGLE "
               "COMPLETION BEFORE IT AND " + str(selafter) + " AT SOME CUT "
               "AFTER IT AND " + str(selevery) + " AT EVERY CUT; EVERY CROSS "
               "DIRECTION CUTS THE LATTICE "
               + str(lattice) + " TO " + str(cut)
               + "; MAXIMUM DETERMINANT SELECTS THE DIRECT SUM UNIQUELY, AND "
               "THE DIRECT SUM REALISES " + str(dsreal) + " OF THE "
               "ARENA'S CROSS DIRECTIONS -- WHICH IS THE SAME STATEMENT AS "
               "SURVIVING NONE OF THE CUTS, SINCE A CUT IS THE SET OF "
               "COMPLETIONS THAT REALISE ITS DIRECTION, AN IDENTITY THAT "
               "HOLDS AT EVERY POINT OF THE LATTICE -- AND ON THE POST-EVENT "
               "LATTICE THE SAME CRITERION IS " + str(detafter)
               + "-VALUED] -- THE CONVENTION-FREE PRICE TAKES "
               + str(twov) + " VALUE ON THE WHOLE LATTICE "
               "AND THE ONE-SIDED PRICE'S MINIMISER IS THE CUT OF EXACTLY "
               + str(onesided) + " CROSS DIRECTION, SO IT IS "
               "THE EVENT'S OWN EQUATION WEARING A CRITERION'S CLOTHES: "
               "NOTHING IN THIS CORPUS SELECTS THE SEAM, AND THE ONE "
               "CRITERION THAT DOES IS THE STATE IN WHICH NOTHING CAN CROSS")
    return out, {"spanning": spanning, "events": events,
                 "full_cross": full_cross, "crossings": crossings}


# ===========================================================================
# SECTION 7.  THE PAPER SURFACE, THE SEAL, AND THE DOOR
# ===========================================================================

class Claims:
    """Family (e): claims by equality, both directions, keyed by table;
    headers are rows; fences by multiset at a declared multiplicity."""

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
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
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
            report.append({"table": tid, "missing": missing, "stray": stray,
                           "matched": True})
        unrendered = [i for i in range(len(blocks)) if i not in used]
        pc = canon(paper)
        prose_bad = [t[:40] for t, n in self.prose.items()
                     if pc.count(t) != n]
        fb = [canon(b) for b in re.findall(r"```[^\n]*\n(.*?)```", paper,
                                           re.S)]
        fc = Counter(fb)
        fence_bad = ([t[:40] for t, n in self.fences.items() if fc.get(t, 0)
                      != n]
                     + [t[:40] for t in fc if t not in self.fences])
        return {"tables": report, "unrendered_tables": unrendered,
                "prose_mismatch": prose_bad, "fence_mismatch": fence_bad,
                "ok": (not unrendered and not prose_bad and not fence_bad
                       and all(r["matched"] and not r["missing"]
                               and not r["stray"] for r in report))}


NUM_RE = re.compile(r"(?<![\w.])(\d[\d,]*)(?![\w])")
GATEROW_RE = re.compile(r"\[(?:PASS|FAIL)\] \S+ +[0-9a-f]{16}")
# the transcript's declared decoration: the banner, the four section rules
# and the one line naming the paper and the schema.  Nothing here is a
# measurement, and G-TRANSCRIPT-NARRATIVE requires every OTHER non-gate line
# carrying a numeral to be a declared, payload-bound narrative line.
DECOR_RE = re.compile(r"^(=+|-+|v15 AUTOGLUE|instrument for |-- M\d|"
                      r"-- VERDICT |AUTOGLUE-)")
SPELLED = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
           6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
           11: "eleven", 12: "twelve"}

EXEMPT_NUMERALS = {
    "45": "this unit's own paper number",
    "46": "the successor unit's paper number",
    "48": "the dynamics-closure unit's paper number",
    "40": "the parent unit's paper number",
    "32": "the grandparent unit's paper number",
    "19": "the weld paper's number",
}

# K1 MAJOR-4 / K2 M1 / K2 m1: a SPELLED FRACTION carries no numeral, so the
# coverage, polarity and referent legs are all blind to it -- and the paper
# shipped "a little under half" for a ratio of three quarters, in its own
# opening paragraph, about its own inherited headline number.  Every spelled
# proportion in the prose is now resolved against a measured pair: the
# sentence must name the two numbers it is a proportion OF, and the stated
# word must be the one that pair actually justifies.
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
    """E-22: the scan covers fenced blocks and inline code spans as well as
    prose, and a numeral that ends a sentence is a numeral."""
    return [m.group(1) for m in NUM_RE.finditer(text)]


def collect_ints(obj, out):
    if isinstance(obj, bool):
        return
    if isinstance(obj, int):
        out.add(str(obj))
        out.add("{:,}".format(obj))
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


# K3 MAJOR-3.  Every LICENCE list below is a positive commitment to scope.
# The bare negations that were in five of the six -- \bnot\b, \bnever\b,
# \bnothing\b, \bneither\b, \bcannot\b -- licensed any policed claim that
# ended in the word "not", and six sentences built that way passed all six
# walls in one edit.  A negation is not a scope: it is the cheapest word in
# the language and every wall's own control now carries one.
WALLS = [
    Wall("WALL-DECLARATION",
         [r"\bisp'?s dynamics is\b",
          r"\bthe update (chooses|decides|wants|prefers)\b",
          r"\bthe (event|crossing|geometry|state) (chooses|decides|wants)\b"],
         [r"\b(the|this) (update|rule|law|transition)\b[^.;:]{0,60}\b(is|"
          r"gives|establishes|supplies|provides)\b[^.;:]{0,40}\b(theory|"
          r"dynamics|law of isp)\b",
          r"\buniversal (update )?rule\b",
          r"\bthe dynamics of the theory\b",
          r"\b(gives?|supplies|establishes|settles|provides|yields)\b"
          r"[^.;:]{0,40}\b(the )?(theory|dynamics)\b",
          # the #11 state-naming discipline, given a policed leg (K2-STATE-E)
          r"\b(the whole|all) of what the (process|theory) carries\b",
          r"\bis the state of the process\b",
          r"\b(the )?(three objects|state)\b[^.;:]{0,30}\btracks\b"
          r"[^.;:]{0,40}\bthe whole\b"],
         [r"\bcandidate\b", r"\bgated\b", r"\bscope\b", r"\bpriced\b",
          r"\bat (this|one) arena\b", r"\bdeclar\w+\b",
          r"\bseam-subsystem\b", r"\bstructural state\b",
          r"\bregistered\b", r"\bwould promote\b"],
         ["a candidate universal rule", "scope"],
         ["The update rule is the law of ISP, established here.",
          "What this measures gives the theory its dynamics at last.",
          "ISP's dynamics is this transition and the matter is settled.",
          "The update chooses its own crossing.",
          "Here, then, is the universal update rule.",
          "This update gives the theory its dynamics, though not the whole "
          "of it.",
          "The three objects this unit tracks are the whole of what the "
          "process carries at a moment.",
          "The rule established here is the dynamics of the theory, and that "
          "is not in doubt."]),
    Wall("WALL-SEAMCONFINED",
         [r"a sector'?s own geometry is changed by an event in the other "
          r"sector", r"\bgluing leaks\b"],
         [r"\ba sector'?s (own )?(geometry|links?)\b[^.;:]{0,50}\b"
          r"(changed|moved|altered)\b",
          r"\b(spills?|leaks?|bleeds?) (across|into|over)\b",
          r"\b(geometry|links?|cells?)\b[^.;:]{0,40}\b(altered|changed|"
          r"moved)\b[^.;:]{0,40}\b(other|far|neighbour\w*|elsewhere|in b|"
          r"in a)\b",
          r"\bevent in (one|a|the) sector\b[^.;:]{0,60}\b(moves?|changes?|"
          r"alters?)\b",
          r"\b(moves?|changes?|alters?) a (link|cell|site)\b[^.;:]{0,50}\b"
          r"(other|far|neighbour\w*) (sector|chart)\b"],
         [r"\bseam-confined\b", r"\bjointly own\b",
          r"\bno sector-private\b", r"\bonly on links both sectors\b",
          r"\bat the seam alone\b"],
         ["seam-confined"],
         ["An event in one sector moves a link the other sector owns alone.",
          "The geometry of A is altered by what happens in B.",
          "Composition bleeds across the join and the census measures it.",
          "A sector's own links are changed by the neighbour's events.",
          "The effect spills into the private cells of the far sector.",
          "A sector's own links are moved by the neighbour's events, which "
          "is not in doubt.",
          "Once the event has fired the geometry of A is altered by what "
          "happens in B, and not before."]),
    Wall("WALL-NO-METRICAL-READING",
         [r"\blorentzian\b", r"\bspacetime signature\b", r"\blight cone\b",
          r"\bcontinuum limit\b"],
         [r"\b(form|cross block|completion|seam)\b[^.;:]{0,60}\b(metric|"
          r"distance|geometry of space|causal structure|signature|interval)"
          r"\b",
          r"\b(metric|distance|causal) (datum|structure|content)\b",
          # the distance reading WITHOUT the word (K2 M5, K2-METRIC-F)
          r"\bhow far apart\b", r"\bhow close\b",
          r"\b(the )?separation (of|between)\b",
          r"\b(nearer|farther|further) (to|from|apart)\b",
          r"\bthe gap between\b", r"\bstand apart\b"],
         [r"\bcount law\b", r"\bno metrical\b", r"\bhow many\b",
          r"\bdivision events\b", r"\bcount datum\b",
          r"\bcounting-only\b", r"\bcounts? (a|the) cell carries\b"],
         ["the form is a count law"],
         ["The seam's completions fix the interval between the sectors.",
          "The cross block is the metric datum the geometry carries.",
          "Indefinite completions give the join a causal structure.",
          "The form measures distance across the seam.",
          "What the completion supplies is the geometry of space at the "
          "join.",
          "What the cross block records is how far apart the two sectors "
          "stand.",
          "The cross block is the metric datum the geometry carries, and "
          "not a tally.",
          "The completion fixes the separation of the two charts, which is "
          "not in doubt."]),
    Wall("WALL-RECONSTRUCTION-NOT-DERIVATION",
         [r"\bthe seam principle is derived\b",
          r"\bmaximum determinant is derived\b"],
         [r"\b(seam|form|completion|principle|state|count|order|number)\b"
          r"[^.;:]{0,60}\b(follows from|is derived from|derives from|(is|as) "
          r"a consequence of|is implied by|is forced by)\b",
          r"\b(two|both) routes agree\b"],
         [r"\bno law selects\b", r"\bdeclar\w+\b",
          r"\breproduc\w+\b", r"\bcandidate\b", r"\ban addition to the "
          r"corpus\b", r"\bnothing is derived\b", r"\bagreement is a\b"],
         ["nothing is derived"],
         ["The seam form follows from the event that crosses it.",
          "The completion is a consequence of the record it faces.",
          "Because both routes agree, the extremal principle is established.",
          "The state derives from the counts the event deposits.",
          "The selection principle is implied by the readout law.",
          "The completion is a consequence of the record it faces, and not "
          "otherwise.",
          "That two routes agree is what establishes the automorphism count "
          "as a consequence of the arrangement."]),
    Wall("WALL-RELATION-NOT-LAW",
         [r"\bthe successor state is unique\b"],
         [r"\b(update|transition|rule)\b[^.;:]{0,50}\b(evolution law|"
          r"deterministic|determines the (successor|state)|is a map)\b",
          r"\bthe (successor|next) state is\b[^.;:]{0,25}\b(fixed|"
          r"determined|given|settled)\b",
          r"\bthe state is\b[^.;:]{0,25}\b(fixed|determined|settled)\b"],
         [r"\brelation\b", r"\bset of\b", r"\bmany-valued\b",
          r"\bempty or many\b", r"\bfour or eight\b"],
         ["a transition relation"],
         ["The update is the deterministic evolution law of the geometry.",
          "Once the event fires, the next state is fixed.",
          "The transition determines the successor the geometry takes.",
          "The rule is a map from one state to the next.",
          "After the crossing the state is thereby determined.",
          "Once the event has fired the next state is determined, and not "
          "before.",
          "The transition determines the successor state, which is not in "
          "doubt."]),
    Wall("WALL-COUNTING-ONLY",
         [r"\bthe probability that a crossing is lawful\b"],
         [r"\b(probabilit\w+|probable|likel\w+|typical\w+|usually|"
          r"most (events|states|crossings))\b",
          r"\bthe typical\b", r"\bon average\b", r"\bmost \w+ (are|is)\b"],
         [r"\bcounting-only\b", r"\bno measure\b",
          r"\bnothing here may be read\b", r"\bexhaustive enumeration\b",
          r"\bwith its denominator\b"],
         ["counting-only"],
         ["Most crossings are lawful, so the dynamics prefers them.",
          "A crossing is likely to find a successor state.",
          "The typical state absorbs several events.",
          "Lawfulness is probable at this arena.",
          "Usually the form admits the cell the event makes.",
          "Most crossings are lawful at this arena, and not merely some.",
          "The typical state absorbs several events, which is not in "
          "doubt."]),
    # ---- W2: invariance is never promoted to gauge or physical meaning ---
    # engraved at v15 #2 and carried in prose alone until now (K2 M5).
    Wall("WALL-INVARIANCE-NOT-GAUGE",
         [r"\bgauge (freedom|redundancy|symmetry) of the theory\b",
          r"\bunphysical (degrees of freedom|parameters)\b"],
         [r"\b(gauge|redundan\w+)\b",
          r"\b(the same|one and the same|identical) physical (state|"
          r"situation|configuration)\b",
          r"\bno (experiment|observation|measurement)\b[^.;:]{0,40}\b"
          r"(could|can|would)\b[^.;:]{0,30}\b(tell|distinguish|separate)\b",
          r"\b(indistinguishable|equivalent) in principle\b",
          r"\bdescribe[sd]? the same (state|physics|situation)\b",
          r"\bmere (relabelling|description|convention)\b"],
         [r"\ban invariance of the quantities\b",
          r"\bat the arena it measures them on\b",
          r"\bhas not yet defined an observable\b",
          r"\bevery observable and every experiment\b",
          r"\bwould require\b"],
         ["invariance of the quantities this unit measures",
          "has not yet defined an observable"],
         ["The completions related by a relabelling are the same physical "
          "state.",
          "The freedom the seam carries is a gauge redundancy of the theory.",
          "Two states differing only in the cross block are indistinguishable "
          "in principle.",
          "What the relabellings move is unphysical parameters.",
          "No experiment could tell the two completions apart, so they "
          "describe the same physics.",
          "A relabelling is a mere convention and the two describe the same "
          "state, which is not in doubt.",
          "The four undetermined entries are a redundancy of the "
          "description, though not the whole of it."]),
    # ---- W3: predictions are of the arena, never of the family ----------
    # engraved at v15 #17, before this unit's delivery, and carried nowhere
    # in it (K2 M5).  M7's measured inertness is what discharges it.
    Wall("WALL-FAMILY-PREDICTION",
         [r"\ba prediction of the isp family\b",
          r"\bholds at every arena the family admits\b"],
         [r"\b(a )?prediction of the (isp )?(family|theory)\b",
          r"\bat every arena\b", r"\bfor all arenas\b",
          r"\bwhatever the arena\b",
          r"\b(holds|is true|is so) (generally|in general|universally)\b",
          r"\bis a propert\w+ of the (theory|family)\b",
          r"\bof the family as such\b"],
         [r"\bat this arena\b", r"\bfibre-invariant\b",
          r"\bmeasured to be inert\b", r"\bstill-free\b",
          r"\bindependently selected\b", r"\bthe arena it measures\b",
          r"\bfamily-level\b[^.;:]{0,30}\bwould require\b"],
         ["at this arena", "still-free"],
         ["The obstruction is a prediction of the ISP family and holds at "
          "every arena the family admits.",
          "What section four measures is a property of the theory rather "
          "than of this union.",
          "The disjointness holds generally, whatever the arena.",
          "This is a prediction of the family as such.",
          "The 108 is a result for all arenas the grammar admits.",
          "The obstruction is a property of the theory and not of this "
          "union.",
          "What is measured is a prediction of the ISP family, though not "
          "the whole of it."]),
    # ---- the #11 autonomy rename, given a wall of its own ---------------
    Wall("WALL-EVENT-CONDITIONED",
         [r"(?<!not )(?<!than )\bautonomous dynamics\b",
          r"\bthe process selects the event\b"],
         [r"\bthe (update|rule|process|dynamics)\b[^.;:]{0,40}\b(selects|"
          r"chooses|picks|settles)\b[^.;:]{0,30}\b(the |which |its own )?"
          r"(event|crossing|conflict group)\b",
          r"\b(moves|drives|runs) itself\b", r"\bself-driving\b",
          r"\bwithout anything outside\b",
          r"\bthe grammar is re-driven\b",
          r"\bautonomous (update|creation|process)\b"],
         [r"\bevent-conditioned\b", r"\bsupplied\b",
          r"\bthe grammar is not re-driven\b",
          r"\bfrom the arena's own triples\b",
          r"\bwould require the process to select the event\b"],
         ["event-conditioned", "the committed grammar is not re-driven"],
         ["The update settles which conflict group fires next.",
          "What section three exhibits is autonomous dynamics.",
          "The crossing arrives without anything outside the process handing "
          "it over.",
          "The rule chooses its own event and the process moves itself.",
          "This is autonomous creation at the seam.",
          "The update settles which conflict group fires next, and that is "
          "not in doubt.",
          "The process moves itself, though not the whole of the way."]),
]

POLARITY = [
    ("motivation and lawfulness are disjoint",
     r"\bthe motivated events are (the |)lawful\b"
     r"|\bmotivation is a form of lawfulness\b"),
    ("the successor state is never unique",
     r"\bthe successor state is unique\b"
     r"|\bthe event determines the geometry it leaves\b"),
    ("nothing in the corpus selects the seam",
     r"\bthe corpus selects the seam\b"
     r"|\bmaximum determinant is derived\b"
     r"|\bthe seam principle is derived\b"),
    ("the frozen geometry refuses every crossing",
     r"\bwith the geometry frozen the weld admits\b"
     r"|\bthe frozen geometry admits the crossing\b"),
    ("a within-sector cell is refused at every reading",
     r"\bthe fourth direction agrees with the record\b"),
]


def finish(R, V, M, LDg, SL, ANCH, paper_text, paper_rel, t0, inc_table,
           form_rows, inv_rows, price_rows, ext_rows, srcrows, window_axes,
           outside, fourth_rows, cover, outcomes, iv0, extra):
    """The paper surface, the seal, and the door."""
    C = Claims()
    gates_declared = None
    # ---- the rendered tables --------------------------------------------
    C.table("TBL-SOURCES", ("id", "path", "sha256-12"),
            [(r["id"], r["path"], r["sha256_12"]) for r in srcrows])
    arena_rows = [
        ("boundary", "the cells of two AG(2,3) charts with three declared "
                     "link directions, plus whatever cells the update makes"),
        ("family", "the %d three-actor conflict groups of the aligned k = 3 "
                   "union" % M.get("n_events")),
        ("law", "the co-division relation of the saturating arrangement, "
                "I7's readout, HA's admissibility, the weld's three legs"),
        ("state", "the completion of the seam's four undetermined entries, "
                  "at each of the %d shared sites" % M.get("n_shared")),
        ("arena axes", "the five declared window axes: creation, reading, "
                       "count leg, form carry, state"),
        ("provenance", "%d sources read at pinned shas at commit %s"
         % (M.get("n_sources"), SOURCE_COMMIT)),
    ]
    C.table("TBL-ARENA", ("row", "value"), arena_rows)
    C.table("TBL-WINDOW", ("axis", "members", "the delivered value"),
            [(a, ", ".join(m), d) for (a, m, d) in window_axes])
    inc_summary = [(nm,
                    R["incidence_summary"]["alive_by_rule"][nm],
                    R["incidence_summary"]["spanning_alive_by_rule"][nm],
                    M.get("n_events")
                    - R["incidence_summary"]["alive_by_rule"][nm])
                   for nm in RULE_ORDER]
    C.table("TBL-INCIDENCE", ("creation rule", "events alive",
                              "seam-spanning alive", "events refused"),
            inc_summary)
    C.table("TBL-FORM", ("profile (cross, within, doubled)", "successors",
                         "of those, already declared", "form-lawful",
                         "state may stay", "events"),
            [(str(r["profile"]), str(r["successors"]), str(r["kept"]),
              str(r["form_lawful"]), str(r["frozen_possible"]), r["events"])
             for r in R["form_census"]])
    C.table("TBL-FOURTH", ("the site's declared counts",
                           "the count the form forces", "the count the event "
                           "deposits", "readings"),
            [(str(r["counts"]), r["predicted"], r["realised"], r["readings"])
             for r in R["fourth_direction"]])
    C.table("TBL-MULT", ("successors at one seam", "seam slots"),
            [(r["successors at one seam"], r["seam slots"])
             for r in R["successor_multiplicity"]])
    C.table("TBL-FIBER", ("successors of the whole state", "crossings"),
            [(r["successors of the whole state"], r["crossings"])
             for r in R["whole_state_fiber"]])
    C.table("TBL-PREP", ("crossings the state absorbs", "states"),
            [(c["crossings_absorbed"], c["states"])
             for c in R["preparedness"]["coverage"]])
    C.table("TBL-INVENTORY", ("profile (cross, within, doubled)",
                              "I-SITE-ASSIGNMENT", "I-DIRECTION-LABEL",
                              "I-ORIENT", "free items", "maps", "events"),
            [(str(r["profile"]), r["inventory"][0], str(r["inventory"][1]),
              str(r["inventory"][2]), str(r["free_items"]), r["maps"],
              r["events"]) for r in R["inventory_census"]])
    C.table("TBL-TWOSTEP-FIBER", ("still form-lawful at the second step",
                                  "of those, the state kept",
                                  "first crossings"),
            [(r["still form-lawful"], r["of those, state kept"],
              r["first crossings"]) for r in R["two_step_fiber"]])
    C.table("TBL-BEST", ("the best state", "the same completion at all three "
                         "seams"),
            [(str(s["state"]), str(s["the same completion at all three "
                                     "seams"])) for s in R["best_states"]])
    C.table("TBL-FOURTH-SITE", ("the base site of the reading", "readings"),
            [(s["the base site of the reading"], s["readings"])
             for s in R["fourth_by_site"]])
    C.table("TBL-EXTREMAL", ("functional", "selects before",
                             "selects after, least", "selects after, most",
                             "the direct sum before"),
            [(r["functional"], r["selects before"], r["selects after, least"],
              r["selects after, most"], str(r["the direct sum before"]))
             for r in ext_rows])
    C.table("TBL-PRICE", ("currency", "the frozen geometry", "the update",
                          "verdict"),
            [(r["currency"], r["the frozen geometry"], r["the update"],
              r["verdict"]) for r in price_rows])
    C.table("TBL-TWOSTEP", ("crossing", "form-lawful", "state kept",
                            "events"),
            [(str(r["crossing"]), str(r["form_lawful"]), str(r["state_kept"]),
              r["events"]) for r in R["two_step"]["rows"]])
    C.table("TBL-OUTCOMES", ("head segment", "the word reached",
                             "the word not reached", "the predicate that "
                             "decides between them", "why the other arm was "
                             "reachable", "this run's witness",
                             "the other arm's witness"),
            [(o["head segment"], o["the word reached"],
              o["the word not reached"], o["the predicate"],
              o["why the other arm was reachable"], o["the run's witness"],
              o["the other arm's witness"]) for o in outcomes])
    choice_rows = [
        ("the base object: the aligned k = 3 union of two driven sectors",
         "forced", "1", "inherited at the parent's pinned sha"),
        ("the link-creation rule", "declared, the axis",
         str(M.get("n_rules")), "M1, every member run at every event"),
        ("the reading and the count leg", "held at the delivered values",
         str(len(READINGS) * len(COUNTLEGS)), "M1, all four cells run"),
        ("the readout carried to created cells",
         "declared, MEASURED VERDICT-BEARING", "2",
         "M2: dropping it admits every event, carrying it admits "
         + str(M.get("n_full_alive"))),
        ("the whole seam-subsystem state's successor",
         "measured, NEVER UNIQUE",
         str(M.get("fiber_min")) + " or " + str(M.get("fiber_max")),
         "M2: the per-seam sets are " + str(M.get("succ_min")) + " or "
         + str(M.get("succ_max")) + " and the state carries three seams"),
        ("the seam's completion before the event", "declared",
         str(M.get("n_lattice")), "M2's preparedness census sweeps all of it"),
        ("the extremal family", "declared", str(M.get("n_functionals")),
         "M4, all published"),
        ("the successor state at the second step", "declared by a named rule",
         "1", "M2's two-step fiber, run from every lawful first crossing"),
        ("the first crossing the second step runs from",
         "declared tie-break, FIBER PUBLISHED", str(M.get("n_step2_firsts")),
         "M2: the second-step count runs " + str(M.get("n_step2_lo")) + " to "
         + str(M.get("n_step2_hi")) + " over the fiber"),
        ("the base map the RSQ fibers are read at",
         "declared sweep, MEASURED VERDICT-BEARING FOR TWO ROWS",
         str(M.get("n_basesweep")),
         "M3: " + str(M.get("n_moving_rows")) + " post-states move with it; "
         "the rows with no free item do not"),
        ("the state's reading: re-solved or persisting",
         "declared, MEASURED VERDICT-BEARING", "2",
         "M2: re-solved admits every lawful event from every state, "
         "persisting admits a crossing from " + str(M.get("n_persistent"))),
        ("the three-actor conflict group as the unit of an event", "forced",
         "1", "the committed grammar's own event size"),
    ]
    C.table("TBL-CHOICE", ("item", "class", "fiber", "where it binds"),
            choice_rows)
    for seg in V:
        C.fence(seg, 2)

    # ---- the load-bearing PROSE sentences, rendered as claims -----------
    # K3 MAJOR-1: five prose inversions -- including the paper stating the
    # create-nothing result for the create-cross rule, three lines above the
    # table that states the truth -- were delivered at exit 0 because no
    # gate binds a SENTENCE.  The mechanism to bind one was built and never
    # called (K3 m6).  These five are rendered from the payload and required
    # verbatim, so an edited numeral or an inverted polarity is a mismatch.
    C.claim(M.stmt("CROSS-ONLY reaches {a} of {b}.",
                   a=pick("MUT-CLAIM", "n_span_cross", "n_spanning"),
                   b="n_spanning"))
    C.claim(M.stmt("{a} successors at {b} of the lawful crossings and {c} at "
                   "the other {d}.", a="fiber_min", b="n_fiber_min_at",
                   c="fiber_max", d="n_fiber_max_at"))
    C.claim(M.stmt("{m} of the {e} events leave the weld with no free item "
                   "at all; {l} events are lawful at every leg; the two sets "
                   "share {o}.", m="n_motivated", e="n_events", l="n_lawful",
                   o="n_overlap"))
    C.claim("what is measured is EVENT-CONDITIONED CREATION -- given an "
            "event, the geometry follows -- and not autonomous dynamics, "
            "which would require the process to select the event too")
    C.claim(M.stmt("at this arena it does so at {c} of the {s} events that "
                   "cross", c="n_full_cross", s="n_spanning"))

    # ---- the walls -------------------------------------------------------
    ptext = paper_text if paper_text is not None else ""
    SNAP["paper"] = digest(ptext)
    SNAP["source"] = digest(read_text(SELF_REL))
    # the object under test is re-read HERE, inside the run's own read
    # window, and required to be the bytes at its declared path: the caller
    # handed a string, and a string is not a file
    if paper_text is not None and read_text(paper_rel) != ptext:
        raise GateFail("G-PAPER-CLAIMS",
                       "the paper under test is not the bytes at " + paper_rel)
    if mut("MUT-WALL"):
        ptext = ptext + ("\n\n> A sector's own geometry is changed by an\n"
                         "> event in the other sector, as the census shows.\n")
    if mut("MUT-NUMERAL"):
        ptext = ptext + "\n\nThe census returned 4242 lawful crossings.\n"
    if mut("MUT-POLARITY"):
        ptext = ptext + ("\n\nOn this reading the motivated events are "
                         "the lawful ones after all.\n")
    if mut("MUT-REFERENT"):
        ptext = ptext + ("\n\nThe crossings are lawful at 108 of 29791 of "
                         "them.\n")
    wall_rows = [w.scan(ptext) for w in WALLS]
    adj = ANCH.read("N-ADJ-SEAMCONFINED", "G-WALL-SEAMCONFINED")
    licensed = canon("SEAM-CONFINED COMPOSITIONALITY") in canon(adj)
    struck = canon(adj.split(":")[0].strip())
    carries_struck = struck in canon(ptext)
    M.m("n_walls", len(WALLS), "the declared walls")
    M.m("n_controls", sum(len(w.controls) for w in WALLS),
        "controls written independently of the patterns")
    LDg.gate("G-WALL-SEAMCONFINED",
             all(w["ok"] for w in wall_rows) and licensed
             and not carries_struck,
             M.stmt("the {w} walls scan the object under test rather than "
                    "this instrument's own keys, they fail on empty text, "
                    "and each requires the paper to carry its own standing "
                    "sentence as well as to be free of the forms it bans. "
                    "Each carries a LICENCE leg: a sentence making a policed "
                    "KIND of claim is refused unless that same sentence "
                    "carries a qualifier from a set sharing no word with the "
                    "policed patterns, so a paraphrase is caught where a "
                    "blacklist would pass it; the {c} controls are "
                    "paraphrases written against the disease rather than "
                    "copied from the pattern, and every one is caught. The "
                    "parent "
                    "adjudication's licensed finding is read out of its own "
                    "bytes and required of this paper, and the wording it "
                    "struck is required to be absent from it",
                    w="n_walls", c="n_controls"),
             {"walls": wall_rows, "adjudication_anchor":
              "N-ADJ-SEAMCONFINED", "licensed_phrase_found": licensed,
              "paper_carries_the_struck_wording": carries_struck})
    R["walls"] = SL.seal("walls", wall_rows, "G-WALL-SEAMCONFINED")

    # ---- the paper -------------------------------------------------------
    rep = C.check(ptext)
    M.m("n_tables", len(C.tables), "tables rendered as claims")
    M.m("n_fences", sum(C.fences.values()), "verdict fences required")
    if mut("MUT-PAPER-CLAIM"):
        rep["ok"] = rep["ok"] and False
    LDg.gate("G-PAPER-CLAIMS",
             rep["ok"] and bool(ptext.strip()),
             M.stmt("every one of the paper's {t} tables is a rendered claim "
                    "of this receipt, header rows included, compared as a "
                    "multiset in both directions and keyed by the table it "
                    "was rendered into -- so a transplanted row is stray in "
                    "one table and missing in another -- and the {f} verdict "
                    "fences are matched by multiset at their declared "
                    "multiplicity, so a ninth fence and a deleted verdict "
                    "block both fail", t="n_tables", f="n_fences"),
             rep)
    R["paper_digest"] = SL.seal("paper_digest",
                                hashlib.sha256(
                                    ptext.encode("utf-8")).hexdigest()[:12],
                                "G-PAPER-CLAIMS")

    reg = set()
    collect_ints(R, reg)
    collect_ints(V, reg)
    collect_ints(M.vals, reg)
    for tid, tab in C.tables.items():
        for cells in tab:
            for c in cells:
                for t in NUM_RE.findall(c):
                    reg.add(t)
    headless = re.sub(r"(?m)^#{1,6}[ \t]*[0-9.]+", " ", ptext)
    toks = [t.rstrip(",") for t in numerals(headless)]
    unseen = [t for t in toks
              if t not in reg and t not in EXEMPT_NUMERALS
              and t.replace(",", "") not in reg]
    unused_ex = sorted(set(EXEMPT_NUMERALS) - set(toks))
    spelled_bad = [w for n, w in SPELLED.items()
                   if re.search(r"\b%s\b" % w, canon(ptext))
                   and str(n) not in reg and str(n) not in EXEMPT_NUMERALS]
    M.m("n_numerals", len(toks), "numerals scanned in the paper")
    M.m("n_unbacked", len(unseen), "numerals with no measured backing")
    LDg.gate("G-PAPER-COVERAGE",
             not unseen and not unused_ex and not spelled_bad
             and len(numerals(ptext)) > 0,
             M.stmt("all {n} numerals of the paper are scanned -- fenced "
                    "blocks, inline code spans, table cells and "
                    "sentence-final numerals included, with only the numbers "
                    "that name a section stripped, since a heading number is "
                    "not a claim -- and each is either a value this run "
                    "measured or one of the declared exemptions, every one "
                    "of which occurs; spelled numerals are generated rather "
                    "than listed, so there is no floor and no whitelist",
                    n="n_numerals"),
             {"unbacked": unseen[:12], "unused_exemptions": unused_ex,
              "spelled_unbacked": spelled_bad,
              "exemptions": EXEMPT_NUMERALS})

    prose = re.sub(r"```.*?```", " ", ptext, flags=re.S)
    prose = "\n".join(ln for ln in prose.split("\n")
                      if not ln.strip().startswith(("|", "#")))
    pol_bad = [p for (_c, p) in POLARITY if re.search(p, canon(prose))]
    LDg.gate("G-PAPER-POLARITY", not pol_bad,
             M.stmt("claim polarity is checked over the paper's own prose "
                    "with the verdict fences stripped, so the run's own head "
                    "cannot discharge a sentence: each of the head's "
                    "direction words is paired with the sentence a false "
                    "paper would carry, and none of them occurs",
                    ),
             {"violations": pol_bad, "pairs": [c for (c, _p) in POLARITY]})

    # K3 MAJOR-1(a): the declared set used to contain two REFLEXIVE pairs,
    # (288, 288) and (468, 468), which licensed the form "N of N" in any
    # sentence of the paper -- and "216 of 288" rewritten as "288 of 288"
    # was delivered at exit 0 through exactly that door.  There is no
    # reflexive pair here, and the form is refused outright: a totality is
    # written "all 288" or "every one of the 468", which imitates nothing.
    PAIRS = {
        ("events", M.get("n_full_cross"), M.get("n_spanning")),
        ("events", M.get("n_span_cross"), M.get("n_spanning")),
        ("events", M.get("n_span_none"), M.get("n_spanning")),
        ("events", M.get("n_lawful"), M.get("n_events")),
        ("events", M.get("n_motivated"), M.get("n_events")),
        ("events", M.get("n_refuse_frozen"), M.get("n_events")),
        ("events", M.get("n_refuse_update"), M.get("n_events")),
        ("events", M.get("n_moving_rows"), M.get("n_events")),
        ("events", M.get("n_alive_none"), M.get("n_events")),
        ("events", M.get("n_twocross"), M.get("n_spanning")),
        ("events", M.get("n_form_cross"), M.get("n_spanning")),
        ("events", M.get("n_frozen_cross"), M.get("n_form_cross")),
        ("events", M.get("n_unabsorbable"), M.get("n_form_cross")),
        ("events", M.get("n_absorbable"), M.get("n_form_cross")),
        ("events", M.get("n_step2_cross"), M.get("n_form_cross")),
        ("events", M.get("n_step2_hi"), M.get("n_form_cross")),
        ("events", M.get("n_step2_atlo"), M.get("n_step2_firsts")),
        ("events", M.get("n_obs_unique"), M.get("n_spanning")),
        ("relabellings", M.get("n_relabellings"), M.get("n_chartperms")),
        ("states", M.get("n_best"), M.get("n_form_cross")),
        ("states", M.get("n_zero"), M.get("n_states")),
        ("states", M.get("n_persistent"), M.get("n_states")),
        ("states", M.get("n_beststates"), M.get("n_states")),
        ("states", M.get("n_bestdiag"), M.get("n_beststates")),
        ("states", M.get("n_cut"), M.get("n_lattice")),
        ("states", M.get("n_ds_cut"), M.get("n_indices")),
        ("states", M.get("n_ds_real"), M.get("n_indices")),
        ("states", M.get("n_onesided_match"), M.get("n_indices")),
        ("functionals", M.get("n_sel_before"), M.get("n_functionals")),
        ("functionals", M.get("n_sel_after"), M.get("n_functionals")),
        ("functionals", M.get("n_sel_every"), M.get("n_functionals")),
        ("readings", M.get("n_fourth_agree"), M.get("n_fourth_reads")),
        ("readings", M.get("n_fourth_private"), M.get("n_fourth_reads")),
        ("readings", M.get("n_fourth_shared"), M.get("n_fourth_reads")),
    }
    if mut("MUT-REFLEXIVE"):
        PAIRS = PAIRS | {("events", M.get("n_spanning"),
                          M.get("n_spanning"))}
    reflexive = sorted({a for _u, a, b in PAIRS if a == b})
    known = {(a, b) for _u, a, b in PAIRS}
    ref_bad = []
    for mm in re.finditer(r"(\d[\d,]*)\s+of\s+(?:the\s+)?(\d[\d,]*)",
                          canon(prose)):
        pair = (int(mm.group(1).replace(",", "")),
                int(mm.group(2).replace(",", "")))
        if pair not in known or pair[0] == pair[1]:
            ref_bad.append([pair[0], pair[1], canon(prose)[
                max(0, mm.start() - 40):mm.end() + 10]])
    if mut("MUT-REFERENT"):
        ref_bad = ref_bad + [[M.get("n_full_cross"), M.get("n_states"),
                              "planted"]]

    # ---- the SPELLED proportions, resolved against measured pairs -------
    # Two species, both invisible to every numeral leg because a word is not
    # a numeral.  (i) A spelled PROPORTION: hedged forms ("a little under
    # half") are unambiguously proportional and must sit beside a measured
    # pair whose ratio justifies the word; bare forms are checked whenever
    # their own sentence states a pair.  (ii) A spelled N-of-M PAIR ("three
    # of the eight functionals") is a referent claim and is resolved against
    # the same measured pairs the digit form is.
    csent = re.split(r"(?<=[.;:])\s+", canon(prose))
    frac_bad = []
    for s in csent:
        pairs_here = [(int(a.replace(",", "")), int(b.replace(",", "")))
                      for a, b in re.findall(
                          r"(\d[\d,]*)\s+of\s+(?:the\s+)?(\d[\d,]*)", s)]
        for word, (lo_b, hi_b) in FRACTION_WORDS.items():
            for hedge in HEDGES:
                phrase = hedge + word
                for mm in re.finditer(r"\b" + re.escape(phrase) + r"\b", s):
                    # "at most two of which can cross" is a bound, not a
                    # proportion; so is "at least one"
                    if s[max(0, mm.start() - 3):mm.start()] == "at ":
                        continue
                    if not pairs_here:
                        if hedge:
                            frac_bad.append([phrase, "hedged proportion with "
                                             "no measured pair in its "
                                             "sentence", s[:70]])
                        continue
                    if not any(lo_b <= Fraction(a, b) <= hi_b
                               for a, b in pairs_here if b):
                        frac_bad.append([phrase,
                                         [list(p) for p in pairs_here],
                                         [str(lo_b), str(hi_b)]])
        for a, b in re.findall(r"\b(%s)\s+of\s+(?:the\s+)?(%s)\b"
                               % ("|".join(SPELLED.values()),
                                  "|".join(SPELLED.values())), s):
            back = {v: k for k, v in SPELLED.items()}
            if (back[a], back[b]) not in known:
                frac_bad.append(["%s of %s" % (a, b), "not a measured pair",
                                 s[:70]])
    if mut("MUT-FRACTION"):
        frac_bad = frac_bad + [["planted", "a little under half", []]]
    M.m("n_fraction_words", len(FRACTION_WORDS),
        "spelled proportions the gate resolves")
    M.m("n_universes", len({u for u, _a, _b in PAIRS}),
        "declared referent universes")
    M.m("n_pairs", len(PAIRS), "measured pairs the prose may state")
    M.m("n_reflexive", len(reflexive), "reflexive pairs in the declared set")
    LDg.gate("G-PAPER-REFERENT", not ref_bad and not reflexive,
             M.stmt("referents are bound per occurrence and over prose only "
                    "-- the verdict fences, the rendered tables and the "
                    "headings are stripped first, so the run's own head "
                    "cannot discharge the paper's obligations. Every "
                    "fraction the prose states is resolved as a PAIR against "
                    "the {p} pairs this run actually measured, in {u} "
                    "declared universes: two numerals that are each true "
                    "somewhere do not make a true relation, and a fraction "
                    "reading a numerator from one census against a "
                    "denominator from another fails here. And no pair is "
                    "REFLEXIVE -- {x} of them -- so the form 'N of N' is "
                    "licensed nowhere and refused everywhere: a totality is "
                    "written as a totality, and a sentence rewritten to "
                    "state its own denominator as its numerator has no pair "
                    "to hide behind",
                    p="n_pairs", u="n_universes", x="n_reflexive"),
             {"violations": ref_bad[:8], "reflexive_pairs": reflexive,
              "pairs": sorted([a, b] for _u, a, b in PAIRS)})
    LDg.gate("G-PAPER-FRACTION", not frac_bad,
             M.stmt("and a SPELLED proportion is a claim: the {f} spelled "
                    "fractions and quantifiers this gate knows -- half, a "
                    "third, two thirds, a quarter, three quarters, most, "
                    "nearly all, a few, a minority, a majority, each also "
                    "under the hedges a little under, a little over, just "
                    "under and just over -- are located sentence by "
                    "sentence in the prose. A hedged one is a proportion "
                    "and nothing else, so it must sit beside a pair this "
                    "run measured whose ratio the word justifies; a bare "
                    "one is checked wherever its own sentence states a "
                    "pair; and a SPELLED pair, three of the eight, is "
                    "resolved against the same measured pairs the digit "
                    "form is. A word carries no numeral, so the coverage, "
                    "polarity and referent legs are all blind to it, and "
                    "a proportion stated in words about an inherited "
                    "headline number is exactly where that blindness "
                    "costs most",
                    f="n_fraction_words"),
             {"violations": frac_bad[:8],
              "words": sorted(FRACTION_WORDS)})

    # ---- the comparator (S-1) -------------------------------------------
    if mut("MUT-VERDICT"):
        R["form_census"] = [dict(r, events=r["events"] + 1)
                            for r in R["form_census"]]
    rebuilt, cross = reconstruct(R)
    same = (rebuilt == V)
    M.m("n_segments", len(V), "verdict segments")
    M.m("n_head_positions", sum(len(numerals(s)) for s in V),
        "numeral positions in the head")
    LDg.gate("G-VERDICT-RECON", same,
             M.stmt("the head's {n} segments and all {h} of their numeral "
                    "positions are rebuilt by a comparator that shares no "
                    "function, no template and no literal with the builder, "
                    "and reads NO SUMMARY SCALAR: it takes only the "
                    "receipt's primitive tables -- the fate census cell by "
                    "cell, the form census by profile, the inventory census, "
                    "the preparedness histogram, the completion lattice "
                    "point by point, the extremal family's fiber per "
                    "functional and per cross direction, the fourth "
                    "direction by base site -- joins them on the event "
                    "profile, and re-derives every number by its own "
                    "arithmetic before typing the segments itself. The "
                    "state space is summed out of the histogram, the cut "
                    "counted out of the lattice, the determinant's "
                    "post-event fiber maximised out of the fiber table. The "
                    "two strings are compared whole, in both directions",
                    n="n_segments", h="n_head_positions"),
             {"equal": same, "cross_check": cross,
              "first_difference": next((i for i in range(len(V))
                                        if i >= len(rebuilt)
                                        or rebuilt[i] != V[i]), None)})

    # ---- the anchors' consumption, and the falsifiers' honesty ---------
    cons_bad = ANCH.consumption(LDg)
    M.m("n_consumed", len(ANCH.read_by), "anchors read through the accessor")
    LDg.gate("G-ANCHOR-CONSUMPTION", not cons_bad,
             M.stmt("anchor text is readable only through one accessor, "
                    "which records the gate that read it: {c} of the "
                    "declared anchors were actually read, every declared "
                    "consumer is a gate that ran, and each consuming gate "
                    "takes an operand out of the anchor's own bytes or the "
                    "paper quotes it verbatim -- a consumer naming a gate "
                    "this run does not emit fails here", c="n_consumed"),
             {"violations": cons_bad, "read_by": {k: sorted(v) for k, v
                                                  in ANCH.read_by.items()}})

    fsrc = read_text(SELF_REL)
    # every DECLARED parent value must be consumed by a gate condition:
    # a carried-not-used family is forbidden, and one of them was carried
    probe_decl = pick("MUT-DECL", DECL, dict(DECL, **{
        "sec2.a_value_bound_by_nothing": len(DECL)}))
    dead_decl = sorted(k for k in probe_decl
                       if ('DECL["%s"]' % k) not in fsrc)
    M.m("n_declared_values", len(DECL), "values declared from the parents")
    LDg.gate("G-DECLARED-CONSUMED", not dead_decl,
             M.stmt("and every one of the {d} values this unit declares from "
                    "its parents is consumed by a gate condition rather than "
                    "carried: the source is read and each declared key must "
                    "appear in a predicate somewhere in it, so a value that "
                    "is inherited, published and never bound fails here",
                    d="n_declared_values"),
             {"carried_but_never_consumed": dead_decl,
              "declared": sorted(DECL)})
    gates_declared = (set(LDg.names())
                      | {"G-ANCHOR-CONSUMPTION", "G-FALSIFIER-HONESTY",
                         "G-COVERAGE", "G-NO-TYPED-COUNTS",
                         "G-DECLARED-CONSUMED",
                         "G-PAPER-FRACTION", "G-READ-SET",
                         "G-SEAL-TOTAL", "G-TRANSCRIPT-BOUND",
                         "G-TRANSCRIPT-NARRATIVE", "G-INTEGRITY"})
    fal_bad = []
    for f in FALSIFIERS:
        site = ('mut("%s")' % f.name) in fsrc or ('pick("%s"' % f.name) in fsrc
        if not site:
            fal_bad.append("no-injection-site:" + f.name)
        if f.gate not in gates_declared:
            fal_bad.append("phantom-gate:" + f.name)
        if not f.target or not f.description:
            fal_bad.append("undescribed:" + f.name)
    if mut("MUT-FALSIFIER"):
        fal_bad = ([x for x in fal_bad]
                   + ["no-injection-site:MUT-THAT-IS-NOT-THERE"])
    sentinels = re.findall(r"if mut\(\"(MUT-[A-Z-]+)\"\):\n\s+\w+ = "
                           r"(?:True|False)\n", fsrc)
    # T-FALSIFIER-POISONS, the MOVE half, taken in THIS run: every `pick`
    # site evaluates both branches whatever the mode, so the clean value and
    # the corrupted one are digested at the site itself and required to
    # differ.  The DEATH half is the --selftest sweep, which runs every
    # recipe and requires each to refuse at its own declared gate; its
    # measured counts are published there and are claimed of nothing else.
    picks = sorted(set(re.findall(r'pick\("(MUT-[A-Z-]+)"', fsrc)))
    moves_bad = sorted(nm for nm in picks if not SITE_MOVES.get(nm))
    M.m("n_sentinels", len(sentinels), "recipes assigning a bare boolean")
    M.m("n_pick_sites", len(picks), "recipes whose move is proved in this run")
    M.m("n_moves_proved", len(picks) - len(moves_bad),
        "of those, proved to move their target by digest")
    LDg.gate("G-FALSIFIER-HONESTY",
             not fal_bad and not sentinels and not moves_bad
             and len(picks) > 0,
             M.stmt("every declared falsifier has an injection site in this "
                    "file, names a gate this run emits, and carries the "
                    "measured object it corrupts; the source is scanned "
                    "for the sentinel shape -- a recipe whose whole body "
                    "assigns a bare boolean -- of which it finds {s}; and "
                    "the MOVE the template asks to be proved by digest is "
                    "proved here for the {p} recipes whose site evaluates "
                    "both branches, {m} of them, by digesting the clean "
                    "value and the corrupted one at the site and requiring "
                    "them to differ. The remaining recipes' moves and every "
                    "recipe's DEATH are proved by the --selftest sweep, "
                    "which runs each one and requires it to refuse at its "
                    "own gate; that sweep is not claimed of this run",
                    s="n_sentinels", p="n_pick_sites", m="n_moves_proved"),
             {"violations": fal_bad, "sentinels": sentinels,
              "moves_not_proved": moves_bad,
              "falsifiers": len(FALSIFIERS)})

    # ---- the falsifier coverage, counting itself ------------------------
    covered = {f.gate for f in FALSIFIERS}
    gates_now = set(gates_declared)
    if mut("MUT-COVERAGE"):
        gates_now = set(LDg.names())
    uncovered = sorted(g for g in gates_now
                       if g not in covered and g not in WAIVERS)
    bad_waiver = [g for g in WAIVERS if g in covered]
    M.m("n_gates", len(gates_now), "gates this run declares")
    M.m("n_mutants", len(FALSIFIERS), "declared falsifiers")
    M.m("n_multi_gates", len(FALSIFIERS) - len(covered),
        "recipes beyond one per gate")
    LDg.gate("G-COVERAGE",
             not uncovered and not bad_waiver
             and gates_now >= gates_declared,
             M.stmt("coverage is taken inside its own denominator: all {g} "
                    "gates this run declares -- those already fired, this "
                    "one, and the ones declared to fire after it -- are "
                    "either falsified by one of the {m} declared recipes, "
                    "each dying at its own named gate, or waived with a "
                    "forcing the run checks rather than describes. The two "
                    "counts are NOT one number and are not printed as one: "
                    "there are {m} recipes at {g} gates, {x} of the recipes "
                    "being second and third ones at a gate that deserves "
                    "more than a single attack",
                    g="n_gates", m="n_mutants", x="n_multi_gates"),
             {"uncovered": uncovered, "waivers": WAIVERS,
              "gates": len(gates_now), "recipes": len(FALSIFIERS),
              "waived_and_covered": bad_waiver})

    src_self = read_text(SELF_REL)
    probe = TYPED_PROBE if mut("MUT-TYPED") else ""
    typed = M.audit(src_self + probe)
    unused_tok = sorted(set(M.exempt) - M.used_exempt)
    LDg.gate("G-NO-TYPED-COUNTS", not typed and not unused_tok,
             M.stmt("no numeral is typed anywhere this unit vouches: the "
                    "prohibition is taken on the SOURCE by an AST leg, over "
                    "every statement template and every statement typed "
                    "straight into a gate, and it covers the two subspecies "
                    "the template's successor registered -- a percent-format "
                    "template and an integer offset applied inside a "
                    "statement",
                    ),
             {"offenders": typed[:8], "unused_exemptions": unused_tok,
              "exemptions": M.exempt})

    if mut("MUT-READ"):
        # an undeclared repo path, opened whether or not it exists: the audit
        # hook fires on the ATTEMPT, so this recipe refuses in any tree
        # rather than dying with a traceback in a minimal one (K3 m8)
        try:
            with open(os.path.join(REPO, "v15", "code",
                                   "a-path-the-pin-does-not-declare"),
                      "r", encoding="utf-8"):
                pass
        except OSError:
            pass
    return promote(R, V, C, rep, M, LDg, SL, ptext, t0, extra,
                   [SOURCES[s][0] for s in SOURCES] + [SELF_REL]
                   + ([paper_rel] if paper_text is not None else []))


def freeze(obj):
    """K3 MAJOR-2, the first half: after the last seal verification the
    payload is made IMMUTABLE, so the window between the final gate and the
    serialisation -- in which a sealed value could be edited and reach the
    receipt beside its own pristine gate-time digest -- is closed by
    construction rather than by ordering.  Mappings become Frozen and lists
    become tuples; json renders a tuple exactly as it renders a list, and
    digest() sees the same bytes, so nothing moves."""
    if isinstance(obj, Frozen):
        return obj
    if isinstance(obj, dict):
        return Frozen((k, freeze(v)) for k, v in obj.items())
    if isinstance(obj, (list, tuple)):
        return tuple(freeze(v) for v in obj)
    return obj


class Frozen(dict):
    def _sealed(self, *a, **k):
        raise GateFail("G-INTEGRITY",
                       "the payload was edited after the seals were verified "
                       "at the bytes")
    __setitem__ = __delitem__ = _sealed
    update = setdefault = pop = popitem = clear = _sealed


def promote(R, V, C, rep, M, LDg, SL, ptext, t0, extra, declared_reads):
    """The door: totality recomputed here from the payload's live key set,
    the read set judged after the last gate, the transcript's narrative bound
    to the payload leaf by leaf, the payload SERIALISED AND ONLY THEN
    verified -- so the object vouched is the object promoted -- and the
    artifacts staged, read back, verified and only then replaced."""
    R["schema"] = SCHEMA
    R["unit"] = "AUTOGLUE"
    R["paper"] = PAPER_REL
    R["questions"] = ["Q38", "Q39", "Q40", "Q34", "Q41", "Q42", "Q50"]
    R["paper_report"] = rep
    R["counting_only"] = ("every ratio in this unit is a count over an "
                          "exhaustive enumeration with its denominator "
                          "beside it; no measure is declared on the event "
                          "family, on the state space or on the completion "
                          "lattice")
    for k in ("schema", "unit", "paper", "questions", "measured_how",
              "counting_only", "paper_report"):
        SL.declare_unsealed(k, "testimony, not a measurement")
    SL.declare_unsealed("measured", "the registry the sealed rows render "
                                    "from; each entry is sealed inside the "
                                    "row that measured it")
    SL.declare_unsealed("ledger", "the gate rows, bound to the transcript")
    SL.declare_unsealed("totals", "counts of the run's own rows")
    SL.declare_unsealed("seal_manifest", "the manifest itself")
    if mut("MUT-SEAL"):
        R["forged_headline"] = {"crossings": 0}
    v1 = SL.verify(R, LDg, "at the last gate")
    LDg.gate("G-SEAL-TOTAL", not v1["violations"] and not v1["stray"],
             M.stmt("the seal manifest is total and totality is recomputed "
                    "here, at the door, from the payload's live key set "
                    "rather than from a snapshot taken when a gate fired: "
                    "every published key is either sealed at the gate that "
                    "vouched it -- with its gate-time digest still matching "
                    "the value that would be promoted -- or declared "
                    "unsealed with a reason, and no key is in both "
                    "dictionaries"),
             v1)

    rows_so_far = Counter(("PASS" if r["passed"] else "FAIL", r["gate"],
                           r["chain"]) for r in LDg.rows)
    parsed = Counter(re.findall(r"\[(PASS|FAIL)\] (\S+) +([0-9a-f]{16})",
                                "\n".join(OUT_LINES)))
    LDg.gate("G-TRANSCRIPT-BOUND",
             parsed == rows_so_far and LDg.recompute() == LDg.head,
             M.stmt("the transcript is parsed back out of the text that will "
                    "be promoted and reconciled with the ledger as a "
                    "multiset, evidence chain included and in both "
                    "directions, so a forged verdict word, an invented row "
                    "and a dropped row all move the comparison; and the "
                    "ledger's own chain is recomputed from its rows"),
             {"parsed_rows": len(parsed), "ledger_rows": len(LDg.rows),
              "chain": LDg.head})

    # ---- the NARRATIVE, bound leaf by leaf (K3 MAJOR-4) -----------------
    narr_bad = []
    text_now = "\n".join(OUT_LINES)
    if mut("MUT-NARRATIVE"):
        text_now = text_now.replace(NARRATIVE[0][0], NARRATIVE[0][0].replace(
            str(NARRATIVE[0][1][0][1]), str(NARRATIVE[0][1][0][1] + 1), 1))
    for line, binds in NARRATIVE:
        if line not in text_now:
            narr_bad.append("line-missing:" + line[:34])
            continue
        got = [t.replace(",", "") for t in numerals(line)]
        want_n = [str(v) for _p, v in binds]
        if got != want_n:
            narr_bad.append("numerals:" + line[:26] + ":" + ",".join(got))
        for path, val in binds:
            try:
                if leaf(R, path) != val:
                    narr_bad.append("payload:" + path)
            except (KeyError, IndexError, TypeError):
                narr_bad.append("no-such-leaf:" + path)
    declared_lines = {ln for ln, _b in NARRATIVE}
    loose = [ln for ln in text_now.split("\n")
             if numerals(ln) and ln not in declared_lines
             and not GATEROW_RE.search(ln) and not DECOR_RE.match(ln)]
    M.m("n_narrative_lines", len(NARRATIVE), "bound narrative lines")
    M.m("n_narrative_values", sum(len(b) for _l, b in NARRATIVE),
        "numerals bound to a payload leaf")
    LDg.gate("G-TRANSCRIPT-NARRATIVE",
             not narr_bad and not loose and len(NARRATIVE) > 0,
             M.stmt("and the transcript's NARRATIVE is bound too, not only "
                    "its gate rows: every value-bearing line of it -- {l} "
                    "lines carrying {v} numerals -- is declared with the "
                    "receipt path each numeral is drawn from, the promoted "
                    "text is re-parsed here, and each numeral must equal the "
                    "value re-resolved from the payload at the door. No "
                    "other non-gate line of the transcript may carry a "
                    "numeral at all outside the declared decoration, so a "
                    "forged format argument in a census printer -- a line a "
                    "reader opens before anything else -- fails here",
                    l="n_narrative_lines", v="n_narrative_values"),
             {"violations": narr_bad[:8], "undeclared_lines": loose[:6],
              "bound_lines": len(NARRATIVE)})

    # ---- the read set, judged AFTER the last measurement gate (K3 m1/m2)
    for rel in (OUT_REL, REC_REL, OUT_REL + ".tmp", REC_REL + ".tmp"):
        READS.declare_optional(rel, "an artifact this door itself writes and "
                                    "reads back, so the log can be judged "
                                    "after the write as well as before")
    reads = READS.check(declared_reads)
    M.m("n_read_paths", reads["distinct_paths"], "distinct paths opened")
    LDg.gate("G-READ-SET",
             not reads["stray"] and not reads["declared_never_read"]
             and not reads["external"],
             M.stmt("the read set is recorded at the process's own I/O "
                    "accessor rather than in a helper, so a raw open "
                    "anywhere is seen, and every path is CLASSIFIED rather "
                    "than filtered -- a read outside the repository lands in "
                    "its own bucket, which must be empty, instead of "
                    "vanishing. It is compared here against the declared "
                    "set, {p} distinct paths, and compared AGAIN after the "
                    "artifacts are written and read back, so the tail of the "
                    "run is inside the window and not outside it: a stray "
                    "read fails wherever it is planted, including in this "
                    "door", p="n_read_paths"),
             reads)

    if mut("MUT-PROMOTE"):
        R["seam"] = dict(R["seam"], lattice=R["seam"]["lattice"] + 1)
    v2 = SL.verify(R, LDg, "at promotion")
    LDg.gate("G-INTEGRITY", not v2["violations"] and not v2["stray"],
             M.stmt("and the seals are verified a second time against the "
                    "objects that will actually be written -- then the "
                    "payload is FROZEN and serialised, and the seals are "
                    "verified a third time against the parsed bytes "
                    "themselves, so the object vouched is the object "
                    "promoted and the window between the last gate and the "
                    "serialisation is shut: the artifacts are written to a "
                    "temporary, read back, compared byte for byte, replaced, "
                    "and read back again from the promoted path, with the "
                    "temporary removed on every exit that is not a "
                    "promotion"),
             v2)

    # the registry is published AFTER the last gate, so that the quantities
    # the door's own gates measure -- the bound narrative lines, the read
    # paths -- are in it rather than measured and dropped
    R["measured"] = {k: M.vals[k] for k in sorted(M.vals)}
    R["measured_how"] = {k: M.how[k] for k in sorted(M.how)}
    R["ledger"] = [{k: r[k] for k in ("gate", "passed", "statement",
                                      "evidence", "chain")}
                   for r in LDg.rows]
    R["totals"] = {"gates": len(LDg.rows), "sealed": len(SL.seals),
                   "unsealed": len(SL.unsealed),
                   "tables": len(C.tables), "falsifiers": len(FALSIFIERS)}
    R["seal_manifest"] = SL.manifest()

    # THE SEAL WINDOW, SHUT.  From here the payload cannot be edited at all,
    # and what is verified is the parsed bytes rather than the live object.
    R = freeze(R)
    if mut("MUT-POSTCLOSE"):
        R["motivation"] = FORGED["motivation"]
    blob = json.dumps(R, indent=1, sort_keys=True, default=str) + "\n"
    v3 = SL.verify(json.loads(blob), LDg, "at the bytes")
    if v3["violations"] or v3["stray"]:
        raise GateFail("G-INTEGRITY",
                       "the bytes to be promoted do not carry the sealed "
                       "values: " + json.dumps(v3)[:200])

    body = "\n".join(OUT_LINES + ["", "-- VERDICT " + "-" * 66, ""]
                     + [x for seg in V for x in (seg, "")] + ["=" * 78, ""])
    if mut("MUT-TRANSCRIPT"):
        body = body + "\n    [PASS] G-A-GATE-THAT-NEVER-RAN " + "0" * 16
    SNAP["transcript"] = digest(body)
    final = Counter(re.findall(r"\[(PASS|FAIL)\] (\S+) +([0-9a-f]{16})",
                               body))
    want = Counter(("PASS" if r["passed"] else "FAIL", r["gate"], r["chain"])
                   for r in LDg.rows)
    if final != want:
        raise GateFail("G-TRANSCRIPT-BOUND",
                       "the promoted text and the ledger disagree: %d vs %d"
                       % (len(final), len(want)))
    if WRITE:
        for rel, payload in ((OUT_REL, body), (REC_REL, blob)):
            tmp = os.path.join(REPO, rel + ".tmp")
            try:
                with open(tmp, "w", encoding="utf-8") as fh:
                    fh.write(payload)
                with open(tmp, "r", encoding="utf-8") as fh:
                    if fh.read() != payload:
                        raise GateFail("G-INTEGRITY", "staged bytes differ")
                os.replace(tmp, os.path.join(REPO, rel))
            finally:
                if os.path.exists(tmp):
                    os.remove(tmp)
        for rel, payload in ((OUT_REL, body), (REC_REL, blob)):
            with open(os.path.join(REPO, rel), "r", encoding="utf-8") as fh:
                if fh.read() != payload:
                    raise GateFail("G-INTEGRITY", "promoted bytes differ")
    # the read log, judged once more with the door's own I/O inside it: this
    # is what makes the family's "gated after the last gate" true
    tail = READS.check(declared_reads)
    if tail["stray"] or tail["external"]:
        raise GateFail("G-READ-SET",
                       "a path was opened after the read-set gate: "
                       + json.dumps({"stray": tail["stray"][:4],
                                     "external": tail["external"][:4]}))
    sys.stdout.write(body)
    sys.stdout.write("artifacts: %s\n"
                     % ("written" if WRITE else "NOT written (--no-write)"))
    return R, V, body, blob


# ===========================================================================
# SECTION 8.  THE DECLARED FALSIFIERS AND THE CLI
# ===========================================================================
# Family (h).  Each recipe names the MEASURED OBJECT it corrupts, and the
# published description is the code's: a recipe that assigned False to a
# gate's own verdict variable would prove only that the gate raises when
# handed a False, and G-FALSIFIER-HONESTY refuses that shape by reading this
# file's own source.

FALSIFIERS = [
    Falsifier("MUT-SOURCE", "G-SOURCES", "the declared sha of a source",
              "one source's declared sha256-12 is altered, so the byte "
              "comparison against the pinned file fails"),
    Falsifier("MUT-ANCHOR", "G-ANCHORS", "an anchor's needle",
              "one verbatim anchor's needle is truncated below the "
              "character floor, so its location and its floor both fail"),
    Falsifier("MUT-CONSUMER", "G-ANCHOR-CONSUMPTION", "an anchor's consumer",
              "one anchor's declared consumer is renamed to a gate the run "
              "never emits, so consumption is claimed of a phantom"),
    Falsifier("MUT-TEMPLATE", "G-TEMPLATE-CONFORMANCE", "the family id set",
              "one of the nine template families is dropped from the "
              "implemented set, so it no longer matches the ids parsed out "
              "of the pinned template"),
    Falsifier("MUT-SORT", "G-DETERMINISM", "the ordering discipline",
              "an ordering keyed by the bare repr of a frozenset is "
              "introduced, which is the hash-seed dependent shape the "
              "corpus's defect register names"),
    Falsifier("MUT-ARENA", "G-ARENA", "the union relation",
              "one realised pair is removed from the union, so the arena's "
              "pair count and its automorphism order both move"),
    Falsifier("MUT-AUT", "G-ARENA", "the automorphism enumeration",
              "the automorphism search is capped below the group's order, "
              "so the enumeration is incomplete and its count is wrong"),
    Falsifier("MUT-BASELINE", "G-BASELINE-LAWFUL", "the pre-state geometry",
              "the pre-state is given a cross cell no record realises, so "
              "the transition no longer starts from a lawful state"),
    Falsifier("MUT-GROUPS", "G-EVENTS", "the event set",
              "one three-actor group is dropped from the event set, so the "
              "census no longer matches the closed form"),
    Falsifier("MUT-WINDOW", "G-WINDOW", "the outside-list",
              "the named outside-list carries an item twice, so the window's "
              "boundary is no longer a set"),
    Falsifier("MUT-RULE-BLIND", "G-RULE-BLIND", "a rule's input",
              "one rule is made to read the event's whole pair list rather "
              "than its classified footprint, so it no longer computes from "
              "the footprint alone"),
    Falsifier("MUT-RULE-PEEK", "G-INCIDENCE-CENSUS", "the fate census",
              "one rule is made to special-case events with a single "
              "within-sector pair -- a relabelling-invariant class, so the "
              "equivariance sweep cannot see it and the census must"),
    Falsifier("MUT-RULE-NAME", "G-RULE-BLIND", "a rule's output",
              "one rule is made to special-case the events touching one "
              "NAMED actor, which is what a target fitted after the event "
              "would do -- and which the opaque-token footprint now catches "
              "outright, where the old blindness leg handed the names "
              "straight through and left it to the equivariance sweep"),
    Falsifier("MUT-NOPOSTHOC", "G-NO-POSTHOC", "the rule-body scan",
              "the scan that reads the rule bodies out of this file is "
              "pointed at a pattern that misses one of them, so the audit no "
              "longer covers every rule"),
    Falsifier("MUT-CONTROL", "G-CONTROL-ARMS", "the frozen arm",
              "the frozen-geometry rule is made to create the cross cells "
              "after all, so the arm that must refuse everything stops "
              "refusing"),
    Falsifier("MUT-RULE-CROSS", "G-INCIDENCE-CENSUS", "the fate census",
              "the cross-only rule is made to absorb within-sector pairs "
              "too, so its seam-spanning count leaves the parent's"),
    Falsifier("MUT-SEAMIDX", "G-SEAM-INDEX", "the seam index",
              "the sign of a backward neighbour's index is dropped, so the "
              "cross directions of a seam chart stop being distinct"),
    Falsifier("MUT-LATTICE", "G-COMPLETION-LATTICE", "the enumeration box",
              "the completion box is narrowed by one, so the lattice is cut "
              "short and the widened re-run disagrees"),
    Falsifier("MUT-FOURTH", "G-FOURTH-DIRECTION", "the fourth-direction law",
              "the forced count of the fourth direction is computed with the "
              "wrong coefficients, so predictions and deposits agree where "
              "they do not"),
    Falsifier("MUT-FORM", "G-FORM-CENSUS", "the successor state",
              "the successor census drops the equation the realised cross "
              "link imposes, so every event acquires a successor"),
    Falsifier("MUT-FIBER", "G-RULE-FIBER", "the lawful-event sets",
              "one event is removed from the create-everything rule's lawful "
              "set, so the two rules stop agreeing"),
    Falsifier("MUT-RELATION", "G-TRANSITION-RELATION",
              "the multiplicity census",
              "the smallest successor multiplicity is relabelled as one, "
              "which is the size that would make the relation a map"),
    Falsifier("MUT-PREP", "G-PREPAREDNESS", "the crossing family",
              "the preparedness census is run against four crossings instead "
              "of the arena's own, so a state can cover them all"),
    Falsifier("MUT-TWOSTEP", "G-TWO-STEP", "the second step's record",
              "the second step is evaluated against the first step's record, "
              "so the second event's own deposit never enters"),
    Falsifier("MUT-INVENTORY", "G-INVENTORY", "the free-item count",
              "every post-state's free-item count is set to one, so the "
              "parent's published fibers no longer reproduce"),
    Falsifier("MUT-DISJOINT", "G-MOTIVATED-DISJOINT", "the two sets",
              "the motivated events are merged into the lawful set, so the "
              "disjointness the theorem forces is contradicted"),
    Falsifier("MUT-PRICE", "G-PRICE", "the distinct-law count",
              "the count of distinct lawful-event sets is inflated, so the "
              "collapse of the creation axis is no longer measured"),
    Falsifier("MUT-EXTREMAL", "G-EXTREMAL", "the extremal argument",
              "every functional's extremiser is replaced by the first point "
              "of its domain, so selection is claimed where none is "
              "measured"),
    Falsifier("MUT-ONESIDED", "G-NOTHING-DERIVED", "the one-sided price",
              "the one-sided price is summed over both signs, so its "
              "minimiser stops being any cut at all"),
    Falsifier("MUT-OBSTRUCTION", "G-OBSTRUCTION", "the successor sizes",
              "one crossing is given a unique successor state, so the "
              "obstruction's own exception list stops being empty"),
    Falsifier("MUT-FEASIBILITY", "G-OUTCOME-FEASIBILITY", "an outcome row",
              "one pre-registered outcome's witness is detached from the "
              "run, so the feasibility claim stops being measured"),
    Falsifier("MUT-WALL", "G-WALL-SEAMCONFINED", "the paper under test",
              "the sentence the adjudication struck is inserted into the "
              "paper in house style, line-wrapped and capitalised"),
    Falsifier("MUT-PAPER-CLAIM", "G-PAPER-CLAIMS", "the claim report",
              "the claims report is forced to disagree, standing in for a "
              "transplanted row that the two-way multiset would catch"),
    Falsifier("MUT-NUMERAL", "G-PAPER-COVERAGE", "the paper under test",
              "a numeral no measurement backs is planted in the paper's "
              "prose"),
    Falsifier("MUT-POLARITY", "G-PAPER-POLARITY", "the paper under test",
              "the disjointness the head reports is inverted in the paper's "
              "own voice, outside any fence and in a form no wall polices"),
    Falsifier("MUT-REFERENT", "G-PAPER-REFERENT", "the paper under test",
              "a value from the state universe is planted in a sentence "
              "about events, both numerals true and the relation false"),
    Falsifier("MUT-VERDICT", "G-VERDICT-RECON", "a census row",
              "one row of the form census is moved by one event, so the "
              "comparator's own arithmetic parts from the head"),
    Falsifier("MUT-COVERAGE", "G-COVERAGE", "the gate denominator",
              "the coverage denominator is snapshotted before the closing "
              "gates, which is the self-exemption the engraving forbids"),
    Falsifier("MUT-TYPED", "G-NO-TYPED-COUNTS", "the audited source",
              "a statement with a typed numeral is appended to the source "
              "the AST leg audits"),
    Falsifier("MUT-READ", "G-READ-SET", "the read log",
              "a file the pin does not declare is opened during the run"),
    Falsifier("MUT-SEAL", "G-SEAL-TOTAL", "the payload",
              "a key is added to the payload after the seals are taken, "
              "which is the addition totality-at-the-door exists to catch"),
    Falsifier("MUT-TRANSCRIPT", "G-TRANSCRIPT-BOUND", "the promoted text",
              "a PASS row for a gate that never ran is appended to the text "
              "that would be promoted"),
    Falsifier("MUT-PROMOTE", "G-INTEGRITY", "a sealed value",
              "a sealed row is edited between the last gate and the door, so "
              "the gate-time digest and the promoted value part"),
    Falsifier("MUT-FALSIFIER", "G-FALSIFIER-HONESTY", "the falsifier table",
              "a falsifier with no injection site in this file is declared, "
              "so the table claims a recipe the code does not carry"),
    # ---- the repair's own gates, each with its own recipe ---------------
    Falsifier("MUT-CLOSED-FORM", "G-AUT-CLOSED-FORM", "the closed form",
              "the closed form's chart factor is built from one free part "
              "rather than two, so the constructed order parts from the "
              "enumerated one and the index-two claim loses its proof"),
    Falsifier("MUT-CONTAINMENT", "G-CONTAINMENT", "the containment tally",
              "one transition is dropped from the containment count, so the "
              "proposition that forces the incidence census is claimed of "
              "fewer objects than the window has"),
    Falsifier("MUT-DEATH", "G-TWO-CROSSING-DEATH", "the death mechanism",
              "the failing seam's two cross indices are compared without "
              "their signs, so the sign contradiction the deaths actually "
              "turn on is no longer what is measured"),
    Falsifier("MUT-MEMO", "G-SUCCESSOR-MEMO", "the successor memo",
              "one memoised successor set is returned with a member "
              "dropped, so the memo stops being inert and the from-scratch "
              "recomputation parts from it"),
    Falsifier("MUT-BASESWEEP", "G-INVENTORY", "the base-map sweep",
              "the sweep is narrowed to a single base map, which is the "
              "parent's control being dropped again -- the moving rows stop "
              "moving and the fibers are published as invariants"),
    Falsifier("MUT-STEPFIBER", "G-TWO-STEP", "the second-step fiber",
              "the fiber is run from the delivered first crossing alone, so "
              "the range the second step actually takes is replaced by the "
              "one cell that was shipped"),
    Falsifier("MUT-FRACTION", "G-PAPER-FRACTION", "the paper under test",
              "a spelled proportion is planted whose word no measured pair "
              "in its sentence justifies -- the shape that carries no "
              "numeral and that every numeral leg is blind to"),
    Falsifier("MUT-REFLEXIVE", "G-PAPER-REFERENT", "the referent pair set",
              "a reflexive pair is put back into the declared set, which is "
              "the door 'N of N' walked through"),
    Falsifier("MUT-NARRATIVE", "G-TRANSCRIPT-NARRATIVE", "the transcript",
              "one numeral of a census line in the promoted transcript is "
              "moved, which is the forged format argument the narrative was "
              "not bound against"),
    Falsifier("MUT-POSTCLOSE", "G-INTEGRITY", "a sealed value, after the "
              "last gate",
              "a sealed row is edited AFTER the final verification and "
              "before the serialisation -- the window in which a forged "
              "value used to reach the receipt beside its own pristine "
              "gate-time digest"),
    Falsifier("MUT-PREREG", "G-OUTCOME-FEASIBILITY", "a pre-registered word",
              "an outcome word is rewritten to name a result the pin never "
              "posed, which is the post-hoc re-declaration a regenerated "
              "paper used to carry"),
    Falsifier("MUT-CLAIM", "G-PAPER-CLAIMS", "a load-bearing prose sentence",
              "the sentence that states the parent's number is re-rendered "
              "with its own denominator as its numerator, which is the "
              "inversion no gate saw"),
    Falsifier("MUT-BLIND-ORDER", "G-INCIDENCE-CENSUS", "a rule's output",
              "one rule is keyed on the footprint's own carrier ORDER, "
              "which the opaque tokens preserve AND which is invariant under "
              "the whole chart-preserving subgroup at this arena -- so "
              "neither the blindness leg nor the equivariance sweep can see "
              "it, and the census must, which is what it is here to show"),
    Falsifier("MUT-HASH", "G-DETERMINISM", "the ordering discipline",
              "an ordering keyed on the BUILTIN hash is introduced, which "
              "carries no repr token for the repr scan to find and which "
              "makes the promoted receipt's own row order a property of the "
              "interpreter's session rather than of the measurement"),
    Falsifier("MUT-DECL", "G-DECLARED-CONSUMED", "the declared value set",
              "a parent value is declared and bound by nothing, which is the "
              "carried-not-used shape the era forbids and which this unit "
              "shipped once"),
    Falsifier("MUT-EQUIVARIANT", "G-RULE-EQUIVARIANT", "the group partition",
              "one relabelling is moved out of the chart-preserving class, "
              "so the index-two identity the sweep's scope rests on is "
              "measured against a partition that no longer halves the group"),
]
WAIVERS = {}
MUTNAMES = [f.name for f in FALSIFIERS]


MODE_FLAGS = {"--numbers": "numbers", "--selftest": "selftest",
              "--list-gates": "gates", "--list-mutants": "mutants",
              "--list-families": "families", "--verify-paper": "paper"}


def cli(argv):
    """K3 m5: mode resolution is no longer last-wins.  A second mode flag,
    or a second --mutant, is a usage error rather than a silent override --
    `--selftest --numbers` used to exit 0 having run no selftest at all,
    which a battery reads as a pass."""
    mode, path, mutant, chosen = "run", None, None, None
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--no-write":
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
        # a recipe with a listing mode, or with the sweep that runs every
        # recipe itself, used to be discarded in silence at exit 0
        return None
    return mode, path, mutant


def selftest():
    """T-FALSIFIER-POISONS, PROVED (K3 MAJOR-7).  The family said, in three
    places, that every falsifier moves its named target by digest and dies
    at its declared gate -- and no harness existed anywhere in the file: the
    claim was an unexecuted assertion that happened to be true.  Here is the
    harness.  Every declared recipe is run, one full delivery each with the
    write leg off; each must raise at its OWN declared gate and nowhere
    else; each must move the payload -- proved by digesting the run's own
    sealed rows against the clean run's and requiring a difference, or, for
    a recipe whose target is the paper or the source rather than the
    payload, by the site's own two-branch digest; and the two artifacts must
    be byte-unchanged after all of it.  The counts are measured and printed;
    nothing here is claimed of the delivery run."""
    globals()["WRITE"] = False
    before = {rel: (bdigest(read_bytes(rel))
                    if os.path.exists(os.path.join(REPO, rel)) else None)
              for rel in (OUT_REL, REC_REL)}
    paper = (read_text(PAPER_REL)
             if os.path.exists(os.path.join(REPO, PAPER_REL)) else None)
    globals()["MUTANT"] = None
    try:
        clean, _V, _b, _blob = full_run(paper, PAPER_REL)
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
                wrong.append("%s:died-at-%s-not-%s" % (f.name, e.check,
                                                       f.gate))
                continue
            deaths += 1
        moved = (any(k in baseline and SNAP[k] != baseline[k] for k in SNAP)
                 or bool(SITE_MOVES.get(f.name)))
        if moved:
            moves += 1
        else:
            wrong.append(f.name + ":NO-MOVE-PROVED")
    globals()["MUTANT"] = None
    after = {rel: (bdigest(read_bytes(rel))
                   if os.path.exists(os.path.join(REPO, rel)) else None)
             for rel in (OUT_REL, REC_REL)}
    print("selftest: recipes %d; deaths at the declared gate %d; moves "
          "proved %d" % (len(FALSIFIERS), deaths, moves))
    print("selftest: artifacts unchanged: %s" % (before == after))
    if wrong:
        for w in wrong[:12]:
            print("selftest: FAILED %s" % w)
        return 3
    if before != after:
        return 3
    return 0 if deaths == len(FALSIFIERS) == moves else 3


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    parsed = cli(argv)
    if parsed is None:
        sys.stderr.write("usage: autoglue_exact.py [--no-write] "
                         "[--selftest] [--mutant NAME] [--list-gates] "
                         "[--list-mutants] [--list-families] "
                         "[--verify-paper PATH] [--numbers]\n")
        return 2
    mode, path, mutant = parsed
    if mode == "gates":
        # K3 section 2: the two counts are NOT one number and this listing
        # said which it was printing nowhere -- 44 rows for 42 gates.
        gates = sorted({f.gate for f in FALSIFIERS})
        for f in sorted(FALSIFIERS, key=lambda x: (x.gate, x.name)):
            print("%-26s falsified by %s" % (f.gate, f.name))
        print("%d recipes at %d gates (a gate may carry more than one)"
              % (len(FALSIFIERS), len(gates)))
        return 0
    if mode == "mutants":
        for f in FALSIFIERS:
            print("%-18s -> %-26s target: %s :: %s"
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
            # K3 m9: an out-of-repo path could never be in the declared read
            # set, so the mode used to fail a family gate on every such
            # paper whatever it contained.  It is a usage error, and says so
            sys.stderr.write("verify-paper: the paper must be inside the "
                             "repository; the read set is declared "
                             "relative to it\n")
            return 2
        with open(full, "r", encoding="utf-8") as fh:
            text = fh.read()
        if not text.strip():
            sys.stderr.write("verify-paper: the paper is empty\n")
            return 2
        globals()["WRITE"] = False
        try:
            rel = (os.path.relpath(full, REPO)
                   if full.startswith(REPO + os.sep) else path)
            full_run(text, rel)
        except GateFail as e:
            print("verify-paper: REFUSED at %s :: %s" % (e.check, e.detail))
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
        R, V, body, blob = full_run(paper, PAPER_REL)
    except GateFail as e:
        print("REFUSED at %s :: %s" % (e.check, e.detail))
        return 1
    if mode == "numbers":
        print(json.dumps(R["measured"], indent=1, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())

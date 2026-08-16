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
    ("N-SEC2-WALL", "A-SEC2",
     "Of the 288 seam-spanning groups, 216 leave the dictionary alive once "
     "the target declares the cross links the event realises",
     "G-INCIDENCE-CENSUS", "PARSED"),
    ("N-SEC2-MOTIVATED", "A-SEC2",
     "And not one of the 216 is MOTIVATED -- not as a tally that came out "
     "that way, but because it cannot come out otherwise.",
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
    "T-FALSIFIER-POISONS": "every falsifier moves its named target by "
                           "digest and dies at its declared gate",
    "T-READ-SET": "reads recorded at the accessor and gated after the last "
                  "gate, order-insensitively",
}


class GateFail(Exception):
    def __init__(self, check, detail):
        super().__init__("%s :: %s" % (check, detail))
        self.check = check
        self.detail = detail


def say(msg=""):
    OUT_LINES.append(msg)


def mut(name):
    return MUTANT == name


def pick(name, normal, corrupted):
    return corrupted if MUTANT == name else normal


def digest(obj):
    blob = json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, default=str)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:16]


def bdigest(b):
    return hashlib.sha256(b).hexdigest()[:12]


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
    hook -- not in a helper, so a raw open() anywhere is seen."""

    def __init__(self):
        self.log = []
        self.exempt = {}

    def install(self):
        def hook(event, args):
            if event == "open":
                p = args[0]
                if isinstance(p, (str, bytes)) and not isinstance(p, bytes):
                    ap = os.path.abspath(p)
                    if ap.startswith(REPO + os.sep):
                        self.log.append(os.path.relpath(ap, REPO))
        sys.addaudithook(hook)

    def declare_exempt(self, rel, reason):
        self.exempt[rel] = reason

    def check(self, declared):
        got = Counter(self.log)
        want = set(declared) | set(self.exempt)
        stray = sorted(k for k in got if k not in want)
        never = sorted(k for k in declared if k not in got)
        unused = sorted(k for k in self.exempt if k not in got)
        return {"stray": stray, "declared_never_read": never,
                "unused_exemptions": unused, "distinct_paths": len(got),
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

# the bare-repr sorts this unit permits, each over a container of TUPLES,
# whose repr is canonical; G-DETERMINISM requires the source to hold no other
SAFE_REPR_SORTS = {
    "actors = sorted(set(amap.values()) | set(bmap.values()), key=repr)",
    "key=repr)}, \"G-EVENTS\")",
    "for k, v in sorted(form_rows.items(), key=repr)]})",
    "key=repr)],",
    "keep.discard(sorted(keep, key=repr)[0])",
    "gg = tuple(sorted(g, key=repr))",
    "for k, v in sorted(inv_rows.items(), key=repr)]})",
    "\"\\n\") if \"key=repr\" in ln})",
}


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

def geometry(cross=(), within=()):
    actors, amap, bmap = gluing_maps(GLUE)
    inc, cells = set(), []
    for chart, mp in (("A", amap), ("B", bmap)):
        for x in SITES:
            for l in LINKS:
                e = frozenset((mp[x], mp[zadd(x, l)]))
                inc.add(e)
                cells.append((chart, x, l, e))
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


def completion_lattice(nA, nB, slack=0):
    """every completion the corpus's own readout admits at this seam type.
    The box is DERIVED from the cross counts themselves; that it does not
    bind is measured, not asserted, by re-running it widened."""
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


def successors(seam, rel, realised_cross):
    """every completion at this seam consistent with the record: admissible
    at the seam's own count vectors, and predicting exactly the count the
    record carries on every realised cross link."""
    nA, nB = seam_counts(seam, rel)
    out = []
    for U in completion_lattice(nA, nB):
        E = uext([[U[0], U[1]], [U[2], U[3]]])
        ok = True
        for p in realised_cross:
            k = cross_index(seam, p)
            if k is None:
                continue
            i, j, s = k
            if mut("MUT-FORM"):
                continue
            if nA[i] + nB[j] - s * E[i][j] != rel[p]:
                ok = False
                break
        if ok:
            out.append(U)
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
    g["ACT"], g["REL"], g["AMAP"], g["BMAP"] = union_relation(GLUE)
    g["INV_A"] = {v: k for k, v in AMAP.items()}
    g["INV_B"] = {v: k for k, v in BMAP.items()}
    g["GROUPS"] = [tuple(ACT[i] for i in gg)
                   for gg in combinations(range(len(ACT)), 3)]
    if mut("MUT-GROUPS"):
        g["GROUPS"] = GROUPS[:-1]
    AUTCACHE.clear()
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
    say("  the aligned union: %d carriers, %d realised pairs, none doubled, "
        "automorphism order %d" % (len(ACT), len(REL), len(perms)))
    say("  the fourth parallel class holds the %d pairs the arrangement does "
        "not declare" % len(FOURTH_PAIRS))
    R["arena"] = SEAL.seal("arena", {
        "points": len(SITES), "classes": len(CLASSES),
        "declared_directions": len(ARRANGEMENT),
        "sector_pairs": len(SECTOR_PAIRS), "fourth_pairs": len(FOURTH_PAIRS),
        "carriers": len(ACT), "pairs": len(REL), "aut": len(perms),
        "doubled": doubled0, "incidence_is_the_support": inc_eq}, "G-ARENA")

    shuffle_ok = all(ekey(e) == ekey(frozenset(list(e)[::-1]))
                     for e in list(REL)[:64])
    body = selfsource()
    decl = body[body.index("SAFE_REPR_SORTS = {"):]
    decl = decl[:decl.index("\n}\n")]
    repr_lines = sorted({ln.strip() for ln in body.replace(decl, "").split(
        "\n") if "key=repr" in ln})
    if mut("MUT-SORT"):
        repr_lines = repr_lines + ["cells = sorted(inc, " + "key=" + "repr)"]
    unsafe = [ln for ln in repr_lines if ln not in SAFE_REPR_SORTS]
    MEAS.m("n_repr_sorts", len(repr_lines), "sorts keyed by a bare repr")
    LD.gate("G-DETERMINISM", shuffle_ok and not unsafe,
            MEAS.stmt("no ordering in this unit is taken on the repr of an "
                      "unordered container, which is the hash-seed dependent "
                      "shape the corpus's own defect register names: every "
                      "such ordering goes through a canonical key, and the "
                      "{n} remaining bare-repr sorts are the declared ones "
                      "over tuples, each named in this file's own frozen "
                      "list -- a new one fails here", n="n_repr_sorts"),
            {"unsafe": unsafe, "declared": sorted(SAFE_REPR_SORTS),
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
                      "pair, count the division events on that pair",
                      n="n_base_cells"),
            {"baseline": {"%s/%s" % k: v for k, v in base.items()},
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
    say("  the event set: %d three-actor conflict groups in %d orbits, %d of "
        "them seam-spanning" % (n_groups, len(orbits), span))
    R["events"] = SEAL.seal("events", {
        "events": n_groups, "orbits": len(orbits), "spanning": span,
        "orbit_sizes": sorted(Counter(len(o) for o in orbits).items()),
        "profiles": sorted(Counter(profile(fps[g]) for g in GROUPS).items(),
                           key=repr)}, "G-EVENTS")

    # ---- M1  THE UPDATE WINDOW ------------------------------------------
    say()
    say("-- M1: THE UPDATE WINDOW " + "-" * 52)
    qtext = ANCH.read("N-PIN-QUESTION", "G-WINDOW")
    window_axes = [
        ("CREATION", list(RULE_ORDER), "NONE"),
        ("READING", list(READINGS), "EMBEDDING and QUOTIENT"),
        ("COUNT LEG", list(COUNTLEGS), "POSITIVE"),
        ("FORM CARRY", ["DROPPED", "CARRIED"], "CARRIED at the seam"),
        ("STATE", ["FROZEN", "RE-SOLVED"], "not posed"),
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

    # the rule is blind to the event: recomputed from a footprint stripped of
    # every name the event carries, and equivariant under the arena's own
    # relabellings.
    blind_bad, equi_bad = [], []
    for g in GROUPS:
        fp = fps[g]
        anon = {"cross": fp["cross"], "within": fp["within"],
                "doubled": fp["doubled"]}
        for nm in RULE_ORDER:
            try:
                if apply_rule(nm, anon) != apply_rule(nm, fp):
                    blind_bad.append(nm)
            except KeyError:
                blind_bad.append(nm)
    KINDPERM = [p for p in perms
                if all(ACT[p[i]][0] == ACT[i][0] for i in range(len(ACT)))]
    MIXING = [p for p in perms if p not in KINDPERM]
    sample = KINDPERM[::max(1, len(KINDPERM) // 64)][:64]
    mixed = MIXING[::max(1, len(MIXING) // 64)][:64]

    def relabel(p):
        return {ACT[i]: ACT[p[i]] for i in range(len(ACT))}

    def image(part, rl):
        return tuple(tuple(sorted((frozenset(rl[x] for x in e) for e in q),
                                  key=ekey)) for q in part)

    chart_free = 0
    for g in GROUPS[::7]:
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
    MEAS.m("n_equi_events", len(GROUPS[::7]), "events swept for equivariance")
    MEAS.m("n_chartperms", len(KINDPERM), "relabellings that keep the charts")
    MEAS.m("n_chartfree", chart_free, "sector-mixing relabellings that move "
                                      "the cross-only rule")
    MEAS.m("n_fullgroup", len(perms), "the union's whole relabelling group")
    LD.gate("G-RULE-BLIND", not blind_bad,
            MEAS.stmt("every rule's output is a function of the event's "
                      "footprint alone: recomputed at all {n} events from a "
                      "footprint carrying no name of the event that made it, "
                      "the four rules return what they returned",
                      n="n_events"),
            {"disagreements": sorted(set(blind_bad))})
    LD.gate("G-RULE-EQUIVARIANT",
            not equi_bad and chart_free == 0
            and len(KINDPERM) * len(RULE_ORDER) // len(READINGS) == len(perms),
            MEAS.stmt("and every rule commutes with the arena's own "
                      "relabellings: swept at {e} events against {p} of the "
                      "{k} automorphisms that keep each chart's actors in "
                      "their own chart, the image of a rule's output is the "
                      "rule's output on the image, so no rule can be "
                      "special-casing an event. The relabellings that do not "
                      "keep the charts are the sector exchange and nothing "
                      "else -- the chart-preserving ones sit at index two -- "
                      "and under those the rules commute as well, at {f} "
                      "exceptions: a crossing stays a crossing when the two "
                      "sectors trade names",
                      e="n_equi_events", p="n_relabellings", k="n_chartperms",
                      f="n_chartfree"),
            {"disagreements": sorted(set(equi_bad)),
             "chart_preserving": len(KINDPERM), "full_group": len(perms),
             "sector_mixing_moves_cross_only": chart_free})

    selfsrc = read_text(SELF_REL)
    pat = pick("MUT-NOPOSTHOC", r"def (rule_\w+)\(fp\):\n((?:    .*\n)+)",
               r"def (rule_c\w+)\(fp\):\n((?:    .*\n)+)")
    rule_src = re.findall(pat, selfsrc)
    banned = ("weld", "fate", "ALIVE", "successors", "verdict", "detect")
    peek = [nm for nm, body in rule_src if any(b in body for b in banned)]
    MEAS.m("n_rule_defs", len(rule_src), "rule bodies found in the source")
    LD.gate("G-NO-POSTHOC", not peek and len(rule_src) == len(RULE_ORDER),
            MEAS.stmt("and no rule can be post hoc: the {n} rule bodies are "
                      "read out of this file's own source and none of them "
                      "mentions the weld, a fate, the successor state or the "
                      "verdict, so no rule in this window can have been "
                      "chosen after seeing whether it worked",
                      n="n_rule_defs"),
            {"bodies": [nm for nm, _b in rule_src], "peeking": peek,
             "banned_terms": list(banned)})

    # the incidence census, per object, at every cell of the window
    inc_rows = Counter()
    fate_by_rule = {nm: Counter() for nm in RULE_ORDER}
    post_cache = {}
    for g in GROUPS:
        for nm in RULE_ORDER:
            fp, geo2, rel2 = advance(g, G0, REL, nm)
            post_cache[(g, nm)] = (geo2, rel2)
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
    LD.gate("G-INCIDENCE-CENSUS",
            span_alive["CROSS-ONLY"] == parent_216 == DECL[
                "sec2.lawful_at_matched"]
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
        say("  %-18s %10d %14d %14d"
            % (nm, alive[nm], span_alive[nm], n_groups - alive[nm]))
    say("  the parent's sentence, parsed: %d of %d lawful at a declared "
        "target" % (parent_216, parent_288))
    inc_table = sorted(({"rule": nm, "reading": rd, "count_leg": cl,
                         "profile": list(pr), "fate": f, "events": c}
                        for (nm, rd, cl, pr, f), c in inc_rows.items()),
                       key=lambda r: (r["rule"], r["reading"],
                                      r["count_leg"], r["profile"]))
    R["incidence_census"] = SEAL.seal("incidence_census", inc_table,
                                      "G-INCIDENCE-CENSUS")
    R["incidence_summary"] = SEAL.seal("incidence_summary", {
        "alive_by_rule": alive, "spanning_alive_by_rule": span_alive,
        "events": n_groups, "cells": ncells}, "G-CONTROL-ARMS")

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
    form_ok, frozen_ok = {}, {}
    fourth_rows = Counter()
    fourth_bad = 0
    for g in GROUPS:
        geo2, rel2 = post_cache[(g, "ALL-NEW")]
        realised = [p for p in rel2 if {x[0] for x in p} == {"A", "B"}]
        sizes, keeps = [], []
        for m in range(len(SHARED)):
            sc = successors(SHARED[m], rel2, realised)
            sizes.append(len(sc))
            keeps.append(sum(1 for U in sc if U in L0))
        # the created cells of the fourth class, read against the record
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
        fourth_bad += agree
        pr = profile(fps[g])
        form_ok[g] = all(s > 0 for s in sizes) and agree == reads
        frozen_ok[g] = all(k > 0 for k in keeps) and agree == reads
        form_rows[(pr, tuple(sizes), tuple(keeps), form_ok[g],
                   frozen_ok[g])] += 1
    n_form_alive = sum(1 for g in GROUPS if form_ok[g])
    n_form_cross = sum(1 for g in GROUPS if form_ok[g] and fps[g]["cross"])
    n_frozen_cross = sum(1 for g in GROUPS
                         if frozen_ok[g] and fps[g]["cross"])
    n_fourth_reads = sum(fourth_rows.values())
    MEAS.m("n_form_alive", n_form_alive, "events with a successor state")
    MEAS.m("n_form_cross", n_form_cross, "crossings among them")
    MEAS.m("n_frozen_cross", n_frozen_cross, "crossings needing no state move")
    MEAS.m("n_fourth_reads", n_fourth_reads, "fourth-direction readings")
    MEAS.m("n_fourth_agree", fourth_bad, "readings where the two agree")
    LD.gate("G-FOURTH-DIRECTION",
            fourth_bad == 0 and n_fourth_reads > 0
            and all(k[1] != k[2] for k in fourth_rows),
            MEAS.stmt("a link inside a sector is a link of the fourth "
                      "parallel class, and an unshared site's form is fixed "
                      "by its own three declared counts with nothing left "
                      "over: the count it forces on that fourth direction is "
                      "read at both ends of every such cell the update "
                      "creates, {r} readings in all, and it agrees with the "
                      "count the event deposits at {a} of them",
                      r="n_fourth_reads", a="n_fourth_agree"),
            {"readings": n_fourth_reads, "agreements": fourth_bad,
             "rows": [{"counts": list(k[0]), "predicted": k[1],
                       "realised": k[2], "readings": v}
                      for k, v in sorted(fourth_rows.items())]})
    two_cross_dead = all(min(k[1]) == 0 for k in form_rows if k[0][0] > 1)
    one_cross_live = all(min(k[1]) > 0 for k in form_rows
                         if k[0] == (1, 0, 2))
    LD.gate("G-FORM-CENSUS",
            n_form_alive > 0 and n_form_cross > 0
            and n_form_cross < span and two_cross_dead and one_cross_live
            and sum(form_rows.values()) == n_groups,
            MEAS.stmt("the form leg is then taken at every one of the {e} "
                      "events, object by object and never by orbit -- the "
                      "chart breaks the symmetry the relation does not -- "
                      "and a successor state exists at all three seams for "
                      "{f} of them, {c} of which put a pair across the seam; "
                      "at {k} of those the state need not move at all",
                      e="n_events", f="n_form_alive", c="n_form_cross",
                      k="n_frozen_cross"),
            {"form_alive": n_form_alive, "crossings": n_form_cross,
             "frozen": n_frozen_cross,
             "rows": [{"profile": list(k[0]), "successors": list(k[1]),
                       "kept": list(k[2]), "form_lawful": k[3],
                       "frozen_possible": k[4], "events": v}
                      for k, v in sorted(form_rows.items(), key=repr)]})
    say()
    say("  the seam: rank %d on %d unknowns, kernel %d; %d completions at the "
        "all-simple seam, all positive definite" % (rank0, len(IDX4), ker0,
                                                    len(L0)))
    say("  the successor state exists at all three seams for %d events, %d of "
        "them crossings; %d need no state move" % (n_form_alive, n_form_cross,
                                                   n_frozen_cross))
    say("  the fourth direction: %d readings, %d agreements"
        % (n_fourth_reads, fourth_bad))
    R["form_census"] = SEAL.seal("form_census",
                                 [{"profile": list(k[0]),
                                   "successors": list(k[1]),
                                   "kept": list(k[2]), "form_lawful": k[3],
                                   "frozen_possible": k[4], "events": v}
                                  for k, v in sorted(form_rows.items(),
                                                     key=repr)],
                                 "G-FORM-CENSUS")
    R["fourth_direction"] = SEAL.seal("fourth_direction",
                                      [{"counts": list(k[0]),
                                        "predicted": k[1], "realised": k[2],
                                        "readings": v}
                                       for k, v in sorted(fourth_rows.items())],
                                      "G-FOURTH-DIRECTION")

    # the two creating rules agree once the form leg binds
    full_alive = {}
    for nm in ("CROSS-ONLY", "ALL-NEW"):
        keep = set()
        for g in GROUPS:
            geo2, rel2 = post_cache[(g, nm)]
            if weld(rel2, geo2, "EMBEDDING", "POSITIVE")["fate"] != "ALIVE":
                continue
            if not form_ok[g]:
                continue
            keep.add(g)
        if mut("MUT-FIBER") and nm == "ALL-NEW":
            keep.discard(sorted(keep, key=repr)[0])
        full_alive[nm] = keep
    same = full_alive["CROSS-ONLY"] == full_alive["ALL-NEW"]
    MEAS.m("n_full_alive", len(full_alive["CROSS-ONLY"]),
           "events lawful at every leg")
    MEAS.m("n_full_cross", sum(1 for g in full_alive["CROSS-ONLY"]
                               if fps[g]["cross"]), "crossings among them")
    LD.gate("G-RULE-FIBER", same and len(full_alive["CROSS-ONLY"]) > 0,
            MEAS.stmt("and the window's creation axis collapses: at the "
                      "complete standard the two rules that create anything "
                      "admit the SAME {n} events, {c} of them crossings, so "
                      "the choice between them is not a price the update "
                      "pays -- it is inert wherever either is lawful",
                      n="n_full_alive", c="n_full_cross"),
            {"cross_only": len(full_alive["CROSS-ONLY"]),
             "all_new": len(full_alive["ALL-NEW"]), "identical": same})

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
    bestn, beststate = -1, None
    LPREP = pick("MUT-PREP", L0, L0[:4])
    for U0 in LPREP:
        for U1 in LPREP:
            s01 = [g for g, s in absorb.items() if U0 in s[0] and U1 in s[1]]
            for U2 in LPREP:
                n = sum(1 for g in s01 if U2 in absorb[g][2])
                cover[n] += 1
                if n > bestn:
                    bestn, beststate = n, (U0, U1, U2)
    MEAS.m("n_states", len(L0) ** len(SHARED), "completions at each seam")
    MEAS.m("n_best", bestn, "the maximum over the state space")
    MEAS.m("n_zero", cover[0], "states ready for no crossing at all")
    MEAS.m("n_crossings", len(absorb), "the arena's crossing events")
    LD.gate("G-PREPAREDNESS",
            sum(cover.values()) == len(L0) ** len(SHARED)
            and bestn < len(absorb) and cover[0] > 0,
            MEAS.stmt("a state declared before the event is ready for only "
                      "part of what can happen: over all {t} states the "
                      "arena admits, the best is ready for {b} of the {f} "
                      "crossings a state can absorb at all -- the rest of "
                      "the {c} seam-spanning events have no successor state "
                      "anywhere -- and {z} states are ready for none. No "
                      "declaration of the seam survives the census",
                      t="n_states", b="n_best", f="n_form_cross",
                      c="n_crossings", z="n_zero"),
            {"states": len(L0) ** len(SHARED), "best": bestn,
             "best_state": [list(u) for u in beststate],
             "ready_for_none": cover[0],
             "coverage": sorted(cover.items())})
    say("  preparedness: over %d states the best absorbs %d of the %d "
        "crossings a state can absorb at all; %d absorb none"
        % (len(L0) ** len(SHARED), bestn, n_form_cross, cover[0]))
    R["preparedness"] = SEAL.seal("preparedness", {
        "states": len(L0) ** len(SHARED), "best": bestn,
        "best_state": [list(u) for u in beststate],
        "ready_for_none": cover[0],
        "coverage": [{"crossings_absorbed": k, "states": v}
                     for k, v in sorted(cover.items())]}, "G-PREPAREDNESS")

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
    first = None
    for g in sorted(absorb, key=ekey):
        if profile(fps[g]) == (1, 0, 2) and form_ok[g]:
            first = g
            break
    geo1, rel1 = post_cache[(first, "CROSS-ONLY")]
    realised1 = [p for p in rel1 if {x[0] for x in p} == {"A", "B"}]
    succ1 = [successors(SHARED[m], rel1, realised1)
             for m in range(len(SHARED))]
    state1 = [min(s, key=lambda U: (sum(abs(x) for x in U), U))
              for s in succ1]
    step2 = Counter()
    for g in GROUPS:
        gg = tuple(sorted(g, key=repr))
        if len(set(gg)) != len(gg):
            continue
        fp2, geo3, rel3 = advance(gg, geo1, rel1, "CROSS-ONLY")
        if mut("MUT-TWOSTEP"):
            rel3 = dict(rel1)
        realised3 = [p for p in rel3 if {x[0] for x in p} == {"A", "B"}
                     and frozenset(p) in geo3["inc"]]
        sizes = [len(successors(SHARED[m], rel3, realised3))
                 for m in range(len(SHARED))]
        keep = all(state1[m] in successors(SHARED[m], rel3, realised3)
                   for m in range(len(SHARED)))
        step2[(len(fp2["cross"]) > 0, all(s > 0 for s in sizes), keep)] += 1
    n2_cross = sum(v for k, v in step2.items() if k[0] and k[1])
    n2_frozen = sum(v for k, v in step2.items() if k[0] and k[1] and k[2])
    MEAS.m("n_step2_cross", n2_cross, "second crossings still form-lawful")
    MEAS.m("n_step2_frozen", n2_frozen, "of those, with the state kept")
    LD.gate("G-TWO-STEP",
            n2_cross < n_form_cross and n2_cross > 0
            and sum(step2.values()) == n_groups,
            MEAS.stmt("the update iterates, and it remembers: from the "
                      "post-state of one lawful crossing, taken at a "
                      "successor named by a declared rule, the second event "
                      "may still cross at {a} of the events that could cross "
                      "first at {b}, and at {c} of them the state survives "
                      "the second event too",
                      a="n_step2_cross", b="n_crossings", c="n_step2_frozen"),
            {"first_event": [str(a) for a in first],
             "successor_sizes": [len(s) for s in succ1],
             "state": [list(u) for u in state1],
             "second_step": [{"crossing": k[0], "form_lawful": k[1],
                              "state_kept": k[2], "events": v}
                             for k, v in sorted(step2.items())]})
    say("  the second step: %d of the events may still cross, %d with the "
        "state kept" % (n2_cross, n2_frozen))
    R["two_step"] = SEAL.seal("two_step", {
        "first_event": [str(a) for a in first],
        "successor_sizes": [len(s) for s in succ1],
        "state": [list(u) for u in state1],
        "second_crossings": n2_cross, "second_frozen": n2_frozen,
        "rows": [{"crossing": k[0], "form_lawful": k[1], "state_kept": k[2],
                  "events": v} for k, v in sorted(step2.items())]},
        "G-TWO-STEP")

    # ---- M3  THE PRICE, AND WHERE MOTIVATION LIVES (Q50) ----------------
    say()
    say("-- M3: THE PRICE AND MOTIVATION " + "-" * 45)
    PERMS3 = list(permutations(range(len(LINKS))))

    def count_field(geo, rel, phi, sperm=None, orient=None):
        sperm = sperm or {"A": tuple(range(len(LINKS))),
                          "B": tuple(range(len(LINKS)))}
        orient = orient or {"A": False, "B": False}
        inv = {v: k for k, v in phi.items()}
        out = {}
        for (chart, x, l, e) in geo["cells"]:
            if chart in ("X", "W"):
                u, v = [inv[t] for t in e]
                out[(chart, ekey(e))] = rel.get(frozenset((u, v)), 0)
                continue
            l2 = LINKS[sperm[chart][LINKS.index(l)]]
            step = zneg(l2) if orient[chart] else l2
            mp = geo["charts"][chart]
            u, v = inv[mp[x]], inv[mp[zadd(x, step)]]
            out[(chart, x, l)] = rel.get(frozenset((u, v)), 0)
        return out

    def fkey(f):
        return tuple(sorted((repr(k), v) for k, v in f.items()))

    def inventory(rel, geo):
        """the RSQ choice inventory at the bare carrier: the number of
        distinct count fields the admissible maps produce, and the fibers of
        the two per-chart relabellings."""
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
        phi = {ACT[i]: ACT[perms2[0][i]] for i in range(len(ACT))}
        labs = {fkey(count_field(geo, rel, phi, {"A": pa, "B": pb}))
                for pa in PERMS3 for pb in PERMS3}
        oris = {fkey(count_field(geo, rel, phi, None, {"A": oa, "B": ob}))
                for oa in (False, True) for ob in (False, True)}
        inv = (len(orb), len(labs), len(oris))
        return {"maps": len(perms2), "complete": complete, "inventory": inv,
                "free_items": sum(1 for v in inv if v > 1)}

    iv0 = inventory(REL, G0)
    inv_rows = Counter()
    motivated, lawful = set(), set()
    for g in GROUPS:
        geo2, rel2 = post_cache[(g, "ALL-NEW")]
        iv = inventory(rel2, geo2)
        if mut("MUT-INVENTORY"):
            iv["free_items"] = 1
        pr = profile(fps[g])
        inv_rows[(pr, iv["inventory"], iv["free_items"], iv["maps"])] += 1
        if iv["free_items"] == 0:
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
    MEAS.m("free_union", iv0["free_items"], "the event-free union's fibers")
    LD.gate("G-INVENTORY",
            iv0["free_items"] == DECL["sec2.union_no_crossing.free"]
            and iv0["maps"] == DECL["sec2.union_no_crossing.maps"]
            and any(k[0] == (1, 0, 2) and k[3] == DECL["sec2.shared_seeded.maps"]
                    and k[2] == DECL["sec2.shared_seeded.free"]
                    for k in inv_rows)
            and any(k[0] == (2, 0, 1) and k[3] == DECL["sec2.b_seeded.maps"]
                    and k[2] == DECL["sec2.b_seeded.free"]
                    for k in inv_rows)
            and sum(inv_rows.values()) == n_groups,
            MEAS.stmt("the weld's forcing is measured at every one of the {e} "
                      "post-states, not at a chosen few: the event-free union "
                      "has {f} free items, and the two crossings the parent "
                      "priced by hand reappear here at the fibers it "
                      "published, from a route that enumerates the orbit of "
                      "the record's own non-unit configuration rather than "
                      "the maps",
                      e="n_events", f="free_union"),
            {"union": iv0,
             "rows": [{"profile": list(k[0]), "inventory": list(k[1]),
                       "free_items": k[2], "maps": k[3], "events": v}
                      for k, v in sorted(inv_rows.items(), key=repr)]})
    say()
    say("  the event-free union: %d maps, fibers %s, free items %d"
        % (iv0["maps"], iv0["inventory"], iv0["free_items"]))
    say("  motivated %d of %d events; lawful at every leg %d; the two sets "
        "share %d" % (len(motivated), n_groups, len(lawful), len(overlap)))
    R["inventory_census"] = SEAL.seal("inventory_census",
                                      [{"profile": list(k[0]),
                                        "inventory": list(k[1]),
                                        "free_items": k[2], "maps": k[3],
                                        "events": v}
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
    LD.gate("G-MOTIVATED-DISJOINT",
            not overlap and not thm_bad and len(motivated) > 0
            and len(lawful) > 0 and "cannot come out otherwise" in motiv,
            MEAS.stmt("motivation and lawfulness are disjoint at this arena, "
                      "and not as a tally: {m} of the events leave the weld "
                      "with no free item and {l} are lawful at every leg, and "
                      "no event is in both sets. The mechanism is checked at "
                      "every object -- an event leaves the weld forced "
                      "exactly when it doubles nothing, which is exactly when "
                      "all three of its pairs are new; three actors give "
                      "three pairs and at most two can cross, since a "
                      "triangle admits no proper two-colouring, so such an "
                      "event always opens a pair inside a sector, and that is "
                      "the cell the sector's own form refuses",
                      m="n_motivated", l="n_lawful"),
            {"motivated": len(motivated), "lawful": len(lawful),
             "overlap": len(overlap), "theorem_violations": thm_bad[:8]})

    # the five currencies, every entry computed
    refusals = {nm: n_groups - alive[nm] for nm in RULE_ORDER}
    lawful_free = sorted({k[2] for k in inv_rows
                          if k[0] == (1, 0, 2)})
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
    price_rows = [
        {"currency": "refutability: events the weld refuses",
         "the frozen geometry": refusals["NONE"],
         "the update": n_groups - len(full_alive["CROSS-ONLY"]),
         "verdict": "PART SPENT"},
        {"currency": "forcing: free items at a lawful crossing",
         "the frozen geometry": iv0["free_items"],
         "the update": lawful_free[-1], "verdict": "SPENT"},
        {"currency": "the state: completions the seam may carry",
         "the frozen geometry": len(L0), "the update": lawful_succ[-1],
         "verdict": "NARROWED"},
        {"currency": "the structure: fourth-class cells creatable",
         "the frozen geometry": len(G0["within"]),
         "the update": within_cells, "verdict": "REFUSED BY THE FORM"},
        {"currency": "the declaration: objects the route declares",
         "the frozen geometry": span, "the update": distinct_laws,
         "verdict": "BOUGHT"},
    ]
    LD.gate("G-PRICE",
            len(price_rows) == len({r["currency"] for r in price_rows})
            and all(isinstance(r["the update"], int) for r in price_rows)
            and distinct_laws == 1 and lawful_free[-1] > iv0["free_items"],
            MEAS.stmt("the price is censused in five currencies, each read "
                      "against the frozen geometry the parent left: the "
                      "update refuses {ru} events where the frozen geometry "
                      "refuses {rf}; it costs the weld's forcing, {ff} free "
                      "items against {fu}; it narrows the seam from {sl} "
                      "completions to at most {sm}; the fourth-class cells it "
                      "would create, {wc} of them, the form refuses "
                      "outright; and where the parent's route declares one "
                      "target per seam-spanning event, {sp} of them, this one "
                      "declares {nl} law",
                      ru="n_refuse_update", rf="n_refuse_frozen",
                      ff="free_lawful", fu="free_union", sl="n_lattice",
                      sm="succ_max", wc="n_within_cells", sp="n_spanning",
                      nl="n_laws"),
            {"rows": price_rows, "distinct_laws": distinct_laws})
    say()
    for r in price_rows:
        say("  %-44s %8s %8s  %s"
            % (r["currency"], r["the frozen geometry"], r["the update"],
               r["verdict"]))
    R["price"] = SEAL.seal("price", price_rows, "G-PRICE")
    R["motivation"] = SEAL.seal("motivation", {
        "motivated": len(motivated), "lawful": len(lawful),
        "overlap": len(overlap),
        "union_free_items": iv0["free_items"],
        "union_maps": iv0["maps"]}, "G-MOTIVATED-DISJOINT")

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
    ext_rows = []
    for nm, f in FUNCTIONALS:
        pre = argext(f, L0)
        post = [len(argext(f, cuts[k])) for k in IDXALL]
        ext_rows.append({"functional": nm, "selects before": len(pre),
                         "selects after, least": min(post),
                         "selects after, most": max(post),
                         "the direct sum before": (0, 0, 0, 0) in pre})
    dettext = ANCH.read("N-SEC2-DET", "G-EXTREMAL")
    detrow = [r for r in ext_rows if r["functional"].startswith("maximum det")][0]
    MEAS.m("n_functionals", len(FUNCTIONALS), "the declared extremal family")
    MEAS.m("n_cut", cutsizes[0], "completions surviving one crossing")
    MEAS.m("n_ds_cut", ds_in_cut, "cuts retaining the direct sum")
    MEAS.m("n_ds_real", ds_realises, "crossings the direct sum can realise")
    MEAS.m("n_det_after", detrow["selects after, most"],
           "the determinant's post-event fiber")
    LD.gate("G-EXTREMAL",
            len(cutsizes) == 1
            and cutsizes[0] == DECL["sec2.aligned_after_crossing"]
            and detrow["selects before"] == 1 and detrow["the direct sum "
                                                         "before"]
            and ds_in_cut == 0 and ds_realises == 0
            and detrow["selects after, most"] > 1
            and "returns the direct sum and nothing else" in dettext,
            MEAS.stmt("the derivation is attempted against {f} declared "
                      "extremal functionals, before the event and after it. "
                      "Every one of the arena's cross directions cuts the "
                      "lattice to the same {c} completions. Maximum "
                      "determinant is the one criterion the parent found "
                      "selective, and the dynamics refutes it twice: the "
                      "completion it returns is the one state under which no "
                      "crossing can be realised at all, {r} of them, and it "
                      "survives {d} of the cuts; on the post-event lattice "
                      "the same criterion is {a}-valued",
                      f="n_functionals", c="n_cut", r="n_ds_real",
                      d="n_ds_cut", a="n_det_after"),
            {"rows": ext_rows, "cut_sizes": cutsizes,
             "direct_sum_in_cuts": ds_in_cut,
             "direct_sum_realises": ds_realises})
    say()
    say("  every cross direction cuts the lattice %d -> %d; the direct sum "
        "survives %d of the cuts and realises %d crossings"
        % (len(L0), cutsizes[0], ds_in_cut, ds_realises))
    for r in ext_rows:
        say("    %-30s selects %2d before, %2d to %2d after"
            % (r["functional"], r["selects before"],
               r["selects after, least"], r["selects after, most"]))
    R["extremal"] = SEAL.seal("extremal", ext_rows, "G-EXTREMAL")
    R["cut_size"] = SEAL.seal("cut_size", cutsizes[0], "G-EXTREMAL")
    R["ds_realises"] = SEAL.seal("ds_realises", ds_realises, "G-EXTREMAL")
    R["ds_in_cut"] = SEAL.seal("ds_in_cut", ds_in_cut, "G-EXTREMAL")

    onesided = argext(pick("MUT-ONESIDED", FUNCTIONALS[5][1],
                           FUNCTIONALS[4][1]), L0)
    matches = [k for k in IDXALL if set(cuts[k]) == set(onesided)]
    twosided = {sum(ccs(U).values()) for U in L0}
    MEAS.m("n_onesided_match", len(matches), "indices whose cut it equals")
    MEAS.m("n_twosided", len(twosided), "values of the two-sided price")
    LD.gate("G-NOTHING-DERIVED",
            len(matches) == 1 and len(twosided) == 1
            and pdcount == len(L0)
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
                      "clothes",
                      n="n_lattice", t="n_twosided", m="n_onesided_match"),
            {"one_sided_matches": [list(k) for k in matches],
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
    outcomes = [
        {"outcome": "TARGET-FREE-EVENT-CONDITIONED-CREATION-EXISTS",
         "reached": len(full_alive["CROSS-ONLY"]) > 0,
         "why it was reachable": "the create-everything rule makes the "
                                 "geometry's incidence the record's own "
                                 "support, so the weld cannot refuse",
         "the run's witness": alive["ALL-NEW"]},
        {"outcome": "BLOCKED-AT-THE-DECLARED-DATUM",
         "reached": bestn < len(absorb),
         "why it was reachable": "with the geometry frozen the parent's wall "
                                 "stands and every seam-spanning event is "
                                 "refused",
         "the run's witness": pick("MUT-FEASIBILITY",
                                   span - span_alive["NONE"], span - 1)},
    ]
    MEAS.m("n_outcomes", len(outcomes), "the pre-registered outcome words")
    LD.gate("G-OUTCOME-FEASIBILITY",
            all(isinstance(o["reached"], bool) for o in outcomes)
            and any(o["reached"] for o in outcomes)
            and outcomes[0]["the run's witness"] == n_groups
            and outcomes[1]["the run's witness"] == span,
            MEAS.stmt("both pre-registered outcome words were reachable at "
                      "the committed corpus before anything was measured, and "
                      "each carries the run's own witness: {n} of them, and "
                      "the two witnesses are the arms of the same runner",
                      n="n_outcomes"),
            {"outcomes": outcomes})
    R["outcomes"] = SEAL.seal("outcomes", outcomes, "G-OUTCOME-FEASIBILITY")

    # ---- THE VERDICT ----------------------------------------------------
    V = build_verdict(MEAS, {
        "full_alive": MEAS.get("n_full_alive"),
        "full_cross": MEAS.get("n_full_cross"),
        "spanning": span, "events": n_groups,
        "parent_lawful": span_alive["CROSS-ONLY"],
        "alive_all": alive["ALL-NEW"],
        "unique": len(obs_bad), "frozen": n_frozen_cross,
        "states": len(L0) ** len(SHARED), "best": bestn, "zero": cover[0],
        "reads": n_fourth_reads, "motivated": len(motivated),
        "lawful": len(lawful), "overlap": len(overlap),
        "functionals": len(FUNCTIONALS), "lattice": len(L0),
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
        "FOUR LINK-CREATION RULES BY TWO READINGS BY TWO COUNT LEGS AT EVERY "
        "ONE OF {ev} THREE-ACTOR EVENTS AND AT BOTH ENDS OF EVERY "
        "TRANSITION, THE RULE FIRING ON THE EVENT'S FOOTPRINT ALONE, NO "
        "TARGET DECLARED AFTER ANY EVENT; WITH THE GEOMETRY FROZEN THE WELD "
        "REFUSES ALL {sp} SEAM-SPANNING EVENTS AND WITH EVERY NEW PAIR "
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
            pl=v["parent_lawful"]))
    seg.append(
        "AUTOGLUE-A-TRANSITION-RELATION-ON-THE-SEAM-SUBSYSTEM-STATE-NOT-"
        "AN-EVOLUTION-LAW-THE-DATUM-THAT-CANNOT-PRECEDE-THE-EVENT-IS-THE-"
        "SEAM'S-CROSS-BLOCK-[THE FOUR "
        "UNDETERMINED ENTRIES OF THE DIRECT-SUM FORM AT EACH SHARED SITE, "
        "OVER THE DECLARED UPDATE WINDOW; THE "
        "SUCCESSOR STATE CENSUSED AT EVERY ONE OF {ev} EVENTS OBJECT BY "
        "OBJECT AND NEVER BY ORBIT: EMPTY OR MANY-VALUED, UNIQUE AT {uq}; "
        "{fr} OF THE {fc} LAWFUL CROSSINGS NEED NO STATE MOVE; OVER ALL "
        "{st} STATES THE ARENA ADMITS THE BEST IS READY FOR {bs} CROSSINGS "
        "AND {zr} ARE READY FOR NONE] -- AND A LINK INSIDE A SECTOR IS "
        "REFUSED OUTRIGHT: AN UNSHARED SITE'S FORM HAS KERNEL ZERO AND "
        "FORCES THE FOURTH DIRECTION'S COUNT AGAINST THE ONE THE EVENT "
        "DEPOSITS AT {rd} OF {rd} READINGS -- SO A STATE RESTRICTS THE "
        "ALLOWED TRANSITIONS ONLY IF IT PERSISTS, WHICH IS A READING AND "
        "NOT A MEASUREMENT".format(
            ev=v["events"], uq=v["unique"], fr=v["frozen"],
            fc=v["full_cross"], st=v["states"], bs=v["best"], zr=v["zero"],
            rd=v["reads"]))
    seg.append(
        "AUTOGLUE-MOTIVATION-AND-LAWFULNESS-ARE-DISJOINT-[{mo} OF {ev} "
        "EVENTS LEAVE THE WELD WITH ZERO FREE ITEMS, {lw} ARE LAWFUL AT "
        "EVERY LEG, AND THE TWO SETS SHARE {ov}] -- BY A THEOREM CHECKED AT "
        "EVERY OBJECT: AN EVENT FORCES THE WELD EXACTLY WHEN IT DOUBLES "
        "NOTHING, WHICH IS EXACTLY WHEN ALL THREE OF ITS PAIRS ARE NEW; A "
        "TRIANGLE ADMITS NO PROPER TWO-COLOURING SO ONE OF THEM FALLS "
        "INSIDE A SECTOR; AND THAT IS THE ONE CELL THE FORM REFUSES -- THE "
        "EVENTS THAT PIN THE WELD DOWN ARE THE EVENTS THE GEOMETRY CANNOT "
        "HOST".format(mo=v["motivated"], ev=v["events"], lw=v["lawful"],
                      ov=v["overlap"]))
    seg.append(
        "AUTOGLUE-NO-SEAM-PRINCIPLE-DERIVED-[{fn} EXTREMAL FUNCTIONALS "
        "MEASURED BEFORE THE EVENT AND AFTER IT; EVERY CROSS DIRECTION CUTS "
        "THE LATTICE {la} TO {ct}; MAXIMUM DETERMINANT SELECTS THE DIRECT "
        "SUM UNIQUELY, THE DIRECT SUM REALISES {dr} OF THE ARENA'S "
        "CROSSINGS AND SURVIVES {dc} OF THE CUTS, AND ON THE POST-EVENT "
        "LATTICE THE SAME CRITERION IS {da}-VALUED] -- THE CONVENTION-FREE "
        "PRICE TAKES {tv} VALUE ON THE WHOLE LATTICE AND THE ONE-SIDED "
        "PRICE'S MINIMISER IS THE CUT OF EXACTLY {os} CROSS DIRECTION, SO "
        "IT IS THE EVENT'S OWN EQUATION WEARING A CRITERION'S CLOTHES: "
        "NOTHING IN THIS CORPUS SELECTS THE SEAM, AND THE ONE CRITERION "
        "THAT DOES IS THE STATE IN WHICH NOTHING CAN CROSS".format(
            fn=v["functionals"], la=v["lattice"], ct=v["cut"],
            dr=v["ds_real"], dc=v["ds_cut"], da=v["det_after"],
            tv=v["two_sided"], os=v["one_sided"]))
    return seg


def reconstruct(R):
    """S-1 BY CONSTRUCTION.  This comparator reads ONLY the receipt's
    primitive tables -- the per-object censuses -- recomputes every number in
    the head from them by its own arithmetic, and carries its own copy of the
    segment law.  It shares no function, no template and no literal with the
    builder above; nothing it needs is taken from a summary key."""
    inc = R["incidence_census"]
    frm = R["form_census"]
    invn = R["inventory_census"]
    ext = R["extremal"]
    prep = R["preparedness"]
    seam = R["seam"]
    fourth = R["fourth_direction"]

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
    motivated = tally(lambda r: r["free_items"] == 0, invn, "events")
    alive_profiles = {tuple(r["profile"]) for r in inc
                      if r["rule"] == "CROSS-ONLY" and r["fate"] == "ALIVE"
                      and (r["reading"], r["count_leg"]) == delivered}
    form_profiles = {tuple(r["profile"]) for r in frm if r["form_lawful"]}
    lawful_set = alive_profiles & form_profiles
    lawful = tally(lambda r: tuple(r["profile"]) in lawful_set, invn,
                   "events")
    overlap = tally(lambda r: r["free_items"] == 0
                    and tuple(r["profile"]) in lawful_set, invn, "events")
    detr = [r for r in ext if r["functional"].count("determinant")
            and r["selects before"] == 1][0]
    cover0 = [c["states"] for c in prep["coverage"]
              if c["crossings_absorbed"] == 0][0]
    crossings = tally(lambda r: r["profile"][0] > 0
                      and (r["reading"], r["count_leg"]) == delivered
                      and r["rule"] == "NONE", inc, "events")
    out = []
    out.append("AUTOGLUE-A-TARGET-FREE-EVENT-CONDITIONED-CROSS-LINK-"
               "CREATION-RULE-EXISTS-AT-THIS-ARENA-AT-" + str(full_cross)
               + "-OF-" + str(spanning) + "-[THE WINDOW: FOUR LINK-CREATION "
               "RULES BY TWO READINGS BY TWO COUNT LEGS AT EVERY ONE OF "
               + str(events) + " THREE-ACTOR EVENTS AND AT BOTH ENDS OF "
               "EVERY TRANSITION, THE RULE FIRING ON THE EVENT'S FOOTPRINT "
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
               "STATE MOVE; OVER ALL " + str(prep["states"]) + " STATES THE "
               "ARENA ADMITS THE BEST IS READY FOR " + str(prep["best"])
               + " CROSSINGS AND " + str(cover0) + " ARE READY FOR NONE] -- "
               "AND A LINK INSIDE A SECTOR IS REFUSED OUTRIGHT: AN UNSHARED "
               "SITE'S FORM HAS KERNEL ZERO AND FORCES THE FOURTH "
               "DIRECTION'S COUNT AGAINST THE ONE THE EVENT DEPOSITS AT "
               + str(reads) + " OF " + str(reads) + " READINGS -- SO A "
               "STATE RESTRICTS THE ALLOWED TRANSITIONS ONLY IF IT PERSISTS, "
               "WHICH IS A READING AND NOT A MEASUREMENT")
    out.append("AUTOGLUE-MOTIVATION-AND-LAWFULNESS-ARE-DISJOINT-["
               + str(motivated) + " OF " + str(events) + " EVENTS LEAVE THE "
               "WELD WITH ZERO FREE ITEMS, " + str(lawful) + " ARE LAWFUL AT "
               "EVERY LEG, AND THE TWO SETS SHARE " + str(overlap) + "] -- "
               "BY A THEOREM CHECKED AT EVERY OBJECT: AN EVENT FORCES THE "
               "WELD EXACTLY WHEN IT DOUBLES NOTHING, WHICH IS EXACTLY WHEN "
               "ALL THREE OF ITS PAIRS ARE NEW; A TRIANGLE ADMITS NO PROPER "
               "TWO-COLOURING SO ONE OF THEM FALLS INSIDE A SECTOR; AND THAT "
               "IS THE ONE CELL THE FORM REFUSES -- THE EVENTS THAT PIN THE "
               "WELD DOWN ARE THE EVENTS THE GEOMETRY CANNOT HOST")
    out.append("AUTOGLUE-NO-SEAM-PRINCIPLE-DERIVED-[" + str(len(ext))
               + " EXTREMAL FUNCTIONALS MEASURED BEFORE THE EVENT AND AFTER "
               "IT; EVERY CROSS DIRECTION CUTS THE LATTICE "
               + str(seam["lattice"]) + " TO " + str(R["cut_size"])
               + "; MAXIMUM DETERMINANT SELECTS THE DIRECT SUM UNIQUELY, THE "
               "DIRECT SUM REALISES " + str(R["ds_realises"]) + " OF THE "
               "ARENA'S CROSSINGS AND SURVIVES " + str(R["ds_in_cut"])
               + " OF THE CUTS, AND ON THE POST-EVENT LATTICE THE SAME "
               "CRITERION IS " + str(detr["selects after, most"])
               + "-VALUED] -- THE CONVENTION-FREE PRICE TAKES "
               + str(R["two_sided_values"]) + " VALUE ON THE WHOLE LATTICE "
               "AND THE ONE-SIDED PRICE'S MINIMISER IS THE CUT OF EXACTLY "
               + str(R["one_sided_matches"]) + " CROSS DIRECTION, SO IT IS "
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
SPELLED = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
           6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
           11: "eleven", 12: "twelve"}

EXEMPT_NUMERALS = {
    "45": "this unit's own paper number",
    "46": "the successor unit's paper number",
    "40": "the parent unit's paper number",
    "32": "the grandparent unit's paper number",
    "19": "the weld paper's number",
}


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
          r"[^.;:]{0,40}\b(the )?(theory|dynamics)\b"],
         [r"\bcandidate\b", r"\bgated\b", r"\bscope\b", r"\bnot the\b",
          r"\bat (this|one) arena\b", r"\bdeclar\w+\b", r"\bnot used\b"],
         ["a candidate universal rule", "scope"],
         ["The update rule is the law of ISP, established here.",
          "What this measures gives the theory its dynamics at last.",
          "ISP's dynamics is this transition and the matter is settled.",
          "The update chooses its own crossing.",
          "Here, then, is the universal update rule."]),
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
         [r"\bseam-confined\b", r"\bjointly own\b", r"\bnever\b",
          r"\bno sector-private\b", r"\bnot\b"],
         ["seam-confined"],
         ["An event in one sector moves a link the other sector owns alone.",
          "The geometry of A is altered by what happens in B.",
          "Composition bleeds across the join and the census measures it.",
          "A sector's own links are changed by the neighbour's events.",
          "The effect spills into the private cells of the far sector."]),
    Wall("WALL-NO-METRICAL-READING",
         [r"\blorentzian\b", r"\bspacetime signature\b", r"\blight cone\b",
          r"\bcontinuum limit\b"],
         [r"\b(form|cross block|completion|seam)\b[^.;:]{0,60}\b(metric|"
          r"distance|geometry of space|causal structure|signature|interval)"
          r"\b",
          r"\b(metric|distance|causal) (datum|structure|content)\b"],
         [r"\bcount law\b", r"\bno metrical\b", r"\bnot\b", r"\bhow many\b",
          r"\bdivision events\b", r"\bcount datum\b"],
         ["the form is a count law"],
         ["The seam's completions fix the interval between the sectors.",
          "The cross block is the metric datum the geometry carries.",
          "Indefinite completions give the join a causal structure.",
          "The form measures distance across the seam.",
          "What the completion supplies is the geometry of space at the "
          "join."]),
    Wall("WALL-RECONSTRUCTION-NOT-DERIVATION",
         [r"\bthe seam principle is derived\b",
          r"\bmaximum determinant is derived\b"],
         [r"\b(seam|form|completion|principle|state)\b[^.;:]{0,50}\b(follows "
          r"from|is derived from|derives from|is a consequence of|is implied "
          r"by|is forced by)\b",
          r"\bbecause (two|both) routes agree\b"],
         [r"\bnot\b", r"\bno law\b", r"\bnothing\b", r"\bdeclar\w+\b",
          r"\breproduc\w+\b", r"\bcandidate\b", r"\bneither\b"],
         ["nothing is derived"],
         ["The seam form follows from the event that crosses it.",
          "The completion is a consequence of the record it faces.",
          "Because both routes agree, the extremal principle is established.",
          "The state derives from the counts the event deposits.",
          "The selection principle is implied by the readout law."]),
    Wall("WALL-RELATION-NOT-LAW",
         [r"\bthe successor state is unique\b"],
         [r"\b(update|transition|rule)\b[^.;:]{0,50}\b(evolution law|"
          r"deterministic|determines the (successor|state)|is a map)\b",
          r"\bthe (successor|next) state is\b[^.;:]{0,25}\b(fixed|"
          r"determined|given|settled)\b",
          r"\bthe state is\b[^.;:]{0,25}\b(fixed|determined|settled)\b"],
         [r"\brelation\b", r"\bset of\b", r"\bnever\b", r"\bnot\b",
          r"\bmany-valued\b", r"\bcannot\b"],
         ["a transition relation"],
         ["The update is the deterministic evolution law of the geometry.",
          "Once the event fires, the next state is fixed.",
          "The transition determines the successor the geometry takes.",
          "The rule is a map from one state to the next.",
          "After the crossing the state is thereby determined."]),
    Wall("WALL-COUNTING-ONLY",
         [r"\bthe probability that a crossing is lawful\b"],
         [r"\b(probabilit\w+|probable|likel\w+|typical\w+|usually|"
          r"most (events|states|crossings))\b",
          r"\bthe typical\b", r"\bon average\b", r"\bmost \w+ (are|is)\b"],
         [r"\bcounting-only\b", r"\bno measure\b", r"\bnot\b",
          r"\bnothing here may be read\b"],
         ["counting-only"],
         ["Most crossings are lawful, so the dynamics prefers them.",
          "A crossing is likely to find a successor state.",
          "The typical state absorbs several events.",
          "Lawfulness is probable at this arena.",
          "Usually the form admits the cell the event makes."]),
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
            [(str(r["profile"]), r["inventory"][0], r["inventory"][1],
              r["inventory"][2], r["free_items"], r["maps"], r["events"])
             for r in R["inventory_census"]])
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
    C.table("TBL-OUTCOMES", ("pre-registered outcome", "reached",
                             "why it was reachable", "the run's witness"),
            [(o["outcome"], str(o["reached"]), o["why it was reachable"],
              o["the run's witness"]) for o in outcomes])
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
         "1", "M2's two-step row, and nothing else uses it"),
        ("the three-actor conflict group as the unit of an event", "forced",
         "1", "the committed grammar's own event size"),
    ]
    C.table("TBL-CHOICE", ("item", "class", "fiber", "where it binds"),
            choice_rows)
    for seg in V:
        C.fence(seg, 2)

    # ---- the walls -------------------------------------------------------
    ptext = paper_text if paper_text is not None else ""
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

    PAIRS = {
        ("events", M.get("n_full_cross"), M.get("n_spanning")),
        ("events", M.get("n_span_cross"), M.get("n_spanning")),
        ("events", M.get("n_span_none"), M.get("n_spanning")),
        ("events", M.get("n_lawful"), M.get("n_events")),
        ("events", M.get("n_motivated"), M.get("n_events")),
        ("events", M.get("n_refuse_frozen"), M.get("n_events")),
        ("events", M.get("n_refuse_update"), M.get("n_events")),
        ("events", M.get("n_alive_all"), M.get("n_events")),
        ("events", M.get("n_form_cross"), M.get("n_spanning")),
        ("events", M.get("n_frozen_cross"), M.get("n_form_cross")),
        ("events", M.get("n_step2_cross"), M.get("n_form_cross")),
        ("events", M.get("n_obs_unique"), M.get("n_spanning")),
        ("events", M.get("n_spanning"), M.get("n_spanning")),
        ("relabellings", M.get("n_relabellings"), M.get("n_chartperms")),
        ("states", M.get("n_best"), M.get("n_form_cross")),
        ("states", M.get("n_zero"), M.get("n_states")),
        ("states", M.get("n_persistent"), M.get("n_states")),
        ("states", M.get("n_cut"), M.get("n_lattice")),
        ("states", M.get("n_pd"), M.get("n_lattice")),
        ("states", M.get("n_ds_cut"), M.get("n_indices")),
        ("states", M.get("n_ds_real"), M.get("n_indices")),
        ("states", M.get("n_onesided_match"), M.get("n_indices")),
        ("readings", M.get("n_fourth_agree"), M.get("n_fourth_reads")),
        ("readings", M.get("n_fourth_reads"), M.get("n_fourth_reads")),
    }
    known = {(a, b) for _u, a, b in PAIRS}
    ref_bad = []
    for mm in re.finditer(r"(\d[\d,]*)\s+of\s+(?:the\s+)?(\d[\d,]*)",
                          canon(prose)):
        pair = (int(mm.group(1).replace(",", "")),
                int(mm.group(2).replace(",", "")))
        if pair not in known:
            ref_bad.append([pair[0], pair[1], canon(prose)[
                max(0, mm.start() - 40):mm.end() + 10]])
    if mut("MUT-REFERENT"):
        ref_bad = ref_bad + [[M.get("n_full_cross"), M.get("n_states"),
                              "planted"]]
    M.m("n_universes", len({u for u, _a, _b in PAIRS}),
        "declared referent universes")
    M.m("n_pairs", len(PAIRS), "measured pairs the prose may state")
    LDg.gate("G-PAPER-REFERENT", not ref_bad,
             M.stmt("referents are bound per occurrence and over prose only "
                    "-- the verdict fences, the rendered tables and the "
                    "headings are stripped first, so the run's own head "
                    "cannot discharge the paper's obligations. Every "
                    "fraction the prose states is resolved as a PAIR against "
                    "the {p} pairs this run actually measured, in {u} "
                    "declared universes: two numerals that are each true "
                    "somewhere do not make a true relation, and a fraction "
                    "reading a numerator from one census against a "
                    "denominator from another fails here",
                    p="n_pairs", u="n_universes"),
             {"violations": ref_bad[:8],
              "pairs": sorted([a, b] for _u, a, b in PAIRS)})

    # ---- the comparator (S-1) -------------------------------------------
    if mut("MUT-VERDICT"):
        R["form_census"] = [dict(r, events=r["events"] + 1)
                            for r in R["form_census"]]
    rebuilt, cross = reconstruct(R)
    same = (rebuilt == V)
    M.m("n_segments", len(V), "verdict segments")
    LDg.gate("G-VERDICT-RECON", same,
             M.stmt("the head's {n} segments are rebuilt by a comparator "
                    "that shares no function, no template and no literal "
                    "with the builder: it reads only the receipt's "
                    "per-object censuses, joins them on the profile, and "
                    "re-derives every number in the head by its own "
                    "arithmetic before typing the segments itself. The two "
                    "strings are compared whole, in both directions",
                    n="n_segments"),
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
    gates_declared = (set(LDg.names())
                      | {"G-ANCHOR-CONSUMPTION", "G-FALSIFIER-HONESTY",
                         "G-COVERAGE", "G-NO-TYPED-COUNTS", "G-READ-SET",
                         "G-SEAL-TOTAL", "G-TRANSCRIPT-BOUND",
                         "G-INTEGRITY"})
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
    M.m("n_sentinels", len(sentinels), "recipes assigning a bare boolean")
    LDg.gate("G-FALSIFIER-HONESTY", not fal_bad and not sentinels,
             M.stmt("every declared falsifier has an injection site in this "
                    "file, names a gate this run emits, and carries the "
                    "measured object it corrupts; and the source is scanned "
                    "for the sentinel shape -- a recipe whose whole body "
                    "assigns a bare boolean -- of which it finds {s}",
                    s="n_sentinels"),
             {"violations": fal_bad, "sentinels": sentinels,
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
    LDg.gate("G-COVERAGE",
             not uncovered and not bad_waiver
             and gates_now >= gates_declared,
             M.stmt("coverage is taken inside its own denominator: all {g} "
                    "gates this run declares -- those already fired, this "
                    "one, and the ones declared to fire after it -- are "
                    "either falsified by one of the {m} declared mutants, "
                    "each dying at its own named gate, or waived with a "
                    "forcing the run checks rather than describes",
                    g="n_gates", m="n_mutants"),
             {"uncovered": uncovered, "waivers": WAIVERS,
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
        read_text("RUNBOOK.md")
    reads = READS.check([SOURCES[s][0] for s in SOURCES]
                        + [SELF_REL] + ([paper_rel] if paper_text is not None
                                        else []))
    LDg.gate("G-READ-SET",
             not reads["stray"] and not reads["declared_never_read"]
             and not reads["unused_exemptions"],
             M.stmt("the read set is recorded at the process's own I/O "
                    "accessor rather than in a helper, so a raw open "
                    "anywhere is seen, and it is compared here -- after the "
                    "last measurement, order-insensitively -- against the "
                    "declared set: a stray read fails wherever it is "
                    "planted, and a declared source never read fails too",
                    ),
             reads)
    return promote(R, V, C, rep, M, LDg, SL, ptext, t0, extra)


def promote(R, V, C, rep, M, LDg, SL, ptext, t0, extra):
    """The door: totality recomputed here from the payload's live key set,
    the gate-time seals verified against what would be promoted, the
    transcript parsed back and reconciled with the ledger, and the artifacts
    staged, read back, verified and only then replaced."""
    R["schema"] = SCHEMA
    R["unit"] = "AUTOGLUE"
    R["paper"] = PAPER_REL
    R["questions"] = ["Q38", "Q39", "Q40", "Q34", "Q41", "Q42", "Q50"]
    R["measured"] = {k: M.vals[k] for k in sorted(M.vals)}
    R["measured_how"] = {k: M.how[k] for k in sorted(M.how)}
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

    if mut("MUT-PROMOTE"):
        R["seam"] = dict(R["seam"], lattice=R["seam"]["lattice"] + 1)
    v2 = SL.verify(R, LDg, "at promotion")
    LDg.gate("G-INTEGRITY", not v2["violations"] and not v2["stray"],
             M.stmt("and the seals are verified a second time against the "
                    "objects that will actually be written, before anything "
                    "is staged: the artifacts are written to a temporary, "
                    "read back, compared byte for byte, replaced, and read "
                    "back again from the promoted path, with the temporary "
                    "removed on every exit that is not a promotion"),
             v2)

    R["ledger"] = [{k: r[k] for k in ("gate", "passed", "evidence", "chain")}
                   for r in LDg.rows]
    R["totals"] = {"gates": len(LDg.rows), "sealed": len(SL.seals),
                   "unsealed": len(SL.unsealed),
                   "tables": len(C.tables)}
    R["seal_manifest"] = SL.manifest()

    body = "\n".join(OUT_LINES + ["", "-- VERDICT " + "-" * 66, ""]
                     + [x for seg in V for x in (seg, "")] + ["=" * 78, ""])
    if mut("MUT-TRANSCRIPT"):
        body = body + "\n    [PASS] G-A-GATE-THAT-NEVER-RAN " + "0" * 16
    final = Counter(re.findall(r"\[(PASS|FAIL)\] (\S+) +([0-9a-f]{16})",
                               body))
    want = Counter(("PASS" if r["passed"] else "FAIL", r["gate"], r["chain"])
                   for r in LDg.rows)
    if final != want:
        raise GateFail("G-TRANSCRIPT-BOUND",
                       "the promoted text and the ledger disagree: %d vs %d"
                       % (len(final), len(want)))
    blob = json.dumps(R, indent=1, sort_keys=True, default=str) + "\n"
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
    Falsifier("MUT-RULE-NAME", "G-RULE-EQUIVARIANT", "a rule's output",
              "one rule is made to special-case the events touching one "
              "NAMED actor, which is what a target fitted after the event "
              "would do and what no relabelling can preserve"),
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
]
WAIVERS = {}
MUTNAMES = [f.name for f in FALSIFIERS]


def cli(argv):
    mode, path, mutant = "run", None, None
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--no-write":
            globals()["WRITE"] = False
        elif a == "--numbers":
            mode = "numbers"
        elif a == "--selftest":
            mode = "selftest"
        elif a == "--list-gates":
            mode = "gates"
        elif a == "--list-mutants":
            mode = "mutants"
        elif a == "--list-families":
            mode = "families"
        elif a == "--verify-paper":
            i += 1
            if i >= len(argv):
                return None
            mode, path = "paper", argv[i]
        elif a == "--mutant":
            i += 1
            if i >= len(argv) or argv[i] not in MUTNAMES:
                return None
            mutant = argv[i]
        else:
            return None
        i += 1
    return mode, path, mutant


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
        for f in FALSIFIERS:
            print("%-24s falsified by %s" % (f.gate, f.name))
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
        globals()["MUTANT"] = "MUT-ANCHOR"
        globals()["WRITE"] = False
        before = {rel: (bdigest(read_bytes(rel))
                        if os.path.exists(os.path.join(REPO, rel)) else None)
                  for rel in (OUT_REL, REC_REL)}
        try:
            paper = (read_text(PAPER_REL)
                     if os.path.exists(os.path.join(REPO, PAPER_REL))
                     else None)
            full_run(paper, PAPER_REL)
        except GateFail as e:
            after = {rel: (bdigest(read_bytes(rel))
                           if os.path.exists(os.path.join(REPO, rel))
                           else None) for rel in (OUT_REL, REC_REL)}
            print("selftest: refused at %s" % e.check)
            print("selftest: artifacts unchanged: %s" % (before == after))
            return 1 if before == after else 3
        print("selftest: THE CORRUPTION WAS NOT CAUGHT")
        return 3
    if mode == "paper":
        full = path if os.path.isabs(path) else os.path.join(REPO, path)
        if not os.path.exists(full) or os.path.isdir(full):
            sys.stderr.write("verify-paper: no such paper\n")
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

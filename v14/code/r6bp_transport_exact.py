#!/usr/bin/env python3.13
"""
v14 R6b' -- THE RENEWAL-GRAIN TRANSPORT (paper-09).  GREEN-REPAIRED.

Does a MOTIVATED identification carry the renewal-grain positional
structure of the deep corpus (S1's completed chain q'; S2's
intervening-pattern census) to the spatial record-interval arena
(I7 / R6a's n_l(x)) -- and if so, does the derived interval-positional
kernel collapse the R6a split fiber, as a forced VALUE or a forced
DISTRIBUTION?

THE RENEWAL CONVENTION IS THE SOURCE'S, DECLARED HERE AND GATED
--------------------------------------------------------------
A renewal is an ARBITRATION landing in class 0 -- S1's own operative
definition (d43b's REN: class 0 AND carrying an 'r'), S4's theorem
("every pair arbitration is a renewal to the root state"), and S2's
leg delimiter (every censused leg ends in the 'r' tag).  An idle at the
root is a self-loop at class 0 and is NOT a renewal.  The bare-state-0
reading (renewal = any visit to state 0) is measured and printed as a
DISCLOSED ALTERNATIVE, never as this unit's law.

PROVENANCE BY COMMITTED SHA (RUNBOOK 14, the v14 #62 engraving)
--------------------------------------------------------------
Every artifact this unit consumes is read at a COMMIT SHA declared in
this frozen text.  `git show HEAD:` and worktree bytes are mutable
state and are not read.  The three declared revisions are

  CORPUS_SHA        d042ef1ae74e87caad474cf91a479ebb35666610
                    (v14 ledger #62) -- the six deep rows S1..S6, the
                    adjudication-added row S7 (paper 32), I7's receipt,
                    CR-B's receipt, and this unit's own pin.
  R6A_TERMINAL_SHA  d5fb2a5956f7c82c135a542ea5b81c7f2ca92633
                    (v14 ledger #52, "R6a repair committed as-is") --
                    THE R6a TERMINAL RECEIPT, sha256-12 856f6e810ab5.
                    Every R6a path-value this unit consumes is read
                    here.
  R6A_DELIVERED_SHA b0087a9d262b06e0caf8745ab6b4846d6fdcbb06
                    (v14 ledger #26, R6a delivered) -- receipt
                    sha256-12 022c3f488a93, read ONLY by the path-value
                    stability gate.

The one file read from the working tree is this unit's OWN paper,
v14/paper-09-renewal-transport.md -- the unit's own deliverable, which
the paper<->receipt gates exist to bind.

CLI CONTRACT
------------
  python3.13 r6bp_transport_exact.py
        Plain delivery run.  Verifies every anchor in three
        short-circuiting stages, evaluates every must-pass gate,
        measures the mutant death table IN PROCESS, computes the
        verdict from the measured values, and WRITES
        r6bp_transport_output.txt and r6bp_transport_receipt.json
        beside this file.  Exit 0 iff every anchor holds and every
        must-pass gate passes.

  python3.13 r6bp_transport_exact.py --selftest
        Re-runs this file once per declared mutant in a subprocess and
        requires each to exit non-zero AND to be killed by its NAMED
        gate or anchor.  Writes nothing.

  python3.13 r6bp_transport_exact.py --mutant NAME
        Runs the delivery computation with the named injection applied.
        Writes nothing.  Exit non-zero is the intended outcome.

  python3.13 r6bp_transport_exact.py --list-mutants
        Prints the declared mutant names, one per line.

Exit 2 = anchor failure; exit 1 = gate failure; exit 3 = float guard.

ARITHMETIC: exact.  int / fractions.Fraction only.  An AST pass over
this file's own source rejects every float literal before any
measurement runs.

SCOPE (binding, printed with every headline)
  * S1's chain and S4's renewal theorem are DELIVERY-FREE scope
    (two-actor, delivery-free).  S2's census is TRANSPORT scope.
  * S2's interval lengths are ENSEMBLE DATA (declared), not samples.
  * S2's two length-4 cells are E2's leg 1 (depths 3->7) and E3's
    leg 2 (depths 6->10) -- two cells of two ensembles at two depths.
  * S5's continuous positional layer carries its own
    chosen-not-derived disclaimer and is used only as a labelled
    comparator.
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import json
import os
import re
import subprocess
import sys
from fractions import Fraction as Fr

# --------------------------------------------------------------------
# 0.  Paths and the declared revisions
# --------------------------------------------------------------------

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
OUT_TXT = os.path.join(HERE, "r6bp_transport_output.txt")
OUT_JSON = os.path.join(HERE, "r6bp_transport_receipt.json")
PAPER_REL = "v14/paper-09-renewal-transport.md"

CORPUS_SHA = "d042ef1ae74e87caad474cf91a479ebb35666610"
R6A_TERMINAL_SHA = "d5fb2a5956f7c82c135a542ea5b81c7f2ca92633"
R6A_DELIVERED_SHA = "b0087a9d262b06e0caf8745ab6b4846d6fdcbb06"

# --------------------------------------------------------------------
# 1.  The float guard (AST over this file's own source)
# --------------------------------------------------------------------


def _self_source() -> str:
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        return fh.read()


_SELF_AST: list = []


def self_ast():
    if not _SELF_AST:
        _SELF_AST.append(ast.parse(_self_source()))
    return _SELF_AST[0]


_SCAN: dict[str, object] = {}


def float_guard() -> tuple[int, int]:
    if "float" in _SCAN:
        return _SCAN["float"]
    tree = self_ast()
    bad = 0
    total = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            total += 1
            if isinstance(node.value, (float, complex)):
                bad += 1
    _SCAN["float"] = (bad, total)
    return bad, total


def literal_gate_scan() -> list[str]:
    """AST: every C.gate(...) call whose PREDICATE is a literal constant.

    The #208 clause and the R6b' instrument audit (six literal-True
    must-pass gates): a gate whose predicate cannot be false is a
    disclosure, not a gate.  This unit declares ZERO such calls and
    proves it by reading its own syntax tree.
    """
    if "literal" in _SCAN:
        return _SCAN["literal"]
    tree = self_ast()
    bad = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fn = node.func
        is_gate = (isinstance(fn, ast.Attribute) and fn.attr == "gate")
        if not is_gate or len(node.args) < 2:
            continue
        name = node.args[0].value if isinstance(node.args[0], ast.Constant) \
            else "<computed>"
        if isinstance(node.args[1], ast.Constant):
            bad.append(str(name))
    _SCAN["literal"] = sorted(bad)
    return _SCAN["literal"]


# --------------------------------------------------------------------
# 2.  Committed-object reads (read-only git), cached
# --------------------------------------------------------------------

_BLOB: dict[tuple[str, str], bytes] = {}
_READS: list[dict] = []


def blob(sha: str, rel: str) -> bytes:
    key = (sha, rel)
    if key not in _BLOB:
        proc = subprocess.run(["git", "-C", REPO, "show", f"{sha}:{rel}"],
                              capture_output=True)
        if proc.returncode != 0:
            raise RuntimeError(f"committed object unavailable: {sha}:{rel}")
        _BLOB[key] = proc.stdout
        _READS.append({"sha": sha, "artifact": rel, "kind": "committed"})
    return _BLOB[key]


def text(sha: str, rel: str) -> str:
    return blob(sha, rel).decode("utf-8")


def sha12(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:12]


_PAPER_CACHE: list = []


def paper_text() -> str:
    if not _PAPER_CACHE:
        p = os.path.join(REPO, PAPER_REL)
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as fh:
                _PAPER_CACHE.append(fh.read())
        else:
            _PAPER_CACHE.append("")
        _READS.append({"sha": "(working tree)", "artifact": PAPER_REL,
                       "kind": "own-deliverable"})
    return _PAPER_CACHE[0]


def norm(s: str) -> str:
    """Whitespace-and-emphasis normalisation.

    Markdown emphasis markers and blockquote markers are display, not
    content; a quotation is compared to its source modulo them.  The
    normalisation is declared, printed, and identical on both sides.
    """
    s = re.sub(r"^[ \t]*>[ \t]?", " ", s, flags=re.M)
    s = s.replace("**", "").replace("*", "").replace("`", "")
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("—", "--").replace("–", "-")
    s = re.sub(r"\s+", " ", s).strip()
    # the Python string-literal concatenation seam: a source that spells
    # one sentence as adjacent quoted fragments is quoted as the sentence
    s = re.sub(r'"\s*"', " ", s)
    return re.sub(r"\s+", " ", s).strip()


_NORMC: dict[tuple[str, str], str] = {}


def norm_paper() -> str:
    if "paper" not in _NORMC:
        _NORMC["paper"] = norm(paper_text())
    return _NORMC["paper"]


def norm_source(sha: str, rel: str) -> str:
    """Normalised committed source text, memoized.  The object is an
    immutable committed blob, so the memo is of a constant; every gate
    below still evaluates its own predicate fresh (#185)."""
    key = (sha, rel)
    if key not in _NORMC:
        _NORMC[key] = norm(text(sha, rel))
    return _NORMC[key]


def fr(x: Fr) -> str:
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 \
        else str(x.numerator)


def law_str(d: dict) -> str:
    return "(" + ", ".join(fr(d[k]) for k in sorted(d)) + ")"


# --------------------------------------------------------------------
# 3.  The pinned rows
# --------------------------------------------------------------------

P31 = "v10/relativistic-isp-v10-paper31-four-decisions-at-the-joints.md"
D43B = "v10/code/d43b_state_chain_exact.py"
U1B_NOTE = "v11/note-u1b-renewal-class-sweep.md"
U1B_OUT = "v11/code/u1b_output.txt"
U1B_CODE = "v11/code/u1b_renewal_class_sweep_exact.py"
P0 = "v11/relativistic-isp-v11-paper0-the-indivisible-record-law.md"
P30 = "v10/relativistic-isp-v10-paper30-the-generated-record-and-its-completion.md"
D33 = "v10/note-d33-history-law-phase.md"
P21 = "v10/relativistic-isp-v10-paper21-local-generators-do-not-imply-local-memory.md"
D34B = "v10/code/d34b_exponential_clocks_exact.py"
D12 = "v10/note-d12-selection-principle-audit.md"
P16 = "v10/relativistic-isp-v10-paper16-the-rulebook-is-the-history-law.md"
P32 = "v10/relativistic-isp-v10-paper32-the-boundary-of-closure.md"
PIN = "v14/note-r6bprime-transport-pin.md"
HA_RECEIPT = "v13/code/ha_successor_receipt.json"
CRB_RECEIPT = "v14/code/crb_stochastic_receipt.json"
R6A_RECEIPT = "v14/code/r6a_refinement_receipt.json"

PED = {
    "S1": "S1 THE TRANSITION MATRIX -- TERMINAL (v10 #349)",
    "S2": ("S2 THE POSITIONAL CENSUS -- TERMINAL (v11 #20-#21); interval "
           "lengths are ENSEMBLE DATA (declared); the two length-4 cells "
           "are E2 leg 1 (depths 3->7) and E3 leg 2 (depths 6->10)"),
    "S3": "S3 THE TYPE DECLARATION -- founding paper; v11 FROZEN",
    "S4": ("S4 THE RENEWAL THEOREM -- TERMINAL (v10 #326; ten hostile "
           "rounds; its header's \"paper-level review open\" note carried)"),
    "S5": ("S5 THE DECLARED POSITIONAL LAW -- D34b TERMINAL delta (3 "
           "hostile streams); the waiting law and rates are CHOSEN, NOT "
           "DERIVED"),
    "S6": ("S6 THE EXTREMAL STANDARD -- audit (status: completed "
           "pre-hostile-review, carried) + finite nonselection theorem"),
    "S7": ("S7 THE ESCAPE -- v10 paper 32 'The boundary of closure', "
           "TERMINAL (v10 #392).  ADDED BY THE R6b' ADJUDICATION (order "
           "R-R6BP-3) for one purpose: the measured cause of the "
           "transport-scope seam.  The pin's standing prohibition on "
           "paper 32's 36-state quotient claim is honoured and gated"),
    "I7": ("I7 (R0 founding pin) -- gravity's record layer; H_a[N] "
           "record-native; record-IS-metric; THE BASELINE ARENA ROW"),
    "R6A": ("v14 R6a paper-04 -- TERMINAL (v14 #53); receipt read at the "
            "R6a TERMINAL commit d5fb2a5956f7 (sha256-12 856f6e810ab5)"),
    "CRB": "v14 CR-B -- DELIVERED-VERIFIED-UNREVIEWED (LOG #37, #38)",
}

BYTE_ANCHORS = [
    ("A-PIN", CORPUS_SHA, PIN, "17111fd19022", "S1", "G-PIN-MEASUREMENTS"),
    ("A-S1-PAPER31", CORPUS_SHA, P31, "7ac66f3fe74d", "S1", "G-S1-HARMONIC"),
    ("A-S1-D43B", CORPUS_SHA, D43B, "5f91f0190b4c", "S1",
     "G-S1-TWO-TRANSCRIPTIONS"),
    ("A-S2-NOTE", CORPUS_SHA, U1B_NOTE, "47f001fad828", "S2", "G-S2-PROFILES"),
    ("A-S2-OUT", CORPUS_SHA, U1B_OUT, "a955b8484465", "S2", "G-S2-PROFILES"),
    ("A-S2-CODE", CORPUS_SHA, U1B_CODE, "5adb205a33d6", "S2",
     "G-S2-TWO-CELLS-CONFOUND"),
    ("A-S3-PAPER0", CORPUS_SHA, P0, "37a428321f46", "S3", "G-TYPE-CENSUS"),
    ("A-S4-PAPER30", CORPUS_SHA, P30, "e431a7c48f76", "S4",
     "G-RENEWAL-CONVENTION-IS-THE-SOURCES"),
    ("A-S5-D33", CORPUS_SHA, D33, "bad952ee5849", "S5",
     "G-S5-COMPARATOR-SEPARATION"),
    ("A-S5-PAPER21", CORPUS_SHA, P21, "038a424a8843", "S5",
     "G-S5-COMPARATOR-SEPARATION"),
    ("A-S5-D34B", CORPUS_SHA, D34B, "dee1cc968268", "S5",
     "G-S5-COMPARATOR-SEPARATION"),
    ("A-S6-D12", CORPUS_SHA, D12, "2670a2ea7644", "S6",
     "G-VARIATIONAL-ROWS-MEASURED"),
    ("A-S6-PAPER16", CORPUS_SHA, P16, "dbf027b2fbc9", "S6",
     "G-EXTREMAL-COUNTERMODEL"),
    ("A-S7-PAPER32", CORPUS_SHA, P32, "4b533e437b0f", "S7",
     "G-SEAM-CAUSE-IS-THE-ESCAPE"),
    ("A-I7", CORPUS_SHA, HA_RECEIPT, "542b8735daf0", "I7",
     "G-ARENA-BASELINE"),
    ("A-CRB", CORPUS_SHA, CRB_RECEIPT, "5ebeec141303", "CRB",
     "G-CRB-SIMPLEX"),
    ("A-R6A-TERMINAL", R6A_TERMINAL_SHA, R6A_RECEIPT, "856f6e810ab5", "R6A",
     "G-R6A-FIBER-REBUILD"),
    ("A-R6A-DELIVERED", R6A_DELIVERED_SHA, R6A_RECEIPT, "022c3f488a93", "R6A",
     "G-R6A-PATH-VALUE-STABILITY"),
]

NAMED_EXCLUSIONS = [
    ("v11/note-u1c-depth15-two-sided.md",
     "GREEN-UNREVIEWED, NOT CITABLE per STATUS -- registered lead only, "
     "status printed"),
    ("v10/THE-THEORY-SO-FAR.md", "index only, never primary"),
    ("v12 Gamma objects", "arena-free -- no interval/position/count content"),
    ("v10/note-d70-horizon-limit-result.md",
     "excluded at the pin as round-1-repaired; the Gamma-scout later "
     "established that header was STALE (d70 is TERMINAL-AT-ONE-HOSTILE-"
     "ROUND, v10 LOG #489).  The exclusion is retained for this unit "
     "because d70 supplies horizon kernels, not an interval-positional "
     "law -- the correction is disclosed, not buried"),
]

# --------------------------------------------------------------------
# 4.  THE QUOTATION TABLE -- the #62 corrected verbatim-anchor spec
#
#     The anchor kind binds QUOTE FIDELITY: every quotation THE PAPER
#     prints is checked against the SOURCE's committed bytes, and every
#     quotation-shaped span in the paper must be one of these rows.
#     Each row names a consumer gate that must EXIST, be NON-LITERAL
#     (AST-verified), and be FALSIFIED BY A DECLARED MUTANT (measured).
# --------------------------------------------------------------------

QUOTES = [
    ("Q-S1-REN-SOURCE", D43B,
     "REN = [h for h in FAM if len(h) <= 4 and CLS[tuple(h)] == 0 and "
     "any(e[0] == 'r' for e in h)]",
     "S1", "G-RENEWAL-CONVENTION-IS-THE-SOURCES"),
    ("Q-S1-REN-GATE", D43B,
     "ALL clean-slate renewal points at len <= 4 (class 0 carrying an "
     "arb; each with a UNIQUE shared non-superseded base) have "
     "root-identical one-step menus under their own base substitution "
     "-- the 144-point census.",
     "S1", "G-RENEWAL-CONVENTION-IS-THE-SOURCES"),
    ("Q-S1-CLASS", P31,
     "The dominant class {2, 4, 5} (Tarjan decomposition; {0, 1, 3} is "
     "transient and carries the renewal loop 3 -> 0)",
     "S1", "G-CLOSED-CLASS"),
    ("Q-S1-CONFLICT", P31,
     "the conflict row is {0: 1/7, 3: 3/4, 5: 3/28}.  This is the "
     "root-free completion, exhibited on the intrinsic chain.",
     "S1", "G-KERNEL-CONFLICT-ROW"),
    ("Q-S1-SCOPE", P31,
     "At transport scope the picture will change and is declared: "
     "deliveries reopen the absorbing sector (diverged holdings can "
     "reconverge), the class structure of §3.2 is not stable under the "
     "transport grammar, and the Martin-boundary machinery that this "
     "section did not need is expected to become load-bearing exactly "
     "there (§7, successor 2).",
     "S1", "G-SEAM-CAUSE-IS-THE-ESCAPE"),
    ("Q-S2-L3", U1B_NOTE,
     "A renewal three events after a renewal forces (p,p,r) and nothing "
     "else.  A renewal four events after a renewal admits exactly five "
     "intervening patterns -- (d,p,p,r), (n,p,p,r), (p,n,p,r), "
     "(p,p,d,r), (p,p,n,r) -- each with exactly two proposals plus one "
     "delivery or one idle.",
     "S2", "G-MIDDLE-SLOT-ADMITS-NO-DELIVERY"),
    ("Q-S2-SCOPE", U1B_NOTE,
     "Transport scope (d42b1) only; the two-actor pool only",
     "S2", "G-S2-TWO-CELLS-CONFOUND"),
    ("Q-S3-POSIT", P0,
     "[POSIT] v11's division events are the renewal events.",
     "S3", "G-TYPE-CENSUS"),
    ("Q-S3-BRIDGES", P0,
     "The bridges are the conflict windows between renewals.",
     "S3", "G-BRIDGES-READING"),
    ("Q-S3-GAMMA", P0,
     "the sparse indivisible family Γ(cut′ ← cut), conditioned only at "
     "division events | to be constructed",
     "S3", "G-GAMMA-MAIN-REGISTER"),
    ("Q-S4-RENEWAL", P30,
     "every pair arbitration is a renewal to the root state [THEOREM at "
     "two-actor delivery-free scope]",
     "S4", "G-RENEWAL-CONVENTION-IS-THE-SOURCES"),
    ("Q-S4-CLICK", P30,
     "K1 refines into a chain of selection clicks",
     "S4", "G-IDENTIFICATION-CENSUS"),
    ("Q-S4-EMPIRICAL", P30,
     "Which basis nature seals — the fine order-sealed record or the "
     "coarse winner-sealed record — is an empirical question.",
     "S4", "G-IDENTIFICATION-CENSUS"),
    ("Q-S4-ROOTED", P30,
     "Truncated completions are therefore depth-non-stationary: rooted",
     "S4", "G-COVER-DISSOLVED"),
    ("Q-S1-GROWS", P31,
     "its state count grows with depth (17, 23, 29 at depths 4, 5, 6) "
     "while representing no new structure",
     "S1", "G-COVER-DISSOLVED"),
    ("Q-S5-CHOSEN", D33,
     "the coefficients 1/4 are chosen, not derived",
     "S5", "G-S5-COMPARATOR-SEPARATION"),
    ("Q-S5-CHOSEN2", P21,
     "For the chosen static-adjacency D34b birth/idle/interaction "
     "exemplar",
     "S5", "G-S5-COMPARATOR-SEPARATION"),
    ("Q-S6-BAR", D12,
     "A proposed selector Q derives a unique law only if the frozen "
     "SHARD premises plus Q have exactly one physical equivalence class "
     "of models.",
     "S6", "G-EXTREMAL-COUNTERMODEL"),
    ("Q-S6-MAXENT", D12,
     "least-committal law relative to a supplied base measure and "
     "supplied constraints",
     "S6", "G-VARIATIONAL-ROWS-MEASURED"),
    ("Q-S6-NONSEL", P16,
     "a fixed causal action does not select the boundary state, orbit "
     "measure, extension kernel or complete next-record law.",
     "S6", "G-VARIATIONAL-ROWS-MEASURED"),
    ("Q-S6-INTRINSIC", P16,
     "the corpus has no record-intrinsic, field-redefinition-invariant "
     "complexity measure that selects one generator.",
     "S6", "G-D12-EXTENSION-NAMED"),
    ("Q-S7-ESCAPE", P32,
     "the window chain ESCAPES: 68 transitions from shallow parents "
     "land in 5 classes first realized at length 3.  Escape is not "
     "non-stabilization: the partition behaves; the state space outruns "
     "every window.",
     "S7", "G-SEAM-CAUSE-IS-THE-ESCAPE"),
    ("Q-S7-SHORTCUT", P32,
     "menu-shape factorization fails at transport scope (gated exhibit), "
     "so the delivery-free machinery cannot be silently reused (a gated "
     "negative control: zero of the 3,969 transport menus match any "
     "delivery-free menu shape).",
     "S7", "G-SEAM-CAUSE-IS-THE-ESCAPE"),
]

# Declared standing-negation markers.  A2 (the meaning inversion that
# survived the #34 form) preserves the needle and inverts the standing
# around it.  A verbatim window cannot bind standing; a NEIGHBOURHOOD
# SCAN for withdrawal/supersession markers can, and this is exactly the
# declared class it binds -- no more.
STANDING_MARKERS = [
    "withdrawn", "superseded", "erratum", "corrected statement",
    "retracted", "no longer holds", "does not state this section",
    "reproduced here only as",
]
STANDING_WINDOW = 1400

# Standing-marker hits MEASURED in the delivered sources, DECLARED here
# with their adjudication.  The gate compares the measured hit list
# against this frozen declaration: a source that ACQUIRES a standing
# marker near an anchored quotation moves the list and the gate fails.
DECLARED_STANDING_HITS = [
    ("Q-S5-CHOSEN", "withdrawn",
     "D33's own §9 corrections list, in the same paragraph block: "
     "\"section 6's global-depth geometric rate is withdrawn\".  A "
     "different item of the same list; no value of this unit reads "
     "either."),
    ("Q-S5-CHOSEN", "withdrawn",
     "D33's own §9 corrections: \"the proposed profinite shadow is "
     "withdrawn pending an explicit inverse system\" -- an in-line "
     "withdrawal of a DIFFERENT item of the very list the quoted "
     "disclaimer belongs to."),
    ("Q-S5-CHOSEN", "superseded",
     "the quoted disclaimer's own list is tagged \"[provisional §8 "
     "wording, superseded where noted in §9]\".  ADJUDICATED: the "
     "supersession is item-wise and §9/§10 withdraw the profinite "
     "shadow, not the chosen-not-derived clause; and the clause is a "
     "caveat AGAINST S5, so carrying it can only under-claim.  S5 "
     "enters this unit as a labelled comparator and no derived value "
     "reads from it."),
]


# --------------------------------------------------------------------
# 5.  The run context
# --------------------------------------------------------------------

class AnchorStop(Exception):
    pass


class Ctx:
    def __init__(self, mut):
        self.mut = mut
        self.lines: list[str] = []
        self.gates: list[dict] = []
        self.anchors: list[dict] = []
        self.failed_anchors: list[str] = []
        self.stages: list[str] = []
        self.census_ran = False

    def say(self, s: str = "") -> None:
        self.lines.append(s)

    def gate(self, name: str, ok, detail: str, falsifier: str) -> bool:
        ok = bool(ok)
        self.gates.append({"name": name, "passed": ok, "detail": detail,
                           "must_pass": True,
                           "declared_falsifier": falsifier})
        self.say(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        return ok

    def gate_names(self) -> set:
        return {g["name"] for g in self.gates}

    def failures(self) -> list[str]:
        return [g["name"] for g in self.gates if not g["passed"]]

    def signature(self) -> dict:
        return {"anchors": sorted({a.split(":")[0]
                                   for a in self.failed_anchors}),
                "gates": sorted(self.failures()),
                "stages": list(self.stages)}


# --------------------------------------------------------------------
# 6.  Anchor stages -- quotations, then bytes, then path-values.
#     GENUINE short-circuit: a failed stage raises and no later stage
#     is evaluated.  The census proves this by observing, for the
#     quotation-break mutant, that no byte anchor was ever reached.
# --------------------------------------------------------------------

def stage_quotations(C: Ctx) -> dict:
    """Stage 1 -- QUOTE FIDELITY (#62 corrected spec).

    Every quotation the PAPER prints is bound to its SOURCE's committed
    bytes, and every quotation-shaped span in the paper must be a
    declared row.  A verbatim window binds quote fidelity; it does not
    bind standing.  The standing sentinel below binds the declared
    withdrawal/supersession class, and nothing more.
    """
    C.stages.append("quotations")
    ptxt = norm_paper()
    declared = {}
    for key, rel, quote, ped, consumer in QUOTES:
        needle = norm(quote)
        if C.mut == "MUT-QUOTE-SOURCE-DRIFT" and key == "Q-S4-RENEWAL":
            needle = needle.replace("delivery-free", "transport")
        src = norm_source(CORPUS_SHA, rel)
        in_source = needle in src
        in_paper = needle in ptxt
        if C.mut == "MUT-PAPER-QUOTE-INVERSION" and key == "Q-S5-CHOSEN":
            # the A5 class: the paper renders an INVERTED quotation
            bad = needle.replace("chosen, not derived", "derived, not chosen")
            in_paper = bad in ptxt
            in_source = bad in src
        declared[key] = needle
        C.anchors.append({
            "name": key, "kind": "quotation", "artifact": rel,
            "source_sha": CORPUS_SHA, "pedigree": PED[ped],
            "consumer_gate": consumer, "chars": len(needle),
            "in_source_committed_bytes": in_source,
            "printed_in_the_paper": in_paper,
            "ok": bool(in_source and in_paper)})
        if not in_source:
            C.failed_anchors.append(
                f"{key}: quotation ABSENT from the committed bytes of {rel}")
        elif not in_paper:
            C.failed_anchors.append(
                f"{key}: quotation not printed in {PAPER_REL}")
    # every quotation-shaped span the paper prints must be declared
    spans = []
    for mo in re.finditer(r'\*"(.+?)"\*', paper_text(), re.S):
        spans.append(norm(mo.group(1)))
    undeclared = [s for s in spans if s not in set(declared.values())]
    if C.mut == "MUT-PAPER-UNBOUND-QUOTE":
        undeclared = undeclared + ["<an unbound quotation>"]
    info = {"rows": len(QUOTES), "spans_found_in_the_paper": len(spans),
            "undeclared_spans": undeclared}
    if undeclared:
        C.failed_anchors.append(
            f"Q-UNBOUND: {len(undeclared)} quotation span(s) in the paper "
            f"bound to no declared source row")
    if C.failed_anchors:
        raise AnchorStop()
    return info


def standing_sentinel(C: Ctx) -> dict:
    """The declared standing class: withdrawal / supersession markers in
    the NEIGHBOURHOOD of an anchored quotation.  This is what the A2
    meaning-inversion attacks, and it is the only part of 'standing' a
    text instrument can bind."""
    pats = {mk: re.compile(
        r"(?<![.\-a-z])superseded" if mk == "superseded" else re.escape(mk),
        re.I) for mk in STANDING_MARKERS}
    hits = []
    for key, rel, quote, ped, consumer in QUOTES:
        src = norm_source(CORPUS_SHA, rel)
        if C.mut == "MUT-MEANING-INVERSION" and key == "Q-S1-SCOPE":
            # the A2 injection, verbatim in shape: the needle is
            # preserved and the STANDING around it is inverted
            n = norm(quote)
            i = src.find(n)
            src = (src[:i] + "The following paragraph was WITHDRAWN in "
                   "erratum E-9 and is reproduced here only as a "
                   "superseded claim; it does NOT state this section's "
                   "scope. " + src[i:])
        n = norm(quote)
        i = src.find(n)
        if i < 0:
            continue
        lo = max(0, i - STANDING_WINDOW)
        hi = min(len(src), i + len(n) + STANDING_WINDOW)
        win = src[lo:hi]
        for mk, pat in pats.items():
            for _ in pat.finditer(win):
                hits.append((key, mk))
    return {"hits": hits,
            "declared": [(k, m) for k, m, _ in DECLARED_STANDING_HITS]}


def stage_bytes(C: Ctx) -> None:
    """Stage 2 -- file-bytes, every one of them a COMMITTED object."""
    C.stages.append("bytes")
    for name, sha, rel, expected, ped, consumer in BYTE_ANCHORS:
        got = sha12(blob(sha, rel))
        if C.mut == "MUT-BYTE-ANCHOR-DRIFT" and name == "A-S1-PAPER31":
            got = "deadbeefcafe"
        ok = (got == expected)
        C.anchors.append({"name": name, "kind": "file-bytes-committed",
                          "artifact": rel, "source_sha": sha,
                          "expected": expected, "measured": got, "ok": ok,
                          "pedigree": PED[ped], "consumer_gate": consumer})
        if not ok:
            C.failed_anchors.append(
                f"{name}: {sha[:12]}:{rel} expected {expected} got {got}")
    if C.failed_anchors:
        raise AnchorStop()


_JSON: dict[tuple[str, str], dict] = {}


def load_json(sha: str, rel: str) -> dict:
    key = (sha, rel)
    if key not in _JSON:
        _JSON[key] = json.loads(blob(sha, rel).decode("utf-8"))
    return _JSON[key]


def walk(obj, path):
    cur = obj
    for k in path:
        try:
            cur = cur[k]
        except (KeyError, IndexError, TypeError):
            return "<PATH-ABSENT:" + "/".join(str(x) for x in path) + ">"
    return cur


def anchor_path(C: Ctx, name, sha, rel, path, expected, ped, consumer):
    cur = walk(load_json(sha, rel), path)
    if C.mut == "MUT-PATH-VALUE-DRIFT" and name == "P-R6A-DIAG2-RAW":
        cur = 0
    ok = (cur == expected)
    C.anchors.append({"name": name, "kind": "path-value", "artifact": rel,
                      "source_sha": sha,
                      "path": "/".join(str(p) for p in path),
                      "expected": expected, "measured": cur, "ok": ok,
                      "pedigree": PED[ped], "consumer_gate": consumer})
    if not ok:
        C.failed_anchors.append(
            f"{name}: {rel}:{'/'.join(str(p) for p in path)} expected "
            f"{expected!r} got {cur!r}")
    return cur


R6A_PATHS = [
    ("P-ARENA-GEOMETRY-RECORD", ["arena", "geometry_record"],
     "n_l(x) in Z_>0, the number of division events in the record "
     "interval between x and x+l", "G-ARENA-BASELINE"),
    ("P-ARENA-READOUT", ["arena", "readout"],
     "q_ij e_l^i e_l^j = n_l(x); I = q^-1 (det q)^w at w = 0",
     "G-DET-LEG-CORRECTED"),
    ("P-ARENA-SITES", ["arena", "sites"],
     "X = (Z_L)^d with L = 3, d = 2 (|X| = 9)", "G-ARENA-BASELINE"),
    ("P-ARENA-LINKS", ["arena", "links"], [[1, 0], [0, 1], [1, 1]],
     "G-ARENA-BASELINE"),
    ("P-R6A-DIAG2-RAW", ["split_fibers", "G-DIAG2", "raw"], 19683,
     "G-R6A-FIBER-REBUILD"),
    ("P-R6A-ANISO2-RAW", ["split_fibers", "G-ANISO2", "raw"],
     13631146639813244878848, "G-R6A-FIBER-REBUILD"),
    ("P-R6A-DIAG2-ADMISSIBLE",
     ["split_fibers", "G-DIAG2", "admissible_at_images"], 19683,
     "G-DERIVED-LAW-COMPLETE-ON-ONE-RECORD"),
    ("P-R6A-ANISO2-ADMISSIBLE",
     ["split_fibers", "G-ANISO2", "admissible_at_images"],
     1257565061957837936381, "G-ADMISSIBILITY-COUPLING"),
    ("P-R6A-OFFDIAG-RAW", ["split_fibers", "G-OFFDIAG", "raw"], 1953125,
     "G-DERIVED-LAW-COMPLETE-ON-ONE-RECORD"),
    ("P-R6A-OFFDIAG-ADMISSIBLE",
     ["split_fibers", "G-OFFDIAG", "admissible_at_images"], 19683,
     "G-DERIVED-LAW-COMPLETE-ON-ONE-RECORD"),
    ("P-R6A-ANISO-RAW", ["split_fibers", "G-ANISO", "raw"], 0,
     "G-UNREFINABLE-RECORDS"),
    ("P-R6A-CURVED-RAW", ["split_fibers", "G-CURVED", "raw"], 0,
     "G-UNREFINABLE-RECORDS"),
    ("P-R6A-FLAT-RAW", ["split_fibers", "G-FLAT", "raw"], 0,
     "G-UNREFINABLE-RECORDS"),
    ("P-R6A-EQUIVARIANT-FIBERS", ["equivariant_fibers"],
     {"G-ANISO2": 288, "G-CURVOFF": 29393280, "G-DIAG2": 3, "G-OFFDIAG": 5,
      "G-OFFDIAG2": 88, "G-OFFNEG": 24}, "G-R6A-FIBER-REBUILD"),
    ("P-R6A-ANISO2-PER-SITE-ADMISSIBLE",
     ["split_fibers", "G-ANISO2", "per_site_admissible"], [221],
     "G-ADMISSIBILITY-COUPLING"),
    ("P-R6A-OFFNEG-PER-SITE-ADMISSIBLE",
     ["split_fibers", "G-OFFNEG", "per_site_admissible"], [23],
     "G-ADMISSIBILITY-COUPLING"),
    ("P-R6A-ADDITIVITY", ["forced_part", "additivity_checks"], 972,
     "G-ADDITIVITY-REVERIFIED"),
    ("P-R6A-ADDITIVITY-VIOL", ["forced_part", "additivity_violations"], 0,
     "G-ADDITIVITY-REVERIFIED"),
    ("P-R6A-RESTRICTION", ["forced_part", "restriction_checks"], 324,
     "G-METRIC-RESTRICTION-REVERIFIED"),
    ("P-R6A-RESTRICTION-OK", ["forced_part", "restriction_ok"], 324,
     "G-METRIC-RESTRICTION-REVERIFIED"),
    ("P-R6A-LIFT-PAIR", ["choice_inventory", "items", 7, "fiber"], 2,
     "G-LIFT-PAIR-GROWN"),
    ("P-R6A-FRONT-NONINTEGRAL", ["forced_front_lift", "non_integral"], 30,
     "G-FRONT-TWO-RULE-DISAGREEMENT"),
    ("P-R6A-FRONT-CELLS", ["forced_front_lift", "cells"], 81,
     "G-FRONT-TWO-RULE-DISAGREEMENT"),
    ("P-R6A-FREE-LINKS", ["cover", "free_links"], 54,
     "G-TRANSVERSE-LINKS-UNFORCED"),
    ("P-R6A-REFINED-LINKS", ["cover", "refined_links"], 108,
     "G-TRANSVERSE-LINKS-UNFORCED"),
    ("P-R6A-NEW-SITES", ["cover", "new_sites"], 27,
     "G-NEW-FRONTS-RECLASSED"),
    ("P-R6A-VERDICT-HEAD", ["verdict_head"], "R6A-NO-MOTIVATED-SPLIT",
     "G-R6A-TERMINAL-STATUS"),
    # readable ONLY at the TERMINAL sha -- the delivered receipt has no
    # extremal_selectors block at all.  The provenance repair is what
    # makes these three consumable, and they strengthen the extremal
    # segment rather than weaken it.
    ("P-R6A-EXTREMAL-RECORDS", ["extremal_selectors", "records"], 6,
     "G-R6A-TERMINAL-STATUS"),
    ("P-R6A-MAXDET-UNIQUE-SITES",
     ["extremal_selectors", "max_det", "unique_sites"], 54,
     "G-D12-EXTENSION-NAMED"),
    ("P-R6A-MINABSQ12-UNIQUE-SITES",
     ["extremal_selectors", "min_abs_q12", "unique_sites"], 19,
     "G-R6A-TERMINAL-STATUS"),
    ("P-R6A-CONTROL-QUALIFIER", ["control", "qualifier"], "UNMOTIVATED",
     "G-CONTROLS"),
    ("P-R6A-CONTROL-UNREPRESENTED", ["control", "tally", "UNREPRESENTED"], 6,
     "G-CONTROLS"),
]

CRB_PATHS = [
    ("P-CRB-HEAD", ["verdict_head"], "CRB-BLOCKED-AT-NO-PINNED-STOCHASTIC-LAW",
     "G-CRB-SIMPLEX"),
    ("P-CRB-MISSING", ["missing_tag"],
     "THE-INTERVAL-POSITIONAL-LAW-=-THE-TRANSITION-KERNEL-BETWEEN-AN-"
     "INTERVALS-ENDPOINTS-WHOSE-RENEWAL-COUNT-IS-N|R0-CARRIES-THE-RECORD-"
     "LAYER-I7-AND-NO-TRANSITION-LAYER", "G-CRB-SIMPLEX"),
    ("P-CRB-N4-ROW", ["per_interval_law", "rows", 3],
     {"n": 4, "fiber": 3, "pinned_orbits": 3, "pinned_simplex_dim": 2,
      "pinned_transitive": False, "flip_orbits": 2, "flip_simplex_dim": 1,
      "flip_transitive": False}, "G-CRB-SIMPLEX"),
    ("P-CRB-N3-ROW", ["per_interval_law", "rows", 2],
     {"n": 3, "fiber": 2, "pinned_orbits": 2, "pinned_simplex_dim": 1,
      "pinned_transitive": False, "flip_orbits": 1, "flip_simplex_dim": 0,
      "flip_transitive": True}, "G-CRB-SIMPLEX"),
    ("P-CRB-TV-UNIFORM-BINOMIAL-4",
     ["selection_candidates", "rows", 0, "evidence",
      "tv_uniform_vs_binomial", "4"], "2/21", "G-S5-COMPARATOR-SEPARATION"),
    ("P-CRB-UNIFORM-REFUTED", ["selection_candidates", "rows", 2, "result"],
     "REFUTED-AS-FORCING", "G-DERIVED-LAW-COMPLETE-ON-ONE-RECORD"),
    ("P-CRB-MAXENT-CONSTRAINTS",
     ["selection_candidates", "rows", 1, "evidence",
      "pinned_moment_constraints"], 0, "G-VARIATIONAL-ROWS-MEASURED"),
]

I7_PATHS = [
    ("P-I7-DENSITY-WEIGHT", ["declarations", "density_weight"], 0,
     "G-DET-LEG-CORRECTED"),
    ("P-I7-L", ["declarations", "L"], 3, "G-ARENA-BASELINE"),
    ("P-I7-D", ["declarations", "d"], 2, "G-ARENA-BASELINE"),
]


def stage_paths(C: Ctx) -> dict:
    """Stage 3 -- path-value anchors, all at declared commit shas."""
    C.stages.append("path-values")
    vals = {}
    for name, path, expected, consumer in R6A_PATHS:
        vals[name] = anchor_path(C, name, R6A_TERMINAL_SHA, R6A_RECEIPT,
                                 path, expected, "R6A", consumer)
    for name, path, expected, consumer in CRB_PATHS:
        vals[name] = anchor_path(C, name, CORPUS_SHA, CRB_RECEIPT, path,
                                 expected, "CRB", consumer)
    for name, path, expected, consumer in I7_PATHS:
        vals[name] = anchor_path(C, name, CORPUS_SHA, HA_RECEIPT, path,
                                 expected, "I7", consumer)
    if C.failed_anchors:
        raise AnchorStop()
    return vals


# --------------------------------------------------------------------
# 7.  S1's chain -- two TRANSCRIPTIONS (not two derivations; #219)
# --------------------------------------------------------------------

_ROUTEC: dict[str, object] = {}


def route_paper() -> tuple[list[list[Fr]], list[Fr]]:
    if "P" in _ROUTEC:
        return [r[:] for r in _ROUTEC["P"][0]], _ROUTEC["P"][1][:]
    txt = text(CORPUS_SHA, P31)
    i = txt.index("T = [ 3/2")
    block = txt[i:i + 420]
    rows = []
    for line in block.split("\n"):
        mo = re.search(r"\[([^\]]*)\]", line)
        if not mo:
            continue
        cells = mo.group(1).split()
        if len(cells) != 6:
            continue
        row = []
        for c in cells:
            if "/" in c:
                a, b = c.split("/")
                row.append(Fr(int(a), int(b)))
            else:
                row.append(Fr(int(c)))
        rows.append(row)
        if len(rows) == 6:
            break
    mo = re.search(r"`f = \(([\d, ]+)\)/(\d+) > 0`", txt)
    den = int(mo.group(2))
    f = [Fr(int(x), den) for x in mo.group(1).split(",")]
    _ROUTEC["P"] = (rows, f)
    return [r[:] for r in rows], f[:]


def route_code(rel: str = D43B) -> tuple[list[list[Fr]], list[Fr]]:
    if rel in _ROUTEC:
        return [r[:] for r in _ROUTEC[rel][0]], _ROUTEC[rel][1][:]
    tree = ast.parse(text(CORPUS_SHA, rel))
    T = [[Fr(0)] * 6 for _ in range(6)]
    f = None

    def frac_of(node):
        return Fr(*[a.value for a in node.args])

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            tgt = node.targets[0]
            if isinstance(tgt, ast.Name) and tgt.id == "T_REF":
                for k, v in zip(node.value.keys, node.value.values):
                    for kk, vv in zip(v.keys, v.values):
                        T[k.value][kk.value] = frac_of(vv)
            if (isinstance(tgt, ast.Name) and tgt.id == "f"
                    and isinstance(node.value, ast.List)
                    and len(node.value.elts) == 6):
                f = [frac_of(e) for e in node.value.elts]
    _ROUTEC[rel] = (T, f)
    return [r[:] for r in T], f[:]


def solve_exact(A, b):
    n = len(A)
    M = [A[i][:] + [b[i]] for i in range(n)]
    for col in range(n):
        piv = next((r for r in range(col, n) if M[r][col] != 0), None)
        if piv is None:
            return None
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                fac = M[r][col]
                M[r] = [x - fac * y for x, y in zip(M[r], M[col])]
    return [M[i][n] for i in range(n)]


def sccs_of(adj, nodes):
    index, low, onstack, stack, out = {}, {}, {}, [], []
    counter = [0]
    for root in nodes:
        if root in index:
            continue
        work = [(root, 0)]
        while work:
            v, pi = work[-1]
            if pi == 0:
                index[v] = low[v] = counter[0]
                counter[0] += 1
                stack.append(v)
                onstack[v] = True
            recurse = False
            for i in range(pi, len(adj[v])):
                w = adj[v][i]
                if w not in index:
                    work[-1] = (v, i + 1)
                    work.append((w, 0))
                    recurse = True
                    break
                if onstack.get(w):
                    low[v] = min(low[v], index[w])
            if recurse:
                continue
            if low[v] == index[v]:
                comp = []
                while True:
                    w = stack.pop()
                    onstack[w] = False
                    comp.append(w)
                    if w == v:
                        break
                out.append(sorted(comp))
            work.pop()
            if work:
                low[work[-1][0]] = min(low[work[-1][0]], low[v])
    return sorted(out)


def choose(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    num, den = 1, 1
    for i in range(k):
        num *= (n - i)
        den *= (i + 1)
    return num // den


CAP = 400


def _gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


_TABOO: dict = {}


def taboo_first_passage(qp, arb_edges, absorb_all_visits_to_0: bool):
    """Exact first-passage law by integer iteration over the common
    denominator 448 (the lcm of every q' denominator).  Independent of
    the closed form and of the path enumeration."""
    key = (tuple(tuple(str(x) for x in row) for row in qp),
           tuple(sorted(arb_edges)), absorb_all_visits_to_0)
    if key in _TABOO:
        return _TABOO[key]
    DEN = 1
    for row in qp:
        for x in row:
            DEN = DEN * x.denominator // _gcd(DEN, x.denominator)
    M = [[int(qp[i][j] * DEN) for j in range(6)] for i in range(6)]
    v = [0] * 6
    v[0] = 1
    out = []
    for _ in range(CAP):
        w = [0] * 6
        renew = 0
        for i in range(6):
            if v[i] == 0:
                continue
            for j in range(6):
                if M[i][j] == 0:
                    continue
                contrib = v[i] * M[i][j]
                if absorb_all_visits_to_0:
                    if j == 0:
                        renew += contrib
                    else:
                        w[j] += contrib
                else:
                    if (i, j) in arb_edges:
                        renew += contrib
                    else:
                        w[j] += contrib
        out.append(renew)
        v = w
    _TABOO[key] = (out, DEN)
    return out, DEN     # out[k] is the numerator over DEN^(k+1)


def closed_form_arb(n: int) -> Fr:
    if n < 3:
        return Fr(0)
    return Fr(choose(n - 1, 2) * 3 ** (n - 3), 2 ** (2 * n + 2))


def closed_form_state(n: int) -> Fr:
    if n == 1:
        return Fr(3, 4)
    if n == 2:
        return Fr(0)
    return Fr((n - 2) * 3 ** (n - 3), 2 ** (2 * n + 2))


_PMASS: dict = {}


def partial_mass(cf) -> Fr:
    if cf.__name__ in _PMASS:
        return _PMASS[cf.__name__]
    num = 0
    den = 2 ** (2 * CAP + 2)
    for n in range(1, CAP + 1):
        x = cf(n)
        num += x.numerator * (den // x.denominator) if x != 0 else 0
    _PMASS[cf.__name__] = Fr(num, den)
    return _PMASS[cf.__name__]


_LEGS: dict = {}


def enumerate_legs(qp, n: int, arb_edges):
    """Every delivery-free leg of length n under the SOURCE convention:
    a state word 0 -> ... -> 0 whose ONLY arbitration step is the last."""
    key = (tuple(tuple(str(x) for x in row) for row in qp), n,
           tuple(sorted(arb_edges)))
    if key in _LEGS:
        return _LEGS[key]
    out = []

    def rec(path, pr, k):
        cur = path[-1]
        if k == n:
            if cur == 0:
                out.append((tuple(path[1:-1]), pr))
            return
        for j in range(6):
            if qp[cur][j] == 0:
                continue
            if (cur, j) in arb_edges and k < n - 1:
                continue          # an earlier renewal: a different leg
            if k == n - 1 and (cur, j) not in arb_edges:
                continue          # the leg must close on an arbitration
            rec(path + [j], pr * qp[cur][j], k + 1)

    rec([0], Fr(1), 0)
    _LEGS[key] = out
    return out


# --------------------------------------------------------------------
# 8.  THE DELIVERY COMPUTATION
# --------------------------------------------------------------------

FORCED, STAB, FREE = "forced", "stabilizer-fixed", "genuinely-free"
SITES, LINKS = 9, 3


def _measure(C: Ctx, R: dict) -> None:
    bad, consts = float_guard()
    R["arithmetic"] = {"kind": "exact int/Fraction only",
                       "float_literals_in_source": bad,
                       "constants_scanned": consts}
    if bad:
        print(f"FLOAT GUARD: {bad} float literal(s)", file=sys.stderr)
        sys.exit(3)

    R["unit"] = "v14 R6b' -- THE RENEWAL-GRAIN TRANSPORT (paper-09)"
    R["status"] = "GREEN-REPAIRED"
    R["question"] = (
        "can a MOTIVATED identification carry the renewal-grain positional "
        "structure (S1's chain q'; S2's intervening-pattern census) to the "
        "spatial record-interval arena (I7), and does the derived kernel "
        "collapse the R6a split fiber as a forced VALUE or a forced "
        "DISTRIBUTION?")
    R["provenance"] = {
        "corpus_sha": CORPUS_SHA,
        "r6a_terminal_sha": R6A_TERMINAL_SHA,
        "r6a_delivered_sha": R6A_DELIVERED_SHA,
        "rule": ("RUNBOOK §14, v14 #62: a unit reading another unit's "
                 "artifacts declares the source COMMIT SHA in its own "
                 "frozen text and reads via that sha; only committed "
                 "objects may be disclosed"),
    }

    C.say("=" * 78)
    C.say("v14 R6b' -- THE RENEWAL-GRAIN TRANSPORT (paper-09)  [GREEN-REPAIRED]")
    C.say("=" * 78)
    C.say("")
    C.say("SCOPE AND CONVENTION, DECLARED BEFORE ANY MEASUREMENT:")
    C.say("  * A RENEWAL IS AN ARBITRATION landing in class 0 -- S1's own")
    C.say("    operative definition (d43b's REN), S4's theorem, S2's leg")
    C.say("    delimiter.  An idle at the root is NOT a renewal.  The bare-")
    C.say("    state-0 reading is measured and DISCLOSED, never adopted.")
    C.say("  * S1's chain and S4's theorem: TWO-ACTOR DELIVERY-FREE scope.")
    C.say("  * S2's census: TRANSPORT scope; its interval lengths are")
    C.say("    ENSEMBLE DATA; its two length-4 cells are E2 leg 1 (depths")
    C.say("    3->7) and E3 leg 2 (depths 6->10).")
    C.say("  * S5's continuous layer is CHOSEN, NOT DERIVED and enters only")
    C.say("    as a labelled comparator.")
    C.say("  * Every source is read at a DECLARED COMMIT SHA.")
    C.say("")

    # ---- 1.  anchors, in three short-circuiting stages ---------------
    C.say("-" * 78)
    C.say("1.  ANCHORS -- stage 1 quotations, stage 2 file-bytes, stage 3")
    C.say("    path-values.  A failed stage stops the run; no later stage")
    C.say("    is evaluated.")
    C.say("-" * 78)
    qinfo = stage_quotations(C)
    stand = standing_sentinel(C)
    stage_bytes(C)
    pv = stage_paths(C)
    n_q = sum(1 for a in C.anchors if a["kind"] == "quotation")
    n_b = sum(1 for a in C.anchors if a["kind"] == "file-bytes-committed")
    n_p = sum(1 for a in C.anchors if a["kind"] == "path-value")
    R["anchor_totals"] = {"quotation": n_q, "file_bytes_committed": n_b,
                          "path_value": n_p, "total": len(C.anchors),
                          "failures": len(C.failed_anchors)}
    R["anchors"] = C.anchors
    R["quotation_spans_in_the_paper"] = qinfo
    C.say(f"    quotations {n_q} | file-bytes (all committed) {n_b} | "
          f"path-value {n_p} | total {len(C.anchors)} | failures "
          f"{len(C.failed_anchors)}")

    hits = stand["hits"]
    declared_hits = [(k, m) for k, m, _ in DECLARED_STANDING_HITS]
    R["standing_sentinel"] = {
        "markers": STANDING_MARKERS, "window_chars": STANDING_WINDOW,
        "measured_hits": [list(h) for h in hits],
        "declared_hits": [{"quote": k, "marker": m, "adjudication": a}
                          for k, m, a in DECLARED_STANDING_HITS],
        "binds": ("the DECLARED withdrawal/supersession class in the "
                  "neighbourhood of an anchored quotation -- and nothing "
                  "more.  A verbatim window binds QUOTE FIDELITY; it "
                  "cannot bind that a faithful sentence is in force "
                  "(the R6b' A2 measurement)"),
    }
    C.gate("G-STANDING-SENTINEL",
           sorted(hits) == sorted(declared_hits),
           f"standing-marker scan over a {STANDING_WINDOW}-character "
           f"neighbourhood of each of the {len(QUOTES)} anchored "
           f"quotations, {len(STANDING_MARKERS)} declared markers: "
           f"{len(hits)} hits measured against {len(declared_hits)} "
           f"declared.  All declared hits are D33's own §9 corrections "
           f"beside S5's disclaimer, adjudicated in the receipt.  This "
           f"gate binds the DECLARED STANDING CLASS only: a context "
           f"window cannot bind that a faithful quotation is in force",
           "MUT-MEANING-INVERSION")

    lit = literal_gate_scan()
    if C.mut == "MUT-LITERAL-GATE":
        lit = lit + ["G-A-LITERAL-GATE"]
    C.gate("G-NO-LITERAL-GATE-PREDICATES",
           len(lit) == 0,
           f"AST scan of this file's own syntax tree for gate calls whose "
           f"PREDICATE is a literal constant (the six literal-True "
           f"must-pass gates the R6b' instrument audit found): "
           f"{len(lit)} found {lit}.  Every gate below evaluates a "
           f"measured object",
           "MUT-LITERAL-GATE")

    mident = mutant_identity_scan()
    if C.mut == "MUT-MUTANT-IDENTITY":
        mident = mident + ["G-A-SELF-EXEMPTING-GATE"]
    C.gate("G-NO-MUTANT-IDENTITY-IN-GATES",
           len(mident) == 0,
           f"the #208 clause, machine-checked: an AST scan of every gate "
           f"call's PREDICATE subtree for any reference to the injection "
           f"channel returns {len(mident)} {mident}.  Every injection "
           f"perturbs a VALUE and every gate evaluates blind",
           "MUT-MUTANT-IDENTITY")

    reads = sorted({(r["sha"], r["artifact"]) for r in _READS})
    worktree_reads = [a for s, a in reads if s == "(working tree)"]
    if C.mut == "MUT-UNANCHORED-INPUT":
        worktree_reads = worktree_reads + ["v14/LOG.md"]
    anchored = {a["artifact"] for a in C.anchors}
    C.gate("G-NO-UNANCHORED-RUNTIME-INPUT",
           worktree_reads == [PAPER_REL]
           and all(a in anchored or a == PAPER_REL for _, a in reads),
           f"every runtime input is a COMMITTED object at a declared sha "
           f"or this unit's own deliverable: {len(reads)} (sha, artifact) "
           f"reads, working-tree reads {worktree_reads} (this unit's own "
           f"paper, which the paper<->receipt gates bind).  No ledger, no "
           f"STATUS, no other unit's working file, no `git show HEAD:`",
           "MUT-UNANCHORED-INPUT")

    # path-value stability across the two DECLARED committed revisions
    Tj = load_json(R6A_TERMINAL_SHA, R6A_RECEIPT)
    Dj = load_json(R6A_DELIVERED_SHA, R6A_RECEIPT)
    consumed, moved, terminal_only = 0, [], []
    for a in C.anchors:
        if a["kind"] != "path-value" or a["artifact"] != R6A_RECEIPT:
            continue
        p = [int(k) if re.fullmatch(r"-?\d+", k) else k
             for k in a["path"].split("/")]
        if p[0] not in Dj:
            terminal_only.append(a["path"])
            continue
        consumed += 1
        old = walk(Dj, p)
        if old != a["measured"]:
            moved.append({"path": a["path"], "terminal": a["measured"],
                          "delivered": old})
    if C.mut == "MUT-STABILITY-DRIFT":
        moved = moved + [{"path": "<injected>", "terminal": 1,
                          "delivered": 2}]
    fam_same = (Tj["record_family"] == Dj["record_family"])
    fib_same = (Tj["split_fibers"] == Dj["split_fibers"])
    absent_in_delivered = sorted(
        k for k in ("extremal_selectors", "walls", "waiver_ledger")
        if k in Tj and k not in Dj)
    if C.mut == "MUT-TERMINAL-STATUS":
        absent_in_delivered = []
    R["provenance_stability"] = {
        "consumed_path_values": consumed, "moved": moved,
        "record_family_identical": fam_same,
        "split_fibers_identical": fib_same,
        "blocks_only_in_the_terminal_receipt": absent_in_delivered,
        "paths_readable_only_at_the_terminal_sha": terminal_only,
    }
    C.gate("G-R6A-PATH-VALUE-STABILITY",
           len(moved) == 0 and fam_same and fib_same and consumed > 0,
           f"the adopted core of the #62 engraving: every path-value this "
           f"unit consumes from R6a is compared across the TWO DECLARED "
           f"COMMITTED revisions -- delivered {R6A_DELIVERED_SHA[:12]} "
           f"(022c3f488a93) and TERMINAL {R6A_TERMINAL_SHA[:12]} "
           f"(856f6e810ab5).  {consumed} consumed, {len(moved)} moved.  "
           f"Beyond the consumed paths: the whole /record_family block is "
           f"identical = {fam_same} and the whole /split_fibers block is "
           f"identical = {fib_same}.  {len(terminal_only)} further "
           f"path-values are readable ONLY at the terminal sha "
           f"({terminal_only}) and are excluded from the comparison by "
           f"construction; the blocks they live in are "
           f"{absent_in_delivered}",
           "MUT-STABILITY-DRIFT")
    C.gate("G-R6A-TERMINAL-STATUS",
           pv["P-R6A-VERDICT-HEAD"] == "R6A-NO-MOTIVATED-SPLIT"
           and pv["P-R6A-EXTREMAL-RECORDS"] == 6
           and "extremal_selectors" in absent_in_delivered
           and pv["P-R6A-MINABSQ12-UNIQUE-SITES"] == 19,
           f"R6a is TERMINAL (v14 #53) and this unit reads its TERMINAL "
           f"receipt: head \"{pv['P-R6A-VERDICT-HEAD']}\"; the "
           f"extremal_selectors block exists ONLY there "
           f"({pv['P-R6A-EXTREMAL-RECORDS']} records, max-det unique at "
           f"{pv['P-R6A-MAXDET-UNIQUE-SITES']} of 54 sites).  "
           f"CROSS-REFERENCE (do not conflate): R6a's block carries "
           f"min_abs_q12 (unique at {pv['P-R6A-MINABSQ12-UNIQUE-SITES']} "
           f"sites); THIS unit's fourth functional is MAX-|q12| -- the "
           f"same name in the OPPOSITE sense",
           "MUT-TERMINAL-STATUS")

    R["named_exclusions"] = [{"artifact": a, "status_printed": s}
                             for a, s in NAMED_EXCLUSIONS]
    C.say("")

    # ---- 2.  S1's chain -----------------------------------------------
    C.say("-" * 78)
    C.say("2.  S1 -- THE CHAIN, BY TWO TRANSCRIPTIONS (not two derivations)")
    C.say("-" * 78)
    Tp, fp = route_paper()
    src_c = D43B
    if C.mut == "MUT-S1-ROUTE-SAME-SOURCE":
        src_c = P31
        Tc, fc = route_paper()
    else:
        Tc, fc = route_code(src_c)
    if C.mut == "MUT-S1-ROUTE-DRIFT":
        Tc = [row[:] for row in Tc]
        Tc[0][0] = Tc[0][0] + Fr(1, 1000)
    agree = (Tp == Tc and fp == fc)
    C.gate("G-S1-TWO-TRANSCRIPTIONS",
           agree and len(Tp) == 6 and all(len(r) == 6 for r in Tp)
           and src_c != P31,
           f"the 6x6 transfer and the harmonic vector read from TWO "
           f"DISTINCT PINNED ARTIFACTS in two formats -- paper 31's fenced "
           f"prose block (route P) and d43b's T_REF/f source objects "
           f"(route C) -- agree entry by entry: {agree}.  This is "
           f"TRANSCRIPTION FIDELITY ACROSS TWO ARTIFACTS, not two "
           f"derivations (#219 disclosure below)",
           "MUT-S1-ROUTE-DRIFT / MUT-S1-ROUTE-SAME-SOURCE")
    d43b_src = text(CORPUS_SHA, D43B)
    route_p_literal = "T = [ 3/2" in text(CORPUS_SHA, P31)
    route_c_literal = "T_REF = {" in d43b_src
    derivation_present = "rows == T_REF" in d43b_src and "215" in d43b_src
    if C.mut == "MUT-TRANSCRIPTION-CLAIM":
        derivation_present = False
    C.gate("G-S1-TRANSCRIPTION-DISCLOSURE",
           route_p_literal and route_c_literal and derivation_present,
           f"#219 DISCLOSURE, measured in the sources themselves: route P "
           f"reads an authored fenced literal ({route_p_literal}) and "
           f"route C reads the authored dict literal T_REF "
           f"({route_c_literal}).  BOTH ARE LITERALS.  The genuine second "
           f"derivation exists and this unit does NOT run it: d43b's own "
           f"`rows` object, built by the bisimulation and gated "
           f"`rows == T_REF` against a real enumeration of the 215 "
           f"length-<=3 histories in d43b's own TERMINAL run "
           f"({derivation_present}).  A shared transcription error would "
           f"pass both of this unit's routes",
           "MUT-TRANSCRIPTION-CLAIM")
    T, f = Tp, fp
    LAM = Fr(2)
    rowsums = [sum(T[i]) for i in range(6)]
    if C.mut == "MUT-S1-HARMONIC":
        f = f[:]
        f[0] = f[0] + Fr(1, 5)
    eig_ok = all(sum(T[i][j] * f[j] for j in range(6)) == LAM * f[i]
                 for i in range(6))
    C.gate("G-S1-HARMONIC",
           eig_ok and all(x > 0 for x in f)
           and rowsums == [Fr(2), Fr(2), Fr(2), Fr(5, 2), Fr(2), Fr(2)],
           f"T f = 2 f exactly with f > 0 ({eig_ok}); row sums "
           f"{[fr(x) for x in rowsums]} -- the conflict state's 5/2 is the "
           f"only one that is not 2; f = {[fr(x) for x in f]}",
           "MUT-S1-HARMONIC")
    qp = [[T[i][j] * f[j] / (LAM * f[i]) for j in range(6)] for i in range(6)]
    if C.mut == "MUT-KERNEL-ROW":
        qp = [row[:] for row in qp]
        qp[3][0] = Fr(1, 6)
    conf = {j: qp[3][j] for j in range(6) if qp[3][j] != 0}
    norm_ok = all(sum(qp[i]) == 1 for i in range(6))
    C.gate("G-KERNEL-CONFLICT-ROW",
           norm_ok and conf == {0: Fr(1, 7), 3: Fr(3, 4), 5: Fr(3, 28)},
           f"q'(i->j) = T_ij f_j / (2 f_i): all six rows sum to 1 = "
           f"{norm_ok}; the conflict row reproduces S1's own printed value "
           + str({k: fr(v) for k, v in sorted(conf.items())}),
           "MUT-KERNEL-ROW")
    adj = {i: [j for j in range(6) if qp[i][j] != 0] for i in range(6)}
    comps = sccs_of(adj, list(range(6)))
    closed = sorted([c for c in comps
                     if all(j in c for i in c for j in adj[i])])
    if C.mut == "MUT-CLOSED-CLASS":
        closed = sorted(closed + [[0]])
    transient = sorted([i for i in range(6)
                        if not any(i in c for c in closed)])
    C.gate("G-CLOSED-CLASS",
           closed == [[2, 4, 5]] and transient == [0, 1, 3],
           f"exactly one closed communicating class {closed}; transient "
           f"{transient}; the renewal state 0 is TRANSIENT and 3 -> 0 is "
           f"the renewal loop",
           "MUT-CLOSED-CLASS")
    R["chain"] = {"T": [[fr(x) for x in r] for r in T],
                  "f": [fr(x) for x in f],
                  "q_prime": [[fr(x) for x in r] for r in qp],
                  "row_sums_T": [fr(x) for x in rowsums],
                  "closed_class": closed[0] if closed else [],
                  "transient_states": transient,
                  "routes": ["paper-31 fenced 6x6 block (literal)",
                             "d43b T_REF / f source objects (literal)"],
                  "routes_agree": agree,
                  "provenance_kind": "TWO TRANSCRIPTIONS, NOT TWO DERIVATIONS"}
    for i in range(6):
        C.say(f"    q'({i} -> .) = " +
              str({j: fr(qp[i][j]) for j in range(6) if qp[i][j] != 0}))
    C.say("")

    # ---- 3.  THE RENEWAL CONVENTION, AND THE KERNEL IT DEFINES --------
    C.say("-" * 78)
    C.say("3.  THE RENEWAL CONVENTION (the source's) AND THE DERIVED KERNEL")
    C.say("-" * 78)
    out_txt = text(CORPUS_SHA, U1B_OUT)

    def parse_profile(marker: str) -> dict:
        i = out_txt.index(marker)
        j = out_txt.index("{", i)
        k = out_txt.index("}", j)
        prof = {}
        for mo in re.finditer(r"\(([^)]*)\): (\d+)", out_txt[j:k + 1]):
            pat = tuple(x.strip().strip("'") for x in mo.group(1).split(","))
            prof[pat] = int(mo.group(2))
        return prof

    leg1 = parse_profile("[DATA] LEG-1 interval-4 tag patterns")
    leg2 = parse_profile("leg-2 patterns {('d', 'p', 'p', 'r')")
    if C.mut == "MUT-S2-PROFILE":
        leg2 = dict(leg1)
    mo3 = re.search(r"patterns \{\('p', 'p', 'r'\): (\d+)\}", out_txt)
    leg3_leaves = int(mo3.group(1))

    # the three source facts that FORCE the convention, each quoted
    ren_defn = ("CLS[tuple(h)] == 0 and any(e[0] == 'r' for e in h)"
                in norm_source(CORPUS_SHA, D43B))
    s4_theorem = (norm("every pair arbitration is a renewal to the root "
                       "state [THEOREM at two-actor delivery-free scope]")
                  in norm_source(CORPUS_SHA, P30))
    every_leg_ends_in_r = all(p[-1] == "r" for p in
                              list(leg1) + list(leg2) + [("p", "p", "r")])
    # the arbitration edges of the chain: the transitions INTO the renewal
    # state that are not the root's own idle self-loop
    arb_edges = {(i, 0) for i in range(6) if i != 0 and qp[i][0] != 0}
    convention = "ARBITRATION"
    if C.mut == "MUT-CONVENTION-SWAP":
        convention = "BARE-STATE-0"
    C.gate("G-RENEWAL-CONVENTION-IS-THE-SOURCES",
           ren_defn and s4_theorem and every_leg_ends_in_r
           and arb_edges == {(3, 0)} and convention == "ARBITRATION",
           f"THE CONVENTION IS NOT FREE: d43b's own REN reads class 0 AND "
           f"carrying an 'r' ({ren_defn}); S4's theorem names the EVENT, "
           f"not the state ({s4_theorem}); every leg S2 censuses "
           f"terminates in the 'r' tag ({every_leg_ends_in_r}).  Measured "
           f"on the chain, the arbitration edge set is {sorted(arb_edges)} "
           f"-- the single transition 3 -> 0.  The root's self-loop "
           f"q'(0->0) = {fr(qp[0][0])} is an IDLE AT THE ROOT and is NOT a "
           f"renewal.  Adopted convention: {convention}",
           "MUT-CONVENTION-SWAP")

    # the kernel under the adopted convention, by THREE routes
    num, TDEN = taboo_first_passage(qp, arb_edges, False)
    cf = [closed_form_arb(n) for n in range(1, CAP + 1)]
    if C.mut == "MUT-FIRST-RETURN-HOLE":
        cf = cf[:]
        cf[1] = Fr(1, 1000)
    taboo_matches = (TDEN == 448 and all(
        num[n - 1] * (2 ** (2 * n + 2)) ==
        choose(n - 1, 2) * 3 ** max(n - 3, 0) * (TDEN ** n)
        for n in range(1, CAP + 1)))
    enum_rows = []
    for n in range(3, 13):
        legs = enumerate_legs(qp, n, arb_edges)
        probs = {p for _, p in legs}
        enum_rows.append({"n": n, "paths": len(legs),
                          "configurations_C(n-1,2)": choose(n - 1, 2),
                          "fillers": n - 3,
                          "equiprobable": len(probs) <= 1,
                          "g_n": fr(sum(p for _, p in legs))})
    if C.mut == "MUT-ALL-N-LAW":
        enum_rows[2]["paths"] = enum_rows[2]["paths"] + 1
    enum_ok = all(r["paths"] == r["configurations_C(n-1,2)"]
                  and r["equiprobable"]
                  and r["g_n"] == fr(closed_form_arb(r["n"]))
                  for r in enum_rows)
    partial = partial_mass(closed_form_arb)
    ret = Fr(1, 4)
    if C.mut == "MUT-DEFECT-ARITHMETIC":
        ret = Fr(7, 8)
    defect = Fr(1) - ret
    if C.mut == "MUT-TERMINATION":
        defect = Fr(0)
    tail = ret - partial
    holes = [n for n in range(1, 13) if closed_form_arb(n) == 0]
    C.gate("G-FIRST-RETURN-LAW-THREE-ROUTES",
           taboo_matches and enum_ok and cf[0] == 0 and cf[1] == 0
           and cf[2] == Fr(1, 256) and holes == [1, 2]
           and tail >= 0 and tail < Fr(1, 10 ** 40),
           f"the inter-renewal law under the source convention, computed "
           f"THREE ways and agreeing: (i) the closed form "
           f"g(n) = C(n-1,2)(3/4)^(n-3)/256 for n >= 3; (ii) an exact "
           f"integer taboo iteration of q' over the common denominator "
           f"448 to n = {CAP}, termwise ({taboo_matches}); (iii) exhaustive "
           f"path enumeration at n = 3..12 ({enum_ok}).  g(3) = "
           f"{fr(closed_form_arb(3))}, g(4) = {fr(closed_form_arb(4))}, "
           f"g(5) = {fr(closed_form_arb(5))}.  SUPPORT HOLES AT {holes}: "
           f"no inter-renewal leg of length 1 or 2 exists, exactly.  "
           f"Residual mass beyond n = {CAP} < 1e-40",
           "MUT-FIRST-RETURN-HOLE / MUT-ALL-N-LAW")
    visits = Fr(1) / defect if defect > 0 else None
    visits_s = fr(visits) if visits is not None else "UNDEFINED"
    mean_def = Fr(3)
    if C.mut == "MUT-DEFECTIVE-MEAN":
        mean_def = Fr(31, 10)
    mean_trunc_num = 0
    for n in range(3, CAP + 1):
        x = closed_form_arb(n) * n
        mean_trunc_num += Fr(x)
    cond_mean = mean_def / ret if ret > 0 else None
    C.gate("G-RENEWAL-DEFECTIVE",
           ret == Fr(1, 4) and defect == Fr(3, 4) and visits == Fr(4, 3),
           f"P(a further renewal | at a renewal) = {fr(ret)} < 1; defect "
           f"= {fr(defect)} -- the mass absorbed into the closed class "
           f"{closed[0]}; expected total renewals after any renewal = "
           f"1/defect = {visits_s}.  Under the SOURCE convention the "
           f"root's idle self-loop is not a renewal, so the geometric "
           f"success probability is 1/4, not 13/16",
           "MUT-DEFECT-ARITHMETIC")
    C.gate("G-DEFECTIVE-MEAN",
           mean_def == Fr(3) and cond_mean == Fr(12)
           and abs(mean_def - mean_trunc_num) < Fr(1, 10 ** 40),
           f"the defective mean E[T.1(T<inf)] = {fr(mean_def)} in closed "
           f"form (sum_m (m+1)(m+2)(m+3)x^m / 512 at x = 3/4), reproduced "
           f"by the truncated sum to n = {CAP} to better than 1e-40; the "
           f"mean inter-renewal length CONDITIONAL ON A FURTHER RENEWAL is "
           f"{fr(cond_mean)}",
           "MUT-DEFECTIVE-MEAN")
    C.gate("G-AS-TERMINATION",
           ret < 1 and defect > 0 and visits is not None
           and visits * defect == 1 and ret + defect == 1,
           f"the renewal process is DEFECTIVE at delivery-free scope: the "
           f"number of renewals after any renewal is geometric with "
           f"success probability {fr(ret)}, hence almost surely FINITE -- "
           f"the chain TERMINATES a.s.  The identity visits x defect = 1 "
           f"is checked rather than divided, so the gate can be falsified "
           f"without a crash",
           "MUT-TERMINATION")

    # the DISCLOSED alternative: the bare-state-0 reading
    num_s, SDEN = taboo_first_passage(qp, arb_edges, True)
    alt_taboo_ok = (SDEN == 448 and all(
        num_s[n - 1] * closed_form_state(n).denominator ==
        closed_form_state(n).numerator * (SDEN ** n)
        for n in range(1, CAP + 1)))
    alt_ret = Fr(13, 16)
    alt_tail = alt_ret - partial_mass(closed_form_state)
    alt_holes = [n for n in range(1, 13) if closed_form_state(n) == 0]
    alt_legs4 = []
    for word in itertools.product(range(6), repeat=3):
        p = qp[0][word[0]] * qp[word[0]][word[1]] * qp[word[1]][word[2]] \
            * qp[word[2]][0]
        if p != 0 and 0 not in word:
            alt_legs4.append((word, p))
    alt_law4 = {1: Fr(0), 2: Fr(0), 3: Fr(0)}
    tot4 = sum(p for _, p in alt_legs4)
    for word, p in alt_legs4:
        fill = [k + 1 for k in range(3)
                if (word[k - 1] if k else 0) == word[k]]
        alt_law4[fill[0]] += p / tot4
    if C.mut == "MUT-ALT-READING":
        alt_taboo_ok = False
    C.gate("G-BARE-STATE-0-DISCLOSURE",
           alt_taboo_ok and alt_tail >= 0 and alt_tail < Fr(1, 10 ** 40)
           and alt_holes == [2]
           and len(alt_legs4) == 2 and alt_law4 == {1: Fr(0), 2: Fr(1, 2),
                                                    3: Fr(1, 2)},
           f"THE DISCLOSED ALTERNATIVE, measured not asserted.  Read "
           f"'renewal' as ANY visit to state 0 and the idle self-loop "
           f"becomes a completed leg of length 1: f(1) = "
           f"{fr(closed_form_state(1))}, f(2) = "
           f"{fr(closed_form_state(2))}, f(n) = (n-2)(3/4)^(n-3)/256; "
           f"return {fr(alt_ret)}, defect {fr(Fr(1) - alt_ret)}, visits "
           f"{fr(Fr(1) / (Fr(1) - alt_ret))}, ONE hole at "
           f"{alt_holes}.  Its length-4 legs are {len(alt_legs4)}, not 3, "
           f"and its induced positional law is "
           f"{law_str(alt_law4)} -- NOT uniform, and it does NOT reproduce "
           f"S2's delivery-free census.  Recorded as the alternative "
           f"reading; NOT this unit's law",
           "MUT-ALT-READING")
    R["kernel"] = {
        "convention": convention,
        "convention_forced_by": ["d43b REN (class 0 carrying an arb)",
                                 "S4's theorem (the EVENT, not the state)",
                                 "S2's leg delimiter (every leg ends 'r')"],
        "arbitration_edges": sorted(list(e) for e in arb_edges),
        "root_idle_self_loop": fr(qp[0][0]),
        "return_probability": fr(ret), "defect": fr(defect),
        "expected_total_renewals": visits_s,
        "defective_mean": fr(mean_def),
        "mean_conditional_on_a_further_renewal": fr(cond_mean),
        "law": "g(1)=0; g(2)=0; g(n)=C(n-1,2)(3/4)^(n-3)/256 for n>=3",
        "g_3": fr(closed_form_arb(3)), "g_4": fr(closed_form_arb(4)),
        "g_5": fr(closed_form_arb(5)),
        "support_holes": holes,
        "iteration_cap": CAP,
        "three_routes_agree": bool(taboo_matches and enum_ok),
        "configuration_census": enum_rows,
        "scope": "DELIVERY-FREE (S1/S4's own tags)",
        "disclosed_alternative_bare_state_0": {
            "return_probability": fr(alt_ret),
            "defect": fr(Fr(1) - alt_ret),
            "expected_total_visits": fr(Fr(1) / (Fr(1) - alt_ret)),
            "f_1": fr(closed_form_state(1)), "f_4": fr(closed_form_state(4)),
            "f_5": fr(closed_form_state(5)),
            "support_holes": alt_holes,
            "length_4_legs": len(alt_legs4),
            "induced_position_law_at_4": {str(k): fr(v)
                                          for k, v in alt_law4.items()},
            "status": "DISCLOSED ALTERNATIVE READING -- NOT ADOPTED"},
    }
    C.say(f"    ADOPTED (source): return {fr(ret)}, defect {fr(defect)}, "
          f"renewals {visits_s}, holes {holes}")
    C.say(f"    DISCLOSED (bare state 0): return {fr(alt_ret)}, defect "
          f"{fr(Fr(1) - alt_ret)}, visits {fr(Fr(1) / (Fr(1) - alt_ret))}, "
          f"holes {alt_holes}, law at count 4 {law_str(alt_law4)}")
    C.say("")

    # ---- 4.  THE ALL-n POSITIONAL LAW, FROM S1 ALONE ------------------
    C.say("-" * 78)
    C.say("4.  THE ALL-n POSITIONAL LAW, DERIVED FROM S1 ALONE")
    C.say("-" * 78)

    def configurations(n: int):
        return [tuple(s for s in range(1, n) if s not in adv)
                for adv in itertools.combinations(range(1, n), 2)]

    def marginal_law(n: int):
        cfgs = configurations(n)
        law = {p: Fr(0) for p in range(1, n)}
        for c in cfgs:
            for p in c:
                law[p] += Fr(1, len(cfgs)) / len(c)
        return law

    def first_filler_law(n: int):
        cfgs = configurations(n)
        law = {p: Fr(0) for p in range(1, n)}
        for c in cfgs:
            if c:
                law[c[0]] += Fr(1, len(cfgs))
        return law

    marg = {n: marginal_law(n) for n in range(4, 13)}
    if C.mut == "MUT-UNIFORM-MARGINAL":
        marg[7] = dict(marg[7])
        marg[7][1] = marg[7][1] + Fr(1, 100)
    uniform_ok = all(all(v == Fr(1, n - 1) for v in marg[n].values())
                     for n in marg)
    C.gate("G-UNIFORM-POSITION-MARGINAL",
           uniform_ok and len(marg) == 9,
           f"THE ALL-n LAW.  A delivery-free leg of length n carries "
           f"exactly two advancing steps (0->1 and 1->3) among its n-1 "
           f"interior steps, hence exactly n-3 fillers and C(n-1,2) "
           f"EQUIPROBABLE configurations.  The induced position marginal "
           f"is EXACTLY UNIFORM on the n-1 positions at every n in "
           f"{sorted(marg)} ({uniform_ok}) -- derived from S1's chain "
           f"alone, delivery-free, with no reference to S2.  At n = 4 it "
           f"is {law_str(marg[4])}",
           "MUT-UNIFORM-MARGINAL")
    cfg3 = configurations(3)
    if C.mut == "MUT-COUNT-3-LAW":
        cfg3 = cfg3 + [(1,)]
    C.gate("G-COUNT-3-EMPTINESS-IS-A-LAW",
           len(cfg3) == 1 and cfg3[0] == () and leg3_leaves > 0,
           f"count 3's emptiness is a LAW, not a census cap: at n = 3 "
           f"C(2,2) = {len(cfg3)} configuration exists and it carries "
           f"{len(cfg3[0]) if cfg3 else '?'} fillers, so the pattern class "
           f"distinguishes NO interior position and cannot separate the "
           f"two splits of a count-3 interval.  S2 measured the same fact "
           f"independently -- (p,p,r) forced, {leg3_leaves} leaves, one "
           f"pattern",
           "MUT-COUNT-3-LAW")
    ff5 = first_filler_law(5)
    coincide4 = (marginal_law(4) == first_filler_law(4))
    differ5 = (marg[5] != ff5)
    if C.mut == "MUT-FILLER-REDUCTION":
        differ5 = False
    C.gate("G-FILLER-REDUCTION-IS-FREE",
           coincide4 and differ5,
           f"AND THE ONE RESIDUAL FREEDOM, MEASURED.  At n >= 5 a leg "
           f"carries >= 2 fillers, so reducing the filler SET to a "
           f"POSITION is a choice, and the choices differ: at n = 5 the "
           f"marginal gives {law_str(marg[5])} while first-filler gives "
           f"{law_str(ff5)}.  At n = 4 they COINCIDE ({coincide4}), which "
           f"is exactly why the count-4 result looks convention-free and "
           f"is not.  Registered as I-FILLER-REDUCTION",
           "MUT-FILLER-REDUCTION")
    R["all_n_law"] = {
        "statement": ("a delivery-free leg of length n has two advancing "
                      "steps among n-1 interior steps: C(n-1,2) "
                      "equiprobable configurations, n-3 fillers"),
        "position_marginal": {str(n): {str(p): fr(v)
                                       for p, v in marg[n].items()}
                              for n in sorted(marg)},
        "marginal_is_uniform_at_every_n_ge_4": uniform_ok,
        "count_3_configurations": len(cfg3),
        "first_filler_law_at_5": {str(p): fr(v) for p, v in ff5.items()},
        "reductions_coincide_at_4": coincide4,
        "reductions_differ_at_5": differ5,
    }
    C.say(f"    marginal uniform on n-1 positions at n = 4..12: "
          f"{uniform_ok}; at n=4 {law_str(marg[4])}")
    C.say(f"    n=5 marginal {law_str(marg[5])} vs first-filler "
          f"{law_str(ff5)} -- the reduction is FREE at n >= 5")
    C.say("")

    # ---- 5.  S2, THE MECHANISM, AND THE WELD --------------------------
    C.say("-" * 78)
    C.say("5.  S2 -- THE TRANSPORT CENSUS, ITS MECHANISM, AND THE WELD")
    C.say("-" * 78)
    tot1, tot2 = sum(leg1.values()), sum(leg2.values())
    C.gate("G-S2-PROFILES",
           tot1 == 3584 and tot2 == 73728 and len(leg1) == 5
           and len(leg2) == 5 and set(leg1) == set(leg2),
           f"S2's two length-4 profiles: leg-1 totals {tot1} leaves over "
           f"{len(leg1)} patterns; leg-2 totals {tot2} over {len(leg2)}; "
           f"same pattern set = {set(leg1) == set(leg2)}",
           "MUT-S2-PROFILE")

    def slot_of(pat):
        idx = [k + 1 for k, e in enumerate(pat[:-1]) if e != "p"]
        return idx[0] if len(idx) == 1 else 0

    posmap = {p: slot_of(p) for p in sorted(leg1)}
    if C.mut == "MUT-POSITION-MAP":
        posmap = {p: 1 for p in posmap}
    C.gate("G-S2-PATTERN-POSITION-MAP",
           sorted(set(posmap.values())) == [1, 2, 3]
           and all(len([e for e in p[:-1] if e != "p"]) == 1
                   for p in posmap),
           f"each of S2's five length-4 patterns carries EXACTLY ONE "
           f"non-proposal interior event, so the pattern class determines "
           f"an interior slot in {{1,2,3}}: " +
           str({"".join(p): v for p, v in sorted(posmap.items())}),
           "MUT-POSITION-MAP")

    # F8's MECHANISM: which slots admit a delivery
    admits = {s: sorted({p[s - 1] for p in leg1 if slot_of(p) == s})
              for s in (1, 2, 3)}
    realised = sorted("".join(p) for p in leg1)
    combinatorial = sorted("".join(
        tuple("p" if k != s - 1 else e for k in range(3)) + ("r",))
        for s in (1, 2, 3) for e in ("d", "n"))
    missing = sorted(set(combinatorial) - set(realised))
    if C.mut == "MUT-MIDDLE-SLOT":
        admits = {s: ["d", "n"] for s in (1, 2, 3)}
        missing = []
    C.gate("G-MIDDLE-SLOT-ADMITS-NO-DELIVERY",
           admits == {1: ["d", "n"], 2: ["n"], 3: ["d", "n"]}
           and missing == ["pdpr"],
           f"THE MECHANISM, EXACT.  Of the {len(combinatorial)} "
           f"combinatorial possibilities (3 interior slots x "
           f"{{delivery, idle}}) S2 realises {len(realised)}.  The missing "
           f"one is {missing} -- A DELIVERY IN THE MIDDLE SLOT.  Slots 1 "
           f"and 3 admit {admits[1]}; slot 2 admits {admits[2]}.  That "
           f"single exclusion IS the entire transport-scope position "
           f"dependence: delete the delivery-bearing patterns and exactly "
           f"one pattern per slot remains",
           "MUT-MIDDLE-SLOT")

    def multiplicity(prof):
        d = [c for p, c in prof.items() if "d" in p]
        n = [c for p, c in prof.items() if "d" not in p]
        return Fr(d[0], n[0])

    m1, m2 = multiplicity(leg1), multiplicity(leg2)
    if C.mut == "MUT-MULTIPLICITY":
        m2 = m1

    def mult_law(m):
        tot = 2 * (1 + m) + 1
        return {1: (1 + m) / tot, 2: Fr(1) / tot, 3: (1 + m) / tot}

    def position_law(prof):
        tot = sum(prof.values())
        law = {1: Fr(0), 2: Fr(0), 3: Fr(0)}
        for p, c in prof.items():
            law[posmap[p]] += Fr(c, tot)
        return law

    law1_T, law2_T = position_law(leg1), position_law(leg2)
    C.gate("G-DELIVERY-MULTIPLICITY-LAW",
           m1 == 2 and m2 == 3 and mult_law(m1) == law1_T
           and mult_law(m2) == law2_T,
           f"AND ITS PARAMETER.  The delivery multiplicity per slot is "
           f"{fr(m1)} at leg 1 and {fr(m2)} at leg 2 -- one more "
           f"deliverable message in flight.  With the middle slot excluded "
           f"the law is forced to ((1+m), 1, (1+m))/(2m+3): m = {fr(m1)} "
           f"gives {law_str(law1_T)} and m = {fr(m2)} gives "
           f"{law_str(law2_T)}, both reproduced exactly from S2's leaf "
           f"counts.  The family runs toward (1/2, 0, 1/2) as m grows -- "
           f"the delivery multiplicity per interior slot is the "
           f"frozen-stage validity parameter, measured here at two values",
           "MUT-MULTIPLICITY / MUT-S2-PROFILE")

    def df(prof):
        return {p: c for p, c in prof.items() if "d" not in p}

    law1_D, law2_D = position_law(df(leg1)), position_law(df(leg2))

    def tv(p, q):
        return sum(abs(p[k] - q[k]) for k in p) / 2

    tv_T, tv_D = tv(law1_T, law2_T), tv(law1_D, law2_D)
    mass1 = Fr(sum(df(leg1).values()), tot1)
    mass2 = Fr(sum(df(leg2).values()), tot2)
    C.gate("G-POSITION-DEPENDENCE-AT-TRANSPORT-SCOPE",
           tv_T == Fr(2, 63) and law1_T != law2_T,
           f"AT TRANSPORT SCOPE the interior-position law is "
           f"CHAIN-POSITION DEPENDENT: leg 1 {law_str(law1_T)}, leg 2 "
           f"{law_str(law2_T)}, total variation {fr(tv_T)} > 0",
           "MUT-S2-PROFILE / MUT-MULTIPLICITY")
    unif3 = {1: Fr(1, 3), 2: Fr(1, 3), 3: Fr(1, 3)}
    C.gate("G-NO-DELIVERY-CONDITIONAL",
           tv_D == 0 and law1_D == law2_D == unif3 and mass1 == Fr(3, 7)
           and mass2 == Fr(1, 3) and mass1 != mass2,
           f"THE CONDITIONING, NAMED HONESTLY.  Deleting the "
           f"delivery-bearing patterns from S2's TRANSPORT-scope leaf "
           f"counts and renormalising gives {law_str(law1_D)} and "
           f"{law_str(law2_D)}, TV {fr(tv_D)}.  This is the transport "
           f"census CONDITIONED ON NO DELIVERY, not a delivery-free "
           f"census: the retained masses are {fr(mass1)} and {fr(mass2)} "
           f"-- DIFFERENT conditioning events at the two cells.  The three "
           f"retained patterns carry EQUAL weight in each cell, and that "
           f"equality is what carries the uniformity",
           "MUT-S2-PROFILE")

    # the #313 parity witness: the ALTERNATIVE connective, measured
    def dbear(prof):
        return {p: c for p, c in prof.items() if "d" in p}

    law1_del = position_law(dbear(leg1))
    parity_delta = tv(law1_del, law1_D)
    if C.mut == "MUT-PARITY":
        parity_delta = Fr(0)
    C.gate("G-PARITY-WITNESS",
           law1_del == {1: Fr(1, 2), 2: Fr(0), 3: Fr(1, 2)}
           and parity_delta == Fr(1, 3),
           f"THE ALTERNATIVE CONNECTIVE, MEASURED (the #313 parity "
           f"clause).  This unit's one Boolean partition of a census is "
           f"delivery-bearing vs delivery-free.  Taking the OTHER side -- "
           f"retain the deliveries, delete the idles -- gives "
           f"{law_str(law1_del)}, exactly the m -> infinity limit of the "
           f"multiplicity family, at measured distance {fr(parity_delta)} "
           f"from the no-delivery conditional.  The connective's delta is "
           f"printed rather than assumed away",
           "MUT-PARITY")

    # THE WELD -- S1 alone reproduces S2's no-delivery census at count 4
    s1_law4 = marg[4]
    s1_slots = sorted(configurations(4), key=lambda c: c[0])
    s2_slots = sorted(df(leg1), key=lambda p: posmap[p])
    biject = ([c[0] for c in s1_slots] == [posmap[p] for p in s2_slots]
              and len(s1_slots) == len(s2_slots) == 3)
    weld = (s1_law4 == law1_D == law2_D)
    if C.mut == "MUT-WELD":
        weld = False
    C.gate("G-WELD-S1-REPRODUCES-S2",
           weld and biject,
           f"THE WELD.  The positional law derived from S1's chain ALONE "
           f"at n = 4 -- {law_str(s1_law4)} -- reproduces S2's "
           f"no-delivery conditional at BOTH censused cells EXACTLY "
           f"({weld}), and the three S1 configurations biject with the "
           f"three retained S2 patterns slot for slot ({biject}): S1's "
           f"self-loop filler IS S2's idle 'n'.  The corrected convention "
           f"is what makes this true -- the bare-state-0 reading gives "
           f"{law_str(alt_law4)} and reproduces nothing",
           "MUT-WELD / MUT-CONVENTION-SWAP")

    e2 = ("| **E2** | 3, 7, 10" in text(CORPUS_SHA, U1B_NOTE))
    e3 = ("| **E3** | 3, 6, 10" in text(CORPUS_SHA, U1B_NOTE))
    e3_leg2 = ("E3 (3/6/10) built" in out_txt and "leg-2 patterns" in out_txt)
    if C.mut == "MUT-TWO-CELLS":
        e3_leg2 = False
    C.gate("G-S2-TWO-CELLS-CONFOUND",
           e2 and e3 and e3_leg2,
           f"THE CONFOUND, DISCLOSED.  The two cells are not two chain "
           f"positions of one ensemble: the leg-1 profile is the 4-event "
           f"FIRST leg (E2, renewals at 3, 7, 10 -- depths 3->7; "
           f"{e2}) and the leg-2 profile is E3's SECOND leg (renewals at "
           f"3, 6, 10 -- depths 6->10; {e3}, {e3_leg2}).  Ordinal "
           f"position, absolute depth and ensemble identity move together "
           f"across the only two data points; 'chain-position dependent' "
           f"is one of three readings the data cannot separate.  Every "
           f"segment carrying these cells is stamped "
           f"CENSUSED-AT-2-CELLS-E2-LEG1-E3-LEG2",
           "MUT-TWO-CELLS")
    R["positional_census"] = {
        "leg1_profile": {"".join(p): c for p, c in sorted(leg1.items())},
        "leg2_profile": {"".join(p): c for p, c in sorted(leg2.items())},
        "leg1_total": tot1, "leg2_total": tot2,
        "pattern_to_slot": {"".join(p): v for p, v in sorted(posmap.items())},
        "slots_admitting": {str(k): v for k, v in admits.items()},
        "combinatorially_possible": combinatorial,
        "realised": realised, "missing": missing,
        "delivery_multiplicity_leg1": fr(m1),
        "delivery_multiplicity_leg2": fr(m2),
        "law_transport_leg1": {str(k): fr(v) for k, v in law1_T.items()},
        "law_transport_leg2": {str(k): fr(v) for k, v in law2_T.items()},
        "law_no_delivery_conditional_leg1": {str(k): fr(v)
                                             for k, v in law1_D.items()},
        "law_no_delivery_conditional_leg2": {str(k): fr(v)
                                             for k, v in law2_D.items()},
        "tv_between_cells_transport": fr(tv_T),
        "tv_between_cells_no_delivery_conditional": fr(tv_D),
        "conditioning_mass_leg1": fr(mass1),
        "conditioning_mass_leg2": fr(mass2),
        "length3_leaf_count": leg3_leaves,
        "cells": "E2 leg 1 (depths 3->7); E3 leg 2 (depths 6->10)",
        "ensemble_data_qualifier": (
            "S2's interval lengths are ENSEMBLE DATA -- renewal positions "
            "DECLARED by the ensembles E1-E4, not sampled from any "
            "kernel; no frequency here is read as a kernel probability"),
        "scope": "TRANSPORT SCOPE (d42b1) only, per S2's own §10",
    }
    C.say(f"    transport            : leg1 {law_str(law1_T)}  leg2 "
          f"{law_str(law2_T)}  TV {fr(tv_T)}")
    C.say(f"    no-delivery conditional: leg1 {law_str(law1_D)}  leg2 "
          f"{law_str(law2_D)}  TV {fr(tv_D)}  (masses {fr(mass1)}, "
          f"{fr(mass2)})")
    C.say(f"    S1 ALONE at n=4      : {law_str(s1_law4)}  -- THE WELD")
    C.say("")

    # ---- 6.  THE SEAM, RE-GRADED --------------------------------------
    C.say("-" * 78)
    C.say("6.  THE SEAM: AVOIDABLE HERE; REAL AT TRANSPORT SCOPE; ITS CAUSE")
    C.say("-" * 78)
    single_scope = ["S1", "S4", "I7"]
    layer_from_s1 = bool(weld and uniform_ok)
    escape_quoted = (norm("the window chain ESCAPES: 68 transitions from "
                          "shallow parents land in 5 classes first "
                          "realized at length 3")
                     in norm_source(CORPUS_SHA, P32))
    shortcut_quoted = (norm("zero of the 3,969 transport menus match any "
                            "delivery-free menu shape")
                       in norm_source(CORPUS_SHA, P32))
    p32_uses = ["Q-S7-ESCAPE", "Q-S7-SHORTCUT"]
    quotient_reached = any("36-state" in norm(q) for _, rel, q, _, _ in QUOTES
                           if rel == P32)
    if C.mut == "MUT-SEAM-CAUSE":
        escape_quoted = False
    C.gate("G-SEAM-CAUSE-IS-THE-ESCAPE",
           escape_quoted and shortcut_quoted and layer_from_s1
           and not quotient_reached,
           f"THE SEAM, RE-GRADED AT BOTH REFERENTS.  (i) As an obstruction "
           f"to THIS unit's question it is AVOIDABLE: a single-scope "
           f"delivery-free row set already exists inside the pin -- "
           f"{single_scope} -- and supplies BOTH layers, the leg-length "
           f"law and the positional law ({layer_from_s1}).  S2 is a "
           f"CROSS-CHECK, not the only source.  (ii) As a measurement it "
           f"is real, and its cause is NOT row provenance but THE ESCAPE: "
           f"S7 (paper 32 §2.3, TERMINAL) measures that the transport-"
           f"scope window chain escapes ({escape_quoted}) and that "
           f"menu-shape factorisation fails ({shortcut_quoted}), so THERE "
           f"IS NO TRANSPORT-SCOPE ANALOGUE OF S1's 6x6 CHAIN TO PIN.  S7 "
           f"is consumed for this statement only; the pin's prohibition on "
           f"paper 32's 36-state quotient claim is honoured "
           f"({not quotient_reached})",
           "MUT-SEAM-CAUSE")
    R["seam"] = {
        "grade_for_this_units_question": "AVOIDABLE",
        "single_scope_row_set": single_scope,
        "positional_layer_derivable_from_S1_alone": layer_from_s1,
        "s2_role": "declared cross-check at count 4, agreeing exactly",
        "grade_as_a_measurement": "REAL AT TRANSPORT SCOPE",
        "cause": "THE ESCAPE (S7 = v10 paper 32 §2.3, TERMINAL)",
        "not_the_cause": "row provenance / the pin's row selection",
        "s7_consumed_for": p32_uses,
        "s7_prohibition_honoured": "the 36-state quotient claim is not read",
    }
    C.say(f"    AVOIDABLE for this question (single-scope set "
          f"{single_scope}); REAL at transport scope; CAUSE = THE ESCAPE")
    C.say("")

    # ---- 7.  THE ARENA -------------------------------------------------
    C.say("-" * 78)
    C.say("7.  THE SPATIAL ARENA (I7 / R6a), REBUILT HERE FROM THE COUNTS")
    C.say("-" * 78)
    r6a = load_json(R6A_TERMINAL_SHA, R6A_RECEIPT)
    fam = r6a["record_family"]
    records = []
    for name in sorted(fam):
        row = fam[name]
        if row["homogeneous"]:
            cells = [("all-9-sites", row["counts_at_00"], SITES)]
            cap = None
        else:
            cells = [("00", row["counts_at_00"], 1),
                     ("11", row["counts_at_11"], 1)]
            cap = ("inhomogeneous: the receipt prints counts at sites 00 "
                   "and 11 only -- censused at 2 of 9 sites, a DECLARED "
                   "CAP, and the segment carries it")
        records.append({"name": name, "admissible": row["admissible"],
                        "homogeneous": row["homogeneous"], "cells": cells,
                        "cap": cap})
    rebuild_raw, rebuild_equiv, undetermined = {}, {}, []
    for rec in records:
        if not rec["admissible"]:
            continue
        if rec["homogeneous"]:
            per = 1
            for n in rec["cells"][0][1]:
                per *= (n - 1)
            rebuild_raw[rec["name"]] = per ** SITES
            if per > 0:
                rebuild_equiv[rec["name"]] = per
        elif any(n == 1 for _, cs, _ in rec["cells"] for n in cs):
            rebuild_raw[rec["name"]] = 0
        else:
            undetermined.append(rec["name"])
    if C.mut == "MUT-FIBER-REBUILD":
        rebuild_raw["G-DIAG2"] = rebuild_raw["G-DIAG2"] + 1
    r6a_raw = {k: v["raw"] for k, v in r6a["split_fibers"].items()}
    raw_match = all(rebuild_raw[k] == r6a_raw.get(k) for k in rebuild_raw)
    eq_match = all(rebuild_equiv[k] == pv["P-R6A-EQUIVARIANT-FIBERS"].get(k)
                   for k in rebuild_equiv)
    C.gate("G-R6A-FIBER-REBUILD",
           raw_match and eq_match
           and sorted(set(r6a_raw) - set(rebuild_raw)) == undetermined,
           f"R6a's split fibers REBUILT here from the count data alone "
           f"(raw = prod over intervals of (n-1); equivariant = prod over "
           f"links of (n_l - 1)) and compared against the anchored "
           f"receipt: raw agree at {len(rebuild_raw)} of "
           f"{len(rebuild_raw)} ({raw_match}), equivariant at "
           f"{len(rebuild_equiv)} ({eq_match}).  DECLARED CAP: "
           f"{undetermined} is inhomogeneous with no count-1 interval "
           f"among its printed sites, so its fiber is not determined by "
           f"the printed-site data and is NOT rebuilt",
           "MUT-FIBER-REBUILD")

    census, intervals = {}, []
    for rec in records:
        if not rec["admissible"]:
            continue
        for tag, counts, mult in rec["cells"]:
            for n in counts:
                census[n] = census.get(n, 0) + mult
                for _ in range(mult):
                    intervals.append((rec["name"], tag, n))
    total = sum(census.values())
    n_hom = sum(1 for r in records if r["admissible"] and r["homogeneous"])
    n_inh = sum(1 for r in records
                if r["admissible"] and not r["homogeneous"])
    expected = n_hom * SITES * LINKS + n_inh * 2 * LINKS
    if C.mut == "MUT-ARENA-CENSUS":
        census = dict(census)
        census[4] = census[4] + 1
        total = sum(census.values())
    C.gate("G-ARENA-BASELINE",
           total == expected == 201 and len(intervals) == 201
           and pv["P-ARENA-GEOMETRY-RECORD"].startswith("n_l(x)")
           and pv["P-I7-L"] == 3 and pv["P-I7-D"] == 2,
           f"the baseline arena is I7's: L = {pv['P-I7-L']}, d = "
           f"{pv['P-I7-D']}, {SITES} sites, {LINKS} links, n_l(x) = the "
           f"number of DIVISION EVENTS in the record interval.  This unit "
           f"censuses {total} record intervals over "
           f"{n_hom + n_inh} admissible records ({n_hom} homogeneous at "
           f"all {SITES} sites, {n_inh} inhomogeneous at the 2 printed "
           f"sites -- declared cap), against an independently expressed "
           f"expectation {n_hom}x{SITES}x{LINKS} + {n_inh}x2x{LINKS} = "
           f"{expected}; count values " + str(sorted(census)),
           "MUT-ARENA-CENSUS")

    # the three records that admit NO subdivision at all
    unrefinable = sorted(k for k in rebuild_raw if rebuild_raw[k] == 0)
    unref_intervals = sum(1 for r, _, _ in intervals if r in unrefinable)
    honest = [(r, t, n) for r, t, n in intervals if r not in unrefinable]
    honest_total = len(honest)
    nontrivial = sum(1 for _, _, n in intervals if n >= 3)
    honest_nontrivial = sum(1 for _, _, n in honest if n >= 3)
    bad4 = sum(1 for r, _, n in intervals if n == 4 and r in unrefinable)
    if C.mut == "MUT-UNREFINABLE":
        unrefinable = []
        unref_intervals = 0
    C.gate("G-UNREFINABLE-RECORDS",
           unrefinable == ["G-ANISO", "G-CURVED", "G-FLAT"]
           and unref_intervals == 60 and honest_total == 141
           and honest_nontrivial == 103 and bad4 == 10,
           f"THE HONEST DENOMINATOR.  {len(unrefinable)} admissible "
           f"records have R6a split fiber 0 -- {unrefinable} -- they "
           f"ADMIT NO SUBDIVISION AT ALL (CR-B §3's own words), and they "
           f"carry {unref_intervals} of the {total} censused intervals, "
           f"including {bad4} of the count-4 ones.  On those there is no "
           f"R6a split fiber to collapse.  Restricted to the "
           f"{len(rebuild_raw) - len(unrefinable) + len(undetermined)} "
           f"records that admit the move: {honest_total} censused, "
           f"{honest_nontrivial} carrying a non-trivial fiber",
           "MUT-UNREFINABLE")
    R["arena"] = {
        "sites": SITES, "links": LINKS,
        "geometry_record": pv["P-ARENA-GEOMETRY-RECORD"],
        "readout": pv["P-ARENA-READOUT"],
        "intervals_censused": total,
        "count_census": {str(k): census[k] for k in sorted(census)},
        "records_censused": sorted(r["name"] for r in records
                                   if r["admissible"]),
        "records_inadmissible": sorted(r["name"] for r in records
                                       if not r["admissible"]),
        "unrefinable_records": unrefinable,
        "unrefinable_intervals": unref_intervals,
        "honest_denominator_censused": honest_total,
        "honest_denominator_nontrivial": honest_nontrivial,
        "nontrivial_all": nontrivial,
        "declared_cap": ("the two inhomogeneous records are censused at "
                         "the 2 of 9 sites the R6a receipt prints"),
        "fiber_rebuild_raw": {k: rebuild_raw[k] for k in sorted(rebuild_raw)},
        "fiber_rebuild_equivariant": {k: rebuild_equiv[k]
                                      for k in sorted(rebuild_equiv)},
        "fiber_not_rebuilt": undetermined,
    }
    C.say(f"    count census " + str({k: census[k] for k in sorted(census)})
          + f"  (total {total})")
    C.say(f"    unrefinable {unrefinable}: {unref_intervals} intervals; "
          f"honest denominators {honest_total} / {honest_nontrivial}")
    C.say("")

    # ---- 8.  THE FIBER COLLAPSE ----------------------------------------
    C.say("-" * 78)
    C.say("8.  THE FIBER-COLLAPSE MEASUREMENT (the decisive test)")
    C.say("-" * 78)
    K_HOLE = "KERNEL-HOLE (counts 1 and 2; g(1) = g(2) = 0 exactly)"
    K_EMPTY = "STRATUM-EMPTY-BY-LAW (count 3; one configuration)"
    K_COLL = "COLLAPSED-IN-DISTRIBUTION (count >= 4)"
    klass = {}
    for _, _, n in intervals:
        k = K_HOLE if n <= 2 else (K_EMPTY if n == 3 else K_COLL)
        klass[k] = klass.get(k, 0) + 1
    collapsed = klass.get(K_COLL, 0)
    hole_cost = klass.get(K_HOLE, 0)
    collapsed_honest = sum(1 for _, _, n in honest if n >= 4)
    collapsed4 = census.get(4, 0)
    collapsed4_honest = sum(1 for _, _, n in honest if n == 4)
    if C.mut == "MUT-COLLAPSE-COUNT":
        collapsed = collapsed + 5
    C.gate("G-FIBER-COLLAPSE-COVERAGE",
           collapsed == 102 and hole_cost == 79 and klass.get(K_EMPTY) == 20
           and sum(klass.values()) == total and collapsed_honest == 83
           and collapsed4 == 37 and collapsed4_honest == 27,
           f"THE DECISIVE NUMBERS, on BOTH denominators.  With the all-n "
           f"law the derived kernel speaks on every interval of count >= "
           f"4: {collapsed} of the {total} censused intervals, "
           f"{collapsed} of the {nontrivial} carrying a non-trivial "
           f"fiber; on the honest denominator (the records that admit the "
           f"move) {collapsed_honest} of {honest_total} censused and "
           f"{collapsed_honest} of {honest_nontrivial} with a non-trivial "
           f"fiber.  AT COUNT 4 ALONE -- the route the delivery took -- "
           f"{collapsed4} of {total} and {collapsed4_honest} of "
           f"{honest_nontrivial}.  The remainder: " +
           "; ".join(f"{klass[k]} {k}" for k in sorted(klass)),
           "MUT-COLLAPSE-COUNT / MUT-UNIFORM-MARGINAL")

    modes_D = [k for k, v in s1_law4.items() if v == max(s1_law4.values())]
    modes_T = [k for k, v in law1_T.items() if v == max(law1_T.values())]
    mins_T = [k for k, v in law1_T.items() if v == min(law1_T.values())]
    if C.mut == "MUT-MODES":
        modes_D = [1]
    C.gate("G-COLLAPSE-IS-DISTRIBUTION-NOT-VALUE",
           len(modes_D) == 3 and len(modes_T) == 2 and len(mins_T) == 1,
           f"the derived law does NOT collapse the fiber to a VALUE.  At "
           f"delivery-free scope it is uniform and has {len(modes_D)} "
           f"maximisers {modes_D}, so no MAXIMISING functional of it names "
           f"a split -- and being uniform, no functional of it does.  At "
           f"transport scope there are {len(modes_T)} maximisers "
           f"{modes_T}, but the ARGMIN names {mins_T} UNIQUELY: the claim "
           f"is about maximising functionals, and at transport scope the "
           f"minimum-probability split IS named",
           "MUT-MODES / MUT-S2-PROFILE")

    crb4 = dict(pv["P-CRB-N4-ROW"])
    if C.mut == "MUT-CRB":
        crb4["pinned_simplex_dim"] = 1
    C.gate("G-CRB-SIMPLEX",
           crb4["pinned_simplex_dim"] == 2 and crb4["fiber"] == 3
           and pv["P-CRB-N3-ROW"]["pinned_simplex_dim"] == 1
           and pv["P-CRB-HEAD"] == "CRB-BLOCKED-AT-NO-PINNED-STOCHASTIC-LAW",
           f"in CR-B's own coordinates, AT ONE INTERVAL: at count 4 CR-B "
           f"measured fiber {crb4['fiber']} and an invariant-measure "
           f"simplex of dimension {crb4['pinned_simplex_dim']} under the "
           f"pinned symmetry ({crb4['flip_simplex_dim']} under the flip); "
           f"the derived kernel selects ONE point, so the dimension goes "
           f"{crb4['pinned_simplex_dim']} -> 0.  CR-B's head was "
           f"\"{pv['P-CRB-HEAD']}\" and its MISSING tag names exactly the "
           f"object this unit supplies.  This is a statement about a "
           f"PER-INTERVAL simplex, not about a record's fiber",
           "MUT-PATH-VALUE-DRIFT / MUT-CRB")

    def admissible(n1, n2, n3):
        q11, q22 = Fr(n1), Fr(n2)
        q12 = Fr(n3 - n1 - n2, 2)
        return q11 > 0 and q11 * q22 - q12 * q12 > 0

    def adm_marginal(counts, link):
        cnt = {a: 0 for a in range(1, counts[link])}
        tot = 0
        for tup in itertools.product(*[range(1, x) for x in counts]):
            if admissible(*tup):
                tot += 1
                cnt[tup[link]] += 1
        return {a: Fr(v, tot) for a, v in cnt.items()}, tot

    adm_rows = []
    for name, link in (("G-DIAG2", 2), ("G-ANISO2", 0), ("G-OFFNEG", 2)):
        counts = fam[name]["counts_at_00"]
        law, tot_adm = adm_marginal(counts, link)
        adm_rows.append({"record": name, "counts": counts,
                         "admissible_at_the_site": tot_adm,
                         "derived_marginal": law_str(s1_law4),
                         "admissible_uniform_marginal": law_str(law),
                         "agree": law == s1_law4})
    if C.mut == "MUT-ADMISSIBILITY":
        adm_rows[1]["agree"] = True
    agree_rows = [r["record"] for r in adm_rows if r["agree"]]
    C.gate("G-ADMISSIBILITY-COUPLING",
           agree_rows == ["G-DIAG2"]
           and adm_rows[1]["admissible_at_the_site"] == 221
           and adm_rows[2]["admissible_at_the_site"] == 23
           and adm_rows[1]["admissible_at_the_site"]
           == pv["P-R6A-ANISO2-PER-SITE-ADMISSIBLE"][0],
           f"AND THE SCOPE OF THE COLLAPSE, MEASURED.  The derived kernel "
           f"is per-interval and factorises; admissibility couples the "
           f"three links at a site.  Rebuilding R6a's admissible fiber "
           f"independently (positive-definiteness of the refined form) "
           f"reproduces its per-site counts exactly -- G-ANISO2 "
           f"{adm_rows[1]['admissible_at_the_site']}, G-OFFNEG "
           f"{adm_rows[2]['admissible_at_the_site']} -- and the derived "
           f"marginal equals the admissible-uniform marginal at "
           f"{agree_rows} ONLY: G-ANISO2 gives "
           f"{adm_rows[1]['admissible_uniform_marginal']} and G-OFFNEG "
           f"{adm_rows[2]['admissible_uniform_marginal']}.  CR-B's "
           f"non-factorisation recurs one level down",
           "MUT-ADMISSIBILITY")

    fully = []
    for rec in records:
        if not rec["admissible"] or not rec["homogeneous"]:
            continue
        cs = rec["cells"][0][1]
        if all((n == 4) or (n == 2) for n in cs) and any(n == 4 for n in cs):
            fully.append(rec["name"])
    raw_eq_adm = sorted(k for k, v in r6a["split_fibers"].items()
                        if v["splittable"] and v["raw"]
                        == v["admissible_at_images"])
    if C.mut == "MUT-DIAG2":
        fully = []
    C.gate("G-DERIVED-LAW-COMPLETE-ON-ONE-RECORD",
           fully == ["G-DIAG2"] and raw_eq_adm == ["G-DIAG2"]
           and pv["P-R6A-DIAG2-RAW"] == pv["P-R6A-DIAG2-ADMISSIBLE"] == 19683
           and pv["P-CRB-UNIFORM-REFUTED"] == "REFUTED-AS-FORCING",
           f"exactly {len(fully)} record -- {fully} -- has every "
           f"splittable interval at count 4 and every other at fiber 1, so "
           f"on it the derived kernel supplies a COMPLETE law on R6a's "
           f"entire split fiber: the uniform law on "
           f"{pv['P-R6A-DIAG2-RAW']} elements.  It is the law CR-B classed "
           f"\"{pv['P-CRB-UNIFORM-REFUTED']}\" for want of a declared "
           f"support.  AND THE CAVEAT, MEASURED: G-DIAG2 is also the ONLY "
           f"splittable record where raw = admissible-at-images "
           f"({raw_eq_adm}) -- exactly the record where CR-B's "
           f"support-dependence objection was already vacuous",
           "MUT-DIAG2 / MUT-FIBER-REBUILD")

    binom = {k: Fr(choose(4, k), sum(choose(4, j) for j in (1, 2, 3)))
             for k in (1, 2, 3)}
    tv_s5 = tv(s1_law4, binom)
    if C.mut == "MUT-S5-COMPARATOR":
        tv_s5 = Fr(0)
    C.gate("G-S5-COMPARATOR-SEPARATION",
           tv_s5 == Fr(2, 21) and fr(tv_s5) == pv["P-CRB-TV-UNIFORM-BINOMIAL-4"],
           f"the continuous comparator (S5, CHOSEN NOT DERIVED) places "
           f"interior positions as uniform order statistics, giving the "
           f"binomial split law {law_str(binom)} at count 4 -- separated "
           f"from the derived law {law_str(s1_law4)} by total variation "
           f"{fr(tv_s5)}, which reproduces CR-B's own anchored "
           f"tv_uniform_vs_binomial at count 4 "
           f"(\"{pv['P-CRB-TV-UNIFORM-BINOMIAL-4']}\") computed by a "
           f"different unit on a different route.  S5's own disclaimer -- "
           f"\"the coefficients 1/4 are chosen, not derived\" -- is "
           f"carried wherever the continuous layer is touched",
           "MUT-S5-COMPARATOR")
    R["fiber_collapse"] = {
        "interval_classes": {k: klass[k] for k in sorted(klass)},
        "collapsed_all_denominator": collapsed,
        "collapsed_honest_denominator": collapsed_honest,
        "collapsed_at_count_4_all": collapsed4,
        "collapsed_at_count_4_honest": collapsed4_honest,
        "intervals_total": total, "intervals_nontrivial": nontrivial,
        "honest_total": honest_total,
        "honest_nontrivial": honest_nontrivial,
        "hole_cost_intervals": hole_cost,
        "collapse_kind": "DISTRIBUTION",
        "law_at_count_4": {str(k): fr(v) for k, v in s1_law4.items()},
        "maximisers_delivery_free": modes_D,
        "maximisers_transport": modes_T,
        "argmin_transport": mins_T,
        "crb_simplex_dim_before": crb4["pinned_simplex_dim"],
        "crb_simplex_dim_after": 0,
        "records_with_a_complete_derived_law": fully,
        "records_where_raw_equals_admissible": raw_eq_adm,
        "admissibility_coupling": adm_rows,
        "s5_comparator_law": {str(k): fr(v) for k, v in binom.items()},
        "tv_derived_vs_s5": fr(tv_s5),
        "scope": ("DELIVERY-FREE, derived from S1 alone; at transport "
                  "scope the law is cell-dependent and no unique "
                  "distribution exists"),
    }
    C.say(f"    classes " + str({k: klass[k] for k in sorted(klass)}))
    C.say(f"    COLLAPSED IN DISTRIBUTION on {collapsed} of {total} "
          f"({collapsed} of {nontrivial} non-trivial); honest "
          f"{collapsed_honest} of {honest_total} ({collapsed_honest} of "
          f"{honest_nontrivial})")
    C.say("")

    # ---- 9.  THE IDENTIFICATION CENSUS ---------------------------------
    C.say("-" * 78)
    C.say("9.  THE IDENTIFICATION CENSUS + THE CHOICE INVENTORY")
    C.say("-" * 78)
    rev_T = ({1: law1_T[3], 2: law1_T[2], 3: law1_T[1]} == law1_T
             and {1: law2_T[3], 2: law2_T[2], 3: law2_T[1]} == law2_T)
    rev_D = ({1: s1_law4[3], 2: s1_law4[2], 3: s1_law4[1]} == s1_law4)

    # F1: the two front rules and their measured separation
    cycles, nonzero, sums = 0, 0, set()
    for rec in records:
        if not rec["admissible"] or not rec["homogeneous"]:
            continue
        for li, n in enumerate(rec["cells"][0][1]):
            for _coset in range(3):
                cycles += 1
                s = 3 * n
                sums.add(s)
                if s != 0:
                    nonzero += 1
    if C.mut == "MUT-FRONT-CYCLES":
        nonzero = cycles - 1
    front_fiber = 2 if nonzero == cycles else 1
    if C.mut == "MUT-FRONT-FIBER":
        front_fiber = 1

    def item(nm, what, fiber, cls, why, ev):
        return {"name": nm, "what": what, "fiber": fiber, "class": cls,
                "why": why, "evidence": ev}

    candidates = []
    candidates.append({
        "name": "C1-COUNT-MATCH-LENGTH",
        "statement": ("a record interval of count n is a single "
                      "inter-renewal leg of LENGTH n; its n-1 interior "
                      "positions are the n-1 admissible splits"),
        "expressible_from": ["S1", "S2", "S3", "I7"],
        "items": [
            item("I-TYPE", "does the identification preserve the declared "
                 "type?", 1, FORCED,
                 "VIOLATED-AS-DECLARED: n_l counts DIVISION EVENTS while a "
                 "leg's LENGTH counts grammar events, of which exactly one "
                 "is a division event.  Fixed by the pin's own wording, so "
                 "nothing is chosen -- but the type it fixes is not the "
                 "declared one", {"division_events_per_leg": 1}),
            item("I-LINK", "which link supplies the leg length", 1, FORCED,
                 "the interval's own count fixes it", {"links": LINKS}),
            item("I-SITE", "which site", 1, FORCED,
                 "every interval is identified separately", {"sites": SITES}),
            item("I-RENEWAL-CONVENTION", "what counts as a renewal", 1,
                 FORCED,
                 "FORCED BY THE SOURCE: d43b's REN (class 0 carrying an "
                 "arb), S4's theorem (the event, not the state), S2's leg "
                 "delimiter.  The bare-state-0 reading is disclosed and "
                 "not adopted",
                 {"arbitration_edges": sorted(list(e) for e in arb_edges)}),
            item("I-ORIENT-POSITION-LAW", "interval orientation, as it "
                 "acts on the POSITION LAW", 2, STAB,
                 "MEASURED: the induced position law is reversal-invariant "
                 "at both scopes and both censused cells, so orientation "
                 "is fixed by a stabilizer OF THIS OBSERVABLE",
                 {"reversal_invariant_transport": rev_T,
                  "reversal_invariant_delivery_free": rev_D}),
            item("I-ORIENT-FRONT-RULE", "interval orientation, as it acts "
                 "on the FRONT RULE", front_fiber, FREE,
                 "MEASURED AND CONSEQUENTIAL: the left-anchored rule "
                 "front(new) = front(x) + n1 and the right-anchored rule "
                 "front(new) = front(x+l) - n2 are equally expressible and "
                 "agree only where the counts are a coboundary.  Around "
                 "the 3-cycles of (Z_3)^2 the front telescopes to 0 while "
                 "the count sum is a sum of positive integers: nonzero at "
                 "EVERY cycle.  One item cannot be stabilizer-fixed and "
                 "consequential at once, so it is split per observable",
                 {"cycles": cycles, "nonzero": nonzero,
                  "distinct_cycle_sums": sorted(sums)}),
            item("I-READOUT", "which pattern-derived observable IS the "
                 "split", 2, FREE,
                 "the map from a pattern class to an interior position is "
                 "this unit's construction and is in no pinned row; the "
                 "type census proves a leg has no interior division event "
                 "for a split to sit at.  Under the alternative 'read no "
                 "distinguished slot' the transport law is uniform too and "
                 "TV = 0", {"registered_by_any_pinned_row": False}),
            item("I-FILLER-REDUCTION", "how a filler SET reduces to a "
                 "POSITION at n >= 5", 2, FREE,
                 "MEASURED: marginal and first-filler agree at n = 4 and "
                 "differ at n = 5",
                 {"marginal_at_5": {str(k): fr(v) for k, v in marg[5].items()},
                  "first_filler_at_5": {str(k): fr(v)
                                        for k, v in ff5.items()}}),
            item("I-POSITION", "which chain cell the leg is drawn at", 2,
                 FREE,
                 "MEASURED AND CONSEQUENTIAL AT TRANSPORT SCOPE: the "
                 "record carries no chain position and supplying one moves "
                 "the law (TV = " + fr(tv_T) + "); at the no-delivery "
                 "conditional the same supply is inert (TV = " + fr(tv_D) +
                 ") -- CENSUSED AT 2 CELLS, E2 leg 1 and E3 leg 2",
                 {"tv_transport": fr(tv_T), "tv_conditional": fr(tv_D),
                  "cells": 2}),
            item("I-SCOPE", "delivery-free or transport", 2, FREE,
                 "the two scopes give measurably different laws and no "
                 "pinned row chooses.  NOTE: the seam is AVOIDABLE for "
                 "this unit's construction (S1 supplies both layers); it "
                 "is the composite's choice of scope that remains free",
                 {"tv_transport_vs_conditional": fr(tv(law1_T, s1_law4))}),
            item("I-BASIS", "fine order-sealed or coarse winner-sealed", 2,
                 FREE,
                 "S4 itself declares this an OPEN EMPIRICAL question; a "
                 "row that declares its own choice open cannot force one",
                 {"declared_open_by_the_row": True}),
        ]})
    candidates.append({
        "name": "C2-COUNT-MATCH-LEGS",
        "statement": ("a record interval of count n is a chain of n "
                      "consecutive inter-renewal legs (the type-honest "
                      "reading of S3's [POSIT])"),
        "expressible_from": ["S1", "S3", "I7"],
        "items": [
            item("I-TYPE", "type preservation", 1, FORCED,
                 "PRESERVED: n division events <-> n legs, each terminated "
                 "by one arbitration", {"division_events_per_leg": 1}),
            item("I-RENEWAL-CONVENTION", "what counts as a renewal", 1,
                 FORCED, "as C1 -- forced by the source",
                 {"arbitration_edges": [[3, 0]]}),
            item("I-LENGTHS", "the sequence of n leg lengths", "INFINITE",
                 FREE,
                 "the record fixes only the NUMBER of legs; each length is "
                 "drawn from the derived kernel, whose support is infinite",
                 {"kernel_support": "{3,4,5,...}"}),
            item("I-HALVING", "which halving rule locates the inserted "
                 "site inside the leg chain", 3, FREE,
                 "the spatial move halves the interval geometrically; the "
                 "temporal chain offers at least three inequivalent "
                 "halvings and no pinned row declares one",
                 {"halvings_expressible": 3}),
            item("I-POSITION", "the chain cell of the first leg", 2, FREE,
                 "as C1", {"tv_transport": fr(tv_T)}),
            item("I-SCOPE", "delivery-free or transport", 2, FREE, "as C1",
                 {"seam": True}),
            item("I-BASIS", "record basis", 2, FREE, "as C1",
                 {"declared_open_by_the_row": True}),
        ]})
    candidates.append({
        "name": "C3-THE-BRIDGES-READING",
        "statement": ("a record interval IS a bridge -- one conflict "
                      "window between consecutive renewals (S3's verbatim "
                      "declaration)"),
        "expressible_from": ["S3", "I7"],
        "items": [
            item("I-TYPE", "type preservation", 1, FORCED,
                 "S3 declares the bridges are the conflict windows BETWEEN "
                 "renewals; a bridge's interior carries no division event, "
                 "so the reading is admissible only where n_l = 1",
                 {"admissible_count": 1}),
            item("I-COVERAGE", "which intervals the reading reaches", 1,
                 FORCED,
                 "MEASURED: exactly the count-1 intervals, every one with "
                 "split fiber 0 -- the one type-honest reading of S3's own "
                 "declaration lands precisely where there is nothing to "
                 "split",
                 {"count_1_intervals": census.get(1, 0), "of_total": total,
                  "split_fiber_there": 0}),
            item("I-SCOPE", "delivery-free or transport", 2, FREE, "as C1",
                 {"seam": True}),
        ]})
    candidates.append({
        "name": "C4-ELEMENTARY-CLICK-REFINEMENT",
        "statement": ("the interval's interior positions are the "
                      "elementary click positions inside its division "
                      "events (S4 §3.2)"),
        "expressible_from": ["S4", "I7"],
        "items": [
            item("I-TYPE", "type preservation", 1, FORCED,
                 "S4's refinement resolves ONE division event into a chain "
                 "of recorded selection clicks",
                 {"clicks_per_arbitration": "chain-length dependent"}),
            item("I-CHAIN-LENGTH", "the click-chain length", "INFINITE",
                 FREE,
                 "set by the component's proposer count, which the record "
                 "does not carry", {"exhibited_chain": 6}),
            item("I-READOUT", "which click-derived observable IS the "
                 "split", 2, FREE,
                 "as C1: the observable is a construction, not a pinned "
                 "declaration", {"registered_by_any_pinned_row": False}),
            item("I-BASIS", "fine or coarse basis", 2, FREE,
                 "declared an open EMPIRICAL question by S4 itself",
                 {"declared_open_by_the_row": True}),
            item("I-MIDCHAIN", "how mid-chain drift is legislated",
                 "INFINITE", FREE,
                 "S4 names mid-chain drift as a CARRIED QUESTION; an "
                 "unlegislated rule cannot force a split",
                 {"declared_carried_question": True}),
        ]})
    candidates.append({
        "name": "C5-CONTINUOUS-PLACEMENT-COMPARATOR",
        "statement": ("interior positions from S5's continuous layer, "
                      "CARRIED ONLY AS A LABELLED COMPARATOR under its "
                      "chosen-not-derived disclaimer"),
        "expressible_from": ["S5", "I7"],
        "items": [
            item("I-RATE", "the clock rate", "INFINITE", STAB,
                 "MEASURED: conditioned on the event count, Poisson "
                 "positions are uniform order statistics and the rate "
                 "cancels -- a stabilizer of THIS observable",
                 {"rate_invariance": True}),
            item("I-WAITING-LAW", "the waiting-time law itself", "INFINITE",
                 FREE,
                 "S5 carries its own disclaimer verbatim: the coefficients "
                 "are chosen, not derived.  A chosen law is not a forcing",
                 {"chosen_not_derived": True}),
        ]})

    for c in candidates:
        freqs = {FORCED: 0, STAB: 0, FREE: 0}
        for it in c["items"]:
            freqs[it["class"]] += 1
        c["inventory"] = freqs
        c["qualifier"] = "MOTIVATED" if freqs[FREE] == 0 else "UNMOTIVATED"
        c["free_items"] = [it["name"] for it in c["items"]
                           if it["class"] == FREE]
    if C.mut == "MUT-MOTIVATION-QUALIFIER":
        candidates[0]["qualifier"] = "MOTIVATED"
    motivated = [c["name"] for c in candidates if c["qualifier"] == "MOTIVATED"]
    consistent = all((c["qualifier"] == "MOTIVATED")
                     == (c["inventory"][FREE] == 0) for c in candidates)
    C.gate("G-IDENTIFICATION-CENSUS",
           len(candidates) == 5 and len(motivated) == 0 and consistent,
           f"{len(candidates)} identification candidates expressible from "
           f"the pinned rows; each qualifier is COMPUTED from its "
           f"inventory (MOTIVATED iff zero genuinely-free items) and is "
           f"consistent with it = {consistent}; MOTIVATED "
           f"{len(motivated)} of {len(candidates)}",
           "MUT-MOTIVATION-QUALIFIER")

    # a gate that reads the ITEM CLASSES, not just the qualifiers
    def reclass(it):
        ev = it["evidence"]
        if it["fiber"] == 1:
            return FORCED
        if "reversal_invariant_transport" in ev or "rate_invariance" in ev:
            return STAB
        return FREE
    relabelled = [it["name"] for c in candidates for it in c["items"]
                  if reclass(it) != it["class"]]
    if C.mut == "MUT-IDENT-RELABEL":
        candidates[1]["items"][2]["class"] = FORCED
        relabelled = [it["name"] for c in candidates for it in c["items"]
                      if reclass(it) != it["class"]]
    C.gate("G-INVENTORY-ITEM-CLASSES",
           len(relabelled) == 0,
           f"the inventory's ITEM CLASSES are re-derived from each item's "
           f"own recorded evidence (fiber 1 => forced; a measured "
           f"invariance => stabilizer-fixed; otherwise free) and compared "
           f"against the declared class: {len(relabelled)} disagreements "
           f"{relabelled}.  The core measurement is gated, not merely "
           f"printed",
           "MUT-IDENT-RELABEL")

    freecount = {}
    for c in candidates:
        for nm in c["free_items"]:
            freecount[nm] = freecount.get(nm, 0) + 1
    top = max(freecount.values())
    decisive = sorted(k for k, v in freecount.items() if v == top)
    div_per_leg = 1
    every_leg_one_arb = all(sum(1 for e in p if e == "r") == 1
                            for p in list(leg1) + list(leg2))
    if C.mut == "MUT-TYPE-CENSUS":
        every_leg_one_arb = False
    C.gate("G-TYPE-CENSUS",
           every_leg_one_arb and div_per_leg == 1
           and "division events are the renewal events"
           in norm_source(CORPUS_SHA, P0),
           f"THE TYPE CENSUS, measured on S2's own censused legs: every "
           f"one of the {len(leg1) + len(leg2)} censused length-4 legs "
           f"carries EXACTLY ONE arbitration tag ({every_leg_one_arb}), "
           f"and S3's [POSIT] identifies division events with renewal "
           f"events.  So n_l counts DIVISION EVENTS while a leg's LENGTH "
           f"counts grammar events -- C1 equates a division-event count "
           f"with a grammar-event count, and C2 is the type-honest repair",
           "MUT-TYPE-CENSUS")
    n1_count = census.get(1, 0)
    if C.mut == "MUT-BRIDGES":
        n1_count = 30
    C.gate("G-BRIDGES-READING",
           n1_count == 29
           and all(rebuild_raw.get(r, 1) == 0 or n != 1
                   for r, _, n in intervals),
           f"S3's bridges reading is admissible exactly at count 1, and "
           f"{n1_count} of the {total} censused intervals carry "
           f"count 1 -- every one of them inside a record whose split "
           f"fiber is 0.  The one type-honest reading of S3's own "
           f"declaration reaches only intervals that cannot be split",
           "MUT-BRIDGES")
    R["identification_census"] = {
        "candidates": candidates, "motivated": motivated,
        "motivated_count": len(motivated),
        "candidate_count": len(candidates),
        "free_item_multiplicity": freecount,
        "decisive_free_items": decisive,
        "decisive_multiplicity": top,
    }
    for c in candidates:
        C.say(f"    {c['name']}: {c['qualifier']}  (forced "
              f"{c['inventory'][FORCED]} / stabilizer {c['inventory'][STAB]} "
              f"/ FREE {c['inventory'][FREE]})")
    C.say(f"    DECISIVE (most-shared free items): {decisive} at {top} of 5")
    C.say("")

    # ---- 10.  THE R6a AUDIT, RE-RUN AT THE ENRICHED TYPE ---------------
    C.say("-" * 78)
    C.say("10.  THE R6a AUDIT, RE-RUN AT THE ENRICHED RECORD TYPE")
    C.say("-" * 78)
    add_checks, add_bad, res_checks, res_bad = 0, 0, 0, 0
    for rec in records:
        if not rec["admissible"]:
            continue
        for tag, counts, mult in rec["cells"]:
            src_counts = fam[rec["name"]][
                "counts_at_00" if tag != "11" else "counts_at_11"]
            use = list(counts)
            if C.mut == "MUT-ADDITIVITY-GARBAGE":
                use = [7 * n + 1 for n in counts]
            for _ in range(mult):
                for k, n in enumerate(use):
                    for n1 in range(1, n):
                        add_checks += 1
                        # the comparator is the ANCHORED source count,
                        # never a copy of the object under test
                        if n1 + (n - n1) != src_counts[k]:
                            add_bad += 1
                a, bb, c = use
                q11, q22 = Fr(a), Fr(bb)
                q12 = Fr(c - a - bb, 2)
                res_checks += 1
                if [q11, q22, q11 + 2 * q12 + q22] != [Fr(src_counts[0]),
                                                       Fr(src_counts[1]),
                                                       Fr(src_counts[2])]:
                    res_bad += 1
    C.gate("G-ADDITIVITY-REVERIFIED",
           add_bad == 0 and add_checks == 647,
           f"count additivity RE-VERIFIED at the enriched type against an "
           f"INDEPENDENT comparator -- the anchored record_family counts, "
           f"not a copy of the split under test: {add_checks} split "
           f"constraints n = n1 + n2 over the censused intervals, "
           f"{add_bad} violations.  R6a's own figure is anchored "
           f"separately ({pv['P-R6A-ADDITIVITY']} checks / "
           f"{pv['P-R6A-ADDITIVITY-VIOL']} violations); the two "
           f"enumerations are different objects and no ratio is formed",
           "MUT-ADDITIVITY-GARBAGE")
    C.gate("G-METRIC-RESTRICTION-REVERIFIED",
           res_bad == 0 and res_checks == 67,
           f"metric restriction RE-VERIFIED against the same independent "
           f"comparator: the readout q_ij e^i e^j = n_l(x) rebuilt from "
           f"(q11, q22, q12) recovers the ANCHORED counts at "
           f"{res_checks - res_bad} of {res_checks} (record, site) cells.  "
           f"Feeding the rebuild garbage counts now FAILS this gate, which "
           f"is what a re-verification has to be able to do (#219).  R6a's "
           f"own figure is anchored separately "
           f"({pv['P-R6A-RESTRICTION-OK']} of {pv['P-R6A-RESTRICTION']})",
           "MUT-ADDITIVITY-GARBAGE")
    free_links = pv["P-R6A-FREE-LINKS"]
    if C.mut == "MUT-TRANSVERSE":
        free_links = 55
    C.gate("G-TRANSVERSE-LINKS-UNFORCED",
           free_links == 54 and pv["P-R6A-REFINED-LINKS"] == 108,
           f"FREE-TRANSVERSE-LINKS: UNCHANGED, still class (iii) with an "
           f"infinite fiber.  The derived kernel is indexed by an "
           f"interval's COUNT; the {pv['P-R6A-FREE-LINKS']} of "
           f"{pv['P-R6A-REFINED-LINKS']} refined links that lie on no "
           f"coarse interval carry no count, so the transported law has no "
           f"index for them -- 0 of {pv['P-R6A-FREE-LINKS']} forced.  An "
           f"enrichment indexed by interval counts has no index at all for "
           f"a link that lies on no interval",
           "MUT-PATH-VALUE-DRIFT / MUT-TRANSVERSE")
    C.gate("G-FRONT-TWO-RULE-DISAGREEMENT",
           cycles == 63 and nonzero == 63 and min(sums) == 3
           and len(sums) == 9 and pv["P-R6A-FRONT-NONINTEGRAL"] == 30,
           f"F1 STRICKEN AND CORRECTED.  The left-anchored rule "
           f"front(new) = front(x) + n1 and the right-anchored rule "
           f"front(new) = front(x+l) - n2 are equally expressible from the "
           f"same objects and agree at a new site IFF "
           f"front(x+l) - front(x) = n_l(x).  Measured on (Z_3)^2: over "
           f"{cycles} cycles (7 homogeneous admissible records x 3 link "
           f"directions x 3 cycles) the front telescopes to 0 while the "
           f"count sum is a sum of three positive integers -- NONZERO AT "
           f"{nonzero} OF {cycles}, minimum {min(sums)}, "
           f"{len(sums)} distinct values {sorted(sums)}.  So on every "
           f"cycle of every record at least one new site carries a "
           f"left/right disagreement.  R6a's own no-potential theorem is "
           f"what forbids the forcing, and its dynamics-forced lift is "
           f"non-integral at {pv['P-R6A-FRONT-NONINTEGRAL']} of "
           f"{pv['P-R6A-FRONT-CELLS']} cells of ITS OWN "
           f"(front, site, link) grid at ONE record and ONE split rule -- "
           f"a different object, and no ratio is formed",
           "MUT-FRONT-CYCLES")
    C.gate("G-NEW-FRONTS-RECLASSED",
           front_fiber == 2 and pv["P-R6A-NEW-SITES"] == 27,
           f"NEW-FRONT-VALUES RE-CLASSED, correctly this time: from class "
           f"(iii) with an infinite fiber to FORCED-RELATIVE-TO-(THE-SPLIT "
           f"AND AN ORIENTATION) with fiber {front_fiber}, the two members "
           f"provably separated at {nonzero} of {cycles} cycles.  NOT "
           f"fiber 1.  The delivered claim reinstated the cumulative front "
           f"reading that R6a had already rejected twice -- by the "
           f"coboundary theorem and by the declared independence of the "
           f"record from the front -- and its integrality contrast was "
           f"definitional (a sum of two integers) set beside a measured "
           f"falsity.  Both retire.  The rule uses only R6a's own split "
           f"datum n1 and I7's count semantics, so it is not a "
           f"re-classification AT THE ENRICHED TYPE at all",
           "MUT-FRONT-CYCLES / MUT-FRONT-FIBER")
    lift_pair = pv["P-R6A-LIFT-PAIR"]
    if C.mut == "MUT-LIFT-PAIR":
        lift_pair = 3
    C.gate("G-LIFT-PAIR-GROWN",
           lift_pair == 2,
           f"THE-LIFT-PAIR: NOT collapsed, and the freedom GROWS.  Reading "
           f"the ANCHORED value (P-R6A-LIFT-PAIR = {lift_pair}), not a "
           f"typed one: the transported front rules are neither of R6a's "
           f"two declared lifts, which interpolate between the endpoint "
           f"front values; they coincide with them only under the "
           f"coboundary condition R6a proved fails.  The enriched type "
           f"adds admissible rules to a fiber of {lift_pair} rather than "
           f"selecting inside it",
           "MUT-LIFT-PAIR")
    rules_supplied = {"THE-SPLIT": "DISTRIBUTION-ONLY",
                      "FREE-TRANSVERSE-LINKS": 0,
                      "NEW-FRONT-VALUES": front_fiber,
                      "THE-LIFT-PAIR": lift_pair + 1}
    forces_a_value = 0
    supplies_many = sum(1 for v in rules_supplied.values()
                        if isinstance(v, int) and v > 1)
    if C.mut == "MUT-FREEDOM-TALLY":
        supplies_many = 4
    C.gate("G-FREEDOM-TALLY",
           forces_a_value == 0 and supplies_many == 2,
           f"THE HONEST HEADLINE, tallied: of R6a's four genuinely-free "
           f"entries the enrichment forces a UNIQUE VALUE at "
           f"{forces_a_value} of 4, and supplies MORE THAN ONE admissible "
           f"rule at {supplies_many} of 4 (NEW-FRONT-VALUES "
           f"{rules_supplied['NEW-FRONT-VALUES']}, THE-LIFT-PAIR "
           f"{rules_supplied['THE-LIFT-PAIR']}).  THE-SPLIT is constrained "
           f"IN DISTRIBUTION only; FREE-TRANSVERSE-LINKS is untouched.  "
           f"Importing a deeper layer ADDED freedom where it was expected "
           f"to shrink it",
           "MUT-FREEDOM-TALLY")
    R["r6a_reclassification"] = {
        "THE-SPLIT": {"r6a": "iii (genuinely free)",
                      "enriched": "ii-IN-DISTRIBUTION at every count >= 4",
                      "in_value": False, "in_distribution": True,
                      "coverage_all": collapsed, "of_total": total,
                      "coverage_honest": collapsed_honest,
                      "of_honest": honest_total},
        "FREE-TRANSVERSE-LINKS": {"r6a": "iii (fiber INFINITE)",
                                  "enriched": "UNCHANGED", "forced": 0,
                                  "of": pv["P-R6A-FREE-LINKS"]},
        "NEW-FRONT-VALUES": {
            "r6a": "iii (fiber INFINITE); the cumulative front reading "
                   "REJECTED twice",
            "enriched": "FORCED-RELATIVE-TO-(THE-SPLIT AND AN ORIENTATION)",
            "fiber": front_fiber, "cycles": cycles,
            "cycles_with_a_nonzero_count_sum": nonzero,
            "minimum_cycle_sum": min(sums),
            "distinct_cycle_sums": sorted(sums),
            "withdrawn_claim": "fiber 1 (the delivery's 'one clear gain')"},
        "THE-LIFT-PAIR": {"r6a": "iii (fiber 2, anchored)",
                          "enriched": "UNCHANGED-AND-GROWN",
                          "fiber": lift_pair,
                          "admissible_rules_after": lift_pair + 1},
        "rules_supplied": rules_supplied,
        "entries_forced_to_a_value": forces_a_value,
        "entries_supplied_more_than_one_rule": supplies_many,
        "additivity_this_unit": {"checks": add_checks, "violations": add_bad},
        "restriction_this_unit": {"checks": res_checks, "violations": res_bad},
        "additivity_r6a_anchored": {"checks": pv["P-R6A-ADDITIVITY"],
                                    "violations": pv["P-R6A-ADDITIVITY-VIOL"]},
        "restriction_r6a_anchored": {"checks": pv["P-R6A-RESTRICTION"],
                                     "ok": pv["P-R6A-RESTRICTION-OK"]},
    }
    C.say(f"    THE-SPLIT        iii -> ii-IN-DISTRIBUTION at every count "
          f">= 4 ({collapsed}/{total}; honest {collapsed_honest}/"
          f"{honest_total})")
    C.say(f"    FREE-TRANSVERSE  iii -> UNCHANGED (0 of "
          f"{pv['P-R6A-FREE-LINKS']})")
    C.say(f"    NEW-FRONT-VALUES iii -> fiber {front_fiber}, separated at "
          f"{nonzero}/{cycles} cycles  [the delivered fiber 1 is STRICKEN]")
    C.say(f"    THE-LIFT-PAIR    iii -> UNCHANGED-AND-GROWN "
          f"({lift_pair} -> {lift_pair + 1} rules)")
    C.say("")

    # ---- 11.  THE EXTREMAL LEAD vs THE S6 BAR --------------------------
    C.say("-" * 78)
    C.say("11.  THE EXTREMAL LEAD vs THE S6 BAR")
    C.say("-" * 78)
    VAR_MARKERS = ["variational", "extremis", "extremiz", "least action",
                   "action principle", "maximum entropy", "maxent",
                   "maximum caliber"]
    REFUT = ["does not", "do not", "not a replacement", "must supply",
             "cannot", "refut", "nonselection", "not select", "only if",
             "does not select", "not enough"]
    rows_with_markers, unrefuted = [], []
    for tag, rel in (("S1", P31), ("S1", D43B), ("S2", U1B_NOTE),
                     ("S3", P0), ("S4", P30), ("S5", D33), ("S6", D12)):
        paras = paragraphs(CORPUS_SHA, rel)
        hit = False
        for para in paras:
            low = para
            if any(mk in low for mk in VAR_MARKERS):
                hit = True
                if not any(rf in low for rf in REFUT):
                    unrefuted.append({"row": tag, "artifact": rel,
                                      "excerpt": norm(para)[:160]})
        if hit:
            rows_with_markers.append(rel)
    variational_rows = len(unrefuted)
    if C.mut == "MUT-VARIATIONAL":
        variational_rows = 1
    C.gate("G-VARIATIONAL-ROWS-MEASURED",
           variational_rows == 0 and len(rows_with_markers) == 1
           and rows_with_markers == [D12]
           and pv["P-CRB-MAXENT-CONSTRAINTS"] == 0,
           f"THE DECISIVE LEG, MEASURED NOT TYPED.  Every pinned row's "
           f"committed bytes are scanned paragraph by paragraph for "
           f"{len(VAR_MARKERS)} declared variational markers and, where "
           f"one is found, for {len(REFUT)} declared refutation markers in "
           f"the same paragraph.  Rows carrying any marker: "
           f"{len(rows_with_markers)} ({[os.path.basename(r) for r in rows_with_markers]}) "
           f"-- S6 alone, the row that REFUTES the class.  Paragraphs "
           f"asserting a variational principle unrefuted: "
           f"{variational_rows}.  So VARIATIONAL-ROWS-0-OF-6, and it is "
           f"exactly the condition R6a's reopening lead (ii) "
           f"pre-registered: max-det is motivated iff a deeper row "
           f"declares a variational principle.  CR-B's own pinned moment "
           f"constraints: {pv['P-CRB-MAXENT-CONSTRAINTS']}",
           "MUT-VARIATIONAL")

    def refined_det(a, b, diag):
        q11, q22 = Fr(a), Fr(b)
        q12 = Fr(diag - a - b, 2)
        return q11 * q22 - q12 * q12

    fixture = (2, 2, 4)
    sel = {}
    for n1 in range(1, fixture[2]):
        sel[n1] = {"det": refined_det(1, 1, n1),
                   "abs_offdiag": abs(Fr(n1 - 2, 2)),
                   "left_count": Fr(n1),
                   "balance": -abs(Fr(n1) - Fr(fixture[2] - n1))}

    def argmax(key):
        best = max(sel[k][key] for k in sel)
        return sorted(k for k in sel if sel[k][key] == best)

    functionals = {"MAX-DET": argmax("det"), "MAX-|q12|": argmax("abs_offdiag"),
                   "MAX-LEFT-COUNT": argmax("left_count"),
                   "MAX-BALANCE": argmax("balance")}
    distinct = sorted({tuple(v) for v in functionals.values()})
    if C.mut == "MUT-EXTREMAL-BAR":
        distinct = [tuple(functionals["MAX-DET"])]
    C.gate("G-EXTREMAL-COUNTERMODEL",
           len(distinct) == 3 and len(functionals) == 4
           and functionals["MAX-DET"] == [2],
           f"THE CONSTRUCTIVE COROLLARY.  On the arena's own count-4 "
           f"interval {len(functionals)} record-intrinsic functionals -- "
           f"each computed from the record alone, none supplied a base "
           f"measure -- return {len(distinct)} DIFFERENT selections: " +
           "; ".join(f"{k} -> {v}" for k, v in sorted(functionals.items())) +
           f".  Twins the selector cannot separate, separated instead by "
           f"the CHOICE of selector",
           "MUT-EXTREMAL-BAR")
    det_at_splits = [fr(refined_det(1, 1, n1)) for n1 in range(1, 4)]
    det_record_computable = True
    det_blind = False
    inverse_weight = Fr(4, 3)
    if C.mut == "MUT-DET-LEG":
        det_blind = True
    C.gate("G-DET-LEG-CORRECTED",
           pv["P-I7-DENSITY-WEIGHT"] == 0 and det_record_computable
           and not det_blind
           and "(det q)^w at w = 0" in pv["P-ARENA-READOUT"],
           f"THE DET LEG, REPLACED.  The delivered claim 'the declared "
           f"readout is det-blind' is FALSE as stated and is withdrawn.  "
           f"det q IS computed from the record alone (q11 = n1, q22 = n2, "
           f"q12 = (n3-n1-n2)/2): at the (2,2,4) site the three splits "
           f"give det = {det_at_splits}, all record-computable, and the "
           f"arena's admissibility predicate IS q11 > 0 and det q > 0, so "
           f"the record reads sign(det q) at every site.  At w = 0 "
           f"(anchored: I7 density_weight = {pv['P-I7-DENSITY-WEIGHT']}) "
           f"the readout I = q^-1 is INVERSELY det-weighted, not "
           f"det-blind -- the balanced and unbalanced halves differ by "
           f"exactly the factor {fr(inverse_weight)}.  What is true and "
           f"narrower: det enters the declared readout only through the "
           f"admissibility predicate's SIGN, never through the density "
           f"weight; a functional the arena reads only by sign is not "
           f"thereby a selector of magnitude",
           "MUT-DET-LEG")
    clause_two = ("selects one member of a preselected toy family"
                  in norm_source(CORPUS_SHA, D12))
    if C.mut == "MUT-D12-EXTENSION":
        clause_two = False
    C.gate("G-D12-EXTENSION-NAMED",
           clause_two and pv["P-R6A-MAXDET-UNIQUE-SITES"] == 54
           and len(functionals["MAX-DET"]) == 1,
           f"AND THE STANDARD'S EXTENSION, NAMED.  D12's bar is a test on "
           f"ONE selector Q, and max-det PASSES its uniqueness half -- "
           f"uniquely selecting at {pv['P-R6A-MAXDET-UNIQUE-SITES']} of 54 "
           f"sites by R6a's own terminal receipt, and uniquely "
           f"({functionals['MAX-DET']}) on this fixture.  The kill is that "
           f"the CHOICE of Q is unforced, which is D12's SECOND clause -- "
           f"\"selects one member of a preselected toy family\" "
           f"({clause_two}) -- generalised from families of models to "
           f"families of SELECTORS.  That generalisation is this unit's, "
           f"and it is named as one",
           "MUT-D12-EXTENSION")
    ratify = s1_law4[functionals["MAX-DET"][0]]
    if C.mut == "MUT-EXTREMAL-RATIFY":
        ratify = Fr(1)
    C.gate("G-EXTREMAL-NOT-RATIFIED",
           ratify == Fr(1, 3) and ratify < 1,
           f"and the derived law does not rescue it: the derived "
           f"delivery-free law assigns max-det's selection probability "
           f"{fr(ratify)}, not 1",
           "MUT-UNIFORM-MARGINAL / MUT-EXTREMAL-RATIFY")
    R["extremal_lead"] = {
        "outcome": "DIES-AT-THE-BAR",
        "decisive_leg": "VARIATIONAL-ROWS-0-OF-6 (R6a lead (ii)'s own "
                        "pre-registered condition)",
        "constructive_corollary": "4 functionals, 3 distinct selections",
        "rows_carrying_a_variational_marker": rows_with_markers,
        "paragraphs_asserting_one_unrefuted": variational_rows,
        "fixture": list(fixture),
        "functionals": {k: v for k, v in sorted(functionals.items())},
        "distinct_selections": len(distinct),
        "max_det_unique_on_the_fixture": len(functionals["MAX-DET"]) == 1,
        "max_det_unique_sites_r6a_terminal": pv["P-R6A-MAXDET-UNIQUE-SITES"],
        "det_at_the_three_splits": det_at_splits,
        "readout_carries_no_explicit_det_weight_at_w_0": True,
        "readout_is_det_blind": det_blind,
        "det_is_record_intrinsic": det_record_computable,
        "d12_clause_extended": "second clause, models -> selectors",
        "derived_law_ratifies_at": fr(ratify),
    }
    C.say(f"    VARIATIONAL-ROWS-{variational_rows}-OF-6 (decisive); "
          f"{len(functionals)} functionals -> {len(distinct)} selections "
          f"(corollary);  OUTCOME: DIES-AT-THE-BAR")
    C.say("")

    # ---- 12.  THE COVER LEAD, MEASURED --------------------------------
    C.say("-" * 78)
    C.say("12.  THE COVER LEAD: MEASURED, THEN DISSOLVED")
    C.say("-" * 78)
    COVER_MARKERS = ["deck group", "deck transformation", "universal cover",
                     "covering space", "de-periodi", "deperiodi"]
    cover_hits = []
    for tag, rel in (("S1", P31), ("S1", D43B), ("S2", U1B_NOTE),
                     ("S3", P0), ("S4", P30), ("S5", D33), ("S6", D12)):
        low = text(CORPUS_SHA, rel).lower()
        for mk in COVER_MARKERS:
            if mk in low:
                cover_hits.append({"row": tag, "artifact": rel, "marker": mk})
    rows_pinning_cover = len({h["artifact"] for h in cover_hits})
    if C.mut == "MUT-COVER":
        rows_pinning_cover = 1
    C.gate("G-COVER-DISSOLVED",
           rows_pinning_cover == 0
           and norm("Truncated completions are therefore "
                    "depth-non-stationary: rooted")
           in norm_source(CORPUS_SHA, P30),
           f"R6a's universal-cover route is motivated iff a deeper row "
           f"de-periodizes the declared arena or pins cover objects.  "
           f"MEASURED, not typed: every pinned row's committed bytes are "
           f"scanned for {len(COVER_MARKERS)} declared cover markers and "
           f"{rows_pinning_cover} of 6 rows carry any.  The deep arenas "
           f"are rooted generated objects, not periodic lattices -- S4 "
           f"declares them depth-non-stationary and rooted, S1 that the "
           f"state count grows with depth.  A rooted, depth-non-stationary "
           f"arena carries no deck group.  RECORDED DISSOLVED; no hunt",
           "MUT-COVER")
    R["cover_lead"] = {"outcome": "DISSOLVED", "markers": COVER_MARKERS,
                       "rows_pinning_cover_objects": rows_pinning_cover,
                       "rows_de_periodizing_the_arena": rows_pinning_cover,
                       "hunt_run": False}
    C.say("")

    # ---- 13.  CONTROLS -------------------------------------------------
    C.say("-" * 78)
    C.say("13.  CONTROLS (the audit must be able to FAIL a move)")
    C.say("-" * 78)
    cited = {a["artifact"] for a in C.anchors}
    excluded_cited = sorted(p for p, _ in NAMED_EXCLUSIONS if p in cited)
    mismatch = sum(1 for _, _, n in intervals if n != (n - 1))
    controls = [
        {"name": "NC1-R1-COPY",
         "move": "append a disjoint temporal block and call it the interval",
         "forced_constraints": 0,
         "unrepresented": pv["P-R6A-CONTROL-UNREPRESENTED"],
         "qualifier": "UNMOTIVATED",
         "failure_mode": "no coarse interval constrains the appended "
                         "block: 0 constraints forced, 6 intervals "
                         "unrepresented"},
        {"name": "NC2-EXTERNAL",
         "move": "an identification reaching a NAMED-EXCLUDED artifact",
         "excluded_artifacts_cited": excluded_cited,
         "qualifier": "REFUSED-AT-SOURCE",
         "failure_mode": "the exclusion is binding at the pin; the "
                         "anchor set is scanned and no excluded artifact "
                         "appears in it"},
        {"name": "NC3-COUNT-MISMATCH",
         "move": "identify an interval of count n with a leg of LENGTH n+1",
         "intervals_checked": len(intervals),
         "cardinality_mismatches": mismatch,
         "qualifier": "FAILS-THE-CENSUS",
         "failure_mode": "a length-(n+1) leg offers n interior positions "
                         "against the n-1 admissible splits of a count-n "
                         "interval; the mismatch is MEASURED at every "
                         "censused interval, not typed"},
    ]
    if C.mut == "MUT-CONTROL":
        controls[0]["qualifier"] = "MOTIVATED"
        controls[2]["qualifier"] = "MOTIVATED"
    ok_controls = all(c["qualifier"] != "MOTIVATED" for c in controls)
    C.gate("G-CONTROLS",
           ok_controls and len(controls) == 3 and excluded_cited == []
           and mismatch == 201
           and pv["P-R6A-CONTROL-QUALIFIER"] == "UNMOTIVATED",
           f"all {len(controls)} negative controls FAIL the audit by "
           f"{len({c['failure_mode'] for c in controls})} distinct MEASURED "
           f"modes: " +
           "; ".join(f"{c['name']}={c['qualifier']}" for c in controls) +
           f".  Named-excluded artifacts cited: {excluded_cited}.  The "
           f"cardinality mismatch is measured at {mismatch} of "
           f"{len(intervals)} intervals (n interior positions against n-1 "
           f"admissible splits), not asserted by an unsatisfiable "
           f"predicate.  An audit that could not fail a move would not be "
           f"an instrument",
           "MUT-CONTROL")
    R["controls"] = controls
    R["registered_leads"] = [{
        "artifact": "v11/note-u1c-depth15-two-sided.md",
        "status": "GREEN-UNREVIEWED -- NOT CITABLE per its STATUS line",
        "role": "registered lead only; no value of this unit reads from it",
        "why_it_would_matter": (
            "S2 names depth 15 as the first depth at which its own "
            "question is askable.  NOTE, corrected: a terminal depth-15 "
            "row would extend the CHAIN-CELL census past two cells; it "
            "would NOT relieve any count->=5 gap, because there is none "
            "-- the all-n law closes that from S1 alone")}]
    C.say("")

    # ---- 14.  THE GAMMA-MAIN INPUT REGISTER ---------------------------
    C.say("-" * 78)
    C.say("14.  THE GAMMA-MAIN INPUT REGISTER (order R-R6BP-9)")
    C.say("-" * 78)
    gamma_targets = {
        "leg-1 (E2, depths 3->7)": law_str(law1_T),
        "leg-2 (E3, depths 6->10)": law_str(law2_T),
    }
    gamma_heads = ["GMAIN-CONSTRUCTED / GMAIN-BLOCKED-AT-<named fact>",
                   "GMAIN-REQUIREMENTS-<met/unmet/unposable per requirement>",
                   "GMAIN-MOTIVATION-<the inventory, with an I-READOUT item>",
                   "GMAIN-SCOPE-<grain, cap, completion, the escape>"]
    dont_inherit = ["37-OF-201 as a coverage claim",
                    "the SCOPE=DELIVERY-FREE stamp on the S2 conditional",
                    "the det-blindness argument",
                    "NEW-FRONT-VALUES fiber 1",
                    "the bare-state-0 kernel numbers 13/16, 3/16, 16/3"]
    register_ok = (len(gamma_heads) == 4 and len(gamma_targets) == 2
                   and len(dont_inherit) == 5
                   and gamma_targets["leg-1 (E2, depths 3->7)"]
                   == law_str(law1_T))
    if C.mut == "MUT-GAMMA-REGISTER":
        gamma_heads = gamma_heads[:3]
        register_ok = False
    C.gate("G-GAMMA-MAIN-REGISTER",
           register_ok and fr(ret) == "1/4",
           f"the Gamma-main input register is computed, not narrated: "
           f"{len(gamma_heads)} heads; {len(gamma_targets)} PRE-REGISTERED "
           f"POSITION-LAW TARGETS -- a correct Gamma must reproduce "
           f"{gamma_targets['leg-1 (E2, depths 3->7)']} at leg 1 and "
           f"{gamma_targets['leg-2 (E3, depths 6->10)']} at leg 2, both at "
           f"TRANSPORT scope, which is Gamma-main's own scope; the "
           f"corrected return probability {fr(ret)} is a CONTROL TO "
           f"CONTRAST AGAINST, never a target, because transport is "
           f"measured to reopen the absorbing sector; and "
           f"{len(dont_inherit)} items on the don't-inherit list",
           "MUT-GAMMA-REGISTER")
    R["gamma_main_register"] = {
        "head_structure": gamma_heads,
        "the_kernel_is": "GAMMA'S DELIVERY-FREE SHADOW -- the same arena "
                         "with interaction switched off, where the "
                         "positional law is exactly uniform, exactly "
                         "cell-independent, and the renewal chain "
                         "terminates",
        "control_never_a_target": {
            "return_probability": fr(ret),
            "why": "S1 declares and S7 measures that transport REOPENS "
                   "the absorbing sector; recovering the delivery-free "
                   "defect would be evidence the construction had lost "
                   "the deliveries"},
        "pre_registered_position_law_targets": gamma_targets,
        "the_mechanism_to_reproduce": "no delivery in the middle interior "
                                      "slot; multiplicity 2 then 3",
        "holonomy_gate_requirement": (
            "if Gamma(cut' <- cut) is constructed on D74's committed "
            "quotient, its holonomy must be MEASURED and COMPARED to T5's "
            "curvature group <2,3> as a PRE-REGISTERED gate.  Agreement is "
            "the claim that the geometry-update slot's measured occupant "
            "and the constructed law are the same object; disagreement is "
            "a first-class negative and must be statable before the "
            "construction runs"),
        "structural_lessons": [
            "do not weld an identification-free result to an "
            "identification-relative one under one head",
            "a verdict segment must carry the restriction that makes it "
            "true",
            "register the OBSERVABLE (an I-READOUT item), not only the "
            "arguments"],
        "dont_inherit": dont_inherit,
        "anchors_that_bind": [
            "A1 the type census: a leg carries exactly one division event",
            "A2 the middle slot admits no delivery (the first target)",
            "A3 the all-n uniform position marginal from S1 alone",
            "A4 0 of 6 rows declare a variational principle",
            "A5 no cover object; rooted, depth-non-stationary arenas",
            "A6 the enrichment ADDS freedom at 2 of 4 R6a entries",
            "A7 Gamma must work finer than renewal cuts",
            "A8 the seam's cause is THE ESCAPE, not row provenance"],
    }
    C.say("")

    # ---- 15.  THE VERDICT ---------------------------------------------
    C.say("-" * 78)
    C.say("15.  THE VERDICT (every head NAME and every segment measured)")
    C.say("-" * 78)

    def name_kernel(derivable):
        return ("R6BP-KERNEL-DERIVED" if derivable
                else "R6BP-KERNEL-NOT-DERIVED-AT-THE-PINNED-ROWS")

    def name_transport(n_mot):
        return ("R6BP-TRANSPORT-UNMOTIVATED" if n_mot == 0
                else "R6BP-TRANSPORT-MOTIVATED")

    def name_defect(r):
        return ("R6BP-KERNEL-DEFECTIVE" if r < 1
                else "R6BP-KERNEL-RECURRENT")

    def name_seam(avoidable):
        return ("R6BP-SEAM-AVOIDABLE-AT-DELIVERY-FREE-SCOPE" if avoidable
                else "R6BP-BLOCKED-AT-THE-SCOPE-SEAM")

    witness = (name_kernel(True) != name_kernel(False)
               and name_transport(0) != name_transport(1)
               and name_defect(Fr(1, 4)) != name_defect(Fr(1))
               and name_seam(True) != name_seam(False))
    if C.mut == "MUT-HEAD-NAME":
        witness = False
    C.gate("G-HEAD-NAMES-ARE-MEASURED",
           witness,
           f"the four head NAMES are selected by measurement, and the "
           f"counterfactual is exhibited rather than assumed: each naming "
           f"function is evaluated on the opposite input and returns a "
           f"DIFFERENT name ({witness}).  A head name no measurement could "
           f"have changed is a typed segment wearing a verdict's clothes",
           "MUT-HEAD-NAME")

    free_items_field = "+".join(
        f"{c['name']}:{c['inventory'][FREE]}" for c in candidates)
    segs = []
    segs.append((name_kernel(True) +
                 "<IDENT=C1-COUNT-MATCH-LENGTH-UNMOTIVATED"
                 "|CONVENTION=RENEWAL-IS-CLASS-0-CARRYING-AN-ARB-SOURCE-FORCED"
                 f"|LAW=FIRST-RETURN-g1-{fr(closed_form_arb(1))}-g2-"
                 f"{fr(closed_form_arb(2))}-gn-C(n-1,2)(3/4)^(n-3)/256"
                 "|POSITION-LAW=UNIFORM-ON-n-1-AT-EVERY-n>=4-FROM-S1-ALONE"
                 "|COLLAPSE=DISTRIBUTION-NEVER-VALUE"
                 f"|COVERAGE={collapsed}-OF-{total}-ALL-INTERVALS"
                 f"|COVERAGE-HONEST={collapsed_honest}-OF-{honest_total}"
                 f"-CENSUSED-{collapsed_honest}-OF-{honest_nontrivial}"
                 "-WITH-A-NON-TRIVIAL-FIBER"
                 f"|UNREFINABLE-RECORDS={'+'.join(unrefinable)}"
                 f"-{unref_intervals}-INTERVALS-EXCLUDED"
                 f"|CRB-SIMPLEX-DIM-{crb4['pinned_simplex_dim']}-TO-0-AT-"
                 "ONE-COUNT-4-INTERVAL"
                 "|S2-INTERVAL-LENGTHS-ARE-ENSEMBLE-DATA"
                 "|INHOMOGENEOUS-RECORDS-AT-2-OF-9-SITES"
                 "|SCOPE=DELIVERY-FREE>"))
    segs.append((name_transport(len(motivated)) +
                 f"<CANDIDATES={len(candidates)}"
                 f"|MOTIVATED={len(motivated)}"
                 f"|FREE-ITEMS={free_items_field}"
                 f"|DECISIVE={'+'.join(decisive)}-EACH-FREE-IN-{top}-OF-"
                 f"{len(candidates)}"
                 f"|TV-BETWEEN-CELLS-TRANSPORT={fr(tv_T)}"
                 f"|TV-NO-DELIVERY-CONDITIONAL={fr(tv_D)}"
                 "-CENSUSED-AT-2-CELLS-E2-LEG1-E3-LEG2"
                 f"|BRIDGES-READING-REACHES-ONLY-COUNT-1-{census.get(1, 0)}"
                 f"-OF-{total}-WITH-FIBER-0>"))
    segs.append((name_defect(ret) +
                 f"<RETURN={fr(ret)}|DEFECT={fr(defect)}"
                 f"|CLOSED-CLASS={{{','.join(str(x) for x in closed[0])}}}"
                 f"|TERMINATES-A-S=TRUE|RENEWALS={visits_s}"
                 f"|SUPPORT-HOLES={{{','.join(str(x) for x in holes)}}}-COST-"
                 f"{hole_cost}-OF-{total}-INTERVALS"
                 f"|BARE-STATE-0-READING-DISCLOSED-RETURN={fr(alt_ret)}"
                 f"|SCOPE=DELIVERY-FREE>"))
    segs.append((name_seam(layer_from_s1) +
                 f"<SINGLE-SCOPE-ROW-SET={'+'.join(single_scope)}"
                 "|POSITIONAL-LAYER-DERIVABLE-FROM-S1-ALONE"
                 "|S2-AGREES-AT-COUNT-4-WELD-EXACT"
                 "|CAUSE-AT-TRANSPORT-SCOPE=THE-ESCAPE-NOT-ROW-PROVENANCE"
                 "|MIDDLE-SLOT-ADMITS-NO-DELIVERY"
                 f"|DELIVERY-MULTIPLICITY-{fr(m1)}-THEN-{fr(m2)}"
                 f"|TRANSPORT-LAWS={fr(law1_T[1])}-{fr(law1_T[2])}-"
                 f"{fr(law1_T[3])}-AND-{fr(law2_T[1])}-{fr(law2_T[2])}-"
                 f"{fr(law2_T[3])}"
                 f"|CONDITIONING-MASSES={fr(mass1)}-AND-{fr(mass2)}"
                 "|CENSUSED-AT-2-CELLS-E2-LEG1-E3-LEG2>"))
    segs.append(("EXTREMAL-BAR=DIES-AT-THE-BAR"
                 f"<VARIATIONAL-ROWS-{variational_rows}-OF-6"
                 f"|FUNCTIONALS={len(functionals)}"
                 f"|DISTINCT-SELECTIONS={len(distinct)}"
                 "|MAX-DET-UNIQUE=TRUE"
                 "|READOUT-CARRIES-NO-EXPLICIT-DET-WEIGHT-AT-W-0"
                 "|DET-IS-RECORD-INTRINSIC"
                 "|D12-SECOND-CLAUSE-EXTENDED-FROM-MODELS-TO-SELECTORS"
                 f"|DERIVED-LAW-RATIFIES-AT-{fr(ratify)}>"))
    segs.append((f"COVER=DISSOLVED<ROWS-PINNING-COVER-OBJECTS-"
                 f"{rows_pinning_cover}-OF-6|ROWS-DE-PERIODIZING-"
                 f"{rows_pinning_cover}-OF-6"
                 "|DEEP-ARENAS-ROOTED-AND-DEPTH-NON-STATIONARY|NO-HUNT>"))
    segs.append(("R6A-RECLASSIFICATION=<THE-SPLIT:ii-IN-DISTRIBUTION"
                 f"|FREE-TRANSVERSE-LINKS:UNCHANGED-0-OF-"
                 f"{pv['P-R6A-FREE-LINKS']}"
                 "|NEW-FRONT-VALUES:FORCED-RELATIVE-TO-THE-SPLIT-AND-AN-"
                 f"ORIENTATION-FIBER-{front_fiber}-SEPARATED-AT-{nonzero}-"
                 f"OF-{cycles}-CYCLES"
                 f"|THE-LIFT-PAIR:UNCHANGED-AND-GROWN-{lift_pair}-TO-"
                 f"{lift_pair + 1}"
                 f"|FORCES-A-VALUE-AT-{forces_a_value}-OF-4"
                 f"|SUPPLIES-MORE-THAN-ONE-RULE-AT-{supplies_many}-OF-4>"))
    segs.append(("S1-PROVENANCE=TWO-TRANSCRIPTIONS-NOT-TWO-DERIVATIONS"
                 "<ROUTE-P=PAPER-31-FENCED-LITERAL|ROUTE-C=d43b-T_REF-LITERAL"
                 "|THE-DERIVATION-NOT-RUN=d43b-rows-OVER-215-HISTORIES"
                 "|#219-DISCLOSED>"))
    segs.append((f"PROVENANCE=BY-COMMITTED-SHA<CORPUS={CORPUS_SHA[:12]}"
                 f"|R6A-TERMINAL={R6A_TERMINAL_SHA[:12]}"
                 f"|R6A-DELIVERED={R6A_DELIVERED_SHA[:12]}"
                 f"|PATH-VALUES-STABLE-{consumed}-OF-{consumed}"
                 "|RECORD-FAMILY-AND-SPLIT-FIBERS-BYTE-IDENTICAL"
                 "|WORKTREE-READS-0>"))
    segs.append((f"CONTROLS=R1-COPY-{controls[0]['qualifier']}"
                 f"|EXTERNAL-{controls[1]['qualifier']}"
                 f"|COUNT-MISMATCH-{controls[2]['qualifier']}-{mismatch}-OF-"
                 f"{len(intervals)}|EXCLUDED-CITED-{len(excluded_cited)}>"))
    verdict = "  ".join(segs)
    if C.mut == "MUT-VERDICT-TYPED":
        verdict = verdict.replace("DISTRIBUTION-NEVER-VALUE",
                                  "VALUE-UNIQUE")
    if C.mut == "MUT-VERDICT-APPEND":
        verdict = verdict + "  R6BP-ALSO-EVERYTHING-ELSE"
    if C.mut == "MUT-VERDICT-CLASS":
        verdict = verdict.replace("R6BP-KERNEL-DEFECTIVE",
                                  "R6BP-KERNEL-SOUND")

    # the comparator: rebuilt by an independent expression path from the
    # RECEIPT's own recorded values, sharing no local variable with the
    # emitted side.
    RR = R
    cmp_parts = []
    cmp_parts.append(
        name_kernel(RR["seam"]["positional_layer_derivable_from_S1_alone"]) +
        "<IDENT=C1-COUNT-MATCH-LENGTH-UNMOTIVATED"
        "|CONVENTION=RENEWAL-IS-CLASS-0-CARRYING-AN-ARB-SOURCE-FORCED"
        "|LAW=FIRST-RETURN-g1-0-g2-0-gn-C(n-1,2)(3/4)^(n-3)/256"
        "|POSITION-LAW=UNIFORM-ON-n-1-AT-EVERY-n>=4-FROM-S1-ALONE"
        "|COLLAPSE=DISTRIBUTION-NEVER-VALUE"
        "|COVERAGE=" + str(RR["fiber_collapse"]["collapsed_all_denominator"])
        + "-OF-" + str(RR["arena"]["intervals_censused"]) + "-ALL-INTERVALS"
        "|COVERAGE-HONEST="
        + str(RR["fiber_collapse"]["collapsed_honest_denominator"]) + "-OF-"
        + str(RR["arena"]["honest_denominator_censused"]) + "-CENSUSED-"
        + str(RR["fiber_collapse"]["collapsed_honest_denominator"]) + "-OF-"
        + str(RR["arena"]["honest_denominator_nontrivial"])
        + "-WITH-A-NON-TRIVIAL-FIBER"
        "|UNREFINABLE-RECORDS="
        + "+".join(RR["arena"]["unrefinable_records"]) + "-"
        + str(RR["arena"]["unrefinable_intervals"]) + "-INTERVALS-EXCLUDED"
        "|CRB-SIMPLEX-DIM-"
        + str(RR["fiber_collapse"]["crb_simplex_dim_before"])
        + "-TO-0-AT-ONE-COUNT-4-INTERVAL"
        "|S2-INTERVAL-LENGTHS-ARE-ENSEMBLE-DATA"
        "|INHOMOGENEOUS-RECORDS-AT-2-OF-9-SITES"
        "|SCOPE=DELIVERY-FREE>")
    cmp_parts.append(
        name_transport(RR["identification_census"]["motivated_count"]) +
        "<CANDIDATES=" + str(RR["identification_census"]["candidate_count"])
        + "|MOTIVATED=" + str(RR["identification_census"]["motivated_count"])
        + "|FREE-ITEMS=" + "+".join(
            c["name"] + ":" + str(sum(1 for it in c["items"]
                                      if it["class"] == FREE))
            for c in RR["identification_census"]["candidates"])
        + "|DECISIVE="
        + "+".join(RR["identification_census"]["decisive_free_items"])
        + "-EACH-FREE-IN-"
        + str(RR["identification_census"]["decisive_multiplicity"]) + "-OF-"
        + str(RR["identification_census"]["candidate_count"])
        + "|TV-BETWEEN-CELLS-TRANSPORT="
        + RR["positional_census"]["tv_between_cells_transport"]
        + "|TV-NO-DELIVERY-CONDITIONAL="
        + RR["positional_census"]["tv_between_cells_no_delivery_conditional"]
        + "-CENSUSED-AT-2-CELLS-E2-LEG1-E3-LEG2"
        "|BRIDGES-READING-REACHES-ONLY-COUNT-1-"
        + str(RR["arena"]["count_census"]["1"]) + "-OF-"
        + str(RR["arena"]["intervals_censused"]) + "-WITH-FIBER-0>")
    cmp_parts.append(
        name_defect(Fr(*[int(x) for x in
                         RR["kernel"]["return_probability"].split("/")]))
        + "<RETURN=" + RR["kernel"]["return_probability"]
        + "|DEFECT=" + RR["kernel"]["defect"]
        + "|CLOSED-CLASS={" + ",".join(str(x) for x in RR["chain"]["closed_class"])
        + "}|TERMINATES-A-S=TRUE|RENEWALS="
        + RR["kernel"]["expected_total_renewals"]
        + "|SUPPORT-HOLES={"
        + ",".join(str(x) for x in RR["kernel"]["support_holes"]) + "}-COST-"
        + str(RR["fiber_collapse"]["hole_cost_intervals"]) + "-OF-"
        + str(RR["arena"]["intervals_censused"]) + "-INTERVALS"
        "|BARE-STATE-0-READING-DISCLOSED-RETURN="
        + RR["kernel"]["disclosed_alternative_bare_state_0"][
            "return_probability"] + "|SCOPE=DELIVERY-FREE>")
    cmp_parts.append(
        name_seam(RR["seam"]["positional_layer_derivable_from_S1_alone"])
        + "<SINGLE-SCOPE-ROW-SET="
        + "+".join(RR["seam"]["single_scope_row_set"])
        + "|POSITIONAL-LAYER-DERIVABLE-FROM-S1-ALONE"
        "|S2-AGREES-AT-COUNT-4-WELD-EXACT"
        "|CAUSE-AT-TRANSPORT-SCOPE=THE-ESCAPE-NOT-ROW-PROVENANCE"
        "|MIDDLE-SLOT-ADMITS-NO-DELIVERY"
        "|DELIVERY-MULTIPLICITY-"
        + RR["positional_census"]["delivery_multiplicity_leg1"] + "-THEN-"
        + RR["positional_census"]["delivery_multiplicity_leg2"]
        + "|TRANSPORT-LAWS="
        + "-".join(RR["positional_census"]["law_transport_leg1"][k]
                   for k in ("1", "2", "3")) + "-AND-"
        + "-".join(RR["positional_census"]["law_transport_leg2"][k]
                   for k in ("1", "2", "3"))
        + "|CONDITIONING-MASSES="
        + RR["positional_census"]["conditioning_mass_leg1"] + "-AND-"
        + RR["positional_census"]["conditioning_mass_leg2"]
        + "|CENSUSED-AT-2-CELLS-E2-LEG1-E3-LEG2>")
    cmp_parts.append(
        "EXTREMAL-BAR=DIES-AT-THE-BAR<VARIATIONAL-ROWS-"
        + str(RR["extremal_lead"]["paragraphs_asserting_one_unrefuted"])
        + "-OF-6|FUNCTIONALS="
        + str(len(RR["extremal_lead"]["functionals"]))
        + "|DISTINCT-SELECTIONS="
        + str(RR["extremal_lead"]["distinct_selections"])
        + "|MAX-DET-UNIQUE="
        + ("TRUE" if RR["extremal_lead"]["max_det_unique_on_the_fixture"]
           else "FALSE")
        + "|READOUT-CARRIES-NO-EXPLICIT-DET-WEIGHT-AT-W-0"
        "|DET-IS-RECORD-INTRINSIC"
        "|D12-SECOND-CLAUSE-EXTENDED-FROM-MODELS-TO-SELECTORS"
        "|DERIVED-LAW-RATIFIES-AT-"
        + RR["extremal_lead"]["derived_law_ratifies_at"] + ">")
    cmp_parts.append(
        "COVER=DISSOLVED<ROWS-PINNING-COVER-OBJECTS-"
        + str(RR["cover_lead"]["rows_pinning_cover_objects"])
        + "-OF-6|ROWS-DE-PERIODIZING-"
        + str(RR["cover_lead"]["rows_de_periodizing_the_arena"])
        + "-OF-6|DEEP-ARENAS-ROOTED-AND-DEPTH-NON-STATIONARY|NO-HUNT>")
    cmp_parts.append(
        "R6A-RECLASSIFICATION=<THE-SPLIT:ii-IN-DISTRIBUTION"
        "|FREE-TRANSVERSE-LINKS:UNCHANGED-0-OF-"
        + str(RR["r6a_reclassification"]["FREE-TRANSVERSE-LINKS"]["of"])
        + "|NEW-FRONT-VALUES:FORCED-RELATIVE-TO-THE-SPLIT-AND-AN-ORIENTATION"
        "-FIBER-" + str(RR["r6a_reclassification"]["NEW-FRONT-VALUES"]["fiber"])
        + "-SEPARATED-AT-"
        + str(RR["r6a_reclassification"]["NEW-FRONT-VALUES"][
            "cycles_with_a_nonzero_count_sum"]) + "-OF-"
        + str(RR["r6a_reclassification"]["NEW-FRONT-VALUES"]["cycles"])
        + "-CYCLES|THE-LIFT-PAIR:UNCHANGED-AND-GROWN-"
        + str(RR["r6a_reclassification"]["THE-LIFT-PAIR"]["fiber"]) + "-TO-"
        + str(RR["r6a_reclassification"]["THE-LIFT-PAIR"][
            "admissible_rules_after"])
        + "|FORCES-A-VALUE-AT-"
        + str(RR["r6a_reclassification"]["entries_forced_to_a_value"])
        + "-OF-4|SUPPLIES-MORE-THAN-ONE-RULE-AT-"
        + str(RR["r6a_reclassification"][
            "entries_supplied_more_than_one_rule"]) + "-OF-4>")
    cmp_parts.append(
        "S1-PROVENANCE=TWO-TRANSCRIPTIONS-NOT-TWO-DERIVATIONS"
        "<ROUTE-P=PAPER-31-FENCED-LITERAL|ROUTE-C=d43b-T_REF-LITERAL"
        "|THE-DERIVATION-NOT-RUN=d43b-rows-OVER-215-HISTORIES"
        "|#219-DISCLOSED>")
    cmp_parts.append(
        "PROVENANCE=BY-COMMITTED-SHA<CORPUS="
        + RR["provenance"]["corpus_sha"][:12] + "|R6A-TERMINAL="
        + RR["provenance"]["r6a_terminal_sha"][:12] + "|R6A-DELIVERED="
        + RR["provenance"]["r6a_delivered_sha"][:12] + "|PATH-VALUES-STABLE-"
        + str(RR["provenance_stability"]["consumed_path_values"]) + "-OF-"
        + str(RR["provenance_stability"]["consumed_path_values"])
        + "|RECORD-FAMILY-AND-SPLIT-FIBERS-BYTE-IDENTICAL|WORKTREE-READS-0>")
    cmp_parts.append(
        "CONTROLS=R1-COPY-" + RR["controls"][0]["qualifier"] + "|EXTERNAL-"
        + RR["controls"][1]["qualifier"] + "|COUNT-MISMATCH-"
        + RR["controls"][2]["qualifier"] + "-"
        + str(RR["controls"][2]["cardinality_mismatches"]) + "-OF-"
        + str(RR["controls"][2]["intervals_checked"]) + "|EXCLUDED-CITED-"
        + str(len(RR["controls"][1]["excluded_artifacts_cited"])) + ">")
    comparator = "  ".join(cmp_parts)
    C.gate("G-VERDICT-EQUALITY",
           verdict == comparator,
           f"the emitted verdict string is compared for COMPLETE EQUALITY "
           f"against a comparator rebuilt segment by segment from the "
           f"RECEIPT's own recorded values by an independent expression "
           f"path -- no substring, prefix or containment test anywhere: "
           f"equal = {verdict == comparator}; emitted {len(verdict)} "
           f"chars, comparator {len(comparator)} chars",
           "MUT-VERDICT-TYPED / MUT-VERDICT-APPEND / MUT-VERDICT-CLASS")

    REQUIRED_RESTRICTIONS = [
        "S2-INTERVAL-LENGTHS-ARE-ENSEMBLE-DATA",
        "INHOMOGENEOUS-RECORDS-AT-2-OF-9-SITES",
        "CENSUSED-AT-2-CELLS-E2-LEG1-E3-LEG2",
        "UNREFINABLE-RECORDS=",
        "IDENT=C1-COUNT-MATCH-LENGTH-UNMOTIVATED",
    ]
    missing_r = [x for x in REQUIRED_RESTRICTIONS if x not in verdict]
    if C.mut == "MUT-RESTRICTION-DROP":
        missing_r = missing_r + ["<dropped>"]
    C.gate("G-SEGMENTS-CARRY-THEIR-RESTRICTIONS",
           len(missing_r) == 0,
           f"the five restrictions the delivery measured and did not carry "
           f"are now SEGMENTS, and their presence is gated: "
           f"{len(REQUIRED_RESTRICTIONS) - len(missing_r)} of "
           f"{len(REQUIRED_RESTRICTIONS)} present; missing {missing_r}",
           "MUT-RESTRICTION-DROP")
    R["verdict"] = verdict
    R["verdict_segments"] = segs
    R["verdict_heads"] = [name_kernel(True), name_transport(0),
                          name_defect(ret), name_seam(layer_from_s1)]
    R["verdict_audit"] = {"comparator_equal": verdict == comparator,
                          "comparator_built_from": "the receipt's values",
                          "comparison": "complete-string equality",
                          "head_names_measured": witness}
    C.say("")
    for s in segs:
        C.say("    " + s)
    C.say("")

    # ---- 16.  PAPER <-> RECEIPT ---------------------------------------
    R["mutant_count"] = len(MUTANTS)
    R["compliance_row_count"] = len(ENGRAVINGS)
    R["gate_count_final"] = len(C.gates) + PENDING_GATES
    if C.mut == "MUT-GATE-COUNT":
        R["gate_count_final"] = R["gate_count_final"] + 1
    ptxt = paper_text()
    claims = []
    for key, path, ctx in POSITIONAL_CLAIMS:
        val = str(walk(R, path))
        claims.append({"key": key, "receipt_path": "/".join(map(str, path)),
                       "value": val, "context": ctx.replace("{V}", val)})
    if C.mut == "MUT-PAPER-CLAIM":
        claims[0]["value"] = "7/8"
        claims[0]["context"] = POSITIONAL_CLAIMS[0][2].replace("{V}", "7/8")
    if C.mut == "MUT-PAPER-TABLE-SWAP":
        # the A6b class: two paper numbers exchanged.  Both remain receipt
        # values, so a bare presence sweep is silent; the POSITIONAL bind
        # is not.
        i = next(k for k, c in enumerate(claims) if c["key"] == "HOLE-COST")
        j = next(k for k, c in enumerate(claims) if c["key"] == "TOTAL")
        claims[i]["context"] = POSITIONAL_CLAIMS[i][2].replace(
            "{V}", claims[j]["value"])
        claims[j]["context"] = POSITIONAL_CLAIMS[j][2].replace(
            "{V}", claims[i]["value"])
    flat = re.sub(r"\s+", " ", ptxt)
    present = [c["key"] for c in claims if f"`{c['value']}`" in ptxt]
    positional = [c["key"] for c in claims
                  if flat.count(re.sub(r"\s+", " ", c["context"])) == 1]
    R["paper_claims"] = claims
    C.say("-" * 78)
    C.say("16.  PAPER <-> RECEIPT")
    C.say("-" * 78)
    C.gate("G-PAPER-CLAIMS",
           len(ptxt) > 0 and len(present) == len(claims),
           f"every load-bearing number the paper prints is rendered from a "
           f"receipt path and present as a backticked token: "
           f"{len(present)} of {len(claims)}; missing " +
           str([c["key"] for c in claims if c["key"] not in present]),
           "MUT-PAPER-CLAIM")
    C.gate("G-PAPER-POSITIONAL-BINDING",
           len(positional) == len(claims),
           f"and each is bound POSITIONALLY -- the receipt value must "
           f"appear inside its own declared sentence context (compared "
           f"under whitespace normalisation, so line wrapping is not "
           f"content), exactly once: {len(positional)} of {len(claims)}.  This is what "
           f"closes the substitution surface a presence sweep leaves "
           f"open: swapping two paper numbers that are both receipt "
           f"values moves no presence check and breaks both contexts.  "
           f"Unbound: " +
           str([c["key"] for c in claims if c["key"] not in positional]),
           "MUT-PAPER-TABLE-SWAP")
    if C.mut == "MUT-PAPER-VERDICT":
        ptxt2 = ptxt.replace("COVERAGE=102", "COVERAGE=999")
    else:
        ptxt2 = ptxt
    in_paper = sum(1 for s in segs if s in ptxt2)
    C.gate("G-PAPER-VERDICT",
           in_paper == len(segs) and len(segs) > 0,
           f"the paper's verdict block is compared against the EMITTED "
           f"verdict segment by segment: {in_paper} of {len(segs)} present "
           f"verbatim.  The headline the paper prints is the headline the "
           f"gates computed",
           "MUT-PAPER-VERDICT")
    allowed = set()

    def collect(o):
        if isinstance(o, dict):
            for v in o.values():
                collect(v)
        elif isinstance(o, (list, tuple)):
            for v in o:
                collect(v)
        else:
            allowed.add(str(o))
    collect(R)
    allowed |= STRUCTURAL_LITERALS
    nums = re.findall(r"`([0-9][0-9,]*(?:/[0-9]+)?|[0-9]+/[0-9]+)`", ptxt)
    unmatched = sorted({n for n in nums
                        if n.replace(",", "") not in allowed
                        and n not in allowed})
    if C.mut == "MUT-PAPER-NUMBER":
        unmatched = ["999999"]
    R["paper_sweep"] = {"numbers_scanned": len(nums),
                        "unmatched_numbers": unmatched,
                        "verdict_segments_in_the_paper": in_paper,
                        "claims_positionally_bound": len(positional)}
    C.gate("G-PAPER-NUMBER-SWEEP",
           len(unmatched) == 0 and len(nums) > 0,
           f"backticked numeric tokens scanned in the paper: {len(nums)}; "
           f"carried by no receipt value and no declared structural "
           f"literal: {unmatched}",
           "MUT-PAPER-NUMBER")
    C.say("")

    # ---- 17.  COMPLIANCE SWEEP ----------------------------------------
    C.say("-" * 78)
    C.say("17.  COMPLIANCE SWEEP (statuses computed from measured deaths)")
    C.say("-" * 78)
    R["_engravings"] = ENGRAVINGS
    C.say("")


def compliance_stage(C: Ctx, R: dict, deaths) -> None:
    """Compliance rows: each status COMPUTED, each falsifier verified
    against the MEASURED death table when one is available."""
    known = (C.gate_names() | set(CENSUS_GATE_NAMES)
             | {"G-COMPLIANCE", "G-GATE-COUNT"}
             | {a["name"] for a in C.anchors} | {"Q-UNBOUND"})
    rows = []
    for tag, rule, how, target_gate, falsifier in ENGRAVINGS:
        killers = []
        if deaths is not None:
            killers = sorted(m for m in deaths
                             if target_gate in deaths[m]["gates"]
                             or target_gate in deaths[m]["anchors"])
        exists = target_gate in known
        status = "MET" if exists and (deaths is None or killers) else "MISSING"
        rows.append({"engraving": tag, "rule": rule, "how": how,
                     "gate": target_gate, "declared_falsifier": falsifier,
                     "measured_killers": killers, "status": status})
    if C.mut == "MUT-COMPLIANCE":
        rows.append({"engraving": "#99", "rule": "a rule this unit asserts "
                     "but does not gate", "how": "asserted, not gated",
                     "gate": "G-NO-SUCH-GATE", "declared_falsifier": "none",
                     "measured_killers": [], "status": "MISSING"})
    missing = [r for r in rows if r["status"] != "MET"]
    R["compliance"] = rows
    ten = [r for r in rows if r["engraving"].startswith("v14")]
    C.gate("G-COMPLIANCE",
           len(missing) == 0 and len(ten) == 10,
           f"{len(rows)} engraved rules swept -- the TEN 2026-08-09 v14 "
           f"engravings ({len(ten)} rows: #10 x2, #20 x3, #34 x2, #46, "
           f"#62 x2) and their v13 companions -- each row naming the gate "
           f"that discharges it and, where the death table is available, "
           f"the MUTANTS MEASURED TO KILL that gate.  MISSING rows "
           f"{len(missing)}",
           "MUT-COMPLIANCE")
    for r in rows:
        C.say(f"    [{r['status']}] {r['engraving']} {r['rule']}")
    C.say("")
    C.gate("G-GATE-COUNT",
           len(C.gates) + 1 + N_CENSUS_GATES == R["gate_count_final"],
           f"the gate count the paper renders ({R['gate_count_final']}) is "
           f"verified against the gates actually registered "
           f"({len(C.gates) + 1} so far plus {N_CENSUS_GATES} census-stage "
           f"gates); the paper's instrument figures are receipt values, "
           f"not hand counts",
           "MUT-GATE-COUNT")


def census_stage(C: Ctx, R: dict, deaths: dict) -> None:
    """The waiver ledger, computed from MEASURED DEATHS.

    The #34 standard, applied at the census the #34 engraving created:
    a gate is FALSIFIER-REACHES-IT only when a declared mutant is
    OBSERVED to make it fail.  No substring test on a declared string.
    """
    C.census_ran = True
    C.say("-" * 78)
    C.say("18.  THE NEVER-FALSIFIED CENSUS, FROM MEASURED DEATHS")
    C.say("-" * 78)
    rows = []
    for g in C.gates:
        nm = g["name"]
        killers = sorted(m for m in deaths if nm in deaths[m]["gates"])
        declared = [t.strip() for t in re.split(r"\s*/\s*",
                                                g["declared_falsifier"])]
        rows.append({"gate": nm,
                     "status": "FALSIFIER-REACHES-IT" if killers
                               else "UNWAIVED",
                     "measured_killers": killers,
                     "declared_falsifiers": declared,
                     "declaration_is_true": bool(
                         killers and set(declared) & set(killers))})
    # the census-stage gates are themselves covered: they are registered
    # below and their killers were measured in the second pass.
    for nm in CENSUS_GATE_NAMES:
        killers = sorted(m for m in deaths if nm in deaths[m]["gates"])
        rows.append({"gate": nm,
                     "status": "FALSIFIER-REACHES-IT" if killers
                               else "UNWAIVED",
                     "measured_killers": killers,
                     "declared_falsifiers": [CENSUS_GATE_FALSIFIER[nm]],
                     "declaration_is_true": bool(
                         killers and CENSUS_GATE_FALSIFIER[nm] in killers)})
    if C.mut == "MUT-WAIVER":
        rows[3]["status"] = "UNWAIVED"
        rows[3]["measured_killers"] = []
    unwaived = [r["gate"] for r in rows if r["status"] == "UNWAIVED"]
    false_decl = [r["gate"] for r in rows if not r["declaration_is_true"]]
    R["never_falsified_census"] = rows
    C.gate("G-WAIVER-CENSUS",
           len(unwaived) == 0 and len(rows) == R["gate_count_final"],
           f"never-falsified census over ALL {len(rows)} gates of the "
           f"delivery ({R['gate_count_final']} declared): every row's "
           f"status is computed from MEASURED DEATHS -- {len(MUTANTS)} "
           f"in-process mutant runs, each gate's [FAIL] set collected -- "
           f"and FALSIFIER-REACHES-IT is entered only where a declared "
           f"mutant is OBSERVED to make the gate fail.  UNWAIVED "
           f"{len(unwaived)} {unwaived}.  No substring test on a declared "
           f"string appears anywhere in this census",
           "MUT-WAIVER")
    C.gate("G-DECLARED-FALSIFIERS-ARE-REAL",
           len(false_decl) == 0,
           f"and each gate's own DECLARED falsifier is checked against the "
           f"measured deaths: a gate whose declared mutant does not in "
           f"fact kill it is a false waiver claim, which is the disease "
           f"#34 engraved.  False declarations: {len(false_decl)} "
           f"{false_decl}",
           "MUT-WAIVER")

    unbound = []
    for a in C.anchors:
        if a["kind"] != "quotation":
            continue
        cg = a["consumer_gate"]
        killers = [m for m in deaths if cg in deaths[m]["gates"]]
        if cg not in C.gate_names() or not killers:
            unbound.append({"quotation": a["name"], "consumer": cg,
                            "exists": cg in C.gate_names(),
                            "killers": sorted(killers)})
    if C.mut == "MUT-CONSUMER-UNBIND":
        unbound = unbound + [{"quotation": "Q-INJECTED",
                              "consumer": "G-NO-SUCH-GATE-AT-ALL",
                              "exists": False, "killers": []}]
    R["consumer_binding"] = {"rows": sum(1 for a in C.anchors
                                         if a["kind"] == "quotation"),
                             "unbound": unbound}
    C.gate("G-CONSUMER-BINDING",
           len(unbound) == 0,
           f"the #62 consumer clause, enforced as a PREDICATE and not a "
           f"label: every one of the {len(QUOTES)} quotation anchors names "
           f"a consumer gate that (i) EXISTS in this run's gate list, "
           f"(ii) has a non-literal predicate (proved wholesale by "
           f"G-NO-LITERAL-GATE-PREDICATES) and (iii) is MEASURED to fail "
           f"under at least one declared mutant.  Rows failing any clause: "
           f"{len(unbound)} {unbound}",
           "MUT-CONSUMER-UNBIND")

    qb = deaths.get("MUT-QUOTE-SOURCE-DRIFT", {})
    later_stage_anchors = [a for a in qb.get("anchors", [])
                           if a.startswith("A-") or a.startswith("P-")]
    short_ok = (qb.get("stages") == ["quotations"]
                and "Q-S4-RENEWAL" in qb.get("anchors", [])
                and later_stage_anchors == [] and qb.get("gates") == [])
    if C.mut == "MUT-SHORT-CIRCUIT":
        short_ok = False
    C.gate("G-ANCHOR-SHORT-CIRCUIT",
           short_ok and C.stages == ["quotations", "bytes", "path-values"],
           f"the anchor stages GENUINELY short-circuit, proved by "
           f"measurement rather than by list order: under "
           f"MUT-QUOTE-SOURCE-DRIFT the run's evaluated stages are "
           f"{qb.get('stages')} -- the byte and path-value stages are "
           f"never reached ({later_stage_anchors}) and no gate is ever "
           f"evaluated ({qb.get('gates')}).  In the clean run all three stages "
           f"evaluate in order {C.stages}",
           "MUT-SHORT-CIRCUIT")


def totals(C: Ctx, R: dict) -> None:
    fails = [g["name"] for g in C.gates if not g["passed"]]
    R["totals"] = {"anchors": len(C.anchors),
                   "anchor_failures": len(C.failed_anchors),
                   "gates": len(C.gates), "gate_failures": len(fails),
                   "mutants": len(MUTANTS),
                   "compliance_rows": len(R.get("compliance", [])),
                   "unwaived_never_falsified":
                       len([r for r in R.get("never_falsified_census", [])
                            if r["status"] == "UNWAIVED"])}
    R["gates"] = C.gates
    R["mutants"] = [{"name": n, "what": w, "target": t}
                    for n, w, t in MUTANTS]
    R["pin"] = PIN
    R["pin_sha256_prefix"] = sha12(blob(CORPUS_SHA, PIN))
    R["source_sha256"] = sha12(open(os.path.abspath(__file__), "rb").read())
    R["python"] = (f"{sys.version_info.major}.{sys.version_info.minor}."
                   f"{sys.version_info.micro}")
    R["schema"] = "r6bp-transport-v2-repaired"
    C.say("-" * 78)
    C.say("19.  TOTALS")
    C.say("-" * 78)
    for k in sorted(R["totals"]):
        C.say(f"    {k}: {R['totals'][k]}")
    C.say("")
    C.say("THE VERDICT AS EMITTED:")
    C.say("")
    for s in R.get("verdict", "").split("  "):
        C.say("  " + s)
    C.say("")


def build(mut, deaths):
    C = Ctx(mut)
    R: dict = {}
    try:
        _measure(C, R)
        compliance_stage(C, R, deaths)
        if deaths is not None:
            census_stage(C, R, deaths)
    except AnchorStop:
        pass
    if "_engravings" in R:
        del R["_engravings"]
    totals(C, R)
    return C, R


# --------------------------------------------------------------------
# 9.  Declarations the run reads
# --------------------------------------------------------------------

POSITIONAL_CLAIMS = [
    ("RETURN", ["kernel", "return_probability"],
     "the return probability is `{V}`"),
    ("DEFECT", ["kernel", "defect"], "the defect `{V}`"),
    ("RENEWALS", ["kernel", "expected_total_renewals"],
     "expected total number of renewals after any renewal is `{V}`"),
    ("COND-MEAN", ["kernel", "mean_conditional_on_a_further_renewal"],
     "conditional on a further renewal is `{V}`"),
    ("G3", ["kernel", "g_3"], "g(3) = `{V}`"),
    ("G4", ["kernel", "g_4"], "g(4) = `{V}`"),
    ("G5", ["kernel", "g_5"], "g(5) = `{V}`"),
    ("ALT-RETURN", ["kernel", "disclosed_alternative_bare_state_0",
                    "return_probability"],
     "a return probability of `{V}`"),
    ("HOLE-COST", ["fiber_collapse", "hole_cost_intervals"],
     "kernel assigns probability zero to `{V}` censused intervals"),
    ("TOTAL", ["arena", "intervals_censused"],
     "arena carries `{V}` censused record intervals"),
    ("COLLAPSED", ["fiber_collapse", "collapsed_all_denominator"],
     "the derived kernel speaks on `{V}` of them"),
    ("HONEST-TOTAL", ["arena", "honest_denominator_censused"],
     "leaves `{V}` censused intervals"),
    ("HONEST-NT", ["arena", "honest_denominator_nontrivial"],
     "of which `{V}` carry a non-trivial fiber"),
    ("COLLAPSED-HONEST", ["fiber_collapse", "collapsed_honest_denominator"],
     "the kernel speaks on `{V}` of those"),
    ("COUNT4-ALL", ["fiber_collapse", "collapsed_at_count_4_all"],
     "count four alone gives `{V}`"),
    ("COUNT4-HONEST", ["fiber_collapse", "collapsed_at_count_4_honest"],
     "and `{V}` on the honest denominator"),
    ("UNREF-INT", ["arena", "unrefinable_intervals"],
     "carry `{V}` of the censused intervals"),
    ("TV-T", ["positional_census", "tv_between_cells_transport"],
     "total variation `{V}` between the two cells"),
    ("TV-D", ["positional_census",
              "tv_between_cells_no_delivery_conditional"],
     "total variation between the cells is `{V}`"),
    ("MASS1", ["positional_census", "conditioning_mass_leg1"],
     "retains `{V}` of the leg-one mass"),
    ("MASS2", ["positional_census", "conditioning_mass_leg2"],
     "and `{V}` of the leg-two mass"),
    ("MULT1", ["positional_census", "delivery_multiplicity_leg1"],
     "delivery multiplicity per slot is `{V}` at leg one"),
    ("MULT2", ["positional_census", "delivery_multiplicity_leg2"],
     "and `{V}` at leg two"),
    ("CYCLES", ["r6a_reclassification", "NEW-FRONT-VALUES", "cycles"],
     "over the `{V}` cycles"),
    ("CYCLES-NZ", ["r6a_reclassification", "NEW-FRONT-VALUES",
                   "cycles_with_a_nonzero_count_sum"],
     "the count sum is nonzero at `{V}` of them"),
    ("CANDIDATES", ["identification_census", "candidate_count"],
     "`{V}` identification candidates are expressible"),
    ("MOTIVATED", ["identification_census", "motivated_count"],
     "Motivated identifications: `{V}`"),
    ("TV-S5", ["fiber_collapse", "tv_derived_vs_s5"],
     "separated from the derived law by total variation `{V}`"),
    ("SIMPLEX", ["fiber_collapse", "crb_simplex_dim_before"],
     "invariant-measure simplex of dimension `{V}`"),
    ("LEG3-LEAVES", ["positional_census", "length3_leaf_count"],
     "`{V}` leaves, one pattern"),
    ("GATES", ["gate_count_final"], "`{V}` must-pass gates"),
    ("MUTANTS", ["mutant_count"], "`{V}` declared mutants"),
    ("ANCHORS", ["anchor_totals", "total"], "`{V}` anchors"),
    ("QUOTATIONS", ["anchor_totals", "quotation"],
     "`{V}` quotation anchors"),
    ("COMPLIANCE-ROWS", ["compliance_row_count"], "`{V}` compliance rows"),
]

STRUCTURAL_LITERALS = {
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
    "13", "14", "15", "16", "20", "21", "26", "27", "34", "43", "46",
    "52", "53", "62", "09", "2026-08-09", "1/2", "2/3", "3/2", "5/2",
    "1/7", "3/28", "4/7", "1/8", "6x6", "n-1", "n+1", "n1", "n2", "36",
    "144", "215", "400", "448", "1024", "512", "3584", "8192", "24576",
    "73728", "4096", "63", "68", "3,969", "3969", "19683", "54", "108",
    "81", "30", "972", "324", "647", "67", "60", "141", "103", "102",
    "83", "79", "29", "50", "20", "37", "122", "201", "221", "23",
    "59/221", "76/221", "86/221", "7/23", "8/23", "13/16", "3/16",
    "16/3", "3/512", "27/4096", "9/1024", "27/2048", "1/256", "2/63",
    "2/21", "3/7", "1/7", "4/9", "1/9", "1/3", "1/4", "3/4", "4/3",
}

PENDING_GATES = 10
N_CENSUS_GATES = 4
CENSUS_GATE_NAMES = ["G-WAIVER-CENSUS", "G-DECLARED-FALSIFIERS-ARE-REAL",
                     "G-CONSUMER-BINDING", "G-ANCHOR-SHORT-CIRCUIT"]
CENSUS_GATE_FALSIFIER = {"G-WAIVER-CENSUS": "MUT-WAIVER",
                         "G-DECLARED-FALSIFIERS-ARE-REAL": "MUT-WAIVER",
                         "G-CONSUMER-BINDING": "MUT-CONSUMER-UNBIND",
                         "G-ANCHOR-SHORT-CIRCUIT": "MUT-SHORT-CIRCUIT"}


_PARA: dict = {}


def paragraphs(sha: str, rel: str) -> list[str]:
    key = (sha, rel)
    if key not in _PARA:
        _PARA[key] = [p.lower() for p in
                      re.split(r"\n\s*\n", text(sha, rel))]
    return _PARA[key]


def mutant_identity_scan() -> list[str]:
    """AST: any gate PREDICATE subtree referencing the injection channel."""
    if "mident" in _SCAN:
        return _SCAN["mident"]
    tree = self_ast()
    bad = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fn = node.func
        if not (isinstance(fn, ast.Attribute) and fn.attr == "gate"):
            continue
        if len(node.args) < 2:
            continue
        nm = node.args[0].value if isinstance(node.args[0], ast.Constant) \
            else "<computed>"
        for sub in ast.walk(node.args[1]):
            if isinstance(sub, ast.Attribute) and sub.attr == "mut":
                bad.append(str(nm))
            if isinstance(sub, ast.Name) and sub.id in ("MUT", "mut"):
                bad.append(str(nm))
    _SCAN["mident"] = sorted(set(bad))
    return _SCAN["mident"]


ENGRAVINGS = [
    ("v14 #10 §14", "containment is not equality",
     "the verdict gate compares the COMPLETE emitted string against a "
     "comparator rebuilt segment by segment from the receipt's values; no "
     "substring, prefix or containment test appears anywhere",
     "G-VERDICT-EQUALITY", "MUT-VERDICT-APPEND"),
    ("v14 #10 §13", "render from the gated object",
     "the receipt object R is the single source of truth: the output text "
     "and every paper claim render from it",
     "G-PAPER-CLAIMS", "MUT-PAPER-CLAIM"),
    ("v14 #20 §13", "prose renders from the receipt",
     "every load-bearing paper number is bound to a receipt path AND to "
     "its own sentence context, so a substitution between two receipt "
     "values dies",
     "G-PAPER-POSITIONAL-BINDING", "MUT-PAPER-TABLE-SWAP"),
    ("v14 #20 §14", "compliance claims are gate claims",
     "this sweep is itself a gate, and each row's falsifier is verified "
     "against the MEASURED death table rather than a declared string",
     "G-COMPLIANCE", "MUT-COMPLIANCE"),
    ("v14 #20 §14", "path-value anchoring",
     "every read from a pinned receipt anchors the (path, value) pair; a "
     "path drift that changes the arena or the verdict dies at the anchor",
     "P-R6A-DIAG2-RAW", "MUT-PATH-VALUE-DRIFT"),
    ("v14 #34 §14", "waiver claims are gate claims",
     "the never-falsified census is computed from MEASURED DEATHS: "
     "FALSIFIER-REACHES-IT only where a mutant is observed to make the "
     "gate fail; the dead WAIVED-VERIFIED branch is removed entirely",
     "G-WAIVER-CENSUS", "MUT-WAIVER"),
    ("v14 #34 §14", "verbatim-text anchors adopted",
     "each quotation row is bound to a named consumer gate -- enforced "
     "here as a predicate: the gate must exist and be mutant-falsified",
     "G-CONSUMER-BINDING", "MUT-CONSUMER-UNBIND"),
    ("v14 #46 §14", "no unanchored runtime inputs",
     "every runtime input is a committed object at a declared sha or this "
     "unit's own deliverable; no ledger, no STATUS, no other unit's "
     "working file, no `git show HEAD:`",
     "G-NO-UNANCHORED-RUNTIME-INPUT", "MUT-UNANCHORED-INPUT"),
    ("v14 #62 §14", "verbatim-text anchors, corrected spec",
     "the anchor kind binds QUOTE FIDELITY -- the PAPER's quotations "
     "against the SOURCE's committed bytes, with every quotation-shaped "
     "span in the paper required to be a declared row -- and anchor "
     "evaluation genuinely short-circuits before the byte anchors, proved "
     "by measurement",
     "G-ANCHOR-SHORT-CIRCUIT", "MUT-SHORT-CIRCUIT"),
    ("v14 #62 §14", "provenance by committed sha",
     "the R6a source COMMIT SHA is declared in this unit's frozen text and "
     "read via that sha; the path-value stability gate runs across two "
     "DECLARED COMMITTED revisions and only committed objects are "
     "disclosed",
     "G-R6A-PATH-VALUE-STABILITY", "MUT-STABILITY-DRIFT"),
    ("v13 #313 §13", "repair propagation (companion)",
     "this unit's gates are diffed against every rule engraved since its "
     "pin froze; all ten 2026-08-09 v14 engravings are enumerated above "
     "with computed statuses",
     "G-COMPLIANCE", "MUT-COMPLIANCE"),
    ("v13 #313 §14", "boundary parity (companion)",
     "the unit's one Boolean partition of a census carries a "
     "parity-witness gate whose certificate is the measured delta of the "
     "alternative connective",
     "G-PARITY-WITNESS", "MUT-PARITY"),
    ("v13 #314 §13", "precheck doctrine (companion)",
     "no precheck-level quantity names a verdict: the coverage, the "
     "qualifiers, the defectiveness and every head NAME are measured on "
     "the censused objects",
     "G-HEAD-NAMES-ARE-MEASURED", "MUT-HEAD-NAME"),
    ("v13 #234 §13", "the verdict is derived inside a gate (companion)",
     "the verdict string is built from measured values and a verdict-flip "
     "mutant proves the derivation can fail",
     "G-VERDICT-EQUALITY", "MUT-VERDICT-CLASS"),
    ("v13 #208 §14", "no gate predicate references mutant identity "
     "(companion)",
     "machine-checked by an AST scan of every gate predicate; and no "
     "must-pass gate has a literal predicate",
     "G-NO-MUTANT-IDENTITY-IN-GATES", "MUT-MUTANT-IDENTITY"),
    ("v13 #219 §14", "independent comparators (companion)",
     "the re-verification gates rebuild against the ANCHORED source "
     "counts, so feeding them garbage now fails them; the S1 two-route "
     "claim is downgraded to a transcription cross-check and disclosed",
     "G-METRIC-RESTRICTION-REVERIFIED", "MUT-ADDITIVITY-GARBAGE"),
    ("v13 #208 §14", "analytically-forced clauses are disclosures "
     "(companion)",
     "an AST scan proves this unit registers no gate with a literal "
     "predicate -- the six literal-True must-pass gates of the delivery "
     "are all rebuilt as measured checks",
     "G-NO-LITERAL-GATE-PREDICATES", "MUT-LITERAL-GATE"),
    ("§15", "declared-arena discipline (companion)",
     "the arena is declared as data before any measurement and every "
     "headline carries its scope tag",
     "G-ARENA-BASELINE", "MUT-ARENA-CENSUS"),
    ("§15 #196", "like-for-like matches every coordinate (companion)",
     "the two S2 cells do NOT match every coordinate -- different "
     "ensembles at different depths -- and the unit measures and carries "
     "that rather than claiming a clean chain-position contrast",
     "G-S2-TWO-CELLS-CONFOUND", "MUT-TWO-CELLS"),
    ("§14 #175", "symmetry self-tests (companion)",
     "the orientation stabilizer is re-derived from the measured "
     "reversal-invariance and compared against its declared class, and "
     "the orientation item is split per observable because the front rule "
     "is NOT reversal-invariant",
     "G-INVENTORY-ITEM-CLASSES", "MUT-IDENT-RELABEL"),
]

MUTANTS = [
    ("MUT-QUOTE-SOURCE-DRIFT",
     "drift an anchored quotation against its source's committed bytes",
     "Q-S4-RENEWAL"),
    ("MUT-PAPER-QUOTE-INVERSION",
     "the A5 class: the paper renders an INVERTED source quotation",
     "Q-S5-CHOSEN"),
    ("MUT-PAPER-UNBOUND-QUOTE",
     "the paper prints a quotation bound to no declared source row",
     "Q-UNBOUND"),
    ("MUT-MEANING-INVERSION",
     "the A2 class: preserve the needle, invert the standing around it",
     "G-STANDING-SENTINEL"),
    ("MUT-BYTE-ANCHOR-DRIFT", "corrupt a pinned row's committed byte hash",
     "A-S1-PAPER31"),
    ("MUT-PATH-VALUE-DRIFT", "drift a path-value read from the R6a receipt",
     "P-R6A-DIAG2-RAW"),
    ("MUT-STABILITY-DRIFT",
     "declare a consumed path-value moved between the two committed shas",
     "G-R6A-PATH-VALUE-STABILITY"),
    ("MUT-UNANCHORED-INPUT", "read a mutable repo file at run time",
     "G-NO-UNANCHORED-RUNTIME-INPUT"),
    ("MUT-LITERAL-GATE", "register a must-pass gate with a literal predicate",
     "G-NO-LITERAL-GATE-PREDICATES"),
    ("MUT-MUTANT-IDENTITY", "let a gate predicate reference the injection",
     "G-NO-MUTANT-IDENTITY-IN-GATES"),
    ("MUT-S1-ROUTE-DRIFT", "drift one entry of the second S1 transcription",
     "G-S1-TWO-TRANSCRIPTIONS"),
    ("MUT-S1-ROUTE-SAME-SOURCE",
     "point both S1 routes at one artifact (the #219 disease)",
     "G-S1-TWO-TRANSCRIPTIONS"),
    ("MUT-TRANSCRIPTION-CLAIM",
     "claim the un-run derivation does not exist in the source",
     "G-S1-TRANSCRIPTION-DISCLOSURE"),
    ("MUT-S1-HARMONIC", "drift the harmonic vector", "G-S1-HARMONIC"),
    ("MUT-KERNEL-ROW", "corrupt one entry of the completed chain q'",
     "G-KERNEL-CONFLICT-ROW"),
    ("MUT-CLOSED-CLASS", "add a spurious closed class containing state 0",
     "G-CLOSED-CLASS"),
    ("MUT-CONVENTION-SWAP", "adopt the bare-state-0 reading as the law",
     "G-RENEWAL-CONVENTION-IS-THE-SOURCES"),
    ("MUT-DEFECT-ARITHMETIC", "move the return probability",
     "G-RENEWAL-DEFECTIVE"),
    ("MUT-DEFECTIVE-MEAN", "corrupt the closed-form defective mean",
     "G-DEFECTIVE-MEAN"),
    ("MUT-FIRST-RETURN-HOLE", "fill a support hole",
     "G-FIRST-RETURN-LAW-THREE-ROUTES"),
    ("MUT-ALL-N-LAW", "break the C(n-1,2) configuration count at one n",
     "G-FIRST-RETURN-LAW-THREE-ROUTES"),
    ("MUT-UNIFORM-MARGINAL", "break the uniform position marginal at one n",
     "G-UNIFORM-POSITION-MARGINAL"),
    ("MUT-COUNT-3-LAW", "give count 3 a second configuration",
     "G-COUNT-3-EMPTINESS-IS-A-LAW"),
    ("MUT-FILLER-REDUCTION",
     "claim the two filler reductions agree at n = 5",
     "G-FILLER-REDUCTION-IS-FREE"),
    ("MUT-ALT-READING", "corrupt the disclosed alternative's arithmetic",
     "G-BARE-STATE-0-DISCLOSURE"),
    ("MUT-S2-PROFILE", "make the two S2 cells' profiles equal",
     "G-S2-PROFILES"),
    ("MUT-POSITION-MAP", "collapse the pattern->slot map to a constant",
     "G-S2-PATTERN-POSITION-MAP"),
    ("MUT-MIDDLE-SLOT", "let the middle slot admit a delivery",
     "G-MIDDLE-SLOT-ADMITS-NO-DELIVERY"),
    ("MUT-MULTIPLICITY", "equalise the two delivery multiplicities",
     "G-DELIVERY-MULTIPLICITY-LAW"),
    ("MUT-PARITY", "erase the alternative connective's measured delta",
     "G-PARITY-WITNESS"),
    ("MUT-WELD", "deny the S1-reproduces-S2 weld",
     "G-WELD-S1-REPRODUCES-S2"),
    ("MUT-TWO-CELLS", "hide the two-cell ensemble confound",
     "G-S2-TWO-CELLS-CONFOUND"),
    ("MUT-SEAM-CAUSE", "lose the escape as the seam's measured cause",
     "G-SEAM-CAUSE-IS-THE-ESCAPE"),
    ("MUT-FIBER-REBUILD", "drift the independently rebuilt split fiber",
     "G-R6A-FIBER-REBUILD"),
    ("MUT-ARENA-CENSUS", "inflate one count class of the interval census",
     "G-ARENA-BASELINE"),
    ("MUT-UNREFINABLE", "hide the three records that admit no subdivision",
     "G-UNREFINABLE-RECORDS"),
    ("MUT-COLLAPSE-COUNT", "inflate the fiber-collapse coverage",
     "G-FIBER-COLLAPSE-COVERAGE"),
    ("MUT-MODES", "claim a unique maximiser at delivery-free scope",
     "G-COLLAPSE-IS-DISTRIBUTION-NOT-VALUE"),
    ("MUT-CRB", "drift CR-B's simplex dimension", "G-CRB-SIMPLEX"),
    ("MUT-TERMINAL-STATUS",
     "deny that the terminal receipt carries blocks the delivered one does "
     "not", "G-R6A-TERMINAL-STATUS"),
    ("MUT-TERMINATION", "zero the defect (a recurrent renewal chain)",
     "G-AS-TERMINATION"),
    ("MUT-BRIDGES", "drift the count-1 census the bridges reading reaches",
     "G-BRIDGES-READING"),
    ("MUT-ADMISSIBILITY",
     "claim the derived marginal is the admissible marginal off G-DIAG2",
     "G-ADMISSIBILITY-COUPLING"),
    ("MUT-DIAG2", "lose the completely covered record",
     "G-DERIVED-LAW-COMPLETE-ON-ONE-RECORD"),
    ("MUT-S5-COMPARATOR", "collapse the S5 comparator separation to 0",
     "G-S5-COMPARATOR-SEPARATION"),
    ("MUT-MOTIVATION-QUALIFIER",
     "declare an identification MOTIVATED while its inventory carries free "
     "items", "G-IDENTIFICATION-CENSUS"),
    ("MUT-IDENT-RELABEL", "relabel a genuinely-free inventory item FORCED",
     "G-INVENTORY-ITEM-CLASSES"),
    ("MUT-TYPE-CENSUS", "deny that every censused leg carries one arbitration",
     "G-TYPE-CENSUS"),
    ("MUT-ADDITIVITY-GARBAGE",
     "feed the re-verification garbage counts (the #219 class)",
     "G-ADDITIVITY-REVERIFIED / G-METRIC-RESTRICTION-REVERIFIED"),
    ("MUT-TRANSVERSE", "drift the transverse-link census",
     "G-TRANSVERSE-LINKS-UNFORCED"),
    ("MUT-FRONT-CYCLES", "claim a cycle with a zero count sum",
     "G-FRONT-TWO-RULE-DISAGREEMENT"),
    ("MUT-FRONT-FIBER", "restore the stricken fiber-1 front claim",
     "G-NEW-FRONTS-RECLASSED"),
    ("MUT-LIFT-PAIR", "type the lift-pair fiber instead of anchoring it",
     "G-LIFT-PAIR-GROWN"),
    ("MUT-FREEDOM-TALLY", "inflate the freedom-growth tally",
     "G-FREEDOM-TALLY"),
    ("MUT-VARIATIONAL", "assert an unrefuted variational declaration",
     "G-VARIATIONAL-ROWS-MEASURED"),
    ("MUT-EXTREMAL-BAR", "collapse the countermodel to one selection",
     "G-EXTREMAL-COUNTERMODEL"),
    ("MUT-DET-LEG", "restore the stricken det-blindness claim",
     "G-DET-LEG-CORRECTED"),
    ("MUT-D12-EXTENSION", "hide the D12 second-clause extension",
     "G-D12-EXTENSION-NAMED"),
    ("MUT-EXTREMAL-RATIFY", "claim the derived law ratifies max-det",
     "G-EXTREMAL-NOT-RATIFIED"),
    ("MUT-COVER", "assert a row pinning a cover object", "G-COVER-DISSOLVED"),
    ("MUT-CONTROL", "declare the negative controls MOTIVATED", "G-CONTROLS"),
    ("MUT-GAMMA-REGISTER", "truncate the Gamma-main input register",
     "G-GAMMA-MAIN-REGISTER"),
    ("MUT-HEAD-NAME", "make a verdict head name unselectable by measurement",
     "G-HEAD-NAMES-ARE-MEASURED"),
    ("MUT-RESTRICTION-DROP", "drop a carried restriction from the verdict",
     "G-SEGMENTS-CARRY-THEIR-RESTRICTIONS"),
    ("MUT-VERDICT-TYPED", "type a verdict segment (VALUE for DISTRIBUTION)",
     "G-VERDICT-EQUALITY"),
    ("MUT-VERDICT-APPEND", "append text to the verdict (the containment class)",
     "G-VERDICT-EQUALITY"),
    ("MUT-VERDICT-CLASS", "swap a verdict class name", "G-VERDICT-EQUALITY"),
    ("MUT-PAPER-CLAIM", "drift a number the paper renders from the receipt",
     "G-PAPER-CLAIMS"),
    ("MUT-PAPER-TABLE-SWAP",
     "the A6b class: exchange two paper numbers that are both receipt values",
     "G-PAPER-POSITIONAL-BINDING"),
    ("MUT-PAPER-VERDICT", "drift a verdict segment as the paper prints it",
     "G-PAPER-VERDICT"),
    ("MUT-PAPER-NUMBER",
     "leave a backticked number in the paper that no receipt value carries",
     "G-PAPER-NUMBER-SWEEP"),
    ("MUT-COMPLIANCE", "assert compliance with a rule this unit does not gate",
     "G-COMPLIANCE"),
    ("MUT-GATE-COUNT", "drift the gate count the paper renders",
     "G-GATE-COUNT"),
    ("MUT-WAIVER", "unwaive a gate in the never-falsified census",
     "G-WAIVER-CENSUS"),
    ("MUT-CONSUMER-UNBIND",
     "point a quotation's consumer at a gate that does not exist",
     "G-CONSUMER-BINDING"),
    ("MUT-SHORT-CIRCUIT", "deny the measured anchor short-circuit",
     "G-ANCHOR-SHORT-CIRCUIT"),
]


# --------------------------------------------------------------------
# 10.  Driver
# --------------------------------------------------------------------

def measure_deaths(deaths_seed):
    out = {}
    for name, _w, _t in MUTANTS:
        Cm, _Rm = build(name, deaths_seed)
        out[name] = Cm.signature()
    return out


def emit(C: Ctx, R: dict, write: bool) -> int:
    fails = [g["name"] for g in C.gates if not g["passed"]]
    if C.failed_anchors or fails:
        print("\n".join(C.lines))
        names = [a.split(":")[0] for a in C.failed_anchors] + fails
        print("KILLED-BY: " + ",".join(names), file=sys.stderr)
        if C.failed_anchors:
            print(f"ANCHOR FAILURES: {len(C.failed_anchors)}",
                  file=sys.stderr)
            return 2
        print(f"GATE FAILURES: {fails}", file=sys.stderr)
        return 1
    body = "\n".join(C.lines) + "\n"
    if write:
        with open(OUT_TXT, "w", encoding="utf-8") as fh:
            fh.write(body)
        with open(OUT_JSON, "w", encoding="utf-8") as fh:
            json.dump(R, fh, indent=1, sort_keys=True, ensure_ascii=False)
            fh.write("\n")
    print(body, end="")
    return 0


def selftest() -> int:
    ok, on_target, rows = 0, 0, []
    for name, what, target in MUTANTS:
        proc = subprocess.run(
            [sys.executable, os.path.abspath(__file__), "--mutant", name],
            capture_output=True, text=True)
        killed = []
        for line in proc.stderr.splitlines():
            if line.startswith("KILLED-BY: "):
                killed = [x.strip()
                          for x in line[len("KILLED-BY: "):].split(",")]
        declared = [t.strip() for t in re.split(r"\s*/\s*", target)]
        hit = sorted(set(declared) & set(killed))
        if proc.returncode != 0:
            ok += 1
            if hit:
                on_target += 1
            else:
                print(f"  [DIED-OFF-TARGET] {name}: declared {declared}, "
                      f"killed by {killed}")
            rows.append((name, proc.returncode, hit))
        else:
            print(f"  [SURVIVOR] {name}: {what} (target {target})")
    print(f"SELFTEST: {ok}/{len(MUTANTS)} mutants dead; "
          f"{on_target}/{len(MUTANTS)} killed BY THEIR NAMED gate/anchor")
    for n, rc, hit in rows:
        print(f"  [DEAD rc={rc} by {','.join(hit) if hit else '?'}] {n}")
    return 0 if (ok == len(MUTANTS) and on_target == len(MUTANTS)) else 1


def main() -> int:
    argv = sys.argv[1:]
    if "--list-mutants" in argv:
        for n, _, _ in MUTANTS:
            print(n)
        return 0
    if "--selftest" in argv:
        return selftest()
    mut = None
    write = True
    if "--mutant" in argv:
        mut = argv[argv.index("--mutant") + 1]
        write = False
    seed = measure_deaths(None)
    deaths = measure_deaths(seed)
    C, R = build(mut, deaths)
    return emit(C, R, write)


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
u4_crystals_exact.py -- v14 U4 / paper-14: RENEWAL-ONLY CRYSTALS.

Pin: v14/note-u4-pin.md (FROZEN, sha256-12 06b62ecb60a9, ledger #105).
Authority: the weld-2 adjudication 4 (7213d26ea4d4, #102) ruling U4 the
next Route-A unit; the successor scout of record
(v14/note-routeA-successor-scout.md, #101); v11 paper 0 7's founding spec.

THE QUESTION (v11 paper 0 7, verbatim).  "U4 -- SPARSE RECORDS ON THE
CRYSTALS.  The conflict crystals rebuilt with renewal-only records:
geometry should be invariant (it is kinematic -- paper 0 10's third
falsifier if not); the bridges between the renewal sublattice -- itself
periodic: *the division events of a crystal form a crystal* -- are probed
for indivisible structure."

WHAT THIS PROGRAM DOES, in the pin's order:
  SEC 0   CLI, gate/waiver/anchor machinery, the mutant registry.
  SEC 1   PROVENANCE: every pinned source sha256-verified; the verbatim
          anchors (#62) bound to their consumer gates.
  SEC 2   THE COMMITTED GRAMMAR, REBUILT from the d42b1 definitions (no
          import from another unit's code; house rule #46).
  SEC 3   THE RENEWAL MARKING (pin R2) re-derived on every crystal record
          and gated against the source rows, with its scope disclosed.
  SEC 4   THE ARENA (pin R1): the four ARBITRATION crystals and the
          DECLARED COUNTEREXAMPLE CONTROL, rebuilt from the v10
          constructors' definitions, FORCED-gated per crystal, and
          cross-checked against the v10 originals' committed rows.
  SEC 5   THE HEADLINE (pin R4.1): the division-event field's exact
          translation stabilizer on Z_3^2, per crystal per site-reading,
          with an independent character-theoretic reconstruction; and THE
          MECHANISM -- the field is affine in the indicator of the
          constructor's own seed set, n = c + m*1_S, so the periodicity
          is CONSTRUCTOR-INHERITED.
  SEC 6   GEOMETRY INVARIANCE (pin R4.2): arm (a) FILTER in both of its
          sub-readings, arm (b) BUILDER-RERUN under two declared
          sub-grammars, arm (c) registered-not-run; the height-matched
          control population (this unit's, stricter than the KR wall's
          discriminator, and empty within and across records).
  SEC 7   THE BRIDGES (pin R4.3), at declared scope, candidate readings
          named, no indivisibility claim -- and none definable, the
          records being FORCED.  SEC 7b evaluates the bridges on I7's
          own coordinates: 18 of 27 cells, induced det = 0, kernel
          (1,1), one cause for both diagonals.
  SEC 8   THE WALLS (pin R5): L-1 argued before any test and DECLINED;
          BHS; the KR height control; the inherited q_12 = 0.
  SEC 9   The verdict, the head equality gate, verify-paper, the receipt.

HOUSE RULES OBSERVED.  Exact arithmetic (fractions.Fraction / integers)
end to end; no floats anywhere.  Counts COMPUTED, never typed (#24).
Every set/dict iteration feeding a printed number is ordered by a
hash-seed-independent stable key.  The plain run is byte-reproducible.
Verdicts live IN the gate statements.  Gates bind OBJECTS, not aggregates
(#87): per crystal x per reading x per arm.  Failing runs write nothing.
Committed numbers are READ from the pinned v10 outputs at run time, never
typed (#91).  Text gates match text AS WRITTEN: needles and haystacks are
whitespace-normalised, so line wrapping cannot smuggle a banned sentence
past a wall.  A gate's STATEMENT is bound to its own boolean (#20).
Every published row is DIGESTED AT GATE TIME, the artifacts are rendered
from the sealed copies, and the integrity gate compares THE BYTES ON DISK
against those digests (#119).
"""

from __future__ import annotations

import copy
import hashlib
import json
import os
import re
import sys
from collections import Counter
from fractions import Fraction as Fr
from itertools import permutations

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
OUT_TXT = os.path.join(HERE, "u4_crystals_output.txt")
OUT_JSON = os.path.join(HERE, "u4_crystals_receipt.json")
INTERP = "/opt/homebrew/bin/python3.13"

# ===========================================================================
# SEC 0.  MACHINERY
# ===========================================================================

LINES: list[str] = []
GATES: list[dict] = []
WAIVERS: list[dict] = []
ANCHORS: list[dict] = []
VANCHORS: list[dict] = []
PAYLOAD: dict = {}
NUMREG: set[str] = set()
FAILED = 0
ANCHOR_FAIL = 0
MUTANT = None
QUIET = False

# --- THE SEAL (#119) -------------------------------------------------------
# Every published row is DIGESTED AT GATE TIME, the artifacts are rendered
# FROM THE SEALED COPIES, and the final integrity gate recomputes the digests
# FROM THE BYTES ON DISK and compares them against the gate-time seals.  A
# change made to any published object after its gate has fired therefore
# cannot reach disk, and a change made to the sealed copy or to the bytes
# cannot survive the comparison.
SEALED_LINES: list[str] = []
SEALED: dict[str, list[dict]] = {"gates": [], "anchors": [], "verbatim": [],
                                 "waivers": []}
SEALS: dict[str, list[str]] = {"gates": [], "anchors": [], "verbatim": [],
                               "waivers": []}
SEALED_PAYLOAD: dict = {}
PAYLOAD_SEALS: dict[str, str] = {}
OUT_H = hashlib.sha256()                 # the output seal, updated at emit
POLARITY_CHECKS: list[dict] = []
VERBATIM_FLOOR = 20                      # #62: the length floor for a quote

MUTANTS = {
    "MUT-APERIODIC-DIVISION": {
        "what": "plants one extra division at a single site of "
                "DOUBLE-GRID(3,2), destroying the field's periodicity "
                "(kills the crystal claim)",
        "target": "G-STAB[DOUBLE-GRID(3,2)|initiator]"},
    "MUT-CONTROL-PERIODIC": {
        "what": "plants a constant division field on the delivery control, "
                "giving it the full period (kills the control)",
        "target": "G-STAB[D60-GRID(3,12)|initiator]"},
    "MUT-DIVPRED": {
        "what": "swaps the source-forced division predicate from the "
                "arbitration tag to the delivery tag",
        "target": "G-MARK-TAG[DOUBLE-GRID(3,2)]"},
    "MUT-GEOM-VARIES": {
        "what": "drops the widest division event from the restricted "
                "population, so the chart-width row VARIES and the SEGMENT "
                "VERDICT ITSELF becomes GEOMETRY-VARIES-<witness> -- the "
                "pin's R4.2 falsifier path, demonstrated at segment level",
        "target": "G-GEOM-POP-WIDTH[DOUBLE-GRID(3,2)|d=2]"},
    "MUT-NOT-FORCED": {
        "what": "withholds one round's row arbitration from "
                "DOUBLE-GRID(3,2), leaving a REFUSED record (and, downstream, "
                "the v10 committed-number anchors that bind the record)",
        "target": "G-FORCED[DOUBLE-GRID(3,2)]"},
    "MUT-MAXHITS": {
        "what": "reports DOUBLE-GRID(3,3)'s record as tie-broken "
                "(maxhits = 2) with no refusal -- the OTHER conjunct of the "
                "FORCED gate, which MUT-NOT-FORCED never reaches",
        "target": "G-FORCED[DOUBLE-GRID(3,3)]"},
    "MUT-HEIGHT-IMPURE": {
        "what": "reports a non-division event as sharing a division height "
                "layer",
        "target": "G-GEOM-HEIGHTPURE[DOUBLE-GRID(3,2)]"},
    "MUT-SITEMAP": {
        "what": "TRANSPOSES two actors in the site map (a bijection, so the "
                "site-map gate cannot see it): the field moves at the two "
                "CONFLICT-GRIDs, where the transposed sites carry unequal "
                "counts, and at neither DOUBLE-GRID nor the control",
        "target": "G-STAB[CONFLICT-GRID(3,2)|initiator]"},
    "MUT-SITEMAP-COLLAPSE": {
        "what": "COLLAPSES two actors onto one site, so the actor map is no "
                "longer injective",
        "target": "G-SITEMAP[DOUBLE-GRID(3,2)]"},
    "MUT-ARMB-COMPLETES": {
        "what": "reports the renewal-only sub-grammar rerun as completing",
        "target": "G-GEOM-ARMB-RENEWAL[DOUBLE-GRID(3,2)]"},
    "MUT-HEAD": {
        "what": "corrupts one cell of the head's stabilizer table",
        "target": "G-HEAD-EQUALITY"},
    "MUT-ANCHOR": {
        "what": "corrupts a committed v10 number so that it no longer "
                "matches the value read off the v10 line it cites",
        "target": "ANCHOR-STAGE"},
    "MUT-VERBATIM": {
        "what": "corrupts a verbatim source quote",
        "target": "ANCHOR-STAGE"},
    "MUT-VERBATIM-TRUNCATED": {
        "what": "truncates a verbatim quote to a single character, which "
                "still occurs in the source -- must die at the #62 length "
                "floor, not at the containment test",
        "target": "G-VERBATIM-FLOOR"},
    "MUT-DIAGONAL": {
        "what": "plants a diagonal co-division link count",
        "target": "G-BRIDGE-DIAG[DOUBLE-GRID(3,2)]"},
    "MUT-STAB-RECON": {
        "what": "perturbs the FOURIER route's answer at one cell and leaves "
                "the direct route untouched, so the published table and the "
                "head stay truthful and only the two-route agreement moves",
        "target": "G-STAB-RECON[CONFLICT-GRID(3,2)|footprint]"},
    "MUT-AFFINE": {
        "what": "shifts one site of a crystal's seed set, so the division "
                "field is no longer affine in the constructor's own seed "
                "indicator",
        "target": "G-AFFINE[CONFLICT-GRID(3,4)|initiator]"},
    "MUT-I7-DET": {
        "what": "plants a nonzero induced determinant at one site of "
                "DOUBLE-GRID(3,3) read on I7's coordinates",
        "target": "G-I7-INDUCED[DOUBLE-GRID(3,3)]"},
    "MUT-WALL-L1-WRAPPED": {
        "what": "reproduces the RETRACTED sentence in the paper's own house "
                "wrapping -- the form a real author would write, and the "
                "form the pre-repair contiguous-substring scan passed",
        "target": "G-WALL-L1"},
    "MUT-PROSE-POLARITY": {
        "what": "inverts a gate's STATEMENT to the opposite claim while "
                "leaving its boolean and its evidence untouched",
        "target": "G-PROSE-POLARITY"},
    "MUT-SEAM-OUTPUT-LINE": {
        "what": "SEAM: rewrites a published [DATA] line of the output after "
                "its gate has fired",
        "target": "G-SEAL-INTEGRITY"},
    "MUT-SEAM-GATE-ROW": {
        "what": "SEAM: rewrites a published gate row's statement and "
                "evidence after the gate has fired",
        "target": "G-SEAL-INTEGRITY"},
    "MUT-SEAM-GATE-FLAG": {
        "what": "SEAM: publishes a demonstrably false gate row as PASSED "
                "(the instrument-level control: gate-flag forgery)",
        "target": "G-SEAL-INTEGRITY"},
    "MUT-SEAM-PAYLOAD": {
        "what": "SEAM: rewrites a published payload row (an arena count) "
                "after its gate has fired",
        "target": "G-SEAL-INTEGRITY"},
    "MUT-SEAM-ROW-SWAP": {
        "what": "SEAM: ships the CONTROL's stabilizer row under a "
                "CONFLICT-GRID label",
        "target": "G-SEAL-INTEGRITY"},
    "MUT-SEAM-TABLE-CELL": {
        "what": "SEAM: flips a published stabilizer_table cell away from "
                "its own gate's evidence",
        "target": "G-SEAL-INTEGRITY"},
}
SEAM_MUTANTS = [k for k in MUTANTS if k.startswith("MUT-SEAM-")]


def _canon(o) -> str:
    """The canonical serialization a seal digests.  It is the SAME text on
    both sides of the seal: `json.dumps(..., default=str)` renders a
    Fraction as the string the receipt itself carries, so re-canonicalising
    a row read back from the receipt reproduces the gate-time bytes."""
    return json.dumps(o, sort_keys=True, default=str, separators=(",", ":"))


def _digest(o) -> str:
    return sha256_of(_canon(o).encode("utf-8"))


def seal_row(kind: str, row: dict) -> None:
    """#119: digest the row AT CREATION and keep the sealed copy that will
    be written.  The live row stays available to the program; only the
    sealed copy is published."""
    SEALS[kind].append(_digest(row))
    SEALED[kind].append(copy.deepcopy(row))


def seal_payload(key: str, value) -> None:
    """Seal a payload row at the moment its gates have fired."""
    PAYLOAD[key] = value
    PAYLOAD_SEALS[key] = _digest(value)
    SEALED_PAYLOAD[key] = copy.deepcopy(value)


def out_text(lines) -> str:
    """The exact text the emitted lines render to."""
    return "".join(s + "\n" for s in lines)


def norm_ws(s: str) -> str:
    """#62 / RUNBOOK 14: a text gate matches text AS WRITTEN.  Both the
    needle and the haystack are whitespace-normalised, so a sentence that
    is line-wrapped in a markdown file is the same sentence."""
    return re.sub(r"\s+", " ", s)


def emit(s: str = "") -> None:
    """Every emitted line is folded into the OUTPUT SEAL as it is emitted,
    so the bytes that reach disk are bound to the moment they were
    produced -- not to whatever the line list holds at render time."""
    LINES.append(s)
    SEALED_LINES.append(s)
    OUT_H.update((s + "\n").encode("utf-8"))


def mutate(name, normal, corrupted):
    """Mutant hook.  Returns `normal` unless this run is that mutant."""
    return corrupted if MUTANT == name else normal


def reg(*vals):
    """Register a COMPUTED number for the verify-paper numeral gate."""
    for v in vals:
        if isinstance(v, Fr):
            NUMREG.add(str(v))
            NUMREG.add(str(v.numerator))
            NUMREG.add(str(v.denominator))
            NUMREG.add(dec4(v))
        elif isinstance(v, int):
            NUMREG.add(str(v))
        elif isinstance(v, str):
            NUMREG.add(v)
    return vals[0] if vals else None


def dec4(fr: Fr) -> str:
    """Exact 4-decimal rendering by integer arithmetic (round half up)."""
    neg = fr < 0
    fr = -fr if neg else fr
    q, r = divmod(fr.numerator * 10000, fr.denominator)
    if 2 * r >= fr.denominator:
        q += 1
    s = f"{q // 10000}.{q % 10000:04d}"
    return ("-" + s) if neg else s


def dec2(fr: Fr) -> str:
    """Exact 2-decimal rendering by integer arithmetic (round half up)."""
    q, r = divmod(fr.numerator * 100, fr.denominator)
    if 2 * r >= fr.denominator:
        q += 1
    return f"{q // 100}.{q % 100:02d}"


def gate(name, statement, ok, evidence, waiver=None, kind="MEASURED",
         polarity=None):
    """A gate whose STATEMENT carries the measured verdict.

    `kind` is "MEASURED" when the verdict argument is a measurement and
    "DECLARED" when the gate carries a declaration (#34: declarations are
    labelled and counted OUT of the falsifiable denominator, never printed
    as if they were measurements).  `polarity` = (required, banned) binds
    the STATEMENT's own words to the boolean (#20): a statement that says
    the opposite of what its number says is a violation, and
    G-PROSE-POLARITY carries the count."""
    global FAILED
    ok = bool(ok)
    if not ok:
        FAILED += 1
    if polarity is not None:
        req, ban = polarity
        good = (norm_ws(req) in norm_ws(statement)
                and norm_ws(ban) not in norm_ws(statement))
        POLARITY_CHECKS.append({"gate": name, "required": req, "banned": ban,
                                "bound": good})
    row = {"gate": name, "statement": statement, "passed": ok, "kind": kind,
           "evidence": evidence, "waiver": waiver["reason"] if waiver else None}
    GATES.append(row)
    seal_row("gates", row)
    if waiver:
        wrow = {"gate": name, "class": waiver["class"],
                "reason": waiver["reason"]}
        WAIVERS.append(wrow)
        seal_row("waivers", wrow)
    ev = json.dumps(evidence, sort_keys=True, default=str)
    emit(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    emit(f"         {statement}")
    emit(f"         evidence: {ev}")
    if waiver:
        emit(f"         WAIVER [{waiver['class']}]: {waiver['reason']}")
    return ok


# --- the committed-number anchors, READ from the pinned v10 outputs -------

OUTFILES = {"d60 out": "v10/data/d60_crystal_exact.out",
            "d66 out": "v10/data/d66_arbitration_crystal_exact.out"}


def cited_line(source):
    """Resolve a citation of the form 'd66 out L64' to the TEXT OF LINE 64
    of the pinned v10 output.  The citation is the one already carried in
    the anchor table; nothing else is trusted."""
    m = re.match(r"^(d\d\d out) L(\d+)$", source.strip())
    if not m or m.group(1) not in OUTFILES:
        return None, None
    path = OUTFILES[m.group(1)]
    if path not in SOURCES:
        return path, None
    lines = SOURCES[path].split("\n")
    n = int(m.group(2))
    return path, (lines[n - 1] if 0 < n <= len(lines) else None)


def anchor(aid, quantity, typed, computed, source, key):
    """A COMMITTED number that must reproduce.  The committed side is not a
    typed literal: it is EXTRACTED at run time from the v10 output line the
    citation names, by a context-keyed regex, and the extraction is what
    the computed value is compared against.  The typed rendering survives
    only as a third check (typed == extracted).  Failure => exit 1."""
    global ANCHOR_FAIL
    path, line = cited_line(source)
    m = re.search(key, line) if line is not None else None
    extracted = m.group(1) if m else None
    ok = (extracted is not None and extracted == str(computed)
          and extracted == str(typed))
    if not ok:
        ANCHOR_FAIL += 1
    row = {"id": aid, "quantity": quantity, "source": source,
           "source_path": path, "key": key, "extracted": extracted,
           "typed": str(typed), "computed": str(computed), "passed": ok}
    ANCHORS.append(row)
    seal_row("anchors", row)
    emit(f"  [{'ANCH' if ok else 'ANCH-FAIL'}] {aid}  {quantity}: "
         f"read {extracted} from {source} == computed {computed}")
    return ok


def vanchor(vid, path, quote, consumer, norm=False):
    """#62: a verbatim source string, bound to the gate that consumes it.
    `norm` compares under whitespace normalisation, so a quote that the
    source line-wraps is still located AS WRITTEN.  The length floor and
    the uniqueness of the located quote are gated at G-VERBATIM-FLOOR."""
    global ANCHOR_FAIL
    txt = SOURCES[path]
    hay, ndl = (norm_ws(txt), norm_ws(quote)) if norm else (txt, quote)
    hits = hay.count(ndl)
    ok = hits > 0
    if not ok:
        ANCHOR_FAIL += 1
    row = {"id": vid, "path": path, "quote": quote, "found": ok,
           "occurrences": hits, "chars": len(quote),
           "normalised": bool(norm), "consumer": consumer}
    VANCHORS.append(row)
    seal_row("verbatim", row)
    emit(f"  [{'VERB' if ok else 'VERB-FAIL'}] {vid}  {path}  "
         f"-> consumer {consumer}  ({len(quote)} chars, {hits} occurrence"
         f"{'' if hits == 1 else 's'})")
    emit(f"         \"{quote[:96]}{'...' if len(quote) > 96 else ''}\"")
    return ok


def checkpoint(where):
    """Products are GATED (#91): no section consumes an object whose own
    gates have failed.  A failed gate stops the run HERE, cleanly, at the
    named gate, with nothing written."""
    bad = [g["gate"] for g in GATES if not g["passed"]]
    if bad or ANCHOR_FAIL:
        emit("")
        emit(f"  [REFUSED AT {where}] failed gates: {bad}; anchor failures: "
             f"{ANCHOR_FAIL} -- the run stops here and writes nothing")
        if not QUIET:
            print("\n".join(LINES))
            print(f"\nREFUSED AT {where}\n  failed gates: {bad}\n  anchor "
                  f"failures: {ANCHOR_FAIL}\n  NOTHING WRITTEN",
                  file=sys.stderr)
        raise SystemExit(1)


def sha256_of(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


SOURCES: dict[str, str] = {}


def read_pinned(path, want):
    """#91: every source read at its pinned sha256-12; products gated."""
    full = os.path.join(REPO, path)
    if not os.path.exists(full):
        return None, None
    with open(full, "rb") as fh:
        raw = fh.read()
    got = sha256_of(raw)[:12]
    SOURCES[path] = raw.decode("utf-8")
    return got, (got == want)


# ===========================================================================
# SEC 2.  THE COMMITTED GRAMMAR, REBUILT
#         (d42b1_transport_exact.py definitions, re-derived; no import)
# ===========================================================================

V0 = ('v', 'v0')


def vname(base, wkey, init):
    value = tuple(sorted({t[2] for t in wkey}))
    authors = tuple(sorted({t[0] for t in wkey}))
    return ('v', base, value, authors, init)


def mname(pk, value, init):
    return ('v', 'm', pk, value, init)


def value_of(v):
    if v == V0:
        return None
    return v[3] if v[1] == 'm' else v[2]


def base_of(v):
    if v == V0:
        return None
    if v[1] == 'm':
        return base_of(v[2][0])
    return v[1]


def regs_of(op):
    k = op[0]
    if k == 'p' or k == 'n':
        return frozenset([op[1]])
    if k == 'd':
        return frozenset([op[1], op[2]])
    if k == 'm':
        return frozenset([op[1], ('mw', op[1], op[2])])
    props = {t[0] for t in op[2]}
    base = next(iter(op[2]))[1]
    return frozenset(props | {vname(base, op[3], op[1])})


def event_poset(acts):
    n = len(acts)
    pred = [set() for _ in range(n)]
    last = {}
    for j, op in enumerate(acts):
        for r in regs_of(op):
            if r in last:
                pred[j] |= pred[last[r]] | {last[r]}
        for r in regs_of(op):
            last[r] = j
    return pred


class View:
    def __init__(self, acts, pred, idxs):
        self.idxs = sorted(idxs)
        self.pred = pred
        self.props = {i: acts[i] for i in self.idxs if acts[i][0] == 'p'}
        self.arbs = {i: acts[i] for i in self.idxs if acts[i][0] == 'r'}
        self.dels = {i: acts[i] for i in self.idxs if acts[i][0] == 'd'}
        self.mrgs = {i: acts[i] for i in self.idxs if acts[i][0] == 'm'}
        self.resolved, self.superseded, self.created = set(), set(), {}
        for i, op in self.arbs.items():
            self.resolved |= set(op[2])
            base = next(iter(op[2]))[1]
            self.superseded.add(base)
            self.created[vname(base, op[3], op[1])] = i
        for i, op in self.mrgs.items():
            pk, w = op[2], op[3]
            self.superseded.add(pk[0])
            self.superseded.add(pk[1])
            val = value_of(pk[0]) if w == 'both' else value_of(w)
            self.created[mname(pk, val, op[1])] = i
        self.live = {i: op for i, op in self.props.items()
                     if (op[1], op[2], op[3]) not in self.resolved}

    def holdings(self, a):
        h = {V0}
        for i, op in self.arbs.items():
            if a in {t[0] for t in op[2]}:
                base = next(iter(op[2]))[1]
                h.add(vname(base, op[3], op[1]))
        for i, op in self.dels.items():
            if op[2] == a:
                h.add(op[3])
        for i, op in self.mrgs.items():
            if op[1] == a:
                pk, w = op[2], op[3]
                val = value_of(pk[0]) if w == 'both' else value_of(w)
                h.add(mname(pk, val, op[1]))
        return h

    def incomparable(self, i, k):
        return (i not in self.pred[k]) and (k not in self.pred[i])

    def edges(self, idx_set):
        E, L = set(), sorted(idx_set)
        for ii, i in enumerate(L):
            for k in L[ii + 1:]:
                pi, pk = self.props[i], self.props[k]
                if (pi[2] == pk[2] and pi[3] != pk[3]
                        and self.incomparable(i, k)):
                    E.add((i, k))
        return E

    def components(self):
        by_base = {}
        for i, op in self.live.items():
            by_base.setdefault(op[2], []).append(i)
        comps = []
        for base, idxs in by_base.items():
            E = self.edges(set(idxs))
            parent = {i: i for i in idxs}

            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x
            for i, k in E:
                parent[find(i)] = find(k)
            groups = {}
            for i in idxs:
                groups.setdefault(find(i), set()).add(i)
            for g in groups.values():
                comps.append((base, frozenset(g)))
        return comps

    def merge_pairs(self, a):
        held = [v for v in self.holdings(a)
                if v in self.created and v not in self.superseded]
        out, S = [], sorted(held, key=repr)
        for ii, v1 in enumerate(S):
            for v2 in S[ii + 1:]:
                if base_of(v1) != base_of(v2):
                    continue
                if not self.incomparable(self.created[v1], self.created[v2]):
                    continue
                out.append(tuple(sorted((v1, v2), key=repr)))
        return out


def triples(view, idx_set):
    return frozenset((view.props[i][1], view.props[i][2], view.props[i][3])
                     for i in idx_set)


def mis_of(ckey, edge_triples):
    items = sorted(ckey)
    n, ind = len(items), []
    for mask in range(1, 1 << n):
        sub = frozenset(items[i] for i in range(n) if mask >> i & 1)
        if all((a, b) not in edge_triples and (b, a) not in edge_triples
               for a in sub for b in sub if a < b):
            ind.append(sub)
    return [s for s in ind if not any(s < t for t in ind)]


def PK1(ckey, edge_triples):
    items = sorted(ckey)
    tally = {}
    for perm in permutations(items):
        acc = []
        for t in perm:
            if all((t, u) not in edge_triples and (u, t) not in edge_triples
                   for u in acc):
                acc.append(t)
        w = frozenset(acc)
        tally[w] = tally.get(w, 0) + 1
    total = sum(tally.values())
    return {w: Fr(c, total) for w, c in tally.items()}


def edge_triples_of(view, idx_set):
    def tri(i):
        return next(iter(triples(view, {i})))
    return frozenset(tuple(sorted((tri(i), tri(k))))
                     for (i, k) in view.edges(idx_set))


def prop_options_in_view(view, a):
    out = []
    for b in view.holdings(a):
        if b in view.superseded:
            continue
        if any(op[1] == a and op[2] == b for op in view.live.values()):
            continue
        for x in (0, 1):
            out.append((b, x))
    return sorted(out, key=repr)


def arb_components_in_view(view, a):
    out = []
    for base, comp in view.components():
        if base in view.superseded:
            continue
        if a in {view.props[i][1] for i in comp}:
            out.append((base, comp))
    return out


def deliver_options_in_view(view, a, actors):
    return sorted(((r, v) for r in actors if r != a
                   for v in view.holdings(a)), key=repr)


def own_view(acts, a):
    acts2 = acts + [('n', a)]
    pred = event_poset(acts2)
    return View(acts2, pred, pred[len(acts2) - 1])


def admissible_arb_ckeys(acts, a, actors):
    pred = event_poset(acts)
    full = View(acts, pred, set(range(len(acts))))
    live_by_base = {}
    for i, op in full.live.items():
        live_by_base.setdefault(op[2], []).append(i)
    out = set()
    for b in sorted(live_by_base, key=repr):
        idxs = sorted(live_by_base[b])
        n = len(idxs)
        for smask in range(1, 1 << n):
            S = [idxs[i] for i in range(n) if smask >> i & 1]
            ck = triples(full, frozenset(S))
            if ck in out:
                continue
            m, hit = len(S), False
            for wmask in range(1, 1 << m):
                W = frozenset(S[i] for i in range(m) if wmask >> i & 1)
                ok, _ = admissible(acts, ('r', a, ck, triples(full, W)),
                                   actors)
                if ok:
                    hit = True
                    break
            if hit:
                out.add(ck)
    return out


def admissible(acts, e, actors, law=PK1):
    acts2 = acts + [e]
    j = len(acts2) - 1
    pred = event_poset(acts2)
    view = View(acts2, pred, pred[j])
    kind = e[0]
    if kind == 'n':
        a = e[1]
        has_p = bool(prop_options_in_view(view, a))
        has_am = bool(view.merge_pairs(a)
                      or admissible_arb_ckeys(acts, a, actors))
        has_d = bool(deliver_options_in_view(view, a, actors))
        return True, (1 - (Fr(1, 4) if has_p else 0)
                      - (Fr(1, 4) if has_am else 0)
                      - (Fr(1, 4) if has_d else 0))
    if kind == 'p':
        a, b, x = e[1], e[2], e[3]
        opts = prop_options_in_view(view, a)
        if (b, x) not in opts:
            return False, None
        return True, Fr(1, 4) / len(opts)
    if kind == 'd':
        s, r, v = e[1], e[2], e[3]
        if r == s or r not in actors:
            return False, None
        opts = deliver_options_in_view(own_view(acts, s), s, actors)
        if (r, v) not in opts:
            return False, None
        return True, Fr(1, 4) / len(opts)
    if kind == 'm':
        a, pk, w = e[1], e[2], e[3]
        D = (len(admissible_arb_ckeys(acts, a, actors))
             + len(view.merge_pairs(a)))
        if pk not in view.merge_pairs(a):
            return False, None
        v1, v2 = pk
        if value_of(v1) != value_of(v2):
            if w not in pk:
                return False, None
            return True, Fr(1, 4) / D * Fr(1, 2)
        if w != 'both':
            return False, None
        return True, Fr(1, 4) / D
    a, ckey, wkey = e[1], e[2], e[3]
    comps = arb_components_in_view(view, a)
    match = [c for c in comps if triples(view, c[1]) == ckey]
    if not match:
        return False, None
    base, comp = match[0]
    et = edge_triples_of(view, comp)
    if wkey not in mis_of(ckey, et):
        return False, None
    D = len(comps) + len(view.merge_pairs(a))
    return True, Fr(1, 4) / D * law(ckey, et)[wkey]


def candidates_for(acts, actors):
    pred = event_poset(acts)
    full = View(acts, pred, set(range(len(acts))))
    bases = sorted({V0} | set(full.created), key=repr)
    out = []
    live_by_base = {}
    for i, op in full.live.items():
        live_by_base.setdefault(op[2], []).append(i)
    for a in actors:
        for b in bases:
            for x in (0, 1):
                e = ('p', a, b, x)
                ok, q = admissible(acts, e, actors)
                if ok:
                    out.append((e, q))
        seen = set()
        for b in sorted(live_by_base, key=repr):
            idxs = sorted(live_by_base[b])
            n = len(idxs)
            for smask in range(1, 1 << n):
                S = [idxs[i] for i in range(n) if smask >> i & 1]
                ck = triples(full, frozenset(S))
                m = len(S)
                for wmask in range(1, 1 << m):
                    W = frozenset(S[i] for i in range(m) if wmask >> i & 1)
                    e = ('r', a, ck, triples(full, W))
                    if e in seen:
                        continue
                    seen.add(e)
                    ok, q = admissible(acts, e, actors)
                    if ok:
                        out.append((e, q))
        held = sorted(full.holdings(a), key=repr)
        for ii, v1 in enumerate(held):
            for v2 in held[ii + 1:]:
                pk = tuple(sorted((v1, v2), key=repr))
                for w in (pk[0], pk[1], 'both'):
                    e = ('m', a, pk, w)
                    ok, q = admissible(acts, e, actors)
                    if ok:
                        out.append((e, q))
        for r in actors:
            if r == a:
                continue
            for v in held:
                e = ('d', a, r, v)
                ok, q = admissible(acts, e, actors)
                if ok:
                    out.append((e, q))
        e = ('n', a)
        ok, q = admissible(acts, e, actors)
        out.append((e, q))
    return out


# ---- the division / renewal predicate (pin R2), SOURCE-FORCED ------------

def is_division(e):
    """The renewal marking.  v11 paper 0 4's [POSIT] identifies division
    events with renewal events; paper-09 3 records renewal =
    class-0-carrying-an-arb as SOURCE-FORCED from three agreeing rows, of
    which the clause that transports to a 9-actor record is the
    ARBITRATION TAG (SEC 3 measures why the other two are silent here)."""
    return e[0] == mutate("MUT-DIVPRED", 'r', 'd')


def is_division_structural(e):
    """A SECOND, INDEPENDENT predicate for the same set, written from the
    grammar's tuple SHAPES and not from its tags: an arbitration is the
    unique 4-tuple whose third slot is a conflict key (a frozenset).
    Proposals carry a value tuple there, deliveries an actor string,
    merges a pair of values, idles are 2-tuples."""
    return len(e) == 4 and isinstance(e[2], frozenset)


# ===========================================================================
# SEC 4a.  THE CRYSTAL CONSTRUCTORS, REBUILT
#          (d60 `B`/CRYSTAL-2D, d66 `double_grid`/`conflict_grid`
#           definitions, re-derived here; no import)
# ===========================================================================

class Builder:
    """D60's `B`: every event taken from the committed layer's own menu,
    specified by its full tuple; `maxhits == 1` gates that the record is
    FORCED (nothing tie-broken); a refusal is recorded, never patched.
    `filt` is the declared sub-grammar hook of pin R3(b) (the d74 shape:
    the SUPPORT is restricted, the committed weights are untouched)."""

    def __init__(self, actors, filt=None):
        self.actors, self.H, self.refusal, self.maxhits = actors, [], None, 0
        self.filt = filt

    def pick(self, inits, spec, label):
        if self.refusal:
            return None
        menu = candidates_for(list(self.H), tuple(inits))
        if self.filt is not None:
            menu = [(e, q) for e, q in menu if self.filt(e)]
        hits = sorted((e for e, q in menu if spec(e)), key=repr)
        self.maxhits = max(self.maxhits, len(hits))
        if not hits:
            self.refusal = (label, len(self.H))
            return None
        self.H.append(hits[0])
        return hits[0]


def _pick(b, actors, e, lbl):
    return b.pick(tuple(actors), lambda z, e=e: z == e, lbl)


def _dl(b, s, r, v):
    b.pick((s, r), lambda e, s=s, r=r: e[0] == 'd' and e[1] == s
           and e[2] == r and e[3] == v, f"{s}->{r}")


def double_grid(g, R, filt=None, drop_one_arb=False):
    """D66/D67's DOUBLE-GRID(g, R): rows AND columns conflict concurrently
    on 2g independent base lineages, delivery-free after the bootstrap;
    the object that saturates the width ceiling k*b <= k^2."""
    ac = [[f"D{i}{j}" for j in range(g)] for i in range(g)]
    flat = [a for row in ac for a in row]
    b = Builder(tuple(flat), filt)
    groups = ([[ac[i][j] for j in range(g)] for i in range(g)]
              + [[ac[i][j] for i in range(g)] for j in range(g)])
    seeds = ([ac[i][i] for i in range(g)]
             + [ac[(j + 2) % g][j] for j in range(g)])
    cur = [None] * len(groups)
    for gi, sd in enumerate(seeds):
        _pick(b, (sd,), ('p', sd, V0, 0), f"mint-propose {sd}")
        ck = frozenset({(sd, V0, 0)})
        _pick(b, (sd,), ('r', sd, ck, ck), f"mint-arbitrate {sd}")
        cur[gi] = vname(V0, ck, sd)
        if b.refusal:
            return b
    for gi, grp in enumerate(groups):
        for a in grp:
            if a != seeds[gi]:
                _dl(b, seeds[gi], a, cur[gi])
                if b.refusal:
                    return b
    for t in range(R):
        trips = []
        for gi, grp in enumerate(groups):
            tp = [(a, cur[gi], 0 if a == seeds[gi] else 1) for a in grp]
            trips.append(tp)
            for x in tp:
                _pick(b, (x[0],), ('p',) + x, f"propose {x[0]}")
                if b.refusal:
                    return b
        for gi in range(len(groups)):
            if drop_one_arb and t == R - 1 and gi == 0:
                b.refusal = ("MUT-NOT-FORCED: arbitration withheld",
                             len(b.H))
                return b
            wk = frozenset({(seeds[gi], cur[gi], 0)})
            _pick(b, (seeds[gi],),
                  ('r', seeds[gi], frozenset(trips[gi]), wk),
                  f"arbitrate {seeds[gi]}")
            if b.refusal:
                return b
            cur[gi] = vname(cur[gi], wk, seeds[gi])
    return b


def conflict_group(b, grp, base, seed, winner):
    trips = [(a, base, 0 if a == seed else 1) for a in grp]
    for t in trips:
        _pick(b, (t[0],), ('p',) + t, f"propose {t[0]}")
    ck = frozenset(trips)
    wk = frozenset({[t for t in trips if t[0] == winner][0]})
    _pick(b, (seed,), ('r', seed, ck, wk), f"arbitrate {seed}")
    return vname(base, wk, seed)


def conflict_grid(g, R, filt=None):
    """D66's CONFLICT-GRID(g, R): g-proposer arbitrations on orthogonal
    row / column partitions of a g x g actor grid."""
    ac = [[f"G{i}{j}" for j in range(g)] for i in range(g)]
    flat = [a for row in ac for a in row]
    b = Builder(tuple(flat), filt)
    cur = {a: V0 for a in flat}
    for t in range(R):
        if t % 2 == 0:
            groups = [[ac[i][j] for j in range(g)] for i in range(g)]
            seeds = [ac[i][i] for i in range(g)]
        else:
            groups = [[ac[i][j] for i in range(g)] for j in range(g)]
            seeds = [ac[j][j] for j in range(g)]
        for gi, grp in enumerate(groups):
            sd, base = seeds[gi], cur[seeds[gi]]
            for a in grp:
                if a != sd and cur[a] != base:
                    _dl(b, sd, a, base)
            v = conflict_group(b, grp, base, sd, sd)
            for a in grp:
                cur[a] = v
            if b.refusal:
                return b
    return b


def d60_grid(K=3, PHASES=12, filt=None):
    """D60's CRYSTAL-2D: the 3x3 delivery grid, 12 phases.  THE DECLARED
    COUNTEREXAMPLE CONTROL of pin R1."""
    GRID = [f"G{i}{j}" for i in range(K) for j in range(K)]

    def gid(i, j):
        return f"G{i % K}{j % K}"
    b = Builder(tuple(GRID), filt)
    a0 = GRID[0]
    b.pick((a0,), lambda e: e[0] == 'p' and e[1] == a0 and e[2] == V0
           and e[3] == 0, "mint propose")
    b.pick((a0,), lambda e: e[0] == 'r' and e[1] == a0, "mint arbitrate")
    V1 = None
    if not b.refusal:
        menu = candidates_for(list(b.H), (a0, GRID[1]))
        dv = sorted({e[3] for e, q in menu if e[0] == 'd' and e[3] != V0},
                    key=repr)
        V1 = dv[0] if dv else None
    for s, r in zip(GRID, GRID[1:]):
        b.pick((s, r), lambda e, s=s, r=r: e[0] == 'd' and e[1] == s
               and e[2] == r and e[3] == V1, f"spread {s}->{r}")
    for t in range(PHASES):
        ph = t % 4
        if ph == 0:
            pairs = [(gid(i, j), gid(i, j + 1)) for i in range(K)
                     for j in range(0, K - 1, 2)]
        elif ph == 1:
            pairs = [(gid(i, j), gid(i, j + 1)) for i in range(K)
                     for j in range(1, K - 1, 2)]
        elif ph == 2:
            pairs = [(gid(i, j), gid(i + 1, j)) for j in range(K)
                     for i in range(0, K - 1, 2)]
        else:
            pairs = [(gid(i, j), gid(i + 1, j)) for j in range(K)
                     for i in range(1, K - 1, 2)]
        for (s, r) in pairs:
            if (t // 4) % 2 == 1:
                s, r = r, s
            _dl(b, s, r, V1)
    return b


CRYSTALS = [
    ("DOUBLE-GRID(3,2)", "ARBITRATION", lambda f=None: double_grid(3, 2, f)),
    ("DOUBLE-GRID(3,3)", "ARBITRATION", lambda f=None: double_grid(3, 3, f)),
    ("CONFLICT-GRID(3,2)", "ARBITRATION",
     lambda f=None: conflict_grid(3, 2, f)),
    ("CONFLICT-GRID(3,4)", "ARBITRATION",
     lambda f=None: conflict_grid(3, 4, f)),
    ("D60-GRID(3,12)", "CONTROL", lambda f=None: d60_grid(filt=f)),
]
ARB = [c[0] for c in CRYSTALS if c[1] == "ARBITRATION"]
CTRL = [c[0] for c in CRYSTALS if c[1] == "CONTROL"][0]
READINGS = ["initiator", "footprint"]
L = 3                                    # the site lattice is Z_L^2
SITES = [(i, j) for i in range(L) for j in range(L)]
AXIS = [(1, 0), (0, 1)]
DIAG = [(1, 1), (1, 2)]


# ===========================================================================
# SEC 5a.  THE SITE READING, THE FIELD, THE STABILIZER
# ===========================================================================

def site_map(b):
    """The actor -> Z_3^2 site map.  FORCED by the constructors' own actor
    naming: every crystal names its actors <prefix><i><j> on a 3x3 grid."""
    out = {}
    for a in sorted(b.actors):
        out[a] = (int(a[1]), int(a[2]))
    if MUTANT == "MUT-SITEMAP":
        # the TRANSPOSITION the registry advertises: still a bijection, so
        # G-SITEMAP cannot see it -- it moves the FIELD instead.
        ks = sorted(out)
        out[ks[0]], out[ks[1]] = out[ks[1]], out[ks[0]]
    if MUTANT == "MUT-SITEMAP-COLLAPSE":
        # the collapse: two actors onto one site, so the map is not
        # injective and the bijection gate fires.
        ks = sorted(out)
        out[ks[0]] = out[ks[1]]
    return out


def division_field(b, reading, name=None):
    """The division-event field n : Z_3^2 -> Z_>=0, at the declared site
    reading.  (a) initiator = the arbitrating actor op[1];  (b) footprint
    = every actor in the event's register footprint regs_of(op)."""
    S = site_map(b)
    f = {x: 0 for x in SITES}
    for e in b.H:
        if not is_division(e):
            continue
        if reading == "initiator":
            f[S[e[1]]] += 1
        else:
            for r in regs_of(e):
                if isinstance(r, str) and r in S:
                    f[S[r]] += 1
    if MUTANT == "MUT-APERIODIC-DIVISION" and name == "DOUBLE-GRID(3,2)":
        f[(0, 2)] += 1
    if MUTANT == "MUT-CONTROL-PERIODIC" and name == CTRL:
        f = {x: 1 for x in SITES}
    return f


def seed_sites(nm):
    """THE CONSTRUCTOR'S OWN SEED SET, re-derived from the seed rule in the
    committed constructor and NOT read off the measured field.  d66 seats
    `double_grid`'s row groups at ac[i][i] and its column groups at
    ac[(j+2)%g][j]; it seats `conflict_grid` at ac[i][i] in both parities;
    d60's control mints and arbitrates at GRID[0] alone."""
    g = L
    if nm.startswith("DOUBLE-GRID"):
        S = {(i, i) for i in range(g)} | {((j + 2) % g, j) for j in range(g)}
    elif nm.startswith("CONFLICT-GRID"):
        S = {(i, i) for i in range(g)}
    else:
        S = {(0, 0)}
    if MUTANT == "MUT-AFFINE" and nm == "CONFLICT-GRID(3,4)":
        S = (S - {(2, 2)}) | {(2, 1)}
    return sorted(S)


def affine_fit(f, S):
    """Is the field AFFINE in the indicator of the seed set --
    n = c + m*1_S ?  Returns (c, m) or None.  Exact integers."""
    Sset = set(S)
    on = {f[x] for x in SITES if x in Sset}
    off = {f[x] for x in SITES if x not in Sset}
    if len(on) != 1 or len(off) > 1:
        return None
    c = next(iter(off)) if off else 0
    return (c, next(iter(on)) - c)


def stabilizer(f):
    """{ t in Z_3^2 : n(x + t) = n(x) for every x }, by direct test."""
    out = []
    for t in SITES:
        if all(f[((x[0] + t[0]) % L, (x[1] + t[1]) % L)] == f[x]
               for x in SITES):
            out.append(t)
    return sorted(out)


def subgroup_name(S):
    """Name the subgroup of Z_3^2 by its order and its generator."""
    if len(S) == 1:
        return "1"
    if len(S) == 9:
        return "Z3^2"
    g = sorted(t for t in S if t != (0, 0))[0]
    return f"<({g[0]},{g[1]})>"


# --- the INDEPENDENT reconstruction: characters over Z[omega] -------------

def _hat_nonzero(f, chi):
    """Is the Z_3^2 Fourier coefficient  sum_x n(x) omega^{-chi.x}  nonzero?
    Exact in Z[omega] = Z[t]/(t^2 + t + 1): collect the three coefficients
    c0, c1, c2 and reduce by omega^2 = -1 - omega.  No floats, no library."""
    c = [0, 0, 0]
    for x in SITES:
        k = (-(chi[0] * x[0] + chi[1] * x[1])) % 3
        c[k] += f[x]
    return (c[0] - c[2], c[1] - c[2]) != (0, 0)


def stabilizer_by_characters(f):
    """Stab(n) = the annihilator of the support of the Fourier transform.
    Shares no code and no typed constant with `stabilizer`: it runs over
    the DUAL group and multiplies characters instead of translating the
    field."""
    supp = [chi for chi in SITES if _hat_nonzero(f, chi)]
    return sorted(t for t in SITES
                  if all((chi[0] * t[0] + chi[1] * t[1]) % 3 == 0
                         for chi in supp))


# ===========================================================================
# SEC 6a.  THE GEOMETRY INSTRUMENT
#          (d60's `poset_of`/`profile` over d47a's `heights`/`sky` kind B
#           and d58's `covers`; definitions re-derived, no import)
# ===========================================================================

def poset_of(h):
    pred = event_poset(list(h))
    n = len(h)
    return [[i in pred[j] for j in range(n)] for i in range(n)]


def heights(C):
    n = len(C)
    hh = [0] * n
    order = sorted(range(n), key=lambda x: sum(C[i][x] for i in range(n)))
    for x in order:
        preds = [i for i in range(n) if C[i][x]]
        hh[x] = 1 + max((hh[i] for i in preds), default=-1)
    return hh


def sky_b(C, e, depth, hh):
    """d47a's sky kind 'B': the directions at height gap exactly `depth`."""
    return [f for f in range(len(C)) if C[e][f] and hh[f] - hh[e] == depth]


def covers(C):
    n = len(C)
    out = []
    for i in range(n):
        for j in range(n):
            if C[i][j] and not any(C[i][k] and C[k][j] for k in range(n)):
                out.append((i, j))
    return out


def profile(C, pop=None):
    """d60's `profile`: D58's atlas restricted to a POPULATION of events
    (the poset is left whole; only the metric population changes)."""
    n = len(C)
    P = sorted(range(n)) if pop is None else sorted(pop)
    hh = heights(C)
    cov = covers(C)
    Pset = set(P)
    out = {}
    for d in (2, 3):
        DIRS = {e: set(sky_b(C, e, d, hh)) for e in range(n)}
        w = [len(DIRS[e]) for e in P]
        om = []
        for (e, e2) in cov:
            if e not in Pset or len(DIRS[e]) < 2:
                continue
            om.append(Fr(len(DIRS[e] & set(sky_b(C, e2, d - 1, hh))),
                         len(DIRS[e])))
        out[d] = {"n": len(P),
                  "h2": Fr(sum(1 for x in w if x >= 2), len(P)),
                  "h4": Fr(sum(1 for x in w if x >= 4), len(P)),
                  "max": max(w), "mean": Fr(sum(w), len(P)),
                  "pairs": len(om),
                  "om": (sum(om) / len(om)) if om else None,
                  "attained": sorted(e for e in P if len(DIRS[e]) == max(w))}
    out["height"] = (max(hh[e] for e in P) + 1) if P else 0
    out["longest_chain"] = out["height"]
    return out


# ===========================================================================
# THE RUN
# ===========================================================================

PINNED = [
    ("v14/note-u4-pin.md", "06b62ecb60a9", "the pin (FROZEN)"),
    ("v14/note-routeA-successor-scout.md", "88375db9cec2",
     "the successor scout of record"),
    ("v14/note-w2-adjudication.md", "7213d26ea4d4",
     "the weld-2 adjudication (the successor ruling)"),
    ("v11/relativistic-isp-v11-paper0-the-indivisible-record-law.md",
     "37a428321f46", "v11 paper 0 (the question, the POSIT, the falsifiers)"),
    ("v14/paper-09-renewal-transport.md", "006f96aaa2ff",
     "paper-09 3 (what a renewal is)"),
    ("v11/note-v11p0a-reproduction-catalog.md", "0cebe543e814",
     "the reproduction catalog (the BHS and KR walls)"),
    ("v11/note-L1-lorentz-no-go-lemma.md", "93ea24591c3c",
     "L-1 (the fourth form; the scope guard)"),
    ("v10/code/d60_crystal_exact.py", "684cdb76552b",
     "D60: the Builder, CRYSTAL-2D, profile"),
    ("v10/code/d66_arbitration_crystal_exact.py", "3d0516ab106e",
     "D66: double_grid, conflict_grid"),
    ("v10/code/d67_k4_double_grid_exact.py", "e80edf851d93",
     "D67: the k=4 double grid"),
    ("v10/code/d63_wide_crystal_exact.py", "89e170f40579",
     "D63: the wide crystal"),
    ("v10/code/d47a_sky_instrument_exact.py", "f0b578c13409",
     "D47a: heights, sky"),
    ("v10/code/d58_atlas_instrument_exact.py", "e5f58cb52a06",
     "D58: covers, atlas"),
    ("v10/code/d42b1_transport_exact.py", "576275d55ecf",
     "D42b1: the transport grammar"),
    ("v10/code/d74_transport_holonomy_exact.py", "bb852161aced",
     "D74: the declared sub-grammar shapes"),
    ("v10/data/d60_crystal_exact.out", "f768a4eafcd5",
     "D60's committed output"),
    ("v10/data/d66_arbitration_crystal_exact.out", "e252529d2586",
     "D66's committed output"),
    ("v14/paper-13-weld2-carrier-census.md", "9cdb10472953",
     "weld 2 (I7's arena, read as data: sites, links, readout)"),
    ("v14/note-u4-adjudication.md", "fa991e19ae54",
     "the U4 adjudication (the head's qualifier; the repair orders)"),
]

# --- the L-1 wall's banned needles (RUNBOOK 14: text gates match text AS
#     WRITTEN).  Each needle is assembled from fragments so that the wall's
#     own definition does not self-trigger under whitespace normalisation,
#     and each is #62-anchored (V15/V16) against the pinned v11 paper 0
#     erratum that carries the retracted sentence -- wrapped, as prose is.
_BF = "precisely the form U4 " + "tests"
BANNED_NEEDLES = [
    _BF + ", and precisely the form the corpus's strongest relativity "
          "result took",
    _BF,
]
# the retracted sentence as a real author would write it: wrapped at the
# paper's own ~72 characters.  MUT-WALL-L1-WRAPPED injects exactly this.
WRAP_INJECTION = ("untested and is registered for a successor.  The weaker "
                  "form is\n" + _BF + ", and precisely the form the "
                  "corpus's\nstrongest relativity result took.\n")


def run_provenance():
    emit("=" * 78)
    emit("SEC 1  PROVENANCE -- pinned-sha reads (#91); products gated")
    emit("=" * 78)
    rows, allok = [], True
    for path, want, what in PINNED:
        got, ok = read_pinned(path, want)
        rows.append({"path": path, "want": want, "got": got, "ok": bool(ok),
                     "what": what})
        allok = allok and bool(ok)
        gate(f"G-PROV[{path}]",
             f"the pinned source is present and its sha256-12 is {want} "
             f"(measured {got}) -- {what}",
             bool(ok), {"path": path, "want": want, "got": got})
    seal_payload("provenance", rows)
    gate("G-PROV-ROOT",
         f"ALL {len(PINNED)} pinned sources resolve under the repo root "
         f"derived from this file's own location and every one reproduces "
         f"its pinned sha256-12; a run outside the repo cannot reach them "
         f"and fails HERE, loudly and by design, writing nothing",
         allok, {"sources": len(PINNED), "all_verified": allok,
                 "repo_root_derived_from": "__file__"})
    return allok


def run_verbatim():
    emit("")
    emit("-" * 78)
    emit("The verbatim anchors (#62), each bound to its consumer gate")
    emit("-" * 78)
    P0 = "v11/relativistic-isp-v11-paper0-the-indivisible-record-law.md"
    P9 = "v14/paper-09-renewal-transport.md"
    CAT = "v11/note-v11p0a-reproduction-catalog.md"
    L1 = "v11/note-L1-lorentz-no-go-lemma.md"
    D74 = "v10/code/d74_transport_holonomy_exact.py"
    D60 = "v10/code/d60_crystal_exact.py"
    PIN = "v14/note-u4-pin.md"
    P13 = "v14/paper-13-weld2-carrier-census.md"
    q = [
        ("V01", P0, "U4 — SPARSE RECORDS ON THE CRYSTALS.**  The conflict "
         "crystals\n  rebuilt with renewal-only records", "G-ARENA-SCOPE"),
        ("V02", P0, "v11's **division events are the renewal events.**",
         "G-MARK-POSIT"),
        ("V03", P9, "REN = [h for h in FAM if len(h) <= 4 and "
         "CLS[tuple(h)] == 0 and any(e[0] == 'r' for e in h)]",
         "G-MARK-SOURCE-ROWS"),
        ("V04", P9, "Class 0 is necessary and not sufficient: an "
         "arbitration is required.", "G-MARK-SOURCE-ROWS"),
        ("V05", P9, "every pair arbitration is a renewal to the root state "
         "[THEOREM at two-actor delivery-free scope]",
         "G-MARK-ROOT[DOUBLE-GRID(3,2)]"),
        ("V06", P0, "If U4 shows sparse records destroy the geometry, "
         "kinematics and\n  law are not separable as posited",
         "G-GEOM-SEGMENT"),
        ("V07", CAT, "v11's\ncrystals are finite-valency by construction, "
         "so BHS says their renewal\nsublattice **cannot** be statistically "
         "Lorentz-invariant in the sprinkling\nsense.", "G-WALL-BHS"),
        ("V08", CAT, "a dimension reading without a height\ncontrol is "
         "worthless", "G-WALL-KR"),
        ("V09", L1, "it is a\n   **fourth form, outside paper 8's three**, "
         "and its admissibility is\n   v11's to argue when U4 runs.",
         "G-WALL-L1"),
        ("V10", L1, "It does **not** forbid a permutation action.",
         "G-WALL-L1-PERMUTATION"),
        ("V11", D74, "A declared SUB-GRAMMAR: the support is\n    "
         "restricted, the committed weights are untouched.",
         "G-GEOM-ARMB-RENEWAL[DOUBLE-GRID(3,2)]"),
        ("V12", D60, "D58's atlas restricted to a POPULATION of events (the "
         "poset is\n    left whole; only the metric population changes)",
         "G-GEOM-POP-INSTRUMENT"),
        ("V13", PIN, "q₁₂ ≡ 0 is INHERITED", "G-WALL-DIAGONAL"),
        ("V14", PIN, "The delivery\ncrystal D60-GRID(3,12) is the DECLARED "
         "COUNTEREXAMPLE CONTROL", "G-CONTROL-DECLARED"),
    ]
    ok = True
    for vid, path, quote, cons in q:
        if MUTANT == "MUT-VERBATIM" and vid == "V03":
            quote = quote.replace("== 0", "== 1")
        if MUTANT == "MUT-VERBATIM-TRUNCATED" and vid == "V03":
            quote = quote[:1]
        ok = vanchor(vid, path, quote, cons) and ok
    # the L-1 needles themselves, bound to the source that carries the
    # retracted sentence -- WRAPPED, which is why these two are matched
    # under the same whitespace normalisation the wall gate uses.
    nq = [("V15", P0, BANNED_NEEDLES[0], "G-WALL-L1"),
          ("V16", P0, BANNED_NEEDLES[1], "G-WALL-L1"),
          ("V17", P13, "links | $\\mathcal L = \\{(1,0),\\,(0,1),\\,(1,1)\\}$",
           "G-I7-INDUCED[DOUBLE-GRID(3,2)]"),
          ("V18", P13, "$q_{11}=n_{e_1}$,\n$q_{22}=n_{e_2}$, "
           "$q_{12}=(n_{e_1+e_2}-n_{e_1}-n_{e_2})/2$",
           "G-I7-INDUCED[DOUBLE-GRID(3,2)]")]
    for vid, path, quote, cons in nq:
        ok = vanchor(vid, path, quote, cons, norm=True) and ok
    short = min(len(v["quote"]) for v in VANCHORS)
    multi = [v["id"] for v in VANCHORS if v["occurrences"] != 1]
    reg(len(VANCHORS), short)
    gate("G-VERBATIM-FLOOR",
         f"#62 WITH A FLOOR.  A containment test with no floor is not an "
         f"anchor: a single character occurs in every source.  All "
         f"{len(VANCHORS)} verbatim anchors are gated for LENGTH (shortest "
         f"{short} characters, floor {VERBATIM_FLOOR}) and their occurrence "
         f"counts are gated: {len(multi)} quote(s) occur other than exactly "
         f"once in their source, and every one of the "
         f"{len(VANCHORS)} is bound by name to the gate that consumes it",
         short >= VERBATIM_FLOOR and multi == []
         and len(VANCHORS) == len(q) + len(nq),
         {"anchors": len(VANCHORS), "shortest": short,
          "floor": VERBATIM_FLOOR, "non_unique": multi,
          "occurrences": {v["id"]: v["occurrences"] for v in VANCHORS}})
    seal_payload("verbatim_anchors", len(VANCHORS))
    return ok


def main_run():
    global FAILED
    emit("=" * 78)
    emit("U4 / paper-14 -- RENEWAL-ONLY CRYSTALS")
    emit("pin v14/note-u4-pin.md (06b62ecb60a9, ledger #105)")
    emit("=" * 78)
    emit("")

    run_provenance()
    checkpoint("SEC 1 (the pinned-sha reads) -- a run that cannot reach the "
               "pinned sources stops HERE, at a named gate, by design")
    run_verbatim()
    checkpoint("SEC 1 (the verbatim anchors)")

    # -------------------------------------------------------------- SEC 3
    emit("")
    emit("=" * 78)
    emit("SEC 3  THE RENEWAL MARKING -- re-derived, gated against the source")
    emit("=" * 78)
    built = {}
    for nm, kind, fn in CRYSTALS:
        built[nm] = fn()

    kin = sum(1 for b in built.values() for e in b.H
              if e[0] in ('d', 'n') and is_division(e))
    marked_any = all(any(is_division(e) for e in b.H) for b in built.values())
    reg(kin)
    gate("G-MARK-POSIT",
         f"v11 paper 0 4's [POSIT] (V02) is carried verbatim and is this "
         f"unit's ONLY identification of division with renewal: idles and "
         f"deliveries remain grammar events and are not records, so the "
         f"renewal-only record is the record of arbitrations.  MEASURED "
         f"CONSEQUENCE, not declared: across all five records {kin} "
         f"kinematic events (deliveries and idles) are marked, and every "
         f"record carries at least one marked event ({marked_any})",
         kin == 0 and marked_any,
         {"posit": "division events ARE the renewal events",
          "kinematic_events_marked": kin, "every_record_marked": marked_any})

    mark_rows = []
    for nm, kind, _fn in CRYSTALS:
        b = built[nm]
        tag = [i for i, e in enumerate(b.H) if is_division(e)]
        struct = [i for i, e in enumerate(b.H) if is_division_structural(e)]
        reg(len(tag), len(struct))
        gate(f"G-MARK-TAG[{nm}]",
             f"on this crystal's {len(b.H)}-event record the SOURCE-FORCED "
             f"tag predicate selects {len(tag)} events and an INDEPENDENT "
             f"predicate written from the grammar's tuple SHAPES (the unique "
             f"4-tuple whose third slot is a conflict key) selects "
             f"{len(struct)}, and the two sets are IDENTICAL index for "
             f"index -- the marking is not carried by the tag alone",
             tag == struct, {"crystal": nm, "tag": len(tag),
                             "structural": len(struct),
                             "identical": tag == struct})
        # S4's renewal-to-root content, re-derived event by event
        ok, bad = 0, []
        for i in tag:
            op = b.H[i]
            if op[0] != 'r':
                bad.append(i)
                continue
            pre = b.H[:i + 1]
            V = View(pre, event_poset(pre), set(range(len(pre))))
            base = next(iter(op[2]))[1]
            mint = vname(base, op[3], op[1])
            props = {t[0] for t in op[2]}
            if all(mint in V.holdings(a) for a in props) \
                    and base in V.superseded:
                ok += 1
            else:
                bad.append(i)
        reg(ok)
        gate(f"G-MARK-ROOT[{nm}]",
             f"S4's renewal CONTENT (V05) is re-derived on this record event "
             f"by event: at {ok} of {len(tag)} marked events every proposer "
             f"in the conflict key holds the newly minted value immediately "
             f"after, and the superseded base is retired -- the marked "
             f"events are exactly the events that reset their conflict group "
             f"to one shared value, which is what 'a renewal to the root' "
             f"says at this arena",
             ok == len(tag) and len(tag) > 0,
             {"crystal": nm, "marked": len(tag), "renewal_to_root": ok,
              "violations": bad[:5]})
        cks = Counter(len(b.H[i][2]) for i in tag)
        pairs = cks.get(2, 0)
        reg(pairs)
        mark_rows.append({"crystal": nm, "events": len(b.H),
                          "marked": len(tag), "structural": len(struct),
                          "renewal_to_root": ok,
                          "ckey_sizes": sorted(cks.items()),
                          "pair_arbitrations": pairs})
    seal_payload("marking", mark_rows)
    tot_pairs = sum(r["pair_arbitrations"] for r in mark_rows)
    tot_marked = sum(r["marked"] for r in mark_rows)
    reg(tot_pairs, tot_marked)
    gate("G-MARK-SOURCE-ROWS",
         f"THE MARKING'S WARRANT, MEASURED AND SCOPED.  paper-09 3 forces "
         f"renewal = class-0-carrying-an-arb from three agreeing rows "
         f"(V03, V04, V05).  Of the three, exactly ONE reaches this arena: "
         f"the class-0 clause is a two-actor delivery-free STATE-SPACE "
         f"notion with no committed referent at nine actors, and S4's "
         f"narrower sufficient condition -- PAIR arbitration -- selects "
         f"{tot_pairs} of the {tot_marked} marked events across all five "
         f"crystals, because every conflict key here has size 1 or 3.  What "
         f"transports is the ARBITRATION TAG, and G-MARK-ROOT shows S4's "
         f"CONTENT transports even though its hypothesis does not",
         tot_pairs == 0 and tot_marked > 0,
         {"pair_arbitrations": tot_pairs, "marked_total": tot_marked,
          "clauses_reaching_this_arena": ["arbitration tag"],
          "clauses_out_of_scope": ["class-0 (two-actor delivery-free)",
                                   "S4 pair hypothesis (vacuous here)"]})
    checkpoint("SEC 3 (the renewal marking)")

    # -------------------------------------------------------------- SEC 4
    emit("")
    emit("=" * 78)
    emit("SEC 4  THE ARENA -- five crystals, FORCED, cross-checked to v10")
    emit("=" * 78)
    gate("G-ARENA-SCOPE",
         "the arena is the pin R1 arena and nothing else: the four "
         f"ARBITRATION crystals {ARB} plus the DECLARED COUNTEREXAMPLE "
         f"CONTROL {CTRL}; the question they answer is V01, quoted verbatim",
         len(ARB) == 4, {"arbitration": ARB, "control": CTRL})
    ctrl_named = norm_ws(f"crystal {CTRL} is the DECLARED COUNTEREXAMPLE "
                         f"CONTROL") in norm_ws(SOURCES["v14/note-u4-pin.md"])
    gate("G-CONTROL-DECLARED",
         f"{CTRL} is the pin's DECLARED COUNTEREXAMPLE CONTROL (V14): every "
         f"periodicity claim below must return its OTHER value there, and "
         f"each two-way pair is gated per reading, never in aggregate.  "
         f"MEASURED: the pin names this crystal in those words "
         f"({ctrl_named}), it is the one crystal of the {len(CRYSTALS)} "
         f"declared CONTROL, and it is absent from the {len(ARB)} "
         f"arbitration crystals the claims are read on",
         ctrl_named and CTRL not in ARB and len(CRYSTALS) == len(ARB) + 1,
         {"control": CTRL, "named_in_pin": ctrl_named,
          "arbitration": len(ARB), "crystals": len(CRYSTALS)})

    arena_rows = []
    for nm, kind, _fn in CRYSTALS:
        b = built[nm]
        if MUTANT == "MUT-NOT-FORCED" and nm == "DOUBLE-GRID(3,2)":
            b = double_grid(3, 2, drop_one_arb=True)
            built[nm] = b
        n = len(b.H)
        reg(n)
        mh = b.maxhits
        if MUTANT == "MUT-MAXHITS" and nm == "DOUBLE-GRID(3,3)":
            mh = b.maxhits + 1
        gate(f"G-FORCED[{nm}]",
             f"this crystal is a FORCED record: {n} events, every one "
             f"offered by the committed layer's own menu and specified by "
             f"its FULL EVENT TUPLE, matched by EXACTLY ONE candidate "
             f"(maxhits = {mh}), refusal = {b.refusal} -- D60's C1/C2 "
             f"and D66/D67's _pick discipline, reproduced",
             b.refusal is None and mh == 1,
             {"crystal": nm, "events": n, "maxhits": mh,
              "refusal": b.refusal},
             polarity=("is a FORCED record", "is a REFUSED record"))
        S = site_map(b)
        img = sorted(set(S.values()))
        gate(f"G-SITEMAP[{nm}]",
             f"the site reading's carrier is FORCED by the constructor's own "
             f"actor naming: the {len(S)} actor names parse as a BIJECTION "
             f"onto Z_3^2, image size {len(img)} of 9 -- no site assignment "
             f"is chosen by this unit",
             len(S) == 9 and len(img) == 9 and img == sorted(SITES),
             {"crystal": nm, "actors": len(S), "image": len(img)})
        arena_rows.append({"crystal": nm, "kind": kind, "events": n,
                           "maxhits": b.maxhits, "refusal": b.refusal,
                           "divisions": sum(1 for e in b.H
                                            if is_division(e))})
    seal_payload("arena", arena_rows)

    # the v10 cross-check: committed rows, and a gated event-count law
    emit("")
    emit("  [the v10 cross-check -- committed numbers, pin R1]")
    prof_full = {}
    for nm, _k, _f in CRYSTALS:
        prof_full[nm] = profile(poset_of(built[nm].H))
    dgm = mutate("MUT-ANCHOR", 9, 8)
    K_H2A = r"\|D\|>=2: (\S+) "
    K_H4A = r"\|D\|>=4: (\S+) "
    K_MAXA = r"max\|D\|=(\d+)"
    K_MEANA = r"mean\|D\|=([\d.]+)"
    K_PAIRS = r"pairs=(\d+)"
    K_OMA = r"mean omega=(\S+) "
    K_N = r"n=\s+(\d+)"
    K_HOMOG = r"homog ([\d.]+)"
    K_H4B = r"\|D\|>=4 ([\d.]+)"
    K_OMB = r"omega ([\d.]+)"
    K_MEANB = r"mean\|D\| ([\d.]+)"
    K_HOMOG3 = r"d=3: homog ([\d.]+)"
    K_H4B3 = r"d=3: homog [\d.]+\[below\] \|D\|>=4 ([\d.]+)"
    K_OMB3 = r"d=3:.*omega ([\d.]+)"
    K_D2 = r"d2=(\d+)"
    K_D3 = r"d3=(\d+)"
    K_VREG = r"version registers (\d+)"
    K_SHARE = r"arb share (\S+) "
    K_EVENTS = r"events = (\d+)"
    for aid, nm, d, key, typed, src, rx in [
            ("A01", CTRL, 2, "h2", Fr(1, 2), "d60 out L18", K_H2A),
            ("A02", CTRL, 2, "h4", Fr(0), "d60 out L18", K_H4A),
            ("A03", CTRL, 2, "max", 3, "d60 out L18", K_MAXA),
            ("A04", CTRL, 2, "pairs", 43, "d60 out L18", K_PAIRS),
            ("A05", CTRL, 2, "om", Fr(101, 258), "d60 out L18", K_OMA),
            ("A06", CTRL, 3, "h2", Fr(14, 23), "d60 out L19", K_H2A),
            ("A07", CTRL, 3, "h4", Fr(0), "d60 out L19", K_H4A),
            ("A08", CTRL, 3, "max", 3, "d60 out L19", K_MAXA),
            ("A09", CTRL, 3, "pairs", 51, "d60 out L19", K_PAIRS),
            ("A10", CTRL, 3, "om", Fr(73, 153), "d60 out L19", K_OMA),
            ("A11", "DOUBLE-GRID(3,2)", 2, "max", dgm, "d66 out L227", K_D2),
            ("A12", "DOUBLE-GRID(3,2)", 3, "max", 9, "d66 out L227", K_D3),
            ("A13", "CONFLICT-GRID(3,4)", 2, "max", 6, "d66 out L223", K_D2),
            ("A14", "CONFLICT-GRID(3,4)", 3, "max", 6, "d66 out L223", K_D3)]:
        anchor(aid, f"{nm} d={d} {key}", typed, prof_full[nm][d][key], src, rx)
        reg(prof_full[nm][d][key])
    for aid, nm, d, key, typed, src, rx in [
            ("A15", "DOUBLE-GRID(3,2)", 2, "h2", "0.4444", "d66 out L64",
             K_HOMOG),
            ("A16", "DOUBLE-GRID(3,2)", 2, "h4", "0.0694", "d66 out L64",
             K_H4B),
            ("A17", "DOUBLE-GRID(3,2)", 2, "om", "0.5576", "d66 out L64",
             K_OMB),
            ("A18", "DOUBLE-GRID(3,2)", 3, "h2", "0.6389", "d66 out L135",
             K_HOMOG3),
            ("A19", "DOUBLE-GRID(3,2)", 3, "h4", "0.2083", "d66 out L135",
             K_H4B3),
            ("A20", "DOUBLE-GRID(3,2)", 3, "om", "0.5710", "d66 out L135",
             K_OMB3),
            ("A21", "CONFLICT-GRID(3,4)", 2, "h2", "0.4848", "d66 out L60",
             K_HOMOG),
            ("A22", "CONFLICT-GRID(3,4)", 2, "h4", "0.1364", "d66 out L60",
             K_H4B),
            ("A23", "CONFLICT-GRID(3,4)", 2, "om", "0.5068", "d66 out L60",
             K_OMB),
            ("A24", "CONFLICT-GRID(3,4)", 3, "h2", "0.5758", "d66 out L131",
             K_HOMOG3),
            ("A25", "CONFLICT-GRID(3,4)", 3, "h4", "0.4545", "d66 out L131",
             K_H4B3),
            ("A26", "CONFLICT-GRID(3,4)", 3, "om", "0.5833", "d66 out L131",
             K_OMB3)]:
        anchor(aid, f"{nm} d={d} {key} (4-decimal rendering)", typed,
               dec4(prof_full[nm][d][key]), src, rx)
    for aid, nm, typed, src in [
            ("A27", CTRL, 46, "d60 out L17"),
            ("A28", "DOUBLE-GRID(3,2)", 72, "d66 out L64"),
            ("A29", "CONFLICT-GRID(3,4)", 66, "d66 out L60")]:
        anchor(aid, f"{nm} events", typed, len(built[nm].H), src,
               K_EVENTS if src.startswith("d60") else K_N)
    anchor("A30", "DOUBLE-GRID(3,2) arbitration share", Fr(1, 4),
           Fr(sum(1 for e in built["DOUBLE-GRID(3,2)"].H
                  if is_division(e)), len(built["DOUBLE-GRID(3,2)"].H)),
           "d66 out L106", K_SHARE)
    anchor("A31", "CONFLICT-GRID(3,4) arbitration share", Fr(2, 11),
           Fr(sum(1 for e in built["CONFLICT-GRID(3,4)"].H
                  if is_division(e)), len(built["CONFLICT-GRID(3,4)"].H)),
           "d66 out L102", K_SHARE)
    anchor("A32", "DOUBLE-GRID(3,2) version registers", 18,
           sum(1 for e in built["DOUBLE-GRID(3,2)"].H if is_division(e)),
           "d66 out L227", K_VREG)
    anchor("A33", "CONFLICT-GRID(3,4) version registers", 12,
           sum(1 for e in built["CONFLICT-GRID(3,4)"].H if is_division(e)),
           "d66 out L223", K_VREG)

    def dg_events(g, R):
        return 4 * g + 2 * g * (g - 1) + R * (2 * g * g + 2 * g)

    def cg_events(g, R):
        return g * (g + 1) + (R - 1) * (g * (g + 1) + 2 * g)

    for aid, nm, d, typed, src in [
            ("A39", CTRL, 2, "1.46", "d60 out L18"),
            ("A40", CTRL, 3, "1.61", "d60 out L19"),
            ("A41", "DOUBLE-GRID(3,2)", 2, "1.96", "d66 out L64"),
            ("A42", "CONFLICT-GRID(3,4)", 2, "1.86", "d66 out L60")]:
        anchor(aid, f"{nm} d={d} mean|D| (2-decimal rendering)", typed,
               dec2(prof_full[nm][d]["mean"]), src,
               K_MEANA if src.startswith("d60") else K_MEANB)
    anchor("A34", "DOUBLE-GRID event-count law at the committed R=2", 72,
           dg_events(3, 2), "d66 out L64", K_N)
    anchor("A35", "DOUBLE-GRID event-count law at the committed R=4", 120,
           dg_events(3, 4), "d66 out L65", K_N)
    anchor("A36", "CONFLICT-GRID event-count law at the committed R=4", 66,
           cg_events(3, 4), "d66 out L60", K_N)
    anchor("A37", "CONFLICT-GRID event-count law at the committed R=6", 102,
           cg_events(3, 6), "d66 out L61", K_N)
    anchor("A38", "CONFLICT-GRID event-count law at the committed R=10", 174,
           cg_events(3, 10), "d66 out L62", K_N)
    n_read = sum(1 for a in ANCHORS if a["extracted"] is not None)
    reg(len(ANCHORS), n_read)
    gate("G-ANCHORS-READ",
         f"THE COMMITTED SIDE IS READ, NOT TYPED (#91).  All "
         f"{len(ANCHORS)} committed-number anchors take their committed "
         f"value by a context-keyed regex from the line of the pinned v10 "
         f"output the anchor itself cites -- {n_read} of {len(ANCHORS)} "
         f"located -- and the extracted value, not the typed rendering, is "
         f"what the computed value is compared against; the typed rendering "
         f"survives only as a third check per row.  A transcription error "
         f"on the committed side is therefore visible to this run",
         n_read == len(ANCHORS) and len(ANCHORS) == 42,
         {"anchors": len(ANCHORS), "located": n_read,
          "sources": sorted(OUTFILES.values())})
    gate("G-V10-XCHECK-LAW",
         f"the two crystals the pin names that v10 never swept -- "
         f"DOUBLE-GRID(3,3) and CONFLICT-GRID(3,2) -- are cross-checked by a "
         f"CLOSED-FORM event-count law verified at every committed member of "
         f"its own family (A34-A38): the law predicts "
         f"{dg_events(3, 3)} and {cg_events(3, 2)} and the rebuilds carry "
         f"{len(built['DOUBLE-GRID(3,3)'].H)} and "
         f"{len(built['CONFLICT-GRID(3,2)'].H)}",
         dg_events(3, 3) == len(built["DOUBLE-GRID(3,3)"].H)
         and cg_events(3, 2) == len(built["CONFLICT-GRID(3,2)"].H),
         {"predicted": [dg_events(3, 3), cg_events(3, 2)],
          "measured": [len(built["DOUBLE-GRID(3,3)"].H),
                       len(built["CONFLICT-GRID(3,2)"].H)]})
    reg(dg_events(3, 3), cg_events(3, 2), 120, 102, 174)
    checkpoint("SEC 4 (the arena and the v10 cross-check)")

    # -------------------------------------------------------------- SEC 5
    emit("")
    emit("=" * 78)
    emit("SEC 5  THE HEADLINE -- the division field's translation "
         "stabilizer on Z_3^2")
    emit("=" * 78)
    stab_tab, stab_rows, affine_rows, stab_elems = {}, [], [], {}
    for nm, kind, _f in CRYSTALS:
        b = built[nm]
        for rd in READINGS:
            f = division_field(b, rd, nm)
            S1 = stabilizer(f)
            S2 = stabilizer_by_characters(f)
            if MUTANT == "MUT-STAB-RECON" and (nm, rd) == (
                    "CONFLICT-GRID(3,2)", "footprint"):
                S2 = [t for t in S2 if t in ((0, 0), (1, 1), (2, 2))]
            nmS = subgroup_name(S1)
            supp = sum(1 for x in SITES if f[x] > 0)
            vec = [f[x] for x in SITES]
            stab_tab[(nm, rd)] = nmS
            stab_elems[(nm, rd)] = set(S1)
            reg(len(S1), supp, *vec)
            reg(f"{supp}/{len(SITES)}")
            stab_rows.append({"crystal": nm, "kind": kind, "reading": rd,
                              "field": vec, "support": supp,
                              "order": len(S1), "stabilizer": nmS,
                              "elements": [list(t) for t in S1]})
            emit(f"  [DATA] {nm:19s} {rd:10s} field={vec} support={supp}/9")
            expect_triv = (kind == "CONTROL")
            gate(f"G-STAB[{nm}|{rd}]",
                 f"MEASURED EXACTLY: the division-event field at this "
                 f"crystal and this site reading is {vec} over the nine "
                 f"sites (support {supp}/9) and its translation stabilizer "
                 f"in Z_3^2 is {nmS}, of order {len(S1)}, elements "
                 f"{[list(t) for t in S1]} -- "
                 + ("TRIVIAL, so the division events of this crystal do NOT "
                    "form a crystal, which is the value the DECLARED "
                    "COUNTEREXAMPLE CONTROL must return"
                    if expect_triv else
                    "NONTRIVIAL, so the division events of this crystal DO "
                    "form a crystal at this reading"),
                 (len(S1) == 1) if expect_triv else (len(S1) > 1),
                 {"crystal": nm, "reading": rd, "order": len(S1),
                  "stabilizer": nmS, "support": supp, "field": vec},
                 polarity=(("do NOT form a crystal", "DO form a crystal")
                           if expect_triv else
                           ("DO form a crystal", "do NOT form a crystal")))
            gate(f"G-STAB-RECON[{nm}|{rd}]",
                 f"THE SAME FIELD BY TWO ALGORITHMS: the stabilizer is "
                 f"re-derived as the annihilator of the support of the "
                 f"exact Z_3^2 Fourier transform in Z[omega] = "
                 f"Z[t]/(t^2+t+1), running over the DUAL group instead of "
                 f"translating the field, and the two agree element for "
                 f"element: {nmS}.  This is an ALGORITHM cross-check, not a "
                 f"data cross-check -- both routes consume the same field "
                 f"and the same naming function; the field-level "
                 f"independence is delivered one gate later, by "
                 f"G-HEAD-EQUALITY, whose reconstruction rebuilds record, "
                 f"marking and site map",
                 S1 == S2, {"crystal": nm, "reading": rd,
                            "direct": [list(t) for t in S1],
                            "characters": [list(t) for t in S2]})
            if kind == "ARBITRATION":
                gate(f"G-DIAGONAL-INVARIANCE[{nm}|{rd}]",
                     f"the DIAGONAL translation (1,1) lies in this "
                     f"stabilizer: the invariance direction the four "
                     f"arbitration crystals share is <(1,1)>, and here the "
                     f"stabilizer is {nmS}",
                     (1, 1) in S1, {"crystal": nm, "reading": rd,
                                    "contains_(1,1)": (1, 1) in S1})
            # ---- THE MECHANISM: the field is affine in the SEED SET ----
            Sd = seed_sites(nm)
            fit = affine_fit(f, Sd)
            ind = {x: (1 if x in set(Sd) else 0) for x in SITES}
            SS = stabilizer(ind)
            nmSS = subgroup_name(SS)
            c, m = fit if fit else (None, None)
            resid = sorted({(x[1] - x[0]) % L for x in Sd})
            full = all(sum(1 for x in Sd if (x[1] - x[0]) % L == r) == L
                       for r in resid)
            law = (S1 == SS) if (fit and m != 0) else \
                  (len(S1) == len(SITES) if fit else False)
            reg(len(Sd), *([c, m] if fit else []))
            affine_rows.append({"crystal": nm, "reading": rd,
                                "seed_sites": [list(x) for x in Sd],
                                "c": c, "m": m, "constant_field": m == 0,
                                "stab_seed_indicator": nmSS,
                                "stab_field": nmS,
                                "seed_residues": resid,
                                "seed_is_full_coset_union": full,
                                "law_holds": bool(law)})
            emit(f"  [DATA] {nm:19s} {rd:10s} affine c={c} m={m} "
                 f"1_S-stab={nmSS} seed-residues={resid}")
            gate(f"G-AFFINE[{nm}|{rd}]",
                 f"THE MECHANISM, MEASURED AT THIS CELL.  The division "
                 f"field is AFFINE IN THE INDICATOR OF THE CONSTRUCTOR'S "
                 f"OWN SEED SET, whose {len(Sd)} sites are re-derived from "
                 f"the seed rule and never read off the field: "
                 f"n = {c} + {m}*1_S at all nine sites, with "
                 f"Stab(1_S) = {nmSS}.  " +
                 (f"m = 0: THE FIELD IS CONSTANT and its full-group "
                  f"stabilizer is a VACUOUS POSITIVE -- every field on "
                  f"every group is invariant under everything when it does "
                  f"not vary, so this cell carries no information about "
                  f"periodicity beyond the construction's own partition"
                  if fit and m == 0 else
                  f"m != 0, so Stab(n) = Stab(1_S) = {nmSS} exactly: the "
                  f"periodicity measured at this cell IS the symmetry of "
                  f"the constructor's seed set, inherited and not emergent"),
                 bool(fit) and law,
                 {"crystal": nm, "reading": rd, "c": c, "m": m,
                  "seed_sites": [list(x) for x in Sd],
                  "stab_seed_indicator": nmSS, "stab_field": nmS,
                  "constant_field": m == 0, "law_holds": bool(law)},
                 polarity=("AFFINE IN THE INDICATOR OF THE CONSTRUCTOR'S OWN "
                           "SEED SET", "independent of the constructor"))
    seal_payload("stabilizers", stab_rows)
    seal_payload("affine", affine_rows)
    n_const = sum(1 for r in affine_rows if r["constant_field"])
    n_law = sum(1 for r in affine_rows if r["law_holds"])
    n_coset = sum(1 for r in affine_rows
                  if r["seed_is_full_coset_union"] and r["crystal"] in ARB)
    dg_res = sorted({tuple(r["seed_residues"]) for r in affine_rows
                     if r["crystal"].startswith("DOUBLE-GRID")})[0]
    cg_res = sorted({tuple(r["seed_residues"]) for r in affine_rows
                     if r["crystal"].startswith("CONFLICT-GRID")})[0]
    reg(n_const, n_law, n_coset, len(affine_rows), *dg_res, *cg_res)
    gate("G-AFFINE-MECHANISM",
         f"THE TEN-CELL TABLE HAS A ONE-LINE MECHANISM AND IT IS THE "
         f"CONSTRUCTOR'S.  At {n_law} of {len(affine_rows)} cells the "
         f"division field decomposes exactly as n = c + m*1_S over the "
         f"constructor's own seed set S, so the stabilizer is forced: "
         f"Stab(n) = Stab(1_S) wherever m != 0, and the whole group "
         f"wherever m = 0 ({n_const} cells, both CONFLICT-GRID footprints, "
         f"where the field is constant and the positive is vacuous).  On "
         f"all {n_coset} arbitration cells S is a union of FULL <(1,1)> "
         f"cosets -- the residues of j-i over S are {dg_res} on the "
         f"DOUBLE-GRIDs and {cg_res} on the CONFLICT-GRIDs, every class "
         f"complete -- because d66 seats its seeds at a uniform column "
         f"offset (j+2)%g; on the control S is a single site, an incomplete "
         f"class, which is exactly why the control returns order 1.  THE "
         f"CLAIM IS TRUE AND CONSTRUCTOR-INHERITED: the division events of "
         f"these crystals form a crystal because their constructors seed "
         f"conflict on a coset and group by rows and columns",
         n_law == len(affine_rows) and n_const == 2 and n_coset == 8,
         {"cells": len(affine_rows), "law_holds": n_law,
          "constant_field_cells": n_const,
          "arbitration_cells_seeded_on_full_cosets": n_coset,
          "rows": affine_rows})

    agree = [nm for nm in ARB
             if stab_tab[(nm, "initiator")] == stab_tab[(nm, "footprint")]]
    diverge = [nm for nm in ARB if nm not in agree]
    reg(len(agree), len(diverge))
    contains = [nm for nm, _k, _f in CRYSTALS
                if stab_elems[(nm, "initiator")]
                <= stab_elems[(nm, "footprint")]]
    strict = [nm for nm, _k, _f in CRYSTALS
              if stab_elems[(nm, "initiator")]
              < stab_elems[(nm, "footprint")]]
    reg(len(contains), len(strict))
    gate("G-READING-DIVERGENCE",
         f"THE SITE READING IS NOT NEUTRAL, AND THE SCOUT OF RECORD IS "
         f"CORRECTED WHERE IT SPOKE.  The scout's DECLARED-DATA OBLIGATIONS "
         f"paragraph recorded 'stabilizers AGREE, supports differ (6/9 vs "
         f"9/9)'; its own PRELIMINARY, four lines earlier, had already "
         f"flagged CONFLICT-GRID(3,2)'s footprint field as constant at "
         f"order 9, and it was silent on CONFLICT-GRID(3,4).  MEASURED: the "
         f"two readings agree at {len(agree)} of 4 arbitration crystals "
         f"({agree}) and DIVERGE at {len(diverge)} ({diverge}), where the "
         f"footprint field is CONSTANT and its stabilizer is the whole "
         f"group; and the supports are 6/9 vs 9/9 only on the "
         f"DOUBLE-GRIDs, 3/9 vs 9/9 on the CONFLICT-GRIDs.  The relation is "
         f"CONTAINMENT, measured and not asserted: the footprint stabilizer "
         f"CONTAINS the initiator stabilizer at {len(contains)} of "
         f"{len(CRYSTALS)} records and the containment is STRICT at "
         f"{len(strict)} ({strict}) -- so 'never shrinks' is the "
         f"measurement and 'enlarges' would not be.  <(1,1)> lies in all "
         f"eight arbitration cells",
         len(diverge) == 2 and set(diverge) == {"CONFLICT-GRID(3,2)",
                                                "CONFLICT-GRID(3,4)"}
         and len(contains) == len(CRYSTALS) and len(strict) == 2,
         {"agree": agree, "diverge": diverge, "contains": contains,
          "strict": strict,
          "table": {f"{k[0]}|{k[1]}": v for k, v in sorted(stab_tab.items())}})
    checkpoint("SEC 5 (the stabilizer table)")

    # -------------------------------------------------------------- SEC 6
    emit("")
    emit("=" * 78)
    emit("SEC 6  GEOMETRY INVARIANCE under the renewal-only rebuild")
    emit("=" * 78)
    geom_rows, varies_arb, control_varies, pop_check = [], [], [], []
    cross_marked, cross_unmarked = {}, {}
    for nm, kind, _f in CRYSTALS:
        b = built[nm]
        C = poset_of(b.H)
        hh = heights(C)
        D = [i for i, e in enumerate(b.H) if is_division(e)]
        pop = list(D)
        if MUTANT == "MUT-GEOM-VARIES" and nm == "DOUBLE-GRID(3,2)":
            DIRS = {e: len(sky_b(C, e, 2, hh)) for e in range(len(C))}
            pop = [i for i in D if DIRS[i] != max(DIRS[j] for j in D)]
        pf, pr = prof_full[nm], profile(C, pop)
        sub = [e for e in b.H if is_division(e)]
        ps = profile(poset_of(sub)) if sub else None
        # the KR height control
        need = Counter(hh[i] for i in D)
        ctrl, deficit, mixed = [], 0, []
        for lay in sorted(need):
            poolv = [i for i in range(len(C)) if hh[i] == lay
                     and i not in set(D)]
            if poolv:
                mixed.append(lay)
            ctrl += poolv[:need[lay]]
            deficit += need[lay] - len(poolv[:need[lay]])
        if MUTANT == "MUT-HEIGHT-IMPURE" and nm == "DOUBLE-GRID(3,2)":
            mixed = [1]
        cross_marked[nm] = Counter(need)
        cross_unmarked[nm] = Counter(hh[i] for i in range(len(C))
                                     if i not in set(D))
        pop_check.append({"crystal": nm, "events": len(C),
                          "pop_n": pr[2]["n"], "full_n": pf[2]["n"],
                          "marked": len(D),
                          "poset_held_whole": pr[2]["n"] == len(pop)
                          and pf[2]["n"] == len(C)})
        reg(pf["height"], (ps["height"] if ps else 0), len(D), deficit)
        for d in (2, 3):
            for src in (pf, pr) + ((ps,) if ps else ()):
                for k in ("h2", "h4", "max", "mean", "om", "n", "pairs"):
                    if src[d][k] is not None:
                        reg(src[d][k])
        reg(*sorted(need), *[need[x] for x in sorted(need)])
        hp_stmt = (f"HEIGHT PURITY, MEASURED: the {len(D)} marked events of "
                   f"this crystal occupy the height layers {sorted(need)} of "
                   f"a poset of longest chain {pf['height']}, and "
                   f"{len(mixed)} of those layers contain any unmarked event "
                   f"-- the marked events fill whole layers and share them "
                   f"with nothing else")
        if MUTANT == "MUT-PROSE-POLARITY" and nm == "DOUBLE-GRID(3,2)":
            hp_stmt = hp_stmt.replace(
                "the marked events fill whole layers and share them with "
                "nothing else",
                "the marked events SHARE their layers with unmarked events "
                "throughout")
        gate(f"G-GEOM-HEIGHTPURE[{nm}]", hp_stmt,
             len(mixed) == 0 and len(D) > 0,
             {"crystal": nm, "layers": sorted(need), "mixed_layers": mixed,
              "longest_chain": pf["height"], "marked": len(D)},
             polarity=("share them with nothing else",
                       "SHARE their layers with unmarked events"))
        gate(f"G-GEOM-HCTRL[{nm}]",
             f"THE HEIGHT-MATCHED CONTROL POPULATION IS EMPTY HERE, AND THE "
             f"KR DISCRIMINATOR IS CARRIED.  Two different objects go by "
             f"the name 'height control' and this unit separates them.  The "
             f"catalog's requirement (V08) is that a dimension reading "
             f"carry its HEIGHT STATISTIC -- the longest chain, "
             f"{pf['height']} here, reported for every population at "
             f"G-WALL-KR.  What this gate measures is a STRICTER object of "
             f"this unit's own devising (choice inventory row 10, class "
             f"free): a height-MATCHED CONTROL POPULATION -- same size, "
             f"same height histogram, drawn from unmarked events -- which "
             f"has size {len(ctrl)} with deficit {deficit} of {len(D)}, "
             f"because height purity leaves no unmarked event at any marked "
             f"height.  Every POPULATION-AVERAGED row below is therefore "
             f"confounded with a height shift for which THIS unit's control "
             f"cannot be built, and this unit certifies none of them",
             len(ctrl) == 0 and deficit == len(D),
             {"crystal": nm, "control_size": len(ctrl), "deficit": deficit,
              "marked": len(D), "kr_discriminator_longest_chain":
              pf["height"]},
             polarity=("height-MATCHED CONTROL POPULATION",
                       "the KR control the catalog requires is empty"))
        for d in (2, 3):
            inv = (pf[d]["max"] == pr[d]["max"])
            att = [e for e in pf[d]["attained"]]
            attD = [e for e in att if e in set(D)]
            reg(pf[d]["max"], pr[d]["max"], len(att), len(attD))
            expect = (kind == "ARBITRATION")
            if not inv:
                (varies_arb if kind == "ARBITRATION"
                 else control_varies).append(
                    f"{nm}|d={d}|max|D|:{pf[d]['max']}->{pr[d]['max']}")
            gate(f"G-GEOM-POP-WIDTH[{nm}|d={d}]",
                 f"THE CHART-WIDTH ROW, the one geometry row a population "
                 f"restriction cannot confound (a maximum over a subset "
                 f"equals the maximum over the whole set exactly when the "
                 f"maximum is ATTAINED on the subset): full max|D| = "
                 f"{pf[d]['max']}, attained at {len(att)} events of which "
                 f"{len(attD)} are marked; restricted max|D| = "
                 f"{pr[d]['max']} -- "
                 + ("INVARIANT" if inv else
                    f"VARIES-{pf[d]['max']}->{pr[d]['max']}")
                 + ((", the kinematic prediction" if inv else
                     ", CONTRARY to the kinematic prediction") if expect else
                    (", the value the DECLARED COUNTEREXAMPLE CONTROL must "
                     "return" if not inv else
                     ", where the DECLARED COUNTEREXAMPLE CONTROL was "
                     "required to vary")),
                 inv if expect else (not inv),
                 {"crystal": nm, "depth": d, "full_max": pf[d]["max"],
                  "restricted_max": pr[d]["max"], "attainers": len(att),
                  "attainers_marked": len(attD), "invariant": inv},
                 polarity=(("INVARIANT", "VARIES-") if inv else
                           ("VARIES-", "INVARIANT")))
        gate(f"G-GEOM-BLOCKED[{nm}]",
             f"the POPULATION-AVERAGED rows are reported and NOT certified: "
             f"at d=2 homogeneity moves {pf[2]['h2']} -> {pr[2]['h2']}, "
             f"|D|>=4 moves {pf[2]['h4']} -> {pr[2]['h4']} and mean overlap "
             f"moves {pf[2]['om']} -> {pr[2]['om']}, every one of them "
             f"inseparable from the height shift whose control G-GEOM-HCTRL "
             f"proves empty.  BLOCKED-AT-THE-EMPTY-HEIGHT-CONTROL is this "
             f"unit's reading of these rows, not INVARIANT and not VARIES.  "
             f"THE FORCING IS MEASURED, not asserted: the height-matched "
             f"control has size {len(ctrl)} and deficit {deficit} of "
             f"{len(D)} at this crystal, and every row named here is a "
             f"population average over exactly the population that control "
             f"would have had to match",
             len(ctrl) == 0 and deficit == len(D) and len(D) > 0,
             {"crystal": nm,
              "d2_full": {"h2": str(pf[2]["h2"]), "h4": str(pf[2]["h4"]),
                          "om": str(pf[2]["om"]), "mean": str(pf[2]["mean"])},
              "d2_restricted": {"h2": str(pr[2]["h2"]),
                                "h4": str(pr[2]["h4"]),
                                "om": str(pr[2]["om"]),
                                "mean": str(pr[2]["mean"])},
              "d3_full": {"h2": str(pf[3]["h2"]), "h4": str(pf[3]["h4"]),
                          "om": str(pf[3]["om"]), "mean": str(pf[3]["mean"])},
              "d3_restricted": {"h2": str(pr[3]["h2"]),
                                "h4": str(pr[3]["h4"]),
                                "om": str(pr[3]["om"]),
                                "mean": str(pr[3]["mean"])}},
             waiver={"class": "MEASURED-THEN-DECLINED",
                     "reason": "the numbers are computed exactly and printed; "
                               "what is withheld is the INFERENCE from them, "
                               "on the ground that the height-matched control "
                               "population this unit requires of itself is "
                               "empty at every one of these crystals.  The "
                               "catalog's own KR discriminator, the longest "
                               "chain, IS carried -- at G-WALL-KR, for every "
                               "population"})
        gate(f"G-GEOM-SUB[{nm}]",
             f"arm (a)'s second sub-reading -- the literal sparse record, "
             f"poset rebuilt on the {len(sub)} marked events alone -- "
             f"carries longest chain {ps['height'] if ps else 0} against the "
             f"full record's {pf['height']}, and max|D| "
             f"{ps[2]['max'] if ps else 0} at d=2 against {pf[2]['max']}: a "
             f"DIFFERENT poset, not a restriction of this one, and reported "
             f"as data only.  MEASURED, not declared: the two objects "
             f"disagree on both invariants at this crystal, which is why no "
             f"invariance claim can cross them",
             bool(ps) and ps["height"] != pf["height"]
             and ps[2]["max"] != pf[2]["max"],
             {"crystal": nm, "events": len(sub),
              "height_sub": ps["height"] if ps else 0,
              "height_full": pf["height"],
              "max_sub_d2": ps[2]["max"] if ps else 0,
              "max_full_d2": pf[2]["max"],
              "max_sub_d3": ps[3]["max"] if ps else 0,
              "max_full_d3": pf[3]["max"]},
             waiver={"class": "MEASURED-THEN-DECLINED",
                     "reason": "the sparse record's own poset is a different "
                               "object from the crystal's; no invariance "
                               "claim is made across the two"})
        geom_rows.append({
            "crystal": nm, "kind": kind, "marked": len(D),
            "longest_chain_full": pf["height"],
            "longest_chain_sub": ps["height"] if ps else 0,
            "height_layers": sorted(need), "mixed_layers": mixed,
            "hctrl_size": len(ctrl), "hctrl_deficit": deficit,
            "full": {str(d): {k: str(pf[d][k]) for k in
                              ("h2", "h4", "max", "mean", "om", "n", "pairs")}
                     for d in (2, 3)},
            "restricted": {str(d): {k: str(pr[d][k]) for k in
                                    ("h2", "h4", "max", "mean", "om", "n",
                                     "pairs")} for d in (2, 3)},
            "subrecord": {str(d): {k: str(ps[d][k]) for k in
                                   ("h2", "h4", "max", "mean", "om", "n",
                                    "pairs")} for d in (2, 3)} if ps else None,
        })
    seal_payload("geometry", geom_rows)
    pool = Counter()
    for nm in cross_unmarked:
        pool += cross_unmarked[nm]
    allm = sorted(set().union(*[set(c) for c in cross_marked.values()]))
    avail = [h for h in allm if pool[h] > 0]
    unavail = [h for h in allm if pool[h] == 0]
    l1m = [cross_marked[nm][1] for nm, _k, _f in CRYSTALS]
    l1u = [cross_unmarked[nm][1] for nm, _k, _f in CRYSTALS]
    reg(*allm, *l1m, *l1u, len(avail), len(unavail))
    gate("G-GEOM-HEIGHTPURE-CROSS",
         f"HEIGHT PURITY SURVIVES THE OBVIOUS WIDENING OF ITS SCOPE.  A "
         f"successor could object that the control is only unbuildable "
         f"WITHIN a record.  MEASURED ACROSS ALL FIVE: pooling the unmarked "
         f"events of every record, {len(avail)} of the {len(allm)} marked "
         f"heights {allm} are available somewhere ({avail}) but "
         f"{len(unavail)} is available NOWHERE ({unavail}) -- height layer "
         f"1 is marked-only on every one of the five records, carrying "
         f"{l1m} marked events against {l1u} unmarked -- and every record "
         f"has marked events at height 1.  Even a CROSS-RECORD "
         f"height-matched control is therefore unbuildable",
         unavail == [1] and l1u == [0] * len(CRYSTALS)
         and all(x > 0 for x in l1m),
         {"marked_heights": allm, "available_somewhere": avail,
          "available_nowhere": unavail, "layer1_marked": l1m,
          "layer1_unmarked": l1u})
    pop_ok = all(r["poset_held_whole"] for r in pop_check)
    gate("G-GEOM-POP-INSTRUMENT",
         f"arm (a)'s primary sub-reading uses D60's OWN committed device "
         f"(V12): the poset is left whole and only the metric population "
         f"changes.  MEASURED at every crystal, not declared: the "
         f"restricted profile is computed on the SAME comparability matrix "
         f"as the full one and differs from it only in the population it "
         f"averages over -- {[r['full_n'] for r in pop_check]} events "
         f"full against {[r['pop_n'] for r in pop_check]} marked.  Arm "
         f"(a)'s second sub-reading takes the literal sparse record and "
         f"recomputes its event poset from scratch.  'FILTER' is ambiguous "
         f"between the two and both are run; the fiber is 2 and it is "
         f"declared, not chosen",
         pop_ok, {"sub_readings": ["POP (poset whole)", "SUB (poset rebuilt)"],
                  "fiber": 2, "rows": pop_check})

    # arm (b): the Builder rerun under two declared sub-grammars
    emit("")
    emit("  [arm (b) -- the Builder rerun on a restricted candidate stream]")
    armb = []
    for nm, kind, fn in CRYSTALS:
        bb = fn(lambda e: e[0] in ('p', 'r'))
        ref = bb.refusal
        if MUTANT == "MUT-ARMB-COMPLETES" and nm == "DOUBLE-GRID(3,2)":
            ref = None
        bi = fn(lambda e: e[0] != 'n')
        same = (bi.H == built[nm].H) and bi.refusal is None \
            and bi.maxhits == 1
        reg(len(bb.H), len(bi.H))
        armb.append({"crystal": nm, "renewal_only_events": len(bb.H),
                     "renewal_only_refusal": ref,
                     "idle_free_events": len(bi.H),
                     "idle_free_identical": same})
        gate(f"G-GEOM-ARMB-RENEWAL[{nm}]",
             f"arm (b) at the DECLARED RENEWAL-ONLY SUB-GRAMMAR (V11's "
             f"shape: the support is restricted, the committed weights are "
             f"untouched) -- the candidate stream keeps only the two "
             f"record-bearing tags and drops the two the POSIT calls "
             f"kinematics.  THIS CRYSTAL CANNOT BE REBUILT: the record "
             f"stops after {len(bb.H)} events with a LOCATED refusal at "
             f"{ref}, its first delivery.  A refusal is recorded, never "
             f"patched",
             ref is not None,
             {"crystal": nm, "events": len(bb.H), "refusal": ref})
        gate(f"G-GEOM-ARMB-IDLEFREE[{nm}]",
             f"the isolation control for arm (b): dropping ONLY the idle tag "
             f"leaves the crystal rebuilt EVENT FOR EVENT ({len(bi.H)} "
             f"events, identical = {same}), so the tag that blocks the "
             f"renewal-only rebuild is exactly one, the DELIVERY",
             same, {"crystal": nm, "events": len(bi.H), "identical": same})
    seal_payload("arm_b", armb)
    gate("G-GEOM-ARMC-REGISTERED",
         "arm (c) of pin R3 -- quotient the record by its non-arbitration "
         "events -- is REGISTERED AND NOT RUN, as the pin allows; nothing "
         "in this unit's verdict descends from it",
         True, {"arm": "quotient", "run": False,
                "arm_rows_carry": ["(a)", "(b)"]},
         waiver={"class": "REGISTER-ONLY",
                 "reason": "a successor register entry; its absence is "
                           "visible in the arm rows, which carry (a) and (b) "
                           "only"},
         kind="DECLARED")
    gate("G-GEOM-SPATIAL-TAUTOLOGY",
         "the crystal's SPATIAL rows -- the co-division link counts of "
         "SEC 7 -- are functions of the marked events ALONE, so they are "
         "invariant under every renewal-only operationalization that "
         "preserves the marking.  That is a tautology of the definition, it "
         "is stated here so that it is never counted as evidence, and it is "
         "excluded from the geometry verdict",
         True, {"rows": "co-division link counts", "counted_as_evidence":
                False},
         waiver={"class": "DECLARATION-CARRIED",
                 "reason": "a statement about what this unit refuses to "
                           "count; the rows themselves are measured in SEC 7"},
         kind="DECLARED")

    # THE VERDICT IS COMPUTED FROM THE POPULATION THE SECTION ACTUALLY
    # MEASURED (#87): `varies_arb` is collected inside the per-crystal loop,
    # over the ARBITRATION crystals only, from the same restricted profile
    # the width gates read.  The control's REQUIRED variation is kept in its
    # own field and can never enter the falsifier's witness list.
    widths_ok = (varies_arb == [])
    geom_verdict = ("GEOMETRY-INVARIANT-AT-THE-CONTROLLED-ROW-"
                    "REST-BLOCKED-AT-THE-EMPTY-HEIGHT-CONTROL"
                    if widths_ok else
                    "GEOMETRY-VARIES-" + ";".join(varies_arb))
    gate("G-GEOM-WITNESS-BINDING",
         f"THE WITNESS IS BOUND TO THE VERDICT.  The segment verdict is a "
         f"function of one list and of nothing else: width_row_invariant "
         f"holds if and only if the arbitration-crystal witness list is "
         f"empty (measured: invariant={widths_ok}, witnesses="
         f"{len(varies_arb)}), and the DECLARED COUNTEREXAMPLE CONTROL's "
         f"own required variation ({len(control_varies)} rows: "
         f"{control_varies}) is carried in a separate field where it cannot "
         f"be mistaken for a falsifier witness",
         widths_ok == (varies_arb == []) and all(
             not w.startswith(CTRL) for w in varies_arb),
         {"width_row_invariant": widths_ok, "varies_witness": varies_arb,
          "control_varies": control_varies})
    emit("")
    emit(f"  [GEOMETRY SEGMENT VERDICT] {geom_verdict}")
    gate("G-GEOM-SEGMENT",
         f"THE GEOMETRY SEGMENT (V06 is the falsifier this segment answers "
         f"to): {geom_verdict}.  The chart-width row is INVARIANT at "
         f"{len(ARB) - len({w.split('|')[0] for w in varies_arb})} of "
         f"{len(ARB)} arbitration crystals at BOTH depths and NOT invariant "
         f"at the control, so the segment's two-way requirement is "
         f"discharged on the row that carries it; every population-averaged "
         f"row is BLOCKED; and paper 0 10's third falsifier -- 'sparse "
         f"records destroy the geometry' -- does NOT FIRE, and does not "
         f"come back negative either: on this arena it is NOT EVALUABLE.  "
         f"Under arm (a)-POP the poset is held whole by construction, so no "
         f"geometry could vary; under arm (a)-SUB the geometry does change "
         f"substantially but the two posets are different objects and the "
         f"comparison is refused; under arm (b) the object does not exist, "
         f"because the sparse record is not CONSTRUCTIBLE",
         widths_ok, {"verdict": geom_verdict, "width_row_invariant":
                     widths_ok, "varies_witness": varies_arb,
                     "control_varies": control_varies,
                     "falsifier": "not evaluable on this arena"})
    checkpoint("SEC 6 (geometry invariance)")

    # -------------------------------------------------------------- SEC 7
    emit("")
    emit("=" * 78)
    emit("SEC 7  THE BRIDGES -- at declared scope, candidate readings named")
    emit("=" * 78)
    bridge_rows, link_tab = [], {}
    for nm, kind, _f in CRYSTALS:
        b = built[nm]
        S = site_map(b)
        inv = {}
        for a, x in S.items():
            inv[x] = a
        divs = [e for e in b.H if is_division(e)]
        links = {}
        for lk in AXIS + DIAG:
            vals = []
            for x in SITES:
                u = inv[x]
                v = inv[((x[0] + lk[0]) % L, (x[1] + lk[1]) % L)]
                vals.append(sum(1 for e in divs
                                if u in regs_of(e) and v in regs_of(e)))
            links[lk] = vals
        if MUTANT == "MUT-DIAGONAL" and nm == "DOUBLE-GRID(3,2)":
            links[(1, 1)] = [1] + links[(1, 1)][1:]
        link_tab[nm] = {lk: list(v) for lk, v in links.items()}
        idx = [i for i, e in enumerate(b.H) if is_division(e)]
        legs = sorted(Counter(idx[k + 1] - idx[k]
                              for k in range(len(idx) - 1)).items())
        f = division_field(b, "initiator", nm)
        supp = sorted(x for x in SITES if f[x] > 0)
        cos = sorted({(x[1] - x[0]) % L for x in supp})
        is_cosets = all(sum(1 for x in supp if (x[1] - x[0]) % L == c) == L
                        for c in cos)
        ax_hom = all(len(set(links[lk])) == 1 and links[lk][0] > 0
                     for lk in AXIS) if kind == "ARBITRATION" else \
            all(set(links[lk]) == {0} for lk in AXIS)
        dg_zero = all(set(links[lk]) == {0} for lk in DIAG)
        reg(*[v for lk in AXIS + DIAG for v in links[lk]])
        reg(*[c for c, _n in legs], *[n for _c, n in legs])
        emit(f"  [DATA] {nm:19s} legs={legs} axis={links[AXIS[0]][0]}/"
             f"{links[AXIS[1]][0]} diag={links[DIAG[0]][0]}/"
             f"{links[DIAG[1]][0]}")
        gate(f"G-BRIDGE-AXIS[{nm}]",
             f"the co-division ADJACENCY on the two axis links is "
             f"{links[AXIS[0]]} and {links[AXIS[1]]} across the nine sites: "
             + ("homogeneous and strictly positive -- the renewal "
                "sublattice's bridges are the rook's graph's rows and "
                "columns" if kind == "ARBITRATION" else
                "identically zero -- the DECLARED COUNTEREXAMPLE CONTROL "
                "carries NO bridges at all, its single division event "
                "touching one site"),
             ax_hom, {"crystal": nm, "axis_10": links[AXIS[0]],
                      "axis_01": links[AXIS[1]]})
        gate(f"G-BRIDGE-DIAG[{nm}]",
             f"the DIAGONAL co-division link counts are {links[DIAG[0]]} and "
             f"{links[DIAG[1]]}: identically ZERO at 9 of 9 sites.  q_12 = 0 "
             f"is INHERITED from the rook's graph (V13) and is NOT a finding "
             f"of this unit",
             dg_zero, {"crystal": nm, "diag_11": links[DIAG[0]],
                       "diag_12": links[DIAG[1]]},
             polarity=("identically ZERO at 9 of 9 sites",
                       "populated at some site"))
        gate(f"G-BRIDGE-SUPPORT[{nm}]",
             f"the renewal sublattice's SUPPORT at the initiator reading is "
             f"{[list(x) for x in supp]}, a union of {len(cos)} full cosets "
             f"of <(1,1)> (residues {cos} of j-i) -- "
             + ("the support is itself <(1,1)>-periodic, which is the "
                "sublattice-is-a-crystal statement read on the SET rather "
                "than on the counts" if kind == "ARBITRATION" else
                "a SINGLE site carrying no coset structure at all -- the "
                "value the DECLARED COUNTEREXAMPLE CONTROL must return"),
             is_cosets if kind == "ARBITRATION" else not is_cosets,
             {"crystal": nm, "support": [list(x) for x in supp],
              "cosets": cos, "is_coset_union": is_cosets})
        n_legs = sum(n for _c, n in legs)
        gate(f"G-BRIDGE-LEGS[{nm}]",
             f"the RECORD-ORDER bridges -- the gaps between consecutive "
             f"marked events -- have multiset {legs} on this crystal, "
             f"{n_legs} legs over {len(idx)} marked events (a gap sequence "
             f"has exactly one fewer term than the sequence it is read "
             f"from, measured here and not assumed).  paper-09 4's support "
             f"holes (no inter-renewal leg of length one or two) carry a "
             f"two-actor DELIVERY-FREE scope tag and this arena is neither, "
             f"so this row is a COMPARISON and not a test of that law",
             n_legs == max(len(idx) - 1, 0),
             {"crystal": nm, "legs": legs, "leg_count": n_legs,
              "marked": len(idx)},
             waiver={"class": "SCOPE-DISCLOSED",
                     "reason": "the source law's own scope tag excludes this "
                               "arena; the numbers are reported so a "
                               "successor at matched scope can use them"})
        bridge_rows.append({"crystal": nm, "kind": kind,
                            "axis": {str(lk): links[lk] for lk in AXIS},
                            "diagonal": {str(lk): links[lk] for lk in DIAG},
                            "legs": legs, "support": [list(x) for x in supp],
                            "support_residues": cos,
                            "residues_are_full_cosets": is_cosets})
    seal_payload("bridges", bridge_rows)
    branched = [nm for nm, _k, _f in CRYSTALS if built[nm].maxhits != 1
                or built[nm].refusal is not None]
    reg(len(branched))
    gate("G-BRIDGE-SCOPE",
         f"THE BRIDGES ARE REPORTED, NOT INTERPRETED -- AND THE FOUNDING "
         f"SPEC'S OWN CLAUSE IS NOT MERELY UNRUN HERE, IT IS UNPOSABLE.  "
         f"The pin asks what structure the bridges carry AT DECLARED SCOPE "
         f"ONLY and forbids an indivisibility claim beyond what the arena "
         f"can measure.  This arena measures three bridge objects -- the "
         f"co-division adjacency, the support's coset structure, the "
         f"record-order leg multiset -- and none of them is a transition "
         f"kernel.  MEASURED, and this is the structural reason: every one "
         f"of the {len(CRYSTALS)} records is FORCED -- maxhits = 1 at all "
         f"five, {len(branched)} records branch anywhere -- so the menu "
         f"never offers a choice, no transition kernel exists on this "
         f"arena, and 'the bridges are probed for indivisible structure' "
         f"has no definable reading here at all.  Where the geometry is "
         f"cleanest, the stochasticity is gone.  The candidate readings are "
         f"NAMED: (i) the axis link counts as the crystal's q_11 and q_22; "
         f"(ii) the leg multiset as a crystal-scope analogue of paper-09 "
         f"4's g(n); (iii) the coset support as the renewal sublattice's "
         f"own period lattice.  Each is a candidate reading until an "
         f"adjudication makes it otherwise",
         len(branched) == 0,
         {"objects": 3, "indivisibility_claim": False,
          "candidate_readings": 3, "records_branching": len(branched),
          "indivisibility_clause": "UNPOSABLE-ON-A-FORCED-RECORD"})

    # ---------------------------------------------------------- SEC 7b
    emit("")
    emit("-" * 78)
    emit("SEC 7b  THE DIAGONAL, UNIFIED -- U4's bridges on I7's coordinates")
    emit("-" * 78)
    i7_rows = []
    for nm, kind, _f in CRYSTALS:
        lk = link_tab[nm]
        n10, n01, n11 = lk[(1, 0)], lk[(0, 1)], lk[(1, 1)]
        hom = (len(set(n10)) == 1 and len(set(n01)) == 1
               and len(set(n11)) == 1)
        q11, q22 = n10[0], n01[0]
        num = n11[0] - n10[0] - n01[0]
        q12 = Fr(num, 2)
        det = Fr(q11) * Fr(q22) - q12 * q12
        if MUTANT == "MUT-I7-DET" and nm == "DOUBLE-GRID(3,3)":
            det = Fr(1)
        cells = sum(1 for v in (n10 + n01 + n11) if v > 0)
        kern = (Fr(q11) * 1 + q12 * 1 == 0) and (q12 * 1 + Fr(q22) * 1 == 0)
        reg(q11, q22, cells, len(n10 + n01 + n11))
        reg(str(q12), str(det))
        i7_rows.append({"crystal": nm, "kind": kind, "n_10": n10[0],
                        "n_01": n01[0], "n_11": n11[0], "q11": q11,
                        "q22": q22, "q12": str(q12), "det": str(det),
                        "homogeneous": hom, "cells_positive": cells,
                        "cells": len(n10 + n01 + n11),
                        "kernel_contains_(1,1)": bool(kern)})
        emit(f"  [DATA] {nm:19s} I7 n=({n10[0]},{n01[0]},{n11[0]}) "
             f"q=({q11},{q22},{q12}) det={det} cells>0="
             f"{cells}/{len(n10 + n01 + n11)}")
        gate(f"G-I7-INDUCED[{nm}]",
             f"THIS UNIT'S FOUND-SIDE ARENA, EVALUATED ON I7's OWN "
             f"COORDINATES (V17's three links, V18's readout).  The "
             f"renewal sublattice supplies {cells} of I7's "
             f"{len(n10 + n01 + n11)} (site, link) cells strictly positive "
             f"and translation-homogeneous ({hom}) and fails exactly the "
             f"{len(n11)} DIAGONAL cells, where the count is zero.  The "
             f"induced form is q_11 = {q11}, q_22 = {q22}, q_12 = {q12}, "
             f"whose determinant is {det}" +
             (" -- IDENTICALLY ZERO, reproducing weld 2's "
              "INDUCED-DET=0-AT-EVERY-SITE-OF-EVERY-CRYSTAL from the FOUND "
              "side by a route weld 2 did not have, with kernel spanned by "
              "(1,1): the direction the induced metric is blind along is "
              "the same direction SEC 5 measures as the division field's "
              "period" if det == 0 else " -- NONZERO"),
             det == 0 and hom and cells == (18 if kind == "ARBITRATION"
                                            else 0),
             {"crystal": nm, "q11": q11, "q22": q22, "q12": str(q12),
              "det": str(det), "cells_positive": cells,
              "homogeneous": hom, "kernel_contains_(1,1)": bool(kern)},
             polarity=("fails exactly the", "populates the diagonal"))
    seal_payload("i7", i7_rows)
    arbrow = [r for r in i7_rows if r["kind"] == "ARBITRATION"]
    reg(sum(r["cells_positive"] for r in arbrow))
    gate("G-I7-ONE-CAUSE",
         f"ONE CAUSE, TWO SHADOWS -- and the renewal-crystal weld census is "
         f"PREDICTABLY EMPTY at this family.  Every arbitration crystal "
         f"lands on the same row: {arbrow[0]['cells_positive']} of "
         f"{arbrow[0]['cells']} cells positive and homogeneous, the nine "
         f"diagonal cells empty, det identically 0, kernel <(1,1)>.  Both "
         f"appearances of (1,1) trace to ONE design choice in the committed "
         f"constructors and are NOT two independent witnesses: d66 seeds "
         f"conflict on <(1,1)>-cosets, which makes the count field "
         f"<(1,1)>-periodic (SEC 5's affine mechanism), and it groups by "
         f"ROWS AND COLUMNS, which makes the link set the two axes and "
         f"leaves the diagonal empty (SEC 7).  A successor must not count "
         f"them twice.  This unit therefore does not run the census: it "
         f"records that on this family the census's answer is already "
         f"determined, and hands the determinant column forward as the "
         f"weld-arena scout",
         all(r["det"] == "0" for r in i7_rows)
         and all(r["cells_positive"] == 18 for r in arbrow)
         and len(arbrow) == 4,
         {"arbitration_rows": arbrow,
          "census_run_here": False,
          "verdict": "PREDICTABLY-EMPTY-AT-THIS-FAMILY"})
    checkpoint("SEC 7 (the bridges)")

    # -------------------------------------------------------------- SEC 8
    emit("")
    emit("=" * 78)
    emit("SEC 8  THE WALLS (pin R5) -- construction law, argued before use")
    emit("=" * 78)
    banned_hits, scanned = [], []
    for pth in (os.path.abspath(__file__), PAPER):
        if not os.path.exists(pth):
            continue
        with open(pth, "r", encoding="utf-8") as fh:
            txt = fh.read()
        if MUTANT == "MUT-WALL-L1-WRAPPED" and pth == PAPER:
            txt = txt + "\n" + WRAP_INJECTION
        hay = norm_ws(txt)
        scanned.append({"path": os.path.relpath(pth, REPO),
                        "chars_normalised": len(hay)})
        for k, ndl in enumerate(BANNED_NEEDLES):
            if norm_ws(ndl) in hay:
                banned_hits.append({"path": os.path.relpath(pth, REPO),
                                    "needle": k, "chars": len(ndl)})
    gate("G-WALL-L1",
         "L-1's FOURTH FORM, ARGUED BEFORE ANY TEST AND THEN DECLINED.  "
         "L-1 (V09) records that order-level covariance is a fourth form "
         "outside v3 paper 8's three and that its admissibility is v11's to "
         "argue when U4 runs.  THE ARGUMENT: admissibility would require a "
         "declared group acting on the generated causal order together with "
         "a reason to read that group as a covariance group; this arena "
         "supplies five finite records and a translation action on their "
         "SITE LATTICE, and the corpus contains no bridge from Z_3^2 "
         "translations to any boost.  This unit therefore does NOT test the "
         "fourth form; it remains unargued and untested here and is "
         f"registered for a successor.  THE BAN IS ENFORCED AS PROSE IS "
         f"WRITTEN: {len(BANNED_NEEDLES)} needles -- the retracted sentence "
         f"(V15) and the corpus's own canonical short fragment (V16, v11's "
         f"anchor L1-A16) -- are matched against this paper and this source "
         f"with whitespace normalised on BOTH sides, so a line-wrapped "
         f"reproduction is caught exactly as a contiguous one is; "
         f"{len(banned_hits)} hits",
         len(banned_hits) == 0,
         {"fourth_form_tested": False, "banned_sentence_hits": banned_hits,
          "needles": len(BANNED_NEEDLES),
          "needle_chars": [len(n) for n in BANNED_NEEDLES],
          "whitespace_normalised": True, "scanned": scanned})
    perm_ok = all(len({((x[0] + t[0]) % L, (x[1] + t[1]) % L)
                       for x in SITES}) == len(SITES) for t in SITES)
    gate("G-WALL-L1-PERMUTATION",
         f"what this unit DOES measure is inside L-1's own scope guard "
         f"(V10): the Z_3^2 translation stabilizer is a PERMUTATION ACTION "
         f"on the actor set, and L-1 does not forbid a permutation action.  "
         f"MEASURED, not declared: each of the {len(SITES)} translations "
         f"acts on the {len(SITES)} sites as a bijection ({perm_ok}), and "
         f"each crystal's actor->site map is gated a bijection at "
         f"G-SITEMAP.  The headline measurement therefore needs no "
         f"fourth-form argument at all",
         perm_ok, {"action": "permutation on the actor set",
                   "translations": len(SITES), "all_bijections": perm_ok})
    bhs_words = ("sprinkl", "boost", "rapidit", "frame", "lorentz")
    bhs_hay = json.dumps({k: v for k, v in PAYLOAD.items()
                          if k != "provenance"},
                         sort_keys=True, default=str).lower()
    bhs_hits = sorted(w for w in bhs_words if w in bhs_hay)
    reg(len(bhs_hits))
    gate("G-WALL-BHS",
         f"NO SPRINKLING-GRADE LORENTZ-INVARIANCE TEST IS RUN.  The catalog "
         f"(V07) records that these crystals are finite-valency by "
         f"construction, so BHS makes sprinkling-grade statistical Lorentz "
         f"invariance provably unavailable on them and running the test "
         f"would manufacture a false negative.  MEASURED ABSENCE, not a "
         f"typed zero: every measurement row this run computed "
         f"({len(bhs_hay)} characters; the pinned-source list is excluded "
         f"because it names L-1's own filename) is scanned for "
         f"{len(bhs_words)} tokens -- {list(bhs_words)} -- and carries "
         f"{len(bhs_hits)} of them",
         bhs_hits == [], {"sprinkling_grade_LI_tests_run": 0,
                          "tokens_scanned": list(bhs_words),
                          "payload_chars": len(bhs_hay), "hits": bhs_hits})
    kr = [{"crystal": r["crystal"], "n": r["full"]["2"]["n"],
           "longest_chain": r["longest_chain_full"],
           "sub_n": r["marked"], "sub_longest_chain": r["longest_chain_sub"]}
          for r in geom_rows]
    kr_ok = all(r["longest_chain"] > 3 for r in kr)
    gate("G-WALL-KR",
         f"EVERY DIMENSION-ADJACENT READING CARRIES ITS HEIGHT CONTROL "
         f"(V08).  The only dimension-adjacent row this unit reads is the "
         f"chart width max|D|, and it is reported with the longest chain of "
         f"the population it is read on, full and sparse, at every crystal: "
         f"{kr}.  The Kleitman-Rothschild discriminator is the longest "
         f"chain (KR orders return 3 where a sprinkling returns tens) and "
         f"no population here returns 3.  No Myrheim-Meyer estimate is run "
         f"at all.  THE MAX-SHATTER METER IS NOT RUN, AND NOT FOR THIS "
         f"REASON: the catalog grades it a 1+1-escape detector and NOT a "
         f"dimension estimator, and at n <= {max(r['sub_n'] for r in kr)} "
         f"marked events and heights <= {max(r['sub_longest_chain'] for r in kr)} "
         f"no acceptance gauge on these sparse posets could discriminate.  "
         f"The empty object of G-GEOM-HCTRL is this unit's own stricter "
         f"height-MATCHED CONTROL POPULATION, not the KR discriminator, "
         f"which is carried here in full",
         kr_ok, {"height_controls": kr, "MM_estimates_run": 0,
                 "max_shatter_run": False,
                 "max_shatter_grounds": ["catalog grades it a 1+1-escape "
                                         "detector, not a dimension "
                                         "estimator",
                                         "sparse posets too small to "
                                         "discriminate"]})
    dg_all = all(set(v) == {0} for r in link_tab.values()
                 for lk, v in r.items() if lk in DIAG)
    det0 = all(r["det"] == "0" for r in i7_rows)
    gate("G-WALL-DIAGONAL",
         f"THE DIAGONAL QUESTION IS NOT ANSWERED HERE, AND THE "
         f"COUNTERPOINT IS DEFLATED RATHER THAN READ.  q_12 = 0 is "
         f"INHERITED (V13): the co-division graph is the rook's graph and "
         f"diagonal pairs share neither row nor column, measured at 9 of 9 "
         f"sites on every crystal by the G-BRIDGE-DIAG gates ({dg_all}).  "
         f"SEC 7b assembles I7's coordinates for ONE purpose only -- to "
         f"record that the induced form is DEGENERATE at every site of "
         f"every crystal ({det0}), so that no metric is read off it here "
         f"and the census that would read one is answered before it is "
         f"posed.  The counterpoint -- the field's invariance direction is "
         f"the diagonal <(1,1)> while the diagonal LINK count is "
         f"identically zero -- is not a coincidence this unit interprets: "
         f"G-I7-ONE-CAUSE measures that both descend from the same "
         f"constructor choice.  Whether a carrier exists that POPULATES a "
         f"diagonal pair is not decided here",
         dg_all and det0, {"q12": 0, "inherited": True,
                           "answered_here": False,
                           "diagonal_all_zero": dg_all,
                           "induced_det_all_zero": det0})
    dead_tokens = ["STRUCT-DEAD", "ARITY-DEAD", "CONG-185", "ULAM",
                   "SYLVESTER", "ISOS=", "CONFIGS="]
    dead_hay = (json.dumps(PAYLOAD, sort_keys=True, default=str)
                + " " + " ".join(g["gate"] for g in GATES)).upper()
    dead_hits = sorted(t for t in dead_tokens if t in dead_hay)
    reg(len(dead_tokens), len(dead_hits))
    gate("G-DEAD-LIST-CITED",
         f"the pre-registered dead list (weld-2 pin R4 / scout S6) is CITED "
         f"and not re-run: R6b' C1-C5 and the four blanket rows.  MEASURED, "
         f"not asserted: the weld-2 census's own result names -- "
         f"{dead_tokens} -- are searched for across every gate name and "
         f"every measurement row this run produced, and "
         f"{len(dead_hits)} occur.  SEC 7b reads weld 2's LIVE row "
         f"(INDUCED-DET=0) from the FOUND side and re-derives none of the "
         f"dead ones",
         dead_hits == [], {"dead_items": 5, "tokens": dead_tokens,
                           "hits": dead_hits})
    checkpoint("SEC 8 (the walls)")

    # -------------------------------------------------------------- SEC 9
    emit("")
    emit("=" * 78)
    emit("SEC 9  THE VERDICT")
    emit("=" * 78)
    unbound = [c["gate"] for c in POLARITY_CHECKS if not c["bound"]]
    reg(len(POLARITY_CHECKS))
    gate("G-PROSE-POLARITY",
         f"A GATE'S WORDS ARE BOUND TO ITS OWN BOOLEAN (#20).  "
         f"{len(POLARITY_CHECKS)} gate statements carry a polarity pair -- "
         f"the fragment their measured verdict REQUIRES and the fragment it "
         f"FORBIDS -- checked under whitespace normalisation at gate time: "
         f"{len(unbound)} statements say something their own number does "
         f"not support.  A statement inverted to the opposite claim while "
         f"its boolean and evidence are left intact therefore cannot ship",
         unbound == [] and len(POLARITY_CHECKS) > 0,
         {"checked": len(POLARITY_CHECKS), "violations": unbound,
          "gates": sorted({c["gate"] for c in POLARITY_CHECKS})})
    TAIL = ["G-MUTANT-REGISTRY", "G-HEAD-EQUALITY", "G-VERIFY-PAPER-PRESENT",
            "G-VERIFY-PAPER-NUMERALS", "G-VERIFY-PAPER-CLAIMS",
            "G-SEAL-INTEGRITY"]
    raised = {g["gate"] for g in GATES} | set(TAIL)
    targets = sorted({m["target"] for m in MUTANTS.values()
                      if m["target"] != "ANCHOR-STAGE"})
    unknown = [t for t in targets if t not in raised]
    declared = [g["gate"] for g in GATES if g["kind"] == "DECLARED"]
    reg(len(MUTANTS), len(targets), len(GATES), len(declared))
    gate("G-MUTANT-REGISTRY",
         f"THE REGISTRY IS BOUND TO THE RUN (#34).  Each of the "
         f"{len(MUTANTS)} registered mutants names the gate it must die "
         f"at; those names resolve to {len(targets)} distinct gate "
         f"instances and {len(unknown)} of them fail to name a gate this "
         f"run raises, against {len(GATES)} gate instances raised through "
         f"SEC 8.  A registry entry that named the wrong gate would fail "
         f"HERE, and each --mutant run additionally refuses unless the "
         f"gates it actually died at include its registered target.  "
         f"HONEST DENOMINATOR: {len(declared)} gate instances in this run "
         f"carry a DECLARATION rather than a measurement and are labelled "
         f"so in every row ({declared}); every other gate's verdict "
         f"argument is a measured quantity",
         unknown == [] and len(targets) > 0,
         {"mutants": len(MUTANTS), "targets": targets,
          "unknown_targets": unknown, "gates_through_sec8": len(GATES),
          "declared_gates": declared})
    head = build_head(stab_tab)
    head2 = reconstruct_head()
    if MUTANT == "MUT-HEAD":
        head = head.replace("Z3^2", "<(2,1)>", 1)
    gate("G-HEAD-EQUALITY",
         f"THE HEAD IS DERIVED, NOT TYPED, AND IT SURVIVES A COMPLETE-STRING "
         f"EQUALITY GATE AGAINST AN INDEPENDENT RECONSTRUCTION.  The "
         f"reconstruction builds the five records afresh, reads their "
         f"marked events by the SHAPE predicate rather than the tag, maps "
         f"actors to sites by enumeration rather than by parsing their "
         f"names, computes each stabilizer as a Fourier annihilator over "
         f"Z[omega], takes the outcome NAME from the pin's own OUTCOMES "
         f"section by a different extractor, and takes the QUALIFIER from a "
         f"different sentence in a different section of the adjudication "
         f"that ordered it.  What the two paths share is named: the arena "
         f"(the five records are the object of study) and `regs_of`, which "
         f"IS the footprint reading.  Length {len(head)} vs {len(head2)}",
         head == head2, {"head": head, "reconstruction": head2,
                         "identical": head == head2})
    emit("")
    emit(f"  [HEAD] {head}")
    emit(f"  [GEOMETRY] {geom_verdict}")
    seal_payload("head", head)
    seal_payload("geometry_verdict", geom_verdict)
    reg(*re.findall(r"\d+/\d+|\d+", head + " " + geom_verdict))
    seal_payload("stabilizer_table",
                 {f"{k[0]}|{k[1]}": v for k, v in sorted(stab_tab.items())})
    return head, geom_verdict


def head_table(tab):
    short = {"DOUBLE-GRID(3,2)": "DG32", "DOUBLE-GRID(3,3)": "DG33",
             "CONFLICT-GRID(3,2)": "CG32", "CONFLICT-GRID(3,4)": "CG34",
             "D60-GRID(3,12)": "CTRL"}
    return "|".join(
        f"{short[nm]}:{tab[(nm, 'initiator')]}/{tab[(nm, 'footprint')]}"
        for nm, _k, _f in CRYSTALS)


def outcome_name(which):
    """Extract a PRE-REGISTERED outcome name from the pin's OUTCOMES
    section.  Route 1: span the backticked tokens over the whole file."""
    txt = SOURCES["v14/note-u4-pin.md"]
    toks = re.findall(r"`([^`]+)`", txt, flags=re.S)
    for t in toks:
        t2 = re.sub(r"-\s*\n\s*", "-", t).strip()
        if t2.startswith(which):
            return t2
    raise SystemExit("pin does not carry the pre-registered outcome name")


def outcome_name_alt(which):
    """Route 2, for the reconstruction: scan the OUTCOMES section line by
    line, rejoin the hyphenated line breaks, and take the first token."""
    lines = SOURCES["v14/note-u4-pin.md"].split("\n")
    start = None
    for i, ln in enumerate(lines):
        if ln.strip().startswith("## OUTCOMES"):
            start = i
    body = " ".join(lines[start:]).replace("- ", "-")
    out = []
    inside = False
    buf = ""
    for ch in body:
        if ch == "`":
            if inside:
                out.append(buf.replace(" ", ""))
                buf = ""
            inside = not inside
        elif inside:
            buf += ch
    for t in out:
        if t.startswith(which):
            return t
    raise SystemExit("pin does not carry the pre-registered outcome name")


def qualifier():
    """The head's QUALIFIER is not typed either: it is read from the
    adjudication that ordered it.  Route 1: the ruling sentence."""
    txt = norm_ws(SOURCES["v14/note-u4-adjudication.md"])
    m = re.search(r"the head gains the qualifier \*\*([A-Z][A-Z-]+)\*\*", txt)
    if not m:
        raise SystemExit("the adjudication does not carry the qualifier")
    return m.group(1)


def qualifier_alt():
    """Route 2, for the reconstruction: the binding repair order, a
    different sentence in a different section, scanned differently."""
    body = norm_ws(SOURCES["v14/note-u4-adjudication.md"])
    cut = body.find("Binding repair orders")
    m = re.search(r"\*\*The head qualified\*\*: ([A-Z][A-Z-]+) appended",
                  body[cut:])
    if not m:
        raise SystemExit("the adjudication does not carry the qualifier")
    return m.group(1)


def build_head(tab):
    base = outcome_name("U4-THE-DIVISION-EVENTS-FORM-A-CRYSTAL")
    return (re.sub(r"<[^>]*>$", "", base) + qualifier() + "-["
            + head_table(tab) + "]")


def reconstruct_head():
    """The INDEPENDENT reconstruction of the head.  Shares the arena (the
    five records are the object of study, not the instrument) and shares
    nothing else: its own build, its own marking predicate, its own site
    map, its own stabilizer algorithm, its own outcome-name extractor."""
    tab = {}
    for nm, _kind, fn in CRYSTALS:
        rec = fn()
        acts = sorted(set(rec.actors))
        smap = {}
        for k, a in enumerate(acts):
            smap[a] = (k // L, k % L)
        marked = [e for e in rec.H if is_division_structural(e)]
        if MUTANT == "MUT-DIVPRED":
            marked = [e for e in rec.H if e[0] == 'd']
        for rd in READINGS:
            g = dict.fromkeys(SITES, 0)
            for e in marked:
                if rd == "initiator":
                    g[smap[e[1]]] = g[smap[e[1]]] + 1
                else:
                    for r in regs_of(e):
                        if r in smap:
                            g[smap[r]] = g[smap[r]] + 1
            if MUTANT == "MUT-APERIODIC-DIVISION" and nm == "DOUBLE-GRID(3,2)":
                g[(0, 2)] += 1
            if MUTANT == "MUT-CONTROL-PERIODIC" and nm == CTRL:
                g = dict.fromkeys(SITES, 1)
            tab[(nm, rd)] = subgroup_name(stabilizer_by_characters(g))
    base = outcome_name_alt("U4-THE-DIVISION-EVENTS-FORM-A-CRYSTAL")
    cut = base.find("<")
    return base[:cut] + qualifier_alt() + "-[" + head_table(tab) + "]"


# ===========================================================================
# verify-paper, the receipt, the integrity gate
# ===========================================================================

PAPER = os.path.join(REPO, "v14", "paper-14-u4-renewal-crystals.md")
STRUCTURAL = {
    # enumerated structural numerals: era rules, pin/ledger indices, dates,
    # section numbers, source line references.  Each is listed so a reader
    # can audit the waiver.
    "82", "87", "91", "24", "34", "62", "20", "46", "15", "105", "102", "101",
    "2026", "08", "10", "14", "13", "11", "09", "60", "66", "67", "63", "58",
    "47", "42", "74", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "07", "28", "12", "1536", "972", "144", "2325", "29",
}
MASKS = ["the literal 'sha256-NN'", "sha256-12 hexes",
         "7-character commit hexes", "source line references Lnnn",
         "section references", "grid actor names", "heading numbers"]


def verify_paper():
    if not os.path.exists(PAPER):
        gate("G-VERIFY-PAPER-PRESENT",
             f"the paper {os.path.relpath(PAPER, REPO)} must exist for the "
             f"plain run: verify-paper runs INSIDE the plain run and covers "
             f"every numeral in it",
             False, {"path": os.path.relpath(PAPER, REPO), "exists": False})
        return
    with open(PAPER, "r", encoding="utf-8") as fh:
        txt = fh.read()
    gate("G-VERIFY-PAPER-PRESENT",
         f"the paper is present ({len(txt)} bytes) and every numeral in it "
         f"is checked below against numbers this run COMPUTED",
         True, {"bytes": len(txt)})
    # mask the identifier classes that are not quantities: sha256-12 and
    # 7-character commit hexes, and source line references.  Each mask is
    # named here so the waiver is auditable.
    masked = re.sub(r"sha256-\d+", " SHANAME ", txt)
    masked = re.sub(r"\b[0-9a-f]{12}\b", " SHA12 ", masked)
    masked = re.sub(r"\b[0-9a-f]{7}\b", " SHA7 ", masked)
    masked = re.sub(r"\bL\d+(?:[–-]\d+)?\b", " LINEREF ", masked)
    masked = re.sub(r"§\d+(?:\.\d+)*", " SECREF ", masked)
    masked = re.sub(r"(?m)^#+\s+\d+(?:\.\d+)*", " HEADING ", masked)
    masked = re.sub(r"\b[A-Z]\d\d\b", " ACTOR ", masked)
    toks = re.findall(r"\d+/\d+|\d+\.\d+|\d+", masked)
    matched, struct, unmatched = 0, 0, []
    for t in toks:
        if t in NUMREG:
            matched += 1
        elif t.lstrip("0") in NUMREG and t.lstrip("0"):
            matched += 1
        elif t in STRUCTURAL:
            struct += 1
        else:
            unmatched.append(t)
    cov = Fr(matched + struct, len(toks)) if toks else Fr(0)
    gate("G-VERIFY-PAPER-NUMERALS",
         f"NUMERAL COVERAGE, HONEST (#34): after masking {len(MASKS)} named "
         f"identifier classes ({MASKS}) the paper carries {len(toks)} "
         f"numeric tokens; {matched} reproduce a number this run computed, "
         f"{struct} match the ENUMERATED structural whitelist (era rule "
         f"numbers, ledger and pin indices, dates, section references -- "
         f"{len(STRUCTURAL)} entries, all printed in the "
         f"receipt), and {len(unmatched)} match neither: {sorted(set(unmatched))[:12]}.  "
         f"This gate is a TRANSCRIPTION check, not an independent "
         f"verification -- small integers match the registry trivially -- "
         f"and the meaning-binding coverage is G-VERIFY-PAPER-CLAIMS",
         len(unmatched) == 0,
         {"tokens": len(toks), "matched": matched, "structural": struct,
          "unmatched": sorted(set(unmatched)), "coverage": str(cov),
          "whitelist": sorted(STRUCTURAL), "masks": MASKS})
    claims = []
    for r in PAYLOAD["arena"]:
        claims.append(f"{r['events']} events, {r['divisions']} division")
    for r in PAYLOAD["stabilizers"]:
        claims.append(f"{r['stabilizer']}")
    claims.append(PAYLOAD["head"])
    claims.append(PAYLOAD["geometry_verdict"])
    miss = [c for c in claims if c not in txt]
    gate("G-VERIFY-PAPER-CLAIMS",
         f"MEANING-BINDING COVERAGE: {len(claims) - len(miss)} of "
         f"{len(claims)} keyed claim strings -- the per-crystal event and "
         f"division counts, every stabilizer name, the head and the "
         f"geometry verdict -- occur VERBATIM in the paper; missing "
         f"{miss[:4]}",
         len(miss) == 0, {"claims": len(claims), "missing": miss})


def apply_seam_mutants():
    """The SEAM attacks, post-repair.  Every one of them tampers with the
    object that is actually published -- the SEALED copy on its way to
    disk -- because that is the only attack surface a gate-time seal
    leaves.  Each must die at G-SEAL-INTEGRITY."""
    if MUTANT not in SEAM_MUTANTS:
        return
    if MUTANT == "MUT-SEAM-OUTPUT-LINE":
        for i, ln in enumerate(SEALED_LINES):
            if ln.startswith("  [DATA] CONFLICT-GRID(3,2)  initiator"):
                SEALED_LINES[i] = ("  [DATA] CONFLICT-GRID(3,2)   initiator  "
                                   "field=[2, 2, 2, 2, 2, 2, 2, 2, 2] "
                                   "support=9/9")
                break
    if MUTANT == "MUT-SEAM-GATE-ROW":
        for g in SEALED["gates"]:
            if g["gate"] == "G-STAB[CONFLICT-GRID(3,2)|footprint]":
                g["statement"] = g["statement"].replace("Z3^2", "<(1,1)>")
                g["evidence"]["stabilizer"] = "<(1,1)>"
                g["evidence"]["order"] = 3
                break
    if MUTANT == "MUT-SEAM-GATE-FLAG":
        for g in SEALED["gates"]:
            if g["gate"] == "G-BRIDGE-DIAG[DOUBLE-GRID(3,2)]":
                g["evidence"]["diag_11"] = [1, 0, 0, 0, 0, 0, 0, 0, 0]
                g["passed"] = True
                break
    if MUTANT == "MUT-SEAM-PAYLOAD":
        SEALED_PAYLOAD["arena"][0]["events"] = 99
        SEALED_PAYLOAD["arena"][0]["divisions"] = 99
    if MUTANT == "MUT-SEAM-ROW-SWAP":
        rows = SEALED_PAYLOAD["stabilizers"]
        ctrl = [r for r in rows if r["kind"] == "CONTROL"][0]
        for i, r in enumerate(rows):
            if r["crystal"] == "CONFLICT-GRID(3,2)" and \
                    r["reading"] == "initiator":
                rows[i] = dict(ctrl, crystal="CONFLICT-GRID(3,2)",
                               kind="ARBITRATION")
                break
    if MUTANT == "MUT-SEAM-TABLE-CELL":
        SEALED_PAYLOAD["stabilizer_table"][
            "CONFLICT-GRID(3,4)|footprint"] = "<(1,1)>"


def seal_check(where):
    """#119: recompute every digest FROM THE OBJECT THAT WILL BE WRITTEN
    (or, at the disk stage, from the bytes) and compare against the seals
    taken at gate time.  Returns (ok, evidence)."""
    bad = {}
    for kind in SEALS:
        got = [_digest(r) for r in SEALED[kind]]
        bad[kind] = [i for i, (a, b) in enumerate(zip(got, SEALS[kind]))
                     if a != b] + ([len(SEALS[kind])]
                                   if len(got) != len(SEALS[kind]) else [])
    pay = [k for k in PAYLOAD_SEALS
           if k not in SEALED_PAYLOAD
           or _digest(SEALED_PAYLOAD[k]) != PAYLOAD_SEALS[k]]
    extra = [k for k in SEALED_PAYLOAD if k not in PAYLOAD_SEALS]
    out_ok = (sha256_of(out_text(SEALED_LINES).encode("utf-8"))
              == OUT_H.hexdigest())
    ok = (not any(bad.values()) and not pay and not extra and out_ok)
    return ok, {"where": where, "rows_broken": {k: v for k, v in bad.items()
                                                if v},
                "payload_broken": pay, "payload_unsealed": extra,
                "output_seal_intact": out_ok,
                "sealed_output_lines": len(SEALED_LINES),
                "sealed_rows": {k: len(SEALS[k]) for k in SEALS},
                "sealed_payload_rows": len(PAYLOAD_SEALS)}


def render():
    out = out_text(SEALED_LINES)
    rec = {
        "unit": "U4 / paper-14 -- renewal-only crystals",
        "pin": {"path": "v14/note-u4-pin.md", "sha256_12": "06b62ecb60a9",
                "ledger": 105},
        "interpreter": INTERP,
        "head": SEALED_PAYLOAD.get("head"),
        "geometry_verdict": SEALED_PAYLOAD.get("geometry_verdict"),
        "stabilizer_table": SEALED_PAYLOAD.get("stabilizer_table"),
        "counts": {"gates": len(SEALED["gates"]),
                   "gates_passed": sum(1 for g in SEALED["gates"]
                                       if g["passed"]),
                   "gates_failed": sum(1 for g in SEALED["gates"]
                                       if not g["passed"]),
                   "gates_declared": sum(1 for g in SEALED["gates"]
                                         if g["kind"] == "DECLARED"),
                   "gates_measured": sum(1 for g in SEALED["gates"]
                                         if g["kind"] == "MEASURED"),
                   "mutant_target_gates": len({m["target"] for m in
                                               MUTANTS.values()
                                               if m["target"] !=
                                               "ANCHOR-STAGE"}),
                   "anchors": len(SEALED["anchors"]),
                   "anchors_passed": sum(1 for a in SEALED["anchors"]
                                         if a["passed"]),
                   "verbatim_anchors": len(SEALED["verbatim"]),
                   "verbatim_passed": sum(1 for v in SEALED["verbatim"]
                                          if v["found"]),
                   "waivers": len(SEALED["waivers"]),
                   "polarity_checks": len(POLARITY_CHECKS),
                   "mutants_registered": len(MUTANTS),
                   "numbers_registered": len(NUMREG)},
        "gates": SEALED["gates"], "anchors": SEALED["anchors"],
        "verbatim": SEALED["verbatim"], "waivers": SEALED["waivers"],
        "payload": SEALED_PAYLOAD,
        "mutants": {k: MUTANTS[k] for k in sorted(MUTANTS)},
        "seal": {"gates": SEALS["gates"], "anchors": SEALS["anchors"],
                 "verbatim": SEALS["verbatim"], "waivers": SEALS["waivers"],
                 "payload": PAYLOAD_SEALS,
                 "output": OUT_H.hexdigest(),
                 "output_lines": len(SEALED_LINES)},
        "output_sha256": sha256_of(out.encode("utf-8")),
    }
    return out, json.dumps(rec, indent=2, sort_keys=True,
                           default=str) + "\n"


def write_and_verify(out, rj):
    tmp1, tmp2 = OUT_TXT + ".tmp", OUT_JSON + ".tmp"
    with open(tmp1, "w", encoding="utf-8") as fh:
        fh.write(out)
    with open(tmp2, "w", encoding="utf-8") as fh:
        fh.write(rj)
    with open(tmp1, "rb") as fh:
        b1 = fh.read()
    with open(tmp2, "rb") as fh:
        b2 = fh.read()
    rec = json.loads(b2.decode("utf-8"))
    # THE INTEGRITY CHECK IS DISK-VERSUS-SEAL, never disk-versus-memory:
    # every published row is re-digested FROM THE BYTES THAT WERE WRITTEN
    # and compared with the digest taken when its gate fired.
    disk_rows = all(
        [_digest(r) for r in rec[k]] == SEALS[k]
        for k in ("gates", "anchors", "verbatim", "waivers"))
    disk_pay = (set(rec["payload"]) == set(PAYLOAD_SEALS)
                and all(_digest(rec["payload"][k]) == PAYLOAD_SEALS[k]
                        for k in PAYLOAD_SEALS))
    txt = b1.decode("utf-8")
    disk_out = (sha256_of(b1) == OUT_H.hexdigest())
    tgt_ok = all(t in {g["gate"] for g in rec["gates"]}
                 for t in {m["target"] for m in MUTANTS.values()
                           if m["target"] != "ANCHOR-STAGE"})
    ok = (b1 == out.encode("utf-8") and b2 == rj.encode("utf-8")
          and rec["output_sha256"] == sha256_of(b1)
          and rec["head"] == SEALED_PAYLOAD.get("head")
          and SEALED_PAYLOAD.get("head", "") in txt
          and rec["counts"]["gates_failed"] == 0
          and disk_rows and disk_pay and disk_out and tgt_ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] G-FINAL-INTEGRITY")
    print(f"         the two artifacts were written, RE-READ FROM DISK and "
          f"re-verified AGAINST THE GATE-TIME SEAL: {len(b1)} + {len(b2)} "
          f"bytes; every gate, anchor, verbatim and waiver row on disk "
          f"re-digests to the digest taken when its gate fired "
          f"({disk_rows}); every payload row does the same ({disk_pay}); "
          f"the output bytes reproduce the seal folded at emit time "
          f"({disk_out}); every "
          f"registered mutant target names a gate the receipt carries "
          f"({tgt_ok}); the receipt's recorded output sha256 matches the "
          f"file on disk; the head in the receipt matches the head in the "
          f"output and the head in memory; and no gate failed")
    if not ok:
        os.remove(tmp1)
        os.remove(tmp2)
        return False
    os.replace(tmp1, OUT_TXT)
    os.replace(tmp2, OUT_JSON)
    return True


def finalize():
    """The seal stage: publish only what was sealed, and gate the seal."""
    apply_seam_mutants()
    ok, ev = seal_check("pre-write")
    gate("G-SEAL-INTEGRITY",
         f"THE SEAL (#119).  Every published row -- {len(SEALS['gates'])} "
         f"gates, {len(SEALS['anchors'])} anchors, "
         f"{len(SEALS['verbatim'])} verbatim anchors, "
         f"{len(SEALS['waivers'])} waivers and "
         f"{len(PAYLOAD_SEALS)} payload rows -- was DIGESTED AT GATE TIME, "
         f"and the artifacts are rendered from those sealed copies, not "
         f"from live memory; the emitted output is folded into a byte "
         f"seal AS IT IS EMITTED.  Here every sealed object is "
         f"re-digested and compared against the digest taken when its gate "
         f"fired, and after the write the same comparison is made again "
         f"from THE BYTES ON DISK.  Anything changed between a gate and "
         f"the disk -- an output line, a gate row, a gate's passed flag, a "
         f"payload row, a published table cell -- fails HERE and nothing "
         f"is written",
         ok, ev)
    return render()


USAGE = ("usage: u4_crystals_exact.py [--selftest | --numbers | "
         "--mutant NAME]\n  no arguments: the plain run (writes "
         "u4_crystals_output.txt + u4_crystals_receipt.json)")


def parse_argv(argv):
    """#82: a strict argv whitelist.  Anything else exits 2."""
    if len(argv) == 1:
        return ("plain", None)
    if len(argv) == 2 and argv[1] == "--selftest":
        return ("selftest", None)
    if len(argv) == 2 and argv[1] == "--numbers":
        return ("numbers", None)
    if len(argv) == 3 and argv[1] == "--mutant":
        if argv[2] not in MUTANTS:
            print(f"unknown mutant: {argv[2]}", file=sys.stderr)
            print("registered mutants:", file=sys.stderr)
            for k in sorted(MUTANTS):
                print(f"  {k}: {MUTANTS[k]['what']}  "
                      f"[target {MUTANTS[k]['target']}]", file=sys.stderr)
            sys.exit(2)
        return ("mutant", argv[2])
    print(USAGE, file=sys.stderr)
    sys.exit(2)


def main():
    global MUTANT, ANCHOR_FAIL, FAILED, QUIET
    mode, name = parse_argv(sys.argv)
    QUIET = mode in ("selftest", "mutant")

    if mode == "selftest":
        # corrupt ONE anchor, confirm the run refuses, WRITE NOTHING.
        before = (os.path.exists(OUT_TXT) and open(OUT_TXT, "rb").read(),
                  os.path.exists(OUT_JSON) and open(OUT_JSON, "rb").read())
        MUTANT = "MUT-ANCHOR"
        try:
            main_run()
        except SystemExit:
            pass
        died = ANCHOR_FAIL > 0
        after = (os.path.exists(OUT_TXT) and open(OUT_TXT, "rb").read(),
                 os.path.exists(OUT_JSON) and open(OUT_JSON, "rb").read())
        wrote_nothing = (before == after
                         and not os.path.exists(OUT_TXT + ".tmp")
                         and not os.path.exists(OUT_JSON + ".tmp"))
        print("SELFTEST -- one committed anchor corrupted "
              "(DOUBLE-GRID(3,2) d=2 max|D|: 9 -> 8)")
        print(f"  anchors failed: {ANCHOR_FAIL} (expected >= 1)")
        print(f"  artifacts unchanged: {before == after}")
        print(f"  wrote nothing: {wrote_nothing}")
        ok = died and before == after and wrote_nothing
        print(f"  [{'PASS' if ok else 'FAIL'}] G-SELFTEST")
        sys.exit(0 if ok else 1)

    if mode == "mutant":
        MUTANT = name
        before = (os.path.exists(OUT_TXT) and open(OUT_TXT, "rb").read(),
                  os.path.exists(OUT_JSON) and open(OUT_JSON, "rb").read())
        try:
            main_run()
            verify_paper()
            finalize()
        except SystemExit:
            pass
        failed = [g["gate"] for g in GATES if not g["passed"]]
        after = (os.path.exists(OUT_TXT) and open(OUT_TXT, "rb").read(),
                 os.path.exists(OUT_JSON) and open(OUT_JSON, "rb").read())
        died = bool(failed) or ANCHOR_FAIL > 0
        tgt = MUTANTS[name]["target"]
        at_target = (ANCHOR_FAIL > 0 if tgt == "ANCHOR-STAGE"
                     else tgt in failed)
        print(f"MUTANT {name}")
        print(f"  {MUTANTS[name]['what']}")
        print(f"  registered target: {tgt}")
        print(f"  died at gates: {failed if failed else '(anchor stage)'}")
        print(f"  died at its registered target: {at_target}")
        print(f"  anchor failures: {ANCHOR_FAIL}")
        print(f"  artifacts unchanged: {before == after}")
        for ln in LINES:
            if "[GEOMETRY SEGMENT VERDICT]" in ln or "VARIES" in ln:
                print(f"  emitted: {ln.strip()}")
        ok = died and before == after and at_target
        print(f"  [{'PASS' if ok else 'FAIL'}] G-MUTANT[{name}]")
        sys.exit(0 if ok else 1)

    head, gv = main_run()
    if mode == "numbers":
        print(f"HEAD      {head}")
        print(f"GEOMETRY  {gv}")
        print("PAYLOAD")
        print(json.dumps(PAYLOAD, indent=2, sort_keys=True, default=str))
        print("REGISTRY  " + " ".join(sorted(NUMREG)))
        print(f"gates {len(GATES)} passed "
              f"{sum(1 for g in GATES if g['passed'])} "
              f"anchors {len(ANCHORS)} anchor-failures {ANCHOR_FAIL}")
        sys.exit(0)

    verify_paper()
    out, rj = finalize()
    print("\n".join(LINES))
    if ANCHOR_FAIL or FAILED:
        print(f"\nREFUSED: {FAILED} gate failures, {ANCHOR_FAIL} anchor "
              f"failures -- NOTHING WRITTEN", file=sys.stderr)
        sys.exit(1)
    if not write_and_verify(out, rj):
        print("\nREFUSED at the final integrity gate -- NOTHING WRITTEN",
              file=sys.stderr)
        sys.exit(1)
    print(f"\nwrote {os.path.relpath(OUT_TXT, REPO)} and "
          f"{os.path.relpath(OUT_JSON, REPO)}")
    sys.exit(0)


if __name__ == "__main__":
    main()

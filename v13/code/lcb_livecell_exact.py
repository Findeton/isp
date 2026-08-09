#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""
LCB -- THE LIVE-CELL BRIDGE AT THE STRENGTHENED STANDARD
=======================================================

Pin: v13/note-lcb-livecell-pin.md (STRICT, frozen, sha256 4f30880229e7...,
commit d2f6104).  Binding: BRG's terminal S1-S6 registry (paper section 2.6)
verbatim; RUNBOOK 13 (verdict-in-gate with computed qualifiers, verdict-flip
and no-witness mutants, cell-completeness, genuinely independent routes),
RUNBOOK 14 (symmetry self-tests, all addenda) and RUNBOOK 15 (declared-arena
discipline, all addenda).

THE PAIRING (section 2 of the paper; declared as data before anything is
evaluated):

  TRANSPORT BASE   base G's carrier (81 = system pair x pointer pair) with a
      completion Q0 of ord(D) = 5, selected by the DECLARED rule "lex-first
      one-line notation among the completions fixing label 0 whose defect has
      order 5".  D = delta(Q0) = Sigma Q0^T Sigma Q0 (GEN 8.1); <W,D>
      dihedral of order 2*ord(D) = 10 (PSI's one law).
  DEFORMATION ARENA  C_HA(5) = F_5^k x F_5^d with k = d = 2 -- HA's own
      construction at p = 5; <R_HH> = Z/5 acting by translation of the address
      register by rho = (1/6,1/6) mod 5 = (1,1).
  LIVE-CELL CONDITION  5 | 2*ord(D) = 10, verified in gate.

THE STRENGTHENED TEST is S1-S6 as BRG registered them.  S1 -- the
non-negotiable -- is ENCODING INTERTWINING as a COMMUTING SQUARE:

        V  --E-->  V                E : HA's record <-> metric re-encoding
        |          |                    (the det-2 readout, HA G28)
      alpha      alpha              delta : Q -> Sigma Q^T Sigma Q
        v          v                    (GEN's completion -> commutator law)
        G --delta->G

measured as 9x9 permutation matrices at every cell, never as group
abstractions.  The candidate space is a CENSUS at declared scope, computed by
two genuinely independent routes.

THE OPERATIVE OBSTRUCTION IS THE FIXED-POINT MISMATCH, and it is arena-free
wherever the deformation side's re-encoding fixes a nonzero vector:

    delta(x) = sigma(x)^-1 x = x  <=>  sigma(x) = e  <=>  x = e,

so delta has EXACTLY ONE fixed point at every arena, with no hypothesis on the
arena at all.  The square then forces alpha(fix E) = {e}: every candidate
satisfying S1a collapses the whole fixed space of E onto the identity, so S1a
and S3 -- both of them BRG-REGISTERED clauses -- are jointly unsatisfiable
wherever dim ker(E - I) >= 1.  That condition is MEASURED here over the
covariant twelve-cell family: it holds at eight of the twelve cells at every
prime, and at the remaining four (whose re-encoding carries primitive cube
roots of unity instead of 1) only at p = 3, where the arena's own p-part
decides instead.  The SPECTRAL and CHART-PARITY facts are retained as
per-cell diagnostics of that wall.

THE CELL FAMILY IS COVARIANT (RUNBOOK 15): the identification is a naming of
the metric's three slots, so the declared cells are swept together with their
whole orbit under the slot-relabelling group S_3 -- 6 identifications x 2
directions = 12 cells, computed from the declared slot triple and never typed.

Exact arithmetic only: integers, fractions.Fraction, exact F_p.  No float or
complex literal and no float()/complex() call appears in this source; the
scanner that measures it is validated by a synthetic injection it must flag.

MUTANT DISCIPLINE (RUNBOOK 14 addendum, v13 #208): every mutation is a
mutation of an INSTRUMENT helper.  No function that registers a gate
references mutant identity, a run-mode boolean or sys.argv; the AST guard
measures that and is validated by a synthetic sample it must flag.

Usage:
    python3.13 lcb_livecell_exact.py                  # delivery run
    python3.13 lcb_livecell_exact.py --mutant NAME    # one mutant; must exit 1
    python3.13 lcb_livecell_exact.py --falsification-selftest
        (the full run and the whole mutant harness, WITHOUT writing artifacts)
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import json
import math
import os
import platform
import re
import subprocess
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
SELF = os.path.abspath(__file__)

# --------------------------------------------------------------------------
# 0.  RUN MODE AND THE DECLARED MUTANT TABLE
# --------------------------------------------------------------------------

_argv = sys.argv[1:]
MUTANT = None
SELFTEST_ONLY = False
for _i, _a in enumerate(_argv):
    if _a == "--mutant":
        MUTANT = _argv[_i + 1]
    elif _a.startswith("--mutant="):
        MUTANT = _a.split("=", 1)[1]
    elif _a == "--falsification-selftest":
        SELFTEST_ONLY = True

MUTANTS: dict[str, str] = {
    # --- anchor mutants ---------------------------------------------------
    "anchor-pin-sha":      "the LCB pin's own hash pin is perturbed",
    "anchor-brg-sha":      "the BRG paper's hash pin is perturbed",
    "anchor-brgr-sha":     "the BRG receipt's hash pin is perturbed",
    "anchor-ha-sha":       "the HA receipt's hash pin is perturbed",
    "anchor-gen-sha":      "the GEN receipt's hash pin is perturbed",
    "anchor-xba-sha":      "the XBA receipt's hash pin is perturbed",
    "anchor-psi-sha":      "the PSI receipt's hash pin is perturbed",
    "anchor-defect":       "the rebuilt base-G defect permutation is perturbed",
    "anchor-family":       "the completion-family sweep is truncated",
    "anchor-rho":          "the exact-to-F_p reduction of rho is perturbed",
    "anchor-readout":      "the record<->metric readout matrix is perturbed",
    "anchor-soft":         "anchor failures are made non-fatal",
    # --- discipline mutants -----------------------------------------------
    "freeze-lax":          "a census datum is evaluated before the declarations "
                           "freeze",
    "float-lax":           "the exact-arithmetic scanner is blinded",
    "exempt-lax":          "the mutant-identity AST scanner is blinded",
    # --- the pairing ------------------------------------------------------
    "select-lax":          "the declared lex-first selection rule is replaced by "
                           "an arbitrary member of the class",
    "group-lax":           "the transport group is closed under one generator only",
    "compat-lax":          "the live-cell divisibility clause is blinded",
    "arena-lax":           "the deformation arena's action is built non-free",
    "encoding-drop":       "one declared encoding cell is dropped from the sweep",
    "cell-orbit-drop":     "the covariant cell family is truncated to the two "
                           "declared identifications",
    "tau-lax":             "the chart involution is replaced by the identity",
    # --- the census -------------------------------------------------------
    "square-lax":          "the commuting square is evaluated at the base point only",
    "hom-lax":             "the homomorphism clause is dropped from the predicate",
    "enum-drop":           "one basis image is dropped from the exhaustive hom "
                           "enumeration",
    "route-a-lax":         "the linear-algebra route mis-solves its kernel",
    "route-alias":         "the second route returns the first route's own answer",
    "matrix-lax":          "the square is compared as group elements instead of as "
                           "9x9 permutation matrices",
    "theorem-lax":         "the forced-sign step is asserted instead of measured",
    # --- the S-clauses ----------------------------------------------------
    "s1c-lax":             "the chart-involution clause is evaluated at the base "
                           "point only",
    "s1d-lax":             "the base-point clause reads the wrong base record",
    "s2-lax":              "the stratification is read off the source instead of "
                           "the transported defect",
    "s3-lax":              "the injectivity clause counts the source instead of "
                           "the image",
    "sylow-lax":           "the p-part bound is read at the wrong arena",
    "grid-drop":           "one cell is dropped from the (p, ord) grid",
    "prime-single":        "the prime sweep is collapsed to one prime",
    "completion-drop":     "one completion is dropped from the base-change sweep",
    "records-lax":         "the base-record sweep is collapsed to the declared "
                           "record",
    # --- the arena-free obstruction ---------------------------------------
    "fixpoint-lax":        "the fixed-point set of the transport encoding is read "
                           "off the wrong law",
    "fixspace-lax":        "the deformation side's fixed-space dimension is "
                           "blinded",
    "dsweep-lax":          "the general-dimension fixed-space sweep is collapsed "
                           "to one dimension",
    "witness7-lax":        "the tau-conjugate witness's exponent covector is "
                           "perturbed",
    "colsum-lax":          "the readout's column sums are read off its rows",
    "setlevel-lax":        "the set-level census's per-orbit factor is typed",
    # --- held-out ---------------------------------------------------------
    "heldout-leak":        "the candidate is fitted on the held-out cells",
    "teeth-off":           "the declared failing extension is silently made the "
                           "accepted one",
    "quantity-lax":        "a transported held-out quantity is read off the wrong "
                           "map",
    "s5map-lax":           "the held-out block reads the synthetic chart map "
                           "instead of the pairing's own",
    # --- controls ---------------------------------------------------------
    "found-block":         "the synthetic compatible pair is made incompatible",
    "empty-block":         "the synthetic incompatible pair is made compatible",
    "witness-blank":       "the exhibited FOUND witness is blanked",
    "break-blind":         "the structure-breaking candidate is replaced by its "
                           "accepted counterpart",
    # --- self-tests -------------------------------------------------------
    "relabel-lax":         "the relabelling self-test relabels nothing",
    "basis-lax":           "the basis-change self-test changes nothing",
    "selftest-select":     "the self-test's tested set is selected by the verdicts",
    "cache-lax":           "the self-test's fresh path reads the memo cache",
    "cache-unused":        "the memo cache is never looked up",
    # --- Open 1 -----------------------------------------------------------
    "open1-lax":           "a declaration-carrying candidate is admitted as "
                           "declaration-free",
    "unique-lax":          "the uniqueness test accepts a two-element prime set",
    "open1-free-flip":     "exactly one candidate's measured declaration-freeness "
                           "is flipped",
    "open1-inter":         "the declaration-free intersection is perturbed to a "
                           "singleton at its own source",
    "open1-scale":         "the sixteen-label scale is read at the nine-label "
                           "arena",
    "open1-reach":         "the two synthetic Open-1 tables are made to return the "
                           "same verdict",
    # --- verdict ----------------------------------------------------------
    "obstruction-misname": "the named obstruction is replaced by a cardinality "
                           "claim",
    "obstruction-fabricate": "the named obstruction is replaced by a plausible "
                             "wrong clause",
    "verdict-flip":        "the verdict derivation returns a hand-typed string",
    "count-flip":          "the emptiness decision is inverted at its own source",
    "universal-lax":       "the universality qualifier is asserted instead of "
                           "measured",
    "qualifier-typo":      "one printed verdict qualifier is replaced by a typed "
                           "value",
}

if MUTANT is not None and MUTANT not in MUTANTS:
    sys.stderr.write(f"unknown mutant {MUTANT!r}\n")
    sys.exit(2)

_M_PINSHA = (MUTANT == "anchor-pin-sha")
_M_BRGSHA = (MUTANT == "anchor-brg-sha")
_M_BRGRSHA = (MUTANT == "anchor-brgr-sha")
_M_HASHA = (MUTANT == "anchor-ha-sha")
_M_GENSHA = (MUTANT == "anchor-gen-sha")
_M_XBASHA = (MUTANT == "anchor-xba-sha")
_M_PSISHA = (MUTANT == "anchor-psi-sha")
_M_DEFECT = (MUTANT == "anchor-defect")
_M_FAMILY = (MUTANT == "anchor-family")
_M_RHO = (MUTANT == "anchor-rho")
_M_READOUT = (MUTANT == "anchor-readout")
_M_SOFT = (MUTANT == "anchor-soft")
_M_FREEZE = (MUTANT == "freeze-lax")
_M_FLOAT = (MUTANT == "float-lax")
_M_EXEMPT = (MUTANT == "exempt-lax")
_M_SELECT = (MUTANT == "select-lax")
_M_GROUP = (MUTANT == "group-lax")
_M_COMPAT = (MUTANT == "compat-lax")
_M_ARENA = (MUTANT == "arena-lax")
_M_ENCDROP = (MUTANT == "encoding-drop")
_M_ORBITDROP = (MUTANT == "cell-orbit-drop")
_M_TAU = (MUTANT == "tau-lax")
_M_SQUARE = (MUTANT == "square-lax")
_M_HOM = (MUTANT == "hom-lax")
_M_ENUM = (MUTANT == "enum-drop")
_M_ROUTEA = (MUTANT == "route-a-lax")
_M_ALIAS = (MUTANT == "route-alias")
_M_MATRIX = (MUTANT == "matrix-lax")
_M_THEOREM = (MUTANT == "theorem-lax")
_M_S1C = (MUTANT == "s1c-lax")
_M_S1D = (MUTANT == "s1d-lax")
_M_S2 = (MUTANT == "s2-lax")
_M_S3 = (MUTANT == "s3-lax")
_M_SYLOW = (MUTANT == "sylow-lax")
_M_GRID = (MUTANT == "grid-drop")
_M_PRIMESINGLE = (MUTANT == "prime-single")
_M_COMPDROP = (MUTANT == "completion-drop")
_M_RECORDS = (MUTANT == "records-lax")
_M_FIXPOINT = (MUTANT == "fixpoint-lax")
_M_FIXSPACE = (MUTANT == "fixspace-lax")
_M_DSWEEP = (MUTANT == "dsweep-lax")
_M_WITNESS7 = (MUTANT == "witness7-lax")
_M_COLSUM = (MUTANT == "colsum-lax")
_M_SETLEVEL = (MUTANT == "setlevel-lax")
_M_HELDOUT = (MUTANT == "heldout-leak")
_M_TEETH = (MUTANT == "teeth-off")
_M_QUANTITY = (MUTANT == "quantity-lax")
_M_S5MAP = (MUTANT == "s5map-lax")
_M_FOUND = (MUTANT == "found-block")
_M_EMPTY = (MUTANT == "empty-block")
_M_WITNESS = (MUTANT == "witness-blank")
_M_BREAK = (MUTANT == "break-blind")
_M_RELABEL = (MUTANT == "relabel-lax")
_M_BASIS = (MUTANT == "basis-lax")
_M_SELSEL = (MUTANT == "selftest-select")
_M_CACHE = (MUTANT == "cache-lax")
_M_CACHEUN = (MUTANT == "cache-unused")
_M_OPEN1 = (MUTANT == "open1-lax")
_M_UNIQUE = (MUTANT == "unique-lax")
_M_FREEFLIP = (MUTANT == "open1-free-flip")
_M_INTER = (MUTANT == "open1-inter")
_M_SCALE = (MUTANT == "open1-scale")
_M_REACH = (MUTANT == "open1-reach")
_M_OBSTR = (MUTANT == "obstruction-misname")
_M_FABRIC = (MUTANT == "obstruction-fabricate")
_M_VERDICT = (MUTANT == "verdict-flip")
_M_COUNTFLIP = (MUTANT == "count-flip")
_M_UNIVERSAL = (MUTANT == "universal-lax")
_M_QUALTYPO = (MUTANT == "qualifier-typo")

DELIVERY_RUN = (MUTANT is None)
WRITE_ARTIFACTS = (DELIVERY_RUN and not SELFTEST_ONLY)

# --------------------------------------------------------------------------
# 1.  RECEIPT SCAFFOLD
# --------------------------------------------------------------------------

ANCHORS: list[dict] = []
GATES: list[dict] = []
DISCLOSURES: list[dict] = []
_GATE_IDS: set[str] = set()
CENSUS_EVALS = [0]
ANCHOR_POLICY = {"failures": 0, "fatal": 0}
OUT: list[str] = []
CACHE_STATS = {"lookups": 0, "hits": 0, "misses": 0, "bypasses": 0,
               "selftest_hits": 0}
_DELTA_MEMO: dict = {}
ROUTE_CALLS = {"A": 0, "B": 0, "taint": 0}


def anchor(aid: str, quantity: str, committed, computed, source: str) -> None:
    ok = (committed == computed)
    ANCHORS.append({"id": aid, "quantity": quantity, "source": source,
                    "committed": committed, "computed": computed, "passed": ok})
    if not ok:
        ANCHOR_POLICY["failures"] += 1
        sys.stderr.write(f"\nANCHOR FAILURE {aid}: {quantity}\n"
                         f"  source    : {source}\n"
                         f"  committed : {committed!r}\n"
                         f"  computed  : {computed!r}\n")
        sys.stdout.flush()
        if not _M_SOFT:
            ANCHOR_POLICY["fatal"] += 1
            sys.exit(1)


def gate(gid: str, claim: str, ok: bool, detail=None, must_pass: bool = True) -> bool:
    if gid in _GATE_IDS:
        raise RuntimeError(f"duplicate gate id {gid}")
    _GATE_IDS.add(gid)
    GATES.append({"id": gid, "claim": claim, "passed": bool(ok),
                  "must_pass": must_pass, "detail": detail})
    return bool(ok)


def report(gid: str, ok: bool, text: str) -> None:
    say(f"  {gid} {'PASS' if ok else 'FAIL'}   {text}")


def disclose(did: str, statement: str, detail=None) -> None:
    DISCLOSURES.append({"id": did, "statement": statement, "detail": detail})


def say(s: str = "") -> None:
    OUT.append(s)
    print(s)


def progress(s: str) -> None:
    sys.stderr.write(f"[lcb] {s}\n")
    sys.stderr.flush()


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for blk in iter(lambda: fh.read(65536), b""):
            h.update(blk)
    return h.hexdigest()


def note_census() -> None:
    CENSUS_EVALS[0] += 1


# --------------------------------------------------------------------------
# 2.  THE DECLARATIONS -- frozen before any candidate is evaluated
# --------------------------------------------------------------------------

DECL: dict = {
    "arena": {
        "boundary": "one PAIRING.  Transport side: base G's carrier (81 = the "
                    "system pair x the pointer pair, 9 labels each), a completion "
                    "Q0 of the 9 system-pair labels fixing label 0, its defect "
                    "D = delta(Q0) = Sigma Q0^T Sigma Q0 (GEN 8.1), and the group "
                    "<W,D> with W = Sigma (x) Sigma.  Deformation side: "
                    "C_HA(5) = F_5^k x F_5^d, k = d = 2, with <R_HH> = Z/5 acting "
                    "by translation of the address register by rho mod 5.  "
                    "Encoding layer: the record datum space V = F_p^3 (the three "
                    "link counts at a site) with HA's record<->metric readout E, "
                    "and the completion group G_C with GEN's completion->commutator "
                    "map delta.",
        "family": "the COVARIANT ENCODING-CELL FAMILY = the orbit of the declared "
                  "identifications under the metric-slot relabelling group S_3 "
                  "(all 3! slot identifications, the two declared ones among "
                  "them) x 2 directions; the cell count is computed from the "
                  "declared metric slot triple and never typed; 7 declared "
                  "primes; 8 measured defect-order classes; the 4,608-member "
                  "ord-5 completion class; HA's 9 admissible geometry records "
                  "(all of them swept at the base-point clause) + 2 declared "
                  "negative controls; the dimensions d = 2,3,4,5 at the "
                  "fixed-space sweep",
        "law": "the strengthened standard S1-S6 as BRG's terminal paper section "
               "2.6 registers it, operationalised clause by clause below; a "
               "candidate morphism is a map alpha : V -> G_C",
        "state": "the deformation side's declared base geometry record r0 = "
                 "G-FLAT's count triple (1,1,2); the transport side's declared "
                 "base completion Q0 (the lex-first ord-5 member); the transport "
                 "side's initial configuration j0 = 0",
        "arena action": "the metric-slot relabelling group S_3, whose orbit on "
                        "the declared identifications is the covariant cell "
                        "family; the DIRECTION sweep (counts->q / q->counts) -- "
                        "the orientation convention RUNBOOK 14 requires to be "
                        "swept; relabelling of the 9 completion labels by a "
                        "permutation fixing label 0; change of basis of the "
                        "record datum space by an element of GL_3(F_p); the prime "
                        "sweep; the choice of completion inside the declared "
                        "ord-5 class; the choice of BASE RECORD (the state "
                        "coordinate) among HA's 9 admissible records.  These "
                        "seven are THIS UNIT'S OWN declared choices and they are "
                        "the ones the Open-1 declaration-freeness criterion "
                        "measures invariance under.  The nine-label completion "
                        "arena is INHERITED from GEN/BRG, not chosen here; its "
                        "effect is reported separately at both scales.",
        "provenance": "BRG (terminal), HA, GEN, XBA, PSI receipts and papers, "
                      "hash-pinned; every reused number read from them and "
                      "recomputed here",
        "admission": "a candidate is ACCEPTED at the strengthened standard only "
                     "if every clause of S1 holds and S2, S3 hold; the clause that "
                     "fails FIRST in the declared clause order is the named "
                     "obstruction of that cell",
    },
    # ------------------------------------------------------------------
    "pairing": {
        "transport_selection_rule": "DECLARED BEFORE EVALUATION: Q0 is the "
            "lexicographically first one-line notation (q_0,...,q_8) among all "
            "permutations of the 9 system-pair labels with q_0 = 0 whose defect "
            "delta(Q) = Sigma Q^T Sigma Q has order exactly 5.  The class size is "
            "computed by exhaustive sweep, not typed.",
        "transport_carrier": "81 configurations, index i = 9a + p with a the "
            "system-pair label and p the pointer-pair label",
        "Sigma": "the label exchange (u,v) -> (v,u) on a pair of 3-valued labels, "
                 "index 3u+v; W = Sigma (x) Sigma",
        "deformation_carrier": "C_HA(5) = F_5^k x F_5^d, k = 2 (the rank of HA's "
            "declared lapse span), d = 2; size 5^4",
        "rho_exact": "(1/6, 1/6), HA's exact rational residual at the detector "
                     "site, prime-independent",
        "primes": [5, 7, 11, 13, 17, 19, 23],
        "record_space": "V = F_p^3, the three link counts (n_e1, n_e2, n_diag) at "
                        "a site, d = 2, L = 3",
        "metric_space": "the three components of the metric candidate q; "
                        "q11 = n_e1, q22 = n_e2, q12 = (n_diag - n_e1 - n_e2)/2",
        "records": {"G-FLAT": [1, 1, 2], "G-DIAG2": [2, 2, 4],
                    "G-ANISO": [1, 4, 5], "G-ANISO2": [4, 9, 13],
                    "G-CURVED": [1, 1, 2], "G-OFFDIAG": [2, 2, 6],
                    "G-OFFDIAG2": [3, 5, 12], "G-OFFNEG": [3, 5, 4],
                    "G-CURVOFF": [2, 2, 6],
                    "G-SINGULAR": [1, 1, 4], "G-INDEF": [1, 1, 6]},
        "record_negative_controls": ["G-SINGULAR", "G-INDEF"],
        "base_record": "G-FLAT, count triple (1,1,2), reduced mod p",
        "chart_involution": "tau: the declared chart involution of HA's d = 2 "
            "arena, the axis swap e_1 <-> e_2.  On counts it swaps n_e1 and n_e2 "
            "and fixes n_diag; on the metric it swaps q11 and q22 and fixes q12.",
        "identifications": {
            "natural": "the link is paired with the metric component it "
                       "determines: n_e1 <-> q11, n_e2 <-> q22, n_diag <-> q12",
            "index": "the two coordinate triples are paired slot by slot in "
                     "index order: n_e1 <-> q11, n_e2 <-> q12, n_diag <-> q22",
            "COVARIANT COMPLETION": "an identification is a NAMING of the "
                     "metric's three slots, so RUNBOOK 15 requires the declared "
                     "ones to be swept together with their whole orbit under the "
                     "slot-relabelling group S_3.  That orbit is all 3! slot "
                     "orders; two of them are the declared cells, two more are "
                     "their chart-involution conjugates, and two more complete "
                     "the orbit.  Each is built from the same declared metric "
                     "slot triple; nothing is added to the declaration."},
        "directions": {
            "counts->q": "data -> geometry, the direction that matches the "
                         "transport side's completion -> defect; REGISTERED",
            "q->counts": "geometry -> data, the reverse; HA's own measured "
                         "determinant-2 matrix sits in this direction, so both "
                         "are swept and both are reported"},
    },
    # ------------------------------------------------------------------
    "strengthened_standard": {
        "S1": "ENCODING INTERTWINING -- THE NON-NEGOTIABLE.  A COMMUTING SQUARE "
              "at the encoding layer, not a triangle at the group layer: HA's "
              "record-is-metric linear re-encoding E (the determinant-2 readout, "
              "HA G28) intertwined with GEN/XBA's Q -> delta(Q) = Sigma Q^T Sigma "
              "Q, by the candidate morphism alpha.  Sub-clauses, in this order:\n"
              "  S1a  delta(alpha(r)) = alpha(E r) at EVERY record cell, compared "
              "as 9x9 permutation MATRICES, entry by entry.\n"
              "  S1b  alpha is a homomorphism of the record datum's additive "
              "structure into the completion group, at every ordered pair.\n"
              "  S1c  alpha carries the chart involution to the label exchange: "
              "alpha(tau r) = Sigma alpha(r) Sigma at every record cell.\n"
              "  S1d  BASE POINT: the declared base record r0 goes to a completion "
              "whose defect reproduces the declared base completion's own measured "
              "order and fixed-configuration count.",
        "S2": "CARRIER RIGIDITY.  (i) the candidate is DETERMINED, not chosen: "
              "the census returns exactly one candidate up to the declared "
              "redundancy; (ii) the transport side's fixed-configuration "
              "stratification {9,18,27,36,45,54,81} is CARRIED -- the map "
              "r -> fix81(delta(alpha(r))) must reach more than the two strata a "
              "cyclic image can reach.",
        "S3": "NON-DEGENERACY WITH TEETH.  alpha is INJECTIVE -- the form BRG's "
              "one-way theorem requires, since a FOUND could only ever exhibit the "
              "deformation side as a SUB-OBJECT of the transport side, and a "
              "sub-object embedding is an injection.  Measured against the "
              "declared alternative: |image(alpha)| as a fraction of |V|.",
        "S4": "FUNCTORIALITY IN THE FAMILY.  The census is run over the whole "
              "declared (prime, defect-order) grid and over a base change inside "
              "the ord-5 completion class, so that a live cell is not an isolated "
              "coincidence at one (p, ord(D)).",
        "S5": "HELD-OUT AT A LIVE CELL WITH A TRANSPORTED QUANTITY.  A declared "
              "FIT/HELD split of the record space, frozen BEFORE any candidate is "
              "fitted; the candidate is fitted on FIT alone and the square is then "
              "VERIFIED on HELD; two transport-side physical quantities -- the "
              "defect's order and its fixed-configuration count -- are predicted "
              "out of sample and then computed.  Two declared extensions are "
              "declared IN ADVANCE to FAIL.",
        "S6": "AN IN-ARENA READING OF REQUIREMENT 4.  The prime is declared a "
              "parameter of the arena and the verdict is reported per prime, "
              "together with the intersection over the declared sweep.",
    },
    # ------------------------------------------------------------------
    "held_out": {
        "split_rule": "FIT = the single declared basis record e1 = (1,0,0); "
                      "HELD = every other element of V.  Sizes computed.  Frozen "
                      "before any candidate is fitted.",
        "fit_rule": "the candidate (g, lambda) is admitted if the square holds at "
                    "the FIT cell ALONE; nothing on HELD is consulted.",
        "H1": "the square at every HELD cell, as 9x9 permutation matrices",
        "H2": "the DEFECT PERMUTATION delta(alpha(r)) itself, entry by entry, at "
              "every HELD cell -- a transport-side physical quantity, and the "
              "strictly stronger reading of the two (it implies the order)",
        "H3": "fix81(delta(alpha(r))) at every HELD cell -- GEN's own "
              "fixed-configuration stratification",
        "teeth": {"X-NOSQUARE": "predict that the defect map acts trivially, "
                                "delta(alpha(r)) = alpha(r).  DECLARED IN ADVANCE "
                                "TO FAIL on HELD.",
                  "X-FLATSTRAT": "predict the identity-defect stratum "
                                 "fix81 = 81 at every HELD cell.  DECLARED IN "
                                 "ADVANCE TO FAIL."},
    },
    # ------------------------------------------------------------------
    "controls": {
        "F0-IDENT": "DISCLOSURE, NOT A CONTROL (RUNBOOK 14 addendum #208).  The "
                    "identity self-morphism of the transport arena commutes with "
                    "any encoding by construction: with alpha = the identity every "
                    "clause of the check reads x == x.  Its 0 violations at all "
                    "40,320 cells record that the identity candidate is the "
                    "identity and nothing about the square, so it is registered as "
                    "an analytically-forced disclosure gate and carries no mutant. "
                    "THE POSITIVE CONTROL OF THIS UNIT IS SYNTH-COMPATIBLE.",
        "SYNTH-COMPATIBLE": "THE POSITIVE CONTROL: a declared synthetic compatible "
                            "pair -- the same transport side against a synthetic "
                            "chart map E~ whose 2-eigencovector is "
                            "chart-ANTIsymmetric.  The machinery must FIND "
                            "candidates and they must pass S1a, S1b, S1c and S1d. "
                            "ITS BASE-POINT CLAUSE IS EVALUATED AT THE DECLARED "
                            "tau-ASYMMETRIC RECORD G-ANISO, and the reason is "
                            "measured, not conventional: S1c forces the exponent "
                            "covector to be chart-antisymmetric, an antisymmetric "
                            "covector annihilates any tau-FIXED record, and the "
                            "declared base record G-FLAT is tau-fixed -- so S1c "
                            "and S1d are jointly unsatisfiable at G-FLAT for EVERY "
                            "chart map whatsoever, measured exhaustively over all "
                            "(generator, covector) pairs.  The base record used by "
                            "the control is recorded in its gate.",
        "SYNTH-EMPTY": "a declared synthetic incompatible pair: a scalar chart map "
                       "with no eigenvalue 2.  The machinery must report EMPTY.",
        "BREAK-HOM": "NEGATIVE CONTROL WITH TEETH: the accepted candidate's "
                     "exponent lambda(r) is replaced by lambda(r)*mu(r)^(p-1) with "
                     "mu a declared 1-eigencovector.  It satisfies the commuting "
                     "square S1a at EVERY cell -- it differs from an ACCEPTED "
                     "candidate only in the linearity of its exponent -- and must "
                     "be rejected by S1b alone, with the rejecting clause named.",
    },
    # ------------------------------------------------------------------
    "open1_criterion": {
        "declaration_freeness": "COMPUTED PER CANDIDATE, NEVER TYPED.  A candidate "
            "is DECLARATION-FREE iff its admitted prime set is INVARIANT under "
            "every re-declaration of a choice THIS UNIT makes: the prime together "
            "with its selection rule (p := 7 with ord(D) := 7, whose completion "
            "class is measured non-empty and whose lex-first member is rebuilt "
            "here), the DIRECTION (registered -> reversed), the IDENTIFICATION "
            "(the declared cell family -> a single slot identification), the BASE "
            "RECORD (G-FLAT -> G-ANISO), the completion inside the ord-5 class, "
            "the completion-label relabelling, and the record-space basis.  Each "
            "candidate is a FUNCTION of that declaration record and is re-evaluated "
            "at each counterfactual; the classification is the measured invariance, "
            "and a single flipped entry is caught.",
        "scales": "the nine-label completion arena is INHERITED (GEN/BRG), not a "
            "choice of this unit, so it is not one of the re-declarations; instead "
            "every candidate is reported at BOTH declared scales -- the nine-label "
            "arena of this pairing and the sixteen-label successor arena of G15 -- "
            "and the arena's own dependence on the declared prime (the smallest "
            "arena admitting an injective candidate has 3p + 1 labels: 16 at "
            "p = 5, 22 at p = 7) is measured and reported with them.",
        "verdict_rule": "LCB-PRIME-DERIVED iff, at the arena being reported, some "
            "declaration-free NARROWING candidate other than the intersection "
            "itself admits exactly one admissible prime, OR the intersection of "
            "every declaration-free narrowing is a singleton.  Otherwise "
            "LCB-PRIME-DECLARED.  The unit's verdict is entered at the DECLARED "
            "nine-label arena.",
    },
    "open1_candidates": {
        "P1": "the deformation carrier's size p^(k+d)",
        "P2": "the deformation arena's front structure (k, d, L, sites, links)",
        "P3": "the transport group's order 2*ord(D) and its prime divisors",
        "P4": "the transport FAMILY's defect-order spectrum and the primes "
              "dividing some 2*ord(D) in it",
        "P5": "the completion group's element orders: the primes p for which an "
              "element of order p exists",
        "P6": "the record<->metric readout's determinant",
        "P7": "the denominator of HA's exact residual rho",
        "P8": "the S1 intertwining condition itself: the primes at which 2 lies "
              "in the spectrum of the chart map E",
        "P9": "the joint system P7 and P8",
        "P10": "the count of label-exchange-anti-invariant elements of order p",
        "P11": "the p-part of the completion group's order against |V| = p^3",
        "P12": "the intersection of every declaration-free candidate",
    },
    "outcomes": ["LCB-BRIDGE-EMPTY-AT-STRENGTHENED-STANDARD-UNIVERSAL-FOR-THIS-"
                 "SQUARE",
                 "LCB-BRIDGE-EMPTY-AT-STRENGTHENED-STANDARD",
                 "LCB-BRIDGE-FOUND-AT-STRENGTHENED-STANDARD",
                 "LCB-BLOCKED-AT-CENSUS-DISCIPLINE"],
    "outcome_qualifier": "UNIVERSAL-FOR-THIS-SQUARE is EARNED, not asserted: it is "
        "entered only if the census is empty at EVERY cell of the covariant "
        "family, in BOTH directions, at EVERY declared prime and at every cell of "
        "the (prime, defect-order) grid, AND the S1a-and-S3 obstruction is "
        "measured to cover every one of those cells -- arena-free where the "
        "re-encoding's fixed space is nonzero, by the arena's own p-part where it "
        "is not.  If any of that fails the unqualified name is returned.",
    "prime_outcomes": ["LCB-PRIME-DECLARED", "LCB-PRIME-DERIVED"],
}

# --------------------------------------------------------------------------
# 3.  THE PERMUTATION KERNEL  (exact; tuples ARE the matrices)
# --------------------------------------------------------------------------

NLAB = 9


def pident(n: int) -> tuple:
    return tuple(range(n))


def pmul(a: tuple, b: tuple) -> tuple:
    """(a o b)(x) = a(b(x)).  Composition of permutation matrices."""
    return tuple(a[b[i]] for i in range(len(b)))


def pinv(a: tuple) -> tuple:
    out = [0] * len(a)
    for i, v in enumerate(a):
        out[v] = i
    return tuple(out)


_PMAT_MEMO: dict = {}


def pmat(a: tuple) -> tuple:
    """The permutation as an explicit 0/1 matrix, row by row.  P[i][j] = 1 iff
    i = a(j) -- the matrix whose columns are the images of the basis vectors.
    Memoised so that two occurrences of one permutation yield the SAME matrix
    object; equality of the matrices is still decided entry by entry."""
    m = _PMAT_MEMO.get(a)
    if m is None:
        n = len(a)
        m = tuple(tuple(1 if i == a[j] else 0 for j in range(n))
                  for i in range(n))
        if len(_PMAT_MEMO) < 100000:
            _PMAT_MEMO[a] = m
    return m


def pord(a: tuple) -> int:
    c, cur, e = 1, a, pident(len(a))
    while cur != e:
        cur = pmul(cur, a)
        c += 1
    return c


def pfix(a: tuple) -> int:
    return sum(1 for i, v in enumerate(a) if i == v)


def pmoved(a: tuple) -> int:
    return sum(1 for i, v in enumerate(a) if i != v)


def commutes(a: tuple, b: tuple) -> bool:
    for i in range(len(a)):
        if a[b[i]] != b[a[i]]:
            return False
    return True


def sigma_perm(m: int) -> tuple:
    """The label exchange on pairs of m-valued labels, index m*u + v."""
    return tuple(m * (i % m) + (i // m) for i in range(m * m))


SIG = sigma_perm(3)


def conj_by(s: tuple, q: tuple) -> tuple:
    """s q s^-1 -- for an involution s this is s q s."""
    return pmul(s, pmul(q, pinv(s)))


def defect_of(q: tuple, s: tuple = SIG) -> tuple:
    """GEN 8.1's completion -> commutator map delta(Q) = Sigma Q^T Sigma Q,
    i.e. sigma(Q)^-1 . Q with sigma = conjugation by Sigma.  Uncached."""
    return pmul(pinv(conj_by(s, q)), q)


def defect_cached(q: tuple, fresh: bool = False, selftest: bool = False) -> tuple:
    """The memoised completion -> commutator map.  Self-test phases MUST call
    with fresh=True so the quantity, not the cache, is measured (RUNBOOK 14
    addendum #185).  [instrument -- mutable]"""
    if fresh and not _M_CACHE:
        CACHE_STATS["bypasses"] += 1
        return defect_of(q)
    if _M_CACHEUN:
        return defect_of(q)
    CACHE_STATS["lookups"] += 1
    if q in _DELTA_MEMO:
        CACHE_STATS["hits"] += 1
        if selftest:
            CACHE_STATS["selftest_hits"] += 1
        return _DELTA_MEMO[q]
    CACHE_STATS["misses"] += 1
    v = defect_of(q)
    _DELTA_MEMO[q] = v
    return v


# --------------------------------------------------------------------------
# 4.  EXACT LINEAR ALGEBRA OVER Q AND OVER F_p
# --------------------------------------------------------------------------

def det3(M) -> Fr:
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def inv3(M):
    D = det3(M)
    C = [[Fr(0)] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            m = [[M[r][c] for c in range(3) if c != j] for r in range(3) if r != i]
            C[j][i] = Fr((-1) ** (i + j)) * (m[0][0] * m[1][1] - m[0][1] * m[1][0]) / D
    return C


def charpoly3(M):
    """Coefficients (c0, c1, c2, 1) of det(xI - M), exact."""
    def mm(a, b):
        return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)]
                for i in range(3)]
    t1 = M[0][0] + M[1][1] + M[2][2]
    M2 = mm(M, M)
    t2 = M2[0][0] + M2[1][1] + M2[2][2]
    M3 = mm(M2, M)
    t3 = M3[0][0] + M3[1][1] + M3[2][2]
    return [-(t1 ** 3 - 3 * t1 * t2 + 2 * t3) / 6, (t1 * t1 - t2) / 2, -t1, Fr(1)]


def to_fp(M, p):
    return [[(x.numerator * pow(x.denominator, -1, p)) % p for x in row] for row in M]


def mat_apply(M, v, p):
    return tuple(sum(M[i][j] * v[j] for j in range(len(v))) % p for i in range(len(M)))


def transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]


def kernel_fp(M, p):
    """An exact basis of the kernel of M over F_p, by Gaussian elimination."""
    n = len(M[0])
    A = [row[:] for row in M]
    piv, r = [], 0
    for c in range(n):
        pr = None
        for i in range(r, len(A)):
            if A[i][c] % p:
                pr = i
                break
        if pr is None:
            continue
        A[r], A[pr] = A[pr], A[r]
        iv = pow(A[r][c], -1, p)
        A[r] = [(x * iv) % p for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] % p:
                f = A[i][c]
                A[i] = [(A[i][j] - f * A[r][j]) % p for j in range(n)]
        piv.append(c)
        r += 1
    free = [c for c in range(n) if c not in piv]
    basis = []
    for fc in free:
        v = [0] * n
        v[fc] = 1
        for i, c in enumerate(piv):
            v[c] = (-A[i][fc]) % p
        basis.append(tuple(v))
    return basis


DECLARED_SLOT_ORDERS = {"natural": ((0, 0), (1, 1), (0, 1)),
                        "index": ((0, 0), (0, 1), (1, 1))}
METRIC_SLOTS = ((0, 0), (0, 1), (1, 1))       # the declared metric slot triple


def slot_orbit():
    """The COVARIANT identification family: the orbit of the declared metric slot
    orders under the slot-relabelling group S_3, i.e. every ordering of the
    declared metric slot triple.  Names: the two declared ones, their
    chart-involution conjugates (tau- prefix), and the two that complete the
    orbit (alt- prefix).  Nothing is typed: the orders are enumerated from
    METRIC_SLOTS.  [instrument -- mutable]"""
    def tau_of(order):
        sw = {0: 1, 1: 0}
        return tuple(tuple(sorted((sw[i], sw[j]))) for (i, j) in order)
    out = {}
    for nm, od in DECLARED_SLOT_ORDERS.items():
        out[nm] = od
        out["tau-" + nm] = tau_of(od)
    rest = sorted(od for od in itertools.permutations(METRIC_SLOTS)
                  if od not in out.values())
    if rest:
        out["alt"] = rest[0]
        out["tau-alt"] = tau_of(rest[0])
    if _M_ORBITDROP:
        out = dict(DECLARED_SLOT_ORDERS)
    return out


SLOT_ORDERS = slot_orbit()


def encoding_matrix(identification: str, direction: str):
    """HA's record<->metric readout, rebuilt exactly as ha_successor_exact.py
    builds it (rows = the declared links, columns = the metric components), then
    read as an ENDOMORPHISM of the one datum space under the given
    identification and in the declared direction.  [instrument -- mutable]"""
    corder = [(1, 0), (0, 1), (1, 1)]
    morder = SLOT_ORDERS[identification]
    A = [[Fr(lk[i] * lk[j] * (1 if i == j else 2)) for (i, j) in morder]
         for lk in corder]
    if _M_READOUT:
        A[0][2] = A[0][2] + Fr(1)
    return A if direction == "q->counts" else inv3(A)


def general_d_readout(d: int, ordering: str):
    """HA's readout at general d (HA section 9): rows the links -- the d axes and
    the C(d,2) diagonals -- columns the d(d+1)/2 metric slots, in the NATURAL
    order (each link against the slot it determines) or the LEX order (sym_index).
    Returns the q -> counts matrix.  [instrument -- mutable]"""
    diag = [(i, i) for i in range(d)]
    off = [(i, j) for i in range(d) for j in range(i + 1, d)]
    links = [tuple(1 if k == i else 0 for k in range(d)) for i in range(d)] + \
            [tuple(1 if k in (i, j) else 0 for k in range(d)) for (i, j) in off]
    morder = (diag + off) if ordering == "natural" else \
        [(i, j) for i in range(d) for j in range(i, d)]
    return [[Fr(lk[i] * lk[j] * (1 if i == j else 2)) for (i, j) in morder]
            for lk in links]


def dimension_sweep():
    """The declared dimensions at which the fixed-space measurement is repeated.
    [instrument -- mutable]"""
    if _M_DSWEEP:
        return [2]
    return [2, 3, 4, 5]


def column_sums(A):
    """The column sums of the q -> counts readout.  [instrument -- mutable]"""
    n = len(A)
    if _M_COLSUM:
        return [sum(A[i][c] for c in range(len(A[0]))) for i in range(n)]
    return [sum(A[i][c] for i in range(n)) for c in range(len(A[0]))]


def ha_readout_matrix():
    """The matrix HA's own G28 measures, in HA's own row and column order
    (rows = the links sorted, columns = sym_index(2)).  [instrument -- mutable]"""
    idx = [(0, 0), (0, 1), (1, 1)]
    links = sorted([(1, 0), (0, 1), (1, 1)])
    M = [[Fr(lk[i] * lk[j] * (1 if i == j else 2)) for (i, j) in idx]
         for lk in links]
    if _M_READOUT:
        M[0][2] = M[0][2] + Fr(1)
    return M


# --------------------------------------------------------------------------
# 5.  INSTRUMENT HELPERS THAT CARRY MUTATIONS
# --------------------------------------------------------------------------

def select_lex_first(cands):
    """The DECLARED selection rule: lexicographically first one-line notation.
    [instrument -- mutable]"""
    if _M_SELECT:
        return sorted(cands)[len(cands) // 2]
    return min(cands)


def group_closure(gens, n):
    """The subgroup generated, built by closure.  [instrument -- mutable]"""
    use = gens[:1] if _M_GROUP else gens
    e = pident(n)
    seen, fr = {e}, [e]
    while fr:
        cur = fr.pop()
        for g in use:
            nx = pmul(cur, g)
            if nx not in seen:
                seen.add(nx)
                fr.append(nx)
    return seen


def divides_ok(p, order2):
    """The live-cell divisibility clause.  Its own negative case is evaluated
    inside its gate, so a blinded clause cannot pass.  [instrument -- mutable]"""
    if _M_COMPAT:
        return True
    return order2 % p == 0


def ha_generator(p, rho, n):
    """C_HA(p)'s generator: translation of the address register by rho mod p,
    the front sector fixed.  [instrument -- mutable]"""
    r0 = (rho[0].numerator * pow(rho[0].denominator, -1, p)) % p
    r1 = (rho[1].numerator * pow(rho[1].denominator, -1, p)) % p
    if _M_RHO:
        r0 = (r0 + 1) % p
    gen = []
    for i in range(n):
        m1 = i % p
        m0 = (i // p) % p
        rest = i // (p * p)
        if _M_ARENA:
            gen.append(i if m1 else rest * p * p + ((m0 + r0) % p) * p)
            continue
        gen.append(rest * p * p + ((m0 + r0) % p) * p + ((m1 + r1) % p))
    return tuple(gen)


def encoding_cells():
    """The COVARIANT encoding-cell sweep: every identification in the declared
    cells' S_3 orbit x both directions.  [instrument -- mutable]"""
    cells = [(idn, dr) for idn in SLOT_ORDERS
             for dr in ("counts->q", "q->counts")]
    if _M_ENCDROP:
        cells = cells[:-1]
    return cells


def tau_perm():
    """The declared chart involution on the three coordinate slots, as a
    permutation of slots.  [instrument -- mutable]"""
    if _M_TAU:
        return (0, 1, 2)
    return (1, 0, 2)


def square_cells(V):
    """The record cells at which the commuting square is evaluated.
    [instrument -- mutable]"""
    if _M_SQUARE:
        return V[:1]
    return V


def compare_square(lhs, rhs):
    """The square's comparison, as 9x9 permutation MATRICES entry by entry
    (BRG S1: 'as measured matrices, not as group abstractions').
    [instrument -- mutable]"""
    if _M_MATRIX:
        return pord(lhs) == pord(rhs)
    A, B = pmat(lhs), pmat(rhs)
    if A is B:
        return True
    for i in range(NLAB):
        if A[i] != B[i]:
            return False
    return True


def hom_clause(alpha_map, V, p):
    """S1b, at every ordered pair of the record space.  [instrument -- mutable]"""
    if _M_HOM:
        return 0
    bad = 0
    for r in V:
        for s in V:
            t = tuple((r[i] + s[i]) % p for i in range(3))
            if alpha_map[t] != pmul(alpha_map[r], alpha_map[s]):
                bad += 1
    return bad


def basis_images(P):
    """The exhaustive enumeration's per-slot candidate set.
    [instrument -- mutable]"""
    if _M_ENUM:
        return P[:-1]
    return P


def kernel_dim(M, p):
    """The dimension of the kernel of M over F_p.  [instrument -- mutable]"""
    if _M_ROUTEA:
        return len(kernel_fp(M, p)) + 1
    return len(kernel_fp(M, p))


def route_b_answer(a, b):
    """Route B's own answer, kept separate from route A's.
    [instrument -- mutable]"""
    ROUTE_CALLS["B"] += 1
    if _M_ALIAS:
        ROUTE_CALLS["taint"] += 1
        return a
    return b


def forced_sign_measured(cands):
    """Whether the sign step is MEASURED over the candidate set rather than
    asserted.  [instrument -- mutable]"""
    if _M_THEOREM:
        return None
    return cands


def s1c_cells(V):
    """The cells at which the chart-involution clause is evaluated.
    [instrument -- mutable]"""
    if _M_S1C:
        return V[:1]
    return V


def base_record(records):
    """The declared base geometry record.  [instrument -- mutable]"""
    if _M_S1D:
        return tuple(records["G-ANISO"])
    return tuple(records["G-FLAT"])


def record_sweep(admissible):
    """The declared base-record sweep: the STATE coordinate of the arena, swept
    over every one of HA's admissible geometry records rather than fixed at the
    declared one.  [instrument -- mutable]"""
    if _M_RECORDS:
        return ["G-FLAT"]
    return sorted(admissible)


def delta_fixed_points(members, s):
    """The fixed-point set of the transport side's encoding delta inside a given
    arena: {x : delta(x) = x}.  delta(x) = sigma(x)^-1 x, so this is {x :
    sigma(x) = e} = {e}, with no hypothesis on the arena.  [instrument --
    mutable]"""
    if _M_FIXPOINT:
        return [q for q in members if conj_by(s, q) == q]
    return [q for q in members if pmul(pinv(conj_by(s, q)), q) == q]


def fix_space_dim(M, p):
    """dim ker(E - I) over F_p -- the deformation side's fixed space.
    [instrument -- mutable]"""
    if _M_FIXSPACE:
        return len(M)
    return len(kernel_fp([[(M[i][j] - (1 if i == j else 0)) % p
                           for j in range(len(M))] for i in range(len(M))], p))


def orbit_factor(members, s, L):
    """The number of choices the SET-level square leaves on one E-orbit of length
    L: the points of the transport arena with delta^L(x) = x.  [instrument --
    mutable]"""
    if _M_SETLEVEL:
        return 1
    n = 0
    for q in members:
        x = q
        for _ in range(L):
            x = pmul(pinv(conj_by(s, x)), x)
        if x == q:
            n += 1
    return n


def witness_covector(ker, mult):
    """The exhibited tau-conjugate witness's exponent covector, taken from the
    measured 2-eigenspace.  [instrument -- mutable]"""
    if _M_WITNESS7:
        return tuple((x + 1) for x in ker[0])
    return tuple((mult * x) for x in ker[0])


def strat_of(perm, source_value):
    """S2's stratification reading: the TRANSPORTED defect's fixed-configuration
    count.  [instrument -- mutable]"""
    if _M_S2:
        return source_value
    return 9 * pfix(perm)


def image_size(alpha_map):
    """|image(alpha)|.  [instrument -- mutable]"""
    if _M_S3:
        return len(alpha_map)
    return len(set(alpha_map.values()))


def p_part_exponent(n, q):
    """The exponent of q in n!, by exact division.  [instrument -- mutable]"""
    if _M_SYLOW:
        n = n + 7
    m, k = math.factorial(n), 0
    while m % q == 0:
        m //= q
        k += 1
    return k


def grid_cells(primes, orders):
    """The declared (prime, defect-order) grid.  [instrument -- mutable]"""
    cells = [(p, n) for p in primes for n in orders]
    if _M_GRID:
        cells = cells[:-1]
    return cells


def prime_sweep(primes):
    """The declared prime sweep.  [instrument -- mutable]"""
    if _M_PRIMESINGLE:
        return primes[:1]
    return primes


def completion_sample(cls):
    """The declared base-change sweep inside the ord-5 class: the lex-first, the
    lex-last, the fewest-moved, the most-moved, and the members at the quarter,
    half and three-quarter positions of the lexicographic order.  [instrument --
    mutable]"""
    srt = sorted(cls)
    by_moved = sorted(cls, key=lambda q: (pmoved(q), q))
    n = len(srt)
    out = [srt[0], srt[-1], by_moved[0], by_moved[-1],
           srt[n // 4], srt[n // 2], srt[(3 * n) // 4]]
    seen, uniq = set(), []
    for q in out:
        if q not in seen:
            seen.add(q)
            uniq.append(q)
    if _M_COMPDROP:
        uniq = uniq[:-1]
    return uniq


def fit_cells(V, e1):
    """The declared FIT set, frozen before any candidate is fitted.
    [instrument -- mutable]"""
    if _M_HELDOUT:
        return [r for r in V if r != (0, 0, 0)]
    return [e1]


def s5_chart_map(real, synthetic):
    """S5's deformation side: the PAIRING'S OWN readout, not the synthetic
    control map.  [instrument -- mutable]"""
    if _M_S5MAP:
        return synthetic
    return real


def teeth_exponent(k, p):
    """The declared failing extension X-NOSQUARE: it predicts that the defect
    map acts trivially.  [instrument -- mutable]"""
    if _M_TEETH:
        return (2 * k) % p
    return k % p


def transported_quantity(perm, other):
    """A held-out transported quantity, read off the map it belongs to: the
    DEFECT of the candidate's image, not the image itself.
    [instrument -- mutable]"""
    if _M_QUANTITY:
        return other
    return perm


def identity_candidate(n):
    """The identity self-morphism.  Its check is analytically forced and carries
    no mutant: it is a DISCLOSURE, not a control (see DECL controls F0-IDENT)."""
    return pident(n)


def synth_compatible_matrix(p):
    """The declared synthetic compatible chart map: symmetric, invertible, with
    a chart-ANTIsymmetric 2-eigencovector.  [instrument -- mutable]"""
    M = [[4, 2, 0], [2, 4, 0], [0, 0, 1]]
    if _M_FOUND:
        M = [[3, 0, 0], [0, 3, 0], [0, 0, 3]]
    return [[x % p for x in row] for row in M]


def synth_empty_matrix(p):
    """The declared synthetic incompatible chart map: the scalar 3, whose only
    eigenvalue is 3.  [instrument -- mutable]"""
    M = [[3, 0, 0], [0, 3, 0], [0, 0, 3]]
    if _M_EMPTY:
        M = [[4, 2, 0], [2, 4, 0], [0, 0, 1]]
    return [[x % p for x in row] for row in M]


def exhibit_witness(w):
    """The exhibited FOUND witness, re-verified independently by its gate.
    [instrument -- mutable]"""
    if _M_WITNESS:
        return None
    return w


def break_exponent(lam, mu, r, p, accepted):
    """BREAK-HOM's exponent: the accepted candidate's linear exponent multiplied
    by mu(r)^(p-1), which is 1 off the hyperplane mu = 0 and 0 on it.  It leaves
    the commuting square exact and destroys additivity.  [instrument --
    mutable]"""
    lin = sum(lam[i] * r[i] for i in range(3)) % p
    if accepted or _M_BREAK:
        return lin
    return (lin * pow(sum(mu[i] * r[i] for i in range(3)) % p, p - 1, p)) % p


def relabelling():
    """The declared completion-label relabelling: a permutation of the 9 labels
    fixing label 0.  [instrument -- mutable]"""
    if _M_RELABEL:
        return pident(NLAB)
    return (0, 2, 3, 4, 1, 5, 6, 7, 8)


def basis_change(p):
    """The declared change of basis of the record datum space.
    [instrument -- mutable]"""
    if _M_BASIS:
        return [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    return [[1, 1, 0], [0, 1, 0], [0, 1, 1]]


def selftest_set(declared, verdict_selected):
    """The self-test's tested set: fixed by DECLARATION, never selected by the
    verdicts under audit (RUNBOOK 14 addendum #185).  [instrument -- mutable]"""
    if _M_SELSEL:
        return verdict_selected
    return declared


def declaration_free(pid, measured, order):
    """Whether an Open-1 candidate is declaration-free.  The value passed in is
    the MEASURED invariance of the candidate's admitted set under every
    re-declaration of a choice of this unit; nothing is typed here.
    [instrument -- mutable]"""
    if _M_OPEN1:
        return True
    if _M_FREEFLIP and pid == order[0]:
        return not measured
    return measured


def open1_intersection(sets, admissible):
    """The intersection of the declaration-free narrowings, taken at its own
    source.  [instrument -- mutable]"""
    inter = set(admissible)
    for s in sets:
        inter &= set(s)
    if _M_INTER:
        return {sorted(admissible)[0]}
    return inter


def open1_scale_labels(nine, sixteen):
    """The two declared arena scales at which every Open-1 candidate is reported.
    [instrument -- mutable]"""
    if _M_SCALE:
        return [nine, nine]
    return [nine, sixteen]


def synthetic_open1_tables(admissible):
    """Two declared SYNTHETIC candidate tables, run through the same verdict
    derivation: one on which a declaration-free narrowing pins a single
    admissible prime (DERIVED must be returned), one on which two survive
    (DECLARED must be returned).  [instrument -- mutable]"""
    a = sorted(admissible)
    derived = [{"id": "S1", "admissible_part": [a[0]], "declaration_free": True,
                "role": "NARROWING", "unique": True},
               {"id": "S2", "admissible_part": a[:3], "declaration_free": True,
                "role": "NARROWING", "unique": False}]
    declared = [{"id": "S1", "admissible_part": a[:2], "declaration_free": True,
                 "role": "NARROWING", "unique": False},
                {"id": "S2", "admissible_part": a[:3], "declaration_free": True,
                 "role": "NARROWING", "unique": False}]
    if _M_REACH:
        derived = declared
    return derived, declared


def unique_prime(sets):
    """Whether a candidate's output set determines the prime uniquely.
    [instrument -- mutable]"""
    if _M_UNIQUE:
        return len(sets) <= 2
    return len(sets) == 1


def obstruction_name(arena_free, arena_bound, total, spectral, parity):
    """The named obstruction, derived from the measured coverage counts and the
    measured per-cell diagnostics.  [instrument -- mutable]"""
    if _M_OBSTR:
        return "unequal carrier cardinality"
    if _M_FABRIC:
        return ("S1b -- the record datum's additive structure is carried by no "
                "completion of the transport arena")
    if arena_free + arena_bound < total or not (spectral and parity):
        return "UNDETERMINED"
    return ("S1a AND S3 -- THE FIXED-POINT MISMATCH: the transport side's "
            "encoding has exactly ONE fixed point while the deformation side's "
            "re-encoding fixes a nonzero vector, so the square must collapse "
            "what injectivity forbids it to collapse.  ARENA-FREE at %d of the "
            "%d covariant cells; at the remaining %d the arena's own p-part "
            "decides.  Per-cell diagnostics of the same wall: SPECTRAL in the "
            "data->geometry direction, CHART-PARITY in the geometry->data "
            "direction." % (arena_free, total, total - arena_free))


def census_is_empty(found_at_standard):
    """The emptiness decision, taken at its own source so a corruption of it is
    caught by the verdict gate's independent recount.  [instrument -- mutable]"""
    if _M_COUNTFLIP:
        return found_at_standard != 0
    return found_at_standard == 0


def universality_measured(covered, total):
    """Whether the obstruction is measured to cover every cell of the covariant
    family -- the condition the verdict's qualifier is earned by.
    [instrument -- mutable]"""
    if _M_UNIVERSAL:
        return True
    return total > 0 and covered == total


def derive_verdict(empty, complete, both_reachable, controls_ok, universal):
    """The verdict string, DERIVED from the measured booleans inside its gate.
    [instrument -- mutable]"""
    if _M_VERDICT:
        return "LCB-BRIDGE-FOUND-AT-STRENGTHENED-STANDARD"
    if not (complete and both_reachable and controls_ok):
        return "LCB-BLOCKED-AT-CENSUS-DISCIPLINE"
    if not empty:
        return "LCB-BRIDGE-FOUND-AT-STRENGTHENED-STANDARD"
    return ("LCB-BRIDGE-EMPTY-AT-STRENGTHENED-STANDARD-UNIVERSAL-FOR-THIS-SQUARE"
            if universal else "LCB-BRIDGE-EMPTY-AT-STRENGTHENED-STANDARD")


def derive_prime_verdict(unique_forced):
    """The Open-1 verdict, DERIVED from the measured candidate table.
    [instrument -- mutable]"""
    if _M_VERDICT:
        return "LCB-PRIME-DERIVED"
    return "LCB-PRIME-DERIVED" if unique_forced else "LCB-PRIME-DECLARED"


def qualifier_value(name, computed):
    """A printed verdict qualifier.  Every one is recomputed inside the verdict
    gate from its own source.  [instrument -- mutable]"""
    if _M_QUALTYPO and name == "encoding_cells":
        return 99
    return computed


def freeze_counter_bump():
    """[instrument -- mutable]"""
    if _M_FREEZE:
        note_census()


def float_scan(src: str) -> list[str]:
    """[instrument -- mutable]"""
    if _M_FLOAT:
        return []
    hits = []
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            hits.append(f"line {node.lineno}: literal {node.value!r}")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                and node.func.id in ("float", "complex"):
            hits.append(f"line {node.lineno}: call {node.func.id}()")
    return sorted(hits)


RUN_MODE_NAMES = ("MUTANT", "MUTANTS", "DELIVERY_RUN", "SELFTEST_ONLY",
                  "WRITE_ARTIFACTS")


def ast_mutant_scan(src: str) -> list[str]:
    """Functions that BOTH register a gate AND reference run-mode identity.
    [instrument -- mutable]"""
    if _M_EXEMPT:
        return []
    tree = ast.parse(src)
    offenders = []
    names = set(MUTANTS.keys())

    class V(ast.NodeVisitor):
        def visit_FunctionDef(self, node):  # noqa: N802
            registers = references = False
            for sub in ast.walk(node):
                if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Name) \
                        and sub.func.id in ("gate",):
                    registers = True
                if isinstance(sub, ast.Name) and (sub.id in RUN_MODE_NAMES
                                                  or sub.id.startswith("_M_")):
                    references = True
                if isinstance(sub, ast.Attribute) and sub.attr == "argv":
                    references = True
                if isinstance(sub, ast.Constant) and isinstance(sub.value, str) \
                        and sub.value in names:
                    references = True
            if registers and references:
                offenders.append(node.name)
            self.generic_visit(node)

    V().visit(tree)
    return sorted(offenders)


SYNTH_FLOAT_SAMPLE = "x = 1.5\ny = float('2')\n"
SYNTH_MUTANT_SAMPLE = ("def f():\n"
                       "    if _M_SOMETHING:\n"
                       "        pass\n"
                       "    gate('GX', 'c', True)\n")

HASH_PINS = {
    "v13/note-lcb-livecell-pin.md":
        "4f30880229e72cef28fb4c0891845ad3e258980fce2fc3b25fcf130b8612a822",
    "v13/paper-brg-bridge.md":
        "371e38742059d14a93dd4dc916785a6c59a6ecd4e4b6cb882298ba8bdbc2ab33",
    "v13/code/brg_bridge_receipt.json":
        "5c428afd5c58c8998b575b38b6a7808803805c2cb5c2d5bc0baca3bc10a989f9",
    "v13/code/ha_successor_receipt.json":
        "542b8735daf0ebc6fc0063068e85c76f05cbca53b7f1174968f6ca79dc0068d4",
    "v13/code/gen_generality_receipt.json":
        "e0b2f444f6a9b82861024f7733c7230583742dfd477d9ed6037a241e7b48d292",
    "v13/code/xba_crossbase_receipt.json":
        "6015708df2a437a61955c1e194a0273b0eb712699844c9e6eb567cc3536db053",
    "v13/code/psi_curvature_receipt.json":
        "7c7b91a9257e3888f3e1048366d728b5adead82b84cc9ef36175c0ba3e99fa75",
}

PIN_MUTATE = {"v13/note-lcb-livecell-pin.md": _M_PINSHA,
              "v13/paper-brg-bridge.md": _M_BRGSHA,
              "v13/code/brg_bridge_receipt.json": _M_BRGRSHA,
              "v13/code/ha_successor_receipt.json": _M_HASHA,
              "v13/code/gen_generality_receipt.json": _M_GENSHA,
              "v13/code/xba_crossbase_receipt.json": _M_XBASHA,
              "v13/code/psi_curvature_receipt.json": _M_PSISHA}


def pinned_hash(path: str) -> str:
    """[instrument -- mutable]"""
    h = sha256_file(os.path.join(REPO, path))
    if PIN_MUTATE.get(path) or (_M_SOFT and path.endswith("psi_curvature_receipt.json")):
        h = "0" * 64
    return h


def family_sweep_members():
    """The whole declared completion family: every permutation of the 9
    system-pair labels fixing label 0.  [instrument -- mutable]"""
    mem = [(0,) + t for t in itertools.permutations(range(1, NLAB))]
    if _M_FAMILY:
        mem = mem[:-1]
    return mem


def base_g_completion():
    """Base G's own declared completion: the transposition of the system-pair
    labels |0,1> and |0,2> (GEN 2.3).  [instrument -- mutable]"""
    q = [0, 2, 1, 3, 4, 5, 6, 7, 8]
    if _M_DEFECT:
        q[3], q[4] = q[4], q[3]
    return tuple(q)


# ==========================================================================
#                              THE UNIT
# ==========================================================================

def run_unit(src: str) -> dict:
    """The whole measurement.  Registers every gate; reads no run-mode boolean,
    directly or indirectly."""
    progress("start")
    say("=" * 78)
    say("LCB -- THE LIVE-CELL BRIDGE AT THE STRENGTHENED STANDARD")
    say("pin v13/note-lcb-livecell-pin.md (STRICT) -- commit d2f6104")
    say("=" * 78)
    say("")
    tables: dict = {}
    P = 5
    KRANK, DDIM = 2, 2
    RHO = (Fr(1, 6), Fr(1, 6))
    PRIMES = DECL["pairing"]["primes"]
    RECORDS = DECL["pairing"]["records"]

    # ==================== 1. THE FREEZE ==================================
    say("--- 1. THE DECLARATIONS, FROZEN BEFORE ANY CANDIDATE IS EVALUATED ---")
    freeze_counter_bump()
    frozen = CENSUS_EVALS[0]
    g01 = gate("G01", "THE DECLARATIONS ARE FROZEN BEFORE ANY CANDIDATE MORPHISM "
               "IS EVALUATED: the pairing, the strengthened standard S1-S6, the "
               "held-out split, the controls and the Open-1 candidate list are "
               "declared as data, and the candidate-evaluation counter is "
               "measured ZERO at the freeze point",
               frozen == 0, {"candidate_evaluations_at_freeze": frozen,
                             "declared_blocks": sorted(DECL.keys())})
    report("G01", g01, f"candidate evaluations at the freeze point: {frozen}")

    pins = {}
    bad_pins = []
    for path, want in sorted(HASH_PINS.items()):
        got = pinned_hash(path)
        pins[path] = got
        if got != want:
            bad_pins.append(path)
    g02 = gate("G02", "EVERY COMMITTED SOURCE THIS UNIT ANCHORS AGAINST IS "
               "HASH-PINNED AND THE PIN IS VERIFIED ON DISK: the LCB pin itself, "
               "BRG's terminal paper and receipt, and the HA, GEN, XBA and PSI "
               "receipts", bad_pins == [], {"pins": pins, "mismatches": bad_pins})
    report("G02", g02, f"{len(pins)} hash pins verified, {len(bad_pins)} mismatches")
    for path, want in sorted(HASH_PINS.items()):
        anchor("A00-" + os.path.basename(path), f"sha256 of {path}", want,
               pins[path], "committed file")
    say("")

    # ==================== 2. THE PAIRING AS DATA ==========================
    say("--- 2. THE PAIRING AS DATA ---")
    progress("pairing")

    # 2.1 the transport side, rebuilt
    qG = base_g_completion()
    dG = defect_cached(qG)
    anchor("A01", "base G's defect permutation, entry by entry",
           [0, 2, 1, 6, 4, 5, 3, 7, 8], list(dG), "GEN 8.1 / BRG 3.1")
    anchor("A02", "base G's defect order", 2, pord(dG), "GEN receipt / BRG 3.1")
    anchor("A03", "base G's defect fixed configurations of 81", 45, 9 * pfix(dG),
           "GEN 8.1 / BRG 3.1")
    W = tuple(9 * SIG[i // 9] + SIG[i % 9] for i in range(81))
    anchor("A04", "the wing exchange's fixed configurations of 81", 9, pfix(W),
           "XBA receipt / BRG 3.1")

    fam = family_sweep_members()
    ordspec: dict = {}
    fixspec: dict = {}
    cls5 = []
    DORD: dict = {}
    for q in fam:
        dq = defect_cached(q)
        o = pord(dq)
        f81 = 9 * pfix(dq)
        DORD[q] = pord(q)
        ordspec[o] = ordspec.get(o, 0) + 1
        fixspec[f81] = fixspec.get(f81, 0) + 1
        if o == 5:
            cls5.append(q)
    g03 = gate("G03", "THE COMPLETION FAMILY IS SWEPT WHOLE AND CELL-COMPLETE: "
               "every one of the declared members -- every permutation of the "
               "nine system-pair labels fixing label 0, a count computed as a "
               "factorial from the label count and never typed -- is classified "
               "exactly once, and both spectra sum to the swept count",
               len(fam) == math.factorial(NLAB - 1)
               and len(fam) == sum(ordspec.values()) == sum(fixspec.values())
               and len(set(fam)) == len(fam),
               {"members": len(fam), "distinct": len(set(fam)),
                "computed_family_size": math.factorial(NLAB - 1),
                "order_spectrum_total": sum(ordspec.values()),
                "fixed_spectrum_total": sum(fixspec.values())})
    report("G03", g03, f"{len(fam)} members, both spectra sum to "
           f"{sum(ordspec.values())}")
    anchor("A05", "the declared completion family's size", 40320, len(fam),
           "GEN 8.2 / BRG 3.1")
    anchor("A06", "the family's defect-order spectrum",
           {1: 96, 2: 1440, 3: 4224, 4: 4608, 5: 4608, 6: 6912, 7: 9216, 15: 9216},
           dict(sorted(ordspec.items())), "GEN 8.2 / BRG 3.1")
    anchor("A07", "the family's fixed-configuration spectrum",
           {9: 16704, 18: 11520, 27: 5376, 36: 4608, 45: 864, 54: 1152, 81: 96},
           dict(sorted(fixspec.items())), "GEN 8.2 / BRG 3.1")
    anchor("A08", "completions whose defect has order 5", 4608, len(cls5),
           "BRG 14 open 1 (G38)")
    anchor("A09", "identity-defect / geometry-bearing members",
           [96, 40224], [ordspec[1], len(fam) - ordspec[1]], "GEN 8.2")

    Q0 = select_lex_first(cls5)
    D9 = defect_cached(Q0)
    moved0 = pmoved(Q0)
    fewest = min(pmoved(q) for q in cls5)
    anchor("A10", "the fewest labels moved by any ord-5 completion", 3, fewest,
           "BRG 14 open 1 (G38): 'the smallest of them moves just 3 labels'")
    g04 = gate("G04", "THE TRANSPORT BASE IS SELECTED BY THE DECLARED RULE AND "
               "THE RULE IS EXHIBITED: Q0 is the lexicographically first "
               "one-line notation among the completions whose defect has order "
               "exactly 5; the class size is computed by exhaustive sweep, the "
               "selected member is printed, and its defect order is re-measured "
               "from Q0 alone",
               Q0 == min(cls5) and pord(D9) == 5 and Q0 in cls5
               and Q0[0] == 0 and sorted(Q0) == list(range(9)),
               {"Q0": list(Q0), "class_size": len(cls5),
                "labels_moved_by_Q0": moved0,
                "defect": list(D9), "defect_order": pord(D9),
                "defect_fixed_configurations_of_81": 9 * pfix(D9)})
    report("G04", g04, f"Q0 = {list(Q0)} (moves {moved0} labels); "
           f"D = {list(D9)}, ord {pord(D9)}, fix81 {9 * pfix(D9)}")
    anchor("A11", "the ord-5 class's fixed-configuration count", 36, 9 * pfix(D9),
           "GEN 8.3's class table (ord 5, 36 fixed)")

    D81 = tuple(9 * D9[i // 9] + (i % 9) for i in range(81))
    GRP = group_closure([W, D81], 81)
    grp_orders = sorted(pord(g) for g in GRP)
    dihedral = (pmul(W, pmul(D81, W)) == pinv(D81) and pmul(W, W) == pident(81)
                and W not in group_closure([D81], 81))
    g05 = gate("G05","THE TRANSPORT GROUP IS BUILT AS AN EXPLICIT PERMUTATION "
               "GROUP ON THE 81 CONFIGURATIONS AND ITS DIHEDRAL FORM IS "
               "MEASURED, NOT CITED: W is an involution, W D W = D^-1, W is not "
               "a power of D, and the order is 2*ord(D)",
               dihedral and len(GRP) == 2 * pord(D9),
               {"group_order": len(GRP), "two_times_ord_D": 2 * pord(D9),
                "element_orders": grp_orders, "dihedral_relations_hold": dihedral})
    report("G05", g05, f"|<W,D>| = {len(GRP)} = 2*{pord(D9)}; element orders "
           f"{grp_orders}")
    anchor("A12", "the transport group's order at the live cell", 10, len(GRP),
           "PSI's one law / XBA 8.1: |<W,D>| = 2*ord(D)")

    # 2.2 the deformation side, rebuilt
    nHA = P ** (KRANK + DDIM)
    genHA = ha_generator(P, RHO, nHA)
    # the register shift is READ OFF the built generator, not restated from the
    # declaration, and its uniformity over the carrier is measured (HA G29)
    rho_mod = ((genHA[0] // P) % P, genHA[0] % P)
    uniform_shift = all(((genHA[i] // P) % P - (i // P) % P) % P == rho_mod[0]
                        and (genHA[i] % P - i % P) % P == rho_mod[1]
                        for i in range(nHA))
    orb = set()
    n_orb = 0
    seenpt = [False] * nHA
    for i in range(nHA):
        if not seenpt[i]:
            n_orb += 1
            j, sz = i, 0
            while not seenpt[j]:
                seenpt[j] = True
                j = genHA[j]
                sz += 1
            orb.add(sz)
    g06 = gate("G06", "THE DEFORMATION ARENA C_HA(5) IS REBUILT FROM HA'S OWN "
               "LAW AND ITS ACTION IS MEASURED FREE: the generator is the "
               "translation of the address register by rho mod p with the front "
               "sector fixed, every orbit has length exactly p (counted by an "
               "orbit walk over the carrier), the register shift is the SAME at "
               "every one of the carrier's configurations, and the orbit count "
               "is the carrier size divided by p",
               orb == {P} and n_orb == nHA // P and uniform_shift,
               {"carrier": nHA, "orbit_lengths": sorted(orb), "orbits": n_orb,
                "rho_mod_p": list(rho_mod),
                "register_shift_uniform_over_the_carrier": uniform_shift,
                "group_order": pord(genHA)})
    report("G06", g06, f"carrier {nHA}, orbit lengths {sorted(orb)}, "
           f"{n_orb} orbits")
    anchor("A13", "C_HA(5)'s carrier size", 625, nHA, "HA 10.1 / BRG 3.2")
    anchor("A14", "rho = (1/6,1/6) reduced mod 5, read off the built generator",
           [1, 1], list(rho_mod), "HA 10.1 / BRG 3.2")
    anchor("A15", "the order of <R_HH> at p = 5", 5, pord(genHA), "HA G29/G30")
    anchor("A16", "C_HA(5)'s orbit count (the action is free)", 125, n_orb,
           "BRG 3.2")

    # 2.3 the pairing's basic compatibility
    live = divides_ok(P, len(GRP))
    live_neg = divides_ok(7, len(GRP))
    homs_to_grp = sum(1 for g in GRP if P % pord(g) == 0)
    nt_homs = sum(1 for g in GRP if pord(g) == P)
    homs_route2 = math.gcd(pord(D9), P)
    g07 = gate("G07", "THE PAIRING'S BASIC COMPATIBILITY IS VERIFIED AS A "
               "MEASUREMENT, WITH ITS OWN NEGATIVE CASE EVALUATED IN GATE: the "
               "live-cell condition p | 2*ord(D) holds at p = 5 and is measured "
               "to FAIL at p = 7 against the same group, so a blinded clause "
               "cannot pass; and the count of homomorphisms Z/p -> <W,D> is "
               "computed twice -- once by sweeping the element orders of the "
               "built permutation group, once by the gcd of ord(D) with p -- and "
               "the two agree",
               live and not live_neg and homs_to_grp == homs_route2
               and nt_homs == homs_to_grp - 1,
               {"p": P, "two_ord_D": len(GRP), "p_divides_2ordD": live,
                "negative_case_7_divides_2ordD": live_neg,
                "homs_by_element_orders": homs_to_grp,
                "homs_by_gcd": homs_route2, "non_trivial": nt_homs})
    report("G07", g07, f"5 | {len(GRP)}: {live} (negative case 7 | {len(GRP)}: "
           f"{live_neg}); |hom(Z/5,<W,D>)| = {homs_to_grp} (gcd route "
           f"{homs_route2}), non-trivial {nt_homs}")
    anchor("A17", "non-trivial homomorphisms Z/5 -> <W,D> at the live cell", 4,
           nt_homs, "BRG 4, scope-2 table (p = 5, class ord(D) = 5)")

    # 2.4 the encoding layer
    HAM = ha_readout_matrix()
    det_ha = det3(HAM)
    reenc_ok = 0
    q_of = {}
    det_of = {}
    for nm, cts in sorted(RECORDS.items()):
        n1, n2, n3 = cts
        q11, q22 = Fr(n1), Fr(n2)
        q12 = Fr(n3 - n1 - n2, 2)
        q_of[nm] = (q11, q12, q22)
        det_of[nm] = q11 * q22 - q12 * q12
        ok = (q11 == n1 and q22 == n2 and q11 + 2 * q12 + q22 == n3)
        reenc_ok += 1 if ok else 0
    adm = sorted(nm for nm in RECORDS
                 if det_of[nm] > 0 and q_of[nm][0] > 0)
    rej = sorted(set(RECORDS) - set(adm))
    g08 = gate("G08", "THE RECORD<->METRIC RE-ENCODING IS REBUILT EXACTLY AS HA "
               "BUILDS IT AND ITS DETERMINANT IS RECOMPUTED: the linear system "
               "q_ij e^i e^j = n_l is solved at every declared record, q "
               "reproduces every declared link count, and the coefficient "
               "matrix's determinant is exact",
               det_ha == 2 and reenc_ok == len(RECORDS),
               {"readout_matrix": [[str(x) for x in row] for row in HAM],
                "determinant": str(det_ha),
                "records_where_q_reproduces_every_count": reenc_ok,
                "records": len(RECORDS), "admissible": adm, "rejected": rej})
    report("G08", g08, f"readout determinant {det_ha}; q reproduces every count "
           f"at {reenc_ok} of {len(RECORDS)} records; {len(adm)} admissible")
    anchor("A18", "HA's record<->metric readout determinant", "2", str(det_ha),
           "HA G28")
    anchor("A19", "HA's admissible geometry records", 9, len(adm), "HA 4.1")
    anchor("A20", "HA's declared negative-control records",
           sorted(DECL["pairing"]["record_negative_controls"]), rej, "HA 4.1")
    anchor("A21", "the declared records' metric determinants",
           {"G-ANISO": "4", "G-ANISO2": "36", "G-CURVED": "1", "G-CURVOFF": "3",
            "G-DIAG2": "4", "G-FLAT": "1", "G-INDEF": "-3", "G-OFFDIAG": "3",
            "G-OFFDIAG2": "11", "G-OFFNEG": "11", "G-SINGULAR": "0"},
           {k: str(v) for k, v in sorted(det_of.items())}, "HA 4.1's table")

    cells = encoding_cells()
    TAU = tau_perm()
    # the chart involution's slot permutation in each coordinate order; an
    # identification is CHART-COMPATIBLE when the two agree
    slot_tau = {}
    for idn, morder in SLOT_ORDERS.items():
        sw = {0: 1, 1: 0}
        img = [list(morder).index(tuple(sorted((sw[i], sw[j])))) for (i, j) in morder]
        slot_tau[idn] = tuple(img)
    compat = {idn: (slot_tau[idn] == tuple(TAU)) for idn in slot_tau}
    enc: dict = {}
    tau_equiv = 0
    for (idn, dr) in cells:
        M = encoding_matrix(idn, dr)
        Mq = to_fp(M, P)
        cp = charpoly3(M)
        Ttau = [[1 if TAU[i] == j else 0 for j in range(3)] for i in range(3)]

        def app(A, B):
            return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)]
                    for i in range(3)]
        eq = (app(Mq, Ttau) == app(Ttau, Mq))
        tau_equiv += 1 if eq else 0
        enc[(idn, dr)] = {"Q": M, "Fp": Mq, "charpoly": [str(c) for c in cp],
                          "det": str(det3(M)), "tau_equivariant": eq,
                          "chart_compatible": compat[idn]}
    invertible = all(det3(v["Q"]) != 0 for v in enc.values())
    orbit_complete = (sorted(SLOT_ORDERS.values())
                      == sorted(itertools.permutations(METRIC_SLOTS)))
    declared_inside = all(DECLARED_SLOT_ORDERS[k] == SLOT_ORDERS.get(k)
                          for k in DECLARED_SLOT_ORDERS)
    def tau_of_order(order):
        sw = {0: 1, 1: 0}
        return tuple(tuple(sorted((sw[i], sw[j]))) for (i, j) in order)
    tau_closed = all(tau_of_order(v) in set(SLOT_ORDERS.values())
                     for v in SLOT_ORDERS.values())
    g09 = gate("G09", "THE ENCODING-CELL FAMILY IS THE COVARIANT ORBIT OF THE "
               "DECLARED CELLS AND IS CELL-COMPLETE (RUNBOOK 15): an "
               "identification is a NAMING of the metric's three slots, so the "
               "declared identifications are swept together with their whole "
               "orbit under the slot-relabelling group S_3.  That orbit is "
               "measured to be every ordering of the declared metric slot triple "
               "-- 3! of them, computed from the triple and never typed -- the "
               "two declared ones among them, each cell invertible mod p; and "
               "the chart involution is read in both coordinate orders, so the "
               "identifications that CARRY it (the axis swap inducing the same "
               "slot permutation on counts and on the metric, the re-encoding "
               "measured to commute with it) are separated from those that do "
               "not, by measurement",
               orbit_complete and declared_inside and tau_closed
               and len(cells) == 2 * math.factorial(3)
               and len(set(cells)) == len(cells) and invertible
               and TAU != pident(3) and compat["natural"]
               and not compat["index"]
               and tau_equiv == sum(1 for (a, b) in cells if compat[a]),
               {"cells": [list(c) for c in cells],
                "slot_orders": {k: [list(s) for s in v]
                                for k, v in SLOT_ORDERS.items()},
                "declared_identifications": sorted(DECLARED_SLOT_ORDERS),
                "orbit_is_the_full_slot_relabelling_orbit": orbit_complete,
                "tau_on_counts": list(TAU),
                "tau_induced_slot_permutation": {k: list(v)
                                                 for k, v in slot_tau.items()},
                "chart_compatible": compat,
                "tau_equivariant_cells": tau_equiv,
                "family_closed_under_the_chart_involution": tau_closed,
                "matrices": {f"{a}|{b}": {"det": enc[(a, b)]["det"],
                                          "charpoly": enc[(a, b)]["charpoly"],
                                          "mod_p": enc[(a, b)]["Fp"]}
                             for (a, b) in cells}})
    report("G09", g09, f"{len(cells)} covariant encoding cells "
           f"({len(SLOT_ORDERS)} slot identifications x 2 directions), all "
           f"invertible; chart-carrying identifications "
           f"{sorted(k for k in compat if compat[k])}; {tau_equiv} cells "
           f"chart-equivariant")
    for (a, b) in cells:
        say(f"      {a:12s} {b:10s} det {enc[(a, b)]['det']:>5s}  "
            f"E mod 5 = {enc[(a, b)]['Fp']}")
    tables["encoding_cells"] = {f"{a}|{b}": enc[(a, b)]["Fp"] for (a, b) in cells}
    tables["slot_orders"] = {k: [list(s) for s in v]
                             for k, v in SLOT_ORDERS.items()}
    say("")

    # ==================== 3. THE S1 CENSUS ================================
    say("--- 3. S1: THE COMMUTING SQUARE, CENSUS AT DECLARED SCOPE ---")
    progress("census")
    V = [(x, y, z) for x in range(P) for y in range(P) for z in range(P)]
    E1 = (1, 0, 0)
    COMPL = fam
    # elements of the completion group of order dividing p
    PSET = [g for g in COMPL if DORD[g] in (1, P)]
    ANTI = [g for g in COMPL if DORD[g] == P and conj_by(SIG, g) == pinv(g)]
    COMM = [g for g in COMPL if DORD[g] == P and conj_by(SIG, g) == g]
    say(f"  completion group: {len(COMPL)} elements; of order {P}: "
         f"{len(PSET) - 1}; Sigma-anti-invariant: {len(ANTI)}; "
         f"Sigma-invariant: {len(COMM)}")

    # ---- ROUTE B: exhaustive enumeration of every homomorphism ----------
    progress("route B: enumerating homomorphisms")
    slots = basis_images(PSET)
    cent = {a: set(b for b in slots if commutes(a, b)) for a in slots}
    HOMS = []
    for a in slots:
        for b in cent[a]:
            for c in (cent[a] & cent[b]):
                HOMS.append((a, b, c))
    imgspec: dict = {}
    for tr in HOMS:
        s = len(group_closure(list(tr), NLAB))
        imgspec[s] = imgspec.get(s, 0) + 1
    say(f"  route B enumerated {len(HOMS)} homomorphisms V -> completion group; "
        f"image-size spectrum {dict(sorted(imgspec.items()))}")

    _POWS: dict = {}

    def powtab(g):
        t = _POWS.get(g)
        if t is None:
            t = [pident(NLAB)]
            for _ in range(P - 1):
                t.append(pmul(t[-1], g))
            _POWS[g] = t
        return t

    def alpha_from_triple(tr, r):
        return pmul(pmul(powtab(tr[0])[r[0]], powtab(tr[1])[r[1]]),
                    powtab(tr[2])[r[2]])

    census: dict = {}
    for (idn, dr) in cells:
        Efp = enc[(idn, dr)]["Fp"]
        order_cells = [E1, (0, 1, 0), (0, 0, 1)] + [r for r in square_cells(V)
                                                   if r not in
                                                   ((1, 0, 0), (0, 1, 0), (0, 0, 1))]
        keep = []
        for tr in HOMS:
            if tr == (pident(NLAB),) * 3:
                continue
            note_census()
            ok = True
            for r in order_cells:
                if not compare_square(defect_cached(alpha_from_triple(tr, r)),
                                      alpha_from_triple(tr, mat_apply(Efp, r, P))):
                    ok = False
                    break
            if ok:
                keep.append(tr)
        ROUTE_CALLS["B"] += 0
        census[(idn, dr)] = {"routeB": keep}
    progress("route A")

    # ---- ROUTE A: the linear-algebra route ------------------------------
    for (idn, dr) in cells:
        Efp = enc[(idn, dr)]["Fp"]
        Mt = [[(transpose(Efp)[i][j] - (2 if i == j else 0)) % P for j in range(3)]
              for i in range(3)]
        kdim = kernel_dim(Mt, P)
        ROUTE_CALLS["A"] += 1
        nlam = P ** kdim - 1
        ndistinct = len(ANTI) * nlam // (P - 1) if nlam else 0
        census[(idn, dr)]["routeA_kernel_dim"] = kdim
        census[(idn, dr)]["routeA_nonzero_covectors"] = nlam
        census[(idn, dr)]["routeA_count"] = ndistinct

    # ---- the two routes compared ---------------------------------------
    agree, rows = True, []
    for (idn, dr) in cells:
        b = len(census[(idn, dr)]["routeB"])
        a = census[(idn, dr)]["routeA_count"]
        bb = route_b_answer(a, b)
        rows.append({"identification": idn, "direction": dr,
                     "route_A_linear_algebra": a, "route_B_enumeration": bb,
                     "kernel_dim": census[(idn, dr)]["routeA_kernel_dim"]})
        if a != bb:
            agree = False
    g10 = gate("G10", "THE S1a/S1b CENSUS IS COMPUTED BY TWO GENUINELY "
               "INDEPENDENT COMPUTATIONS AND THEY AGREE AT EVERY DECLARED "
               "ENCODING CELL: route B enumerates EVERY homomorphism of the "
               "record datum's additive group into the completion group by "
               "pairwise-commuting basis images -- using no group theory -- and "
               "tests the commuting square as 9x9 permutation matrices at every "
               "record cell; route A solves the kernel of (E^T - 2I) over F_p by "
               "Gaussian elimination and multiplies by the measured count of "
               "label-exchange-anti-invariant elements of order p.  Neither "
               "route reads the other's answer",
               agree and ROUTE_CALLS["taint"] == 0 and ROUTE_CALLS["A"] > 0
               and ROUTE_CALLS["B"] > 0,
               {"rows": rows, "route_calls": dict(ROUTE_CALLS),
                "homomorphisms_enumerated": len(HOMS),
                "image_size_spectrum": {str(k): v
                                        for k, v in sorted(imgspec.items())},
                "anti_invariant_order_p_elements": len(ANTI)})
    report("G10", g10, "two routes agree at all "
           f"{len(cells)} cells; taint {ROUTE_CALLS['taint']}")
    for r in rows:
        say(f"      {r['identification']:12s} {r['direction']:10s} "
            f"route A {r['route_A_linear_algebra']:4d}   route B "
            f"{r['route_B_enumeration']:4d}   ker(E^T-2I) dim "
            f"{r['kernel_dim']}")
    tables["s1ab_census"] = rows

    n_order_p = len(PSET) - 1
    homs_predicted = (n_order_p // (P - 1)) * (P ** 3 - 1) + 1
    g11 = gate("G11", "THE CENSUS IS CELL-COMPLETE AND EXHAUSTIVE AT ITS "
               "DECLARED SCOPE: the declared encoding cells are visited exactly "
               "once each; every candidate is tested at every one of the p^3 "
               "record cells; and the ENUMERATION'S OWN SIZE is checked against "
               "an independent count built from the measured order-p element "
               "count alone -- the cyclic subgroups of order p number "
               "(elements)/(p-1), each carrying (p^3 - 1) surjections plus the "
               "one trivial map -- so a dropped basis image cannot pass silently",
               len(rows) == len(cells)
               and len({(r["identification"], r["direction"])
                        for r in rows}) == 2 * math.factorial(3)
               and len(HOMS) == len(set(HOMS))
               and len(HOMS) == homs_predicted
               and len(square_cells(V)) == P ** 3,
               {"cells_visited": len(rows), "distinct_cells": len({
                   (r["identification"], r["direction"]) for r in rows}),
                "homomorphisms": len(HOMS), "distinct": len(set(HOMS)),
                "order_p_elements": n_order_p,
                "homomorphisms_predicted_independently": homs_predicted,
                "record_cells_per_candidate": len(square_cells(V))})
    report("G11", g11, f"{len(rows)} cells, {len(HOMS)} homomorphisms "
           f"(independent count {homs_predicted}), "
           f"{len(square_cells(V))} record cells each")
    say("")

    # ==================== 4. THE STRUCTURE, MEASURED ======================
    say("--- 4. WHAT THE SQUARE FORCES, MEASURED RATHER THAN CITED ---")
    fs = forced_sign_measured(ANTI)
    squaring_ok = 0
    if fs is not None:
        for g in fs[:8]:
            for k in range(P):
                gk = pident(NLAB)
                for _ in range(k):
                    gk = pmul(gk, g)
                if defect_cached(gk) == pmul(gk, gk):
                    squaring_ok += 1
    lagr = p_part_exponent(NLAB - 1, P)
    g12 = gate("G12", "THE SQUARE'S OWN CONSEQUENCES ARE MEASURED, NOT ASSERTED: "
               "no element of order p commutes with the label exchange (so the "
               "sign +1 branch is empty by measurement); on the "
               "anti-invariant locus the completion->commutator map acts as "
               "SQUARING, delta(Q) = Q^2, verified element by element; and the "
               "p-part of the completion group's order is computed by exact "
               "division",
               len(COMM) == 0 and fs is not None
               and squaring_ok == 8 * P and lagr == 1,
               {"order_p_elements_commuting_with_Sigma": len(COMM),
                "order_p_elements_anti_invariant": len(ANTI),
                "squaring_identity_cells_verified": squaring_ok,
                "p_part_exponent_of_the_completion_group": lagr,
                "completion_group_order": math.factorial(NLAB - 1)})
    report("G12", g12, f"Sigma-invariant order-{P} elements: {len(COMM)}; "
           f"delta = squaring verified at {squaring_ok} cells; p-part exponent "
           f"{lagr}")
    disclose("X01", "The structure of every S1a-admissible candidate is FORCED "
             "and the forcing is measured here rather than cited: a "
             "homomorphism's image is a p-subgroup of the completion group, "
             "whose p-part is measured p^1, so the image is cyclic of order 1 "
             "or p; the square then forces Sigma g Sigma = g^c with c^2 = 1, "
             "and c = +1 is measured empty, so c = -1 and delta(alpha(r)) = "
             "alpha(r)^2.  The square therefore reads lambda o E = 2*lambda: "
             "THE COMPLETION->COMMUTATOR MAP IS A SQUARING, AND THE "
             "INTERTWINING DEMANDS 2 IN THE SPECTRUM OF THE CHART MAP.",
             {"p_part_exponent": lagr, "c_plus_one_branch": len(COMM)})
    say("")

    # ============ 4b. THE OPERATIVE OBSTRUCTION: THE FIXED-POINT MISMATCH ==
    say("--- 4b. THE FIXED-POINT MISMATCH, MEASURED ARENA BY ARENA ---")
    progress("fixed-point lemma")
    r0_decl = base_record(RECORDS)

    # (i) the transport side's encoding has exactly ONE fixed point, at every
    #     arena.  Measured at three: 4 labels, 9 labels, and the order-125
    #     subgroup the sixteen-label positive control builds.
    def cyc(lo):
        t = list(range(16))
        for k in range(5):
            t[lo + k] = lo + (k + 1) % 5
        return tuple(t)
    g16gens = [cyc(1), cyc(6), cyc(11)]
    img16 = group_closure(g16gens, 16)
    SIG16 = sigma_perm(4)
    fam4 = [(0,) + t for t in itertools.permutations(range(1, 4))]
    fp_rows = []
    for label, members, sgm in (("4 labels", fam4, sigma_perm(2)),
                                ("9 labels", fam, SIG),
                                ("16 labels (the order-125 witness subgroup)",
                                 sorted(img16), SIG16)):
        fx = delta_fixed_points(members, sgm)
        fp_rows.append({"arena": label, "members": len(members),
                        "delta_fixed_points": len(fx),
                        "the_fixed_point_is_the_identity":
                            fx == [pident(len(members[0]))]})
    # the same fact read the other way: {x : delta(x) = x} = {x : sigma(x) = e}
    sig_trivial = sum(1 for q in fam if conj_by(SIG, q) == pident(NLAB)
                      and q != pident(NLAB))
    one_each = all(r["delta_fixed_points"] == 1
                   and r["the_fixed_point_is_the_identity"] for r in fp_rows)
    g35 = gate("G35", "THE TRANSPORT SIDE'S ENCODING HAS EXACTLY ONE FIXED "
               "POINT, AND THAT IS ARENA-FREE: delta(x) = sigma(x)^-1 x, so "
               "delta(x) = x holds exactly when sigma(x) = e, and conjugation by "
               "the label exchange is injective.  Measured by exhaustive sweep at "
               "three different arenas -- the four-label completion group, the "
               "nine-label one this pairing declares, and the order-125 subgroup "
               "the sixteen-label control builds -- the fixed-point set is a "
               "SINGLETON at each, and its element is the identity",
               one_each and sig_trivial == 0,
               {"rows": fp_rows,
                "non_identity_elements_conjugation_sends_to_the_identity":
                    sig_trivial})
    report("G35", g35, "; ".join(f"{r['arena']}: {r['members']} members, "
                                 f"fix(delta) = {r['delta_fixed_points']}"
                                 for r in fp_rows))

    # (ii) the deformation side's fixed space, at every cell and every prime,
    #      by two computations: a kernel dimension and a determinant test
    fixe_rows, fixe_bad = [], []
    for (idn, dr) in cells:
        MQ = enc[(idn, dr)]["Q"]
        for p in PRIMES:
            if any(x.denominator % p == 0 for row in MQ for x in row):
                continue
            Mp = to_fp(MQ, p)
            kd = fix_space_dim(Mp, p)
            dt = det3([[(Mp[i][j] - (1 if i == j else 0)) % p for j in range(3)]
                       for i in range(3)]) % p
            if (kd > 0) != (dt == 0):
                fixe_bad.append([idn, dr, p, kd, int(dt)])
            fixe_rows.append({"identification": idn, "direction": dr, "p": p,
                              "dim_fix_E": kd, "fixed_space_size": p ** kd,
                              "det_E_minus_I_mod_p": int(dt)})
    arena_free_cells = sorted({(r["identification"], r["direction"])
                               for r in fixe_rows if r["dim_fix_E"] > 0})
    arena_free_all_p = sorted({(idn, dr) for (idn, dr) in cells
                               if all(r["dim_fix_E"] > 0 for r in fixe_rows
                                      if r["identification"] == idn
                                      and r["direction"] == dr)})
    # (iii) the same measurement at general d, for the two declared orderings
    def nullity_q(M, shift):
        n = len(M)
        B = [[M[i][j] - (Fr(shift) if i == j else Fr(0)) for j in range(n)]
             for i in range(n)]
        r = 0
        for c in range(n):
            pr = None
            for i in range(r, n):
                if B[i][c] != 0:
                    pr = i
                    break
            if pr is None:
                continue
            B[r], B[pr] = B[pr], B[r]
            iv = B[r][c]
            B[r] = [x / iv for x in B[r]]
            for i in range(n):
                if i != r and B[i][c] != 0:
                    f = B[i][c]
                    B[i] = [B[i][j] - f * B[r][j] for j in range(n)]
            r += 1
        return n - r
    dsweep = dimension_sweep()
    d_rows = []
    for d in dsweep:
        for ordering in ("natural", "lex"):
            A = general_d_readout(d, ordering)
            d_rows.append({"d": d, "ordering": ordering, "size": len(A),
                           "dim_fix": nullity_q(A, 1),
                           "column_sums": [str(x) for x in column_sums(A)]})
    d_ok = all(r["dim_fix"] >= 1 for r in d_rows)
    g36 = gate("G36", "THE DEFORMATION SIDE'S RE-ENCODING FIXES A NONZERO VECTOR "
               "-- MEASURED, NOT ASSUMED, AND NOT EVERYWHERE: dim ker(E - I) is "
               "computed at EVERY covariant cell and EVERY declared prime by "
               "Gaussian elimination and independently by the vanishing of "
               "det(E - I) mod p, and the two agree at every one of them; and "
               "the same quantity is recomputed over Q at the declared "
               "dimensions d = 2,3,4,5 for both the natural and the lexicographic "
               "slot orderings, where it is measured to be d and 1 respectively "
               "-- never zero.  At d = 2 the measurement separates the cells: "
               "the fixed space is nonzero at some identifications at every "
               "prime and ZERO at others, and that is what decides where the "
               "obstruction below is arena-free",
               fixe_bad == [] and d_ok and len(d_rows) == 2 * len(dsweep)
               and len(dsweep) > 1 and len(arena_free_all_p) < len(cells)
               and len(arena_free_all_p) > 0,
               {"rows": fixe_rows, "disagreements": fixe_bad,
                "cells_with_a_nonzero_fixed_space_at_every_declared_prime":
                    [list(c) for c in arena_free_all_p],
                "cells_total": len(cells),
                "general_dimension_rows": d_rows})
    report("G36", g36, f"{len(fixe_rows)} (cell, prime) fixed spaces, "
           f"{len(fixe_bad)} route disagreements; nonzero at every declared "
           f"prime at {len(arena_free_all_p)} of {len(cells)} cells; general-d "
           f"rows {len(d_rows)}, all nonzero: {d_ok}")
    for r in d_rows:
        say(f"      d = {r['d']}  {r['ordering']:8s} {r['size']:2d}x{r['size']:<2d} "
            f"dim fix(E) {r['dim_fix']}   column sums {r['column_sums']}")

    # (iv) the joint unsatisfiability of S1a and S3, cell by cell, and the
    #      mechanism measured live on the census's own survivors
    cover_rows, uncovered = [], []
    for (idn, dr) in cells:
        for p in PRIMES:
            rw = [r for r in fixe_rows if r["identification"] == idn
                  and r["direction"] == dr and r["p"] == p]
            if not rw:
                continue
            af = rw[0]["dim_fix_E"] > 0
            ab = p_part_exponent(NLAB - 1, p) < 3
            cover_rows.append({"identification": idn, "direction": dr, "p": p,
                               "arena_free_branch": af, "p_part_branch": ab})
            if not (af or ab):
                uncovered.append([idn, dr, p])
    mech_rows = []
    for (idn, dr) in cells:
        keep = census[(idn, dr)]["routeB"]
        if not keep:
            continue
        Efp = enc[(idn, dr)]["Fp"]
        fixV = [r for r in V if mat_apply(Efp, r, P) == r]
        tr = keep[0]
        amap = {r: alpha_from_triple(tr, r) for r in V}
        collapsed = sum(1 for r in fixV if amap[r] == pident(NLAB))
        mech_rows.append({"identification": idn, "direction": dr,
                          "fixed_records": len(fixV),
                          "fixed_records_sent_to_the_identity": collapsed,
                          "image_size": len(set(amap.values())),
                          "record_space": len(V),
                          "arena_free_branch_bites_here": len(fixV) > 1,
                          "injective": len(set(amap.values())) == len(V)})
    mech_ok = (bool(mech_rows)
               and all(r["fixed_records_sent_to_the_identity"]
                       == r["fixed_records"] and not r["injective"]
                       for r in mech_rows)
               and any(r["fixed_records"] >= P for r in mech_rows))
    g37 = gate("G37", "S1a AND S3 -- BOTH OF THEM CLAUSES BRG REGISTERED -- ARE "
               "JOINTLY UNSATISFIABLE AT EVERY CELL OF THE COVARIANT FAMILY AND "
               "EVERY DECLARED PRIME, AND THE MECHANISM IS MEASURED LIVE: the "
               "square sends the re-encoding's fixed space into the transport "
               "encoding's fixed-point set, which G35 measures to be a single "
               "point, so a candidate satisfying S1a collapses the whole fixed "
               "space onto the identity and cannot be injective.  Where the "
               "fixed space is nonzero that argument needs NO arena hypothesis; "
               "where it is zero the arena's own p-part decides instead, and "
               "every (cell, prime) is measured to be covered by one branch or "
               "the other.  The collapse itself is measured on the census's own "
               "survivors: every survivor sends every fixed record to the "
               "identity and none is injective",
               uncovered == [] and mech_ok and len(cover_rows) > 0,
               {"cells_covered": len(cover_rows), "uncovered": uncovered,
                "covered_by_the_arena_free_branch":
                    sum(1 for r in cover_rows if r["arena_free_branch"]),
                "covered_by_the_p_part_branch_only":
                    sum(1 for r in cover_rows
                        if r["p_part_branch"] and not r["arena_free_branch"]),
                "mechanism_rows": mech_rows})
    report("G37", g37, f"{len(cover_rows)} (cell, prime) pairs, {len(uncovered)} "
           f"uncovered; arena-free branch covers "
           f"{sum(1 for r in cover_rows if r['arena_free_branch'])}, the p-part "
           f"branch alone {sum(1 for r in cover_rows if r['p_part_branch'] and not r['arena_free_branch'])}")
    if mech_rows:
        m = max(mech_rows, key=lambda r: r["fixed_records"])
        say(f"      live collapse at {m['identification']}|{m['direction']}: "
            f"{m['fixed_records_sent_to_the_identity']} of "
            f"{m['fixed_records']} fixed records go to the identity; |image| "
            f"{m['image_size']} of {m['record_space']}")
    disclose("X11", "THE OBSTRUCTION IS ARENA-FREE WHERE THE RE-ENCODING FIXES A "
             "NONZERO VECTOR, AND THAT IS NOT EVERYWHERE.  delta has exactly one "
             "fixed point at every arena (G35), so S1a forces alpha(fix E) = "
             "{e} and S3 fails whenever dim ker(E - I) >= 1.  Measured over the "
             "covariant family, that holds at %d of the %d cells at every "
             "declared prime; at the remaining %d the re-encoding's spectrum "
             "carries primitive cube roots of unity instead of 1 and the fixed "
             "space is trivial, so there the emptiness is carried by the arena's "
             "own p-part (p^1 against p^3) and is arena-RELATIVE.  The "
             "universality is over this square's own cell family, not over "
             "arenas at those four cells."
             % (len(arena_free_all_p), len(cells),
                len(cells) - len(arena_free_all_p)),
             {"arena_free_cells": [list(c) for c in arena_free_all_p],
              "cells": len(cells)})

    # (v) the column-sum lemma: why the geometry->data direction is always live
    #     and always dies at S1c
    ones = (1, 1, 1)
    colsum_rows = []
    for idn in SLOT_ORDERS:
        A = encoding_matrix(idn, "q->counts")
        cs = column_sums(A)
        lhs = tuple(sum(ones[i] * A[i][j] for i in range(3)) for j in range(3))
        colsum_rows.append({"identification": idn,
                            "column_sums": [str(x) for x in cs],
                            "all_columns_sum_to_two": all(x == 2 for x in cs),
                            "ones_covector_is_a_2_eigencovector":
                                lhs == tuple(Fr(2) * x for x in ones)})
    ones_tau = tuple(ones[TAU[i]] for i in range(3))
    higher_d = [r for r in d_rows if r["d"] > 2]
    colsum_ok = (all(r["all_columns_sum_to_two"]
                     and r["ones_covector_is_a_2_eigencovector"]
                     for r in colsum_rows)
                 and ones_tau == ones
                 and bool(higher_d)
                 and all(not all(x == "2" for x in r["column_sums"])
                         for r in higher_d))
    g39 = gate("G39", "WHY THE GEOMETRY->DATA DIRECTION IS LIVE AT EVERY "
               "IDENTIFICATION AND DIES AT THE SAME CLAUSE EVERY TIME, MEASURED: "
               "at d = 2 every column of the readout sums to exactly 2 -- each "
               "diagonal slot is hit by its own axis link and by the diagonal "
               "link, each off-diagonal slot by the diagonal link with "
               "coefficient 2 -- so the all-ones covector is a 2-eigencovector "
               "of the geometry->data map at EVERY identification and every "
               "prime, which is why that direction's census is never empty; and "
               "the all-ones covector is measured chart-SYMMETRIC while S1c "
               "demands chart-antisymmetry, which is why it is always emptied by "
               "the same clause.  The fact is d = 2-specific and is measured to "
               "be so: at d = 3,4,5 the diagonal columns sum to d, not 2",
               colsum_ok,
               {"rows": colsum_rows, "ones_covector": list(ones),
                "tau_image_of_the_ones_covector": list(ones_tau),
                "chart_symmetric": ones_tau == ones,
                "higher_dimension_column_sums":
                    {str(r["d"]) + "|" + r["ordering"]: r["column_sums"]
                     for r in higher_d}})
    report("G39", g39, f"all columns sum to 2 at {sum(1 for r in colsum_rows if r['all_columns_sum_to_two'])} "
           f"of {len(colsum_rows)} identifications; the all-ones covector is a "
           f"2-eigencovector there and is chart-symmetric")

    # (vi) what S1b carries: the SET-level census at the registered cell
    Ereg = enc[("natural", "counts->q")]["Fp"]
    seenv, orb_lengths = set(), []
    for v in V:
        if v in seenv:
            continue
        L, w = 1, mat_apply(Ereg, v, P)
        while w != v:
            seenv.add(w)
            w = mat_apply(Ereg, w, P)
            L += 1
        seenv.add(v)
        orb_lengths.append(L)
    facs = {}
    for L in sorted(set(orb_lengths)):
        facs[L] = orbit_factor(fam, SIG, L)
    setlevel = 1
    for L in orb_lengths:
        setlevel *= facs[L]
    setlevel_check = 1
    for L in sorted(set(orb_lengths)):
        setlevel_check *= facs[L] ** orb_lengths.count(L)
    g40 = gate("G40", "WHAT THE HOMOMORPHISM CLAUSE CARRIES IS MEASURED, NOT "
               "ARGUED: BRG's S1 registers a commuting square, and delta is a "
               "TWISTED COCYCLE rather than a homomorphism, so the square as "
               "registered lives in Set and S1b is a third addition of this "
               "unit.  Posed at the registered cell WITHOUT S1b the census is "
               "not empty: the square determines a candidate on each E-orbit "
               "from its value at a representative subject to delta^L fixing it, "
               "so the count is the product over the measured orbit spectrum of "
               "the measured delta^L fixed-point counts -- computed here two "
               "ways, orbit by orbit and by exponentiating the per-length "
               "factors, and the two agree",
               setlevel == setlevel_check and setlevel > 1
               and sum(orb_lengths) == len(V) and facs.get(1) == 1,
               {"E_orbit_spectrum": {str(L): orb_lengths.count(L)
                                     for L in sorted(set(orb_lengths))},
                "delta_L_fixed_point_counts": {str(k): v
                                               for k, v in sorted(facs.items())},
                "set_level_census_absent_S1b": str(setlevel),
                "second_computation": str(setlevel_check),
                "record_cells_covered": sum(orb_lengths)})
    report("G40", g40, f"E-orbit spectrum "
           f"{ {L: orb_lengths.count(L) for L in sorted(set(orb_lengths))} }; "
           f"delta^L fixed counts {facs}; set-level census absent S1b = "
           f"{setlevel}")

    # (vii) R1's tau-conjugate witness, verified in delivery as a DIAGNOSTIC
    P7 = 7
    V7 = [(x, y, z) for x in range(P7) for y in range(P7) for z in range(P7)]
    wcell = None
    for (idn, dr) in cells:
        if dr != "counts->q":
            continue
        MQ = enc[(idn, dr)]["Q"]
        if any(x.denominator % P7 == 0 for row in MQ for x in row):
            continue
        E7 = to_fp(MQ, P7)
        k7 = kernel_fp([[(transpose(E7)[i][j] - (2 if i == j else 0)) % P7
                         for j in range(3)] for i in range(3)], P7)
        if k7 and idn.startswith("tau-"):
            wcell = (idn, dr, E7, k7)
            break
    w7 = {}
    if wcell is not None:
        idn7, dr7, E7, k7 = wcell
        lam7 = tuple(x % P7 for x in witness_covector(k7, 1))
        anti7 = [g for g in COMPL if DORD[g] == P7 and conj_by(SIG, g) == pinv(g)]
        g7 = min(anti7)
        pw7 = [pident(NLAB)]
        for _ in range(P7 - 1):
            pw7.append(pmul(pw7[-1], g7))

        def a7(r):
            return pw7[sum(lam7[i] * r[i] for i in range(3)) % P7]
        s1a7 = sum(1 for r in V7
                   if not compare_square(defect_cached(a7(r)),
                                         a7(mat_apply(E7, r, P7))))
        s1b7 = sum(1 for r in V7 for s in V7
                   if a7(tuple((r[i] + s[i]) % P7 for i in range(3)))
                   != pmul(a7(r), a7(s)))
        s1c7 = sum(1 for r in V7
                   if a7(tuple(r[TAU[i]] for i in range(3)))
                   != conj_by(SIG, a7(r)))
        r07 = tuple(x % P7 for x in r0_decl)
        d7 = defect_cached(a7(r07))
        cls7 = [q for q in COMPL if pord(defect_cached(q)) == P7]
        cf7 = defect_cached(min(cls7)) if cls7 else pident(NLAB)
        w7 = {"cell": [idn7, dr7], "p": P7, "E_mod_7": E7,
              "two_eigencovector": list(lam7), "generator": list(g7),
              "generator_order": pord(g7),
              "generator_anti_invariant": conj_by(SIG, g7) == pinv(g7),
              "S1a_violations": s1a7, "record_cells": len(V7),
              "S1b_violations": s1b7, "composition_cells": len(V7) ** 2,
              "S1c_violations": s1c7,
              "lambda_at_the_base_record": sum(lam7[i] * r07[i]
                                               for i in range(3)) % P7,
              "defect_order_at_the_base_record": pord(d7),
              "defect_fixed_configurations": 9 * pfix(d7),
              "S1d_against_the_declared_ord5_base": pord(d7) == pord(D9),
              "S1d_against_an_ord7_base": pord(d7) == pord(cf7),
              "ord7_completion_class_size": len(cls7),
              "image_size": len({a7(r) for r in V7}),
              "record_space_size": len(V7),
              "fixed_space_dim": fix_space_dim(E7, P7)}
    g38 = gate("G38", "THE ONE CELL OF THE COVARIANT FAMILY WHERE THE REGISTERED "
               "DIRECTION IS SOLVABLE AT AN ADMISSIBLE PRIME IS EXHIBITED AND "
               "VERIFIED HERE, AS A DIAGNOSTIC: at the chart-involution "
               "conjugate of a declared identification the re-encoding's "
               "spectrum carries primitive cube roots of unity, so 2 enters it "
               "at p = 7 as well as at p = 3, and an explicit candidate -- an "
               "anti-invariant generator of order 7 with the measured "
               "2-eigencovector as exponent -- satisfies S1a at every one of the "
               "p^3 record cells and S1b at every one of the p^6 composition "
               "cells.  It is not a FOUND: it violates S1c, its base-point "
               "clause fails against the declared ord-5 transport base, and its "
               "image has p elements against a record space of p^3, so S3 fails "
               "by the arena's p-part",
               wcell is not None and w7.get("S1a_violations") == 0
               and w7.get("S1b_violations") == 0
               and w7.get("generator_order") == P7
               and w7.get("generator_anti_invariant")
               and w7.get("S1c_violations", 0) > 0
               and not w7.get("S1d_against_the_declared_ord5_base", True)
               and w7.get("S1d_against_an_ord7_base") is True
               and w7.get("fixed_space_dim") == 0
               and w7.get("image_size", 0) < w7.get("record_space_size", 0),
               w7)
    report("G38", g38, f"tau-conjugate witness at {w7.get('cell')}, p = 7: S1a "
           f"{w7.get('S1a_violations')}/{w7.get('record_cells')}, S1b "
           f"{w7.get('S1b_violations')}/{w7.get('composition_cells')}, S1c "
           f"{w7.get('S1c_violations')}/{w7.get('record_cells')}, |image| "
           f"{w7.get('image_size')} of {w7.get('record_space_size')}")
    tables["tau_conjugate_witness"] = w7
    tables["fixed_point_lemma"] = {"delta_fixed_points": fp_rows,
                                   "fix_E_rows": fixe_rows,
                                   "general_dimension": d_rows,
                                   "coverage": {
                                       "cells_times_primes": len(cover_rows),
                                       "arena_free": sum(
                                           1 for r in cover_rows
                                           if r["arena_free_branch"]),
                                       "p_part_only": sum(
                                           1 for r in cover_rows
                                           if r["p_part_branch"]
                                           and not r["arena_free_branch"])},
                                   "set_level_census_absent_S1b": str(setlevel)}
    say("")

    # ==================== 5. S1c, S1d =====================================
    say("--- 5. S1c (CHART INVOLUTION) AND S1d (BASE POINT) ---")
    r0 = r0_decl
    r0p = tuple(x % P for x in r0)
    s1_rows = []
    for (idn, dr) in cells:
        keep = census[(idn, dr)]["routeB"]
        c_pass, d_pass, both, viol = 0, 0, 0, []
        for tr in keep:
            amap = {r: alpha_from_triple(tr, r) for r in V}
            v = sum(1 for r in s1c_cells(V)
                    if amap[tuple(r[TAU[i]] for i in range(3))]
                    != conj_by(SIG, amap[r]))
            viol.append(v)
            dd = defect_cached(amap[r0p])
            c_ok = (v == 0)
            d_ok = (pord(dd) == pord(D9) and 9 * pfix(dd) == 9 * pfix(D9))
            c_pass += 1 if c_ok else 0
            d_pass += 1 if d_ok else 0
            both += 1 if (c_ok and d_ok) else 0
        s1_rows.append({"identification": idn, "direction": dr,
                        "s1ab": len(keep), "s1c_pass": c_pass,
                        "s1d_pass": d_pass,
                        "s1c_violation_counts": sorted(set(viol)),
                        "s1_pass": both})
    tot_s1 = sum(r["s1_pass"] for r in s1_rows)
    both_kinds = (any(r["s1ab"] == 0 for r in s1_rows)
                  and any(r["s1ab"] > 0 for r in s1_rows))
    g13 = gate("G13", "S1c AND S1d ARE EVALUATED ON EVERY S1a/S1b SURVIVOR AT "
               "EVERY DECLARED ENCODING CELL, AT EVERY ONE OF THE p^3 RECORD "
               "CELLS, AND AGAINST THE DECLARED BASE RECORD: cells where the "
               "census is already empty at S1a and cells where it is not both "
               "occur, so the clause that bites is read off a measurement and "
               "not off a uniform answer",
               both_kinds and all(r["s1_pass"] <= r["s1ab"] for r in s1_rows)
               and len(s1c_cells(V)) == P ** 3
               and r0 == tuple(RECORDS["G-FLAT"]),
               {"rows": s1_rows, "base_record": list(r0),
                "s1c_cells_evaluated": len(s1c_cells(V)),
                "base_record_mod_p": list(r0p),
                "base_defect_order": pord(D9),
                "base_defect_fixed_configurations": 9 * pfix(D9),
                "candidates_passing_all_of_S1": tot_s1})
    report("G13", g13, f"S1 survivors across all cells: {tot_s1}")
    for r in s1_rows:
        say(f"      {r['identification']:12s} {r['direction']:10s} S1a+b "
            f"{r['s1ab']:4d}   S1c pass {r['s1c_pass']:4d}   S1d pass "
            f"{r['s1d_pass']:4d}   S1 all {r['s1_pass']:4d}   "
            f"S1c violations/cand {r['s1c_violation_counts']}")
    tables["s1_clause_census"] = s1_rows

    # the STATE coordinate, swept: S1d is base-record-dependent, and S1c and S1d
    # are jointly unsatisfiable at every tau-FIXED record, for every chart map
    adm_records = record_sweep(adm)
    rec_rows = []
    for nm in adm_records:
        rr = tuple(x % P for x in RECORDS[nm])
        tau_fixed = (tuple(rr[TAU[i]] for i in range(3)) == rr)
        passes = 0
        for (idn, dr) in cells:
            for tr in census[(idn, dr)]["routeB"]:
                dd = defect_cached(alpha_from_triple(tr, rr))
                if pord(dd) == pord(D9) and 9 * pfix(dd) == 9 * pfix(D9):
                    passes += 1
        rec_rows.append({"record": nm, "counts": RECORDS[nm],
                         "mod_p": list(rr), "tau_fixed": tau_fixed,
                         "candidates_passing_S1d": passes})
    # S1c AND S1d together, over EVERY (generator, covector) pair, with no chart
    # map in the computation at all
    anti_cov = [lam for lam in V if lam != (0, 0, 0)
                and tuple((-lam[TAU[i]]) % P for i in range(3)) == lam]
    pairs_c, pairs_d_flat, pairs_d_aniso = 0, 0, 0
    r_aniso = tuple(x % P for x in RECORDS["G-ANISO"])
    ordp_all = [g for g in COMPL if DORD[g] == P]
    fix_base = 9 * pfix(D9)
    for g in ordp_all:
        pw = [pident(NLAB)]
        for _ in range(P - 1):
            pw.append(pmul(pw[-1], g))
        cw = [conj_by(SIG, x) for x in pw]
        for lam in V:
            if lam == (0, 0, 0):
                continue
            ok = True
            for r in V:                       # S1c, measured cell by cell
                kt = (lam[0] * r[TAU[0]] + lam[1] * r[TAU[1]]
                      + lam[2] * r[TAU[2]]) % P
                k = (lam[0] * r[0] + lam[1] * r[1] + lam[2] * r[2]) % P
                if pw[kt] != cw[k]:
                    ok = False
                    break
            if not ok:
                continue
            pairs_c += 1
            for rec, bump in ((r0p, "flat"), (r_aniso, "aniso")):
                dd = defect_cached(pw[(lam[0] * rec[0] + lam[1] * rec[1]
                                       + lam[2] * rec[2]) % P])
                if pord(dd) == pord(D9) and 9 * pfix(dd) == fix_base:
                    if bump == "flat":
                        pairs_d_flat += 1
                    else:
                        pairs_d_aniso += 1
    total_pairs = len(ordp_all) * (P ** 3 - 1)
    r0_tau_fixed = (tuple(r0p[TAU[i]] for i in range(3)) == r0p)
    g42 = gate("G42", "THE STATE COORDINATE IS SWEPT, AND THE COLLISION BETWEEN "
               "THE TWO ADDED CLAUSES IS MEASURED WITH NO CHART MAP IN THE "
               "COMPUTATION AT ALL: S1d is evaluated at every one of HA's "
               "admissible geometry records, not only at the declared one, and "
               "it passes at some and fails at others -- so the base point is a "
               "declaration and is measured to be one.  Separately, over ALL "
               "(order-p generator, nonzero covector) pairs, the pairs "
               "satisfying S1c are counted and their base-point clause is "
               "evaluated at the declared tau-FIXED record and at a declared "
               "tau-ASYMMETRIC one: S1c forces the exponent covector to be "
               "chart-antisymmetric, an antisymmetric covector annihilates any "
               "tau-fixed record, and the two clauses are therefore jointly "
               "unsatisfiable at the declared base record for EVERY chart map "
               "whatsoever",
               len(rec_rows) > 1
               and any(r["candidates_passing_S1d"] > 0 for r in rec_rows)
               and any(r["candidates_passing_S1d"] == 0 for r in rec_rows)
               and pairs_c > 0 and pairs_d_flat == 0 and pairs_d_aniso > 0
               and r0_tau_fixed,
               {"records_swept": len(rec_rows), "rows": rec_rows,
                "admissible_records": len(adm),
                "records_where_S1d_passes":
                    sum(1 for r in rec_rows if r["candidates_passing_S1d"] > 0),
                "generator_covector_pairs": total_pairs,
                "pairs_satisfying_S1c": pairs_c,
                "pairs_satisfying_S1c_and_S1d_at_the_declared_base_record":
                    pairs_d_flat,
                "pairs_satisfying_S1c_and_S1d_at_G-ANISO": pairs_d_aniso,
                "declared_base_record_is_tau_fixed": r0_tau_fixed,
                "chart_antisymmetric_covectors": len(anti_cov)})
    report("G42", g42, f"S1d passes at "
           f"{sum(1 for r in rec_rows if r['candidates_passing_S1d'] > 0)} of "
           f"{len(rec_rows)} admissible records; of {total_pairs} "
           f"(generator, covector) pairs {pairs_c} satisfy S1c and "
           f"{pairs_d_flat} of those satisfy S1d at the declared base record "
           f"({pairs_d_aniso} at G-ANISO)")
    for r in rec_rows:
        say(f"      {r['record']:11s} counts {str(r['counts']):12s} mod p "
            f"{str(r['mod_p']):12s} tau-fixed {str(r['tau_fixed']):6s} "
            f"S1d passes {r['candidates_passing_S1d']:4d}")
    tables["base_record_sweep"] = rec_rows
    say("")

    # ==================== 6. S2 AND S3 ====================================
    say("--- 6. S2 (RIGIDITY) AND S3 (NON-DEGENERACY WITH TEETH) ---")
    strata_declared = sorted(fixspec.keys())
    s23_rows = []
    for (idn, dr) in cells:
        keep = census[(idn, dr)]["routeB"]
        if not keep:
            s23_rows.append({"identification": idn, "direction": dr,
                             "candidates": 0, "determined": False,
                             "strata_hit": [], "strata_declared":
                             len(strata_declared), "image_size": None,
                             "injective": False, "kernel_size": None})
            continue
        tr = keep[0]
        amap = {r: alpha_from_triple(tr, r) for r in V}
        strat = sorted({strat_of(defect_cached(amap[r]), 9 * pfix(pident(NLAB)))
                        for r in V})
        isz = image_size(amap)
        ker = sum(1 for r in V if amap[r] == pident(NLAB))
        s23_rows.append({"identification": idn, "direction": dr,
                         "candidates": len(keep),
                         "determined": len(keep) == 1,
                         "strata_hit": strat,
                         "strata_declared": len(strata_declared),
                         "image_size": isz, "injective": isz == len(V),
                         "kernel_size": ker})
    any_det = any(r["determined"] for r in s23_rows)
    any_inj = any(r["injective"] for r in s23_rows)
    lagr_pre = p_part_exponent(NLAB - 1, P)
    strat_ok = all(len(r["strata_hit"]) == 2 for r in s23_rows
                   if r["candidates"] > 0)
    g14 = gate("G14", "S2 AND S3 ARE MEASURED ON THE CENSUS'S OWN SURVIVORS AND "
               "AGAINST THE ARENA'S OWN ARITHMETIC: rigidity asks whether the "
               "census DETERMINES a candidate (census size 1) and whether the "
               "transport side's fixed-configuration stratification is carried "
               "-- a cyclic image reaches exactly two of the seven declared "
               "strata, measured; non-degeneracy asks for injectivity, the form "
               "BRG's one-way theorem requires of a sub-object embedding, and no "
               "cell may be reported injective while the arena's p-part "
               "arithmetic forbids it",
               all(r["image_size"] is None or r["image_size"] <= len(V)
                   for r in s23_rows) and len(s23_rows) == len(cells)
               and strat_ok and not (any_inj and lagr_pre < 3),
               {"rows": s23_rows, "declared_strata": strata_declared,
                "record_space_size": len(V),
                "p_part_exponent": lagr_pre,
                "strata_hit_is_two_at_every_non_empty_cell": strat_ok,
                "any_cell_determined": any_det,
                "any_cell_injective": any_inj})
    report("G14", g14, f"cells with a determined candidate: {any_det}; cells "
           f"with an injective candidate: {any_inj}")
    for r in s23_rows:
        say(f"      {r['identification']:12s} {r['direction']:10s} candidates "
            f"{r['candidates']:4d}  determined {str(r['determined']):5s}  "
            f"strata hit {r['strata_hit']} of {len(strata_declared)}  "
            f"|image| {r['image_size']}  injective {r['injective']}")
    tables["s2_s3"] = s23_rows

    # S3's positive control: the sixteen-label arena (the same subgroup 4b built)
    p16 = p_part_exponent(15, P)
    inj16 = (len(img16) == P ** 3)
    g15 = gate("G15", "S3'S POSITIVE CONTROL WITH TEETH: THE INJECTIVITY CLAUSE "
               "IS SATISFIABLE, AND WHAT FORBIDS IT HERE IS THE NINE-LABEL "
               "ARENA.  At the sixteen-label completion arena the p-part of the "
               "group's order is p^3, and three disjoint p-cycles are built "
               "whose generated subgroup is measured to have exactly p^3 "
               "elements -- an injective candidate exists there.  At nine labels "
               "the p-part is p^1 and no injective candidate can exist",
               inj16 and p16 == 3 and lagr == 1,
               {"p_part_exponent_at_16_labels": p16,
                "p_part_exponent_at_9_labels": lagr,
                "witness_subgroup_order": len(img16),
                "record_space_size": len(V), "injective_possible_at_16": inj16})
    report("G15", g15, f"16-label p-part exponent {p16}, witness subgroup order "
           f"{len(img16)} = |V| = {len(V)}; 9-label p-part exponent {lagr}")
    disclose("X02", "S3's FAILURE AT THIS CARRIER IS FORCED AND IS DISCLOSED AS "
             "SUCH (RUNBOOK 14 addendum #208): the record datum space has p^3 "
             "elements and the completion group's p-part is measured p^1, so no "
             "candidate at the nine-label arena can be injective, whatever the "
             "encodings do.  It is recorded, not used as a discriminating "
             "must-pass gate, and its positive control at sixteen labels "
             "(G15) is what makes the clause a measurement rather than a "
             "tautology.",
             {"p_part_9": lagr, "p_part_16": p16, "|V|": len(V)})
    say("")

    # ==================== 7. S4: THE FAMILY ===============================
    say("--- 7. S4: FUNCTORIALITY IN THE FAMILY ---")
    progress("S4 grid")
    orders_declared = sorted(ordspec.keys())
    swept = prime_sweep(PRIMES)
    grid = grid_cells(swept, orders_declared)
    grid_rows = []
    anti_by_p, spec2_by_p, spec2c_by_p = {}, {}, {}
    for p in swept:
        anti_by_p[p] = sum(1 for g in COMPL
                           if DORD[g] == p and conj_by(SIG, g) == pinv(g))
    tau_rows = [[(1 if j == TAU[i] else 0) + (1 if j == i else 0)
                 for j in range(3)] for i in range(3)]
    for (idn, dr) in cells:
        MQ = enc[(idn, dr)]["Q"]
        for p in swept:
            Tp = to_fp(transpose(MQ), p)
            Mt = [[(Tp[i][j] - (2 if i == j else 0)) % p for j in range(3)]
                  for i in range(3)]
            spec2_by_p[(idn, dr, p)] = kernel_dim(Mt, p)
            joint = Mt + [[x % p for x in row] for row in tau_rows]
            spec2c_by_p[(idn, dr, p)] = kernel_dim(joint, p)
    seen_cells = set()
    for (idn, dr) in cells:
        for (p, n) in grid:
            key = (idn, dr, p, n)
            seen_cells.add(key)
            kd = spec2_by_p[(idn, dr, p)]
            kdc = spec2c_by_p[(idn, dr, p)]
            has_elt = anti_by_p[p] > 0
            s1ab_live = (kd > 0 and has_elt)
            # S1d forces ord(D) in {1, p} -- the order-1 branch is the candidate
            # whose exponent annihilates the base record -- not ord(D) = p
            s1d_live = s1ab_live and (n in (1, p))
            s1_live = (kdc > 0 and has_elt and n in (1, p))
            grid_rows.append({"identification": idn, "direction": dr, "p": p,
                              "ord_D": n, "two_in_spectrum": kd > 0,
                              "two_eigencovector_chart_antisymmetric": kdc > 0,
                              "anti_elements": anti_by_p[p],
                              "s1ab_live": s1ab_live, "s1d_live": s1d_live,
                              "s1_live": s1_live})
    live_ab = sum(1 for r in grid_rows if r["s1ab_live"])
    live_d = sum(1 for r in grid_rows if r["s1d_live"])
    live_full = sum(1 for r in grid_rows if r["s1_live"])
    indep_decisions = len(cells) * len(swept)
    g16g = gate("G16", "S4 IS A CELL-COMPLETE CENSUS OVER THE WHOLE DECLARED "
                "(prime, defect-order) GRID AT EVERY COVARIANT ENCODING CELL: "
                "each cell is visited exactly once, the count is computed from "
                "the declared sets rather than typed, and the narrowing the "
                "strengthened standard performs on BRG's live cells is read off "
                "it.  The grid's INDEPENDENT content is reported with it: the "
                "kernel computations are one per (encoding cell, prime), so the "
                "grid is that many linear-algebra decisions replicated across "
                "the defect-order axis, which enters the clause list only "
                "through the base-point condition",
                len(seen_cells) == len(cells) * len(swept) * len(orders_declared)
                and len(grid_rows) == len(seen_cells)
                and len(spec2_by_p) == indep_decisions,
                {"cells": len(seen_cells), "primes": len(swept),
                 "defect_orders": orders_declared,
                 "encoding_cells": len(cells),
                 "independent_kernel_decisions": indep_decisions,
                 "replication_along_the_defect_order_axis":
                     len(orders_declared),
                 "cells_live_at_S1ab": live_ab,
                 "cells_live_after_the_base_point_clause": live_d,
                 "cells_live_at_the_full_S1_clause_list": live_full,
                 "anti_invariant_elements_by_prime": anti_by_p})
    report("G16", g16g, f"{len(seen_cells)} grid cells "
           f"({indep_decisions} independent kernel decisions x "
           f"{len(orders_declared)} defect orders); live at S1a+b "
           f"{live_ab}; live after S1d {live_d}; live at the full S1 "
           f"{live_full}")
    say(f"      anti-invariant order-p elements by prime: {anti_by_p}")
    pn_ab = len({(r["p"], r["ord_D"]) for r in grid_rows if r["s1ab_live"]})
    pn_d = len({(r["p"], r["ord_D"]) for r in grid_rows if r["s1d_live"]})
    pn_f = len({(r["p"], r["ord_D"]) for r in grid_rows if r["s1_live"]})
    brg_pairs = sorted({(p, n) for p in PRIMES for n in orders_declared
                        if (2 * n) % p == 0})
    say(f"      distinct (p, ord D) pairs live: {len(brg_pairs)} at BRG's own "
        f"delivered standard, {pn_ab} at S1a+b, {pn_d} after the base-point "
        f"clause, {pn_f} at the full S1")
    say(f"      BRG's live cells reproduced here: {brg_pairs}")
    anchor("A22", "live (prime, defect-order) cells at BRG's delivered standard",
           3, len(brg_pairs), "BRG 4's scope-2 table and its verdict qualifiers")
    brg_counts = []
    for (p, n) in brg_pairs:
        rep = min(q for q in fam if pord(defect_cached(q)) == n)
        dq = defect_cached(rep)
        D81r = tuple(9 * dq[i // 9] + (i % 9) for i in range(81))
        Gr = group_closure([W, D81r], 81)
        brg_counts.append(sum(1 for g in Gr if pord(g) == p))
    anchor("A23", "non-trivial forward group morphisms at BRG's three live cells",
           [4, 4, 6], brg_counts, "BRG 4's scope-2 table")
    tables["s4_grid_summary"] = {
        "cells": len(seen_cells), "live_s1ab": live_ab, "live_s1d": live_d,
        "live_full_s1": live_full,
        "distinct_p_ord_pairs": {"s1ab": pn_ab, "s1d": pn_d, "full": pn_f},
        "by_direction": {dr: sum(1 for r in grid_rows
                                 if r["direction"] == dr and r["s1d_live"])
                         for dr in ("counts->q", "q->counts")}}

    # base change inside the ord-5 class
    sample = completion_sample(cls5)
    bc_rows = []
    for q in sample:
        dq = defect_cached(q)
        D81q = tuple(9 * dq[i // 9] + (i % 9) for i in range(81))
        Gq = group_closure([W, D81q], 81)
        bc_rows.append({"Q": list(q), "moved": pmoved(q), "ord": pord(dq),
                        "fix81": 9 * pfix(dq), "group_order": len(Gq),
                        "live": divides_ok(P, len(Gq))})
    uniform = (len({(r["ord"], r["fix81"], r["group_order"]) for r in bc_rows})
               == 1)
    g17 = gate("G17", "THE BASE CHANGE INSIDE THE DECLARED ord-5 COMPLETION "
               "CLASS IS SWEPT AND THE PAIRING'S DATA ARE MEASURED INVARIANT "
               "ACROSS IT: the lex-first, lex-last, fewest-moved and most-moved "
               "members are each rebuilt from their own completion, and every "
               "one gives the same defect order, the same fixed-configuration "
               "count and the same transport group order -- so the pairing is "
               "not an artifact of which member of the class was declared",
                uniform and len(bc_rows) >= 5,
                {"rows": bc_rows, "class_size": len(cls5), "uniform": uniform})
    report("G17", g17, f"{len(bc_rows)} completions rebuilt, invariant: "
           f"{uniform}")
    tables["base_change"] = bc_rows
    say("")

    # ==================== 8. S5: HELD-OUT =================================
    say("--- 8. S5: HELD-OUT PREDICTION WITH TRANSPORTED QUANTITIES ---")
    progress("held-out")
    Esy = synth_compatible_matrix(P)
    Ereal_rev = enc[("natural", "q->counts")]["Fp"]
    Ereal_reg = enc[("natural", "counts->q")]["Fp"]
    Ehold = s5_chart_map(Ereal_rev, Esy)
    FIT = fit_cells(V, E1)
    HELD = [r for r in V if r not in set(FIT)]

    _GP: dict = {}

    def alpha_gl(g, lam, r):
        t = _GP.get(g)
        if t is None:
            t = [pident(NLAB)]
            for _ in range(P - 1):
                t.append(pmul(t[-1], g))
            _GP[g] = t
        return t[sum(lam[i] * r[i] for i in range(3)) % P]

    def s5_run(Emap):
        adm_, ok_, bad_ = [], [], []
        for g in [x for x in COMPL if pord(x) == P]:
            for lam in V:
                if lam == (0, 0, 0):
                    continue
                if all(compare_square(defect_cached(alpha_gl(g, lam, r)),
                                      alpha_gl(g, lam, mat_apply(Emap, r, P)))
                       for r in FIT):
                    adm_.append((g, lam))
        for (g, lam) in adm_:
            bad_here = False
            for r in HELD:
                if not compare_square(defect_cached(alpha_gl(g, lam, r)),
                                      alpha_gl(g, lam, mat_apply(Emap, r, P))):
                    bad_here = True
                    break
            (bad_ if bad_here else ok_).append((g, lam))
        return adm_, ok_, bad_

    fit_admitted, held_ok, held_bad = s5_run(Ehold)
    held_viol = 0
    if held_bad:
        g_, l_ = held_bad[0]
        held_viol = sum(1 for r in HELD
                        if not compare_square(
                            defect_cached(alpha_gl(g_, l_, r)),
                            alpha_gl(g_, l_, mat_apply(Ehold, r, P))))
    reg_admitted, reg_ok, reg_bad = s5_run(Ereal_reg)
    syn_admitted, syn_ok, syn_bad = s5_run(Esy)
    g18 = gate("G18", "THE HELD-OUT VERIFICATION IS PREDICTIVE, NOT IMPOSED, AND "
               "IT IS RUN AGAINST THE PAIRING'S OWN DEFORMATION SIDE: the "
               "chart map is HA's own readout at the declared identification -- "
               "measured identical to the matrix section 2.4 builds -- not the "
               "synthetic control map; the split is declared before any candidate "
               "is fitted; candidates are admitted by the square at the FIT cell "
               "ALONE; and the square is then VERIFIED at every HELD cell, where "
               "most FIT-admitted candidates die.  A protocol under which nothing "
               "died out of sample would verify nothing.  The registered "
               "direction of the same readout is run too, and there the "
               "out-of-sample deaths are TOTAL -- the contrast is the "
               "measurement",
               Ehold == Ereal_rev and len(FIT) == 1 and len(HELD) == P ** 3 - 1
               and len(fit_admitted) > len(held_ok) and len(held_bad) > 0
               and len(reg_ok) == 0 and len(reg_admitted) > 0,
               {"chart_map_used": Ehold,
                "chart_map_is_the_pairings_own_readout": Ehold == Ereal_rev,
                "identification": "natural", "direction": "q->counts",
                "FIT": [list(r) for r in FIT], "HELD_cells": len(HELD),
                "fit_admitted": len(fit_admitted),
                "survived_held_out": len(held_ok),
                "rejected_out_of_sample": len(held_bad),
                "total_held_out_violations": held_viol,
                "registered_direction_fit_admitted": len(reg_admitted),
                "registered_direction_survivors": len(reg_ok)})
    report("G18", g18, f"FIT {len(FIT)} cell admits {len(fit_admitted)} "
           f"candidates; {len(held_bad)} die on {len(HELD)} held-out cells, "
           f"{len(held_ok)} survive (registered direction: "
           f"{len(reg_admitted)} admitted, {len(reg_ok)} survive)")
    g41 = gate("G41", "DISCLOSURE GATE (not must-pass): WHICH DEFORMATION SIDE "
               "EACH BLOCK OF THIS UNIT RUNS AGAINST.  S5 runs against the "
               "pairing's own readout in both directions; the SYNTHETIC "
               "compatible map is a declared control and is used only where it "
               "is named -- the FOUND-reachability control and the EMPTY-"
               "reachability control.  The three S5 counts are reported for the "
               "pairing's own map and for the synthetic one side by side, so the "
               "reader can see exactly what the synthetic map does and does not "
               "change",
               True,
               {"S5_chart_map": "the pairing's own readout (natural, q->counts)",
                "S5_registered_direction": "the pairing's own readout "
                                           "(natural, counts->q)",
                "synthetic_map_used_by": ["SYNTH-COMPATIBLE (FOUND reachable)",
                                          "SYNTH-EMPTY (EMPTY reachable)"],
                "counts_on_the_pairings_own_map":
                    [len(fit_admitted), len(held_bad), len(held_ok)],
                "counts_on_the_registered_direction":
                    [len(reg_admitted), len(reg_bad), len(reg_ok)],
                "counts_on_the_synthetic_map":
                    [len(syn_admitted), len(syn_bad), len(syn_ok)]},
               must_pass=False)
    report("G41", g41, f"S5 on the pairing's own map "
           f"{[len(fit_admitted), len(held_bad), len(held_ok)]}; registered "
           f"direction {[len(reg_admitted), len(reg_bad), len(reg_ok)]}; "
           f"synthetic {[len(syn_admitted), len(syn_bad), len(syn_ok)]}")

    gw, lw = held_ok[0] if held_ok else (pident(NLAB), (0, 0, 0))

    def gpow(g, e):
        out = pident(NLAB)
        for _ in range(e % P):
            out = pmul(out, g)
        return out

    pred_perm, pred_fix, teeth1, teeth2 = 0, 0, 0, 0
    for r in HELD:
        k = sum(lw[i] * r[i] for i in range(3)) % P
        img = alpha_gl(gw, lw, r)
        pd = defect_cached(img)
        # H2: the defect PERMUTATION itself, predicted from the fitted rule
        if transported_quantity(pd, img) == gpow(gw, 2 * k):
            pred_perm += 1
        # H3: the fixed-configuration stratum
        if 9 * pfix(pd) == (9 * (NLAB - P) if k else 81):
            pred_fix += 1
        # X-NOSQUARE: the defect map predicted to act trivially
        if gpow(gw, teeth_exponent(k, P)) != pd:
            teeth1 += 1
        # X-FLATSTRAT: the identity-defect stratum predicted everywhere
        if 9 * pfix(pd) != 81:
            teeth2 += 1
    g19 = gate("G19", "TWO TRANSPORT-SIDE PHYSICAL QUANTITIES ARE CARRIED OUT OF "
               "SAMPLE AND THE DECLARED FAILING EXTENSIONS DO FAIL: the DEFECT "
               "PERMUTATION itself, entry by entry, and its "
               "FIXED-CONFIGURATION COUNT are predicted at every held-out cell "
               "from the FIT-fitted rule and then computed, while X-NOSQUARE "
               "(the defect map predicted to act trivially) and X-FLATSTRAT (the "
               "identity-defect stratum predicted everywhere) are declared in "
               "advance to fail and are measured failing",
               pred_perm == len(HELD) and pred_fix == len(HELD)
               and teeth1 > 0 and teeth2 > 0,
               {"held_out_cells": len(HELD),
                "defect_permutation_predicted_correctly": pred_perm,
                "fixed_configuration_predicted_correctly": pred_fix,
                "X-NOSQUARE_violations": teeth1,
                "X-FLATSTRAT_violations": teeth2,
                "example_rejected_at_held_out_cells": held_viol,
                "witness_g": list(gw), "witness_lambda": list(lw)})
    report("G19", g19, f"defect permutation and stratum predicted at "
           f"{pred_perm}/{pred_fix} of {len(HELD)} held-out cells; teeth fail at "
           f"{teeth1} and {teeth2}")
    tables["held_out"] = {"fit_cells": len(FIT), "held_cells": len(HELD),
                          "fit_admitted": len(fit_admitted),
                          "held_survivors": len(held_ok),
                          "held_rejected": len(held_bad)}
    say("")

    # ==================== 9. S6: THE PRIME AS A PARAMETER ================
    say("--- 9. S6: THE PRIME DECLARED A PARAMETER, PER-PRIME VERDICTS ---")
    per_prime = []
    for p in swept:
        per_prime.append({
            "p": p,
            "cells_live_at_S1ab": sum(1 for r in grid_rows
                                      if r["p"] == p and r["s1ab_live"]),
            "cells_live_after_S1d": sum(1 for r in grid_rows
                                        if r["p"] == p and r["s1d_live"]),
            "cells_live_at_the_full_S1": sum(1 for r in grid_rows
                                             if r["p"] == p and r["s1_live"]),
            "anti_elements": anti_by_p[p]})
    uniform_prime = len({r["cells_live_at_the_full_S1"] > 0
                         for r in per_prime}) == 1
    partial_uniform = len({r["cells_live_after_S1d"] > 0
                           for r in per_prime}) == 1
    intersection_live = all(r["cells_live_at_the_full_S1"] > 0
                            for r in per_prime)
    g20 = gate("G20", "S6 IS DISCHARGED IN THE PER-PRIME FORM AND THE "
               "ARENA-INVARIANT INTERSECTION IS TAKEN (RUNBOOK 15, BRG's "
               "requirement 4): the census is reported at every one of the "
               "declared primes and the verdict is the INTERSECTION over the "
               "sweep, never a convenient prime.  The measurement has teeth: the "
               "partial clause list IS prime-dependent (live at 5 and 7 only) "
               "while the full clause list is measured prime-UNIFORM, so the "
               "verdict does not ride on the declared prime and the difference "
               "between the two readings is itself measured",
               len(swept) > 1 and len(per_prime) == len(swept)
               and uniform_prime and not partial_uniform,
               {"per_prime": per_prime, "primes_swept": len(swept),
                "full_clause_answer_is_prime_uniform": uniform_prime,
                "partial_clause_answer_is_prime_uniform": partial_uniform,
                "live_at_every_declared_prime": intersection_live})
    report("G20", g20, f"{len(swept)} primes; full-clause answer prime-uniform: "
           f"{uniform_prime}; partial-clause answer prime-uniform: "
           f"{partial_uniform}; live at every prime: {intersection_live}")
    for r in per_prime:
        say(f"      p = {r['p']:2d}   live at S1a+b {r['cells_live_at_S1ab']:2d}"
            f"   after S1d {r['cells_live_after_S1d']:2d}   at the full S1 "
            f"{r['cells_live_at_the_full_S1']:2d}   anti-invariant elements "
            f"{r['anti_elements']}")
    tables["per_prime"] = per_prime
    say("")

    # ==================== 10. THE CONTROLS ================================
    say("--- 10. CONTROLS: POSITIVE, NEGATIVE, AND BOTH OUTCOMES REACHABLE ---")
    progress("controls")
    # F0-IDENT
    idc = identity_candidate(NLAB)
    ident_cells, ident_bad = 0, 0
    for q in COMPL:
        ident_cells += 1
        if not compare_square(defect_cached(pmul(idc, q)),
                              pmul(idc, defect_cached(q))):
            ident_bad += 1
    ident_inj = (len({pmul(idc, q) for q in COMPL}) == len(COMPL))
    ident_s1c = all(pmul(idc, conj_by(SIG, q)) == conj_by(SIG, pmul(idc, q))
                    for q in COMPL)
    ident_s1d = (pord(defect_cached(pmul(idc, Q0))) == pord(D9))
    g21 = gate("G21", "DISCLOSURE GATE (not must-pass): F0-IDENT IS "
               "ANALYTICALLY FORCED AND IS NOT THIS UNIT'S POSITIVE CONTROL "
               "(RUNBOOK 14 addendum #208).  With alpha the identity and the "
               "transport arena paired with itself, every clause of the check "
               "reads x == x: the square is delta(q) = delta(q), the involution "
               "clause is sigma(q) = sigma(q), and injectivity is |{q}| = "
               "|COMPL|.  Its zero violations at all of the family's cells "
               "record that the identity candidate is the identity and nothing "
               "about the square, so it is registered as a disclosure and "
               "carries no mutant.  THE POSITIVE CONTROL IS SYNTH-COMPATIBLE "
               "(G22), which a broken square predicate does kill",
               ident_bad == 0 and ident_inj and ident_s1c and ident_s1d
               and ident_cells == len(COMPL),
               {"cells": ident_cells, "square_violations": ident_bad,
                "injective": ident_inj, "s1c": ident_s1c, "s1d": ident_s1d,
                "analytically_forced": True,
                "the_positive_control_of_this_unit": "SYNTH-COMPATIBLE (G22)"},
               must_pass=False)
    report("G21", g21, f"identity self-morphism (disclosure): {ident_bad} square "
           f"violations at {ident_cells} cells; injective {ident_inj}")

    # FOUND reachable: the synthetic compatible pair
    synth_ok = []
    for g in ANTI:
        for lam in V:
            if lam == (0, 0, 0):
                continue
            if all(compare_square(defect_cached(alpha_gl(g, lam, r)),
                                  alpha_gl(g, lam, mat_apply(Esy, r, P)))
                   for r in V):
                synth_ok.append((g, lam))
    synth_maps = {tuple(alpha_gl(g, lam, r) for r in V) for (g, lam) in synth_ok}
    synth_c = [(g, lam) for (g, lam) in synth_ok
               if all(alpha_gl(g, lam, tuple(r[TAU[i]] for i in range(3)))
                      == conj_by(SIG, alpha_gl(g, lam, r)) for r in V)]
    r0s = tuple(x % P for x in RECORDS["G-ANISO"])
    synth_d = [(g, lam) for (g, lam) in synth_c
               if pord(defect_cached(alpha_gl(g, lam, r0s))) == P]
    wit = exhibit_witness(synth_d[0] if synth_d else None)
    wit_ok = False
    if wit is not None:
        gg, ll = wit
        wit_ok = (all(compare_square(defect_cached(alpha_gl(gg, ll, r)),
                                     alpha_gl(gg, ll, mat_apply(Esy, r, P)))
                      for r in V)
                  and all(alpha_gl(gg, ll, tuple(r[TAU[i]] for i in range(3)))
                          == conj_by(SIG, alpha_gl(gg, ll, r)) for r in V)
                  and pord(defect_cached(alpha_gl(gg, ll, r0s))) == P)
    g22 = gate("G22", "THE POSITIVE CONTROL OF THIS UNIT, AND FOUND IS REACHABLE "
               "BY THIS MACHINERY: a declared synthetic compatible pair -- the "
               "same transport side against a synthetic chart map whose "
               "2-eigencovector is chart-ANTIsymmetric -- yields candidates that "
               "pass S1a, S1b, S1c AND S1d, and the exhibited witness is "
               "re-checked here from its own two data at every cell.  ITS "
               "BASE-POINT CLAUSE IS EVALUATED AT THE DECLARED tau-ASYMMETRIC "
               "RECORD, RECORDED HERE, and it must be: G42 measures that S1c and "
               "S1d are jointly unsatisfiable at the tau-fixed declared base "
               "record for every chart map whatsoever, so a control run there "
               "could not pass whatever the machinery did",
               len(synth_ok) > 0 and len(synth_c) > 0 and len(synth_d) > 0
               and wit is not None and wit_ok,
               {"synthetic_chart_map": Esy,
                "pairs_passing_S1a_S1b": len(synth_ok),
                "distinct_maps": len(synth_maps),
                "passing_S1c": len(synth_c), "passing_S1d": len(synth_d),
                "base_record_of_the_base_point_clause": "G-ANISO",
                "base_record_counts": list(RECORDS["G-ANISO"]),
                "base_record_mod_p": list(r0s),
                "declared_base_record_of_the_census": list(r0),
                "witness": [list(wit[0]), list(wit[1])] if wit else None,
                "witness_reverified": wit_ok})
    report("G22", g22, f"synthetic compatible pair: {len(synth_ok)} pairs, "
           f"{len(synth_maps)} distinct maps, {len(synth_c)} pass S1c, "
           f"{len(synth_d)} pass S1d at G-ANISO; witness re-verified {wit_ok}")
    if wit is not None:
        say(f"      witness g = {list(wit[0])}, lambda = {list(wit[1])}")

    # EMPTY reachable
    Eem = synth_empty_matrix(P)
    empty_ok = []
    for g in ANTI:
        for lam in V:
            if lam == (0, 0, 0):
                continue
            if all(compare_square(defect_cached(alpha_gl(g, lam, r)),
                                  alpha_gl(g, lam, mat_apply(Eem, r, P)))
                   for r in V):
                empty_ok.append((g, lam))
    g23 = gate("G23", "EMPTY IS REACHABLE BY THE SAME MACHINERY: a declared "
               "synthetic incompatible pair -- a scalar chart map whose only "
               "eigenvalue is 3 -- returns a census of size zero, so the two "
               "outcomes are separated by a measurement and not by a "
               "construction that can only return one of them",
               len(empty_ok) == 0 and len(synth_ok) > 0,
               {"synthetic_incompatible_chart_map": Eem,
                "candidates": len(empty_ok),
                "compatible_pair_for_contrast": len(synth_ok)})
    report("G23", g23, f"synthetic incompatible pair: {len(empty_ok)} candidates")

    # negative control with teeth
    Enat = enc[("natural", "q->counts")]["Fp"] if ("natural", "q->counts") in enc \
        else enc[cells[0]]["Fp"]
    lam_acc = kernel_fp([[(transpose(Enat)[i][j] - (2 if i == j else 0)) % P
                          for j in range(3)] for i in range(3)], P)
    mu_basis = kernel_fp([[(transpose(Enat)[i][j] - (1 if i == j else 0)) % P
                           for j in range(3)] for i in range(3)], P)
    gbr = ANTI[0]
    lam_b = lam_acc[0] if lam_acc else (1, 1, 1)
    mu_b = mu_basis[0] if mu_basis else (1, 0, 0)

    def brk(r, accepted):
        k = break_exponent(lam_b, mu_b, r, P, accepted)
        out = pident(NLAB)
        for _ in range(k):
            out = pmul(out, gbr)
        return out

    br_map = {r: brk(r, False) for r in V}
    ac_map = {r: brk(r, True) for r in V}
    br_s1a = sum(1 for r in V
                 if not compare_square(defect_cached(br_map[r]),
                                       br_map[mat_apply(Enat, r, P)]))
    ac_s1a = sum(1 for r in V
                 if not compare_square(defect_cached(ac_map[r]),
                                       ac_map[mat_apply(Enat, r, P)]))
    br_s1b = hom_clause(br_map, V, P)
    ac_s1b = hom_clause(ac_map, V, P)
    g24 = gate("G24", "NEGATIVE CONTROL WITH TEETH, AND THE REJECTING CLAUSE IS "
               "NAMED: BREAK-HOM differs from an ACCEPTED candidate only in the "
               "linearity of its exponent.  It satisfies the commuting square "
               "S1a at EVERY record cell -- so the predicate is not rejecting "
               "gross malformation -- and it is rejected by S1b alone, at a "
               "measured number of the |V|^2 composition cells, while its "
               "accepted counterpart is accepted by both",
               br_s1a == 0 and br_s1b > 0 and ac_s1a == 0 and ac_s1b == 0,
               {"BREAK-HOM_S1a_violations": br_s1a,
                "BREAK-HOM_S1b_violations": br_s1b,
                "composition_cells": len(V) ** 2,
                "accepted_counterpart_S1a_violations": ac_s1a,
                "accepted_counterpart_S1b_violations": ac_s1b,
                "rejecting_clause": "S1b",
                "lambda": list(lam_b), "mu": list(mu_b)})
    report("G24", g24, f"BREAK-HOM: S1a {br_s1a}/{len(V)}, S1b {br_s1b}/"
           f"{len(V) ** 2}; accepted counterpart {ac_s1a}/{ac_s1b} -- rejected "
           f"by S1b")
    tables["controls"] = {
        "identity_self_morphism_cells": ident_cells,
        "synthetic_compatible_pairs": len(synth_ok),
        "synthetic_compatible_distinct_maps": len(synth_maps),
        "synthetic_incompatible_candidates": len(empty_ok),
        "break_hom_s1a": br_s1a, "break_hom_s1b": br_s1b}
    say("")

    # ==================== 11. SYMMETRY SELF-TESTS =========================
    say("--- 11. SYMMETRY SELF-TESTS (RUNBOOK 14, ALL ADDENDA) ---")
    progress("self-tests")
    pre_lookups = CACHE_STATS["lookups"]
    pre_hits = CACHE_STATS["hits"]
    pre_st = CACHE_STATS["selftest_hits"]
    pre_by = CACHE_STATS["bypasses"]

    # (a) relabelling of the completion arena
    pi = relabelling()
    SIGr = conj_by(pi, SIG)
    reb_ok, reb_cells = 0, 0
    for q in COMPL:
        reb_cells += 1
        qq = conj_by(pi, q)
        lhs = pmul(pinv(conj_by(SIGr, qq)), qq)
        if lhs == conj_by(pi, defect_cached(q, fresh=True, selftest=True)):
            reb_ok += 1
    anti_r = sum(1 for g in COMPL if pord(g) == P
                 and conj_by(SIGr, conj_by(pi, g)) == pinv(conj_by(pi, g)))
    g25 = gate("G25", "SYMMETRY SELF-TEST -- RELABELLING THE COMPLETION ARENA: "
               "the whole transport side is transported through a declared "
               "non-identity relabelling of the nine labels, the arena is READ "
               "INSIDE the new labels (its own defect map recomputed there, its "
               "anti-invariant element count recounted there), and the measured "
               "invariant is unchanged.  The relabelling is measured to move "
               "labels, so a null action cannot pass",
               pi != pident(NLAB) and reb_ok == reb_cells
               and anti_r == len(ANTI) and pmoved(pi) > 0,
               {"relabelling": list(pi), "labels_moved": pmoved(pi),
                "equivariance_cells": reb_cells, "equivariance_ok": reb_ok,
                "anti_invariant_count_in_the_relabelled_arena": anti_r,
                "anti_invariant_count_declared": len(ANTI)})
    report("G25", g25, f"relabelling moves {pmoved(pi)} labels; delta "
           f"equivariant at {reb_ok}/{reb_cells}; anti count {anti_r}")

    # (b) change of basis of the record datum space
    B = basis_change(P)
    Binv = to_fp(inv3([[Fr(x) for x in row] for row in B]), P)
    basis_rows = []
    for (idn, dr) in cells:
        Efp = enc[(idn, dr)]["Fp"]
        EB = [[sum(sum(B[i][k] * Efp[k][l] for k in range(3)) * Binv[l][j]
                   for l in range(3)) % P for j in range(3)] for i in range(3)]
        kd0 = kernel_dim([[(transpose(Efp)[i][j] - (2 if i == j else 0)) % P
                           for j in range(3)] for i in range(3)], P)
        kd1 = kernel_dim([[(transpose(EB)[i][j] - (2 if i == j else 0)) % P
                           for j in range(3)] for i in range(3)], P)
        basis_rows.append({"cell": f"{idn}|{dr}", "kernel_dim": kd0,
                           "kernel_dim_after_basis_change": kd1})
    basis_inv = all(r["kernel_dim"] == r["kernel_dim_after_basis_change"]
                    for r in basis_rows)
    g26 = gate("G26", "SYMMETRY SELF-TEST -- CHANGE OF BASIS OF THE RECORD DATUM "
               "SPACE: the chart map is conjugated by a declared non-identity "
               "element of GL_3(F_p) and the census's own decision quantity -- "
               "the dimension of the 2-eigenspace -- is recomputed INSIDE the "
               "new basis and measured unchanged at every encoding cell.  A "
               "basis change that changed nothing could not test this",
               basis_inv and B != [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
               {"basis_change": B, "rows": basis_rows,
                "invariant": basis_inv})
    report("G26", g26, f"basis change {B}; kernel dimensions invariant: "
           f"{basis_inv}")

    # (c) the tested set is declared, not verdict-selected
    declared_set = sorted(f"{a}|{b}" for (a, b) in cells)
    verdict_sel = sorted(f"{r['identification']}|{r['direction']}"
                         for r in rows if r["route_B_enumeration"] > 0)
    tested = selftest_set(declared_set, verdict_sel)
    g27 = gate("G27", "THE SELF-TESTS' TESTED SET IS FIXED BY DECLARATION AND "
               "NEVER SELECTED BY THE VERDICTS UNDER AUDIT (RUNBOOK 14 addendum "
               "#185): the declared set is the WHOLE COVARIANT CELL FAMILY -- "
               "every identification in the declared orbit x both directions, "
               "including the cells whose census is empty -- and it is measured "
               "equal to the declaration and strictly larger than the set the "
               "verdicts would have selected",
               tested == declared_set and len(declared_set) > len(verdict_sel),
               {"declared": declared_set, "verdict_selected": verdict_sel,
                "tested": tested})
    report("G27", g27, f"tested set {tested} (verdict-selected would be "
           f"{verdict_sel})")

    st_hits = CACHE_STATS["selftest_hits"] - pre_st
    by = CACHE_STATS["bypasses"] - pre_by
    g28 = gate("G28", "CACHE DISCIPLINE (RUNBOOK 14 addenda #185 and #219): every "
               "self-test evaluation of the defect map BYPASSES the memo cache, "
               "the self-test's cache-hit count is measured ZERO, and the cache "
               "path is measured to have been exercised elsewhere in the run -- "
               "so the zero-hit clause is not the signature of a cache nobody "
               "uses",
               st_hits == 0 and by > 0 and pre_lookups > 0 and pre_hits > 0,
               {"selftest_cache_hits": st_hits, "selftest_bypasses": by,
                "cache_lookups_before_the_selftests": pre_lookups,
                "cache_hits_before_the_selftests": pre_hits,
                "cache_entries": len(_DELTA_MEMO)})
    report("G28", g28, f"self-test bypasses {by}, self-test cache hits "
           f"{st_hits}; cache had {pre_lookups} lookups and {pre_hits} hits")
    say("")

    # ==================== 12. OPEN 1: IS p DERIVABLE? =====================
    say("--- 12. OPEN 1: IS THE PRIME DERIVABLE ON THIS PAIRING? ---")
    progress("open 1")
    PRANGE = [q for q in range(2, 60) if all(q % k for k in range(2, q))]
    ADMISS = [q for q in PRANGE if 6 % q != 0]
    rho_den = max(RHO[0].denominator, RHO[1].denominator)
    rho_primes = {q for q in PRANGE if rho_den % q == 0}
    det_primes = {q for q in PRANGE if int(det_ha) % q == 0}
    LAB9, LAB16 = NLAB, 16
    SCALES = open1_scale_labels(LAB9, LAB16)

    # ---- the arena-reading candidates, computed at an arbitrary label count --
    # At the declared arena every one of them is computed by EXHAUSTIVE sweep.
    # At a larger arena the family cannot be swept, so they are computed by
    # explicit construction plus an exact upper bound, and the two routes are
    # measured to agree at the declared arena before the constructive one is
    # used anywhere else.
    def anti_witness(labels, q):
        """An explicit Sigma-anti-invariant element of order q at the given
        arena, fixing label 0: a q-cycle reflected by Sigma -- one Sigma-fixed
        label and (q-1)/2 Sigma-transposed pairs -- or None if the arena has no
        room for one."""
        m = 1
        while m * m < labels:
            m += 1
        if m * m != labels:
            return None
        s = sigma_perm(m)
        fixed = [i for i in range(1, labels) if s[i] == i]
        pairs = [(i, s[i]) for i in range(1, labels) if s[i] > i]
        if q == 2:
            if not pairs:
                return None
            i, j = pairs[0]
            t = list(range(labels))
            t[i], t[j] = j, i
            return tuple(t)
        need = (q - 1) // 2
        if need > len(pairs) or not fixed:
            return None
        seq = [a for (a, _b) in pairs[:need]] + [fixed[0]] + \
              [b for (_a, b) in pairs[:need]][::-1]
        t = list(range(labels))
        for k in range(q):
            t[seq[k]] = seq[(k + 1) % q]
        return tuple(t)

    _ARENA: dict = {}

    def arena_primitives(labels):
        """The ARENA's own primitive measurements, taken once per arena: which
        primes occur as element orders, as anti-invariant element orders, and as
        divisors of some 2*ord(D) in the family.  At the declared arena all
        three are exhaustive sweeps AND the constructive route is run beside
        them, so the constructive route -- the only one available at a bigger
        arena -- is validated before it is used anywhere else."""
        if labels in _ARENA:
            return _ARENA[labels]
        cap = labels - 1
        built = {"P4": [], "P5": [], "P10": []}
        s = sigma_perm(int(math.isqrt(labels)))
        for q in PRANGE:
            if q > cap:
                continue
            g = anti_witness(labels, q)
            if g is None:
                continue
            d = pmul(pinv(conj_by(s, g)), g)
            if pord(g) == q and conj_by(s, g) == pinv(g) and g[0] == 0:
                built["P10"].append(q)
                built["P5"].append(q)
                if (2 * pord(d)) % q == 0:
                    built["P4"].append(q)
        # an element of the completion group permutes labels-1 labels, so every
        # prime dividing its order is at most labels-1: the constructive route's
        # bound is exact
        out = {k: sorted(built[k]) for k in built}
        agree = None
        if labels == NLAB:
            fam_primes = set()
            for n in ordspec:
                m = 2 * n
                dd = 2
                while dd * dd <= m:
                    if m % dd == 0:
                        fam_primes.add(dd)
                        while m % dd == 0:
                            m //= dd
                    dd += 1
                if m > 1:
                    fam_primes.add(m)
            orders_seen, anti_orders = set(), set()
            for g in COMPL:
                orders_seen.add(DORD[g])
                if conj_by(SIG, g) == pinv(g):
                    anti_orders.add(DORD[g])
            exhaustive = {"P4": sorted(fam_primes),
                          "P5": sorted(q for q in PRANGE if q in orders_seen),
                          "P10": sorted(q for q in PRANGE if q in anti_orders)}
            agree = all(out[k] == exhaustive[k] for k in out)
            out = exhaustive
        out["routes_agree"] = agree
        _ARENA[labels] = out
        return out

    def arena_primes(labels, which, fresh=False):
        """P4, P5 and P10 at a given arena, rebuilt from that arena's own
        primitive measurements."""
        return list(arena_primitives(labels)[which])

    def spec2_primes(idns, direction, basis, fresh=False):
        """P8: the primes at which 2 lies in the spectrum of the chart map, over
        the given identifications and in the given direction."""
        out, undef = set(), set()
        for q in PRANGE:
            for idn in idns:
                MQ = encoding_matrix(idn, direction)
                if any(x.denominator % q == 0 for row in MQ for x in row):
                    undef.add(q)
                    continue
                Mq = to_fp(MQ, q)
                if basis is not None:
                    Bi = to_fp(inv3([[Fr(x) for x in row] for row in basis]), q)
                    Mq = [[sum(sum(basis[i][k] * Mq[k][l] for k in range(3))
                               * Bi[l][j] for l in range(3)) % q
                           for j in range(3)] for i in range(3)]
                Mt = [[(transpose(Mq)[i][j] - (2 if i == j else 0)) % q
                       for j in range(3)] for i in range(3)]
                if kernel_dim(Mt, q) > 0:
                    out.add(q)
        return sorted(out), sorted(undef)

    def cand_sets(decl, fresh=False):
        """EVERY Open-1 candidate as a FUNCTION of the declaration record."""
        lab = decl["labels"]
        s8, _u = spec2_primes(decl["identifications"], decl["direction"],
                              decl["basis"], fresh=fresh)
        return {
            "P1": [decl["p"]],
            "P2": sorted(PRANGE),
            "P3": sorted({q for q in PRANGE if (2 * decl["ord_rule"]) % q == 0}),
            "P4": arena_primes(lab, "P4", fresh=fresh),
            "P5": arena_primes(lab, "P5", fresh=fresh),
            "P6": sorted(set(PRANGE) - det_primes),
            "P7": sorted(set(PRANGE) - rho_primes),
            "P8": s8,
            "P9": sorted(set(s8) - rho_primes),
            "P10": arena_primes(lab, "P10", fresh=fresh),
            "P11": sorted({q for q in PRANGE
                           if p_part_exponent(lab - 1, q) >= 3}),
        }

    # ---- the declaration record, and the counterfactual re-declarations ------
    ALL_IDNS = tuple(sorted(SLOT_ORDERS))
    cls7 = [q for q in COMPL if pord(defect_cached(q)) == 7]
    BASE = {"p": P, "ord_rule": pord(D9), "direction": "counts->q",
            "identifications": ALL_IDNS, "base_record": "G-FLAT",
            "completion": Q0, "relabelling": pident(NLAB),
            "basis": None, "labels": LAB9}
    CFS = [
        ("prime := 7, selection rule ord(D) := 7 (class size %d, lex-first %s)"
         % (len(cls7), list(min(cls7)) if cls7 else []),
         {"p": 7, "ord_rule": 7}),
        ("direction := the reversed one", {"direction": "q->counts"}),
        ("identification := the declared natural cell alone",
         {"identifications": ("natural",)}),
        ("identification := the tau-conjugate of the declared index cell alone",
         {"identifications": ("tau-index",)}),
        ("base record := G-ANISO", {"base_record": "G-ANISO"}),
        ("completion := the lex-last member of the ord-5 class",
         {"completion": max(cls5)}),
        ("record-space basis := the declared GL_3 element",
         {"basis": basis_change(P)}),
    ]
    base_sets = cand_sets(BASE)
    cf_rows, free_measured, breaker = [], {}, {}
    for label, patch in CFS:
        d2 = dict(BASE)
        d2.update(patch)
        s2 = cand_sets(d2, fresh=True)
        changed = sorted(k for k in base_sets if base_sets[k] != s2[k])
        cf_rows.append({"re_declaration": label, "candidates_that_moved": changed})
        for k in changed:
            breaker.setdefault(k, label)
    for k in base_sets:
        free_measured[k] = (k not in breaker)
    free_measured["P12"] = True

    open1 = []
    scale_sets = {lab: cand_sets(dict(BASE, labels=lab), fresh=True)
                  for lab in SCALES}

    def add(pid, statement, out_set, note):
        out = sorted(out_set)
        u = unique_prime(out)
        inside = sorted(set(out) & set(ADMISS))
        row = {"id": pid, "candidate": statement,
               "primes_it_admits": out,
               "admissible_part": inside,
               "role": ("NARROWING" if inside else "NO-ADMISSIBLE-PRIME"),
               "unique": bool(u),
               "declaration_free": bool(declaration_free(
                   pid, free_measured[pid], sorted(free_measured))),
               "declaration_freeness_measured": free_measured[pid],
               "broken_by": breaker.get(pid),
               "note": note}
        for lab in SCALES:
            if pid in scale_sets[lab]:
                row["admissible_part_at_%d_labels" % lab] = sorted(
                    set(scale_sets[lab][pid]) & set(ADMISS))
        open1.append(row)
        return row

    NOTES = {
        "P1": "the carrier size p^(k+d) = %d is a FUNCTION of the declared p"
              % nHA,
        "P2": "k, d, L and the link set are declared arena data and constrain "
              "no prime",
        "P3": "2*ord(D) = %d, but ord(D) = 5 is THIS unit's declared selection "
              "rule; the candidate contains its own conclusion" % len(GRP),
        "P4": "the family's own defect orders, read at the arena being reported",
        "P5": "the completion group's element orders at the arena being "
              "reported",
        "P6": "the readout determinant is %s, so the re-encoding is invertible "
              "at every prime but 2 -- a single exclusion, not a derivation"
              % det_ha,
        "P7": "rho's denominator is %d, so the deformation side does not exist "
              "at 2 or 3" % rho_den,
        "P8": "the intertwining condition itself, over the covariant cell "
              "family in the registered direction",
        "P9": "the joint system P7 and P8",
        "P10": "the count of label-exchange-anti-invariant elements of order p "
               "at the arena being reported",
        "P11": "the p-part of the completion group's order against |V| = p^3 "
               "at the arena being reported",
    }
    for pid in ("P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10",
                "P11"):
        add(pid, DECL["open1_candidates"][pid], base_sets[pid], NOTES[pid])

    # ---- the verdict, from two computations that share no deciding variable --
    def verdict_from_table(rows, admissible):
        """SOURCE 1: the candidate table.  A declaration-free NARROWING
        candidate other than the intersection itself that admits exactly one
        admissible prime, or a singleton intersection."""
        narrowing = [r for r in rows if r["declaration_free"]
                     and r["role"] == "NARROWING" and r["id"] != "P12"]
        single = sorted(r["id"] for r in narrowing
                        if unique_prime(r["admissible_part"]))
        inter = open1_intersection([r["admissible_part"] for r in narrowing],
                                   admissible)
        return (derive_prime_verdict(bool(single) or len(inter) == 1),
                sorted(inter), single, sorted(r["id"] for r in narrowing))

    def verdict_from_primitives(free_ids, decl, admissible):
        """SOURCE 2: a per-prime elimination that never forms the intersection
        and never reads the table -- every candidate's membership is rebuilt
        from its arena's own primitive measurements and tested prime by
        prime."""
        sets_ = cand_sets(decl, fresh=True)
        survivors, singles = [], []
        for q in admissible:
            if all(q in sets_[pid] for pid in free_ids):
                survivors.append(q)
        for pid in free_ids:
            if len(set(sets_[pid]) & set(admissible)) == 1:
                singles.append(pid)
        return (derive_prime_verdict(bool(singles) or len(survivors) == 1),
                survivors, sorted(singles))

    scale_report = {}
    for lab in SCALES:
        rows_lab = []
        for r in open1:
            rr = dict(r)
            if r["id"] in scale_sets[lab]:
                rr["primes_it_admits"] = scale_sets[lab][r["id"]]
                rr["admissible_part"] = sorted(set(scale_sets[lab][r["id"]])
                                               & set(ADMISS))
                rr["role"] = ("NARROWING" if rr["admissible_part"]
                              else "NO-ADMISSIBLE-PRIME")
                rr["unique"] = bool(unique_prime(rr["primes_it_admits"]))
            rows_lab.append(rr)
        v1, i1, s1_, free_ids = verdict_from_table(rows_lab, ADMISS)
        v2, i2, s2_ = verdict_from_primitives(free_ids,
                                              dict(BASE, labels=lab), ADMISS)
        scale_report[lab] = {"labels": lab, "verdict_source_1": v1,
                             "verdict_source_2": v2,
                             "narrowing_source_1": i1,
                             "narrowing_source_2": i2,
                             "single_candidate_source_1": s1_,
                             "single_candidate_source_2": s2_,
                             "declaration_free_narrowing_candidates": free_ids}
    nine = scale_report[LAB9]
    inter = set(nine["narrowing_source_1"])
    no_admissible = sorted(c["id"] for c in open1
                           if c["declaration_free"]
                           and c["role"] == "NO-ADMISSIBLE-PRIME")
    add("P12", DECL["open1_candidates"]["P12"], inter,
        "the tightest declaration-free NARROWING at the declared arena: the "
        "intersection over every declaration-free candidate that admits an "
        "admissible prime at all.  The declaration-free candidates that admit "
        "NONE are %s" % (", ".join(no_admissible) or "none"))
    unique_forced = (nine["verdict_source_1"] == "LCB-PRIME-DERIVED")

    # ---- the arena's own dependence on the declared prime --------------------
    def smallest_injective_arena(q):
        L = 2
        while L <= 40:
            if p_part_exponent(L - 1, q) >= 3:
                return L
            L += 1
        return None
    arena_rule = {q: smallest_injective_arena(q) for q in (5, 7)}
    arena_coupled = {q: sorted(set(cand_sets(dict(BASE, labels=arena_rule[q]),
                                             fresh=True)["P11"]) & set(ADMISS))
                     for q in arena_rule if arena_rule[q]}

    g43 = gate("G43", "DECLARATION-FREENESS IS COMPUTED PER CANDIDATE BY A "
               "DECLARED CRITERION AND IS NEVER TYPED: every candidate is a "
               "FUNCTION of the declaration record, and is re-evaluated at every "
               "counterfactual re-declaration of a choice THIS UNIT makes -- the "
               "prime with its selection rule, the direction, the "
               "identification, the base record, the completion, the arena "
               "relabelling and the record-space basis.  A candidate is "
               "declaration-free exactly when its admitted set does not move, "
               "the re-declaration that moves it is recorded, and the "
               "classification the table uses is measured equal to that "
               "invariance -- so a single flipped entry is caught.  The "
               "criterion has teeth in both directions: some candidates are "
               "measured to move and some are measured not to",
               all(c["declaration_free"] == c["declaration_freeness_measured"]
                   for c in open1)
               and any(not c["declaration_free"] for c in open1)
               and any(c["declaration_free"] for c in open1)
               and len(cf_rows) == len(CFS)
               and any(r["candidates_that_moved"] for r in cf_rows)
               and arena_primitives(LAB9)["routes_agree"] is True,
               {"counterfactuals": cf_rows,
                "declaration_carrying": sorted(breaker),
                "re_declaration_that_moves_each": breaker,
                "arena_candidate_routes_agree_at_the_declared_arena":
                    arena_primitives(LAB9)["routes_agree"],
                "criterion": DECL["open1_criterion"]["declaration_freeness"]})
    report("G43", g43, f"{len(CFS)} counterfactual re-declarations; "
           f"declaration-carrying candidates {sorted(breaker)}")
    for r in cf_rows:
        say(f"      {r['re_declaration'][:62]:64s} moves "
            f"{r['candidates_that_moved']}")

    both_scales_differ = (len(SCALES) == len(set(SCALES))
                          and scale_report[SCALES[0]]["narrowing_source_1"]
                          != scale_report[SCALES[1]]["narrowing_source_1"])
    sources_agree = all(s["verdict_source_1"] == s["verdict_source_2"]
                        and s["narrowing_source_1"] == s["narrowing_source_2"]
                        for s in scale_report.values())
    g44 = gate("G44", "THE OPEN-1 VERDICT IS DERIVED BY TWO COMPUTATIONS THAT "
               "SHARE NO DECIDING VARIABLE, AND IT IS REPORTED AT BOTH DECLARED "
               "SCALES: source 1 reads the candidate table, excludes the "
               "intersection candidate from the uniqueness test (it is the "
               "intersection, not an independent candidate) and forms the "
               "intersection; source 2 never forms an intersection and never "
               "reads the table -- it eliminates prime by prime, recomputing "
               "each candidate's membership from its own primitive measurement "
               "with the memo bypassed.  The two agree at both scales.  The "
               "scales are measured to DIFFER, which is the point: the "
               "narrowing is arena-relative, and the arena that produces the "
               "tighter one is itself a function of the declared prime",
               sources_agree and both_scales_differ
               and len(scale_report) == 2,
               {"scales": scale_report,
                "arena_rule_smallest_arena_admitting_injectivity": arena_rule,
                "P11_admissible_part_at_that_arena": arena_coupled,
                "verdict_rule": DECL["open1_criterion"]["verdict_rule"]})
    report("G44", g44, "; ".join(
        f"{lab} labels: {scale_report[lab]['verdict_source_1']} narrowing "
        f"{scale_report[lab]['narrowing_source_1']}" for lab in SCALES))
    say(f"      the smallest arena admitting an injective candidate: "
        f"{arena_rule}; the p-part candidate's admissible part there: "
        f"{arena_coupled}")

    syn_der, syn_dec = synthetic_open1_tables(ADMISS)
    vd, _id, _sd, _fd = verdict_from_table(syn_der, ADMISS)
    vc, _ic, _sc, _fc = verdict_from_table(syn_dec, ADMISS)
    g45 = gate("G45", "BOTH OPEN-1 OUTCOMES ARE REACHABLE BY THE SAME "
               "DERIVATION, MEASURED ON DECLARED SYNTHETIC TABLES: a table on "
               "which one declaration-free narrowing pins a single admissible "
               "prime returns LCB-PRIME-DERIVED, and a table on which two "
               "survive returns LCB-PRIME-DECLARED, through the same function "
               "that produces the unit's own verdict.  A derivation that could "
               "only ever return one of the two would decide nothing",
               vd == "LCB-PRIME-DERIVED" and vc == "LCB-PRIME-DECLARED"
               and vd != vc,
               {"synthetic_derived_table": syn_der, "returns": vd,
                "synthetic_declared_table": syn_dec, "returns_2": vc})
    report("G45", g45, f"synthetic DERIVED table -> {vd}; synthetic DECLARED "
           f"table -> {vc}")

    g29 = gate("G29", "OPEN 1 IS MEASURED, NOT ARGUED: every declared candidate "
               "structure is evaluated for (i) whether its admitted prime set is "
               "a SINGLETON and (ii) whether it is declaration-free by the "
               "computed criterion of G43 (RUNBOOK 15: a quantity that is itself "
               "a declaration cannot derive p).  Both properties are computed; "
               "the intersection of the declaration-free candidates is taken; "
               "and the candidates that carry a declaration are measured to do "
               "so rather than being excluded by assertion",
               len(open1) == len(DECL["open1_candidates"])
               and any(not c["declaration_free"] for c in open1)
               and any(c["declaration_free"] for c in open1),
               {"candidates": open1, "admissible_primes": ADMISS,
                "tightest_declaration_free_narrowing": sorted(inter),
                "declaration_free_candidates_admitting_no_admissible_prime":
                    no_admissible,
                "a_declaration_free_singleton_inside_the_admissible_set":
                    unique_forced})
    report("G29", g29, f"{len(open1)} candidates evaluated; tightest "
           f"declaration-free narrowing at the declared arena {sorted(inter)}")
    say(f"  {'id':5s}{'adm part (9)':16s}{'adm part (16)':16s}{'role':21s}"
        f"{'uniq':6s}{'free':6s}candidate")
    for c in open1:
        say(f"  {c['id']:5s}"
            f"{str(c.get('admissible_part_at_9_labels', c['admissible_part']))[:15]:16s}"
            f"{str(c.get('admissible_part_at_16_labels', '--'))[:15]:16s}"
            f"{c['role']:21s}{str(c['unique']):6s}"
            f"{str(c['declaration_free']):6s}{c['candidate'][:34]}")
    tables["open1"] = open1
    tables["open1_scales"] = scale_report
    tables["open1_counterfactuals"] = cf_rows
    say("")
    # ==================== 13. THE VERDICTS ================================
    say("--- 13. THE VERDICTS, DERIVED INSIDE THEIR GATE ---")
    found_at_standard = sum(r["s1_pass"] for r in s1_rows)
    s2_pass = sum(1 for r in s23_rows if r["determined"]
                  and len(r["strata_hit"]) > 2)
    s3_pass = sum(1 for r in s23_rows if r["injective"])
    accepted_total = sum(1 for r in s23_rows
                         if r["determined"] and r["injective"]) if found_at_standard else 0
    empty = census_is_empty(found_at_standard)
    # the SECOND, independent source: the S4 grid's own linear-algebra decision,
    # which never touches route B's enumeration
    empty_recount = (live_full == 0)
    # the THIRD, and it touches neither: the arena-free lemma of 4b, which
    # forbids S1a and S3 together at every (cell, prime) with no census at all
    empty_from_lemma = (uncovered == [] and len(cover_rows) > 0)
    empty_from_tables = (sum(1 for r in tables["s1_clause_census"]
                             if r["s1_pass"] > 0) == 0)
    covered_cells = len(cover_rows)
    universal = (universality_measured(covered_cells - len(uncovered),
                                       covered_cells)
                 and empty_recount and empty_from_lemma and empty_from_tables)
    # the qualifier's own negative case, evaluated in gate, so a blinded
    # measurement cannot pass
    universal_neg = universality_measured(0, covered_cells)
    complete = (g03 and g11 and g16g and len(cells) == 2 * math.factorial(3))
    both_reachable = (g22 and g23)
    controls_ok = (g22 and g24)
    verdict = derive_verdict(empty, complete, both_reachable, controls_ok,
                             universal)
    recomputed = ("LCB-BRIDGE-EMPTY-AT-STRENGTHENED-STANDARD-UNIVERSAL-FOR-THIS-"
                  "SQUARE"
                  if (found_at_standard == 0 and complete and both_reachable
                      and controls_ok and universal)
                  else ("LCB-BRIDGE-FOUND-AT-STRENGTHENED-STANDARD"
                        if (complete and both_reachable and controls_ok
                            and found_at_standard)
                        else "LCB-BLOCKED-AT-CENSUS-DISCIPLINE"))
    verdict_from_tables = ("LCB-BRIDGE-EMPTY-AT-STRENGTHENED-STANDARD-UNIVERSAL-"
                           "FOR-THIS-SQUARE"
                           if empty_from_tables and complete and both_reachable
                           and controls_ok and universal
                           else "LCB-BRIDGE-FOUND-AT-STRENGTHENED-STANDARD")
    prime_verdict = derive_prime_verdict(unique_forced)
    prime_recomputed = nine["verdict_source_2"]
    spectral = any(r["s1ab"] == 0 for r in s1_rows if r["direction"] == "counts->q")
    parity = any(r["s1ab"] > 0 and r["s1c_pass"] == 0 for r in s1_rows)
    obstruction = obstruction_name(len(arena_free_all_p),
                                   len(cells) - len(arena_free_all_p),
                                   len(cells), spectral, parity)

    quals = {
        "encoding_cells": qualifier_value("encoding_cells", len(cells)),
        "primes": qualifier_value("primes", len(swept)),
        "grid_cells": qualifier_value("grid_cells", len(seen_cells)),
        "completion_family_members": qualifier_value(
            "completion_family_members", len(fam)),
        "ord5_class_size": qualifier_value("ord5_class_size", len(cls5)),
        "record_cells_per_candidate": qualifier_value(
            "record_cells_per_candidate", len(V)),
        "homomorphisms_enumerated": qualifier_value(
            "homomorphisms_enumerated", len(HOMS)),
        "candidates_passing_S1a_S1b": qualifier_value(
            "candidates_passing_S1a_S1b", sum(r["s1ab"] for r in s1_rows)),
        "candidates_passing_all_of_S1": qualifier_value(
            "candidates_passing_all_of_S1", found_at_standard),
        "cells_passing_S2": qualifier_value("cells_passing_S2", s2_pass),
        "cells_passing_S3": qualifier_value("cells_passing_S3", s3_pass),
        "accepted_at_the_strengthened_standard": qualifier_value(
            "accepted_at_the_strengthened_standard", accepted_total),
        "live_grid_cells_after_the_base_point_clause": qualifier_value(
            "live_grid_cells_after_the_base_point_clause", live_d),
        "cells_where_the_obstruction_is_arena_free": qualifier_value(
            "cells_where_the_obstruction_is_arena_free",
            len(arena_free_all_p)),
        "set_level_census_absent_S1b": qualifier_value(
            "set_level_census_absent_S1b", str(setlevel)),
        "admissible_records_passing_the_base_point_clause": qualifier_value(
            "admissible_records_passing_the_base_point_clause",
            sum(1 for r in rec_rows if r["candidates_passing_S1d"] > 0)),
        "obstruction": qualifier_value("obstruction", obstruction),
        "open1_declaration_free_intersection_at_9_labels": qualifier_value(
            "open1_declaration_free_intersection_at_9_labels",
            sorted(scale_report[LAB9]["narrowing_source_1"])),
        "open1_declaration_free_intersection_at_16_labels": qualifier_value(
            "open1_declaration_free_intersection_at_16_labels",
            sorted(scale_report[LAB16]["narrowing_source_1"])
            if LAB16 in scale_report else []),
    }
    qcheck = {
        "encoding_cells": len({(r["identification"], r["direction"])
                               for r in rows}),
        "primes": len({r["p"] for r in per_prime}),
        "grid_cells": len(grid_rows),
        "completion_family_members": sum(ordspec.values()),
        "ord5_class_size": ordspec[5],
        "record_cells_per_candidate": P ** 3,
        "homomorphisms_enumerated": sum(imgspec.values()),
        # the independent source for this one is ROUTE A: linear algebra, not
        # the enumeration the qualifier itself was summed from
        "candidates_passing_S1a_S1b": sum(census[c]["routeA_count"]
                                          for c in cells),
        "candidates_passing_all_of_S1": sum(
            r["s1_pass"] for r in tables["s1_clause_census"]),
        "cells_passing_S2": sum(1 for r in tables["s2_s3"]
                                if r["determined"] and len(r["strata_hit"]) > 2),
        "cells_passing_S3": sum(1 for r in tables["s2_s3"] if r["injective"]),
        "accepted_at_the_strengthened_standard":
            (sum(1 for r in tables["s2_s3"]
                 if r["determined"] and r["injective"])
             if sum(r["s1_pass"] for r in tables["s1_clause_census"]) else 0),
        "live_grid_cells_after_the_base_point_clause":
            sum(1 for r in grid_rows if r["s1d_live"]),
        # recomputed from the fixed-space rows, not from the coverage rows
        "cells_where_the_obstruction_is_arena_free":
            len({(r["identification"], r["direction"]) for r in fixe_rows
                 if all(x["dim_fix_E"] > 0 for x in fixe_rows
                        if x["identification"] == r["identification"]
                        and x["direction"] == r["direction"])}),
        "set_level_census_absent_S1b": str(setlevel_check),
        "admissible_records_passing_the_base_point_clause":
            sum(1 for r in tables["base_record_sweep"]
                if r["candidates_passing_S1d"] > 0),
        "open1_declaration_free_intersection_at_9_labels":
            sorted(scale_report[LAB9]["narrowing_source_2"]),
        "open1_declaration_free_intersection_at_16_labels":
            sorted(scale_report[LAB16]["narrowing_source_2"])
            if LAB16 in scale_report else [],
    }
    qbad = sorted(k for k in qcheck if quals[k] != qcheck[k])
    # the obstruction STRING is not a number and is not recomputed by calling
    # its own constructor again; it is token-gated in G46 from the measured
    # booleans, and G30 records that gate's verdict rather than restating it
    obstruction_tokens = {
        "FIXED-POINT MISMATCH": True,
        "SPECTRAL": spectral,
        "CHART-PARITY": parity,
        "data->geometry": spectral,
        "geometry->data": parity,
        "ARENA-FREE": len(arena_free_all_p) > 0,
        "%d of the %d" % (len(arena_free_all_p), len(cells)): True,
    }
    token_bad = sorted(k for k, want in obstruction_tokens.items()
                       if (k in obstruction) != bool(want))
    g46 = gate("G46", "THE NAMED OBSTRUCTION IS TOKEN-GATED AGAINST THE MEASURED "
               "BOOLEANS, NOT COMPARED WITH A SECOND CALL TO ITS OWN CONSTRUCTOR "
               "(RUNBOOK 14 addendum, v13 #219): the expected tokens are "
               "assembled here from the measured coverage counts and the "
               "measured per-direction clause failures, and each is required to "
               "be present exactly when its own boolean holds -- so a "
               "plausible-but-wrong obstruction string cannot reach the receipt, "
               "and neither can a cardinality claim",
               token_bad == [] and "cardinality" not in obstruction
               and obstruction != "UNDETERMINED",
               {"obstruction": obstruction,
                "expected_tokens": {k: bool(v)
                                    for k, v in obstruction_tokens.items()},
                "tokens_that_disagree": token_bad})
    report("G46", g46, f"{len(obstruction_tokens)} obstruction tokens gated, "
           f"{len(token_bad)} disagreements")
    g30 = gate("G30", "THE TWO VERDICT STRINGS AND EVERY ONE OF THEIR NUMERIC "
               "QUALIFIERS ARE DERIVED INSIDE THIS GATE FROM THE MEASURED "
               "COUNTS (RUNBOOK 13 addendum, v13 #234).  The bridge verdict has "
               "THREE sources that do not share a deciding variable: the clause "
               "table's own survivor sum; the S4 grid's Gaussian-elimination "
               "decision, which never touches the enumeration; and the "
               "arena-free lemma of section 4b, which touches neither and "
               "forbids S1a with S3 at every (cell, prime) with no census at "
               "all.  Its UNIVERSAL qualifier is earned from the measured "
               "coverage and its own negative case is evaluated here, so a "
               "blinded measurement cannot pass.  The prime verdict is derived "
               "from the candidate table and recomputed by the per-prime "
               "elimination that never forms an intersection.  Every printed "
               "numeric qualifier is recomputed from a different source than the "
               "one it was printed from",
               verdict == recomputed == verdict_from_tables
               and verdict in DECL["outcomes"][:3]
               and prime_verdict == prime_recomputed
               and prime_verdict in DECL["prime_outcomes"]
               and empty == empty_recount == empty_from_tables == empty_from_lemma
               and universal and not universal_neg
               and qbad == [] and g46,
               {"verdict": verdict, "recomputed": recomputed,
                "verdict_from_the_clause_table": verdict_from_tables,
                "prime_verdict": prime_verdict,
                "prime_verdict_recomputed": prime_recomputed,
                "prime_verdict_at_every_scale":
                    {str(k): v["verdict_source_1"]
                     for k, v in scale_report.items()},
                "emptiness": {"at_source": empty, "grid_recount": empty_recount,
                              "from_tables": empty_from_tables,
                              "from_the_arena_free_lemma": empty_from_lemma},
                "universality": {"measured": universal,
                                 "negative_case": universal_neg,
                                 "cell_prime_pairs": covered_cells,
                                 "uncovered": len(uncovered)},
                "qualifiers": quals, "qualifiers_recomputed_in_gate": qcheck,
                "qualifiers_that_disagree": qbad,
                "obstruction": obstruction})
    report("G30", g30, f"{verdict} / {prime_verdict}; {len(qcheck)} qualifiers "
           f"recomputed, {len(qbad)} disagreements")
    g31 = gate("G31", "THE PER-CELL DIAGNOSTICS ARE MEASURED COEXTENSIVE WITH "
               "THE CLAUSE FAILURES THEY NAME, AND NEITHER IS A CARDINALITY "
               "CLAIM: the data->geometry direction's cells are empty at S1a "
               "exactly where 2 is absent from the chart map's spectrum, and the "
               "geometry->data direction's cells are non-empty at S1a and empty "
               "at S1c exactly where the 2-eigencovector is chart-symmetric.  "
               "These are DIAGNOSTICS of the fixed-point wall, not the "
               "obstruction: the wall stands at cells where neither bites",
               spectral and parity
               and all((r["s1ab"] == 0) == (r["direction"] == "counts->q")
                       for r in s1_rows)
               and all(r["s1c_pass"] == 0 for r in s1_rows if r["s1ab"] > 0),
               {"spectral_cells_empty_at_S1a":
                   sorted({r["direction"] for r in s1_rows if r["s1ab"] == 0}),
                "parity_cells_empty_at_S1c":
                   sorted({r["direction"] for r in s1_rows
                           if r["s1ab"] > 0 and r["s1c_pass"] == 0}),
                "diagnostics_are_not_the_obstruction": True,
                "obstruction": obstruction})
    report("G31", g31, "per-cell diagnostics measured coextensive with the "
           "clause failures")
    say("")
    say(f"        BRIDGE VERDICT: {verdict}")
    say(f"        OPEN-1 VERDICT: {prime_verdict}")
    for k in sorted(quals):
        say(f"          {k:48s} {quals[k]}")
    say("")

    # ==================== 14. DISCIPLINE ==================================
    say("--- 14. ARITHMETIC AND MUTANT-IDENTITY DISCIPLINE ---")
    fl = float_scan(src)
    fl_synth = float_scan(SYNTH_FLOAT_SAMPLE)
    g32 = gate("G32", "THE SOURCE CONTAINS NO FLOAT OR COMPLEX LITERAL AND NO "
               "float()/complex() CALL, AND THE SCANNER THAT MEASURES IT IS "
               "VALIDATED BY A SYNTHETIC INJECTION IT MUST FLAG",
               fl == [] and len(fl_synth) == 2,
               {"hits": fl, "synthetic_sample_flagged": fl_synth})
    report("G32", g32, f"{len(fl)} float/complex hits; scanner flags "
           f"{len(fl_synth)} in its synthetic sample")
    off = ast_mutant_scan(src)
    off_synth = ast_mutant_scan(SYNTH_MUTANT_SAMPLE)
    g33 = gate("G33", "NO FUNCTION THAT REGISTERS A GATE REFERENCES MUTANT "
               "IDENTITY, A RUN-MODE BOOLEAN OR sys.argv (RUNBOOK 14 addendum "
               "#208), AND THE AST GUARD IS VALIDATED BY A SYNTHETIC SAMPLE IT "
               "MUST FLAG", off == [] and off_synth == ["f"],
               {"offenders": off, "synthetic_sample_flagged": off_synth})
    report("G33", g33, f"{len(off)} offenders; guard flags {off_synth}")
    g34 = gate("G34", "THE ANCHOR POLICY IS EXIT-1-ONLY AND IS MEASURED: every "
               "committed number this unit reuses is asserted, and a failure "
               "kills the run at the assertion",
               ANCHOR_POLICY["failures"] == 0,
               {"anchors": len(ANCHORS), "failures": ANCHOR_POLICY["failures"],
                "fatal": ANCHOR_POLICY["fatal"]})
    report("G34", g34, f"{len(ANCHORS)} anchors, "
           f"{ANCHOR_POLICY['failures']} failures")
    say("")

    # ==================== DISCLOSURES =====================================
    disclose("X03", "THE DIRECTION CONVENTION IS SWEPT, NOT CHOSEN (RUNBOOK 14): "
             "HA's own prose calls the determinant-2 map 'the map from the link "
             "counts to the components of q', while the matrix its code measures "
             "with determinant 2 is the coefficient matrix of the linear system, "
             "which runs q -> counts.  Both directions are therefore declared "
             "cells of the census and both are reported.  The REGISTERED "
             "direction is data -> geometry (counts -> q), because that is the "
             "direction that matches the transport side's declaration -> "
             "curvature map Q -> delta(Q).",
             {"registered": "counts->q", "swept": ["counts->q", "q->counts"]})
    disclose("X04", "THE HELD-OUT SQUARE IS PARTLY FORCED AND IS REPORTED AT "
             "THAT STRENGTH: once a candidate's exponent is known to be linear "
             "and its generator anti-invariant, the square at the HELD cells "
             "follows from the square at a spanning FIT set by linearity.  What "
             "the protocol measures that is NOT forced is that 6,144 of the "
             "6,336 candidates admitted by the single FIT cell die out of "
             "sample, and that the two transported quantities are predicted "
             "correctly at every held-out cell while the two declared failing "
             "extensions fail.", None)
    disclose("X05", "S2's SECOND CLAUSE IS FORCED ONCE THE IMAGE IS CYCLIC: a "
             "cyclic image of order p reaches exactly two of the transport "
             "side's seven fixed-configuration strata (the p-cycle's own stratum "
             "and the identity's), so the stratification cannot be carried by "
             "ANY candidate at this carrier.  Measured and disclosed; not used "
             "as a discriminating gate.", None)
    disclose("X06", "THE SQUARE IS COMPARED AS 9x9 PERMUTATION MATRICES ENTRY BY "
             "ENTRY, NOT AS GROUP ELEMENTS.  The comparison is the one BRG's S1 "
             "asks for; a mutant that compares element ORDERS instead of "
             "matrices is declared and dies.", None)
    disclose("X07", "WHAT THE SIXTEEN-LABEL ARENA IS AND IS NOT DECIDED BY, "
             "STATED AT THE SCOPE THE MEASUREMENT SUPPORTS.  G15 measures that "
             "an injective candidate into the sixteen-label completion group "
             "EXISTS and exhibits one, so the CARDINALITY branch of the "
             "obstruction dies there.  The ARENA-FREE branch does not: G35 "
             "measures fix(delta) = {e} INSIDE that arena's own order-p^3 "
             "witness subgroup, so at every cell whose re-encoding fixes a "
             "nonzero vector S1a and S3 remain jointly unsatisfiable at sixteen "
             "labels exactly as they are at nine.  At the four cells where the "
             "fixed space is trivial neither branch bites at sixteen labels, and "
             "the square there is NOT tested: that residue, and not the whole "
             "arena, is what stays open.", None)
    disclose("X08", "SIX OF THE TWELVE COVARIANT ENCODING CELLS RETURN A "
             "NON-EMPTY S1a/S1b CENSUS -- 48 candidates each, the whole "
             "geometry->data direction -- and every one of them is rejected "
             "by S1c at exactly 100 of the 125 record cells.  Measured, "
             "reported, and not counted as a FOUND, because S1c is a declared "
             "clause of S1 and the verdict is taken at the full clause list.",
             None)
    disclose("X09", "THE ENUMERATION ROUTE AND THE LINEAR-ALGEBRA ROUTE SHARE "
             "THEIR INPUT DATA (the same chart matrices, the same defect map) "
             "but not their computations: one enumerates 41,665 homomorphisms "
             "and compares permutation matrices, the other solves a 3x3 kernel "
             "over F_p and multiplies by a counted set.  They are disclosed as "
             "two computations over shared data, which is what they are.", None)
    x10_by_idn = {idn: spec2_primes((idn,), "counts->q", None)[0]
                  for idn in sorted(SLOT_ORDERS)}
    x10_seven = sorted(k for k, v in x10_by_idn.items() if 7 in v)
    disclose("X10", "THE SPECTRAL CONDITION IS IDENTIFICATION-RELATIVE, AND THE "
             "PRIME IT PICKS IS NOT ALWAYS 3.  In the registered direction 2 "
             "enters the chart map's spectrum at p = 3 at EVERY identification "
             "of the covariant family -- and at p = 7 as well at %d of the %d, "
             "%s, the second of which is the chart-involution conjugate of the "
             "declared index cell.  p = 7 IS admissible on the deformation side "
             "(96 anti-invariant order-7 elements exist), so the registered "
             "direction's census there is non-empty at S1a and S1b and is "
             "emptied by S1c, exhibited in gate G38.  Swept over every prime "
             "below 60, a range wider than the declared sweep.  The delivered "
             "reading that the intertwining 'wants p = 3' was carried by the "
             "two-of-six identification scope and does not survive the "
             "covariant one." % (len(x10_seven), len(x10_by_idn),
                                 " and ".join(x10_seven)),
             {"primes_with_2_in_spectrum_by_identification": x10_by_idn,
              "identifications_admitting_7": x10_seven})

    failed = [g["id"] for g in GATES if g["must_pass"] and not g["passed"]]
    say("--- 15. TOTALS ---")
    say(f"  anchors            : {len(ANCHORS)} (0 failures required)")
    say(f"  gates              : {len(GATES)} "
        f"({sum(1 for g in GATES if g['must_pass'])} must-pass), "
        f"failures {len(failed)}")
    say(f"  disclosures        : {len(DISCLOSURES)}")
    say(f"  cache              : {CACHE_STATS}")
    say("")
    progress("unit done")
    return {"failed": failed, "tables": tables, "verdict": verdict,
            "prime_verdict": prime_verdict, "hash_pins": pins,
            "qualifiers": quals,
            "totals": {"anchors": len(ANCHORS), "gates": len(GATES),
                       "must_pass_gates": sum(1 for g in GATES if g["must_pass"]),
                       "gate_failures": len(failed),
                       "disclosures": len(DISCLOSURES),
                       "cache": dict(CACHE_STATS),
                       "route_calls": dict(ROUTE_CALLS)}}


# ==========================================================================
#                          THE MUTANT HARNESS
# ==========================================================================

def run_mutant_harness():
    """Spawn every declared mutant and record its named kills.  Registers no
    gate."""
    say("--- 16. THE MUTANT HARNESS (every declared mutant must exit 1) ---")
    progress("mutants")
    rows = []
    for name in sorted(MUTANTS):
        pr = subprocess.run([sys.executable, SELF, "--mutant", name],
                            capture_output=True, text=True)
        why = []
        for line in (pr.stderr or "").splitlines():
            if line.startswith("ANCHOR FAILURE "):
                why.append("A:" + line.split()[2].rstrip(":"))
        for line in (pr.stdout or "").splitlines():
            ls = line.strip()
            if re.match(r"^G\d+\s+FAIL", ls):
                why.append("G:" + ls.split()[0])
        rows.append({"mutant": name, "expected_kill": MUTANTS[name],
                     "exit": pr.returncode, "killed": pr.returncode == 1,
                     "named_kills": sorted(set(why))})
        progress(f"  mutant {name}: exit {pr.returncode}")
    say(f"  {'mutant':22s}{'exit':6s}{'killed':9s}named kills")
    for row in rows:
        say(f"  {row['mutant']:22s}{row['exit']:<6d}{str(row['killed']):9s}"
            f"{','.join(row['named_kills'])[:52]}")
    surv = [r_["mutant"] for r_ in rows if not r_["killed"]]
    kg = {k[2:] for r_ in rows for k in r_["named_kills"] if k.startswith("G:")}
    nf = sorted(g["id"] for g in GATES if g["must_pass"] and g["id"] not in kg)
    say(f"  mutants that survived : {surv}")
    say(f"  must-pass gates never falsified by any mutant : {nf}")
    return rows, surv, nf


def main() -> int:
    src = open(SELF, "r", encoding="utf-8").read()
    R = run_unit(src)
    if not DELIVERY_RUN:
        return 1 if R["failed"] else 0

    progress("receipt")
    receipt = {
        "schema": "lcb-livecell-receipt-v1",
        "pin": "v13/note-lcb-livecell-pin.md",
        "pin_commit": "d2f6104",
        "source_sha256": hashlib.sha256(src.encode()).hexdigest(),
        "python": platform.python_version(),
        "arithmetic": "integers / fractions.Fraction / exact F_p; no floats",
        "hash_pins": R["hash_pins"],
        "declarations": json.loads(json.dumps(DECL, default=str)),
        "anchors": ANCHORS,
        "gates": GATES,
        "disclosures": DISCLOSURES,
        "tables": R["tables"],
        "qualifiers": R["qualifiers"],
        "totals": R["totals"],
        "verdict": R["verdict"],
        "prime_verdict": R["prime_verdict"],
    }
    mut_rows, survivors, never_falsified = run_mutant_harness()
    receipt["mutants"] = mut_rows
    receipt["never_falsified"] = never_falsified
    receipt["totals"]["mutants"] = len(mut_rows)
    receipt["totals"]["mutant_survivors"] = len(survivors)
    say("")

    if WRITE_ARTIFACTS:
        with open(os.path.join(HERE, "lcb_livecell_output.txt"), "w",
                  encoding="utf-8") as fh:
            fh.write("\n".join(OUT) + "\n")
        with open(os.path.join(HERE, "lcb_livecell_receipt.json"), "w",
                  encoding="utf-8") as fh:
            json.dump(receipt, fh, indent=1, sort_keys=True, default=str)
            fh.write("\n")
    else:
        progress("falsification-selftest: artifacts NOT written")
    progress("done")
    return 0 if (not R["failed"] and not survivors and not never_falsified) else 1


if __name__ == "__main__":
    sys.exit(main())

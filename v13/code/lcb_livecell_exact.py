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
    # --- held-out ---------------------------------------------------------
    "heldout-leak":        "the candidate is fitted on the held-out cells",
    "teeth-off":           "the declared failing extension is silently made the "
                           "accepted one",
    "quantity-lax":        "a transported held-out quantity is read off the wrong "
                           "map",
    # --- controls ---------------------------------------------------------
    "ident-block":         "the identity self-morphism is made unfindable",
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
    # --- verdict ----------------------------------------------------------
    "obstruction-misname": "the named obstruction is replaced by a cardinality "
                           "claim",
    "verdict-flip":        "the verdict derivation returns a hand-typed string",
    "count-flip":          "the emptiness decision is inverted at its own source",
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
_M_HELDOUT = (MUTANT == "heldout-leak")
_M_TEETH = (MUTANT == "teeth-off")
_M_QUANTITY = (MUTANT == "quantity-lax")
_M_IDENT = (MUTANT == "ident-block")
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
_M_OBSTR = (MUTANT == "obstruction-misname")
_M_VERDICT = (MUTANT == "verdict-flip")
_M_COUNTFLIP = (MUTANT == "count-flip")
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
        "family": "4 declared ENCODING CELLS = 2 identifications x 2 directions; "
                  "7 declared primes; 8 measured defect-order classes; the "
                  "4,608-member ord-5 completion class; HA's 9 admissible "
                  "geometry records + 2 declared negative controls",
        "law": "the strengthened standard S1-S6 as BRG's terminal paper section "
               "2.6 registers it, operationalised clause by clause below; a "
               "candidate morphism is a map alpha : V -> G_C",
        "state": "the deformation side's declared base geometry record r0 = "
                 "G-FLAT's count triple (1,1,2); the transport side's declared "
                 "base completion Q0 (the lex-first ord-5 member); the transport "
                 "side's initial configuration j0 = 0",
        "arena action": "the identification sweep (natural / index); the DIRECTION "
                        "sweep (counts->q / q->counts) -- the orientation "
                        "convention RUNBOOK 14 requires to be swept; relabelling "
                        "of the 9 completion labels by a permutation fixing label "
                        "0; change of basis of the record datum space by an "
                        "element of GL_3(F_p); the prime sweep; the choice of "
                        "completion inside the declared ord-5 class",
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
                     "index order: n_e1 <-> q11, n_e2 <-> q12, n_diag <-> q22"},
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
        "H2": "ord(delta(alpha(r))) at every HELD cell -- a transport-side "
              "physical quantity",
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
        "F0-IDENT": "POSITIVE CONTROL: the identity self-morphism of the transport "
                    "arena -- source and target both the completion group with the "
                    "encoding delta, alpha = the identity.  The census machinery "
                    "must FIND it, at every one of the 40,320 cells, and it must "
                    "pass S1a, S1c, S1d and S3.",
        "SYNTH-COMPATIBLE": "a declared synthetic compatible pair: the same "
                            "transport side against a synthetic chart map E~ whose "
                            "2-eigencovector is chart-ANTIsymmetric.  The machinery "
                            "must FIND candidates and they must pass S1a-S1d.",
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
    "outcomes": ["LCB-BRIDGE-EMPTY-AT-STRENGTHENED-STANDARD",
                 "LCB-BRIDGE-FOUND-AT-STRENGTHENED-STANDARD",
                 "LCB-BLOCKED-AT-CENSUS-DISCIPLINE"],
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


def encoding_matrix(identification: str, direction: str):
    """HA's record<->metric readout, rebuilt exactly as ha_successor_exact.py
    builds it (rows = the declared links, columns = the metric components), then
    read as an ENDOMORPHISM of the one datum space under the declared
    identification and in the declared direction.  [instrument -- mutable]"""
    corder = [(1, 0), (0, 1), (1, 1)]
    morder = ({"natural": [(0, 0), (1, 1), (0, 1)],
               "index": [(0, 0), (0, 1), (1, 1)]})[identification]
    A = [[Fr(lk[i] * lk[j] * (1 if i == j else 2)) for (i, j) in morder]
         for lk in corder]
    if _M_READOUT:
        A[0][2] = A[0][2] + Fr(1)
    return A if direction == "q->counts" else inv3(A)


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
    """The declared 2 x 2 encoding-cell sweep.  [instrument -- mutable]"""
    cells = [(idn, dr) for idn in ("natural", "index")
             for dr in ("counts->q", "q->counts")]
    if _M_ENCDROP:
        cells = cells[:3]
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
    """The identity self-morphism.  [instrument -- mutable]"""
    if _M_IDENT:
        return pmul(pident(n), (1, 0) + tuple(range(2, n)))
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


def declaration_free(pid, computed):
    """Whether an Open-1 candidate is declaration-free: it must take no declared
    prime and no declared choice of this unit among its inputs.
    [instrument -- mutable]"""
    if _M_OPEN1:
        return True
    return computed


def unique_prime(sets):
    """Whether a candidate's output set determines the prime uniquely.
    [instrument -- mutable]"""
    if _M_UNIQUE:
        return len(sets) <= 2
    return len(sets) == 1


def obstruction_name(spectral, parity):
    """The named obstruction, derived from the measured clause failures.
    [instrument -- mutable]"""
    if _M_OBSTR:
        return "unequal carrier cardinality"
    if spectral and parity:
        return ("S1 -- encoding intertwining: SPECTRAL in the data->geometry "
                "direction (2 is not in the chart map's spectrum) and "
                "CHART-PARITY in the geometry->data direction (the "
                "2-eigencovector is chart-symmetric where the intertwining "
                "needs it chart-antisymmetric)")
    return "UNDETERMINED"


def census_is_empty(found_at_standard):
    """The emptiness decision, taken at its own source so a corruption of it is
    caught by the verdict gate's independent recount.  [instrument -- mutable]"""
    if _M_COUNTFLIP:
        return found_at_standard != 0
    return found_at_standard == 0


def derive_verdict(empty, complete, both_reachable, controls_ok):
    """The verdict string, DERIVED from the measured booleans inside its gate.
    [instrument -- mutable]"""
    if _M_VERDICT:
        return "LCB-BRIDGE-FOUND-AT-STRENGTHENED-STANDARD"
    if not (complete and both_reachable and controls_ok):
        return "LCB-BLOCKED-AT-CENSUS-DISCIPLINE"
    return ("LCB-BRIDGE-EMPTY-AT-STRENGTHENED-STANDARD" if empty
            else "LCB-BRIDGE-FOUND-AT-STRENGTHENED-STANDARD")


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
    # the chart involution's slot permutation in each of the two coordinate
    # orders; an identification is CHART-COMPATIBLE when the two agree
    slot_tau = {}
    for idn, morder in (("natural", [(0, 0), (1, 1), (0, 1)]),
                        ("index", [(0, 0), (0, 1), (1, 1)])):
        sw = {0: 1, 1: 0}
        img = [morder.index(tuple(sorted((sw[i], sw[j])))) for (i, j) in morder]
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
    g09 = gate("G09", "THE FOUR DECLARED ENCODING CELLS ARE BUILT AND "
               "CELL-COMPLETE (2 identifications x 2 directions), EACH ONE "
               "INVERTIBLE MOD p, AND THE CHART INVOLUTION IS READ IN BOTH "
               "COORDINATE ORDERS: the NATURAL identification carries the chart "
               "involution -- the axis swap induces the SAME slot permutation on "
               "counts and on the metric, and the re-encoding is measured to "
               "COMMUTE with it, so the deformation side's encoding is "
               "chart-EQUIVARIANT -- while the INDEX identification is measured "
               "NOT to carry it.  Exactly one of the two identifications is "
               "chart-compatible, and that is a measurement",
               len(cells) == 4 and len(set(cells)) == 4 and invertible
               and TAU != pident(3) and compat["natural"]
               and not compat["index"]
               and tau_equiv == sum(1 for (a, b) in cells if compat[a]),
               {"cells": [list(c) for c in cells],
                "tau_on_counts": list(TAU),
                "tau_induced_slot_permutation": {k: list(v)
                                                 for k, v in slot_tau.items()},
                "chart_compatible": compat,
                "tau_equivariant_cells": tau_equiv,
                "matrices": {f"{a}|{b}": {"det": enc[(a, b)]["det"],
                                          "charpoly": enc[(a, b)]["charpoly"],
                                          "mod_p": enc[(a, b)]["Fp"]}
                             for (a, b) in cells}})
    report("G09", g09, f"{len(cells)} encoding cells, all invertible; "
           f"chart-compatible identifications {compat}; {tau_equiv} cells "
           f"chart-equivariant")
    for (a, b) in cells:
        say(f"      {a:8s} {b:10s} det {enc[(a, b)]['det']:>5s}  "
            f"E mod 5 = {enc[(a, b)]['Fp']}")
    tables["encoding_cells"] = {f"{a}|{b}": enc[(a, b)]["Fp"] for (a, b) in cells}
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

    def alpha_from_triple(tr, r):
        out = pident(NLAB)
        for k in range(3):
            for _ in range(r[k]):
                out = pmul(out, tr[k])
        return out

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
        say(f"      {r['identification']:8s} {r['direction']:10s} "
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
               len(rows) == 4 and len({(r["identification"], r["direction"])
                                       for r in rows}) == 4
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

    # ==================== 5. S1c, S1d =====================================
    say("--- 5. S1c (CHART INVOLUTION) AND S1d (BASE POINT) ---")
    r0 = base_record(RECORDS)
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
        say(f"      {r['identification']:8s} {r['direction']:10s} S1a+b "
            f"{r['s1ab']:4d}   S1c pass {r['s1c_pass']:4d}   S1d pass "
            f"{r['s1d_pass']:4d}   S1 all {r['s1_pass']:4d}   "
            f"S1c violations/cand {r['s1c_violation_counts']}")
    tables["s1_clause_census"] = s1_rows
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
        say(f"      {r['identification']:8s} {r['direction']:10s} candidates "
            f"{r['candidates']:4d}  determined {str(r['determined']):5s}  "
            f"strata hit {r['strata_hit']} of {len(strata_declared)}  "
            f"|image| {r['image_size']}  injective {r['injective']}")
    tables["s2_s3"] = s23_rows

    # S3's positive control: the sixteen-label arena
    p16 = p_part_exponent(15, P)

    def cyc(lo):
        t = list(range(16))
        for k in range(5):
            t[lo + k] = lo + (k + 1) % 5
        return tuple(t)
    g16 = [cyc(1), cyc(6), cyc(11)]
    img16 = group_closure(g16, 16)
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
            s1d_live = s1ab_live and (n == p)
            s1_live = (kdc > 0 and has_elt and n == p)
            grid_rows.append({"identification": idn, "direction": dr, "p": p,
                              "ord_D": n, "two_in_spectrum": kd > 0,
                              "two_eigencovector_chart_antisymmetric": kdc > 0,
                              "anti_elements": anti_by_p[p],
                              "s1ab_live": s1ab_live, "s1d_live": s1d_live,
                              "s1_live": s1_live})
    live_ab = sum(1 for r in grid_rows if r["s1ab_live"])
    live_d = sum(1 for r in grid_rows if r["s1d_live"])
    live_full = sum(1 for r in grid_rows if r["s1_live"])
    g16g = gate("G16", "S4 IS A CELL-COMPLETE CENSUS OVER THE WHOLE DECLARED "
                "(prime, defect-order) GRID AT EVERY ENCODING CELL: each cell is "
                "visited exactly once, the count is computed from the declared "
                "sets rather than typed, and the narrowing the strengthened "
                "standard performs on BRG's live cells is read off it",
                len(seen_cells) == len(cells) * len(swept) * len(orders_declared)
                and len(grid_rows) == len(seen_cells),
                {"cells": len(seen_cells), "primes": len(swept),
                 "defect_orders": orders_declared,
                 "encoding_cells": len(cells),
                 "cells_live_at_S1ab": live_ab,
                 "cells_live_after_the_base_point_clause": live_d,
                 "cells_live_at_the_full_S1_clause_list": live_full,
                 "anti_invariant_elements_by_prime": anti_by_p})
    report("G16", g16g, f"{len(seen_cells)} grid cells; live at S1a+b "
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
    FIT = fit_cells(V, E1)
    HELD = [r for r in V if r not in set(FIT)]

    def alpha_gl(g, lam, r):
        k = sum(lam[i] * r[i] for i in range(3)) % P
        out = pident(NLAB)
        for _ in range(k):
            out = pmul(out, g)
        return out

    fit_admitted = []
    for g in [x for x in COMPL if pord(x) == P]:
        for lam in V:
            if lam == (0, 0, 0):
                continue
            if all(compare_square(defect_cached(alpha_gl(g, lam, r)),
                                  alpha_gl(g, lam, mat_apply(Esy, r, P)))
                   for r in FIT):
                fit_admitted.append((g, lam))
    held_ok, held_bad, held_viol = [], [], 0
    for (g, lam) in fit_admitted:
        bad_here = False
        for r in HELD:
            if not compare_square(defect_cached(alpha_gl(g, lam, r)),
                                  alpha_gl(g, lam, mat_apply(Esy, r, P))):
                bad_here = True
                break
        if not bad_here:
            held_ok.append((g, lam))
        else:
            held_bad.append((g, lam))
    if held_bad:
        g_, l_ = held_bad[0]
        held_viol = sum(1 for r in HELD
                        if not compare_square(
                            defect_cached(alpha_gl(g_, l_, r)),
                            alpha_gl(g_, l_, mat_apply(Esy, r, P))))
    g18 = gate("G18", "THE HELD-OUT VERIFICATION IS PREDICTIVE, NOT IMPOSED: the "
               "split is declared before any candidate is fitted, candidates are "
               "admitted by the square at the FIT cell ALONE, and the square is "
               "then VERIFIED at every HELD cell -- where most FIT-admitted "
               "candidates die.  A protocol under which nothing died out of "
               "sample would verify nothing",
               len(FIT) == 1 and len(HELD) == P ** 3 - 1
               and len(fit_admitted) > len(held_ok) and len(held_bad) > 0,
               {"FIT": [list(r) for r in FIT], "HELD_cells": len(HELD),
                "fit_admitted": len(fit_admitted),
                "survived_held_out": len(held_ok),
                "rejected_out_of_sample": len(held_bad),
                "total_held_out_violations": held_viol})
    report("G18", g18, f"FIT {len(FIT)} cell admits {len(fit_admitted)} "
           f"candidates; {len(held_bad)} die on {len(HELD)} held-out cells, "
           f"{len(held_ok)} survive")

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
    g21 = gate("G21", "POSITIVE CONTROL: THE CENSUS MACHINERY FINDS THE IDENTITY "
               "SELF-MORPHISM.  The transport arena is paired with itself -- the "
               "completion group with the encoding delta on both sides -- and "
               "the identity candidate is run through the SAME square "
               "comparison, at every one of the family's cells, and through the "
               "same S1c, S1d and S3 clauses.  A predicate that could not accept "
               "the identity would decide nothing",
               ident_bad == 0 and ident_inj and ident_s1c and ident_s1d
               and ident_cells == len(COMPL),
               {"cells": ident_cells, "square_violations": ident_bad,
                "injective": ident_inj, "s1c": ident_s1c, "s1d": ident_s1d})
    report("G21", g21, f"identity self-morphism: {ident_bad} square violations "
           f"at {ident_cells} cells; injective {ident_inj}")

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
    g22 = gate("G22", "FOUND IS REACHABLE BY THIS MACHINERY, AND ITS WITNESS IS "
               "EXHIBITED AND INDEPENDENTLY RE-VERIFIED: a declared synthetic "
               "compatible pair -- the same transport side against a synthetic "
               "chart map whose 2-eigencovector is chart-ANTIsymmetric -- yields "
               "candidates that pass S1a, S1b, S1c AND S1d, and the exhibited "
               "witness is re-checked here from its own two data at every cell",
               len(synth_ok) > 0 and len(synth_c) > 0 and len(synth_d) > 0
               and wit is not None and wit_ok,
               {"synthetic_chart_map": Esy,
                "pairs_passing_S1a_S1b": len(synth_ok),
                "distinct_maps": len(synth_maps),
                "passing_S1c": len(synth_c), "passing_S1d": len(synth_d),
                "witness": [list(wit[0]), list(wit[1])] if wit else None,
                "witness_reverified": wit_ok})
    report("G22", g22, f"synthetic compatible pair: {len(synth_ok)} pairs, "
           f"{len(synth_maps)} distinct maps, {len(synth_c)} pass S1c, "
           f"{len(synth_d)} pass S1d; witness re-verified {wit_ok}")
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
    declared_set = sorted(f"{a}|{b}" for (a, b) in
                          [(i, d) for i in ("natural", "index")
                           for d in ("counts->q", "q->counts")])
    verdict_sel = sorted(f"{r['identification']}|{r['direction']}"
                         for r in rows if r["route_B_enumeration"] > 0)
    tested = selftest_set(declared_set, verdict_sel)
    g27 = gate("G27", "THE SELF-TESTS' TESTED SET IS FIXED BY DECLARATION AND "
               "NEVER SELECTED BY THE VERDICTS UNDER AUDIT (RUNBOOK 14 addendum "
               "#185): the declared set is the full 2 x 2 sweep including the "
               "cells whose census is empty, and it is measured equal to the "
               "declaration and strictly larger than the set the verdicts would "
               "have selected",
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
    fam_primes = set()
    for n in ordspec:
        m = 2 * n
        d = 2
        while d * d <= m:
            if m % d == 0:
                fam_primes.add(d)
                while m % d == 0:
                    m //= d
            d += 1
        if m > 1:
            fam_primes.add(m)
    elt_primes = {p for p in range(2, NLAB + 1)
                  if all(p % k for k in range(2, p))
                  and any(pord(g) == p for g in COMPL)}
    rho_den = max(RHO[0].denominator, RHO[1].denominator)
    rho_primes = {q for q in PRANGE if rho_den % q == 0}
    det_primes = {q for q in PRANGE if int(det_ha) % q == 0}
    spec2 = set()
    undefined_primes = set()
    for p in range(2, 60):
        if all(p % k for k in range(2, p)):
            for (idn, dr) in cells:
                if dr != "counts->q":
                    continue
                MQ = enc[(idn, dr)]["Q"]
                if any(x.denominator % p == 0 for row in MQ for x in row):
                    undefined_primes.add(p)
                    continue
                Tp = to_fp(transpose(MQ), p)
                Mt = [[(Tp[i][j] - (2 if i == j else 0)) % p for j in range(3)]
                      for i in range(3)]
                if kernel_dim(Mt, p) > 0:
                    spec2.add(p)
    open1 = []

    def add(pid, statement, out_set, free, note):
        out = sorted(out_set) if isinstance(out_set, (set, list)) else out_set
        u = unique_prime(out) if isinstance(out, list) else False
        inside = sorted(set(out) & set(ADMISS))
        open1.append({"id": pid, "candidate": statement,
                      "primes_it_admits": out,
                      "admissible_part": inside,
                      "role": ("NARROWING" if inside else "NO-ADMISSIBLE-PRIME"),
                      "unique": bool(u),
                      "declaration_free": bool(declaration_free(pid, free)),
                      "note": note})

    add("P1", DECL["open1_candidates"]["P1"], [P], False,
        "the carrier size p^(k+d) = %d is a FUNCTION of the declared p; it "
        "cannot derive it" % nHA)
    add("P2", DECL["open1_candidates"]["P2"], sorted(PRANGE), False,
        "k, d, L and the link set are declared arena data and constrain no prime")
    add("P3", DECL["open1_candidates"]["P3"],
        sorted({q for q in PRANGE if (2 * pord(D9)) % q == 0}), False,
        "2*ord(D) = %d, but ord(D) = 5 is THIS unit's declared selection rule; "
        "the candidate contains its own conclusion" % len(GRP))
    add("P4", DECL["open1_candidates"]["P4"], sorted(fam_primes), True,
        "the family's own defect orders admit %s; intersected with "
        "admissibility, two survive" % sorted(fam_primes))
    add("P5", DECL["open1_candidates"]["P5"], sorted(elt_primes), True,
        "the completion group has elements of order p for p in %s; intersected "
        "with admissibility, two survive" % sorted(elt_primes))
    add("P6", DECL["open1_candidates"]["P6"],
        sorted(set(PRANGE) - det_primes), True,
        "the readout determinant is %s, so the re-encoding is invertible at "
        "every prime but 2 -- a single exclusion, not a derivation" % det_ha)
    add("P7", DECL["open1_candidates"]["P7"],
        sorted(set(PRANGE) - rho_primes), True,
        "rho's denominator is %d, so the deformation side does not exist at 2 "
        "or 3" % rho_den)
    add("P8", DECL["open1_candidates"]["P8"], sorted(spec2), True,
        "the intertwining is solvable at exactly one prime in the registered "
        "direction, swept over every prime below 60 -- and it is a prime the "
        "deformation side cannot be built at; the re-encoding is undefined at "
        "%s" % sorted(undefined_primes))
    add("P9", DECL["open1_candidates"]["P9"],
        sorted(spec2 - rho_primes), True,
        "the joint system is EMPTY: the only prime that solves the intertwining "
        "is one of the two at which rho fails to reduce")
    add("P10", DECL["open1_candidates"]["P10"],
        sorted({p for p in ADMISS if anti_by_p.get(p, 0) > 0}), True,
        "48 at p = 5 and 96 at p = 7; zero at every larger declared prime")
    add("P11", DECL["open1_candidates"]["P11"], [], True,
        "the p-part of the completion group's order is p^1 at every prime, "
        "against |V| = p^3: no prime admits an injective candidate here")
    free_sets = [set(c["admissible_part"]) for c in open1
                 if c["declaration_free"] and c["role"] == "NARROWING"]
    inter = set(ADMISS)
    for s in free_sets:
        inter &= s
    no_admissible = sorted(c["id"] for c in open1
                           if c["declaration_free"]
                           and c["role"] == "NO-ADMISSIBLE-PRIME")
    add("P12", DECL["open1_candidates"]["P12"], sorted(inter), True,
        "the tightest declaration-free NARROWING: the intersection over every "
        "declaration-free candidate that admits an admissible prime at all.  "
        "The declaration-free candidates that admit NONE are %s"
        % ", ".join(no_admissible))
    unique_forced = any(c["unique"] and c["declaration_free"]
                        and c["role"] == "NARROWING"
                        and set(c["primes_it_admits"]) <= set(ADMISS)
                        and c["primes_it_admits"] for c in open1)
    g29 = gate("G29", "OPEN 1 IS MEASURED, NOT ARGUED: every declared candidate "
               "structure is evaluated for (i) whether its admitted prime set is "
               "a SINGLETON and (ii) whether it is itself declaration-free "
               "(RUNBOOK 15: a quantity that is itself a declaration cannot "
               "derive p).  Both properties are computed; the intersection of "
               "the declaration-free candidates is taken; and the candidates "
               "that carry a declaration are measured to do so rather than being "
               "excluded by assertion",
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
           f"declaration-free narrowing {sorted(inter)}")
    say(f"  {'id':5s}{'admissible part':18s}{'role':21s}{'uniq':6s}{'free':6s}"
        f"candidate")
    for c in open1:
        say(f"  {c['id']:5s}{str(c['admissible_part'])[:17]:18s}{c['role']:21s}"
            f"{str(c['unique']):6s}{str(c['declaration_free']):6s}"
            f"{c['candidate'][:36]}")
    tables["open1"] = open1
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
    empty_from_tables = (sum(1 for r in tables["s1_clause_census"]
                             if r["s1_pass"] > 0) == 0)
    complete = (g03 and g11 and g16g and len(cells) == 4)
    both_reachable = (g22 and g23)
    controls_ok = (g21 and g24)
    verdict = derive_verdict(empty, complete, both_reachable, controls_ok)
    recomputed = ("LCB-BRIDGE-EMPTY-AT-STRENGTHENED-STANDARD"
                  if (found_at_standard == 0 and complete and both_reachable
                      and controls_ok)
                  else ("LCB-BRIDGE-FOUND-AT-STRENGTHENED-STANDARD"
                        if (complete and both_reachable and controls_ok)
                        else "LCB-BLOCKED-AT-CENSUS-DISCIPLINE"))
    verdict_from_tables = ("LCB-BRIDGE-EMPTY-AT-STRENGTHENED-STANDARD"
                           if empty_from_tables and complete and both_reachable
                           and controls_ok
                           else "LCB-BRIDGE-FOUND-AT-STRENGTHENED-STANDARD")
    prime_verdict = derive_prime_verdict(unique_forced)
    prime_recomputed = ("LCB-PRIME-DERIVED" if len(inter) == 1
                        else "LCB-PRIME-DECLARED")
    spectral = any(r["s1ab"] == 0 for r in s1_rows if r["direction"] == "counts->q")
    parity = any(r["s1ab"] > 0 and r["s1c_pass"] == 0 for r in s1_rows)
    obstruction = obstruction_name(spectral, parity)

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
        "obstruction": qualifier_value("obstruction", obstruction),
        "open1_declaration_free_intersection": qualifier_value(
            "open1_declaration_free_intersection", sorted(inter)),
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
        "candidates_passing_S1a_S1b": sum(len(census[c]["routeB"]) for c in cells),
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
        "obstruction": obstruction_name(spectral, parity),
        "open1_declaration_free_intersection": sorted(inter),
    }
    qbad = sorted(k for k in qcheck if quals[k] != qcheck[k])
    g30 = gate("G30", "THE TWO VERDICT STRINGS AND EVERY ONE OF THEIR "
               "QUALIFIERS ARE DERIVED INSIDE THIS GATE FROM THE MEASURED "
               "COUNTS (RUNBOOK 13 addendum, v13 #234): the bridge verdict is "
               "derived once from the emptiness decision, recomputed by a second "
               "expression over the same booleans, and derived a THIRD time from "
               "the recorded clause table by re-reading the per-cell survivor "
               "counts; the prime verdict is derived and recomputed from the "
               "candidate table's own intersection; and every printed qualifier "
               "is recomputed here from its own source",
               verdict == recomputed == verdict_from_tables
               and verdict in DECL["outcomes"][:2]
               and prime_verdict == prime_recomputed
               and prime_verdict in DECL["prime_outcomes"]
               and empty == empty_recount == empty_from_tables
               and qbad == [] and obstruction != "UNDETERMINED"
               and "cardinality" not in obstruction,
               {"verdict": verdict, "recomputed": recomputed,
                "verdict_from_the_clause_table": verdict_from_tables,
                "prime_verdict": prime_verdict,
                "prime_verdict_recomputed": prime_recomputed,
                "emptiness": {"at_source": empty, "recount": empty_recount,
                              "from_tables": empty_from_tables},
                "qualifiers": quals, "qualifiers_recomputed_in_gate": qcheck,
                "qualifiers_that_disagree": qbad,
                "obstruction": obstruction})
    report("G30", g30, f"{verdict} / {prime_verdict}; {len(qcheck)} qualifiers "
           f"recomputed, {len(qbad)} disagreements")
    g31 = gate("G31", "THE NAMED OBSTRUCTION IS MEASURED COEXTENSIVE WITH THE "
               "CLAUSE FAILURES AND IS NOT A CARDINALITY CLAIM: the "
               "data->geometry direction's cells are empty at S1a exactly where "
               "2 is absent from the chart map's spectrum, and the "
               "geometry->data direction's cells are non-empty at S1a and empty "
               "at S1c exactly where the 2-eigencovector is chart-symmetric.  No "
               "cardinality test is used as a criterion anywhere in this unit",
               spectral and parity
               and all((r["s1ab"] == 0) == (r["direction"] == "counts->q")
                       for r in s1_rows),
               {"spectral_cells_empty_at_S1a": [r["direction"] for r in s1_rows
                                                if r["s1ab"] == 0],
                "parity_cells_empty_at_S1c": [r["direction"] for r in s1_rows
                                              if r["s1ab"] > 0
                                              and r["s1c_pass"] == 0],
                "obstruction": obstruction})
    report("G31", g31, "obstruction measured coextensive with the clause "
           "failures")
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
    disclose("X07", "THE UNIT DECIDES NOTHING ABOUT THE SIXTEEN-LABEL ARENA "
             "BEYOND ITS ARITHMETIC: G15 measures that an injective candidate "
             "into the sixteen-label completion group EXISTS and exhibits one. "
             "Whether any of them satisfies the commuting square there is NOT "
             "tested and is registered as an open question.", None)
    disclose("X08", "TWO OF THE FOUR ENCODING CELLS RETURN A NON-EMPTY S1a/S1b "
             "CENSUS -- 48 candidates each -- and every one of them is rejected "
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
    disclose("X10", "THE PRIME 3 IS THE ONLY PRIME AT WHICH THE REGISTERED "
             "INTERTWINING IS SOLVABLE, AND IT IS INADMISSIBLE ON THE "
             "DEFORMATION SIDE.  The chart map's spectrum contains 1, 1/2 and "
             "(in the index identification) -1; 2 joins it only when 2 = 1/2 or "
             "2 = -1 mod p, i.e. only at p = 3, where HA's residual (1/6,1/6) "
             "does not reduce.  This is measured over a prime range wider than "
             "the declared sweep.", None)

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

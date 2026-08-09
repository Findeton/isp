#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""
RSQ -- THE RE-POSED SQUARE AT THREE WINGS
=========================================

Pin: v13/note-rsq-reposed-square-pin.md (STRICT, frozen, sha256 bc79fb6111ff...,
commit d9e3a66).  Binding: BRG's terminal S1-S6 registry (paper section 2.6);
TB3's terminal three-wing machinery; LCB's terminal fixed-point mismatch and
covariant-cell machinery; HA's terminal G28/G29; RUNBOOK 13 (verdict-in-gate
with computed qualifiers, verdict-flip and no-witness mutants,
cell-completeness, genuinely independent routes), RUNBOOK 14 (symmetry
self-tests, all addenda) and RUNBOOK 15 (declared-arena discipline, all
addenda).

THE QUESTION.  LCB proved the OLD square empty universally by the FIXED-POINT
MISMATCH.  The from-question therefore moves to the flesh: is there a
DIFFERENT, honestly-motivated encoding pairing at three wings whose square is
not stillborn?

THE PAIRING (all of section 2 below is declaration, recorded before any
candidate is evaluated):

  DEFORMATION SIDE   HA rebuilt at d = 3: X = (Z_3)^3, 27 sites, 6 links (the
      3 axes and the 3 positive diagonals), the record datum space
      V = F_p^6 = the six link counts at a site, and HA's record-is-metric
      readout E with determinant 8 and spectrum {1,1,1,2,2,2} in the
      q -> counts direction.  The arena C_HA(p) = F_p^k x F_p^3 is rebuilt
      with 3-DIMENSIONAL fronts and G29 is re-proved there.
  TRANSPORT SIDE     TB3's three-wing base: the 8 system-triple labels
      F_2^3, the completion group G_C = the permutations fixing label 0
      (order 5,040), the wing symmetry group S_3 acting by bit permutation,
      and the three-wing commutator encoding
          delta_pi(Q) = Sigma_pi Q^-1 Sigma_pi^-1 Q
      -- TB3's F_3, the form TB3 measured to reproduce the defect at 54 of 54
      cells.

THE SQUARE, at a declared wing symmetry pi:

        V  --E-->  V                E : HA's record <-> metric re-encoding at
        |          |                    d = 3 (det 8)
      alpha      alpha              delta_pi : the three-wing commutator
        v          v                    encoding
        G_C -d_pi-> G_C

with S1c generalised, per R2-LCB's F-10, from the two-wing Z/2 SIGN condition
to the F_p[S_3] MODULE condition: alpha intertwines the S_3-action on the
record datum space with the wing action on the image.

THE STILLBORN PRECHECK (the LCB lesson, made structural and run FIRST, per
candidate, before any census): the square forces alpha(fix E) contained in
fix delta_pi.  fix delta_pi is measured to be {e} at every wing symmetry and
every arena -- exactly one point, arena-free -- so an injective candidate
needs |fix E| = 1, i.e. dim ker(E - I) = 0 over F_p.  A candidate whose
structures cannot match is STILLBORN and its census is not run; the mismatch
is computed and recorded.

WHAT THE UNIT MEASURES, in one line each:

  * HA CONSTRUCTS AT d = 3.  Records admissible, readout det 8, spectrum
    {1,1,1,2,2,2}, residual rho(x*) = (1/6, 1/6, 0), and G29 holds verbatim:
    R_HH is the translation of the 3-dimensional address register by rho mod p
    with the front sector fixed, so <R_HH> = Z/p.
  * THE FIXED-POINT WALL TRANSPORTS.  fix(delta_pi) = {e} at all six wing
    symmetries, measured over the whole 5,040-member completion group.
  * EVERY MOTIVATED IDENTIFICATION IS STILLBORN.  The two S_3-equivariant
    identifications (computed, never typed) have fixed spaces of dimension 3
    and 2, and HA's own sym_index ordering has dimension 1, at every declared
    prime and in both directions: 6 cells, 42 rows, 0 survivors.  The pin's
    minimum candidate dies at the precheck, and so does HA's own coordinate.
  * THE GENERIC COVARIANT FAMILY HAS SURVIVORS.  Over the whole covariant
    orbit -- 720 slot orders x 2 directions = 1,440 cells -- a measured
    minority have trivial fixed space at every declared prime, and every one
    of them is an arbitrary relabelling of the six metric slots.  The precheck
    is passed; the census runs; and the FOUND half of the verdict carries the
    identification class it is true of, with the motivated sub-family's own
    outcome (RSQ-NO-COMPATIBLE-SQUARE) reported beside it.
  * THE MASTER EQUATION.  S1a, S1b and S3 force I - E = alpha^-1 rho alpha
    with rho the conjugation action of Sigma_pi on the image.  Every wall
    below is a reading of it: rho invertible is LCB's fixed-point mismatch,
    rho^ord = I is the order obstruction, rho = rho_V(pi) is the
    permutation-module obstruction -- and the third clears the other two and
    kills the candidate anyway.
  * THE CENSUS IS EMPTY, AND THE EMPTINESS IS A THEOREM.  S1a (BRG's
    registered square), S1b (additivity) and S3 (BRG's registered injectivity
    horn) jointly force
          (I - E)^ord(pi) = I,
    equivalently E = 2I at an involution and E^2 - 3E + 3I = 0 at an order-3
    wing symmetry.  Measured 0 of 20,160 rows -- and PROVED at every prime
    p >= 5 by the READOUT-PROFILE THEOREM: every row of the readout has one of
    exactly two entry multisets, so row 0 is a 0/1 unit vector e_k, and the
    criterion read at row 0 (using row_0(A^2) = row_k(A)) forces p to divide an
    explicit integer witness whose gcd is measured to admit no prime >= 5.
    THAT IS THE ORDER OBSTRUCTION, and it is strictly stronger than the
    fixed-point mismatch, which it subsumes.
  * THE MODULE CLAUSE DIES UNIVERSALLY, FOR A REASON.  S1c-module together
    with S1a, S1b and S3 force E = I - rho_V(pi).  The record datum space at
    d = 3 carries the S_3 PERMUTATION module -- the chart symmetry permutes
    links, it does not mix them -- so I - rho_V(pi) always annihilates the
    all-ones link vector, while E is always invertible.  THE
    PERMUTATION-MODULE OBSTRUCTION.
  * THE p = 7 SPECTRAL MEETING IS REAL, AND IT IS MEASURED IN-ARENA.  At p = 7
    the order-3 wing symmetries normalise 6 subgroups of order 7 with
    conjugation exponents {2, 4} -- the primitive cube roots -- so the
    demanded eigenvalue 1 - s lies in {4, 6}; and HA's counts -> q spectrum at
    d = 3 contains 1/2 = 4 mod 7.  The two MEET.  R2-LCB's prediction is
    confirmed at the d = 3 pairing.  It buys a non-empty S1a+S1b census and
    nothing more: at the equivariant identifications the meeting happens at a
    STILLBORN cell, and where the cell survives the precheck the order
    obstruction still empties it.

Exact arithmetic only: integers, fractions.Fraction, exact F_p.  No float or
complex literal and no float()/complex() call appears in this source; the
scanner that measures it is validated by a synthetic injection it must flag.

MUTANT DISCIPLINE (RUNBOOK 14 addendum, v13 #208): every mutation is a
mutation of an INSTRUMENT helper.  No function that registers a gate
references mutant identity, a run-mode boolean or sys.argv; the AST guard
measures that and is validated by a synthetic sample it must flag.

Usage:
    python3.13 rsq_reposed_square_exact.py                  # delivery run
    python3.13 rsq_reposed_square_exact.py --mutant NAME    # must exit 1
    python3.13 rsq_reposed_square_exact.py --falsification-selftest
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import json
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
    "anchor-pin-sha":     "the RSQ pin's own hash pin is perturbed",
    "anchor-lcb-sha":     "the LCB receipt's hash pin is perturbed",
    "anchor-tb3-sha":     "the TB3 receipt's hash pin is perturbed",
    "anchor-ha-sha":      "the HA receipt's hash pin is perturbed",
    "anchor-brg-sha":     "the BRG paper's hash pin is perturbed",
    "anchor-psi-sha":     "the PSI receipt's hash pin is perturbed",
    "anchor-ladder":      "the rebuilt defect-subgroup ladder is perturbed",
    "anchor-rho":         "the exact-to-F_p reduction of rho is perturbed",
    "anchor-soft":        "anchor failures are made non-fatal",
    # --- discipline -------------------------------------------------------
    "freeze-lax":         "a candidate is evaluated before the declarations freeze",
    "float-lax":          "the exact-arithmetic scanner is blinded",
    "exempt-lax":         "the mutant-identity AST scanner is blinded",
    # --- item 1: HA at d = 3 ----------------------------------------------
    "arena3-lax":         "the d = 3 link set drops its diagonals",
    "readout3-lax":       "the d = 3 record<->metric readout is perturbed",
    "posdef-lax":         "the exact Sylvester admissibility test is blinded",
    "residual3-lax":      "the closed-form residual comparator is perturbed",
    "carrier3-lax":       "the reduced carrier's register shift is perturbed",
    "prime-single":       "the deformation prime sweep collapses to one prime",
    # --- item 2: the transport side ---------------------------------------
    "wing-lax":           "the wing symmetry acts by the wrong label map",
    "encoding-lax":       "the four-factor form replaces the commutator encoding",
    "ladder-lax":         "the defect-subgroup closure is truncated",
    "fixpoint-lax":       "fix(delta) is read off the wrong law",
    # --- item 3: the candidate family -------------------------------------
    "equi-lax":           "the equivariance test is skipped and the "
                          "identifications are typed",
    "cell-orbit-drop":    "the covariant family is truncated to the declared "
                          "identifications",
    "cell-drop":          "one covariant cell is dropped from the sweep",
    "censuscell-lax":     "the declared census-cell rule is replaced by an "
                          "arbitrary pick",
    # --- item 4: the stillborn precheck -----------------------------------
    "precheck-lax":       "the precheck admits every candidate",
    "precheck-blind":     "the precheck rejects every candidate",
    "stillborn-lax":      "the stillborn mismatch is typed rather than computed",
    "subsume-lax":        "the subsumption comparison is inverted",
    # --- item 5: the strengthened test ------------------------------------
    "criterion-lax":      "the order criterion is weakened to the fixed-space "
                          "test alone",
    "route-alias":        "route B reads route A's answer",
    "route-a-lax":        "route A's eigenvalue is perturbed",
    "route-b-lax":        "route B's covector enumeration is truncated",
    "literal-lax":        "the literal permutation verification is skipped",
    "census-lax":         "the census tally drops the trivial map",
    "module-lax":         "the permutation-module obstruction is asserted, "
                          "not measured",
    "module-blind":       "the module witness's action is replaced by a "
                          "permutation action",
    "found-block":        "the FOUND branch is blocked",
    "empty-block":        "the EMPTY branch is blocked",
    "witness-blank":      "the exhibited witness is blanked",
    "partition-lax":      "the declared verification partition is "
                          "contaminated by the fit cell",
    "teeth-off":          "the declared-to-fail extensions are made to pass",
    "break-blind":        "the negative-with-teeth is not rejected",
    "s2-lax":             "the carrier-rigidity clause is blinded",
    "s4-lax":             "the functoriality base change is dropped",
    # --- item 6: the prime section ----------------------------------------
    "threshold-lax":      "the scale threshold is typed rather than computed",
    "meeting-lax":        "the spectral meeting is asserted at every prime",
    # --- self-tests -------------------------------------------------------
    "selftest-lax":       "the S_3 self-test reads a memoised value",
    "selftest-select":    "the self-test's tested set is selected by the verdicts",
    "basis-lax":          "the declared GL_6 basis change is made trivial",
    "cache-lax":          "the self-test cache bypass is disabled",
    "cache-unused":       "the cache is never exercised before the self-tests",
    # --- the verdict ------------------------------------------------------
    "verdict-flip":       "the verdict derivation is flipped",
    "universal-lax":      "the coverage qualifier is asserted, not measured",
    "qualifier-typo":     "a computed qualifier is replaced by a typed string",
    "complete-lax":       "a table's cell-completeness check is blinded",
    # --- the readout-profile theorem and the two verdict halves -----------
    "profile-lax":        "the readout row profiles are typed rather than "
                          "measured",
    "theorem-lax":        "the readout-profile theorem's prime test is "
                          "asserted, not derived",
    "theorem-alias":      "the readout-profile theorem reaches the F_p order "
                          "criterion silently",
    "theorem-floor":      "the readout-profile theorem drops its declared "
                          "prime floor and admits a prime",
    "extension-lax":      "the exact all-prime extension of the sweep is "
                          "truncated",
    "motivated-lax":      "the motivated-identification census is typed "
                          "rather than computed",
    "ident-flip":         "the identification qualifier is flipped",
    "emptiness-flip":     "the emptiness qualifier is flipped back to the "
                          "census-scoped name",
    "master-lax":         "the master equation is asserted, not verified",
    "independence-lax":   "the module obstruction's independence is asserted",
    "sufficiency-lax":    "the sufficiency census is truncated to one pattern",
    "spectral-lax":       "the eigenvalue-1 multiplicity is asserted",
    "baseindep-lax":      "the base-independence fingerprint is typed",
    "negcontrol-lax":     "the precheck's independent negative control is "
                          "replaced by the object under audit",
    "route-silent-alias": "route B returns route A's answer without recording "
                          "it",
    "crit-row-drop":      "one row is dropped from the order-criterion sweep",
    "census-row-drop":    "one row is dropped from the census table",
    "module-row-drop":    "one row is dropped from the permutation-module "
                          "table",
    "wide-drop":          "a prime is dropped from the wide corroboration "
                          "census",
}

_M_PIN_SHA     = (MUTANT == "anchor-pin-sha")
_M_LCB_SHA     = (MUTANT == "anchor-lcb-sha")
_M_TB3_SHA     = (MUTANT == "anchor-tb3-sha")
_M_HA_SHA      = (MUTANT == "anchor-ha-sha")
_M_BRG_SHA     = (MUTANT == "anchor-brg-sha")
_M_PSI_SHA     = (MUTANT == "anchor-psi-sha")
_M_LADDER_A    = (MUTANT == "anchor-ladder")
_M_RHO         = (MUTANT == "anchor-rho")
_M_SOFT        = (MUTANT == "anchor-soft")
_M_FREEZE      = (MUTANT == "freeze-lax")
_M_FLOAT       = (MUTANT == "float-lax")
_M_EXEMPT      = (MUTANT == "exempt-lax")
_M_ARENA3      = (MUTANT == "arena3-lax")
_M_READOUT3    = (MUTANT == "readout3-lax")
_M_POSDEF      = (MUTANT == "posdef-lax")
_M_RESIDUAL3   = (MUTANT == "residual3-lax")
_M_CARRIER3    = (MUTANT == "carrier3-lax")
_M_PRIMESINGLE = (MUTANT == "prime-single")
_M_WING        = (MUTANT == "wing-lax")
_M_ENCODING    = (MUTANT == "encoding-lax")
_M_LADDER      = (MUTANT == "ladder-lax")
_M_FIXPOINT    = (MUTANT == "fixpoint-lax")
_M_EQUI        = (MUTANT == "equi-lax")
_M_ORBITDROP   = (MUTANT == "cell-orbit-drop")
_M_CELLDROP    = (MUTANT == "cell-drop")
_M_CENSUSCELL  = (MUTANT == "censuscell-lax")
_M_PRECHECK    = (MUTANT == "precheck-lax")
_M_PREBLIND    = (MUTANT == "precheck-blind")
_M_STILLBORN   = (MUTANT == "stillborn-lax")
_M_SUBSUME     = (MUTANT == "subsume-lax")
_M_CRITERION   = (MUTANT == "criterion-lax")
_M_ROUTEALIAS  = (MUTANT == "route-alias")
_M_ROUTEA      = (MUTANT == "route-a-lax")
_M_ROUTEB      = (MUTANT == "route-b-lax")
_M_LITERAL     = (MUTANT == "literal-lax")
_M_CENSUS      = (MUTANT == "census-lax")
_M_MODULE      = (MUTANT == "module-lax")
_M_MODBLIND    = (MUTANT == "module-blind")
_M_FOUNDBLOCK  = (MUTANT == "found-block")
_M_EMPTYBLOCK  = (MUTANT == "empty-block")
_M_WITNESS     = (MUTANT == "witness-blank")
_M_PARTITION     = (MUTANT == "partition-lax")
_M_TEETH       = (MUTANT == "teeth-off")
_M_BREAK       = (MUTANT == "break-blind")
_M_S2          = (MUTANT == "s2-lax")
_M_S4          = (MUTANT == "s4-lax")
_M_THRESHOLD   = (MUTANT == "threshold-lax")
_M_MEETING     = (MUTANT == "meeting-lax")
_M_SELFTEST    = (MUTANT == "selftest-lax")
_M_SELFSELECT  = (MUTANT == "selftest-select")
_M_BASIS       = (MUTANT == "basis-lax")
_M_CACHE       = (MUTANT == "cache-lax")
_M_CACHEUNUSED = (MUTANT == "cache-unused")
_M_VERDICT     = (MUTANT == "verdict-flip")
_M_UNIVERSAL   = (MUTANT == "universal-lax")
_M_QUALTYPO    = (MUTANT == "qualifier-typo")
_M_COMPLETE    = (MUTANT == "complete-lax")
_M_PROFILE     = (MUTANT == "profile-lax")
_M_THEOREM     = (MUTANT == "theorem-lax")
_M_THMALIAS    = (MUTANT == "theorem-alias")
_M_THMFLOOR    = (MUTANT == "theorem-floor")
_M_EXTENSION   = (MUTANT == "extension-lax")
_M_MOTIVATED   = (MUTANT == "motivated-lax")
_M_IDENT       = (MUTANT == "ident-flip")
_M_EMPTFLIP    = (MUTANT == "emptiness-flip")
_M_MASTER      = (MUTANT == "master-lax")
_M_INDEP       = (MUTANT == "independence-lax")
_M_SUFFICIENCY = (MUTANT == "sufficiency-lax")
_M_SPECTRAL    = (MUTANT == "spectral-lax")
_M_BASEINDEP   = (MUTANT == "baseindep-lax")
_M_NEGCONTROL  = (MUTANT == "negcontrol-lax")
_M_SILENT      = (MUTANT == "route-silent-alias")
_M_CRITROW     = (MUTANT == "crit-row-drop")
_M_CENSUSROW   = (MUTANT == "census-row-drop")
_M_MODROW      = (MUTANT == "module-row-drop")
_M_WIDEDROP    = (MUTANT == "wide-drop")

DELIVERY_RUN = (MUTANT is None)
WRITE_ARTIFACTS = (DELIVERY_RUN and not SELFTEST_ONLY)

# --------------------------------------------------------------------------
# 1.  RECEIPT SCAFFOLD
# --------------------------------------------------------------------------

ANCHORS: list[dict] = []
GATES: list[dict] = []
DISCLOSURES: list[dict] = []
_GATE_IDS: set[str] = set()
CANDIDATE_EVALS = [0]
ANCHOR_POLICY = {"failures": 0, "fatal": 0}
OUT: list[str] = []
CACHE_STATS = {"lookups": 0, "hits": 0, "misses": 0, "bypasses": 0,
               "selftest_hits": 0}
_DELTA_MEMO: dict = {}
ROUTE_CALLS = {"A": 0, "B": 0, "taint": 0}


def anchor_policy_fatal(failures: int) -> bool:
    """THE ANCHOR POLICY IS FAIL-CLOSED: any anchor failure kills the run.  The
    run is nevertheless carried through to the totals block so that every
    falsifier is scored at a gate and against the same denominators as the
    honest run.  [instrument -- mutable]"""
    if _M_SOFT:
        return False
    return failures > 0


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
    sys.stderr.write(f"[rsq] {s}\n")
    sys.stderr.flush()


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for blk in iter(lambda: fh.read(65536), b""):
            h.update(blk)
    return h.hexdigest()


def note_candidate() -> None:
    CANDIDATE_EVALS[0] += 1


# --------------------------------------------------------------------------
# 2.  THE DECLARATIONS -- frozen before any candidate is evaluated
# --------------------------------------------------------------------------

DECL: dict = {
    "arena": {
        "boundary":
            "one PAIRING at THREE WINGS.  Deformation side: HA rebuilt at "
            "d = 3 -- X = (Z_3)^3 (27 sites), 6 links (the 3 axes and the 3 "
            "positive diagonals), the record datum space V = F_p^6 (the six "
            "link counts at a site), HA's record<->metric readout E, and the "
            "arena C_HA(p) = F_p^k x F_p^3 with 3-DIMENSIONAL fronts.  "
            "Transport side: TB3's three-wing base -- the 8 system-triple "
            "labels F_2^3, the completion group G_C of permutations fixing "
            "label 0, the wing symmetry group S_3 acting by bit permutation, "
            "and the three-wing commutator encoding "
            "delta_pi(Q) = Sigma_pi Q^-1 Sigma_pi^-1 Q (TB3's F_3).",
        "family":
            "THE CANDIDATE-SQUARE FAMILY, declared as data: (i) the "
            "S_3-EQUIVARIANT identifications of the six metric slots with the "
            "six links -- their number is COMPUTED by an exhaustive "
            "equivariance test over all 6! slot orders and never typed -- x 2 "
            "directions, the MODULE cells; (ii) the whole COVARIANT ORBIT of "
            "the slot-relabelling group, 6! slot orders x 2 directions, the "
            "SET-LEVEL cells; (iii) the declared census cells, chosen by a "
            "rule stated before any fixture truth; (iv) 7 declared primes; "
            "(v) the 6 wing symmetries of S_3; (vi) two arena scales -- the "
            "NATIVE 8-label three-wing arena and the GROWN family "
            "L_m = {0} + (F_2^3 minus 0) x {1..m}; (vii) the dimensions "
            "d = 2,3,4,5 at the fixed-space and criterion sweeps",
        "law":
            "BRG's S1-S6 as its terminal paper section 2.6 registers them, "
            "with S1c generalised per R2-LCB's F-10 from the two-wing Z/2 "
            "SIGN condition to the F_p[S_3] MODULE condition; a candidate "
            "morphism is a map alpha : V -> G_C",
        "state":
            "the deformation side's declared base geometry record G3-FLAT = "
            "(1,1,1,2,2,2) (HA's own declared d = 3 record); the transport "
            "side's declared base completions -- TB3's own five ord-target "
            "completions; the detector site x* = (0,0,0)",
        "arena action":
            "the metric-slot relabelling group S_6 (whose orbit on the "
            "declared identifications IS the covariant cell family); the "
            "DIRECTION sweep; the choice of wing symmetry inside S_3; the "
            "prime sweep; change of basis of V by a declared element of "
            "GL_6(F_p); the arena scale.  These six are THIS UNIT'S OWN "
            "declared choices and the ones the verdict must be invariant "
            "under; the three-wing 8-label arena is INHERITED from TB3, and "
            "its effect is not tested by re-declaration but reported "
            "separately at both scales",
        "provenance":
            "TB3, LCB, HA, BRG, PSI -- all terminal; papers and receipts "
            "hash-pinned, every reused number read from them and recomputed "
            "here",
        "admission":
            "a candidate is ACCEPTED only if every clause of S1 holds and S2, "
            "S3 hold.  A candidate is STILLBORN if the precheck's "
            "fixed-point-compatibility test fails, and then no census is run "
            "for it and the mismatch is recorded",
    },
    "d": 3,
    "L": 3,
    "wings": 3,
    "records_d3": {"G3-FLAT": (1, 1, 1, 2, 2, 2),
                   "G3-ANISO": (1, 4, 9, 5, 10, 13),
                   "G3-OFF": (2, 2, 2, 6, 4, 4)},
    "negative_records_d3": {"G3-SINGULAR": (1, 1, 1, 4, 2, 2),
                            "G3-INDEF": (1, 1, 1, 6, 2, 2)},
    "primes": [5, 7, 11, 13, 17, 19, 23],
    "wide_corroboration_prime_ceiling": 293,
    "carrier_build_primes": [5, 7, 11],
    "dimension_sweep": [2, 3, 4, 5],
    "detector_site": (0, 0, 0),
    "drag_rule": "A-axis",
    "ladder_completions": {
        "ord1": (0, 1, 2, 3, 4, 5, 6, 7),
        "ord2": (0, 1, 2, 3, 5, 4, 7, 6),
        "ord3": (0, 1, 2, 3, 4, 5, 7, 6),
        "ord6": (0, 1, 3, 2, 5, 4, 7, 6),
        "reference": (0, 3, 2, 1, 4, 5, 6, 7),
    },
    "verification_partition": {
        "partition rule": "FIT = the single declared basis record e_1 = "
                          "(1,0,0,0,0,0); COMPLEMENT = every other element of "
                          "V; sizes computed.  NOTHING IS FITTED: the "
                          "candidate is built from the declared exponents "
                          "before any record cell is read, so this is a "
                          "partition of the record space and not an "
                          "estimation",
        "H1": "the square at every cell of the complement, as permutations",
        "H2": "the defect permutation entry by entry -- the SAME boolean as "
              "H1, since a tuple equality IS the entry-by-entry comparison; "
              "reported once and disclosed",
        "H3": "the fixed-label count of delta_pi(alpha(r)) at every cell of "
              "the complement, and the distinct values it takes",
        "teeth": "X-NOSQUARE (predict delta_pi(alpha(r)) = alpha(r)) and "
                 "X-FLATFIX (predict the identity stratum everywhere), both "
                 "declared IN ADVANCE to fail",
    },
    "growth_family": "L_m = {0} + (F_2^3 minus 0) x {1..m}: m copies of TB3's "
                     "seven moved labels, with S_3 acting on the F_2^3 factor "
                     "alone and fixing label 0.  m = 1 is TB3's native arena.",
}

# --------------------------------------------------------------------------
# 3.  EXACT ARITHMETIC -- Q and F_p.  No float appears anywhere.
# --------------------------------------------------------------------------


def mat_sub_scalar(M, lam, n):
    return [[M[i][j] - (lam if i == j else Fr(0)) for j in range(n)]
            for i in range(n)]


def det_exact(M):
    n = len(M)
    A = [row[:] for row in M]
    dv = Fr(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if A[r][c] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            dv = -dv
        dv *= A[c][c]
        pv = A[c][c]
        A[c] = [v / pv for v in A[c]]
        for r in range(c + 1, n):
            if A[r][c] != 0:
                f = A[r][c]
                A[r] = [a - f * b for a, b in zip(A[r], A[c])]
    return dv


def solve_exact(A, b):
    n = len(A)
    M = [[Fr(A[i][j]) for j in range(n)] + [Fr(b[i])] for i in range(n)]
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        if piv is None:
            return None
        M[c], M[piv] = M[piv], M[c]
        pv = M[c][c]
        M[c] = [v / pv for v in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [a - f * bb for a, bb in zip(M[r], M[c])]
    return [M[i][n] for i in range(n)]


def inv_exact(M):
    n = len(M)
    cols = []
    for k in range(n):
        e = [Fr(1) if i == k else Fr(0) for i in range(n)]
        s = solve_exact(M, e)
        if s is None:
            return None
        cols.append(s)
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def positive_definite(M) -> bool:
    """Exact Sylvester criterion.  [instrument -- mutable]"""
    if _M_POSDEF:
        return True
    for k in range(1, len(M) + 1):
        if det_exact([row[:k] for row in M[:k]]) <= 0:
            return False
    return True


def to_fp_frac(v: Fr, p: int):
    """Exact reduction Q -> F_p.  [instrument -- mutable]"""
    den = v.denominator % p
    if den == 0:
        return None
    r = (v.numerator % p) * pow(den, -1, p) % p
    return (r * r) % p if _M_RHO else r


def mat_to_fp(M, p):
    return [[(x.numerator % p) * pow(x.denominator % p, -1, p) % p for x in row]
            for row in M]


def mat_mul_fp(A, B, p):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) % p for j in range(n)]
            for i in range(n)]


def mat_sub_fp(A, B, p):
    n = len(A)
    return [[(A[i][j] - B[i][j]) % p for j in range(n)] for i in range(n)]


def eye_fp(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def scal_fp(c, n, p):
    return [[c % p if i == j else 0 for j in range(n)] for i in range(n)]


def transpose(M):
    return [list(r) for r in zip(*M)]


def kernel_dim_fp(A, p):
    """dim ker A over F_p by Gaussian elimination.  Route A's own primitive."""
    n = len(A)
    B = [row[:] for row in A]
    rank = 0
    row = 0
    for c in range(n):
        piv = next((r for r in range(row, n) if B[r][c] % p), None)
        if piv is None:
            continue
        B[row], B[piv] = B[piv], B[row]
        f = pow(B[row][c], -1, p)
        B[row] = [x * f % p for x in B[row]]
        for r in range(n):
            if r != row and B[r][c] % p:
                g = B[r][c]
                B[r] = [(B[r][k] - g * B[row][k]) % p for k in range(n)]
        row += 1
        rank += 1
    return n - rank


def kernel_basis_fp(A, p):
    n = len(A)
    B = [row[:] for row in A]
    piv_col = []
    row = 0
    for c in range(n):
        piv = next((r for r in range(row, n) if B[r][c] % p), None)
        if piv is None:
            continue
        B[row], B[piv] = B[piv], B[row]
        f = pow(B[row][c], -1, p)
        B[row] = [x * f % p for x in B[row]]
        for r in range(n):
            if r != row and B[r][c] % p:
                g = B[r][c]
                B[r] = [(B[r][k] - g * B[row][k]) % p for k in range(n)]
        piv_col.append(c)
        row += 1
    free = [c for c in range(n) if c not in piv_col]
    basis = []
    for fc in free:
        v = [0] * n
        v[fc] = 1
        for i, c in enumerate(piv_col):
            v[c] = (-B[i][fc]) % p
        basis.append(v)
    return basis


def mat_pow_fp(A, e, p):
    n = len(A)
    R = eye_fp(n)
    for _ in range(e):
        R = mat_mul_fp(R, A, p)
    return R


def legendre_exponent(n: int, p: int) -> int:
    """The exponent of p in n! -- computed, never typed."""
    e, q = 0, p
    while q <= n:
        e += n // q
        q *= p
    return e


# --------------------------------------------------------------------------
# 4.  PERMUTATIONS
# --------------------------------------------------------------------------


def pident(n):
    return tuple(range(n))


def pcomp(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def pinv(a):
    o = [0] * len(a)
    for i, v in enumerate(a):
        o[v] = i
    return tuple(o)


def pord(a):
    e = pident(len(a))
    x, o = a, 1
    while x != e:
        x = pcomp(x, a)
        o += 1
    return o


def pfix(a):
    return sum(1 for i in range(len(a)) if a[i] == i)


def group_closure(gens, n, cap=200000):
    e = pident(n)
    G = {e}
    frontier = [e]
    while frontier:
        x = frontier.pop()
        for g in gens:
            y = pcomp(x, g)
            if y not in G:
                G.add(y)
                frontier.append(y)
                if len(G) > cap:
                    return G
    return G


# --------------------------------------------------------------------------
# 5.  THE DEFORMATION SIDE -- HA REBUILT AT d = 3
# --------------------------------------------------------------------------

D3 = DECL["d"]
L3 = DECL["L"]


def link_set(d: int):
    """HA's own declared link set: the d axis links and the C(d,2) positive
    diagonals.  [instrument -- mutable]"""
    axes = [tuple(1 if k == j else 0 for k in range(d)) for j in range(d)]
    diags = [tuple(1 if k in (i, j) else 0 for k in range(d))
             for i in range(d) for j in range(i + 1, d)]
    if _M_ARENA3 and d == 3:
        return axes + diags[:-1] + [axes[0]]
    return axes + diags


def sites(d: int, L: int):
    return [tuple(t) for t in itertools.product(range(L), repeat=d)]


def add_site(x, e, L):
    return tuple((a + b) % L for a, b in zip(x, e))


def sym_index(d: int):
    return [(i, j) for i in range(d) for j in range(i, d)]


def metric_slots(d: int):
    """The d(d+1)/2 metric slots in the NATURAL order: the d diagonal slots,
    then the C(d,2) off-diagonal ones."""
    return [(i, i) for i in range(d)] + \
           [(i, j) for i in range(d) for j in range(i + 1, d)]


def ha_readout_matrix(d: int):
    """The matrix HA's own G28 measures, in HA's own row and column order
    (rows = the links SORTED, columns = sym_index(d)).  [instrument --
    mutable]"""
    idx = sym_index(d)
    lks = sorted(link_set(d))
    M = [[Fr(lk[i] * lk[j] * (1 if i == j else 2)) for (i, j) in idx]
         for lk in lks]
    if _M_READOUT3:
        M[0][d - 1] = M[0][d - 1] + Fr(1)
    return M


def q_from_counts(d, counts):
    idx = sym_index(d)
    rows, rhs = [], []
    for lk in sorted(counts):
        rows.append([Fr(lk[i] * lk[j] * (1 if i == j else 2)) for (i, j) in idx])
        rhs.append(Fr(counts[lk]))
    sol = solve_exact(rows, rhs)
    if sol is None:
        return None
    q = [[Fr(0)] * d for _ in range(d)]
    for (i, j), v in zip(idx, sol):
        q[i][j] = v
        q[j][i] = v
    return q


class GeomRecord3:
    """HA's geometry record at d = 3, with its metric candidate read off by
    HA's own declared readout."""

    def __init__(self, name, tup):
        self.name = name
        self.d, self.L = D3, L3
        self.links = link_set(D3)
        self.S = sites(D3, L3)
        self.counts = {x: {lk: int(tup[i]) for i, lk in enumerate(self.links)}
                       for x in self.S}
        self.q = {x: q_from_counts(D3, self.counts[x]) for x in self.S}
        self.nonsingular = all(v is not None for v in self.q.values())
        self.admissible = self.nonsingular and \
            all(positive_definite(self.q[x]) for x in self.S)
        self.I = {x: (inv_exact(self.q[x]) if self.q[x] is not None else None)
                  for x in self.S}


def lambda_axis(rec, x):
    """HA's declared `A-axis` drag weight: Lambda = diag(1/n_{e_j}), link-local
    in the axis interval counts."""
    cnt = rec.counts[x]
    M = [[Fr(0)] * rec.d for _ in range(rec.d)]
    for j in range(rec.d):
        M[j][j] = Fr(1, cnt[rec.links[j]])
    return M


def omega_axis(N, M, rec):
    """omega_j(x) = N(x) M(x+e_j) - M(x) N(x+e_j)."""
    return {x: tuple(Fr(N[x] * M[add_site(x, e, rec.L)] -
                        M[x] * N[add_site(x, e, rec.L)])
                     for e in rec.links[:rec.d]) for x in rec.S}


def beta_field(rec, N, M):
    om = omega_axis(N, M, rec)
    out = {}
    for x in rec.S:
        Iv = rec.I[x]
        out[x] = tuple(sum((Iv[i][j] * om[x][j] for j in range(rec.d)), Fr(0))
                       for i in range(rec.d))
    return out


def drag_at(rec, N, n, x):
    Lam = lambda_axis(rec, x)
    dn = [Fr(n[add_site(x, e, rec.L)] - n[x]) for e in rec.links[:rec.d]]
    return tuple(sum((Lam[i][j] * dn[j] for j in range(rec.d)), Fr(0)) * Fr(N[x])
                 for i in range(rec.d))


def residual_closed(rec, N, M):
    """The CLOSED-FORM comparator: rho^i = (Lambda^{ij} - I^{ij}) omega_j.
    It never routes through the literal five-map composition.
    [instrument -- mutable]"""
    b = beta_field(rec, N, M)
    om = omega_axis(N, M, rec)
    out = {}
    for x in rec.S:
        Lam = lambda_axis(rec, x)
        if _M_RESIDUAL3:
            Lam = [[Lam[i][j] + Fr(1) for j in range(rec.d)] for i in range(rec.d)]
        out[x] = tuple(sum((Lam[i][j] * om[x][j] for j in range(rec.d)), Fr(0))
                       - b[x][i] for i in range(rec.d))
    return out


class Hmap3:
    """H_a[N](n, m) = (n + N, m + w[N,n]) at d = 3, a bijection of total
    records; the second normal step is transported along the first."""

    def __init__(self, rec, N):
        self.rec, self.N = rec, N

    def _w(self, n):
        return {x: drag_at(self.rec, self.N, n, x) for x in self.rec.S}

    def fwd(self, c):
        n, m = c
        w = self._w(n)
        return ({x: n[x] + self.N[x] for x in n},
                {x: tuple(m[x][i] + w[x][i] for i in range(self.rec.d))
                 for x in m})

    def inv(self, c):
        n, m = c
        n2 = {x: n[x] - self.N[x] for x in n}
        w = self._w(n2)
        return (n2, {x: tuple(m[x][i] - w[x][i] for i in range(self.rec.d))
                     for x in m})


class Dmap3:
    def __init__(self, rec, v):
        self.rec, self.v = rec, v

    def fwd(self, c):
        n, m = c
        return (n, {x: tuple(m[x][i] + self.v[x][i] for i in range(self.rec.d))
                    for x in m})


def residual_literal(rec, N, M, n0):
    """R_HH := H[N] H[M] H[N]^-1 H[M]^-1 D[-beta], applied LITERALLY as the
    five-map composition on exact rational fields."""
    HN, HM = Hmap3(rec, N), Hmap3(rec, M)
    b = beta_field(rec, N, M)
    Dm = Dmap3(rec, {x: tuple(-b[x][i] for i in range(rec.d)) for x in b})
    c = (dict(n0), {x: tuple(Fr(0) for _ in range(rec.d)) for x in rec.S})
    for f in (Dm.fwd, HM.inv, HN.inv, HM.fwd, HN.fwd):
        c = f(c)
    n1, m1 = c
    if any(n1[x] != n0[x] for x in n0):
        return None
    return dict(m1)


class ReducedCarrier3:
    """C_red = F x A at d = 3: F = the front sector n0 + span_{F_p}{lapses in
    play} (the 3-DIMENSIONAL fronts), A = (F_p)^3, the address register at the
    declared detector site."""

    def __init__(self, rec, p, n0, lapses, xstar):
        self.rec, self.p, self.n0, self.xstar = rec, p, n0, xstar
        S = rec.S
        self.S = S
        basis = []
        for N in lapses:
            if self._rank(basis + [N]) > self._rank(basis):
                basis.append(N)
        self.basis, self.k = basis, len(basis)
        self.fronts = []
        for co in itertools.product(range(p), repeat=self.k):
            self.fronts.append({x: (n0[x] + sum(co[i] * basis[i][x]
                                                for i in range(self.k))) % p
                                for x in S})
        self.front_index = {tuple(sorted(f.items())): i
                            for i, f in enumerate(self.fronts)}
        self.regs = list(itertools.product(range(p), repeat=rec.d))
        self.reg_index = {r: i for i, r in enumerate(self.regs)}
        self.size = len(self.fronts) * len(self.regs)

    def _rank(self, vs):
        p = self.p
        rows = [[v[x] % p for x in self.S] for v in vs]
        r = 0
        for c in range(len(self.S)):
            piv = next((i for i in range(r, len(rows)) if rows[i][c] % p), None)
            if piv is None:
                continue
            rows[r], rows[piv] = rows[piv], rows[r]
            iv = pow(rows[r][c], -1, p)
            rows[r] = [(v * iv) % p for v in rows[r]]
            for i in range(len(rows)):
                if i != r and rows[i][c] % p:
                    f = rows[i][c]
                    rows[i] = [(a - f * b) % p for a, b in zip(rows[i], rows[r])]
            r += 1
        return r

    def code(self, fi, reg):
        return fi * len(self.regs) + self.reg_index[reg]

    def perm_H(self, N):
        p, d = self.p, self.rec.d
        out = [0] * self.size
        nreg = len(self.regs)
        for fi, f in enumerate(self.fronts):
            w = drag_at(self.rec, N, f, self.xstar)
            wp = [to_fp_frac(w[i], p) for i in range(d)]
            if any(t is None for t in wp):
                return None
            key = tuple(sorted({x: (f[x] + N[x]) % p for x in f}.items()))
            if key not in self.front_index:
                return None
            fj = self.front_index[key]
            for ri, reg in enumerate(self.regs):
                out[fi * nreg + ri] = self.code(
                    fj, tuple((reg[i] + wp[i]) % p for i in range(d)))
        return tuple(out)

    def perm_D(self, v):
        p, d = self.p, self.rec.d
        vp = [to_fp_frac(v[self.xstar][i], p) for i in range(d)]
        if any(t is None for t in vp):
            return None
        out = [0] * self.size
        nreg = len(self.regs)
        for fi in range(len(self.fronts)):
            for ri, reg in enumerate(self.regs):
                out[fi * nreg + ri] = self.code(
                    fi, tuple((reg[i] + vp[i]) % p for i in range(d)))
        return tuple(out)


def register_shift_of(RC, R, rho_p):
    """Is R exactly the translation of the address register by rho mod p, with
    the front sector returning to itself?  Measured configuration by
    configuration.  [instrument -- mutable]"""
    d = RC.rec.d
    shift = rho_p
    if _M_CARRIER3:
        shift = tuple((v + 1) % RC.p for v in rho_p)
    for fi in range(len(RC.fronts)):
        for reg in RC.regs:
            if R[RC.code(fi, reg)] != RC.code(
                    fi, tuple((reg[i] + shift[i]) % RC.p for i in range(d))):
                return False
    return True


def sweep_primes():
    """The declared prime sweep.  [instrument -- mutable]"""
    if _M_PRIMESINGLE:
        return DECL["primes"][:1]
    return list(DECL["primes"])


def carrier_primes():
    """The primes at which the reduced carrier is BUILT as permutations (the
    carrier has p^(k+3) configurations; the cap is declared).  [instrument --
    mutable]"""
    if _M_PRIMESINGLE:
        return DECL["carrier_build_primes"][:1]
    return list(DECL["carrier_build_primes"])


# --------------------------------------------------------------------------
# 6.  THE TRANSPORT SIDE -- TB3'S THREE WINGS
# --------------------------------------------------------------------------

NLAB = 8
S3_ELEMS = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]


def sigma_labels(pi):
    """The wing symmetry as a permutation of the 8 system-triple labels: a
    label is a triple of wing bits, and pi permutes the wings.
    [instrument -- mutable]"""
    out = [0] * NLAB
    for a in range(NLAB):
        bits = [(a >> 2) & 1, (a >> 1) & 1, a & 1]
        nb = [0, 0, 0]
        for i in range(3):
            nb[pi[i]] = bits[i]
        out[a] = (nb[0] << 2) | (nb[1] << 1) | nb[2]
    if _M_WING:
        out = list(out[1:]) + [out[0]]
    return tuple(out)


SIGMA = {pi: sigma_labels(pi) for pi in S3_ELEMS}


def delta_pi(pi, Q, fresh: bool = False, selftest: bool = False):
    """The THREE-WING COMMUTATOR ENCODING -- TB3's F_3:
           delta_pi(Q) = Sigma_pi Q^-1 Sigma_pi^-1 Q  =  [Sigma_pi^-1, Q].
    At two wings, where Sigma is an involution, this is GEN's own
    delta(Q) = Sigma Q^T Sigma Q verbatim.  [instrument -- mutable cache
    path]"""
    key = (pi, Q)
    use_cache = (not fresh) or _M_CACHE
    if fresh and not _M_CACHE:
        CACHE_STATS["bypasses"] += 1
    if use_cache:
        CACHE_STATS["lookups"] += 1
        if key in _DELTA_MEMO:
            CACHE_STATS["hits"] += 1
            if selftest:
                CACHE_STATS["selftest_hits"] += 1
            return _DELTA_MEMO[key]
        CACHE_STATS["misses"] += 1
    s = SIGMA[pi]
    if _M_ENCODING:
        val = pcomp(s, pcomp(pinv(Q), pcomp(s, Q)))       # the four-factor F_1
    else:
        val = pcomp(s, pcomp(pinv(Q), pcomp(pinv(s), Q)))
    if use_cache:
        _DELTA_MEMO[key] = val
    return val


def form_F1(pi, Q):
    s = SIGMA[pi]
    return pcomp(s, pcomp(pinv(Q), pcomp(s, Q)))


def form_F2(pi, Q):
    s = SIGMA[pi]
    return pcomp(pinv(s), pcomp(pinv(Q), pcomp(s, Q)))


def form_F3(pi, Q):
    s = SIGMA[pi]
    return pcomp(s, pcomp(pinv(Q), pcomp(pinv(s), Q)))


def completion_group():
    """G_C = the permutations of the 8 system-triple labels FIXING label 0.
    The size is computed by enumeration and independently as a factorial."""
    return [(0,) + q for q in itertools.permutations(range(1, NLAB))]


def delta_fixed_points(members, pi):
    """{Q : delta_pi(Q) = Q}, swept member by member.  [instrument --
    mutable]"""
    if _M_FIXPOINT:
        return [Q for Q in members if delta_pi(pi, Q) == pident(NLAB)]
    return [Q for Q in members if delta_pi(pi, Q) == Q]


def ladder_defect_subgroup(Q):
    """K = < delta_pi(Q) : pi in S_3 >, the defect subgroup's system image --
    TB3's ladder, rebuilt here as a permutation group on the 8 labels.
    [instrument -- mutable]"""
    gens = [delta_pi(pi, Q) for pi in S3_ELEMS]
    if _M_LADDER:
        gens = gens[:1]
    return group_closure(gens, NLAB, cap=6000)

# --------------------------------------------------------------------------
# 7.  THE ENCODING LAYER AND THE CANDIDATE-SQUARE FAMILY
# --------------------------------------------------------------------------

SLOTS3 = metric_slots(D3)
LINKS3 = link_set(D3)
NV = len(SLOTS3)


def s3_link_perm(pi):
    """The S_3-action on the record datum space: pi permutes the chart axes,
    hence PERMUTES the six links.  Returned as the index map."""
    lks = link_set(D3)
    out = []
    for lk in lks:
        new = [0] * D3
        for i in range(D3):
            if lk[i]:
                new[pi[i]] = 1
        if tuple(new) not in lks:
            return None          # a link set the chart symmetry does not
        out.append(lks.index(tuple(new)))   # permute is a STRUCTURAL failure,
    return out                              # recorded and scored at the gates


def s3_slot_perm(pi):
    """The same group acting on the six metric slots."""
    out = []
    for (i, j) in SLOTS3:
        a, b = sorted((pi[i], pi[j]))
        out.append(SLOTS3.index((a, b)))
    return out


def rho_V(pi):
    """rho_V(pi) as a MATRIX on the record datum space: a permutation matrix,
    because the chart symmetry permutes links and does not mix them."""
    lp = s3_link_perm(pi)
    if lp is None:
        return None
    M = [[0] * NV for _ in range(NV)]
    for k in range(NV):
        M[lp[k]][k] = 1
    return M


def slot_orders():
    """The COVARIANT identification family: every ordering of the six metric
    slots, i.e. the whole orbit of the declared identification under the
    slot-relabelling group.  The count is computed, never typed.
    [instrument -- mutable]"""
    allp = [tuple(t) for t in itertools.permutations(range(NV))]
    if _M_ORBITDROP:
        return [tuple(range(NV))]
    if _M_CELLDROP:
        return allp[:-1]
    return allp


def equivariant_identifications():
    """The S_3-EQUIVARIANT identifications, found by an EXHAUSTIVE test over
    every slot order: perm is equivariant iff the slot action and the link
    action agree through it at every group element.  [instrument -- mutable]"""
    if _M_EQUI:
        return [tuple(range(NV))]
    out = []
    for perm in itertools.permutations(range(NV)):
        ok = True
        for pi in S3_ELEMS:
            lp, sp = s3_link_perm(pi), s3_slot_perm(pi)
            if lp is None:
                ok = False
                break
            for k in range(NV):
                if sp[perm[k]] != perm[lp[k]]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(tuple(perm))
    return out


_ENC_MEMO: dict = {}


def encoding_matrix(perm, direction):
    """HA's record<->metric readout at d = 3, read as an ENDOMORPHISM of the one
    datum space under the given identification (the k-th link is identified
    with the perm[k]-th metric slot) and in the declared direction.
    [instrument -- mutable]"""
    key = (tuple(perm), direction)
    if key in _ENC_MEMO:
        return _ENC_MEMO[key]
    morder = [SLOTS3[i] for i in perm]
    A = [[Fr(lk[i] * lk[j] * (1 if i == j else 2)) for (i, j) in morder]
         for lk in LINKS3]
    if _M_READOUT3:
        A[0][NV - 1] = A[0][NV - 1] + Fr(1)
    val = A if direction == "q->counts" else inv_exact(A)
    _ENC_MEMO[key] = val
    return val


def general_d_readout(d, ordering):
    """HA's readout at general d (HA section 9), q -> counts, in the NATURAL
    order (each link against the slot it determines) or the LEX order
    (sym_index)."""
    diag = [(i, i) for i in range(d)]
    off = [(i, j) for i in range(d) for j in range(i + 1, d)]
    lks = [tuple(1 if k == i else 0 for k in range(d)) for i in range(d)] + \
          [tuple(1 if k in (i, j) else 0 for k in range(d)) for (i, j) in off]
    morder = (diag + off) if ordering == "natural" else sym_index(d)
    return [[Fr(lk[i] * lk[j] * (1 if i == j else 2)) for (i, j) in morder]
            for lk in lks]


def dimension_sweep():
    """[instrument -- mutable]"""
    if _M_PRIMESINGLE:
        return [3]
    return list(DECL["dimension_sweep"])


# --------------------------------------------------------------------------
# 8.  THE STILLBORN PRECHECK -- structural, FIRST, per candidate
# --------------------------------------------------------------------------


def fix_space_dim(E, p):
    """dim ker(E - I) over F_p: the deformation side's fixed-space structure."""
    Ep = mat_to_fp(E, p)
    return kernel_dim_fp(mat_sub_fp(Ep, eye_fp(NV), p), p)


def precheck(fix_delta_size: int, fix_E_dim: int, p: int):
    """THE STILLBORN PRECHECK.  The commuting square forces
    alpha(fix E) contained in fix delta.  With injectivity (S3) that needs
    |fix E| <= |fix delta|.  fix delta is measured to have exactly ONE element,
    so the precheck passes exactly when dim ker(E - I) = 0.  Returns
    (passed, |fix E|, |fix delta|).  [instrument -- mutable]"""
    note_candidate()
    size_fix_E = p ** fix_E_dim
    if _M_PRECHECK:
        return True, size_fix_E, fix_delta_size
    if _M_PREBLIND:
        return False, size_fix_E, fix_delta_size
    return size_fix_E <= fix_delta_size, size_fix_E, fix_delta_size


def stillborn_mismatch(size_fix_E, fix_delta_size):
    """The mismatch a stillborn square is recorded with.  [instrument --
    mutable]"""
    if _M_STILLBORN:
        return "1 : 1"
    return f"{size_fix_E} : {fix_delta_size}"


# --------------------------------------------------------------------------
# 9.  THE STRENGTHENED TEST -- the order criterion and the two census routes
# --------------------------------------------------------------------------


def order_criterion(E, p, ordpi):
    """THE ORDER CRITERION.  S1a and S1b make the image A an abelian
    Sigma-stable subgroup on which delta_pi acts as I - rho_A(pi); S3 makes
    alpha an isomorphism V -> A, so rho_A(pi) = I - alpha E alpha^-1 and
    rho_A(pi)^ord(Sigma_pi) = I.  Hence

        (I - E)^ord(pi) = I over F_p

    is NECESSARY for any candidate satisfying S1a and S1b and S3.
    [instrument -- mutable]"""
    note_candidate()
    Ep = mat_to_fp(E, p)
    S = mat_sub_fp(eye_fp(NV), Ep, p)
    if _M_CRITERION:
        return kernel_dim_fp(mat_sub_fp(Ep, eye_fp(NV), p), p) == 0
    return mat_pow_fp(S, ordpi, p) == eye_fp(NV)


def order_criterion_polynomial(E, p, ordpi):
    """The same criterion by its POLYNOMIAL form, computed independently of the
    matrix power: at ord 2 it is E = 2I; at ord 3 it is E^2 - 3E + 3I = 0
    (whose roots are exactly 1 - omega for omega a primitive cube root of 1).
    Order 1 forces the constant map."""
    Ep = mat_to_fp(E, p)
    if ordpi == 1:
        return False
    if ordpi == 2:
        return Ep == scal_fp(2, NV, p)
    E2 = mat_mul_fp(Ep, Ep, p)
    Z = [[(E2[i][j] - 3 * Ep[i][j] + (3 if i == j else 0)) % p
          for j in range(NV)] for i in range(NV)]
    return all(all(v == 0 for v in row) for row in Z)


def cube_roots(p):
    return [s for s in range(1, p) if pow(s, 3, p) == 1]


def cyclic_subgroups_of_order(members, p):
    """Every cyclic subgroup of order p in G_C, with a FIXED generator each.
    Enumerated from the measured element orders, never from a formula."""
    subs = {}
    for Q in members:
        if pord(Q) != p:
            continue
        grp = set()
        x = pident(NLAB)
        for _ in range(p):
            grp.add(x)
            x = pcomp(x, Q)
        key = frozenset(grp)
        if key not in subs:
            subs[key] = Q
    return subs


def conjugation_exponent(pi, g, p):
    """s with Sigma_pi g Sigma_pi^-1 = g^s, or None when Sigma_pi does not
    normalise <g>.  Measured by permutation arithmetic."""
    s = SIGMA[pi]
    cg = pcomp(s, pcomp(g, pinv(s)))
    x = pident(NLAB)
    for j in range(p):
        if x == cg:
            return j
        x = pcomp(x, g)
    return None


_DEXP_MEMO: dict = {}


def delta_exponent_table(pi, g, p):
    """dexp[j] = the exponent of delta_pi(g^j) inside <g>, or None if
    delta_pi(g^j) leaves <g>.  Built from PERMUTATIONS -- route B's own
    primitive, with no linear algebra anywhere in it."""
    key = (pi, g, p)
    if key in _DEXP_MEMO:
        return _DEXP_MEMO[key]
    powers = {}
    x = pident(NLAB)
    for j in range(p):
        powers[x] = j
        x = pcomp(x, g)
    out = []
    x = pident(NLAB)
    for j in range(p):
        out.append(powers.get(delta_pi(pi, x)))
        x = pcomp(x, g)
    _DEXP_MEMO[key] = out
    return out


def dexp_slope(dexp, p):
    """The unique c with dexp[j] = c*j for every j, or None.  This is the whole
    of what route B needs from the exponent table."""
    if any(v is None for v in dexp):
        return None
    c = None
    for j in range(1, p):
        cand = dexp[j] * pow(j, -1, p) % p
        if c is None:
            c = cand
        elif c != cand:
            return None
    return c


_PROJ_MEMO: dict = {}


def projective_covectors(p, n):
    """A complete set of representatives of the nonzero covectors up to
    scaling: the first nonzero coordinate normalised to 1.  The count is
    computed.  [instrument -- mutable]"""
    key = (p, n)
    if key in _PROJ_MEMO:
        return _PROJ_MEMO[key]
    out = []
    for lead in range(n):
        for tail in itertools.product(range(p), repeat=n - 1 - lead):
            out.append(tuple([0] * lead + [1] + list(tail)))
    if _M_ROUTEB:
        out = out[:len(out) // 2]
    _PROJ_MEMO[key] = out
    return out


_PROP_MEMO: dict = {}


def proportionality_buckets(E, p, key):
    """Route B's covector enumeration: every projective covector is
    enumerated and classified by the constant c with lambda . E = c lambda,
    when one exists.  The tally is the enumeration's own bookkeeping."""
    if key in _PROP_MEMO:
        return _PROP_MEMO[key]
    Ep = mat_to_fp(E, p)
    prop = {}
    for lam in projective_covectors(p, NV):
        w = [sum(lam[i] * Ep[i][k] for i in range(NV)) % p for k in range(NV)]
        c = None
        for k in range(NV):
            if lam[k]:
                c = w[k] * pow(lam[k], -1, p) % p
                break
        if c is not None and all(w[k] == c * lam[k] % p for k in range(NV)):
            prop[c] = prop.get(c, 0) + 1
    _PROP_MEMO[key] = prop
    return prop


def route_a_count(E, p, pi, subs_norm, ordpi):
    """ROUTE A -- LINEAR ALGEBRA.  A candidate alpha(r) = g^{lambda(r)} with
    <g> normalised by Sigma_pi with exponent s satisfies the square iff
    lambda . E = (1 - s) lambda, i.e. lambda lies in ker(E^T - (1-s)I).  The
    count is the sum over the measured normalised subgroups of the number of
    nonzero solutions, plus the trivial map."""
    ROUTE_CALLS["A"] += 1
    note_candidate()
    Ep = mat_to_fp(E, p)
    Et = transpose(Ep)
    total = 1
    per = {}
    for s in sorted({sv for (_, sv) in subs_norm}):
        lam = (1 - s) % p
        if _M_ROUTEA:
            lam = (lam + 1) % p
        k = kernel_dim_fp(mat_sub_fp(Et, scal_fp(lam, NV, p), p), p)
        cnt = (p ** k) - 1
        nsub = sum(1 for (_, sv) in subs_norm if sv == s)
        per[s] = {"demanded_eigenvalue": lam, "kernel_dim": k,
                  "nonzero_covectors": cnt, "subgroups": nsub}
        total += nsub * cnt
    return total, per


def route_b_count(E, p, pi, subs_all, ordpi, cellkey):
    """ROUTE B -- EXHAUSTIVE ENUMERATION, NO LINEAR ALGEBRA.  Every cyclic
    subgroup of order p is enumerated, its delta-exponent table is built from
    PERMUTATIONS, and every covector is enumerated (projectively, with the
    measured redundancy p - 1 restored).  The square is decided from the
    exponent table alone."""
    ROUTE_CALLS["B"] += 1
    note_candidate()
    if _M_ROUTEALIAS:
        ROUTE_CALLS["taint"] += 1
        return route_a_count(E, p, pi, [(g, s) for (g, s) in subs_all
                                        if s is not None], ordpi)[0]
    if _M_SILENT:
        return route_a_count(E, p, pi, [(g, s) for (g, s) in subs_all
                                        if s is not None], ordpi)[0]
    slopes = [dexp_slope(delta_exponent_table(pi, g, p), p)
              for (g, _s) in subs_all]
    live = [c for c in slopes if c is not None]
    total = 1
    if live:
        prop = proportionality_buckets(E, p, (cellkey, p))
        for c in live:
            total += prop.get(c, 0) * (p - 1)
    if _M_CENSUS:
        total -= 1
    return total


def route_b_full_count(E, p, pi, subs_all):
    """The CALIBRATION of route B's projective enumeration: the same count
    taken over EVERY covector of F_p^6, with no redundancy quotient and no
    projective bookkeeping."""
    Ep = mat_to_fp(E, p)
    slopes = [dexp_slope(delta_exponent_table(pi, g, p), p)
              for (g, _s) in subs_all]
    live = [c for c in slopes if c is not None]
    total = 1
    for lam in itertools.product(range(p), repeat=NV):
        if not any(lam):
            continue
        w = [sum(lam[i] * Ep[i][k] for i in range(NV)) % p for k in range(NV)]
        for c in live:
            if all(w[k] == c * lam[k] % p for k in range(NV)):
                total += 1
    return total


def literal_square_violations(pi, g, lam, E, p, cells):
    """ROUTE C -- the LITERAL permutation verification: alpha(r) = g^{lambda(r)}
    built as an actual permutation and the square compared entry by entry at
    every declared record cell.  [instrument -- mutable]"""
    if _M_LITERAL:
        return 0
    Ep = mat_to_fp(E, p)
    lamE = [sum(lam[i] * Ep[i][k] for i in range(NV)) % p for k in range(NV)]
    powers = []
    x = pident(NLAB)
    for _ in range(p):
        powers.append(x)
        x = pcomp(x, g)
    dperm = [delta_pi(pi, powers[j]) for j in range(p)]
    bad = 0
    for r in cells:
        lr = (lam[0] * r[0] + lam[1] * r[1] + lam[2] * r[2] + lam[3] * r[3] +
              lam[4] * r[4] + lam[5] * r[5]) % p
        ler = (lamE[0] * r[0] + lamE[1] * r[1] + lamE[2] * r[2] +
               lamE[3] * r[3] + lamE[4] * r[4] + lamE[5] * r[5]) % p
        if dperm[lr] != powers[ler]:
            bad += 1
    return bad


# --------------------------------------------------------------------------
# 10.  THE GROWN ARENA AND THE IN-ARENA POSITIVE CONTROL
# --------------------------------------------------------------------------


def growth_labels(m):
    """L_m = {0} + (F_2^3 minus 0) x {1..m}: m copies of TB3's seven moved
    labels.  Point (v, k) has index 1 + k*7 + (v-1)."""
    return 1 + 7 * m


def growth_sigma(pi, m):
    """The wing symmetry on L_m: S_3 acts on the F_2^3 factor alone and fixes
    label 0 and the copy index."""
    sl = sigma_labels(pi)
    n = growth_labels(m)
    out = list(range(n))
    for k in range(m):
        for v in range(1, 8):
            out[1 + k * 7 + (v - 1)] = 1 + k * 7 + (sl[v] - 1)
    return tuple(out)


def scale_threshold_divisibility(p, rank):
    """The smallest number of labels n such that p^rank divides |G_C| =
    (n-1)!.  Computed by Legendre's formula, never typed.  [instrument --
    mutable]"""
    if _M_THRESHOLD:
        return 3 * p + 1
    n = 1
    while legendre_exponent(n - 1, p) < rank:
        n += 1
    return n


def scale_threshold_elementary(p, rank):
    """The smallest n such that S_{n-1} contains an elementary abelian
    subgroup of rank `rank`: the minimal faithful permutation degree of
    (Z/p)^rank is rank*p."""
    if _M_THRESHOLD:
        return 3 * p + 1
    return rank * p + 1


def growth_member_threshold(p, rank):
    """The smallest member of the DECLARED growth family L_m whose completion
    group admits an elementary abelian subgroup of the required rank."""
    m = 1
    while 7 * m < rank * p:
        m += 1
    return m


def control_blocks(m, p, cs):
    """The IN-ARENA positive control at the grown arena.  Each block B_k of
    the growth family is identified with Z/p so that the wing symmetry acts on
    it as multiplication by c_k; the block generator is then translation by 1,
    and conjugation by the wing symmetry sends it to its c_k-th power.
    Returns the generators as permutations of L_m."""
    n = growth_labels(m)
    SIG = growth_sigma((1, 2, 0), m)
    if sorted(SIG) != list(range(n)):
        return None, None    # the wing symmetry is not a permutation of L_m,
    gens = []                # so the control's arena does not construct
    for k in range(m):
        blk = [1 + k * 7 + (v - 1) for v in range(1, 8)]
        fixed = [x for x in blk if SIG[x] == x]
        if len(fixed) != 1:
            return None, None
        f0 = fixed[0]
        rest = [x for x in blk if x != f0]
        orbs, seen = [], set()
        for x in rest:
            if x in seen:
                continue
            o, y = [x], SIG[x]
            while y != x:
                o.append(y)
                y = SIG[y]
            seen.update(o)
            orbs.append(o)
        if len(orbs) != 2:
            return None, None
        c = cs[k]
        sub, y = [1], c % p
        while y != 1:
            sub.append(y)
            y = y * c % p
        other = [z for z in range(1, p) if z not in sub]
        st = min(other)
        oo, y = [st], st * c % p
        while y != st:
            oo.append(y)
            y = y * c % p
        lab = {f0: 0}
        for i, z in enumerate(orbs[0]):
            lab[z] = sub[i]
        for i, z in enumerate(orbs[1]):
            lab[z] = oo[i]
        rlab = {v: kk for kk, v in lab.items()}
        g = list(range(n))
        for pnt, val in lab.items():
            g[pnt] = rlab[(val + 1) % p]
        gens.append(tuple(g))
    return gens, SIG


def control_alpha(gens, powers, r):
    """alpha(r) = product of g_k^{r_k}: the candidate morphism of the
    in-arena positive control.  [instrument -- mutable]"""
    if _M_WITNESS:
        return powers[0][0]
    a = powers[0][r[0]]
    for k in range(1, len(gens)):
        a = pcomp(a, powers[k][r[k]])
    return a


def synthetic_module_action(p):
    """A SYNTHETIC S_3-action on a 2-dimensional record space that is NOT a
    permutation action: the standard representation, whose order-3 element has
    the primitive cube roots as eigenvalues, so I - rho is INVERTIBLE.  This is
    the positive control for the permutation-module obstruction.
    [instrument -- mutable]"""
    if _M_MODBLIND:
        return [[0, 1], [1, 0]]
    return [[0, (p - 1) % p], [1, (p - 1) % p]]


def verification_partition(p):
    """FIT = the single declared basis record e_1; the COMPLEMENT is every
    other element
    of V.  Declared before any candidate is fitted.  [instrument -- mutable]"""
    if _M_PARTITION:
        return tuple([0] * NV), None
    return tuple([1] + [0] * (NV - 1)), None


def teeth_predictions(actual_defect, actual_fix, alpha_perm, nlab):
    """The two extensions declared IN ADVANCE to fail.  [instrument --
    mutable]"""
    if _M_TEETH:
        return True, True
    return (actual_defect == alpha_perm), (actual_fix == nlab)


def break_hom_from_forms(lval, mval, p):
    """BREAK-HOM's exponent, given the two linear forms already evaluated: the
    accepted exponent multiplied by a 1-eigencovector raised to the (p-1)st
    power.  [instrument -- mutable]"""
    if _M_BREAK:
        return lval % p
    return lval * pow(mval % p, p - 1, p) % p


def break_hom_exponent(lam, mu, r, p):
    """BREAK-HOM: the accepted exponent multiplied by a 1-eigencovector raised
    to the p-1 power -- it satisfies the commuting square at every cell and
    differs from an accepted candidate only in the LINEARITY of its exponent,
    so it must be rejected by S1b alone."""
    return break_hom_from_forms(sum(lam[i] * r[i] for i in range(NV)),
                                sum(mu[i] * r[i] for i in range(NV)), p)


def basis_change(p):
    """A declared element of GL_6(F_p) for the change-of-basis self-test.
    [instrument -- mutable]"""
    if _M_BASIS:
        return eye_fp(NV)
    P = eye_fp(NV)
    P[0][1] = 1
    P[2][3] = 1
    P[4][5] = 1
    P[0][5] = 1
    return P


def selftest_set(declared_cells, verdict_selected):
    """RUNBOOK 14 addendum: the self-test's tested set is fixed by DECLARATION,
    never selected by the verdicts under audit.  [instrument -- mutable]"""
    if _M_SELFSELECT:
        return verdict_selected
    return declared_cells


def selftest_fresh():
    """Self-test phases must evaluate FRESH -- the memo is bypassed.
    [instrument -- mutable]"""
    return not _M_SELFTEST


def warm_the_cache(members, pi):
    """The cache must be measured to have been EXERCISED before the self-tests
    begin, or its zero-hit clause is vacuous.  [instrument -- mutable]"""
    if _M_CACHEUNUSED:
        return 0
    n = 0
    for Q in members:
        delta_pi(pi, Q)
        n += 1
    return n

# --------------------------------------------------------------------------
# 11.  THE VERDICT LAYER -- derived in gate, never typed
# --------------------------------------------------------------------------


def derive_verdict(any_precheck_survivor: bool, census_empty: bool,
                   found_reachable: bool, empty_reachable: bool,
                   d3_constructed: bool):
    """The pre-registered outcomes, and ONLY these.  The string is DERIVED here
    from the measured counts; the verdict-flip mutant proves the derivation can
    fail.  [instrument -- mutable]"""
    if _M_VERDICT:
        any_precheck_survivor = not any_precheck_survivor
    if not d3_constructed:
        return "RSQ-BLOCKED-AT-THE-d3-DEFORMATION-ARENA"
    if not (found_reachable and empty_reachable):
        return "RSQ-BLOCKED-AT-THE-TWO-WAY-CENSUS-INSTRUMENT"
    if not any_precheck_survivor:
        return "RSQ-NO-COMPATIBLE-SQUARE"
    if census_empty:
        return "RSQ-SQUARE-FOUND-BRIDGE-EMPTY"
    return "RSQ-SQUARE-FOUND-BRIDGE-FOUND"


def freeze_counter_bump():
    """The freeze counter's own falsifier: this helper evaluates a candidate
    BEFORE the declarations freeze.  [instrument -- mutable]"""
    if _M_FREEZE:
        note_candidate()


def ladder_measured(order: int):
    """The rebuilt defect-subgroup order, as the anchor reads it.
    [instrument -- mutable]"""
    return order + 1 if _M_LADDER_A else order


def found_branch(viol, inj, homviol, norm_ok, comm_ok):
    """The FOUND branch's own decision.  [instrument -- mutable]"""
    if _M_FOUNDBLOCK:
        return False
    return (viol == 0 and inj and homviol == 0 and norm_ok and comm_ok)


def empty_branch(result: bool):
    """The EMPTY branch's own decision.  [instrument -- mutable]"""
    if _M_EMPTYBLOCK:
        return False
    return bool(result)


def s2_stratification_carried(values):
    """S2: the transport side's fixed-label stratification is CARRIED -- the
    verified defect permutations must take more than one value.
    [instrument -- mutable]"""
    if _M_S2:
        return True
    return len(values) > 1


def s4_base_rows(rows):
    """S4: the declared base-change family.  [instrument -- mutable]"""
    if _M_S4:
        return rows[:1]
    return rows


def meeting_verdict(ha_half, demanded, inarena):
    """The spectral meeting's own decision: HA's eigenvalue must lie BOTH in
    the demanded set and in the set the arena actually realises.
    [instrument -- mutable]"""
    if _M_MEETING:
        return True
    return (ha_half in demanded) and (ha_half in inarena)


def teeth_exempt(alpha_perm, ident):
    """The verified cells at which BOTH declared-to-fail extensions are
    ANALYTICALLY forced, because the candidate maps the record to the
    identity.  [instrument -- mutable]"""
    if _M_TEETH:
        return True
    return alpha_perm == ident


def coverage_qualifier(order_covered: int, total: int):
    """The coverage qualifier is MEASURED, not asserted.  [instrument --
    mutable]"""
    if _M_UNIVERSAL:
        return "UNIVERSAL-FOR-THIS-FAMILY"
    if order_covered == total and total > 0:
        return "UNIVERSAL-FOR-THIS-FAMILY"
    return f"PARTIAL-{order_covered}-OF-{total}"


def qualifier_value(name: str, computed):
    """Every numeric qualifier is recomputed at the point of use.
    [instrument -- mutable]"""
    if _M_QUALTYPO:
        return "1440"
    return computed


def completeness(parts, total):
    """Cell-completeness: the parts of every table must sum to its swept total.
    [instrument -- mutable]"""
    if _M_COMPLETE:
        return True
    return sum(parts) == total


def subsumption_holds(criterion_cells, precheck_cells):
    """The precheck is the SHADOW of the order criterion: every cell that
    satisfies the criterion must have trivial fixed space.  [instrument --
    mutable]"""
    if _M_SUBSUME:
        return precheck_cells <= criterion_cells
    return criterion_cells <= precheck_cells


def module_obstruction_measured(E, pi, p):
    """THE PERMUTATION-MODULE OBSTRUCTION, measured rather than asserted.
    S1c-module with S1a, S1b and S3 force E = I - rho_V(pi).  rho_V(pi) is a
    PERMUTATION matrix, so (I - rho_V(pi)) annihilates the all-ones link
    vector; E is invertible, so it does not.  Returns
    (equal, I_minus_rho_kills_ones, E_kills_ones).  [instrument -- mutable]"""
    R = rho_V(pi)
    if E is None or R is None:
        return False, False, False
    Ep = mat_to_fp(E, p)
    IR = [[((1 if i == j else 0) - R[i][j]) % p for j in range(NV)]
          for i in range(NV)]
    ones = [1] * NV
    ir_ones = [sum(IR[i][k] * ones[k] for k in range(NV)) % p for i in range(NV)]
    e_ones = [sum(Ep[i][k] * ones[k] for k in range(NV)) % p for i in range(NV)]
    if _M_MODULE:
        return True, all(v == 0 for v in ir_ones), all(v == 0 for v in e_ones)
    return (Ep == IR, all(v == 0 for v in ir_ones),
            all(v == 0 for v in e_ones))


def census_cell_rule(cells_meta, primes):
    """THE DECLARED CENSUS-CELL RULE, stated before any fixture truth:
      (a) every S_3-EQUIVARIANT identification, both directions;
      (b) HA's own sym_index (LEX) ordering, both directions;
      (c) per direction, the LEXICOGRAPHICALLY FIRST slot order whose fixed
          space is trivial at every declared prime;
      (d) per direction, the LEXICOGRAPHICALLY FIRST slot order whose fixed
          space is trivial at p = 7 AND whose transposed encoding admits the
          order-3 demanded eigenvalue there.
    The resulting set is de-duplicated and its size is COMPUTED.
    [instrument -- mutable]"""
    if _M_CENSUSCELL:
        return [cells_meta[0]["key"]]
    keys = []
    for meta in cells_meta:
        if meta["role"] in ("module", "lex"):
            keys.append(meta["key"])
    for direction in ("q->counts", "counts->q"):
        first_c = None
        first_d = None
        for meta in cells_meta:
            if meta["direction"] != direction:
                continue
            if first_c is None and meta["trivial_fix_all_primes"]:
                first_c = meta["key"]
            if first_d is None and meta["trivial_fix_at_7"] and \
                    meta["meets_at_7"]:
                first_d = meta["key"]
        for k in (first_c, first_d):
            if k is not None:
                keys.append(k)
    out = []
    for k in keys:
        if k not in out:
            out.append(k)
    return out


# --------------------------------------------------------------------------
# 11a.  THE READOUT-PROFILE THEOREM -- the emptiness, derived
#
# The order criterion is decided here WITHOUT any linear algebra over F_p and
# without any census: from the INTEGER readout A alone, by its row profiles.
#
#   (i)   Every row of A is a row of the record<->metric readout in some column
#         order, so its multiset of entries is one of exactly two profiles:
#         an AXIS link gives (0,0,0,0,0,1) and a DIAGONAL link gives
#         (0,0,0,1,1,2).  Column order cannot change a multiset.
#   (ii)  Row 0 -- the axis link e_0 -- is therefore the unit vector e_k, where
#         k is the position the identification gives the metric slot (0,0).
#   (iii) det A = +-8, so E is invertible at every prime p >= 3 and the
#         criterion (I - E)^ord = I is equivalent to a POLYNOMIAL identity in
#         A with integer coefficients:
#             ord 2, q->counts    A = 2I            ord 2, counts->q   2A = I
#             ord 3, q->counts    A^2 - 3A + 3I = 0 ord 3, counts->q   3A^2 - 3A + I = 0
#   (iv)  Reading that identity at ROW 0 and using row_0(A^2) = row_k(A) turns
#         it into an equation between explicit INTEGER vectors; the criterion
#         at a prime p therefore forces p | gcd(witness).  Every witness gcd is
#         measured to have no prime factor >= 5, so the criterion fails at
#         EVERY prime p >= 5 -- at every slot order, both directions, both
#         wing-symmetry orders.  That is a THEOREM, and the 20,160-row sweep is
#         its confirmation rather than its evidence.
# --------------------------------------------------------------------------


def integer_readout(perm):
    """The q -> counts readout at a slot order, as an INTEGER matrix.  This is
    the theorem's only input: no prime, no field, no census."""
    E = encoding_matrix(perm, "q->counts")
    if E is None:
        return None
    return [[int(v) for v in row] for row in E]


def row_profiles(A):
    """The multiset of entries of each row, sorted.  [instrument -- mutable]"""
    if _M_PROFILE:
        return [(0, 0, 0, 0, 0, 1) for _ in A]
    return [tuple(sorted(row)) for row in A]


def slot_position(perm, slot):
    """The position the identification `perm` gives a metric slot."""
    for k in range(NV):
        if SLOTS3[perm[k]] == slot:
            return k
    return None


def criterion_identity(A, direction, ordpi):
    """The criterion's POLYNOMIAL form as an integer matrix that must vanish
    mod p.  Equivalent to (I - E)^ord = I whenever E is invertible."""
    n = len(A)

    def ide(i, j):
        return 1 if i == j else 0
    if ordpi == 2 and direction == "q->counts":
        return [[A[i][j] - 2 * ide(i, j) for j in range(n)] for i in range(n)]
    if ordpi == 2:
        return [[2 * A[i][j] - ide(i, j) for j in range(n)] for i in range(n)]
    A2 = [[sum(A[i][k] * A[k][j] for k in range(n)) for j in range(n)]
          for i in range(n)]
    if direction == "q->counts":
        return [[A2[i][j] - 3 * A[i][j] + 3 * ide(i, j) for j in range(n)]
                for i in range(n)]
    return [[3 * A2[i][j] - 3 * A[i][j] + ide(i, j) for j in range(n)]
            for i in range(n)]


def criterion_row0_witness(A, k, direction, ordpi):
    """Row 0 of the criterion's polynomial identity, written from the PROFILE
    data alone: row_0(A) = e_k and row_0(A^2) = row_k(A)."""
    e0 = [1 if i == 0 else 0 for i in range(NV)]
    ek = [1 if i == k else 0 for i in range(NV)]
    rk = A[k]
    if ordpi == 2 and direction == "q->counts":
        return [ek[i] - 2 * e0[i] for i in range(NV)]
    if ordpi == 2:
        return [2 * ek[i] - e0[i] for i in range(NV)]
    if direction == "q->counts":
        return [rk[i] - 3 * ek[i] + 3 * e0[i] for i in range(NV)]
    return [3 * rk[i] - 3 * ek[i] + e0[i] for i in range(NV)]


def prime_factors(n: int) -> list[int]:
    """The prime factors of |n|; the empty list at 0 and +-1."""
    n = abs(n)
    out = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            if d not in out:
                out.append(d)
            n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def gcd_of(values) -> int:
    g = 0
    for v in values:
        g = _gcd(g, int(v))
    return g


def _gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def admissible_primes_of_witness(v, floor_prime: int):
    """The primes >= floor_prime that could satisfy the criterion at this
    (slot order, direction, wing order): a prime must divide the witness's
    gcd.  A gcd of 0 would leave every prime admissible.  [instrument --
    mutable]"""
    if _M_THEOREM:
        return []
    if _M_THMALIAS:
        order_criterion([[Fr(0)] * NV for _ in range(NV)], floor_prime, 2)
    g = gcd_of(v)
    if g == 0:
        return ["EVERY-PRIME"]
    if _M_THMFLOOR:
        return prime_factors(g)
    return [q for q in prime_factors(g) if q >= floor_prime]


def all_prime_hits(M, floor_prime: int):
    """The EXACT extension of the criterion sweep to every prime at once: the
    identity's whole matrix must vanish mod p, so only the primes dividing its
    gcd can satisfy it.  [instrument -- mutable]"""
    g = gcd_of(v for row in M for v in row)
    if g == 0:
        return ["EVERY-PRIME"]
    return [q for q in prime_factors(g) if q >= floor_prime]


# --------------------------------------------------------------------------
# 11b.  THE TWO VERDICT HALVES -- both names computed
# --------------------------------------------------------------------------


def identification_qualifier(motivated_survivors: int, generic_survivors: int):
    """THE FOUND HALF'S NAME.  The precheck's survivors are classified by the
    identification class they belong to -- MOTIVATED (the S_3-equivariant
    identifications and HA's own sym_index ordering) or GENERIC (an arbitrary
    relabelling of the six metric slots).  The name says which.  [instrument --
    mutable]"""
    if _M_IDENT:
        return "FOUND-AT-A-MOTIVATED-IDENTIFICATION"
    if motivated_survivors > 0:
        return "FOUND-AT-A-MOTIVATED-IDENTIFICATION"
    if generic_survivors > 0:
        return "FOUND-ONLY-AT-UNMOTIVATED-IDENTIFICATIONS"
    return "NO-SURVIVOR-AT-ANY-IDENTIFICATION"


def emptiness_qualifier(coverage: str, theorem_holds: bool, floor_prime: int):
    """THE EMPTY HALF'S NAME.  Coverage alone earns only the census-scoped
    name; the readout-profile theorem earns the prime-unbounded one.
    [instrument -- mutable]"""
    if _M_EMPTFLIP:
        return "UNIVERSAL-FOR-THIS-FAMILY"
    if coverage != "UNIVERSAL-FOR-THIS-FAMILY":
        return coverage
    if theorem_holds:
        return f"UNIVERSAL-BY-THEOREM-AT-EVERY-PRIME-GE-{floor_prime}"
    return "UNIVERSAL-FOR-THIS-FAMILY"


def motivated_precheck_survivors(rows):
    """The survivor count over the MOTIVATED sub-family, computed from the
    per-row precheck results.  [instrument -- mutable]"""
    if _M_MOTIVATED:
        return 1
    return sum(1 for r in rows if r["precheck"] == "PASS")


def master_equation_holds(lhs, rhs):
    """I - E = alpha^-1 rho alpha, read one record at a time: conjugation by
    Sigma on the image, pulled back through alpha, IS the matrix I - E.
    [instrument -- mutable]"""
    if _M_MASTER:
        return True
    return lhs == rhs


def module_independence(precheck_passes: bool, criterion_passes: bool,
                        singular: bool):
    """The module obstruction is INDEPENDENT of the other two walls: the
    module-forced E clears LCB's precheck and the order criterion and dies
    anyway, because E must be invertible and I - rho_V(pi) is not.
    [instrument -- mutable]"""
    if _M_INDEP:
        return True
    return precheck_passes and criterion_passes and singular


def sufficiency_patterns(patterns):
    """The declared sufficiency census: every diagonal pattern the criterion
    admits at p = 7, ord 3.  [instrument -- mutable]"""
    if _M_SUFFICIENCY:
        return patterns[:1]
    return patterns


def spectral_multiplicity(dim_fix: int, d: int):
    """The measured multiplicity of the eigenvalue 1 in HA's readout at a
    motivated identification.  [instrument -- mutable]"""
    if _M_SPECTRAL:
        return d
    return dim_fix


def base_fingerprint(cells, primes, orders, subgroup_sizes):
    """The census's DECIDING INPUTS, fingerprinted inside the per-base loop:
    if the fingerprint is the same at every ladder base then the census cannot
    depend on the base, and base-independence is measured rather than typed.
    [instrument -- mutable]"""
    if _M_BASEINDEP:
        return "IDENTICAL"
    return json.dumps({"cells": sorted(cells), "primes": sorted(primes),
                       "wing_orders": sorted(orders),
                       "subgroup_counts": sorted(subgroup_sizes)},
                      sort_keys=True)


def independent_bad_encoding(p: int):
    """The precheck's negative control, INDEPENDENT of the family under audit:
    a synthetic invertible matrix with a one-dimensional fixed space that is
    not a readout at any slot order or direction.  [instrument -- mutable]"""
    if _M_NEGCONTROL:
        return encoding_matrix(tuple(range(NV)), "q->counts")
    return [[Fr(1 if i == 0 else 3) if i == j else Fr(0) for j in range(NV)]
            for i in range(NV)]


def extension_scope(triples: int) -> int:
    """The number of triples the exact extension actually reaches.
    [instrument -- mutable]"""
    return triples - 1 if _M_EXTENSION else triples


def extended_primes(lo: int, hi: int) -> list[int]:
    """The primes in [lo, hi], sieved rather than typed: the prime range of the
    WIDE corroboration census.  [instrument -- mutable]"""
    sieve = [True] * (hi + 1)
    sieve[0] = sieve[1] = False
    q = 2
    while q * q <= hi:
        if sieve[q]:
            for t in range(q * q, hi + 1, q):
                sieve[t] = False
        q += 1
    out = [q for q in range(lo, hi + 1) if sieve[q]]
    return out[:-1] if _M_WIDEDROP else out


def drop_row_criterion(rows):
    """[instrument -- mutable]"""
    return rows[:-1] if _M_CRITROW else rows


def drop_row_census(rows):
    """[instrument -- mutable]"""
    return rows[:-1] if _M_CENSUSROW else rows


def drop_row_module(rows):
    """[instrument -- mutable]"""
    return rows[:-1] if _M_MODROW else rows


# --------------------------------------------------------------------------
# 12.  SOURCE SCANNERS AND HASH PINS
# --------------------------------------------------------------------------


def float_scan(src: str) -> list[str]:
    """Grep + AST sweep for floats.  Validated by a synthetic injection it must
    flag.  [instrument -- mutable]"""
    hits = []
    if _M_FLOAT:
        return hits
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            hits.append(f"literal at line {node.lineno}")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and \
                node.func.id in ("float", "complex"):
            hits.append(f"call {node.func.id} at line {node.lineno}")
    return hits


def float_scan_selftest() -> bool:
    sample = "x = 1.5\ny = float(2)\n"
    return len(float_scan(sample)) >= 1 if not _M_FLOAT else False


GATE_REGISTRARS = ("gate", "anchor")
MUTANT_TOKENS = ("MUTANT", "SELFTEST_ONLY", "argv")


def ast_mutant_scan(src: str) -> list[str]:
    """No function that registers a gate may reference mutant identity.
    Validated by a synthetic sample it must flag.  [instrument -- mutable]"""
    hits = []
    if _M_EXEMPT:
        return hits
    tree = ast.parse(src)
    for fn in [n for n in ast.walk(tree)
               if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]:
        registers = any(isinstance(c, ast.Call) and isinstance(c.func, ast.Name)
                        and c.func.id in GATE_REGISTRARS
                        for c in ast.walk(fn))
        if not registers:
            continue
        for n in ast.walk(fn):
            if isinstance(n, ast.Name) and (
                    n.id in MUTANT_TOKENS or n.id.startswith("_M_")):
                hits.append(f"{fn.name} references {n.id} at line {n.lineno}")
    return hits


def ast_mutant_scan_selftest() -> bool:
    sample = ("def f():\n"
              "    if _M_X:\n"
              "        pass\n"
              "    gate('G', 'c', True)\n")
    return len(ast_mutant_scan(sample)) >= 1 if not _M_EXEMPT else False


PINS = {
    "pin": ("v13/note-rsq-reposed-square-pin.md", "bc79fb6111ff6c90"),
    "lcb_paper": ("v13/paper-lcb-livecell.md", "3ff069d2127b0917"),
    "lcb_receipt": ("v13/code/lcb_livecell_receipt.json", "3e502f685ab3010f"),
    "tb3_paper": ("v13/paper-tb3-third-base.md", "4a1f9c53d8640145"),
    "tb3_receipt": ("v13/code/tb3_third_base_receipt.json", "c9bc956fe75129bd"),
    "ha_paper": ("v13/paper-ha-successor.md", "f286ba10d2d9a0f3"),
    "ha_receipt": ("v13/code/ha_successor_receipt.json", "542b8735daf0ebc6"),
    "brg_paper": ("v13/paper-brg-bridge.md", "371e38742059d14a"),
    "brg_receipt": ("v13/code/brg_bridge_receipt.json", "5c428afd5c58c899"),
    "psi_paper": ("v13/paper-psi-curvature.md", "41d358d421d8288d"),
    "psi_receipt": ("v13/code/psi_curvature_receipt.json", "7c7b91a9257e3888"),
}

_PIN_MUT = {"pin": _M_PIN_SHA or _M_SOFT, "lcb_receipt": _M_LCB_SHA,
            "tb3_receipt": _M_TB3_SHA, "ha_receipt": _M_HA_SHA,
            "brg_paper": _M_BRG_SHA, "psi_receipt": _M_PSI_SHA}


def pinned_prefix(key: str) -> str:
    """[instrument -- mutable]"""
    path = os.path.join(REPO, PINS[key][0])
    pre = sha256_file(path)[:16]
    if _PIN_MUT.get(key):
        pre = pre[:-1] + ("0" if pre[-1] != "0" else "1")
    return pre

# ==========================================================================
#                                THE UNIT
# ==========================================================================


def run_unit(src: str) -> dict:
    tables: dict = {}
    quals: dict = {}
    say("=" * 78)
    say("RSQ -- THE RE-POSED SQUARE AT THREE WINGS")
    say("=" * 78)
    say("")

    # ---------------------------------------------------------------- 1 ---
    say("------------------------------------------------------------------")
    say("1. THE DECLARATIONS, FROZEN; THE SCANNERS; THE HASH PINS")
    say("------------------------------------------------------------------")
    progress("declarations")
    freeze_counter_bump()
    g01 = gate("G01", "THE DECLARATIONS ARE FROZEN BEFORE ANY CANDIDATE IS "
               "EVALUATED.  Every candidate evaluation in this instrument runs "
               "through a counter; the counter is measured HERE and must read "
               "zero.  What this records is the ordering WITHIN ONE EXECUTION; "
               "it is not offered as proof that the declarations were fixed "
               "before any fixture truth was seen, which no in-run measurement "
               "can establish",
               CANDIDATE_EVALS[0] == 0,
               {"candidates_evaluated_before_the_freeze": CANDIDATE_EVALS[0]})
    report("G01", g01, f"candidate evaluations at the freeze point: "
                       f"{CANDIDATE_EVALS[0]}")
    # the declared REFERENCE PRIME of the census-cell rule and of the printed
    # per-prime column, taken from the declared sweep rather than typed
    pref = 7 if 7 in sweep_primes() else sweep_primes()[0]
    floor_prime = 5

    fh = float_scan(src)
    fst = float_scan_selftest()
    g02 = gate("G02", "EXACT ARITHMETIC ONLY: the source carries no float or "
               "complex literal and no float()/complex() call, measured by an "
               "AST sweep that is itself VALIDATED by a synthetic injection it "
               "must flag", len(fh) == 0 and fst,
               {"float_hits": fh, "scanner_flags_the_synthetic_sample": fst})
    report("G02", g02, f"float hits {len(fh)}; scanner self-test {fst}")

    ah = ast_mutant_scan(src)
    ast_st = ast_mutant_scan_selftest()
    g03 = gate("G03", "NO GATE-REGISTERING FUNCTION REFERENCES MUTANT IDENTITY "
               "(RUNBOOK 14 addendum, v13 #208): every mutation is a mutation "
               "of an INSTRUMENT helper.  The AST guard is validated by a "
               "synthetic sample it must flag", len(ah) == 0 and ast_st,
               {"exempt_hits": ah, "scanner_flags_the_synthetic_sample": ast_st})
    report("G03", g03, f"mutant-identity hits {len(ah)}; scanner self-test "
                       f"{ast_st}")

    hp = {}
    for k in sorted(PINS):
        pre = pinned_prefix(k)
        hp[k] = {"path": PINS[k][0], "sha256_prefix": pre}
        anchor(f"A-SHA-{k}", f"sha256 prefix of {PINS[k][0]}", PINS[k][1], pre,
               "this file, pinned SHA-256 of a TERMINAL artifact")
    say(f"  {len(PINS)} terminal artifacts hash-pinned and verified "
        f"(TB3 #299, LCB #297, HA #262, BRG #276, PSI #265)")
    say("")

    # ---------------------------------------------------------------- 2 ---
    say("------------------------------------------------------------------")
    say("2. ITEM 1 -- HA REBUILT AT d = 3: THE DEFORMATION ARENA")
    say("------------------------------------------------------------------")
    progress("HA at d=3")
    lks = link_set(D3)
    S = sites(D3, L3)
    nlinks_forced = D3 + (D3 * (D3 - 1)) // 2
    recs = {nm: GeomRecord3(nm, t) for nm, t in DECL["records_d3"].items()}
    negs = {nm: GeomRecord3(nm, t) for nm, t in DECL["negative_records_d3"].items()}
    adm = sorted(nm for nm, r in recs.items() if r.admissible)
    neg_rejected = sorted(nm for nm, r in negs.items() if not r.admissible)
    say(f"  |X| = {len(S)} sites, {len(lks)} links "
        f"(the {D3} axes and the {(D3*(D3-1))//2} positive diagonals)")
    say(f"  declared records admissible: {adm}")
    say(f"  declared negative controls REJECTED: {neg_rejected} "
        f"(of {len(negs)})")
    g04 = gate("G04", "THE d = 3 ARENA CONSTRUCTS.  The site set and the link "
               "set are enumerated and their sizes agree with the counts the "
               "declaration forces; all three of HA's own declared d = 3 "
               "records are admissible by the EXACT Sylvester criterion at "
               "every site; and both declared negative controls -- one "
               "singular, one indefinite -- are REJECTED by the same test, so "
               "the admissibility clause is not vacuous",
               len(S) == L3 ** D3 and len(lks) == nlinks_forced and
               len(adm) == len(recs) and len(neg_rejected) == len(negs),
               {"sites": len(S), "sites_forced": L3 ** D3,
                "links": len(lks), "links_forced": nlinks_forced,
                "admissible_records": adm, "of_declared": len(recs),
                "negative_controls_rejected": neg_rejected,
                "of_negative_controls": len(negs)})
    report("G04", g04, f"{len(S)} sites, {len(lks)} links, {len(adm)}/"
                       f"{len(recs)} admissible, {len(neg_rejected)}/"
                       f"{len(negs)} controls rejected")

    RO = ha_readout_matrix(D3)
    det3 = det_exact(RO)
    reenc_ok = reenc_tot = 0
    for nm in adm:
        r = recs[nm]
        for x in r.S:
            reenc_tot += 1
            if all(sum(r.q[x][i][j] * lk[i] * lk[j] for i in range(D3)
                       for j in range(D3)) == r.counts[x][lk] for lk in r.links):
                reenc_ok += 1
    Enat = encoding_matrix(tuple(range(NV)), "q->counts")
    detnat = det_exact(Enat)
    spec_nat = [Enat[i][i] for i in range(NV)]
    dsweep_rows = []
    for dd in dimension_sweep():
        for ordering in ("natural", "lex"):
            A = general_d_readout(dd, ordering)
            n = len(A)
            dsweep_rows.append({"d": dd, "ordering": ordering, "size": n,
                                "det": str(det_exact(A)),
                                "column_sums": [str(sum(A[i][c] for i in range(n)))
                                                for c in range(n)]})
    det_law_ok = all(row["det"] == str(2 ** ((row["d"] * (row["d"] - 1)) // 2))
                     for row in dsweep_rows if row["ordering"] == "natural")
    say(f"  HA's own G28 readout at d = 3 (rows the links SORTED, columns "
        f"sym_index): det = {det3}")
    say(f"  the natural identification's readout, q -> counts: det = {detnat}, "
        f"diagonal (its spectrum, triangular) = {[str(v) for v in spec_nat]}")
    say(f"  q reproduces every declared link count at {reenc_ok} of "
        f"{reenc_tot} sites")
    g05 = gate("G05", "THE d = 3 RECORD-IS-METRIC READOUT IS AN INVERTIBLE "
               "LINEAR RE-ENCODING WITH DETERMINANT 8 AND SPECTRUM "
               "{1,1,1,2,2,2} -- exactly the requirement R2-LCB measured for "
               "the successor.  The determinant is computed exactly; q "
               "reproduces every declared link count at every site of every "
               "admissible record; and the general law det = 2^(d(d-1)/2) with "
               "spectrum {1^d, 2^(d(d-1)/2)} is re-measured at every swept "
               "dimension",
               det3 == Fr(8) and detnat == Fr(8) and reenc_ok == reenc_tot and
               reenc_tot > 0 and
               sorted(str(v) for v in spec_nat) == ["1", "1", "1", "2", "2", "2"]
               and det_law_ok,
               {"HA_convention_determinant": str(det3),
                "natural_identification_determinant": str(detnat),
                "spectrum": [str(v) for v in spec_nat],
                "sites_where_q_reproduces_every_count": reenc_ok,
                "sites_tested": reenc_tot,
                "general_dimension_rows": dsweep_rows,
                "determinant_law_holds_at_every_swept_dimension": det_law_ok})
    report("G05", g05, f"det {det3}; spectrum {[str(v) for v in spec_nat]}; "
                       f"re-encoding {reenc_ok}/{reenc_tot}")
    anchor("A-LCB-D3-NAT", "LCB G36 general-d row: d = 3, natural, dim fix(E)",
           3, fix_space_dim(encoding_matrix(tuple(range(NV)), "q->counts"), 5),
           "LCB committed receipt (G36)")
    lexperm = tuple(SLOTS3.index(s) for s in sym_index(D3))
    anchor("A-LCB-D3-LEX", "LCB G36 general-d row: d = 3, lex, dim fix(E)",
           1, fix_space_dim(encoding_matrix(lexperm, "q->counts"), 5),
           "LCB committed receipt (G36)")
    anchor("A-LCB-D3-COLSUM", "LCB G36 general-d row: d = 3, natural, column "
           "sums", ["3", "3", "3", "2", "2", "2"],
           [row["column_sums"] for row in dsweep_rows
            if row["d"] == 3 and row["ordering"] == "natural"][0],
           "LCB committed receipt (G36)")
    anchor("A-HA-D2-DET", "HA G28: the d = 2 readout determinant", "2",
           str(det_exact(ha_readout_matrix(2))), "HA committed receipt (G28)")

    rec = recs["G3-OFF"]
    Nl = {y: (1 if y == DECL["detector_site"] else 0) for y in S}
    Ml = {y: (1 if y in ((0, 0, 1), (0, 1, 0), (1, 0, 0)) else 0) for y in S}
    xs = DECL["detector_site"]
    # the residual is defined only where the record's metric is: a link set
    # that does not determine one is a STRUCTURAL failure, recorded as such and
    # scored at the gates below rather than raised
    arena_well_posed = (len(set(lks)) == len(lks) and rec.nonsingular)
    lit_ok = lit_tot = 0
    nonzero_sites = 0
    rho_x = tuple(Fr(0) for _ in range(D3))
    rho_closed = None
    if arena_well_posed:
        rho_closed = residual_closed(rec, Nl, Ml)
        n0flat = {x: 0 for x in S}
        rho_lit = residual_literal(rec, Nl, Ml, n0flat)
        for x in S:
            lit_tot += 1
            if rho_lit is not None and \
                    all(rho_lit[x][i] == rho_closed[x][i] for i in range(D3)):
                lit_ok += 1
        rho_x = rho_closed[xs]
        nonzero_sites = sum(1 for x in S
                            if any(v != 0 for v in rho_closed[x]))
    say(f"  the residual R_HH at d = 3, two comparators (the literal five-map "
        f"composition and the closed form): {lit_ok} of {lit_tot} sites agree")
    say(f"  exact rational residual at the detector site x* = {xs}: "
        f"{[str(v) for v in rho_x]}; nonzero at {nonzero_sites} of {len(S)} "
        f"sites")
    g06 = gate("G06", "THE d = 3 RESIDUAL RUNS, AND ITS TWO COMPARATORS AGREE. "
               "R_HH is computed both as the LITERAL five-map composition on "
               "exact rational fields and by the CLOSED FORM built from the "
               "drag rule and the record readout without touching the "
               "composition; the two agree at every site.  The residual is "
               "measured NONZERO at the detector site, so the arena it "
               "generates is not trivial",
               arena_well_posed and lit_ok == lit_tot and lit_tot > 0 and
               any(v != 0 for v in rho_x),
               {"link_set_determines_a_metric": arena_well_posed,
                "sites_where_the_two_comparators_agree": lit_ok,
                "sites_tested": lit_tot,
                "residual_at_the_detector_site": [str(v) for v in rho_x],
                "sites_with_a_nonzero_residual": nonzero_sites,
                "of_sites": len(S)})
    report("G06", g06, f"{lit_ok}/{lit_tot} agree; rho(x*) = "
                       f"{[str(v) for v in rho_x]}")

    prime_rows = []
    trans_ok = trans_tot = 0
    for p in sweep_primes():
        rho_p = tuple(to_fp_frac(v, p) for v in rho_x)
        row = {"p": p, "carrier": p ** (2 + D3),
               "rho_mod_p": list(rho_p), "built": False,
               "group_order": None, "translation": None}
        if p in carrier_primes() and arena_well_posed:
            n0 = {x: (x[0] * x[1] * x[2]) % p for x in S}
            RC = ReducedCarrier3(rec, p, n0, [Nl, Ml], xs)
            PN, PM = RC.perm_H(Nl), RC.perm_H(Ml)
            bb = beta_field(rec, Nl, Ml)
            PD = RC.perm_D({x: tuple(-bb[x][i] for i in range(D3)) for x in S})
            if PN is not None and PM is not None and PD is not None:
                R = pcomp(PN, pcomp(PM, pcomp(pinv(PN), pcomp(pinv(PM), PD))))
                trans_tot += 1
                tr = register_shift_of(RC, R, rho_p)
                if tr:
                    trans_ok += 1
                row.update({"built": True, "k": RC.k, "carrier": RC.size,
                            "fronts": len(RC.fronts),
                            "register_dimension": D3,
                            "group_order": pord(R), "translation": tr})
        prime_rows.append(row)
        progress(f"  carrier prime {p}")
    orders = [r["group_order"] for r in prime_rows if r["built"]]
    built_primes = [r["p"] for r in prime_rows if r["built"]]
    order_is_prime = (orders == built_primes)
    say(f"  {'p':5s}{'carrier':11s}{'k':4s}{'rho mod p':14s}"
        f"{'|<R_HH>|':10s}translation-by-rho")
    for r in prime_rows:
        say(f"  {r['p']:<5d}{r['carrier']:<11d}{str(r.get('k','-')):4s}"
            f"{str(r['rho_mod_p']):14s}{str(r['group_order']):10s}"
            f"{r['translation']}")
    g07 = gate("G07", "HA's G29 HOLDS VERBATIM AT d = 3, WITH 3-DIMENSIONAL "
               "FRONTS.  R_HH acts on the reduced carrier "
               "C_HA(p) = F_p^k x F_p^3 as the TRANSLATION OF THE "
               "3-DIMENSIONAL ADDRESS REGISTER by rho mod p, measured "
               "configuration by configuration, with the front sector "
               "returning to itself; hence <R_HH> is cyclic of order p "
               "wherever rho is nonzero mod p.  The deformation side of the "
               "re-posed square therefore CONSTRUCTS at d = 3",
               trans_ok == trans_tot and trans_tot > 0 and order_is_prime,
               {"primes_built": built_primes, "carriers_checked": trans_tot,
                "translation_structure_confirmed": trans_ok,
                "measured_group_orders": orders,
                "order_equals_the_declared_prime": order_is_prime,
                "rows": prime_rows,
                "build_cap": "the carrier has p^(k+3) configurations; the "
                             "primes at which it is BUILT as permutations are "
                             "declared, and rho is reduced at every declared "
                             "prime"})
    report("G07", g07, f"translation structure {trans_ok}/{trans_tot}; "
                       f"orders {orders} against primes {built_primes}")
    g08 = gate("G08", "THE HOLONOMY ORDER IS AN ARENA COORDINATE AT d = 3 TOO "
               "(RUNBOOK 15, HA's G30 re-proved here): swept over the built "
               "primes the measured group order EQUALS the declared prime at "
               "every one, while the exact rational residual is measured "
               "prime-INDEPENDENT.  A quantity that moves with the arena may "
               "serve as an instrument reading and may never enter as a "
               "conclusion, and no argument below uses it",
               order_is_prime and len(set(orders)) == len(orders) and
               len(orders) > 1,
               {"built_primes": built_primes, "measured_orders": orders,
                "exact_residual": [str(v) for v in rho_x],
                "residual_is_prime_independent": True})
    report("G08", g08, f"orders {orders} track the primes {built_primes}")
    tables["ha_d3_prime_sweep"] = prime_rows
    d3_constructed = g04 and g05 and g06 and g07
    say("")

    # ---------------------------------------------------------------- 3 ---
    say("------------------------------------------------------------------")
    say("3. ITEM 2 -- THE TRANSPORT SIDE AT THREE WINGS")
    say("------------------------------------------------------------------")
    progress("transport side")
    GC = completion_group()
    import math as _math
    gc_forced = _math.factorial(NLAB - 1)
    wing_orders = sorted(pord(SIGMA[pi]) for pi in S3_ELEMS)
    wing_abelian = all(pcomp(SIGMA[a], SIGMA[b]) == pcomp(SIGMA[b], SIGMA[a])
                       for a in S3_ELEMS for b in S3_ELEMS)
    wing_closed = all(pcomp(SIGMA[a], SIGMA[b]) in set(SIGMA.values())
                      for a in S3_ELEMS for b in S3_ELEMS)
    fix_all = sorted(set.intersection(*[{i for i in range(NLAB)
                                        if SIGMA[pi][i] == i}
                                       for pi in S3_ELEMS]))
    invol = sum(1 for pi in S3_ELEMS if pcomp(SIGMA[pi], SIGMA[pi]) ==
                pident(NLAB))
    say(f"  |G_C| = {len(GC)} (enumerated) = {gc_forced} (the factorial the "
        f"declaration forces)")
    say(f"  the wing symmetry group: order {len(set(SIGMA.values()))}, "
        f"abelian {wing_abelian}, element orders {wing_orders}")
    say(f"  labels fixed by EVERY wing symmetry: {fix_all}; wing symmetries "
        f"with P^2 = 1: {invol} of {len(S3_ELEMS)}")
    g09 = gate("G09", "THE THREE-WING TRANSPORT BASE IS REBUILT.  The "
               "completion group -- the permutations of the 8 system-triple "
               "labels FIXING label 0 -- is enumerated and its size agrees "
               "with the factorial the declaration forces; the wing symmetry "
               "group is measured closed, NON-ABELIAN, of order 6 with "
               "element orders {1,2,2,2,3,3}; every wing symmetry fixes labels "
               "0 and 7 (7 = |111>), and exactly 4 of the 6 square to the "
               "identity",
               len(GC) == gc_forced and len(set(SIGMA.values())) == 6 and
               (not wing_abelian) and wing_closed and
               wing_orders == [1, 2, 2, 2, 3, 3] and fix_all == [0, 7],
               {"completion_group_order": len(GC),
                "completion_group_order_forced": gc_forced,
                "wing_group_order": len(set(SIGMA.values())),
                "abelian": wing_abelian, "closed": wing_closed,
                "element_orders": wing_orders,
                "labels_fixed_by_every_wing_symmetry": fix_all,
                "wing_symmetries_with_P_squared_equal_1": invol})
    report("G09", g09, f"|G_C| = {len(GC)}; wing orders {wing_orders}; fixed "
                       f"labels {fix_all}")
    anchor("A-TB3-CENSUS", "TB3: the completion census size", 5040, len(GC),
           "TB3 committed receipt (TB3-A1-ORDCENSUS)")
    anchor("A-TB3-WING", "TB3: the wing symmetry group's element orders",
           [1, 2, 2, 2, 3, 3], wing_orders, "TB3 committed receipt (TB3-S3)")
    anchor("A-TB3-INVOL", "TB3: wing symmetries with P^2 = 1 "
           "(TB3's F_1 hits 36 = 4 x 9 members)", 4, invol,
           "TB3 committed receipt (TB3-A2, form_hits F_1 = 36 over 9 members)")

    f1f3 = {"agree": 0, "differ": 0, "agree_at_involutions": 0,
            "involution_cells": 0, "delta_is_F3": 0}
    formcells = 0
    for pi in S3_ELEMS:
        isinv = (pcomp(SIGMA[pi], SIGMA[pi]) == pident(NLAB))
        for nm, Q in sorted(DECL["ladder_completions"].items()):
            formcells += 1
            if delta_pi(pi, Q) == form_F3(pi, Q):
                f1f3["delta_is_F3"] += 1
            same = (delta_pi(pi, Q) == form_F1(pi, Q))
            f1f3["agree" if same else "differ"] += 1
            if isinv:
                f1f3["involution_cells"] += 1
                if same:
                    f1f3["agree_at_involutions"] += 1
    cocycle_bad = 0
    cocycle_cells = 0
    for pi in S3_ELEMS:
        for nmX, X in sorted(DECL["ladder_completions"].items()):
            for nmY, Y in sorted(DECL["ladder_completions"].items()):
                cocycle_cells += 1
                lhs = form_F2(pi, pcomp(X, Y))
                rhs = pcomp(form_F2(pi, Y), pcomp(pinv(Y),
                                                  pcomp(form_F2(pi, X), Y)))
                if lhs != rhs:
                    cocycle_bad += 1
    say(f"  the three commutator forms at {formcells} (wing symmetry, "
        f"completion) cells: F_1 = F_3 at {f1f3['agree']}, and at "
        f"{f1f3['agree_at_involutions']} of {f1f3['involution_cells']} "
        f"involution cells")
    say(f"  the twisted cocycle identity: {cocycle_bad} deviations of "
        f"{cocycle_cells} cells")
    g10 = gate("G10", "THE THREE-WING COMMUTATOR ENCODING IS THE ONE TB3 "
               "DECIDED.  delta_pi(Q) = Sigma_pi Q^-1 Sigma_pi^-1 Q is TB3's "
               "F_3 = [Sigma_pi^-1, Q]; the four-factor writing F_1 is "
               "measured to agree with it at EXACTLY the cells whose wing "
               "symmetry squares to the identity and nowhere else -- so the "
               "two readings really do come apart at three wings, as TB3 "
               "measured -- and the twisted cocycle identity for F_2 holds "
               "with zero deviations",
               f1f3["agree"] == f1f3["agree_at_involutions"] and
               f1f3["agree"] == f1f3["involution_cells"] and
               f1f3["differ"] > 0 and cocycle_bad == 0 and cocycle_cells > 0
               and f1f3["delta_is_F3"] == formcells,
               {"cells": formcells, "delta_equals_F3": f1f3["delta_is_F3"],
                "F1_equals_F3": f1f3["agree"],
                "F1_differs_from_F3": f1f3["differ"],
                "involution_cells": f1f3["involution_cells"],
                "F1_equals_F3_at_involution_cells":
                    f1f3["agree_at_involutions"],
                "cocycle_cells": cocycle_cells,
                "cocycle_deviations": cocycle_bad})
    report("G10", g10, f"F1=F3 at {f1f3['agree']}/{formcells}; cocycle "
                       f"deviations {cocycle_bad}")

    ladder = {}
    for nm, Q in sorted(DECL["ladder_completions"].items()):
        K = ladder_defect_subgroup(Q)
        ladder[nm] = len(K)
    committed_ladder = {"ord1": 1, "ord2": 168, "ord3": 12, "ord6": 2520,
                        "reference": 360}
    lad_meas = {k: ladder_measured(ladder[k]) for k in ladder}
    say(f"  the ladder rebuilt as the structure-group family "
        f"(K = <delta_pi(Q) : pi in S_3>): "
        f"{ {k: ladder[k] for k in sorted(ladder)} }")
    g11 = gate("G11", "TB3's LADDER IS REBUILT HERE AS THE STRUCTURE-GROUP "
               "FAMILY OF THIS PAIRING.  The defect subgroup "
               "K = <delta_pi(Q) : pi in S_3> is closed explicitly as a "
               "permutation group on the 8 labels at each of TB3's five "
               "declared ord-target completions, and its order reproduces "
               "TB3's own defect-subgroup order at every one: 1 < 12 < 168 < "
               "360 < 2520, the ladder 1 < A_4 < GL(3,2) < A_6 < A_7",
               all(ladder[k] == committed_ladder[k] for k in committed_ladder)
               and len(set(ladder.values())) == len(committed_ladder),
               {"rebuilt": {k: ladder[k] for k in sorted(ladder)},
                "committed": committed_ladder})
    report("G11", g11, f"ladder {sorted(ladder.values())}")
    for nm in sorted(committed_ladder):
        anchor(f"A-TB3-K-{nm}", f"TB3 ladder: |K| at the {nm} completion",
               committed_ladder[nm], lad_meas[nm],
               "TB3 committed receipt (TB3-LADDER, defect_subgroup_order)")

    fixrows = []
    for pi in S3_ELEMS:
        fx = delta_fixed_points(GC, pi)
        fixrows.append({"pi": list(pi), "ord": pord(SIGMA[pi]),
                        "members": len(GC), "fix_size": len(fx),
                        "the_fixed_point_is_the_identity":
                            fx == [pident(NLAB)]})
    # LCB's own two-wing 9-label arena, rebuilt here as an external anchor
    NL9 = 9
    sig9 = tuple(3 * (i % 3) + (i // 3) for i in range(NL9))
    gc9 = [(0,) + q for q in itertools.permutations(range(1, NL9))]
    fix9 = 0
    for Q in gc9:
        if pcomp(sig9, pcomp(pinv(Q), pcomp(pinv(sig9), Q))) == Q:
            fix9 += 1
    anchor("A-LCB-FIXDELTA", "LCB G35: |fix(delta)| at the 9-label arena",
           1, fix9, "LCB committed receipt (G35)")
    allfix1 = all(r["fix_size"] == 1 and r["the_fixed_point_is_the_identity"]
                  for r in fixrows)
    say(f"  fix(delta_pi) at all {len(S3_ELEMS)} wing symmetries over all "
        f"{len(GC)} completions: "
        f"{sorted({r['fix_size'] for r in fixrows})}")
    say(f"  the same measurement at LCB's own 9-label two-wing arena "
        f"({len(gc9)} members): {fix9}")
    g12 = gate("G12", "THE FIXED-POINT WALL TRANSPORTS TO THREE WINGS "
               "UNCHANGED.  delta_pi(Q) = Q forces Sigma_pi Q^-1 Sigma_pi^-1 = "
               "e, hence Q = e, because conjugation is injective -- there is "
               "no hypothesis on the arena in that line.  Measured member by "
               "member over the whole completion group at EVERY one of the six "
               "wing symmetries, and again at LCB's own nine-label two-wing "
               "arena: exactly ONE fixed point everywhere, and it is the "
               "identity",
               allfix1 and fix9 == 1,
               {"rows": fixrows, "nine_label_arena_members": len(gc9),
                "nine_label_arena_fix_size": fix9})
    report("G12", g12, f"|fix(delta_pi)| = 1 at {len(fixrows)}/{len(fixrows)} "
                       f"wing symmetries; 9-label arena {fix9}")
    tables["fix_delta"] = fixrows
    fix_delta_size = fixrows[0]["fix_size"]
    say("")

    # ---------------------------------------------------------------- 4 ---
    say("------------------------------------------------------------------")
    say("4. ITEM 3 -- THE CANDIDATE-SQUARE FAMILY, DECLARED AS DATA")
    say("------------------------------------------------------------------")
    progress("candidate family")
    equi = equivariant_identifications()
    perms = slot_orders()
    forced_orders = 1
    for _i in range(1, NV + 1):
        forced_orders *= _i
    directions = ("q->counts", "counts->q")
    say(f"  slot orders enumerated: {len(perms)} (the factorial the "
        f"declaration forces: {forced_orders})")
    say(f"  S_3-EQUIVARIANT identifications, found by an exhaustive "
        f"equivariance test: {len(equi)}")
    for e in equi:
        say(f"     {[str(SLOTS3[i]) for i in e]}")
    g13 = gate("G13", "THE S_3-EQUIVARIANT IDENTIFICATIONS ARE COMPUTED, NOT "
               "TYPED.  Every one of the 6! slot orders is tested for "
               "equivariance between the S_3-action on the six links and the "
               "S_3-action on the six metric slots, at every group element; "
               "the surviving set is measured to have exactly two members -- "
               "the NATURAL identification (each diagonal slot with its axis "
               "link) and the SWAP identification (each diagonal slot with the "
               "diagonal link of the complementary pair).  Two is what the "
               "orbit structure forces: both index sets are two free copies of "
               "the natural S_3-set, and the centraliser of S_3 in S_3 is "
               "trivial",
               len(perms) == forced_orders and len(equi) == 2 and
               tuple(range(NV)) in equi,
               {"slot_orders": len(perms), "slot_orders_forced": forced_orders,
                "equivariant_identifications": len(equi),
                "equivariant_slot_orders": [list(e) for e in equi],
                "natural_is_among_them": tuple(range(NV)) in equi})
    report("G13", g13, f"{len(perms)} slot orders; {len(equi)} equivariant")

    cells_meta = []
    dropped = 0
    for perm in perms:
        for direction in directions:
            E = encoding_matrix(perm, direction)
            if E is None:
                dropped += 1
                continue
            role = "set"
            if perm in equi:
                role = "module"
            elif perm == tuple(SLOTS3.index(s) for s in sym_index(D3)):
                role = "lex"
            fixdims = {p: fix_space_dim(E, p) for p in sweep_primes()}
            Ep7 = mat_to_fp(E, pref)
            Et7 = transpose(Ep7)
            meets7 = any(kernel_dim_fp(
                mat_sub_fp(Et7, scal_fp((1 - s) % pref, NV, pref), pref),
                pref) > 0
                for s in cube_roots(pref) if s != 1)
            cells_meta.append({
                "key": (perm, direction), "perm": list(perm),
                "direction": direction, "role": role,
                "fix_dims": fixdims,
                "trivial_fix_all_primes": all(v == 0 for v in fixdims.values()),
                "trivial_fix_at_7": fixdims[pref] == 0,
                "meets_at_7": meets7})
    ncells = len(cells_meta)
    ncells_forced = forced_orders * len(directions)
    role_counts = {}
    for m in cells_meta:
        role_counts[m["role"]] = role_counts.get(m["role"], 0) + 1
    say(f"  the COVARIANT cell family: {ncells} cells "
        f"({len(perms)} slot orders x {len(directions)} directions), roles "
        f"{ {k: role_counts[k] for k in sorted(role_counts)} }")
    g14 = gate("G14", "THE COVARIANT CELL FAMILY IS THE WHOLE ORBIT OF THE "
               "DECLARED IDENTIFICATION UNDER THE SLOT-RELABELLING GROUP "
               "(RUNBOOK 15): every ordering of the six metric slots, in both "
               "directions.  The count is computed from the declared slot set "
               "and never typed, every slot order is classified exactly once, "
               "and the classification is CELL-COMPLETE -- the role counts sum "
               "to the swept total",
               ncells == ncells_forced and dropped == 0 and
               completeness(list(role_counts.values()), ncells),
               {"cells": ncells, "cells_forced": ncells_forced,
                "invertible_failures": dropped,
                "role_counts": {k: role_counts[k] for k in sorted(role_counts)},
                "cell_complete": completeness(list(role_counts.values()),
                                              ncells)})
    report("G14", g14, f"{ncells}/{ncells_forced} cells; roles complete "
                       f"{completeness(list(role_counts.values()), ncells)}")

    census_keys = census_cell_rule(cells_meta, sweep_primes())
    meta_by_key = {m["key"]: m for m in cells_meta}
    census_cells = [meta_by_key[k] for k in census_keys if k in meta_by_key]
    # the rule's own expected return, rebuilt HERE by a second enumeration that
    # shares no code with census_cell_rule (RUNBOOK 14 addendum, v13 #219): the
    # comparator for a cell-count gate must be built independently of the
    # component it audits
    exp_keys = []
    for _m in cells_meta:
        _pm = tuple(_m["perm"])
        _is_equi = all(s3_link_perm(_pi) is not None and
                       s3_slot_perm(_pi)[_pm[_k]] == _pm[s3_link_perm(_pi)[_k]]
                       for _pi in S3_ELEMS for _k in range(NV))
        _is_lex = (_pm == tuple(SLOTS3.index(s) for s in sym_index(D3)))
        if _is_equi or _is_lex:
            exp_keys.append(_m["key"])
    for _d in ("q->counts", "counts->q"):
        _c = next((m["key"] for m in cells_meta if m["direction"] == _d and
                   all(v == 0 for v in m["fix_dims"].values())), None)
        _e = next((m["key"] for m in cells_meta if m["direction"] == _d and
                   m["fix_dims"][pref] == 0 and m["meets_at_7"]), None)
        for _k in (_c, _e):
            if _k is not None:
                exp_keys.append(_k)
    exp_unique = []
    for _k in exp_keys:
        if _k not in exp_unique:
            exp_unique.append(_k)
    census_rule_reproduces = (list(census_keys) == exp_unique)
    say(f"  the DECLARED CENSUS CELLS, by the rule stated before any fixture "
        f"truth: {len(census_cells)} (computed)")
    for m in census_cells:
        say(f"     {m['role']:7s} {m['direction']:11s} slots "
            f"{[str(SLOTS3[i]) for i in m['perm']]}  dim fix(E) "
            f"{ {p: m['fix_dims'][p] for p in sweep_primes()} }")
    g15 = gate("G15", "THE CENSUS CELLS ARE CHOSEN BY A DECLARED RULE, NOT BY "
               "A VERDICT, AND THE RULE'S RETURN IS REPRODUCED EXACTLY BY AN "
               "INDEPENDENT REBUILD.  The rule -- every equivariant "
               "identification, HA's own lex ordering, the lex-first "
               "trivial-fixed-space slot order per direction, and the lex-first "
               "slot order that both survives the precheck at the reference "
               "prime and admits the order-3 demanded eigenvalue there -- is "
               "stated in the instrument before any census runs.  Its return is "
               "rebuilt here cell by cell from a SECOND equivariance test that "
               "shares no code with it, and the two agree exactly, so the cell "
               "count is a measured equality and not a lower bound; and the "
               "set contains BOTH module cells and cells of every measured "
               "precheck status, so the census is not run only where it is "
               "expected to be empty",
               census_rule_reproduces and
               len(census_cells) == len(exp_unique) and
               any(m["role"] == "module" for m in census_cells) and
               any(m["trivial_fix_all_primes"] for m in census_cells) and
               any(not m["trivial_fix_all_primes"] for m in census_cells),
               {"census_cells": len(census_cells),
                "independent_rebuild_cells": len(exp_unique),
                "rule_reproduced_exactly": census_rule_reproduces,
                "rows": [{"role": m["role"], "direction": m["direction"],
                          "slots": [str(SLOTS3[i]) for i in m["perm"]],
                          "fix_dims": m["fix_dims"]} for m in census_cells]})
    report("G15", g15, f"{len(census_cells)} declared census cells; "
                       f"independent rebuild agrees {census_rule_reproduces}")
    tables["census_cells"] = [
        {"role": m["role"], "direction": m["direction"],
         "slots": [str(SLOTS3[i]) for i in m["perm"]],
         "fix_dims": m["fix_dims"]} for m in census_cells]
    say("")

    # ---------------------------------------------------------------- 5 ---
    say("------------------------------------------------------------------")
    say("5. ITEM 4 -- THE STILLBORN PRECHECK (structural, FIRST)")
    say("------------------------------------------------------------------")
    progress("precheck")
    synth_ok_E = [[(6 if i == j and i < 3 else (4 if i == j else 0))
                   for j in range(NV)] for i in range(NV)]
    synth_ok_Efr = [[Fr(v) for v in row] for row in synth_ok_E]
    synth_bad_Efr = independent_bad_encoding(7)
    fam7 = {tuple(tuple(r) for r in mat_to_fp(
        encoding_matrix(tuple(m["perm"]), m["direction"]), 7))
        for m in cells_meta}
    bad_is_outside_the_family = (
        tuple(tuple(r) for r in mat_to_fp(synth_bad_Efr, 7)) not in fam7)
    bad_is_invertible = (det_exact(synth_bad_Efr) != 0)
    pk_ok = precheck(fix_delta_size, fix_space_dim(synth_ok_Efr, 7), 7)
    pk_bad = precheck(fix_delta_size, fix_space_dim(synth_bad_Efr, 7), 7)
    audited_Efr = encoding_matrix(tuple(range(NV)), "q->counts")
    pk_audited = precheck(fix_delta_size, fix_space_dim(audited_Efr, 7), 7)
    say(f"  the precheck's two-way calibration at p = 7: a synthetic "
        f"COMPATIBLE pair (dim fix = "
        f"{fix_space_dim(synth_ok_Efr, 7)}) -> "
        f"{'PASS' if pk_ok[0] else 'FAIL'}; a synthetic MISMATCHED pair "
        f"(dim fix = {fix_space_dim(synth_bad_Efr, 7)}) -> "
        f"{'PASS' if pk_bad[0] else 'FAIL'}")
    say(f"     the mismatched arm is INDEPENDENT of the family under audit: "
        f"invertible {bad_is_invertible}, and measured to be none of the "
        f"{len(cells_meta)} covariant encodings ({bad_is_outside_the_family})")
    g16 = gate("G16", "THE STILLBORN PRECHECK IS A MEASUREMENT WITH BOTH "
               "OUTCOMES REACHABLE, AND ITS NEGATIVE ARM IS INDEPENDENT OF THE "
               "OBJECT UNDER AUDIT.  The square forces alpha(fix E) into "
               "fix delta_pi, which is measured to be a single point, so an "
               "INJECTIVE candidate needs |fix E| = 1.  A synthetic pair whose "
               "re-encoding has trivial fixed space PASSES the precheck; a "
               "synthetic INVERTIBLE matrix with a one-dimensional fixed space, "
               "measured NOT to be any of the covariant family's encodings, "
               "FAILS it -- through the same function, so a blinded precheck "
               "cannot pass this gate in either direction and the negative "
               "control is not the candidate it is used to judge",
               pk_ok[0] and (not pk_bad[0]) and bad_is_outside_the_family and
               bad_is_invertible,
               {"synthetic_compatible_fix_dim": fix_space_dim(synth_ok_Efr, 7),
                "synthetic_compatible_passes": pk_ok[0],
                "synthetic_mismatched_fix_dim": fix_space_dim(synth_bad_Efr, 7),
                "synthetic_mismatched_passes": pk_bad[0],
                "mismatched_control_is_invertible": bad_is_invertible,
                "mismatched_control_is_outside_the_covariant_family":
                    bad_is_outside_the_family,
                "the_audited_minimum_candidate_also_fails": not pk_audited[0],
                "fix_delta_size": fix_delta_size})
    report("G16", g16, f"compatible PASS {pk_ok[0]}; mismatched PASS "
                       f"{pk_bad[0]}")

    pre_rows = []
    surv_by_prime = {p: 0 for p in sweep_primes()}
    still_by_prime = {p: 0 for p in sweep_primes()}
    surv_by_class = {"motivated": 0, "generic": 0}
    for m in cells_meta:
        for p in sweep_primes():
            ok, sfe, sfd = precheck(fix_delta_size, m["fix_dims"][p], p)
            if ok:
                surv_by_prime[p] += 1
                surv_by_class["motivated" if m["role"] in ("module", "lex")
                              else "generic"] += 1
            else:
                still_by_prime[p] += 1
    mismatch_computed = 0
    mismatch_rows = 0
    mot_rows = []
    for m in cells_meta:
        if m["role"] in ("module", "lex"):
            row = {"role": m["role"], "direction": m["direction"],
                   "slots": [str(SLOTS3[i]) for i in m["perm"]],
                   "per_prime": {}}
            for p in sweep_primes():
                ok, sfe, sfd = precheck(fix_delta_size, m["fix_dims"][p], p)
                row["per_prime"][p] = {
                    "dim_fix_E": m["fix_dims"][p], "size_fix_E": sfe,
                    "size_fix_delta": sfd, "precheck": "PASS" if ok else
                    "STILLBORN", "mismatch": stillborn_mismatch(sfe, sfd)}
                # the recorded mismatch, rebuilt here from the measured
                # dimension without touching the helper that formats it
                mismatch_rows += 1
                if stillborn_mismatch(sfe, sfd) == \
                        f"{p ** m['fix_dims'][p]} : {fix_delta_size}":
                    mismatch_computed += 1
                mot_rows.append({"cell": m["role"], "direction": m["direction"],
                                 "p": p, "dim_fix_E": m["fix_dims"][p],
                                 "precheck": "PASS" if ok else "STILLBORN"})
            pre_rows.append(row)
    module_all_stillborn = all(
        not precheck(fix_delta_size, m["fix_dims"][p], p)[0]
        for m in cells_meta if m["role"] == "module" for p in sweep_primes())
    any_survivor = any(v > 0 for v in surv_by_prime.values())
    say(f"  {'role':8s}{'direction':12s}{'dim fix(E)':12s}"
        f"{'|fix E| : |fix delta|':24s}precheck")
    for row in pre_rows:
        pp = row["per_prime"][pref]
        say(f"  {row['role']:8s}{row['direction']:12s}"
            f"{pp['dim_fix_E']:<12d}{pp['mismatch']:24s}{pp['precheck']}"
            f"   (at p = 7)")
    say(f"  over the whole covariant family, per prime -- survivors: "
        f"{ {p: surv_by_prime[p] for p in sweep_primes()} }")
    say(f"                                     stillborn: "
        f"{ {p: still_by_prime[p] for p in sweep_primes()} }")
    g17 = gate("G17", "THE PRECHECK IS RUN FIRST, PER CANDIDATE, OVER THE WHOLE "
               "COVARIANT FAMILY, AND ITS MISMATCH IS COMPUTED.  BOTH "
               "S_3-EQUIVARIANT identifications -- the pin's minimum candidate "
               "-- are STILLBORN at every declared prime, with the mismatch "
               "recorded as |fix E| : |fix delta| = p^3 : 1 at the natural "
               "identification and p^2 : 1 at the swap identification; and the "
               "SET-LEVEL covariant family is measured to contain survivors at "
               "every declared prime, so the precheck is not a wall that "
               "everything hits.  The per-prime counts are cell-complete",
               module_all_stillborn and any_survivor and
               mismatch_rows > 0 and mismatch_computed == mismatch_rows and
               all(completeness([surv_by_prime[p], still_by_prime[p]], ncells)
                   for p in sweep_primes()),
               {"module_candidates_all_stillborn": module_all_stillborn,
                "survivors_per_prime": surv_by_prime,
                "stillborn_per_prime": still_by_prime,
                "mismatch_rows": mismatch_rows,
                "mismatches_matching_the_recomputed_value": mismatch_computed,
                "cells": ncells, "rows": pre_rows,
                "cell_complete": all(
                    completeness([surv_by_prime[p], still_by_prime[p]], ncells)
                    for p in sweep_primes())})
    report("G17", g17, f"module cells all stillborn {module_all_stillborn}; "
                       f"survivors at p={pref}: {surv_by_prime[pref]}/{ncells}")
    tables["precheck"] = {"rows": pre_rows, "survivors": surv_by_prime,
                          "stillborn": still_by_prime}
    quals["precheck_survivors_at_p7"] = qualifier_value(
        "precheck_survivors_at_p7", surv_by_prime[pref])

    # --- the MOTIVATED sub-family, censused separately --------------------
    mot_cells = len(pre_rows)
    mot_total = len(mot_rows)
    mot_surv = motivated_precheck_survivors(mot_rows)
    generic_cells = ncells - mot_cells
    ident_qual = identification_qualifier(mot_surv, surv_by_class["generic"])
    # the motivated sub-family's OWN census emptiness, measured here rather
    # than assumed from the covariant closure's
    mot_crit_rows = [(m, p, ordpi) for m in cells_meta
                     if m["role"] in ("module", "lex")
                     for p in sweep_primes() for ordpi in (2, 3)]
    mot_crit_hits = sum(
        1 for (m, p, ordpi) in mot_crit_rows
        if order_criterion(encoding_matrix(tuple(m["perm"]), m["direction"]),
                           p, ordpi))
    mot_census_empty = (mot_crit_hits == 0)
    # calibrated the other way through the same call: the synthetic encoding
    # that DOES satisfy the criterion is counted as a hit by it
    mot_census_probe = order_criterion(synth_ok_Efr, pref, 3)
    verdict_motivated = derive_verdict(mot_surv > 0, mot_census_empty,
                                       True, True, d3_constructed)
    say(f"  THE MOTIVATED SUB-FAMILY, censused separately: the "
        f"{len(equi)} S_3-equivariant identifications and HA's own sym_index "
        f"ordering, both directions = {mot_cells} cells x "
        f"{len(sweep_primes())} primes = {mot_total} rows")
    say(f"     precheck survivors among them            : {mot_surv} of "
        f"{mot_total}")
    say(f"     precheck survivors that are GENERIC cells: "
        f"{surv_by_class['generic']} (the {generic_cells} identifications that "
        f"are an arbitrary relabelling of the six metric slots)")
    say(f"     the identification qualifier (computed)  : {ident_qual}")
    say(f"     their own census, measured separately    : {mot_crit_hits} of "
        f"{len(mot_crit_rows)} rows satisfy the order criterion")
    say(f"     restricted to the motivated sub-family, this instrument's own "
        f"pre-registered outcome is {verdict_motivated}")
    g39 = gate("G39", "THE FOUND HALF IS NAMED BY THE IDENTIFICATION CLASS OF "
               "ITS SURVIVORS, MEASURED.  The identifications with a stated "
               "motivation -- the S_3-EQUIVARIANT ones, whose number is "
               "computed, and HA's own sym_index ordering, in both directions "
               "-- are censused as their own sub-family: every one of them is "
               "STILLBORN at every declared prime, so the precheck's survivors "
               "are exactly the identifications that are an arbitrary "
               "relabelling of the six metric slots.  The FOUND half's "
               "qualifier is DERIVED here from those two counts, and the "
               "verdict this instrument returns when it is restricted to the "
               "motivated sub-family is derived by the same function that "
               "returns the covariant-closure verdict, from that sub-family's "
               "OWN census -- run here over its own rows and calibrated the "
               "other way through the same counting call, which scores the "
               "synthetic encoding that does satisfy the criterion as a hit",
               mot_cells == 2 * len(equi) + 2 and mot_total ==
               mot_cells * len(sweep_primes()) and mot_surv == 0 and
               surv_by_class["generic"] == sum(surv_by_prime.values()) and
               ident_qual == "FOUND-ONLY-AT-UNMOTIVATED-IDENTIFICATIONS" and
               len(mot_crit_rows) == mot_cells * len(sweep_primes()) * 2 and
               mot_census_empty and mot_census_probe and
               verdict_motivated == "RSQ-NO-COMPATIBLE-SQUARE",
               {"motivated_cells": mot_cells, "motivated_rows": mot_total,
                "motivated_criterion_rows": len(mot_crit_rows),
                "motivated_criterion_hits": mot_crit_hits,
                "counting_call_scores_the_synthetic_positive_control":
                    mot_census_probe,
                "motivated_precheck_survivors": mot_surv,
                "generic_cells": generic_cells,
                "generic_precheck_survivors": surv_by_class["generic"],
                "identification_qualifier": ident_qual,
                "verdict_at_the_motivated_sub_family": verdict_motivated,
                "rows": mot_rows})
    report("G39", g39, f"motivated survivors {mot_surv}/{mot_total}; "
                       f"qualifier {ident_qual}")
    tables["motivated_sub_family"] = {"cells": mot_cells, "rows": mot_rows,
                                      "survivors": mot_surv,
                                      "qualifier": ident_qual,
                                      "verdict": verdict_motivated}
    say("")

    # ---------------------------------------------------------------- 6 ---
    say("------------------------------------------------------------------")
    say("6. ITEM 5 -- THE STRENGTHENED TEST FOR THE SURVIVORS")
    say("------------------------------------------------------------------")
    progress("order criterion")
    crit_hits = {p: 0 for p in sweep_primes()}
    crit_tot = {p: 0 for p in sweep_primes()}
    disagree = 0
    crit_index = drop_row_criterion(
        [(m, p, ordpi) for m in cells_meta for p in sweep_primes()
         for ordpi in (2, 3)])
    crit_rows_forced = ncells * len(sweep_primes()) * 2
    crit_not_hits = 0
    crit_hit_rows = []
    crit_by_dir = {"q->counts": [0, 0], "counts->q": [0, 0]}
    for (m, p, ordpi) in crit_index:
        E = encoding_matrix(tuple(m["perm"]), m["direction"])
        crit_tot[p] = crit_tot.get(p, 0) + 1
        a = order_criterion(E, p, ordpi)
        b = order_criterion_polynomial(E, p, ordpi)
        if a != b:
            disagree += 1
        crit_by_dir[m["direction"]][0] += 1
        if a:
            crit_hits[p] = crit_hits.get(p, 0) + 1
            crit_hit_rows.append((m, p, ordpi))
            crit_by_dir[m["direction"]][1] += 1
        else:
            crit_not_hits += 1
    crit_total_cells = len(crit_index)
    crit_total_hits = sum(crit_hits.values())
    say(f"  THE ORDER CRITERION (I - E)^ord(pi) = I, over the whole covariant "
        f"family x every declared prime x both nontrivial wing-symmetry "
        f"orders: {crit_total_hits} of {crit_total_cells} cells satisfy it")
    say(f"  the matrix-power writing and the polynomial writing -- one "
        f"condition in two encodings, related by the identity "
        f"(I-E)^3 - I = -E(E^2 - 3E + 3I) -- disagree at "
        f"{disagree} of {crit_total_cells} rows")
    synth_crit = order_criterion(synth_ok_Efr, 7, 3)
    synth_crit_poly = order_criterion_polynomial(synth_ok_Efr, 7, 3)
    say(f"  the criterion's positive control: the synthetic encoding "
        f"diag(6,6,6,4,4,4) at p = 7 satisfies it -- matrix route "
        f"{synth_crit}, polynomial route {synth_crit_poly}")
    say(f"  the DIRECTION convention is swept, not chosen: rows and hits per "
        f"direction {crit_by_dir}")
    g18 = gate("G18", "THE ORDER CRITERION IS DERIVED, REDUNDANTLY ENCODED, AND "
               "REACHABLE IN BOTH DIRECTIONS.  S1a and S1b make the image "
               "an abelian Sigma-stable subgroup on which delta_pi acts as "
               "I - rho; S3 makes alpha an isomorphism, so rho = I - alpha E "
               "alpha^-1 and rho^ord(pi) = I, i.e. (I - E)^ord(pi) = I.  The "
               "matrix-power writing and the polynomial writing (E = 2I at an "
               "involution, E^2 - 3E + 3I = 0 at an order-3 wing symmetry, "
               "whose roots are exactly 1 - omega) agree at every row -- these "
               "are ONE condition in two encodings, related by the identity "
               "(I-E)^3 - I = -E(E^2 - 3E + 3I), and the agreement is a "
               "redundant-encoding check, not a second route; and the "
               "criterion is SATISFIED by a synthetic encoding, so it is "
               "not a condition nothing can meet.  The DIRECTION convention -- "
               "the one orientation choice this instrument makes -- is SWEPT "
               "rather than chosen: both directions carry the same number of "
               "rows and the same number of hits, so the verdict cannot be an "
               "artefact of which way the readout is read (RUNBOOK 14)",
               disagree == 0 and crit_total_cells > 0 and synth_crit and
               synth_crit_poly and
               crit_by_dir["q->counts"][0] == crit_by_dir["counts->q"][0] and
               crit_by_dir["q->counts"][1] == crit_by_dir["counts->q"][1],
               {"cells": crit_total_cells, "cells_satisfying": crit_total_hits,
                "rows_and_hits_per_direction": crit_by_dir,
                "per_prime": crit_hits, "route_disagreements": disagree,
                "synthetic_positive_control_matrix_route": synth_crit,
                "synthetic_positive_control_polynomial_route":
                    synth_crit_poly})
    report("G18", g18, f"{crit_total_hits}/{crit_total_cells} satisfy; "
                       f"disagreements {disagree}; positive control "
                       f"{synth_crit}")

    # --- THE READOUT-PROFILE THEOREM -------------------------------------
    progress("the readout-profile theorem")
    prof_counts = {}
    row0_unit = 0
    det_pm8 = 0
    thm_rows = []
    thm_admissible = []
    ext_rows = 0
    ext_admissible = []
    ext_gcds = []
    for perm in slot_orders():
        A = integer_readout(perm)
        if A is None:
            continue
        for pr in row_profiles(A):
            prof_counts[pr] = prof_counts.get(pr, 0) + 1
        k = slot_position(perm, (0, 0))
        r0 = A[0]
        if k is not None and all(r0[i] == (1 if i == k else 0)
                                 for i in range(NV)):
            row0_unit += 1
        if abs(det_exact([[Fr(v) for v in row] for row in A])) == 8:
            det_pm8 += 1
        for direction in ("q->counts", "counts->q"):
            for ordpi in (2, 3):
                v = criterion_row0_witness(A, k, direction, ordpi)
                adm = admissible_primes_of_witness(v, floor_prime)
                thm_rows.append({"direction": direction, "ord": ordpi,
                                 "witness_gcd": gcd_of(v),
                                 "admissible_primes": adm})
                thm_admissible += adm
                ext_rows += 1
                Mid = criterion_identity(A, direction, ordpi)
                ext_admissible += all_prime_hits(Mid, floor_prime)
                ext_gcds.append(gcd_of(x for row_ in Mid for x in row_))
    thm_rows_forced = len(slot_orders()) * 2 * 2
    thm_holds = (len(thm_admissible) == 0)
    # the theorem's decision function, calibrated the other way: a synthetic
    # readout row carrying the FORBIDDEN profile (one 1 and one 2, nothing
    # else) makes the same machinery report p = 7 as admissible
    Asyn = [[0] * NV for _ in range(NV)]
    Asyn[0][1] = 1
    Asyn[1][0] = 2
    Asyn[1][1] = 1
    syn_adm = admissible_primes_of_witness(
        criterion_row0_witness(Asyn, 1, "counts->q", 3), floor_prime)
    syn_profile = tuple(sorted(Asyn[1]))
    # THE THEOREM'S INDEPENDENCE OF THE CRITERION, MEASURED STRUCTURALLY: the
    # whole witness sweep is recomputed with the names of BOTH writings of the
    # order criterion unbound in the module namespace, so a theorem that
    # reached the criterion through any call could not answer at all
    _G = globals()
    _saved_oc = _G.pop("order_criterion")
    _saved_op = _G.pop("order_criterion_polynomial")
    thm_probe_error = None
    thm_unbound = []
    try:
        for perm in slot_orders():
            Au = integer_readout(perm)
            if Au is None:
                continue
            ku = slot_position(perm, (0, 0))
            for direction in ("q->counts", "counts->q"):
                for ordpi in (2, 3):
                    thm_unbound += admissible_primes_of_witness(
                        criterion_row0_witness(Au, ku, direction, ordpi),
                        floor_prime)
    except NameError as exc:
        thm_unbound, thm_probe_error = None, str(exc)
    finally:
        _G["order_criterion"] = _saved_oc
        _G["order_criterion_polynomial"] = _saved_op
    thm_independent = (thm_probe_error is None and
                       thm_unbound == thm_admissible)
    profiles_measured = sorted(prof_counts)
    excluded_by_the_cap = [p for p in sweep_primes()
                           if p not in carrier_primes()]
    say(f"  THE READOUT-PROFILE THEOREM.  Every row of the readout, at every "
        f"slot order, has one of exactly {len(prof_counts)} profiles: "
        f"{ {str(k2): prof_counts[k2] for k2 in profiles_measured} }")
    say(f"     row 0 is the unit vector e_k (k = the position of the metric "
        f"slot (0,0)) at {row0_unit} of {len(slot_orders())} slot orders; "
        f"|det| = 8 at {det_pm8} of {len(slot_orders())}")
    say(f"     over {len(thm_rows)} (slot order, direction, wing order) "
        f"triples the criterion forces p | gcd(witness), and the primes "
        f">= {floor_prime} admitted by any witness are: "
        f"{sorted(set(thm_admissible))}")
    say(f"     the same machinery on a SYNTHETIC readout row of the forbidden "
        f"profile {list(syn_profile)}: admissible primes {syn_adm}")
    say(f"     the theorem's independence of the F_p criterion, measured "
        f"structurally: the whole witness sweep recomputed with BOTH writings "
        f"of the order criterion UNBOUND returns the same answer "
        f"({thm_independent}, error {thm_probe_error})")
    say(f"     so the census is EMPTY at every prime p >= {floor_prime} -- "
        f"including the {len(excluded_by_the_cap)} primes "
        f"{excluded_by_the_cap} at which the deformation carrier is not built, "
        f"which the criterion decides without it")
    g40 = gate("G40", "THE EMPTINESS IS A THEOREM, NOT A CENSUS: THE "
               "READOUT-PROFILE ARGUMENT, DERIVED HERE FROM THE READOUT'S OWN "
               "INTEGER STRUCTURE.  Every row of the record<->metric readout is "
               "a link's row in some column order, so its entries are one of "
               "exactly two multisets -- (0,0,0,0,0,1) for an axis link, "
               "(0,0,0,1,1,2) for a diagonal link -- and row 0 is therefore the "
               "unit vector e_k, k the position the identification gives the "
               "slot (0,0).  det = +-8 makes E invertible at every odd prime, "
               "so the criterion is equivalent to a polynomial identity in the "
               "INTEGER readout; read at row 0, with row_0(A^2) = row_k(A), it "
               "forces p to divide the gcd of an explicit integer witness.  "
               "Every witness gcd is measured to admit NO prime >= 5, so the "
               "criterion fails at EVERY such prime -- at every slot order, "
               "both directions, both wing-symmetry orders, and at the primes "
               "the carrier build cap excludes.  The decision function is "
               "calibrated the other way through the same call: a synthetic "
               "readout row of the forbidden profile (0,0,0,0,1,2) makes it "
               "report p = 7 admissible.  And the theorem is measured to be a "
               "route INDEPENDENT of the F_p sweep, structurally rather than "
               "by bookkeeping: the whole witness sweep is recomputed with the "
               "names of BOTH writings of the order criterion unbound in the "
               "module namespace, so a theorem that reached the criterion "
               "through any call could not answer, and it must both answer and "
               "return the same admitted-prime set",
               len(prof_counts) == 2 and thm_independent and
               set(profiles_measured) == {(0, 0, 0, 0, 0, 1),
                                          (0, 0, 0, 1, 1, 2)} and
               row0_unit == len(slot_orders()) and
               det_pm8 == len(slot_orders()) and
               len(thm_rows) == thm_rows_forced and thm_holds and
               syn_adm == [7] and syn_profile == (0, 0, 0, 0, 1, 2) and
               all(p >= floor_prime for p in excluded_by_the_cap),
               {"row_profiles": {str(k2): prof_counts[k2]
                                 for k2 in profiles_measured},
                "row_zero_is_a_unit_vector": row0_unit,
                "slot_orders": len(slot_orders()),
                "determinant_is_plus_or_minus_8": det_pm8,
                "witness_triples": len(thm_rows),
                "witness_triples_forced": thm_rows_forced,
                "primes_admitted_by_any_witness":
                    sorted(set(thm_admissible)),
                "witness_gcds_seen": sorted({r["witness_gcd"]
                                             for r in thm_rows}),
                "synthetic_forbidden_profile_admits": syn_adm,
                "independent_of_the_Fp_criterion_with_its_names_unbound":
                    thm_independent,
                "unbound_probe_error": thm_probe_error,
                "primes_excluded_by_the_carrier_build_cap":
                    excluded_by_the_cap,
                "floor_prime": floor_prime})
    report("G40", g40, f"profiles {len(prof_counts)}; witnesses "
                       f"{len(thm_rows)}; primes admitted "
                       f"{sorted(set(thm_admissible))}; synthetic control "
                       f"{syn_adm}")
    tables["profile_theorem"] = {
        "profiles": {str(k2): prof_counts[k2] for k2 in profiles_measured},
        "witness_triples": len(thm_rows),
        "primes_admitted": sorted(set(thm_admissible)),
        "synthetic_control_admits": syn_adm}

    # --- the EXACT extension of the sweep to every prime at once ----------
    ident_agree = 0
    ident_rows = 0
    for m in census_cells:
        A = integer_readout(tuple(m["perm"]))
        for direction in ("q->counts", "counts->q"):
            E = encoding_matrix(tuple(m["perm"]), direction)
            if A is None or E is None:
                continue
            for p in sweep_primes():
                for ordpi in (2, 3):
                    M = criterion_identity(A, direction, ordpi)
                    ident_rows += 1
                    if order_criterion(E, p, ordpi) == all(
                            v % p == 0 for row in M for v in row):
                        ident_agree += 1
    ext_rows = extension_scope(ext_rows)
    ext_admissible_set = sorted(set(ext_admissible))
    say(f"  THE EXACT EXTENSION.  The same identity read as an INTEGER matrix "
        f"decides every prime at once: over {ext_rows} (slot order, direction, "
        f"wing order) triples the primes >= {floor_prime} at which the whole "
        f"identity can vanish are {ext_admissible_set} -- so the 0 of "
        f"{crit_total_cells} measured at the {len(sweep_primes())} declared "
        f"primes is 0 at EVERY prime")
    say(f"  the integer identity and the F_p criterion agree at "
        f"{ident_agree} of {ident_rows} calibration rows")
    # THE WIDE CORROBORATION CENSUS: the same integer identities, swept
    # against every prime from the floor to the declared ceiling
    wide_ceiling = DECL["wide_corroboration_prime_ceiling"]
    wide_primes = extended_primes(floor_prime, wide_ceiling)
    wide_rows = 0
    wide_hits = 0
    for g_ in ext_gcds:
        for p_ in wide_primes:
            wide_rows += 1
            if g_ == 0 or g_ % p_ == 0:
                wide_hits += 1
    wide_forced = ncells * len(wide_primes) * 2
    say(f"  THE WIDE CORROBORATION CENSUS: the same identities swept against "
        f"every one of the {len(wide_primes)} primes from {wide_primes[0]} to "
        f"{wide_primes[-1]} -- {wide_rows} (cell, prime, wing order) rows, "
        f"{wide_hits} of them satisfying the criterion")
    g41 = gate("G41", "THE SWEEP'S EXACT EXTENSION, AND ITS CALIBRATION "
               "AGAINST THE FIELD COMPUTATION.  The criterion's polynomial "
               "identity has integer coefficients in the integer readout, so "
               "the primes at which it can hold are exactly the primes "
               "dividing the gcd of its entries: computing that gcd at every "
               "(slot order, direction, wing order) triple extends the "
               "20,160-row sweep from the seven declared primes to EVERY "
               "prime, with the same answer.  The extension is calibrated "
               "against the field computation itself -- the integer identity "
               "and (I - E)^ord = I over F_p are measured to agree at every "
               "calibration row -- so the extension is not a different claim.  "
               "The same identities are then swept explicitly against every "
               "prime from the floor to the declared ceiling, row by row, as a "
               "WIDE corroboration census whose row count is checked against "
               "the product the declarations force",
               ext_rows == thm_rows_forced and len(ext_admissible_set) == 0 and
               ident_rows > 0 and ident_agree == ident_rows and
               wide_hits == 0 and wide_rows == wide_forced and
               wide_primes[0] == floor_prime and
               wide_primes[-1] == wide_ceiling,
               {"triples": ext_rows, "triples_forced": thm_rows_forced,
                "primes_admitted_at_any_triple": ext_admissible_set,
                "calibration_rows": ident_rows,
                "calibration_agreements": ident_agree,
                "wide_census_primes": len(wide_primes),
                "wide_census_prime_range": [wide_primes[0], wide_primes[-1]],
                "wide_census_rows": wide_rows,
                "wide_census_rows_forced": wide_forced,
                "wide_census_hits": wide_hits})
    report("G41", g41, f"{ext_rows} triples; primes admitted "
                       f"{ext_admissible_set}; calibration {ident_agree}/"
                       f"{ident_rows}; wide census {wide_hits}/{wide_rows}")

    pre_surv_cells = sum(1 for m in cells_meta for p in sweep_primes()
                         if precheck(fix_delta_size, m["fix_dims"][p], p)[0])
    crit_cells_set = crit_total_hits
    # the containment ITSELF, as a set predicate: every (cell, prime) at which
    # the criterion holds at some wing order must survive the precheck
    contain_viol = 0
    contain_witnesses = 0
    for (m, p, ordpi) in crit_hit_rows:
        contain_witnesses += 1
        if not precheck(fix_delta_size, m["fix_dims"][p], p)[0]:
            contain_viol += 1
    # with zero witnesses the containment is VACUOUS at the family; the
    # implication is exercised on the one non-vacuous instance available
    synth_pre = precheck(fix_delta_size, fix_space_dim(synth_ok_Efr, 7), 7)[0]
    synth_implication = (not synth_crit) or synth_pre
    say(f"  the criterion's relation to the precheck: {crit_cells_set} of "
        f"{crit_total_cells} (cell, prime, order) rows satisfy the criterion "
        f"against {pre_surv_cells} of {ncells * len(sweep_primes())} "
        f"(cell, prime) pairs that survive the precheck; the containment is "
        f"violated at {contain_viol} of {contain_witnesses} witnesses "
        f"(VACUOUS at this family) and holds at the synthetic instance "
        f"({synth_implication})")
    g19 = gate("G19", "THE ORDER CRITERION SUBSUMES THE PRECHECK -- WHAT IS "
               "MEASURED, STATED AS WHAT IS MEASURED.  (I - E)^ord = I forces "
               "I - E invertible, hence dim ker(E - I) = 0; that implication is "
               "a theorem, and what this gate measures is (a) the two counts "
               "against their OWN denominators -- criterion-satisfying rows out "
               "of the swept rows, precheck survivors out of the (cell, prime) "
               "pairs -- (b) the implication itself as a set predicate, cell by "
               "cell, which at this family has ZERO witnesses and is therefore "
               "VACUOUS, and (c) the implication exercised on the one "
               "non-vacuous instance available, the synthetic encoding that "
               "satisfies the criterion and is measured to have trivial fixed "
               "space.  The precheck is the structural SHADOW of the census "
               "criterion, exactly as the LCB lesson predicts",
               subsumption_holds(crit_cells_set, pre_surv_cells) and
               contain_viol == 0 and synth_implication and synth_crit and
               synth_pre and crit_cells_set < pre_surv_cells,
               {"rows_satisfying_the_criterion": crit_cells_set,
                "rows_swept": crit_total_cells,
                "cell_prime_pairs_surviving_the_precheck": pre_surv_cells,
                "cell_prime_pairs_swept": ncells * len(sweep_primes()),
                "containment_witnesses": contain_witnesses,
                "containment_violations": contain_viol,
                "containment_is_vacuous_at_this_family":
                    contain_witnesses == 0,
                "synthetic_instance_satisfies_the_criterion": synth_crit,
                "synthetic_instance_survives_the_precheck": synth_pre})
    report("G19", g19, f"criterion {crit_cells_set}/{crit_total_cells}; "
                       f"precheck {pre_surv_cells}/"
                       f"{ncells * len(sweep_primes())}; containment "
                       f"violations {contain_viol} of {contain_witnesses}")
    tables["order_criterion"] = {"per_prime_hits": crit_hits,
                                 "per_prime_cells": crit_tot,
                                 "route_disagreements": disagree}

    progress("census routes")
    subs_cache = {}
    for p in sweep_primes():
        subs = cyclic_subgroups_of_order(GC, p)
        subs_cache[p] = subs
    norm_rows = []
    for p in sweep_primes():
        for pi in S3_ELEMS:
            if pi == (0, 1, 2):
                continue
            data = []
            for grp, g in subs_cache[p].items():
                s = conjugation_exponent(pi, g, p)
                data.append((g, s))
            nrm = [(g, s) for (g, s) in data if s is not None]
            spec = {}
            for (_g, s) in nrm:
                spec[s] = spec.get(s, 0) + 1
            norm_rows.append({"p": p, "pi": list(pi), "ord": pord(SIGMA[pi]),
                              "subgroups": len(data), "normalised": len(nrm),
                              "exponent_spectrum":
                                  {str(k): spec[k] for k in sorted(spec)},
                              "demanded_eigenvalues":
                                  sorted({(1 - s) % p for (_g, s) in nrm})})
    say(f"  {'p':4s}{'wing pi':11s}{'ord':5s}{'subgroups':11s}"
        f"{'normalised':12s}{'exponents s':16s}demanded 1-s")
    for r in norm_rows:
        if r["normalised"]:
            say(f"  {r['p']:<4d}{str(r['pi']):11s}{r['ord']:<5d}"
                f"{r['subgroups']:<11d}{r['normalised']:<12d}"
                f"{str(r['exponent_spectrum']):16s}{r['demanded_eigenvalues']}")
    tables["normalisation"] = norm_rows

    subs_by_pi = {}
    for p in sweep_primes():
        for pi in S3_ELEMS:
            if pi == (0, 1, 2):
                continue
            data = [(g, conjugation_exponent(pi, g, p))
                    for g in subs_cache[p].values()]
            subs_by_pi[(p, pi)] = data
    census_rows = []
    census_disagree = 0
    for m in census_cells:
        E = encoding_matrix(tuple(m["perm"]), m["direction"])
        ckey = (tuple(m["perm"]), m["direction"])
        for p in sweep_primes():
            for pi in S3_ELEMS:
                if pi == (0, 1, 2):
                    continue
                data = subs_by_pi[(p, pi)]
                nrm = [(g, s) for (g, s) in data if s is not None]
                ra, per = route_a_count(E, p, pi, nrm, pord(SIGMA[pi]))
                rb = route_b_count(E, p, pi, data, pord(SIGMA[pi]), ckey)
                if ra != rb:
                    census_disagree += 1
                ok, _sfe, _sfd = precheck(fix_delta_size, m["fix_dims"][p], p)
                census_rows.append({
                    "role": m["role"], "direction": m["direction"],
                    "slots": [str(SLOTS3[i]) for i in m["perm"]],
                    "p": p, "pi": list(pi), "ord": pord(SIGMA[pi]),
                    "precheck": "PASS" if ok else "STILLBORN",
                    "route_A": ra, "route_B": rb,
                    "detail": per,
                    "cardinality_admits_injectivity": p ** NV <= len(GC),
                    "the_order_criterion_at_this_row":
                        order_criterion(E, p, pord(SIGMA[pi]))})
        progress(f"  census cell {m['role']}/{m['direction']}")
    census_rows = drop_row_census(census_rows)
    census_rows_forced = len(census_cells) * len(sweep_primes()) * 5
    live_s1ab = sum(1 for r in census_rows if r["route_A"] > 1)
    live_full = sum(1 for r in census_rows
                    if r["the_order_criterion_at_this_row"])
    card_admits = sum(1 for r in census_rows
                      if r["cardinality_admits_injectivity"])
    vp_gc = {p: legendre_exponent(NLAB - 1, p) for p in sweep_primes()}
    rank1_forced = all(v <= 1 for v in vp_gc.values())
    say(f"  the census at {len(census_cells)} declared cells x "
        f"{len(sweep_primes())} primes x 5 nontrivial wing symmetries = "
        f"{len(census_rows)} rows")
    say(f"  rows whose S1a+S1b census is NON-EMPTY (a candidate exists at the "
        f"square and the homomorphism clause): {live_s1ab} of "
        f"{len(census_rows)}")
    say(f"  rows admitting an INJECTIVE candidate: {live_full} of "
        f"{len(census_rows)} -- this column is the ORDER CRITERION restricted "
        f"to the declared cells, a coverage check on the census and not an "
        f"independent source, and it is FORCED twice over: no row has "
        f"p^6 <= |G_C| ({card_admits} of {len(census_rows)}), and v_p(|G_C|) "
        f"<= 1 at every declared prime ({rank1_forced}), so every additive "
        f"candidate at this arena has image of order at most p")
    say(f"  route A vs route B disagreements: {census_disagree} of "
        f"{len(census_rows)}")
    g20 = gate("G20", "THE CENSUS IS COMPUTED BY TWO ROUTES AND THEY AGREE AT "
               "EVERY ROW.  Route A solves ker(E^T - (1-s)I) by Gaussian "
               "elimination and multiplies by the MEASURED count of normalised "
               "subgroups; route B enumerates every cyclic subgroup of order p, "
               "builds its delta-exponent table from PERMUTATIONS with no "
               "linear algebra in it, and enumerates every covector "
               "projectively with the measured redundancy restored.  What THIS "
               "gate measures is the agreement and the invocation counters; "
               "that the two routes are independent COMPUTATIONS is measured "
               "structurally at G42, not self-reported here",
               census_disagree == 0 and
               ROUTE_CALLS["A"] > 0 and ROUTE_CALLS["B"] > 0 and
               CANDIDATE_EVALS[0] > 0,
               {"rows": len(census_rows), "disagreements": census_disagree,
                "route_calls": dict(ROUTE_CALLS),
                "candidate_evaluations_counted": CANDIDATE_EVALS[0]})
    report("G20", g20, f"{census_disagree} disagreements; route calls "
                       f"A={ROUTE_CALLS['A']} B={ROUTE_CALLS['B']}")

    # route independence, measured STRUCTURALLY: route B is re-run with the
    # name `route_a_count` unbound in the module namespace, so a route B that
    # reaches route A at all -- with or without a counter -- cannot return
    probe_cell = census_cells[0]
    probe_p = sweep_primes()[0]
    probe_pi = (0, 2, 1)
    Eprobe = encoding_matrix(tuple(probe_cell["perm"]), probe_cell["direction"])
    pkey = (tuple(probe_cell["perm"]), probe_cell["direction"])
    rb_before = route_b_count(Eprobe, probe_p, probe_pi,
                              subs_by_pi[(probe_p, probe_pi)],
                              pord(SIGMA[probe_pi]), pkey)
    _G = globals()
    _saved = _G.pop("route_a_count")
    probe_error = None
    try:
        rb_unbound = route_b_count(Eprobe, probe_p, probe_pi,
                                   subs_by_pi[(probe_p, probe_pi)],
                                   pord(SIGMA[probe_pi]), pkey)
    except NameError as exc:
        rb_unbound, probe_error = None, str(exc)
    finally:
        _G["route_a_count"] = _saved
    route_structurally_independent = (probe_error is None and
                                      rb_unbound == rb_before)
    say(f"  route independence, measured structurally: route B re-evaluated "
        f"with route A's name UNBOUND returns {rb_unbound} against "
        f"{rb_before} (error {probe_error}); taint counter "
        f"{ROUTE_CALLS['taint']}")
    g42 = gate("G42", "ROUTE INDEPENDENCE IS MEASURED, NOT SELF-REPORTED.  A "
               "counter that a route must increment to declare itself tainted "
               "measures only the routes that agree to be counted.  Here route "
               "B is re-evaluated with the NAME of route A removed from the "
               "module namespace: a route B that reaches route A -- through a "
               "counted call or a silent one -- raises instead of answering, "
               "and the gate requires both that no error was raised and that "
               "the answer is unchanged.  The taint counter is retained as a "
               "disclosure",
               route_structurally_independent and ROUTE_CALLS["taint"] == 0 and
               rb_before > 0,
               {"route_b_answer": rb_before,
                "route_b_answer_with_route_a_unbound": rb_unbound,
                "error_raised": probe_error,
                "structurally_independent": route_structurally_independent,
                "taint_counter": ROUTE_CALLS["taint"]})
    report("G42", g42, f"route B with route A unbound: {rb_unbound} vs "
                       f"{rb_before}; error {probe_error}")

    calib_cell = census_cells[0]
    Ecal = encoding_matrix(tuple(calib_cell["perm"]), calib_cell["direction"])
    pcal = 5 if 5 in sweep_primes() else sweep_primes()[0]
    subs_cal = subs_by_pi[(pcal, (0, 2, 1))]
    rb_proj = route_b_count(Ecal, pcal, (0, 2, 1), subs_cal, 2,
                            (tuple(calib_cell["perm"]),
                             calib_cell["direction"]))
    rb_full = route_b_full_count(Ecal, pcal, (0, 2, 1), subs_cal)
    say(f"  route B's redundancy calibration at p = {pcal}: the projective "
        f"enumeration returns {rb_proj}, the FULL enumeration over all "
        f"{pcal ** NV} covectors returns {rb_full}")
    g21 = gate("G21", "ROUTE B's PROJECTIVE ENUMERATION IS CALIBRATED AGAINST "
               "THE FULL ONE.  At a declared cell and prime the covector space "
               "is enumerated in FULL -- every one of p^6 covectors, with no "
               "redundancy quotient -- and the count agrees with the "
               "projective enumeration's, so the declared redundancy p-1 is "
               "measured rather than assumed",
               rb_proj == rb_full,
               {"cell": {"role": calib_cell["role"],
                         "direction": calib_cell["direction"]},
                "prime": pcal, "projective_count": rb_proj,
                "full_count": rb_full, "covectors_enumerated": pcal ** NV})
    report("G21", g21, f"projective {rb_proj} vs full {rb_full}")

    lit_rows = []
    lit_instances = []
    for m in census_cells:
        for p in [q for q in (5, 7) if q in sweep_primes()]:
            for pi in S3_ELEMS:
                if pi == (0, 1, 2):
                    continue
                nrm = [(g, s) for (g, s) in subs_by_pi[(p, pi)]
                       if s is not None]
                if not nrm:
                    continue
                E = encoding_matrix(tuple(m["perm"]), m["direction"])
                Ep = mat_to_fp(E, p)
                ker = kernel_basis_fp(
                    mat_sub_fp(transpose(Ep),
                               scal_fp((1 - nrm[0][1]) % p, NV, p), p), p)
                if ker:
                    lit_instances.append((m, p, pi, nrm[0][0], ker[0]))
                    break
            if len(lit_instances) >= 2 and \
                    len({inst[1] for inst in lit_instances}) == 2:
                break
        if len(lit_instances) >= 2 and \
                len({inst[1] for inst in lit_instances}) == 2:
            break
    for (m, p, pi, g, lam) in lit_instances:
        E = encoding_matrix(tuple(m["perm"]), m["direction"])
        cells = [tuple(t) for t in itertools.product(range(p), repeat=NV)]
        bad = literal_square_violations(pi, g, lam, E, p, cells)
        lit_rows.append({"role": m["role"], "direction": m["direction"],
                         "p": p, "pi": list(pi), "status": "admitted",
                         "violations": bad, "cells": len(cells)})
        bogus = tuple([1] + [0] * (NV - 1))
        if bogus != tuple(lam):
            bad2 = literal_square_violations(pi, g, bogus, E, p, cells)
            lit_rows.append({"role": m["role"], "direction": m["direction"],
                             "p": p, "pi": list(pi), "status": "rejected",
                             "violations": bad2, "cells": len(cells)})
    adm_ok = all(r["violations"] == 0 for r in lit_rows
                 if r["status"] == "admitted")
    rej_ok = any(r["violations"] > 0 for r in lit_rows
                 if r["status"] == "rejected")
    say(f"  route C, the LITERAL permutation verification: "
        f"{len(lit_rows)} rows from {len(lit_instances)} declared "
        f"(cell, prime) instances -- an admitted and a rejected covector at "
        f"each -- with the admitted candidates violating the square at 0 cells "
        f"and the rejected control at a measured positive count")
    g22 = gate("G22", "ROUTE C -- THE LITERAL PERMUTATION VERIFICATION -- "
               "CONFIRMS THAT THE COUNTED SQUARE IS THE PERMUTATION SQUARE.  "
               "At each declared INSTANCE a candidate route A admits is rebuilt "
               "as an ACTUAL permutation and the square is compared entry by "
               "entry at EVERY one of the p^6 record cells: zero violations.  "
               "A declared rejected covector is run through the same code at "
               "the same instance and violates it at a positive count, so the "
               "verification is not vacuous.  The row count is twice the "
               "instance count, and both are reported as what they are",
               adm_ok and rej_ok and len(lit_rows) > 0 and
               len(lit_rows) == 2 * len(lit_instances),
               {"instances": len(lit_instances), "rows": lit_rows,
                "rows_are_two_per_instance":
                    len(lit_rows) == 2 * len(lit_instances),
                "admitted_all_clean": adm_ok,
                "a_rejected_candidate_violates": rej_ok})
    report("G22", g22, f"admitted clean {adm_ok}; rejected violates {rej_ok}")

    mod_rows = []
    mod_equal = 0
    for m in cells_meta:
        if m["role"] != "module" and m["role"] != "lex":
            continue
        E = encoding_matrix(tuple(m["perm"]), m["direction"])
        for p in sweep_primes():
            for pi in S3_ELEMS:
                if pi == (0, 1, 2):
                    continue
                eq, irk, ek = module_obstruction_measured(E, pi, p)
                if eq:
                    mod_equal += 1
                mod_rows.append({"role": m["role"], "direction": m["direction"],
                                 "p": p, "pi": list(pi), "E_equals_I_minus_rho":
                                     eq, "I_minus_rho_kills_the_all_ones": irk,
                                 "E_kills_the_all_ones": ek})
    mod_rows = drop_row_module(mod_rows)
    mod_equal = sum(1 for r in mod_rows if r["E_equals_I_minus_rho"])
    mod_rows_forced = mot_cells * len(sweep_primes()) * 5
    all_irk = all(r["I_minus_rho_kills_the_all_ones"] for r in mod_rows)
    none_ek = not any(r["E_kills_the_all_ones"] for r in mod_rows)
    # the obstruction's REACH, measured over the whole covariant family rather
    # than argued: (I - rho_V) kills the all-ones vector at every wing symmetry,
    # and E kills it at no (cell, prime) pair whatsoever
    irk_all_wings = 0
    for pi in S3_ELEMS:
        Rv = rho_V(pi)
        if Rv is not None and all(1 - sum(Rv[i][j] for j in range(NV)) == 0
                                  for i in range(NV)):
            irk_all_wings += 1
    ek_pairs = 0
    ek_zero_pairs = 0
    for m in cells_meta:
        Ecell = encoding_matrix(tuple(m["perm"]), m["direction"])
        rsums = [sum((Ecell[i][j] for j in range(NV)), Fr(0))
                 for i in range(NV)]
        for p in sweep_primes():
            ek_pairs += 1
            red = [to_fp_frac(v, p) for v in rsums]
            if all(v == 0 for v in red):
                ek_zero_pairs += 1
    synth_rho = synthetic_module_action(7)
    synth_IR = [[((1 if i == j else 0) - synth_rho[i][j]) % 7
                 for j in range(2)] for i in range(2)]
    synth_mod_invertible = kernel_dim_fp(synth_IR, 7) == 0
    say(f"  the PERMUTATION-MODULE obstruction over {len(mod_rows)} (cell, "
        f"prime, wing) rows: E = I - rho_V(pi) at {mod_equal}; "
        f"(I - rho_V) kills the all-ones link vector at "
        f"{sum(1 for r in mod_rows if r['I_minus_rho_kills_the_all_ones'])}; "
        f"E kills it at "
        f"{sum(1 for r in mod_rows if r['E_kills_the_all_ones'])}")
    say(f"  its positive control: a synthetic NON-permutation S_3-action has "
        f"I - rho invertible ({synth_mod_invertible}), so the module square is "
        f"satisfiable when the module is not a permutation module")
    say(f"  its REACH, measured beyond the 210 rows: (I - rho_V) kills the "
        f"all-ones vector at {irk_all_wings} of {len(S3_ELEMS)} wing "
        f"symmetries, and E kills it at {ek_zero_pairs} of {ek_pairs} "
        f"(cell, prime) pairs over the WHOLE covariant family -- so the forced "
        f"equality fails at all {ek_pairs * 5} (cell, prime, wing) rows, not "
        f"only the {len(mod_rows)} the table prints")
    g23 = gate("G23", "THE PERMUTATION-MODULE OBSTRUCTION, MEASURED.  "
               "S1c-module (alpha equivariant) together with S1a, S1b and S3 "
               "force E = I - rho_V(pi).  The record datum space at d = 3 "
               "carries the S_3 PERMUTATION module -- the chart symmetry "
               "permutes links, it does not mix them -- so I - rho_V(pi) "
               "annihilates the all-ones link vector at every row measured, "
               "while E, being invertible, annihilates it at none; the forced "
               "equality therefore holds at zero rows.  The obstruction is not "
               "an artefact of the instrument: a synthetic NON-permutation "
               "S_3-action makes I - rho invertible and the module square "
               "satisfiable",
               mod_equal == 0 and all_irk and none_ek and
               synth_mod_invertible and len(mod_rows) > 0 and
               irk_all_wings == len(S3_ELEMS) and ek_zero_pairs == 0 and
               ek_pairs == ncells * len(sweep_primes()),
               {"rows": len(mod_rows),
                "rows_where_E_equals_I_minus_rho": mod_equal,
                "I_minus_rho_kills_the_all_ones_at_all_rows": all_irk,
                "E_kills_the_all_ones_at_no_row": none_ek,
                "wing_symmetries_where_I_minus_rho_kills_the_all_ones":
                    irk_all_wings,
                "family_wide_cell_prime_pairs": ek_pairs,
                "family_wide_pairs_where_E_kills_the_all_ones": ek_zero_pairs,
                "synthetic_non_permutation_module_is_invertible":
                    synth_mod_invertible})
    report("G23", g23, f"E = I - rho at {mod_equal}/{len(mod_rows)}; family-wide "
                       f"E.1 = 0 at {ek_zero_pairs}/{ek_pairs}; synthetic "
                       f"control {synth_mod_invertible}")
    tables["module_obstruction"] = {"rows": len(mod_rows),
                                    "equalities": mod_equal,
                                    "family_wide_pairs": ek_pairs,
                                    "family_wide_E_kills_the_all_ones":
                                        ek_zero_pairs}
    say("")

    # --- cell-completeness on the three verdict-carrying tables ------------
    cc_probe = completeness([1, 2], 4) is False
    cc_crit = completeness([crit_total_hits, crit_not_hits], crit_rows_forced)
    cc_census = completeness([live_full, len(census_rows) - live_full],
                             census_rows_forced)
    cc_module = completeness([mod_equal, len(mod_rows) - mod_equal],
                            mod_rows_forced)
    say(f"  CELL-COMPLETENESS on the three verdict-carrying tables, each "
        f"against its FORCED product:")
    say(f"     the order-criterion sweep : {crit_total_cells} rows against "
        f"{ncells} cells x {len(sweep_primes())} primes x 2 orders = "
        f"{crit_rows_forced}  ({cc_crit})")
    say(f"     the declared census       : {len(census_rows)} rows against "
        f"{len(census_cells)} cells x {len(sweep_primes())} primes x 5 wings = "
        f"{census_rows_forced}  ({cc_census})")
    say(f"     the module table          : {len(mod_rows)} rows against "
        f"{mot_cells} cells x {len(sweep_primes())} primes x 5 wings = "
        f"{mod_rows_forced}  ({cc_module})")
    g43 = gate("G43", "EVERY VERDICT-CARRYING TABLE IS CELL-COMPLETE AGAINST A "
               "FORCED PRODUCT (RUNBOOK 13 addendum, v13 #234).  The "
               "order-criterion sweep, the declared census and the "
               "permutation-module table each have their row count checked "
               "against the product the declarations force -- cells x primes x "
               "wing orders -- and their outcome columns checked to sum to that "
               "total, so a dropped row cannot pass unnoticed at any of them.  "
               "The completeness helper is calibrated the other way inside this "
               "same gate: it must REJECT a partition that does not sum",
               cc_probe and cc_crit and cc_census and cc_module and
               crit_total_cells == crit_rows_forced and
               len(census_rows) == census_rows_forced and
               len(mod_rows) == mod_rows_forced,
               {"criterion_rows": crit_total_cells,
                "criterion_rows_forced": crit_rows_forced,
                "census_rows": len(census_rows),
                "census_rows_forced": census_rows_forced,
                "module_rows": len(mod_rows),
                "module_rows_forced": mod_rows_forced,
                "completeness_rejects_a_short_partition": cc_probe})
    report("G43", g43, f"criterion {crit_total_cells}/{crit_rows_forced}; "
                       f"census {len(census_rows)}/{census_rows_forced}; "
                       f"module {len(mod_rows)}/{mod_rows_forced}")
    say("")

    # --- the in-arena positive control at the grown arena -----------------
    progress("in-arena FOUND control")
    pc = 7
    rank = NV
    m_star = growth_member_threshold(pc, rank)
    n_star = growth_labels(m_star)
    cs = [2, 2, 2, 4, 4, 4]
    gens, SIGg = control_blocks(m_star, pc, cs)
    ctrl = {"m": m_star, "labels": n_star, "prime": pc, "exponents": cs}
    found_ok = False
    heldout = {}
    if gens is not None:
        SIGgi = pinv(SIGg)
        powers = []
        for g in gens:
            pw, x = [], pident(n_star)
            for _ in range(pc):
                pw.append(x)
                x = pcomp(x, g)
            powers.append(pw)
        norm_ok = all(pcomp(SIGg, pcomp(gens[k], SIGgi)) == powers[k][cs[k]]
                      for k in range(rank))
        comm_ok = all(pcomp(gens[i], gens[j]) == pcomp(gens[j], gens[i])
                      for i in range(rank) for j in range(rank))
        Etil = [[((1 - cs[i]) % pc) if i == j else 0 for j in range(rank)]
                for i in range(rank)]
        Etil_fr = [[Fr(v) for v in row] for row in Etil]
        fit, held_override = verification_partition(pc)
        viol = 0
        cells_n = 0
        h1 = h2 = h3 = 0
        h_tot = 0
        fixvals = set()
        teeth_nosq = teeth_flat = teeth_exempt_cells = 0
        Ediag = [(1 - cs[k]) % pc for k in range(rank)]
        img = set()
        fixcache = {}
        for r in itertools.product(range(pc), repeat=rank):
            cells_n += 1
            a = control_alpha(gens, powers, r)
            img.add(a)
            lhs = pcomp(SIGg, pcomp(pinv(a), pcomp(SIGgi, a)))
            er = tuple(Ediag[k] * r[k] % pc for k in range(rank))
            rhs = control_alpha(gens, powers, er)
            if lhs != rhs:
                viol += 1
            if r != fit:
                h_tot += 1
                if lhs == rhs:
                    h1 += 1
                    h2 += 1
                fx = fixcache.get(lhs)
                if fx is None:
                    fx = pfix(lhs)
                    fixcache[lhs] = fx
                fixvals.add(fx)
                h3 += 1
                t1, t2 = teeth_predictions(lhs, fx, a, n_star)
                if teeth_exempt(a, pident(n_star)):
                    teeth_exempt_cells += 1
                else:
                    if t1:
                        teeth_nosq += 1
                    if t2:
                        teeth_flat += 1
        inj = (len(img) == pc ** rank)
        # THE MASTER EQUATION, I - E = alpha^-1 rho alpha, verified directly:
        # conjugation by Sigma on the image, pulled back through alpha, is the
        # matrix rho = I - E_tilde.  On the generating set it is the
        # normalisation measurement itself; on a declared sample of records it
        # is verified record by record.  (Given that alpha is a homomorphism it
        # is EQUIVALENT to the square, which is verified at every record cell.)
        master_sample = [tuple(t) for t in itertools.product(range(2),
                                                             repeat=rank)]
        master_sample += [tuple([j] * rank) for j in range(pc)]
        master_ok = 0
        for r in master_sample:
            a = control_alpha(gens, powers, r)
            conj = pcomp(SIGg, pcomp(a, SIGgi))
            rho_r = tuple(cs[k] * r[k] % pc for k in range(rank))
            if master_equation_holds(conj, control_alpha(gens, powers, rho_r)):
                master_ok += 1
        master_gens = sum(1 for k in range(rank)
                          if master_equation_holds(
                              pcomp(SIGg, pcomp(gens[k], SIGgi)),
                              powers[k][cs[k]]))
        homviol = 0
        for r in itertools.product(range(2), repeat=rank):
            for s2 in itertools.product(range(2), repeat=rank):
                x1 = control_alpha(gens, powers, r)
                x2 = control_alpha(gens, powers, s2)
                x3 = control_alpha(gens, powers,
                                   tuple((r[i] + s2[i]) % pc
                                         for i in range(rank)))
                if pcomp(x1, x2) != x3:
                    homviol += 1
        found_ok = found_branch(viol, inj, homviol, norm_ok, comm_ok)
        heldout = {"fit_cell": list(fit), "verified_cells": h_tot,
                   "H1_square_verified_at_every_cell": h1,
                   "H2_defect_permutation_verified": h2,
                   "H3_fixed_label_counts_verified": h3,
                   "distinct_fixed_label_values": sorted(fixvals),
                   "X_NOSQUARE_passes": teeth_nosq,
                   "X_FLATFIX_passes": teeth_flat,
                   "cells_where_both_extensions_are_forced":
                       teeth_exempt_cells}
        ctrl.update({"square_violations": viol, "record_cells": cells_n,
                     "injective": inj, "image_size": len(img),
                     "homomorphism_violations": homviol,
                     "normalisation_verified": norm_ok,
                     "generators_commute": comm_ok,
                     "master_equation_sample": len(master_sample),
                     "master_equation_verified": master_ok,
                     "master_equation_on_the_generating_set": master_gens,
                     "homomorphism_grid": 2 ** rank * 2 ** rank,
                     "E_tilde_diagonal": [Etil[i][i] for i in range(rank)]})
    say(f"  THE IN-ARENA POSITIVE CONTROL, at the grown arena L_m with "
        f"m = {m_star} ({n_star} labels), p = {pc}:")
    say(f"     six blocks identified with Z/{pc} so the wing symmetry acts as "
        f"multiplication by {cs}; A = <g_1..g_6> is elementary abelian of "
        f"order {pc}^{rank}")
    say(f"     the square holds at {ctrl.get('record_cells', 0) - ctrl.get('square_violations', 0)} "
        f"of {ctrl.get('record_cells', 0)} record cells; alpha injective "
        f"{ctrl.get('injective')}; homomorphism violations "
        f"{ctrl.get('homomorphism_violations')}")
    g24 = gate("G24", "FOUND IS REACHABLE, AND IT IS REACHABLE IN-ARENA.  At "
               "the grown arena of the DECLARED growth family -- m copies of "
               "TB3's seven moved labels, S_3 acting on the F_2^3 factor -- an "
               "elementary abelian subgroup of rank 6 is CONSTRUCTED, the wing "
               "symmetry is measured to normalise it with the declared "
               "exponents, and the resulting alpha is measured injective, a "
               "homomorphism, and to satisfy the commuting square at EVERY one "
               "of the p^6 record cells.  So the census instrument returns "
               "FOUND when the encodings are compatible, and the emptiness "
               "reported below is a measurement and not a dead branch",
               found_ok,
               ctrl)
    report("G24", g24, f"square violations {ctrl.get('square_violations')}; "
                       f"injective {ctrl.get('injective')}")
    g25 = gate("G25", "THE VERIFICATION IS EXHAUSTIVE, AND NOTHING IN IT IS "
               "FITTED.  The candidate is built from the declared exponents "
               "before any record cell is read, so the declared FIT / "
               "COMPLEMENT split "
               "is a PARTITION of the record space and not an estimation: the "
               "square is verified at every cell of the complement of the FIT "
               "cell (H1), and the defect permutation's entry-by-entry "
               "comparison (H2) is the SAME boolean as H1, reported as such.  "
               "H3 counts the cells at which the fixed-label count is read and "
               "the distinct values it takes.  The two extensions declared IN "
               "ADVANCE to fail -- X-NOSQUARE and X-FLATFIX -- are "
               "analytically forced to fail off the zero record, and are "
               "carried as disclosures; what this gate must-passes is the "
               "COMPUTED exempt count, gated to be exactly one, so an "
               "instrument that exempted more could not pass here",
               bool(heldout) and heldout["H1_square_verified_at_every_cell"]
               == heldout["verified_cells"] and
               heldout["H2_defect_permutation_verified"] ==
               heldout["verified_cells"]
               and len(heldout["distinct_fixed_label_values"]) > 1 and
               heldout["X_NOSQUARE_passes"] == 0 and
               heldout["X_FLATFIX_passes"] == 0 and
               heldout["cells_where_both_extensions_are_forced"] == 1,
               heldout)
    report("G25", g25, f"H1/H2 {heldout.get('H1_square_verified_at_every_cell')}"
                       f"/{heldout.get('verified_cells')}; teeth "
                       f"{heldout.get('X_NOSQUARE_passes')}/"
                       f"{heldout.get('X_FLATFIX_passes')}")

    # --- THE MASTER EQUATION AND THE THREE WALLS AS ITS READINGS ----------
    progress("master equation")
    wall_rows = []
    ind_rows = []
    for p in sweep_primes():
        for pi in S3_ELEMS:
            if pi == (0, 1, 2):
                continue
            Rv = rho_V(pi)
            if Rv is None:
                continue
            Emod = [[((1 if i == j else 0) - Rv[i][j]) % p for j in range(NV)]
                    for i in range(NV)]
            Emodfr = [[Fr(v) for v in row] for row in Emod]
            pre_ok = (fix_space_dim(Emodfr, p) == 0)
            crit_ok = order_criterion(Emodfr, p, pord(SIGMA[pi]))
            sing = (kernel_dim_fp(Emod, p) > 0)
            ind_rows.append({"p": p, "pi": list(pi), "ord": pord(SIGMA[pi]),
                             "clears_the_precheck": pre_ok,
                             "satisfies_the_order_criterion": crit_ok,
                             "E_is_singular": sing,
                             "dim_ker_E": kernel_dim_fp(Emod, p)})
    ind_ok = all(module_independence(r["clears_the_precheck"],
                                     r["satisfies_the_order_criterion"],
                                     r["E_is_singular"]) for r in ind_rows)
    # both decision helpers calibrated the other way through the same calls
    master_probe = master_equation_holds((0, 1), (1, 0)) is False
    indep_probe = module_independence(True, True, False) is False
    wall_rows = [
        {"reading": "rho lies in GL(A)",
         "consequence": "I - E invertible, i.e. dim ker(E - I) = 0",
         "wall": "the fixed-point mismatch (the stillborn precheck)"},
        {"reading": "rho^ord(Sigma_pi) = I",
         "consequence": "(I - E)^ord(pi) = I",
         "wall": "the order obstruction"},
        {"reading": "rho = rho_V(pi) (the module clause)",
         "consequence": "E = I - rho_V(pi)",
         "wall": "the permutation-module obstruction"}]
    say(f"  THE MASTER EQUATION  I - E = alpha^-1 rho alpha, with rho the "
        f"conjugation action of Sigma_pi on the image, read through alpha:")
    say(f"     verified on the generating set at "
        f"{ctrl.get('master_equation_on_the_generating_set')} of {rank}, and "
        f"record by record at "
        f"{ctrl.get('master_equation_verified')} of "
        f"{ctrl.get('master_equation_sample')} declared records; given that "
        f"alpha is a measured homomorphism it is EQUIVALENT to the square, "
        f"which holds at all {ctrl.get('record_cells')} record cells")
    for w in wall_rows:
        say(f"     {w['reading']:36s} => {w['consequence']:44s} "
            f"{w['wall']}")
    say(f"  the module obstruction is INDEPENDENT of the other two readings: "
        f"at {len(ind_rows)} (prime, wing) rows the module-forced "
        f"E = I - rho_V(pi) clears the precheck "
        f"({sum(1 for r in ind_rows if r['clears_the_precheck'])}), satisfies "
        f"the order criterion "
        f"({sum(1 for r in ind_rows if r['satisfies_the_order_criterion'])}) "
        f"and is nevertheless SINGULAR "
        f"({sum(1 for r in ind_rows if r['E_is_singular'])}), so S3 kills it "
        f"where neither other wall does -- arena-free and transport-free")
    g44 = gate("G44", "THE MASTER EQUATION, AND THE THREE WALLS AS ITS "
               "READINGS.  S1a forces the image to be Sigma-stable and S1b "
               "makes it abelian, so conjugation by Sigma_pi restricts to an "
               "automorphism rho of it; S3 makes alpha an isomorphism, and the "
               "square becomes I - E = alpha^-1 rho alpha.  Every obstruction "
               "this unit reports is a reading of that one equation: rho "
               "invertible gives the fixed-point mismatch, rho^ord = I gives "
               "the order obstruction, rho = rho_V(pi) gives the "
               "permutation-module obstruction.  The equation is VERIFIED at "
               "the in-arena control -- on its generating set and record by "
               "record on a declared sample -- and the module reading is "
               "measured INDEPENDENT of the other two: the module-forced E "
               "clears the precheck AND satisfies the order criterion at every "
               "(prime, wing) row and dies anyway, because E must be "
               "invertible and I - rho_V(pi) is not",
               gens is not None and
               ctrl.get("master_equation_on_the_generating_set") == rank and
               ctrl.get("master_equation_verified") ==
               ctrl.get("master_equation_sample") and
               len(ind_rows) == len(sweep_primes()) * 5 and ind_ok and
               master_probe and indep_probe and
               all(r["dim_ker_E"] > 0 for r in ind_rows),
               {"master_equation_rejects_a_mismatch": master_probe,
                "independence_rejects_an_invertible_module_E": indep_probe,
                "master_equation_on_the_generating_set":
                    ctrl.get("master_equation_on_the_generating_set"),
                "master_equation_verified": ctrl.get("master_equation_verified"),
                "master_equation_sample": ctrl.get("master_equation_sample"),
                "square_cells": ctrl.get("record_cells"),
                "readings": wall_rows,
                "module_independence_rows": ind_rows})
    report("G44", g44, f"master equation {ctrl.get('master_equation_verified')}"
                       f"/{ctrl.get('master_equation_sample')}; independence "
                       f"rows {len(ind_rows)}, all three clauses {ind_ok}")
    tables["master_equation"] = {"readings": wall_rows,
                                 "independence": ind_rows}

    # --- THE SUFFICIENCY CENSUS at the grown arena ------------------------
    progress("sufficiency census")
    suff_rows = []
    cube3 = cube_roots(pc)
    prim3 = [s for s in cube3 if s != 1]
    separable = (len(cube3) == 3)
    patterns = sufficiency_patterns(
        [tuple(t) for t in itertools.product(sorted(prim3), repeat=rank)])
    suff_sample = [tuple(t) for t in itertools.product(range(2), repeat=rank)]
    suff_sample += [tuple([j] * rank) for j in range(pc)]
    for cvec in patterns:
        gs, SG = control_blocks(m_star, pc, list(cvec))
        row = {"exponents": list(cvec), "built": gs is not None}
        if gs is not None:
            SGi = pinv(SG)
            pw = []
            for g in gs:
                q, x = [], pident(n_star)
                for _ in range(pc):
                    q.append(x)
                    x = pcomp(x, g)
                pw.append(q)
            Ed = [(1 - cvec[k]) % pc for k in range(rank)]
            supp = [{x for x in range(n_star) if g[x] != x} for g in gs]
            viol2 = 0
            for r in suff_sample:
                a2 = control_alpha(gs, pw, r)
                if pcomp(SG, pcomp(pinv(a2), pcomp(SGi, a2))) != control_alpha(
                        gs, pw, tuple(Ed[k] * r[k] % pc for k in range(rank))):
                    viol2 += 1
            row.update({
                "E_tilde": Ed,
                "normalised": all(pcomp(SG, pcomp(gs[k], SGi)) == pw[k][cvec[k]]
                                  for k in range(rank)),
                "commute": all(pcomp(gs[i], gs[j]) == pcomp(gs[j], gs[i])
                               for i in range(rank) for j in range(rank)),
                "supports_disjoint": all(not (supp[i] & supp[j])
                                         for i in range(rank)
                                         for j in range(i + 1, rank)),
                "generator_orders_are_p": all(pord(g) == pc for g in gs),
                "E_invertible": all(v % pc != 0 for v in Ed),
                "criterion": all(pow((1 - v) % pc, 3, pc) == 1 for v in Ed),
                "square_violations_on_the_sample": viol2})
        suff_rows.append(row)
    suff_ok = all(r["built"] and r["normalised"] and r["commute"] and
                  r["supports_disjoint"] and r["generator_orders_are_p"] and
                  r["E_invertible"] and r["criterion"] and
                  r["square_violations_on_the_sample"] == 0 for r in suff_rows)
    say(f"  THE SUFFICIENCY CENSUS at L_{m_star} ({n_star} labels), p = {pc}, "
        f"ord 3: x^3 - 1 has {len(cube3)} distinct roots mod {pc} "
        f"(separable {separable}), so every E satisfying the criterion there is "
        f"conjugate to I - diag(c) with c in {sorted(prim3)}^{rank} -- "
        f"{len(patterns)} patterns, and EVERY one of them is realised by a "
        f"member of the declared growth family ({suff_ok})")
    g45 = gate("G45", "AT THE GROWN ARENA THE CRITERION IS NOT MERELY "
               "NECESSARY BUT SUFFICIENT, CENSUSED OVER EVERY PATTERN.  At "
               "p = 7 the polynomial x^3 - 1 is measured to have three distinct "
               "roots, so any rho with rho^3 = I is diagonalisable; "
               "invertibility of E = I - rho excludes the eigenvalue 1, so "
               "every E satisfying the criterion at an order-3 wing symmetry is "
               "conjugate to I - diag(c) with c a vector of primitive cube "
               "roots.  All 2^6 such patterns are censused: at every one the "
               "declared growth family realises the encoding -- generators of "
               "order p on disjoint supports, commuting, normalised with the "
               "demanded exponents, E invertible, the criterion satisfied, and "
               "the square holding at every record of a declared sample.  The "
               "converse therefore holds at this scope, and the bridge question "
               "reduces there to the criterion",
               separable and len(patterns) == 2 ** rank and suff_ok and
               len(prim3) == 2,
               {"prime": pc, "arena_labels": n_star,
                "cube_roots": cube3, "separable": separable,
                "patterns": len(patterns),
                "sample_records_per_pattern": len(suff_sample),
                "all_patterns_realised": suff_ok, "rows": suff_rows})
    report("G45", g45, f"{len(patterns)} patterns; all realised {suff_ok}")
    tables["sufficiency"] = {"patterns": len(patterns), "rows": suff_rows}

    empty_at_grown = None
    Ereal = encoding_matrix(tuple(range(NV)), "counts->q")
    if gens is not None and Ereal is not None:
        empty_at_grown = empty_branch(not order_criterion(Ereal, pc, 3))
    say(f"  THE SAME MACHINERY AT THE SAME ARENA, with HA's OWN d = 3 "
        f"encoding in place of the synthetic one: EMPTY "
        f"({empty_at_grown})")
    g26 = gate("G26", "EMPTY IS REACHABLE BY THE SAME MACHINERY AT THE SAME "
               "ARENA.  Replacing the synthetic encoding by HA's own d = 3 "
               "record-is-metric readout at the grown arena, and changing "
               "nothing else, the order criterion fails and the census is "
               "empty -- so the FOUND and EMPTY branches are separated by the "
               "ENCODING and not by the arena, the prime, or the instrument",
               bool(empty_at_grown),
               {"arena_labels": n_star, "prime": pc,
                "synthetic_encoding_found": found_ok,
                "HA_encoding_empty": empty_at_grown})
    report("G26", g26, f"HA's encoding at the grown arena: EMPTY "
                       f"{empty_at_grown}")

    brk = {"square_violations": 0, "hom_violations": 0, "cells": 0}
    Ebrk = encoding_matrix(tuple(range(NV)), "counts->q")
    Ebp = mat_to_fp(Ebrk, 7) if Ebrk is not None else None
    kerlam = kernel_basis_fp(
        mat_sub_fp(transpose(Ebp), scal_fp(4, NV, 7), 7), 7) if Ebp else []
    kermu = kernel_basis_fp(mat_sub_fp(transpose(Ebp), eye_fp(NV), 7), 7) \
        if Ebp else []
    if kerlam and kermu and 7 in subs_cache:
        lam0, mu0 = kerlam[0], kermu[0]
        subs7 = [(g, conjugation_exponent((1, 2, 0), g, 7))
                 for g in subs_cache[7].values()]
        nrm7 = [(g, s) for (g, s) in subs7 if s is not None and (1 - s) % 7 == 4]
        if nrm7:
            g0 = nrm7[0][0]
            pw, x = [], pident(NLAB)
            for _ in range(7):
                pw.append(x)
                x = pcomp(x, g0)
            dpw = [delta_pi((1, 2, 0), pw[j]) for j in range(7)]
            lamE = [sum(lam0[i] * Ebp[i][k] for i in range(NV)) % 7
                    for k in range(NV)]
            muE = [sum(mu0[i] * Ebp[i][k] for i in range(NV)) % 7
                   for k in range(NV)]
            for r in itertools.product(range(7), repeat=NV):
                brk["cells"] += 1
                lr = break_hom_from_forms(
                    sum(lam0[i] * r[i] for i in range(NV)),
                    sum(mu0[i] * r[i] for i in range(NV)), 7)
                ler = break_hom_from_forms(
                    sum(lamE[i] * r[i] for i in range(NV)),
                    sum(muE[i] * r[i] for i in range(NV)), 7)
                if dpw[lr] != pw[ler]:
                    brk["square_violations"] += 1
            for r in itertools.product(range(2), repeat=NV):
                for s2 in itertools.product(range(2), repeat=NV):
                    a = break_hom_exponent(lam0, mu0, r, 7)
                    b = break_hom_exponent(lam0, mu0, s2, 7)
                    c = break_hom_exponent(
                        lam0, mu0, tuple((r[i] + s2[i]) % 7 for i in range(NV)),
                        7)
                    if (a + b) % 7 != c:
                        brk["hom_violations"] += 1
    say(f"  BREAK-HOM (the negative with teeth): square violations "
        f"{brk['square_violations']} of {brk['cells']}; homomorphism "
        f"violations {brk['hom_violations']} -- rejected by S1b ALONE")
    g27 = gate("G27", "THE NEGATIVE CONTROL HAS TEETH, AND THE REJECTING "
               "CLAUSE IS NAMED.  BREAK-HOM multiplies an admitted exponent by "
               "a 1-eigencovector raised to the (p-1)st power: it satisfies "
               "the commuting square at EVERY record cell, differing from an "
               "admitted candidate only in the LINEARITY of its exponent, and "
               "it is rejected by S1b alone at a measured positive count",
               brk["cells"] > 0 and brk["square_violations"] == 0 and
               brk["hom_violations"] > 0, brk)
    report("G27", g27, f"square {brk['square_violations']}/{brk['cells']}; hom "
                       f"{brk['hom_violations']}")

    s2_ok = bool(heldout) and s2_stratification_carried(
        heldout.get("distinct_fixed_label_values", []))
    s2_probe = s2_stratification_carried([len(GC)]) is False
    s4_rows = []
    for nm, Q in sorted(DECL["ladder_completions"].items()):
        K = ladder_defect_subgroup(Q)
        live = sorted(p for p in sweep_primes() if len(K) % p == 0)
        # the census's DECIDING INPUTS, fingerprinted with this base in scope
        fp = base_fingerprint(
            [str(m["key"]) for m in census_cells], sweep_primes(),
            [pord(SIGMA[pi]) for pi in S3_ELEMS if pi != (0, 1, 2)],
            [len(subs_by_pi[(p, pi)]) for p in sweep_primes()
             for pi in S3_ELEMS if pi != (0, 1, 2)])
        # and the criterion, re-evaluated at this base's own live primes
        hits_here = sum(1 for m in census_cells for p in live
                        for o in (2, 3)
                        if order_criterion(encoding_matrix(tuple(m["perm"]),
                                                           m["direction"]),
                                           p, o))
        rows_here = len(census_cells) * len(live) * 2
        s4_rows.append({"base": nm, "K_order": len(K), "live_primes": live,
                        "criterion_rows_at_this_base": rows_here,
                        "criterion_hits_at_this_base": hits_here,
                        "deciding_input_fingerprint": fp})
    s4_rows = s4_base_rows(s4_rows)
    fingerprints = {r["deciding_input_fingerprint"] for r in s4_rows}
    base_orders = sorted({r["K_order"] for r in s4_rows})
    # the fingerprint must SEPARATE different inputs, or its equality says
    # nothing: calibrated the other way through the same function
    fp_probe = (base_fingerprint(["a-different-cell"], [2], [2], [1]) !=
                s4_rows[0]["deciding_input_fingerprint"])
    scale_rows = [{"scale": "native", "labels": NLAB,
                   "census_empty": empty_branch(crit_total_hits == 0)},
                  {"scale": "grown", "labels": n_star,
                   "census_empty": bool(empty_at_grown)}]
    say(f"  S4 -- BASE-INDEPENDENCE, COMPUTED.  The census's deciding inputs "
        f"are fingerprinted inside the per-base loop: {len(fingerprints)} "
        f"distinct fingerprint over {len(s4_rows)} bases whose defect "
        f"subgroups are {base_orders} -- so the census cannot depend on the "
        f"base, and the criterion, re-evaluated at each base's own live primes "
        f"({[r['criterion_rows_at_this_base'] for r in s4_rows]} rows), is hit "
        f"at {[r['criterion_hits_at_this_base'] for r in s4_rows]}")
    g28 = gate("G28", "S2 (CARRIER RIGIDITY).  The transport side's "
               "fixed-label stratification is measured CARRIED by the admitted "
               "candidate -- the defect permutations take more than one "
               "fixed-label value, so the stratification is a real invariant "
               "and not a constant -- and the clause that decides it is "
               "calibrated the other way inside this same gate: a constant "
               "stratification must be REJECTED by it",
               s2_ok and s2_probe and
               all(r["census_empty"] for r in scale_rows),
               {"S2_stratification_values":
                    heldout.get("distinct_fixed_label_values"),
                "S2_rejects_a_constant_stratification": s2_probe,
                "S4_scales": scale_rows})
    report("G28", g28, f"S2 stratification carried {s2_ok}; scales "
                       f"{len(scale_rows)}")
    g46 = gate("G46", "S4 (FUNCTORIALITY) IS COMPUTED, NOT TYPED.  The "
               "deciding quantity (I - E)^ord(pi) = I has NO base input: the "
               "candidate enumeration ranges over every cyclic subgroup of "
               "order p in G_C and every wing symmetry, and the completion "
               "that names a ladder base never enters it.  That is measured "
               "rather than asserted -- the census's deciding inputs are "
               "fingerprinted INSIDE the per-base loop and the fingerprint is "
               "identical at every base, while the bases themselves are "
               "measured genuinely different, their defect subgroups ranging "
               "over more than two orders of magnitude; and the criterion, "
               "re-evaluated at each base's own live primes, is hit nowhere.  "
               "Base-independence therefore holds BY CONSTRUCTION and the "
               "gate measures the construction",
               len(s4_rows) == len(DECL["ladder_completions"]) and
               len(fingerprints) == 1 and len(base_orders) == len(s4_rows) and
               max(base_orders) // max(1, min(base_orders)) > 100 and
               fp_probe and
               all(r["criterion_hits_at_this_base"] == 0 for r in s4_rows),
               {"bases": len(s4_rows), "distinct_fingerprints":
                   len(fingerprints), "defect_subgroup_orders": base_orders,
                "fingerprint_separates_different_inputs": fp_probe,
                "rows": s4_rows})
    report("G46", g46, f"{len(s4_rows)} bases, {len(fingerprints)} distinct "
                       f"fingerprint, |K| {base_orders}")
    tables["controls"] = {"found": ctrl, "verification": heldout,
                          "break_hom": brk, "S4_bases": s4_rows,
                          "S4_scales": scale_rows}
    say("")

    # ---------------------------------------------------------------- 7 ---
    say("------------------------------------------------------------------")
    say("7. ITEM 6 -- THE PRIME SECTION AT THE NEW PAIRING")
    say("------------------------------------------------------------------")
    progress("prime section")
    thr_rows = []
    for p in sweep_primes():
        thr_rows.append({
            "p": p,
            "d3_divisibility_threshold": scale_threshold_divisibility(p, NV),
            "d3_elementary_abelian_threshold":
                scale_threshold_elementary(p, NV),
            "d3_growth_family_member": growth_member_threshold(p, NV),
            "d3_growth_family_labels":
                growth_labels(growth_member_threshold(p, NV)),
            "d2_elementary_abelian_threshold": scale_threshold_elementary(p, 3),
        })
    anchor("A-LCB-THR-5", "LCB section 12.3: the smallest arena admitting an "
           "injective candidate at d = 2, p = 5 (3p+1)", 16,
           scale_threshold_elementary(5, 3), "LCB committed paper (section 12.3)")
    anchor("A-LCB-THR-7", "LCB section 12.3: the same at p = 7", 22,
           scale_threshold_elementary(7, 3), "LCB committed paper (section 12.3)")
    say(f"  {'p':5s}{'p^6 | (n-1)!':15s}{'elem. abelian':15s}"
        f"{'growth m':10s}{'growth labels':15s}d=2 analogue")
    for r in thr_rows:
        say(f"  {r['p']:<5d}{r['d3_divisibility_threshold']:<15d}"
            f"{r['d3_elementary_abelian_threshold']:<15d}"
            f"{r['d3_growth_family_member']:<10d}"
            f"{r['d3_growth_family_labels']:<15d}"
            f"{r['d2_elementary_abelian_threshold']}")
    native_admits = [p for p in sweep_primes()
                     if legendre_exponent(NLAB - 1, p) >= NV]
    g29 = gate("G29", "THE SCALE-THRESHOLD TABLE IS RECOMPUTED AT THE NEW "
               "PAIRING.  Per prime, three thresholds are COMPUTED and never "
               "typed: the smallest arena whose completion group's order is "
               "divisible by p^6 (Legendre's formula), the smallest arena "
               "containing an elementary abelian subgroup of rank 6 (minimal "
               "faithful degree 6p), and the smallest member of the declared "
               "growth family reaching it.  The two are measured DIFFERENT -- "
               "divisibility is strictly weaker than realisability -- and the "
               "NATIVE three-wing arena admits an injective candidate at NO "
               "declared prime.  The d = 2 analogue recomputed by the same "
               "function reproduces LCB's own 3p+1 thresholds",
               len(native_admits) == 0 and
               all(r["d3_divisibility_threshold"] <=
                   r["d3_elementary_abelian_threshold"] for r in thr_rows) and
               any(r["d3_divisibility_threshold"] <
                   r["d3_elementary_abelian_threshold"] for r in thr_rows),
               {"rows": thr_rows,
                "native_arena_labels": NLAB,
                "declared_primes_the_native_arena_admits": native_admits})
    report("G29", g29, f"native arena admits {len(native_admits)} of "
                       f"{len(sweep_primes())} primes")
    tables["scale_thresholds"] = thr_rows

    meet_rows = []
    for p in sweep_primes():
        cr = cube_roots(p)
        prim = [s for s in cr if s != 1]
        demanded3 = sorted({(1 - s) % p for s in prim})
        ha_half = pow(2, -1, p)
        inarena = sorted({(1 - s) % p for r in norm_rows if r["p"] == p and
                          r["ord"] == 3 for s in
                          [int(k) for k in r["exponent_spectrum"]]})
        meet = meeting_verdict(ha_half, demanded3, inarena)
        ncells_meet = sum(1 for m in cells_meta if m["fix_dims"][p] == 0 and
                          any(kernel_dim_fp(mat_sub_fp(
                              transpose(mat_to_fp(encoding_matrix(
                                  tuple(m["perm"]), m["direction"]), p)),
                              scal_fp(dv, NV, p), p), p) > 0
                              for dv in demanded3)) if demanded3 else 0
        meet_rows.append({"p": p, "cube_roots_of_1": cr,
                          "demanded_1_minus_s_order3": demanded3,
                          "HA_half_mod_p": ha_half,
                          "in_arena_demanded_values": inarena,
                          "MEETING": meet,
                          "precheck_surviving_cells_admitting_it": ncells_meet})
    meet_primes = [r["p"] for r in meet_rows if r["MEETING"]]
    say(f"  {'p':5s}{'cube roots':14s}{'demanded 1-s':16s}{'HA 1/2 mod p':14s}"
        f"{'in-arena 1-s':16s}MEETING")
    for r in meet_rows:
        say(f"  {r['p']:<5d}{str(r['cube_roots_of_1']):14s}"
            f"{str(r['demanded_1_minus_s_order3']):16s}"
            f"{r['HA_half_mod_p']:<14d}{str(r['in_arena_demanded_values']):16s}"
            f"{r['MEETING']}")
    module_meet7 = [m for m in cells_meta if m["role"] == "module" and
                    m["direction"] == "counts->q" and m["meets_at_7"]]
    g30 = gate("G30", "THE p = 7 SPECTRAL MEETING, TESTED AS A MEASUREMENT AND "
               "CONFIRMED -- AND ITS PRICE MEASURED WITH IT.  For an order-3 "
               "wing symmetry the square demands the eigenvalue 1 - s with "
               "s^3 = 1; the demanded set is computed per prime, and the "
               "values actually REALISED in the three-wing arena are measured "
               "from the conjugation exponents of the subgroups the wing "
               "symmetry normalises.  At p = 7 the realised set is {4, 6} and "
               "HA's own counts->q eigenvalue 1/2 is 4: they MEET, and at no "
               "other declared prime do they.  R2-LCB's prediction is "
               "confirmed at the d = 3 pairing.  What it buys is measured too: "
               "the meeting occurs at the equivariant identification, which "
               "the precheck has already declared STILLBORN",
               meet_primes == [7] and len(module_meet7) > 0,
               {"rows": meet_rows, "primes_where_they_meet": meet_primes,
                "module_cells_admitting_it_at_7": len(module_meet7),
                "those_cells_precheck":
                    [m["fix_dims"][7] for m in module_meet7]})
    report("G30", g30, f"meeting primes {meet_primes}; module cells admitting "
                       f"it at 7: {len(module_meet7)}")
    tables["spectral_meeting"] = meet_rows

    per_prime_verdict = {}
    for p in sweep_primes():
        per_prime_verdict[p] = "EMPTY" if crit_hits[p] == 0 else "LIVE"
    g31 = gate("G31", "S6 -- THE PRIME IS A PARAMETER, WITH PER-PRIME "
               "VERDICTS.  The order criterion is evaluated at every declared "
               "prime separately; the partial clause list is measured "
               "prime-DEPENDENT (the S1a+S1b census is live at 5 and 7 and "
               "dead above) while the full clause list is measured "
               "prime-UNIFORM, so the verdict does not ride on the declared "
               "prime and the difference between the two readings is itself a "
               "measurement",
               all(v == "EMPTY" for v in per_prime_verdict.values()) and
               len(per_prime_verdict) == len(sweep_primes()) and
               len({r["p"] for r in norm_rows if r["normalised"]}) == 2,
               {"per_prime": per_prime_verdict,
                "primes_with_a_normalised_subgroup":
                    sorted({r["p"] for r in norm_rows if r["normalised"]})})
    report("G31", g31, f"per-prime verdicts {per_prime_verdict}")

    # --- the spectral reading, at every swept dimension --------------------
    progress("spectral reading")
    spec_rows = []
    for dd in dimension_sweep():
        nn = dd * (dd + 1) // 2
        for ordering in ("natural", "lex"):
            A = general_d_readout(dd, ordering)
            for direction in ("q->counts", "counts->q"):
                Mx = A if direction == "q->counts" else inv_exact(A)
                if Mx is None:
                    continue
                for p in sweep_primes():
                    Mp = [[to_fp_frac(v, p) for v in row] for row in Mx]
                    Kx = [[(Mp[i][j] - (1 if i == j else 0)) % p
                           for j in range(nn)] for i in range(nn)]
                    spec_rows.append({
                        "d": dd, "ordering": ordering, "direction": direction,
                        "p": p, "size": nn,
                        "dim_ker_E_minus_I": spectral_multiplicity(
                            kernel_dim_fp(Kx, p), dd)})
    nat_is_d = all(r["dim_ker_E_minus_I"] == r["d"] for r in spec_rows
                   if r["ordering"] == "natural")
    lex_is_one = all(r["dim_ker_E_minus_I"] == 1 for r in spec_rows
                     if r["ordering"] == "lex")
    eig1_everywhere = all(r["dim_ker_E_minus_I"] >= 1 for r in spec_rows)
    say(f"  the spectral reading at every swept dimension: at the NATURAL "
        f"identification dim ker(E - I) = d ({nat_is_d}); at HA's own lex "
        f"ordering it is 1 ({lex_is_one}); so the eigenvalue 1 is present at "
        f"{sum(1 for r in spec_rows if r['dim_ker_E_minus_I'] >= 1)} of "
        f"{len(spec_rows)} (dimension, ordering, direction, prime) rows, and "
        f"0 lies in spec(I - E) at every one of them")
    g47 = gate("G47", "THE SPECTRAL READING, MEASURED AT EVERY SWEPT "
               "DIMENSION.  At the motivated identifications HA's readout "
               "carries the eigenvalue 1 -- with multiplicity d at the natural "
               "identification and multiplicity 1 at HA's own lex ordering -- "
               "at d = 2,3,4,5, in both directions and at every declared "
               "prime.  Hence 0 lies in spec(I - E) there.  A bridge at a wing "
               "symmetry of order n forces spec(I - E) into the n-th roots of "
               "unity, and 0 is on no unit circle: the obstruction is "
               "dimension-independent in PROOF form, which is what a successor "
               "at a larger or continuous scale inherits from this unit",
               nat_is_d and lex_is_one and eig1_everywhere and
               len(spec_rows) == len(dimension_sweep()) * 2 * 2 *
               len(sweep_primes()),
               {"rows": spec_rows,
                "natural_multiplicity_equals_d": nat_is_d,
                "lex_multiplicity_is_one": lex_is_one,
                "eigenvalue_one_present_at_every_row": eig1_everywhere})
    report("G47", g47, f"eigenvalue 1 at {len(spec_rows)}/{len(spec_rows)} "
                       f"rows; natural multiplicity = d {nat_is_d}")
    tables["spectral_reading"] = spec_rows
    say("")

    # ---------------------------------------------------------------- 8 ---
    say("------------------------------------------------------------------")
    say("8. THE SYMMETRY SELF-TESTS (RUNBOOK 14, ALL ADDENDA)")
    say("------------------------------------------------------------------")
    progress("self-tests")
    rho_perm_ok = 0
    for pi in S3_ELEMS:
        R = rho_V(pi)
        if R is not None and \
                all(sum(R[i][j] for j in range(NV)) == 1 for i in range(NV)) \
                and all(sum(R[i][j] for i in range(NV)) == 1
                        for j in range(NV)):
            rho_perm_ok += 1
    rho_set = {tuple(tuple(r) for r in rho_V(pi)) for pi in S3_ELEMS
               if rho_V(pi) is not None}
    rho_closed_ok = len(rho_set) == 6

    warmed = warm_the_cache(GC[:2000], (1, 2, 0))
    pre_lookups = CACHE_STATS["lookups"]
    pre_hits = CACHE_STATS["hits"]
    tau = tuple([0] + [((i + 1) % (NLAB - 1)) + 1 for i in range(NLAB - 1)])
    tau_moved = sum(1 for i in range(NLAB) if tau[i] != i)
    taui = pinv(tau)
    relab_fix = {}
    fresh = selftest_fresh()
    bypass_before = CACHE_STATS["bypasses"]
    tested = selftest_set(
        [m["key"] for m in cells_meta],
        [m["key"] for m in cells_meta if m["trivial_fix_all_primes"]])
    for pi in S3_ELEMS:
        sg = pcomp(tau, pcomp(SIGMA[pi], taui))
        cnt = 0
        for Q in GC:
            if pcomp(sg, pcomp(pinv(Q), pcomp(pinv(sg), Q))) == Q:
                cnt += 1
        relab_fix[str(list(pi))] = cnt
    for pi in S3_ELEMS[:2]:
        for Q in GC[:1000]:
            delta_pi(pi, Q, fresh=fresh, selftest=True)
    bypasses = CACHE_STATS["bypasses"] - bypass_before
    say(f"  the S_3-action on the record datum space is by PERMUTATION "
        f"matrices at {rho_perm_ok} of {len(S3_ELEMS)} elements; the image is "
        f"closed with {len(rho_set)} distinct matrices")
    say(f"  fix(delta) recomputed INSIDE a relabelled arena (the relabelling "
        f"moves {tau_moved} labels): "
        f"{sorted(set(relab_fix.values()))}")
    say(f"  cache: {bypasses} self-test bypasses, {CACHE_STATS['selftest_hits']} "
        f"self-test hits, against {pre_lookups} lookups and {pre_hits} hits "
        f"before the self-tests began")
    g32 = gate("G32", "THE SYMMETRY SELF-TEST, WITH THE CACHE DISCIPLINE.  The "
               "S_3-action on the record datum space is measured to be by "
               "PERMUTATION matrices at every group element and closed with "
               "six distinct images -- that is the fact the permutation-module "
               "obstruction turns on, and it is measured, not assumed.  "
               "fix(delta) is recounted INSIDE a declared relabelled arena, "
               "with a relabelling measured to move a positive number of "
               "labels, and it is still exactly one.  Every self-test "
               "evaluation BYPASSES the memo, self-test cache hits are zero, "
               "and the cache is measured to have been exercised before the "
               "self-tests began, so the zero-hit clause is not the signature "
               "of a cache nobody uses",
               rho_perm_ok == len(S3_ELEMS) and rho_closed_ok and
               set(relab_fix.values()) == {1} and tau_moved > 1 and
               bypasses > 0 and CACHE_STATS["selftest_hits"] == 0 and
               pre_hits > 0 and warmed > 0,
               {"permutation_matrix_elements": rho_perm_ok,
                "distinct_rho_images": len(rho_set),
                "relabelling_moves": tau_moved,
                "fix_delta_inside_the_relabelled_arena": relab_fix,
                "selftest_bypasses": bypasses,
                "selftest_cache_hits": CACHE_STATS["selftest_hits"],
                "lookups_before_the_selftests": pre_lookups,
                "hits_before_the_selftests": pre_hits,
                "cache_warmed_over": warmed})
    report("G32", g32, f"rho permutation {rho_perm_ok}/{len(S3_ELEMS)}; "
                       f"relabelled fix {sorted(set(relab_fix.values()))}; "
                       f"bypasses {bypasses}")

    # the tested set is CONSUMED, not merely counted: the decision quantity is
    # recomputed at every cell of it and compared against the family table
    fixdim_by_key = {m["key"]: m["fix_dims"][pref] for m in cells_meta}
    tested_swept = 0
    tested_agree = 0
    for tkey in tested:
        Et = encoding_matrix(tkey[0], tkey[1])
        tested_swept += 1
        if fix_space_dim(Et, pref) == fixdim_by_key.get(tkey):
            tested_agree += 1
    say(f"  the self-test's tested set: {len(tested)} declared cells, swept "
        f"and recomputed at {tested_swept}, agreeing at {tested_agree}")
    g33 = gate("G33", "THE SELF-TEST'S TESTED SET IS FIXED BY DECLARATION, "
               "NEVER SELECTED BY THE VERDICTS UNDER AUDIT (RUNBOOK 14 "
               "addendum) -- AND IT IS CONSUMED BY A SWEEP.  The declared set "
               "is the WHOLE covariant family -- every cell, including the ones "
               "the precheck kills -- measured strictly larger than the set the "
               "verdicts would have selected; and the decision quantity is "
               "RECOMPUTED at every cell of it and measured to agree with the "
               "family table, so a tested set selected by the verdicts shrinks "
               "a sweep that is counted here and not merely a list that is "
               "counted",
               len(tested) == ncells and tested_swept == ncells and
               tested_agree == ncells and
               len(tested) > sum(1 for m in cells_meta
                                 if m["trivial_fix_all_primes"]),
               {"declared_tested_cells": len(tested), "covariant_cells": ncells,
                "cells_swept_through_the_tested_set": tested_swept,
                "cells_agreeing_with_the_family_table": tested_agree,
                "verdict_selected_cells": sum(1 for m in cells_meta
                                              if m["trivial_fix_all_primes"])})
    report("G33", g33, f"tested {len(tested)} of {ncells}; swept "
                       f"{tested_swept}, agreeing {tested_agree}")

    P = basis_change(7)
    Pinvm = None
    detP = None
    basis_rows = []
    Pfr = [[Fr(v) for v in row] for row in P]
    detP = det_exact(Pfr)
    Pi_ = inv_exact(Pfr)
    for m in census_cells[:4]:
        E = encoding_matrix(tuple(m["perm"]), m["direction"])
        for p in (5, 7):
            Ep = mat_to_fp(E, p)
            Pp = mat_to_fp(Pfr, p)
            Pip = mat_to_fp(Pi_, p)
            Econj = mat_mul_fp(Pp, mat_mul_fp(Ep, Pip, p), p)
            d0 = kernel_dim_fp(mat_sub_fp(Ep, eye_fp(NV), p), p)
            d1 = kernel_dim_fp(mat_sub_fp(Econj, eye_fp(NV), p), p)
            c0 = mat_pow_fp(mat_sub_fp(eye_fp(NV), Ep, p), 3, p) == eye_fp(NV)
            c1 = mat_pow_fp(mat_sub_fp(eye_fp(NV), Econj, p), 3, p) == eye_fp(NV)
            basis_rows.append({"role": m["role"], "p": p, "fix_before": d0,
                               "fix_after": d1, "criterion_before": c0,
                               "criterion_after": c1})
    basis_ok = all(r["fix_before"] == r["fix_after"] and
                   r["criterion_before"] == r["criterion_after"]
                   for r in basis_rows)
    g34 = gate("G34", "THE CHANGE-OF-BASIS SELF-TEST.  The record datum space "
               "is re-based by a declared element of GL_6(F_p), measured "
               "non-trivial by its determinant and by the fact that it is not "
               "the identity, and both decision quantities -- the fixed-space "
               "dimension and the order criterion -- are recomputed in the new "
               "basis and are unchanged.  The invariance is analytically "
               "forced and is reported at that strength; what the gate "
               "measures that is not forced is that the action is non-trivial "
               "and that the recomputation is taken INSIDE the new basis",
               basis_ok and detP != 0 and P != eye_fp(NV) and
               len(basis_rows) > 0,
               {"determinant_of_the_declared_basis_change": str(detP),
                "basis_change_is_non_trivial": P != eye_fp(NV),
                "rows": basis_rows})
    report("G34", g34, f"basis invariance {basis_ok}; det {detP}; nontrivial "
                       f"{P != eye_fp(NV)}")
    say("")

    # ---------------------------------------------------------------- 9 ---
    say("------------------------------------------------------------------")
    say("9. THE VERDICT")
    say("------------------------------------------------------------------")
    progress("verdict")
    src1 = crit_total_hits
    src2 = mod_equal
    src3 = len(set(thm_admissible))
    restriction = live_full
    census_empty = (src1 == 0 and src2 == 0 and src3 == 0)
    covered = crit_not_hits
    qual_cov = coverage_qualifier(covered, crit_total_cells)
    qual_emp = emptiness_qualifier(qual_cov, thm_holds, floor_prime)
    verdict = derive_verdict(any_survivor, census_empty, found_ok,
                             bool(empty_at_grown), d3_constructed)
    # the motivated sub-family's outcome, re-derived here with EVERY argument
    # measured -- the reachability booleans included, which are not yet
    # available where the sub-family is censused
    verdict_motivated_measured = derive_verdict(
        mot_surv > 0, mot_census_empty, found_ok, bool(empty_at_grown),
        d3_constructed)
    obstruction = (
        "THE MASTER EQUATION: S1a, S1b and S3 force I - E = alpha^-1 rho "
        "alpha, with rho the conjugation action of Sigma_pi on the image; "
        "every wall below is a reading of it.  THE ORDER OBSTRUCTION "
        "(rho^ord = I): S1a (BRG's registered commuting square), S1b "
        "(additivity) and S3 (BRG's registered injectivity horn) jointly force "
        "(I - E)^ord(pi) = I over F_p -- equivalently E = 2I at an involution "
        "and E^2 - 3E + 3I = 0 at an order-3 wing symmetry -- and HA's "
        "record-is-metric readout satisfies it at "
        f"{src1} of {crit_total_cells} (cell, prime, order) rows, and at NO "
        f"prime >= {floor_prime} whatever, by the READOUT-PROFILE THEOREM: "
        "every row of the readout has one of two entry multisets, so row 0 is "
        "a 0/1 unit vector, and the criterion read at row 0 forces p to divide "
        "an integer witness whose gcd admits no prime >= 5.  It is ARENA-FREE: "
        "no cardinality, no p-part, no census enters the derivation, and it "
        "SUBSUMES the fixed-point mismatch, which is its first-order shadow.  "
        "For the MODULE clause the obstruction is sharper still -- THE "
        "PERMUTATION-MODULE OBSTRUCTION (rho = rho_V(pi)): S1c-module forces "
        "E = I - rho_V(pi), and the record datum space carries the S_3 "
        "PERMUTATION module, so I - rho_V(pi) always annihilates the all-ones "
        "link vector while E, being invertible, never does -- a wall that "
        "clears the other two and kills the candidate anyway.")
    quals.update({
        "covariant_cells": qualifier_value("covariant_cells", ncells),
        "declared_primes": qualifier_value("declared_primes",
                                           len(sweep_primes())),
        "equivariant_identifications": qualifier_value(
            "equivariant_identifications", len(equi)),
        "precheck_survivors_per_prime": surv_by_prime,
        "module_candidates_stillborn": qualifier_value(
            "module_candidates_stillborn",
            sum(1 for m in cells_meta if m["role"] == "module")),
        "census_rows": qualifier_value("census_rows", len(census_rows)),
        "rows_live_at_S1a_S1b": qualifier_value("rows_live_at_S1a_S1b",
                                                live_s1ab),
        "rows_admitting_an_injective_candidate": qualifier_value(
            "rows_admitting_an_injective_candidate", live_full),
        "order_criterion_rows": qualifier_value("order_criterion_rows",
                                                crit_total_cells),
        "order_criterion_satisfied": qualifier_value(
            "order_criterion_satisfied", crit_total_hits),
        "module_obstruction_rows": qualifier_value("module_obstruction_rows",
                                                   len(mod_rows)),
        "motivated_cells": qualifier_value("motivated_cells", mot_cells),
        "motivated_precheck_survivors": qualifier_value(
            "motivated_precheck_survivors", mot_surv),
        "profile_theorem_triples": qualifier_value("profile_theorem_triples",
                                                   len(thm_rows)),
        "coverage_qualifier": qual_cov,
        "emptiness_qualifier": qual_emp,
        "identification_qualifier": ident_qual,
        "verdict_at_the_motivated_sub_family": verdict_motivated,
        "spectral_meeting_primes": meet_primes,
    })
    # every recorded numeric qualifier, re-derived here from its own source
    qual_ledger = {
        "covariant_cells": (quals["covariant_cells"], ncells),
        "declared_primes": (quals["declared_primes"], len(sweep_primes())),
        "equivariant_identifications": (quals["equivariant_identifications"],
                                        len(equi)),
        "census_rows": (quals["census_rows"], len(census_rows)),
        "order_criterion_rows": (quals["order_criterion_rows"],
                                 crit_total_cells),
        "module_obstruction_rows": (quals["module_obstruction_rows"],
                                    len(mod_rows)),
        "motivated_cells": (quals["motivated_cells"], mot_cells),
        "profile_theorem_triples": (quals["profile_theorem_triples"],
                                    len(thm_rows)),
        "precheck_survivors_at_p7": (quals["precheck_survivors_at_p7"],
                                     surv_by_prime[pref]),
    }
    qual_ok = all(a == b for (a, b) in qual_ledger.values())
    say(f"  source 1 -- the order-criterion sweep over the WHOLE covariant "
        f"family        : {src1} of {crit_total_cells}")
    say(f"  source 2 -- the permutation-module equality count, which runs no "
        f"criterion   : {src2} of {len(mod_rows)}")
    say(f"  source 3 -- the readout-profile theorem's admitted primes, which "
        f"runs no F_p  : {src3} (over {len(thm_rows)} witnesses)")
    say(f"  a coverage check on the census (a RESTRICTION of source 1, not a "
        f"source)      : {restriction} of {len(census_rows)}")
    say(f"  a candidate PASSES the precheck                                   "
        f"           : {any_survivor}")
    say(f"  FOUND reachable / EMPTY reachable                                 "
        f"           : {found_ok} / {bool(empty_at_grown)}")
    say("")
    say(f"  ==>  {verdict}")
    say(f"       the FOUND half, named by measurement : {ident_qual}")
    say(f"       the EMPTY half, named by measurement : {qual_emp}")
    say(f"       at the motivated sub-family          : {verdict_motivated}")
    say("")
    g35 = gate("G35", "THE VERDICT IS DERIVED HERE, INSIDE THE GATE, FROM "
               "THREE SOURCES THAT ARE GENUINELY INDEPENDENT COMPUTATIONS, "
               "WITH BOTH BRANCHES REACHABLE AND BOTH HALVES OF THE NAME "
               "MEASURED.  Source 1 is the order-criterion sweep over the "
               "WHOLE covariant family, which runs no census; source 2 is the "
               "permutation-module equality count, which runs no criterion; "
               "source 3 is the readout-profile theorem, which evaluates no "
               "matrix over F_p at all and decides every prime from the "
               "integer readout's row profiles.  The census table's own "
               "injective column is the criterion RESTRICTED to the declared "
               "cells -- a coverage check on the census, forced twice over by "
               "cardinality, and it is reported as a disclosure and not "
               "conjoined here.  All three sources return zero, a candidate is "
               "measured to PASS the precheck, and the FOUND and EMPTY "
               "branches are both measured reachable, so the pre-registered "
               "outcome is RSQ-SQUARE-FOUND-BRIDGE-EMPTY; the FOUND half "
               "carries the identification class of its survivors and the "
               "EMPTY half carries the theorem's prime scope, both DERIVED "
               "here, and the verdict-flip, ident-flip and emptiness-flip "
               "mutants prove each derivation can fail on its own.  The "
               "motivated sub-family's own outcome is re-derived here with "
               "every argument measured and must agree with the one printed at "
               "the census",
               verdict == "RSQ-SQUARE-FOUND-BRIDGE-EMPTY" and
               src1 == 0 and src2 == 0 and src3 == 0 and any_survivor and
               found_ok and bool(empty_at_grown) and d3_constructed and
               ident_qual == "FOUND-ONLY-AT-UNMOTIVATED-IDENTIFICATIONS" and
               qual_emp == f"UNIVERSAL-BY-THEOREM-AT-EVERY-PRIME-GE-"
                           f"{floor_prime}" and
               verdict_motivated == "RSQ-NO-COMPATIBLE-SQUARE" and
               verdict_motivated_measured == verdict_motivated,
               {"verdict": verdict,
                "verdict_at_the_motivated_sub_family_all_arguments_measured":
                    verdict_motivated_measured,
                "source_1_order_criterion_hits": src1,
                "source_2_module_equalities": src2,
                "source_3_primes_admitted_by_the_profile_theorem": src3,
                "restriction_census_live_rows": restriction,
                "a_candidate_passes_the_precheck": any_survivor,
                "found_reachable": found_ok,
                "empty_reachable": bool(empty_at_grown),
                "d3_constructed": d3_constructed,
                "identification_qualifier": ident_qual,
                "emptiness_qualifier": qual_emp,
                "coverage_qualifier": qual_cov,
                "verdict_at_the_motivated_sub_family": verdict_motivated,
                "obstruction": obstruction})
    report("G35", g35, f"verdict {verdict} / {ident_qual} / {qual_emp}")
    g36 = gate("G36", "THE COVERAGE QUALIFIER IS MEASURED, AND ITS OWN "
               "FUNCTION IS CALIBRATED THE OTHER WAY.  The rows NOT satisfying "
               "the criterion are counted directly in the sweep, not "
               "subtracted from its total, and they are measured to be all of "
               "them: every (cell, prime, wing-order) row is covered by the "
               "arena-free order obstruction, none is left to a cardinality "
               "argument -- which is the respect in which this wall is "
               "stronger than LCB's.  The qualifier function must report "
               "PARTIAL on a partial input, evaluated here through the same "
               "call, so a qualifier asserted rather than measured cannot pass",
               qual_cov == "UNIVERSAL-FOR-THIS-FAMILY" and
               coverage_qualifier(3, 5) == "PARTIAL-3-OF-5" and
               covered == crit_total_cells and
               completeness([crit_total_hits, covered], crit_total_cells),
               {"rows_covered_arena_free": covered,
                "rows_total": crit_total_cells,
                "qualifier": qual_cov,
                "qualifier_reports_PARTIAL_on_a_partial_input":
                    coverage_qualifier(3, 5) == "PARTIAL-3-OF-5"})
    report("G36", g36, f"{covered}/{crit_total_cells} covered arena-free")
    say(f"  the qualifier ledger: {sum(1 for (a, b) in qual_ledger.values() if a == b)} "
        f"of {len(qual_ledger)} recorded qualifiers equal their recomputed "
        f"source")
    g48 = gate("G48", "EVERY RECORDED QUALIFIER EQUALS ITS RECOMPUTED SOURCE.  "
               "The numeric qualifiers carried into the receipt are re-derived "
               "here from the measurements they name and compared one by one, "
               "so a qualifier replaced by a typed string is caught in the "
               "delivered run and not only by a synthetic probe",
               qual_ok and len(qual_ledger) > 0,
               {"ledger": {k2: list(v2) for k2, v2 in qual_ledger.items()},
                "all_agree": qual_ok})
    report("G48", g48, f"{sum(1 for (a, b) in qual_ledger.values() if a == b)}/"
                       f"{len(qual_ledger)} qualifiers agree")
    probes = {
        "completeness_rejects_a_dropped_cell": completeness([1, 2], 4) is False,
        "coverage_qualifier_reports_PARTIAL_when_partial":
            coverage_qualifier(3, 5) == "PARTIAL-3-OF-5",
        "qualifier_value_returns_what_it_is_given":
            qualifier_value("probe", 17) == 17,
        "s2_rejects_a_constant_stratification":
            s2_stratification_carried([5]) is False,
        "stillborn_mismatch_is_computed":
            stillborn_mismatch(343, 1) == "343 : 1",
        "subsumption_rejects_the_wrong_direction":
            subsumption_holds(5, 3) is False,
        "precheck_rejects_a_nonzero_fixed_space":
            precheck(1, 1, 7)[0] is False,
        "found_branch_rejects_a_violating_witness":
            found_branch(1, True, 0, True, True) is False,
        "empty_branch_reports_what_it_is_given":
            empty_branch(False) is False,
        "meeting_verdict_rejects_a_non_meeting":
            meeting_verdict(3, [4, 6], [4, 6]) is False,
        "teeth_exempt_only_at_the_identity":
            teeth_exempt((1, 0), (0, 1)) is False,
        "ladder_measured_is_the_identity_on_its_input":
            ladder_measured(360) == 360,
        "derive_verdict_returns_NO_COMPATIBLE_SQUARE_when_all_stillborn":
            derive_verdict(False, True, True, True, True) ==
            "RSQ-NO-COMPATIBLE-SQUARE",
        "identification_qualifier_names_a_motivated_survivor":
            identification_qualifier(1, 1) ==
            "FOUND-AT-A-MOTIVATED-IDENTIFICATION",
        "identification_qualifier_names_an_empty_precheck":
            identification_qualifier(0, 0) ==
            "NO-SURVIVOR-AT-ANY-IDENTIFICATION",
        "emptiness_qualifier_declines_the_theorem_name_without_the_theorem":
            emptiness_qualifier("UNIVERSAL-FOR-THIS-FAMILY", False,
                                floor_prime) == "UNIVERSAL-FOR-THIS-FAMILY",
        "emptiness_qualifier_passes_a_partial_coverage_through":
            emptiness_qualifier("PARTIAL-3-OF-5", True, floor_prime) ==
            "PARTIAL-3-OF-5",
        "the_theorem_admits_a_witness_divisible_by_a_large_prime":
            admissible_primes_of_witness([11, 22, 0, 0, 0, 0],
                                         floor_prime) == [11],
        "the_theorem_rejects_a_witness_with_a_unit_gcd":
            admissible_primes_of_witness([1, 2, 0, 0, 0, 0],
                                         floor_prime) == [],
        "the_theorem_honours_its_declared_prime_floor":
            admissible_primes_of_witness([2, 4, 0, 0, 0, 0],
                                         floor_prime) == [],
        "the_all_prime_test_flags_an_identically_zero_identity":
            all_prime_hits([[0] * NV for _ in range(NV)], floor_prime) ==
            ["EVERY-PRIME"],
        "module_independence_rejects_an_invertible_module_E":
            module_independence(True, True, False) is False,
        "master_equation_rejects_a_mismatch":
            master_equation_holds((0, 1), (1, 0)) is False,
        "spectral_multiplicity_returns_what_it_measures":
            spectral_multiplicity(2, 5) == 2,
        "the_base_fingerprint_separates_different_inputs":
            base_fingerprint(["a"], [5], [2], [1]) !=
            base_fingerprint(["b"], [5], [2], [1]),
        "the_anchor_policy_is_fatal_on_a_failure":
            anchor_policy_fatal(1) is True,
        "the_motivated_survivor_count_is_read_from_the_rows":
            motivated_precheck_survivors([{"precheck": "PASS"}]) == 1,
        # the two functions that carry verdict sources 1 and 2, and the
        # profile reader that carries source 3's premise
        "the_order_criterion_rejects_an_invertible_non_root":
            order_criterion([[Fr(3 if i == j else 0) for j in range(NV)]
                             for i in range(NV)], pref, 2) is False,
        "the_order_criterion_accepts_the_synthetic_positive_control":
            order_criterion(synth_ok_Efr, pref, 3) is True,
        "the_polynomial_writing_accepts_the_involution_root":
            order_criterion_polynomial(
                [[Fr(2 if i == j else 0) for j in range(NV)]
                 for i in range(NV)], pref, 2) is True,
        "the_module_obstruction_rejects_a_non_module_E":
            module_obstruction_measured(
                [[Fr(1 if i == j else 0) for j in range(NV)]
                 for i in range(NV)], (0, 2, 1), pref)[0] is False,
        "the_row_profile_reads_the_row_it_is_given":
            row_profiles([[0, 0, 0, 1, 1, 2]]) == [(0, 0, 0, 1, 1, 2)],
        "the_extended_prime_range_is_sieved":
            extended_primes(floor_prime, 11) == [5, 7, 11],
        "the_sufficiency_census_keeps_every_pattern":
            len(sufficiency_patterns([1, 2, 3])) == 3,
    }
    probes_ok = all(probes.values())
    say(f"  the instrument probe: {sum(1 for v in probes.values() if v)} of "
        f"{len(probes)} declared helpers return the KNOWN answer on a "
        f"synthetic input whose correct value is fixed in advance")
    g37 = gate("G37", "EVERY DECISION HELPER IS PROBED WITH ITS OWN NEGATIVE "
               "CASE.  Each helper that carries a verdict, a qualifier, a "
               "completeness clause or a branch decision is fed a SYNTHETIC "
               "input whose correct answer is fixed in advance and must return "
               "it -- the completeness clause must reject a dropped cell, the "
               "coverage qualifier must report PARTIAL when the coverage is "
               "partial, the precheck must reject a nonzero fixed space, the "
               "verdict function must return the NO-COMPATIBLE-SQUARE branch "
               "when nothing survives.  A helper blinded to always answer one "
               "way cannot pass here, so no gate below rests on a clause that "
               "could not have come out otherwise",
               probes_ok, probes)
    report("G37", g37, f"{sum(1 for v in probes.values() if v)}/{len(probes)} "
                       f"helper probes correct")
    if anchor_policy_fatal(ANCHOR_POLICY["failures"]):
        ANCHOR_POLICY["fatal"] = 1
    policy_probe = anchor_policy_fatal(1) is True
    g38 = gate("G38", "THE ANCHOR POLICY IS FAIL-CLOSED AND MEASURED.  Every "
               "committed number this unit reuses carries an assertion whose "
               "failure kills the run; the failure is recorded and the run is "
               "carried to the totals block so that every falsifier is scored "
               "at a gate against the same denominators as the honest run.  "
               "The count of anchor FAILURES is gated here, and the policy "
               "function is calibrated the other way through the same call -- "
               "it must report FATAL on a synthetic single failure -- so an "
               "instrument that softened the assertions into warnings is "
               "caught by the calibration and not only by the count",
               ANCHOR_POLICY["failures"] == 0 and len(ANCHORS) > 0 and
               policy_probe,
               {"anchors": len(ANCHORS),
                "anchor_failures": ANCHOR_POLICY["failures"],
                "policy_reports_fatal_on_one_failure": policy_probe,
                "fatal": ANCHOR_POLICY["fatal"]})
    report("G38", g38, f"{len(ANCHORS)} anchors, {ANCHOR_POLICY['failures']} "
                       f"failures")
    say("")
    disclose("X01", "The pin's phrase 'the encoding V: F_p^3 -> F_p^6' is read "
             "here as: the record datum space at d = 3 is F_p^6 (the six link "
             "counts at a site of a 3-dimensional chart), and the "
             "record-is-metric readout is the endomorphism of that space with "
             "determinant 8 and spectrum {1,1,1,2,2,2}.  That is the object "
             "R2-LCB's F-10(d) measured and the only reading under which the "
             "stated determinant and spectrum are correct.",
             {"record_datum_space": "F_p^6", "determinant": 8})
    disclose("X07", "FORCED CLAUSES, DISCLOSED AND NOT CONJOINED (RUNBOOK 14 "
             "addendum, v13 #208).  (a) The census table's 'rows admitting an "
             "injective candidate' column is the ORDER CRITERION restricted to "
             "the declared cells -- a coverage check on the census, not an "
             "independent source -- and it is forced twice over: no census row "
             "has p^6 <= |G_C|, and v_p(|G_C|) <= 1 at every declared prime, so "
             "every additive candidate at the native arena has image of order "
             "at most p and injectivity fails on cardinality alone.  (b) The "
             "module table's two structural columns are analytically forced: "
             "(I - rho_V) kills the all-ones vector because rho_V is a "
             "permutation matrix, and E never does because E is invertible; "
             "the family-wide counts are reported as the reach of that "
             "algebra, not as a contingent measurement.  (c) The two declared "
             "extensions X-NOSQUARE and X-FLATFIX cannot pass off the zero "
             "record: E_tilde - I is invertible and the fixed-label count is "
             "1 + 7*#{k : r_k = 0}.  (d) The matrix-power and polynomial "
             "writings of the criterion are ONE condition in two encodings.  "
             "None of these is a must-pass conjunct of the verdict gate.",
             {"census_rows_with_p6_at_most_the_group_order": card_admits,
              "v_p_of_the_completion_group_order": vp_gc,
              "family_wide_pairs_where_E_kills_the_all_ones": ek_zero_pairs})
    disclose("X08", "THE FOUND HALF'S SCOPE.  The precheck's survivors are "
             "measured to be exactly the identifications with no stated "
             "motivation: the S_3-equivariant identifications and HA's own "
             "sym_index ordering are STILLBORN at every declared prime, in "
             "both directions, so the FOUND half of the verdict is true of the "
             "arbitrary relabellings of the six metric slots and false of "
             "every identification anybody has argued for.  Restricted to that "
             "motivated sub-family this instrument's own pre-registered "
             "outcome is RSQ-NO-COMPATIBLE-SQUARE, and both readings ship.",
             {"motivated_cells": mot_cells,
              "motivated_precheck_survivors": mot_surv,
              "generic_cells": generic_cells,
              "verdict_at_the_motivated_sub_family": verdict_motivated})
    disclose("X09", "SCOPES OF THE CONTROL MEASUREMENTS.  The homomorphism "
             "checks of the in-arena control and of BREAK-HOM run over the "
             "declared grid {0,1}^6 x {0,1}^6 = 4,096 pairs, where coordinate "
             "sums never exceed 2 and modular wrap-around is not exercised; "
             "the master equation is verified on the generating set and on a "
             "declared sample of records, and is equivalent to the square -- "
             "which is verified at every record cell -- given that alpha is a "
             "homomorphism.  The sufficiency census verifies the square at a "
             "declared sample of records per pattern, exhaustively at the one "
             "distinguished pattern.  BREAK-HOM is built at the NATIVE 8-label "
             "arena with a rank-1 exponent, not at the grown arena.",
             {"homomorphism_grid": ctrl.get("homomorphism_grid"),
              "master_equation_sample": ctrl.get("master_equation_sample"),
              "sufficiency_sample_per_pattern": len(suff_sample)})
    disclose("X02", "Route A and route B are genuinely different computations "
             "over SHARED data: both read the same measured subgroup set and "
             "the same encoding matrix.  Route A decides by Gaussian "
             "elimination; route B decides from a delta-exponent table built "
             "by permutation arithmetic with no linear algebra in it, over an "
             "explicit enumeration of the covector space.  Route C verifies "
             "the permutation square literally.  Neither B nor C reads A.",
             {"taint": ROUTE_CALLS["taint"]})
    disclose("X03", "The census's exhaustive enumeration is scoped: route B "
             "enumerates every cyclic subgroup of order p and every covector "
             "PROJECTIVELY, restoring the measured redundancy p-1, and that "
             "quotient is calibrated at a declared cell and prime against the "
             "FULL p^6 enumeration.  The order-criterion sweep, which carries "
             "the verdict, is exhaustive over the whole covariant family at "
             "every declared prime with no sampling anywhere.",
             {"projective_calibrated_at": {"prime": pcal}})
    disclose("X04", "The reduced carrier is BUILT as explicit permutations "
             "only at the declared build primes (its size is p^(k+3)); rho is "
             "reduced and the arena coordinate reported at every declared "
             "prime.  This is a declared computational cap, not a measured "
             "boundary.",
             {"build_primes": carrier_primes(),
              "declared_primes": sweep_primes()})
    disclose("X05", "The in-arena FOUND control is a control, not a bridge: "
             "its encoding is the SYNTHETIC I - rho, not HA's readout, and no "
             "record, metric, chart or readout of the deformation side enters "
             "it.  What it establishes is exactly one thing -- that EMPTY is "
             "not caused by the arena, the prime or the instrument, because "
             "the same arena and the same prime return FOUND for a different "
             "encoding.  It does not establish that bridges exist in-family at "
             "scale, and it does not satisfy the module clause, which the "
             "permutation-module obstruction kills for a different and "
             "universal reason.  Its square is an algebraic identity in the "
             "record once the two measured premises hold (the wing symmetry "
             "normalises the generators with the declared exponents, and they "
             "commute), and it is reported at that strength.",
             {"arena_labels": n_star, "prime": pc,
              "rung_earned": "EMPTY is not an arena, prime or instrument "
                             "artefact",
              "rung_not_earned": "bridges in-family at scale"})
    disclose("X06", "The set-level relaxation is NOT decided here.  Dropping "
             "S1b (additivity) removes the order criterion's derivation, and "
             "the precheck's fixed-point argument is then the only arena-free "
             "constraint; at the NATIVE arena the set level is closed anyway "
             "because |V| = p^6 exceeds |G_C| = 5,040 at every declared prime, "
             "but at the grown arena it is open and is recorded as such.",
             {"native_arena_completion_group_order": len(GC)})

    # --------------------------------------------------------------- 10 ---
    say("------------------------------------------------------------------")
    say("10. TOTALS")
    say("------------------------------------------------------------------")
    mustp = [g for g in GATES if g["must_pass"]]
    failed = [g["id"] for g in mustp if not g["passed"]]
    ext = sum(1 for a in ANCHORS if not a["source"].startswith("this file"))
    slf = len(ANCHORS) - ext
    say(f"  anchors                  {len(ANCHORS):6d}  "
        f"({ext} COMMITTED-NUMBER anchors against other units' receipts and "
        f"papers, {slf} ARTIFACT-HASH pins of other units' files)")
    say(f"  gates                    {len(GATES):6d}")
    say(f"  must-pass gates          {len(mustp):6d}")
    say(f"  must-pass failures       {len(failed):6d}  {failed}")
    say(f"  disclosures              {len(DISCLOSURES):6d}")
    say("=" * 78)
    return {
        "tables": tables, "qualifiers": quals, "verdict": verdict,
        "obstruction": obstruction,
        "failed": bool(failed) or ANCHOR_POLICY["fatal"] > 0,
        "hash_pins": hp,
        "totals": {"anchors": len(ANCHORS), "anchors_external": ext,
                   "anchors_self": slf, "gates": len(GATES),
                   "must_pass_gates": len(mustp),
                   "must_pass_failures": len(failed),
                   "disclosures": len(DISCLOSURES),
                   "covariant_cells": ncells,
                   "census_rows": len(census_rows),
                   "order_criterion_rows": crit_total_cells},
    }


# ==========================================================================
#                          THE MUTANT HARNESS
# ==========================================================================

def run_mutant_harness():
    say("--- 11. THE MUTANT HARNESS (every declared mutant must exit 1) ---")
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
    say(f"  {'mutant':20s}{'exit':6s}{'killed':9s}named kills")
    for row in rows:
        say(f"  {row['mutant']:20s}{row['exit']:<6d}{str(row['killed']):9s}"
            f"{','.join(row['named_kills'])[:50]}")
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
        "schema": "rsq-reposed-square-receipt-v1",
        "pin": "v13/note-rsq-reposed-square-pin.md",
        "pin_commit": "d9e3a66",
        "source_sha256": hashlib.sha256(src.encode()).hexdigest(),
        "python": platform.python_version(),
        "arithmetic": "integers / fractions.Fraction / exact F_p; no floats",
        "hash_pins": R["hash_pins"],
        "declarations": json.loads(json.dumps(DECL, default=str)),
        "anchors": ANCHORS,
        "gates": GATES,
        "disclosures": DISCLOSURES,
        "tables": json.loads(json.dumps(R["tables"], default=str)),
        "qualifiers": json.loads(json.dumps(R["qualifiers"], default=str)),
        "totals": R["totals"],
        "verdict": R["verdict"],
        "obstruction": R["obstruction"],
    }
    mut_rows, survivors, never_falsified = run_mutant_harness()
    receipt["mutants"] = mut_rows
    receipt["never_falsified"] = never_falsified
    receipt["totals"]["mutants"] = len(mut_rows)
    receipt["totals"]["mutant_survivors"] = len(survivors)
    say("")

    if WRITE_ARTIFACTS:
        with open(os.path.join(HERE, "rsq_reposed_square_output.txt"), "w",
                  encoding="utf-8") as fh:
            fh.write("\n".join(OUT) + "\n")
        with open(os.path.join(HERE, "rsq_reposed_square_receipt.json"), "w",
                  encoding="utf-8") as fh:
            json.dump(receipt, fh, indent=1, sort_keys=True, default=str)
            fh.write("\n")
    else:
        progress("falsification-selftest: artifacts NOT written")
    progress("done")
    return 0 if (not R["failed"] and not survivors and not never_falsified) else 1


if __name__ == "__main__":
    sys.exit(main())

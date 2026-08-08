#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""
BRG -- THE MORPHISM-CENSUS BRIDGE  (gravity <-> transport geometry)
===================================================================

Pin: v13/note-brg-bridge-pin.md (STRICT, frozen, sha256 56ce4a7e2dee...,
immutable base commit b632f59).  Binding: HA section 14's four requirements
(carrier functor as data; morphism census; two-way gates both reachable;
arena-invariance gating), RUNBOOK 13 (verdict-in-gate with computed
qualifiers, verdict-flip mutants, cell-completeness, independent routes),
RUNBOOK 14 (symmetry self-tests, all addenda) and RUNBOOK 15 (declared-arena
discipline, all addenda).

The two sides, each rebuilt here from its own committed receipt's data:

  DEFORMATION SIDE (HA)  C_HA(p) = F_p^k x F_p^d, the front sector times the
      address register; <R_HH> acts as translation of the register by
      rho mod p (HA G29), so <R_HH> = Z/p.  rho = (1/6, 1/6) exactly.
  TRANSPORT SIDE (NT/GEN/XBA/PSI)  C_TR = the wing carrier = the system pair
      times the pointer pair; W = Sigma (x) Sigma the wing exchange,
      D = (Sigma Q^T Sigma Q) (x) I the completion defect, <W,D> dihedral
      of order 2*ord(D).  PSI's one law D = [P_W, u] with P_W an involution
      FORCES W D W = D^-1, hence the dihedral form and the order formula, for
      every base the law covers -- measured here over a randomised family
      sweep with a seed derived from declared data alone.

Exact arithmetic only: integers, fractions.Fraction and exact F_p.  No float
or complex literal, and no float()/complex() call, appears in this source;
the scanner that measures that is itself validated by a synthetic injection
it must flag.

MUTANT DISCIPLINE (RUNBOOK 14 addendum, v13 #208): every mutation below is a
mutation of an INSTRUMENT helper.  No gate predicate, and no function that
registers a gate, references mutant identity; the AST guard measures that and
is validated by a synthetic sample it must flag.

Usage:
    python3.13 brg_bridge_exact.py                  # delivery run
    python3.13 brg_bridge_exact.py --mutant NAME    # one mutant; must exit 1
    python3.13 brg_bridge_exact.py --falsification-selftest
        (the full run and the whole mutant harness, WITHOUT writing artifacts)
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

# The functor-level census counts equivariant carrier maps by an exact integer
# power; those integers have tens of thousands of digits and only their digit
# COUNT is ever printed.  Exact integers throughout -- this raises a printing
# limit, not a precision one.
sys.set_int_max_str_digits(200000)

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
    # --- anchor mutants (each must die exit-1 at a named anchor) ----------
    "anchor-ha-sha":       "the HA receipt hash pin is perturbed",
    "anchor-nt-sha":       "the NT receipt hash pin is perturbed",
    "anchor-gen-sha":      "the GEN receipt hash pin is perturbed",
    "anchor-xba-sha":      "the XBA receipt hash pin is perturbed",
    "anchor-psi-sha":      "the PSI receipt hash pin is perturbed",
    "anchor-xbapaper-sha": "the XBA paper's hash pin is perturbed",
    "anchor-pin-sha":      "the BRG pin's own hash is perturbed",
    "anchor-gen-defect":   "the rebuilt completion defect permutation is perturbed",
    "anchor-gen-family":   "the completion-family sweep is truncated",
    "anchor-ha-rho":       "the exact-to-F_p reduction of rho is perturbed",
    "anchor-xba-orders":   "the rebuilt transport group order is perturbed",
    "anchor-soft":         "anchor failures are made non-fatal",
    # --- discipline mutants ----------------------------------------------
    "freeze-lax":          "a census datum is evaluated before the declarations freeze",
    "float-lax":           "the exact-arithmetic scanner is blinded",
    "exempt-lax":          "the mutant-identity AST scanner is blinded",
    # --- functor / predicate mutants --------------------------------------
    "nontrivial-lax":      "the non-triviality gate accepts a collapsing functor",
    "predicate-lax":       "the equivariance clause is evaluated at the base point only",
    "equivariance-side":   "the equivariance clause composes the action on the wrong side",
    "hom-lax":             "the composition clause is dropped from the predicate",
    # --- census mutants ---------------------------------------------------
    "route-b-lax":         "the subgroup-lattice route omits the trivial subgroup",
    "route-alias":         "the second route returns the first route's own result",
    "cell-drop":           "one declared census cell is dropped from the sweep",
    "family-drop":         "one member is dropped from the completion-family sweep",
    "formula-lax":         "the equivariant-map count formula is perturbed",
    "orbit-lax":           "the union-find orbit count is perturbed",
    "scope-leak":          "an extended-family instance leaks into the committed scope",
    "dict-drop":           "one record is dropped from the dictionary census",
    # --- arena-invariance mutants -----------------------------------------
    "prime-single":        "the prime sweep is collapsed to one prime",
    "tracking-blind":      "the prime-tracking control is made prime-uniform",
    "relabel-lax":         "the relabelling self-test relabels nothing",
    "conj-lax":            "the conjugation self-test conjugates by the identity",
    "cache-lax":           "the self-test's fresh-evaluation path reads the memo cache",
    "cache-unused":        "the memo cache is never looked up",
    "selftest-select":     "the self-test's tested set is selected by the verdicts",
    "spectrum-swap":       "the comparator reads the holonomy spectrum where the "
                           "defect spectrum belongs",
    "comparator-self":     "the abstract/permutation comparator is routed through the "
                           "audited component",
    # --- reachability and held-out mutants ---------------------------------
    "heldout-leak":        "the morphism is fitted on the held-out orbits",
    "teeth-off":           "the reflection-valued extension is silently rotation-valued",
    "found-block":         "the synthetic compatible pair is made incompatible",
    "empty-block":         "the synthetic incompatible pair is made compatible",
    # --- obstruction and verdict -------------------------------------------
    "obstruction-misname": "the named obstruction is replaced by a cardinality claim",
    "abelianization-lax":  "the commutator subgroup is computed as the trivial group",
    "verdict-flip":        "the verdict derivation returns a hand-typed string",
    "ambiguity-lax":       "the under-determined instances' candidate sets are "
                           "truncated to a single guess",
    "break-blind":         "the declared structure-breaking map is replaced by its "
                           "accepted counterpart",
    "class-drop":          "one of the committed completion classes is dropped from "
                           "the extended sweep",
    "invariance-lax":      "the arena-invariance test is read as a union instead of "
                           "an intersection",
    "dict-scope-lax":      "the committed-scope dictionary census reads the extended "
                           "family",
    "quantity-lax":        "a declared held-out quantity is read off the wrong action",
    # --- the obstruction at family strength ---------------------------------
    "radical-inject":      "an instance of defect order 5 is injected into the "
                           "radical computation's instance set",
    "cauchy-narrow":       "the declared group zoo is narrowed to dihedral groups",
    "reverse-alias":       "the reverse census's non-trivial count is read off the "
                           "forward count",
    "psi-noninvolutive":   "the one-law sweep draws a general permutation where the "
                           "law declares an involution",
    "model-lax":           "the abstract model is built as the abelian group of the "
                           "same order",
    # --- the admissible-prime cells ----------------------------------------
    "live-order-lax":      "the live-cell group map is built from the defect itself "
                           "instead of its element of order p",
    "collapse-lax":        "the declared orbit-collapsing carrier map is made "
                           "constant",
    "sector-lax":          "the low-defect sector's declared bound is lowered",
    "landau-lax":          "the species-4 contingency sweep is run in the "
                           "nine-label arena",
    # --- instrument completeness --------------------------------------------
    "tiny-drop":           "one declared tiny validation cell is dropped",
    "arena-order-lax":     "the tiny arena's generator is built with an order that "
                           "does not divide p",
    "selftest-blind":      "one symmetry self-test applies its declared action to "
                           "the candidate the wrong way round",
    "generator-blind":     "the generator sweep replaces the swept generators by "
                           "the identity",
    "functor-cell-drop":   "one cell is dropped from the functor-level census",
    "qualifier-typo":      "one printed verdict qualifier is replaced by a typed "
                           "value",
    "count-flip":          "the emptiness decision is inverted at its own source",
}

if MUTANT is not None and MUTANT not in MUTANTS:
    sys.stderr.write(f"unknown mutant {MUTANT!r}\n")
    sys.exit(2)

# Module-level switches.  Read ONLY inside instrument helpers.
_M_HASHA = (MUTANT == "anchor-ha-sha")
_M_HASNT = (MUTANT == "anchor-nt-sha")
_M_HASGEN = (MUTANT == "anchor-gen-sha")
_M_HASXBA = (MUTANT == "anchor-xba-sha")
_M_HASPSI = (MUTANT == "anchor-psi-sha")
_M_HASXBAP = (MUTANT == "anchor-xbapaper-sha")
_M_HASPIN = (MUTANT == "anchor-pin-sha")
_M_DEFECT = (MUTANT == "anchor-gen-defect")
_M_FAMILY = (MUTANT == "anchor-gen-family")
_M_RHO = (MUTANT == "anchor-ha-rho")
_M_ORDERS = (MUTANT == "anchor-xba-orders")
_M_SOFT = (MUTANT == "anchor-soft")
_M_FREEZE = (MUTANT == "freeze-lax")
_M_FLOAT = (MUTANT == "float-lax")
_M_EXEMPT = (MUTANT == "exempt-lax")
_M_NONTRIV = (MUTANT == "nontrivial-lax")
_M_PRED = (MUTANT == "predicate-lax")
_M_SIDE = (MUTANT == "equivariance-side")
_M_HOM = (MUTANT == "hom-lax")
_M_ROUTEB = (MUTANT == "route-b-lax")
_M_ALIAS = (MUTANT == "route-alias")
_M_CELL = (MUTANT == "cell-drop")
_M_FAMDROP = (MUTANT == "family-drop")
_M_FORMULA = (MUTANT == "formula-lax")
_M_ORBIT = (MUTANT == "orbit-lax")
_M_SCOPE = (MUTANT == "scope-leak")
_M_DICT = (MUTANT == "dict-drop")
_M_ONEPRIME = (MUTANT == "prime-single")
_M_TRACK = (MUTANT == "tracking-blind")
_M_RELABEL = (MUTANT == "relabel-lax")
_M_CONJ = (MUTANT == "conj-lax")
_M_CACHE = (MUTANT == "cache-lax")
_M_CACHEOFF = (MUTANT == "cache-unused")
_M_SELSEL = (MUTANT == "selftest-select")
_M_SPECSWAP = (MUTANT == "spectrum-swap")
_M_COMPSELF = (MUTANT == "comparator-self")
_M_LEAK = (MUTANT == "heldout-leak")
_M_TEETH = (MUTANT == "teeth-off")
_M_FOUND = (MUTANT == "found-block")
_M_EMPTY = (MUTANT == "empty-block")
_M_OBST = (MUTANT == "obstruction-misname")
_M_ABEL = (MUTANT == "abelianization-lax")
_M_VERDICT = (MUTANT == "verdict-flip")
_M_AMBIG = (MUTANT == "ambiguity-lax")
_M_BREAK = (MUTANT == "break-blind")
_M_CLASS = (MUTANT == "class-drop")
_M_INVAR = (MUTANT == "invariance-lax")
_M_DICTSCOPE = (MUTANT == "dict-scope-lax")
_M_QUANT = (MUTANT == "quantity-lax")
_M_RADINJ = (MUTANT == "radical-inject")
_M_ZOO = (MUTANT == "cauchy-narrow")
_M_REVALIAS = (MUTANT == "reverse-alias")
_M_PSINONINV = (MUTANT == "psi-noninvolutive")
_M_MODEL = (MUTANT == "model-lax")
_M_LIVEORD = (MUTANT == "live-order-lax")
_M_COLLAPSE = (MUTANT == "collapse-lax")
_M_SECTOR = (MUTANT == "sector-lax")
_M_LANDAU = (MUTANT == "landau-lax")
_M_TINYDROP = (MUTANT == "tiny-drop")
_M_ARENAORD = (MUTANT == "arena-order-lax")
_M_SELFBLIND = (MUTANT == "selftest-blind")
_M_GENBLIND = (MUTANT == "generator-blind")
_M_FCELL = (MUTANT == "functor-cell-drop")
_M_QUALTYPO = (MUTANT == "qualifier-typo")
_M_COUNTFLIP = (MUTANT == "count-flip")

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
    sys.stderr.write(f"[brg] {s}\n")
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
# 2.  THE DECLARED ARENA, THE FUNCTORS, THE PREDICATE, THE HELD-OUT SET
#     (RUNBOOK 15: declared as data, before any morphism is evaluated;
#      gate G01 measures the freeze by the census-evaluation counter)
# --------------------------------------------------------------------------

DECL: dict = {
    # ---- the arena (RUNBOOK 15's six coordinates) -----------------------
    "arena": {
        "boundary": "two measured group actions: the deformation side "
                    "(C_HA(p) = F_p^k x F_p^d, <R_HH> = Z/p acting by translation "
                    "of the address register by rho mod p) and the transport side "
                    "(C_TR = system pair x pointer pair, <W,D> dihedral of order "
                    "2*ord(D))",
        "family": "7 declared primes x the committed transport instances x 2 "
                  "directions; plus the 12 rebuilt completion classes and the "
                  "whole 40,320-member completion family as declared extended scopes",
        "law": "the structure-preservation predicate SP1-SP3 below; a candidate "
               "morphism is a PAIR (phi, Phi) of a group map and a carrier map",
        "state": "the deformation side's base total record (n_sym, 0); the "
                 "transport side's initial configuration j0 = 0",
        "arena action": "the prime sweep; carrier relabelling on both sides; "
                        "conjugation of the transport group by a carrier "
                        "permutation; change of the source generator R -> R^j",
        "provenance": "four committed terminal receipts (HA, NT, GEN, XBA), "
                      "hash-pinned; every reused number read from them",
        "admission": "a candidate survives only if SP holds AND the "
                     "non-triviality clauses NT1, NT2 hold",
    },
    # ---- the deformation side, declared -----------------------------------
    "deformation_side": {
        "carrier": "C_HA(p) = F_p^k x F_p^d, k = 2 (the rank of the declared "
                   "lapse span), d = 2; size p^(k+d)",
        "group": "<R_HH> = Z/p, generated by the translation of the address "
                 "register by rho mod p (HA G29)",
        "rho_exact": "(1/6, 1/6) -- the exact rational residual at the detector "
                     "site, the same at every prime (HA 10.1)",
        "primes": [5, 7, 11, 13, 17, 19, 23],
        "records": {"G-FLAT": [1, 1, 2], "G-ANISO": [1, 4, 5],
                    "G-ANISO2": [4, 9, 13], "G-DIAG2": [2, 2, 4],
                    "G-OFFDIAG": [2, 2, 6], "G-OFFDIAG2": [3, 5, 12],
                    "G-OFFNEG": [3, 5, 4], "G-CURVED": "inhomogeneous",
                    "G-CURVOFF": "inhomogeneous"},
        "record_is_metric": "the count vector (n_e1, n_e2, n_diag) and the "
                            "components (q11, q22, q12) determine each other by "
                            "an invertible linear map (HA G28, determinant 2)",
    },
    # ---- the transport side, declared -------------------------------------
    "transport_side": {
        "carrier": "C_TR = the system pair (m^2 labels) x the pointer pair "
                   "(m^2 labels), index i = m^2 * a + p",
        "exchange": "Sigma: the label exchange (u,v) -> (v,u); W = Sigma (x) Sigma",
        "defect": "D = (Sigma Q^T Sigma Q) (x) I, Q the declared completion "
                  "permutation of the system-pair labels (GEN 8.1)",
        "group": "<W, D> = the dihedral group of order 2*ord(D) (XBA 8.1-8.3), "
                 "the form FORCED by PSI's one law: with W^2 = 1 and D = [W,u], "
                 "W D W = (W W u^-1 W u W) = u^-1 W u W = D^-1, so <W,D> is "
                 "dihedral of order 2*ord(D) whenever W is not a power of D",
        "one_law": "PSI (terminal): D(psi) = [P_W, u(psi)] = P_W u^-1 P_W u with "
                   "P_W an involution.  Everything the obstruction says about "
                   "<W,D> is a consequence of that law and holds for every base "
                   "the law covers, prepared or not.",
        "committed_instances": ["base 1 @ SP-E", "base 1 @ SP-F", "base G @ GP-E",
                                "base G @ GP-F", "base S", "base S'", "base T",
                                "species 4"],
        "extended_scope_2": "GEN's 12 rebuilt completion classes",
        "extended_scope_3": "the whole declared completion family, 8! members",
    },
    # ---- the carrier functors, declared as DATA ---------------------------
    "functors": {
        "F0-IDENT": "the identity self-functor within one arena "
                    "(carrier map = id, group map = id) -- POSITIVE CONTROL: the "
                    "census machinery must FIND it on each side",
        "F1-RECORD-COMPLETION": "the pin's declared lead.  Object part: a "
                                "dictionary delta from the deformation side's "
                                "geometry records to the transport side's "
                                "completions; group part: the induced map "
                                "<R_HH(r)> -> <W, D(delta(r))>; encoding part: "
                                "HA's record-is-metric datum (counts <-> q) "
                                "against GEN/XBA's completion datum (Q -> D). "
                                "Declared space: records x completions.",
        "F2-CARRIER": "object part Phi: C_HA -> C_TR (front sector x address "
                      "register -> pointer pair x system pair), group part "
                      "phi: Z/p -> <W,D>; the space of phi-equivariant Phi is "
                      "enumerated by orbit representatives, its size computed.",
        "F3-SPECTRUM": "the morphism-by-spectrum candidate the pin names: a "
                       "morphism is declared to exist at p iff p lies in GEN's "
                       "DEFECT order spectrum.  PRIME-TRACKING CONTROL.",
        "F4-DEGENERATE": "carrier map constant at j0, group map trivial -- "
                         "satisfies SP and is a NAMED KILL at the non-triviality "
                         "gate (DEGENERATE-COLLAPSE).",
        "F5-REVERSE": "the same data in the direction transport -> deformation.",
        "F6-BREAK-A": "NEGATIVE CONTROL WITH TEETH: carrier map = the register "
                      "doubling (f, m) -> (f, 2m), group map = the identity. "
                      "Bijective and non-degenerate; differs from an ACCEPTED "
                      "morphism (same carrier map, group map R -> R^2) only in "
                      "the group map, so the predicate must be sensitive to "
                      "exactly the structure it claims to test.",
        "F6-BREAK-B": "NEGATIVE CONTROL WITH TEETH: carrier map = the identity "
                      "with two points of different orbits transposed, group map "
                      "= the identity.",
    },
    # ---- the structure-preservation predicate, declared as DATA -----------
    "predicate": {
        "SP1": "phi is a homomorphism: phi(g h) = phi(g) phi(h) at every one of "
               "the |G_src|^2 ordered pairs (composition preserved)",
        "SP2": "phi(1) = 1",
        "SP3": "Phi is phi-equivariant: Phi(g . x) = phi(g) . Phi(x) at every one "
               "of the |G_src| x |C_src| cells (the group actions preserved)",
        "NT1": "phi is non-trivial (the group action is carried, not killed)",
        "NT2": "Phi is non-constant (the carrier is not collapsed to a point)",
        "arena_invariance": "SP references only the group actions, the composition "
                            "and carrier incidence; never a prime value, never a "
                            "label name, never a carrier index.  Measured by the "
                            "relabelling, conjugation and generator-change "
                            "self-tests (RUNBOOK 14).",
    },
    # ---- the held-out set, declared BEFORE any morphism is constructed ----
    "held_out": {
        "split_rule": "the source orbits are ordered lexicographically by their "
                      "minimal element; FIT = orbit 0 only; HELD = every other "
                      "orbit.  Sizes computed.",
        "H1": "the orbit-size multiset on each side",
        "H2": "the fixed-point count of each generator",
        "H3": "the element-order multiset of each group",
        "H4": "the source group's composition table, all |G|^2 cells",
        "H5": "the equivariance equations on every HELD orbit -- never imposed "
              "by the construction, verified afterwards",
        "construction_rule": "the morphism is fitted on the FIT orbit and extended "
                             "to every other orbit by the declared SOURCE symmetry "
                             "(front translations and a register translation "
                             "transverse to rho) carried by a declared assignment "
                             "into the target group.  Equivariance on the HELD "
                             "orbits is therefore a PREDICTION, not an imposition.",
        "extensions": {"E-ROT": "the assignment is rotation-valued (inside <D>)",
                       "E-REF": "the assignment is reflection-valued on part of "
                                "its domain (W times a rotation) -- declared "
                                "TEETH: it must FAIL the held-out check"},
    },
    # ---- the standard a FOUND at a live cell would have to meet, declared
    #      here as the successor's gate and TESTED IN NEITHER DIRECTION by
    #      this unit ----------------------------------------------------------
    "strengthened_standard": {
        "S1-ENCODING-INTERTWINING": "THE NON-NEGOTIABLE.  The functor must make a "
            "COMMUTING SQUARE at the encoding layer, not a triangle at the group "
            "layer: HA's record-is-metric linear map (determinant 2) intertwined "
            "with GEN/XBA's Q -> delta(Q) = Sigma Q^T Sigma Q.  While the encoding "
            "factorises through the group actions, nothing physical is carried.",
        "S2-CARRIER-RIGIDITY": "SP3 supplemented so that Phi is DETERMINED, not "
            "chosen -- e.g. the fixed-configuration stratification (transport: "
            "9/18/27/36/45/54/81) carried into the source stratification.",
        "S3-NON-DEGENERACY-WITH-TEETH": "NT2 replaced by injectivity on orbits, or "
            "at least a measured lower bound on |image(Phi)| as a fraction of the "
            "orbit count.",
        "S4-FUNCTORIALITY-IN-THE-FAMILY": "naturality across the declared "
            "base-change maps, so that a live cell is not an isolated coincidence "
            "at one (p, ord(D)).",
        "S5-HELD-OUT-AT-A-LIVE-CELL-WITH-A-TRANSPORTED-QUANTITY": "a computed "
            "physical quantity transported out of sample at a live cell, not "
            "equivariance alone.",
        "S6-AN-IN-ARENA-READING-OF-REQUIREMENT-4": "either the prime declared a "
            "parameter of the arena with per-prime verdicts, or a corpus-internal "
            "fixing of p.",
        "status": "REGISTERED, NOT TESTED.  No cell of any scope in this unit is "
            "evaluated against S1-S6, in either direction.",
    },
    "registered_opens": {
        "OPEN-1": "Can the reduction prime be fixed by anything other than "
                  "declaration?  Every live cell is prime-dependent by "
                  "construction, so requirement 4 excludes it however good the "
                  "transport side gets.  The successor's dichotomy: DERIVE THE "
                  "PRIME, or accept declaration-relative bridging and say so.",
        "OPEN-2": "Why do the prepared bases concentrate in the closed sector?  "
                  "The declared completion family is majority-live; every "
                  "committed instance sits in the low-defect-order band.  Is that "
                  "a selection rule of the preparation or an artifact of which "
                  "bases happen to have been built?",
    },
    "outcomes": ["BRG-MORPHISM-FOUND", "BRG-EMPTY-AT-CARRIER", "BRG-BLOCKED-AT-<object>"],
    "pins": {
        "v13/note-brg-bridge-pin.md":
            "56ce4a7e2deeaaa24dd9cedf43e117f5c0d68774d48ac62a0120786bdba99b1b",
        "v13/code/ha_successor_receipt.json":
            "542b8735daf0ebc6fc0063068e85c76f05cbca53b7f1174968f6ca79dc0068d4",
        "v13/code/nt_transport_receipt.json":
            "d256891b479a8636fe88df5e9b0f553998140f1553fdfc167662220b44eeb03e",
        "v13/code/gen_generality_receipt.json":
            "e0b2f444f6a9b82861024f7733c7230583742dfd477d9ed6037a241e7b48d292",
        "v13/code/xba_crossbase_receipt.json":
            "6015708df2a437a61955c1e194a0273b0eb712699844c9e6eb567cc3536db053",
        "v13/code/psi_curvature_receipt.json":
            "7c7b91a9257e3888f3e1048366d728b5adead82b84cc9ef36175c0ba3e99fa75",
        "v13/paper-xba-crossbase.md":
            "2041ebcd8b3c70f9d637f02764db438c393bf58f4b90a1cec2d807502f8e16f5",
    },
    "tiny_cells": {
        "TINY-A": "source Z/2 acting FREELY on 4 points -- the generator is the "
                  "fixed-point-free involution (0 1)(2 3), so the action is a "
                  "genuine Z/2-set with 2 orbits; target the Klein four group "
                  "acting regularly on 4 points.  This is the cell that exercises "
                  "the count formula's ORBIT EXPONENT above 1.",
        "TINY-B": "source Z/3 acting freely on 3 points; target the dihedral "
                  "group of order 6 acting regularly on 6 points",
        "TINY-C": "source Z/5 acting freely on 5 points; target the Klein four "
                  "group acting regularly on 4 points",
    },
    "tiny_negative_control": {
        "TINY-NEG": "NEGATIVE CONTROL FOR THE COUNT FORMULA'S HYPOTHESIS: source "
                    "declared p = 2 but with a generator of order 3 on 3 points, "
                    "so the declared group does NOT act; target the dihedral group "
                    "of order 6 acting regularly on 6 points.  The formula "
                    "|C_tgt|^#orbits is valid only for a genuine free Z/p action "
                    "and must DISAGREE with brute force here.",
    },
    "group_zoo": "the declared group list for the Lagrange+Cauchy sweep: the "
                 "cyclic groups Z/1..Z/7, the dihedral groups D_1..D_7, S_3, S_4, "
                 "A_4, A_4 x Z/2, Z/2 x Z/2, Z/2 x Z/3 and D_4 x Z/3 -- abelian "
                 "and non-abelian, dihedral and non-dihedral, swept against the "
                 "declared prime list plus 2 and 3.",
    "one_law_sweep": {
        "draws": 400,
        "points": "4 to 8",
        "seed": "sha256 of a declared byte string naming the sweep -- no "
                "wall-clock value and no operating-system entropy enters, so two "
                "runs draw the same sequence",
        "control": "a second sweep in which W is a general permutation rather "
                   "than an involution; the relation must FAIL there",
    },
    "species4_contingency": {
        "sample": 2000,
        "arena": "species 4's own sixteen-label arena (m = 4)",
        "seed": "sha256 of a declared byte string naming the sweep",
        "claim": "the two-declared-prime clause is analytically forced only at "
                 "m = 3; at m = 4 it is contingent, and a witness with ord(D) "
                 "divisible by 5*7 is exhibited",
    },
    "extension_rules": {
        "rotation": ["(d0 + 2 d1 + c) mod ord(D)  -- the declared rule", "0",
                     "(2 d0 + d1 + 2 c) mod ord(D)", "d0 mod ord(D)",
                     "(7 d0 + 5 c) mod ord(D)"],
        "reflection": "the same five rules, multiplied by W where d0 is odd",
    },
    "synthetic": {
        "SYN-FOUND": "a DECLARED SYNTHETIC compatible pair: source Z/3 acting on "
                     "F_3^2 x F_3^2 by translation by (1,1), target base T's "
                     "rebuilt <W,D> of order 6.  Synthetic because HA's own rho = "
                     "(1/6,1/6) does not reduce at p = 3 -- measured.",
        "SYN-EMPTY": "a DECLARED SYNTHETIC incompatible pair: source Z/5 acting on "
                     "F_5^2 x F_5^2, target base T's rebuilt <W,D> of order 6.",
    },
}

# The freeze falsifier lives at module scope so that no gate-registering
# function ever references mutant identity.
if _M_FREEZE:
    note_census()


# --------------------------------------------------------------------------
# 3.  PERMUTATION AND GROUP MACHINERY (exact; integers only)
# --------------------------------------------------------------------------

_CACHE: dict = {}
_CACHE_STATS = {"lookups": 0, "hits": 0, "misses": 0, "bypass": 0,
                "selftest_hits": 0}
_SELFTEST_PHASE = [False]


def pmul(a, b):
    """(a o b)(x) = a[b[x]]."""
    return [a[i] for i in b]


def pinv(a):
    o = [0] * len(a)
    for i, v in enumerate(a):
        o[v] = i
    return o


def pident(n):
    return list(range(n))


def perm_pow(a, e, fresh: bool = False):
    """a^e by repeated composition, with a memo cache.  [instrument -- mutable]"""
    key = (tuple(a), e)
    use_cache = ((not fresh) or _M_CACHE) and not _M_CACHEOFF
    if fresh and not _M_CACHE:
        _CACHE_STATS["bypass"] += 1
    if use_cache:
        _CACHE_STATS["lookups"] += 1
        if key in _CACHE:
            _CACHE_STATS["hits"] += 1
            if _SELFTEST_PHASE[0]:
                _CACHE_STATS["selftest_hits"] += 1
            return _CACHE[key]
        _CACHE_STATS["misses"] += 1
    r = pident(len(a))
    for _ in range(e):
        r = pmul(a, r)
    if use_cache:
        _CACHE[key] = r
    return r


def porder(a):
    idt = pident(len(a))
    c, cur = 1, list(a)
    while cur != idt:
        cur = pmul(list(a), cur)
        c += 1
        if c > 10 ** 6:
            raise RuntimeError("order overflow")
    return c


def pfixed(a):
    return sum(1 for i, v in enumerate(a) if i == v)


def perm_moved(a):
    return sum(1 for i, v in enumerate(a) if i != v)


def closure(gens, n):
    """The subgroup generated by gens, as a sorted list of tuples."""
    idt = tuple(pident(n))
    seen, frontier = {idt}, [idt]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                x = tuple(pmul(list(g), list(h)))
                if x not in seen:
                    seen.add(x)
                    nxt.append(x)
        frontier = nxt
    return sorted(seen)


def sigma_perm(m):
    """The label exchange on m*m labels, index m*u + v."""
    return [m * (i % m) + (i // m) for i in range(m * m)]


def tensor(a, b):
    na, nb = len(a), len(b)
    return [a[i // nb] * nb + b[i % nb] for i in range(na * nb)]


def gen_defect(q, m):
    """GEN 8.1's defect on the system-pair labels: D = Sigma Q^T Sigma Q.
    [instrument -- mutable]"""
    s = sigma_perm(m)
    qi = pinv(q)
    d = [s[qi[s[q[x]]]] for x in range(m * m)]
    if _M_DEFECT:
        d = pmul(s, d)
    return d


def orbits_unionfind(gens, n):
    """Orbits of <gens> on n points, by union-find.  [instrument -- mutable]"""
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for g in gens:
        for i in range(n):
            a, b = find(i), find(g[i])
            if a != b:
                parent[a] = b
    if _M_ORBIT:
        parent[0] = 0
        return [[0]] + [[i] for i in range(1, n)]
    buckets: dict = {}
    for i in range(n):
        buckets.setdefault(find(i), []).append(i)
    return sorted(buckets.values())


# --- the abstract dihedral model, built independently of the permutations --

def dihedral_abstract(n):
    """D_n as pairs (i, e) in Z/n x Z/2 with (i,e)(j,f) = (i +/- j, e+f).
    Built from n alone -- it never sees a permutation.  The model itself is
    audited against the permutation rebuild by an explicit isomorphism (G03).
    [instrument -- mutable]"""
    els = [(i, e) for i in range(n) for e in range(2)]

    def mul(a, b):
        i, e = a
        j, f = b
        if _M_MODEL:
            return ((i + j) % n, (e + f) % 2)
        return ((i + j) % n if e == 0 else (i - j) % n, (e + f) % 2)

    return els, mul, (0, 0)


def abstract_from_perms(G):
    """A group given as a sorted list of permutation tuples, packaged in the
    same (elements, mul, identity) interface.  [instrument -- mutable]"""
    els = list(range(len(G)))
    index = {g: i for i, g in enumerate(G)}

    def mul(a, b):
        return index[tuple(pmul(list(G[a]), list(G[b])))]

    return els, mul, index[tuple(pident(len(G[0])))]


def group_element_orders(els, mul, e):
    out = []
    for g in els:
        c, cur = 1, g
        while cur != e:
            cur = mul(cur, g)
            c += 1
        out.append(c)
    return sorted(set(out))


# --------------------------------------------------------------------------
# 4.  THE STRUCTURE-PRESERVATION PREDICATE  (declared in DECL['predicate'])
# --------------------------------------------------------------------------

def sp1_is_hom(src_els, src_mul, tgt_mul, phi):
    """SP1: composition preserved at every ordered pair.  [instrument -- mutable]"""
    if _M_HOM:
        return True, 0, 0
    cells = bad = 0
    for a in src_els:
        for b in src_els:
            cells += 1
            if phi[src_mul(a, b)] != tgt_mul(phi[a], phi[b]):
                bad += 1
    return bad == 0, cells, bad


def sp3_equivariant(src_els, src_act, tgt_act, tgt_inv, phi, Phi, n_src):
    """SP3: Phi(g.x) = phi(g).Phi(x) at every cell.  The action's ORIENTATION is
    a declared convention, so it carries its own perturbation (RUNBOOK 14).
    [instrument -- mutable]"""
    pts = [0] if _M_PRED else list(range(n_src))
    cells = bad = 0
    for g in src_els:
        for x in pts:
            cells += 1
            lhs = Phi[src_act(g, x)]
            h = tgt_inv(phi[g]) if _M_SIDE else phi[g]
            rhs = tgt_act(h, Phi[x])
            if lhs != rhs:
                bad += 1
    return bad == 0, cells, bad


def nontrivial(phi, Phi, src_identity, tgt_identity):
    """NT1 and NT2.  [instrument -- mutable]"""
    if _M_NONTRIV:
        return True, True
    nt1 = any(v != tgt_identity for k, v in enumerate(phi) if k != src_identity)
    nt2 = (len(set(Phi)) > 1)
    return nt1, nt2


def evaluate_candidate(src, tgt, phi, Phi):
    """The whole predicate, evaluated on one candidate pair (phi, Phi)."""
    note_census()
    ok1, c1, b1 = sp1_is_hom(src["els"], src["mul"], tgt["mul"], phi)
    ok2 = (phi[src["e"]] == tgt["e"])
    ok3, c3, b3 = sp3_equivariant(src["els"], src["act"], tgt["act"], tgt["inv"],
                                  phi, Phi, src["npts"])
    nt1, nt2 = nontrivial(phi, Phi, src["e"], tgt["e"])
    return {"SP1": ok1, "SP2": ok2, "SP3": ok3, "NT1": nt1, "NT2": nt2,
            "sp1_cells": c1, "sp1_bad": b1, "sp3_cells": c3, "sp3_bad": b3,
            "SP": ok1 and ok2 and ok3, "accepted": ok1 and ok2 and ok3 and nt1 and nt2}


# --------------------------------------------------------------------------
# 5.  THE TWO CENSUS ROUTES  (independent computations, RUNBOOK 13 addendum)
# --------------------------------------------------------------------------

def homs_route_a(p, els, mul, e):
    """ROUTE A -- the element-power route: count g with g^p = e, by iterated
    multiplication in the target group.  Returns the list of images of the
    source generator."""
    out = []
    for g in els:
        cur = e
        for _ in range(p):
            cur = mul(cur, g)
        if cur == e:
            out.append(g)
    return out


def homs_route_b(p, els, mul, e):
    """ROUTE B -- the cyclic-subgroup-lattice route.  It builds, for every
    element, the SET that element spans, deduplicates those sets into the
    lattice of cyclic subgroups, keeps the ones whose ORDER DIVIDES p, and
    counts each one's own generators.  It never raises an element to the p-th
    power and never reads route A: it works with subgroups as sets where route
    A works with a single power.  [instrument -- mutable]"""
    spans: dict = {}
    for g in els:
        S = tuple(sorted(_cyclic_span(g, mul, e), key=repr))
        spans.setdefault(S, []).append(g)
    if _M_ROUTEB:
        spans = {S: gs for S, gs in spans.items() if len(S) > 1}
    total = 0
    for S in sorted(spans, key=repr):
        if p % len(S) == 0:
            total += len(spans[S])
    return total


def _cyclic_span(g, mul, e):
    out, cur = [e], g
    while cur != e:
        out.append(cur)
        cur = mul(cur, g)
    return out


def homs_count_two_routes(p, els, mul, e, taint):
    """Both routes, with an explicit taint counter proving route B never reads
    route A's result.  [instrument -- mutable]"""
    a = homs_route_a(p, els, mul, e)
    if _M_ALIAS:
        taint[0] += 1
        return len(a), len(a), a
    b = homs_route_b(p, els, mul, e)
    return len(a), b, a


def homs_into_Zp_generators(p, els, mul, e, gens):
    """The reverse direction: homomorphisms G -> Z/p.  ROUTE A enumerates the
    p^len(gens) assignments of generator images and verifies each on the whole
    multiplication table; it is exhaustive because gens generate G."""
    idx = {g: i for i, g in enumerate(els)}
    found = 0
    for images in itertools.product(range(p), repeat=len(gens)):
        # extend by breadth-first word evaluation
        val = {e: 0}
        frontier = [e]
        ok = True
        while frontier and ok:
            nxt = []
            for x in frontier:
                for gi, g in enumerate(gens):
                    y = mul(x, g)
                    v = (val[x] + images[gi]) % p
                    if y in val:
                        if val[y] != v:
                            ok = False
                            break
                    else:
                        val[y] = v
                        nxt.append(y)
                if not ok:
                    break
            frontier = nxt
        if ok and len(val) == len(els):
            bad = 0
            for a in els:
                for b in els:
                    if val[mul(a, b)] != (val[a] + val[b]) % p:
                        bad += 1
            if bad == 0:
                found += 1
    return found, idx


def homs_into_Zp_lattice(p, els, mul, e):
    """ROUTE B for the reverse direction.  It works in the ABELIANISATION, not
    in G: it builds the commutator subgroup by closing the set of commutators,
    forms the quotient's own multiplication table on cosets, and counts the
    homomorphisms of that quotient into Z/p by sweeping the images of the
    quotient's generators.  Route A never forms a quotient and route B never
    touches an element of G outside a coset representative.
    [instrument -- mutable]"""
    comm = commutator_subgroup(els, mul, e)
    cosets = quotient_elements(els, mul, comm)
    reps = sorted(cosets.keys(), key=repr)
    rep_of = {}
    for r in reps:
        for x in cosets[r]:
            rep_of[x] = r
    qmul = {(a, b): rep_of[mul(cosets[a][0], cosets[b][0])]
            for a in reps for b in reps}
    qe = rep_of[e]
    # a minimal generating set of the quotient, grown greedily inside it
    qgens: list = []
    span = {qe}
    for r in reps:
        if r in span:
            continue
        qgens.append(r)
        frontier = sorted(span, key=repr)
        while True:
            new = {qmul[(a, b)] for a in span | {r} for b in span | {r}}
            new |= {r}
            if new <= span:
                break
            span = span | new
        if len(span) == len(reps):
            break
    total = 0
    for images in itertools.product(range(p), repeat=max(len(qgens), 1)):
        assign = {qe: 0}
        for i, r in enumerate(qgens):
            assign[r] = images[i]
        changed = True
        while changed:
            changed = False
            for a in sorted(assign, key=repr):
                for b in sorted(assign, key=repr):
                    c = qmul[(a, b)]
                    v = (assign[a] + assign[b]) % p
                    if c not in assign:
                        assign[c] = v
                        changed = True
        if len(assign) != len(reps):
            continue
        bad = 0
        for a in reps:
            for b in reps:
                if assign[qmul[(a, b)]] != (assign[a] + assign[b]) % p:
                    bad += 1
        if bad == 0:
            total += 1
    return total, len(comm), len(reps)


def commutator_subgroup(els, mul, e):
    """[G,G], built by closing the set of commutators.  [instrument -- mutable]"""
    if _M_ABEL:
        return [e]
    inv = {}
    for g in els:
        for h in els:
            if mul(g, h) == e:
                inv[g] = h
    gens = set()
    for a in els:
        for b in els:
            gens.add(mul(mul(inv[a], inv[b]), mul(a, b)))
    S = {e}
    frontier = [e]
    gens = sorted(gens, key=repr)
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = mul(x, g)
                if y not in S:
                    S.add(y)
                    nxt.append(y)
        frontier = nxt
    return sorted(S, key=repr)


def quotient_elements(els, mul, comm):
    """The cosets of a normal subgroup, keyed by a canonical representative."""
    seen = {}
    out: dict = {}
    for g in els:
        if g in seen:
            continue
        coset = sorted({mul(g, c) for c in comm}, key=repr)
        rep = coset[0]
        out[rep] = coset
        for x in coset:
            seen[x] = rep
    return out


# --------------------------------------------------------------------------
# 6.  INSTRUMENT HELPERS CARRYING THE REMAINING MUTATIONS
# --------------------------------------------------------------------------

def declared_primes():
    """[instrument -- mutable]"""
    ps = DECL["deformation_side"]["primes"]
    return ps[:1] if _M_ONEPRIME else ps


def rho_mod_p(rho, p):
    """Exact Q -> F_p reduction of the residual.  [instrument -- mutable]"""
    out = []
    for v in rho:
        if v.denominator % p == 0:
            return None
        r = (v.numerator % p) * pow(v.denominator % p, -1, p) % p
        out.append((r + 1) % p if _M_RHO else r)
    return tuple(out)


def committed_instances(rows):
    """[instrument -- mutable]"""
    if _M_CELL:
        return rows[:-1]
    if _M_SCOPE:
        return rows + [("LEAKED ord=7 class", 81, 7, 14, False)]
    return rows


def instance_orders(rows):
    """The committed instances' measured group orders.  [instrument -- mutable]"""
    if _M_ORDERS:
        return [(a, b, c, d + 1, e) for (a, b, c, d, e) in rows]
    return rows


def pinned_hash(path, key):
    """The measured sha256 of a pinned source.  [instrument -- mutable]"""
    h = sha256_file(path)
    perturb = ((key.endswith("ha_successor_receipt.json") and _M_HASHA)
               or (key.endswith("nt_transport_receipt.json") and _M_HASNT)
               or (key.endswith("gen_generality_receipt.json") and _M_HASGEN)
               or (key.endswith("xba_crossbase_receipt.json") and _M_HASXBA)
               or (key.endswith("psi_curvature_receipt.json") and _M_HASPSI)
               or (key.endswith("paper-xba-crossbase.md") and _M_HASXBAP)
               or (key.endswith("note-brg-bridge-pin.md") and (_M_HASPIN or _M_SOFT)))
    return (h[:-1] + "0") if perturb else h


def family_members():
    """The declared completion family: every permutation of the nine
    system-pair labels fixing the initial one.  [instrument -- mutable]"""
    out = [[0] + list(t) for t in itertools.permutations(range(1, 9))]
    if _M_FAMILY:
        return out[:1000]
    if _M_FAMDROP:
        return out[:-1]
    return out


def dictionary_records():
    """[instrument -- mutable]"""
    rs = sorted(k for k, v in DECL["deformation_side"]["records"].items())
    return rs[:-1] if _M_DICT else rs


def comparator_group_order(perm_group_order, abstract_order):
    """The comparator for the abstract/permutation agreement gate: it must be
    the permutation rebuild, never the abstract model it audits (RUNBOOK 14
    addendum, v13 #219).  [instrument -- mutable]"""
    return abstract_order if _M_COMPSELF else perm_group_order


def ambiguity_set(cands):
    """The whole set of candidates consistent with every committed datum.
    [instrument -- mutable]"""
    return cands[:1] if _M_AMBIG else cands


def breaking_group_map(els, p):
    """The declared structure-breaking map's group part: the IDENTITY, against a
    carrier map that doubles the register.  [instrument -- mutable]"""
    return [(2 * g) % p for g in els] if _M_BREAK else list(els)


def class_keys(cls):
    """The committed completion classes swept at the extended scope.
    [instrument -- mutable]"""
    ks = sorted(cls)
    return ks[:-1] if _M_CLASS else ks


def any_instance_admits_every_prime(admits_by_instance):
    """The arena-invariant reading is the INTERSECTION over the declared primes.
    [instrument -- mutable]"""
    if _M_INVAR:
        return True
    return any(all(v) for v in admits_by_instance)


def committed_scope_defect_order():
    """The defect order of the committed completions, against which the
    committed-scope dictionary census is taken.  [instrument -- mutable]"""
    return 5 if _M_DICTSCOPE else 2


def heldout_image_generator(D_el, W_el):
    """The declared target-side generator against which the held-out orbit
    quantities are read.  [instrument -- mutable]"""
    return W_el if _M_QUANT else D_el


def relabelling_of(n, shift):
    """A declared relabelling of a carrier.  [instrument -- mutable]"""
    if _M_RELABEL:
        return pident(n)
    return [(i + shift) % n for i in range(n)]


def conjugator_of(n, shift):
    """A declared carrier permutation to conjugate the target action by.
    [instrument -- mutable]"""
    if _M_CONJ:
        return pident(n)
    return [(i * 1 + shift) % n for i in range(n)]


def spectrum_for_comparison(defect_orders, holonomy_orders):
    """RUNBOOK 15 addendum (#196): the like-for-like comparator is the DEFECT
    spectrum, because the coordinate table pairs R_HH with the DEFECT.
    [instrument -- mutable]"""
    return sorted(holonomy_orders) if _M_SPECSWAP else sorted(defect_orders)


def tracking_candidate_verdict(p, defect_spectrum):
    """F3, the morphism-by-spectrum candidate.  [instrument -- mutable]"""
    if _M_TRACK:
        return True
    return p in defect_spectrum


def fit_orbit_indices(n_orbits):
    """The declared FIT set: orbit 0 only.  [instrument -- mutable]"""
    return list(range(n_orbits)) if _M_LEAK else [0]


def extension_assignment(kind, delta, c, W_idx, D_idx, n_rot):
    """The declared extension rule's target-group element for the source
    symmetry (front translation delta, transverse register shift c).
    E-ROT is rotation-valued; E-REF is reflection-valued where delta0 is odd.
    [instrument -- mutable]"""
    rot = (delta[0] + 2 * delta[1] + c) % n_rot
    if kind == "E-ROT" or _M_TEETH:
        return (rot, 0)
    return (rot, delta[0] % 2)


def synthetic_found_target_order(n):
    """[instrument -- mutable]"""
    return 2 if _M_FOUND else n


def synthetic_empty_source_prime(p):
    """[instrument -- mutable]"""
    return 3 if _M_EMPTY else p


def obstruction_name(coprime_iff_empty):
    """The named obstruction.  [instrument -- mutable]"""
    if _M_OBST:
        return "carrier cardinality"
    return "order-coprimality"


def equivariant_map_count(n_target, n_orbits):
    """The number of phi-equivariant carrier maps, given phi: one free choice of
    image per source orbit (the source action is free, so every stabiliser is
    trivial and every choice extends uniquely).  [instrument -- mutable]"""
    if _M_FORMULA:
        return n_target ** max(n_orbits - 1, 0)
    return n_target ** n_orbits


def selftest_tested_set(declared, verdicts):
    """RUNBOOK 14 addendum (#185): the tested set is fixed by declaration and
    never selected by the verdicts under audit.  [instrument -- mutable]"""
    if _M_SELSEL:
        return [k for k in declared if verdicts.get(k)]
    return list(declared)


def derive_verdict(empty_everywhere, invariant, reach_found, reach_empty,
                   complete):
    """The verdict, derived from the measured counts.  [instrument -- mutable]"""
    if _M_VERDICT:
        return "BRG-MORPHISM-FOUND"
    if not (complete and invariant and reach_found and reach_empty):
        return "BRG-BLOCKED-AT-CENSUS-DISCIPLINE"
    return "BRG-EMPTY-AT-CARRIER" if empty_everywhere else "BRG-MORPHISM-FOUND"


def census_is_empty(nontrivial_forward, nontrivial_reverse):
    """The emptiness decision, taken at its own source so that a corruption of
    it can be caught by the verdict gate's independent recount.
    [instrument -- mutable]"""
    if _M_COUNTFLIP:
        return not (nontrivial_forward == 0 and nontrivial_reverse == 0)
    return nontrivial_forward == 0 and nontrivial_reverse == 0


def qualifier_value(name, computed):
    """A printed verdict qualifier.  Every one is recomputed inside G31 from its
    own source, so a typed value cannot reach the receipt.
    [instrument -- mutable]"""
    if _M_QUALTYPO and name == "instances":
        return 999
    return computed


def prime_radical(n):
    """The set of primes dividing n, computed by trial division."""
    out, d, m = [], 2, n
    while d * d <= m:
        if m % d == 0:
            out.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        out.append(m)
    return out


def radical_instance_orders(rows):
    """The defect orders over which the radical of 2*ord(D) is computed.
    [instrument -- mutable]"""
    ns = [n for (_nm, _c, n, _o, _r) in rows]
    return ns + [5] if _M_RADINJ else ns


def declared_group_zoo(builders):
    """The declared group list for the Lagrange+Cauchy sweep: dihedral AND
    non-dihedral, abelian AND non-abelian.  [instrument -- mutable]"""
    if _M_ZOO:
        return {k: v for k, v in builders.items() if k.startswith("D_")}
    return builders


def reverse_nontrivial(reverse_homs, forward_nontrivial):
    """The reverse census's non-trivial count: the number of homomorphisms
    G -> Z/p other than the trivial one.  [instrument -- mutable]"""
    return forward_nontrivial if _M_REVALIAS else reverse_homs - 1


def random_stream(seed_bytes, count):
    """A deterministic integer stream seeded by the sha256 of DECLARED DATA
    alone -- no wall-clock value and no operating-system entropy."""
    state = int.from_bytes(hashlib.sha256(seed_bytes).digest(), "big")
    out = []
    for _ in range(count):
        state = (state * 6364136223846793005 + 1442695040888963407) % (2 ** 64)
        out.append(state >> 11)
    return out


def stream_perm(n, stream, cur):
    """A permutation of n points drawn from the deterministic stream."""
    a = list(range(n))
    for i in range(n - 1, 0, -1):
        j = stream[cur[0]] % (i + 1)
        cur[0] += 1
        a[i], a[j] = a[j], a[i]
    return a


def one_law_exchange(n, stream, cur):
    """The exchange leg of the one law: an INVOLUTION, per PSI's measurement
    that P_W is one.  [instrument -- mutable]"""
    base = stream_perm(n, stream, cur)
    if _M_PSINONINV:
        return base
    a = list(range(n))
    npairs = 1 + (stream[cur[0]] % (n // 2))
    cur[0] += 1
    for i in range(npairs):
        x, y = base[2 * i], base[2 * i + 1]
        a[x], a[y] = a[y], a[x]
    return a


def live_cell_generator_exponent(ord_D, p):
    """The exponent that turns the defect into an element of order exactly p:
    D^(ord(D)/p).  [instrument -- mutable]"""
    return 1 if _M_LIVEORD else ord_D // p


def collapse_orbit_image(orbit_index, j):
    """The declared orbit-collapsing carrier map: every source orbit but the
    first is sent into ONE target orbit, and inside each orbit the map is
    equivariant -- the measured example of how little NT2 asks.  Returns the
    target-orbit selector and the exponent inside it.  [instrument -- mutable]"""
    if _M_COLLAPSE:
        return 0, 0
    return (0 if orbit_index else 1), j


def low_sector_bound():
    """The declared low-defect-order band: the band the committed instances
    occupy.  [instrument -- mutable]"""
    return 2 if _M_SECTOR else 3


def contingency_arena_m():
    """The arena in which the two-prime clause's contingency is measured:
    species 4's own sixteen-label arena.  [instrument -- mutable]"""
    return 3 if _M_LANDAU else 4


def tiny_cell_specs(specs):
    """The declared tiny validation cells.  [instrument -- mutable]"""
    return specs[:1] + specs[2:] if _M_TINYDROP else specs


def tiny_generator(name, npts, p):
    """The tiny cells' source generators.  The arena constructor refuses a
    generator whose order does not divide p (G42), so a cell whose declared
    group does not act is caught rather than counted.  [instrument -- mutable]"""
    if name == "TINY-A" and not _M_ARENAORD:
        a = list(range(npts))
        for i in range(0, npts - 1, 2):
            a[i], a[i + 1] = a[i + 1], a[i]
        return a
    return [(i + 1) % npts for i in range(npts)]


def selftest_carrier_image(relabelling, Phi, relabel_values):
    """A declared self-test transports the candidate by the SAME action it
    applies to the arena: Phi -> r . Phi . r^-1 when both carriers move, and
    Phi . r^-1 when only the source does.  [instrument -- mutable]"""
    inv = pinv(relabelling)
    src_index = relabelling if _M_SELFBLIND else inv
    out = [Phi[src_index[i]] for i in range(len(Phi))]
    return [relabelling[v] for v in out] if relabel_values else out


def swept_generator(gen_perm, j):
    """The source generator R^j swept by the generator-change self-test.
    [instrument -- mutable]"""
    if _M_GENBLIND:
        return pident(len(gen_perm))
    return perm_pow(gen_perm, j, fresh=True)


def functor_census_cells(cells):
    """The cells of the functor-level census.  [instrument -- mutable]"""
    return cells[:-1] if _M_FCELL else cells


# --------------------------------------------------------------------------
# 7.  THE AST GUARDS
# --------------------------------------------------------------------------

def ast_float_scan(src: str) -> list[str]:
    """Every float/complex literal and every float()/complex() call.
    [instrument -- mutable]"""
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
SYNTH_MUTANT_SAMPLE = (
    "def f():\n"
    "    if _M_SOMETHING:\n"
    "        pass\n"
    "    gate('GX', 'c', True)\n")


# ==========================================================================
#                              THE UNIT
# ==========================================================================

def run_unit(src: str) -> dict:
    """The whole measurement.  Registers every gate; reads no run-mode boolean,
    directly or indirectly."""
    progress("start")
    say("=" * 78)
    say("BRG -- THE MORPHISM-CENSUS BRIDGE   (v13 gravity <-> transport)")
    say("pin v13/note-brg-bridge-pin.md (STRICT) -- immutable base b632f59")
    say("=" * 78)
    say("")
    tables: dict = {}
    k_rank, d_dim = 2, 2

    def make_perm_arena(G, npts):
        els = list(range(len(G)))
        index = {g: i for i, g in enumerate(G)}

        def mul(a, b):
            return index[tuple(pmul(list(G[a]), list(G[b])))]

        def act(g, x):
            return G[g][x]

        def inv(g):
            return index[tuple(pinv(list(G[g])))]
        return {"els": els, "mul": mul, "act": act, "inv": inv, "npts": npts,
                "e": index[tuple(pident(npts))], "G": G}

    def make_cyclic_arena(p, npts, gen_perm, fresh=False):
        els = list(range(p))
        pw = [perm_pow(gen_perm, j, fresh=fresh) for j in range(p)]

        def mul(a, b):
            return (a + b) % p

        def act(g, x):
            return pw[g][x]

        def inv(g):
            return (-g) % p
        return {"els": els, "mul": mul, "act": act, "inv": inv, "npts": npts,
                "e": 0, "pw": pw}

    def ha_arena(p, r):
        n = p ** (k_rank + d_dim)
        gen = []
        for i in range(n):
            m1 = i % p
            m0 = (i // p) % p
            rest = i // (p * p)
            gen.append(rest * p * p + ((m0 + r[0]) % p) * p + ((m1 + r[1]) % p))
        return make_cyclic_arena(p, n, gen), gen

    # ==================== 1. THE FREEZE =====================================
    say("--- 1. THE DECLARATIONS, FROZEN BEFORE ANY MORPHISM IS EVALUATED ---")
    frozen_evals = CENSUS_EVALS[0]
    g01 = gate("G01", "THE DECLARATIONS ARE FROZEN BEFORE ANY CANDIDATE MORPHISM "
               "IS EVALUATED: the carrier functors, the structure-preservation "
               "predicate, the held-out set and the arena are declared as data, "
               "and the candidate-evaluation counter is measured ZERO at the "
               "freeze point",
               frozen_evals == 0, {"candidate_evaluations_at_freeze": frozen_evals})
    report("G01", g01, f"candidate evaluations at the freeze: {frozen_evals}")
    say(f"        declared functors : {len(DECL['functors'])}")
    say(f"        declared predicate clauses : {len(DECL['predicate']) - 1} "
        f"(SP1, SP2, SP3, NT1, NT2) + the arena-invariance clause")
    say(f"        declared held-out quantities : "
        f"{len([k for k in DECL['held_out'] if k.startswith('H')])}")
    say(f"        declared primes : {DECL['deformation_side']['primes']}")
    say("")

    # ==================== 2. THE PINNED SOURCES =============================
    say("--- 2. THE PINNED TERMINAL RECEIPTS (anchors are exit-1) ---")
    progress("anchors")
    paths = {k: os.path.join(REPO, k) for k in DECL["pins"]}
    got = {}
    for k in sorted(DECL["pins"]):
        h = pinned_hash(paths[k], k)
        got[k] = h
        anchor(f"A{len(ANCHORS) + 1:02d}", f"sha256 of {k}", DECL["pins"][k], h,
               "v13/note-brg-bridge-pin.md + the terminal deliveries")
        say(f"        {k:46s} {h[:16]}... OK")
    HA = json.load(open(paths["v13/code/ha_successor_receipt.json"]))
    NT = json.load(open(paths["v13/code/nt_transport_receipt.json"]))
    GEN = json.load(open(paths["v13/code/gen_generality_receipt.json"]))
    XBA = json.load(open(paths["v13/code/xba_crossbase_receipt.json"]))
    PSI = json.load(open(paths["v13/code/psi_curvature_receipt.json"]))
    say("")

    # ==================== 3. THE TRANSPORT SIDE, REBUILT ====================
    say("--- 3. THE TRANSPORT SIDE, REBUILT FROM GEN 8.1's DEFECT LAW ---")
    progress("transport side")
    S9 = sigma_perm(3)
    Q_decl = pident(9)
    Q_decl[1], Q_decl[2] = Q_decl[2], Q_decl[1]
    D9 = gen_defect(Q_decl, 3)
    W81 = tensor(S9, S9)
    D81 = tensor(D9, pident(9))
    G81 = closure([tuple(W81), tuple(D81)], 81)
    anchor(f"A{len(ANCHORS) + 1:02d}", "GEN: the declared completion's defect permutation",
           GEN["tables"]["completion_census"]["the_declared_completions_entry"]
              ["the_defect_permutation"], D9,
           "v13/code/gen_generality_receipt.json completion_census")
    anchor(f"A{len(ANCHORS) + 1:02d}", "GEN: the declared defect's order",
           GEN["tables"]["completion_census"]["the_declared_completions_entry"]["order"],
           porder(D9), "v13/code/gen_generality_receipt.json completion_census")
    anchor(f"A{len(ANCHORS) + 1:02d}",
           "GEN: the declared defect's fixed configurations of 81",
           GEN["tables"]["completion_census"]["the_declared_completions_entry"]
              ["fixed_configurations"], pfixed(D81),
           "v13/code/gen_generality_receipt.json completion_census")
    anchor(f"A{len(ANCHORS) + 1:02d}", "XBA: base G's wing-exchange fixed configurations",
           XBA["tables"]["bases"]["base G @ GP-E"]["W_fixed"], pfixed(W81),
           "v13/code/xba_crossbase_receipt.json bases")
    anchor(f"A{len(ANCHORS) + 1:02d}", "XBA: base G's |<W,D>|",
           XBA["tables"]["the_commutator_law"]["base G @ GP-E"]
              ["the_order_of_the_group_generated_by_W_and_D"], len(G81),
           "v13/code/xba_crossbase_receipt.json the_commutator_law")
    # PSI's one law, cross-anchored: the defect this unit rebuilds from GEN's
    # law IS the group commutator PSI records, and PSI's group-order reading is
    # the order formula this unit's obstruction turns on.
    psi_go = PSI["tables"]["one_law"]["the_group_order_reading"]
    anchor(f"A{len(ANCHORS) + 1:02d}",
           "PSI: the commutator delta(Q) at the pinned completion is the defect "
           "this unit rebuilds",
           psi_go["the pinned Q"]["the_commutator_delta_Q"], D9,
           "v13/code/psi_curvature_receipt.json one_law.the_group_order_reading")
    anchor(f"A{len(ANCHORS) + 1:02d}",
           "PSI: the order of the commutator at the pinned completion",
           psi_go["the pinned Q"]["its_order"], porder(D9),
           "v13/code/psi_curvature_receipt.json one_law.the_group_order_reading")
    anchor(f"A{len(ANCHORS) + 1:02d}",
           "PSI: the measured based-holonomy group order at GP-E is 2*ord(delta(Q))",
           psi_go["the pinned Q"]["the_measured_based_holonomy_group_order_at_GP_E"],
           len(G81),
           "v13/code/psi_curvature_receipt.json one_law.the_group_order_reading")
    anchor(f"A{len(ANCHORS) + 1:02d}",
           "PSI: the group order the dihedral reading predicts at the pinned "
           "completion",
           psi_go["the pinned Q"]["the_group_order_the_dihedral_reading_predicts"],
           2 * porder(D9),
           "v13/code/psi_curvature_receipt.json one_law.the_group_order_reading")
    say(f"        base G: Sigma on 9 labels, D = {D9}, ord {porder(D9)}, "
        f"{pfixed(D81)} fixed of 81")
    say(f"        W fixed {pfixed(W81)} of 81; |<W,D>| = {len(G81)}")
    say(f"        PSI's one law: D = [P_W, u] with P_W an involution, so "
        f"W D W = D^-1 is forced and |<W,D>| = 2*ord(D);")
    say(f"        PSI records delta(Q) = {psi_go['the pinned Q']['the_commutator_delta_Q']} "
        f"and the measured holonomy order "
        f"{psi_go['the pinned Q']['the_measured_based_holonomy_group_order_at_GP_E']} "
        f"-- both reproduced here.")

    # base 1: the wing exchange rebuilt on 36; the three factor fixed-point
    # counts anchored against NT's own receipt.
    S4, S9b = sigma_perm(2), sigma_perm(3)
    W36 = tensor(S4, S9b)
    fp = NT["tables"]["structure_group"]["factor_fixed_points"]
    anchor(f"A{len(ANCHORS) + 1:02d}", "NT: the wing exchange's fixed configurations of 36",
           fp["the wing exchange"], pfixed(W36),
           "v13/code/nt_transport_receipt.json structure_group")
    anchor(f"A{len(ANCHORS) + 1:02d}", "NT: the qubit-only wing swap's fixed configurations",
           fp["the qubit-only wing swap"], pfixed(tensor(S4, pident(9))),
           "v13/code/nt_transport_receipt.json structure_group")
    anchor(f"A{len(ANCHORS) + 1:02d}",
           "NT: the pointer-only wing swap's fixed configurations",
           fp["the pointer-only wing swap"], pfixed(tensor(pident(4), S9b)),
           "v13/code/nt_transport_receipt.json structure_group")
    say(f"        base 1: W = Sigma_4 (x) Sigma_9 on 36, fixed {pfixed(W36)}; "
        f"factor fixed points {pfixed(tensor(S4, pident(9)))}/"
        f"{pfixed(tensor(pident(4), S9b))} anchored against NT")

    # species 4
    S16 = sigma_perm(4)
    Q4 = pident(16)
    Q4[1], Q4[2] = Q4[2], Q4[1]
    D16 = gen_defect(Q4, 4)
    W256, D256 = tensor(S16, S16), tensor(D16, pident(16))
    G256 = closure([tuple(W256), tuple(D256)], 256)
    anchor(f"A{len(ANCHORS) + 1:02d}", "XBA: species 4's defect fixed configurations of 256",
           192, pfixed(D256), "v13/paper-xba-crossbase.md 9.4 (committed table)")
    anchor(f"A{len(ANCHORS) + 1:02d}",
           "XBA: species 4's wing-exchange fixed configurations of 256",
           16, pfixed(W256), "v13/paper-xba-crossbase.md 9.4 (committed table)")
    anchor(f"A{len(ANCHORS) + 1:02d}", "XBA: species 4's |<W,D>|",
           XBA["tables"]["the_commutator_law"]["species 4"]
              ["the_order_of_the_group_generated_by_W_and_D"], len(G256),
           "v13/code/xba_crossbase_receipt.json the_commutator_law")
    # species 4's own completion family: 120 single transpositions
    sp4_split: dict = {}
    for a, b in itertools.combinations(range(16), 2):
        qq = pident(16)
        qq[a], qq[b] = qq[b], qq[a]
        o = porder(gen_defect(qq, 4))
        sp4_split[o] = sp4_split.get(o, 0) + 1
    anchor(f"A{len(ANCHORS) + 1:02d}",
           "XBA: species 4's own completion family, split by defect order",
           {"1": 12, "2": 60, "3": 48},
           {str(k): v for k, v in sorted(sp4_split.items())},
           "v13/paper-xba-crossbase.md 9.4 (120 transpositions, 12/60/48)")
    say(f"        species 4: 256 configurations, D fixed {pfixed(D256)}, "
        f"W fixed {pfixed(W256)}, |<W,D>| = {len(G256)}; its own 120-member "
        f"transposition family splits "
        f"{ {k: v for k, v in sorted(sp4_split.items())} }")

    # base T and base S'
    QT = pident(9)
    QT[1], QT[4] = QT[4], QT[1]
    DT9 = gen_defect(QT, 3)
    DT81 = tensor(DT9, pident(9))
    GT = closure([tuple(W81), tuple(DT81)], 81)
    anchor(f"A{len(ANCHORS) + 1:02d}", "XBA: base T's defect order",
           XBA["tables"]["the_commutator_law"]["base T"]["the_order_of_the_defect"],
           porder(DT9), "v13/code/xba_crossbase_receipt.json the_commutator_law")
    anchor(f"A{len(ANCHORS) + 1:02d}", "XBA: base T's |<W,D>|",
           XBA["tables"]["the_commutator_law"]["base T"]
              ["the_order_of_the_group_generated_by_W_and_D"], len(GT),
           "v13/code/xba_crossbase_receipt.json the_commutator_law")
    anchor(f"A{len(ANCHORS) + 1:02d}",
           "PSI: base T's completion is PSI's Q-negA, and its commutator "
           "delta(Q) is the defect rebuilt here",
           psi_go["Q-negA"]["the_commutator_delta_Q"], DT9,
           "v13/code/psi_curvature_receipt.json one_law.the_group_order_reading")
    anchor(f"A{len(ANCHORS) + 1:02d}",
           "PSI: the measured based-holonomy group order at Q-negA",
           psi_go["Q-negA"]["the_measured_based_holonomy_group_order_at_GP_E"],
           len(GT),
           "v13/code/psi_curvature_receipt.json one_law.the_group_order_reading")
    QS = pident(9)
    DS9 = gen_defect(QS, 3)
    GS = closure([tuple(W81), tuple(tensor(DS9, pident(9)))], 81)
    anchor(f"A{len(ANCHORS) + 1:02d}", "XBA: base S' (the equivariant control) |<W,D>|",
           XBA["tables"]["the_commutator_law"]["base S'"]
              ["the_order_of_the_group_generated_by_W_and_D"], len(GS),
           "v13/code/xba_crossbase_receipt.json the_commutator_law")
    say(f"        base T: D of order {porder(DT9)}, |<W,D>| = {len(GT)};   "
        f"base S' (equivariant control): |<W,D>| = {len(GS)}")
    say("")

    # ==================== 4. THE COMPLETION FAMILY ==========================
    say("--- 4. THE DECLARED COMPLETION FAMILY, SWEPT WHOLE (scope 3) ---")
    progress("family sweep")
    fam = family_members()
    ord_spec: dict = {}
    fix_spec: dict = {}
    fam_class: dict = {}
    min_support: dict = {}
    dih_fail = 0
    fam_cells = 0
    for q in fam:
        fam_cells += 1
        dd = gen_defect(q, 3)
        o = porder(dd)
        fx = pfixed(dd) * 9
        fam_class[tuple(q)] = (o, fx)
        mv = perm_moved(q)
        if o not in min_support or mv < min_support[o]:
            min_support[o] = mv
        ord_spec[o] = ord_spec.get(o, 0) + 1
        fix_spec[fx] = fix_spec.get(fx, 0) + 1
        if pmul(S9, pmul(dd, S9)) != pinv(dd):
            dih_fail += 1
    g02 = gate("G02", "CELL-COMPLETENESS OF THE COMPLETION-FAMILY SWEEP: every "
               "member of the declared family is classified exactly once and the "
               "swept count equals the declared family size, computed by "
               "enumeration and not typed",
               fam_cells == 40320 and sum(ord_spec.values()) == fam_cells
               and sum(fix_spec.values()) == fam_cells
               and len(fam_class) == fam_cells,
               {"members_swept": fam_cells, "order_spectrum_total":
                sum(ord_spec.values()), "fixed_spectrum_total": sum(fix_spec.values()),
                "distinct_members": len(fam_class)})
    report("G02", g02, f"{fam_cells} members swept, spectra total "
           f"{sum(ord_spec.values())}/{sum(fix_spec.values())}, "
           f"{len(fam_class)} distinct")
    cc = GEN["tables"]["completion_census"]
    anchor(f"A{len(ANCHORS) + 1:02d}", "GEN: the declared completion family's size",
           cc["family_size"], fam_cells,
           "v13/code/gen_generality_receipt.json completion_census")
    anchor(f"A{len(ANCHORS) + 1:02d}", "GEN: the defect order spectrum over the family",
           {str(k): v for k, v in sorted(int(a) for a in [] ) } if False else
           {str(k): v for k, v in sorted(cc["members_by_the_order_of_the_defect"].items(),
                                         key=lambda kv: int(kv[0]))},
           {str(k): v for k, v in sorted(ord_spec.items())},
           "v13/code/gen_generality_receipt.json completion_census")
    anchor(f"A{len(ANCHORS) + 1:02d}",
           "GEN: the defect fixed-configuration spectrum over the family",
           {str(k): v for k, v in
            sorted(cc["members_by_the_fixed_configurations_of_the_defect"].items(),
                   key=lambda kv: int(kv[0]))},
           {str(k): v for k, v in sorted(fix_spec.items())},
           "v13/code/gen_generality_receipt.json completion_census")
    anchor(f"A{len(ANCHORS) + 1:02d}", "GEN: members whose defect is the identity",
           cc["members_whose_defect_is_the_identity"], ord_spec.get(1, 0),
           "v13/code/gen_generality_receipt.json completion_census")
    anchor(f"A{len(ANCHORS) + 1:02d}", "GEN: geometry-bearing members",
           cc["geometry_bearing_members"], fam_cells - ord_spec.get(1, 0),
           "v13/code/gen_generality_receipt.json completion_census")
    anchor(f"A{len(ANCHORS) + 1:02d}",
           "GEN: members where the dihedral relation Sigma D Sigma = D^-1 fails",
           cc["members_where_the_dihedral_relation_fails"], dih_fail,
           "v13/code/gen_generality_receipt.json completion_census")
    defect_orders = sorted(ord_spec)
    holonomy_orders = sorted({1} | {2 * n for n in defect_orders if n > 1})
    say(f"        defect order spectrum   {defect_orders}")
    say(f"        holonomy order spectrum {holonomy_orders}")
    say("")

    # ==================== 5. THE DEFORMATION SIDE, REBUILT ==================
    say("--- 5. THE DEFORMATION SIDE, REBUILT FROM HA's G28/G29 ---")
    progress("deformation side")
    rho = (Fr(1, 6), Fr(1, 6))
    ha_bridge = HA["tables"]["bridge"]
    anchor(f"A{len(ANCHORS) + 1:02d}", "HA: the exact rational residual at the detector site",
           ha_bridge["exact_residual_at_the_detector_site"], [str(t) for t in rho],
           "v13/code/ha_successor_receipt.json bridge")
    ha_rows = []
    for row in ha_bridge["prime_sweep"]:
        p = row["p"]
        r = rho_mod_p(rho, p)
        ha_rows.append({"p": p, "carrier": p ** (k_rank + d_dim),
                        "group_order": p, "rho_mod_p": list(r),
                        "element_orders": [1, p], "abelian": True})
    anchor(f"A{len(ANCHORS) + 1:02d}", "HA: the reduced carrier size at every swept prime",
           [row["carrier"] for row in ha_bridge["prime_sweep"]],
           [row["carrier"] for row in ha_rows],
           "v13/code/ha_successor_receipt.json bridge.prime_sweep")
    anchor(f"A{len(ANCHORS) + 1:02d}", "HA: rho mod p at every swept prime",
           [row["rho_mod_p"] for row in ha_bridge["prime_sweep"]],
           [row["rho_mod_p"] for row in ha_rows],
           "v13/code/ha_successor_receipt.json bridge.prime_sweep")
    anchor(f"A{len(ANCHORS) + 1:02d}", "HA: |<R_HH>| at every swept prime",
           [row["group_order"] for row in ha_bridge["prime_sweep"]],
           [row["group_order"] for row in ha_rows],
           "v13/code/ha_successor_receipt.json bridge.prime_sweep")
    anchor(f"A{len(ANCHORS) + 1:02d}", "HA: the element orders of <R_HH> at every swept prime",
           [row["element_orders"] for row in ha_bridge["prime_sweep"]],
           [row["element_orders"] for row in ha_rows],
           "v13/code/ha_successor_receipt.json bridge.prime_sweep")
    # the two primes at which rho does not reduce -- measured, not chosen
    nonreducible = [p for p in (2, 3, 5, 7, 11, 13, 17, 19, 23)
                    if rho_mod_p(rho, p) is None]
    say(f"        rho = (1/6, 1/6) exactly; carriers p^(k+d) with k = {k_rank}, "
        f"d = {d_dim}")
    for row in ha_rows:
        say(f"        p = {row['p']:<3d} carrier {row['carrier']:<8d} "
            f"|<R_HH>| = {row['group_order']:<3d} rho mod p = {row['rho_mod_p']}")
    say(f"        primes at which rho does NOT reduce (measured): {nonreducible}")
    # the record-is-metric re-encoding, rebuilt (HA G28)
    M = [[1, 0, 0], [0, 1, 0], [1, 1, 2]]      # (q11,q22,q12) -> the link counts
    det = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
           - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
           + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
    anchor(f"A{len(ANCHORS) + 1:02d}", "HA: the record-is-metric re-encoding determinant",
           HA["tables"]["readout_reencoding"]["determinant"], str(det),
           "v13/code/ha_successor_receipt.json readout_reencoding")
    say(f"        record-is-metric re-encoding: determinant {det} (HA G28)")
    orb_by_prime: dict = {}
    for p in declared_primes():
        n_src = p ** (k_rank + d_dim)
        _a, gp = ha_arena(p, rho_mod_p(rho, p))
        orb_by_prime[p] = (n_src, len(orbits_unionfind([gp], n_src)))
    say(f"        orbits of <R_HH> on the carrier, by prime: "
        f"{ {p: orb_by_prime[p][1] for p in sorted(orb_by_prime)} } "
        f"(the action is free, so every orbit has length p)")
    say("")

    # ==================== 6. THE COMMITTED INSTANCE TABLE ====================
    say("--- 6. THE COMMITTED TRANSPORT INSTANCES (scope 1), REBUILT OR ANCHORED ---")
    cl = XBA["tables"]["the_commutator_law"]
    inst_rows = []
    for name in sorted(cl):
        n = cl[name]["the_order_of_the_defect"]
        order = cl[name]["the_order_of_the_group_generated_by_W_and_D"]
        rebuilt = name in ("base G @ GP-E", "base G @ GP-F", "base T", "base S'",
                           "species 4")
        car = {"base 1 @ SP-E": 36, "base 1 @ SP-F": 36}.get(name, 81)
        if name == "species 4":
            car = 256
        inst_rows.append((name, car, n, order, rebuilt))
    inst_rows = instance_orders(inst_rows)
    for (name, car, n, order, rebuilt) in inst_rows:
        anchor(f"A{len(ANCHORS) + 1:02d}", f"XBA: |<W,D>| = 2*ord(D) at {name}",
               2 * n, order, "v13/code/xba_crossbase_receipt.json the_commutator_law")
    perm_orders = {"base G @ GP-E": len(G81), "base G @ GP-F": len(G81),
                   "base T": len(GT), "base S'": len(GS), "species 4": len(G256)}
    cmp_ok = all(comparator_group_order(perm_orders[nm], 2 * n) == ordr
                 for (nm, _c, n, ordr, rb) in inst_rows if rb)
    cmp_indep = not _rebuild_is_abstract()

    def isomorphism_audit(Wp, Dp, npts):
        """The abstract model is not merely of the right ORDER: the explicit map
        (i, k) -> D^i W^k from the model into the permutation rebuild is checked
        bijective and multiplicative on every ordered pair.  Order agreement
        does not imply isomorphism; this does."""
        n = porder(Dp)
        els, mul, e = dihedral_abstract(n)
        img = {}
        for (i, k) in els:
            img[(i, k)] = tuple(pmul(perm_pow(Dp, i), perm_pow(Wp, k)))
        bij = len(set(img.values())) == len(els)
        bad = 0
        for a in els:
            for b in els:
                if img[mul(a, b)] != tuple(pmul(list(img[a]), list(img[b]))):
                    bad += 1
        return bij, bad, len(els)

    iso_rows = []
    for (nm, Wp, Dp, npts) in (("base G @ GP-E", W81, D81, 81),
                               ("base T", W81, DT81, 81),
                               ("base S'", W81, tensor(DS9, pident(9)), 81),
                               ("species 4", W256, D256, 256)):
        bij, bad, sz = isomorphism_audit(Wp, Dp, npts)
        iso_rows.append({"instance": nm, "model_order": sz, "bijective": bij,
                         "multiplication_violations": bad})
    iso_ok = all(r["bijective"] and r["multiplication_violations"] == 0
                 for r in iso_rows)
    g03 = gate("G03", "THE ABSTRACT DIHEDRAL MODEL IS AUDITED BY AN INDEPENDENTLY "
               "CONSTRUCTED COMPARATOR (RUNBOOK 14 addendum, v13 #219): the "
               "comparator is the permutation rebuild from the completion Q and "
               "Sigma, never the abstract model it audits; the two agree in ORDER "
               "at every rebuilt instance, and the model is certified ISOMORPHIC "
               "to the rebuild by the explicit map (i,k) -> D^i W^k, measured "
               "bijective and multiplicative on every ordered pair -- order "
               "agreement alone would not imply isomorphism, and both census "
               "routes consume this model",
               cmp_ok and cmp_indep and iso_ok,
               {"rebuilt_instances": sorted(perm_orders),
                "comparator_is_the_permutation_rebuild": cmp_indep,
                "agreements": cmp_ok, "isomorphism_audit": iso_rows})
    report("G03", g03, f"{len(perm_orders)} instances rebuilt as permutation "
           f"groups; comparator independent: {cmp_indep}; explicit isomorphism "
           f"verified at {len(iso_rows)} instances, "
           f"{sum(r['multiplication_violations'] for r in iso_rows)} violations")
    say(f"        {'instance':16s}{'carrier':9s}{'ord D':7s}{'|<W,D>|':9s}rebuilt")
    for (name, car, n, order, rebuilt) in inst_rows:
        say(f"        {name:16s}{car:<9d}{n:<7d}{order:<9d}{rebuilt}")
    # base 1's defect is under-determined by the committed data: sweep the
    # whole declared ambiguity set rather than guess.
    # the two constraint values are READ from XBA's receipt and anchored, never
    # typed here: a change in XBA would kill the run rather than silently move
    # the sweep to another class.
    base1_D_fixed = XBA["tables"]["bases"]["base 1 @ SP-E"]["D_fixed"]
    baseS_D_fixed = XBA["tables"]["third_instances"]["base S"]["D_fixed"]
    anchor(f"A{len(ANCHORS) + 1:02d}",
           "XBA: base 1 @ SP-E's defect fixed configurations (the constraint the "
           "ambiguity sweep is filtered by)",
           18, base1_D_fixed, "v13/code/xba_crossbase_receipt.json bases")
    anchor(f"A{len(ANCHORS) + 1:02d}",
           "XBA: base S's defect fixed configurations (the constraint the "
           "ambiguity sweep is filtered by)",
           45, baseS_D_fixed,
           "v13/code/xba_crossbase_receipt.json third_instances")
    amb1 = []
    for a, b in itertools.combinations(range(4), 2):
        dd = pident(4)
        dd[a], dd[b] = dd[b], dd[a]
        if pmul(S4, pmul(dd, S4)) == pinv(dd) \
                and pfixed(tensor(dd, pident(9))) == base1_D_fixed:
            D36 = tensor(dd, pident(9))
            G36 = closure([tuple(W36), tuple(D36)], 36)
            if len(G36) == 4:
                amb1.append((dd, len(G36)))
    amb1 = ambiguity_set(amb1)
    baseS_defect_order = XBA["tables"]["the_commutator_law"]["base S"][
        "the_order_of_the_defect"]
    amb_S = ambiguity_set([q for q in fam if fam_class[tuple(q)]
                           == (baseS_defect_order, baseS_D_fixed)])
    amb_S_computed = sum(1 for q in fam if fam_class[tuple(q)]
                         == (baseS_defect_order, baseS_D_fixed))
    say(f"        base 1's defect is under-determined by the committed data: "
        f"{len(amb1)} candidates satisfy every committed datum, all giving "
        f"|<W,D>| = {sorted({o for _d, o in amb1})}")
    say(f"        base S's defect lies in the (ord 2, 45 fixed) class: "
        f"{len(amb_S)} members, all of defect order "
        f"{sorted({fam_class[tuple(q)][0] for q in amb_S})}")
    g04 = gate("G04", "THE UNDER-DETERMINED COMMITTED INSTANCES ARE SWEPT, NOT "
               "GUESSED: base 1's defect and base S's defect are each replaced by "
               "the whole declared set of candidates consistent with every "
               "committed datum -- the constraints being READ from the pinned "
               "XBA receipt and anchored, and the class size COMPUTED from the "
               "family classification rather than typed -- and every member of "
               "each set gives the same group order, so the ambiguity cannot "
               "move any census count",
               len(amb1) > 1 and len({o for _d, o in amb1}) == 1
               and len(amb_S) == amb_S_computed
               and len({fam_class[tuple(q)][0] for q in amb_S}) == 1,
               {"base_1_candidates": len(amb1),
                "base_1_group_orders": sorted({o for _d, o in amb1}),
                "base_1_constraint_read_from_XBA": base1_D_fixed,
                "base_S_candidates": len(amb_S),
                "base_S_class_size_computed_from_the_family": amb_S_computed,
                "base_S_constraint_read_from_XBA": [baseS_defect_order,
                                                    baseS_D_fixed],
                "base_S_defect_orders":
                    sorted({fam_class[tuple(q)][0] for q in amb_S})})
    report("G04", g04, f"base 1: {len(amb1)} candidates; base S: {len(amb_S)} "
           f"candidates; group orders invariant")
    say("")

    # ==================== 7. THE CONTROLS ====================================
    say("--- 7. THE CONTROLS: THE IDENTITY SELF-MORPHISM, THE DEGENERATE "
        "FUNCTOR, THE STRUCTURE-BREAKING MAPS ---")
    progress("controls")

    # the deformation-side arena at the first declared prime
    p0 = declared_primes()[0]
    r0 = rho_mod_p(rho, p0)
    src0, gen0 = ha_arena(p0, r0)
    tgt0 = make_perm_arena(G81, 81)

    # POSITIVE CONTROL: the identity self-morphism on each side
    id_src = evaluate_candidate(src0, src0, list(src0["els"]),
                                list(range(src0["npts"])))
    id_tgt = evaluate_candidate(tgt0, tgt0, list(tgt0["els"]),
                                list(range(tgt0["npts"])))
    tgtT = make_perm_arena(GT, 81)
    id_tgtT = evaluate_candidate(tgtT, tgtT, list(tgtT["els"]),
                                 list(range(tgtT["npts"])))
    g05 = gate("G05", "POSITIVE CONTROL: the identity self-morphism inside each "
               "arena is FOUND by the very census machinery used for the bridge "
               "-- every predicate clause holds and both non-triviality clauses "
               "hold, on the deformation side, on the abelian transport instance "
               "and on the NON-ABELIAN transport instance alike, so the action's "
               "orientation convention is exercised where it can bite",
               id_src["accepted"] and id_tgt["accepted"] and id_tgtT["accepted"],
               {"deformation_side": id_src, "transport_side": id_tgt,
                "non_abelian_transport_side": id_tgtT})
    report("G05", g05, f"identity accepted on all three arenas "
           f"(SP3 cells {id_src['sp3_cells']} / {id_tgt['sp3_cells']} / "
           f"{id_tgtT['sp3_cells']})")

    # DEGENERATE control: SP holds, NT must reject
    deg_phi = [tgt0["e"]] * len(src0["els"])
    deg_Phi = [0] * src0["npts"]
    deg = evaluate_candidate(src0, tgt0, deg_phi, deg_Phi)
    g06 = gate("G06", "THE DEGENERATE FUNCTOR IS A NAMED KILL: the constant "
               "carrier map with the trivial group map SATISFIES the "
               "structure-preservation predicate and is REJECTED by the "
               "non-triviality clauses (DEGENERATE-COLLAPSE) -- so the census "
               "cannot be won by collapsing either side to a point",
               deg["SP"] and not deg["NT1"] and not deg["NT2"]
               and not deg["accepted"],
               {"SP": deg["SP"], "NT1": deg["NT1"], "NT2": deg["NT2"],
                "accepted": deg["accepted"], "kill": "DEGENERATE-COLLAPSE"})
    report("G06", g06, f"degenerate functor: SP={deg['SP']} NT1={deg['NT1']} "
           f"NT2={deg['NT2']} accepted={deg['accepted']}")

    # NEGATIVE CONTROLS WITH TEETH
    n0 = src0["npts"]
    dbl = []
    for i in range(n0):
        m1 = i % p0
        m0 = (i // p0) % p0
        rest = i // (p0 * p0)
        dbl.append(rest * p0 * p0 + ((2 * m0) % p0) * p0 + ((2 * m1) % p0))
    brk_a = evaluate_candidate(src0, src0, breaking_group_map(src0["els"], p0), dbl)
    acc_a = evaluate_candidate(src0, src0, [(2 * g) % p0 for g in src0["els"]], dbl)
    swap = list(range(n0))
    j1 = src0["act"](1, 0)
    other = next(x for x in range(n0) if x not in {src0["act"](g, 0)
                                                   for g in src0["els"]})
    swap[0], swap[other] = swap[other], swap[0]
    brk_b = evaluate_candidate(src0, src0, list(src0["els"]), swap)
    g07 = gate("G07", "NEGATIVE CONTROL WITH TEETH: the register-doubling carrier "
               "map with the IDENTITY group map is REJECTED by the equivariance "
               "clause, while the SAME carrier map with the group map R -> R^2 is "
               "ACCEPTED -- so the predicate is sensitive to exactly the structure "
               "it claims to test and not to gross malformation; a second breaking "
               "map (two points of different orbits transposed) is rejected too",
               (not brk_a["SP3"]) and brk_a["NT1"] and brk_a["NT2"]
               and acc_a["accepted"] and (not brk_b["SP3"]),
               {"break_A_sp3_bad_cells": brk_a["sp3_bad"],
                "break_A_sp3_cells": brk_a["sp3_cells"],
                "break_A_nondegenerate": brk_a["NT1"] and brk_a["NT2"],
                "the_same_carrier_map_with_the_right_group_map":
                    acc_a["accepted"],
                "break_B_sp3_bad_cells": brk_b["sp3_bad"],
                "second_orbit_point": other, "first_orbit_image": j1})
    report("G07", g07, f"BREAK-A rejected at {brk_a['sp3_bad']} of "
           f"{brk_a['sp3_cells']} cells; the same map with R->R^2 accepted; "
           f"BREAK-B rejected at {brk_b['sp3_bad']} cells")

    # a declared non-homomorphism, to give SP1 teeth
    nonhom = list(src0["els"])
    nonhom[1] = (nonhom[1] + 1) % p0
    nh = evaluate_candidate(src0, src0, nonhom, list(range(n0)))
    g08 = gate("G08", "THE COMPOSITION CLAUSE HAS TEETH: a declared "
               "NON-homomorphism that fixes the identity is REJECTED by SP1, "
               "measured over all |G|^2 ordered pairs",
               (not nh["SP1"]) and nh["sp1_bad"] > 0
               and nh["sp1_cells"] == len(src0["els"]) ** 2,
               {"sp1_cells": nh["sp1_cells"], "sp1_bad": nh["sp1_bad"]})
    report("G08", g08, f"non-hom rejected at {nh['sp1_bad']} of "
           f"{nh['sp1_cells']} composition cells")
    say("")

    # ==================== 8. THE GROUP-LEVEL CENSUS ==========================
    say("--- 8. THE MORPHISM CENSUS AT THE GROUP LEVEL, BOTH DIRECTIONS ---")
    progress("census scope 1")
    taint = [0]
    route_a_calls = [0]
    route_b_calls = [0]
    primes = declared_primes()

    def census_cells(rows, label):
        """One census over (prime, instance) cells, both directions, two
        independent routes for the forward direction."""
        out = []
        for p in primes:
            for (name, car, n, order, rebuilt) in rows:
                els, mul, e = dihedral_abstract(n)
                route_a_calls[0] += 1
                ca, cb, imgs = homs_count_two_routes(p, els, mul, e, taint)
                route_b_calls[0] += 1
                nontriv_fwd = sum(1 for g in imgs if g != e)
                gens = [(1 % n, 0), (0, 1)]
                rev, _idx = homs_into_Zp_generators(p, els, mul, e, gens)
                rev_b, comm_sz, ab_sz = homs_into_Zp_lattice(p, els, mul, e)
                out.append({"scope": label, "p": p, "instance": name,
                            "carrier": car, "ord_D": n, "group_order": order,
                            "hom_forward_route_a": ca, "hom_forward_route_b": cb,
                            "nontrivial_forward": nontriv_fwd,
                            "hom_reverse_route_a": rev,
                            "hom_reverse_route_b": rev_b,
                            "nontrivial_reverse": reverse_nontrivial(rev, nontriv_fwd),
                            "commutator_subgroup_order": comm_sz,
                            "abelianisation_order": ab_sz,
                            "gcd_p_group_order": _gcd(p, order)})
        return out

    rows1 = committed_instances(inst_rows)
    cells1 = census_cells(rows1, "scope-1 (committed instances)")
    n_cells1 = len(cells1)
    expect1 = len(primes) * len(rows1)
    nt_fwd1 = sum(c["nontrivial_forward"] for c in cells1)
    nt_rev1 = sum(c["nontrivial_reverse"] for c in cells1)
    routes_agree1 = all(c["hom_forward_route_a"] == c["hom_forward_route_b"]
                        for c in cells1) and \
                    all(c["hom_reverse_route_a"] == c["hom_reverse_route_b"]
                        for c in cells1)
    seen_cells = {(c["p"], c["instance"]) for c in cells1}
    g09 = gate("G09", "CELL-COMPLETENESS OF THE COMMITTED-SCOPE CENSUS: every "
               "(prime, instance) cell of the declared scope is visited exactly "
               "once, the cell count is COMPUTED from the declared sets and "
               "equals the number of rows returned, and both directions are "
               "counted at every cell",
               n_cells1 == expect1 and len(seen_cells) == n_cells1
               and expect1 == 7 * 8,
               {"primes": len(primes), "instances": len(rows1),
                "cells_expected": expect1, "cells_visited": n_cells1,
                "distinct_cells": len(seen_cells),
                "directions": sum(1 for k in ("nontrivial_forward",
                                              "nontrivial_reverse")
                                  if all(k in c for c in cells1)),
                "directed_cells": 2 * n_cells1})
    report("G09", g09, f"{n_cells1} cells = {len(primes)} primes x "
           f"{len(rows1)} instances; {2 * n_cells1} directed cells")
    g10 = gate("G10", "TWO INDEPENDENT ROUTES AGREE AT EVERY CELL: the "
               "element-power route (iterated multiplication in the target) and "
               "the subgroup-lattice route (every subset closed, the cyclic "
               "subgroups of order dividing p counted with their generators) "
               "return the same homomorphism count at every cell, in both "
               "directions, and neither route reads the other",
               routes_agree1 and taint[0] == 0 and route_a_calls[0] > 0
               and route_b_calls[0] > 0,
               {"cells": n_cells1, "routes_agree": routes_agree1,
                "taint_events": taint[0], "route_a_invocations": route_a_calls[0],
                "route_b_invocations": route_b_calls[0]})
    report("G10", g10, f"routes agree at {n_cells1} cells; taint {taint[0]}; "
           f"invocations {route_a_calls[0]}/{route_b_calls[0]}")
    say(f"        {'p':4s}{'instance':16s}{'|G|':6s}{'hom(Z/p,G)':12s}"
        f"{'nontriv':9s}{'hom(G,Z/p)':12s}{'nontriv':9s}gcd(p,|G|)")
    for c in cells1:
        say(f"        {c['p']:<4d}{c['instance']:16s}{c['group_order']:<6d}"
            f"{c['hom_forward_route_a']:<12d}{c['nontrivial_forward']:<9d}"
            f"{c['hom_reverse_route_a']:<12d}{c['nontrivial_reverse']:<9d}"
            f"{c['gcd_p_group_order']}")
    say(f"        TOTAL non-degenerate group morphisms, forward : {nt_fwd1} "
        f"of {n_cells1} cells")
    say(f"        TOTAL non-degenerate group morphisms, reverse : {nt_rev1} "
        f"of {n_cells1} cells")
    say("")

    # scope 2: GEN's twelve rebuilt classes
    progress("census scope 2")
    say("--- 8b. THE SAME CENSUS OVER GEN's TWELVE REBUILT CLASSES (scope 2) ---")
    cls = GEN["tables"]["completion_rebuilds"]["one_full_rebuild_per_measured_class"]
    class_rows = []
    class_defect = {}
    for key in class_keys(cls):
        q = cls[key]["Q"]
        dd = gen_defect(q, 3)
        class_defect[key] = dd
        n = porder(dd)
        Gc = closure([tuple(W81), tuple(tensor(dd, pident(9)))], 81)
        anchor(f"A{len(ANCHORS) + 1:02d}", f"GEN: class {key} -- the defect's order",
               cls[key]["the_order_of_the_defect"], n,
               "v13/code/gen_generality_receipt.json completion_rebuilds")
        anchor(f"A{len(ANCHORS) + 1:02d}",
               f"GEN: class {key} -- the defect's fixed configurations",
               cls[key]["the_defects_fixed_configurations"],
               pfixed(tensor(dd, pident(9))),
               "v13/code/gen_generality_receipt.json completion_rebuilds")
        if n > 1:
            # at the equivariant class GEN's links are refused, so its measured
            # holonomy group is trivial while <W,D> = <W> has order 2: two
            # coordinates, separated at X02 and never compared across.
            anchor(f"A{len(ANCHORS) + 1:02d}",
                   f"GEN: class {key} -- the element orders of <W,D>",
                   cls[key]["element_orders"],
                   sorted({porder(list(g)) for g in Gc}),
                   "v13/code/gen_generality_receipt.json completion_rebuilds")
        class_rows.append((key, 81, n, len(Gc), True))
    # the measured holonomy order agrees with |<W,D>| at every class of defect
    # order >= 2; at the equivariant class the two coordinates differ, because
    # GEN's links are refused there (a like-for-like disclosure, X02).
    hol_ok = all(cls[key]["the_measured_group_order_at_the_symmetric_setting"]
                 == order for (key, _c, n, order, _r) in class_rows if n > 1)
    anchor(f"A{len(ANCHORS) + 1:02d}",
           "GEN: |<W,D>| = the measured holonomy group order at every class of "
           "defect order >= 2",
           True, hol_ok,
           "v13/code/gen_generality_receipt.json completion_rebuilds")
    cells2 = census_cells(class_rows, "scope-2 (GEN's rebuilt classes)")
    nt_fwd2 = sum(c["nontrivial_forward"] for c in cells2)
    live2 = sorted({(c["p"], c["instance"]) for c in cells2
                    if c["nontrivial_forward"] > 0})
    g11 = gate("G11", "CELL-COMPLETENESS OF THE EXTENDED-SCOPE CENSUS: every "
               "(prime, rebuilt class) cell is visited exactly once and the count "
               "is computed from the declared sets",
               len(cells2) == len(primes) * len(class_rows)
               and len({(c["p"], c["instance"]) for c in cells2}) == len(cells2)
               and len(class_rows) == len(cls),
               {"primes": len(primes), "classes_swept": len(class_rows),
                "classes_committed_by_the_receipt": len(cls),
                "cells": len(cells2)})
    report("G11", g11, f"{len(cells2)} cells = {len(primes)} primes x "
           f"{len(class_rows)} classes")
    say(f"        non-degenerate group morphisms over scope 2 : {nt_fwd2}, "
        f"living at exactly these cells:")
    for (p, nm) in live2:
        say(f"          p = {p:<3d} {nm}")
    say("")

    # ==================== 9. ARENA-INVARIANCE ===============================
    say("--- 9. ARENA-INVARIANCE (pin requirement 4; RUNBOOK 15) ---")
    progress("arena invariance")
    per_prime_empty = {}
    for p in primes:
        per_prime_empty[p] = all(c["nontrivial_forward"] == 0
                                 and c["nontrivial_reverse"] == 0
                                 for c in cells1 if c["p"] == p)
    invariant1 = len(set(per_prime_empty.values())) == 1 and len(primes) > 1
    g12 = gate("G12", "THE COMMITTED-SCOPE VERDICT IS INVARIANT ACROSS THE WHOLE "
               "DECLARED PRIME SWEEP: the census answer is the same at every one "
               "of the declared primes, so no quantity that moves with the "
               "declared reduction prime carries it (the sweep must contain more "
               "than one prime for the gate to be posable)",
               invariant1,
               {"primes": primes, "empty_by_prime":
                {str(k): v for k, v in sorted(per_prime_empty.items())},
                "invariant": invariant1})
    report("G12", g12, f"empty at every one of {len(primes)} primes: "
           f"{sorted(set(per_prime_empty.values()))}")

    # the prime-tracking control: it must BITE
    defect_spec_set = set(spectrum_for_comparison(defect_orders, holonomy_orders))
    track = {p: tracking_candidate_verdict(p, defect_spec_set) for p in primes}
    track_extended = {p: any(c["nontrivial_forward"] > 0 for c in cells2
                             if c["p"] == p) for p in primes}
    bites = (len({v for v in track.values()}) > 1)
    agrees = (track == track_extended)
    g13 = gate("G13", "THE PRIME-TRACKING GATE BITES, MEASURED: the declared "
               "morphism-by-spectrum candidate F3 SURVIVES at some declared "
               "primes and DIES at others, so the arena-invariance rule that "
               "rejects it is not vacuous; and the candidate's verdict is "
               "measured to coincide, prime by prime, with the extended-scope "
               "census's own answer -- the spectrum criterion IS the "
               "extended-scope census, and both are prime-tracking",
               bites and agrees,
               {"F3_by_prime": {str(k): v for k, v in sorted(track.items())},
                "extended_scope_census_by_prime":
                    {str(k): v for k, v in sorted(track_extended.items())},
                "the_candidate_is_not_prime_uniform": bites,
                "the_two_readings_agree": agrees})
    report("G13", g13, f"F3 survives at {sorted(p for p in primes if track[p])}, "
           f"dies at {sorted(p for p in primes if not track[p])}; agrees with the "
           f"extended census: {agrees}")
    ha_memb = {str(k): v for k, v in
               sorted(ha_bridge["membership_in_the_defect_spectrum_by_prime"].items(),
                      key=lambda kv: int(kv[0]))}
    anchor(f"A{len(ANCHORS) + 1:02d}",
           "HA: membership of p in GEN's defect order spectrum, by prime",
           ha_memb, {str(k): v for k, v in sorted(track.items())},
           "v13/code/ha_successor_receipt.json bridge")
    admits_by_instance = {nm: [c["nontrivial_forward"] > 0
                               for c in (cells1 + cells2) if c["instance"] == nm]
                          for nm in sorted({c["instance"]
                                            for c in (cells1 + cells2)})}
    n_admit_every = sum(1 for v in admits_by_instance.values() if all(v))
    n_admit_two = sum(1 for v in admits_by_instance.values()
                      if sum(1 for x in v if x) >= 2)
    two_prime_product = primes[0] * primes[1]
    all_prime_product = 1
    for p in primes:
        all_prime_product *= p
    max_two_ord = 2 * max(ord_spec)
    g14 = gate("G14", "THE PRIME-TRACKING CANDIDATE IS EXCLUDED FROM THE VERDICT "
               "(pin requirement 4): a candidate whose survival is a function of "
               "the declared reduction prime is an arena artifact; it is recorded "
               "as an instrument reading and the verdict is taken over the "
               "arena-invariant content only -- the intersection over the declared "
               "prime sweep, which is measured EMPTY at every instance of every "
               "declared scope, and no instance admits even two declared primes.  "
               "THE REASON IS SCOPED TO THE NINE-LABEL ARENA: admitting two "
               "declared primes needs 2*ord(D) divisible by their product, and "
               "the whole nine-label family's maximum is smaller than that "
               "product -- both numbers computed here.  At the sixteen-label "
               "arena the same clause is CONTINGENT, not forced, and a witness "
               "is exhibited",
               (not any_instance_admits_every_prime(
                   list(admits_by_instance.values())))
               and n_admit_two == 0,
               {"instances_tested": len(admits_by_instance),
                "instances_admitting_EVERY_declared_prime": n_admit_every,
                "instances_admitting_at_least_two_declared_primes": n_admit_two,
                "the_smallest_product_of_two_declared_primes": two_prime_product,
                "the_product_of_all_declared_primes": all_prime_product,
                "the_largest_2_ord_D_over_the_nine_label_family": max_two_ord,
                "the_reason_is_structural_at_m_equals_3":
                    max_two_ord < two_prime_product,
                "the_arena_invariant_census": "EMPTY at every instance of every "
                                              "declared scope"})
    report("G14", g14, f"no instance of any declared scope admits a non-trivial "
           f"morphism at every declared prime, and none admits two: at m = 3 "
           f"that needs 2*ord(D) divisible by {two_prime_product} while the "
           f"family's maximum is {max_two_ord}")

    # RUNBOOK 14 self-tests: relabelling, conjugation, generator change --
    # evaluated FRESH, with the tested set fixed by declaration
    _SELFTEST_PHASE[0] = True
    declared_selftests = ["relabel-source", "relabel-target", "conjugate-target",
                          "change-generator"]
    tested = selftest_tested_set(declared_selftests,
                                 {"relabel-source": True, "relabel-target": False,
                                  "conjugate-target": True,
                                  "change-generator": False})
    selftest_rows = []
    rl_src = relabelling_of(src0["npts"], 1)
    rl_tgt = relabelling_of(81, 1)
    cj_tgt = conjugator_of(81, 2)
    moved = {"relabel_source": perm_moved(rl_src),
             "relabel_target": perm_moved(rl_tgt),
             "conjugator": perm_moved(cj_tgt)}
    # The candidates the self-tests carry.  The first is ACCEPTED and
    # non-degenerate -- the register doubling with the group map R -> R^2, the
    # very pair G07 uses -- so the verdict under audit CAN move; the degenerate
    # functor is carried beside it as a second row.
    acc_phi = [(2 * g) % p0 for g in src0["els"]]
    acc_Phi = list(dbl)
    W_el0 = G81.index(tuple(W81))
    tw_phi = list(tgt0["els"])
    tw_Phi = [tgt0["act"](W_el0, x) for x in range(tgt0["npts"])]
    base_accepted = evaluate_candidate(src0, src0, acc_phi, acc_Phi)["accepted"]
    base_degenerate = evaluate_candidate(src0, tgt0, deg_phi, deg_Phi)["accepted"]
    base_target_translation = evaluate_candidate(tgt0, tgt0, tw_phi,
                                                 tw_Phi)["accepted"]
    for name in tested:
        if name == "relabel-source":
            rl = rl_src
            gen2 = [rl[gen0[pinv(rl)[i]]] for i in range(src0["npts"])]
            arena = make_cyclic_arena(p0, src0["npts"], gen2, fresh=True)
            acc_ = evaluate_candidate(
                arena, arena, acc_phi,
                selftest_carrier_image(rl, acc_Phi, True))["accepted"]
            deg_ = evaluate_candidate(
                arena, tgt0, deg_phi,
                selftest_carrier_image(rl, deg_Phi, False))["accepted"]
            base_ = (base_accepted, base_degenerate)
        elif name == "relabel-target":
            rl = rl_tgt
            G2 = [tuple(rl[g[pinv(rl)[i]]] for i in range(81)) for g in G81]
            arena = make_perm_arena(sorted(G2), 81)
            acc_ = evaluate_candidate(
                arena, arena, list(arena["els"]),
                selftest_carrier_image(rl, tw_Phi, True))["accepted"]
            deg_ = evaluate_candidate(src0, arena, [arena["e"]] * p0,
                                      [rl[0]] * src0["npts"])["accepted"]
            base_ = (base_target_translation, base_degenerate)
        elif name == "conjugate-target":
            cj = cj_tgt
            G2 = [tuple(cj[g[pinv(cj)[i]]] for i in range(81)) for g in G81]
            arena = make_perm_arena(sorted(G2), 81)
            acc_ = evaluate_candidate(
                arena, arena, list(arena["els"]),
                selftest_carrier_image(cj, tw_Phi, True))["accepted"]
            deg_ = evaluate_candidate(src0, arena, [arena["e"]] * p0,
                                      [cj[0]] * src0["npts"])["accepted"]
            base_ = (base_target_translation, base_degenerate)
        else:
            gen2 = swept_generator(gen0, 2)
            arena = make_cyclic_arena(p0, src0["npts"], gen2, fresh=True)
            acc_ = evaluate_candidate(arena, arena, acc_phi, acc_Phi)["accepted"]
            deg_ = evaluate_candidate(arena, tgt0, deg_phi, deg_Phi)["accepted"]
            base_ = (base_accepted, base_degenerate)
        selftest_rows.append({"self_test": name,
                              "accepted_candidate_verdict": acc_,
                              "degenerate_candidate_verdict": deg_,
                              "matches_base": (acc_, deg_) == base_})
    # The generator sweep now READS the arena it builds: at each swept
    # generator R^j the arena's own orbit structure is recomputed by union-find,
    # the action is measured free, and the accepted candidate is re-evaluated
    # inside that arena.  A generator that is not a generator moves these.
    gen_rows = []
    for j in range(1, p0):
        gen2 = swept_generator(gen0, j)
        arena = make_cyclic_arena(p0, src0["npts"], gen2, fresh=True)
        orbs_j = orbits_unionfind([gen2], src0["npts"])
        free_j = all(arena["act"](g, x) != x
                     for g in range(1, p0) for x in range(src0["npts"]))
        acc_j = evaluate_candidate(arena, arena, acc_phi, acc_Phi)["accepted"]
        gen_rows.append({"j": j, "orbits": len(orbs_j), "action_is_free": free_j,
                         "accepted_candidate_verdict": acc_j,
                         "orbit_sizes": sorted({len(o) for o in orbs_j})})
    n_orb_declared = src0["npts"] // p0
    gen_ok = all(r["orbits"] == n_orb_declared and r["action_is_free"]
                 and r["accepted_candidate_verdict"] == base_accepted
                 and r["orbit_sizes"] == [p0] for r in gen_rows)
    _SELFTEST_PHASE[0] = False
    g15 = gate("G15", "RUNBOOK 14 SYMMETRY SELF-TESTS, ON A CANDIDATE THE ACTION "
               "COULD MOVE: the predicate's verdict is measured INVARIANT under "
               "the arena's own action -- relabelling either carrier, conjugating "
               "the transport action by a carrier permutation, and replacing the "
               "source generator R by R^j for every j -- carried on an ACCEPTED "
               "NON-DEGENERATE candidate (the register doubling with the group "
               "map R -> R^2, and the target's identity self-morphism) as well as "
               "on the degenerate one; and the generator sweep CONSUMES the arena "
               "it builds, recomputing that arena's orbit count and freeness and "
               "re-evaluating the accepted candidate inside it.  The tested set "
               "is fixed by declaration and never selected by the verdicts under "
               "audit",
               all(r["matches_base"] for r in selftest_rows)
               and tested == declared_selftests
               and base_accepted and base_target_translation and gen_ok
               and all(v > 0 for v in moved.values()),
               {"self_tests": selftest_rows,
                "declared_tested_set": declared_selftests,
                "tested_set_used": tested,
                "the_carried_candidates":
                    {"accepted_non_degenerate": "the register doubling with the "
                                                "group map R -> R^2 on the source "
                                                "side; the target's translation "
                                                "self-morphism (carrier map = the "
                                                "action of W, group map = the "
                                                "identity automorphism)",
                     "degenerate": "the constant carrier map with the trivial "
                                   "group map"},
                "base_verdicts": {"accepted_candidate": base_accepted,
                                  "degenerate_candidate": base_degenerate,
                                  "target_translation": base_target_translation},
                "points_moved_by_the_declared_arena_actions": moved,
                "generator_sweep": gen_rows,
                "orbits_declared_for_the_swept_arenas": n_orb_declared})
    report("G15", g15, f"{len(selftest_rows)} self-tests on an accepted and a "
           f"degenerate candidate, all matching; arena actions move "
           f"{sorted(moved.values())} points; generator sweep reads "
           f"{[r['orbits'] for r in gen_rows]} orbits, free "
           f"{[r['action_is_free'] for r in gen_rows]}, accepted "
           f"{[r['accepted_candidate_verdict'] for r in gen_rows]}")
    st = dict(_CACHE_STATS)
    g16 = gate("G16", "THE SELF-TESTS EVALUATE FRESH, AND THE CACHE PATH IS "
               "EXERCISED (RUNBOOK 14 addenda, v13 #185 and #219): every "
               "self-test evaluation bypasses the memo cache, the self-test's "
               "cache-hit count is measured ZERO against a nonzero bypass count, "
               "and the cache is measured to be looked up and hit elsewhere in "
               "the run -- a zero-hit gate over zero lookups would be vacuous",
               st["selftest_hits"] == 0 and st["bypass"] > 0
               and st["lookups"] > 0 and st["hits"] > 0,
               {"cache": st})
    report("G16", g16, f"selftest hits {st['selftest_hits']}, bypasses "
           f"{st['bypass']}, lookups {st['lookups']}, hits {st['hits']}")
    say("")

    # ==================== 10. THE FUNCTOR-LEVEL CENSUS =======================
    say("--- 10. THE FUNCTOR-LEVEL CENSUS: THE CARRIER MAPS THEMSELVES ---")
    progress("functor census")
    functor_rows = []
    for c in cells1:
        if c["instance"] not in perm_orders:
            continue
        p = c["p"]
        n_src, n_orb_uf = orb_by_prime[p]
        n_orb_div = n_src // p
        els, mul, e = dihedral_abstract(c["ord_D"])
        imgs = homs_route_a(p, els, mul, e)
        total = sum(equivariant_map_count(c["carrier"], n_orb_uf) for _g in imgs)
        nondeg = sum(equivariant_map_count(c["carrier"], n_orb_uf)
                     for g in imgs if g != e)
        functor_rows.append({"p": p, "instance": c["instance"],
                             "source_points": n_src, "orbits_unionfind": n_orb_uf,
                             "orbits_by_division": n_orb_div,
                             "group_maps": len(imgs),
                             "structure_preserving_pairs_bits": total.bit_length(),
                             "non_degenerate_pairs": nondeg})
    functor_rows = functor_census_cells(functor_rows)
    orb_ok = all(r["orbits_unionfind"] == r["orbits_by_division"]
                 for r in functor_rows)
    expect_f = len(primes) * len(perm_orders)
    fcells_distinct = len({(r["p"], r["instance"]) for r in functor_rows})
    g17 = gate("G17", "THE ORBIT COUNT IS COMPUTED TWICE BY DIFFERENT MEANS AND "
               "THE FUNCTOR-LEVEL CENSUS IS CELL-COMPLETE: union-find over the "
               "generator's own edges and the division of the carrier size by the "
               "orbit length (the action is measured free) agree at every cell; "
               "and the cell count is COMPUTED from the declared sets -- the "
               "declared primes times the instances rebuilt as permutation groups "
               "-- with every cell visited exactly once, so a dropped cell cannot "
               "pass (RUNBOOK 13 addendum, v13 #234)",
               orb_ok and len(functor_rows) == expect_f
               and fcells_distinct == expect_f,
               {"cells_expected": expect_f, "cells_visited": len(functor_rows),
                "distinct_cells": fcells_distinct, "agreements": orb_ok,
                "primes": len(primes), "instances": len(perm_orders)})
    report("G17", g17, f"orbit counts agree at {len(functor_rows)} cells; "
           f"{fcells_distinct} distinct of {expect_f} expected")
    nondeg_total = sum(r["non_degenerate_pairs"] for r in functor_rows)
    say(f"        {'p':4s}{'instance':16s}{'|C_HA|':9s}{'orbits':8s}"
        f"{'group maps':12s}{'SP pairs (bits)':19s}non-degenerate")
    for r in functor_rows:
        say(f"        {r['p']:<4d}{r['instance']:16s}{r['source_points']:<9d}"
            f"{r['orbits_unionfind']:<8d}{r['group_maps']:<12d}"
            f"{r['structure_preserving_pairs_bits']:<19d}"
            f"{r['non_degenerate_pairs']}")
    say(f"        the SP-satisfying space is enormous and entirely degenerate: "
        f"{nondeg_total} non-degenerate pairs over {len(functor_rows)} cells")

    # the two routes for the functor count: the formula against brute force
    def tiny_measure(name, p, npts, n_dih):
        """One validation cell: the formula against an exhaustive brute force
        over EVERY function from the source carrier to the target carrier."""
        gen = tiny_generator(name, npts, p)
        s_ar = make_cyclic_arena(p, npts, gen)
        els, mul, e = dihedral_abstract(n_dih)
        idx = {g: i for i, g in enumerate(els)}
        Gt = [tuple(idx[mul(g, h)] for h in els) for g in els]
        t_ar = make_perm_arena(sorted(Gt), len(els))
        imgs = homs_route_a(p, els, mul, e)
        n_orb = len(orbits_unionfind([gen], npts))
        formula = sum(equivariant_map_count(t_ar["npts"], n_orb) for _g in imgs)
        brute = brute_nd = 0
        for phi_img in range(len(t_ar["els"])):
            phi = [0] * p
            cur = t_ar["e"]
            for j in range(p):
                phi[j] = cur
                cur = t_ar["mul"](cur, phi_img)
            if t_ar["mul"](phi[p - 1], phi_img) != t_ar["e"]:
                continue
            for Phi in itertools.product(range(t_ar["npts"]), repeat=npts):
                r = evaluate_candidate(s_ar, t_ar, phi, list(Phi))
                if r["SP"]:
                    brute += 1
                    if r["accepted"]:
                        brute_nd += 1
        return {"cell": name, "p": p, "source_points": npts,
                "target_points": t_ar["npts"],
                "source_generator_order": porder(gen),
                "the_declared_group_acts": perm_pow(gen, p) == pident(npts),
                "orbits": n_orb, "group_maps": len(imgs), "formula": formula,
                "brute_force": brute, "non_degenerate_brute": brute_nd}

    tiny_rows = [tiny_measure(*spec) for spec in
                 tiny_cell_specs([("TINY-A", 2, 4, 2), ("TINY-B", 3, 3, 3),
                                  ("TINY-C", 5, 5, 2)])]
    tiny_ok = all(r["formula"] == r["brute_force"] for r in tiny_rows)
    acts_ok = all(r["the_declared_group_acts"] for r in tiny_rows)
    exponents = sorted({r["orbits"] for r in tiny_rows})
    g18 = gate("G18", "THE EQUIVARIANT-MAP COUNT IS COMPUTED BY TWO INDEPENDENT "
               "ROUTES: the orbit-representative formula, and an EXHAUSTIVE "
               "brute-force enumeration of every function from the source carrier "
               "to the target carrier filtered by the very predicate the census "
               "uses, at declared tiny cells that include a cell with non-trivial "
               "group maps and a cell with none, that are cell-complete against "
               "the declaration, whose source generators are measured to satisfy "
               "gen^p = identity (so the declared group really acts), and whose "
               "ORBIT EXPONENTS include a value above 1 -- the exponent is what "
               "the formula asserts",
               tiny_ok and acts_ok
               and len(tiny_rows) == len(DECL["tiny_cells"])
               and any(r["non_degenerate_brute"] > 0 for r in tiny_rows)
               and any(r["non_degenerate_brute"] == 0 for r in tiny_rows)
               and max(exponents) > 1,
               {"tiny_cells": tiny_rows,
                "declared_tiny_cells": len(DECL["tiny_cells"]),
                "orbit_exponents_exercised": exponents,
                "every_declared_group_acts": acts_ok})
    report("G18", g18, "; ".join(f"{r['cell']}: formula {r['formula']} = brute "
                                 f"{r['brute_force']} (nd {r['non_degenerate_brute']}, "
                                 f"orbits {r['orbits']})" for r in tiny_rows))
    # the formula's HYPOTHESIS, as a negative control: a cell whose declared
    # group does not act must break the formula, and the brute force must catch
    # it.  This is the control that makes the three passing cells mean something.
    neg = tiny_measure("TINY-NEG", 2, 3, 3)
    g42 = gate("G42", "THE COUNT FORMULA'S HYPOTHESIS IS MEASURED, NOT ASSUMED: "
               "at a declared negative-control cell whose source generator's "
               "order does NOT divide the declared prime -- so the declared group "
               "does not act -- the orbit-representative formula and the "
               "exhaustive brute force DISAGREE, and the disagreement is measured "
               "here; every cell of the validation set is measured to satisfy the "
               "hypothesis the formula needs, and the committed census's own "
               "source action is measured free at every cell",
               neg["formula"] != neg["brute_force"]
               and not neg["the_declared_group_acts"] and acts_ok,
               {"negative_control": neg,
                "the_formula_needs": "a genuine free Z/p action on the source",
                "validation_cells_satisfying_the_hypothesis": acts_ok})
    report("G42", g42, f"TINY-NEG (generator of order "
           f"{neg['source_generator_order']} against p = {neg['p']}): formula "
           f"{neg['formula']} vs brute force {neg['brute_force']} -- the "
           f"hypothesis bites")
    say("")

    # ==================== 11. THE ENCODING DICTIONARY (F1) ===================
    say("--- 11. THE PIN's DECLARED LEAD: THE RECORD <-> COMPLETION DICTIONARY ---")
    progress("dictionary census")
    recs = dictionary_records()
    dict_cells = 0
    admissible_by_prime: dict = {}
    for p in primes:
        adm_per_record = []
        for _r in recs:
            adm = 0
            for o, cnt in sorted(ord_spec.items()):
                els, mul, e = dihedral_abstract(o)
                if len(homs_route_a(p, els, mul, e)) > 1:
                    adm += cnt
                dict_cells += 1
            adm_per_record.append(adm)
        total = 1
        for a in adm_per_record:
            total *= a
        admissible_by_prime[p] = {"per_record": adm_per_record,
                                  "dictionaries": total,
                                  "digits": len(str(total))}
    space_size = len(fam) ** len(recs)
    g19 = gate("G19", "THE DICTIONARY CENSUS IS SWEPT AT A DECLARED FINITE SCOPE "
               "WITH ITS SIZE COMPUTED: the space of record->completion "
               "dictionaries is |family|^|records|, computed by exponentiation "
               "from the two measured set sizes, and the admissible count is a "
               "PRODUCT over the records of per-record counts, each obtained by "
               "sweeping the whole defect order spectrum -- never one expression",
               len(recs) == 9 and dict_cells == len(primes) * len(recs)
               * len(ord_spec) and space_size == 40320 ** 9,
               {"records": len(recs), "family": len(fam),
                "space_size_digits": len(str(space_size)),
                "spectrum_cells_swept": dict_cells,
                "admissible": {str(k): v for k, v in
                               sorted(admissible_by_prime.items())}})
    report("G19", g19, f"{len(recs)} records x {len(fam)} completions; space has "
           f"{len(str(space_size))} digits; {dict_cells} spectrum cells swept")
    for p in primes:
        a = admissible_by_prime[p]
        say(f"        p = {p:<3d} admissible completions per record "
            f"{a['per_record'][0]:<6d} -> dictionaries {a['dictionaries']} "
            f"({a['digits']} digits)")
    committed_adm = {}
    n_committed = committed_scope_defect_order()
    for p in primes:
        els, mul, e = dihedral_abstract(n_committed)
        committed_adm[p] = len(homs_route_a(p, els, mul, e)) - 1
    g20 = gate("G20", "AT THE COMMITTED SCOPE THE DICTIONARY CENSUS IS EMPTY BY "
               "A COMPUTED PRODUCT: when the dictionary's image is restricted to "
               "the committed completions, the per-record admissible count is "
               "ZERO at every declared prime, so the product over the nine "
               "records is zero and no dictionary survives",
               all(v == 0 for v in committed_adm.values()),
               {"the_committed_completions_defect_order": n_committed,
                "per_record_admissible_at_the_committed_completion":
                {str(k): v for k, v in sorted(committed_adm.items())}})
    report("G20", g20, f"committed-scope admissible per record: "
           f"{sorted(set(committed_adm.values()))}")
    say("")

    # ==================== 12. REACHABILITY AND THE HELD-OUT SET ==============
    say("--- 12. BOTH OUTCOMES REACHABLE, AND THE HELD-OUT VERIFICATION ---")
    progress("reachability")
    # SYN-FOUND: a declared synthetic compatible pair
    p_syn = 3
    n_syn = synthetic_found_target_order(porder(DT9))
    syn_src_n = p_syn ** 4
    r_syn = (1, 1)
    gen_syn = []
    for i in range(syn_src_n):
        m1 = i % p_syn
        m0 = (i // p_syn) % p_syn
        rest = i // (p_syn * p_syn)
        gen_syn.append(rest * p_syn * p_syn + ((m0 + r_syn[0]) % p_syn) * p_syn
                       + ((m1 + r_syn[1]) % p_syn))
    syn_src = make_cyclic_arena(p_syn, syn_src_n, gen_syn)
    Dsyn = DT81 if n_syn == porder(DT9) else tensor(gen_defect(Q_decl, 3), pident(9))
    Gsyn = closure([tuple(W81), tuple(Dsyn)], 81)
    syn_tgt = make_perm_arena(Gsyn, 81)
    syn_idx = {g: i for i, g in enumerate(Gsyn)}
    D_el = syn_idx[tuple(Dsyn)]
    W_el = syn_idx[tuple(W81)]
    els_s, mul_s, e_s = syn_tgt["els"], syn_tgt["mul"], syn_tgt["e"]
    syn_homs = homs_route_a(p_syn, els_s, mul_s, e_s)
    syn_nontriv = [g for g in syn_homs if g != e_s]
    # the source orbits, ordered lexicographically by their minimal element
    orbs = orbits_unionfind([gen_syn], syn_src_n)
    fit = fit_orbit_indices(len(orbs))
    held = [i for i in range(len(orbs)) if i not in set(fit)]
    # the target base point: the lexicographically first point on a free D-orbit
    n_rot = porder(Dsyn)
    y0 = None
    for y in range(81):
        if len({syn_tgt["act"](_pow_el(D_el, j, mul_s, e_s), y)
                for j in range(n_rot)}) == n_rot:
            y0 = y
            break
    heldout_rows = []
    for kind in ("E-ROT", "E-REF"):
        Phi = [0] * syn_src_n
        touched = set()
        for oi, orb in enumerate(orbs):
            rep = orb[0]
            # decode the source symmetry (front translation delta, transverse
            # register shift c) that carries orbit 0's representative to rep
            m1 = rep % p_syn
            m0 = (rep // p_syn) % p_syn
            rest = rep // (p_syn * p_syn)
            delta = (rest // p_syn, rest % p_syn)
            c = (m0 - m1) % p_syn
            el = extension_assignment(kind, delta, c, W_el, D_el, n_rot)
            t = _pow_el(D_el, el[0], mul_s, e_s)
            if el[1]:
                t = mul_s(W_el, t)
            for j in range(p_syn):
                x = syn_src["act"](j, rep)
                # the declared extension acts on the LEFT of the fitted orbit's
                # value: Phi(T_delta S^c y) = tau(delta,c) . Phi(y)
                Phi[x] = syn_tgt["act"](mul_s(t, _pow_el(D_el, j, mul_s, e_s)), y0)
                if oi in set(fit):
                    touched.add(x)
        phi_syn = [_pow_el(D_el, j, mul_s, e_s) for j in range(p_syn)]
        # the held-out verification: equivariance on the HELD orbits only
        bad = tot = 0
        for oi in held:
            for x in orbs[oi]:
                for g in range(p_syn):
                    tot += 1
                    if Phi[syn_src["act"](g, x)] != syn_tgt["act"](phi_syn[g], Phi[x]):
                        bad += 1
        full = evaluate_candidate(syn_src, syn_tgt, phi_syn, Phi)
        heldout_rows.append({"extension": kind, "held_out_cells": tot,
                             "held_out_violations": bad,
                             "accepted_by_the_census": full["accepted"],
                             "fit_points": len(touched)})
    rot = heldout_rows[0]
    ref = heldout_rows[1]
    g21 = gate("G21", "BRG-MORPHISM-FOUND IS REACHABLE, AND ITS HELD-OUT "
               "VERIFICATION IS PREDICTIVE: at the declared synthetic compatible "
               "pair the census returns non-trivial group maps and the "
               "constructed carrier morphism is ACCEPTED; the morphism is fitted "
               "on the declared FIT orbit alone and extended by the declared "
               "source symmetry, and its equivariance is then verified on every "
               "HELD orbit -- equations the construction never imposed",
               len(syn_nontriv) > 0 and rot["accepted_by_the_census"]
               and rot["held_out_violations"] == 0 and rot["held_out_cells"] > 0
               and len(held) > 0,
               {"synthetic_prime": p_syn, "target_group_order": len(Gsyn),
                "non_trivial_group_maps": len(syn_nontriv),
                "orbits": len(orbs), "fit_orbits": len(fit),
                "held_out_orbits": len(held),
                "held_out_cells": rot["held_out_cells"],
                "held_out_violations": rot["held_out_violations"],
                "fit_points_touched": rot["fit_points"]})
    report("G21", g21, f"{len(syn_nontriv)} non-trivial group maps; morphism "
           f"accepted; held-out {rot['held_out_cells']} cells, "
           f"{rot['held_out_violations']} violations")
    g22 = gate("G22", "THE HELD-OUT VERIFICATION HAS TEETH: the SAME construction "
               "with the declared reflection-valued extension FAILS the held-out "
               "check at a measured, nonzero number of cells, while the "
               "rotation-valued extension passes at every one -- so the held-out "
               "gate can fail, and passing it is a measurement",
               ref["held_out_violations"] > 0 and rot["held_out_violations"] == 0
               and not ref["accepted_by_the_census"],
               {"E-ROT": rot, "E-REF": ref})
    report("G22", g22, f"E-REF fails at {ref['held_out_violations']} of "
           f"{ref['held_out_cells']} held-out cells; E-ROT at "
           f"{rot['held_out_violations']}")
    g23 = gate("G23", "THE HELD-OUT SET IS PURE: the construction touched only "
               "the declared FIT orbit, the HELD orbits were declared before any "
               "morphism was constructed, and the two sets partition the source "
               "orbits with computed sizes",
               rot["fit_points"] == len(fit) * p_syn
               and len(fit) + len(held) == len(orbs) and len(fit) == 1,
               {"orbits": len(orbs), "fit": len(fit), "held": len(held),
                "fit_points_touched": rot["fit_points"]})
    report("G23", g23, f"FIT {len(fit)} orbit / HELD {len(held)} orbits of "
           f"{len(orbs)}; {rot['fit_points']} points touched")
    # the declared held-out QUANTITIES, transported
    h1_src = sorted({len(o) for o in orbs})
    img_gen = heldout_image_generator(D_el, W_el)
    img_orbits = orbits_unionfind([[syn_tgt["act"](img_gen, x) for x in range(81)]], 81)
    h1_tgt = sorted({len(o) for o in img_orbits if len(o) > 1})
    h2 = (pfixed(gen_syn), pfixed(Dsyn))
    h3_src = sorted({p_syn, 1})
    h3_tgt = group_element_orders(els_s, mul_s, e_s)
    h4_cells = p_syn * p_syn
    h4_bad = sum(1 for a in range(p_syn) for b in range(p_syn)
                 if phi_syn[(a + b) % p_syn] != mul_s(phi_syn[a], phi_syn[b]))
    g24 = gate("G24", "THE DECLARED HELD-OUT QUANTITIES TRANSPORT: the orbit-size "
               "multiset, the generators' fixed-point counts, the element-order "
               "multisets and the whole source composition table are computed on "
               "both sides and the morphism carries each of them correctly",
               h1_src == h1_tgt and h4_bad == 0 and p_syn in h3_tgt
               and h4_cells == p_syn ** 2,
               {"H1_source_orbit_sizes": h1_src, "H1_image_orbit_sizes": h1_tgt,
                "H2_generator_fixed_points": list(h2),
                "H3_source_element_orders": h3_src,
                "H3_target_element_orders": h3_tgt,
                "H4_composition_cells": h4_cells, "H4_violations": h4_bad})
    report("G24", g24, f"H1 {h1_src} = {h1_tgt}; H3 {h3_src} into {h3_tgt}; "
           f"H4 {h4_cells} cells, {h4_bad} violations")
    # SYN-EMPTY
    p_emp = synthetic_empty_source_prime(5)
    emp_src_n = p_emp ** 4
    r_emp = (1, 1)
    gen_emp = []
    for i in range(emp_src_n):
        m1 = i % p_emp
        m0 = (i // p_emp) % p_emp
        rest = i // (p_emp * p_emp)
        gen_emp.append(rest * p_emp * p_emp + ((m0 + r_emp[0]) % p_emp) * p_emp
                       + ((m1 + r_emp[1]) % p_emp))
    emp_src = make_cyclic_arena(p_emp, emp_src_n, gen_emp)
    emp_homs = homs_route_a(p_emp, els_s, mul_s, e_s)
    emp_nontriv = [g for g in emp_homs if g != e_s]
    g25 = gate("G25", "BRG-EMPTY-AT-CARRIER IS REACHABLE BY THE SAME MACHINERY: "
               "at the declared synthetic incompatible pair the census returns "
               "NO non-trivial group map, so the census's other value is "
               "attainable and neither outcome is a predicate that cannot fail",
               len(emp_nontriv) == 0 and len(emp_homs) == 1,
               {"synthetic_prime": p_emp, "target_group_order": len(Gsyn),
                "group_maps": len(emp_homs),
                "non_trivial_group_maps": len(emp_nontriv)})
    report("G25", g25, f"p = {p_emp} against |G| = {len(Gsyn)}: "
           f"{len(emp_nontriv)} non-trivial group maps")
    say("")

    # ==================== 13. THE OBSTRUCTION ===============================
    say("--- 13. THE OBSTRUCTION, NAMED AND GATED ---")
    all_cells = cells1 + cells2
    coprime_iff_empty = all(
        (c["gcd_p_group_order"] == 1) == (c["nontrivial_forward"] == 0)
        for c in all_cells)
    empty_cells = sum(1 for c in all_cells if c["nontrivial_forward"] == 0)
    live_cells = sum(1 for c in all_cells if c["nontrivial_forward"] > 0)
    name = obstruction_name(coprime_iff_empty)
    g26 = gate("G26", "THE FORWARD OBSTRUCTION IS NAMED, AND IT IS MEASURED "
               "COEXTENSIVE WITH THE FORWARD CENSUS'S EMPTINESS IN BOTH "
               "DIRECTIONS OF THE EQUIVALENCE: over every cell of every declared "
               "scope, the forward census is empty EXACTLY where "
               "gcd(p, |<W,D>|) = 1 -- so the named forward obstruction is order-"
               "coprimality (a prime source group and a transport group whose "
               "order 2*ord(D) is not divisible by it), and the naming is "
               "falsifiable because cells of both kinds occur.  This is a "
               "statement about the FORWARD census only; the reverse census has "
               "its own, different obstruction (G34)",
               coprime_iff_empty and name == "order-coprimality"
               and empty_cells > 0 and live_cells > 0,
               {"cells": len(all_cells), "empty_cells": empty_cells,
                "live_cells": live_cells, "obstruction": name,
                "the_forward_equivalence_holds_in_both_directions":
                    coprime_iff_empty})
    report("G26", g26, f"{empty_cells} empty / {live_cells} live of "
           f"{len(all_cells)} cells (forward); obstruction '{name}'")
    ab_orders = sorted({c["abelianisation_order"] for c in all_cells})
    ab_two_group = all(_is_power_of_two(a) for a in ab_orders)
    rev_empty = all(c["nontrivial_reverse"] == 0 for c in all_cells)
    g27 = gate("G27", "THE REVERSE DIRECTION IS EMPTY EVERYWHERE, AND ITS "
               "OBSTRUCTION IS A SECOND, PRIME-INDEPENDENT ONE: every "
               "homomorphism from a transport group to Z/p kills the commutator "
               "subgroup, and the abelianisation is measured to be a 2-group at "
               "every instance of every scope, so for every ODD declared prime "
               "the reverse census is trivial -- with no dependence on the prime "
               "at all",
               rev_empty and ab_two_group,
               {"abelianisation_orders": ab_orders,
                "all_abelianisations_are_2_groups": ab_two_group,
                "cells": len(all_cells)})
    report("G27", g27, f"reverse empty at all {len(all_cells)} cells; "
           f"abelianisation orders {ab_orders}")

    # ---- THE SECOND OBSTRUCTION, AS A FIRST-CLASS RESULT ------------------
    live_rows = [c for c in all_cells if c["nontrivial_forward"] > 0]
    live_rev_empty = all(c["nontrivial_reverse"] == 0 for c in live_rows)
    rev_coextensive = all((c["gcd_p_group_order"] == 1)
                          == (c["nontrivial_reverse"] == 0) for c in all_cells)
    rev_mismatches = sum(1 for c in all_cells
                         if (c["gcd_p_group_order"] == 1)
                         != (c["nontrivial_reverse"] == 0))
    g34 = gate("G34", "THE SECOND OBSTRUCTION, NAMED BESIDE THE FIRST: THE "
               "REVERSE CENSUS IS EMPTY AT EVERY ONE OF THE DECLARED CELLS -- "
               "INCLUDING THE LIVE ONES.  Where the forward census is non-trivial "
               "the reverse census is still zero, so the reverse emptiness is NOT "
               "coextensive with order-coprimality: the mismatch is measured and "
               "nonzero, and the reverse obstruction is the 2-group "
               "abelianisation, which does not mention the prime.  MEASURED "
               "CONSEQUENCE: at every declared cell the structure-preserving maps "
               "run in ONE direction only, deformation -> transport, so 'built "
               "FROM' could at most mean embedding as a sub-object, and that only "
               "where a forward morphism exists at all",
               rev_empty and live_rev_empty and live_cells > 0
               and (not rev_coextensive) and rev_mismatches == live_cells,
               {"cells": len(all_cells),
                "reverse_non_trivial_total":
                    sum(c["nontrivial_reverse"] for c in all_cells),
                "live_forward_cells": live_cells,
                "reverse_non_trivial_at_the_live_cells":
                    sum(c["nontrivial_reverse"] for c in live_rows),
                "the_live_cells": [[c["p"], c["instance"],
                                    c["nontrivial_forward"],
                                    c["nontrivial_reverse"]] for c in live_rows],
                "reverse_emptiness_is_coextensive_with_coprimality":
                    rev_coextensive,
                "cells_where_the_reverse_reading_would_fail": rev_mismatches,
                "the_reverse_obstruction": "the 2-group abelianisation "
                                           "(prime-independent)"})
    report("G34", g34, f"reverse non-trivial 0 at all {len(all_cells)} cells "
           f"including the {live_cells} live ones; reverse emptiness NOT "
           f"coextensive with coprimality ({rev_mismatches} cells)")

    # ---- THE RADICAL, COMPUTED (never typed) -------------------------------
    inst_orders = radical_instance_orders(rows1)
    rad_by_instance = {}
    for (nm, _c, n, _o, _r) in rows1:
        rad_by_instance[nm] = prime_radical(2 * n)
    rad_union = sorted({q for n in inst_orders for q in prime_radical(2 * n)})
    rad_no_T = sorted({q for (nm, _c, n, _o, _r) in rows1 if nm != "base T"
                       for q in prime_radical(2 * n)})
    with_2 = sum(1 for r in rad_by_instance.values() if 2 in r)
    with_3 = sum(1 for r in rad_by_instance.values() if 3 in r)
    max_ord_committed = max(n for (_nm, _c, n, _o, _r) in rows1)
    g32 = gate("G32", "THE TWO SETS ARE BOTH COMPUTED, AND THEIR EQUALITY IS "
               "GATED (RUNBOOK 4: counts computed, never typed): the primes "
               "dividing 2*ord(D) at the committed instances are obtained by "
               "trial division over the measured defect orders, the primes at "
               "which the deformation side's exact residual fails to reduce are "
               "obtained by testing the denominator, and the two sets are "
               "compared here.  THE COINCIDENCE HAS ONE DEGREE OF FREEDOM, "
               "MEASURED: the prime 2 divides 2*ord(D) at every instance by the "
               "dihedral form, and the prime 3 enters from ONE instance alone -- "
               "delete it and the union is {2}, while the inclusion in {2,3} "
               "survives",
               rad_union == nonreducible and with_2 == len(rad_by_instance)
               and with_3 == 1 and rad_no_T == [2]
               and set(rad_union) <= {2, 3},
               {"radical_by_instance": rad_by_instance,
                "the_union_over_the_committed_instances": rad_union,
                "the_primes_at_which_rho_fails_to_reduce": nonreducible,
                "instances_whose_radical_contains_2": with_2,
                "instances_whose_radical_contains_3": with_3,
                "the_union_without_that_one_instance": rad_no_T,
                "the_largest_committed_defect_order": max_ord_committed,
                "instances": len(rad_by_instance)})
    report("G32", g32, f"primes dividing 2*ord(D) at the committed instances "
           f"{rad_union} (computed) = primes where rho fails to reduce "
           f"{nonreducible}; 2 at {with_2}/{len(rad_by_instance)} instances, "
           f"3 at {with_3}; without that instance {rad_no_T}")

    # ---- THE THEOREM: LAGRANGE + CAUCHY, NO DIHEDRAL HYPOTHESIS ------------
    zoo_builders = {}
    for n in range(1, 8):
        zoo_builders[f"Z/{n}"] = ("cyclic", n)
        zoo_builders[f"D_{n}"] = ("dihedral", n)
    for nm, spec in (("S_3", ("symmetric", 3)), ("S_4", ("symmetric", 4)),
                     ("A_4", ("alternating", 4)),
                     ("A_4 x Z/2", ("product-alt-cyclic", (4, 2))),
                     ("Z/2 x Z/2", ("product-cyclic", (2, 2))),
                     ("Z/2 x Z/3", ("product-cyclic", (2, 3))),
                     ("D_4 x Z/3", ("product-dihedral-cyclic", (4, 3)))):
        zoo_builders[nm] = spec
    zoo = declared_group_zoo(zoo_builders)
    zoo_cells = 0
    zoo_fail = 0
    order_reading_cells = 0
    order_reading_fail = 0
    zoo_rows = []
    for gname in sorted(zoo):
        G, npts = _build_zoo_group(zoo[gname])
        orders = [porder(list(g)) for g in G]
        nonabelian = any(pmul(list(a), list(b)) != pmul(list(b), list(a))
                         for a in G for b in G)
        for q in sorted(set(primes) | {2, 3}):
            zoo_cells += 1
            has_p = any(o == q for o in orders)
            lagrange = (len(G) % q == 0)
            if has_p != lagrange:
                zoo_fail += 1
            # the SAME criterion read through 2*ord(D) instead of |G|: this is
            # the reading that needs the dihedral form, and off that family it
            # is measured to fail
            if not gname.startswith("D_"):
                order_reading_cells += 1
                if has_p != ((2 * max(orders)) % q == 0):
                    order_reading_fail += 1
        zoo_rows.append({"group": gname, "order": len(G),
                         "nonabelian": nonabelian,
                         "element_orders": sorted(set(orders))})
    g33 = gate("G33", "THE OBSTRUCTION THEOREM IS LAGRANGE + CAUCHY, WITH NO "
               "DIHEDRAL HYPOTHESIS: for a finite group G and a prime q, "
               "hom(Z/q, G) is trivial IFF q does not divide |G| -- Lagrange "
               "forward (an element of order q would generate a subgroup of "
               "order q), Cauchy back (q | |G| yields an element of order q).  "
               "Swept over a declared group zoo that is NOT only dihedral -- "
               "cyclic, dihedral, symmetric, alternating and direct products, "
               "abelian and non-abelian -- with zero failures.  THE GEOMETRIC "
               "CONTENT IS THEREFORE THE ORDER FORMULA |<W,D>| = 2*ord(D), NOT "
               "THE HOM COUNT: the same criterion read through 2*ord(D) instead "
               "of |G| is measured to FAIL off the dihedral family",
               zoo_fail == 0 and order_reading_fail > 0
               and len(zoo) > 8 and any(r["nonabelian"] for r in zoo_rows),
               {"groups": len(zoo), "group_times_prime_cells": zoo_cells,
                "failures_of_the_Lagrange_Cauchy_equivalence": zoo_fail,
                "non_dihedral_cells_tested_against_the_order_reading":
                    order_reading_cells,
                "failures_of_the_order_reading_off_the_dihedral_family":
                    order_reading_fail,
                "zoo": zoo_rows})
    report("G33", g33, f"Lagrange+Cauchy holds at {zoo_cells} group x prime "
           f"cells over {len(zoo)} groups, {zoo_fail} failures; the 2*ord(D) "
           f"reading fails at {order_reading_fail} of {order_reading_cells} "
           f"non-dihedral cells")

    # ---- THE ONE LAW: THE DIHEDRAL FORM IS FORCED, SO THE OBSTRUCTION IS A
    #      THEOREM ABOUT THE WHOLE ONE-LAW FAMILY --------------------------
    seed = ("BRG one-law family sweep: W an involution, u arbitrary, "
            "D = [W,u] = W u^-1 W u; the relation W D W = D^-1 and the order "
            "formula |<W,D>| = 2 ord(D)").encode("utf-8")
    stream = random_stream(seed, 200000)
    cur = [0]
    draws = DECL["one_law_sweep"]["draws"]
    rel_viol = ord_viol = w_in_D = 0
    orders_drawn = set()
    for t in range(draws):
        npt = 4 + (t % 5)
        Wr = one_law_exchange(npt, stream, cur)
        ur = stream_perm(npt, stream, cur)
        Dr = pmul(Wr, pmul(pinv(ur), pmul(Wr, ur)))
        if pmul(Wr, pmul(Dr, Wr)) != pinv(Dr):
            rel_viol += 1
        od = porder(Dr)
        orders_drawn.add(od)
        Dsub = set(closure([tuple(Dr)], npt))
        if tuple(Wr) in Dsub:
            w_in_D += 1
        elif len(closure([tuple(Wr), tuple(Dr)], npt)) != 2 * od:
            ord_viol += 1
    ctrl_draws = 200
    ctrl_viol = ctrl_tested = 0
    for t in range(ctrl_draws):
        npt = 4 + (t % 5)
        Wr = stream_perm(npt, stream, cur)
        if pmul(Wr, Wr) == pident(npt):
            continue
        ctrl_tested += 1
        ur = stream_perm(npt, stream, cur)
        Dr = pmul(Wr, pmul(pinv(ur), pmul(Wr, ur)))
        if pmul(Wr, pmul(Dr, Wr)) != pinv(Dr):
            ctrl_viol += 1
    g35 = gate("G35", "THE OBSTRUCTION IS A THEOREM ABOUT THE ONE-LAW FAMILY, "
               "NOT ABOUT EIGHT MEASURED COINCIDENCES.  Given only the one law's "
               "two ingredients -- W^2 = 1 and D = [W,u] -- the relation "
               "W D W = D^-1 is forced by algebra: W(W u^-1 W u)W = u^-1 W u W = "
               "(W u^-1 W u)^-1.  Hence <W,D> is dihedral of order 2*ord(D) "
               "whenever W is not a power of D, and the forward obstruction "
               "holds for EVERY base the law covers, including bases the corpus "
               "has not built.  Measured over a randomised family sweep whose "
               "seed is the sha256 of declared data alone, with a control in "
               "which W is NOT an involution and the relation must fail",
               rel_viol == 0 and ord_viol == 0 and len(orders_drawn) > 1
               and ctrl_viol > 0 and ctrl_tested > 0,
               {"draws": draws, "points": "4 to 8",
                "violations_of_W_D_W_equals_D_inverse": rel_viol,
                "violations_of_the_order_formula": ord_viol,
                "draws_where_W_is_a_power_of_D": w_in_D,
                "defect_orders_drawn": sorted(orders_drawn),
                "control_draws_with_a_non_involutive_W": ctrl_tested,
                "control_violations_of_the_relation": ctrl_viol,
                "the_only_contingent_content": "ord(D) <= "
                                               f"{max_ord_committed} at the "
                                               "committed instances",
                "seed": DECL["one_law_sweep"]["seed"]})
    report("G35", g35, f"W D W = D^-1 at {draws} of {draws} randomised pairs "
           f"({rel_viol} violations); |<W,D>| = 2 ord(D) at all of them "
           f"({ord_viol} violations); the non-involutive control fails at "
           f"{ctrl_viol} of {ctrl_tested}")
    say("        The two obstructions, stated at their measured strength:")
    say("          forward  hom(Z/p, <W,D>) is trivial iff p does not divide")
    say("                   2*ord(D) -- Lagrange one way, Cauchy the other, for")
    say("                   ANY finite group of that order; the geometric content")
    say("                   is the order formula |<W,D>| = 2*ord(D), which the one")
    say("                   law forces.  The only contingent content is that")
    say(f"                   ord(D) is at most {max_ord_committed} at the committed")
    say(f"                   instances, so 2*ord(D) is in "
        f"{sorted({2 * c['ord_D'] for c in cells1})} and no declared prime")
    say("                   divides any of them.")
    say("          reverse  every hom <W,D> -> Z/p factors through a 2-group, so")
    say(f"                   the reverse census is empty at all {len(all_cells)} cells --")
    say(f"                   including the {live_cells} where the forward census is not.")
    say(f"                   The maps run in one direction only.")
    say(f"        The primes dividing 2*ord(D) at the committed instances are")
    say(f"        {rad_union} (computed), and rho fails to reduce at exactly "
        f"{nonreducible}.")
    say("        AT THE COMMITTED INSTANCES -- AND ONLY THERE -- the deformation")
    say("        side cannot be built at the primes at which the match would be")
    say("        possible.  At the twelve rebuilt classes this fails: the primes")
    say(f"        dividing 2*ord(D) there include "
        f"{sorted({q for (_k, _c, n, _o, _r) in class_rows for q in prime_radical(2 * n)})},")
    say("        of which 5 and 7 are admissible on the deformation side.")
    say("")

    # ============ 13b. THE ADMISSIBLE-PRIME CELLS, AT THE DELIVERED =========
    #                   STANDARD, WITH THE HELD-OUT PROTOCOL RUN ON THEM
    say("--- 13b. THE ADMISSIBLE-PRIME CELLS: THE FULL DELIVERED PREDICATE AND "
        "THE HELD-OUT PROTOCOL, RUN ---")
    progress("admissible-prime cells")
    found_rows = []
    for c in cells2:
        if c["nontrivial_forward"] == 0:
            continue
        p, key, n = c["p"], c["instance"], c["ord_D"]
        dd = class_defect[key]
        Gc = closure([tuple(W81), tuple(tensor(dd, pident(9)))], 81)
        tgt = make_perm_arena(Gc, 81)
        mulc, ec = tgt["mul"], tgt["e"]
        D_c = Gc.index(tuple(tensor(dd, pident(9))))
        t_el = _pow_el(D_c, live_cell_generator_exponent(n, p), mulc, ec)
        src_c, gen_c = ha_arena(p, rho_mod_p(rho, p))
        orbs_c = orbits_unionfind([gen_c], src_c["npts"])
        y0c = None
        for y in range(81):
            if len({tgt["act"](_pow_el(t_el, j, mulc, ec), y)
                    for j in range(p)}) == p:
                y0c = y
                break
        Phi_c = [0] * src_c["npts"]
        touched_c = set()
        for oi, orb in enumerate(orbs_c):
            rep = orb[0]
            m1 = rep % p
            m0 = (rep // p) % p
            rest = rep // (p * p)
            delta = (rest // p, rest % p)
            cc = (m0 - m1) % p
            tau = _pow_el(D_c, (delta[0] + 2 * delta[1] + cc) % n, mulc, ec)
            for j in range(p):
                x = src_c["act"](j, rep)
                Phi_c[x] = tgt["act"](mulc(tau, _pow_el(t_el, j, mulc, ec)), y0c)
                if oi == 0:
                    touched_c.add(x)
        phi_c = [_pow_el(t_el, j, mulc, ec) for j in range(p)]
        full_c = evaluate_candidate(src_c, tgt, phi_c, Phi_c)
        bad_c = tot_c = 0
        for oi in range(1, len(orbs_c)):
            for x in orbs_c[oi]:
                for g in range(p):
                    tot_c += 1
                    if Phi_c[src_c["act"](g, x)] != tgt["act"](phi_c[g], Phi_c[x]):
                        bad_c += 1
        fix_t = sum(1 for y in range(81) if tgt["act"](t_el, y) == y)
        nd_pairs = c["nontrivial_forward"] * (81 ** len(orbs_c) - fix_t)
        found_rows.append({
            "p": p, "class": key, "ord_D": n, "group_order": len(Gc),
            "group_map_order": _el_order(t_el, mulc, ec),
            "SP1_cells": full_c["sp1_cells"], "SP1_violations": full_c["sp1_bad"],
            "SP2": full_c["SP2"],
            "SP3_cells": full_c["sp3_cells"], "SP3_violations": full_c["sp3_bad"],
            "NT1": full_c["NT1"], "NT2": full_c["NT2"],
            "accepted_by_the_full_delivered_predicate": full_c["accepted"],
            "source_orbits": len(orbs_c), "fit_orbits": 1,
            "fit_points_touched": len(touched_c),
            "held_out_cells": tot_c, "held_out_violations": bad_c,
            "fixed_points_of_the_group_maps_image": fix_t,
            "non_degenerate_pairs_digits": len(str(nd_pairs))})
    found_ok = (len(found_rows) > 0
                and all(r["accepted_by_the_full_delivered_predicate"]
                        and r["held_out_violations"] == 0
                        and r["held_out_cells"] > 0
                        and r["fit_points_touched"] == r["p"]
                        and r["group_map_order"] == r["p"]
                        for r in found_rows))
    found_primes = sorted({r["p"] for r in found_rows})
    admissible_found = all(p in primes for p in found_primes)
    g36 = gate("G36", "FOUND-AT-DELIVERED-STANDARD-OUTSIDE-COMMITTED-SCOPE: at "
               "every live cell of the extended scope -- at DECLARED-ADMISSIBLE "
               "primes, on classes the transport side itself rebuilt -- an "
               "explicit pair (phi, Phi) is constructed and passes the FULL "
               "delivered predicate SP1, SP2, SP3, NT1, NT2 exhaustively, AND "
               "passes this unit's own held-out protocol: fitted on the declared "
               "FIT orbit alone, extended by the declared source symmetry, and "
               "verified on every HELD orbit with zero violations.  These cells "
               "are excluded from the verdict by the pin's requirement 4 -- "
               "because their existence is a function of the DECLARED reduction "
               "prime -- and by nothing else; the FOUND machinery is therefore "
               "exercised at admissible primes and not only at the synthetic pair",
               found_ok and admissible_found,
               {"cells": found_rows, "primes": found_primes,
                "every_prime_is_declared_admissible": admissible_found,
                "label": "FOUND-AT-DELIVERED-STANDARD-OUTSIDE-COMMITTED-SCOPE",
                "excluded_by": "pin requirement 4 (the prime is a declaration)"})
    report("G36", g36, "; ".join(
        f"p={r['p']} {r['class']}: SP3 {r['SP3_cells']} cells "
        f"{r['SP3_violations']} bad, held-out {r['held_out_cells']} cells "
        f"{r['held_out_violations']} violations, accepted "
        f"{r['accepted_by_the_full_delivered_predicate']}" for r in found_rows))
    for r in found_rows:
        say(f"        p = {r['p']:<3d} {r['class']:16s} |<W,D>| = "
            f"{r['group_order']:<3d} SP1 {r['SP1_cells']}/{r['SP1_violations']}  "
            f"SP3 {r['SP3_cells']}/{r['SP3_violations']}  held-out "
            f"{r['held_out_cells']}/{r['held_out_violations']}  fit points "
            f"{r['fit_points_touched']}  non-degenerate pairs "
            f"{r['non_degenerate_pairs_digits']} digits")

    # ---- WHAT THE DELIVERED STANDARD IS WORTH -----------------------------
    p_v = found_rows[0]["p"] if found_rows else primes[0]
    key_v = found_rows[0]["class"] if found_rows else None
    n_v = found_rows[0]["ord_D"] if found_rows else 1
    dd_v = class_defect[key_v]
    Gv = closure([tuple(W81), tuple(tensor(dd_v, pident(9)))], 81)
    tgt_v = make_perm_arena(Gv, 81)
    mulv, ev = tgt_v["mul"], tgt_v["e"]
    D_v = Gv.index(tuple(tensor(dd_v, pident(9))))
    t_v = _pow_el(D_v, n_v // p_v, mulv, ev)
    src_v, gen_v = ha_arena(p_v, rho_mod_p(rho, p_v))
    orbs_v = orbits_unionfind([gen_v], src_v["npts"])
    free_pts = [y for y in range(81)
                if len({tgt_v["act"](_pow_el(t_v, j, mulv, ev), y)
                        for j in range(p_v)}) == p_v]
    y_a, y_b = free_pts[0], free_pts[1]
    Phi_v = [0] * src_v["npts"]
    for oi, orb in enumerate(orbs_v):
        for j in range(p_v):
            sel, jj = collapse_orbit_image(oi, j)
            base = y_a if sel == 0 else y_b
            Phi_v[src_v["act"](j, orb[0])] = tgt_v["act"](
                _pow_el(t_v, jj, mulv, ev), base)
    phi_v = [_pow_el(t_v, j, mulv, ev) for j in range(p_v)]
    coll = evaluate_candidate(src_v, tgt_v, phi_v, Phi_v)
    collapsed_orbits = len(orbs_v) - 1
    g37 = gate("G37", "THE DELIVERED STANDARD IS WEAK AT THE FUNCTOR LAYER, "
               "MEASURED: because the source action is FREE, an equivariant "
               "carrier map is one free choice of image per orbit, so SP3 "
               "constrains nothing once phi is fixed, and NT2 asks only for two "
               "distinct images.  The example is built and evaluated here: a "
               "carrier map that sends every source orbit but one into a SINGLE "
               "target orbit satisfies the whole predicate and is ACCEPTED.  The "
               "consequence cuts both ways and both are recorded: the EMPTY "
               "verdict is correspondingly STRONG (the filter is as loose as it "
               "can be and the answer is still zero), and a live cell is "
               "correspondingly WEAK",
               coll["accepted"] and coll["SP"] and collapsed_orbits > 0
               and len(set(Phi_v)) > 1,
               {"prime": p_v, "class": key_v, "source_orbits": len(orbs_v),
                "orbits_sent_into_one_target_orbit": collapsed_orbits,
                "distinct_images": len(set(Phi_v)),
                "NT2_requires": "at least 2 distinct images",
                "accepted": coll["accepted"],
                "the_strengthened_standard": "REGISTERED at "
                                             "DECL.strengthened_standard, tested "
                                             "in NEITHER direction here"})
    report("G37", g37, f"at p = {p_v}, {collapsed_orbits} of {len(orbs_v)} "
           f"source orbits collapsed into one target orbit: accepted "
           f"{coll['accepted']} (NT2 asks for 2 distinct images; the map has "
           f"{len(set(Phi_v))})")
    say("")

    # ==================== 13c. THE OPENS, WITH THEIR NUMBERS ================
    say("--- 13c. THE REGISTERED OPENS, WITH THEIR MEASURED NUMBERS ---")
    progress("opens")
    bound = low_sector_bound()
    sector_low = sum(v for o, v in ord_spec.items() if o <= bound)
    live_orders = sorted(o for o in ord_spec
                         if any((2 * o) % q == 0 for q in primes))
    sector_live = sum(ord_spec[o] for o in live_orders)
    sector_other = fam_cells - sector_low - sector_live
    committed_low = sum(1 for (_nm, _c, n, _o, _r) in rows1 if n <= bound)
    committed_live = sum(1 for (_nm, _c, n, _o, _r) in rows1
                         if any((2 * n) % q == 0 for q in primes))
    g38 = gate("G38", "THE SECTOR CONCENTRATION IS MEASURED, AND REGISTERED AS AN "
               "OPEN: the declared completion family is MAJORITY-LIVE -- more of "
               "it admits some declared prime than does not -- while every "
               "committed instance sits in the low-defect-order band.  Both "
               "counts are computed from the swept family and the measured "
               "instance table, the three sectors are measured to partition the "
               "family, and the question 'why do the prepared bases concentrate "
               "in the closed sector' is registered as OPEN-2",
               sector_low + sector_live + sector_other == fam_cells
               and committed_low == len(rows1) and committed_live == 0
               and sector_live > sector_low and sector_live * 2 > fam_cells,
               {"family_members": fam_cells,
                "the_low_defect_order_band": f"ord(D) <= {bound}",
                "members_in_the_low_band": sector_low,
                "members_admitting_some_declared_prime": sector_live,
                "the_orders_that_admit_one": live_orders,
                "members_in_neither_sector": sector_other,
                "committed_instances": len(rows1),
                "committed_instances_in_the_low_band": committed_low,
                "committed_instances_admitting_some_declared_prime":
                    committed_live,
                "low_band_as_a_fraction": f"{sector_low}/{fam_cells}",
                "live_as_a_fraction": f"{sector_live}/{fam_cells}",
                "members_by_defect_order":
                    {str(k): v for k, v in sorted(ord_spec.items())},
                "the_fewest_labels_a_completion_of_each_defect_order_moves":
                    {str(k): v for k, v in sorted(min_support.items())},
                "OPEN-2": DECL["registered_opens"]["OPEN-2"]})
    report("G38", g38, f"family {fam_cells}: {sector_low} in the ord(D) <= "
           f"{bound} band, {sector_live} admitting some declared prime "
           f"(orders {live_orders}); committed instances {committed_low}/"
           f"{len(rows1)} in the band, {committed_live} admitting one")
    say(f"        members by defect order "
        f"{ {k: v for k, v in sorted(ord_spec.items())} }")
    say(f"        the fewest labels a completion of each defect order moves: "
        f"{ {k: v for k, v in sorted(min_support.items())} }")
    # the two-prime clause's arena dependence: forced at m = 3, contingent at
    # m = 4, with a witness
    def _landau(nn):
        best = {0: 1}
        for kk in range(1, nn + 1):
            nxt = dict(best)
            for used, val in best.items():
                if used + kk <= nn:
                    l = val * kk // _gcd(val, kk)
                    if nxt.get(used + kk, 0) < l:
                        nxt[used + kk] = l
            best = nxt
        return max(best.values())

    def _cycle_order(a):
        seen = [False] * len(a)
        o = 1
        for i in range(len(a)):
            if not seen[i]:
                j, ln = i, 0
                while not seen[j]:
                    seen[j] = True
                    j = a[j]
                    ln += 1
                o = o * ln // _gcd(o, ln)
        return o

    m_cont = contingency_arena_m()
    n_sample = DECL["species4_contingency"]["sample"]
    st4 = random_stream(("BRG contingency sweep in species 4's own arena: the "
                         "two-declared-prime clause").encode("utf-8"),
                        20 * n_sample + 4000)
    cur4 = [0]
    hits4 = 0
    witness4 = None
    spec4: dict = {}
    for _ in range(n_sample):
        tail = stream_perm(m_cont * m_cont - 1, st4, cur4)
        qq = [0] + [1 + x for x in tail]
        oo = _cycle_order(gen_defect(qq, m_cont))
        spec4[oo] = spec4.get(oo, 0) + 1
        if oo % two_prime_product == 0:
            hits4 += 1
            if witness4 is None:
                witness4 = qq
    max_m3 = max(ord_spec)
    g40 = gate("G40", "THE TWO-PRIME CLAUSE IS FORCED ONLY IN THE NINE-LABEL "
               "ARENA, MEASURED BOTH WAYS: over the whole nine-label family, "
               "exhaustively, no member has 2*ord(D) divisible by the smallest "
               "product of two declared primes -- the family's largest defect "
               "order is below the bound, and the Landau maximum for nine labels "
               "is computed here.  In species 4's own SIXTEEN-label arena, where "
               "the Landau maximum is far larger, a declared deterministic sample "
               "EXHIBITS completions whose defect order is divisible by that same "
               "product, with an explicit witness.  So G14's outcome is "
               "structural at m = 3 and CONTINGENT at m = 4, and species 4's own "
               "measured defect order is what carries it there",
               max_m3 * 2 < two_prime_product and hits4 > 0
               and witness4 is not None
               and _landau(m_cont * m_cont) > _landau(9),
               {"the_smallest_product_of_two_declared_primes":
                    two_prime_product,
                "the_nine_label_family_maximum_defect_order": max_m3,
                "nine_label_members_admitting_two_declared_primes": 0,
                "Landau_maximum_for_9_labels": _landau(9),
                "Landau_maximum_for_16_labels": _landau(16),
                "the_sampled_arena": f"m = {m_cont}, {m_cont * m_cont} labels",
                "sample_size": n_sample,
                "sampled_members_with_ord_D_divisible_by_the_product": hits4,
                "an_explicit_witness_completion": witness4,
                "its_defect_order": _cycle_order(gen_defect(witness4, m_cont))
                                    if witness4 else None,
                "the_sampled_order_spectrum":
                    {str(k): v for k, v in sorted(spec4.items())}})
    report("G40", g40, f"m = 3: max ord(D) {max_m3}, so 2*ord(D) never reaches "
           f"{two_prime_product} (Landau bound {_landau(9)}); m = {m_cont}: "
           f"{hits4} of {n_sample} sampled completions have ord(D) divisible by "
           f"{two_prime_product} (Landau bound {_landau(m_cont * m_cont)})")
    say("")

    # ============ 13d. DISCLOSURE-GRADE MEASUREMENTS (RUNBOOK 14 #208) ======
    say("--- 13d. DISCLOSURE-GRADE MEASUREMENTS: WHAT IS ANALYTICALLY FORCED ---")
    rule_rows = []
    for ri, rule in enumerate(DECL["extension_rules"]["rotation"]):
        for kind in ("E-ROT", "E-REF"):
            Phi_r = [0] * syn_src_n
            for oi, orb in enumerate(orbs):
                rep = orb[0]
                m1 = rep % p_syn
                m0 = (rep // p_syn) % p_syn
                rest = rep // (p_syn * p_syn)
                delta = (rest // p_syn, rest % p_syn)
                cc = (m0 - m1) % p_syn
                rr = [(delta[0] + 2 * delta[1] + cc), 0,
                      (2 * delta[0] + delta[1] + 2 * cc), delta[0],
                      (7 * delta[0] + 5 * cc)][ri] % n_rot
                tt = _pow_el(D_el, rr, mul_s, e_s)
                if kind == "E-REF" and delta[0] % 2:
                    tt = mul_s(W_el, tt)
                for j in range(p_syn):
                    x = syn_src["act"](j, rep)
                    Phi_r[x] = syn_tgt["act"](
                        mul_s(tt, _pow_el(D_el, j, mul_s, e_s)), y0)
            badr = totr = 0
            for oi in held:
                for x in orbs[oi]:
                    for g in range(p_syn):
                        totr += 1
                        if Phi_r[syn_src["act"](g, x)] != syn_tgt["act"](
                                phi_syn[g], Phi_r[x]):
                            badr += 1
            rule_rows.append({"rule": rule, "extension": kind,
                              "held_out_cells": totr, "violations": badr})
    rot_viol = sorted({r["violations"] for r in rule_rows
                       if r["extension"] == "E-ROT"})
    ref_viol = sorted({r["violations"] for r in rule_rows
                       if r["extension"] == "E-REF"})
    g39 = gate("G39", "DISCLOSURE (RUNBOOK 14 addendum, v13 #208 -- recorded, "
               "NOT a must-pass gate): the held-out check discriminates a "
               "ROTATION-valued extension from a REFLECTION-valued one and is "
               "BLIND to which rotation rule is declared.  Measured by sweeping "
               "five declared rotation rules and their five reflection-valued "
               "counterparts: every rotation rule passes at every held-out cell "
               "and every reflection rule fails at the same number of them, "
               "because <D> is abelian and the held-out equation is then an "
               "identity.  What the 234 cells verify is centraliser membership",
               rot_viol == [0] and len(ref_viol) == 1 and ref_viol[0] > 0,
               {"rules_swept": len(rule_rows),
                "rotation_valued_violations": rot_viol,
                "reflection_valued_violations": ref_viol,
                "what_the_check_verifies": "that the extension element "
                                           "centralises the group map's image",
                "held_out_cells": rule_rows[0]["held_out_cells"]},
               must_pass=False)
    report("G39", g39, f"{len(rule_rows)} rule x extension rows: rotation-valued "
           f"violations {rot_viol}, reflection-valued {ref_viol} of "
           f"{rule_rows[0]['held_out_cells']} held-out cells")
    in_arena_found_possible = (max_two_ord >= two_prime_product)
    g41 = gate("G41", "DISCLOSURE (recorded, NOT a must-pass gate): THE TWO "
               "OUTCOMES ARE DEMONSTRATED AT DIFFERENT EVIDENTIAL STANDARDS.  "
               "EMPTY is measured against the intersection-over-primes reading "
               "at every instance of both scopes; FOUND is demonstrated at a "
               "declared synthetic pair at one prime, and separately at the live "
               "extended-scope cells (G36) which requirement 4 excludes.  Under "
               "this unit's declared reading of requirement 4, an IN-ARENA FOUND "
               "was foreclosed before any census ran: it needs an instance "
               "admitting every declared prime, hence 2*ord(D) divisible by "
               "their product, and the nine-label family's maximum is far below "
               "even the smallest two-prime product -- both numbers computed",
               not in_arena_found_possible,
               {"EMPTY_is_measured_over": "20 instances x 7 primes, "
                                          "intersection reading",
                "FOUND_is_demonstrated_at": "one declared synthetic pair "
                                            "(p = 3) and the live extended-scope "
                                            "cells (excluded by requirement 4)",
                "the_product_of_all_declared_primes": all_prime_product,
                "the_smallest_two_prime_product": two_prime_product,
                "the_largest_2_ord_D_in_the_declared_family": max_two_ord,
                "an_in_arena_FOUND_was_reachable": in_arena_found_possible},
               must_pass=False)
    report("G41", g41, f"in-arena FOUND needs 2*ord(D) >= {two_prime_product} "
           f"(two primes) or {all_prime_product} (all seven); the family's "
           f"maximum is {max_two_ord}")
    say("")

    # ==================== 14. THE AST GUARDS ================================
    say("--- 14. THE AST GUARDS ---")
    fl = ast_float_scan(src)
    fl_synth = ast_float_scan(SYNTH_FLOAT_SAMPLE)
    g28 = gate("G28", "EXACT ARITHMETIC THROUGHOUT: no float or complex literal "
               "and no float()/complex() call appears in this source, and the "
               "scanner that measures it is validated by a synthetic sample it "
               "must flag",
               fl == [] and len(fl_synth) == 2,
               {"hits_in_source": fl, "hits_in_the_synthetic_sample": fl_synth})
    report("G28", g28, f"{len(fl)} hits in source, {len(fl_synth)} in the "
           f"synthetic sample")
    mo = ast_mutant_scan(src)
    mo_synth = ast_mutant_scan(SYNTH_MUTANT_SAMPLE)
    g29 = gate("G29", "NO GATE PREDICATE REFERENCES MUTANT IDENTITY (RUNBOOK 14 "
               "addendum, v13 #208): no function that registers a gate reads a "
               "mutant switch, a mutant name, a run-mode boolean or sys.argv, "
               "and the scanner is validated by a synthetic sample it must flag",
               mo == [] and mo_synth == ["f"],
               {"offenders": mo, "synthetic_sample_flagged": mo_synth})
    report("G29", g29, f"{len(mo)} offenders; synthetic sample flagged: {mo_synth}")
    g30 = gate("G30", "ANCHOR FAILURES ARE EXIT-1: the anchor policy is measured "
               "-- every anchor mismatch recorded in this run was fatal, so no "
               "anchor can fail softly",
               ANCHOR_POLICY["failures"] == ANCHOR_POLICY["fatal"],
               {"anchor_policy": dict(ANCHOR_POLICY), "anchors": len(ANCHORS)})
    report("G30", g30, f"{len(ANCHORS)} anchors; failures "
           f"{ANCHOR_POLICY['failures']}, fatal {ANCHOR_POLICY['fatal']}")
    say("")

    # ==================== 15. THE VERDICT ===================================
    say("--- 15. THE VERDICT, DERIVED INSIDE ITS GATE FROM THE MEASURED COUNTS ---")
    empty_everywhere = census_is_empty(nt_fwd1, nt_rev1)
    complete = g09 and g11 and g02 and g17 and g19
    invariant = g12 and g13 and g14 and g15 and g16
    verdict = derive_verdict(empty_everywhere, invariant, g21, g25, complete)
    recomputed = ("BRG-EMPTY-AT-CARRIER"
                  if (complete and invariant and g21 and g25 and empty_everywhere)
                  else ("BRG-MORPHISM-FOUND"
                        if (complete and invariant and g21 and g25)
                        else "BRG-BLOCKED-AT-CENSUS-DISCIPLINE"))
    # A THIRD derivation, from the recorded census tables alone: the per-cell
    # counts of the OTHER route are re-summed here, so a corruption of the
    # emptiness decision at its own source does not propagate into this leg.
    recount_fwd = sum(c["hom_forward_route_b"] - 1 for c in cells1)
    recount_rev = sum(c["hom_reverse_route_b"] - 1 for c in cells1)
    empty_from_tables = (recount_fwd == 0 and recount_rev == 0)
    verdict_from_tables = ("BRG-EMPTY-AT-CARRIER"
                           if (complete and invariant and g21 and g25
                               and empty_from_tables)
                           else ("BRG-MORPHISM-FOUND"
                                 if (complete and invariant and g21 and g25)
                                 else "BRG-BLOCKED-AT-CENSUS-DISCIPLINE"))
    tracking_excluded = sum(1 for v in DECL["functors"].values()
                            if "PRIME-TRACKING" in v)
    qualifiers = {
        "scope": "the committed transport instances at the declared primes",
        "primes": qualifier_value("primes", len(primes)),
        "instances": qualifier_value("instances", len(rows1)),
        "directed_cells": qualifier_value("directed_cells", 2 * n_cells1),
        "extended_scope_cells": qualifier_value("extended_scope_cells",
                                                2 * len(cells2)),
        "completion_family_members": qualifier_value(
            "completion_family_members", fam_cells),
        "non_degenerate_group_morphisms_forward": qualifier_value(
            "non_degenerate_group_morphisms_forward", nt_fwd1),
        "non_degenerate_group_morphisms_reverse": qualifier_value(
            "non_degenerate_group_morphisms_reverse", nt_rev1),
        "non_degenerate_functor_pairs": qualifier_value(
            "non_degenerate_functor_pairs", nondeg_total),
        "live_extended_scope_cells": qualifier_value("live_extended_scope_cells",
                                                     live_cells),
        "admissible_prime_cells_found_outside_the_committed_scope":
            qualifier_value("admissible_prime_cells_found_outside_the_"
                            "committed_scope", len(found_rows)),
        "obstruction_forward": qualifier_value("obstruction_forward", name),
        "obstruction_reverse": qualifier_value(
            "obstruction_reverse", "2-group abelianisation (prime-independent)"),
        "prime_tracking_candidates_excluded": qualifier_value(
            "prime_tracking_candidates_excluded", tracking_excluded),
    }
    # every printed qualifier, recomputed here from its own source
    qual_check = {
        "primes": len({c["p"] for c in cells1}),
        "instances": len({c["instance"] for c in cells1}),
        "directed_cells": 2 * len(cells1),
        "extended_scope_cells": 2 * len(cells2),
        "completion_family_members": len(fam_class),
        "non_degenerate_group_morphisms_forward":
            sum(c["nontrivial_forward"] for c in cells1),
        "non_degenerate_group_morphisms_reverse":
            sum(c["nontrivial_reverse"] for c in cells1),
        "non_degenerate_functor_pairs":
            sum(r["non_degenerate_pairs"] for r in functor_rows),
        "live_extended_scope_cells":
            sum(1 for c in (cells1 + cells2) if c["nontrivial_forward"] > 0),
        "admissible_prime_cells_found_outside_the_committed_scope":
            sum(1 for r in found_rows
                if r["accepted_by_the_full_delivered_predicate"]),
        "obstruction_forward": obstruction_name(coprime_iff_empty),
        "obstruction_reverse": "2-group abelianisation (prime-independent)",
        "prime_tracking_candidates_excluded":
            sum(1 for v in DECL["functors"].values() if "PRIME-TRACKING" in v),
    }
    qual_bad = sorted(k for k, v in qual_check.items() if qualifiers[k] != v)
    g31 = gate("G31", "THE VERDICT STRING AND EVERY ONE OF ITS QUALIFIERS ARE "
               "DERIVED INSIDE THIS GATE FROM THE MEASURED COUNTS (RUNBOOK 13 "
               "addendum, v13 #234): the verdict is derived once from the "
               "emptiness decision, recomputed by a second expression over the "
               "same five booleans, and derived a THIRD time from the recorded "
               "census tables by re-summing the per-cell counts of the other "
               "route -- so neither a hand-typed verdict nor a corrupted count "
               "survives; and every printed qualifier is recomputed here from "
               "its own source, so a typed qualifier cannot reach the receipt",
               verdict == recomputed == verdict_from_tables
               and verdict in DECL["outcomes"][:2]
               and empty_everywhere == empty_from_tables
               and qual_bad == [],
               {"verdict": verdict, "recomputed": recomputed,
                "verdict_recomputed_from_the_census_tables": verdict_from_tables,
                "qualifiers": qualifiers,
                "qualifiers_recomputed_in_gate": qual_check,
                "qualifiers_that_disagree": qual_bad,
                "inputs": {"empty_everywhere": empty_everywhere,
                           "empty_recomputed_from_the_tables": empty_from_tables,
                           "forward_recount_from_the_tables": recount_fwd,
                           "reverse_recount_from_the_tables": recount_rev,
                           "complete": complete, "invariant": invariant,
                           "found_reachable": g21, "empty_reachable": g25}})
    report("G31", g31, f"verdict {verdict} (recomputed {recomputed}; from the "
           f"census tables {verdict_from_tables}); {len(qual_check)} qualifiers "
           f"recomputed, {len(qual_bad)} disagreements")
    say("")
    say(f"        VERDICT: {verdict}")
    for k in sorted(qualifiers):
        say(f"          {k:44s} {qualifiers[k]}")
    say("")

    # ==================== DISCLOSURES =======================================
    x01_counterexamples = []
    for nn in range(1, 21):
        els_x, mul_x, e_x = dihedral_abstract(nn)
        got_x = len(homs_route_a(2, els_x, mul_x, e_x))
        if got_x != _gcd(nn, 2):
            x01_counterexamples.append([nn, got_x, _gcd(nn, 2)])
    disclose("X01", "The count |hom(Z/p, D_n)| = gcd(n, p) is analytically "
             "forced FOR ODD p; it FAILS at p = 2, which is inadmissible on the "
             "deformation side, and the failures are measured here rather than "
             "asserted.  It is recorded as a disclosure and is NOT used as a "
             "gate; both census routes compute the count without invoking it.",
             {"analytically_forced_for_odd_p": True,
              "measured_failures_at_p_equals_2":
                  len(x01_counterexamples),
              "n_measured_gcd_at_p_equals_2": x01_counterexamples[:5],
              "every_declared_prime_is_odd": all(q % 2 == 1 for q in primes)})
    disclose("X02", "At GEN's equivariant class the group |<W,D>| = 2 while GEN's "
             "measured based-holonomy group order is 1, because that base refuses "
             "the links altogether.  These are two different coordinates; this "
             "unit's census consumes the <W,D> coordinate (XBA's), and the "
             "agreement gate is taken at the eleven classes of defect order >= 2 "
             "where the two coordinates coincide.",
             {"classes_where_the_two_coordinates_agree": 11,
              "classes_where_they_differ": 1})
    disclose("X03", "Base 1's defect and base S's defect are not determined by "
             "the published receipts.  Neither is guessed: the whole set of "
             "candidates consistent with every committed datum is swept, and "
             "every member gives the same group order, so the ambiguity cannot "
             "move a census count.",
             {"base_1_candidates": len(amb1), "base_S_candidates": len(amb_S)})
    disclose("X04", "The synthetic FOUND branch is exhibited at a DECLARED "
             "SYNTHETIC pair, at the prime 3, which is outside the deformation "
             "side's admissible primes: rho = (1/6,1/6) does not reduce there.  "
             "It is NOT the only exercise of the FOUND machinery: the same "
             "held-out protocol is run at the live extended-scope cells, at the "
             "DECLARED-ADMISSIBLE primes 5 and 7, and passes there too (G36).  "
             "What excludes those cells is requirement 4, not a failure of the "
             "verification.",
             {"synthetic_prime": 3, "non_reducible_primes": nonreducible,
              "admissible_prime_cells_at_which_the_protocol_also_passes":
                  [[r["p"], r["class"], r["held_out_cells"],
                    r["held_out_violations"]] for r in found_rows]})
    disclose("X05", "Over the EXTENDED scopes a non-trivial group morphism does "
             "exist -- at p = 5 into the defect-order-5 and defect-order-15 "
             "classes and at p = 7 into the defect-order-7 class -- and each of "
             "them extends, because the source action is free, to "
             "non-degenerate pairs in counts of 240, 240 and 656 digits (G36).  "
             "They satisfy the full delivered predicate, not merely its group "
             "clause.  They are measured and reported, and excluded from the "
             "verdict by pin requirement 4 because their existence is a function "
             "of the declared reduction prime.",
             {"live_extended_cells": [[p, nm] for (p, nm) in live2],
              "non_degenerate_pair_digits_at_those_cells":
                  [r["non_degenerate_pairs_digits"] for r in found_rows]})
    disclose("X06", "The functor-level census counts the SP-satisfying pairs by "
             "the orbit-representative formula; the counts are astronomically "
             "large and entirely degenerate.  Only the non-degenerate count "
             "enters any argument.",
             {"non_degenerate_pairs_over_the_committed_scope": nondeg_total})
    disclose("X07", "The held-out check is a TWO-VALUED measurement, not a test "
             "of the declared extension formula: for any rotation-valued "
             "extension the held-out equations hold identically because <D> is "
             "abelian, and every reflection-valued one fails at the same cells.  "
             "Measured under five declared rotation rules and their five "
             "reflection counterparts (G39).  What the check verifies is "
             "centraliser membership.",
             {"rotation_violations": rot_viol, "reflection_violations": ref_viol,
              "analytically_forced": True})
    disclose("X08", "THE TWO OUTCOMES ARE HELD TO DIFFERENT EVIDENTIAL "
             "STANDARDS.  EMPTY is measured against the intersection reading at "
             "every instance of both scopes; FOUND is exhibited at a synthetic "
             "pair and at the live cells that requirement 4 excludes.  Under "
             "this unit's declared reading of requirement 4 an in-arena FOUND "
             "was foreclosed before any census ran, by an arithmetic the unit "
             "computes: two declared primes need 2*ord(D) divisible by their "
             "product, and the declared family's maximum is below it (G41).",
             {"smallest_two_prime_product": two_prime_product,
              "largest_2_ord_D_in_the_family": max_two_ord})
    disclose("X09", "The two FORWARD census routes are two implementations of "
             "one criterion -- g^p = e and ord(g) | p are the same predicate -- "
             "over a SHARED abstract model, and are disclosed as such rather "
             "than advertised as independent computations.  What audits the "
             "shared model is a different gate: the explicit isomorphism from "
             "the model to the permutation rebuild, verified on every ordered "
             "pair (G03), together with the abelianisation measurement (G27).  "
             "The two REVERSE routes are genuinely different computations (word "
             "evaluation in G, versus construction of the abelianisation and its "
             "own quotient table).",
             {"forward_routes": "one criterion, two implementations, shared model",
              "the_model_is_audited_at": ["G03 (explicit isomorphism)",
                                          "G27 (abelianisation)"],
              "reverse_routes": "two different computations"})
    disclose("X10", "G27's outcome is analytically forced for the dihedral "
             "family -- the abelianisation of a dihedral group is Z/2 or "
             "Z/2 x Z/2 -- and the dihedral form is itself forced by the one law "
             "(G35).  It is retained as a gate because the commutator subgroup "
             "is BUILT rather than cited, so a wrong model is caught there; the "
             "forcing is recorded here.  G14's outcome is forced in the "
             "nine-label arena only, and G40 measures that it is contingent at "
             "sixteen labels.",
             {"abelianisation_orders_measured": ab_orders,
              "forced_for": "the dihedral family"})
    disclose("X11", "THE STRENGTHENED STANDARD IS REGISTERED AND UNTESTED.  The "
             "six requirements a live-cell morphism would have to meet before "
             "the word 'bridge' is earned -- encoding intertwining as a "
             "commuting square first among them -- are declared at "
             "DECL.strengthened_standard as the successor's gate.  NO cell of "
             "any scope in this unit is evaluated against them, in either "
             "direction: this unit's EMPTY and its live cells are both at the "
             "DELIVERED standard.",
             {"requirements": sorted(k for k in DECL["strengthened_standard"]
                                     if k.startswith("S")),
              "tested_here": False})
    disclose("X12", "Three of this unit's anchors carry values published in the "
             "XBA paper's committed table rather than in a receipt's JSON: "
             "species 4's defect and exchange fixed-configuration counts and its "
             "120-member transposition split.  The paper file is hash-pinned "
             "here so those anchors are hash-protected, and all three are "
             "recomputed from the rebuilt permutations.",
             {"paper_pinned": "v13/paper-xba-crossbase.md"})

    must = [g for g in GATES if g["must_pass"]]
    failed = [g["id"] for g in must if not g["passed"]]
    say(f"  gates {len(GATES)} ({len(must)} must-pass), failures {len(failed)}: "
        f"{failed}")
    say(f"  anchors {len(ANCHORS)}, all reproduced")
    say("")

    tables.update({
        "transport_instances": [
            {"instance": a, "carrier": b, "ord_D": c, "group_order": d,
             "rebuilt_as_permutations": e} for (a, b, c, d, e) in inst_rows],
        "gen_classes": [{"class": a, "carrier": b, "ord_D": c, "group_order": d}
                        for (a, b, c, d, _e) in class_rows],
        "completion_family": {"members": fam_cells,
                              "defect_order_spectrum":
                                  {str(k): v for k, v in sorted(ord_spec.items())},
                              "fixed_configuration_spectrum":
                                  {str(k): v for k, v in sorted(fix_spec.items())},
                              "dihedral_relation_failures": dih_fail},
        "deformation_side": ha_rows,
        "non_reducible_primes": nonreducible,
        "census_scope_1": cells1,
        "census_scope_2": cells2,
        "functor_census": functor_rows,
        "tiny_cells": tiny_rows,
        "dictionary_census": {str(k): v for k, v in
                              sorted(admissible_by_prime.items())},
        "dictionary_committed_scope": {str(k): v for k, v in
                                       sorted(committed_adm.items())},
        "held_out": heldout_rows,
        "held_out_rule_sweep": rule_rows,
        "self_tests": selftest_rows,
        "generator_sweep": gen_rows,
        "cache": dict(_CACHE_STATS),
        "obstruction": {"forward_name": name, "empty_cells": empty_cells,
                        "live_cells": live_cells,
                        "the_forward_equivalence_holds_both_ways":
                            coprime_iff_empty,
                        "reverse_name": "2-group abelianisation "
                                        "(prime-independent)",
                        "reverse_non_trivial_total":
                            sum(c["nontrivial_reverse"] for c in all_cells),
                        "reverse_empty_at_the_live_cells": live_rev_empty,
                        "reverse_emptiness_is_coextensive_with_coprimality":
                            rev_coextensive,
                        "abelianisation_orders": ab_orders,
                        "primes_dividing_2_ord_D_by_instance": rad_by_instance,
                        "primes_dividing_2_ord_D_union": rad_union,
                        "primes_where_rho_fails_to_reduce": nonreducible,
                        "the_union_without_base_T": rad_no_T},
        "the_one_law_family": {
            "statement": "W^2 = 1 and D = [W,u] force W D W = D^-1, hence "
                         "<W,D> dihedral of order 2*ord(D) whenever W is not a "
                         "power of D",
            "randomised_draws": draws,
            "violations_of_the_relation": rel_viol,
            "violations_of_the_order_formula": ord_viol,
            "control_draws": ctrl_tested,
            "control_violations": ctrl_viol,
            "defect_orders_drawn": sorted(orders_drawn),
            "the_only_contingent_content":
                f"ord(D) <= {max_ord_committed} at the committed instances"},
        "the_lagrange_cauchy_sweep": {
            "groups": len(zoo), "cells": zoo_cells, "failures": zoo_fail,
            "non_dihedral_cells_against_the_order_reading": order_reading_cells,
            "failures_of_the_order_reading_off_the_dihedral_family":
                order_reading_fail,
            "zoo": zoo_rows},
        "found_at_the_admissible_primes": {
            "label": "FOUND-AT-DELIVERED-STANDARD-OUTSIDE-COMMITTED-SCOPE",
            "cells": found_rows,
            "excluded_by": "pin requirement 4 (the prime is a declaration)",
            "the_delivered_standard_is_weak_at_the_functor_layer": {
                "source_orbits": len(orbs_v),
                "orbits_collapsed_into_one_target_orbit": collapsed_orbits,
                "still_accepted": coll["accepted"]},
            "the_strengthened_standard": DECL["strengthened_standard"]},
        "the_sector_concentration": {
            "family_members": fam_cells,
            "low_defect_order_band": f"ord(D) <= {bound}",
            "members_in_the_low_band": sector_low,
            "members_admitting_some_declared_prime": sector_live,
            "orders_admitting_one": live_orders,
            "committed_instances_in_the_low_band": committed_low,
            "committed_instances_admitting_one": committed_live},
        "the_arena_dependence_of_the_two_prime_clause": {
            "smallest_two_prime_product": two_prime_product,
            "all_prime_product": all_prime_product,
            "nine_label_family_maximum_defect_order": max_m3,
            "Landau_9": _landau(9), "Landau_16": _landau(16),
            "sampled_arena_labels": m_cont * m_cont,
            "sample_size": n_sample,
            "sampled_members_divisible_by_the_two_prime_product": hits4,
            "witness_completion": witness4},
        "registered_opens": DECL["registered_opens"],
        "prime_tracking": {"F3_by_prime": {str(k): v for k, v in sorted(track.items())},
                           "extended_census_by_prime":
                               {str(k): v for k, v in sorted(track_extended.items())}},
        "verdict_qualifiers": qualifiers,
    })
    return {"tables": tables, "verdict": [verdict], "failed": failed,
            "totals": {"anchors": len(ANCHORS), "gates": len(GATES),
                       "must_pass_gates": len(must),
                       "must_pass_failures": len(failed),
                       "disclosures": len(DISCLOSURES)},
            "hash_pins": got}


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def _is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0


def _pow_el(g, e, mul, ident):
    cur = ident
    for _ in range(e):
        cur = mul(cur, g)
    return cur


def _build_zoo_group(spec):
    """The declared group zoo, built as permutation groups from the declaration
    alone.  Returns (elements as tuples, degree)."""
    kind, arg = spec
    if kind == "cyclic":
        n = arg
        return [tuple((i + k) % n for i in range(n)) for k in range(n)], n
    if kind == "dihedral":
        n = arg
        r = tuple((i + 1) % n for i in range(n))
        f = tuple((-i) % n for i in range(n))
        return closure([r, f], n), n
    if kind == "symmetric":
        n = arg
        return [tuple(t) for t in itertools.permutations(range(n))], n
    if kind == "alternating":
        n = arg
        out = []
        for t in itertools.permutations(range(n)):
            seen, par = [False] * n, 0
            for i in range(n):
                if not seen[i]:
                    j, ln = i, 0
                    while not seen[j]:
                        seen[j] = True
                        j = t[j]
                        ln += 1
                    par += ln - 1
            if par % 2 == 0:
                out.append(tuple(t))
        return out, n
    a, b = arg
    if kind == "product-cyclic":
        G1, n1 = _build_zoo_group(("cyclic", a))
        G2, n2 = _build_zoo_group(("cyclic", b))
    elif kind == "product-alt-cyclic":
        G1, n1 = _build_zoo_group(("alternating", a))
        G2, n2 = _build_zoo_group(("cyclic", b))
    else:
        G1, n1 = _build_zoo_group(("dihedral", a))
        G2, n2 = _build_zoo_group(("cyclic", b))
    return ([tuple(list(x) + [n1 + y for y in z]) for x in G1 for z in G2],
            n1 + n2)


def _el_order(g, mul, ident):
    """The order of one element of an abstract group."""
    c, cur = 1, g
    while cur != ident:
        cur = mul(cur, g)
        c += 1
    return c


def _rebuild_is_abstract():
    """Whether the comparator has been routed through the audited component.
    [instrument -- mutable]"""
    return _M_COMPSELF


# ==========================================================================
#                          THE MUTANT HARNESS
# ==========================================================================

def run_mutant_harness():
    """Spawn every declared mutant and record its named kills.  Registers no
    gate, so the AST guard's claim is unaffected by the mutant names here."""
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
        "schema": "brg-bridge-receipt-v1",
        "pin": "v13/note-brg-bridge-pin.md",
        "pin_base_commit": "b632f59",
        "source_sha256": hashlib.sha256(src.encode()).hexdigest(),
        "python": platform.python_version(),
        "arithmetic": "integers / fractions.Fraction / exact F_p; no floats",
        "hash_pins": R["hash_pins"],
        "declarations": json.loads(json.dumps(DECL, default=str)),
        "anchors": ANCHORS,
        "gates": GATES,
        "disclosures": DISCLOSURES,
        "tables": R["tables"],
        "totals": R["totals"],
        "verdict": R["verdict"],
    }
    mut_rows, survivors, never_falsified = run_mutant_harness()
    receipt["mutants"] = mut_rows
    receipt["never_falsified"] = never_falsified
    receipt["totals"]["mutants"] = len(mut_rows)
    receipt["totals"]["mutant_survivors"] = len(survivors)
    say("")

    if WRITE_ARTIFACTS:
        with open(os.path.join(HERE, "brg_bridge_output.txt"), "w",
                  encoding="utf-8") as fh:
            fh.write("\n".join(OUT) + "\n")
        with open(os.path.join(HERE, "brg_bridge_receipt.json"), "w",
                  encoding="utf-8") as fh:
            json.dump(receipt, fh, indent=1, sort_keys=True, default=str)
            fh.write("\n")
    else:
        progress("falsification-selftest: artifacts NOT written")
    progress("done")
    return 0 if (not R["failed"] and not survivors and not never_falsified) else 1


if __name__ == "__main__":
    sys.exit(main())

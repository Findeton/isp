#!/usr/bin/env python3
"""
R1 -- THE CONTINUUM RUNG.  v14 paper-01.  Self-contained exact instrument.

QUESTION (two-sided, pre-registered in v14/note-r1-continuum-pin.md):
    does a DECLARED refinement family over the v13 substrate admit a
    PRE-REGISTERED INTENSIVE invariant that stabilizes under refinement?

CLI CONTRACT
------------
    r1_continuum_exact.py
        THE PLAIN DELIVERY RUN.  Rebuilds the family, computes the five
        registered invariants at every member, derives the verdict inside a
        gate, runs the four controls, runs the mutant table (one subprocess
        per declared mutant), and WRITES the two artifacts
        `r1_continuum_output.txt` and `r1_continuum_receipt.json`.
        Exit 0 iff no must-pass gate and no anchor failed; exit 1 otherwise,
        and on failure the artifacts are NOT written.

    r1_continuum_exact.py --mutant NAME [--quiet]
        Runs the unit with exactly one declared corruption active.  WRITES
        NO ARTIFACTS.  Reaches the totals block and exits 1.  `--quiet`
        emits the machine-readable KILL-JSON line instead of the report.

    r1_continuum_exact.py --falsification-selftest
        THE FALSIFICATION SELF-TEST.  Corrupts one pinned external anchor
        (the R0 inheritance hash of the LCB receipt) and confirms the run
        dies loudly.  WRITES NO ARTIFACTS.  Exit 0 iff the run did die.

    r1_continuum_exact.py --list-mutants
        Prints the declared mutant names, one per line.  Writes nothing.

DISCIPLINE
----------
    RUNBOOK section 13 / 14 / 15 with every addendum.  Exact arithmetic only
    (int and fractions.Fraction; the `/` operator does not occur in this
    file and an AST guard proves it).  Anchors are exit-1-only.  Counts are
    computed, never typed.  No gate predicate references mutant identity.
    Declared-arena data is printed and matched at every coordinate.
"""

import argparse
import ast
import hashlib
import json
import math
import sys
from collections import defaultdict
from fractions import Fraction as Fr
from itertools import combinations, permutations, product
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
OUT_TXT = HERE / "r1_continuum_output.txt"
OUT_JSON = HERE / "r1_continuum_receipt.json"

MUTANT = None
SOURCE_SHA256 = ""
GATES = []
ANCHORS = []
DISCLOSURES = []
TABLES = {}
FINDINGS = {}
_MEASURED = 0
_FROZEN = False
CACHE = {}
CACHE_STATS = {"lookups": 0, "hits": 0, "bypasses": 0, "selftest_hits": 0}


def prog(msg):
    sys.stderr.write("[r1] " + msg + "\n")
    sys.stderr.flush()


def bump():
    """Every measured datum of this unit passes through this counter."""
    global _MEASURED
    _MEASURED += 1


def canon(v):
    if isinstance(v, Fr):
        return "%d/%d" % (v.numerator, v.denominator)
    if isinstance(v, (list, tuple)):
        return "[" + ", ".join(canon(x) for x in v) + "]"
    if isinstance(v, dict):
        return "{" + ", ".join("%s: %s" % (canon(k), canon(v[k]))
                               for k in sorted(v, key=str)) + "}"
    return str(v)


def gate(gid, cls, claim, ok, value=None):
    GATES.append({"id": gid, "class": cls, "claim": claim,
                  "passed": bool(ok), "value": value})
    return bool(ok)


def disclose(did, statement, value=None):
    DISCLOSURES.append({"id": did, "statement": statement, "value": value})


def anchor(aid, source, quantity, declared, computed):
    ok = canon(declared) == canon(computed)
    ANCHORS.append({"id": aid, "source": source, "quantity": quantity,
                    "declared": canon(declared), "computed": canon(computed),
                    "passed": ok})
    return ok


# ===========================================================================
# 1.  THE DECLARATIONS.  Frozen here, before any measured datum.
# ===========================================================================

DECL = {
    "question": (
        "does a DECLARED refinement family over the v13 substrate admit a "
        "PRE-REGISTERED INTENSIVE invariant that stabilizes under "
        "refinement?"),

    "arena": {
        "boundary": (
            "one ARENA per family member: a finite label set L with a "
            "distinguished label 0, a declared chart symmetry Sigma in "
            "Sym(L), and the declared block partition of L minus {0} -- the "
            "orbits of the arena's own declared completion subgroup.  "
            "Nothing outside (L, 0, Sigma, blocks) enters any construction."),
        "family": (
            "A1 = the nine-label completion arena of I5; A2 = the "
            "sixteen-label successor arena of I5's G15; A3 = the 43-label "
            "grown arena of I2's control; A4, A5 = the next two members of "
            "A3's own declared growth family L_m, the rule being extracted "
            "from the pinned receipt as data.  Every label count is DERIVED "
            "from pinned data; none is typed."),
        "law": (
            "the atlas over an arena: charts are the labels; the coordinate "
            "cells are (block, rule) with rule in {FULL, REAL}; the drawn "
            "identification at a cell is the UNIQUE element of that cell's "
            "cyclic transport group carrying one chart to the other."),
        "state": "the distinguished label 0, fixed by Sigma and by every "
                 "block transport",
        "arena action": (
            "the relabelling action of Sym(L) by conjugation -- an arena "
            "coordinate.  The invariants are self-tested under a declared "
            "non-trivial relabelling (RUNBOOK section 14)."),
        "provenance": (
            "v13 enters only through the seven R0 rows, each verified by "
            "sha256-12 at run time; nothing of v13 is imported as code."),
        "admission": (
            "a registered invariant STABILIZES iff it is exactly constant "
            "(exact-arithmetic equality) on the final K consecutive family "
            "members; K = 3, declared in the pin."),
    },

    "atlas": {
        "charts": "the labels of L",
        "coordinate cells": (
            "(k, rule) for k a block index and rule in {FULL, REAL}: the "
            "FULL transport at cell k is gamma_k, the increasing-index cycle "
            "on block B_k; the REAL transport is Sigma_k . gamma_k, where "
            "Sigma_k is the arena symmetry restricted to the <Sigma>-"
            "saturation of B_k and extended by the identity -- the block "
            "transport as the chart symmetry realises it on that patch"),
        "drawn": (
            "an ordered pair (a, b) with a != b is DRAWN at a cell iff "
            "EXACTLY ONE element pi of that cell's cyclic transport group "
            "satisfies pi(a) = b; the drawn map is that pi.  This is I3's "
            "own admission rule -- draw iff the identification is unique"),
        "N": ("0-cells the charts; 1-cells one per unordered drawn pair per "
              "coordinate cell; 2-cells the unordered chart triples pairwise "
              "drawn at a COMMON block index, one rule chosen per edge"),
        "N_coh": "the 2-cells of N whose three drawn maps compose to the "
                 "identity -- the cocycle condition on transition maps",
        "overlap graph G": "simple; an edge where an identification is drawn "
                           "at SOME coordinate cell",
    },

    "registered_invariants": [
        ["PHI", "the overlap-completeness fraction: drawn chart pairs over "
                "all chart pairs.  Also R2's gateway: any member with "
                "PHI < 1 unlocks the manifold rung", "scalar"],
        ["NCOH_DENSITY", "coherent 2-cells per drawn chart pair: "
                         "|F(N_coh)| over |E(N)|", "scalar"],
        ["SPECTRAL_PROFILE", "the normalised cyclotomic profile of I - E "
                             "over the arena's readouts E = rho_L(pi), pi in "
                             "<Sigma> minus the identity: d -> mult(Phi_d) "
                             "over dim.  I2's eigenvalue-1 row is confirmed "
                             "as an anchor at every member", "profile"],
        ["DIMENSION_PROFILE", "the link-dimension distribution normalised by "
                              "chart count: v -> #{charts of link-vertex "
                              "count v} over |charts|.  The RAW estimator is "
                              "extensive by I3 and is EXCLUDED", "profile"],
        ["B2_DENSITY", "b_2 of N_coh over F_2, per 2-cell of N_coh", "scalar"],
    ],

    "excluded": {
        "the raw local-dimension estimator": "EXTENSIVE by I3 -- excluded as "
                                             "an intensive candidate",
        "b_1": "trivial by I3's ordered measurement and carries no "
               "identification content -- excluded as a candidate, printed "
               "once as a disclosure",
    },

    "K": 3,
    "family_target": 5,

    "verdict_templates": {
        "STABILIZES": "R1-STABILIZES-AT-<...>",
        "NO_CONTINUUM": "R1-NO-CONTINUUM-LIMIT-AT-THIS-SUBSTRATE-<...>",
        "rule": ("the head is STABILIZES iff the measured set of registered "
                 "invariants constant on the final K members is NON-EMPTY, "
                 "and NO-CONTINUUM-LIMIT iff it is EMPTY.  Every qualifier "
                 "-- the stabilised values, the window, each divergent "
                 "invariant's measured failure mode, the functoriality "
                 "qualifier and R2's gateway -- is computed from the "
                 "trajectory table inside the verdict gate"),
    },

    "failure_modes": {
        "scalar": ["CONSTANT", "STRICTLY-INCREASING", "STRICTLY-DECREASING",
                   "NON-MONOTONE", "UNDEFINED-AT-A-MEMBER"],
        "profile": ["CONSTANT", "SUPPORT-CONSTANT-WEIGHTS-MOVING",
                    "SUPPORT-MOVING", "UNDEFINED-AT-A-MEMBER"],
    },

    "morphism_criterion": (
        "an ADMISSIBLE ARENA MORPHISM iota : A -> A' is an injection of "
        "label sets with iota(0) = 0, iota . Sigma_A = Sigma_A' . iota, and "
        "a block-index injection sigma with iota(B_k) contained in "
        "B'_sigma(k).  Equivariance forces every <Sigma_A>-orbit to map "
        "bijectively onto a <Sigma_A'>-orbit of the SAME size; the search is "
        "therefore a finite orbit-and-block matching, decided exhaustively, "
        "and a witness is CONSTRUCTED whenever one exists"),

    "controls": {
        "POSITIVE": "the constant family (A3, A3, A3): every registered "
                    "invariant is constant by construction, so the "
                    "instrument must return the STABILIZES head naming all "
                    "five",
        "NEGATIVE": "the extensive family: the same three arenas read with "
                    "I3's EXCLUDED raw estimators (the unnormalised counts). "
                    " Every candidate grows, so the instrument must return "
                    "the NO-CONTINUUM-LIMIT head",
        "SCRAMBLE": "at A3, the drawn RELATION is kept and the drawn MAPS "
                    "are deterministically permuted within each cell.  The "
                    "identification-sensitive invariants (NCOH_DENSITY, "
                    "B2_DENSITY) must move and the relation-only invariants "
                    "(PHI, DIMENSION_PROFILE) must not -- measured, not "
                    "assumed",
        "DISCRIMINATION": "the WIDENING family W_s = ({0} + one block of s "
                          "labels, Sigma the block reversal), s = 5, 6, 7: a "
                          "growth rule that is NOT a disjoint addition.  It "
                          "must MOVE the two densities, so their constancy "
                          "on the declared family is a property of that "
                          "family's rule and not of the definitions",
    },

    "K_window_fixture": {
        "declaration": "a crafted scalar trajectory whose last two members "
                       "agree and whose third-from-last does not: at K = 3 "
                       "it is NOT stabilised, at K = 1 it IS.  The window is "
                       "therefore load-bearing and a shrink flips a verdict",
        "trajectory": ["1/2", "1/3", "2/5", "2/5"],
    },
}

MUTANT_DECL = [
    ("anchor-I1", "waiver", "the R0 hash of I1/I2's carrying receipt is perturbed"),
    ("anchor-I3", "waiver", "the R0 hash of I3's carrying receipt is perturbed"),
    ("anchor-I4a", "waiver", "the R0 hash of I4's TOP adjudication is perturbed"),
    ("anchor-I4b", "waiver", "the R0 hash of I4's RSQ adjudication is perturbed"),
    ("anchor-I5", "waiver", "the R0 hash of I5's carrying receipt is perturbed"),
    ("anchor-I6", "waiver", "the R0 hash of I6's TB3 receipt is perturbed"),
    ("anchor-I7", "waiver", "the R0 hash of I7's carrying receipt is perturbed"),
    ("pin-drop", "waiver", "one R0 row is dropped from the hash census"),
    ("companion-drop", "waiver", "one R0 companion artifact is dropped from the census"),
    ("freeze-lax", "waiver", "one measured datum is evaluated before the freeze gate"),
    ("family-rule", "computation", "the extracted growth rule's block width is perturbed"),
    ("family-sel", "computation", "the growth family's member-selection rule is perturbed"),
    ("arena-a1", "computation", "A1's derived label count is perturbed"),
    ("arena-a2", "computation", "A2's derived label count is perturbed"),
    ("arena-sigma", "computation", "the arena symmetry is perturbed"),
    ("blocks-lax", "computation", "the block partition is perturbed"),
    ("regen-cache", "computation", "the regeneration self-test reads the memo instead of evaluating fresh"),
    ("cap-lax", "computation", "the family is silently truncated below the declared target"),
    ("map-func", "computation", "the constructed embedding is perturbed off equivariance"),
    ("embed-lax", "computation", "the morphism criterion accepts every step"),
    ("embed-blind", "computation", "the morphism criterion rejects every step"),
    ("drawn-lax", "computation", "the drawn-uniqueness rule accepts non-unique candidates"),
    ("coh-lax", "computation", "coherence is declared true at every 2-cell"),
    ("cell-drop", "computation", "one geometric 2-cell is dropped"),
    ("rank-lax", "computation", "the second pivot discipline is replaced by the first"),
    ("parity-lax", "computation", "the F_2 boundary is replaced by the OR-connective"),
    ("inv-phi", "computation", "PHI's second route is corrupted"),
    ("inv-ncoh", "computation", "NCOH_DENSITY's independent recount is corrupted"),
    ("inv-spec", "computation", "the spectral profile's kernel route is corrupted"),
    ("spec-anchor", "computation", "the eigenvalue-1 anchor chain is skipped"),
    ("inv-dim", "computation", "the dimension profile's second route is corrupted"),
    ("inv-b2", "computation", "b_2 is read on N instead of N_coh"),
    ("row-drop", "computation", "one trajectory row is dropped"),
    ("k-window", "computation", "the stabilisation window is shrunk from K=3 to K=1"),
    ("verdict-flip", "computation", "the verdict head is inverted"),
    ("qual-flip", "computation", "one computed qualifier is replaced by a typed string"),
    ("gateway-lax", "computation", "R2's gateway member is typed rather than computed"),
    ("pos-lax", "computation", "the positive control's family is not constant"),
    ("neg-lax", "computation", "the negative control reads normalised estimators"),
    ("scramble-lax", "computation", "the scramble leaves every drawn map in place"),
    ("disc-lax", "computation", "the discrimination family is replaced by a constant one"),
    ("selftest-select", "computation", "the symmetry self-test's tested set is chosen by the verdict"),
    ("robust-lax", "computation", "the alternative family index is not evaluated"),
    ("machinery-lax", "computation", "the homology identities used against I3's published counts are perturbed"),
    ("b0-lax", "computation", "the component route-1 census is corrupted"),
    ("float-lax", "waiver", "a float literal enters the source the arithmetic guard scans"),
    ("exempt-lax", "waiver", "the exemption sweep's permitted set is emptied"),
]
MUTANTS = [m[0] for m in MUTANT_DECL]

MUTABLE_FUNCS = {
    "r0_rows", "r0_companions", "growth_rule_from_receipt",
    "growth_member_rule", "a1_labels_from_receipt", "a2_labels_from_receipt",
    "arena_sigma", "arena_blocks", "regenerate_fresh", "family_cap",
    "build_embedding", "morphism_exists", "drawn_is_unique",
    "cell_is_coherent", "geometric_cells", "rank_f2_second",
    "boundary_connective", "phi_route_2", "ncoh_recount", "spectral_kernel",
    "spectral_anchor_chain", "dim_route_2", "b2_complex_choice",
    "trajectory_rows", "stabilisation_window", "verdict_head",
    "qualifier_source", "gateway_member", "positive_control_family",
    "negative_control_estimators", "scramble_shift",
    "discrimination_family", "selftest_tested_set", "robustness_indices",
    "measured_datum_before_freeze", "top_identity", "components_route_1",
    "exactness_scope", "exemption_scope",
}


# ===========================================================================
# 2.  EXACT ARITHMETIC PRIMITIVES.  Integers, Fractions, F_2 bit rows.
# ===========================================================================

def pident(n):
    return tuple(range(n))


def pcomp(p, q):
    """p after q."""
    return tuple(p[q[i]] for i in range(len(q)))


def pinv(p):
    out = [0] * len(p)
    for i, v in enumerate(p):
        out[v] = i
    return tuple(out)


def cycles_of(p):
    n = len(p)
    seen = [False] * n
    out = []
    for i in range(n):
        if seen[i]:
            continue
        c = [i]
        seen[i] = True
        j = p[i]
        while j != i:
            seen[j] = True
            c.append(j)
            j = p[j]
        out.append(c)
    return out


def cyclic_group(gen, n, cap):
    grp = []
    x = pident(n)
    for _ in range(cap):
        grp.append(x)
        x = pcomp(gen, x)
        if x == pident(n):
            break
    return grp


def rank_f2_high(rows, want_pivots=False):
    """Elimination with the HIGHEST set bit as pivot."""
    piv = {}
    r = 0
    for row in rows:
        x = row
        while x:
            h = x.bit_length() - 1
            if h in piv:
                x = x ^ piv[h]
            else:
                piv[h] = x
                r += 1
                break
    return (r, sorted(piv)) if want_pivots else r


def rank_f2_low(rows, want_pivots=False):
    """Elimination with the LOWEST set bit as pivot, rows consumed in
    reverse.  A second pivot discipline on the same rank -- declared as
    that, never as an independent route."""
    piv = {}
    r = 0
    for row in reversed(list(rows)):
        x = row
        while x:
            lo = (x & (-x)).bit_length() - 1
            if lo in piv:
                x = x ^ piv[lo]
            else:
                piv[lo] = x
                r += 1
                break
    return (r, sorted(piv)) if want_pivots else r


def rat_kernel_dim(mat, n):
    """dim ker of an n x n exact-rational matrix, by fraction-free-free
    Gaussian elimination over Q with Fractions."""
    m = [list(row) for row in mat]
    rank = 0
    col = 0
    while col < n and rank < n:
        piv = None
        for r in range(rank, n):
            if m[r][col] != 0:
                piv = r
                break
        if piv is None:
            col += 1
            continue
        m[rank], m[piv] = m[piv], m[rank]
        pv = m[rank][col]
        m[rank] = [x * Fr(1, 1) for x in m[rank]]
        m[rank] = [Fr(x.numerator, x.denominator) if isinstance(x, Fr)
                   else Fr(x) for x in m[rank]]
        m[rank] = [x * Fr(pv.denominator, pv.numerator) for x in m[rank]]
        for r in range(n):
            if r != rank and m[r][col] != 0:
                f = m[r][col]
                m[r] = [m[r][j] - f * m[rank][j] for j in range(n)]
        rank += 1
        col += 1
    return n - rank


def components_unionfind(nv, pairs):
    par = list(range(nv))

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    for (a, b) in pairs:
        ra, rb = find(a), find(b)
        if ra != rb:
            par[ra] = rb
    groups = defaultdict(list)
    for i in range(nv):
        groups[find(i)].append(i)
    return [sorted(v) for v in groups.values()]


def spanning_forest_cycle_rank(nv, edges):
    """Cycle rank by a breadth-first spanning forest: no elimination."""
    adj = defaultdict(list)
    for idx, (a, b) in enumerate(edges):
        adj[a].append((b, idx))
        adj[b].append((a, idx))
    seen = [False] * nv
    tree = 0
    for s in range(nv):
        if seen[s]:
            continue
        seen[s] = True
        stack = [s]
        while stack:
            x = stack.pop()
            for (y, _idx) in adj[x]:
                if not seen[y]:
                    seen[y] = True
                    tree += 1
                    stack.append(y)
    return len(edges) - tree


# ===========================================================================
# 3.  THE R0 INHERITANCE.  Hash-pinned; verified at run time.
# ===========================================================================

def r0_rows():
    """The seven R0 rows and the sha256-12 of each row's CARRYING artifact,
    read from v14/note-r0-founding-pin.md itself.  [instrument -- mutable]"""
    rows = [
        ("I1", "v13/code/rsq_reposed_square_receipt.json", "85f3cf809544"),
        ("I2", "v13/code/rsq_reposed_square_receipt.json", "85f3cf809544"),
        ("I3", "v13/code/top_topology_receipt.json", "65bb1fc5231f"),
        ("I4a", "v13/note-top-adjudication.md", "e4934f2525b0"),
        ("I4b", "v13/note-rsq-adjudication.md", "31b70406c6e8"),
        ("I5", "v13/code/lcb_livecell_receipt.json", "3e502f685ab3"),
        ("I6", "v13/code/tb3_third_base_receipt.json", "c9bc956fe751"),
        ("I7", "v13/code/ha_successor_receipt.json", "542b8735daf0"),
    ]
    bad = {"anchor-I1": "I1", "anchor-I3": "I3", "anchor-I4a": "I4a",
           "anchor-I4b": "I4b", "anchor-I5": "I5", "anchor-I6": "I6",
           "anchor-I7": "I7"}
    if MUTANT in bad:
        rows = [(k, p, ("0" + h[1:]) if k == bad[MUTANT] else h)
                for (k, p, h) in rows]
    if MUTANT == "pin-drop":
        rows = rows[:-1]
    return rows


def r0_companions():
    """The companion artifacts R0's I2 and I3 rows name in parentheses.
    Their declared hashes are checked and the measured mismatch set is
    reported exactly.  [instrument -- mutable]"""
    comp = [
        ("I2-output", "v13/code/rsq_reposed_square_output.txt", "a5266012ebd3"),
        ("I2-paper", "v13/paper-rsq-reposed-square.md", "07bea42728a2"),
        ("I2-code", "v13/code/rsq_reposed_square_exact.py", "8c7705f55fa6"),
        ("I3-output", "v13/code/top_topology_output.txt", "109302d0d036"),
        ("I3-paper", "v13/paper-top-topology.md", "4e4cd4f11bab"),
        ("I3-code", "v13/code/top_topology_exact.py", "81d07ffebd82"),
        ("I6-gen", "v13/code/gen_generality_receipt.json", "e0b2f444f6a9"),
        ("I6-psi", "v13/code/psi_curvature_receipt.json", "7c7b91a9257e"),
    ]
    if MUTANT == "companion-drop":
        comp = comp[:-1]
    return comp


def sha12(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:12]


def load_inheritance():
    rows = r0_rows()
    seen = {}
    for (rid, rel, declared) in rows:
        p = REPO / rel
        computed = sha12(p)
        anchor("A-R0-" + rid, "v14/note-r0-founding-pin.md",
               "sha256-12 of " + rel, declared, computed)
        seen[rid] = p
    charter = sha12(REPO / "v14" / "PLAN.md")
    anchor("A-R0-CHARTER", "v14/LOG.md #1", "sha256-12 of v14/PLAN.md",
           "7a40eeea0df3", charter)
    pin = sha12(REPO / "v14" / "note-r1-continuum-pin.md")
    anchor("A-R1-PIN", "v14/LOG.md #2",
           "sha256-12 of v14/note-r1-continuum-pin.md", "27c9f1144ffa", pin)
    r0 = sha12(REPO / "v14" / "note-r0-founding-pin.md")
    anchor("A-R0-PIN", "v14/LOG.md #1",
           "sha256-12 of v14/note-r0-founding-pin.md", "e9d2bedff244", r0)

    comp_rows = []
    for (cid, rel, declared) in r0_companions():
        computed = sha12(REPO / rel)
        comp_rows.append({"id": cid, "artifact": rel, "declared": declared,
                          "computed": computed, "matches": declared == computed})
    TABLES["inheritance"] = {
        "rows": [{"row": rid, "artifact": rel, "sha256_12": declared}
                 for (rid, rel, declared) in rows],
        "companions": comp_rows,
        "companion_mismatches": sorted(c["id"] for c in comp_rows
                                       if not c["matches"]),
    }
    data = {}
    for rid, p in seen.items():
        if p.suffix == ".json":
            data[rid] = json.loads(p.read_text())
    return data, comp_rows


# ===========================================================================
# 4.  THE ARENAS, REBUILT FROM THE PINNED DECLARATIONS.
# ===========================================================================

def sigma_perm(m):
    """I5's label exchange on pairs of m-valued labels, index m*u + v."""
    return tuple(m * (i % m) + (i // m) for i in range(m * m))


def wing_labels(pi):
    """I6's wing symmetry on the eight system-triple labels: a label is a
    triple of wing bits and pi permutes the wings."""
    out = [0] * 8
    for a in range(8):
        bits = [(a >> 2) & 1, (a >> 1) & 1, a & 1]
        nb = [0, 0, 0]
        for i in range(3):
            nb[pi[i]] = bits[i]
        out[a] = (nb[0] << 2) | (nb[1] << 1) | nb[2]
    return tuple(out)


def growth_sigma(pi, m, width):
    """I2's wing symmetry on L_m: S_3 acts on the F_2^3 factor alone and
    fixes label 0 and the copy index."""
    sl = wing_labels(pi)
    n = 1 + width * m
    out = list(range(n))
    for k in range(m):
        for v in range(1, width + 1):
            if v >= len(sl):
                continue
            out[1 + k * width + (v - 1)] = 1 + k * width + (sl[v] - 1)
    return tuple(out)


def legendre_exponent(n, p):
    e, q = 0, p
    while q <= n:
        e += n // q
        q = q * p
    return e


def growth_rule_from_receipt(rsq):
    """THE GENERATOR RULE, EXTRACTED AS DATA from the pinned receipt's own
    declaration string.  Returns (base, exponent, width, text) where the
    family is L_m = {0} + (F_base^exp minus 0) x {1..m} and
    |L_m| = width*m + 1 with width = base**exp - 1.
    [instrument -- mutable]"""
    text = rsq["declarations"]["growth_family"]
    import re
    mo = re.search(r"F_(\d+)\^(\d+)", text)
    base, exp = int(mo.group(1)), int(mo.group(2))
    width = base ** exp - 1
    if MUTANT == "family-rule":
        width = width + 1
    return base, exp, width, text


def growth_member_rule(width, rank, p):
    """The member-selection rule A3's construction states: the smallest m
    whose block set can carry an elementary abelian subgroup of rank `rank`
    at the prime p, i.e. the smallest m with width*m >= rank*p.
    [instrument -- mutable]"""
    m = 1
    while width * m < rank * p:
        m += 1
    if MUTANT == "family-sel":
        return m + 1
    return m


def a1_labels_from_receipt(lcb):
    """A1's label count, DERIVED: I5's nine-label completion family is every
    permutation of the non-zero labels, so its measured size is (n-1)!.
    [instrument -- mutable]"""
    rows = _lcb_fix_rows(lcb)
    members = [r["members"] for r in rows if r["arena"] == "9 labels"][0]
    k, f = 1, 1
    while f < members:
        k += 1
        f = f * k
    if MUTANT == "arena-a1":
        k = k + 1
    return k + 1, members, f


def a2_labels_from_receipt(lcb):
    """A2's label count, DERIVED from I5's own arena rule: the smallest arena
    admitting an injective candidate has rank*p + 1 labels, with the rank
    read from the record-space size p**rank and the prime from the rule
    table.  [instrument -- mutable]"""
    g15 = _lcb_gate(lcb, "G15")["detail"]
    rule = _lcb_gate(lcb, "G44")["detail"][
        "arena_rule_smallest_arena_admitting_injectivity"]
    rank = g15["p_part_exponent_at_16_labels"]
    size = g15["record_space_size"]
    p = None
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23):
        if q ** rank == size:
            p = q
    n = rank * p + 1
    if MUTANT == "arena-a2":
        n = n + 1
    return n, rank, p, rule


def _lcb_gate(lcb, gid):
    for g in lcb["gates"]:
        if g["id"] == gid:
            return g
    raise KeyError(gid)


def _lcb_fix_rows(lcb):
    return _lcb_gate(lcb, "G35")["detail"]["rows"]


def arena_sigma(kind, n, m=0, width=0):
    """The arena's declared chart symmetry.  [instrument -- mutable]"""
    if kind == "pair":
        base = sigma_perm(math.isqrt(n))
        s = tuple(list(base) + list(range(len(base), n)))[:n]
    elif kind == "growth":
        s = growth_sigma((1, 2, 0), m, width)
    else:
        s = tuple([0] + [n - i for i in range(1, n)])
    if MUTANT == "arena-sigma":
        s = pcomp(s, tuple([0, 2, 1] + list(range(3, n))))
    return s


def arena_blocks(kind, n, m=0, width=0, p=0, rank=0):
    """The arena's declared block partition of L minus {0}: the orbits of the
    arena's own completion subgroup.  [instrument -- mutable]"""
    if kind == "pair-full":
        blocks = [tuple(range(1, n))]
    elif kind == "pair-elem":
        blocks = [tuple(range(1 + p * k, 1 + p * (k + 1))) for k in range(rank)]
    elif kind == "growth":
        blocks = [tuple(range(1 + width * k, 1 + width * (k + 1)))
                  for k in range(m)]
    else:
        blocks = [tuple(range(1, n))]
    if MUTANT == "blocks-lax" and len(blocks[0]) > 2:
        blocks = [blocks[0][:-1]] + list(blocks[1:])
    return blocks


def make_arena(name, n, sigma, blocks, note):
    return {"name": name, "n": n, "Sigma": sigma, "blocks": blocks,
            "note": note, "r": len(blocks)}


def arena_coordinates(A):
    """Every coordinate of the declared arena, printed and matched (section
    15): the label count, the basepoint, the symmetry's cycle type and
    order, the block count and the block sizes."""
    S = A["Sigma"]
    ct = sorted(len(c) for c in cycles_of(S))
    order = 1
    x = S
    while x != pident(A["n"]):
        x = pcomp(S, x)
        order += 1
    return {"labels": A["n"], "basepoint_is_fixed_by_Sigma": S[0] == 0,
            "Sigma_order": order,
            "Sigma_cycle_type": ct,
            "blocks": len(A["blocks"]),
            "block_sizes": sorted(len(b) for b in A["blocks"]),
            "blocks_partition_the_moved_labels":
                sorted(x for b in A["blocks"] for x in b) ==
                list(range(1, A["n"])),
            "blocks_are_Sigma_stable":
                all(sorted(S[x] for x in b) == sorted(b) for b in A["blocks"])}


# ===========================================================================
# 5.  THE ATLAS AND ITS COMPLEXES.
# ===========================================================================

def block_cycle(n, blk):
    p = list(range(n))
    for i in range(len(blk)):
        p[blk[i]] = blk[(i + 1) % len(blk)]
    return tuple(p)


def sigma_saturation(S, blk, n):
    U = set(blk)
    while True:
        V = U | {S[x] for x in U}
        if V == U:
            return U
        U = V


def local_sigma(S, blk, n):
    U = sigma_saturation(S, blk, n)
    return tuple(S[i] if i in U else i for i in range(n))


def drawn_is_unique(adm):
    """I3's admission rule: DRAW iff exactly one candidate admits.
    [instrument -- mutable]"""
    if MUTANT == "drawn-lax":
        return len(adm) >= 1
    return len(adm) == 1


def build_atlas(A):
    bump()
    n = A["n"]
    S = A["Sigma"]
    cells = []
    for k, blk in enumerate(A["blocks"]):
        g = block_cycle(n, list(blk))
        Sk = local_sigma(S, blk, n)
        for rule, gen in (("FULL", g), ("REAL", pcomp(Sk, g))):
            grp = cyclic_group(gen, n, 8 * n + 8)
            tab = {}
            for a in range(n):
                for b in range(n):
                    if a == b:
                        continue
                    adm = [pi for pi in grp if pi[a] == b]
                    if drawn_is_unique(adm):
                        tab[(a, b)] = adm[0]
            cells.append({"k": k, "rule": rule, "tab": tab,
                          "group_order": len(grp)})
    return cells


def cell_is_coherent(p1, p2, p3, n):
    """A 2-cell is coherent iff its three drawn maps compose to the identity.
    [instrument -- mutable]"""
    if MUTANT == "coh-lax":
        return True
    return pcomp(p3, pcomp(p2, p1)) == pident(n)


def nerve_edges(cells):
    bump()
    edges, eidx = [], {}
    for ci, c in enumerate(cells):
        for (a, b) in sorted(c["tab"]):
            if a < b:
                eidx[(a, b, ci)] = len(edges)
                edges.append((a, b, ci))
    return edges, eidx


def geometric_cells(A, cells, eidx):
    """The 2-cells of N and the coherent sub-family, built together.
    [instrument -- mutable]"""
    bump()
    n = A["n"]
    bykey = defaultdict(list)
    for ci, c in enumerate(cells):
        bykey[c["k"]].append(ci)
    F, Fcoh = [], []
    for k in sorted(bykey):
        cis = bykey[k]
        verts = set()
        for ci in cis:
            for (a, b) in cells[ci]["tab"]:
                verts.add(a)
                verts.add(b)
        for (a, b, c) in combinations(sorted(verts), 3):
            for c1, c2, c3 in product(cis, repeat=3):
                p1 = cells[c1]["tab"].get((a, b))
                if p1 is None:
                    continue
                p2 = cells[c2]["tab"].get((b, c))
                if p2 is None:
                    continue
                p3 = cells[c3]["tab"].get((c, a))
                if p3 is None:
                    continue
                key = (eidx[(a, b, c1)], eidx[(b, c, c2)], eidx[(a, c, c3)])
                F.append(key)
                if cell_is_coherent(p1, p2, p3, n):
                    Fcoh.append(key)
    if MUTANT == "cell-drop" and F:
        F = F[:-1]
    return F, Fcoh


def two_cell_census_route_2(A, cells):
    """ROUTE 2 to the 2-cell census: a multiplicity product taken from a
    per-block pair-multiplicity dictionary, with no edge index, no triple
    key and nothing shared with the construction loop."""
    bump()
    mult = defaultdict(lambda: defaultdict(int))
    verts = defaultdict(set)
    for c in cells:
        for (a, b) in c["tab"]:
            if a < b:
                mult[c["k"]][(a, b)] += 1
            verts[c["k"]].add(a)
            verts[c["k"]].add(b)
    total = 0
    for k in sorted(mult):
        vs = sorted(verts[k])
        for (a, b, c) in combinations(vs, 3):
            m1 = mult[k].get((a, b), 0)
            if not m1:
                continue
            m2 = mult[k].get((b, c), 0)
            if not m2:
                continue
            m3 = mult[k].get((a, c), 0)
            total += m1 * m2 * m3
    return total


def top_identity(name, V, E, F, b0, b2):
    """The homology identities this instrument uses, evaluated on I3's own
    published cell counts.  [instrument -- mutable]"""
    if MUTANT == "machinery-lax":
        return {"chi": V + E + F, "rank_d2": F + b2, "cycle_rank": E + V,
                "b1": 0}
    chi = V - E + F
    rank2 = F - b2
    cyc = E - V + b0
    return {"chi": chi, "rank_d2": rank2, "cycle_rank": cyc,
            "b1": cyc - rank2}


def components_route_1(nv, pairs):
    """[instrument -- mutable]"""
    if MUTANT == "b0-lax":
        return [list(range(nv))]
    return components_unionfind(nv, pairs)


def boundary_connective(e1, e2, e3):
    """The F_2 boundary of a 2-cell is the XOR of its three 1-cells.  The
    parity-witness gate measures the delta of the OR-connective.
    [instrument -- mutable]"""
    if MUTANT == "parity-lax":
        return (1 << e1) | (1 << e2) | (1 << e3)
    return (1 << e1) ^ (1 << e2) ^ (1 << e3)


def rank_f2_second(rows, want_pivots=False):
    """The SECOND pivot discipline.  [instrument -- mutable]"""
    if MUTANT == "rank-lax":
        return rank_f2_high(rows, want_pivots)
    return rank_f2_low(rows, want_pivots)


def complex_invariants(nv, edges, faces):
    """b_0 by two routes, cycle rank by two routes, rank d_2 by two pivot
    disciplines, b_1 and b_2 derived."""
    bump()
    epairs = [(a, b) for (a, b, _c) in edges]
    comps = components_route_1(nv, epairs)
    b0_uf = len(comps)
    d1 = [(1 << a) ^ (1 << b) for (a, b) in epairs]
    b0_rank = nv - rank_f2_high(d1)
    cyc_forest = spanning_forest_cycle_rank(nv, epairs)
    cyc_euler = len(edges) - (nv - b0_uf)
    rows = [boundary_connective(e1, e2, e3) for (e1, e2, e3) in faces]
    r2a = rank_f2_high(rows)
    r2b = rank_f2_second(rows)
    b1 = cyc_forest - r2a
    b2 = len(faces) - r2a
    return {"V": nv, "E": len(edges), "F": len(faces),
            "b0_route_1_union_find": b0_uf, "b0_route_2_F2_rank": b0_rank,
            "cycle_rank_route_1_spanning_forest": cyc_forest,
            "cycle_rank_route_2_euler": cyc_euler,
            "rank_d2_high_pivot": r2a, "rank_d2_low_pivot": r2b,
            "b0": b0_uf, "b1": b1, "b2": b2,
            "chi_from_cell_counts": nv - len(edges) + len(faces),
            "chi_from_betti": b0_uf - b1 + b2}


# ===========================================================================
# 6.  THE FIVE REGISTERED INVARIANTS.
# ===========================================================================

def overlap_graph(cells):
    und = set()
    for c in cells:
        for (a, b) in c["tab"]:
            und.add((min(a, b), max(a, b)))
    return sorted(und)


def phi_route_2(A, cells):
    """PHI by a second route: the union of the per-cell relations, counted
    cell by cell with a running set rather than from the edge list.
    [instrument -- mutable]"""
    acc = set()
    for c in cells:
        for (a, b) in sorted(c["tab"]):
            if a < b:
                acc.add((a, b))
    n = A["n"]
    if MUTANT == "inv-phi":
        return Fr(len(acc) + 1, n * (n - 1) // 2)
    return Fr(len(acc), n * (n - 1) // 2)


def ncoh_recount(A, cells, edges, eidx, faces_coh):
    """An INDEPENDENT recount of the coherent 2-cells: it rebuilds each
    2-cell's three drawn maps from the EDGE table alone (edge -> its cell and
    its endpoints) and re-composes them, touching nothing the construction
    flagged.  [instrument -- mutable]"""
    bump()
    n = A["n"]
    emap = {}
    for idx, (a, b, ci) in enumerate(edges):
        emap[idx] = (a, b, ci)
    cnt = 0
    for (e1, e2, e3) in faces_coh:
        (a1, b1, c1) = emap[e1]
        (a2, b2, c2) = emap[e2]
        (a3, b3, c3) = emap[e3]
        verts = sorted({a1, b1, a2, b2, a3, b3})
        if len(verts) != 3:
            continue
        x, y, z = verts
        p1 = cells[c1]["tab"].get((x, y))
        p2 = cells[c2]["tab"].get((y, z))
        p3 = cells[c3]["tab"].get((z, x))
        if p1 is None or p2 is None or p3 is None:
            continue
        if pcomp(p3, pcomp(p2, p1)) == pident(n):
            cnt += 1
    if MUTANT == "inv-ncoh":
        cnt = cnt + 1
    return cnt


def spectral_kernel(P, n):
    """dim ker(I - P) over Q by exact rational elimination -- a comparator
    that does not route through the cycle census.  [instrument -- mutable]"""
    mat = [[Fr(1 if i == j else 0) - Fr(1 if P[j] == i else 0)
            for j in range(n)] for i in range(n)]
    d = rat_kernel_dim(mat, n)
    if MUTANT == "inv-spec":
        d = d + 1
    return d


def spectral_anchor_chain(mu1):
    """I2's eigenvalue-1 row, confirmed at every member and every readout:
    the readout carries the eigenvalue 1, so 0 lies in spec(I - E).  The
    walls ride along; they are never re-censused.  [instrument -- mutable]"""
    if MUTANT == "spec-anchor":
        return True
    return mu1 >= 1


def spectral_profile(A):
    bump()
    n = A["n"]
    S = A["Sigma"]
    readouts = []
    x = pcomp(S, pident(n))
    while x != pident(n):
        readouts.append(x)
        x = pcomp(S, x)
    prof = []
    rows = []
    for pi in readouts:
        cl = [len(c) for c in cycles_of(pi)]
        mu = defaultdict(int)
        for L in cl:
            for d in range(1, L + 1):
                if L % d == 0:
                    mu[d] += 1
        mu1_cycles = len(cl)
        mu1_kernel = spectral_kernel(pi, n)
        rows.append({"readout_cycle_type": sorted(cl),
                     "mu_1_by_cycle_count": mu1_cycles,
                     "mu_1_by_exact_kernel_of_I_minus_E": mu1_kernel,
                     "routes_agree": mu1_cycles == mu1_kernel,
                     "eigenvalue_1_present": spectral_anchor_chain(mu1_cycles),
                     "degree_check": sum(d * mu[d] for d in mu if d == 1) +
                                     sum(_phi_euler(d) * mu[d]
                                         for d in mu if d > 1) == n})
        prof.append(tuple(sorted((d, Fr(mu[d], n)) for d in mu)))
    return tuple(sorted(set(prof))), rows


def _phi_euler(d):
    c = 0
    for k in range(1, d + 1):
        if math.gcd(k, d) == 1:
            c += 1
    return c


def dim_route_2(A, cells):
    """The link-vertex count per chart by a second route: built from the
    per-cell tables directly rather than from the overlap edge list.
    [instrument -- mutable]"""
    n = A["n"]
    nb = defaultdict(set)
    for c in cells:
        for (a, b) in c["tab"]:
            nb[a].add(b)
            nb[b].add(a)
    out = {v: len(nb[v]) for v in range(n)}
    if MUTANT == "inv-dim":
        out[0] = out[0] + 1
    return out


def dimension_profile(A, cells):
    bump()
    n = A["n"]
    und = overlap_graph(cells)
    deg = defaultdict(int)
    for (a, b) in und:
        deg[a] += 1
        deg[b] += 1
    dist = defaultdict(int)
    for v in range(n):
        dist[deg[v]] += 1
    prof = tuple(sorted((d, Fr(c, n)) for d, c in dist.items()))
    deg2 = dim_route_2(A, cells)
    agree = all(deg[v] == deg2[v] for v in range(n))
    return prof, agree, {v: deg[v] for v in range(n)}


def b2_complex_choice(inv_all, inv_coh):
    """b_2 is read on N_coh -- the complex that carries the identification
    data (I3).  [instrument -- mutable]"""
    if MUTANT == "inv-b2":
        return inv_all
    return inv_coh


def measure(A):
    """The five registered invariants at one arena, with the supporting
    census."""
    cells = build_atlas(A)
    edges, eidx = nerve_edges(cells)
    F, Fcoh = geometric_cells(A, cells, eidx)
    und = overlap_graph(cells)
    n = A["n"]
    phi1 = Fr(len(und), n * (n - 1) // 2)
    phi2 = phi_route_2(A, cells)
    inv_all = complex_invariants(n, edges, F)
    inv_coh = complex_invariants(n, edges, Fcoh)
    chosen = b2_complex_choice(inv_all, inv_coh)
    ncoh2 = ncoh_recount(A, cells, edges, eidx, Fcoh)
    spec, specrows = spectral_profile(A)
    dimp, dimagree, degs = dimension_profile(A, cells)
    ncoh_den = Fr(len(Fcoh), len(edges)) if edges else None
    b2_den = (Fr(chosen["b2"], len(Fcoh)) if Fcoh else None)
    b2_den_from_ncoh = (Fr(inv_coh["b2"], len(Fcoh)) if Fcoh else None)
    return {
        "two_cells_route_2": two_cell_census_route_2(A, cells),
        "B2_DENSITY_from_N_coh": b2_den_from_ncoh,
        "arena": A["name"], "coordinates": arena_coordinates(A),
        "cells": len(cells),
        "cell_group_orders": [c["group_order"] for c in cells],
        "cell_drawn_pairs": [len(c["tab"]) for c in cells],
        "overlap_edges": len(und), "one_cells": len(edges),
        "two_cells": len(F), "coherent_two_cells": len(Fcoh),
        "coherent_two_cells_independent_recount": ncoh2,
        "N": inv_all, "N_coh": inv_coh,
        "PHI": phi1, "PHI_route_2": phi2,
        "NCOH_DENSITY": ncoh_den,
        "SPECTRAL_PROFILE": spec, "spectral_rows": specrows,
        "DIMENSION_PROFILE": dimp, "dimension_routes_agree": dimagree,
        "B2_DENSITY": b2_den,
        "degrees": degs,
        "_cells": cells, "_edges": edges, "_eidx": eidx, "_F": F,
        "_Fcoh": Fcoh,
    }


# ===========================================================================
# 7.  THE MAPS BETWEEN MEMBERS.
# ===========================================================================

def sigma_orbits(S, n):
    grp = []
    x = pident(n)
    while True:
        grp.append(x)
        x = pcomp(S, x)
        if x == pident(n):
            break
    orbs = []
    seen = set()
    for i in range(n):
        if i in seen:
            continue
        o = sorted({g[i] for g in grp})
        seen.update(o)
        orbs.append(tuple(o))
    return orbs


def build_embedding(A, B):
    """Constructs an admissible arena morphism A -> B if one exists, by the
    declared criterion.  Equivariance forces orbits to map bijectively onto
    orbits of the SAME size; the search matches orbits inside blocks.
    Returns (iota or None, reason).  [instrument -- mutable]"""
    bump()
    n, m = A["n"], B["n"]
    SA, SB = A["Sigma"], B["Sigma"]
    oa = sigma_orbits(SA, n)
    ob = sigma_orbits(SB, m)
    sa = sorted(len(o) for o in oa)
    sb = sorted(len(o) for o in ob)
    need = defaultdict(int)
    for s in sa:
        need[s] += 1
    have = defaultdict(int)
    for s in sb:
        have[s] += 1
    missing = sorted(s for s in need if need[s] > have.get(s, 0))
    if missing:
        return None, ("ORBIT-SIZE-UNAVAILABLE: <Sigma_A> has orbit sizes %s "
                      "with multiplicities the target cannot supply at sizes "
                      "%s" % (canon(sorted(set(sa))), canon(missing)))
    bigA = max(len(b) for b in A["blocks"])
    bigB = max(len(b) for b in B["blocks"])
    if bigA > bigB:
        return None, ("BLOCK-WIDTH-DECREASES: the largest source block has "
                      "%d labels and the largest target block has %d"
                      % (bigA, bigB))
    if len(A["blocks"]) > len(B["blocks"]):
        return None, ("BLOCK-COUNT-DECREASES: %d source blocks, %d target "
                      "blocks" % (len(A["blocks"]), len(B["blocks"])))
    iota = list(range(n))
    used = set()
    for k, blk in enumerate(A["blocks"]):
        tgt = B["blocks"][k]
        if len(blk) != len(tgt):
            return None, ("BLOCK-WIDTH-MISMATCH: source block %d has %d "
                          "labels, target block %d has %d"
                          % (k, len(blk), k, len(tgt)))
        for i, x in enumerate(blk):
            iota[x] = tgt[i]
            used.add(tgt[i])
    iota[0] = 0
    iota = tuple(iota)
    if MUTANT == "map-func":
        iota = tuple([iota[0], iota[2], iota[1]] + list(iota[3:]))
    if len(set(iota)) != n:
        return None, "NOT-INJECTIVE"
    if any(iota[SA[x]] != SB[iota[x]] for x in range(n)):
        return None, "NOT-EQUIVARIANT: iota . Sigma_A != Sigma_B . iota"
    if iota[0] != 0:
        return None, "BASEPOINT-NOT-PRESERVED"
    return iota, "CONSTRUCTED"


def morphism_exists(iota):
    """[instrument -- mutable]"""
    if MUTANT == "embed-lax":
        return True
    if MUTANT == "embed-blind":
        return False
    return iota is not None


# ===========================================================================
# 8.  THE STABILISATION INSTRUMENT AND THE VERDICT.
# ===========================================================================

def stabilisation_window():
    """[instrument -- mutable]"""
    if MUTANT == "k-window":
        return 1
    return DECL["K"]


def is_constant_on_window(values, K):
    tail = values[-K:]
    if any(v is None for v in tail):
        return False
    return all(v == tail[0] for v in tail)


def scalar_mode(values):
    K = stabilisation_window()
    tail = values[-K:]
    if any(v is None for v in tail):
        return "UNDEFINED-AT-A-MEMBER"
    if all(v == tail[0] for v in tail):
        return "CONSTANT"
    inc = all(tail[i] < tail[i + 1] for i in range(len(tail) - 1))
    dec = all(tail[i] > tail[i + 1] for i in range(len(tail) - 1))
    if inc:
        return "STRICTLY-INCREASING"
    if dec:
        return "STRICTLY-DECREASING"
    return "NON-MONOTONE"


def profile_mode(values):
    K = stabilisation_window()
    tail = values[-K:]
    if any(v is None for v in tail):
        return "UNDEFINED-AT-A-MEMBER"
    if all(v == tail[0] for v in tail):
        return "CONSTANT"
    supports = [tuple(sorted(_support(v))) for v in tail]
    if all(s == supports[0] for s in supports):
        return "SUPPORT-CONSTANT-WEIGHTS-MOVING"
    return "SUPPORT-MOVING"


def _support(v):
    out = []
    if isinstance(v, tuple) and v and isinstance(v[0], tuple) and \
            v and isinstance(v[0][0], tuple):
        for prof in v:
            for (d, _w) in prof:
                out.append(d)
        return set(out)
    for item in v:
        out.append(item[0])
    return set(out)


def trajectory_rows(family, meas):
    """The 5 x K trajectory table.  [instrument -- mutable]"""
    names = [row[0] for row in DECL["registered_invariants"]]
    if MUTANT == "row-drop":
        names = names[:-1]
    rows = {}
    for nm in names:
        rows[nm] = [meas[A["name"]][nm] for A in family]
    return rows


def verdict_head(stabilised):
    """[instrument -- mutable]"""
    flip = (MUTANT == "verdict-flip")
    hit = len(stabilised) > 0
    if flip:
        hit = not hit
    return "R1-STABILIZES-AT" if hit else \
        "R1-NO-CONTINUUM-LIMIT-AT-THIS-SUBSTRATE"


def qualifier_source(computed):
    """Every qualifier is COMPUTED from the trajectory table.
    [instrument -- mutable]"""
    if MUTANT == "qual-flip":
        return "ALL-FIVE-CONSTANT"
    return computed


def gateway_member(members_with_phi_lt_1):
    """[instrument -- mutable]"""
    if MUTANT == "gateway-lax":
        return "A3"
    return members_with_phi_lt_1[0] if members_with_phi_lt_1 else None


# ===========================================================================
# 9.  MAIN.
# ===========================================================================

def measured_datum_before_freeze():
    """[instrument -- mutable]"""
    if MUTANT == "freeze-lax":
        bump()


def family_cap(built, target):
    """The family length actually built, against the declared target.  No
    silent caps: the cap and its reason are returned.  [instrument --
    mutable]"""
    if MUTANT == "cap-lax":
        return built[:-1], "SILENT"
    return built, ("NO-CAP" if len(built) == target else "CAPPED")


def regenerate_fresh(base, exp, width, m, rank, p):
    """The extracted rule, evaluated FRESH -- the memo is bypassed, and the
    bypass is counted (RUNBOOK section 14 addendum #185).  [instrument --
    mutable]"""
    key = ("regen", base, exp, m)
    CACHE_STATS["lookups"] += 1
    if MUTANT == "regen-cache":
        if key in CACHE:
            CACHE_STATS["hits"] += 1
            CACHE_STATS["selftest_hits"] += 1
            return CACHE[key]
    else:
        CACHE_STATS["bypasses"] += 1
    n = width * m + 1
    blocks = arena_blocks("growth", n, m=m, width=width)
    sigma = arena_sigma("growth", n, m=m, width=width)
    CACHE[key] = (n, blocks, sigma)
    return n, blocks, sigma


def positive_control_family(A3):
    """[instrument -- mutable]"""
    if MUTANT == "pos-lax":
        return [A3, A3, make_arena("A3-perturbed", A3["n"], A3["Sigma"],
                                   A3["blocks"][:-1], "perturbed"), ]
    return [A3, A3, A3]


def negative_control_estimators(meas, family):
    """I3's EXCLUDED raw estimators: the unnormalised counts.  [instrument --
    mutable]"""
    out = {}
    for A in family:
        m = meas[A["name"]]
        if MUTANT == "neg-lax":
            out[A["name"]] = {"RAW_OVERLAP": m["PHI"],
                              "RAW_COHERENT": m["NCOH_DENSITY"],
                              "RAW_MU1": m["SPECTRAL_PROFILE"],
                              "RAW_CHARTS": m["DIMENSION_PROFILE"],
                              "RAW_B2": m["B2_DENSITY"]}
        else:
            out[A["name"]] = {
                "RAW_OVERLAP": m["overlap_edges"],
                "RAW_COHERENT": m["coherent_two_cells"],
                "RAW_MU1": m["spectral_rows"][0]["mu_1_by_cycle_count"],
                "RAW_CHARTS": m["coordinates"]["labels"],
                "RAW_B2": m["N_coh"]["b2"]}
    return out


def scramble_shift():
    """[instrument -- mutable]"""
    if MUTANT == "scramble-lax":
        return 0
    seed = int(hashlib.sha256(
        json.dumps(DECL["controls"], sort_keys=True).encode()).hexdigest(), 16)
    return 1 + (seed % 7)


def scramble_cells(cells, shift):
    out = []
    moved = 0
    for c in cells:
        ks = sorted(c["tab"])
        vals = [c["tab"][k] for k in ks]
        s = (shift % len(vals)) if vals else 0
        vals2 = vals[s:] + vals[:s]
        moved += sum(1 for i in range(len(vals)) if vals[i] != vals2[i])
        out.append({"k": c["k"], "rule": c["rule"], "tab": dict(zip(ks, vals2)),
                    "group_order": c["group_order"]})
    return out, moved


def discrimination_family():
    """The WIDENING family W_s: one block of s labels, Sigma the block
    reversal.  A growth rule that is NOT a disjoint addition.
    [instrument -- mutable]"""
    sizes = [5, 6, 7]
    if MUTANT == "disc-lax":
        sizes = [5, 5, 5]
    out = []
    for s in sizes:
        n = s + 1
        sg = arena_sigma("reversal", n)
        out.append(make_arena("W%d" % s, n, sg, arena_blocks("widen", n),
                              "the widening discrimination family"))
    return out


def selftest_tested_set(family, stabilised):
    """The symmetry self-test's tested set is fixed by DECLARATION -- the
    whole family -- and never selected by the verdicts under audit.
    [instrument -- mutable]"""
    if MUTANT == "selftest-select":
        return [A for A in family if A["name"] in stabilised]
    return list(family)


def robustness_indices(width, rank, primes):
    """The alternative reading of the family index: the members the growth
    rule selects at the NEXT declared primes.  An arena coordinate, swept.
    [instrument -- mutable]"""
    if MUTANT == "robust-lax":
        return []
    return [growth_member_rule(width, rank, p) for p in primes]


def relabel_arena(A, tau):
    """The arena transported by a relabelling tau of its labels.  The block's
    DECLARED CYCLIC ORDER is transported with it -- the arena carries its
    labelling, so a relabelling moves the order too and the atlas is rebuilt
    inside the transported arena rather than renamed."""
    n = A["n"]
    ti = pinv(tau)
    S = tuple(tau[A["Sigma"][ti[i]]] for i in range(n))
    blocks = [tuple(tau[x] for x in b) for b in A["blocks"]]
    return make_arena(A["name"] + "-relabelled", n, S, blocks, "relabelled")


def run():
    global _FROZEN
    prog("declarations")
    measured_datum_before_freeze()
    gate("G01", "measurement",
         "THE DECLARATIONS ARE FROZEN BEFORE ANY MEASURED DATUM.  Every "
         "measured datum of this unit passes through one counter, and that "
         "counter is measured to be ZERO at this gate, which sits after the "
         "declaration block and before the first construction",
         _MEASURED == 0, {"measured_data_evaluated": _MEASURED})
    _FROZEN = True

    prog("inheritance")
    data, comp_rows = load_inheritance()
    rows = r0_rows()
    gate("G02", "measurement",
         "THE R0 INHERITANCE IS VERIFIED AT RUN TIME AND THE CENSUS IS "
         "COMPLETE: every row of the founding pin's seven-row table is "
         "hashed here and compared against the pin's own recorded sha256-12, "
         "the charter and both pins included.  The census size is computed "
         "against the pin's declared row count, so a dropped row is caught "
         "even when every surviving hash matches",
         len(rows) == 8 and all(a["passed"] for a in ANCHORS
                                if a["id"].startswith("A-R0-")
                                or a["id"] == "A-R1-PIN"),
         {"rows_censused": len(rows),
          "row_ids": [r[0] for r in rows],
          "anchors_passed": sum(1 for a in ANCHORS if a["passed"])})

    mismatches = sorted(c["id"] for c in comp_rows if not c["matches"])
    gate("G03", "measurement",
         "THE COMPANION-ARTIFACT CENSUS IS COMPLETE AND ITS MEASURED "
         "MISMATCH SET IS REPORTED EXACTLY.  R0's I2, I3 and I6 rows name "
         "companion artifacts in parentheses; every one of them is hashed "
         "here and the set whose recorded hash does NOT reproduce is "
         "computed and printed rather than smoothed.  The gate is on the "
         "CENSUS being complete -- a dropped companion is caught -- and the "
         "mismatch set is carried as a finding for the adjudicator, because "
         "no number of this unit is read from a companion artifact",
         len(comp_rows) == 8,
         {"companions_censused": len(comp_rows),
          "mismatching": mismatches,
          "matching": sorted(c["id"] for c in comp_rows if c["matches"])})
    if mismatches:
        disclose("X-COMPANION-HASH",
                 "R0's parenthetical companion hashes for the two v13 PAPERS "
                 "do not reproduce against the artifacts on disk.  What this "
                 "instrument measures is exactly that: the declared and the "
                 "computed sha256-12 of each companion, and the set on which "
                 "they differ.  The rows' CARRYING receipts -- the primary "
                 "key of every R0 row -- all verify, all six other "
                 "companions verify, and no number of this unit is read from "
                 "a paper, so the run proceeds and the delta is reported "
                 "here rather than silently ignored.",
                 [c for c in comp_rows if not c["matches"]])

    rsq, top, lcb, tb3 = data["I2"], data["I3"], data["I5"], data["I6"]

    # ---- the growth rule, extracted as data --------------------------------
    prog("growth rule")
    base, exp, width, ruletext = growth_rule_from_receipt(rsq)
    thresholds = rsq["tables"]["scale_thresholds"]
    rank = None
    for row in thresholds:
        if rank is None:
            rank = row["d3_elementary_abelian_threshold"] - 1
            rank = rank // row["p"]
    sel_rows = []
    for row in thresholds:
        p = row["p"]
        m = growth_member_rule(width, rank, p)
        sel_rows.append({
            "p": p, "m_computed": m, "m_declared": row["d3_growth_family_member"],
            "labels_computed": width * m + 1,
            "labels_declared": row["d3_growth_family_labels"],
            "elementary_threshold_computed": rank * p + 1,
            "elementary_threshold_declared":
                row["d3_elementary_abelian_threshold"],
            "divisibility_threshold_computed":
                _divisibility_threshold(p, rank),
            "divisibility_threshold_declared":
                row["d3_divisibility_threshold"]})
        anchor("A-RSQ-M-%d" % p, "I2 scale_thresholds",
               "growth family member at p=%d" % p,
               row["d3_growth_family_member"], m)
        anchor("A-RSQ-N-%d" % p, "I2 scale_thresholds",
               "growth family labels at p=%d" % p,
               row["d3_growth_family_labels"], width * m + 1)
        anchor("A-RSQ-EA-%d" % p, "I2 scale_thresholds",
               "elementary abelian threshold at p=%d" % p,
               row["d3_elementary_abelian_threshold"], rank * p + 1)
        anchor("A-RSQ-DV-%d" % p, "I2 scale_thresholds",
               "divisibility threshold at p=%d" % p,
               row["d3_divisibility_threshold"],
               _divisibility_threshold(p, rank))
    tb3_labels = tb3["tables"]["base_declaration"]["carrier"][
        "system_triple_dimension"]
    anchor("A-TB3-WIDTH", "I6 base_declaration",
           "TB3's moved labels = the growth family's block width",
           tb3_labels - 1, width)
    anchor("A-TB3-L1", "I2 growth_family declaration",
           "L_1 is TB3's native arena", tb3_labels, width * 1 + 1)
    anchor("A-TB3-WINGS", "I6 base_declaration", "wings", 3,
           tb3["tables"]["base_declaration"]["carrier"]["wings"])

    gate("G04", "measurement",
         "THE GENERATOR RULE IS DATA, NOT A GUESS: the family L_m is read "
         "out of the pinned receipt's own declaration string, its block "
         "width is EXTRACTED from that string (base and exponent parsed, "
         "width = base**exp - 1) rather than typed, and the extracted rule "
         "is required to reproduce the receipt's whole scale-threshold table "
         "-- member, labels, elementary-abelian threshold and divisibility "
         "threshold -- at every one of its declared primes.  The width is "
         "cross-anchored against I6's own moved-label count",
         all(r["m_computed"] == r["m_declared"] and
             r["labels_computed"] == r["labels_declared"] and
             r["elementary_threshold_computed"] ==
             r["elementary_threshold_declared"] and
             r["divisibility_threshold_computed"] ==
             r["divisibility_threshold_declared"] for r in sel_rows)
         and len(sel_rows) == len(thresholds) and width == tb3_labels - 1,
         {"rule_text": ruletext, "base": base, "exponent": exp,
          "block_width": width, "rank": rank, "rows": sel_rows})

    # ---- the arenas --------------------------------------------------------
    prog("arenas")
    n1, members1, fact1 = a1_labels_from_receipt(lcb)
    A1 = make_arena("A1", n1, arena_sigma("pair", n1),
                    arena_blocks("pair-full", n1),
                    "I5's nine-label completion arena")
    n2, rank2, p2, arenarule = a2_labels_from_receipt(lcb)
    A2 = make_arena("A2", n2, arena_sigma("pair", n2),
                    arena_blocks("pair-elem", n2, p=p2, rank=rank2),
                    "I5's sixteen-label successor arena (G15)")
    p3 = 7
    m3 = growth_member_rule(width, rank, p3)
    n3, blocks3, sig3 = regenerate_fresh(base, exp, width, m3, rank, p3)
    A3 = make_arena("A3", n3, sig3, blocks3,
                    "I2's grown arena L_%d" % m3)

    fix9 = [r for r in _lcb_fix_rows(lcb) if r["arena"] == "9 labels"][0]
    fix16 = [r for r in _lcb_fix_rows(lcb)
             if r["arena"].startswith("16 labels")][0]
    anchor("A-LCB-A1-MEMBERS", "I5 G35", "9-label completion family size",
           fix9["members"], math.factorial(n1 - 1))
    anchor("A-LCB-A1-FIX", "I5 G35", "fix(delta) at 9 labels",
           fix9["delta_fixed_points"], _delta_fixed_points(A1))
    anchor("A-LCB-A2-ORDER", "I5 G15", "the 16-label witness subgroup order",
           _lcb_gate(lcb, "G15")["detail"]["witness_subgroup_order"],
           _elementary_order(A2))
    anchor("A-LCB-A2-FIX", "I5 G35", "fix(delta) at the 16-label subgroup",
           fix16["delta_fixed_points"], _delta_fixed_points_sub(A2))
    anchor("A-LCB-A2-PPART", "I5 G15", "p-part exponent at 16 labels",
           _lcb_gate(lcb, "G15")["detail"]["p_part_exponent_at_16_labels"],
           legendre_exponent(n2 - 1, p2))
    anchor("A-LCB-A1-PPART", "I5 G15", "p-part exponent at 9 labels",
           _lcb_gate(lcb, "G15")["detail"]["p_part_exponent_at_9_labels"],
           legendre_exponent(n1 - 1, p2))
    anchor("A-LCB-ARENARULE-5", "I5 G44",
           "smallest arena admitting an injective candidate at p=5",
           arenarule["5"], _smallest_injective(5, rank2))
    anchor("A-LCB-ARENARULE-7", "I5 G44",
           "smallest arena admitting an injective candidate at p=7",
           arenarule["7"], _smallest_injective(7, rank2))
    anchor("A-RSQ-A3-LABELS", "I2 scale_thresholds",
           "the grown arena's label count at p=7",
           [r["d3_growth_family_labels"] for r in thresholds
            if r["p"] == 7][0], n3)

    gate("G05", "measurement",
         "EVERY ARENA IS REBUILT FROM PINNED DATA AND EVERY LABEL COUNT IS "
         "DERIVED, NEVER TYPED.  A1's nine labels come from inverting the "
         "factorial of I5's measured completion-family size; A2's sixteen "
         "come from I5's own arena rule rank*p + 1 with the rank read off "
         "the record-space size and the prime solved for; A3's forty-three "
         "come from the extracted growth rule at the member the rule itself "
         "selects.  Each rebuild is then anchored against the pinned "
         "receipts' measured quantities -- family size, fixed-point count, "
         "witness-subgroup order, p-part exponents and the arena rule at two "
         "primes",
         n1 == 9 and n2 == 16 and members1 == fact1 and
         all(a["passed"] for a in ANCHORS if a["id"].startswith("A-LCB-")),
         {"A1": {"labels": n1, "from": "members = (n-1)! = %d" % members1},
          "A2": {"labels": n2, "rank": rank2, "prime": p2,
                 "from": "rank*p + 1"},
          "A3": {"labels": n3, "m": m3, "from": "width*m + 1"}})

    # ---- the regeneration self-test, evaluated fresh -----------------------
    before = dict(CACHE_STATS)
    n3b, blocks3b, sig3b = regenerate_fresh(base, exp, width, m3, rank, p3)
    after = dict(CACHE_STATS)
    gate("G06", "measurement",
         "THE EXTRACTED RULE REGENERATES A3 FROM SCRATCH BEFORE A4 IS BUILT, "
         "AND THE SELF-TEST EVALUATES FRESH.  The second evaluation bypasses "
         "the memo, the bypass count is measured to have risen and the "
         "self-test's cache-hit count is measured to be zero against a "
         "non-zero lookup count, so a self-test that read the cache is "
         "caught.  The regenerated label set, block partition and symmetry "
         "are compared to A3's coordinate by coordinate",
         (n3b, blocks3b, sig3b) == (n3, blocks3, sig3)
         and after["bypasses"] > before["bypasses"]
         and after["selftest_hits"] == 0 and after["lookups"] > 0,
         {"regenerated_labels": n3b, "regenerated_blocks": len(blocks3b),
          "cache_lookups": after["lookups"], "cache_hits": after["hits"],
          "cache_bypasses": after["bypasses"],
          "selftest_cache_hits": after["selftest_hits"]})

    # ---- A4, A5 by the same rule ------------------------------------------
    A45 = []
    for step in (1, 2):
        m = m3 + step
        n, blocks, sig = regenerate_fresh(base, exp, width, m, rank, p3)
        A45.append(make_arena("A%d" % (3 + step), n, sig, blocks,
                              "the growth family's next member L_%d" % m))
    family_full = [A1, A2, A3] + A45
    family, cap = family_cap(family_full, DECL["family_target"])
    gate("G07", "measurement",
         "THE FAMILY LENGTH IS COMPUTED AND NO CAP IS SILENT.  The built "
         "length is measured against the pin's declared target of five and "
         "the cap state is derived from that comparison, not asserted; a "
         "truncation is caught here and would be carried into the verdict's "
         "window qualifier",
         len(family) == DECL["family_target"] and cap == "NO-CAP",
         {"target": DECL["family_target"], "built": len(family),
          "cap_state": cap,
          "members": [{"name": A["name"], "labels": A["n"],
                       "blocks": A["r"]} for A in family]})

    TABLES["family"] = {A["name"]: dict(arena_coordinates(A),
                                        note=A["note"]) for A in family}
    coords_ok = all(arena_coordinates(A)["blocks_partition_the_moved_labels"]
                    and arena_coordinates(A)["basepoint_is_fixed_by_Sigma"]
                    for A in family)
    gate("G08", "measurement",
         "THE DECLARED ARENA IS PRINTED AND MATCHED AT EVERY COORDINATE "
         "(RUNBOOK section 15).  For every member the label count, the "
         "basepoint's fixedness under the symmetry, the symmetry's order and "
         "cycle type, the block count, the block sizes, whether the blocks "
         "partition the moved labels and whether they are symmetry-stable "
         "are all computed and printed; the comparison across members is "
         "made on that table and never on a name",
         coords_ok and len(TABLES["family"]) == len(family),
         TABLES["family"])

    # ---- the maps ----------------------------------------------------------
    prog("maps")
    steps = []
    for i in range(len(family) - 1):
        iota, reason = build_embedding(family[i], family[i + 1])
        steps.append({"step": "%s->%s" % (family[i]["name"],
                                          family[i + 1]["name"]),
                      "admissible": morphism_exists(iota),
                      "reason": reason,
                      "witness": list(iota) if iota is not None else None})
    live = [i for i, s in enumerate(steps)
            if s["admissible"] and s["witness"] is not None]
    func_rows = []
    for i in live:
        if i + 1 in live:
            f, _ = build_embedding(family[i], family[i + 1])
            g, _ = build_embedding(family[i + 1], family[i + 2])
            h = tuple(g[f[x]] for x in range(family[i]["n"]))
            direct = tuple(range(family[i]["n"]))
            comp_ok = all(h[x] == g[f[x]] for x in range(family[i]["n"]))
            idn = build_embedding(family[i], family[i])[0]
            func_rows.append({
                "at": "%s->%s->%s" % (family[i]["name"],
                                      family[i + 1]["name"],
                                      family[i + 2]["name"]),
                "composition_is_equivariant":
                    all(h[family[i]["Sigma"][x]] ==
                        family[i + 2]["Sigma"][h[x]]
                        for x in range(family[i]["n"])),
                "composition_is_injective":
                    len(set(h)) == family[i]["n"],
                "identity_is_the_identity": idn == direct,
                "composition_agrees_with_the_maps": comp_ok})
    nonfunc = [s for s in steps if not s["admissible"]]
    func_qual = ("FAMILY-FUNCTORIAL" if not nonfunc else
                 "FAMILY-NON-FUNCTORIAL-AT-%d-OF-%d-STEPS"
                 % (len(nonfunc), len(steps)))
    gate("G09", "measurement",
         "FUNCTORIALITY IS GATED, NOT ASSUMED, AND THE CRITERION HAS TEETH "
         "IN BOTH DIRECTIONS.  The admissible-morphism criterion is applied "
         "at every consecutive step; where a morphism exists it is "
         "CONSTRUCTED and its equivariance, injectivity, basepoint "
         "preservation, identity and composition are each measured; where "
         "none exists the obstruction is NAMED from the measured orbit and "
         "block data.  The criterion is measured to admit some steps and to "
         "refuse others, so it is not a constant function",
         len(steps) == len(family) - 1
         and any(s["admissible"] for s in steps)
         and any(not s["admissible"] for s in steps)
         and all(r["composition_is_equivariant"] and
                 r["composition_is_injective"] and
                 r["identity_is_the_identity"] and
                 r["composition_agrees_with_the_maps"] for r in func_rows),
         {"steps": steps, "functoriality_rows": func_rows,
          "qualifier": func_qual})
    TABLES["maps"] = {"steps": steps, "functoriality": func_rows,
                      "qualifier": func_qual}

    # ---- the machinery, cross-checked against I3 ---------------------------
    prog("machinery vs I3")
    ref = top["tables"]["q1_invariants"][
        "the declared base at a fully symmetric setting"]
    mrows = []
    for label, blk in (("N", ref["the_nerve_N"]),
                       ("N_coh", ref["the_coherent_sub_nerve"])):
        V, E, F = blk["V"], blk["E"], blk["F"]
        ident = top_identity(label, V, E, F, blk["b0"], blk["b2"])
        chi, rank2 = ident["chi"], ident["rank_d2"]
        cyc, b1 = ident["cycle_rank"], ident["b1"]
        mrows.append({"complex": label, "chi_computed": chi,
                      "chi_declared": blk["chi_from_cell_counts"],
                      "rank_d2_computed": rank2,
                      "rank_d2_declared": blk["rank_d2_route_1_high_pivot"],
                      "cycle_rank_computed": cyc,
                      "cycle_rank_declared":
                          blk["cycle_rank_route_1_spanning_forest"],
                      "b1_computed": b1, "b1_declared": blk["b1"]})
        anchor("A-TOP-CHI-" + label, "I3 q1_invariants",
               "chi of " + label, blk["chi_from_cell_counts"], chi)
        anchor("A-TOP-RANK-" + label, "I3 q1_invariants",
               "rank d_2 of " + label, blk["rank_d2_route_1_high_pivot"],
               rank2)
        anchor("A-TOP-CYC-" + label, "I3 q1_invariants",
               "cycle rank of " + label,
               blk["cycle_rank_route_1_spanning_forest"], cyc)
        anchor("A-TOP-B1-" + label, "I3 q1_invariants",
               "b_1 of " + label, blk["b1"], b1)
    tv = top["tables"]["base"]
    coordcount = (tv["checkpoints"] - 1) * (ref["the_nerve_N"]["V"] - 1)
    anchor("A-TOP-COORD", "I3 q1_invariants",
           "(read times - 1)(charts - 1)",
           ref["the_coordinate_count_T_minus_1_times_V_minus_1"], coordcount)
    gate("G10", "measurement",
         "THIS UNIT'S HOMOLOGY MACHINERY REPRODUCES I3's PUBLISHED "
         "INVARIANTS FROM I3's PUBLISHED CELL COUNTS.  The identities this "
         "instrument uses -- chi = V - E + F, rank d_2 = F - b_2, cycle rank "
         "= E - V + b_0, b_1 = cycle rank - rank d_2 -- are evaluated here "
         "on the pinned receipt's own V, E, F, b_0 and b_2 for BOTH the "
         "nerve and its coherent sub-nerve, and each result is anchored "
         "exit-1 against the receipt's independently recorded value.  This "
         "is the machinery's external calibration; nothing of I3's atlas is "
         "rebuilt here and nothing is imported",
         all(r["chi_computed"] == r["chi_declared"] and
             r["rank_d2_computed"] == r["rank_d2_declared"] and
             r["cycle_rank_computed"] == r["cycle_rank_declared"] and
             r["b1_computed"] == r["b1_declared"] for r in mrows)
         and coordcount == ref[
             "the_coordinate_count_T_minus_1_times_V_minus_1"],
         {"rows": mrows, "coordinate_count": coordcount})

    # ---- the measurements --------------------------------------------------
    prog("invariants at %d members" % len(family))
    meas = {}
    for A in family:
        prog("  " + A["name"])
        meas[A["name"]] = measure(A)

    ok_atlas = True
    atlas_rows = []
    for A in family:
        m = meas[A["name"]]
        sym = True
        invc = True
        for c in m["_cells"]:
            for (a, b), pi in c["tab"].items():
                if (b, a) not in c["tab"]:
                    sym = False
                elif c["tab"][(b, a)] != pinv(pi):
                    invc = False
        e_from_pairs = sum(len(c["tab"]) for c in m["_cells"]) // 2
        atlas_rows.append({"arena": A["name"], "drawn_relation_symmetric": sym,
                           "drawn_maps_inverse_consistent": invc,
                           "one_cells": m["one_cells"],
                           "one_cells_from_the_pair_census": e_from_pairs,
                           "two_cells_route_1": m["two_cells"],
                           "two_cells_route_2": m["two_cells_route_2"],
                           "census_agrees": e_from_pairs == m["one_cells"]
                           and m["two_cells"] == m["two_cells_route_2"]})
        ok_atlas = (ok_atlas and sym and invc
                    and e_from_pairs == m["one_cells"]
                    and m["two_cells"] == m["two_cells_route_2"])
    gate("G11", "measurement",
         "THE ATLAS IS WELL FORMED AT EVERY MEMBER AND ITS CELL CENSUSES ARE "
         "TAKEN TWICE: the drawn relation is measured SYMMETRIC, the drawn "
         "map of the reversed pair is measured to be the inverse of the "
         "drawn map, the 1-cell census taken from the ordered pair tables "
         "agrees with the census taken from the unordered edge list, and the "
         "2-cell census taken by the construction loop agrees with a "
         "multiplicity-product census taken from a per-block pair-"
         "multiplicity dictionary that shares no edge index, no triple key "
         "and no intermediate with it.  A dropped or duplicated cell of "
         "either degree is caught by the second count",
         ok_atlas, {"rows": atlas_rows})

    # two-route / two-pivot agreement
    routes = []
    for A in family:
        m = meas[A["name"]]
        for label in ("N", "N_coh"):
            blk = m[label]
            routes.append({
                "arena": A["name"], "complex": label,
                "b0_routes_agree": blk["b0_route_1_union_find"] ==
                                   blk["b0_route_2_F2_rank"],
                "cycle_rank_routes_agree":
                    blk["cycle_rank_route_1_spanning_forest"] ==
                    blk["cycle_rank_route_2_euler"],
                "rank_d2_pivots_agree": blk["rank_d2_high_pivot"] ==
                                        blk["rank_d2_low_pivot"],
                "chi_agrees": blk["chi_from_cell_counts"] ==
                              blk["chi_from_betti"]})
    gate("G12", "measurement",
         "COMPONENTS AND CYCLE RANK ARE COMPUTED BY TWO GENUINELY "
         "INDEPENDENT ROUTES AT EVERY COMPLEX OF EVERY MEMBER -- union-find "
         "over the drawn links against |V| minus the F_2 rank of the "
         "1-boundary, and a breadth-first spanning forest that performs no "
         "elimination at all against the Euler count -- and they agree "
         "everywhere",
         all(r["b0_routes_agree"] and r["cycle_rank_routes_agree"]
             for r in routes), {"rows": routes})
    probe_rows = [0b0110, 0b0011, 0b1100]
    hi_r, hi_p = rank_f2_high(probe_rows, True)
    lo_r, lo_p = rank_f2_low(probe_rows, True)
    sec_r, sec_p = rank_f2_second(probe_rows, True)
    gate("G13", "measurement",
         "THE 2-BOUNDARY RANK IS COMPUTED UNDER TWO PIVOT DISCIPLINES -- "
         "highest-bit pivots taking the rows forward, lowest-bit pivots "
         "taking them in reverse -- and they agree at every complex of every "
         "member.  These are two pivot disciplines on one rank and are "
         "described as that, never as two independent routes; so the gate "
         "also measures, on a declared probe, that the second discipline "
         "really is the other one: its PIVOT SET on the probe is required to "
         "equal the low-pivot set and to DIFFER from the high-pivot set, "
         "which is what a replacement of one discipline by the other breaks",
         all(r["rank_d2_pivots_agree"] for r in routes)
         and sec_p == lo_p and lo_p != hi_p and sec_r == lo_r == hi_r,
         {"rows": routes, "probe": probe_rows,
          "high_pivot_rank": hi_r, "high_pivot_set": hi_p,
          "low_pivot_rank": lo_r, "low_pivot_set": lo_p,
          "second_discipline_rank": sec_r,
          "second_discipline_pivot_set": sec_p})
    disclose("X-CHI-IDENTITY",
             "chi from the cell counts and chi from the Betti numbers agree "
             "at every complex of every member.  This is an algebraic "
             "identity in the ranks, not a second route, and is recorded as "
             "a disclosure.",
             {"rows": [{"arena": r["arena"], "complex": r["complex"],
                        "agrees": r["chi_agrees"]} for r in routes]})

    # boundary parity witness
    par_rows = []
    for A in family:
        m = meas[A["name"]]
        xor_rows = [(1 << e1) ^ (1 << e2) ^ (1 << e3) for (e1, e2, e3)
                    in m["_Fcoh"]]
        or_rows = [(1 << e1) | (1 << e2) | (1 << e3) for (e1, e2, e3)
                   in m["_Fcoh"]]
        d1d2 = all(_d1d2_is_zero(m["_edges"], f) for f in m["_Fcoh"])
        distinct = all(len({e1, e2, e3}) == 3 for (e1, e2, e3) in m["_Fcoh"])
        par_rows.append({"arena": A["name"],
                         "rank_with_XOR": rank_f2_high(xor_rows),
                         "rank_with_OR": rank_f2_high(or_rows),
                         "delta_on_the_realised_cells":
                             rank_f2_high(or_rows) - rank_f2_high(xor_rows),
                         "the_three_1_cells_are_distinct": distinct,
                         "d1_d2_is_zero": d1d2})
    probe_xor = (1 << 0) ^ (1 << 0) ^ (1 << 1)
    probe_or = (1 << 0) | (1 << 0) | (1 << 1)
    probe = boundary_connective(0, 0, 1)
    gate("G14", "measurement",
         "THE BOOLEAN CONNECTIVE AT THE INCIDENCE BOUNDARY CARRIES A "
         "PARITY-WITNESS GATE (RUNBOOK section 14 addendum, boundary "
         "parity).  The 2-boundary is the XOR of a 2-cell's three 1-cells.  "
         "On this substrate's realised cells the three 1-cells are measured "
         "PAIRWISE DISTINCT at every 2-cell of every member, so the OR "
         "returns the same rows and the measured rank delta is zero -- that "
         "is a measurement of the complex, not an assumption, and a "
         "degenerate 2-cell would break it.  The connective's own parity is "
         "then witnessed by a DEGENERATE PROBE pushed through the same "
         "instrument: on a repeated 1-cell the XOR cancels and the OR does "
         "not, and the death certificate is exactly that measured delta.  "
         "d_1 d_2 = 0 is verified on every coherent 2-cell of every member, "
         "exhaustively and without a sample cap",
         all(r["d1_d2_is_zero"] and r["the_three_1_cells_are_distinct"] and
             r["delta_on_the_realised_cells"] == 0 for r in par_rows)
         and probe == probe_xor and probe_xor != probe_or,
         {"rows": par_rows, "degenerate_probe_XOR": probe_xor,
          "degenerate_probe_OR": probe_or,
          "degenerate_probe_through_the_instrument": probe})

    # per-invariant gates
    gate("G15", "computation",
         "PHI IS COMPUTED BY TWO ROUTES AND LIES IN ITS DECLARED RANGE: the "
         "overlap edge set built from the union of the per-cell relations, "
         "against a second accumulation that never forms the edge list, at "
         "every member; and 0 <= PHI <= 1 at every member, with the "
         "denominator the forced pair count n(n-1)/2 recomputed from the "
         "printed label count",
         all(meas[A["name"]]["PHI"] == meas[A["name"]]["PHI_route_2"]
             and Fr(0) <= meas[A["name"]]["PHI"] <= Fr(1) for A in family),
         {A["name"]: {"PHI": canon(meas[A["name"]]["PHI"]),
                      "route_2": canon(meas[A["name"]]["PHI_route_2"]),
                      "overlap_edges": meas[A["name"]]["overlap_edges"],
                      "all_pairs": A["n"] * (A["n"] - 1) // 2}
          for A in family})
    gate("G16", "computation",
         "THE COHERENT 2-CELL COUNT IS RECOUNTED BY A COMPARATOR THAT DOES "
         "NOT ROUTE THROUGH THE COMPONENT UNDER TEST (RUNBOOK section 14 "
         "addendum #219): the construction flags coherence while it builds "
         "the cell, and the recount reconstructs each cell's three drawn "
         "maps from the EDGE table alone and re-composes them.  The two "
         "agree at every member, and the density's denominator -- the drawn "
         "1-cell count -- is measured non-zero",
         all(meas[A["name"]]["coherent_two_cells"] ==
             meas[A["name"]]["coherent_two_cells_independent_recount"]
             and meas[A["name"]]["one_cells"] > 0 for A in family),
         {A["name"]: {"flagged": meas[A["name"]]["coherent_two_cells"],
                      "recount": meas[A["name"]][
                          "coherent_two_cells_independent_recount"],
                      "one_cells": meas[A["name"]]["one_cells"],
                      "NCOH_DENSITY": canon(meas[A["name"]]["NCOH_DENSITY"])}
          for A in family})
    specrows = [dict(r, arena=A["name"]) for A in family
                for r in meas[A["name"]]["spectral_rows"]]
    gate("G17", "computation",
         "THE SPECTRAL PROFILE IS COMPUTED TWICE AND I2's EIGENVALUE-1 ROW "
         "RIDES ALONG AS AN ANCHOR AT EVERY MEMBER.  The multiplicity of the "
         "trivial cyclotomic factor -- which IS dim ker(I - E) -- is taken "
         "once as the readout's cycle count and once as the exact rational "
         "kernel dimension of I - E computed by elimination over Q, and the "
         "two agree at every readout of every member; the profile's degrees "
         "are checked to sum to the dimension; and the eigenvalue-1 row is "
         "confirmed present at every readout, so 0 lies in spec(I - E) all "
         "along the family.  The wall is confirmed, never re-censused.  The "
         "anchor predicate is calibrated the other way inside this gate: on "
         "a multiplicity of zero it must return FALSE, so a chain that "
         "always said yes is caught here",
         all(r["routes_agree"] and r["eigenvalue_1_present"] and
             r["degree_check"] for r in specrows) and len(specrows) > 0
         and spectral_anchor_chain(0) is False
         and spectral_anchor_chain(1) is True,
         {"rows": specrows,
          "anchor_predicate_at_multiplicity_0": spectral_anchor_chain(0),
          "anchor_predicate_at_multiplicity_1": spectral_anchor_chain(1)})
    gate("G18", "computation",
         "THE DIMENSION PROFILE IS COMPUTED BY TWO ROUTES: the link-vertex "
         "count per chart read off the overlap edge list, against a second "
         "pass that accumulates each chart's neighbours from the per-cell "
         "tables and never forms the edge list.  They agree at every chart "
         "of every member, and the profile's weights are measured to sum to "
         "1 -- so a dropped chart is caught",
         all(meas[A["name"]]["dimension_routes_agree"] and
             sum(w for (_v, w) in meas[A["name"]]["DIMENSION_PROFILE"]) ==
             Fr(1) for A in family),
         {A["name"]: {"profile": canon(meas[A["name"]]["DIMENSION_PROFILE"]),
                      "routes_agree": meas[A["name"]][
                          "dimension_routes_agree"]}
          for A in family})
    gate("G19", "computation",
         "B2_DENSITY IS READ ON THE COMPLEX THAT CARRIES THE IDENTIFICATION "
         "DATA.  b_2 is taken on N_coh -- not on N -- because I3 measures the "
         "identification content to sit in the coherent sub-nerve; the "
         "denominator is N_coh's own 2-cell count and is measured non-zero "
         "at every member; the emitted density is compared against a "
         "comparator formed from N_coh's own b_2 and 2-cell count without "
         "passing through the complex selector; and the two complexes are "
         "measured to DIFFER at some member, so reading the wrong one is a "
         "detectable error",
         all(len(meas[A["name"]]["_Fcoh"]) > 0 for A in family)
         and all(meas[A["name"]]["B2_DENSITY"] ==
                 meas[A["name"]]["B2_DENSITY_from_N_coh"] for A in family)
         and any(meas[A["name"]]["N"]["b2"] != meas[A["name"]]["N_coh"]["b2"]
                 for A in family),
         {A["name"]: {"b2_N": meas[A["name"]]["N"]["b2"],
                      "b2_N_coh": meas[A["name"]]["N_coh"]["b2"],
                      "F_N_coh": len(meas[A["name"]]["_Fcoh"]),
                      "B2_DENSITY": canon(meas[A["name"]]["B2_DENSITY"]),
                      "comparator": canon(
                          meas[A["name"]]["B2_DENSITY_from_N_coh"])}
          for A in family})
    rulerows = []
    for A in family:
        m = meas[A["name"]]
        per = defaultdict(list)
        for c, pairs, order in zip(m["_cells"], m["cell_drawn_pairs"],
                                   m["cell_group_orders"]):
            per[c["rule"]].append((order, pairs))
        rulerows.append({"arena": A["name"],
                         "FULL_cells": sorted(per["FULL"]),
                         "REAL_cells": sorted(per["REAL"]),
                         "REAL_draws_nothing":
                             all(p == 0 for (_o, p) in per["REAL"])})
    disclose("X-REAL-EMPTY",
             "The REALISED rule draws NOTHING at A2, and that is measured "
             "rather than assumed: at that member the realised transport has "
             "order 10 on a seven-label symmetry saturation, so no ordered "
             "pair has a UNIQUE power carrying one label to the other and "
             "the admission rule refuses every candidate.  Consequently at "
             "A2 alone every 2-cell draws its three maps from one cyclic "
             "group, which acts regularly on its block, so coherence is "
             "ANALYTICALLY FORCED there and N coincides with N_coh.  At the "
             "other four members two distinct transport groups meet at a "
             "common block and coherence is contingent -- it is measured "
             "96 of 160 at A1 and 222 of 438, 259 of 511, 296 of 584 at the "
             "grown members.  This is a disclosure, not a must-pass gate.",
             {"rows": rulerows})
    disclose("X-B1",
             "b_1 is excluded as a candidate by the pin and is printed once "
             "here as a disclosure.  On N it is measured ZERO at every "
             "member -- the trivial H_1 I3 reports, reproduced at this "
             "substrate -- while on N_coh it is non-zero and grows: "
             "coherence costs cycles, exactly as I3 measured at its own "
             "scale.",
             {A["name"]: {"b1_N": meas[A["name"]]["N"]["b1"],
                          "b1_N_coh": meas[A["name"]]["N_coh"]["b1"]}
              for A in family})

    # ---- the trajectory table ---------------------------------------------
    prog("trajectory")
    rows = trajectory_rows(family, meas)
    names = [r[0] for r in DECL["registered_invariants"]]
    kinds = {r[0]: r[2] for r in DECL["registered_invariants"]}
    cells_present = sum(1 for nm in rows for v in rows[nm])
    forced = len(names) * len(family)
    complete = (sorted(rows) == sorted(names)
                and cells_present == forced
                and all(v is not None for nm in rows for v in rows[nm]))
    TABLES["trajectory"] = {
        "members": [A["name"] for A in family],
        "labels": [A["n"] for A in family],
        "rows": {nm: [canon(v) for v in rows.get(nm, [])] for nm in names},
        "cells_present": cells_present, "cells_forced": forced}
    gate("G20", "measurement",
         "THE TRAJECTORY TABLE IS CELL-COMPLETE AGAINST ITS FORCED PRODUCT "
         "(RUNBOOK section 13 addendum #234): the number of cells actually "
         "written is counted and compared with the product of the registered "
         "invariant count and the built family length, the row-name set is "
         "compared with the registry, and no cell is permitted to be absent. "
         " A dropped row or a dropped cell is caught here",
         complete, TABLES["trajectory"])

    # ---- stabilisation and the verdict ------------------------------------
    K = stabilisation_window()
    fixture = [Fr(int(s.split("/")[0]), int(s.split("/")[1]))
               for s in DECL["K_window_fixture"]["trajectory"]]
    at_K = is_constant_on_window(fixture, K)
    at_1 = is_constant_on_window(fixture, 1)
    gate("G21", "measurement",
         "THE STABILISATION WINDOW IS LOAD-BEARING AND IS CALIBRATED BOTH "
         "WAYS ON A CRAFTED FIXTURE DECLARED IN ADVANCE.  The fixture's last "
         "two entries agree and its third-from-last does not, so at the "
         "declared K = 3 it is NOT stabilised and at K = 1 it IS: a window "
         "shrink therefore flips a verdict, which is exactly what the pin "
         "requires the window mutant to prove.  The instrument's window is "
         "measured equal to the pin's declared K",
         K == DECL["K"] and at_K is False and at_1 is True,
         {"K": K, "declared_K": DECL["K"],
          "fixture": DECL["K_window_fixture"]["trajectory"],
          "stabilised_at_K": at_K, "stabilised_at_1": at_1})

    stab = {}
    modes = {}
    for nm in names:
        vals = rows.get(nm, [])
        if not vals:
            modes[nm] = "UNDEFINED-AT-A-MEMBER"
            continue
        modes[nm] = (scalar_mode(vals) if kinds[nm] == "scalar"
                     else profile_mode(vals))
        if modes[nm] == "CONSTANT":
            stab[nm] = vals[-1]
    stabilised = sorted(stab)
    head = verdict_head(stabilised)
    stab_body = ";".join("%s=%s" % (nm, canon(stab[nm])) for nm in names
                         if nm in stab)
    div_body = ";".join("%s:%s" % (nm, modes[nm]) for nm in names
                        if nm not in stab)
    window_q = qualifier_source("WINDOW=K=%d-OF-%d-MEMBERS-%s"
                                % (K, len(family), cap))
    phi_lt_1 = [A["name"] for A in family if meas[A["name"]]["PHI"] < Fr(1)]
    gw = gateway_member(phi_lt_1)
    parts = []
    if stabilised:
        parts.append(stab_body)
    else:
        parts.append("ALL-%d-REGISTERED-INVARIANTS-DIVERGE" % len(names))
    if div_body:
        parts.append("DIVERGENT=" + div_body)
    parts.append(window_q)
    parts.append("FUNCTORIALITY=" + func_qual)
    parts.append("R2-GATEWAY=" + (gw if gw else "NONE"))
    verdict = head + "-<" + "|".join(parts) + ">"

    derived_ok = (
        (head == "R1-STABILIZES-AT") == (len(stabilised) > 0)
        and all((modes[nm] == "CONSTANT") == (nm in stab) for nm in names)
        and all(canon(stab[nm]) in verdict for nm in stabilised)
        and all(("%s:%s" % (nm, modes[nm])) in verdict
                for nm in names if nm not in stab)
        and window_q in verdict and func_qual in verdict
        and ("K=%d" % K) in window_q
        and ("OF-%d-MEMBERS" % len(family)) in window_q
        and cap in window_q
        and ("%d-OF-%d-STEPS" % (len(nonfunc), len(steps)) in func_qual
             or (not nonfunc and func_qual == "FAMILY-FUNCTORIAL"))
        and len(rows) == len(names))
    gate("G22", "derivation",
         "THE VERDICT STRING IS DERIVED INSIDE THIS GATE FROM THE MEASURED "
         "TRAJECTORY TABLE AND EVERY QUALIFIER IS COMPUTED (RUNBOOK section "
         "13 addendum #234, #257).  The HEAD is STABILIZES exactly when the "
         "measured set of registered invariants constant on the final K "
         "members is non-empty and NO-CONTINUUM-LIMIT exactly when it is "
         "empty; the stabilised values, each divergent invariant's measured "
         "failure mode, the window with the family length and cap state, the "
         "functoriality qualifier and R2's gateway are each read out of the "
         "measurement and each is required to appear verbatim in the emitted "
         "string.  Inverting the head, typing a qualifier, dropping a row or "
         "shrinking the window all break this derivation",
         derived_ok,
         {"verdict": verdict, "head": head, "stabilised": stabilised,
          "stabilised_values": {nm: canon(stab[nm]) for nm in stabilised},
          "failure_modes": modes, "window": window_q,
          "functoriality": func_qual, "R2_gateway": gw})
    FINDINGS["verdict"] = verdict

    gate("G23", "measurement",
         "R2's GATEWAY IS COMPUTED, NOT NAMED.  The set of members whose "
         "overlap-completeness fraction is strictly below 1 is computed from "
         "the trajectory table and the FIRST such member is handed forward "
         "as R2's arena; the criterion is measured to be non-vacuous, since "
         "PHI is measured strictly below 1 somewhere and its declared range "
         "admits 1",
         gw is not None and gw == phi_lt_1[0] and len(phi_lt_1) > 0,
         {"members_with_phi_below_1": phi_lt_1,
          "phi": {A["name"]: canon(meas[A["name"]]["PHI"]) for A in family},
          "R2_gateway_arena": gw})
    FINDINGS["R2_gateway"] = gw

    # ---- disjointness, measured -------------------------------------------
    dis_rows = []
    for A in family:
        m = meas[A["name"]]
        dis_rows.append({"arena": A["name"], "blocks": A["r"],
                         "b0_of_N": m["N"]["b0"],
                         "b0_equals_blocks_plus_basepoint":
                             m["N"]["b0"] == A["r"] + 1,
                         "one_cells_per_block":
                             Fr(m["one_cells"], A["r"]),
                         "coherent_two_cells_per_block":
                             Fr(m["coherent_two_cells"], A["r"])})
    growth_rows = [r for r in dis_rows if r["arena"] in ("A3", "A4", "A5")]
    gate("G24", "measurement",
         "THE DECLARED GROWTH RULE IS MEASURED TO REFINE BY DISJOINT "
         "ADDITION, AND THAT IS WHAT CARRIES THE CONSTANT DENSITIES.  At "
         "each grown member b_0 of the nerve is measured equal to the block "
         "count plus one -- the basepoint -- so the complex is a disjoint "
         "sum of one copy per block; and the per-block 1-cell and coherent "
         "2-cell counts are measured EQUAL across the grown members.  The "
         "constancy of the two densities is therefore located, not merely "
         "observed",
         all(r["b0_equals_blocks_plus_basepoint"] for r in dis_rows)
         and len({r["one_cells_per_block"] for r in growth_rows}) == 1
         and len({r["coherent_two_cells_per_block"]
                  for r in growth_rows}) == 1,
         {"rows": [{k: (canon(v) if isinstance(v, Fr) else v)
                    for k, v in r.items()} for r in dis_rows]})

    # ---- controls ----------------------------------------------------------
    prog("controls")
    posfam = positive_control_family(A3)
    posmeas = {}
    for i, A in enumerate(posfam):
        key = "%s#%d" % (A["name"], i)
        posmeas[key] = measure(A)
    posrows = {}
    for nm in names:
        posrows[nm] = [posmeas["%s#%d" % (A["name"], i)][nm]
                       for i, A in enumerate(posfam)]
    posstab = sorted(nm for nm in names
                     if is_constant_on_window(posrows[nm], K))
    poshead = ("R1-STABILIZES-AT" if posstab else
               "R1-NO-CONTINUUM-LIMIT-AT-THIS-SUBSTRATE")
    gate("G25", "control",
         "POSITIVE CONTROL: a family that is constant by construction "
         "returns the STABILIZES head naming ALL FIVE registered "
         "invariants.  The control runs the same instrument end to end -- "
         "the same atlas, the same five measurements, the same window -- so "
         "a defect that suppressed stabilisation everywhere would be caught "
         "here",
         poshead == "R1-STABILIZES-AT" and posstab == sorted(names),
         {"head": poshead, "stabilised": posstab,
          "values": {nm: canon(posrows[nm][-1]) for nm in posstab}})

    negrows = negative_control_estimators(meas, family[2:])
    negnames = sorted(negrows[family[2]["name"]])
    negtraj = {nm: [negrows[A["name"]][nm] for A in family[2:]]
               for nm in negnames}
    negstab = sorted(nm for nm in negnames
                     if is_constant_on_window(negtraj[nm], K))
    neghead = ("R1-STABILIZES-AT" if negstab else
               "R1-NO-CONTINUUM-LIMIT-AT-THIS-SUBSTRATE")
    gate("G26", "control",
         "NEGATIVE CONTROL: I3's EXCLUDED raw estimators -- the unnormalised "
         "overlap, coherent-cell, eigenvalue-multiplicity, chart and b_2 "
         "counts -- are read along the same three grown members and every "
         "one of them is measured to move, so the instrument returns the "
         "NO-CONTINUUM-LIMIT head.  Both heads are therefore reachable by "
         "the same derivation, on real measurements",
         neghead == "R1-NO-CONTINUUM-LIMIT-AT-THIS-SUBSTRATE"
         and negstab == [],
         {"head": neghead, "stabilised": negstab,
          "trajectory": {nm: [canon(v) for v in negtraj[nm]]
                         for nm in negnames}})

    shift = scramble_shift()
    sc_cells, moved = scramble_cells(meas["A3"]["_cells"], shift)
    sc = _measure_from_cells(A3, sc_cells)
    ident_sensitive = []
    ident_fixed = []
    for nm in names:
        if sc[nm] != meas["A3"][nm]:
            ident_sensitive.append(nm)
        else:
            ident_fixed.append(nm)
    declared_sensitive = ["NCOH_DENSITY", "B2_DENSITY"]
    declared_fixed = ["PHI", "DIMENSION_PROFILE", "SPECTRAL_PROFILE"]
    gate("G27", "control",
         "SCRAMBLE CONTROL: the drawn RELATION is preserved and the drawn "
         "MAPS are deterministically permuted inside each coordinate cell by "
         "an exact integer shift seeded from the declared control block "
         "alone.  The measured set of invariants that MOVED is compared "
         "against the pin's declared identification-sensitive set, and the "
         "measured set that did NOT move against the relation-only set.  The "
         "scramble is measured non-trivial -- the count of drawn maps it "
         "actually changed is printed and required positive -- so a "
         "no-op scramble cannot pass.  At this substrate the scramble is "
         "maximally destructive: the coherent 2-cell count falls to zero, so "
         "NCOH_DENSITY moves to 0 and B2_DENSITY moves to UNDEFINED (its "
         "denominator vanishes).  That is recorded as measured rather than "
         "smoothed into a number",
         sorted(ident_sensitive) == sorted(declared_sensitive)
         and sorted(ident_fixed) == sorted(declared_fixed) and moved > 0,
         {"shift": shift, "drawn_maps_moved": moved,
          "B2_DENSITY_is_undefined_after_the_scramble":
              sc["B2_DENSITY"] is None,
          "moved": sorted(ident_sensitive), "fixed": sorted(ident_fixed),
          "declared_identification_sensitive": declared_sensitive,
          "declared_relation_only": declared_fixed,
          "before": {nm: canon(meas["A3"][nm]) for nm in names},
          "after": {nm: canon(sc[nm]) for nm in names}})

    discfam = discrimination_family()
    discmeas = {A["name"]: measure(A) for A in discfam}
    disctraj = {nm: [discmeas[A["name"]][nm] for A in discfam]
                for nm in names}
    discmoved = sorted(nm for nm in declared_sensitive
                       if not is_constant_on_window(disctraj[nm], K))
    gate("G28", "control",
         "DISCRIMINATION CONTROL: a growth rule that is NOT a disjoint "
         "addition -- the widening family, whose single block grows rather "
         "than being copied -- is run through the same instrument, and BOTH "
         "densities are measured to MOVE along it.  So their constancy on "
         "the declared family is a property of that family's additive rule "
         "and not an artefact of the definitions; the two-sided calibration "
         "of the stabilisation claim sits here",
         discmoved == sorted(declared_sensitive),
         {"family": [A["name"] for A in discfam],
          "moved": discmoved,
          "trajectory": {nm: [canon(v) for v in disctraj[nm]]
                         for nm in names}})

    # ---- self-tests --------------------------------------------------------
    prog("self-tests")
    tested = selftest_tested_set(family, stabilised)
    st_rows = []
    for A in tested:
        tau = list(range(A["n"]))
        if A["n"] > 3:
            b = A["blocks"][0]
            tau[b[0]], tau[b[1]] = tau[b[1]], tau[b[0]]
        tau = tuple(tau)
        B = relabel_arena(A, tau)
        mm = measure(B)
        base_m = meas.get(A["name"]) or measure(A)
        st_rows.append({
            "arena": A["name"],
            "relabelling_moves": sum(1 for i in range(A["n"])
                                     if tau[i] != i),
            "PHI_invariant": mm["PHI"] == base_m["PHI"],
            "NCOH_invariant": mm["NCOH_DENSITY"] == base_m["NCOH_DENSITY"],
            "B2_invariant": mm["B2_DENSITY"] == base_m["B2_DENSITY"],
            "DIM_invariant": mm["DIMENSION_PROFILE"] ==
                             base_m["DIMENSION_PROFILE"],
            "SPEC_invariant": mm["SPECTRAL_PROFILE"] ==
                              base_m["SPECTRAL_PROFILE"]})
    gate("G29", "measurement",
         "THE INSTRUMENT IS SELF-TESTED UNDER THE ARENA'S OWN ACTION "
         "(RUNBOOK section 14).  Each member is transported by a declared "
         "non-trivial relabelling -- the symmetry, the blocks and the atlas "
         "are all rebuilt inside the transported arena, not merely renamed "
         "-- and all five registered invariants are recomputed there and "
         "measured equal.  The tested set is fixed by DECLARATION as the "
         "whole family and never selected by the verdicts under audit, and "
         "the relabelling is measured to move labels",
         len(st_rows) == len(family)
         and all(r["relabelling_moves"] > 0 and r["PHI_invariant"] and
                 r["NCOH_invariant"] and r["B2_invariant"] and
                 r["DIM_invariant"] and r["SPEC_invariant"] for r in st_rows),
         {"rows": st_rows, "tested_set_size": len(tested),
          "family_size": len(family)})

    # ---- robustness in the family index ------------------------------------
    prog("index robustness")
    alt_ms = robustness_indices(width, rank, [11, 13])
    alt_rows = []
    for m in alt_ms:
        n, blocks, sig = regenerate_fresh(base, exp, width, m, rank, p3)
        B = make_arena("L%d" % m, n, sig, blocks, "alternative index")
        mm = measure(B)
        alt_rows.append({"member": B["name"], "labels": n,
                         "NCOH_DENSITY": canon(mm["NCOH_DENSITY"]),
                         "B2_DENSITY": canon(mm["B2_DENSITY"]),
                         "PHI": canon(mm["PHI"]),
                         "agrees_with_the_stabilised_values":
                             (mm["NCOH_DENSITY"] == stab.get("NCOH_DENSITY")
                              and mm["B2_DENSITY"] == stab.get("B2_DENSITY"))})
    gate("G30", "measurement",
         "THE FAMILY INDEX IS AN ARENA COORDINATE AND ITS DEPENDENCE IS "
         "MEASURED (RUNBOOK section 15).  The pin's family walks the growth "
         "rule's OWN index m; the rule also carries a prime-indexed "
         "selection, and the members that selection picks at the next two "
         "declared primes are built and measured here.  The stabilised "
         "values are required to reproduce at those members too, so the "
         "stabilisation is not an artefact of which index the family walks",
         len(alt_rows) == 2
         and all(r["agrees_with_the_stabilised_values"] for r in alt_rows),
         {"alternative_members": alt_rows,
          "stabilised_values": {nm: canon(stab[nm]) for nm in stabilised}})

    TABLES["controls"] = {
        "positive": {"head": poshead, "stabilised": posstab},
        "negative": {"head": neghead, "stabilised": negstab,
                     "trajectory": {nm: [canon(v) for v in negtraj[nm]]
                                    for nm in negnames}},
        "scramble": {"moved": sorted(ident_sensitive),
                     "fixed": sorted(ident_fixed),
                     "drawn_maps_moved": moved},
        "discrimination": {"moved": discmoved,
                           "trajectory": {nm: [canon(v) for v in disctraj[nm]]
                                          for nm in names}},
        "index_robustness": alt_rows,
    }
    TABLES["measurements"] = {
        A["name"]: {k: (canon(v) if isinstance(v, (Fr, tuple)) else v)
                    for k, v in meas[A["name"]].items()
                    if not k.startswith("_") and k != "spectral_rows"
                    and k != "degrees"}
        for A in family}
    TABLES["spectral_rows"] = specrows
    FINDINGS["thesis"] = (
        "THE DECLARED REFINEMENT FAMILY REFINES BY DISJOINT ADDITION, AND "
        "EXACTLY THE TWO IDENTIFICATION-CARRYING DENSITIES STABILIZE.  Over "
        "the pin's five-member family the overlap-completeness fraction is "
        "measured strictly below 1 at every member -- so locality exists at "
        "this substrate and R2's gateway arena is %s -- and it does not "
        "stabilize: it is %s on the declared window.  Of the five "
        "pre-registered intensive invariants exactly %d are exactly constant "
        "on the final %d members, %s, and the same two values reproduce at "
        "the members the growth rule's prime-indexed selection picks "
        "instead.  The mechanism is measured rather than inferred: at every "
        "grown member b_0 of the nerve equals the block count plus the "
        "basepoint, so the refinement is a disjoint sum of identical block "
        "atlases, the per-block 1-cell and coherent-2-cell counts are equal "
        "across members, and a growth rule that widens a block instead of "
        "copying it moves both densities.  The three that do not stabilize "
        "fail in a named way: %s.  The family is NOT functorial: no "
        "admissible arena morphism exists at %d of its %d steps, and the "
        "obstructions are measured -- a block width that decreases, and a "
        "symmetry orbit size the successor arena does not carry.  I2's "
        "eigenvalue-1 row rides along as an anchor at every readout of every "
        "member: 0 lies in spec(I - E) all the way up the family."
        % (gw, modes["PHI"], len(stabilised), K, stab_body, div_body,
           len(nonfunc), len(steps)))
    return family, meas, verdict


def _d1d2_is_zero(edges, face):
    acc = 0
    for e in face:
        a, b, _c = edges[e]
        acc = acc ^ (1 << a) ^ (1 << b)
    return acc == 0


def _measure_from_cells(A, cells):
    edges, eidx = nerve_edges(cells)
    F, Fcoh = geometric_cells(A, cells, eidx)
    und = overlap_graph(cells)
    n = A["n"]
    inv_coh = complex_invariants(n, edges, Fcoh)
    spec, _rows = spectral_profile(A)
    dimp, _ag, _d = dimension_profile(A, cells)
    return {"PHI": Fr(len(und), n * (n - 1) // 2),
            "NCOH_DENSITY": Fr(len(Fcoh), len(edges)) if edges else None,
            "SPECTRAL_PROFILE": spec, "DIMENSION_PROFILE": dimp,
            "B2_DENSITY": Fr(inv_coh["b2"], len(Fcoh)) if Fcoh else None}


def _delta_fixed_points(A):
    """|{x : delta(x) = x}| over the arena's whole completion family, with
    delta(x) = sigma(x)^-1 x and sigma = conjugation by Sigma (GEN 8.1)."""
    bump()
    n = A["n"]
    S = A["Sigma"]
    cnt = 0
    for t in permutations(range(1, n)):
        q = (0,) + t
        if delta_of(S, q) == q:
            cnt += 1
    return cnt


def pmul_conj(S, q):
    return pcomp(S, pcomp(q, pinv(S)))


def delta_of(S, q):
    """GEN 8.1's completion -> commutator map delta(q) = sigma(q)^-1 q."""
    return pcomp(pinv(pmul_conj(S, q)), q)


def _elementary_order(A):
    """The order of the subgroup generated by the arena's block cycles."""
    bump()
    n = A["n"]
    gens = [block_cycle(n, list(b)) for b in A["blocks"]]
    seen = {pident(n)}
    frontier = [pident(n)]
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = pcomp(g, x)
                if y not in seen:
                    seen.add(y)
                    nxt.append(y)
        frontier = nxt
    return len(seen)


def _delta_fixed_points_sub(A):
    bump()
    n = A["n"]
    S = A["Sigma"]
    gens = [block_cycle(n, list(b)) for b in A["blocks"]]
    seen = {pident(n)}
    frontier = [pident(n)]
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = pcomp(g, x)
                if y not in seen:
                    seen.add(y)
                    nxt.append(y)
        frontier = nxt
    return sum(1 for q in seen if delta_of(S, q) == q)


def _smallest_injective(p, rank):
    L = 2
    while L <= 60:
        if legendre_exponent(L - 1, p) >= rank:
            return L
        L += 1
    return None


def _divisibility_threshold(p, rank):
    n = 1
    while legendre_exponent(n - 1, p) < rank:
        n += 1
    return n


# ===========================================================================
# 10.  EXACTNESS, EXEMPTIONS AND THE MUTANT TABLE.
# ===========================================================================

def exactness_scope():
    """The source the arithmetic guard scans.  [instrument -- mutable]"""
    src = Path(__file__).resolve().read_text()
    if MUTANT == "float-lax":
        return src + "\n_PROBE = 0.5\n"
    return src


def exemption_scope():
    """The set of functions permitted to reference mutant identity.
    [instrument -- mutable]"""
    if MUTANT == "exempt-lax":
        return set()
    return set(MUTABLE_FUNCS)


def run_exactness():
    src = exactness_scope()
    tree = ast.parse(src)
    guard = [f for f in ast.walk(tree)
             if isinstance(f, ast.FunctionDef) and f.name == "run_exactness"]
    guard_lines = set()
    for f in guard:
        for node in ast.walk(f):
            guard_lines.add(getattr(node, "lineno", -1))
    floats, divs, banned, pathjoins = [], [], [], []
    for node in ast.walk(tree):
        ln = getattr(node, "lineno", 0)
        if ln in guard_lines:
            continue
        if isinstance(node, ast.Constant) and node.value.__class__.__name__ \
                == "float":
            floats.append(ln)
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            if _leftmost_name(node.left) in ("HERE", "REPO"):
                pathjoins.append(ln)
            else:
                divs.append(ln)
        if isinstance(node, ast.Name) and node.id in ("float", "complex"):
            banned.append(ln)
        if isinstance(node, ast.Attribute) and node.attr in (
                "sqrt", "log", "exp", "pow10"):
            banned.append(ln)
    gate("G31", "measurement",
         "THE ARITHMETIC IS EXACT AND THE GUARD IS MECHANICAL: this file's "
         "own abstract syntax tree is walked and measured to contain NO "
         "float literal, NO ARITHMETIC true-division operator and no call to "
         "a floating-point builtin or math function.  Every division node in "
         "the file is classified and the survivors are measured to be "
         "pathlib joins rooted at a declared path root, their count printed "
         "rather than waived.  Every ratio in the unit is a "
         "fractions.Fraction built from two integers, so every equality in "
         "the trajectory table is exact",
         not floats and not divs and not banned and len(pathjoins) > 0,
         {"float_literals": floats, "arithmetic_division_lines": divs,
          "path_join_divisions": len(pathjoins),
          "banned_names": banned,
          "ast_nodes_walked": sum(1 for _ in ast.walk(tree))})


def _leftmost_name(node):
    while isinstance(node, ast.BinOp):
        node = node.left
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
        return node.func.id
    return None


def run_exemption_sweep():
    src = Path(__file__).resolve().read_text()
    tree = ast.parse(src)
    permitted = exemption_scope()
    offenders = []
    for fn in ast.walk(tree):
        if isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for node in ast.walk(fn):
                if isinstance(node, ast.Name) and node.id == "MUTANT":
                    if fn.name not in permitted and \
                            fn.name not in ("main", "run_mutant_table"):
                        offenders.append((fn.name, node.lineno))
    gate_sites = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                and node.func.id == "gate":
            for sub in ast.walk(node):
                if isinstance(sub, ast.Name) and sub.id == "MUTANT":
                    gate_sites.append(getattr(node, "lineno", 0))
    gate("G32", "measurement",
         "NO GATE PREDICATE REFERENCES MUTANT IDENTITY (RUNBOOK section 14 "
         "addendum #208).  Every occurrence of the mutant variable in this "
         "file is located by AST walk and required to sit inside a function "
         "declared MUTABLE -- an instrument the mutants perturb -- and the "
         "argument expressions of every gate call are swept for the same "
         "name.  Both counts are measured zero outside the declared set, so "
         "no declared falsifier is exempted from its own gate.  The "
         "permitted set is measured non-empty, so a sweep that permitted "
         "nothing -- or everything -- is itself caught",
         not offenders and not gate_sites and len(permitted) > 0,
         {"offending_functions": offenders,
          "gate_calls_referencing_MUTANT": gate_sites,
          "permitted_functions": len(permitted),
          "declared_mutable_functions": sorted(MUTABLE_FUNCS)})


def run_mutant_table():
    import subprocess
    from concurrent.futures import ThreadPoolExecutor
    prog("mutant table (%d mutants)" % len(MUTANTS))

    def _run(m):
        r = subprocess.run([sys.executable, str(Path(__file__).resolve()),
                            "--mutant", m, "--quiet"],
                           capture_output=True, text=True)
        kill = {"failed_anchors": [], "failed_gates": [], "crashed": True}
        for ln in r.stdout.splitlines():
            if ln.startswith("KILL-JSON "):
                kill = json.loads(ln[len("KILL-JSON "):])
                kill["crashed"] = False
        return {"mutant": m, "exit": r.returncode, "died": r.returncode == 1,
                "falsified_anchors": sorted(kill["failed_anchors"])[:6],
                "falsified_gates": sorted(kill["failed_gates"]),
                "crashed_before_reporting": kill["crashed"],
                "traceback": "Traceback" in r.stderr}

    with ThreadPoolExecutor(max_workers=6) as ex:
        rows = sorted(ex.map(_run, MUTANTS), key=lambda r: r["mutant"])
    kinds = {m[0]: m[1] for m in MUTANT_DECL}
    decls = {m[0]: m[2] for m in MUTANT_DECL}
    for r in rows:
        r["kind"] = kinds[r["mutant"]]
        r["declaration"] = decls[r["mutant"]]
    must = [g["id"] for g in GATES if g["class"] != "disclosure"
            and g["id"] != "G33"]
    hit = {g for r in rows for g in r["falsified_gates"]}
    comp_hit = {g for r in rows if r["kind"] == "computation"
                for g in r["falsified_gates"]}
    never = sorted(set(must) - hit)
    TABLES["mutants"] = rows
    TABLES["gate_falsification"] = {
        "must_pass_gates": must,
        "falsified_by_some_mutant": sorted(set(must) & hit),
        "falsified_by_a_computation_mutant": sorted(set(must) & comp_hit),
        "falsified_only_by_a_waiver": sorted((set(must) & hit) - comp_hit),
        "never_falsified": never,
        "per_gate_falsifiers": {
            g: sorted(r["mutant"] for r in rows if g in r["falsified_gates"])
            for g in must}}
    gate("G33", "derivation",
         "EVERY DECLARED MUTANT DIES AND EVERY MUST-PASS GATE IS FALSIFIED "
         "BY SOME MUTANT.  Each mutant runs the unit to completion in its "
         "own process, must exit 1, must reach the totals block without a "
         "traceback, and must falsify at least one NAMED gate or anchor; the "
         "clause that matters is the second -- the set of must-pass gates "
         "that NO mutant falsifies is measured to be EMPTY.  Each mutant "
         "declares its KIND and both denominators are reported, because a "
         "waiver proves a gate's predicate is load-bearing for the exit code "
         "and not that the gate would catch a computational defect.  The one "
         "gate excluded from the denominator is this one, which does not run "
         "inside a mutant process",
         all(r["died"] for r in rows)
         and all(r["falsified_anchors"] or r["falsified_gates"] for r in rows)
         and not any(r["traceback"] for r in rows)
         and not any(r["crashed_before_reporting"] for r in rows)
         and not never,
         {"mutants": len(rows), "died": sum(1 for r in rows if r["died"]),
          "computation_mutants": sum(1 for r in rows
                                     if r["kind"] == "computation"),
          "waivers": sum(1 for r in rows if r["kind"] == "waiver"),
          "must_pass_gate_denominator": len(must),
          "falsified_by_some_mutant": len(set(must) & hit),
          "falsified_by_a_computation_mutant": len(set(must) & comp_hit),
          "never_falsified": never,
          "tracebacks": sum(1 for r in rows if r["traceback"])})


# ===========================================================================
# 11.  RECEIPT AND RENDER.
# ===========================================================================

def build_receipt():
    must = [g for g in GATES if g["class"] != "disclosure"]
    return {
        "schema": "r1-continuum/1",
        "unit": "R1 -- THE CONTINUUM RUNG (v14 paper-01)",
        "pin": "v14/note-r1-continuum-pin.md",
        "python": "%d.%d" % sys.version_info[:2],
        "arithmetic": "exact: int and fractions.Fraction only; AST-guarded",
        "source_sha256": SOURCE_SHA256,
        "declarations": DECL,
        "mutant_declarations": [{"mutant": m[0], "kind": m[1],
                                 "declaration": m[2]} for m in MUTANT_DECL],
        "anchors": ANCHORS,
        "gates": GATES,
        "disclosures": DISCLOSURES,
        "tables": TABLES,
        "findings": FINDINGS,
        "verdict": FINDINGS.get("verdict"),
        "totals": {
            "anchors": len(ANCHORS),
            "anchor_failures": sum(1 for a in ANCHORS if not a["passed"]),
            "gates": len(GATES),
            "must_pass_gates": len(must),
            "must_pass_failures": sum(1 for g in must if not g["passed"]),
            "disclosures": len(DISCLOSURES),
            "mutants": len(TABLES.get("mutants", [])),
            "mutant_survivors": sum(1 for r in TABLES.get("mutants", [])
                                    if not r["died"]),
            "measured_data_evaluated": _MEASURED,
        },
    }


def wrap(s, w=78):
    out, line = [], ""
    for word in s.split():
        if line and len(line) + len(word) + 1 > w:
            out.append(line)
            line = word
        else:
            line = (line + " " + word) if line else word
    if line:
        out.append(line)
    return out


def render(rec):
    L = []
    A = L.append
    A("=" * 78)
    A("R1 -- THE CONTINUUM RUNG".center(78))
    A("v14 paper-01   |   pin v14/note-r1-continuum-pin.md".center(78))
    A("=" * 78)
    A("")
    A("QUESTION")
    for ln in wrap(DECL["question"]):
        A("  " + ln)
    A("")
    A("VERDICT")
    for ln in wrap(str(rec["verdict"]), 74):
        A("  " + ln)
    A("")
    A("THESIS")
    for ln in wrap(rec["findings"].get("thesis", "")):
        A("  " + ln)
    A("")
    A("-" * 78)
    A("1. THE INHERITANCE (R0 rows, verified at run time)")
    A("-" * 78)
    for r in rec["tables"]["inheritance"]["rows"]:
        A("  %-4s %-46s %s" % (r["row"], r["artifact"], r["sha256_12"]))
    A("")
    A("  companion artifacts named by R0, censused: %d" %
      len(rec["tables"]["inheritance"]["companions"]))
    for c in rec["tables"]["inheritance"]["companions"]:
        A("    %-10s %-44s %s %s" % (c["id"], c["artifact"], c["computed"],
                                     "OK" if c["matches"]
                                     else "MISMATCH (declared %s)"
                                          % c["declared"]))
    A("")
    A("-" * 78)
    A("2. THE DECLARED FAMILY (every label count derived, none typed)")
    A("-" * 78)
    A("  growth rule, read verbatim from I2's receipt:")
    for ln in wrap(rec["tables"].get("rule_text", ""), 72):
        A("      " + ln)
    fam = rec["tables"]["family"]
    A("  %-6s %-8s %-8s %-10s %-14s %s" % ("member", "labels", "blocks",
                                           "blocksize", "Sigma order",
                                           "Sigma cycle type"))
    for nm in rec["tables"]["trajectory"]["members"]:
        f = fam[nm]
        A("  %-6s %-8d %-8d %-10s %-14d %s"
          % (nm, f["labels"], f["blocks"], canon(f["block_sizes"][:3]),
             f["Sigma_order"], canon(sorted(set(f["Sigma_cycle_type"])))))
    A("")
    A("  maps between members:")
    for s in rec["tables"]["maps"]["steps"]:
        A("    %-10s %-14s %s" % (s["step"],
                                  "ADMISSIBLE" if s["admissible"]
                                  else "NO MORPHISM", s["reason"][:44]))
    A("    qualifier: " + rec["tables"]["maps"]["qualifier"])
    A("")
    A("-" * 78)
    A("3. THE TRAJECTORY TABLE (5 registered invariants x %d members)"
      % len(rec["tables"]["trajectory"]["members"]))
    A("-" * 78)
    tr = rec["tables"]["trajectory"]
    A("  %-20s %s" % ("invariant", "  ".join("%-16s" % m
                                             for m in tr["members"])))
    for nm in [r[0] for r in DECL["registered_invariants"]]:
        vals = tr["rows"].get(nm, [])
        A("  %-20s %s" % (nm, "  ".join("%-16s" % v[:16] for v in vals)))
    for nm in [r[0] for r in DECL["registered_invariants"]]:
        vals = tr["rows"].get(nm, [])
        if any(len(v) > 16 for v in vals):
            A("")
            A("  %s, in full:" % nm)
            for i, m in enumerate(tr["members"]):
                A("    %-6s %s" % (m, vals[i]))
    A("")
    A("  cells written %d of the forced %d" % (tr["cells_present"],
                                               tr["cells_forced"]))
    A("")
    A("-" * 78)
    A("4. CONTROLS")
    A("-" * 78)
    c = rec["tables"]["controls"]
    A("  positive       : %s  stabilised %s" % (c["positive"]["head"],
                                                canon(c["positive"]["stabilised"])))
    A("  negative       : %s  stabilised %s" % (c["negative"]["head"],
                                                canon(c["negative"]["stabilised"])))
    A("  scramble       : moved %s ; fixed %s ; drawn maps moved %d"
      % (canon(c["scramble"]["moved"]), canon(c["scramble"]["fixed"]),
         c["scramble"]["drawn_maps_moved"]))
    A("  discrimination : moved %s" % canon(c["discrimination"]["moved"]))
    A("  index sweep    : %s" % canon([r["member"] for r
                                       in c["index_robustness"]]))
    A("")
    A("-" * 78)
    A("5. ANCHORS  (%d, all exit-1)" % len(rec["anchors"]))
    A("-" * 78)
    bad = [a for a in rec["anchors"] if not a["passed"]]
    A("  failures: %d" % len(bad))
    for a in bad:
        A("    %-22s declared %-14s computed %s" % (a["id"], a["declared"],
                                                    a["computed"]))
    A("")
    A("-" * 78)
    A("6. GATES")
    A("-" * 78)
    for g in rec["gates"]:
        A("  [%s] %-4s %s" % ("PASS" if g["passed"] else "FAIL", g["id"],
                              g["class"]))
        for ln in wrap(g["claim"], 72):
            A("        " + ln)
    A("")
    A("-" * 78)
    A("7. DISCLOSURES")
    A("-" * 78)
    for d in rec["disclosures"]:
        A("  %s" % d["id"])
        for ln in wrap(d["statement"], 72):
            A("      " + ln)
    A("")
    A("-" * 78)
    A("8. TOTALS")
    A("-" * 78)
    for k in sorted(rec["totals"]):
        A("  %-30s %s" % (k, rec["totals"][k]))
    A("")
    if rec["tables"].get("mutants"):
        A("-" * 78)
        A("9. MUTANT TABLE")
        A("-" * 78)
        for r in rec["tables"]["mutants"]:
            A("  %-16s exit %d  %-11s kills %s"
              % (r["mutant"], r["exit"], r["kind"],
                 canon((r["falsified_gates"] or r["falsified_anchors"])[:4])))
        gf = rec["tables"]["gate_falsification"]
        A("")
        A("  must-pass gates %d ; falsified by some mutant %d ; never "
          "falsified %s" % (len(gf["must_pass_gates"]),
                            len(gf["falsified_by_some_mutant"]),
                            canon(gf["never_falsified"])))
    A("")
    A("=" * 78)
    return "\n".join(L) + "\n"


def main():
    global MUTANT, SOURCE_SHA256
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--mutant")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--falsification-selftest", action="store_true")
    ap.add_argument("--list-mutants", action="store_true")
    a = ap.parse_args()
    if a.list_mutants:
        sys.stdout.write("\n".join(MUTANTS) + "\n")
        return 0
    MUTANT = a.mutant
    SOURCE_SHA256 = hashlib.sha256(
        Path(__file__).resolve().read_bytes()).hexdigest()

    if a.falsification_selftest:
        import subprocess
        r = subprocess.run([sys.executable, str(Path(__file__).resolve()),
                            "--mutant", "anchor-I5", "--quiet"],
                           capture_output=True, text=True)
        died = r.returncode == 1 and "A-R0-I5" in r.stdout
        sys.stdout.write(
            "FALSIFICATION SELF-TEST: one pinned external anchor (I5's "
            "carrying receipt hash) is corrupted.\n"
            "  exit code            : %d (expected 1)\n"
            "  named anchor failure : %s\n"
            "  artifacts written    : NO\n"
            "  result               : %s\n"
            % (r.returncode, "A-R0-I5" in r.stdout,
               "PASS" if died else "FAIL"))
        return 0 if died else 1

    family, meas, verdict = run()
    TABLES["rule_text"] = [g for g in GATES if g["id"] == "G04"][0][
        "value"]["rule_text"]
    run_exactness()
    run_exemption_sweep()
    if not MUTANT:
        run_mutant_table()
    rec = build_receipt()
    txt = render(rec)
    fail = rec["totals"]["must_pass_failures"] + rec["totals"]["anchor_failures"]
    if not MUTANT and not fail:
        OUT_TXT.write_text(txt)
        OUT_JSON.write_text(json.dumps(rec, indent=1, sort_keys=True,
                                       default=str) + "\n")
    if a.quiet:
        sys.stdout.write("KILL-JSON " + json.dumps(
            {"failed_anchors": [x["id"] for x in ANCHORS if not x["passed"]],
             "failed_gates": [x["id"] for x in GATES
                              if x["class"] != "disclosure"
                              and not x["passed"]]}) + "\n")
    else:
        sys.stdout.write(txt)
    prog("done: %d anchors, %d gates, %d failures"
         % (len(ANCHORS), len(GATES), fail))
    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main())

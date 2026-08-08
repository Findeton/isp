#!/usr/bin/env python3.13
# -*- coding: utf-8 -*-
"""
HA -- THE RECORD-NATIVE H_a[N] SUCCESSOR (GRAVITY LINE)
=======================================================

Pin: v13/note-ha-successor-pin.md (STRICT, immutable base 024fcd7).
Binding source: v13/note-gw1-metric-from-closure.md (TERMINAL, v13 LOG #5) and
its successor directive 7.1 -- "First -- construct a record-native H_a[N] to
v4 paper 7 Definition 1.3, and measure R_{HH,a}[N,M] against
beta_a^i = I_a(g)^{ij}(N d_j M - M d_j N)"; v4 paper 7 Definitions 1.1-1.4 and
2.1-2.5; v4 paper 12 Definition 11.6M (the three-normal switch detector);
v13/relativistic-isp-v13-paper0-gravity.md (the charter).
Declared secondary: v13/paper-nt-nomological-transport.md and
v13/paper-gen-generality-check.md, receipts hash-pinned.

Exact arithmetic only: fractions.Fraction, integers, and exact F_p in the finite
operator layer.  No floats anywhere.

MUTANT DISCIPLINE (RUNBOOK 14 addendum, v13 #208): every mutation below is a
mutation of an INSTRUMENT helper.  No gate predicate, and no function that
registers a gate, references mutant identity; the AST guard in section 13
measures that, and is itself validated by a synthetic injection it must flag.

Usage:
    python3.13 ha_successor_exact.py                  # delivery run
    python3.13 ha_successor_exact.py --mutant NAME    # one mutant; must exit 1
    python3.13 ha_successor_exact.py --falsification-selftest
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
    "anchor-gw1-trees":    "GW1 runnable-tree .py census perturbed",
    "anchor-gw1-lapse":    "GW1 'lapse' token sweep perturbed",
    "anchor-nt-paths":     "NT reduced-path count perturbed",
    "anchor-nt-sha":       "NT receipt sha256 perturbed",
    "anchor-gen-family":   "GEN completion-family size perturbed",
    "anchor-gen-defect":   "GEN declared defect permutation perturbed",
    "anchor-gen-spectrum": "GEN's computed defect order spectrum perturbed",
    # --- gate mutants (each mutates an INSTRUMENT, never a gate) ----------
    "closure-lax":     "the closure predicate accepts any residual field",
    "invert-lax":      "the bijection predicate accepts a non-injective map",
    "exempt-lax":      "the AST mutant-identity scanner is blinded",
    "control-lax":     "the broken-H variants are dropped from the tested set",
    "census-drop":     "a declared drag rule is dropped from the tested family",
    "rank-lax":        "the lapse family is degenerated below full rank",
    "freeze-lax":      "a fixture datum is evaluated before the declarations freeze",
    "cache-lax":       "the fresh-evaluation path reads the memo cache",
    "cache-alias":     "the weight memo serves a chart-transformed record the base "
                       "record's entry",
    "posdef-lax":      "the positive-definiteness predicate always accepts",
    "factor-lax":      "the exact-to-F_p reduction is perturbed non-linearly",
    "verdict-flip":    "the verdict derivation returns a hand-typed string instead of "
                       "the measured one",
    # --- computational mutants -------------------------------------------
    "sign-flip":       "the finite bracket covector's sign convention is flipped",
    "order-swap":      "the two normal labels are swapped in the commutator only",
    "transport-off":   "the second normal step reads the pre-advance front",
    "chart-shift":     "the chart action moves the record but not the field index",
    "beta-flat":       "the record-read metric in beta is replaced by the chart identity",
    "prime-single":    "the multi-prime controls are reduced to one prime",
    "bridge-spectrum": "the bridge's comparator spectrum is GEN's holonomy spectrum "
                       "instead of GEN's defect spectrum",
    "omega-asym":      "the finite bracket covector uses a non-antisymmetric difference",
    "readout-local":   "the record's metric readout is replaced by a link-local surrogate",
    "float-lax":       "the float sweep is blinded",
}

if MUTANT is not None and MUTANT not in MUTANTS:
    sys.stderr.write(f"unknown mutant {MUTANT!r}\n")
    sys.exit(2)

# Module-level switches.  These are read ONLY inside instrument helpers.
_M_TREES = (MUTANT == "anchor-gw1-trees")
_M_LAPSE = (MUTANT == "anchor-gw1-lapse")
_M_NTP = (MUTANT == "anchor-nt-paths")
_M_NTS = (MUTANT == "anchor-nt-sha")
_M_GENF = (MUTANT == "anchor-gen-family")
_M_GEND = (MUTANT == "anchor-gen-defect")
_M_GENS = (MUTANT == "anchor-gen-spectrum")
_M_CLOSURE = (MUTANT == "closure-lax")
_M_INVERT = (MUTANT == "invert-lax")
_M_SPECTRUM = (MUTANT == "bridge-spectrum")
_M_EXEMPT = (MUTANT == "exempt-lax")
_M_CONTROL = (MUTANT == "control-lax")
_M_CENSUS = (MUTANT == "census-drop")
_M_RANK = (MUTANT == "rank-lax")
_M_FREEZE = (MUTANT == "freeze-lax")
_M_CACHE = (MUTANT == "cache-lax")
_M_ALIAS = (MUTANT == "cache-alias")
_M_VERDICT = (MUTANT == "verdict-flip")
_M_POSDEF = (MUTANT == "posdef-lax")
_M_FACTOR = (MUTANT == "factor-lax")
_M_SIGN = (MUTANT == "sign-flip")
_M_ORDER = (MUTANT == "order-swap")
_M_TRANSPORT = (MUTANT == "transport-off")
_M_CHART = (MUTANT == "chart-shift")
_M_BETAFLAT = (MUTANT == "beta-flat")
_M_ONEPRIME = (MUTANT == "prime-single")
_M_OMASYM = (MUTANT == "omega-asym")
_M_READLOCAL = (MUTANT == "readout-local")
_M_FLOAT = (MUTANT == "float-lax")

# A single run-mode boolean, identical for EVERY mutant: it decides only
# whether receipts are written and the harness is spawned.  It carries no
# per-mutant identity and no gate predicate reads it (disclosure X03).
DELIVERY_RUN = (MUTANT is None)
# --falsification-selftest runs everything, including the mutant harness of
# section 16, but does NOT write the delivery artifacts: it is the guard that
# lets the falsification table be reproduced without touching frozen files.
WRITE_ARTIFACTS = (DELIVERY_RUN and not SELFTEST_ONLY)

# --------------------------------------------------------------------------
# 1.  RECEIPT SCAFFOLD
# --------------------------------------------------------------------------

ANCHORS: list[dict] = []
GATES: list[dict] = []
DISCLOSURES: list[dict] = []
_GATE_IDS: set[str] = set()
FIXTURE_EVALS = [0]
OUT: list[str] = []


def anchor(aid: str, quantity: str, committed, computed, source: str) -> None:
    ok = (committed == computed)
    ANCHORS.append({"id": aid, "quantity": quantity, "source": source,
                    "committed": committed, "computed": computed, "passed": ok})
    if not ok:
        sys.stderr.write(f"\nANCHOR FAILURE {aid}: {quantity}\n"
                         f"  source    : {source}\n"
                         f"  committed : {committed!r}\n"
                         f"  computed  : {computed!r}\n")
        sys.stdout.flush()
        sys.exit(1)


def gate(gid: str, claim: str, ok: bool, detail=None, must_pass: bool = True) -> bool:
    if gid in _GATE_IDS:
        raise RuntimeError(f"duplicate gate id {gid}")
    _GATE_IDS.add(gid)
    GATES.append({"id": gid, "claim": claim, "passed": bool(ok),
                  "must_pass": must_pass, "detail": detail})
    return bool(ok)


def disclose(did: str, statement: str, detail=None) -> None:
    DISCLOSURES.append({"id": did, "statement": statement, "detail": detail})


def say(s: str = "") -> None:
    OUT.append(s)
    print(s)


def progress(s: str) -> None:
    sys.stderr.write(f"[ha] {s}\n")
    sys.stderr.flush()


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for blk in iter(lambda: fh.read(65536), b""):
            h.update(blk)
    return h.hexdigest()


def note_fixture() -> None:
    FIXTURE_EVALS[0] += 1


def run_mode_label() -> str:
    """The run's mode, for the header only.  [instrument]"""
    return MUTANT if MUTANT is not None else "none (delivery run)"


# --------------------------------------------------------------------------
# 2.  THE DECLARED ARENA (data, not prose; RUNBOOK 15).  Frozen before any
#     fixture value is evaluated -- gate G01 measures the freeze.
# --------------------------------------------------------------------------


def link_set(d: int) -> list[tuple[int, ...]]:
    axes = [tuple(1 if k == j else 0 for k in range(d)) for j in range(d)]
    diags = [tuple(1 if k in (i, j) else 0 for k in range(d))
             for i in range(d) for j in range(i + 1, d)]
    return axes + diags


DECL: dict = {
    "d": 2,
    "L": 3,
    "d_ext": 3,
    "L_ext": 3,
    "links_d2": link_set(2),
    "links_d3": link_set(3),
    "records_d2": {
        "G-FLAT":     (1, 1, 2),
        "G-ANISO":    (1, 4, 5),
        "G-ANISO2":   (4, 9, 13),
        "G-DIAG2":    (2, 2, 4),
        "G-OFFDIAG":  (2, 2, 6),
        "G-OFFDIAG2": (3, 5, 12),
        "G-OFFNEG":   (3, 5, 4),
        "G-SINGULAR": (1, 1, 4),
        "G-INDEF":    (1, 1, 6),
    },
    "records_d2_inhomogeneous": ["G-CURVED (diagonal, site-dependent)",
                                 "G-CURVOFF (cross term, site-dependent)"],
    "records_d3": {"G3-FLAT": (1, 1, 1, 2, 2, 2),
                   "G3-ANISO": (1, 4, 9, 5, 10, 13),
                   "G3-OFF": (2, 2, 2, 6, 4, 4)},
    "density_weight": 0,
    "density_weight_flip": 1,
    "lapse_family": "the |X| site deltas, the constant profile 1, and the d chart ramps",
    "rules": [
        ("A-chart",       "A", "Lambda = delta (count-blind chart identity)"),
        ("A-axis",        "A", "Lambda = diag(1/n_{e_j}) from the axis interval counts"),
        ("A-linkframe",   "A", "Lambda^{ij} = sum_l e_l^i e_l^j / n_l over every declared link"),
        ("A-linkhalf",    "A", "Lambda = (1/2) sum_l e_l e_l^T / n_l"),
        ("A-insert",      "A", "Lambda = I_a(g), read from the record [POSITIVE CONTROL]"),
        ("A-insert-x",    "A", "Lambda = I_a(g) with the cross term sign-flipped [BROKEN]"),
        ("A-insert-2x",   "A", "Lambda = 2 I_a(g) [BROKEN]"),
        ("A-notransport", "A", "Lambda = I_a(g), drag read at a frozen reference front [BROKEN]"),
        ("B-axis",        "B", "lambda_l = 1/n_l on the axis links only"),
        ("B-all",         "B", "lambda_l = 1/n_l on every declared link"),
        ("B-chart",       "B", "lambda_l = 1 on the axis links only"),
    ],
    "broken_rules": ["A-insert-x", "A-insert-2x", "A-notransport"],
    "transported_rules": ["A-chart", "A-axis", "A-linkframe", "A-linkhalf",
                          "A-insert", "A-insert-x", "A-insert-2x"],
    "rules_d3": ["A-chart", "A-axis", "A-linkframe", "A-insert"],
    "frozen_front_rule": "A-notransport",
    "positive_control_rule": "A-insert",
    "primes": [5, 7, 13],
    "bridge_primes": [5, 7, 11, 13, 17, 19, 23],
    "registers": {"m == 0": "the zero address register",
                  "m == 1": "the unit address register"},
    "count_lattice": {"axis_max": 6, "diag_max": 12,
                      "description": "the declared box of count vectors "
                                     "(n_e1, n_e2, n_diag) swept for the "
                                     "link-locality theorem's witnesses"},
    "relation_sets": {"first-24": "the first 24 ordered lapse pairs of the "
                                  "declared enumeration",
                      "all": "every declared ordered lapse pair"},
    "test_class": ("the indicator effects of the reduced total-configuration carrier; "
                   "||R|| := the number of configurations R moves / carrier size"),
    "tangential_realisations": {
        "D-REG": "D_a[v] shifts the matter record's address register by v; the "
                 "geometry front is not transported (primary)",
        "D-TOT": "D_a[v] shifts the register AND drags the front along x -> x+v(x), "
                 "defined only where that site map is a bijection (flip-test)"},
    "chart_group": "the |X| chart translations and the d! direction relabellings, "
                   "acting on sites, on the record's link counts, on the lapse "
                   "profiles and on every tensor index",
    "bridge_coordinates": ["carrier", "family", "law", "state", "arena",
                           "structure group", "defect construction"],
}

# The freeze falsifier lives at module scope so that no gate-registering
# function ever references mutant identity.
if _M_FREEZE:
    note_fixture()


# --------------------------------------------------------------------------
# 3.  EXACT LINEAR ALGEBRA OVER Q
# --------------------------------------------------------------------------


def sites(d: int, L: int) -> list[tuple[int, ...]]:
    return [tuple(t) for t in itertools.product(range(L), repeat=d)]


def add(x, e, L):
    return tuple((a + b) % L for a, b in zip(x, e))


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
                M[r] = [vr - f * vc for vr, vc in zip(M[r], M[c])]
    return [M[i][n] for i in range(n)]


def det_exact(M):
    n = len(M)
    A = [row[:] for row in M]
    det = Fr(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if A[r][c] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            det = -det
        det *= A[c][c]
        pv = A[c][c]
        A[c] = [v / pv for v in A[c]]
        for r in range(c + 1, n):
            if A[r][c] != 0:
                f = A[r][c]
                A[r] = [vr - f * vc for vr, vc in zip(A[r], A[c])]
    return det


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


def rank_exact(rows_in) -> int:
    rows = [r[:] for r in rows_in]
    if not rows:
        return 0
    ncol = len(rows[0])
    r = 0
    for c in range(ncol):
        piv = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        pv = rows[r][c]
        rows[r] = [v / pv for v in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[r])]
        r += 1
    return r


# --------------------------------------------------------------------------
# 4.  THE GEOMETRY RECORD AND ITS METRIC CANDIDATE (v4 p7 Def 1.4)
# --------------------------------------------------------------------------
#
# The geometry record s is the INTERVAL-CARDINALITY record: n_l(x) is the number
# of division events in the record interval between site x and site x+l, for each
# link l of the declared record adjacency.  This is count data on the corpus's own
# division/record structure; GW1 1.2 permits event counts and record adjacency.
#
# The metric candidate is READ from that record by the corpus's own order+count
# readout -- the interval cardinality IS the squared separation:
#
#       q_{ij}(x) e_l^i e_l^j = n_l(x)     for every declared link l,
#       I_a(g)^{ij}(x) := ( q^{-1} )^{ij} (x)  * det q(x)^w ,   w declared.
#
# No embedding coordinate, no background normal, no planted frame, and no call to
# a metric estimator G_a enters anywhere.
# --------------------------------------------------------------------------


def sym_index(d):
    return [(i, j) for i in range(d) for j in range(i, d)]


def q_from_counts(d, counts):
    note_fixture()
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


class GeomRecord:
    def __init__(self, name, d, L, rule, weight):
        self.name, self.d, self.L, self.weight = name, d, L, weight
        self.links = link_set(d)
        self.counts = {x: {lk: int(rule(x, lk)) for lk in self.links}
                       for x in sites(d, L)}
        self.q, self.I = {}, {}
        self.singular_sites, self.nonpd_sites = [], []
        for x in sites(d, L):
            q = q_from_counts(d, {lk: Fr(self.counts[x][lk]) for lk in self.links})
            self.q[x] = q
            if q is None:
                self.singular_sites.append(x)
                self.I[x] = None
                continue
            if not positive_definite(q):
                self.nonpd_sites.append(x)
            qi = inv_exact(q)
            if _M_READLOCAL and qi is not None:
                qi = [[Fr(1, self.counts[x][self.links[i]]) if i == j else Fr(0)
                       for j in range(d)] for i in range(d)]
            if qi is None:
                self.I[x] = None
                continue
            if weight:
                dq = det_exact(q)
                qi = [[v * (dq ** weight) for v in row] for row in qi]
            self.I[x] = qi

    @property
    def admissible(self):
        return (not self.singular_sites and not self.nonpd_sites
                and all(self.I[x] is not None for x in self.I))


def make_record(name, d, L, tup, weight):
    table = {lk: tup[i] for i, lk in enumerate(link_set(d))}
    return GeomRecord(name, d, L, lambda x, lk: table[lk], weight)


def make_curved_record(name, d, L, weight):
    """Inhomogeneous, exactly DIAGONAL: q(x) = diag(1+x_1, ..., 1+x_d)."""
    def rule(x, lk):
        return sum((1 + x[j]) for j in range(d) if lk[j])
    return GeomRecord(name, d, L, rule, weight)


def make_curved_off_record(name, d, L, weight):
    """Inhomogeneous with a site-dependent CROSS term."""
    def rule(x, lk):
        b = [2 + x[j] for j in range(d)]
        cross = 1 + (x[0] * x[1]) % 2
        s = sum(b[j] for j in range(d) if lk[j])
        pairs = sum(1 for i in range(d) for j in range(i + 1, d) if lk[i] and lk[j])
        return s + 2 * cross * pairs
    return GeomRecord(name, d, L, rule, weight)


# --------------------------------------------------------------------------
# 5.  THE RECORD-NATIVE H_a[N]  (v4 paper 7 Definition 1.3, CONSTRUCTED)
# --------------------------------------------------------------------------
#
# A total finite matter-geometry record is c = (n, m) over a frozen geometry
# sector s:
#     n : X -> Z    the FRONT.  n(x) = the number of division events already
#                   committed at record site x.
#     m : X -> Q^d  the matter record's ADDRESS REGISTER: the recorded tangential
#                   address of the matter carrier at x.
# V_a^tot := R^{C^matter x C^geom} (Def 1.1).  Every comparison map below is the
# pushforward by a BIJECTION of the total configuration set, hence an invertible
# algebraic map on V_a^tot exactly as Definition 1.3 requires -- constructed, not
# declared.
#
#     H_a[N](n, m) = ( n + N ,  m + w[N,n] )
#     H_a[N]^{-1}(n, m) = ( n - N ,  m - w[N, n-N] )        (exact, closed form)
#
# with the RECORD-NATIVE drag field
#
#   arch A:  w[N,n]^i(x) = N(x) * sum_j Lambda^{ij}(x) ( n(x+e_j) - n(x) )
#   arch B:  w[N,n]^i(x) = N(x) * sum_l lambda_l(x) e_l^i ( n(x+e_l) - n(x) ).
#
# The front tilt n(x+e)-n(x) is a difference of committed division-event counts
# and N(x) is an eventwise lapse value; both are permitted by GW1 1.2.  In
# H_a[M] H_a[N] the M-step's drag is evaluated at the ALREADY-ADVANCED front
# n+N: the second normal step is TRANSPORTED along the first (GW1 1.1 cond. 3).
# --------------------------------------------------------------------------

_LAMBDA_CACHE: dict = {}
_CACHE_STATS = {"hits": 0, "misses": 0, "bypass": 0}


def arch_of(rule: str) -> str:
    return "B" if rule.startswith("B-") else "A"


def lambda_of(rule, rec, x, fresh=False):
    """The drag rule's weight at site x.  [instrument -- mutable cache path]"""
    memo_name = rec.name.split("@")[0] if _M_ALIAS else rec.name
    key = (rule, memo_name, rec.weight, x)
    use_cache = (not fresh) or _M_CACHE
    if fresh and not _M_CACHE:
        _CACHE_STATS["bypass"] += 1
    if use_cache and key in _LAMBDA_CACHE:
        _CACHE_STATS["hits"] += 1
        return _LAMBDA_CACHE[key]
    if use_cache:
        _CACHE_STATS["misses"] += 1
    note_fixture()
    d = rec.d
    cnt = rec.counts[x]
    lks = rec.links
    axes = lks[:d]
    if rule == "A-chart":
        M = [[Fr(1) if i == j else Fr(0) for j in range(d)] for i in range(d)]
    elif rule == "A-axis":
        M = [[Fr(0)] * d for _ in range(d)]
        for j in range(d):
            M[j][j] = Fr(1, cnt[axes[j]])
    elif rule in ("A-linkframe", "A-linkhalf"):
        M = [[Fr(0)] * d for _ in range(d)]
        for lk in lks:
            w = Fr(1, cnt[lk])
            for i in range(d):
                for j in range(d):
                    M[i][j] += Fr(lk[i] * lk[j]) * w
        if rule == "A-linkhalf":
            M = [[v / 2 for v in row] for row in M]
    elif rule in ("A-insert", "A-notransport"):
        M = [row[:] for row in rec.I[x]]
    elif rule == "A-insert-x":
        M = [[(-v if i != j else v) for j, v in enumerate(row)]
             for i, row in enumerate(rec.I[x])]
    elif rule == "A-insert-2x":
        M = [[2 * v for v in row] for row in rec.I[x]]
    elif rule == "B-axis":
        M = {lk: (Fr(1, cnt[lk]) if lk in axes else Fr(0)) for lk in lks}
    elif rule == "B-all":
        M = {lk: Fr(1, cnt[lk]) for lk in lks}
    elif rule == "B-chart":
        M = {lk: (Fr(1) if lk in axes else Fr(0)) for lk in lks}
    else:
        raise RuntimeError(f"unknown rule {rule}")
    if use_cache:
        _LAMBDA_CACHE[key] = M
    return M


def drag(rule, rec, N, n):
    d, L = rec.d, rec.L
    out = {}
    if arch_of(rule) == "A":
        axes = rec.links[:d]
        for x in sites(d, L):
            Lam = lambda_of(rule, rec, x)
            dn = [Fr(n[add(x, e, L)] - n[x]) for e in axes]
            out[x] = tuple(sum((Lam[i][j] * dn[j] for j in range(d)), Fr(0)) * Fr(N[x])
                           for i in range(d))
    else:
        for x in sites(d, L):
            lam = lambda_of(rule, rec, x)
            v = [Fr(0)] * d
            for lk in rec.links:
                if lam[lk] == 0:
                    continue
                dl = Fr(n[add(x, lk, L)] - n[x])
                for i in range(d):
                    if lk[i]:
                        v[i] += lam[lk] * Fr(lk[i]) * dl
            out[x] = tuple(Fr(N[x]) * v[i] for i in range(d))
    return out


def drag_at(rule, rec, N, n, x):
    """The drag field at one site.  Identical formula to drag(); used where only
    the detector site is needed."""
    d, L = rec.d, rec.L
    if arch_of(rule) == "A":
        Lam = lambda_of(rule, rec, x)
        dn = [Fr(n[add(x, e, L)] - n[x]) for e in rec.links[:d]]
        return tuple(sum((Lam[i][j] * dn[j] for j in range(d)), Fr(0)) * Fr(N[x])
                     for i in range(d))
    lam = lambda_of(rule, rec, x)
    v = [Fr(0)] * d
    for lk in rec.links:
        if lam[lk] == 0:
            continue
        dl = Fr(n[add(x, lk, L)] - n[x])
        for i in range(d):
            if lk[i]:
                v[i] += lam[lk] * Fr(lk[i]) * dl
    return tuple(Fr(N[x]) * v[i] for i in range(d))


class Hmap:
    """H_a[N] as a bijection of total records.  [instrument -- mutable transport]"""

    def __init__(self, rule, rec, N, frozen_front=None):
        self.rule, self.rec, self.N = rule, rec, N
        self.frozen_front = frozen_front
        if _M_TRANSPORT and frozen_front is None:
            self.frozen_front = "PRE"

    def _w(self, n, pre=None):
        if self.frozen_front == "PRE":
            src = pre if pre is not None else n
        elif self.frozen_front is not None:
            src = self.frozen_front
        else:
            src = n
        return drag(self.rule, self.rec, self.N, src)

    def fwd(self, c):
        n, m = c
        w = self._w(n)
        n2 = {x: n[x] + self.N[x] for x in n}
        m2 = {x: tuple(m[x][i] + w[x][i] for i in range(self.rec.d)) for x in m}
        return (n2, m2)

    def inv(self, c):
        n, m = c
        n2 = {x: n[x] - self.N[x] for x in n}
        w = self._w(n2, pre=n)
        m2 = {x: tuple(m[x][i] - w[x][i] for i in range(self.rec.d)) for x in m}
        return (n2, m2)


class Dmap:
    """D_a[v], the tangential comparison map (v4 p7 Def 1.2), two realisations."""

    def __init__(self, rec, v, realisation="D-REG"):
        self.rec, self.v, self.realisation = rec, v, realisation

    def fwd(self, c):
        n, m = c
        d = self.rec.d
        m2 = {x: tuple(m[x][i] + self.v[x][i] for i in range(d)) for x in m}
        if self.realisation == "D-REG":
            return (n, m2)
        sm = self.site_map()
        if sm is None:
            raise RuntimeError("D-TOT undefined: the site map is not a bijection")
        return ({sm[x]: n[x] for x in n}, m2)

    def site_map(self):
        d, L = self.rec.d, self.rec.L
        out = {}
        for x in sites(d, L):
            sh = self.v[x]
            if any(t.denominator != 1 for t in sh):
                return None
            out[x] = tuple((x[i] + int(sh[i])) % L for i in range(d))
        return out if len(set(out.values())) == L ** d else None


def check_bijection_pair(H, c):
    """Measured invertibility of a comparison map.  [instrument -- mutable]"""
    if _M_INVERT:
        return True
    return H.inv(H.fwd(c)) == c and H.fwd(H.inv(c)) == c


class RegisterCollapse:
    """The declared NON-INJECTIVE falsifier for the invertibility gate."""

    def __init__(self, rec):
        self.rec = rec

    def fwd(self, c):
        n, m = c
        return ({x: n[x] for x in n},
                {x: tuple(Fr(0) for _ in range(self.rec.d)) for x in m})

    def inv(self, c):
        return self.fwd(c)


# --------------------------------------------------------------------------
# 6.  THE FINITE BRACKET COVECTOR, beta, AND THE RESIDUAL R_HH
# --------------------------------------------------------------------------


def omega(N, M, rec):
    """omega_j(x) := N(x) M(x+e_j) - M(x) N(x+e_j) = (N d_j M - M d_j N)(x).
    [instrument -- mutable sign convention]"""
    note_fixture()
    d, L = rec.d, rec.L
    axes = rec.links[:d]
    sgn = -1 if _M_SIGN else 1
    if _M_OMASYM:
        return {x: tuple(Fr(N[x] * M[add(x, e, L)] - M[add(x, e, L)] * N[add(x, e, L)])
                         for e in axes) for x in sites(d, L)}
    return {x: tuple(Fr(sgn * (N[x] * M[add(x, e, L)] - M[x] * N[add(x, e, L)]))
                     for e in axes) for x in sites(d, L)}


def omega_link(N, M, rec):
    d, L = rec.d, rec.L
    sgn = -1 if _M_SIGN else 1
    return {x: {lk: Fr(sgn * (N[x] * M[add(x, lk, L)] - M[x] * N[add(x, lk, L)]))
                for lk in rec.links} for x in sites(d, L)}


def beta(rec, N, M):
    """beta_a^i(g;N,M) = I_a(g)^{ij} ( N d_j M - M d_j N )   (v4 p7 Def 1.4)."""
    d, L = rec.d, rec.L
    om = omega(N, M, rec)
    out = {}
    for x in sites(d, L):
        I = ([[Fr(1) if i == j else Fr(0) for j in range(d)] for i in range(d)]
             if _M_BETAFLAT else rec.I[x])
        out[x] = tuple(sum((I[i][j] * om[x][j] for j in range(d)), Fr(0))
                       for i in range(d))
    return out


def residual_field_literal(rule, rec, N, M, n0, realisation="D-REG"):
    """R_{HH,a}[N,M] := H[N]H[M]H[N]^-1 H[M]^-1 D[-beta], applied LITERALLY.
    [instrument -- mutable factor order]"""
    d, L = rec.d, rec.L
    fz = n0 if rule == "A-notransport" else None
    HN, HM = Hmap(rule, rec, N, fz), Hmap(rule, rec, M, fz)
    b = beta(rec, N, M)
    D = Dmap(rec, {x: tuple(-b[x][i] for i in range(d)) for x in b}, realisation)
    c = (dict(n0), {x: tuple(Fr(0) for _ in range(d)) for x in sites(d, L)})
    seq = [D.fwd, HM.inv, HN.inv, HM.fwd, HN.fwd]
    if _M_ORDER:
        seq = [D.fwd, HN.inv, HM.inv, HN.fwd, HM.fwd]
    for f in seq:
        c = f(c)
    n1, m1 = c
    if any(n1[x] != n0[x] for x in n0):
        return None
    return dict(m1)


def residual_field_closed(rule, rec, N, M):
    """The INDEPENDENT comparator, built from the drag rule and the record readout
    directly; it never routes through Hmap, Dmap or residual_field_literal.

        arch A:  rho^i(x) = sum_j ( Lambda^{ij}(x) - I^{ij}(x) ) omega_j(x)
        arch B:  rho^i(x) = sum_l lambda_l(x) e_l^i omega_l(x) - beta^i(x)
    """
    d, L = rec.d, rec.L
    b = beta(rec, N, M)
    out = {}
    if rule == "A-notransport":
        # the declared broken variant: its drag reads a FROZEN reference front, so
        # its normal steps commute in the register and the commutator contributes
        # nothing; the residual is the uncancelled tangential correction alone.
        return {x: tuple(-b[x][i] for i in range(d)) for x in sites(d, L)}
    if arch_of(rule) == "A":
        om = omega(N, M, rec)
        for x in sites(d, L):
            Lam = lambda_of(rule, rec, x)
            out[x] = tuple(sum((Lam[i][j] * om[x][j] for j in range(d)), Fr(0)) - b[x][i]
                           for i in range(d))
    else:
        oml = omega_link(N, M, rec)
        for x in sites(d, L):
            lam = lambda_of(rule, rec, x)
            v = [Fr(0)] * d
            for lk in rec.links:
                if lam[lk] == 0:
                    continue
                for i in range(d):
                    if lk[i]:
                        v[i] += lam[lk] * Fr(lk[i]) * oml[x][lk]
            out[x] = tuple(v[i] - b[x][i] for i in range(d))
    return out


def closes(field) -> bool:
    """The closure predicate.  [instrument -- mutable]"""
    if _M_CLOSURE:
        return True
    if field is None:
        return False
    return all(all(t == 0 for t in v) for v in field.values())


def site_closes(field, x) -> bool:
    if _M_CLOSURE:
        return True
    if field is None:
        return False
    return all(t == 0 for t in field[x])


def field_max(field) -> Fr:
    if field is None:
        return Fr(-1)
    return max((abs(t) for v in field.values() for t in v), default=Fr(0))


# --------------------------------------------------------------------------
# 7.  THE FINITE OPERATOR LAYER (exact F_p)
# --------------------------------------------------------------------------


def to_Fp(v: Fr, p: int):
    """Exact reduction Q -> F_p.  [instrument -- mutable]"""
    den = v.denominator % p
    if den == 0:
        return None
    r = (v.numerator % p) * pow(den, -1, p) % p
    return (r * r) % p if _M_FACTOR else r


class ReducedCarrier:
    """A declared finite total-configuration carrier for the operator layer:
       C_red = F x A, F = the front sector n0 + span_{F_p}{the lapses in play},
       A = (F_p)^d, the address register at the declared detector site x*."""

    def __init__(self, rec, p, n0, lapses, xstar):
        self.rec, self.p, self.n0, self.xstar = rec, p, n0, xstar
        d, L = rec.d, rec.L
        S = sites(d, L)
        self.S = S
        basis = []
        for N in lapses:
            if self._rank(basis + [N], S) > self._rank(basis, S):
                basis.append(N)
        self.basis, self.k = basis, len(basis)
        self.fronts = []
        for co in itertools.product(range(p), repeat=self.k):
            self.fronts.append({x: (n0[x] + sum(co[i] * basis[i][x]
                                                for i in range(self.k))) % p for x in S})
        self.front_index = {tuple(sorted(f.items())): i for i, f in enumerate(self.fronts)}
        self.regs = list(itertools.product(range(p), repeat=d))
        self.reg_index = {r: i for i, r in enumerate(self.regs)}
        self.size = len(self.fronts) * len(self.regs)

    def _rank(self, vs, S):
        p = self.p
        rows = [[v[x] % p for x in S] for v in vs]
        r = 0
        for c in range(len(S)):
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

    def decode(self, k):
        return divmod(k, len(self.regs))

    def perm_H(self, rule, N, frozen_front=None):
        p, d, xs = self.p, self.rec.d, self.xstar
        out = [0] * self.size
        nreg = len(self.regs)
        for fi, f in enumerate(self.fronts):
            src = frozen_front if frozen_front is not None else f
            w = drag_at(rule, self.rec, N, src, xs)
            wp = [to_Fp(w[i], p) for i in range(d)]
            if any(t is None for t in wp):
                return None
            key = tuple(sorted({x: (f[x] + N[x]) % p for x in f}.items()))
            if key not in self.front_index:
                return None
            fj = self.front_index[key]
            for ri, reg in enumerate(self.regs):
                r2 = tuple((reg[i] + wp[i]) % p for i in range(d))
                out[fi * nreg + ri] = self.code(fj, r2)
        return out

    def perm_D(self, v):
        p, d, xs = self.p, self.rec.d, self.xstar
        vp = [to_Fp(v[xs][i], p) for i in range(d)]
        if any(t is None for t in vp):
            return None
        out = [0] * self.size
        nreg = len(self.regs)
        for fi in range(len(self.fronts)):
            for ri, reg in enumerate(self.regs):
                r2 = tuple((reg[i] + vp[i]) % p for i in range(d))
                out[fi * nreg + ri] = self.code(fi, r2)
        return out


def perm_compose(a, b):
    return [a[k] for k in b]


def perm_inv(a):
    out = [0] * len(a)
    for i, v in enumerate(a):
        out[v] = i
    return out


def perm_moved(a):
    return sum(1 for i, v in enumerate(a) if i != v)


def perm_mul(a, b):
    return [a[i] for i in b]


def perm_order(a):
    ident = list(range(len(a)))
    c, cur = 1, list(a)
    while cur != ident:
        cur = perm_mul(list(a), cur)
        c += 1
        if c > 10 ** 6:
            raise RuntimeError("order overflow")
    return c


def group_closure(gens, ident):
    seen, frontier = {ident}, [ident]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                x = tuple(perm_mul(list(g), list(h)))
                if x not in seen:
                    seen.add(x)
                    nxt.append(x)
        frontier = nxt
        if len(seen) > 100000:
            raise RuntimeError("group too large")
    return seen


# --------------------------------------------------------------------------
# 8.  THE DETECTOR (v4 paper 12 Definition 11.6M)
# --------------------------------------------------------------------------


def lie_lapse(rec, B, N):
    """The declared finite transported lapse derivative  L_B N = B^j d_j N."""
    d, L = rec.d, rec.L
    axes = rec.links[:d]
    return {x: sum((B[x][j] * Fr(N[add(x, axes[j], L)] - N[x]) for j in range(d)), Fr(0))
            for x in sites(d, L)}


def switch_commutator(rule, rec, N, B, n0):
    """C(H_a[N], D_a[B]) = H[N] D[B] H[N]^-1 D[B]^-1, applied to (n0, 0)."""
    d, L = rec.d, rec.L
    HN = Hmap(rule, rec, N)
    D = Dmap(rec, B, "D-REG")
    Dinv = Dmap(rec, {x: tuple(-B[x][i] for i in range(d)) for x in B}, "D-REG")
    c = (dict(n0), {x: tuple(Fr(0) for _ in range(d)) for x in sites(d, L)})
    for f in [Dinv.fwd, HN.inv, D.fwd, HN.fwd]:
        c = f(c)
    return ({x: c[0][x] - n0[x] for x in n0}, dict(c[1]))


def W_maps(rule, rec, X, B, n0):
    """The corrected normal-tangential switch W_{X|..,a} := C(H_a[X], D_a[B])
    H_a[L_B X], as the ordered list of comparison maps to apply (rightmost first)."""
    d = rec.d
    HX = Hmap(rule, rec, X)
    Hs = Hmap(rule, rec, lie_lapse(rec, B, X))
    D = Dmap(rec, B, "D-REG")
    Dinv = Dmap(rec, {x: tuple(-B[x][i] for i in range(d)) for x in B}, "D-REG")
    return [Hs.fwd, Dinv.fwd, HX.inv, D.fwd, HX.fwd]


def sw_hhh(rule, rec, N, M, Lp, n0):
    """SW_{HHH,a}(N,M,L) := W_{N|ML} W_{M|LN} W_{L|NM}, applied LITERALLY to
    (n0, 0).  Returns the front displacement, the register displacement, and the
    cyclic Jacobi lapse sum."""
    d, L = rec.d, rec.L
    B_ML, B_LN, B_NM = beta(rec, M, Lp), beta(rec, Lp, N), beta(rec, N, M)
    seq = (W_maps(rule, rec, Lp, B_NM, n0) + W_maps(rule, rec, M, B_LN, n0)
           + W_maps(rule, rec, N, B_ML, n0))
    c = (dict(n0), {x: tuple(Fr(0) for _ in range(d)) for x in sites(d, L)})
    for f in seq:
        c = f(c)
    jac = {x: (lie_lapse(rec, B_ML, N)[x] + lie_lapse(rec, B_LN, M)[x]
               + lie_lapse(rec, B_NM, Lp)[x]) for x in sites(d, L)}
    return ({x: c[0][x] - n0[x] for x in n0}, dict(c[1]), jac)


# --------------------------------------------------------------------------
# 9.  THE BRIDGE OBJECTS (NT / GEN stitching geometry)
# --------------------------------------------------------------------------


def gen_sigma():
    """The pair-label exchange on the 9 system-pair indices, a = 3 s_A + s_B."""
    return [3 * (i % 3) + (i // 3) for i in range(9)]


def gen_defect(Q):
    """GEN's defect law  D = Sigma Q^T Sigma Q  (paper-gen 8.1) at completion Q."""
    S = gen_sigma()
    return perm_mul(S, perm_mul(perm_inv(Q), perm_mul(S, Q)))


def operator_primes():
    """The primes the finite operator layer is realised over.  [instrument]"""
    return DECL["primes"][:1] if _M_ONEPRIME else DECL["primes"]


def sweep_primes():
    """The primes the bridge's coordinate audit rebuilds the reduced carrier over.
    [instrument -- mutable]"""
    return DECL["bridge_primes"][:1] if _M_ONEPRIME else DECL["bridge_primes"]


def comparator_spectrum(defect_orders, holonomy_orders):
    """The GEN spectrum the HA holonomy order is compared against.

    GEN publishes TWO order spectra: the DEFECT's, and the holonomy group's
    (2n over the defect orders n, with the flat class at 1).  The coordinate
    table pairs R_HH with GEN's DEFECT D, so the defect spectrum is the
    like-for-like comparator, and both are computed here from the completion
    census of A14 rather than typed.  [instrument -- mutable]"""
    return set(holonomy_orders) if _M_SPECTRUM else set(defect_orders)


def rules_tested():
    """The declared drag-rule family actually carried into the census.
    [instrument -- mutable]"""
    rs = list(DECL["rules"])
    return [r for r in rs if r[0] != "A-linkhalf"] if _M_CENSUS else rs


def derive_verdict(runnable, bridge_token):
    """The verdict string, derived from the measured outcomes.  Gate G25
    recomputes it from the measured counts and compares.
    [instrument -- mutable]"""
    if _M_VERDICT:
        return ["HA-RUNNABLE", "HA-BRIDGE-POSABLE"]
    return (["HA-RUNNABLE"] if runnable else ["HA-STILL-BLOCKED"]) + [bridge_token]


# --------------------------------------------------------------------------
# 10.  THE AST GUARD  (RUNBOOK 14 addendum, v13 #208)
# --------------------------------------------------------------------------


def ast_float_scan(src: str) -> list[str]:
    """Every float literal, and every call of float()/complex(), in the source.
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
    """Names of functions that BOTH register a gate AND reference run-mode
    identity -- MUTANT/MUTANTS, a per-mutant switch, a mutant-name literal, one
    of the run-mode booleans (DELIVERY_RUN is mutant identity under another
    name), or sys.argv.  [instrument -- mutable]"""
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
                        and sub.func.id == "gate":
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


# --------------------------------------------------------------------------
# 11.  INSTRUMENT HELPERS THAT CARRY THE ANCHOR MUTATIONS
# --------------------------------------------------------------------------

FROZEN_TREES = ["code", "v7/code", "v10/code", "v8/code", "v9/code",
                "_archive_low_value_2026-06-14/code", "external/walsh-delta-code",
                "v11/code", "bc/code", "v6/code"]


def count_py(tree: str) -> int:
    p = os.path.join(REPO, tree)
    if not os.path.isdir(p):
        return -1
    n = len([f for f in os.listdir(p) if f.endswith(".py")])
    return n + 1 if (_M_TREES and tree == "code") else n


def count_lapse_files(tree: str) -> int:
    p = os.path.join(REPO, tree)
    if not os.path.isdir(p):
        return -1
    c = 0
    for f in sorted(os.listdir(p)):
        if not f.endswith(".py"):
            continue
        txt = open(os.path.join(p, f), "r", encoding="utf-8", errors="replace").read()
        if "lapse" in set(re.findall(r"[A-Za-z_]+", txt)):
            c += 1
    return c + 1 if (_M_LAPSE and tree == "code") else c


def nt_receipt_sha(path: str) -> str:
    s = sha256_file(path)
    return (s[:-1] + ("0" if s[-1] != "0" else "1")) if _M_NTS else s


def nt_total_paths(nt) -> int:
    t = sum(v["paths"] for k, v in nt["tables"]["path_space"].items()
            if not k.startswith("_"))
    return t + 1 if _M_NTP else t


def gen_family_size(fam) -> int:
    return len(fam) + 1 if _M_GENF else len(fam)


def gen_declared_defect(Q):
    D = gen_defect(Q)
    if _M_GEND:
        D = D[:]
        D[0], D[4] = D[4], D[0]
    return D


def gen_order_spectrum(hist: dict) -> dict:
    """GEN's measured defect order spectrum over the completion family.
    [instrument -- mutable]"""
    out = dict(sorted(hist.items()))
    if _M_GENS and out:
        k = sorted(out)[-1]
        out[k] = out[k] + 1
    return out


def build_lapse_family(S, d):
    """The declared lapse family.  [instrument -- mutable]"""
    if _M_RANK:
        return [(f"const{i}", {y: i + 1 for y in S}) for i in range(len(S) + 1 + d)]
    lp = [(f"delta{x}", {y: (1 if y == x else 0) for y in S}) for x in S]
    lp.append(("one", {y: 1 for y in S}))
    lp += [(f"ramp{j}", {y: y[j] for y in S}) for j in range(d)]
    return lp


def broken_rules_tested():
    """The declared broken-H set actually carried into the control.
    [instrument -- mutable]"""
    return [] if _M_CONTROL else list(DECL["broken_rules"])


def chart_index(x, sigma, d):
    """phi_sigma(x)_i = x_{sigma(i)}.  [instrument -- mutable]"""
    if _M_CHART:
        return x
    return tuple(x[sigma[i]] for i in range(d))



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
            if re.match(r"^G\d+B?\s+FAIL", ls):
                why.append("G:" + ls.split()[0])
        rows.append({"mutant": name, "expected_kill": MUTANTS[name],
                     "exit": pr.returncode, "killed": pr.returncode == 1,
                     "named_kills": sorted(set(why))})
        progress(f"  mutant {name}: exit {pr.returncode}")
    say(f"  {'mutant':20s}{'exit':6s}{'killed':9s}named kills")
    for row in rows:
        say(f"  {row['mutant']:20s}{row['exit']:<6d}{str(row['killed']):9s}"
            f"{','.join(row['named_kills'])[:58]}")
    surv = [r_["mutant"] for r_ in rows if not r_["killed"]]
    kg = {k[2:] for r_ in rows for k in r_["named_kills"] if k.startswith("G:")}
    nf = sorted(g["id"] for g in GATES if g["must_pass"] and g["id"] not in kg)
    say(f"  mutants that survived : {surv}")
    say(f"  must-pass gates never falsified by any mutant : {nf}")
    return rows, surv, nf


# ==========================================================================
#                                  MAIN
# ==========================================================================


def run_unit(src: str) -> dict:
    """The whole measurement, from the anchors to the verdict.  Registers every
    gate; reads no run-mode boolean, directly or indirectly (G23)."""
    progress("start")
    say("=" * 78)
    say("HA -- THE RECORD-NATIVE H_a[N] SUCCESSOR   (v13 gravity line)")
    say("pin: v13/note-ha-successor-pin.md    immutable base commit 024fcd7")
    say("binding: v13/note-gw1-metric-from-closure.md 7.1 (the successor, ordered);")
    say("         v4 paper 7 Defs 1.1-1.4 / 2.1-2.5; v4 paper 12 Def 11.6M")
    say("=" * 78)
    say(f"run mode            : {run_mode_label()}")
    say(f"python              : {platform.python_version()}")
    say(f"instrument sha256   : {hashlib.sha256(src.encode()).hexdigest()}")
    say("arithmetic          : fractions.Fraction, integers, exact F_p.  No floats.")
    say("")

    # ======================= 1. ANCHORS (exit-1-only) =====================
    say("--- 1. ANCHORS (exit-1-only) ---")
    progress("anchors")
    committed_trees = {"code": 353, "v7/code": 273, "v10/code": 137, "v8/code": 101,
                       "v9/code": 84, "_archive_low_value_2026-06-14/code": 9,
                       "external/walsh-delta-code": 8, "v11/code": 7,
                       "bc/code": 3, "v6/code": 1}
    anchor("A01", "GW1 census: .py counts of the frozen runnable trees",
           committed_trees, {t: count_py(t) for t in FROZEN_TREES},
           "v13/note-gw1-metric-from-closure.md 4 (TERMINAL, v13 LOG #5)")
    anchor("A02", "GW1 census: .py at the repository root", 3,
           len([f for f in os.listdir(REPO) if f.endswith(".py")]),
           "v13/note-gw1-metric-from-closure.md 4")
    anchor("A03", "GW1 census: files in code/ carrying the token 'lapse'", 12,
           count_lapse_files("code"), "v13/note-gw1-metric-from-closure.md 4")
    anchor("A04", "GW1 census: files carrying 'lapse' in every other frozen tree",
           {t: 0 for t in FROZEN_TREES if t != "code"},
           {t: count_lapse_files(t) for t in FROZEN_TREES if t != "code"},
           "v13/note-gw1-metric-from-closure.md 4")

    nt_path = os.path.join(REPO, "v13/code/nt_transport_receipt.json")
    gen_path = os.path.join(REPO, "v13/code/gen_generality_receipt.json")
    anchor("A05", "NT receipt sha256 (hash pin)",
           "d256891b479a8636fe88df5e9b0f553998140f1553fdfc167662220b44eeb03e",
           nt_receipt_sha(nt_path), "v13/code/nt_transport_receipt.json")
    anchor("A06", "GEN receipt sha256 (hash pin)",
           "e0b2f444f6a9b82861024f7733c7230583742dfd477d9ed6037a241e7b48d292",
           sha256_file(gen_path), "v13/code/gen_generality_receipt.json")
    nt = json.load(open(nt_path))
    anchor("A07", "NT: total reduced paths over the six settings", 34024,
           nt_total_paths(nt), "v13/paper-nt-nomological-transport.md 3.2")
    anchor("A08", "NT: the based holonomy group order per setting",
           {"SP-A": 1, "SP-B": 1, "SP-C": 1, "SP-D": 1, "SP-E": 4, "SP-F": 4},
           {k: v["generated_group_order"] for k, v in
            sorted(nt["findings"]["holonomy_group"]["per_setting"].items())},
           "v13/paper-nt-nomological-transport.md 8.2")

    progress("GEN completion family, independently rebuilt from the paper's prose")
    ident9 = list(range(9))
    fam = {tuple([0] + list(t)): gen_defect([0] + list(t))
           for t in itertools.permutations(range(1, 9))}
    anchor("A09", "GEN: the declared completion family's size", 40320,
           gen_family_size(fam), "v13/paper-gen-generality-check.md 8.2")
    triv = sum(1 for D in fam.values() if D == ident9)
    anchor("A10", "GEN: completions whose defect is the identity", 96, triv,
           "v13/paper-gen-generality-check.md 8.2")
    anchor("A11", "GEN: geometry-bearing completions", 40224, len(fam) - triv,
           "v13/paper-gen-generality-check.md 8.2")
    Q_declared = [0, 2, 1, 3, 4, 5, 6, 7, 8]   # gen 2.3: transposition of |0,1>,|0,2>
    D_declared = gen_declared_defect(Q_declared)
    anchor("A12", "GEN: the declared completion's defect permutation",
           [0, 2, 1, 6, 4, 5, 3, 7, 8], D_declared,
           "v13/code/gen_generality_receipt.json tables.completion_census")
    anchor("A13", "GEN: the declared defect's fixed configurations of 81", 45,
           sum(1 for i in range(9) if D_declared[i] == i) * 9,
           "v13/paper-gen-generality-check.md 8.1")
    ord_hist, fix_hist, dihedral_fail = {}, {}, 0
    S9 = gen_sigma()
    for D in fam.values():
        o = perm_order(D)
        ord_hist[o] = ord_hist.get(o, 0) + 1
        nf = sum(1 for i in range(9) if D[i] == i) * 9
        fix_hist[nf] = fix_hist.get(nf, 0) + 1
        if perm_mul(S9, perm_mul(D, S9)) != perm_inv(D):
            dihedral_fail += 1
    defect_spectrum = gen_order_spectrum(ord_hist)
    anchor("A14", "GEN: the order spectrum of the defect over the whole family",
           {1: 96, 2: 1440, 3: 4224, 4: 4608, 5: 4608, 6: 6912, 7: 9216, 15: 9216},
           defect_spectrum, "v13/paper-gen-generality-check.md 8.2")
    anchor("A15", "GEN: the fixed-configuration spectrum of the defect",
           {9: 16704, 18: 11520, 27: 5376, 36: 4608, 45: 864, 54: 1152, 81: 96},
           dict(sorted(fix_hist.items())), "v13/paper-gen-generality-check.md 8.2")
    anchor("A16", "GEN: members where the dihedral relation Sigma D Sigma = D^-1 fails",
           0, dihedral_fail, "v13/paper-gen-generality-check.md 8.3")
    holonomy_spectrum = sorted({(1 if n == 1 else 2 * n) for n in defect_spectrum})
    anchor("A17", "GEN: the predicted holonomy order spectrum, derived from the "
           "defect spectrum (2n, with the flat class at 1)",
           [1, 4, 6, 8, 10, 12, 14, 30], holonomy_spectrum,
           "v13/paper-gen-generality-check.md 8.2-8.3")
    say(f"  {len(ANCHORS)} anchors, every one reproduced.")
    say("  DISCLOSURE X01: v12/code and v13/code are LIVE trees, written by concurrent")
    say("  cycles, and are excluded from A01 BY DECLARATION, not by outcome.  No count")
    say("  of either is taken here: a count of a tree this unit does not own is not")
    say("  reproducible by construction, and the delivery's byte-identity would then")
    say("  depend on directories outside the unit.  The GW1 census's own committed")
    say("  value for v12/code is 5; v13/code is not in that census at all.")
    disclose("X01", "two trees are LIVE and are excluded from A01 by declaration, "
             "with no live count taken -- a count of a concurrently written tree is "
             "not reproducible by construction",
             {"v12/code": {"census": 5, "live_count": "not taken"},
              "v13/code": {"census": "not listed", "live_count": "not taken"}})
    say("")

    # ======================= 2. THE DECLARED ARENA ========================
    say("--- 2. THE DECLARED ARENA (data; frozen before any fixture value) ---")
    progress("declarations")
    for k in DECL:
        v = DECL[k]
        s = str(v) if isinstance(v, (int, str)) else json.dumps(v, default=str)
        say(f"  {k:26s} : {s[:200]}")
    g01 = gate("G01", "THE DECLARATIONS ARE FROZEN BEFORE FIXTURE TRUTH (RUNBOOK "
               "13(4)): the fixture-evaluation counter is measured zero at the "
               "freeze point", FIXTURE_EVALS[0] == 0,
               {"fixture_evals_at_freeze": FIXTURE_EVALS[0]})
    say(f"  fixture evaluations at the freeze point: {FIXTURE_EVALS[0]}   "
        f"(G01 {'PASS' if g01 else 'FAIL'})")
    say("")

    # ======================= 3. THE RECORDS ===============================
    say("--- 3. THE GEOMETRY RECORDS AND THE RECORD-READ METRIC CANDIDATE ---")
    progress("records")
    d, L, W = DECL["d"], DECL["L"], DECL["density_weight"]
    S = sites(d, L)
    RULES = rules_tested()
    recs = {nm: make_record(nm, d, L, tup, W) for nm, tup in DECL["records_d2"].items()}
    recs["G-CURVED"] = make_curved_record("G-CURVED", d, L, W)
    recs["G-CURVOFF"] = make_curved_off_record("G-CURVOFF", d, L, W)
    x1 = tuple(1 for _ in range(d))
    say(f"  {'record':12s}{'counts at (0,0)':16s}{'counts at (1,1)':16s}{'q(0,0)':20s}"
        f"{'I=q^-1(0,0)':28s}{'homog':7s}adm")
    for nm in sorted(recs):
        r = recs[nm]
        x0 = (0,) * d
        c = tuple(r.counts[x0][lk] for lk in r.links)
        c1 = tuple(r.counts[x1][lk] for lk in r.links)
        homog = all(r.counts[x] == r.counts[x0] for x in S)
        q = r.q[x0]
        qs = ("[" + ",".join(str(q[i][j]) for i in range(d) for j in range(d)) + "]"
              ) if q else "singular"
        Is = ("[" + ",".join(str(r.I[x0][i][j]) for i in range(d) for j in range(d)) + "]"
              ) if r.I[x0] else "none"
        say(f"  {nm:12s}{str(c):16s}{str(c1):16s}{qs:20s}{Is:28s}"
            f"{str(homog):7s}{r.admissible}")
    adm = {nm: recs[nm].admissible for nm in sorted(recs)}
    bad = ("G-SINGULAR", "G-INDEF")
    g02 = gate("G02", "THE RECORD READOUT'S ADMISSIBILITY GATE REJECTS BOTH DECLARED "
               "DEGENERATE RECORDS -- the SINGULAR one (det q = 0) and the INDEFINITE "
               "one (det q < 0) -- and accepts every other one (negative control with "
               "teeth, in both failure modes)",
               all(not adm[k] for k in bad)
               and all(v for k, v in adm.items() if k not in bad),
               {"admissible": adm, "declared_negative_controls": list(bad)})
    say(f"  G02 readout control: {'PASS' if g02 else 'FAIL'}   rejected: "
        f"{[k for k in bad if not adm[k]]}")
    ADM = [nm for nm in sorted(recs) if recs[nm].admissible]
    say("")

    # ======================= 4. LAPSE FAMILY AND RANK =====================
    say("--- 4. THE LAPSE FAMILY AND THE IDENTIFIABILITY RANK (GW1 5, item 7) ---")
    progress("lapse family and rank")
    lapses = build_lapse_family(S, d)
    pairs = [(a, b) for a in range(len(lapses)) for b in range(len(lapses)) if a != b]
    say(f"  |lapse family| = {len(lapses)}   ordered pairs tested = {len(pairs)}")
    rec0 = recs["G-FLAT"]
    om_cache = {(a, b): omega(lapses[a][1], lapses[b][1], rec0) for (a, b) in pairs}
    rank_at = {x: rank_exact([[om_cache[(a, b)][x][i] for i in range(d)]
                              for (a, b) in pairs]) for x in S}
    g03 = gate("G03", "THE TESTED LAPSE PAIRS REALISE A FULL-RANK BRACKET-COVECTOR "
               "FAMILY AT EVERY SITE, so the closure relation IDENTIFIES the structure "
               "function uniquely (GW1 5 item 7 -- 'no committed run tests rank')",
               all(v == d for v in rank_at.values()),
               {"rank_per_site": {str(k): v for k, v in sorted(rank_at.items())}})
    say(f"  realised covector rank per site: {sorted(set(rank_at.values()))}  (d = {d})")
    say(f"  G03 identifiability: {'PASS' if g03 else 'FAIL'}")
    say("")

    # ======================= 5. INVERTIBILITY =============================
    say("--- 5. H_a[N] : V_a^tot -> V_a^tot, CONSTRUCTED AND MEASURED INVERTIBLE ---")
    progress("invertibility")
    n_base = {x: (2 * x[0] + 5 * x[1]) % 7 for x in S}
    m_zero = {x: tuple(Fr(0) for _ in range(d)) for x in S}
    m_one = {x: tuple(Fr(1) for _ in range(d)) for x in S}
    registers = [("m == 0", m_zero), ("m == 1", m_one)]
    inv_fail = inv_tested = 0
    per_reg = {}
    for rlabel, mreg in registers:
        f0 = t0 = 0
        for rule, _a, _dsc in RULES:
            for nm in ADM:
                for (lname, N) in lapses[:4]:
                    H = Hmap(rule, recs[nm], N)
                    inv_tested += 1
                    t0 += 1
                    if not check_bijection_pair(H, (dict(n_base), dict(mreg))):
                        inv_fail += 1
                        f0 += 1
        per_reg[rlabel] = {"tested": t0, "failures": f0}
    coll = RegisterCollapse(recs["G-FLAT"])
    fals = {rlabel: (not check_bijection_pair(coll, (dict(n_base), dict(mreg))))
            for rlabel, mreg in registers}
    g04 = gate("G04", "EVERY MEMBER OF THE CONSTRUCTED H FAMILY IS AN EXACT BIJECTION "
               "OF TOTAL RECORDS, MEASURED BY H^-1 H = H H^-1 = id AT BOTH DECLARED "
               "ADDRESS REGISTERS; and the declared non-injective falsifier (register "
               "collapse) is REJECTED by the same predicate at the register that "
               "distinguishes it -- both sides of the control are run at both "
               "coordinates (RUNBOOK 15 addendum, like-for-like)",
               inv_fail == 0 and fals["m == 1"],
               {"tested": inv_tested, "failures": inv_fail,
                "per_register": per_reg, "falsifier_rejected_at": fals})
    say(f"  H^-1 H = id measured on {inv_tested} (rule, record, lapse, register) "
        f"instances over both declared registers; failures {inv_fail}")
    say(f"  declared non-injective falsifier rejected: {fals}   "
        f"(G04 {'PASS' if g04 else 'FAIL'})")
    say("  Both sides are run at both registers.  At m == 0 the falsifier is NOT")
    say("  rejected and cannot be: collapsing an already-zero register is the identity")
    say("  there, so no predicate could separate them.  The teeth are at m == 1, and")
    say("  the H family is measured invertible at both.")
    say("")

    # ======================= 6. THE RESIDUAL ==============================
    say("--- 6. THE GW1 RESIDUAL  R_HH,a[N,M] = H[N]H[M]H[N]^-1 H[M]^-1 D[-beta] ---")
    say("       RUN at the committed finite scope, by two independent routes:")
    say("       (a) the LITERAL composition of the five comparison maps;")
    say("       (b) the CLOSED form, built from the drag rule and the record")
    say("           readout without ever touching (a).")
    progress("residual sweep: closed form, literal composition, antisymmetry")
    results, per_site = {}, {}
    lit_fail = lit_cmp = 0
    ins_lit_nonzero = 0
    fields_computed = 0
    ord_bad = ord_tested = 0
    sigma_fields: dict = {}
    for rule, _a, _dsc in RULES:
        for nm in ADM:
            r = recs[nm]
            nz, worst, wit = 0, Fr(0), None
            zero_sites = {x: True for x in S}
            blk = {}
            for (a, b) in pairs:
                fc = residual_field_closed(rule, r, lapses[a][1], lapses[b][1])
                blk[(a, b)] = fc
                fields_computed += 1
                if not closes(fc):
                    nz += 1
                    if field_max(fc) > worst:
                        worst, wit = field_max(fc), (lapses[a][0], lapses[b][0])
                for x in S:
                    if not site_closes(fc, x):
                        zero_sites[x] = False
            results[(rule, nm)] = {"nonzero_pairs": nz, "total_pairs": len(pairs),
                                   "closes": nz == 0, "max_abs": str(worst),
                                   "witness": wit}
            per_site[(rule, nm)] = sum(1 for x in S if zero_sites[x])
            # the LITERAL five-map composition, at every cell of this row
            for (a, b) in pairs:
                fl = residual_field_literal(rule, r, lapses[a][1], lapses[b][1], n_base)
                lit_cmp += 1
                if fl is None or any(fl[x] != blk[(a, b)][x] for x in S):
                    lit_fail += 1
                if rule == DECL["positive_control_rule"] \
                        and (fl is None or any(any(t != 0 for t in fl[x]) for x in S)):
                    ins_lit_nonzero += 1
            # the update-order control, at every cell of this row
            for (a, b) in pairs:
                ord_tested += 1
                if any(blk[(a, b)][x][i] != -blk[(b, a)][x][i]
                       for x in S for i in range(d)):
                    ord_bad += 1
            if (rule, nm) == ("A-axis", "G-OFFDIAG"):
                sigma_fields = blk
        progress(f"  residual: {rule}")
    g05 = gate("G05", "THE LITERAL FIVE-MAP COMPOSITION AND THE INDEPENDENTLY BUILT "
               "CLOSED FORM AGREE FIELD BY FIELD, AT EVERY CELL OF THE HEADLINE TABLE "
               "(the comparator is not a copy of the audited object routed through it "
               "-- RUNBOOK 14 addendum, v13 #219)",
               lit_fail == 0 and lit_cmp == len(RULES) * len(ADM) * len(pairs),
               {"compared": lit_cmp, "disagreements": lit_fail,
                "scope": "every (rule, record, ordered lapse pair) cell",
                "shared_ingredient": "both routes call the same beta(), so a "
                                     "common-mode beta error is invisible here and is "
                                     "policed by G06/G08/G12/G21 instead"})
    say(f"  literal-vs-closed comparisons {lit_cmp} (every cell of the table), "
        f"disagreements {lit_fail}   (G05 {'PASS' if g05 else 'FAIL'})")
    say("")
    say(f"  CLOSURE TABLE.  Cells give the number of the {len(pairs)} ordered lapse")
    say("  pairs at which R_HH is NOT the identity ('CLOSES' = none of them).")
    say(f"  {'rule':14s}" + "".join(f"{nm:11s}" for nm in ADM))
    for rule, _a, _dsc in RULES:
        say(f"  {rule:14s}" + "".join(
            f"{('CLOSES' if results[(rule, nm)]['closes'] else str(results[(rule, nm)]['nonzero_pairs'])):11s}"
            for nm in ADM))
    say("")
    g06 = gate("G06", "POSITIVE CONTROL: the metric-INSERTED rule (Lambda = I_a(g)) "
               "closes exactly, at every admissible record and every tested lapse pair "
               "-- BY BOTH ROUTES.  The closed-form clause is analytically forced by "
               "the same identity X02 discloses for G08; the LITERAL five-map clause "
               "is not, and is the measurement",
               all(results[(DECL["positive_control_rule"], nm)]["closes"] for nm in ADM)
               and ins_lit_nonzero == 0,
               {nm: results[(DECL["positive_control_rule"], nm)]["closes"] for nm in ADM}
               | {"literal_route_nonzero_cells": ins_lit_nonzero})
    bl = broken_rules_tested()
    brk = {rn: sum(1 for nm in ADM if not results[(rn, nm)]["closes"]) for rn in bl}
    g07 = gate("G07", "NEGATIVE CONTROL WITH TEETH: every declared BROKEN H variant "
               "fails closure on at least one admissible record -- including the "
               "variant whose ONLY defect is that its second normal step is not "
               "transported along the first",
               len(brk) == len(DECL["broken_rules"]) and all(v > 0 for v in brk.values()),
               {"declared": DECL["broken_rules"], "tested": bl, "failing_records": brk})
    say(f"  G06 positive control (A-insert closes everywhere) : "
        f"{'PASS' if g06 else 'FAIL'}")
    say(f"  G07 broken-H negative control : {'PASS' if g07 else 'FAIL'}   {brk}")
    say("")

    # ------- the sector law -------
    say("  THE SECTOR LAW, measured cell by cell.  For each architecture-A rule and")
    say("  each record: the number of sites where the drag weight Lambda coincides")
    say("  with the record-read I_a(g), and the number where the residual vanishes")
    say(f"  for every one of the {len(pairs)} tested lapse pairs (out of {len(S)} sites).")
    sector, mism = {}, []
    for rule, _a, _dsc in RULES:
        if arch_of(rule) != "A":
            continue
        for nm in ADM:
            r = recs[nm]
            same = sum(1 for x in S
                       if all(lambda_of(rule, r, x)[i][j] == r.I[x][i][j]
                              for i in range(d) for j in range(d)))
            sector[(rule, nm)] = {"Lambda_equals_I_sites": same,
                                  "residual_zero_sites": per_site[(rule, nm)],
                                  "sites": len(S)}
            if rule in DECL["transported_rules"] and same != per_site[(rule, nm)]:
                mism.append(f"{rule}|{nm}")
    adjudicated = sum(1 for (rule, nm) in sector if rule in DECL["transported_rules"])
    g08 = gate("G08", "SITE BY SITE, THE RESIDUAL VANISHES EXACTLY WHERE THE DRAG "
               "RULE'S WEIGHT COINCIDES WITH THE RECORD-READ INVERSE METRIC, over the "
               "whole rule x record x site grid.  What closure forces is that the "
               "weight be the record's count-matrix inverse -- a JOINT, not "
               "link-local, function of the record (G09); nothing external is "
               "inserted, since by X05 the record and the metric candidate are one "
               "datum in two coordinate systems",
               len(mism) == 0, {"cells_in_grid": len(sector),
                                "cells_adjudicated": adjudicated,
                                "excluded_rule": DECL["frozen_front_rule"],
                                "mismatches": mism})
    say(f"  {'rule':14s}" + "".join(f"{nm:11s}" for nm in ADM))
    for rule, _a, _dsc in RULES:
        if arch_of(rule) != "A":
            continue
        say(f"  {rule:14s}" + "".join(
            f"{str(sector[(rule, nm)]['Lambda_equals_I_sites']) + '/' + str(sector[(rule, nm)]['residual_zero_sites']):11s}"
            for nm in ADM))
    say(f"  G08 sector law: {'PASS' if g08 else 'FAIL'}   mismatching cells {mism}")
    fr = DECL["frozen_front_rule"]
    fr_same = all(sector[(fr, nm)]["Lambda_equals_I_sites"] == len(S) for nm in ADM)
    fr_zero = all(sector[(fr, nm)]["residual_zero_sites"] == 0 for nm in ADM)
    g08b = gate("G08B", "TRANSPORT OF THE SECOND NORMAL STEP IS MEASURED NECESSARY: the "
                "declared frozen-front variant carries Lambda = I_a(g) at EVERY site -- "
                "it is fully metric-inserted -- and its residual vanishes at NO site and "
                "no record.  Insertion alone does not buy closure; the transported "
                "second step (GW1 1.1 condition 3) is independently required",
                fr_same and fr_zero,
                {"rule": fr, "Lambda = I at every site, every record": fr_same,
                 "residual vanishes nowhere": fr_zero,
                 "row": {nm: sector[(fr, nm)] for nm in ADM}})
    say(f"  G08B transport necessity ({fr}: Lambda = I at 9/9 sites, residual zero at "
        f"0/9): {'PASS' if g08b else 'FAIL'}")
    disclose("X04", "G16 and G19 are ANALYTICALLY FORCED and are therefore recorded, "
             "not must-pass: the front advance n -> n+N is an additive translation, so "
             "the HH commutator acts trivially on a matter-free carrier (G16); and the "
             "address register is passive under the front, so H_a[N] and D_a[B] commute "
             "identically (G19).  Both are printed because they are the measured shape "
             "of this construction, and both are consequences of declared choices, not "
             "discoveries.")
    disclose("X03", "The instrument carries ONE run-mode boolean, DELIVERY_RUN, "
             "identical for every mutant, which decides only whether receipts are "
             "written and the mutant harness is spawned.  It carries no per-mutant "
             "identity, and that no gate depends on it is now MEASURED rather than "
             "asserted: the whole measurement lives in a function that registers every "
             "gate and reads no run-mode name, the run-mode branch lives in a function "
             "that registers none, and G23's scanner treats DELIVERY_RUN, "
             "SELFTEST_ONLY, WRITE_ARTIFACTS and sys.argv as mutant identity under "
             "another name, with one synthetic injection per channel that it must flag.")
    disclose("X02", "The equivalence measured by G08 is ANALYTICALLY FORCED once G03's "
             "rank is full: rho^i = (Lambda^{ij} - I^{ij}) omega_j vanishes on a "
             "spanning covector family iff Lambda = I.  The same identity forces the "
             "CLOSED-FORM clause of G06 and the A-insert clauses of G12 and G21; those "
             "clauses are disclosures, and the measurement in each case is the LITERAL "
             "five-map route, which the identity does not force (G05, and G06's literal "
             "clause).  The forcing is conditional on G03, which a declared mutant "
             "genuinely breaks, so the pair is not vacuous.  The measured content of "
             "the sector law is G03's rank, the cell census, and the residual "
             "magnitudes below.")
    say("")
    say("  THE CROSS-TERM WALL.  A-axis is the link-local record-native rule: its")
    say("  weight is diag(1/n_{e_j}), read from the axis interval counts alone.")
    for nm in ADM:
        r = recs[nm]
        x0 = (0,) * d
        Lam, I = lambda_of("A-axis", r, x0), r.I[x0]
        say(f"    {nm:12s} (Lambda - I)(0,0) = ["
            + ",".join(str(Lam[i][j] - I[i][j]) for i in range(d) for j in range(d))
            + f"]   q^12 = {r.q[x0][0][1]}   max|rho| = "
              f"{results[('A-axis', nm)]['max_abs']}")
    say("")

    # ======================= 7. LINK LOCALITY =============================
    say("--- 7. NO LINK-LOCAL RECORD-NATIVE WEIGHT CLOSES  (theorem, witness gated) ---")
    progress("link locality")
    say("  A weight is LINK-LOCAL when Lambda = sum_l f_l(n_l) e_l e_l^T, i.e. each")
    say("  declared link contributes a weight that is a function of ITS OWN interval")
    say("  count alone.  At d = 2 that reads, component by component,")
    say("     Lambda^11 = f_1(n_e1) + f_3(n_diag),  Lambda^22 = f_2(n_e2) + f_3(n_diag),")
    say("     Lambda^12 = f_3(n_diag).")
    say("  Closure at a site forces Lambda = I_a(g) there (G08, with G03's full rank),")
    say("  so f_3(n_diag) = I^12 for EVERY admissible record.  Two admissible records")
    say("  that share n_diag and demand different I^12 therefore refute the whole")
    say("  link-local family at once.")
    x0 = (0,) * d
    dlk = recs[ADM[0]].links[d]              # the declared diagonal link e_1 + e_2
    cross_witness = None
    for nm1 in ADM:
        for nm2 in ADM:
            if nm1 >= nm2 or cross_witness is not None:
                continue
            r1, r2 = recs[nm1], recs[nm2]
            if r1.counts[x0][dlk] == r2.counts[x0][dlk] \
                    and r1.I[x0][0][1] != r2.I[x0][0][1]:
                cross_witness = {
                    "records": [nm1, nm2], "link": str(dlk),
                    "shared_interval_count": r1.counts[x0][dlk],
                    "f_3_demanded": [str(r1.I[x0][0][1]), str(r2.I[x0][0][1])],
                    "count_vectors": [str(tuple(r1.counts[x0][t] for t in r1.links)),
                                      str(tuple(r2.counts[x0][t] for t in r2.links))]}
    axis_witness = None
    for nm1 in ADM:
        for nm2 in ADM:
            for j in range(d):
                if nm1 >= nm2 or axis_witness is not None:
                    continue
                r1, r2 = recs[nm1], recs[nm2]
                lk = r1.links[j]
                if r1.counts[x0][lk] == r2.counts[x0][lk] \
                        and r1.I[x0][j][j] != r2.I[x0][j][j]:
                    axis_witness = {
                        "records": [nm1, nm2], "direction": j, "link": str(lk),
                        "shared_interval_count": r1.counts[x0][lk],
                        "I^jj_demanded": [str(r1.I[x0][j][j]), str(r2.I[x0][j][j])],
                        "count_vectors":
                            [str(tuple(r1.counts[x0][t] for t in r1.links)),
                             str(tuple(r2.counts[x0][t] for t in r2.links))]}
    witness = {"link_local_family": cross_witness,
               "diagonal_restricted_subfamily": axis_witness}
    g09 = gate("G09", "NO LINK-LOCAL RECORD-NATIVE WEIGHT CLOSES (theorem, witness "
               "gated): closure forces Lambda = I_a(g), a link-local weight has "
               "Lambda^12 = f_3(n_diag) depending on the diagonal link's own count "
               "alone, and two admissible records SHARE that count while demanding "
               "different I^12.  The second witness refutes only the "
               "diagonal-restricted subfamily Lambda^jj = f(n_e_j), and is reported "
               "as the weaker statement it is",
               cross_witness is not None and axis_witness is not None,
               {"witness": witness})
    say(f"  in-family witness (refutes every link-local weight): "
        f"{json.dumps(cross_witness)}")
    say(f"  diagonal-restricted witness (refutes Lambda^jj = f(n_e_j) only): "
        f"{json.dumps(axis_witness)}")
    say(f"  G09 link-locality theorem: {'PASS' if g09 else 'FAIL'}")
    say("  Mechanism: I^{ij} = adj(q)^{ij} / det q, and det q is a JOINT function of")
    say("  every link count at the site.  A weight that reads only its own link's")
    say("  count cannot see it.  Closure therefore requires a rule that computes the")
    say("  record's count-matrix inverse -- which is the metric.")
    lat_max_a = DECL["count_lattice"]["axis_max"]
    lat_max_c = DECL["count_lattice"]["diag_max"]
    lat = []
    for a_ in range(1, lat_max_a + 1):
        for b_ in range(1, lat_max_a + 1):
            for c_ in range(1, lat_max_c + 1):
                q_ = [[Fr(a_), Fr(c_ - a_ - b_, 2)], [Fr(c_ - a_ - b_, 2), Fr(b_)]]
                if q_[0][0] > 0 and det_exact(q_) > 0:
                    lat.append((a_, b_, c_, q_, det_exact(q_)))
    lat_w11 = lat_w12 = 0
    for i_ in range(len(lat)):
        a1, b1, c1, q1, d1_ = lat[i_]
        for j_ in range(i_ + 1, len(lat)):
            a2, b2, c2, q2, d2_ = lat[j_]
            if c1 != c2:
                continue
            if -q1[0][1] / d1_ != -q2[0][1] / d2_:
                lat_w12 += 1
            if a1 == a2 and q1[1][1] / d1_ != q2[1][1] / d2_:
                lat_w11 += 1
    g09b = gate("G09B", "THE LINK-LOCALITY WITNESS IS NOT AN ISOLATED ACCIDENT OF THE "
                "DECLARED NINE: over the declared count lattice the number of "
                "admissible pairs that share the diagonal count and demand different "
                "I^12, and that share (n_e1, n_diag) and demand different I^11, is "
                "censused", True,
                {"lattice": DECL["count_lattice"], "admissible_points": len(lat),
                 "pairs_sharing_n_diag_with_different_I12": lat_w12,
                 "pairs_sharing_n_e1_and_n_diag_with_different_I11": lat_w11},
                must_pass=False)
    say(f"  declared count lattice: {len(lat)} admissible count vectors; pairs sharing")
    say(f"  n_diag but demanding different I^12: {lat_w12}; pairs sharing (n_e1, n_diag)")
    say(f"  but demanding different I^11: {lat_w11}   (G09B recorded)")
    say("")

    # ======================= 8. THE OPERATOR LAYER ========================
    say("--- 8. THE FINITE OPERATOR LAYER: R_HH AS AN ACTUAL OPERATOR ON V_a^tot ---")
    progress("operator layer")
    op_rows, op_built, op_mismatch, op_nonbij, op_undef = [], 0, 0, 0, 0
    pa, pb = 0, 1
    Na, Mb = lapses[pa][1], lapses[pb][1]
    seen_nonzero: dict[tuple[str, str], bool] = {}
    exact_nonzero: dict[tuple[str, str], bool] = {}
    modular_blind: list[str] = []
    oprimes = operator_primes()
    plan = [(oprimes[0], S)] + [(pp, S[:1]) for pp in oprimes[1:]]
    for p, site_list in plan:
        n0p = {x: n_base[x] % p for x in S}
        for rule, _a, _dsc in RULES:
            for nm in ADM:
                r = recs[nm]
                bb = beta(r, Na, Mb)
                mb = {x: tuple(-bb[x][i] for i in range(d)) for x in S}
                fc = residual_field_closed(rule, r, Na, Mb)
                if x0 in site_list:
                    exact_nonzero[(rule, nm)] = any(t != 0 for t in fc[x0])
                    seen_nonzero.setdefault((rule, nm), False)
                for xs in site_list:
                    RC = ReducedCarrier(r, p, n0p, [Na, Mb], xs)
                    fz = n0p if rule == "A-notransport" else None
                    PN, PM = RC.perm_H(rule, Na, fz), RC.perm_H(rule, Mb, fz)
                    PD = RC.perm_D(mb)
                    if PN is None or PM is None or PD is None:
                        op_undef += 1
                        continue
                    op_built += 1
                    for P in (PN, PM, PD):
                        if len(set(P)) != RC.size:
                            op_nonbij += 1
                    R = perm_compose(PN, perm_compose(PM, perm_compose(
                        perm_inv(PN), perm_compose(perm_inv(PM), PD))))
                    moved = perm_moved(R)
                    red = [to_Fp(v, p) for v in fc[xs]]
                    if (moved == 0) != all(t == 0 for t in red):
                        op_mismatch += 1
                    if xs == x0:
                        key = (rule, nm)
                        seen_nonzero[key] = seen_nonzero.get(key, False) or (moved > 0)
                    if p == oprimes[0] and xs == x0:
                        op_rows.append((rule, nm, p, RC.size, moved))
    for key, nzq in sorted(exact_nonzero.items()):
        if nzq and not seen_nonzero.get(key):
            modular_blind.append(f"{key[0]}|{key[1]}")
    g10 = gate("G10", "EVERY COMPARISON MAP IS AN EXACT PERMUTATION OF THE REDUCED "
               "TOTAL-CONFIGURATION CARRIER, AND THE OPERATOR PRODUCT R_HH IS THE "
               "IDENTITY OPERATOR EXACTLY WHERE THE RESIDUAL FIELD REDUCES TO ZERO AT "
               "THE DETECTOR SITE", op_mismatch == 0 and op_nonbij == 0,
               {"carriers_built": op_built, "reductions_undefined": op_undef,
                "operator_vs_field_mismatches": op_mismatch,
                "non_bijective_maps": op_nonbij, "primes": oprimes})
    g10b = gate("G10B", "NO CELL WITH A NONZERO EXACT-RATIONAL RESIDUAL IS INVISIBLE "
                "AT EVERY TESTED PRIME -- counting a prime at which the reduction is "
                "UNDEFINED as not seeing it: the finite operator layer's verdict is not "
                "a modular artefact (the declared primes are each other's control)",
                modular_blind == [],
                {"cells": len(exact_nonzero), "primes": oprimes,
                 "blind_at_every_prime": modular_blind})
    say(f"  reduced carriers built {op_built} over primes {oprimes}; reductions "
        f"undefined {op_undef}; non-bijective maps {op_nonbij}; "
        f"operator-vs-field mismatches {op_mismatch}")
    say(f"  G10 operator layer: {'PASS' if g10 else 'FAIL'};  "
        f"G10B multi-prime: {'PASS' if g10b else 'FAIL'} "
        f"(blind at every prime: {modular_blind})")
    say(f"  ||R_HH|| on the carrier at p={oprimes[0]}, x*=(0,0), (N,M) = "
        f"({lapses[pa][0]},{lapses[pb][0]}):")
    say(f"    {'rule':14s}{'record':12s}{'carrier':9s}{'moved':8s}moved/carrier")
    for (rule, nm, p, size, moved) in op_rows:
        say(f"    {rule:14s}{nm:12s}{size:<9d}{moved:<8d}{Fr(moved, size)}")
    say("")
    progress("second comparator")
    fac_fail = fac_tested = 0
    for rule in ("A-axis", "A-insert", "A-chart"):
        for nm in ADM:
            r = recs[nm]
            p = 5
            n0p = {x: n_base[x] % p for x in S}
            bb = beta(r, Na, Mb)
            mb = {x: tuple(-bb[x][i] for i in range(d)) for x in S}
            fc = residual_field_closed(rule, r, Na, Mb)
            for xs in S[:3]:
                RC = ReducedCarrier(r, p, n0p, [Na, Mb], xs)
                PN, PM = RC.perm_H(rule, Na, None), RC.perm_H(rule, Mb, None)
                PD = RC.perm_D(mb)
                if PN is None or PM is None or PD is None:
                    continue
                R = perm_compose(PN, perm_compose(PM, perm_compose(
                    perm_inv(PN), perm_compose(perm_inv(PM), PD))))
                k = RC.code(0, tuple(0 for _ in range(d)))
                _, ri = RC.decode(R[k])
                fac_tested += 1
                if list(RC.regs[ri]) != [to_Fp(v, p) for v in fc[xs]]:
                    fac_fail += 1
    g11 = gate("G11", "THE OPERATOR'S OWN REGISTER DISPLACEMENT, READ OFF THE "
               "PERMUTATION ITSELF, EQUALS THE EXACT-RATIONAL RESIDUAL FIELD REDUCED "
               "MOD p AT THE DETECTOR SITE (a second comparator, differently routed)",
               fac_fail == 0 and fac_tested > 0,
               {"tested": fac_tested, "failures": fac_fail})
    say(f"  operator-displacement vs field mod p: {fac_tested} tested, {fac_fail} "
        f"failures   (G11 {'PASS' if g11 else 'FAIL'})")
    say("")

    # ======================= 9. THE GW1 PIN'S CONTROL LIST =================
    say("--- 9. THE GW1 PIN'S OWN CONTROL LIST, RUN ---")
    progress("controls")
    fl_c = results[("A-axis", "G-FLAT")]["closes"]
    cu_c = results[("A-axis", "G-CURVED")]["closes"]
    of_c = results[("A-axis", "G-OFFDIAG")]["closes"]
    co_c = results[("A-axis", "G-CURVOFF")]["closes"]
    g12 = gate("G12", "FLAT AND CURVED TARGETS SEPARATE: the link-local record-native "
               "rule closes on the flat record AND on the inhomogeneous diagonal "
               "('curved') record, and fails on both cross-term records",
               fl_c and cu_c and (not of_c) and (not co_c),
               {"G-FLAT": fl_c, "G-CURVED": cu_c, "G-OFFDIAG": of_c, "G-CURVOFF": co_c})
    say(f"  flat/curved: G-FLAT {fl_c}, G-CURVED {cu_c}, G-OFFDIAG {of_c}, "
        f"G-CURVOFF {co_c}   (G12 {'PASS' if g12 else 'FAIL'})")

    g13 = gate("G13", "UPDATE-ORDER CONTROL: exchanging the two normal labels sends the "
               "residual field to its exact negative at every site, so the measured "
               "two-cell is genuinely antisymmetric and not an artefact of one order "
               "-- over EVERY rule, record and ordered lapse pair",
               ord_bad == 0 and ord_tested == len(RULES) * len(ADM) * len(pairs),
               {"tested": ord_tested, "violations": ord_bad,
                "scope": "every (rule, record, ordered lapse pair) cell"})
    say(f"  update-order control: {ord_tested} cells (every rule, record and ordered "
        f"pair), antisymmetry violations {ord_bad}   (G13 {'PASS' if g13 else 'FAIL'})")

    progress("chart self-test, the FULL declared chart group")
    cb = dict(_CACHE_STATS)
    chart_bad = chart_tested = 0
    fresh_tested = fresh_bad = 0
    sigmas = list(itertools.permutations(range(d)))
    shifts = S
    base_field = {}
    for sigma in sigmas:
        for sh in shifts:
            for nm in ADM:
                r = recs[nm]

                def phi(x, sigma=sigma, sh=sh):
                    y = chart_index(x, sigma, d)
                    return tuple((y[i] + sh[i]) % L for i in range(d))

                def phil(lk, sigma=sigma):
                    return chart_index(lk, sigma, d)
                inv_phi = {phi(x): x for x in S}
                inv_phil = {phil(lk): lk for lk in r.links}

                def rule_fn(y, m, r=r, inv_phi=inv_phi, inv_phil=inv_phil):
                    return r.counts[inv_phi[y]][inv_phil[m]]
                r2 = GeomRecord(f"{r.name}@chart{sigma}{sh}", d, L,
                               rule_fn, W)
                for (a, b) in pairs:
                    Nn, Mm = lapses[a][1], lapses[b][1]
                    N2 = {phi(x): Nn[x] for x in S}
                    M2 = {phi(x): Mm[x] for x in S}
                    if (nm, a, b) not in base_field:
                        base_field[(nm, a, b)] = residual_field_closed("A-axis", r,
                                                                      Nn, Mm)
                    f1 = base_field[(nm, a, b)]
                    f2 = residual_field_closed("A-axis", r2, N2, M2)
                    for x in S:
                        lhs = tuple(f1[x][sigma[i]] for i in range(d))
                        chart_tested += 1
                        if lhs != f2[phi(x)]:
                            chart_bad += 1
                # the memo is load-bearing above: every comparand is served through
                # it.  Here the SAME weights are recomputed with the memo BYPASSED
                # and compared against what the memo returns, on both the base and
                # the chart-transformed record, so an aliased memo cannot survive.
                for rr in (r, r2):
                    for x in S:
                        fresh_tested += 1
                        if lambda_of("A-axis", rr, x, fresh=True) \
                                != lambda_of("A-axis", rr, x):
                            fresh_bad += 1
        progress(f"  chart relabelling {sigma} done")
    ca = dict(_CACHE_STATS)
    g14 = gate("G14", "CHART SELF-TEST (RUNBOOK 14): the residual field is EQUIVARIANT "
               "under EVERY element of the declared chart group -- all |X| translations "
               "times all d! direction relabellings -- at every admissible record, every "
               "ordered lapse pair and every site, measured component by component on "
               "freshly rebuilt records",
               chart_bad == 0
               and chart_tested == len(sigmas) * len(shifts) * len(ADM) * len(pairs) * len(S),
               {"site_comparisons": chart_tested,
                "component_comparisons": chart_tested * d,
                "violations": chart_bad,
                "group_elements": len(sigmas) * len(shifts),
                "relabellings": len(sigmas), "translations": len(shifts)})
    g15 = gate("G15", "THE WEIGHT MEMO IS EXERCISED AND ITS RETURNS ARE MEASURED "
               "CORRECT: the self-test's own comparands are served through the memo, "
               "and every one of those weights is recomputed with the memo BYPASSED "
               "and compared against it, on the base record and on the "
               "chart-transformed record alike (RUNBOOK 14 addenda, v13 #185 / #219: "
               "a zero-hit cache gate is vacuous, and a cache that is never checked "
               "against a fresh evaluation is a cache, not a measurement)",
               ca["bypass"] > cb["bypass"] and ca["hits"] > 0 and ca["misses"] > 0
               and fresh_bad == 0 and fresh_tested > 0,
               {"hits": ca["hits"], "misses": ca["misses"],
                "fresh_bypasses": ca["bypass"],
                "fresh_vs_memo_compared": fresh_tested,
                "fresh_vs_memo_disagreements": fresh_bad})
    say(f"  chart self-test over the full declared group: {chart_tested} site "
        f"comparisons ({chart_tested * d} components), violations {chart_bad}   "
        f"(G14 {'PASS' if g14 else 'FAIL'})")
    say(f"  cache hits {ca['hits']}, misses {ca['misses']}, fresh bypasses "
        f"{ca['bypass']}; fresh-vs-memo compared {fresh_tested}, disagreements "
        f"{fresh_bad}   (G15 {'PASS' if g15 else 'FAIL'})")

    mf_trivial = True
    for rule, _a, _dsc in RULES:
        for nm in ADM:
            HN, HM = Hmap(rule, recs[nm], Na), Hmap(rule, recs[nm], Mb)
            c = (dict(n_base), {})
            for f in [HM.inv, HN.inv, HM.fwd, HN.fwd]:
                c = f(c)
            if c[0] != n_base:
                mf_trivial = False
    g16 = gate("G16", "MATTER CONTROL: on the matter-free carrier the HH commutator is "
               "the identity for every rule and record, so the deformation-closure test "
               "has NO content without matter records -- measured, not asserted",
               mf_trivial, {"matter_free_commutator_trivial": mf_trivial},
               must_pass=False)
    say(f"  matter-free vs matter-conditioned: the matter-free commutator is trivial "
        f"for every cell: {mf_trivial}   (G16 {'PASS' if g16 else 'FAIL'})")

    progress("convention flip-tests")
    recsW = {nm: make_record(nm, d, L, tup, DECL["density_weight_flip"])
             for nm, tup in DECL["records_d2"].items()}
    recsW["G-CURVED"] = make_curved_record("G-CURVED", d, L, DECL["density_weight_flip"])
    recsW["G-CURVOFF"] = make_curved_off_record("G-CURVOFF", d, L,
                                                DECL["density_weight_flip"])
    flip_rows = {}
    for nm in ADM:
        rW = recsW[nm]
        nz = sum(1 for (a, b) in pairs
                 if not closes(residual_field_closed("A-axis", rW, lapses[a][1],
                                                     lapses[b][1])))
        flip_rows[nm] = {"w=0": results[("A-axis", nm)]["nonzero_pairs"], "w=1": nz}
    moved_cells = [nm for nm, v in flip_rows.items() if (v["w=0"] == 0) != (v["w=1"] == 0)]
    g17 = gate("G17", "DENSITY-WEIGHT FLIP-TEST (GW1 5, item 5): the closure verdict is "
               "measured under BOTH declared normalisation conventions and every cell "
               "whose verdict moves is named", True,
               {"per_record": flip_rows, "verdict_moves_at": moved_cells},
               must_pass=False)
    say("  density-weight flip-test (I = q^-1 against I = q^-1 det q):")
    for nm in sorted(flip_rows):
        say(f"    {nm:12s} w=0 nonzero pairs {flip_rows[nm]['w=0']:5d}    "
            f"w=1 nonzero pairs {flip_rows[nm]['w=1']:5d}")
    say(f"  verdict moves at: {moved_cells}")

    tot_ok = tot_undef = tot_nonzero = tot_nonzero_ok = 0
    for nm in ADM:
        r = recs[nm]
        for (a, b) in pairs:
            bb = beta(r, lapses[a][1], lapses[b][1])
            nonzero = any(t != 0 for v in bb.values() for t in v)
            tot_nonzero += 1 if nonzero else 0
            Dt = Dmap(r, {x: tuple(-bb[x][i] for i in range(d)) for x in S}, "D-TOT")
            sm = Dt.site_map()
            if sm is None:
                tot_undef += 1
            else:
                tot_ok += 1
                if nonzero:
                    tot_nonzero_ok += 1
    g18 = gate("G18", "TANGENTIAL-REALISATION FLIP-TEST (the bookkeeping split): under "
               "D-TOT, D_a[v] must drag the geometry front along the site map "
               "x -> x+v(x).  MEASURED: of the brackets this arena realises, the number "
               "with beta nonzero that nevertheless admit a bijective site map",
               True,
               {"pairs": len(pairs) * len(ADM), "beta nonzero": tot_nonzero,
                "site map defined": tot_ok, "site map undefined": tot_undef,
                "beta nonzero AND site map defined": tot_nonzero_ok}, must_pass=False)
    say(f"  D-TOT flip-test over {len(pairs) * len(ADM)} (record, lapse pair) cells: "
        f"beta nonzero {tot_nonzero}, site map defined {tot_ok}, undefined "
        f"{tot_undef}; nonzero-beta cells admitting a site map: {tot_nonzero_ok}")
    say("")

    # ======================= 10. THE DETECTOR =============================
    say("--- 10. THE THREE-NORMAL SWITCH DETECTOR W_{N|ML,a} (v4 p12 Def 11.6M) ---")
    progress("detector")
    det_rows, comm_triv, comm_tested = [], 0, 0
    det_nonzero = 0
    hhh_cmp = hhh_bad = 0
    for rule in ("A-insert", "A-axis", "A-chart"):
        for nm in ADM:
            r = recs[nm]
            for (a, b, c_) in [(0, 1, 2), (0, 3, 9), (9, 10, 0), (1, 4, 10)]:
                Nl, Ml, Ll = lapses[a][1], lapses[b][1], lapses[c_][1]
                B_ML = beta(r, Ml, Ll)
                cf, cr = switch_commutator(rule, r, Nl, B_ML, n_base)
                comm_tested += 1
                triv = all(cf[x] == 0 for x in S) and all(all(t == 0 for t in cr[x])
                                                          for x in S)
                comm_triv += 1 if triv else 0
                df, dr, jac = sw_hhh(rule, r, Nl, Ml, Ll, n_base)
                front0 = all(df[x] == 0 for x in S)
                reg0 = all(all(t == 0 for t in dr[x]) for x in S)
                jac0 = all(jac[x] == 0 for x in S)
                if not (front0 and reg0):
                    det_nonzero += 1
                # the closed form of the displacement, built from the three
                # TRANSPORTED LAPSE DERIVATIVES and the drag weight alone:
                #   Delta m^i = Lambda^{ij} ( B d_j C + A d_j B + A d_j C ),
                #   A = L_{B_ML}N,  B = L_{B_LN}M,  C = L_{B_NM}L,
                # valid because C(H,D) degenerates here and A + B + C = 0.
                A3 = lie_lapse(r, B_ML, Nl)
                B3 = lie_lapse(r, beta(r, Ll, Nl), Ml)
                C3 = lie_lapse(r, beta(r, Nl, Ml), Ll)
                pred = {}
                for x in S:
                    Lam = lambda_of(rule, r, x)
                    dC = [Fr(C3[add(x, e, L)] - C3[x]) for e in r.links[:d]]
                    dB = [Fr(B3[add(x, e, L)] - B3[x]) for e in r.links[:d]]
                    pred[x] = tuple(
                        sum((Lam[i][j] * (Fr(B3[x]) * dC[j] + Fr(A3[x]) * dB[j]
                                          + Fr(A3[x]) * dC[j]) for j in range(d)), Fr(0))
                        for i in range(d))
                hhh_cmp += 1
                if any(pred[x] != dr[x] for x in S):
                    hhh_bad += 1
                det_rows.append((rule, nm, f"({a},{b},{c_})", triv, jac0,
                                 front0, reg0,
                                 str(max((abs(t) for v in dr.values() for t in v),
                                         default=Fr(0)))))
    g19 = gate("G19", "THE NORMAL-TANGENTIAL GROUP COMMUTATOR C(H_a[N], D_a[B]) IS "
               "MEASURED TRIVIAL ON THIS SUBSTRATE, so the corrected switch degenerates "
               "to W = H_a[L_B N]: the construction does NOT reproduce v4 paper 13 "
               "Proposition 3.6's nonzero detector, and that is a measurement",
               comm_triv == comm_tested, {"tested": comm_tested, "trivial": comm_triv},
               must_pass=False)
    jac_bad = [r_ for r_ in det_rows if not r_[4]]
    det_bad = [r_ for r_ in det_rows if not (r_[5] and r_[6])]
    g20 = gate("G20", "THE THREE-NORMAL DETECTOR IS EVALUATED BY LITERAL COMPOSITION OF "
               "THE THREE CORRECTED SWITCHES: the cyclic Jacobi lapse sum, the front "
               "displacement and the register displacement of SW_HHH are each measured "
               "at every tested triple, and the nonvanishing cells are named", True,
               {"triples": len(det_rows),
                "jacobi_lapse_sum_nonvanishing": len(jac_bad),
                "SW_HHH_not_the_identity": len(det_bad),
                "nonidentity_cells": [f"{r_[0]}|{r_[1]}|{r_[2]}|max_reg={r_[7]}"
                                      for r_ in det_bad]}, must_pass=False)
    say(f"  C(H[N],D[B]) trivial at {comm_triv}/{comm_tested} tested cells   "
        f"(G19 {'PASS' if g19 else 'FAIL'})")
    say(f"  {'rule':11s}{'record':12s}{'(N,M,L)':11s}{'C=I':7s}{'Jac=0':8s}"
        f"{'front=0':9s}{'reg=0':8s}max|reg|")
    for r_ in det_rows[:14]:
        say(f"  {r_[0]:11s}{r_[1]:12s}{r_[2]:11s}{str(r_[3]):7s}{str(r_[4]):8s}"
            f"{str(r_[5]):9s}{str(r_[6]):8s}{r_[7]}")
    say(f"  ... {len(det_rows)} triples in all.  The cyclic Jacobi LAPSE sum is "
        f"nonvanishing at {len(jac_bad)};")
    say(f"  SW_HHH is not the identity at {len(det_bad)} of them "
        f"(Det_HHH > 0 there).")
    g20b = gate("G20B", "THE THREE-NORMAL DISPLACEMENT HAS AN EXACT CLOSED FORM, AND "
                "IT IS MEASURED: with the normal-tangential commutator degenerate and "
                "the Jacobi lapse sum zero, the register displacement of SW_HHH is "
                "Lambda^{ij}( B d_j C + A d_j B + A d_j C ) in the three transported "
                "lapse derivatives A = L_{B_ML}N, B = L_{B_LN}M, C = L_{B_NM}L -- "
                "compared against the LITERAL composition of the three corrected "
                "switches at every tested triple",
                hhh_bad == 0 and hhh_cmp == len(det_rows),
                {"compared": hhh_cmp, "disagreements": hhh_bad})
    say(f"  SW_HHH closed form vs literal composition: {hhh_cmp} triples, "
        f"disagreements {hhh_bad}   (G20B {'PASS' if g20b else 'FAIL'})")
    by_rule = {}
    for r_ in det_rows:
        k = r_[0]
        by_rule.setdefault(k, [0, 0])
        by_rule[k][1] += 1
        if not (r_[5] and r_[6]):
            by_rule[k][0] += 1
    for k in sorted(by_rule):
        say(f"    {k:12s} Det_HHH > 0 at {by_rule[k][0]:3d} of {by_rule[k][1]:3d} "
            f"tested triples")
    say("  READ THIS AGAINST SECTION 6: the metric-inserted rule closes the HH PAIR")
    say("  residual exactly at every record, and its three-normal object is")
    say("  nevertheless nonzero.  The comparison is between a CORRECTED pair object")
    say("  and an UNCORRECTED triple: v4 paper 7 defines no triple-level correction,")
    say("  so a nonzero SW_HHH is what the definitions predict, and the content is")
    say("  the exact closed form above -- the finite measurement of v4 paper 12's own")
    say("  reason for building the corrected switch.")
    say("")

    # ======================= 11. GENERAL d ================================
    say("--- 11. THE GENERAL-d EXTENSION (v4 p7 is general-d; d = 3 run) ---")
    progress("general d")
    d3, L3 = DECL["d_ext"], DECL["L_ext"]
    S3 = sites(d3, L3)
    recs3 = {nm: make_record(nm, d3, L3, tup, W) for nm, tup in DECL["records_d3"].items()}
    lp3 = [(f"delta{x}", {y: (1 if y == x else 0) for y in S3}) for x in S3[:6]]
    lp3.append(("one", {y: 1 for y in S3}))
    pairs3 = [(a, b) for a in range(len(lp3)) for b in range(len(lp3)) if a != b]
    say(f"  |X| = {len(S3)} sites, {len(recs3)} records, {len(pairs3)} lapse pairs")
    res3 = {}
    rules3 = [r for r in DECL["rules_d3"] if r in {t[0] for t in RULES}]
    say(f"  {'rule':14s}" + "".join(f"{nm:12s}" for nm in sorted(recs3)))
    for rule in rules3:
        row = f"  {rule:14s}"
        for nm in sorted(recs3):
            r = recs3[nm]
            if not r.admissible:
                row += f"{'inadm':12s}"
                continue
            nz = sum(1 for (a, b) in pairs3
                     if not closes(residual_field_closed(rule, r, lp3[a][1], lp3[b][1])))
            res3[(rule, nm)] = nz
            row += f"{('CLOSES' if nz == 0 else str(nz)):12s}"
        say(row)
    g21 = gate("G21", "THE GENERAL-d EXTENSION REPRODUCES THE SAME SEPARATION AT d = 3: "
               "the metric-inserted rule closes on every admissible record; the "
               "link-local rule closes on the diagonal records and fails on the "
               "cross-term record",
               all(res3.get(("A-insert", nm), 1) == 0 for nm in sorted(recs3)
                   if recs3[nm].admissible)
               and res3.get(("A-axis", "G3-OFF"), 0) > 0
               and res3.get(("A-axis", "G3-ANISO"), 1) == 0
               and res3.get(("A-axis", "G3-FLAT"), 1) == 0,
               {f"{k[0]}|{k[1]}": v for k, v in sorted(res3.items())})
    say(f"  G21 general-d: {'PASS' if g21 else 'FAIL'}")
    say("")

    # ======================= 12. THE BRIDGE ===============================
    say("=" * 78)
    say("--- 12. THE DECLARED SECONDARY, AS A COORDINATE AUDIT: WHAT DOES R_HH")
    say("        SHARE WITH THE STITCHING GEOMETRY'S DATA, AND WHAT IS ARENA?")
    say("        (NT and GEN, receipts hash-pinned at A05/A06)")
    say("=" * 78)
    progress("bridge")
    say("  12.1  THE STRUCTURE OF R_HH ON THE REDUCED CARRIER, and its dependence on")
    say("        the declared reduction prime.  R_HH is formed as an explicit")
    say("        permutation product and the group it generates is the CYCLIC group")
    say("        generated by that one permutation -- not a loop product of link")
    say("        transports, and not a multi-generator group.")
    r = recs["G-OFFDIAG"]
    N_sym = {y: (1 if y == (0, 0) else 0) for y in S}             # swap-symmetric
    M_sym = {y: (1 if y in ((0, 1), (1, 0)) else 0) for y in S}   # swap-symmetric
    xs = (0, 0)
    rho_exact = residual_field_closed("A-axis", r, N_sym, M_sym)[xs]

    def ha_sigma(RC_):
        out = [0] * RC_.size
        for fi, f in enumerate(RC_.fronts):
            key = tuple(sorted({x: f[(x[1], x[0])] for x in S}.items()))
            fj = RC_.front_index.get(key)
            if fj is None:
                return None
            for reg in RC_.regs:
                out[RC_.code(fi, reg)] = RC_.code(fj, (reg[1], reg[0]))
        return out

    prime_rows = []
    trans_ok = trans_tested = 0
    RC = SIG = R_HA = None
    for pp in sweep_primes():
        n_symp = {x: (x[0] * x[1]) % pp for x in S}   # symmetric under the swap
        RCp = ReducedCarrier(r, pp, n_symp, [N_sym, M_sym], xs)
        PN, PM = RCp.perm_H("A-axis", N_sym, None), RCp.perm_H("A-axis", M_sym, None)
        bb = beta(r, N_sym, M_sym)
        PD = RCp.perm_D({x: tuple(-bb[x][i] for i in range(d)) for x in S})
        Rp = perm_compose(PN, perm_compose(PM, perm_compose(
            perm_inv(PN), perm_compose(perm_inv(PM), PD))))
        grp = sorted(group_closure([tuple(Rp)], tuple(range(RCp.size))))
        abelian = all(perm_mul(list(g1), list(g2)) == perm_mul(list(g2), list(g1))
                      for g1 in grp for g2 in grp)
        exps = sorted({perm_order(list(g)) for g in grp})
        rho_p = tuple(to_Fp(v, pp) for v in rho_exact)
        # is R_HH exactly the translation of the address register by rho mod p?
        trans_tested += 1
        if None not in rho_p and all(
                Rp[RCp.code(fi, reg)] == RCp.code(
                    fi, tuple((reg[i] + rho_p[i]) % pp for i in range(d)))
                for fi in range(len(RCp.fronts)) for reg in RCp.regs):
            trans_ok += 1
        SIGp = ha_sigma(RCp)
        dih_p = None if SIGp is None else \
            (perm_mul(SIGp, perm_mul(Rp, SIGp)) == perm_inv(Rp))
        prime_rows.append({"p": pp, "carrier": RCp.size, "group_order": len(grp),
                           "abelian": abelian, "element_orders": exps,
                           "rho_mod_p": list(rho_p), "sigma_relation": dih_p})
        if RC is None:
            RC, SIG, R_HA = RCp, SIGp, Rp
            ha_group, ha_order = grp, len(grp)
            ha_abelian, ha_exponents = abelian, exps
        progress(f"  bridge prime {pp}")
    p = prime_rows[0]["p"]
    say(f"        exact rational residual at the detector site: {rho_exact} -- the "
        f"SAME at every prime")
    say(f"        {'p':5s}{'carrier':10s}{'|<R>|':8s}{'abelian':9s}{'elt orders':14s}"
        f"{'rho mod p':12s}SigmaRSigma=R^-1")
    for row in prime_rows:
        say(f"        {row['p']:<5d}{row['carrier']:<10d}{row['group_order']:<8d}"
            f"{str(row['abelian']):9s}{str(row['element_orders']):14s}"
            f"{str(row['rho_mod_p']):12s}{row['sigma_relation']}")
    orders = [row["group_order"] for row in prime_rows]
    swept = [row["p"] for row in prime_rows]
    order_is_prime = (orders == swept)
    g29 = gate("G29", "R_HH ACTS ON THE REDUCED CARRIER AS THE TRANSLATION OF THE "
               "ADDRESS REGISTER BY rho mod p, MEASURED PERMUTATION BY PERMUTATION: "
               "the front sector returns to itself and every configuration is moved by "
               "the same register shift, so <R_HH> is cyclic of order p whenever rho is "
               "nonzero mod p -- the group is read off the arena, not off the physics",
               trans_ok == trans_tested and trans_tested > 0,
               {"primes": swept, "carriers_checked": trans_tested,
                "translation_structure_confirmed": trans_ok})
    g30 = gate("G30", "THE HOLONOMY ORDER IS AN ARENA COORDINATE, NOT A PROPERTY OF "
               "R_HH (RUNBOOK 15): swept over the declared primes the measured group "
               "order EQUALS the declared prime at every one, while the exact rational "
               "residual is prime-independent.  A quantity that moves with the arena "
               "may serve as an instrument reading and may not enter as a conclusion",
               order_is_prime and len(set(orders)) == len(orders) and len(orders) > 1,
               {"primes": swept, "measured_orders": orders,
                "order_equals_the_declared_prime": order_is_prime,
                "exact_residual": [str(t) for t in rho_exact],
                "residual_is_prime_independent": True})
    say(f"        G29 translation structure: {'PASS' if g29 else 'FAIL'}   "
        f"(<R> is cyclic of order p at every swept prime)")
    say(f"        G30 arena-determinism: {'PASS' if g30 else 'FAIL'}   "
        f"measured orders {orders} against declared primes {swept}")
    say("")

    say("  12.2  GEN's OWN RELATIONS, AND THE SPECTRUM THE COMPARISON MUST USE.")
    D_gen = gen_defect(Q_declared)
    gen_dih = perm_mul(S9, perm_mul(D_gen, S9)) == perm_inv(D_gen)
    gen_ord = perm_order(D_gen)
    # a permutation that is NOT of the sandwich form Sigma Q^-1 Sigma Q
    P_ctrl = list(range(9))
    P_ctrl[0], P_ctrl[1], P_ctrl[2] = P_ctrl[1], P_ctrl[2], P_ctrl[0]
    ctrl_dih = perm_mul(S9, perm_mul(P_ctrl, S9)) == perm_inv(P_ctrl)
    say(f"        GEN's declared defect: order {gen_ord}, Sigma D Sigma = D^-1 : "
        f"{gen_dih}")
    say("        DISCLOSURE X06: that relation is ANALYTICALLY FORCED for every")
    say("        completion -- with D = Sigma Q^-1 Sigma Q and Sigma^2 = id,")
    say("        Sigma D Sigma = (Sigma Q^-1 Sigma Q)^-1 = D^-1 identically, which is")
    say("        why A16 counts 0 failures over all 40320 members.  It is a disclosure,")
    say("        not a discriminating control.  The relation is not vacuous for")
    say("        arbitrary permutations -- a declared 3-cycle outside the sandwich form")
    say(f"        satisfies it: {ctrl_dih} -- it is forced for every COMPLETION.")
    disclose("X06", "GEN's dihedral relation Sigma D Sigma = D^-1 is analytically "
             "forced for every completion Q by Sigma^2 = id and D = Sigma Q^-1 Sigma Q, "
             "so A16's 0 failures over 40320 members and the 'positive control' reading "
             "of the relation are disclosures, not discriminating measurements; a "
             "declared permutation outside the sandwich form is exhibited against it",
             {"declared_3_cycle_satisfies_the_relation": ctrl_dih})
    comp_spec = comparator_spectrum(sorted(defect_spectrum),
                                    holonomy_spectrum)
    say("        GEN publishes TWO spectra, and BOTH are computed here from the")
    say(f"        completion census: the DEFECT order spectrum {sorted(defect_spectrum)}")
    say(f"        (multiplicities {dict(defect_spectrum)}) and the derived HOLONOMY")
    say(f"        order spectrum {holonomy_spectrum}.  The coordinate table pairs R_HH")
    say("        with GEN's DEFECT D, so the defect spectrum is the like-for-like")
    say("        comparator; comparing HA against one and GEN against the other would")
    say("        be a class-vs-class verdict read at two coordinates (RUNBOOK 15).")
    memb = {row["p"]: (row["group_order"] in comp_spec) for row in prime_rows}
    mult = {row["p"]: defect_spectrum.get(row["group_order"], 0) for row in prime_rows}
    for row in prime_rows:
        pp = row["p"]
        say(f"          order {row['group_order']:<3d} at p = {pp:<3d} in the defect "
            f"spectrum: {str(memb[pp]):6s} (multiplicity {mult[pp]} of "
            f"{sum(defect_spectrum.values())})")
    g31 = gate("G31", "THE SPECTRUM COMPARISON IS ARENA-DEPENDENT TOO, AND IS RUN "
               "AGAINST THE COMPUTED DEFECT SPECTRUM RATHER THAN A TYPED TUPLE: the "
               "measured holonomy order lies in GEN's own defect order spectrum at some "
               "declared primes and outside it at others, so membership is a property "
               "of the reduction prime and not of R_HH",
               len(set(memb.values())) > 1,
               {"membership_by_prime": memb, "multiplicity_by_prime": mult,
                "comparator": "GEN's defect order spectrum, computed at A14",
                "defect_spectrum": dict(defect_spectrum),
                "holonomy_spectrum": holonomy_spectrum})
    say(f"        G31 spectrum comparison: {'PASS' if g31 else 'FAIL'}   "
        f"membership by prime {memb}")
    say("")

    say("  12.3  THE Sigma-RELATION CENSUS, decomposed.  Sigma is the declared chart")
    say("        involution; on the reduced carrier it exists only where the front")
    say("        sector is swap-closed, and the relation Sigma R Sigma = R^-1 is")
    say("        POSABLE only there.  Three readings are reported, not one.")
    n_sym = {x: (x[0] * x[1]) % p for x in S}
    ha_dih = None if SIG is None else (perm_mul(SIG, perm_mul(R_HA, SIG))
                                       == perm_inv(R_HA))
    rel_rows = {}
    for setname, PS in (("first-24", pairs[:24]), ("all", pairs)):
        sur = sur_vac = full = 0
        cdef = chold = cid = 0
        for (a, b) in PS:
            Nn, Mm = lapses[a][1], lapses[b][1]
            f = sigma_fields[(a, b)]
            if f[xs][0] + f[xs][1] == 0:
                sur += 1
                if all(t == 0 for t in f[xs]):
                    sur_vac += 1
            if all(f[x][0] + f[x][1] == 0 for x in S):
                full += 1
            RCq = ReducedCarrier(r, p, n_sym, [Nn, Mm], xs)
            PNq, PMq = RCq.perm_H("A-axis", Nn, None), RCq.perm_H("A-axis", Mm, None)
            bq = beta(r, Nn, Mm)
            PDq = RCq.perm_D({x: tuple(-bq[x][i] for i in range(d)) for x in S})
            if PNq is None or PMq is None or PDq is None:
                continue
            Rq = perm_compose(PNq, perm_compose(PMq, perm_compose(
                perm_inv(PNq), perm_compose(perm_inv(PMq), PDq))))
            SIGq = ha_sigma(RCq)
            if SIGq is None:
                continue
            cdef += 1
            if perm_mul(SIGq, perm_mul(Rq, SIGq)) == perm_inv(Rq):
                chold += 1
                if Rq == list(range(RCq.size)):
                    cid += 1
        rel_rows[setname] = {
            "pairs": len(PS), "surrogate_holds": sur,
            "surrogate_holds_vacuously": sur_vac,
            "full_field_relation_holds": full,
            "carrier_relation_posable": cdef, "carrier_relation_holds": chold,
            "carrier_relation_holds_at_the_identity": cid}
        say(f"        [{setname}] of {len(PS)} ordered pairs: the single-site surrogate "
            f"rho_1 + rho_2 = 0")
        say(f"          holds at {sur}, of which {sur_vac} are cells where R_HH is the "
            f"identity at the")
        say(f"          detector site; the SAME relation stated over the whole field "
            f"holds at {full};")
        say(f"          the carrier-level relation is POSABLE (Sigma exists) at "
            f"{cdef} and holds at")
        say(f"          {chold}, of which {cid} are cells where R_HH is the identity.")
    g32 = gate("G32", "THE Sigma-RELATION CENSUS IS REPORTED AT EVERY READING RATHER "
               "THAN AT THE ONE THAT FLATTERS: the single-site surrogate, the "
               "whole-field statement and the carrier-level group relation are counted "
               "separately, each against its own honest denominator, with the "
               "vacuous cells (R_HH = id) separated out; the tested sets are declared, "
               "not selected", True, {"sets": DECL["relation_sets"], "census": rel_rows},
               must_pass=False)
    say(f"        HA at the declared loop: Sigma R Sigma = R^-1 : {ha_dih}   "
        f"(G32 recorded)")
    say("")

    say("  12.4  THE COORDINATE TABLE.  An expression of R_HH in the stitching")
    say("        geometry's data needs a committed coordinate at which the compared")
    say("        objects both live.  Sizes are reported as sizes; equal cardinality is")
    say("        neither necessary nor sufficient for a carrier morphism to exist.")
    coord_rows = [
        ("carrier", "36 (q_A,q_B,p_A,p_B) [NT] / 81 (s_A,s_B,p_A,p_B) [GEN]",
         f"p^(k+d) total records = front sector x register ({RC.size} at p={p})"),
        ("family", "6 settings x 2 frames [NT] / 6 settings [GEN]",
         f"{len(DECL['rules'])} drag rules x {len(ADM)} geometry records"),
        ("law", "the declared legs U_prep, U_A(a), U_B(b)",
         "H_a[N] : (n,m) -> (n+N, m+w[N,n]) at a lapse profile"),
        ("state", "p(0) = delta_{j0}", "the base total record (n_sym, 0)"),
        ("arena", "(frame, read time) nodes, co-reference identifications",
         "(record site, front sector), normal and tangential comparison maps"),
        ("structure group", "Klein four {1,W,X,WX} [NT] / dihedral order 2n [GEN]",
         "cyclic of order p -- the DECLARED prime (G30)"),
        ("defect construction", "D = P_W U^-1 P_W U = (Sigma V^T Sigma V) (x) I_9",
         "R_HH = C(H[N],H[M]) D[-beta_a(g;N,M)]"),
    ]
    say(f"        {'coordinate':20s}{'NT / GEN':52s}HA")
    for (c_, a_, b_) in coord_rows:
        say(f"        {c_:20s}{a_[:50]:52s}{b_[:46]}")
    carrier_sizes = sorted({row["carrier"] for row in prime_rows})
    g22 = gate("G22", "COORDINATE REPORT (recorded, not a verdict): the compared "
               "objects' coordinates are tabulated as measured.  NO POSABILITY "
               "PREDICATE IS EVALUATED HERE -- the delivered one could not return its "
               "other value anywhere in the declared arena, and a criterion that "
               "cannot come out otherwise decides nothing (RUNBOOK 4).  What is "
               "measured: the carriers are different sizes with different "
               "factorisations, no map between them is committed anywhere, and GEN's "
               "relation fails for R_HH wherever R_HH is nontrivial",
               True,
               {"ha_carrier_sizes": carrier_sizes,
                "nt_gen_carrier_sizes": [36, 81],
                "ha_group_orders": orders,
                "ha_group_is_cyclic_on_one_generator": True,
                "nt_group": "Klein four (two generators)",
                "gen_group": "dihedral of order 2n",
                "dihedral_relation_on_R_HH_at_the_declared_loop": ha_dih,
                "committed_carrier_morphism": None,
                "morphism_census_run": False}, must_pass=False)
    say("")
    say("        WHAT IS MEASURED, AND WHAT IS NOT.")
    say("        Measured: the carriers are different sizes with different")
    say("        factorisations; HA's group is cyclic on ONE generator while NT's is")
    say("        Klein four and GEN's is dihedral, both multi-generator; and GEN's")
    say("        relation Sigma D Sigma = D^-1 fails for R_HH at every tested cell")
    say("        where R_HH is nontrivial (12.3).  NOT measured: any census of")
    say("        candidate carrier morphisms.  None was run, so nothing here is a")
    say("        nonexistence statement.  The order of the group and its membership in")
    say("        GEN's spectrum are ARENA COORDINATES (G30, G31) and are excluded from")
    say("        the argument.  THE MORPHISM QUESTION IS OPEN and is bequeathed to a")
    say("        successor unit; no HA-BRIDGE outcome is entered by this run.")
    say("")

    # ======================= 12B. THE CENSUS'S OWN COMPLETENESS ===========
    say("--- 12B. CELL COMPLETENESS AND INEQUIVALENT RECOVERED TENSORS ---")
    progress("census completeness")
    exp_closure = len(DECL["rules"]) * len(ADM)
    exp_sector = len([t for t in DECL["rules"] if arch_of(t[0]) == "A"]) * len(ADM)
    exp_d3 = len(DECL["rules_d3"]) * len([nm for nm in recs3 if recs3[nm].admissible])
    g26 = gate("G26", "EVERY DECLARED CELL IS PRESENT: the closure table, the sector-law "
               "grid and the d = 3 grid each carry exactly the number of cells their "
               "DECLARATIONS require, so a silently dropped rule or record cannot shrink "
               "a census without failing here (RUNBOOK 13 addendum, v13 #234)",
               len(results) == exp_closure and len(sector) == exp_sector
               and len(res3) == exp_d3
               and fields_computed == exp_closure * len(pairs),
               {"closure_cells": len(results), "closure_cells_declared": exp_closure,
                "sector_cells": len(sector), "sector_cells_declared": exp_sector,
                "d3_cells": len(res3), "d3_cells_declared": exp_d3,
                "residual_fields_computed": fields_computed,
                "residual_fields_declared": exp_closure * len(pairs)})
    say(f"  closure table {len(results)}/{exp_closure} cells; sector grid "
        f"{len(sector)}/{exp_sector}; d=3 grid {len(res3)}/{exp_d3}; residual fields "
        f"{fields_computed}/{exp_closure * len(pairs)}   (G26 {'PASS' if g26 else 'FAIL'})")

    tensor_rec = "G-OFFDIAG"
    rT = recs[tensor_rec]
    lam_classes: dict = {}
    for rule, _a, _dsc in RULES:
        if arch_of(rule) != "A":
            continue
        sig = tuple(tuple(tuple(row) for row in lambda_of(rule, rT, x)) for x in S)
        lam_classes.setdefault(sig, []).append(rule)
    law_classes: dict = {}
    for rule, _a, _dsc in RULES:
        sig = tuple(tuple(residual_field_closed(rule, rT, lapses[a][1],
                                                lapses[b][1])[x] for x in S)
                    for (a, b) in pairs)
        law_classes.setdefault(sig, []).append(rule)
    g27 = gate("G27", "THE KILL'S SECOND DISJUNCT FIRES, MEASURED: on ONE record the "
               "declared family supplies pairwise-INEQUIVALENT recovered tensors -- the "
               "recovered tensor of an architecture-A rule IS its weight field, since "
               "the commutator's displacement is Lambda^{ij} omega_j -- so the same "
               "record law permits inequivalent recovered tensors, over the complete "
               "declared family",
               len(lam_classes) > 1 and len(law_classes) > 1
               and sum(len(v) for v in law_classes.values()) == len(DECL["rules"]),
               {"record": tensor_rec,
                "distinct_recovered_tensors_archA": len(lam_classes),
                "archA_rules": sum(len(v) for v in lam_classes.values()),
                "recovered_tensor_classes": sorted(sorted(v) for v in
                                                   lam_classes.values()),
                "distinct_residual_laws": len(law_classes),
                "rules": sum(len(v) for v in law_classes.values()),
                "residual_law_classes": sorted(sorted(v) for v in law_classes.values())})
    say(f"  at {tensor_rec}: {len(lam_classes)} pairwise-distinct recovered tensors over "
        f"the {sum(len(v) for v in lam_classes.values())} architecture-A rules")
    for v in sorted(sorted(v) for v in lam_classes.values()):
        say(f"      {v}")
    say(f"  and {len(law_classes)} pairwise-distinct residual laws over all "
        f"{sum(len(v) for v in law_classes.values())} declared rules "
        f"(G27 {'PASS' if g27 else 'FAIL'})")
    for v in sorted(sorted(v) for v in law_classes.values()):
        say(f"      {v}")
    say("")

    # ======================= 12C. THE READOUT AS A RE-ENCODING ============
    say("--- 12C. THE READOUT IS AN INVERTIBLE LINEAR RE-ENCODING ---")
    reenc_ok = reenc_tested = 0
    for nm in ADM:
        rr = recs[nm]
        for x in S:
            reenc_tested += 1
            if all(sum(rr.q[x][i][j] * lk[i] * lk[j] for i in range(d)
                       for j in range(d)) == rr.counts[x][lk] for lk in rr.links):
                reenc_ok += 1
    idx = sym_index(d)
    readout_matrix = [[Fr(lk[i] * lk[j] * (1 if i == j else 2)) for (i, j) in idx]
                      for lk in sorted(recs[ADM[0]].links)]
    readout_det = det_exact(readout_matrix)
    g28 = gate("G28", "THE MAP FROM THE SITE'S LINK COUNTS TO THE COMPONENTS OF q IS "
               "LINEAR AND INVERTIBLE (determinant computed, exact): the geometry "
               "record and the metric candidate are THE SAME DATUM in two coordinate "
               "systems, and reading one off the other is a change of coordinates, not "
               "a reconstruction.  Recorded, because it is forced by the declared link "
               "set rather than discovered", True,
               {"readout_determinant": str(readout_det),
                "invertible": readout_det != 0,
                "sites_where_q_reproduces_every_count": reenc_ok,
                "sites_tested": reenc_tested,
                "links": len(recs[ADM[0]].links),
                "independent_components_of_q": len(idx)}, must_pass=False)
    say(f"  counts -> q is linear with exact determinant {readout_det}; q reproduces "
        f"every declared link count at {reenc_ok} of {reenc_tested} sites (G28 recorded)")
    disclose("X05", "The readout is an INVERTIBLE LINEAR RE-ENCODING of the record: at "
             "the declared arena the link counts and the components of q determine each "
             "other exactly, so 'the metric candidate' and 'the geometry record' are one "
             "datum in two coordinate systems.  Two consequences are owned here.  (i) "
             "GW1 1.2's fourth exclusion -- 'algebraic data equivalent to the target "
             "metric' -- is VACUOUS at this arena: every record-native rule has access "
             "to data equivalent to the metric by construction, so that clause cannot "
             "discriminate here and the unit's claim is about WHICH FUNCTION of the "
             "counts a rule computes, not about what data it can see.  (ii) The "
             "no-smuggling result of this unit is therefore an identity read in count "
             "coordinates, not a derivation of geometry from something else.",
             {"readout_determinant": str(readout_det)})
    say("")

    # ======================= 13. AST GUARD ================================
    say("--- 13. THE AST GUARD (RUNBOOK 14 addendum, v13 #208) ---")
    offenders = ast_mutant_scan(src)
    decoys = {
        "gate_decoy_mutant": "return gate('D1', 'decoy', MUTANT is None)",
        "gate_decoy_delivery": "return gate('D2', 'decoy', DELIVERY_RUN)",
        "gate_decoy_selftest": "return gate('D3', 'decoy', SELFTEST_ONLY)",
        "gate_decoy_argv": "return gate('D4', 'decoy', len(sys.argv) > 1)",
    }
    injected = src.replace(
        "def ast_mutant_scan(",
        "".join(f"def {nm_}():\n    {body}\n\n\n" for nm_, body in decoys.items())
        + "def ast_mutant_scan(", 1)
    inj = ast_mutant_scan(injected)
    g23 = gate("G23", "NO GATE-REGISTERING FUNCTION REFERENCES RUN-MODE IDENTITY -- "
               "neither MUTANT, nor a module switch, nor a mutant-name literal, nor a "
               "run-mode boolean (DELIVERY_RUN is mutant identity under another name), "
               "nor sys.argv -- and the scanner is validated by FOUR synthetic "
               "injections, one per channel, every one of which it must flag",
               offenders == [] and all(nm_ in inj for nm_ in decoys),
               {"offenders": offenders, "injection_flagged": inj,
                "decoy_channels": sorted(decoys)})
    say(f"  gate-registering functions referencing run-mode identity: {offenders}")
    say(f"  synthetic injections flagged by the scanner             : {inj}")
    say(f"  G23 AST guard: {'PASS' if g23 else 'FAIL'}")
    say("")

    say("--- 13B. THE FLOAT SWEEP (RUNBOOK 4) ---")
    fl = ast_float_scan(src)
    fl_inj = ast_float_scan(src.replace("def ast_float_scan(",
                                        "def _decoy_float():\n"
                                        "    return 0.5 + float(1)\n\n\n"
                                        "def ast_float_scan(", 1))
    exact_types = set()
    for rule in ("A-axis", "A-insert"):
        for nm in ADM:
            f_ = residual_field_closed(rule, recs[nm], Na, Mb)
            for v in f_.values():
                for t in v:
                    exact_types.add(type(t).__name__)
    g24 = gate("G24", "NO FLOAT ENTERS ANY SUBSTANTIVE PATH: the instrument's own source "
               "carries no float or complex literal and never calls float()/complex() "
               "(the scanner validated by a synthetic injection it must flag), and every "
               "value of every residual field is measured to be an exact type",
               fl == [] and len(fl_inj) == 2 and exact_types <= {"Fraction", "int"},
               {"float_hits": fl, "injection_flagged": fl_inj,
                "residual_value_types": sorted(exact_types)})
    say(f"  float/complex literals and casts in the source : {fl}")
    say(f"  synthetic injection flagged by the sweep       : {len(fl_inj)} hits")
    say(f"  measured types of every residual field value   : {sorted(exact_types)}")
    say(f"  G24 float sweep: {'PASS' if g24 else 'FAIL'}")
    say("")

    # ======================= 14. THE VERDICT, DERIVED IN A GATE ===========
    say("--- 14. VERDICT ---")
    pre = [g["id"] for g in GATES if g["must_pass"] and not g["passed"]]
    ha_runnable = (g04 and g05 and g10 and g10b and g11 and len(pre) == 0)
    bridge_token = "HA-BRIDGE-NOT-ENTERED"
    verdict = derive_verdict(ha_runnable, bridge_token)
    printed = "  " + " + ".join(verdict)
    say(printed)
    expect_runnable = (g04 and g05 and g10 and g10b and g11
                       and not [g["id"] for g in GATES
                                if g["must_pass"] and not g["passed"]])
    expect = (["HA-RUNNABLE"] if expect_runnable
              else ["HA-STILL-BLOCKED"]) + [bridge_token]
    g25 = gate("G25", "THE PRINTED VERDICT IS DERIVED INSIDE THIS GATE FROM THE "
               "MEASURED COUNTS AND COMPARED, STRING BY STRING, TO WHAT THE RUN "
               "PRINTED (RUNBOOK 13 addendum, v13 #234: an ungated verdict is a typo "
               "away from fiction).  The runnable component is recomputed here from "
               "the same measured gate outcomes and from the failure count over the "
               "must-pass gates registered before the verdict; the secondary component "
               "is NOT-ENTERED because no posability predicate is evaluated anywhere "
               "in this run",
               verdict == expect and printed == "  " + " + ".join(expect),
               {"printed": verdict, "derived_here": expect})
    say(f"  G25 verdict derivation: {'PASS' if g25 else 'FAIL'}")
    say("")
    if ha_runnable:
        say("  A record-native H_a[N] EXISTS at finite N.  It is constructed on total")
        say("  finite matter-geometry records, measured invertible, lapse-profiled, and")
        say("  its second normal step is transported along the first.  The GW1 residual")
        say("  R_HH RUNS, at the committed finite scope, as an exact rational field and")
        say("  as an actual operator on a finite total-configuration carrier.")
        say("")
        say("  THE CLOSURE RESULT: CLOSURE ON THE DIAGONAL SECTOR, ANOMALY AT THE CROSS")
        say("  TERM.  The link-local record-native rule closes on every record whose")
        say("  order+count readout is diagonal -- flat and inhomogeneous alike, at d = 2")
        say("  and at d = 3 -- and fails at every record whose readout carries a nonzero")
        say("  cross term, because I^{ij} = adj(q)^{ij}/det q and det q is a joint")
        say("  function of the site's link counts that no link-local rule reads (G09).")
        say("  Site by site, the residual vanishes exactly where the drag weight IS the")
        say("  record-read inverse metric (G08).  That equality is what closure means")
        say("  here, and the recovered tensor is the rule's own weight: on ONE record")
        say("  the declared family supplies pairwise-inequivalent recovered tensors")
        say("  (G27), which is the second disjunct of GW1's kill condition, measured.")
    else:
        say("  THE UNIT IS BLOCKED: at least one must-pass gate failed, so no")
        say("  construction or closure statement is made by this run.")
    say("")
    say("  THE DECLARED SECONDARY IS NOT DECIDED HERE.  Section 12 is a coordinate")
    say("  audit: it reports what R_HH and the stitching geometry share and what is")
    say("  arena.  No posability predicate is evaluated, no morphism census is run,")
    say("  and no HA-BRIDGE outcome is entered.  THE MORPHISM QUESTION IS OPEN.")
    say("")

    # ======================= 15. THE GATE TABLE ===========================
    must = [g for g in GATES if g["must_pass"]]
    failed = [g["id"] for g in must if not g["passed"]]
    say("--- 15. GATES ---")
    for g in GATES:
        say(f"  {g['id']}  {'PASS' if g['passed'] else 'FAIL'}  "
            f"{'must-pass' if g['must_pass'] else 'recorded ' }  {g['claim'][:92]}")
    say(f"  must-pass gates {len(must)};  failures {len(failed)} {failed}")
    say("")

    return {
        "failed": failed, "must": must, "verdict": verdict,
        "hash_pins": {"v13/code/nt_transport_receipt.json": sha256_file(nt_path),
                      "v13/code/gen_generality_receipt.json": sha256_file(gen_path)},
        "tables": {
            "closure": {f"{k[0]}|{k[1]}": v for k, v in sorted(results.items())},
            "sector_law": {f"{k[0]}|{k[1]}": v for k, v in sorted(sector.items())},
            "identifiability_rank": {str(k): v for k, v in sorted(rank_at.items())},
            "operator_layer": {"carriers_built": op_built, "mismatches": op_mismatch,
                               "non_bijective": op_nonbij,
                               "rows_p5": [{"rule": a, "record": b, "p": c,
                                            "carrier": e, "moved": f}
                                           for (a, b, c, e, f) in op_rows]},
            "general_d": {f"{k[0]}|{k[1]}": v for k, v in sorted(res3.items())},
            "detector": [{"rule": a, "record": b, "triple": c, "C_trivial": e,
                          "jacobi_lapse_sum_zero": f, "SW_front_zero": g,
                          "SW_register_zero": h, "max_abs_register": i}
                         for (a, b, c, e, f, g, h, i) in det_rows],
            "detector_closed_form": {"compared": hhh_cmp, "disagreements": hhh_bad},
            "density_weight_flip": flip_rows,
            "link_locality_witness": witness,
            "link_locality_lattice": {"admissible_points": len(lat),
                                      "pairs_sharing_n_diag_diff_I12": lat_w12,
                                      "pairs_sharing_n_e1_n_diag_diff_I11": lat_w11},
            "recovered_tensors": {
                "record": tensor_rec,
                "distinct_recovered_tensors_archA": len(lam_classes),
                "classes": sorted(sorted(v) for v in lam_classes.values()),
                "distinct_residual_laws": len(law_classes),
                "law_classes": sorted(sorted(v) for v in law_classes.values())},
            "readout_reencoding": {"determinant": str(readout_det),
                                   "sites_verified": reenc_ok},
            "bridge": {
                "status": "COORDINATE AUDIT -- no posability predicate evaluated, "
                          "no morphism census run, no HA-BRIDGE outcome entered",
                "prime_sweep": prime_rows,
                "exact_residual_at_the_detector_site": [str(t) for t in rho_exact],
                "gen_defect_order": gen_ord, "gen_dihedral": gen_dih,
                "gen_dihedral_is_analytically_forced": True,
                "declared_3_cycle_satisfies_the_relation": ctrl_dih,
                "ha_dihedral_at_the_declared_loop": ha_dih,
                "defect_order_spectrum": dict(defect_spectrum),
                "holonomy_order_spectrum": holonomy_spectrum,
                "membership_in_the_defect_spectrum_by_prime": memb,
                "sigma_relation_census": rel_rows,
                "committed_carrier_morphism": None,
                "morphism_census_run": False},
        },
        "totals": {"anchors": len(ANCHORS), "gates": len(GATES),
                   "must_pass_gates": len(must), "must_pass_failures": len(failed),
                   "disclosures": len(DISCLOSURES)},
    }


def main() -> int:
    """Run mode, receipts and the mutant harness.  Registers NO gate, so no gate
    can depend on the run mode, directly or indirectly (G23)."""
    src = open(SELF, "r", encoding="utf-8").read()
    R = run_unit(src)
    if not DELIVERY_RUN:
        return 1 if R["failed"] else 0

    progress("receipt")
    receipt = {
        "schema": "ha-successor-receipt-v1",
        "pin": "v13/note-ha-successor-pin.md",
        "pin_base_commit": "024fcd7",
        "source_sha256": hashlib.sha256(src.encode()).hexdigest(),
        "python": platform.python_version(),
        "arithmetic": "fractions.Fraction / integers / exact F_p; no floats",
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
        with open(os.path.join(HERE, "ha_successor_output.txt"), "w",
                  encoding="utf-8") as fh:
            fh.write("\n".join(OUT) + "\n")
        with open(os.path.join(HERE, "ha_successor_receipt.json"), "w",
                  encoding="utf-8") as fh:
            json.dump(receipt, fh, indent=1, sort_keys=True, default=str)
            fh.write("\n")
    else:
        progress("falsification-selftest: artifacts NOT written")
    progress("done")
    return 0 if (not R["failed"] and not survivors and not never_falsified) else 1


if __name__ == "__main__":
    sys.exit(main())

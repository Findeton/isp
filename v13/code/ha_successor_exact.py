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
    "anchor-gw1-trees":   "GW1 runnable-tree .py census perturbed",
    "anchor-gw1-lapse":   "GW1 'lapse' token sweep perturbed",
    "anchor-nt-paths":    "NT reduced-path count perturbed",
    "anchor-nt-sha":      "NT receipt sha256 perturbed",
    "anchor-gen-family":  "GEN completion-family size perturbed",
    "anchor-gen-defect":  "GEN declared defect permutation perturbed",
    # --- gate mutants (each mutates an INSTRUMENT, never a gate) ----------
    "closure-lax":    "the closure predicate accepts any residual field",
    "invert-lax":     "the bijection predicate accepts a non-injective map",
    "bridge-lax":     "the bridge posability predicate drops its coordinate test",
    "exempt-lax":     "the AST mutant-identity scanner is blinded",
    "control-lax":    "the broken-H variants are dropped from the tested set",
    "rank-lax":       "the lapse family is degenerated below full rank",
    "freeze-lax":     "a fixture datum is evaluated before the declarations freeze",
    "cache-lax":      "the fresh-evaluation path reads the memo cache",
    "posdef-lax":     "the positive-definiteness predicate always accepts",
    "factor-lax":     "the exact-to-F_p reduction is perturbed non-linearly",
    # --- computational mutants -------------------------------------------
    "sign-flip":      "the finite bracket covector's sign convention is flipped",
    "order-swap":     "the two normal labels are swapped in the commutator only",
    "transport-off":  "the second normal step reads the pre-advance front",
    "chart-shift":    "the chart action moves the record but not the field index",
    "beta-flat":      "the record-read metric in beta is replaced by the chart identity",
    "prime-single":   "the operator layer's multi-prime control is reduced to one prime",
    "omega-asym":     "the finite bracket covector uses a non-antisymmetric difference",
    "readout-local":  "the record's metric readout is replaced by a link-local surrogate",
    "float-lax":      "the float sweep is blinded",
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
_M_CLOSURE = (MUTANT == "closure-lax")
_M_INVERT = (MUTANT == "invert-lax")
_M_BRIDGE = (MUTANT == "bridge-lax")
_M_EXEMPT = (MUTANT == "exempt-lax")
_M_CONTROL = (MUTANT == "control-lax")
_M_RANK = (MUTANT == "rank-lax")
_M_FREEZE = (MUTANT == "freeze-lax")
_M_CACHE = (MUTANT == "cache-lax")
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
    "frozen_front_rule": "A-notransport",
    "positive_control_rule": "A-insert",
    "primes": [5, 7, 13],
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
    key = (rule, rec.name, rec.weight, x)
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


def bridge_posable(carrier_match, in_spectrum, relation_holds):
    """The declared posability predicate.  [instrument -- mutable]"""
    if _M_BRIDGE:
        return True
    return bool(carrier_match and in_spectrum and relation_holds)


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


def ast_mutant_scan(src: str) -> list[str]:
    """Names of functions that BOTH register a gate AND reference mutant identity.
    [instrument -- mutable]"""
    if _M_EXEMPT:
        return []
    tree = ast.parse(src)
    offenders = []
    names = set(MUTANTS.keys())
    switches = {n for n in dir() if n.startswith("_M_")}

    class V(ast.NodeVisitor):
        def visit_FunctionDef(self, node):  # noqa: N802
            registers = references = False
            for sub in ast.walk(node):
                if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Name) \
                        and sub.func.id == "gate":
                    registers = True
                if isinstance(sub, ast.Name) and (sub.id in ("MUTANT", "MUTANTS")
                                                  or sub.id.startswith("_M_")):
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


def main() -> int:
    progress("start")
    src = open(SELF, "r", encoding="utf-8").read()
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
    anchor("A14", "GEN: the order spectrum of the defect over the whole family",
           {1: 96, 2: 1440, 3: 4224, 4: 4608, 5: 4608, 6: 6912, 7: 9216, 15: 9216},
           dict(sorted(ord_hist.items())), "v13/paper-gen-generality-check.md 8.2")
    anchor("A15", "GEN: the fixed-configuration spectrum of the defect",
           {9: 16704, 18: 11520, 27: 5376, 36: 4608, 45: 864, 54: 1152, 81: 96},
           dict(sorted(fix_hist.items())), "v13/paper-gen-generality-check.md 8.2")
    anchor("A16", "GEN: members where the dihedral relation Sigma D Sigma = D^-1 fails",
           0, dihedral_fail, "v13/paper-gen-generality-check.md 8.3")
    say(f"  {len(ANCHORS)} anchors, every one reproduced.")
    v12n = len([f for f in os.listdir(os.path.join(REPO, "v12/code")) if f.endswith(".py")])
    v13n = len([f for f in os.listdir(os.path.join(REPO, "v13/code")) if f.endswith(".py")])
    say(f"  DISCLOSURE X01: v12/code carries {v12n} .py against the GW1 census's 5, and")
    say(f"  v13/code carries {v13n} (four concurrent cycles).  Both are declared LIVE")
    say("  and excluded from A01 BY DECLARATION, not by outcome.")
    disclose("X01", "two trees moved since the GW1 census and are excluded from A01 "
             "by declaration", {"v12/code": {"census": 5, "now": v12n},
                                "v13/code": {"census": "not listed", "now": v13n}})
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
    inv_fail = inv_tested = 0
    for rule, _a, _dsc in DECL["rules"]:
        for nm in ADM:
            for (lname, N) in lapses[:4]:
                H = Hmap(rule, recs[nm], N)
                inv_tested += 1
                if not check_bijection_pair(H, (dict(n_base), dict(m_zero))):
                    inv_fail += 1
    coll = RegisterCollapse(recs["G-FLAT"])
    m1 = {x: tuple(Fr(1) for _ in range(d)) for x in S}
    falsifier_rejected = not check_bijection_pair(coll, (dict(n_base), dict(m1)))
    g04 = gate("G04", "EVERY MEMBER OF THE CONSTRUCTED H FAMILY IS AN EXACT BIJECTION "
               "OF TOTAL RECORDS, MEASURED BY H^-1 H = H H^-1 = id; and the declared "
               "non-injective falsifier (register collapse) is REJECTED by the same "
               "predicate", inv_fail == 0 and falsifier_rejected,
               {"tested": inv_tested, "failures": inv_fail,
                "falsifier_rejected": falsifier_rejected})
    say(f"  H^-1 H = id measured on {inv_tested} (rule, record, lapse) triples; "
        f"failures {inv_fail}")
    say(f"  declared non-injective falsifier rejected: {falsifier_rejected}   "
        f"(G04 {'PASS' if g04 else 'FAIL'})")
    say("")

    # ======================= 6. THE RESIDUAL ==============================
    say("--- 6. THE GW1 RESIDUAL  R_HH,a[N,M] = H[N]H[M]H[N]^-1 H[M]^-1 D[-beta] ---")
    say("       RUN at the committed finite scope, by two independent routes:")
    say("       (a) the LITERAL composition of the five comparison maps;")
    say("       (b) the CLOSED form, built from the drag rule and the record")
    say("           readout without ever touching (a).")
    progress("residual sweep")
    results, per_site = {}, {}
    lit_fail = lit_cmp = 0
    for rule, _a, _dsc in DECL["rules"]:
        for nm in ADM:
            r = recs[nm]
            nz, worst, wit = 0, Fr(0), None
            zero_sites = {x: True for x in S}
            for (a, b) in pairs:
                fc = residual_field_closed(rule, r, lapses[a][1], lapses[b][1])
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
            for (a, b) in [(p_, q_) for (p_, q_) in pairs if p_ < 4 and q_ < 4]:
                fl = residual_field_literal(rule, r, lapses[a][1], lapses[b][1], n_base)
                fc = residual_field_closed(rule, r, lapses[a][1], lapses[b][1])
                lit_cmp += 1
                if fl is None or any(fl[x] != fc[x] for x in S):
                    lit_fail += 1
    g05 = gate("G05", "THE LITERAL FIVE-MAP COMPOSITION AND THE INDEPENDENTLY BUILT "
               "CLOSED FORM AGREE FIELD BY FIELD (the comparator is not a copy of the "
               "audited object routed through it -- RUNBOOK 14 addendum, v13 #219)",
               lit_fail == 0, {"compared": lit_cmp, "disagreements": lit_fail})
    say(f"  literal-vs-closed comparisons {lit_cmp}, disagreements {lit_fail}   "
        f"(G05 {'PASS' if g05 else 'FAIL'})")
    say("")
    say(f"  CLOSURE TABLE.  Cells give the number of the {len(pairs)} ordered lapse")
    say("  pairs at which R_HH is NOT the identity ('CLOSES' = none of them).")
    say(f"  {'rule':14s}" + "".join(f"{nm:11s}" for nm in ADM))
    for rule, _a, _dsc in DECL["rules"]:
        say(f"  {rule:14s}" + "".join(
            f"{('CLOSES' if results[(rule, nm)]['closes'] else str(results[(rule, nm)]['nonzero_pairs'])):11s}"
            for nm in ADM))
    say("")
    g06 = gate("G06", "POSITIVE CONTROL: the metric-INSERTED rule (Lambda = I_a(g)) "
               "closes exactly, at every admissible record and every tested lapse pair",
               all(results[("A-insert", nm)]["closes"] for nm in ADM),
               {nm: results[("A-insert", nm)]["closes"] for nm in ADM})
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
    for rule, _a, _dsc in DECL["rules"]:
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
    g08 = gate("G08", "SITE BY SITE, THE RESIDUAL VANISHES EXACTLY WHERE THE DRAG "
               "RULE'S WEIGHT COINCIDES WITH THE RECORD-READ INVERSE METRIC: closure "
               "IS insertion, over the whole rule x record x site grid",
               len(mism) == 0, {"cells": len(sector), "mismatches": mism})
    say(f"  {'rule':14s}" + "".join(f"{nm:11s}" for nm in ADM))
    for rule, _a, _dsc in DECL["rules"]:
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
             "identity, no gate predicate reads it, and the AST guard (G23) forbids "
             "every gate-registering function from naming MUTANT, a per-mutant "
             "switch, or a mutant name.")
    disclose("X02", "The equivalence measured by G08 is ANALYTICALLY FORCED once G03's "
             "rank is full: rho^i = (Lambda^{ij} - I^{ij}) omega_j vanishes on a "
             "spanning covector family iff Lambda = I.  It is therefore recorded as a "
             "DISCLOSURE, not claimed as an independent discovery; the measured content "
             "is G03's rank, the cell census, and the residual magnitudes below.")
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
    say("--- 7. CAN ANY LINK-LOCAL RECORD-NATIVE WEIGHT CLOSE?  (measured) ---")
    progress("link locality")
    witness = None
    x0 = (0,) * d
    cand = [(nm1, nm2, j) for nm1 in ADM for nm2 in ADM for j in range(d)
            if nm1 < nm2]
    for (nm1, nm2, j) in cand:
        if witness is not None:
            break
        r1, r2 = recs[nm1], recs[nm2]
        lk = r1.links[j]
        if r1.counts[x0][lk] == r2.counts[x0][lk] \
                and r1.I[x0][j][j] != r2.I[x0][j][j]:
            witness = {"records": [nm1, nm2], "direction": j, "link": str(lk),
                       "shared_interval_count": r1.counts[x0][lk],
                       "I^jj_demanded": [str(r1.I[x0][j][j]), str(r2.I[x0][j][j])],
                       "other_counts": [str(tuple(r1.counts[x0][t] for t in r1.links)),
                                        str(tuple(r2.counts[x0][t] for t in r2.links))]}
    g09 = gate("G09", "A LINK-LOCAL RECORD-NATIVE WEIGHT CANNOT CLOSE IN GENERAL: two "
               "admissible records AGREE on a link's own interval count yet the "
               "record-read inverse metric demands DIFFERENT weights there "
               "(counterexample exhibited, not argued)",
               witness is not None, {"witness": witness})
    say(f"  counterexample: {json.dumps(witness)}")
    say(f"  G09 link-locality obstruction: {'PASS' if g09 else 'FAIL'}")
    say("  Reading: I^{jj} = adj(q)^{jj} / det q, and det q is a JOINT function of every")
    say("  link count at the site.  A weight that reads only its own link's count")
    say("  cannot see it.  Closure therefore requires a rule that computes the")
    say("  record's count-matrix inverse -- which is the metric.")
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
        for rule, _a, _dsc in DECL["rules"]:
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

    ord_bad = ord_tested = 0
    for nm in ADM:
        r = recs[nm]
        for (a, b) in pairs[:40]:
            f1 = residual_field_closed("A-axis", r, lapses[a][1], lapses[b][1])
            f2 = residual_field_closed("A-axis", r, lapses[b][1], lapses[a][1])
            ord_tested += 1
            if any(f1[x][i] != -f2[x][i] for x in S for i in range(d)):
                ord_bad += 1
    g13 = gate("G13", "UPDATE-ORDER CONTROL: exchanging the two normal labels sends the "
               "residual field to its exact negative at every site, so the measured "
               "two-cell is genuinely antisymmetric and not an artefact of one order",
               ord_bad == 0, {"tested": ord_tested, "violations": ord_bad})
    say(f"  update-order control: {ord_tested} pairs, antisymmetry violations "
        f"{ord_bad}   (G13 {'PASS' if g13 else 'FAIL'})")

    progress("chart self-test")
    cb = dict(_CACHE_STATS)
    chart_bad = chart_tested = 0
    sigmas = list(itertools.permutations(range(d)))
    shifts = S
    for sigma in sigmas:
        inv_sigma = [0] * d
        for i in range(d):
            inv_sigma[sigma[i]] = i
        for sh in shifts[:3]:
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
                for (a, b) in pairs[:10]:
                    Nn, Mm = lapses[a][1], lapses[b][1]
                    N2 = {phi(x): Nn[x] for x in S}
                    M2 = {phi(x): Mm[x] for x in S}
                    f1 = residual_field_closed("A-axis", r, Nn, Mm)
                    f2 = residual_field_closed("A-axis", r2, N2, M2)
                    for x in S:
                        lhs = tuple(f1[x][sigma[i]] for i in range(d))
                        chart_tested += 1
                        if lhs != f2[phi(x)]:
                            chart_bad += 1
                for x in S:
                    lambda_of("A-axis", r, x, fresh=True)
    ca = dict(_CACHE_STATS)
    g14 = gate("G14", "CHART SELF-TEST (RUNBOOK 14): the residual field is EQUIVARIANT "
               "under every declared chart translation and direction relabelling, "
               "measured site by site and component by component on freshly rebuilt "
               "records", chart_bad == 0,
               {"tested": chart_tested, "violations": chart_bad,
                "relabellings": len(sigmas), "translations": len(shifts[:3])})
    g15 = gate("G15", "THE SELF-TEST'S CACHE PATH IS EXERCISED AND ITS FRESH PATH "
               "BYPASSES IT (RUNBOOK 14 addenda, v13 #185 / #219: a zero-hit cache gate "
               "must also gate that the cache path is used at all)",
               ca["bypass"] > cb["bypass"] and ca["hits"] > 0 and ca["misses"] > 0,
               {"hits": ca["hits"], "misses": ca["misses"], "fresh_bypasses": ca["bypass"]})
    say(f"  chart self-test: {chart_tested} component comparisons, violations "
        f"{chart_bad}   (G14 {'PASS' if g14 else 'FAIL'})")
    say(f"  cache hits {ca['hits']}, misses {ca['misses']}, fresh bypasses "
        f"{ca['bypass']}   (G15 {'PASS' if g15 else 'FAIL'})")

    mf_trivial = True
    for rule, _a, _dsc in DECL["rules"]:
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
    say("  residual exactly at every record, and its three-normal detector is")
    say("  nevertheless nonzero.  Pair closure does not buy HHH closure -- the finite")
    say("  measurement of v4 paper 12's own reason for building the corrected switch.")
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
    say(f"  {'rule':14s}" + "".join(f"{nm:12s}" for nm in sorted(recs3)))
    for rule in ("A-chart", "A-axis", "A-linkframe", "A-insert"):
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
    say("--- 12. THE DECLARED SECONDARY: CAN R_HH BE EXPRESSED IN THE STITCHING")
    say("        GEOMETRY'S DATA?  (NT and GEN, receipts hash-pinned at A05/A06)")
    say("=" * 78)
    progress("bridge")
    say("  12.1  THE HA RESIDUAL AS A HOLONOMY, computed in the coordinate NT and GEN")
    say("        use: the based closed-loop product of the link transports, counted as")
    say("        group elements and never as name labels.")
    p = 5
    r = recs["G-OFFDIAG"]
    n_sym = {x: (x[0] * x[1]) % p for x in S}          # symmetric under the swap
    N_sym = {y: (1 if y == (0, 0) else 0) for y in S}  # symmetric
    M_sym = {y: (1 if y in ((0, 1), (1, 0)) else 0) for y in S}   # symmetric
    xs = (0, 0)
    RC = ReducedCarrier(r, p, n_sym, [N_sym, M_sym], xs)
    PN, PM = RC.perm_H("A-axis", N_sym, None), RC.perm_H("A-axis", M_sym, None)
    bb = beta(r, N_sym, M_sym)
    PD = RC.perm_D({x: tuple(-bb[x][i] for i in range(d)) for x in S})
    R_HA = perm_compose(PN, perm_compose(PM, perm_compose(
        perm_inv(PN), perm_compose(perm_inv(PM), PD))))
    ha_group = sorted(group_closure([tuple(R_HA)], tuple(range(RC.size))))
    ha_order = len(ha_group)
    ha_abelian = all(perm_mul(list(g1), list(g2)) == perm_mul(list(g2), list(g1))
                     for g1 in ha_group for g2 in ha_group)
    ha_exponents = sorted({perm_order(list(g)) for g in ha_group})
    say(f"        carrier {RC.size}; HA residual holonomy group order {ha_order}, "
        f"abelian {ha_abelian}, element orders {ha_exponents}")

    say("  12.2  GEN's OWN STRUCTURAL RELATIONS, tested on the HA residual, with GEN's")
    say("        own defect as the positive control.")
    D_gen = gen_defect(Q_declared)
    gen_dih = perm_mul(S9, perm_mul(D_gen, S9)) == perm_inv(D_gen)
    gen_ord = perm_order(D_gen)
    say(f"        [positive control] GEN's declared defect: order {gen_ord}, "
        f"Sigma D Sigma = D^-1 : {gen_dih}")

    def ha_sigma(RC):
        out = [0] * RC.size
        for fi, f in enumerate(RC.fronts):
            key = tuple(sorted({x: f[(x[1], x[0])] for x in S}.items()))
            fj = RC.front_index.get(key)
            if fj is None:
                return None
            for reg in RC.regs:
                out[RC.code(fi, reg)] = RC.code(fj, (reg[1], reg[0]))
        return out
    SIG = ha_sigma(RC)
    say(f"        the declared chart involution preserves the front sector: "
        f"{SIG is not None}")
    ha_dih = None
    dih_hold = dih_tested = 0
    if SIG is not None:
        ha_dih = (perm_mul(SIG, perm_mul(R_HA, SIG)) == perm_inv(R_HA))
        for (a, b) in pairs[:24]:
            Nn, Mm = lapses[a][1], lapses[b][1]
            rho = residual_field_closed("A-axis", r, Nn, Mm)[xs]
            dih_tested += 1
            if rho[0] + rho[1] == 0:
                dih_hold += 1
    say(f"        HA: Sigma R Sigma = R^-1 at the declared loop : {ha_dih}")
    say(f"        over {dih_tested} further lapse pairs the same relation holds at "
        f"{dih_hold} of them")

    say("  12.3  THE COORDINATE TABLE.  A stitching-geometry expression of R_HH needs a")
    say("        committed coordinate at which the compared objects both live.")
    coord_rows = [
        ("carrier", "36 (q_A,q_B,p_A,p_B) [NT] / 81 (s_A,s_B,p_A,p_B) [GEN]",
         f"{RC.size} total records = front sector x address register"),
        ("family", "6 settings x 2 frames [NT] / 6 settings [GEN]",
         f"{len(DECL['rules'])} drag rules x {len(ADM)} geometry records"),
        ("law", "the declared legs U_prep, U_A(a), U_B(b)",
         "H_a[N] : (n,m) -> (n+N, m+w[N,n]) at a lapse profile"),
        ("state", "p(0) = delta_{j0}", "the base total record (n_sym, 0)"),
        ("arena", "(frame, read time) nodes, co-reference identifications",
         "(record site, front sector), normal and tangential comparison maps"),
        ("structure group", "Klein four {1,W,X,WX} [NT] / dihedral order 2n [GEN]",
         f"elementary abelian of exponent {p}, order {ha_order} here"),
        ("defect construction", "D = P_W U^-1 P_W U = (Sigma V^T Sigma V) (x) I_9",
         "R_HH = C(H[N],H[M]) D[-beta_a(g;N,M)]"),
    ]
    say(f"        {'coordinate':20s}{'NT / GEN':52s}HA")
    for (c_, a_, b_) in coord_rows:
        say(f"        {c_:20s}{a_[:50]:52s}{b_[:46]}")
    carrier_match = RC.size in (36, 81)
    in_spectrum = ha_order in (1, 4, 6, 8, 10, 12, 14, 30)
    is_klein = (ha_order == 4 and ha_abelian and ha_exponents in ([1, 2], [2], [1]))
    posable = bridge_posable(carrier_match, in_spectrum, bool(ha_dih))
    say("")
    say(f"        carrier size matches a committed NT/GEN carrier   : {carrier_match}")
    say(f"        HA holonomy order in GEN's measured spectrum       : {in_spectrum}"
        f"   (order {ha_order}; spectrum {{1,4,6,8,10,12,14,30}})")
    say(f"        HA holonomy group is NT/GEN's Klein four-group     : {is_klein}")
    say(f"        GEN's defining relation Sigma D Sigma = D^-1 holds : {ha_dih}")
    g22 = gate("G22", "BRIDGE POSABILITY IS DECIDED BY THE COORDINATE TABLE AND BY GEN's "
               "OWN DEFINING RELATION, both measured: an expression of R_HH in the "
               "stitching geometry's data requires a committed carrier match AND a "
               "structure group in GEN's measured family AND the dihedral relation; "
               "the positive control is that GEN's own defect satisfies the relation",
               gen_dih and (not posable),
               {"carrier_match": carrier_match, "ha_group_order": ha_order,
                "ha_abelian": ha_abelian, "ha_element_orders": ha_exponents,
                "in_gen_spectrum": in_spectrum, "is_klein": is_klein,
                "dihedral_relation_on_R_HH": ha_dih,
                "dihedral_relation_over_further_pairs": f"{dih_hold}/{dih_tested}",
                "positive_control_gen_defect_relation": gen_dih,
                "posable": posable})
    say("")
    say(f"        BRIDGE VERDICT: {'POSABLE' if posable else 'NOT POSABLE'}   "
        f"(G22 {'PASS' if g22 else 'FAIL'})")
    if not posable:
        say("        NAMED OBSTRUCTION -- NO COMMITTED CARRIER MORPHISM.  The stitching")
        say("        geometry's defect law is a statement about a fixed 81-element (or")
        say("        36-element) process carrier factorised as a system pair times a")
        say("        pointer pair, with Sigma the pair-label exchange and the defect the")
        say("        failure of a declared completion to intertwine that exchange.  R_HH")
        say("        lives on total matter-geometry records with no such factorisation,")
        say("        no exchange-typed completion, and no committed map to that carrier.")
        say("        The measured consequences: the HA holonomy group has order "
            f"{ha_order},")
        say(f"        exponent {p}, which is {'in' if in_spectrum else 'NOT in'} GEN's "
            f"measured order spectrum; and GEN's defining relation is measured")
        say(f"        {'to hold' if ha_dih else 'NOT to hold'} for R_HH, while the same "
            f"relation is measured to hold for")
        say("        GEN's own defect (the positive control).")
    say("")

    # ======================= 13. AST GUARD ================================
    say("--- 13. THE AST GUARD (RUNBOOK 14 addendum, v13 #208) ---")
    offenders = ast_mutant_scan(src)
    injected = src.replace(
        "def ast_mutant_scan(",
        "def gate_decoy_injected():\n"
        "    return gate('DECOY', 'decoy', MUTANT is None)\n\n\n"
        "def ast_mutant_scan(", 1)
    inj = ast_mutant_scan(injected)
    g23 = gate("G23", "NO GATE-REGISTERING FUNCTION REFERENCES MUTANT IDENTITY (neither "
               "MUTANT, nor a module switch, nor a mutant-name literal), and the scanner "
               "is validated by a synthetic injection that it MUST flag",
               offenders == [] and "gate_decoy_injected" in inj,
               {"offenders": offenders, "injection_flagged": inj})
    say(f"  gate-registering functions referencing mutant identity: {offenders}")
    say(f"  synthetic injection flagged by the scanner            : {inj}")
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

    # ======================= 14. GATES AND VERDICT ========================
    must = [g for g in GATES if g["must_pass"]]
    failed = [g["id"] for g in must if not g["passed"]]
    say("--- 14. GATES ---")
    for g in GATES:
        say(f"  {g['id']}  {'PASS' if g['passed'] else 'FAIL'}  "
            f"{'must-pass' if g['must_pass'] else 'recorded ' }  {g['claim'][:92]}")
    say(f"  must-pass gates {len(must)};  failures {len(failed)} {failed}")
    say("")

    say("--- 15. VERDICT ---")
    ha_runnable = (g04 and g05 and g10 and g10b and g11 and len(failed) == 0)
    verdict = (["HA-RUNNABLE"] if ha_runnable else ["HA-STILL-BLOCKED"]) + \
              ["HA-BRIDGE-POSABLE" if posable else "HA-BRIDGE-NOT-POSABLE"]
    say("  " + " + ".join(verdict))
    say("")
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
    say("  record-read inverse metric (G08): on this construction, closure is")
    say("  insertion.  GW1's kill condition is thereby measured rather than asserted.")
    say("")

    if not DELIVERY_RUN:
        return 1 if failed else 0

    # ======================= receipt ======================================
    progress("receipt")
    receipt = {
        "schema": "ha-successor-receipt-v1",
        "pin": "v13/note-ha-successor-pin.md",
        "pin_base_commit": "024fcd7",
        "source_sha256": hashlib.sha256(src.encode()).hexdigest(),
        "python": platform.python_version(),
        "arithmetic": "fractions.Fraction / integers / exact F_p; no floats",
        "hash_pins": {"v13/code/nt_transport_receipt.json": sha256_file(nt_path),
                      "v13/code/gen_generality_receipt.json": sha256_file(gen_path)},
        "declarations": json.loads(json.dumps(DECL, default=str)),
        "anchors": ANCHORS,
        "gates": GATES,
        "disclosures": DISCLOSURES,
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
            "density_weight_flip": flip_rows,
            "link_locality_witness": witness,
            "bridge": {"ha_holonomy_order": ha_order, "ha_abelian": ha_abelian,
                       "ha_element_orders": ha_exponents,
                       "gen_defect_order": gen_ord, "gen_dihedral": gen_dih,
                       "ha_dihedral": ha_dih,
                       "ha_dihedral_over_pairs": f"{dih_hold}/{dih_tested}",
                       "carrier_match": carrier_match,
                       "in_gen_spectrum": in_spectrum, "posable": posable},
        },
        "totals": {"anchors": len(ANCHORS), "gates": len(GATES),
                   "must_pass_gates": len(must), "must_pass_failures": len(failed),
                   "disclosures": len(DISCLOSURES)},
        "verdict": verdict,
    }

    # ======================= the mutant harness ===========================
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
    return 0 if (not failed and not survivors and not never_falsified) else 1


if __name__ == "__main__":
    sys.exit(main())

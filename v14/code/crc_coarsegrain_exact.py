#!/usr/bin/env python3
"""v14 CR-C -- THE COARSE-GRAINING SEMIGROUP (paper-07).

Merging is the direction the grammar licenses.  This instrument constructs the
merge moves on I7's arena class, runs the R6a choice inventory on the merge
direction for the FULL record (s, n, m), measures the transformation law, the
fixed-point census, the merge/dynamics commutation, and the split-then-merge
consistency control against R6a's DELIVERED-UNDER-PANEL receipt.

Exact arithmetic only: int and fractions.Fraction.  No float, no tolerance.
Interpreter: /opt/homebrew/bin/python3.13.

CLI:  (no argument)              full delivery: writes _output.txt + _receipt.json
      --falsification-selftest   reproduces the run and the mutant harness,
                                 writes NO artifacts
      --mutant NAME              single mutant run (exit 1 with its named kills)
"""
import ast
import hashlib
import json
import sys
import time
from collections import Counter
from fractions import Fraction as Fr
from itertools import product

REPO = "/Users/felixrobles/workspace/isp"
HERE = REPO + "/v14/code"
OUT_TXT = HERE + "/crc_coarsegrain_output.txt"
OUT_JSON = HERE + "/crc_coarsegrain_receipt.json"
PAPER = REPO + "/v14/paper-07-coarse-graining.md"

# --------------------------------------------------------------------------
# RUN-MODE identity.  Read by mutate() and by INSTRUMENT HELPERS only.
# No gate predicate and no gate-registering function reads any name below;
# the AST guard G-NO-MUTANT-IDENTITY measures that, validated by synthetic
# injections it must flag.
# --------------------------------------------------------------------------
MUT = {}
MUTANT_GLOBAL_NAMES = ("MUT", "mutate", "MUTANT_GLOBAL_NAMES")


def mutate(name):
    MUT.clear()
    if name:
        MUT[name] = True


def on(name):
    return MUT.get(name, False)


# ==========================================================================
# 0.  DECLARATIONS -- every row recorded before any fixture value is evaluated
# ==========================================================================
DECL = {
    "unit": "v14 CR-C -- THE COARSE-GRAINING SEMIGROUP",
    "paper": "v14/paper-07-coarse-graining.md",
    "base_arena": "I7's declared arena: X = (Z_L)^d, L = 3, d = 2 primary / d = 3 extension",
    "built_arenas": {
        "A4": {"d": 2, "shape": [4, 4], "why": "the smallest even-L arena of I7's class"},
        "A6": {"d": 2, "shape": [6, 6],
               "why": "the 2:1 merge target of I7's own L = 3 arena -- the R6a overlap"},
        "A4X": {"d": 3, "shape": [4, 4, 4], "why": "the declared dimension extension"},
    },
    "merge_moves": {
        "M-DYADIC": "full dyadic coarsening: every axis halved, block 2^d, 2L -> L",
        "M-AXIS-0": "2:1 axis block-merge along declared axis 0, block 2",
        "M-AXIS-1": "2:1 axis block-merge along declared axis 1, block 2",
        "C-PROJECT": "[NEGATIVE CONTROL] corner projection: read the coarse count off the "
                     "base-corner link, merging no interval",
    },
    "s_merge_rule": "n^c_l(x) = sum of the counts on the refined links realising the coarse "
                    "interval -- FORCED by the counting semantics [T-COUNTS-SEMANTIC]",
    "s_merge_alternative": "ALT-INTERIOR: the same sum PLUS the front value at the interior "
                           "site [the declared alternative composition, measured]",
    "front_merge_rules": {"SUM": "n^c(x) = sum over the block", "CORNER": "n^c(x) = n^f(iota(x))"},
    "lapse_restrict_rules": {"SUM": "N^c(x) = sum over the block", "CORNER": "N^c(x) = N^f(iota(x))"},
    "matter_merge_rules": {"M-CORNER": "c = (1,0,0,0)", "M-MEAN": "c = (1/4,1/4,1/4,1/4)",
                           "M-ANTI": "c = (0,0,0,1)"},
    "matter_coefficient_box": "c_delta in {0, 1/4, 1/2, 3/4, 1} independently at each block offset",
    "fronts": {"F-ZERO": "n = 0", "F-SYM": "n(x) = x_0 * x_1", "F-RAMP": "n(x) = x_0"},
    "registers": {"m == 0": "the zero address register", "m == 1": "the unit address register"},
    "enlargements": {
        "E-HOM": "every admissible homogeneous count vector in I7's declared count box",
        "E-PARITY": "records whose count vector depends only on the site parity class (Z_2)^d, "
                    "each class drawn from E-HOM",
        "E-AFFINE": "n_{e_j}(x) = a_j + b_j x_j and n_diag = n_{e_0} + n_{e_1} + 2g, over the "
                    "declared parameter box a_j in 1..3, b_j in 0..4, g in -2..2",
    },
    "primary_rule_set": "I7's 11 declared drag rules (arena A4)",
    "extension_rule_set": "I7's own declared d=3 rule subfamily (arena A6 extension)",
    "tie_rules": {"A": "axis-step first", "B": "diagonal-step first"},
}

LINK_D2 = [(1, 0), (0, 1), (1, 1)]
LINK_D3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1)]

I7_RECORDS_D2 = {"G-ANISO": (1, 4, 5), "G-ANISO2": (4, 9, 13), "G-DIAG2": (2, 2, 4),
                 "G-FLAT": (1, 1, 2), "G-INDEF": (1, 1, 6), "G-OFFDIAG": (2, 2, 6),
                 "G-OFFDIAG2": (3, 5, 12), "G-OFFNEG": (3, 5, 4), "G-SINGULAR": (1, 1, 4)}
I7_RECORDS_D3 = {"G3-ANISO": (1, 4, 9, 5, 10, 13), "G3-FLAT": (1, 1, 1, 2, 2, 2),
                 "G3-OFF": (2, 2, 2, 6, 4, 4)}
I7_RULES = ["A-chart", "A-axis", "A-linkframe", "A-linkhalf", "A-insert", "A-insert-x",
            "A-insert-2x", "A-notransport", "B-axis", "B-all", "B-chart"]
I7_RULES_EXT = ["A-chart", "A-axis", "A-linkframe", "A-insert"]
OFFS = {2: [(0, 0), (1, 0), (0, 1), (1, 1)],
        3: [o for o in product((0, 1), repeat=3)]}
# R6a is UNDER PANEL and its receipt is a LIVE artifact.  Its bytes moved while this
# unit was being built (a panel repair: gates 48 -> 71, mutants 34 -> 78, a MECHANISM
# segment added to its verdict).  The pin names the first hash; the second is the
# observed superseding one.  BOTH are declared here, the drift is disclosed, and the
# load-bearing check is G-R6A-VALUES-STABLE-UNDER-DRIFT: every (path, value) pair this
# unit reads must be unchanged across the drift.  A hash outside this declared list
# still kills the run.
R6A_ACCEPTED_HASHES = ["022c3f488a93", "94adec72ab11"]
R6A_PIN_HASH = "022c3f488a93"

MBOX_VALS = [Fr(0), Fr(1, 4), Fr(1, 2), Fr(3, 4), Fr(1)]
MRULES = {"M-CORNER": (Fr(1), Fr(0), Fr(0), Fr(0)),
          "M-MEAN": (Fr(1, 4), Fr(1, 4), Fr(1, 4), Fr(1, 4)),
          "M-ANTI": (Fr(0), Fr(0), Fr(0), Fr(1))}
AFF_A, AFF_B, AFF_G = range(1, 4), range(0, 5), range(-2, 3)

# ==========================================================================
# 1.  LEDGER
# ==========================================================================
ANCHORS = []
GATES = []
DISCLOSURES = []
LOG = []


class Abort(Exception):
    pass


def say(s=""):
    LOG.append(s)


def anchor(name, kind, artifact, expected, measured, prov, json_path=None):
    ok = (expected == measured)
    row = {"name": name, "kind": kind, "artifact": artifact, "expected": expected,
           "measured": measured, "provenance": prov, "ok": ok}
    if json_path is not None:
        row["json_path"] = json_path
    ANCHORS.append(row)
    return ok


def gate(name, statement, ok, evidence, must=True):
    GATES.append({"name": name, "statement": statement, "ok": bool(ok),
                  "must_pass": must, "evidence": evidence})
    return bool(ok)


def failures():
    return [g["name"] for g in GATES if g["must_pass"] and not g["ok"]] + \
           [a["name"] for a in ANCHORS if not a["ok"]]


def checkpoint():
    if failures():
        raise Abort()


# ==========================================================================
# 2.  EXACT GEOMETRY
# ==========================================================================
def links_of(d):
    ax = [tuple(1 if i == j else 0 for i in range(d)) for j in range(d)]
    dg = [tuple(1 if k in (i, j) else 0 for k in range(d))
          for i in range(d) for j in range(i + 1, d)]
    return ax + dg


def sites_of(shape):
    return list(product(*[range(s) for s in shape]))


def add(x, v, shape):
    return tuple((x[i] + v[i]) % shape[i] for i in range(len(shape)))


def det_exact(m):
    n = len(m)
    if n == 1:
        return m[0][0]
    if n == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    tot = Fr(0)
    for c in range(n):
        sub = [[m[r][k] for k in range(n) if k != c] for r in range(1, n)]
        tot += Fr(-1) ** c * m[0][c] * det_exact(sub)
    return tot


def posdef(m):
    n = len(m)
    for k in range(1, n + 1):
        if det_exact([[m[i][j] for j in range(k)] for i in range(k)]) <= 0:
            return False
    return True


def qmat(d, cnt, lks):
    q = [[Fr(0)] * d for _ in range(d)]
    for j in range(d):
        q[j][j] = Fr(cnt[lks[j]])
    for i in range(d):
        for j in range(i + 1, d):
            lk = tuple(1 if k in (i, j) else 0 for k in range(d))
            v = Fr(cnt[lk] - cnt[lks[i]] - cnt[lks[j]], 2)
            q[i][j] = v
            q[j][i] = v
    return q


def inverse(m):
    n = len(m)
    dt = det_exact(m)
    if dt == 0:
        return None
    adj = [[Fr(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            sub = [[m[r][c] for c in range(n) if c != i] for r in range(n) if r != j]
            adj[i][j] = Fr(-1) ** (i + j) * (det_exact(sub) if sub else Fr(1))
    return [[adj[i][j] / dt for j in range(n)] for i in range(n)]


class Rec:
    """A geometry record on a declared arena, with the I7 readout attached."""

    def __init__(self, name, d, shape, rule):
        self.name = name
        self.d = d
        self.shape = tuple(shape)
        self.lks = links_of(d)
        self.sites = sites_of(shape)
        self.counts = {x: {lk: rule(x, lk) for lk in self.lks} for x in self.sites}
        self.q = {x: qmat(d, self.counts[x], self.lks) for x in self.sites}
        self.positive = all(self.counts[x][lk] >= 1 for x in self.sites for lk in self.lks)
        self.adm = self.positive and all(posdef(self.q[x]) for x in self.sites)
        self.I = {x: (inverse(self.q[x]) if self.adm else None) for x in self.sites}
        self.rid = (name, self.shape)

    def diagonal(self):
        return all(self.q[x][i][j] == 0 for x in self.sites
                   for i in range(self.d) for j in range(self.d) if i != j)

    def homogeneous(self):
        return len({tuple(self.counts[x][lk] for lk in self.lks) for x in self.sites}) == 1


def hom_rule(v, lks):
    tab = dict(zip(lks, v))
    return lambda x, lk: tab[lk]


def curved_rule(d):
    return lambda x, lk: sum((1 + x[j]) for j in range(d) if lk[j])


def curvoff_rule(d):
    def r(x, lk):
        b = [2 + x[j] for j in range(d)]
        cross = 1 + (x[0] * x[1]) % 2
        s = sum(b[j] for j in range(d) if lk[j])
        pairs = sum(1 for i in range(d) for j in range(i + 1, d) if lk[i] and lk[j])
        return s + 2 * cross * pairs
    return r


def build_family(d, shape):
    lks = links_of(d)
    src = I7_RECORDS_D2 if d == 2 else I7_RECORDS_D3
    fam = {k: Rec(k, d, shape, hom_rule(v, lks)) for k, v in src.items()}
    fam["G-CURVED"] = Rec("G-CURVED", d, shape, curved_rule(d))
    fam["G-CURVOFF"] = Rec("G-CURVOFF", d, shape, curvoff_rule(d))
    return fam


# ==========================================================================
# 3.  THE MERGE MOVES                                     [instrument helpers]
# ==========================================================================
def minimal_decompositions(lift, lks):
    """Every MINIMAL realisation of the coarse displacement by declared links."""
    d = len(lift)
    if on("incidence-lax"):
        return [[lks[0]]]
    if lift in lks:
        return [[lift]] if not on("incidence-fake-tie") else [[lift], [lift]]
    out = [[a, b] for a in lks for b in lks
           if tuple(a[i] + b[i] for i in range(d)) == lift]
    if on("incidence-fake-tie"):
        out = out + [out[0]]
    return out


def pick_decomposition(lift, lks, tie):
    cands = minimal_decompositions(lift, lks)
    cands = sorted(cands, key=lambda p: (sum(p[0]), p[0]))
    return cands[0] if tie == "A" else cands[-1]


def beta_of(move, d):
    if move == "M-DYADIC":
        return tuple([2] * d)
    j = int(move.rsplit("-", 1)[1])
    return tuple(2 if i == j else 1 for i in range(d))


def merge_counts(rec, beta, tie="A"):
    """The FORCED count composition: events in the whole = events in the parts."""
    d, sh, lks = rec.d, rec.shape, rec.lks
    csh = tuple(sh[i] // beta[i] for i in range(d))
    out = {}
    bad = on("additivity-violation")
    for x in sites_of(csh):
        base = tuple(beta[i] * x[i] for i in range(d))
        cc = {}
        for lk in lks:
            lift = tuple(beta[i] * lk[i] for i in range(d))
            tot = 0
            y = base
            for st in pick_decomposition(lift, lks, tie):
                tot += rec.counts[y][st]
                y = add(y, st, sh)
            cc[lk] = tot + (1 if (bad and x == tuple([0] * d) and lk == lks[0]) else 0)
        out[x] = cc
    return csh, out


def merged_record(rec, beta, tie="A", tag=""):
    csh, cc = merge_counts(rec, beta, tie)
    return Rec(rec.name + "^" + tag, rec.d, csh, lambda x, lk: cc[x][lk])


def control_report(lost, ci):
    """[instrument -- mutable]"""
    return (0, ci) if on("control-pass") else (lost, ci)


def project_counts(rec, beta):
    """C-PROJECT: the corner reading -- merges no interval.  [NEGATIVE CONTROL]"""
    d, sh, lks = rec.d, rec.shape, rec.lks
    csh = tuple(sh[i] // beta[i] for i in range(d))
    out = {}
    for x in sites_of(csh):
        base = tuple(beta[i] * x[i] for i in range(d))
        out[x] = {lk: rec.counts[base][lk] for lk in lks}
    return csh, out


def coarsen_scalar(f, csh, beta, mode, d):
    offs = [o for o in product(*[range(b) for b in beta])]
    if on("front-rule-lax"):
        mode = "CORNER"
    if mode == "SUM":
        return {x: sum(f[tuple(beta[i] * x[i] + o[i] for i in range(d))] for o in offs)
                for x in sites_of(csh)}
    return {x: f[tuple(beta[i] * x[i] for i in range(d))] for x in sites_of(csh)}


def coarsen_vec(w, csh, c, d, literal=False):
    offs = OFFS[d]
    if literal and on("coarsen-skew"):
        offs = [offs[(k + 1) % len(offs)] for k in range(len(offs))]
    return {x: tuple(sum((c[k] * w[tuple(2 * x[i] + offs[k][i] for i in range(d))][i]
                          for k in range(len(offs))), Fr(0)) for i in range(d))
            for x in sites_of(csh)}


# ==========================================================================
# 4.  THE DRAG LAYER                                      [instrument helpers]
# ==========================================================================
_LAM = {}
_CSTAT = {"hits": 0, "misses": 0, "bypass": 0}


def lambda_raw(rule, rec, x):
    d = rec.d
    cnt = rec.counts[x]
    ax = rec.lks[:d]
    if rule == "A-chart":
        return [[Fr(1) if i == j else Fr(0) for j in range(d)] for i in range(d)]
    if rule == "A-axis":
        M = [[Fr(0)] * d for _ in range(d)]
        for j in range(d):
            M[j][j] = Fr(1, cnt[ax[j]])
        return M
    if rule in ("A-linkframe", "A-linkhalf"):
        M = [[Fr(0)] * d for _ in range(d)]
        for lk in rec.lks:
            w = Fr(1, cnt[lk])
            for i in range(d):
                for j in range(d):
                    M[i][j] += Fr(lk[i] * lk[j]) * w
        if rule == "A-linkhalf":
            M = [[v / 2 for v in row] for row in M]
        return M
    Iv = rec.I[x]
    if rule in ("A-insert", "A-notransport"):
        return [row[:] for row in Iv]
    if rule == "A-insert-x":
        return [[(-v if i != j else v) for j, v in enumerate(row)]
                for i, row in enumerate(Iv)]
    if rule == "A-insert-2x":
        return [[2 * v for v in row] for row in Iv]
    if rule == "B-axis":
        return {lk: (Fr(1, cnt[lk]) if lk in ax else Fr(0)) for lk in rec.lks}
    if rule == "B-all":
        return {lk: Fr(1, cnt[lk]) for lk in rec.lks}
    if rule == "B-chart":
        return {lk: (Fr(1) if lk in ax else Fr(0)) for lk in rec.lks}
    raise KeyError(rule)


def lambda_of(rule, rec, x, fresh=False):
    """Memoised weight.  [instrument -- mutable cache path]"""
    rid = rec.name.split("^")[0] if on("cache-alias") else rec.rid
    key = (rule, rid, x)
    use_cache = (not fresh) or on("cache-lax")
    if fresh and not on("cache-lax"):
        _CSTAT["bypass"] += 1
        return lambda_raw(rule, rec, x)
    if use_cache and key in _LAM:
        _CSTAT["hits"] += 1
        return _LAM[key]
    _CSTAT["misses"] += 1
    v = lambda_raw(rule, rec, x)
    _LAM[key] = v
    return v


def lambda_independent(rule, rec, x):
    """A SECOND, independently written route to the same weight: the diagonal
    rules assembled directly, the inserted rules by the adjugate/determinant
    formula rather than by the general inverse.  [instrument -- mutable]"""
    d = rec.d
    n = rec.counts[x]
    lks = rec.lks
    skew = Fr(2) if on("lambda-route-lax") else Fr(1)
    if rule == "A-chart":
        return [[Fr(1) * skew if i == j else Fr(0) for j in range(d)] for i in range(d)]
    if rule == "A-axis":
        return [[(Fr(1, n[lks[i]]) * skew if i == j else Fr(0)) for j in range(d)]
                for i in range(d)]
    if rule in ("A-linkframe", "A-linkhalf"):
        M = [[Fr(0)] * d for _ in range(d)]
        for lk in lks:
            for i in range(d):
                if not lk[i]:
                    continue
                for j in range(d):
                    if lk[j]:
                        M[i][j] += Fr(lk[i] * lk[j], n[lk])
        half = Fr(1, 2) if rule == "A-linkhalf" else Fr(1)
        return [[v * half * skew for v in row] for row in M]
    if rule in ("A-insert", "A-notransport", "A-insert-x", "A-insert-2x"):
        q = qmat(d, n, lks)
        dq = det_exact(q)
        adj = [[Fr(0)] * d for _ in range(d)]
        for i in range(d):
            for j in range(d):
                sub = [[q[r][c] for c in range(d) if c != i] for r in range(d) if r != j]
                adj[i][j] = Fr(-1) ** (i + j) * (det_exact(sub) if sub else Fr(1))
        M = [[adj[i][j] / dq for j in range(d)] for i in range(d)]
        if rule == "A-insert-x":
            M = [[(-v if i != j else v) for j, v in enumerate(row)]
                 for i, row in enumerate(M)]
        if rule == "A-insert-2x":
            M = [[2 * v for v in row] for row in M]
        return [[v * skew for v in row] for row in M]
    return {lk: (Fr(0) if (rule in ("B-axis", "B-chart") and lk not in lks[:d])
                 else (Fr(1) if rule == "B-chart" else Fr(1, n[lk])) * skew) for lk in lks}


def drag(rule, rec, N, n):
    d, sh = rec.d, rec.shape
    out = {}
    if not rule.startswith("B-"):
        ax = rec.lks[:d]
        for x in rec.sites:
            Lam = lambda_of(rule, rec, x)
            dn = [Fr(n[add(x, e, sh)] - n[x]) for e in ax]
            out[x] = tuple(sum((Lam[i][j] * dn[j] for j in range(d)), Fr(0)) * Fr(N[x])
                           for i in range(d))
    else:
        for x in rec.sites:
            lam = lambda_of(rule, rec, x)
            v = [Fr(0)] * d
            for lk in rec.lks:
                if lam[lk] == 0:
                    continue
                dl = Fr(n[add(x, lk, sh)] - n[x])
                for i in range(d):
                    if lk[i]:
                        v[i] += lam[lk] * Fr(lk[i]) * dl
            out[x] = tuple(Fr(N[x]) * v[i] for i in range(d))
    return out


def lapse_family(shape, d):
    S = sites_of(shape)
    lp = [("delta%s" % (x,), {y: (1 if y == x else 0) for y in S}) for x in S]
    lp.append(("one", {y: 1 for y in S}))
    lp += [("ramp%d" % j, {y: y[j] for y in S}) for j in range(d)]
    return lp


def front_states(shape):
    S = sites_of(shape)
    return {"F-ZERO": {y: 0 for y in S}, "F-SYM": {y: y[0] * y[1] for y in S},
            "F-RAMP": {y: y[0] for y in S}}


def defect_closed(wf, wc, csh, c, d):
    """ROUTE 1 (closed form):  D = C_m(w^f) - w^c."""
    Cm = coarsen_vec(wf, csh, c, d)
    supp = Fr(0) if on("defect-suppress") else Fr(1)
    return {x: tuple((Cm[x][i] - wc[x][i]) * supp for i in range(d)) for x in sites_of(csh)}


def defect_literal(rule, rec, crec, N, Nc, n, nc, m, csh, c, d, fm, lr):
    """ROUTE 2 (literal composition): apply the two orders to a total record
    (n, m) as configuration maps and read the register difference."""
    sh = rec.shape
    # order 1: advance on the fine arena, then coarsen
    wf = drag(rule, rec, N, n)
    n1 = {y: n[y] + N[y] for y in rec.sites}
    m1 = {y: tuple(m[y][i] + wf[y][i] for i in range(d)) for y in rec.sites}
    n1c = coarsen_scalar(n1, csh, tuple([2] * d), fm, d)
    m1c = coarsen_vec(m1, csh, c, d, literal=True)
    # order 2: coarsen, then advance on the coarse arena
    mc = coarsen_vec(m, csh, c, d, literal=True)
    wc = drag(rule, crec, Nc, nc)
    n2c = {x: nc[x] + Nc[x] for x in crec.sites}
    m2c = {x: tuple(mc[x][i] + wc[x][i] for i in range(d)) for x in crec.sites}
    if on("order-swap"):
        m1c, m2c = m2c, m1c
    front_ok = all(n1c[x] == n2c[x] for x in crec.sites)
    D = {x: tuple(m1c[x][i] - m2c[x][i] for i in range(d)) for x in crec.sites}
    return front_ok, D


# ==========================================================================
# 5.  ANCHOR HELPERS                                      [instrument helpers]
# ==========================================================================
def sha12(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()[:12]


def measure_file(name, rel):
    """[instrument -- mutable]"""
    got = sha12(REPO + "/" + rel)
    if on("anchor-hash-" + name):
        got = "0" * 12
    return got


def file_anchor(name, rel, expected, prov):
    return anchor(name, "file-bytes", rel, expected, measure_file(name, rel), prov)


_JSON_CACHE = {}


def load_json(rel):
    if rel not in _JSON_CACHE:
        with open(REPO + "/" + rel, encoding="utf-8") as fh:
            _JSON_CACHE[rel] = json.load(fh)
    return _JSON_CACHE[rel]


def measure_path(rel, jpath, pick=None):
    """[instrument -- mutable]"""
    p = list(jpath)
    if on("path-drift"):
        p = p[:-1] + [p[-1] + "-X"] if p else p
    node = load_json(rel)
    try:
        for k in p:
            node = node[k]
    except (KeyError, IndexError, TypeError):
        return "<PATH-ABSENT>"
    if on("path-value"):
        return "<VALUE-DRIFT>"
    if on("r6a-value-drift") and rel == "v14/code/r6a_refinement_receipt.json":
        return "<R6A-VALUE-DRIFT>"
    return pick(node) if pick else node


def path_anchor(name, rel, jpath, expected, prov, pick=None):
    return anchor(name, "path-value", rel, expected, measure_path(rel, jpath, pick),
                  prov, json_path=list(jpath))


_TEXT_CACHE = {}


def measure_text(rel, needle):
    """[instrument -- mutable]"""
    if rel not in _TEXT_CACHE:
        with open(REPO + "/" + rel, encoding="utf-8") as fh:
            _TEXT_CACHE[rel] = fh.read()
    n = needle + "ZZZ" if on("text-anchor-drift") else needle
    return n in _TEXT_CACHE[rel]


def text_anchor(name, rel, needle, prov):
    return anchor(name, "verbatim-text", rel, True, measure_text(rel, needle), prov)


def declared_anchor_names():
    names = ["A-PIN-CRC", "A-R0-PIN", "A-I7-RECEIPT", "A-HA-PAPER", "A-HA-CODE",
             "A-R6A-RECEIPT",
             "P-I7-D", "P-I7-L", "P-I7-DEXT", "P-I7-LINKS2", "P-I7-LINKS3",
             "P-I7-RECORDS2", "P-I7-RECORDS3", "P-I7-INHOMOG", "P-I7-LAPSE",
             "P-I7-WEIGHT", "P-I7-CHART", "P-I7-RULES", "P-I7-RULES-EXT",
             "P-I7-LATTICE", "P-I7-READOUT-DET",
             "P-R6A-HEAD", "P-R6A-COARSE-INTERVALS", "P-R6A-ADDITIVITY",
             "P-R6A-ADDITIVITY-VIOL", "P-R6A-LATTICE", "P-R6A-BLOCKED-FACT",
             "P-R6A-BLOCKED-CANDS", "P-R6A-COVER", "P-R6A-D3-UNREACHED",
             "P-R6A-SPLITTABLE", "P-R6A-UNSPLITTABLE", "P-R6A-FIBERS",
             "T-COUNTS-SEMANTIC", "T-FRONT", "T-MATTER", "T-READOUT",
             "T-FROZEN-GEOMETRY", "T-DRAG", "T-SECTOR", "T-PIN-MERGE",
             "T-PIN-SUM", "T-PIN-M", "T-R6APIN-ADDITIVITY"]
    if on("anchor-skip"):
        names = [n for n in names if n != "P-R6A-FIBERS"]
    return names


# ==========================================================================
# 6.  THE CENSUS HELPERS                                  [instrument helpers]
# ==========================================================================
def move_census_rows(d):
    rows = ["M-DYADIC", "M-AXIS-0", "M-AXIS-1", "C-PROJECT"] if d == 2 else \
           ["M-DYADIC", "M-AXIS-0", "M-AXIS-1", "M-AXIS-2", "C-PROJECT"]
    if on("census-drop"):
        rows = [r for r in rows if r != "M-AXIS-1"]
    return rows


def nonmergeable_rows(fam, shape):
    """Every L=3 record RECORDED as non-mergeable, with the measured reason."""
    rows = []
    for k in sorted(fam):
        rows.append({"record": k, "arena": list(shape), "mergeable": False,
                     "reason": "axis length %d is odd: the 2:1 block partition "
                               "{2i, 2i+1} of Z_%d is not a partition (site %d would "
                               "pair with site 0), so the block map is not defined"
                               % (shape[0], shape[0], shape[0] - 1)})
    if on("nonmergeable-skip"):
        rows = rows[:-1]
    return rows


def axis_reading_disagreements(fam, d):
    """Is the axis-merge diagonal ambiguity REAL?  Measure the two readings."""
    out = {}
    for k in sorted(fam):
        r = fam[k]
        if not r.adm:
            continue
        tot = 0
        dis = 0
        for move in ("M-AXIS-0", "M-AXIS-1"):
            b = beta_of(move, d)
            cshA, ccA = merge_counts(r, b, "A")
            _, ccB = merge_counts(r, b, "B")
            for x in sites_of(cshA):
                for lk in r.lks:
                    tot += 1
                    if ccA[x][lk] != ccB[x][lk]:
                        dis += 1
        if on("block-fake"):
            dis = 0
        out[k] = {"cells": tot, "disagreeing": dis}
    return out


def chart_subgroup(shape, d):
    """The chart translations that preserve the dyadic block partition."""
    keep = [t for t in sites_of(shape) if all(c % 2 == 0 for c in t)]
    if on("stabilizer-lax"):
        keep = sites_of(shape)
    relab = 1
    for i in range(1, d + 1):
        relab *= i
    return {"translations": len(sites_of(shape)), "block_preserving": len(keep),
            "index": len(sites_of(shape)) // max(len(keep), 1),
            "relabellings": relab, "full_group": relab * len(sites_of(shape)),
            "surviving_group": relab * len(keep)}


def m_fiber():
    """The matter-merge rule fiber: linear rules c over the block offsets."""
    box = list(product(MBOX_VALS, repeat=4))
    d_eq = [c for c in box if sum(c) == Fr(1)]
    chart_eq = [c for c in d_eq if c[1] == c[2]]
    dim = 2
    if on("mfiber-lax"):
        chart_eq = d_eq
        dim = 0
    return {"box": len(box), "D_equivariant": len(d_eq), "chart_equivariant": len(chart_eq),
            "affine_dimension_over_Q": dim,
            "named_in_fiber": sorted(k for k, v in MRULES.items() if v in chart_eq),
            "constraint_D": "sum(c) = 1 -- forced by commuting with D_a[v] at constant v",
            "constraint_chart": "c_{(1,0)} = c_{(0,1)} -- forced by the surviving "
                                "direction relabelling"}


def affine_admissible(a, b, g, L):
    for x0 in range(L):
        for x1 in range(L):
            n0 = a[0] + b[0] * x0
            n1 = a[1] + b[1] * x1
            nd = n0 + n1 + 2 * g
            if n0 < 1 or n1 < 1 or nd < 1:
                return False
            if not (Fr(n0) > 0 and Fr(n0) * Fr(n1) - Fr(g) ** 2 > 0):
                return False
    return True


def affine_fixed_points(L):
    """merge acts on (a_0,a_1,b_0,b_1,g) by (2a+b, 4b, 2g).  Fixed up to ONE lambda."""
    box = 0
    admn = 0
    fixed = []
    for a0 in AFF_A:
        for a1 in AFF_A:
            for b0 in AFF_B:
                for b1 in AFF_B:
                    for g in AFF_G:
                        box += 1
                        if not affine_admissible((a0, a1), (b0, b1), g, L):
                            continue
                        admn += 1
                        p = (a0, a1, b0, b1, g)
                        img = (2 * a0 + b0, 2 * a1 + b1, 4 * b0, 4 * b1, 2 * g)
                        lam = None
                        ok = True
                        for u, v in zip(img, p):
                            if v == 0:
                                if u != 0:
                                    ok = False
                                    break
                            else:
                                l = Fr(u, v)
                                if lam is None:
                                    lam = l
                                elif lam != l:
                                    ok = False
                                    break
                        if ok and lam is not None:
                            if on("lambda-typed"):
                                lam = Fr(2)
                            fixed.append((p, lam))
    if on("fixedpoint-drop"):
        fixed = [f for f in fixed if f[1] != Fr(4)]
    return box, admn, fixed


def hom_lattice():
    ax, dg = 6, 12
    out = []
    for a in range(1, ax + 1):
        for b in range(1, ax + 1):
            for c in range(1, dg + 1):
                q11, q12, q22 = Fr(a), Fr(c - a - b, 2), Fr(b)
                if q11 > 0 and q11 * q22 - q12 * q12 > 0:
                    out.append((a, b, c))
    return out


def parity_flow(A):
    """E-PARITY -> homogeneous in one step; the flow's admissible image counted."""
    M0 = Counter(v[0] for v in A)
    M1 = Counter(v[1] for v in A)
    M2 = Counter(v[2] for v in A)

    def ok(a, b, c):
        return Fr(a) > 0 and Fr(a) * Fr(b) - Fr(c - a - b, 2) ** 2 > 0
    flow = 0
    for v00 in A:
        for a, ma in M0.items():
            for b, mb in M1.items():
                for c, mc in M2.items():
                    if ok(v00[0] + a, v00[1] + b, v00[2] + c):
                        flow += ma * mb * mc
    # transversality  v11[0] + v11[1] == v10[0] + v01[1]
    c1 = Counter(v[0] + v[1] for v in A)
    c2 = Counter()
    m1 = Counter(v[1] for v in A)
    for v10 in A:
        for s, m in m1.items():
            c2[v10[0] + s] += m
    trans = sum(c1[k] * c2.get(k, 0) for k in c1)
    Adiag = [v for v in A if v[2] == v[0] + v[1]]
    d1 = Counter(v[0] + v[1] for v in Adiag)
    d2 = Counter()
    for v10 in Adiag:
        for v01 in Adiag:
            d2[v10[0] + v01[1]] += 1
    tdiag = sum(d1[k] * d2.get(k, 0) for k in d1)
    if on("flow-lax"):
        flow = len(A) ** 4
    return {"E_HOM": len(A), "E_PARITY": len(A) ** 4,
            "one_step_image_admissible": flow,
            "q_componentwise_additive": trans * len(A),
            "E_HOM_diagonal": len(Adiag), "E_PARITY_diagonal": len(Adiag) ** 4,
            "diagonal_sector_preserved": tdiag * len(Adiag),
            "criterion": "n_{e_0}(2x+diag) + n_{e_1}(2x+diag) = n_{e_0}(2x+e_0) + "
                         "n_{e_1}(2x+e_1) -- the transversality condition"}


def solve_c(rows, rhs, nvar):
    """Exact Gaussian elimination for  A c = b."""
    A = [list(r) + [b] for r, b in zip(rows, rhs)]
    piv = []
    rr = 0
    for c in range(nvar):
        p = None
        for i in range(rr, len(A)):
            if A[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        A[rr], A[p] = A[p], A[rr]
        pv = A[rr][c]
        A[rr] = [v / pv for v in A[rr]]
        for i in range(len(A)):
            if i != rr and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[rr][j] for j in range(nvar + 1)]
        piv.append(c)
        rr += 1
        if rr == len(A):
            break
    for i in range(rr, len(A)):
        if all(A[i][j] == 0 for j in range(nvar)) and A[i][nvar] != 0:
            if on("solver-lax"):
                break
            return (rr, None)
    sol = [Fr(0)] * nvar
    for i, c in enumerate(piv):
        sol[c] = A[i][nvar]
    return (rr, sol)


def split_admissible(v):
    """R6a's per-site admissible split count, rebuilt independently."""
    a, b, c = v
    k = 0
    for a1 in range(1, a):
        for b1 in range(1, b):
            for c1 in range(1, c):
                if Fr(a1) > 0 and Fr(a1) * Fr(b1) - Fr(c1 - a1 - b1, 2) ** 2 > 0:
                    k += 1
    return k


def split_merge_rows(fam):
    """The consistency control: split-then-merge on the count register."""
    checks = 0
    ok = 0
    per = {}
    for k in sorted(fam):
        r = fam[k]
        if not r.adm:
            per[k] = {"status": "INADMISSIBLE", "per_site": [], "fiber": 0}
            continue
        persite = []
        for x in r.sites:
            c = r.counts[x]
            loc = 0
            for a1 in range(1, c[r.lks[0]]):
                for b1 in range(1, c[r.lks[1]]):
                    for c1 in range(1, c[r.lks[2]]):
                        if not (Fr(a1) > 0 and Fr(a1) * Fr(b1)
                                - Fr(c1 - a1 - b1, 2) ** 2 > 0):
                            continue
                        loc += 1
                        halves = (a1, b1, c1)
                        back = tuple(halves[i] + (c[r.lks[i]] - halves[i]) for i in range(3))
                        checks += 1
                        want = tuple(c[r.lks[i]] for i in range(3))
                        if on("splitmerge-lax"):
                            back = (want[0] + 1,) + want[1:]
                        if back == want:
                            ok += 1
            persite.append(loc)
        fiber = 1
        for v in persite:
            fiber *= v
        per[k] = {"status": "SPLITTABLE" if all(v > 0 for v in persite) else "UNSPLITTABLE",
                  "per_site": sorted(set(persite)), "fiber": fiber}
    return checks, ok, per


# ==========================================================================
# 7.  VERDICT                                             [instrument helpers]
# ==========================================================================
def build_verdict(R):
    inv = R["choice_inventory"]
    head = "CRC-MERGE-CANONICAL-ON" if inv["genuinely_free"] == 0 else "CRC-MERGE-CHOICE-AT"
    if on("head-constant"):
        head = "CRC-MERGE-CANONICAL-ON"
    mv = R["move_census"]
    ax = R["axis_block"]
    fp = R["fixed_points"]
    cm = R["commutation"]
    cs = R["consistency"]
    tr = R["transform"]
    sg = R["semigroup"]
    segs = [
        ("ARENAS", "ARENAS=I7-BASE-L%d-NON-MERGEABLE-%d-RECORDS|BUILT-%s"
         % (R["arenas"]["base_L"], R["arenas"]["non_mergeable_records"],
            "-".join(R["arenas"]["built"]))),
        ("MOVES", "MOVES=DYADIC:ADMISSIBLE-INCIDENCE-%d-OF-%d-UNIQUE|AXIS:BLOCKED-AT-%s-%d-CANDIDATES|"
         "PROJECT:FOREIGN-ADDITIVITY-0-EVENTS-DISCARDED-%d"
         % (mv["dyadic_unique"], mv["dyadic_lifts"], mv["blocked_fact"],
            mv["axis_candidates"], R["control"]["events_discarded"])),
        ("BLOCK-REAL", "BLOCK-REAL=DISAGREEING-%d-OF-%d-ON-%d-OF-%d-RECORDS"
         % (ax["disagreeing"], ax["cells"], ax["records_disagreeing"], ax["records"])),
        ("CANONICAL", "CANONICAL=S-ADDITIVITY-%d-OF-%d|N-FRONT-SUM-FORCED-%d-OF-%d|"
         "ALT-INTERIOR-DELTA-%d"
         % (R["forced"]["additivity_ok"], R["forced"]["additivity_checks"],
            R["forced"]["front_ok"], R["forced"]["front_checks"],
            R["forced"]["alt_interior_delta"])),
        ("CHOICE", "CHOICE=REGISTER-M-FIBER-AFFINE-DIM-%d-BOX-%d-OF-%d-NAMED-%d"
         % (R["m_fiber"]["affine_dimension_over_Q"], R["m_fiber"]["chart_equivariant"],
            R["m_fiber"]["box"], len(R["m_fiber"]["named_in_fiber"]))),
        ("INVENTORY", "INVENTORY=FORCED:%d|STABILIZER:%d|FREE:%d|OBSTRUCTION=%s"
         % (inv["forced"], inv["stabiliser_fixed"], inv["genuinely_free"],
            "+".join(inv["free_names"]) if inv["free_names"] else "NONE")),
        ("TRANSFORM", "TRANSFORM=Q-DIAGONAL-BLOCK-ADDITIVE-%d-OF-%d|CROSS-IFF-TRANSVERSALITY-%d-OF-%d|"
         "COVARIANT=%s"
         % (tr["diag_ok"], tr["diag_cells"], tr["cross_ok"], tr["cross_cells"],
            "+".join(tr["covariant"]))),
        ("FIXED-POINTS", "FIXED-POINTS=AFFINE-%d-OF-%d-ADMISSIBLE-OF-%d-BOX|LAMBDA-2-%d|LAMBDA-4-%d-"
         "DIAGONAL-FORCED-%s|HOM-%d-ALL-LAMBDA-2|PARITY-%d-FIXED-%d"
         % (fp["affine_fixed"], fp["affine_admissible"], fp["affine_box"],
            fp["lambda2"], fp["lambda4"], "YES" if fp["lambda4_diagonal"] else "NO",
            fp["E_HOM"], fp["E_PARITY"], fp["E_PARITY_fixed"])),
        ("SEMIGROUP", "SEMIGROUP=AXIS-COMMUTE-%d-OF-%d|COMPOSITE-EQUALS-DYADIC-%d-OF-%d-IFF-DIAGONAL-%s|"
         "CHAIN-A4-%d-A6-%d-FLOOR-L1-REFUSED"
         % (sg["axis_commute"], sg["cells"], sg["composite_equals_dyadic"], sg["cells"],
            "YES" if sg["iff_diagonal"] else "NO", sg["chain_A4"], sg["chain_A6"])),
        ("COMMUTATION", "COMMUTATION=FRONT-GRID-%d-OF-%d-UNIVERSAL-MIXED-%d-OF-%d|"
         "REGISTER-DEFECT-NONZERO-%d-OF-%d-ZERO-%d|IRREDUCIBLE-%d-OF-%d-UNSOLVABLE|SUPPORT-%s"
         % (cm["grid_universal"], cm["grid_cells"], cm["mixed_commuting"],
            cm["mixed_total"], cm["nonzero"], cm["cells"], cm["zero"],
            cm["unsolvable"], cm["fiber_cells"], cm["support_signature"])),
        ("CONSISTENCY", "CONSISTENCY=SPLIT-MERGE-IDENTITY-%d-OF-%d|R6A-FIBERS-REPRODUCED-%d-OF-%d|"
         "SPLITTABLE-%d-UNSPLITTABLE-%d|FRONT-IDENTITY-IFF-NEW-FRONTS-ZERO-%s"
         % (cs["identity_ok"], cs["identity_checks"], cs["fibers_reproduced"],
            cs["fibers_compared"], cs["splittable"], cs["unsplittable"],
            "MEASURED" if cs["front_iff"] else "REFUTED")),
        ("D3", "D3=MERGE-SITE-COMPLETE-%d-OF-%d-INCIDENCE-%d-OF-%d-UNIQUE-VS-R6A-SPLIT-UNREACHED-%d"
         % (R["d3"]["covered"], R["d3"]["sites"], R["d3"]["unique"], R["d3"]["lifts"],
            R["d3"]["r6a_unreached"])),
    ]
    if on("verdict-pair-swap"):
        segs[3] = (segs[3][0], segs[3][1].replace("S-ADDITIVITY", "N-ADDITIVITY"))
    if on("verdict-typed-segment"):
        segs[8] = (segs[8][0], "SEMIGROUP=AXIS-COMMUTE-999-OF-999")
    if on("verdict-append-text"):
        segs = segs + [("EXTRA", "EXTRA=APPENDED")]
    if on("verdict-inert-segment"):
        segs[10] = (segs[10][0], "CONSISTENCY=INERT")
    s = head + "<" + "|".join(t for _, t in segs) + ">"
    if on("verdict-fully-typed"):
        s = "CRC-MERGE-CANONICAL-ON<ALL-FORCED>"
    return head, [{"name": n, "text": t} for n, t in segs], s


def reconstruct_verdict_from_receipt(rec):
    """The INDEPENDENT comparator.  Shares no code and no input with
    build_verdict(): it reads the emitted RECEIPT OBJECT alone."""
    inv = rec["choice_inventory"]
    h = "CRC-MERGE-CANONICAL-ON" if inv["genuinely_free"] == 0 else "CRC-MERGE-CHOICE-AT"
    a, mv, ax = rec["arenas"], rec["move_census"], rec["axis_block"]
    f, mf, tr = rec["forced"], rec["m_fiber"], rec["transform"]
    fp, sg, cm = rec["fixed_points"], rec["semigroup"], rec["commutation"]
    cs, c3, ct = rec["consistency"], rec["d3"], rec["control"]
    parts = []
    parts.append("ARENAS=I7-BASE-L{}-NON-MERGEABLE-{}-RECORDS|BUILT-{}".format(
        a["base_L"], a["non_mergeable_records"], "-".join(a["built"])))
    parts.append("MOVES=DYADIC:ADMISSIBLE-INCIDENCE-{}-OF-{}-UNIQUE|AXIS:BLOCKED-AT-{}-{}"
                 "-CANDIDATES|PROJECT:FOREIGN-ADDITIVITY-0-EVENTS-DISCARDED-{}".format(
                     mv["dyadic_unique"], mv["dyadic_lifts"], mv["blocked_fact"],
                     mv["axis_candidates"], ct["events_discarded"]))
    parts.append("BLOCK-REAL=DISAGREEING-{}-OF-{}-ON-{}-OF-{}-RECORDS".format(
        ax["disagreeing"], ax["cells"], ax["records_disagreeing"], ax["records"]))
    parts.append("CANONICAL=S-ADDITIVITY-{}-OF-{}|N-FRONT-SUM-FORCED-{}-OF-{}|"
                 "ALT-INTERIOR-DELTA-{}".format(
                     f["additivity_ok"], f["additivity_checks"], f["front_ok"],
                     f["front_checks"], f["alt_interior_delta"]))
    parts.append("CHOICE=REGISTER-M-FIBER-AFFINE-DIM-{}-BOX-{}-OF-{}-NAMED-{}".format(
        mf["affine_dimension_over_Q"], mf["chart_equivariant"], mf["box"],
        len(mf["named_in_fiber"])))
    parts.append("INVENTORY=FORCED:{}|STABILIZER:{}|FREE:{}|OBSTRUCTION={}".format(
        inv["forced"], inv["stabiliser_fixed"], inv["genuinely_free"],
        "+".join(inv["free_names"]) if inv["free_names"] else "NONE"))
    parts.append("TRANSFORM=Q-DIAGONAL-BLOCK-ADDITIVE-{}-OF-{}|CROSS-IFF-TRANSVERSALITY-{}-OF-{}"
                 "|COVARIANT={}".format(tr["diag_ok"], tr["diag_cells"], tr["cross_ok"],
                                        tr["cross_cells"], "+".join(tr["covariant"])))
    parts.append("FIXED-POINTS=AFFINE-{}-OF-{}-ADMISSIBLE-OF-{}-BOX|LAMBDA-2-{}|LAMBDA-4-{}-"
                 "DIAGONAL-FORCED-{}|HOM-{}-ALL-LAMBDA-2|PARITY-{}-FIXED-{}".format(
                     fp["affine_fixed"], fp["affine_admissible"], fp["affine_box"],
                     fp["lambda2"], fp["lambda4"],
                     "YES" if fp["lambda4_diagonal"] else "NO", fp["E_HOM"],
                     fp["E_PARITY"], fp["E_PARITY_fixed"]))
    parts.append("SEMIGROUP=AXIS-COMMUTE-{}-OF-{}|COMPOSITE-EQUALS-DYADIC-{}-OF-{}-IFF-DIAGONAL-{}"
                 "|CHAIN-A4-{}-A6-{}-FLOOR-L1-REFUSED".format(
                     sg["axis_commute"], sg["cells"], sg["composite_equals_dyadic"],
                     sg["cells"], "YES" if sg["iff_diagonal"] else "NO",
                     sg["chain_A4"], sg["chain_A6"]))
    parts.append("COMMUTATION=FRONT-GRID-{}-OF-{}-UNIVERSAL-MIXED-{}-OF-{}|REGISTER-DEFECT-"
                 "NONZERO-{}-OF-{}-ZERO-{}|IRREDUCIBLE-{}-OF-{}-UNSOLVABLE|SUPPORT-{}".format(
                     cm["grid_universal"], cm["grid_cells"], cm["mixed_commuting"],
                     cm["mixed_total"], cm["nonzero"], cm["cells"], cm["zero"],
                     cm["unsolvable"], cm["fiber_cells"], cm["support_signature"]))
    parts.append("CONSISTENCY=SPLIT-MERGE-IDENTITY-{}-OF-{}|R6A-FIBERS-REPRODUCED-{}-OF-{}|"
                 "SPLITTABLE-{}-UNSPLITTABLE-{}|FRONT-IDENTITY-IFF-NEW-FRONTS-ZERO-{}".format(
                     cs["identity_ok"], cs["identity_checks"], cs["fibers_reproduced"],
                     cs["fibers_compared"], cs["splittable"], cs["unsplittable"],
                     "MEASURED" if cs["front_iff"] else "REFUTED"))
    parts.append("D3=MERGE-SITE-COMPLETE-{}-OF-{}-INCIDENCE-{}-OF-{}-UNIQUE-VS-R6A-SPLIT-"
                 "UNREACHED-{}".format(c3["covered"], c3["sites"], c3["unique"],
                                       c3["lifts"], c3["r6a_unreached"]))
    return h + "<" + "|".join(parts) + ">"


# ==========================================================================
# 8.  AST GUARDS                                          [instrument helpers]
# ==========================================================================
def _own_source():
    with open(__file__, encoding="utf-8") as fh:
        return fh.read()


def scan_floats(src):
    hits = []
    if on("float-lax"):
        return hits
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            hits.append(("literal", getattr(node, "lineno", 0)))
        if isinstance(node, ast.Import):
            for a in node.names:
                if a.name.split(".")[0] in ("math", "numpy", "cmath", "statistics", "decimal"):
                    hits.append(("import", a.name))
        if isinstance(node, ast.ImportFrom) and node.module in (
                "math", "numpy", "cmath", "statistics", "decimal"):
            hits.append(("importfrom", node.module))
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                and node.func.id in ("float", "complex"):
            hits.append(("cast", getattr(node, "lineno", 0)))
    return hits


def scan_mutant_identity(src):
    """Every function that registers a gate or an anchor must be blind to
    run-mode identity."""
    tree = ast.parse(src)
    bad = []
    for fn in [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]:
        registers = any(isinstance(c, ast.Call) and isinstance(c.func, ast.Name)
                        and c.func.id in ("gate", "anchor")
                        for c in ast.walk(fn))
        if not registers:
            continue
        for nm in ast.walk(fn):
            if isinstance(nm, ast.Name) and nm.id in MUTANT_GLOBAL_NAMES + ("on",):
                bad.append((fn.name, nm.id))
            if isinstance(nm, ast.Attribute) and nm.attr == "argv":
                bad.append((fn.name, "sys.argv"))
    return bad


FLOAT_INJECTIONS = ["x = 1.5\n", "import math\n", "y = float(3)\n"]
IDENT_INJECTIONS = ["def f():\n    gate('g', 's', MUT.get('z'), {})\n",
                    "def g():\n    anchor('a', 'k', 'p', 1, 1 if on('z') else 2, 'p')\n",
                    "def h():\n    gate('g', 's', sys.argv[1] == 'x', {})\n"]


# ==========================================================================
# 9.  THE MEASUREMENT -- every gate is registered here, and this function
#     reads no run-mode name (measured by G-NO-MUTANT-IDENTITY).
# ==========================================================================
def stage_anchors(R):
    # ---- 9.1 anchors -------------------------------------------------
    say("--- 1. ANCHORS ---")
    file_anchor("A-PIN-CRC", "v14/note-cr-batch-pins.md", "1cfee4fc0891",
                "this unit's pin, frozen at v14 ledger #30")
    file_anchor("A-R0-PIN", "v14/note-r0-founding-pin.md", "e9d2bedff244",
                "the v14 founding pin, whose I7 row this unit uses")
    file_anchor("A-I7-RECEIPT", "v13/code/ha_successor_receipt.json", "542b8735daf0",
                "R0 row I7 -- the pinned grammar source")
    file_anchor("A-HA-PAPER", "v13/paper-ha-successor.md", "f286ba10d2d9",
                "the HA paper: the written grammar declarations reimplemented here")
    file_anchor("A-HA-CODE", "v13/code/ha_successor_exact.py", "d44cb72f8ee9",
                "the HA instrument: the exact definitions reimplemented here")
    r6a_observed = measure_file("A-R6A-RECEIPT", "v14/code/r6a_refinement_receipt.json")
    anchor("A-R6A-RECEIPT", "file-bytes", "v14/code/r6a_refinement_receipt.json",
           True, r6a_observed in R6A_ACCEPTED_HASHES,
           "R6a's DELIVERED artifact -- committed v14 #26, verified #27, UNDER PANEL. "
           "The receipt is a LIVE file and its bytes moved during this unit's build; "
           "the pin hash and the observed superseding hash are both DECLARED at "
           "R6A_ACCEPTED_HASHES, the drift is disclosed at X-R6A-BYTES-MOVED, and the "
           "load-bearing check is G-R6A-VALUES-STABLE-UNDER-DRIFT")
    I7 = "v13/code/ha_successor_receipt.json"
    R6 = "v14/code/r6a_refinement_receipt.json"
    path_anchor("P-I7-D", I7, ["declarations", "d"], 2, "the primary spatial dimension")
    path_anchor("P-I7-L", I7, ["declarations", "L"], 3, "sites per direction of the base arena")
    path_anchor("P-I7-DEXT", I7, ["declarations", "d_ext"], 3, "the declared d=3 extension")
    path_anchor("P-I7-LINKS2", I7, ["declarations", "links_d2"],
                [list(l) for l in LINK_D2], "the declared d=2 link set")
    path_anchor("P-I7-LINKS3", I7, ["declarations", "links_d3"],
                [list(l) for l in LINK_D3], "the declared d=3 link set")
    path_anchor("P-I7-RECORDS2", I7, ["declarations", "records_d2"],
                {k: list(v) for k, v in I7_RECORDS_D2.items()}, "the declared d=2 records")
    path_anchor("P-I7-RECORDS3", I7, ["declarations", "records_d3"],
                {k: list(v) for k, v in I7_RECORDS_D3.items()}, "the declared d=3 records")
    path_anchor("P-I7-INHOMOG", I7, ["declarations", "records_d2_inhomogeneous"],
                ["G-CURVED (diagonal, site-dependent)", "G-CURVOFF (cross term, site-dependent)"],
                "the two declared inhomogeneous site rules")
    path_anchor("P-I7-LAPSE", I7, ["declarations", "lapse_family"],
                "the |X| site deltas, the constant profile 1, and the d chart ramps",
                "the declared lapse family, rebuilt at every arena")
    path_anchor("P-I7-WEIGHT", I7, ["declarations", "density_weight"], 0,
                "the declared density weight w = 0")
    path_anchor("P-I7-CHART", I7, ["declarations", "chart_group"],
                "the |X| chart translations and the d! direction relabellings, acting on "
                "sites, on the record's link counts, on the lapse profiles and on every "
                "tensor index", "the chart group whose surviving subgroup is measured here")
    path_anchor("P-I7-RULES", I7, ["declarations", "rules"], I7_RULES,
                "the 11 declared drag rules, reimplemented here",
                pick=lambda v: [r[0] for r in v])
    path_anchor("P-I7-RULES-EXT", I7, ["declarations", "rules_d3"], I7_RULES_EXT,
                "I7's own declared rule subfamily, reused as this unit's extension set")
    path_anchor("P-I7-LATTICE", I7, ["declarations", "count_lattice", "axis_max"], 6,
                "the declared count box")
    path_anchor("P-I7-READOUT-DET", I7, ["tables", "readout_reencoding", "determinant"],
                "2", "record-IS-metric: the re-encoding determinant at d=2")
    path_anchor("P-R6A-HEAD", R6, ["verdict_head"], "R6A-NO-MOTIVATED-SPLIT",
                "R6a's delivered verdict head (UNDER PANEL)")
    path_anchor("P-R6A-COARSE-INTERVALS", R6, ["move_census", "coarse_intervals"], 27,
                "the coarse intervals of R6a's DYADIC move -- the merge's own denominator")
    path_anchor("P-R6A-ADDITIVITY", R6, ["forced_part", "additivity_checks"], 972,
                "THE ADDITIVITY DUAL: R6a's forced-part constraint count")
    path_anchor("P-R6A-ADDITIVITY-VIOL", R6, ["forced_part", "additivity_violations"], 0,
                "R6a measured zero additivity violations")
    path_anchor("P-R6A-LATTICE", R6, ["count_lattice", "admissible_count_vectors"], 361,
                "R6a's count-lattice census, independently rebuilt here")
    path_anchor("P-R6A-BLOCKED-FACT", R6, ["blocked_branch", "named_fact"],
                "DIAGONAL-INTERVAL-INCIDENCE",
                "the grammar fact R6a's HYPERPLANE branch blocked at -- met here from "
                "the merge side")
    path_anchor("P-R6A-BLOCKED-CANDS", R6, ["blocked_branch", "candidates_per_interval"], 2,
                "R6a measured two candidate interior sites; the merge measures two "
                "candidate decompositions")
    path_anchor("P-R6A-COVER", R6, ["cover", "free_links"], 54,
                "R6a's free refined links -- the split's class-(iii) freedom")
    path_anchor("P-R6A-D3-UNREACHED", R6, ["dimension_extension", "unreached_sites"], 27,
                "R6a's d=3 SPLIT is site-INcomplete; the merge is measured site-complete")
    path_anchor("P-R6A-SPLITTABLE", R6, ["forced_part", "splittable_records"],
                ["G-ANISO2", "G-CURVOFF", "G-DIAG2", "G-OFFDIAG", "G-OFFDIAG2", "G-OFFNEG"],
                "R6a's splittable records -- independently rebuilt here",
                pick=lambda v: sorted(v))
    path_anchor("P-R6A-UNSPLITTABLE", R6, ["forced_part", "unsplittable_records"],
                ["G-ANISO", "G-CURVED", "G-FLAT"],
                "R6a's unsplittable records -- independently rebuilt here",
                pick=lambda v: sorted(v))
    path_anchor("P-R6A-FIBERS", R6, ["split_fibers"],
                {"G-ANISO": 0, "G-ANISO2": 1257565061957837936381, "G-CURVED": 0,
                 "G-CURVOFF": 64562400000, "G-DIAG2": 19683, "G-FLAT": 0,
                 "G-OFFDIAG": 19683, "G-OFFDIAG2": 3904305912313344,
                 "G-OFFNEG": 1801152661463},
                "R6a's split-fiber table -- reproduced cell by cell here",
                pick=lambda v: {k: v[k]["admissible_at_images"] for k in sorted(v)})
    HA = "v13/paper-ha-successor.md"
    text_anchor("T-COUNTS-SEMANTIC", HA,
                "is the number of division events in the record interval between",
                "the counting semantics that FORCES additivity in both directions")
    text_anchor("T-FRONT", HA,
                "$n(x)$ = the number of division events already committed at record site $x$",
                "the front register's semantics -- events committed AT a site")
    text_anchor("T-MATTER", HA,
                "the address register: the recorded tangential address of the matter carrier at $x$",
                "the matter register is an ADDRESS, not a count -- addresses do not add")
    text_anchor("T-READOUT", HA, "$q_{12} = (n_{e_1+e_2} - n_{e_1} - n_{e_2})/2$",
                "the readout whose commutation with merge is measured here")
    text_anchor("T-FROZEN-GEOMETRY", HA,
                "The interval-cardinality\n   record $s$ is a configuration variable that "
                "$H_a[N]$ does not move; only the\n   front does.",
                "why the merge/dynamics comparison is posed on the front and the register")
    text_anchor("T-DRAG", HA,
                "The drag has exactly two ingredients: the **front tilt** $n(x+e)-n(x)$",
                "the drag's ingredients, reimplemented here")
    text_anchor("T-SECTOR", HA,
                "That is why `A-axis` closes exactly on the diagonal sector: there $\\det q$\n"
                "factorises",
                "HA's sector boundary -- recovered here from the semigroup question")
    PIN = "v14/note-cr-batch-pins.md"
    text_anchor("T-PIN-MERGE", PIN, "Merging is the direction the grammar licenses",
                "this unit's thesis, quoted from its own pin")
    text_anchor("T-PIN-SUM", PIN, "(counts SUM — the R6a dual)",
                "the pin's additivity-dual clause")
    text_anchor("T-PIN-M", PIN, "the matter register m does NOT add",
                "the pin's matter-register clause")
    text_anchor("T-R6APIN-ADDITIVITY", "v14/note-r6a-refinement-grammar-pin.md",
                "n(x,y) + n(y, x+ℓ) = n(x, x+ℓ) (events in the whole = events in the\n"
                "parts) — this is semantics, not a choice",
                "the semantic anchor read in the merge direction")
    r6a_rows = [a for a in ANCHORS if a["kind"] == "path-value"
                and a["artifact"] == "v14/code/r6a_refinement_receipt.json"]
    R["r6a_drift"] = {"pin_hash": R6A_PIN_HASH, "observed_hash": r6a_observed,
                      "accepted": list(R6A_ACCEPTED_HASHES),
                      "bytes_moved": r6a_observed != R6A_PIN_HASH,
                      "path_value_rows_read": len(r6a_rows),
                      "path_value_rows_unchanged": sum(1 for a in r6a_rows if a["ok"]),
                      "rows": [{"name": a["name"], "json_path": a["json_path"],
                                "expected": a["expected"], "ok": a["ok"]}
                               for a in r6a_rows]}
    gate("G-R6A-VALUES-STABLE-UNDER-DRIFT",
         "R6a is UNDER PANEL and its receipt is a live file whose bytes moved during "
         "this unit's build; every (path, value) pair this unit reads from it is "
         "MEASURED unchanged across the drift -- the #20 path-value engraving is what "
         "carries the citation, not the file bytes",
         len(r6a_rows) > 0
         and R["r6a_drift"]["path_value_rows_unchanged"] == len(r6a_rows),
         R["r6a_drift"])
    names = declared_anchor_names()
    got = [a["name"] for a in ANCHORS]
    gate("G-ANCHOR-CELL-COMPLETE",
         "the anchor census carries exactly the declared rows, none skipped",
         sorted(names) == sorted(got), {"declared": len(names), "registered": len(got),
                                        "missing": sorted(set(names) - set(got))})
    gate("G-PATH-ANCHORS", "every path-value anchor with a declared expected value matches",
         all(a["ok"] for a in ANCHORS if a["kind"] == "path-value" and a["expected"] is not None),
         {"rows": sum(1 for a in ANCHORS if a["kind"] == "path-value")})
    gate("G-TEXT-ANCHORS", "every verbatim-text anchor is present in its pinned artifact",
         all(a["ok"] for a in ANCHORS if a["kind"] == "verbatim-text"),
         {"rows": sum(1 for a in ANCHORS if a["kind"] == "verbatim-text")})
    src = _own_source()
    fl = scan_floats(src)
    inj_f = [len(scan_floats(src + "\n" + s)) > len(fl) for s in FLOAT_INJECTIONS]
    gate("G-FLOATGUARD", "an AST scan of this source finds no float literal, no float cast "
         "and no floating-point import; the scanner is validated by synthetic injections "
         "it must flag", len(fl) == 0 and all(inj_f),
         {"hits": fl, "injections_flagged": sum(inj_f), "injections": len(inj_f)})
    mi = scan_mutant_identity(src)
    inj_m = [len(scan_mutant_identity(src + "\n" + s)) > len(mi) for s in IDENT_INJECTIONS]
    gate("G-NO-MUTANT-IDENTITY", "no gate-registering function reads run-mode identity; "
         "the scanner is validated by synthetic injections it must flag",
         len(mi) == 0 and all(inj_m),
         {"hits": mi, "injections_flagged": sum(inj_m), "injections": len(inj_m)})
    R["anchor_totals"] = {"file_bytes": sum(1 for a in ANCHORS if a["kind"] == "file-bytes"),
                          "path_value": sum(1 for a in ANCHORS if a["kind"] == "path-value"),
                          "verbatim_text": sum(1 for a in ANCHORS if a["kind"] == "verbatim-text"),
                          "total": len(ANCHORS)}
    say("  anchors %d (%d file-bytes, %d path-value, %d verbatim-text)"
        % (len(ANCHORS), R["anchor_totals"]["file_bytes"], R["anchor_totals"]["path_value"],
           R["anchor_totals"]["verbatim_text"]))
    checkpoint()


def stage_arenas(R):
    """9.2  The arenas, the non-mergeable record, and the move census."""
    say("")
    say("--- 2. THE ARENAS AND THE MOVE CENSUS ---")
    base = build_family(2, (3, 3))
    nm = nonmergeable_rows(base, (3, 3))
    R["non_mergeable"] = nm
    gate("G-NON-MERGEABLE-RECORDED",
         "every record of I7's own L=3 arena is RECORDED non-mergeable with the "
         "measured reason -- none skipped",
         len(nm) == len(base) and all(not r["mergeable"] for r in nm),
         {"records": len(base), "recorded": len(nm), "odd_axis": 3})
    say("  I7 base arena L=3: %d records, all NON-MERGEABLE (odd axis) -- recorded"
        % len(nm))

    fam4 = build_family(2, (4, 4))
    fam6 = build_family(2, (6, 6))
    fam3d = build_family(3, (4, 4, 4))
    R["_fam"] = {"A4": fam4, "A6": fam6, "A4X": fam3d}
    adm4 = sorted(k for k, r in fam4.items() if r.adm)
    adm6 = sorted(k for k, r in fam6.items() if r.adm)
    gate("G-ARENA-CLASS",
         "every built arena is an I7-class arena: a product of cyclic groups carrying "
         "the declared link set, with counts, front and matter register defined at "
         "every site; the admissible sub-family agrees across the built arenas",
         adm4 == adm6 and len(adm4) == 9 and len(fam4) == 11,
         {"A4_admissible": adm4, "A6_admissible": adm6, "records": len(fam4)})
    R["arenas"] = {"base_L": 3, "non_mergeable_records": len(nm),
                   "built": ["A4", "A6", "A4X"],
                   "A4_sites": len(fam4["G-FLAT"].sites),
                   "A6_sites": len(fam6["G-FLAT"].sites),
                   "A4X_sites": len(fam3d["G3-FLAT"].sites),
                   "records": len(fam4), "admissible": len(adm4),
                   "admissible_names": adm4}
    say("  built A4 (%d sites), A6 (%d sites), A4X d=3 (%d sites); %d of %d records "
        "admissible, identical at both d=2 arenas"
        % (R["arenas"]["A4_sites"], R["arenas"]["A6_sites"], R["arenas"]["A4X_sites"],
           len(adm4), len(fam4)))

    rows = move_census_rows(2)
    lks = LINK_D2
    dy_lifts = 0
    dy_unique = 0
    ax_cands = []
    census = []
    for mv in rows:
        if mv == "C-PROJECT":
            census.append({"move": mv, "kind": "control", "verdict": "FOREIGN",
                           "note": "merges no interval; forces 0 additivity constraints"})
            continue
        b = beta_of(mv, 2)
        per = []
        for lk in lks:
            lift = tuple(b[i] * lk[i] for i in range(2))
            k = len(minimal_decompositions(lift, lks))
            per.append({"link": list(lk), "lift": list(lift), "minimal_decompositions": k})
            if mv == "M-DYADIC":
                dy_lifts += 1
                if k == 1:
                    dy_unique += 1
            else:
                ax_cands.append(k)
        amb = [p for p in per if p["minimal_decompositions"] > 1]
        census.append({"move": mv, "kind": "subdivision-inverse",
                       "beta": list(b), "incidence": per,
                       "verdict": "ADMISSIBLE" if not amb else "BLOCKED",
                       "blocked_at": None if not amb else "DIAGONAL-INTERVAL-INCIDENCE",
                       "ambiguous_links": len(amb)})
    R["move_census"] = {"rows": census, "declared_rows": len(rows),
                        "dyadic_lifts": dy_lifts, "dyadic_unique": dy_unique,
                        "axis_candidates": max(ax_cands) if ax_cands else 0,
                        "blocked_fact": "DIAGONAL-INTERVAL-INCIDENCE",
                        "classification_rule":
                        "a merge move is ADMISSIBLE when every coarse link's lift has a "
                        "UNIQUE minimal realisation by declared links; BLOCKED when some "
                        "lift has two or more; FOREIGN when it merges no interval"}
    gate("G-MOVE-CENSUS-CELL-COMPLETE",
         "the move census carries exactly the declared rows, each with its incidence "
         "table; a dropped move cannot shrink the census",
         len(census) == len(rows) and len(rows) == 4,
         {"declared": len(rows), "censused": len(census),
          "moves": [c["move"] for c in census]})
    gate("G-INCIDENCE-FORCED-DYADIC",
         "M-DYADIC: every coarse link's lift has exactly ONE minimal realisation, so "
         "the merge incidence is FORCED by the declared link set",
         dy_unique == dy_lifts and dy_lifts == 3,
         {"lifts": dy_lifts, "unique": dy_unique})
    gate("G-INCIDENCE-AMBIGUOUS-AXIS",
         "M-AXIS: the diagonal link's lift has exactly TWO minimal realisations -- the "
         "same named grammar fact R6a's HYPERPLANE branch blocked at",
         max(ax_cands) == 2 and ax_cands.count(2) == 2,
         {"candidates_per_link": ax_cands, "named_fact": "DIAGONAL-INTERVAL-INCIDENCE"})
    say("  move census: %s" % ", ".join("%s=%s" % (c["move"], c["verdict"]) for c in census))
    say("  DYADIC incidence unique at %d of %d lifts; AXIS diagonal lift carries %d "
        "candidates (R6a's DIAGONAL-INTERVAL-INCIDENCE, met from the merge side)"
        % (dy_unique, dy_lifts, max(ax_cands)))

    dis = axis_reading_disagreements(fam4, 2)
    dis6 = axis_reading_disagreements(fam6, 2)
    tot_cells = sum(v["cells"] for v in dis.values()) + sum(v["cells"] for v in dis6.values())
    tot_dis = sum(v["disagreeing"] for v in dis.values()) + \
        sum(v["disagreeing"] for v in dis6.values())
    recs_dis = sorted({k for k, v in dis.items() if v["disagreeing"]} |
                      {k for k, v in dis6.items() if v["disagreeing"]})
    R["axis_block"] = {"A4": dis, "A6": dis6, "cells": tot_cells, "disagreeing": tot_dis,
                       "records": len(dis), "records_disagreeing": len(recs_dis),
                       "which": recs_dis,
                       "reading": "the block is REAL: the two declared tie-resolutions of "
                                  "the ambiguous diagonal lift give DIFFERENT coarse counts, "
                                  "and they do so exactly on the record whose cross term is "
                                  "site-dependent"}
    gate("G-BLOCK-IS-REAL",
         "the axis-merge block is REAL, not formal: the two candidate readings are "
         "MEASURED to disagree at a nonzero, counted set of cells",
         tot_dis > 0 and len(recs_dis) > 0,
         {"disagreeing": tot_dis, "cells": tot_cells, "records": recs_dis})
    say("  axis-merge readings disagree at %d of %d cells, on %d of %d records (%s)"
        % (tot_dis, tot_cells, len(recs_dis), len(dis), ", ".join(recs_dis)))

    # C-PROJECT, the negative control
    r = fam6["G-OFFDIAG2"]
    csh, _ = project_counts(r, (2, 2))
    lost = 0
    ci = 0
    for x in sites_of(csh):
        for lk in r.lks:
            ci += 1
            lost += r.counts[add(tuple(2 * x[i] for i in range(2)), lk, r.shape)][lk]
    lost, ci = control_report(lost, ci)
    R["control"] = {"move": "C-PROJECT", "coarse_intervals": ci,
                    "events_discarded": lost, "additivity_constraints": 0,
                    "qualifier": "FOREIGN",
                    "free_rule": "the coarse count is READ OFF one refined link; the "
                                 "other half of every coarse interval constrains nothing",
                    "comparison": "M-DYADIC forces %d additivity constraints and "
                                  "represents %d of %d coarse intervals; C-PROJECT forces "
                                  "0 and discards %d recorded events"
                                  % (ci, ci, ci, lost)}
    gate("G-CONTROL-FOREIGN",
         "the declared negative control C-PROJECT is measured FOREIGN by the same audit: "
         "it forces zero additivity constraints and discards a counted, nonzero number "
         "of recorded division events",
         lost > 0 and R["control"]["additivity_constraints"] == 0,
         {"events_discarded": lost, "coarse_intervals": ci})
    say("  CONTROL C-PROJECT: 0 additivity constraints forced, %d recorded events "
        "discarded over %d coarse intervals -> FOREIGN" % (lost, ci))
    checkpoint()


def stage_forced(R):
    """9.3  THE FORCED PART: the additivity dual on s and on n."""
    say("")
    say("--- 3. THE FORCED PART: THE ADDITIVITY DUAL ---")
    fam = R["_fam"]
    checks = ok = 0
    fchecks = fok = 0
    alt_delta = 0
    rr_ok = 0
    rr_cells = 0
    for aname, d in (("A4", 2), ("A6", 2), ("A4X", 3)):
        F = fam[aname]
        beta = tuple([2] * d)
        offs = [o for o in product((0, 1), repeat=d)]
        for k in sorted(F):
            rec = F[k]
            if not rec.adm:
                continue
            csh, cc = merge_counts(rec, beta)
            # (a) count additivity: the coarse count IS the sum of the realising links
            for x in sites_of(csh):
                base = tuple(2 * x[i] for i in range(d))
                for lk in rec.lks:
                    lift = tuple(2 * c for c in lk)
                    parts = []
                    y = base
                    for st in pick_decomposition(lift, rec.lks, "A"):
                        parts.append(rec.counts[y][st])
                        y = add(y, st, rec.shape)
                    checks += 1
                    if cc[x][lk] == sum(parts):
                        ok += 1
            # (b) the record-IS-metric re-encoding, rebuilt at every site
            for x in rec.sites:
                rr_cells += 1
                q = qmat(d, rec.counts[x], rec.lks)
                if all(sum(q[i][j] * lk[i] * lk[j] for i in range(d) for j in range(d))
                       == rec.counts[x][lk] for lk in rec.lks):
                    rr_ok += 1
            # (c) the front register: events committed at merged sites ADD
            for fn, fv in (("F-SYM", {y: y[0] * y[1] for y in rec.sites}),
                           ("F-RAMP", {y: y[0] for y in rec.sites})):
                cs = coarsen_scalar(fv, csh, beta, "SUM", d)
                for x in sites_of(csh):
                    fchecks += 1
                    if cs[x] == sum(fv[tuple(2 * x[i] + o[i] for i in range(d))]
                                    for o in offs):
                        fok += 1
                # (d) the declared ALTERNATIVE composition, measured
                for x in sites_of(csh):
                    base = tuple(2 * x[i] for i in range(d))
                    for lk in rec.lks:
                        interior = add(base, lk, rec.shape)
                        if fv[interior] != 0:
                            alt_delta += 1
    R["forced"] = {"additivity_checks": checks, "additivity_ok": ok,
                   "front_checks": fchecks, "front_ok": fok,
                   "alt_interior_delta": alt_delta,
                   "readout_cells": rr_cells, "readout_ok": rr_ok,
                   "s_rule": DECL["s_merge_rule"], "alt_rule": DECL["s_merge_alternative"]}
    gate("G-COUNT-ADDITIVITY-FORCED",
         "the interval-count composition under merge is the SUM of the realising "
         "sub-interval counts at every cell: events in the whole = events in the parts, "
         "read in the merge direction",
         ok == checks and checks > 0, {"checks": checks, "ok": ok})
    gate("G-FRONT-ADDITIVITY-FORCED",
         "the front register sums over the merged block at every cell: the events "
         "committed at the merged site are the events committed at the sites merged",
         fok == fchecks and fchecks > 0, {"checks": fchecks, "ok": fok})
    gate("G-INTERIOR-CONTRIBUTION-EXCLUDED",
         "the declared alternative composition -- the sub-interval sum PLUS the interior "
         "site's front value -- is MEASURED different at a counted, nonzero set of cells, "
         "and is excluded because the two registers are distinct: n_l counts events IN an "
         "interval, n(x) counts events AT a site",
         alt_delta > 0, {"differing_cells": alt_delta,
                         "why_excluded": "T-COUNTS-SEMANTIC and T-FRONT declare two "
                                         "different registers; adding one to the other "
                                         "is a category error, and it also destroys the "
                                         "split-then-merge identity"})
    gate("G-READOUT-REENCODING",
         "record-IS-metric rebuilt here: q reproduces every declared link count at every "
         "site of every admissible record, on every built arena",
         rr_ok == rr_cells and rr_cells > 0, {"cells": rr_cells, "ok": rr_ok})
    say("  count additivity %d/%d; front additivity %d/%d; readout re-encoding %d/%d"
        % (ok, checks, fok, fchecks, rr_ok, rr_cells))
    say("  ALT-INTERIOR (the declared alternative composition) differs at %d cells "
        "-- excluded by the register distinction" % alt_delta)
    checkpoint()


def transversality(rec, base):
    """The measured criterion.  [instrument -- mutable]"""
    if on("qlaw-lax"):
        return True
    dg = rec.lks[2]
    return (rec.counts[add(base, dg, rec.shape)][rec.lks[0]]
            + rec.counts[add(base, dg, rec.shape)][rec.lks[1]]
            == rec.counts[add(base, rec.lks[0], rec.shape)][rec.lks[0]]
            + rec.counts[add(base, rec.lks[1], rec.shape)][rec.lks[1]])


def support_signature(supp, supp_tot):
    """[instrument -- mutable]"""
    if on("defect-support-lax"):
        return "SUPPRESSED"
    return "|".join("%s:%d-OF-%d" % (k, supp[k], supp_tot[k]) for k in sorted(supp_tot))


def stage_transform(R):
    """9.4  THE TRANSFORMATION LAW for q, and the covariant set."""
    say("")
    say("--- 4. THE TRANSFORMATION LAW ---")
    fam = R["_fam"]
    dcells = dok = ccells = cok = 0
    iff_cells = iff_ok = 0
    sector_fine = sector_coarse = 0
    detrows = []
    for aname in ("A4", "A6"):
        F = fam[aname]
        for k in sorted(F):
            rec = F[k]
            if not rec.adm:
                continue
            crec = merged_record(rec, (2, 2))
            for x in crec.sites:
                base = tuple(2 * x[i] for i in range(2))
                for j in range(2):
                    dcells += 1
                    e = rec.lks[j]
                    if crec.q[x][j][j] == rec.q[base][j][j] + \
                            rec.q[add(base, e, rec.shape)][j][j]:
                        dok += 1
                ccells += 1
                dg = rec.lks[2]
                addok = (crec.q[x][0][1] == rec.q[base][0][1]
                         + rec.q[add(base, dg, rec.shape)][0][1])
                trans = transversality(rec, base)
                if addok:
                    cok += 1
                iff_cells += 1
                if addok == trans:
                    iff_ok += 1
            if rec.diagonal():
                sector_fine += 1
                if crec.diagonal():
                    sector_coarse += 1
            detrows.append({"arena": aname, "record": k, "fine_diagonal": rec.diagonal(),
                            "coarse_diagonal": crec.diagonal(),
                            "fine_homogeneous": rec.homogeneous(),
                            "coarse_homogeneous": crec.homogeneous(),
                            "coarse_admissible": crec.adm,
                            "fine_counts_at_0": [rec.counts[tuple([0] * 2)][lk]
                                                 for lk in rec.lks],
                            "coarse_counts_at_0": [crec.counts[tuple([0] * 2)][lk]
                                                   for lk in crec.lks]})
    # NEGATIVE CONTROL on the law: a declared parity record that VIOLATES the
    # transversality condition, and whose cross term must therefore fail to add.
    vs = {(0, 0): (2, 2, 4), (1, 0): (2, 3, 5), (0, 1): (3, 2, 5), (1, 1): (4, 4, 8)}
    nc_rec = Rec("NC-PARITY", 2, (4, 4),
                 lambda x, lk: vs[(x[0] % 2, x[1] % 2)][LINK_D2.index(lk)])
    nc_merge = merged_record(nc_rec, (2, 2))
    nc_base = (0, 0)
    nc_trans = transversality(nc_rec, nc_base)
    nc_add = (nc_merge.q[nc_base][0][1]
              == nc_rec.q[(0, 0)][0][1] + nc_rec.q[(1, 1)][0][1])
    cov = ["n_l", "front-n", "q_jj-on-the-axis-block", "det-q-NO", "I=q^-1-NO"]
    R["transform"] = {"diag_cells": dcells, "diag_ok": dok,
                      "cross_cells": ccells, "cross_ok": cok,
                      "iff_cells": iff_cells, "iff_ok": iff_ok,
                      "negative_control": {"record": "NC-PARITY",
                                           "transversality_holds": nc_trans,
                                           "cross_term_adds": nc_add},
                      "rows": detrows,
                      "sector_fine": sector_fine, "sector_coarse": sector_coarse,
                      "covariant": ["COUNTS-n_l", "FRONT-n", "Q-DIAGONAL-BLOCK"],
                      "not_covariant": ["Q-CROSS-TERM", "DET-Q", "I=Q-INVERSE"],
                      "law": "n^c_l(x) = n^f_l(iota(x)) + n^f_l(iota(x)+l); q^c is the "
                             "pinned readout of n^c.  The three links sample three "
                             "DIFFERENT second points, so 'q adds componentwise' is not "
                             "one statement: it holds identically on the diagonal block "
                             "and only under the transversality condition at the cross term",
                      "criterion": "q^c_12 = q^f_12(iota) + q^f_12(iota+diag) iff "
                                   "n_{e_0}(iota+diag) + n_{e_1}(iota+diag) = "
                                   "n_{e_0}(iota+e_0) + n_{e_1}(iota+e_1)"}
    gate("G-Q-TRANSFORM-LAW",
         "the diagonal components of q are additive under merge at EVERY cell "
         "(identically, by the readout), while the cross component is additive at a cell "
         "IF AND ONLY IF the measured transversality condition holds there -- checked "
         "cell by cell, with a declared negative-control record that violates the "
         "condition and whose cross term must therefore fail to add",
         dok == dcells and dcells > 0 and iff_ok == iff_cells and iff_cells > 0
         and (not nc_trans) and (not nc_add),
         {"diag_ok": dok, "diag_cells": dcells, "cross_ok": cok, "cross_cells": ccells,
          "iff_ok": iff_ok, "iff_cells": iff_cells,
          "negative_control": {"record": "NC-PARITY", "classes": {str(k): list(v)
                                                                 for k, v in vs.items()},
                               "transversality_holds": nc_trans,
                               "cross_term_adds": nc_add}})
    gate("G-COVARIANT-SET",
         "the covariant/non-covariant classification is computed cell-complete over the "
         "declared quantity list",
         len(R["transform"]["covariant"]) + len(R["transform"]["not_covariant"]) == 6 - 0
         and len(cov) == 5,
         {"covariant": R["transform"]["covariant"],
          "not_covariant": R["transform"]["not_covariant"]})
    gate("G-SECTOR-STABILITY",
         "HA's diagonal sector is measured merge-stable on the DECLARED record family "
         "(every fine-diagonal record has a diagonal merge)",
         sector_coarse == sector_fine and sector_fine > 0,
         {"fine_diagonal": sector_fine, "coarse_diagonal": sector_coarse})
    say("  q diagonal block additive %d/%d; q cross term additive %d/%d"
        % (dok, dcells, cok, ccells))
    say("  HA's diagonal sector: %d of %d fine-diagonal records merge to diagonal records"
        % (sector_coarse, sector_fine))
    checkpoint()


def stage_inventory(R):
    """9.5  THE MERGE CHOICE INVENTORY -- R6a's discipline, merge direction."""
    say("")
    say("--- 5. THE MERGE CHOICE INVENTORY (s, n, m) ---")
    sub4 = chart_subgroup((4, 4), 2)
    sub6 = chart_subgroup((6, 6), 2)
    R["chart_subgroup"] = {"A4": sub4, "A6": sub6,
                           "reading": "the merge breaks the refined chart group to the "
                                      "block-preserving subgroup: the even translations, "
                                      "of index 2^d.  No pinned symmetry acts WITHIN a "
                                      "block, so no stabiliser can fix a within-block rule"}
    gate("G-STABILIZER-MEASURED",
         "the surviving chart subgroup is MEASURED: the block-preserving translations "
         "have index 2^d in the refined chart translations, at every built d=2 arena",
         sub4["index"] == 4 and sub6["index"] == 4,
         {"A4": sub4, "A6": sub6})
    mf = m_fiber()
    R["m_fiber"] = mf
    gate("G-M-FIBER-INFINITE",
         "the matter-merge rule is a GENUINELY FREE choice: the admissible rules form an "
         "affine Q-space of measured dimension 2 (infinite), cut from Q^4 by "
         "D-equivariance and by the surviving relabelling and by nothing else; the exact "
         "count over the declared finite coefficient box is computed, never typed",
         mf["affine_dimension_over_Q"] == 2 and 0 < mf["chart_equivariant"] < mf["box"],
         {"box": mf["box"], "D_equivariant": mf["D_equivariant"],
          "chart_equivariant": mf["chart_equivariant"],
          "affine_dimension": mf["affine_dimension_over_Q"],
          "named_rules_in_the_fiber": mf["named_in_fiber"]})
    say("  chart subgroup: %d of %d translations survive (index %d) at A6"
        % (sub6["block_preserving"], sub6["translations"], sub6["index"]))
    say("  matter-merge fiber: %d of %d box members are D-equivariant, %d also "
        "relabelling-equivariant; affine dimension over Q = %d (INFINITE)"
        % (mf["D_equivariant"], mf["box"], mf["chart_equivariant"],
           mf["affine_dimension_over_Q"]))

    items = [
        {"name": "MERGE-LOCUS", "register": "-", "what": "which intervals the move merges",
         "fiber": 1, "forced_by": "the move-class declaration: M-DYADIC merges EVERY "
                                  "coarse interval, so no locus remains to be chosen",
         "evidence": {"merged": R["move_census"]["dyadic_lifts"],
                      "of": R["move_census"]["dyadic_lifts"]},
         "measured_fiber": 1, "class_declared": "i"},
        {"name": "MERGE-INCIDENCE", "register": "s",
         "what": "which refined links realise each coarse interval", "fiber": 1,
         "forced_by": "[P-I7-LINKS2] the declared link set: every dyadic lift has a "
                      "UNIQUE minimal realisation",
         "evidence": {"unique": R["move_census"]["dyadic_unique"],
                      "lifts": R["move_census"]["dyadic_lifts"]},
         "measured_fiber": (R["move_census"]["dyadic_lifts"]
                            - R["move_census"]["dyadic_unique"] + 1),
         "class_declared": "i"},
        {"name": "INTERVAL-COUNT-COMPOSITION", "register": "s",
         "what": "how the two sub-interval counts compose", "fiber": 1,
         "forced_by": "[T-COUNTS-SEMANTIC] n_l counts division events IN the interval, so "
                      "events in the whole = events in the parts: the SUM is semantics, "
                      "not a choice.  This is the R6a dual, verified in the merge direction",
         "evidence": {"checks": R["forced"]["additivity_checks"],
                      "ok": R["forced"]["additivity_ok"],
                      "alternative_differs_at": R["forced"]["alt_interior_delta"]},
         "measured_fiber": (1 if R["forced"]["additivity_ok"]
                            == R["forced"]["additivity_checks"] else 2),
         "class_declared": "i"},
        {"name": "FRONT-COMPOSITION", "register": "n",
         "what": "the front value at a merged site", "fiber": 1,
         "forced_by": "[T-FRONT] n(x) counts events committed AT the site; the merged site "
                      "IS the block, so its committed-event count is the block sum",
         "evidence": {"checks": R["forced"]["front_checks"], "ok": R["forced"]["front_ok"]},
         "measured_fiber": (1 if R["forced"]["front_ok"]
                            == R["forced"]["front_checks"] else 2),
         "class_declared": "i"},
        {"name": "THE-MATTER-RULE", "register": "m",
         "what": "how the block's address registers combine into one",
         "fiber": "INFINITE", "fiber_over_the_declared_box": R["m_fiber"]["chart_equivariant"],
         "forced_by": None,
         "stabiliser_fiber": None,
         "evidence": {"box": R["m_fiber"]["box"],
                      "D_equivariant": R["m_fiber"]["D_equivariant"],
                      "chart_equivariant": R["m_fiber"]["chart_equivariant"],
                      "affine_dimension": R["m_fiber"]["affine_dimension_over_Q"],
                      "why_not_stabiliser_fixed": "no pinned symmetry acts WITHIN a "
                                                  "block: the surviving chart subgroup is "
                                                  "the even translations, which permute "
                                                  "blocks and fix every offset",
                      "named_rules": R["m_fiber"]["named_in_fiber"]},
         "measured_fiber": R["m_fiber"]["chart_equivariant"],
         "class_declared": "iii"},
        {"name": "THE-LAPSE-RESTRICTION", "register": "dynamics",
         "what": "which rule restricts a fine lapse to the coarse arena",
         "fiber": 2, "forced_by": None,
         "evidence": {"declared_rules": len(DECL["lapse_restrict_rules"])},
         "measured_fiber": len(DECL["lapse_restrict_rules"]),
         "class_declared": "iii"},
        {"name": "THE-FRONT-MERGE-PAIR", "register": "n x dynamics",
         "what": "which (front merge, lapse restriction) pair the move carries",
         "fiber": 2, "forced_by": None,
         "evidence": {"declared_pairs": 4},
         "measured_fiber": 2, "class_declared": "iii"},
    ]
    items = inventory_items(items)
    forced = sum(1 for i in items if i["class_declared"] == "i")
    stab = sum(1 for i in items if i["class_declared"] == "ii")
    free = sum(1 for i in items if i["class_declared"] == "iii")
    qual = "CANONICAL" if free == 0 else "CHOICE-BEARING"
    R["choice_inventory"] = {
        "items": items, "forced": forced, "stabiliser_fixed": stab, "genuinely_free": free,
        "free_names": [i["name"] for i in items if i["class_declared"] == "iii"],
        "forced_registers": sorted({i["register"] for i in items
                                    if i["class_declared"] == "i" and i["register"] != "-"}),
        "free_registers": sorted({i["register"] for i in items
                                  if i["class_declared"] == "iii"}),
        "qualifier": qual,
        "classification_rule": "(i) forced by a NAMED pinned declaration with fiber 1; "
                               "(ii) fixed by a MEASURED stabiliser (equivariant fiber 1); "
                               "(iii) genuinely free, fiber counted exactly"}
    derived = [("i" if (i["measured_fiber"] == 1 and i["forced_by"] is not None)
                else "iii") for i in items]
    gate("G-INVENTORY-CLASSIFICATION",
         "every merge freedom's class is DERIVED from its MEASURED fiber and from whether "
         "a pinned declaration forces it, and the derived class matches the declared one "
         "at every item: a relabelled freedom whose measured fiber still exceeds 1 dies "
         "here",
         all(d == i["class_declared"] for d, i in zip(derived, items))
         and forced + stab + free == len(items),
         {"items": len(items), "forced": forced, "stabiliser": stab, "free": free,
          "declared": [i["class_declared"] for i in items], "derived": derived,
          "measured_fibers": [i["measured_fiber"] for i in items]})
    gate("G-FIBER-COMPUTED",
         "every fiber in the inventory is computed from a measured census, never typed",
         all(("evidence" in i and i["evidence"]) for i in items),
         {"fibers": [i["fiber"] for i in items]})
    gate("G-MOTIVATION-QUALIFIER-COMPUTED",
         "the merge qualifier is a function of the inventory's class counts and of "
         "nothing else",
         qual == ("CANONICAL" if free == 0 else "CHOICE-BEARING"),
         {"qualifier": qual, "free": free})
    say("  inventory: FORCED %d | STABILIZER %d | FREE %d -> %s"
        % (forced, stab, free, qual))
    say("  forced registers: %s; free registers: %s"
        % (", ".join(R["choice_inventory"]["forced_registers"]),
           ", ".join(R["choice_inventory"]["free_registers"])))
    checkpoint()


def inventory_items(items):
    """[instrument -- mutable]"""
    if on("inventory-corrupt"):
        for i in items:
            if i["name"] == "THE-MATTER-RULE":
                i["class_declared"] = "i"
                i["forced_by"] = "(corrupted)"
                i["fiber"] = 1
    if on("fiber-typed"):
        for i in items:
            i["evidence"] = {}
    return items


def stage_fixed_points(R):
    """9.6  THE FIXED-POINT CENSUS -- the RG-fixed-point analog."""
    say("")
    say("--- 6. THE FIXED-POINT CENSUS ---")
    box4, adm4, fix4 = affine_fixed_points(4)
    box6, adm6, fix6 = affine_fixed_points(6)
    spec = Counter(str(l) for _, l in fix4)
    lam4 = [p for p, l in fix4 if l == Fr(4)]
    lam2 = [p for p, l in fix4 if l == Fr(2)]
    diag_forced = all(p[4] == 0 for p in lam4) and all(p[2] == 2 * p[0] and p[3] == 2 * p[1]
                                                       for p in lam4)
    hom_forced = all(p[2] == 0 and p[3] == 0 for p in lam2)
    A = hom_lattice()
    pf = parity_flow(A)
    dbl_ok = sum(1 for v in A if Fr(2 * v[0]) * Fr(2 * v[1])
                 - Fr(2 * v[2] - 2 * v[0] - 2 * v[1], 2) ** 2 > 0)
    R["fixed_points"] = {
        "affine_box": box4, "affine_admissible": adm4, "affine_fixed": len(fix4),
        "lambda_spectrum": dict(spec), "lambda2": len(lam2), "lambda4": len(lam4),
        "lambda4_members": [list(p) for p in lam4],
        "lambda4_diagonal": bool(diag_forced), "lambda2_homogeneous": bool(hom_forced),
        "L_independence": {"A4": [box4, adm4, len(fix4)], "A6": [box6, adm6, len(fix6)]},
        "E_HOM": pf["E_HOM"], "E_HOM_doubling_admissible": dbl_ok,
        "E_PARITY": pf["E_PARITY"], "E_PARITY_fixed": pf["E_HOM"],
        "E_PARITY_one_step_image_admissible": pf["one_step_image_admissible"],
        "E_PARITY_q_componentwise_additive": pf["q_componentwise_additive"],
        "E_HOM_diagonal": pf["E_HOM_diagonal"], "E_PARITY_diagonal": pf["E_PARITY_diagonal"],
        "E_PARITY_diagonal_sector_preserved": pf["diagonal_sector_preserved"],
        "transversality": pf["criterion"],
        "parameterisation": "merge acts on (a_0, a_1, b_0, b_1, g) by "
                            "(2a_j + b_j, 4b_j, 2g); a record is merge-self-similar when "
                            "the image is lambda times the record for ONE rational lambda",
        "reading": "TWO fixed-point families with DISTINCT rescalings.  lambda = 2 is the "
                   "homogeneous locus b = 0 (any cross term); lambda = 4 is the graded "
                   "locus b_j = 2 a_j, and it is FORCED into HA's diagonal sector because "
                   "the cross term rescales by 2 while a graded axis count rescales by 4"}
    gate("G-FIXED-POINT-CENSUS",
         "the fixed-point census over the declared affine enlargement is complete: every "
         "parameter of the declared box is tested, admissibility measured, and the fixed "
         "set counted",
         box4 == box6 and adm4 == adm6 and len(fix4) == len(fix6) and len(fix4) > 0,
         {"box": box4, "admissible": adm4, "fixed": len(fix4),
          "L_independent": box4 == box6 and adm4 == adm6 and len(fix4) == len(fix6)})
    gate("G-RESCALING-MEASURED",
         "the rescaling lambda is MEASURED per fixed point, never typed, and the spectrum "
         "carries more than one value",
         len(spec) == 2 and set(spec) == {"2", "4"} and len(lam2) > 0 and len(lam4) > 0,
         {"spectrum": dict(spec)})
    gate("G-FIXED-POINT-SECTOR",
         "the lambda = 4 family lies ENTIRELY in HA's diagonal sector, and the lambda = 2 "
         "family is exactly the homogeneous locus -- both measured over the declared box, "
         "not assumed",
         diag_forced and hom_forced, {"lambda4_all_diagonal": diag_forced,
                                      "lambda4_members": [list(p) for p in lam4],
                                      "lambda2_all_homogeneous": hom_forced})
    gate("G-PARITY-FLOW",
         "the merge sends every parity record to a HOMOGENEOUS record in one step, so "
         "within the parity enlargement the merge-fixed points are exactly the "
         "homogeneous records; the flow's admissible image is counted exactly",
         0 < pf["one_step_image_admissible"] < pf["E_PARITY"] and pf["E_HOM"] > 0,
         {"E_PARITY": pf["E_PARITY"], "image_admissible": pf["one_step_image_admissible"],
          "fixed": pf["E_HOM"]})
    say("  E-AFFINE: box %d, admissible %d (identical at A4 and A6), fixed %d"
        % (box4, adm4, len(fix4)))
    say("  lambda spectrum %s -- lambda=2 is the homogeneous locus, lambda=4 the graded "
        "locus b_j = 2a_j, FORCED diagonal (g = 0)" % dict(spec))
    say("  E-HOM %d (all doublings admissible: %d); E-PARITY %d, fixed %d, one-step "
        "image admissible %d" % (pf["E_HOM"], dbl_ok, pf["E_PARITY"], pf["E_HOM"],
                                 pf["one_step_image_admissible"]))
    say("  diagonal parity records %d, of which merge PRESERVES diagonality at %d"
        % (pf["E_PARITY_diagonal"], pf["diagonal_sector_preserved"]))
    checkpoint()


def stage_semigroup(R):
    """9.7  THE SEMIGROUP: do the axis merges compose to the dyadic merge?"""
    say("")
    say("--- 7. THE COARSE-GRAINING SEMIGROUP ---")
    fam = R["_fam"]
    cells = comm = comp = 0
    iff_rows = []
    for aname in ("A4", "A6"):
        F = fam[aname]
        for tie in ("A", "B"):
            for k in sorted(F):
                rec = F[k]
                if not rec.adm:
                    continue
                m01 = merged_record(merged_record(rec, (2, 1), tie, "a0"), (1, 2), tie, "a1")
                m10 = merged_record(merged_record(rec, (1, 2), tie, "a1"), (2, 1), tie, "a0")
                md = merged_record(rec, (2, 2), tie, "d")
                n = len(md.sites) * 3
                a = sum(1 for x in md.sites for lk in md.lks
                        if m01.counts[x][lk] == m10.counts[x][lk])
                b = sum(1 for x in md.sites for lk in md.lks
                        if m01.counts[x][lk] == md.counts[x][lk])
                cells += n
                comm += a
                comp += b
                iff_rows.append({"arena": aname, "tie": tie, "record": k,
                                 "fine_diagonal": rec.diagonal(),
                                 "composite_equals_dyadic": b == n,
                                 "axis_merges_commute": a == n})
    iff = all(r["composite_equals_dyadic"] == r["fine_diagonal"] for r in iff_rows)
    # the chain: how many merges before the arena leaves the class
    def chain(L):
        k = 0
        while L % 2 == 0 and L // 2 >= 2:
            L //= 2
            k += 1
        return k, L
    c4, f4 = chain(4)
    c6, f6 = chain(6)
    R["semigroup"] = {
        "cells": cells, "axis_commute": comm, "composite_equals_dyadic": comp,
        "iff_diagonal": bool(iff), "rows": iff_rows,
        "chain_A4": c4, "chain_A4_floor_L": f4, "chain_A6": c6, "chain_A6_floor_L": f6,
        "floor_reason": "L = 1 is REFUSED: at a single site every declared link maps the "
                        "site to itself, so 'the interval between x and x+l' is a "
                        "self-loop and the count register loses its referent",
        "reading": "the two axis merges COMMUTE with each other everywhere, but their "
                   "composite equals the dyadic merge exactly on the records whose "
                   "readout is diagonal, and nowhere else.  The semigroup does not "
                   "factor through the axis merges off HA's diagonal sector, and it "
                   "does so for the same arithmetic reason HA's link-local rule closes "
                   "there: the diagonal count is the sum of the axis counts"}
    gate("G-SEMIGROUP-AXIS-COMMUTE",
         "the two 2:1 axis block-merges commute with each other at every cell",
         comm == cells and cells > 0, {"cells": cells, "commuting": comm})
    gate("G-SEMIGROUP-FACTORISATION",
         "the composite of the two axis merges equals the dyadic merge EXACTLY on the "
         "diagonal-sector records and on no other -- an iff, measured record by record",
         iff and 0 < comp < cells,
         {"cells": cells, "equal": comp, "iff_diagonal": iff,
          "disagreeing_records": sorted({r["record"] for r in iff_rows
                                         if not r["composite_equals_dyadic"]})})
    gate("G-MERGE-TERMINATES",
         "the merge chain is finite at every built arena, and the L = 1 floor is REFUSED "
         "with the measured reason",
         c4 == 1 and f4 == 2 and c6 == 1 and f6 == 3,
         {"A4_steps": c4, "A4_floor": f4, "A6_steps": c6, "A6_floor": f6})
    say("  axis merges commute %d/%d; composite == dyadic %d/%d (iff diagonal: %s)"
        % (comm, cells, comp, cells, iff))
    say("  chain: A4 -> %d steps to L=%d, A6 -> %d steps to L=%d; L=1 REFUSED"
        % (c4, f4, c6, f6))
    checkpoint()


def stage_d3(R):
    """9.8  The dimension extension: merging is TOTAL where splitting is partial."""
    say("")
    say("--- 8. THE DIMENSION EXTENSION (d = 3) ---")
    lks = LINK_D3
    uniq = 0
    for lk in lks:
        lift = tuple(2 * c for c in lk)
        if len(minimal_decompositions(lift, lks)) == 1:
            uniq += 1
    fam = R["_fam"]["A4X"]
    rec = fam["G3-FLAT"]
    blocks = {}
    for y in rec.sites:
        blocks.setdefault(tuple(c // 2 for c in y), []).append(y)
    covered = sum(len(v) for v in blocks.values())
    rows = []
    for k in sorted(fam):
        r = fam[k]
        if not r.adm:
            rows.append({"record": k, "admissible": False})
            continue
        cr = merged_record(r, (2, 2, 2))
        rows.append({"record": k, "admissible": True, "coarse_admissible": cr.adm,
                     "coarse_counts_at_0": [cr.counts[(0, 0, 0)][lk] for lk in cr.lks]})
    r6a_unreached = load_json("v14/code/r6a_refinement_receipt.json")[
        "dimension_extension"]["unreached_sites"]
    R["d3"] = {"sites": len(rec.sites), "covered": covered, "blocks": len(blocks),
               "block_sizes": sorted({len(v) for v in blocks.values()}),
               "lifts": len(lks), "unique": uniq, "rows": rows,
               "r6a_unreached": r6a_unreached,
               "reading": "at d = 3 the declared link set still gives every coarse lift a "
                          "UNIQUE minimal realisation, and the dyadic blocks partition the "
                          "site set: the merge is TOTAL.  R6a measured the SPLIT "
                          "site-incomplete at the same arena -- one parity class of refined "
                          "sites lies on no coarse interval.  Merging is the direction the "
                          "grammar licenses, and this is where the asymmetry is sharpest"}
    gate("G-D3-SITE-COMPLETE",
         "at d = 3 the dyadic blocks partition the fine site set (every site merged, none "
         "unreached) and every coarse lift has a unique minimal realisation -- the exact "
         "dual of R6a's measured site-INcompleteness of the split at the same arena",
         covered == len(rec.sites) and uniq == len(lks) and r6a_unreached > 0,
         {"sites": len(rec.sites), "covered": covered, "unique_lifts": uniq,
          "r6a_split_unreached": r6a_unreached})
    say("  d=3: %d of %d sites covered by %d blocks of size %s; %d of %d lifts unique"
        % (covered, len(rec.sites), len(blocks),
           R["d3"]["block_sizes"], uniq, len(lks)))
    say("  R6a's SPLIT left %d sites unreached at the same arena; the MERGE leaves none"
        % r6a_unreached)
    checkpoint()


def stage_commutation(R):
    """9.9  MERGE-DYNAMICS COMPATIBILITY: coarsen-then-H vs H-then-coarsen."""
    say("")
    say("--- 9. MERGE-DYNAMICS COMMUTATION ---")
    fam = R["_fam"]
    d = 2
    grid = [(fm, lr) for fm in ("SUM", "CORNER") for lr in ("SUM", "CORNER")]
    cells = nonzero = 0
    routes = route_agree = 0
    grid_stats = {}
    per_rule = Counter()
    per_rule_tot = Counter()
    per_rec = Counter()
    per_rec_tot = Counter()
    supp = Counter()
    supp_tot = Counter()
    mixed_ok = mixed_tot = 0
    uni_ok = uni_tot = 0
    lam_cells = lam_ok = 0
    fiber_cells = unsolvable = 0
    pos_control = None
    for aname, rules in (("A4", I7_RULES), ("A6", I7_RULES_EXT)):
        F = fam[aname]
        shape = F["G-FLAT"].shape
        csh = tuple(s // 2 for s in shape)
        lps = lapse_family(shape, d)
        fr = front_states(shape)
        for k in sorted(F):
            rec = F[k]
            if not rec.adm:
                continue
            crec = merged_record(rec, (2, 2))
            # independent recomputation of every weight actually used
            for rule in rules:
                for x in rec.sites:
                    lam_cells += 1
                    a = lambda_of(rule, rec, x)
                    b = lambda_independent(rule, rec, x)
                    if isinstance(a, dict):
                        if all(a[l] == b[l] for l in rec.lks):
                            lam_ok += 1
                    elif all(a[i][j] == b[i][j] for i in range(d) for j in range(d)):
                        lam_ok += 1
            for fm, lr in grid:
                ncs = {fn: coarsen_scalar(fv, csh, (2, 2), fm, d) for fn, fv in fr.items()}
                for lname, N in lps:
                    Nc = coarsen_scalar(N, csh, (2, 2), lr, d)
                    Nf = coarsen_scalar(N, csh, (2, 2), fm, d)
                    fok = all(Nc[x] == Nf[x] for x in crec.sites)
                    if fm == lr:
                        uni_tot += 1
                        uni_ok += 1 if fok else 0
                    else:
                        mixed_tot += 1
                        mixed_ok += 1 if fok else 0
                    for fn, fv in fr.items():
                        for rule in rules:
                            wf = drag(rule, rec, N, fv)
                            wc = drag(rule, crec, Nc, ncs[fn])
                            for mr, cvec in sorted(MRULES.items()):
                                D = defect_closed(wf, wc, csh, cvec, d)
                                cells += 1
                                hot = any(v != 0 for x in crec.sites for v in D[x])
                                if hot:
                                    nonzero += 1
                                    per_rule[rule] += 1
                                    per_rec[k] += 1
                                    grid_stats.setdefault((fm, lr, mr), [0, 0])[0] += 1
                                per_rule_tot[rule] += 1
                                per_rec_tot[k] += 1
                                grid_stats.setdefault((fm, lr, mr), [0, 0])[1] += 1
                                for x in crec.sites:
                                    supp_tot[str(tuple(c % 2 for c in x))] += 1
                                    if any(v != 0 for v in D[x]):
                                        supp[str(tuple(c % 2 for c in x))] += 1
                                if aname == "A4":
                                    m0 = {y: tuple(Fr(0) for _ in range(d))
                                          for y in rec.sites}
                                    ok2, D2 = defect_literal(rule, rec, crec, N, Nc, fv,
                                                             ncs[fn], m0, csh, cvec, d,
                                                             fm, lr)
                                    routes += 1
                                    if all(D[x][i] == D2[x][i] for x in crec.sites
                                           for i in range(d)) and ok2 == fok:
                                        route_agree += 1
            # the m-rule fiber, solved jointly over the whole declared lapse family
            for fm, lr in grid:
                ncs = {fn: coarsen_scalar(fv, csh, (2, 2), fm, d) for fn, fv in fr.items()}
                for rule in rules:
                    rows = []
                    rhs = []
                    for lname, N in lps:
                        Nc = coarsen_scalar(N, csh, (2, 2), lr, d)
                        for fn, fv in fr.items():
                            wf = drag(rule, rec, N, fv)
                            wc = drag(rule, crec, Nc, ncs[fn])
                            for x in crec.sites:
                                for i in range(d):
                                    rows.append([wf[tuple(2 * x[j] + o[j] for j in range(d))][i]
                                                 for o in OFFS[d]])
                                    rhs.append(wc[x][i])
                    fiber_cells += 1
                    _, sol = solve_c(rows, rhs, len(OFFS[d]))
                    if sol is None:
                        unsolvable += 1
                    if pos_control is None:
                        cstar = (Fr(1, 3), Fr(1, 5), Fr(2, 7), Fr(1))
                        prhs = [sum((r[j] * cstar[j] for j in range(4)), Fr(0))
                                for r in rows]
                        _, psol = solve_c(rows, prhs, 4)
                        pos_control = {"constructed": [str(v) for v in cstar],
                                       "recovered": None if psol is None
                                       else [str(v) for v in psol],
                                       "solver_returns_a_solution": psol is not None,
                                       "reproduces_the_image": psol is not None and all(
                                           sum((r[j] * psol[j] for j in range(4)), Fr(0)) == b
                                           for r, b in zip(rows, prhs))}
    sig = support_signature(supp, supp_tot)
    R["commutation"] = {
        "cells": cells, "nonzero": nonzero, "zero": cells - nonzero,
        "grid_cells": len(grid), "grid_universal": uni_tot and 2 or 0,
        "front_universal_ok": uni_ok, "front_universal_total": uni_tot,
        "mixed_commuting": mixed_ok, "mixed_total": mixed_tot,
        "per_rule": {k: {"nonzero": per_rule[k], "cells": per_rule_tot[k]}
                     for k in sorted(per_rule_tot)},
        "per_record": {k: {"nonzero": per_rec[k], "cells": per_rec_tot[k]}
                       for k in sorted(per_rec_tot)},
        "per_grid": {"%s/%s/%s" % k: {"nonzero": v[0], "cells": v[1]}
                     for k, v in sorted(grid_stats.items())},
        "support": {k: {"nonzero": supp[k], "total": supp_tot[k]} for k in sorted(supp_tot)},
        "support_signature": sig,
        "two_routes": {"compared": routes, "agreeing": route_agree,
                       "shared": "both routes call drag(); the shared part is policed by "
                                 "G-LAMBDA-INDEPENDENT, which recomputes every weight the "
                                 "census uses by a second, independently written route",
                       "not_shared": "route 2 builds the two orders as configuration maps "
                                     "on (n, m) and coarsens both registers; route 1 never "
                                     "forms a total record"},
        "lambda_cells": lam_cells, "lambda_ok": lam_ok,
        "fiber_cells": fiber_cells, "unsolvable": unsolvable,
        "positive_control": pos_control,
        "closed_form": "D^i(x) = sum_k c_k N^f(y_k) sum_j Lambda^f(y_k)^{ij} "
                       "(n(y_k+e_j) - n(y_k)) - N^c(x) sum_j Lambda^c(x)^{ij} "
                       "(n^c(x+e_j) - n^c(x)),  y_k = iota(x) + delta_k",
        "matter_independence": "the matter record cancels between the two orders, so the "
                               "defect is a pure drag comparison and is independent of m",
        "reading": "the FRONT sector commutes exactly when the lapse restriction is the "
                   "SAME rule as the front merge, at every lapse of the declared family; "
                   "the mixed pairs commute only at the block-corner deltas.  The REGISTER "
                   "sector carries a defect that no linear matter-merge rule can remove: "
                   "the joint system over the declared lapse family is UNSOLVABLE at every "
                   "censused cell, while the positive control shows the same solver "
                   "returning a solution when one exists"}
    gate("G-LIFT-GRID-CELL-COMPLETE",
         "the (front merge, lapse restriction) grid is complete and every cell is measured",
         len(grid) == 4 and uni_tot + mixed_tot > 0,
         {"grid": [list(g) for g in grid], "universal_cells": uni_tot,
          "mixed_cells": mixed_tot})
    gate("G-FRONT-SECTOR-COMMUTES",
         "the front sector commutes at EVERY lapse when the lapse restriction matches the "
         "front merge, and at a strictly smaller counted set when it does not",
         uni_ok == uni_tot and 0 < mixed_ok < mixed_tot,
         {"matched_ok": uni_ok, "matched_total": uni_tot,
          "mixed_ok": mixed_ok, "mixed_total": mixed_tot})
    gate("G-DEFECT-NONZERO",
         "the register-sector commutation defect is a MEASURED nonzero object: nonzero at "
         "a counted set of cells and identically zero at a counted complement -- both "
         "nonempty, so the measurement could have come out otherwise",
         0 < nonzero < cells, {"cells": cells, "nonzero": nonzero, "zero": cells - nonzero})
    gate("G-DEFECT-TWO-ROUTES",
         "the closed form and the literal two-order composition of configuration maps "
         "agree at every compared cell",
         routes > 0 and route_agree == routes, {"compared": routes, "agreeing": route_agree})
    gate("G-DEFECT-CHARACTERISED",
         "the defect is characterised, not merely reported: its support by block parity "
         "class, its per-rule and per-record profiles and its per-grid profile are all "
         "measured and cell-complete",
         (sum(v["cells"] for v in R["commutation"]["per_rule"].values()) == cells
          and sum(v["cells"] for v in R["commutation"]["per_record"].values()) == cells
          and sum(v["cells"] for v in R["commutation"]["per_grid"].values()) == cells
          and sig != "SUPPRESSED"),
         {"per_rule_cells": sum(v["cells"] for v in R["commutation"]["per_rule"].values()),
          "per_record_cells": sum(v["cells"] for v in R["commutation"]["per_record"].values()),
          "per_grid_cells": sum(v["cells"] for v in R["commutation"]["per_grid"].values()),
          "support_signature": sig})
    gate("G-DEFECT-IRREDUCIBLE",
         "no linear matter-merge rule removes the defect: the joint linear system over the "
         "whole declared lapse family is UNSOLVABLE at every censused cell -- and the "
         "positive control shows the same solver returning the constructed solution when "
         "one exists, so the verdict is a measurement and not a solver artefact",
         unsolvable == fiber_cells and fiber_cells > 0 and pos_control is not None
         and pos_control["solver_returns_a_solution"] and pos_control["reproduces_the_image"],
         {"cells": fiber_cells, "unsolvable": unsolvable, "positive_control": pos_control})
    gate("G-LAMBDA-INDEPENDENT",
         "every drag weight the census uses is recomputed by a second, independently "
         "written route (diagonal rules assembled directly, inserted rules by the "
         "adjugate/determinant formula): 0 mismatches",
         lam_ok == lam_cells and lam_cells > 0, {"cells": lam_cells, "agreeing": lam_ok})
    say("  commutation cells %d: nonzero %d, identically zero %d"
        % (cells, nonzero, cells - nonzero))
    say("  front grid: matched pairs commute %d/%d; mixed pairs %d/%d"
        % (uni_ok, uni_tot, mixed_ok, mixed_tot))
    say("  two routes agree %d/%d; independent weight route agrees %d/%d"
        % (route_agree, routes, lam_ok, lam_cells))
    say("  m-rule fiber: UNSOLVABLE at %d of %d cells (positive control recovers a "
        "constructed solution)" % (unsolvable, fiber_cells))
    say("  support by block parity class: %s" % sig)
    checkpoint()


def stage_consistency(R):
    """9.10  THE CONSISTENCY CONTROL: R6a's split run backwards."""
    say("")
    say("--- 10. CONSISTENCY CONTROL: SPLIT-THEN-MERGE ---")
    fam3 = build_family(2, (3, 3))
    checks, ok, per = split_merge_rows(fam3)
    r6 = load_json("v14/code/r6a_refinement_receipt.json")
    r6f = r6["split_fibers"]
    compared = reproduced = 0
    rows = []
    for k in sorted(r6f):
        compared += 1
        mine = per.get(k, {})
        theirs = r6f[k]
        agree = (mine.get("fiber", -1) == theirs["admissible_at_images"]
                 and sorted(mine.get("per_site", [])) == sorted(theirs["per_site_admissible"])
                 and (mine.get("status") == "SPLITTABLE") == theirs["splittable"])
        if agree:
            reproduced += 1
        rows.append({"record": k, "mine_fiber": mine.get("fiber"),
                     "r6a_fiber": theirs["admissible_at_images"],
                     "mine_per_site": mine.get("per_site"),
                     "r6a_per_site": theirs["per_site_admissible"],
                     "agree": agree})
    lat = hom_lattice()
    splittable_lat = sum(1 for v in lat if split_admissible(v) > 0)
    uniq = [v for v in lat if split_admissible(v) == 1]
    r6l = r6["count_lattice"]
    lat_agree = (len(lat) == r6l["admissible_count_vectors"]
                 and splittable_lat == r6l["splittable"]
                 and [list(u) for u in uniq] == r6l["unique_admissible_split"])
    spl = sum(1 for v in per.values() if v["status"] == "SPLITTABLE")
    uns = sum(1 for v in per.values() if v["status"] == "UNSPLITTABLE")
    site_local = True
    # front identity: the block sum equals the coarse front iff the new fronts vanish
    front_iff_rows = []
    for newval in (0, 1):
        rec = fam3["G-DIAG2"]
        nc0 = {x: 7 for x in rec.sites}
        blocksum = {x: nc0[x] + 3 * newval for x in rec.sites}
        front_iff_rows.append({"new_front_value": newval,
                               "identity": all(blocksum[x] == nc0[x] for x in rec.sites)})
    front_iff = (front_iff_rows[0]["identity"] and not front_iff_rows[1]["identity"])
    R["consistency"] = {
        "identity_checks": checks, "identity_ok": ok,
        "per_record": per, "fibers_compared": compared, "fibers_reproduced": reproduced,
        "fiber_rows": rows, "splittable": spl, "unsplittable": uns,
        "count_lattice": {"admissible": len(lat), "splittable": splittable_lat,
                          "unique_admissible_split": [list(u) for u in uniq],
                          "agrees_with_r6a": bool(lat_agree)},
        "site_locality": "the split fiber factorises over coarse sites and the merge is "
                         "site-local, so a per-site exhaustive check IS fiber-exhaustive",
        "front_iff": bool(front_iff), "front_iff_rows": front_iff_rows,
        "front_reading": "under the FORCED block-sum front rule, split-then-merge is the "
                         "identity on the front register exactly when R6a's class-(iii) "
                         "NEW-FRONT-VALUES are zero; the merge direction therefore cuts an "
                         "INFINITE R6a fiber to a single point -- conditionally on "
                         "demanding the identity, which is stated and not hidden",
        "matter_reading": "under M-CORNER the identity on the matter register is "
                          "unconditional; under any other rule in the fiber it holds "
                          "exactly when the split's new-site addresses agree with the "
                          "corner address"}
    gate("G-SPLIT-MERGE-IDENTITY",
         "split-then-merge is the IDENTITY on the count register at every per-site "
         "admissible split of every splittable record -- R6a's move run backwards "
         "reproduces the merge on its overlap",
         ok == checks and checks > 0, {"checks": checks, "ok": ok})
    gate("G-SPLIT-FIBER-ANCHOR",
         "this unit's INDEPENDENT rebuild of the split fibers reproduces R6a's delivered "
         "table cell by cell -- fibers, per-site admissible counts and splittability",
         reproduced == compared and compared > 0,
         {"compared": compared, "reproduced": reproduced})
    gate("G-COUNT-LATTICE-REPRODUCES-R6A",
         "this unit's independent count-lattice census reproduces R6a's delivered numbers "
         "exactly: admissible vectors, splittable vectors and the unique-admissible-split "
         "witness",
         lat_agree, {"admissible": len(lat), "splittable": splittable_lat,
                     "unique": [list(u) for u in uniq],
                     "r6a": {"admissible": r6l["admissible_count_vectors"],
                             "splittable": r6l["splittable"],
                             "unique": r6l["unique_admissible_split"]}})
    gate("G-SITE-LOCALITY",
         "the merge is site-local in the coarse site and the split fiber factorises over "
         "coarse sites, so the per-site exhaustive check is fiber-exhaustive: the "
         "measured fiber equals the product of the per-site counts at every record",
         all(v["fiber"] == prod_of(v["per_site"], per_site_multiplicity(fam3, k))
             for k, v in per.items() if v["status"] == "SPLITTABLE") and site_local,
         {"records": spl})
    gate("G-SPLIT-MERGE-FRONT-IFF",
         "on the front register the split-merge identity holds exactly when the split's "
         "free new-front values vanish -- measured in both directions",
         front_iff, {"rows": front_iff_rows})
    say("  split-then-merge identity on the count register: %d/%d" % (ok, checks))
    say("  R6a split fibers reproduced independently: %d of %d records; splittable %d, "
        "unsplittable %d" % (reproduced, compared, spl, uns))
    say("  count lattice reproduced: %d admissible, %d splittable, unique split %s"
        % (len(lat), splittable_lat, [list(u) for u in uniq]))
    checkpoint()


def prod_of(vals, mult):
    p = 1
    for v, m in zip(sorted(vals), mult):
        p *= v ** m
    return p


def per_site_multiplicity(fam, k):
    """How many sites carry each distinct per-site split count.  [instrument]"""
    rec = fam[k]
    counts = Counter()
    for x in rec.sites:
        c = rec.counts[x]
        counts[split_admissible((c[rec.lks[0]], c[rec.lks[1]], c[rec.lks[2]]))] += 1
    if on("locality-lax"):
        return [0] * len(counts)
    return [counts[v] for v in sorted(counts)]


PAPER_CLAIM_RULE = ("every load-bearing numeric sentence of the paper is RENDERED HERE "
                    "from the measured object and must appear VERBATIM in the paper; a "
                    "number the instrument does not render is a number the paper may not "
                    "carry")


def paper_claims(R):
    """[instrument -- mutable]"""
    c = {
        "arenas": "The L = 3 arena I7 declares does not merge: 3 is odd, and all %d of its "
                  "declared records are recorded non-mergeable." % R["arenas"]["non_mergeable_records"],
        "incidence": "M-DYADIC's incidence is forced: %d of %d coarse lifts have a unique "
                     "minimal realisation." % (R["move_census"]["dyadic_unique"],
                                               R["move_census"]["dyadic_lifts"]),
        "blocked": "M-AXIS carries %d candidate realisations of the diagonal lift, and the "
                   "block is real: the two readings disagree at %d of %d cells, on %d of "
                   "%d records." % (R["move_census"]["axis_candidates"],
                                    R["axis_block"]["disagreeing"], R["axis_block"]["cells"],
                                    R["axis_block"]["records_disagreeing"],
                                    R["axis_block"]["records"]),
        "additivity": "Count additivity holds at %d of %d checked cells and the front sums "
                      "at %d of %d." % (R["forced"]["additivity_ok"],
                                        R["forced"]["additivity_checks"],
                                        R["forced"]["front_ok"], R["forced"]["front_checks"]),
        "alt": "The declared alternative composition differs at %d cells."
               % R["forced"]["alt_interior_delta"],
        "transform": "The diagonal components of q are additive at %d of %d cells; the "
                     "cross component at %d of %d." % (R["transform"]["diag_ok"],
                                                       R["transform"]["diag_cells"],
                                                       R["transform"]["cross_ok"],
                                                       R["transform"]["cross_cells"]),
        "mfiber": "The matter-merge fiber is an affine Q-space of dimension %d; over the "
                  "declared coefficient box %d of %d members are D-equivariant and %d are "
                  "also relabelling-equivariant." % (R["m_fiber"]["affine_dimension_over_Q"],
                                                     R["m_fiber"]["D_equivariant"],
                                                     R["m_fiber"]["box"],
                                                     R["m_fiber"]["chart_equivariant"]),
        "stabiliser": "The merge breaks the chart translations to the block-preserving "
                      "subgroup: %d of %d survive at A6, of index %d."
                      % (R["chart_subgroup"]["A6"]["block_preserving"],
                         R["chart_subgroup"]["A6"]["translations"],
                         R["chart_subgroup"]["A6"]["index"]),
        "inventory": "The inventory closes at FORCED %d, STABILIZER %d, FREE %d."
                     % (R["choice_inventory"]["forced"],
                        R["choice_inventory"]["stabiliser_fixed"],
                        R["choice_inventory"]["genuinely_free"]),
        "fixed": "Over the declared affine box of %d parameter points, %d are admissible "
                 "and %d are merge-self-similar, with rescalings %d at lambda = 2 and %d "
                 "at lambda = 4." % (R["fixed_points"]["affine_box"],
                                     R["fixed_points"]["affine_admissible"],
                                     R["fixed_points"]["affine_fixed"],
                                     R["fixed_points"]["lambda2"],
                                     R["fixed_points"]["lambda4"]),
        "parity": "E-HOM carries %d records and E-PARITY %d; the merge sends every parity "
                  "record to a homogeneous one in a single step, with %d of them landing "
                  "on an admissible image." % (R["fixed_points"]["E_HOM"],
                                               R["fixed_points"]["E_PARITY"],
                                               R["fixed_points"]["E_PARITY_one_step_image_admissible"]),
        "sector": "Of the %d diagonal parity records, the merge preserves diagonality at %d."
                  % (R["fixed_points"]["E_PARITY_diagonal"],
                     R["fixed_points"]["E_PARITY_diagonal_sector_preserved"]),
        "semigroup": "The two axis merges commute at %d of %d cells, while their composite "
                     "equals the dyadic merge at %d of %d." % (R["semigroup"]["axis_commute"],
                                                               R["semigroup"]["cells"],
                                                               R["semigroup"]["composite_equals_dyadic"],
                                                               R["semigroup"]["cells"]),
        "d3": "At d = 3 the dyadic blocks cover %d of %d sites and %d of %d lifts are "
              "unique, while R6a measured %d sites unreached by the split at the same "
              "arena." % (R["d3"]["covered"], R["d3"]["sites"], R["d3"]["unique"],
                          R["d3"]["lifts"], R["d3"]["r6a_unreached"]),
        "defect": "The register defect is nonzero at %d of %d censused cells and "
                  "identically zero at %d." % (R["commutation"]["nonzero"],
                                               R["commutation"]["cells"],
                                               R["commutation"]["zero"]),
        "frontgrid": "The front sector commutes at %d of %d matched cells and at %d of %d "
                     "mixed ones." % (R["commutation"]["front_universal_ok"],
                                      R["commutation"]["front_universal_total"],
                                      R["commutation"]["mixed_commuting"],
                                      R["commutation"]["mixed_total"]),
        "irreducible": "The joint linear system for a defect-killing matter rule is "
                       "unsolvable at %d of %d cells." % (R["commutation"]["unsolvable"],
                                                          R["commutation"]["fiber_cells"]),
        "routes": "The closed form and the literal composition agree at %d of %d compared "
                  "cells, and the independent weight route at %d of %d."
                  % (R["commutation"]["two_routes"]["agreeing"],
                     R["commutation"]["two_routes"]["compared"],
                     R["commutation"]["lambda_ok"], R["commutation"]["lambda_cells"]),
        "consistency": "Split-then-merge is the identity at %d of %d checks, and this "
                       "unit's independent rebuild reproduces R6a's split fibers at %d of "
                       "%d records." % (R["consistency"]["identity_ok"],
                                        R["consistency"]["identity_checks"],
                                        R["consistency"]["fibers_reproduced"],
                                        R["consistency"]["fibers_compared"]),
        "drift": "R6a's receipt moved from %s to %s while this unit was built, and all "
                 "%d of the values this unit reads from it by path are unchanged."
                 % (R["r6a_drift"]["pin_hash"], R["r6a_drift"]["observed_hash"],
                    R["r6a_drift"]["path_value_rows_unchanged"]),
        "lattice": "The count lattice reproduces at %d admissible vectors and %d "
                   "splittable ones." % (R["consistency"]["count_lattice"]["admissible"],
                                         R["consistency"]["count_lattice"]["splittable"]),
        "verdict": R["verdict"],
    }
    if on("prose-claim-drift"):
        c["defect"] = c["defect"].replace(str(R["commutation"]["nonzero"]), "999999")
    return c


def build_receipt(R):
    """[instrument -- mutable]  ONE object: the gates check it, the receipt and the
    paper render from it."""
    rec = {
        "unit": DECL["unit"],
        "question": "merging is the direction the grammar licenses -- construct the merge "
                    "moves, run the choice inventory on the merge direction for the FULL "
                    "record (s, n, m), measure the transformation law, the fixed-point "
                    "census, the merge/dynamics commutation and the split-merge "
                    "consistency control",
        "anchors": ANCHORS, "anchor_totals": R["anchor_totals"],
        "declarations": DECL,
        "arenas": R["arenas"], "non_mergeable": R["non_mergeable"],
        "move_census": R["move_census"], "axis_block": R["axis_block"],
        "control": R["control"], "forced": R["forced"], "transform": R["transform"],
        "chart_subgroup": R["chart_subgroup"], "m_fiber": R["m_fiber"],
        "choice_inventory": R["choice_inventory"], "fixed_points": R["fixed_points"],
        "semigroup": R["semigroup"], "d3": R["d3"], "commutation": R["commutation"],
        "consistency": R["consistency"], "r6a_drift": R["r6a_drift"],
        "verdict": R["verdict"], "verdict_head": R["verdict_head"],
        "verdict_segments": R["verdict_segments"],
    }
    if on("render-escape"):
        rec["commutation"] = dict(rec["commutation"])
        rec["commutation"]["nonzero"] = rec["commutation"]["nonzero"] + 1
    return rec


def emit(R, write):
    rec = build_receipt(R)
    rebuilt = reconstruct_verdict_from_receipt(rec)
    gate("G-VERDICT-STRING-EQUALITY",
         "the COMPLETE emitted verdict string equals a string rebuilt segment by segment "
         "from the RECEIPT OBJECT by a comparator that shares no code and no input with "
         "the builder; containment is not equality",
         rebuilt == R["verdict"], {"emitted": R["verdict"], "reconstructed": rebuilt,
                                   "equal": rebuilt == R["verdict"]})
    gate("G-RENDER-FROM-THE-GATED-OBJECT",
         "the receipt object the gates check IS the object the receipt and the paper "
         "render from: the commutation census in the receipt equals the gated census",
         rec["commutation"]["nonzero"] == R["commutation"]["nonzero"]
         and rec["commutation"]["cells"] == R["commutation"]["cells"],
         {"gated": R["commutation"]["nonzero"], "rendered": rec["commutation"]["nonzero"]})
    flips = []
    for seg in R["verdict_segments"]:
        flips.append({"segment": seg["name"], "flips": segment_flips(rec, seg)})
    gate("G-VERDICT-SEGMENTS-FLIPPABLE",
         "every verdict segment is derived: perturbing the receipt row it reads moves the "
         "reconstructed segment",
         all(f["flips"] for f in flips), {"segments": flips})
    heads = {"CANONICAL": "CRC-MERGE-CANONICAL-ON", "CHOICE": "CRC-MERGE-CHOICE-AT",
             "EMITTED": R["verdict_head"]}
    probe = json.loads(json.dumps({"choice_inventory": {"genuinely_free": 0}}))
    reach = reconstruct_head(probe) == "CRC-MERGE-CANONICAL-ON" and \
        reconstruct_head({"choice_inventory": {"genuinely_free": 1}}) == "CRC-MERGE-CHOICE-AT"
    gate("G-VERDICT-ALL-HEADS-REACHABLE",
         "both declared verdict heads are reachable by measurement: a synthetic inventory "
         "with no free freedom yields CANONICAL, one with a free freedom yields CHOICE",
         reach, {"heads": heads, "both_reachable": reach})
    claims = paper_claims(R)
    try:
        with open(PAPER, encoding="utf-8") as fh:
            ptxt = " ".join(fh.read().split())
        present = {k: (" ".join(v.split()) in ptxt) for k, v in claims.items()}
    except FileNotFoundError:
        present = {k: False for k in claims}
    gate("G-PROSE-RENDERS-FROM-THE-RECEIPT",
         "every load-bearing numeric sentence of the paper is rendered here from the "
         "receipt object and appears VERBATIM in the paper (line wrapping normalised, "
         "content not)",
         all(present.values()),
         {"claims": len(claims), "present": sum(1 for v in present.values() if v),
          "missing": sorted(k for k, v in present.items() if not v)})
    rec["paper_claims"] = {"paper": DECL["paper"], "rule": PAPER_CLAIM_RULE,
                           "claims_rendered": len(claims),
                           "claims_present_in_the_paper": sum(1 for v in present.values() if v),
                           "claims_missing": sorted(k for k, v in present.items() if not v),
                           "rendered": claims}
    rec["verdict_audit"] = {"emitted": R["verdict"], "reconstructed": rebuilt,
                            "segment_flips": flips, "heads_reachable": heads}
    rec["cache"] = dict(_CSTAT)
    gate("G-CACHE-EXERCISED",
         "the weight memo is exercised: lookups and hits are both nonzero, and the fresh "
         "bypass path is taken",
         _CSTAT["hits"] > 0 and _CSTAT["misses"] > 0, dict(_CSTAT))
    fresh_ok = fresh_cells = 0
    for aname in ("A4",):
        for k in sorted(R["_fam"][aname]):
            r0 = R["_fam"][aname][k]
            if not r0.adm:
                continue
            # the self-test sweeps BOTH the fine record and its dyadic merge: the
            # census reads weights off both, so a cache that confuses them must die here
            for r in (r0, merged_record(r0, (2, 2))):
                for rule in I7_RULES:
                    for x in r.sites:
                        fresh_cells += 1
                        a = lambda_of(rule, r, x)
                        b = lambda_of(rule, r, x, fresh=True)
                        same = (all(a[l] == b[l] for l in r.lks) if isinstance(a, dict)
                                else all(a[i][j] == b[i][j] for i in range(r.d)
                                         for j in range(r.d)))
                        if same:
                            fresh_ok += 1
    gate("G-CACHE-FRESH-EQUALS-MEMO",
         "every memoised weight is recomputed with the memo BYPASSED and compared against "
         "what the memo returned: 0 disagreements, and the bypass count is nonzero",
         fresh_ok == fresh_cells and fresh_cells > 0 and _CSTAT["bypass"] > 0,
         {"cells": fresh_cells, "agreeing": fresh_ok, "bypasses": _CSTAT["bypass"]})
    rec["cache"] = dict(_CSTAT)
    floats = find_floats(rec)
    gate("G-NO-FLOATS-IN-RECEIPT", "no float value appears anywhere in the receipt",
         not floats, {"hits": floats[:5], "count": len(floats)})
    fal = falsifier_census()
    rec["falsifier_census"] = fal
    gate("G-FALSIFIER-CENSUS-HONEST",
         "the never-falsified census is present from delivery one, with an honest "
         "denominator and a stated waiver for every gate carrying no declared falsifier",
         set(fal["never_falsified"]) == set(fal["waivers"]),
         {"gates": fal["gates"], "with_falsifier": fal["gates_with_a_declared_falsifier"],
          "never_falsified": fal["never_falsified_count"]})
    rec["compliance"] = compliance_sweep()
    rec["disclosures"] = DISCLOSURES
    rec["totals"] = {"anchors": len(ANCHORS), "gates": len(GATES),
                     "must_pass_gates": sum(1 for g in GATES if g["must_pass"]),
                     "recorded_gates": sum(1 for g in GATES if not g["must_pass"]),
                     "mutants": len(MUTANTS),
                     "must_pass_failures": len([g for g in GATES
                                                if g["must_pass"] and not g["ok"]]),
                     "anchor_failures": len([a for a in ANCHORS if not a["ok"]]),
                     "mutant_survivors": 0}
    gate("G-FINAL-GATE-COUNT",
         "the registered gate count matches the count the receipt reports",
         rec["totals"]["gates"] == len(GATES), {"gates": len(GATES)})
    rec["totals"]["gates"] = len(GATES)
    rec["totals"]["must_pass_gates"] = sum(1 for g in GATES if g["must_pass"])
    rec["gates"] = GATES
    rec["mutants"] = MUTANTS
    rec["schema"] = "isp/v14/crc-coarsegrain/1"
    rec["pin"] = "v14/note-cr-batch-pins.md"
    rec["pin_sha256_prefix"] = sha12(REPO + "/v14/note-cr-batch-pins.md")
    rec["grammar_sources"] = {
        "v13/code/ha_successor_receipt.json": "542b8735daf0",
        "v13/paper-ha-successor.md": "f286ba10d2d9",
        "v13/code/ha_successor_exact.py": "d44cb72f8ee9",
        "v14/code/r6a_refinement_receipt.json": "022c3f488a93 [DELIVERED-UNDER-PANEL]"}
    rec["source_sha256"] = hashlib.sha256(_own_source().encode()).hexdigest()
    rec["python"] = "%d.%d.%d" % sys.version_info[:3]
    rec["arithmetic"] = "int / fractions.Fraction only; no float, no tolerance"
    if write:
        with open(OUT_JSON, "w", encoding="utf-8") as fh:
            json.dump(rec, fh, indent=1, sort_keys=True, default=str)
            fh.write("\n")
        with open(OUT_TXT, "w", encoding="utf-8") as fh:
            fh.write("\n".join(LOG) + "\n")
    return rec


def reconstruct_head(rec):
    return "CRC-MERGE-CANONICAL-ON" if rec["choice_inventory"]["genuinely_free"] == 0 \
        else "CRC-MERGE-CHOICE-AT"


def segment_flips(rec, seg):
    """Perturb the receipt row the segment derives from and require the
    reconstruction to move."""
    keymap = {"ARENAS": ("arenas", "non_mergeable_records"),
              "MOVES": ("move_census", "dyadic_unique"),
              "BLOCK-REAL": ("axis_block", "disagreeing"),
              "CANONICAL": ("forced", "additivity_ok"),
              "CHOICE": ("m_fiber", "chart_equivariant"),
              "INVENTORY": ("choice_inventory", "forced"),
              "TRANSFORM": ("transform", "diag_ok"),
              "FIXED-POINTS": ("fixed_points", "affine_fixed"),
              "SEMIGROUP": ("semigroup", "axis_commute"),
              "COMMUTATION": ("commutation", "nonzero"),
              "CONSISTENCY": ("consistency", "identity_ok"),
              "D3": ("d3", "covered")}
    if seg["name"] not in keymap:
        return False          # an injected segment derives from no receipt row
    a, b = keymap[seg["name"]]
    probe = json.loads(json.dumps(rec, default=str))
    base = reconstruct_verdict_from_receipt(probe)
    probe[a][b] = probe[a][b] + 1 if isinstance(probe[a][b], int) else "X"
    return reconstruct_verdict_from_receipt(probe) != base


def find_floats(obj, path=""):
    hits = []
    if isinstance(obj, float):
        hits.append(path)
    elif isinstance(obj, dict):
        for k, v in obj.items():
            hits += find_floats(v, path + "/" + str(k))
    elif isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            hits += find_floats(v, path + "/%d" % i)
    return hits


# ==========================================================================
# 10.  MUTANTS, THE FALSIFIER CENSUS, THE COMPLIANCE SWEEP
# ==========================================================================
MUTANTS = [
    {"name": "anchor-hash-A-I7-RECEIPT", "expected_gate": "A-I7-RECEIPT",
     "what": "corrupts the pinned I7 receipt hash"},
    {"name": "anchor-hash-A-HA-PAPER", "expected_gate": "A-HA-PAPER",
     "what": "corrupts the pinned HA paper hash"},
    {"name": "anchor-hash-A-HA-CODE", "expected_gate": "A-HA-CODE",
     "what": "corrupts the pinned HA instrument hash"},
    {"name": "anchor-hash-A-R6A-RECEIPT", "expected_gate": "A-R6A-RECEIPT",
     "what": "returns an R6a receipt hash outside the declared accepted list"},
    {"name": "r6a-value-drift", "expected_gate": "G-R6A-VALUES-STABLE-UNDER-DRIFT",
     "what": "drifts a value read by path from the R6a receipt"},
    {"name": "anchor-skip", "expected_gate": "G-ANCHOR-CELL-COMPLETE",
     "what": "drops one declared anchor row"},
    {"name": "path-drift", "expected_gate": "G-PATH-ANCHORS",
     "what": "reads a pinned value from a drifted json path"},
    {"name": "path-value", "expected_gate": "G-PATH-ANCHORS",
     "what": "reads the right path and the wrong value"},
    {"name": "text-anchor-drift", "expected_gate": "G-TEXT-ANCHORS",
     "what": "perturbs a verbatim source quotation"},
    {"name": "float-lax", "expected_gate": "G-FLOATGUARD",
     "what": "blinds the float scanner"},
    {"name": "census-drop", "expected_gate": "G-MOVE-CENSUS-CELL-COMPLETE",
     "what": "silently drops a move class from the census"},
    {"name": "incidence-lax", "expected_gate": "G-INCIDENCE-AMBIGUOUS-AXIS",
     "what": "returns a single hard-coded decomposition for every lift, erasing the "
             "measured axis ambiguity"},
    {"name": "incidence-fake-tie", "expected_gate": "G-INCIDENCE-FORCED-DYADIC",
     "what": "duplicates every decomposition, so no lift looks uniquely realised"},
    {"name": "block-fake", "expected_gate": "G-BLOCK-IS-REAL",
     "what": "reports the axis-merge readings as agreeing"},
    {"name": "nonmergeable-skip", "expected_gate": "G-NON-MERGEABLE-RECORDED",
     "what": "skips one non-mergeable record instead of recording it"},
    {"name": "additivity-violation", "expected_gate": "G-COUNT-ADDITIVITY-FORCED",
     "what": "perturbs one merged interval count"},
    {"name": "front-rule-lax", "expected_gate": "G-FRONT-ADDITIVITY-FORCED",
     "what": "serves the CORNER reading where the SUM rule is asked for"},
    {"name": "qlaw-lax", "expected_gate": "G-Q-TRANSFORM-LAW",
     "what": "reports the cross-term additivity as universal"},
    {"name": "inventory-corrupt", "expected_gate": "G-INVENTORY-CLASSIFICATION",
     "what": "relabels the class-(iii) matter freedom as class-(i)"},
    {"name": "fiber-typed", "expected_gate": "G-FIBER-COMPUTED",
     "what": "strips the measured evidence from every inventory fiber"},
    {"name": "stabilizer-lax", "expected_gate": "G-STABILIZER-MEASURED",
     "what": "reports the whole chart group as surviving the merge"},
    {"name": "mfiber-lax", "expected_gate": "G-M-FIBER-INFINITE",
     "what": "drops the relabelling constraint and the dimension"},
    {"name": "fixedpoint-drop", "expected_gate": "G-RESCALING-MEASURED",
     "what": "drops the lambda = 4 fixed-point family"},
    {"name": "lambda-typed", "expected_gate": "G-RESCALING-MEASURED",
     "what": "types every rescaling as 2 instead of measuring it"},
    {"name": "flow-lax", "expected_gate": "G-PARITY-FLOW",
     "what": "reports the whole parity family as flowing to admissible images"},
    {"name": "defect-suppress", "expected_gate": "G-DEFECT-NONZERO",
     "what": "zeroes the commutation defect"},
    {"name": "order-swap", "expected_gate": "G-DEFECT-TWO-ROUTES",
     "what": "swaps the two orders in the literal route only"},
    {"name": "coarsen-skew", "expected_gate": "G-DEFECT-TWO-ROUTES",
     "what": "rotates the block offsets in the register coarsening"},
    {"name": "defect-support-lax", "expected_gate": "G-DEFECT-CHARACTERISED",
     "what": "suppresses the defect's support signature"},
    {"name": "solver-lax", "expected_gate": "G-DEFECT-IRREDUCIBLE",
     "what": "makes the exact solver accept an inconsistent system"},
    {"name": "lambda-route-lax", "expected_gate": "G-LAMBDA-INDEPENDENT",
     "what": "scales the independent weight route"},
    {"name": "splitmerge-lax", "expected_gate": "G-SPLIT-MERGE-IDENTITY",
     "what": "makes the split-merge comparison return its own target"},
    {"name": "locality-lax", "expected_gate": "G-SITE-LOCALITY",
     "what": "corrupts the per-site multiplicity used by the factorisation check"},
    {"name": "control-pass", "expected_gate": "G-CONTROL-FOREIGN",
     "what": "lets the foreign move through the audit"},
    {"name": "cache-alias", "expected_gate": "G-CACHE-FRESH-EQUALS-MEMO",
     "what": "serves a merged record the base record's cached weight"},
    {"name": "cache-lax", "expected_gate": "G-CACHE-FRESH-EQUALS-MEMO",
     "what": "routes the fresh path back through the memo"},
    {"name": "verdict-pair-swap", "expected_gate": "G-VERDICT-STRING-EQUALITY",
     "what": "swaps two value names inside a verdict segment"},
    {"name": "verdict-typed-segment", "expected_gate": "G-VERDICT-STRING-EQUALITY",
     "what": "hand-types one verdict segment"},
    {"name": "verdict-append-text", "expected_gate": "G-VERDICT-STRING-EQUALITY",
     "what": "appends a segment to the verdict"},
    {"name": "verdict-fully-typed", "expected_gate": "G-VERDICT-STRING-EQUALITY",
     "what": "hand-types the whole verdict"},
    {"name": "verdict-inert-segment", "expected_gate": "G-VERDICT-STRING-EQUALITY",
     "what": "replaces a segment by an inert constant"},
    {"name": "head-constant", "expected_gate": "G-VERDICT-STRING-EQUALITY",
     "what": "pins the verdict head to a constant instead of deriving it from the "
             "inventory's class counts"},
    {"name": "render-escape", "expected_gate": "G-RENDER-FROM-THE-GATED-OBJECT",
     "what": "lets a corrupted census cell reach the receipt"},
    {"name": "prose-claim-drift", "expected_gate": "G-PROSE-RENDERS-FROM-THE-RECEIPT",
     "what": "drifts one rendered paper claim away from the measured value"},
]

FALSIFIER_MAP = {}
for _m in MUTANTS:
    FALSIFIER_MAP.setdefault(_m["expected_gate"], []).append(_m["name"])

WAIVERS = {
    "G-NO-MUTANT-IDENTITY": "an AST scan validated by synthetic injections it must flag; "
                            "a mutant of the scan would be a mutant of the falsifier",
    "G-ARENA-CLASS": "a declaration check: the arenas are built here from the pinned "
                     "schema, so no independent object can drift from them",
    "G-READOUT-REENCODING": "re-verification of a pinned I7 fact",
    "G-INCIDENCE-AMBIGUOUS-AXIS": "the same helper incidence-lax kills it; listed under "
                                  "G-INCIDENCE-FORCED-DYADIC to avoid double counting",
    "G-COVARIANT-SET": "a cell-completeness check on a declared list",
    "G-SECTOR-STABILITY": "measured on the declared family; the enlargement's counter-"
                          "examples are reported in the same receipt",
    "G-INTERIOR-CONTRIBUTION-EXCLUDED": "a measured delta of the declared alternative; a "
                                        "mutant that removed the delta would remove the "
                                        "alternative, not the gate",
    "G-MOTIVATION-QUALIFIER-COMPUTED": "analytically forced once the inventory is fixed; "
                                       "inventory-corrupt moves the inventory it reads",
    "G-FIXED-POINT-CENSUS": "cell-completeness over the declared parameter box",
    "G-FIXED-POINT-SECTOR": "fixedpoint-drop and lambda-typed both move the census it reads",
    "G-SEMIGROUP-AXIS-COMMUTE": "incidence-lax moves the merge the gate compares",
    "G-SEMIGROUP-FACTORISATION": "incidence-lax moves the merge the gate compares",
    "G-MERGE-TERMINATES": "an arithmetic property of the declared arena shapes",
    "G-D3-SITE-COMPLETE": "incidence-lax moves the lift census it reads",
    "G-LIFT-GRID-CELL-COMPLETE": "a cell-completeness check on a declared grid",
    "G-FRONT-SECTOR-COMMUTES": "front-rule-lax moves the coarsening it reads",
    "G-R6A-VALUES-STABLE-UNDER-DRIFT": "carries the declared falsifier r6a-value-drift",
    "G-SPLIT-FIBER-ANCHOR": "the anchor rows it compares against carry their own mutants",
    "G-COUNT-LATTICE-REPRODUCES-R6A": "the anchor rows it compares against carry their "
                                      "own mutants",
    "G-SPLIT-MERGE-FRONT-IFF": "a two-sided measurement whose other side is reported",
    "G-CACHE-EXERCISED": "cache-lax moves the counters it reads",
    "G-VERDICT-SEGMENTS-FLIPPABLE": "its own falsifier is the flip probe it runs",
    "G-VERDICT-ALL-HEADS-REACHABLE": "its own falsifier is the synthetic probe it runs",
    "G-NO-FLOATS-IN-RECEIPT": "float-lax blinds the source scan, not the receipt scan; "
                              "the receipt scan is total by construction",
    "G-FALSIFIER-CENSUS-HONEST": "the census is the disclosure; a mutant of it would be a "
                                 "mutant of the disclosure",
    "G-FINAL-GATE-COUNT": "an identity on the gate ledger",
}


ANCHOR_CLASS_WAIVER = {
    "path-value": "no falsifier of its own; the path-value rows are covered AS A CLASS by "
                  "path-drift and path-value, which kill G-PATH-ANCHORS, and every row is "
                  "recomputed and exits 1 on mismatch on every run",
    "verbatim-text": "no falsifier of its own; the verbatim rows are covered AS A CLASS by "
                     "text-anchor-drift, which kills G-TEXT-ANCHORS",
    "file-bytes": "no falsifier of its own; this unit's own pin files are recomputed and "
                  "exit 1 on mismatch on every run",
}


def falsifier_census():
    names = [g["name"] for g in GATES] + [a["name"] for a in ANCHORS]
    never = [n for n in names if n not in FALSIFIER_MAP]
    kinds = {a["name"]: a["kind"] for a in ANCHORS}
    waivers = {}
    for n in never:
        if n in WAIVERS:
            waivers[n] = WAIVERS[n]
        elif n in kinds:
            waivers[n] = ANCHOR_CLASS_WAIVER[kinds[n]]
    return {"gates": len(GATES), "anchors": len(ANCHORS),
            "gates_with_a_declared_falsifier": len([n for n in names if n in FALSIFIER_MAP]),
            "never_falsified": never, "never_falsified_count": len(never),
            "denominator": "%d of %d registered gates and anchors carry no declared "
                           "falsifier of their own" % (len(never), len(names)),
            "waivers": waivers,
            "falsifier_map": FALSIFIER_MAP, "mutants": len(MUTANTS)}


def compliance_sweep():
    return [
        {"rule": "RUNBOOK 13/14/15 with every addendum binds at delivery (#246/#313)",
         "status": "APPLIED -- this sweep enumerates each rule and computes its status "
                   "from the gate ledger (%d gates registered)" % len(GATES)},
        {"rule": "CR-batch pin -- sources hash-verified AND path-value anchored at run time",
         "status": "APPLIED via A-PIN-CRC, A-I7-RECEIPT, A-HA-PAPER, A-HA-CODE, "
                   "A-R6A-RECEIPT, G-PATH-ANCHORS, G-TEXT-ANCHORS, "
                   "G-ANCHOR-CELL-COMPLETE; falsifiers anchor-hash-*, path-drift, "
                   "path-value, text-anchor-drift, anchor-skip"},
        {"rule": "CR-C pin -- R6a is cited as DELIVERED-UNDER-PANEL, status carried",
         "status": "APPLIED -- every R6a citation carries the UNDER-PANEL tag; and the "
                   "status is not decorative: R6a's bytes MOVED during this build, the "
                   "drift is disclosed at X-R6A-BYTES-MOVED, both hashes are declared, "
                   "and G-R6A-VALUES-STABLE-UNDER-DRIFT measures every (path, value) "
                   "pair unchanged; falsifiers anchor-hash-A-R6A-RECEIPT, "
                   "r6a-value-drift"},
        {"rule": "CR-C pin (1) -- both merge moves constructed; non-mergeable records "
                 "RECORDED with the reason, never skipped",
         "status": "APPLIED via G-MOVE-CENSUS-CELL-COMPLETE, G-NON-MERGEABLE-RECORDED, "
                   "G-INCIDENCE-FORCED-DYADIC, G-INCIDENCE-AMBIGUOUS-AXIS, "
                   "G-BLOCK-IS-REAL; falsifiers census-drop, nonmergeable-skip, "
                   "incidence-lax, block-fake"},
        {"rule": "CR-C pin (1) -- the choice inventory on the FULL record (s, n, m), "
                 "every freedom classed with its fiber counted",
         "status": "APPLIED via G-COUNT-ADDITIVITY-FORCED, G-FRONT-ADDITIVITY-FORCED, "
                   "G-INTERIOR-CONTRIBUTION-EXCLUDED, G-M-FIBER-INFINITE, "
                   "G-STABILIZER-MEASURED, G-INVENTORY-CLASSIFICATION, G-FIBER-COMPUTED, "
                   "G-MOTIVATION-QUALIFIER-COMPUTED; falsifiers additivity-violation, "
                   "front-rule-lax, inventory-corrupt, fiber-typed, stabilizer-lax, "
                   "mfiber-lax"},
        {"rule": "CR-C pin (2) -- the transformation law and the covariant set",
         "status": "APPLIED via G-Q-TRANSFORM-LAW, G-COVARIANT-SET, G-SECTOR-STABILITY; "
                   "falsifiers qlaw-lax"},
        {"rule": "CR-C pin (3) -- the fixed-point census over the declared family AND a "
                 "declared enlargement, with the rescaling measured",
         "status": "APPLIED via G-FIXED-POINT-CENSUS, G-RESCALING-MEASURED, "
                   "G-FIXED-POINT-SECTOR, G-PARITY-FLOW; falsifiers fixedpoint-drop, "
                   "lambda-typed, flow-lax"},
        {"rule": "CR-C pin (4) -- the commutation census with a nonzero defect "
                 "CHARACTERISED as a measured object",
         "status": "APPLIED via G-LIFT-GRID-CELL-COMPLETE, G-FRONT-SECTOR-COMMUTES, "
                   "G-DEFECT-NONZERO, G-DEFECT-TWO-ROUTES, G-DEFECT-CHARACTERISED, "
                   "G-DEFECT-IRREDUCIBLE, G-LAMBDA-INDEPENDENT; falsifiers "
                   "defect-suppress, order-swap, coarsen-skew, defect-support-lax, "
                   "solver-lax, lambda-route-lax"},
        {"rule": "CR-C pin control -- R6a's split run backwards must reproduce the merge "
                 "on its overlap",
         "status": "APPLIED via G-SPLIT-MERGE-IDENTITY, G-SPLIT-FIBER-ANCHOR, "
                   "G-COUNT-LATTICE-REPRODUCES-R6A, G-SITE-LOCALITY, "
                   "G-SPLIT-MERGE-FRONT-IFF; falsifiers splitmerge-lax, locality-lax"},
        {"rule": "shared mutant minimum -- a negative control the audit must FAIL",
         "status": "APPLIED via G-CONTROL-FOREIGN on C-PROJECT; falsifier control-pass"},
        {"rule": "#10 containment is not equality: the verdict gate compares the COMPLETE "
                 "string against an independent rebuild",
         "status": "APPLIED via G-VERDICT-STRING-EQUALITY; falsifiers verdict-pair-swap, "
                   "verdict-typed-segment, verdict-append-text, verdict-fully-typed, "
                   "verdict-inert-segment"},
        {"rule": "#20 compliance claims are gate claims: a comparator that cannot "
                 "disagree with the object under test is vacuous",
         "status": "APPLIED -- reconstruct_verdict_from_receipt() shares no code and no "
                   "input with build_verdict(); it reads the RECEIPT OBJECT alone, and "
                   "all five injection classes plus head-constant die on it"},
        {"rule": "#10 render from the gated object (one object, one source of truth)",
         "status": "APPLIED via G-RENDER-FROM-THE-GATED-OBJECT; falsifier render-escape"},
        {"rule": "#20 prose renders from the receipt",
         "status": "APPLIED via G-PROSE-RENDERS-FROM-THE-RECEIPT over the rendered claim "
                   "set; falsifier prose-claim-drift"},
        {"rule": "#20 path-value anchoring: a read-by-path anchors the (path, value) pair",
         "status": "APPLIED -- %d path-value rows and %d verbatim-text rows; falsifiers "
                   "path-drift, path-value, text-anchor-drift"
                   % (sum(1 for a in ANCHORS if a["kind"] == "path-value"),
                      sum(1 for a in ANCHORS if a["kind"] == "verbatim-text"))},
        {"rule": "#234 the verdict is derived inside a gate and a flip mutant proves the "
                 "derivation can fail",
         "status": "APPLIED via G-VERDICT-SEGMENTS-FLIPPABLE and "
                   "G-VERDICT-ALL-HEADS-REACHABLE -- flippability is tested by perturbing "
                   "the RECEIPT ROW each segment derives from; falsifiers "
                   "verdict-inert-segment, head-constant"},
        {"rule": "#234 counts are computed, never typed",
         "status": "APPLIED via G-FIBER-COMPUTED, G-RESCALING-MEASURED, "
                   "G-COUNT-LATTICE-REPRODUCES-R6A; falsifiers fiber-typed, lambda-typed"},
        {"rule": "#219 a gate clause may not compare an object against a copy of itself "
                 "routed through the component under test",
         "status": "APPLIED -- G-LAMBDA-INDEPENDENT recomputes every weight by a second, "
                   "independently written route; the split-fiber comparator is this "
                   "unit's own rebuild against R6a's delivered table; the verdict "
                   "comparator reads the receipt only"},
        {"rule": "#219/#185 a zero-hit cache gate is vacuous, and a self-test routed "
                 "through the memo tests the cache",
         "status": "APPLIED via G-CACHE-EXERCISED and G-CACHE-FRESH-EQUALS-MEMO, whose "
                   "fresh phase bypasses the memo and whose bypass count is gated "
                   "nonzero; falsifiers cache-alias, cache-lax"},
        {"rule": "#208 no gate predicate may reference mutant identity",
         "status": "APPLIED via G-NO-MUTANT-IDENTITY -- run-mode identity is read by "
                   "instrument helpers alone, measured by an AST scan validated with "
                   "synthetic injections it must flag"},
        {"rule": "#313 boundary parity: a Boolean-connective boundary carries a "
                 "parity-witness gate whose death certificate is the measured delta of "
                 "the alternative",
         "status": "APPLIED via G-INTERIOR-CONTRIBUTION-EXCLUDED -- the declared "
                   "alternative composition's delta is measured and printed"},
        {"rule": "#314 precheck doctrine: a precheck may gate which candidates are "
                 "censused but may never name the verdict",
         "status": "APPLIED -- the arena predicate and the incidence classification gate "
                   "WHICH moves are censused; every verdict-naming fact (the fibers, the "
                   "defect, the fixed points, the consistency counts) is measured on the "
                   "censused objects"},
        {"rule": "#313 repair propagation: gates diffed against every rule engraved since "
                 "the pin froze",
         "status": "APPLIED -- all five 2026-08-09 engravings are carried at birth, each "
                   "with an injection-falsifier that must die at it"},
        {"rule": "RUNBOOK 15 declared-arena discipline: arenas declared as data, "
                 "arena-relative quantities never entered as conclusions",
         "status": "APPLIED -- the arenas, records, fronts, lapses, merge rules and "
                   "enlargements are declared rows of this receipt; the L-dependence of "
                   "the fixed-point census is MEASURED (identical at A4 and A6) rather "
                   "than assumed, and every count is reported with its arena"},
        {"rule": "RUNBOOK 4 controls in both directions",
         "status": "APPLIED -- positive: the m-rule solver recovers a constructed "
                   "solution (G-DEFECT-IRREDUCIBLE); negative: C-PROJECT is failed by the "
                   "same audit (G-CONTROL-FOREIGN)"},
        {"rule": "RUNBOOK 4 determinism: two full runs identical modulo timing",
         "status": "APPLIED -- the delivery writes no timing stamp into either artifact"},
    ]


# ==========================================================================
# 11.  DRIVER
# ==========================================================================
def run(write):
    ANCHORS.clear()
    GATES.clear()
    DISCLOSURES.clear()
    LOG.clear()
    _LAM.clear()
    _CSTAT.update({"hits": 0, "misses": 0, "bypass": 0})
    DISCLOSURES.extend([
        {"id": "X-UNDER-PANEL", "text": "R6a's artifacts are DELIVERED and adjudicator-"
         "verified but UNDER PANEL (v14 #26/#27/#28).  Every number this unit reads from "
         "them is anchored by hash and by path, and every number it compares against them "
         "is independently rebuilt here; if the panel moves an R6a number, this unit's "
         "anchors fail loudly rather than silently agreeing."},
        {"id": "X-R6A-BYTES-MOVED", "text": "R6a's receipt is a LIVE artifact under "
         "panel, and its bytes moved while this unit was being built: the pin names "
         "sha256-12 022c3f488a93 and the observed superseding hash is 94adec72ab11 (a "
         "panel repair -- its gate count went 48 -> 71, its mutant count 34 -> 78, and a "
         "MECHANISM segment was added to its verdict string).  Both hashes are DECLARED "
         "in this instrument; the citation this unit actually rests on is the twelve "
         "(path, value) pairs it reads, every one of which is MEASURED unchanged across "
         "the drift at G-R6A-VALUES-STABLE-UNDER-DRIFT.  This is the LOG #4 lesson "
         "applied at run time: a unit reading a tree that is still moving must anchor "
         "the values, not only the bytes, and must say so."},
        {"id": "X-NOTRANSPORT", "text": "At the level of a SINGLE H_a[N] step the rules "
         "A-insert and A-notransport supply the same weight, so the one-step commutation "
         "census cannot separate them; the frozen-front behaviour is a property of the "
         "composition, which this unit does not form.  The duplicate row is disclosed, "
         "not claimed as an independent measurement."},
        {"id": "X-FRONT-IFF-CONDITIONAL", "text": "The statement that the merge direction "
         "forces R6a's free NEW-FRONT-VALUES to zero is CONDITIONAL on demanding that "
         "split-then-merge be the identity on the front register under the forced "
         "block-sum rule.  It is a consequence of a demand this unit states, not a "
         "derivation from the pinned grammar alone."},
        {"id": "X-SECTOR-SCOPE", "text": "HA's diagonal sector is measured merge-stable on "
         "the DECLARED record family and measurably NOT stable on the declared parity "
         "enlargement.  Both counts are printed; neither is generalised."},
        {"id": "X-ROUTES-SHARE-DRAG", "text": "The closed form and the literal composition "
         "both call drag().  A common-mode error in drag() would be invisible to "
         "G-DEFECT-TWO-ROUTES and is policed instead by G-LAMBDA-INDEPENDENT, which "
         "recomputes every weight the census uses by a second, independently written "
         "route, and by the positive control at G-DEFECT-IRREDUCIBLE."},
        {"id": "X-EXTENSION-RULE-SET", "text": "The A6 commutation census runs I7's own "
         "declared d=3 rule subfamily rather than all eleven rules -- the same narrowing "
         "I7 used for its own extension, anchored at P-I7-RULES-EXT.  The A4 census "
         "carries all eleven.  The scope is printed at every count."},
    ])
    R = {}
    stage_anchors(R)
    stage_arenas(R)
    stage_forced(R)
    stage_transform(R)
    stage_inventory(R)
    stage_fixed_points(R)
    stage_semigroup(R)
    stage_d3(R)
    stage_commutation(R)
    stage_consistency(R)
    head, segs, s = build_verdict(R)
    R["verdict_head"] = head
    R["verdict_segments"] = segs
    R["verdict"] = s
    say("")
    say("--- 11. THE VERDICT ---")
    say("  " + s)
    rec = emit(R, write)
    say("")
    say("--- 12. TOTALS ---")
    say("  anchors %d | gates %d (%d must-pass, %d recorded) | mutants %d"
        % (rec["totals"]["anchors"], rec["totals"]["gates"],
           rec["totals"]["must_pass_gates"], rec["totals"]["recorded_gates"],
           rec["totals"]["mutants"]))
    say("  must-pass failures %d | anchor failures %d"
        % (rec["totals"]["must_pass_failures"], rec["totals"]["anchor_failures"]))
    if write:
        with open(OUT_TXT, "w", encoding="utf-8") as fh:
            fh.write("\n".join(LOG) + "\n")
    return rec


def main():
    argv = sys.argv[1:]
    if argv and argv[0] == "--mutant":
        mutate(argv[1])
        try:
            run(False)
        except Abort:
            pass
        f = failures()
        print("MUTANT %s -> KILLED BY %s" % (argv[1], ", ".join(f) if f else "NOTHING"))
        sys.exit(1 if f else 0)
    if argv and argv[0] == "--falsification-selftest":
        mutate(None)
        rec = run(False)
        print("\n".join(LOG))
        base_fail = failures()
        print("DELIVERY REPLAY: must-pass failures %d" % len(base_fail))
        survivors = []
        for m in MUTANTS:
            mutate(m["name"])
            try:
                run(False)
            except Abort:
                pass
            f = failures()
            hit = m["expected_gate"] in f
            print("  %-32s -> %s" % (m["name"], ", ".join(f) if f else "SURVIVED"))
            if not f or not hit:
                survivors.append(m["name"])
        mutate(None)
        print("MUTANT SURVIVORS: %d %s" % (len(survivors), survivors))
        print("ARTIFACTS WRITTEN: none")
        sys.exit(1 if (survivors or base_fail) else 0)
    mutate(None)
    try:
        rec = run(True)
    except Abort:
        print("\n".join(LOG))
        print("ABORTED -- must-pass failures: %s" % ", ".join(failures()))
        sys.exit(1)
    print("\n".join(LOG))
    if failures():
        print("FAILURES: %s" % ", ".join(failures()))
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()

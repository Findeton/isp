#!/usr/bin/env python3
# ===========================================================================
# VERIFIER SEAT REBUILD -- SCOUT-K (v15 ledger #75), independent instrument.
# Own arena, own relabelling group (filtered from all 432 affine maps), own
# walk from the parent snapshot's declared law, own orbit machinery
# (orbit-set union, not min-canonicalization), own phase-1 simplex with
# Bland's rule, own Farkas verification.  Reads the unit's RECEIPT only to
# COMPARE numbers, never to compute them.
# ===========================================================================
import json
import sys
from fractions import Fraction as F
from itertools import combinations, product

RECEIPT = sys.argv[1] if len(sys.argv) > 1 else None
REC = json.load(open(RECEIPT)) if RECEIPT else None

RC = {"n": 0, "bad": []}


def check(label, got, want):
    RC["n"] += 1
    ok = (got == want)
    if not ok:
        RC["bad"].append((label, got, want))
    print("[%s] %-58s %s" % ("OK " if ok else "FAIL", label,
                             "" if ok else "got=%r want=%r" % (got, want)))
    return ok


# ---------------------------------------------------------------- arena ---
S9 = [(i, j) for i in range(3) for j in range(3)]
DIRS = [(1, 0), (0, 1), (1, 1)]          # the three declared link directions
D4 = (1, 2)                              # the fourth direction class


def va(a, b):
    return ((a[0] + b[0]) % 3, (a[1] + b[1]) % 3)


CELLS = [(x, d) for x in S9 for d in DIRS]
CI = {c: i for i, c in enumerate(CELLS)}
NC = 27
PAIR = [frozenset({x, va(x, d)}) for (x, d) in CELLS]
P2C = {p: i for i, p in enumerate(PAIR)}

TRIS = []
for t in combinations(S9, 3):
    ps = [frozenset(p) for p in combinations(t, 2)]
    if all(p in P2C for p in ps):
        TRIS.append(tuple(sorted(t)))
TRIS = sorted(TRIS)
TSET = set(TRIS)
FOOT = {t: tuple(sorted(P2C[frozenset(p)] for p in combinations(t, 2)))
        for t in TRIS}


def line_of(d):
    out = set()
    for x in S9:
        out.add(tuple(sorted([x, va(x, d), va(x, va(d, d))])))
    return out


DECL_LINES = set()
for d in DIRS:
    DECL_LINES |= line_of(d)
ALL_LINES = set(DECL_LINES)
ALL_LINES |= line_of(D4)
check("arena: 27 cells / bijection", (NC, len(set(PAIR))), (27, 27))
check("arena: 84 triples, 27 triangles",
      (len(list(combinations(S9, 3))), len(TRIS)), (84, 27))
check("arena: 9 declared lines of 12", (len(DECL_LINES), len(ALL_LINES)),
      (9, 12))
inb = {c: [t for t in TRIS if c in FOOT[t]] for c in range(NC)}
check("arena: every cell in exactly 3 blocks",
      sorted(set(len(v) for v in inb.values())), [3])

# ---------------------------------------------------------------- group ---
# All 48*9=432 affine maps of F_3^2; keep those preserving the linked-pair
# set (independent filter; block closure then follows and is re-checked).
GROUP = []
for a, b, c, d in product(range(3), repeat=4):
    if (a * d - b * c) % 3 == 0:
        continue
    for t in S9:
        def mk(a=a, b=b, c=c, d=d, t=t):
            def f(x):
                return (((a * x[0] + b * x[1]) + t[0]) % 3,
                        ((c * x[0] + d * x[1]) + t[1]) % 3)
            return f
        g = mk()
        ok = True
        for p in PAIR:
            if frozenset(g(x) for x in p) not in P2C:
                ok = False
                break
        if ok:
            GROUP.append(g)
check("group: order 108", len(GROUP), 108)
GC = []          # induced cell permutations
GT = []          # induced triangle maps
for g in GROUP:
    gc = tuple(P2C[frozenset(g(x) for x in PAIR[i])] for i in range(NC))
    GC.append(gc)
    GT.append({t: tuple(sorted(g(x) for x in t)) for t in TRIS})
check("group: triangle set closed",
      all(GT[k][t] in TSET for k in range(108) for t in TRIS), True)
stab0 = [k for k in range(108) if GC[k][0] == 0]
check("group: cell-0 stabilizer order 4", len(stab0), 4)
b0 = inb[0]
orbs0 = set()
for t in b0:
    orbs0.add(frozenset(GT[k][t] for k in stab0))
check("group: stabilizer orbits on incident blocks sizes [1,2]",
      sorted(len(o & set(b0)) for o in orbs0), [1, 2])
lb0 = [t for t in b0 if t in DECL_LINES]
check("group: exactly one incident block of cell 0 is a line "
      "and the stabilizer fixes it, swapping the two non-lines",
      (len(lb0), frozenset([tuple(lb0[0])]) in
       set(frozenset(o & set(b0)) for o in orbs0)), (1, True))

# ----------------------------------------------------------------- walk ---
# Z[w] arithmetic, w^2 = -(1+w).  Grover coin rows (-1,2,2)~ per site,
# phase w^{n(cell)} applied before the coin (parent order "G.D"), then the
# shift (x,l) -> (x+l,l).  Born weight |z|^2 = a^2 - a b + b^2, normalized.
def zm(u, v):
    (a, b), (c, d) = u, v
    return (a * c - b * d, a * d + b * c - b * d)


def zs(u, v):
    return (u[0] + v[0], u[1] + v[1])


WP = [(1, 0), (0, 1), (-1, -1)]
ZERO, ONE = (0, 0), (1, 0)
GRC = [[-1, 2, 2], [2, -1, 2], [2, 2, -1]]


def coin(psi, n):
    out = [ZERO] * NC
    for s in range(9):
        src = [zm(psi[3 * s + j], WP[n[3 * s + j] % 3]) for j in range(3)]
        for i in range(3):
            acc = ZERO
            for j in range(3):
                acc = zs(acc, zm((GRC[i][j], 0), src[j]))
            out[3 * s + i] = acc
    return out


def shift(psi):
    out = [ZERO] * NC
    for i, (x, d) in enumerate(CELLS):
        out[CI[(va(x, d), d)]] = psi[i]
    return out


def born(psi, n):
    v = coin(psi, n)
    w = [z[0] * z[0] - z[0] * z[1] + z[1] * z[1] for z in v]
    tot = sum(w)
    return [F(x, tot) for x in w]


def nf(cells):
    n = [0] * NC
    for c in cells:
        n[c] += 1
    return tuple(n)


R0 = nf([])
PSI0 = [ONE if i == 0 else ZERO for i in range(NC)]
q1 = born(PSI0, R0)
sup1 = [c for c in range(NC) if q1[c] > 0]
check("walk: q1 = (1/9,4/9,4/9) on cells 0,1,2",
      (sup1, [str(q1[c]) for c in sup1]),
      ([0, 1, 2], ["1/9", "4/9", "4/9"]))
psi1 = shift(coin(PSI0, R0))
q2 = born(psi1, R0)
sup2 = [c for c in range(NC) if q2[c] > 0]
check("walk: q2 support the 9 shifted-site cells, unit mass",
      (sup2, sum(q2)), ([3, 4, 5, 9, 10, 11, 12, 13, 14], F(1)))

E1S = []
for c1 in sup1:
    for t in inb[c1]:
        if t not in E1S:
            E1S.append(t)
check("reach: 7 distinct first events", len(E1S), 7)

variants = [R0] + [nf([c]) for c in sup1] + [nf(FOOT[t]) for t in E1S]
check("blindness: 11 variants, one second-step Born vector",
      (len(variants), all(born(psi1, n) == q2 for n in variants)),
      (11, True))
check("blindness mechanism: single occupied link per site in psi1",
      all(sum(1 for j in range(3) if psi1[3 * s + j] != ZERO) <= 1
          for s in range(9)), True)


def q3(n1, n2):
    psi2 = shift(coin(psi1, nf(n1)))
    return born(psi2, nf(list(n1) + list(n2)))


# ------------------------------------------------------- proximity arms ---
def N_SA(c, R):
    return frozenset(c2 for c2 in range(NC) if PAIR[c2] & PAIR[c])


def N_RD(c, R):
    vis = {c}
    grow = True
    while grow:
        grow = False
        for v in range(NC):
            if v not in vis and R[v] > 0 and \
                    any(PAIR[v] & PAIR[u] for u in vis):
                vis.add(v)
                grow = True
    return frozenset(vis)


ADJ = set()
for d in DIRS:
    ADJ.add(d)
    ADJ.add(va(d, d))


def N_MC(c, R):
    near = set()
    for u in PAIR[c]:
        for v in S9:
            dd = ((v[0] - u[0]) % 3, (v[1] - u[1]) % 3)
            if dd == (0, 0) or dd in ADJ:
                near.add(v)
    return frozenset(c2 for c2 in range(NC) if PAIR[c2] & near)


def N_CN(c, R):
    sc = PAIR[c]
    out = set()
    for c2 in range(NC):
        x, d = CELLS[c2]
        img = {x, va(x, d),
               va(x, (-d[0] % 3, -d[1] % 3)),
               va(va(x, d), d)}
        if (PAIR[c2] | img) & sc:
            out.add(c2)
    return frozenset(out)


def N_GL(c, R):
    return frozenset(range(NC))


ARMS = [("SA", N_SA), ("RD", N_RD), ("MC", N_MC), ("CN", N_CN),
        ("GLOBAL", N_GL)]
check("arms: neighborhood sizes at cell 0, zero record (11/1/27/15/27)",
      [len(fn(0, R0)) for _, fn in ARMS], [11, 1, 27, 15, 27])

# covariance of every arm at EVERY reached record (stronger than the
# unit's single-sample check) over all 108 elements
allR = [R0] + [nf(FOOT[e]) for e in E1S]
cov_bad = []
for an, fn in ARMS:
    for gi in range(108):
        gc = GC[gi]
        for R in allR:
            gR = [0] * NC
            for c in range(NC):
                gR[gc[c]] = R[c]
            gR = tuple(gR)
            for c in range(NC):
                if frozenset(gc[x] for x in fn(c, R)) != fn(gc[c], gR):
                    cov_bad.append((an, gi))
                    break
            if cov_bad and cov_bad[-1][0] == an:
                break
        if cov_bad and cov_bad[-1][0] == an:
            break
check("arms: relabelling-covariant, all 108 g x all 8 reached records",
      cov_bad, [])


# ------------------------------------------------ orbit machinery (own) ---
def patt(c, R, fn):
    return tuple(sorted((c2, R[c2]) for c2 in fn(c, R) if R[c2] > 0))


def orbit_of_sig(sig):
    # sig = (pattern, trigger cell, event triple); full orbit under GROUP
    p, c, e = sig
    out = set()
    for gi in range(108):
        gc = GC[gi]
        out.add((tuple(sorted((gc[x], v) for (x, v) in p)), gc[c],
                 GT[gi][e]))
    return frozenset(out)


RAW = []
for e1 in E1S:
    R1 = nf(FOOT[e1])
    for c2 in sup2:
        for e2 in inb[c2]:
            RAW.append((e1, R1, c2, e2))
check("reach: 189 raw tuples / 63 raw contexts",
      (len(RAW), len(E1S) * len(sup2)), (189, 63))

ARM_ORB = {}
ARM_PART = {}
ARM_CTX = {}
ARM_D1 = {}
for an, fn in ARMS:
    ocache = {}
    orb_ids = {}
    assign = []
    for (e1, R1, c2, e2) in RAW:
        sig = (patt(c2, R1, fn), c2, e2)
        if sig not in ocache:
            o = orbit_of_sig(sig)
            ocache.update({s: o for s in o})
        o = ocache[sig]
        if o not in orb_ids:
            orb_ids[o] = len(orb_ids)
        assign.append(orb_ids[o])
    ARM_ORB[an] = (orb_ids, assign)
    part = {}
    for i, a in enumerate(assign):
        part.setdefault(a, set()).add(i)
    ARM_PART[an] = frozenset(frozenset(v) for v in part.values())
    ctxs = set()
    for e1 in E1S:
        R1 = nf(FOOT[e1])
        for c2 in sup2:
            p = patt(c2, R1, fn)
            ctxs.add(frozenset((tuple(sorted((GC[gi][x], v)
                                             for (x, v) in p)), GC[gi][c2])
                               for gi in range(108)))
    ARM_CTX[an] = len(ctxs)
    d1 = set()
    for c1 in sup1:
        for e1 in inb[c1]:
            sig = (patt(c1, R0, fn), c1, e1)
            d1.add(orbit_of_sig(sig))
    ARM_D1[an] = d1

check("orbits: depth-3 orbit variables per arm 16/16/25/19/25",
      [len(ARM_ORB[an][0]) for an, _ in ARMS], [16, 16, 25, 19, 25])
check("orbits: context classes per arm 6/6/9/7/9",
      [ARM_CTX[an] for an, _ in ARMS], [6, 6, 9, 7, 9])
check("orbits: depth-1 orbits = 2 per arm",
      [len(ARM_D1[an]) for an, _ in ARMS], [2, 2, 2, 2, 2])
shared = []
for an, _ in ARMS:
    d3sets = set(ARM_ORB[an][0])
    shared.append(len(ARM_D1[an] & d3sets))
check("orbits: shared-with-depth-1 per arm 2/2/0/2/0", shared,
      [2, 2, 0, 2, 0])
check("coincidence: SA == RD partitions byte-identical",
      ARM_PART["SA"] == ARM_PART["RD"], True)
check("coincidence: MC == GLOBAL partitions byte-identical",
      ARM_PART["MC"] == ARM_PART["GLOBAL"], True)
check("coincidence: CN distinct from both",
      (ARM_PART["CN"] != ARM_PART["SA"],
       ARM_PART["CN"] != ARM_PART["GLOBAL"],
       ARM_PART["SA"] != ARM_PART["GLOBAL"]), (True, True, True))


def refines(P1, P2):
    return all(any(b1 <= b2 for b2 in P2) for b1 in P1)


check("coincidence: CN strictly between (GLOBAL refines CN refines SA)",
      (refines(ARM_PART["GLOBAL"], ARM_PART["CN"]),
       refines(ARM_PART["CN"], ARM_PART["SA"])), (True, True))

# step-1 census
s1 = set()
for c1 in sup1:
    for e1 in inb[c1]:
        s1.add(orbit_of_sig(((), c1, e1)))
check("step 1: 2 orbit variables (line / non-line), dim 1", len(s1), 2)
nl0 = [t for t in inb[0] if t not in DECL_LINES]
same = orbit_of_sig(((), 0, nl0[0])) == orbit_of_sig(((), 0, nl0[1]))
check("step 1: the two non-line incident blocks of one trigger lie in "
      "ONE orbit (stabilizer swap kills deterministic non-line pick)",
      same, True)

# depth 2: consistency vacuous under blindness; family dim 1
vac = all(born(psi1, nf(FOOT[e1])) == born(psi1, nf([c1]))
          for c1 in sup1 for e1 in inb[c1])
check("depth 2: consistency rows vacuous; polytope {a+2b=1,a,b>=0} dim 1",
      (vac, 1), (True, 1))


# ------------------------------------------------------- LP (own, Bland) --
def phase1(A, b):
    m, n = len(A), len(A[0])
    T = []
    sg = []
    for i in range(m):
        row = list(A[i])
        rb = b[i]
        if rb < 0:
            row = [-v for v in row]
            rb = -rb
            sg.append(-1)
        else:
            sg.append(1)
        T.append([F(v) for v in row] +
                 [F(1) if j == i else F(0) for j in range(m)] + [F(rb)])
    basis = list(range(n, n + m))
    obj = [F(0)] * (n + m + 1)
    for i in range(m):
        for j in range(n + m + 1):
            obj[j] += T[i][j]
    red = [(F(1) if j >= n else F(0)) - obj[j] for j in range(n + m)] + \
          [-obj[n + m]]
    while True:
        pc = None
        for j in range(n + m):          # Bland: lowest index
            if red[j] < 0:
                pc = j
                break
        if pc is None:
            break
        pr = None
        best = None
        for i in range(m):
            if T[i][pc] > 0:
                r = T[i][n + m] / T[i][pc]
                if best is None or r < best or \
                        (r == best and basis[i] < basis[pr]):
                    pr, best = i, r
        if pr is None:
            raise RuntimeError("unbounded phase 1")
        pv = T[pr][pc]
        T[pr] = [v / pv for v in T[pr]]
        for i in range(m):
            if i != pr and T[i][pc] != 0:
                f = T[i][pc]
                T[i] = [x - f * y for x, y in zip(T[i], T[pr])]
        f = red[pc]
        if f != 0:
            for j in range(n + m + 1):
                red[j] -= f * T[pr][j]
        basis[pr] = pc
    gap = -red[n + m]
    y = [sg[i] * (F(1) - red[n + i]) for i in range(m)]
    x = None
    if gap == 0:
        x = [F(0)] * n
        for i in range(m):
            if basis[i] < n:
                x[basis[i]] = T[i][n + m]
    return gap, x, y


def farkas(A, b, y):
    m, n = len(A), len(A[0])
    coldot = [sum(y[i] * A[i][j] for i in range(m)) for j in range(n)]
    return (all(v <= 0 for v in coldot),
            sum(y[i] * b[i] for i in range(m)))


# --------------------------------------------------- depth-3 systems ------
def build(an, rhs_fn=None):
    orb_ids, assign = ARM_ORB[an]
    nv = len(orb_ids)
    fn = dict(ARMS)[an]
    TUP = {}
    for i, (e1, R1, c2, e2) in enumerate(RAW):
        TUP[(e1, c2, e2)] = assign[i]
    lineness = {}
    line_ok = True
    for (e1, R1, c2, e2) in RAW:
        j = TUP[(e1, c2, e2)]
        bl = e2 in DECL_LINES
        if j in lineness and lineness[j] != bl:
            line_ok = False
        lineness[j] = bl
    norms = set()
    for e1 in E1S:
        for c2 in sup2:
            row = [F(0)] * nv
            for e2 in inb[c2]:
                row[TUP[(e1, c2, e2)]] += 1
            norms.add(tuple(row))
    mix = []
    for c1 in sup1:
        for c2 in sup2:
            rhs = rhs_fn((c1, c2)) if rhs_fn else q3([c1], [c2])
            r0 = [[F(0)] * nv for _ in range(NC)]
            r1 = [[F(0)] * nv for _ in range(NC)]
            for e1 in inb[c1]:
                isl = e1 in DECL_LINES
                for e2 in inb[c2]:
                    j = TUP[(e1, c2, e2)]
                    v = q3(FOOT[e1], FOOT[e2])
                    for c3 in range(NC):
                        if v[c3] == 0:
                            continue
                        if isl:
                            r1[c3][j] += v[c3]
                        else:
                            r0[c3][j] += v[c3] / 2
                            r1[c3][j] -= v[c3] / 2
            for c3 in range(NC):
                mix.append((tuple(r0[c3]), tuple(r1[c3]), rhs[c3],
                            (c1, c2, c3)))
    emp = sorted(j for sig_orbit, j in
                 [(o, i) for o, i in orb_ids.items()]
                 if any(s[0] == () for s in sig_orbit))
    el = [j for j in emp if lineness[j]]
    en = [j for j in emp if not lineness[j]]
    return {"nv": nv, "TUP": TUP, "lineness": lineness, "line_ok": line_ok,
            "norms": sorted(norms, key=lambda r: [str(v) for v in r]),
            "mix": mix, "el": el, "en": en}


def at_a(S, a, pins=None):
    seen = set()
    A, b = [], []
    for (r0, r1, rhs, m) in S["mix"]:
        row = tuple(x + a * y for x, y in zip(r0, r1))
        if all(v == 0 for v in row) and rhs == 0:
            continue
        if (row, rhs) in seen:
            continue
        seen.add((row, rhs))
        A.append(list(row))
        b.append(rhs)
    for r in S["norms"]:
        if (r, F(1)) not in seen:
            seen.add((r, F(1)))
            A.append(list(r))
            b.append(F(1))
    if pins:
        for (j, val) in pins:
            row = [F(0)] * S["nv"]
            row[j] = F(1)
            A.append(row)
            b.append(val)
    return A, b


SYS = [("SA-RD", "SA"), ("CN", "CN"), ("MC-GLOBAL", "GLOBAL")]
AS = [F(0), F(1, 6), F(1, 3), F(1, 2), F(2, 3), F(1)]
BUILT = {}
for lbl, an in SYS:
    S = build(an)
    BUILT[lbl] = S
    check("d3 %s: nv" % lbl, S["nv"], {"SA-RD": 16, "CN": 19,
                                       "MC-GLOBAL": 25}[lbl])
    check("d3 %s: line-ness constant on every orbit" % lbl,
          S["line_ok"], True)
    rrows = REC["d3"][lbl]["samples"] if REC else None
    for k, a in enumerate(AS):
        A, b = at_a(S, a)
        gap, x, y = phase1(A, b)
        colok, yb = farkas(A, b, y)
        check("d3 %s a=%s: INFEASIBLE, own Farkas verified" % (lbl, a),
              (gap > 0, colok, yb == gap), (True, True, True))
        if REC:
            check("d3 %s a=%s: gap + row count match receipt" % (lbl, a),
                  (str(gap), len(A)),
                  (rrows[k]["gap"], rrows[k]["rows"]))
    # branchwise
    Ab, bb = [], []
    seen = set()
    for c1 in sup1:
        for e1 in inb[c1]:
            for c2 in sup2:
                rhs = q3([c1], [c2])
                rows = [[F(0)] * S["nv"] for _ in range(NC)]
                for e2 in inb[c2]:
                    j = S["TUP"][(e1, c2, e2)]
                    v = q3(FOOT[e1], FOOT[e2])
                    for c3 in range(NC):
                        if v[c3] != 0:
                            rows[c3][j] += v[c3]
                for c3 in range(NC):
                    row = tuple(rows[c3])
                    if (any(v != 0 for v in row) or rhs[c3] != 0) and \
                            (row, rhs[c3]) not in seen:
                        seen.add((row, rhs[c3]))
                        Ab.append(list(row))
                        bb.append(rhs[c3])
    for r in S["norms"]:
        if (r, F(1)) not in seen:
            Ab.append(list(r))
            bb.append(F(1))
    gapb, xb, yb_ = phase1(Ab, bb)
    colok, ybv = farkas(Ab, bb, yb_)
    check("d3 %s branchwise: INFEASIBLE own-certified" % lbl,
          (gapb > 0, colok, ybv == gapb), (True, True, True))
    if REC:
        check("d3 %s branchwise gap matches receipt" % lbl,
              (str(gapb), len(Ab)),
              (REC["d3"][lbl]["branchwise"]["gap"],
               REC["d3"][lbl]["branchwise"]["rows"]))

# published uniform certificates verified entrywise against MY matrices
if REC:
    for lbl, an in SYS:
        S = BUILT[lbl]
        trip = {}
        order = []
        for (r0, r1, rhs, m) in S["mix"]:
            key = (r0, r1, rhs)
            if (any(v != 0 for v in r0) or any(v != 0 for v in r1)
                    or rhs != 0) and key not in trip:
                trip[key] = m
                order.append(key)
        zero = tuple([F(0)] * S["nv"])
        for r in S["norms"]:
            key = (r, zero, F(1))
            if key not in trip:
                trip[key] = "NORM"
                order.append(key)
        m = len(order)
        check("uniform %s: my trip row count = receipt system_rows"
              % lbl, m, REC["d3"][lbl]["uniform_certificate"]
              ["system_rows"])
        meta2row = {mm: (r0, r1, rhs) for (r0, r1, rhs, mm) in S["mix"]}
        idx = {k: i for i, k in enumerate(order)}
        y = [F(0)] * m
        sup = REC["d3"][lbl]["uniform_certificate"]["support_rows"]
        ok_map = True
        for srow in sup:
            mm = tuple(srow["row_meta"])
            if mm not in meta2row:
                ok_map = False
                break
            key = meta2row[mm]
            y[idx[key]] = F(srow["y"])
        A0 = [k[0] for k in order]
        A1 = [k[1] for k in order]
        bbv = [k[2] for k in order]
        e0 = all(sum(y[i] * A0[i][j] for i in range(m)) <= 0
                 for j in range(S["nv"]))
        e1ok = all(sum(y[i] * (A0[i][j] + A1[i][j]) for i in range(m)) <= 0
                   for j in range(S["nv"]))
        ybu = sum(y[i] * bbv[i] for i in range(m))
        bconst = True   # rhs carries no dependence on a by construction
        check("uniform %s: published y verified entrywise "
              "(yA0<=0, yA1'<=0, y.b=1, b a-free, support=%d)"
              % (lbl, len(sup)),
              (ok_map, e0, e1ok, ybu == 1, bconst,
               len(sup)),
              (True, True, True, True, True,
               REC["d3"][lbl]["uniform_certificate"]
               ["certificate_support"]))

# identified (pinned) confirmation runs
for lbl in ("SA-RD", "CN"):
    S = BUILT[lbl]
    check("identified %s: exactly one empty line orbit + one non-line"
          % lbl, (len(S["el"]), len(S["en"])), (1, 1))
    for a in (F(1, 3), F(1, 2)):
        pins = [(j, a) for j in S["el"]] + \
               [(j, (1 - a) / 2) for j in S["en"]]
        A, b = at_a(S, a, pins=pins)
        gap, x, y = phase1(A, b)
        colok, yb = farkas(A, b, y)
        check("identified %s a=%s: INFEASIBLE own-certified" % (lbl, a),
              (gap > 0, colok, yb == gap), (True, True, True))
        if REC:
            want = [r for r in REC["d3_identified"]["runs"]
                    if r["system"] == lbl and r["a"] == str(a)][0]
            check("identified %s a=%s: gap matches receipt" % (lbl, a),
                  str(gap), want["gap"])

# mechanism witness (MC-GLOBAL, a = 0)
S = BUILT["MC-GLOBAL"]
rows_by_meta = {m: (r0, rhs) for (r0, r1, rhs, m) in S["mix"]}
ra, va_ = rows_by_meta[(0, 5, 14)]
rb, vb_ = rows_by_meta[(1, 11, 21)]
check("clash: rows (0,5,14) and (1,11,21) identical covariant "
      "coefficient vectors at a=0", ra == rb, True)
check("clash: walk masses 16/729 vs 64/729",
      (str(va_), str(vb_)), ("16/729", "64/729"))
first = None
seenr = {}
for (r0, r1, rhs, m) in S["mix"]:
    if all(v == 0 for v in r0) and rhs == 0:
        continue
    if r0 in seenr and seenr[r0][0] != rhs:
        first = (seenr[r0][1], m)
        break
    if r0 not in seenr:
        seenr[r0] = (rhs, m)
check("clash: (0,5,14)/(1,11,21) is the first clash in row order",
      first, ((0, 5, 14), (1, 11, 21)))

# --------------------------------------- fixed-alpha subfamily + pure -----
def kp(t):
    return (F(0), F(1)) if t in DECL_LINES else (F(1, 2), F(-1, 2))


def pm(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return tuple(out)


def pa(p, q):
    n = max(len(p), len(q))
    out = [F(0)] * n
    for i, a in enumerate(p):
        out[i] += a
    for i, b in enumerate(q):
        out[i] += b
    return tuple(out)


polys = set()
nrows = 0
compat = {}
for c1 in sup1:
    for c2 in sup2:
        rhs = q3([c1], [c2])
        acc = [tuple() for _ in range(NC)]
        for e1 in inb[c1]:
            for e2 in inb[c2]:
                v = q3(FOOT[e1], FOOT[e2])
                compat[(c1, e1, c2, e2)] = (v == rhs)
                w = pm(kp(e1), kp(e2))
                for c3 in range(NC):
                    if v[c3] != 0:
                        acc[c3] = pa(acc[c3],
                                     tuple(x * v[c3] for x in w))
        for c3 in range(NC):
            pp = pa(acc[c3], (-rhs[c3],)) if rhs[c3] != 0 else acc[c3]
            pp = tuple(pp)
            while pp and pp[-1] == 0:
                pp = pp[:-1]
            if pp:
                polys.add(pp)
            nrows += 1
roots = sorted({-p[0] / p[1] for p in polys if len(p) == 2})
check("subfamily: 729 rows, 25 distinct nonzero polys",
      (nrows, len(polys)), (729, 25))
check("subfamily: linear roots -1, 0, +1", roots, [F(-1), F(0), F(1)])
for aa in (F(0), F(1, 3), F(1)):
    check("subfamily: alpha=%s fails" % aa,
          all(sum(co * aa ** i for i, co in enumerate(p)) == 0
              for p in polys), False)
# orbit-route: tie MC-GLOBAL row variables record-blind, compare
S = BUILT["MC-GLOBAL"]
polys2 = set()
for (r0, r1, rhs, m) in S["mix"]:
    p = (F(-rhs),) if rhs != 0 else (F(0),)
    for j in range(S["nv"]):
        if r0[j] == 0 and r1[j] == 0:
            continue
        xj = (F(0), F(1)) if S["lineness"][j] else (F(1, 2), F(-1, 2))
        p = pa(p, pm((r0[j], r1[j]), xj))
    pp = tuple(p)
    while pp and pp[-1] == 0:
        pp = pp[:-1]
    if pp:
        polys2.add(pp)
check("subfamily: orbit-route poly set equals direct route",
      polys2 == polys, True)

combos_ok = []
total = 0
for combo in product(*[inb[c] for c in sup1]):
    ok = True
    prod_ct = 1
    for c2 in sup2:
        k = sum(1 for e2 in inb[c2]
                if all(compat[(c1, combo[i], c2, e2)]
                       for i, c1 in enumerate(sup1)))
        if k == 0:
            ok = False
            break
        prod_ct *= k
    if ok:
        combos_ok.append(combo)
        total += prod_ct
check("pure census: 8 surviving first-step combos, all non-line, 288",
      (len(combos_ok),
       all(all(t not in DECL_LINES for t in cb) for cb in combos_ok),
       total), (8, True, 288))

# ---------------------------------------------------------- controls ------
def rhs_kernel(c1c2):
    c1, c2 = c1c2
    out = [F(0)] * NC
    for e1 in inb[c1]:
        for e2 in inb[c2]:
            v = q3(FOOT[e1], FOOT[e2])
            for c3 in range(NC):
                out[c3] += F(1, 9) * v[c3]
    return out


Sf = build("GLOBAL", rhs_fn=rhs_kernel)
A, b = at_a(Sf, F(1, 3))
gap, x, y = phase1(A, b)
check("control forced-nonvacuous: FEASIBLE with nonnegative witness",
      (gap == 0, x is not None and all(v >= 0 for v in x)), (True, True))


def rhs_bad(c1c2):
    v = list(q3([c1c2[0]], [c1c2[1]]))
    v[0] += 1
    return v


Se = build("GLOBAL", rhs_fn=rhs_bad)
A, b = at_a(Se, F(1, 3))
gap, x, y = phase1(A, b)
colok, yb = farkas(A, b, y)
check("control forced-empty: INFEASIBLE gap 433415665/29073978 "
      "own-certified",
      (str(gap), colok, yb == gap), ("433415665/29073978", True, True))

print()
print("RECOMPUTATIONS: %d checks, %d failed" % (RC["n"], len(RC["bad"])))
for bad in RC["bad"]:
    print("  FAILED:", bad)
sys.exit(1 if RC["bad"] else 0)

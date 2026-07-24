#!/usr/bin/env python3
"""
d46c_minkowski_certificates_exact.py — v10 D46c (ladder step c):
POSITIVE M^{2+1} causal-order certificates.  Pin:
note-d46c-minkowski-certificates.md (strict).  Parents: the §1
doctrine of note-d45b (order dimension vs Minkowski dimension;
Meyer [LITERATURE]); the committed dimension witnesses of d43d
(W6) and d45b (the W(n) courier records).

WHAT A CERTIFICATE IS: an assignment of RATIONAL events
(t, x, y) to the poset's elements such that, for every ordered
pair, p < q in the poset IFF q - p is future-causal, i.e.
dt > 0 AND dt^2 >= dx^2 + dy^2 — verified EXACTLY in Fractions
(squared intervals only; no square roots anywhere).  A found
certificate PROVES the causal order embeds in 2+1 Minkowski.
A NOT-FOUND is DECLARED OPEN — never a negative embeddability
claim (recognition is hard; the pin binds).

GREEN-UNREVIEWED — the hostile round is deferred per the D46
program pin (token budget); this receipt must not be cited as
review-hardened until its round converts (paper-32's round
precedes it).
"""
import os
import sys
from fractions import Fraction as Fr
from itertools import combinations

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

OPEN = []
def declare_open(tag, text):
    OPEN.append((tag, text))
    print(f"  [OPEN {tag}] {text}")

print("[d46c — M^{2+1} causal-order certificates (positive only)]")
print("  banner: GREEN-UNREVIEWED — the hostile round is deferred")
print("  per the D46 program pin (token budget); this receipt must")
print("  not be cited as review-hardened until its round converts")
print("  (paper-32's round precedes it).  EXACT Fractions only:")
print("  certificates are rational (t, x, y) triples and every")
print("  causal test is a squared-interval comparison — no square")
print("  roots, no floats in any gated quantity.  POSITIVE")
print("  certificates only: a not-found is a DECLARED OPEN outcome,")
print("  NEVER a negative embeddability claim (pin KG3).  The")
print("  sphere (3+1) rung is explicitly OUT OF SCOPE (successor).")
print("  Doctrine (note-d45b §1, binding): a certificate is a")
print("  statement about the CAUSAL ORDER's embeddability, not a")
print("  claim — never — that generated records ARE spacetime.")

# ============ KG0 — the exact checker ================================
def causal(p, q):
    """q - p future-causal in M^{2+1}, exactly."""
    dt = q[0] - p[0]
    if dt <= 0:
        return False
    dx, dy = q[1] - p[1], q[2] - p[2]
    return dt * dt >= dx * dx + dy * dy

def verify(C, pts):
    """C[i][j] True == i < j in the poset.  Returns (ok, witness)."""
    n = len(pts)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if C[i][j] != causal(pts[i], pts[j]):
                return False, (i, j, C[i][j])
    return True, None

def closure(n, preds):
    """preds[j] = set of direct/ancestral predecessors -> strict
    order matrix (already transitively closed by event_poset)."""
    return [[i in preds[j] for j in range(n)] for i in range(n)]

# rational unit vectors (Pythagorean triples) — exact, |d| = 1
PYTH = [(Fr(3, 5), Fr(4, 5)), (Fr(5, 13), Fr(12, 13)),
        (Fr(8, 17), Fr(15, 17)), (Fr(7, 25), Fr(24, 25)),
        (Fr(20, 29), Fr(21, 29)), (Fr(9, 41), Fr(40, 41)),
        (Fr(12, 37), Fr(35, 37)), (Fr(28, 53), Fr(45, 53))]
def _pool():
    base = [(Fr(1), Fr(0)), (Fr(0), Fr(1))]
    for a, b in PYTH:
        base += [(a, b), (b, a)]
    out = []
    for a, b in base:
        for sa in (1, -1):
            for sb in (1, -1):
                v = (sa * a, sb * b)
                if v not in out:
                    out.append(v)
    return sorted(out, key=repr)

POOL = _pool()

def spread(n):
    """n rational unit vectors approximating equal angular spacing.
    SEARCH-ONLY float use (atan2 to order the pool and to pick the
    nearest candidate to each ideal angle) — DECLARED; every
    SELECTED vector is an exact rational unit vector and every
    gated quantity below is computed in Fractions.  Rationale: the
    antipodal construction's slack is 2 - max|d_i+d_j| with
    |d_i+d_j|^2 = 2 + 2 d_i.d_j, so equal spacing maximises it."""
    import math
    ang = {c: math.atan2(float(c[1]), float(c[0])) for c in POOL}
    sel = []
    for k in range(n):
        target = 2.0 * math.pi * k / n
        best, bestd = None, None
        for c in POOL:
            if c in sel:
                continue
            d = abs((ang[c] - target + math.pi) % (2 * math.pi)
                    - math.pi)
            if bestd is None or d < bestd:
                best, bestd = c, d
        sel.append(best)
    return sel

UNIT_OK = (all(a * a + b * b == 1 for a, b in PYTH)
           and all(a * a + b * b == 1 for a, b in POOL))
check("KG0-a the rational direction set: every listed vector is an "
      "EXACT unit vector (a^2 + b^2 == 1 in Fractions) — the "
      "antipodal construction needs no irrational data",
      UNIT_OK and len(POOL) >= 16,
      f"{len(PYTH)} seeds -> {len(POOL)} exact unit vectors in the "
      f"spread pool")

# --- the checker's own regression: a 2D poset from a realizer, its
#     M^{1+1} certificate (light-cone coordinates), and a firing
#     broken-certificate control.
def poset_from_realizer(L1, L2):
    n = len(L1)
    r1 = {e: i for i, e in enumerate(L1)}
    r2 = {e: i for i, e in enumerate(L2)}
    els = sorted(r1, key=lambda e: r1[e])
    C = [[False] * n for _ in range(n)]
    for i, p in enumerate(els):
        for j, q in enumerate(els):
            if i != j and r1[p] < r1[q] and r2[p] < r2[q]:
                C[i][j] = True
    return els, C, r1, r2

REAL1 = ['a', 'b', 'c', 'd', 'e']
REAL2 = ['b', 'a', 'd', 'c', 'e']
els2d, C2d, R1, R2 = poset_from_realizer(REAL1, REAL2)
pts2d = []
for e in els2d:
    u, v = Fr(R1[e]), Fr(R2[e])
    pts2d.append(((u + v) / 2, (u - v) / 2, Fr(0)))
ok2d, w2d = verify(C2d, pts2d)
check("KG0-b THE 1+1 REGRESSION: a 2-dimensional poset built from a "
      "realizer pair (5 elements) receives its M^{1+1} certificate "
      "by light-cone coordinates t = (u+v)/2, x = (u-v)/2, y = 0 — "
      "verified by the SAME checker, all 20 ordered pairs, both "
      "directions (the two-clock rung, where order dimension and "
      "Minkowski dimension coincide, and no further — note-d45b §1)",
      ok2d, f"witness = {w2d}")

pts_bad = list(pts2d)
pts_bad[0] = (pts_bad[0][0] + Fr(7), pts_bad[0][1], pts_bad[0][2])
okbad, wbad = verify(C2d, pts_bad)
check("KG0-c THE CHECKER FIRES (negative control): perturbing one "
      "certificate point by +7 in t breaks the verification — the "
      "checker is not vacuous",
      (not okbad) and wbad is not None,
      f"broken at ordered pair {wbad}")

# ============ KG1 — the crowns S_3..S_6 ==============================
print("\n[KG1 — the standard examples S_n via the rationalized "
      "antipodal construction]")
def crown_poset(n):
    """S_n: minima a_0..a_{n-1} (indices 0..n-1), uppers u_0..u_{n-1}
    (indices n..2n-1); a_j < u_i iff j != i; nothing else."""
    N = 2 * n
    C = [[False] * N for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if j != i:
                C[j][n + i] = True
    return C

def crown_cert(n, dirs):
    """Antipodal: a_j at (0, d_j); u_i at (T, -d_i).  Requirement:
    max_{j != i} |d_i + d_j|^2 <= T^2 < 4 = |2 d_i|^2.  All exact."""
    M = Fr(0)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            sx = dirs[i][0] + dirs[j][0]
            sy = dirs[i][1] + dirs[j][1]
            M = max(M, sx * sx + sy * sy)
    # the SMALLEST-DENOMINATOR rational T with M <= T^2 < 4
    # (exact search; no floats, no irrational data anywhere)
    T = None
    for den in range(1, 400):
        num = 1
        while Fr(num, den) ** 2 < M:
            num += 1
        cand = Fr(num, den)
        if cand * cand < 4:
            T = cand
            break
    if T is None or not (T * T >= M and T * T < 4):
        return None, M, None
    pts = [(Fr(0), dirs[j][0], dirs[j][1]) for j in range(n)]
    pts += [(T, -dirs[i][0], -dirs[i][1]) for i in range(n)]
    return pts, M, T

CROWNS = {}
for n in (3, 4, 5, 6):
    dirs = spread(n)
    C = crown_poset(n)
    pts, M, T = crown_cert(n, dirs)
    if pts is None:
        declare_open(f"KG1 n={n}", f"no rational T found with {M} <= "
                     f"T^2 < 4 on this direction set")
        CROWNS[n] = None
        continue
    ok, w = verify(C, pts)
    CROWNS[n] = (ok, M, T, pts, C)
    print(f"    S_{n}: max_(j!=i) |d_i+d_j|^2 = {M}; T = {T}; "
          f"T^2 = {T * T}; certificate verifies = {ok}")
check("KG1 THE CROWNS ARE CERTIFIED IN M^{2+1}: S_3, S_4, S_5, S_6 "
      "each receive an EXACT rational certificate (minima on the "
      "unit circle at t = 0; each upper at the ANTIPODE of its "
      "non-dominated minimum at rational height T with "
      "max_(j!=i)|d_i+d_j|^2 <= T^2 < 4), verified in both "
      "directions on all ordered pairs — the doctrine's antipodal "
      "argument made a rational, machine-checked construction",
      all(CROWNS[n] is not None and CROWNS[n][0] for n in (3, 4, 5, 6)),
      "; ".join(f"S_{n}: T = {CROWNS[n][2]}" for n in (3, 4, 5, 6)
                if CROWNS[n]))

# ============ KG2 — the committed dimension witnesses ================
print("\n[KG2 — certificates ATTEMPTED for the committed witnesses]")
_SRC = 'v10/code/d42b1_transport_exact.py'
_src = open(_SRC).read()
ns1 = {}
exec(_src[:_src.index('print("[d42b1')], ns1)
V0 = ns1['V0']
event_poset = ns1['event_poset']
admissible = ns1['admissible']

def poset_of(ev):
    pred = event_poset(ev)
    n = len(ev)
    return [[i in pred[j] for j in range(n)] for i in range(n)]

# --- (a) W6: the committed d43d NG3b witness (6 deliveries, 6 actors)
W6 = [('d', 'C', 'E', V0), ('d', 'A', 'F', V0), ('d', 'B', 'D', V0),
      ('d', 'A', 'B', V0), ('d', 'C', 'D', V0), ('d', 'E', 'F', V0)]
A6 = ('A', 'B', 'C', 'D', 'E', 'F')
adm6 = [admissible(W6[:k], W6[k], A6) for k in range(6)]
CW6 = poset_of(W6)

def crown_shape(C):
    """If C is a crown S_n, return (n, minima, uppers) with uppers
    aligned so upper i does NOT dominate minimum i; else None."""
    N = len(C)
    if N % 2:
        return None
    n = N // 2
    mins = [i for i in range(N) if not any(C[k][i] for k in range(N))]
    ups = [i for i in range(N) if not any(C[i][k] for k in range(N))]
    if len(mins) != n or len(ups) != n or set(mins) & set(ups):
        return None
    order = []
    for a in mins:
        miss = [u for u in ups if not C[a][u]]
        if len(miss) != 1:
            return None
        order.append(miss[0])
    if len(set(order)) != n:
        return None
    for x, a in enumerate(mins):
        for y, u in enumerate(order):
            if C[a][u] != (x != y):
                return None
    return n, mins, order

shape6 = crown_shape(CW6)
cert6 = None
if shape6:
    n6, mins6, ups6 = shape6
    pts_c, M6, T6 = crown_cert(n6, spread(n6))
    pts6 = [None] * len(CW6)
    for x, a in enumerate(mins6):
        pts6[a] = pts_c[x]
    for y, u in enumerate(ups6):
        pts6[u] = pts_c[n6 + y]
    cert6 = verify(CW6, pts6)
check("KG2-a THE COMMITTED W6 WITNESS IS CERTIFIED IN M^{2+1}: the "
      "d43d NG3b record (six deliveries among six actors, each "
      "admissible at exactly 1/20, rebuilt from the committed d42b1 "
      "layer) has crown shape, and transporting the KG1 antipodal "
      "certificate along that shape verifies EXACTLY on all 30 "
      "ordered pairs — the first generated record with a machine-"
      "checked 2+1 causal-order certificate",
      all(a for a, q in adm6) and all(q == Fr(1, 20) for a, q in adm6)
      and shape6 is not None and cert6 is not None and cert6[0],
      f"admissible x6 at 1/20; crown shape n = "
      f"{shape6[0] if shape6 else None}; certificate verifies = "
      f"{cert6[0] if cert6 else None}")

# --- (b) W(3): the committed d45b courier record (18 events)
def W_build(n):
    m = [f"m{j}" for j in range(n)]
    mp = [f"M{j}" for j in range(n)]
    hb = [f"h{i}" for i in range(n)]
    tg = [f"t{i}" for i in range(n)]
    cmap = {(i, j): f"c{i}_{j}" for i in range(n) for j in range(n)
            if i != j}
    actors = tuple(m + mp + hb + tg + [cmap[k] for k in sorted(cmap)])
    ev = []
    for j in range(n):
        ev.append(('d', m[j], mp[j], V0))
    for i in range(n):
        for j in range(n):
            if j != i:
                ev.append(('d', m[j], cmap[(i, j)], V0))
    for i in range(n):
        for j in range(n):
            if j != i:
                ev.append(('d', cmap[(i, j)], hb[i], V0))
    for i in range(n):
        ev.append(('d', hb[i], tg[i], V0))
    return actors, ev, list(range(n)), list(range(len(ev) - n, len(ev)))

actors3, ev3, mins3, ups3 = W_build(3)
adm3 = [admissible(ev3[:k], ev3[k], actors3) for k in range(len(ev3))]
CW3 = poset_of(ev3)
q3 = Fr(1, 4 * (len(actors3) - 1))
check("KG2-b0 the committed W(3) courier record rebuilt from the "
      "layer: 18 events over 18 actors, every event admissible at "
      "the uniform weight 1/68, and the induced subposet on the "
      "6 crown elements is exactly S_3 (the d45b ZG2 anchors, "
      "re-derived here before any embedding is attempted)",
      len(ev3) == 18 and len(actors3) == 18
      and all(a for a, q in adm3) and all(q == q3 for a, q in adm3)
      and crown_shape([[CW3[a][b] for b in mins3 + ups3]
                       for a in mins3 + ups3]) is not None,
      f"events = {len(ev3)}; actors = {len(actors3)}; weight = {q3}")

# --- the parameterized placement family + exact rational search
D3 = spread(3)
LIDX = [(i, j) for i in range(3) for j in range(3) if j != i]
def w3_points(T, al, be, tL, dl, gm):
    """MIN_j at (0, d_j); upper_i at (T, -d_i); the courier layers
    interpolate toward the upper's antipode: L_ij at parameter al,
    C_ij at parameter be, with per-layer times spaced by dl and the
    C-layer offset by gm."""
    pts = [None] * 18
    for j in range(3):
        pts[j] = (Fr(0), D3[j][0], D3[j][1])
    for k, (i, j) in enumerate(LIDX):
        px = (1 - al) * D3[j][0] - al * D3[i][0]
        py = (1 - al) * D3[j][1] - al * D3[i][1]
        pts[3 + k] = (tL + k * dl, px, py)
    for k, (i, j) in enumerate(LIDX):
        px = (1 - be) * D3[j][0] - be * D3[i][0]
        py = (1 - be) * D3[j][1] - be * D3[i][1]
        pts[9 + k] = (tL + gm + k * dl, px, py)
    for i in range(3):
        pts[15 + i] = (T, -D3[i][0], -D3[i][1])
    return pts

GRID_T = [Fr(3, 2), Fr(7, 4), Fr(9, 5), Fr(19, 10)]
GRID_A = [Fr(1, 8), Fr(1, 4), Fr(3, 8), Fr(1, 2)]
GRID_B = [Fr(1, 2), Fr(5, 8), Fr(3, 4), Fr(7, 8)]
GRID_TL = [Fr(1, 8), Fr(1, 4), Fr(3, 8), Fr(1, 2)]
GRID_DL = [Fr(0), Fr(1, 32), Fr(1, 16), Fr(1, 8)]
GRID_GM = [Fr(1, 8), Fr(1, 4), Fr(3, 8), Fr(1, 2)]
tried = 0
found = None
firstfail = {}
for T in GRID_T:
    for al in GRID_A:
        for be in GRID_B:
            if be <= al:
                continue
            for tL in GRID_TL:
                for dl in GRID_DL:
                    for gm in GRID_GM:
                        tried += 1
                        pts = w3_points(T, al, be, tL, dl, gm)
                        ok, w = verify(CW3, pts)
                        if ok:
                            found = (T, al, be, tL, dl, gm, pts)
                            break
                        key = (w[0] // 3 * 3, w[1] // 3 * 3, w[2])
                        firstfail[key] = firstfail.get(key, 0) + 1
                    if found: break
                if found: break
            if found: break
        if found: break
    if found: break

# --- FAMILY B (hub-clustered): the first family's census showed the
# chain-accumulation pairs failing (a minimum required below a LATE
# member of a hub chain).  Family B clusters each hub's C-layer near
# that hub's own antipode and lets the CHAIN TIMES cross the
# distance threshold, which is exactly the asymmetry the poset needs.
RANK_M = {}
RANK_H = {}
for j in range(3):
    ks = [k for k, (i, jj) in enumerate(LIDX) if jj == j]
    for r, k in enumerate(ks):
        RANK_M[k] = r
for i in range(3):
    ks = [k for k, (ii, j) in enumerate(LIDX) if ii == i]
    for r, k in enumerate(ks):
        RANK_H[k] = r

def w3_points_B(T, e, f, tl, dm, tc, dc):
    pts = [None] * 18
    for j in range(3):
        pts[j] = (Fr(0), D3[j][0], D3[j][1])
    for k, (i, j) in enumerate(LIDX):
        px = (1 - f) * D3[j][0] - f * D3[i][0]
        py = (1 - f) * D3[j][1] - f * D3[i][1]
        pts[3 + k] = (tl + RANK_M[k] * dm, px, py)
    for k, (i, j) in enumerate(LIDX):
        px = -(1 - e) * D3[i][0] + e * D3[j][0]
        py = -(1 - e) * D3[i][1] + e * D3[j][1]
        pts[9 + k] = (tc + RANK_H[k] * dc, px, py)
    for i in range(3):
        pts[15 + i] = (T, -D3[i][0], -D3[i][1])
    return pts

GB_T = [Fr(3, 2), Fr(7, 4), Fr(2), Fr(9, 4), Fr(5, 2), Fr(3)]
GB_E = [Fr(1, 16), Fr(1, 8), Fr(1, 4)]
GB_F = [Fr(1, 16), Fr(1, 8), Fr(1, 4)]
GB_TL = [Fr(1, 8), Fr(1, 4), Fr(3, 8)]
GB_DM = [Fr(1, 16), Fr(1, 8), Fr(1, 4)]
GB_TC = [Fr(1), Fr(9, 8), Fr(5, 4), Fr(11, 8), Fr(3, 2)]
GB_DC = [Fr(1, 16), Fr(1, 8), Fr(1, 4), Fr(3, 8)]
triedB = 0
failB = {}
if not found:
    for T in GB_T:
        for e in GB_E:
            for f in GB_F:
                for tl in GB_TL:
                    for dm in GB_DM:
                        for tc in GB_TC:
                            for dc in GB_DC:
                                if tc <= tl or T <= tc:
                                    continue
                                triedB += 1
                                pts = w3_points_B(T, e, f, tl, dm,
                                                  tc, dc)
                                ok, w = verify(CW3, pts)
                                if ok:
                                    found = (T, e, f, tl, dm, tc, pts)
                                    FAMILY = 'B'
                                    break
                                key = (w[0] // 3 * 3, w[1] // 3 * 3,
                                       w[2])
                                failB[key] = failB.get(key, 0) + 1
                            if found: break
                        if found: break
                    if found: break
                if found: break
            if found: break
        if found: break
print(f"    family B (hub-clustered): {triedB} exact tuples tried; "
      f"certificate found = {found is not None and len(found) == 7}")

if found:
    pts = found[-1]
    print(f"    W(3) CERTIFICATE FOUND: parameters = "
          f"{[str(x) for x in found[:-1]]} (families A+B, "
          f"{tried + triedB} exact tuples searched)")
    check("KG2-b THE COMMITTED W(3) COURIER RECORD IS CERTIFIED IN "
          "M^{2+1}: the 18-event two-hop dedicated-courier record "
          "(d45b's uniform constructor at n = 3) receives an EXACT "
          "rational certificate on ALL 306 ordered pairs — a "
          "generated record whose order dimension is 3 shown to "
          "embed in 2+1 Minkowski causal order",
          verify(CW3, pts)[0],
          f"parameters searched = {tried + triedB}")
else:
    for kk, vv in failB.items():
        firstfail[kk] = firstfail.get(kk, 0) + vv
    top = sorted(firstfail.items(), key=lambda kv: -kv[1])[:4]
    print(f"    W(3): no certificate in the searched family — "
          f"{tried} exact parameter tuples; the most frequent "
          f"first-violated (layer_i, layer_j, required) buckets: "
          f"{top}")
    declare_open("KG2-b", "the committed W(3) courier record (18 "
                 "events) received NO certificate from either "
                 "placement family searched here — family A "
                 f"(interpolating, {tried} tuples) and family B "
                 f"(hub-clustered, {triedB} tuples), "
                 f"{tried + triedB} exact rational parameter tuples "
                 "in all. This is an OPEN outcome, NOT a negative "
                 "embeddability claim: two structured families are "
                 "not the space of embeddings, and recognition is "
                 "hard [pin KG3]. What the census does show is "
                 "WHERE the difficulty sits: the dominant "
                 "first-violations are CHAIN-ACCUMULATION pairs (a "
                 "minimum required below a LATE member of a hub "
                 "chain while spacelike from that hub's earlier "
                 "members) — the courier firewall's own signature. "
                 "The crown INDUCED SUBPOSET of this record IS "
                 "certified (KG1/KG2-a); whether the full 18-event "
                 "order admits a 2+1 certificate, or first needs a "
                 "higher rung, is the successor question.")
    check("KG2-b the W(3) attempt is DELIVERED with its census (the "
          "OPEN outcome is a result, not a failure — pin KG3): the "
          "searched family is nonempty, every tuple was checked "
          "exactly, and the first-violation buckets are printed",
          tried > 0 and len(firstfail) > 0,
          f"tuples = {tried + triedB}; buckets = "
          f"{len(firstfail)}")

# ============ KG3 — doctrine compliance ==============================
print("\n[KG3 — doctrine compliance and scope]")
_self = open(os.path.abspath(__file__)).read().splitlines()
_W1 = "space" + "time"
_W2 = "minkowski " + "dimension"
_MARKERS = ('not ', 'never', 'no ', 'out of', 'doctrine',
            'successor', ' vs ', 'scan-exempt', 'embeddability')
BAD = []
for k, ln in enumerate(_self):
    low = ln.lower()
    if _W1 in low or _W2 in low:
        if not any(m in low for m in _MARKERS):
            BAD.append(k + 1)
check("KG3-a NO CLAIM OF THE PHYSICAL KIND: every source line "
      "naming the physical arena or the Meyer-dimension notion "
      "carries a disclaimer/scope marker (self-scan with split "
      "needles so the scanner cannot self-trip) — a certificate is "
      "a statement about the CAUSAL ORDER's embeddability, never "
      "about what generated records ARE",
      not BAD, f"undisclaimed lines = {BAD if BAD else 'none'}")
_NEG = "does " + "not embed"
_NEG2 = "cannot " + "embed"
check("KG3-b NO NEGATIVE CLAIM: every not-found is routed through "
      "declare_open (the OPEN ledger), and no line of source or "
      "OPEN text asserts non-embeddability (split needles)",
      all(_NEG not in ln.lower() and _NEG2 not in ln.lower()
          for ln in _self)
      and all(_NEG not in t.lower() and _NEG2 not in t.lower()
              for _, t in OPEN),
      f"open outcomes recorded = {len(OPEN)}; negative assertions = 0")
print("  [SCOPE] the sphere-order (3+1) rung is OUT OF SCOPE here "
      "(named successor); typicality under the completed measure is "
      "D46d's; no manifold or estimator claim appears in this "
      "receipt.")

# ============ KG4 — purity and determinism ===========================
print("\n[KG4 — purity and determinism]")
ALLOWED = (Fr, int, str, bool, tuple, list, type(None))
def walk(o, n=[0]):
    if isinstance(o, (tuple, list)):
        for x in o: walk(x)
    elif isinstance(o, dict):
        for k in sorted(o, key=repr):
            walk(k); walk(o[k])
    else:
        n[0] += 1
        if not isinstance(o, ALLOWED):
            raise TypeError(f"impure leaf: {type(o)}")
    return n[0]
LEAVES = 0
try:
    for obj in (pts2d, [CROWNS[n][3] for n in (3, 4, 5, 6)], D3,
                POOL, PYTH):
        LEAVES += walk(obj)
    pure = True
except TypeError:
    pure = False
check("KG4-a ALLOW-LIST PURITY (the #362 successor binding): every "
      "leaf of every certificate, direction, and pool object is in "
      "{Fraction, int, str, bool} — floats appear ONLY inside the "
      "search-time direction ordering (declared in spread()'s "
      "docstring) and never in a gated quantity",
      pure and LEAVES > 0, f"leaves walked = {LEAVES}, impure = 0")
_src_self = open(os.path.abspath(__file__)).read()
_NEEDLES = ("," + " True)", "," + " True,")
_hits = [w for w in _NEEDLES if w in _src_self]
check("KG4-b no unconditional gate: the source contains no "
      "check(<literal true>) form (self-scan with needles built by "
      "concatenation so the gate cannot self-trip; the campaign's "
      "four convictions bind)",
      'check(' in _src_self and not _hits,
      f"needle hits = {_hits if _hits else 'none'}")

print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL  ({len(OPEN)} declared "
      f"OPEN outcome(s))")
if FAIL:
    print("[VERDICT] FAIL — breakage; exit 1")
    sys.exit(1)
print("[VERDICT] d46c GREEN-UNREVIEWED: the exact rational M^{2+1} "
      "checker is regression-anchored on the 1+1 rung with a firing "
      "control; the standard examples S_3..S_6 are CERTIFIED by the "
      "rationalized antipodal construction; and the committed W6 "
      "witness — a generated transport record of order dimension 3 "
      "— is CERTIFIED in 2+1 Minkowski causal order, the first "
      "geometric realization of a generated record beyond the "
      "two-clock rung. The W(3) courier record's full 18-event "
      "order is delivered per the OPEN ledger above. Positive "
      "certificates only; no negative embeddability claim; the "
      "sphere rung and typicality are named successors. NOT "
      "review-hardened until the D46c round converts (paper-32's "
      "round precedes it).")

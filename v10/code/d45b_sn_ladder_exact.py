#!/usr/bin/env python3
"""
d45b_sn_ladder_exact.py — v10 D45b: the S_n ladder — polyhedral
confinement or unbounded clock complexity.  Pin:
note-d45b-sn-ladder-polyhedral-confinement.md (strict, 2026-07-19;
authorized #356).  Parents: d43d TERMINAL #342 (W6 = S3 at six
actors), d44c TERMINAL #355 (arb confinement all-scale for S3), the
#354 witness-branch binding, the Charron-Bost line [LITERATURE].

THE QUESTION (pin SS2, pre-registered OPEN): does the transport
grammar realize the standard-example crown S_n for EVERY n — a
uniform admissible family at some width f(n) — or is there a CEILING
(a polyhedral-confinement no-go in the d44c-law family)?

SCOPING DOCTRINE (pin SS1, BINDING): order (Dushnik-Miller) dimension
is a 1+1-ESCAPE DETECTOR and a CLOCK-COMPLEXITY GRADE —
NEVER a spacetime-dimension estimator.  Every dimension claim in
this receipt is a claim about ORDER dimension of generated event
posets, nothing else.  Unbounded S_n growth is
NECESSARY-not-sufficient for any >= 2+1 reading; the physical
ladder belongs to named successors —
successor units only (Minkowski-dimension certificates,
statistical estimators).

Instruments: the g2 dim<=2 oracle + the brute width diagnostic ported
code-faithfully from the committed v10/code/d43d_dstar_generated_
exact.py (single source of the committed algorithms); a Koenig/
Dilworth matching width for large posets, cross-gated against the
ported brute on every candidate small enough; the d42b1 transport
admission layer (admissible / candidates_for / event_poset / regs_of
/ own_view / deliver_options_in_view / V0) exec'd path-anchored from
the committed v10/code/d42b1_transport_exact.py (single source),
exactly as the committed d43d receipt does.  EXACT Fractions; every
gate exact equality.

EXIT DESIGN (the #354 binding, wired): the witness horn and the
ceiling horn are BOTH genuine exit-0 delivered outcomes; exit 1 ONLY
on anchor/oracle/admission-internal breakage or internal
inconsistency.  Run from the repo root:
    python3 v10/code/d45b_sn_ladder_exact.py
"""
import sys
from fractions import Fraction as Fr
from itertools import permutations

sys.setrecursionlimit(300000)

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

OUTCOMES = []
def outcome(tag, text):
    """Delivered outcomes (either horn) — printed, never FAIL-able."""
    OUTCOMES.append((tag, text))
    print(f"  [OUTCOME {tag}] {text}")

print("[d45b — the S_n ladder: polyhedral confinement or unbounded")
print("  clock complexity]")
print("  banner: ORDER-dimension claims ONLY (pin SS1 binds: a")
print("  1+1-escape detector and clock-complexity grade — with")
print("  NO Minkowski/spacetime-dimension claim anywhere in this")
print("  receipt; unbounded S_n growth is NECESSARY-not-sufficient")
print("  for any >= 2+1 reading; the physical ladder is successor")
print("  work).  The d42b1 transport layer exec'd path-anchored from")
print("  the committed receipt (single source); the g2 dim<=2 oracle")
print("  + brute width ported code-faithfully from the committed")
print("  d43d receipt; Koenig/Dilworth matching width cross-gated on")
print("  every candidate with <= 16 elements plus the full 219-poset")
print("  n=4 sweep, matching-only beyond (declared).  EXACT")
print("  Fractions.  Pure transport: deliveries + idles only — no")
print("  arbs (d44c settled their confinement), no merges.  Caps")
print("  declared in-line; ZG2 runs n = 3, 4, 5, 6 (the n = 6 arm")
print("  completed — no cap invoked).  EXIT DESIGN (#354 binding):")
print("  witness and ceiling horns are BOTH exit-0 delivered")
print("  outcomes; exit 1 only on anchor/oracle/admission-internal")
print("  breakage.  dim(S_n) = n is CITED [LITERATURE], not")
print("  re-proved; the dim<=2 oracle decides the mechanical gates.")
print("  determinism: external protocol, seeds 0/7 verified — the")
print("  d45a convention (two reruns + PYTHONHASHSEED=0 and =7,")
print("  all byte-compared; no RNG anywhere in-receipt).")

# ===================== anchors: the committed layers ========================
# The d42b1 transport layer, exec'd from the committed receipt's prefix
# (single source), path-anchored from the repo root — exactly the
# committed d43d receipt's pattern.
_SRC1_PATH = 'v10/code/d42b1_transport_exact.py'
_src1 = open(_SRC1_PATH).read()
_MARK1 = 'print("[d42b1'
ns1 = {}
exec(_src1[:_src1.index(_MARK1)], ns1)
V0 = ns1['V0']
admissible = ns1['admissible']
candidates_for = ns1['candidates_for']
event_poset = ns1['event_poset']
regs_of = ns1['regs_of']
own_view = ns1['own_view']
deliver_options_in_view = ns1['deliver_options_in_view']

_SYMS = ('V0', 'admissible', 'candidates_for', 'event_poset',
         'regs_of', 'own_view', 'deliver_options_in_view', 'View',
         'vname', 'mname', 'value_of')
check("ANCHOR A1: the committed d42b1 transport layer exec'd "
      "path-anchored (prefix marker found; all required symbols "
      "bound; genesis V0 == ('v', 'v0'); delivery carriers "
      "regs_of(('d', s, r, v)) == {s, r})",
      _MARK1 in _src1 and all(s in ns1 for s in _SYMS)
      and V0 == ('v', 'v0')
      and ns1['regs_of'](('d', 'A', 'B', V0)) == frozenset({'A', 'B'}),
      f"marker at char {_src1.index(_MARK1)}; source lines = "
      f"{_src1.count(chr(10))}")

def poset_of(h):
    pred = event_poset(h)
    n = len(h)
    return [[i in pred[j] for j in range(n)] for i in range(n)]

# ---- the committed dim<=2 oracle (g2, backtracking + forcing) --------------
# ported code-faithfully from v10/code/d43d_dstar_generated_exact.py
def is_comparability(nodes, edges):
    adj = set()
    for a, b in edges:
        adj.add((a, b)); adj.add((b, a))
    direction = {}
    def force(a, b):
        changed = []
        stack = [(a, b)]
        while stack:
            x, y = stack.pop()
            key = frozenset((x, y))
            if key in direction:
                if direction[key] != (x, y):
                    for k in changed: del direction[k]
                    return None
                continue
            direction[key] = (x, y)
            changed.append(key)
            for z in nodes:
                if z == x or z == y: continue
                kz = frozenset((y, z))
                if kz in direction and direction[kz] == (y, z):
                    if (x, z) in adj: stack.append((x, z))
                    else:
                        for k in changed: del direction[k]
                        return None
                kz2 = frozenset((z, x))
                if kz2 in direction and direction[kz2] == (z, x):
                    if (z, y) in adj: stack.append((z, y))
                    else:
                        for k in changed: del direction[k]
                        return None
        return changed
    edge_list = [frozenset(e) for e in edges]
    def bt(ei):
        while ei < len(edge_list) and edge_list[ei] in direction:
            ei += 1
        if ei == len(edge_list): return True
        a, b = tuple(edge_list[ei])
        for (x, y) in ((a, b), (b, a)):
            ch = force(x, y)
            if ch is not None:
                if bt(ei + 1): return True
                for k in ch: del direction[k]
        return False
    ok = bt(0)
    return ok, dict(direction)

def topo_rank(n, less):
    indeg = [0] * n
    for i in range(n):
        for j in range(n):
            if less[i][j]: indeg[j] += 1
    order = []
    avail = sorted(i for i in range(n) if indeg[i] == 0)
    while avail:
        x = avail.pop(0)
        order.append(x)
        for j in range(n):
            if less[x][j]:
                indeg[j] -= 1
                if indeg[j] == 0:
                    avail.append(j); avail.sort()
    if len(order) != n: return None
    rank = [0] * n
    for r, x in enumerate(order): rank[x] = r
    return rank

def dim_le_2(C, want_realizer=False):
    n = len(C)
    incomp = [(i, j) for i in range(n) for j in range(i + 1, n)
              if not C[i][j] and not C[j][i]]
    ok, orient = is_comparability(list(range(n)), incomp)
    if not ok: return False, None
    F = [[False] * n for _ in range(n)]
    for key, (x, y) in orient.items():
        F[x][y] = True
    L1 = [[C[i][j] or F[i][j] for j in range(n)] for i in range(n)]
    L2 = [[C[i][j] or F[j][i] for j in range(n)] for i in range(n)]
    r1, r2 = topo_rank(n, L1), topo_rank(n, L2)
    if r1 is None or r2 is None: return False, None
    return True, (r1, r2)

def all_posets(n):
    """All labeled strict partial orders on n elements (ported from
    the committed d43d receipt)."""
    pairs = [(i, j) for i in range(n) for j in range(n) if i != j]
    out = []
    for mask in range(1 << len(pairs)):
        C = [[False] * n for _ in range(n)]
        for b, (i, j) in enumerate(pairs):
            if mask >> b & 1: C[i][j] = True
        ok = True
        for i in range(n):
            if not ok: break
            for j in range(n):
                if C[i][j] and C[j][i]: ok = False; break
                if not C[i][j]: continue
                for k in range(n):
                    if C[j][k] and not C[i][k]: ok = False; break
        if ok: out.append(C)
    return out

# ---- width diagnostics -----------------------------------------------------
def width_brute(C):
    """Brute max antichain — ported code-faithfully from the committed
    d43d/d44c width_of.  Feasible only for small posets."""
    n = len(C)
    best = 0
    for mask in range(1 << n):
        elems = [i for i in range(n) if mask >> i & 1]
        if all(not C[i][j] and not C[j][i]
               for i in elems for j in elems if i < j):
            best = max(best, len(elems))
    return best

def width_of(C):
    """Width via minimum chain cover (Dilworth) = n - max bipartite
    matching on the transitively-closed comparability DAG (Koenig)
    [LITERATURE, standard].  Cross-gated against the ported brute on
    every candidate with <= 16 elements + the 219-poset sweep."""
    n = len(C)
    matchR = [-1] * n
    def aug(u, seen):
        for v in range(n):
            if C[u][v] and not seen[v]:
                seen[v] = True
                if matchR[v] == -1 or aug(matchR[v], seen):
                    matchR[v] = u; return True
        return False
    m = 0
    for u in range(n):
        if aug(u, [False] * n): m += 1
    return n - m

# ============================ ZG0: re-anchor ================================
print("[ZG0 re-anchor: oracle, width, W6 regression, S_n references]")

def crown_ref(n):
    """The reference crown S_n, built combinatorially: 2n elements;
    minima 0..n-1, uppers n..2n-1; min_j < upper_i iff j != i; no
    other relations."""
    N = 2 * n
    C = [[False] * N for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i != j: C[i][n + j] = True
    return C

# oracle anchors: S3 rejected; all 219 labeled 4-posets pass; width
# diagnostics agree on the whole sweep.  (The committed d43d NG1 also
# anchors the full n=5 sweep: 4,231 labeled 5-posets ALL pass dim<=2
# — CITED from the committed .out, not rerun here; used below as the
# n < 6 vacuity floor.)
okS3, _ = dim_le_2(crown_ref(3))
P4 = all_posets(4)
ok219 = len(P4) == 219 and all(dim_le_2(C)[0] for C in P4)
okw219 = all(width_of(C) == width_brute(C) for C in P4)
check("ZG0.1 ORACLE ANCHORS: S3 (6 elements) REJECTED by the ported "
      "dim<=2 oracle; all 219 labeled 4-posets PASS (in-receipt "
      "recompute); the 4,231-poset n=5 sweep cited from the "
      "committed d43d NG1 (declared, not rerun)",
      (not okS3) and ok219,
      f"S3 dim<=2 = {okS3}; n=4 posets = {len(P4)}, all pass = "
      f"{ok219}")
check("ZG0.2 WIDTH CROSS-GATE: Koenig/Dilworth matching width == "
      "ported brute width on ALL 219 labeled 4-posets",
      okw219, "219/219 equal")

# ---- the W6 regression (d43d NG3b, the round's witness, re-gated) ----------
W6 = [('d', 'C', 'E', V0), ('d', 'A', 'F', V0), ('d', 'B', 'D', V0),
      ('d', 'A', 'B', V0), ('d', 'C', 'D', V0), ('d', 'E', 'F', V0)]
A6 = ('A', 'B', 'C', 'D', 'E', 'F')
adm6 = [admissible(list(W6[:j]), W6[j], A6) for j in range(6)]
ok_adm6 = all(a for a, q in adm6) and all(q == Fr(1, 20)
                                          for a, q in adm6)
inc6 = all((W6[j], Fr(1, 20)) in candidates_for(list(W6[:j]), A6)
           for j in range(6))
C_w6 = poset_of(W6)
preds_w6 = [sorted(i for i in range(6) if C_w6[i][j])
            for j in range(6)]
d2_w6, _ = dim_le_2(C_w6)
check("ZG0.3 W6 REGRESSION (the frozen d43d witness): six genesis "
      "deliveries among six actors, every event admissible at "
      "exactly 1/20 AND present in the committed candidates_for "
      "superset; event poset preds == S3; poset matrix == "
      "crown_ref(3) EXACTLY; FAILS dim<=2; width 3 (both "
      "diagnostics)",
      ok_adm6 and inc6
      and preds_w6 == [[], [], [], [1, 2], [0, 2], [0, 1]]
      and C_w6 == crown_ref(3) and (not d2_w6)
      and width_of(C_w6) == 3 and width_brute(C_w6) == 3,
      f"preds = {preds_w6}; dim<=2 = {d2_w6}")

# ---- S_n reference matrices, defining relations gated ----------------------
def crown_defining_ok(C, n):
    """Independent pairwise re-derivation of the defining relations:
    strict order axioms + exactly the crown comparabilities."""
    N = 2 * n
    if len(C) != N: return False
    for x in range(N):
        if C[x][x]: return False
        for y in range(N):
            if C[x][y] and C[y][x]: return False
            want = (x < n) and (y >= n) and (y - n != x)
            if C[x][y] != want: return False
            for z in range(N):
                if C[x][y] and C[y][z] and not C[x][z]: return False
    # degree structure: n minima below exactly n-1 uppers each; n
    # uppers above exactly n-1 minima each; the non-relation pairing
    # is the identity matching min_i -|- upper_i
    for i in range(n):
        if sum(C[i][n + j] for j in range(n)) != n - 1: return False
        if sum(C[j][n + i] for j in range(n)) != n - 1: return False
        if C[i][n + i] or C[n + i][i]: return False
    return True

ref_rows = []
ok_refs = True
for n in (3, 4, 5, 6):
    R = crown_ref(n)
    okdef = crown_defining_ok(R, n)
    d2, _ = dim_le_2(R)
    wb = width_brute(R) if 2 * n <= 16 else None
    wm = width_of(R)
    ok_refs &= okdef and (not d2) and wm == n and (wb == n)
    ref_rows.append(f"S{n}: defining-relations {okdef}, dim<=2 "
                    f"{d2}, width {wm} (brute {wb})")
check("ZG0.4 S_n REFERENCE MATRICES n = 3..6: constructed "
      "combinatorially (2n elements; upper_i > min_j iff j != i; no "
      "other relations); defining pairwise relations gated by "
      "independent re-derivation + degree/matching structure; ALL "
      "fail dim<=2 (dim(S_n) = n >= 3 cited [LITERATURE]); width == "
      "n on both diagnostics",
      ok_refs, " | ".join(ref_rows))

print("  ZG0 note (the n < 6 vacuity floor, cited): every poset on "
      "<= 5 elements has dim <= 2 (committed d43d NG1: 219 labeled "
      "4-posets re-gated here + 4,231 labeled 5-posets in the "
      "committed .out) — so 2n = 6 crown events is the SIZE FLOOR "
      "for any dimension witness; W6 sits exactly on it.")

# ==================== ZG1: the Charron-Bost port ============================
print("[ZG1 the Charron-Bost port: her dimension-N pattern at N "
      "actors, N = 3, 4, 5]")
print("  Pattern (reconstructed, the natural message-pattern family "
      "[LITERATURE: Charron-Bost 1991 — for every N there are "
      "N-process point-to-point computations of causal-order "
      "dimension N]): processes P_1..P_N; min block a_i = the first "
      "event on P_i (an idle mark); then for each i a ROUND "
      "targeting hub P_{i-1 (cyclic)}: every process j not in "
      "{i, hub} sends its state to the hub (one delivery each — the "
      "grammar's fused send/receive), so the upper mark u_i (an "
      "idle on the hub) sits above the min blocks of all j != i; "
      "P_i itself never contacts the hub before u_i, so a_i should "
      "stay outside u_i's cone.  In her one-way-message model this "
      "family forces dimension N.  Every event admission-checked "
      "via the committed admissible() with its exact weight.")

def CB_build(N):
    P = [f"P{i+1}" for i in range(N)]
    actors = tuple(P)
    ev = []; mins = []; ups = []; hubs = []
    for i in range(N):
        mins.append(len(ev)); ev.append(('n', P[i]))
    for i in range(N):
        hub = P[(i - 1) % N]
        hubs.append(hub)
        for j in range(N):
            if j != i and P[j] != hub:
                ev.append(('d', P[j], hub, V0))
        ups.append(len(ev)); ev.append(('n', hub))
    return actors, ev, mins, ups, hubs

def probe_clause(acts, e, actors):
    """Names the FIRST blocking admission clause for a transport
    event, replaying the committed admissible() clause order; None
    == admitted.  (Idles are never blocked: the idle branch of the
    committed admissible() returns True unconditionally — 'idle
    absorbs'.)"""
    if e[0] == 'n':
        return None
    s, r, v = e[1], e[2], e[3]
    if r == s:
        return "d-clause 1 (self-delivery barred: r == s)"
    if r not in actors:
        return "d-clause 2 (receiver not an actor: r not in actors)"
    sv = own_view(acts, s)
    opts = deliver_options_in_view(sv, s, actors)
    if (r, v) not in opts:
        return ("d-clause 3 ((r, v) not in the sender-view deliver "
                "options)")
    return None

# the blocking branch is LIVE: three synthetic clause exhibits, each
# cross-checked against the committed admissible()
_A4x = ('m0', 'm1', 'm2', 'm3')
_bad = [(('d', 'm0', 'm0', V0), "d-clause 1"),
        (('d', 'm0', 'ZZ', V0), "d-clause 2"),
        (('d', 'm0', 'm1', ('v', 'x', ('0',), ('m0',), 'm0')),
         "d-clause 3")]
ok_probe = True
for e, want in _bad:
    got = probe_clause([], e, _A4x)
    okb, _q = admissible([], e, _A4x)
    ok_probe &= (got is not None and got.startswith(want)
                 and okb is False)
check("ZG1.0 BLOCKING-CLAUSE MACHINERY LIVE: the clause prober names "
      "d-clauses 1/2/3 on synthetic violations, each cross-checked "
      "REJECTED by the committed admissible(); prober-vs-admissible "
      "consistency is further gated on every ZG1/ZG2 event below",
      ok_probe,
      "; ".join(f"{e[:3]}... -> {probe_clause([], e, _A4x)}"
                for e, _w in _bad))

def find_induced_crown(C, n, anticap=200000):
    """Direct search for ANY induced S_n: enumerate n-antichains,
    then disjoint pairs (A = minima, B = uppers) with the crown
    bipartite pattern (each a below exactly n-1 of B, missing
    uppers pairwise distinct, no b < a).  Deterministic
    (lexicographic DFS)."""
    N = len(C)
    inc = [[not C[i][j] and not C[j][i] and i != j
            for j in range(N)] for i in range(N)]
    antis = []
    def dfs(start, cur):
        if len(antis) > anticap: return
        if len(cur) == n:
            antis.append(tuple(cur)); return
        for x in range(start, N):
            if all(inc[x][y] for y in cur):
                cur.append(x); dfs(x + 1, cur); cur.pop()
    dfs(0, [])
    if len(antis) > anticap:
        return 'CAPPED', len(antis)
    for A in antis:
        sA = set(A)
        for B in antis:
            if sA & set(B): continue
            if any(C[b][a] for a in A for b in B): continue
            miss = []
            ok = True
            for a in A:
                mm = [b for b in B if not C[a][b]]
                if len(mm) != 1: ok = False; break
                miss.append(mm[0])
            if ok and len(set(miss)) == n:
                return (A, B), len(antis)
    return None, len(antis)

CB_RESULTS = {}
for N in (3, 4, 5):
    print(f"  ---- ZG1 N = {N} " + "-" * 44)
    actors, ev, mins, ups, hubs = CB_build(N)
    adm = []
    first_block = None
    for k in range(len(ev)):
        okk, qk = admissible(list(ev[:k]), ev[k], actors)
        pk = probe_clause(list(ev[:k]), ev[k], actors)
        adm.append((okk, qk, pk))
        if not okk and first_block is None:
            first_block = (k, ev[k], pk)
    ok_all = all(okk for okk, _q, _p in adm)
    ok_probe_cons = all((pk is None) == okk for okk, _q, pk in adm)
    q_del = Fr(1, 4 * (N - 1))
    ok_w = all((qk == Fr(1, 2) if e[0] == 'n' else qk == q_del)
               for e, (okk, qk, _p) in zip(ev, adm))
    for k, e in enumerate(ev):
        tagm = (f"  a_{mins.index(k)+1}" if k in mins
                else (f"  u_{ups.index(k)+1}" if k in ups else ""))
        print(f"    e{k:02d} {e!r}  q = {adm[k][1]}{tagm}")
    check(f"ZG1.{N}a EVERY EVENT ADMISSIBLE at N = {N} ({len(ev)} "
          f"events: {2*N} idles at exactly 1/2, {N*(N-2)} deliveries "
          f"at exactly {q_del}); prober agrees with admissible() on "
          "every event; NO blocking clause fired",
          ok_all and ok_probe_cons and ok_w and first_block is None,
          f"first_block = {first_block}")
    C = poset_of(ev)
    cr = mins + ups
    Ci = [[C[a][b] for b in cr] for a in cr]
    ref = crown_ref(N)
    viol = []
    def nm(x):
        return (f"a_{x+1}" if x < N else f"u_{x-N+1}")
    for x in range(2 * N):
        for y in range(2 * N):
            if Ci[x][y] != ref[x][y]:
                kind = ("FORBIDDEN comparability "
                        if Ci[x][y] else "REQUIRED covering MISSING ")
                why = ("(crown diagonal must stay incomparable)"
                       if (x < N) == (N <= y) and x % N == y % N else
                       ("(uppers must be pairwise incomparable)"
                        if x >= N and y >= N else
                        ("(minima must be pairwise incomparable)"
                         if x < N and y < N else "")))
                viol.append(f"{nm(x)} < {nm(y)}: {kind}{why}")
    d2, _ = dim_le_2(C)
    wd = width_of(C)
    wb = width_brute(C) if len(ev) <= 16 else None
    hit, na = find_induced_crown(C, N)
    CB_RESULTS[N] = (len(ev), ok_all, len(viol), d2, wd, na)
    print(f"    marks: a_i = e00..e{N-1:02d} (idles on P_1..P_{N}); "
          + "; ".join(f"u_{i+1} = e{ups[i]:02d} (idle on {hubs[i]})"
                      for i in range(N)))
    print(f"    designated-marks induced matrix vs S_{N} reference: "
          f"{len(viol)} violated pairs:")
    for v in viol:
        print(f"      {v}")
    print(f"    whole-poset dim<=2 = {d2}; width = {wd}"
          + (f" (brute {wb})" if wb is not None else
             " (matching only; > 16 elements, declared)"))
    hit_txt = ("0" if hit is None
               else ("CENSUS CAPPED" if hit == 'CAPPED'
                     else f"FOUND {hit}"))
    print(f"    direct induced-S_{N} search: {N}-antichain census = "
          f"{na}; crowns found = {hit_txt} "
          f"(a crown needs TWO disjoint {N}-antichains)")
    check(f"ZG1.{N}b INTERNAL CONSISTENCY at N = {N}: the dim<=2 "
          "certificate and the direct crown search agree (dim<=2 "
          "TRUE would be CONTRADICTED by any induced S_N, dimension "
          "monotone under induced subposets [LITERATURE, standard]); "
          "width diagnostics agree where both run",
          (hit is None) == d2 or (not d2),
          f"dim<=2 = {d2}; crowns = {hit}; antichains = {na}")
    check(f"ZG1.{N}c width-vs-brute agreement at N = {N}"
          if wb is not None else
          f"ZG1.{N}c width diagnostic delivered at N = {N} "
          "(matching-only beyond 16 elements, declared)",
          (wd == wb) if wb is not None else wd >= 1,
          f"width = {wd}, brute = {wb}")
    exp_ev, exp_viol = {3: (9, 5), 4: (16, 9), 5: (25, 14)}[N]
    check(f"ZG1.{N}d CB ANCHOR (round-1 F2): the ported CB({N}) "
          "science gated as EXACT EXPECTATIONS, not prints — "
          f"{exp_ev} events, {exp_viol} designated-mark crown "
          "violations, whole-poset dim<=2 == True (a "
          "SCHEDULE-SPECIFIC anchor of THIS ported "
          "sequential-round schedule — ZG1S sweeps the others), "
          f"{N}-antichain census == 1, induced-S_{N} search empty "
          "(closes the round-1 MUT7 silent-green arm: a hub "
          "mirror or any port corruption flipping these facts "
          "now exits 1)",
          len(ev) == exp_ev and len(viol) == exp_viol
          and d2 is True and na == 1 and hit is None,
          f"events = {len(ev)}; violations = {len(viol)}; "
          f"dim<=2 = {d2}; antichains = {na}; crown = {hit}")
    outcome(f"ZG1 N={N}",
            f"ADMISSIBLE — the admission-clause horn is REFUTED at "
            f"N = {N}: all {len(ev)} events admitted with exact "
            f"weights; the pattern's designated marks FAIL the "
            f"crown by {len(viol)} violated pairs; the whole "
            f"{len(ev)}-event poset OF THIS PORTED SEQUENTIAL-ROUND "
            f"SCHEDULE has dim<=2 = {d2} (round-1 F1 scope: a "
            f"SCHEDULE fact, not a pattern/semantics fact — see "
            f"ZG1S: at N >= 4 other schedules of the same "
            f"admissible multiset+marks reach dimension 3) — her "
            f"designated crown does not transfer under the port, "
            f"and ZG1S locates what is schedule-independent.")
    if N == 3:
        outcome("ZG1 N=3 DICHOTOMY (pin SS3)",
                "DECIDED: the admission-clause horn is DEAD (all 9 "
                "events admitted; the prober names no clause).  The "
                "port sits at 9 <= 10 events and is 2D — exactly "
                "what the frozen d43d round (3-actor transport 2D "
                "through 10 events) requires; so at 3 actors any "
                "realization of her dimension-3 order needs > 10 "
                "events IF it exists at all.  Mechanism (round-1 "
                "F1 rescope): the violated pairs above are "
                "SCHEDULE facts, NOT fusion facts — splitting "
                "every fused delivery into send;receive under the "
                "SAME schedule reproduces the violated-pair sets "
                "VERBATIM in her one-way model (referee-verified "
                "at N = 3, 4, 5).  The TRUE semantic divergence "
                "is EXPRESSIBILITY: her crown-realizing schedule "
                "is sends-before-receives (every send dispatched "
                "before any hub collects — referee-verified to "
                "realize the crown exactly in the one-way model "
                "at N = 3, 4), and the grammar's ONE two-carrier "
                "fused join makes that schedule INEXPRESSIBLE — a "
                "send cannot precede its own receive.  ZG2 shows "
                "where the crown price is actually paid: "
                "dedicated couriers, not more rounds.")

# ============ ZG1S: the round-1 schedule sweep (F1, in-receipt) =============
print("[ZG1S the round-1 schedule sweep (referee F1, the strong "
      "option (d)): CB(4)'s own admissible message multiset + marks "
      "under ALL 8! = 40,320 orderings]")
print("  Rule (the referee's, reproduced exactly): the N min idles "
      "first; the 8 fused deliveries in permuted order; each "
      "round's upper idle IMMEDIATELY after that round's LAST "
      "delivery in the permuted order (marks = the port's own; "
      "round of ported delivery k is k // (N-2)).  The identity "
      "permutation must reproduce the ported CB(4) history "
      "event-for-event (gated).  Per schedule: the full event "
      "poset (the committed event_poset), the dim<=2 verdict, and "
      "the designated-mark crown-violation count vs crown_ref(4).")
print("  Admissibility is NOT re-gated per schedule (idles absorb "
      "unconditionally; genesis deliveries are prefix-blind — the "
      "ZG3 schema, gated mechanically at all 172 base-case events); "
      "it IS re-gated event-by-event on the referee's exemplar "
      "below.  No RNG anywhere: the N = 4 sweeps are EXHAUSTIVE; "
      "the referee's N = 5 sample stays CITED, not rerun.")

def marked_schedule(N, msgs, hubs, perm):
    """The referee's mark rule applied to a permutation of the
    ported delivery list msgs (round of msgs[k] = k // (N-2))."""
    per = N - 2
    last = {}
    for pos, k in enumerate(perm):
        r = k // per
        last[r] = max(last.get(r, -1), pos)
    ev = [('n', f"P{i+1}") for i in range(N)]
    ups = [None] * N
    for pos, k in enumerate(perm):
        ev.append(msgs[k])
        for r in range(N):
            if last.get(r) == pos:
                ups[r] = len(ev)
                ev.append(('n', hubs[r]))
    return ev, list(range(N)), ups

def crown_viol_count(C, mins_s, ups_s, ref):
    idx = mins_s + ups_s
    m = len(idx)
    return sum(C[idx[x]][idx[y]] != ref[x][y]
               for x in range(m) for y in range(m))

actors4s, ev4_port, mins4_port, ups4_port, hubs4 = CB_build(4)
msgs4 = [e for e in ev4_port if e[0] == 'd']
ref4 = crown_ref(4)
ev_id, mins_id, ups_id = marked_schedule(4, msgs4, hubs4,
                                         tuple(range(8)))
check("ZG1S.1 IDENTITY REPRODUCTION: the mark rule applied to the "
      "identity permutation reproduces the ported CB(4) history "
      "EVENT-FOR-EVENT — same 16 events, same order, same "
      "designated mark positions",
      ev_id == ev4_port and mins_id == mins4_port
      and ups_id == ups4_port,
      f"events equal = {ev_id == ev4_port}; ups = {ups_id} vs "
      f"port {ups4_port}")

n_sched = 0
n_dimgt = 0
n_dimgt_s3free = 0
min_viol4 = None
for perm in permutations(range(8)):
    ev_s, mins_s, ups_s = marked_schedule(4, msgs4, hubs4, perm)
    C_s = poset_of(ev_s)
    v_s = crown_viol_count(C_s, mins_s, ups_s, ref4)
    if min_viol4 is None or v_s < min_viol4:
        min_viol4 = v_s
    d2_s, _ = dim_le_2(C_s)
    if not d2_s:
        n_dimgt += 1
        hit_s, _na_s = find_induced_crown(C_s, 3)
        if hit_s is None:
            n_dimgt_s3free += 1
    n_sched += 1
check("ZG1S.2 THE SWEEP CENSUS (the referee's F1 number, "
      "reproduced in-receipt): all 8! = 40,320 marked schedules "
      "enumerated; EXACTLY 248 have whole-poset dim<=2 == False — "
      "the ZG1 'dimension-silent' claim is SCHEDULE-SPECIFIC at "
      "N = 4, now gated, not just review-carried",
      n_sched == 40320 and n_dimgt == 248,
      f"schedules = {n_sched}; dim>2 = {n_dimgt} (referee: 248)")
check("ZG1S.3 THE DESIGNATED CROWN DIES EVERYWHERE: minimum "
      "designated-mark crown-violation count over ALL 40,320 "
      "marked schedules == 4 (> 0 — no schedule of this multiset "
      "realizes her designated S_4 crown)",
      min_viol4 == 4, f"min violations = {min_viol4} (referee: 4)")
check("ZG1S.4 NO INDUCED S_3 ANYWHERE IN THE SWEEP: every one of "
      "the 248 dim>2 schedules was searched directly — ZERO "
      "contain an induced S_3 (their dimension is carried by "
      "non-crown 3-irreducibles); the 40,072 dim<=2 schedules are "
      "S_3-free BY MONOTONICITY (an induced S_3 would force "
      "dim >= 3 [LITERATURE, standard]) — the crown route at "
      "f(4) = 4 actors, <= 16 events of this multiset, is closed "
      "SCHEDULE-INDEPENDENTLY",
      n_dimgt_s3free == n_dimgt,
      f"{n_dimgt_s3free}/{n_dimgt} dim>2 schedules S_3-free")

EX_PERM = (6, 3, 1, 2, 0, 7, 4, 5)
EX_EVENTS = [('n', 'P1'), ('n', 'P2'), ('n', 'P3'), ('n', 'P4'),
             ('d', 'P1', 'P3', V0), ('d', 'P4', 'P1', V0),
             ('d', 'P3', 'P4', V0), ('d', 'P3', 'P1', V0),
             ('n', 'P1'), ('d', 'P2', 'P4', V0), ('n', 'P4'),
             ('d', 'P2', 'P3', V0), ('n', 'P3'),
             ('d', 'P1', 'P2', V0), ('d', 'P4', 'P2', V0),
             ('n', 'P2')]
ev_ex, mins_ex, ups_ex = marked_schedule(4, msgs4, hubs4, EX_PERM)
adm_ex = [admissible(list(ev_ex[:k]), ev_ex[k], actors4s)
          for k in range(len(ev_ex))]
ok_adm_ex = (all(a for a, _q in adm_ex)
             and all(q == (Fr(1, 2) if e[0] == 'n' else Fr(1, 12))
                     for e, (_a, q) in zip(ev_ex, adm_ex)))
C_ex = poset_of(ev_ex)
d2_ex, _ = dim_le_2(C_ex)
v_ex = crown_viol_count(C_ex, mins_ex, ups_ex, ref4)
for k, e in enumerate(ev_ex):
    print(f"    ex e{k:02d} {e!r}  q = {adm_ex[k][1]}")
check("ZG1S.5 THE REFEREE'S EXEMPLAR (frozen round-1 appendix, "
      "schedule (6,3,1,2,0,7,4,5)): reproduced event-for-event "
      "from the appendix listing; EVERY event admitted by the "
      "committed admissible() at the ZG1 weights (idles 1/2, "
      "deliveries 1/12); whole-poset dim<=2 == False; its own "
      "designated marks still violate the crown (5 pairs)",
      ev_ex == EX_EVENTS and ok_adm_ex and d2_ex is False
      and v_ex == 5,
      f"events equal = {ev_ex == EX_EVENTS}; admissible = "
      f"{ok_adm_ex}; dim<=2 = {d2_ex}; violations = {v_ex}")

ok_bare4 = True
n_bare4 = 0
for perm in permutations(range(8)):
    d2_b, _ = dim_le_2(poset_of([msgs4[k] for k in perm]))
    ok_bare4 &= d2_b
    n_bare4 += 1
check("ZG1S.6 BARE DELIVERIES NEVER ESCAPE at N = 4: all 40,320 "
      "orderings of the 8 deliveries ALONE (no idles) are "
      "dim<=2 — the idle marks are LOAD-BEARING for the "
      "dimension escape (the referee's item 3)",
      ok_bare4 and n_bare4 == 40320,
      f"{n_bare4} bare orderings, all dim<=2 = {ok_bare4}")

actors3s, ev3_port, mins3_port, ups3_port, hubs3 = CB_build(3)
msgs3 = [e for e in ev3_port if e[0] == 'd']
ref3 = crown_ref(3)
ev3_id, mins3_id, ups3_id = marked_schedule(3, msgs3, hubs3,
                                            tuple(range(3)))
ok_m3 = True
min_viol3 = None
ok_bare3 = True
for perm in permutations(range(3)):
    ev_s, mins_s, ups_s = marked_schedule(3, msgs3, hubs3, perm)
    C_s = poset_of(ev_s)
    d2_s, _ = dim_le_2(C_s)
    ok_m3 &= d2_s
    v_s = crown_viol_count(C_s, mins_s, ups_s, ref3)
    if min_viol3 is None or v_s < min_viol3:
        min_viol3 = v_s
    d2_b, _ = dim_le_2(poset_of([msgs3[k] for k in perm]))
    ok_bare3 &= d2_b
check("ZG1S.7 THE N = 3 SWEEP IS EXHAUSTIVELY SILENT: identity "
      "reproduction holds at N = 3 too; ALL 6 marked schedules "
      "AND all 6 bare-delivery orderings are dim<=2 (the N = 3 "
      "silence is real — consistent with the frozen d43d "
      "3-actor-2D-through-10 round); the designated crown still "
      "dies at every schedule (minimum 3 violations over all 6)",
      ev3_id == ev3_port and mins3_id == mins3_port
      and ups3_id == ups3_port and ok_m3 and ok_bare3
      and min_viol3 == 3,
      f"marked all dim<=2 = {ok_m3}; bare all dim<=2 = "
      f"{ok_bare3}; min violations = {min_viol3} (referee: 3)")

print("  ZG1S citation (N = 5, NOT rerun): 582 of 4,000 SAMPLED "
      "marked schedules at N = 5 are dim>2 (~15%) — CITED to the "
      "frozen round-1 review (RNG-sampled there; this receipt "
      "runs no RNG, so the number stays review-carried, "
      "definition-level verified by the referee).")
outcome("ZG1S",
        "the round-1 F1 reversal is RECEIPT-GATED: 'dimension-"
        "silent' was a SCHEDULE fact — 248/40,320 marked "
        "schedules of CB(4)'s own admissible multiset+marks have "
        "order dimension > 2 (N = 5: 582/4,000 sampled, cited); "
        "what survives SCHEDULE-INDEPENDENTLY: the designated "
        "crown dies under every schedule (min 4 violations at "
        "N = 4, 3 at N = 3), NO induced S_3 exists anywhere in "
        "the sweep, and the bare deliveries never escape two "
        "clocks — the idle marks are load-bearing.  Her f(N) = N "
        "CROWN route stays closed; her f(N) = N DIMENSION route "
        "is open at N >= 4 on her own multiset.")

# ================== ZG2: the uniform family W(n) ============================
print("[ZG2 the uniform family W(n): S_n as an INDUCED SUBPOSET of a "
      "generated transport record, n = 3, 4, 5, 6]")
print("  Constructor (two-hop dedicated-courier firewall; every "
      "event a genesis delivery): actors m_j, M_j (minima wire "
      "pairs), c_i_j (one dedicated courier per (upper i, minimum "
      "j != i)), h_i (upper hubs), t_i (upper targets) — n^2 + 3n "
      "actors.  Events in order: MIN_j = ('d', m_j, M_j) [n crown "
      "minima, pairwise-disjoint carrier pairs]; hop 1 PU(i,j) = "
      "('d', m_j, c_i_j) for j != i [each sender wire m_j feeds "
      "only FRESH couriers, so wire m_j's cone stays {MIN_j + its "
      "own pickups} — no foreign minima back-flow]; hop 2 SH(i,j) "
      "= ('d', c_i_j, h_i) [hub h_i accumulates exactly the minima "
      "j != i]; U_i = ('d', h_i, t_i) [n crown uppers, "
      "pairwise-disjoint carrier pairs, disjoint from all minima "
      "pairs].  2n^2 events.  Certification is by INDUCED SUBPOSET "
      "on the 2n crown events (pin SS3: for n >= 4 the uppers sit "
      "above n - 1 >= 3 minima — beyond the 2-carrier capacity — so "
      "intermediates are REQUIRED; dimension is monotone under "
      "induced subposets [LITERATURE, standard]; dim(S_n) = n "
      "cited, not re-proved).")

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
            if j != i: ev.append(('d', m[j], cmap[(i, j)], V0))
    for i in range(n):
        for j in range(n):
            if j != i: ev.append(('d', cmap[(i, j)], hb[i], V0))
    for i in range(n):
        ev.append(('d', hb[i], tg[i], V0))
    mins = list(range(n))
    ups = list(range(len(ev) - n, len(ev)))
    return actors, ev, mins, ups

W_RESULTS = {}
ZG4_FIRED = False
for n in (3, 4, 5, 6):
    print(f"  ---- ZG2 n = {n} " + "-" * 44)
    actors, ev, mins, ups = W_build(n)
    A = len(actors)
    q_exp = Fr(1, 4 * (A - 1))
    adm = []
    first_block = None
    for k in range(len(ev)):
        okk, qk = admissible(list(ev[:k]), ev[k], actors)
        pk = probe_clause(list(ev[:k]), ev[k], actors)
        adm.append((okk, qk, pk))
        if not okk and first_block is None:
            first_block = (k, ev[k], pk)
    ok_all = all(okk for okk, _q, _p in adm)
    ok_probe_cons = all((pk is None) == okk for okk, _q, pk in adm)
    ok_w = all(qk == q_exp for _o, qk, _p in adm)
    for k, e in enumerate(ev):
        tagm = (f"  MIN_{mins.index(k)}" if k in mins
                else (f"  U_{ups.index(k)}" if k in ups else ""))
        print(f"    e{k:02d} {e!r}  q = {adm[k][1]}{tagm}")
    print(f"    crown indices: minima = {mins}, uppers = {ups}")
    if not ok_all:
        # the ceiling arm's admission face: deliver the first
        # blocking clause exactly (exit-0 delivered outcome)
        ZG4_FIRED = True
        outcome(f"ZG4 n={n}",
                f"OBSTRUCTION (admission): event e{first_block[0]} "
                f"= {first_block[1]!r} REJECTED by "
                f"{first_block[2]} — the W(n) family stops here.")
        W_RESULTS[n] = (A, len(ev), None, None, False)
        continue
    check(f"ZG2.{n}a EVERY EVENT ADMISSIBLE at n = {n}: all "
          f"{len(ev)} genesis deliveries admitted by the committed "
          f"admissible() at the UNIFORM exact weight 1/(4(A-1)) = "
          f"{q_exp} (A = {A} actors; holdings stay {{v0}} "
          "everywhere); prober agrees on every event",
          ok_all and ok_w and ok_probe_cons,
          f"{len(ev)} events x q = {q_exp}")
    crown_idx = mins + ups
    crown_regs = [regs_of(ev[k]) for k in crown_idx]
    ok_disj = all(not (crown_regs[x] & crown_regs[y])
                  for x in range(2 * n) for y in range(x + 1, 2 * n))
    check(f"ZG2.{n}b CROWN CARRIER DISCIPLINE at n = {n}: the 2n "
          "crown events have pairwise-DISJOINT carrier pairs "
          "(regs_of gated — two deliveries sharing any carrier are "
          "comparable, so this is necessary for the crown's "
          "incomparabilities)",
          ok_disj, f"2n = {2*n} carrier pairs pairwise disjoint")
    C = poset_of(ev)
    Ci = [[C[a][b] for b in crown_idx] for a in crown_idx]
    ref = crown_ref(n)
    if Ci == ref:
        d2, _ = dim_le_2(C)
        wd = width_of(C)
        wb = width_brute(C) if len(ev) <= 16 else None
        mu = q_exp ** len(ev)
        ok_mu = mu == Fr(1, (4 * (A - 1)) ** len(ev))
        check(f"ZG2.{n}c THE INDUCED CROWN at n = {n}: the full "
              f"pairwise comparability matrix of the {2*n} "
              "designated events == the S_n reference EXACTLY "
              "(all 4n^2 entries)",
              Ci == ref, f"matrix {2*n}x{2*n} equal")
        check(f"ZG2.{n}d WHOLE-POSET DIMENSION GATE at n = {n}: the "
              f"full {len(ev)}-event poset FAILS dim<=2 (consistent "
              "with the induced S_n + monotonicity; an oracle PASS "
              "here would be oracle/anchor breakage)",
              not d2, f"dim<=2 = {d2}")
        check(f"ZG2.{n}e WIDTH + MEASURE at n = {n}: width >= n "
              "(sanity: dim <= width, so an S_n-dimension record "
              "NEEDS width >= n); mu = q^events exactly",
              wd >= n and ok_mu
              and (wb is None or wb == wd),
              f"width = {wd}"
              + (f" (brute {wb})" if wb is not None
                 else " (matching only; > 16 elements, declared)")
              + f"; mu = (1/{4*(A-1)})^{len(ev)} (denominator "
              f"{len(str(mu.denominator))} digits)")
        W_RESULTS[n] = (A, len(ev), wd, q_exp, True)
        outcome(f"ZG2 n={n}",
                f"WITNESS — S_{n} REALIZED as an induced subposet "
                f"of an admissible pure-transport record: {A} "
                f"actors, {len(ev)} events, width {wd}, every "
                f"event at exact weight {q_exp}; the whole poset "
                f"fails dim<=2 (order dimension >= {n} by "
                "monotonicity + dim(S_n) = n [LITERATURE]).")
    else:
        # the ceiling arm's order face: deliver the obstruction
        # exactly (which pairwise relation failed)
        ZG4_FIRED = True
        bad = []
        for x in range(2 * n):
            for y in range(2 * n):
                if Ci[x][y] != ref[x][y]:
                    nx = (f"MIN_{x}" if x < n else f"U_{x-n}")
                    ny = (f"MIN_{y}" if y < n else f"U_{y-n}")
                    bad.append(f"{nx} < {ny} is "
                               f"{Ci[x][y]} (reference "
                               f"{ref[x][y]})")
        outcome(f"ZG4 n={n}",
                f"OBSTRUCTION (order): the induced matrix deviates "
                f"from S_{n} at {len(bad)} pairs — first: "
                f"{bad[0]} — the unrealizable relation delivered.")
        for b in bad[:8]:
            print(f"      {b}")
        W_RESULTS[n] = (A, len(ev), None, q_exp, False)
    if n == 3 and W_RESULTS[3][4]:
        okW6cls = (Ci == crown_ref(3) and Ci == poset_of(W6))
        check("ZG2.3f the n = 3 arm LANDS IN THE W6 CLASS (pin ZG2): "
              "W(3)'s induced crown matrix == crown_ref(3) == the "
              "committed W6 witness's full poset matrix — the same "
              "order S3, here realized through intermediates (W6 "
              "itself is the carrier-capacity-minimal member: 6 "
              "events, the ZG0 size floor)",
              okW6cls, "matrices equal")

# ================= ZG3: the all-n schema (the uniform arm) ==================
print("[ZG3 the general-n schema]")
ALL_WITNESS = all(W_RESULTS.get(n, (0, 0, 0, 0, False))[4]
                  for n in (3, 4, 5, 6))
if ALL_WITNESS:
    ok_forms = True
    for n in (3, 4, 5, 6):
        A, E, wd, q, _ok = W_RESULTS[n]
        ok_forms &= (A == n * n + 3 * n and E == 2 * n * n
                     and q == Fr(1, 4 * (n * n + 3 * n - 1)))
    check("ZG3.1 SCHEMA CLOSED FORMS gated at the base cases n = "
          "3, 4, 5, 6: actors(n) = n^2 + 3n; events(n) = 2n^2 "
          "(n minima + n(n-1) hop-1 + n(n-1) hop-2 + n uppers); "
          "crown = the first n and last n events; per-event weight "
          "= 1/(4(n^2 + 3n - 1)) UNIFORM over the whole history "
          "(gated event-by-event above)",
          ok_forms, "4/4 base cases match the closed forms")
    print("  ZG3 schema (the parameter counts as functions of n):")
    print("    actors(n)  = n^2 + 3n   [m_j, M_j, h_i, t_i: 4n; "
          "couriers c_i_j: n(n-1)]")
    print("    events(n)  = 2n^2       [n + n(n-1) + n(n-1) + n]")
    print("    weight(n)  = 1/(4(n^2 + 3n - 1)) per event, uniform;")
    print("      mu(n)    = weight(n)^(2n^2)")
    print("    crown(n)   = events 0..n-1 (MIN_j) and 2n^2-n.."
          "2n^2-1 (U_i)")
    print("    width measured at the base cases: "
          + ", ".join(f"f({n}) = {W_RESULTS[n][2]}"
                      for n in (3, 4, 5, 6))
          + "  [MEASURED = 2n - 1 at all four base cases; each "
          ">= n as dim <= width requires; the all-n width formula "
          "is NOT claimed]")
    print("    step n -> n+1: add actors m_n, M_n, h_n, t_n + "
          "couriers c_n_j, c_i_n (2n + 4 actors); add MIN_n, "
          "hop-1/hop-2 rows PU/SH(n, j) and columns PU/SH(i, n), "
          "U_n (4n + 2 events).")
    print("    the admissibility schema is PREFIX-BLIND: every event "
          "is a genesis delivery ('d', s, r, v0) with s != r in the "
          "actor tuple; in a pure genesis-delivery history every "
          "actor's holdings stay {v0} (a delivery of v0 adds no new "
          "version), so the sender-view option set is always the "
          "full {(r, v0): r != s} of size A - 1 and d-clauses 1-3 "
          "cannot fire — gated mechanically at all 172 events of "
          "the four base cases (the all-n induction is the SS8 "
          "proof note — pointer fixed per round-1 N2; SS6/SS7 of "
          "the note are amendment sections — written at "
          "conversion by the author, not claimed by this "
          "receipt).")
    outcome("ZG3", "the constructor is UNIFORM in n: closed-form "
            "schema delivered with 4/4 mechanical base cases; the "
            "all-n statement is a [THEOREM candidate] carrying "
            "these receipts (author's proof note at conversion).")
else:
    print("  ZG3 not available: the uniform arm did not survive all "
          "base cases (see the ZG4 obstruction outcomes above).")

# ==================== ZG4: the ceiling arm (branch state) ===================
print("[ZG4 the ceiling arm]")
if not ZG4_FIRED:
    print("  ZG4 NOT FIRED: no admission clause and no unrealizable "
          "pairwise relation anywhere in ZG2 (the obstruction "
          "machinery is live — exercised by ZG1.0's synthetic "
          "clause exhibits and the ZG2 branch structure — but the "
          "record went to the witness horn at every n).")

# ========================== ZG5: accounting =================================
print("[ZG5 accounting: f(n) censused vs Charron-Bost's f(N) = N]")
print("    n | actors | events | width | per-event weight | mu")
for n in (3, 4, 5, 6):
    A, E, wd, q, okn = W_RESULTS[n]
    if okn:
        print(f"    {n} | {A:6d} | {E:6d} | {wd:5d} | {q} "
              f"| (1/{4*(A-1)})^{E}")
    else:
        print(f"    {n} | {A:6d} | {E:6d} |  the ceiling arm fired "
              "(see ZG4)")
print("  Charron-Bost comparison [LITERATURE]: her model realizes "
      "dimension N with f(N) = N processes and one-way messages; "
      "the transport grammar refuses HER SCHEDULE, not her "
      "dimension (round-1 F1 scope): the PORTED sequential-round "
      "schedules are dim <= 2 at N = 3, 4, 5 actors, but ZG1S "
      "gates that 248/40,320 reorderings of the same admissible "
      "multiset+marks reach dimension 3 at N = 4 — what is closed "
      "SCHEDULE-INDEPENDENTLY is her designated CROWN (dead under "
      "every schedule; no induced S_3 anywhere; bare deliveries "
      "never escape).  For the CERTIFIED crown the grammar pays "
      "n^2 + 3n actors / 2n^2 fused joins instead (ZG2).  At "
      "n = 3 the committed record's minimal witness is W6: 6 "
      "actors / 6 events — the ZG0 size floor; the uniform "
      "constructor is NOT claimed minimal at any n.")

# ========================== ZG6: discipline =================================
print("[ZG6 discipline]")
check("ZG6.1 width DIAGNOSTICS DELIVERED (label aligned to the "
      "boolean, round-1 N3): this gate verifies ONLY that a width "
      "value was delivered for every surviving W(n) arm and that "
      "all three CB ports were censused; the brute-vs-matching "
      "cross-gates ran INLINE (ZG0.2 on all 219 4-posets, ZG0.4, "
      "ZG1.Nc on every candidate with <= 16 elements); NO W(n) "
      "poset receives a brute check (all > 16 elements — "
      "matching-only there, declared); the n < 6 vacuity floor is "
      "CITED (ZG0 note)",
      all(W_RESULTS[n][2] is not None for n in (3, 4, 5, 6)
          if W_RESULTS[n][4]) and len(CB_RESULTS) == 3,
      "diagnostics delivered in-line above")
_T1 = "Mink" "owski"      # scan tokens split across literals so
_T2 = "space" "time"      # these lines never self-trigger the scan
_DISCLAIM = ("NEVER", "NO ", "successor")
_scan_hits = 0
_scan_bad = []
for _ln, _line in enumerate(open(__file__).read().splitlines(), 1):
    if _T1 in _line or _T2 in _line:
        _scan_hits += 1
        if not any(_d in _line for _d in _DISCLAIM):
            _scan_bad.append(_ln)
check("ZG6.2 scoping discipline (pin SS1) — now a MECHANICAL "
      "self-scan, round-1 F3 (was a vacuous check(True)): every "
      "source line naming Minkowski or spacetime carries NO bare "
      "claim — each such line must also contain a disclaimer "
      "marker (NEVER / NO / successor); the scan is LIVE (token "
      "lines counted, >= 4 expected) and finds zero undisclaimed "
      "lines; order dimension stays a 1+1-escape detector and "
      "clock-complexity grade throughout",
      _scan_bad == [] and _scan_hits >= 4,
      f"{_scan_hits} token lines scanned, {len(_scan_bad)} "
      "undisclaimed" + (f" (lines {_scan_bad})" if _scan_bad
                        else ""))
print("  ZG6.3 note (round-1 F3: DEMOTED from a vacuous "
      "check(True) to a printed note — not counted in the PASS "
      "tally): exit design (#354 binding) — witness and ceiling "
      "are both exit-0 delivered outcomes (the ZG2 branch "
      "structure above; the ceiling branch prints its obstruction "
      "and continues); exit 1 is reserved for anchor/oracle/"
      "admission-internal breakage = any FAIL in this tally.  The "
      "wiring is demonstrated by the note SS6 A5 scratchpad "
      "mutant battery (constructor corruption -> ZG4 ceiling "
      "outcomes AT exit 0; oracle/weight corruption -> exit 1), "
      "independently confirmed by the round-1 referee's "
      "MUT1-MUT6 battery.")

# ============================== verdict =====================================
print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL; "
      f"{len(OUTCOMES)} delivered outcomes")
if FAIL:
    print("[VERDICT] FAIL — anchor/oracle/admission-internal "
          "breakage; exit 1")
    sys.exit(1)
nw = sum(1 for n in (3, 4, 5, 6)
         if W_RESULTS.get(n, (0, 0, 0, 0, False))[4])
if nw == 4:
    print("[VERDICT] d45b delivered — THE WITNESS HORN: the "
          "transport grammar is NOT dimension-confined at the "
          "tested ladder.  S_n is realized as an induced subposet "
          "of an admissible pure-transport generated record at "
          "every n in {3, 4, 5, 6} by ONE uniform constructor "
          "(actors n^2 + 3n, events 2n^2, uniform exact weights), "
          "with the general-n schema delivered (ZG3) — the "
          "necessary condition for any round-cone reading HOLDS at "
          "the base cases, as ORDER dimension only (pin SS1).  The "
          "Charron-Bost port (ZG1) is fully admissible and its "
          "PORTED sequential-round schedules are dim <= 2 at "
          "N = 3, 4, 5 actors — a SCHEDULE fact, not a "
          "pattern/semantics fact (round-1 F1, gated in ZG1S: "
          "248/40,320 reorderings of her own admissible "
          "multiset+marks reach dimension 3 at N = 4); what is "
          "closed schedule-independently is her designated CROWN "
          "(dead everywhere; no induced S_3; bare deliveries "
          "never escape — idles are load-bearing), NOT her "
          "dimension route; no admission clause fires anywhere.  "
          "The grammar's certified crown price is paid in "
          "dedicated couriers instead.  Exit 0.")
else:
    print("[VERDICT] d45b delivered — THE CEILING ARM: the uniform "
          "family stops (see the ZG4 obstruction outcomes); the "
          "polyhedral-confinement reading stands at the failed n.  "
          "Exit 0.")
sys.exit(0)

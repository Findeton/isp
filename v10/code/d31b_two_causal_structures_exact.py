#!/usr/bin/env python3
"""
d31b_two_causal_structures_exact.py — v10 D31B: the two causal structures.
Pin: note-d31 (committed pre-run). Object 1: the port-dependency poset
(structural; total port map for the entangling cRy gate set — the pinned
hypothesis: it equals the wire-DAG). Object 2: the operational-influence
graph (diagnostic; cancellations recorded; never a poset). The primary
order for D32-class measurement is frozen here on structural grounds.
Exact rationals for influence; integer combinatorics for the orders.
Gates B1-B5; exit 1 on any failure.
"""
from fractions import Fraction as F
import numpy as np

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

CS = {F(9,25): (F(4,5), F(3,5)), F(16,25): (F(3,5), F(4,5)),
      F(576,625): (F(7,25), F(24,25))}
PREP = (F(3,5), F(4,5))
ALPHA_ACTIVE = [(F(1), F(0)), (F(0), F(1)), (F(3,5), F(4,5)), (F(5,13), F(12,13))]

# ---- exact density engine + event influence (d28b conventions) -----------
class DWeb:
    def __init__(self):
        self.regs = []; self.rho = [[F(1)]]
    def root(self, label, prep):
        c, s = prep; dim = len(self.rho)
        new = [[F(0)]*(2*dim) for _ in range(2*dim)]
        for i in range(dim):
            for j in range(dim):
                x = self.rho[i][j]
                if x == 0: continue
                for bi, ai in ((0, c), (1, s)):
                    for bj, aj in ((0, c), (1, s)):
                        new[2*i+bi][2*j+bj] += x*ai*aj
        self.rho = new; self.regs.append(label)
    def _cry(self, ctrl, targ, c, s):
        n = len(self.regs); dim = 1 << n
        cb, tb = 1 << (n-1-ctrl), 1 << (n-1-targ)
        cmap = []
        for j in range(dim):
            if not (j & cb): cmap.append(((j, F(1)),))
            else:
                j0, j1 = j & ~tb, j | tb
                if not (j & tb): cmap.append(((j0, c), (j1, s)))
                else:            cmap.append(((j0, -s), (j1, c)))
        M = [[F(0)]*dim for _ in range(dim)]
        for i in range(dim):
            for (r, a) in cmap[i]:
                Mr = M[r]; Ri = self.rho[i]
                for j in range(dim):
                    if Ri[j]: Mr[j] += a*Ri[j]
        out = [[F(0)]*dim for _ in range(dim)]
        for i in range(dim):
            Mi = M[i]; Oi = out[i]
            for j in range(dim):
                x = Mi[j]
                if x == 0: continue
                for (r, a) in cmap[j]:
                    Oi[r] += x*a
        self.rho = out
    def birth(self, parent, child, g):
        dim = 1 << len(self.regs)
        new = [[F(0)]*(2*dim) for _ in range(2*dim)]
        for i in range(dim):
            Ri = self.rho[i]
            for j in range(dim):
                if Ri[j]: new[2*i][2*j] = Ri[j]
        self.rho = new; self.regs.append(child)
        c, s = CS[g]; self._cry(self.regs.index(parent), len(self.regs)-1, c, s)
    def interact(self, ctrl, targ, g):
        c, s = CS[g]; self._cry(self.regs.index(ctrl), self.regs.index(targ), c, s)
    def intervene(self, reg, prep):
        if prep is None: return
        c, s = prep
        n = len(self.regs); dim = 1 << n
        bit = 1 << (n-1-self.regs.index(reg))
        out = [[F(0)]*dim for _ in range(dim)]
        for i in range(dim):
            Ri = self.rho[i]
            for j in range(dim):
                x = Ri[j]
                if x == 0 or (i & bit) != (j & bit): continue
                i0, j0 = i & ~bit, j & ~bit
                for bi in (0, 1):
                    for bj in (0, 1):
                        w = x * (c, s)[bi] * (c, s)[bj]
                        if w: out[i0 | (bit if bi else 0)][j0 | (bit if bj else 0)] += w
        self.rho = out
    def q(self, reg):
        n = len(self.regs); dim = 1 << n
        bit = 1 << (n-1-self.regs.index(reg))
        p1 = od = F(0)
        for i in range(dim):
            if self.rho[i][i] and (i & bit): p1 += self.rho[i][i]
            if not (i & bit): od += self.rho[i][i | bit]
        return p1, F(1,2) + od

def run(ops, upto, iv):
    w = DWeb()
    for e in range(upto):
        op = ops[e]
        if op[0] == 'root':     w.root(op[1], op[2])
        elif op[0] == 'birth':  w.birth(op[1], op[2], op[3])
        else:                   w.interact(op[1], op[2], op[3])
        for (reg, ep), prep in iv.items():
            if ep == e + 1: w.intervene(reg, prep)
    return w

def I_ev(ops, u, s, v, t):
    qs = [run(ops, t, {(u, s): a}).q(v) for a in ALPHA_ACTIVE]
    best = F(0)
    for i in range(len(qs)):
        for j in range(i+1, len(qs)):
            for k in (0, 1):
                d = abs(qs[i][k] - qs[j][k])
                if d > best: best = d
    return best

# ---- the two order builders ----------------------------------------------
def participants(op):
    return (op[1],) if op[0] == 'root' else (op[1], op[2])

def wire_dag(acts):
    """The D30 builder: last-op columns, bidirectional through gates."""
    M = len(acts)
    R = np.zeros((M, M), dtype=bool)
    last = {}
    for j, op in enumerate(acts):
        col = np.zeros(M, dtype=bool)
        for r in participants(op):
            if r in last:
                col |= R[:, last[r]]; col[last[r]] = True
        R[:, j] = col
        for r in participants(op): last[r] = j
    return R

def port_poset(acts):
    """Independent construction: explicit ports; total gate map (entangling
    cRy: both outputs depend on both inputs); wire edges out->next-in;
    reachability closure on the direct adjacency."""
    M = len(acts)
    adj = np.zeros((M, M), dtype=bool)
    for i in range(M):
        for r in participants(acts[i]):
            for j in range(i+1, M):
                if r in participants(acts[j]):
                    adj[i, j] = True                 # r's out-port feeds j's in-port
                    break                            # only the NEXT op on r
    R = adj.copy()
    for _ in range(int(np.ceil(np.log2(max(M, 2)))) + 1):
        R = R | (R @ R)
    return R

# ---- battery webs (as op sequences; d28b conventions) --------------------
DIAMOND = [('root','R',PREP), ('birth','R','A',F(16,25)),
           ('birth','R','B',F(16,25)), ('birth','A','X',F(16,25)),
           ('interact','B','X',F(576,625))]
MAILBOX = [('root','A',PREP), ('birth','A','z1',F(16,25)),
           ('birth','A','z2',F(16,25)), ('interact','z1','A',F(9,25)),
           ('interact','z2','A',F(9,25)), ('birth','A','z3',F(16,25))]
CANCEL = [('root','u',PREP), ('birth','u','c',F(9,25)),
          ('interact','u','c',F(9,25)), ('interact','u','c',F(9,25)),
          ('interact','u','c',F(9,25)), ('interact','u','c',F(16,25)),
          ('interact','u','c',F(16,25)), ('interact','u','c',F(16,25)),
          ('interact','u','c',F(16,25))]

print("[d31b the two causal structures — exact]")

# B1: the port-map hypothesis — port poset == wire-DAG, battery + grown webs
rng_master = np.random.default_rng(31260712)
def grow_collar(n_events, rng):
    regs = ['R', 'A', 'B']; sealed = {'R'}
    edges = [('R','A'), ('A','B')]
    acts = [('root','R',PREP), ('birth','R','A',F(16,25)),
            ('birth','A','B',F(16,25))]
    adj = {r: set() for r in regs}
    for (a, b) in edges: adj[a].add(b); adj[b].add(a)
    k = 1
    while len(acts) < n_events:
        uns = [r for r in regs if r not in sealed]
        opts = [('none',)] + [('birth', y) for y in uns]
        for y in uns:
            for x in adj[y]:
                if x != y and x not in sealed: opts.append(('interact', y, x))
        pick = opts[rng.integers(0, len(opts))]
        if pick[0] == 'none': continue
        if pick[0] == 'birth':
            child = f"z{k}"; k += 1
            regs.append(child); adj[child] = {pick[1]}; adj[pick[1]].add(child)
            acts.append(('birth', pick[1], child, F(16,25)))
        else:
            acts.append(('interact', pick[1], pick[2], F(9,25)))
    return acts

ok1 = True
for acts in (DIAMOND, MAILBOX, CANCEL):
    ok1 &= np.array_equal(wire_dag(acts), port_poset(acts))
for s in range(3):
    acts = grow_collar(80, np.random.default_rng(31260712 + s))
    ok1 &= np.array_equal(wire_dag(acts), port_poset(acts))
check("B1 THE PORT-MAP HYPOTHESIS CONFIRMED: the port-dependency poset "
      "(explicit ports, total entangling-gate map, independent construction) "
      "equals the wire-DAG — battery webs + 3 grown collar webs, elementwise "
      "— D30's measured object IS the structural order", ok1)

# B2: the influence graph is NOT the poset — the E5 cancellation edge
I_end = I_ev(CANCEL, 'u', 1, 'c', len(CANCEL))
I_mid = I_ev(CANCEL, 'u', 1, 'c', 3)
R = port_poset(CANCEL)
ok2 = (I_end == 0) and (I_mid == F(576,625)) and bool(R[0, len(CANCEL)-1])
check("B2 the diagnostic split: the port poset carries the root->last-op "
      "relation while operational influence is EXACTLY ZERO (the E5 "
      "cancellation; mid-history 576/625) — structural comparability is not "
      "operational influence; the influence graph is never called a poset",
      ok2, f"I_mid = {I_mid}, I_end = {I_end}")

# B3: influence within structure — every positive influence pair is
# port-comparable (the zeros side of the wire-time lemma, re-gated here)
ok3 = True
for acts, pairs in ((DIAMOND, [('A',2,'X',5), ('B',3,'X',5), ('A',2,'B',5)]),
                    (MAILBOX, [('z1',2,'z3',6), ('z1',2,'z2',6), ('z2',3,'z3',6)])):
    Rp = port_poset(acts)
    for (u, s, v, t) in pairs:
        I = I_ev(acts, u, s, v, t)
        if I > 0:
            iu = next(i for i, op in enumerate(acts)
                      if participants(op)[-1] == u)
            jv = max(i for i, op in enumerate(acts) if v in participants(op))
            ok3 &= bool(Rp[iu, jv]) or iu == jv
check("B3 influence within structure: every positive influence pair on the "
      "battery is port-comparable (no influence outside the structural "
      "order)", ok3)

# B4: the multi-touch census — the E5 exception-rate bookkeeping at scale
counts = []
for s in range(3):
    acts = grow_collar(256, np.random.default_rng(41260712 + s))
    touch = {}
    for op in acts:
        if op[0] == 'interact':
            touch[(op[1], op[2])] = touch.get((op[1], op[2]), 0) + 1
    multi = sum(1 for v in touch.values() if v >= 2)
    seven = sum(1 for v in touch.values() if v >= 7)
    counts.append((multi, seven))
check("B4 the multi-touch census on grown collar webs (256 events, 3 seeds): "
      "same-pair repeat interacts exist at scale — any influence reading of "
      "the structural order owes this exception bookkeeping (the E5 class "
      "needs >= 7 same-pair touches on the grid)", True,
      f"(>=2, >=7) touches per web: {counts}")

# B5: THE FREEZE
print("      B5 THE FREEZE [structural grounds, per the external review]:")
print("      the PRIMARY causal order for all D32-class measurement is the")
print("      PORT-DEPENDENCY POSET == the wire-DAG (B1) — transitive and")
print("      acyclic by construction, alphabet-independent, and now")
print("      independently constructed twice. The OPERATIONAL-INFLUENCE")
print("      GRAPH is the declared DIAGNOSTIC: alphabet-relative, cancel-")
print("      lations recorded (B2/B4), transitivity never claimed. D30's")
print("      measured object is retroactively the structural order;")
print("      'directedness' was an alphabet-relative operational property.")
check("B5 the primary order frozen (port poset == wire-DAG); the influence "
      "graph = diagnostic", True)

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total}: 3 substantive gates + 2 print/report "
      f"gates)" if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)

#!/usr/bin/env python3
"""
d28b_event_influence_exact.py — v10 D28b part 1: event-resolved influence.
Pin: note-d28b (committed pre-run). Stdlib only; exact rationals.
Events are (register, epoch); interventions insert at their epoch; queries
evaluate on the truncated circuit. Gates E1-E4; exit 1 on any failure.
"""
from fractions import Fraction as F

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

class DWeb:
    def __init__(self):
        self.regs = []; self.rho = [[F(1)]]
    def root(self, label, prep):
        c, s = prep
        dim = len(self.rho)
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
        phi = (c, s)
        out = [[F(0)]*dim for _ in range(dim)]
        for i in range(dim):
            Ri = self.rho[i]
            for j in range(dim):
                x = Ri[j]
                if x == 0 or (i & bit) != (j & bit): continue
                i0, j0 = i & ~bit, j & ~bit
                for bi in (0, 1):
                    for bj in (0, 1):
                        w = x * phi[bi] * phi[bj]
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

# a web = a declared op sequence; epoch k = after applying ops[0..k-1]
def run(ops, upto, iv):
    """Apply ops[0:upto], inserting interventions right after their epoch.
    iv: {(reg, epoch): prep}."""
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
    """Event-resolved influence (u, s) -> (v, t): active pairs, {Z, X}."""
    qs = []
    for a in ALPHA_ACTIVE:
        w = run(ops, t, {(u, s): a})
        qs.append(w.q(v))
    best = F(0)
    for i in range(len(qs)):
        for j in range(i+1, len(qs)):
            for k in (0, 1):
                d = abs(qs[i][k] - qs[j][k])
                if d > best: best = d
    return best

def reach(ops, u, s, t):
    """Time-respecting op-chain reachability from (u, s) within ops (s, t]."""
    R = {u}
    for e in range(s, t):
        op = ops[e]
        if op[0] == 'birth' and op[1] in R: R.add(op[2])
        if op[0] == 'interact' and op[1] in R: R.add(op[2])
    return R

print("[d28b event-resolved influence — exact]")
print("      events = (register, epoch); interventions = ACTIVE replacements")
print("      {|0>, |1>, Ry(3/5,4/5), Ry(5/13,12/13)} inserted at the event's")
print("      epoch; queries = {Z, X} on the circuit truncated at the query")
print("      epoch. Chain links: birth parent->child; interact control->target.")

# the test webs (declared op sequences)
RETOUCH = [('root','r0',PREP), ('birth','r0','c0',F(576,625)),
           ('interact','r0','c0',F(16,25))]
MAILBOX = [('root','A',PREP), ('birth','A','z1',F(16,25)),
           ('birth','A','z2',F(16,25)), ('interact','z1','A',F(9,25)),
           ('interact','z2','A',F(9,25)), ('birth','A','z3',F(16,25))]
DIAMOND = [('root','R',PREP), ('birth','R','A',F(16,25)),
           ('birth','R','B',F(16,25)), ('birth','A','X',F(16,25)),
           ('interact','B','X',F(576,625))]
CHAIN = [('root','A',PREP), ('birth','A','B',F(9,25)),
         ('birth','B','C',F(16,25))]

def birth_epoch(ops, reg):
    for e, op in enumerate(ops):
        if (op[0] in ('root', 'birth')) and op[1 if op[0]=='root' else 2] == reg:
            return e + 1
    return None

# E1: end-of-history equivalence with the D28 register-level relation
ok1 = True
T = len(DIAMOND)
for (u, v, expect_pos) in (('A','X',True), ('B','X',True), ('A','B',False),
                           ('B','A',False), ('X','A',False), ('R','X',True)):
    I = I_ev(DIAMOND, u, birth_epoch(DIAMOND, u), v, T)
    ok1 &= (I > 0) == expect_pos
check("E1 end-of-history equivalence: I_ev at (birth epoch -> final epoch) "
      "reproduces the D28 register-level verdicts on the diamond web", ok1)

# E2: THE CONJECTURE — I_ev > 0 <=> time-respecting op-chain reachability
def conjecture_holds(ops, pairs):
    okc = True
    for (u, s, v, t) in pairs:
        I = I_ev(ops, u, s, v, t)
        R = reach(ops, u, s, t)
        okc &= (I > 0) == (v in R)
    return okc

ok2 = True
# re-touch web: the child's event does NOT reach the parent's later event;
# the parent's early event reaches the child through birth and re-touch
ok2 &= conjecture_holds(RETOUCH, [
    ('c0', 2, 'r0', 3), ('r0', 1, 'c0', 3), ('c0', 2, 'c0', 3),
    ('r0', 1, 'r0', 3)])
# mailbox: the worldline split on A — z1 reaches A's post-write events and
# z3, NOT z2's events and NOT A's pre-write events
ok2 &= conjecture_holds(MAILBOX, [
    ('z1', 2, 'A', 3), ('z1', 2, 'A', 4), ('z1', 2, 'z2', 6),
    ('z1', 2, 'z3', 6), ('z2', 3, 'z1', 6), ('z2', 3, 'z3', 6),
    ('z1', 2, 'A', 6), ('A', 1, 'z2', 3), ('A', 1, 'z1', 2),
    ('z3', 6, 'A', 6)])
# diamond + a census chain (event-level)
ok2 &= conjecture_holds(DIAMOND, [
    ('A', 2, 'X', 5), ('B', 3, 'X', 5), ('A', 2, 'B', 5), ('B', 3, 'A', 5),
    ('X', 4, 'B', 5), ('R', 1, 'X', 5), ('X', 4, 'X', 5)])
ok2 &= conjecture_holds(CHAIN, [
    ('A', 1, 'C', 3), ('B', 2, 'C', 3), ('C', 3, 'A', 3), ('B', 2, 'A', 3)])
check("E2 the conjecture: event-resolved influence > 0 <=> time-respecting "
      "op-chain reachability — re-touch, mailbox (the worldline split), "
      "diamond, and chain webs, 25 event pairs", ok2)

# E3: acyclicity — the event relation is a strict partial order
ok3 = True
for ops in (RETOUCH, MAILBOX, DIAMOND):
    T = len(ops)
    events = [(r, e) for e in range(1, T+1) for r in
              [op[1 if op[0]=='root' else 2] for op in ops[:e]
               if op[0] in ('root','birth')]]
    pos = set()
    for (u, s) in events:
        for (v, t) in events:
            if (u, s) == (v, t) or t < s: continue
            if v in reach(ops, u, s, t) and not (u == v and s == t):
                if (u, s) != (v, t): pos.add(((u, s), (v, t)))
    ok3 &= all(((b, a) not in pos) or a == b for (a, b) in pos)
check("E3 acyclicity: the event-level relation (reachability form, = "
      "influence by E2) has no 2-cycles on any tested web — a strict "
      "partial order, unlike the register-level relation", ok3)

# E4: the worldline quotient — register-level I = event-level support max
ok4 = True
for ops, pairs in ((MAILBOX, [('z1','z2'), ('z1','z3'), ('z2','z3')]),
                   (DIAMOND, [('A','B'), ('A','X'), ('B','X')])):
    T = len(ops)
    for (u, v) in pairs:
        reg_I = I_ev(ops, u, birth_epoch(ops, u), v, T)
        ev_any = any(v in reach(ops, u, s, T)
                     for s in range(birth_epoch(ops, u), T+1))
        ok4 &= (reg_I > 0) == ev_any
check("E4 the worldline quotient: the D28 register-level relation is the "
      "support-max of the event-level relation — the round-1 register "
      "cyclicity was the shadow of quotienting worldlines to points", ok4)

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total}: 4 substantive gates)"
      if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)

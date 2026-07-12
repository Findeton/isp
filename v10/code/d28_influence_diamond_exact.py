#!/usr/bin/env python3
"""
d28_influence_diamond_exact.py — v10 D28 receipt 1: the (A,Q)-relative
influence relation, the tree influence theorem, the tree no-go, and the
minimal operational diamond. Pin: note-d28 (committed pre-run).
Stdlib only; exact rationals; real density-matrix engine.
Gates T0-T3 per the pin; exit 1 on any failure.
"""
from fractions import Fraction as F
from itertools import permutations, product

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

# ---- real density-matrix engine (sparse controlled-Ry application) ----
class DWeb:
    def __init__(self, roots):
        """roots: list of (label, (c, s)) prepared product registers."""
        self.regs = [lab for lab, _ in roots]
        dim = 1 << len(self.regs)
        self.rho = [[F(0)]*dim for _ in range(dim)]
        amps = [F(1)]
        for _, (c, s) in roots:
            amps = [a*x for a in amps for x in (c, s)]
        for i, ai in enumerate(amps):
            if ai == 0: continue
            for j, aj in enumerate(amps):
                if aj: self.rho[i][j] = ai*aj
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
        c, s = CS[g]
        self._cry(self.regs.index(parent), len(self.regs)-1, c, s)
    def interact(self, ctrl, targ, g):
        c, s = CS[g]
        self._cry(self.regs.index(ctrl), self.regs.index(targ), c, s)
    def intervene(self, reg, prep):
        """Unconditioned replacement of `reg` with the pure state (c, s);
        prep None = no-op. No postselection."""
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
    def r1(self, reg):
        """Reduced 1-register state: (p0, p1, offdiag)."""
        n = len(self.regs); dim = 1 << n
        bit = 1 << (n-1-self.regs.index(reg))
        p0 = p1 = od = F(0)
        for i in range(dim):
            if self.rho[i][i]:
                if i & bit: p1 += self.rho[i][i]
                else:       p0 += self.rho[i][i]
            if not (i & bit):
                j = i | bit
                od += self.rho[i][j]
        return p0, p1, od
    def zdiag(self, reg):
        return self.r1(reg)[:2]

# queries Q = {Z, X} on the target register (real family: tomographically complete)
def queries(web, reg):
    p0, p1, od = web.r1(reg)
    return (p1,                      # Z: P(1)
            F(1,2) + od)             # X: P(+)

ALPHA = [None, (F(1), F(0)), (F(0), F(1)), (F(3,5), F(4,5)), (F(5,13), F(12,13))]

def influence(builder, u, v):
    """I_{A,Q}(u -> v): max over intervention pairs and queries of |dP|.
    builder(intervention_map) -> DWeb; intervention applied at u's site
    immediately after u's birth."""
    qs = [queries(builder({u: a}), v) for a in ALPHA]
    best = F(0)
    for i in range(len(qs)):
        for j in range(i+1, len(qs)):
            for k in (0, 1):
                d = abs(qs[i][k] - qs[j][k])
                if d > best: best = d
    return best

# ---- tree machinery (census import, D24 conventions) ----
def rooted_trees(children):
    nodes = ['A'] + children
    for parents in product(*[[p for p in nodes if p != ch] for ch in children]):
        pm = dict(zip(children, parents)); good = True
        for ch in children:
            seen, cur = set(), ch
            while cur != 'A':
                if cur in seen or cur not in pm: good = False; break
                seen.add(cur); cur = pm[cur]
            if not good: break
        if good: yield pm

def schedule_of(pm):
    out, placed = [], {'A'}
    while len(out) < len(pm):
        for ch in sorted(pm):
            if ch not in placed and pm[ch] in placed:
                out.append(ch); placed.add(ch)
    return out

def descendants(pm, u):
    out = set()
    for v in pm:
        cur = v
        while cur != 'A' and cur in pm:
            cur = pm[cur]
            if cur == u: out.add(v); break
    return out

def tree_builder(pm, gm, sched):
    def build(iv):
        w = DWeb([('A', PREP)])
        w.intervene('A', iv.get('A'))
        for ch in sched:
            w.birth(pm[ch], ch, gm[ch])
            w.intervene(ch, iv.get(ch))
        return w
    return build

print("[d28 influence + diamond — exact]")
print("      alphabets printed: A = {no-op, prep|0>, prep|1>, Ry(3/5,4/5),")
print("      Ry(5/13,12/13)} (unconditioned replacements, no postselection);")
print("      Q = {Z, X} (tomographically complete for the real family;")
print("      enrichment of either alphabet can only enlarge the relation).")

# T0: A0a exhibit — isometric birth = blank activation + unitary (kinematic)
w1 = DWeb([('A', PREP)]); w1.birth('A', 'B', F(16,25))
w2 = DWeb([('A', PREP), ('B', (F(1), F(0)))])   # blank first...
w2.interact('A', 'B', F(16,25))                  # ...then the unitary
r1m = [row[:] for row in w1.rho]
ok0 = all(r1m[i][j] == w2.rho[i][j] for i in range(4) for j in range(4))
check("T0 (A0a): birth == blank-activation-then-unitary, exact on the state "
      "(kinematic normal form; locality NOT claimed — A0c)", ok0)

# T1: the tree influence theorem, exhaustive over the census
ok1 = True; n_pairs = 0
for children in (['B','C'], ['B','C','D']):
    for pm in rooted_trees(children):
        gm = {ch: g for ch, g in zip(sorted(pm), [F(9,25), F(16,25), F(576,625)])}
        sched = schedule_of(pm)
        build = tree_builder(pm, gm, sched)
        nodes = ['A'] + children
        for u in nodes:
            desc_u = descendants(pm, u)
            for v in nodes:
                if v == u: continue
                n_pairs += 1
                I = influence(build, u, v)
                ok1 &= (I > 0) == (v in desc_u)
check("T1 tree influence theorem: I(u->v) > 0 <=> v is a descendant of u "
      "through nonzero couplings — exhaustive over the 19-tree census; "
      "ancestor/incomparable zeros = no-signalling", ok1, f"{n_pairs} ordered pairs")

# T1b: a g=0 edge blocks; order-independence of I
w0 = DWeb([('A', PREP)])
CS[F(0)] = (F(1), F(0))
def build_g0(iv):
    w = DWeb([('A', PREP)]); w.intervene('A', iv.get('A'))
    w.birth('A', 'B', F(0)); w.intervene('B', iv.get('B'))
    return w
ok1b = influence(build_g0, 'A', 'B') == 0
pm = {'B': 'A', 'C': 'A', 'D': 'B'}
gm = {'B': F(9,25), 'C': F(16,25), 'D': F(576,625)}
for sched in (['B','C','D'], ['C','B','D'], ['B','D','C']):
    build = tree_builder(pm, gm, sched)
    ok1b &= influence(build, 'B', 'D') == influence(tree_builder(pm, gm, ['B','C','D']), 'B', 'D')
    ok1b &= influence(build, 'C', 'D') == 0
check("T1b: a g = 0 edge blocks influence exactly; I is construction-order "
      "independent (gauge inherited from the law)", ok1b)

# T2: the tree no-go — combinatorial AND operational, over the census
ok2 = True
for children in (['B','C'], ['B','C','D']):
    for pm in rooted_trees(children):
        gm = {ch: g for ch, g in zip(sorted(pm), [F(9,25), F(16,25), F(576,625)])}
        build = tree_builder(pm, gm, schedule_of(pm))
        nodes = ['A'] + children
        for x in nodes:
            for y in nodes:
                if x >= y: continue
                if x in descendants(pm, y) or y in descendants(pm, x): continue
                ok2 &= not (descendants(pm, x) & descendants(pm, y))
                for d in nodes:
                    ok2 &= not (influence(build, x, d) > 0 and influence(build, y, d) > 0)
check("T2 tree no-go: incomparable records have DISJOINT descendant sets and "
      "no common operational future — exhaustive over the census", ok2)
print("      T2 contrast [LITERATURE]: any two spacelike Minkowski events share")
print("      a common future (continuum theorem). Finite-sprinkling caveat: a")
print("      bounded window may lack the sampled common future — the finite")
print("      statistical gate is D29's, NOT this theorem. Conclusion: diamond-")
print("      forming cross-branch interaction is NECESSARY; A0a shows it is")
print("      representable after blank activation; representability is not")
print("      locality (A0c) — constraining it is K's job (receipt 2).")

# T3: the minimal operational diamond, all gates
G_AX, G_BX = F(16,25), F(576,625)
EV = ['bA', 'bB', 'bX', 'iBX']
def diamond_build(iv, order=('bA','bB','bX','iBX')):
    w = DWeb([('R', PREP)]); w.intervene('R', iv.get('R'))
    for ev in order:
        if ev == 'bA': w.birth('R', 'A', F(16,25)); w.intervene('A', iv.get('A'))
        if ev == 'bB': w.birth('R', 'B', F(16,25)); w.intervene('B', iv.get('B'))
        if ev == 'bX': w.birth('A', 'X', G_AX);     w.intervene('X', iv.get('X'))
        if ev == 'iBX': w.interact('B', 'X', G_BX)
    return w
ok3 = True
build = lambda iv: diamond_build(iv)
IAB, IBA = influence(build, 'A', 'B'), influence(build, 'B', 'A')
IAX, IBX = influence(build, 'A', 'X'), influence(build, 'B', 'X')
ok3 &= IAB == 0 and IBA == 0 and IAX > 0 and IBX > 0
closure = {'R': {'A','B','X'}, 'A': {'X'}, 'B': {'X'}, 'X': set()}
for u in closure:
    for v in ('R','A','B','X'):
        if v == u: continue
        ok3 &= (influence(build, u, v) > 0) == (v in closure[u])
check("T3a THE DIAMOND: A || B (I = 0 both ways), I(A->X) > 0, I(B->X) > 0; "
      "the full influence matrix equals the declared transitive closure",
      ok3, f"I(A->X) = {IAX}, I(B->X) = {IBX}")

# T3b: sealed-value protection + dispersal ledger through the interaction
wpre = diamond_build({}, order=('bA','bB','bX'))
zA_pre, zB_pre = wpre.zdiag('A'), wpre.zdiag('B')
odB_pre = wpre.r1('B')[2]
wpost = diamond_build({})
ok3b = wpost.zdiag('A') == zA_pre and wpost.zdiag('B') == zB_pre
odB_post = wpost.r1('B')[2]
check("T3b sealed values protected: A's and B's Z-diagonals exactly invariant "
      "through the interaction (nondemolition control); B's coherence ledger "
      "printed (dispersal, not value rewrite)", ok3b,
      f"B offdiag {odB_pre} -> {odB_post}")

# T3c: gauge over all causal-compatible schedules (interactions included);
# states compared LABEL-CANONICALLY (schedules place registers at different
# tensor positions — the D24 label-keyed convention, now on density matrices)
def canon(w):
    n = len(w.regs); dim = 1 << n
    order = sorted(range(n), key=lambda q: w.regs[q])
    def pi(i):
        return sum(((i >> (n-1-q)) & 1) << (n-1-k) for k, q in enumerate(order))
    out = [[F(0)]*dim for _ in range(dim)]
    for i in range(dim):
        for j in range(dim):
            if w.rho[i][j]: out[pi(i)][pi(j)] = w.rho[i][j]
    return tuple(tuple(row) for row in out)
orders = [o for o in permutations(EV)
          if o.index('bA') < o.index('bX') and o.index('bX') < o.index('iBX')
          and o.index('bB') < o.index('iBX')]
laws = {canon(diamond_build({}, order=o)) for o in orders}
ok3c = len(laws) == 1
check("T3c gauge with interactions: all causal-compatible schedules give the "
      "identical label-canonical global state", ok3c, f"{len(orders)} schedules")

# T3d: the synergy gate — A's influence profile on X depends on B's setting
def build_fixedB(beta):
    return lambda iv: diamond_build({**iv, 'B': beta})
IA_b0 = influence(build_fixedB((F(1), F(0))), 'A', 'X')
IA_b1 = influence(build_fixedB((F(0), F(1))), 'A', 'X')
w11 = diamond_build({'A': (F(0), F(1)), 'B': (F(0), F(1))})
pX11 = w11.r1('X')[1]
ok3d = IA_b0 != IA_b1
check("T3d synergy: the A-influence profile on X differs exactly across fixed "
      "B-settings — D carries genuine joint dependence, not two copies", ok3d,
      f"I_A|B=0 = {IA_b0}, I_A|B=1 = {IA_b1}")
print(f"      non-additivity print: P(X=1 | A,B forced to 1) = {pX11} = "
      "sin^2(thA+thB); additive-naive g_AX + g_BX = 16/25 + 576/625 = 976/625 > 1.")

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total}: 8 substantive gates)"
      if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)

#!/usr/bin/env python3
"""
d28b_rs_covariant_kernel_exact.py — v10 D28b part 2: the RS-covariance
theorem. Pin: note-d28b (committed pre-run). Stdlib only; exact rationals.
K_flat (the path-uniform kernel) exists at every finite horizon and is
exactly RS-path-covariant; the residual obstruction is stationarity.
Gates R1-R6; exit 1 on any failure.
"""
from fractions import Fraction as F
from itertools import permutations

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

# ---- the D28 kernels (for R1; conventions of d28_opportunity_kernels) ----
SEED_REGS = ('R', 'A', 'B')
SEED_EDGES = (('R','A'), ('A','B'))
SEED_SEALED = frozenset({'R'})
def d_cover(regs, edges, x, y):
    adj = {r: set() for r in regs}
    for (u, v) in edges: adj[u].add(v); adj[v].add(u)
    front, seen, d = {x}, {x}, 0
    while front:
        if y in front: return d
        front = {w for u in front for w in adj[u]} - seen
        seen |= front; d += 1
    return None
def options(regs, edges, sealed, kernel):
    uns = [r for r in regs if r not in sealed]
    opts = [(('none',), F(1))]
    for y in uns: opts.append((('birth', y), F(1)))
    for y in uns:
        for x in uns:
            if x == y: continue
            d = d_cover(regs, edges, y, x)
            if d is not None and d <= 1: opts.append((('interact', y, x), F(1)))
            elif kernel[0] == 'tail' and d is not None:
                opts.append((('interact', y, x), kernel[1] * F(1,2)**d))
    Z = sum(w for _, w in opts)
    return [(op, w/Z) for op, w in opts]
def apply_op(regs, edges, op, counter):
    if op[0] == 'none': return regs, edges
    if op[0] == 'birth':
        child = f"z{counter}"
        return regs + (child,), edges + ((op[1], child),)
    return regs, edges + ((op[1], op[2]),)

print("[d28b RS-covariant kernel — exact]")

# R1: the functional equation + the D28 kernels' violation (N11 re-gated)
print("      the path-covariance functional equation, for independent op")
print("      pairs: w(o1|H) w(o2|H+o1) = w(o2|H) w(o1|H+o2).")
def path_prob(kernel, ops_seq):
    regs, edges, p, counter = SEED_REGS, SEED_EDGES, F(1), 1
    for op in ops_seq:
        w = dict(options(regs, edges, SEED_SEALED, kernel)).get(op)
        if w is None: return F(0)
        p *= w
        regs, edges = apply_op(regs, edges, op, counter)
        if op[0] == 'birth': counter += 1
    return p
ok1 = (path_prob(('collar',), [('birth','A'), ('interact','A','B')]) == F(1,40)
   and path_prob(('collar',), [('interact','A','B'), ('birth','A')]) == F(1,25)
   and path_prob(('tail', F(1,5)), [('birth','A'), ('interact','A','B')]) == F(2,81)
   and path_prob(('tail', F(1,5)), [('interact','A','B'), ('birth','A')]) == F(1,25))
check("R1 the D28 kernels violate path-covariance (N11 re-gated: collar "
      "1/40 vs 1/25; tail 2/81 vs 1/25)", ok1)

# ---- K_flat: the path-uniform kernel on the none-free full grammar ----
FRESH = ('z1', 'z2', 'z3')
def grammar(regs, sealed):
    uns = [r for r in regs if r not in sealed]
    ops = [('b', y) for y in uns]
    ops += [('i', x, y) for x in uns for y in uns if x != y]
    return ops
def g_apply(regs, edges, op):
    if op[0] == 'b':
        child = FRESH[sum(1 for r in regs if r in FRESH)]
        return regs + (child,), edges + (('b', op[1], child),)
    return regs, edges + (('i', op[1], op[2]),)
def canon(regs, edges):
    """Canonical form up to fresh-label ISOMORPHISM (arc-delta upgrade:
    present fresh labels are mapped onto the canonical prefix z1..zk, so
    name choice — not just assignment — is normalized; behavior on the
    enumerated domain is unchanged, since the kernel assigns prefix names)."""
    fresh = [r for r in regs if r in FRESH]
    targets = FRESH[:len(fresh)]
    best = None
    for perm in permutations(targets):
        m = dict(zip(fresh, perm))
        e2 = tuple(sorted((t, m.get(a, a), m.get(b, b)) for (t, a, b) in edges))
        r2 = tuple(sorted(m.get(r, r) for r in regs))
        key = (r2, e2)
        if best is None or key < best: best = key
    return best

def phi_tables(T):
    """Backward recursion: Phi_t on canonical webs at each depth, horizon T."""
    # forward-enumerate reachable canonical webs per depth (with a concrete
    # representative), then recurse backward
    reps = [dict() for _ in range(T+1)]
    seed_edges = (('b','R','A'), ('b','A','B'))
    reps[0] = {canon(SEED_REGS, seed_edges): (SEED_REGS, seed_edges)}
    for t in range(T):
        for key, (regs, edges) in list(reps[t].items()):
            for op in grammar(regs, SEED_SEALED):
                r2, e2 = g_apply(regs, edges, op)
                reps[t+1].setdefault(canon(r2, e2), (r2, e2))
    phi = [dict() for _ in range(T+1)]
    for key in reps[T]: phi[T][key] = F(1)
    for t in range(T-1, -1, -1):
        for key, (regs, edges) in reps[t].items():
            tot = F(0)
            for op in grammar(regs, SEED_SEALED):
                r2, e2 = g_apply(regs, edges, op)
                tot += phi[t+1][canon(r2, e2)]
            phi[t][key] = tot
    return reps, phi

def kflat_weight(regs, edges, op, t, phi):
    r2, e2 = g_apply(regs, edges, op)
    return phi[t+1][canon(r2, e2)] / phi[t][canon(regs, edges)]

T2 = 2
reps2, phi2 = phi_tables(T2)
SEED_TE = (('b','R','A'), ('b','A','B'))

# R2: exact normalization at every reachable node
ok2 = True
for t in range(T2):
    for key, (regs, edges) in reps2[t].items():
        tot = sum(kflat_weight(regs, edges, op, t, phi2)
                  for op in grammar(regs, SEED_SEALED))
        ok2 &= (tot == 1)
check("R2 K_flat normalization: weights sum to 1 exactly at every reachable "
      "history node (horizon T = 2)", ok2,
      f"Phi(seed) = {phi2[0][canon(SEED_REGS, SEED_TE)]}")

# R3: PATH-COVARIANCE, exhaustive — all paths to each final web, equal products
paths_per_web = {}
def walk2(regs, edges, t, p):
    if t == T2:
        key = canon(regs, edges)
        paths_per_web.setdefault(key, []).append(p)
        return
    for op in grammar(regs, SEED_SEALED):
        w = kflat_weight(regs, edges, op, t, phi2)
        r2, e2 = g_apply(regs, edges, op)
        walk2(r2, e2, t+1, p*w)
walk2(SEED_REGS, SEED_TE, 0, F(1))
n_multi = sum(1 for v in paths_per_web.values() if len(v) > 1)
ok3 = all(len(set(v)) == 1 for v in paths_per_web.values()) and n_multi > 0
tot_mass = sum(sum(v) for v in paths_per_web.values())
ok3 &= tot_mass == 1
check("R3 PATH-COVARIANCE, exhaustive: every accretion path to the same "
      "canonical final web carries the IDENTICAL product; total mass 1",
      ok3, f"{len(paths_per_web)} final webs, {n_multi} genuinely multi-path")

# R4: the battery on K_flat (arc-round M5 upgrade: the fixed-horizon
# marginalization gate + two genuine relabeling classes)
ok4 = True
for key, (regs, edges) in reps2[0].items():
    for op in grammar(regs, SEED_SEALED):
        ok4 &= ('R' not in op[1:])                      # sealed protection
        ok4 &= kflat_weight(regs, edges, op, 0, phi2) > 0   # nonzero
# fixed-horizon cylinder gate: the step-1 marginal of the depth-2 law
# equals the step-1 weights AT THE SAME HORIZON (cross-horizon fails — R5)
marg = {}
for op in grammar(SEED_REGS, SEED_SEALED):
    w1 = kflat_weight(SEED_REGS, SEED_TE, op, 0, phi2)
    r2, e2 = g_apply(SEED_REGS, SEED_TE, op)
    tot2 = sum(kflat_weight(r2, e2, op2, 1, phi2)
               for op2 in grammar(r2, SEED_SEALED))
    marg[op] = w1 * tot2
    ok4 &= (marg[op] == w1)
# relabeling class 1: two accretion orders birthing from A and B assign
# fresh labels oppositely; canon merges them and Phi agrees
rA1, eA1 = g_apply(SEED_REGS, SEED_TE, ('b', 'A'))
rAB1, eAB1 = g_apply(rA1, eA1, ('b', 'B'))     # z1 from A, z2 from B
rB2, eB2 = g_apply(SEED_REGS, SEED_TE, ('b', 'B'))
rBA2, eBA2 = g_apply(rB2, eB2, ('b', 'A'))     # z1 from B, z2 from A
ok4 &= canon(rAB1, eAB1) == canon(rBA2, eBA2)
# relabeling class 2: a single fresh label renamed EXPLICITLY (arc-delta
# fix: the earlier presence check was tautological) — the z2-named copy of
# the z1-web must canon-merge with it
ok4 &= canon(('R','A','B','z2'), SEED_TE + (('b','A','z2'),)) == canon(rA1, eA1)
check("R4 the battery (arc-round upgrade): sealed protection, positive "
      "weights, the FIXED-HORIZON cylinder gate (step-1 marginal of the "
      "depth-2 law == the step-1 weights; the cross-horizon failure is "
      "R5's content, not a cylinder defect), and TWO relabeling classes "
      "(opposite fresh-label assignments canon-merge with equal Phi; "
      "single-label rename); preparation-independence structural", ok4)

# R5: the STATIONARITY obstruction — horizon-dependence of the weights
T3 = 3
reps3, phi3 = phi_tables(T3)
w2 = {op: kflat_weight(SEED_REGS, SEED_TE, op, 0, phi2)
      for op in grammar(SEED_REGS, SEED_SEALED)}
w3 = {op: kflat_weight(SEED_REGS, SEED_TE, op, 0, phi3)
      for op in grammar(SEED_REGS, SEED_SEALED)}
ok5 = any(w2[op] != w3[op] for op in w2)
check("R5 the stationarity obstruction: K_flat's step-1 weights at horizon "
      "T = 2 differ from horizon T = 3 — path-covariant, NOT stationary; "
      "the sharpened F12 choice is on the record", ok5,
      f"w(birth A): {w2[('b','A')]} at T=2 vs {w3[('b','A')]} at T=3")
print("      R5 the sharpened kernel-selector (F12) statement: the selector")
print("      must choose within {stationary + covariance-violating (the D28")
print("      collar/tail class), path-covariant + horizon-dependent (the")
print("      K_flat class), or a stationary-and-covariant kernel — whose")
print("      existence for this grammar is the remaining open question, the")
print("      functional equation printed at R1}.")

# R6: honesty — the none-free scope
print("      R6 scope: K_flat is NONE-FREE by construction; a none step")
print("      changes path length, so path-covariance across accretion orders")
print("      is posed on the none-free skeleton (one more reason the D28")
print("      kernels, which carry the none arm, fail it). Flags-observable")
print("      reading: with the full flag sequence recorded, path-covariance")
print("      = the demand that bookkeeping order carry no probability — the")
print("      cg-line's construction-order gauge promoted to the stochastic")
print("      kernel; K_flat satisfies it, the D28 kernels do not.")
check("R6 scope prints emitted", True)

print()
total = PASS + FAIL
print(f"ALL CHECKS PASS ({PASS}/{total}: 5 substantive gates + 1 print gate)"
      if FAIL == 0 else f"FAILURES: {FAIL}/{total}")
if FAIL: raise SystemExit(1)

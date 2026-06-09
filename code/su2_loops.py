#!/usr/bin/env python3
"""
SU(2) Wilson-loop PATH representation + the non-abelian Makeenko-Migdal loop equation
(paper 42, Target I, module 2 -- M3).

The abelian engine (mm_equations.abelian_loop_equation) works on winding CHAINS
{(site,mu): winding}, which suffice for U(1) (no splitting). The SU(2) loop equation has
a FIERZ SPLITTING term at every repeated traversal of the differentiated link -- and which
sub-loops result depends on the loop's PATH ORDERING, which the chain forgets. So loops are
here ordered closed WALKS; W-values and deformations still reduce to chains (W depends only
on windings), and only the split needs the walk.

Conventions (validated, see scratch_su2_check.py): weight prod_p exp[(beta/N) Re tr U_p],
N=2, W(C)=(1/N) tr(holonomy). Multiplying the loop equation by 4N to clear fractions, the
generator returns INTEGER + beta-linear coefficients:

  contact     :  2(N^2-1) W(C)                      [ = 6 W(C) for SU(2) ]
  deformation :  beta * sum_{p contains l0} s_p [ W(C+dp) - W(C-dp) ]
  split (FF)  :  per other FORWARD occurrence j of l0:
                   + 2 N^2 <W(C1) W(C2)>  - 2 W(C)  [ = 8<W C1 W C2> - 2 W(C) ]

C1, C2 = the two arcs of the walk between the two l0 traversals.

Equation format (extends the abelian {key:(a,b)}):  (linear, bilinear)
  linear   = { chain_key            : (a, b) }   coeff a + b*beta, observable W(key)
  bilinear = { (key1, key2) [sorted]: (a, b) }   coeff a + b*beta, observable <W(k1) W(k2)>
The empty chain_key = identity, W = 1.
"""
from loops import (e, add, sub, plaq_boundary, plaquettes_with_link, chain_add,
                   canonical_full as canon, _signed_perms, _apply_g, _translate, _PERMS)

N = 2


def canonical_pair(c1, c2, d):
    """Canonical key for the UNORDERED two-loop observable <W(c1) W(c2)>, invariant under:
    the hypercubic point group + a SHARED translation (relative position preserved),
    independent orientation reversal of each loop (W(C)=W(-C)), and swap c1<->c2.
    (Per-loop canonicalization is WRONG here -- it forgets the relative position the
    correlator depends on.)"""
    if d not in _PERMS:
        _PERMS[d] = list(_signed_perms(d))
    if not c1 and not c2:
        return (frozenset(), frozenset())
    best = None
    for g in _PERMS[d]:
        g1, g2 = _apply_g(c1, g, d), _apply_g(c2, g, d)
        for r1 in (g1, {k: -v for k, v in g1.items()}):
            for r2 in (g2, {k: -v for k, v in g2.items()}):
                for (a, b) in ((r1, r2), (r2, r1)):       # unordered
                    sites = [s for (s, _) in a] + [s for (s, _) in b]
                    if not sites:
                        continue
                    shift = min(sites)                    # SHARED translation
                    fa = frozenset(_translate(a, shift).items())
                    fb = frozenset(_translate(b, shift).items())
                    key = (sorted(fa), sorted(fb))
                    if best is None or key < best[0]:
                        best = (key, (fa, fb))
    return best[1]
CONTACT = 2 * (N * N - 1)     # 6
SPLIT = 2 * N * N             # 8


# ---- directed-step walk utilities ----
# step = (site, mu, s): the link L(site,mu) [site = lower endpoint], traversed s=+1 (site->site+e_mu)
# or s=-1 (site+e_mu->site).
def step_start(step):
    site, mu, s = step
    return site if s == +1 else add(site, e(mu, len(site)))


def step_end(step):
    site, mu, s = step
    return add(site, e(mu, len(site))) if s == +1 else site


def walk_link(step):
    """The undirected link variable (site, mu) underlying a step."""
    return (step[0], step[1])


def is_closed_walk(w):
    if not w:
        return True
    return all(step_end(w[i]) == step_start(w[(i + 1) % len(w)]) for i in range(len(w)))


def walk_to_chain(w):
    c = {}
    for (site, mu, s) in w:
        c[(site, mu)] = c.get((site, mu), 0) + s
    return {k: v for k, v in c.items() if v != 0}


def reverse_walk(w):
    return [(site, mu, -s) for (site, mu, s) in reversed(w)]


def reduce_walk(w):
    """Remove adjacent backtracking pairs (U_l U_l^{-1} = 1), cyclically, until none remain.
    Loop-word reduction: chain-invariant, leaves the Wilson-loop observable unchanged.
    A fully backtracking walk reduces to [] (the identity, W=1)."""
    w = list(w)
    changed = True
    while changed and w:
        changed = False
        n = len(w)
        for i in range(n):
            a, b = w[i], w[(i + 1) % n]
            if (a[0], a[1]) == (b[0], b[1]) and a[2] == -b[2]:      # inverses
                j = (i + 1) % n
                w = [w[k] for k in range(n) if k != i and k != j]
                changed = True
                break
    return w


def has_backward_partner(walk, link):
    """True if `link`=(site,mu) is traversed BACKWARD somewhere in walk (a forward-backward
    self-intersection). The forward-anchored equation here covers contact+deformation+FF
    splits only; an FB partner needs the (unimplemented) FB split, so such anchors are skipped."""
    return any((st[0], st[1]) == link and st[2] == -1 for st in walk)


def plaquette_walk(x, mu, nu, d):
    """The 4-step boundary walk of P(x;mu,nu): x ->mu-> ->nu-> <-mu<- <-nu<- x."""
    emu, enu = e(mu, d), e(nu, d)
    return [(x, mu, +1),
            (add(x, emu), nu, +1),
            (add(x, enu), mu, -1),
            (x, nu, -1)]


# ---- the SU(2) loop equation ----
def su2_loop_equation(walk, anchor, d):
    """Schwinger-Dyson / Makeenko-Migdal equation for SU(2), anchored at walk[anchor]
    (must traverse its link FORWARD, s=+1). Returns (linear, bilinear)."""
    assert is_closed_walk(walk), "walk must be closed"
    site, mu, s = walk[anchor]
    assert s == +1, "anchor must be a forward step (s=+1)"
    x = site
    C = walk_to_chain(walk)
    lin, bil = {}, {}

    def accL(chain, a, b):
        k = canon(chain, d)
        ca, cb = lin.get(k, (0, 0))
        lin[k] = (ca + a, cb + b)

    def accB(c1, c2, a, b):
        key = canonical_pair(c1, c2, d)                # JOINT canon (relative position kept)
        ca, cb = bil.get(key, (0, 0))
        bil[key] = (ca + a, cb + b)

    # contact (anchor occurrence, Casimir)
    accL(C, CONTACT, 0)

    # deformation (action's plaquettes at l0=(x,mu)); W depends on chain only
    for (P, sp) in plaquettes_with_link(x, mu, d):
        base, a, b = P
        dp = plaq_boundary(base, a, b, d)
        accL(chain_add(C, dp, +1), 0, +sp)
        accL(chain_add(C, dp, -1), 0, -sp)

    # split: every OTHER traversal of the same link variable (x,mu)
    n = len(walk)
    for j in range(n):
        if j == anchor:
            continue
        if walk_link(walk[j]) != (x, mu):
            continue
        sj = walk[j][2]
        if sj == +1:                                   # forward-forward split
            arc1 = [walk[(anchor + t) % n] for t in range((j - anchor) % n)]
            arc2 = [walk[(j + t) % n] for t in range((anchor - j) % n)]
            accB(walk_to_chain(arc1), walk_to_chain(arc2), SPLIT, 0)
            accL(C, -2, 0)
        # forward-backward (sj=-1) splits exist too; not emitted here (documented).

    lin = {k: (a, b) for k, (a, b) in lin.items() if not (a == 0 and b == 0)}
    bil = {k: (a, b) for k, (a, b) in bil.items() if not (a == 0 and b == 0)}
    return lin, bil


# ---- walk-space machinery for CLOSURE (M3 step 1): emit deformations + splits as WALKS,
#      so the system can be closed (the chain forgets self-intersection structure) ----
def _apply_g_step(step, g, d):
    perm, signs = g
    P, Q = step_start(step), step_end(step)

    def M(z):
        ns = [0] * d
        for i in range(d):
            ns[perm[i]] = signs[i] * z[i]
        return tuple(ns)

    gP, gQ = M(P), M(Q)
    pm, sp = perm[step[1]], step[2] * signs[step[1]]
    return (gP if sp == 1 else gQ, pm, sp)


def canonical_walk(walk, d):
    """Canonical key for a single-loop OBSERVABLE: invariant under cyclic rotation, orientation
    reversal, translation, and the hypercubic point group. Distinguishes walks with the same
    winding chain but different self-intersection structure (different holonomies)."""
    if not walk:
        return ()
    if d not in _PERMS:
        _PERMS[d] = list(_signed_perms(d))
    best = None
    for w0 in (walk, reverse_walk(walk)):
        for g in _PERMS[d]:
            gw = [_apply_g_step(st, g, d) for st in w0]
            shift = min([step_start(st) for st in gw] + [step_end(st) for st in gw])
            gw = [(sub(st[0], shift), st[1], st[2]) for st in gw]
            n = len(gw)
            for r in range(n):
                rot = tuple(gw[r:] + gw[:r])
                if best is None or rot < best:
                    best = rot
    return best


def _min_rotation(steps):
    t = tuple(steps)
    n = len(t)
    return min(t[r:] + t[:r] for r in range(n)) if n else ()


def canonical_walk_pair(w1, w2, d):
    """Canonical key for the two-loop OBSERVABLE <W(w1) W(w2)>: same point-group g + SHARED
    translation applied to both (relative position kept), each walk independently cyclic-
    rotated and reversal-folded, and the pair unordered. Keyed by WALK (holonomy), not chain."""
    if d not in _PERMS:
        _PERMS[d] = list(_signed_perms(d))
    best = None
    for (a0, b0) in ((w1, w2), (w2, w1)):
        for ra in (a0, reverse_walk(a0)):
            for rb in (b0, reverse_walk(b0)):
                for g in _PERMS[d]:
                    ga = [_apply_g_step(st, g, d) for st in ra]
                    gb = [_apply_g_step(st, g, d) for st in rb]
                    pts = ([step_start(s) for s in ga] + [step_end(s) for s in ga] +
                           [step_start(s) for s in gb] + [step_end(s) for s in gb])
                    if not pts:
                        return ((), ())
                    sh = min(pts)
                    ka = _min_rotation([(sub(s[0], sh), s[1], s[2]) for s in ga])
                    kb = _min_rotation([(sub(s[0], sh), s[1], s[2]) for s in gb])
                    key = (ka, kb)
                    if best is None or key < best:
                        best = key
    return best


def skey(walk, d):
    """Single-loop observable key: reduce backtracks, then canonical walk (holonomy-faithful)."""
    return canonical_walk(reduce_walk(walk), d)


def pkey(w1, w2, d):
    """Two-loop observable key (joint, position-aware)."""
    return canonical_walk_pair(reduce_walk(w1), reduce_walk(w2), d)


def plaq_walks_through(x, mu, d):
    """Plaquette boundary walks containing link (x,mu), each ROTATED to start with (x,mu,+1)."""
    out = []
    for (P, s) in plaquettes_with_link(x, mu, d):
        base, a, b = P
        pw = plaquette_walk(base, a, b, d)
        idx = next(i for i, st in enumerate(pw) if (st[0], st[1]) == (x, mu))
        if pw[idx][2] == -1:                        # ensure forward traversal of l0
            pw = reverse_walk(pw)
            idx = next(i for i, st in enumerate(pw) if (st[0], st[1]) == (x, mu))
        out.append(pw[idx:] + pw[:idx])
    return out


def su2_eq_walks(walk, anchor, d):
    """SU(2) loop equation emitting WALKS (not chains): for closure. Returns
    (lin, bil): lin = [(walk, a, b)], bil = [((w1,w2), a, b)], coeff a+b*beta, sum = 0."""
    assert walk[anchor][2] == +1, "anchor must be forward"
    x, mu = walk[anchor][0], walk[anchor][1]
    lin = [(walk, CONTACT, 0)]                       # contact (Casimir)
    for pw in plaq_walks_through(x, mu, d):          # deformation: insert plaquette walk
        D = walk[:anchor] + pw + [pw[0]] + walk[anchor + 1:]          # "double": C + dp
        S = walk[:anchor] + reverse_walk(pw[1:]) + walk[anchor + 1:]   # "smooth": C - dp
        lin.append((D, 0, +1))
        lin.append((S, 0, -1))
    bil = []
    n = len(walk)
    for j in range(n):                               # Fierz split at every OTHER traversal of l0
        if j == anchor or (walk[j][0], walk[j][1]) != (x, mu):
            continue
        if walk[j][2] == +1:                         # forward-forward: arcs INCLUDE the two l0's
            arc1 = [walk[(anchor + t) % n] for t in range((j - anchor) % n)]
            arc2 = [walk[(j + t) % n] for t in range((anchor - j) % n)]
            bil.append(((arc1, arc2), +SPLIT, 0))
            lin.append((walk, -2, 0))
        else:                                        # forward-backward: arcs EXCLUDE the two l0's
            A = reduce_walk([walk[(anchor + 1 + t) % n] for t in range((j - anchor - 1) % n)])
            B = reduce_walk([walk[(j + 1 + t) % n] for t in range((anchor - j - 1) % n)])
            if not A and not B:                      # <W(e)W(e)> = 1
                lin.append(([], -SPLIT, 0))
            elif not A:                              # <W(e)W(B)> = <W(B)>
                lin.append((B, -SPLIT, 0))
            elif not B:
                lin.append((A, -SPLIT, 0))
            else:
                bil.append(((A, B), -SPLIT, 0))
            lin.append((walk, +2, 0))
    return lin, bil

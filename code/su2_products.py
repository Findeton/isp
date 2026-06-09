#!/usr/bin/env python3
"""
Product (2-loop) Schwinger-Dyson equation + 3-loop joint canonicalization (paper 42, M3 step 1
of §18.12). Differentiating <W(C) W(C')> w.r.t. a link of C gives the single-loop operator for C
TIMES the spectator W(C'):

  0 = <[contact+deformation+split of C] * W(C')>
    = sum (single-eq coeff) <W(X) W(C')>   +   sum (split coeff) <W(C_1) W(C_2) W(C')>,

a valid SD identity (NOT the single-loop eq times a constant -- it is the L^a-of-a-product
identity). It RELATES two- and THREE-loop correlators, so it constrains the 3-loop variables the
localizing blocks introduce. First pass: C' must NOT traverse the anchor link (else a cross/merge
term appears); that subset already generates the 3-loop structure. Validated by MC like FF/FB.
"""
from su2_loops import (su2_eq_walks, reverse_walk, reduce_walk, _apply_g_step, _min_rotation,
                       step_start, step_end, _signed_perms, _PERMS)
from loops import sub
from itertools import permutations, product as iproduct


def product_eq_walks(C, anchor, Cp, d):
    """SD equation for <W(C) W(Cp)>, anchored at C[anchor] (forward), Cp not sharing that link.
    Returns (bil, tri): bil = [((X,Cp), a, b)] (2-loop), tri = [((X,Y,Cp), a, b)] (3-loop)."""
    x, mu = C[anchor][0], C[anchor][1]
    if any((st[0], st[1]) == (x, mu) for st in Cp):
        return None                                      # Cp shares the link -> cross term (TODO)
    lin, bil = su2_eq_walks(C, anchor, d)
    bil_out = [((X, Cp), a, b) for (X, a, b) in lin]
    tri_out = [((X, Y, Cp), a, b) for ((X, Y), a, b) in bil]
    return bil_out, tri_out


def canonical_walk_triple(w1, w2, w3, d):
    """Canonical key for <W(w1)W(w2)W(w3)>: same point-group g + SHARED translation on all three,
    each walk independently cyclic-rotated and reversal-folded, unordered over the three."""
    if d not in _PERMS:
        _PERMS[d] = list(_signed_perms(d))
    best = None
    for perm in permutations((w1, w2, w3)):
        for revs in iproduct((False, True), repeat=3):
            rs = [reverse_walk(w) if r else w for w, r in zip(perm, revs)]
            for g in _PERMS[d]:
                gs = [[_apply_g_step(st, g, d) for st in w] for w in rs]
                pts = [p for gw in gs for s in gw for p in (step_start(s), step_end(s))]
                if not pts:
                    return ((), (), ())
                sh = min(pts)
                ks = tuple(_min_rotation([(sub(s[0], sh), s[1], s[2]) for s in gw]) for gw in gs)
                if best is None or ks < best:
                    best = ks
    return best


def tkey(w1, w2, w3, d):
    return canonical_walk_triple(reduce_walk(w1), reduce_walk(w2), reduce_walk(w3), d)

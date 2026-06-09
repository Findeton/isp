#!/usr/bin/env python3
"""
Lattice geometry + Wilson-loop (1-chain cycle) representation, for the U(1)/SU(2)
loop-equation bootstrap (paper 42, Target I, module 1).

A site is a d-tuple of ints. A link L(x,mu) runs x -> x+e_mu. A 1-chain is a dict
{(site,mu): winding}; a Wilson-loop observable W(C) corresponds to a *closed* 1-chain
(cycle) C, identified modulo lattice translation and orientation reversal (W(C)=W(-C)).
A plaquette P(x;mu,nu), mu<nu, has oriented boundary (mu, nu, -mu, -nu).

Includes an exact 2D filling rule (winding number per plaquette) used to VALIDATE the
loop equations: in 2D U(1), W(C) = prod_p I_{w_p}(beta)/I_0(beta), w_p the winding of C.
"""
from itertools import combinations


def e(mu, d):
    v = [0] * d; v[mu] = 1; return tuple(v)

def add(x, v): return tuple(a + b for a, b in zip(x, v))
def sub(x, v): return tuple(a - b for a, b in zip(x, v))


def plaq_boundary(x, mu, nu, d):
    """Oriented boundary 1-chain of P(x;mu,nu) [mu<nu], as {(site,dir): winding}."""
    emu, enu = e(mu, d), e(nu, d)
    c = {}
    def al(site, dirn, w): c[(site, dirn)] = c.get((site, dirn), 0) + w
    al(x, mu, +1)              # x        -> x+mu
    al(add(x, emu), nu, +1)    # x+mu     -> x+mu+nu
    al(add(x, enu), mu, -1)    # x+mu+nu  -> x+nu      (link (x+nu,mu) reversed)
    al(x, nu, -1)              # x+nu     -> x
    return {k: v for k, v in c.items() if v != 0}


def chain_add(c1, c2, sign=1):
    out = dict(c1)
    for k, v in c2.items():
        out[k] = out.get(k, 0) + sign * v
        if out[k] == 0: del out[k]
    return out


def boundary(chain, d):
    """d(1-chain): {site: net}. A link winding w on L(x,mu) gives +w at head x+e_mu, -w at tail x."""
    bd = {}
    for (site, mu), w in chain.items():
        h, t = add(site, e(mu, d)), site
        bd[h] = bd.get(h, 0) + w
        bd[t] = bd.get(t, 0) - w
    return {s: v for s, v in bd.items() if v != 0}


def is_closed(chain, d):
    return len(boundary(chain, d)) == 0


def _translate(chain, shift):
    return {(sub(site, shift), mu): w for (site, mu), w in chain.items()}


def canonical(chain, d):
    """Canonical key mod translation AND orientation reversal (W(C)=W(-C))."""
    if not chain:
        return frozenset()
    def canon_translate(c):
        base = min(site for (site, mu) in c)             # min tail-site
        return frozenset(_translate(c, base).items())
    neg = {k: -v for k, v in chain.items()}
    return min(canon_translate(chain), canon_translate(neg), key=lambda fs: sorted(fs))


# ---- full lattice point-group canonicalization (hyperoctahedral group + translation + reversal) ----
def _signed_perms(d):
    from itertools import permutations, product
    for perm in permutations(range(d)):
        for signs in product((1, -1), repeat=d):
            yield perm, signs


def _apply_g(chain, g, d):
    """Apply signed permutation g=(perm,signs): M e_mu = signs[mu] e_{perm[mu]}."""
    perm, signs = g
    def Ms(x):
        ns = [0] * d
        for mu in range(d): ns[perm[mu]] = signs[mu] * x[mu]
        return tuple(ns)
    out = {}
    for (site, mu), w in chain.items():
        Mx, pm, s = Ms(site), perm[mu], signs[mu]
        if s == 1:
            k, ww = (Mx, pm), w
        else:                                            # axis flipped: link reversed
            k, ww = (sub(Mx, e(pm, d)), pm), -w
        out[k] = out.get(k, 0) + ww
    return {k: v for k, v in out.items() if v != 0}


_PERMS = {}
def canonical_full(chain, d):
    """Canonical key mod the FULL lattice symmetry: point group + translation + orientation reversal.
    Valid because <W(C)> is invariant under the hypercubic point group and W(C)=W(-C)."""
    if not chain:
        return frozenset()
    if d not in _PERMS:
        _PERMS[d] = list(_signed_perms(d))
    best = None
    for g in _PERMS[d]:
        gc = _apply_g(chain, g, d)
        for c in (gc, {k: -v for k, v in gc.items()}):
            base = min(site for (site, mu) in c)
            fs = frozenset(_translate(c, base).items())
            key = sorted(fs)
            if best is None or key < best[0]:
                best = (key, fs)
    return best[1]


def plaquettes_with_link(x, mu, d):
    """All plaquettes containing L(x,mu); yields (P=(site,a,b), s) with s=coeff of L(x,mu) in dP."""
    out = []
    for nu in range(d):
        if nu == mu: continue
        a, b = sorted((mu, nu))
        for base in (x, sub(x, e(nu, d))):               # two plaquettes share the mu-edge
            db = plaq_boundary(base, a, b, d)
            s = db.get((x, mu), 0)
            if s != 0:
                out.append(((base, a, b), s))
    return out


# ---- exact 2D U(1) solution, for validation ----
def fill_winding_2d(chain):
    """2D only: winding number w_p of cycle C around each plaquette (lower-left corner)."""
    assert all(mu in (0, 1) for (_, mu) in chain), "2D only"
    # D[P at (i,j)] = sum_{j'<=j} C[ horizontal link L((i,j'),0) ]
    cols = {}
    for (site, mu), w in chain.items():
        if mu == 0:
            cols.setdefault(site[0], []).append((site[1], w))
    wind = {}
    for i, lst in cols.items():
        lst.sort()
        # cumulative sum from below; assign D to plaquette rows
        jmin = lst[0][0]; jmax = lst[-1][0]
        acc = 0
        contrib = {j: 0 for j, _ in lst}
        for j, w in lst: contrib[j] += w
        for j in range(jmin, jmax + 1):
            acc += contrib.get(j, 0)
            if acc != 0:
                wind[(i, j)] = wind.get((i, j), 0) + acc
    return wind


def exact_W_2d(chain, beta):
    """Exact 2D U(1) Wilson loop:  W(C) = prod_p I_{w_p}(beta)/I_0(beta)."""
    from scipy.special import iv
    w = fill_winding_2d(chain)
    val = 1.0
    I0 = iv(0, beta)
    for p, wp in w.items():
        val *= iv(abs(wp), beta) / I0
    return float(val)

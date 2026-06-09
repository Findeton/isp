#!/usr/bin/env python3
"""
Monte-Carlo validation of the SU(2) loop-equation generators (M3), against the actual theory:
  - single-loop equation: contact + deformation + FF + FB splits  (su2_eq_walks)
  - product (2-loop) equation: <single-eq operator * W(C')> = 0, generating 3-loop correlators
    (su2_products.product_eq_walks)
The Schwinger-Dyson identity sum coeff*<...> = 0 must hold for ensemble averages up to MC error;
the simple-loop residual is the noise floor.
"""
from su2_loops import su2_eq_walks, plaquette_walk, reverse_walk
from su2_products import product_eq_walks
from su2_mc import measure

d = 2


def lollipop_1plaq():
    A = [((1, 0), 0, +1), ((2, 0), 1, +1), ((1, 1), 0, -1), ((1, 0), 1, -1)]
    return [((0, 0), 0, +1)] + A + [((0, 0), 0, -1)]


def lollipop_2plaq():
    A = [((1, 0), 0, +1), ((2, 0), 1, +1), ((1, 1), 0, -1), ((1, 0), 1, -1)]
    B = [((0, 0), 1, +1), ((-1, 1), 0, -1), ((-1, 0), 1, -1), ((-1, 0), 0, +1)]
    return [((0, 0), 0, +1)] + A + [((0, 0), 0, -1)] + B


def collect(terms_lin, terms_bil, terms_tri):
    """Return products list + index map for a set of lin/bil/tri terms."""
    prods, idx = [], {}
    def add(*walks):
        key = tuple(tuple(w) for w in walks)
        if key not in idx:
            idx[key] = len(prods); prods.append([list(w) for w in walks])
        return idx[key]
    for (w, _, _) in terms_lin:
        add(w)
    for ((w1, w2), _, _) in terms_bil:
        add(w1, w2)
    for ((w1, w2, w3), _, _) in terms_tri:
        add(w1, w2, w3)
    return prods, idx


def resid(lin, bil, tri, vals, idx, beta):
    r = 0.0
    for (w, a, b) in lin:
        r += (a + b * beta) * vals[idx[(tuple(w),)]]
    for ((w1, w2), a, b) in bil:
        r += (a + b * beta) * vals[idx[(tuple(w1), tuple(w2))]]
    for ((w1, w2, w3), a, b) in tri:
        r += (a + b * beta) * vals[idx[(tuple(w1), tuple(w2), tuple(w3))]]
    return r


if __name__ == "__main__":
    P = plaquette_walk((0, 0), 0, 1, d)
    Cp = plaquette_walk((3, 3), 0, 1, d)            # spectator, shares no link with loops at origin

    # single-loop equation cases (lin, bil, tri=[])
    single = {
        "simple 1x1 (baseline)": su2_eq_walks(P, 0, d) + ([],),
        "doubled 1x1 (FF)": su2_eq_walks(P + P, 0, d) + ([],),
        "lollipop x1 (FB, B empty)": su2_eq_walks(lollipop_1plaq(), 0, d) + ([],),
        "lollipop x2 (FB, disjoint)": su2_eq_walks(lollipop_2plaq(), 0, d) + ([],),
    }
    # product equation: single-eq(C) * W(Cp); generates 3-loop correlators from C's splits
    bilp, trip = product_eq_walks(P + P, 0, Cp, d)        # doubled-1x1 (FF) * W(Cp)
    products_case = {"product: doubled-1x1 * W(Cp) (2- and 3-loop)": ([], bilp, trip)}

    allcases = {**{k: (l, b, t) for k, (l, b, t) in single.items()}, **products_case}

    # one big products list across all cases
    prods, idx = [], {}
    def merge(lin, bil, tri):
        global prods, idx
        p2, i2 = collect(lin, bil, tri)
        for key in i2:
            if key not in idx:
                idx[key] = len(prods); prods.append([list(w) for w in key])
    for (l, b, t) in allcases.values():
        merge(l, b, t)

    for beta in (1.0, 2.0):
        vals, n = measure(6, beta, prods, therm=2000, nmeas=24000, gap=3, eps=0.45)
        print(f"\nbeta={beta}  (L=6, {n} measurements)")
        for name, (l, b, t) in allcases.items():
            print(f"  residual = {resid(l, b, t, vals, idx, beta):+.4f}   {name}")
    print("\n(simple-1x1 = MC noise floor; FF, FB, and the product (3-loop) eq at that scale => validated.)")

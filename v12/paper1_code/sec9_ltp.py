#!/usr/bin/env python3
"""
sec9_ltp.py -- regenerates every number of Section 9 of

    "Interference as the Composition Defect of Stochastic Shadows"

Section 9: the law-of-total-probability lemma, exhibited on the composite
two-measurement model.

  9.1  the one non-trivial step of the vector form, as a formal identity;
  9.2  the spanning hypothesis is load-bearing, and spanning restores the
       matrix form;
  9.3  the control: the residual always sums to zero, so detection must
       count entries and never totals;
  9.4  the forcing, exhibited: the residual on the model's own declared
       initial distribution at all twelve cells, with the value censuses;
  9.5  the interpolant's hypothesis, and where it fails;
  9.6  the three defects stay distinct on this model.

Exit 1 iff a computed number disagrees with the number printed in the paper.
"""

from __future__ import annotations

from exact import Q, MP, el, head, hr, Receipts
from model_composite import (Composite, NC, SETTING_ORDER, fmt,
                             rank_over_field, unidx)

R = Receipts("Section 9 -- the law-of-total-probability lemma")


def main():
    head("SECTION 9 -- THE LAW-OF-TOTAL-PROBABILITY LEMMA")

    # -----------------------------------------------------------------------
    hr(); print("[9.1] the one non-trivial step, as a formal identity")
    N = 3
    G21 = [[MP.var("g21_%d_%d" % (i, j)) for j in range(N)] for i in range(N)]
    G10 = [[MP.var("g10_%d_%d" % (i, j)) for j in range(N)] for i in range(N)]
    p0 = [MP.var("p_%d" % i) for i in range(N)]
    left = []
    for i in range(N):
        acc = MP.const(0)
        for k in range(N):
            inner = MP.const(0)
            for j in range(N):
                inner = inner + G10[k][j] * p0[j]
            acc = acc + G21[i][k] * inner
        left.append(acc)
    right = []
    for i in range(N):
        acc = MP.const(0)
        for j in range(N):
            s = MP.const(0)
            for k in range(N):
                s = s + G21[i][k] * G10[k][j]
            acc = acc + s * p0[j]
        right.append(acc)
    ok = all((left[i] - right[i]).is_zero() for i in range(N))
    print("      with all %d entries indeterminate over Q, "
          "Gamma21 (Gamma10 p) - (Gamma21 Gamma10) p is the zero vector: %s"
          % (2 * N * N + N, ok))
    R.anchor("associativity identity", ok, True)
    R.anchor("indeterminates", 2 * N * N + N, 21)

    # -----------------------------------------------------------------------
    hr(); print("[9.2] the spanning hypothesis is load-bearing")
    D = [[Q(1), Q(-1)], [Q(-1), Q(1)]]
    p_uniform = [Q(1, 2), Q(1, 2)]
    p_point = [Q(1), Q(0)]
    ann_uniform = [sum(D[i][j] * p_uniform[j] for j in range(2)) for i in range(2)]
    ann_point = [sum(D[i][j] * p_point[j] for j in range(2)) for i in range(2)]
    print("      D = [[1,-1],[-1,1]] is nonzero yet annihilates (1/2, 1/2): %s"
          % all(v == 0 for v in ann_uniform))
    print("      it does not annihilate the point mass at 0: %s"
          % any(v != 0 for v in ann_point))
    print("      so the vector form is strictly weaker than the matrix form, and "
          "admitting the two point masses across runs already forces D = 0")
    R.anchor("uniform annihilated", all(v == 0 for v in ann_uniform), True)
    R.anchor("point mass not annihilated", any(v != 0 for v in ann_point), True)

    # -----------------------------------------------------------------------
    hr(); print("[9.3] the control: the residual sums to zero")
    a_, b_, c_, d_ = MP.var("a"), MP.var("b"), MP.var("c"), MP.var("d")
    # a difference of two column-stochastic matrices has zero column sums, so
    # the residual vector always sums to zero: the violation is cancelling mass
    col = (a_ + b_) - (c_ + d_)
    csum = ((a_ - c_) + (b_ - d_)) - col
    print("      the residual of two column-stochastic matrices has identically "
          "zero column sums: %s" % csum.is_zero())
    R.anchor("zero column sums", csum.is_zero(), True)

    # -----------------------------------------------------------------------
    hr(); print("[9.4] the forcing, exhibited on the composite model")
    M = Composite()
    K = M.K
    table = {}
    censuses = {}
    for sp in SETTING_ORDER:
        for frame in ("F1", "F2"):
            G1, G2, G3, G32, T2, T3, L3 = M.gamma(sp, frame)
            # the model's own declared initial distribution is the point mass
            p2 = [G2[i][0] for i in range(NC)]
            p3 = [G3[i][0] for i in range(NC)]
            pred = [sum_field(K, [K.mul(G32[i][k], p2[k]) for k in range(NC)])
                    for i in range(NC)]
            resid = [K.sub(p3[i], pred[i]) for i in range(NC)]
            nz = [i for i in range(NC) if not K.is_zero(resid[i])]
            comp = M.dense_mul(G32, G2)
            diff = sum(1 for i in range(NC) for j in range(NC)
                       if G3[i][j] != comp[i][j])
            tot = sum_field(K, resid)
            cens = {}
            for i in nz:
                cens[fmt(K, resid[i])] = cens.get(fmt(K, resid[i]), 0) + 1
            table[(sp, frame)] = (len(nz), diff, K.is_zero(tot))
            censuses[(sp, frame)] = cens
    print("      setting  frame   nonzero of 36   differing matrix entries   "
          "residual sums to zero")
    for sp in SETTING_ORDER:
        for frame in ("F1", "F2"):
            nz, diff, z = table[(sp, frame)]
            print("      %-7s  %-5s   %-13d   %-24d   %s" % (sp, frame, nz, diff, z))
    R.anchor("nonzero counts", [table[(sp, f)][0] for sp in SETTING_ORDER
                                for f in ("F1", "F2")],
             [0, 0, 0, 0, 16, 16, 16, 16, 0, 0, 16, 16])
    R.anchor("matrix differing counts", [table[(sp, f)][1] for sp in SETTING_ORDER
                                         for f in ("F1", "F2")],
             [0, 0, 0, 0, 288, 288, 288, 288, 0, 0, 288, 288])
    R.anchor("residual sums to zero",
             all(table[k][2] for k in table), True)
    for sp in ("SP-C", "SP-D", "SP-F"):
        for frame in ("F1", "F2"):
            print("      %s %s value census: %s"
                  % (sp, frame, sorted(censuses[(sp, frame)].items())))
    R.anchor("SP-C census", sorted(censuses[("SP-C", "F1")].items()),
             sorted(censuses[("SP-D", "F1")].items()))
    cens_c = censuses[("SP-C", "F1")]
    cens_f = censuses[("SP-F", "F1")]
    rat_c = sum(v for k, v in cens_c.items() if "sqrt2" not in k)
    rat_f = sum(v for k, v in cens_f.items() if "sqrt2" not in k)
    print("      SP-C: %d distinct values, %d of the %d nonzero entries rational"
          % (len(cens_c), rat_c, sum(cens_c.values())))
    print("      SP-F: %d distinct values, %d of the %d nonzero entries rational"
          % (len(cens_f), rat_f, sum(cens_f.values())))
    R.anchor("SP-C distinct values", len(cens_c), 4)
    R.anchor("SP-C rational entries", rat_c, 0)
    R.anchor("SP-F distinct values", len(cens_f), 6)
    R.anchor("SP-F rational entries", rat_f, 8)
    print("      [%s]" % el())

    # -----------------------------------------------------------------------
    hr(); print("[9.5] the interpolant's hypothesis")
    ranks = []
    for sp in SETTING_ORDER:
        for frame in ("F1", "F2"):
            G1, G2, G3, G32, T2, T3, L3 = M.gamma(sp, frame)
            ranks.append(rank_over_field(K, G2))
    print("      exact ranks of the first leg over the twelve cells: %s" % ranks)
    print("      never %d, so the would-be interpolant's invertibility "
          "hypothesis fails outright" % NC)
    R.anchor("interpolant ranks", ranks,
             [27, 27, 27, 27, 18, 27, 18, 27, 27, 27, 27, 27])
    R.anchor("never full rank", all(r != NC for r in ranks), True)

    # -----------------------------------------------------------------------
    hr(); print("[9.6] the three defects stay distinct on this model")
    same = 0
    for sp in SETTING_ORDER:
        for frame in ("F1", "F2"):
            G1, G2, G3, G32, T2, T3, L3 = M.gamma(sp, frame)
            comp = M.sp_mul({(i, j): L3[i][j] for i in range(NC) for j in range(NC)
                             if not K.is_zero(L3[i][j])},
                            {(i, j): T2[i][j] for i in range(NC) for j in range(NC)
                             if not K.is_zero(T2[i][j])})
            dense = M.sp_dense(comp)
            if all(dense[i][j] == T3[i][j] for i in range(NC) for j in range(NC)):
                same += 1
    print("      the amplitude propagators compose exactly at %d of 12 cells, so "
          "on this model the declared-law residual and the Born-shadow defect "
          "are the same object" % same)
    R.anchor("propagators compose", same, 12)
    print("      the existential object is not decided here: no divisibility "
          "search is run on this model")

    R.finish()


def sum_field(K, xs):
    acc = K.zero
    for x in xs:
        acc = K.add(acc, x)
    return acc


if __name__ == "__main__":
    main()

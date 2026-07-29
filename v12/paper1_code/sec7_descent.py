#!/usr/bin/env python3
"""
sec7_descent.py -- regenerates every number of Section 7 of

    "Interference as the Composition Defect of Stochastic Shadows"

Section 7: record descent and its limit.

  7.1  availability alone block-diagonalizes the cut-coherence tensor;
  7.2  both hypotheses make it fully diagonal, recovering the records theorem;
  7.3  block-diagonality is not phase triviality: a coarse record;
  7.4  the eraser restores the cross-sector entries;
  7.5  on unitary families a fully diagonal tensor always carries a record --
       with the degeneracy of the block-structured census disclosed;
  7.6  the limit: a recorded pair whose composite is still phase-nontrivial.

Exit 1 iff a computed number disagrees with the number printed in the paper.
"""

from __future__ import annotations

import itertools

from exact import Q, Cyc, born, el, head, hr, is_unitary, mat_mul, Receipts
from sec4_records import (h_avail, h_corr, kron, labels_of, merge_partition,
                          set_partitions, support_of, delta_field, zero_mat)

R = Receipts("Section 7 -- record descent")


def tensor(K, U2, U1, n):
    """C^{ij}_{kl} = w_k^{ij} conj(w_l^{ij}) with w_k^{ij} = U2_ik U1_kj."""
    out = {}
    for i in range(n):
        for j in range(n):
            w = [K.mul(U2[i][k], U1[k][j]) for k in range(n)]
            out[(i, j)] = [[K.mul(w[k], K.conj(w[l])) for l in range(n)]
                           for k in range(n)]
    return out


def cross_sector(K, C, part, n):
    return sum(1 for (i, j), M in C.items() for k in range(n) for l in range(n)
               if part[k] != part[l] and not K.is_zero(M[k][l]))


def off_diagonal(K, C, n):
    return sum(1 for (i, j), M in C.items() for k in range(n) for l in range(n)
               if k != l and not K.is_zero(M[k][l]))


def main():
    head("SECTION 7 -- RECORD DESCENT AND ITS LIMIT")
    K = Cyc(8)
    isq2 = K.scal(K.add(K.zpow(1), K.zpow(-1)), Q(1, 2))
    H = [[isq2, isq2], [isq2, K.neg(isq2)]]
    I2 = [[K.one, K.zero], [K.zero, K.one]]
    CNOT = [[K.one, K.zero, K.zero, K.zero],
            [K.zero, K.one, K.zero, K.zero],
            [K.zero, K.zero, K.zero, K.one],
            [K.zero, K.zero, K.one, K.zero]]
    ops = [kron(K, I2, I2), kron(K, H, I2), kron(K, I2, H), kron(K, H, H),
           CNOT, mat_mul(K, CNOT, kron(K, H, I2)),
           mat_mul(K, kron(K, H, I2), CNOT),
           [[K.one, K.zero, K.zero, K.zero], [K.zero, K.zero, K.one, K.zero],
            [K.zero, K.one, K.zero, K.zero], [K.zero, K.zero, K.zero, K.one]]]
    assert all(is_unitary(K, M) for M in ops)
    parts15 = [labels_of(p, 4) for p in set_partitions(4)]

    # -----------------------------------------------------------------------
    hr(); print("[7.1-7.2] the two descent theorems")
    n_avail = n_avail_block = 0
    n_both = n_both_diag = n_both_flat = 0
    for U2 in ops:
        S2 = support_of(K, U2)
        for U1 in ops:
            S1 = support_of(K, U1)
            C = tensor(K, U2, U1, 4)
            for pi in parts15:
                a, c = h_avail(S2, 4, pi), h_corr(S1, 4, pi)
                if a:
                    n_avail += 1
                    if cross_sector(K, C, pi, 4) == 0:
                        n_avail_block += 1
                if a and c:
                    n_both += 1
                    if off_diagonal(K, C, 4) == 0:
                        n_both_diag += 1
                    if zero_mat(K, delta_field(K, U2, U1)):
                        n_both_flat += 1
    print("      8 declared operators x 15 partitions x 8 = 960 triples")
    print("      availability holds on %d; the tensor is block-diagonal on all %d"
          % (n_avail, n_avail_block))
    print("      both hypotheses hold on %d; the tensor is fully diagonal on %d "
          "and the defect vanishes on %d" % (n_both, n_both_diag, n_both_flat))
    R.anchor("availability triples", n_avail, 432)
    R.anchor("block-diagonal", n_avail_block, 432)
    R.anchor("both-hypothesis triples", n_both, 259)
    R.anchor("fully diagonal", n_both_diag, 259)
    R.anchor("defect vanishes", n_both_flat, 259)

    # -----------------------------------------------------------------------
    hr(); print("[7.3] block-diagonality is not phase triviality")
    U2c, U1c = kron(K, I2, H), kron(K, I2, H)
    coarse = [0, 0, 1, 1]
    Cc = tensor(K, U2c, U1c, 4)
    cs = cross_sector(K, Cc, coarse, 4)
    od = off_diagonal(K, Cc, 4)
    Dc = delta_field(K, U2c, U1c)
    print("      at the coarse record [0,0,1,1] with U2 = U1 = I x H: "
          "cross-sector entries %d, off-diagonal entries inside the blocks %d, "
          "defect zero = %s" % (cs, od, zero_mat(K, Dc)))
    R.anchor("coarse cross-sector", cs, 0)
    R.anchor("coarse in-block off-diagonal", od, 16)
    R.anchor("coarse availability", h_avail(support_of(K, U2c), 4, coarse), True)
    R.anchor("coarse correlation fails", h_corr(support_of(K, U1c), 4, coarse), False)
    R.anchor("coarse defect nonzero", zero_mat(K, Dc), False)

    # -----------------------------------------------------------------------
    hr(); print("[7.4] the eraser restores the cross-sector entries")
    U1e = mat_mul(K, CNOT, kron(K, H, I2))
    U2p = kron(K, H, I2)
    U2e = mat_mul(K, kron(K, H, I2), CNOT)
    rec = [0, 1, 0, 1]
    Cp = tensor(K, U2p, U1e, 4)
    Ce = tensor(K, U2e, U1e, 4)
    print("      preserving leg: cross-sector %d, off-diagonal %d"
          % (cross_sector(K, Cp, rec, 4), off_diagonal(K, Cp, 4)))
    print("      erasing leg   : cross-sector %d, off-diagonal %d"
          % (cross_sector(K, Ce, rec, 4), off_diagonal(K, Ce, 4)))
    De = delta_field(K, U2e, U1e)
    vals = sorted({str(K.to_rat(v)) for r in De for v in r})
    print("      correlation still holds = %s ; availability fails = %s ; the "
          "residual returns with entries %s"
          % (h_corr(support_of(K, U1e), 4, rec),
             not h_avail(support_of(K, U2e), 4, rec), vals))
    R.anchor("preserving cross-sector", cross_sector(K, Cp, rec, 4), 0)
    R.anchor("preserving off-diagonal", off_diagonal(K, Cp, 4), 0)
    R.anchor("eraser cross-sector", cross_sector(K, Ce, rec, 4), 16)
    R.anchor("eraser correlation holds", h_corr(support_of(K, U1e), 4, rec), True)
    R.anchor("eraser availability fails", h_avail(support_of(K, U2e), 4, rec), False)
    R.anchor("eraser residual values", vals, ["-1/2", "0", "1/2"])

    # -----------------------------------------------------------------------
    hr(); print("[7.5] a fully diagonal tensor on unitary families")
    diag_pairs = 0
    diag_with_record = 0
    for U2 in ops:
        S2 = support_of(K, U2)
        for U1 in ops:
            S1 = support_of(K, U1)
            C = tensor(K, U2, U1, 4)
            if off_diagonal(K, C, 4) == 0:
                diag_pairs += 1
                if h_corr(S1, 4, merge_partition(S2, 4)):
                    diag_with_record += 1
    print("      of the 64 ordered pairs, %d have a fully diagonal tensor and "
          "the decision criterion finds a record in %d of them"
          % (diag_pairs, diag_with_record))
    R.anchor("diagonal pairs", diag_pairs, 49)
    R.anchor("diagonal pairs with a record", diag_with_record, 49)

    # the block-structured census, and its declared degeneracy
    blocks = []
    for t in range(8):
        blocks.append(mat_mul(K, H, [[K.one, K.zero], [K.zero, K.zpow(t)]]))
    blocks.append(I2)
    blocks.append([[K.zero, K.one], [K.one, K.zero]])

    def embed(A, B, ra, ca, rb, cb):
        M = [[K.zero] * 4 for _ in range(4)]
        for i in range(2):
            for j in range(2):
                M[ra[i]][ca[j]] = A[i][j]
                M[rb[i]][cb[j]] = B[i][j]
        return M
    census = 0
    census_diag = 0
    census_rec = 0
    atmost1 = 0
    exactly1 = 0
    for A in blocks:
        for B in blocks:
            U2b = embed(A, B, [0, 1], [2, 3], [2, 3], [0, 1])
            for Cb in blocks:
                for Db in blocks:
                    U1b = embed(Cb, Db, [0, 2], [2, 3], [1, 3], [0, 1])
                    census += 1
                    live = [sum(1 for k in range(4)
                                if not K.is_zero(K.mul(U2b[i][k], U1b[k][j])))
                            for i in range(4) for j in range(4)]
                    if max(live) <= 1:
                        atmost1 += 1
                    if min(live) == 1 and max(live) == 1:
                        exactly1 += 1
                    T = tensor(K, U2b, U1b, 4)
                    if off_diagonal(K, T, 4) == 0:
                        census_diag += 1
                        if h_corr(support_of(K, U1b), 4,
                                  merge_partition(support_of(K, U2b), 4)):
                            census_rec += 1
    print("      the block-structured census: %d pairs, %d with a fully diagonal "
          "tensor, %d of those carrying a record" % (census, census_diag, census_rec))
    print("      DISCLOSED: %d of the %d have at most one live path per endpoint "
          "pair by the block pattern alone (%d have exactly one), so their "
          "diagonality is forced before any record question is asked"
          % (atmost1, census, exactly1))
    R.anchor("block census size", census, 10000)
    R.anchor("block census diagonal", census_diag, 10000)
    R.anchor("block census with record", census_rec, 10000)
    R.anchor("block census degenerate", atmost1, 10000)
    R.anchor("block census exactly one", exactly1, 4096)
    print("      [%s]" % el())

    # -----------------------------------------------------------------------
    hr(); print("[7.6] the limit of record descent")
    Hd = [[K.mul(H[i][j], K.zpow(1) if j == 1 else K.one) for j in range(2)]
          for i in range(2)]
    U2w = embed(H, H, [0, 1], [2, 3], [2, 3], [0, 1])
    U2wp = embed(H, Hd, [0, 1], [2, 3], [2, 3], [0, 1])
    U1w = embed(H, H, [0, 2], [2, 3], [1, 3], [0, 1])
    S2w, S1w = support_of(K, U2w), support_of(K, U1w)
    mp = merge_partition(S2w, 4)
    hasrec = h_corr(S1w, 4, mp)
    Tw = tensor(K, U2w, U1w, 4)
    od_w = off_diagonal(K, Tw, 4)
    P1 = mat_mul(K, U2w, U1w)
    P2 = mat_mul(K, U2wp, U1w)

    def haag(M, i, ip, j, jp):
        return K.mul(K.mul(M[i][j], M[ip][jp]),
                     K.mul(K.conj(M[i][jp]), K.conj(M[ip][j])))
    h1, h2 = haag(P1, 0, 2, 0, 2), haag(P2, 0, 2, 0, 2)
    print("      the witness pair carries a record structure (merge classes %s): "
          "%s ; its tensor is fully diagonal (%d off-diagonal entries)"
          % (mp, hasrec, od_w))
    print("      yet the two composites' four-cycle invariants differ: %s vs %s"
          % (h1, h2))
    R.anchor("limit merge classes", mp, [1, 1, 3, 3])
    R.anchor("limit has record", hasrec, True)
    R.anchor("limit tensor diagonal", od_w, 0)
    R.anchor("limit composites differ", h1 != h2, True)

    R.finish()


if __name__ == "__main__":
    main()

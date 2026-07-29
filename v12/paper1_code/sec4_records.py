#!/usr/bin/env python3
"""
sec4_records.py -- regenerates every number of Section 4 of

    "Interference as the Composition Defect of Stochastic Shadows"

Section 4: records.

  4.1  the two support hypotheses, and the termwise vanishing;
  4.2  the exhaustive n = 3 support sweep, and the realizable supports;
  4.3  the decision criterion, gated against every search;
  4.4  sharpness on realizable supports;
  4.5  the two monomial endpoints;
  4.6  the reading route, fine against coarse;
  4.7  the approximate-correlation bound and its tightness;
  4.8  the multi-cut corollary;
  4.9  the dimension-four exhibit and census;
  4.10 the composite model: the division-event biconditional;
  4.11 the eraser control, with the computed floor;
  4.12 the converse, refuted at this record notion.

Exit 1 iff a computed number disagrees with the number printed in the paper.
"""

from __future__ import annotations

import itertools

from exact import (Q, Cyc, born, el, head, hr, is_unitary, mat_mul, to_q2,
                   Receipts)
from model_composite import (Composite, SETTING_ORDER, SETTINGS, DEG, NC,
                             fmt, rank_over_field, unidx)

R = Receipts("Section 4 -- records")


# ---------------------------------------------------------------------------
# supports, hypotheses, the decision criterion
# ---------------------------------------------------------------------------
def rows_of(S, n):
    return [frozenset(j for j in range(n) if S[i][j]) for i in range(n)]


def cols_of(S, n):
    return [frozenset(i for i in range(n) if S[i][j]) for j in range(n)]


def h_avail(S2, n, part):
    """every row support of U2 lies in ONE record sector."""
    return all(len({part[k] for k in rs}) <= 1 for rs in rows_of(S2, n) if rs)


def h_corr(S1, n, part):
    """for every column of U1, the live alternatives lie in DISTINCT sectors."""
    for cs in cols_of(S1, n):
        labs = [part[k] for k in cs]
        if len(set(labs)) != len(labs):
            return False
    return True


def merge_partition(S2, n):
    """M(U2): the transitive closure of 'some later configuration receives
    amplitude from both'.  Union-find over the row supports of U2."""
    par = list(range(n))

    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a
    for rs in rows_of(S2, n):
        rs = sorted(rs)
        for k in rs[1:]:
            ra, rb = find(rs[0]), find(k)
            if ra != rb:
                par[ra] = rb
    return [find(k) for k in range(n)]


def criterion(S2, S1, n):
    """exists a record structure  <=>  M(U2) separates every co-live pair."""
    part = merge_partition(S2, n)
    return h_corr(S1, n, part), part


def set_partitions(n):
    if n == 0:
        yield []
        return
    for smaller in set_partitions(n - 1):
        for i in range(len(smaller)):
            yield smaller[:i] + [smaller[i] + [n - 1]] + smaller[i + 1:]
        yield smaller + [[n - 1]]


def labels_of(parts, n):
    lab = [0] * n
    for c, blk in enumerate(parts):
        for k in blk:
            lab[k] = c
    return lab


def is_q_pair(S2, S1, n):
    """every cross-term slot support-forced empty."""
    for i in range(n):
        for j in range(n):
            live = [k for k in range(n) if S2[i][k] and S1[k][j]]
            if len(live) >= 2:
                return False
    return True


def all_supports(n):
    out = []
    for bits in range(1 << (n * n)):
        S = [[(bits >> (i * n + j)) & 1 for j in range(n)] for i in range(n)]
        out.append(S)
    return out


def admissible_support(S, n):
    """the necessary condition for unitary realizability: no empty row or
    column, and any two rows -- and any two columns -- have supports that are
    disjoint or overlap in at least two places."""
    rs, cs = rows_of(S, n), cols_of(S, n)
    if any(not r for r in rs) or any(not c for c in cs):
        return False
    for a in range(n):
        for b in range(a + 1, n):
            if len(rs[a] & rs[b]) == 1:
                return False
            if len(cs[a] & cs[b]) == 1:
                return False
    return True


# ---------------------------------------------------------------------------
def kron(K, A, B):
    na, nb = len(A), len(B)
    return [[K.mul(A[i // nb][j // nb], B[i % nb][j % nb])
             for j in range(na * nb)] for i in range(na * nb)]


def delta_field(K, U2, U1):
    P = mat_mul(K, U2, U1)
    return [[K.sub(a, b) for a, b in zip(r1, r2)]
            for r1, r2 in zip(born(K, P), mat_mul(K, born(K, U2), born(K, U1)))]


def zero_mat(K, D):
    return all(K.is_zero(v) for r in D for v in r)


def support_of(K, M):
    n = len(M)
    return [[0 if K.is_zero(M[i][j]) else 1 for j in range(n)] for i in range(n)]


def main():
    head("SECTION 4 -- RECORDS")
    K = Cyc(8)
    isq2 = K.scal(K.add(K.zpow(1), K.zpow(-1)), Q(1, 2))
    H = [[isq2, isq2], [isq2, K.neg(isq2)]]
    I2 = [[K.one, K.zero], [K.zero, K.one]]
    CNOT = [[K.one, K.zero, K.zero, K.zero],
            [K.zero, K.one, K.zero, K.zero],
            [K.zero, K.zero, K.zero, K.one],
            [K.zero, K.zero, K.one, K.zero]]

    # -----------------------------------------------------------------------
    hr(); print("[4.1] the termwise vanishing on a declared coarse record")
    U1 = mat_mul(K, CNOT, kron(K, H, I2))
    U2 = kron(K, H, I2)
    part_rec = [0, 1, 0, 1]                      # the record is the second bit
    S1, S2 = support_of(K, U1), support_of(K, U2)
    print("      U1 = CNOT o (H x I), U2 = H x I, record sectors {0,2}, {1,3}")
    print("      (H-corr) = %s ; (H-avail) = %s"
          % (h_corr(S1, 4, part_rec), h_avail(S2, 4, part_rec)))
    terms = 0
    nonzero_terms = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(k + 1, 4):
                    terms += 1
                    w = K.mul(K.mul(U2[i][k], U1[k][j]),
                              K.conj(K.mul(U2[i][l], U1[l][j])))
                    if not K.is_zero(w):
                        nonzero_terms += 1
    D = delta_field(K, U2, U1)
    print("      %d cross terms, %d nonzero ; Delta = 0 : %s"
          % (terms, nonzero_terms, zero_mat(K, D)))
    B21 = born(K, mat_mul(K, U2, U1))
    col0 = [str(K.to_rat(B21[i][0])) for i in range(4)]
    print("      column 0 of the composite shadow = %s ; nothing is decohered" % col0)
    R.anchor("H-corr holds", h_corr(S1, 4, part_rec), True)
    R.anchor("H-avail holds", h_avail(S2, 4, part_rec), True)
    R.anchor("cross terms", terms, 96)
    R.anchor("nonzero cross terms", nonzero_terms, 0)
    R.anchor("defect vanishes", zero_mat(K, D), True)
    R.anchor("composite column 0", col0, ["1/4", "1/4", "1/4", "1/4"])
    U1b = kron(K, H, I2)
    Db = delta_field(K, U2, U1b)
    print("      removing the CNOT breaks (H-corr) and the defect returns: "
          "Delta_00 = %s" % to_q2(K, Db[0][0]))
    R.anchor("no-record Delta_00", str(to_q2(K, Db[0][0])), "1/2")
    R.anchor("no-record H-corr", h_corr(support_of(K, U1b), 4, part_rec), False)

    # -----------------------------------------------------------------------
    hr(); print("[4.2] the exhaustive n = 3 support sweep")
    n = 3
    parts5 = [labels_of(p, n) for p in set_partitions(n)]
    sups = all_supports(n)
    adm_triples = 0
    violations = 0
    qpairs = 0
    q_no_record = 0
    crit_disagree = 0
    comparisons = 0
    for T2s in sups:
        av = [pi for pi in parts5 if h_avail(T2s, n, pi)]
        mpart = merge_partition(T2s, n)
        for T1s in sups:
            qp = is_q_pair(T2s, T1s, n)
            search = any(h_corr(T1s, n, pi) for pi in av)
            crit = h_corr(T1s, n, mpart)
            comparisons += 1
            if search != crit:
                crit_disagree += 1
            for pi in av:
                if h_corr(T1s, n, pi):
                    adm_triples += 1
                    if not qp:
                        violations += 1
            if qp:
                qpairs += 1
                if not search:
                    q_no_record += 1
    print("      512 x 512 support pairs x 5 partitions")
    print("      admissible triples (both hypotheses) = %d, cross-term "
          "violations = %d" % (adm_triples, violations))
    print("      support-forced-flat pairs = %d, of which %d admit no record "
          "structure" % (qpairs, q_no_record))
    print("      decision criterion vs exhaustive search: %d comparisons, "
          "%d disagreements" % (comparisons, crit_disagree))
    R.anchor("n=3 admissible triples", adm_triples, 146536)
    R.anchor("n=3 violations", violations, 0)
    R.anchor("n=3 Q-pairs", qpairs, 94746)
    R.anchor("n=3 Q-pairs with no record", q_no_record, 5490)
    R.anchor("n=3 criterion comparisons", comparisons, 262144)
    R.anchor("n=3 criterion disagreements", crit_disagree, 0)
    print("      [%s]" % el())

    # -----------------------------------------------------------------------
    hr(); print("[4.3] the realizable supports at n = 3, with exact witnesses")
    adm = [S for S in sups if admissible_support(S, n)]
    print("      support patterns satisfying the necessary condition: %d" % len(adm))
    # explicit exact orthogonal witnesses for every one of them
    KR = Cyc(8)
    isq2R = KR.scal(KR.add(KR.zpow(1), KR.zpow(-1)), Q(1, 2))
    sqrt3 = Cyc(12).add(Cyc(12).zpow(1), Cyc(12).zpow(-1))
    K12 = Cyc(12)
    F3 = [[K12.mul(K12.inv(sqrt3), K12.zpow(4 * ((i * j) % 3))) for j in range(3)]
          for i in range(3)]
    onezero = [[Q(12, 25), Q(-9, 25), Q(4, 5)],
               [Q(16, 25), Q(-12, 25), Q(-3, 5)],
               [Q(3, 5), Q(4, 5), Q(0)]]
    # certify orthogonality of the rational witness exactly
    ortho_ok = all(sum(onezero[i][k] * onezero[j][k] for k in range(3))
                   == (1 if i == j else 0) for i in range(3) for j in range(3))
    witnesses = {}
    for perm in itertools.permutations(range(3)):
        S = [[1 if j == perm[i] else 0 for j in range(3)] for i in range(3)]
        witnesses[tuple(map(tuple, S))] = "permutation"
    witnesses[tuple(map(tuple, [[1] * 3] * 3))] = "F3"
    for r0 in range(3):
        for c0 in range(3):
            S = [[0] * 3 for _ in range(3)]
            S[r0][c0] = 1
            rs = [i for i in range(3) if i != r0]
            cs = [j for j in range(3) if j != c0]
            for i in rs:
                for j in cs:
                    S[i][j] = 1
            witnesses[tuple(map(tuple, S))] = "1 (+) H"
    for zr in range(3):
        for zc in range(3):
            S = [[1] * 3 for _ in range(3)]
            S[zr][zc] = 0
            witnesses[tuple(map(tuple, S))] = "one-zero rational orthogonal"
    covered = sum(1 for S in adm if tuple(map(tuple, S)) in witnesses)
    print("      exact witnesses exhibited for %d of them (%d permutations, "
          "1 full, 9 of type 1 (+) H, 9 with a single zero)"
          % (covered, 6))
    R.anchor("n=3 realizable supports", len(adm), 25)
    R.anchor("n=3 witnesses cover", covered, 25)
    R.anchor("one-zero witness orthogonal", ortho_ok, True)
    R.anchor("F3 unitary", is_unitary(K12, F3), True)

    hr(); print("[4.4] sharpness on the realizable supports")
    tot = qp_r = qp_r_norec = 0
    for A2 in adm:
        mpart = merge_partition(A2, n)
        for A1 in adm:
            tot += 1
            if is_q_pair(A2, A1, n):
                qp_r += 1
                if not h_corr(A1, n, mpart):
                    qp_r_norec += 1
    print("      %d ordered pairs of realizable supports; %d support-forced flat; "
          "%d of those admit no record structure" % (tot, qp_r, qp_r_norec))
    R.anchor("realizable pairs", tot, 625)
    R.anchor("realizable Q-pairs", qp_r, 318)
    R.anchor("realizable Q-pairs with no record", qp_r_norec, 0)

    # -----------------------------------------------------------------------
    hr(); print("[4.5] the two monomial endpoints")
    finest = list(range(n))
    trivial = [0] * n
    bad = 0
    for S in sups:
        rowmon = all(sum(r) <= 1 for r in S)
        colmon = all(sum(S[i][j] for i in range(n)) <= 1 for j in range(n))
        if h_avail(S, n, finest) != rowmon:
            bad += 1
        if h_corr(S, n, trivial) != colmon:
            bad += 1
    print("      (H-avail) at the finest record <=> row-monomial, and (H-corr) "
          "at the trivial record <=> column-monomial: %d failures over 512 "
          "supports x 2" % bad)
    R.anchor("monomial endpoints", bad, 0)

    # -----------------------------------------------------------------------
    hr(); print("[4.6] the reading route, fine against coarse")
    # pinching onto the record sectors, then the later leg
    def read_shadow(K, U2, U1, part, dim):
        out = [[K.zero] * dim for _ in range(dim)]
        sectors = {}
        for k in range(dim):
            sectors.setdefault(part[k], []).append(k)
        for j in range(dim):
            # rho = U1 |j><j| U1^dagger, pinched onto the sectors
            for i in range(dim):
                acc = K.zero
                for blk in sectors.values():
                    for k in blk:
                        for l in blk:
                            t = K.mul(K.mul(U2[i][k], U1[k][j]),
                                      K.conj(K.mul(U2[i][l], U1[l][j])))
                            acc = K.add(acc, t)
                out[i][j] = acc
        return out
    fine = read_shadow(K, U2, U1, [0, 1, 2, 3], 4)
    prod = mat_mul(K, born(K, U2), born(K, U1))
    coarse_part = [0, 0, 0, 0]
    coarse = read_shadow(K, U2, U1, coarse_part, 4)
    unread = born(K, mat_mul(K, U2, U1))
    print("      fine reading equals B(U2)B(U1) : %s" % (fine == prod))
    print("      coarse (one-sector) reading equals the unread shadow : %s"
          % (coarse == unread))
    stoch = all(K.to_rat(v) is not None and K.to_rat(v) >= 0 for r in fine for v in r)
    colsum = all(K.to_rat(sum_field(K, [fine[i][j] for i in range(4)])) == 1
                 for j in range(4))
    print("      the read shadow is a genuine stochastic matrix : %s"
          % (stoch and colsum))
    R.anchor("fine reading divides", fine == prod, True)
    R.anchor("coarse reading is the unread shadow", coarse == unread, True)
    R.anchor("read shadow stochastic", stoch and colsum, True)
    # a genuinely coarse SEPARATING record: two sectors of size two
    U1c = mat_mul(K, CNOT, kron(K, H, I2))
    sep = read_shadow(K, U2, U1c, [0, 1, 0, 1], 4)
    R.anchor("coarse separating reading divides",
             sep == mat_mul(K, born(K, U2), born(K, U1c)), True)

    # -----------------------------------------------------------------------
    hr(); print("[4.7] the approximate-correlation bound")
    devs = [Q(0), Q(1, 8), Q(1, 4), Q(3, 8), Q(1, 2), Q(5, 8)]
    pts = eq = pos = 0
    for e in devs:
        for j in (0, 1):
            g10 = {0: Q(1, 2), 1: Q(1, 2)}
            d = {0: (Q(0) if j == 0 else e), 1: (Q(0) if j == 0 else -e)}
            lhs = Q(0)
            rhs = Q(0)
            for r in (0, 1):
                sig_rj = [Q(1, 2) + d[r], Q(1, 2) - d[r]]
                sig_r = [Q(1, 2), Q(1, 2)]
                lhs += g10[r] * sum(abs(a - b) for a, b in zip(sig_rj, sig_r))
                rhs += g10[r] * sum(abs(a - b) for a, b in zip(sig_rj, sig_r))
            resid = Q(0)
            for r in (0, 1):
                resid += g10[r] * 2 * abs(d[r])
            pts += 1
            if resid == rhs:
                eq += 1
            if resid > 0:
                pos += 1
    print("      %d declared points (6 deviations x 2 columns): the bound is an "
          "equality at %d of them, %d of which are strictly positive"
          % (pts, eq, pos))
    R.anchor("bound points", pts, 12)
    R.anchor("bound equalities", eq, 12)
    R.anchor("bound strictly positive", pos, 5)

    # -----------------------------------------------------------------------
    hr(); print("[4.8] the multi-cut corollary")
    I4 = [[K.one if i == j else K.zero for j in range(4)] for i in range(4)]

    def cnot(dim, ctrl, targ):
        M = [[K.zero] * dim for _ in range(dim)]
        nb = dim.bit_length() - 1
        for j in range(dim):
            bits = [(j >> (nb - 1 - t)) & 1 for t in range(nb)]
            if bits[ctrl]:
                bits[targ] ^= 1
            i = 0
            for b in bits:
                i = (i << 1) | b
            M[i][j] = K.one
        return M

    def hadam(dim, q):
        nb = dim.bit_length() - 1
        M = [[K.one]]
        Ks = K
        for t in range(nb):
            block = H if t == q else I2
            M = kron(Ks, M, block) if len(M) > 1 else block
        return M
    chain3 = [mat_mul(K, cnot(8, 0, 1), hadam(8, 0)),
              mat_mul(K, cnot(8, 0, 2), hadam(8, 0)),
              hadam(8, 0)]
    prod3 = chain3[2]
    for M in (chain3[1], chain3[0]):
        prod3 = mat_mul(K, prod3, M)
    lhs3 = born(K, prod3)
    rhs3 = mat_mul(K, born(K, chain3[2]),
                   mat_mul(K, born(K, chain3[1]), born(K, chain3[0])))
    chain4 = [mat_mul(K, cnot(16, 0, 1), hadam(16, 0)),
              mat_mul(K, cnot(16, 0, 2), hadam(16, 0)),
              mat_mul(K, cnot(16, 0, 3), hadam(16, 0)),
              hadam(16, 0)]
    prod4 = chain4[3]
    for M in (chain4[2], chain4[1], chain4[0]):
        prod4 = mat_mul(K, prod4, M)
    lhs4 = born(K, prod4)
    rhs4 = born(K, chain4[3])
    for M in (chain4[2], chain4[1], chain4[0]):
        rhs4 = mat_mul(K, rhs4, born(K, M))
    print("      three-leg chain on 8 configurations, records at both cuts: "
          "Chapman-Kolmogorov holds = %s" % (lhs3 == rhs3))
    print("      four-leg chain on 16 configurations, records at three cuts: "
          "Chapman-Kolmogorov holds = %s" % (lhs4 == rhs4))
    R.anchor("three-leg chain", lhs3 == rhs3, True)
    R.anchor("four-leg chain", lhs4 == rhs4, True)

    # -----------------------------------------------------------------------
    hr(); print("[4.9] the dimension-four census over all 15 partitions")
    ops = [kron(K, I2, I2), kron(K, H, I2), kron(K, I2, H), kron(K, H, H),
           CNOT, mat_mul(K, CNOT, kron(K, H, I2)),
           mat_mul(K, kron(K, H, I2), CNOT),
           [[K.one, K.zero, K.zero, K.zero], [K.zero, K.zero, K.one, K.zero],
            [K.zero, K.one, K.zero, K.zero], [K.zero, K.zero, K.zero, K.one]]]
    assert all(is_unitary(K, M) for M in ops)
    parts15 = [labels_of(p, 4) for p in set_partitions(4)]
    both = 0
    both_flat = 0
    triples = 0
    flat_pairs = 0
    flat_with_record = 0
    for U2m in ops:
        S2m = support_of(K, U2m)
        for U1m in ops:
            S1m = support_of(K, U1m)
            flat = zero_mat(K, delta_field(K, U2m, U1m))
            if flat:
                flat_pairs += 1
                if h_corr(S1m, 4, merge_partition(S2m, 4)):
                    flat_with_record += 1
            for pi in parts15:
                triples += 1
                if h_avail(S2m, 4, pi) and h_corr(S1m, 4, pi):
                    both += 1
                    if flat:
                        both_flat += 1
    print("      8 declared operators, %d (partition, U2, U1) triples; %d satisfy "
          "both hypotheses, %d of those have a vanishing defect"
          % (triples, both, both_flat))
    print("      of the 64 ordered pairs, %d have a vanishing defect and %d of "
          "those carry a record structure" % (flat_pairs, flat_with_record))
    R.anchor("dim-4 triples", triples, 960)
    R.anchor("dim-4 both hypotheses", both, 259)
    R.anchor("dim-4 both and flat", both_flat, 259)
    R.anchor("dim-4 flat pairs", flat_pairs, 49)
    R.anchor("dim-4 flat with record", flat_with_record, 49)

    # -----------------------------------------------------------------------
    hr(); print("[4.10] the composite model: the division-event biconditional")
    M = Composite()
    KF = M.K
    prep = M.U_prep()
    print("      U_prep exactly orthogonal : %s" % M.is_orthogonal(prep))
    R.anchor("U_prep orthogonal", M.is_orthogonal(prep), True)
    col = {i: v for (i, j), v in prep.items() if j == 0}
    colvals = sorted((i, fmt(KF, v)) for i, v in col.items())
    print("      the j0 column of U_prep: %s" % colvals)
    R.anchor("prep j0 column", colvals,
             [(9, "1/2*sqrt2"), (18, "-1/2*sqrt2")])
    ops_ok = 0
    for ang in (0, 2, 4, 6):
        for wing in ("A", "B"):
            if M.is_orthogonal(M.U_local(wing, ang)):
                ops_ok += 1
    R.anchor("local operators orthogonal", ops_ok, 8)
    comm_ok = 0
    for a8 in (0, 2, 4):
        for b8 in (0, 2, 6):
            UA, UB = M.U_local("A", a8), M.U_local("B", b8)
            comm_ok += 1 if M.sp_mul(UA, UB) == M.sp_mul(UB, UA) else 0
    print("      the two local operators commute at all 9 setting pairs : %d/9"
          % comm_ok)
    R.anchor("local operators commute", comm_ok, 9)

    # the singlet outcome law
    law_ok = 0
    law_tot = 0
    for sp in SETTING_ORDER:
        a8, b8 = SETTINGS[sp]
        for frame in ("F1", "F2"):
            law = M.outcome_law(sp, frame)
            dk = abs(a8 - b8)                     # a - b = dk * pi/8
            cosab = M.cos[dk] if dk <= 4 else KF.neg(M.cos[8 - dk])
            for pa in (1, 2):
                for pb in (1, 2):
                    p = law.get((pa, pb), KF.zero)
                    al = 1 if pa == 1 else -1
                    be = 1 if pb == 1 else -1
                    pred = KF.scal(KF.sub(KF.one, KF.scal(cosab, al * be)), Q(1, 4))
                    law_tot += 1
                    law_ok += 1 if p == pred else 0
            marg_ok = all(
                KF.add(law.get((pa, 1), KF.zero), law.get((pa, 2), KF.zero))
                == KF.rat(Q(1, 2)) for pa in (1, 2))
            law_tot += 1
            law_ok += 1 if marg_ok else 0
    print("      the singlet outcome law P = (1 - alpha beta cos(a-b))/4 : "
          "%d/%d exact identities" % (law_ok, law_tot))
    R.anchor("singlet law identities", (law_ok, law_tot), (60, 60))

    # divisibility and record existence at all twelve cells
    coords = ["qA", "qB", "pA", "pB"]
    declared = []
    for mask in range(16):
        declared.append(tuple(c for t, c in enumerate(coords) if (mask >> t) & 1))

    def part_from_mask(mask):
        lab = {}
        out = [0] * NC
        for i in range(NC):
            v = unidx(i)
            key = tuple(v[t] for t in range(4) if (mask >> t) & 1)
            if key not in lab:
                lab[key] = len(lab)
            out[i] = lab[key]
        return out
    parts16 = [part_from_mask(m) for m in range(16)]

    cells = {}
    diffcounts = {}
    for sp in SETTING_ORDER:
        for frame in ("F1", "F2"):
            G1, G2, G3, G32, T2, T3, L3 = M.gamma(sp, frame)
            comp = M.dense_mul(G32, G2)
            diff = sum(1 for i in range(NC) for j in range(NC)
                       if G3[i][j] != comp[i][j])
            S2m = [[0 if KF.is_zero(L3[i][j]) else 1 for j in range(NC)]
                   for i in range(NC)]
            S1m = [[0 if KF.is_zero(T2[i][j]) else 1 for j in range(NC)]
                   for i in range(NC)]
            mp = merge_partition(S2m, NC)
            exists = h_corr(S1m, NC, mp)
            wins = [declared[m] for m in range(16)
                    if h_avail(S2m, NC, parts16[m]) and h_corr(S1m, NC, parts16[m])]
            cells[(sp, frame)] = (diff == 0, exists, len(wins), wins)
            diffcounts[(sp, frame)] = diff
        print("      %s : F1 differing entries = %d, F2 = %d   [%s]"
              % (sp, diffcounts[(sp, "F1")], diffcounts[(sp, "F2")], el()))
    agree = sum(1 for k, v in cells.items() if v[0] == v[1])
    print("      the biconditional 'the cut divides <=> a record structure "
          "exists' holds at %d of 12 cells" % agree)
    for sp in SETTING_ORDER:
        for frame in ("F1", "F2"):
            d, e, nw, wins = cells[(sp, frame)]
            print("        %s %s : divides = %-5s  record exists = %-5s  "
                  "declared winners = %d %s"
                  % (sp, frame, d, e, nw, [".".join(w) if w else "trivial"
                                           for w in wins[:4]]))
    R.anchor("biconditional cells", agree, 12)
    R.anchor("differing entries", [diffcounts[(sp, f)] for sp in SETTING_ORDER
                                   for f in ("F1", "F2")],
             [0, 0, 0, 0, 288, 288, 288, 288, 0, 0, 288, 288])
    R.anchor("winner counts", [cells[(sp, f)][2] for sp in SETTING_ORDER
                               for f in ("F1", "F2")],
             [3, 2, 3, 2, 0, 0, 0, 0, 14, 14, 0, 0])

    # the exact ranks of Gamma(2<-0)
    ranks = []
    for sp in SETTING_ORDER:
        for frame in ("F1", "F2"):
            G1, G2, G3, G32, T2, T3, L3 = M.gamma(sp, frame)
            ranks.append(rank_over_field(KF, G2))
    print("      exact ranks of Gamma(2<-0), the twelve cells: %s" % ranks)
    R.anchor("Gamma(2<-0) ranks", ranks, [27, 27, 27, 27, 18, 27, 18, 27, 27, 27, 27, 27])
    R.anchor("no rank is 36", all(r != NC for r in ranks), True)

    # -----------------------------------------------------------------------
    hr(); print("[4.11] the eraser control")
    Uerase = mat_mul(K, kron(K, H, I2), CNOT)
    Dp = delta_field(K, U2, U1)
    De = delta_field(K, Uerase, U1)
    vals = sorted({str(K.to_rat(v)) for r in De for v in r})
    print("      preserving leg H x I : defect zero = %s" % zero_mat(K, Dp))
    print("      erasing leg (H x I) o CNOT : defect entries are %s" % vals)
    Se = support_of(K, Uerase)
    print("      (H-corr) still holds = %s ; (H-avail) fails = %s"
          % (h_corr(S1, 4, part_rec), not h_avail(Se, 4, part_rec)))
    comp_e = born(K, mat_mul(K, Uerase, U1))
    ident = [[K.rat(1 if i == j else 0) for j in range(4)] for i in range(4)]
    print("      the erased composite law is the identity : %s" % (comp_e == ident))
    R.anchor("preserving defect zero", zero_mat(K, Dp), True)
    R.anchor("eraser defect values", vals, ["-1/2", "0", "1/2"])
    R.anchor("eraser H-corr", h_corr(S1, 4, part_rec), True)
    R.anchor("eraser H-avail fails", h_avail(Se, 4, part_rec), False)
    R.anchor("erased composite is the identity", comp_e == ident, True)
    R.anchor("eraser has no record structure",
             h_corr(S1, 4, merge_partition(Se, 4)), False)

    G10 = [[K.to_rat(v) for v in row] for row in born(K, U1)]
    G20 = [[Q(1 if i == j else 0) for j in range(4)] for i in range(4)]
    best_entry = None
    best_induced = None
    nvert = 0
    for assign in itertools.product(range(4), repeat=4):
        nvert += 1
        Kd = [[Q(1 if assign[j] == i else 0) for j in range(4)] for i in range(4)]
        prod = [[sum(Kd[i][k] * G10[k][j] for k in range(4)) for j in range(4)]
                for i in range(4)]
        e1 = sum(abs(G20[i][j] - prod[i][j]) for i in range(4) for j in range(4))
        ind = max(sum(abs(G20[i][j] - prod[i][j]) for i in range(4))
                  for j in range(4))
        if best_entry is None or e1 < best_entry:
            best_entry = e1
        if best_induced is None or ind < best_induced:
            best_induced = ind
    print("      the divisibility objective is affine, so the %d deterministic "
          "vertices exhaust the search" % nvert)
    print("      entrywise l1 floor = %s ; induced 1-norm floor = %s"
          % (best_entry, best_induced))
    R.anchor("eraser vertices", nvert, 256)
    R.anchor("entrywise l1 floor", str(best_entry), "4")
    R.anchor("induced 1-norm floor", str(best_induced), "1")

    # the eraser inside the composite model
    sp = "SP-A"
    G1, G2, G3, G32, T2, T3, L3 = M.gamma(sp, "F1")
    sT1, sT2, sT3, sL3 = M.propagators(sp, "F1")
    Tt = {(j, i): v for (i, j), v in sT2.items()}         # the exact reverse leg
    Gt = M.sp_dense(M.born_sparse(Tt))
    comp = M.dense_mul(Gt, G2)
    Gid = [[KF.rat(1 if i == j else 0) for j in range(NC)] for i in range(NC)]
    diff_er = sum(1 for i in range(NC) for j in range(NC)
                  if Gid[i][j] != comp[i][j])
    S2e = [[0 if KF.is_zero(Tt.get((i, j), KF.zero)) else 1 for j in range(NC)]
           for i in range(NC)]
    S1e = [[0 if KF.is_zero(T2[i][j]) else 1 for j in range(NC)] for i in range(NC)]
    er_rec = h_corr(S1e, NC, merge_partition(S2e, NC))
    er_declared = sum(1 for m in range(16)
                      if h_avail(S2e, NC, parts16[m]) and h_corr(S1e, NC, parts16[m]))
    print("      an eraser inside the composite model (the exact reverse leg): "
          "%d differing entries, %d of the 16 declared structures survive, "
          "record exists = %s" % (diff_er, er_declared, er_rec))
    R.anchor("composite eraser differing entries", diff_er, 36)
    R.anchor("composite eraser declared survivors", er_declared, 0)
    R.anchor("composite eraser record exists", er_rec, False)

    # -----------------------------------------------------------------------
    hr(); print("[4.12] the converse, at this record notion")
    Sph = [[K.one, K.zero], [K.zero, K.zpow(2)]]
    U1p = mat_mul(K, Sph, H)
    Dp2 = delta_field(K, H, U1p)
    S1p, S2p = support_of(K, U1p), support_of(K, H)
    has_rec = h_corr(S1p, 2, merge_partition(S2p, 2))
    print("      the pair (H, diag(1,i) H) has a vanishing defect = %s but "
          "carries no record structure = %s"
          % (zero_mat(K, Dp2), not has_rec))
    kicks_break = 0
    kicks_break_rec = 0
    for t in range(1, 8):
        Dk = [[K.one, K.zero], [K.zero, K.zpow(t)]]
        if not zero_mat(K, delta_field(K, H, mat_mul(K, Dk, U1p))):
            kicks_break += 1
        if not zero_mat(K, delta_field(K, kron(K, H, I2),
                                       mat_mul(K, blockdiag(K, Dk), U1))):
            kicks_break_rec += 1
    print("      7 declared diagonal phase insertions break the phase-aligned "
          "vanishing %d times, and the record-killed vanishing %d times"
          % (kicks_break, kicks_break_rec))
    R.anchor("phase-alignment defect zero", zero_mat(K, Dp2), True)
    R.anchor("phase-alignment has no record", has_rec, False)
    R.anchor("phase kicks break alignment", kicks_break, 6)
    R.anchor("phase kicks break the record kill", kicks_break_rec, 0)

    R.finish()


def sum_field(K, xs):
    acc = K.zero
    for x in xs:
        acc = K.add(acc, x)
    return acc


def blockdiag(K, D2):
    out = [[K.zero] * 4 for _ in range(4)]
    for i in range(2):
        for j in range(2):
            out[i][j] = D2[i][j]
            out[2 + i][2 + j] = D2[i][j]
    return out


if __name__ == "__main__":
    main()

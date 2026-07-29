#!/usr/bin/env python3
"""
sec5_gauge.py -- regenerates every number of Section 5 of

    "Interference as the Composition Defect of Stochastic Shadows"

Section 5: the gauge of a compositional law.

  5.1  the full entrywise orbit is exactly the modulus class;
  5.2  triple products are invariants of the one-index ray gauge, not of the
       entrywise matrix gauge; the four-cycle invariant survives;
  5.3  the composition-compatibility theorem, both halves, exhaustively over
       declared finite phase groups, with the degenerate-support measurement;
  5.4  the unitarity-preservation theorem, with the placed-rotation gap;
  5.5  the full gauge moves the composite's Born shadow;
  5.6  the boundary group and the uncompensated cut;
  5.7  the single-arrow orbit theorem: cycle rank, holonomy invariance,
       constructive completeness, support stratification.

Exit 1 iff a computed number disagrees with the number printed in the paper.
"""

from __future__ import annotations

import itertools

from exact import (Q, Cyc, born, cycle_rank, el, head, hr, is_unitary,
                   mat_mul, spanning_forest, Receipts)

R = Receipts("Section 5 -- the gauge of a compositional law")


def family2(K):
    isq2 = K.scal(K.add(K.zpow(1), K.zpow(-1)), Q(1, 2))
    H = [[isq2, isq2], [isq2, K.neg(isq2)]]
    fam = []
    for perm in ((0, 1), (1, 0)):
        for a in range(4):
            for b in range(4):
                d = [K.zpow(2 * a), K.zpow(2 * b)]
                M = [[K.zero, K.zero], [K.zero, K.zero]]
                for i in range(2):
                    M[i][perm[i]] = d[perm[i]]
                fam.append(M)
    for s in range(8):
        for t in range(8):
            fam.append(mat_mul(K, [[K.one, K.zero], [K.zero, K.zpow(s)]],
                               mat_mul(K, H, [[K.one, K.zero],
                                              [K.zero, K.zpow(t)]])))
    return fam, H


def family3(K):
    sqrt3 = K.add(K.zpow(1), K.zpow(-1))
    isq3 = K.inv(sqrt3)
    F3 = [[K.mul(isq3, K.zpow(4 * ((j * k) % 3))) for k in range(3)]
          for j in range(3)]
    fam = []
    for perm in itertools.permutations(range(3)):
        for a in range(3):
            for b in range(3):
                d = [K.one, K.zpow(4 * a), K.zpow(4 * b)]
                M = [[K.zero] * 3 for _ in range(3)]
                for i in range(3):
                    M[i][perm[i]] = d[perm[i]]
                fam.append(M)
    for a in range(3):
        for b in range(3):
            fam.append(mat_mul(
                K, [[K.one, K.zero, K.zero], [K.zero, K.zpow(4 * a), K.zero],
                    [K.zero, K.zero, K.one]],
                mat_mul(K, F3, [[K.one, K.zero, K.zero],
                                [K.zero, K.zpow(4 * b), K.zero],
                                [K.zero, K.zero, K.one]])))
    return fam, F3


def support(K, M):
    n = len(M)
    return tuple(tuple(0 if K.is_zero(M[i][j]) else 1 for j in range(n))
                 for i in range(n))


def moduli(K, M):
    return tuple(tuple(K.normsq(x) for x in row) for row in M)


def bipartite(S, n):
    edges = []
    for i in range(n):
        for j in range(n):
            if S[i][j]:
                edges.append((i, n + j))
    return edges


def switching_equivalent(K, U, V):
    """Build the vertex switching on the bipartite support graph, or report
    that none exists.  Returns (bool, d_row, d_col)."""
    n = len(U)
    if support(K, U) != support(K, V) or moduli(K, U) != moduli(K, V):
        return False, None, None
    adj = {}
    for i in range(n):
        for j in range(n):
            if not K.is_zero(U[i][j]):
                adj.setdefault(i, []).append(("c", j))
                adj.setdefault(n + j, []).append(("r", i))
    d = {}
    for start in range(2 * n):
        if start in d or start not in adj:
            continue
        d[start] = K.one
        stack = [start]
        while stack:
            v = stack.pop()
            for (kind, w) in adj[v]:
                wv = w if kind == "r" else n + w
                if kind == "c":
                    i, j = v, w
                else:
                    i, j = w, v - n
                # V_ij = d_i conj(d_j) U_ij
                ratio = K.mul(V[i][j], K.inv(U[i][j]))
                if wv in d:
                    continue
                # V_ij = d_i conj(d_{n+j}) U_ij
                if kind == "c":                # v is the row, wv the column
                    d[wv] = K.mul(K.conj(ratio), K.inv(K.conj(d[v])))
                else:                          # v is the column, wv the row
                    d[wv] = K.mul(ratio, K.inv(K.conj(d[v])))
                stack.append(wv)
    for i in range(n):
        for j in range(n):
            if K.is_zero(U[i][j]):
                continue
            di = d.get(i, K.one)
            dj = d.get(n + j, K.one)
            if K.mul(K.mul(di, K.conj(dj)), U[i][j]) != V[i][j]:
                return False, None, None
    return True, d, None


def haagerup(K, M, i, ip, j, jp):
    return K.mul(K.mul(M[i][j], M[ip][jp]),
                 K.mul(K.conj(M[i][jp]), K.conj(M[ip][j])))


def main():
    head("SECTION 5 -- THE GAUGE OF A COMPOSITIONAL LAW")
    K8 = Cyc(8)
    K12 = Cyc(12)
    F2, H = family2(K8)
    F3fam, F3 = family3(K12)

    # -----------------------------------------------------------------------
    hr(); print("[5.1] the full entrywise orbit is exactly the modulus class")
    reach = 0
    tested = 0
    for U in F2:
        for V in F2:
            if moduli(K8, U) != moduli(K8, V):
                continue
            tested += 1
            ok = True
            for i in range(2):
                for j in range(2):
                    if K8.is_zero(U[i][j]):
                        if not K8.is_zero(V[i][j]):
                            ok = False
                        continue
                    th = K8.mul(V[i][j], K8.inv(U[i][j]))
                    if K8.normsq(th) != K8.one:
                        ok = False
            reach += 1 if ok else 0
    classes = {}
    for U in F2:
        classes.setdefault(moduli(K8, U), []).append(U)
    multi = sum(1 for v in classes.values() if len(v) > 1)
    allphase = all(all(moduli(K8, mm) == key for mm in v)
                   for key, v in classes.items())
    print("      %d ordered pairs of the 2x2 family share their moduli; a "
          "unimodular connecting matrix is built in all %d" % (tested, reach))
    print("      %d Born-shadow classes, %d of them with more than one member"
          % (len(classes), multi))
    R.anchor("modulus-matched pairs", tested, 4608)
    R.anchor("connecting matrices built", reach, 4608)
    R.anchor("Born-shadow classes", len(classes), 3)
    R.anchor("multi-member classes", multi, 3)
    R.anchor("class members share moduli", allphase, True)

    # -----------------------------------------------------------------------
    hr(); print("[5.2] triple products, and the four-cycle invariant")
    full3 = [M for M in F3fam if all(not K12.is_zero(x) for r in M for x in r)]
    theta = [[K12.zpow(4) if (i, j) == (0, 1) else K12.one
              for j in range(3)] for i in range(3)]
    dout = [K12.one, K12.one, K12.zpow(4)]
    din = [K12.one, K12.one, K12.one]
    moved_schur = moved_bdry = ray_inv = 0
    hg_inv = 0
    hg_tot = 0
    for M in full3:
        def trip(X):
            return K12.mul(K12.mul(X[0][1], X[1][2]), X[2][0])
        Mth = [[K12.mul(theta[i][j], M[i][j]) for j in range(3)] for i in range(3)]
        Mbd = [[K12.mul(K12.mul(dout[i], K12.conj(din[j])), M[i][j])
                for j in range(3)] for i in range(3)]
        if trip(Mth) != trip(M):
            moved_schur += 1
        if trip(Mbd) != trip(M):
            moved_bdry += 1
        lam = [K12.one, K12.zpow(4), K12.zpow(8)]
        Mray = [[K12.mul(K12.mul(K12.conj(lam[i]), lam[j]), M[i][j])
                 for j in range(3)] for i in range(3)]
        if trip(Mray) == trip(M):
            ray_inv += 1
        for (i, ip) in itertools.combinations(range(3), 2):
            for (j, jp) in itertools.combinations(range(3), 2):
                hg_tot += 1
                if haagerup(K12, Mbd, i, ip, j, jp) == haagerup(K12, M, i, ip, j, jp):
                    hg_inv += 1
    print("      %d full-support 3x3 members; the triple product is moved by a "
          "declared entrywise gauge on %d and by a declared boundary gauge on %d"
          % (len(full3), moved_schur, moved_bdry))
    print("      under the one-index ray gauge it is invariant on %d of %d"
          % (ray_inv, len(full3)))
    print("      the four-cycle invariant is unchanged by the boundary gauge on "
          "%d of %d index quadruples" % (hg_inv, hg_tot))
    R.anchor("full-support 3x3 members", len(full3), 9)
    R.anchor("triple moved by entrywise gauge", moved_schur, 9)
    R.anchor("triple moved by boundary gauge", moved_bdry, 9)
    R.anchor("triple ray-invariant", ray_inv, 9)
    R.anchor("four-cycle boundary-invariant", (hg_inv, hg_tot), (81, 81))

    # -----------------------------------------------------------------------
    hr(); print("[5.3] the composition-compatibility theorem")

    def star_and_family(n, m):
        """count Theta pairs over mu_m satisfying (star), and those admitting
        an object-indexed family; entries are exponents modulo m."""
        allth = list(itertools.product(range(m), repeat=n * n))
        nstar = nfam = both = 0
        for A in allth:
            Am = [A[i * n:(i + 1) * n] for i in range(n)]
            for B in allth:
                Bm = [B[i * n:(i + 1) * n] for i in range(n)]
                star = True
                for i in range(n):
                    for j in range(n):
                        v = (Am[i][0] + Bm[0][j]) % m
                        for k in range(1, n):
                            if (Am[i][k] + Bm[k][j]) % m != v:
                                star = False
                                break
                        if not star:
                            break
                    if not star:
                        break
                d2 = [Am[i][0] % m for i in range(n)]
                d1 = [(Am[0][0] - Am[0][k]) % m for k in range(n)]
                d0 = [(-Bm[0][j]) % m for j in range(n)]
                fam = all((d2[i] - d1[k]) % m == Am[i][k] % m
                          for i in range(n) for k in range(n)) and \
                    all((d1[k] - d0[j]) % m == Bm[k][j] % m
                        for k in range(n) for j in range(n))
                nstar += 1 if star else 0
                nfam += 1 if fam else 0
                both += 1 if star == fam else 0
        return len(allth) ** 2, nstar, nfam, both

    for n, m in ((2, 4), (3, 2)):
        tot, ns, nf, agree = star_and_family(n, m)
        print("      n = %d over mu_%d : %d ordered Theta pairs; %d satisfy the "
              "pointwise equation, %d admit an object-indexed family, %d agreements"
              % (n, m, tot, ns, nf, agree))
        R.anchor("n=%d pairs" % n, tot, {2: 65536, 3: 262144}[n])
        R.anchor("n=%d star count" % n, ns, {2: 1024, 3: 256}[n])
        R.anchor("n=%d family count" % n, nf, {2: 1024, 3: 256}[n])
        R.anchor("n=%d agreements" % n, agree, {2: 65536, 3: 262144}[n])
        print("      [%s]" % el())

    # separately-boundary factors: the surplus is the uncompensated cut
    def boundary_thetas(n, m):
        out = set()
        for d in itertools.product(range(m), repeat=n):
            for e in itertools.product(range(m), repeat=n):
                out.add(tuple((d[i] - e[j]) % m for i in range(n) for j in range(n)))
        return out
    bt = boundary_thetas(2, 4)
    print("      boundary-form Theta at n = 2 over mu_4 : %d ; both factors "
          "separately of boundary form : %d ; surplus over the coupled count : %d"
          % (len(bt), len(bt) ** 2, len(bt) ** 2 - 1024))
    R.anchor("boundary Theta count", len(bt), 64)
    R.anchor("separately boundary pairs", len(bt) ** 2, 4096)
    R.anchor("uncompensated surplus", len(bt) ** 2 - 1024, 3072)

    # the quantifier, measured: a degenerate pair licenses nothing
    X = [[K8.zero, K8.one], [K8.one, K8.zero]]
    star_set = set()
    for A in itertools.product(range(4), repeat=4):
        Am = [A[0:2], A[2:4]]
        for B in itertools.product(range(4), repeat=4):
            Bm = [B[0:2], B[2:4]]
            good = True
            for i in range(2):
                for j in range(2):
                    v = (Am[i][0] + Bm[0][j]) % 4
                    if (Am[i][1] + Bm[1][j]) % 4 != v:
                        good = False
            if good:
                star_set.add((A, B))
    comp_counts = {}
    for label, (U2, U1) in (("(H, H)", (H, H)), ("(H, X)", (H, X))):
        cnt = 0
        agree = 0
        for A in itertools.product(range(4), repeat=4):
            Am = [[K8.zpow(2 * A[0]), K8.zpow(2 * A[1])],
                  [K8.zpow(2 * A[2]), K8.zpow(2 * A[3])]]
            TU2 = [[K8.mul(Am[i][j], U2[i][j]) for j in range(2)] for i in range(2)]
            for B in itertools.product(range(4), repeat=4):
                Bm = [[K8.zpow(2 * B[0]), K8.zpow(2 * B[1])],
                      [K8.zpow(2 * B[2]), K8.zpow(2 * B[3])]]
                TU1 = [[K8.mul(Bm[i][j], U1[i][j]) for j in range(2)]
                       for i in range(2)]
                L = mat_mul(K8, TU2, TU1)
                Rm = mat_mul(K8, U2, U1)
                ok = True
                for i in range(2):
                    for j in range(2):
                        if K8.is_zero(Rm[i][j]):
                            if not K8.is_zero(L[i][j]):
                                ok = False
                        else:
                            th = K8.mul(L[i][j], K8.inv(Rm[i][j]))
                            if K8.normsq(th) != K8.one:
                                ok = False
                if ok:
                    cnt += 1
                if ok == ((A, B) in star_set):
                    agree += 1
        comp_counts[label] = (cnt, agree)
        print("      compatibility measured on the single pair %s : %d of 65536 "
              "Theta pairs are compatible (agreement with the pointwise equation: "
              "%d)" % (label, cnt, agree))
    R.anchor("compatible on (H,H)", comp_counts["(H, H)"][0], 1024)
    R.anchor("(H,H) agrees with star", comp_counts["(H, H)"][1], 65536)
    R.anchor("compatible on (H,X)", comp_counts["(H, X)"][0], 65536)
    print("      [%s]" % el())

    # -----------------------------------------------------------------------
    hr(); print("[5.4] the unitarity-preservation theorem")

    def placed_unitary(K, n, i, j, k, l, c, s):
        """the unitary carrying columns {k,l} into rows {i,j}."""
        M = [[K.zero] * n for _ in range(n)]
        M[i][k] = c
        M[j][l] = c
        M[i][l] = K.neg(s)
        M[j][k] = s
        restr = [r for r in range(n) if r not in (i, j)]
        restc = [cc for cc in range(n) if cc not in (k, l)]
        for a, b in zip(restr, restc):
            M[a][b] = K.one
        return M

    for n, m, Kf in ((2, 8, K8), (3, 2, K12)):
        allth = list(itertools.product(range(m), repeat=n * n))
        bt = boundary_thetas(n, m)
        c = Kf.rat(Q(3, 5)); s = Kf.rat(Q(4, 5))
        placed = []
        for (i, j) in itertools.combinations(range(n), 2):
            for (k, l) in itertools.combinations(range(n), 2):
                U = placed_unitary(Kf, n, i, j, k, l, c, s)
                assert is_unitary(Kf, U)
                placed.append(U)
        coord = []
        for (k, l) in itertools.combinations(range(n), 2):
            U = placed_unitary(Kf, n, k, l, k, l, c, s)
            placed_ok = is_unitary(Kf, U)
            assert placed_ok
            coord.append(U)
        fam = F2 if n == 2 else F3fam
        stride = fam[::6] if n == 2 else fam[::5]
        n_pres = n_hg = n_bd = 0
        n_placed = n_coord = 0
        for A in allth:
            Th = [[Kf.zpow((Kf.n // m) * A[i * n + j]) for j in range(n)]
                  for i in range(n)]
            pres = all(is_unitary(Kf, [[Kf.mul(Th[i][j], U[i][j]) for j in range(n)]
                                       for i in range(n)]) for U in stride)
            hgt = all(haagerup(Kf, Th, i, ip, j, jp) == Kf.one
                      for (i, ip) in itertools.combinations(range(n), 2)
                      for (j, jp) in itertools.combinations(range(n), 2))
            bd = tuple(A[i * n + j] % m for i in range(n) for j in range(n)) in bt
            pl = all(is_unitary(Kf, [[Kf.mul(Th[i][j], U[i][j]) for j in range(n)]
                                     for i in range(n)]) for U in placed)
            co = all(is_unitary(Kf, [[Kf.mul(Th[i][j], U[i][j]) for j in range(n)]
                                     for i in range(n)]) for U in coord)
            n_pres += 1 if pres else 0
            n_hg += 1 if hgt else 0
            n_bd += 1 if bd else 0
            n_placed += 1 if pl else 0
            n_coord += 1 if co else 0
        print("      n = %d over mu_%d : %d Theta ; unitarity-preserving on the "
              "declared family %d ; four-cycle-trivial %d ; boundary form %d"
              % (n, m, len(allth), n_pres, n_hg, n_bd))
        print("            the placed construction leaves %d standing; the "
              "coordinate-plane rotations leave %d" % (n_placed, n_coord))
        R.anchor("n=%d Theta count" % n, len(allth), {2: 4096, 3: 512}[n])
        R.anchor("n=%d unitarity-preserving" % n, n_pres, {2: 512, 3: 32}[n])
        R.anchor("n=%d four-cycle-trivial" % n, n_hg, {2: 512, 3: 32}[n])
        R.anchor("n=%d boundary form" % n, n_bd, {2: 512, 3: 32}[n])
        R.anchor("n=%d placed" % n, n_placed, {2: 512, 3: 32}[n])
        R.anchor("n=%d coordinate-plane" % n, n_coord, {2: 512, 3: 64}[n])
        print("      [%s]" % el())

    # -----------------------------------------------------------------------
    hr(); print("[5.5] the full gauge moves the composite's Born shadow")
    Th = [[K8.one, K8.one], [K8.one, K8.rat(-1)]]
    HH = mat_mul(K8, H, H)
    ThH = [[K8.mul(Th[i][j], H[i][j]) for j in range(2)] for i in range(2)]
    moved = born(K8, mat_mul(K8, ThH, ThH)) != born(K8, HH)
    kills = not is_unitary(K8, ThH)
    print("      with Theta = [[1,1],[1,-1]] on the pair (H,H): the composite's "
          "Born shadow moves = %s ; unitarity is destroyed = %s" % (moved, kills))
    R.anchor("full gauge moves the shadow", moved, True)
    R.anchor("full gauge destroys unitarity", kills, True)

    # -----------------------------------------------------------------------
    hr(); print("[5.6] the boundary group and the uncompensated cut")
    scal = K8.zpow(1)
    contains = {"projective scalar": True, "compensated cut": True,
                "same-space rephasing": True}
    d = [K8.one, K8.zpow(2)]
    Th_scalar = [[scal for _ in range(2)] for _ in range(2)]
    Th_same = [[K8.mul(d[i], K8.conj(d[j])) for j in range(2)] for i in range(2)]
    bt8 = boundary_thetas(2, 8)
    in_b_scalar = tuple(1 for _ in range(4)) in bt8
    in_b_same = tuple((2 * (i == 1) - 2 * (j == 1)) % 8
                      for i in range(2) for j in range(2)) in bt8
    print("      the boundary group contains the projective scalar (%s) and the "
          "same-space rephasing (%s)" % (in_b_scalar, in_b_same))
    R.anchor("boundary contains scalar", in_b_scalar, True)
    R.anchor("boundary contains rephasing", in_b_same, True)

    # -----------------------------------------------------------------------
    hr(); print("[5.7] the single-arrow orbit theorem")
    rank_ok = 0
    mu_range = {2: set(), 3: set()}
    monomial_mu = []
    for Kf, fam, n in ((K8, F2, 2), (K12, F3fam, 3)):
        for M in fam:
            S = support(Kf, M)
            edges = bipartite(S, n)
            mu = cycle_rank(2 * n, edges)
            mu_range[n].add(mu)
            rank_ok += 1
            if all(sum(r) <= 1 for r in S):
                monomial_mu.append(mu)
    print("      cycle rank computed on all %d members; range at 2x2 = %s, at "
          "3x3 = %s" % (rank_ok, sorted(mu_range[2]), sorted(mu_range[3])))
    print("      every monomial member has cycle rank 0: %s (%d members)"
          % (set(monomial_mu) == {0}, len(monomial_mu)))
    R.anchor("members with a cycle rank", rank_ok, 159)
    R.anchor("2x2 cycle ranks", sorted(mu_range[2]), [0, 1])
    R.anchor("3x3 cycle ranks", sorted(mu_range[3]), [0, 4])
    R.anchor("monomial cycle rank zero", set(monomial_mu) == {0}, True)
    R.anchor("monomial members", len(monomial_mu), 86)

    equiv_counts = {}
    cross = 0
    for Kf, fam, n in ((K8, F2, 2), (K12, F3fam, 3)):
        eq = 0
        disagree = 0
        for U in fam:
            for V in fam:
                built, _, _ = switching_equivalent(Kf, U, V)
                if support(Kf, U) != support(Kf, V) and built:
                    cross += 1
                # holonomy test on a cycle basis
                if support(Kf, U) == support(Kf, V) and moduli(Kf, U) == moduli(Kf, V):
                    hol_agree = all(
                        haagerup(Kf, U, i, ip, j, jp) == haagerup(Kf, V, i, ip, j, jp)
                        for (i, ip) in itertools.combinations(range(n), 2)
                        for (j, jp) in itertools.combinations(range(n), 2)
                        if not (Kf.is_zero(U[i][j]) or Kf.is_zero(U[ip][jp])
                                or Kf.is_zero(U[i][jp]) or Kf.is_zero(U[ip][j])))
                else:
                    hol_agree = False
                if built:
                    eq += 1
                if built != hol_agree:
                    disagree += 1
        equiv_counts[n] = (eq, disagree, len(fam) ** 2)
        print("      n = %d : %d of %d ordered pairs are boundary-equivalent "
              "(switching built and verified entrywise); %d disagreements with "
              "the four-cycle test" % (n, eq, len(fam) ** 2, disagree))
    R.anchor("2x2 equivalent pairs", equiv_counts[2][0], 4608)
    R.anchor("3x3 equivalent pairs", equiv_counts[3][0], 567)
    R.anchor("2x2 holonomy disagreements", equiv_counts[2][1], 0)
    R.anchor("3x3 holonomy disagreements", equiv_counts[3][1], 0)
    R.anchor("cross-support equivalences", cross, 0)

    R.finish()


if __name__ == "__main__":
    main()

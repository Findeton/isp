#!/usr/bin/env python3
"""
sec2_defect_algebra.py -- regenerates every number of Section 2 of

    "Interference as the Composition Defect of Stochastic Shadows:
     Records, Gauge, and the Loop Signature of Indivisible Stochastic
     Processes"

Section 2: the three defects and the coherence law.

  2.1  the closed form / cross-term identity, symbolically at d = 2..6 and
       against the definition on every census pair;
  2.2  the two reference families F2 and F3 and the vanishing census;
  2.3  the three-defect separation (the exact rotation pair);
  2.4  the coherence law and the tree law, as formal-matrix identities;
  2.5  the content-free demonstration (six substitutes for B);
  2.6  the invariance group, including the uncompensated-cut handle;
  2.7  the doubly-centred structure, the sharp bounds, the n = 2 range;
  2.8  the two-sided annihilator (the monomial group);
  2.9  pairwise flatness does not imply n-fold flatness;
  2.10 the flat-spectrum identification at N = 2, 3, 4, 5;
  2.11 reality of the entries, reversal covariance, the odd channel.

The Born projection is carried IN THE FIELD: the modulus square of an entry
of a product need not be rational (|1 + zeta_8|^2 = 2 + sqrt 2).  Order
comparisons are made only in Q(sqrt 2), by the exact sign oracle; the two
sharp bounds are certified by polynomial identities, not by comparisons.

Exit 1 iff a computed number disagrees with the number printed in the paper.
"""

from __future__ import annotations

import itertools

from exact import (Q, Cyc, MP, born, el, head, hr, is_unitary, mat_mul,
                   to_q2, Receipts)

R = Receipts("Section 2 -- the defect algebra")


# ---------------------------------------------------------------------------
# the two reference families
# ---------------------------------------------------------------------------
def family2():
    """F2 subset U(2) over Q(zeta_8): 96 members, 32 of them monomial."""
    K = Cyc(8)
    isq2 = K.scal(K.add(K.zpow(1), K.zpow(-1)), Q(1, 2))      # 1/sqrt 2
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
            L = [[K.one, K.zero], [K.zero, K.zpow(s)]]
            Rt = [[K.one, K.zero], [K.zero, K.zpow(t)]]
            fam.append(mat_mul(K, L, mat_mul(K, H, Rt)))
    return K, fam, H


def family3():
    """F3 subset U(3) over Q(zeta_12): 63 members, 54 of them monomial."""
    K = Cyc(12)
    sqrt3 = K.add(K.zpow(1), K.zpow(-1))                      # 2 cos(pi/6)
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
            L = [[K.one, K.zero, K.zero], [K.zero, K.zpow(4 * a), K.zero],
                 [K.zero, K.zero, K.one]]
            Rt = [[K.one, K.zero, K.zero], [K.zero, K.zpow(4 * b), K.zero],
                  [K.zero, K.zero, K.one]]
            fam.append(mat_mul(K, L, mat_mul(K, F3, Rt)))
    return K, fam, F3


def msub(K, A, B):
    return [[K.sub(a, b) for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def delta(K, U2, U1):
    """Delta^B(U2,U1) = B(U2 U1) - B(U2) B(U1), as field elements."""
    return msub(K, born(K, mat_mul(K, U2, U1)),
                mat_mul(K, born(K, U2), born(K, U1)))


def is_zero_mat(K, D):
    return all(K.is_zero(v) for r in D for v in r)


def is_row_monomial(K, U):
    return all(sum(1 for x in row if not K.is_zero(x)) <= 1 for row in U)


def is_col_monomial(K, U):
    n = len(U)
    return all(sum(1 for i in range(n) if not K.is_zero(U[i][j])) <= 1
               for j in range(len(U[0])))


# ---------------------------------------------------------------------------
def main():
    head("SECTION 2 -- THE THREE DEFECTS AND THE COHERENCE LAW")

    K2, F2, H = family2()
    K3, F3fam, F3 = family3()
    print("[2.0] reference families: |F2| = %d, |F3| = %d" % (len(F2), len(F3fam)))
    R.anchor("|F2|", len(F2), 96)
    R.anchor("|F3|", len(F3fam), 63)
    R.anchor("F2 unitary", sum(1 for M in F2 if is_unitary(K2, M)), 96)
    R.anchor("F3 unitary", sum(1 for M in F3fam if is_unitary(K3, M)), 63)
    R.anchor("F2 monomial", sum(1 for M in F2 if is_row_monomial(K2, M)), 32)
    R.anchor("F3 monomial", sum(1 for M in F3fam if is_row_monomial(K3, M)), 54)
    # every family entry has a rational, non-negative modulus square
    badmod = 0
    for K, fam in ((K2, F2), (K3, F3fam)):
        for M in fam:
            for row in M:
                for x in row:
                    t = K.normsq(x)
                    q = K.to_rat(t)
                    if q is None or q < 0:
                        badmod += 1
    R.anchor("family moduli non-negative rational", badmod, 0)

    # -----------------------------------------------------------------------
    hr(); print("[2.1] the closed form, symbolically at d = 2..6")
    ok = True
    for d in range(2, 7):
        x = [MP.var("x%d" % k) for k in range(d)]
        y = [MP.var("y%d" % k) for k in range(d)]
        sx = MP.const(0); sy = MP.const(0)
        for k in range(d):
            sx = sx + x[k]; sy = sy + y[k]
        lhs = sx * sx + sy * sy
        for k in range(d):
            lhs = lhs - (x[k] * x[k] + y[k] * y[k])
        rhs = MP.const(0)
        for k in range(d):
            for l in range(k + 1, d):
                rhs = rhs + MP.const(2) * (x[k] * x[l] + y[k] * y[l])
        ok = ok and (lhs - rhs).is_zero()
    print("      |sum w|^2 - sum |w|^2 = 2 sum_{k<l} Re(w_k conj w_l), d = 2..6 : %s"
          % ("identity" if ok else "FAILS"))
    R.anchor("closed form d=2..6", ok, True)

    hr(); print("[2.1b] the identity against the definition, on every census pair")
    mism = 0
    checked = 0
    for K, fam in ((K2, F2), (K3, F3fam)):
        n = len(fam[0])
        for U2 in fam:
            for U1 in fam:
                D = delta(K, U2, U1)
                for i in range(n):
                    for j in range(n):
                        wk = [K.mul(U2[i][k], U1[k][j]) for k in range(n)]
                        acc = K.zero
                        for k in range(n):
                            for l in range(k + 1, n):
                                acc = K.add(acc, K.scal(
                                    K.re(K.mul(wk[k], K.conj(wk[l]))), 2))
                        checked += 1
                        if acc != D[i][j]:
                            mism += 1
        print("      %dx%d done  [%s]" % (n, n, el()))
    print("      entries checked = %d, mismatches = %d" % (checked, mism))
    R.anchor("cross-term entries", checked, 72585)
    R.anchor("cross-term mismatches", mism, 0)

    # -----------------------------------------------------------------------
    hr(); print("[2.2] the vanishing census")
    census = {}
    d00_vals_2x2 = []
    trace_pm = {1: 0, -1: 0}
    asym_nonzero = 0
    for tag, K, fam, n in (("2x2", K2, F2, 2), ("3x3", K3, F3fam, 3)):
        c = {"cond0": 0, "condN": 0, "free0": 0, "freeN": 0}
        for U2 in fam:
            rm = is_row_monomial(K, U2)
            for U1 in fam:
                cond = rm or is_col_monomial(K, U1)
                D = delta(K, U2, U1)
                z = is_zero_mat(K, D)
                c["cond0" if z else "condN"] += 1 if cond else 0
                if not cond:
                    c["free0" if z else "freeN"] += 1
                A = [[K.scal(K.sub(D[i][j], D[j][i]), Q(1, 2)) for j in range(n)]
                     for i in range(n)]
                if not is_zero_mat(K, A):
                    asym_nonzero += 1
                tr = K.zero
                for i in range(n):
                    tr = K.add(tr, D[i][i])
                if tr == K.rat(1):
                    trace_pm[1] += 1
                if tr == K.rat(-1):
                    trace_pm[-1] += 1
                if n == 2:
                    d00_vals_2x2.append(to_q2(K, D[0][0]))
        census[tag] = c
        print("      %s : cond & zero = %d, cond & nonzero = %d, "
              "free & zero = %d, free & nonzero = %d"
              % (tag, c["cond0"], c["condN"], c["free0"], c["freeN"]))
    R.anchor("2x2 cond&zero", census["2x2"]["cond0"], 5120)
    R.anchor("2x2 cond&nonzero", census["2x2"]["condN"], 0)
    R.anchor("2x2 free&zero", census["2x2"]["free0"], 1024)
    R.anchor("2x2 free&nonzero", census["2x2"]["freeN"], 3072)
    R.anchor("3x3 cond&zero", census["3x3"]["cond0"], 3888)
    R.anchor("3x3 cond&nonzero", census["3x3"]["condN"], 0)
    R.anchor("3x3 free&zero", census["3x3"]["free0"], 54)
    R.anchor("3x3 free&nonzero", census["3x3"]["freeN"], 27)

    DHH = delta(K2, H, H)
    R.anchor("Delta(H,H)", [[str(to_q2(K2, v)) for v in r] for r in DHH],
             [["1/2", "-1/2"], ["-1/2", "1/2"]])
    isq2 = K2.scal(K2.add(K2.zpow(1), K2.zpow(-1)), Q(1, 2))
    iu = K2.mul(K2.zpow(2), isq2)
    W = [[isq2, iu], [iu, isq2]]
    R.anchor("W unitary", is_unitary(K2, W), True)
    R.anchor("Delta(H,W) = 0", is_zero_mat(K2, delta(K2, H, W)), True)
    print("      Delta(H,H) = [[1/2,-1/2],[-1/2,1/2]] ; Delta(H,W) = 0 with "
          "H, W both fully unbiased")

    # -----------------------------------------------------------------------
    hr(); print("[2.3] the three-defect separation")
    c, s = MP.var("c"), MP.var("s")
    unit = c * c + s * s - MP.const(1)
    lhs00 = c * c
    rhs00 = (MP.const(1) + (MP.const(2) * c * c - MP.const(1))) * MP.const(Q(1, 2))
    ok_S = (lhs00 - rhs00).is_zero()
    lhs01 = s * s
    rhs01 = (MP.const(1) - (MP.const(2) * c * c - MP.const(1))) * MP.const(Q(1, 2))
    ok_S = ok_S and ((lhs01 - rhs01) - unit).is_zero()
    cc, dd = MP.var("cc"), MP.var("dd")

    def Ssym(t):
        h = MP.const(Q(1, 2))
        return [[h * (MP.const(1) + t), h * (MP.const(1) - t)],
                [h * (MP.const(1) - t), h * (MP.const(1) + t)]]
    Pp = [[Ssym(cc)[i][0] * Ssym(dd)[0][j] + Ssym(cc)[i][1] * Ssym(dd)[1][j]
           for j in range(2)] for i in range(2)]
    Tgt = Ssym(cc * dd)
    ok_SS = all((Pp[i][j] - Tgt[i][j]).is_zero() for i in range(2) for j in range(2))
    print("      B(R(theta)) = S(cos 2 theta) modulo c^2 + s^2 = 1 : %s" % ok_S)
    print("      S(c) S(d) = S(cd) as a polynomial identity over Q : %s" % ok_SS)
    R.anchor("B(R)=S(cos2t)", ok_S, True)
    R.anchor("S(c)S(d)=S(cd)", ok_SS, True)

    c1 = Q(2) * Q(24, 25) ** 2 - 1
    c2 = Q(2) * Q(4, 5) ** 2 - 1
    s1 = Q(2) * Q(24, 25) * Q(7, 25)
    s2 = Q(2) * Q(4, 5) * Q(3, 5)
    ctot = c1 * c2 - s1 * s2
    d00 = (ctot - c1 * c2) / 2
    kdiv = ctot / c1
    print("      c1 = %s, c2 = %s, c_tot = %s" % (c1, c2, ctot))
    print("      Delta_00 = %s ; the divisor is K = S(%s)" % (d00, kdiv))
    R.anchor("c1", str(c1), "527/625")
    R.anchor("c2", str(c2), "7/25")
    R.anchor("c_tot", str(ctot), "-7/25")
    R.anchor("Delta_00 rotation", str(d00), "-4032/15625")
    R.anchor("divisor parameter", str(kdiv), "-175/527")

    def S(t):
        return [[(1 + t) / 2, (1 - t) / 2], [(1 - t) / 2, (1 + t) / 2]]

    def rmul(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)]
                for i in range(2)]
    Kdiv = S(kdiv)
    R.anchor("K B(U1) = B(U2U1)", rmul(Kdiv, S(c1)) == S(ctot), True)
    R.anchor("K stochastic", all(v >= 0 for r in Kdiv for v in r)
             and all(sum(Kdiv[i][j] for i in range(2)) == 1 for j in range(2)), True)
    R.anchor("K != B(U2)", Kdiv != S(c2), True)

    tested = 0
    bad = 0
    for p in range(1, 40):
        for q_ in range(1, 40):
            den = p * p + q_ * q_
            a = Q(p * p - q_ * q_, den)
            if a == 0:
                continue
            for r_ in range(-12, 13):
                cT = Q(r_, 13)
                if abs(cT) > abs(a):
                    continue
                tested += 1
                M = S(cT / a)
                if not (all(v >= 0 for row in M for v in row)
                        and rmul(M, S(a)) == S(cT)):
                    bad += 1
    print("      the rotation divisor construction: %d exact (c1, c_tot) pairs, "
          "%d failures" % (tested, bad))
    R.anchor("rotation divisor pairs", tested, 22062)
    R.anchor("rotation divisor failures", bad, 0)

    # -----------------------------------------------------------------------
    hr(); print("[2.4] the coherence law and the tree law, formal matrices")

    def formal(sym, d):
        return [[MP.var("%s_%d_%d" % (sym, i, j)) for j in range(d)] for i in range(d)]

    def fmul(A, B, d):
        return [[sum((A[i][k] * B[k][j] for k in range(d)), MP.const(0))
                 for j in range(d)] for i in range(d)]

    def fsub(A, B, d):
        return [[A[i][j] - B[i][j] for j in range(d)] for i in range(d)]

    def fadd(A, B, d):
        return [[A[i][j] + B[i][j] for j in range(d)] for i in range(d)]

    okc = True
    for d in (2, 3):
        B1, B2, B3 = formal("b1", d), formal("b2", d), formal("b3", d)
        B21, B32, B321 = formal("b21", d), formal("b32", d), formal("b321", d)
        D21 = fsub(B21, fmul(B2, B1, d), d)
        D32 = fsub(B32, fmul(B3, B2, d), d)
        D3_21 = fsub(B321, fmul(B3, B21, d), d)
        D32_1 = fsub(B321, fmul(B32, B1, d), d)
        L = fadd(D32_1, fmul(D32, B1, d), d)
        Rr = fadd(D3_21, fmul(B3, D21, d), d)
        common = fsub(B321, fmul(B3, fmul(B2, B1, d), d), d)
        for i in range(d):
            for j in range(d):
                okc = okc and (L[i][j] - Rr[i][j]).is_zero()
                okc = okc and (L[i][j] - common[i][j]).is_zero()
    print("      coherence law with 24 independent variables at d = 2 and 54 at "
          "d = 3 : %s" % ("identity" if okc else "FAILS"))
    R.anchor("coherence law formal", okc, True)

    def bracketings(seq):
        if len(seq) == 1:
            yield seq[0]
            return
        for k in range(1, len(seq)):
            for L_ in bracketings(seq[:k]):
                for Rr_ in bracketings(seq[k:]):
                    yield (L_, Rr_)

    def leaves(t):
        return leaves(t[0]) + leaves(t[1]) if isinstance(t, tuple) else (t,)

    d = 2
    Bvar = {}

    def Bof(seg):
        if seg not in Bvar:
            Bvar[seg] = formal("B%s" % ("_".join(map(str, seg))), d)
        return Bvar[seg]

    def leafprod(seg):
        P = Bof((seg[0],))
        for k in seg[1:]:
            P = fmul(P, Bof((k,)), d)
        return P

    def Phi(t):
        if not isinstance(t, tuple):
            return [[MP.const(0)] * d for _ in range(d)]
        lv, rv = leaves(t[0]), leaves(t[1])
        DL = fsub(Bof(lv + rv), fmul(Bof(lv), Bof(rv), d), d)
        return fadd(fadd(DL, fmul(Phi(t[0]), Bof(rv), d), d),
                    fmul(leafprod(lv), Phi(t[1]), d), d)

    tree_ok = True
    tree_counts = []
    for n in range(2, 6):
        seq = tuple(range(n))
        prod = Bof((0,))
        for k in range(1, n):
            prod = fmul(prod, Bof((k,)), d)
        target = fsub(Bof(seq), prod, d)
        cnt = 0
        for t in bracketings(seq):
            cnt += 1
            Ph = Phi(t)
            for i in range(d):
                for j in range(d):
                    tree_ok = tree_ok and (Ph[i][j] - target[i][j]).is_zero()
        tree_counts.append(cnt)
    print("      tree law at n = 2..5, %s bracketings : %s"
          % (tree_counts, "identity" if tree_ok else "FAILS"))
    R.anchor("tree law", tree_ok, True)
    R.anchor("bracketing counts", tree_counts, [1, 2, 5, 14])

    # -----------------------------------------------------------------------
    hr(); print("[2.5] the law is content-free about the Born projection")
    d = 2

    def m_id(M):
        return M

    def m_transpose(M):
        return [[M[j][i] for j in range(d)] for i in range(d)]

    def m_affine(M):
        Tt = m_transpose(M)
        return [[M[i][j] + MP.const(2) * Tt[i][j]
                 + (MP.const(3) if i == j else MP.const(0))
                 for j in range(d)] for i in range(d)]

    def m_const(M):
        return [[MP.const(7) if (i + j) % 2 == 0 else MP.const(-1)
                 for j in range(d)] for i in range(d)]

    def m_double(M):
        return [[MP.const(2) * M[i][j] for j in range(d)] for i in range(d)]

    def m_zero(M):
        return [[MP.const(0) for _ in range(d)] for _ in range(d)]

    A1, A2, A3 = formal("a1", d), formal("a2", d), formal("a3", d)
    A21, A32 = fmul(A2, A1, d), fmul(A3, A2, d)
    A321 = fmul(A3, A21, d)
    subs = {}
    for name, f in (("identity", m_id), ("transpose", m_transpose),
                    ("M + 2M^T + 3I", m_affine),
                    ("constant (argument ignored)", m_const),
                    ("doubling", m_double), ("zero map", m_zero)):
        f1, f2, f3 = f(A1), f(A2), f(A3)
        f21, f32, f321 = f(A21), f(A32), f(A321)
        L = fadd(fsub(f321, fmul(f32, f1, d), d),
                 fmul(fsub(f32, fmul(f3, f2, d), d), f1, d), d)
        Rr = fadd(fsub(f321, fmul(f3, f21, d), d),
                  fmul(f3, fsub(f21, fmul(f2, f1, d), d), d), d)
        subs[name] = all((L[i][j] - Rr[i][j]).is_zero()
                         for i in range(d) for j in range(d))
        print("      substitute %-30s : %s"
              % (name, "law holds" if subs[name] else "law FAILS"))
    R.anchor("six substitutes hold", all(subs.values()) and len(subs) == 6, True)

    # -----------------------------------------------------------------------
    hr(); print("[2.6] the invariance group")
    stride2 = F2[::4]
    stride3 = F3fam[::3]
    R.anchor("stride sizes", (len(stride2), len(stride3)), (24, 21))
    counts = dict(normalized=0, outer=0, cut=0, equiv=0, rev=0,
                  unc_moved=0, unc_total=0)
    for K, fam, stride, n in ((K2, F2, stride2, 2), (K3, F3fam, stride3, 3)):
        I = [[K.one if i == j else K.zero for j in range(n)] for i in range(n)]
        for U in stride:
            if is_zero_mat(K, delta(K, I, U)):
                counts["normalized"] += 1
            if is_zero_mat(K, delta(K, U, I)):
                counts["normalized"] += 1
        Dg = [[K.zpow(K.n // 4 * (i + 1)) if i == j else K.zero for j in range(n)]
              for i in range(n)]
        Dgi = [[K.inv(Dg[i][j]) if i == j else K.zero for j in range(n)]
               for i in range(n)]
        sh = list(range(1, n)) + [0]
        for U2 in stride:
            for U1 in stride:
                base = delta(K, U2, U1)
                if delta(K, mat_mul(K, Dg, U2), mat_mul(K, U1, Dg)) == base:
                    counts["outer"] += 1
                if delta(K, mat_mul(K, U2, Dg), mat_mul(K, Dgi, U1)) == base:
                    counts["cut"] += 1
                Pm = [[K.one if j == sh[i] else K.zero for j in range(n)]
                      for i in range(n)]
                shinv = [0] * n
                for i_ in range(n):
                    shinv[sh[i_]] = i_
                lhs = delta(K, mat_mul(K, Pm, U2), mat_mul(K, U1, Pm))
                rhs = [[base[sh[i]][shinv[j]] for j in range(n)] for i in range(n)]
                if lhs == rhs:
                    counts["equiv"] += 1

                def tr(M):
                    return [[M[j][i] for j in range(n)] for i in range(n)]
                if tr(base) == delta(K, tr(U1), tr(U2)):
                    counts["rev"] += 1
                if n == 2:
                    counts["unc_total"] += 1
                    if delta(K, mat_mul(K, U2, Dg), U1) != base:
                        counts["unc_moved"] += 1
    print("      normalized %d/%d ; outer torus %d ; compensated cut %d ; "
          "equivariance %d ; reversal %d"
          % (counts["normalized"], 2 * (len(stride2) + len(stride3)),
             counts["outer"], counts["cut"], counts["equiv"], counts["rev"]))
    print("      the uncompensated cut insertion MOVES the defect on %d of %d "
          "declared 2x2 stride pairs" % (counts["unc_moved"], counts["unc_total"]))
    npairs = len(stride2) ** 2 + len(stride3) ** 2
    R.anchor("normalized", counts["normalized"], 90)
    R.anchor("outer torus", counts["outer"], npairs)
    R.anchor("compensated cut", counts["cut"], npairs)
    R.anchor("equivariance", counts["equiv"], npairs)
    R.anchor("reversal covariance", counts["rev"], npairs)
    R.anchor("uncompensated moved", counts["unc_moved"], 192)
    R.anchor("uncompensated total", counts["unc_total"], 576)

    # -----------------------------------------------------------------------
    hr(); print("[2.7] doubly-centred structure, the two certificates, the range")
    viol_center = 0
    cert_lo = 0
    cert_hi = 0
    entries = 0
    for K, fam, n in ((K2, F2, 2), (K3, F3fam, 3)):
        for U2 in fam:
            b2 = born(K, U2)
            for U1 in fam:
                b1 = born(K, U1)
                sm = mat_mul(K, b2, b1)
                D = delta(K, U2, U1)
                for i in range(n):
                    acc = K.zero
                    for j in range(n):
                        acc = K.add(acc, D[i][j])
                    if not K.is_zero(acc):
                        viol_center += 1
                for j in range(n):
                    acc = K.zero
                    for i in range(n):
                        acc = K.add(acc, D[i][j])
                    if not K.is_zero(acc):
                        viol_center += 1
                for i in range(n):
                    for j in range(n):
                        entries += 1
                        wk = [K.mul(U2[i][k], U1[k][j]) for k in range(n)]
                        tot = K.zero
                        for x in wk:
                            tot = K.add(tot, x)
                        # certificate 1: Delta + s = |sum_k w_k|^2
                        if K.add(D[i][j], sm[i][j]) == K.normsq(tot):
                            cert_lo += 1
                        # certificate 2: n s - (Delta + s) = sum_{k<l} |w_k - w_l|^2
                        acc = K.zero
                        for a in range(n):
                            for b in range(a + 1, n):
                                acc = K.add(acc, K.normsq(K.sub(wk[a], wk[b])))
                        if K.sub(K.scal(sm[i][j], n),
                                 K.add(D[i][j], sm[i][j])) == acc:
                            cert_hi += 1
    print("      doubly-centred violations = %d over %d entries" % (viol_center, entries))
    print("      lower certificate holds %d/%d ; upper certificate holds %d/%d"
          % (cert_lo, entries, cert_hi, entries))
    R.anchor("doubly-centred violations", viol_center, 0)
    R.anchor("census entries", entries, 72585)
    R.anchor("lower certificate", cert_lo, 72585)
    R.anchor("upper certificate", cert_hi, 72585)

    lo = min(d00_vals_2x2)
    hi = max(d00_vals_2x2)
    print("      exact range of Delta_00 over the 9216 2x2 pairs: [%s, %s]" % (lo, hi))
    R.anchor("n=2 range low", str(lo), "-1/2")
    R.anchor("n=2 range high", str(hi), "1/2")
    Hm = [[K2.one, K2.zero], [K2.zero, K2.rat(-1)]]
    R.anchor("Delta(H, diag(1,-1)H)_00",
             str(to_q2(K2, delta(K2, H, mat_mul(K2, Hm, H))[0][0])), "-1/2")
    R.anchor("Delta(H,H)_00", str(to_q2(K2, DHH[0][0])), "1/2")

    # -----------------------------------------------------------------------
    hr(); print("[2.8] the two-sided annihilator")
    probe_stats = {}
    for K, fam, n in ((K2, F2, 2), (K3, F3fam, 3)):
        probes = []
        for (k, l) in itertools.combinations(range(n), 2):
            for m in range(2):
                V = [[K.one if i == j else K.zero for j in range(n)] for i in range(n)]
                V[k][k] = K.rat(Q(3, 5)); V[k][l] = K.rat(Q(-4, 5))
                V[l][k] = K.rat(Q(4, 5)); V[l][l] = K.rat(Q(3, 5))
                Dm = [[K.one if i == j else K.zero for j in range(n)] for i in range(n)]
                Dm[k][k] = K.zpow(K.n // 4) if m else K.one
                probes.append(mat_mul(K, Dm, V))
        assert all(is_unitary(K, P) for P in probes)
        # the right-slot probes are the transposes: the reversal covariance
        # Delta(U2,U1)^T = Delta(U1^T, U2^T) turns the left-slot argument into
        # the right-slot one.
        probesT = [[[P[j][i] for j in range(n)] for i in range(n)] for P in probes]
        nL = uL = nR = uR = 0
        for U in fam:
            if not is_row_monomial(K, U):
                nL += 1
                if all(is_zero_mat(K, delta(K, U, P)) for P in probes):
                    uL += 1
            if not is_col_monomial(K, U):
                nR += 1
                if all(is_zero_mat(K, delta(K, P, U)) for P in probesT):
                    uR += 1
        probe_stats[n] = (len(probes), nL, uL, nR, uR)
        print("      n = %d : %d probes ; %d non-row-monomial, %d unseparated ; "
              "%d non-column-monomial, %d unseparated" % (n, len(probes), nL, uL, nR, uR))
    R.anchor("2x2 probes", probe_stats[2][0], 2)
    R.anchor("3x3 probes", probe_stats[3][0], 6)
    R.anchor("2x2 non-row-monomial", probe_stats[2][1], 64)
    R.anchor("3x3 non-row-monomial", probe_stats[3][1], 9)
    R.anchor("unseparated left", probe_stats[2][2] + probe_stats[3][2], 0)
    R.anchor("unseparated right", probe_stats[2][4] + probe_stats[3][4], 0)

    # -----------------------------------------------------------------------
    hr(); print("[2.9] pairwise flatness does not imply n-fold flatness")
    found = None
    K, fam = K2, F2
    flat_pairs = {}
    for i2 in range(len(fam)):
        for i1 in range(len(fam)):
            if is_zero_mat(K, delta(K, fam[i2], fam[i1])):
                flat_pairs.setdefault(i2, []).append(i1)
    for i2, i1s in sorted(flat_pairs.items()):
        if found:
            break
        for i1 in i1s:
            if found:
                break
            for i0 in flat_pairs.get(i1, []):
                A = mat_mul(K, fam[i2], mat_mul(K, fam[i1], fam[i0]))
                lhs = born(K, A)
                rhs = mat_mul(K, born(K, fam[i2]),
                              mat_mul(K, born(K, fam[i1]), born(K, fam[i0])))
                if lhs != rhs:
                    found = (i2, i1, i0)
                    break
    print("      three-step chain, both cuts flat, three-fold defect nonzero: "
          "family indices %s" % (found,))
    R.anchor("3-chain witness", found is not None, True)

    # -----------------------------------------------------------------------
    hr(); print("[2.10] the flat-spectrum identification")
    flat_counts = {}
    for N, nfield, mgroup in ((2, 8, 8), (3, 12, 6), (4, 8, 8), (5, 5, 5)):
        K = Cyc(nfield)
        try:
            sN = K.sqrt_of(N)
        except ArithmeticError:
            g = K.zero
            for a in range(N):
                g = K.add(g, K.zpow((K.n // N) * ((a * a) % N)))
            assert K.mul(g, g) == K.rat(N)
            sN = g
        isN = K.inv(sN)
        FN = [[K.mul(isN, K.zpow((K.n // N) * ((j * k) % N))) for k in range(N)]
              for j in range(N)]
        assert is_unitary(K, FN), "F_%d unitary" % N
        total = flat = agree = 0
        for eps in itertools.product(range(mgroup), repeat=N - 1):
            e = [K.one] + [K.zpow((K.n // mgroup) * t) for t in eps]
            total += 1
            E = [[e[i] if i == j else K.zero for j in range(N)] for i in range(N)]
            bm = born(K, mat_mul(K, FN, mat_mul(K, E, FN)))
            isflat = all(v == K.rat(Q(1, N)) for r in bm for v in r)
            dft_flat = True
            for sft in range(N):
                acc = K.zero
                for m in range(N):
                    acc = K.add(acc, K.mul(e[m], K.zpow((K.n // N) * ((m * sft) % N))))
                if K.normsq(acc) != K.rat(N):
                    dft_flat = False
                    break
            auto = True
            for lag in range(1, N):
                acc = K.zero
                for m in range(N):
                    acc = K.add(acc, K.mul(e[m], K.conj(e[(m + lag) % N])))
                if not K.is_zero(acc):
                    auto = False
                    break
            flat += 1 if isflat else 0
            agree += 1 if (isflat == dft_flat == auto) else 0
        flat_counts[N] = (total, flat, agree)
        print("      N = %d : %d interleaving diagonals, %d with a vanishing defect, "
              "%d/%d three-way agreements" % (N, total, flat, agree, total))
    R.anchor("N=2 (total,flat)", flat_counts[2][:2], (8, 2))
    R.anchor("N=3 (total,flat)", flat_counts[3][:2], (36, 6))
    R.anchor("N=4 (total,flat)", flat_counts[4][:2], (512, 16))
    R.anchor("N=5 (total,flat)", flat_counts[5][:2], (625, 20))
    R.anchor("flat-spectrum agreement",
             all(flat_counts[N][2] == flat_counts[N][0] for N in (2, 3, 4, 5)), True)

    K = K2
    bad = tot = 0
    for s_, t_, u_, v_ in itertools.product(range(8), repeat=4):
        tot += 1
        U2 = mat_mul(K, [[K.one, K.zero], [K.zero, K.zpow(s_)]],
                     mat_mul(K, H, [[K.one, K.zero], [K.zero, K.zpow(t_)]]))
        U1 = mat_mul(K, [[K.one, K.zero], [K.zero, K.zpow(u_)]],
                     mat_mul(K, H, [[K.one, K.zero], [K.zero, K.zpow(v_)]]))
        if is_zero_mat(K, delta(K, U2, U1)) != (((t_ + u_) % 8) in (2, 6)):
            bad += 1
    print("      N = 2 closed form  t + u = +-2 (mod 8) : %d quadruples, %d mismatches"
          % (tot, bad))
    R.anchor("N=2 closed form quadruples", tot, 4096)
    R.anchor("N=2 closed form mismatches", bad, 0)

    K = K3
    sqrt3 = K.add(K.zpow(1), K.zpow(-1))
    isq3 = K.inv(sqrt3)
    F3m = [[K.mul(isq3, K.zpow(4 * ((j * k) % 3))) for k in range(3)] for j in range(3)]
    bad3 = tot3 = 0
    for a2, b2, a1, b1 in itertools.product(range(3), repeat=4):
        tot3 += 1

        def Dm(m):
            return [[K.one, K.zero, K.zero],
                    [K.zero, K.zpow(4 * m), K.zero],
                    [K.zero, K.zero, K.one]]
        U2 = mat_mul(K, Dm(a2), mat_mul(K, F3m, Dm(b2)))
        U1 = mat_mul(K, Dm(a1), mat_mul(K, F3m, Dm(b1)))
        if is_zero_mat(K, delta(K, U2, U1)) != (((b2 + a1) % 3) != 0):
            bad3 += 1
    print("      N = 3 closed form  b2 + a1 != 0 (mod 3) : %d quadruples, %d mismatches"
          % (tot3, bad3))
    R.anchor("N=3 closed form quadruples", tot3, 81)
    R.anchor("N=3 closed form mismatches", bad3, 0)

    # -----------------------------------------------------------------------
    hr(); print("[2.11] reality, reversal covariance, the odd channel")
    print("      antisymmetric part nonzero on %d of the 13185 census pairs"
          % asym_nonzero)
    print("      trace of the defect = +1 on %d pairs and = -1 on %d pairs"
          % (trace_pm[1], trace_pm[-1]))
    R.anchor("census antisym nonzero", asym_nonzero, 0)
    R.anchor("trace +1 count", trace_pm[1], 512)
    R.anchor("trace -1 count", trace_pm[-1], 512)

    K = K3

    def rot(k, l):
        M = [[K.one if i == j else K.zero for j in range(3)] for i in range(3)]
        M[k][k] = K.rat(Q(3, 5)); M[k][l] = K.rat(Q(-4, 5))
        M[l][k] = K.rat(Q(4, 5)); M[l][l] = K.rat(Q(3, 5))
        return M
    Wset = [rot(0, 1), rot(1, 2), mat_mul(K, rot(0, 1), F3m),
            mat_mul(K, rot(1, 2), F3m)]
    assert all(is_unitary(K, M) for M in Wset)
    infam = sum(1 for M in Wset if M in F3fam)
    odd_nonzero = odd_flip = 0
    first = None
    for U2 in Wset:
        for U1 in Wset:
            D = delta(K, U2, U1)
            A = [[K.scal(K.sub(D[i][j], D[j][i]), Q(1, 2)) for j in range(3)]
                 for i in range(3)]
            if not is_zero_mat(K, A):
                odd_nonzero += 1
                if first is None:
                    first = sorted({str(K.to_rat(v)) for r in A for v in r
                                    if not K.is_zero(v)})

            def tr(M):
                return [[M[j][i] for j in range(3)] for i in range(3)]
            Dr = delta(K, tr(U1), tr(U2))
            Ar = [[K.scal(K.sub(Dr[i][j], Dr[j][i]), Q(1, 2)) for j in range(3)]
                  for i in range(3)]
            if all(Ar[i][j] == K.neg(A[i][j]) for i in range(3) for j in range(3)):
                odd_flip += 1
    print("      the odd-channel witness set: 4 members, %d of them in the "
          "reference family" % infam)
    print("      antisymmetric part nonzero on %d of 16 ordered pairs; "
          "reversal-odd on %d of 16" % (odd_nonzero, odd_flip))
    print("      its nonzero antisymmetric values: %s" % first)
    R.anchor("odd witness in family", infam, 0)
    R.anchor("odd channel nonzero pairs", odd_nonzero, 12)
    R.anchor("odd channel flips", odd_flip, 16)
    R.anchor("odd channel values", first, ["-14/625", "14/625"])

    R.finish()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
model_composite.py -- the composite two-measurement model of the paper,
built from scratch in exact arithmetic and shared by Sections 4, 8 and 9.

The model is a finite indivisible-stochastic-process model of a bipartite
two-measurement experiment, in the sense of the framework the paper extends:
a fixed configuration space, definite configurations at all times, and a
transition matrix that is the Born shadow of a real orthogonal propagator.

  configuration space   C = {(qA, qB, pA, pB)},  qX in {0,1},
                        pX in {r, +, -},  |C| = 36
  index                 i = ((qA*2 + qB)*3 + pA)*3 + pB
  initial configuration j0 = 0, i.e. (0, 0, r, r)

  preparation           U_prep = V (x) I_9, with V real orthogonal carrying
                        e_0 to the singlet vector (0, 1/sqrt2, -1/sqrt2, 0)
                        on (qA qB) = (00, 01, 10, 11)
  local measurement     U_X(theta) = sum_s Pi^theta_s (x) Sh^{n(s)} acting on
                        (q_X, p_X) and trivially on the other pair, where
                        Pi^theta_+- are the rank-one projectors onto
                        (cos(theta/2), sin(theta/2)) and (-sin(theta/2),
                        cos(theta/2)), Sh is the 3-cycle r -> + -> - -> r,
                        and n(+) = 1, n(-) = 2.

  frames                F1 = (prep, A, B) and F2 = (prep, B, A): the same two
                        local events in the two orders, on one configuration
                        space.  The two local operators commute.

Every entry lies in the totally real quartic field Q(cos pi/8), so the
arithmetic is exact and equality of field elements is equality of tuples.
"""

from __future__ import annotations

from exact import Q, cos_pi8_field, q8_to_q2

NQ = 2
NP = 3
NC = 36

SETTINGS = {                     # (label, a, b) with angles as multiples of pi/8
    "SP-A": (0, 2),              # (0, pi/4)      = (0 deg, 45 deg)
    "SP-B": (0, 6),              # (0, 3pi/4)     = (0 deg, 135 deg)
    "SP-C": (4, 2),              # (pi/2, pi/4)   = (90 deg, 45 deg)
    "SP-D": (4, 6),              # (pi/2, 3pi/4)  = (90 deg, 135 deg)
    "SP-E": (0, 0),              # (0, 0)
    "SP-F": (2, 2),              # (pi/4, pi/4)   = (45 deg, 45 deg)
}
SETTING_ORDER = ["SP-A", "SP-B", "SP-C", "SP-D", "SP-E", "SP-F"]
DEG = {0: "0", 2: "45", 4: "90", 6: "135"}


def idx(qa, qb, pa, pb):
    return ((qa * 2 + qb) * 3 + pa) * 3 + pb


def unidx(i):
    pb = i % 3
    pa = (i // 3) % 3
    qb = (i // 9) % 2
    qa = i // 18
    return qa, qb, pa, pb


class Composite:
    def __init__(self):
        K = cos_pi8_field()
        self.K = K
        x = K.xpow(1)
        # cos(k pi/8) and sin(k pi/8) as polynomials in x = cos(pi/8):
        #   cos(0)=1, cos(pi/8)=x, cos(pi/4)=2x^2-1, cos(3pi/8)=4x^3-3x
        self.cos = {0: K.rat(1), 1: K.poly([0, 1]), 2: K.poly([-1, 0, 2]),
                    3: K.poly([0, -3, 0, 4]), 4: K.rat(0)}
        self.sin = {k: self.cos[4 - k] for k in range(5)}
        # certificate: cos^2 + sin^2 = 1 at every half-angle used
        for k in range(5):
            assert K.add(K.mul(self.cos[k], self.cos[k]),
                         K.mul(self.sin[k], self.sin[k])) == K.one, k

    # -- sparse matrices as dict[(row, col)] -> field element ---------------
    def sp_mul(self, A, B):
        K = self.K
        bycol = {}
        for (i, k), v in A.items():
            bycol.setdefault(k, []).append((i, v))
        out = {}
        for (k, j), v in B.items():
            for (i, u) in bycol.get(k, ()):
                t = K.mul(u, v)
                if not K.is_zero(t):
                    key = (i, j)
                    s = K.add(out.get(key, K.zero), t)
                    if K.is_zero(s):
                        out.pop(key, None)
                    else:
                        out[key] = s
        return out

    def sp_dense(self, A, n=NC):
        K = self.K
        M = [[K.zero] * n for _ in range(n)]
        for (i, j), v in A.items():
            M[i][j] = v
        return M

    def is_orthogonal(self, A, n=NC):
        K = self.K
        cols = {}
        for (i, j), v in A.items():
            cols.setdefault(j, []).append((i, v))
        for j1 in range(n):
            for j2 in range(j1, n):
                acc = K.zero
                d1 = dict(cols.get(j1, ()))
                for (i, v) in cols.get(j2, ()):
                    if i in d1:
                        acc = K.add(acc, K.mul(d1[i], v))
                tgt = K.one if j1 == j2 else K.zero
                if acc != tgt:
                    return False
        return True

    # -- the operators ------------------------------------------------------
    def U_prep(self):
        K = self.K
        r2 = self.cos[2]                        # 1/sqrt 2 = cos(pi/4)
        V = [[K.zero, K.zero, K.one, K.zero],
             [r2, r2, K.zero, K.zero],
             [K.neg(r2), r2, K.zero, K.zero],
             [K.zero, K.zero, K.zero, K.one]]
        out = {}
        for a in range(4):
            for b in range(4):
                if K.is_zero(V[a][b]):
                    continue
                qa1, qb1 = a // 2, a % 2
                qa0, qb0 = b // 2, b % 2
                for pa in range(3):
                    for pb in range(3):
                        out[(idx(qa1, qb1, pa, pb), idx(qa0, qb0, pa, pb))] = V[a][b]
        return out

    def _proj(self, half):
        """the two rank-one projectors at half-angle `half` * pi/8."""
        K = self.K
        c, s = self.cos[half], self.sin[half]
        Pp = [[K.mul(c, c), K.mul(c, s)], [K.mul(s, c), K.mul(s, s)]]
        Pm = [[K.mul(s, s), K.neg(K.mul(s, c))],
              [K.neg(K.mul(c, s)), K.mul(c, c)]]
        return Pp, Pm

    def U_local(self, wing, angle8):
        """U_X(theta) with theta = angle8 * pi/8, wing in {'A','B'}."""
        K = self.K
        assert angle8 % 2 == 0
        Pp, Pm = self._proj(angle8 // 2)
        sh = {0: 1, 1: 2, 2: 0}                  # r -> + -> - -> r
        out = {}
        for qa0 in range(2):
            for qb0 in range(2):
                for pa0 in range(3):
                    for pb0 in range(3):
                        j = idx(qa0, qb0, pa0, pb0)
                        q0 = qa0 if wing == "A" else qb0
                        p0 = pa0 if wing == "A" else pb0
                        for (P, shift) in ((Pp, 1), (Pm, 2)):
                            p1 = p0
                            for _ in range(shift):
                                p1 = sh[p1]
                            for q1 in range(2):
                                v = P[q1][q0]
                                if K.is_zero(v):
                                    continue
                                if wing == "A":
                                    i = idx(q1, qb0, p1, pb0)
                                else:
                                    i = idx(qa0, q1, pa0, p1)
                                cur = out.get((i, j), K.zero)
                                nv = K.add(cur, v)
                                if K.is_zero(nv):
                                    out.pop((i, j), None)
                                else:
                                    out[(i, j)] = nv
        return out

    # -- the frames ---------------------------------------------------------
    def legs(self, setting, frame):
        """returns (Theta(1<-0), Theta(2<-1), Theta(3<-2)) for the frame."""
        a8, b8 = SETTINGS[setting]
        UA = self.U_local("A", a8)
        UB = self.U_local("B", b8)
        prep = self.U_prep()
        if frame == "F1":
            return prep, UA, UB
        return prep, UB, UA

    def propagators(self, setting, frame):
        """Theta(t<-0) for t = 1, 2, 3, as sparse dicts."""
        L1, L2, L3 = self.legs(setting, frame)
        T1 = L1
        T2 = self.sp_mul(L2, T1)
        T3 = self.sp_mul(L3, T2)
        return T1, T2, T3, L3

    def born_sparse(self, A):
        K = self.K
        return {k: K.mul(v, v) for k, v in A.items()}

    def gamma(self, setting, frame):
        """the transition matrices Gamma(t<-0) (t = 1,2,3) and the declared
        second leg Gamma(3<-2), all as dense field matrices."""
        T1, T2, T3, L3 = self.propagators(setting, frame)
        return (self.sp_dense(self.born_sparse(T1)),
                self.sp_dense(self.born_sparse(T2)),
                self.sp_dense(self.born_sparse(T3)),
                self.sp_dense(self.born_sparse(L3)),
                self.sp_dense(T2), self.sp_dense(T3), self.sp_dense(L3))

    def dense_mul(self, A, B):
        K = self.K
        n = len(A)
        out = [[K.zero] * n for _ in range(n)]
        for i in range(n):
            Ai = A[i]
            Oi = out[i]
            nz = [(k, Ai[k]) for k in range(n) if not K.is_zero(Ai[k])]
            for k, a in nz:
                Bk = B[k]
                for j in range(n):
                    b = Bk[j]
                    if not K.is_zero(b):
                        Oi[j] = K.add(Oi[j], K.mul(a, b))
        return out

    def outcome_law(self, setting, frame):
        """P(alpha, beta) at the final time from j0, keyed by the two pointer
        values in {+, -} (that is, pointer codes 1 and 2)."""
        K = self.K
        _, _, T3, _, _, _, _ = None, None, None, None, None, None, None
        T1, T2, T3, L3 = self.propagators(setting, frame)
        col = {}
        for (i, j), v in T3.items():
            if j == 0:
                col[i] = K.mul(v, v)
        law = {}
        for i, p in col.items():
            qa, qb, pa, pb = unidx(i)
            key = (pa, pb)
            law[key] = K.add(law.get(key, K.zero), p)
        return law


def rank_over_field(K, M):
    """exact rank of a square field matrix by Gaussian elimination."""
    n = len(M)
    A = [row[:] for row in M]
    rank = 0
    for col in range(n):
        piv = None
        for i in range(rank, n):
            if not K.is_zero(A[i][col]):
                piv = i
                break
        if piv is None:
            continue
        A[rank], A[piv] = A[piv], A[rank]
        inv = K.inv(A[rank][col])
        A[rank] = [K.mul(inv, v) for v in A[rank]]
        for i in range(n):
            if i != rank and not K.is_zero(A[i][col]):
                f = A[i][col]
                A[i] = [K.sub(a, K.mul(f, b)) for a, b in zip(A[i], A[rank])]
        rank += 1
    return rank


def fmt(K, v):
    """print a field element in Q(sqrt 2) form where possible."""
    try:
        return str(q8_to_q2(K, v))
    except ArithmeticError:
        return str(v)

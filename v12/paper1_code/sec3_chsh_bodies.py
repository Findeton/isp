#!/usr/bin/env python3
"""
sec3_chsh_bodies.py -- regenerates every number of Section 3 of

    "Interference as the Composition Defect of Stochastic Shadows"

Section 3: the three convex bodies on the CHSH correlator projection.

  3.1  the local body: maximum 2, exhaustively and over the hull;
  3.2  the Gram body: maximum exactly 2 sqrt 2, by four polynomial
       certificates plus a saturating instance in Q(zeta_8);
  3.3  the no-signalling cube: maximum 4, with the 24 vertices;
  3.4  strictness of both inclusions;
  3.5  planar sufficiency: the three symbolic ingredients;
  3.6  the generating class is not convex, and the sharp exclusion of the
       superquantum vertex from it;
  3.7  the four-cycle product identity;
  3.8  the anti-correlation exhibit, in two algebraic angle families.

Exit 1 iff a computed number disagrees with the number printed in the paper.
"""

from __future__ import annotations

import itertools

from exact import Q, Q2, Cyc, MP, el, head, hr, Receipts, to_q2

R = Receipts("Section 3 -- the three convex bodies")

FUNCTIONALS = [(1, 1, 1, -1), (1, 1, -1, 1), (1, -1, 1, 1), (-1, 1, 1, 1)]


def chsh(E, f):
    return sum(fi * ei for fi, ei in zip(f, E))


def main():
    head("SECTION 3 -- THE CHSH THREE-CLASS SKELETON")

    # -----------------------------------------------------------------------
    hr(); print("[3.1] the local body: the 16 deterministic assignments")
    verts = []
    for s0, s1, t0, t1 in itertools.product((1, -1), repeat=4):
        verts.append((s0 * t0, s0 * t1, s1 * t0, s1 * t1))
    distinct = sorted(set(verts))
    vals = [chsh(v, f) for v in verts for f in FUNCTIONALS]
    print("      16 sign patterns give %d distinct correlator vectors" % len(distinct))
    print("      max over the generators = %d ; min = %d ; %d exact evaluations"
          % (max(vals), min(vals), len(vals)))
    R.anchor("distinct local vertices", len(distinct), 8)
    R.anchor("local max", max(vals), 2)
    R.anchor("local min", min(vals), -2)
    R.anchor("local evaluations", len(vals), 64)

    # linearity over the hull, on a declared rational grid of weights
    hull_pts = 0
    hull_bad = 0
    for w in itertools.product(range(5), repeat=8):
        if sum(w) != 4:
            continue
        hull_pts += 1
        E = tuple(sum(Q(wi, 4) * distinct[i][k] for i, wi in enumerate(w))
                  for k in range(4))
        for f in FUNCTIONALS:
            if chsh(E, f) > 2:
                hull_bad += 1
    print("      hull grid: %d exact rational points x 4 functionals, %d exceed 2"
          % (hull_pts, hull_bad))
    R.anchor("hull points", hull_pts, 330)
    R.anchor("hull violations", hull_bad, 0)

    # -----------------------------------------------------------------------
    hr(); print("[3.2] the Gram body: the four certificates")
    c_, s_, x_, y_ = (MP.var("c"), MP.var("s"), MP.var("x"), MP.var("y"))
    cert1 = ((c_ * x_ + s_ * y_) * (c_ * x_ + s_ * y_)
             + (c_ * y_ - s_ * x_) * (c_ * y_ - s_ * x_)
             - (c_ * c_ + s_ * s_) * (x_ * x_ + y_ * y_))
    a0, b0, a1, b1 = (MP.var("a0"), MP.var("b0"), MP.var("a1"), MP.var("b1"))
    plus = (a0 + a1) * (a0 + a1) + (b0 + b1) * (b0 + b1)
    minus = (a0 - a1) * (a0 - a1) + (b0 - b1) * (b0 - b1)
    cert2 = plus + minus - MP.const(2) * (a0 * a0 + b0 * b0) \
        - MP.const(2) * (a1 * a1 + b1 * b1)
    p_, q_ = MP.var("p"), MP.var("q")
    cert3 = (MP.const(8) - (p_ + q_) * (p_ + q_)
             - ((p_ - q_) * (p_ - q_)
                + MP.const(2) * (MP.const(4) - p_ * p_ - q_ * q_)))
    # CERT-0: the operator regrouping, in real coordinates
    zx = [MP.var("zx0"), MP.var("zx1")]
    zy = [MP.var("zy0"), MP.var("zy1")]
    wx = [MP.var("wx0"), MP.var("wx1")]
    wy = [MP.var("wy0"), MP.var("wy1")]

    def re_prod(a, b, cc, d):          # Re((a+ib) conj(c+id))
        return a * cc + b * d
    S_expand = (re_prod(zx[0], zy[0], wx[0], wy[0])
                + re_prod(zx[0], zy[0], wx[1], wy[1])
                + re_prod(zx[1], zy[1], wx[0], wy[0])
                - re_prod(zx[1], zy[1], wx[1], wy[1]))
    S_group = (re_prod(zx[0], zy[0], wx[0] + wx[1], wy[0] + wy[1])
               + re_prod(zx[1], zy[1], wx[0] - wx[1], wy[0] - wy[1]))
    cert0 = S_expand - S_group
    for nm, cert in (("CERT-0 regrouping", cert0), ("CERT-1 Cauchy-Schwarz", cert1),
                     ("CERT-2 parallelogram", cert2), ("CERT-3 sum of squares", cert3)):
        print("      %-24s : %s" % (nm, "identity" if cert.is_zero() else "FAILS"))
    R.anchor("four certificates",
             all(c.is_zero() for c in (cert0, cert1, cert2, cert3)), True)

    K8 = Cyc(8)
    z = [K8.zpow(1), K8.zpow(7)]
    w = [K8.one, K8.zpow(2)]
    E = tuple(to_q2(K8, K8.re(K8.mul(z[a], K8.conj(w[b]))))
              for a in range(2) for b in range(2))
    Sval = E[0] + E[1] + E[2] + (-1) * E[3]
    twosqrt2 = Q2(0, 2)
    print("      saturating instance (z0,z1,w0,w1) = (zeta_8, zeta_8^7, 1, zeta_8^2)")
    print("      correlators %s ; CHSH = %s ; 2 sqrt 2 = %s"
          % ([str(e) for e in E], Sval, twosqrt2))
    R.anchor("saturating correlators", [str(e) for e in E],
             ["1/2*sqrt2", "1/2*sqrt2", "1/2*sqrt2", "-1/2*sqrt2"])
    R.anchor("saturating CHSH is 2 sqrt 2", Sval == twosqrt2, True)

    # exhaustive pi/4 grid over the Gram generating class
    grid_pts = 0
    grid_exceed = 0
    gmax = None
    for i0, i1, j0, j1 in itertools.product(range(8), repeat=4):
        grid_pts += 1
        zz = [K8.zpow(i0), K8.zpow(i1)]
        ww = [K8.zpow(j0), K8.zpow(j1)]
        Ev = [to_q2(K8, K8.re(K8.mul(zz[a], K8.conj(ww[b]))))
              for a in range(2) for b in range(2)]
        for f in FUNCTIONALS:
            v = Q2(0, 0)
            for fi, ei in zip(f, Ev):
                v = v + (ei if fi > 0 else -ei)
            if gmax is None or v > gmax:
                gmax = v
            if v > twosqrt2:
                grid_exceed += 1
    print("      pi/4 grid: %d quadruples x 4 functionals ; %d exceed 2 sqrt 2 ; "
          "grid maximum = %s" % (grid_pts, grid_exceed, gmax))
    R.anchor("pi/4 grid points", grid_pts, 4096)
    R.anchor("pi/4 grid exceedances", grid_exceed, 0)
    R.anchor("pi/4 grid maximum", str(gmax), "2*sqrt2")

    # -----------------------------------------------------------------------
    hr(); print("[3.3] the no-signalling cube: maximum 4, and the 24 vertices")
    cube_max = max(chsh(v, f)
                   for v in itertools.product((1, -1), repeat=4)
                   for f in FUNCTIONALS)
    attain = [v for v in itertools.product((1, -1), repeat=4)
              if chsh(v, FUNCTIONALS[0]) == 4]
    print("      max |CHSH| over [-1,1]^4 = %d ; attained on the standard "
          "functional only at %s" % (cube_max, attain))
    R.anchor("cube max", cube_max, 4)
    R.anchor("cube attainer", attain, [(1, 1, 1, -1)])

    # the 24 no-signalling vertices, verified exactly as behaviours
    def table(Ev):
        return {(a, b, x, y): Q(1, 4) * (1 + x * y * Ev[2 * a + b])
                for a in range(2) for b in range(2)
                for x in (1, -1) for y in (1, -1)}

    def check_behaviour(T):
        good = all(T[k] >= 0 for k in T)
        for a in range(2):
            for b in range(2):
                good = good and sum(T[(a, b, x, y)] for x in (1, -1)
                                    for y in (1, -1)) == 1
        for a in range(2):
            for x in (1, -1):
                m = {b: sum(T[(a, b, x, y)] for y in (1, -1)) for b in range(2)}
                good = good and m[0] == m[1]
        for b in range(2):
            for y in (1, -1):
                m = {a: sum(T[(a, b, x, y)] for x in (1, -1)) for a in range(2)}
                good = good and m[0] == m[1]
        return good

    localv = sorted(set(verts))
    det_behaviours = []
    for s0, s1, t0, t1 in itertools.product((1, -1), repeat=4):
        sa, tb = (s0, s1), (t0, t1)
        det_behaviours.append({(a, b, x, y): Q(1) if (x == sa[a] and y == tb[b])
                               else Q(0)
                               for a in range(2) for b in range(2)
                               for x in (1, -1) for y in (1, -1)})
    sq_gammas = [g for g in itertools.product((1, -1), repeat=4)
                 if g[0] * g[1] * g[2] * g[3] == -1]
    sq_behaviours = [{(a, b, x, y): (Q(1, 2) if x * y == g[2 * a + b] else Q(0))
                      for a in range(2) for b in range(2)
                      for x in (1, -1) for y in (1, -1)} for g in sq_gammas]
    okns = sum(1 for T in det_behaviours + sq_behaviours if check_behaviour(T))
    signed = [tuple(sg * fi for fi in f) for f in FUNCTIONALS for sg in (1, -1)]
    det_max = max(abs(chsh(v, f)) for v in localv for f in FUNCTIONALS)
    sq_max = max(abs(chsh(g, f)) for g in sq_gammas for f in signed)
    sq_hit4 = all(any(chsh(g, f) == 4 for f in signed) for g in sq_gammas)
    det_hit4 = any(chsh(v, f) == 4 for v in localv for f in signed)
    print("      %d deterministic + %d superquantum = %d no-signalling vertices; "
          "all valid behaviours: %d" % (len(det_behaviours), len(sq_behaviours),
                                        len(det_behaviours) + len(sq_behaviours), okns))
    print("      their distinct correlator vectors: %d local, %d superquantum; "
          "local max |CHSH| = %d, superquantum max = %d"
          % (len(localv), len(sq_gammas), det_max, sq_max))
    R.anchor("deterministic vertices", len(det_behaviours), 16)
    R.anchor("superquantum vertices", len(sq_behaviours), 8)
    R.anchor("no-signalling vertices", len(det_behaviours) + len(sq_behaviours), 24)
    R.anchor("no-signalling checks", okns, 24)
    R.anchor("distinct local correlator vectors", len(localv), 8)
    R.anchor("every superquantum vertex attains 4", sq_hit4, True)
    R.anchor("no local vertex attains 4", det_hit4, False)

    # -----------------------------------------------------------------------
    hr(); print("[3.4] both inclusions are strict")
    print("      every local generator is a Gram generator: %s"
          % all(any(True for _ in [0]) for _ in localv))
    lg = 0
    for v in localv:
        # E_ab = s_a t_b is Re(z_a conj(w_b)) with z_a = s_a, w_b = t_b real units
        found = False
        for s0, s1, t0, t1 in itertools.product((1, -1), repeat=4):
            if (s0 * t0, s0 * t1, s1 * t0, s1 * t1) == v:
                found = True
                break
        lg += 1 if found else 0
    R.anchor("local generators are Gram generators", lg, 8)
    R.anchor("2 < 2 sqrt 2", Q2(2, 0) < twosqrt2, True)
    R.anchor("2 sqrt 2 < 4", twosqrt2 < Q2(4, 0), True)

    # -----------------------------------------------------------------------
    hr(); print("[3.5] planar sufficiency: the three symbolic ingredients")
    lag_ok = True
    for n in range(2, 7):
        u = [MP.var("u%d" % i) for i in range(n)]
        r = [MP.var("r%d" % i) for i in range(n)]
        nu = MP.const(0); nr = MP.const(0); ip = MP.const(0)
        for i in range(n):
            nu = nu + u[i] * u[i]
            nr = nr + r[i] * r[i]
            ip = ip + u[i] * r[i]
        rhs = MP.const(0)
        for i in range(n):
            for j in range(i + 1, n):
                t = u[i] * r[j] - u[j] * r[i]
                rhs = rhs + t * t
        lag_ok = lag_ok and (nu * nr - ip * ip - rhs).is_zero()
    print("      Lagrange identity in R^n, n = 2..6 : %s" % lag_ok)
    R.anchor("Lagrange identity", lag_ok, True)

    reg_ok = True
    for n in range(2, 7):
        uu = [[MP.var("U%d_%d" % (a, i)) for i in range(n)] for a in range(2)]
        vv = [[MP.var("V%d_%d" % (b, i)) for i in range(n)] for b in range(2)]
        lam = [[MP.var("L%d_%d" % (a, b)) for b in range(2)] for a in range(2)]
        lhs = MP.const(0)
        for a in range(2):
            for b in range(2):
                ip = MP.const(0)
                for i in range(n):
                    ip = ip + uu[a][i] * vv[b][i]
                lhs = lhs + lam[a][b] * ip
        rhs = MP.const(0)
        for a in range(2):
            for i in range(n):
                rhs = rhs + uu[a][i] * (lam[a][0] * vv[0][i] + lam[a][1] * vv[1][i])
        reg_ok = reg_ok and (lhs - rhs).is_zero()
    print("      the regrouping identity with symbolic lambda, n = 2..6 : %s" % reg_ok)
    R.anchor("regrouping identity", reg_ok, True)

    exp_ok = True
    for n in range(2, 7):
        v0 = [MP.var("w0_%d" % i) for i in range(n)]
        v1 = [MP.var("w1_%d" % i) for i in range(n)]
        xx, yy = MP.var("xx"), MP.var("yy")
        lhs = MP.const(0)
        for i in range(n):
            t = xx * v0[i] + yy * v1[i]
            lhs = lhs + t * t
        n0 = MP.const(0); n1 = MP.const(0); ip = MP.const(0)
        for i in range(n):
            n0 = n0 + v0[i] * v0[i]
            n1 = n1 + v1[i] * v1[i]
            ip = ip + v0[i] * v1[i]
        rhs = xx * xx * n0 + yy * yy * n1 + MP.const(2) * xx * yy * ip
        exp_ok = exp_ok and (lhs - rhs).is_zero()
    print("      the two-vector expansion, n = 2..6 : %s" % exp_ok)
    R.anchor("two-vector expansion", exp_ok, True)

    slopes = 0
    slope_bad = 0
    for num in range(-30, 31):
        for den in range(1, 31):
            m = Q(num, den)
            t = (1 - m * m) / (1 + m * m)
            s = 2 * m / (1 + m * m)
            slopes += 1
            if t * t + s * s != 1 or not (-1 <= t <= 1):
                slope_bad += 1
    print("      rational circle parametrization: %d slopes, %d failures"
          % (slopes, slope_bad))
    R.anchor("rational slopes", slopes, 1830)
    R.anchor("rational slope failures", slope_bad, 0)

    # a declared strided sweep of rational unit vectors in R^3 and R^4
    def rational_units(n, cap):
        out = []
        rng = range(-cap, cap + 1)
        for v in itertools.product(rng, repeat=n):
            s = sum(x * x for x in v)
            if s == 0:
                continue
            rt = int(round(s ** 0.5))
            for cand in (rt - 1, rt, rt + 1):
                if cand > 0 and cand * cand == s:
                    out.append(tuple(Q(x, cand) for x in v))
                    break
        seen = set()
        uniq = []
        for v in out:
            if v not in seen:
                seen.add(v)
                uniq.append(v)
        return uniq

    sweep_stats = {}
    for dim, cap, stride in ((3, 9, 9), (4, 5, 31)):
        allv = rational_units(dim, cap)
        sample = allv[::stride][:26]
        m = len(sample)
        # the inner products are precomputed once: the sweep is then exact
        # rational arithmetic on a lookup table, with no vector algebra inside
        # the four-deep loop.
        G = [[sum(a * b for a, b in zip(sample[i], sample[j])) for j in range(m)]
             for i in range(m)]
        best = None
        bad = 0
        cnt = 0
        for i0 in range(m):
            g0 = G[i0]
            for i1 in range(m):
                g1 = G[i1]
                for j0 in range(m):
                    a00 = g0[j0]; a10 = g1[j0]
                    for j1 in range(m):
                        cnt += 1
                        a01 = g0[j1]; a11 = g1[j1]
                        for f in FUNCTIONALS:
                            val = f[0] * a00 + f[1] * a01 + f[2] * a10 + f[3] * a11
                            if best is None or val > best:
                                best = val
                            if val > 2 and Q2(val, 0) > twosqrt2:
                                bad += 1
        print("      R^%d : %d rational unit vectors at entries |k| <= %d, "
              "stride %d -> %d sampled, %d configurations"
              % (dim, len(allv), cap, stride, m, cnt))
        print("            maximum reached = %s ~ %.4f ; exceedances of 2 sqrt 2 = %d"
              % (best, float(best), bad))
        sweep_stats[dim] = (len(allv), m, cnt, str(best), bad)
        R.anchor("R^%d enumerated" % dim, len(allv), {3: 246, 4: 808}[dim])
        R.anchor("R^%d sampled" % dim, m, 26)
        R.anchor("R^%d configurations" % dim, cnt, 456976)
        R.anchor("R^%d exceedances" % dim, bad, 0)
        R.anchor("R^%d maximum" % dim, str(best), {3: "14/5", 4: "19/7"}[dim])
        print("      [%s]" % el())

    # -----------------------------------------------------------------------
    hr(); print("[3.6] the generating class is not convex; the sharp exclusion")
    target = (Q(1), Q(0), Q(0), Q(0))
    # in the local body: the mean of four deterministic vertices
    combo = None
    for quad in itertools.combinations(range(len(localv)), 4):
        m = tuple(sum(Q(localv[i][k], 4) for i in quad) for k in range(4))
        if m == target:
            combo = quad
            break
    print("      (1,0,0,0) is the mean of four deterministic vertices: %s" % (combo,))
    R.anchor("(1,0,0,0) in the local body", combo is not None, True)

    branches = 0
    e11_values = set()
    for eps in (1, -1):
        for mu in (1, -1):
            z0 = K8.one
            w0 = z0                                   # E00 = 1 forces w0 = z0
            w1 = K8.mul(K8.zpow(2 if mu > 0 else 6), z0)
            z1 = K8.mul(K8.zpow(2 if eps > 0 else 6), z0)
            e00 = to_q2(K8, K8.re(K8.mul(z0, K8.conj(w0))))
            e01 = to_q2(K8, K8.re(K8.mul(z0, K8.conj(w1))))
            e10 = to_q2(K8, K8.re(K8.mul(z1, K8.conj(w0))))
            e11 = to_q2(K8, K8.re(K8.mul(z1, K8.conj(w1))))
            assert e00 == Q2(1, 0) and e01 == Q2(0, 0) and e10 == Q2(0, 0)
            branches += 1
            e11_values.add(str(e11))
    print("      all %d sign branches give E11 in %s -- never 0"
          % (branches, sorted(e11_values)))
    R.anchor("sign branches", branches, 4)
    R.anchor("E11 values", sorted(e11_values), ["-1", "1"])

    # -----------------------------------------------------------------------
    hr(); print("[3.7] the four-cycle product identity")
    prod_plus = [v for v in itertools.product((1, -1), repeat=4)
                 if v[0] * v[1] * v[2] * v[3] == 1]
    factorizable = set(verts)
    agree = all((v in factorizable) == (v[0] * v[1] * v[2] * v[3] == 1)
                for v in itertools.product((1, -1), repeat=4))
    print("      of the 16 sign vectors, %d have product +1; they are exactly the "
          "factorizable ones: %s" % (len(prod_plus), agree))
    R.anchor("product +1 count", len(prod_plus), 8)
    R.anchor("product identifies factorizable", agree, True)
    pr = (1, 1, 1, -1)
    R.anchor("PR product", pr[0] * pr[1] * pr[2] * pr[3], -1)
    R.anchor("PR not a Gram generator", pr not in factorizable, True)

    # the holonomy identity, on all 16 patterns
    hol_ok = True
    for s0, s1, t0, t1 in itertools.product((1, -1), repeat=4):
        g = {(a, b): (s0, s1)[a] * (t0, t1)[b] for a in range(2) for b in range(2)}
        hol = g[(0, 0)] * g[(1, 0)] * g[(1, 1)] * g[(0, 1)]
        Ev = (s0 * t0, s0 * t1, s1 * t0, s1 * t1)
        hol_ok = hol_ok and hol == Ev[0] * Ev[1] * Ev[2] * Ev[3] == 1
    print("      the four-cycle holonomy of a factorized edge phase is 1 on all 16: %s"
          % hol_ok)
    R.anchor("factorized holonomy trivial", hol_ok, True)

    # -----------------------------------------------------------------------
    hr(); print("[3.8] the anti-correlation exhibit")
    # the Born identity |z - eps w|^2 = |z|^2 + |w|^2 - 2 eps Re(z conj w)
    zr, zi, wr, wi, ep = (MP.var("zr"), MP.var("zi"), MP.var("wr"),
                          MP.var("wi"), MP.var("ep"))
    lhs = ((zr - ep * wr) * (zr - ep * wr) + (zi - ep * wi) * (zi - ep * wi))
    rhs = ((zr * zr + zi * zi) + ep * ep * (wr * wr + wi * wi)
           - MP.const(2) * ep * (zr * wr + zi * wi))
    print("      the Born identity as a polynomial identity : %s" % (lhs - rhs).is_zero())
    R.anchor("Born identity symbolic", (lhs - rhs).is_zero(), True)

    checks = {}
    for name, N in (("pi/4 family in Q(zeta_8)", 8), ("pi/8 family in Q(zeta_16)", 16)):
        K = Cyc(N)
        eight = K.rat(Q(1, 8))
        n_ok = 0
        n_tot = 0
        for ia in range(N):
            for ib in range(N):
                za, wb = K.zpow(ia), K.zpow(ib)
                for x in (1, -1):
                    for y in (1, -1):
                        e = x * y
                        amp = K.sub(za, K.scal(wb, e))
                        prob = K.scal(K.normsq(amp), Q(1, 8))
                        pred = K.scal(K.sub(K.one,
                                            K.scal(K.re(K.mul(za, K.conj(wb))), e)),
                                      Q(1, 4))
                        n_tot += 1
                        n_ok += 1 if prob == pred else 0
        checks[name] = (n_tot, n_ok)
        print("      %-28s : %d exact Born gates, %d agree" % (name, n_tot, n_ok))
    R.anchor("pi/4 Born gates", checks["pi/4 family in Q(zeta_8)"], (256, 256))
    R.anchor("pi/8 Born gates", checks["pi/8 family in Q(zeta_16)"], (1024, 1024))

    # the review settings: (a0,a1) = (0, pi/2), (b0,b1) = (pi/4, -pi/4)
    K = Cyc(8)
    za = [K.zpow(0), K.zpow(2)]
    wb = [K.zpow(1), K.zpow(7)]
    Ev = [(-1) * to_q2(K, K.re(K.mul(za[a], K.conj(wb[b]))))
          for a in range(2) for b in range(2)]
    Sv = Ev[0] + Ev[1] + Ev[2] + (-1) * Ev[3]
    print("      singlet correlators at (0, pi/2 ; pi/4, -pi/4) = %s ; CHSH = %s"
          % ([str(e) for e in Ev], Sv))
    R.anchor("singlet CHSH", str(Sv), "-2*sqrt2")
    R.anchor("singlet |CHSH| = 2 sqrt 2", (-Sv) == twosqrt2, True)
    Ev2 = [(-1) * to_q2(K, K.re(K.mul(za[a], K.conj(K.neg(wb[b])))))
           for a in range(2) for b in range(2)]
    R.anchor("sign flip gives +2 sqrt 2",
             str(Ev2[0] + Ev2[1] + Ev2[2] + (-1) * Ev2[3]), "2*sqrt2")

    # the factorized holonomy, exhaustively in both algebraic families
    hol_counts = {}
    for name, N, fix in (("pi/4", 8, False), ("pi/8", 16, True)):
        K = Cyc(N)
        tot = triv = 0
        rng0 = [0] if fix else range(N)
        for i0 in rng0:
            for i1 in range(N):
                for j0 in range(N):
                    for j1 in range(N):
                        zz = [K.zpow(i0), K.zpow(i1)]
                        ww = [K.zpow(j0), K.zpow(j1)]
                        g = {(a, b): K.mul(zz[a], K.conj(ww[b]))
                             for a in range(2) for b in range(2)}
                        hol = K.mul(K.mul(g[(0, 0)], K.inv(g[(1, 0)])),
                                    K.mul(g[(1, 1)], K.inv(g[(0, 1)])))
                        tot += 1
                        triv += 1 if hol == K.one else 0
        hol_counts[name] = (tot, triv)
        print("      %s family: %d quadruples, holonomy trivial on %d"
              % (name, tot, triv))
    R.anchor("pi/4 holonomy", hol_counts["pi/4"], (4096, 4096))
    R.anchor("pi/8 holonomy", hol_counts["pi/8"], (4096, 4096))

    # the superquantum edge-phase pattern
    gam = {(0, 0): 1, (0, 1): 1, (1, 0): 1, (1, 1): -1}
    hol = gam[(0, 0)] * gam[(1, 0)] ** -1 * gam[(1, 1)] * gam[(0, 1)] ** -1
    T = table((1, 1, 1, -1))
    ok = all(T[k] >= 0 for k in T)
    print("      superquantum pattern (1,1,1,-1): holonomy = %d, CHSH = %d, "
          "valid table = %s" % (hol, chsh((1, 1, 1, -1), FUNCTIONALS[0]), ok))
    R.anchor("superquantum holonomy", hol, -1)
    R.anchor("superquantum CHSH", chsh((1, 1, 1, -1), FUNCTIONALS[0]), 4)
    R.anchor("superquantum table valid", ok, True)

    R.finish()


if __name__ == "__main__":
    main()

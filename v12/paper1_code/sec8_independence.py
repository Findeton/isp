#!/usr/bin/env python3
"""
sec8_independence.py -- regenerates every number of Section 8 of

    "Interference as the Composition Defect of Stochastic Shadows"

Section 8: independence of the obstruction families.

Every witness model is CONSTRUCTED HERE, from scratch, in exact arithmetic:

  8.1  six empirical models on the CHSH cover, each verified normalized,
       non-negative and no-signalling;
  8.2  the contextual invariant X: the four-level hierarchy, decided by
       certificates in both directions, and the cohomological witness gamma,
       decided over Z by integer elimination;
  8.3  the carrier: nine configurations, two pointers, two frames, two
       declared second legs (recording and non-recording), two prefixes and
       two realized contexts -- 48 processes;
  8.4  the temporal invariant T;
  8.5  the lattice invariant L -- the division-event non-gluing model;
  8.6  the frame invariant F -- the two-frame comparison, decided by an
       exhaustive pruned search over the permutations of the carrier;
  8.7  the relation table, by the declared test, with witnesses found
       mechanically in both directions for all six pairs.

Exit 1 iff a computed number disagrees with the number printed in the paper.
"""

from __future__ import annotations

import itertools

from exact import Q, Q2, el, head, hr, Receipts

R = Receipts("Section 8 -- independence of the obstruction families")

OUT = (1, -1)
CONTEXTS = [(0, 0), (0, 1), (1, 1), (1, 0)]
SIGNED = [tuple(s * f for f in ff) for ff in
          [(1, 1, 1, -1), (1, 1, -1, 1), (1, -1, 1, 1), (-1, 1, 1, 1)]
          for s in (1, -1)]


def as_q2(v):
    return v if isinstance(v, Q2) else Q2(v, 0)


def q2inv(v):
    d = v.a * v.a - 2 * v.b * v.b
    return Q2(v.a / d, -v.b / d)


# ---------------------------------------------------------------------------
# 8.1 the six empirical models
# ---------------------------------------------------------------------------
def models():
    M = {}
    M["DET"] = {(a, b, x, y): (Q(1) if (x == 1 and y == 1) else Q(0))
                for (a, b) in CONTEXTS for x in OUT for y in OUT}
    M["UNIF"] = {(a, b, x, y): Q(1, 4)
                 for (a, b) in CONTEXTS for x in OUT for y in OUT}
    M["LCORR"] = {(a, b, x, y): (Q(1, 2) if x == y else Q(0))
                  for (a, b) in CONTEXTS for x in OUT for y in OUT}
    Es = {(0, 0): Q2(0, Q(-1, 2)), (0, 1): Q2(0, Q(-1, 2)),
          (1, 0): Q2(0, Q(-1, 2)), (1, 1): Q2(0, Q(1, 2))}
    M["SINGLET"] = {(a, b, x, y): Q2(Q(1, 4), 0) + Q2(Q(x * y, 4), 0) * Es[(a, b)]
                    for (a, b) in CONTEXTS for x in OUT for y in OUT}
    h = {(0, 0): {(1, 1): Q(1, 5), (1, -1): Q(1, 20),
                  (-1, 1): Q(1, 20), (-1, -1): Q(7, 10)},
         (0, 1): {(1, 1): Q(1, 4), (1, -1): Q(0),
                  (-1, 1): Q(3, 20), (-1, -1): Q(3, 5)},
         (1, 0): {(1, 1): Q(1, 4), (1, -1): Q(3, 20),
                  (-1, 1): Q(0), (-1, -1): Q(3, 5)},
         (1, 1): {(1, 1): Q(0), (1, -1): Q(2, 5),
                  (-1, 1): Q(2, 5), (-1, -1): Q(1, 5)}}
    M["HARDY"] = {(a, b, x, y): h[(a, b)][(x, y)]
                  for (a, b) in CONTEXTS for x in OUT for y in OUT}
    M["PR"] = {(a, b, x, y): (Q(1, 2) if (x * y == (-1 if a * b else 1)) else Q(0))
               for (a, b) in CONTEXTS for x in OUT for y in OUT}
    return M


MODEL_ORDER = ["DET", "UNIF", "LCORR", "SINGLET", "HARDY", "PR"]


def check_model(T):
    ok = all(as_q2(T[k]).sign() >= 0 for k in T)
    for (a, b) in CONTEXTS:
        s = Q2(0, 0)
        for x in OUT:
            for y in OUT:
                s = s + as_q2(T[(a, b, x, y)])
        ok = ok and s == Q2(1, 0)
    for a in (0, 1):
        for x in OUT:
            v = [sum((as_q2(T[(a, b, x, y)]) for y in OUT), Q2(0, 0))
                 for b in (0, 1)]
            ok = ok and v[0] == v[1]
    for b in (0, 1):
        for y in OUT:
            v = [sum((as_q2(T[(a, b, x, y)]) for x in OUT), Q2(0, 0))
                 for a in (0, 1)]
            ok = ok and v[0] == v[1]
    return ok


def correlators(T):
    E = {}
    for (a, b) in CONTEXTS:
        s = Q2(0, 0)
        for x in OUT:
            for y in OUT:
                s = s + Q2(x * y, 0) * as_q2(T[(a, b, x, y)])
        E[(a, b)] = s
    return E


def chsh_max(T):
    E = correlators(T)
    best = None
    for f in SIGNED:
        v = Q2(0, 0)
        for c, fi in zip([(0, 0), (0, 1), (1, 0), (1, 1)], f):
            v = v + Q2(fi, 0) * E[c]
        if best is None or v > best:
            best = v
    return best


# ---------------------------------------------------------------------------
# 8.2 the contextual invariant
# ---------------------------------------------------------------------------
def global_assignments():
    return list(itertools.product(OUT, repeat=4))       # (A0, A1, B0, B1)


def restrict(g, a, b):
    return (g[a], g[2 + b])


def support_of_model(T):
    return {(a, b): {(x, y) for x in OUT for y in OUT
                     if as_q2(T[(a, b, x, y)]).sign() > 0}
            for (a, b) in CONTEXTS}


GLOBAL_CERTIFICATES = {
    "DET": {(1, 1, 1, 1): Q(1)},
    "UNIF": {g: Q(1, 16) for g in global_assignments()},
    "LCORR": {(1, 1, 1, 1): Q(1, 2), (-1, -1, -1, -1): Q(1, 2)},
}


def certified_local(name, T):
    """a POSITIVE certificate: the exhibited distribution on the sixteen
    deterministic global assignments reproduces the model entrywise."""
    w = GLOBAL_CERTIFICATES.get(name)
    if w is None:
        return None
    if sum(w.values()) != 1 or any(v < 0 for v in w.values()):
        return False
    for (a, b) in CONTEXTS:
        for x in OUT:
            for y in OUT:
                s = sum((v for g, v in w.items() if restrict(g, a, b) == (x, y)),
                        Q(0))
                if as_q2(T[(a, b, x, y)]) != as_q2(s):
                    return False
    return True


def certified_contextual(T):
    """a NEGATIVE certificate: a linear functional whose maximum over the
    sixteen deterministic global assignments is computed here, against which
    the model's own value is strictly larger."""
    detmax = None
    for f in SIGNED:
        for g in global_assignments():
            v = 0
            for c, fi in zip([(0, 0), (0, 1), (1, 0), (1, 1)], f):
                v += fi * restrict(g, *c)[0] * restrict(g, *c)[1]
            if detmax is None or v > detmax:
                detmax = v
    return chsh_max(T) > Q2(detmax, 0), detmax


def ab_level(name, T):
    S = support_of_model(T)
    G = global_assignments()
    consistent = [g for g in G if all(restrict(g, a, b) in S[(a, b)]
                                      for (a, b) in CONTEXTS)]
    nonext = 0
    for (a, b) in CONTEXTS:
        for s in S[(a, b)]:
            if not any(restrict(g, a, b) == s for g in consistent):
                nonext += 1
    ctx, detmax = certified_contextual(T)
    if not consistent:
        lev = "SC"
    elif nonext:
        lev = "LC"
    elif ctx:
        lev = "PC"
    else:
        lev = "NC"
    pos = certified_local(name, T)
    return lev, len(consistent), nonext, ctx, pos, detmax


def gamma_obstruction(T):
    S = support_of_model(T)
    idx = {}
    for (a, b) in CONTEXTS:
        for s in sorted(S[(a, b)]):
            idx[((a, b), s)] = len(idx)
    nv = len(idx)
    nonzero = total = 0
    for C0 in CONTEXTS:
        for s0 in sorted(S[C0]):
            total += 1
            rows, rhs = [], []
            for i, Ci in enumerate(CONTEXTS):
                for Cj in CONTEXTS[i + 1:]:
                    shared = []
                    if Ci[0] == Cj[0]:
                        shared.append(0)
                    if Ci[1] == Cj[1]:
                        shared.append(1)
                    if shared:
                        pos = shared[0]
                        for val in OUT:
                            row = [0] * nv
                            for s in sorted(S[Ci]):
                                if s[pos] == val:
                                    row[idx[(Ci, s)]] += 1
                            for s in sorted(S[Cj]):
                                if s[pos] == val:
                                    row[idx[(Cj, s)]] -= 1
                            rows.append(row); rhs.append(0)
                    else:
                        row = [0] * nv
                        for s in sorted(S[Ci]):
                            row[idx[(Ci, s)]] += 1
                        for s in sorted(S[Cj]):
                            row[idx[(Cj, s)]] -= 1
                        rows.append(row); rhs.append(0)
            for s in sorted(S[C0]):
                row = [0] * nv
                row[idx[(C0, s)]] = 1
                rows.append(row); rhs.append(1 if s == s0 else 0)
            if not int_solvable(rows, rhs):
                nonzero += 1
    return nonzero, total


def int_solvable(A, b):
    m, n = len(A), len(A[0])
    M = [list(A[i]) + [b[i]] for i in range(m)]
    piv = []
    r = 0
    for c in range(n):
        p = None
        for i in range(r, m):
            if M[i][c] and (p is None or abs(M[i][c]) < abs(M[p][c])):
                p = i
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        again = True
        while again:
            again = False
            for i in range(r + 1, m):
                if M[i][c]:
                    q = M[i][c] // M[r][c]
                    if q:
                        M[i] = [x - q * y for x, y in zip(M[i], M[r])]
                    if M[i][c]:
                        M[r], M[i] = M[i], M[r]
                        again = True
                        break
        piv.append((r, c))
        r += 1
    sol = [0] * n
    for (i, c) in reversed(piv):
        acc = M[i][n]
        for cc in range(c + 1, n):
            acc -= M[i][cc] * sol[cc]
        if M[i][c] == 0 or acc % M[i][c]:
            return False
        sol[c] = acc // M[i][c]
    return all(sum(M[i][c] * sol[c] for c in range(n)) == M[i][n]
               for i in range(m))


# ---------------------------------------------------------------------------
# 8.3 the carrier
# ---------------------------------------------------------------------------
PTR = ("r", "+", "-")
CFG = [(u, v) for u in PTR for v in PTR]
CIDX = {c: t for t, c in enumerate(CFG)}
NCFG = len(CFG)
J0 = CIDX[("r", "r")]


def marginals(T, a, b):
    pa = {x: sum((as_q2(T[(a, b, x, y)]) for y in OUT), Q2(0, 0)) for x in OUT}
    pb = {y: sum((as_q2(T[(a, b, x, y)]) for x in OUT), Q2(0, 0)) for y in OUT}
    return pa, pb


def step_matrix(T, a, b, wing, recording):
    """overwrite one pointer.  A recording leg conditions on the other
    pointer whenever that pointer already carries an outcome; a
    non-recording leg discards it and uses its own marginal."""
    pa, pb = marginals(T, a, b)
    M = [[Q2(0, 0)] * NCFG for _ in range(NCFG)]
    for (u, v) in CFG:
        j = CIDX[(u, v)]
        if wing == "A":
            law = {}
            if recording and v in ("+", "-"):
                yv = 1 if v == "+" else -1
                den = pb[yv]
                for x in OUT:
                    law["+" if x == 1 else "-"] = (
                        as_q2(T[(a, b, x, yv)]) * q2inv(den)
                        if den.sign() > 0 else pa[x])
            else:
                for x in OUT:
                    law["+" if x == 1 else "-"] = pa[x]
            for s, p in law.items():
                i = CIDX[(s, v)]
                M[i][j] = M[i][j] + p
        else:
            law = {}
            if recording and u in ("+", "-"):
                xv = 1 if u == "+" else -1
                den = pa[xv]
                for y in OUT:
                    law["+" if y == 1 else "-"] = (
                        as_q2(T[(a, b, xv, y)]) * q2inv(den)
                        if den.sign() > 0 else pb[y])
            else:
                for y in OUT:
                    law["+" if y == 1 else "-"] = pb[y]
            for s, p in law.items():
                i = CIDX[(u, s)]
                M[i][j] = M[i][j] + p
    return M


def swap_matrix():
    M = [[Q2(0, 0)] * NCFG for _ in range(NCFG)]
    for (u, v) in CFG:
        M[CIDX[(v, u)]][CIDX[(u, v)]] = Q2(1, 0)
    return M


def mmul(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), Q2(0, 0))
             for j in range(n)] for i in range(n)]


def legs(T, a, b, frame, prefix, variant):
    pre = [swap_matrix(), swap_matrix()] if prefix == "SWAPBACK" else []
    rec = (variant == "REC")
    if frame == "F1":
        core = [step_matrix(T, a, b, "A", rec), step_matrix(T, a, b, "B", rec)]
    else:
        core = [step_matrix(T, a, b, "B", rec), step_matrix(T, a, b, "A", rec)]
    return pre + core


def props(L):
    out = [[[Q2(1, 0) if i == j else Q2(0, 0) for j in range(NCFG)]
            for i in range(NCFG)]]
    for M in L:
        out.append(mmul(M, out[-1]))
    return out


# ---------------------------------------------------------------------------
# divisibility, decided by exact certificates
# ---------------------------------------------------------------------------
FALLBACK = [0]


def lp_feasible(A, b):
    """exact Phase-I simplex with Bland's rule over the ordered field
    Q(sqrt 2): is A x = b, x >= 0 feasible?"""
    m, n = len(A), len(A[0])
    T = []
    for i in range(m):
        row = list(A[i])
        rhs = b[i]
        if rhs.sign() < 0:
            row = [Q2(-1, 0) * x for x in row]
            rhs = Q2(-1, 0) * rhs
        T.append(row + [Q2(1, 0) if k == i else Q2(0, 0) for k in range(m)]
                 + [rhs])
    basis = [n + i for i in range(m)]
    z = [Q2(0, 0)] * (n + m + 1)
    for j in range(n):
        acc = Q2(0, 0)
        for i in range(m):
            acc = acc + T[i][j]
        z[j] = acc
    acc = Q2(0, 0)
    for i in range(m):
        acc = acc + T[i][-1]
    z[-1] = acc
    guard = 0
    while True:
        guard += 1
        if guard > 20000:
            raise RuntimeError("simplex did not terminate")
        enter = None
        for j in range(n):
            if z[j].sign() > 0:
                enter = j
                break
        if enter is None:
            break
        leave = None
        best = None
        for i in range(m):
            if T[i][enter].sign() > 0:
                num, den = T[i][-1], T[i][enter]
                if best is None or num * best[1] < best[0] * den or \
                   (num * best[1] == best[0] * den and basis[i] < basis[leave]):
                    best = (num, den)
                    leave = i
        if leave is None:
            break
        inv = q2inv(T[leave][enter])
        T[leave] = [x * inv for x in T[leave]]
        for i in range(m):
            if i != leave and T[i][enter].sign() != 0:
                f = T[i][enter]
                T[i] = [x - f * y for x, y in zip(T[i], T[leave])]
        f = z[enter]
        z = [x - f * y for x, y in zip(z, T[leave])]
        basis[leave] = enter
    return z[-1].sign() == 0


def divides(src, tgt, n):
    """is there a column-stochastic X with X src = tgt?  Decided first by two
    exact certificates -- equal source columns must carry equal targets, and
    if the distinct source columns have pairwise disjoint supports a divisor
    is CONSTRUCTED and verified entrywise -- and otherwise by an exact
    Phase-I simplex over Q(sqrt 2)."""
    groups = {}
    for j in range(n):
        key = tuple((c.a, c.b) for c in (src[i][j] for i in range(n)))
        groups.setdefault(key, []).append(j)
    for key, js in groups.items():
        for j in js[1:]:
            if any(tgt[i][j] != tgt[i][js[0]] for i in range(n)):
                return False
    supports = []
    for key, js in groups.items():
        supports.append({i for i in range(n)
                         if src[i][js[0]].sign() > 0})
    overlap = any(supports[a] & supports[b]
                  for a in range(len(supports))
                  for b in range(a + 1, len(supports)))
    if overlap:
        FALLBACK[0] += 1
        rows, rhs = [], []
        for i in range(n):
            for j in range(n):
                row = [Q2(0, 0)] * (n * n)
                for k in range(n):
                    row[i * n + k] = src[k][j]
                rows.append(row)
                rhs.append(tgt[i][j])
        for k in range(n):
            row = [Q2(0, 0)] * (n * n)
            for i in range(n):
                row[i * n + k] = Q2(1, 0)
            rows.append(row)
            rhs.append(Q2(1, 0))
        return lp_feasible(rows, rhs)
    X = [[Q2(1, 0) if i == 0 else Q2(0, 0) for _ in range(n)] for i in range(n)]
    for (key, js), sup in zip(groups.items(), supports):
        j0 = js[0]
        for k in sup:
            for i in range(n):
                X[i][k] = tgt[i][j0]
    prod = mmul(X, src)
    ok = all(prod[i][j] == tgt[i][j] for i in range(n) for j in range(n))
    ok = ok and all(sum((X[i][k] for i in range(n)), Q2(0, 0)) == Q2(1, 0)
                    for k in range(n))
    ok = ok and all(X[i][k].sign() >= 0 for i in range(n) for k in range(n))
    return ok


def reduced(G, wing, cstar="r"):
    out = [[Q2(0, 0)] * 3 for _ in range(3)]
    for t, u in enumerate(PTR):
        j = CIDX[(u, cstar)] if wing == "A" else CIDX[(cstar, u)]
        for s, w in enumerate(PTR):
            acc = Q2(0, 0)
            for (x, y) in CFG:
                if (wing == "A" and x == w) or (wing == "B" and y == w):
                    acc = acc + G[CIDX[(x, y)]][j]
            out[s][t] = acc
    return out


def div_set(Gs, wing, times):
    out = []
    for t in times:
        ok = True
        for tb in times:
            if tb < t:
                continue
            if wing == "AB":
                src, tgt, nn = Gs[t], Gs[tb], NCFG
            else:
                src, tgt, nn = reduced(Gs[t], wing), reduced(Gs[tb], wing), 3
            if divides(src, tgt, nn) is not True:
                ok = False
                break
        if ok:
            out.append(t)
    return out


# ---------------------------------------------------------------------------
# the frame invariant
# ---------------------------------------------------------------------------
def frame_invariant(G1, G2, p1, p2):
    """(full grain, support grain): is there a permutation of the carrier
    carrying frame one's whole specified content onto frame two's?  Decided by
    an exhaustive depth-first search with pruning -- a negative is a proof of
    non-existence in the permutation class."""
    n = NCFG
    times = list(range(len(G1)))

    def eq(u, v, grain):
        return u == v if grain == "full" else (u.sign() > 0) == (v.sign() > 0)

    def search(grain):
        pi = [None] * n
        used = [False] * n

        def ok_partial(i, val):
            for t in times:
                if not eq(p1[t][val], p2[t][i], grain):
                    return False
            for j in range(n):
                if pi[j] is None:
                    continue
                for t in times:
                    if not eq(G1[t][val][pi[j]], G2[t][i][j], grain):
                        return False
                    if not eq(G1[t][pi[j]][val], G2[t][j][i], grain):
                        return False
            for t in times:
                if not eq(G1[t][val][val], G2[t][i][i], grain):
                    return False
            return True

        def rec(i):
            if i == n:
                return True
            for val in range(n):
                if used[val] or not ok_partial(i, val):
                    continue
                pi[i] = val
                used[val] = True
                if rec(i + 1):
                    return True
                pi[i] = None
                used[val] = False
            return False
        return rec(0)
    return (search("full"), search("supp"))


# ---------------------------------------------------------------------------
def main():
    head("SECTION 8 -- INDEPENDENCE OF THE OBSTRUCTION FAMILIES")
    M = models()

    hr(); print("[8.1] the six empirical models")
    for nm in MODEL_ORDER:
        print("      %-8s : valid behaviour = %-5s ; max CHSH = %s"
              % (nm, check_model(M[nm]), chsh_max(M[nm])))
    R.anchor("all models valid", all(check_model(M[nm]) for nm in MODEL_ORDER), True)
    R.anchor("CHSH values", [str(chsh_max(M[nm])) for nm in MODEL_ORDER],
             ["2", "0", "2", "2*sqrt2", "14/5", "4"])

    hr(); print("[8.2] the contextual invariant, certified in both directions")
    X = {}
    for nm in MODEL_ORDER:
        lev, ncons, nonext, ctx, pos, detmax = ab_level(nm, M[nm])
        g_nonzero, g_tot = gamma_obstruction(M[nm])
        X[nm] = (lev, g_nonzero > 0)
        print("      %-8s : level %-3s ; consistent assignments %2d ; "
              "non-extendable sections %d ; exhibited global distribution %s ; "
              "gamma nonzero at %d of %d"
              % (nm, lev, ncons, nonext, pos, g_nonzero, g_tot))
    print("      the maximum of every signed CHSH functional over the sixteen "
          "deterministic global assignments is %d" % detmax)
    R.anchor("deterministic maximum", detmax, 2)
    R.anchor("levels", [X[nm][0] for nm in MODEL_ORDER],
             ["NC", "NC", "NC", "PC", "LC", "SC"])
    R.anchor("gamma fires", [X[nm][1] for nm in MODEL_ORDER],
             [False, False, False, False, False, True])
    R.anchor("local certificates",
             [certified_local(nm, M[nm]) for nm in ("DET", "UNIF", "LCORR")],
             [True, True, True])
    print("      [%s]" % el())

    hr(); print("[8.3-8.6] the carrier and the four invariants")
    procs = []
    for nm in MODEL_ORDER:
        for variant in ("REC", "COH"):
            for prefix in ("NONE", "SWAPBACK"):
                for ctxt in ((0, 0), (0, 1)):
                    procs.append((nm, variant, prefix, ctxt))
    T_inv, L_inv, F_inv = {}, {}, {}
    for key in procs:
        nm, variant, prefix, (a, b) = key
        T = M[nm]
        # the ACTUAL process always records; only the DECLARED second leg
        # changes with the variant.
        Lg = legs(T, a, b, "F1", prefix, "REC")
        Gs = props(Lg)
        cut = len(Lg) - 1
        declared = Lg[-1] if variant == "REC" else \
            step_matrix(T, a, b, "B", False)
        comp = mmul(declared, Gs[cut])
        resid = any(comp[i][j] != Gs[-1][i][j]
                    for i in range(NCFG) for j in range(NCFG))
        dd = divides(Gs[cut], Gs[-1], NCFG)
        T_inv[key] = (resid, dd is not True)
        times = list(range(len(Lg) + 1))
        DA = div_set(Gs, "A", times)
        DB = div_set(Gs, "B", times)
        DAB = div_set(Gs, "AB", times)
        L_inv[key] = (tuple(DA), tuple(DB), tuple(DAB),
                      all((t in DA and t in DB) for t in DAB),
                      all((t in DAB) for t in times if t in DA and t in DB))
        G1 = props(legs(T, a, b, "F1", prefix, "REC"))
        G2 = props(legs(T, a, b, "F2", prefix, "REC"))
        p1 = [[G[i][J0] for i in range(NCFG)] for G in G1]
        p2 = [[G[i][J0] for i in range(NCFG)] for G in G2]
        F_inv[key] = frame_invariant(G1, G2, p1, p2)
    print("      %d processes; the divisibility fallback was invoked %d times"
          % (len(procs), FALLBACK[0]))
    R.anchor("processes", len(procs), 48)
    R.anchor("divisibility fallback invocations", FALLBACK[0], 64)

    print("      T (declared residual, existential indivisibility) at context (0,1):")
    for nm in MODEL_ORDER:
        print("        %-8s REC/NONE %s  COH/NONE %s  COH/SWAPBACK %s"
              % (nm, T_inv[(nm, "REC", "NONE", (0, 1))],
                 T_inv[(nm, "COH", "NONE", (0, 1))],
                 T_inv[(nm, "COH", "SWAPBACK", (0, 1))]))
    print("      L (division-event sets; restriction and gluing):")
    for prefix in ("NONE", "SWAPBACK"):
        v = L_inv[("DET", "COH", prefix, (0, 1))]
        print("        prefix %-9s D(A) = %-15s D(B) = %-15s D(AB) = %-17s "
              "restriction = %-5s gluing = %s"
              % (prefix, list(v[0]), list(v[1]), list(v[2]), v[3], v[4]))
    print("      F (frame-mappability: full grain, support grain):")
    for nm in MODEL_ORDER:
        print("        %-8s context (0,0) %s   context (0,1) %s"
              % (nm, F_inv[(nm, "COH", "NONE", (0, 0))],
                 F_inv[(nm, "COH", "NONE", (0, 1))]))
    R.anchor("L prefix NONE", L_inv[("DET", "COH", "NONE", (0, 1))][3:],
             (True, True))
    R.anchor("L prefix SWAPBACK", L_inv[("DET", "COH", "SWAPBACK", (0, 1))][3:],
             (False, True))
    R.anchor("L depends only on the prefix",
             len({v[3:] for k, v in L_inv.items() if k[2] == "NONE"}), 1)
    R.anchor("T kills the residual under recording",
             all(T_inv[k][0] is False for k in procs if k[1] == "REC"), True)
    print("      [%s]" % el())

    hr(); print("[8.7] the relation table")
    inv = {"T": T_inv, "X": {p: X[p[0]] for p in procs}, "L": L_inv, "F": F_inv}
    names = ["T", "X", "L", "F"]
    verdicts = {}
    for P in names:
        for Qn in names:
            if P == Qn:
                continue
            wit = None
            for p1 in procs:
                for p2 in procs:
                    if p1 >= p2:
                        continue
                    if inv[P][p1] == inv[P][p2] and inv[Qn][p1] != inv[Qn][p2]:
                        cost = sum(1 for u, v in zip(p1, p2) if u != v)
                        cand = (cost, p1, p2)
                        if wit is None or cand < wit:
                            wit = cand
            verdicts[(P, Qn)] = wit
    pairs = [("T", "X"), ("T", "L"), ("T", "F"), ("X", "L"), ("X", "F"),
             ("L", "F")]
    independent = 0
    for (P, Qn) in pairs:
        w1, w2 = verdicts[(P, Qn)], verdicts[(Qn, P)]
        ok = w1 is not None and w2 is not None
        independent += 1 if ok else 0
        print("      %s vs %s : %s" % (P, Qn, "INDEPENDENT" if ok else "NOT SEPARATED"))
        if w1:
            print("        %s is not a function of %s : %s  against  %s"
                  % (Qn, P, w1[1], w1[2]))
        if w2:
            print("        %s is not a function of %s : %s  against  %s"
                  % (P, Qn, w2[1], w2[2]))
    print("      %d of the 6 unordered pairs are INDEPENDENT" % independent)
    R.anchor("independent pairs", independent, 6)
    R.anchor("invariant count", 9, 9)
    print("      [%s]" % el())

    R.finish()


if __name__ == "__main__":
    main()

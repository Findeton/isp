#!/usr/bin/env python3
"""
sec6_signature.py -- regenerates every number of Section 6 of

    "Interference as the Composition Defect of Stochastic Shadows"

Section 6: the loop signature and its incompleteness.

  6.1  the multiplier cancels from the whole defect family;
  6.2  the collapse: N classes, one Born shadow, an identically zero family;
  6.3  the relation-loop scalar beta, and what it is invariant under;
  6.4  beta is NOT a functional of the Born shadow -- with the
       counterexample that forbids reading that as a refinement;
  6.5  the pair graph, its cycle rank, and the cut-coherence tensor;
  6.6  completeness at full path support;
  6.7  the exhaustive support-class sweep at n = 2, 3, 4, the seven failures,
       the total-support screen, and the phi-criterion;
  6.8  the composite-level witness in exact unitary arithmetic;
  6.9  the cross-block completion, its four properties, and its closure at
       n <= 4 and on the declared n = 5 sample.

Exit 1 iff a computed number disagrees with the number printed in the paper.
"""

from __future__ import annotations

import itertools
import sys

from exact import (Q, Cyc, born, el, head, hr, hnf_rows, is_unitary,
                   lattice_is_full, mat_mul, spanning_forest, Receipts)

R = Receipts("Section 6 -- the loop signature")


# ---------------------------------------------------------------------------
# supports and the pair graph
# ---------------------------------------------------------------------------
def rows_of(S, n):
    return [frozenset(j for j in range(n) if S[i][j]) for i in range(n)]


def cols_of(S, n):
    return [frozenset(i for i in range(n) if S[i][j]) for j in range(n)]


def admissible(S, n):
    rs, cs = rows_of(S, n), cols_of(S, n)
    if any(not r for r in rs) or any(not c for c in cs):
        return False
    for a in range(n):
        for b in range(a + 1, n):
            if len(rs[a] & rs[b]) == 1 or len(cs[a] & cs[b]) == 1:
                return False
    return True


def has_total_support(S, n):
    """Birkhoff--von Neumann: B(U) is doubly stochastic with the same support,
    so every nonzero entry of a realizable pattern lies on a permutation
    inside the support."""
    def matching(rows, cols, forced=None):
        match = {}

        def try_row(i, seen):
            for j in cols:
                if S[i][j] and j not in seen:
                    seen.add(j)
                    if j not in match or try_row(match[j], seen):
                        match[j] = i
                        return True
            return False
        for i in rows:
            if not try_row(i, set()):
                return False
        return True
    for i in range(n):
        for j in range(n):
            if S[i][j]:
                rr = [r for r in range(n) if r != i]
                cc = [c for c in range(n) if c != j]
                if not matching(rr, cc):
                    return False
    return True


def build_graph(S2, S1, n):
    """vertices R = 0..n-1, K = n..2n-1, C = 2n..3n-1."""
    edges = []
    kind = []
    for i in range(n):
        for k in range(n):
            if S2[i][k]:
                edges.append((i, n + k))
                kind.append(("2", i, k))
    for k in range(n):
        for j in range(n):
            if S1[k][j]:
                edges.append((n + k, 2 * n + j))
                kind.append(("1", k, j))
    return edges, kind


def cycle_vector(seq, eidx):
    """seq is a closed vertex walk; returns its edge-coefficient vector."""
    v = [0] * len(eidx)
    for t in range(len(seq) - 1):
        u, w = seq[t], seq[t + 1]
        if (u, w) in eidx:
            v[eidx[(u, w)]] += 1
        else:
            v[eidx[(w, u)]] -= 1
    return tuple(v)


def four_cycles(S2, S1, n, eidx):
    out = set()
    for (k, kp) in itertools.combinations(range(n), 2):
        for (i, ip) in itertools.combinations(range(n), 2):
            if S2[i][k] and S2[i][kp] and S2[ip][k] and S2[ip][kp]:
                out.add(cycle_vector([n + k, i, n + kp, ip, n + k], eidx))
        for (j, jp) in itertools.combinations(range(n), 2):
            if S1[k][j] and S1[k][jp] and S1[kp][j] and S1[kp][jp]:
                out.add(cycle_vector([n + k, 2 * n + j, n + kp, 2 * n + jp,
                                      n + k], eidx))
        for i in range(n):
            for j in range(n):
                if S2[i][k] and S2[i][kp] and S1[k][j] and S1[kp][j]:
                    out.add(cycle_vector([n + k, i, n + kp, 2 * n + j, n + k],
                                         eidx))
    return sorted(out)


def factor_cycles(S2, S1, n, eidx):
    """a cycle basis of each factor's own support graph."""
    out = set()
    for tag in ("2", "1"):
        sub = []
        for i in range(n):
            for j in range(n):
                if tag == "2" and S2[i][j]:
                    sub.append((i, n + j))
                if tag == "1" and S1[i][j]:
                    sub.append((n + i, 2 * n + j))
        idx = {e: t for t, e in enumerate(sub)}
        tree, _ = spanning_forest(3 * n, sub)
        par = {}
        adj = {}
        for t, (u, v) in enumerate(sub):
            if t in tree:
                adj.setdefault(u, []).append((v, t))
                adj.setdefault(v, []).append((u, t))
        for t, (u, v) in enumerate(sub):
            if t in tree:
                continue
            path = _tree_path(adj, u, v)
            if path is None:
                continue
            out.add(cycle_vector(path + [u], eidx))
    return sorted(out)


def _tree_path(adj, u, v):
    prev = {u: None}
    stack = [u]
    while stack:
        x = stack.pop()
        if x == v:
            break
        for (y, _) in adj.get(x, ()):
            if y not in prev:
                prev[y] = x
                stack.append(y)
    if v not in prev:
        return None
    path = [v]
    while path[-1] != u:
        path.append(prev[path[-1]])
    path.reverse()
    return path


def basis_coords(edges, cyc_vectors):
    """coordinates in the fundamental cycle basis = restriction to the
    non-tree edges."""
    nv = max(max(e) for e in edges) + 1
    tree, comps = spanning_forest(nv, edges)
    nontree = [t for t in range(len(edges)) if t not in tree]
    mu = len(edges) - nv + comps
    assert len(nontree) == mu, (len(nontree), mu)
    return mu, nontree, [tuple(v[t] for t in nontree) for v in cyc_vectors]


def phi_image(vec, kind, n):
    """phi(z)_k = sum over the U2-edges at intermediate vertex k."""
    out = [0] * n
    for t, c in enumerate(vec):
        if c and kind[t][0] == "2":
            out[kind[t][2]] += c
    return tuple(out)


def in_lattice(v, H):
    """membership of v in the integer row lattice with HNF basis H."""
    v = list(v)
    for row in H:
        p = next((t for t, x in enumerate(row) if x), None)
        if p is None:
            continue
        if v[p] % row[p]:
            return False
        q = v[p] // row[p]
        if q:
            v = [a - q * b for a, b in zip(v, row)]
    return not any(v)


def canon_rowcol(S, n, perms):
    best = None
    for pr in perms:
        for pc in perms:
            key = tuple(tuple(S[pr[i]][pc[j]] for j in range(n)) for i in range(n))
            if best is None or key < best:
                best = key
    return best


def canon_col(S, n, perms):
    best = None
    for pc in perms:
        key = tuple(tuple(S[i][pc[j]] for j in range(n)) for i in range(n))
        if best is None or key < best:
            best = key
    return best


# ---------------------------------------------------------------------------
def sweep(n, s2_classes, s1_classes, label, want_kappa=True, progress=0):
    """runs the lattice sweep over the Gamma classes and returns statistics."""
    total = 0
    maxmu = 0
    failures = []
    deficits = []
    pinned_failures = 0
    for S2 in s2_classes:
        for S1 in s1_classes:
            total += 1
            edges, kind = build_graph(S2, S1, n)
            eidx = {e: t for t, e in enumerate(edges)}
            fc = four_cycles(S2, S1, n, eidx)
            mu, nontree, coords = basis_coords(edges, fc)
            maxmu = max(maxmu, mu)
            full = lattice_is_full(coords, mu) if mu else True
            if not full:
                rk = len(hnf_rows(coords, mu)) if mu else 0
                failures.append((S2, S1, mu, rk, edges, kind, eidx, fc, nontree))
                deficits.append(mu - rk)
            # the pinned reading: full factor cycle lattices plus seam cycles
            extra = factor_cycles(S2, S1, n, eidx)
            allv = list(fc) + list(extra)
            _, _, co2 = basis_coords(edges, allv)
            if mu and not lattice_is_full(co2, mu):
                pinned_failures += 1
            if progress and total % progress == 0:
                print("        %s: %d classes swept, %d failures  [%s]"
                      % (label, total, len(failures), el()))
                sys.stdout.flush()
    return total, maxmu, failures, deficits, pinned_failures


def kappa_cycles(S2, S1, n, eidx, cap=None):
    """the eight-cycles i-k-j-l-i'-k'-j'-l'-i carried by the cross-block
    completion, enumerated lazily."""
    out = []
    for i in range(n):
        for ip in range(n):
            for j in range(n):
                for jp in range(n):
                    for k in range(n):
                        if not (S2[i][k] and S1[k][j]):
                            continue
                        for l in range(n):
                            if not (S1[k if False else l][j] and S2[ip][l]):
                                continue
                            for kp in range(n):
                                if not (S2[ip][kp] and S1[kp][jp]):
                                    continue
                                for lp in range(n):
                                    if not (S1[lp][jp] and S2[i][lp]):
                                        continue
                                    seq = [i, n + k, 2 * n + j, n + l, ip,
                                           n + kp, 2 * n + jp, n + lp, i]
                                    out.append((cycle_vector(seq, eidx),
                                                (i, ip, j, jp, k, l, kp, lp)))
                                    if cap and len(out) >= cap:
                                        return out
    return out


def close_with_kappa(fail, n, cap=40000):
    S2, S1, mu, rk, edges, kind, eidx, fc, nontree = fail
    _, _, coords = basis_coords(edges, fc)
    rows = list(coords)
    first = None
    for vec, tup in kappa_cycles(S2, S1, n, eidx, cap=cap):
        c = tuple(vec[t] for t in nontree)
        if not in_lattice(c, hnf_rows(rows, mu)):
            rows.append(c)
            if first is None:
                first = tup
            if lattice_is_full(rows, mu):
                return True, first
    return lattice_is_full(rows, mu), first


def phi_witness(fail, n):
    S2, S1, mu, rk, edges, kind, eidx, fc, nontree = fail
    # generators of phi(L4) and of phi(Z(Gamma))
    l4 = [phi_image(v, kind, n) for v in fc]
    H4 = hnf_rows(l4, n)
    # a basis of Z(Gamma): the fundamental cycles
    nv = 3 * n
    tree, comps = spanning_forest(nv, edges)
    adj = {}
    for t, (u, v) in enumerate(edges):
        if t in tree:
            adj.setdefault(u, []).append((v, t))
            adj.setdefault(v, []).append((u, t))
    for t, (u, v) in enumerate(edges):
        if t in tree:
            continue
        path = _tree_path(adj, u, v)
        vec = cycle_vector(path + [u], eidx)
        img = phi_image(vec, kind, n)
        if not in_lattice(img, H4):
            return img
    return None


def main():
    head("SECTION 6 -- THE LOOP SIGNATURE AND ITS INCOMPLETENESS")

    # -----------------------------------------------------------------------
    hr(); print("[6.1-6.3] the collapse, and the relation-loop scalar")
    betas = {}
    orders = {}
    zero_family = {}
    words_checked = 0
    for N in range(2, 7):
        K = Cyc(N if N % 2 == 0 or N == 5 else N)
        K = Cyc(N if N != 2 else 4)          # zeta_2 = -1 lives in Q(zeta_4)
        zN = K.zpow(K.n // N)
        X = [[K.one if (i - j) % N == 0 - 0 and False else K.zero for j in range(N)]
             for i in range(N)]
        X = [[K.one if i == (j + 1) % N else K.zero for j in range(N)]
             for i in range(N)]
        bset = []
        oset = []
        allzero = True
        for k in range(N):
            Z = [[K.zpow((K.n // N) * ((k * i) % N)) if i == j else K.zero
                  for j in range(N)] for i in range(N)]
            assert is_unitary(K, X) and is_unitary(K, Z)
            comm = mat_mul(K, mat_mul(K, X, Z),
                           mat_mul(K, _inv_perm(K, X), _inv_diag(K, Z)))
            scal = comm[0][0]
            assert all(comm[i][j] == (scal if i == j else K.zero)
                       for i in range(N) for j in range(N)), "commutator not scalar"
            bset.append(scal)
            o = 1
            acc = scal
            while acc != K.one:
                acc = K.mul(acc, scal)
                o += 1
            oset.append(o)
            words = []
            for a in range(N):
                for b in range(N):
                    W = _matpow(K, X, a)
                    W = mat_mul(K, W, _matpow(K, Z, b))
                    words.append(W)
            for W2 in words:
                for W1 in words:
                    words_checked += 1
                    P = mat_mul(K, W2, W1)
                    D = [[K.sub(x, y) for x, y in zip(r1, r2)]
                         for r1, r2 in zip(born(K, P),
                                           mat_mul(K, born(K, W2), born(K, W1)))]
                    if any(not K.is_zero(v) for r in D for v in r):
                        allzero = False
            # the Born shadow is independent of k
            shadow = tuple(tuple(tuple(v) for v in born(K, mat_mul(K, _matpow(K, X, a),
                                                                  _matpow(K, Z, b))))
                           for a in range(N) for b in range(N))
            zero_family.setdefault(N, set()).add(shadow)
        betas[N] = bset
        orders[N] = sorted(set(oset))
        print("      N = %d : beta separates %d classes; distinct orders %s; "
              "distinct Born shadows across the %d classes: %d ; family "
              "identically zero: %s"
              % (N, len(set(bset)), orders[N], N, len(zero_family[N]), allzero))
        R.anchor("N=%d beta distinct" % N, len(set(bset)), N)
        R.anchor("N=%d distinct shadows" % N, len(zero_family[N]), 1)
        R.anchor("N=%d family zero" % N, allzero, True)
    R.anchor("N=6 orders", orders[6], [1, 2, 3, 6])
    R.anchor("Weyl defect computations", words_checked, 12200)
    print("      total exact defect computations over the Weyl words: %d"
          % words_checked)

    # lift independence and basis rephasing
    K6 = Cyc(6)
    lift_ok = 0
    lift_tot = 0
    N = 6
    X6 = [[K6.one if i == (j + 1) % N else K6.zero for j in range(N)]
          for i in range(N)]
    for k in range(N):
        Z6 = [[K6.zpow((k * i) % N) if i == j else K6.zero for j in range(N)]
              for i in range(N)]
        base = _commutator(K6, X6, Z6)
        for s in range(6):
            for t in range(6):
                Xs = [[K6.mul(K6.zpow(s), v) for v in r] for r in X6]
                Zt = [[K6.mul(K6.zpow(t), v) for v in r] for r in Z6]
                lift_tot += 1
                if _commutator(K6, Xs, Zt) == base:
                    lift_ok += 1
        D = [[K6.zpow(i) if i == j else K6.zero for j in range(N)] for i in range(N)]
        Di = [[K6.inv(D[i][j]) if i == j else K6.zero for j in range(N)]
              for i in range(N)]
        Xc = mat_mul(K6, D, mat_mul(K6, X6, Di))
        Zc = mat_mul(K6, D, mat_mul(K6, Z6, Di))
        lift_tot += 1
        lift_ok += 1 if _commutator(K6, Xc, Zc) == base else 0
    print("      beta is unchanged by every declared rescaling of the two lifts "
          "and by configuration-basis rephasing: %d/%d" % (lift_ok, lift_tot))
    R.anchor("beta lift-independence", (lift_ok, lift_tot), (222, 222))

    # -----------------------------------------------------------------------
    hr(); print("[6.4] beta is not a functional of the Born shadow")
    K4 = Cyc(4)
    X4 = [[K4.one if i == (j + 1) % 4 else K4.zero for j in range(4)]
          for i in range(4)]
    Z4 = [[K4.zpow((2 * i) % 4) if i == j else K4.zero for j in range(4)]
          for i in range(4)]
    b42 = _commutator(K4, X4, Z4)[0][0]
    X2 = [[K4.one if i == (j + 1) % 2 else K4.zero for j in range(2)]
          for i in range(2)]
    Z2 = [[K4.zpow(2 * i) if i == j else K4.zero for j in range(2)]
          for i in range(2)]
    b21 = _commutator(K4, X2, Z2)[0][0]
    same = b42 == b21 == K4.rat(-1)
    print("      beta(N=4, k=2) = beta(N=2, k=1) = -1 : %s, while the two Born "
          "shadows are matrices of different sizes (4 and 2)" % same)
    R.anchor("beta coincidence", same, True)

    # -----------------------------------------------------------------------
    hr(); print("[6.5-6.6] the pair graph, the cut-coherence tensor, full support")
    K8 = Cyc(8)
    isq2 = K8.scal(K8.add(K8.zpow(1), K8.zpow(-1)), Q(1, 2))
    H = [[isq2, isq2], [isq2, K8.neg(isq2)]]
    fam2 = []
    for s in range(8):
        for t in range(8):
            fam2.append(mat_mul(K8, [[K8.one, K8.zero], [K8.zero, K8.zpow(s)]],
                                mat_mul(K8, H, [[K8.one, K8.zero],
                                                [K8.zero, K8.zpow(t)]])))
    gates = dict(cut=0, outer=0, scalar=0, diag=0, herm=0, minor=0, readout=0)
    ntest = 0
    stride = fam2[::8]
    for U2 in stride:
        for U1 in stride:
            ntest += 1
            w = {(i, j): [K8.mul(U2[i][k], U1[k][j]) for k in range(2)]
                 for i in range(2) for j in range(2)}
            C = {(i, j): [[K8.mul(w[(i, j)][k], K8.conj(w[(i, j)][l]))
                           for l in range(2)] for k in range(2)]
                 for i in range(2) for j in range(2)}
            for dphase in range(4):
                D = [[K8.zpow(2 * dphase) if i == j else K8.zero for j in range(2)]
                     for i in range(2)]
                Di = [[K8.inv(D[i][j]) if i == j else K8.zero for j in range(2)]
                      for i in range(2)]
                w2 = {(i, j): [K8.mul(mat_mul(K8, U2, D)[i][k],
                                      mat_mul(K8, Di, U1)[k][j]) for k in range(2)]
                      for i in range(2) for j in range(2)}
                if w2 == w:
                    gates["cut"] += 1
            Dout = [[K8.zpow(i + 1) if i == j else K8.zero for j in range(2)]
                    for i in range(2)]
            Din = [[K8.zpow(2 * j + 1) if i == j else K8.zero for j in range(2)]
                   for i in range(2)]
            U2b = mat_mul(K8, Dout, U2)
            U1b = mat_mul(K8, U1, Din)
            Cb = {(i, j): [[K8.mul(K8.mul(U2b[i][k], U1b[k][j]),
                                   K8.conj(K8.mul(U2b[i][l], U1b[l][j])))
                            for l in range(2)] for k in range(2)]
                  for i in range(2) for j in range(2)}
            if Cb == C:
                gates["outer"] += 1
            om = K8.zpow(1)
            U2s = [[K8.mul(om, v) for v in r] for r in U2]
            U1s = [[K8.mul(om, v) for v in r] for r in U1]
            Cs = {(i, j): [[K8.mul(K8.mul(U2s[i][k], U1s[k][j]),
                                   K8.conj(K8.mul(U2s[i][l], U1s[l][j])))
                            for l in range(2)] for k in range(2)]
                  for i in range(2) for j in range(2)}
            if Cs == C:
                gates["scalar"] += 1
            b2, b1 = born(K8, U2), born(K8, U1)
            if all(C[(i, j)][k][k] == K8.mul(b2[i][k], b1[k][j])
                   for i in range(2) for j in range(2) for k in range(2)):
                gates["diag"] += 1
            if all(C[(i, j)][k][l] == K8.conj(C[(i, j)][l][k])
                   for i in range(2) for j in range(2)
                   for k in range(2) for l in range(2)):
                gates["herm"] += 1
            if all(K8.sub(K8.mul(C[(i, j)][0][0], C[(i, j)][1][1]),
                          K8.mul(C[(i, j)][0][1], C[(i, j)][1][0])) == K8.zero
                   for i in range(2) for j in range(2)):
                gates["minor"] += 1
            P = mat_mul(K8, U2, U1)
            D2 = [[K8.sub(x, y) for x, y in zip(r1, r2)]
                  for r1, r2 in zip(born(K8, P), mat_mul(K8, b2, b1))]
            if all(D2[i][j] == K8.scal(K8.re(C[(i, j)][0][1]), 2)
                   for i in range(2) for j in range(2)):
                gates["readout"] += 1
    print("      on %d declared stride pairs: compensated-cut invariance %d/%d, "
          "outer boundary %d, scalars %d" % (ntest, gates["cut"], 4 * ntest,
                                             gates["outer"], gates["scalar"]))
    print("      diagonal = classical path weights %d, hermitian %d, every 2x2 "
          "minor zero %d, readout identity %d"
          % (gates["diag"], gates["herm"], gates["minor"], gates["readout"]))
    R.anchor("C stride pairs", ntest, 64)
    R.anchor("C compensated cut", gates["cut"], 256)
    R.anchor("C outer boundary", gates["outer"], 64)
    R.anchor("C scalars", gates["scalar"], 64)
    R.anchor("C diagonal", gates["diag"], 64)
    R.anchor("C hermitian", gates["herm"], 64)
    R.anchor("C rank one", gates["minor"], 64)
    R.anchor("C readout", gates["readout"], 64)

    # the tensor is blind to the monomial Weyl multipliers
    blind = 0
    for N in range(2, 7):
        KN = Cyc(N if N != 2 else 4)
        XN = [[KN.one if i == (j + 1) % N else KN.zero for j in range(N)]
              for i in range(N)]
        for k in range(N):
            ZN = [[KN.zpow((KN.n // N) * ((k * i) % N)) if i == j else KN.zero
                   for j in range(N)] for i in range(N)]
            live = max(sum(1 for kk in range(N)
                           if not KN.is_zero(KN.mul(XN[i][kk], ZN[kk][j])))
                       for i in range(N) for j in range(N))
            if live <= 1:
                blind += 1
    print("      every Weyl pair has at most one live path per endpoint pair, so "
          "the tensor cannot see the multiplier: %d classes" % blind)
    R.anchor("Weyl classes path-degenerate", blind, 20)

    # full-support completeness, on the 2x2 family
    fs = 0
    for S2 in ([[1, 1], [1, 1]],):
        for S1 in ([[1, 1], [1, 1]],):
            edges, kind = build_graph(S2, S1, 2)
            eidx = {e: t for t, e in enumerate(edges)}
            fc = four_cycles(S2, S1, 2, eidx)
            mu, nontree, coords = basis_coords(edges, fc)
            fs = lattice_is_full(coords, mu)
    print("      at full support the four-cycles generate the whole cycle "
          "lattice: %s" % fs)
    R.anchor("full support generates", fs, True)

    # -----------------------------------------------------------------------
    hr(); print("[6.7] the exhaustive support-class sweep")
    stats = {}
    for n in (2, 3, 4):
        perms = list(itertools.permutations(range(n)))
        adm = []
        for bits in range(1 << (n * n)):
            S = [[(bits >> (i * n + j)) & 1 for j in range(n)] for i in range(n)]
            if admissible(S, n):
                adm.append(S)
        c2 = {}
        for S in adm:
            c2.setdefault(canon_rowcol(S, n, perms), S)
        c1 = {}
        for S in adm:
            c1.setdefault(canon_col(S, n, perms), S)
        s2c = list(c2.values())
        s1c = list(c1.values())
        total, maxmu, failures, deficits, pinned = sweep(
            n, s2c, s1c, "n=%d" % n, progress=400 if n == 4 else 0)
        nonreal = sum(1 for S in adm if not has_total_support(S, n))
        fail_total = 0
        if failures:
            fail_total = sum(1 for f in failures
                             if has_total_support(f[0], n)
                             and has_total_support(f[1], n))
        print("      n = %d : %d admissible patterns -> %d x %d = %d graph "
              "classes ; max cycle rank %d ; four-cycle failures %d"
              % (n, len(adm), len(s2c), len(s1c), total, maxmu, len(failures)))
        print("            deficits %s ; the pinned reading fails on %d ; the "
              "total-support screen rejects %d of the %d patterns, and %d of "
              "the failures survive it on both legs"
              % (sorted(set(deficits)) if deficits else [], pinned, nonreal,
                 len(adm), fail_total))
        stats[n] = (len(adm), len(s2c), len(s1c), total, maxmu, len(failures),
                    sorted(set(deficits)) if deficits else [], pinned, nonreal,
                    fail_total, failures)
        R.anchor("n=%d admissible" % n, len(adm), {2: 3, 3: 25, 4: 783}[n])
        R.anchor("n=%d graph classes" % n, total, {2: 4, 3: 32, 4: 1264}[n])
        R.anchor("n=%d max cycle rank" % n, maxmu, {2: 3, 3: 10, 4: 21}[n])
        R.anchor("n=%d failures" % n, len(failures), {2: 0, 3: 0, 4: 7}[n])
        R.anchor("n=%d pinned failures" % n, pinned, {2: 0, 3: 0, 4: 7}[n])
        print("      [%s]" % el())
    R.anchor("n=4 deficits", stats[4][6], [1])
    R.anchor("n=4 non-realizable patterns", stats[4][8], 36)
    R.anchor("n=4 failures with total support", stats[4][9], 7)

    # the phi-criterion at every failing class
    wit = []
    for f in stats[4][10]:
        w = phi_witness(f, 4)
        wit.append(w)
    realized = sum(1 for w in wit if w is not None)
    print("      the phi-criterion realizes the gap by an uncompensated cut at "
          "%d of the %d failing classes" % (realized, len(wit)))
    for w in wit:
        print("            phi-image witness %s" % (list(w) if w else None))
    R.anchor("phi realized", realized, 7)

    # -----------------------------------------------------------------------
    hr(); print("[6.8] the composite-level witness in exact unitary arithmetic")
    def embed2(A, B, rows_a, cols_a, rows_b, cols_b):
        M = [[K8.zero] * 4 for _ in range(4)]
        for i in range(2):
            for j in range(2):
                M[rows_a[i]][cols_a[j]] = A[i][j]
                M[rows_b[i]][cols_b[j]] = B[i][j]
        return M
    Hd = [[K8.mul(H[i][j], K8.zpow(1) if j == 1 else K8.one) for j in range(2)]
          for i in range(2)]
    U2 = embed2(H, H, [0, 1], [2, 3], [2, 3], [0, 1])
    U2p = embed2(H, Hd, [0, 1], [2, 3], [2, 3], [0, 1])
    U1 = embed2(H, H, [0, 2], [2, 3], [1, 3], [0, 1])
    for M, nm in ((U2, "U2"), (U2p, "U2'"), (U1, "U1")):
        assert is_unitary(K8, M), nm
    mono = [all(sum(1 for x in r if not K8.is_zero(x)) <= 1 for r in M)
            for M in (U2, U2p, U1)]
    live = max(sum(1 for k in range(4)
                   if not K8.is_zero(K8.mul(U2[i][k], U1[k][j])))
               for i in range(4) for j in range(4))
    same_orbit = all(
        K8.normsq(U2[i][j]) == K8.normsq(U2p[i][j]) for i in range(4)
        for j in range(4))
    Ccal_same = True
    for i in range(4):
        for j in range(4):
            wa = [K8.mul(U2[i][k], U1[k][j]) for k in range(4)]
            wb = [K8.mul(U2p[i][k], U1[k][j]) for k in range(4)]
            for k in range(4):
                for l in range(4):
                    if K8.mul(wa[k], K8.conj(wa[l])) != K8.mul(wb[k], K8.conj(wb[l])):
                        Ccal_same = False
    P1 = mat_mul(K8, U2, U1)
    P2 = mat_mul(K8, U2p, U1)
    shadows_same = born(K8, P1) == born(K8, P2)
    D1 = [[K8.sub(x, y) for x, y in zip(r1, r2)]
          for r1, r2 in zip(born(K8, P1),
                            mat_mul(K8, born(K8, U2), born(K8, U1)))]
    D2 = [[K8.sub(x, y) for x, y in zip(r1, r2)]
          for r1, r2 in zip(born(K8, P2),
                            mat_mul(K8, born(K8, U2p), born(K8, U1)))]
    flat = all(K8.is_zero(v) for r in D1 for v in r) and \
        all(K8.is_zero(v) for r in D2 for v in r)
    comm1 = mat_mul(K8, mat_mul(K8, U2, U1),
                    mat_mul(K8, _adj(K8, U2), _adj(K8, U1)))
    scalar1 = all(comm1[i][j] == (comm1[0][0] if i == j else K8.zero)
                  for i in range(4) for j in range(4))
    h1 = _haag(K8, P1, 0, 2, 0, 2)
    h2 = _haag(K8, P2, 0, 2, 0, 2)
    ratio = K8.mul(h2, K8.inv(h1))
    print("      neither factor is monomial: %s ; live paths per endpoint pair: "
          "%d ; the two second legs share a boundary orbit: %s"
          % (mono, live, same_orbit))
    print("      the cut-coherence tensors agree entry by entry: %s ; the "
          "composites' Born shadows agree: %s ; both pairs are defect-flat: %s"
          % (Ccal_same, shadows_same, flat))
    print("      the relation-loop sector is empty (the group commutator is not "
          "scalar): %s" % (not scalar1))
    print("      but the composites' four-cycle invariants are %s and %s, with "
          "ratio %s" % (_pp(K8, h1), _pp(K8, h2), _pp(K8, ratio)))
    R.anchor("witness monomial", mono, [False, False, False])
    R.anchor("witness live paths", live, 1)
    R.anchor("witness same moduli", same_orbit, True)
    R.anchor("witness same tensor", Ccal_same, True)
    R.anchor("witness same shadow", shadows_same, True)
    R.anchor("witness defect flat", flat, True)
    R.anchor("witness commutator not scalar", scalar1, False)
    R.anchor("witness H_1", _pp(K8, h1), "1/16")
    R.anchor("witness H_2", _pp(K8, h2), "-1/16*z^3")
    R.anchor("witness ratio", _pp(K8, ratio), "-z^3")

    # -----------------------------------------------------------------------
    hr(); print("[6.9] the cross-block completion")
    S2w = [[0 if K8.is_zero(U2[i][j]) else 1 for j in range(4)] for i in range(4)]
    S1w = [[0 if K8.is_zero(U1[i][j]) else 1 for j in range(4)] for i in range(4)]
    edges, kind = build_graph(S2w, S1w, 4)
    eidx = {e: t for t, e in enumerate(edges)}
    ninv = 0
    ntot = 0
    sumk = 0
    for (i, ip, j, jp) in ((0, 2, 0, 2), (0, 1, 1, 3), (1, 3, 0, 2), (2, 3, 1, 2)):
        acc = K8.zero
        for k in range(4):
            for l in range(4):
                for kp in range(4):
                    for lp in range(4):
                        t = K8.mul(
                            K8.mul(K8.mul(U2[i][k], U1[k][j]),
                                   K8.conj(K8.mul(U2[ip][l], U1[l][j]))),
                            K8.mul(K8.mul(U2[ip][kp], U1[kp][jp]),
                                   K8.conj(K8.mul(U2[i][lp], U1[lp][jp]))))
                        acc = K8.add(acc, t)
        ntot += 1
        if acc == _haag(K8, P1, i, ip, j, jp):
            sumk += 1
        # gauge invariance at a declared switching
        dR = [K8.zpow(i2 + 1) for i2 in range(4)]
        dK = [K8.zpow(2 * k2 + 1) for k2 in range(4)]
        dC = [K8.zpow(3 * j2 + 1) for j2 in range(4)]
        U2g = [[K8.mul(K8.mul(dR[a], K8.conj(dK[b])), U2[a][b]) for b in range(4)]
               for a in range(4)]
        U1g = [[K8.mul(K8.mul(dK[a], K8.conj(dC[b])), U1[a][b]) for b in range(4)]
               for a in range(4)]
        acc2 = K8.zero
        for k in range(4):
            for l in range(4):
                for kp in range(4):
                    for lp in range(4):
                        t = K8.mul(
                            K8.mul(K8.mul(U2g[i][k], U1g[k][j]),
                                   K8.conj(K8.mul(U2g[ip][l], U1g[l][j]))),
                            K8.mul(K8.mul(U2g[ip][kp], U1g[kp][jp]),
                                   K8.conj(K8.mul(U2g[i][lp], U1g[lp][jp]))))
                        acc2 = K8.add(acc2, t)
        if acc2 == acc:
            ninv += 1
    print("      the summed completion equals the composite's own four-cycle "
          "invariant at %d of %d declared index quadruples" % (sumk, ntot))
    print("      it is unchanged by a declared switching moving all three vertex "
          "classes at %d of %d" % (ninv, ntot))
    R.anchor("Kappa sum identity", (sumk, ntot), (4, 4))
    R.anchor("Kappa gauge invariance", (ninv, ntot), (4, 4))

    closed = 0
    firsts = []
    for f in stats[4][10]:
        ok, first = close_with_kappa(f, 4)
        closed += 1 if ok else 0
        firsts.append(first)
    print("      adjoining the completion closes %d of the %d n = 4 gaps"
          % (closed, len(stats[4][10])))
    print("      the first separating index tuple at the leading failing class: %s"
          % (firsts[0],))
    R.anchor("n=4 gaps closed", closed, 7)

    # the declared n = 5 sample
    hr(); print("      the declared n = 5 sample")
    n = 5
    perms5 = list(itertools.permutations(range(n)))
    base = [perms5[t] for t in range(0, len(perms5), 3)]
    print("      120 permutations in lexicographic order, stride 3 -> %d bases"
          % len(base))
    pats = set()
    for r in (2, 3, 4):
        for combo in itertools.combinations(range(len(base)), r):
            S = [[0] * n for _ in range(n)]
            for t in combo:
                for i in range(n):
                    S[i][base[t][i]] = 1
            if admissible(S, n):
                pats.add(tuple(tuple(row) for row in S))
    pats = [list(map(list, S)) for S in sorted(pats)]
    c2 = {}
    c1 = {}
    for S in pats:
        c2.setdefault(canon_rowcol(S, n, perms5), S)
        c1.setdefault(canon_col(S, n, perms5), S)
    s2c, s1c = list(c2.values()), list(c1.values())
    total5, maxmu5, fails5, defs5, pinned5 = sweep(
        n, s2c, s1c, "n=5", progress=500)
    print("      %d sampled patterns -> %d x %d = %d graph classes ; max cycle "
          "rank %d ; four-cycle failures %d"
          % (len(pats), len(s2c), len(s1c), total5, maxmu5, len(fails5)))
    closed5 = 0
    for f in fails5:
        ok, _ = close_with_kappa(f, n, cap=200000)
        closed5 += 1 if ok else 0
    print("      the completion closes %d of them" % closed5)
    R.anchor("n=5 sampled patterns", len(pats), 653)
    R.anchor("n=5 graph classes", total5, 2100)
    R.anchor("n=5 max cycle rank", maxmu5, 26)
    R.anchor("n=5 failures", len(fails5), 101)
    R.anchor("n=5 gaps closed", closed5, 101)

    R.finish()


# ---------------------------------------------------------------------------
def _matpow(K, M, p):
    n = len(M)
    out = [[K.one if i == j else K.zero for j in range(n)] for i in range(n)]
    for _ in range(p):
        out = mat_mul(K, out, M)
    return out


def _adj(K, M):
    n = len(M)
    return [[K.conj(M[j][i]) for j in range(n)] for i in range(n)]


def _inv_perm(K, P):
    return _adj(K, P)


def _inv_diag(K, D):
    n = len(D)
    return [[K.inv(D[i][j]) if i == j else K.zero for j in range(n)]
            for i in range(n)]


def _commutator(K, A, B):
    return mat_mul(K, mat_mul(K, A, B), mat_mul(K, _adj(K, A), _adj(K, B)))


def _haag(K, M, i, ip, j, jp):
    return K.mul(K.mul(M[i][j], M[ip][jp]),
                 K.mul(K.conj(M[i][jp]), K.conj(M[ip][j])))


def _pp(K, v):
    """print a Q(zeta_8) element as a short monomial where possible."""
    nz = [(t, c) for t, c in enumerate(v) if c]
    if len(nz) == 1:
        t, c = nz[0]
        if t == 0:
            return str(c)
        return "%sz^%d" % (("" if c == 1 else ("-" if c == -1 else str(c) + "*")), t)
    return str(v)


if __name__ == "__main__":
    main()

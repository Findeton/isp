import math
from collections import defaultdict

import mpmath as mp


def fmt(x, n=36):
    return mp.nstr(x, n)


def zero_matrix(n):
    return [[mp.mpf(0) for _ in range(n)] for _ in range(n)]


def scale_matrix(matrix, scale):
    scale = mp.mpf(scale)
    return [[scale * value for value in row] for row in matrix]


def add_matrices(*matrices):
    n = len(matrices[0])
    out = zero_matrix(n)
    for matrix in matrices:
        for i in range(n):
            for j in range(n):
                out[i][j] += matrix[i][j]
    return out


def offdiag_sum(matrix):
    n = len(matrix)
    return mp.fsum(matrix[i][j] for i in range(n) for j in range(n) if i != j)


def project_symmetric_zero_row(matrix):
    n = len(matrix)
    sym = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                sym[i][j] = (mp.mpf(matrix[i][j]) + mp.mpf(matrix[j][i])) / 2

    row = [mp.fsum(sym[i][j] for j in range(n) if i != j) for i in range(n)]
    total_row = mp.fsum(row)
    correction_constant = -total_row / ((n - 2) * (n - 1))
    out = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                h = (row[i] + row[j]) / (n - 2) + correction_constant
                out[i][j] = sym[i][j] - h
    return out


def max_row_linf(matrix):
    n = len(matrix)
    return max(abs(mp.fsum(matrix[i][j] for j in range(n) if i != j)) for i in range(n))


def axis_excess(matrix):
    n = len(matrix)
    return offdiag_sum([[matrix[i][j] ** 2 for j in range(n)] for i in range(n)]) / (
        mp.mpf(n) * (n - 1)
    )


def A_anti(z, c):
    z = mp.mpf(z)
    c = mp.mpf(c)
    if z <= -c:
        return mp.mpf(0)
    if z < c:
        return (z + c) ** 2 / (4 * c)
    return z


def marginal_cdf(x, c):
    return A_anti(x, c) - A_anti(mp.mpf(x) - 1, c)


def legendre_nodes(n, left, right):
    xs, ws = mp.gauss_quadrature(n, "legendre")
    mid = (mp.mpf(left) + mp.mpf(right)) / 2
    half = (mp.mpf(right) - mp.mpf(left)) / 2
    return [(mid + half * xs[i], half * ws[i]) for i in range(n)]


def clamp_unit(x):
    if x < 0:
        return mp.mpf(0)
    if x > 1:
        return mp.mpf(1)
    return x


def rank_kernel_values(n, low, high):
    between = high - low
    above = 1 - high
    fact = mp.mpf(math.factorial(n - 2))
    out = []
    for a in range(n - 1):
        low_pow = low**a
        for b in range(a + 1, n):
            coeff = fact / (
                mp.mpf(math.factorial(a))
                * mp.mpf(math.factorial(b - a - 1))
                * mp.mpf(math.factorial(n - 1 - b))
            )
            value = coeff * low_pow * (between ** (b - a - 1)) * (above ** (n - 1 - b))
            out.append((a, b, value))
    return out


def physical_delta(n, c, nodes=12):
    c = mp.mpf(c)
    matrix = zero_matrix(n)
    density_factor = 1 / (4 * c * c)
    for s, ws in legendre_nodes(nodes, 0, 1):
        for e0, we0 in legendre_nodes(nodes, -c, c):
            r0 = clamp_unit(marginal_cdf(s + e0, c))
            for e1, we1 in legendre_nodes(nodes + 1, -c, c):
                r1 = clamp_unit(marginal_cdf(s + e1, c))
                weight = ws * we0 * we1 * density_factor
                if r0 < r1:
                    for a, b, value in rank_kernel_values(n, r0, r1):
                        matrix[a][b] += weight * value
                elif r1 < r0:
                    for b, a, value in rank_kernel_values(n, r1, r0):
                        matrix[a][b] += weight * value

    sym = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                sym[i][j] = (matrix[i][j] + matrix[j][i]) / 2
    total = offdiag_sum(sym)
    uniform = 1 / (mp.mpf(n) * (n - 1))
    residue = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                probability = sym[i][j] / total
                residue[i][j] = mp.mpf(n) * (n - 1) * (probability - uniform)
    return project_symmetric_zero_row(residue)


def falling(n, k):
    out = mp.mpf(1)
    for value in range(k):
        out *= n - value
    return out


def directed_pair_entries(D):
    n = len(D)
    return [((1 << i) | (1 << j), D[i][j]) for i in range(n) for j in range(n) if i != j]


def undirected_edge_entries(D):
    n = len(D)
    return [((1 << i) | (1 << j), D[i][j]) for i in range(n) for j in range(i + 1, n)]


def disjoint_moments(D):
    n = len(D)
    entries = directed_pair_entries(D)
    dp = {0: mp.mpf(1)}
    out = {0: mp.mpf(1)}
    for r in range(1, n // 2 + 1):
        next_dp = defaultdict(mp.mpf)
        for used, value in dp.items():
            for mask, edge_value in entries:
                if used & mask:
                    continue
                next_dp[used | mask] += value * edge_value
        out[r] = mp.fsum(next_dp.values()) / falling(n, 2 * r)
        dp = next_dp
    return out


def unordered_matching_sums(D):
    n = len(D)
    entries = undirected_edge_entries(D)
    dp = {0: mp.mpf(1)}
    out = {0: mp.mpf(1)}
    for r in range(1, n // 2 + 1):
        next_dp = defaultdict(mp.mpf)
        for used, value in dp.items():
            for mask, edge_value in entries:
                if used & mask:
                    continue
                next_dp[used | mask] += value * edge_value
        out[r] = mp.fsum(next_dp.values())
        dp = next_dp
    return out


def rho_from_unordered_matching(n, r, matching_sum):
    return (mp.mpf(2) ** r) * matching_sum / falling(n, 2 * r)


def coefficient_profile(D):
    n = len(D)
    rho = disjoint_moments(D)
    q = {r: mp.mpf(math.comb(n // 2, r)) * rho[r] * rho[r] for r in range(1, n // 2 + 1)}
    beta = {
        r: mp.mpf(n) * mp.power(abs(q[r]), mp.mpf(1) / r)
        for r in range(2, n // 2 + 1)
    }
    return q, rho, beta


def normalized_matching_coefficients(D):
    n = len(D)
    rho = disjoint_moments(D)
    return [rho.get(r, mp.mpf(0)) for r in range(n // 2 + 1)]


def scaled_matching_coefficients(D):
    n = len(D)
    rho = disjoint_moments(D)
    return [rho.get(r, mp.mpf(0)) * (mp.mpf(n) ** r) for r in range(n // 2 + 1)]


def matrix_to_mp(D, scale=1):
    n = len(D)
    scale = mp.mpf(scale)
    return mp.matrix([[scale * D[i][j] for j in range(n)] for i in range(n)])


def trace_powers_scaled(D, max_r):
    n = len(D)
    A = matrix_to_mp(D, scale=1 / mp.mpf(n))
    current = mp.eye(n)
    out = {}
    for k in range(1, max_r + 1):
        current = current * A
        out[k] = mp.fsum(current[i, i] for i in range(n))
    return out


def reciprocal_determinant_coefficients(D, max_r):
    traces = trace_powers_scaled(D, max_r)
    log_coeff = {k: ((-1) ** k) * (mp.mpf(2) ** k) * traces[k] / k for k in range(1, max_r + 1)}
    coeff = [mp.mpf(0) for _ in range(max_r + 1)]
    coeff[0] = mp.mpf(1)
    for n in range(1, max_r + 1):
        coeff[n] = mp.fsum(k * log_coeff[k] * coeff[n - k] for k in range(1, n + 1)) / n
    return coeff, traces, log_coeff


def symmetric_eigenvalues_scaled(D):
    n = len(D)
    A = matrix_to_mp(D, scale=1 / mp.mpf(n))
    vals = mp.eigsy(A, eigvals_only=True)
    return sorted([mp.mpf(v) for v in vals], key=lambda x: abs(x), reverse=True)


def balanced_block_D(n):
    half = n // 2
    matrix = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                same = (i < half and j < half) or (i >= half and j >= half)
                matrix[i][j] = mp.mpf(1) if same else mp.mpf(-1)
    return project_symmetric_zero_row(matrix)


def fourier_vector(n, k, kind):
    out = []
    for i in range(n):
        x = (mp.mpf(i) + mp.mpf("0.5")) / n
        angle = 2 * mp.pi * k * x
        out.append(mp.cos(angle) if kind == "cos" else mp.sin(angle))
    mean = mp.fsum(out) / n
    centered = [value - mean for value in out]
    norm = mp.sqrt(mp.fsum(value * value for value in centered))
    return [value / norm for value in centered]


def outer_kernel(vector):
    n = len(vector)
    out = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                out[i][j] = vector[i] * vector[j]
    return project_symmetric_zero_row(out)


def calibrate_to_q2(D, target_q2):
    q, _rho, _beta = coefficient_profile(D)
    return scale_matrix(D, (target_q2 / q[2]) ** mp.mpf("0.25"))

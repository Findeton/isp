#!/usr/bin/env python3
"""
Paper 28 receipt: cumulant/spectral attack on the stable-cancellation lemma.

The missing lemma from Paper 28 is:

    prove stable signed cancellation in the exact Mobius/falling-factor
    2-core expansion for the physical rank-copula, strong enough to imply
    the coefficient-root envelope.

This receipt does not prove the lemma.  It tests the proof route that should
be tried next:

1. replace the raw coefficient sequence rho_r by the log/cumulant sequence;
2. estimate the finite Cauchy radius suggested by the log series;
3. check whether the physical kernel has less coherent spectral mass than a
   q2-calibrated staged block.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

import math
import sys
from itertools import permutations, product

import mpmath as mp

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140


def fmt(x, n=36):
    return mp.nstr(x, n)


checks = []


def check(name, ok, detail=""):
    ok = bool(ok)
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def zero_matrix(n):
    return [[mp.mpf(0) for _ in range(n)] for _ in range(n)]


def offdiag_sum(matrix):
    n = len(matrix)
    return mp.fsum(matrix[i][j] for i in range(n) for j in range(n) if i != j)


def scale_matrix(matrix, scale):
    scale = mp.mpf(scale)
    return [[scale * value for value in row] for row in matrix]


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
    return mp.fsum(
        matrix[i][j] ** 2 for i in range(n) for j in range(n) if i != j
    ) / (mp.mpf(n) * (n - 1))


def normalize_A_one(matrix):
    A = axis_excess(matrix)
    if A == 0:
        raise ValueError("zero matrix")
    return scale_matrix(matrix, 1 / mp.sqrt(A)), A


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
            value = coeff * low_pow * (between ** (b - a - 1)) * (
                above ** (n - 1 - b)
            )
            out.append((a, b, value))
    return out


def physical_delta(n, c, nodes):
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


def balanced_block_D(n):
    half = n // 2
    matrix = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                same = (i < half and j < half) or (i >= half and j >= half)
                matrix[i][j] = mp.mpf(1) if same else mp.mpf(-1)
    return project_symmetric_zero_row(matrix)


def falling(n, k):
    out = mp.mpf(1)
    for value in range(k):
        out *= n - value
    return out


def direct_disjoint_moment(D, r):
    n = len(D)
    if r == 0:
        return mp.mpf(1)
    entries = []
    for i in range(n):
        for j in range(n):
            if i != j:
                entries.append(((1 << i) | (1 << j), D[i][j]))
    dp = {0: mp.mpf(1)}
    for _depth in range(1, r + 1):
        next_dp = {}
        for used, value in dp.items():
            for mask, edge_value in entries:
                if used & mask:
                    continue
                key = used | mask
                next_dp[key] = next_dp.get(key, mp.mpf(0)) + value * edge_value
        dp = next_dp
    return mp.fsum(dp.values()) / falling(n, 2 * r)


def set_partitions(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    first = items[0]
    for partition in set_partitions(items[1:]):
        yield ((first,),) + partition
        for index in range(len(partition)):
            block = tuple(sorted(partition[index] + (first,)))
            yield partition[:index] + (block,) + partition[index + 1 :]


def canonical_partition(partition):
    return tuple(sorted((tuple(sorted(block)) for block in partition), key=lambda b: b[0]))


def adjacency_from_partition(r, partition):
    block_of = {}
    for block_index, block in enumerate(partition):
        for endpoint in block:
            block_of[endpoint] = block_index
    v = len(partition)
    adj = [[0 for _ in range(v)] for _ in range(v)]
    degrees = [0 for _ in range(v)]
    for edge in range(r):
        a = block_of[2 * edge]
        b = block_of[2 * edge + 1]
        if a == b:
            return None
        adj[a][b] += 1
        adj[b][a] += 1
        degrees[a] += 1
        degrees[b] += 1
    if min(degrees) < 2:
        return None
    return adj


def canonical_adjacency(adj):
    v = len(adj)
    best = None
    for perm in permutations(range(v)):
        flat = tuple(adj[perm[i]][perm[j]] for i in range(v) for j in range(i + 1, v))
        if best is None or flat < best:
            best = flat
    return (v, best)


def decode_adjacency(code):
    v, flat = code
    adj = [[0 for _ in range(v)] for _ in range(v)]
    cursor = 0
    for i in range(v):
        for j in range(i + 1, v):
            adj[i][j] = flat[cursor]
            adj[j][i] = flat[cursor]
            cursor += 1
    return adj


def mobius_from_adjacency(adj):
    out = mp.mpf(1)
    for degree in [sum(row) for row in adj]:
        out *= (-1) ** (degree - 1) * math.factorial(degree - 1)
    return out


def two_core_shape_counts(r):
    seen = set()
    out = {}
    for partition in set_partitions(range(2 * r)):
        partition = canonical_partition(partition)
        if partition in seen:
            continue
        seen.add(partition)
        adj = adjacency_from_partition(r, partition)
        if adj is None:
            continue
        code = canonical_adjacency(adj)
        out[code] = out.get(code, 0) + 1
    return out


def graph_edges(adj):
    edges = []
    for i in range(len(adj)):
        for j in range(i + 1, len(adj)):
            for _ in range(adj[i][j]):
                edges.append((i, j))
    return edges


def connected_component_count(adj):
    v = len(adj)
    seen = set()
    count = 0
    for start in range(v):
        if start in seen:
            continue
        count += 1
        stack = [start]
        seen.add(start)
        while stack:
            node = stack.pop()
            for nxt, multiplicity in enumerate(adj[node]):
                if multiplicity and nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
    return count


def homomorphism_average(D, adj):
    n = len(D)
    v = len(adj)
    edges = graph_edges(adj)
    total = mp.mpf(0)
    count = mp.mpf(n) ** v
    for assignment in product(range(n), repeat=v):
        product_value = mp.mpf(1)
        for i, j in edges:
            product_value *= D[assignment[i]][assignment[j]]
        total += product_value
    return total / count


def mobius_component_sums(D, r):
    n = len(D)
    total = mp.mpf(0)
    connected = mp.mpf(0)
    disconnected = mp.mpf(0)
    connected_abs = mp.mpf(0)
    disconnected_abs = mp.mpf(0)
    for code, count in two_core_shape_counts(r).items():
        adj = decode_adjacency(code)
        v = len(adj)
        mu = mobius_from_adjacency(adj)
        H = homomorphism_average(D, adj)
        weight = mp.mpf(count) * mu * (mp.mpf(n) ** v) / falling(n, 2 * r)
        term = weight * H
        total += term
        if connected_component_count(adj) == 1:
            connected += term
            connected_abs += abs(term)
        else:
            disconnected += term
            disconnected_abs += abs(term)
    return {
        "total": total,
        "connected": connected,
        "disconnected": disconnected,
        "connected_abs": connected_abs,
        "disconnected_abs": disconnected_abs,
    }


def coefficient(n, r, rho):
    return mp.mpf(math.comb(n // 2, r)) * rho * rho


def log_series_coefficients(rho):
    """Return ell with log(sum rho_r z^r) = sum ell_r z^r."""
    max_r = len(rho) - 1
    ell = [mp.mpf(0) for _ in range(max_r + 1)]
    if rho[0] != 1:
        raise ValueError("rho[0] must be one")
    for n in range(1, max_r + 1):
        correction = mp.fsum(k * ell[k] * rho[n - k] for k in range(1, n))
        ell[n] = rho[n] - correction / n
    return ell


def exp_series_coefficients(ell):
    """Invert log_series_coefficients for a consistency check."""
    max_r = len(ell) - 1
    rho = [mp.mpf(0) for _ in range(max_r + 1)]
    rho[0] = mp.mpf(1)
    for n in range(1, max_r + 1):
        rho[n] = mp.fsum(k * ell[k] * rho[n - k] for k in range(1, n + 1)) / n
    return rho


def cauchy_gamma_from_log(ell, n, budget, lo=mp.mpf("0"), hi=mp.mpf("10")):
    """Largest gamma in [lo, hi] with sum |ell_r| (gamma n)^r <= budget."""
    def value(gamma):
        radius = gamma * n
        return mp.fsum(abs(ell[r]) * radius**r for r in range(2, len(ell)))

    while value(hi) <= budget:
        hi *= 2
    for _ in range(160):
        mid = (lo + hi) / 2
        if value(mid) <= budget:
            lo = mid
        else:
            hi = mid
    return lo, value(lo)


def matrix_to_mp(matrix):
    return mp.matrix([[mp.mpf(value) for value in row] for row in matrix])


def eig_spectrum(matrix):
    vals, _vecs = mp.eigsy(matrix_to_mp(matrix))
    return [mp.mpf(vals[i]) for i in range(len(vals))]


def spectral_report(matrix):
    vals = eig_spectrum(matrix)
    squares = [value * value for value in vals]
    fourths = [square * square for square in squares]
    sum2 = mp.fsum(squares)
    sum4 = mp.fsum(fourths)
    top2 = max(squares)
    participation = (sum2 * sum2 / sum4) if sum4 else mp.inf
    return {
        "vals": vals,
        "top_abs": mp.sqrt(top2),
        "top_square_share": top2 / sum2 if sum2 else mp.inf,
        "participation": participation,
        "trace2": sum2,
        "trace4": sum4,
    }


print("=" * 80)
print("Paper 28 cumulant/spectral cancellation receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

n = 12
c = mp.mpf("0.5")
nodes = 12
max_r = n // 2
block_scale = mp.mpf("0.410498227581451253")

physical = physical_delta(n, c, nodes)
block_base, _block_A = normalize_A_one(balanced_block_D(n))
block = scale_matrix(block_base, block_scale)

families = [("physical", physical), ("q2_block", block)]

print("\n=== Kernel checks ===")
for name, D in families:
    print(f"{name} row_linf = {fmt(max_row_linf(D), 18)}")

rows = {}
print("\n=== Coefficients and log/cumulant coefficients ===")
for name, D in families:
    rho = [mp.mpf(1)]
    q = [mp.mpf(0)]
    scaled_matching = [mp.mpf(1)]
    for r in range(1, max_r + 1):
        rho_r = direct_disjoint_moment(D, r)
        rho.append(rho_r)
        q.append(coefficient(n, r, rho_r))
        unordered_matching = falling(n, 2 * r) * rho_r / math.factorial(r)
        scaled_matching.append(unordered_matching / (mp.mpf(n) ** (2 * r)))
    ell = log_series_coefficients(rho)
    eta = log_series_coefficients(scaled_matching)
    recovered = exp_series_coefficients(ell)
    recovered_matching = exp_series_coefficients(eta)
    reconstruction_error = max(abs(rho[i] - recovered[i]) for i in range(max_r + 1))
    matching_error = max(
        abs(scaled_matching[i] - recovered_matching[i]) for i in range(max_r + 1)
    )
    gamma_half, gamma_budget = cauchy_gamma_from_log(ell, n, mp.mpf("0.5"))
    gamma_one, gamma_one_budget = cauchy_gamma_from_log(ell, n, mp.mpf("1.0"))
    matching_gamma_one, _matching_budget = cauchy_gamma_from_log(eta, n, mp.mpf("1.0"))
    rows[name] = {
        "rho": rho,
        "q": q,
        "scaled_matching": scaled_matching,
        "ell": ell,
        "eta": eta,
        "reconstruction_error": reconstruction_error,
        "matching_error": matching_error,
        "gamma_half": gamma_half,
        "gamma_half_budget": gamma_budget,
        "gamma_one": gamma_one,
        "gamma_one_budget": gamma_one_budget,
        "matching_gamma_one": matching_gamma_one,
    }
    print(f"\n{name}:")
    print(f"  reconstruction_error = {fmt(reconstruction_error, 18)}")
    print(f"  scaled_matching_reconstruction_error = {fmt(matching_error, 18)}")
    print(
        f"  gamma_budget_0.5 = {fmt(gamma_half, 18)} "
        f"(radius={fmt(gamma_half * n, 18)})"
    )
    print(
        f"  gamma_budget_1.0 = {fmt(gamma_one, 18)} "
        f"(radius={fmt(gamma_one * n, 18)})"
    )
    print(
        f"  matching_log_gamma_budget_1.0 = {fmt(matching_gamma_one, 18)} "
        f"(radius={fmt(matching_gamma_one * n, 18)})"
    )
    for r in range(1, max_r + 1):
        rho_root = n * (abs(rho[r]) ** (mp.mpf(1) / r)) if rho[r] else mp.mpf(0)
        q_root = n * (abs(q[r]) ** (mp.mpf(1) / r)) if q[r] else mp.mpf(0)
        ell_root = n * (abs(ell[r]) ** (mp.mpf(1) / r)) if ell[r] else mp.mpf(0)
        eta_root = (
            n * (abs(eta[r]) ** (mp.mpf(1) / r)) if eta[r] else mp.mpf(0)
        )
        print(
            f"  r={r}, rho={fmt(rho[r], 18)}, ell={fmt(ell[r], 18)}, "
            f"eta={fmt(eta[r], 18)}, "
            f"N|rho|^(1/r)={fmt(rho_root, 18)}, "
            f"N|ell|^(1/r)={fmt(ell_root, 18)}, "
            f"N|eta|^(1/r)={fmt(eta_root, 18)}, "
            f"Nq^(1/r)={fmt(q_root, 18)}"
        )

print("\n=== Physical/staged ratios ===")
for r in range(2, max_r + 1):
    q_ratio = rows["q2_block"]["q"][r] / rows["physical"]["q"][r]
    ell_ratio = (
        abs(rows["q2_block"]["ell"][r]) / abs(rows["physical"]["ell"][r])
        if rows["physical"]["ell"][r]
        else mp.inf
    )
    eta_ratio = (
        abs(rows["q2_block"]["eta"][r]) / abs(rows["physical"]["eta"][r])
        if rows["physical"]["eta"][r]
        else mp.inf
    )
    rho_ratio = (
        abs(rows["q2_block"]["rho"][r]) / abs(rows["physical"]["rho"][r])
        if rows["physical"]["rho"][r]
        else mp.inf
    )
    print(
        f"r={r}, |rho| ratio={fmt(rho_ratio, 18)}, "
        f"|ell| ratio={fmt(ell_ratio, 18)}, "
        f"|eta| ratio={fmt(eta_ratio, 18)}, q ratio={fmt(q_ratio, 18)}"
    )

print("\n=== Connected versus disconnected 2-core terms ===")
component_rows = {}
max_component_r = 5
for name, D in families:
    component_rows[name] = {}
    print(f"\n{name}:")
    for r in range(2, max_component_r + 1):
        parts = mobius_component_sums(D, r)
        component_rows[name][r] = parts
        total_error = abs(parts["total"] - rows[name]["rho"][r])
        log_gap = rows[name]["ell"][r] - parts["connected"]
        disconnected_gap = (rows[name]["rho"][r] - rows[name]["ell"][r]) - parts[
            "disconnected"
        ]
        print(
            f"  r={r}, total_error={fmt(total_error, 8)}, "
            f"connected={fmt(parts['connected'], 18)}, "
            f"disconnected={fmt(parts['disconnected'], 18)}, "
            f"ell={fmt(rows[name]['ell'][r], 18)}, "
            f"ell-connected={fmt(log_gap, 18)}, "
            f"finite_denominator_gap={fmt(disconnected_gap, 18)}"
        )

print("\n=== Spectral concentration ===")
spectra = {}
for name, D in families:
    spectra[name] = spectral_report(D)
    report = spectra[name]
    print(f"\n{name}:")
    print(f"  top_abs_eigenvalue = {fmt(report['top_abs'], 18)}")
    print(f"  top_square_share = {fmt(report['top_square_share'], 18)}")
    print(f"  participation_ratio = {fmt(report['participation'], 18)}")
    print(f"  trace2 = {fmt(report['trace2'], 18)}")
    print(f"  trace4 = {fmt(report['trace4'], 18)}")
    sorted_vals = sorted(report["vals"], key=lambda x: abs(x), reverse=True)
    print(
        "  top_abs_spectrum = "
        + ", ".join(fmt(value, 12) for value in sorted_vals[:5])
    )

physical = rows["physical"]
block = rows["q2_block"]
spectral_physical = spectra["physical"]
spectral_block = spectra["q2_block"]

check(
    "both kernels remain canonical after projection",
    max_row_linf(families[0][1]) < mp.mpf("1e-80")
    and max_row_linf(families[1][1]) < mp.mpf("1e-80"),
    f"physical={fmt(max_row_linf(families[0][1]), 18)} "
    f"block={fmt(max_row_linf(families[1][1]), 18)}",
)
check(
    "log/cumulant transform reconstructs the coefficient series",
    physical["reconstruction_error"] < mp.mpf("1e-80")
    and block["reconstruction_error"] < mp.mpf("1e-80"),
    f"physical={fmt(physical['reconstruction_error'], 18)} "
    f"block={fmt(block['reconstruction_error'], 18)}",
)
check(
    "matching-polynomial log transform reconstructs the scaled matching series",
    physical["matching_error"] < mp.mpf("1e-80")
    and block["matching_error"] < mp.mpf("1e-80"),
    f"physical={fmt(physical['matching_error'], 18)} "
    f"block={fmt(block['matching_error'], 18)}",
)
check(
    "q2 calibration is preserved in this receipt",
    abs(block["q"][2] / physical["q"][2] - 1) < mp.mpf("1e-12"),
    f"q2_ratio={fmt(block['q'][2] / physical['q'][2], 18)}",
)
check(
    "high-order q ratios still expose staged coherence",
    block["q"][5] / physical["q"][5] > mp.mpf("200"),
    f"q5_ratio={fmt(block['q'][5] / physical['q'][5], 18)}",
)
check(
    "log/cumulant ratios expose the staged block by r=5",
    abs(block["ell"][5]) / abs(physical["ell"][5]) > mp.mpf("10"),
    f"ell5_ratio={fmt(abs(block['ell'][5]) / abs(physical['ell'][5]), 18)}",
)
check(
    "matching-log coefficient alone does not expose the staged block at r=5",
    abs(block["eta"][5]) / abs(physical["eta"][5]) < mp.mpf("1"),
    f"eta5_ratio={fmt(abs(block['eta'][5]) / abs(physical['eta'][5]), 18)}",
)
component_total_error = max(
    abs(component_rows[name][r]["total"] - rows[name]["rho"][r])
    for name, _D in families
    for r in range(2, max_component_r + 1)
)
check(
    "2-core component expansion reproduces the direct rho coefficients",
    component_total_error < mp.mpf("1e-70"),
    f"max_error={fmt(component_total_error, 18)}",
)
check(
    "disconnected 2-core pieces first appear in the audited higher orders",
    abs(component_rows["physical"][4]["disconnected"]) > mp.mpf("1e-12")
    and abs(component_rows["physical"][5]["disconnected"]) > mp.mpf("1e-12"),
    f"phys_r4={fmt(component_rows['physical'][4]['disconnected'], 18)} "
    f"phys_r5={fmt(component_rows['physical'][5]['disconnected'], 18)}",
)
check(
    "physical log-series has a larger empirical Cauchy gamma at budget one",
    physical["gamma_one"] > block["gamma_one"],
    f"physical={fmt(physical['gamma_one'], 18)} "
    f"block={fmt(block['gamma_one'], 18)}",
)
check(
    "physical matching-log series has a larger empirical Cauchy gamma at budget one",
    physical["matching_gamma_one"] > block["matching_gamma_one"],
    f"physical={fmt(physical['matching_gamma_one'], 18)} "
    f"block={fmt(block['matching_gamma_one'], 18)}",
)
check(
    "staged block has more concentrated spectral square mass",
    spectral_block["top_square_share"] > spectral_physical["top_square_share"],
    f"physical={fmt(spectral_physical['top_square_share'], 18)} "
    f"block={fmt(spectral_block['top_square_share'], 18)}",
)
check(
    "physical kernel has higher spectral participation",
    spectral_physical["participation"] > spectral_block["participation"],
    f"physical={fmt(spectral_physical['participation'], 18)} "
    f"block={fmt(spectral_block['participation'], 18)}",
)

print("\n=== Proof route implication ===")
print("The log/cumulant transform is exact and reconstructs the coefficient")
print("series.  In this finite receipt, the staged block is still visible in")
print("the high-order cumulants, and it has more concentrated spectral mass.")
print("The quotient-graph connected sum is not identical to the ordinary log")
print("coefficient at finite N.  The hard-core matching/Mayer log is cleaner")
print("formally and has a larger empirical radius, but its r=5 coefficient")
print("alone does not expose the staged block.  The analytic target is")
print("therefore a hybrid one: a matching-cluster expansion plus the")
print("falling-factor/normalization map back to the normalized rho_r")
print("coefficients, with spectral/Schatten bounds for the physical")
print("rank-copula.  The receipt does not prove the all-order bound.")

print("\n" + "=" * 80)
failed = [name for name, ok, _detail in checks if not ok]
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")

if failed:
    print(f"\nCHECKS FAILED: {len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"\nCHECKS PASSED: {len(checks)}/{len(checks)}")
print("DONE.")

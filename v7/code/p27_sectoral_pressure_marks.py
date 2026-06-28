#!/usr/bin/env python3
"""
Paper 27 receipt: sectoral pressure law with explicit matter marks.

The Fourier boundary receipt showed that pressure density cannot simply ban
coherent modes, because some Fourier structure may be field-like rather than
geometric staging.  This receipt tests a sectoral rule:

    pressure applies to the geometry residual after removing the part carried
    by explicit matter/mark fields.

Given a symmetric zero-row kernel D and node marks F, form the mark-generated
pair-kernel span from symmetric products f_a(i) f_b(j)+f_b(i) f_a(j).  Project
D onto that span in off-diagonal Frobenius inner product.  The candidate
geometry diagnostic is the pressure density of the residual D - Pi_F D.

Hostile checks:

  * correct Fourier marks rescue pure Fourier geometry pressure;
  * wrong Fourier marks do not rescue the wrong frequency;
  * physical-plus-Fourier loses mark-carried amplitude, but the normalized
    residual pressure shape need not decrease;
  * block marks can launder a block only by paying a field-energy cost that
    grows with N, unlike low-frequency Fourier marks.

This is not a theorem.  It is a finite receipt for the proposed sector split:
geometry pressure plus marked matter/field-energy bookkeeping.  Failures of
the naive "just project marks and apply pressure" rule are treated as useful
constraints.

All asserted non-integer arithmetic uses mpmath with dps=140.
"""

from functools import lru_cache
import math
import sys

import mpmath as mp

sys.stdout.reconfigure(line_buffering=True)
mp.mp.dps = 140


def fmt(x, n=32):
    return mp.nstr(x, n)


checks = []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")


def zero_matrix(n):
    return [[mp.mpf(0) for _ in range(n)] for _ in range(n)]


def copy_matrix(D):
    return [[mp.mpf(value) for value in row] for row in D]


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


def add_matrices(A, B, scale_B=mp.mpf(1)):
    n = len(A)
    out = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            out[i][j] = A[i][j] + scale_B * B[i][j]
    return out


def axis_excess(D):
    n = len(D)
    return mp.fsum(D[i][j] ** 2 for i in range(n) for j in range(n) if i != j) / (
        mp.mpf(n) * (n - 1)
    )


def normalize_A_one(D):
    A = axis_excess(D)
    if A == 0:
        raise ValueError("zero matrix")
    scale = 1 / mp.sqrt(A)
    n = len(D)
    return [[scale * D[i][j] for j in range(n)] for i in range(n)], A


def max_row_linf(D):
    n = len(D)
    return max(abs(mp.fsum(D[i][j] for j in range(n) if i != j)) for i in range(n))


def offdiag_inner(A, B):
    n = len(A)
    return mp.fsum(A[i][j] * B[i][j] for i in range(n) for j in range(n) if i != j)


def falling(n, k):
    out = mp.mpf(1)
    for value in range(k):
        out *= n - value
    return out


def matching_sums(D):
    n = len(D)
    full = (1 << n) - 1

    @lru_cache(maxsize=None)
    def rec(mask):
        if mask == 0:
            return (mp.mpf(1),)
        first_bit = mask & -mask
        i = first_bit.bit_length() - 1
        rest = mask ^ first_bit
        base = list(rec(rest))
        out = base + [mp.mpf(0)]
        remaining = rest
        while remaining:
            bit = remaining & -remaining
            j = bit.bit_length() - 1
            sub = rec(rest ^ bit)
            weight = D[i][j]
            if len(out) < len(sub) + 1:
                out.extend(mp.mpf(0) for _ in range(len(sub) + 1 - len(out)))
            for r, value in enumerate(sub):
                out[r + 1] += weight * value
            remaining ^= bit
        return tuple(out)

    return rec(full)


def matching_metrics(D):
    n = len(D)
    A = axis_excess(D)
    if A < mp.mpf("1e-80"):
        return {
            "A": A,
            "q2": mp.mpf(0),
            "tail_ratio": mp.mpf(0),
            "pressure_density": mp.mpf(0),
            "formula_q2": mp.mpf(0),
            "row_linf": max_row_linf(D),
        }
    D1, _ = normalize_A_one(D)
    sums = matching_sums(D1)
    coeffs = {}
    for r in range(1, min(len(sums), n // 2 + 1)):
        rho = mp.mpf(math.factorial(r)) * (mp.mpf(2) ** r) * sums[r] / falling(n, 2 * r)
        coeffs[r] = mp.mpf(math.comb(n // 2, r)) * rho * rho
    q2 = coeffs.get(2, mp.mpf(0))
    tail = mp.fsum(coeffs[r] for r in coeffs if r >= 3)
    zN = 1 + mp.fsum(coeffs[r] * (mp.mpf(n) ** r) for r in coeffs if r >= 2)
    formula_q2 = mp.mpf(math.comb(n // 2, 2)) * (
        2 / ((mp.mpf(n) - 2) * (mp.mpf(n) - 3))
    ) ** 2
    return {
        "A": A,
        "q2": q2,
        "tail_ratio": tail / q2 if q2 else mp.mpf(0),
        "pressure_density": mp.log(zN) / n,
        "formula_q2": formula_q2,
        "row_linf": max_row_linf(D1),
    }


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


def physical_delta_D(n, c, nodes):
    c = mp.mpf(c)
    s_nodes = legendre_nodes(nodes, 0, 1)
    e0_nodes = legendre_nodes(nodes, -c, c)
    e1_nodes = legendre_nodes(nodes + 1, -c, c)
    matrix = zero_matrix(n)
    density_factor = 1 / (4 * c * c)
    for s, ws in s_nodes:
        for e0, we0 in e0_nodes:
            r0 = clamp_unit(marginal_cdf(s + e0, c))
            for e1, we1 in e1_nodes:
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

    total = mp.fsum(sym[i][j] for i in range(n) for j in range(n) if i != j)
    uniform = 1 / (mp.mpf(n) * (n - 1))
    residue = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                residue[i][j] = mp.mpf(n) * (n - 1) * (sym[i][j] / total - uniform)
    return project_symmetric_zero_row(residue)


def cosine_D(n, frequency):
    matrix = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = mp.cos(2 * mp.pi * frequency * (i - j) / n)
    return project_symmetric_zero_row(matrix)


def block_D(n):
    matrix = zero_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                same = (i < n // 2 and j < n // 2) or (i >= n // 2 and j >= n // 2)
                matrix[i][j] = mp.mpf(1) if same else mp.mpf(-1)
    return project_symmetric_zero_row(matrix)


def combined_normalized(D0, D1, lam):
    A0, _ = normalize_A_one(D0)
    A1, _ = normalize_A_one(D1)
    return project_symmetric_zero_row(add_matrices(A0, A1, mp.mpf(lam)))


def centered_features(features):
    centered = []
    for feature in features:
        mean = mp.fsum(feature) / len(feature)
        centered.append([mp.mpf(value) - mean for value in feature])
    return centered


def orthonormal_features(features):
    out = []
    for feature in centered_features(features):
        v = list(feature)
        for basis in out:
            coeff = mp.fsum(v[i] * basis[i] for i in range(len(v)))
            v = [v[i] - coeff * basis[i] for i in range(len(v))]
        norm2 = mp.fsum(value * value for value in v)
        if norm2 > mp.mpf("1e-80"):
            norm = mp.sqrt(norm2)
            out.append([value / norm for value in v])
    return out


def feature_energy(features):
    ortho = orthonormal_features(features)
    n = len(ortho[0]) if ortho else 0
    total = mp.mpf(0)
    for feature in ortho:
        total += (mp.mpf(n) ** 2) * mp.fsum(
            (feature[(i + 1) % n] - feature[i]) ** 2 for i in range(n)
        )
    return total


def pair_basis_from_features(features):
    ortho = orthonormal_features(features)
    if not ortho:
        return []
    n = len(ortho[0])
    basis = []
    for a in range(len(ortho)):
        for b in range(a, len(ortho)):
            matrix = zero_matrix(n)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    if a == b:
                        matrix[i][j] = ortho[a][i] * ortho[a][j]
                    else:
                        matrix[i][j] = ortho[a][i] * ortho[b][j] + ortho[b][i] * ortho[a][j]
            projected = project_symmetric_zero_row(matrix)
            if axis_excess(projected) > mp.mpf("1e-80"):
                basis.append(projected)
    return basis


def project_onto_mark_span(D, features):
    basis = pair_basis_from_features(features)
    n = len(D)
    if not basis:
        return zero_matrix(n)
    gram = mp.matrix(len(basis))
    rhs = mp.matrix(len(basis), 1)
    for i, Bi in enumerate(basis):
        rhs[i] = offdiag_inner(D, Bi)
        for j, Bj in enumerate(basis):
            gram[i, j] = offdiag_inner(Bi, Bj)
    coeffs = mp.lu_solve(gram, rhs)
    projection = zero_matrix(n)
    for k, Bk in enumerate(basis):
        for i in range(n):
            for j in range(n):
                projection[i][j] += coeffs[k] * Bk[i][j]
    return project_symmetric_zero_row(projection)


def residual_after_marks(D, features):
    projection = project_onto_mark_span(D, features)
    return project_symmetric_zero_row(add_matrices(D, projection, -1))


def fourier_features(n, frequency):
    return [
        [mp.cos(2 * mp.pi * frequency * i / n) for i in range(n)],
        [mp.sin(2 * mp.pi * frequency * i / n) for i in range(n)],
    ]


def block_features(n):
    return [[mp.mpf(1) if i < n // 2 else mp.mpf(-1) for i in range(n)]]


def run_case(label, D, features):
    residual = residual_after_marks(D, features)
    raw = matching_metrics(D)
    residual_metrics = matching_metrics(residual)
    energy = feature_energy(features) if features else mp.mpf(0)
    print(
        f"{label:28s} raw_p={fmt(raw['pressure_density'], 12)} "
        f"res_p={fmt(residual_metrics['pressure_density'], 12)} "
        f"res_A={fmt(residual_metrics['A'], 12)} mark_E={fmt(energy, 12)}"
    )
    return {
        "label": label,
        "raw": raw,
        "residual": residual_metrics,
        "energy": energy,
    }


print("=" * 80)
print("Paper 27 sectoral pressure with marks receipt")
print("=" * 80)
print(f"mp.dps = {mp.mp.dps}")

nodes = 10
sizes = [8, 10, 12, 14, 16]
rows = {}
max_q2_error = mp.mpf(0)
max_row_after = mp.mpf(0)

for n in sizes:
    print("\n" + "=" * 80)
    print(f"N={n}")
    print("=" * 80)
    cos1 = cosine_D(n, 1)
    cos2 = cosine_D(n, 2)
    block = block_D(n)
    rows[(n, "cos1_none")] = run_case("cos1 / no marks", cos1, [])
    rows[(n, "cos1_correct")] = run_case("cos1 / cos1 marks", cos1, fourier_features(n, 1))
    rows[(n, "cos2_wrong")] = run_case("cos2 / cos1 marks", cos2, fourier_features(n, 1))
    rows[(n, "cos2_correct")] = run_case("cos2 / cos2 marks", cos2, fourier_features(n, 2))
    rows[(n, "block_wrong")] = run_case("block / cos1 marks", block, fourier_features(n, 1))
    rows[(n, "block_marked")] = run_case("block / block mark", block, block_features(n))
    if n <= 14:
        physical = physical_delta_D(n, mp.mpf("0.5"), nodes)
        mixed = combined_normalized(physical, cos1, mp.mpf("1"))
        rows[(n, "mixed_none")] = run_case("phys+cos1 / no marks", mixed, [])
        rows[(n, "mixed_correct")] = run_case(
            "phys+cos1 / cos1 marks", mixed, fourier_features(n, 1)
        )
    for row in rows.values():
        max_row_after = max(max_row_after, row["raw"]["row_linf"], row["residual"]["row_linf"])
        if row["raw"]["q2"]:
            max_q2_error = max(max_q2_error, abs(row["raw"]["q2"] - row["raw"]["formula_q2"]))
        if row["residual"]["q2"]:
            max_q2_error = max(
                max_q2_error,
                abs(row["residual"]["q2"] - row["residual"]["formula_q2"]),
            )

cos1_raw_pressures = [rows[(n, "cos1_none")]["raw"]["pressure_density"] for n in sizes]
cos1_residual_pressures = [rows[(n, "cos1_correct")]["residual"]["pressure_density"] for n in sizes]
cos2_wrong_pressures = [rows[(n, "cos2_wrong")]["residual"]["pressure_density"] for n in sizes]
block_mark_energies = [rows[(n, "block_marked")]["energy"] for n in sizes]
cos1_mark_energies = [rows[(n, "cos1_correct")]["energy"] for n in sizes]
block_mark_residuals = [rows[(n, "block_marked")]["residual"]["pressure_density"] for n in sizes]
block_wrong_residuals = [rows[(n, "block_wrong")]["residual"]["pressure_density"] for n in sizes]
mixed_raw = [rows[(n, "mixed_none")]["raw"]["pressure_density"] for n in sizes if n <= 14]
mixed_residual = [
    rows[(n, "mixed_correct")]["residual"]["pressure_density"] for n in sizes if n <= 14
]
mixed_raw_A = [rows[(n, "mixed_none")]["raw"]["A"] for n in sizes if n <= 14]
mixed_residual_A = [
    rows[(n, "mixed_correct")]["residual"]["A"] for n in sizes if n <= 14
]
physical_residual_A = [rows[(n, "cos1_correct")]["residual"]["A"] for n in sizes]

print("\n=== Summary ===")
print("cos1 raw pressure = " + ", ".join(fmt(value, 12) for value in cos1_raw_pressures))
print(
    "cos1 residual pressure with correct marks = "
    + ", ".join(fmt(value, 12) for value in cos1_residual_pressures)
)
print(
    "cos2 residual pressure with wrong cos1 marks = "
    + ", ".join(fmt(value, 12) for value in cos2_wrong_pressures)
)
print("cos1 mark energy = " + ", ".join(fmt(value, 12) for value in cos1_mark_energies))
print("block mark energy = " + ", ".join(fmt(value, 12) for value in block_mark_energies))
print("mixed raw pressure = " + ", ".join(fmt(value, 12) for value in mixed_raw))
print("mixed residual pressure = " + ", ".join(fmt(value, 12) for value in mixed_residual))
print("mixed raw A = " + ", ".join(fmt(value, 12) for value in mixed_raw_A))
print("mixed residual A = " + ", ".join(fmt(value, 12) for value in mixed_residual_A))

check(
    "zero-row projection is enforced",
    max_row_after < mp.mpf("1e-80"),
    f"max_row_after={fmt(max_row_after, 18)}",
)
check(
    "universal q2 coefficient is reproduced when residual is nonzero",
    max_q2_error < mp.mpf("1e-80"),
    f"max_q2_error={fmt(max_q2_error, 18)}",
)
check(
    "correct Fourier marks erase pure cos1 geometry pressure",
    max(cos1_residual_pressures) < mp.mpf("1e-40")
    and max(physical_residual_A) < mp.mpf("1e-40"),
    "max_res_p=" + fmt(max(cos1_residual_pressures), 12)
    + " max_res_A=" + fmt(max(physical_residual_A), 12),
)
check(
    "wrong Fourier marks do not erase cos2 pressure",
    max(cos2_wrong_pressures) > mp.mpf("0.7"),
    "max_wrong_res_p=" + fmt(max(cos2_wrong_pressures), 12),
)
check(
    "correct Fourier marks remove mixed wave amplitude but not always pressure shape",
    all(mixed_residual_A[i] < mixed_raw_A[i] for i in range(len(mixed_raw_A)))
    and max(mixed_residual) > max(mixed_raw),
    f"max_mixed_raw_p={fmt(max(mixed_raw), 12)} max_mixed_res_p={fmt(max(mixed_residual), 12)} "
    f"max_resA/rawA={fmt(max(mixed_residual_A[i] / mixed_raw_A[i] for i in range(len(mixed_raw_A))), 12)}",
)
check(
    "block can be marked away only with growing mark energy",
    max(block_mark_residuals) < mp.mpf("1e-40")
    and all(block_mark_energies[i] < block_mark_energies[i + 1] for i in range(len(block_mark_energies) - 1)),
    "block_energy=" + ", ".join(fmt(value, 8) for value in block_mark_energies),
)
check(
    "low-frequency Fourier mark energy stays bounded while block energy grows",
    max(cos1_mark_energies) < mp.mpf("80")
    and block_mark_energies[-1] > mp.mpf("1.5") * block_mark_energies[0],
    f"max_cos_E={fmt(max(cos1_mark_energies), 12)} block_growth="
    f"{fmt(block_mark_energies[-1] / block_mark_energies[0], 12)}",
)
check(
    "smooth marks can partially but not uniformly launder block geometry",
    min(block_wrong_residuals) < mp.mpf("0.7") and max(block_wrong_residuals) > mp.mpf("0.8"),
    "block_wrong_res_p=" + ", ".join(fmt(value, 12) for value in block_wrong_residuals),
)

print("\n=== Consequence ===")
print("The sectoral split partly works and partly fails in exactly the useful")
print("places.  Correct Fourier marks remove pure Fourier pressure, and wrong")
print("Fourier marks do not erase the wrong frequency.  In mixed physical-plus-wave")
print("kernels the mark projection removes amplitude, but the A-normalized residual")
print("pressure shape can increase.  Smooth marks can also partially launder block")
print("geometry because a step has low-frequency components.  The law therefore")
print("cannot be only 'project out marks and apply pressure'.  It needs a coupled")
print("budget: residual geometry pressure, residual amplitude, mark field energy,")
print("and a rule preventing marks from silently defining the geometry itself.")

print("\n" + "=" * 80)
passed = sum(1 for _, ok, _ in checks if ok)
total = len(checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
print(f"\nCHECKS PASSED: {passed}/{total}")
if passed != total:
    raise SystemExit(1)
print("DONE.")

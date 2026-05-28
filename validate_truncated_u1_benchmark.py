"""Finite-block validation for the truncated compact U(1) gauge-matter benchmark.

Covers three layers at pure-stdlib scale:

  1. Exact Gauss commutation and Gauss-sector decomposition of the combined
     matter-link Hamiltonian on an L=2 ring with K=1 link truncation.
  2. Exact physical-sector elimination: on each compatible (Gauss sector,
     global-flux seed w) block, the reduced matter Hamiltonian obtained from
     the full matter-link problem agrees with the explicit Coulomb-string
     formula of the benchmark paper.
  3. First exact interaction-sensitive exchange-defect coefficient on the
     minimal reduced three-state prototype extracted from an L=4 one-particle
     sector at fixed flux seed w, verifying the c4 = t^4 and
     c6 = t^4*[(13/6)t^2 - (delta_{n+3/2}(X)^2 + delta_{n+1/2}(Y)^2)/12]
     structure with the delta gaps populated by the quadratic Coulomb-string
     interaction.
"""
from __future__ import annotations

import math
from typing import Iterable, List


Matrix = List[List[complex]]


def eye(size: int) -> Matrix:
    return [[1.0 + 0.0j if row == col else 0.0j for col in range(size)] for row in range(size)]


def zeros(rows: int, cols: int) -> Matrix:
    return [[0.0 + 0.0j for _ in range(cols)] for _ in range(rows)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    rows = len(left)
    cols = len(right[0])
    inner = len(right)
    result = zeros(rows, cols)
    for row in range(rows):
        for col in range(cols):
            total = 0.0 + 0.0j
            for index in range(inner):
                total += left[row][index] * right[index][col]
            result[row][col] = total
    return result


def add(left: Matrix, right: Matrix) -> Matrix:
    return [[left[row][col] + right[row][col] for col in range(len(left[0]))] for row in range(len(left))]


def scale(matrix: Matrix, scalar: complex) -> Matrix:
    return [[scalar * value for value in row] for row in matrix]


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return add(matmul(left, right), scale(matmul(right, left), -1.0))


def max_abs(matrix: Matrix) -> float:
    best = 0.0
    for row in matrix:
        for value in row:
            best = max(best, abs(value))
    return best


def inverse(matrix: Matrix) -> Matrix:
    size = len(matrix)
    augmented = [row[:] + identity_row[:] for row, identity_row in zip(matrix, eye(size))]
    for pivot_index in range(size):
        pivot_row = max(range(pivot_index, size), key=lambda row: abs(augmented[row][pivot_index]))
        pivot_value = augmented[pivot_row][pivot_index]
        if abs(pivot_value) < 1e-15:
            raise ValueError("matrix is singular")
        augmented[pivot_index], augmented[pivot_row] = augmented[pivot_row], augmented[pivot_index]
        normalized_pivot = augmented[pivot_index][pivot_index]
        augmented[pivot_index] = [entry / normalized_pivot for entry in augmented[pivot_index]]
        for row in range(size):
            if row == pivot_index:
                continue
            factor = augmented[row][pivot_index]
            if abs(factor) == 0.0:
                continue
            augmented[row] = [
                augmented[row][col] - factor * augmented[pivot_index][col]
                for col in range(2 * size)
            ]
    return [row[size:] for row in augmented]


def matrix_exp(hamiltonian: Matrix, delta: float, terms: int = 50) -> Matrix:
    result = eye(len(hamiltonian))
    term = eye(len(hamiltonian))
    factor = -1j * delta
    for order in range(1, terms + 1):
        term = matmul(term, hamiltonian)
        term = scale(term, factor / order)
        result = add(result, term)
    return result


def gamma(unitary: Matrix) -> Matrix:
    size = len(unitary)
    result = zeros(size, size)
    for row in range(size):
        for col in range(size):
            result[row][col] = abs(unitary[row][col]) ** 2
    return result


def comparison_map(reference_hamiltonian: Matrix, localized_hamiltonian: Matrix, delta: float) -> Matrix:
    gamma_reference = gamma(matrix_exp(reference_hamiltonian, delta))
    gamma_localized = gamma(matrix_exp(localized_hamiltonian, delta))
    return matmul(gamma_localized, inverse(gamma_reference))


def exchange_defect(left: Matrix, right: Matrix) -> Matrix:
    return matmul(matmul(matmul(left, right), inverse(left)), inverse(right))


def solve_linear_system(matrix: list[list[float]], values: list[float]) -> list[float]:
    size = len(values)
    augmented = [row[:] + [values[index]] for index, row in enumerate(matrix)]
    for pivot_index in range(size):
        pivot_row = max(range(pivot_index, size), key=lambda row: abs(augmented[row][pivot_index]))
        pivot_value = augmented[pivot_row][pivot_index]
        if abs(pivot_value) < 1e-20:
            raise ValueError("system is singular")
        augmented[pivot_index], augmented[pivot_row] = augmented[pivot_row], augmented[pivot_index]
        normalized = augmented[pivot_index][pivot_index]
        augmented[pivot_index] = [entry / normalized for entry in augmented[pivot_index]]
        for row in range(size):
            if row == pivot_index:
                continue
            factor = augmented[row][pivot_index]
            augmented[row] = [
                augmented[row][col] - factor * augmented[pivot_index][col]
                for col in range(size + 1)
            ]
    return [augmented[row][-1] for row in range(size)]


def fit_even_power_series(sample_deltas: Iterable[float], sample_values: Iterable[complex], powers: list[int]) -> list[float]:
    deltas = list(sample_deltas)
    minimum_power = min(powers)
    shifted_powers = [power - minimum_power for power in powers]
    values = [value.real / (delta ** minimum_power) for delta, value in zip(deltas, sample_values)]
    vandermonde = [[delta ** power for power in shifted_powers] for delta in deltas]
    return solve_linear_system(vandermonde, values)


def relative_error(extracted: float, expected: float) -> float:
    reference = max(1.0, abs(expected))
    return abs(extracted - expected) / reference


def fermion_basis(num_sites: int) -> list[tuple[int, ...]]:
    return [tuple((state >> shift) & 1 for shift in range(num_sites - 1, -1, -1)) for state in range(2 ** num_sites)]


def link_basis(num_links: int, truncation: int) -> list[tuple[int, ...]]:
    dim = 2 * truncation + 1
    total = dim ** num_links
    result: list[tuple[int, ...]] = []
    for index in range(total):
        cursor = index
        entries = []
        for _ in range(num_links):
            entries.append(cursor % dim - truncation)
            cursor //= dim
        result.append(tuple(entries))
    return result


def combined_basis(num_sites: int, num_links: int, truncation: int) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    fermions = fermion_basis(num_sites)
    links = link_basis(num_links, truncation)
    return [(matter, flux) for matter in fermions for flux in links]


def hopping_sign(matter: tuple[int, ...], source: int, target: int) -> int:
    low, high = sorted((source, target))
    parity = 0
    for site in range(low + 1, high):
        parity ^= matter[site]
    return -1 if parity else 1


def build_mass_hamiltonian(
    basis: list[tuple[tuple[int, ...], tuple[int, ...]]],
    mass: float,
) -> Matrix:
    size = len(basis)
    result = zeros(size, size)
    for index, (matter, _flux) in enumerate(basis):
        energy = 0.0
        for site, occupation in enumerate(matter):
            energy += mass * ((-1) ** site) * occupation
        result[index][index] = energy
    return result


def build_electric_hamiltonian(
    basis: list[tuple[tuple[int, ...], tuple[int, ...]]],
    coupling: float,
) -> Matrix:
    size = len(basis)
    result = zeros(size, size)
    for index, (_matter, flux) in enumerate(basis):
        energy = 0.5 * coupling * coupling * sum(value * value for value in flux)
        result[index][index] = energy
    return result


def build_hopping_hamiltonian(
    basis: list[tuple[tuple[int, ...], tuple[int, ...]]],
    hopping: float,
    truncation: int,
    bonds: list[tuple[int, int, int]],
) -> Matrix:
    """Bonds are triples (source, target, link_index). A +1 fermion moves from
    source to target, and the Wilson link operator lowers the electric
    eigenvalue at link_index by one (so the adjoint raises it)."""

    size = len(basis)
    index_of = {state: idx for idx, state in enumerate(basis)}
    result = zeros(size, size)
    for source, target, link_index in bonds:
        for index, (matter, flux) in enumerate(basis):
            if matter[source] != 1 or matter[target] != 0:
                continue
            new_matter = list(matter)
            new_matter[source] = 0
            new_matter[target] = 1
            new_flux = list(flux)
            new_flux[link_index] = flux[link_index] - 1
            if abs(new_flux[link_index]) > truncation:
                continue
            sign = hopping_sign(matter, source, target)
            new_state = (tuple(new_matter), tuple(new_flux))
            new_index = index_of[new_state]
            result[new_index][index] += -hopping * sign
            result[index][new_index] += -hopping * sign
    return result


def build_obc_gauss_generator(
    basis: list[tuple[tuple[int, ...], tuple[int, ...]]],
    site: int,
    background: list[int],
) -> Matrix:
    """G_n = E_{link n} - E_{link n-1} - (N_n - q^bg_n) on an OBC chain.

    Valid for interior sites 1 <= site <= L - 2 where both links exist.
    """

    size = len(basis)
    result = zeros(size, size)
    right_link = site
    left_link = site - 1
    for index, (matter, flux) in enumerate(basis):
        value = flux[right_link] - flux[left_link] - (matter[site] - background[site])
        result[index][index] = value
    return result


def coulomb_prefix(matter: tuple[int, ...], background: list[int], seed: int) -> list[int]:
    prefix = []
    running = seed
    for site in range(len(matter)):
        running = running + (matter[site] - background[site])
        prefix.append(running)
    return prefix


def build_reduced_matter_hamiltonian(
    matter_states: list[tuple[int, ...]],
    num_links: int,
    mass: float,
    coupling: float,
    hopping: float,
    background: list[int],
    seed: int,
    bonds: list[tuple[int, int, int]],
    truncation: int,
) -> Matrix:
    """Exact reduced matter Hamiltonian on a fixed Gauss sector and fixed
    left-boundary flux seed. The bond list is inherited from the full model
    and used to decide which hops respect the truncation."""

    size = len(matter_states)
    index_of = {state: idx for idx, state in enumerate(matter_states)}
    result = zeros(size, size)
    for index, matter in enumerate(matter_states):
        prefix = coulomb_prefix(matter, background, seed)
        mass_energy = mass * sum(((-1) ** site) * occupation for site, occupation in enumerate(matter))
        electric_energy = 0.5 * coupling * coupling * sum(value * value for value in prefix[:num_links])
        result[index][index] = mass_energy + electric_energy
    for source, target, link_index in bonds:
        for index, matter in enumerate(matter_states):
            if matter[source] != 1 or matter[target] != 0:
                continue
            prefix = coulomb_prefix(matter, background, seed)
            new_prefix_value = prefix[link_index] - 1
            if abs(new_prefix_value) > truncation:
                continue
            new_matter = list(matter)
            new_matter[source] = 0
            new_matter[target] = 1
            new_state = tuple(new_matter)
            if new_state not in index_of:
                continue
            sign = hopping_sign(matter, source, target)
            new_index = index_of[new_state]
            result[new_index][index] += -hopping * sign
            result[index][new_index] += -hopping * sign
    return result


def restrict_matrix_to_indices(matrix: Matrix, indices: list[int]) -> Matrix:
    size = len(indices)
    result = zeros(size, size)
    for row in range(size):
        for col in range(size):
            result[row][col] = matrix[indices[row]][indices[col]]
    return result


def embed_matter_config(
    matter: tuple[int, ...],
    num_links: int,
    background: list[int],
    seed: int,
    truncation: int,
) -> tuple[int, ...] | None:
    prefix = coulomb_prefix(matter, background, seed)
    flux = prefix[:num_links]
    if any(abs(value) > truncation for value in flux):
        return None
    return tuple(flux)


def gauss_check(num_sites: int, truncation: int, mass: float, coupling: float, hopping: float, background: list[int]) -> float:
    num_links = num_sites - 1
    basis = combined_basis(num_sites, num_links, truncation)
    bonds: list[tuple[int, int, int]] = []
    for site in range(num_links):
        bonds.append((site, site + 1, site))
    full = add(
        add(
            build_mass_hamiltonian(basis, mass),
            build_electric_hamiltonian(basis, coupling),
        ),
        build_hopping_hamiltonian(basis, hopping, truncation, bonds),
    )
    worst = 0.0
    for site in range(1, num_sites - 1):
        generator = build_obc_gauss_generator(basis, site, background)
        worst = max(worst, max_abs(commutator(generator, full)))
    return worst


def elimination_check(num_sites: int, truncation: int, mass: float, coupling: float, hopping: float, background: list[int]) -> tuple[int, float]:
    num_links = num_sites - 1
    basis = combined_basis(num_sites, num_links, truncation)
    index_of = {state: idx for idx, state in enumerate(basis)}
    bonds: list[tuple[int, int, int]] = []
    for site in range(num_links):
        bonds.append((site, site + 1, site))
    full = add(
        add(
            build_mass_hamiltonian(basis, mass),
            build_electric_hamiltonian(basis, coupling),
        ),
        build_hopping_hamiltonian(basis, hopping, truncation, bonds),
    )

    fermions = fermion_basis(num_sites)
    neutral_matter_states = [
        matter
        for matter in fermions
        if sum(matter) == sum(background)
    ]

    worst = 0.0
    checked_blocks = 0
    for seed in range(-truncation, truncation + 1):
        embedded = []
        matter_block = []
        for matter in neutral_matter_states:
            flux = embed_matter_config(matter, num_links, background, seed, truncation)
            if flux is None:
                continue
            full_state = (matter, flux)
            if full_state not in index_of:
                continue
            embedded.append(index_of[full_state])
            matter_block.append(matter)
        if len(matter_block) < 2:
            continue
        restricted = restrict_matrix_to_indices(full, embedded)
        reduced = build_reduced_matter_hamiltonian(
            matter_block, num_links, mass, coupling, hopping, background, seed, bonds, truncation,
        )
        diff = add(restricted, scale(reduced, -1.0))
        worst = max(worst, max_abs(diff))
        checked_blocks += 1
    return checked_blocks, worst


def prototype_theorem3_check(hopping: float, mass: float, coupling: float, seed: int) -> tuple[float, float, float, float, float, float]:
    """Minimal reduced three-state prototype extracted from an L=4 one-particle
    sector at background q=(1,0,0,0) and fixed flux seed w.

    States X = (0,0,0,1), Y = (0,0,1,0), Z = (0,1,0,0).
    """

    background = [1, 0, 0, 0]
    states = [
        (0, 0, 0, 1),
        (0, 0, 1, 0),
        (0, 1, 0, 0),
    ]
    num_links = len(background) - 1

    diagonal: list[float] = []
    for matter in states:
        prefix = coulomb_prefix(matter, background, seed)
        electric = 0.5 * coupling * coupling * sum(value * value for value in prefix[:num_links])
        mass_energy = mass * sum(((-1) ** site) * occupation for site, occupation in enumerate(matter))
        diagonal.append(electric + mass_energy)

    reference_hamiltonian = zeros(3, 3)
    for i in range(3):
        reference_hamiltonian[i][i] = diagonal[i]
    reference_hamiltonian[0][1] = -hopping
    reference_hamiltonian[1][0] = -hopping
    reference_hamiltonian[1][2] = -hopping
    reference_hamiltonian[2][1] = -hopping

    left_hamiltonian = zeros(3, 3)
    for i in range(3):
        left_hamiltonian[i][i] = diagonal[i]
    left_hamiltonian[0][1] = -hopping
    left_hamiltonian[1][0] = -hopping

    right_hamiltonian = zeros(3, 3)
    for i in range(3):
        right_hamiltonian[i][i] = diagonal[i]
    right_hamiltonian[1][2] = -hopping
    right_hamiltonian[2][1] = -hopping

    deltas = [0.010, 0.012, 0.014, 0.016]
    entries: list[complex] = []
    for delta in deltas:
        left_map = comparison_map(reference_hamiltonian, left_hamiltonian, delta)
        right_map = comparison_map(reference_hamiltonian, right_hamiltonian, delta)
        defect = exchange_defect(left_map, right_map)
        entries.append(defect[2][0])

    extracted_c4, extracted_c6, _, _ = fit_even_power_series(deltas, entries, [4, 6, 8, 10])

    gap_x = diagonal[0] - diagonal[1]
    gap_y = diagonal[2] - diagonal[1]
    predicted_c4 = hopping ** 4
    predicted_c6 = hopping ** 4 * (
        (13.0 / 6.0) * hopping ** 2 - (gap_x ** 2 + gap_y ** 2) / 12.0
    )
    return extracted_c4, predicted_c4, extracted_c6, predicted_c6, gap_x, gap_y


def main() -> None:
    print("Truncated U(1) matter-link benchmark validation")
    print()

    mass = 0.35
    coupling = 0.7
    hopping = 1.0
    background = [1, 0, 1]

    commutation_residual = gauss_check(3, 2, mass, coupling, hopping, background)
    print("Gauss commutation on L=3 OBC, K=2")
    print(f"  max |[G_n, H]|                 = {commutation_residual:.3e}")
    print()

    checked_blocks, elimination_residual = elimination_check(3, 2, mass, coupling, hopping, background)
    print("Elimination match on L=3 OBC, K=2")
    print(f"  physical blocks checked        = {checked_blocks}")
    print(f"  max |H_full|_phys - H_reduced| = {elimination_residual:.3e}")
    print()

    print("Prototype Theorem 3 on L=4 one-particle sector, w = 0")
    c4_ext, c4_pred, c6_ext, c6_pred, gap_x, gap_y = prototype_theorem3_check(
        hopping=1.0, mass=0.35, coupling=0.7, seed=0,
    )
    print(f"  gap delta_{{n+3/2}}(X)            = {gap_x:.12f}")
    print(f"  gap delta_{{n+1/2}}(Y)            = {gap_y:.12f}")
    print(f"  extracted c4                   = {c4_ext:.12f}")
    print(f"  predicted  c4 = t^4            = {c4_pred:.12f}")
    print(f"  rel. error                     = {relative_error(c4_ext, c4_pred):.3e}")
    print(f"  extracted c6                   = {c6_ext:.12f}")
    print(f"  predicted  c6                  = {c6_pred:.12f}")
    print(f"  rel. error                     = {relative_error(c6_ext, c6_pred):.3e}")
    print()

    print("Prototype Theorem 3 on L=4 one-particle sector, w = 1")
    c4_ext2, c4_pred2, c6_ext2, c6_pred2, gap_x2, gap_y2 = prototype_theorem3_check(
        hopping=1.0, mass=0.35, coupling=0.7, seed=1,
    )
    print(f"  gap delta_{{n+3/2}}(X)            = {gap_x2:.12f}")
    print(f"  gap delta_{{n+1/2}}(Y)            = {gap_y2:.12f}")
    print(f"  extracted c4                   = {c4_ext2:.12f}")
    print(f"  predicted  c4 = t^4            = {c4_pred2:.12f}")
    print(f"  rel. error                     = {relative_error(c4_ext2, c4_pred2):.3e}")
    print(f"  extracted c6                   = {c6_ext2:.12f}")
    print(f"  predicted  c6                  = {c6_pred2:.12f}")
    print(f"  rel. error                     = {relative_error(c6_ext2, c6_pred2):.3e}")


if __name__ == "__main__":
    main()

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


def tri_diagonal(energies: list[float], hopping_bonds: list[tuple[int, int]], hopping_strength: float) -> Matrix:
    size = len(energies)
    matrix = zeros(size, size)
    for index, energy in enumerate(energies):
        matrix[index][index] = energy
    for left, right in hopping_bonds:
        matrix[left][right] = -hopping_strength
        matrix[right][left] = -hopping_strength
    return matrix


def particle_basis(num_sites: int) -> list[tuple[int, ...]]:
    return [tuple((state >> shift) & 1 for shift in range(num_sites - 1, -1, -1)) for state in range(2 ** num_sites)]


def reduced_diagonal_energy(state: tuple[int, ...], mass: float, electric_strength: float, lambdas: list[float]) -> float:
    mass_term = sum(((-1) ** site) * occupation for site, occupation in enumerate(state))
    prefix = 1
    electric_term = 0.0
    for site, occupation in enumerate(state):
        prefix *= -1 if occupation else 1
        electric_term += lambdas[site] * prefix
    return mass * mass_term - electric_strength * electric_term


def occupation_hamiltonian(
    basis: list[tuple[int, ...]],
    hopping_bonds: list[tuple[int, int]],
    hopping_strength: float,
    mass: float,
    electric_strength: float,
    lambdas: list[float],
) -> Matrix:
    index_of = {state: index for index, state in enumerate(basis)}
    matrix = zeros(len(basis), len(basis))

    for index, state in enumerate(basis):
        matrix[index][index] = reduced_diagonal_energy(state, mass, electric_strength, lambdas)
        for left, right in hopping_bonds:
            if state[left] == state[right]:
                continue
            moved = list(state)
            moved[left], moved[right] = moved[right], moved[left]
            moved_state = tuple(moved)
            matrix[index_of[moved_state]][index] = -hopping_strength
    return matrix


def theorem3_check() -> tuple[float, float, float, float]:
    hopping_strength = 1.0
    delta_left = 0.6
    delta_right = 2.2
    energy_y = 0.0
    energy_x = delta_left
    energy_z = delta_right

    reference_hamiltonian = tri_diagonal([energy_x, energy_y, energy_z], [(0, 1), (1, 2)], hopping_strength)
    left_hamiltonian = tri_diagonal([energy_x, energy_y, energy_z], [(0, 1)], hopping_strength)
    right_hamiltonian = tri_diagonal([energy_x, energy_y, energy_z], [(1, 2)], hopping_strength)

    deltas = [0.010, 0.012, 0.014, 0.016]
    entry_values = []
    for delta in deltas:
        left_map = comparison_map(reference_hamiltonian, left_hamiltonian, delta)
        right_map = comparison_map(reference_hamiltonian, right_hamiltonian, delta)
        defect = exchange_defect(left_map, right_map)
        entry_values.append(defect[2][0])

    extracted_c4, extracted_c6, _, _ = fit_even_power_series(deltas, entry_values, [4, 6, 8, 10])
    predicted_c4 = hopping_strength ** 4
    predicted_c6 = hopping_strength ** 4 * (
        (13.0 / 6.0) * hopping_strength ** 2 - (delta_left ** 2 + delta_right ** 2) / 12.0
    )
    return extracted_c4, predicted_c4, extracted_c6, predicted_c6


def proposition4c_check() -> dict[str, tuple[float, float]]:
    hopping_strength = 1.0
    energies = [0.8, -0.2, 1.1]
    reference_hamiltonian = tri_diagonal(energies, [(0, 1), (1, 2)], hopping_strength)
    localized_hamiltonian = tri_diagonal(energies, [(1, 2)], hopping_strength)

    deltas = [0.010, 0.012, 0.014, 0.016]
    maps = [comparison_map(reference_hamiltonian, localized_hamiltonian, delta) for delta in deltas]

    expected_entries = {
        "A4[Z,Y]": ((2, 1), 1.0 / 3.0),
        "A4[Y,Z]": ((1, 2), -2.0 / 3.0),
        "A4[X,Z]": ((0, 2), 3.0 / 4.0),
        "A4[Z,X]": ((2, 0), -1.0 / 4.0),
    }

    results: dict[str, tuple[float, float]] = {}
    for label, (indices, expected_value) in expected_entries.items():
        row, col = indices
        sample_values = [current_map[row][col] for current_map in maps]
        extracted_a4, _, _, _ = fit_even_power_series(deltas, sample_values, [4, 6, 8, 10])
        results[label] = (extracted_a4, expected_value)
    return results


def proposition4d_check() -> tuple[float, float]:
    hopping_strength = 1.0
    reference_hamiltonian = tri_diagonal([0.0, 0.0, 0.0, 0.0], [(0, 1), (1, 2), (2, 3)], hopping_strength)
    left_hamiltonian = tri_diagonal([0.0, 0.0, 0.0, 0.0], [(1, 2), (2, 3)], hopping_strength)
    right_hamiltonian = tri_diagonal([0.0, 0.0, 0.0, 0.0], [(0, 1), (1, 2)], hopping_strength)

    deltas = [0.010, 0.012, 0.014, 0.016]
    values = []
    for delta in deltas:
        left_map = comparison_map(reference_hamiltonian, left_hamiltonian, delta)
        right_map = comparison_map(reference_hamiltonian, right_hamiltonian, delta)
        defect = exchange_defect(left_map, right_map)
        values.append(defect[3][0])

    extracted_c6, _, _, _ = fit_even_power_series(deltas, values, [6, 8, 10, 12])
    predicted_c6 = 0.5 * hopping_strength ** 6
    return extracted_c6, predicted_c6


def fixed_strip_one_particle_fiber_check() -> tuple[Matrix, Matrix, float]:
    hopping_strength = 1.0
    # Generic frozen-exterior one-particle fiber energies with inactive outer bonds.
    reference_hamiltonian = tri_diagonal([0.7, -0.4, 1.3, 0.2], [(0, 1), (1, 2), (2, 3)], hopping_strength)
    left_hamiltonian = tri_diagonal([0.7, -0.4, 1.3, 0.2], [(1, 2), (2, 3)], hopping_strength)
    right_hamiltonian = tri_diagonal([0.7, -0.4, 1.3, 0.2], [(0, 1), (1, 2)], hopping_strength)

    deltas = [0.010, 0.012, 0.014, 0.016]
    extracted_matrix = zeros(4, 4)
    for row in range(4):
        for col in range(4):
            if row == col:
                continue
            sample_values = []
            for delta in deltas:
                left_map = comparison_map(reference_hamiltonian, left_hamiltonian, delta)
                right_map = comparison_map(reference_hamiltonian, right_hamiltonian, delta)
                defect = exchange_defect(left_map, right_map)
                sample_values.append(defect[row][col])
            extracted_c6, _, _, _ = fit_even_power_series(deltas, sample_values, [6, 8, 10, 12])
            extracted_matrix[row][col] = extracted_c6

    expected_matrix = zeros(4, 4)
    channel_coefficients = {
        (1, 0): -1.0 / 12.0,
        (2, 0): -5.0 / 12.0,
        (3, 0): 1.0 / 2.0,
        (2, 1): 1.0 / 3.0,
        (3, 1): -5.0 / 12.0,
        (3, 2): -1.0 / 12.0,
    }
    for (row, col), coefficient in channel_coefficients.items():
        expected_matrix[row][col] = coefficient
        expected_matrix[col][row] = -coefficient

    max_relative_error = 0.0
    for row in range(4):
        for col in range(4):
            if row == col:
                continue
            max_relative_error = max(
                max_relative_error,
                relative_error(extracted_matrix[row][col].real, expected_matrix[row][col].real),
            )
    return extracted_matrix, expected_matrix, max_relative_error


def full_fixed_strip_block_check() -> tuple[float, float, float]:
    basis = particle_basis(4)
    hopping_strength = 1.0
    mass = 0.7
    electric_strength = 0.5
    lambdas = [0.9, -0.4, 1.1, 0.2]

    reference_hamiltonian = occupation_hamiltonian(
        basis,
        [(0, 1), (1, 2), (2, 3)],
        hopping_strength,
        mass,
        electric_strength,
        lambdas,
    )
    left_hamiltonian = occupation_hamiltonian(
        basis,
        [(1, 2), (2, 3)],
        hopping_strength,
        mass,
        electric_strength,
        lambdas,
    )
    right_hamiltonian = occupation_hamiltonian(
        basis,
        [(0, 1), (1, 2)],
        hopping_strength,
        mass,
        electric_strength,
        lambdas,
    )

    defect = exchange_defect(comparison_map(reference_hamiltonian, left_hamiltonian, 0.015), comparison_map(reference_hamiltonian, right_hamiltonian, 0.015))
    particle_numbers = [sum(state) for state in basis]
    max_off_block = 0.0
    for row in range(len(basis)):
        for col in range(len(basis)):
            if particle_numbers[row] != particle_numbers[col]:
                max_off_block = max(max_off_block, abs(defect[row][col]))

    vacuum_index = basis.index((0, 0, 0, 0))
    full_index = basis.index((1, 1, 1, 1))
    scalar_block_deviation = max(abs(defect[vacuum_index][vacuum_index] - 1.0), abs(defect[full_index][full_index] - 1.0))

    one_particle_states = [
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (0, 0, 0, 1),
    ]
    one_particle_indices = [basis.index(state) for state in one_particle_states]

    deltas = [0.010, 0.012, 0.014, 0.016]
    extracted_matrix = zeros(4, 4)
    for row in range(4):
        for col in range(4):
            if row == col:
                continue
            sample_values = []
            for delta in deltas:
                current_defect = exchange_defect(
                    comparison_map(reference_hamiltonian, left_hamiltonian, delta),
                    comparison_map(reference_hamiltonian, right_hamiltonian, delta),
                )
                sample_values.append(current_defect[one_particle_indices[row]][one_particle_indices[col]])
            extracted_c6, _, _, _ = fit_even_power_series(deltas, sample_values, [6, 8, 10, 12])
            extracted_matrix[row][col] = extracted_c6

    expected_matrix = zeros(4, 4)
    channel_coefficients = {
        (1, 0): -1.0 / 12.0,
        (2, 0): -5.0 / 12.0,
        (3, 0): 1.0 / 2.0,
        (2, 1): 1.0 / 3.0,
        (3, 1): -5.0 / 12.0,
        (3, 2): -1.0 / 12.0,
    }
    for (row, col), coefficient in channel_coefficients.items():
        expected_matrix[row][col] = coefficient
        expected_matrix[col][row] = -coefficient

    max_one_particle_error = 0.0
    for row in range(4):
        for col in range(4):
            if row == col:
                continue
            max_one_particle_error = max(
                max_one_particle_error,
                relative_error(extracted_matrix[row][col].real, expected_matrix[row][col].real),
            )

    return max_off_block, abs(scalar_block_deviation), max_one_particle_error


def extract_sector_c6_matrix(
    basis: list[tuple[int, ...]],
    reference_hamiltonian: Matrix,
    left_hamiltonian: Matrix,
    right_hamiltonian: Matrix,
    sector_states: list[tuple[int, ...]],
    powers: list[int],
) -> Matrix:
    sector_indices = [basis.index(state) for state in sector_states]
    deltas = [0.010, 0.012, 0.014, 0.016]
    extracted_matrix = zeros(len(sector_states), len(sector_states))
    for row in range(len(sector_states)):
        for col in range(len(sector_states)):
            if row == col:
                continue
            sample_values = []
            for delta in deltas:
                current_defect = exchange_defect(
                    comparison_map(reference_hamiltonian, left_hamiltonian, delta),
                    comparison_map(reference_hamiltonian, right_hamiltonian, delta),
                )
                sample_values.append(current_defect[sector_indices[row]][sector_indices[col]])
            extracted_c6, _, _, _ = fit_even_power_series(deltas, sample_values, powers)
            extracted_matrix[row][col] = extracted_c6
    return extracted_matrix


def max_entrywise_difference(left: Matrix, right: Matrix) -> float:
    max_difference = 0.0
    for row in range(len(left)):
        for col in range(len(left[0])):
            max_difference = max(max_difference, abs(left[row][col] - right[row][col]))
    return max_difference


def two_particle_block_interaction_check() -> tuple[float, float]:
    basis = particle_basis(4)
    hopping_strength = 1.0
    mass = 0.7
    lambdas = [0.9, -0.4, 1.1, 0.2]
    two_particle_states = [
        (1, 1, 0, 0),
        (1, 0, 1, 0),
        (1, 0, 0, 1),
        (0, 1, 1, 0),
        (0, 1, 0, 1),
        (0, 0, 1, 1),
    ]

    def build_triplet(electric_strength: float) -> tuple[Matrix, Matrix, Matrix]:
        reference_hamiltonian = occupation_hamiltonian(
            basis,
            [(0, 1), (1, 2), (2, 3)],
            hopping_strength,
            mass,
            electric_strength,
            lambdas,
        )
        left_hamiltonian = occupation_hamiltonian(
            basis,
            [(1, 2), (2, 3)],
            hopping_strength,
            mass,
            electric_strength,
            lambdas,
        )
        right_hamiltonian = occupation_hamiltonian(
            basis,
            [(0, 1), (1, 2)],
            hopping_strength,
            mass,
            electric_strength,
            lambdas,
        )
        return reference_hamiltonian, left_hamiltonian, right_hamiltonian

    interacting_triplet = build_triplet(0.5)
    free_triplet = build_triplet(0.0)

    interacting_block = extract_sector_c6_matrix(
        basis,
        interacting_triplet[0],
        interacting_triplet[1],
        interacting_triplet[2],
        two_particle_states,
        [6, 8, 10, 12],
    )
    free_block = extract_sector_c6_matrix(
        basis,
        free_triplet[0],
        free_triplet[1],
        free_triplet[2],
        two_particle_states,
        [6, 8, 10, 12],
    )

    antisymmetry_error = 0.0
    for row in range(len(interacting_block)):
        for col in range(len(interacting_block)):
            antisymmetry_error = max(
                antisymmetry_error,
                abs(interacting_block[row][col] + interacting_block[col][row]),
            )

    interaction_signal = max_entrywise_difference(interacting_block, free_block)
    return antisymmetry_error, interaction_signal


def extract_comparison_map_order(
    reference_hamiltonian: Matrix,
    localized_hamiltonian: Matrix,
    deltas: list[float],
    fit_powers: list[int],
    target_power: int,
) -> Matrix:
    size = len(reference_hamiltonian)
    maps = [comparison_map(reference_hamiltonian, localized_hamiltonian, delta) for delta in deltas]
    target_index = fit_powers.index(target_power)
    result = zeros(size, size)
    for row in range(size):
        for col in range(size):
            samples = []
            for sample_map in maps:
                value = sample_map[row][col]
                if row == col:
                    value = value - 1.0
                samples.append(value)
            coefficients = fit_even_power_series(deltas, samples, fit_powers)
            result[row][col] = coefficients[target_index]
    return result


def proposition_h_check() -> tuple[float, float, Matrix, Matrix, Matrix]:
    """Proposition H: minimal one-particle five-site overlap prototype.

    Verify that the pure two-step overlap shell [A_n^[4], A_{n+4}^[4]]
    has end-to-end entry [4][0] equal to 3/16 t^8 at t = 1.
    """
    hopping_strength = 1.0
    energies = [0.0, 0.0, 0.0, 0.0, 0.0]
    reference_hamiltonian = tri_diagonal(
        energies, [(0, 1), (1, 2), (2, 3), (3, 4)], hopping_strength
    )
    left_hamiltonian = tri_diagonal(
        energies, [(1, 2), (2, 3), (3, 4)], hopping_strength
    )
    right_hamiltonian = tri_diagonal(
        energies, [(0, 1), (1, 2), (2, 3)], hopping_strength
    )

    deltas = [0.010, 0.012, 0.014, 0.016]
    fit_powers = [2, 4, 6, 8]

    a_left_4 = extract_comparison_map_order(
        reference_hamiltonian, left_hamiltonian, deltas, fit_powers, 4
    )
    a_right_4 = extract_comparison_map_order(
        reference_hamiltonian, right_hamiltonian, deltas, fit_powers, 4
    )

    commutator = add(
        matmul(a_left_4, a_right_4),
        scale(matmul(a_right_4, a_left_4), -1.0),
    )
    end_to_end = commutator[4][0].real
    expected = 3.0 / 16.0
    return end_to_end, expected, commutator, a_left_4, a_right_4


def relative_error(extracted: float, expected: float) -> float:
    scale = max(1.0, abs(expected))
    return abs(extracted - expected) / scale


def main() -> None:
    theorem3_extracted_c4, theorem3_expected_c4, theorem3_extracted_c6, theorem3_expected_c6 = theorem3_check()
    proposition4c_results = proposition4c_check()
    proposition4d_extracted_c6, proposition4d_expected_c6 = proposition4d_check()
    fiber_extracted_matrix, fiber_expected_matrix, fiber_max_error = fixed_strip_one_particle_fiber_check()
    full_off_block, full_scalar_block_deviation, full_one_particle_error = full_fixed_strip_block_check()
    two_particle_antisymmetry_error, two_particle_interaction_signal = two_particle_block_interaction_check()
    prop_h_extracted, prop_h_expected, prop_h_commutator, prop_h_a_left_4, prop_h_a_right_4 = proposition_h_check()

    print("Theorem 3 prototype check")
    print(f"  extracted c4 = {theorem3_extracted_c4:.12f}")
    print(f"  expected  c4 = {theorem3_expected_c4:.12f}")
    print(f"  rel. error   = {relative_error(theorem3_extracted_c4, theorem3_expected_c4):.3e}")
    print(f"  extracted c6 = {theorem3_extracted_c6:.12f}")
    print(f"  expected  c6 = {theorem3_expected_c6:.12f}")
    print(f"  rel. error   = {relative_error(theorem3_extracted_c6, theorem3_expected_c6):.3e}")
    print()

    print("Proposition 4C shell checks")
    for label, (extracted_value, expected_value) in proposition4c_results.items():
        print(f"  {label}: extracted = {extracted_value:.12f}, expected = {expected_value:.12f}, rel. error = {relative_error(extracted_value, expected_value):.3e}")
    print()

    print("Proposition 4D broader prototype check")
    print(f"  extracted c6 = {proposition4d_extracted_c6:.12f}")
    print(f"  expected  c6 = {proposition4d_expected_c6:.12f}")
    print(f"  rel. error   = {relative_error(proposition4d_extracted_c6, proposition4d_expected_c6):.3e}")
    print()

    print("Fixed-strip one-particle fiber check")
    print("  extracted c6 matrix:")
    for row in fiber_extracted_matrix:
        print("   ", " ".join(f"{value.real: .12f}" for value in row))
    print("  expected c6 matrix:")
    for row in fiber_expected_matrix:
        print("   ", " ".join(f"{value.real: .12f}" for value in row))
    print(f"  max rel. error = {fiber_max_error:.3e}")
    print()

    print("Full fixed-strip block check")
    print(f"  max cross-sector entry     = {full_off_block:.3e}")
    print(f"  max vacuum/full deviation  = {full_scalar_block_deviation:.3e}")
    print(f"  max one-particle rel. error = {full_one_particle_error:.3e}")
    print()

    print("Two-particle block interaction check")
    print(f"  max antisymmetry error     = {two_particle_antisymmetry_error:.3e}")
    print(f"  max interacting-free diff  = {two_particle_interaction_signal:.3e}")
    print()

    print("Proposition H overlap prototype check (five-site one-particle)")
    print(f"  [A_n^[4], A_n+4^[4]][4][0] extracted = {prop_h_extracted:.12f}")
    print(f"  expected 3/16 t^8                   = {prop_h_expected:.12f}")
    print(f"  rel. error                          = {relative_error(prop_h_extracted, prop_h_expected):.3e}")
    print("  A_n^[4] (left, t^4 units):")
    for row in prop_h_a_left_4:
        print("   ", " ".join(f"{value.real: .9f}" for value in row))
    print("  A_n+4^[4] (right, t^4 units):")
    for row in prop_h_a_right_4:
        print("   ", " ".join(f"{value.real: .9f}" for value in row))
    print("  commutator [A_n^[4], A_n+4^[4]] (t^8 units):")
    for row in prop_h_commutator:
        print("   ", " ".join(f"{value.real: .9f}" for value in row))


if __name__ == "__main__":
    main()
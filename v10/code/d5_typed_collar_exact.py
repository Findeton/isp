#!/usr/bin/env python3
"""D5 exact receipt: supplied factor partitions and separator composition.

All decisive finite gates use integers and Fraction.  The executable builds a
finite binary factor-token arena, verifies exact separator contraction and
elimination-order invariance, tests factorization-relative sufficiency with retained
messages, and separates channel rank from raw participant count.  It uses only
the Python standard library and writes no files.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from math import gcd
from typing import Callable, Dict, FrozenSet, Iterable, Mapping, Sequence, Tuple


State = Tuple[int, ...]

CHECKS = 0
PASSED = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global CHECKS, PASSED
    CHECKS += 1
    if not condition:
        raise AssertionError(f"{label}: {detail}")
    PASSED += 1
    suffix = f" ({detail})" if detail else ""
    print(f"PASS {CHECKS:02d}: {label}{suffix}")


def all_states(variables: Sequence[str]) -> Tuple[State, ...]:
    return tuple(product((-1, 1), repeat=len(variables)))


def state_index(state: State) -> int:
    index = 0
    for value in state:
        index = 2 * index + int(value == 1)
    return index


@dataclass(frozen=True)
class Table:
    variables: Tuple[str, ...]
    values: Tuple[Fraction, ...]
    provenance: FrozenSet[str]
    kind: str = "message"

    def __post_init__(self) -> None:
        if len(set(self.variables)) != len(self.variables):
            raise ValueError("table variables must be unique")
        if len(self.values) != 1 << len(self.variables):
            raise ValueError("table size does not match variable count")
        if self.kind not in {"positive_factor", "support_factor", "message", "identity"}:
            raise ValueError(f"unknown table kind: {self.kind}")
        if any(value < 0 for value in self.values):
            raise ValueError("factor/message weights must be nonnegative")
        if self.kind in {"positive_factor", "support_factor"}:
            if not self.variables:
                raise ValueError("primitive factor scope must be nonempty")
            if len(self.provenance) != 1:
                raise ValueError("primitive factor requires one unique provenance ID")
            if self.kind == "positive_factor" and any(value <= 0 for value in self.values):
                raise ValueError("positive factors require strictly positive entries")
            if self.kind == "support_factor" and not any(value > 0 for value in self.values):
                raise ValueError("support factors require nonempty support")
        if self.kind == "identity" and (
            self.variables or self.provenance or self.values != (Fraction(1),)
        ):
            raise ValueError("identity is the provenance-free scalar one")

    def value(self, assignment: Mapping[str, int]) -> Fraction:
        return self.values[state_index(tuple(assignment[var] for var in self.variables))]

    def normalized(self) -> Tuple[Fraction, ...]:
        total = sum(self.values, Fraction(0))
        if total <= 0:
            raise ValueError("cannot normalize a nonpositive table")
        return tuple(value / total for value in self.values)


def make_table(
    variables: Sequence[str],
    function: Callable[[Mapping[str, int]], Fraction | int],
    provenance: str | Iterable[str],
    *,
    allow_zeros: bool = False,
) -> Table:
    variables = tuple(variables)
    provenances = frozenset((provenance,)) if isinstance(provenance, str) else frozenset(provenance)
    values = []
    for state in all_states(variables):
        assignment = dict(zip(variables, state))
        values.append(Fraction(function(assignment)))
    kind = "support_factor" if allow_zeros else "positive_factor"
    return Table(variables, tuple(values), provenances, kind)


def reorder(table: Table, variables: Sequence[str]) -> Table:
    variables = tuple(variables)
    if set(variables) != set(table.variables):
        raise ValueError("reorder must preserve the variable set")
    values = []
    for state in all_states(variables):
        values.append(table.value(dict(zip(variables, state))))
    return Table(variables, tuple(values), table.provenance, table.kind)


def multiply(left: Table, right: Table, *, reject_duplicate: bool = True) -> Table:
    overlap = left.provenance & right.provenance
    if reject_duplicate and overlap:
        raise ValueError(f"duplicate provenance: {sorted(overlap)}")
    variables = left.variables + tuple(var for var in right.variables if var not in left.variables)
    values = []
    for state in all_states(variables):
        assignment = dict(zip(variables, state))
        values.append(left.value(assignment) * right.value(assignment))
    return Table(variables, tuple(values), left.provenance | right.provenance, "message")


def multiply_all(tables: Sequence[Table]) -> Table:
    if not tables:
        return Table((), (Fraction(1),), frozenset(), "identity")
    result = tables[0]
    for table in tables[1:]:
        result = multiply(result, table)
    return result


def sum_out(table: Table, variable: str) -> Table:
    if variable not in table.variables:
        return table
    remaining = tuple(var for var in table.variables if var != variable)
    values = []
    for state in all_states(remaining):
        assignment = dict(zip(remaining, state))
        total = Fraction(0)
        for value in (-1, 1):
            assignment[variable] = value
            total += table.value(assignment)
        del assignment[variable]
        values.append(total)
    return Table(remaining, tuple(values), table.provenance, "message")


def eliminate_tables(tables: Sequence[Table], order: Sequence[str]) -> Table:
    current = list(tables)
    for variable in order:
        selected = [table for table in current if variable in table.variables]
        current = [table for table in current if variable not in table.variables]
        if selected:
            current.append(sum_out(multiply_all(selected), variable))
    return multiply_all(current)


def effective_message(
    tables: Sequence[Table], boundary: Sequence[str], order: Sequence[str] | None = None
) -> Table:
    boundary = tuple(boundary)
    variables = tuple(dict.fromkeys(var for table in tables for var in table.variables))
    interior = tuple(var for var in variables if var not in boundary)
    if order is None:
        order = interior
    if len(order) != len(interior) or len(set(order)) != len(order) or set(order) != set(interior):
        raise ValueError("elimination order must contain exactly the interior variables")
    message = eliminate_tables(tables, order)
    ordered = reorder(message, boundary)
    return Table(ordered.variables, ordered.values, ordered.provenance, "message")


def relabel(table: Table, mapping: Mapping[str, str]) -> Table:
    variables = tuple(mapping.get(var, var) for var in table.variables)
    return Table(variables, table.values, table.provenance, table.kind)


def semantic_values(table: Table, variables: Sequence[str]) -> Tuple[Fraction, ...]:
    return reorder(table, variables).values


def predict_candidate_state(
    message: Table, candidate_factors: Sequence[Table], new_var: str
) -> Tuple[Fraction, Fraction]:
    combined = multiply_all((message, *candidate_factors))
    for variable in tuple(var for var in combined.variables if var != new_var):
        combined = sum_out(combined, variable)
    combined = reorder(combined, (new_var,))
    normalized = combined.normalized()
    return normalized[0], normalized[1]


def matrix_rank(matrix: Sequence[Sequence[Fraction]]) -> int:
    rows = [list(map(Fraction, row)) for row in matrix]
    if not rows:
        return 0
    ncols = len(rows[0])
    rank = 0
    for column in range(ncols):
        pivot = next((row for row in range(rank, len(rows)) if rows[row][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][column]
        rows[rank] = [value / scale for value in rows[rank]]
        for row in range(len(rows)):
            if row == rank or not rows[row][column]:
                continue
            scale = rows[row][column]
            rows[row] = [a - scale * b for a, b in zip(rows[row], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def character(mask: int, state: State) -> int:
    value = 1
    for bit, coordinate in enumerate(state):
        if mask & (1 << bit):
            value *= coordinate
    return value


def covariance_matrix(
    n: int, masks: Sequence[int], probabilities: Mapping[State, Fraction]
) -> Tuple[Tuple[Fraction, ...], ...]:
    states = all_states(tuple(str(i) for i in range(n)))
    means = [
        sum((probabilities[state] * character(mask, state) for state in states), Fraction(0))
        for mask in masks
    ]
    rows = []
    for i, left in enumerate(masks):
        row = []
        for j, right in enumerate(masks):
            product_mean = sum(
                (
                    probabilities[state]
                    * character(left, state)
                    * character(right, state)
                    for state in states
                ),
                Fraction(0),
            )
            row.append(product_mean - means[i] * means[j])
        rows.append(tuple(row))
    return tuple(rows)


def uniform_probabilities(n: int) -> Dict[State, Fraction]:
    states = all_states(tuple(str(i) for i in range(n)))
    return {state: Fraction(1, 1 << n) for state in states}


def product_probabilities(n: int, plus_probability: Fraction) -> Dict[State, Fraction]:
    result = {}
    for state in all_states(tuple(str(i) for i in range(n))):
        probability = Fraction(1)
        for value in state:
            probability *= plus_probability if value == 1 else 1 - plus_probability
        result[state] = probability
    return result


def total_variation(
    left: Mapping[State, Fraction], right: Mapping[State, Fraction]
) -> Fraction:
    return sum((abs(left[state] - right[state]) for state in left), Fraction(0)) / 2


def chi_square(
    distribution: Mapping[State, Fraction], reference: Mapping[State, Fraction]
) -> Fraction:
    return sum(
        (
            (distribution[state] - reference[state]) ** 2 / reference[state]
            for state in distribution
        ),
        Fraction(0),
    )


def marginal(table: Table, keep: Sequence[str]) -> Table:
    keep = tuple(keep)
    result = table
    for variable in tuple(var for var in result.variables if var not in keep):
        result = sum_out(result, variable)
    return reorder(result, keep)


def normalized_product_of_one_site_marginals(table: Table) -> Tuple[Fraction, ...]:
    variables = table.variables
    normalized_marginals = {
        variable: marginal(table, (variable,)).normalized() for variable in variables
    }
    values = []
    for state in all_states(variables):
        value = Fraction(1)
        for variable, coordinate in zip(variables, state):
            value *= normalized_marginals[variable][int(coordinate == 1)]
        values.append(value)
    return tuple(values)


def proportional(left: Table, right: Table) -> bool:
    if set(left.variables) != set(right.variables):
        return False
    right = reorder(right, left.variables)
    ratio = None
    for left_value, right_value in zip(left.values, right.values):
        if left_value == 0 and right_value == 0:
            continue
        if left_value == 0 or right_value == 0:
            return False
        current = left_value / right_value
        if ratio is None:
            ratio = current
        elif current != ratio:
            return False
    return ratio is not None


def factor_components(tables: Sequence[Table], variables: Iterable[str]) -> Tuple[FrozenSet[str], ...]:
    if any(table.kind not in {"positive_factor", "support_factor"} for table in tables):
        raise ValueError("factor-hypergraph components use primitive factor tokens only")
    adjacency = {variable: set() for variable in variables}
    for table in tables:
        for left, right in combinations(table.variables, 2):
            adjacency.setdefault(left, set()).add(right)
            adjacency.setdefault(right, set()).add(left)
        for variable in table.variables:
            adjacency.setdefault(variable, set())
    unseen = set(adjacency)
    components = []
    while unseen:
        root = min(unseen)
        unseen.remove(root)
        component = {root}
        stack = [root]
        while stack:
            current = stack.pop()
            for neighbor in adjacency[current] & unseen:
                unseen.remove(neighbor)
                component.add(neighbor)
                stack.append(neighbor)
        components.append(frozenset(component))
    return tuple(sorted(components, key=lambda component: tuple(sorted(component))))


def has_primitive_factor_incidence(tables: Sequence[Table], left: str, right: str) -> bool:
    return any(
        table.kind in {"positive_factor", "support_factor"}
        and left in table.variables
        and right in table.variables
        for table in tables
    )


def essential_variables(table: Table) -> FrozenSet[str]:
    essential = set()
    for variable in table.variables:
        other = tuple(item for item in table.variables if item != variable)
        for state in all_states(other):
            assignment = dict(zip(other, state))
            assignment[variable] = -1
            minus = table.value(assignment)
            assignment[variable] = 1
            plus = table.value(assignment)
            if minus != plus:
                essential.add(variable)
                break
    return frozenset(essential)


def irreducible_pair_interaction(table: Table) -> bool:
    if len(table.variables) != 2:
        raise ValueError("pair interaction test requires two variables")
    a, b, c, d = table.values
    return a * d != b * c


def bernoulli_table(width: int, plus_probability: Fraction, provenance: str) -> Table:
    variables = tuple(f"b{i}" for i in range(width))
    values = []
    for state in all_states(variables):
        probability = Fraction(1)
        for coordinate in state:
            probability *= plus_probability if coordinate == 1 else 1 - plus_probability
        values.append(probability)
    return Table(variables, tuple(values), frozenset((provenance,)), "message")


def edge_factor(left: str, right: str, equal: int, different: int, provenance: str) -> Table:
    return make_table(
        (left, right),
        lambda assignment: equal if assignment[left] == assignment[right] else different,
        provenance,
        allow_zeros=(equal == 0 or different == 0),
    )


def main() -> None:
    print("D5 :: exact supplied factor-partition and separator-state receipt")
    print("ARITHMETIC: integers and Fraction only for every verdict gate")

    # R1: complete parity ledgers.
    parity_ranks = []
    for n in range(1, 4):
        masks = tuple(range(1, 1 << n))
        covariance = covariance_matrix(n, masks, uniform_probabilities(n))
        parity_ranks.append(matrix_rank(covariance))
    check(
        "R1 complete parity ledgers have exact ranks 1/3/7",
        parity_ranks == [1, 3, 7],
        f"ranks={parity_ranks}",
    )

    duplicate_covariance = covariance_matrix(2, (1, 2, 1), uniform_probabilities(2))
    original_pair_rank = matrix_rank(
        covariance_matrix(2, (1, 2), uniform_probabilities(2))
    )
    swapped_pair_rank = matrix_rank(
        covariance_matrix(2, (2, 1), uniform_probabilities(2))
    )
    single_rank = matrix_rank(covariance_matrix(2, (1,), uniform_probabilities(2)))
    check(
        "R2 screen-relative rank separates duplication, joint relabeling, and adding a translated channel",
        matrix_rank(duplicate_covariance) == 2
        and original_pair_rank == swapped_pair_rank == 2
        and single_rank == 1
        and original_pair_rank > single_rank,
        "duplicate is dependent; whole-model swap preserves rank; adding the swap image can raise rank",
    )

    parity_supports = []
    for n in range(1, 11):
        mask = (1 << n) - 1
        covariance = covariance_matrix(n, (mask,), uniform_probabilities(n))
        parity_supports.append((n, matrix_rank(covariance)))
    check(
        "R3 one collective parity channel has rank one at every audited arity",
        all(rank == 1 for _, rank in parity_supports),
        f"participant/rank endpoints={parity_supports[0]},{parity_supports[-1]}",
    )

    product_rank_trace = []
    for n in range(1, 7):
        covariance = covariance_matrix(
            n, tuple(1 << index for index in range(n)), product_probabilities(n, Fraction(3, 4))
        )
        product_rank_trace.append((matrix_rank(covariance), sum(covariance[i][i] for i in range(n))))
    check(
        "R4 independent channels have unbounded exact rank and extensive Fisher trace",
        product_rank_trace == [(n, Fraction(3 * n, 4)) for n in range(1, 7)],
        f"rank/trace through six channels={product_rank_trace[-1]}",
    )

    weak_m = (1, 2, 4, 8, 16, 32, 64, 128)
    uniform_binary = {(-1,): Fraction(1, 2), (1,): Fraction(1, 2)}
    weak_distributions = tuple(
        {
            (-1,): Fraction(m, 2 * m + 1),
            (1,): Fraction(m + 1, 2 * m + 1),
        }
        for m in weak_m
    )
    weak_tv = tuple(total_variation(distribution, uniform_binary) for distribution in weak_distributions)
    check(
        "R5 positive rational channels have no frozen positive evidence floor",
        all(left > right > 0 for left, right in zip(weak_tv, weak_tv[1:]))
        and weak_tv[-1] == Fraction(1, 514),
        "TV=1/[2(2m+1)] decreases to zero analytically; finite shadow ends at 1/514",
    )

    weak_deltas = tuple(Fraction(1, 2 ** (index + 3)) for index in range(16))
    geometric_distributions = tuple(
        {
            (-1,): Fraction(1, 2) - delta,
            (1,): Fraction(1, 2) + delta,
        }
        for delta in weak_deltas
    )
    geometric_chi = tuple(
        chi_square(distribution, uniform_binary) for distribution in geometric_distributions
    )
    kl_upper_partial = tuple(
        sum(geometric_chi[:width], Fraction(0))
        for width in range(1, len(weak_deltas) + 1)
    )
    check(
        "R6 arbitrarily many nonzero independent weak channels fit one finite KL upper budget",
        all(left < right for left, right in zip(kl_upper_partial, kl_upper_partial[1:]))
        and geometric_chi == tuple(4 * delta * delta for delta in weak_deltas)
        and kl_upper_partial[-1] < Fraction(1, 12),
        "KL<=chi-square=4 delta^2 per channel; the infinite geometric upper sum is 1/12",
    )

    # C1-C3: exact separator contraction.
    f_as = edge_factor("A", "S", 3, 1, "f_as")
    f_st = make_table(
        ("S", "T"),
        lambda a: {( -1, -1): 3, (-1, 1): 1, (1, -1): 2, (1, 1): 4}[(a["S"], a["T"])],
        "f_st",
    )
    f_tb = edge_factor("T", "B", 2, 1, "f_tb")
    chain_factors = (f_as, f_st, f_tb)
    direct_chain = effective_message(chain_factors, ("A", "B"), ("S", "T"))
    reverse_chain = effective_message(chain_factors, ("A", "B"), ("T", "S"))
    left_piece = effective_message((f_as, f_st), ("A", "T"), ("S",))
    composed_chain = effective_message((left_piece, f_tb), ("A", "B"), ("T",))
    right_piece = effective_message((f_st, f_tb), ("S", "B"), ("T",))
    right_composed_chain = effective_message((f_as, right_piece), ("A", "B"), ("S",))
    check(
        "C1 direct elimination equals both separator-contraction parenthesizations",
        direct_chain.values == composed_chain.values == right_composed_chain.values,
        f"boundary table={direct_chain.values}",
    )
    duplicate_order_refused = False
    try:
        effective_message(chain_factors, ("A", "B"), ("S", "T", "S"))
    except ValueError:
        duplicate_order_refused = True
    check(
        "C2 elimination schedule is invariant for one fixed identified factor multiset",
        direct_chain.values == reverse_chain.values and duplicate_order_refused,
        "S-then-T equals T-then-S; duplicate schedules are refused; no physical birth-order theorem is inferred",
    )

    branch_factors = (
        edge_factor("R", "H", 2, 1, "branch_rh"),
        edge_factor("R", "K", 3, 1, "branch_rk"),
        edge_factor("H", "A", 2, 1, "branch_ha"),
        edge_factor("H", "B", 3, 1, "branch_hb"),
        edge_factor("K", "C", 2, 1, "branch_kc"),
        edge_factor("K", "D", 3, 1, "branch_kd"),
    )
    branch_boundary = ("A", "B", "C", "D")
    branch_direct = effective_message(branch_factors, branch_boundary, ("H", "K", "R"))
    branch_left = effective_message(
        (branch_factors[0], branch_factors[2], branch_factors[3]),
        ("R", "A", "B"),
        ("H",),
    )
    branch_right = effective_message(
        (branch_factors[1], branch_factors[4], branch_factors[5]),
        ("R", "C", "D"),
        ("K",),
    )
    branch_nested = effective_message((branch_left, branch_right), branch_boundary, ("R",))
    check(
        "C3 branching-tree leaf messages equal direct elimination",
        branch_direct.values == branch_nested.values,
        f"boundary entries={len(branch_direct.values)}; endpoints={branch_direct.values[0]}/{branch_direct.values[-1]}",
    )

    mapping = {"A": "Q", "S": "R", "T": "U", "B": "V"}
    relabeled_factors = tuple(relabel(table, mapping) for table in chain_factors)
    relabeled_message = effective_message(relabeled_factors, ("Q", "V"), ("R", "U"))
    check(
        "C4 joint relabeling preserves the exact separator prediction",
        relabeled_message.values == direct_chain.values,
        "variable names are gauge when tables and scopes move jointly",
    )

    duplicate_refused = False
    try:
        multiply(f_as, relabel(f_as, {"A": "X", "S": "Y"}))
    except ValueError:
        duplicate_refused = True
    check(
        "C5 duplicate factor identity is refused",
        duplicate_refused,
        "the same supplied factor token cannot be counted on both sides of a gluing",
    )

    separator_factor = make_table(
        ("S1",), lambda a: 2 if a["S1"] == -1 else 3, "owned_separator"
    )
    own_left_edge = edge_factor("A1", "S1", 3, 1, "own_as")
    own_right_edge = edge_factor("S1", "B1", 2, 1, "own_sb")
    ownership_direct = effective_message(
        (own_left_edge, separator_factor, own_right_edge), ("A1", "B1"), ("S1",)
    )
    left_owned = effective_message((own_left_edge, separator_factor), ("A1", "S1"), ())
    left_assignment = effective_message((left_owned, own_right_edge), ("A1", "B1"), ("S1",))
    right_owned = effective_message((separator_factor, own_right_edge), ("S1", "B1"), ())
    right_assignment = effective_message((own_left_edge, right_owned), ("A1", "B1"), ("S1",))
    nested_reuse_refused = False
    try:
        multiply(left_owned, separator_factor)
    except ValueError:
        nested_reuse_refused = True
    check(
        "C6 supplied exactly-once separator ownership is assignment-independent",
        ownership_direct.values == left_assignment.values == right_assignment.values
        and nested_reuse_refused,
        "ownership may be assigned left or right once; nested provenance union refuses reuse",
    )

    loop_factors = (
        edge_factor("H", "A", 3, 1, "loop_ha"),
        edge_factor("H", "B", 3, 1, "loop_hb"),
        edge_factor("A", "B", 2, 1, "loop_ab"),
    )
    loop_message = effective_message(loop_factors, ("A", "B"), ("H",))
    loop_product = normalized_product_of_one_site_marginals(loop_message)
    check(
        "C7 a loopy factor separator requires joint state information",
        loop_message.normalized() != loop_product
        and loop_message.values == (Fraction(20), Fraction(6), Fraction(6), Fraction(20)),
        "joint table is correlated while both one-site marginals are uniform",
    )

    # S1-S4: exact sufficiency and its law-relative boundary.
    history_one = (
        make_table(("B",), lambda a: 2 if a["B"] == -1 else 4, "h1"),
    )
    history_two = (
        make_table(
            ("X", "B"),
            lambda a: {(-1, -1): 1, (-1, 1): 1, (1, -1): 1, (1, 1): 3}[(a["X"], a["B"])],
            "h2",
        ),
    )
    message_one = effective_message(history_one, ("B",), ())
    message_two = effective_message(history_two, ("B",), ("X",))
    birth_bz = (edge_factor("B", "Z", 3, 1, "birth_bz"),)
    prediction_one = predict_candidate_state(message_one, birth_bz, "Z")
    prediction_two = predict_candidate_state(message_two, birth_bz, "Z")
    check(
        "S1 distinct interiors with the same separator message are predictively equivalent",
        message_one.values == message_two.values and prediction_one == prediction_two,
        f"message={message_one.values}; prediction={prediction_one}",
    )

    reverse_history = (
        make_table(
            ("X", "B"),
            lambda a: {(-1, -1): 1, (-1, 1): 1, (1, -1): 3, (1, 1): 1}[(a["X"], a["B"])],
            "h3",
        ),
    )
    reverse_message = effective_message(reverse_history, ("B",), ("X",))
    reverse_prediction = predict_candidate_state(reverse_message, birth_bz, "Z")
    check(
        "S2 identical unmarked boundaries can require different marked predictions",
        message_two.variables == reverse_message.variables
        and message_two.values != reverse_message.values
        and prediction_two != reverse_prediction,
        f"predictions={prediction_two} versus {reverse_prediction}",
    )

    unmarked_prediction = predict_candidate_state(
        make_table(("B",), lambda _a: 1, "unmarked"), birth_bz, "Z"
    )
    check(
        "S3 retained accumulated messages can screen history without making the unmarked process Markov",
        unmarked_prediction == (Fraction(1, 2), Fraction(1, 2))
        and prediction_two == (Fraction(5, 12), Fraction(7, 12))
        and reverse_prediction == (Fraction(7, 12), Fraction(5, 12)),
        "same visible B is insufficient; the accumulated factor message is sufficient for the audited continuation",
    )

    check(
        "S4 the separator encoder composes supplied factor-law data but does not select it",
        history_two[0].variables == reverse_history[0].variables
        and history_two[0].values != reverse_history[0].values
        and prediction_two != reverse_prediction,
        "same scope/proposal, different supplied factor tables, different exact law",
    )

    scaled_message = make_table(
        ("B",), lambda a: 1 if a["B"] == -1 else 2, "scaled_message"
    )
    scaled_prediction = predict_candidate_state(scaled_message, birth_bz, "Z")
    check(
        "S5 the exact predictive message is a positive ray, not an absolute normalization",
        proportional(message_two, scaled_message)
        and scaled_prediction == prediction_two
        and not proportional(message_two, reverse_message),
        "proportional tables are predictively identical; a nonproportional table is distinguished",
    )

    # B1-B5: connected proposal-domain closure and the multileg-token boundary.
    base_factors = (
        edge_factor("A", "B", 2, 1, "base_ab"),
        edge_factor("C", "D", 2, 1, "base_cd"),
    )
    base_components = factor_components(base_factors, ("A", "B", "C", "D"))
    local_birth = (edge_factor("Z", "A", 2, 1, "birth_za"),)
    local_components = factor_components(base_factors + local_birth, ("A", "B", "C", "D", "Z"))
    check(
        "B1 a supplied one-component proposal extends without rewriting old factors",
        len(base_components) == 2
        and len(local_components) == 2
        and base_factors == (base_factors + local_birth)[: len(base_factors)],
        f"components before/after={len(base_components)}/{len(local_components)}",
    )

    joining_birth = (
        edge_factor("Z", "A", 2, 1, "join_za"),
        edge_factor("Z", "C", 2, 1, "join_zc"),
    )
    joined_components = factor_components(base_factors + joining_birth, ("A", "B", "C", "D", "Z"))
    check(
        "B2 joining old components requires an explicit multileg proposal token",
        len(joined_components) == 1
        and has_primitive_factor_incidence(joining_birth, "Z", "A")
        and has_primitive_factor_incidence(joining_birth, "Z", "C"),
        "the proposal, not sum-product composition, supplies both primitive factor legs",
    )

    old_variables = ("A", "B", "C", "D")
    spanning_refusals = 0
    local_acceptances = 0
    component_by_variable = {
        variable: index
        for index, component in enumerate(base_components)
        for variable in component
    }
    for width in range(1, len(old_variables) + 1):
        for parents in combinations(old_variables, width):
            if len({component_by_variable[parent] for parent in parents}) == 1:
                local_acceptances += 1
            else:
                spanning_refusals += 1
    connected_growth = [edge_factor("R0", "R1", 2, 1, "seed")]
    variables = {"R0", "R1"}
    for step in range(2, 8):
        new = f"R{step}"
        parent = f"R{step - 1}"
        connected_growth.append(edge_factor(new, parent, 2, 1, f"grow_{step}"))
        variables.add(new)
    check(
        "B3 a connected-component proposal domain is closed given a connected seed",
        spanning_refusals > 0
        and local_acceptances > 0
        and len(factor_components(tuple(connected_growth), variables)) == 1,
        f"one-component subsets={local_acceptances}; cross-component subsets={spanning_refusals}",
    )

    ancestry_factors = (
        edge_factor("H", "A", 3, 1, "anc_ha"),
        edge_factor("H", "B", 3, 1, "anc_hb"),
    )
    ancestry_message = effective_message(ancestry_factors, ("A", "B"), ("H",))
    check(
        "B4 shared ancestry may correlate records without primitive A-B factor incidence",
        ancestry_message.normalized() != normalized_product_of_one_site_marginals(ancestry_message)
        and not has_primitive_factor_incidence(ancestry_factors, "A", "B"),
        "correlation through H is not primitive A-B factor-hyperedge incidence",
    )

    dummy_leg = make_table(
        ("A2", "B2"), lambda a: 1 if a["A2"] == -1 else 2, "dummy_leg"
    )
    separable_pair = make_table(
        ("A2", "B2"),
        lambda a: (1 if a["A2"] == -1 else 2) * (1 if a["B2"] == -1 else 3),
        "separable_pair",
    )
    irreducible_pair = edge_factor("A2", "B2", 2, 1, "irreducible_pair")
    check(
        "B5 listed scope, essential dependence, irreducible interaction, and derived message are distinct",
        essential_variables(dummy_leg) == frozenset(("A2",))
        and essential_variables(separable_pair) == frozenset(("A2", "B2"))
        and not irreducible_pair_interaction(separable_pair)
        and irreducible_pair_interaction(irreducible_pair)
        and ancestry_message.kind == "message"
        and all(table.kind == "positive_factor" for table in ancestry_factors),
        "dummy leg / separable pair / irreducible pair / derived correlation are separately typed",
    )

    # K1-K4: separator width, numeric growth, and projective nonselection.
    separator_sizes = tuple((width, 1 << width, (1 << width) - 1) for width in range(1, 9))
    check(
        "K1 arbitrary binary separator tables grow as 2^b entries",
        separator_sizes[-1] == (8, 256, 255),
        "width eight requires 256 weights / 255 normalized degrees",
    )

    transition = lambda left, right, provenance: make_table(
        (left, right),
        lambda a: {
            (-1, -1): 1,
            (-1, 1): 1,
            (1, -1): 1,
            (1, 1): 2,
        }[(a[left], a[right])],
        provenance,
    )
    chain_message = make_table(("X0",), lambda _a: 1, "chain_seed")
    chain_predictions = []
    primitive_ray_bits = []
    normalized_fraction_bits = []
    primitive_rays = []
    recurrence_ok = True
    previous_ray = (1, 1)
    for step in range(1, 33):
        edge = transition(f"X{step - 1}", f"X{step}", f"chain_{step}")
        chain_message = sum_out(multiply(chain_message, edge), f"X{step - 1}")
        chain_message = reorder(chain_message, (f"X{step}",))
        chain_predictions.append(chain_message.normalized())
        integers = tuple(int(value) for value in chain_message.values)
        divisor = gcd(integers[0], integers[1])
        primitive = tuple(value // divisor for value in integers)
        primitive_rays.append(primitive)
        primitive_ray_bits.append(max(value.bit_length() for value in primitive))
        normalized_fraction_bits.append(
            max(
                max(value.numerator.bit_length(), value.denominator.bit_length())
                for value in chain_message.normalized()
            )
        )
        expected = (
            previous_ray[0] + previous_ray[1],
            previous_ray[0] + 2 * previous_ray[1],
        )
        recurrence_ok = recurrence_ok and integers == expected and divisor == 1
        previous_ray = integers
    check(
        "K2 bounded-width chain messages compose with a fixed two-entry separator",
        all(len(prediction) == 2 for prediction in chain_predictions)
        and len(set(chain_predictions)) == 32
        and len(set(primitive_rays)) == 32,
        "separator width stays one through 32 distinct exact messages",
    )
    check(
        "K3 the canonical primitive ray has unbounded exact rational description in the audited recurrence",
        recurrence_ok
        and all(left < right for left, right in zip(primitive_ray_bits, primitive_ray_bits[1:]))
        and all(left < right for left, right in zip(normalized_fraction_bits, normalized_fraction_bits[1:])),
        f"primitive bits {primitive_ray_bits[0]}->{primitive_ray_bits[-1]}; normalized bits {normalized_fraction_bits[0]}->{normalized_fraction_bits[-1]}",
    )

    tower_ok = True
    for p in (Fraction(2, 3), Fraction(3, 4)):
        family = {width: bernoulli_table(width, p, f"tower_{p}_{width}") for width in range(1, 9)}
        for width in range(2, 9):
            pushed = sum_out(family[width], f"b{width - 1}")
            if pushed.values != family[width - 1].values:
                tower_ok = False
    tower_two = bernoulli_table(1, Fraction(2, 3), "tower_a").values
    tower_three = bernoulli_table(1, Fraction(3, 4), "tower_b").values
    check(
        "K4 compatible finite/projective message towers host but do not select a law",
        tower_ok and tower_two != tower_three,
        "p=2/3 and p=3/4 are distinct exact compatible towers",
    )

    zero_chain = (
        edge_factor("A0", "S0", 1, 0, "zero_as"),
        edge_factor("S0", "B0", 1, 0, "zero_sb"),
    )
    zero_direct = effective_message(zero_chain, ("A0", "B0"), ("S0",))
    zero_refusal = False
    try:
        Table(("Q0",), (Fraction(0), Fraction(0)), frozenset(("impossible",))).normalized()
    except ValueError:
        zero_refusal = True
    check(
        "Z1 one typed nonnegative support control composes when total support is nonempty",
        zero_direct.values == (Fraction(1), Fraction(0), Fraction(0), Fraction(1))
        and all(table.kind == "support_factor" for table in zero_chain)
        and zero_direct.normalized() == (Fraction(1, 2), Fraction(0), Fraction(0), Fraction(1, 2)),
        "deterministic equality separator has two zero boundary fibers; no general zero theorem is inferred",
    )
    check(
        "Z2 an impossible all-zero message is refused rather than normalized",
        zero_refusal,
        "support-sensitive extension is a refusal outside the positive base arena",
    )

    negative_refused = False
    try:
        Table(("N0",), (Fraction(-1), Fraction(2)), frozenset(), "message")
    except ValueError:
        negative_refused = True
    check(
        "Z3 negative factor/message weights are rejected by the table type",
        negative_refused,
        "signed normalization cannot enter the probability arena",
    )

    equality_support = edge_factor("A3", "B3", 1, 0, "support_equal")
    inequality_support = edge_factor("A3", "B3", 0, 1, "support_unequal")
    incompatible_message = multiply(equality_support, inequality_support)
    incompatible_refused = False
    try:
        incompatible_message.normalized()
    except ValueError:
        incompatible_refused = True
    check(
        "Z4 incompatible nonnegative supports produce an explicit impossible message",
        incompatible_message.values == (Fraction(0),) * 4 and incompatible_refused,
        "support factors are typed controls; fiberwise support calculus remains open",
    )

    # Conditional candidate-state normalization and factor-value nonselection.
    candidate_factors_a = (edge_factor("B", "Z", 4, 1, "candidate_a"),)
    candidate_factors_b = (edge_factor("B", "Z", 2, 1, "candidate_b"),)
    candidate_prediction_a = predict_candidate_state(message_two, candidate_factors_a, "Z")
    candidate_prediction_b = predict_candidate_state(message_two, candidate_factors_b, "Z")
    check(
        "L1 supplied positive proposal factors give normalized conditional candidate-state weights",
        sum(candidate_prediction_a, Fraction(0)) == 1
        and all(value > 0 for value in candidate_prediction_a),
        f"prediction={candidate_prediction_a}",
    )
    check(
        "L2 separator composition does not select the numerical proposal factor",
        candidate_prediction_a != candidate_prediction_b,
        f"same scope gives {candidate_prediction_a} versus {candidate_prediction_b}",
    )

    single_a = frozenset(("Z", "A"))
    single_b = frozenset(("Z", "B"))
    joint_ab = frozenset(("Z", "A", "B"))
    scope_candidates = (single_a, single_b, joint_ab)
    swap = {"A": "B", "B": "A", "Z": "Z"}

    def swap_scope(scope: FrozenSet[str]) -> FrozenSet[str]:
        return frozenset(swap[variable] for variable in scope)

    invariant_scope_families = []
    for mask in range(1 << len(scope_candidates)):
        family = frozenset(
            scope for index, scope in enumerate(scope_candidates) if mask & (1 << index)
        )
        moved = frozenset(swap_scope(scope) for scope in family)
        if family == moved:
            invariant_scope_families.append(family)
    check(
        "L3 the frozen symmetric arena has multiple nonempty swap-invariant eligibility families",
        len(invariant_scope_families) == 4
        and sum(bool(family) for family in invariant_scope_families) == 3
        and frozenset((single_a,)) not in invariant_scope_families,
        "single-A choice fails swap covariance; pair-family, joint-family, and all-family survive",
    )

    payload = "|".join(
        (
            str(parity_ranks),
            str(product_rank_trace),
            str(direct_chain.values),
            str(loop_message.values),
            str(prediction_two),
            str(reverse_prediction),
            str(separator_sizes),
            str(primitive_ray_bits),
            str(normalized_fraction_bits),
            str(weak_tv),
            str(kl_upper_partial[-1]),
            str(zero_direct.values),
            str(len(invariant_scope_families)),
        )
    )
    digest = sha256(payload.encode("utf-8")).hexdigest()
    print(f"CANONICAL PAYLOAD SHA256: {digest}")
    print(f"RECEIPT: {PASSED}/{CHECKS} exact checks passed")
    print(
        "VERDICT: CONDITIONAL-FACTOR-PARTITION-COMPOSITION + EXACT-SEPARATOR-STATE-GROWTH "
        "+ CONNECTED-DOMAIN-CLOSURE-GIVEN-SEED + BOUNDED-KL-NO-RANK/ARITY-BOUND "
        "+ SCOPE/VALUE-NONSELECTION"
    )
    print(
        "BOUNDARY: the complete factor cover, unique-ID ownership, scopes/values, proposal measure, "
        "seal/no-birth rule, and first cross-component token remain additional law data"
    )


if __name__ == "__main__":
    main()

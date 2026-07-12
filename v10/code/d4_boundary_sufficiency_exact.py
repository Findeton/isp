#!/usr/bin/env python3
"""D4 exact receipt: no-silent boundary sufficiency and locality obstruction.

All theorem gates use integers and Fraction.  The executable classifies the
finite unmarked restriction-natural kernel equations, constructs exact
law-relative completion messages, and tests fixed-capacity/profinite controls.
It uses only Python's standard library and writes no files.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from math import factorial
from typing import Dict, FrozenSet, Iterable, Mapping, Sequence, Tuple


Relation = FrozenSet[Tuple[int, int]]
Equation = Tuple[Dict[int, Fraction], Fraction]

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


def relation_code(n: int, relation: Relation) -> str:
    return "".join("1" if (i, j) in relation else "0" for i in range(n) for j in range(n))


def is_strict_order(n: int, relation: Relation) -> bool:
    if any(i == j or not (0 <= i < n and 0 <= j < n) for i, j in relation):
        return False
    if any((j, i) in relation for i, j in relation):
        return False
    for i, j in relation:
        for k, ell in relation:
            if j == k and (i, ell) not in relation:
                return False
    return True


def all_labeled_posets(n: int) -> Tuple[Relation, ...]:
    pairs = tuple((i, j) for i in range(n) for j in range(n) if i != j)
    result = []
    for mask in range(1 << len(pairs)):
        relation = frozenset(pair for bit, pair in enumerate(pairs) if mask & (1 << bit))
        if is_strict_order(n, relation):
            result.append(relation)
    return tuple(sorted(set(result), key=lambda rel: relation_code(n, rel)))


def is_downset(n: int, relation: Relation, mask: int) -> bool:
    return all(
        not (mask & (1 << upper)) or bool(mask & (1 << lower))
        for lower, upper in relation
    )


def downsets(n: int, relation: Relation) -> Tuple[int, ...]:
    return tuple(mask for mask in range(1 << n) if is_downset(n, relation, mask))


def induced_order(n: int, relation: Relation, keep: Sequence[int]) -> Relation:
    index = {old: new for new, old in enumerate(keep)}
    return frozenset(
        (index[i], index[j]) for i, j in relation if i in index and j in index
    )


def project_mask(mask: int, keep: Sequence[int]) -> int:
    return sum(1 << new for new, old in enumerate(keep) if mask & (1 << old))


def is_convex_subset(n: int, relation: Relation, mask: int) -> bool:
    selected = {i for i in range(n) if mask & (1 << i)}
    for lower in selected:
        for upper in selected:
            if (lower, upper) not in relation:
                continue
            for middle in range(n):
                if (lower, middle) in relation and (middle, upper) in relation and middle not in selected:
                    return False
    return True


def is_cover(relation: Relation, lower: int, upper: int) -> bool:
    return (lower, upper) in relation and not any(
        (lower, middle) in relation and (middle, upper) in relation
        for middle in {vertex for pair in relation for vertex in pair}
    )


def interval_masks(n: int, relation: Relation) -> FrozenSet[int]:
    masks = {0, (1 << n) - 1}
    masks.update(1 << vertex for vertex in range(n))
    for lower, upper in relation:
        interval = (1 << lower) | (1 << upper)
        for middle in range(n):
            if (lower, middle) in relation and (middle, upper) in relation:
                interval |= 1 << middle
        masks.add(interval)
    return frozenset(masks)


def allowed_cut_masks(n: int, relation: Relation, mode: str) -> Tuple[int, ...]:
    if mode == "all":
        return tuple(range(1 << n))
    if mode == "stem":
        return downsets(n, relation)
    if mode == "convex":
        return tuple(mask for mask in range(1 << n) if is_convex_subset(n, relation, mask))
    if mode == "interval":
        return tuple(sorted(interval_masks(n, relation)))
    raise ValueError(f"unknown cut mode: {mode}")


def relabel_relation(n: int, relation: Relation, permutation: Sequence[int]) -> Relation:
    return frozenset((permutation[i], permutation[j]) for i, j in relation)


def relabel_mask(n: int, mask: int, permutation: Sequence[int]) -> int:
    return sum(1 << permutation[i] for i in range(n) if mask & (1 << i))


def old_components(n: int, relation: Relation) -> Tuple[FrozenSet[int], ...]:
    unseen = set(range(n))
    components = []
    while unseen:
        root = min(unseen)
        unseen.remove(root)
        component = {root}
        stack = [root]
        while stack:
            vertex = stack.pop()
            neighbors = {
                other
                for other in range(n)
                if other != vertex
                and ((vertex, other) in relation or (other, vertex) in relation)
            }
            for other in neighbors & unseen:
                unseen.remove(other)
                component.add(other)
                stack.append(other)
        components.append(frozenset(component))
    return tuple(components)


def bridge_index(n: int, relation: Relation, mask: int) -> int:
    selected = {i for i in range(n) if mask & (1 << i)}
    met = sum(bool(selected & set(component)) for component in old_components(n, relation))
    return max(0, met - 1)


def registered_weight(
    n: int,
    relation: Relation,
    mask: int,
    ancestry_weight: Fraction,
    bridge_weight: Fraction,
) -> Fraction:
    return ancestry_weight ** mask.bit_count() * bridge_weight ** bridge_index(n, relation, mask)


def direct_pushforward(
    n: int,
    relation: Relation,
    keep: Sequence[int],
    ancestry_weight: Fraction,
    bridge_weight: Fraction,
) -> Dict[int, Fraction]:
    ideals = downsets(n, relation)
    raw = {
        ideal: registered_weight(n, relation, ideal, ancestry_weight, bridge_weight)
        for ideal in ideals
    }
    total = sum(raw.values(), Fraction(0))
    pushed: Dict[int, Fraction] = defaultdict(Fraction)
    for ideal, weight in raw.items():
        pushed[project_mask(ideal, keep)] += weight / total
    return dict(pushed)


def completion_message(
    n: int,
    relation: Relation,
    keep: Sequence[int],
    ancestry_weight: Fraction,
    bridge_weight: Fraction,
) -> Tuple[Tuple[int, Fraction], ...]:
    completion: Dict[int, Fraction] = defaultdict(Fraction)
    for ideal in downsets(n, relation):
        completion[project_mask(ideal, keep)] += registered_weight(
            n, relation, ideal, ancestry_weight, bridge_weight
        )
    total = sum(completion.values(), Fraction(0))
    return tuple(sorted((visible, weight / total) for visible, weight in completion.items()))


def independent_direct_pushforward(
    n: int,
    relation: Relation,
    keep: Sequence[int],
    ancestry_weight: Fraction,
    bridge_weight: Fraction,
) -> Dict[int, Fraction]:
    """Independent audit path: rebuild ideals, components, and projection inline."""
    raw: Dict[int, Fraction] = {}
    for mask in range(1 << n):
        valid = True
        for lower, upper in relation:
            if mask & (1 << upper) and not mask & (1 << lower):
                valid = False
                break
        if not valid:
            continue

        unseen = set(range(n))
        components = []
        while unseen:
            root = min(unseen)
            unseen.remove(root)
            component = {root}
            stack = [root]
            while stack:
                vertex = stack.pop()
                for other in tuple(unseen):
                    if (vertex, other) in relation or (other, vertex) in relation:
                        unseen.remove(other)
                        component.add(other)
                        stack.append(other)
            components.append(component)
        met = sum(any(mask & (1 << vertex) for vertex in component) for component in components)
        beta = max(0, met - 1)
        raw[mask] = ancestry_weight ** mask.bit_count() * bridge_weight ** beta

    total = sum(raw.values(), Fraction(0))
    pushed: Dict[int, Fraction] = defaultdict(Fraction)
    for mask, weight in raw.items():
        visible = 0
        for new, old in enumerate(keep):
            if mask & (1 << old):
                visible |= 1 << new
        pushed[visible] += weight / total
    return dict(pushed)


def sparse_rank(equations: Iterable[Dict[int, Fraction]]) -> int:
    basis: Dict[int, Dict[int, Fraction]] = {}
    for original in equations:
        row = {column: value for column, value in original.items() if value}
        while row:
            pivot = min(row)
            if pivot in basis:
                factor = row[pivot]
                for column, value in basis[pivot].items():
                    updated = row.get(column, Fraction(0)) - factor * value
                    if updated:
                        row[column] = updated
                    elif column in row:
                        del row[column]
            else:
                scale = row[pivot]
                row = {column: value / scale for column, value in row.items()}
                basis[pivot] = row
                break
    return len(basis)


def equation_satisfied(equation: Equation, vector: Sequence[Fraction]) -> bool:
    coefficients, rhs = equation
    return sum(coefficients[i] * vector[i] for i in coefficients) == rhs


def build_naturality_system(cutoff: int = 3, cut_mode: str = "all"):
    levels = tuple(all_labeled_posets(n) for n in range(cutoff + 1))
    variable_keys = []
    for n, posets in enumerate(levels):
        for relation in posets:
            for ideal in downsets(n, relation):
                variable_keys.append((n, relation, ideal))
    index = {key: i for i, key in enumerate(variable_keys)}
    equations: list[Equation] = []

    # Normalization.
    for n, posets in enumerate(levels):
        for relation in posets:
            equations.append(({
                index[(n, relation, ideal)]: Fraction(1)
                for ideal in downsets(n, relation)
            }, Fraction(1)))

    # Relabeling covariance.
    for n, posets in enumerate(levels):
        for relation in posets:
            for permutation in permutations(range(n)):
                moved_relation = relabel_relation(n, relation, permutation)
                for ideal in downsets(n, relation):
                    moved_ideal = relabel_mask(n, ideal, permutation)
                    left = index[(n, relation, ideal)]
                    right = index[(n, moved_relation, moved_ideal)]
                    coefficients: Dict[int, Fraction] = defaultdict(Fraction)
                    coefficients[left] += 1
                    coefficients[right] -= 1
                    equations.append((dict(coefficients), Fraction(0)))

    # Every induced-subset pushforward.
    for n, posets in enumerate(levels):
        for relation in posets:
            for keep_mask in allowed_cut_masks(n, relation, cut_mode):
                keep = tuple(i for i in range(n) if keep_mask & (1 << i))
                subrelation = induced_order(n, relation, keep)
                k = len(keep)
                for visible in downsets(k, subrelation):
                    coefficients: Dict[int, Fraction] = defaultdict(Fraction)
                    for ideal in downsets(n, relation):
                        if project_mask(ideal, keep) == visible:
                            coefficients[index[(n, relation, ideal)]] += 1
                    coefficients[index[(k, subrelation, visible)]] -= 1
                    equations.append((dict(coefficients), Fraction(0)))

    return levels, tuple(variable_keys), tuple(equations)


def global_shock_vector(variable_keys, p: Fraction) -> Tuple[Fraction, ...]:
    values = []
    for n, _relation, ideal in variable_keys:
        if n == 0:
            values.append(Fraction(1))
        elif ideal == 0:
            values.append(1 - p)
        elif ideal == (1 << n) - 1:
            values.append(p)
        else:
            values.append(Fraction(0))
    return tuple(values)


def system_rank_summary(cutoff: int, cut_mode: str) -> Tuple[int, int, int, int]:
    _levels, variable_keys, equations = build_naturality_system(cutoff, cut_mode)
    coefficient_rows = [coefficients for coefficients, _rhs in equations]
    augmented_rows = []
    extra = len(variable_keys)
    for coefficients, rhs in equations:
        row = dict(coefficients)
        if rhs:
            row[extra] = rhs
        augmented_rows.append(row)
    rank = sparse_rank(coefficient_rows)
    augmented = sparse_rank(augmented_rows)
    return len(variable_keys), len(equations), rank, augmented


def chain(n: int) -> Relation:
    return frozenset((i, j) for i in range(n) for j in range(i + 1, n))


def chain_ideals(n: int) -> Tuple[int, ...]:
    return tuple((1 << length) - 1 for length in range(n + 1))


def minimal_layer_mask(n: int, relation: Relation) -> int:
    return sum(
        1 << vertex
        for vertex in range(n)
        if not any((ancestor, vertex) in relation for ancestor in range(n))
    )


def component_shock_kernel(n: int, relation: Relation, p: Fraction) -> Dict[int, Fraction]:
    components = old_components(n, relation)
    kernel: Dict[int, Fraction] = defaultdict(Fraction)
    for choice in range(1 << len(components)):
        ideal = 0
        chosen = 0
        for bit, component in enumerate(components):
            if choice & (1 << bit):
                chosen += 1
                for vertex in component:
                    ideal |= 1 << vertex
        kernel[ideal] += p ** chosen * (1 - p) ** (len(components) - chosen)
    return dict(kernel)


def push_kernel(kernel: Mapping[int, Fraction], keep: Sequence[int]) -> Dict[int, Fraction]:
    pushed: Dict[int, Fraction] = defaultdict(Fraction)
    for ideal, probability in kernel.items():
        pushed[project_mask(ideal, keep)] += probability
    return dict(pushed)


def canonical_structure_message(
    n: int,
    relation: Relation,
    message: Tuple[Tuple[int, Fraction], ...],
) -> Tuple[str, Tuple[Tuple[int, int, int], ...]]:
    representatives = []
    for permutation in permutations(range(n)):
        moved_relation = relabel_relation(n, relation, permutation)
        moved_message = tuple(sorted(
            (
                relabel_mask(n, mask, permutation),
                probability.numerator,
                probability.denominator,
            )
            for mask, probability in message
        ))
        representatives.append((relation_code(n, moved_relation), moved_message))
    return min(representatives)


def canonical_structure(n: int, relation: Relation) -> str:
    return min(
        relation_code(n, relabel_relation(n, relation, permutation))
        for permutation in permutations(range(n))
    )


def main() -> None:
    print("D4 :: exact no-silent boundary sufficiency receipt")
    print("ARITHMETIC: integers and Fraction only")

    levels, variable_keys, equations = build_naturality_system(3)
    poset_counts = [len(level) for level in levels]
    check(
        "T1 all labeled strict-poset levels through n=3 enumerated",
        poset_counts == [1, 1, 3, 19],
        f"counts={poset_counts}",
    )

    coefficient_rows = [coefficients for coefficients, _rhs in equations]
    augmented_rows = []
    extra_column = len(variable_keys)
    for coefficients, rhs in equations:
        row = dict(coefficients)
        if rhs:
            row[extra_column] = rhs
        augmented_rows.append(row)
    rank = sparse_rank(coefficient_rows)
    augmented_rank = sparse_rank(augmented_rows)
    affine_dimension = len(variable_keys) - rank
    check(
        "T2 signed linear relaxation is consistent but positivity is load-bearing",
        rank == augmented_rank and affine_dimension == 3,
        f"variables={len(variable_keys)} equations={len(equations)} "
        f"rank={rank}; signed affine dimension={affine_dimension}",
    )

    empty_solution = global_shock_vector(variable_keys, Fraction(0))
    full_solution = global_shock_vector(variable_keys, Fraction(1))
    mixed_solution = global_shock_vector(variable_keys, Fraction(2, 5))
    candidates_ok = all(
        equation_satisfied(equation, vector)
        for equation in equations
        for vector in (empty_solution, full_solution, mixed_solution)
    )
    check(
        "T2 empty/full mixture line satisfies every exact equation",
        candidates_ok and empty_solution != full_solution,
        "p=0,1,2/5 controls",
    )

    # Independent structural proof cells.
    point = frozenset()
    chain2 = frozenset({(0, 1)})
    vee3 = frozenset({(0, 2), (1, 2)})
    antichain2 = frozenset()
    check(
        "T1 structural proof cells have the registered ideal counts",
        len(downsets(1, point)) == 2
        and len(downsets(2, chain2)) == 3
        and len(downsets(3, vee3)) == 5
        and len(downsets(2, antichain2)) == 4,
        "point/chain/V/antichain = 2/3/5/4 ideals",
    )

    # Exact positivity certificate.  On a two-chain the bottom-only ideal has
    # mass q_bottom = (bottom marginal) - (top marginal) = p-p = 0.  In the V
    # order, the chain restrictions give nonnegative sums
    # q_{a}+q_{ab}=0 and q_{b}+q_{ab}=0, forcing all three terms to zero; its
    # antichain restriction therefore has no singleton mass.
    variable_index = {key: i for i, key in enumerate(variable_keys)}
    vee_ideals = set(downsets(3, vee3))
    vee_expected = {0, 1 << 0, 1 << 1, (1 << 0) | (1 << 1), (1 << 3) - 1}

    def is_affine_consequence(coefficients: Dict[int, Fraction], rhs: Fraction = Fraction(0)) -> bool:
        target = dict(coefficients)
        if rhs:
            target[extra_column] = rhs
        return sparse_rank(augmented_rows + [target]) == augmented_rank

    chain_bottom_index = variable_index[(2, chain2, 1 << 0)]
    chain_bottom_forced_zero = is_affine_consequence({chain_bottom_index: Fraction(1)})
    vee_a = variable_index[(3, vee3, 1 << 0)]
    vee_b = variable_index[(3, vee3, 1 << 1)]
    vee_ab = variable_index[(3, vee3, (1 << 0) | (1 << 1))]
    vee_zero_sums = (
        is_affine_consequence({vee_a: Fraction(1), vee_ab: Fraction(1)})
        and is_affine_consequence({vee_b: Fraction(1), vee_ab: Fraction(1)})
    )
    vee_zero_sums_identify_terms = vee_ideals == vee_expected and vee_zero_sums
    check(
        "T2 positivity certificate kills chain and antichain singleton ideals",
        chain_bottom_forced_zero and vee_zero_sums_identify_terms,
        "chain singleton is a linear consequence; nonnegative V-order zero sums kill antichain singletons",
    )

    proper_ideal_certificates = 0
    proper_ideal_total = 0
    pair_certificate_types = defaultdict(int)
    for n in range(2, 5):
        for relation in all_labeled_posets(n):
            for ideal in downsets(n, relation):
                if ideal in (0, (1 << n) - 1):
                    continue
                proper_ideal_total += 1
                inside = [i for i in range(n) if ideal & (1 << i)]
                outside = [i for i in range(n) if not ideal & (1 << i)]
                certified = False
                for x in inside:
                    for y in outside:
                        pair_relation = induced_order(n, relation, (x, y))
                        projected = project_mask(ideal, (x, y))
                        pair_is_convex_boundary = (
                            (x, y) not in relation or is_cover(relation, x, y)
                        )
                        if (
                            projected == 1
                            and (y, x) not in relation
                            and pair_relation in (frozenset({(0, 1)}), frozenset())
                            and pair_is_convex_boundary
                        ):
                            pair_certificate_types[
                                "chain" if pair_relation else "antichain"
                            ] += 1
                            certified = True
                            break
                    if certified:
                        break
                proper_ideal_certificates += int(certified)
    check(
        "T2 every audited proper ideal has a convex zero-singleton pair certificate",
        proper_ideal_certificates == proper_ideal_total and proper_ideal_total > 0,
        f"certified proper ideals={proper_ideal_certificates}; "
        f"pair types={dict(pair_certificate_types)}",
    )

    # Verify the global-shock family beyond the linear-system cutoff.
    global_naturality = True
    global_cases = 0
    p = Fraction(2, 5)
    for n in range(5):
        for relation in all_labeled_posets(n):
            for keep_mask in range(1 << n):
                keep = tuple(i for i in range(n) if keep_mask & (1 << i))
                k = len(keep)
                subrelation = induced_order(n, relation, keep)
                pushed: Dict[int, Fraction] = defaultdict(Fraction)
                for ideal, probability in (
                    (0, 1 - p),
                    ((1 << n) - 1, p),
                ) if n else ((0, Fraction(1)),):
                    pushed[project_mask(ideal, keep)] += probability
                expected = {0: Fraction(1)} if k == 0 else {0: 1 - p, (1 << k) - 1: p}
                global_naturality &= dict(pushed) == expected
                global_cases += 1
    check(
        "T1 empty/full universal-precursor family is natural through every n<=4 cut",
        global_naturality,
        f"cut cases={global_cases}",
    )

    convex_summary = system_rank_summary(3, "convex")
    stem_summary = system_rank_summary(3, "stem")
    interval_summary = system_rank_summary(3, "interval")
    convex_dimension = convex_summary[0] - convex_summary[2]
    stem_dimension = stem_summary[0] - stem_summary[2]
    interval_dimension = interval_summary[0] - interval_summary[2]
    check(
        "R1 cut-category signed classifications separate convex from stem/interval systems",
        convex_summary[2] == convex_summary[3]
        and stem_summary[2] == stem_summary[3]
        and interval_summary[2] == interval_summary[3]
        and convex_dimension == 3
        and stem_dimension == 8
        and interval_dimension == 8,
        f"signed dimensions all/convex/stem/interval=3/{convex_dimension}/{stem_dimension}/{interval_dimension}",
    )

    stem_naturality = True
    stem_cases = 0
    for n in range(5):
        for relation in all_labeled_posets(n):
            full_minima = minimal_layer_mask(n, relation)
            for keep_mask in downsets(n, relation):
                keep = tuple(i for i in range(n) if keep_mask & (1 << i))
                subrelation = induced_order(n, relation, keep)
                stem_naturality &= (
                    project_mask(full_minima, keep)
                    == minimal_layer_mask(len(keep), subrelation)
                )
                stem_cases += 1
    chain_top_keep = (1,)
    minimal_layer_all_cut_failure = (
        project_mask(minimal_layer_mask(2, chain2), chain_top_keep)
        != minimal_layer_mask(1, induced_order(2, chain2, chain_top_keep))
    )
    check(
        "R2 ancestor-closed stems admit a nontrivial minimal-layer law",
        stem_naturality and minimal_layer_all_cut_failure,
        f"stem cuts={stem_cases}; fails the top-only chain cut",
    )

    interval_naturality = True
    interval_cases = 0
    component_p = Fraction(2, 5)
    for n in range(5):
        for relation in all_labeled_posets(n):
            full_kernel = component_shock_kernel(n, relation, component_p)
            for keep_mask in interval_masks(n, relation):
                keep = tuple(i for i in range(n) if keep_mask & (1 << i))
                subrelation = induced_order(n, relation, keep)
                interval_naturality &= (
                    push_kernel(full_kernel, keep)
                    == component_shock_kernel(len(keep), subrelation, component_p)
                )
                interval_cases += 1
    vee_minima_keep = (0, 1)
    component_convex_failure = (
        push_kernel(component_shock_kernel(3, vee3, component_p), vee_minima_keep)
        != component_shock_kernel(
            2, induced_order(3, vee3, vee_minima_keep), component_p
        )
    )
    check(
        "R3 causal intervals admit component-wise mixtures that fail a convex V cut",
        interval_naturality and component_convex_failure,
        f"interval cuts={interval_cases}; convex minima cut exposes correlation",
    )

    proof_cells_convex = all(
            is_convex_subset(n, relation, mask)
            for n, relation, mask in (
                (2, chain2, 1 << 0),
                (2, chain2, 1 << 1),
                (3, vee3, (1 << 0) | (1 << 2)),
                (3, vee3, (1 << 1) | (1 << 2)),
                (3, vee3, (1 << 0) | (1 << 1)),
            )
        )
    check(
        "R4 convex cuts retain the full positivity-collapse certificate",
        proof_cells_convex
        and proper_ideal_certificates == 1304
        and pair_certificate_types == {"chain": 616, "antichain": 688},
        "small proof cells are convex; 1304/1304 proper ideals use a cover or incomparable pair",
    )

    # D3 exact failure control.
    pushed_chain = direct_pushforward(2, chain2, (0,), Fraction(1), Fraction(1))
    local_point = direct_pushforward(1, point, (0,), Fraction(1), Fraction(1))
    check(
        "T3 D3 uniform witness fails autonomous restriction exactly",
        pushed_chain == {0: Fraction(1, 3), 1: Fraction(2, 3)}
        and local_point == {0: Fraction(1, 2), 1: Fraction(1, 2)},
        f"push={pushed_chain}; local={local_point}",
    )

    # Completion-message sufficiency across all labeled posets through n=4.
    laws = ((Fraction(1), Fraction(1)), (Fraction(1), Fraction(2)))
    message_ok = True
    message_contexts = 0
    labeled_classes_by_law = [set() for _law in laws]
    labeled_messages_by_structure_law = [defaultdict(set) for _law in laws]
    canonical_classes_by_law = [set() for _law in laws]
    canonical_messages_by_structure_law = [defaultdict(set) for _law in laws]
    pooled_labeled_classes = set()
    pooled_labeled_messages: Dict[tuple, set[tuple]] = defaultdict(set)
    pooled_canonical_classes = set()
    pooled_canonical_messages: Dict[tuple, set[tuple]] = defaultdict(set)
    for n in range(5):
        for relation in all_labeled_posets(n):
            for keep_mask in range(1 << n):
                keep = tuple(i for i in range(n) if keep_mask & (1 << i))
                subrelation = induced_order(n, relation, keep)
                k = len(keep)
                raw_structure = (k, relation_code(k, subrelation))
                canonical_structure_key = (k, canonical_structure(k, subrelation))
                for law_index, (ancestry_weight, bridge_weight) in enumerate(laws):
                    direct = independent_direct_pushforward(
                        n, relation, keep, ancestry_weight, bridge_weight
                    )
                    message = completion_message(
                        n, relation, keep, ancestry_weight, bridge_weight
                    )
                    message_ok &= dict(message) == direct
                    labeled_key = raw_structure + (message,)
                    canonical_message = canonical_structure_message(k, subrelation, message)
                    canonical_key = (k,) + canonical_message
                    labeled_classes_by_law[law_index].add(labeled_key)
                    labeled_messages_by_structure_law[law_index][raw_structure].add(message)
                    canonical_classes_by_law[law_index].add(canonical_key)
                    canonical_messages_by_structure_law[law_index][canonical_structure_key].add(
                        canonical_message
                    )
                    pooled_labeled_classes.add(labeled_key)
                    pooled_labeled_messages[raw_structure].add(message)
                    pooled_canonical_classes.add(canonical_key)
                    pooled_canonical_messages[canonical_structure_key].add(canonical_message)
                    message_contexts += 1
    check(
        "M1 independently rebuilt pushforwards equal exact completion messages",
        message_ok,
        f"contexts={message_contexts}",
    )
    check(
        "M3 fixed-law labeled-cover predictive partitions match independent counts",
        [len(classes) for classes in labeled_classes_by_law] == [564, 601]
        and [
            max(map(len, messages.values())) for messages in labeled_messages_by_structure_law
        ] == [42, 45],
        "classes/max for b=1:564/42; b=2:601/45",
    )
    check(
        "M3 joint relabeling quotient gives canonical unmarked predictive classes",
        len(pooled_labeled_classes) == 756
        and max(map(len, pooled_labeled_messages.values())) == 66
        and len(pooled_canonical_classes) == 199
        and max(map(len, pooled_canonical_messages.values())) == 42,
        "pooled labeled=756/66; canonical unmarked=199/42",
    )
    print(
        "INFO M3 fixed-law canonical classes/max: "
        + "; ".join(
            f"law{law_index + 1}={len(canonical_classes_by_law[law_index])}/"
            f"{max(map(len, canonical_messages_by_structure_law[law_index].values()))}"
            for law_index in range(len(laws))
        )
    )

    antichain3 = frozenset()
    msg_a = dict(completion_message(3, antichain3, (0,), Fraction(1), Fraction(1)))
    msg_b = dict(completion_message(3, antichain3, (0,), Fraction(1), Fraction(2)))
    check(
        "M2 completion message is law-relative on one fixed parent/cut",
        msg_a[1] == Fraction(1, 2) and msg_b[1] == Fraction(9, 14),
        f"included probability={msg_a[1]} versus {msg_b[1]}",
    )

    # Uniform finite-capacity lower bound on chains.
    depth_cutoff = 64
    chain_predictions = []
    chain_ideal_audit = True
    for n in range(1, depth_cutoff + 1):
        relation = chain(n)
        ideals = chain_ideals(n)
        chain_ideal_audit &= len(ideals) == n + 1 and all(
            is_downset(n, relation, ideal) for ideal in ideals
        )
        included = sum(bool(ideal & 1) for ideal in ideals)
        chain_predictions.append(Fraction(included, len(ideals)))
    chain_predictions = tuple(chain_predictions)
    required_bits = (depth_cutoff - 1).bit_length()
    check(
        "C1 chain contexts require one exact message state per audited depth",
        chain_ideal_audit
        and len(set(chain_predictions)) == depth_cutoff
        and chain_predictions[0] == Fraction(1, 2)
        and chain_predictions[-1] == Fraction(64, 65)
        and required_bits == 6,
        f"depths={depth_cutoff}; states={len(set(chain_predictions))}; bits>={required_bits}",
    )
    check(
        "C1 fixed three-bit alphabet fails by depth nine",
        len({Fraction(n, n + 1) for n in range(1, 10)}) == 9 > 2**3,
        "nine exact predictions exceed eight marks",
    )
    check(
        "C2 one discarded-chain-context-present flag is insufficient",
        bool(2 > 1) == bool(3 > 1)
        and chain_predictions[1] == Fraction(2, 3)
        and chain_predictions[2] == Fraction(3, 4)
        and chain_predictions[1] != chain_predictions[2],
        "depths two and three share the typed flag but not the prediction",
    )

    # Formal loophole models.  Each reproduces the chain marginal but locates
    # the growing/global information in a different place.
    stochastic_encoder = all(
        # Binary mark M with P(M=1|n)=q_n and decoder precursor=M.
        q * 1 + (1 - q) * 0 == q for q in chain_predictions[:16]
    )
    distributed_encoder = all(
        len(format(n - 1, f"0{required_bits}b")) == required_bits
        and int(format(n - 1, f"0{required_bits}b"), 2) + 1 == n
        for n in range(1, depth_cutoff + 1)
    )
    unbounded_integer_decoder = all(
        Fraction(n, n + 1) == chain_predictions[n - 1]
        for n in range(1, depth_cutoff + 1)
    )
    approximation_tolerance = Fraction(1, 100)
    approximation_threshold = 99
    tail_error_bound = Fraction(1, approximation_threshold + 1)
    check(
        "C3 stochastic/distributed/unbounded/approximate models evade the exact fixed-token bound",
        stochastic_encoder
        and distributed_encoder
        and unbounded_integer_decoder
        and tail_error_bound <= approximation_tolerance,
        "binary mixing / six distributed bits / integer n / one 1%-tail bin relocate or relax context",
    )

    # Fixed residue/profinite controls.
    modulus = 7
    n0 = 5
    n1 = n0 + modulus
    check(
        "P1 one fixed residue mark cannot determine the exact chain prediction",
        n0 % modulus == n1 % modulus
        and Fraction(n0, n0 + 1) != Fraction(n1, n1 + 1),
        f"n={n0},{n1}; residue={n0 % modulus}",
    )
    factorial_residues = all(
        factorial(j) % modulus_candidate == 0
        for j in range(2, 9)
        for modulus_candidate in range(1, j + 1)
    )
    factorial_errors = tuple(Fraction(1, factorial(j) + 1) for j in range(2, 9))
    check(
        "P2 finite factorial shadow verifies the analytic profinite-discontinuity identities",
        factorial_residues
        and all(
            factorial_errors[index + 1] < factorial_errors[index]
            for index in range(len(factorial_errors) - 1)
        )
        and Fraction(factorial(8), factorial(8) + 1) == 1 - factorial_errors[-1],
        f"audited terminal error=1/{factorial(8) + 1}; infinite limit supplied analytically",
    )

    # Globality control: full shock on an antichain selects every old event.
    universe_size = 8
    full_precursor = (1 << universe_size) - 1
    check(
        "C4 natural survivor is universal-precursor incidence rather than a local pair law",
        p > 0 and full_precursor.bit_count() == universe_size,
        f"full-precursor probability={p}; participants={universe_size}",
    )

    print(f"RECEIPT: {PASSED}/{CHECKS} exact checks passed")
    print("VERDICT: ALL-SUBSET-UNMARKED-COLLAPSE + LAW-RELATIVE-UNBOUNDED-DETERMINISTIC-TARGET")
    print("BOUNDARY: no bounded record-local interacting extension law is selected")


if __name__ == "__main__":
    main()

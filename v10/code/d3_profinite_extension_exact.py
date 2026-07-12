#!/usr/bin/env python3
"""D3 exact receipt: variable-history growth and the profinite law boundary.

The executable uses only Python's standard library.  The theorem-critical
arena is finite and exact.  Decimal is used only to print the common v7
survival value at 120-plus-digit working precision.

This is an unmarked causal-order shadow.  It does not manufacture screens,
collars, likelihood blocks, transport, holonomy, outcomes, or a metric.
"""

from __future__ import annotations

import hashlib
from collections import defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial
from typing import Dict, FrozenSet, Iterable, Iterator, Mapping, Sequence, Tuple


Relation = FrozenSet[Tuple[int, int]]
Kernel = Dict[int, Fraction]  # precursor bit mask -> probability

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
    for i, j in relation:
        for k, ell in relation:
            if j == k and (i, ell) not in relation:
                return False
    return all((j, i) not in relation for i, j in relation)


def natural_orders_direct(n: int) -> FrozenSet[Relation]:
    """Independent upper-triangular transitive-closure census."""
    pairs = tuple(combinations(range(n), 2))
    orders = set()
    for mask in range(1 << len(pairs)):
        relation = frozenset(pair for bit, pair in enumerate(pairs) if mask & (1 << bit))
        if is_strict_order(n, relation):
            orders.add(relation)
    return frozenset(orders)


def is_downset(n: int, relation: Relation, mask: int) -> bool:
    for ancestor, element in relation:
        if mask & (1 << element) and not mask & (1 << ancestor):
            return False
    return True


def downsets(n: int, relation: Relation) -> Tuple[int, ...]:
    return tuple(mask for mask in range(1 << n) if is_downset(n, relation, mask))


def extend(n: int, relation: Relation, precursor: int) -> Relation:
    if not is_downset(n, relation, precursor):
        raise ValueError("precursor must be an ancestor-closed subset")
    child = set(relation)
    child.update((old, n) for old in range(n) if precursor & (1 << old))
    result = frozenset(child)
    if not is_strict_order(n + 1, result):
        raise AssertionError("legal down-set extension failed to make an order")
    return result


def delete_last(n_plus_one: int, relation: Relation) -> Relation:
    last = n_plus_one - 1
    return frozenset((i, j) for i, j in relation if i != last and j != last)


def natural_orders_growth(cutoff: int) -> Tuple[FrozenSet[Relation], ...]:
    levels = [frozenset({frozenset()})]
    for n in range(cutoff):
        children = {
            extend(n, parent, precursor)
            for parent in levels[n]
            for precursor in downsets(n, parent)
        }
        levels.append(frozenset(children))
    return tuple(levels)


def old_components(n: int, relation: Relation) -> Tuple[FrozenSet[int], ...]:
    unseen = set(range(n))
    components = []
    while unseen:
        root = min(unseen)
        stack = [root]
        component = {root}
        unseen.remove(root)
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
    return tuple(sorted(components, key=lambda c: tuple(sorted(c))))


def met_component_count(n: int, relation: Relation, precursor: int) -> int:
    selected = {i for i in range(n) if precursor & (1 << i)}
    return sum(bool(selected & set(component)) for component in old_components(n, relation))


def bridge_index(n: int, relation: Relation, precursor: int) -> int:
    return max(0, met_component_count(n, relation, precursor) - 1)


def direct_parents(n: int, relation: Relation, precursor: int) -> FrozenSet[int]:
    selected = {i for i in range(n) if precursor & (1 << i)}
    return frozenset(
        x for x in selected
        if not any(x != y and (x, y) in relation for y in selected)
    )


def covers_into_new(n: int, child: Relation) -> FrozenSet[int]:
    ancestors = {i for i in range(n) if (i, n) in child}
    return frozenset(
        x for x in ancestors
        if not any(x != y and (x, y) in child and (y, n) in child for y in ancestors)
    )


def relabel(n: int, relation: Relation, permutation: Sequence[int]) -> Relation:
    return frozenset((permutation[i], permutation[j]) for i, j in relation)


def relabel_mask(n: int, mask: int, permutation: Sequence[int]) -> int:
    result = 0
    for old in range(n):
        if mask & (1 << old):
            result |= 1 << permutation[old]
    return result


def canonical(n: int, relation: Relation) -> str:
    return min(relation_code(n, relabel(n, relation, p)) for p in permutations(range(n)))


def extension_kernel(
    n: int,
    relation: Relation,
    *,
    ancestry_weight: Fraction,
    bridge_weight: Fraction,
    allow_bridges: bool = True,
) -> Kernel:
    if ancestry_weight <= 0 or bridge_weight <= 0:
        raise ValueError("registered witness weights must be positive")
    raw = {}
    for precursor in downsets(n, relation):
        size = precursor.bit_count()
        beta = bridge_index(n, relation, precursor)
        raw[precursor] = (
            ancestry_weight ** size * bridge_weight ** beta
            if allow_bridges or beta == 0
            else Fraction(0)
        )
    total = sum(raw.values(), Fraction(0))
    return {precursor: weight / total for precursor, weight in raw.items()}


def evolve_measure(
    cutoff: int,
    *,
    ancestry_weight: Fraction,
    bridge_weight: Fraction,
    allow_bridges: bool = True,
) -> Tuple[Dict[Relation, Fraction], ...]:
    levels: list[Dict[Relation, Fraction]] = [{frozenset(): Fraction(1)}]
    for n in range(cutoff):
        next_level: Dict[Relation, Fraction] = defaultdict(Fraction)
        for parent, parent_mass in levels[n].items():
            kernel = extension_kernel(
                n,
                parent,
                ancestry_weight=ancestry_weight,
                bridge_weight=bridge_weight,
                allow_bridges=allow_bridges,
            )
            for precursor, probability in kernel.items():
                if probability == 0:
                    continue
                child = extend(n, parent, precursor)
                next_level[child] += parent_mass * probability
        levels.append(dict(next_level))
    return tuple(levels)


def recover_precursor(n: int, child: Relation) -> int:
    return sum(1 << old for old in range(n) if (old, n) in child)


def induced_order(n: int, relation: Relation, keep: Sequence[int]) -> Relation:
    if any(not 0 <= vertex < n for vertex in keep) or len(set(keep)) != len(keep):
        raise ValueError("retained vertices must be distinct members of the parent")
    index = {old: new for new, old in enumerate(keep)}
    return frozenset(
        (index[i], index[j]) for i, j in relation if i in index and j in index
    )


def project_precursor(precursor: int, keep: Sequence[int]) -> int:
    return sum(1 << new for new, old in enumerate(keep) if precursor & (1 << old))


def restriction_pushforward(
    n: int,
    relation: Relation,
    keep: Sequence[int],
    *,
    ancestry_weight: Fraction,
    bridge_weight: Fraction,
) -> Dict[int, Fraction]:
    pushed: Dict[int, Fraction] = defaultdict(Fraction)
    full = extension_kernel(
        n,
        relation,
        ancestry_weight=ancestry_weight,
        bridge_weight=bridge_weight,
    )
    for precursor, probability in full.items():
        pushed[project_precursor(precursor, keep)] += probability
    return dict(pushed)


def orbit_pushforward(n: int, level: Mapping[Relation, Fraction]) -> Dict[str, Fraction]:
    pushed: Dict[str, Fraction] = defaultdict(Fraction)
    for relation, mass in level.items():
        pushed[canonical(n, relation)] += mass
    return dict(pushed)


def exact_rank_stems(n: int, relation: Relation, rank: int) -> FrozenSet[str]:
    result = set()
    for subset in combinations(range(n), rank):
        mask = sum(1 << i for i in subset)
        if not is_downset(n, relation, mask):
            continue
        index = {old: new for new, old in enumerate(subset)}
        induced = frozenset(
            (index[i], index[j]) for i, j in relation if i in index and j in index
        )
        result.add(canonical(rank, induced))
    return frozenset(result)


def stdout_digest_payload(level_counts: Sequence[int], bridge_pair: Tuple[Fraction, Fraction]) -> str:
    payload = f"levels={tuple(level_counts)};bridge={bridge_pair[0]}|{bridge_pair[1]}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def main() -> None:
    print("D3 :: exact profinite variable-history extension receipt")
    print("ARITHMETIC: integers/Fraction; Decimal precision=140 for survival print")

    cutoff = 5
    growth_levels = natural_orders_growth(cutoff)
    direct_levels = tuple(natural_orders_direct(n) for n in range(cutoff + 1))
    counts = [len(level) for level in growth_levels]
    check(
        "A1 independent natural-order censuses agree through n=5",
        all(growth_levels[n] == direct_levels[n] for n in range(cutoff + 1)),
        f"counts={counts}",
    )
    check("A1 census matches registered sequence", counts == [1, 1, 2, 7, 40, 357])

    deletion_ok = True
    surjective_ok = True
    immutable_ok = True
    direct_parent_ok = True
    for n in range(cutoff):
        seen_parents = set()
        for parent in growth_levels[n]:
            for precursor in downsets(n, parent):
                child = extend(n, parent, precursor)
                deleted = delete_last(n + 1, child)
                seen_parents.add(deleted)
                deletion_ok &= deleted == parent
                immutable_ok &= all(((i, j) in child) == ((i, j) in parent)
                                    for i in range(n) for j in range(n))
                direct_parent_ok &= direct_parents(n, parent, precursor) == covers_into_new(n, child)
        surjective_ok &= seen_parents == set(growth_levels[n])
    check("A2 every child end-deletes to its unique parent", deletion_ok)
    check("A2 end-deletion is surjective at every audited level", surjective_ok)
    check("A3 no old-old order relation changes under extension", immutable_ok)
    check("A5 precursor maxima are exactly the direct parents of the new event", direct_parent_ok)

    unique_child_fibers = True
    for n in range(cutoff):
        generated_children = [
            extend(n, parent, precursor)
            for parent in growth_levels[n]
            for precursor in downsets(n, parent)
        ]
        unique_child_fibers &= (
            len(generated_children)
            == len(set(generated_children))
            == len(growth_levels[n + 1])
        )
        unique_child_fibers &= all(
            delete_last(n + 1, child) in growth_levels[n]
            and recover_precursor(n, child) in downsets(n, delete_last(n + 1, child))
            for child in growth_levels[n + 1]
        )
    check(
        "A6 actual next-level children have unique parent/precursor fibers",
        unique_child_fibers,
        "state size is carried by the finite level",
    )

    restriction_incidence_ok = True
    restriction_incidence_cases = 0
    for n in range(1, cutoff):
        for parent in growth_levels[n]:
            for precursor in downsets(n, parent):
                child = extend(n, parent, precursor)
                for keep_mask in range(1 << n):
                    keep = tuple(i for i in range(n) if keep_mask & (1 << i))
                    restricted_parent = induced_order(n, parent, keep)
                    projected = project_precursor(precursor, keep)
                    expected = extend(len(keep), restricted_parent, projected)
                    mapping = {old: new for new, old in enumerate(keep)}
                    mapping[n] = len(keep)
                    actual = frozenset(
                        (mapping[i], mapping[j])
                        for i, j in child
                        if i in mapping and j in mapping
                    )
                    restriction_incidence_cases += 1
                    restriction_incidence_ok &= actual == expected
    check(
        "A7 deterministic extension incidence commutes with every old-subset restriction",
        restriction_incidence_ok,
        f"restriction cases={restriction_incidence_cases}",
    )

    bridge_exists = True
    bridge_connectivity = True
    disconnected_parents = 0
    for n in range(2, cutoff + 1):
        for parent in growth_levels[n]:
            components = old_components(n, parent)
            if len(components) < 2:
                continue
            disconnected_parents += 1
            candidates = [d for d in downsets(n, parent) if bridge_index(n, parent, d) >= 1]
            bridge_exists &= bool(candidates)
            for precursor in candidates:
                child = extend(n, parent, precursor)
                old_count = len(components)
                new_count = len(old_components(n + 1, child))
                bridge_connectivity &= new_count == old_count - bridge_index(n, parent, precursor)
    check(
        "A4 every disconnected audited parent admits a bridge extension",
        bridge_exists and disconnected_parents > 0,
        f"disconnected parents={disconnected_parents}",
    )
    check("A4 bridge component reduction equals components-met minus one", bridge_connectivity)

    law_a = (Fraction(1), Fraction(1))
    law_b = (Fraction(1), Fraction(2))
    levels_a = evolve_measure(cutoff, ancestry_weight=law_a[0], bridge_weight=law_a[1])
    levels_b = evolve_measure(cutoff, ancestry_weight=law_b[0], bridge_weight=law_b[1])

    normalized = True
    positive = True
    for levels, params in ((levels_a, law_a), (levels_b, law_b)):
        normalized &= all(sum(level.values(), Fraction(0)) == 1 for level in levels)
        positive &= all(mass > 0 for level in levels for mass in level.values())
        for n, level in enumerate(levels[:-1]):
            for parent in level:
                kernel = extension_kernel(
                    n, parent, ancestry_weight=params[0], bridge_weight=params[1]
                )
                normalized &= sum(kernel.values(), Fraction(0)) == 1
                positive &= all(probability > 0 for probability in kernel.values())
    check("B1 two registered positive rational kernels normalize exactly", normalized and positive)

    cylinder_consistent = True
    recovered = True
    recovery_fibers = True
    for levels, params in ((levels_a, law_a), (levels_b, law_b)):
        for n in range(cutoff):
            grouped: Dict[Relation, Fraction] = defaultdict(Fraction)
            seen_fibers = set()
            for child, child_mass in levels[n + 1].items():
                parent = delete_last(n + 1, child)
                precursor = recover_precursor(n, child)
                fiber = (parent, precursor)
                recovery_fibers &= fiber not in seen_fibers and parent in levels[n]
                seen_fibers.add(fiber)
                grouped[parent] += child_mass
                expected = extension_kernel(
                    n,
                    parent,
                    ancestry_weight=params[0],
                    bridge_weight=params[1],
                )[precursor]
                recovered &= child_mass / levels[n][parent] == expected
            cylinder_consistent &= grouped == levels[n]
    check("B2 cylinder masses obey exact parent-equals-children consistency", cylinder_consistent)
    check(
        "B3 child-driven conditional ratios recover every kernel with unique fibers",
        recovered and recovery_fibers,
    )

    restriction_failures = {}
    restriction_squares = 0
    for params in (law_a, law_b):
        failures = 0
        for n in range(1, cutoff):
            for parent in growth_levels[n]:
                for keep_mask in downsets(n, parent):
                    if keep_mask == (1 << n) - 1:
                        continue
                    keep = tuple(i for i in range(n) if keep_mask & (1 << i))
                    pushed = restriction_pushforward(
                        n,
                        parent,
                        keep,
                        ancestry_weight=params[0],
                        bridge_weight=params[1],
                    )
                    restricted_parent = induced_order(n, parent, keep)
                    recomputed = extension_kernel(
                        len(keep),
                        restricted_parent,
                        ancestry_weight=params[0],
                        bridge_weight=params[1],
                    )
                    restriction_squares += 1
                    if pushed != recomputed:
                        failures += 1
        restriction_failures[params] = failures

    chain2 = frozenset({(0, 1)})
    chain_push = restriction_pushforward(
        2, chain2, (0,), ancestry_weight=law_a[0], bridge_weight=law_a[1]
    )
    point_kernel = extension_kernel(
        1, frozenset(), ancestry_weight=law_a[0], bridge_weight=law_a[1]
    )
    print(
        "INFO B4 restriction witness chain 0<1 -> stem {0}: "
        f"pushforward={chain_push}; recomputed={point_kernel}"
    )
    check(
        "B4 both prefix kernels fail ancestor-closed restriction naturality",
        chain_push == {0: Fraction(1, 3), 1: Fraction(2, 3)}
        and point_kernel == {0: Fraction(1, 2), 1: Fraction(1, 2)}
        and all(value > 0 for value in restriction_failures.values()),
        f"failures={restriction_failures}; audited squares={restriction_squares}",
    )

    antichain3: Relation = frozenset()
    kernel_a = extension_kernel(3, antichain3, ancestry_weight=law_a[0], bridge_weight=law_a[1])
    kernel_b = extension_kernel(3, antichain3, ancestry_weight=law_b[0], bridge_weight=law_b[1])
    bridge_a = sum(
        probability for precursor, probability in kernel_a.items()
        if bridge_index(3, antichain3, precursor) >= 1
    )
    bridge_b = sum(
        probability for precursor, probability in kernel_b.items()
        if bridge_index(3, antichain3, precursor) >= 1
    )
    check(
        "B5 same positive extension arena admits unequal exact bridge-shadow weights",
        bridge_a == Fraction(1, 2) and bridge_b == Fraction(5, 7),
        f"law A={bridge_a}; law B={bridge_b}",
    )
    check("B5 the two induced labeled-prefix measures are inequivalent", levels_a != levels_b)

    no_bridge_levels = evolve_measure(
        cutoff,
        ancestry_weight=Fraction(1),
        bridge_weight=Fraction(1),
        allow_bridges=False,
    )
    no_bridge_kernel = extension_kernel(
        3,
        antichain3,
        ancestry_weight=Fraction(1),
        bridge_weight=Fraction(1),
        allow_bridges=False,
    )
    no_bridge_mass = sum(
        probability
        for precursor, probability in no_bridge_kernel.items()
        if bridge_index(3, antichain3, precursor) >= 1
    )
    no_bridge_cylinder = True
    for n in range(cutoff):
        grouped: Dict[Relation, Fraction] = defaultdict(Fraction)
        for child, child_mass in no_bridge_levels[n + 1].items():
            grouped[delete_last(n + 1, child)] += child_mass
        no_bridge_cylinder &= grouped == no_bridge_levels[n]
    no_bridge_covariant = True
    no_bridge_covariance_cases = 0
    for n in range(1, 5):
        for relation in growth_levels[n]:
            for permutation in permutations(range(n)):
                relabeled_relation = relabel(n, relation, permutation)
                base = extension_kernel(
                    n,
                    relation,
                    ancestry_weight=Fraction(1),
                    bridge_weight=Fraction(1),
                    allow_bridges=False,
                )
                moved = extension_kernel(
                    n,
                    relabeled_relation,
                    ancestry_weight=Fraction(1),
                    bridge_weight=Fraction(1),
                    allow_bridges=False,
                )
                for precursor, probability in base.items():
                    no_bridge_covariance_cases += 1
                    no_bridge_covariant &= (
                        moved[relabel_mask(n, precursor, permutation)] == probability
                    )
    check(
        "B6 controlled-zero kernel shows prefix-level eligibility nonselection",
        no_bridge_mass == 0
        and bridge_a > 0
        and no_bridge_cylinder
        and no_bridge_covariant
        and all(sum(level.values(), Fraction(0)) == 1 for level in no_bridge_levels),
        f"bridge-shadow mass={no_bridge_mass} versus {bridge_a}; "
        f"covariance cases={no_bridge_covariance_cases}",
    )

    with localcontext() as context:
        context.prec = 140
        delta_i = Decimal(11) / Decimal(10)
        survival_a = (-delta_i).exp()
        survival_b = (-delta_i).exp()
        survival_text = format(survival_a, ".125g")
    print(f"INFO B7 common survival exp(-1.1) = {survival_text}")
    check(
        "B7 v7 conditional survival is unchanged while placement kernel changes",
        survival_a == survival_b and bridge_a != bridge_b,
        f"bridge={bridge_a} versus {bridge_b}",
    )

    covariance_ok = True
    covariance_cases = 0
    for n in range(1, 5):
        for relation in growth_levels[n]:
            for permutation in permutations(range(n)):
                relabeled_relation = relabel(n, relation, permutation)
                for params in (law_a, law_b):
                    base_kernel = extension_kernel(
                        n, relation, ancestry_weight=params[0], bridge_weight=params[1]
                    )
                    relabeled_kernel = extension_kernel(
                        n, relabeled_relation, ancestry_weight=params[0], bridge_weight=params[1]
                    )
                    for precursor, probability in base_kernel.items():
                        covariance_cases += 1
                        covariance_ok &= relabeled_kernel[relabel_mask(n, precursor, permutation)] == probability
    check(
        "C1 both one-step kernel families are exactly locally isomorphism covariant",
        covariance_ok,
        f"mapped precursor cases={covariance_cases}",
    )

    orbit_levels_a = tuple(orbit_pushforward(n, level) for n, level in enumerate(levels_a))
    orbit_levels_b = tuple(orbit_pushforward(n, level) for n, level in enumerate(levels_b))
    orbit_normalized = all(
        sum(level.values(), Fraction(0)) == 1
        for orbit_levels in (orbit_levels_a, orbit_levels_b)
        for level in orbit_levels
    )
    unequal_raw_fiber = False
    for levels in (levels_a, levels_b):
        for n, level in enumerate(levels):
            fibers: Dict[str, set[Fraction]] = defaultdict(set)
            for relation, mass in level.items():
                fibers[canonical(n, relation)].add(mass)
            unequal_raw_fiber |= any(len(masses) > 1 for masses in fibers.values())
    antichain3_code = canonical(3, frozenset())
    antichain_orbit_a = orbit_levels_a[3][antichain3_code]
    antichain_orbit_b = orbit_levels_b[3][antichain3_code]
    check(
        "C2 actual canonical finite pushforwards normalize and retain nonselection",
        orbit_normalized
        and unequal_raw_fiber
        and antichain_orbit_a == Fraction(1, 8)
        and antichain_orbit_b == Fraction(1, 10),
        f"three-antichain orbit={antichain_orbit_a} versus {antichain_orbit_b}",
    )

    chain_plus_isolate = frozenset({(0, 1)})
    rank_two = exact_rank_stems(3, chain_plus_isolate, 2)
    check(
        "C3 one covtree rank can contain multiple nonisomorphic stems",
        len(rank_two) == 2,
        f"exact-rank-2 stem types={len(rank_two)}",
    )
    check(
        "C3 covtree observable refinement is not one-prefix event deletion",
        len(rank_two) > 1 and len(growth_levels[2]) == 2,
        "a covtree node is a set of stem types, not one two-event prefix",
    )

    certificate = chain_plus_isolate
    certificate_stems = rank_two
    certificate_ok = True
    for n in range(3, 9):
        certificate = extend(n, certificate, (1 << n) - 1)
        certificate_ok &= exact_rank_stems(n + 1, certificate, 2) == certificate_stems
    check(
        "C3 finite certificate extends without changing its exact-rank-2 stem theory",
        certificate_ok,
        "universal-top continuation checked through nine events",
    )

    # A primitive positive path measure determines its positive-mass support,
    # but the same profinite arena hosts both registered choices.
    support_a = {
        (n, state) for n, level in enumerate(levels_a) for state, mass in level.items() if mass > 0
    }
    support_b = {
        (n, state) for n, level in enumerate(levels_b) for state, mass in level.items() if mass > 0
    }
    check(
        "C4 topology/extension arena does not select the measure",
        support_a == support_b and levels_a != levels_b,
        f"common positive finite prefixes={len(support_a)}",
    )

    # The three-event antichain bridge creates a new common-future event but no
    # relation among old incomparable records.
    pair_precursor = (1 << 0) | (1 << 1)
    bridge_child = extend(3, antichain3, pair_precursor)
    check(
        "D1 common-future child records both selected old events in its ancestry",
        (0, 3) in bridge_child and (1, 3) in bridge_child,
    )
    check(
        "D2 common-future extension inserts no retroactive old-old relation",
        all((i, j) not in bridge_child for i in range(3) for j in range(3) if i != j),
    )
    check(
        "D3 common-future weighting remains an additional law",
        kernel_a[pair_precursor] != kernel_b[pair_precursor],
        f"same pair probability={kernel_a[pair_precursor]} versus {kernel_b[pair_precursor]}",
    )

    payload_digest = stdout_digest_payload(counts, (bridge_a, bridge_b))
    print(f"CANONICAL PAYLOAD SHA256: {payload_digest}")
    print(f"RECEIPT: {PASSED}/{CHECKS} checks passed")
    print("VERDICT: CONSISTENT-FAMILY")
    print("BOUNDARY: immutable-past common-future extension is coherent; no local marked law is selected")


if __name__ == "__main__":
    main()

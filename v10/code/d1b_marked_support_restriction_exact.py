#!/usr/bin/env python3
"""D1B exact receipt: marked record histories, local seams, and typed restriction.

This receipt is deliberately separate from d1_no_silent_center_exact.py.  The
first receipt tests a finite conditional-independence filter.  This one asks
whether the boundary objects used by that filter have enough record structure
to support claims about locality, support birth, and restriction.

All pass/fail decisions use integer arithmetic.  No tolerance participates in
the verdict.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from itertools import combinations, product
from typing import Dict, FrozenSet, Iterable, Mapping, Sequence, Tuple


Atom = Tuple[int, ...]
Partition = Tuple[Tuple[int, ...], ...]
Support = FrozenSet[str]


def check(label: str, condition: bool) -> None:
    global CHECKS, PASSED
    CHECKS += 1
    if not condition:
        raise AssertionError(label)
    PASSED += 1
    print(f"PASS {CHECKS:02d}: {label}")


def canon_partition(labels: Sequence[object]) -> Partition:
    blocks: Dict[object, list[int]] = {}
    order: list[object] = []
    for atom, label in enumerate(labels):
        if label not in blocks:
            blocks[label] = []
            order.append(label)
        blocks[label].append(atom)
    return tuple(sorted((tuple(blocks[label]) for label in order), key=lambda b: b[0]))


def refines(fine: Partition, coarse: Partition) -> bool:
    coarse_sets = [set(block) for block in coarse]
    return all(any(set(block) <= target for target in coarse_sets) for block in fine)


def exact_ci(table: Sequence[Sequence[Sequence[int]]], partition: Partition) -> bool:
    """X and Z are conditionally independent in every partition block."""
    nx = len(table)
    nz = len(table[0])
    for block in partition:
        aggregate = [[sum(table[x][z][b] for b in block) for z in range(nz)] for x in range(nx)]
        for x1 in range(nx):
            for x2 in range(x1 + 1, nx):
                for z1 in range(nz):
                    for z2 in range(z1 + 1, nz):
                        if aggregate[x1][z1] * aggregate[x2][z2] != aggregate[x1][z2] * aggregate[x2][z1]:
                            return False
    return True


def is_lookup(partition: Partition, occupied: FrozenSet[int]) -> bool:
    return all(len(set(block) & occupied) <= 1 for block in partition)


@dataclass(frozen=True)
class BoundaryField:
    """A named, marked boundary observable.

    carrier is the set of record lineages to which the field is jointly
    available.  provenance is stable under restriction; projected is an
    idempotent type marker, not a name-changing operation.
    """

    name: str
    carrier: Support
    values: Tuple[int, ...]
    kind: str
    provenance: str
    projected: bool = False


@dataclass(frozen=True)
class JointLaw:
    lineages: Tuple[str, ...]
    outcomes: Tuple[Atom, ...]
    counts: Tuple[Tuple[int, ...], ...]  # outcome by boundary atom

    @property
    def boundary_atoms(self) -> int:
        return len(self.counts[0])

    def restrict(self, keep: Support) -> "JointLaw":
        new_lineages = tuple(lineage for lineage in self.lineages if lineage in keep)
        indices = tuple(self.lineages.index(lineage) for lineage in new_lineages)
        aggregate: Dict[Atom, list[int]] = {}
        for outcome, row in zip(self.outcomes, self.counts):
            projected = tuple(outcome[index] for index in indices)
            aggregate.setdefault(projected, [0] * self.boundary_atoms)
            for b, count in enumerate(row):
                aggregate[projected][b] += count
        outcomes = tuple(sorted(aggregate))
        return JointLaw(new_lineages, outcomes, tuple(tuple(aggregate[outcome]) for outcome in outcomes))


@dataclass(frozen=True)
class MarkedHistory:
    lineages: Tuple[str, ...]
    parents: Tuple[Tuple[str, str | None], ...]
    ports: Tuple[Tuple[str, str], ...]
    fields: Tuple[BoundaryField, ...]
    existing_supports: Tuple[Support, ...]
    law: JointLaw

    def restrict(self, keep: Support) -> "MarkedHistory":
        kept_lineages = tuple(lineage for lineage in self.lineages if lineage in keep)
        projected_fields = []
        for field in self.fields:
            carrier = field.carrier & keep
            if carrier:
                projected_fields.append(replace(field, carrier=carrier, projected=field.projected or carrier != field.carrier))
        projected_supports = sorted(
            {support & keep for support in self.existing_supports if len(support & keep) >= 2},
            key=support_key,
        )
        return MarkedHistory(
            kept_lineages,
            tuple((lineage, parent) for lineage, parent in self.parents if lineage in keep),
            tuple((lineage, port) for lineage, port in self.ports if lineage in keep),
            tuple(projected_fields),
            tuple(projected_supports),
            self.law.restrict(keep),
        )


def support_key(support: Support) -> Tuple[int, Tuple[str, ...]]:
    return len(support), tuple(sorted(support))


def connected_components(history: MarkedHistory) -> Tuple[Support, ...]:
    adjacency = {lineage: {lineage} for lineage in history.lineages}

    def join(carrier: Iterable[str]) -> None:
        carrier = tuple(carrier)
        for left in carrier:
            for right in carrier:
                adjacency[left].add(right)

    parent_groups: Dict[str, list[str]] = {}
    for lineage, parent in history.parents:
        if parent is not None:
            parent_groups.setdefault(parent, []).append(lineage)
    for group in parent_groups.values():
        join(group)
    for support in history.existing_supports:
        join(support)
    for field in history.fields:
        if field.kind in {"ancestor", "joint-boundary"}:
            join(field.carrier)

    unseen = set(history.lineages)
    components = []
    while unseen:
        seed = min(unseen)
        stack = [seed]
        reached = set()
        while stack:
            item = stack.pop()
            if item in reached:
                continue
            reached.add(item)
            stack.extend(adjacency[item] - reached)
        unseen -= reached
        components.append(frozenset(reached))
    return tuple(sorted(components, key=support_key))


def candidate_supports(history: MarkedHistory) -> Tuple[Support, ...]:
    """An ancestry-local seam generator, explicitly supplied as an axiom.

    Candidate carriers are direct structural hyperedges: a sibling group with
    one recorded parent, an existing support, or a marked joint field carrier.
    Overlapping carriers are *not* transitively completed.  Only lineages
    exposing an output port can participate.
    """
    port_lineages = {lineage for lineage, port in history.ports if port.startswith("out:")}
    carriers: set[Support] = set()
    parent_groups: Dict[str, set[str]] = {}
    for lineage, parent in history.parents:
        if parent is not None:
            parent_groups.setdefault(parent, set()).add(lineage)
    carriers.update(frozenset(group) for group in parent_groups.values() if len(group) >= 2)
    carriers.update(history.existing_supports)
    carriers.update(
        field.carrier
        for field in history.fields
        if field.kind in {"ancestor", "joint-boundary"} and len(field.carrier) >= 2
    )
    candidates = []
    for carrier in carriers:
        ordered = sorted(carrier & port_lineages)
        for size in range(2, len(ordered) + 1):
            candidates.extend(frozenset(choice) for choice in combinations(ordered, size))
    return tuple(sorted(set(candidates), key=support_key))


def table_for_cut(law: JointLaw, left: Support, right: Support) -> Tuple[Tuple[Tuple[int, ...], ...], ...]:
    active = left | right
    restricted = law.restrict(active)
    left_indices = tuple(restricted.lineages.index(lineage) for lineage in sorted(left))
    right_indices = tuple(restricted.lineages.index(lineage) for lineage in sorted(right))
    left_values = sorted({tuple(outcome[index] for index in left_indices) for outcome in restricted.outcomes})
    right_values = sorted({tuple(outcome[index] for index in right_indices) for outcome in restricted.outcomes})
    left_lookup = {value: index for index, value in enumerate(left_values)}
    right_lookup = {value: index for index, value in enumerate(right_values)}
    table = [[[0] * restricted.boundary_atoms for _ in right_values] for _ in left_values]
    for outcome, counts in zip(restricted.outcomes, restricted.counts):
        x = left_lookup[tuple(outcome[index] for index in left_indices)]
        z = right_lookup[tuple(outcome[index] for index in right_indices)]
        for b, count in enumerate(counts):
            table[x][z][b] += count
    return tuple(tuple(tuple(row) for row in plane) for plane in table)


def screen_fields(history: MarkedHistory, support: Support) -> Tuple[BoundaryField, ...]:
    return tuple(field for field in history.fields if field.kind == "screen" and support <= field.carrier)


def center_fields(history: MarkedHistory, support: Support) -> Tuple[BoundaryField, ...]:
    return tuple(
        field
        for field in history.fields
        if field.kind in {"ancestor", "joint-boundary", "center-candidate"} and support <= field.carrier
    )


def partition_from_fields(fields: Sequence[BoundaryField], selected: Sequence[int], boundary_atoms: int) -> Partition:
    labels = []
    for b in range(boundary_atoms):
        labels.append(tuple(fields[index].values[b] for index in selected))
    return canon_partition(labels)


def visible_screen_partition(history: MarkedHistory, support: Support) -> Partition:
    screens = screen_fields(history, support)
    return partition_from_fields(screens, tuple(range(len(screens))), history.law.boundary_atoms)


def admissible_centers(
    history: MarkedHistory, support: Support, table: Sequence[Sequence[Sequence[int]]]
) -> Tuple[Tuple[Partition, Tuple[Tuple[str, str], ...]], ...]:
    """Enumerate only algebras generated by marked boundary fields.

    Generator identity is the typed pair (field name, stable provenance), not
    merely the induced atom partition.  D1B treats both marks as physical until
    a later ontology explicitly supplies a gauge quotient.
    """
    screen = screen_fields(history, support)
    centers = center_fields(history, support)
    fields = screen + centers
    screen_indices = tuple(range(len(screen)))
    generated: Dict[Partition, set[Tuple[Tuple[str, str], ...]]] = {}
    for size in range(len(centers) + 1):
        for chosen in combinations(range(len(centers)), size):
            selected = screen_indices + tuple(len(screen) + index for index in chosen)
            partition = partition_from_fields(fields, selected, history.law.boundary_atoms)
            generators = tuple(
                sorted((centers[index].name, centers[index].provenance) for index in chosen)
            )
            if exact_ci(table, partition):
                generated.setdefault(partition, set()).add(generators)
    minimal_partitions = {
        partition
        for partition in generated
        if not any(other != partition and refines(partition, other) for other in generated)
    }
    minima = []
    for partition in minimal_partitions:
        selections = generated[partition]
        irredundant = [
            selection
            for selection in selections
            if not any(set(other) < set(selection) for other in selections)
        ]
        minima.extend((partition, selection) for selection in irredundant)
    return tuple(sorted(minima, key=lambda item: (len(item[0]), item[0], item[1])))


def occupied_atoms(table: Sequence[Sequence[Sequence[int]]]) -> FrozenSet[int]:
    boundary_atoms = len(table[0][0])
    return frozenset(
        b
        for b in range(boundary_atoms)
        if sum(table[x][z][b] for x in range(len(table)) for z in range(len(table[0]))) > 0
    )


def cut_center_status(
    history: MarkedHistory, left: Support, right: Support
) -> Tuple[Tuple[Partition, Tuple[Tuple[str, str], ...]], ...]:
    support = left | right
    table = table_for_cut(history.law, left, right)
    return tuple(
        item for item in admissible_centers(history, support, table) if not is_lookup(item[0], occupied_atoms(table))
    )


def support_is_eligible(history: MarkedHistory, support: Support) -> bool:
    ordered = tuple(sorted(support))
    cuts = []
    for size in range(1, len(ordered)):
        for left_tuple in combinations(ordered, size):
            left = frozenset(left_tuple)
            right = support - left
            if tuple(sorted(left)) > tuple(sorted(right)):
                continue
            cuts.append((left, right))
    if not cuts:
        return False
    for left, right in cuts:
        table = table_for_cut(history.law, left, right)
        screen = visible_screen_partition(history, support)
        if exact_ci(table, screen):
            return False
        status = cut_center_status(history, left, right)
        if len(status) != 1 or status[0][0] == screen or not status[0][1]:
            return False
    return True


def eligible_supports(history: MarkedHistory) -> Tuple[Support, ...]:
    return tuple(support for support in candidate_supports(history) if support_is_eligible(history, support))


def project_support_family(supports: Sequence[Support], keep: Support) -> Tuple[Support, ...]:
    return tuple(
        sorted(
            {support & keep for support in supports if len(support & keep) >= 2},
            key=support_key,
        )
    )


def product_joint_history() -> MarkedHistory:
    lineages = ("A", "B", "C")
    outcomes = tuple(product((0, 1), repeat=3))
    vectors = {
        "A": ((3, 1), (1, 3)),
        "B": ((4, 1), (1, 4)),
        "C": ((5, 1), (1, 5)),
    }
    boundary_h = (0, 0, 1, 1)
    counts = []
    for outcome in outcomes:
        row = []
        for h in boundary_h:
            count = 1
            for lineage, value in zip(lineages, outcome):
                count *= vectors[lineage][h][value]
            row.append(count)
        counts.append(tuple(row))
    law = JointLaw(lineages, outcomes, tuple(counts))
    fields = (
        BoundaryField("H", frozenset(lineages), boundary_h, "ancestor", "root:H"),
        BoundaryField("N", frozenset({"A"}), (0, 1, 0, 1), "nuisance", "A:N"),
    )
    return MarkedHistory(
        lineages,
        (("A", "root"), ("B", "root"), ("C", "root")),
        (("A", "out:A"), ("B", "out:B"), ("C", "out:C")),
        fields,
        (),
        law,
    )


def disconnected_history() -> MarkedHistory:
    # The law is statistically dependent, but no parent, support, or joint field
    # licenses a cross-component seam.
    outcomes = ((0, 0), (0, 1), (1, 0), (1, 1))
    counts = ((9,), (1,), (1,), (9,))
    return MarkedHistory(
        ("A", "B"),
        (("A", "root:A"), ("B", "root:B")),
        (("A", "out:A"), ("B", "out:B")),
        (),
        (),
        JointLaw(("A", "B"), outcomes, counts),
    )


def connected_factorized_history() -> MarkedHistory:
    outcomes = ((0, 0), (0, 1), (1, 0), (1, 1))
    counts = tuple((1, 1, 1, 1) for _ in outcomes)
    return MarkedHistory(
        ("A", "B"),
        (("A", "root"), ("B", "root")),
        (("A", "out:A"), ("B", "out:B")),
        (BoundaryField("H", frozenset({"A", "B"}), (0, 0, 1, 1), "ancestor", "root:H"),),
        (),
        JointLaw(("A", "B"), outcomes, counts),
    )


def overlapping_pair_history() -> MarkedHistory:
    outcomes = tuple(product((0, 1), repeat=3))
    counts = tuple((1,) for _ in outcomes)
    return MarkedHistory(
        ("A", "B", "C"),
        (("A", "root:A"), ("B", "root:B"), ("C", "root:C")),
        (("A", "out:A"), ("B", "out:B"), ("C", "out:C")),
        (),
        (frozenset({"A", "B"}), frozenset({"B", "C"})),
        JointLaw(("A", "B", "C"), outcomes, counts),
    )


def synergy_projectivity_history() -> MarkedHistory:
    """Pairwise-independent but jointly dependent common-root history."""
    lineages = ("A", "R", "Z")
    outcomes = tuple(product((0, 1), repeat=3))
    a = ((3, 1), (1, 3))
    r = ((4, 1), (1, 4))
    z = ((5, 1), (1, 5))
    states = tuple((u, v, nuisance) for u, v in product((0, 1), repeat=2) for nuisance in (0, 1))
    counts = []
    for av, rv, zv in outcomes:
        row = []
        for u, v, _ in states:
            parity = u ^ v
            row.append(a[u][av] * r[parity][rv] * z[v][zv])
        counts.append(tuple(row))
    return MarkedHistory(
        lineages,
        (("A", "root"), ("R", "root"), ("Z", "root")),
        (("A", "out:A"), ("R", "out:R"), ("Z", "out:Z")),
        (
            BoundaryField(
                "H",
                frozenset(lineages),
                tuple(2 * u + v for u, v, _ in states),
                "ancestor",
                "root:Huv",
            ),
            BoundaryField(
                "N",
                frozenset({"A"}),
                tuple(nuisance for _, _, nuisance in states),
                "nuisance",
                "A:N",
            ),
        ),
        (),
        JointLaw(lineages, outcomes, tuple(counts)),
    )


def robust_competing_history() -> MarkedHistory:
    matrices = (
        ((16, 4), (4, 1)),
        ((3, 2), (12, 8)),
        ((1, 4), (4, 16)),
        ((2, 8), (3, 12)),
    )
    outcomes = ((0, 0), (0, 1), (1, 0), (1, 1))
    counts = tuple(tuple(matrices[b][x][z] for b in range(4)) for x, z in outcomes)
    return MarkedHistory(
        ("A", "B"),
        (("A", "root:A"), ("B", "root:B")),
        (("A", "out:A"), ("B", "out:B")),
        (
            BoundaryField("R", frozenset({"A", "B"}), (0, 1, 1, 2), "center-candidate", "AB:R"),
            BoundaryField("C", frozenset({"A", "B"}), (0, 1, 2, 2), "center-candidate", "AB:C"),
        ),
        (frozenset({"A", "B"}),),
        JointLaw(("A", "B"), outcomes, counts),
    )


def canonical_history(history: MarkedHistory) -> tuple:
    return (
        history.lineages,
        history.parents,
        history.ports,
        tuple((f.name, tuple(sorted(f.carrier)), f.values, f.kind, f.provenance, f.projected) for f in history.fields),
        tuple(tuple(sorted(support)) for support in history.existing_supports),
        history.law,
    )


def main() -> None:
    global CHECKS, PASSED
    CHECKS = 0
    PASSED = 0

    root = product_joint_history()
    check("M1 marked root history has one structural component", connected_components(root) == (frozenset({"A", "B", "C"}),))
    check(
        "M2 ancestry-local generator supplies all pair and triple candidates",
        candidate_supports(root)
        == (
            frozenset({"A", "B"}),
            frozenset({"A", "C"}),
            frozenset({"B", "C"}),
            frozenset({"A", "B", "C"}),
        ),
    )
    root_without_c_port = replace(root, ports=tuple(item for item in root.ports if item[0] != "C"))
    check(
        "M2b removing C's output port removes every C-bearing candidate",
        candidate_supports(root_without_c_port) == (frozenset({"A", "B"}),),
    )

    pair_statuses = {}
    for pair in (frozenset({"A", "B"}), frozenset({"A", "C"}), frozenset({"B", "C"})):
        left = frozenset({min(pair)})
        right = pair - left
        pair_statuses[pair] = cut_center_status(root, left, right)
    check(
        "M3 every pair cut has the unique marked nonlookup center H",
        all(len(status) == 1 and status[0][1] == (("H", "root:H"),) for status in pair_statuses.values()),
    )

    triple_cuts = (
        (frozenset({"A", "B"}), frozenset({"C"})),
        (frozenset({"A", "C"}), frozenset({"B"})),
        (frozenset({"B", "C"}), frozenset({"A"})),
    )
    check(
        "M4 all three bipartitions of ABC have the unique marked center H",
        all(
            len(cut_center_status(root, left, right)) == 1
            and cut_center_status(root, left, right)[0][1] == (("H", "root:H"),)
            for left, right in triple_cuts
        ),
    )
    check(
        "M5 cutwise eligibility leaves pair and triple supports simultaneously eligible",
        eligible_supports(root) == candidate_supports(root),
    )
    factorized = connected_factorized_history()
    check(
        "M6 a connected but factorized support is a candidate and is refused as already complete",
        candidate_supports(factorized) == (frozenset({"A", "B"}),)
        and exact_ci(
            table_for_cut(factorized.law, frozenset({"A"}), frozenset({"B"})),
            visible_screen_partition(factorized, frozenset({"A", "B"})),
        )
        and eligible_supports(factorized) == (),
    )
    complete_screen = replace(
        root,
        fields=(replace(root.fields[0], kind="screen"), root.fields[1]),
    )
    check(
        "M7 a visible complete H screen refuses every otherwise structural candidate",
        candidate_supports(complete_screen) == candidate_supports(root)
        and eligible_supports(complete_screen) == (),
    )
    duplicate_h = replace(
        root,
        fields=(
            replace(root.fields[0], name="A@B", provenance="C"),
            root.fields[1],
            replace(root.fields[0], name="A", provenance="B@C"),
        ),
    )
    duplicate_status = cut_center_status(duplicate_h, frozenset({"A"}), frozenset({"B"}))
    check(
        "M8 delimiter-adversarial provenance fields remain two typed center algebras",
        len(duplicate_status) == 2
        and len({partition for partition, _ in duplicate_status}) == 1
        and {selection for _, selection in duplicate_status}
        == {(("A@B", "C"),), (("A", "B@C"),)}
        and frozenset({"A", "B"}) not in eligible_supports(duplicate_h),
    )

    disconnected = disconnected_history()
    check("L1 disconnected marked history has two structural components", len(connected_components(disconnected)) == 2)
    disconnected_table = table_for_cut(disconnected.law, frozenset({"A"}), frozenset({"B"}))
    check(
        "L2 exact statistical dependence alone does not license a cross-component candidate seam",
        not exact_ci(disconnected_table, ((0,),)) and candidate_supports(disconnected) == (),
    )
    check("L3 therefore no cross-component support can pass the filter", eligible_supports(disconnected) == ())
    overlapping = overlapping_pair_history()
    check(
        "L4 overlapping AB and BC carriers do not transitively license AC or ABC",
        connected_components(overlapping) == (frozenset({"A", "B", "C"}),)
        and candidate_supports(overlapping)
        == (frozenset({"A", "B"}), frozenset({"B", "C"})),
    )

    ab = root.restrict(frozenset({"A", "B"}))
    check("R1 genuine record restriction projects lineages, ports, law, and field carriers", ab.lineages == ("A", "B") and ab.fields[0].carrier == frozenset({"A", "B"}) and ab.fields[0].projected)
    check("R2 the restricted AB history recomputes exactly one candidate support", candidate_supports(ab) == (frozenset({"A", "B"}),))
    check("R3 the restricted AB support remains uniquely eligible through H", eligible_supports(ab) == (frozenset({"A", "B"}),) and cut_center_status(ab, frozenset({"A"}), frozenset({"B"}))[0][1] == (("H", "root:H"),))
    check(
        "R3b projecting the full eligible-support family equals recomputation on AB",
        project_support_family(eligible_supports(root), frozenset({"A", "B"})) == eligible_supports(ab),
    )

    direct_a = root.restrict(frozenset({"A"}))
    successive_a = root.restrict(frozenset({"A", "B"})).restrict(frozenset({"A"}))
    check("R4 marked record restriction is idempotent/path-independent on ABC to A", canonical_history(direct_a) == canonical_history(successive_a))
    check("R5 no support candidate survives a one-lineage restriction", candidate_supports(direct_a) == () and eligible_supports(direct_a) == ())
    root_set = frozenset(root.lineages)
    nonempty_keeps = tuple(
        frozenset(choice)
        for size in range(1, len(root.lineages) + 1)
        for choice in combinations(root.lineages, size)
    )
    check(
        "R6 support-family projection agrees with recomputation on every nonempty root restriction",
        all(
            project_support_family(eligible_supports(root), keep) == eligible_supports(root.restrict(keep))
            for keep in nonempty_keeps
        ),
    )
    nested_paths = []
    for middle in nonempty_keeps:
        if not middle <= root_set:
            continue
        ordered_middle = tuple(sorted(middle))
        for size in range(1, len(ordered_middle) + 1):
            for choice in combinations(ordered_middle, size):
                nested_paths.append((middle, frozenset(choice)))
    check(
        "R7 typed history restriction is path-independent on the full nonempty subset lattice",
        all(
            canonical_history(root.restrict(keep))
            == canonical_history(root.restrict(middle).restrict(keep))
            for middle, keep in nested_paths
        ),
    )

    synergy = synergy_projectivity_history()
    synergy_full = frozenset(synergy.lineages)
    check(
        "P1 parity/synergy history has only the triple support eligible",
        eligible_supports(synergy) == (synergy_full,),
    )
    synergy_az = synergy.restrict(frozenset({"A", "Z"}))
    check(
        "P2 every pair restriction is screen-complete and has no eligible support",
        all(
            eligible_supports(synergy.restrict(pair)) == ()
            for pair in (
                frozenset({"A", "R"}),
                frozenset({"A", "Z"}),
                frozenset({"R", "Z"}),
            )
        ),
    )
    check(
        "P3 typed eligibility-family naturality fails on ARZ to AZ",
        project_support_family(eligible_supports(synergy), frozenset({"A", "Z"}))
        == (frozenset({"A", "Z"}),)
        and eligible_supports(synergy_az) == (),
    )
    synergy_keeps = tuple(
        frozenset(choice)
        for size in range(1, len(synergy.lineages) + 1)
        for choice in combinations(synergy.lineages, size)
    )
    check(
        "P4 the marked history data remain path-independent despite eligibility failure",
        all(
            canonical_history(synergy.restrict(keep))
            == canonical_history(synergy.restrict(middle).restrict(keep))
            for middle in synergy_keeps
            for keep in synergy_keeps
            if keep <= middle
        ),
    )

    robust = robust_competing_history()
    robust_table = table_for_cut(robust.law, frozenset({"A"}), frozenset({"B"}))
    robust_minima = admissible_centers(robust, frozenset({"A", "B"}), robust_table)
    check("C1 marked-field census recovers exactly two incomparable minimal centers", len(robust_minima) == 2 and {names for _, names in robust_minima} == {(("R", "AB:R"),), (("C", "AB:C"),)})
    check("C2 both competing centers are nonlookup", all(not is_lookup(partition, occupied_atoms(robust_table)) for partition, _ in robust_minima))
    check("C3 the no-silent filter does not uniquely select between the marked centers", len(cut_center_status(robust, frozenset({"A"}), frozenset({"B"}))) == 2)

    print()
    print(f"RECEIPT: {PASSED}/{CHECKS} exact checks passed")
    print("SCOPE: centers are generated only by marked boundary fields; arbitrary atom partitions are excluded")
    print("POSITIVE: an explicitly supplied ancestry-local seam axiom blocks unsupported cross-component joins")
    print("POSITIVE: marked history data are path-independent on both tested subset lattices")
    print("REFUSAL: eligibility-family naturality fails on an exact parity/synergy restriction")
    print("REFUSAL: cutwise no-silent eligibility does not select one support from the supplied candidate family")
    print("REFUSAL: the seam axiom and the common-root field are additional record structure, not consequences of conditional independence")


if __name__ == "__main__":
    main()

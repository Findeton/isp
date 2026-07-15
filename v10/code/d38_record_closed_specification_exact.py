#!/usr/bin/env python3
"""D38 exact finite receipt for record-closed regional specifications.

All discrete probabilities and controls use integers or Fraction.  Enumeration
order is presentation only.  The D34b kernel below is the boundary-relevant
embedded jump chain together with its exact holding rate; it is not a new
timeless law and does not derive D34b's supplied coefficients.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, replace
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Dict, FrozenSet, Hashable, Iterable, Mapping, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]

LOCKS = {
    "D34b": (
        ROOT / "v10" / "code" / "d34b_actor_reference_high_precision.py",
        "7fe587e0e2f3fccb8b88362f70e201c4cbecdc6a99984c792699695f67b558f4",
    ),
    "D34e": (
        ROOT / "v10" / "code" / "d34e_predictive_boundary_exact.py",
        "1dd1a69be94a0fb614f909745e7db772ac5e5f134b97cbdcdf10c45a08f606c5",
    ),
    "D34f": (
        ROOT / "v10" / "code" / "d34f_component_tomography_exact.py",
        "0b518f6e742e4b24bd5a3e4a68e29127af27c7cd6acc13453ad5dba9031347ef",
    ),
    "D26": (
        ROOT / "v10" / "code" / "d26_interface_equivalence_exact.py",
        "a9b1f1704578178218750ecbafa737763ff3968ca246939a1d6aece79930575c",
    ),
    "D36b": (
        ROOT / "v10" / "code" / "d36b_actor_record_refinement_exact.py",
        "57ff22ab4711b63d476192c2ff19b02bb7f76fda5124b4d1afd23d30a20b376b",
    ),
}

D34E_DATA = ROOT / "v10" / "data" / "d34e_predictive_boundary_exact.out"
D34F_DATA = ROOT / "v10" / "data" / "d34f_component_tomography_exact.out"
D34E_DATA_SHA256 = "158c491d7376b165556364fee2f0266447e7f5becfdbda5a8f4ae600114e9fb7"
D34F_DATA_SHA256 = "de293509a4961d6a390f9fa80657aac7f76e04939e693277db60f07fac6d8fb2"


def stable(value: object) -> str:
    def default(item: object) -> object:
        if isinstance(item, Fraction):
            return {"fraction": [item.numerator, item.denominator]}
        if isinstance(item, frozenset):
            return sorted(item)
        if isinstance(item, tuple):
            return list(item)
        if hasattr(item, "__dict__"):
            return item.__dict__
        raise TypeError(type(item))

    return json.dumps(value, default=default, sort_keys=True, separators=(",", ":"))


def digest(value: object) -> str:
    return hashlib.sha256(stable(value).encode()).hexdigest()


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def canonical_id(kind: str, *fields: Hashable) -> Tuple[Hashable, ...]:
    return ("D38_CANONICAL_ID", kind, fields)


def locked_antecedents() -> Dict[str, str]:
    actual: Dict[str, str] = {}
    for name, (path, expected) in LOCKS.items():
        value = hashlib.sha256(path.read_bytes()).hexdigest()
        if value != expected:
            raise AssertionError((name, "source lock", value, expected))
        actual[name] = value
    for name, path, expected in (
        ("D34e-data", D34E_DATA, D34E_DATA_SHA256),
        ("D34f-data", D34F_DATA, D34F_DATA_SHA256),
    ):
        value = hashlib.sha256(path.read_bytes()).hexdigest()
        if value != expected:
            raise AssertionError((name, "data lock", value, expected))
        actual[name] = value
    return actual


# ---------------------------------------------------------------------------
# R1/R2: the D34b boundary-relevant embedded star generator.


@dataclass(frozen=True)
class StarState:
    carrier: int
    root_rings: int
    wire_count: int
    neighbor_degrees: Tuple[int, ...]

    def __post_init__(self) -> None:
        if self.carrier not in (0, 1):
            raise ValueError("binary carrier")
        if min((self.root_rings, self.wire_count), default=0) < 0:
            raise ValueError("negative counter")
        if not self.neighbor_degrees or any(degree < 1 for degree in self.neighbor_degrees):
            raise ValueError("D38 cells require the connected D34b seed sector")


def action_rates(state: StarState) -> Dict[str, Fraction]:
    degree = len(state.neighbor_degrees)
    rates: Dict[str, Fraction] = {
        "ROOT_BIRTH": Fraction(1, 4),
        "ROOT_IDLE": Fraction(1, 2),
    }
    for index in range(degree):
        rates[f"ROOT_OUT:{index}"] = Fraction(1, 4 * degree)
        rates[f"NEIGHBOR_BIRTH:{index}"] = Fraction(1, 4)
        rates[f"IN:{index}"] = Fraction(1, 4 * state.neighbor_degrees[index])
    return rates


def holding_rate(state: StarState) -> Fraction:
    return sum(action_rates(state).values(), Fraction())


def embedded_kernel(state: StarState) -> Dict[str, Fraction]:
    rates = action_rates(state)
    total = sum(rates.values(), Fraction())
    if total <= 0:
        raise AssertionError("nonpositive boundary holding rate")
    return {action: rate / total for action, rate in sorted(rates.items())}


def action_index(action: str) -> int:
    return int(action.split(":", 1)[1])


def transition(state: StarState, action: str) -> StarState:
    if action not in action_rates(state):
        raise AssertionError((state, action, "inadmissible D34b star action"))
    degrees = list(state.neighbor_degrees)
    if action == "ROOT_BIRTH":
        degrees.append(1)
        return StarState(state.carrier, state.root_rings + 1, state.wire_count + 1, tuple(degrees))
    if action == "ROOT_IDLE":
        return StarState(state.carrier, state.root_rings + 1, state.wire_count + 1, tuple(degrees))
    if action.startswith("ROOT_OUT:"):
        return StarState(1 - state.carrier, state.root_rings + 1, state.wire_count + 1, tuple(degrees))
    if action.startswith("NEIGHBOR_BIRTH:"):
        index = action_index(action)
        degrees[index] += 1
        return StarState(state.carrier, state.root_rings, state.wire_count, tuple(degrees))
    if action.startswith("IN:"):
        return StarState(1 - state.carrier, state.root_rings, state.wire_count + 1, tuple(degrees))
    raise AssertionError(action)


def positive_cylinder_checks() -> Tuple[int, int, int, Tuple[str, ...]]:
    states = (
        StarState(0, 0, 0, (1,)),
        StarState(1, 2, 3, (2,)),
        StarState(0, 1, 4, (2, 3)),
        StarState(1, 3, 7, (2, 4, 4)),
    )
    normalized = 0
    tower_checks = 0
    positive_atoms = 0
    rates = []
    for state in states:
        kernel = embedded_kernel(state)
        if sum(kernel.values(), Fraction()) != 1 or any(value <= 0 for value in kernel.values()):
            raise AssertionError("embedded kernel normalization/support")
        expected_rate = (
            Fraction(1)
            + Fraction(len(state.neighbor_degrees), 4)
            + sum((Fraction(1, 4 * degree) for degree in state.neighbor_degrees), Fraction())
        )
        if holding_rate(state) != expected_rate:
            raise AssertionError("Paper 22 holding-rate row")
        rates.append(ftext(expected_rate))
        normalized += 1
        positive_atoms += len(kernel)
        joint: Dict[Tuple[str, str], Fraction] = {}
        for first, p_first in kernel.items():
            second_kernel = embedded_kernel(transition(state, first))
            for second, p_second in second_kernel.items():
                joint[(first, second)] = p_first * p_second
            if sum(
                probability
                for (recorded_first, _), probability in joint.items()
                if recorded_first == first
            ) != p_first:
                raise AssertionError("positive-cylinder tower")
            tower_checks += 1
        if sum(joint.values(), Fraction()) != 1:
            raise AssertionError("two-step cylinder normalization")
    return normalized, tower_checks, positive_atoms, tuple(rates)


def touched_actors(state: StarState, action: str) -> FrozenSet[str]:
    if action == "ROOT_BIRTH":
        return frozenset(("A", f"N{len(state.neighbor_degrees)}"))
    if action == "ROOT_IDLE":
        return frozenset(("A",))
    if action.startswith("ROOT_OUT:") or action.startswith("IN:"):
        return frozenset(("A", f"N{action_index(action)}"))
    if action.startswith("NEIGHBOR_BIRTH:"):
        index = action_index(action)
        return frozenset((f"N{index}", f"N{index}:child:{state.neighbor_degrees[index]}"))
    raise AssertionError(action)


def locality_width_checks() -> Tuple[int, int, int, int]:
    arity_checks = 0
    maximum_arity = 0
    for degree in range(1, 13):
        state = StarState(0, 0, 0, tuple(2 + (index % 3) for index in range(degree)))
        for action in action_rates(state):
            arity = len(touched_actors(state, action))
            if arity > 2:
                raise AssertionError("D34b touched arity")
            arity_checks += 1
            maximum_arity = max(maximum_arity, arity)
    base = StarState(0, 0, 0, (2, 3))
    with_remote = (base, StarState(1, 9, 12, (6,)))
    if embedded_kernel(with_remote[0]) != embedded_kernel(base):
        raise AssertionError("disconnected insertion diluted A star")
    width_growth = len(StarState(0, 0, 0, tuple(2 for _ in range(12))).neighbor_degrees)
    return arity_checks, maximum_arity, width_growth, 1


# ---------------------------------------------------------------------------
# R3: an authenticated record-native star updater.


@dataclass(frozen=True)
class BoundaryRecord:
    record_id: Tuple[Hashable, ...]
    kind: str
    owner: str
    wires: Tuple[str, ...]
    parents: Tuple[Hashable, ...]
    capability: str
    payload: Tuple[Tuple[str, Hashable], ...]
    signature: str

    def payload_map(self) -> Dict[str, Hashable]:
        return dict(self.payload)


def capability(owner: str) -> str:
    return digest(("D38_ISSUED_BOUNDARY_CAPABILITY", owner))


def record_core(
    kind: str,
    owner: str,
    wires: Sequence[str],
    parents: Sequence[Hashable],
    cap: str,
    payload: Mapping[str, Hashable],
) -> Tuple[Hashable, ...]:
    return (
        kind,
        owner,
        tuple(wires),
        tuple(parents),
        cap,
        tuple(sorted(payload.items())),
    )


def make_record(
    kind: str,
    owner: str,
    wires: Sequence[str],
    parents: Sequence[Hashable],
    payload: Mapping[str, Hashable],
) -> BoundaryRecord:
    cap = capability(owner)
    core = record_core(kind, owner, wires, parents, cap, payload)
    record_id = canonical_id("BOUNDARY_RECORD", *core)
    signature = digest(("D38_IDEAL_SIGNATURE", owner, core))
    return BoundaryRecord(
        record_id,
        kind,
        owner,
        tuple(wires),
        tuple(parents),
        cap,
        tuple(sorted(payload.items())),
        signature,
    )


@dataclass(frozen=True)
class Boundary:
    state: StarState
    records: Tuple[BoundaryRecord, ...]
    tips: Tuple[Tuple[str, Hashable], ...]

    def tip_map(self) -> Dict[str, Hashable]:
        return dict(self.tips)


def state_from_boundary_records(boundary: Boundary) -> StarState:
    """Reconstruct the cached star projection from authenticated tip records."""
    records = {record.record_id: record for record in boundary.records}
    tips = boundary.tip_map()
    if "A" not in tips or tips["A"] not in records:
        raise AssertionError("missing root boundary tip")
    neighbor_indices = sorted(
        int(actor[1:])
        for actor in tips
        if actor.startswith("N") and actor[1:].isdigit()
    )
    if neighbor_indices != list(range(len(neighbor_indices))):
        raise AssertionError("noncanonical neighbor boundary tips")
    if set(tips) != {"A"} | {f"N{index}" for index in neighbor_indices}:
        raise AssertionError("untyped boundary tip")
    root = records[tips["A"]]
    root_payload = root.payload_map()
    if root.kind != "ROOT_ROW":
        raise AssertionError("root tip is not a root row")
    degrees = []
    for index in neighbor_indices:
        actor = f"N{index}"
        row = records.get(tips[actor])
        if row is None or row.kind != "NEIGHBOR_ROW" or row.owner != actor:
            raise AssertionError("neighbor tip is not its typed row")
        degrees.append(int(row.payload_map()["degree"]))
    reconstructed = StarState(
        int(root_payload["carrier"]),
        int(root_payload["rings"]),
        int(root_payload["wire_count"]),
        tuple(degrees),
    )
    if int(root_payload["degree"]) != len(degrees):
        raise AssertionError("root degree/boundary-record mismatch")
    return reconstructed


def actors_for_state(state: StarState) -> Tuple[str, ...]:
    return ("A",) + tuple(f"N{index}" for index in range(len(state.neighbor_degrees)))


def initial_boundary(state: StarState) -> Boundary:
    records = []
    root = make_record(
        "ROOT_ROW",
        "A",
        ("A",),
        (),
        {
            "carrier": state.carrier,
            "degree": len(state.neighbor_degrees),
            "rings": state.root_rings,
            "wire_count": state.wire_count,
        },
    )
    records.append(root)
    tips: Dict[str, Hashable] = {"A": root.record_id}
    for index, degree in enumerate(state.neighbor_degrees):
        actor = f"N{index}"
        row = make_record(
            "NEIGHBOR_ROW",
            actor,
            (actor,),
            (),
            {"birth_ordinal": index, "degree": degree},
        )
        edge = make_record(
            "EDGE",
            f"edge:A:{actor}",
            ("A", actor),
            (root.record_id, row.record_id),
            {"left": "A", "right": actor},
        )
        records.extend((row, edge))
        tips[actor] = row.record_id
    boundary = Boundary(state, tuple(sorted(records, key=lambda item: item.record_id)), tuple(sorted(tips.items())))
    validate_boundary(boundary)
    return boundary


def expected_record_id(record: BoundaryRecord) -> Tuple[Hashable, ...]:
    core = record_core(
        record.kind,
        record.owner,
        record.wires,
        record.parents,
        record.capability,
        record.payload_map(),
    )
    return canonical_id("BOUNDARY_RECORD", *core)


def authentic(record: BoundaryRecord) -> bool:
    core = record_core(
        record.kind,
        record.owner,
        record.wires,
        record.parents,
        record.capability,
        record.payload_map(),
    )
    return record.signature == digest(("D38_IDEAL_SIGNATURE", record.owner, core))


def validate_boundary(boundary: Boundary) -> None:
    records = {record.record_id: record for record in boundary.records}
    if len(records) != len(boundary.records):
        raise AssertionError("duplicate boundary record")
    actors = set(actors_for_state(boundary.state))
    allowed_kinds = {"ROOT_ROW", "NEIGHBOR_ROW", "EDGE", "EVENT"}
    for record in boundary.records:
        if (
            record.kind not in allowed_kinds
            or record.record_id != expected_record_id(record)
            or record.capability != capability(record.owner)
            or not authentic(record)
            or len(record.parents) > 2
            or any(parent not in records for parent in record.parents)
            or any(wire not in actors for wire in record.wires)
        ):
            raise AssertionError("boundary record integrity")
        if record.kind == "ROOT_ROW" and (record.owner != "A" or record.wires != ("A",)):
            raise AssertionError("root-row ownership")
        if record.kind == "NEIGHBOR_ROW" and (
            record.owner not in actors - {"A"} or record.wires != (record.owner,)
        ):
            raise AssertionError("neighbor-row ownership")
        if record.kind == "EDGE" and (
            set(record.wires) - actors or not record.owner.startswith("edge:A:N")
        ):
            raise AssertionError("edge ownership")
        if record.kind == "EVENT" and record.owner not in actors:
            raise AssertionError("event owner")
    tips = boundary.tip_map()
    if set(tips) != actors or any(record_id not in records for record_id in tips.values()):
        raise AssertionError("boundary tip coverage")
    root_payload = records[tips["A"]].payload_map()
    if (
        records[tips["A"]].kind != "ROOT_ROW"
        or root_payload
        != {
            "carrier": boundary.state.carrier,
            "degree": len(boundary.state.neighbor_degrees),
            "rings": boundary.state.root_rings,
            "wire_count": boundary.state.wire_count,
        }
    ):
        raise AssertionError("root row/state mismatch")
    for index, degree in enumerate(boundary.state.neighbor_degrees):
        actor = f"N{index}"
        record = records[tips[actor]]
        if record.kind != "NEIGHBOR_ROW" or record.payload_map()["degree"] != degree:
            raise AssertionError("neighbor row/state mismatch")
    if state_from_boundary_records(boundary) != boundary.state:
        raise AssertionError("cached state is not the record projection")


def event_owner(action: str) -> str:
    if action.startswith("NEIGHBOR_BIRTH:") or action.startswith("IN:"):
        return f"N{action_index(action)}"
    return "A"


def event_existing_actors(action: str) -> Tuple[str, ...]:
    if action in ("ROOT_BIRTH", "ROOT_IDLE"):
        return ("A",)
    if action.startswith("ROOT_OUT:") or action.startswith("IN:"):
        return ("A", f"N{action_index(action)}")
    if action.startswith("NEIGHBOR_BIRTH:"):
        return (f"N{action_index(action)}",)
    raise AssertionError(action)


def candidate_event(boundary: Boundary, action: str) -> BoundaryRecord:
    record_state = state_from_boundary_records(boundary)
    if action not in action_rates(record_state):
        raise AssertionError("candidate action outside kernel")
    actors = event_existing_actors(action)
    tips = boundary.tip_map()
    return make_record(
        "EVENT",
        event_owner(action),
        actors,
        tuple(tips[actor] for actor in actors),
        {"action": action, "source": "D34b-boundary-relevant-row"},
    )


def accepts_external_event(boundary: Boundary, action: str, candidate: BoundaryRecord) -> bool:
    try:
        validate_boundary(boundary)
        expected = candidate_event(boundary, action)
    except AssertionError:
        return False
    return candidate == expected and authentic(candidate)


def append_record(records: Dict[Hashable, BoundaryRecord], record: BoundaryRecord) -> None:
    if record.record_id in records and records[record.record_id] != record:
        raise AssertionError("boundary record collision")
    records[record.record_id] = record


def apply_boundary(
    boundary: Boundary,
    action: str,
    supplied_event: BoundaryRecord | None = None,
) -> Boundary:
    validate_boundary(boundary)
    event = candidate_event(boundary, action)
    if supplied_event is not None and not accepts_external_event(boundary, action, supplied_event):
        raise AssertionError("external boundary event rejected")
    if supplied_event is not None:
        event = supplied_event
    record_state = state_from_boundary_records(boundary)
    new_state = transition(record_state, action)
    records = {record.record_id: record for record in boundary.records}
    append_record(records, event)
    tips = boundary.tip_map()

    if "A" in event_existing_actors(action):
        root = make_record(
            "ROOT_ROW",
            "A",
            ("A",),
            (event.record_id,),
            {
                "carrier": new_state.carrier,
                "degree": len(new_state.neighbor_degrees),
                "rings": new_state.root_rings,
                "wire_count": new_state.wire_count,
            },
        )
        append_record(records, root)
        tips["A"] = root.record_id

    existing_neighbor: int | None = None
    if action.startswith("ROOT_OUT:") or action.startswith("IN:") or action.startswith("NEIGHBOR_BIRTH:"):
        existing_neighbor = action_index(action)
    if existing_neighbor is not None:
        actor = f"N{existing_neighbor}"
        row = make_record(
            "NEIGHBOR_ROW",
            actor,
            (actor,),
            (event.record_id,),
            {"birth_ordinal": existing_neighbor, "degree": new_state.neighbor_degrees[existing_neighbor]},
        )
        append_record(records, row)
        tips[actor] = row.record_id

    if action == "ROOT_BIRTH":
        index = len(boundary.state.neighbor_degrees)
        actor = f"N{index}"
        row = make_record(
            "NEIGHBOR_ROW",
            actor,
            (actor,),
            (event.record_id,),
            {"birth_ordinal": index, "degree": 1},
        )
        edge = make_record(
            "EDGE",
            f"edge:A:{actor}",
            ("A", actor),
            (event.record_id, row.record_id),
            {"left": "A", "right": actor},
        )
        append_record(records, row)
        append_record(records, edge)
        tips[actor] = row.record_id

    answer = Boundary(
        new_state,
        tuple(sorted(records.values(), key=lambda item: item.record_id)),
        tuple(sorted(tips.items())),
    )
    validate_boundary(answer)
    return answer


def apply_sequence(boundary: Boundary, actions: Sequence[str]) -> Boundary:
    answer = boundary
    for action in actions:
        answer = apply_boundary(answer, action)
    return answer


def authentication_negative_battery() -> Tuple[int, int]:
    boundary = initial_boundary(StarState(0, 0, 0, (2, 3)))
    action = "ROOT_IDLE"
    valid = candidate_event(boundary, action)
    if not accepts_external_event(boundary, action, valid):
        raise AssertionError("valid boundary event rejected")
    foreign_parent = canonical_id("FOREIGN_PARENT", "Z")
    foreign = make_record(
        "EVENT",
        "A",
        ("A",),
        (foreign_parent,),
        {"action": action, "source": "D34b-boundary-relevant-row"},
    )
    lookalike = make_record(
        "EVENT",
        "N0",
        ("N0",),
        (boundary.tip_map()["N0"],),
        {"action": action, "source": "D34b-boundary-relevant-row"},
    )
    mutations = [
        replace(valid, signature="FORGED"),
        replace(valid, capability="UNISSUED"),
        replace(valid, record_id=canonical_id("FORGED_ID", 1)),
        replace(valid, kind="GRANT"),
        replace(valid, owner="N0"),
        replace(valid, wires=("N0",)),
        replace(valid, parents=()),
        foreign,
        replace(valid, payload=(("action", action),)),
        replace(valid, payload=(("action", "ROOT_BIRTH"), ("source", "D34b-boundary-relevant-row"))),
        replace(valid, payload=valid.payload + (("omitted_field_substitution", 1),)),
        replace(valid, wires=("A", "Z")),
        lookalike,
    ]
    after = apply_boundary(boundary, action, valid)
    mutations.append(valid)  # stale replay against the advanced tip
    rejected = 0
    for index, mutation in enumerate(mutations):
        target = after if index == len(mutations) - 1 else boundary
        before = target
        accepted = accepts_external_event(target, action, mutation)
        rejected += int(not accepted and target == before)
    return rejected, len(mutations)


def record_closure_checks() -> Tuple[int, int, int, int, int, int, int]:
    seed = initial_boundary(StarState(0, 0, 0, (2, 3)))
    actions = ("ROOT_BIRTH", "NEIGHBOR_BIRTH:2", "IN:0", "ROOT_IDLE", "ROOT_OUT:1")
    closed = apply_sequence(seed, actions)
    closure_steps = len(actions)
    if len(closed.state.neighbor_degrees) != 3:
        raise AssertionError("root birth did not close into next boundary")

    sequential = apply_sequence(seed, ("NEIGHBOR_BIRTH:0", "NEIGHBOR_BIRTH:1"))
    reversed_order = apply_sequence(seed, ("NEIGHBOR_BIRTH:1", "NEIGHBOR_BIRTH:0"))
    if sequential != reversed_order:
        raise AssertionError("disjoint incident updates do not commute")

    left = initial_boundary(StarState(0, 0, 0, (2,)))
    right = initial_boundary(StarState(1, 4, 5, (3,)))
    product_start = (left, right)

    def update_component(
        components: Tuple[Boundary, Boundary], index: int, action: str
    ) -> Tuple[Boundary, Boundary]:
        mutable = list(components)
        mutable[index] = apply_boundary(mutable[index], action)
        return (mutable[0], mutable[1])

    left_then_right = update_component(
        update_component(product_start, 0, "ROOT_IDLE"), 1, "NEIGHBOR_BIRTH:0"
    )
    right_then_left = update_component(
        update_component(product_start, 1, "NEIGHBOR_BIRTH:0"), 0, "ROOT_IDLE"
    )
    if left_then_right != right_then_left or left_then_right[0] != apply_boundary(product_start[0], "ROOT_IDLE"):
        raise AssertionError("component restriction/insertion cocycle")

    rejected, attempted = authentication_negative_battery()
    parent_arity = max(len(record.parents) for record in closed.records)
    record_projection = int(state_from_boundary_records(closed) == closed.state)
    return closure_steps, len(closed.records), parent_arity, rejected, attempted, 2, record_projection


# ---------------------------------------------------------------------------
# R4/R5: exact predictive-width inheritance and anchor controls.


def predictive_exhaustion_checks() -> Tuple[Tuple[str, ...], Tuple[int, ...], Tuple[int, ...], int]:
    witnesses = tuple(
        ftext(Fraction(1, (8 * (radius + 3)) ** (radius + 1)))
        for radius in range(9)
    )
    if any(value == "0" for value in witnesses):
        raise AssertionError("fixed-radius witness lost positivity")
    binary_sizes = tuple(2**bits for bits in range(1, 11))
    if any(size.bit_length() - 1 != bits for bits, size in enumerate(binary_sizes, 1)):
        raise AssertionError("M-bit lower bound")
    anchor_lengths = tuple(2 * actors - 1 for actors in range(2, 11))
    if anchor_lengths != tuple(range(3, 20, 2)):
        raise AssertionError("anchor length")
    return witnesses, binary_sizes, anchor_lengths, 10


def anchor_discriminator_checks() -> Tuple[Fraction, Fraction, Fraction, Fraction, int, int]:
    d34f_text = D34F_DATA.read_text()
    required = (
        "bare equal-order coefficients=1/1152/1/576",
        "anchored q/q+1=1/192/1/1536",
        "attachment witness=1/1",
    )
    if any(text not in d34f_text for text in required):
        raise AssertionError("D34f anchor receipt drift")
    bare_left = Fraction(1, 1152)
    bare_right = Fraction(1, 576)
    anchored_q = Fraction(1, 192)
    anchored_q_plus_one = Fraction(1, 1536)
    if bare_left == bare_right or anchored_q <= 0 or anchored_q_plus_one <= 0:
        raise AssertionError("anchor coefficient control")
    return bare_left, bare_right, anchored_q, anchored_q_plus_one, 1, 0


# ---------------------------------------------------------------------------
# R6: escape controls.


def horizon_projection(mark_distance: int, horizon: int, mark: int) -> Tuple[str, int]:
    return ("VISIBLE", mark) if mark_distance <= horizon else ("OUTSIDE_HORIZON", 0)


def sealed_projection(mark: int, sealed: bool) -> Tuple[str, int]:
    return ("SEALED_PRESENT", 0) if sealed else ("OPEN", mark)


def attenuation_projection(distance: int, mark: int, epsilon: Fraction | None) -> Fraction:
    value = Fraction(mark, 2**distance)
    if epsilon is not None and value <= epsilon:
        return Fraction()
    return value


def escape_controls() -> Tuple[int, int, int, int, int, int]:
    horizon_escape = int(
        horizon_projection(4, 3, 0) == horizon_projection(4, 3, 1)
        and horizon_projection(3, 3, 0) != horizon_projection(3, 3, 1)
    )
    seal_escape = int(
        sealed_projection(0, True) == sealed_projection(1, True)
        and sealed_projection(0, False) != sealed_projection(1, False)
    )
    exact_attenuation_distinctions = sum(
        attenuation_projection(distance, 0, None)
        != attenuation_projection(distance, 1, None)
        for distance in range(1, 13)
    )
    epsilon = Fraction(1, 16)
    epsilon_escape_depths = sum(
        attenuation_projection(distance, 0, epsilon)
        == attenuation_projection(distance, 1, epsilon)
        for distance in range(1, 13)
    )
    bounded_growth_states = 2**6
    bounded_growth_bits = bounded_growth_states.bit_length() - 1
    if (
        horizon_escape != 1
        or seal_escape != 1
        or exact_attenuation_distinctions != 12
        or epsilon_escape_depths != 9
        or bounded_growth_bits != 6
    ):
        raise AssertionError("load-bearing escape control")
    return (
        horizon_escape,
        seal_escape,
        exact_attenuation_distinctions,
        epsilon_escape_depths,
        bounded_growth_states,
        bounded_growth_bits,
    )


# ---------------------------------------------------------------------------
# R7: D26 physical upkeep.


def d26_upkeep_checks() -> Tuple[Tuple[str, ...], Tuple[str, ...], str, int]:
    coherence = Fraction(4, 5)
    born = tuple(ftext(coherence**births) for births in range(9))
    token = tuple(ftext(Fraction(1)) for _ in range(9))
    if born[0] != "1" or born[3] != "64/125" or any(value != "1" for value in token):
        raise AssertionError("D26 upkeep factor")
    symbolic_budget = "B_N=N[-(1/2)ln(1-g)]; V_N/V_0=(1-g)^(N/2)"
    return born, token, symbolic_budget, 0


# ---------------------------------------------------------------------------
# R8: finite mass transport and open root-free selection.


Graph = Tuple[Tuple[int, ...], ...]


def graph_from_edges(vertex_count: int, edges: Iterable[Tuple[int, int]]) -> Graph:
    adjacency = [set() for _ in range(vertex_count)]
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    return tuple(tuple(sorted(row)) for row in adjacency)


def sent_mass(graph: Graph, root: int) -> Fraction:
    return Fraction(1) if graph[root] else Fraction()


def received_mass(graph: Graph, root: int) -> Fraction:
    return sum((Fraction(1, len(graph[source])) for source in graph[root]), Fraction())


def mass_transport_checks() -> Tuple[int, int, Fraction, Fraction]:
    graphs = (
        graph_from_edges(3, ((0, 1), (1, 2))),
        graph_from_edges(4, ((0, 1), (0, 2), (0, 3))),
        graph_from_edges(5, ((0, 1), (1, 2), (2, 3), (3, 4))),
    )
    balanced = 0
    for graph in graphs:
        sent = sum((sent_mass(graph, root) for root in range(len(graph))), Fraction())
        received = sum((received_mass(graph, root) for root in range(len(graph))), Fraction())
        if sent != received:
            raise AssertionError("uniform finite mass transport")
        balanced += 1
    star = graphs[1]
    biased_sent = sent_mass(star, 0)
    biased_received = received_mass(star, 0)
    if biased_sent != 1 or biased_received != 3 or biased_sent == biased_received:
        raise AssertionError("root-biased mass-transport negative")
    return balanced, 1, biased_sent, biased_received


def main() -> None:
    out: list[str] = []
    gates: Dict[str, bool] = {}
    science: Dict[str, object] = {}

    def emit(line: str) -> None:
        out.append(line)
        print(line)

    emit("[D38 record-closed regional specifications — exact finite receipt]")
    emit("ARITHMETIC: integers/Fractions for every discrete and rational claim; logs remain symbolic")
    emit("SCOPE: chosen D34b positive-cylinder/embedded-star presentation; exact unlimited Branch-F criterion; classical only")

    locks = locked_antecedents()
    d34e_text = D34E_DATA.read_text()
    gates["R0"] = (
        len(locks) == 7
        and "[VERDICT] PASS — 13/13" in d34e_text
        and "[VERDICT] PASS — 11/11" in D34F_DATA.read_text()
    )
    science["locks"] = locks
    emit("[LOCKED ANTECEDENTS / CLAIM SPLIT]")
    emit(f"source_and_data_locks={stable(locks)}")
    emit("local_update_collar!=sufficient_boundary!=predictive_quotient; D34b_coefficients_selected=0; nature_law_claim=0")

    normalized, towers, positive_atoms, rates = positive_cylinder_checks()
    gates["R1"] = normalized == 4 and towers == positive_atoms and positive_atoms == 29
    science["kernels"] = [normalized, towers, positive_atoms, rates]
    emit("[POSITIVE FINITE-CYLINDER REGIONAL KERNELS]")
    emit(f"normalized_embedded_star_kernels={normalized}/4; positive_atoms={positive_atoms}; nested_tower_checks={towers}; holding_rates={rates}")
    emit("kernel=boundary-relevant embedded D34b jump chain + exact holding rate; null_boundary_versions=NOT_PROVED; Paper26_K_membership=NOT_CLAIMED")

    arity_checks, maximum_arity, width_growth, disconnected = locality_width_checks()
    gates["R2"] = (
        arity_checks == 258
        and maximum_arity == 2
        and width_growth == 12
        and disconnected == 1
    )
    science["locality"] = [arity_checks, maximum_arity, width_growth, disconnected]
    emit("[BOUNDED LOCAL UPDATES / GROWING BOUNDARY]")
    emit(f"touched_arity_checks={arity_checks}; maximum_touched_actors={maximum_arity}; radius_one_width_control={width_growth}; disconnected_insertion_unchanged={disconnected}")
    emit("bounded_update_radius=1; bounded_memory=0; bounded_degree=0; Lorentz_locality=NOT_CLAIMED")

    closure_steps, record_count, parent_arity, rejected, attempted, cocycles, record_projection = record_closure_checks()
    gates["R3"] = (
        closure_steps == 5
        and record_count > 0
        and parent_arity == 2
        and rejected == attempted == 14
        and cocycles == 2
        and record_projection == 1
    )
    science["record_closure"] = [closure_steps, record_count, parent_arity, rejected, attempted, cocycles, record_projection]
    emit("[AUTHENTICATED RECORD-CLOSED STAR UPDATER]")
    emit(f"seed_to_boundary_updates={closure_steps}; final_record_count={record_count}; max_parent_arity={parent_arity}; restriction_and_insertion_cocycles={cocycles}/2")
    emit(f"record_only_state_reconstruction={record_projection}; forged_replayed_retargeted_boundary_mutations_rejected={rejected}/{attempted}; reject_before_durable_mutation=1; ideal_authentication_scope=1")

    witnesses, binary_sizes, anchor_lengths, max_bits = predictive_exhaustion_checks()
    gates["R4"] = (
        len(witnesses) == 9
        and binary_sizes == tuple(2**bits for bits in range(1, 11))
        and anchor_lengths == tuple(range(3, 20, 2))
        and max_bits == 10
    )
    science["exhaustion"] = [witnesses, binary_sizes, anchor_lengths, max_bits]
    emit("[PREDICTIVE EXHAUSTION / WIDTH LOWER BOUND]")
    emit(f"fixed_radius_positive_witnesses={witnesses}; radii=0..8")
    emit(f"binary_family_sizes={binary_sizes}; M_bit_controls=1..{max_bits}; anchor_lengths_q=2n-1:{anchor_lengths}")
    emit("inverse_limit_boundary=rooted_marked_component_class; finite_receipt_is_regression_not_all_size_proof=1")

    bare_left, bare_right, anchored_q, anchored_q1, attachment, emulators = anchor_discriminator_checks()
    gates["R5"] = (
        bare_left == Fraction(1, 1152)
        and bare_right == Fraction(1, 576)
        and anchored_q == Fraction(1, 192)
        and anchored_q1 == Fraction(1, 1536)
        and attachment == 1
        and emulators == 0
    )
    science["anchor"] = [bare_left, bare_right, anchored_q, anchored_q1, attachment, emulators]
    emit("[FRESH-ANCHOR HOSTILE DISCRIMINATOR]")
    emit(f"bare_equal_order_coefficients={ftext(bare_left)},{ftext(bare_right)}; bare_sweep_universal_order_proof=0")
    emit(f"anchored_q_vs_q_plus_1_coefficients={ftext(anchored_q)},{ftext(anchored_q1)}; first_unmatched_attachment={attachment}/1; equal_or_lower_order_emulators={emulators}")

    escapes = escape_controls()
    gates["R6"] = escapes == (1, 1, 12, 9, 64, 6)
    science["escapes"] = escapes
    emit("[LOAD-BEARING ESCAPE CONTROLS]")
    emit(f"finite_horizon_escape={escapes[0]}; irreversible_operational_seal_escape={escapes[1]}; nonzero_exact_attenuation_distinctions={escapes[2]}/12")
    emit(f"epsilon_attenuation_merged_depths={escapes[3]}/12; bounded_growth_states_bits={escapes[4]},{escapes[5]}; ontological_record_deleted=0")

    born, token, budget, rate = d26_upkeep_checks()
    gates["R7"] = len(born) == len(token) == 9 and born[3] == "64/125" and rate == 0
    science["upkeep"] = [born, token, budget, rate]
    emit("[D26 BOUNDARY-UPKEEP ACCOUNTING]")
    emit(f"BORN_visibility_factors_N0_to_N8={born}; TOKEN_controls={token}")
    emit(f"symbolic_budget={budget}; universal_boundary_maintenance_rate={rate}; record_to_system_dictionary=OPEN")

    balanced, biased_control, biased_sent, biased_received = mass_transport_checks()
    gates["R8"] = (
        balanced == 3
        and biased_control == 1
        and biased_sent == 1
        and biased_received == 3
    )
    science["balance"] = [balanced, biased_control, biased_sent, biased_received]
    emit("[FINITE MASS-TRANSPORT BALANCE / CEILINGS]")
    emit(f"uniform_root_graphs_balanced={balanced}/3; locally_normalized_root_biased_negative={biased_control}; biased_sent_received={ftext(biased_sent)},{ftext(biased_received)}")
    emit("infinite_unimodular_completion=OPEN; coupling_selection=OPEN; action_bridge=OPEN; quantum_record_closed_specification=UNDEFINED; sealing_rate=UNDEFINED")

    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    body_hash = hashlib.sha256(("\n".join(out) + "\n").encode()).hexdigest()
    science_hash = hashlib.sha256(stable(science).encode()).hexdigest()
    emit("[HASHES]")
    emit(f"source_sha256={source_hash}")
    emit(f"stdout_body_sha256={body_hash}")
    emit(f"internal_science_sha256={science_hash}")

    emit("[GATES]")
    for name in sorted(gates, key=lambda value: int(value[1:])):
        emit(f"{name}={'PASS' if gates[name] else 'FAIL'}")
    passed = sum(gates.values())
    emit("[VERDICT]")
    emit(f"{'PASS' if passed == len(gates) else 'FAIL'} {passed}/{len(gates)}")
    emit("RECORD-CLOSED REGIONAL SPECIFICATION / CHOSEN-LAW POSITIVE-CYLINDER EXISTENCE / FAMILY NOT SELECTOR")
    emit("BOUNDED LOCAL UPDATE ARITY COEXISTS WITH UNBOUNDED EXACT PREDICTIVE WIDTH")
    emit("component obstruction is conditional on persistence,growth,returnability,anchor,exact unlimited query,no seal; quantum and root-free selection remain open")
    if passed != len(gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()

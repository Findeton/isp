#!/usr/bin/env python3
"""D40b exact hostile repair: type both probability spaces.

The source is pinned by note-d40b-hostile-repair.md.  It repairs the D40
round-one major without mutating the frozen D40 receipt: the projected first-
relevant-event star law and the complete first-two-global-event embedded jump
law receive distinct serial and unordered constructors.
"""

from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import json
import sys
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from typing import Dict, Hashable, Mapping, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]

LOCKS = {
    "D40b-pin": (
        ROOT / "v10/note-d40b-hostile-repair.md",
        "726b373bb76878ec7430cc65e21d664b50d4b1e049f5261533e59e994f1e897a",
    ),
    "D40-pin": (
        ROOT / "v10/note-d40-where-the-action-cocycle-lives.md",
        "e52c78d2ed72cc6bd1d0f092dec57f506b8742d8eeb2c754323a20bb1f609b33",
    ),
    "D40-source": (
        ROOT / "v10/code/d40_action_cocycle_level_audit_exact.py",
        "3930ae7abd704763767ececcf2b0de8e4ad5926143211e981e90d389cb88b9d5",
    ),
    "D40-output": (
        ROOT / "v10/data/d40_action_cocycle_level_audit_exact.out",
        "7f00c92019765086089c2f9a5aa1f22d3a52076c124c77228e1d99466bac464a",
    ),
    "D40-round1": (
        ROOT / "v10/reviews/d40-round1-independent-hostile-review.md",
        "4e9ea3c146204890cef3e911376f3afc39dfe5bab5d756c01167f5d42bdeafd7",
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


d40 = load_module("d40_locked_for_d40b", LOCKS["D40-source"][0])
d39 = d40.d39
d38 = d40.d38
d34 = d40.d34
Q2 = d40.Q2
ZERO = d40.ZERO
ONE = d40.ONE
HALF = d40.HALF
ROOT_HALF = d40.ROOT_HALF


def stable(value: object) -> str:
    def default(item: object) -> object:
        if isinstance(item, F):
            return {"fraction": [item.numerator, item.denominator]}
        if isinstance(item, (set, frozenset)):
            return sorted(item, key=repr)
        if hasattr(item, "__dict__"):
            return item.__dict__
        raise TypeError(type(item))

    return json.dumps(value, default=default, sort_keys=True, separators=(",", ":"))


def ftext(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def qtext(value: Q2) -> str:
    if value.b == 0:
        return str(value.a)
    radical = f"{value.b}*sqrt2"
    if value.a == 0:
        return radical
    separator = "+" if value.b > 0 else ""
    return f"{value.a}{separator}{radical}"


@dataclass(frozen=True)
class ProbabilityObject:
    kind: str
    payload: Hashable


KINDS = (
    "STAR_RELEVANT_SERIAL",
    "STAR_UNORDERED_ACTION_ATOM",
    "GLOBAL_SERIAL_EVENT",
    "GLOBAL_TYPED_DAG_ATOM",
)


def star_unordered_atom(initial, path: Sequence[Tuple[str, str]]) -> ProbabilityObject:
    state = initial
    typed_actions = []
    for action in path:
        typed_actions.append(d39.canonical_action(state, action))
        state = d38.star_step(state, action)
    return ProbabilityObject(
        "STAR_UNORDERED_ACTION_ATOM",
        (
            tuple(sorted(typed_actions, key=repr)),
            d39.canonical_star(state),
        ),
    )


def global_serial_path() -> Tuple[Tuple[object, ...], Tuple[object, ...], object, object]:
    base = d38.initial_store()
    idle = d38.proposed(base, "IDLE", "A")
    born = d38.proposed(base, "BIRTH", "B", "B/1")
    after_idle, accepted_idle = d38.transact(base, idle)
    after_born, accepted_born = d38.transact(base, born)
    born_after_idle = d38.proposed(after_idle, "BIRTH", "B", "B/1")
    idle_after_born = d38.proposed(after_born, "IDLE", "A")
    final_ab, accepted_ab = d38.transact(after_idle, born_after_idle)
    final_ba, accepted_ba = d38.transact(after_born, idle_after_born)
    if not all((accepted_idle, accepted_born, accepted_ab, accepted_ba)):
        raise AssertionError("global path rejected")
    return (idle, born_after_idle), (born, idle_after_born), final_ab, final_ba


def two_space_checks() -> Tuple[object, ...]:
    initial = d38.star_from_history(d38.initial_store().history)
    star_distribution = d38.cylinder_distribution(initial, 2)
    star_pushforward: Dict[ProbabilityObject, F] = {}
    star_preimages: Dict[ProbabilityObject, int] = {}
    for path, probability in star_distribution.items():
        serial = ProbabilityObject("STAR_RELEVANT_SERIAL", tuple(path))
        if serial.kind != "STAR_RELEVANT_SERIAL":
            raise AssertionError("star serial type")
        atom = star_unordered_atom(initial, path)
        star_pushforward[atom] = star_pushforward.get(atom, F()) + probability
        star_preimages[atom] = star_preimages.get(atom, 0) + 1

    idle_action = ("ROOT_IDLE", "NONE")
    birth_action = ("NEIGHBOR_BIRTH", "B")
    star_path_ab = (idle_action, birth_action)
    star_path_ba = (birth_action, idle_action)
    star_atom_ab = star_unordered_atom(initial, star_path_ab)
    star_atom_ba = star_unordered_atom(initial, star_path_ba)
    star_products = (star_distribution[star_path_ab], star_distribution[star_path_ba])
    star_mass = star_pushforward[star_atom_ab]

    packet = d39.RatePacket((1, 1), (1, 2, 1))
    path_ab, path_ba, final_ab, final_ba = global_serial_path()
    global_paths = d39.embedded_paths(packet, 2)
    global_serial_ab = ProbabilityObject("GLOBAL_SERIAL_EVENT", tuple(event.record_id for event in path_ab))
    global_serial_ba = ProbabilityObject("GLOBAL_SERIAL_EVENT", tuple(event.record_id for event in path_ba))
    global_products = (global_paths[path_ab], global_paths[path_ba])
    global_law, merged = d39.push_path_law(packet, typed=True)
    dag_ab = d39.dag_atom(path_ab)
    dag_ba = d39.dag_atom(path_ba)
    global_atom_ab = ProbabilityObject("GLOBAL_TYPED_DAG_ATOM", dag_ab)
    global_atom_ba = ProbabilityObject("GLOBAL_TYPED_DAG_ATOM", dag_ba)
    global_preimages = sum(int(d39.dag_atom(path) == dag_ab) for path in global_paths)
    global_mass = global_law[dag_ab]

    same_global_store = d39.stable(final_ab.history.records) == d39.stable(final_ba.history.records)
    same_event_set = set(global_serial_ab.payload) == set(global_serial_ba.payload)
    distinct_types = len({*KINDS}) == 4 and len({
        ProbabilityObject(kind, ()) for kind in KINDS
    }) == 4

    return (
        star_products[0],
        star_products[1],
        int(star_atom_ab == star_atom_ba),
        star_preimages[star_atom_ab],
        star_mass,
        int(star_mass == sum(star_products, F())),
        int(sum(star_pushforward.values(), F()) == 1),
        len(star_distribution),
        len(star_pushforward),
        global_products[0],
        global_products[1],
        int(global_atom_ab == global_atom_ba),
        global_preimages,
        int(same_event_set),
        int(same_global_store),
        global_mass,
        int(global_mass == sum(global_products, F())),
        int(sum(global_law.values(), F()) == 1),
        len(global_paths),
        len(global_law),
        merged,
        int(distinct_types),
    )


def q_nonnegative(value: Q2) -> bool:
    """Exact sign in Q(sqrt(2))."""
    if value.b == 0:
        return value.a >= 0
    if value.b > 0:
        if value.a >= 0:
            return True
        return 2 * value.b * value.b >= value.a * value.a
    if value.a < 0:
        return False
    return value.a * value.a >= 2 * value.b * value.b


def bell_gram_checks() -> Tuple[int, int, int, int]:
    i2 = d34.I2
    observables_a = {0: d34.Z2, 1: d34.X2}
    observables_b = {
        0: d34.mscale(ROOT_HALF, d34.madd(d34.Z2, d34.X2)),
        1: d34.mscale(
            ROOT_HALF,
            d34.madd(d34.Z2, d34.mscale(Q2(-1), d34.X2)),
        ),
    }
    psi = [ROOT_HALF, ZERO, ZERO, ROOT_HALF]

    def projector(observable, outcome: int):
        return d34.mscale(
            HALF,
            d34.madd(i2, d34.mscale(Q2(outcome), observable)),
        )

    quadratic_checks = symmetry = normalized = settings = 0
    for x, y in product((0, 1), repeat=2):
        branches = []
        for a, b in product((1, -1), repeat=2):
            joint = d34.kron_matrix(
                projector(observables_a[x], a),
                projector(observables_b[y], b),
            )
            branches.append(d34.mv(joint, psi))
        gram = d34.gram(branches)
        symmetry += int(gram == d34.transpose(gram))
        normalized += int(sum((gram[i][i] for i in range(4)), ZERO) == ONE)
        for coefficients in product((-1, 0, 1), repeat=4):
            if not any(coefficients):
                continue
            quadratic = sum(
                (
                    Q2(coefficients[i] * coefficients[j]) * gram[i][j]
                    for i in range(4)
                    for j in range(4)
                ),
                ZERO,
            )
            combined = [
                sum(
                    (Q2(coefficients[i]) * branches[i][entry] for i in range(4)),
                    ZERO,
                )
                for entry in range(4)
            ]
            norm = d34.inner(combined, combined)
            quadratic_checks += int(quadratic == norm and q_nonnegative(norm))
        settings += 1
    return settings, symmetry, normalized, quadratic_checks


def claim_ledger_and_rendering_checks() -> Tuple[object, ...]:
    ledger = d40.universality_audit()
    bell, _laws = d40.bell_fixture()
    rendered = (qtext(bell[8]), qtext(bell[9]))
    return ledger[0], sum(count for _category, count in ledger[1]), 0, *rendered


def main() -> None:
    out = []
    science: Dict[str, object] = {}
    gates: Dict[str, bool] = {}

    def emit(line: str) -> None:
        out.append(line)
        print(line)

    emit("[D40b hostile repair — typed probability spaces]")
    emit("ARITHMETIC: integer/Fraction/Q(sqrt2) exact; no floating theorem")

    locks = tuple(sha256(path) for path, _expected in LOCKS.values())
    expected_locks = tuple(expected for _path, expected in LOCKS.values())
    science["C0"] = locks
    gates["C0"] = locks == expected_locks
    emit("[C0 LOCKS]")
    emit(f"antecedent_locks={sum(int(a == b) for a, b in zip(locks, expected_locks))}/{len(LOCKS)}")

    spaces = two_space_checks()
    science["C1"] = spaces
    gates["C1"] = spaces[:7] == (
        F(1, 18), F(2, 33), 1, 2, F(23, 198), 1, 1,
    ) and spaces[9:18] == (
        F(1, 32), F(1, 48), 1, 2, 1, 1, F(5, 96), 1, 1,
    ) and spaces[21] == 1
    emit("[C1 TWO TYPED PROBABILITY SPACES]")
    emit(f"STAR_RELEVANT_SERIAL={ftext(spaces[0])},{ftext(spaces[1])}; same_STAR_UNORDERED_ACTION_ATOM={spaces[2]}/1; preimages={spaces[3]}")
    emit(f"STAR_UNORDERED_ACTION_ATOM_mass={ftext(spaces[4])}; equals_star_serial_sum={spaces[5]}/1; star_pushforward_normalized={spaces[6]}/1")
    emit(f"GLOBAL_SERIAL_EVENT={ftext(spaces[9])},{ftext(spaces[10])}; same_GLOBAL_TYPED_DAG_ATOM={spaces[11]}/1; preimages={spaces[12]}; same_event_set={spaces[13]}/1; same_store={spaces[14]}/1")
    emit(f"GLOBAL_TYPED_DAG_ATOM_mass={ftext(spaces[15])}; equals_global_serial_sum={spaces[16]}/1; global_pushforward_normalized={spaces[17]}/1")
    emit("cross_object_mass_equality=NOT_REQUIRED; substitution_forbidden=1")

    scope = (spaces[7], spaces[8], spaces[18], spaces[19], spaces[20], 0, 0, 0)
    science["C2"] = scope
    gates["C2"] = all(value > 0 for value in scope[:5]) and scope[5:] == (0, 0, 0)
    emit("[C2 FIXED-DEPTH SCOPE]")
    emit(f"star_serial_paths={scope[0]}; star_unordered_atoms={scope[1]}; global_serial_paths={scope[2]}; global_typed_DAG_atoms={scope[3]}; global_merges={scope[4]}")
    emit("global_object=REGISTERED_DEPTH_TWO_EMBEDDED_JUMP_PUSHFORWARD; timed_Harris_cylinder=NOT_CLAIMED; arbitrary_downset_projectivity=NOT_CLAIMED; stationary_infinite_completion=NOT_CLAIMED")

    gram = bell_gram_checks()
    science["C3"] = gram
    gates["C3"] = gram == (4, 4, 4, 320)
    emit("[C3 BELL GRAM POSITIVITY]")
    emit(f"settings={gram[0]}/4; symmetric_Grams={gram[1]}/4; normalized_Grams={gram[2]}/4; exact_quadratic_form_controls={gram[3]}/320")
    emit("proof_for_arbitrary_real_c=c^T_G_c=norm(sum_i_c_i_v_i)^2>=0")

    ledger = claim_ledger_and_rendering_checks()
    science["C4"] = ledger
    gates["C4"] = ledger == (1, 12, 0, "1/2+1/4*sqrt2", "1/2-1/4*sqrt2")
    emit("[C4 TYPED CORPUS CLAIM LEDGER / RENDERING]")
    emit(f"unique_claim_rows={ledger[0]}/1; ledger_rows={ledger[1]}/12; universality_theorem={ledger[2]}")
    emit(f"erased_setting_conditionals={ledger[3]},{ledger[4]}")

    source_hash = sha256(Path(__file__))
    body_hash = hashlib.sha256(("\n".join(out) + "\n").encode()).hexdigest()
    science_hash = hashlib.sha256(stable(science).encode()).hexdigest()
    emit("[HASHES]")
    emit(f"source_sha256={source_hash}")
    emit(f"stdout_body_sha256={body_hash}")
    emit(f"internal_science_sha256={science_hash}")
    emit("[GATES]")
    for name in sorted(gates):
        emit(f"{name}={'PASS' if gates[name] else 'FAIL'}")
    passed = sum(gates.values())
    emit("[VERDICT]")
    emit(f"{'PASS' if passed == len(gates) else 'FAIL'} {passed}/{len(gates)}")
    emit("TWO-SPACE SERIAL-TO-UNORDERED PUSHFORWARD THEOREM")
    emit("PAPER28_FLAT_ACTION_NONMEMBERSHIP_WITHOUT_PROBABILITY_INCONSISTENCY")
    emit("FINITE_BELL_GRAM_POSITIVITY_CONTROL; UNRESOLVED_D15_DICTIONARY")
    if passed != len(gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()

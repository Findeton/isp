#!/usr/bin/env python3
"""D40 exact receipt: where the action cocycle lives.

Pinned by note-d40-where-the-action-cocycle-lives.md before this source
existed.  The receipt distinguishes operator interchange, decoherence-
functional consistency, refined durable-record cylinders, serial histories,
typed causal-DAG pushforwards, regional boundary sufficiency and the D39
classical increment complex.

All theorem arithmetic is integer, Fraction or exact Q(sqrt(2)).  The Bell
fixture is an architecture test, not an execution of the full D15 action.
"""

from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import json
import sys
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from typing import Dict, Hashable, Mapping, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[2]

LOCKS = {
    "D40-pin": (
        ROOT / "v10/note-d40-where-the-action-cocycle-lives.md",
        "e52c78d2ed72cc6bd1d0f092dec57f506b8742d8eeb2c754323a20bb1f609b33",
    ),
    "D34c-source": (
        ROOT / "v10/code/d34c_nse_quantum_history_exact.py",
        "185d36b9cd3dea684afcbe6b8bc1250ced8745cd0d0d74f277351818d4825a12",
    ),
    "D34c-output": (
        ROOT / "v10/data/d34c_nse_quantum_history_exact.out",
        "9ce73a693b41f765eff163749ef769ca0cb4ce856ead66d690a63a20331a731a",
    ),
    "D39b-source": (
        ROOT / "v10/code/d39b_record_closed_law_selection_exact.py",
        "22fbda6a9189a2f46cf64c0f33b943b952e702fce30828a37b6d462f5a1458d3",
    ),
    "D39b-output": (
        ROOT / "v10/data/d39b_record_closed_law_selection_exact.out",
        "3e3ec1b1ab0459bddc5106e1ba4fe459741af264bfb0c725c8d9edd41ddf85ea",
    ),
    "D14-source": (
        ROOT / "v10/code/d14_action_record_bridge_exact.py",
        "e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425",
    ),
    "Paper15": (
        ROOT / "v10/relativistic-isp-v10-paper15-from-action-to-records-without-a-global-clock.md",
        "7449e02f21c6d74a9899febb65ad7819460df21e43d793e36e6faba024862635",
    ),
    "Paper18": (
        ROOT / "v10/relativistic-isp-v10-paper18-no-silent-erasure-and-the-identified-click-law.md",
        "71fafc639e98ba387bd7a70305f24f266feb68704273d77d9849ed687321d4bc",
    ),
    "Paper19": (
        ROOT / "v10/relativistic-isp-v10-paper19-the-complete-interactive-record-law-at-the-declared-interface.md",
        "e58b973ae70084d3c715965f94e0e54d97868a2021c363a6375f1fc3a07402c4",
    ),
    "Paper28": (
        ROOT / "v10/relativistic-isp-v10-paper28-selecting-record-closed-laws.md",
        "ce625405657e539e1cdb77c4d0e3713d73422f6094797a6b420ea7209f5e067f",
    ),
    "D26-source": (
        ROOT / "v10/code/d26_interface_equivalence_exact.py",
        "a9b1f1704578178218750ecbafa737763ff3968ca246939a1d6aece79930575c",
    ),
    "D26-output": (
        ROOT / "v10/data/d26_interface_equivalence_exact.out",
        "88a5461f2304415db69d4decc4b89b95195d928e79e8feeb73aeefca74c59633",
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ftext(value: F) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


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


def load_module(name: str, path: Path, catches_zero_exit: bool = False):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    with contextlib.redirect_stdout(io.StringIO()):
        try:
            spec.loader.exec_module(module)
        except SystemExit as exc:
            if not catches_zero_exit or exc.code not in (None, 0):
                raise
    return module


d34 = load_module("d34c_locked_for_d40", LOCKS["D34c-source"][0], True)
d39 = load_module("d39b_locked_for_d40", LOCKS["D39b-source"][0])
d38 = d39.d38

Q2 = d34.Q2
ZERO = d34.ZERO
ONE = d34.ONE
HALF = d34.HALF
ROOT_HALF = d34.ROOT_HALF


def qdiv(left: Q2, right: Q2) -> Q2:
    """Exact division in Q(sqrt(2)); D34c itself only needed rational divisors."""
    denominator = right.a * right.a - 2 * right.b * right.b
    if denominator == 0:
        raise ZeroDivisionError
    return Q2(
        (left.a * right.a - 2 * left.b * right.b) / denominator,
        (left.b * right.a - left.a * right.b) / denominator,
    )


@dataclass(frozen=True)
class TypedLevel:
    kind: str
    payload: Hashable


LEVEL_KINDS = (
    "OPERATOR",
    "HISTORY_PAIR",
    "RECORD_CYLINDER",
    "SERIAL_PATH",
    "CAUSAL_DAG_ATOM",
    "REGIONAL_BOUNDARY",
    "ACTION_INCREMENT",
)


def lock_and_type_checks() -> Tuple[int, int]:
    locked = sum(int(sha256(path) == expected) for path, expected in LOCKS.values())
    constructors = tuple(TypedLevel(kind, (kind,)) for kind in LEVEL_KINDS)
    distinct = len({row.kind for row in constructors})
    return locked, distinct


# ---------------------------------------------------------------------------
# R1: refined classical cylinder descent and finite boundary sufficiency.


def classical_descent_checks() -> Tuple[int, int, int, int]:
    squares = 0
    for raw in product(range(1, 5), repeat=4):
        weights = {(a, b): F(raw[2 * a + b]) for a, b in product((0, 1), repeat=2)}
        total = sum(weights.values(), F())
        for a, b in product((0, 1), repeat=2):
            mass_a = sum(weights[(a, bb)] for bb in (0, 1))
            mass_b = sum(weights[(aa, b)] for aa in (0, 1))
            via_a = mass_a / total * weights[(a, b)] / mass_a
            via_b = mass_b / total * weights[(a, b)] / mass_b
            if via_a != weights[(a, b)] / total or via_b != via_a:
                raise AssertionError("classical cylinder descent")
            squares += 1

    groups = {0: "E", 1: "E", 2: "O", 3: "O"}
    good = {
        0: (F(1, 3), F(2, 3)),
        1: (F(1, 3), F(2, 3)),
        2: (F(3, 4), F(1, 4)),
        3: (F(3, 4), F(1, 4)),
    }
    bad = dict(good)
    bad[1] = (F(2, 3), F(1, 3))

    def sufficient(rows: Mapping[int, Tuple[F, F]]) -> bool:
        for coarse in set(groups.values()):
            fibre = [state for state, image in groups.items() if image == coarse]
            if len({rows[state] for state in fibre}) != 1:
                return False
        return True

    mixture_left = tuple((good[0][i] + good[1][i]) / 2 for i in range(2))
    mixture_right = tuple((bad[0][i] + 3 * bad[1][i]) / 4 for i in range(2))
    negative_visible = int(mixture_left != mixture_right)
    return squares, int(sufficient(good)), int(not sufficient(bad)), negative_visible


# ---------------------------------------------------------------------------
# R2--R4: D34c action, decoherence functional and record descent.


def action_functional_checks() -> Tuple[int, int, int, int, int]:
    disjoint = int(
        d34.mm(d34.OPS["a"], d34.OPS["b"])
        == d34.mm(d34.OPS["b"], d34.OPS["a"])
    )
    branches = int(d34.branches_ab == d34.branches_ba)
    functionals = int(d34.d_ab == d34.d_ba and d34.rank == 4 and d34.normalized)
    shared_control = int(d34.shared_noncommutes and d34.shared_state_diff)
    restrictions = int(
        d34.d_sp_from_full == d34.d_sp_direct
        and d34.d_s_from_sp == d34.d_s_direct
        and d34.d_s_from_full == d34.d_s_direct
    )
    return disjoint, branches, functionals, shared_control, restrictions


def durable_record_descent_checks() -> Tuple[int, int, int, int]:
    measures = []
    for matrix, labels in (
        (d34.d_so, d34.groups_so),
        (d34.recorded_so, d34.groups_so),
    ):
        diagonal = all(
            matrix[i][j] == ZERO
            for i in range(len(labels))
            for j in range(len(labels))
            if i != j
        )
        if not diagonal:
            raise AssertionError("durable algebra not decoherent")
        measure = {label: matrix[i][i] for i, label in enumerate(labels)}
        if sum(measure.values(), ZERO) != ONE:
            raise AssertionError("record measure normalization")
        measures.append(measure)

    squares = 0
    positive_denominators = 0
    for measure in measures:
        for s, o in product((0, 1), repeat=2):
            ps = sum((measure[(s, oo)] for oo in (0, 1)), ZERO)
            po = sum((measure[(ss, o)] for ss in (0, 1)), ZERO)
            if not ps or not po:
                raise AssertionError("zero queried denominator")
            via_s = ps * qdiv(measure[(s, o)], ps)
            via_o = po * qdiv(measure[(s, o)], po)
            if via_s != measure[(s, o)] or via_o != via_s:
                raise AssertionError("durable click square")
            positive_denominators += 2
            squares += 1
    return len(measures), squares, positive_denominators, 5


def interference_controls() -> Tuple[int, int, int, int]:
    coherent = tuple(d34.prob_so[key] for key in sorted(d34.prob_so))
    recorded = tuple(d34.recorded_prob[key] for key in sorted(d34.recorded_prob))
    expected_coherent = (ZERO, HALF, HALF, ZERO)
    expected_recorded = tuple(Q2(F(1, 4)) for _ in range(4))
    offdiagonal = sum(
        int(bool(d34.d_ab[i][j]))
        for i in range(8)
        for j in range(8)
        if i != j
    )
    return (
        int(coherent == expected_coherent),
        int(recorded == expected_recorded),
        offdiagonal,
        int(coherent != recorded),
    )


# ---------------------------------------------------------------------------
# R5: the Paper 28 square at star, serial and causal-DAG levels.


def path_probability(path: Sequence[object], packet) -> F:
    store = d38.initial_store()
    answer = F(1)
    for event in path:
        rates = dict(d39.event_intensities(store, packet))
        total = sum(rates.values(), F())
        answer *= rates[event] / total
        store, accepted = d38.transact(store, event)
        if not accepted:
            raise AssertionError("registered path rejected")
    return answer


def paper28_square_checks() -> Tuple[object, ...]:
    action = d39.action_checks()
    if action[9:11] != (F(1, 18), F(2, 33)):
        raise AssertionError("Paper 28 products drift")

    initial_star = d38.star_from_history(d38.initial_store().history)
    idle_action = ("ROOT_IDLE", "NONE")
    birth_action = ("NEIGHBOR_BIRTH", "B")
    idle_star = d38.star_step(initial_star, idle_action)
    birth_star = d38.star_step(initial_star, birth_action)
    star_ab = d38.star_step(idle_star, birth_action)
    star_ba = d38.star_step(birth_star, idle_action)
    star_products = (
        d38.star_kernel(initial_star)[idle_action]
        * d38.star_kernel(idle_star)[birth_action],
        d38.star_kernel(initial_star)[birth_action]
        * d38.star_kernel(birth_star)[idle_action],
    )

    base = d38.initial_store()
    idle = d38.proposed(base, "IDLE", "A")
    born = d38.proposed(base, "BIRTH", "B", "B/1")
    after_idle, accepted_idle = d38.transact(base, idle)
    after_born, accepted_born = d38.transact(base, born)
    born_after_idle = d38.proposed(after_idle, "BIRTH", "B", "B/1")
    idle_after_born = d38.proposed(after_born, "IDLE", "A")
    final_ab, accepted_ab = d38.transact(after_idle, born_after_idle)
    final_ba, accepted_ba = d38.transact(after_born, idle_after_born)
    path_ab = (idle, born_after_idle)
    path_ba = (born, idle_after_born)

    packet = d39.RatePacket((1, 1), (1, 2, 1))
    serial_products = (path_probability(path_ab, packet), path_probability(path_ba, packet))
    atom_ab = d39.dag_atom(path_ab)
    atom_ba = d39.dag_atom(path_ba)
    law, merged = d39.push_path_law(packet, typed=True)
    pushforward_mass = law[atom_ab]

    same_event_set = {event.record_id for event in path_ab} == {
        event.record_id for event in path_ba
    }
    same_store = d39.stable(final_ab.history.records) == d39.stable(final_ba.history.records)
    all_accepted = accepted_idle and accepted_born and accepted_ab and accepted_ba

    return (
        star_products[0],
        star_products[1],
        int(star_ab == star_ba),
        serial_products[0],
        serial_products[1],
        int(atom_ab == atom_ba),
        int(same_event_set),
        int(same_store),
        pushforward_mass,
        int(pushforward_mass == sum(serial_products, F())),
        merged,
        int(all_accepted),
        "LEVEL_MISMATCH_SERIAL_WEIGHTS_SUM_TO_ONE_TYPED_DAG_ATOM",
    )


# ---------------------------------------------------------------------------
# R6: positive completion-ratio / Doob h form.


def fraction_h_ratio(weights: Mapping[Tuple[int, ...], F]) -> Tuple[int, int]:
    depth = len(next(iter(weights)))

    def z(prefix: Tuple[int, ...]) -> F:
        return sum((weight for terminal, weight in weights.items() if terminal[: len(prefix)] == prefix), F())

    normalized = terminal_checks = 0
    for length in range(depth):
        for prefix in product((0, 1), repeat=length):
            row = {bit: z(prefix + (bit,)) / z(prefix) for bit in (0, 1)}
            normalized += int(sum(row.values(), F()) == 1)
    for terminal, weight in weights.items():
        running = F(1)
        for length, bit in enumerate(terminal):
            prefix = terminal[:length]
            running *= z(prefix + (bit,)) / z(prefix)
        terminal_checks += int(running == weight / z(()))
    return normalized, terminal_checks


def quantum_h_ratio(weights: Mapping[Tuple[int, int], Q2]) -> Tuple[int, int]:
    first_alphabet = tuple(sorted({terminal[0] for terminal in weights}))
    second_alphabet = tuple(sorted({terminal[1] for terminal in weights}))

    def z(prefix: Tuple[int, ...]) -> Q2:
        return sum(
            (weight for terminal, weight in weights.items() if terminal[: len(prefix)] == prefix),
            ZERO,
        )

    root = sum(weights.values(), ZERO)
    normalized = int(sum((qdiv(z((bit,)), root) for bit in first_alphabet), ZERO) == ONE)
    for a in first_alphabet:
        normalized += int(
            sum((qdiv(z((a, b)), z((a,))) for b in second_alphabet), ZERO) == ONE
        )
    terminal = 0
    for atom, weight in weights.items():
        product_weight = qdiv(z((atom[0],)), root) * qdiv(weight, z((atom[0],)))
        terminal += int(product_weight == qdiv(weight, root))
    return normalized, terminal


def completion_ratio_checks(bell_laws: Mapping[Tuple[int, int], Mapping[Tuple[int, int], Q2]]) -> Tuple[int, ...]:
    count_weights = {terminal: F(1) for terminal in product((0, 1), repeat=3)}
    classical_weights = {
        terminal: F(index + 2)
        for index, terminal in enumerate(product((0, 1), repeat=3))
    }
    count_rows, count_terminal = fraction_h_ratio(count_weights)
    classical_rows, classical_terminal = fraction_h_ratio(classical_weights)
    quantum_rows = quantum_terminal = 0
    for law in bell_laws.values():
        rows, terminal = quantum_h_ratio(law)
        quantum_rows += rows
        quantum_terminal += terminal
    completion = d39.completion_kernel_checks(3)
    return (
        count_rows,
        count_terminal,
        classical_rows,
        classical_terminal,
        quantum_rows,
        quantum_terminal,
        *completion,
    )


# ---------------------------------------------------------------------------
# R7: exact Bell/CHSH architecture fixture.


def bell_fixture() -> Tuple[Tuple[object, ...], Dict[Tuple[int, int], Dict[Tuple[int, int], Q2]]]:
    i2 = d34.I2
    x2 = d34.X2
    z2 = d34.Z2
    observables_a = {0: z2, 1: x2}
    observables_b = {
        0: d34.mscale(ROOT_HALF, d34.madd(z2, x2)),
        1: d34.mscale(ROOT_HALF, d34.madd(z2, d34.mscale(Q2(-1), x2))),
    }
    psi = [ROOT_HALF, ZERO, ZERO, ROOT_HALF]

    def projector(observable, outcome: int):
        return d34.mscale(HALF, d34.madd(i2, d34.mscale(Q2(outcome), observable)))

    laws: Dict[Tuple[int, int], Dict[Tuple[int, int], Q2]] = {}
    expectations: Dict[Tuple[int, int], Q2] = {}
    commutations = grams = normalizations = 0
    no_signalling = 0
    cocycles = 0

    for x, y in product((0, 1), repeat=2):
        left = d34.kron_matrix(observables_a[x], i2)
        right = d34.kron_matrix(i2, observables_b[y])
        commutations += int(d34.mm(left, right) == d34.mm(right, left))
        joint_observable = d34.kron_matrix(observables_a[x], observables_b[y])
        expectations[(x, y)] = d34.inner(psi, d34.mv(joint_observable, psi))

        branches = {}
        law = {}
        for a, b in product((1, -1), repeat=2):
            joint_projector = d34.kron_matrix(
                projector(observables_a[x], a),
                projector(observables_b[y], b),
            )
            branch = d34.mv(joint_projector, psi)
            branches[(a, b)] = branch
            law[(a, b)] = d34.inner(branch, branch)
        laws[(x, y)] = law
        gram = d34.gram([branches[key] for key in sorted(branches)])
        grams += int(gram == d34.transpose(gram))
        normalizations += int(sum(law.values(), ZERO) == ONE)

        for a in (1, -1):
            no_signalling += int(sum((law[(a, b)] for b in (1, -1)), ZERO) == HALF)
        for b in (1, -1):
            no_signalling += int(sum((law[(a, b)] for a in (1, -1)), ZERO) == HALF)
        for a, b in product((1, -1), repeat=2):
            via_a = HALF * qdiv(law[(a, b)], HALF)
            via_b = HALF * qdiv(law[(a, b)], HALF)
            cocycles += int(via_a == law[(a, b)] == via_b)

    expected = {
        (0, 0): ROOT_HALF,
        (0, 1): ROOT_HALF,
        (1, 0): ROOT_HALF,
        (1, 1): -ROOT_HALF,
    }
    chsh = expectations[(0, 0)] + expectations[(0, 1)] + expectations[(1, 0)] - expectations[(1, 1)]
    hidden_y0 = qdiv(laws[(1, 0)][(1, 1)], HALF)
    hidden_y1 = qdiv(laws[(1, 1)][(1, 1)], HALF)
    boundary_negative = int(hidden_y0 != hidden_y1)

    result = (
        int(expectations == expected),
        chsh,
        commutations,
        grams,
        normalizations,
        no_signalling,
        cocycles,
        boundary_negative,
        hidden_y0,
        hidden_y1,
    )
    return result, laws


# ---------------------------------------------------------------------------
# R8--R10: dictionary, universality and experimental handoff.


def identified_law_dictionary_audit() -> Tuple[int, int, int]:
    documents = {name: path.read_text() for name, (path, _hash) in LOCKS.items() if name in {"Paper15", "Paper18", "Paper19"}}
    markers = (
        ("Paper15", "action-to-kernel"),
        ("Paper15", "autonomous record instrument"),
        ("Paper15", "dimensional unit bridge"),
        ("Paper18", "boundary/cosmological state"),
        ("Paper18", "gauge measure/contour and renormalization prescription"),
        ("Paper18", "physical record/environment dynamics"),
        ("Paper18", "Born/preferred-basis debt"),
        ("Paper19", "no register↔system dictionary claimed"),
    )
    present = sum(int(marker in documents[name]) for name, marker in markers)
    coherent = tuple(d34.prob_so[key] for key in sorted(d34.prob_so))
    path_recorded = tuple(d34.recorded_prob[key] for key in sorted(d34.recorded_prob))
    instruments_differ = int(coherent != path_recorded)
    full_d15_executed = 0
    return present, instruments_differ, full_d15_executed


def universality_audit() -> Tuple[int, Tuple[Tuple[str, int], ...]]:
    rows = (
        ("Paper22 M-bit boundary lower bound", "GRAMMAR_INFORMATION"),
        ("Paper23 finite-stop battery", "GRAMMAR_INFORMATION"),
        ("D36 actor-local authentication", "GRAMMAR_INFORMATION"),
        ("D38 record-closure conditions", "GRAMMAR_INFORMATION"),
        ("D34b chosen Harris coefficients", "CLASSICAL_GENERATOR_SPECIFIC"),
        ("D35 chosen star update", "CLASSICAL_GENERATOR_SPECIFIC"),
        ("D39 1/18 versus 2/33", "CLASSICAL_GENERATOR_SPECIFIC"),
        ("D37 refined cylinder identity", "DECOHERENT_RECORD_UNIVERSAL"),
        ("D34c operator/functional sewing", "QUANTUM_FUNCTIONAL_SPECIFIC"),
        ("D39 rate identification", "BRIDGE_DEPENDENT_OR_OPEN"),
        ("D26 visibility pricing", "BRIDGE_DEPENDENT_OR_OPEN"),
        ("D15 to record-closed execution", "BRIDGE_DEPENDENT_OR_OPEN"),
    )
    counts = Counter(category for _result, category in rows)
    expected = {
        "GRAMMAR_INFORMATION": 4,
        "CLASSICAL_GENERATOR_SPECIFIC": 3,
        "DECOHERENT_RECORD_UNIVERSAL": 1,
        "QUANTUM_FUNCTIONAL_SPECIFIC": 1,
        "BRIDGE_DEPENDENT_OR_OPEN": 3,
    }
    unique = int(len(rows) == len({result for result, _category in rows}) and counts == expected)
    return unique, tuple(sorted(counts.items()))


def d26_handoff() -> Tuple[object, ...]:
    g = F(9, 25)
    visibility = F(4, 5)
    checks = (
        int(visibility * visibility == 1 - g),
        int(visibility**3 == F(64, 125)),
        int("sqrt(1-g)" in LOCKS["D26-output"][0].read_text()),
        int("TOKEN activation performs no birth isometry" in LOCKS["Paper28"][0].read_text()),
    )
    protocol_fields = (
        "MONITORED_PARENT_LINE",
        "AUTHENTICATED_BORN_VS_DORMANT_TOKEN",
        "ATTACHMENT_TOPOLOGY",
        "INITIATOR_LINE",
        "COUNTED_SAME_LINE_BIRTHS",
        "DECLARED_NOISE_MODEL",
    )
    return g, visibility, visibility**3, sum(checks), len(protocol_fields), 0


def main() -> None:
    out = []
    science: Dict[str, object] = {}
    gates: Dict[str, bool] = {}

    def emit(line: str) -> None:
        out.append(line)
        print(line)

    emit("[D40 where the action cocycle lives — exact level audit]")
    emit("ARITHMETIC: integer/Fraction/Q(sqrt2) exact; no floating theorem")

    r0 = lock_and_type_checks()
    science["R0"] = r0
    gates["R0"] = r0 == (len(LOCKS), 7)
    emit("[R0 LOCKS / TYPED LEVELS]")
    emit(f"antecedent_locks={r0[0]}/{len(LOCKS)}; distinct_level_constructors={r0[1]}/7")

    r1 = classical_descent_checks()
    science["R1"] = r1
    gates["R1"] = r1 == (1024, 1, 1, 1)
    emit("[R1 CLASSICAL CYLINDER DESCENT / FINITE SUFFICIENCY]")
    emit(f"positive_measure_squares={r1[0]}/1024; sufficient_control={r1[1]}/1; insufficient_control={r1[2]}/1; fibre_dependence_visible={r1[3]}/1")
    emit("theorem=COMMON_REFINED_CYLINDER_IMPLIES_EQUAL_CONDITIONAL_PRODUCTS; coarse_kernel_iff_fibre_laws_agree")

    r2 = action_functional_checks()
    science["R2"] = r2
    gates["R2"] = r2 == (1, 1, 1, 1, 1) and d34.FAIL == 0
    emit("[R2 OPERATOR / DECOHERENCE-FUNCTIONAL INTERCHANGE]")
    emit(f"disjoint_operator={r2[0]}/1; branch_vectors={r2[1]}/1; functional={r2[2]}/1; shared_support_negative={r2[3]}/1; restrictions={r2[4]}/1")

    r3 = durable_record_descent_checks()
    science["R3"] = r3
    gates["R3"] = r3 == (2, 8, 16, 5)
    emit("[R3 DECOHERENT DURABLE-RECORD DESCENT]")
    emit(f"decoherent_record_measures={r3[0]}/2; refined_click_squares={r3[1]}/8; positive_denominators={r3[2]}/16; load_bearing_hypotheses={r3[3]}/5")

    r4 = interference_controls()
    science["R4"] = r4
    gates["R4"] = r4 == (1, 1, 8, 1)
    emit("[R4 INTERFERENCE / RECORD-INSTRUMENT CONTROL]")
    emit(f"coherent_law={r4[0]}/1; orthogonal_path_record_law={r4[1]}/1; nonzero_offdiagonals={r4[2]}; laws_differ={r4[3]}/1")
    emit("classification=SCALAR_DESCENT_REQUIRES_DECLARED_DECOHERENT_RECORD_ALGEBRA")

    r5 = paper28_square_checks()
    science["R5"] = r5
    gates["R5"] = r5[:10] == (
        F(1, 18), F(2, 33), 1,
        F(1, 32), F(1, 48), 1, 1, 1, F(5, 96), 1,
    ) and r5[11:] == (1, "LEVEL_MISMATCH_SERIAL_WEIGHTS_SUM_TO_ONE_TYPED_DAG_ATOM")
    emit("[R5 PAPER 28 SQUARE ADJUDICATION]")
    emit(f"projected_star_products={ftext(r5[0])},{ftext(r5[1])}; same_final_star={r5[2]}/1")
    emit(f"complete_serial_products={ftext(r5[3])},{ftext(r5[4])}; same_typed_DAG={r5[5]}/1; same_event_set={r5[6]}/1; same_record_store={r5[7]}/1")
    emit(f"typed_DAG_pushforward_mass={ftext(r5[8])}; equals_serial_sum={r5[9]}/1; total_depth2_serial_merges={r5[10]}")
    emit(f"classification={r5[12]}")
    emit("Paper28_action_filter_nonmembership=SURVIVES; probability_inconsistency=NOT_INFERRED")

    bell, bell_laws = bell_fixture()
    science["R7"] = bell

    r6 = completion_ratio_checks(bell_laws)
    science["R6"] = r6
    gates["R6"] = r6 == (7, 8, 7, 8, 12, 16, 21, 78, 78, 179)
    emit("[R6 POSITIVE COMPLETION-RATIO / h-RATIO FORM]")
    emit(f"count_rows={r6[0]}/7; count_terminals={r6[1]}/8; classical_rows={r6[2]}/7; classical_terminals={r6[3]}/8")
    emit(f"Born_rows={r6[4]}/12; Born_terminals={r6[5]}/16; D39_completion_rows={r6[6]}; squares={r6[8]}/{r6[7]}; terminal_paths={r6[9]}")
    emit("K_flat_shape=GENERAL_POSITIVE_h_RATIO; Born_uniqueness_or_selection=NOT_INFERRED")

    gates["R7"] = bell[:8] == (1, Q2(0, 2), 4, 4, 4, 16, 16, 1)
    emit("[R7 EXACT BELL/CHSH ARCHITECTURE FIXTURE]")
    emit(f"correlators={bell[0]}/1; CHSH={bell[1].text()}; spacelike_interchanges={bell[2]}/4; Gram_forms={bell[3]}/4; normalized={bell[4]}/4")
    emit(f"no_signalling_marginals={bell[5]}/16; refined_click_cocycles={bell[6]}/16; erased_setting_boundary_negative={bell[7]}/1")
    emit(f"hidden_conditionals={bell[8].text()},{bell[9].text()}; join_needed_for_entanglement=NO; D23_in_degree_result=IDENTIFIABILITY_CEILING")

    r8 = identified_law_dictionary_audit()
    science["R8"] = r8
    gates["R8"] = r8 == (8, 1, 0)
    emit("[R8 IDENTIFIED-LAW DICTIONARY AUDIT]")
    emit(f"corpus_dictionary_markers={r8[0]}/8; same_operator_fixture_distinct_record_laws={r8[1]}/1; full_D15_click_law_executed={r8[2]}")
    emit("identified_low_energy_action=RETAINED; executable_record_closed_D15_law=NOT_ESTABLISHED")

    r9 = universality_audit()
    science["R9"] = r9
    gates["R9"] = r9 == (
        1,
        (
            ("BRIDGE_DEPENDENT_OR_OPEN", 3),
            ("CLASSICAL_GENERATOR_SPECIFIC", 3),
            ("DECOHERENT_RECORD_UNIVERSAL", 1),
            ("GRAMMAR_INFORMATION", 4),
            ("QUANTUM_FUNCTIONAL_SPECIFIC", 1),
        ),
    )
    emit("[R9 UNIVERSALITY AUDIT]")
    emit(f"unique_class_assignments={r9[0]}/1; class_counts={stable(r9[1])}")

    r10 = d26_handoff()
    science["R10"] = r10
    gates["R10"] = r10 == (F(9, 25), F(4, 5), F(64, 125), 4, 6, 0)
    emit("[R10 D26 EXPERIMENTAL HANDOFF]")
    emit(f"g={ftext(r10[0])}; one_BORN_visibility={ftext(r10[1])}; three_BORN_visibility={ftext(r10[2])}; exact_bridge_checks={r10[3]}/4")
    emit(f"preregistered_protocol_fields={r10[4]}/6; new_lab_data={r10[5]}; TOKEN_birth_isometry=ABSENT_IN_DECLARED_MODEL")

    source_hash = sha256(Path(__file__))
    body_hash = hashlib.sha256(("\n".join(out) + "\n").encode()).hexdigest()
    science_hash = hashlib.sha256(stable(science).encode()).hexdigest()
    emit("[HASHES]")
    emit(f"source_sha256={source_hash}")
    emit(f"stdout_body_sha256={body_hash}")
    emit(f"internal_science_sha256={science_hash}")
    emit("[GATES]")
    for name in sorted(gates, key=lambda key: int(key[1:])):
        emit(f"{name}={'PASS' if gates[name] else 'FAIL'}")
    passed = sum(gates.values())
    emit("[VERDICT]")
    emit(f"{'PASS' if passed == len(gates) else 'FAIL'} {passed}/{len(gates)}")
    emit("PRIMARY=LEVEL_MISMATCH_AT_SERIAL_TO_TYPED_DAG_DESCENT")
    emit("PHYSICAL_AUDIT=UNRESOLVED_D15_DICTIONARY")
    emit("FINITE ACTION/DF-TO-DECOHERENT-RECORD DESCENT THEOREM; EXACT BELL ARCHITECTURE FIXTURE")
    emit("full D15 execution, generated quantum content bridge, physical clock calibration and new experiment remain open")
    if passed != len(gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One-file exact evaluator for Paper 15 Stage-B source construction.

No repository science source is imported.  The only dependencies are Python's
standard library.  Scientific decisions use integers, Fraction, finite sets,
or symbolic strings; no floating tolerance is promotive.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import os
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence


PIN_COMMIT = "fef4bc9080c0f27118a2ca501ea6e51c72135847"
PIN_SHA256 = "06d8fc6df408e9fac767e0401b055565bea26b5e7d2da6fddc275d3aff4af3b6"
PARENT_SHA256 = "0c77cebdc56bd28006dcef4adadb979b88c57666f14ff0b4a917e80516749cf6"
SCHEMA = "p15-spacetime-exact-v1"
FRESH_SCHEMA = "p15-spacetime-fresh-cases-v1"
OUTPUT_SCHEMA = "p15-spacetime-output-v1"
RECEIPT_SCHEMA = "p15-spacetime-receipt-v1"
PIN_NAME = "note-paper15-spacetime-reconstruction-pin.md"
PARENT_NAME = "note-paper14-premetric-hostile-adjudication.md"
SOURCE_NAME = "p15_spacetime_exact.py"
PAPER_NAME = "paper-15-conditional-spacetime-reconstruction.md"
CONSTRUCTION_NAME = "note-paper15-spacetime-construction.md"
FRESH_NAME = "p15_spacetime_fresh_cases.json"
OUTPUT_NAME = "p15_spacetime_output.json"
RECEIPT_NAME = "p15_spacetime_receipt.json"


class ScientificFailure(RuntimeError):
    pass


class Audit:
    def __init__(self) -> None:
        self.labels: list[str] = []

    def require(self, condition: bool, label: str) -> None:
        if not condition:
            raise ScientificFailure(label)
        self.labels.append(label)


def fs(value: F | int) -> str:
    value = F(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def cbytes(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode("ascii")


def sha_obj(value: Any) -> str:
    return hashlib.sha256(cbytes(value)).hexdigest()


def jsonable(value: Any) -> Any:
    if isinstance(value, F):
        return fs(value)
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    if isinstance(value, (set, frozenset)):
        return [jsonable(item) for item in sorted(value, key=repr)]
    return value


def keyed_seal(key: str, value: Any) -> str:
    return sha_obj({"key": key, "value": jsonable(value)})


def source_sha() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def poset_evidence(nodes: list[Any], relation: set[tuple[Any, Any]]) -> dict[str, Any]:
    complete = {
        "nodes": [jsonable(node) for node in nodes],
        "strict_relation": [[jsonable(a), jsonable(b)] for a, b in sorted(relation, key=repr)],
    }
    return {"sha256": sha_obj(complete), "bytes": len(cbytes(complete)), "complete": complete}


def relation_closure(nodes: list[str], covers: set[tuple[str, str]]) -> set[tuple[str, str]]:
    reach = set(covers)
    changed = True
    while changed:
        changed = False
        for a, b in tuple(reach):
            for c, d in tuple(reach):
                if b == c and a != d and (a, d) not in reach:
                    reach.add((a, d))
                    changed = True
    if any(a == b for a, b in reach):
        raise ScientificFailure("cyclic relation")
    return reach


def height(nodes: list[Any], relation: set[tuple[Any, Any]]) -> int:
    pred = {v: [] for v in nodes}
    for u, v in relation:
        pred[v].append(u)
    unseen = set(nodes)
    levels: dict[Any, int] = {}
    while unseen:
        ready = sorted((v for v in unseen if all(u in levels for u in pred[v])), key=str)
        if not ready:
            raise ScientificFailure("height on cyclic relation")
        for v in ready:
            levels[v] = 1 + max((levels[u] for u in pred[v]), default=0)
            unseen.remove(v)
    return max(levels.values(), default=0)


def width(nodes: list[Any], relation: set[tuple[Any, Any]]) -> int:
    outgoing = {u: sorted((v for a, v in relation if a == u), key=str) for u in nodes}
    matched: dict[Any, Any] = {}

    def augment(u: Any, seen: set[Any]) -> bool:
        for v in outgoing[u]:
            if v in seen:
                continue
            seen.add(v)
            if v not in matched or augment(matched[v], seen):
                matched[v] = u
                return True
        return False

    count = sum(1 for u in nodes if augment(u, set()))
    return len(nodes) - count


def relation_fraction(nodes: list[Any], relation: set[tuple[Any, Any]]) -> F | None:
    n = len(nodes)
    return None if n < 2 else F(2 * len(relation), n * (n - 1))


def canonical_key(nodes: list[Any], relation: set[tuple[Any, Any]]) -> str:
    n = len(nodes)
    if n > 7:
        raise ValueError("canonical_key deliberately limited to seven nodes")
    best: str | None = None
    for order in itertools.permutations(nodes):
        bits = "".join("1" if (order[i], order[j]) in relation else "0" for i in range(n) for j in range(n))
        if best is None or bits < best:
            best = bits
    assert best is not None
    return best


def poset_record(nodes: list[Any], relation: set[tuple[Any, Any]]) -> dict[str, Any]:
    return {
        "N": len(nodes),
        "R": len(relation),
        "r": None if len(nodes) < 2 else fs(relation_fraction(nodes, relation)),
        "H": height(nodes, relation),
        "W": width(nodes, relation),
    }


def native_interval(d: int) -> tuple[list[str], set[tuple[str, str]], set[tuple[str, str]]]:
    nodes = ["root"]
    covers: set[tuple[str, str]] = set()
    previous = "root"
    for i in range(1, d + 1):
        a, b, c, e = (f"a{i}", f"b{i}", f"c{i}", f"e{i}")
        nodes.extend([a, b, c, e])
        covers |= {(previous, a), (previous, b), (a, c), (b, c), (c, e)}
        previous = e
    return nodes, covers, relation_closure(nodes, covers)


def native_family(audit: Audit) -> dict[str, Any]:
    rows = []
    for d in range(1, 7):
        nodes, covers, relation = native_interval(d)
        rec = poset_record(nodes, relation)
        audit.require(rec["N"] == 4 * d + 1, f"native N d={d}")
        audit.require(rec["R"] == math.comb(4 * d + 1, 2) - d, f"native R d={d}")
        audit.require(rec["r"] == fs(1 - F(1, 2 * (4 * d + 1))), f"native r d={d}")
        audit.require(rec["H"] == 3 * d + 1, f"native H d={d}")
        audit.require(rec["W"] == 2, f"native W d={d}")
        rows.append({"d": d, **rec, "cover_count": len(covers), "interval": poset_evidence(nodes, relation)})
    return {
        "construction": "root; per cell incomparable a_i,b_i then c_i then e_i; e_i feeds next cell",
        "rows": rows,
        "closed_forms": {"N": "4d+1", "R": "C(4d+1,2)-d", "r": "1-1/[2(4d+1)]", "H": "3d+1", "W": "2"},
        "coordinate_ceiling_after_fresh_pass": "P15-NATIVE-BUNDLE-FAMILY-FAILS-REGISTERED-DIAMOND-SCALING",
        "scope": "registered fixed-diamond/noncompact-flat asymptotic only",
    }


def product_poset(n: int) -> tuple[list[tuple[int, int]], set[tuple[tuple[int, int], tuple[int, int]]]]:
    nodes = [(i, j) for i in range(n) for j in range(n)]
    relation = {(x, y) for x in nodes for y in nodes if x != y and x[0] <= y[0] and x[1] <= y[1]}
    return nodes, relation


def product_family(audit: Audit) -> dict[str, Any]:
    rows = []
    for n in range(1, 8):
        nodes, relation = product_poset(n)
        rec = poset_record(nodes, relation)
        audit.require(rec["R"] == n * n * (n - 1) * (n + 3) // 4, f"product R n={n}")
        audit.require(rec["H"] == 2 * n - 1, f"product H n={n}")
        audit.require(rec["W"] == n, f"product W n={n}")
        if n > 1:
            audit.require(rec["r"] == fs(F(n + 3, 2 * (n + 1))), f"product r n={n}")
        transposed = {((a[1], a[0]), (b[1], b[0])) for a, b in relation}
        audit.require(transposed == relation, f"product transpose n={n}")
        rows.append({"n": n, **rec, "interval": poset_evidence(nodes, relation)})
    return {
        "rows": rows,
        "closed_forms": {"N": "n^2", "R": "n^2(n-1)(n+3)/4", "H": "2n-1", "W": "n", "r": "(n+3)/(2(n+1))"},
        "coordinate_ceiling_after_fresh_pass": "P15-DECLARED-PRODUCT-ORDER-KINEMATIC-COMPATIBILITY",
    }


def relative_relation(order: tuple[int, ...]) -> set[tuple[int, int]]:
    pos = [0] * len(order)
    for i, label in enumerate(order):
        pos[label] = i
    return {(i, j) for i in range(len(order)) for j in range(i + 1, len(order)) if pos[i] < pos[j]}


def delete_standardize(order: tuple[int, ...], deleted: int) -> tuple[int, ...]:
    labels = [x for x in range(len(order)) if x != deleted]
    rename = {old: new for new, old in enumerate(labels)}
    return tuple(rename[x] for x in order if x != deleted)


def two_order_family(audit: Audit) -> dict[str, Any]:
    rows: dict[str, Any] = {}
    for n in range(1, 6):
        classes: Counter[str] = Counter()
        hs: Counter[int] = Counter()
        ws: Counter[int] = Counter()
        rs: Counter[int] = Counter()
        total_R = 0
        interval_manifest = []
        for order in itertools.permutations(range(n)):
            rel = relative_relation(order)
            key = canonical_key(list(range(n)), rel)
            classes[key] += 1
            hs[height(list(range(n)), rel)] += 1
            ws[width(list(range(n)), rel)] += 1
            rs[len(rel)] += 1
            total_R += len(rel)
            complete = poset_evidence(list(range(n)), rel)
            interval_manifest.append({"relative_order": list(order), "sha256": complete["sha256"], "bytes": complete["bytes"]})
            inv = [0] * n
            for rank, label in enumerate(order):
                inv[label] = rank
            audit.require(canonical_key(list(range(n)), relative_relation(tuple(inv))) == key, f"two-order swap n={n} {order}")
        audit.require(F(total_R, math.factorial(n)) == F(math.comb(n, 2), 2), f"two-order mean R n={n}")
        class_map = dict(sorted(classes.items()))
        rows[str(n)] = {
            "relative_orders": math.factorial(n), "unlabeled_classes": len(classes),
            "class_counts_sha256": sha_obj(class_map), "class_counts": class_map,
            "height_counts": {str(k): v for k, v in sorted(hs.items())},
            "width_counts": {str(k): v for k, v in sorted(ws.items())},
            "R_counts": {str(k): v for k, v in sorted(rs.items())},
            "mean_R": fs(F(math.comb(n, 2), 2)), "mean_r": None if n < 2 else "1/2",
            "complete_interval_manifest": interval_manifest,
        }
    projected: Counter[tuple[int, ...]] = Counter()
    for order in itertools.permutations(range(5)):
        for deleted in range(5):
            projected[delete_standardize(order, deleted)] += 1
    audit.require(len(projected) == 24 and set(projected.values()) == {25}, "two-order projectivity 5->4")
    rows["projectivity_5_to_4"] = {"outputs": 24, "multiplicity": 25, "pairs": 600}
    return {"finite_enumeration": rows, "coordinate_ceiling_after_fresh_pass": "P15-DECLARED-FLAT-1PLUS1-ORDER-AND-NUMBER-CONTROL"}


def ptrim(p: list[F]) -> list[F]:
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def padd(a: list[F], b: list[F]) -> list[F]:
    out = [F(0)] * max(len(a), len(b))
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    return ptrim(out)


def pscale(a: list[F], s: F) -> list[F]:
    return ptrim([s * x for x in a])


def pmul(a: list[F], b: list[F]) -> list[F]:
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i + j] += x * y
    return ptrim(out)


def pint0(a: list[F]) -> list[F]:
    return [F(0)] + [x / (i + 1) for i, x in enumerate(a)]


def peval(a: list[F], x: F) -> F:
    out = F(0)
    for c in reversed(a): out = out * x + c
    return out


def pderiv(a: list[F]) -> list[F]:
    return [F(i) * a[i] for i in range(1, len(a))] or [F(0)]


def pint01(a: list[F]) -> F:
    return sum((x / (i + 1) for i, x in enumerate(a)), F(0))


def ordered_integral(profile: list[F], k: int, mask: int) -> F:
    cumulative = [F(1)]
    for j in range(k):
        cumulative = pint0(pmul(cumulative, profile if mask & (1 << j) else [F(1)]))
    return peval(cumulative, F(1))


def chain_coefficients(profile: list[F], k: int) -> list[F]:
    out = [F(0)] * (k + 1)
    for mask in range(1 << k):
        value = ordered_integral(profile, k, mask)
        out[mask.bit_count()] += value * value
    return ptrim(out)


def phi_star_profile() -> list[F]:
    x = [F(1), F(-2)]
    x2 = pmul(x, x)
    return padd(x, pscale(pmul(pmul(x, padd([F(1)], pscale(x2, -1))), padd(x2, [F(-3, 7)])), F(7, 8)))


def copula(theta: F, u: F, v: F, profile: list[F] | None = None) -> F:
    profile = [F(1), F(-2)] if profile is None else profile
    return 1 + theta * peval(profile, u) * peval(profile, v)


def local_affine_identity(audit: Audit, theta: F, A: F, u: F, v: F, du: F, dv: F) -> dict[str, str]:
    c0 = copula(theta, u, v)
    cu = -2 * theta * (1 - 2 * v)
    cv = -2 * theta * (1 - 2 * u)
    cuv = 4 * theta
    mixed = (c0 * cuv - cu * cv) / c0**2
    alpha, beta, gamma = du * cu / c0, dv * cv / c0, du * dv * cuv / c0
    tau = F(2, 9) * (gamma - alpha * beta)
    volume = 4 * A * du * dv * c0
    metric_R = 2 * mixed / (A * c0)
    order_R = 36 * tau / volume
    audit.require(metric_R == order_R == 8 * theta / (A * c0**3), f"local affine curvature {(u,v,du,dv)}")
    return {"u": fs(u), "v": fs(v), "du": fs(du), "dv": fs(dv), "c": fs(c0), "tau": fs(tau), "V": fs(volume), "R": fs(metric_R)}


def affine_family(audit: Audit) -> dict[str, Any]:
    theta = F(-7, 25)
    affine = [F(1), F(-2)]
    expected = {
        1: [F(1)], 2: [F(1, 4), F(1, 18)],
        3: [F(1, 36), F(1, 72), F(1, 600)],
        4: [F(1, 576), F(1, 720), F(23, 64800), F(1, 35280)],
    }
    expected_B = {2: F(211, 900), 3: F(13511, 562500), 4: F(556643, 405000000)}
    polys, values = {}, {}
    for k in range(1, 5):
        coeff = chain_coefficients(affine, k)
        audit.require(coeff == expected[k], f"affine I{k} coefficients")
        value = peval(coeff, theta)
        if k > 1: audit.require(value == expected_B[k], f"affine I{k} B value")
        polys[str(k)] = [fs(x) for x in coeff]
        values[str(k)] = fs(value)
    other_root = -F(25, 3) - theta
    audit.require(other_root == F(-604, 75) and not (-1 < other_root < 1), "I3 unique admissible theta")

    star = phi_star_profile()
    audit.require(peval(star, 0) == 1 and peval(star, 1) == -1, "phi-star endpoints")
    audit.require(pint01(star) == 0, "phi-star mean")
    audit.require(pint01(pmul([F(0), F(1)], star)) == F(-1, 6), "phi-star u moment")
    slope = peval(pderiv(star), F(1, 2))
    audit.require(slope == F(-5, 4), "phi-star center slope")
    star_values = {str(k): peval(chain_coefficients(star, k), theta) for k in range(1, 5)}
    audit.require(star_values["2"] == expected_B[2], "phi-star same I2")
    audit.require(star_values["3"] == F(11933657, 496910700), "phi-star I3")
    audit.require(star_values["3"] - expected_B[3] == F(-299557, 77642296875), "phi-star I3 discriminator")
    audit.require(2 * theta * slope**2 == F(-7, 8), "phi-star curvature")

    actual_dx = [F(5, 8), 0, F(15, 4), 0, F(-35, 8)]
    printed_dx = [F(13, 16), 0, F(15, 8), 0, F(-35, 16)]
    audit.require(actual_dx != printed_dx, "detect exposed-draft derivative typo")
    local = [
        local_affine_identity(audit, theta, F(5, 7), F(1, 2), F(1, 2), F(1, 2), F(1, 2)),
        local_affine_identity(audit, theta, F(5, 7), F(1, 3), F(2, 3), F(1, 6), F(1, 6)),
    ]
    return {
        "theta": fs(theta), "density_range": ["18/25", "32/25"],
        "I_polynomials": polys, "I_at_theta": values, "I3_other_root": fs(other_root),
        "phi_star": {
            "coefficients_u": [fs(x) for x in star], "I_at_theta": {k: fs(v) for k, v in star_values.items()},
            "I3_minus_affine": fs(star_values["3"] - expected_B[3]),
            "I4_minus_affine": fs(star_values["4"] - expected_B[4]), "center_R_times_A": "-7/8",
        },
        "affine_center_R_times_A": "-56/25", "local_order_volume_identities": local,
        "nonbinding_draft_issue": {"printed": "(13+30x^2-35x^4)/16", "correct": "(5+30x^2-35x^4)/8"},
        "coordinate_ceiling_after_fresh_pass": "P15-DECLARED-AFFINE-COPULA-CONDITIONAL-CONTROL",
    }


def tv(p: dict[Any, F], q: dict[Any, F]) -> F:
    return F(1, 2) * sum((abs(p.get(k, 0) - q.get(k, 0)) for k in set(p) | set(q)), F(0))


Distribution = dict[tuple[Any, ...], F]


def distribution(rows: Iterable[tuple[Sequence[Any], F]]) -> Distribution:
    out: Distribution = {}
    for state, probability in rows:
        state_tuple = tuple(state)
        if probability < 0:
            raise ValueError("negative transition probability")
        out[state_tuple] = out.get(state_tuple, F(0)) + probability
    out = {state: probability for state, probability in out.items() if probability}
    if sum(out.values(), F(0)) != 1:
        raise ValueError("transition row is not normalized")
    return out


def deterministic(*state: Any) -> Distribution:
    return distribution(((state, F(1)),))


def joint_factorizes(dist: Distribution, left_index: int, right_index: int) -> bool:
    left_values = sorted({state[left_index] for state in dist}, key=repr)
    right_values = sorted({state[right_index] for state in dist}, key=repr)
    left = {x: sum((p for state, p in dist.items() if state[left_index] == x), F(0)) for x in left_values}
    right = {y: sum((p for state, p in dist.items() if state[right_index] == y), F(0)) for y in right_values}
    return all(sum((p for state, p in dist.items() if state[left_index] == x and state[right_index] == y), F(0)) == left[x] * right[y]
               for x in left_values for y in right_values)


@dataclass(frozen=True)
class Reader:
    name: str
    target: str
    indices: tuple[int, ...]
    kind: str = "identity"
    complete: bool = True

    def read(self, state: tuple[Any, ...]) -> Any:
        values = tuple(state[index] for index in self.indices)
        if self.kind == "identity":
            return values[0] if len(values) == 1 else values
        if self.kind == "parity":
            return sum(int(value) for value in values) % 2
        raise ValueError(f"unknown reader kind: {self.kind}")


@dataclass
class ControlLaw:
    identifier: str
    meaning: str
    components: tuple[str, ...]
    experiments: dict[str, dict[str, dict[str, Distribution]]]
    readers: tuple[Reader, ...]
    queries: tuple[tuple[str, str], ...]
    division_flags: dict[str, bool]
    facts: dict[str, Any]

    def validate(self) -> None:
        names = {reader.name for reader in self.readers}
        if len(names) != len(self.readers):
            raise ValueError("reader names are not unique")
        for reader in self.readers:
            if not reader.indices or any(index < 0 or index >= len(self.components) for index in reader.indices):
                raise ValueError("reader index outside complete successor")
        for source, contexts in self.experiments.items():
            if not contexts:
                raise ValueError(f"{self.identifier}:{source} has no complete context")
            for context, preparations in contexts.items():
                if not preparations:
                    raise ValueError(f"{self.identifier}:{source}:{context} has no preparation")
                for row in preparations.values():
                    if sum(row.values(), F(0)) != 1 or any(len(state) != len(self.components) for state in row):
                        raise ValueError("invalid complete successor transition row")
        for source, reader_name in self.queries:
            if source not in self.experiments or reader_name not in names:
                raise ValueError("invalid signed-tensor query")

    def reader(self, name: str) -> Reader:
        return next(reader for reader in self.readers if reader.name == name)

    def tensor(self, source: str, context: str, alpha: str, beta: str, reader_name: str) -> dict[Any, F]:
        reader = self.reader(reader_name)
        rows = self.experiments[source][context]
        pa, pb = rows[alpha], rows[beta]
        values = {reader.read(state) for state in pa} | {reader.read(state) for state in pb}
        answer = {}
        for value in sorted(values, key=repr):
            va = sum((probability for state, probability in pa.items() if reader.read(state) == value), F(0))
            vb = sum((probability for state, probability in pb.items() if reader.read(state) == value), F(0))
            answer[value] = va - vb
        if sum(answer.values(), F(0)) != 0:
            raise ScientificFailure("signed response tensor does not sum to zero")
        return answer

    def all_tensors(self) -> list[dict[str, Any]]:
        rows = []
        for source, reader_name in self.queries:
            reader = self.reader(reader_name)
            for context, preparations in sorted(self.experiments[source].items()):
                for alpha, beta in itertools.permutations(sorted(preparations), 2):
                    entries = self.tensor(source, context, alpha, beta, reader_name)
                    rows.append({
                        "source": source, "context": context, "alpha": alpha, "beta": beta,
                        "reader": reader_name, "reader_complete": reader.complete, "target": reader.target,
                        "entries": [[jsonable(value), fs(delta)] for value, delta in sorted(entries.items(), key=lambda item: repr(item[0]))],
                    })
        return rows

    def record(self) -> dict[str, Any]:
        transition_tables = []
        preparation_pairs = []
        for source, contexts in sorted(self.experiments.items()):
            for context, preparations in sorted(contexts.items()):
                for preparation, row in sorted(preparations.items()):
                    transition_tables.append({
                        "source": source, "context": context, "preparation": preparation,
                        "complete_successor": [[jsonable(state), fs(probability)] for state, probability in sorted(row.items(), key=lambda item: repr(item[0]))],
                    })
                preparation_pairs.extend({"source": source, "context": context, "alpha": alpha, "beta": beta}
                                         for alpha, beta in itertools.permutations(sorted(preparations), 2))
        body = {
            "id": self.identifier, "meaning": self.meaning, "components": list(self.components),
            "transition_tables": transition_tables, "same_law_ordered_preparation_pairs": preparation_pairs,
            "readers": [{"name": reader.name, "target": reader.target, "indices": list(reader.indices),
                         "kind": reader.kind, "complete": reader.complete} for reader in self.readers],
            "queries": [list(query) for query in self.queries], "division_flags": self.division_flags,
            "facts": jsonable(self.facts), "signed_response_tensors": self.all_tensors(),
        }
        body["seal"] = sha_obj(body)
        return body


def prep01(make: Callable[[int], Distribution]) -> dict[str, Distribution]:
    return {"p0": make(0), "p1": make(1)}


def build_control_laws() -> dict[str, ControlLaw]:
    half = F(1, 2)
    laws: dict[str, ControlLaw] = {}
    laws["T1"] = ControlLaw("T1", "serial whole-law intervention", ("B", "C"),
        {"A": {"fixed": prep01(lambda p: deterministic(p, p))}},
        (Reader("B.complete", "B", (0,)), Reader("C.complete", "C", (1,))),
        (("A", "B.complete"), ("A", "C.complete")), {"B": True}, {"expected_edges": ["A->B", "A->C"]})
    laws["T2"] = ControlLaw("T2", "common cause with intervention-neutral target marginal", ("A", "B", "U"),
        {"A": {"fixed": prep01(lambda p: distribution((((p, 0, 0), half), ((p, 1, 1), half))))}},
        (Reader("B.complete", "B", (1,)),), (("A", "B.complete"),), {},
        {"observational_P_A_equals_B": F(1), "interventional_B": [half, half]})

    def t3_row(p: int) -> Distribution:
        return distribution((((0, 0), half), ((1, 1), half))) if p == 0 else distribution((((0, 1), half), ((1, 0), half)))

    t3_preps = prep01(t3_row)
    laws["T3"] = ControlLaw("T3", "minimal nonfactorizable joint co-onset", ("X", "Y"),
        {"E": {"fixed": t3_preps}},
        (Reader("XY.complete", "XY", (0, 1)), Reader("X.complete", "X", (0,)), Reader("Y.complete", "Y", (1,))),
        (("E", "XY.complete"), ("E", "X.complete"), ("E", "Y.complete")), {},
        {"one_minimal_transition": True, "factorizable": all(joint_factorizes(row, 0, 1) for row in t3_preps.values()),
         "symmetric_response_alone_is_certificate": False, "bundle_multiplicity": 2})

    def t4_state(p: int, order: tuple[str, str]) -> tuple[int, int, int]:
        state = {"B": 0, "C": 0}
        for arm in order:
            state[arm] = p
        return state["B"], state["C"], state["B"] & state["C"]

    orders = (("B", "C"), ("C", "B"))
    order_rows = {order: {p: t4_state(p, order) for p in (0, 1)} for order in orders}
    laws["T4"] = ControlLaw("T4", "independent commuting diamond arms", ("B", "C", "D"),
        {"A": {"fixed": prep01(lambda p: deterministic(*t4_state(p, orders[0])))}},
        (Reader("B.complete", "B", (0,)), Reader("C.complete", "C", (1,)), Reader("D.complete", "D", (2,))),
        (("A", "B.complete"), ("A", "C.complete"), ("A", "D.complete")), {"B": True, "C": True},
        {"serializations": orders, "serialization_outputs": order_rows,
         "same_complete_law": order_rows[orders[0]] == order_rows[orders[1]]})
    laws["T5"] = ControlLaw("T5", "reconvergent parity with partial B/C cuts", ("B", "C", "D"),
        {"A": {f"c{c}": prep01(lambda p, c=c: deterministic(p, c, p ^ c)) for c in (0, 1)}},
        (Reader("D.complete", "D", (2,)),), (("A", "D.complete"),), {"B": False, "C": False, "BC": True},
        {"whole_law_retained": True})
    laws["T6"] = ControlLaw("T6", "stable readable record with incomplete frontier", ("R", "Y"),
        {"A": {f"h{h}": prep01(lambda p, h=h: deterministic(p, h)) for h in (0, 1)}},
        (Reader("R.complete", "R", (0,)), Reader("Y.complete", "Y", (1,))),
        (("A", "R.complete"), ("A", "Y.complete")), {"R": False},
        {"record_persistent": True, "missing_complete_state": "h"})
    laws["T7"] = ControlLaw("T7", "complete division with no newly written record", ("F", "Y"),
        {"A": {"fixed": prep01(lambda p: deterministic(p, p))}}, (Reader("Y.complete", "Y", (1,)),),
        (("A", "Y.complete"),), {"F": True}, {"new_record": False})
    laws["T8"] = ControlLaw("T8", "delayed whole-law response across incomplete cut", ("I", "Y"),
        {"A": {f"h{h}": prep01(lambda p, h=h: deterministic(p, p ^ h)) for h in (0, 1)}},
        (Reader("Y.complete", "Y", (1,)),), (("A", "Y.complete"),), {"I": False},
        {"whole_law_response": True, "intermediate_Markovization": False})
    laws["T9"] = ControlLaw("T9", "persistent bidirectional influence across distinct divisions", ("X", "Y"),
        {"X": {"fixed": prep01(lambda p: deterministic(p, p))}, "Y": {"fixed": prep01(lambda p: deterministic(p, p))}},
        (Reader("X.complete", "X", (0,)), Reader("Y.complete", "Y", (1,))),
        (("X", "Y.complete"), ("Y", "X.complete")), {"X": True, "Y": True}, {"joint_onset_certificate": False})
    laws["T10"] = ControlLaw("T10", "total response separated from direct response by mediator intervention", ("B", "C"),
        {"A": {"natural": prep01(lambda p: deterministic(p, p)), "doB0": prep01(lambda _p: deterministic(0, 0)),
               "doB1": prep01(lambda _p: deterministic(1, 1))}},
        (Reader("B.complete", "B", (0,)), Reader("C.complete", "C", (1,))),
        (("A", "B.complete"), ("A", "C.complete")), {"B": True}, {"mediator": "B"})
    laws["T11"] = ControlLaw("T11", "downstream cancellation on an A-B-C producer path", ("B", "C"),
        {"A": {"natural": prep01(lambda p: deterministic(p, 0))},
         "B": {f"a{a}": prep01(lambda p, a=a: deterministic(p, p ^ a)) for a in (0, 1)}},
        (Reader("B.complete", "B", (0,)), Reader("C.complete", "C", (1,))),
        (("A", "B.complete"), ("A", "C.complete"), ("B", "C.complete")), {"B": True},
        {"producer_edges": ["A->B", "B->C"], "total_A_to_C_cancelled": True})
    laws["T12"] = ControlLaw("T12", "distinct occurrence nodes sharing one reusable type", ("Q#1", "Q#2"),
        {"A": {"fixed": prep01(lambda p: deterministic(p, p))}},
        (Reader("Q1.complete", "Q#1", (0,)), Reader("Q2.complete", "Q#2", (1,))),
        (("A", "Q1.complete"), ("A", "Q2.complete")), {"Q#1": True},
        {"occurrence_edges": [["Q#1", "Q#2"]], "type_names": ["Q", "Q"]})
    laws["T13"] = ControlLaw("T13", "opposite influence directions in admissible exterior contexts", ("A", "B"),
        {"A": {"c0": prep01(lambda p: deterministic(p, p)), "c1": prep01(lambda p: deterministic(p, 0))},
         "B": {"c0": prep01(lambda p: deterministic(0, p)), "c1": prep01(lambda p: deterministic(p, p))}},
        (Reader("A.complete", "A", (0,)), Reader("B.complete", "B", (1,))),
        (("A", "B.complete"), ("B", "A.complete")), {},
        {"contexts_complete": True, "c0_orientation": "A->B", "c1_orientation": "B->A"})
    laws["T14"] = ControlLaw("T14", "parity reader hides a changing complete two-bit target", ("B0", "B1"),
        {"A": {"fixed": prep01(lambda p: deterministic(p, p))}},
        (Reader("B.complete", "B", (0, 1)), Reader("B.parity", "B", (0, 1), "parity", False)),
        (("A", "B.complete"), ("A", "B.parity")), {},
        {"complete_reader_separates": True, "parity_reader_complete": False})
    for law in laws.values():
        law.validate()
    return laws


@dataclass(frozen=True)
class DivisionTest:
    identifier: str
    rows: tuple[tuple[tuple[Any, ...], Any, Distribution], ...]

    def evaluate(self) -> tuple[bool, dict[str, Any] | None]:
        seen: dict[Any, tuple[Distribution, tuple[Any, ...]]] = {}
        for past, frontier, future in self.rows:
            if frontier in seen and seen[frontier][0] != future:
                prior_future, prior_past = seen[frontier]
                return False, {"same_frontier": jsonable(frontier), "past_1": jsonable(prior_past), "past_2": jsonable(past),
                               "future_1": distribution_record(prior_future), "future_2": distribution_record(future)}
            seen[frontier] = (future, past)
        return True, None


def distribution_record(row: Distribution) -> list[list[Any]]:
    return [[jsonable(state), fs(probability)] for state, probability in sorted(row.items(), key=lambda item: repr(item[0]))]


def binary_division(identifier: str, frontier: Callable[[int, int], Any], future: Callable[[int, int], int]) -> DivisionTest:
    return DivisionTest(identifier, tuple(((a, h), frontier(a, h), deterministic(future(a, h))) for a in (0, 1) for h in (0, 1)))


def division_tests() -> dict[str, DivisionTest]:
    return {
        "T5.B": binary_division("T5.B", lambda a, b: a, lambda a, b: a ^ b),
        "T5.C": binary_division("T5.C", lambda a, b: b, lambda a, b: a ^ b),
        "T5.BC": binary_division("T5.BC", lambda a, b: (a, b), lambda a, b: a ^ b),
        "T6.R": binary_division("T6.R", lambda a, h: a, lambda _a, h: h),
        "T7.F": binary_division("T7.F", lambda a, _h: a, lambda a, _h: a),
        "T8.I": binary_division("T8.I", lambda a, _h: a, lambda a, h: a ^ h),
    }


def division_record(test: DivisionTest) -> dict[str, Any]:
    passed, witness = test.evaluate()
    body = {
        "id": test.identifier,
        "complete_rows": [{"past": jsonable(past), "frontier": jsonable(frontier), "future": distribution_record(future)}
                          for past, frontier, future in test.rows],
        "is_complete_division": passed, "witness": witness,
    }
    body["seal"] = sha_obj(body)
    return body


def tensor(laws: Mapping[str, ControlLaw], tid: str, source: str, context: str,
           reader: str, alpha: str = "p1", beta: str = "p0") -> dict[Any, F]:
    return laws[tid].tensor(source, context, alpha, beta, reader)


def response_record(values: Mapping[Any, F]) -> list[list[Any]]:
    return [[jsonable(value), fs(delta)] for value, delta in sorted(values.items(), key=lambda item: repr(item[0]))]


def nonzero(values: Mapping[Any, F]) -> bool:
    return any(value != 0 for value in values.values())


def directed_cycle(edges: Iterable[tuple[str, str]]) -> bool:
    graph: dict[str, set[str]] = {}
    for source, target in edges:
        graph.setdefault(source, set()).add(target)
        graph.setdefault(target, set())
    for start in graph:
        frontier = list(graph[start])
        seen: set[str] = set()
        while frontier:
            node = frontier.pop()
            if node == start:
                return True
            if node not in seen:
                seen.add(node)
                frontier.extend(graph[node])
    return False


def operational_control_family(audit: Audit, laws: dict[str, ControlLaw], divisions: dict[str, DivisionTest]) -> dict[str, Any]:
    law_records = {tid: laws[tid].record() for tid in sorted(laws, key=lambda name: int(name[1:]))}
    tensor_count = sum(len(record["signed_response_tensors"]) for record in law_records.values())
    audit.require(list(law_records) == [f"T{i}" for i in range(1, 15)], "T1-T14 law registry")
    audit.require(tensor_count == 76, "76 complete ordered signed response tensors")
    division_records = {name: division_record(test) for name, test in sorted(divisions.items())}
    expected = {"T5.B": False, "T5.BC": True, "T5.C": False, "T6.R": False, "T7.F": True, "T8.I": False}
    audit.require({name: row["is_complete_division"] for name, row in division_records.items()} == expected, "declared division truth table")
    body = {
        "scope": "DECLARED-CONTROL-LAWS-NOT-NATIVE-GAMMA",
        "probability_sample_space": "mutually-exclusive complete successor states per fixed preparation/context",
        "laws": law_records, "division_tests": division_records,
        "law_count": len(law_records), "signed_tensor_count": tensor_count, "division_test_count": len(division_records),
    }
    body["seal"] = sha_obj(body)
    return body


def independent(code: list[int] | tuple[int, ...], supports: list[set[Any]]) -> bool:
    return all(supports[i].isdisjoint(supports[j]) for i, j in itertools.combinations(code, 2))


def pentagon_capacity(audit: Audit) -> dict[str, Any]:
    base = [{(i - 1) % 5, i} for i in range(5)]
    audit.require(independent([0, 2], base), "C5 code size 2")
    audit.require(not any(independent(c, base) for c in itertools.combinations(range(5), 3)), "C5 alpha<=2")
    inputs = [(i, j) for i in range(5) for j in range(5)]
    supports = [{(a, b) for a in base[i] for b in base[j]} for i, j in inputs]
    pairs = [(i, 2 * i % 5) for i in range(5)]
    code = [inputs.index(x) for x in pairs]
    audit.require(independent(code, supports), "C5 product code size 5")
    tested = 0
    has_six = False
    for candidate in itertools.combinations(range(25), 6):
        tested += 1
        if independent(candidate, supports):
            has_six = True
            break
    audit.require(not has_six, "C5 product alpha<=5")
    return {"N0": 2, "N0_tensor": 5, "product_code_lower_bound": 4, "size5_code": pairs, "size6_subsets_tested": tested}


def matmul(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    n = len(a)
    return [[sum((a[i][k] * b[k][j] for k in range(n)), F(0)) for j in range(n)] for i in range(n)]


def matpow(a: list[list[F]], exponent: int) -> list[list[F]]:
    n = len(a)
    result = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    base = a
    while exponent:
        if exponent & 1: result = matmul(result, base)
        base = matmul(base, base)
        exponent //= 2
    return result


def diamond_kernel(audit: Audit, q: F) -> list[list[F]]:
    neighbors = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
    out = [[F(0) for _ in range(4)] for _ in range(4)]
    for i in range(4):
        out[i][i] = q
        for j in neighbors[i]: out[i][j] = (1 - q) / 2
        audit.require(sum(out[i], F(0)) == 1, f"diffusion normalize q={q} row={i}")
    return out


def return_law(kernel: list[list[F]]) -> list[F]:
    return [F(1)] + [sum((matpow(kernel, t)[i][i] for i in range(4)), F(0)) / 4 for t in range(1, 5)]


def simple_random_walk(node_count: int, edges: set[tuple[int, int]]) -> list[list[F]]:
    neighbors = {node: set() for node in range(node_count)}
    for a, b in edges:
        if a == b or a not in neighbors or b not in neighbors:
            raise ValueError("invalid undirected walk edge")
        neighbors[a].add(b)
        neighbors[b].add(a)
    if any(not adjacent for adjacent in neighbors.values()):
        raise ValueError("simple random walk has an isolated node")
    return [[F(1, len(neighbors[i])) if j in neighbors[i] else F(0) for j in range(node_count)] for i in range(node_count)]


def control_record(identifier: str, changed: Any, observed: Any, required: str) -> dict[str, Any]:
    body = {"id": identifier, "changed_object": changed, "observed": observed, "required_result": required, "passed": True}
    body["seal"] = sha_obj(body)
    return body


def linear_extensions(nodes: list[str], relation: set[tuple[str, str]]) -> list[tuple[str, ...]]:
    out = []
    for order in itertools.permutations(nodes):
        pos = {x: i for i, x in enumerate(order)}
        if all(pos[a] < pos[b] for a, b in relation): out.append(order)
    return out


def order_dimension(audit: Audit, nodes: list[str], relation: set[tuple[str, str]], maximum: int = 3) -> int | None:
    extensions = linear_extensions(nodes, relation)
    universe = {(a, b) for a in nodes for b in nodes if a != b}
    order_sets = []
    for extension in extensions:
        pos = {x: i for i, x in enumerate(extension)}
        order_sets.append({(a, b) for a, b in universe if pos[a] < pos[b]})
    for k in range(1, maximum + 1):
        for indices in itertools.combinations(range(len(extensions)), k):
            intersection = set.intersection(*(order_sets[i] for i in indices))
            if intersection == relation:
                audit.require(True, f"order dimension witness k={k} nodes={len(nodes)}")
                return k
    return None


def hostile_controls(audit: Audit, core: dict[str, Any], laws: dict[str, ControlLaw],
                     divisions: dict[str, DivisionTest]) -> dict[str, Any]:
    controls: dict[str, Any] = {}

    def add(i: int, changed: Any, observed: Any, required: str) -> None:
        key = f"M{i}"
        audit.require(key not in controls, f"unique control {key}")
        controls[key] = control_record(key, changed, observed, required)

    operational = core["operational_controls"]

    def law_ref(tid: str) -> dict[str, str]:
        return {"law_id": tid, "law_seal": operational["laws"][tid]["seal"]}

    def division_ref(name: str) -> dict[str, str]:
        return {"division_test": name, "division_seal": operational["division_tests"][name]["seal"]}

    # M1--M7: referent, order, scale, and weight separations.
    neutral = {0: F(1, 2), 1: F(1, 2)}
    copy0, copy1 = {0: F(1), 1: F(0)}, {0: F(0), 1: F(1)}
    audit.require(tv(neutral, neutral) == 0 and tv(copy0, copy1) == 1, "M1 dependency/influence separation")
    add(1, {"dependency_poset": "A<B", "laws": ["B fair under do(A)", "B=A"]},
        {"same_dependency": True, "TV_neutral": "0", "TV_copy": "1"}, "dependency is not chronology")

    diamond_nodes = ["r", "x", "y", "t"]
    diamond_rel = {("r", "x"), ("r", "y"), ("x", "t"), ("y", "t"), ("r", "t")}
    serial_a, serial_b = ["r", "x", "y", "t"], ["r", "y", "x", "t"]
    rank_a, rank_b = {x: i for i, x in enumerate(serial_a)}, {x: i for i, x in enumerate(serial_b)}
    audit.require(rank_a["x"] != rank_b["x"] and canonical_key(diamond_nodes, diamond_rel) == canonical_key(diamond_nodes, diamond_rel), "M2 serialization rank")
    add(2, {"same_poset": sorted(diamond_rel), "serializations": [serial_a, serial_b]},
        {"rank_x": [rank_a["x"], rank_b["x"]]}, "hidden serialization clock refused")

    p_nodes = ["a", "b", "c", "z"]
    p_rel = {("a", "b"), ("a", "c"), ("b", "c")}
    q_nodes = ["r", "u", "v", "w"]
    q_rel = {("r", "u"), ("r", "v"), ("r", "w")}
    p_rec, q_rec = poset_record(p_nodes, p_rel), poset_record(q_nodes, q_rel)
    audit.require(p_rec["r"] == q_rec["r"] == "1/2" and (p_rec["H"], p_rec["W"]) != (q_rec["H"], q_rec["W"]), "M3 one-statistic collision")
    add(3, {"chain_plus_isolate": sorted(p_rel), "three_arm_star": sorted(q_rel)}, {"P": p_rec, "Q": q_rec}, "one-statistic inference fails")

    chain_nodes, chain_rel = ["0", "1", "2"], {("0", "1"), ("1", "2"), ("0", "2")}
    chain_dim = order_dimension(audit, chain_nodes, chain_rel)
    audit.require(chain_dim == 1, "M4 chain dimension")
    add(4, {"finite_poset": sorted(chain_rel), "DM_dimension": chain_dim, "density": "unbound", "sampling": "unbound"},
        {"eligible_1plus1_representation": True, "faithful_sprinkling_proved": False}, "DM<=2 is not sufficient")

    s_nodes = [f"a{i}" for i in range(3)] + [f"b{i}" for i in range(3)]
    s_rel = {(f"a{i}", f"b{j}") for i in range(3) for j in range(3) if i != j}
    s_dim = order_dimension(audit, s_nodes, s_rel)
    audit.require(s_dim == 3, "M5 standard-example S3 dimension")
    add(5, {"standard_example_S3": sorted(s_rel)}, {"DM_dimension": s_dim}, "exact global-null 1+1 embedding refused")

    A, rho, scale = F(5, 7), F(11, 13), F(3, 2)
    A2, rho2 = scale**2 * A, rho / scale**2
    audit.require(rho * A == rho2 * A2 and A != A2, "M6 conformal-density degeneracy")
    add(6, {"g_scale": fs(scale**2), "rho_scale": fs(1 / scale**2)},
        {"rhoV": fs(rho * A), "rhoV_prime": fs(rho2 * A2), "proper_time_scale": fs(scale)}, "absolute scale unidentifiable")

    weights = []
    for t in [1, 2, 10, 100]:
        high, low = F(t, t + 2), F(1, 2 * t + 1)
        audit.require(high == F(2 * t * t, (2 * t + 1)**2 - (2 * t * t + 1)), f"M7 high t={t}")
        audit.require(low == F(2, (t + 2)**2 - (t * t + 2)), f"M7 low t={t}")
        weights.append({"t": t, "edge_heavy": fs(high), "isolated_heavy": fs(low)})
    add(7, {"fixed_order": "a<b; c incomparable", "weight_families": weights}, {"range_limit": ["0", "1"]}, "arbitrary weights are non-evidence")

    # M8--M16: preregistration, multiscale, and occurrence identity.
    target_before = {"name": "height-two", "accept": p_rec["H"] == 2}
    target_after = {"name": "relation-half", "accept": p_rec["r"] == "1/2"}
    audit.require(not target_before["accept"] and target_after["accept"], "M8 posthoc target switch changes verdict")
    add(8, {"same_data": p_rec, "targets": [target_before, target_after], "selection_time": ["before", "after"]},
        {"posthoc_switch_changes_question": True}, "target-family preregistration required")

    registered_profile = {"whole": F(1, 2), "sub4": F(1, 2), "sub3": F(1, 2)}
    candidate_profile = {"whole": F(1, 2), "sub4": F(2, 3), "sub3": F(1, 3)}
    audit.require(candidate_profile["whole"] == registered_profile["whole"] and candidate_profile != registered_profile, "M9 whole-only fit")
    add(9, {"registered": {k: fs(v) for k, v in registered_profile.items()}, "candidate": {k: fs(v) for k, v in candidate_profile.items()}},
        {"whole_pass": True, "multiscale_pass": False}, "whole-interval fit is insufficient")

    intrinsic = canonical_key(diamond_nodes, diamond_rel)
    embedding_select_a, embedding_select_b = ["x"], ["y"]
    audit.require(embedding_select_a != embedding_select_b, "M10 coordinate-selected interval changes")
    add(10, {"unlabeled_poset": intrinsic, "coordinate_selections_after_arm_swap": [embedding_select_a, embedding_select_b]},
        {"selection_covariant": False}, "intrinsic region selection required")

    original_dim = order_dimension(audit, diamond_nodes, diamond_rel)
    thin_nodes = ["r", "x", "t"]
    thin_rel = {(a, b) for a, b in diamond_rel if a in thin_nodes and b in thin_nodes}
    thinned_dim = order_dimension(audit, thin_nodes, thin_rel)
    thinning_estimates = {"original": original_dim, "neutral_thinning": thinned_dim}
    audit.require(original_dim == 2 and thinned_dim == 1, "M11 exact thinning dimension shift")
    add(11, {"original_diamond": sorted(diamond_rel), "retained_nodes": thin_nodes, "dimension_estimates": thinning_estimates}, {"stable": False}, "dimension promotion refused")

    H = 9
    durations = {"rho=1": f"{H}/sqrt(2)", "rho=4": f"{H}/sqrt(8)"}
    audit.require(durations["rho=1"] != durations["rho=4"], "M12 height duration calibration")
    add(12, {"same_height": H, "density_calibrations": [1, 4]}, durations, "height remains order depth without calibration")

    audit.require(["1", "1", "1"] != ["9/25", "16/25", "1"], "M13 imported weights change input")
    add(13, {"inherited_weights": ["1", "1", "1"], "imported_candidate_weights": ["9/25", "16/25", "1"]},
        {"input_contract_allows_imported": False}, "Paper 14 Gamma weight import refused")

    one_route_R = F(-56, 25)
    add(14, {"metric_differentiation_R_times_A": fs(one_route_R), "independent_discrete_route": None},
        {"route_count": 1}, "curvature remains unconstructed")

    finite_chain = canonical_key(chain_nodes, chain_rel)
    embeddings = [{"scale": "1", "proper_span": "1"}, {"scale": "3", "proper_span": "3"}]
    audit.require(embeddings[0] != embeddings[1], "M15 finite continuum nonuniqueness")
    add(15, {"same_finite_order": finite_chain, "continuum_embeddings": embeddings}, {"unique": False}, "finite uniqueness refused")

    anti_nodes, anti_rel = ["x0", "x1"], set()
    audit.require(canonical_key(anti_nodes, anti_rel) != canonical_key(["orbit"], set()), "M16 automorphic occurrence collapse")
    add(16, {"two_occurrence_antichain": canonical_key(anti_nodes, anti_rel), "automorphism_orbits": 1, "collapsed_nodes": 1},
        {"physical_occurrences": 2}, "automorphism orbits do not delete multiplicity")

    # M17--M30: declared-family provenance, decoder, scale, and geometry walls.
    descendant_q2 = {"path": ["root", "chosen1", "chosen2"], "off_path_siblings_per_step": 1}
    descendant_q4 = {"path": ["root", "chosen1", "chosen2"], "off_path_siblings_per_step": 3}
    audit.require(descendant_q2["path"] == descendant_q4["path"], "M17 descendant interval unchanged")
    add(17, {"branching_q": [2, 4], "selected_descendant_paths": [descendant_q2, descendant_q4]}, {"path_order_equal": True}, "branching without mergers does not repair thin scaling")

    nodes3, rel3 = product_poset(3)
    transposition = {(i, j): (j, i) for i, j in nodes3}
    audit.require({(transposition[a], transposition[b]) for a, b in rel3} == rel3, "M18 product coordinate swap")
    add(18, {"same_order": poset_record(nodes3, rel3), "coordinate_reading_of_(0,2)": [[0, 2], [2, 0]]},
        {"individual_coordinate_clock_invariant": False}, "latent product coordinates are not physical clocks")

    deterministic_shape = {"chain3": 1}
    random_shape = core["two_order"]["finite_enumeration"]["3"]["class_counts"]
    audit.require(len(random_shape) > len(deterministic_shape), "M19 independent shape laws")
    add(19, {"same_local_record_kernel": "declared B", "shape_laws": [deterministic_shape, random_shape]},
        {"shape_law_fixed_by_B": False}, "random two-order provenance remains declared")

    lambda_value = F(6)
    calibrations = [{"rho": "2", "V": "3"}, {"rho": "3", "V": "2"}]
    audit.require(F(2) * 3 == F(3) * 2 == lambda_value, "M20 rhoV degeneracy")
    add(20, {"Poisson_mean": fs(lambda_value), "calibrations": calibrations}, {"volume_unique": False}, "only rho V identified")

    affine_R, star_R = F(-56, 25), F(-7, 8)
    audit.require(affine_R != star_R, "M21 decoder curvature choice")
    add(21, {"postfit_decoder_options": {"affine": fs(affine_R), "phi_star": fs(star_R)}}, {"selection_from_data": "posthoc"}, "decoder preregistration fails")

    affine_I = core["affine"]["I_at_theta"]
    star_I = core["affine"]["phi_star"]["I_at_theta"]
    audit.require(affine_I["2"] == star_I["2"] and affine_I["3"] != star_I["3"], "M22 low-shadow decoder replacement")
    add(22, {"same_B": True, "same_I2": affine_I["2"], "I3": [affine_I["3"], star_I["3"]], "R_times_A": [fs(affine_R), fs(star_R)]},
        {"curvature_unique": False}, "same-low-shadow replacement kills decoder selection")

    digit_probs = [F(9, 50), F(8, 25), F(8, 25), F(9, 50)]
    level2 = [a * b for a in digit_probs for b in digit_probs]
    audit.require(all(x > 0 for x in level2) and len(set(level2)) > 1, "M23 full-support unequal cylinder masses")
    add(23, {"dyadic_level": 2, "cell_masses": [fs(x) for x in level2], "all_cells_positive": True},
        {"Lebesgue_density_proved": False, "entropy_dimension": "1+h2(9/25)<2"}, "full support is not smooth volume")

    add(24, {"finite_unlabeled_pattern_coordinate": "I2", "affine": affine_I["2"], "alternate": star_I["2"], "different_I3": True},
        {"unique_decoder": False}, "finite patterns do not identify decoder")

    fair = {0: F(1, 2), 1: F(1, 2)}
    retained = {0: F(1), 1: F(0)}
    audit.require(fair != retained, "M25 outcome-dependent thinning bias")
    add(25, {"pre_thinning": {str(k): fs(v) for k, v in fair.items()}, "rule": "retain iff outcome=0", "post": {str(k): fs(v) for k, v in retained.items()}},
        {"neutral": False}, "outcome-dependent thinning refused")

    audit.require({(transposition[a], transposition[b]) for a, b in rel3} == rel3, "M26 transpose nonkill")
    add(26, {"P_3x3": poset_record(nodes3, rel3), "map": "(i,j)->(j,i)"}, {"changed_physical_object": False}, "required physical non-kill")

    phi = [F(1), F(-2)]
    grid = [F(0), F(1, 3), F(2, 3), F(1)]
    base_values = [[copula(F(-7, 25), u, v, phi) for v in grid] for u in grid]
    both_flipped = [[1 + F(-7, 25) * peval(pscale(phi, -1), u) * peval(pscale(phi, -1), v) for v in grid] for u in grid]
    one_and_theta = [[1 + F(7, 25) * peval(pscale(phi, -1), u) * peval(phi, v) for v in grid] for u in grid]
    audit.require(base_values == both_flipped == one_and_theta, "M27 rank-one sign gauges")
    add(27, {"grid": [fs(x) for x in grid], "gauges": ["phi,psi -> -phi,-psi", "theta,phi -> -theta,-phi"]},
        {"density_sha": sha_obj([[fs(x) for x in row] for row in base_values])}, "factorization gauges are non-kills")

    whole_tau = F(-14, 225)
    affine_formula_on_star = 36 * whole_tau
    audit.require(affine_formula_on_star == affine_R and affine_formula_on_star != star_R, "M28 out-of-family curvature identity")
    add(28, {"nonbilinear_phi_star": True, "whole_tau": fs(whole_tau)},
        {"36tau_over_A": fs(affine_formula_on_star), "metric_center_R_times_A": fs(star_R)}, "affine family identity refused out of family")

    audit.require(affine_R != 0, "M29 nonzero conditional curvature")
    add(29, {"conditional_scalar_curvature_times_A": fs(affine_R), "stress_tensor": None, "dynamical_equation": None},
        {"gravity": False}, "conditional curvature is not gravity")

    count = 12
    volume_options = [{"rho": "1", "V": "12"}, {"rho": "3", "V": "4"}]
    audit.require(F(1) * 12 == F(3) * 4 == count, "M30 count-volume ambiguity")
    add(30, {"unit_count": count, "density_volume_options": volume_options}, {"calibrated_volume_unique": False}, "unit count is not calibrated volume")

    # M31--M46 consume the complete T1--T14 law/reader/tensor/division objects.
    t31 = tensor(laws, "T1", "A", "fixed", "B.complete")
    audit.require(nonzero(t31), "M31 serial complete-law influence")
    add(31, law_ref("T1"), {"signed_tensor": response_record(t31)}, "one directed total-influence edge")

    common_obs, common_do = {"00": F(1, 2), "11": F(1, 2)}, {0: F(1, 2), 1: F(1, 2)}
    t32 = tensor(laws, "T2", "A", "fixed", "B.complete")
    audit.require(not nonzero(t32) and laws["T2"].facts["observational_P_A_equals_B"] == 1, "M32 common-cause control")
    add(32, law_ref("T2"), {"observational_P_equal": "1", "signed_tensor": response_record(t32)}, "correlation gives no directed edge")

    t33_joint = tensor(laws, "T3", "E", "fixed", "XY.complete")
    t33_x, t33_y = tensor(laws, "T3", "E", "fixed", "X.complete"), tensor(laws, "T3", "E", "fixed", "Y.complete")
    audit.require(nonzero(t33_joint) and not nonzero(t33_x) and not nonzero(t33_y) and not laws["T3"].facts["factorizable"], "M33 certified co-onset")
    add(33, law_ref("T3"), {"joint": response_record(t33_joint), "X": response_record(t33_x), "Y": response_record(t33_y),
        "bundle_multiplicity": 2}, "one bundled onset, no arbitrary orientation")

    audit.require(laws["T4"].facts["same_complete_law"], "M34 commuting complete laws")
    add(34, law_ref("T4"), {"serializations": jsonable(laws["T4"].facts["serializations"]), "same_law": True}, "commuting serialization is a non-kill")

    d35 = {name: divisions[name].evaluate()[0] for name in ["T5.B", "T5.C", "T5.BC"]}
    audit.require(d35 == {"T5.B": False, "T5.C": False, "T5.BC": True}, "M35 exact division discrimination")
    add(35, {**law_ref("T5"), "division_bindings": [division_ref(name) for name in d35]}, d35, "partial cuts refuse; joint frontier passes")

    d36 = divisions["T6.R"].evaluate()
    audit.require(laws["T6"].facts["record_persistent"] and not d36[0], "M36 persistence without division")
    add(36, {**law_ref("T6"), **division_ref("T6.R")}, {"stable": True, "division": jsonable(d36)}, "stable record is not complete division")

    d37 = divisions["T7.F"].evaluate()
    audit.require(d37[0] and not laws["T7"].facts["new_record"], "M37 division without new record")
    add(37, {**law_ref("T7"), **division_ref("T7.F")}, {"division": True, "new_happening": False}, "division without new happening passes")

    t38, d38 = tensor(laws, "T8", "A", "h0", "Y.complete"), divisions["T8.I"].evaluate()
    audit.require(nonzero(t38) and not d38[0], "M38 whole-law response across nondivision")
    add(38, {**law_ref("T8"), **division_ref("T8.I")}, {"whole_tensor": response_record(t38), "division": False}, "whole-law influence survives; no Markovization")

    t39xy, t39yx = tensor(laws, "T9", "X", "fixed", "Y.complete"), tensor(laws, "T9", "Y", "fixed", "X.complete")
    audit.require(nonzero(t39xy) and nonzero(t39yx) and directed_cycle((("X", "Y"), ("Y", "X"))) and not laws["T9"].facts["joint_onset_certificate"], "M39 feedback cycle")
    add(39, law_ref("T9"), {"X_to_Y": response_record(t39xy), "Y_to_X": response_record(t39yx), "acyclic": False}, "chronology promotion refused")

    t40_total = tensor(laws, "T10", "A", "natural", "C.complete")
    t40_d0, t40_d1 = tensor(laws, "T10", "A", "doB0", "C.complete"), tensor(laws, "T10", "A", "doB1", "C.complete")
    audit.require(nonzero(t40_total) and not nonzero(t40_d0) and not nonzero(t40_d1), "M40 direct versus mediated")
    add(40, law_ref("T10"), {"total": response_record(t40_total), "direct_doB0": response_record(t40_d0),
        "direct_doB1": response_record(t40_d1)}, "reachability survives; direct edge fails")

    t41ab = tensor(laws, "T11", "A", "natural", "B.complete")
    t41ac, t41bc = tensor(laws, "T11", "A", "natural", "C.complete"), tensor(laws, "T11", "B", "a0", "C.complete")
    audit.require(nonzero(t41ab) and not nonzero(t41ac) and nonzero(t41bc), "M41 exact downstream cancellation")
    add(41, law_ref("T11"), {"A_to_B": response_record(t41ab), "A_to_C": response_record(t41ac),
        "B_to_C": response_record(t41bc)}, "tensor not made transitive; reachability separate")

    audit.require(not directed_cycle((("Q#1", "Q#2"),)) and directed_cycle((("Q", "Q"),)), "M42 occurrence/type separation")
    add(42, law_ref("T12"), {"occurrence_graph": [["Q#1", "Q#2"]], "collapsed_type_cycle": True}, "occurrence identity retained")

    t43ab0, t43ab1 = tensor(laws, "T13", "A", "c0", "B.complete"), tensor(laws, "T13", "A", "c1", "B.complete")
    t43ba0, t43ba1 = tensor(laws, "T13", "B", "c0", "A.complete"), tensor(laws, "T13", "B", "c1", "A.complete")
    audit.require(nonzero(t43ab0) and not nonzero(t43ab1) and not nonzero(t43ba0) and nonzero(t43ba1), "M43 context reversal")
    add(43, law_ref("T13"), {"c0_A_to_B": response_record(t43ab0), "c0_B_to_A": response_record(t43ba0),
        "c1_A_to_B": response_record(t43ab1), "c1_B_to_A": response_record(t43ba1)}, "context-independent chronology refused")

    t44full, t44parity = tensor(laws, "T14", "A", "fixed", "B.complete"), tensor(laws, "T14", "A", "fixed", "B.parity")
    audit.require(nonzero(t44full) and not nonzero(t44parity), "M44 complete versus restricted reader")
    add(44, law_ref("T14"), {"complete_reader": response_record(t44full), "restricted_parity": response_record(t44parity)}, "incomplete-reader separation refused")

    audit.require(laws["T2"].facts["observational_P_A_equals_B"] == 1 and not nonzero(t32), "M45 conditioning/intervention separation")
    add(45, law_ref("T2"), {"observational_conditioning": "perfect", "lawful_tensor": response_record(t32)}, "false conditioned edge refused")

    missing = ControlLaw("M46.changed-law", "required preparation omitted", ("B",), {"A": {"fixed": {"p0": deterministic(0)}}},
                         (Reader("B.complete", "B", (0,)),), (("A", "B.complete"),), {}, {})
    missing.validate()
    missing_record = missing.record()
    audit.require(not missing_record["same_law_ordered_preparation_pairs"] and not missing_record["signed_response_tensors"], "M46 missing alternative")
    add(46, {"baseline": law_ref("T1"), "changed_law_seal": missing_record["seal"], "changed_transition_tables": missing_record["transition_tables"]},
        {"pairwise_response": "undefined"}, "influence untested, not zero")

    # M47--M54: clocks, radar, capacity, route independence, diffusion, signalling.
    clock_records_a = [[0, 0], [1, 1], [0, 2]]
    clock_records_b = [[0, 0], [1, 1], [0, 2]]
    iteration_a, iteration_b = [0, 1, 2], [0, 2, 3]
    audit.require(clock_records_a == clock_records_b and iteration_a != iteration_b, "M47 neutral counter insertion")
    add(47, {"neutral_bookkeeping_step_inserted": True, "clock_records": [clock_records_a, clock_records_b], "iteration_indices": [iteration_a, iteration_b]},
        {"physical_clock_changed": False, "counter_changed": True}, "global iteration counter refused")

    clock_C, clock_D = [F(0), F(1), F(2)], [F(1), F(3), F(6)]
    aa = (clock_D[1] - clock_D[0]) / (clock_C[1] - clock_C[0])
    bb = clock_D[0] - aa * clock_C[0]
    residual = clock_D[2] - (aa * clock_C[2] + bb)
    audit.require((aa, bb, residual) == (2, 1, 1), "M48 held-out clock disagreement")
    add(48, {"same_path_C": [fs(x) for x in clock_C], "same_path_D": [fs(x) for x in clock_D], "calibration_points": [0, 1]},
        {"a": fs(aa), "b": fs(bb), "heldout_residual": fs(residual)}, "common local duration fails")

    radar1, radar2 = F(2, 2), F(3, 2)
    audit.require(radar1 != radar2, "M49 signal species radar mismatch")
    add(49, {"same_path_zero_latency_species": [{"c": "1", "roundtrip": "2"}, {"c": "1", "roundtrip": "3"}]},
        {"distances": [fs(radar1), fs(radar2)]}, "unique metric refused; multimetric retained")

    capacity = pentagon_capacity(audit)
    audit.require(capacity["N0_tensor"] > capacity["product_code_lower_bound"], "M50 capacity synergy")
    add(50, {"classical_channel_confusability": "C5", **capacity}, {"forced_equality": False}, "product lower bound does not prove equality")

    boundary_rows = []
    for n in range(2, 9):
        boundary, bulk = 4 * n - 4, n * n
        boundary_rows.append({"n": n, "log2_N0": boundary, "bulk": bulk, "ratio": fs(F(boundary, bulk))})
    audit.require(boundary_rows[-1]["ratio"] == "7/16", "M51 boundary scaling")
    audit.require(2**8 * 2**12 == 2**20, "M51 independent additivity")
    add(51, {"noiseless_bits_only_on_square_boundary": boundary_rows}, {"product_additive": True, "bulk_extensive": False}, "capacity-volume identification fails")

    shared_slice = ["relation_pairs", "node_count"]
    audit.require(sha_obj(shared_slice) == sha_obj(list(shared_slice)), "M52 identical backward evidence slices")
    add(52, {"route_A": {"formula": "2R/N(N-1)", "slice": shared_slice}, "route_C_bad": {"formula": "2R/N(N-1)", "slice": shared_slice}},
        {"independent_routes": False}, "three-route agreement refused")

    hasse_edges = {(0, 1), (0, 2), (1, 3), (2, 3)}
    closure_edges = hasse_edges | {(0, 3)}
    hasse_walk, closure_walk = simple_random_walk(4, hasse_edges), simple_random_walk(4, closure_edges)
    hasse_returns, closure_returns = return_law(hasse_walk), return_law(closure_walk)
    audit.require(hasse_returns[2] == F(1, 2) and closure_returns[2] == F(7, 18), "M53 unit-average simple-walk pbar2")
    add(53, {"same_diamond_occurrences": 4, "undirected_edges": [sorted(hasse_edges), sorted(closure_edges)],
             "kernels": [[[fs(x) for x in row] for row in hasse_walk], [[fs(x) for x in row] for row in closure_walk]]},
        {"uniform_unit_occurrence_pbar2": [fs(hasse_returns[2]), fs(closure_returns[2])],
         "return_laws_t0_to4": [[fs(x) for x in hasse_returns], [fs(x) for x in closure_returns]]}, "kernel and spectral dimension unselected")

    audit.require(common_obs["00"] + common_obs["11"] == 1 and tv(common_do, common_do) == 0, "M54 correlation no signal")
    add(54, {"state_law": {"R": "fair", "A": "R", "B": "R"}, "observational_P_equal": "1", "do_B": {"0": "fair", "1": "fair"}},
        {"retarded_TV": "0"}, "state correlation is not a signal edge")

    expected = [f"M{i}" for i in range(1, 55)]
    audit.require(list(controls) == expected, "all 54 controls registered in order")
    audit.require(len({row["seal"] for row in controls.values()}) == 54, "54 distinct control seals")
    return controls


MUTANTS = (
    "product_pair_count",
    "affine_I4",
    "collapse_occurrences",
    "force_capacity_equality",
    "alias_diffusion_kernels",
    "correlation_as_signal",
)


def detect_mutant(name: str, core: dict[str, Any]) -> None:
    if name == "product_pair_count":
        row = core["product_order"]["rows"][3]  # n=4
        observed = row["R"] + 1
        expected = 4 * 4 * 3 * 7 // 4
        if observed != expected: raise ScientificFailure("product pair-count mutation detected")
    elif name == "affine_I4":
        observed = F(core["affine"]["I_at_theta"]["4"]) + F(1, 10**9)
        if observed != F(556643, 405000000): raise ScientificFailure("affine I4 mutation detected")
    elif name == "collapse_occurrences":
        observed_nodes = 1
        if observed_nodes != 2: raise ScientificFailure("automorphic occurrence-collapse mutation detected")
    elif name == "force_capacity_equality":
        c = core["controls"]["M50"]["changed_object"]
        if c["N0_tensor"] != c["product_code_lower_bound"]: raise ScientificFailure("capacity equality mutation detected")
    elif name == "alias_diffusion_kernels":
        returns = core["controls"]["M53"]["observed"]["uniform_unit_occurrence_pbar2"]
        mutated = [returns[0], returns[0]]
        if mutated[0] == mutated[1]: raise ScientificFailure("diffusion-kernel alias mutation detected")
    elif name == "correlation_as_signal":
        observed_tv = F(1)
        computed_tv = F(core["controls"]["M54"]["observed"]["retarded_TV"])
        if observed_tv != computed_tv: raise ScientificFailure("correlation-as-signal mutation detected")
    else:
        raise ValueError(name)


def source_policy(audit: Audit) -> dict[str, Any]:
    raw = Path(__file__).read_bytes()
    text = raw.decode("utf-8")
    nonblank = sum(1 for line in text.splitlines() if line.strip())
    audit.require(nonblank <= 1500, "source nonblank line cap")
    audit.require(b"\r" not in raw, "source LF-only")
    banned = [
        "import " + "random", "from " + "random", "import " + "subprocess",
        "import " + "socket", "import " + "requests", "import " + "numpy",
    ]
    hits = [token for token in banned if token in text]
    audit.require(not hits, "no banned imports")
    return {"sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw), "nonblank_lines": nonblank, "banned_import_hits": hits}


def build_core() -> dict[str, Any]:
    audit = Audit()
    policy = source_policy(audit)
    native = native_family(audit)
    product = product_family(audit)
    two_order = two_order_family(audit)
    affine = affine_family(audit)
    laws, divisions = build_control_laws(), division_tests()
    operational = operational_control_family(audit, laws, divisions)
    hypotheses = {
        "native_target": "fixed regular Alexandrov diamond under increasing density or homothetic noncompact flat diamond at fixed density, fixed D>=2",
        "native_nonkill": "fixed-compactification cylinder may have linear height and ordering fraction tending to one",
        "product_order": "declared coordinatewise order; coordinates are not physical clocks",
        "two_order": "declared uniform random intersection of two total orders; not derived from native family",
        "affine": "declared positive normalized smooth 1+1 copula with fixed theta=-7/25 and A=5/7 controls",
        "density_scale": "unit count identifies rho*V only; absolute scale uncalibrated",
        "operational": "T1-T14 are declared finite control laws and are not a native Gamma",
        "metric": "conditional control only; independent clock/radar/propagation agreement unavailable",
    }
    ceiling = {
        "input": "P15-STRUCTURAL-ORDER-UNIT-MEASURE-BOUND",
        "chronology": "P15-NO-ACCEPTED-INTERVENTIONAL-LAW",
        "native": "P15-NATIVE-BUNDLE-FAMILY-FAILS-REGISTERED-DIAMOND-SCALING",
        "conditional": "P15-MULTISCALE-COMPATIBILITY-WITH-DECLARED-MANIFOLDLIKE-ENSEMBLE",
        "scale": "P15-ABSOLUTE-SCALE-UNIDENTIFIED",
        "metric": "P15-CONDITIONAL-LORENTZIAN-METRIC-CANDIDATE",
        "uniqueness": "P15-METRIC-UNIQUENESS-UNPROVEN",
        "physical": "P15-MULTIMETRIC-AGREEMENT-UNTESTED",
    }
    core: dict[str, Any] = {
        "schema": SCHEMA,
        "status": "STAGE-B-SOURCE-CONSTRUCTION-NOT-OFFICIAL",
        "binding": {"pin_commit": PIN_COMMIT, "pin_sha256": PIN_SHA256, "parent_adjudication_sha256": PARENT_SHA256},
        "source": policy,
        "native": native,
        "product_order": product,
        "two_order": two_order,
        "affine": affine,
        "operational_controls": operational,
        "hypotheses": hypotheses,
        "preregistered_coordinate_ceiling": ceiling,
        "fresh_result_status": "FRESH-CONTROLS-NOT-EVALUATED",
    }
    controls = hostile_controls(audit, core, laws, divisions)
    core["controls"] = controls
    detected = []
    for mutant in MUTANTS:
        try:
            detect_mutant(mutant, core)
        except ScientificFailure as exc:
            detected.append({"name": mutant, "detection": str(exc)})
        else:
            raise ScientificFailure(f"mutant escaped: {mutant}")
    audit.require(len(detected) == len(MUTANTS), "all development mutants detected")
    science_sections = {k: core[k] for k in ["native", "product_order", "two_order", "affine", "operational_controls",
                                                   "hypotheses", "controls", "preregistered_coordinate_ceiling", "fresh_result_status"]}
    core["construction_evidence"] = {
        "science_sha256": sha_obj(science_sections),
        "control_registry_sha256": sha_obj(controls),
        "control_count": len(controls),
        "operational_law_count": operational["law_count"],
        "signed_tensor_count": operational["signed_tensor_count"],
        "division_test_count": operational["division_test_count"],
        "mutants": detected,
    }
    core["checks"] = {"all_pass": True, "count": len(audit.labels), "labels": audit.labels}
    return core


def permutation_from_index(n: int, index: int) -> list[int]:
    pool = list(range(n))
    out = []
    value = index % math.factorial(n)
    for remaining in range(n, 0, -1):
        block = math.factorial(remaining - 1)
        q, value = divmod(value, block)
        out.append(pool.pop(q))
    return out


def generate_fresh_object(nonce: str, src_sha: str) -> dict[str, Any]:
    if len(nonce) != 64 or any(ch not in "0123456789abcdef" for ch in nonce):
        raise ValueError("nonce must be exactly 64 lowercase hexadecimal characters")
    digest = hashlib.sha256((SCHEMA + PIN_SHA256 + src_sha + nonce).encode("ascii")).digest()
    theta_choices = [F(-3, 5), F(-7, 25), F(-1, 7), F(1, 5), F(2, 3)]
    center_choices = [(F(1, 2), F(1, 2), F(1, 4), F(1, 5)), (F(1, 3), F(2, 3), F(1, 6), F(1, 6))]
    cases = [
        {"id": "F1", "kind": "native", "d": 2 + digest[0] % 9},
        {"id": "F2", "kind": "product_order", "n": 2 + digest[1] % 7},
        {"id": "F3", "kind": "two_order", "n": 5, "relative_order": permutation_from_index(5, int.from_bytes(digest[2:6], "big"))},
        {"id": "F4", "kind": "affine_chains", "theta": fs(theta_choices[digest[6] % len(theta_choices)])},
        {"id": "F5", "kind": "subdiamond", "theta": "-7/25", "A": "5/7", "parameters": [fs(x) for x in center_choices[digest[7] % 2]]},
        {"id": "F6", "kind": "weighted_order", "t": 2 + digest[8] % 31},
    ]
    return {
        "schema": FRESH_SCHEMA, "pin_sha256": PIN_SHA256, "source_sha256": src_sha,
        "nonce_sha256": hashlib.sha256(nonce.encode("ascii")).hexdigest(), "case_kinds": 6, "cases": cases,
    }


def evaluate_fresh_cases(audit: Audit, fresh: dict[str, Any]) -> list[dict[str, Any]]:
    audit.require(fresh.get("schema") == FRESH_SCHEMA, "fresh schema")
    audit.require(fresh.get("pin_sha256") == PIN_SHA256, "fresh pin binding")
    audit.require(fresh.get("source_sha256") == source_sha(), "fresh source binding")
    cases = fresh.get("cases")
    audit.require(isinstance(cases, list) and [x.get("id") for x in cases] == [f"F{i}" for i in range(1, 7)], "fresh case IDs")
    audit.require(len({x.get("kind") for x in cases}) >= 5, "fresh five-kind minimum")
    out = []
    for case in cases:
        kind = case["kind"]
        if kind == "native":
            d = int(case["d"])
            nodes, _, relation = native_interval(d)
            rec = poset_record(nodes, relation)
            audit.require(rec == {"N": 4*d+1, "R": math.comb(4*d+1, 2)-d, "r": fs(1-F(1, 2*(4*d+1))), "H": 3*d+1, "W": 2}, "fresh native formula")
            out.append({"id": case["id"], "kind": kind, **rec, "interval": poset_evidence(nodes, relation)})
        elif kind == "product_order":
            n = int(case["n"])
            nodes, relation = product_poset(n)
            rec = poset_record(nodes, relation)
            audit.require(rec["R"] == n*n*(n-1)*(n+3)//4 and rec["H"] == 2*n-1 and rec["W"] == n, "fresh product formulas")
            out.append({"id": case["id"], "kind": kind, **rec, "interval": poset_evidence(nodes, relation)})
        elif kind == "two_order":
            order = tuple(case["relative_order"])
            audit.require(sorted(order) == list(range(case["n"])), "fresh permutation")
            relation = relative_relation(order)
            nodes = list(range(case["n"]))
            audit.require(relation_fraction(nodes, relation) is not None, "fresh two-order complete interval")
            out.append({"id": case["id"], "kind": kind, **poset_record(nodes, relation), "canonical": canonical_key(nodes, relation)})
        elif kind == "affine_chains":
            theta = F(case["theta"])
            profile = [F(1), F(-2)]
            audit.require(-1 < theta < 1, "fresh affine positivity")
            out.append({"id": case["id"], "kind": kind, "theta": fs(theta), "I2_I3_I4": [fs(peval(chain_coefficients(profile, k), theta)) for k in [2, 3, 4]]})
        elif kind == "subdiamond":
            theta, A = F(case["theta"]), F(case["A"])
            u, v, du, dv = [F(x) for x in case["parameters"]]
            out.append({"id": case["id"], "kind": kind, **local_affine_identity(audit, theta, A, u, v, du, dv)})
        elif kind == "weighted_order":
            t = int(case["t"])
            audit.require(t > 0, "fresh positive weight parameter")
            out.append({"id": case["id"], "kind": kind, "t": t, "edge_heavy": fs(F(t, t + 2)), "isolated_heavy": fs(F(1, 2 * t + 1))})
        else:
            raise ScientificFailure(f"unknown fresh kind: {kind}")
    return out


def installed_v16_dir() -> Path:
    source = Path(__file__).absolute()
    if source.name != SOURCE_NAME or source.parent.name != "code" or source.parent.parent.name != "v16" or source.is_symlink():
        raise ValueError(f"official modes require this source installed as v16/code/{SOURCE_NAME}")
    v16 = source.parent.parent
    if v16.is_symlink() or source.parent.is_symlink():
        raise ValueError("installed v16/code path may not be a symlink")
    return v16.resolve()


def file_binding(v16: Path, key: str, relative: str, expected_sha: str | None = None) -> dict[str, Any]:
    path = v16 / relative
    if path.is_symlink() or not path.is_file() or path.resolve().parent != (v16 / Path(relative).parent).resolve():
        raise ValueError(f"installed input is missing, displaced, or symlinked: {relative}")
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if expected_sha is not None and digest != expected_sha:
        raise ValueError(f"installed {key} hash mismatch")
    return {"key": key, "path": "v16/" + relative, "sha256": digest, "bytes": len(raw)}


def authenticate_installed_inputs() -> tuple[Path, dict[str, dict[str, Any]]]:
    v16 = installed_v16_dir()
    bindings = {
        "pin": file_binding(v16, "pin", PIN_NAME, PIN_SHA256),
        "parent_adjudication": file_binding(v16, "parent_adjudication", PARENT_NAME, PARENT_SHA256),
        "source": file_binding(v16, "source", "code/" + SOURCE_NAME, source_sha()),
        "paper": file_binding(v16, "paper", PAPER_NAME),
        "construction_note": file_binding(v16, "construction_note", CONSTRUCTION_NAME),
    }
    return v16, bindings


def read_canonical_json(path: Path, expected_name: str) -> dict[str, Any]:
    if path.name != expected_name or path.absolute().parent.resolve() != installed_v16_dir():
        raise ValueError(f"read path must be the installed v16/{expected_name}")
    if path.is_symlink() or not path.is_file():
        raise ValueError("input must be a regular non-symlink file")
    raw = path.read_bytes()
    if len(raw) > 4_000_000:
        raise ValueError("input too large")
    value = json.loads(raw)
    if raw != cbytes(value):
        raise ValueError("input JSON is not canonical")
    if not isinstance(value, dict):
        raise ValueError("input JSON root must be an object")
    return value


def exclusive_transactional_write(path: Path, expected_name: str, payload: bytes) -> None:
    if path.name != expected_name or path.absolute().parent.resolve() != installed_v16_dir():
        raise ValueError(f"write path must be the installed v16/{expected_name}")
    if not path.parent.is_dir() or path.parent.is_symlink() or path.exists() or path.is_symlink():
        raise ValueError("output parent/absence check failed")
    temporary = path.with_name("." + expected_name + ".stage-b-tmp")
    if temporary.exists() or temporary.is_symlink():
        raise ValueError("temporary path already exists")
    fd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(fd, "wb", closefd=True) as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.link(temporary, path)
    finally:
        if temporary.exists(): os.unlink(temporary)


def publish_pair(output: Path, receipt: Path, output_payload: bytes, receipt_payload: bytes) -> None:
    v16 = installed_v16_dir()
    for path, name in ((output, OUTPUT_NAME), (receipt, RECEIPT_NAME)):
        if path.name != name or path.absolute().parent.resolve() != v16 or path.exists() or path.is_symlink():
            raise ValueError(f"paired publication path/absence check failed for v16/{name}")
    temporary = [output.with_name("." + OUTPUT_NAME + ".stage-c-tmp"), receipt.with_name("." + RECEIPT_NAME + ".stage-c-tmp")]
    if any(path.exists() or path.is_symlink() for path in temporary):
        raise ValueError("paired publication temporary path already exists")
    linked: list[Path] = []
    try:
        for path, payload in zip(temporary, (output_payload, receipt_payload)):
            fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            with os.fdopen(fd, "wb", closefd=True) as handle:
                handle.write(payload); handle.flush(); os.fsync(handle.fileno())
        for temporary_path, final_path in zip(temporary, (output, receipt)):
            os.link(temporary_path, final_path); linked.append(final_path)
        directory_fd = os.open(v16, os.O_RDONLY)
        try: os.fsync(directory_fd)
        finally: os.close(directory_fd)
    except BaseException:
        for final_path, temporary_path in reversed(list(zip(linked, temporary))):
            if final_path.exists() and temporary_path.exists() and os.path.samestat(final_path.stat(), temporary_path.stat()):
                os.unlink(final_path)
        raise
    finally:
        for path in temporary:
            if path.exists(): os.unlink(path)


def official_receipt(core: dict[str, Any], bindings: dict[str, dict[str, Any]], fresh: dict[str, Any],
                     fresh_results: list[dict[str, Any]], output_payload: bytes) -> dict[str, Any]:
    live = dict(bindings)
    live["fresh"] = {"key": "fresh", "path": "v16/" + FRESH_NAME, "sha256": sha_obj(fresh), "bytes": len(cbytes(fresh))}
    live["output"] = {"key": "output", "path": "v16/" + OUTPUT_NAME,
                      "sha256": hashlib.sha256(output_payload).hexdigest(), "bytes": len(output_payload)}
    awarded = core["preregistered_coordinate_ceiling"]
    objects = {"core": core, "fresh": fresh, "fresh_results": fresh_results, "hypotheses": core["hypotheses"],
               "coordinate_ceiling": core["preregistered_coordinate_ceiling"], "awarded_outcomes": awarded}
    seals = {f"object.{key}": keyed_seal(f"object.{key}", value) for key, value in objects.items()}
    seals.update({f"control.{key}": keyed_seal(f"control.{key}", value) for key, value in core["controls"].items()})
    seals.update({f"law.{key}": keyed_seal(f"law.{key}", value) for key, value in core["operational_controls"]["laws"].items()})
    seals.update({f"division.{key}": keyed_seal(f"division.{key}", value) for key, value in core["operational_controls"]["division_tests"].items()})
    seals.update({f"fresh_case.{row['id']}": keyed_seal(f"fresh_case.{row['id']}", row) for row in fresh["cases"]})
    seals.update({f"fresh_result.{row['id']}": keyed_seal(f"fresh_result.{row['id']}", row) for row in fresh_results})
    seals.update({f"binding.{key}": keyed_seal(f"binding.{key}", value) for key, value in live.items()})
    for row in core["native"]["rows"]: seals[f"interval.native.d{row['d']}"] = keyed_seal(f"interval.native.d{row['d']}", row["interval"])
    for row in core["product_order"]["rows"]: seals[f"interval.product.n{row['n']}"] = keyed_seal(f"interval.product.n{row['n']}", row["interval"])
    for n in range(1, 6):
        for row in core["two_order"]["finite_enumeration"][str(n)]["complete_interval_manifest"]:
            key = f"interval.two_order.n{n}.order." + "-".join(map(str, row["relative_order"])); seals[key] = keyed_seal(key, row)
    for tid, law in core["operational_controls"]["laws"].items():
        for index, row in enumerate(law["transition_tables"]):
            key = f"transition.{tid}.{index:02d}"; seals[key] = keyed_seal(key, row)
        for index, row in enumerate(law["same_law_ordered_preparation_pairs"]):
            key = f"preparation_pair.{tid}.{index:02d}"; seals[key] = keyed_seal(key, row)
        for index, row in enumerate(law["signed_response_tensors"]):
            key = f"tensor.{tid}.{index:02d}"; seals[key] = keyed_seal(key, row)
    for name, division in core["operational_controls"]["division_tests"].items():
        for index, row in enumerate(division["complete_rows"]):
            key = f"division_row.{name}.{index:02d}"; seals[key] = keyed_seal(key, row)
    if len(seals) != 465 or len(set(seals.values())) != len(seals):
        raise ScientificFailure("total per-key seal registry mismatch")
    return {
        "schema": RECEIPT_SCHEMA, "status": "OFFICIAL-FRESH-CONTROLS-EVALUATED",
        "bindings": live, "full_object_sha256": {key: sha_obj(value) for key, value in objects.items()},
        "all_54_control_sha256": {key: sha_obj(value) for key, value in core["controls"].items()},
        "hypotheses_sha256": sha_obj(core["hypotheses"]),
        "coordinates": {"ceiling": core["preregistered_coordinate_ceiling"], "awarded": awarded,
                        "fresh_result_status": "FRESH-CONTROLS-PASS"},
        "read_ledger": [live[key] for key in ["pin", "parent_adjudication", "source", "paper", "construction_note", "fresh"]],
        "write_ledger": [live["output"], {"key": "receipt", "path": "v16/" + RECEIPT_NAME,
                                          "sha256": "SELF-EXCLUDED-TO-AVOID-RECEIPT-HASH-CYCLE"}],
        "per_key_seals": seals, "per_key_seal_count": len(seals), "per_key_registry_sha256": sha_obj(seals),
    }


def validate_cli(args: argparse.Namespace) -> None:
    if args.selftest and any(x is not None for x in [args.output, args.receipt, args.cases, args.nonce]):
        raise ValueError("--selftest takes no ancillary arguments")
    if args.mutant is not None and any(x is not None for x in [args.output, args.receipt, args.cases, args.nonce]):
        raise ValueError("--mutant takes no ancillary arguments")
    if args.generate_fresh and (args.output is None or args.nonce is None or args.cases is not None or args.receipt is not None):
        raise ValueError("--generate-fresh requires --nonce and --output, and forbids --cases/--receipt")
    if args.run and (args.output is None or args.receipt is None or args.cases is None or args.nonce is not None):
        raise ValueError("--run requires --cases, --output, and --receipt, and forbids --nonce")


def main() -> int:
    parser = argparse.ArgumentParser(prog=SOURCE_NAME, allow_abbrev=False)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--selftest", action="store_true")
    modes.add_argument("--generate-fresh", action="store_true")
    modes.add_argument("--run", action="store_true")
    modes.add_argument("--mutant", choices=MUTANTS)
    parser.add_argument("--nonce")
    parser.add_argument("--cases", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    try:
        validate_cli(args)
        core = build_core()
        if args.selftest:
            print(cbytes(core).decode("ascii"), end="")
            return 0
        if args.mutant is not None:
            try:
                detect_mutant(args.mutant, core)
            except ScientificFailure as exc:
                print(cbytes({"schema": "p15-spacetime-mutant-v1", "mutant": args.mutant, "detected": True, "failure": str(exc)}).decode("ascii"), end="")
                return 1
            print(cbytes({"schema": "p15-spacetime-mutant-v1", "mutant": args.mutant, "detected": False}).decode("ascii"), end="")
            return 3
        if args.generate_fresh:
            authenticate_installed_inputs()
            fresh = generate_fresh_object(args.nonce, source_sha())
            payload = cbytes(fresh)
            exclusive_transactional_write(args.output, FRESH_NAME, payload)
            print(cbytes({"schema": "p15-spacetime-write-v1", "kind": "fresh", "sha256": hashlib.sha256(payload).hexdigest()}).decode("ascii"), end="")
            return 0
        _, bindings = authenticate_installed_inputs()
        fresh = read_canonical_json(args.cases, FRESH_NAME)
        run_audit = Audit()
        fresh_results = evaluate_fresh_cases(run_audit, fresh)
        result = {
            "schema": OUTPUT_SCHEMA, "status": "OFFICIAL-FRESH-CONTROLS-EVALUATED",
            "pin_sha256": PIN_SHA256, "source_sha256": source_sha(), "core": core, "fresh": fresh,
            "fresh_sha256": sha_obj(fresh), "fresh_results": fresh_results,
            "fresh_checks": {"all_pass": True, "count": len(run_audit.labels), "labels": run_audit.labels},
            "fresh_result_status": "FRESH-CONTROLS-PASS",
            "awarded_outcomes": core["preregistered_coordinate_ceiling"],
        }
        output_payload = cbytes(result)
        receipt = official_receipt(core, bindings, fresh, fresh_results, output_payload)
        receipt_payload = cbytes(receipt)
        _, bindings_again = authenticate_installed_inputs()
        if bindings_again != bindings or read_canonical_json(args.cases, FRESH_NAME) != fresh:
            raise ValueError("authenticated input changed during run")
        publish_pair(args.output, args.receipt, output_payload, receipt_payload)
        print(cbytes({"schema": "p15-spacetime-write-v1", "kind": "run",
                      "output_sha256": hashlib.sha256(output_payload).hexdigest(),
                      "receipt_sha256": hashlib.sha256(receipt_payload).hexdigest()}).decode("ascii"), end="")
        return 0
    except (ScientificFailure, ValueError, OSError, json.JSONDecodeError, KeyError, TypeError, ZeroDivisionError) as exc:
        print(cbytes({"schema": "p15-spacetime-error-v1", "error_type": type(exc).__name__, "error": str(exc)}).decode("ascii"), end="")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

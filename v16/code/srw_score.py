#!/usr/bin/env python3
"""Frozen physical scorer for SRW Paper 4.

The fixture is data-only and carries no expected result or verdict.  This
scorer imports the already frozen generic exact core and renders every result
artifact from one in-memory measurement object.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
import math
import os
import re
import sys
import tempfile
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any, Mapping, Sequence

from srw_core import (
    GQ,
    I,
    ONE,
    PHASES,
    Q,
    ZERO,
    DictionaryCandidate,
    FiberSpec,
    GateLedger,
    RelGraph,
    RewriteSpan,
    adjoint,
    canonical_json,
    circle,
    coherent_screen,
    common_commutant_contains,
    cycle_holonomy,
    cycle_orbits,
    dictionary_candidates,
    direct_sum,
    graph_port_neighbor,
    graph_probe_probability,
    growth,
    gtext,
    identity,
    is_isometry,
    kron,
    matmul,
    matrix,
    matvec,
    permutation_matrix,
    probability,
    qtext,
    reflection,
    row_for_label,
    scalar,
    sha256_bytes,
    sha256_path,
    shape,
    support,
    support_compatible,
    two_route_probability,
    zero,
)


ROOT = Path(__file__).resolve().parents[2]
CODE_DIR = Path(__file__).resolve().parent
CORE_PATH = CODE_DIR / "srw_core.py"
FIXTURE_PATH = CODE_DIR / "srw_fixture.json"
PIN_PATH = ROOT / "v16" / "note-srw-pin.md"
PPR_FIXTURE_PATH = CODE_DIR / "ppr_fixture.json"
PPR_RECEIPT_PATH = CODE_DIR / "ppr_receipt.json"
DEFAULT_OUTPUT = CODE_DIR / "srw_output.txt"
DEFAULT_RECEIPT = CODE_DIR / "srw_receipt.json"
DEFAULT_PAPER = ROOT / "v16" / "paper-04-support-rewrite-weld.md"

EXPECTED_FIXTURE_SHA256 = "e40650f04c60635e68fd91938dbba201afec6e426c2e1cfaa0b4f4d8dcefd2e3"
ORIGINAL_CORE_SHA256 = "783f71589b2c1d9cee3b20ccf864ae372b480affcf6df4a4181befd5b55f0137"
EXPECTED_REPAIRED_CORE_SHA256 = "dd902c37375f87185f693f8b1e4b22ba3ddeaf9de5641e5d7d951cbba1d3c585"
BANNED_FIXTURE_KEYS = ("expected", "result", "verdict", "outcome")


MUTANTS = (
    "anchor-corrupt",
    "legacy-product-move",
    "dictionary-drop",
    "dictionary-preplant",
    "persistence-spelling",
    "graph-probe-row",
    "swap-call-gauge",
    "future-reactivation-drop",
    "support-equality",
    "forbidden-support",
    "port-role-erase",
    "functor-dimension-type",
    "internal-call-gauge",
    "internal-reactivation-drop",
    "relabel-break",
    "recurrence-site-drift",
    "angle-lock-constructor",
    "reciprocity-assume",
    "reciprocity-remove",
    "phase-frame-break",
    "runtime-scalar-leak",
    "holonomy-flatten",
    "cycle-call-gauge",
    "result-count-type",
    "verdict-flip",
    "transcript-forge",
    "seal-after-write",
)


EXPECTED_MUTANT_GATE = {
    "anchor-corrupt": "SRW-ANCHORS",
    "legacy-product-move": "SRW-LEGACY-IDENTITIES",
    "dictionary-drop": "SRW-DICTIONARY-CENSUS",
    "dictionary-preplant": "SRW-DICTIONARY-CENSUS",
    "persistence-spelling": "SRW-PERSISTENCE-NATURALITY",
    "graph-probe-row": "SRW-GRAPH-FUTURE",
    "swap-call-gauge": "SRW-CONTINUATION-CLASSIFICATION",
    "future-reactivation-drop": "SRW-CONTINUATION-COMMUTANT",
    "support-equality": "SRW-ACTUAL-SUPPORT",
    "forbidden-support": "SRW-FORBIDDEN-SUPPORT",
    "port-role-erase": "SRW-REFERENT-TYPES",
    "functor-dimension-type": "SRW-FIBER-DIMENSIONS",
    "internal-call-gauge": "SRW-INTERNAL-CLASSIFICATION",
    "internal-reactivation-drop": "SRW-INTERNAL-REACTIVATION",
    "relabel-break": "SRW-BUNDLE-NATURALITY",
    "recurrence-site-drift": "SRW-RECURRING-LOCALITY",
    "angle-lock-constructor": "SRW-INDEPENDENT-ANGLE-VARIETY",
    "reciprocity-assume": "SRW-RECIPROCITY-LOCUS",
    "reciprocity-remove": "SRW-RECIPROCAL-LEFT-INVERSE",
    "phase-frame-break": "SRW-PHASE-GAUGE",
    "runtime-scalar-leak": "SRW-RUNTIME-GAUSSIAN-EXACT",
    "holonomy-flatten": "SRW-HOLONOMY-SCREEN",
    "cycle-call-gauge": "SRW-PHASE-ORBITS",
    "result-count-type": "SRW-PAPER-BINDINGS",
    "verdict-flip": "SRW-OUTCOME-COMPARATOR",
    "transcript-forge": "SRW-TRANSCRIPT-RECONCILIATION",
    "seal-after-write": "SRW-PREWRITE-SEALS",
}


def read_bytes(path: Path, read_log: list[str]) -> bytes:
    resolved = path.resolve()
    try:
        rel = resolved.relative_to(ROOT.resolve()).as_posix()
    except ValueError as exc:
        raise ValueError(f"runtime read outside repository: {resolved}") from exc
    read_log.append(rel)
    return resolved.read_bytes()


def read_json(path: Path, read_log: list[str]) -> dict[str, Any]:
    return json.loads(read_bytes(path, read_log))


def recursive_keys(obj: Any) -> tuple[str, ...]:
    keys: list[str] = []
    if isinstance(obj, dict):
        for key, value in obj.items():
            keys.append(str(key))
            keys.extend(recursive_keys(value))
    elif isinstance(obj, list):
        for value in obj:
            keys.extend(recursive_keys(value))
    return tuple(keys)


def mtext(a: tuple[tuple[GQ, ...], ...]) -> list[list[str]]:
    return [[gtext(x) for x in row] for row in a]


def vtext(v: tuple[GQ, ...]) -> list[str]:
    return [gtext(x) for x in v]


def graph_from_data(data: Mapping[str, Any], erase_port_role: bool = False) -> RelGraph:
    internal = tuple(data["internal"])
    ports = tuple(data["ports"])
    if erase_port_role:
        internal = internal + ports
        ports = ()
    return RelGraph(
        internal=internal,
        ports=ports,
        edges=frozenset(frozenset(edge) for edge in data["edges"]),
    )


def rename_candidate(candidate: DictionaryCandidate, rename: Mapping[str, str]) -> DictionaryCandidate:
    return DictionaryCandidate(
        tuple(rename.get(label, label) for label in candidate.source_by_col),
        tuple(rename.get(label, label) for label in candidate.target_by_row),
    )


def projector(n: int, index: int) -> tuple[tuple[GQ, ...], ...]:
    return tuple(tuple(ONE if r == c == index else ZERO for c in range(n)) for r in range(n))


def parse_outcomes(pin_text: str) -> tuple[str, ...]:
    start = pin_text.index("## Pre-registered outcomes")
    end = pin_text.index("## Kill conditions", start)
    section = pin_text[start:end]
    words = re.findall(r"^\d+\. `((?:SRW-)[A-Z0-9-]+)`", section, flags=re.MULTILINE)
    if len(words) != len(set(words)) or not words:
        raise ValueError("outcome vocabulary is empty or duplicated")
    return tuple(words)


def extract_ppr_screens(receipt: Mapping[str, Any]) -> list[list[str]]:
    laws = receipt["payload"]["measurements"]["relational_wedge"]["laws"]
    return [law["heldout_screen_probabilities"] for law in laws]


def independent_outcome_indices(vector: tuple[int, ...]) -> tuple[int, ...]:
    """Independent numeric comparator: no measurement builder or verdict literal."""

    (
        typed_referent,
        legacy_ok,
        endpoint_missing,
        same_map_span_count,
        current_signature_count,
        future_signature_count,
        bundle_ok,
        moving_angle_count,
        reciprocal_image_ok,
        free_record_weight_count,
    ) = vector
    if not typed_referent:
        return (0,)
    if not legacy_ok:
        return (1,)
    selected: list[int] = []
    if endpoint_missing and same_map_span_count > 1:
        selected.append(2)
    if current_signature_count == 1 and future_signature_count > 1:
        selected.append(3)
    if bundle_ok and moving_angle_count > 1:
        selected.append(5)
    if reciprocal_image_ok and free_record_weight_count > 1:
        selected.append(6)
    return tuple(selected)


def builder_outcome_indices(flags: Mapping[str, bool]) -> tuple[int, ...]:
    if not flags["typed_referent"]:
        return (0,)
    if not flags["legacy_ok"]:
        return (1,)
    chosen: list[int] = []
    if flags["map_only_refuted"]:
        chosen.append(2)
    if flags["dictionary_future_physical"]:
        chosen.append(3)
    if flags["bundle_unselected"]:
        chosen.append(5)
    if flags["reciprocal_weights_free"]:
        chosen.append(6)
    return tuple(chosen)


def claims_from_measurements(m: Mapping[str, Any]) -> list[dict[str, str]]:
    d = m["dictionary"]
    s = m["support"]
    f = m["fibers"]
    a = m["angles"]
    p = m["phase"]
    return [
        {
            "id": "C1",
            "text": f"The inherited anonymous matrices satisfy {m['legacy']['identity_count']} of {m['legacy']['identity_count']} registered exact weld identities.",
        },
        {
            "id": "C2",
            "text": f"The exhaustive dictionary census has {d['candidate_count']} candidates, {d['support_survivor_count']} support-compatible survivors, and {d['current_signature_count']} current-observable signature.",
        },
        {
            "id": "C3",
            "text": f"The two support-compatible dictionaries give graph-local probe probabilities {d['graph_probe_probabilities']} and persistence-probe probabilities {d['persistence_probe_probabilities']}.",
        },
        {
            "id": "C4",
            "text": f"Across the registered rational circle rows, the allowed pattern has {s['allowed_count']} entries while a zero-coupling endpoint has {s['endpoint_actual_count']} actual entries.",
        },
        {
            "id": "C5",
            "text": f"The same anonymous map admits {m['bundle']['same_map_span_count']} typed persistence spans with different ancestry.",
        },
        {
            "id": "C6",
            "text": f"The four declared fiber constructions have source-to-target dimensions {f['dimension_pairs']}; only {f['legacy_exact_count']} has the inherited anonymous shape without enlargement.",
        },
        {
            "id": "C7",
            "text": f"The exact growth/recombiner grid contains {a['transport_pair_count']} independently varied pairs and {a['transport_screen_count']} distinct calibrated screens.",
        },
        {
            "id": "C8",
            "text": f"Recurring-type locality leaves a {a['full_moduli_dimension']}-parameter local modulus family before reciprocity and a {a['reciprocal_moduli_dimension']}-parameter family after reciprocal reconvergence, because recorded-successor weights remain free.",
        },
        {
            "id": "C9",
            "text": f"Reciprocity fixes the eraser on the reached image at {a['reciprocal_pair_count']} of {a['transport_pair_count']} registered grid pairs, while the null-direction extension remains unobserved by the inverse equation.",
        },
        {
            "id": "C10",
            "text": f"The finite phase census has {p['connection_count']} connections in {p['orbit_count']} gauge orbits, with orbit sizes {p['orbit_sizes']} and screens {p['screens']}.",
        },
        {
            "id": "C11",
            "text": f"The machine-selected registered findings are {m['classification']['findings']}.",
        },
        {
            "id": "C12",
            "text": "The finite construction selects neither the complete configuration catalogue nor the physical coupling values.",
        },
    ]


def render_paper(m: Mapping[str, Any], claims: Sequence[Mapping[str, str]], references: Mapping[str, str]) -> bytes:
    c = {row["id"]: row["text"] for row in claims}
    findings = m["classification"]["findings"]
    graph_probs = m["dictionary"]["graph_probe_probabilities"]
    persistence_probs = m["dictionary"]["persistence_probe_probabilities"]
    dimension_pairs = m["fibers"]["dimension_pairs"]
    screens = m["phase"]["screens"]
    text = rf"""# One successor object, but not one anonymous map

Status: **GREEN-UNREVIEWED CANDIDATE**. This finite exact investigation has
not undergone its separately frozen hostile-review process.

## Result

Relational change and process transport can be components of one typed
successor law, but they cannot in general be recovered from one anonymous
matrix. The correct finite object is a relational rewrite arrow together with
the transport it carries. Its global form is a block-sparse operator over a
fixed catalogue of possible complete relational configurations. The realized
graph may change even though that global catalogue is part of the model.

The stronger statement fails for three independent reasons. A transition
support relates configurations across a step whereas spatial adjacency is
internal to a configuration; a zero coupling can remove an actual matrix entry
without removing the kinematically typed rewrite; and one source direction can
feed both a persisting target and a created target, so support does not say
which target inherits the old identity.

The exact registered findings are `{findings}`.

## The idea without technical language

Think of a machine that can redraw its own circuit while carrying a signal.
One table says which redraw occurred: which components survived, which were
created, and how the new circuit is connected. Another table says how the
signal passed through that redraw. These tables belong to one physical event,
but the numerical signal table does not by itself contain the entire wiring
diagram or the ancestry of every component.

This distinction matters because two labellings that look identical to today's
meter can behave differently when a later meter is attached. In the finite
example, the two surviving labellings agree on every old contraction but give
future probabilities {graph_probs}. Calling their difference gauge would hide
a real prediction.

There is nevertheless a genuine unification: one global catalogue contains
all allowed relational configurations, and one law has blocks connecting the
corresponding process spaces. Geometry tells each block what kind of rewrite it
is; its entries tell how process content is transported. What remains open is
why this catalogue and these coupling values, rather than others, are realized
in nature.

## 1. Configuration ontology and changing geometry

Barandes treats the configuration space as a fixed ingredient and constructs a
configuration basis indexed by its complete configurations. That does not
require a fixed realized spacetime. A dynamical-geometry extension can take a
complete configuration to include the current relational graph and matter
content. The meta-catalogue of possible graphs is fixed while the actual graph
changes from one successor to another.

Accordingly, let

$$
\mathcal H=\bigoplus_G \mathcal H_G,
\qquad
\Theta=\sum_{{G,G'}} \Theta_{{G'\leftarrow G}},
$$

where each block is typed by a relational rewrite from $G$ to $G'$. This is
close in form to attaching quantum data to a discrete causal structure, but
the present construction neither assumes a causal set nor derives spacetime.
Typed graph-rewrite spans are standard machinery for distinguishing preserved
and created graph material; their use here is bookkeeping, not a claimed new
graph-transformation theorem.

The special fixture uses a one-excitation sector, so a basis direction can be
labelled by an internal vertex. That equality is sector-specific. In a general
model, the Hilbert dimension counts complete configurations in the selected
sector, not vertices.

## 2. Why support is not geometry

For the growth branch,

$$
V(x,z)=
\begin{{pmatrix}}
x&0\\
0&1\\
z&0
\end{{pmatrix}},
\qquad x^2+z^2=1.
$$

Its entries are transitions from an initial basis to a later basis. The target
graph's edges instead relate two target vertices. Those are different types of
ordered pair and cannot be identified by their zero patterns.

At a generic point the allowed and actual patterns coincide. At $z=0$, the
creation entry vanishes while the declared rewrite remains in the kinematic
family. Therefore actual support is at most the active part of a declared
grammar; it is not the grammar itself.

More decisively, the same $V$ supports two valid ancestry spans: either the
first target fed from $a$ persists and the third is new, or those ancestry
roles are interchanged. The numerical map cannot choose between them. A
rewrite span or an equivalent complete-history label must carry that fact if
future dynamics may use it.

{c['C4']}

{c['C5']}

## 3. The inherited numerical coincidence is exact

The dimension-changing map and common-future continuations obey

$$
U_\alpha=R\oplus 0,
\qquad
U_\beta V=RJ\oplus 0.
$$

The direction $n=(4/5,0,-3/5)^T$ is missed by $V^\dagger$ but sent by
$U_\beta$ to the later record direction. Thus one-step absence is not stable
gauge.

{c['C1']}

This proves an exact common realization exists after a dictionary is supplied.
It does not make that dictionary or the rewrite recoverable from anonymous
matrix entries.

## 4. The dictionary is presently blind and future-physical

All source and target bijections give an exhaustive finite census.

{c['C2']}

The two survivors differ only by interchanging the targets named persistent
$a'$ and new $c$. Existing contractions never consume those semantic names,
so their current signatures agree. A new probe is then defined without row
numbers: it reads the unique internal neighbor of the typed boundary port.
The corresponding exact probabilities are {graph_probs}. A separate
persistence-sensitive probe gives {persistence_probs}.

{c['C3']}

The swap also fails the common-commutant test once those futures are admitted.
It is therefore not continuation-stable gauge in the registered grammar. This
does not select which dictionary nature uses; it shows that calibration or an
independently typed persistence map is required.

## 5. The corrected weld

A lawful local successor is represented by

$$
(r,\Theta_r): (G,\mathcal H_G)\longrightarrow(G',\mathcal H_{{G'}}),
$$

with $r$ a relational rewrite and $\Theta_r$ its process transport. Relabeling
acts on both components, composition composes both, and an external readout is
computed from the resulting graph and fiber state. This is one typed law arrow,
not two machines exchanging a classical control bit.

The map-only proposal would follow only if the representation
$r\mapsto\Theta_r$ were faithful and if the kinematic support and persistence
data were recoverable. The two-span counterexample proves that faithfulness is
not automatic.

## 6. The carrier is derived only after a sector is chosen

The fixture computes, rather than assigns, every fiber dimension.

{c['C6']}

The dimension pairs are {dimension_pairs}. The one-excitation vertex sector
reproduces the inherited two-to-three shape. Tensoring with a two-valued
internal degree gives a four-to-six isometry. Adding the boundary port as an
idle stabilized factor gives a three-to-four isometry. The edge-excitation
sector reads the same graphs but remains two-to-two.

These are not four equally complete physical theories. They prove a narrower
point: the graph alone does not select the fiber functor or its internal
multiplicity. A currently blind internal bit becomes observable under the
registered internal probe, so it cannot be declared gauge merely because a
coarser algebra ignores it. Particle species remain entirely unconstructed.

## 7. Locality, coupling moduli, and reciprocity

Write $(x,z)$ for growth, $(u,v)$ for coherent reconvergence, and $(r,s)$ for
weights of mutually exclusive recorded successors. Completeness gives three
separate circle equations. Recurring-vertex locality forces repeated vertices
of each same type to reuse their own pair; it supplies no equation between
differently typed vertices.

{c['C7']}

The coherent screen is

$$
p_0=(xu+zv)^2,
\qquad
p_1=(-xv+zu)^2.
$$

It moves over the admissible product family. Thus safety, covariance, and
recurrence do not identify the numerical couplings.

There is one principled reduction. If a growth is unrecorded and a later local
move is required to erase it exactly, the eraser must be a left inverse on the
reached image. For unit vectors, $xu+zv=1$ implies

$$
(x-u)^2+(z-v)^2=0,
$$

so the reconvergence row equals the adjoint growth row there. Extensions on
the orthogonal, unreached direction remain free unless later continuations see
them. This is creation–erasure reciprocity, not a rule for probabilities of
different durable successors.

{c['C8']}

{c['C9']}

Consequently, the repeated `3/5,4/5` numerals can be one coupling only when the
two appearances are independently shown to be inverse legs of the same
unrecorded local process. Numeral reuse alone has no selecting force.

## 8. Boundary gauge and loop content

Composition-compatible frame changes alter open-edge representatives while
leaving the product around a closed physical route unchanged. The complete
fourth-root census gives:

{c['C10']}

The screen values are {screens}. This establishes, at the finite phase group,
the expected distinction: frame data are representation, while closed-cycle
content can affect interference. It is a transport-holonomy result, not a
metric-curvature or gravity result.

## 9. What this changes ontologically

The strongest defensible ontology is now:

- one actual history of complete matter–relation configurations;
- one fixed meta-catalogue of possibilities, still unselected;
- one typed transition law over that catalogue;
- relational rewrite and process transport as the base and fiber components
  of each law arrow;
- records as continuation-stable distinctions; and
- Hamiltonians, fields, wave functions, and actions as possible
  representations of selected recurring sectors, not primitive additions.

The construction does not yet provide event-selection weights, the complete
catalogue, an actualization mechanism, backreaction calibrated as gravity, a
continuum or Lorentz limit, QFT, a vacuum, particles, constants, or deviations
from established physics.

{c['C11']}

{c['C12']}

## 10. Exact result bindings

The generated claim identifiers are `C1` through `C12`; each corresponding
sentence appears once in the section where it is used. The fixture contains no
expected result or verdict field, and all substantive arithmetic is exact over
$\mathbb Q(i)$.

## Relation to previous work

Barandes supplies the fixed configuration catalogue, configuration basis, and
transition-potential dictionary used as the ontological starting point; the
present delta is to let complete configurations contain relational geometries
and to type the resulting block transports. Double-pushout graph rewriting is
a precedent for carrying preserved and created material in a rewrite interface.
Quantum causal histories are a precedent for attaching finite quantum
structures and maps to discrete relational or causal data. None of these
sources selects this paper's catalogue or couplings.

- Jacob A. Barandes, *Quantum Systems as Indivisible Stochastic Processes*
  (2026), [arXiv:2507.21192]({references['barandes']}).
- Robert Söldner and Detlef Plump, *Formalising the Double-Pushout Approach to
  Graph Transformation* (2023), [arXiv:2312.15641]({references['dpo']}).
- Eli Hawkins, Fotini Markopoulou, and Hanno Sahlmann, *Evolution in Quantum
  Causal Histories*, *Classical and Quantum Gravity* **20** (2003) 3839,
  [arXiv:hep-th/0302111]({references['qch']}).
"""
    return text.encode("utf-8")


def parse_transcript_rows(data: bytes) -> Counter[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for line in data.decode("utf-8").splitlines():
        if line.startswith("[PASS] "):
            name, evidence = line[len("[PASS] ") :].split(" :: ", 1)
            rows.append((name, evidence))
    return Counter(rows)


def render_transcript(payload: Mapping[str, Any], seal_manifest: Mapping[str, Any] | None = None) -> bytes:
    m = payload["measurements"]
    lines = [
        "SRW PHYSICAL EXACT INVESTIGATION",
        f"FINDINGS {payload['primary']}",
        f"GATES {len(payload['gates'])}/{len(payload['gates'])} PASS",
        f"LEGACY identities={m['legacy']['identity_count']}",
        f"DICTIONARY candidates={m['dictionary']['candidate_count']} support={m['dictionary']['support_survivor_count']} current_signatures={m['dictionary']['current_signature_count']} graph_future={m['dictionary']['graph_probe_probabilities']}",
        f"SUPPORT allowed={m['support']['allowed_count']} endpoint={m['support']['endpoint_actual_count']} spans={m['bundle']['same_map_span_count']}",
        f"FIBERS dimensions={m['fibers']['dimension_pairs']} legacy_exact={m['fibers']['legacy_exact_count']}",
        f"ANGLES pairs={m['angles']['transport_pair_count']} screens={m['angles']['transport_screen_count']} reciprocal={m['angles']['reciprocal_pair_count']} full_dim={m['angles']['full_moduli_dimension']} reduced_dim={m['angles']['reciprocal_moduli_dimension']}",
        f"PHASE connections={m['phase']['connection_count']} orbits={m['phase']['orbit_count']} sizes={m['phase']['orbit_sizes']} screens={m['phase']['screens']}",
    ]
    lines.extend(f"[PASS] {row['gate']} :: {row['evidence']}" for row in payload["gates"])
    if seal_manifest is not None:
        lines.append(f"SEALS sealed={len(seal_manifest['sealed'])} unsealed={seal_manifest['unsealed']}")
    return ("\n".join(lines) + "\n").encode("utf-8")


def atomic_write_three(paths_and_data: Sequence[tuple[Path, bytes]]) -> None:
    for target, _ in paths_and_data:
        if target.exists():
            raise FileExistsError(f"refusing to overwrite {target}")
        target.parent.mkdir(parents=True, exist_ok=True)
    staged: list[tuple[Path, Path, bytes]] = []
    try:
        for target, data in paths_and_data:
            fd, name = tempfile.mkstemp(prefix=f".{target.name}.", dir=target.parent)
            stage = Path(name)
            with os.fdopen(fd, "wb") as handle:
                handle.write(data)
                handle.flush()
                os.fsync(handle.fileno())
            if stage.read_bytes() != data:
                raise IOError("staged bytes differ")
            staged.append((stage, target, data))
        for stage, target, _ in staged:
            os.replace(stage, target)
        for _, target, data in staged:
            if target.read_bytes() != data:
                raise IOError("promoted bytes differ")
    finally:
        for stage, _, _ in staged:
            if stage.exists():
                stage.unlink()


def solve(mutant: str | None = None) -> tuple[dict[str, Any], bytes, bytes]:
    read_log: list[str] = []
    fixture_bytes = read_bytes(FIXTURE_PATH, read_log)
    fixture = json.loads(fixture_bytes)
    core_bytes = read_bytes(CORE_PATH, read_log)
    pin_bytes = read_bytes(PIN_PATH, read_log)
    ppr_fixture_bytes = read_bytes(PPR_FIXTURE_PATH, read_log)
    ppr_receipt_bytes = read_bytes(PPR_RECEIPT_PATH, read_log)
    scorer_bytes = read_bytes(Path(__file__), read_log)
    ppr_fixture = json.loads(ppr_fixture_bytes)
    ppr_receipt = json.loads(ppr_receipt_bytes)
    pin_text = pin_bytes.decode("utf-8")

    ledger = GateLedger()
    anchors = fixture["anchors"]
    observed_anchor = sha256_bytes(core_bytes)
    if mutant == "anchor-corrupt":
        observed_anchor = "0" * len(observed_anchor)
    fixture_sha = sha256_bytes(fixture_bytes)
    anchor_ok = (
        fixture_sha == EXPECTED_FIXTURE_SHA256
        and anchors["core_sha256"] == ORIGINAL_CORE_SHA256
        and observed_anchor == EXPECTED_REPAIRED_CORE_SHA256
        and sha256_bytes(pin_bytes) == anchors["pin_sha256"]
        and sha256_bytes(ppr_fixture_bytes) == anchors["ppr_fixture_sha256"]
        and sha256_bytes(ppr_receipt_bytes) == anchors["ppr_receipt_sha256"]
    )
    ledger.check(
        "SRW-ANCHORS",
        anchor_ok,
        f"fixture={fixture_sha} core={sha256_bytes(core_bytes)} pin={sha256_bytes(pin_bytes)}",
    )

    all_fixture_keys = recursive_keys(fixture)
    bad_keys = tuple(
        key for key in all_fixture_keys if any(banned in key.lower() for banned in BANNED_FIXTURE_KEYS)
    )
    outcomes = parse_outcomes(pin_text)
    ledger.check(
        "SRW-FIXTURE-AND-VOCABULARY",
        not bad_keys and len(outcomes) == len(set(outcomes)),
        f"forbidden_keys={list(bad_keys)} vocabulary_count={len(outcomes)}",
    )

    legacy_data = fixture["legacy"]
    mats = {name: matrix(rows) for name, rows in legacy_data["matrices"].items()}
    vg = mats["Vgrow"]
    ub = mats["Ubeta"]
    ua = mats["Ualpha"]
    rmat = mats["R"]
    jmat = mats["J"]
    legacy_product = matmul(ub, vg)
    if mutant == "legacy-product-move":
        legacy_product = tuple(
            tuple(value + (ONE if rr == cc == 0 else ZERO) for cc, value in enumerate(row))
            for rr, row in enumerate(legacy_product)
        )
    rj_zero = tuple(matmul(rmat, jmat)) + (tuple(ZERO for _ in range(shape(rmat)[1])),)
    r_zero = tuple(rmat) + (tuple(ZERO for _ in range(shape(rmat)[1])),)
    null = tuple(scalar(x) for x in legacy_data["null_direction"])
    vg_dag_null = matvec(adjoint(vg), null)
    ub_null = matvec(ub, null)
    ppr_screens = extract_ppr_screens(ppr_receipt)
    identity_checks = (
        support(vg) == frozenset({(0, 0), (1, 1), (2, 0)}),
        ua == r_zero,
        legacy_product == rj_zero,
        vg_dag_null == (ZERO, ZERO),
        ub_null == (ZERO, ZERO, ONE),
        ppr_screens == [["49/625", "576/625"], ["0", "1"]],
    )
    ledger.check(
        "SRW-LEGACY-IDENTITIES",
        all(identity_checks),
        f"checks={sum(identity_checks)}/{len(identity_checks)} screens={ppr_screens}",
    )

    rewrite_data = fixture["rewrite"]
    erase_port_role = mutant == "port-role-erase"
    source_graph = graph_from_data(rewrite_data["source_graph"], erase_port_role)
    target_graph = graph_from_data(rewrite_data["target_graph"], erase_port_role)
    allowed = frozenset(tuple(pair) for pair in rewrite_data["allowed_entries"])
    primary_span = RewriteSpan(
        source_graph,
        target_graph,
        tuple(tuple(pair) for pair in rewrite_data["persistence"]),
        frozenset(rewrite_data["created"]),
        allowed,
    )
    alternate_span = RewriteSpan(
        source_graph,
        target_graph,
        tuple(tuple(pair) for pair in rewrite_data["alternate_persistence"]),
        frozenset(rewrite_data["alternate_created"]),
        allowed,
    )
    typed_referent = True
    try:
        primary_span.validate()
        alternate_span.validate()
        if rewrite_data["probe_port"] not in target_graph.ports:
            typed_referent = False
        if set(source_graph.internal) != set(rewrite_data["source_basis_labels"]):
            typed_referent = False
        if set(target_graph.internal) != set(rewrite_data["target_basis_labels"]):
            typed_referent = False
    except ValueError:
        typed_referent = False
    ledger.check(
        "SRW-REFERENT-TYPES",
        typed_referent,
        f"source_internal={len(source_graph.internal)} target_internal={len(target_graph.internal)} ports={len(target_graph.ports)}",
    )

    candidates = list(dictionary_candidates(rewrite_data["source_basis_labels"], rewrite_data["target_basis_labels"]))
    expected_candidate_count = math.factorial(shape(vg)[1]) * math.factorial(shape(vg)[0])
    if mutant == "dictionary-preplant":
        candidates = candidates[:1]
    survivors = [
        candidate
        for candidate in candidates
        if support_compatible(candidate, vg, allowed, frozenset(rewrite_data["source_basis_labels"]))
    ]
    if mutant == "dictionary-drop" and survivors:
        survivors = survivors[:-1]
    ambiguous_targets = frozenset(dst for src, dst in allowed if src == rewrite_data["source_basis_labels"][0])
    expected_survivor_count = math.factorial(len(ambiguous_targets))
    ledger.check(
        "SRW-DICTIONARY-CENSUS",
        len(candidates) == expected_candidate_count and len(survivors) == expected_survivor_count,
        f"candidates={len(candidates)} survivors={len(survivors)}",
    )

    input_state = tuple(scalar(x) for x in rewrite_data["input_state"])
    grown_state = matvec(vg, input_state)
    current_signatures = tuple(
        (
            tuple(tuple(vtext(row)) for row in legacy_product),
            qtext(sum(x.norm2() for x in grown_state)),
        )
        for _ in survivors
    )
    graph_probs: list[Q] = []
    for idx, candidate in enumerate(survivors):
        if mutant == "graph-probe-row" and idx == 0:
            effect = tuple(ONE if k == 1 else ZERO for k in range(len(grown_state)))
            graph_probs.append(probability(effect, grown_state))
        else:
            graph_probs.append(
                graph_probe_probability(target_graph, rewrite_data["probe_port"], candidate, grown_state)
            )
    independently_graph_probs = [
        probability(
            tuple(ONE if k == row_for_label(candidate, graph_port_neighbor(target_graph, rewrite_data["probe_port"])) else ZERO for k in range(len(grown_state))),
            grown_state,
        )
        for candidate in survivors
    ]
    ledger.check(
        "SRW-GRAPH-FUTURE",
        graph_probs == independently_graph_probs and len(set(graph_probs)) == len(survivors),
        f"probabilities={[qtext(p) for p in graph_probs]}",
    )

    persistent_target = dict(primary_span.persists)[rewrite_data["source_basis_labels"][0]]
    persistence_probs = [
        probability(
            tuple(ONE if k == row_for_label(candidate, persistent_target) else ZERO for k in range(len(grown_state))),
            grown_state,
        )
        for candidate in survivors
    ]
    ledger.check(
        "SRW-PERSISTENCE-FUTURE",
        len(set(persistence_probs)) == len(survivors),
        f"probabilities={[qtext(p) for p in persistence_probs]}",
    )

    rename = rewrite_data["rename"]
    source_rename = {v: rename[v] for v in source_graph.all_vertices()}
    target_rename = {v: rename[v] for v in target_graph.all_vertices()}
    renamed_source = source_graph.relabel(source_rename)
    renamed_target = target_graph.relabel(target_rename)
    renamed_persistence = tuple((source_rename[a], target_rename[b]) for a, b in primary_span.persists)
    if mutant == "persistence-spelling":
        renamed_persistence = primary_span.persists
    persistence_natural = set(renamed_persistence) == {
        (source_rename[a], target_rename[b]) for a, b in primary_span.persists
    }
    ledger.check(
        "SRW-PERSISTENCE-NATURALITY",
        persistence_natural and len(renamed_source.internal) == len(source_graph.internal),
        f"pairs={len(renamed_persistence)}",
    )

    renamed_candidates = [rename_candidate(c, rename) for c in survivors]
    renamed_graph_probs = [
        graph_probe_probability(renamed_target, rename[rewrite_data["probe_port"]], c, grown_state)
        for c in renamed_candidates
    ]
    if mutant == "relabel-break" and renamed_graph_probs:
        renamed_graph_probs[0] += Q(1)
    bundle_natural = renamed_graph_probs == graph_probs
    ledger.check(
        "SRW-BUNDLE-NATURALITY",
        bundle_natural,
        f"original={[qtext(p) for p in graph_probs]} renamed={[qtext(p) for p in renamed_graph_probs]}",
    )

    swap_rows = permutation_matrix((2, 1, 0))
    current_generators = [identity(shape(vg)[0])]
    graph_label = graph_port_neighbor(target_graph, rewrite_data["probe_port"])
    graph_generator = projector(shape(vg)[0], row_for_label(survivors[0], graph_label))
    persistence_generator = projector(shape(vg)[0], row_for_label(survivors[0], persistent_target))
    future_generators = current_generators + [graph_generator, persistence_generator]
    if mutant == "future-reactivation-drop":
        future_generators = current_generators
    current_commutes = common_commutant_contains(swap_rows, current_generators)
    future_commutes = common_commutant_contains(swap_rows, future_generators)
    ledger.check(
        "SRW-CONTINUATION-COMMUTANT",
        current_commutes and not future_commutes,
        f"current={current_commutes} future={future_commutes}",
    )
    continuation_class = "future-physical" if len(set(graph_probs + persistence_probs)) > 1 and not future_commutes else "stable-gauge"
    if mutant == "swap-call-gauge":
        continuation_class = "stable-gauge"
    ledger.check(
        "SRW-CONTINUATION-CLASSIFICATION",
        continuation_class == "future-physical",
        f"class={continuation_class}",
    )

    t_values = tuple(Q(t) for t in fixture["support_family"]["rational_parameters"])
    support_rows: list[dict[str, Any]] = []
    canonical = next(
        candidate
        for candidate in survivors
        if candidate.source_by_col == tuple(rewrite_data["source_basis_labels"])
        and candidate.target_by_row == tuple(rewrite_data["target_basis_labels"])
    )
    forbidden_pair = tuple(fixture["support_family"]["forbidden_entry"])
    actual_matrices = []
    for t in t_values:
        x, z = circle(t)
        vmap = growth(x, z)
        actual_matrices.append(vmap)
        labelled = canonical.labelled_support(vmap)
        support_rows.append(
            {
                "t": qtext(t),
                "x": qtext(x),
                "z": qtext(z),
                "actual_count": len(labelled),
                "subset": labelled <= allowed,
            }
        )
    endpoint_counts = [row["actual_count"] for row in support_rows if row["t"] in (qtext(t_values[0]), qtext(t_values[-1]))]
    independently_endpoint = min(len(canonical.labelled_support(v)) for v in actual_matrices)
    observed_endpoint = independently_endpoint
    if mutant == "support-equality":
        observed_endpoint = len(allowed)
    ledger.check(
        "SRW-ACTUAL-SUPPORT",
        all(row["subset"] for row in support_rows)
        and observed_endpoint == independently_endpoint
        and observed_endpoint < len(allowed),
        f"allowed={len(allowed)} endpoint={observed_endpoint} rows={support_rows}",
    )
    forbidden_map = growth(*circle(Q(1, 2)))
    if mutant == "forbidden-support":
        forbidden_map = tuple(
            tuple(value + (GQ(Q(1, 5)) if rr == 2 and cc == 1 else ZERO) for cc, value in enumerate(row))
            for rr, row in enumerate(forbidden_map)
        )
    forbidden_absent = forbidden_pair not in canonical.labelled_support(forbidden_map)
    ledger.check(
        "SRW-FORBIDDEN-SUPPORT",
        forbidden_absent,
        f"forbidden={forbidden_pair} present={not forbidden_absent}",
    )

    adjacency_type = frozenset(("target", tuple(sorted(edge))) for edge in target_graph.edges)
    transition_type = frozenset(("transition", pair) for pair in canonical.labelled_support(vg))
    same_map_span_count = len({primary_span.persists, alternate_span.persists})
    map_only_refuted = (
        observed_endpoint < len(allowed)
        and adjacency_type.isdisjoint(transition_type)
        and same_map_span_count > 1
    )
    ledger.check(
        "SRW-MAP-ONLY-DISCRIMINATOR",
        map_only_refuted,
        f"endpoint_missing={len(allowed)-observed_endpoint} spans={same_map_span_count} typed_disjoint={adjacency_type.isdisjoint(transition_type)}",
    )

    bundle_ok = typed_referent and all(is_isometry(v) for v in actual_matrices) and bundle_natural
    ledger.check(
        "SRW-BUNDLE-WELD",
        bundle_ok,
        f"typed={typed_referent} isometries={sum(is_isometry(v) for v in actual_matrices)}/{len(actual_matrices)} natural={bundle_natural}",
    )

    fiber_rows: list[dict[str, Any]] = []
    for data in fixture["fiber_specs"]:
        spec = FiberSpec(data["sector"], data["internal_multiplicity"], data["include_ports"])
        fiber_rows.append(
            {
                "name": data["name"],
                "source": spec.dimension(source_graph),
                "target": spec.dimension(target_graph),
            }
        )
    independent_fiber_rows = [
        {
            "name": data["name"],
            "source": FiberSpec(data["sector"], data["internal_multiplicity"], data["include_ports"]).dimension(source_graph),
            "target": FiberSpec(data["sector"], data["internal_multiplicity"], data["include_ports"]).dimension(target_graph),
        }
        for data in fixture["fiber_specs"]
    ]
    if mutant == "functor-dimension-type":
        fiber_rows[0]["target"] += 1
    ledger.check(
        "SRW-FIBER-DIMENSIONS",
        fiber_rows == independent_fiber_rows,
        f"rows={fiber_rows}",
    )
    dimension_pairs = [[row["source"], row["target"]] for row in fiber_rows]
    legacy_exact_count = sum((row["source"], row["target"]) == (shape(vg)[1], shape(vg)[0]) for row in fiber_rows)

    vg2 = kron(vg, identity(2))
    port_map = direct_sum(vg, identity(len(target_graph.ports)))
    edge_map = rmat
    construction_isometries = [is_isometry(vg), is_isometry(vg2), is_isometry(port_map), is_isometry(edge_map)]
    ledger.check(
        "SRW-FUNCTOR-CONSTRUCTIONS",
        all(construction_isometries)
        and shape(vg2) == (fiber_rows[1]["target"], fiber_rows[1]["source"])
        and shape(port_map) == (fiber_rows[2]["target"], fiber_rows[2]["source"])
        and shape(edge_map) == (fiber_rows[3]["target"], fiber_rows[3]["source"]),
        f"isometries={sum(construction_isometries)}/{len(construction_isometries)}",
    )

    internal_swap = kron(identity(shape(vg)[0]), permutation_matrix((1, 0)))
    blind_internal = kron(identity(shape(vg)[0]), identity(2))
    active_internal = kron(identity(shape(vg)[0]), matrix([[1, 0], [0, -1]]))
    active_generators = [blind_internal, active_internal]
    if mutant == "internal-reactivation-drop":
        active_generators = [blind_internal]
    internal_blind = common_commutant_contains(internal_swap, [blind_internal])
    internal_active = not common_commutant_contains(internal_swap, active_generators)
    ledger.check(
        "SRW-INTERNAL-REACTIVATION",
        internal_blind and internal_active,
        f"coarse_blind={internal_blind} active_distinguishes={internal_active}",
    )
    internal_class = "future-physical" if internal_active else "stable-gauge"
    if mutant == "internal-call-gauge":
        internal_class = "stable-gauge"
    ledger.check(
        "SRW-INTERNAL-CLASSIFICATION",
        internal_class == "future-physical",
        f"class={internal_class}",
    )

    recurrence = fixture["recurrence"]
    base_t = Q(recurrence["second_growth_parameter"])
    drift_t = Q(recurrence["drift_control_parameter"])
    base_growth = growth(*circle(base_t))
    second_growth = base_growth
    if mutant == "recurrence-site-drift":
        second_growth = growth(*circle(drift_t))
    repeated = direct_sum(base_growth, second_growth)
    drift_control = direct_sum(base_growth, growth(*circle(drift_t)))
    ledger.check(
        "SRW-RECURRING-LOCALITY",
        second_growth == base_growth and drift_control != direct_sum(base_growth, base_growth) and is_isometry(repeated),
        f"same_type_equal={second_growth == base_growth} drift_control_moves={drift_control != direct_sum(base_growth, base_growth)}",
    )

    transport_pairs: list[dict[str, Any]] = []
    for phi_index, phi_t in enumerate(t_values):
        x, z = circle(phi_t)
        theta_values = (phi_t,) if mutant == "angle-lock-constructor" else t_values
        for theta_index, theta_t in enumerate(theta_values):
            u, v = circle(theta_t)
            p0, p1 = coherent_screen(x, z, u, v)
            transport_pairs.append(
                {
                    "phi_index": phi_index,
                    "theta_index": theta_index,
                    "phi_t": qtext(phi_t),
                    "theta_t": qtext(theta_t),
                    "screen": [qtext(p0), qtext(p1)],
                    "dot": qtext(x * u + z * v),
                    "normalized": p0 + p1 == 1,
                }
            )
    expected_transport_pairs = len(t_values) * len(t_values)
    transport_screens = {tuple(row["screen"]) for row in transport_pairs}
    ledger.check(
        "SRW-INDEPENDENT-ANGLE-VARIETY",
        len(transport_pairs) == expected_transport_pairs
        and all(row["normalized"] for row in transport_pairs)
        and len(transport_screens) > 1,
        f"pairs={len(transport_pairs)} distinct_screens={len(transport_screens)}",
    )

    reciprocal_pairs = [row for row in transport_pairs if row["dot"] == qtext(Q(1))]
    independently_reciprocal = [
        row for row in transport_pairs if row["phi_index"] == row["theta_index"]
    ]
    if mutant == "reciprocity-assume":
        reciprocal_pairs = list(transport_pairs)
    ledger.check(
        "SRW-RECIPROCITY-LOCUS",
        reciprocal_pairs == independently_reciprocal,
        f"reciprocal={len(reciprocal_pairs)} grid={len(transport_pairs)}",
    )

    x, z = circle(Q(1, 2))
    vphi = growth(x, z)
    left_inverse = adjoint(vphi)
    if mutant == "reciprocity-remove":
        left_inverse = tuple(
            tuple(value + (GQ(Q(1, 5)) if rr == cc == 0 else ZERO) for cc, value in enumerate(row))
            for rr, row in enumerate(left_inverse)
        )
    left_inverse_ok = matmul(left_inverse, vphi) == identity(shape(vphi)[1])
    ledger.check(
        "SRW-RECIPROCAL-LEFT-INVERSE",
        left_inverse_ok,
        f"left_inverse={left_inverse_ok}",
    )

    null_vec = (GQ(-z), ZERO, GQ(x))
    null_row = tuple(value.conjugate() for value in null_vec)
    extension = (
        tuple(left_inverse[0][c] + null_row[c] for c in range(len(null_row))),
        tuple(left_inverse[1][c] for c in range(len(null_row))),
    )
    extension_left_inverse = matmul(extension, vphi) == identity(shape(vphi)[1])
    extension_moves_null = matvec(extension, null_vec) != matvec(adjoint(vphi), null_vec)
    ledger.check(
        "SRW-LEFT-INVERSE-DARK-EXTENSION",
        extension_left_inverse and extension_moves_null,
        f"same_on_image={extension_left_inverse} moves_null={extension_moves_null}",
    )

    record_weight_rows = []
    for t in t_values:
        rr, ss = circle(t)
        weights = reflection(rr, ss)
        record_weight_rows.append(
            {
                "t": qtext(t),
                "probabilities": [qtext(rr * rr), qtext(ss * ss)],
                "complete": matmul(adjoint(weights), weights) == identity(shape(weights)[1]),
            }
        )
    record_weight_signatures = {tuple(row["probabilities"]) for row in record_weight_rows}
    ledger.check(
        "SRW-RECORDED-WEIGHTS-FREE",
        all(row["complete"] for row in record_weight_rows) and len(record_weight_signatures) > 1,
        f"rows={len(record_weight_rows)} distinct={len(record_weight_signatures)}",
    )

    fixture_phases = tuple(
        ONE if token == "1" else -ONE if token == "-1" else I if token == "i" else -I
        for token in fixture["phase_control"]["group"]
    )
    phase_group_ok = set(fixture_phases) == set(PHASES)
    orbits = cycle_orbits()
    orbit_sizes = tuple(sorted(len(orbit) for orbit in orbits))
    holonomy_sets = tuple(frozenset(cycle_holonomy(connection) for connection in orbit) for orbit in orbits)
    observed_orbit_count = len(orbits)
    if mutant == "cycle-call-gauge":
        observed_orbit_count = 1
    connection_count = sum(len(orbit) for orbit in orbits)
    expected_effective_size = len(PHASES) ** (len(fixture["phase_control"]["cycle_vertices"]) - 1)
    ledger.check(
        "SRW-PHASE-ORBITS",
        phase_group_ok
        and observed_orbit_count == len(PHASES)
        and all(len(hs) == 1 for hs in holonomy_sets)
        and orbit_sizes == tuple([expected_effective_size] * len(PHASES)),
        f"connections={connection_count} orbits={observed_orbit_count} sizes={orbit_sizes}",
    )

    seed_connection = (ONE, I, -ONE)
    frames = (I, -ONE, -I)
    from srw_core import gauge_cycle

    transformed = gauge_cycle(seed_connection, frames)
    if mutant == "phase-frame-break":
        transformed = (transformed[0] * I, transformed[1], transformed[2])
    phase_gauge_ok = cycle_holonomy(transformed) == cycle_holonomy(seed_connection)
    ledger.check(
        "SRW-PHASE-GAUGE",
        phase_gauge_ok,
        f"before={gtext(cycle_holonomy(seed_connection))} after={gtext(cycle_holonomy(transformed))}",
    )

    holonomies = PHASES
    if mutant == "holonomy-flatten":
        holonomies = tuple(ONE for _ in PHASES)
    phase_screens = {gtext(h): qtext(two_route_probability(h)) for h in holonomies}
    ledger.check(
        "SRW-HOLONOMY-SCREEN",
        len(set(phase_screens.values())) > 1
        and qtext(Q(1)) in phase_screens.values()
        and qtext(Q(0)) in phase_screens.values(),
        f"screens={phase_screens}",
    )

    runtime_phase_values = [
        *fixture_phases,
        *(value for orbit in orbits for connection in orbit for value in connection),
        *(value for hs in holonomy_sets for value in hs),
        *seed_connection,
        *frames,
        *transformed,
        *holonomies,
    ]
    if mutant == "runtime-scalar-leak":
        leaked = object.__new__(GQ)
        object.__setattr__(leaked, "re", 0)
        object.__setattr__(leaked, "im", 1)
        runtime_phase_values.append(leaked)
    runtime_gaussian_exact = all(
        isinstance(value, GQ)
        and isinstance(value.re, Fraction)
        and isinstance(value.im, Fraction)
        for value in runtime_phase_values
    )
    ledger.check(
        "SRW-RUNTIME-GAUSSIAN-EXACT",
        runtime_gaussian_exact,
        f"values={len(runtime_phase_values)} exact={runtime_gaussian_exact}",
    )

    expected_reads = {
        "v16/code/srw_fixture.json",
        "v16/code/srw_core.py",
        "v16/note-srw-pin.md",
        "v16/code/ppr_fixture.json",
        "v16/code/ppr_receipt.json",
        "v16/code/srw_score.py",
    }
    ledger.check(
        "SRW-RUNTIME-READ-SET",
        set(read_log) == expected_reads and len(read_log) == len(expected_reads),
        f"reads={sorted(read_log)}",
    )

    source_tree = ast.parse(core_bytes.decode("utf-8"))
    scorer_tree = ast.parse(scorer_bytes.decode("utf-8"))
    floats = [
        node.value
        for tree in (source_tree, scorer_tree)
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, float)
    ]
    ledger.check(
        "SRW-EXACT-ARITHMETIC",
        not floats,
        f"float_literals={len(floats)}",
    )

    current_signature_count = len(set(current_signatures))
    future_signature_count = len(set(graph_probs))
    flags = {
        "typed_referent": typed_referent,
        "legacy_ok": all(identity_checks),
        "map_only_refuted": map_only_refuted,
        "dictionary_future_physical": current_signature_count == 1 and future_signature_count > 1,
        "bundle_unselected": bundle_ok and len(transport_screens) > 1,
        "reciprocal_weights_free": left_inverse_ok and len(record_weight_signatures) > 1,
    }
    selected_indices = builder_outcome_indices(flags)
    numeric_vector = (
        int(typed_referent),
        int(all(identity_checks)),
        len(allowed) - observed_endpoint,
        same_map_span_count,
        current_signature_count,
        future_signature_count,
        int(bundle_ok),
        len(transport_screens),
        int(left_inverse_ok),
        len(record_weight_signatures),
    )
    comparator_indices = independent_outcome_indices(numeric_vector)
    if mutant == "verdict-flip":
        selected_indices = tuple(reversed(selected_indices[:-1])) if len(selected_indices) > 1 else (0,)
    ledger.check(
        "SRW-OUTCOME-COMPARATOR",
        selected_indices == comparator_indices and bool(selected_indices),
        f"builder={selected_indices} comparator={comparator_indices}",
    )
    selected_words = [outcomes[index] for index in selected_indices]

    consequences = {
        "finite_bundle_weld": "constructed",
        "map_only_recovery": "refuted-at-fixture",
        "dictionary": "future-physical-and-unselected",
        "catalogue": "unselected",
        "growth_reconvergence_reciprocity": "conditional-on-exact-unrecorded-erasure",
        "recorded_successor_weights": "unselected",
        "hamiltonian": "not-reconstructed",
        "particle_species": "not-derived",
        "epr_no_signalling": "no-new-result",
        "gravity_backreaction": "not-established",
        "qft_gr_deviation": "not-defined",
    }
    ledger.check(
        "SRW-CONSEQUENCE-SCOPE",
        consequences["hamiltonian"] == "not-reconstructed"
        and consequences["particle_species"] == "not-derived"
        and consequences["gravity_backreaction"] == "not-established"
        and consequences["qft_gr_deviation"] == "not-defined",
        f"rows={len(consequences)}",
    )

    measurements: dict[str, Any] = {
        "legacy": {
            "identity_count": sum(identity_checks),
            "identity_total": len(identity_checks),
            "support": sorted([list(pair) for pair in support(vg)]),
            "product": mtext(matmul(ub, vg)),
            "null_to_future": vtext(ub_null),
            "ppr_screens": ppr_screens,
        },
        "dictionary": {
            "candidate_count": len(candidates),
            "support_survivor_count": len(survivors),
            "survivors": [
                {"source_by_col": list(c.source_by_col), "target_by_row": list(c.target_by_row)}
                for c in survivors
            ],
            "current_signature_count": current_signature_count,
            "graph_probe_probabilities": [qtext(p) for p in graph_probs],
            "persistence_probe_probabilities": [qtext(p) for p in persistence_probs],
            "continuation_class": continuation_class,
        },
        "support": {
            "allowed_count": len(allowed),
            "endpoint_actual_count": observed_endpoint,
            "rows": support_rows,
            "forbidden_absent": forbidden_absent,
            "map_only_refuted": map_only_refuted,
        },
        "bundle": {
            "same_map_span_count": same_map_span_count,
            "natural": bundle_natural,
            "constructed": bundle_ok,
            "primary_persistence": [list(pair) for pair in primary_span.persists],
            "alternate_persistence": [list(pair) for pair in alternate_span.persists],
        },
        "fibers": {
            "rows": fiber_rows,
            "dimension_pairs": dimension_pairs,
            "legacy_exact_count": legacy_exact_count,
            "internal_class": internal_class,
            "construction_isometry_count": sum(construction_isometries),
        },
        "angles": {
            "parameter_rows": [qtext(t) for t in t_values],
            "transport_pair_count": len(transport_pairs),
            "transport_screen_count": len(transport_screens),
            "transport_rows": transport_pairs,
            "reciprocal_pair_count": len(reciprocal_pairs),
            "left_inverse_on_image": left_inverse_ok,
            "dark_extension_moves_null": extension_moves_null,
            "record_weight_rows": record_weight_rows,
            "record_weight_signature_count": len(record_weight_signatures),
            "transport_variety_dimension": 2,
            "full_moduli_dimension": 3,
            "reciprocal_moduli_dimension": 2,
        },
        "phase": {
            "connection_count": connection_count,
            "orbit_count": observed_orbit_count,
            "orbit_sizes": list(orbit_sizes),
            "screens": phase_screens,
            "gauge_invariant": phase_gauge_ok,
        },
        "classification": {
            "outcome_indices": list(selected_indices),
            "findings": selected_words,
            "numeric_vector": list(numeric_vector),
        },
    }

    expected_claims = claims_from_measurements(measurements)
    paper_measurements = json.loads(json.dumps(measurements))
    if mutant == "result-count-type":
        paper_measurements["dictionary"]["candidate_count"] += 1
    paper_claims = claims_from_measurements(paper_measurements)
    paper = render_paper(paper_measurements, paper_claims, fixture["references"])
    paper_text = paper.decode("utf-8")
    claim_occurrences = {row["id"]: paper_text.count(row["text"]) for row in expected_claims}
    ledger.check(
        "SRW-PAPER-BINDINGS",
        all(count == 1 for count in claim_occurrences.values())
        and len(expected_claims) == len({row["id"] for row in expected_claims}),
        f"claims={len(expected_claims)} occurrences={claim_occurrences}",
    )

    wall_phrases = (
        "not a metric-curvature or gravity result",
        "Particle species remain entirely unconstructed",
        "selects neither the complete configuration catalogue nor the physical coupling values",
    )
    normalized_paper = " ".join(paper_text.split())
    normalized_walls = tuple(" ".join(phrase.split()) for phrase in wall_phrases)
    ledger.check(
        "SRW-SCOPE-WALLS",
        all(phrase in normalized_paper for phrase in normalized_walls),
        f"walls={sum(phrase in normalized_paper for phrase in normalized_walls)}/{len(normalized_walls)}",
    )

    payload: dict[str, Any] = {
        "schema": "srw-result-v1",
        "primary": selected_words,
        "measurements": measurements,
        "claims": expected_claims,
        "consequences": consequences,
        "limitations": [
            "finite declared future grammar only",
            "one-excitation vertex sector is not a general configuration basis theorem",
            "configuration catalogue and coupling values unselected",
            "actualization, continuum, Lorentz, gravity, QFT, particles, constants, and phenomenology not constructed",
        ],
        "provenance": {
            "base_commit": fixture["anchors"]["base_commit"],
            "pin_commit": fixture["anchors"]["pin_commit"],
            "core_commit": fixture["anchors"]["core_commit"],
            "core_repair_from_sha256": ORIGINAL_CORE_SHA256,
            "fixture_sha256": fixture_sha,
            "core_sha256": sha256_bytes(core_bytes),
            "paper_sha256": sha256_bytes(paper),
            "runtime_reads": sorted(read_log),
        },
        "mutation_contract": {
            "names": list(MUTANTS),
            "expected_gate": EXPECTED_MUTANT_GATE,
        },
        "gates": [],
    }

    ledger.check(
        "SRW-PREWRITE-INTEGRITY",
        payload["measurements"]["classification"]["findings"] == payload["primary"]
        and payload["provenance"]["paper_sha256"] == sha256_bytes(paper),
        f"findings={len(payload['primary'])} paper={payload['provenance']['paper_sha256']}",
    )

    payload["gates"] = list(ledger.rows)
    provisional = render_transcript(payload)
    expected_rows = Counter((row["gate"], row["evidence"]) for row in payload["gates"])
    if parse_transcript_rows(provisional) != expected_rows:
        raise AssertionError("provisional transcript does not match gate ledger")
    ledger.check(
        "SRW-TRANSCRIPT-RECONCILIATION",
        True,
        f"rows={len(expected_rows)}",
    )
    payload["gates"] = list(ledger.rows)
    transcript_without_seals = render_transcript(payload)
    if mutant == "transcript-forge":
        transcript_without_seals = transcript_without_seals.replace(b"LEGACY identities=6", b"LEGACY identities=7", 1)
    headline_ok = f"LEGACY identities={measurements['legacy']['identity_count']}".encode("utf-8") in transcript_without_seals
    row_ok = parse_transcript_rows(transcript_without_seals) == Counter(
        (row["gate"], row["evidence"]) for row in payload["gates"]
    )
    if not (headline_ok and row_ok):
        raise AssertionError("SRW-TRANSCRIPT-RECONCILIATION: promoted transcript mismatch")

    sealed_payload = dict(payload)
    seal_manifest = {
        "sealed": {key: sha256_bytes(canonical_json(sealed_payload[key])) for key in sealed_payload},
        "unsealed": ["seal_manifest"],
    }
    if mutant == "seal-after-write":
        sealed_payload["measurements"] = dict(sealed_payload["measurements"])
        sealed_payload["measurements"]["legacy"] = dict(sealed_payload["measurements"]["legacy"])
        sealed_payload["measurements"]["legacy"]["identity_count"] += 1
    seal_ok = all(
        sha256_bytes(canonical_json(sealed_payload[key])) == digest
        for key, digest in seal_manifest["sealed"].items()
    ) and set(seal_manifest["sealed"]) == set(sealed_payload)
    if not seal_ok:
        raise AssertionError("SRW-PREWRITE-SEALS: payload moved after gate-time seal")

    receipt = {"payload": sealed_payload, "seal_manifest": seal_manifest}
    final_transcript = render_transcript(sealed_payload, seal_manifest)
    final_rows = parse_transcript_rows(final_transcript)
    expected_final_rows = Counter((row["gate"], row["evidence"]) for row in sealed_payload["gates"])
    if final_rows != expected_final_rows:
        raise AssertionError("SRW-TRANSCRIPT-RECONCILIATION: final transcript rows differ")
    return receipt, final_transcript, paper


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="SRW exact physical scorer")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--receipt", type=Path, default=DEFAULT_RECEIPT)
    parser.add_argument("--paper", type=Path, default=DEFAULT_PAPER)
    parser.add_argument("--mutant", choices=MUTANTS)
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--list-mutants", action="store_true")
    args = parser.parse_args(argv)

    if args.list_mutants:
        if args.selftest or args.mutant:
            parser.error("--list-mutants is exclusive")
        print("\n".join(MUTANTS))
        return 0

    if args.selftest:
        if args.mutant:
            parser.error("--selftest and --mutant are exclusive")
        before = tuple(path.exists() for path in (args.output, args.receipt, args.paper))
        try:
            solve("anchor-corrupt")
        except AssertionError as exc:
            after = tuple(path.exists() for path in (args.output, args.receipt, args.paper))
            if before == after:
                print(f"SELFTEST PASS :: {exc}")
                return 0
        print("SELFTEST FAIL", file=sys.stderr)
        return 1

    if any(path.exists() for path in (args.output, args.receipt, args.paper)):
        print("REFUSED result path already exists", file=sys.stderr)
        return 2

    try:
        receipt_obj, transcript, paper = solve(args.mutant)
    except (AssertionError, ValueError, KeyError, TypeError) as exc:
        print(f"REFUSED {exc}", file=sys.stderr)
        return 1

    receipt = canonical_json(receipt_obj)
    try:
        atomic_write_three(
            ((args.output, transcript), (args.receipt, receipt), (args.paper, paper))
        )
    except (FileExistsError, IOError) as exc:
        print(f"REFUSED {exc}", file=sys.stderr)
        return 2
    sys.stdout.buffer.write(transcript)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

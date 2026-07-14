#!/usr/bin/env python3
"""D36b authenticated actor/mailbox and immutable-record refinement.

This companion locks the repaired D36 reference transition system, rebuilds
its positive P4 semantics from actor-owned mailboxes and authenticated carried
records, and checks the forgetful projection exactly.  It also constructs
independent BORN and TOKEN opening transitions.  All arithmetic is exact; no
loop index, mailbox order or retry count is interpreted as physical time.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from collections import defaultdict, deque
from dataclasses import dataclass, field, replace
from functools import lru_cache
from pathlib import Path
from typing import Dict, FrozenSet, Iterable, List, Mapping, Optional, Sequence, Tuple


HERE = Path(__file__).resolve().parent
BASE_PATH = HERE / "d36_birth_coordination_exact.py"
BASE_SHA256 = "2a05f24529d716d6a8780d20ed5eba05fae6e3ac73ffdd490528b2be5b273683"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


if sha256(BASE_PATH.read_bytes()) != BASE_SHA256:
    raise RuntimeError("D36 repaired reference source hash mismatch")
_SPEC = importlib.util.spec_from_file_location("d36_reference_locked", BASE_PATH)
assert _SPEC and _SPEC.loader
ref = importlib.util.module_from_spec(_SPEC)
sys.modules["d36_reference_locked"] = ref
_SPEC.loader.exec_module(ref)


def freeze(value: object) -> object:
    if isinstance(value, Mapping):
        return [
            [freeze(key), freeze(item)]
            for key, item in sorted(value.items(), key=lambda pair: repr(pair[0]))
        ]
    if isinstance(value, (tuple, list)):
        return [freeze(item) for item in value]
    if isinstance(value, (set, frozenset)):
        return [freeze(item) for item in sorted(value, key=repr)]
    if hasattr(value, "__dataclass_fields__"):
        return [value.__class__.__name__] + [
            [name, freeze(getattr(value, name))]
            for name in value.__dataclass_fields__
        ]
    return value


def stable(value: object) -> str:
    return json.dumps(freeze(value), sort_keys=True, separators=(",", ":"))


def digest(value: object) -> str:
    return sha256(stable(value).encode())


PREPARE = "PREPARE"
GRANT = "GRANT"
REJECT = "REJECT"
COMMIT = "COMMIT"
ABORT = "ABORT"
ACK = "ACK"


@dataclass(frozen=True)
class Record:
    record_id: str
    owner_kind: str
    owner_index: int
    kind: str
    parents: Tuple[str, ...]
    payload: Tuple[object, ...]


@lru_cache(maxsize=None)
def make_record(
    owner_kind: str,
    owner_index: int,
    kind: str,
    parents: Sequence[str],
    payload: Sequence[object],
) -> Record:
    core = (owner_kind, owner_index, kind, tuple(parents), tuple(payload))
    return Record(digest(("record", core)), owner_kind, owner_index, kind, tuple(parents), tuple(payload))


@lru_cache(maxsize=None)
def evidence_header(record: Record) -> Tuple[object, ...]:
    payload = record.payload
    if record.kind in (GRANT, REJECT) and len(payload) == 6:
        # The exact causal predecessor is retained in the record and ledger,
        # while the reference transition quotient needs only the typed claim.
        payload = (payload[0], payload[1], payload[2], payload[3], payload[5])
    elif record.kind in ("APPLY", "RELEASE") and len(payload) == 7:
        # The live version and exact response-record identity are physical
        # history data, not coordination-state coordinates.
        payload = (payload[0], payload[1], payload[2], payload[3], payload[5])
    elif record.kind in ("DECISION_COMMIT", "DECISION_ABORT") and len(payload) == 3:
        # The response commitment is signed exactly but quotiented from the
        # finite coordination graph.
        payload = (payload[0], payload[1])
    return record.owner_kind, record.owner_index, record.kind, payload


@dataclass(frozen=True)
class Envelope:
    kind: str
    sender_kind: str
    sender_index: int
    target_kind: str
    target_index: int
    tx_index: int
    participant_index: int
    body_digest: str
    base_version: int
    capability: str
    attempt_id: str
    response_record_id: str = field(compare=False, hash=False)
    # The actor-transition graph is quotiented by the carried evidence header;
    # complete immutable record bytes are checked on replayed histories.
    evidence: Record = field(compare=False, hash=False)
    application_code: int
    signature: str = field(compare=False, hash=False)

    @property
    def envelope_id(self) -> str:
        # Replay protection is deliberately defined on the coordination
        # message identity.  Exact evidence authenticity is checked separately.
        return digest(("coordination-envelope", self.public_fields()))

    def public_fields(self) -> Tuple[object, ...]:
        return (
            self.kind,
            self.sender_kind,
            self.sender_index,
            self.target_kind,
            self.target_index,
            self.tx_index,
            self.participant_index,
            self.body_digest,
            self.base_version,
            self.capability,
            self.attempt_id,
            evidence_header(self.evidence),
            self.application_code,
        )

    def authenticated_fields(self) -> Tuple[object, ...]:
        # The record ID commits its owner, kind, complete payload and parents.
        # This physical statement is strictly finer than public_fields(), which
        # is only the finite coordination-quotient label.
        return (
            self.kind,
            self.sender_kind,
            self.sender_index,
            self.target_kind,
            self.target_index,
            self.tx_index,
            self.participant_index,
            self.body_digest,
            self.base_version,
            self.capability,
            self.attempt_id,
            self.response_record_id,
            self.evidence.record_id,
            self.application_code,
        )


@lru_cache(maxsize=None)
def actor_key(kind: str, index: int) -> str:
    return digest(("ideal-auth-key", kind, index))


@lru_cache(maxsize=None)
def signed_envelope(
    kind: str,
    sender_kind: str,
    sender_index: int,
    target_kind: str,
    target_index: int,
    tx_index: int,
    participant_index: int,
    body_digest: str,
    base_version: int,
    capability: str,
    attempt_id: str,
    response_record_id: str,
    evidence: Record,
    application_code: int = 0,
) -> Envelope:
    authenticated = (
        kind,
        sender_kind,
        sender_index,
        target_kind,
        target_index,
        tx_index,
        participant_index,
        body_digest,
        base_version,
        capability,
        attempt_id,
        response_record_id,
        evidence.record_id,
        application_code,
    )
    signature = digest(("ideal-signature", actor_key(sender_kind, sender_index), authenticated))
    return Envelope(
        kind,
        sender_kind,
        sender_index,
        target_kind,
        target_index,
        tx_index,
        participant_index,
        body_digest,
        base_version,
        capability,
        attempt_id,
        response_record_id,
        evidence,
        application_code,
        signature,
    )


def authentic(envelope: Envelope) -> bool:
    expected = digest(
        (
            "ideal-signature",
            actor_key(envelope.sender_kind, envelope.sender_index),
            envelope.authenticated_fields(),
        )
    )
    return envelope.signature == expected


@lru_cache(maxsize=None)
def capability_id(tx_index: int, participant_index: int, actor_name: str) -> str:
    return digest(("issued-route-capability", tx_index, participant_index, actor_name))


@dataclass(frozen=True)
class ParticipantActor:
    name: str
    version: int
    version_record: str
    head_record: str = field(compare=False, hash=False)
    promise: int
    promise_attempt: str
    applications: Tuple[int, ...]
    response_records: Tuple[str, ...] = field(compare=False, hash=False)
    capabilities: Tuple[str, ...]
    authorizations: Tuple[Tuple[int, str, str, int, str], ...]
    used: Tuple[str, ...]
    mailbox: Tuple[Envelope, ...]


@dataclass(frozen=True)
class TransactionActor:
    name: str
    tx_index: int
    members: Tuple[int, ...]
    base_versions: Tuple[int, ...]
    body_digest: str
    attempt_id: str
    logical_tau: Tuple[object, ...]
    carrier: Record
    head_record: str = field(compare=False, hash=False)
    capabilities: Tuple[str, ...]
    responses: Tuple[int, ...]
    response_evidence: Tuple[Optional[Record], ...] = field(compare=False, hash=False)
    response_record_ids: Tuple[str, ...] = field(compare=False, hash=False)
    phase: int
    acknowledgements: Tuple[int, ...]
    acknowledgement_evidence: Tuple[Optional[Record], ...] = field(compare=False, hash=False)
    decision: Optional[Record] = field(compare=False, hash=False)
    close: Optional[Record] = field(compare=False, hash=False)
    used: Tuple[str, ...]
    mailbox: Tuple[Envelope, ...]


@dataclass(frozen=True)
class ActorWorld:
    fixture_name: str
    mode: str
    participants: Tuple[ParticipantActor, ...]
    transactions: Tuple[TransactionActor, ...]


@dataclass(frozen=True)
class BornPreState:
    fixture_name: str
    participant_versions: Tuple[int, ...]
    requested_bases: Tuple[Tuple[int, ...], ...]


@dataclass(frozen=True)
class TokenPreState:
    fixture_name: str
    participant_versions: Tuple[int, ...]
    requested_bases: Tuple[Tuple[int, ...], ...]
    dormant_slots: Tuple[str, ...]


@lru_cache(maxsize=None)
def envelope_order_key(envelope: Envelope) -> str:
    return stable(envelope.public_fields())


def sorted_mailbox(messages: Iterable[Envelope]) -> Tuple[Envelope, ...]:
    return tuple(sorted(messages, key=envelope_order_key))


LOCAL_FIXTURES: Dict[str, ref.Fixture] = {
    "single": (ref.Tx("P", ("A", "B")),),
    "continuation": (ref.Tx("P", ("A", "B")), ref.Tx("Q", ("A", "B"))),
}

REFERENCE_COUNTS = {
    "pair": (1113, 2984, 8),
    "triangle": (34637, 140028, 17),
    "disjoint": (289, 816, 1),
    "partial": (1517, 5162, 2),
}


def fixture_for(name: str) -> ref.Fixture:
    return ref.FIXTURES[name] if name in ref.FIXTURES else LOCAL_FIXTURES[name]


def requested_base_rows(
    fixture: ref.Fixture,
    participant_count: int,
    base_version: int,
) -> Tuple[Tuple[int, ...], ...]:
    members = ref.fixture_indices(fixture)
    return tuple(
        tuple(base_version if participant in tx_members else -1 for participant in range(participant_count))
        for tx_members in members
    )


def initial_seed_records(names: Sequence[str], versions: Sequence[int]) -> Tuple[Record, ...]:
    return tuple(
        make_record("P", index, "SEED", (), (name, version))
        for index, (name, version) in enumerate(zip(names, versions))
    )


def open_actor_world(
    fixture_name: str,
    mode: str,
    participant_versions: Optional[Tuple[int, ...]] = None,
    requested_bases: Optional[Tuple[Tuple[int, ...], ...]] = None,
    carrier_epoch: int = 0,
) -> Tuple[ActorWorld, Tuple[Record, ...]]:
    fixture = fixture_for(fixture_name)
    names = ref.participant_names(fixture)
    count = len(names)
    versions = participant_versions or (0,) * count
    bases = requested_bases or requested_base_rows(fixture, count, 0)
    seeds = initial_seed_records(names, versions)
    participant_mailboxes: List[List[Envelope]] = [[] for _ in names]
    transactions: List[TransactionActor] = []
    opening_records: List[Record] = list(seeds)

    for tx_index, tx in enumerate(fixture):
        members = ref.fixture_indices(fixture)[tx_index]
        initiator = members[0]
        caps = tuple(
            capability_id(tx_index, participant, names[participant]) if participant in members else ""
            for participant in range(count)
        )
        logical_tau = (
            "logical-transaction",
            seeds[initiator].record_id,
            tx_index,
            tuple((names[p], "participant", p) for p in members),
            tuple(caps[p] for p in members),
        )
        if mode == "BORN":
            carrier = make_record(
                "T",
                tx_index,
                "T0_BIRTH",
                (seeds[initiator].record_id,),
                (logical_tau, ("attempt-slot", carrier_epoch)),
            )
        elif mode == "TOKEN":
            slot = make_record(
                "T", tx_index, "DORMANT_SLOT", (), (fixture_name, tx_index, carrier_epoch)
            )
            opening_records.append(slot)
            carrier = make_record(
                "T",
                tx_index,
                "SLOT_ACTIVATION",
                (slot.record_id, seeds[initiator].record_id),
                (logical_tau, ("attempt-slot", carrier_epoch)),
            )
        else:
            raise AssertionError(mode)
        opening_records.append(carrier)
        body_digest = digest((logical_tau, members, bases[tx_index]))
        attempt_id = digest(
            ("structural-attempt", carrier.record_id, body_digest, members, bases[tx_index])
        )
        responses = tuple(0 if p in members else -1 for p in range(count))
        acknowledgements = tuple(0 if p in members else -1 for p in range(count))
        evidence = tuple(None for _ in range(count))
        response_record_ids = tuple("" for _ in range(count))
        transactions.append(
            TransactionActor(
                tx.name,
                tx_index,
                members,
                bases[tx_index],
                body_digest,
                attempt_id,
                logical_tau,
                carrier,
                carrier.record_id,
                caps,
                responses,
                evidence,
                response_record_ids,
                ref.OPEN,
                acknowledgements,
                evidence,
                None,
                None,
                (),
                (),
            )
        )
        for participant in members:
            participant_mailboxes[participant].append(
                signed_envelope(
                    PREPARE,
                    "T",
                    tx_index,
                    "P",
                    participant,
                    tx_index,
                    participant,
                    body_digest,
                    bases[tx_index][participant],
                    caps[participant],
                    attempt_id,
                    "",
                    carrier,
                )
            )

    participants = []
    for participant, name in enumerate(names):
        caps = tuple(
            capability_id(tx_index, participant, name)
            for tx_index, members in enumerate(ref.fixture_indices(fixture))
            if participant in members
        )
        authorizations = tuple(
            (
                tx_index,
                transactions[tx_index].attempt_id,
                transactions[tx_index].body_digest,
                transactions[tx_index].base_versions[participant],
                transactions[tx_index].capabilities[participant],
            )
            for tx_index, members in enumerate(ref.fixture_indices(fixture))
            if participant in members
        )
        participants.append(
            ParticipantActor(
                name,
                versions[participant],
                seeds[participant].record_id,
                seeds[participant].record_id,
                -1,
                "",
                tuple(-1 if participant not in members else 0 for members in ref.fixture_indices(fixture)),
                tuple("" for _ in fixture),
                tuple(sorted(caps)),
                authorizations,
                (),
                sorted_mailbox(participant_mailboxes[participant]),
            )
        )
    return ActorWorld(fixture_name, mode, tuple(participants), tuple(transactions)), tuple(opening_records)


def born_open(state: BornPreState) -> Tuple[ActorWorld, Tuple[Record, ...]]:
    return open_actor_world(state.fixture_name, "BORN", state.participant_versions, state.requested_bases)


def token_activate(state: TokenPreState) -> Tuple[ActorWorld, Tuple[Record, ...]]:
    world, records = open_actor_world(
        state.fixture_name, "TOKEN", state.participant_versions, state.requested_bases
    )
    actual_slots = tuple(record.record_id for record in records if record.kind == "DORMANT_SLOT")
    if actual_slots != state.dormant_slots:
        raise AssertionError((actual_slots, state.dormant_slots))
    return world, records


@lru_cache(maxsize=None)
def valid_record(record: Record) -> bool:
    rebuilt = make_record(
        record.owner_kind,
        record.owner_index,
        record.kind,
        record.parents,
        record.payload,
    )
    return rebuilt == record


def add_used(used: Tuple[str, ...], envelope: Envelope) -> Tuple[str, ...]:
    return tuple(sorted(set(used) | {envelope.envelope_id}))


def bounded_merge(
    owner_index: int,
    stage: str,
    roots: Sequence[Record],
) -> Tuple[Record, Tuple[Record, ...]]:
    if not roots:
        raise AssertionError("empty merge")
    current = list(sorted(roots, key=lambda record: record.record_id))
    created: List[Record] = []
    level = 0
    while len(current) > 1:
        next_level: List[Record] = []
        for offset in range(0, len(current), 2):
            group = current[offset : offset + 2]
            if len(group) == 1:
                next_level.append(group[0])
                continue
            merged = make_record(
                "T",
                owner_index,
                f"{stage}_MERGE",
                tuple(record.record_id for record in group),
                (level, offset // 2),
            )
            created.append(merged)
            next_level.append(merged)
        current = next_level
        level += 1
    return current[0], tuple(created)


def participant_accepts_prepare(actor: ParticipantActor, envelope: Envelope) -> bool:
    return (
        envelope.kind == PREPARE
        and envelope.target_kind == "P"
        and envelope.target_index >= 0
        and envelope.participant_index == envelope.target_index
        and envelope.sender_kind == "T"
        and envelope.sender_index == envelope.tx_index
        and envelope.capability in actor.capabilities
        and (
            envelope.tx_index,
            envelope.attempt_id,
            envelope.body_digest,
            envelope.base_version,
            envelope.capability,
        )
        in actor.authorizations
        and envelope.evidence.owner_kind == "T"
        and envelope.evidence.owner_index == envelope.tx_index
        and envelope.evidence.kind
        in ("T0_BIRTH", "SLOT_ACTIVATION", "T1_REBASE_BIRTH", "REBASE_ACTIVATION")
        and envelope.evidence.record_id
        == digest(
            (
                "record",
                (
                    envelope.evidence.owner_kind,
                    envelope.evidence.owner_index,
                    envelope.evidence.kind,
                    envelope.evidence.parents,
                    envelope.evidence.payload,
                ),
            )
        )
        and valid_record(envelope.evidence)
        and authentic(envelope)
        and envelope.envelope_id not in actor.used
    )


def participant_accepts_decision(actor: ParticipantActor, envelope: Envelope) -> bool:
    expected_kind = "DECISION_COMMIT" if envelope.kind == COMMIT else "DECISION_ABORT"
    return (
        envelope.kind in (COMMIT, ABORT)
        and envelope.target_kind == "P"
        and envelope.target_index == envelope.participant_index
        and envelope.sender_kind == "T"
        and envelope.sender_index == envelope.tx_index
        and envelope.capability in actor.capabilities
        and (
            envelope.tx_index,
            envelope.attempt_id,
            envelope.body_digest,
            envelope.base_version,
            envelope.capability,
        )
        in actor.authorizations
        and envelope.evidence.owner_kind == "T"
        and envelope.evidence.owner_index == envelope.tx_index
        and envelope.evidence.kind == expected_kind
        and len(envelope.evidence.parents) == 1
        and envelope.evidence.payload[:2] == (envelope.attempt_id, envelope.body_digest)
        and len(envelope.evidence.payload) == 3
        and envelope.response_record_id == actor.response_records[envelope.tx_index]
        and bool(envelope.response_record_id)
        and valid_record(envelope.evidence)
        and authentic(envelope)
        and envelope.envelope_id not in actor.used
    )


def handle_participant(
    actor: ParticipantActor,
    actor_index: int,
    envelope: Envelope,
) -> Tuple[ParticipantActor, Tuple[Envelope, ...], Tuple[Record, ...], bool]:
    applications = list(actor.applications)
    response_records = list(actor.response_records)
    if envelope.kind == PREPARE:
        if not participant_accepts_prepare(actor, envelope):
            return actor, (), (), False
        if applications[envelope.tx_index] != 0:
            return actor, (), (), False
        grant = actor.version == envelope.base_version and actor.promise == -1
        response_kind = GRANT if grant else REJECT
        response_code = 1 if grant else 2
        evidence = make_record(
            "P",
            actor_index,
            response_kind,
            (actor.head_record, envelope.evidence.record_id),
            (
                envelope.tx_index,
                envelope.attempt_id,
                envelope.body_digest,
                envelope.base_version,
                actor.version,
                envelope.capability,
            ),
        )
        response = signed_envelope(
            response_kind,
            "P",
            actor_index,
            "T",
            envelope.tx_index,
            envelope.tx_index,
            actor_index,
            envelope.body_digest,
            envelope.base_version,
            envelope.capability,
            envelope.attempt_id,
            evidence.record_id,
            evidence,
            response_code,
        )
        updated = replace(
            actor,
            head_record=evidence.record_id,
            promise=envelope.tx_index if grant else actor.promise,
            promise_attempt=envelope.attempt_id if grant else actor.promise_attempt,
            response_records=tuple(
                evidence.record_id if index == envelope.tx_index else value
                for index, value in enumerate(response_records)
            ),
            used=add_used(actor.used, envelope),
        )
        return updated, (response,), (evidence,), True

    if envelope.kind in (COMMIT, ABORT):
        if not participant_accepts_decision(actor, envelope):
            return actor, (), (), False
        if applications[envelope.tx_index] != 0:
            return actor, (), (), False
        if envelope.kind == COMMIT:
            if (
                actor.promise != envelope.tx_index
                or actor.promise_attempt != envelope.attempt_id
                or actor.version != envelope.base_version
            ):
                return actor, (), (), False
            application_code = 1
            application_kind = "APPLY"
            next_version = actor.version + 1
            next_promise = -1
            next_promise_attempt = ""
        else:
            application_code = 2
            application_kind = "RELEASE"
            next_version = actor.version
            next_promise = -1 if actor.promise == envelope.tx_index else actor.promise
            next_promise_attempt = (
                "" if actor.promise == envelope.tx_index else actor.promise_attempt
            )
        application = make_record(
            "P",
            actor_index,
            application_kind,
            (actor.head_record, envelope.evidence.record_id),
            (
                envelope.tx_index,
                envelope.attempt_id,
                envelope.body_digest,
                envelope.base_version,
                actor.version,
                envelope.capability,
                envelope.response_record_id,
            ),
        )
        applications[envelope.tx_index] = application_code
        acknowledgement = signed_envelope(
            ACK,
            "P",
            actor_index,
            "T",
            envelope.tx_index,
            envelope.tx_index,
            actor_index,
            envelope.body_digest,
            envelope.base_version,
            envelope.capability,
            envelope.attempt_id,
            envelope.response_record_id,
            application,
            application_code,
        )
        updated = replace(
            actor,
            version=next_version,
            version_record=application.record_id if application_code == 1 else actor.version_record,
            head_record=application.record_id,
            promise=next_promise,
            promise_attempt=next_promise_attempt,
            applications=tuple(applications),
            used=add_used(actor.used, envelope),
        )
        return updated, (acknowledgement,), (application,), True
    return actor, (), (), False


def transaction_accepts_response(actor: TransactionActor, envelope: Envelope) -> bool:
    participant = envelope.participant_index
    if participant not in actor.members:
        return False
    expected = GRANT if envelope.application_code == 1 else REJECT
    return (
        envelope.kind in (GRANT, REJECT)
        and envelope.kind == expected
        and envelope.target_kind == "T"
        and envelope.target_index == actor.tx_index
        and envelope.tx_index == actor.tx_index
        and envelope.sender_kind == "P"
        and envelope.sender_index == participant
        and envelope.body_digest == actor.body_digest
        and envelope.base_version == actor.base_versions[participant]
        and envelope.capability == actor.capabilities[participant]
        and envelope.attempt_id == actor.attempt_id
        and envelope.response_record_id == envelope.evidence.record_id
        and envelope.evidence.owner_kind == "P"
        and envelope.evidence.owner_index == participant
        and envelope.evidence.kind == expected
        and len(envelope.evidence.parents) == 2
        and envelope.evidence.parents[1] == actor.carrier.record_id
        and len(envelope.evidence.payload) == 6
        and envelope.evidence.payload[0] == envelope.tx_index
        and envelope.evidence.payload[1] == actor.attempt_id
        and envelope.evidence.payload[2] == actor.body_digest
        and envelope.evidence.payload[3] == actor.base_versions[participant]
        and envelope.evidence.payload[5] == actor.capabilities[participant]
        and (expected == REJECT or envelope.evidence.payload[4] == actor.base_versions[participant])
        and valid_record(envelope.evidence)
        and authentic(envelope)
        and envelope.envelope_id not in actor.used
    )


def transaction_accepts_ack(actor: TransactionActor, envelope: Envelope) -> bool:
    participant = envelope.participant_index
    expected_kind = "APPLY" if actor.phase == ref.COMMIT else "RELEASE"
    expected_code = 1 if actor.phase == ref.COMMIT else 2
    return (
        envelope.kind == ACK
        and actor.phase in (ref.COMMIT, ref.ABORT)
        and participant in actor.members
        and envelope.target_kind == "T"
        and envelope.target_index == actor.tx_index
        and envelope.tx_index == actor.tx_index
        and envelope.sender_kind == "P"
        and envelope.sender_index == participant
        and envelope.body_digest == actor.body_digest
        and envelope.base_version == actor.base_versions[participant]
        and envelope.capability == actor.capabilities[participant]
        and envelope.attempt_id == actor.attempt_id
        and envelope.response_record_id == actor.response_record_ids[participant]
        and envelope.application_code == expected_code
        and envelope.evidence.owner_kind == "P"
        and envelope.evidence.owner_index == participant
        and envelope.evidence.kind == expected_kind
        and actor.decision is not None
        and len(envelope.evidence.parents) == 2
        and envelope.evidence.parents[1] == actor.decision.record_id
        and len(envelope.evidence.payload) == 7
        and envelope.evidence.payload[0] == envelope.tx_index
        and envelope.evidence.payload[1] == actor.attempt_id
        and envelope.evidence.payload[2] == actor.body_digest
        and envelope.evidence.payload[3] == actor.base_versions[participant]
        and envelope.evidence.payload[5] == actor.capabilities[participant]
        and envelope.evidence.payload[6] == actor.response_record_ids[participant]
        and actor.decision.record_id in envelope.evidence.parents
        and valid_record(envelope.evidence)
        and authentic(envelope)
        and envelope.envelope_id not in actor.used
    )


def handle_transaction(
    actor: TransactionActor,
    envelope: Envelope,
) -> Tuple[TransactionActor, Tuple[Envelope, ...], Tuple[Record, ...], bool]:
    tx_index = actor.tx_index
    if envelope.kind in (GRANT, REJECT):
        if actor.phase != ref.OPEN or not transaction_accepts_response(actor, envelope):
            return actor, (), (), False
        participant = envelope.participant_index
        if actor.responses[participant] != 0:
            return actor, (), (), False
        responses = list(actor.responses)
        response_evidence = list(actor.response_evidence)
        response_record_ids = list(actor.response_record_ids)
        receipt = make_record(
            "T",
            tx_index,
            "RESPONSE_RECEIPT",
            (actor.head_record, envelope.evidence.record_id),
            (participant, envelope.kind, actor.attempt_id, actor.body_digest),
        )
        responses[participant] = envelope.application_code
        response_evidence[participant] = receipt
        response_record_ids[participant] = envelope.evidence.record_id
        created: List[Record] = [receipt]
        outgoing: List[Envelope] = []
        phase = actor.phase
        decision = actor.decision
        if all(responses[p] in (1, 2) for p in actor.members):
            phase = ref.COMMIT if all(responses[p] == 1 for p in actor.members) else ref.ABORT
            decision_kind = "DECISION_COMMIT" if phase == ref.COMMIT else "DECISION_ABORT"
            response_commitment = digest(
                tuple(response_record_ids[member] for member in actor.members)
            )
            decision = make_record(
                "T",
                tx_index,
                decision_kind,
                (receipt.record_id,),
                (actor.attempt_id, actor.body_digest, response_commitment),
            )
            created.append(decision)
            for member in actor.members:
                outgoing.append(
                    signed_envelope(
                        COMMIT if phase == ref.COMMIT else ABORT,
                        "T",
                        tx_index,
                        "P",
                        member,
                        tx_index,
                        member,
                        actor.body_digest,
                        actor.base_versions[member],
                        actor.capabilities[member],
                        actor.attempt_id,
                        response_record_ids[member],
                        decision,
                    )
                )
        updated = replace(
            actor,
            responses=tuple(responses),
            response_evidence=tuple(response_evidence),
            response_record_ids=tuple(response_record_ids),
            phase=phase,
            decision=decision,
            head_record=decision.record_id if decision is not None else receipt.record_id,
            used=add_used(actor.used, envelope),
        )
        return updated, tuple(outgoing), tuple(created), True

    if envelope.kind == ACK:
        if not transaction_accepts_ack(actor, envelope):
            return actor, (), (), False
        participant = envelope.participant_index
        if actor.acknowledgements[participant] != 0:
            return actor, (), (), False
        acknowledgements = list(actor.acknowledgements)
        acknowledgement_evidence = list(actor.acknowledgement_evidence)
        assert actor.decision is not None
        receipt = make_record(
            "T",
            tx_index,
            "ACK_RECEIPT",
            (actor.head_record, envelope.evidence.record_id),
            (participant, envelope.application_code, actor.attempt_id, actor.body_digest),
        )
        acknowledgements[participant] = 1
        acknowledgement_evidence[participant] = receipt
        created = [receipt]
        phase = actor.phase
        close = actor.close
        if all(acknowledgements[p] == 1 for p in actor.members):
            close = make_record(
                "T",
                tx_index,
                "CLOSE",
                (receipt.record_id,),
                (actor.attempt_id, actor.body_digest),
            )
            created.append(close)
            phase = ref.CLOSED
        updated = replace(
            actor,
            acknowledgements=tuple(acknowledgements),
            acknowledgement_evidence=tuple(acknowledgement_evidence),
            phase=phase,
            close=close,
            head_record=close.record_id if close is not None else receipt.record_id,
            used=add_used(actor.used, envelope),
        )
        return updated, (), tuple(created), True
    return actor, (), (), False


Service = Tuple[str, int, int]


def services(world: ActorWorld) -> Tuple[Service, ...]:
    result = []
    for index, actor in enumerate(world.participants):
        result.extend(("P", index, message) for message in range(len(actor.mailbox)))
    for index, actor in enumerate(world.transactions):
        result.extend(("T", index, message) for message in range(len(actor.mailbox)))
    return tuple(result)


def append_to_target(world: ActorWorld, envelope: Envelope) -> ActorWorld:
    participants = list(world.participants)
    transactions = list(world.transactions)
    if envelope.target_kind == "P":
        actor = participants[envelope.target_index]
        participants[envelope.target_index] = replace(
            actor, mailbox=sorted_mailbox(actor.mailbox + (envelope,))
        )
    elif envelope.target_kind == "T":
        actor = transactions[envelope.target_index]
        transactions[envelope.target_index] = replace(
            actor, mailbox=sorted_mailbox(actor.mailbox + (envelope,))
        )
    else:
        raise AssertionError(envelope.target_kind)
    return replace(world, participants=tuple(participants), transactions=tuple(transactions))


def service_world(
    world: ActorWorld,
    service: Service,
) -> Tuple[ActorWorld, Tuple[Record, ...], bool]:
    kind, actor_index, message_index = service
    participants = list(world.participants)
    transactions = list(world.transactions)
    if kind == "P":
        actor = participants[actor_index]
        envelope = actor.mailbox[message_index]
        actor_without = replace(actor, mailbox=actor.mailbox[:message_index] + actor.mailbox[message_index + 1 :])
        updated, outgoing, records, accepted = handle_participant(actor_without, actor_index, envelope)
        participants[actor_index] = updated
    elif kind == "T":
        actor = transactions[actor_index]
        envelope = actor.mailbox[message_index]
        actor_without = replace(actor, mailbox=actor.mailbox[:message_index] + actor.mailbox[message_index + 1 :])
        updated, outgoing, records, accepted = handle_transaction(actor_without, envelope)
        transactions[actor_index] = updated
    else:
        raise AssertionError(kind)
    next_world = replace(world, participants=tuple(participants), transactions=tuple(transactions))
    for outgoing_envelope in outgoing:
        next_world = append_to_target(next_world, outgoing_envelope)
    return next_world, records, accepted


def bare_message(envelope: Envelope) -> ref.Message:
    kind_map = {
        PREPARE: ref.PREPARE,
        GRANT: ref.GRANT_RESPONSE,
        REJECT: ref.REJECT_RESPONSE,
        COMMIT: ref.COMMIT_DECISION,
        ABORT: ref.ABORT_DECISION,
        ACK: ref.ACK,
    }
    return kind_map[envelope.kind], envelope.tx_index, envelope.participant_index


def project_reference(world: ActorWorld) -> ref.FFState:
    fixture = fixture_for(world.fixture_name)
    participant_count = len(world.participants)
    responses = []
    applications = []
    acknowledgements = []
    incidence = ref.fixture_indices(fixture)
    for tx_index, tx in enumerate(world.transactions):
        for participant in range(participant_count):
            if participant in incidence[tx_index]:
                responses.append(tx.responses[participant])
                applications.append(world.participants[participant].applications[tx_index])
                acknowledgements.append(tx.acknowledgements[participant])
            else:
                responses.append(-1)
                applications.append(-1)
                acknowledgements.append(-1)
    pending = tuple(
        sorted(
            bare_message(envelope)
            for actor in world.participants + world.transactions
            for envelope in actor.mailbox
        )
    )
    return ref.FFState(
        versions=tuple(actor.version for actor in world.participants),
        promises=tuple(actor.promise for actor in world.participants),
        responses=tuple(responses),
        phases=tuple(actor.phase for actor in world.transactions),
        applications=tuple(applications),
        acknowledgements=tuple(acknowledgements),
        pending=pending,
    )


def append_records(ledger: Dict[str, Record], records: Iterable[Record]) -> int:
    before = dict(ledger)
    maximum_arity = 0
    for record in records:
        if not valid_record(record):
            raise AssertionError(("record digest", record))
        if record.record_id in ledger and ledger[record.record_id] != record:
            raise AssertionError(("record collision", record.record_id))
        if record.record_id in ledger:
            raise AssertionError(("duplicate append", record.record_id))
        missing = [parent for parent in record.parents if parent not in ledger]
        if missing:
            raise AssertionError(("missing parents", record.kind, missing))
        ledger[record.record_id] = record
        maximum_arity = max(maximum_arity, len(record.parents))
    if any(ledger[key] != value for key, value in before.items()):
        raise AssertionError("immutable prefix changed")
    return maximum_arity


def record_ancestors(ledger: Mapping[str, Record], record_id: str) -> FrozenSet[str]:
    result: set[str] = set()
    stack = list(ledger[record_id].parents)
    while stack:
        current = stack.pop()
        if current in result:
            continue
        if current not in ledger:
            raise AssertionError(("ancestry hole", current))
        result.add(current)
        stack.extend(ledger[current].parents)
    return frozenset(result)


def transaction_relevant_records(ledger: Mapping[str, Record], tx_index: int) -> FrozenSet[str]:
    result = set()
    for record in ledger.values():
        if record.owner_kind == "T" and record.owner_index == tx_index:
            result.add(record.record_id)
        elif record.owner_kind == "P" and record.kind in (GRANT, REJECT, "APPLY", "RELEASE"):
            if record.payload and record.payload[0] == tx_index:
                result.add(record.record_id)
    return frozenset(result)


def validate_owned_wires(ledger: Mapping[str, Record]) -> None:
    by_owner: Dict[Tuple[str, int], List[Record]] = defaultdict(list)
    for record in ledger.values():
        by_owner[(record.owner_kind, record.owner_index)].append(record)
    for owner, records in by_owner.items():
        ids = {record.record_id for record in records}
        same_parent: Dict[str, Optional[str]] = {}
        children: Dict[str, int] = defaultdict(int)
        for record in records:
            parents = [parent for parent in record.parents if parent in ids]
            if len(parents) > 1:
                raise AssertionError(("wire has two same-owner parents", owner, record.kind))
            same_parent[record.record_id] = parents[0] if parents else None
            if parents:
                children[parents[0]] += 1
        roots = [record_id for record_id, parent in same_parent.items() if parent is None]
        if len(roots) != 1 or any(count > 1 for count in children.values()):
            raise AssertionError(("wire not linear", owner, roots, children))
        visited = set()
        current = roots[0]
        while current is not None:
            if current in visited:
                raise AssertionError(("wire cycle", owner))
            visited.add(current)
            next_nodes = [record_id for record_id, parent in same_parent.items() if parent == current]
            current = next_nodes[0] if next_nodes else None
        if visited != ids:
            raise AssertionError(("wire disconnected", owner, ids - visited))


def validate_terminal_ledger(world: ActorWorld, ledger: Mapping[str, Record]) -> Tuple[int, int]:
    projected = project_reference(world)
    fixture = fixture_for(world.fixture_name)
    if not ref.terminal_well_typed(fixture, projected):
        raise AssertionError("terminal projection not typed")
    maximum_arity = max((len(record.parents) for record in ledger.values()), default=0)
    if maximum_arity > 2:
        raise AssertionError(("parent arity", maximum_arity))
    validate_owned_wires(ledger)
    for tx_index, actor in enumerate(world.transactions):
        if actor.tx_index != tx_index:
            raise AssertionError(("transaction actor/index mismatch", actor.tx_index, tx_index))
        if actor.close is None or actor.close.record_id not in ledger:
            raise AssertionError(("missing close", tx_index))
        ancestry = record_ancestors(ledger, actor.close.record_id) | {actor.close.record_id}
        required = transaction_relevant_records(ledger, actor.tx_index)
        if not required.issubset(ancestry):
            raise AssertionError(("closure missing records", tx_index, required - ancestry))
        for participant in actor.members:
            response_kinds = {
                record.kind
                for record in ledger.values()
                if record.owner_kind == "P"
                and record.owner_index == participant
                and record.payload
                and record.payload[0] == tx_index
            }
            if not response_kinds.intersection({GRANT, REJECT}):
                raise AssertionError(("missing response record", tx_index, participant))
            if not response_kinds.intersection({"APPLY", "RELEASE"}):
                raise AssertionError(("missing application record", tx_index, participant))
    return len(ledger), maximum_arity


@dataclass(frozen=True)
class GraphSummary:
    actor_states: int
    actor_edges: int
    projected_states: int
    projected_edges: int
    actor_terminals: int
    projected_terminal_classes: Tuple[Tuple[str, ...], ...]
    terminal_ledgers: int
    maximum_ledger_records: int
    maximum_parent_arity: int
    edge_record_checks: int


def path_to_initial(
    terminal: ref.FFState,
    initial: ref.FFState,
    predecessor: Mapping[ref.FFState, Tuple[ref.FFState, Service]],
) -> Tuple[Service, ...]:
    path: List[Service] = []
    current = terminal
    while current != initial:
        prior, service = predecessor[current]
        path.append(service)
        current = prior
    return tuple(reversed(path))


def replay_path(
    fixture_name: str,
    mode: str,
    path: Sequence[Service],
) -> Tuple[ActorWorld, Dict[str, Record], int]:
    world, opening = open_actor_world(fixture_name, mode)
    ledger: Dict[str, Record] = {}
    maximum_arity = append_records(ledger, opening)
    for service in path:
        world, records, accepted = service_world(world, service)
        if not accepted:
            raise AssertionError(("normal replay rejected", service))
        maximum_arity = max(maximum_arity, append_records(ledger, records))
    return world, ledger, maximum_arity


def actor_graph(fixture_name: str, mode: str) -> GraphSummary:
    fixture = fixture_for(fixture_name)
    initial, _ = open_actor_world(fixture_name, mode)
    expected_states, expected_edges, expected_terminals = REFERENCE_COUNTS[fixture_name]
    initial_projection = project_reference(initial)
    seen_projections = {initial_projection}
    edge_count = 0
    edge_record_checks = 0
    predecessor: Dict[ref.FFState, Tuple[ref.FFState, Service]] = {}
    terminals: List[ref.FFState] = []

    def explore(world: ActorWorld) -> None:
        nonlocal edge_count, edge_record_checks
        source_projection = project_reference(world)
        available = services(world)
        if not available:
            terminals.append(source_projection)
        bare_services = []
        for service in available:
            kind, actor_index, message_index = service
            actor = world.participants[actor_index] if kind == "P" else world.transactions[actor_index]
            envelope = actor.mailbox[message_index]
            bare = bare_message(envelope)
            bare_services.append(bare)
            next_world, records, accepted = service_world(world, service)
            if not accepted:
                raise AssertionError(("normal actor envelope rejected", fixture_name, mode, service))
            if not records or len({record.record_id for record in records}) != len(records):
                raise AssertionError(("missing/duplicate record delta", fixture_name, mode, service))
            if any(not valid_record(record) or len(record.parents) > 2 for record in records):
                raise AssertionError(("invalid record delta", fixture_name, mode, service))
            edge_record_checks += 1
            target_projection = project_reference(next_world)
            try:
                pending_index = source_projection.pending.index(bare)
            except ValueError as error:
                raise AssertionError(("missing projected message", bare)) from error
            expected_projection = ref.ff_deliver(fixture, source_projection, pending_index)
            if target_projection != expected_projection:
                raise AssertionError(("step projection mismatch", fixture_name, mode, service))
            edge_count += 1
            if target_projection not in seen_projections:
                seen_projections.add(target_projection)
                predecessor[target_projection] = (source_projection, service)
                explore(next_world)
        if tuple(sorted(bare_services)) != source_projection.pending:
            raise AssertionError(("mailbox/reference opportunity mismatch", source_projection))

    explore(initial)
    if (
        len(seen_projections) != expected_states
        or edge_count != expected_edges
        or len(terminals) != expected_terminals
    ):
        raise AssertionError(
            (
                "projection not onto reference",
                fixture_name,
                mode,
                len(seen_projections),
                expected_states,
                edge_count,
                expected_edges,
                len(terminals),
                expected_terminals,
            )
        )

    terminal_classes = set()
    max_records = 0
    max_arity = 0
    for terminal_projection in terminals:
        path = path_to_initial(terminal_projection, initial_projection, predecessor)
        replayed, ledger, replay_arity = replay_path(fixture_name, mode, path)
        if project_reference(replayed) != terminal_projection:
            raise AssertionError("replay mismatch")
        records, arity = validate_terminal_ledger(replayed, ledger)
        max_records = max(max_records, records)
        max_arity = max(max_arity, arity, replay_arity)
        terminal_classes.add(tuple(sorted(ref.committed_names(fixture, terminal_projection))))
    return GraphSummary(
        len(seen_projections),
        edge_count,
        len(seen_projections),
        edge_count,
        len(terminals),
        tuple(sorted(terminal_classes)),
        len(terminals),
        max_records,
        max_arity,
        edge_record_checks,
    )


def service_key(world: ActorWorld, service: Service) -> str:
    kind, actor_index, message_index = service
    actor = world.participants[actor_index] if kind == "P" else world.transactions[actor_index]
    envelope = actor.mailbox[message_index]
    return stable((kind, actor_index, envelope.public_fields()))


def run_policy(
    fixture_name: str,
    mode: str,
    reverse: bool = False,
    participant_versions: Optional[Tuple[int, ...]] = None,
    requested_bases: Optional[Tuple[Tuple[int, ...], ...]] = None,
    carrier_epoch: int = 0,
) -> Tuple[ActorWorld, Dict[str, Record]]:
    world, opening = open_actor_world(
        fixture_name,
        mode,
        participant_versions,
        requested_bases,
        carrier_epoch,
    )
    ledger: Dict[str, Record] = {}
    append_records(ledger, opening)
    world = run_to_quiescence(world, ledger, reverse)
    validate_terminal_ledger(world, ledger)
    return world, ledger


def run_to_quiescence(
    world: ActorWorld,
    ledger: Dict[str, Record],
    reverse: bool = False,
) -> ActorWorld:
    """Service only addressed actor mailboxes, continuing the supplied world."""
    while services(world):
        by_actor: Dict[Tuple[str, int], List[Service]] = defaultdict(list)
        for candidate in services(world):
            by_actor[(candidate[0], candidate[1])].append(candidate)
        local_heads = [
            min(candidates, key=lambda service: service_key(world, service))
            for candidates in by_actor.values()
        ]
        # The policies reverse only which actor mailbox is serviced.  Each
        # actor retains its own local mailbox order, so only incomparable
        # cross-actor construction order is gauged.
        chosen = sorted(local_heads, key=lambda service: (service[0], service[1]), reverse=reverse)[0]
        world, records, accepted = service_world(world, chosen)
        if not accepted:
            raise AssertionError(("policy rejected", chosen))
        append_records(ledger, records)
    return world


def dormant_slot_ids(fixture_name: str, epoch: int = 0) -> Tuple[str, ...]:
    fixture = fixture_for(fixture_name)
    return tuple(
        make_record("T", tx_index, "DORMANT_SLOT", (), (fixture_name, tx_index, epoch)).record_id
        for tx_index, _ in enumerate(fixture)
    )


def opening_relation_gate(fixture_name: str) -> Tuple[int, int, int]:
    fixture = fixture_for(fixture_name)
    count = len(ref.participant_names(fixture))
    versions = (0,) * count
    bases = requested_base_rows(fixture, count, 0)
    born_pre = BornPreState(fixture_name, versions, bases)
    token_pre = TokenPreState(fixture_name, versions, bases, dormant_slot_ids(fixture_name))
    born_world, born_records = born_open(born_pre)
    token_world, token_records = token_activate(token_pre)
    coordination_equal = int(project_reference(born_world) == project_reference(token_world))
    born_support = sum(record.kind == "T0_BIRTH" for record in born_records)
    token_dormant = sum(record.kind == "DORMANT_SLOT" for record in token_records)
    support_equal = int(
        tuple(sorted(record.kind for record in born_records))
        == tuple(sorted(record.kind for record in token_records))
    )
    if coordination_equal != 1 or born_support != len(fixture) or token_dormant != len(fixture):
        raise AssertionError("opening relation")
    return coordination_equal, support_equal, born_support + token_dormant


def world_until_decision(mode: str = "BORN", carrier_epoch: int = 0) -> ActorWorld:
    world, _ = open_actor_world("single", mode, carrier_epoch=carrier_epoch)
    while world.transactions[0].decision is None:
        available = services(world)
        chosen = sorted(available, key=lambda service: service_key(world, service))[0]
        world, _, accepted = service_world(world, chosen)
        if not accepted:
            raise AssertionError("decision setup")
    return world


def adversarial_gate() -> Tuple[int, int]:
    rejected = 0
    attempted = 0
    world, _ = open_actor_world("pair", "BORN")
    participant = world.participants[0]
    prepare = next(envelope for envelope in participant.mailbox if envelope.kind == PREPARE)

    # One-use replay protection on an otherwise valid prepare.
    first, _, _, accepted = handle_participant(participant, 0, prepare)
    if not accepted:
        raise AssertionError("valid prepare rejected")
    attempted += 1
    second, _, _, accepted_again = handle_participant(first, 0, prepare)
    rejected += int(not accepted_again and second == first)

    # Unissued capability and disconnected-recipient lookalike.
    unissued = signed_envelope(
        PREPARE,
        prepare.sender_kind,
        prepare.sender_index,
        prepare.target_kind,
        prepare.target_index,
        prepare.tx_index,
        prepare.participant_index,
        prepare.body_digest,
        prepare.base_version,
        "UNISSUED",
        prepare.attempt_id,
        prepare.response_record_id,
        prepare.evidence,
    )
    attempted += 1
    after, _, _, accepted = handle_participant(participant, 0, unissued)
    rejected += int(not accepted and after == participant)

    attempted += 1
    other = world.participants[1]
    after, _, _, accepted = handle_participant(other, 1, prepare)
    rejected += int(not accepted and after == other)

    transaction = world.transactions[0]
    cap = transaction.capabilities[0]
    response_record = make_record(
        "P",
        0,
        GRANT,
        (world.participants[0].version_record, transaction.carrier.record_id),
        (0, transaction.attempt_id, transaction.body_digest, 0, 0, cap),
    )
    valid_response = signed_envelope(
        GRANT,
        "P",
        0,
        "T",
        0,
        0,
        0,
        transaction.body_digest,
        0,
        cap,
        transaction.attempt_id,
        response_record.record_id,
        response_record,
        1,
    )

    # Forged response signature reproduces the round-one attack and now fails.
    attempted += 1
    forged_response = replace(valid_response, signature="FORGED")
    after_tx, _, _, accepted = handle_transaction(transaction, forged_response)
    rejected += int(not accepted and after_tx == transaction)

    # Even an ideally signed response is rejected if its record binds a wrong base.
    wrong_record = make_record(
        "P",
        0,
        GRANT,
        (world.participants[0].version_record, transaction.carrier.record_id),
        (0, transaction.attempt_id, transaction.body_digest, 99, 99, cap),
    )
    wrong_base = signed_envelope(
        GRANT,
        "P",
        0,
        "T",
        0,
        0,
        0,
        transaction.body_digest,
        0,
        cap,
        transaction.attempt_id,
        wrong_record.record_id,
        wrong_record,
        1,
    )
    attempted += 1
    after_tx, _, _, accepted = handle_transaction(transaction, wrong_base)
    rejected += int(not accepted and after_tx == transaction)

    # Exact record identity, including every parent and the formerly omitted
    # live-version field, is inside the signature.  Same quotient headers may
    # not be substituted under an unchanged signature.
    parent_deleted = make_record(
        "P",
        0,
        GRANT,
        (transaction.carrier.record_id,),
        response_record.payload,
    )
    if evidence_header(parent_deleted) != evidence_header(response_record):
        raise AssertionError("parent-deletion control moved quotient header")
    attempted += 1
    substituted = replace(valid_response, evidence=parent_deleted)
    after_tx, _, _, accepted = handle_transaction(transaction, substituted)
    rejected += int(not authentic(substituted) and not accepted and after_tx == transaction)

    omitted_field_changed = make_record(
        "P",
        0,
        GRANT,
        response_record.parents,
        (0, transaction.attempt_id, transaction.body_digest, 0, 99, cap),
    )
    if evidence_header(omitted_field_changed) != evidence_header(response_record):
        raise AssertionError("omitted-field control moved quotient header")
    attempted += 1
    substituted = replace(valid_response, evidence=omitted_field_changed)
    after_tx, _, _, accepted = handle_transaction(transaction, substituted)
    rejected += int(not authentic(substituted) and not accepted and after_tx == transaction)

    decision_world = world_until_decision()
    decision_tx = decision_world.transactions[0]
    decision_participant_index = next(
        index
        for index, actor in enumerate(decision_world.participants)
        if any(envelope.kind == COMMIT for envelope in actor.mailbox)
    )
    decision_actor = decision_world.participants[decision_participant_index]
    decision_envelope = next(
        envelope for envelope in decision_actor.mailbox if envelope.kind == COMMIT
    )

    attempted += 1
    forged_decision = replace(decision_envelope, signature="FORGED")
    after, _, _, accepted = handle_participant(
        decision_actor, decision_participant_index, forged_decision
    )
    rejected += int(not accepted and after == decision_actor)

    spliced_decision = make_record(
        "T",
        decision_tx.tx_index,
        decision_envelope.evidence.kind,
        ("NONEXISTENT",),
        decision_envelope.evidence.payload,
    )
    if evidence_header(spliced_decision) != evidence_header(decision_envelope.evidence):
        raise AssertionError("decision splice moved quotient header")
    attempted += 1
    splice = replace(decision_envelope, evidence=spliced_decision)
    after, _, _, accepted = handle_participant(
        decision_actor, decision_participant_index, splice
    )
    rejected += int(not authentic(splice) and not accepted and after == decision_actor)

    applied, outgoing, _, accepted = handle_participant(
        decision_actor, decision_participant_index, decision_envelope
    )
    if not accepted or len(outgoing) != 1:
        raise AssertionError("valid decision setup")
    attempted += 1
    replayed, _, _, accepted_again = handle_participant(
        applied, decision_participant_index, decision_envelope
    )
    rejected += int(not accepted_again and replayed == applied)

    attempted += 1
    forged_ack = replace(outgoing[0], signature="FORGED")
    after_tx, _, _, accepted = handle_transaction(decision_tx, forged_ack)
    rejected += int(not accepted and after_tx == decision_tx)

    # Same body/base but a different exact carrier is a different structural
    # attempt.  A valid old decision cannot be replayed into the new actor.
    for mode in ("BORN", "TOKEN"):
        epoch_zero = world_until_decision(mode, 0)
        epoch_one = world_until_decision(mode, 1)
        old_index = next(
            index
            for index, actor in enumerate(epoch_zero.participants)
            if any(envelope.kind == COMMIT for envelope in actor.mailbox)
        )
        new_index = next(
            index
            for index, actor in enumerate(epoch_one.participants)
            if any(envelope.kind == COMMIT for envelope in actor.mailbox)
        )
        if old_index != new_index:
            raise AssertionError("same-base replay participant moved")
        old_commit = next(
            envelope
            for envelope in epoch_zero.participants[old_index].mailbox
            if envelope.kind == COMMIT
        )
        new_actor = epoch_one.participants[new_index]
        if epoch_zero.transactions[0].body_digest != epoch_one.transactions[0].body_digest:
            raise AssertionError("same-base replay body differs")
        if epoch_zero.transactions[0].attempt_id == epoch_one.transactions[0].attempt_id:
            raise AssertionError("structural attempt did not change")
        attempted += 1
        after, outgoing, records, accepted = handle_participant(new_actor, new_index, old_commit)
        rejected += int(not accepted and after == new_actor and not outgoing and not records)
    return rejected, attempted


def scheduler_gauge_gate() -> Tuple[int, str]:
    initial, opening = open_actor_world("disjoint", "BORN")
    fixture = fixture_for("disjoint")
    available = services(initial)
    checks = 0
    hashes = []
    for first_index, first in enumerate(available):
        first_actor = initial.participants[first[1]] if first[0] == "P" else initial.transactions[first[1]]
        first_envelope = first_actor.mailbox[first[2]]
        for second in available[first_index + 1 :]:
            second_actor = initial.participants[second[1]] if second[0] == "P" else initial.transactions[second[1]]
            second_envelope = second_actor.mailbox[second[2]]
            if set(fixture[first_envelope.tx_index].participants) & set(
                fixture[second_envelope.tx_index].participants
            ):
                continue
            branch_results = []
            for order in ((first, second), (second, first)):
                world = initial
                ledger: Dict[str, Record] = {}
                append_records(ledger, opening)
                for service in order:
                    world, records, accepted = service_world(world, service)
                    if not accepted:
                        raise AssertionError(("gauge service rejected", service))
                    append_records(ledger, records)
                branch_results.append((world, ledger))
            if branch_results[0] != branch_results[1]:
                raise AssertionError(("incomparable actor services did not commute", first, second))
            hashes.append(digest(tuple(sorted(branch_results[0][1].items()))))
            checks += 1
    if checks != 4:
        raise AssertionError(("gauge check census", checks))
    return checks, digest(tuple(hashes))


def append_rebase_attempt(
    old_world: ActorWorld,
    ledger: Dict[str, Record],
    mode: str,
    dormant_slot: Optional[Record],
) -> Tuple[ActorWorld, Record]:
    """Open one supplied rebase attempt on the actual terminal actor world."""
    old_tx = old_world.transactions[0]
    if old_tx.close is None or services(old_world):
        raise AssertionError("rebase requires one closed quiescent attempt")
    tx_index = 1
    members = old_tx.members
    bases = tuple(1 if participant in members else -1 for participant in range(len(old_world.participants)))
    logical_tau = old_tx.logical_tau
    body_digest = digest((logical_tau, members, bases))
    if mode == "BORN":
        carrier = make_record(
            "T",
            tx_index,
            "T1_REBASE_BIRTH",
            (old_tx.close.record_id,),
            (logical_tau, ("attempt-slot", 1)),
        )
    elif mode == "TOKEN":
        if dormant_slot is None or dormant_slot.record_id not in ledger:
            raise AssertionError("missing pre-existing dormant rebase slot")
        carrier = make_record(
            "T",
            tx_index,
            "REBASE_ACTIVATION",
            (dormant_slot.record_id, old_tx.close.record_id),
            (logical_tau, ("attempt-slot", 1)),
        )
    else:
        raise AssertionError(mode)
    append_records(ledger, (carrier,))
    attempt_id = digest(("structural-attempt", carrier.record_id, body_digest, members, bases))
    capabilities = old_tx.capabilities
    responses = tuple(0 if participant in members else -1 for participant in range(len(old_world.participants)))
    acknowledgements = tuple(
        0 if participant in members else -1 for participant in range(len(old_world.participants))
    )
    empty_evidence = tuple(None for _ in old_world.participants)
    new_tx = TransactionActor(
        "Q",
        tx_index,
        members,
        bases,
        body_digest,
        attempt_id,
        logical_tau,
        carrier,
        carrier.record_id,
        capabilities,
        responses,
        empty_evidence,
        tuple("" for _ in old_world.participants),
        ref.OPEN,
        acknowledgements,
        empty_evidence,
        None,
        None,
        (),
        (),
    )

    participants = []
    for participant_index, actor in enumerate(old_world.participants):
        applications = actor.applications + (
            0 if participant_index in members else -1,
        )
        response_records = actor.response_records + ("",)
        authorization = (
            tx_index,
            attempt_id,
            body_digest,
            bases[participant_index],
            capabilities[participant_index],
        )
        updated = replace(
            actor,
            applications=applications,
            response_records=response_records,
            authorizations=tuple(sorted(actor.authorizations + (authorization,))),
        )
        if participant_index in members:
            prepare = signed_envelope(
                PREPARE,
                "T",
                tx_index,
                "P",
                participant_index,
                tx_index,
                participant_index,
                body_digest,
                bases[participant_index],
                capabilities[participant_index],
                attempt_id,
                "",
                carrier,
            )
            updated = replace(updated, mailbox=sorted_mailbox(updated.mailbox + (prepare,)))
        participants.append(updated)
    return (
        ActorWorld(
            "continuation",
            mode,
            tuple(participants),
            old_world.transactions + (new_tx,),
        ),
        carrier,
    )


def continuation_gate() -> Tuple[int, int, int, int, int, int, int, int, str]:
    old_bases = ((0, 0),)
    current_versions = (1, 1)
    stale_count = 0
    rebase_count = 0
    prefix_preserved = 0
    ledger_valid = 0
    ancestry_count = 0
    stale_replay_rejected = 0
    total_records = 0
    lineage_ids = []
    final_versions = set()
    for mode in ("BORN", "TOKEN"):
        world, opening = open_actor_world(
            "single",
            mode,
            participant_versions=current_versions,
            requested_bases=old_bases,
            carrier_epoch=0,
        )
        old_prepare = world.participants[0].mailbox[0]
        ledger: Dict[str, Record] = {}
        append_records(ledger, opening)
        dormant_slot: Optional[Record] = None
        if mode == "TOKEN":
            dormant_slot = make_record(
                "T", 1, "DORMANT_SLOT", (), ("continuation", 1, 1)
            )
            append_records(ledger, (dormant_slot,))

        world = run_to_quiescence(world, ledger)
        validate_terminal_ledger(world, ledger)
        old_tx = world.transactions[0]
        old_outcome = ref.committed_names(fixture_for("single"), project_reference(world))
        if old_outcome or tuple(actor.version for actor in world.participants) != current_versions:
            raise AssertionError("old-base attempt did not abort stale")
        if not all(old_tx.responses[p] == 2 for p in old_tx.members):
            raise AssertionError("stale path did not carry rejects")
        if old_tx.close is None:
            raise AssertionError("stale attempt missing close")
        stale_count += 1
        old_prefix = dict(ledger)

        world, carrier = append_rebase_attempt(world, ledger, mode, dormant_slot)
        world = run_to_quiescence(world, ledger)
        validate_terminal_ledger(world, ledger)
        ledger_valid += 1
        new_tx = world.transactions[1]
        outcome = ref.committed_names(fixture_for("continuation"), project_reference(world))
        if outcome != frozenset(("Q",)):
            raise AssertionError(("persistent rebase outcome", mode, outcome))
        versions = tuple(actor.version for actor in world.participants)
        if versions != (2, 2):
            raise AssertionError("rebased versions")
        final_versions.add(versions[0])
        rebase_count += 1
        if old_tx.logical_tau != new_tx.logical_tau or old_tx.attempt_id == new_tx.attempt_id:
            raise AssertionError("logical lineage / structural attempt separation")
        if old_tx.body_digest == new_tx.body_digest:
            raise AssertionError("requested-base body did not change")
        if all(ledger[record_id] == record for record_id, record in old_prefix.items()):
            prefix_preserved += 1
        assert new_tx.close is not None
        new_ancestry = record_ancestors(ledger, new_tx.close.record_id)
        if old_tx.close.record_id in new_ancestry:
            ancestry_count += 1
        else:
            raise AssertionError("old close absent below new close")
        final_actor = world.participants[0]
        after, outgoing, records, accepted = handle_participant(final_actor, 0, old_prepare)
        if not accepted and after == final_actor and not outgoing and not records:
            stale_replay_rejected += 1
        total_records += len(ledger)
        lineage_ids.append(carrier.record_id)
    if final_versions != {2}:
        raise AssertionError(final_versions)
    return (
        stale_count,
        rebase_count,
        2,
        prefix_preserved,
        ledger_valid,
        ancestry_count,
        stale_replay_rejected,
        total_records,
        digest((total_records, tuple(lineage_ids))),
    )


def clear_runtime_caches() -> None:
    make_record.cache_clear()
    evidence_header.cache_clear()
    signed_envelope.cache_clear()
    valid_record.cache_clear()
    envelope_order_key.cache_clear()


def main() -> None:
    report: List[str] = []
    science: Dict[str, object] = {}
    gates: Dict[str, bool] = {}

    def emit(line: str = "") -> None:
        print(line)
        report.append(line)

    emit("[D36b authenticated actor-record refinement — exact receipt]")
    emit(f"locked_reference_sha256={BASE_SHA256}")
    emit("SCOPE: supplied finite closed attempts; ideal authentication; no numerical time")

    graph_rows = {}
    opening_rows = {}
    all_projection = True
    all_ledgers = True
    for fixture_name in ("pair", "triangle", "disjoint", "partial"):
        opening_rows[fixture_name] = opening_relation_gate(fixture_name)
        born = actor_graph(fixture_name, "BORN")
        clear_runtime_caches()
        token = actor_graph(fixture_name, "TOKEN")
        clear_runtime_caches()
        graph_rows[fixture_name] = {
            "BORN": born,
            "TOKEN": token,
        }
        expected = REFERENCE_COUNTS[fixture_name]
        all_projection &= (
            (born.projected_states, born.projected_edges, born.actor_terminals) == expected
            and (token.projected_states, token.projected_edges, token.actor_terminals) == expected
            and born.projected_terminal_classes == token.projected_terminal_classes
        )
        all_ledgers &= (
            born.terminal_ledgers == born.actor_terminals
            and token.terminal_ledgers == token.actor_terminals
            and born.maximum_parent_arity <= 2
            and token.maximum_parent_arity <= 2
            and born.edge_record_checks == born.actor_edges
            and token.edge_record_checks == token.actor_edges
        )
        emit(
            f"{fixture_name}: reference={expected[0]}/{expected[1]}/{expected[2]}; "
            f"BORN={born.actor_states}/{born.actor_edges}/{born.actor_terminals}; "
            f"TOKEN={token.actor_states}/{token.actor_edges}/{token.actor_terminals}; "
            f"terminal_ledgers={born.terminal_ledgers}+{token.terminal_ledgers}; "
            f"edge_record_checks={born.edge_record_checks}+{token.edge_record_checks}; "
            f"max_records={max(born.maximum_ledger_records, token.maximum_ledger_records)}; "
            f"max_parent_arity={max(born.maximum_parent_arity, token.maximum_parent_arity)}"
        )

    gates["A0"] = all_projection
    gates["A1"] = all_ledgers
    gates["A2"] = all(value[0] == 1 and value[1] == 0 for value in opening_rows.values())
    science["graphs"] = {
        name: {
            mode: [
                summary.actor_states,
                summary.actor_edges,
                summary.actor_terminals,
                summary.projected_terminal_classes,
                summary.terminal_ledgers,
                summary.maximum_ledger_records,
                summary.maximum_parent_arity,
                summary.edge_record_checks,
            ]
            for mode, summary in modes.items()
        }
        for name, modes in graph_rows.items()
    }
    science["openings"] = opening_rows
    emit("[BORN / TOKEN OBSERVABLE ALGEBRAS]")
    emit("coordination_projection_equal_all_fixtures=1")
    emit("full_support_record_algebra_equal=0; birth_and_dormant_activation_remain_ontologically_distinct")
    emit(
        "actor_graph_quotient=typed_coordination_headers; exact_record_ids_signed_separately=1; "
        "every_representative_edge_emits_checked_record_delta=1; "
        "one_complete_append_only_ledger_per_terminal_quotient_state=1"
    )

    rejected, attempted = adversarial_gate()
    gates["A3"] = rejected == attempted == 13
    science["attacks"] = [rejected, attempted]
    emit("[AUTHENTICATION / REPLAY ATTACKS]")
    emit(
        f"reject_before_durable_mutation={rejected}/{attempted}; "
        "forged_response=1; wrong_base=1; forged_decision=1; forged_ack=1; "
        "prepare_replay=1; duplicate_apply=1; unissued_capability=1; disconnected_lookalike=1; "
        "parent_deletion=1; omitted_field_substitution=1; nonexistent_decision_parent=1; "
        "same_base_cross_attempt_replay=2"
    )

    gauge_checks, gauge_hash = scheduler_gauge_gate()
    gates["A4"] = gauge_checks == 4
    science["gauge"] = [gauge_checks, gauge_hash]
    emit("[DISJOINT SCHEDULER GAUGE]")
    emit(
        f"incomparable_two-service_diamonds={gauge_checks}; both_orders_same_world_and_ledger=1; "
        f"history_family_sha256={gauge_hash}"
    )

    (
        stale,
        rebase,
        final_version,
        prefix_preserved,
        ledger_valid,
        old_close_ancestry,
        stale_replay,
        continuation_records,
        lineage_id,
    ) = continuation_gate()
    gates["A5"] = (
        stale,
        rebase,
        final_version,
        prefix_preserved,
        ledger_valid,
        old_close_ancestry,
        stale_replay,
    ) == (2, 2, 2, 2, 2, 2, 2)
    science["continuation"] = [
        stale,
        rebase,
        final_version,
        prefix_preserved,
        ledger_valid,
        old_close_ancestry,
        stale_replay,
        continuation_records,
        lineage_id,
    ]
    emit("[TWO-EPOCH STALE / REBASE CONTINUATION]")
    emit(
        f"old_base_abort={stale}/2; rebased_commit={rebase}/2; final_versions={final_version}; "
        f"same_world_prefix_preserved={prefix_preserved}/2; combined_ledger_valid={ledger_valid}/2; "
        f"old_close_below_new_close={old_close_ancestry}/2; stale_envelope_rejected={stale_replay}/2; "
        f"combined_records={continuation_records}; lineage_carriers_sha256={lineage_id}"
    )

    participant_fields = tuple(ParticipantActor.__dataclass_fields__)
    transaction_fields = tuple(TransactionActor.__dataclass_fields__)
    gates["A6"] = "mailbox" in participant_fields and "mailbox" in transaction_fields
    gates["A7"] = not any(
        word in field.lower()
        for field in participant_fields + transaction_fields
        for word in ("time", "rate", "duration")
    )
    science["ownership"] = [participant_fields, transaction_fields]
    emit("[OWNERSHIP / CLOCK SCOPE]")
    emit("participant_and_transaction_mailboxes_owned=1; network_only_selects_addressed_mailbox=1")
    emit("time_rate_duration_fields=0; serializer_step_is_not_physical_time=1")

    gates["A8"] = max(
        summary.maximum_parent_arity
        for modes in graph_rows.values()
        for summary in modes.values()
    ) <= 2
    gates["A9"] = sum(
        summary.terminal_ledgers
        for modes in graph_rows.values()
        for summary in modes.values()
    ) == 56
    gates["A10"] = tuple(gates) == tuple(f"A{index}" for index in range(10)) and all(gates.values())
    gates["A11"] = BASE_PATH.exists() and sha256(BASE_PATH.read_bytes()) == BASE_SHA256
    science["gates"] = gates

    source_hash = sha256(Path(__file__).read_bytes())
    body_hash = sha256(("\n".join(report) + "\n").encode())
    science_hash = sha256(stable(science).encode())
    emit("[HASHES]")
    emit(f"source_sha256={source_hash}")
    emit(f"stdout_body_sha256={body_hash}")
    emit(f"internal_science_sha256={science_hash}")
    emit("[GATES]")
    for name in sorted(gates, key=lambda value: int(value[1:])):
        emit(f"{name}={'PASS' if gates[name] else 'FAIL'}")
    failed = [name for name, passed in gates.items() if not passed]
    emit("[VERDICT]")
    if failed:
        emit(f"FAIL {len(gates)-len(failed)}/{len(gates)}; failed={failed}")
        raise SystemExit(1)
    emit(f"PASS {len(gates)}/{len(gates)}")
    emit("CLOCK-FREE ACTOR-LOCAL APPEND-ONLY COORDINATION REFINEMENT / FAILURE-FREE CLOSED ATTEMPTS")
    emit("BORN and TOKEN are coordination-equivalent at the audited horizon, not ontologically identical")
    emit("opportunity, arbitration selection, crash recovery, unbounded completion and quantum join remain open")


if __name__ == "__main__":
    main()

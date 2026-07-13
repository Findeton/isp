#!/usr/bin/env python3
"""
d34b_actor_reference_high_precision.py — literal actor reference for the
repaired D34b Harris process. Pin: note-d33 §7, before this file existed.

This is deliberately NOT a program that first chooses one actor from a
global list. Every actor owns a private counter-addressed clock/mark tape and
an absolute next-ring time. A heap and an independent scan-min engine are
two serial implementations of the same autonomous actor semantics.

MODEL/IMPLEMENTATION SEPARATION: the theorem uses ideal iid Uniform/Exp
coordinates. This executable uses a deterministic BLAKE2 PRF on a 256-bit
grid and evaluates logarithms at 100 Decimal digits. It is a reproducible
high-precision reference, not literally an independent continuous source:
grid ties have tiny nonzero probability and are fail-closed by NumericalTie.
Marks use exact 256-bit quartiles and unbiased rejection for partner ranks.
Birth labels are flat parent-local Ulam paths. Passive receptions touch both
causal wires but never reset the receiver clock or consume its mark.
Auxiliary times/global serialization are omitted from the physical DAG key.

The bounded exact oracle below has its own state transition code and its own
physical-key serializer.
Bounds in tests are verifier bounds, never horizons of the ideal model.
Gates A1--A8;
exit 1 on any failure.
"""

from collections import Counter, defaultdict
from dataclasses import dataclass, field
from decimal import Decimal, getcontext
from fractions import Fraction as F
import hashlib
import heapq
import math

getcontext().prec = 100
TWO256 = 1 << 256

PASS = 0
FAIL = 0


def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))


def rid_key(rid):
    if isinstance(rid, str):
        return rid, ()
    return rid[0], tuple(rid[1:])


def rid_text(rid):
    root, path = rid_key(rid)
    return root if not path else root + "/" + ".".join(str(x) for x in path)


def eid_key(eid):
    return rid_key(eid[0]), eid[2]


def child_id(parent, ordinal):
    if ordinal < 1:
        raise ValueError(ordinal)
    if isinstance(parent, str):
        return (parent, ordinal)
    return parent + (ordinal,)


def root_of(rid):
    return rid if isinstance(rid, str) else rid[0]


def touched(kind, initiator, target):
    if kind == "n":
        return (initiator,)
    return (initiator, target)


def physical_event_key(events):
    """Order-free stable wire-DAG key. Event IDs are local actor-ring
    addresses, not global event numbers. Auxiliary times are absent."""
    rows = []
    for e in events:
        eid_text = f"{rid_text(e['eid'][0])}#r{e['eid'][2]}"
        rows.append((
            eid_text, e["kind"], rid_text(e["initiator"]),
            None if e["target"] is None else rid_text(e["target"]),
            tuple(sorted(f"{rid_text(p[0])}#r{p[2]}" for p in e["preds"])),
        ))
    return tuple(sorted(rows))


def tape_uint(seed, rid, ring, domain, retry=0):
    root, path = rid_key(rid)
    fields = [b"d34b-actor-v2", str(seed).encode(), root.encode(),
              str(ring).encode(), domain.encode(), str(retry).encode()]
    fields += [str(x).encode() for x in path]
    payload = b"".join(len(x).to_bytes(4, "big") + x for x in fields)
    return int.from_bytes(hashlib.blake2b(payload, digest_size=32).digest(),
                          "big")


def tape_uniform(seed, rid, ring, domain, retry=0):
    # Strictly between 0 and 1; conversion is exact before Decimal division.
    x = tape_uint(seed, rid, ring, domain, retry)
    return Decimal(x + 1) / Decimal(TWO256 + 1)


def tape_wait(seed, rid, wait_index):
    return -tape_uniform(seed, rid, wait_index, "wait").ln()


def tape_randbelow(seed, rid, ring, m):
    if m <= 0:
        raise ValueError("empty partner alphabet")
    limit = (TWO256 // m) * m
    retry = 0
    while True:
        x = tape_uint(seed, rid, ring, "partner", retry)
        if x < limit:
            return x % m
        retry += 1


@dataclass
class Actor:
    rid: object
    sealed: bool
    neighbors: set = field(default_factory=set)
    ring_index: int = 0
    birth_index: int = 0
    next_ring: object = None


class NumericalTie(RuntimeError):
    pass


class World:
    def __init__(self, seed, remote=False, engine="heap"):
        if engine not in ("heap", "scan"):
            raise ValueError(engine)
        self.seed = int(seed)
        self.engine = engine
        self.t = Decimal(0)
        self.actors = {}
        self.events = []
        self.last_event = {}
        self.heap = []
        self._add_seed_actor("R", True)
        self._add_seed_actor("A", False)
        self._add_seed_actor("B", False)
        self._link("R", "A")
        self._link("A", "B")
        if remote:
            self._add_seed_actor("P", False)
            self._add_seed_actor("Q", False)
            self._link("P", "Q")
        for rid, actor in sorted(self.actors.items(), key=lambda z: rid_key(z[0])):
            if not actor.sealed:
                actor.next_ring = tape_wait(self.seed, rid, 0)
                self._heap_push(actor)

    def _add_seed_actor(self, rid, sealed):
        self.actors[rid] = Actor(rid=rid, sealed=sealed)

    def _link(self, a, b):
        self.actors[a].neighbors.add(b)
        self.actors[b].neighbors.add(a)

    def _heap_push(self, actor):
        heapq.heappush(self.heap, (actor.next_ring, rid_key(actor.rid), actor.rid))

    def _live(self):
        return [a for a in self.actors.values() if not a.sealed]

    def _select_heap(self):
        time, key, rid = heapq.heappop(self.heap)
        if self.heap and self.heap[0][0] == time:
            raise NumericalTie(f"equal Decimal deadlines at {time}")
        return time, rid

    def _select_scan(self):
        rows = sorted(((a.next_ring, rid_key(a.rid), a.rid) for a in self._live()))
        if len(rows) > 1 and rows[0][0] == rows[1][0]:
            raise NumericalTie(f"equal Decimal deadlines at {rows[0][0]}")
        return rows[0][0], rows[0][2]

    def peek_next(self):
        if self.engine == "heap":
            time, key, rid = self.heap[0]
            if len(self.heap) > 1:
                two = heapq.nsmallest(2, self.heap)
                if two[0][0] == two[1][0]:
                    raise NumericalTie(f"equal Decimal deadlines at {two[0][0]}")
            return time, rid
        return self._select_scan()

    def _eligible(self, rid):
        return sorted((x for x in self.actors[rid].neighbors
                       if not self.actors[x].sealed), key=rid_key)

    def _draw_kind(self, actor):
        code = tape_uint(self.seed, actor.rid, actor.ring_index, "kind") & 3
        if code == 0:
            return "b", None
        eligible = self._eligible(actor.rid)
        if code == 1 and eligible:
            j = tape_randbelow(self.seed, actor.rid, actor.ring_index,
                               len(eligible))
            return "i", eligible[j]
        return "n", None

    def _append_event(self, kind, y, target, time, ring_number):
        eid = (y, "r", ring_number)
        wires = touched(kind, y, target)
        preds = frozenset(self.last_event[w] for w in wires
                          if w in self.last_event)
        event = {
            "eid": eid,
            "kind": kind,
            "initiator": y,
            "target": target,
            "preds": preds,
            "time": time,
        }
        self.events.append(event)
        for w in wires:
            self.last_event[w] = eid
        return event

    def process_next(self, forced=None):
        if self.engine == "heap":
            time, rid = self._select_heap()
        else:
            time, rid = self._select_scan()
        self.t = time
        actor = self.actors[rid]
        kind, target = forced if forced is not None else self._draw_kind(actor)
        if kind == "i" and target not in self._eligible(rid):
            raise ValueError("forced/marked interaction is ineligible")
        actor.ring_index += 1
        ring_number = actor.ring_index
        if kind == "b":
            actor.birth_index += 1
            child = child_id(rid, actor.birth_index)
            target = child
            if child in self.actors:
                raise AssertionError("nonlocal birth-label collision")
            self.actors[child] = Actor(rid=child, sealed=False)
            self._link(rid, child)
            child_actor = self.actors[child]
            child_actor.next_ring = time + tape_wait(self.seed, child, 0)
            if self.engine == "heap":
                self._heap_push(child_actor)
        event = self._append_event(kind, rid, target, time, ring_number)
        actor.next_ring = time + tape_wait(self.seed, rid, actor.ring_index)
        if self.engine == "heap":
            self._heap_push(actor)
        return event

    def run_time(self, horizon):
        horizon = Decimal(horizon)
        while True:
            time, rid = self.peek_next()
            if time > horizon:
                break
            self.process_next()
        return self

    def run_events(self, count):
        for _ in range(count):
            self.process_next()
        return self

    def run_actor_rings(self, rid, count):
        while self.actors[rid].ring_index < count:
            self.process_next()
        return self

    def history_key(self):
        return physical_event_key(self.events)

    def event_rows(self, include_time=True):
        out = []
        for e in self.events:
            row = (e["eid"], e["kind"], e["initiator"], e["target"],
                   tuple(sorted(e["preds"], key=eid_key)))
            if include_time:
                row += (e["time"],)
            out.append(row)
        return tuple(out)


def reconstruct_preds(events):
    """Separately coded incidence reconstruction: intentionally does not
    call touched(), the producer helper."""
    last = {}
    out = {}
    for e in events:
        if e["kind"] == "n":
            wires = (e["initiator"],)
        elif e["kind"] in ("b", "i"):
            wires = (e["initiator"], e["target"])
        else:
            raise AssertionError(e["kind"])
        out[e["eid"]] = frozenset(last[w] for w in wires if w in last)
        for w in wires:
            last[w] = e["eid"]
    return out


def closure(events):
    pred = {e["eid"]: set(e["preds"]) for e in events}
    changed = True
    while changed:
        changed = False
        for e in list(pred):
            expanded = set(pred[e])
            for p in list(pred[e]):
                expanded |= pred[p]
            if expanded != pred[e]:
                pred[e] = expanded
                changed = True
    return pred


def project_shared(world, include_actor_state=False):
    shared = {rid for rid in world.actors if root_of(rid) in ("A", "B")}
    events = [e for e in world.events
              if set(touched(e["kind"], e["initiator"], e["target"])) <= shared]
    rows = []
    for e in events:
        rows.append((e["eid"], e["kind"], e["initiator"], e["target"],
                     tuple(sorted(e["preds"], key=eid_key)), e["time"]))
    if not include_actor_state:
        return tuple(rows)
    actors = []
    for rid in sorted(shared, key=rid_key):
        a = world.actors[rid]
        ns = tuple(sorted((x for x in a.neighbors if x in shared), key=rid_key))
        actors.append((rid, a.ring_index, a.birth_index, a.next_ring, ns))
    return tuple(rows), tuple(actors)


def world_snapshot(world):
    actors = []
    for rid in sorted(world.actors, key=rid_key):
        a = world.actors[rid]
        actors.append((rid, a.sealed, a.ring_index, a.birth_index, a.next_ring,
                       tuple(sorted(a.neighbors, key=rid_key))))
    return world.event_rows(), tuple(actors)


print("[d34b literal autonomous actors — 100-decimal reference]")


# A1: heap and scan are pathwise the same autonomous-clock realization.
ok1 = True
dag_count = 0
for seed in range(24):
    h = World(81000 + seed, engine="heap").run_time("4")
    s = World(81000 + seed, engine="scan").run_time("4")
    ok1 &= h.event_rows() == s.event_rows()
    ok1 &= h.history_key() == s.history_key()
    rebuilt = reconstruct_preds(h.events)
    ok1 &= all(rebuilt[e["eid"]] == e["preds"] for e in h.events)
    cl = closure(h.events)
    ok1 &= all(eid not in ps for eid, ps in cl.items())
    dag_count += len(h.events)
check(
    "A1 LITERAL ACTORS / SERIALIZER GAUGE: private 100-decimal deadlines "
    "run by heap and by separately implemented scan-min are pathwise "
    "identical; the stored wire-DAG agrees with a separately coded incidence "
    "reconstruction "
    "and is acyclic",
    ok1,
    f"24 tapes, {dag_count} events; every set traversal is structurally sorted",
)


# A2: ideal clocks tie with probability zero. Finite deterministic PRF-grid
# ties are possible and are an error, never a label tie-break. No probability
# bound for BLAKE2 outputs is claimed here. Flat IDs carry no recursion-depth
# horizon.
tie_world = World(991)
same = Decimal("1.25")
tie_world.actors["A"].next_ring = same
tie_world.actors["B"].next_ring = same
tie_world.heap = []
for actor in tie_world._live():
    tie_world._heap_push(actor)
tie_raised = False
try:
    tie_world.peek_next()
except NumericalTie:
    tie_raised = True
deep = "A"
for depth in range(6000):
    deep = child_id(deep, 1)
deep_ok = (root_of(deep) == "A" and len(rid_key(deep)[1]) == 6000
           and isinstance(tape_uint(991, deep, 0, "depth-test"), int))
check(
    "A2 HF2 + NO SOFTWARE LINEAGE CAP: ideal continuous clocks tie with "
    "probability zero; the deterministic 256-bit PRF grid can tie and an "
    "artificial equal deadline raises NumericalTie, never a label rule. "
    "Flat Ulam paths encode/hash beyond depth 5000 without recursion",
    tie_raised and deep_ok,
    "finite-grid tie fail-closed; no BLAKE2 probability theorem; "
    "depth tested=6000",
)


# A3: passive reception touches A's wire but not A's private process state.
w = World(7123, engine="scan")
# Force B to win while retaining an actual scheduled time.
w.actors["B"].next_ring = min(w.actors["A"].next_ring,
                              w.actors["B"].next_ring) / 2
a_before = (w.actors["A"].ring_index, w.actors["A"].next_ring,
            tape_uint(w.seed, "A", w.actors["A"].ring_index, "kind"))
reception = w.process_next(forced=("i", "A"))
a_after = (w.actors["A"].ring_index, w.actors["A"].next_ring,
           tape_uint(w.seed, "A", w.actors["A"].ring_index, "kind"))
# Now make A the next scheduled actor (test harness only) and force A's own
# ring to be a birth. This timing edit occurs AFTER the bit-identity capture.
other_deadline = min(a.next_ring for rid, a in w.actors.items()
                     if not a.sealed and rid != "A")
w.actors["A"].next_ring = w.t + (other_deadline - w.t) / 2
birth = w.process_next(forced=("b", None))
ok3 = (
    reception["initiator"] == "B" and reception["target"] == "A"
    and a_before == a_after
    and reception["eid"] in birth["preds"]
    and birth["target"] == ("A", 1)
)
check(
    "A3 PASSIVE RECEPTION: forced i(B,A) changes A's causal wire but leaves "
    "A's ring count, next deadline, and next keyed mark bit-identical; A's "
    "later b(A,alpha) has the reception as predecessor and alpha is parent-"
    "local",
    ok3,
    f"A state unchanged={a_before == a_after}; birth child={birth['target']}",
)


# A4: remote locality under the correct stopping rules, plus negative control.
time_equal = 0
ring_equal = 0
global_diff = 0
for seed in range(40):
    base = 92000 + seed
    a = World(base, remote=False).run_time("4")
    ar = World(base, remote=True).run_time("4")
    time_equal += project_shared(a, True) == project_shared(ar, True)
    b = World(base, remote=False).run_actor_rings("A", 8)
    br = World(base, remote=True).run_actor_rings("A", 8)
    ring_equal += project_shared(b, True) == project_shared(br, True)
    g = World(base, remote=False).run_events(12)
    gr = World(base, remote=True).run_events(12)
    global_diff += project_shared(g) != project_shared(gr)
ok4 = time_equal == ring_equal == 40 and global_diff > 0
check(
    "A4 PATHWISE REMOTE LOCALITY: Seed2 and Seed2 disjoint-union(P--Q), "
    "coupled on shared actor tapes, have bit-identical shared-component "
    "times/marks/lineages/DAG and actor states at fixed physical T and at "
    "fixed A-local rings. Fixed GLOBAL event depth differs (negative control)",
    ok4,
    f"fixed-T {time_equal}/40; fixed-A-rings {ring_equal}/40; global-depth "
    f"different {global_diff}/40",
)


# A5: time restriction uses the same source tape and is exactly projective.
restriction_ok = True
restricted_events = 0
for seed in range(24):
    long = World(110000 + seed).run_time("2")
    snap_at_2 = world_snapshot(long)
    long.run_time("5")
    short = World(110000 + seed).run_time("2")
    prefix = tuple(row for row in long.event_rows()
                   if row[-1] <= Decimal(2))
    restriction_ok &= prefix == short.event_rows()
    restriction_ok &= snap_at_2 == world_snapshot(short)
    restricted_events += len(prefix)
check(
    "A5 FIXED-TIME PROJECTIVITY: one run to T=5 restricted to t<=2 is "
    "bit-identical—including full actor/neighbor/next-deadline state—to a "
    "fresh run to T=2 on the same private tapes (the "
    "physical restriction variable is time/source noise, not 'delete the "
    "last global event')",
    restriction_ok,
    f"24 coupled pairs, {restricted_events} retained events",
)


# ---------------------------------------------------------------------------
# Independent bounded exact embedded oracle (separate transition code).

def o_seed():
    # World also contains an inert sealed root R linked to A.  R owns no
    # clock, is ineligible as an interaction target, and cannot appear in an
    # event or event predecessor, so this event-DAG oracle suppresses it.
    return {
        "actors": {"A": [0, 0], "B": [0, 0]},  # rings, births
        "adj": {"A": {"B"}, "B": {"A"}},
        "events": [],
        "last": {},
    }


def o_copy(s):
    return {
        "actors": {r: list(v) for r, v in s["actors"].items()},
        "adj": {r: set(v) for r, v in s["adj"].items()},
        "events": list(s["events"]),
        "last": dict(s["last"]),
    }


def o_actions(s, y):
    ns = sorted(s["adj"][y], key=rid_key)
    return ([('b', None, F(1, 4))]
            + [('i', x, F(1, 4 * len(ns))) for x in ns]
            + [('n', None, F(1, 2))])


def o_move(s, y, kind, target):
    z = o_copy(s)
    z["actors"][y][0] += 1
    eid = (y, "r", z["actors"][y][0])
    if kind == "b":
        z["actors"][y][1] += 1
        ordinal = z["actors"][y][1]
        target = (y, ordinal) if isinstance(y, str) else y + (ordinal,)
        z["actors"][target] = [0, 0]
        z["adj"][y].add(target)
        z["adj"][target] = {y}
    wires = (y,) if kind == "n" else (y, target)
    preds = frozenset(z["last"][r] for r in wires if r in z["last"])
    z["events"].append({"eid": eid, "kind": kind, "initiator": y,
                        "target": target, "preds": preds,
                        "time": None})
    for r in wires:
        z["last"][r] = eid
    return z


def o_id_text(rid):
    """Oracle-local serializer; intentionally independent of rid_text()."""
    if isinstance(rid, str):
        return rid
    return str(rid[0]) + "/" + ".".join(str(x) for x in rid[1:])


def o_event_key(events):
    """Oracle-local physical serializer; intentionally independent of
    physical_event_key()."""
    rows = []
    for event in events:
        eid = event["eid"]
        pred_text = []
        for pred in event["preds"]:
            pred_text.append(f"{o_id_text(pred[0])}#r{pred[2]}")
        rows.append((
            f"{o_id_text(eid[0])}#r{eid[2]}",
            event["kind"],
            o_id_text(event["initiator"]),
            None if event["target"] is None else o_id_text(event["target"]),
            tuple(sorted(pred_text)),
        ))
    return tuple(sorted(rows))


def o_state_key(s):
    actors = tuple(sorted((o_id_text(r), tuple(v))
                          for r, v in s["actors"].items()))
    adj = tuple(sorted((o_id_text(r), tuple(sorted(o_id_text(x) for x in xs)))
                       for r, xs in s["adj"].items()))
    last = tuple(sorted((o_id_text(r), f"{o_id_text(e[0])}#r{e[2]}")
                        for r, e in s["last"].items()))
    return actors, adj, o_event_key(s["events"]), last


def oracle(depth):
    level = {o_state_key(o_seed()): (o_seed(), F(1))}
    for _ in range(depth):
        nxt = {}
        for s, mass in level.values():
            actors = sorted(s["actors"], key=rid_key)
            k = len(actors)
            row = F(0)
            for y in actors:
                for kind, target, q in o_actions(s, y):
                    wgt = F(1, k) * q
                    row += wgt
                    z = o_move(s, y, kind, target)
                    key = o_state_key(z)
                    if key in nxt:
                        nxt[key] = (nxt[key][0], nxt[key][1] + mass * wgt)
                    else:
                        nxt[key] = (z, mass * wgt)
            if row != 1:
                raise AssertionError(row)
        level = nxt
    classes = defaultdict(F)
    for s, p in level.values():
        classes[o_event_key(s["events"])] += p
    return dict(classes)


# A6: exact oracle versus literal high-precision actors at two events.
exact2 = oracle(2)
nsamp = 12000
observed = Counter()
for j in range(nsamp):
    sim = World(300000 + j).run_events(2)
    observed[sim.history_key()] += 1
all_keys = set(exact2) | set(observed)
chi2 = 0.0
max_z = 0.0
for key in all_keys:
    p = float(exact2.get(key, F(0)))
    obs = observed.get(key, 0)
    if p == 0:
        chi2 = math.inf
        max_z = math.inf
        break
    exp = nsamp * p
    chi2 += (obs - exp) ** 2 / exp
    var = nsamp * p * (1 - p)
    if var > 0:
        max_z = max(max_z, abs(obs - exp) / math.sqrt(var))
df = len(exact2) - 1
chi_bar = df + 8 * math.sqrt(2 * df)
ok6 = (sum(exact2.values(), F(0)) == 1
       and set(observed) <= set(exact2)
       and chi2 < chi_bar and max_z < 6.0)
check(
    "A6 INDEPENDENT EXACT ORACLE: the separately coded rational embedded "
    "chain and serializer have mass one; 12,000 finite-PRF, 100-decimal-"
    "evaluated two-event actor worlds land only in its canonical wire-DAG "
    "classes and clear conservative chi-square/effectwise bars. This is a "
    "bounded concordance test, not equality of discrete and ideal clocks",
    ok6,
    f"classes={len(exact2)}, chi2={chi2:.3f} < {chi_bar:.3f}, max|z|="
    f"{max_z:.3f} < 6",
)


# A7: PRF-quality diagnostics and ideal-clock/Yule finite-time checks.
# These frozen, conservative bars are implementation diagnostics, not exact
# familywise hypothesis tests or a proof that the PRF is iid.
DIAGNOSTIC_Z_BAR = 8.0
winner_ok = True
winner_detail = []
clock_trials = 3000
for k in (1, 2, 4, 8):
    counts = [0] * k
    min_sum = Decimal(0)
    for j in range(clock_trials):
        waits = [tape_wait(700000 + j, ("frozen", r), 0)
                 for r in range(k)]
        winner = min(range(k), key=lambda r: waits[r])
        counts[winner] += 1
        min_sum += waits[winner]
    mean_min = min_sum / clock_trials
    expected = Decimal(1) / k
    se_mean = expected / Decimal(clock_trials).sqrt()
    winner_ok &= abs(mean_min - expected) < Decimal(DIAGNOSTIC_Z_BAR) * se_mean
    if k > 1:
        se_count = math.sqrt(clock_trials * (1 / k) * (1 - 1 / k))
        winner_ok &= (max(abs(c - clock_trials / k) for c in counts)
                      < DIAGNOSTIC_Z_BAR * se_count)
    winner_detail.append(f"k{k}:mean-min={mean_min:.8g},counts={counts}")

child_wins = 0
child_trials = 4000
for j in range(child_trials):
    seed = 800000 + j
    parent_post = tape_wait(seed, "A", 1)
    child_first = tape_wait(seed, ("A", 1), 0)
    child_wins += child_first < parent_post
child_z = abs(child_wins - child_trials / 2) / math.sqrt(child_trials / 4)

yule_trials = 2000
pop_sum = 0
ring_sum = 0
pop_hist = Counter()
for j in range(yule_trials):
    sim = World(900000 + j).run_time("4")
    pop_sum += len(sim._live())
    pop_hist[len(sim._live())] += 1
    ring_sum += len(sim.events)
mean_pop = pop_sum / yule_trials
mean_rings = ring_sum / yule_trials
target_pop = 2 * math.exp(1)
target_rings = 8 * (math.exp(1) - 1)
# Exact standard errors. N(4) is negative-binomial for a Yule process.
var_pop = 2 * math.exp(1) * (math.exp(1) - 1)
se_pop = math.sqrt(var_pop / yule_trials)
pop_z = abs(mean_pop - target_pop) / se_pop

# Total-ring second moment from the joint (N,R) generator, lambda=1/4:
# dE[R]/dt=E[N], dE[NR]/dt=E[N^2]+lambda E[NR]+lambda E[N],
# dE[R^2]/dt=2E[NR]+E[N].
n0 = 2
lam = 0.25
T4 = 4.0
E4 = math.exp(lam * T4)
ring_second = (
    n0 * (n0 + 1) * (E4 - 1) ** 2 / lam ** 2
    - 2 * n0 * (1 - lam) * (E4 * (lam * T4 - 1) + 1) / lam ** 2
    + n0 * (E4 - 1) / lam
)
var_rings = ring_second - target_rings ** 2
se_rings = math.sqrt(var_rings / yule_trials)
ring_z = abs(mean_rings - target_rings) / se_rings

# Negative-binomial population distribution, bins 2..15 plus the tail.
p0 = math.exp(-1)
expected_bins = {}
for n in range(2, 16):
    expected_bins[n] = yule_trials * (n - 1) * p0 ** 2 * (1 - p0) ** (n - 2)
expected_bins[16] = yule_trials - sum(expected_bins.values())
observed_bins = {n: pop_hist.get(n, 0) for n in range(2, 16)}
observed_bins[16] = sum(v for n, v in pop_hist.items() if n >= 16)
yule_chi = sum((observed_bins[n] - expected_bins[n]) ** 2 / expected_bins[n]
               for n in expected_bins)
yule_df = len(expected_bins) - 1
yule_bar = yule_df + DIAGNOSTIC_Z_BAR * math.sqrt(2 * yule_df)

# Direct PRF quartile and unbiased-rank diagnostics (not proofs of iid source
# noise). The rejection construction itself is exact on each uniform word.
mark_trials = 50000
kind_counts = [0, 0, 0, 0]
for j in range(mark_trials):
    kind_counts[tape_uint(950000, "A", j, "kind") & 3] += 1
kind_se = math.sqrt(mark_trials * .25 * .75)
kind_z = max(abs(x - mark_trials / 4) for x in kind_counts) / kind_se
partner_z = 0.0
for mpart in (3, 7, 17):
    counts = [0] * mpart
    for j in range(mark_trials):
        counts[tape_randbelow(960000 + mpart, "A", j, mpart)] += 1
    se = math.sqrt(mark_trials * (1 / mpart) * (1 - 1 / mpart))
    partner_z = max(partner_z,
                    max(abs(x - mark_trials / mpart) for x in counts) / se)

yule_ok = (pop_z < DIAGNOSTIC_Z_BAR and ring_z < DIAGNOSTIC_Z_BAR
           and yule_chi < yule_bar)
ok7 = (winner_ok and child_z < DIAGNOSTIC_Z_BAR and yule_ok
       and kind_z < DIAGNOSTIC_Z_BAR and partner_z < DIAGNOSTIC_Z_BAR)
check(
    "A7 CLOCK/YULE/PRF CHECKS: frozen-grid actor winners and minimum waits "
    "match the ideal 1/k and Exp(k) targets; parent/child post-birth clocks "
    "match P(child wins)=1/2; finite-time population clears the ideal law's "
    "exact negative-binomial target and derived moment bars; ring counts "
    "clear the joint-generator variance bar; mark quartiles and partner "
    "ranks clear one frozen eight-SD diagnostic bar (not an exact "
    "familywise test)",
    ok7,
    "; ".join(winner_detail) + f"; child {child_wins}/{child_trials} "
    f"(z={child_z:.2f}); N4={mean_pop:.3f}/{target_pop:.3f} z={pop_z:.2f}, "
    f"rings4={mean_rings:.3f}/{target_rings:.3f} z={ring_z:.2f}; NB-chi="
    f"{yule_chi:.2f}<{yule_bar:.2f}; kind/partner max|z|="
    f"{kind_z:.2f}/{partner_z:.2f}",
)


# A8 dependent scorecard.
ok8 = FAIL == 0
check(
    "A8 ACTOR-ARCHITECTURE SCORECARD: these are autonomous actor objects "
    "with private state, deadlines, counters, and counter-addressed PRF "
    "coordinates; one central evaluator atomically records shared events. "
    "The ideal independent-clock law is the theorem, not the finite PRF. "
    "Earned here: pathwise serializer equivalence, causal "
    "receptions, fixed-time projectivity, remote coupling, exact-oracle "
    "concordance, and finite-time Yule checks. Not claimed: exact continuous "
    "randomness in software, OS-thread/mailbox distribution, dynamic "
    "adjacency, component joining, or quantum NSE",
    ok8,
)

print()
total = PASS + FAIL
if FAIL:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
print(f"ALL CHECKS PASS ({PASS}/{total}: A1-A7 substantive; A8 dependent scorecard)")

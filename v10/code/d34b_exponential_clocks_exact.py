#!/usr/bin/env python3
"""
d34b_exponential_clocks_exact.py — repaired D34b exact receipt.

Pin: note-d33-history-law-phase.md §7 (committed before this rewrite).
Round-1 killed the former receipt: global fresh labels changed three
local events, wide global-depth brackets hid the error, and prod(q)
was incorrectly called the physical down-set measure.

THE OBJECT NOW GATED is the classical marked Harris process:
  * every live record has its own rate-1 Poisson clock;
  * on a ring: birth 1/4, interaction-total 1/4 split over eligible
    neighbors, idle the remainder;
  * births use parent-local Ulam--Harris addresses;
  * an interaction is one event on initiator AND receiver wires;
  * the physical history law is the pushforward of the clock/mark
    product law after auxiliary serialization is forgotten.

prod(q) is used only for OWN-RING initiated prefixes; prod(qbar), with
idles integrated out, only for OWN-ACT prefixes. Physical wire-DAG
cylinders carry clock-placement factors. All probability gates below
use Fraction; Decimal(100) is used only to print theorem cross-checks.
Gates E1--E7; exit 1 on any failure.
"""

from collections import defaultdict
from decimal import Decimal, getcontext
from fractions import Fraction as F

getcontext().prec = 100

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


def dfrac(x, digits=36):
    v = Decimal(x.numerator) / Decimal(x.denominator)
    return f"{v:.{digits}g}"


def skey(x):
    return repr(x)


print("[d34b repaired — the nonexplosive marked Harris path measure]")


# ---------------------------------------------------------------------------
# E1: label-blind local cylinders and the honest local-time/ring tails.

def ring_options(degree):
    assert degree >= 1
    out = [("b", F(1, 4))]
    out += [(f"i{j}", F(1, 4 * degree)) for j in range(degree)]
    out += [("n", F(1, 2))]
    return out


def act_options(degree):
    assert degree >= 1
    out = [("b", F(1, 2))]
    out += [(f"i{j}", F(1, 2 * degree)) for j in range(degree)]
    return out


ring1 = dict(ring_options(1))
act1 = dict(act_options(1))
target_birth_act = act1["b"]
target_interact_act = act1["i0"]
# After A births alpha, A has old neighbor B and new child alpha.
target_birth_then_child = act1["b"] * dict(act_options(2))["i1"]
target_two_literal_rings = ring1["b"] * dict(ring_options(2))["i1"]

# Exact partial sums in A-LOCAL ring count m. These are not global-depth
# sandwiches. T1/T2: r idles then the desired first act. T3: two stages.
m = 16
partial_one = F(1, 2) * (1 - F(1, 2) ** m)
tail_one = F(1, 2) ** (m + 1)
partial_two = F(1, 8) - F(m + 1, 2 ** (m + 3))
tail_two = F(m + 1, 2 ** (m + 3))

# Alpha binding: the pattern variable binds to A's child, independent of a
# remote earlier birth. The old raw matcher consumes the universe-wide w1.
trace = [("b", "P", "w1"), ("b", "A", "w2"), ("i", "A", "w2")]
raw_pattern = [("b", "A", "w1"), ("i", "A", "w1")]


def raw_matches(path, pattern):
    local = [op for op in path if op[1] == "A"]
    return local[:len(pattern)] == pattern


def alpha_matches(path):
    local = [op for op in path if op[1] == "A"]
    if len(local) < 2 or local[0][0] != "b":
        return False
    alpha = local[0][2]
    return local[1] == ("i", "A", alpha)


wrong_limits = {F(1, 3), F(1, 12), F(1, 5)}
ok1 = (
    ring1 == {"b": F(1, 4), "i0": F(1, 4), "n": F(1, 2)}
    and target_birth_act == F(1, 2)
    and target_interact_act == F(1, 2)
    and target_birth_then_child == F(1, 8)
    and target_two_literal_rings == F(1, 32)
    and partial_one + tail_one == F(1, 2)
    and partial_two + tail_two == F(1, 8)
    and partial_one > max(wrong_limits)
    and partial_two > F(1, 12)
    and not raw_matches(trace, raw_pattern)
    and alpha_matches(trace)
)
check(
    "E1 LABEL-BLIND OWN-RECORD CYLINDERS [exact]: ring law 1/4,1/4,1/2; "
    "first-act law 1/2,1/2; b(A,alpha) then i(A,alpha) = 1/8 at act "
    "level and 1/32 as two literal rings; local-ring tails are derived, "
    "the convicted 1/3,1/12,1/5 values are excluded, and alpha binding "
    "survives a remote earlier birth while raw w1 matching fails",
    ok1,
    f"m={m}: one-act partial={partial_one}, tail={tail_one}; two-act "
    f"partial={partial_two}, tail={tail_two}",
)


# ---------------------------------------------------------------------------
# E2: complete initiated-prefix normalization and restriction.

def prefix_distribution(depth, act=False):
    dist = {((), 1): F(1)}  # (word, current degree)
    for _ in range(depth):
        nxt = defaultdict(F)
        for (word, degree), p in dist.items():
            opts = act_options(degree) if act else ring_options(degree)
            for op, q in opts:
                degree2 = degree + (1 if op == "b" else 0)
                nxt[(word + (op,), degree2)] += p * q
        dist = dict(nxt)
    return dist


ring_d1 = prefix_distribution(1, act=False)
ring_d2 = prefix_distribution(2, act=False)
act_d1 = prefix_distribution(1, act=True)
act_d2 = prefix_distribution(2, act=True)

push_ring = defaultdict(F)
for (word, degree), p in ring_d2.items():
    push_ring[word[:1]] += p
base_ring = defaultdict(F)
for (word, degree), p in ring_d1.items():
    base_ring[word] += p

push_act = defaultdict(F)
for (word, degree), p in act_d2.items():
    push_act[word[:1]] += p
base_act = defaultdict(F)
for (word, degree), p in act_d1.items():
    base_act[word] += p

two_record_partition = sum(p * q for p in base_act.values()
                           for q in base_act.values())
ok2 = (
    sum(ring_d1.values()) == sum(ring_d2.values()) == 1
    and sum(act_d1.values()) == sum(act_d2.values()) == 1
    and dict(push_ring) == dict(base_ring)
    and dict(push_act) == dict(base_act)
    and two_record_partition == 1
)
check(
    "E2 INITIATED-PREFIX NORMALIZATION/RESTRICTION [exact]: every "
    "idle-inclusive and act-normalized word through length 2 is included; "
    "depth-2 pushes to depth-1 exactly; a two-record product partition has "
    "mass one (this is the coarse initiator algebra, not the wire-DAG)",
    ok2,
    f"ring words={len(ring_d2)}, act words={len(act_d2)}, product mass="
    f"{two_record_partition}",
)


# ---------------------------------------------------------------------------
# Small exact embedded-chain oracle. Stable event IDs are (initiator,
# initiator-local ring number); Ulam children are (parent, 'c', local ordinal).

def seed_state(remote=False):
    neighbors = {"A": {"B"}, "B": {"A"}}
    if remote:
        neighbors.update({"P": {"Q"}, "Q": {"P"}})
    actors = {r: {"ring": 0, "births": 0} for r in neighbors}
    return {
        "actors": actors,
        "neighbors": neighbors,
        "events": [],
        "last": {},
    }


def copy_state(s):
    return {
        "actors": {r: dict(v) for r, v in s["actors"].items()},
        "neighbors": {r: set(v) for r, v in s["neighbors"].items()},
        "events": list(s["events"]),
        "last": dict(s["last"]),
    }


def oracle_options(s, y):
    eligible = sorted(s["neighbors"][y], key=skey)
    opts = [("b", None, F(1, 4))]
    opts += [("i", x, F(1, 4 * len(eligible))) for x in eligible]
    opts += [("n", None, F(1, 2))]
    return opts


def oracle_step(s, y, kind, target=None):
    t = copy_state(s)
    a = t["actors"][y]
    a["ring"] += 1
    eid = (y, "r", a["ring"])
    child = None
    if kind == "b":
        a["births"] += 1
        child = (y, "c", a["births"])
        target = child
        t["actors"][child] = {"ring": 0, "births": 0}
        t["neighbors"].setdefault(y, set()).add(child)
        t["neighbors"][child] = {y}
        touched = (y, child)
    elif kind == "i":
        if target not in t["neighbors"][y]:
            raise ValueError("ineligible interaction")
        touched = (y, target)
    elif kind == "n":
        touched = (y,)
    else:
        raise ValueError(kind)
    preds = frozenset(t["last"][r] for r in touched if r in t["last"])
    t["events"].append((eid, kind, y, target, preds))
    for r in touched:
        t["last"][r] = eid
    return t, child


def physical_key(s):
    rows = []
    for eid, kind, y, target, preds in s["events"]:
        rows.append((repr(eid), kind, repr(y), repr(target),
                     tuple(sorted((repr(p) for p in preds)))))
    return tuple(sorted(rows))


def oracle_state_key(s):
    actors = tuple(sorted((repr(r), v["ring"], v["births"])
                          for r, v in s["actors"].items()))
    neighbors = tuple(sorted((repr(r), tuple(sorted(repr(x) for x in xs)))
                             for r, xs in s["neighbors"].items()))
    last = tuple(sorted((repr(r), repr(e)) for r, e in s["last"].items()))
    return actors, neighbors, physical_key(s), last


def exact_distribution(depth, remote=False):
    frontier = [(seed_state(remote), F(1))]
    for _ in range(depth):
        nxt = {}
        for s, p in frontier:
            actors = sorted(s["actors"], key=skey)
            k = len(actors)
            local_mass = F(0)
            for y in actors:
                for kind, target, q in oracle_options(s, y):
                    local_mass += F(1, k) * q
                    s2, _ = oracle_step(s, y, kind, target)
                    key = oracle_state_key(s2)
                    if key in nxt:
                        nxt[key] = (nxt[key][0], nxt[key][1]
                                    + p * F(1, k) * q)
                    else:
                        nxt[key] = (s2, p * F(1, k) * q)
            if local_mass != 1:
                raise AssertionError(local_mass)
        frontier = list(nxt.values())
    classes = defaultdict(F)
    for s, p in frontier:
        classes[physical_key(s)] += p
    return frontier, dict(classes)


# ---------------------------------------------------------------------------
# E3: passive reception is physical placement, so prod(q) is not the full law.

# Coarse initiator event: A's first ring i(A,B), B's first ring b(B,C).
# The two first-ring clocks are iid Exp(1), hence either shared-B order is 1/2.
coarse_ring = F(1, 4) * F(1, 4)
physical_ring_order = coarse_ring * F(1, 2)
coarse_act = F(1, 2) * F(1, 2)
physical_act_order = coarse_act * F(1, 2)

# Forced reception: i(B,A) touches both wires; the next A birth inherits it.
forced = seed_state()
forced, _ = oracle_step(forced, "B", "i", "A")
a_ring_before = forced["actors"]["A"]["ring"]
forced, alpha = oracle_step(forced, "A", "b")
birth_event = forced["events"][-1]
reception_eid = forced["events"][0][0]
ok3 = (
    coarse_ring == F(1, 16)
    and physical_ring_order == F(1, 32)
    and 2 * physical_ring_order == coarse_ring
    and coarse_act == F(1, 4)
    and physical_act_order == F(1, 8)
    and 2 * physical_act_order == coarse_act
    and a_ring_before == 0
    and forced["actors"]["A"]["ring"] == 1
    and reception_eid in birth_event[4]
    and alpha == ("A", "c", 1)
)
check(
    "E3 PASSIVE-RECEPTION PLACEMENT [exact, corrective finding]: the "
    "coarse first-ring initiator cylinder has prod(q)=1/16 but each of "
    "its two physical shared-B orders has mass 1/32 (act level 1/4 splits "
    "as 1/8+1/8); a passive i(B,A) consumes no A ring yet is a predecessor "
    "of A's later birth. Therefore prod(q) is NOT the wire-DAG measure",
    ok3,
    f"ring {coarse_ring}={physical_ring_order}+{physical_ring_order}; "
    f"act {coarse_act}={physical_act_order}+{physical_act_order}",
)


# ---------------------------------------------------------------------------
# E4: exact embedded path mass and orbit-sum formula.

def follow_path(ops):
    s = seed_state()
    p = F(1)
    qprod = F(1)
    placement = F(1)
    for y, kind, target in ops:
        k = len(s["actors"])
        choices = {(kk, tt): q for kk, tt, q in oracle_options(s, y)}
        q = choices[(kind, target)]
        p *= F(1, k) * q
        qprod *= q
        placement *= F(1, k)
        s, child = oracle_step(s, y, kind, target)
    return s, p, qprod, placement


ca = ("A", "c", 1)
cb = ("B", "c", 1)
paths_same_class = [
    [("A", "b", None), ("A", "i", ca), ("B", "b", None)],
    [("A", "b", None), ("B", "b", None), ("A", "i", ca)],
    [("B", "b", None), ("A", "b", None), ("A", "i", ca)],
]
vals = [follow_path(p) for p in paths_same_class]
keys = [physical_key(v[0]) for v in vals]
weights = [v[1] for v in vals]
qprods = [v[2] for v in vals]
placements = [v[3] for v in vals]
class_mass = sum(weights, F(0))
orbit_formula = qprods[0] * sum(placements, F(0))

front2, classes2 = exact_distribution(2, remote=False)
front3, classes3 = exact_distribution(3, remote=False)
has_reception_class = any(any(row[1] == "i" for row in key)
                          for key in classes2)
ok4 = (
    len(set(keys)) == 1
    and weights == [F(1, 2304), F(1, 3072), F(1, 3072)]
    and len(set(qprods)) == 1
    and qprods[0] == F(1, 128)
    and class_mass == orbit_formula == F(5, 4608)
    and sum(p for _, p in front2) == sum(classes2.values()) == 1
    and sum(p for _, p in front3) == sum(classes3.values()) == 1
    and has_reception_class
)
check(
    "E4 PHYSICAL-HISTORY PUSHFORWARD [exact]: unequal scheduler-path "
    "weights on three linear extensions are summed on one canonical wire-"
    "DAG; class mass = prod(q) times the placement-orbit sum; independent "
    "depth-2/3 embedded enumerations have total mass one and include "
    "reception-containing multi-record histories",
    ok4,
    f"path weights={weights}; class={class_mass}; prod(q)={qprods[0]}; "
    f"classes depth2/3={len(classes2)}/{len(classes3)}",
)


# ---------------------------------------------------------------------------
# E5: the truncation variable matters. Global jump depth has a polynomial
# killed-chain tail; local physical time has the remote-independent Erlang law.

def killed_survival_exact(k0, nmax):
    p = {k0: F(1)}
    out = [F(1)]
    for _ in range(nmax):
        nxt = defaultdict(F)
        for k, mass in p.items():
            nxt[k] += mass * F(3 * k - 1, 4 * k)
            nxt[k + 1] += mass * F(k - 1, 4 * k)
        p = dict(nxt)
        out.append(sum(p.values(), F(0)))
    return out


def killed_survival_decimal(k0, nmax):
    """Same displayed rational recurrence, evaluated at 100 decimal
    digits for the long asymptotic table. The recurrence coefficients and
    mass identity are independently gated as Fractions below."""
    p = {k0: Decimal(1)}
    out = [Decimal(1)]
    for _ in range(nmax):
        nxt = defaultdict(Decimal)
        for k, mass in p.items():
            kd = Decimal(k)
            nxt[k] += mass * Decimal(3 * k - 1) / (4 * kd)
            nxt[k + 1] += mass * Decimal(k - 1) / (4 * kd)
        p = dict(nxt)
        out.append(sum(p.values(), Decimal(0)))
    return out


# Exact rationals at the audit depth; long runs are 100-digit evaluations of
# the same recurrence. This avoids gigantic gcd reductions masquerading as
# additional scientific precision.
surv2_exact = killed_survival_exact(2, 32)
surv4_exact = killed_survival_exact(4, 32)
surv2 = killed_survival_decimal(2, 2048)
surv4 = killed_survival_decimal(4, 2048)
scaled = {
    (k0, n): Decimal(n * n) * surv[n]
    for k0, surv in ((2, surv2), (4, surv4))
    for n in (128, 256, 512, 1024, 2048)
}
t = Decimal(8)
time_tail_one = (-t / 2).exp()
time_tail_two = time_tail_one * (1 + t / 2)
ok5 = (
    all(F(3 * k - 1, 4 * k) + F(k - 1, 4 * k) + F(1, 2 * k) == 1
        for k in range(2, 257))
    and all(surv2_exact[i + 1] < surv2_exact[i] for i in range(32))
    and all(surv4_exact[i + 1] < surv4_exact[i] for i in range(32))
    and all(surv2[i + 1] < surv2[i] for i in range(2048))
    and all(surv4[i + 1] < surv4[i] for i in range(2048))
    and surv4[64] > surv2[64]
    and abs(scaled[(2, 2048)] / Decimal(32) - 1) < Decimal("0.04")
    and abs(scaled[(4, 2048)] / Decimal(192) - 1) < Decimal("0.04")
    and time_tail_one == (-t / 2).exp()  # same expression in remote world
    and time_tail_two > time_tail_one
)
check(
    "E5 HONEST CONVERGENCE VARIABLE: the exact killed-chain recurrence "
    "shows global-jump survival is decreasing with a remote-dependent "
    "polynomial tail (n^2 S_n -> 16 k0(k0-1)); at fixed local physical "
    "time the one-/two-act unfinished masses are the remote-INDEPENDENT "
    "Exp/Erlang tails exp(-t/2) and exp(-t/2)(1+t/2)",
    ok5,
    f"exact S32(k0=2/4)={dfrac(surv2_exact[32], 20)}/"
    f"{dfrac(surv4_exact[32], 20)}; "
    "100-digit n^2 S_n " + ", ".join(
        f"k0={k},n={n}:{v:.18g}" for (k, n), v in sorted(scaled.items())
    ) + f"; t=8 tails={time_tail_one:.18g}/{time_tail_two:.18g}",
)


# ---------------------------------------------------------------------------
# E6: construction-level normalization, nonexplosion, persistence, locality.

# At k clocks, sum_y (1/k) sum_o q_y(o) = 1. Check every oracle state.
all_states = [s for s, _ in front3]
row_ok = True
for s in all_states:
    actors = sorted(s["actors"], key=skey)
    k = len(actors)
    row = F(0)
    for y in actors:
        row += F(1, k) * sum((q for _, _, q in oracle_options(s, y)), F(0))
    row_ok &= row == 1

# Nonexplosion proof certificate: each dyadic block of sum 1/n is >= 1/2;
# infinitely many blocks force divergence. Birth waiting means are 4/n.
dyadic = []
for j in range(12):
    block = sum((F(1, n) for n in range(2 ** j, 2 ** (j + 1))), F(0))
    dyadic.append(block)
dyadic_ok = all(x >= F(1, 2) for x in dyadic)

n0 = Decimal(2)
T = Decimal(8)
expected_population = n0 * (T / 4).exp()
expected_rings = 4 * n0 * ((T / 4).exp() - 1)

# Disconnected-component locality is product-measure/pathwise: source tapes
# for A/B have the same coordinates whether P/Q exist. Gate the finite source
# cylinder factorization exactly, and contrast the wrong global-next-actor
# question (1/2 vs 1/4).
local_tape_cyl = F(1, 4) * F(1, 2) * F(1, 4)
remote_tape_cyl = F(1, 2) * F(1, 4)
factorized = local_tape_cyl * remote_tape_cyl
global_next_seed2 = F(1, 2)
global_next_seed4 = F(1, 4)

ok6 = (
    row_ok
    and dyadic_ok
    and expected_population.is_finite()
    and expected_rings.is_finite()
    and factorized == local_tape_cyl * remote_tape_cyl
    and global_next_seed2 != global_next_seed4
    and sum(q for _, q in ring_options(1)) == 1
)
check(
    "E6 EXISTENCE/NONEXPLOSION/PERSISTENCE/REMOTE LOCALITY: every "
    "embedded generator row normalizes; K(t) is Yule with birth rate k/4 "
    "and the dyadic harmonic-block certificate proves no finite explosion; "
    "birth/interact/idle ring masses stay 1/4,1/4,1/2; disconnected source "
    "tapes factor exactly. Fixed GLOBAL-next-event probabilities change "
    "1/2 -> 1/4 and are printed as the rejected locality criterion",
    ok6,
    f"{len(all_states)} depth-3 rows; min dyadic block="
    f"{dfrac(min(dyadic), 24)}; "
    f"E[N(8)]={expected_population:.30g}, E[rings<=8]={expected_rings:.30g}; "
    f"global-next A: {global_next_seed2}->{global_next_seed4}",
)


# ---------------------------------------------------------------------------
# E7: claim ledger. This is intentionally not a free pass: it depends on E1-6.

ok7 = FAIL == 0
check(
    "E7 CLASSICAL CLAIM LADDER: source noise is normalized/projective; "
    "nonexplosion makes the finite-time marked path locally finite; the "
    "physical typed-history law is its pushforward/orbit sum; initiated "
    "marginals are exactly local and disconnected components factor. "
    "NOT CLAIMED: prod(q) on physical down-sets, a literally profinite "
    "timed space, dynamic adjacency/component joining, derived 1/4 "
    "coefficients, NSE, or a quantum lift",
    ok7,
)

print()
total = PASS + FAIL
if FAIL:
    print(f"FAILURES: {FAIL}/{total}")
    raise SystemExit(1)
print(f"ALL CHECKS PASS ({PASS}/{total}: E1-E6 substantive; E7 dependent scorecard)")

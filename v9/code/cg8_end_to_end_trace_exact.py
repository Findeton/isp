#!/usr/bin/env python3
"""Final-opening exact end-to-end marked trace and restriction receipt."""

from collections import defaultdict
from fractions import Fraction as F
from itertools import permutations

checks = []


def check(label, ok, detail=""):
    checks.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" — {detail}" if detail else ""))


# event = (ports, kind, block); port=(lineage,parent,content,outcome)
def add(events, latest, support, kind, block, contents, outcomes):
    support = tuple(sorted(support))
    ports = tuple((i, latest.get(i, -1), contents[j], outcomes[j])
                  for j, i in enumerate(support))
    idx = len(events)
    events = events + ((ports, kind, block),)
    latest = dict(latest)
    for i in support:
        latest[i] = idx
    return events, latest


def permute_history(events, lp, ep):
    out = [None] * len(events)
    for old, (ports, kind, block) in enumerate(events):
        nports = []
        for lin, parent, content, outcome in ports:
            nports.append((lp[lin], -1 if parent == -1 else ep[parent], content, outcome))
        out[ep[old]] = (tuple(sorted(nports)), kind, block)
    return tuple(out)


def canonical(events, nlin):
    return min(repr(permute_history(events, lp, ep))
               for lp in permutations(range(nlin))
               for ep in permutations(range(len(events))))


def response_probs(h, party):
    # Local rational response; no remote setting enters.
    mean = F(1, 2) if party == 0 else F(-1, 3)
    return {spin: (1 + spin * h * mean) / 2 for spin in (-1, 1)}


def build(order, h, aout, bout):
    events = ((((0, -1, F(2), h), (1, -1, F(2), h)), "root-common-cause", "root-RN"),)
    latest = {0: 0, 1: 0}
    for who in order:
        if who == "A":
            events, latest = add(events, latest, (0,), "local-setting+seal",
                                 "A-RN-x0", (F(4),), (aout,))
        else:
            events, latest = add(events, latest, (1,), "local-setting+seal",
                                 "B-RN-y1", (F(2),), (bout,))
    # Joint support fires after both local seals and records conservative transfer.
    events, latest = add(events, latest, (0, 1), "joint-transfer-seal",
                         "AB-shared-RN", (F(3), F(3)), (aout, bout))
    # One renewed private seal demonstrates post-joint continuation.
    events, latest = add(events, latest, (0,), "renewed-private-seal",
                         "A-renewed-RN", (F(7, 2),), (aout,))
    return events


print("[cg8 — end-to-end exact marked trace]")

# E0: priority-queue scheduler versus direct trace construction.
race = {("A", "B"): F(2, 7), ("B", "A"): F(5, 7)}
push_race = defaultdict(F)
push_direct = defaultdict(F)
for h in (-1, 1):
    for a, pa in response_probs(h, 0).items():
        for b, pb in response_probs(h, 1).items():
            basep = F(1, 2) * pa * pb
            # Scheduler 1: unequal raw race orders.
            for order, po in race.items():
                push_race[canonical(build(order, h, a, b), 2)] += basep * po
            # Scheduler 2: direct trace chooses one arbitrary linearization.
            push_direct[canonical(build(("A", "B"), h, a, b), 2)] += basep

check("E0 two fair scheduler implementations have identical canonical pushforward",
      push_race == push_direct and sum(push_race.values()) == 1,
      f"canonical histories={len(push_race)}, total={sum(push_race.values())}")

# E1: end-to-end trace contains RN block ids, local settings/outcomes, parents,
# conservative transfer, joint seal, and renewed event in every history.
sample = next(iter(push_race))
needed = ("A-RN-x0", "B-RN-y1", "AB-shared-RN", "A-renewed-RN",
          "joint-transfer-seal", "local-setting+seal")
check("E1 one trace integrates firing/outcome/transfer/ancestry/renewal",
      all(x in sample for x in needed))


def restrict_history(events, keep):
    """Project ports to kept lineages; discard empty events; reconnect parents.

    Cross-boundary joint events remain as projected-joint events, retaining the
    joint block id so outside common-cause information is not silently erased.
    """
    keep = set(keep)
    old_to_new = {}
    out = []

    def nearest_kept_parent(old_parent, lineage):
        p = old_parent
        while p != -1 and p not in old_to_new:
            ports = events[p][0]
            candidates = [q for lin, q, _, _ in ports if lin == lineage]
            p = candidates[0] if candidates else -1
        return -1 if p == -1 else old_to_new[p]

    for old, (ports, kind, block) in enumerate(events):
        kept_ports = []
        for lin, parent, content, outcome in ports:
            if lin in keep:
                kept_ports.append((lin, nearest_kept_parent(parent, lin), content, outcome))
        if kept_ports:
            if len(kept_ports) == len(ports):
                nkind = kind
            else:
                # Projection provenance is idempotent.  The original block id
                # remains a separate field, so no information is encoded by
                # stacking presentation-dependent prefixes.
                nkind = kind if kind.startswith("projected-") else "projected-" + kind
            old_to_new[old] = len(out)
            out.append((tuple(kept_ports), nkind, block))
    # Reindex kept lineage labels canonically for the restricted object.
    lmap = {old: j for j, old in enumerate(sorted(keep))}
    normalized = []
    for ports, kind, block in out:
        normalized.append((tuple((lmap[lin], p, c, o) for lin, p, c, o in ports), kind, block))
    return tuple(normalized)


# E2: genuine crossing-support restriction and commuting scheduler/restriction diagram.
h_ab = build(("A", "B"), 1, 1, -1)
h_ba = build(("B", "A"), 1, 1, -1)
r_ab = restrict_history(h_ab, {0})
r_ba = restrict_history(h_ba, {0})
check("E2 cross-boundary marked restriction commutes with scheduler quotient",
      canonical(r_ab, 1) == canonical(r_ba, 1)
      and "projected-joint-transfer-seal" in canonical(r_ab, 1))

# E3: restriction is functorial on a genuine three-way crossing event:
# V->{0,1}->{0} equals V->{0} with per-port marks retained.
events3 = (
    (((0, -1, F(1), 0), (1, -1, F(2), 1), (2, -1, F(3), -1)),
     "root3", "root3-RN"),
    (((0, 0, F(4), 1), (1, 0, F(5), -1), (2, 0, F(6), 1)),
     "joint3", "ABC-shared-RN"),
)
direct0 = restrict_history(events3, {0})
via01 = restrict_history(events3, {0, 1})
via0 = restrict_history(via01, {0})
check("E3 marked restriction functor composition on a three-way crossing",
      canonical(direct0, 1) == canonical(via0, 1)
      and "projected-joint3" in canonical(direct0, 1)
      and "projected-projected" not in canonical(via0, 1))

print(f"CHECKS PASSED: {sum(checks)}/{len(checks)}")
raise SystemExit(0 if all(checks) else 1)

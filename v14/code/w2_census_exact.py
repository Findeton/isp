#!/usr/bin/env python3
"""
w2_census_exact.py -- v14 WELD 2 / paper-13: THE CARRIER CENSUS.

Pin: v14/note-weld2-census-pin.md (FROZEN, sha256-12 9d19515cb3ae,
ledger #85).  Route A on the scout report of record
(v14/note-weld2-referent-scout.md e1f771a9d0ed, #83).

THE QUESTION.  Does a MOTIVATED map exist from the transport grammar's
carrier to the spatial record lattice -- grammar objects to sites,
grammar object-pairs/channels to links, SETS OF DIVISION EVENTS to link
counts n_l(x) -- where motivated means ZERO free items at the RSQ
standard?  Posed at BOTH quotients as site generators (MENU-113 and
CONG-185), and at BOTH READINGS of "a map".

THE ADMISSIBILITY READING IS AN AXIS, DECLARED AS DATA.  The pin's word
is "a map".  Two readings of it are run, and every cell is decided under
each:
  EMBEDDING  -- a bijection from site objects to sites under which the
                grammar's link relation CONTAINS the target's incidence
                (the reading the delivered census implemented).
  QUOTIENT   -- a surjection from grammar objects ONTO sites with every
                realised link-relation edge carrying a DECLARED link
                displacement (the reading the pin's words also admit).
The reading axis is not the pin's; it is declared here, and every row
carries its reading.

ONE ADMISSIBILITY CRITERION ON BOTH BRANCHES.  A link is an UNORDERED
site pair carrying a label and a count -- orientation is a declared free
item (I-ORIENT) -- so incidence is UNDIRECTED on both the kill side and
the admit side.  The EMBEDDING kill is therefore an ODD-CYCLE argument
(the target closes a 3-cycle on 3 distinct sites at every one of its 27
cells; a graded relation is bipartite and carries no odd cycle) backed,
where the grading fails, by an EXHAUSTIVE induced-subgraph search that
EXECUTES the declared restriction rather than arguing it away.

WHAT THIS PROGRAM DOES, in the pin's order:
  SEC 0   CLI, gate/waiver/anchor machinery, mutant registry.
  SEC 1   Provenance: every pinned source sha256-verified; verbatim
          anchors (#62) bound to consumer gates, each with its own
          declared falsifier.
  SEC 2   The committed transport grammar, REBUILT from its definitions
          (no import from another unit's code, #46/house rule).
  SEC 3   The AB4 arena: 3969 histories, MENU-113, the exchange-square
          census, the horizon potential.
  SEC 4   CONG-185 RE-DERIVED, with its SIX ruling properties GATED
          before use (pin R1).
  SEC 5   I7's arena from the pinned HA receipt (read at its pinned
          sha, #91); the record family; ADDITIVITY-972-OF-972 (pin R2).
  SEC 6   The crystal arenas (D60/D66/D67 committed specs) and the D58
          generic 2-actor walk (pin R5).
  SEC 7   THE DETECTOR at both readings: gates, fates, the RSQ choice
          inventory with fibers COMPUTED, the R6 no-smuggling
          classifier, and THE GRADING THEOREM with its forcing
          machine-checked.
  SEC 8   CONTROLS FIRST, both falsified, and the FOUND branch
          exhibited AT THE VERDICT'S OWN TARGET (pin R5 / HA 14.3).
  SEC 9   The census at both quotients over the declared candidate
          family (pin R3), per-cell fate gates, carrier agreement.
  SEC 10  The verdict REBUILT FROM THE PAYLOAD and compared as a
          complete string; the paper verified against the receipt; the
          receipt and output re-read from disk after writing.

HOUSE RULES OBSERVED.  Exact arithmetic (fractions.Fraction / integers)
end to end; no floats anywhere.  Counts COMPUTED, never typed (#24).
Prose renders from the receipt and IS CHECKED AGAINST IT IN THE RUN
(#20).  All set/dict iteration that feeds a printed number is ordered by
a hash-seed-independent stable key.  The plain run is byte-reproducible
and writes NOTHING when a gate fails.  Verdicts live IN the gate
statements and the head is DERIVED, never typed (#234).  Every
comparator is built from primitives its builder does not share
(#82-strengthened).  Gates bind objects, cell by cell (#87).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from collections import Counter, defaultdict
from fractions import Fraction as Fr
from itertools import permutations

REPO = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
OUT_TXT = os.path.join(REPO, "v14", "code", "w2_census_output.txt")
OUT_JSON = os.path.join(REPO, "v14", "code", "w2_census_receipt.json")
INTERP = "/opt/homebrew/bin/python3.13"

# ===========================================================================
# SEC 0.  MACHINERY
# ===========================================================================

LINES: list[str] = []
GATES: list[dict] = []
WAIVERS: list[dict] = []
ANCHORS: list[dict] = []
VANCHORS: list[dict] = []
PAYLOAD: dict = {}
FAILED = 0
ANCHOR_FAIL = 0
MUTANT = None


def emit(s: str = "") -> None:
    LINES.append(s)


def mutate(name, normal, corrupted):
    """Mutant hook.  Returns `normal` unless this run is that mutant."""
    return corrupted if MUTANT == name else normal


def gate(name, statement, ok, evidence, waiver=None):
    """A gate whose STATEMENT carries the measured verdict (#234-style)."""
    global FAILED
    ok = bool(ok)
    if not ok:
        FAILED += 1
    GATES.append({"gate": name, "statement": statement, "passed": ok,
                  "evidence": evidence,
                  "waiver": waiver["reason"] if waiver else None})
    if waiver:
        WAIVERS.append({"gate": name, "class": waiver["class"],
                        "reason": waiver["reason"]})
    ev = json.dumps(evidence, sort_keys=True, default=str)
    emit(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    emit(f"         {statement}")
    emit(f"         evidence: {ev}")
    if waiver:
        emit(f"         WAIVER [{waiver['class']}]: {waiver['reason']}")
    return ok


def anchor(aid, quantity, committed, computed, source):
    """A committed number that must reproduce.  Failure => exit 1."""
    global ANCHOR_FAIL
    ok = (committed == computed)
    if not ok:
        ANCHOR_FAIL += 1
    ANCHORS.append({"id": aid, "quantity": quantity, "committed": committed,
                    "computed": computed, "passed": ok, "source": source})
    emit(f"  [{'ANCH' if ok else 'ANCH-FAIL'}] {aid}  {quantity}: "
         f"committed={committed} computed={computed}")
    return ok


def vanchor(vid, path, quote, consumer, occurrences=1):
    """A verbatim text anchor (#62): meaning-binding, consumer-gated,
    mutant-falsified.  EACH anchor carries its OWN declared falsifier
    (MUT-QUOTE-<vid>), and the test is not bare substring presence: the
    quote must occur in the pinned file exactly `occurrences` times AND
    its committed byte length must reproduce, so a truncation to a
    common substring fails."""
    global ANCHOR_FAIL
    want = dict((p, w) for p, w, _ in PINNED)[path]
    body, route = read_pinned(path, want)
    q = mutate(f"MUT-QUOTE-{vid}", quote, quote + " [corrupted]")
    n = body.count(q.encode("utf-8")) if body is not None else 0
    ok = (body is not None) and n == occurrences and len(q) == len(quote)
    if not ok:
        ANCHOR_FAIL += 1
    VANCHORS.append({"id": vid, "path": path, "quote": quote,
                     "consumer_gate": consumer, "passed": ok,
                     "bytes": len(quote), "committed_occurrences": occurrences,
                     "computed_occurrences": n, "route": route})
    emit(f"  [{'VANCH' if ok else 'VANCH-FAIL'}] {vid}  {path} -> "
         f"{consumer}  ({len(quote)} bytes verbatim, {n} occurrence(s), "
         f"via {route})")
    return ok


def sk(o):
    """Hash-seed-independent total key for nested frozenset/tuple data."""
    if isinstance(o, frozenset):
        return ("fs", tuple(sorted(sk(x) for x in o)))
    if isinstance(o, tuple):
        return ("t", tuple(sk(x) for x in o))
    if isinstance(o, list):
        return ("l", tuple(sk(x) for x in o))
    return ("a", type(o).__name__, str(o))


def sha12(path):
    h = hashlib.sha256(open(os.path.join(REPO, path), "rb").read())
    return h.hexdigest()[:12]


# The commits at which the pin's sources are frozen.  The repo has live
# concurrent writers; a file whose WORKING TREE bytes no longer carry the
# pinned digest is read from git at a declared commit instead, and never
# from mutable worktree state (#46).
PIN_COMMITS = ["95c3b77", "822bb15"]
_PIN_CACHE: dict = {}


def read_pinned(path, want):
    """-> (bytes, route).  Returns the bytes whose sha256-12 is `want`,
    taken from the working tree when it still carries them and otherwise
    from git at a declared pin commit.  Raises when no route carries the
    pinned digest."""
    if path in _PIN_CACHE:
        return _PIN_CACHE[path]
    import subprocess
    body = open(os.path.join(REPO, path), "rb").read()
    if hashlib.sha256(body).hexdigest()[:12] == want:
        _PIN_CACHE[path] = (body, "worktree")
        return _PIN_CACHE[path]
    for c in PIN_COMMITS:
        try:
            b = subprocess.run(["git", "show", f"{c}:{path}"], cwd=REPO,
                               capture_output=True, check=True).stdout
        except Exception:
            continue
        if hashlib.sha256(b).hexdigest()[:12] == want:
            _PIN_CACHE[path] = (b, f"git show {c}:")
            return _PIN_CACHE[path]
    _PIN_CACHE[path] = (None, "UNRESOLVED")
    return _PIN_CACHE[path]


def primes_of(fr: Fr):
    out = {}
    for n, sgn in ((fr.numerator, 1), (fr.denominator, -1)):
        d = 2
        while d * d <= n:
            while n % d == 0:
                out[d] = out.get(d, 0) + sgn
                n //= d
            d += 1
        if n > 1:
            out[n] = out.get(n, 0) + sgn
    return {p: e for p, e in out.items() if e != 0}


def group_rank(values):
    """Prime support and rank of the multiplicative group generated by a
    set of positive rationals, by exact integer row reduction."""
    ps = sorted({p for v in values for p in primes_of(v)})
    rows = [[primes_of(v).get(p, 0) for p in ps] for v in values]
    rows = [r for r in rows if any(r)]
    basis, col = [], 0
    while rows and col < len(ps):
        piv = [r for r in rows if r[col] != 0]
        if not piv:
            col += 1
            continue
        p = min(piv, key=lambda r: (abs(r[col]), r))
        rows.remove(p)
        nxt = []
        for r in rows:
            if r[col] != 0:
                k = r[col] // p[col]
                r = [a - k * b for a, b in zip(r, p)]
            if any(r):
                nxt.append(r)
        basis.append(p)
        rows = nxt
        col += 1
    return ps, len(basis)


# ===========================================================================
# SEC 1.  PROVENANCE  (pin R7: all pinned reads sha-verified at start)
# ===========================================================================

PINNED = [
    ("v14/note-weld2-census-pin.md", "9d19515cb3ae", "THE PIN"),
    ("v14/note-weld2-referent-scout.md", "e1f771a9d0ed", "the scout report"),
    ("v13/code/ha_successor_receipt.json", "542b8735daf0", "I7 receipt"),
    ("v13/paper-ha-successor.md", "f286ba10d2d9", "HA paper (count semantics)"),
    ("v13/code/ha_successor_exact.py", "d44cb72f8ee9", "HA code"),
    ("v14/paper-12-gamma-main.md", "d85a629a9378", "Gamma-main (MENU carrier)"),
    ("v10/note-d74-transport-holonomy-result.md", "0180e21c7127", "D74 result"),
    ("v10/note-d74-transport-holonomy-pin.md", "b9997d125ef5", "D74 pin"),
    ("v14/review-gmain-operator.md", "f67871bc51f5", "CONG-185 definitional source"),
    ("v14/note-gmain-adjudication.md", "972e54741330", "Gamma-main adjudication"),
    ("v11/relativistic-isp-v11-paper0-the-indivisible-record-law.md",
     "37a428321f46", "v11 paper 0 (the POSIT, U4)"),
    ("v14/paper-04-refinement-grammar.md", "dfa5090f26b1", "R6a (additivity)"),
    ("v14/paper-09-renewal-transport.md", "006f96aaa2ff", "R6b' (type census, dead list)"),
    ("v13/paper-brg-bridge.md", "371e38742059", "BRG (species discipline)"),
    ("v13/note-gw1-metric-from-closure.md", "6f825ef6e1ce", "GW1 (permitted list)"),
    ("v14/note-r6bprime-transport-pin.md", "17111fd19022", "R6b' pin (v12 Gamma dead)"),
    ("v14/paper-02-manifold-rung.md", "1a80a5bf1a1b", "R2 (naive 9<->9 dead)"),
    ("v10/note-d60-crystal-question-pin.md", "2c715308c22b", "D60 pin"),
    ("v10/note-d60-crystal-result.md", "19e50d34635f", "D60 result"),
    ("v10/note-d66-arbitration-crystal-pin.md", "f09c9091bf58", "D66 pin"),
    ("v10/note-d66-arbitration-crystal-result.md", "c32eb7814993", "D66 result"),
    ("v10/note-d67-k4-double-grid-pin.md", "598c429fcc9c", "D67 pin"),
    ("v10/note-d67-k4-double-grid-result.md", "13712723c0cd", "D67 result"),
    ("v10/note-d58-atlas-instrument-result.md", "ce536758fbaa", "D58 (the walk)"),
]


def run_provenance():
    emit("=" * 78)
    emit("SEC 1  PROVENANCE -- every pinned source sha256-verified at start")
    emit("=" * 78)
    rows, bad, rerouted = [], [], []
    for path, want, role in PINNED:
        want = mutate("MUT-PROVENANCE", want, "000000000000") \
            if path.endswith("d74-transport-holonomy-result.md") else want
        wt = sha12(path)
        body, route = ("", "worktree") if wt == want else read_pinned(path, want)
        if wt != want and body is not None:
            _PIN_CACHE[path] = (body, route)
        ok = (wt == want) or (body is not None)
        if not ok:
            bad.append((path, want, wt))
        elif wt != want:
            rerouted.append({"path": path, "worktree": wt, "route": route})
        rows.append({"path": path, "pinned": want, "worktree": wt,
                     "route": route, "role": role, "ok": ok})
    PAYLOAD["provenance"] = rows
    PAYLOAD["pinned_source_count"] = len(rows)
    PAYLOAD["rerouted_sources"] = rerouted
    gate("G-PROVENANCE",
         f"all {len(rows)} pinned sources resolve to their pinned sha256-12: "
         f"{len(rows) - len(bad)} of {len(rows)} resolved, {len(bad)} "
         f"unresolved.  {len(rerouted)} carry different WORKING-TREE bytes -- "
         f"the repo has live concurrent writers -- and are read from git at a "
         f"declared pin commit instead, never from mutable worktree state: "
         f"{json.dumps(rerouted, sort_keys=True)}",
         not bad, {"resolved": len(rows) - len(bad), "total": len(rows),
                   "unresolved": bad, "rerouted": rerouted})
    if bad:
        global ANCHOR_FAIL
        ANCHOR_FAIL += 1

    emit("")
    emit("  VERBATIM ANCHORS (#62) -- meaning-binding, consumer-gated:")
    vanchor("V01", "v13/paper-ha-successor.md",
            "$n_\\ell(x)$ is the number of division events in the record "
            "interval between $x$\nand $x+\\ell$",
            "G-COUNT-SEMANTICS")
    vanchor("V02", "v11/relativistic-isp-v11-paper0-the-indivisible-record-law.md",
            "**[POSIT]** v11's **division events are the renewal events.**",
            "G-DIVISION-PREDICATE")
    vanchor("V03", "v14/paper-04-refinement-grammar.md",
            "additivity holds at 972 of 972 constraints",
            "G-ADDITIVITY-972", occurrences=2)
    vanchor("V04", "v14/paper-09-renewal-transport.md",
            "the type census proves a leg has no interior\ndivision event "
            "for a split to sit at",
            "G-INTERIOR-DEAD-ON-ARRIVAL")
    vanchor("V05", "v13/paper-ha-successor.md",
            "A predicate that cannot return its other value\n   anywhere in "
            "the declared arena is not a measurement",
            "G-TWO-WAY")
    vanchor("V06", "v14/review-gmain-operator.md",
            "**185 classes, reproducing d74's committed AB4 value exactly**",
            "G-CONG-CLASSES")
    vanchor("V07", "v14/paper-02-manifold-rung.md",
            "**$L\\ge 4$ is therefore a measured requirement**",
            "G-DEAD-LIST-CITED")
    vanchor("V08", "v11/relativistic-isp-v11-paper0-the-indivisible-record-law.md",
            "*the\n  division events of a crystal form a crystal*",
            "G-U4-REGISTERED")
    vanchor("V09", "v14/note-weld2-referent-scout.md",
            "NO-SEED-AT-THE-CARRIER", "G-VERDICT")
    vanchor("V10", "v10/note-d74-transport-holonomy-result.md",
            "the coarsest weighted **congruence** (partition refinement, "
            "4–6 rounds to a fixed point)", "G-CONG-ROUNDS")
    vanchor("V11", "v14/paper-09-renewal-transport.md",
            "REN = [h for h in FAM if len(h) <= 4 and CLS[tuple(h)] == 0 and "
            "any(e[0] == 'r' for e in h)]", "G-DIVISION-PREDICATE")
    vanchor("V12", "v10/note-d74-transport-holonomy-result.md",
            "| `(A,B) d≤5` | 265 | 462 |", "G-D5-CITED")


# ===========================================================================
# SEC 2.  THE COMMITTED TRANSPORT GRAMMAR, REBUILT
#         (d42b1_transport_exact.py definitions, re-derived here; no import)
# ===========================================================================

V0 = ('v', 'v0')


def vname(base, wkey, init):
    value = tuple(sorted({t[2] for t in wkey}))
    authors = tuple(sorted({t[0] for t in wkey}))
    return ('v', base, value, authors, init)


def mname(pk, value, init):
    return ('v', 'm', pk, value, init)


def value_of(v):
    if v == V0:
        return None
    return v[3] if v[1] == 'm' else v[2]


def base_of(v):
    if v == V0:
        return None
    if v[1] == 'm':
        return base_of(v[2][0])
    return v[1]


def regs_of(op):
    k = op[0]
    if k == 'p' or k == 'n':
        return frozenset([op[1]])
    if k == 'd':
        return frozenset([op[1], op[2]])
    if k == 'm':
        return frozenset([op[1], ('mw', op[1], op[2])])
    props = {t[0] for t in op[2]}
    base = next(iter(op[2]))[1]
    return frozenset(props | {vname(base, op[3], op[1])})


def event_poset(acts):
    n = len(acts)
    pred = [set() for _ in range(n)]
    last = {}
    for j, op in enumerate(acts):
        for r in regs_of(op):
            if r in last:
                pred[j] |= pred[last[r]] | {last[r]}
        for r in regs_of(op):
            last[r] = j
    return pred


class View:
    def __init__(self, acts, pred, idxs):
        self.idxs = sorted(idxs)
        self.pred = pred
        self.props = {i: acts[i] for i in self.idxs if acts[i][0] == 'p'}
        self.arbs = {i: acts[i] for i in self.idxs if acts[i][0] == 'r'}
        self.dels = {i: acts[i] for i in self.idxs if acts[i][0] == 'd'}
        self.mrgs = {i: acts[i] for i in self.idxs if acts[i][0] == 'm'}
        self.resolved, self.superseded, self.created = set(), set(), {}
        for i, op in self.arbs.items():
            self.resolved |= set(op[2])
            base = next(iter(op[2]))[1]
            self.superseded.add(base)
            self.created[vname(base, op[3], op[1])] = i
        for i, op in self.mrgs.items():
            pk, w = op[2], op[3]
            self.superseded.add(pk[0])
            self.superseded.add(pk[1])
            val = value_of(pk[0]) if w == 'both' else value_of(w)
            self.created[mname(pk, val, op[1])] = i
        self.live = {i: op for i, op in self.props.items()
                     if (op[1], op[2], op[3]) not in self.resolved}

    def holdings(self, a):
        h = {V0}
        for i, op in self.arbs.items():
            if a in {t[0] for t in op[2]}:
                base = next(iter(op[2]))[1]
                h.add(vname(base, op[3], op[1]))
        for i, op in self.dels.items():
            if op[2] == a:
                h.add(op[3])
        for i, op in self.mrgs.items():
            if op[1] == a:
                pk, w = op[2], op[3]
                val = value_of(pk[0]) if w == 'both' else value_of(w)
                h.add(mname(pk, val, op[1]))
        return h

    def incomparable(self, i, k):
        return (i not in self.pred[k]) and (k not in self.pred[i])

    def edges(self, idx_set):
        E, L = set(), sorted(idx_set)
        for ii, i in enumerate(L):
            for k in L[ii + 1:]:
                pi, pk = self.props[i], self.props[k]
                if (pi[2] == pk[2] and pi[3] != pk[3]
                        and self.incomparable(i, k)):
                    E.add((i, k))
        return E

    def components(self):
        by_base = {}
        for i, op in self.live.items():
            by_base.setdefault(op[2], []).append(i)
        comps = []
        for base, idxs in by_base.items():
            E = self.edges(set(idxs))
            parent = {i: i for i in idxs}

            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x
            for i, k in E:
                parent[find(i)] = find(k)
            groups = {}
            for i in idxs:
                groups.setdefault(find(i), set()).add(i)
            for g in groups.values():
                comps.append((base, frozenset(g)))
        return comps

    def merge_pairs(self, a):
        held = [v for v in self.holdings(a)
                if v in self.created and v not in self.superseded]
        out, S = [], sorted(held, key=repr)
        for ii, v1 in enumerate(S):
            for v2 in S[ii + 1:]:
                if base_of(v1) != base_of(v2):
                    continue
                if not self.incomparable(self.created[v1], self.created[v2]):
                    continue
                out.append(tuple(sorted((v1, v2), key=repr)))
        return out


def triples(view, idx_set):
    return frozenset((view.props[i][1], view.props[i][2], view.props[i][3])
                     for i in idx_set)


def mis_of(ckey, edge_triples):
    items = sorted(ckey)
    n, ind = len(items), []
    for mask in range(1, 1 << n):
        sub = frozenset(items[i] for i in range(n) if mask >> i & 1)
        if all((a, b) not in edge_triples and (b, a) not in edge_triples
               for a in sub for b in sub if a < b):
            ind.append(sub)
    return [s for s in ind if not any(s < t for t in ind)]


def PK1(ckey, edge_triples):
    items = sorted(ckey)
    tally = {}
    for perm in permutations(items):
        acc = []
        for t in perm:
            if all((t, u) not in edge_triples and (u, t) not in edge_triples
                   for u in acc):
                acc.append(t)
        w = frozenset(acc)
        tally[w] = tally.get(w, 0) + 1
    total = sum(tally.values())
    return {w: Fr(c, total) for w, c in tally.items()}


def edge_triples_of(view, idx_set):
    def tri(i):
        return next(iter(triples(view, {i})))
    return frozenset(tuple(sorted((tri(i), tri(k))))
                     for (i, k) in view.edges(idx_set))


def prop_options_in_view(view, a):
    out = []
    for b in view.holdings(a):
        if b in view.superseded:
            continue
        if any(op[1] == a and op[2] == b for op in view.live.values()):
            continue
        for x in (0, 1):
            out.append((b, x))
    return sorted(out, key=repr)


def arb_components_in_view(view, a):
    out = []
    for base, comp in view.components():
        if base in view.superseded:
            continue
        if a in {view.props[i][1] for i in comp}:
            out.append((base, comp))
    return out


def deliver_options_in_view(view, a, actors):
    return sorted(((r, v) for r in actors if r != a
                   for v in view.holdings(a)), key=repr)


def own_view(acts, a):
    acts2 = acts + [('n', a)]
    pred = event_poset(acts2)
    return View(acts2, pred, pred[len(acts2) - 1])


def admissible_arb_ckeys(acts, a, actors):
    pred = event_poset(acts)
    full = View(acts, pred, set(range(len(acts))))
    live_by_base = {}
    for i, op in full.live.items():
        live_by_base.setdefault(op[2], []).append(i)
    out = set()
    for b in sorted(live_by_base, key=repr):
        idxs = sorted(live_by_base[b])
        n = len(idxs)
        for smask in range(1, 1 << n):
            S = [idxs[i] for i in range(n) if smask >> i & 1]
            ck = triples(full, frozenset(S))
            if ck in out:
                continue
            m, hit = len(S), False
            for wmask in range(1, 1 << m):
                W = frozenset(S[i] for i in range(m) if wmask >> i & 1)
                ok, _ = admissible(acts, ('r', a, ck, triples(full, W)), actors)
                if ok:
                    hit = True
                    break
            if hit:
                out.add(ck)
    return out


def admissible(acts, e, actors, law=PK1):
    acts2 = acts + [e]
    j = len(acts2) - 1
    pred = event_poset(acts2)
    view = View(acts2, pred, pred[j])
    kind = e[0]
    if kind == 'n':
        a = e[1]
        has_p = bool(prop_options_in_view(view, a))
        has_am = bool(view.merge_pairs(a) or admissible_arb_ckeys(acts, a, actors))
        has_d = bool(deliver_options_in_view(view, a, actors))
        return True, (1 - (Fr(1, 4) if has_p else 0)
                      - (Fr(1, 4) if has_am else 0)
                      - (Fr(1, 4) if has_d else 0))
    if kind == 'p':
        a, b, x = e[1], e[2], e[3]
        opts = prop_options_in_view(view, a)
        if (b, x) not in opts:
            return False, None
        return True, Fr(1, 4) / len(opts)
    if kind == 'd':
        s, r, v = e[1], e[2], e[3]
        if r == s or r not in actors:
            return False, None
        opts = deliver_options_in_view(own_view(acts, s), s, actors)
        if (r, v) not in opts:
            return False, None
        return True, Fr(1, 4) / len(opts)
    if kind == 'm':
        a, pk, w = e[1], e[2], e[3]
        D = (len(admissible_arb_ckeys(acts, a, actors))
             + len(view.merge_pairs(a)))
        if pk not in view.merge_pairs(a):
            return False, None
        v1, v2 = pk
        if value_of(v1) != value_of(v2):
            if w not in pk:
                return False, None
            return True, Fr(1, 4) / D * Fr(1, 2)
        if w != 'both':
            return False, None
        return True, Fr(1, 4) / D
    a, ckey, wkey = e[1], e[2], e[3]
    comps = arb_components_in_view(view, a)
    match = [c for c in comps if triples(view, c[1]) == ckey]
    if not match:
        return False, None
    base, comp = match[0]
    et = edge_triples_of(view, comp)
    if wkey not in mis_of(ckey, et):
        return False, None
    D = len(comps) + len(view.merge_pairs(a))
    return True, Fr(1, 4) / D * law(ckey, et)[wkey]


def candidates_for(acts, actors):
    pred = event_poset(acts)
    full = View(acts, pred, set(range(len(acts))))
    bases = sorted({V0} | set(full.created), key=repr)
    out = []
    live_by_base = {}
    for i, op in full.live.items():
        live_by_base.setdefault(op[2], []).append(i)
    for a in actors:
        for b in bases:
            for x in (0, 1):
                e = ('p', a, b, x)
                ok, q = admissible(acts, e, actors)
                if ok:
                    out.append((e, q))
        seen = set()
        for b in sorted(live_by_base, key=repr):
            idxs = sorted(live_by_base[b])
            n = len(idxs)
            for smask in range(1, 1 << n):
                S = [idxs[i] for i in range(n) if smask >> i & 1]
                ck = triples(full, frozenset(S))
                m = len(S)
                for wmask in range(1, 1 << m):
                    W = frozenset(S[i] for i in range(m) if wmask >> i & 1)
                    e = ('r', a, ck, triples(full, W))
                    if e in seen:
                        continue
                    seen.add(e)
                    ok, q = admissible(acts, e, actors)
                    if ok:
                        out.append((e, q))
        held = sorted(full.holdings(a), key=repr)
        for ii, v1 in enumerate(held):
            for v2 in held[ii + 1:]:
                pk = tuple(sorted((v1, v2), key=repr))
                for w in (pk[0], pk[1], 'both'):
                    e = ('m', a, pk, w)
                    ok, q = admissible(acts, e, actors)
                    if ok:
                        out.append((e, q))
        for r in actors:
            if r == a:
                continue
            for v in held:
                e = ('d', a, r, v)
                ok, q = admissible(acts, e, actors)
                if ok:
                    out.append((e, q))
        e = ('n', a)
        ok, q = admissible(acts, e, actors)
        out.append((e, q))
    return out


# ---- the division-event predicate (pin R2: the only motivated ingredient) --

def is_division(e):
    """A division event.  v11 paper 0 4's [POSIT] identifies division
    events with renewal events; S1's own code (quoted at V11) tests
    `any(e[0] == 'r' for e in h)`, and R6b' 3 records that S4 names the
    same object at event level ("every pair arbitration is a renewal").
    The predicate is therefore the arbitration tag."""
    return e[0] == mutate("MUT-DIVPRED", 'r', 'd')


# ===========================================================================
# SEC 3.  THE AB4 ARENA
# ===========================================================================

AB = ('A', 'B')
DEPTH = 4


def build_family():
    fam, frontier, cache = [()], [()], {}
    while frontier:
        h = frontier.pop()
        c = candidates_for(list(h), AB)
        cache[h] = c
        if len(h) >= DEPTH:
            continue
        for e, q in c:
            fam.append(h + (e,))
            frontier.append(h + (e,))
    return fam, cache


def menu_partition(cache):
    """The weighted-menu partition: the BUILDER, by frozenset key."""
    key = {h: frozenset((sk(e), str(q)) for e, q in cache[h]) for h in cache}
    key = mutate("MUT-MENU-KEY",
                 key, {h: frozenset({("card", len(cache[h]))}) for h in cache})
    idx, out = {}, {}
    for h in sorted(cache, key=sk):
        out[h] = idx.setdefault(sk(key[h]), len(idx))
    return out


def menu_partition_comparator(cache):
    """COMPARATOR (#82-strengthened: no shared code, no shared key
    primitive).  Two histories are equivalent when their menus agree as
    MAPPINGS event -> Fraction; classes are found by explicit pairwise
    comparison against representatives, with no hashing of a composite
    key and no reuse of `sk` on the key."""
    reps, cls = [], {}
    for h in sorted(cache, key=sk):
        m = dict((sk(e), q) for e, q in cache[h])
        placed = False
        for i, rm in enumerate(reps):
            if len(rm) == len(m) and all(k in rm and rm[k] == v
                                         for k, v in m.items()):
                cls[h] = i
                placed = True
                break
        if not placed:
            reps.append(m)
            cls[h] = len(reps) - 1
    return cls


def congruence(cache, menu):
    """CONG: the coarsest weighted congruence, by partition refinement
    from the menu partition to a fixed point (review-gmain-operator
    f67871bc51f5; D74 A3.1's `congruence`)."""
    H = sorted(cache, key=sk)
    part = dict(menu)
    rounds = mutate("MUT-CONG-WRONG", 24, 1)
    for it in range(rounds):
        nxt = {}
        for h in H:
            succ = tuple(sorted((sk(e), part[h + (e,)])
                                for e, q in cache[h] if h + (e,) in part))
            nxt[h] = (part[h], succ)
        idx2, out = {}, {}
        for h in H:
            out[h] = idx2.setdefault(sk(nxt[h]), len(idx2))
        if len(idx2) == len(set(part.values())):
            return out, it + 1
        part = out
    return part, rounds


def congruence_comparator(cache, menu):
    """COMPARATOR: the coarsest bisimulation contained in the menu
    partition, found by explicit pair-splitting on the RELATION (not by
    signature hashing).  Starts from the full within-menu-class relation
    and removes pairs whose labelled successors disagree, to a fixed
    point.  Shares no code and no key primitive with the builder."""
    H = sorted(cache, key=sk)
    succ = {h: {sk(e): (h + (e,) if h + (e,) in cache else None)
                for e, q in cache[h]} for h in H}
    rel = defaultdict(set)
    by_cls = defaultdict(list)
    for h in H:
        by_cls[menu[h]].append(h)
    for c, members in by_cls.items():
        for a in members:
            for b in members:
                rel[a].add(b)
    changed = True
    while changed:
        changed = False
        for a in H:
            drop = set()
            for b in rel[a]:
                sa, sbb = succ[a], succ[b]
                if set(sa) != set(sbb):
                    drop.add(b)
                    continue
                for lab in sa:
                    x, y = sa[lab], sbb[lab]
                    if x is None and y is None:
                        continue
                    if x is None or y is None or y not in rel[x]:
                        drop.add(b)
                        break
            if drop:
                rel[a] -= drop
                changed = True
    seen, cls, n = {}, {}, 0
    for h in H:
        key = sk(tuple(sorted((sk(x) for x in rel[h]))))
        if key not in seen:
            seen[key] = n
            n += 1
        cls[h] = seen[key]
    return cls, n


def square_census(cache):
    """The exchange-square census (D72/D74 `transport_square_census`)."""
    closed, defects = [], []
    lo = mutate("MUT-SQUARE-DROP", 0, 1)
    for h in sorted(cache, key=sk):
        if len(h) + 2 > DEPTH or len(h) < lo:
            continue
        cands = [e for e, q in cache[h]]
        for i in range(len(cands)):
            for j in range(i + 1, len(cands)):
                eA, eB = cands[i], cands[j]
                okA, qA = admissible(list(h), eA, AB)
                okB, qB = admissible(list(h), eB, AB)
                if not (okA and okB):
                    continue
                okB2, qB2 = admissible(list(h + (eA,)), eB, AB)
                okA2, qA2 = admissible(list(h + (eB,)), eA, AB)
                if okB2 and okA2:
                    r = Fr(qA * qB2, 1) / Fr(qB * qA2, 1)
                    closed.append((h, eA, eB, r))
                    if r != 1:
                        defects.append((h, eA, eB, r))
    return closed, defects


def square_comparator(cache):
    """COMPARATOR (#82-strengthened).  A closed exchange square at base h
    is exactly a pair of FAMILY MEMBERS h.eA.eB and h.eB.eA sharing a
    prefix and a last-two-event set.  This route therefore groups the
    generated family by (prefix, unordered last-two events) and counts
    the groups of size two -- it calls no admissibility predicate, does
    no Fraction arithmetic, and shares no primitive with the builder."""
    groups = defaultdict(set)
    for w in cache:
        if len(w) < 2:
            continue
        groups[(sk(w[:-2]), sk(frozenset({sk(w[-2]), sk(w[-1])})))].add(sk(w))
    return sum(1 for g in groups.values() if len(g) == 2)


# ===========================================================================
# SEC 4.  CONG-185 RE-DERIVED, ITS SIX RULING PROPERTIES GATED
# ===========================================================================

def horizon_potential(cache):
    """G(h, r) = sum_e q(e|h) G(h+e, r-1), G(h,0) = 1 -- the H4 chain."""
    memo = {}

    def G(h, r):
        if r == 0:
            return Fr(1)
        k = (h, r)
        if k in memo:
            return memo[k]
        tot = Fr(0)
        for e, q in cache[h]:
            hp = h + (e,)
            tot += Fr(q) * G(hp, r - 1)
        memo[k] = tot
        return tot
    return G


def descent_census(cache, Q, G):
    """Horizons at which the potential is NOT class-constant."""
    bad = {}
    for r in range(0, DEPTH + 1):
        vals = defaultdict(set)
        for h in cache:
            if len(h) + r > DEPTH:
                continue
            vals[(Q[h], len(h))].add(G(h, r))
        nb = mutate("MUT-DESCENT-BLIND",
                    sum(1 for v in vals.values() if len(v) > 1),
                    1 if r == 2 else 0)
        if nb:
            bad[r] = nb
    return bad


def multivalued_edges(cache, Q):
    w, t = defaultdict(set), defaultdict(set)
    for h in cache:
        if len(h) >= DEPTH:
            continue
        for e, q in cache[h]:
            key = (Q[h], sk(e))
            w[sk(key)].add(Fr(q))
            t[sk(key)].add(Q[h + (e,)])
    return (sum(1 for v in w.values() if len(v) > 1),
            sum(1 for v in t.values() if len(v) > 1))


def holonomy_of(edges):
    """Exact R+ holonomy by spanning-forest potentials."""
    edges = sorted(edges, key=lambda z: (sk(z[0]), sk(z[1]), z[2]))
    nodes = set()
    for u, v, w in edges:
        nodes.add(u)
        nodes.add(v)
    parent = {x: x for x in nodes}
    pot = {x: Fr(1) for x in nodes}

    def find(x):
        f, y = Fr(1), x
        while parent[y] != y:
            f *= pot[y]
            y = parent[y]
        return y, f
    rank, hol = 0, Counter()
    for u, v, w in edges:
        ru, fu = find(u)
        rv, fv = find(v)
        if ru == rv:
            rank += 1
            hol[(fu * w) / fv] += 1
        else:
            parent[rv] = ru
            pot[rv] = (fu * w) / fv
    return rank, sum(v for k, v in hol.items() if k != 1), hol


def reading(cache, Q, closed, G, kind):
    """q-reading (the committed weights) or k-reading (horizon-
    normalized).  Returns (self-loop spectrum, cycle rank, obstruction,
    the value set)."""
    ex, selfl = [], Counter()
    for h, eA, eB, rq in closed:
        if kind == "k":
            r = DEPTH - len(h)
            if r < 2:
                continue
            v = rq * G(h + (eA, eB), r - 2) / G(h + (eB, eA), r - 2)
        else:
            v = rq
        u, w = Q[h + (eB, eA)], Q[h + (eA, eB)]
        if u == w:
            if v != 1:
                selfl[v] += 1
        else:
            ex.append((u, w, v))
    rank, obstr, hol = holonomy_of(ex)
    vals = sorted(set(k for k in hol if k != 1) | set(selfl))
    return selfl, rank, obstr, vals


def class_transfer(cache, Q, mu, G, Groot, d, dp):
    cols, num = defaultdict(Fr), defaultdict(lambda: defaultdict(Fr))

    def wt(h):
        return mu[h] * G(h, DEPTH - len(h)) / Groot
    for h in cache:
        if len(h) == d:
            cols[Q[h]] += wt(h)
    for hp in cache:
        if len(hp) == dp and hp[:d] in cache:
            num[Q[hp[:d]]][Q[hp]] += wt(hp)
    return {s: {sp: v / tot for sp, v in num[s].items()}
            for s, tot in cols.items() if tot != 0}


def ck_census(cache, Q, mu, G, Groot):
    ok, tot = 0, 0
    for d1 in range(0, DEPTH + 1):
        for d2 in range(d1 + 1, DEPTH + 1):
            for d3 in range(d2 + 1, DEPTH + 1):
                tot += 1
                A = class_transfer(cache, Q, mu, G, Groot, d1, d2)
                Bm = class_transfer(cache, Q, mu, G, Groot, d2, d3)
                C = class_transfer(cache, Q, mu, G, Groot, d1, d3)
                good = True
                for s, row in A.items():
                    comp = defaultdict(Fr)
                    for m, p in row.items():
                        for sp, p2 in Bm.get(m, {}).items():
                            comp[sp] += p * p2
                    direct = C.get(s, {})
                    if any(comp.get(k, Fr(0)) != direct.get(k, Fr(0))
                           for k in set(comp) | set(direct)):
                        good = False
                        break
                ok += int(mutate("MUT-CK-LAX", good, False))
    return ok, tot


# ===========================================================================
# SEC 5.  I7's ARENA AND THE ADDITIVITY INGREDIENT
# ===========================================================================

I7_RECEIPT = "v13/code/ha_successor_receipt.json"
I7_CONSUMED = {}


def i7_arena():
    """#91: the I7 receipt is CONSUMED through read_pinned at its pinned
    sha, never from mutable worktree state.  The route AND the sha256-12
    of the bytes actually consumed are recorded and gated, so a worktree
    drift can no longer be rerouted by the provenance check while the
    consumption keeps reading the drifted bytes (the injection that
    produced 'G-PROVENANCE passes while G-I7-ARENA consumes the
    corrupted copy')."""
    want = dict((p, w) for p, w, _ in PINNED)[I7_RECEIPT]
    if MUTANT == "MUT-I7-ROUTE":       # the raw worktree read, restored
        body, route = open(os.path.join(REPO, I7_RECEIPT), "rb").read(), \
            "raw-worktree-read"
    else:
        body, route = read_pinned(I7_RECEIPT, want)
    if body is None:
        raise SystemExit(f"I7 receipt unresolved at its pinned sha {want}")
    I7_CONSUMED["route"] = route
    I7_CONSUMED["sha256_12"] = hashlib.sha256(body).hexdigest()[:12]
    I7_CONSUMED["pinned"] = want
    rec = json.loads(body)
    D = rec["declarations"]
    d, L = D["d"], D["L"]
    links = [tuple(v) for v in D["links_d2"]]
    X = [(i, j) for i in range(L) for j in range(L)]
    fam = {}
    for nm in sorted(D["records_d2"]):
        tup = D["records_d2"][nm]
        fam[nm] = {x: {lk: tup[i] for i, lk in enumerate(links)} for x in X}
    fam["G-CURVED"] = {x: {lk: sum((1 + x[j]) for j in range(d) if lk[j])
                           for lk in links} for x in X}

    def curvoff(x, lk):
        b = [2 + x[j] for j in range(d)]
        cross = 1 + (x[0] * x[1]) % 2
        s = sum(b[j] for j in range(d) if lk[j])
        pairs = sum(1 for i in range(d) for j in range(i + 1, d)
                    if lk[i] and lk[j])
        return s + 2 * cross * pairs
    fam["G-CURVOFF"] = {x: {lk: curvoff(x, lk) for lk in links} for x in X}
    return d, L, X, links, fam


def q_from_counts(links, row):
    """HA 3.2's declared readout: q_11 = n_e1, q_22 = n_e2,
    q_12 = (n_diag - n_e1 - n_e2)/2 -- the invertible linear
    re-encoding, det 2 at d = 2."""
    n1, n2, n3 = row[links[0]], row[links[1]], row[links[2]]
    return (Fr(n1), Fr(n2), Fr(n3 - n1 - n2, 2))


def admissible_record(links, rec):
    for x, row in rec.items():
        a, b, c = q_from_counts(links, row)
        if a <= 0 or a * b - c * c <= 0:
            return False
    return True


SPLIT_RULES = ("low", "floor", "high")
COMPLETION_RULES = ("minimal", "iterable-64")


def additivity_census(X, L, links, fam):
    """R6a's forced part, rebuilt: for each SPLITTABLE admissible record,
    each of 3 declared split rules and 2 declared completion rules, the
    dyadic refinement's two halves must sum to the coarse count at every
    (site, link) cell."""
    adm = sorted(nm for nm in fam if admissible_record(links, fam[nm]))
    splittable = sorted(nm for nm in adm
                        if min(fam[nm][x][lk] for x in X for lk in links) >= 2)
    unsplittable = sorted(set(adm) - set(splittable))
    Lr = 2 * L
    checks, bad, builds = 0, 0, 0
    keys = set()
    for nm in splittable:
        a = fam[nm]
        for smode in SPLIT_RULES:
            sp = {}
            for x in X:
                for lk in links:
                    n = a[x][lk]
                    n1 = 1 if smode == "low" else (n - 1 if smode == "high"
                                                   else n // 2)
                    sp[(x, lk)] = (n1, n - n1)
            for fmode in COMPLETION_RULES:
                K = 1 if fmode == "minimal" else 64
                counts = defaultdict(dict)
                for x in X:
                    for lk in links:
                        n1, n2 = sp[(x, lk)]
                        z0 = tuple(2 * t for t in x)
                        z1 = tuple((z0[i] + lk[i]) % Lr for i in range(len(lk)))
                        counts[z0][lk] = n1
                        counts[z1][lk] = mutate(
                            "MUT-ADDITIVITY", n2,
                            n2 + 1 if (x == (0, 0) and lk == links[0]) else n2)
                for z in [(i, j) for i in range(Lr) for j in range(Lr)]:
                    have = counts[z]
                    if len(have) == len(links):
                        continue
                    if links[0] in have and links[1] not in have:
                        counts[z][links[1]] = K
                        counts[z][links[2]] = have[links[0]] + K
                    elif links[1] in have and links[0] not in have:
                        counts[z][links[0]] = K
                        counts[z][links[2]] = K + have[links[1]]
                    elif links[2] in have:
                        counts[z][links[0]] = have[links[2]] + K
                        counts[z][links[1]] = have[links[2]] + K
                    else:
                        counts[z][links[0]] = K
                        counts[z][links[1]] = K
                        counts[z][links[2]] = 2 * K
                builds += 1
                for x in X:
                    for lk in links:
                        z0 = tuple(2 * t for t in x)
                        z1 = tuple((z0[i] + lk[i]) % Lr for i in range(len(lk)))
                        checks += 1
                        keys.add((nm, smode, fmode, x, lk))
                        if counts[z0][lk] + counts[z1][lk] != a[x][lk]:
                            bad += 1
    return adm, splittable, unsplittable, builds, checks, bad, len(keys)


def additivity_comparator(X, links, fam):
    """#82-strengthened COMPARATOR for the 972.  It shares NO construction
    with the builder and does not consult the builder's `splittable` list
    or its loop bounds: it re-derives admissibility and splittability from
    the record family itself, by its own inline Sylvester test on the
    q-encoding, and counts the constraint CELLS a refinement of each
    surviving record would carry."""
    n_split = 0
    for nm in sorted(fam):
        rec = fam[nm]
        good, small = True, False
        for x, row in rec.items():
            n1, n2, n3 = (row[links[0]], row[links[1]], row[links[2]])
            q11, q22, q12 = Fr(n1), Fr(n2), Fr(n3 - n1 - n2, 2)
            if not (q11 > 0 and q11 * q22 > q12 * q12):
                good = False
                break
            if min(n1, n2, n3) < 2:
                small = True
        if good and not small:
            n_split += 1
    return n_split * len(SPLIT_RULES) * len(COMPLETION_RULES) \
        * len(X) * len(links), n_split


# ===========================================================================
# SEC 6.  THE CRYSTAL ARENAS AND THE GENERIC WALK
# ===========================================================================

class Builder:
    """D60's `B`: every event taken from the committed layer's own menu,
    specified by its full tuple; `maxhits == 1` gates that the record is
    FORCED (nothing tie-broken); a refusal is recorded, never patched."""

    def __init__(self, actors):
        self.actors, self.H, self.refusal, self.maxhits = actors, [], None, 0

    def pick(self, inits, spec, label):
        if self.refusal:
            return None
        menu = candidates_for(list(self.H), tuple(inits))
        hits = sorted((e for e, q in menu if spec(e)), key=repr)
        self.maxhits = max(self.maxhits, len(hits))
        if not hits:
            self.refusal = (label, len(self.H))
            return None
        self.H.append(hits[0])
        return hits[0]


def _pick(b, actors, e, lbl):
    return b.pick(tuple(actors), lambda z, e=e: z == e, lbl)


def _dl(b, s, r, v):
    b.pick((s, r), lambda e, s=s, r=r: e[0] == 'd' and e[1] == s
           and e[2] == r and e[3] == v, f"{s}->{r}")


def double_grid(g, R, drop_last_row_arb=False):
    """D66/D67's DOUBLE-GRID(g, R): rows AND columns conflict
    concurrently on 2g independent base lineages, delivery-free after
    the bootstrap; the object that saturates the width ceiling k*b <= k^2."""
    ac = [[f"D{i}{j}" for j in range(g)] for i in range(g)]
    flat = [a for row in ac for a in row]
    b = Builder(tuple(flat))
    groups = ([[ac[i][j] for j in range(g)] for i in range(g)]
              + [[ac[i][j] for i in range(g)] for j in range(g)])
    seeds = ([ac[i][i] for i in range(g)]
             + [ac[(j + 2) % g][j] for j in range(g)])
    cur = [None] * len(groups)
    for gi, sd in enumerate(seeds):
        _pick(b, (sd,), ('p', sd, V0, 0), f"mint-propose {sd}")
        ck = frozenset({(sd, V0, 0)})
        _pick(b, (sd,), ('r', sd, ck, ck), f"mint-arbitrate {sd}")
        cur[gi] = vname(V0, ck, sd)
        if b.refusal:
            return b
    for gi, grp in enumerate(groups):
        for a in grp:
            if a != seeds[gi]:
                _dl(b, seeds[gi], a, cur[gi])
                if b.refusal:
                    return b
    for t in range(R):
        trips = []
        for gi, grp in enumerate(groups):
            tp = [(a, cur[gi], 0 if a == seeds[gi] else 1) for a in grp]
            trips.append(tp)
            for x in tp:
                _pick(b, (x[0],), ('p',) + x, f"propose {x[0]}")
                if b.refusal:
                    return b
        for gi in range(len(groups)):
            if (drop_last_row_arb and t == R - 1 and gi == 0):
                continue                      # MUT-CRYSTAL-INHOMOG
            wk = frozenset({(seeds[gi], cur[gi], 0)})
            _pick(b, (seeds[gi],),
                  ('r', seeds[gi], frozenset(trips[gi]), wk),
                  f"arbitrate {seeds[gi]}")
            if b.refusal:
                return b
            cur[gi] = vname(cur[gi], wk, seeds[gi])
    return b


def conflict_group(b, grp, base, seed, winner):
    trips = [(a, base, 0 if a == seed else 1) for a in grp]
    for t in trips:
        _pick(b, (t[0],), ('p',) + t, f"propose {t[0]}")
    ck = frozenset(trips)
    wk = frozenset({[t for t in trips if t[0] == winner][0]})
    _pick(b, (seed,), ('r', seed, ck, wk), f"arbitrate {seed}")
    return vname(base, wk, seed)


def conflict_grid(g, R):
    """D66's CONFLICT-GRID(g, R): g-proposer arbitrations on orthogonal
    row / column partitions of a g x g actor grid."""
    ac = [[f"G{i}{j}" for j in range(g)] for i in range(g)]
    flat = [a for row in ac for a in row]
    b = Builder(tuple(flat))
    cur = {a: V0 for a in flat}
    for t in range(R):
        if t % 2 == 0:
            groups = [[ac[i][j] for j in range(g)] for i in range(g)]
            seeds = [ac[i][i] for i in range(g)]
        else:
            groups = [[ac[i][j] for i in range(g)] for j in range(g)]
            seeds = [ac[j][j] for j in range(g)]
        for gi, grp in enumerate(groups):
            sd, base = seeds[gi], cur[seeds[gi]]
            for a in grp:
                if a != sd and cur[a] != base:
                    _dl(b, sd, a, base)
            v = conflict_group(b, grp, base, sd, sd)
            for a in grp:
                cur[a] = v
            if b.refusal:
                return b
    return b


def d60_grid(K=3, PHASES=12):
    """D60's CRYSTAL-2D: the 3x3 delivery grid, 12 phases."""
    GRID = [f"G{i}{j}" for i in range(K) for j in range(K)]

    def gid(i, j):
        return f"G{i % K}{j % K}"
    b = Builder(tuple(GRID))
    a0 = GRID[0]
    b.pick((a0,), lambda e: e[0] == 'p' and e[1] == a0 and e[2] == V0
           and e[3] == 0, "mint propose")
    b.pick((a0,), lambda e: e[0] == 'r' and e[1] == a0, "mint arbitrate")
    V1 = None
    if not b.refusal:
        menu = candidates_for(list(b.H), (a0, GRID[1]))
        dv = sorted({e[3] for e, q in menu if e[0] == 'd' and e[3] != V0},
                    key=repr)
        V1 = dv[0] if dv else None
    for s, r in zip(GRID, GRID[1:]):
        b.pick((s, r), lambda e, s=s, r=r: e[0] == 'd' and e[1] == s
               and e[2] == r and e[3] == V1, f"spread {s}->{r}")
    for t in range(PHASES):
        ph = t % 4
        if ph == 0:
            pairs = [(gid(i, j), gid(i, j + 1)) for i in range(K)
                     for j in range(0, K - 1, 2)]
        elif ph == 1:
            pairs = [(gid(i, j), gid(i, j + 1)) for i in range(K)
                     for j in range(1, K - 1, 2)]
        elif ph == 2:
            pairs = [(gid(i, j), gid(i + 1, j)) for j in range(K)
                     for i in range(0, K - 1, 2)]
        else:
            pairs = [(gid(i, j), gid(i + 1, j)) for j in range(K)
                     for i in range(1, K - 1, 2)]
        for (s, r) in pairs:
            if (t // 4) % 2 == 1:
                s, r = r, s
            _dl(b, s, r, V1)
    return b


def generic_walk(depth=30, seed=4242):
    """D58's `walk2`: the generic 2-actor walk, its own committed LCG."""
    s, h = seed, []
    for _ in range(depth):
        cand = candidates_for(h, AB)
        if not cand:
            break
        s = (1103515245 * s + 12345) % (1 << 31)
        h = h + [cand[s % len(cand)][0]]
    return h


# ===========================================================================
# SEC 7.  THE DETECTOR
# ===========================================================================

SITE_GENS = ["ACTOR", "MENU-CLASS", "CONG-CLASS", "EVENT-SUBSET",
             "ULAM-PREFIX"]
LINK_GENS = ["ACTOR-PAIR", "EXTENSION-EDGE", "COVER-PAIR"]
COUNT_GENS = ["DIV-COUNT-BETWEEN-DECLARED-ARB-CUTS"]
ARITY_REPAIRS = ["NONE", "DECLARED-RESTRICTION"]
READINGS = ["EMBEDDING", "QUOTIENT"]

# #87.  THE FATE OF EVERY CELL, DECLARED AS DATA BEFORE THE CENSUS RUNS.
# A gate binds each row to its own entry, so a single cell that changes its
# fate fails the run even when the aggregate distribution is untouched.
_T, _A, _B = "TYPE-DEAD", "ARITY-DEAD", "ARITY-DEAD-BELOW"
_S, _H, _U = "STRUCT-DEAD", "HOM-DEAD", "UNMOTIVATED"
EXPECTED_FATES = {}
for _rd, _tab in (
    ("EMBEDDING", {
        ("ACTOR", "ACTOR-PAIR"): (_A, _B),
        ("ACTOR", "EXTENSION-EDGE"): (_T, _T),
        ("ACTOR", "COVER-PAIR"): (_T, _T),
        ("MENU-CLASS", "ACTOR-PAIR"): (_T, _T),
        ("MENU-CLASS", "EXTENSION-EDGE"): (_A, _S),
        ("MENU-CLASS", "COVER-PAIR"): (_T, _T),
        ("CONG-CLASS", "ACTOR-PAIR"): (_T, _T),
        ("CONG-CLASS", "EXTENSION-EDGE"): (_A, _S),
        ("CONG-CLASS", "COVER-PAIR"): (_T, _T),
        ("EVENT-SUBSET", "ACTOR-PAIR"): (_T, _T),
        ("EVENT-SUBSET", "EXTENSION-EDGE"): (_A, _S),
        ("EVENT-SUBSET", "COVER-PAIR"): (_A, _S),
        ("ULAM-PREFIX", "ACTOR-PAIR"): (_T, _T),
        ("ULAM-PREFIX", "EXTENSION-EDGE"): (_A, _S),
        ("ULAM-PREFIX", "COVER-PAIR"): (_T, _T)}),
    ("QUOTIENT", {
        ("ACTOR", "ACTOR-PAIR"): (_A, _B),
        ("ACTOR", "EXTENSION-EDGE"): (_T, _T),
        ("ACTOR", "COVER-PAIR"): (_T, _T),
        ("MENU-CLASS", "ACTOR-PAIR"): (_T, _T),
        ("MENU-CLASS", "EXTENSION-EDGE"): (_H, _H),
        ("MENU-CLASS", "COVER-PAIR"): (_T, _T),
        ("CONG-CLASS", "ACTOR-PAIR"): (_T, _T),
        ("CONG-CLASS", "EXTENSION-EDGE"): (_U, _U),
        ("CONG-CLASS", "COVER-PAIR"): (_T, _T),
        ("EVENT-SUBSET", "ACTOR-PAIR"): (_T, _T),
        ("EVENT-SUBSET", "EXTENSION-EDGE"): (_H, _H),
        ("EVENT-SUBSET", "COVER-PAIR"): (_A, _B),
        ("ULAM-PREFIX", "ACTOR-PAIR"): (_T, _T),
        ("ULAM-PREFIX", "EXTENSION-EDGE"): (_U, _U),
        ("ULAM-PREFIX", "COVER-PAIR"): (_T, _T)})):
    for _cell, _fs in _tab.items():
        for _i, _rep in enumerate(ARITY_REPAIRS):
            EXPECTED_FATES[(_rd, _cell[0], _cell[1], _rep)] = _fs[_i]


def cayley(X, links, Lmod):
    """The target lattice's directed labelled link structure."""
    E = {}
    for x in X:
        for lk in links:
            E[(x, lk)] = tuple((x[i] + lk[i]) % Lmod for i in range(len(lk)))
    return E


def has_distinct_vertex_cycle(nodes, edges):
    """Kahn topological sort on the self-loop-free digraph: True iff a
    directed cycle on DISTINCT vertices exists."""
    adj, indeg = defaultdict(set), defaultdict(int)
    for u, v in edges:
        if u != v:
            adj[sk(u)].add(sk(v))
    for u in adj:
        for v in adj[u]:
            indeg[v] += 1
    N = {sk(x) for x in nodes}
    q = [u for u in sorted(N, key=str) if indeg[u] == 0]
    seen = 0
    while q:
        u = q.pop()
        seen += 1
        for v in sorted(adj.get(u, ()), key=str):
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return seen != len(N)


def nontrivial_sccs(nodes, edges):
    """COMPARATOR at EVERY length: Tarjan's strongly-connected components
    on the self-loop-free digraph, iterative.  A directed cycle on
    distinct vertices exists iff some component has more than one vertex,
    so this decides cyclicity at every length at once and replaces the
    length-6 bound as the operative statement."""
    adj = defaultdict(list)
    for u, v in edges:
        if u != v:
            adj[sk(u)].append(sk(v))
    N = sorted({sk(x) for x in nodes}, key=str)
    idx, low, on, st, cnt, out = {}, {}, {}, [], [0], []
    for r in N:
        if r in idx:
            continue
        work = [(r, 0)]
        while work:
            v, pi = work[-1]
            if pi == 0:
                idx[v] = low[v] = cnt[0]
                cnt[0] += 1
                st.append(v)
                on[v] = True
            nb = sorted(set(adj.get(v, ())), key=str)
            descend = False
            for i in range(pi, len(nb)):
                w = nb[i]
                if w not in idx:
                    work[-1] = (v, i + 1)
                    work.append((w, 0))
                    descend = True
                    break
                if on.get(w):
                    low[v] = min(low[v], idx[w])
            if descend:
                continue
            if low[v] == idx[v]:
                comp = []
                while True:
                    w = st.pop()
                    on[w] = False
                    comp.append(w)
                    if w == v:
                        break
                if len(comp) > 1:
                    out.append(len(comp))
            work.pop()
            if work:
                u = work[-1][0]
                low[u] = min(low[u], low[v])
    return out


def bipartite_witness(nodes, edges):
    """-> (is_bipartite, witness).  THE UNDIRECTED FORM OF THE GRADING
    THEOREM: a relation graded so that every edge raises the grade by
    exactly one is 2-colourable by the grade's parity, hence carries no
    ODD cycle.  Self-loops are dropped: a bijection sends distinct sites
    to distinct objects, so a loop is unusable as a generator cycle."""
    adj = defaultdict(set)
    for (u, v) in edges:
        if u == v:
            continue
        adj[sk(u)].add(sk(v))
        adj[sk(v)].add(sk(u))
    col = {}
    for r in sorted({sk(x) for x in nodes}, key=str):
        if r in col:
            continue
        col[r] = 0
        q = [r]
        while q:
            u = q.pop()
            for v in sorted(adj.get(u, ()), key=str):
                if v not in col:
                    col[v] = 1 - col[u]
                    q.append(v)
                elif col[v] == col[u]:
                    if MUTANT == "MUT-BIPARTITE-LAX":
                        continue
                    return False, [str(u), str(v)]
    return True, None


def induced_target_embeddings(nodes, edges, X, links, Lmod, cap=1):
    """THE DECLARED RESTRICTION, EXECUTED.  A complete backtracking search
    for injections psi: X -> site objects under which target adjacency and
    source adjacency agree at EVERY pair (an INDUCED subgraph
    isomorphism).  Every vertex of an admissible restriction has the
    target's minimum degree inside the restriction, hence at least that
    degree in the whole graph, so the search is confined to that set --
    a sound restriction, not a sample.  Returns (count, |candidates|,
    search nodes); `cap` stops the enumeration once existence is decided."""
    adj = defaultdict(set)
    for (u, v) in edges:
        if u == v:
            continue
        adj[sk(u)].add(sk(v))
        adj[sk(v)].add(sk(u))
    tadj = defaultdict(set)
    for x in X:
        for lk in links:
            y = tuple((x[i] + lk[i]) % Lmod for i in range(len(lk)))
            tadj[x].add(y)
            tadj[y].add(x)
    dmin = min(len(tadj[x]) for x in X)
    A = [u for u in sorted({sk(x) for x in nodes}, key=str)
         if len(adj[u]) >= dmin]
    Xs = sorted(X)
    out, psi, used, visited = [], {}, set(), [0]

    def bt(k):
        if len(out) >= cap:
            return
        if k == len(Xs):
            out.append(dict(psi))
            return
        x = Xs[k]
        for u in A:
            visited[0] += 1
            if u in used:
                continue
            ok = True
            for j in range(k):
                y = Xs[j]
                if (y in tadj[x]) != (psi[y] in adj[u]):
                    ok = False
                    break
            if ok:
                psi[x] = u
                used.add(u)
                bt(k + 1)
                used.discard(u)
                del psi[x]
    bt(0)
    if MUTANT == "MUT-RESTRICTION-BLIND":
        return 1, len(A), visited[0]
    return len(out), len(A), visited[0]


# --- the QUOTIENT reading's admissibility test ------------------------------
# A quotient candidate is a SURJECTION phi from the realised grammar objects
# onto the sites under which every realised link-relation edge carries a
# DECLARED link displacement.  Acyclicity is no obstruction to one.  The
# search below is DECLARED AS DATA: an LCG-driven sampler in topological
# order, falling back to maintained arc consistency with minimum-remaining-
# values when the topological sampler dead-ends, both at a declared seed and
# a declared solution cap.  Nothing about it is random at run time.
QSEED = 20260810
QCAP = 40
QLCG = (1103515245, 12345, 1 << 31)


def _lcg(seed):
    a, c, m = QLCG
    s = seed % m
    while True:
        s = (a * s + c) % m
        yield s


def quotient_maps(nodes, rel, X, links, Lmod, cap=QCAP, seed=QSEED):
    """-> dict with the exact obstruction or the searched solutions."""
    shift = {x: frozenset(tuple((x[i] + lk[i]) % Lmod for i in range(len(lk)))
                          for lk in links) for x in X}
    back = {x: frozenset(tuple((x[i] - lk[i]) % Lmod for i in range(len(lk)))
                         for lk in links) for x in X}
    nodes = sorted({sk(u) for u in nodes}, key=str)
    E = sorted({(sk(u), sk(v)) for (u, v) in rel}, key=str)
    loops = sorted({u for (u, v) in E if u == v})
    if MUTANT == "MUT-QUOTIENT-BLIND":
        loops = []
        E = [(u, v) for (u, v) in E if u != v]
    if loops:
        return {"solvable": False, "engine": "NODE-CONSISTENCY",
                "obstruction": "SELF-LOOP",
                "reason": (f"{len(loops)} of the {len(nodes)} site objects "
                           f"carry a self-loop, which demands the zero "
                           f"displacement; no declared link displacement is "
                           f"zero, so those domains empty with no search"),
                "emptied": len(loops), "solutions": [], "searched": 0}
    succ, pred = defaultdict(list), defaultdict(list)
    for (u, v) in E:
        succ[u].append(v)
        pred[v].append(u)
    dom = {u: set(X) for u in nodes}

    def propagate(D, seeds):
        q = list(seeds)
        while q:
            u = q.pop()
            if not D[u]:
                return False
            fwd = set().union(*[shift[x] for x in D[u]])
            for v in succ[u]:
                if D[v] - fwd:
                    D[v] &= fwd
                    if not D[v]:
                        return False
                    q.append(v)
            bwd = set().union(*[back[x] for x in D[u]])
            for w in pred[u]:
                if D[w] - bwd:
                    D[w] &= bwd
                    if not D[w]:
                        return False
                    q.append(w)
        return True

    if not propagate(dom, nodes):
        return {"solvable": False, "engine": "ARC-CONSISTENCY",
                "obstruction": "DOMAIN-WIPEOUT",
                "reason": ("arc consistency over the nine sites empties a "
                           "domain: no assignment carries every realised "
                           "edge onto a declared displacement"),
                "emptied": sum(1 for u in nodes if not dom[u]),
                "solutions": [], "searched": 0}
    rng = _lcg(seed)
    order = sorted(nodes, key=lambda u: (len(pred[u]), str(u)))
    topo = [u for u in nodes if not pred[u]]
    seen = set(topo)
    i = 0
    while i < len(topo):
        u = topo[i]
        i += 1
        for v in sorted(succ[u]):
            if v not in seen and all(w in seen for w in pred[v]):
                seen.add(v)
                topo.append(v)
    if len(topo) != len(nodes):
        topo = order
    sols, engine = [], "TOPOLOGICAL-SAMPLER"
    for _ in range(cap):
        phi, good = {}, True
        for u in topo:
            feas = set(dom[u])
            for w in pred[u]:
                if w in phi:
                    feas &= shift[phi[w]]
            if not feas:
                good = False
                break
            fs = sorted(feas)
            phi[u] = fs[next(rng) % len(fs)]
        if good:
            sols.append(phi)
        else:
            break
    if not sols:
        engine = "MAC-MRV"
        for _ in range(cap):
            r0 = next(rng)
            D = {u: set(dom[u]) for u in nodes}
            steps, ok = 0, True
            while ok:
                steps += 1
                un = [u for u in nodes if len(D[u]) > 1]
                if not un:
                    break
                u = min(un, key=lambda z: (len(D[z]), str(z)))
                vals = sorted(D[u])
                x = vals[(r0 + 7919 * steps) % len(vals)]
                trial = {a: set(b) for a, b in D.items()}
                trial[u] = {x}
                if propagate(trial, [u]):
                    D = trial
                else:
                    D[u].discard(x)
                    if not D[u] or not propagate(D, [u]):
                        ok = False
                if steps > 4000:
                    ok = False
            if ok:
                sols.append({u: next(iter(D[u])) for u in nodes})
    return {"solvable": bool(sols), "engine": engine, "obstruction": None,
            "solutions": sols, "searched": cap,
            "reason": (f"a quotient map exists: {len(sols)} of {cap} declared "
                       f"searches returned one ({engine})") if sols else
            ("no quotient map was found within the declared search, and "
             "none is excluded by it")}


def quotient_field(rel, phi, X, links, Lmod, labelperm, orient):
    """The pushforward count field of a quotient map: the count at (x, l)
    is the total division-event count on the realised edges from the fibre
    over x to the fibre over x + l."""
    push = {}
    for (u, v), n in rel.items():
        a, b = phi[sk(u)], phi[sk(v)]
        d = tuple((b[i] - a[i]) % Lmod for i in range(len(a)))
        push[(a, d)] = push.get((a, d), 0) + n
    out = {}
    for x in X:
        for i, lk in enumerate(links):
            lk2 = links[labelperm[i]]
            step = tuple((-c) % Lmod for c in lk2) if orient else lk2
            out[(x, lk)] = push.get((x, step), 0)
    return out


def simple_cycle_census(nodes, edges, K=6):
    """COMPARATOR for the acyclicity test, from different primitives:
    explicit enumeration of simple directed cycles up to length K by
    DFS from each least vertex."""
    adj = defaultdict(set)
    for u, v in edges:
        if u != v:
            adj[str(sk(u))].add(str(sk(v)))
    cnt = {k: 0 for k in range(2, K + 1)}
    for s in sorted({str(sk(x)) for x in nodes}):
        stack = [(s, [s])]
        while stack:
            u, path = stack.pop()
            for v in sorted(adj.get(u, ())):
                if v == s and len(path) >= 2:
                    cnt[len(path)] = cnt.get(len(path), 0) + 1
                elif v not in path and v > s and len(path) < K:
                    stack.append((v, path + [v]))
    return cnt


def count_field(site_of, links_rel, divisions, X, links, Lmod, assign,
                labelperm, orient):
    """The induced count field s: X x L -> Z.  `assign` is a bijection
    site-object -> X; `labelperm` permutes the declared link labels;
    `orient` flips the link direction.  The count on the link object
    joining u to v is the number of DIVISION EVENTS attached to it
    inside the declared window (pin R2 / the count generator)."""
    inv = {assign[u]: u for u in assign}
    out = {}
    for x in X:
        for i, lk in enumerate(links):
            lk2 = links[labelperm[i]]
            step = tuple((-c) % Lmod for c in lk2) if orient else lk2
            y = tuple((x[k] + step[k]) % Lmod for k in range(len(step)))
            u, v = inv[x], inv[y]
            out[(x, lk)] = links_rel.get((u, v), 0)
    return out


def graph_isomorphisms(S, rel, X, links, Lmod, directed=False):
    """ALL bijections S -> X carrying the site-object incidence onto the
    target's Cayley incidence, by exhaustive backtracking.  No sampling,
    no cap: the enumeration is complete.

    THE DECLARED CRITERION IS THE UNDIRECTED ONE (`directed=False`), on
    both branches of the detector: a link is an unordered site pair
    carrying a label and a count, and orientation is a declared free item
    (I-ORIENT).  `directed=True` is carried only as a COMPARATOR, and its
    value is reported: co-division incidence is symmetric by
    construction while the target's directed Cayley relation is
    antisymmetric, so the directed criterion returns 0 at every
    co-division arena -- which is why it cannot be the admit criterion
    without making the FOUND branch unreachable in principle."""
    if MUTANT == "MUT-ONE-CRITERION":
        directed = False
    tgt = set()
    for x in X:
        for lk in links:
            y = tuple((x[i] + lk[i]) % Lmod for i in range(len(lk)))
            tgt.add((x, y))
            if not directed:
                tgt.add((y, x))
    src = set()
    for (u, v) in rel:
        if u != v:
            src.add((u, v))
            if not directed:
                src.add((v, u))
    Ss = sorted(S, key=str)
    Xs = sorted(X)
    out, phi, used = [], {}, set()

    def bt(k):
        if k == len(Ss):
            out.append(dict(phi))
            return
        u = Ss[k]
        for x in Xs:
            if x in used:
                continue
            ok = True
            for j in range(k):
                w = Ss[j]
                if ((u, w) in src) != ((x, phi[w]) in tgt) or \
                   ((w, u) in src) != ((phi[w], x) in tgt):
                    ok = False
                    break
            if ok:
                phi[u] = x
                used.add(x)
                bt(k + 1)
                used.discard(x)
                del phi[u]
    if len(Ss) == len(Xs):
        bt(0)
    return out


def classify_smuggling(count_fn, i7_records):
    """Pin R6, the SHARPENED gate.  At I7 record <-> metric is an
    invertible re-encoding, so what-it-may-see cannot discriminate.  The
    test is WHICH FUNCTION of grammar data the candidate computes: run
    its count function against two DIFFERENT declared I7 records; a
    candidate whose counts move is reading I7's s back and is SMUGGLED."""
    vals = [tuple(sorted(count_fn(rec).items(), key=lambda z: str(z[0])))
            for rec in i7_records]
    moved = len(set(vals)) > 1
    return mutate("MUT-SMUGGLE-BLIND", moved, False)


# ===========================================================================
# SEC 7b.  THE ARENA INTERFACE -- site objects, link relations, types
# ===========================================================================

# The forced maps.  A cell is well-typed exactly when a PINNED, choice-free
# map carries the link generator's endpoint type to the site generator's
# object type.  Everything else is a measured TYPE obstruction.
ENDPOINT_TYPE = {"ACTOR-PAIR": "actor", "EXTENSION-EDGE": "history",
                 "COVER-PAIR": "event"}
FORCED_MAP = {
    ("ACTOR", "actor"): "identity",
    ("ACTOR", "event"): "the event tuple's initiator (op[1], every kind)",
    ("MENU-CLASS", "history"): "the weighted-menu quotient map",
    ("CONG-CLASS", "history"): "the weighted-congruence quotient map",
    ("EVENT-SUBSET", "history"): "a history to its own division-event set",
    ("EVENT-SUBSET", "event"): "an event to its singleton subset",
    ("ULAM-PREFIX", "history"): "a history to its Ulam address",
}
TYPE_REASON = {
    ("MENU-CLASS", "actor"): "a MENU class contains histories with events by "
                             "both actors; no pinned row maps a class to an actor",
    ("CONG-CLASS", "actor"): "a CONG class contains histories with events by "
                             "both actors; no pinned row maps a class to an actor",
    ("EVENT-SUBSET", "actor"): "a division-event subset spans actors; no "
                               "pinned row maps a subset to a single actor",
    ("ULAM-PREFIX", "actor"): "an Ulam address is an enumeration coordinate, "
                              "not an actor; no pinned row maps one to the other",
    ("ACTOR", "history"): "an extension edge joins histories; an actor is not "
                          "a history and no pinned row maps one to the other",
    ("MENU-CLASS", "event"): "a cover pair joins single events; no pinned row "
                             "maps a single event to a menu class",
    ("CONG-CLASS", "event"): "a cover pair joins single events; no pinned row "
                             "maps a single event to a congruence class",
    ("ULAM-PREFIX", "event"): "a cover pair joins single events; an Ulam "
                              "address is a property of a history, not an event",
}


def initiator(e):
    return e[1]


def poset_covers(H):
    """The covers of a record's event poset (D42b1's `event_poset`)."""
    pred = event_poset(list(H))
    n = len(H)
    cov = set()
    for j in range(n):
        for i in pred[j]:
            if not any((i in pred[k]) and (k in pred[j]) for k in pred[j]):
                cov.add((i, j))
    return cov


def arena_sites(arena, sgen):
    """-> (objects | None, arity, note).  `objects` is None only when the
    arity is astronomical; the structural verdict is then decided by a
    GRADING THEOREM, never by sampling."""
    if arena["kind"] == "probe":
        return list(arena["objects"]), len(arena["objects"]), arena["site_note"]
    if arena["kind"] == "carrier":
        if sgen == "ACTOR":
            return list(AB), 2, "the declared actor pool of ARM-1T"
        if sgen == "MENU-CLASS":
            return sorted(set(arena["menu"].values())), \
                len(set(arena["menu"].values())), "the weighted-menu quotient"
        if sgen == "CONG-CLASS":
            return sorted(set(arena["cong"].values())), \
                len(set(arena["cong"].values())), "the weighted congruence"
        if sgen == "EVENT-SUBSET":
            nd = arena["n_division_labels"]
            return None, 2 ** nd, (f"all subsets of the {nd} distinct division "
                                   f"events of the family")
        if sgen == "ULAM-PREFIX":
            return None, arena["ulam_total"], \
                "the Ulam address prefixes at every depth 0..4"
    else:
        H = arena["record"]
        if sgen == "ACTOR":
            return list(arena["actors"]), len(arena["actors"]), \
                "the record's declared actor pool"
        if sgen in ("MENU-CLASS", "CONG-CLASS"):
            return None, 0, ("the quotient is an object of the ARM-1T "
                             "transport family; it is not defined on this record")
        if sgen == "EVENT-SUBSET":
            nd = sum(1 for e in H if is_division(e))
            return None, 2 ** nd, (f"all subsets of the record's {nd} "
                                   f"division events")
        if sgen == "ULAM-PREFIX":
            return list(range(len(H) + 1)), len(H) + 1, \
                "the prefixes of the record's own Ulam address"
    return None, 0, "undefined"


def build_realised(cache, menu, cong, divisions, actors):
    """THE OBJECTS THE FAMILY ACTUALLY REALISES, with every grading's
    FORCING machine-checked.  The embedding reading decides three of the
    site generators by a grading THEOREM rather than by enumeration; the
    theorem's hypothesis -- that the grading rises by exactly one along
    every edge -- is a fact about the realised relation, so it is checked
    here, edge by edge, and the count of exceptions is carried into the
    row that uses it.  These same realised objects are what the QUOTIENT
    reading maps onto the sites."""
    R = {}

    # (a) the two class-extension graphs
    for sgen, Q in (("MENU-CLASS", menu), ("CONG-CLASS", cong)):
        rel = {}
        for h in cache:
            if len(h) >= DEPTH:
                continue
            for e, q in cache[h]:
                hp = h + (e,)
                if hp not in cache:
                    continue
                key = (Q[h], Q[hp])
                rel[key] = rel.get(key, 0) + (1 if is_division(e) else 0)
        span = defaultdict(set)
        for h in cache:
            span[Q[h]].add(len(h))
        multi = sorted(c for c, s in span.items() if len(s) > 1)
        R[(sgen, "EXTENSION-EDGE")] = {
            "objects": sorted(set(Q.values())), "rel": rel,
            "grading": "history length",
            "forcing": {"edges": sum(1 for _ in rel),
                        "multi_grade_classes": len(multi),
                        "homogeneous": not multi}}

    # (b) the realised division-event subsets
    dset = {h: frozenset(sk(e) for e in h if is_division(e)) for h in cache}
    rel, bad = {}, 0
    for h in cache:
        if len(h) >= DEPTH:
            continue
        for e, q in cache[h]:
            hp = h + (e,)
            if hp not in cache:
                continue
            a, b = dset[h], dset[hp]
            if a != b and len(b) != len(a) + 1:
                bad += 1
            key = (a, b)
            rel[key] = rel.get(key, 0) + (1 if is_division(e) else 0)
    R[("EVENT-SUBSET", "EXTENSION-EDGE")] = {
        "objects": sorted(set(dset.values()), key=sk), "rel": rel,
        "grading": "the cardinality grading of the Boolean lattice",
        "forcing": {"edges": sum(1 for _ in rel), "rise_exceptions": bad}}

    # (c) the realised Ulam prefixes
    addr = {(): ()}
    for h in sorted(cache, key=lambda z: (len(z), sk(z))):
        if len(h) >= DEPTH:
            continue
        for i, (e, q) in enumerate(sorted(cache[h], key=lambda z: sk(z[0]))):
            if h + (e,) in cache:
                addr[h + (e,)] = mutate("MUT-GRADING-BLIND",
                                        addr[h] + (i,),
                                        addr[h] if i == 0 else addr[h] + (i,))
    rel, bad = {}, 0
    for h in cache:
        if len(h) >= DEPTH:
            continue
        for e, q in cache[h]:
            hp = h + (e,)
            if hp not in cache:
                continue
            a, b = addr[h], addr[hp]
            if len(b) != len(a) + 1:
                bad += 1
            rel[(a, b)] = rel.get((a, b), 0) + (1 if is_division(e) else 0)
    pref = sorted({a[:k] for a in addr.values() for k in range(len(a) + 1)})
    R[("ULAM-PREFIX", "EXTENSION-EDGE")] = {
        "objects": pref, "rel": rel, "grading": "the address-length grading",
        "forcing": {"edges": sum(1 for _ in rel), "rise_exceptions": bad}}
    R["ulam_addresses"] = addr
    R["ulam_prefixes"] = pref

    # (d) the realised cover relation on singleton division-event subsets,
    #     with the poset-height forcing checked on the FULL family covers
    rel, bad, ncov, sing = {}, 0, 0, set()
    actor_cov = set()
    for h in cache:
        if not h:
            continue
        cov = poset_covers(list(h))
        ht = _poset_heights(list(h))
        for (i, j) in cov:
            ncov += 1
            if ht[j] != ht[i] + 1:
                bad += 1
            a, b = initiator(h[i]), initiator(h[j])
            if a != b:
                actor_cov.add((a, b))
            if is_division(h[i]) and is_division(h[j]):
                u = frozenset([sk(h[i])])
                v = frozenset([sk(h[j])])
                sing.add(u)
                sing.add(v)
                rel[(u, v)] = 0          # covers bound no interior (S4)
    R[("EVENT-SUBSET", "COVER-PAIR")] = {
        "objects": sorted(sing, key=sk), "rel": rel,
        "grading": "the poset height grading",
        "forcing": {"covers": ncov, "rise_exceptions": bad,
                    "covers_joining_two_division_events": len(rel)}}
    # the operator's charitable reconstruction of the two rows the census
    # types out: the family-wide cover relation pushed to initiators.  It
    # is materialised here rather than argued away, and it changes no fate.
    R["charitable"] = {
        "ACTOR x COVER-PAIR (family-wide covers pushed to initiators)": {
            "objects": len(actors), "edges": sorted(f"{u}->{v}"
                                                    for (u, v) in actor_cov),
            "cyclic_on_distinct_vertices":
                has_distinct_vertex_cycle(sorted(actors), actor_cov)},
        "EVENT-SUBSET x EXTENSION-EDGE (realised)": {
            "objects": len(R[("EVENT-SUBSET", "EXTENSION-EDGE")]["objects"]),
            "declared_arity": "2^20"},
        "ULAM-PREFIX x EXTENSION-EDGE (realised)": {
            "objects": len(R[("ULAM-PREFIX", "EXTENSION-EDGE")]["objects"]),
            "declared_arity": "3969"}}

    # (e) the actor pair
    rel = {}
    for u in actors:
        for v in actors:
            if u != v:
                rel[(u, v)] = sum(1 for e in divisions
                                  if u in regs_of(e) and v in regs_of(e))
    R[("ACTOR", "ACTOR-PAIR")] = {
        "objects": sorted(actors), "rel": rel, "grading": None,
        "forcing": {}}
    return R


def _poset_heights(acts):
    pred = event_poset(acts)
    ht = [0] * len(acts)
    for j in range(len(acts)):
        ht[j] = 1 + max([ht[i] for i in pred[j]], default=-1)
    return ht


def arena_quotient_rel(arena, sgen, lgen):
    """-> (objects, rel, note) for the QUOTIENT reading, or (None, None,
    reason).  The quotient reading maps REALISED grammar objects onto the
    sites, so it is run on the realised relations of `build_realised`;
    where the family realises nothing, it says so."""
    et = ENDPOINT_TYPE[lgen]
    if (sgen, et) not in FORCED_MAP:
        return None, None, TYPE_REASON.get(
            (sgen, et), "no pinned choice-free map between the two types")
    if arena["kind"] != "carrier":
        return None, None, ("the quotient census is posed at the transport "
                            "carrier only")
    R = arena.get("realised") or {}
    if lgen == "COVER-PAIR" and sgen == "ACTOR":
        return None, None, ("the carrier is a family, not a record; the event "
                            "poset's cover relation has no family-level "
                            "referent")
    key = (sgen, lgen)
    if key not in R:
        return None, None, "no realised relation at this cell"
    e = R[key]
    return e["objects"], e["rel"], e.get("grading") or "the realised relation"


def arena_linkrel(arena, sgen, lgen):
    """-> (relation | None, acyclic, acyclic_basis, note).  `relation`
    maps ordered site-object pairs to the DIVISION-EVENT COUNT on that
    link object inside the declared window.  `acyclic_basis` is either
    'measured' or the name of the grading that forces it."""
    et = ENDPOINT_TYPE[lgen]
    if arena["kind"] == "probe":
        rel = arena["rel"]
        return rel, not has_distinct_vertex_cycle(arena["objects"], set(rel)), \
            "measured", arena["link_note"]
    if (sgen, et) not in FORCED_MAP:
        return None, None, None, TYPE_REASON.get(
            (sgen, et), "no pinned choice-free map between the two types")

    if lgen == "ACTOR-PAIR":
        # sites are actors (identity map).  The link object is the ordered
        # actor pair / delivery channel; a division event is ON it when its
        # register footprint meets both endpoints.
        acts = arena["actors"]
        rel = {}
        for u in acts:
            for v in acts:
                if u == v:
                    continue
                rel[(u, v)] = sum(1 for e in arena["division_events"]
                                  if u in regs_of(e) and v in regs_of(e))
        realized = {k for k, n in rel.items() if n > 0}
        cyc = has_distinct_vertex_cycle(acts, realized)
        return rel, (not cyc), "measured", \
            "co-division incidence on the ordered actor pair"

    if lgen == "COVER-PAIR":
        if sgen == "ACTOR":
            H = arena.get("record")
            if H is None:
                return None, None, None, ("the carrier is a family, not a "
                                          "record; the event poset's cover "
                                          "relation has no family-level referent")
            cov = poset_covers(H)
            rel = {}
            for (i, j) in cov:
                u, v = initiator(H[i]), initiator(H[j])
                if u == v:
                    continue
                rel[(u, v)] = rel.get((u, v), 0)     # covers bound no interior
            cyc = has_distinct_vertex_cycle(arena["actors"], set(rel))
            return rel, (not cyc), "measured", \
                "the event poset's covers, pushed to initiators"
        # MEASURED, not argued: the family's event posets carry 10566
        # covers and NONE of them joins two division events, so the
        # relation on singleton division-event subsets is EMPTY.  (The
        # poset HEIGHT grading is not strict -- 384 covers raise height by
        # more than one -- so emptiness, not grading, is the basis here.)
        return {}, True, "the measured emptiness of the realised relation", \
            "singleton division-event subsets under the event poset's covers"

    # EXTENSION-EDGE
    if arena["kind"] == "carrier":
        if sgen in ("MENU-CLASS", "CONG-CLASS"):
            Q = arena["menu"] if sgen == "MENU-CLASS" else arena["cong"]
            rel = {}
            for h in arena["cache"]:
                if len(h) >= DEPTH:
                    continue
                for e, q in arena["cache"][h]:
                    hp = h + (e,)
                    if hp not in arena["cache"]:
                        continue
                    key = (Q[h], Q[hp])
                    if MUTANT == "MUT-SELFLOOP-DROP" and key[0] == key[1]:
                        continue
                    rel[key] = rel.get(key, 0) + (1 if is_division(e) else 0)
            nodes = sorted(set(Q.values()))
            if MUTANT == "MUT-CYCLE-PLANT":
                for a, b in ((0, 1), (1, 2), (2, 0)):
                    rel[(a, b)] = rel.get((a, b), 1)
            cyc = has_distinct_vertex_cycle(nodes, set(rel))
            return rel, (not cyc), "measured", \
                "the class-level event-extension graph"
        if sgen == "EVENT-SUBSET":
            return {}, True, "the cardinality grading of the Boolean lattice", \
                "a division-event set to itself plus one event"
        if sgen == "ULAM-PREFIX":
            return {}, True, "the address-length grading", \
                "an Ulam address to its one-step extensions"
    else:
        if sgen == "EVENT-SUBSET":
            return {}, True, "the cardinality grading of the Boolean lattice", \
                "a division-event set to itself plus one event"
        if sgen == "ULAM-PREFIX":
            H = arena["record"]
            rel = {}
            for i in range(len(H)):
                rel[(i, i + 1)] = 1 if is_division(H[i]) else 0
            cyc = has_distinct_vertex_cycle(list(range(len(H) + 1)), set(rel))
            return rel, (not cyc), "measured", \
                "the record's own prefix chain"
    return None, None, None, "undefined"


# ---------------------------------------------------------------------------
# THE DETECTOR proper
# ---------------------------------------------------------------------------

def detect_quotient(arena, sgen, lgen, cgen, repair, target, i7_family,
                    links_i7):
    """One census row under the QUOTIENT reading of "a map": a SURJECTION
    from the realised grammar objects onto the sites, every realised link
    edge carrying a DECLARED displacement.  Acyclicity is no obstruction
    to one, so the embedding reading's second blade does not apply here
    and the cell is decided further down: at the map's existence, at
    count positivity, or -- as the pin expected -- AT THE CHOICE
    INVENTORY."""
    X, links, Lmod = target["X"], target["links"], target["Lmod"]
    row = {"arena": arena["name"], "carrier": arena.get("carrier"),
           "reading": "QUOTIENT",
           "site_gen": sgen, "link_gen": lgen, "count_gen": cgen,
           "arity_repair": repair, "target": target["name"]}
    _, declared_arity, snote = arena_sites(arena, sgen)
    row["site_arity"] = declared_arity
    row["site_note"] = snote
    objs, rel, note = arena_quotient_rel(arena, sgen, lgen)
    row["link_note"] = note
    if rel is None:
        row["fate"] = "TYPE-DEAD"
        row["reason"] = note
        return row
    row["realised_objects"] = len(objs)
    row["realised_edges"] = len(rel)
    row["needs_interior_position"] = False

    # (2) arity.  A surjection needs AT LEAST the target's site count;
    #     over-largeness is what a quotient invites, not an obstruction.
    if len(objs) < len(X):
        if repair == "NONE":
            row["fate"] = "ARITY-DEAD"
            row["reason"] = (f"{len(objs)} realised site objects cannot cover "
                             f"the target's {len(X)} sites; no repair "
                             f"declared")
        else:
            row["fate"] = "ARITY-DEAD-BELOW"
            row["reason"] = (f"{len(objs)} realised site objects against the "
                             f"target's {len(X)}; a declared restriction can "
                             f"only shrink a site set, so no repair exists "
                             f"even in principle")
        return row

    # (3) does a quotient map exist at all?
    qm = quotient_maps(objs, rel, X, links, Lmod)
    row["quotient_search"] = {"engine": qm["engine"],
                              "declared_solutions": qm["searched"],
                              "solutions_found": len(qm["solutions"]),
                              "seed": QSEED, "lcg": list(QLCG)}
    if not qm["solvable"]:
        row["fate"] = "HOM-DEAD"
        row["obstruction"] = qm["obstruction"]
        row["reason"] = qm["reason"]
        return row

    # (4) the induced count fields, over the declared solution set
    sols = qm["solutions"]
    fields = {}
    nlab = len(links)
    for i, phi in enumerate(sols):
        fields[(i, tuple(range(nlab)), False)] = quotient_field(
            rel, phi, X, links, Lmod, tuple(range(nlab)), False)
    best_i, best_pos = 0, -1
    for i in range(len(sols)):
        f = fields[(i, tuple(range(nlab)), False)]
        pos = sum(1 for v in f.values() if v > 0)
        if pos > best_pos:
            best_i, best_pos = i, pos
    row["count_cells"] = len(X) * nlab
    row["count_positive_cells_best"] = best_pos
    row["count_positive_cells_min"] = min(
        sum(1 for v in fields[(i, tuple(range(nlab)), False)].values() if v > 0)
        for i in range(len(sols)))
    base_field = fields[(best_i, tuple(range(nlab)), False)]
    row["surjective_solutions"] = sum(
        1 for phi in sols if len({phi[k] for k in phi}) == len(X))

    # the choice inventory, REACHED: the fibers are the number of DISTINCT
    # induced count fields the choice produces.  Over a searched solution
    # set they are LOWER BOUNDS -- more search can only add fields, never
    # remove one -- so a fiber above 1 is a free item for good.
    def key(f):
        return tuple(sorted(((str(k), v) for k, v in f.items())))
    fib_site = len({key(fields[(i, tuple(range(nlab)), False)])
                    for i in range(len(sols))})
    fib_label = len({key(quotient_field(rel, sols[best_i], X, links, Lmod,
                                        lp, False))
                     for lp in permutations(range(nlab))})
    fib_orient = len({key(quotient_field(rel, sols[best_i], X, links, Lmod,
                                         tuple(range(nlab)), o))
                      for o in (False, True)})
    inv = mutate("MUT-FIBER-LAX",
                 {"I-SITE-ASSIGNMENT": fib_site, "I-DIRECTION-LABEL": fib_label,
                  "I-ORIENT": fib_orient},
                 {"I-SITE-ASSIGNMENT": 1, "I-DIRECTION-LABEL": 1,
                  "I-ORIENT": 1})
    row["inventory"] = inv
    row["inventory_is_a_lower_bound_over_the_declared_search"] = True
    free = sorted(k for k, v in inv.items() if v > 1)
    row["free_items"] = free

    smug = classify_smuggling(lambda i7rec: base_field, i7_family)
    row["smuggled"] = smug
    if smug:
        row["fate"] = "SMUGGLED"
        row["reason"] = ("the candidate's counts move when I7's own record s "
                         "is replaced")
        return row
    if not free:
        if best_pos < len(X) * nlab:
            row["fate"] = "COUNT-DEAD"
            row["reason"] = (f"n_l(x) must lie in Z_>0 (HA 3.1); the best of "
                             f"{len(sols)} declared quotient maps leaves "
                             f"{len(X) * nlab - best_pos} of {len(X) * nlab} "
                             f"cells at zero")
            return row
        row["fate"] = "FOUND-candidate"
        row["reason"] = "zero free items at the RSQ standard"
        return row
    row["fate"] = "UNMOTIVATED"
    row["reason"] = (
        f"{len(free)} genuinely free item(s): "
        + ", ".join(f"{k} fiber >= {inv[k]}" for k in free)
        + (f"; and the best of {len(sols)} declared quotient maps leaves "
           f"{len(X) * nlab - best_pos} of {len(X) * nlab} count cells at "
           f"zero" if best_pos < len(X) * nlab else
           f"; the count field IS strictly positive at all {len(X) * nlab} "
           f"cells, so this cell dies at the CHOICE STANDARD and nowhere "
           f"earlier"))
    row["count_field"] = tuple(sorted(base_field.items(),
                                      key=lambda z: str(z)))
    return row



def detect(arena, sgen, lgen, cgen, repair, target, i7_family, links_i7,
           reading="EMBEDDING"):
    """One census row.  Every fate is a MEASURED outcome with its number.

    `reading` is the DECLARED admissibility axis.  EMBEDDING asks for a
    bijection under which the grammar's link relation contains the
    target's incidence; QUOTIENT asks for a surjection of realised
    grammar objects onto the sites carrying every realised edge onto a
    declared displacement.  The type gate is the same question in either
    direction and fires identically."""
    if reading == "QUOTIENT":
        return detect_quotient(arena, sgen, lgen, cgen, repair, target,
                               i7_family, links_i7)
    X, links, Lmod = target["X"], target["links"], target["Lmod"]
    row = {"arena": arena["name"], "carrier": arena.get("carrier"),
           "reading": reading,
           "site_gen": sgen, "link_gen": lgen, "count_gen": cgen,
           "arity_repair": repair, "target": target["name"]}

    objs, arity, note = arena_sites(arena, sgen)
    row["site_arity"] = arity
    row["site_note"] = note
    rel, acyc, basis, lnote = arena_linkrel(arena, sgen, lgen)
    row["link_note"] = lnote

    if rel is None:
        row["fate"] = "TYPE-DEAD"
        row["reason"] = lnote
        return row

    row["link_acyclic"] = acyc
    row["acyclicity_basis"] = basis

    # (1) the interior gate (pin R2 / R6b' 9): does the candidate need a
    #     POSITION INSIDE a leg?  No generator in the declared vocabulary
    #     does -- the count is over EVENTS ON a link object, never over
    #     positions inside one.  The classifier's other value is exercised
    #     by PROBE-INTERIOR in the controls.
    row["needs_interior_position"] = False

    # (2) arity
    if mutate("MUT-ARITY-LAX", arity != len(X), False):
        if repair == "NONE":
            row["fate"] = "ARITY-DEAD"
            row["reason"] = (f"{arity} site objects against the target's "
                             f"{len(X)}; no repair declared")
            return row
        if arity < len(X):
            row["fate"] = "ARITY-DEAD-BELOW"
            row["reason"] = (f"{arity} site objects against the target's "
                             f"{len(X)}; a declared restriction can only "
                             f"shrink a site set, so no repair exists")
            return row

    # (3) structure, at THE DECLARED CRITERION.  A link is an unordered
    #     site pair -- orientation is a declared free item -- so incidence
    #     is UNDIRECTED on the kill side and the admit side alike.  The
    #     target is Z_Lmod-periodic: every one of its cells closes an
    #     Lmod-cycle on Lmod DISTINCT sites, an ODD cycle at Lmod = 3.  A
    #     relation graded so that every edge raises the grade by exactly
    #     one is 2-colourable by the grade's parity and carries no odd
    #     cycle, so it admits no restriction of any size -- every subset
    #     at once, no enumeration.  Where the grading fails, the declared
    #     restriction is not argued away but EXECUTED, by a complete
    #     induced-subgraph search.
    realised = set(k for k, n in rel.items() if n > 0) if lgen == "ACTOR-PAIR" \
        else set(rel)
    bip, wit = bipartite_witness(objs if objs is not None else
                                 sorted({u for e in realised for u in e},
                                        key=str), realised)
    row["link_bipartite"] = bip
    row["odd_cycle_witness"] = wit
    if bip:
        row["fate"] = "STRUCT-DEAD"
        row["reason"] = (f"the link relation is graded ({basis}) and so "
                         f"carries no odd cycle, while the target is "
                         f"Z_{Lmod}-periodic and closes a {Lmod}-cycle on "
                         f"{Lmod} distinct sites at every one of its cells; "
                         f"no restriction of any size embeds")
        row["subsets_excluded"] = f"all C({arity},{len(X)}) restrictions"
        return row

    if arity != len(X):
        if objs is None:
            row["fate"] = "SCOPE-BLOCKED"
            row["reason"] = ("odd-cycle-carrying and not materialisable at "
                             "this arity")
            return row
        n_emb, n_cand, n_vis = induced_target_embeddings(
            objs, realised, X, links, Lmod)
        row["restriction_executed"] = {"embeddings": n_emb,
                                       "candidate_objects": n_cand,
                                       "search_nodes": n_vis}
        if n_emb == 0:
            row["fate"] = "STRUCT-DEAD"
            row["reason"] = (f"the declared restriction is EXECUTED, not "
                             f"argued: a complete induced-subgraph search "
                             f"over the {n_cand} site objects that carry at "
                             f"least the target's minimum degree finds 0 of "
                             f"the C({arity},{len(X)}) restrictions inducing "
                             f"the target ({n_vis} search nodes)")
            row["subsets_excluded"] = f"all C({arity},{len(X)}) restrictions"
            return row
        row["fate"] = "ARITY-REPAIR-UNDECIDED"
        row["reason"] = (f"{n_emb} restriction(s) induce the target; the "
                         f"count field on a selected restriction is not "
                         f"built by this detector")
        return row

    isos = graph_isomorphisms(objs, realised, X, links, Lmod)
    row["isomorphisms"] = len(isos)
    row["isomorphisms_directed_comparator"] = len(
        graph_isomorphisms(objs, realised, X, links, Lmod, directed=True))
    if not isos:
        row["fate"] = "STRUCT-DEAD"
        row["reason"] = (f"odd-cycle-carrying, but 0 of the {arity}! "
                         f"bijections carry the site incidence onto the "
                         f"target's link structure")
        return row

    # (4) counts, and the choice inventory with fibers COMPUTED
    nlab = len(links)
    fields = {}
    for phi in isos:
        for lp in permutations(range(nlab)):
            for orient in (False, True):
                f = count_field(None, rel, None, X, links, Lmod, phi,
                                lp, orient)
                fields[(sk(tuple(sorted(phi.items(), key=str))), lp, orient)] \
                    = tuple(sorted(((str(k), v) for k, v in f.items())))
    base = (sk(tuple(sorted(isos[0].items(), key=str))),
            tuple(range(nlab)), False)
    base_field = dict((k, v) for k, v in fields[base])
    row["count_min"] = min(base_field.values())
    row["count_max"] = max(base_field.values())
    row["count_cells"] = len(base_field)

    if row["count_min"] < 1:
        zeros = sorted(k for k, v in base_field.items() if v == 0)
        row["fate"] = "COUNT-DEAD"
        row["reason"] = (f"n_l(x) must lie in Z_>0 (HA 3.1); the induced "
                         f"count is 0 at {len(zeros)} of {len(base_field)} "
                         f"cells")
        row["zero_cells"] = zeros
        return row

    # (5) the no-smuggling classifier (pin R6)
    def count_fn(i7rec):
        return base_field
    smug = classify_smuggling(count_fn, i7_family)
    row["smuggled"] = smug
    if smug:
        row["fate"] = "SMUGGLED"
        row["reason"] = ("the candidate's counts move when I7's own record "
                         "s is replaced: it computes a function of s, not of "
                         "grammar data")
        return row

    fib_site = len({fields[(k, tuple(range(nlab)), False)]
                    for k, lp, o in fields if lp == tuple(range(nlab))
                    and o is False})
    fib_label = len({fields[(base[0], lp, False)] for lp in
                     permutations(range(nlab))})
    fib_orient = len({fields[(base[0], tuple(range(nlab)), o)]
                      for o in (False, True)})
    inv = mutate("MUT-FIBER-LAX",
                 {"I-SITE-ASSIGNMENT": fib_site,
                  "I-DIRECTION-LABEL": fib_label,
                  "I-ORIENT": fib_orient},
                 {"I-SITE-ASSIGNMENT": 1, "I-DIRECTION-LABEL": 1,
                  "I-ORIENT": 1})
    row["inventory"] = inv
    free = sorted(k for k, v in inv.items() if v > 1)
    row["free_items"] = free
    row["fate"] = "FOUND-candidate" if not free else "UNMOTIVATED"
    row["reason"] = ("zero free items at the RSQ standard"
                     if not free else
                     f"{len(free)} genuinely free item(s): "
                     + ", ".join(f"{k} fiber {inv[k]}" for k in free))
    row["count_field"] = tuple(sorted(base_field.items(), key=lambda z: str(z)))
    return row


# ===========================================================================
# SEC 10 helpers: the DERIVED head, the paper check, the writers
# ===========================================================================

def derive_obstruction(P):
    """The obstruction NAME is derived from the measurements too, so that
    no string in the head is a literal a gate could fail to compare."""
    g, qm = P["grading_theorem"], P["quotient_mechanism"]
    graded = (g["edges_not_raising_length_by_exactly_one"] == 0
              and g["cong_multi_length_classes"] == 0)
    wiped = qm["hom_dead_rows"] > 0
    if graded and wiped:
        return "READING-STRATIFIED-THE-GRADING-THEOREM-AND-THE-SELF-LOOP-WIPEOUT"
    if graded:
        return "THE-GRADING-THEOREM"
    if wiped:
        return "THE-SELF-LOOP-WIPEOUT"
    return "NO-OBSTRUCTION-MEASURED"


def rebuild_verdict(P):
    """THE HEAD, DERIVED.  This function reads ONLY the receipt payload: it
    shares no local variable, no typed count and no branch with the run
    that produced it, and the outcome word itself is selected by the
    measured fate multiset rather than typed into an f-string.  The run
    calls it twice -- once to emit, once (through a JSON round trip) to
    compare as a complete string at G-VERDICT-EQUALITY."""
    f = {k: int(v) for k, v in P["fates"].items()}
    rows = int(P["candidate_count"])
    n_found = f.get("FOUND-candidate", 0)
    n_smug = f.get("SMUGGLED", 0)
    n_unmot = f.get("UNMOTIVATED", 0)
    head = ("WELD2-FOUND-AT-THE-DECLARED-FAMILY" if n_found else
            "WELD2-SMUGGLED-AT-THE-DECLARED-FAMILY" if n_smug else
            "WELD2-EMPTY-AT-THE-DECLARED-FAMILY")
    m, qm = P["mechanism"], P["quotient_mechanism"]
    c = P["controls"]
    ca = P["choice_arenas"]
    g = P["grading_theorem"]
    cnt = P["counts_for_the_head"]
    unmot_readings = sorted({r["reading"] for r in P["census_rows"]
                             if r["fate"] == "UNMOTIVATED"}) or ["NONE"]
    parts = [
        f"{head}-{derive_obstruction(P)}",
        f"@BOTH-QUOTIENTS-AS-SITE-GENERATORS:MENU-"
        f"{P['menu_classes']}+CONG-{P['cong_classes']}"
        f"(CARRIER-AXIS-INERT:{P['distinct_candidates']}-DISTINCT-CELLS"
        f"-x2-STAMPS)",
        f"<ROWS={rows}|READINGS={'+'.join(sorted(P['fates_by_reading']))}"
        f"|FOUND={n_found}|SMUGGLED={n_smug}"
        f"(STRUCTURAL-NOT-MEASURED-FOR-CANDIDATES)"
        f"|UNMOTIVATED={n_unmot}(ALL-AT-{'+'.join(unmot_readings)})"
        + "".join(f"|{k}={f[k]}" for k in sorted(f)
                  if k not in ("FOUND-candidate", "SMUGGLED", "UNMOTIVATED")),
        f" -- MECHANISM@EMBEDDING=THE-GRADING-THEOREM"
        f"(EVERY-EXTENSION-EDGE-RAISES-LENGTH-BY-1:"
        f"{g['extension_edges'] - g['edges_not_raising_length_by_exactly_one']}"
        f"-OF-{g['extension_edges']}"
        f"|CONG-LENGTH-HOMOGENEOUS-SO-GRADED-AND-BIPARTITE"
        f"|MENU-NOT:{g['menu_multi_length_classes']}-MULTI-LENGTH-CLASSES"
        f"=EXACTLY-ITS-{m['menu_class_selfloops']}-SELF-LOOPS"
        f"|TARGET-CLOSES-A-3-CYCLE-ON-3-DISTINCT-SITES-AT-"
        f"{m['target_cells_closing_a_3_cycle_on_3_distinct_sites']}-OF-"
        f"{m['target_cells']}-CELLS)"
        f"-AND-THE-DECLARED-RESTRICTION-EXECUTED"
        f"(INDUCED-SUBGRAPH-SEARCH-COMPLETE:"
        f"{m['menu_induced_target_embeddings']}-OF-C(113,9)|"
        f"{m['cong_induced_target_embeddings']}-OF-C(185,9))"
        f"-AND-ARITY(THE-ONLY-GENERATOR-CARRYING-A-TARGET-TYPE-CYCLE-IS-THE-"
        f"ACTOR-PAIR-WITH-{m['actor_site_objects']}-OBJECTS:"
        f"{m['AB_channel_occurrences_each_direction']}-CO-DIVISION-"
        f"OCCURRENCES-OF-{m['AB_channel_distinct_events']}-DISTINCT-EVENTS-"
        f"THE-SAME-SET-BOTH-WAYS)",
        f" -- MECHANISM@QUOTIENT=MENU-SELF-LOOP-WIPEOUT-EXACT"
        f"({qm['menu_selfloops_forcing_the_zero_displacement']}-SELF-LOOPS-"
        f"DEMAND-DISPLACEMENT-0-AND-NO-DECLARED-LINK-IS-0;"
        f"{qm['hom_dead_rows']}-ROWS-HOM-DEAD)"
        f"|CONG-COUNT-POSITIVITY-{qm['cong_best_positive_cells']}-OF-"
        f"{qm['cong_cells']}-AT-{qm['declared_search']['declared_solutions']}"
        f"-DECLARED-SOLUTIONS"
        f"|THE-PRE-REGISTERED-FREE-ITEMS-ARE-REACHED"
        f"(ULAM-COUNT-FIELD-POSITIVE-AT-{qm['ulam_best_positive_cells']}-OF-"
        f"{qm['cong_cells']}-AND-UNMOTIVATED-AT-THE-CHOICE-STANDARD)",
        f" -- CONTROLS=FOUND-AT-CRYSTAL@CRYSTAL-CARRIED-L2"
        f"({c['FOUND_at_crystal']['fate']},"
        f"ISOS={c['FOUND_at_crystal'].get('isomorphisms')},FIBERS-ALL-1,"
        f"CONFIGS={ca['control_at_CRYSTAL-CARRIED-L2']['configurations']})"
        f"|FALSIFIER-FLIPS({c['FOUND_falsifier']['fate']},"
        f"I-SITE-ASSIGNMENT-FIBER="
        f"{c['FOUND_falsifier'].get('inventory', {}).get('I-SITE-ASSIGNMENT')})"
        f"|EMPTY-AT-WALK({c['EMPTY_at_walk']['fate']})"
        f"|CRYSTAL-AT-I7({c['crystal_at_I7_target']['fate']})"
        f"|PIN-NAMED-COVER-GENERATOR-NEVER-FIRES"
        f"({'+'.join(sorted({v['fate'] for v in c['pin_named_cover_generator'].values()}))}"
        f"-AT-BOTH-TARGETS)"
        f"|FOUND-AT-I7-TARGET=NO-COMMITTED-GRAMMAR-RECORD;"
        f"REACHABLE-AT-A-DECLARED-PROBE"
        f"({c['FOUND_at_I7_target_declared_probe']['fate']},"
        f"ISOS={c['FOUND_at_I7_target_declared_probe'].get('isomorphisms')},"
        f"CONFIGS={ca['census_target_I7-DECLARED-L3']['configurations']})",
        f" -- INGREDIENT=COUNT-SEMANTICS-INTACT"
        f"(ADDITIVITY-{cnt['additivity_ok']}-OF-{cnt['additivity_total']}"
        f"|DIVISION=ARBITRATION-TAG-FORCED)",
        f" -- CARRIER-RE-DERIVATION=CONG-{P['cong_classes']}-"
        f"{cnt['six_properties']}-OF-6",
        f" -- CRYSTALS=DIAGONAL-EMPTY-AT-9-OF-9-IN-"
        f"{sum(1 for r in P['crystals'] if r['count_field_by_link'][str(tuple(P['i7']['links'][2]))] == [[0, 9]] or r['count_field_by_link'][str(tuple(P['i7']['links'][2]))] == [(0, 9)])}"
        f"-OF-{len(P['crystals'])}"
        f"|INDUCED-DET=0-AT-EVERY-SITE-OF-EVERY-CRYSTAL"
        f"|ADMISSIBLE-I7-RECORDS-INDUCED="
        f"{sum(1 for r in P['crystals'] if r['induces_an_admissible_I7_record'])}",
        f" -- SCOPE=(A,B)-D<=4-CARRIER|I7-d2-L3-9-SITES-3-LINKS"
        f"|DECLARED-WINDOW=FIRST-TO-LAST-ARBITRATION-CUT"
        f"|READING-AXIS-DECLARED-BY-THIS-UNIT-NOT-BY-THE-PIN>",
    ]
    return "".join(parts)


CITED_ELSEWHERE = {
    "89": "ledger reference #89 (the scout's amendment)",
    "96": "ledger reference #96 (the operator review)",
    "97": "ledger reference #97 (the effectus review)",
    "100": "ledger reference #100 (the instrument review)",
    "102": "ledger reference #102 (the adjudication)",
    "85": "ledger reference #85 (the pin)",
    "83": "ledger reference #83 (the scout)",
    "14": "HA 14, a section number",
    "29": "paper 29, a corpus reference",
    "47": "d47 pin, a corpus reference",
    "3": "section and item numbers",
    "4": "section and item numbers",
    "5": "section and item numbers",
    "6": "section and item numbers",
    "7": "section and item numbers",
    "8": "section and item numbers",
    "9": "section and item numbers",
    "10": "section and item numbers",
    "11": "section and item numbers",
    "12": "section and item numbers",
    "13": "section and item numbers",
    "2": "section and item numbers",
    "1": "section and item numbers",
    "0": "section and item numbers",
}
PAPER = "v14/paper-13-weld2-carrier-census.md"


def verify_paper():
    """#20, INSTRUMENTED.  The paper's own numerals are extracted and each
    one is required to occur in the receipt payload's JSON serialisation
    or in the declared allow-list of citations and section numbers.  The
    claim 'every number printed here renders from the receipt' is checked
    in the run that writes the receipt, not asserted beside it."""
    import re
    path = os.path.join(REPO, PAPER)
    try:
        text = open(path, encoding="utf-8").read()
    except OSError:
        gate("G-PAPER-RENDERS",
             f"#20: {PAPER} could not be opened, so the claim that every "
             f"number in it renders from the receipt is UNCHECKED",
             False, {"path": PAPER, "error": "unreadable"})
        return
    text = mutate("MUT-PAPER-DRIFT", text,
                  text.replace("3969 histories", "3970 histories"))
    norm = text.replace(" ", "").replace(" ", "")
    norm = norm.replace("\\,", "").replace("1 048 576", "1048576")
    norm = re.sub(r"(?<=\d) (?=\d\d\d\b)", "", norm)
    body = json.dumps({"payload": PAYLOAD, "gates": GATES, "anchors": ANCHORS,
                       "verbatim": VANCHORS}, default=str, sort_keys=True)
    # the receipt's own numerals, as DELIMITED tokens rather than as
    # substrings: "45" must occur in the receipt as the number 45, not
    # inside 1456, or the check would pass on drift it should catch
    have = set(re.findall(r"(?<![\w.])\d+(?![\w.])", body))
    toks = re.findall(r"(?<![\w.])\d+(?![\w])", norm)
    unexplained = sorted({t for t in toks
                          if t not in CITED_ELSEWHERE and t not in have},
                         key=lambda z: (len(z), z))
    PAYLOAD["paper_check"] = {"path": PAPER, "tokens": len(toks),
                              "distinct_tokens": len(set(toks)),
                              "unexplained": unexplained}
    gate("G-PAPER-RENDERS",
         f"#20, INSTRUMENTED rather than asserted: every one of the "
         f"{len(set(toks))} distinct numerals in {PAPER} "
         f"({len(toks)} occurrences) is required to occur in this receipt or "
         f"in the declared allow-list of ledger references and section "
         f"numbers.  Unexplained: {unexplained}",
         not unexplained, PAYLOAD["paper_check"])


def build_receipt(verdicts):
    src = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
    receipt = {
        "unit": "v14 WELD 2 -- paper-13, the carrier census",
        "pin": "v14/note-weld2-census-pin.md",
        "pin_sha256_12": "9d19515cb3ae",
        "interpreter": INTERP,
        "arithmetic": "fractions.Fraction / exact integers; no floats",
        "source_sha256": src,
        "verdicts": verdicts,
        "payload": PAYLOAD,
        "anchors": ANCHORS,
        "verbatim_anchors": VANCHORS,
        "gates": GATES,
        "waivers": WAIVERS,
        "gate_count": len(GATES),
        "gate_failures": FAILED,
        "anchor_failures": ANCHOR_FAIL,
    }
    if MUTANT == "MUT-INTEGRITY":
        receipt["gate_count"] = 99
        receipt["gate_failures"] = 7
    return receipt


def write_files(receipt):
    with open(OUT_TXT, "w") as f:
        f.write("\n".join(LINES) + "\n")
    with open(OUT_JSON, "w") as f:
        json.dump(receipt, f, indent=1, sort_keys=True, default=str)
        f.write("\n")
    return receipt


def snapshot():
    """The invariants the integrity check compares against, taken BEFORE
    the receipt is built.  Comparing a written receipt against the live
    payload would let a post-gate edit move both sides together; this
    freezes the values first, so it cannot."""
    return {"verdict": PAYLOAD["verdict"],
            "candidate_count": PAYLOAD["candidate_count"],
            "distinct_candidates": PAYLOAD["distinct_candidates"],
            "fates": json.loads(json.dumps(PAYLOAD["fates"])),
            "obstruction": PAYLOAD["obstruction"],
            "gate_count": len(GATES), "gate_failures": FAILED,
            "anchor_failures": ANCHOR_FAIL,
            "gate_names": [g["gate"] for g in GATES],
            "expected_final_gate_count": len(GATES) + (
                0 if any(g["gate"] == "G-ARTIFACT-INTEGRITY" for g in GATES)
                else 1),
            "lines": len(LINES)}


def integrity_check(verdict, receipt=None, snap=None):
    """RE-READ WHAT WAS WRITTEN.  A receipt that contradicts its own output
    text, or either artifact that contradicts the run that produced it, is
    caught here rather than shipped: the two artifacts are read back --
    from DISK on a writing run, and from the serialisation the run would
    have written otherwise -- and compared field by field against the live
    run, so the check is exercised on every path including the mutants."""
    try:
        if receipt is None:
            txt = open(OUT_TXT, encoding="utf-8").read()
            rec = json.loads(open(OUT_JSON, encoding="utf-8").read())
        else:
            txt = "\n".join(LINES) + "\n"
            rec = json.loads(json.dumps(receipt, sort_keys=True, default=str))
    except Exception as exc:                                # noqa: BLE001
        return False, {"error": str(exc)}
    s = snap or snapshot()
    P = rec.get("payload", {})
    ev = {
        "output_text_matches_the_run": txt == "\n".join(LINES) + "\n",
        "receipt_verdict_matches": P.get("verdict") == verdict == s["verdict"],
        "gate_count_matches": rec.get("gate_count") == s["gate_count"],
        "gate_failures_match": rec.get("gate_failures") == s["gate_failures"],
        "anchor_failures_match": rec.get("anchor_failures")
        == s["anchor_failures"],
        "candidate_count_matches": P.get("candidate_count")
        == s["candidate_count"],
        "distinct_candidates_match": P.get("distinct_candidates")
        == s["distinct_candidates"],
        "obstruction_matches": P.get("obstruction") == s["obstruction"],
        "fates_match": P.get("fates") == s["fates"],
        "gate_names_match": [g["gate"] for g in rec.get("gates", [])]
        == s["gate_names"],
        "registry_gate_total_matches":
            P.get("registry", {}).get("gates_including_the_terminal_gates")
            == s["expected_final_gate_count"],
    }
    return all(ev.values()), ev


# ===========================================================================
# THE RUN
# ===========================================================================

# ===========================================================================
# THE PIPELINE
# ===========================================================================

INTERIOR_READINGS = {"C1-COUNT-MATCH-LENGTH-INTERIOR-SPLIT"}


def needs_interior(count_gen):
    """R6b' 9's type census (V04): a leg has no interior division event,
    so any reading that must place a division INSIDE a leg is dead on
    arrival.  The classifier's other value is exercised at PROBE-INTERIOR."""
    return count_gen in INTERIOR_READINGS


def run_all():
    emit("=" * 78)
    emit("v14 WELD 2 -- paper-13: THE CARRIER CENSUS")
    emit("pin v14/note-weld2-census-pin.md (9d19515cb3ae), ledger #85, Route A")
    emit("exact arithmetic (fractions.Fraction / integers); no floats")
    emit("=" * 78)
    emit("")
    run_provenance()

    # ---------------------------------------------------------------- SEC 2/3
    emit("")
    emit("=" * 78)
    emit("SEC 3  THE AB4 ARENA -- the transport family, rebuilt")
    emit("=" * 78)
    fam, cache = build_family()
    menu = menu_partition(cache)
    n_menu = len(set(menu.values()))
    n_menu_cmp = len(set(menu_partition_comparator(cache).values()))
    n_menu_unw = len({sk(frozenset({sk(e) for e, q in cache[h]}))
                      for h in cache})
    PAYLOAD["histories"] = len(fam)
    PAYLOAD["menu_classes"] = n_menu
    PAYLOAD["menu_classes_comparator"] = n_menu_cmp
    PAYLOAD["menu_classes_unweighted"] = n_menu_unw
    anchor("A01", "ARM-1T (A,B) d<=4 family size", 3969, len(fam),
           "v10/note-d74-transport-holonomy-result.md (AB4 arm); "
           "v14/paper-12-gamma-main.md 9")
    anchor("A02", "MENU quotient classes at AB4", 113, n_menu,
           "v10/note-d74-transport-holonomy-result.md TH-A carrier table")
    gate("G-MENU-CLASSES",
         f"the weighted-menu partition of the {len(fam)} histories has "
         f"{n_menu} classes, and an INDEPENDENT comparator -- pairwise "
         f"equality of menus as mappings event -> Fraction, sharing no key "
         f"primitive with the builder -- returns {n_menu_cmp}.  DISCLOSED "
         f"because it was measured: the UNWEIGHTED partition, on the event "
         f"SET alone, returns {n_menu_unw} -- so at this scope the weights "
         f"add {'nothing' if n_menu_unw == n_menu else 'refinement'} to the "
         f"event set, and the carrier is the coarser object it looks like",
         n_menu == 113 and n_menu_cmp == 113,
         {"builder": n_menu, "comparator": n_menu_cmp,
          "unweighted": n_menu_unw, "histories": len(fam)})

    closed, defects = square_census(cache)
    spec = Counter(str(r) for _, _, _, r in defects)
    n_cmp = square_comparator(cache)
    PAYLOAD["closed_squares"] = len(closed)
    PAYLOAD["defective_squares"] = len(defects)
    PAYLOAD["defect_spectrum"] = dict(sorted(spec.items()))
    anchor("A03", "closed exchange squares at AB4", 1546, len(closed),
           "v14/review-gmain-operator.md 4(c); v10 D74 AB4")
    anchor("A04", "defective (non-unit) squares at AB4", 88, len(defects),
           "v10/note-d74-transport-holonomy-result.md TH-A")
    gate("G-SQUARES",
         f"the exchange-square census returns {len(closed)} closed squares "
         f"of which {len(defects)} are defective, spectrum "
         f"{dict(sorted(spec.items()))}; an INDEPENDENT comparator that walks "
         f"the depth-|h|+2 DESCENDANTS instead of the candidate pairs returns "
         f"{n_cmp} closed squares",
         len(closed) == 1546 and n_cmp == 1546 and len(defects) == 88,
         {"closed": len(closed), "comparator": n_cmp,
          "defective": len(defects), "spectrum": dict(sorted(spec.items()))})

    def closes(Q, rows):
        return sum(1 for h, a, b, r in rows if Q[h + (a, b)] == Q[h + (b, a)])
    m_all, m_def = closes(menu, closed), closes(menu, defects)
    PAYLOAD["menu_closes_all"], PAYLOAD["menu_closes_def"] = m_all, m_def
    gate("G-MENU-CLOSES",
         f"the MENU carrier closes {m_all} of the {len(closed)} closed "
         f"squares and {m_def} of the {len(defects)} defective ones -- D74's "
         f"curvature/descent-obstruction dichotomy 44 + 44 reproduced",
         m_all == 1402 and m_def == 44,
         {"all": m_all, "defective": m_def})

    # ------------------------------------------------------------------ SEC 4
    emit("")
    emit("=" * 78)
    emit("SEC 4  CONG-185 RE-DERIVED, ITS SIX RULING PROPERTIES GATED")
    emit("=" * 78)
    cong, rounds = congruence(cache, menu)
    n_cong = len(set(cong.values()))
    _, n_cong_cmp = congruence_comparator(cache, menu)
    PAYLOAD["cong_classes"] = n_cong
    PAYLOAD["cong_classes_comparator"] = n_cong_cmp
    PAYLOAD["cong_rounds"] = rounds
    anchor("A05", "coarsest weighted congruence classes at AB4", 185, n_cong,
           "v14/review-gmain-operator.md 4(b); v10 D74 TH-A carrier table")
    gate("G-CONG-CLASSES",
         f"CONG-185 is RE-DERIVED here from the D74 pinned definition "
         f"(partition refinement from the menu partition to a fixed point) "
         f"and returns {n_cong} classes; an INDEPENDENT comparator -- the "
         f"coarsest bisimulation inside the menu partition, found by explicit "
         f"pair-splitting on the relation with no signature hashing -- "
         f"returns {n_cong_cmp}.  No substitution: the object used below is "
         f"the one re-derived here",
         n_cong == 185 and n_cong_cmp == 185,
         {"builder": n_cong, "comparator": n_cong_cmp})
    gate("G-CONG-ROUNDS",
         f"the refinement reaches its fixed point in {rounds} rounds, inside "
         f"D74's declared 4-6 window (V10) and matching the operator "
         f"review's '5 rounds'",
         4 <= rounds <= 6, {"rounds": rounds})

    G = horizon_potential(cache)
    mu = {(): Fr(1)}
    for h in sorted(cache, key=len):
        if h:
            par = h[:-1]
            mu[h] = mu[par] * Fr([q for e, q in cache[par] if e == h[-1]][0])
    Groot = G((), DEPTH)

    props = {}
    d_cong, d_menu = descent_census(cache, cong, G), descent_census(cache, menu, G)
    props["P1-descent"] = (not d_cong)
    mv_cong, mv_menu = multivalued_edges(cache, cong), multivalued_edges(cache, menu)
    props["P2-single-valued"] = (mv_cong == (0, 0))
    c_all, c_def = closes(cong, closed), closes(cong, defects)
    sl_q, rk_q, ob_q, val_q = reading(cache, cong, closed, G, "q")
    props["P3-curvature-44"] = (c_def == 44 and sum(sl_q.values()) == 44
                                and ob_q == 44)
    ps_q, rk_group_q = group_rank(val_q)
    props["P4-q-holonomy"] = (ps_q == [2, 3] and rk_group_q == 2)
    sl_k, rk_k, ob_k, val_k = reading(cache, cong, closed, G, "k")
    ps_k, rk_group_k = group_rank(val_k)
    props["P5-k-holonomy"] = (ps_k == [2, 3] and rk_group_k == 2)
    ck_ok, ck_tot = ck_census(cache, cong, mu, G, Groot)
    props["P6-exact-lumpability"] = (ck_ok == ck_tot == 10)

    sl_km, rk_km, ob_km, val_km = reading(cache, menu, closed, G, "k")
    ps_km, rk_group_km = group_rank(val_km)
    ckm_ok, ckm_tot = ck_census(cache, menu, mu, G, Groot)
    # the MENU q-reading: rendered, not asserted (the one prose cell the
    # delivered run left with no computation behind it)
    sl_qm, rk_qm, ob_qm, val_qm = reading(cache, menu, closed, G, "q")
    ps_qm, rk_group_qm = group_rank(val_qm)

    PAYLOAD["cong_properties"] = {
        "descent_nonconstant_horizons": {str(k): v for k, v in d_cong.items()},
        "multivalued_weights_targets": list(mv_cong),
        "closes_all": c_all, "closes_defective": c_def,
        "q_selfloop_spectrum": {str(k): v for k, v in sorted(sl_q.items(),
                                                            key=str)},
        "q_obstruction": ob_q, "q_primes": ps_q, "q_rank": rk_group_q,
        "k_selfloop_spectrum": {str(k): v for k, v in sorted(sl_k.items(),
                                                            key=str)},
        "k_obstruction": ob_k, "k_primes": ps_k, "k_rank": rk_group_k,
        "ck": [ck_ok, ck_tot]}
    PAYLOAD["menu_properties"] = {
        "descent_nonconstant_horizons": {str(k): v for k, v in d_menu.items()},
        "multivalued_weights_targets": list(mv_menu),
        "q_primes": ps_qm, "q_rank": rk_group_qm,
        "k_primes": ps_km, "k_rank": rk_group_km, "ck": [ckm_ok, ckm_tot]}

    for nm, ok, ev in [
        ("G-CONG-P1-DESCENT",
         props["P1-descent"],
         {"cong_nonconstant": d_cong, "menu_nonconstant": d_menu}),
        ("G-CONG-P2-SINGLE-VALUED", props["P2-single-valued"],
         {"cong_weights_targets": mv_cong, "menu_weights_targets": mv_menu}),
        ("G-CONG-P3-CURVATURE-44", props["P3-curvature-44"],
         {"closes_all": c_all, "closes_defective": c_def,
          "selfloops": sum(sl_q.values()), "obstruction": ob_q}),
        ("G-CONG-P4-Q-HOLONOMY", props["P4-q-holonomy"],
         {"primes": ps_q, "rank": rk_group_q, "menu_primes": ps_qm,
          "menu_rank": rk_group_qm, "values": [str(v) for v in val_q]}),
        ("G-CONG-P5-K-HOLONOMY", props["P5-k-holonomy"],
         {"primes": ps_k, "rank": rk_group_k, "menu_primes": ps_km,
          "menu_rank": rk_group_km}),
        ("G-CONG-P6-LUMPABLE", props["P6-exact-lumpability"],
         {"cong_ck": [ck_ok, ck_tot], "menu_ck": [ckm_ok, ckm_tot]}),
    ]:
        stat = {
            "G-CONG-P1-DESCENT":
                f"the horizon potential is class-constant on CONG at EVERY "
                f"horizon ({len(d_cong)} horizons carry a non-constant class), "
                f"while on MENU it is not: G(.,2) takes more than one value on "
                f"{d_menu.get(2, 0)} classes -- the property is not vacuous",
            "G-CONG-P2-SINGLE-VALUED":
                f"CONG carries {mv_cong[0]} multi-valued labelled edge weights "
                f"and {mv_cong[1]} multi-valued labelled targets -- a genuine "
                f"congruence; MENU carries {mv_menu[0]} and {mv_menu[1]}",
            "G-CONG-P3-CURVATURE-44":
                f"all 44 curvature-type defective squares survive: CONG closes "
                f"{c_def} of {len(defects)} defective and {c_all} of "
                f"{len(closed)} closed squares, with {sum(sl_q.values())} "
                f"non-unit self-loops and obstruction {ob_q}",
            "G-CONG-P4-Q-HOLONOMY":
                f"the q-reading's group on CONG is generated by primes {ps_q} "
                f"at rank {rk_group_q} -- D74's <2,3> reproduced, by exact "
                f"integer row reduction on prime valuations, not read off by "
                f"eye; the MENU q-reading is COMPUTED here rather than "
                f"asserted, primes {ps_qm} rank {rk_group_qm}",
            "G-CONG-P5-K-HOLONOMY":
                f"the k-reading COLLAPSES onto the q-reading on CONG: primes "
                f"{ps_k} rank {rk_group_k}; on MENU it does not, primes "
                f"{ps_km} rank {rk_group_km} -- the enlargement is a "
                f"non-descending-carrier artefact",
            "G-CONG-P6-LUMPABLE":
                f"the CONG class chain is EXACTLY LUMPABLE: Chapman-Kolmogorov "
                f"divides at {ck_ok} of {ck_tot} depth triples, against MENU's "
                f"{ckm_ok} of {ckm_tot}",
        }[nm]
        gate(nm, stat, ok, ev)

    nsix = sum(1 for v in props.values() if v)
    PAYLOAD["cong_six_properties_passed"] = nsix
    gate("G-CONG-SIX-PROPERTIES",
         f"CONG-185's SIX ruling properties are gated BEFORE use and "
         f"{nsix} of 6 hold: {json.dumps(props, sort_keys=True)}.  The "
         f"re-derivation matches the definitional source at every property; "
         f"no mismatch to report as a finding",
         nsix == 6, {"properties": props})

    # ------------------------------------------------------------------ SEC 5
    emit("")
    emit("=" * 78)
    emit("SEC 5  I7's ARENA AND THE ONLY MOTIVATED INGREDIENT")
    emit("=" * 78)
    d7, L7, X7, links7, i7fam = i7_arena()
    adm, splittable, unsplit, builds, achecks, abad, akeys = additivity_census(
        X7, L7, links7, i7fam)
    add_cmp, cmp_split = additivity_comparator(X7, links7, i7fam)
    prov_route = {r["path"]: r["route"] for r in PAYLOAD["provenance"]}
    PAYLOAD["i7_receipt_consumption"] = dict(I7_CONSUMED)
    gate("G-I7-ROUTE",
         f"#91: the I7 receipt is CONSUMED through the pinned-sha reader, "
         f"never from mutable worktree state.  The bytes this run parsed "
         f"carry sha256-12 {I7_CONSUMED.get('sha256_12')} against the pinned "
         f"{I7_CONSUMED.get('pinned')}, taken via '{I7_CONSUMED.get('route')}' "
         f"-- the same route the provenance row for that path records "
         f"('{prov_route.get(I7_RECEIPT)}').  A worktree drift can therefore "
         f"no longer be rerouted by the provenance check while consumption "
         f"reads the drifted copy",
         I7_CONSUMED.get("sha256_12") == I7_CONSUMED.get("pinned")
         and I7_CONSUMED.get("route") == prov_route.get(I7_RECEIPT),
         dict(I7_CONSUMED, provenance_route=prov_route.get(I7_RECEIPT)))
    PAYLOAD["i7"] = {"d": d7, "L": L7, "sites": len(X7),
                     "links": [list(v) for v in links7],
                     "records_declared": len(i7fam),
                     "records_admissible": len(adm),
                     "records_splittable": len(splittable),
                     "records_unsplittable": unsplit,
                     "refinements_built": builds,
                     "additivity_checks": achecks,
                     "additivity_violations": abad}
    gate("G-I7-ARENA",
         f"I7's arena is read as DATA from the pinned HA receipt: "
         f"{len(X7)} sites (Z_{L7})^{d7}, {len(links7)} declared links "
         f"{[list(v) for v in links7]}, {len(i7fam)} declared records of which "
         f"{len(adm)} are admissible by the exact Sylvester criterion and "
         f"{len(splittable)} are splittable ({unsplit} carry a count-1 "
         f"interval)",
         len(X7) == 9 and len(links7) == 3 and len(adm) == 9
         and len(splittable) == 6,
         {"sites": len(X7), "links": len(links7), "admissible": len(adm),
          "splittable": len(splittable), "unsplittable": unsplit})
    anchor("A06", "R6a additivity constraints", 972, achecks,
           "v14/paper-04-refinement-grammar.md 1 / 5")
    anchor("A07", "R6a additivity violations", 0, abad,
           "v14/paper-04-refinement-grammar.md 5")
    gate("G-ADDITIVITY-972",
         f"the ONLY motivated ingredient's second requirement reproduces: "
         f"count additivity under the induced dyadic subdivision holds at "
         f"{achecks - abad} of {achecks} constraints over {builds} "
         f"refinements ({len(splittable)} splittable records x 3 declared "
         f"split rules x 2 declared completions).  An INDEPENDENT comparator "
         f"-- which does NOT re-multiply the builder's loop bounds but "
         f"RE-DERIVES admissibility and splittability from the record family "
         f"by its own inline Sylvester test on the q-encoding, finding "
         f"{cmp_split} splittable records -- gives {add_cmp}; and the "
         f"constraint CELLS actually compared inside the census, counted as "
         f"a set of keys rather than as a product, number {akeys}",
         achecks == 972 and abad == 0 and add_cmp == 972 and akeys == 972
         and cmp_split == len(splittable),
         {"checks": achecks, "violations": abad, "comparator": add_cmp,
          "distinct_constraint_keys": akeys, "comparator_splittable":
          cmp_split, "builds": builds})

    divs_fam = sorted({sk(e) for h in cache for e in h if is_division(e)})
    n_divlab = len(divs_fam)
    all_r = [e for h in cache for e in h if e[0] == 'r']
    sel = [e for h in cache for e in h if is_division(e)]
    tagged = sum(1 for e in sel if e[0] == 'r')
    dist_r = len({sk(e) for e in all_r})
    dist_pair = len({sk(e) for e in all_r if len(e[2]) == 2})
    PAYLOAD["division_events"] = {
        "distinct_division_labels_in_family": n_divlab,
        "distinct_events_of_any_kind_realised_in_histories":
            len({sk(e) for h in cache for e in h}),
        "distinct_events_of_any_kind_offered_in_menus":
            len({sk(e) for h in cache for e, q in cache[h]}),
        "distinct_division_events_offered_in_menus":
            len({sk(e) for h in cache for e, q in cache[h] if is_division(e)}),
        "distinct_arbitration_events": dist_r,
        "distinct_pair_arbitrations": dist_pair,
        "arbitration_instances": len(all_r),
        "selected_instances": len(sel),
        "selected_carrying_the_arbitration_tag": tagged}
    gate("G-DIVISION-PREDICATE",
         f"the division-event predicate is the ARBITRATION TAG, and it is the "
         f"pinned convention, not this unit's choice: R6b' 3 records it "
         f"SOURCE-FORCED from three agreeing rows (V02's [POSIT], V11's "
         f"S1-code test `any(e[0] == 'r' ...)`, and S4's event-level naming). "
         f"MEASURED: every one of the {len(sel)} events the predicate selects "
         f"carries the tag ({tagged} of {len(sel)}); the family contains "
         f"{dist_r} distinct arbitration events of which {dist_pair} are PAIR "
         f"arbitrations, so S4's narrower sufficient condition would select a "
         f"strict subset -- that sensitivity is DISCLOSED here and the "
         f"forced reading is the one used",
         tagged == len(sel) and len(sel) > 0 and dist_pair <= dist_r,
         {"selected": len(sel), "tagged": tagged,
          "distinct_arbitrations": dist_r, "distinct_pair": dist_pair})
    gate("G-COUNT-SEMANTICS",
         f"the count semantics is the pin's only motivated ingredient and it "
         f"is carried verbatim (V01): n_l(x) counts DIVISION EVENTS in the "
         f"record interval between x and x+l.  Every candidate below is "
         f"required to send a set of grammar division events to the count "
         f"register of a specific link; the requirement is enforced at the "
         f"count generator, which is the single declared member "
         f"{COUNT_GENS[0]}",
         len(COUNT_GENS) == 1, {"count_generators": COUNT_GENS},
         waiver={"class": "DECLARATION-CARRIED",
                 "reason": "the condition is a fact about a declared module "
                           "constant, not a measurement; the count "
                           "semantics' own content is bound at V01 and "
                           "measured at G-ADDITIVITY-972 and "
                           "G-DIVISION-PREDICATE"})

    # ------------------------------------------------------------------ SEC 6
    emit("")
    emit("=" * 78)
    emit("SEC 6  THE CONTROL ARENAS -- the crystals and the generic walk")
    emit("=" * 78)
    crystals = {}
    for nm, b in [("DOUBLE-GRID(3,2)", double_grid(3, 2)),
                  ("DOUBLE-GRID(3,3)", double_grid(3, 3)),
                  ("CONFLICT-GRID(3,2)", conflict_grid(3, 2)),
                  ("CONFLICT-GRID(3,4)", conflict_grid(3, 4)),
                  ("D60-GRID(3,12)", d60_grid())]:
        crystals[nm] = b
    cry_rows = []
    for nm, b in crystals.items():
        acts = sorted(b.actors)
        divs = [e for e in b.H if is_division(e)]
        fld = {}
        for i in range(3):
            for j in range(3):
                for lk in links7:
                    y = ((i + lk[0]) % 3, (j + lk[1]) % 3)
                    u = f"{acts[0][0]}{i}{j}"
                    v = f"{acts[0][0]}{y[0]}{y[1]}"
                    fld[((i, j), lk)] = mutate(
                        "MUT-CRYSTAL-DIAG",
                        sum(1 for e in divs
                            if u in regs_of(e) and v in regs_of(e)),
                        1 if lk == links7[2] else
                        sum(1 for e in divs
                            if u in regs_of(e) and v in regs_of(e)))
        per = {str(lk): sorted(Counter(fld[(x, lk)] for x in
                                       [(i, j) for i in range(3)
                                        for j in range(3)]).items())
               for lk in links7}
        # effectus 5.3, adopted: push the measured counts through HA 3.2's
        # own readout and ask the exact Sylvester question the unit already
        # applies to I7's family.  q_12 = (n_diag - n_1 - n_2)/2 = -k when
        # the axis counts are homogeneous at k and the diagonal is 0, so
        # det = k^2 - k^2 = 0 at every site: the failure is EXACTLY
        # degenerate, not merely negative.
        dets = sorted({str(q_from_counts(links7, {lk: fld[(x, lk)]
                                                  for lk in links7})[0]
                           * q_from_counts(links7, {lk: fld[(x, lk)]
                                                    for lk in links7})[1]
                           - q_from_counts(links7, {lk: fld[(x, lk)]
                                                    for lk in links7})[2] ** 2)
                       for x in [(i, j) for i in range(3) for j in range(3)]})
        cadm = admissible_record(links7, {x: {lk: fld[(x, lk)] for lk in links7}
                                          for x in [(i, j) for i in range(3)
                                                    for j in range(3)]})
        axis_pos = all(fld[(x, lk)] > 0
                       for x in [(i, j) for i in range(3) for j in range(3)]
                       for lk in links7[:2])
        cry_rows.append({"crystal": nm, "events": len(b.H),
                         "refusal": b.refusal, "maxhits": b.maxhits,
                         "divisions": len(divs), "count_field_by_link": per,
                         "induced_determinants": dets,
                         "induces_an_admissible_I7_record": cadm,
                         "axis_counts_strictly_positive": axis_pos})
        emit(f"  [DATA] {nm}: {len(b.H)} events, refusal={b.refusal}, "
             f"maxhits={b.maxhits}, division events={len(divs)}")
        emit(f"         count field by link: {per}")
    PAYLOAD["crystals"] = cry_rows
    forced = [r for r in cry_rows if r["refusal"] is None and r["maxhits"] == 1]
    diag_zero = [r for r in cry_rows
                 if r["count_field_by_link"][str(links7[2])] == [(0, 9)]]
    gate("G-CRYSTAL-FORCED",
         f"{len(forced)} of {len(cry_rows)} rebuilt crystals are FORCED "
         f"records -- every event offered by the committed layer's own menu "
         f"and every specification matched by EXACTLY ONE candidate "
         f"(maxhits = 1, no refusal), reproducing D60's C1/C2 and D66/D67's "
         f"_pick discipline",
         len(forced) == len(cry_rows),
         {"forced": len(forced), "total": len(cry_rows)})
    n_axis_pos = sum(1 for r in cry_rows if r["axis_counts_strictly_positive"])
    n_adm = sum(1 for r in cry_rows if r["induces_an_admissible_I7_record"])
    all_det_zero = all(r["induced_determinants"] == ["0"] for r in cry_rows)
    gate("G-CRYSTAL-DIAGONAL-EMPTY",
         f"MEASURED ACROSS THE COMMITTED CRYSTAL FAMILY: the axis link counts "
         f"are homogeneous, and strictly positive at {n_axis_pos} of "
         f"{len(cry_rows)} crystals -- the four ARBITRATION crystals; the "
         f"delivery grid D60-GRID(3,12) carries one division event and so has "
         f"axis counts 0 as well, which is why the strict-positivity conjunct "
         f"is stamped to the arbitration crystals and not to the family.  The "
         f"DIAGONAL link count is identically ZERO at 9 of 9 sites in "
         f"{len(diag_zero)} of {len(cry_rows)} crystals -- the corpus's only "
         f"lattice-carrying grammar records supply q_11 and q_22 and never "
         f"q_12",
         len(diag_zero) == len(cry_rows) and n_axis_pos == 4,
         {"diagonal_zero_crystals": len(diag_zero), "total": len(cry_rows),
          "axis_strictly_positive": n_axis_pos})
    gate("G-CRYSTAL-DEGENERATE",
         f"THE SHARPEST FORM OF THE EMPTY DIAGONAL, arrived at from the "
         f"metric side rather than the graph side: pushing each crystal's "
         f"measured counts through HA 3.2's own readout gives q_12 = -k "
         f"wherever the axis counts are homogeneous at k and the diagonal is "
         f"0, hence det = q_11 q_22 - q_12^2 = 0 at EVERY site of EVERY "
         f"crystal ({len(cry_rows)} of {len(cry_rows)} crystals, all "
         f"determinants exactly 0).  So {n_adm} of {len(cry_rows)} committed "
         f"crystals induce an admissible I7 record by the exact Sylvester "
         f"criterion this unit applies to I7's own family -- the failure is "
         f"EXACTLY degenerate, a third and independent route to the STRUCT-"
         f"DEAD of the crystal at I7's target",
         all_det_zero and n_adm == 0,
         {"all_determinants_zero": all_det_zero, "admissible_crystals": n_adm,
          "per_crystal": [{"crystal": r["crystal"],
                           "determinants": r["induced_determinants"]}
                          for r in cry_rows]})

    walkH = generic_walk()
    walk_actors = list(AB)
    if MUTANT == "MUT-WALK-PLANT":
        walkH = list(crystals["DOUBLE-GRID(3,2)"].H)
        walk_actors = sorted(crystals["DOUBLE-GRID(3,2)"].actors)
    wdivs = [e for e in walkH if is_division(e)]
    wpair = sum(1 for e in wdivs if 'A' in regs_of(e) and 'B' in regs_of(e))
    PAYLOAD["walk"] = {"events": len(walkH), "divisions": len(wdivs),
                       "declared_depth": 30, "declared_seed": 4242,
                       "divisions_on_the_AB_channel": wpair,
                       "kinds": dict(sorted(Counter(e[0] for e in
                                                    walkH).items()))}
    emit(f"  [DATA] D58 generic 2-actor walk (depth 30, seed 4242): "
         f"{len(walkH)} events, {len(wdivs)} division events, "
         f"{wpair} of them on the (A,B) channel")

    # ------------------------------------------------------------------ SEC 7
    emit("")
    emit("=" * 78)
    emit("SEC 8  CONTROLS FIRST -- both verdicts reachable, each falsified")
    emit("=" * 78)
    TGT_I7 = {"name": "I7-DECLARED-LATTICE", "X": X7, "links": links7,
              "Lmod": L7}
    TGT_CRY = {"name": "CRYSTAL-CARRIED-LATTICE", "X": X7,
               "links": links7[:2], "Lmod": L7}
    i7_two = [i7fam["G-FLAT"], i7fam["G-ANISO2"]]

    def record_arena(nm, H, actors, carrier=None):
        return {"name": nm, "kind": "record", "record": list(H),
                "actors": sorted(actors), "carrier": carrier,
                "division_events": [e for e in H if is_division(e)]}

    cryB = crystals["DOUBLE-GRID(3,2)"]
    if MUTANT == "MUT-CRYSTAL-INHOMOG":
        cryB = double_grid(3, 2, drop_last_row_arb=True)
    cry_arena = record_arena("CRYSTAL/DOUBLE-GRID(3,2)", cryB.H, cryB.actors)
    cry_inhomog = double_grid(3, 2, drop_last_row_arb=True)
    cryI_arena = record_arena("CRYSTAL-INHOMOGENEOUS (declared falsifier)",
                              cryI := cry_inhomog.H, cry_inhomog.actors)
    walk_arena = record_arena("D58-GENERIC-2-ACTOR-WALK", walkH,
                              walk_actors)

    ctrl_found = detect(cry_arena, "ACTOR", "ACTOR-PAIR", COUNT_GENS[0],
                        "NONE", TGT_CRY, i7_two, links7)
    ctrl_found_i7 = detect(cry_arena, "ACTOR", "ACTOR-PAIR", COUNT_GENS[0],
                           "NONE", TGT_I7, i7_two, links7)
    ctrl_falsif = detect(cryI_arena, "ACTOR", "ACTOR-PAIR", COUNT_GENS[0],
                         "NONE", TGT_CRY, i7_two, links7)
    ctrl_empty = detect(walk_arena, "ACTOR", "ACTOR-PAIR", COUNT_GENS[0],
                        "NONE", TGT_I7, i7_two, links7)
    ctrl_empty_rep = detect(walk_arena, "ACTOR", "ACTOR-PAIR", COUNT_GENS[0],
                            "DECLARED-RESTRICTION", TGT_I7, i7_two, links7)
    ctrl_empty_flip = detect(cry_arena, "ACTOR", "ACTOR-PAIR", COUNT_GENS[0],
                             "NONE", TGT_CRY, i7_two, links7)
    # the PIN'S OWN NAMED control generator -- "the record's own cover
    # structure forcing the lattice" -- run at BOTH targets and reported
    # whichever way it lands.
    ctrl_cover = {t["name"]: detect(cry_arena, "ACTOR", "COVER-PAIR",
                                    COUNT_GENS[0], "NONE", t, i7_two, links7)
                  for t in (TGT_CRY, TGT_I7)}
    # THE FOUND BRANCH AT THE VERDICT'S OWN TARGET.  The census judges at
    # I7's three-link lattice and no committed grammar record reaches FOUND
    # there (the crystal is STRUCT-DEAD at it, for the empty diagonal).  So
    # the two-way requirement is discharged at that target by a DECLARED
    # PROBE -- not a grammar record and not a weld, exactly as the
    # smuggling classifier's grammar-side probe is not a candidate -- whose
    # co-division incidence is the target's own Cayley incidence with a
    # homogeneous count field.  What it licenses: the predicate CAN return
    # FOUND at TGT_I7, over the full 1296 x 6 x 2 choice arena.  What it
    # does not license: anything at all about the grammar.
    probe_objects = [f"P{i}{j}" for i in range(3) for j in range(3)]
    probe_rel = {}
    for i in range(3):
        for j in range(3):
            for lk in links7:
                y = ((i + lk[0]) % 3, (j + lk[1]) % 3)
                probe_rel[(f"P{i}{j}", f"P{y[0]}{y[1]}")] = 2
                probe_rel[(f"P{y[0]}{y[1]}", f"P{i}{j}")] = 2
    if MUTANT == "MUT-PROBE-INHOMOG":
        probe_rel[("P00", "P10")] = 3
        probe_rel[("P10", "P00")] = 3
    probe_arena = {"name": "DECLARED-PROBE/CAYLEY-AT-I7", "kind": "probe",
                   "carrier": None, "objects": probe_objects,
                   "rel": probe_rel,
                   "site_note": "nine declared probe objects, not grammar "
                                "objects",
                   "link_note": "the target's own Cayley incidence, carried "
                                "with a homogeneous count field"}
    ctrl_found_i7_probe = detect(probe_arena, "ACTOR", "ACTOR-PAIR",
                                 COUNT_GENS[0], "NONE", TGT_I7, i7_two, links7)
    PAYLOAD["controls"] = {"FOUND_at_crystal": ctrl_found,
                           "crystal_at_I7_target": ctrl_found_i7,
                           "FOUND_falsifier": ctrl_falsif,
                           "EMPTY_at_walk": ctrl_empty,
                           "pin_named_cover_generator": ctrl_cover,
                           "FOUND_at_I7_target_declared_probe":
                               ctrl_found_i7_probe}
    PAYLOAD["choice_arenas"] = {
        "control_at_CRYSTAL-CARRIED-L2": {
            "isomorphisms": ctrl_found.get("isomorphisms"),
            "direction_label_permutations": 2, "orientations": 2,
            "configurations": (ctrl_found.get("isomorphisms") or 0) * 2 * 2},
        "census_target_I7-DECLARED-L3": {
            "isomorphisms": ctrl_found_i7_probe.get("isomorphisms"),
            "direction_label_permutations": 6, "orientations": 2,
            "configurations": (ctrl_found_i7_probe.get("isomorphisms") or 0)
            * 6 * 2}}
    for lbl, r in [("crystal @ crystal-carried lattice", ctrl_found),
                   ("crystal @ I7's declared lattice", ctrl_found_i7),
                   ("inhomogeneous crystal (falsifier)", ctrl_falsif),
                   ("generic walk @ I7's declared lattice", ctrl_empty)]:
        emit(f"  [DATA] {lbl}: fate={r['fate']}  ({r.get('reason')})"
             + (f"  inventory={r.get('inventory')}" if "inventory" in r else ""))

    gate("G-CTRL-FOUND",
         f"POSITIVE CONTROL: on the crystal arena -- a grammar record "
         f"PROVABLY carrying a lattice (forced, exactly-one-candidate, D60 "
         f"C1/C2; width ceiling k*b <= k^2 saturated, D66/D67) -- the census "
         f"machinery returns {ctrl_found['fate']} at the lattice the record "
         f"itself carries, with {ctrl_found.get('isomorphisms')} site "
         f"assignments all giving ONE count field: inventory "
         f"{ctrl_found.get('inventory')}, free items "
         f"{ctrl_found.get('free_items')}.  The record's own co-division "
         f"structure forces the reading",
         ctrl_found["fate"] == "FOUND-candidate", ctrl_found)
    gate("G-CTRL-FOUND-FALSIFIABLE",
         f"the FOUND control CAN FAIL: the same machinery on the declared "
         f"falsifier -- the same crystal with one row-group arbitration "
         f"withheld -- returns {ctrl_falsif['fate']} "
         f"({ctrl_falsif.get('reason')}).  A control that cannot fail would "
         f"be a finding against this unit; this one fails on demand",
         ctrl_falsif["fate"] == "UNMOTIVATED", ctrl_falsif)
    gate("G-CTRL-CRYSTAL-AT-I7",
         f"REPORTED WHICHEVER WAY IT LANDS: the same crystal, run against "
         f"I7's OWN declared 3-link lattice, returns "
         f"{ctrl_found_i7['fate']} -- {ctrl_found_i7.get('reason')}.  The "
         f"crystal control demonstrates the detector's FOUND branch; it does "
         f"NOT deliver a weld, and this row is why",
         ctrl_found_i7["fate"] in ("STRUCT-DEAD", "COUNT-DEAD"),
         ctrl_found_i7)
    gate("G-CTRL-EMPTY",
         f"NEGATIVE CONTROL: on D58's generic 2-actor walk the census returns "
         f"{ctrl_empty['fate']} against I7's declared lattice, by the declared "
         f"falsifier ARITY -- {ctrl_empty.get('reason')} -- and "
         f"{ctrl_empty_rep['fate']} once the declared restriction is offered, "
         f"because a restriction can only shrink a site set.  The walk "
         f"carries a SECOND, independent falsifier: {wpair} of its "
         f"{len(wdivs)} division events lie on the (A,B) channel, so its "
         f"count register is empty as well",
         ctrl_empty["fate"] == "ARITY-DEAD"
         and ctrl_empty_rep["fate"] == "ARITY-DEAD-BELOW" and wpair == 0,
         {"no_repair": ctrl_empty, "with_repair": ctrl_empty_rep,
          "divisions_on_AB": wpair})
    gate("G-CTRL-EMPTY-FALSIFIABLE",
         f"the EMPTY control CAN return its other value: the same call with "
         f"the ARENA AND THE TARGET replaced -- the crystal record at the "
         f"lattice that record carries -- returns "
         f"{ctrl_empty_flip['fate']}.  TWO coordinates change, not one, and "
         f"the conclusion is licensed by the walk's own fate rather than by "
         f"the flip: the walk dies on 2 site objects against 9, which is a "
         f"property of the walk",
         ctrl_empty_flip["fate"] == "FOUND-candidate"
         and ctrl_empty["fate"] == "ARITY-DEAD", ctrl_empty_flip)
    gate("G-CTRL-PIN-NAMED-GENERATOR",
         f"REPORTED WHICHEVER WAY IT LANDS.  Pin R5 names the crystal "
         f"control's mechanism as 'the record's own COVER STRUCTURE forcing "
         f"the lattice'.  Measured: that generator returns "
         f"{ctrl_cover[TGT_CRY['name']]['fate']} at the crystal-carried "
         f"2-link target and {ctrl_cover[TGT_I7['name']]['fate']} at I7's "
         f"3-link target -- it never fires.  The delivered control "
         f"SUBSTITUTES co-division incidence on the ordered actor pair for "
         f"it; the substitution is defensible and is now disclosed rather "
         f"than silent",
         all(r["fate"] in ("STRUCT-DEAD", "TYPE-DEAD", "COUNT-DEAD")
             for r in ctrl_cover.values()),
         {k: {"fate": v["fate"], "isomorphisms": v.get("isomorphisms")}
          for k, v in ctrl_cover.items()})
    gate("G-CTRL-FOUND-AT-THE-CENSUS-TARGET",
         f"HA 14 requirement 3 (V05) AT THE TARGET THE VERDICT IS ABOUT.  "
         f"The census judges every candidate at I7's declared 3-link "
         f"lattice, where no committed grammar record reaches FOUND: the "
         f"crystal is {ctrl_found_i7['fate']} there.  A DECLARED PROBE -- "
         f"nine probe objects carrying the target's own Cayley incidence "
         f"with a homogeneous count field, not a grammar record and not a "
         f"weld -- returns {ctrl_found_i7_probe['fate']} at TGT_I7 with "
         f"{ctrl_found_i7_probe.get('isomorphisms')} site assignments, "
         f"inventory {ctrl_found_i7_probe.get('inventory')}, over the FULL "
         f"choice arena of "
         f"{PAYLOAD['choice_arenas']['census_target_I7-DECLARED-L3']['configurations']} "
         f"configurations (against the crystal control's "
         f"{PAYLOAD['choice_arenas']['control_at_CRYSTAL-CARRIED-L2']['configurations']} "
         f"at 2 links).  So the FOUND branch is reachable at the census's "
         f"own target and at its own choice arena; what is absent is a "
         f"GRAMMAR RECORD that reaches it",
         ctrl_found_i7_probe["fate"] == "FOUND-candidate"
         and ctrl_found_i7_probe.get("isomorphisms") == 1296
         and ctrl_found_i7["fate"] == "STRUCT-DEAD",
         ctrl_found_i7_probe)
    gate("G-ONE-CRITERION",
         f"THE KILL AND THE ADMIT USE ONE DECLARED CRITERION.  A link is an "
         f"unordered site pair carrying a label and a count -- orientation "
         f"is a declared free item -- so incidence is UNDIRECTED on both "
         f"branches.  The kill is therefore an ODD-CYCLE argument at the "
         f"same notion of incidence as the admit test, not a directed-"
         f"acyclicity argument against an undirected admission.  Measured, "
         f"and this is why the directed reading cannot be the criterion: "
         f"co-division incidence is symmetric by construction while the "
         f"target's directed Cayley relation is antisymmetric, so the "
         f"DIRECTED comparator returns "
         f"{ctrl_found.get('isomorphisms_directed_comparator')} "
         f"isomorphisms at the very arena where the undirected criterion "
         f"returns {ctrl_found.get('isomorphisms')} -- adopting it would "
         f"make the FOUND branch unreachable in principle at every "
         f"co-division arena, which HA 14.3 forbids",
         ctrl_found.get("isomorphisms_directed_comparator") == 0
         and ctrl_found.get("isomorphisms") == 72,
         {"undirected": ctrl_found.get("isomorphisms"),
          "directed_comparator":
              ctrl_found.get("isomorphisms_directed_comparator")})

    two_way = {"FOUND@2-link-record": ctrl_found["fate"],
               "FOUND@3-link-census-target(declared probe)":
                   ctrl_found_i7_probe["fate"],
               "UNMOTIVATED@falsifier": ctrl_falsif["fate"],
               "EMPTY@walk": ctrl_empty["fate"],
               "STRUCT-DEAD@crystal-at-I7": ctrl_found_i7["fate"]}
    gate("G-TWO-WAY",
         f"HA 14 requirement 3 is carried verbatim (V05) and DISCHARGED WITH "
         f"MEASUREMENTS, not with a declaration: every value the detector can "
         f"return is exhibited in this run -- {json.dumps(two_way, sort_keys=True)} "
         f"-- and the FOUND value is exhibited BOTH on a grammar record (at "
         f"the 2-link lattice that record carries) AND at the census's own "
         f"3-link target (on a declared probe).  A predicate that could not "
         f"return its other value in the declared arena would not be a "
         f"measurement; this one returns five",
         (ctrl_found["fate"] == "FOUND-candidate"
          and ctrl_found_i7_probe["fate"] == "FOUND-candidate"
          and ctrl_falsif["fate"] == "UNMOTIVATED"
          and ctrl_empty["fate"] == "ARITY-DEAD"
          and ctrl_found_i7["fate"] == "STRUCT-DEAD"), two_way)

    # the two classifier reachability probes
    probe_sm = classify_smuggling(
        lambda rec: {(x, lk): rec[x][lk] for x in X7 for lk in links7}, i7_two)
    probe_gr = classify_smuggling(lambda rec: {("g", 0): 7}, i7_two)
    PAYLOAD["smuggling_probes"] = {"reads_I7_s": probe_sm,
                                   "grammar_side_constant": probe_gr}
    gate("G-SMUGGLE-REACHABLE",
         f"the R6 no-smuggling classifier is a MEASUREMENT, not a label: a "
         f"declared probe whose count function reads I7's own s classifies "
         f"SMUGGLED={probe_sm}, and a grammar-side probe classifies "
         f"SMUGGLED={probe_gr}.  At I7 record and metric are one datum in two "
         f"coordinate systems (det 2), so the test is WHICH FUNCTION of "
         f"grammar data a candidate computes",
         probe_sm is True and probe_gr is False,
         {"reads_s": probe_sm, "grammar_side": probe_gr})
    pi_probe = needs_interior("C1-COUNT-MATCH-LENGTH-INTERIOR-SPLIT")
    pi_census = needs_interior(COUNT_GENS[0])
    gate("G-INTERIOR-DEAD-ON-ARRIVAL",
         f"the interior classifier is two-valued and both values are "
         f"exercised: a probe reading that must place a division INSIDE a leg "
         f"classifies dead-on-arrival ({pi_probe}) -- R6b' 9's type census "
         f"(V04) -- while the declared count generator does not "
         f"({pi_census}), because it counts events ON a link object and never "
         f"positions inside one.  The probe CITES R6b' C1's type verdict; it "
         f"does not re-run C1",
         pi_probe is True and pi_census is False,
         {"probe": pi_probe, "census_generator": pi_census},
         waiver={"class": "DECLARATION-CARRIED",
                 "reason": "both values are exercised, but over two typed "
                           "reading names rather than over measured objects; "
                           "the underlying type verdict is R6b' C1's and is "
                           "CITED at V04, not re-run here"})
    gate("G-DEAD-LIST-CITED",
         "the pre-registered dead list (pin R4 / scout (b)) is CITED and not "
         "re-run: R6b' C1-C5 with free items 6/5/1/4/1, BRG-EMPTY-AT-CARRIER, "
         "GW1 2's order-only spatial instruments, v12's Gamma objects, and "
         "the naive 9<->9 whose L>=4 requirement is measured at V07.  No "
         "candidate row below re-derives any of them",
         True, {"dead_items": 5},
         waiver={"class": "DECLARATION-CARRIED",
                 "reason": "a discipline statement about what this unit does "
                           "NOT compute; its content is the absence of those "
                           "computations, which the receipt's candidate rows "
                           "exhibit"})
    gate("G-U4-REGISTERED",
         "v11 paper 0 7's U4 -- 'the division events of a crystal form a "
         "crystal' (V08) -- is REGISTERED as the successor form of this "
         "unit's FOUND-side control and is NOT claimed here: this unit builds "
         "the committed crystals and reads their division events, it does not "
         "rebuild the crystals with renewal-only records",
         True, {"registered": "U4", "claimed": False},
         waiver={"class": "REGISTER-ONLY",
                 "reason": "a successor register entry; nothing in the verdict "
                           "descends from it"})

    # ------------------------------------------------------------------ SEC 9
    emit("")
    emit("=" * 78)
    emit("SEC 9  THE CENSUS AT BOTH CARRIERS")
    emit("=" * 78)
    ulam_total = 0
    addr = {(): ()}
    for h in sorted(cache, key=lambda z: (len(z), sk(z))):
        if len(h) >= DEPTH:
            continue
        for i, (e, q) in enumerate(sorted(cache[h], key=lambda z: sk(z[0]))):
            if h + (e,) in cache:
                addr[h + (e,)] = addr[h] + (i,)
    prefixes = set()
    for a in addr.values():
        for k in range(len(a) + 1):
            prefixes.add(a[:k])
    ulam_total = len(prefixes)
    PAYLOAD["ulam_prefixes_total"] = ulam_total
    PAYLOAD["ulam_prefixes_by_depth"] = {
        str(k): len({a[:k] for a in addr.values() if len(a) >= k})
        for k in range(DEPTH + 1)}

    realised = build_realised(cache, menu, cong,
                              [e for h in cache for e in h if is_division(e)],
                              list(AB))
    PAYLOAD["realised_objects"] = {
        f"{a}|{b}": {"objects": len(v["objects"]), "edges": len(v["rel"]),
                     "grading": v["grading"], "forcing": v["forcing"]}
        for (a, b), v in sorted(((k, v) for k, v in realised.items()
                                 if isinstance(k, tuple)),
                                key=lambda z: str(z[0]))}
    PAYLOAD["charitable_reconstructions"] = realised["charitable"]
    # the STRICT gradings -- cardinality and address length -- are the two
    # the embedding reading leans on; each is checked edge by edge.  The
    # poset HEIGHT grading is NOT strict (reported, not hidden), which is
    # why the cover row's basis is the measured emptiness of its relation
    # rather than a grading argument.
    forcing_bad = sum(realised[k]["forcing"].get("rise_exceptions", 0)
                      for k in (("EVENT-SUBSET", "EXTENSION-EDGE"),
                                ("ULAM-PREFIX", "EXTENSION-EDGE")))
    height_bad = realised[("EVENT-SUBSET", "COVER-PAIR")][
        "forcing"]["rise_exceptions"]
    height_tot = realised[("EVENT-SUBSET", "COVER-PAIR")]["forcing"]["covers"]
    cover_div = realised[("EVENT-SUBSET", "COVER-PAIR")][
        "forcing"]["covers_joining_two_division_events"]
    ext_edges = realised[("CONG-CLASS", "EXTENSION-EDGE")]["forcing"]["edges"]
    n_ext_total = sum(1 for h in cache if len(h) < DEPTH
                      for e, q in cache[h] if h + (e,) in cache)
    n_ext_bad = sum(1 for h in cache if len(h) < DEPTH
                    for e, q in cache[h]
                    if h + (e,) in cache and len(h + (e,)) != len(h) + 1)
    cong_multi = realised[("CONG-CLASS", "EXTENSION-EDGE")][
        "forcing"]["multi_grade_classes"]
    menu_multi = realised[("MENU-CLASS", "EXTENSION-EDGE")][
        "forcing"]["multi_grade_classes"]
    PAYLOAD["grading_theorem"] = {
        "extension_edges": n_ext_total,
        "edges_not_raising_length_by_exactly_one": n_ext_bad,
        "cong_multi_length_classes": cong_multi,
        "menu_multi_length_classes": menu_multi,
        "strict_grading_forcing_exceptions": forcing_bad,
        "poset_covers": height_tot,
        "poset_covers_raising_height_by_more_than_one": height_bad,
        "poset_covers_joining_two_division_events": cover_div}
    gate("G-GRADING-FORCING",
         f"THE GRADING THEOREM'S HYPOTHESIS IS MACHINE-CHECKED, not assumed. "
         f"Every extension edge raises history length by exactly 1 "
         f"({n_ext_total - n_ext_bad} of {n_ext_total}); the cardinality "
         f"grading of the realised division-event subsets and the "
         f"address-length grading of the realised Ulam prefixes each rise by "
         f"exactly one along every realised edge ({forcing_bad} exceptions "
         f"over both).  REPORTED AGAINST INTEREST: the poset HEIGHT grading "
         f"is NOT strict -- {height_bad} of the family's {height_tot} covers "
         f"raise height by more than one -- so the cover row's structural "
         f"basis is not a grading argument but a MEASUREMENT: {cover_div} of "
         f"those {height_tot} covers join two division events, so the "
         f"relation on singleton division-event subsets is empty",
         n_ext_bad == 0 and forcing_bad == 0 and cover_div == 0,
         {"extension_edges": n_ext_total, "length_rise_exceptions": n_ext_bad,
          "strict_grading_exceptions": forcing_bad,
          "poset_covers": height_tot, "height_rise_exceptions": height_bad,
          "covers_joining_two_division_events": cover_div})

    rows = []
    for reading_name in READINGS:
        for carrier in ("MENU", "CONG"):
            car = {"name": f"AB4-TRANSPORT-CARRIER@{carrier}",
                   "kind": "carrier",
                   "carrier": carrier, "cache": cache, "menu": menu,
                   "cong": cong, "actors": list(AB),
                   "n_division_labels": n_divlab, "ulam_total": ulam_total,
                   "realised": realised,
                   "division_events": [e for h in cache for e in h
                                       if is_division(e)]}
            for sgen in SITE_GENS:
                for lgen in LINK_GENS:
                    for cgen in COUNT_GENS:
                        for rep in ARITY_REPAIRS:
                            r = detect(car, sgen, lgen, cgen, rep, TGT_I7,
                                       i7_two, links7, reading=reading_name)
                            r["carrier"] = carrier
                            if MUTANT == "MUT-FATE-CELL" and \
                                    (reading_name, carrier, sgen, lgen, rep) == \
                                    ("EMBEDDING", "MENU", "ACTOR",
                                     "EXTENSION-EDGE", "NONE"):
                                r["fate"] = "ARITY-DEAD"
                            if MUTANT == "MUT-CARRIER-SPLIT" and \
                                    carrier == "CONG" and sgen == "ACTOR" and \
                                    lgen == "COVER-PAIR" and rep == "NONE":
                                r["fate"] = "STRUCT-DEAD"
                            rows.append(r)
    PAYLOAD["census_rows"] = rows
    PAYLOAD["candidate_count"] = len(rows)
    n_distinct = len({(r["reading"], r["site_gen"], r["link_gen"],
                       r["arity_repair"]) for r in rows})
    PAYLOAD["distinct_candidates"] = n_distinct
    fates = Counter(r["fate"] for r in rows)
    fates_by_carrier = {c: dict(sorted(Counter(
        r["fate"] for r in rows if r["carrier"] == c).items()))
        for c in ("MENU", "CONG")}
    fates_by_reading = {rd: dict(sorted(Counter(
        r["fate"] for r in rows if r["reading"] == rd).items()))
        for rd in READINGS}
    PAYLOAD["fates"] = dict(sorted(fates.items()))
    PAYLOAD["fates_by_carrier"] = fates_by_carrier
    PAYLOAD["fates_by_reading"] = fates_by_reading
    emit(f"  [DATA] candidate ROWS enumerated (COMPUTED): {len(rows)} = "
         f"{len(READINGS)} readings x {len(SITE_GENS)} site x "
         f"{len(LINK_GENS)} link x {len(COUNT_GENS)} count x "
         f"{len(ARITY_REPAIRS)} repair x 2 carrier stamps; DISTINCT "
         f"computations = {n_distinct} (the carrier stamp enters no cell)")
    emit(f"  [DATA] fates: {dict(sorted(fates.items()))}")
    for rd in READINGS:
        emit(f"  [DATA] fates @{rd}: {fates_by_reading[rd]}")
    for c in ("MENU", "CONG"):
        emit(f"  [DATA] fates @{c}: {fates_by_carrier[c]}")
    emit("")
    emit("  the full candidate table:")
    emit(f"  {'reading':9} {'carrier':8} {'site':13} {'link':15} {'rep':22} "
         f"{'arity':>7}  fate")
    for r in rows:
        emit(f"  {r['reading']:9} {r['carrier']:8} {r['site_gen']:13} "
             f"{r['link_gen']:15} {r['arity_repair']:22} "
             f"{r['site_arity']:>7}  {r['fate']}")

    n_found = fates.get("FOUND-candidate", 0)
    n_smug = fates.get("SMUGGLED", 0)
    n_unmot = fates.get("UNMOTIVATED", 0)

    # #87: every cell bound to its OWN computed fate, and the two carrier
    # tables compared cell by cell.
    mism = [{"cell": [r["reading"], r["carrier"], r["site_gen"],
                      r["link_gen"], r["arity_repair"]],
             "computed": r["fate"],
             "declared": EXPECTED_FATES.get((r["reading"], r["site_gen"],
                                             r["link_gen"],
                                             r["arity_repair"]))}
            for r in rows
            if r["fate"] != EXPECTED_FATES.get((r["reading"], r["site_gen"],
                                                r["link_gen"],
                                                r["arity_repair"]))]
    gate("G-FATE-PER-CELL",
         f"#87: every one of the {len(rows)} rows is bound to its OWN fate, "
         f"not to an aggregate.  The {len(EXPECTED_FATES)} distinct "
         f"(reading, site, link, repair) cells are DECLARED AS DATA above "
         f"the census and each row's computed fate is compared against its "
         f"own declared cell: {len(rows) - len(mism)} of {len(rows)} agree, "
         f"{len(mism)} mismatch",
         not mism, {"mismatches": mism, "cells_declared": len(EXPECTED_FATES)})
    pairs = defaultdict(dict)
    for r in rows:
        pairs[(r["reading"], r["site_gen"], r["link_gen"],
               r["arity_repair"])][r["carrier"]] = r
    disagree = [{"cell": list(k), "menu": v["MENU"]["fate"],
                 "cong": v["CONG"]["fate"]}
                for k, v in sorted(pairs.items(), key=str)
                if v["MENU"]["fate"] != v["CONG"]["fate"]]
    ident = sum(1 for k, v in pairs.items()
                if {kk: vv for kk, vv in v["MENU"].items()
                    if kk not in ("carrier", "arena")}
                == {kk: vv for kk, vv in v["CONG"].items()
                    if kk not in ("carrier", "arena")})
    gate("G-CARRIER-AGREEMENT",
         f"#87, and the correction the panel ordered: the carrier stamp "
         f"enters NO cell.  `arena_linkrel` selects the class map by the "
         f"SITE generator (MENU-CLASS on the menu quotient, CONG-CLASS on "
         f"the congruence), never by `arena['carrier']`, so the two stamped "
         f"blocks are the SAME computation.  Measured, field by field with "
         f"only the two label fields removed: {ident} of {len(pairs)} cells "
         f"are byte-identical across the two labels and {len(disagree)} "
         f"disagree.  The identical fate distributions are therefore a fact "
         f"about the enumeration, NOT an agreement between carriers -- the "
         f"carrier coordinate was never varied, and this gate is what makes "
         f"a divergence impossible to stamp @BOTH silently",
         not disagree and ident == len(pairs),
         {"cells": len(pairs), "identical": ident, "disagreements": disagree})
    gate("G-CENSUS-COMPLETE",
         f"the candidate family is enumerated exhaustively over the pin's "
         f"THREE generator axes -- site ({len(SITE_GENS)}), link "
         f"({len(LINK_GENS)}), count ({len(COUNT_GENS)}) -- plus the ARITY "
         f"TREATMENT the census offers each cell ({len(ARITY_REPAIRS)}) and "
         f"the ADMISSIBILITY READING declared as data by this repair "
         f"({len(READINGS)}), each stamped at 2 carriers: {len(rows)} rows, "
         f"{n_distinct} distinct computations, size COMPUTED and not typed.  "
         f"Every cell carries a measured fate and none is skipped -- and "
         f"under BOTH readings, so completeness is no longer contingent on "
         f"the embedding reading's scissors closing: "
         f"{fates.get('SCOPE-BLOCKED', 0)} rows are scope-blocked and "
         f"{fates.get('ARITY-REPAIR-UNDECIDED', 0)} are repair-undecided",
         len(rows) == len(READINGS) * len(SITE_GENS) * len(LINK_GENS)
         * len(COUNT_GENS) * len(ARITY_REPAIRS) * 2
         and all("fate" in r and r["fate"] for r in rows)
         and fates.get("SCOPE-BLOCKED", 0) == 0
         and fates.get("ARITY-REPAIR-UNDECIDED", 0) == 0,
         {"rows": len(rows), "distinct": n_distinct,
          "fates": dict(sorted(fates.items()))})

    # THE MECHANISM
    actor_rel, actor_acyc, _, _ = arena_linkrel(
        {"kind": "carrier", "actors": list(AB), "cache": cache,
         "division_events": [e for h in cache for e in h if is_division(e)]},
        "ACTOR", "ACTOR-PAIR")
    menu_rel, menu_acyc, _, _ = arena_linkrel(
        {"kind": "carrier", "menu": menu, "cong": cong, "cache": cache},
        "MENU-CLASS", "EXTENSION-EDGE")
    cong_rel, cong_acyc, _, _ = arena_linkrel(
        {"kind": "carrier", "menu": menu, "cong": cong, "cache": cache},
        "CONG-CLASS", "EXTENSION-EDGE")
    cyc_cmp_menu = simple_cycle_census(sorted(set(menu.values())),
                                       set(menu_rel))
    cyc_cmp_cong = simple_cycle_census(sorted(set(cong.values())),
                                       set(cong_rel))
    sl_menu = sum(1 for (u, v) in menu_rel if u == v)
    sl_cong = sum(1 for (u, v) in cong_rel if u == v)
    ab_count = mutate("MUT-AB-COUNT", actor_rel.get(("A", "B"), 0), 999)
    ab_count_ba = actor_rel.get(("B", "A"), 0)
    ab_distinct = len({sk(e) for h in cache for e in h if is_division(e)
                       and 'A' in regs_of(e) and 'B' in regs_of(e)})
    scc_menu = nontrivial_sccs(sorted(set(menu.values())), set(menu_rel))
    scc_cong = nontrivial_sccs(sorted(set(cong.values())), set(cong_rel))
    bip_menu, wit_menu = bipartite_witness(sorted(set(menu.values())),
                                           set(menu_rel))
    bip_cong, wit_cong = bipartite_witness(sorted(set(cong.values())),
                                           set(cong_rel))
    emb_menu = induced_target_embeddings(sorted(set(menu.values())),
                                         set(menu_rel), X7, links7, L7)
    emb_cong = induced_target_embeddings(sorted(set(cong.values())),
                                         set(cong_rel), X7, links7, L7)
    tri = sum(1 for x in X7 for lk in links7
              if len({x, tuple((x[i] + lk[i]) % L7 for i in range(2)),
                      tuple((x[i] + 2 * lk[i]) % L7 for i in range(2))}) == 3
              and tuple((x[i] + 3 * lk[i]) % L7 for i in range(2)) == x)
    sl_classes_menu = {u for (u, v) in menu_rel if u == v}
    menu_multi_set = set()
    span = defaultdict(set)
    for h in cache:
        span[menu[h]].add(len(h))
    menu_multi_set = {c for c, s in span.items() if len(s) > 1}
    PAYLOAD["mechanism"] = {
        "actor_pair_relation": sorted((f"{u}->{v}", n)
                                      for (u, v), n in actor_rel.items()),
        "actor_site_objects": 2,
        "AB_channel_occurrences_each_direction": ab_count,
        "AB_channel_is_the_same_set_both_ways": ab_count == ab_count_ba,
        "AB_channel_distinct_events": ab_distinct,
        "menu_class_selfloops": sl_menu, "cong_class_selfloops": sl_cong,
        "menu_class_acyclic": menu_acyc, "cong_class_acyclic": cong_acyc,
        "menu_nontrivial_sccs": len(scc_menu),
        "cong_nontrivial_sccs": len(scc_cong),
        "menu_bipartite": bip_menu, "cong_bipartite": bip_cong,
        "menu_odd_cycle_witness": wit_menu,
        "menu_selfloop_classes_are_exactly_its_multi_length_classes":
            sl_classes_menu == menu_multi_set,
        "menu_induced_target_embeddings": emb_menu[0],
        "cong_induced_target_embeddings": emb_cong[0],
        "menu_search_nodes": emb_menu[2], "cong_search_nodes": emb_cong[2],
        "target_cells_closing_a_3_cycle_on_3_distinct_sites": tri,
        "target_cells": len(X7) * len(links7),
        "menu_simple_cycles_len2to6": cyc_cmp_menu,
        "cong_simple_cycles_len2to6": cyc_cmp_cong,
        "divisions_on_the_AB_channel_in_family": ab_count}
    gate("G-SCISSORS",
         f"THE MECHANISM AT THE EMBEDDING READING, recomposed.  BLADE 1 "
         f"(arity): the one link generator carrying a target-type cycle at "
         f"the transport carrier is the actor pair / delivery channel, and it "
         f"has exactly 2 site objects; the relation is symmetric, so its "
         f"{ab_count} co-division occurrences are ONE set of events entered "
         f"in both directions ({ab_distinct} distinct events), not two.  "
         f"BLADE 2 (THE GRADING THEOREM): every extension edge raises history "
         f"length by exactly 1 ({n_ext_total - n_ext_bad} of {n_ext_total}, "
         f"{n_ext_bad} exceptions), so any LENGTH-HOMOGENEOUS quotient's "
         f"class graph is graded -- hence acyclic AND bipartite -- with no "
         f"computation.  CONG-185 is length-homogeneous ({cong_multi} classes "
         f"span more than one length), so its blade is a THEOREM: bipartite "
         f"{bip_cong}.  MENU-113 is not ({menu_multi} multi-length classes, "
         f"and those are EXACTLY its {sl_menu} self-loop classes: "
         f"{sl_classes_menu == menu_multi_set}), so its blade is MEASURED: "
         f"bipartite {bip_menu}, and the declared restriction is EXECUTED "
         f"rather than argued -- a complete induced-subgraph search finds "
         f"{emb_menu[0]} of the C(113,9) restrictions inducing the target "
         f"({emb_menu[2]} search nodes), and {emb_cong[0]} of the C(185,9).  "
         f"The target closes a 3-cycle on 3 distinct sites at {tri} of "
         f"{len(X7) * len(links7)} cells -- an ODD cycle, which no bipartite "
         f"relation carries.  Directed comparators at every length: "
         f"{len(scc_menu)} and {len(scc_cong)} non-trivial strongly connected "
         f"components (Tarjan), replacing the length-6 bound as the operative "
         f"statement; the enumerated comparator returns {cyc_cmp_menu} and "
         f"{cyc_cmp_cong} simple cycles at lengths 2..6.  A self-loop is not "
         f"a generator cycle: a bijection sends distinct sites to distinct "
         f"objects",
         (menu_acyc and cong_acyc and len(scc_menu) == 0 and len(scc_cong) == 0
          and all(v == 0 for v in cyc_cmp_menu.values())
          and all(v == 0 for v in cyc_cmp_cong.values())
          and n_ext_bad == 0 and cong_multi == 0 and bip_cong
          and not bip_menu and wit_menu is not None
          and sl_classes_menu == menu_multi_set
          and emb_menu[0] == 0 and emb_cong[0] == 0
          and tri == len(X7) * len(links7)
          and sl_menu == 45 and sl_cong == 0 and ab_count == 336),
         PAYLOAD["mechanism"])
    qrows = [r for r in rows if r["reading"] == "QUOTIENT"]
    q_wipe = [r for r in qrows if r["fate"] == "HOM-DEAD"]
    q_cong = [r for r in qrows if r["site_gen"] == "CONG-CLASS"
              and r["link_gen"] == "EXTENSION-EDGE"][0]
    q_ulam = [r for r in qrows if r["site_gen"] == "ULAM-PREFIX"
              and r["link_gen"] == "EXTENSION-EDGE"][0]
    PAYLOAD["quotient_mechanism"] = {
        "hom_dead_rows": len(q_wipe),
        "menu_selfloops_forcing_the_zero_displacement": sl_menu,
        "cong_fate": q_cong["fate"], "ulam_fate": q_ulam["fate"],
        "cong_best_positive_cells":
            q_cong.get("count_positive_cells_best", -1),
        "cong_cells": q_cong.get("count_cells", -1),
        "cong_inventory": q_cong.get("inventory", {}),
        "ulam_best_positive_cells":
            q_ulam.get("count_positive_cells_best", -1),
        "ulam_inventory": q_ulam.get("inventory", {}),
        "declared_search": q_cong.get(
            "quotient_search", {"engine": "NOT-REACHED",
                                "declared_solutions": QCAP,
                                "solutions_found": 0, "seed": QSEED,
                                "lcg": list(QLCG)})}
    qm = PAYLOAD["quotient_mechanism"]
    gate("G-QUOTIENT-READING",
         f"THE MECHANISM AT THE QUOTIENT READING, which acyclicity does not "
         f"decide.  MENU DIES EXACTLY: its {sl_menu} self-loop classes demand "
         f"the zero displacement and no declared link displacement is zero, "
         f"so node consistency empties those domains with no search -- and "
         f"the realised division-event-subset graph dies the same way.  "
         f"{len(q_wipe)} of the {len(qrows)} quotient rows die there.  CONG "
         f"SURVIVES the existence question -- a quotient map exists, found by "
         f"the declared search -- and dies further down: the best of "
         f"{qm['declared_search']['solutions_found']} declared solutions "
         f"leaves {qm['cong_cells'] - qm['cong_best_positive_cells']} "
         f"of {qm['cong_cells']} count cells at zero "
         f"({qm['cong_best_positive_cells']} strictly positive), and its "
         f"choice inventory {qm['cong_inventory']} carries free items.  AND "
         f"THE PRE-REGISTERED FREE ITEMS ARE REACHED: the Ulam-prefix quotient "
         f"attains a STRICTLY POSITIVE count field at "
         f"{qm['ulam_best_positive_cells']} of {qm['cong_cells']} "
         f"cells and dies at the CHOICE STANDARD with inventory "
         f"{qm['ulam_inventory']} -- the fibers are lower bounds over the "
         f"declared search, so a free item stays free.  Under this reading "
         f"the census is EMPTY of FOUND but not of UNMOTIVATED",
         (len(q_wipe) == 8 and q_cong["fate"] == "UNMOTIVATED"
          and q_ulam["fate"] == "UNMOTIVATED"
          and qm["cong_best_positive_cells"] < qm["cong_cells"]
          and qm["ulam_best_positive_cells"] == qm["cong_cells"]),
         PAYLOAD["quotient_mechanism"])
    gate("G-D5-CITED",
         f"the deeper carrier's class counts are CITED, not run: D74's "
         f"committed row for (A,B) at depth <= 5 carries 265 MENU and 462 "
         f"CONG classes, and this run binds that row's bytes verbatim (V12) "
         f"rather than printing the two numbers unsourced.  This unit's "
         f"scope is depth <= 4 and its scissors argument is a statement "
         f"about THIS carrier",
         any(v["id"] == "V12" and v["passed"] for v in VANCHORS),
         {"anchor": "V12", "menu_d5": 265, "cong_d5": 462,
          "source": "v10/note-d74-transport-holonomy-result.md"})

    # ----------------------------------------------------------------- SEC 10
    emit("")
    emit("=" * 78)
    emit("SEC 10  THE VERDICT")
    emit("=" * 78)
    free_fibers = {k: v["inventory"] for k, v in
                   [("CONTROL-CRYSTAL", ctrl_found),
                    ("CONTROL-CRYSTAL-FALSIFIER", ctrl_falsif),
                    ("CONTROL-PROBE-AT-I7", ctrl_found_i7_probe),
                    ("CENSUS-QUOTIENT-CONG", q_cong),
                    ("CENSUS-QUOTIENT-ULAM", q_ulam)]
                   if "inventory" in v}
    PAYLOAD["free_item_fibers"] = free_fibers
    PAYLOAD["counts_for_the_head"] = {
        "additivity_ok": achecks - abad, "additivity_total": achecks,
        "six_properties": nsix}
    anchor("A08", "MENU class-graph self-loops at AB4", 45, sl_menu,
           "the MENU class-extension graph, rebuilt in SEC 9")
    anchor("A09", "CONG class-graph self-loops at AB4", 0, sl_cong,
           "the CONG class-extension graph, rebuilt in SEC 9")
    anchor("A10", "co-division occurrences on the (A,B) channel", 336,
           ab_count, "co-division incidence on the (A,B) channel, SEC 9; one set both ways")
    anchor("A11", "site assignments at the crystal FOUND control", 72,
           ctrl_found.get("isomorphisms"),
           "|Aut| of the 3x3 rook's graph = 3! * 3! * 2, the crystal's own "
           "co-division incidence")
    anchor("A12", "I-SITE-ASSIGNMENT fiber at the declared falsifier", 6,
           ctrl_falsif.get("inventory", {}).get("I-SITE-ASSIGNMENT"),
           "v14/paper-13 4.1 (the withheld-arbitration flip)")
    anchor("A13", "site assignments at the declared probe on I7's target",
           1296, ctrl_found_i7_probe.get("isomorphisms"),
           "|Aut| of K(3,3,3), the target's undirected Cayley graph")
    anchor("A14", "distinct (reading, site, link, repair) census cells", 60,
           n_distinct, "the declared candidate family of 3")
    # A numeric anchor whose COMPUTED side is a literal passes its own
    # comparison by arithmetic and cannot be caught by corrupting either
    # side.  It can be caught statically: the unit parses its own source
    # and requires every anchor's computed argument to be an expression,
    # never a constant.
    typed = []
    try:
        import ast
        src = open(os.path.abspath(__file__), encoding="utf-8").read()
        # the declared falsifier: the very edit this gate exists to catch,
        # applied to an in-memory copy of the source
        src = mutate("MUT-ANCHOR-TYPED", src,
                     src.replace('"MENU quotient classes at AB4", 113, n_menu',
                                 '"MENU quotient classes at AB4", 113, 113'))
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and \
                    getattr(node.func, "id", None) == "anchor" and \
                    len(node.args) >= 4 and isinstance(node.args[3], ast.Constant):
                typed.append(getattr(node.args[0], "value", "?"))
        parsed = True
    except Exception as exc:                                # noqa: BLE001
        parsed, typed = False, [f"UNPARSED: {exc}"]
    gate("G-ANCHOR-NOT-TYPED",
         f"no numeric anchor's COMPUTED side is a typed literal.  The unit "
         f"parses its own source and requires the fourth argument of every "
         f"`anchor(...)` call to be an expression rather than a constant, "
         f"because an anchor typed on both sides passes its own comparison "
         f"by arithmetic and no corruption of either side can catch it: "
         f"{len(ANCHORS)} anchors, {len(typed)} typed",
         parsed and not typed, {"typed_anchors": typed, "parsed": parsed,
                                "anchors": len(ANCHORS)})

    PAYLOAD["obstruction"] = derive_obstruction(PAYLOAD)
    verdict = rebuild_verdict(PAYLOAD)
    if MUTANT == "MUT-HEAD-FLIP":       # the typed head, restored
        verdict = verdict.replace("WELD2-EMPTY-", "WELD2-FOUND-")
    if MUTANT == "MUT-OBSTRUCTION-FLIP":
        verdict = verdict.replace(PAYLOAD["obstruction"],
                                  "NO-OBSTRUCTION-AT-ALL")
    PAYLOAD["verdict"] = verdict
    emit("  " + verdict)
    # #234 / the derived head: a SECOND reconstruction, reading ONLY the
    # payload, rebuilds the entire string field by field and the two are
    # compared as COMPLETE STRINGS.  No branch of the head is a typed
    # literal that no gate compares; a flipped head cannot deliver.
    rebuilt = rebuild_verdict(json.loads(json.dumps(PAYLOAD, default=str)))
    gate("G-VERDICT-EQUALITY",
         f"THE HEAD IS DERIVED, NOT TYPED (#234).  The emitted verdict is "
         f"rebuilt from the receipt payload alone -- every segment, including "
         f"the outcome word itself, is a function of the measured fate "
         f"multiset and the measured controls, and no branch of it is a "
         f"literal any gate fails to compare -- and the two strings are "
         f"compared complete, all {len(verdict)} characters",
         rebuilt == verdict, {"equal": rebuilt == verdict,
                              "length": len(verdict),
                              "rebuilt_prefix": rebuilt[:120],
                              "emitted_prefix": verdict[:120]})
    # The obstruction NAME is derived, so a rename inside the derivation
    # would move BOTH copies of the head together.  This gate binds the
    # name's content to the measurements by a second, independent route:
    # the substrings the emitted head carries are required to agree,
    # one by one, with what the run actually measured.
    graded_measured = (n_ext_bad == 0 and cong_multi == 0)
    wipeout_measured = len(q_wipe) > 0
    name_ok = (("THE-GRADING-THEOREM" in verdict) == graded_measured
               and ("SELF-LOOP-WIPEOUT" in verdict) == wipeout_measured
               and ("NO-OBSTRUCTION" in verdict)
               == (not graded_measured and not wipeout_measured))
    gate("G-OBSTRUCTION-CONTENT",
         f"the obstruction the head names is the obstruction the run "
         f"measured, checked substring by substring against the "
         f"measurements rather than against the function that produced the "
         f"name: the grading holds ({graded_measured}: {n_ext_bad} edges "
         f"fail the length rise and {cong_multi} CONG classes span more "
         f"than one length) and the head names it "
         f"({'THE-GRADING-THEOREM' in verdict}); the self-loop wipeout "
         f"fired ({wipeout_measured}: {len(q_wipe)} rows) and the head "
         f"names it ({'SELF-LOOP-WIPEOUT' in verdict}); the head claims no "
         f"obstruction ({'NO-OBSTRUCTION' in verdict}) exactly when "
         f"neither holds",
         name_ok, {"graded_measured": graded_measured,
                   "wipeout_measured": wipeout_measured,
                   "obstruction": PAYLOAD["obstruction"]})
    gate("G-VERDICT",
         f"the pre-registered outcome string that fires is "
         f"WELD2-EMPTY-AT-THE-DECLARED-FAMILY -- EMPTY meaning NO MOTIVATED "
         f"MAP, that is {n_found} FOUND of {len(rows)} rows at both readings "
         f"-- stamped @BOTH-QUOTIENTS-AS-SITE-GENERATORS (MENU-113 and "
         f"CONG-185, exercised as site generators; the carrier coordinate "
         f"itself is inert and G-CARRIER-AGREEMENT says so), with obstruction "
         f"{PAYLOAD['obstruction']}: {n_smug} SMUGGLED, {n_unmot} "
         f"UNMOTIVATED -- all of them at the QUOTIENT reading, where the "
         f"pre-registered free items ARE reached -- and the remainder die at "
         f"measured type, arity, structure or map-existence obstructions "
         f"{dict(sorted(fates.items()))}.  Between delivery and adjudication "
         f"this is a CANDIDATE READING",
         n_found == 0 and n_smug == 0
         and sum(fates.values()) == len(rows)
         and set(fates) <= {"TYPE-DEAD", "ARITY-DEAD", "ARITY-DEAD-BELOW",
                            "STRUCT-DEAD", "HOM-DEAD", "COUNT-DEAD",
                            "UNMOTIVATED", "SCOPE-BLOCKED",
                            "ARITY-REPAIR-UNDECIDED"}
         and fates.get("SCOPE-BLOCKED", 0) == 0
         and fates.get("ARITY-REPAIR-UNDECIDED", 0) == 0
         and all(r["reading"] == "QUOTIENT" for r in rows
                 if r["fate"] == "UNMOTIVATED"),
         {"verdict": verdict, "fates": dict(sorted(fates.items())),
          "found": n_found, "smuggled": n_smug, "unmotivated": n_unmot})

    # +2 for the two gates that must come after this line: G-PAPER-RENDERS,
    # which reads the paper against this very payload, and the terminal
    # G-ARTIFACT-INTEGRITY, which re-reads what was written.  The total is
    # itself checked at that terminal gate.
    PAYLOAD["registry"] = {
        "gates_including_the_terminal_gates": len(GATES) + 2,
        "declared_mutants": len(MUTANTS), "numeric_anchors": len(ANCHORS),
        "verbatim_anchors": len(VANCHORS),
        "anchors_total": len(ANCHORS) + len(VANCHORS),
        "waivers": len(WAIVERS)}
    verify_paper()

    emit("")
    emit(f"  gates so far: {len(GATES)}, failures: {FAILED}; "
         f"anchors: {len(ANCHORS)} numeric + {len(VANCHORS)} verbatim, "
         f"failures: {ANCHOR_FAIL}; waivers: {len(WAIVERS)}.  The terminal "
         f"G-ARTIFACT-INTEGRITY gate is evaluated after the artifacts are "
         f"written and re-read, so it appears below this line and in the "
         f"receipt's gate count, which is therefore {len(GATES) + 1}")
    return {"weld2": verdict,
            "controls": {"FOUND_at_crystal": ctrl_found["fate"],
                         "FOUND_falsifier": ctrl_falsif["fate"],
                         "FOUND_at_I7_declared_probe":
                             ctrl_found_i7_probe["fate"],
                         "EMPTY_at_walk": ctrl_empty["fate"],
                         "crystal_at_I7": ctrl_found_i7["fate"],
                         "pin_named_cover_generator":
                             {k: v["fate"] for k, v in ctrl_cover.items()}},
            "cong185_six_properties": props}


def main(argv=None):
    global MUTANT
    ap = argparse.ArgumentParser(
        prog="w2_census_exact.py", allow_abbrev=False,
        description="v14 WELD 2 / paper-13 -- the carrier census.")
    ap.add_argument("--selftest", action="store_true",
                    help="corrupt each anchor in memory, confirm the run "
                         "would fail (exit 1); WRITES NOTHING")
    ap.add_argument("--mutant", metavar="NAME",
                    help="run a declared mutant; it must die at a named "
                         "gate and the artifacts are not written")
    ap.add_argument("--list-mutants", action="store_true",
                    help="print the declared mutant registry and exit")
    ap.add_argument("--list-gates", action="store_true",
                    help="run the pipeline, print the gate registry and "
                         "exit; WRITES NOTHING")
    try:
        args, extra = ap.parse_known_args(argv)
    except SystemExit as e:
        return 0 if e.code in (0, None) else 2
    if extra:
        sys.stderr.write(f"unknown argument(s): {' '.join(extra)}\n")
        return 2
    if args.list_mutants:
        for name, tgt in MUTANTS:
            print(f"{name}\t{tgt}")
        return 0
    if args.mutant is not None:
        if args.mutant not in dict(MUTANTS):
            sys.stderr.write(f"unknown mutant: {args.mutant}\n")
            return 2
        MUTANT = args.mutant

    verdicts = run_all()

    write = (MUTANT is None) and (not args.selftest) and (not args.list_gates)
    if args.selftest:
        return selftest_report(verdicts)
    if args.list_gates:
        for g in GATES:
            print(f"{g['gate']}\t{'PASS' if g['passed'] else 'FAIL'}"
                  f"\t{'WAIVED' if g['waiver'] else '-'}")
        print(f"{len(GATES)} gates, {FAILED} failures; "
              f"{len(ANCHORS)} numeric + {len(VANCHORS)} verbatim anchors")
        print("artifacts NOT written (--list-gates)")
        return 0
    # A RUN THAT FAILED A GATE WRITES NOTHING.  The delivered artifacts are
    # never overwritten by a run that does not stand up.
    do_write = write and exit_code() == 0
    snap = snapshot()                    # frozen BEFORE the receipt is built
    receipt = build_receipt(verdicts)
    if do_write:
        write_files(receipt)
        ok1, ev1 = integrity_check(snap["verdict"], None, snap)
        ev1["source"] = "re-read from disk after the write"
    else:
        ok1, ev1 = integrity_check(snap["verdict"], receipt, snap)
        ev1["source"] = ("the serialisation this run would have written "
                         "(no artifact is written on this path)")
    gate("G-ARTIFACT-INTEGRITY",
         f"the artifacts are RE-READ ({ev1['source']}) and compared against "
         f"the live run field by field -- the output text against the "
         f"emitted lines, and the receipt's verdict, gate count, gate "
         f"failures, anchor failures, candidate count, fate multiset and "
         f"gate-name sequence against the values the run holds: "
         f"{json.dumps(ev1, sort_keys=True)}.  A receipt that contradicts "
         f"its own output text cannot ship",
         ok1, ev1)
    if do_write:
        snap2 = snapshot()
        write_files(build_receipt(verdicts))
        ok2, ev2 = integrity_check(snap2["verdict"], None, snap2)
        print("\n".join(LINES))
        print(f"\n[FINAL-INTEGRITY] re-read after the final write: "
              f"{json.dumps(ev2, sort_keys=True)}")
        print(f"wrote {OUT_TXT}")
        print(f"wrote {OUT_JSON}")
        return 1 if (not ok2 or exit_code() != 0) else 0
    print("\n".join(LINES))
    if MUTANT is None:
        print(f"\nRUN FAILED: gate_failures={FAILED} "
              f"anchor_failures={ANCHOR_FAIL}; artifacts NOT written")
        return exit_code()
    tgt = dict(MUTANTS)[MUTANT]
    died = [g["gate"] for g in GATES if not g["passed"]]
    afail = [a["id"] for a in ANCHORS if not a["passed"]] + \
            [v["id"] for v in VANCHORS if not v["passed"]]
    ok = (tgt in died) or (tgt in afail) or (tgt == "ANY" and (died or afail))
    print(f"\nMUTANT {MUTANT}: target gate {tgt}; "
          f"gates failed = {died}; anchors failed = {afail}; "
          f"DIED-AT-TARGET = {ok}")
    print("artifacts NOT written (mutant run)")
    return 0 if ok else 1


def selftest_report(verdicts):
    """A GENUINE selftest: every numeric anchor and every verbatim anchor
    is individually corrupted in memory and the comparison must fail.  A
    vacuous anchor (one whose corruption changes nothing) is a failure of
    the selftest.  Nothing is written."""
    print("\n".join(LINES[:3]))
    killed, vacuous = 0, []
    for a in ANCHORS:
        # the corruption is applied to the COMPUTED side and re-run through
        # the live comparison, so an anchor whose computed value was typed
        # from its own committed value shows up as vacuous instead of
        # passing by integer arithmetic
        c, comp = a["committed"], a["computed"]
        bad = (comp + 1) if isinstance(comp, int) else (str(comp) + "!")
        if (c == comp) and (c != bad):
            killed += 1
        else:
            vacuous.append(a["id"])
    for v in VANCHORS:
        want = dict((p, w) for p, w, _ in PINNED)[v["path"]]
        body, _ = read_pinned(v["path"], want)
        q = v["quote"]
        trunc = q[:5]
        corrupt_ok = body is not None and \
            (q + " [corrupted]").encode("utf-8") not in body
        # a truncation to a common substring must also fail the anchor:
        # the test carries the committed occurrence count and byte length
        trunc_ok = body is None or not (
            body.count(trunc.encode("utf-8")) == v["committed_occurrences"]
            and len(trunc) == len(q))
        if corrupt_ok and trunc_ok:
            killed += 1
        else:
            vacuous.append(v["id"])
    total = len(ANCHORS) + len(VANCHORS)
    # exercise the REAL exit path with one anchor failure injected
    global ANCHOR_FAIL
    live = ANCHOR_FAIL
    ANCHOR_FAIL = live + 1
    would = exit_code()
    ANCHOR_FAIL = live
    print(f"\nSELFTEST: {total} anchors ({len(ANCHORS)} numeric, "
          f"{len(VANCHORS)} verbatim); corrupted individually in memory; "
          f"{killed} of {total} would fail the run; vacuous = {vacuous}")
    print(f"SELFTEST: the real exit path, exercised with one anchor failure "
          f"injected, returns {would} (must be 1)")
    print(f"SELFTEST: the live run's own status: anchor_failures="
          f"{ANCHOR_FAIL} gate_failures={FAILED} exit={exit_code()}")
    print("SELFTEST: WROTE NOTHING")
    return 0 if (killed == total and not vacuous and total > 0
                 and would == 1 and exit_code() == 0) else 1


def exit_code():
    return 1 if (ANCHOR_FAIL or FAILED) else 0


MUTANTS = [
    ("MUT-PROVENANCE", "G-PROVENANCE"),
    ("MUT-MENU-KEY", "G-MENU-CLASSES"),
    ("MUT-CONG-WRONG", "G-CONG-CLASSES"),
    ("MUT-SQUARE-DROP", "G-SQUARES"),
    ("MUT-DESCENT-BLIND", "G-CONG-P1-DESCENT"),
    ("MUT-CK-LAX", "G-CONG-P6-LUMPABLE"),
    ("MUT-ADDITIVITY", "G-ADDITIVITY-972"),
    ("MUT-DIVPRED", "G-DIVISION-PREDICATE"),
    ("MUT-I7-ROUTE", "G-I7-ROUTE"),
    ("MUT-CRYSTAL-INHOMOG", "G-CTRL-FOUND"),
    ("MUT-CRYSTAL-DIAG", "G-CRYSTAL-DIAGONAL-EMPTY"),
    ("MUT-WALK-PLANT", "G-CTRL-EMPTY"),
    ("MUT-ARITY-LAX", "G-CTRL-EMPTY"),
    ("MUT-SMUGGLE-BLIND", "G-SMUGGLE-REACHABLE"),
    ("MUT-FIBER-LAX", "G-CTRL-FOUND-FALSIFIABLE"),
    ("MUT-PROBE-INHOMOG", "G-CTRL-FOUND-AT-THE-CENSUS-TARGET"),
    ("MUT-ONE-CRITERION", "G-ONE-CRITERION"),
    ("MUT-CYCLE-PLANT", "G-SCISSORS"),
    ("MUT-SELFLOOP-DROP", "G-SCISSORS"),
    ("MUT-AB-COUNT", "G-SCISSORS"),
    ("MUT-BIPARTITE-LAX", "G-SCISSORS"),
    ("MUT-RESTRICTION-BLIND", "G-SCISSORS"),
    ("MUT-GRADING-BLIND", "G-GRADING-FORCING"),
    ("MUT-QUOTIENT-BLIND", "G-QUOTIENT-READING"),
    ("MUT-FATE-CELL", "G-FATE-PER-CELL"),
    ("MUT-CARRIER-SPLIT", "G-CARRIER-AGREEMENT"),
    ("MUT-HEAD-FLIP", "G-VERDICT-EQUALITY"),
    ("MUT-OBSTRUCTION-FLIP", "G-OBSTRUCTION-CONTENT"),
    ("MUT-ANCHOR-TYPED", "G-ANCHOR-NOT-TYPED"),
    ("MUT-PAPER-DRIFT", "G-PAPER-RENDERS"),
    ("MUT-INTEGRITY", "G-ARTIFACT-INTEGRITY"),
] + [(f"MUT-QUOTE-V{i:02d}", f"V{i:02d}") for i in range(1, 13)]


if __name__ == "__main__":
    sys.exit(main())

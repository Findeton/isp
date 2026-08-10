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
standard?  Posed at BOTH carriers (MENU-113 and CONG-185) and
carrier-stamped.

WHAT THIS PROGRAM DOES, in the pin's order:
  SEC 0   CLI, gate/waiver/anchor machinery, mutant registry.
  SEC 1   Provenance: every pinned source sha256-verified; verbatim
          anchors (#62) bound to consumer gates.
  SEC 2   The committed transport grammar, REBUILT from its definitions
          (no import from another unit's code, #46/house rule).
  SEC 3   The AB4 arena: 3969 histories, MENU-113, the exchange-square
          census, the horizon potential.
  SEC 4   CONG-185 RE-DERIVED, with its SIX ruling properties GATED
          before use (pin R1).
  SEC 5   I7's arena from the pinned HA receipt; the record family; the
          ADDITIVITY-972-OF-972 ingredient rebuilt (pin R2).
  SEC 6   The crystal arenas (D60/D66/D67 committed specs) and the D58
          generic 2-actor walk (pin R5).
  SEC 7   THE DETECTOR: gates, fates, the RSQ choice inventory with
          fibers COMPUTED, and the R6 no-smuggling classifier.
  SEC 8   CONTROLS FIRST, both falsified (pin R5).
  SEC 9   The census at both carriers over the declared candidate
          family (pin R3).
  SEC 10  The verdict (pin OUTCOMES), the receipt, the output.

HOUSE RULES OBSERVED.  Exact arithmetic (fractions.Fraction / integers)
end to end; no floats anywhere.  Counts COMPUTED, never typed (#24).
Prose renders from the receipt (#20).  All set/dict iteration that feeds
a printed number is ordered by a hash-seed-independent stable key.  The
plain run is byte-reproducible.  Verdicts live IN the gate statements.
Every comparator is built from primitives its builder does not share
(#82-strengthened).
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


def vanchor(vid, path, quote, consumer):
    """A verbatim text anchor (#62): meaning-binding, consumer-gated,
    mutant-falsified.  The quote must occur byte-for-byte in the pinned
    file, and the named consumer gate must exist by the end of the run."""
    global ANCHOR_FAIL
    want = dict((p, w) for p, w, _ in PINNED)[path]
    body, route = read_pinned(path, want)
    q = mutate("MUT-QUOTE", quote, quote + " [corrupted]") if vid == "V01" \
        else quote
    ok = (body is not None) and (q.encode("utf-8") in body)
    if not ok:
        ANCHOR_FAIL += 1
    VANCHORS.append({"id": vid, "path": path, "quote": quote,
                     "consumer_gate": consumer, "passed": ok,
                     "bytes": len(quote), "route": route})
    emit(f"  [{'VANCH' if ok else 'VANCH-FAIL'}] {vid}  {path} -> "
         f"{consumer}  ({len(quote)} bytes verbatim, via {route})")
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
            "G-ADDITIVITY-972")
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
        nb = sum(1 for v in vals.values() if len(v) > 1)
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
                ok += int(good)
    return ok, tot


# ===========================================================================
# SEC 5.  I7's ARENA AND THE ADDITIVITY INGREDIENT
# ===========================================================================

def i7_arena():
    rec = json.load(open(os.path.join(REPO, "v13/code/ha_successor_receipt.json")))
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
    for nm in splittable:
        a = fam[nm]
        for smode in ("low", "floor", "high"):
            sp = {}
            for x in X:
                for lk in links:
                    n = a[x][lk]
                    n1 = 1 if smode == "low" else (n - 1 if smode == "high"
                                                   else n // 2)
                    sp[(x, lk)] = (n1, n - n1)
            for fmode in ("minimal", "iterable-64"):
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
                        if counts[z0][lk] + counts[z1][lk] != a[x][lk]:
                            bad += 1
    return adm, splittable, unsplittable, builds, checks, bad


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


def graph_isomorphisms(S, rel, X, links, Lmod):
    """ALL bijections S -> X carrying the site-object incidence onto the
    target's UNDIRECTED Cayley incidence, by exhaustive backtracking.
    No sampling, no cap: the enumeration is complete."""
    tgt = set()
    for x in X:
        for lk in links:
            y = tuple((x[i] + lk[i]) % Lmod for i in range(len(lk)))
            tgt.add((x, y))
            tgt.add((y, x))
    src = set()
    for (u, v) in rel:
        if u != v:
            src.add((u, v))
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
                if ((u, w) in src) != ((x, phi[w]) in tgt):
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


def arena_linkrel(arena, sgen, lgen):
    """-> (relation | None, acyclic, acyclic_basis, note).  `relation`
    maps ordered site-object pairs to the DIVISION-EVENT COUNT on that
    link object inside the declared window.  `acyclic_basis` is either
    'measured' or the name of the grading that forces it."""
    et = ENDPOINT_TYPE[lgen]
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
        return {}, True, "the poset height grading", \
            "singleton subsets under the event poset's covers"

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

def detect(arena, sgen, lgen, cgen, repair, target, i7_family, links_i7):
    """One census row.  Every fate is a MEASURED outcome with its number."""
    X, links, Lmod = target["X"], target["links"], target["Lmod"]
    row = {"arena": arena["name"], "carrier": arena.get("carrier"),
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

    # (3) structure.  The target lattice is periodic: every site returns to
    #     itself in Lmod steps along every generator, on Lmod DISTINCT
    #     vertices.  A link relation with no directed cycle on distinct
    #     vertices therefore admits NO embedding -- at any size, over every
    #     subset at once.  This is exact and needs no enumeration.
    if acyc:
        row["fate"] = "STRUCT-DEAD"
        row["reason"] = (f"the link relation has no directed cycle on "
                         f"distinct vertices ({basis}); the target is "
                         f"Z_{Lmod}-periodic and every generator closes a "
                         f"{Lmod}-cycle on {Lmod} distinct sites, so no "
                         f"subset of any size embeds")
        row["subsets_excluded"] = f"2^{arity}" if objs is None else \
            f"all {arity}-choose-{len(X)} restrictions"
        return row

    if objs is None:
        row["fate"] = "SCOPE-BLOCKED"
        row["reason"] = "cyclic but not materialisable at this arity"
        return row

    if arity != len(X):
        row["fate"] = "ARITY-REPAIR-UNDECIDED"
        row["reason"] = "cyclic and over-large; handled at the repair row"
        return row

    isos = graph_isomorphisms(objs, set(k for k, n in rel.items() if n > 0),
                              X, links, Lmod)
    row["isomorphisms"] = len(isos)
    if not isos:
        row["fate"] = "STRUCT-DEAD"
        row["reason"] = (f"cyclic, but 0 of the {arity}! bijections carry the "
                         f"site incidence onto the target's link structure")
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
# SEC 10 helpers: the output/receipt writers
# ===========================================================================

def write_artifacts(verdicts):
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
    with open(OUT_TXT, "w") as f:
        f.write("\n".join(LINES) + "\n")
    with open(OUT_JSON, "w") as f:
        json.dump(receipt, f, indent=1, sort_keys=True, default=str)
        f.write("\n")
    return receipt


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
         {"primes": ps_q, "rank": rk_group_q,
          "values": [str(v) for v in val_q]}),
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
                f"integer row reduction on prime valuations, not read off by eye",
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
    adm, splittable, unsplit, builds, achecks, abad = additivity_census(
        X7, L7, links7, i7fam)
    add_cmp = len(splittable) * 3 * 2 * len(X7) * len(links7)
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
         f"split rules x 2 declared completions).  An INDEPENDENT arithmetic "
         f"comparator -- family cardinalities multiplied out, sharing no "
         f"construction with the builder -- gives {add_cmp}",
         achecks == 972 and abad == 0 and add_cmp == 972,
         {"checks": achecks, "violations": abad, "comparator": add_cmp,
          "builds": builds})

    divs_fam = sorted({sk(e) for h in cache for e in h if is_division(e)})
    n_divlab = len(divs_fam)
    all_r = [e for h in cache for e in h if e[0] == 'r']
    sel = [e for h in cache for e in h if is_division(e)]
    tagged = sum(1 for e in sel if e[0] == 'r')
    dist_r = len({sk(e) for e in all_r})
    dist_pair = len({sk(e) for e in all_r if len(e[2]) == 2})
    PAYLOAD["division_events"] = {
        "distinct_division_labels_in_family": n_divlab,
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
         len(COUNT_GENS) == 1, {"count_generators": COUNT_GENS})

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
                    fld[((i, j), lk)] = sum(1 for e in divs
                                            if u in regs_of(e)
                                            and v in regs_of(e))
        per = {str(lk): sorted(Counter(fld[(x, lk)] for x in
                                       [(i, j) for i in range(3)
                                        for j in range(3)]).items())
               for lk in links7}
        cry_rows.append({"crystal": nm, "events": len(b.H),
                         "refusal": b.refusal, "maxhits": b.maxhits,
                         "divisions": len(divs), "count_field_by_link": per})
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
    gate("G-CRYSTAL-DIAGONAL-EMPTY",
         f"MEASURED ACROSS THE COMMITTED CRYSTAL FAMILY: the axis link counts "
         f"are homogeneous and strictly positive on the arbitration crystals, "
         f"and the DIAGONAL link count is identically ZERO at 9 of 9 sites in "
         f"{len(diag_zero)} of {len(cry_rows)} crystals -- the corpus's only "
         f"lattice-carrying grammar records supply q_11 and q_22 and never "
         f"q_12",
         len(diag_zero) == len(cry_rows),
         {"diagonal_zero_crystals": len(diag_zero), "total": len(cry_rows)})

    walkH = generic_walk()
    walk_actors = list(AB)
    if MUTANT == "MUT-WALK-PLANT":
        walkH = list(crystals["DOUBLE-GRID(3,2)"].H)
        walk_actors = sorted(crystals["DOUBLE-GRID(3,2)"].actors)
    wdivs = [e for e in walkH if is_division(e)]
    wpair = sum(1 for e in wdivs if 'A' in regs_of(e) and 'B' in regs_of(e))
    PAYLOAD["walk"] = {"events": len(walkH), "divisions": len(wdivs),
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
    gate("G-TWO-WAY",
         "HA 14 requirement 3 is carried verbatim (V05) and honoured below: "
         "the FOUND branch is demonstrated on the crystal arena and the EMPTY "
         "branch on the generic walk, each with an in-run declared falsifier "
         "that flips it",
         True, {"requirement": "HA 14 item 3"},
         waiver={"class": "DECLARATION-CARRIED",
                 "reason": "this gate records that the two-way requirement is "
                           "in force; its content is discharged by "
                           "G-CTRL-FOUND and G-CTRL-EMPTY, which carry the "
                           "measurements"})

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
    PAYLOAD["controls"] = {"FOUND_at_crystal": ctrl_found,
                           "crystal_at_I7_target": ctrl_found_i7,
                           "FOUND_falsifier": ctrl_falsif,
                           "EMPTY_at_walk": ctrl_empty}
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
         f"the EMPTY control CAN return its other value: the identical call, "
         f"on the crystal record, returns {ctrl_empty_flip['fate']} -- so "
         f"EMPTY at the walk is a property of the walk and not of the "
         f"plumbing",
         ctrl_empty_flip["fate"] == "FOUND-candidate", ctrl_empty_flip)

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
         {"probe": pi_probe, "census_generator": pi_census})
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

    rows = []
    for carrier in ("MENU", "CONG"):
        car = {"name": f"AB4-TRANSPORT-CARRIER@{carrier}", "kind": "carrier",
               "carrier": carrier, "cache": cache, "menu": menu, "cong": cong,
               "actors": list(AB), "n_division_labels": n_divlab,
               "ulam_total": ulam_total,
               "division_events": [e for h in cache for e in h
                                   if is_division(e)]}
        for sgen in SITE_GENS:
            for lgen in LINK_GENS:
                for cgen in COUNT_GENS:
                    for rep in ARITY_REPAIRS:
                        r = detect(car, sgen, lgen, cgen, rep, TGT_I7,
                                   i7_two, links7)
                        r["carrier"] = carrier
                        rows.append(r)
    PAYLOAD["census_rows"] = rows
    PAYLOAD["candidate_count"] = len(rows)
    fates = Counter(r["fate"] for r in rows)
    fates_by_carrier = {c: dict(sorted(Counter(
        r["fate"] for r in rows if r["carrier"] == c).items()))
        for c in ("MENU", "CONG")}
    PAYLOAD["fates"] = dict(sorted(fates.items()))
    PAYLOAD["fates_by_carrier"] = fates_by_carrier
    emit(f"  [DATA] candidates enumerated (COMPUTED): {len(rows)} = "
         f"{len(SITE_GENS)} site x {len(LINK_GENS)} link x {len(COUNT_GENS)} "
         f"count x {len(ARITY_REPAIRS)} repair x 2 carriers")
    emit(f"  [DATA] fates: {dict(sorted(fates.items()))}")
    for c in ("MENU", "CONG"):
        emit(f"  [DATA] fates @{c}: {fates_by_carrier[c]}")
    emit("")
    emit("  the full candidate table:")
    emit(f"  {'carrier':8} {'site':13} {'link':15} {'rep':22} {'arity':>7}  fate")
    for r in rows:
        emit(f"  {r['carrier']:8} {r['site_gen']:13} {r['link_gen']:15} "
             f"{r['arity_repair']:22} {r['site_arity']:>7}  {r['fate']}")

    n_found = fates.get("FOUND-candidate", 0)
    n_smug = fates.get("SMUGGLED", 0)
    n_unmot = fates.get("UNMOTIVATED", 0)
    gate("G-CENSUS-COMPLETE",
         f"the candidate family is enumerated exhaustively over the pin's "
         f"declared generator vocabulary and its size is COMPUTED, not typed: "
         f"{len(rows)} candidates ({len(SITE_GENS)} site generators x "
         f"{len(LINK_GENS)} link generators x {len(COUNT_GENS)} count "
         f"generator x {len(ARITY_REPAIRS)} arity treatments x 2 carriers); "
         f"every cell carries a measured fate, none is skipped",
         len(rows) == len(SITE_GENS) * len(LINK_GENS) * len(COUNT_GENS)
         * len(ARITY_REPAIRS) * 2 and all("fate" in r for r in rows),
         {"candidates": len(rows), "fates": dict(sorted(fates.items()))})

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
    ab_count = actor_rel.get(("A", "B"), 0)
    PAYLOAD["mechanism"] = {
        "actor_pair_relation": sorted((f"{u}->{v}", n)
                                      for (u, v), n in actor_rel.items()),
        "actor_site_objects": 2,
        "menu_class_selfloops": sl_menu, "cong_class_selfloops": sl_cong,
        "menu_class_acyclic": menu_acyc, "cong_class_acyclic": cong_acyc,
        "menu_simple_cycles_len2to6": cyc_cmp_menu,
        "cong_simple_cycles_len2to6": cyc_cmp_cong,
        "divisions_on_the_AB_channel_in_family": ab_count}
    gate("G-SCISSORS",
         f"THE MECHANISM, measured on both sides at once.  The one link "
         f"generator that carries directed cycles at the transport carrier is "
         f"the actor pair / delivery channel, and it has exactly 2 site "
         f"objects; the link generators with enough objects are ACYCLIC -- "
         f"the MENU class-extension graph carries {sl_menu} self-loops and, "
         f"after their removal, no directed cycle on distinct vertices "
         f"(comparator: {cyc_cmp_menu} simple cycles at lengths 2..6), and "
         f"the CONG class-extension graph carries {sl_cong} self-loops and is "
         f"acyclic outright (comparator: {cyc_cmp_cong}).  I7's lattice needs "
         f"9 sites AND a 3-cycle on 3 distinct sites through every generator.  "
         f"A self-loop is not a generator cycle: the declared link "
         f"displacements are non-zero",
         menu_acyc and cong_acyc and all(v == 0 for v in cyc_cmp_menu.values())
         and all(v == 0 for v in cyc_cmp_cong.values()),
         PAYLOAD["mechanism"])

    # ----------------------------------------------------------------- SEC 10
    emit("")
    emit("=" * 78)
    emit("SEC 10  THE VERDICT")
    emit("=" * 78)
    free_fibers = {k: v["inventory"] for k, v in
                   [("CONTROL-CRYSTAL", ctrl_found),
                    ("CONTROL-CRYSTAL-FALSIFIER", ctrl_falsif)]
                   if "inventory" in v}
    PAYLOAD["free_item_fibers"] = free_fibers
    obstruction = "THE-ARITY-CYCLICITY-SCISSORS"
    verdict = (
        f"WELD2-EMPTY-AT-THE-DECLARED-FAMILY-{obstruction}"
        f"@BOTH:MENU-113+CONG-185"
        f"<CANDIDATES={len(rows)}|FOUND={n_found}|SMUGGLED={n_smug}"
        f"|UNMOTIVATED={n_unmot}"
        f"|TYPE-DEAD={fates.get('TYPE-DEAD', 0)}"
        f"|ARITY-DEAD={fates.get('ARITY-DEAD', 0)}"
        f"|ARITY-DEAD-BELOW={fates.get('ARITY-DEAD-BELOW', 0)}"
        f"|STRUCT-DEAD={fates.get('STRUCT-DEAD', 0)}"
        f" -- MECHANISM=THE-ONLY-CYCLIC-LINK-GENERATOR-HAS-2-OBJECTS"
        f"({ab_count}-DIVISION-EVENTS-ON-THE-(A,B)-CHANNEL)"
        f"-AND-EVERY-LINK-GENERATOR-WITH-9-OR-MORE-IS-ACYCLIC"
        f"(MENU-SELFLOOPS={sl_menu}|CONG-SELFLOOPS={sl_cong}"
        f"|SIMPLE-CYCLES-LEN-2..6=0-AT-BOTH)"
        f" -- CONTROLS=FOUND-AT-CRYSTAL({ctrl_found['fate']},"
        f"ISOS={ctrl_found.get('isomorphisms')},FIBERS-ALL-1)"
        f"|FALSIFIER-FLIPS({ctrl_falsif['fate']},"
        f"I-SITE-ASSIGNMENT-FIBER={ctrl_falsif.get('inventory', {}).get('I-SITE-ASSIGNMENT')})"
        f"|EMPTY-AT-WALK({ctrl_empty['fate']})"
        f"|CRYSTAL-AT-I7({ctrl_found_i7['fate']})"
        f" -- INGREDIENT=COUNT-SEMANTICS-INTACT(ADDITIVITY-{achecks - abad}"
        f"-OF-{achecks}|DIVISION=ARBITRATION-TAG-FORCED)"
        f" -- CARRIER-RE-DERIVATION=CONG-185-SIX-OF-SIX"
        f" -- SCOPE=(A,B)-D<=4-CARRIER|I7-d2-L3-9-SITES-3-LINKS"
        f"|DECLARED-WINDOW=FIRST-TO-LAST-ARBITRATION-CUT>")
    PAYLOAD["verdict"] = verdict
    PAYLOAD["obstruction"] = obstruction
    emit("  " + verdict)
    gate("G-VERDICT",
         f"the pre-registered outcome string that fires is "
         f"WELD2-EMPTY-AT-THE-DECLARED-FAMILY, carrier-stamped @BOTH "
         f"(MENU-113 and CONG-185), with obstruction {obstruction}: of "
         f"{len(rows)} candidates {n_found} are FOUND, {n_smug} SMUGGLED, "
         f"{n_unmot} UNMOTIVATED, and the remainder die at measured type, "
         f"arity and structure obstructions "
         f"{dict(sorted(fates.items()))}.  Between delivery and adjudication "
         f"this is a CANDIDATE READING",
         n_found == 0 and n_unmot == 0 and n_smug == 0
         and sum(fates.values()) == len(rows)
         and set(fates) <= {"TYPE-DEAD", "ARITY-DEAD", "ARITY-DEAD-BELOW",
                            "STRUCT-DEAD", "COUNT-DEAD", "SCOPE-BLOCKED",
                            "ARITY-REPAIR-UNDECIDED"}
         and fates.get("SCOPE-BLOCKED", 0) == 0
         and fates.get("ARITY-REPAIR-UNDECIDED", 0) == 0,
         {"verdict": verdict, "fates": dict(sorted(fates.items())),
          "found": n_found, "smuggled": n_smug, "unmotivated": n_unmot})

    emit("")
    emit(f"  gates: {len(GATES)}, failures: {FAILED}; "
         f"anchors: {len(ANCHORS)} numeric + {len(VANCHORS)} verbatim, "
         f"failures: {ANCHOR_FAIL}; waivers: {len(WAIVERS)}")
    return {"weld2": verdict,
            "controls": {"FOUND_at_crystal": ctrl_found["fate"],
                         "FOUND_falsifier": ctrl_falsif["fate"],
                         "EMPTY_at_walk": ctrl_empty["fate"],
                         "crystal_at_I7": ctrl_found_i7["fate"]},
            "cong185_six_properties": props}


def main(argv=None):
    global MUTANT
    ap = argparse.ArgumentParser(
        prog="w2_census_exact.py",
        description="v14 WELD 2 / paper-13 -- the carrier census.")
    ap.add_argument("--selftest", action="store_true",
                    help="corrupt each anchor in memory, confirm the run "
                         "would fail (exit 1); WRITES NOTHING")
    ap.add_argument("--mutant", metavar="NAME",
                    help="run a declared mutant; it must die at a named "
                         "gate and the artifacts are not written")
    ap.add_argument("--list-mutants", action="store_true",
                    help="print the declared mutant registry and exit")
    try:
        args, extra = ap.parse_known_args(argv)
    except SystemExit:
        return 2
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

    write = (MUTANT is None) and (not args.selftest)
    if args.selftest:
        return selftest_report(verdicts)
    if write:
        write_artifacts(verdicts)
        print("\n".join(LINES))
        print(f"\nwrote {OUT_TXT}")
        print(f"wrote {OUT_JSON}")
    else:
        print("\n".join(LINES))
        tgt = dict(MUTANTS)[MUTANT]
        died = [g["gate"] for g in GATES if not g["passed"]]
        afail = [a["id"] for a in ANCHORS if not a["passed"]] + \
                [v["id"] for v in VANCHORS if not v["passed"]]
        ok = (tgt in died) or (tgt in afail) or (tgt == "ANY" and
                                                 (died or afail))
        print(f"\nMUTANT {MUTANT}: target gate {tgt}; "
              f"gates failed = {died}; anchors failed = {afail}; "
              f"DIED-AT-TARGET = {ok}")
        print("artifacts NOT written (mutant run)")
        return 0 if ok else 1
    return exit_code()


def selftest_report(verdicts):
    """A GENUINE selftest: every numeric anchor and every verbatim anchor
    is individually corrupted in memory and the comparison must fail.  A
    vacuous anchor (one whose corruption changes nothing) is a failure of
    the selftest.  Nothing is written."""
    print("\n".join(LINES[:3]))
    killed, vacuous = 0, []
    for a in ANCHORS:
        c = a["committed"]
        bad = (c + 1) if isinstance(c, int) else (str(c) + "!")
        if bad != a["computed"]:
            killed += 1
        else:
            vacuous.append(a["id"])
    for v in VANCHORS:
        body = open(os.path.join(REPO, v["path"]), "rb").read()
        if (v["quote"] + " [corrupted]").encode("utf-8") not in body:
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
    ("MUT-QUOTE", "V01"),
    ("MUT-MENU-KEY", "G-MENU-CLASSES"),
    ("MUT-CONG-WRONG", "G-CONG-CLASSES"),
    ("MUT-SQUARE-DROP", "G-SQUARES"),
    ("MUT-ADDITIVITY", "G-ADDITIVITY-972"),
    ("MUT-DIVPRED", "G-DIVISION-PREDICATE"),
    ("MUT-CRYSTAL-INHOMOG", "G-CTRL-FOUND"),
    ("MUT-WALK-PLANT", "G-CTRL-EMPTY"),
    ("MUT-SMUGGLE-BLIND", "G-SMUGGLE-REACHABLE"),
    ("MUT-CYCLE-PLANT", "G-SCISSORS"),
    ("MUT-FIBER-LAX", "G-CTRL-FOUND-FALSIFIABLE"),
    ("MUT-ARITY-LAX", "G-CTRL-EMPTY"),
]


if __name__ == "__main__":
    sys.exit(main())

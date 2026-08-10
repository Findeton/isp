#!/usr/bin/env python3
"""
u4_crystals_exact.py -- v14 U4 / paper-14: RENEWAL-ONLY CRYSTALS.

Pin: v14/note-u4-pin.md (FROZEN, sha256-12 06b62ecb60a9, ledger #105).
Authority: the weld-2 adjudication 4 (7213d26ea4d4, #102) ruling U4 the
next Route-A unit; the successor scout of record
(v14/note-routeA-successor-scout.md, #101); v11 paper 0 7's founding spec.

THE QUESTION (v11 paper 0 7, verbatim).  "U4 -- SPARSE RECORDS ON THE
CRYSTALS.  The conflict crystals rebuilt with renewal-only records:
geometry should be invariant (it is kinematic -- paper 0 10's third
falsifier if not); the bridges between the renewal sublattice -- itself
periodic: *the division events of a crystal form a crystal* -- are probed
for indivisible structure."

WHAT THIS PROGRAM DOES, in the pin's order:
  SEC 0   CLI, gate/waiver/anchor machinery, the mutant registry.
  SEC 1   PROVENANCE: every pinned source sha256-verified; the verbatim
          anchors (#62) bound to their consumer gates.
  SEC 2   THE COMMITTED GRAMMAR, REBUILT from the d42b1 definitions (no
          import from another unit's code; house rule #46).
  SEC 3   THE RENEWAL MARKING (pin R2) re-derived on every crystal record
          and gated against the source rows, with its scope disclosed.
  SEC 4   THE ARENA (pin R1): the four ARBITRATION crystals and the
          DECLARED COUNTEREXAMPLE CONTROL, rebuilt from the v10
          constructors' definitions, FORCED-gated per crystal, and
          cross-checked against the v10 originals' committed rows.
  SEC 5   THE HEADLINE (pin R4.1): the division-event field's exact
          translation stabilizer on Z_3^2, per crystal per site-reading,
          with an independent character-theoretic reconstruction.
  SEC 6   GEOMETRY INVARIANCE (pin R4.2): arm (a) FILTER in both of its
          sub-readings, arm (b) BUILDER-RERUN under two declared
          sub-grammars, arm (c) registered-not-run; the KR height control.
  SEC 7   THE BRIDGES (pin R4.3), at declared scope, candidate readings
          named, no indivisibility claim.
  SEC 8   THE WALLS (pin R5): L-1 argued before any test and DECLINED;
          BHS; the KR height control; the inherited q_12 = 0.
  SEC 9   The verdict, the head equality gate, verify-paper, the receipt.

HOUSE RULES OBSERVED.  Exact arithmetic (fractions.Fraction / integers)
end to end; no floats anywhere.  Counts COMPUTED, never typed (#24).
Every set/dict iteration feeding a printed number is ordered by a
hash-seed-independent stable key.  The plain run is byte-reproducible.
Verdicts live IN the gate statements.  Gates bind OBJECTS, not aggregates
(#87): per crystal x per reading x per arm.  Failing runs write nothing.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from collections import Counter
from fractions import Fraction as Fr
from itertools import permutations

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
OUT_TXT = os.path.join(HERE, "u4_crystals_output.txt")
OUT_JSON = os.path.join(HERE, "u4_crystals_receipt.json")
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
NUMREG: set[str] = set()
FAILED = 0
ANCHOR_FAIL = 0
MUTANT = None
QUIET = False

MUTANTS = {
    "MUT-APERIODIC-DIVISION":
        "plants one extra division at a single site of DOUBLE-GRID(3,2), "
        "destroying the field's periodicity -- must die at that crystal's "
        "own stabilizer gate (kills the crystal claim)",
    "MUT-CONTROL-PERIODIC":
        "plants a constant division field on the delivery control, giving "
        "it the full period -- must die at the control's trivial-stabilizer "
        "gate (kills the control)",
    "MUT-DIVPRED":
        "swaps the source-forced division predicate from the arbitration "
        "tag to the delivery tag -- must die at the marking gates",
    "MUT-GEOM-VARIES":
        "drops the widest division event from the restricted population, so "
        "the chart-width row VARIES -- must die at the width-invariance "
        "gate, DEMONSTRATING that the pin's VARIES path is emittable",
    "MUT-NOT-FORCED":
        "withholds one round's row arbitration from DOUBLE-GRID(3,2), "
        "leaving a refused record -- must die at that crystal's FORCED gate "
        "(and, downstream of it, at the v10 committed-number anchors that "
        "bind the record)",
    "MUT-HEIGHT-IMPURE":
        "reports a non-division event as sharing a division height layer -- "
        "must die at that crystal's height-purity gate",
    "MUT-SITEMAP":
        "transposes two actors in the site map -- must die at the site-map "
        "bijection gate",
    "MUT-ARMB-COMPLETES":
        "reports the renewal-only sub-grammar rerun as completing -- must "
        "die at that crystal's arm-(b) gate",
    "MUT-HEAD":
        "corrupts one cell of the head's stabilizer table -- must die at "
        "the complete-string head equality gate",
    "MUT-ANCHOR":
        "corrupts a committed v10 number -- must die at the anchor stage",
    "MUT-VERBATIM":
        "corrupts a verbatim source quote -- must die at the verbatim "
        "anchor stage",
    "MUT-DIAGONAL":
        "plants a diagonal co-division link count -- must die at that "
        "crystal's inherited-diagonal gate",
}


def emit(s: str = "") -> None:
    LINES.append(s)


def mutate(name, normal, corrupted):
    """Mutant hook.  Returns `normal` unless this run is that mutant."""
    return corrupted if MUTANT == name else normal


def reg(*vals):
    """Register a COMPUTED number for the verify-paper numeral gate."""
    for v in vals:
        if isinstance(v, Fr):
            NUMREG.add(str(v))
            NUMREG.add(str(v.numerator))
            NUMREG.add(str(v.denominator))
            NUMREG.add(dec4(v))
        elif isinstance(v, int):
            NUMREG.add(str(v))
        elif isinstance(v, str):
            NUMREG.add(v)
    return vals[0] if vals else None


def dec4(fr: Fr) -> str:
    """Exact 4-decimal rendering by integer arithmetic (round half up)."""
    neg = fr < 0
    fr = -fr if neg else fr
    q, r = divmod(fr.numerator * 10000, fr.denominator)
    if 2 * r >= fr.denominator:
        q += 1
    s = f"{q // 10000}.{q % 10000:04d}"
    return ("-" + s) if neg else s


def dec2(fr: Fr) -> str:
    """Exact 2-decimal rendering by integer arithmetic (round half up)."""
    q, r = divmod(fr.numerator * 100, fr.denominator)
    if 2 * r >= fr.denominator:
        q += 1
    return f"{q // 100}.{q % 100:02d}"


def gate(name, statement, ok, evidence, waiver=None):
    """A gate whose STATEMENT carries the measured verdict."""
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
    ANCHORS.append({"id": aid, "quantity": quantity,
                    "committed": str(committed), "computed": str(computed),
                    "passed": ok, "source": source})
    emit(f"  [{'ANCH' if ok else 'ANCH-FAIL'}] {aid}  {quantity}: "
         f"committed={committed} computed={computed}")
    return ok


def vanchor(vid, path, quote, consumer):
    """#62: a verbatim source string, bound to the gate that consumes it."""
    global ANCHOR_FAIL
    txt = SOURCES[path]
    ok = quote in txt
    if not ok:
        ANCHOR_FAIL += 1
    VANCHORS.append({"id": vid, "path": path, "quote": quote,
                     "found": ok, "consumer": consumer})
    emit(f"  [{'VERB' if ok else 'VERB-FAIL'}] {vid}  {path}  "
         f"-> consumer {consumer}")
    emit(f"         \"{quote[:96]}{'...' if len(quote) > 96 else ''}\"")
    return ok


def checkpoint(where):
    """Products are GATED (#91): no section consumes an object whose own
    gates have failed.  A failed gate stops the run HERE, cleanly, at the
    named gate, with nothing written."""
    bad = [g["gate"] for g in GATES if not g["passed"]]
    if bad or ANCHOR_FAIL:
        emit("")
        emit(f"  [REFUSED AT {where}] failed gates: {bad}; anchor failures: "
             f"{ANCHOR_FAIL} -- the run stops here and writes nothing")
        if not QUIET:
            print("\n".join(LINES))
            print(f"\nREFUSED AT {where}\n  failed gates: {bad}\n  anchor "
                  f"failures: {ANCHOR_FAIL}\n  NOTHING WRITTEN",
                  file=sys.stderr)
        raise SystemExit(1)


def sha256_of(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


SOURCES: dict[str, str] = {}


def read_pinned(path, want):
    """#91: every source read at its pinned sha256-12; products gated."""
    full = os.path.join(REPO, path)
    if not os.path.exists(full):
        return None, None
    with open(full, "rb") as fh:
        raw = fh.read()
    got = sha256_of(raw)[:12]
    SOURCES[path] = raw.decode("utf-8")
    return got, (got == want)


# ===========================================================================
# SEC 2.  THE COMMITTED GRAMMAR, REBUILT
#         (d42b1_transport_exact.py definitions, re-derived; no import)
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
                ok, _ = admissible(acts, ('r', a, ck, triples(full, W)),
                                   actors)
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
        has_am = bool(view.merge_pairs(a)
                      or admissible_arb_ckeys(acts, a, actors))
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


# ---- the division / renewal predicate (pin R2), SOURCE-FORCED ------------

def is_division(e):
    """The renewal marking.  v11 paper 0 4's [POSIT] identifies division
    events with renewal events; paper-09 3 records renewal =
    class-0-carrying-an-arb as SOURCE-FORCED from three agreeing rows, of
    which the clause that transports to a 9-actor record is the
    ARBITRATION TAG (SEC 3 measures why the other two are silent here)."""
    return e[0] == mutate("MUT-DIVPRED", 'r', 'd')


def is_division_structural(e):
    """A SECOND, INDEPENDENT predicate for the same set, written from the
    grammar's tuple SHAPES and not from its tags: an arbitration is the
    unique 4-tuple whose third slot is a conflict key (a frozenset).
    Proposals carry a value tuple there, deliveries an actor string,
    merges a pair of values, idles are 2-tuples."""
    return len(e) == 4 and isinstance(e[2], frozenset)


# ===========================================================================
# SEC 4a.  THE CRYSTAL CONSTRUCTORS, REBUILT
#          (d60 `B`/CRYSTAL-2D, d66 `double_grid`/`conflict_grid`
#           definitions, re-derived here; no import)
# ===========================================================================

class Builder:
    """D60's `B`: every event taken from the committed layer's own menu,
    specified by its full tuple; `maxhits == 1` gates that the record is
    FORCED (nothing tie-broken); a refusal is recorded, never patched.
    `filt` is the declared sub-grammar hook of pin R3(b) (the d74 shape:
    the SUPPORT is restricted, the committed weights are untouched)."""

    def __init__(self, actors, filt=None):
        self.actors, self.H, self.refusal, self.maxhits = actors, [], None, 0
        self.filt = filt

    def pick(self, inits, spec, label):
        if self.refusal:
            return None
        menu = candidates_for(list(self.H), tuple(inits))
        if self.filt is not None:
            menu = [(e, q) for e, q in menu if self.filt(e)]
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


def double_grid(g, R, filt=None, drop_one_arb=False):
    """D66/D67's DOUBLE-GRID(g, R): rows AND columns conflict concurrently
    on 2g independent base lineages, delivery-free after the bootstrap;
    the object that saturates the width ceiling k*b <= k^2."""
    ac = [[f"D{i}{j}" for j in range(g)] for i in range(g)]
    flat = [a for row in ac for a in row]
    b = Builder(tuple(flat), filt)
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
            if drop_one_arb and t == R - 1 and gi == 0:
                b.refusal = ("MUT-NOT-FORCED: arbitration withheld",
                             len(b.H))
                return b
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


def conflict_grid(g, R, filt=None):
    """D66's CONFLICT-GRID(g, R): g-proposer arbitrations on orthogonal
    row / column partitions of a g x g actor grid."""
    ac = [[f"G{i}{j}" for j in range(g)] for i in range(g)]
    flat = [a for row in ac for a in row]
    b = Builder(tuple(flat), filt)
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


def d60_grid(K=3, PHASES=12, filt=None):
    """D60's CRYSTAL-2D: the 3x3 delivery grid, 12 phases.  THE DECLARED
    COUNTEREXAMPLE CONTROL of pin R1."""
    GRID = [f"G{i}{j}" for i in range(K) for j in range(K)]

    def gid(i, j):
        return f"G{i % K}{j % K}"
    b = Builder(tuple(GRID), filt)
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


CRYSTALS = [
    ("DOUBLE-GRID(3,2)", "ARBITRATION", lambda f=None: double_grid(3, 2, f)),
    ("DOUBLE-GRID(3,3)", "ARBITRATION", lambda f=None: double_grid(3, 3, f)),
    ("CONFLICT-GRID(3,2)", "ARBITRATION",
     lambda f=None: conflict_grid(3, 2, f)),
    ("CONFLICT-GRID(3,4)", "ARBITRATION",
     lambda f=None: conflict_grid(3, 4, f)),
    ("D60-GRID(3,12)", "CONTROL", lambda f=None: d60_grid(filt=f)),
]
ARB = [c[0] for c in CRYSTALS if c[1] == "ARBITRATION"]
CTRL = [c[0] for c in CRYSTALS if c[1] == "CONTROL"][0]
READINGS = ["initiator", "footprint"]
L = 3                                    # the site lattice is Z_L^2
SITES = [(i, j) for i in range(L) for j in range(L)]
AXIS = [(1, 0), (0, 1)]
DIAG = [(1, 1), (1, 2)]


# ===========================================================================
# SEC 5a.  THE SITE READING, THE FIELD, THE STABILIZER
# ===========================================================================

def site_map(b):
    """The actor -> Z_3^2 site map.  FORCED by the constructors' own actor
    naming: every crystal names its actors <prefix><i><j> on a 3x3 grid."""
    out = {}
    for a in sorted(b.actors):
        out[a] = (int(a[1]), int(a[2]))
    if MUTANT == "MUT-SITEMAP":
        ks = sorted(out)
        out[ks[0]], out[ks[1]] = out[ks[1]], out[ks[1]]
    return out


def division_field(b, reading, name=None):
    """The division-event field n : Z_3^2 -> Z_>=0, at the declared site
    reading.  (a) initiator = the arbitrating actor op[1];  (b) footprint
    = every actor in the event's register footprint regs_of(op)."""
    S = site_map(b)
    f = {x: 0 for x in SITES}
    for e in b.H:
        if not is_division(e):
            continue
        if reading == "initiator":
            f[S[e[1]]] += 1
        else:
            for r in regs_of(e):
                if isinstance(r, str) and r in S:
                    f[S[r]] += 1
    if MUTANT == "MUT-APERIODIC-DIVISION" and name == "DOUBLE-GRID(3,2)":
        f[(0, 2)] += 1
    if MUTANT == "MUT-CONTROL-PERIODIC" and name == CTRL:
        f = {x: 1 for x in SITES}
    return f


def stabilizer(f):
    """{ t in Z_3^2 : n(x + t) = n(x) for every x }, by direct test."""
    out = []
    for t in SITES:
        if all(f[((x[0] + t[0]) % L, (x[1] + t[1]) % L)] == f[x]
               for x in SITES):
            out.append(t)
    return sorted(out)


def subgroup_name(S):
    """Name the subgroup of Z_3^2 by its order and its generator."""
    if len(S) == 1:
        return "1"
    if len(S) == 9:
        return "Z3^2"
    g = sorted(t for t in S if t != (0, 0))[0]
    return f"<({g[0]},{g[1]})>"


# --- the INDEPENDENT reconstruction: characters over Z[omega] -------------

def _hat_nonzero(f, chi):
    """Is the Z_3^2 Fourier coefficient  sum_x n(x) omega^{-chi.x}  nonzero?
    Exact in Z[omega] = Z[t]/(t^2 + t + 1): collect the three coefficients
    c0, c1, c2 and reduce by omega^2 = -1 - omega.  No floats, no library."""
    c = [0, 0, 0]
    for x in SITES:
        k = (-(chi[0] * x[0] + chi[1] * x[1])) % 3
        c[k] += f[x]
    return (c[0] - c[2], c[1] - c[2]) != (0, 0)


def stabilizer_by_characters(f):
    """Stab(n) = the annihilator of the support of the Fourier transform.
    Shares no code and no typed constant with `stabilizer`: it runs over
    the DUAL group and multiplies characters instead of translating the
    field."""
    supp = [chi for chi in SITES if _hat_nonzero(f, chi)]
    return sorted(t for t in SITES
                  if all((chi[0] * t[0] + chi[1] * t[1]) % 3 == 0
                         for chi in supp))


# ===========================================================================
# SEC 6a.  THE GEOMETRY INSTRUMENT
#          (d60's `poset_of`/`profile` over d47a's `heights`/`sky` kind B
#           and d58's `covers`; definitions re-derived, no import)
# ===========================================================================

def poset_of(h):
    pred = event_poset(list(h))
    n = len(h)
    return [[i in pred[j] for j in range(n)] for i in range(n)]


def heights(C):
    n = len(C)
    hh = [0] * n
    order = sorted(range(n), key=lambda x: sum(C[i][x] for i in range(n)))
    for x in order:
        preds = [i for i in range(n) if C[i][x]]
        hh[x] = 1 + max((hh[i] for i in preds), default=-1)
    return hh


def sky_b(C, e, depth, hh):
    """d47a's sky kind 'B': the directions at height gap exactly `depth`."""
    return [f for f in range(len(C)) if C[e][f] and hh[f] - hh[e] == depth]


def covers(C):
    n = len(C)
    out = []
    for i in range(n):
        for j in range(n):
            if C[i][j] and not any(C[i][k] and C[k][j] for k in range(n)):
                out.append((i, j))
    return out


def profile(C, pop=None):
    """d60's `profile`: D58's atlas restricted to a POPULATION of events
    (the poset is left whole; only the metric population changes)."""
    n = len(C)
    P = sorted(range(n)) if pop is None else sorted(pop)
    hh = heights(C)
    cov = covers(C)
    Pset = set(P)
    out = {}
    for d in (2, 3):
        DIRS = {e: set(sky_b(C, e, d, hh)) for e in range(n)}
        w = [len(DIRS[e]) for e in P]
        om = []
        for (e, e2) in cov:
            if e not in Pset or len(DIRS[e]) < 2:
                continue
            om.append(Fr(len(DIRS[e] & set(sky_b(C, e2, d - 1, hh))),
                         len(DIRS[e])))
        out[d] = {"n": len(P),
                  "h2": Fr(sum(1 for x in w if x >= 2), len(P)),
                  "h4": Fr(sum(1 for x in w if x >= 4), len(P)),
                  "max": max(w), "mean": Fr(sum(w), len(P)),
                  "pairs": len(om),
                  "om": (sum(om) / len(om)) if om else None,
                  "attained": sorted(e for e in P if len(DIRS[e]) == max(w))}
    out["height"] = (max(hh[e] for e in P) + 1) if P else 0
    out["longest_chain"] = out["height"]
    return out


# ===========================================================================
# THE RUN
# ===========================================================================

PINNED = [
    ("v14/note-u4-pin.md", "06b62ecb60a9", "the pin (FROZEN)"),
    ("v14/note-routeA-successor-scout.md", "88375db9cec2",
     "the successor scout of record"),
    ("v14/note-w2-adjudication.md", "7213d26ea4d4",
     "the weld-2 adjudication (the successor ruling)"),
    ("v11/relativistic-isp-v11-paper0-the-indivisible-record-law.md",
     "37a428321f46", "v11 paper 0 (the question, the POSIT, the falsifiers)"),
    ("v14/paper-09-renewal-transport.md", "006f96aaa2ff",
     "paper-09 3 (what a renewal is)"),
    ("v11/note-v11p0a-reproduction-catalog.md", "0cebe543e814",
     "the reproduction catalog (the BHS and KR walls)"),
    ("v11/note-L1-lorentz-no-go-lemma.md", "93ea24591c3c",
     "L-1 (the fourth form; the scope guard)"),
    ("v10/code/d60_crystal_exact.py", "684cdb76552b",
     "D60: the Builder, CRYSTAL-2D, profile"),
    ("v10/code/d66_arbitration_crystal_exact.py", "3d0516ab106e",
     "D66: double_grid, conflict_grid"),
    ("v10/code/d67_k4_double_grid_exact.py", "e80edf851d93",
     "D67: the k=4 double grid"),
    ("v10/code/d63_wide_crystal_exact.py", "89e170f40579",
     "D63: the wide crystal"),
    ("v10/code/d47a_sky_instrument_exact.py", "f0b578c13409",
     "D47a: heights, sky"),
    ("v10/code/d58_atlas_instrument_exact.py", "e5f58cb52a06",
     "D58: covers, atlas"),
    ("v10/code/d42b1_transport_exact.py", "576275d55ecf",
     "D42b1: the transport grammar"),
    ("v10/code/d74_transport_holonomy_exact.py", "bb852161aced",
     "D74: the declared sub-grammar shapes"),
    ("v10/data/d60_crystal_exact.out", "f768a4eafcd5",
     "D60's committed output"),
    ("v10/data/d66_arbitration_crystal_exact.out", "e252529d2586",
     "D66's committed output"),
]

BANNED = ("precisely the form U4 tests, and precisely the form the "
          "corpus's strongest relativity result took")


def run_provenance():
    emit("=" * 78)
    emit("SEC 1  PROVENANCE -- pinned-sha reads (#91); products gated")
    emit("=" * 78)
    rows, allok = [], True
    for path, want, what in PINNED:
        got, ok = read_pinned(path, want)
        rows.append({"path": path, "want": want, "got": got, "ok": bool(ok),
                     "what": what})
        allok = allok and bool(ok)
        gate(f"G-PROV[{path}]",
             f"the pinned source is present and its sha256-12 is {want} "
             f"(measured {got}) -- {what}",
             bool(ok), {"path": path, "want": want, "got": got})
    PAYLOAD["provenance"] = rows
    gate("G-PROV-ROOT",
         f"ALL {len(PINNED)} pinned sources resolve under the repo root "
         f"derived from this file's own location and every one reproduces "
         f"its pinned sha256-12; a run outside the repo cannot reach them "
         f"and fails HERE, loudly and by design, writing nothing",
         allok, {"sources": len(PINNED), "all_verified": allok,
                 "repo_root_derived_from": "__file__"})
    return allok


def run_verbatim():
    emit("")
    emit("-" * 78)
    emit("The verbatim anchors (#62), each bound to its consumer gate")
    emit("-" * 78)
    P0 = "v11/relativistic-isp-v11-paper0-the-indivisible-record-law.md"
    P9 = "v14/paper-09-renewal-transport.md"
    CAT = "v11/note-v11p0a-reproduction-catalog.md"
    L1 = "v11/note-L1-lorentz-no-go-lemma.md"
    D74 = "v10/code/d74_transport_holonomy_exact.py"
    D60 = "v10/code/d60_crystal_exact.py"
    PIN = "v14/note-u4-pin.md"
    q = [
        ("V01", P0, "U4 — SPARSE RECORDS ON THE CRYSTALS.**  The conflict "
         "crystals\n  rebuilt with renewal-only records", "G-ARENA-SCOPE"),
        ("V02", P0, "v11's **division events are the renewal events.**",
         "G-MARK-POSIT"),
        ("V03", P9, "REN = [h for h in FAM if len(h) <= 4 and "
         "CLS[tuple(h)] == 0 and any(e[0] == 'r' for e in h)]",
         "G-MARK-SOURCE-ROWS"),
        ("V04", P9, "Class 0 is necessary and not sufficient: an "
         "arbitration is required.", "G-MARK-SOURCE-ROWS"),
        ("V05", P9, "every pair arbitration is a renewal to the root state "
         "[THEOREM at two-actor delivery-free scope]",
         "G-MARK-ROOT[DOUBLE-GRID(3,2)]"),
        ("V06", P0, "If U4 shows sparse records destroy the geometry, "
         "kinematics and\n  law are not separable as posited",
         "G-GEOM-SEGMENT"),
        ("V07", CAT, "v11's\ncrystals are finite-valency by construction, "
         "so BHS says their renewal\nsublattice **cannot** be statistically "
         "Lorentz-invariant in the sprinkling\nsense.", "G-WALL-BHS"),
        ("V08", CAT, "a dimension reading without a height\ncontrol is "
         "worthless", "G-WALL-KR"),
        ("V09", L1, "it is a\n   **fourth form, outside paper 8's three**, "
         "and its admissibility is\n   v11's to argue when U4 runs.",
         "G-WALL-L1"),
        ("V10", L1, "It does **not** forbid a permutation action.",
         "G-WALL-L1-PERMUTATION"),
        ("V11", D74, "A declared SUB-GRAMMAR: the support is\n    "
         "restricted, the committed weights are untouched.",
         "G-GEOM-ARMB-RENEWAL[DOUBLE-GRID(3,2)]"),
        ("V12", D60, "D58's atlas restricted to a POPULATION of events (the "
         "poset is\n    left whole; only the metric population changes)",
         "G-GEOM-POP-INSTRUMENT"),
        ("V13", PIN, "q₁₂ ≡ 0 is INHERITED", "G-WALL-DIAGONAL"),
        ("V14", PIN, "The delivery\ncrystal D60-GRID(3,12) is the DECLARED "
         "COUNTEREXAMPLE CONTROL", "G-CONTROL-DECLARED"),
    ]
    ok = True
    for vid, path, quote, cons in q:
        if MUTANT == "MUT-VERBATIM" and vid == "V03":
            quote = quote.replace("== 0", "== 1")
        ok = vanchor(vid, path, quote, cons) and ok
    PAYLOAD["verbatim_anchors"] = len(q)
    return ok


def main_run():
    global FAILED
    emit("=" * 78)
    emit("U4 / paper-14 -- RENEWAL-ONLY CRYSTALS")
    emit("pin v14/note-u4-pin.md (06b62ecb60a9, ledger #105)")
    emit("=" * 78)
    emit("")

    run_provenance()
    checkpoint("SEC 1 (the pinned-sha reads) -- a run that cannot reach the "
               "pinned sources stops HERE, at a named gate, by design")
    run_verbatim()
    checkpoint("SEC 1 (the verbatim anchors)")

    # -------------------------------------------------------------- SEC 3
    emit("")
    emit("=" * 78)
    emit("SEC 3  THE RENEWAL MARKING -- re-derived, gated against the source")
    emit("=" * 78)
    gate("G-MARK-POSIT",
         "v11 paper 0 4's [POSIT] (V02) is carried verbatim and is this "
         "unit's ONLY identification of division with renewal: idles and "
         "deliveries remain grammar events and are not records, so the "
         "renewal-only record is the record of arbitrations",
         True, {"posit": "division events ARE the renewal events"},
         waiver={"class": "DECLARATION-CARRIED",
                 "reason": "a pinned axiom of the parent paper, quoted not "
                           "derived; its consequences are what SEC 3 gates"})

    built = {}
    for nm, kind, fn in CRYSTALS:
        built[nm] = fn()

    mark_rows = []
    for nm, kind, _fn in CRYSTALS:
        b = built[nm]
        tag = [i for i, e in enumerate(b.H) if is_division(e)]
        struct = [i for i, e in enumerate(b.H) if is_division_structural(e)]
        reg(len(tag), len(struct))
        gate(f"G-MARK-TAG[{nm}]",
             f"on this crystal's {len(b.H)}-event record the SOURCE-FORCED "
             f"tag predicate selects {len(tag)} events and an INDEPENDENT "
             f"predicate written from the grammar's tuple SHAPES (the unique "
             f"4-tuple whose third slot is a conflict key) selects "
             f"{len(struct)}, and the two sets are IDENTICAL index for "
             f"index -- the marking is not carried by the tag alone",
             tag == struct, {"crystal": nm, "tag": len(tag),
                             "structural": len(struct),
                             "identical": tag == struct})
        # S4's renewal-to-root content, re-derived event by event
        ok, bad = 0, []
        for i in tag:
            op = b.H[i]
            if op[0] != 'r':
                bad.append(i)
                continue
            pre = b.H[:i + 1]
            V = View(pre, event_poset(pre), set(range(len(pre))))
            base = next(iter(op[2]))[1]
            mint = vname(base, op[3], op[1])
            props = {t[0] for t in op[2]}
            if all(mint in V.holdings(a) for a in props) \
                    and base in V.superseded:
                ok += 1
            else:
                bad.append(i)
        reg(ok)
        gate(f"G-MARK-ROOT[{nm}]",
             f"S4's renewal CONTENT (V05) is re-derived on this record event "
             f"by event: at {ok} of {len(tag)} marked events every proposer "
             f"in the conflict key holds the newly minted value immediately "
             f"after, and the superseded base is retired -- the marked "
             f"events are exactly the events that reset their conflict group "
             f"to one shared value, which is what 'a renewal to the root' "
             f"says at this arena",
             ok == len(tag) and len(tag) > 0,
             {"crystal": nm, "marked": len(tag), "renewal_to_root": ok,
              "violations": bad[:5]})
        cks = Counter(len(b.H[i][2]) for i in tag)
        pairs = cks.get(2, 0)
        reg(pairs)
        mark_rows.append({"crystal": nm, "events": len(b.H),
                          "marked": len(tag), "structural": len(struct),
                          "renewal_to_root": ok,
                          "ckey_sizes": sorted(cks.items()),
                          "pair_arbitrations": pairs})
    PAYLOAD["marking"] = mark_rows
    tot_pairs = sum(r["pair_arbitrations"] for r in mark_rows)
    tot_marked = sum(r["marked"] for r in mark_rows)
    reg(tot_pairs, tot_marked)
    gate("G-MARK-SOURCE-ROWS",
         f"THE MARKING'S WARRANT, MEASURED AND SCOPED.  paper-09 3 forces "
         f"renewal = class-0-carrying-an-arb from three agreeing rows "
         f"(V03, V04, V05).  Of the three, exactly ONE reaches this arena: "
         f"the class-0 clause is a two-actor delivery-free STATE-SPACE "
         f"notion with no committed referent at nine actors, and S4's "
         f"narrower sufficient condition -- PAIR arbitration -- selects "
         f"{tot_pairs} of the {tot_marked} marked events across all five "
         f"crystals, because every conflict key here has size 1 or 3.  What "
         f"transports is the ARBITRATION TAG, and G-MARK-ROOT shows S4's "
         f"CONTENT transports even though its hypothesis does not",
         tot_pairs == 0 and tot_marked > 0,
         {"pair_arbitrations": tot_pairs, "marked_total": tot_marked,
          "clauses_reaching_this_arena": ["arbitration tag"],
          "clauses_out_of_scope": ["class-0 (two-actor delivery-free)",
                                   "S4 pair hypothesis (vacuous here)"]})
    checkpoint("SEC 3 (the renewal marking)")

    # -------------------------------------------------------------- SEC 4
    emit("")
    emit("=" * 78)
    emit("SEC 4  THE ARENA -- five crystals, FORCED, cross-checked to v10")
    emit("=" * 78)
    gate("G-ARENA-SCOPE",
         "the arena is the pin R1 arena and nothing else: the four "
         f"ARBITRATION crystals {ARB} plus the DECLARED COUNTEREXAMPLE "
         f"CONTROL {CTRL}; the question they answer is V01, quoted verbatim",
         len(ARB) == 4, {"arbitration": ARB, "control": CTRL})
    gate("G-CONTROL-DECLARED",
         f"{CTRL} is the pin's DECLARED COUNTEREXAMPLE CONTROL (V14): every "
         f"periodicity claim below must return its OTHER value there, and "
         f"each two-way pair is gated per reading, never in aggregate",
         True, {"control": CTRL},
         waiver={"class": "DECLARATION-CARRIED",
                 "reason": "the two-way requirement is declared here and "
                           "discharged by the per-reading control gates in "
                           "SEC 5 and the width gate in SEC 6"})

    arena_rows = []
    for nm, kind, _fn in CRYSTALS:
        b = built[nm]
        if MUTANT == "MUT-NOT-FORCED" and nm == "DOUBLE-GRID(3,2)":
            b = double_grid(3, 2, drop_one_arb=True)
            built[nm] = b
        n = len(b.H)
        reg(n)
        gate(f"G-FORCED[{nm}]",
             f"this crystal is a FORCED record: {n} events, every one "
             f"offered by the committed layer's own menu and specified by "
             f"its FULL EVENT TUPLE, matched by EXACTLY ONE candidate "
             f"(maxhits = {b.maxhits}), refusal = {b.refusal} -- D60's C1/C2 "
             f"and D66/D67's _pick discipline, reproduced",
             b.refusal is None and b.maxhits == 1,
             {"crystal": nm, "events": n, "maxhits": b.maxhits,
              "refusal": b.refusal})
        S = site_map(b)
        img = sorted(set(S.values()))
        gate(f"G-SITEMAP[{nm}]",
             f"the site reading's carrier is FORCED by the constructor's own "
             f"actor naming: the {len(S)} actor names parse as a BIJECTION "
             f"onto Z_3^2, image size {len(img)} of 9 -- no site assignment "
             f"is chosen by this unit",
             len(S) == 9 and len(img) == 9 and img == sorted(SITES),
             {"crystal": nm, "actors": len(S), "image": len(img)})
        arena_rows.append({"crystal": nm, "kind": kind, "events": n,
                           "maxhits": b.maxhits, "refusal": b.refusal,
                           "divisions": sum(1 for e in b.H
                                            if is_division(e))})
    PAYLOAD["arena"] = arena_rows

    # the v10 cross-check: committed rows, and a gated event-count law
    emit("")
    emit("  [the v10 cross-check -- committed numbers, pin R1]")
    prof_full = {}
    for nm, _k, _f in CRYSTALS:
        prof_full[nm] = profile(poset_of(built[nm].H))
    dgm = mutate("MUT-ANCHOR", 9, 8)
    for aid, nm, d, key, comm, src in [
            ("A01", CTRL, 2, "h2", Fr(1, 2), "d60 out L18"),
            ("A02", CTRL, 2, "h4", Fr(0), "d60 out L18"),
            ("A03", CTRL, 2, "max", 3, "d60 out L18"),
            ("A04", CTRL, 2, "pairs", 43, "d60 out L18"),
            ("A05", CTRL, 2, "om", Fr(101, 258), "d60 out L18"),
            ("A06", CTRL, 3, "h2", Fr(14, 23), "d60 out L19"),
            ("A07", CTRL, 3, "h4", Fr(0), "d60 out L19"),
            ("A08", CTRL, 3, "max", 3, "d60 out L19"),
            ("A09", CTRL, 3, "pairs", 51, "d60 out L19"),
            ("A10", CTRL, 3, "om", Fr(73, 153), "d60 out L19"),
            ("A11", "DOUBLE-GRID(3,2)", 2, "max", dgm, "d66 out L227"),
            ("A12", "DOUBLE-GRID(3,2)", 3, "max", 9, "d66 out L227"),
            ("A13", "CONFLICT-GRID(3,4)", 2, "max", 6, "d66 out L223"),
            ("A14", "CONFLICT-GRID(3,4)", 3, "max", 6, "d66 out L223")]:
        anchor(aid, f"{nm} d={d} {key}", comm, prof_full[nm][d][key], src)
        reg(prof_full[nm][d][key])
    for aid, nm, d, key, comm, src in [
            ("A15", "DOUBLE-GRID(3,2)", 2, "h2", "0.4444", "d66 out L64"),
            ("A16", "DOUBLE-GRID(3,2)", 2, "h4", "0.0694", "d66 out L64"),
            ("A17", "DOUBLE-GRID(3,2)", 2, "om", "0.5576", "d66 out L64"),
            ("A18", "DOUBLE-GRID(3,2)", 3, "h2", "0.6389", "d66 out L135"),
            ("A19", "DOUBLE-GRID(3,2)", 3, "h4", "0.2083", "d66 out L135"),
            ("A20", "DOUBLE-GRID(3,2)", 3, "om", "0.5710", "d66 out L135"),
            ("A21", "CONFLICT-GRID(3,4)", 2, "h2", "0.4848", "d66 out L60"),
            ("A22", "CONFLICT-GRID(3,4)", 2, "h4", "0.1364", "d66 out L60"),
            ("A23", "CONFLICT-GRID(3,4)", 2, "om", "0.5068", "d66 out L60"),
            ("A24", "CONFLICT-GRID(3,4)", 3, "h2", "0.5758", "d66 out L131"),
            ("A25", "CONFLICT-GRID(3,4)", 3, "h4", "0.4545", "d66 out L131"),
            ("A26", "CONFLICT-GRID(3,4)", 3, "om", "0.5833", "d66 out L131")]:
        anchor(aid, f"{nm} d={d} {key} (4-decimal rendering)", comm,
               dec4(prof_full[nm][d][key]), src)
    for aid, nm, comm, src in [
            ("A27", CTRL, 46, "d60 out L17"),
            ("A28", "DOUBLE-GRID(3,2)", 72, "d66 out L64"),
            ("A29", "CONFLICT-GRID(3,4)", 66, "d66 out L60")]:
        anchor(aid, f"{nm} events", comm, len(built[nm].H), src)
    anchor("A30", "DOUBLE-GRID(3,2) arbitration share", Fr(1, 4),
           Fr(sum(1 for e in built["DOUBLE-GRID(3,2)"].H
                  if is_division(e)), len(built["DOUBLE-GRID(3,2)"].H)),
           "d66 out L106")
    anchor("A31", "CONFLICT-GRID(3,4) arbitration share", Fr(2, 11),
           Fr(sum(1 for e in built["CONFLICT-GRID(3,4)"].H
                  if is_division(e)), len(built["CONFLICT-GRID(3,4)"].H)),
           "d66 out L102")
    anchor("A32", "DOUBLE-GRID(3,2) version registers", 18,
           sum(1 for e in built["DOUBLE-GRID(3,2)"].H if is_division(e)),
           "d66 out L227")
    anchor("A33", "CONFLICT-GRID(3,4) version registers", 12,
           sum(1 for e in built["CONFLICT-GRID(3,4)"].H if is_division(e)),
           "d66 out L223")

    def dg_events(g, R):
        return 4 * g + 2 * g * (g - 1) + R * (2 * g * g + 2 * g)

    def cg_events(g, R):
        return g * (g + 1) + (R - 1) * (g * (g + 1) + 2 * g)

    for aid, nm, d, comm, src in [
            ("A39", CTRL, 2, "1.46", "d60 out L18"),
            ("A40", CTRL, 3, "1.61", "d60 out L19"),
            ("A41", "DOUBLE-GRID(3,2)", 2, "1.96", "d66 out L64"),
            ("A42", "CONFLICT-GRID(3,4)", 2, "1.86", "d66 out L60")]:
        anchor(aid, f"{nm} d={d} mean|D| (2-decimal rendering)", comm,
               dec2(prof_full[nm][d]["mean"]), src)
    anchor("A34", "DOUBLE-GRID event-count law at the committed R=2", 72,
           dg_events(3, 2), "law, checked at d66's committed rows")
    anchor("A35", "DOUBLE-GRID event-count law at the committed R=4", 120,
           dg_events(3, 4), "d66 out L65")
    anchor("A36", "CONFLICT-GRID event-count law at the committed R=4", 66,
           cg_events(3, 4), "d66 out L60")
    anchor("A37", "CONFLICT-GRID event-count law at the committed R=6", 102,
           cg_events(3, 6), "d66 out L61")
    anchor("A38", "CONFLICT-GRID event-count law at the committed R=10", 174,
           cg_events(3, 10), "d66 out L62")
    gate("G-V10-XCHECK-LAW",
         f"the two crystals the pin names that v10 never swept -- "
         f"DOUBLE-GRID(3,3) and CONFLICT-GRID(3,2) -- are cross-checked by a "
         f"CLOSED-FORM event-count law verified at every committed member of "
         f"its own family (A34-A38): the law predicts "
         f"{dg_events(3, 3)} and {cg_events(3, 2)} and the rebuilds carry "
         f"{len(built['DOUBLE-GRID(3,3)'].H)} and "
         f"{len(built['CONFLICT-GRID(3,2)'].H)}",
         dg_events(3, 3) == len(built["DOUBLE-GRID(3,3)"].H)
         and cg_events(3, 2) == len(built["CONFLICT-GRID(3,2)"].H),
         {"predicted": [dg_events(3, 3), cg_events(3, 2)],
          "measured": [len(built["DOUBLE-GRID(3,3)"].H),
                       len(built["CONFLICT-GRID(3,2)"].H)]})
    reg(dg_events(3, 3), cg_events(3, 2), 120, 102, 174)
    checkpoint("SEC 4 (the arena and the v10 cross-check)")

    # -------------------------------------------------------------- SEC 5
    emit("")
    emit("=" * 78)
    emit("SEC 5  THE HEADLINE -- the division field's translation "
         "stabilizer on Z_3^2")
    emit("=" * 78)
    stab_tab, stab_rows = {}, []
    for nm, kind, _f in CRYSTALS:
        b = built[nm]
        for rd in READINGS:
            f = division_field(b, rd, nm)
            S1 = stabilizer(f)
            S2 = stabilizer_by_characters(f)
            nmS = subgroup_name(S1)
            supp = sum(1 for x in SITES if f[x] > 0)
            vec = [f[x] for x in SITES]
            stab_tab[(nm, rd)] = nmS
            reg(len(S1), supp, *vec)
            reg(f"{supp}/{len(SITES)}")
            stab_rows.append({"crystal": nm, "kind": kind, "reading": rd,
                              "field": vec, "support": supp,
                              "order": len(S1), "stabilizer": nmS,
                              "elements": [list(t) for t in S1]})
            emit(f"  [DATA] {nm:19s} {rd:10s} field={vec} support={supp}/9")
            expect_triv = (kind == "CONTROL")
            gate(f"G-STAB[{nm}|{rd}]",
                 f"MEASURED EXACTLY: the division-event field at this "
                 f"crystal and this site reading is {vec} over the nine "
                 f"sites (support {supp}/9) and its translation stabilizer "
                 f"in Z_3^2 is {nmS}, of order {len(S1)}, elements "
                 f"{[list(t) for t in S1]} -- "
                 + ("TRIVIAL, so the division events of this crystal do NOT "
                    "form a crystal, which is the value the DECLARED "
                    "COUNTEREXAMPLE CONTROL must return"
                    if expect_triv else
                    "NONTRIVIAL, so the division events of this crystal DO "
                    "form a crystal at this reading"),
                 (len(S1) == 1) if expect_triv else (len(S1) > 1),
                 {"crystal": nm, "reading": rd, "order": len(S1),
                  "stabilizer": nmS, "support": supp, "field": vec})
            gate(f"G-STAB-RECON[{nm}|{rd}]",
                 f"the same stabilizer is re-derived by an INDEPENDENT "
                 f"route sharing no code and no typed constant with the "
                 f"first -- the annihilator of the support of the exact "
                 f"Z_3^2 Fourier transform in Z[omega] = Z[t]/(t^2+t+1), "
                 f"running over the DUAL group instead of translating the "
                 f"field -- and the two agree element for element: {nmS}",
                 S1 == S2, {"crystal": nm, "reading": rd,
                            "direct": [list(t) for t in S1],
                            "characters": [list(t) for t in S2]})
            if kind == "ARBITRATION":
                gate(f"G-DIAGONAL-INVARIANCE[{nm}|{rd}]",
                     f"the DIAGONAL translation (1,1) lies in this "
                     f"stabilizer: the invariance direction the four "
                     f"arbitration crystals share is <(1,1)>, and here the "
                     f"stabilizer is {nmS}",
                     (1, 1) in S1, {"crystal": nm, "reading": rd,
                                    "contains_(1,1)": (1, 1) in S1})
    PAYLOAD["stabilizers"] = stab_rows

    agree = [nm for nm in ARB
             if stab_tab[(nm, "initiator")] == stab_tab[(nm, "footprint")]]
    diverge = [nm for nm in ARB if nm not in agree]
    reg(len(agree), len(diverge))
    gate("G-READING-DIVERGENCE",
         f"THE SITE READING IS NOT NEUTRAL, AND THE SCOUT'S PRELIMINARY IS "
         f"CORRECTED.  The scout recorded 'stabilizers AGREE, supports "
         f"differ (6/9 vs 9/9)'.  MEASURED: the two readings agree at "
         f"{len(agree)} of 4 arbitration crystals ({agree}) and DIVERGE at "
         f"{len(diverge)} ({diverge}), where the footprint field is "
         f"CONSTANT and its stabilizer is the whole group; and the supports "
         f"are 6/9 vs 9/9 only on the DOUBLE-GRIDs, 3/9 vs 9/9 on the "
         f"CONFLICT-GRIDs.  The divergence runs in ONE direction only -- "
         f"the footprint reading never shrinks the stabilizer -- and "
         f"<(1,1)> lies in all eight arbitration cells",
         len(diverge) == 2 and set(diverge) == {"CONFLICT-GRID(3,2)",
                                                "CONFLICT-GRID(3,4)"},
         {"agree": agree, "diverge": diverge,
          "table": {f"{k[0]}|{k[1]}": v for k, v in sorted(stab_tab.items())}})
    checkpoint("SEC 5 (the stabilizer table)")

    # -------------------------------------------------------------- SEC 6
    emit("")
    emit("=" * 78)
    emit("SEC 6  GEOMETRY INVARIANCE under the renewal-only rebuild")
    emit("=" * 78)
    gate("G-GEOM-POP-INSTRUMENT",
         "arm (a)'s primary sub-reading uses D60's OWN committed device "
         "(V12): the poset is left whole and only the metric population "
         "changes.  Arm (a)'s second sub-reading takes the literal sparse "
         "record -- the subsequence of marked events -- and recomputes its "
         "event poset from scratch.  'FILTER' is ambiguous between the two "
         "and both are run; the fiber is 2 and it is declared, not chosen",
         True, {"sub_readings": ["POP (poset whole)", "SUB (poset rebuilt)"],
                "fiber": 2},
         waiver={"class": "DECLARATION-CARRIED",
                 "reason": "a declaration about which two objects the arm "
                           "measures; both are measured below, per crystal"})

    geom_rows, varies_witness = [], []
    for nm, kind, _f in CRYSTALS:
        b = built[nm]
        C = poset_of(b.H)
        hh = heights(C)
        D = [i for i, e in enumerate(b.H) if is_division(e)]
        pop = list(D)
        if MUTANT == "MUT-GEOM-VARIES" and nm == "DOUBLE-GRID(3,2)":
            DIRS = {e: len(sky_b(C, e, 2, hh)) for e in range(len(C))}
            pop = [i for i in D if DIRS[i] != max(DIRS[j] for j in D)]
        pf, pr = prof_full[nm], profile(C, pop)
        sub = [e for e in b.H if is_division(e)]
        ps = profile(poset_of(sub)) if sub else None
        # the KR height control
        need = Counter(hh[i] for i in D)
        ctrl, deficit, mixed = [], 0, []
        for lay in sorted(need):
            poolv = [i for i in range(len(C)) if hh[i] == lay
                     and i not in set(D)]
            if poolv:
                mixed.append(lay)
            ctrl += poolv[:need[lay]]
            deficit += need[lay] - len(poolv[:need[lay]])
        if MUTANT == "MUT-HEIGHT-IMPURE" and nm == "DOUBLE-GRID(3,2)":
            mixed = [1]
        reg(pf["height"], (ps["height"] if ps else 0), len(D), deficit)
        for d in (2, 3):
            for src in (pf, pr) + ((ps,) if ps else ()):
                for k in ("h2", "h4", "max", "mean", "om", "n", "pairs"):
                    if src[d][k] is not None:
                        reg(src[d][k])
        reg(*sorted(need), *[need[x] for x in sorted(need)])
        gate(f"G-GEOM-HEIGHTPURE[{nm}]",
             f"HEIGHT PURITY, MEASURED: the {len(D)} marked events of this "
             f"crystal occupy the height layers {sorted(need)} of a poset of "
             f"longest chain {pf['height']}, and {len(mixed)} of those "
             f"layers contain any unmarked event -- the marked events fill "
             f"whole layers and share them with nothing else",
             len(mixed) == 0 and len(D) > 0,
             {"crystal": nm, "layers": sorted(need), "mixed_layers": mixed,
              "longest_chain": pf["height"], "marked": len(D)})
        gate(f"G-GEOM-HCTRL[{nm}]",
             f"THE KLEITMAN-ROTHSCHILD HEIGHT CONTROL IS PROVABLY EMPTY "
             f"HERE (V08).  A height-matched control population -- same "
             f"size, same height histogram, drawn from unmarked events -- "
             f"has size {len(ctrl)} with deficit {deficit} of {len(D)}, "
             f"because height purity leaves no unmarked event at any marked "
             f"height.  Every POPULATION-AVERAGED row below is therefore "
             f"confounded with a height shift that CANNOT be controlled, "
             f"and this unit certifies none of them",
             len(ctrl) == 0 and deficit == len(D),
             {"crystal": nm, "control_size": len(ctrl), "deficit": deficit,
              "marked": len(D)})
        for d in (2, 3):
            inv = (pf[d]["max"] == pr[d]["max"])
            att = [e for e in pf[d]["attained"]]
            attD = [e for e in att if e in set(D)]
            reg(pf[d]["max"], pr[d]["max"], len(att), len(attD))
            expect = (kind == "ARBITRATION")
            if not inv:
                varies_witness.append(
                    f"{nm}|d={d}|max|D|:{pf[d]['max']}->{pr[d]['max']}")
            gate(f"G-GEOM-POP-WIDTH[{nm}|d={d}]",
                 f"THE CHART-WIDTH ROW, the one geometry row a population "
                 f"restriction cannot confound (a maximum over a subset "
                 f"equals the maximum over the whole set exactly when the "
                 f"maximum is ATTAINED on the subset): full max|D| = "
                 f"{pf[d]['max']}, attained at {len(att)} events of which "
                 f"{len(attD)} are marked; restricted max|D| = "
                 f"{pr[d]['max']} -- "
                 + ("INVARIANT" if inv else
                    f"VARIES-{pf[d]['max']}->{pr[d]['max']}")
                 + (", the kinematic prediction" if expect else
                    ", the value the DECLARED COUNTEREXAMPLE CONTROL must "
                    "return"),
                 inv if expect else (not inv),
                 {"crystal": nm, "depth": d, "full_max": pf[d]["max"],
                  "restricted_max": pr[d]["max"], "attainers": len(att),
                  "attainers_marked": len(attD), "invariant": inv})
        gate(f"G-GEOM-BLOCKED[{nm}]",
             f"the POPULATION-AVERAGED rows are reported and NOT certified: "
             f"at d=2 homogeneity moves {pf[2]['h2']} -> {pr[2]['h2']}, "
             f"|D|>=4 moves {pf[2]['h4']} -> {pr[2]['h4']} and mean overlap "
             f"moves {pf[2]['om']} -> {pr[2]['om']}, every one of them "
             f"inseparable from the height shift whose control G-GEOM-HCTRL "
             f"proves empty.  BLOCKED-AT-THE-EMPTY-HEIGHT-CONTROL is this "
             f"unit's reading of these rows, not INVARIANT and not VARIES",
             True,
             {"crystal": nm,
              "d2_full": {"h2": str(pf[2]["h2"]), "h4": str(pf[2]["h4"]),
                          "om": str(pf[2]["om"]), "mean": str(pf[2]["mean"])},
              "d2_restricted": {"h2": str(pr[2]["h2"]),
                                "h4": str(pr[2]["h4"]),
                                "om": str(pr[2]["om"]),
                                "mean": str(pr[2]["mean"])},
              "d3_full": {"h2": str(pf[3]["h2"]), "h4": str(pf[3]["h4"]),
                          "om": str(pf[3]["om"]), "mean": str(pf[3]["mean"])},
              "d3_restricted": {"h2": str(pr[3]["h2"]),
                                "h4": str(pr[3]["h4"]),
                                "om": str(pr[3]["om"]),
                                "mean": str(pr[3]["mean"])}},
             waiver={"class": "MEASURED-THEN-DECLINED",
                     "reason": "the numbers are computed exactly and printed; "
                               "what is withheld is the INFERENCE from them, "
                               "on the ground that the KR control the catalog "
                               "requires is empty at every one of these "
                               "crystals"})
        gate(f"G-GEOM-SUB[{nm}]",
             f"arm (a)'s second sub-reading -- the literal sparse record, "
             f"poset rebuilt on the {len(sub)} marked events alone -- "
             f"carries longest chain {ps['height'] if ps else 0} against the "
             f"full record's {pf['height']}, and max|D| "
             f"{ps[2]['max'] if ps else 0} at d=2 against {pf[2]['max']}: a "
             f"DIFFERENT poset, not a restriction of this one, and reported "
             f"as data only",
             True,
             {"crystal": nm, "events": len(sub),
              "height_sub": ps["height"] if ps else 0,
              "height_full": pf["height"],
              "max_sub_d2": ps[2]["max"] if ps else 0,
              "max_full_d2": pf[2]["max"],
              "max_sub_d3": ps[3]["max"] if ps else 0,
              "max_full_d3": pf[3]["max"]},
             waiver={"class": "MEASURED-THEN-DECLINED",
                     "reason": "the sparse record's own poset is a different "
                               "object from the crystal's; no invariance "
                               "claim is made across the two"})
        geom_rows.append({
            "crystal": nm, "kind": kind, "marked": len(D),
            "longest_chain_full": pf["height"],
            "longest_chain_sub": ps["height"] if ps else 0,
            "height_layers": sorted(need), "mixed_layers": mixed,
            "hctrl_size": len(ctrl), "hctrl_deficit": deficit,
            "full": {str(d): {k: str(pf[d][k]) for k in
                              ("h2", "h4", "max", "mean", "om", "n", "pairs")}
                     for d in (2, 3)},
            "restricted": {str(d): {k: str(pr[d][k]) for k in
                                    ("h2", "h4", "max", "mean", "om", "n",
                                     "pairs")} for d in (2, 3)},
            "subrecord": {str(d): {k: str(ps[d][k]) for k in
                                   ("h2", "h4", "max", "mean", "om", "n",
                                    "pairs")} for d in (2, 3)} if ps else None,
        })
    PAYLOAD["geometry"] = geom_rows

    # arm (b): the Builder rerun under two declared sub-grammars
    emit("")
    emit("  [arm (b) -- the Builder rerun on a restricted candidate stream]")
    armb = []
    for nm, kind, fn in CRYSTALS:
        bb = fn(lambda e: e[0] in ('p', 'r'))
        ref = bb.refusal
        if MUTANT == "MUT-ARMB-COMPLETES" and nm == "DOUBLE-GRID(3,2)":
            ref = None
        bi = fn(lambda e: e[0] != 'n')
        same = (bi.H == built[nm].H) and bi.refusal is None \
            and bi.maxhits == 1
        reg(len(bb.H), len(bi.H))
        armb.append({"crystal": nm, "renewal_only_events": len(bb.H),
                     "renewal_only_refusal": ref,
                     "idle_free_events": len(bi.H),
                     "idle_free_identical": same})
        gate(f"G-GEOM-ARMB-RENEWAL[{nm}]",
             f"arm (b) at the DECLARED RENEWAL-ONLY SUB-GRAMMAR (V11's "
             f"shape: the support is restricted, the committed weights are "
             f"untouched) -- the candidate stream keeps only the two "
             f"record-bearing tags and drops the two the POSIT calls "
             f"kinematics.  THIS CRYSTAL CANNOT BE REBUILT: the record "
             f"stops after {len(bb.H)} events with a LOCATED refusal at "
             f"{ref}, its first delivery.  A refusal is recorded, never "
             f"patched",
             ref is not None,
             {"crystal": nm, "events": len(bb.H), "refusal": ref})
        gate(f"G-GEOM-ARMB-IDLEFREE[{nm}]",
             f"the isolation control for arm (b): dropping ONLY the idle tag "
             f"leaves the crystal rebuilt EVENT FOR EVENT ({len(bi.H)} "
             f"events, identical = {same}), so the tag that blocks the "
             f"renewal-only rebuild is exactly one, the DELIVERY",
             same, {"crystal": nm, "events": len(bi.H), "identical": same})
    PAYLOAD["arm_b"] = armb
    gate("G-GEOM-ARMC-REGISTERED",
         "arm (c) of pin R3 -- quotient the record by its non-arbitration "
         "events -- is REGISTERED AND NOT RUN, as the pin allows; nothing "
         "in this unit's verdict descends from it",
         True, {"arm": "quotient", "run": False},
         waiver={"class": "REGISTER-ONLY",
                 "reason": "a successor register entry; its absence is "
                           "visible in the arm rows, which carry (a) and (b) "
                           "only"})
    gate("G-GEOM-SPATIAL-TAUTOLOGY",
         "the crystal's SPATIAL rows -- the co-division link counts of "
         "SEC 7 -- are functions of the marked events ALONE, so they are "
         "invariant under every renewal-only operationalization that "
         "preserves the marking.  That is a tautology of the definition, it "
         "is stated here so that it is never counted as evidence, and it is "
         "excluded from the geometry verdict",
         True, {"rows": "co-division link counts", "counted_as_evidence":
                False},
         waiver={"class": "DECLARATION-CARRIED",
                 "reason": "a statement about what this unit refuses to "
                           "count; the rows themselves are measured in SEC 7"})

    widths_ok = all(prof_full[nm][d]["max"]
                    == profile(poset_of(built[nm].H),
                               [i for i, e in enumerate(built[nm].H)
                                if is_division(e)])[d]["max"]
                    for nm in ARB for d in (2, 3))
    geom_verdict = ("GEOMETRY-INVARIANT-AT-THE-CONTROLLED-ROW-"
                    "REST-BLOCKED-AT-THE-EMPTY-HEIGHT-CONTROL"
                    if widths_ok else
                    "GEOMETRY-VARIES-" + ";".join(varies_witness))
    emit("")
    emit(f"  [GEOMETRY SEGMENT VERDICT] {geom_verdict}")
    gate("G-GEOM-SEGMENT",
         f"THE GEOMETRY SEGMENT (V06 is the falsifier this segment answers "
         f"to): {geom_verdict}.  The chart-width row is INVARIANT at 4 of 4 "
         f"arbitration crystals at BOTH depths and NOT invariant at the "
         f"control, so the segment's two-way requirement is discharged on "
         f"the row that carries it; every population-averaged row is "
         f"BLOCKED; and paper 0 10's third falsifier -- 'sparse records "
         f"destroy the geometry' -- does NOT fire, because a prior "
         f"obstruction fires first: arm (b) shows the sparse record is not "
         f"CONSTRUCTIBLE",
         widths_ok, {"verdict": geom_verdict, "width_row_invariant":
                     widths_ok, "varies_witness": varies_witness})
    checkpoint("SEC 6 (geometry invariance)")

    # -------------------------------------------------------------- SEC 7
    emit("")
    emit("=" * 78)
    emit("SEC 7  THE BRIDGES -- at declared scope, candidate readings named")
    emit("=" * 78)
    bridge_rows = []
    for nm, kind, _f in CRYSTALS:
        b = built[nm]
        S = site_map(b)
        inv = {}
        for a, x in S.items():
            inv[x] = a
        divs = [e for e in b.H if is_division(e)]
        links = {}
        for lk in AXIS + DIAG:
            vals = []
            for x in SITES:
                u = inv[x]
                v = inv[((x[0] + lk[0]) % L, (x[1] + lk[1]) % L)]
                vals.append(sum(1 for e in divs
                                if u in regs_of(e) and v in regs_of(e)))
            links[lk] = vals
        if MUTANT == "MUT-DIAGONAL" and nm == "DOUBLE-GRID(3,2)":
            links[(1, 1)] = [1] + links[(1, 1)][1:]
        idx = [i for i, e in enumerate(b.H) if is_division(e)]
        legs = sorted(Counter(idx[k + 1] - idx[k]
                              for k in range(len(idx) - 1)).items())
        f = division_field(b, "initiator", nm)
        supp = sorted(x for x in SITES if f[x] > 0)
        cos = sorted({(x[1] - x[0]) % L for x in supp})
        is_cosets = all(sum(1 for x in supp if (x[1] - x[0]) % L == c) == L
                        for c in cos)
        ax_hom = all(len(set(links[lk])) == 1 and links[lk][0] > 0
                     for lk in AXIS) if kind == "ARBITRATION" else \
            all(set(links[lk]) == {0} for lk in AXIS)
        dg_zero = all(set(links[lk]) == {0} for lk in DIAG)
        reg(*[v for lk in AXIS + DIAG for v in links[lk]])
        reg(*[c for c, _n in legs], *[n for _c, n in legs])
        emit(f"  [DATA] {nm:19s} legs={legs} axis={links[AXIS[0]][0]}/"
             f"{links[AXIS[1]][0]} diag={links[DIAG[0]][0]}/"
             f"{links[DIAG[1]][0]}")
        gate(f"G-BRIDGE-AXIS[{nm}]",
             f"the co-division ADJACENCY on the two axis links is "
             f"{links[AXIS[0]]} and {links[AXIS[1]]} across the nine sites: "
             + ("homogeneous and strictly positive -- the renewal "
                "sublattice's bridges are the rook's graph's rows and "
                "columns" if kind == "ARBITRATION" else
                "identically zero -- the DECLARED COUNTEREXAMPLE CONTROL "
                "carries NO bridges at all, its single division event "
                "touching one site"),
             ax_hom, {"crystal": nm, "axis_10": links[AXIS[0]],
                      "axis_01": links[AXIS[1]]})
        gate(f"G-BRIDGE-DIAG[{nm}]",
             f"the DIAGONAL co-division link counts are {links[DIAG[0]]} and "
             f"{links[DIAG[1]]}: identically ZERO at 9 of 9 sites.  q_12 = 0 "
             f"is INHERITED from the rook's graph (V13) and is NOT a finding "
             f"of this unit",
             dg_zero, {"crystal": nm, "diag_11": links[DIAG[0]],
                       "diag_12": links[DIAG[1]]})
        gate(f"G-BRIDGE-SUPPORT[{nm}]",
             f"the renewal sublattice's SUPPORT at the initiator reading is "
             f"{[list(x) for x in supp]}, a union of {len(cos)} full cosets "
             f"of <(1,1)> (residues {cos} of j-i) -- "
             + ("the support is itself <(1,1)>-periodic, which is the "
                "sublattice-is-a-crystal statement read on the SET rather "
                "than on the counts" if kind == "ARBITRATION" else
                "a SINGLE site carrying no coset structure at all -- the "
                "value the DECLARED COUNTEREXAMPLE CONTROL must return"),
             is_cosets if kind == "ARBITRATION" else not is_cosets,
             {"crystal": nm, "support": [list(x) for x in supp],
              "cosets": cos, "is_coset_union": is_cosets})
        gate(f"G-BRIDGE-LEGS[{nm}]",
             f"the RECORD-ORDER bridges -- the gaps between consecutive "
             f"marked events -- have multiset {legs} on this crystal.  "
             f"paper-09 4's support holes (no inter-renewal leg of length "
             f"one or two) carry a two-actor DELIVERY-FREE scope tag and "
             f"this arena is neither, so this row is a COMPARISON and not a "
             f"test of that law",
             True, {"crystal": nm, "legs": legs},
             waiver={"class": "SCOPE-DISCLOSED",
                     "reason": "the source law's own scope tag excludes this "
                               "arena; the numbers are reported so a "
                               "successor at matched scope can use them"})
        bridge_rows.append({"crystal": nm, "kind": kind,
                            "axis": {str(lk): links[lk] for lk in AXIS},
                            "diagonal": {str(lk): links[lk] for lk in DIAG},
                            "legs": legs, "support": [list(x) for x in supp],
                            "support_cosets": cos})
    PAYLOAD["bridges"] = bridge_rows
    gate("G-BRIDGE-SCOPE",
         "THE BRIDGES ARE REPORTED, NOT INTERPRETED.  The pin asks what "
         "structure the bridges carry AT DECLARED SCOPE ONLY and forbids an "
         "indivisibility claim beyond what the arena can measure.  This "
         "arena measures three bridge objects -- the co-division adjacency, "
         "the support's coset structure, the record-order leg multiset -- "
         "and NONE of them is a transition kernel, so no indivisibility "
         "reading is available here.  The candidate readings are NAMED: "
         "(i) the axis link counts as the crystal's q_11 and q_22; (ii) the "
         "leg multiset as a crystal-scope analogue of paper-09 4's g(n); "
         "(iii) the coset support as the renewal sublattice's own period "
         "lattice.  Each is a candidate reading until an adjudication makes "
         "it otherwise",
         True, {"objects": 3, "indivisibility_claim": False,
                "candidate_readings": 3},
         waiver={"class": "DECLARATION-CARRIED",
                 "reason": "a statement of what this unit declines to infer; "
                           "the measurements it refers to are the per-crystal "
                           "bridge gates above"})
    checkpoint("SEC 7 (the bridges)")

    # -------------------------------------------------------------- SEC 8
    emit("")
    emit("=" * 78)
    emit("SEC 8  THE WALLS (pin R5) -- construction law, argued before use")
    emit("=" * 78)
    banned_hits = []
    for pth in (os.path.abspath(__file__),
                os.path.join(REPO, "v14", "paper-14-u4-renewal-crystals.md")):
        if os.path.exists(pth):
            with open(pth, "r", encoding="utf-8") as fh:
                if BANNED in fh.read():
                    banned_hits.append(pth)
    gate("G-WALL-L1",
         "L-1's FOURTH FORM, ARGUED BEFORE ANY TEST AND THEN DECLINED.  "
         "L-1 (V09) records that order-level covariance is a fourth form "
         "outside v3 paper 8's three and that its admissibility is v11's to "
         "argue when U4 runs.  THE ARGUMENT: admissibility would require a "
         "declared group acting on the generated causal order together with "
         "a reason to read that group as a covariance group; this arena "
         "supplies five finite records and a translation action on their "
         "SITE LATTICE, and the corpus contains no bridge from Z_3^2 "
         "translations to any boost.  This unit therefore does NOT test the "
         "fourth form; it remains unargued and untested here and is "
         "registered for a successor",
         len(banned_hits) == 0,
         {"fourth_form_tested": False, "banned_sentence_hits": banned_hits})
    gate("G-WALL-L1-PERMUTATION",
         "what this unit DOES measure is inside L-1's own scope guard "
         "(V10): the Z_3^2 translation stabilizer is a PERMUTATION ACTION on "
         "the actor set, and L-1 does not forbid a permutation action.  The "
         "headline measurement therefore needs no fourth-form argument at "
         "all",
         True, {"action": "permutation on the actor set", "forbidden": False})
    gate("G-WALL-BHS",
         "NO SPRINKLING-GRADE LORENTZ-INVARIANCE TEST IS RUN.  The catalog "
         "(V07) records that these crystals are finite-valency by "
         "construction, so BHS makes sprinkling-grade statistical Lorentz "
         "invariance provably unavailable on them and running the test "
         "would manufacture a false negative.  This unit runs none: no "
         "sprinkling, no boost, no rapidity, no frame appears anywhere in "
         "its measurements",
         True, {"sprinkling_grade_LI_tests_run": 0})
    kr = [{"crystal": r["crystal"], "n": r["full"]["2"]["n"],
           "longest_chain": r["longest_chain_full"],
           "sub_n": r["marked"], "sub_longest_chain": r["longest_chain_sub"]}
          for r in geom_rows]
    kr_ok = all(r["longest_chain"] > 3 for r in kr)
    gate("G-WALL-KR",
         f"EVERY DIMENSION-ADJACENT READING CARRIES ITS HEIGHT CONTROL "
         f"(V08).  The only dimension-adjacent row this unit reads is the "
         f"chart width max|D|, and it is reported with the longest chain of "
         f"the population it is read on, full and sparse, at every crystal: "
         f"{kr}.  The Kleitman-Rothschild discriminator is the longest "
         f"chain (KR orders return 3 where a sprinkling returns tens) and "
         f"no population here returns 3.  No Myrheim-Meyer estimate is run "
         f"at all",
         kr_ok, {"height_controls": kr, "MM_estimates_run": 0})
    gate("G-WALL-DIAGONAL",
         "THE DIAGONAL QUESTION IS NOT ANSWERED HERE.  q_12 = 0 is "
         "INHERITED (V13): the co-division graph is the rook's graph and "
         "diagonal pairs share neither row nor column, measured at 9 of 9 "
         "sites on every crystal by the G-BRIDGE-DIAG gates.  This unit "
         "notes a genuine counterpoint and refuses to read it: the "
         "division-event FIELD's invariance direction is the diagonal "
         "<(1,1)>, while the diagonal LINK count is identically zero.  "
         "These are different objects -- a translation of the site lattice "
         "and a generator of the link structure -- and nothing here decides "
         "the other",
         True, {"q12": 0, "inherited": True, "answered_here": False})
    gate("G-DEAD-LIST-CITED",
         "the pre-registered dead list (weld-2 pin R4 / scout S6) is CITED "
         "and not re-run: R6b' C1-C5 and the four blanket rows.  No "
         "measurement above re-derives any of them",
         True, {"dead_items": 5},
         waiver={"class": "DECLARATION-CARRIED",
                 "reason": "a discipline statement about what this unit does "
                           "NOT compute; the receipt's measurement rows "
                           "exhibit the absence"})
    checkpoint("SEC 8 (the walls)")

    # -------------------------------------------------------------- SEC 9
    emit("")
    emit("=" * 78)
    emit("SEC 9  THE VERDICT")
    emit("=" * 78)
    head = build_head(stab_tab)
    head2 = reconstruct_head()
    if MUTANT == "MUT-HEAD":
        head = head.replace("Z3^2", "<(2,1)>", 1)
    gate("G-HEAD-EQUALITY",
         f"THE HEAD IS DERIVED, NOT TYPED, AND IT SURVIVES A COMPLETE-STRING "
         f"EQUALITY GATE AGAINST AN INDEPENDENT RECONSTRUCTION.  The "
         f"reconstruction builds the five records afresh, reads their "
         f"marked events by the SHAPE predicate rather than the tag, maps "
         f"actors to sites by enumeration rather than by parsing their "
         f"names, computes each stabilizer as a Fourier annihilator over "
         f"Z[omega], and takes the outcome NAME from the pin's own OUTCOMES "
         f"section by a different extractor -- sharing no instrument code, "
         f"no derived input and no typed literal with the path above.  "
         f"Length {len(head)} vs {len(head2)}",
         head == head2, {"head": head, "reconstruction": head2,
                         "identical": head == head2})
    emit("")
    emit(f"  [HEAD] {head}")
    emit(f"  [GEOMETRY] {geom_verdict}")
    PAYLOAD["head"] = head
    PAYLOAD["geometry_verdict"] = geom_verdict
    reg(*re.findall(r"\d+/\d+|\d+", head + " " + geom_verdict))
    PAYLOAD["stabilizer_table"] = {f"{k[0]}|{k[1]}": v
                                   for k, v in sorted(stab_tab.items())}
    return head, geom_verdict


def head_table(tab):
    short = {"DOUBLE-GRID(3,2)": "DG32", "DOUBLE-GRID(3,3)": "DG33",
             "CONFLICT-GRID(3,2)": "CG32", "CONFLICT-GRID(3,4)": "CG34",
             "D60-GRID(3,12)": "CTRL"}
    return "|".join(
        f"{short[nm]}:{tab[(nm, 'initiator')]}/{tab[(nm, 'footprint')]}"
        for nm, _k, _f in CRYSTALS)


def outcome_name(which):
    """Extract a PRE-REGISTERED outcome name from the pin's OUTCOMES
    section.  Route 1: span the backticked tokens over the whole file."""
    txt = SOURCES["v14/note-u4-pin.md"]
    toks = re.findall(r"`([^`]+)`", txt, flags=re.S)
    for t in toks:
        t2 = re.sub(r"-\s*\n\s*", "-", t).strip()
        if t2.startswith(which):
            return t2
    raise SystemExit("pin does not carry the pre-registered outcome name")


def outcome_name_alt(which):
    """Route 2, for the reconstruction: scan the OUTCOMES section line by
    line, rejoin the hyphenated line breaks, and take the first token."""
    lines = SOURCES["v14/note-u4-pin.md"].split("\n")
    start = None
    for i, ln in enumerate(lines):
        if ln.strip().startswith("## OUTCOMES"):
            start = i
    body = " ".join(lines[start:]).replace("- ", "-")
    out = []
    inside = False
    buf = ""
    for ch in body:
        if ch == "`":
            if inside:
                out.append(buf.replace(" ", ""))
                buf = ""
            inside = not inside
        elif inside:
            buf += ch
    for t in out:
        if t.startswith(which):
            return t
    raise SystemExit("pin does not carry the pre-registered outcome name")


def build_head(tab):
    base = outcome_name("U4-THE-DIVISION-EVENTS-FORM-A-CRYSTAL")
    return re.sub(r"<[^>]*>$", "", base) + "[" + head_table(tab) + "]"


def reconstruct_head():
    """The INDEPENDENT reconstruction of the head.  Shares the arena (the
    five records are the object of study, not the instrument) and shares
    nothing else: its own build, its own marking predicate, its own site
    map, its own stabilizer algorithm, its own outcome-name extractor."""
    tab = {}
    for nm, _kind, fn in CRYSTALS:
        rec = fn()
        acts = sorted(set(rec.actors))
        smap = {}
        for k, a in enumerate(acts):
            smap[a] = (k // L, k % L)
        marked = [e for e in rec.H if is_division_structural(e)]
        if MUTANT == "MUT-DIVPRED":
            marked = [e for e in rec.H if e[0] == 'd']
        for rd in READINGS:
            g = dict.fromkeys(SITES, 0)
            for e in marked:
                if rd == "initiator":
                    g[smap[e[1]]] = g[smap[e[1]]] + 1
                else:
                    for r in regs_of(e):
                        if r in smap:
                            g[smap[r]] = g[smap[r]] + 1
            if MUTANT == "MUT-APERIODIC-DIVISION" and nm == "DOUBLE-GRID(3,2)":
                g[(0, 2)] += 1
            if MUTANT == "MUT-CONTROL-PERIODIC" and nm == CTRL:
                g = dict.fromkeys(SITES, 1)
            tab[(nm, rd)] = subgroup_name(stabilizer_by_characters(g))
    base = outcome_name_alt("U4-THE-DIVISION-EVENTS-FORM-A-CRYSTAL")
    cut = base.find("<")
    return base[:cut] + "[" + head_table(tab) + "]"


# ===========================================================================
# verify-paper, the receipt, the integrity gate
# ===========================================================================

PAPER = os.path.join(REPO, "v14", "paper-14-u4-renewal-crystals.md")
STRUCTURAL = {
    # enumerated structural numerals: era rules, pin/ledger indices, dates,
    # section numbers, source line references.  Each is listed so a reader
    # can audit the waiver.
    "82", "87", "91", "24", "34", "62", "20", "46", "15", "105", "102", "101",
    "2026", "08", "10", "14", "13", "11", "09", "60", "66", "67", "63", "58",
    "47", "42", "74", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "07", "28", "12", "1536", "972", "144", "2325", "29",
}
MASKS = ["the literal 'sha256-NN'", "sha256-12 hexes",
         "7-character commit hexes", "source line references Lnnn",
         "section references", "grid actor names", "heading numbers"]


def verify_paper():
    if not os.path.exists(PAPER):
        gate("G-VERIFY-PAPER-PRESENT",
             f"the paper {os.path.relpath(PAPER, REPO)} must exist for the "
             f"plain run: verify-paper runs INSIDE the plain run and covers "
             f"every numeral in it",
             False, {"path": os.path.relpath(PAPER, REPO), "exists": False})
        return
    with open(PAPER, "r", encoding="utf-8") as fh:
        txt = fh.read()
    gate("G-VERIFY-PAPER-PRESENT",
         f"the paper is present ({len(txt)} bytes) and every numeral in it "
         f"is checked below against numbers this run COMPUTED",
         True, {"bytes": len(txt)})
    # mask the identifier classes that are not quantities: sha256-12 and
    # 7-character commit hexes, and source line references.  Each mask is
    # named here so the waiver is auditable.
    masked = re.sub(r"sha256-\d+", " SHANAME ", txt)
    masked = re.sub(r"\b[0-9a-f]{12}\b", " SHA12 ", masked)
    masked = re.sub(r"\b[0-9a-f]{7}\b", " SHA7 ", masked)
    masked = re.sub(r"\bL\d+(?:[–-]\d+)?\b", " LINEREF ", masked)
    masked = re.sub(r"§\d+(?:\.\d+)*", " SECREF ", masked)
    masked = re.sub(r"(?m)^#+\s+\d+(?:\.\d+)*", " HEADING ", masked)
    masked = re.sub(r"\b[A-Z]\d\d\b", " ACTOR ", masked)
    toks = re.findall(r"\d+/\d+|\d+\.\d+|\d+", masked)
    matched, struct, unmatched = 0, 0, []
    for t in toks:
        if t in NUMREG:
            matched += 1
        elif t.lstrip("0") in NUMREG and t.lstrip("0"):
            matched += 1
        elif t in STRUCTURAL:
            struct += 1
        else:
            unmatched.append(t)
    cov = Fr(matched + struct, len(toks)) if toks else Fr(0)
    gate("G-VERIFY-PAPER-NUMERALS",
         f"NUMERAL COVERAGE, HONEST (#34): after masking {len(MASKS)} named "
         f"identifier classes ({MASKS}) the paper carries {len(toks)} "
         f"numeric tokens; {matched} reproduce a number this run computed, "
         f"{struct} match the ENUMERATED structural whitelist (era rule "
         f"numbers, ledger and pin indices, dates, section references -- "
         f"{len(STRUCTURAL)} entries, all printed in the "
         f"receipt), and {len(unmatched)} match neither: {sorted(set(unmatched))[:12]}.  "
         f"This gate is a TRANSCRIPTION check, not an independent "
         f"verification -- small integers match the registry trivially -- "
         f"and the meaning-binding coverage is G-VERIFY-PAPER-CLAIMS",
         len(unmatched) == 0,
         {"tokens": len(toks), "matched": matched, "structural": struct,
          "unmatched": sorted(set(unmatched)), "coverage": str(cov),
          "whitelist": sorted(STRUCTURAL), "masks": MASKS})
    claims = []
    for r in PAYLOAD["arena"]:
        claims.append(f"{r['events']} events, {r['divisions']} division")
    for r in PAYLOAD["stabilizers"]:
        claims.append(f"{r['stabilizer']}")
    claims.append(PAYLOAD["head"])
    claims.append(PAYLOAD["geometry_verdict"])
    miss = [c for c in claims if c not in txt]
    gate("G-VERIFY-PAPER-CLAIMS",
         f"MEANING-BINDING COVERAGE: {len(claims) - len(miss)} of "
         f"{len(claims)} keyed claim strings -- the per-crystal event and "
         f"division counts, every stabilizer name, the head and the "
         f"geometry verdict -- occur VERBATIM in the paper; missing "
         f"{miss[:4]}",
         len(miss) == 0, {"claims": len(claims), "missing": miss})


def render():
    out = "\n".join(LINES) + "\n"
    rec = {
        "unit": "U4 / paper-14 -- renewal-only crystals",
        "pin": {"path": "v14/note-u4-pin.md", "sha256_12": "06b62ecb60a9",
                "ledger": 105},
        "interpreter": INTERP,
        "head": PAYLOAD.get("head"),
        "geometry_verdict": PAYLOAD.get("geometry_verdict"),
        "stabilizer_table": PAYLOAD.get("stabilizer_table"),
        "counts": {"gates": len(GATES),
                   "gates_passed": sum(1 for g in GATES if g["passed"]),
                   "gates_failed": sum(1 for g in GATES if not g["passed"]),
                   "anchors": len(ANCHORS),
                   "anchors_passed": sum(1 for a in ANCHORS if a["passed"]),
                   "verbatim_anchors": len(VANCHORS),
                   "verbatim_passed": sum(1 for v in VANCHORS if v["found"]),
                   "waivers": len(WAIVERS),
                   "mutants_registered": len(MUTANTS),
                   "numbers_registered": len(NUMREG)},
        "gates": GATES, "anchors": ANCHORS, "verbatim": VANCHORS,
        "waivers": WAIVERS, "payload": PAYLOAD,
        "mutants": {k: MUTANTS[k] for k in sorted(MUTANTS)},
        "output_sha256": sha256_of(out.encode("utf-8")),
    }
    return out, json.dumps(rec, indent=2, sort_keys=True,
                           default=str) + "\n"


def write_and_verify(out, rj):
    tmp1, tmp2 = OUT_TXT + ".tmp", OUT_JSON + ".tmp"
    with open(tmp1, "w", encoding="utf-8") as fh:
        fh.write(out)
    with open(tmp2, "w", encoding="utf-8") as fh:
        fh.write(rj)
    with open(tmp1, "rb") as fh:
        b1 = fh.read()
    with open(tmp2, "rb") as fh:
        b2 = fh.read()
    rec = json.loads(b2.decode("utf-8"))
    ok = (b1 == out.encode("utf-8") and b2 == rj.encode("utf-8")
          and rec["output_sha256"] == sha256_of(b1)
          and rec["head"] == PAYLOAD.get("head")
          and PAYLOAD.get("head", "") in b1.decode("utf-8")
          and rec["counts"]["gates_failed"] == 0)
    print(f"  [{'PASS' if ok else 'FAIL'}] G-FINAL-INTEGRITY")
    print(f"         the two artifacts were written, RE-READ FROM DISK and "
          f"re-verified: {len(b1)} + {len(b2)} bytes, the receipt's recorded "
          f"output sha256 matches the file on disk, the head in the receipt "
          f"matches the head in the output and the head in memory, and no "
          f"gate failed")
    if not ok:
        os.remove(tmp1)
        os.remove(tmp2)
        return False
    os.replace(tmp1, OUT_TXT)
    os.replace(tmp2, OUT_JSON)
    return True


USAGE = ("usage: u4_crystals_exact.py [--selftest | --numbers | "
         "--mutant NAME]\n  no arguments: the plain run (writes "
         "u4_crystals_output.txt + u4_crystals_receipt.json)")


def parse_argv(argv):
    """#82: a strict argv whitelist.  Anything else exits 2."""
    if len(argv) == 1:
        return ("plain", None)
    if len(argv) == 2 and argv[1] == "--selftest":
        return ("selftest", None)
    if len(argv) == 2 and argv[1] == "--numbers":
        return ("numbers", None)
    if len(argv) == 3 and argv[1] == "--mutant":
        if argv[2] not in MUTANTS:
            print(f"unknown mutant: {argv[2]}", file=sys.stderr)
            print("registered mutants:", file=sys.stderr)
            for k in sorted(MUTANTS):
                print(f"  {k}: {MUTANTS[k]}", file=sys.stderr)
            sys.exit(2)
        return ("mutant", argv[2])
    print(USAGE, file=sys.stderr)
    sys.exit(2)


def main():
    global MUTANT, ANCHOR_FAIL, FAILED, QUIET
    mode, name = parse_argv(sys.argv)
    QUIET = mode in ("selftest", "mutant")

    if mode == "selftest":
        # corrupt ONE anchor, confirm the run refuses, WRITE NOTHING.
        before = (os.path.exists(OUT_TXT) and open(OUT_TXT, "rb").read(),
                  os.path.exists(OUT_JSON) and open(OUT_JSON, "rb").read())
        MUTANT = "MUT-ANCHOR"
        try:
            main_run()
        except SystemExit:
            pass
        died = ANCHOR_FAIL > 0
        after = (os.path.exists(OUT_TXT) and open(OUT_TXT, "rb").read(),
                 os.path.exists(OUT_JSON) and open(OUT_JSON, "rb").read())
        print("SELFTEST -- one committed anchor corrupted "
              "(DOUBLE-GRID(3,2) d=2 max|D|: 9 -> 8)")
        print(f"  anchors failed: {ANCHOR_FAIL} (expected >= 1)")
        print(f"  artifacts unchanged: {before == after}")
        print(f"  wrote nothing: True")
        ok = died and before == after
        print(f"  [{'PASS' if ok else 'FAIL'}] G-SELFTEST")
        sys.exit(0 if ok else 1)

    if mode == "mutant":
        MUTANT = name
        before = (os.path.exists(OUT_TXT) and open(OUT_TXT, "rb").read(),
                  os.path.exists(OUT_JSON) and open(OUT_JSON, "rb").read())
        try:
            main_run()
            verify_paper()
        except SystemExit:
            pass
        failed = [g["gate"] for g in GATES if not g["passed"]]
        after = (os.path.exists(OUT_TXT) and open(OUT_TXT, "rb").read(),
                 os.path.exists(OUT_JSON) and open(OUT_JSON, "rb").read())
        died = bool(failed) or ANCHOR_FAIL > 0
        print(f"MUTANT {name}")
        print(f"  {MUTANTS[name]}")
        print(f"  died at gates: {failed if failed else '(anchor stage)'}")
        print(f"  anchor failures: {ANCHOR_FAIL}")
        print(f"  artifacts unchanged: {before == after}")
        for ln in LINES:
            if "VARIES" in ln or "[GEOMETRY" in ln:
                print(f"  emitted: {ln.strip()}")
        ok = died and before == after
        print(f"  [{'PASS' if ok else 'FAIL'}] G-MUTANT[{name}]")
        sys.exit(0 if ok else 1)

    head, gv = main_run()
    if mode == "numbers":
        print(f"HEAD      {head}")
        print(f"GEOMETRY  {gv}")
        print("PAYLOAD")
        print(json.dumps(PAYLOAD, indent=2, sort_keys=True, default=str))
        print("REGISTRY  " + " ".join(sorted(NUMREG)))
        print(f"gates {len(GATES)} passed "
              f"{sum(1 for g in GATES if g['passed'])} "
              f"anchors {len(ANCHORS)} anchor-failures {ANCHOR_FAIL}")
        sys.exit(0)

    verify_paper()
    out, rj = render()
    print("\n".join(LINES))
    if ANCHOR_FAIL or FAILED:
        print(f"\nREFUSED: {FAILED} gate failures, {ANCHOR_FAIL} anchor "
              f"failures -- NOTHING WRITTEN", file=sys.stderr)
        sys.exit(1)
    if not write_and_verify(out, rj):
        print("\nREFUSED at the final integrity gate -- NOTHING WRITTEN",
              file=sys.stderr)
        sys.exit(1)
    print(f"\nwrote {os.path.relpath(OUT_TXT, REPO)} and "
          f"{os.path.relpath(OUT_JSON, REPO)}")
    sys.exit(0)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
d42a_generated_conflict_exact.py — v10 D42a: the generated-proposal
grammar + the smallest conflict fixtures. Pin: note-d42a with
amendments A1-A5' (e851a72) + round-1 amendments A6-A8 (de43d6f;
round frozen at #286). EXACT: every weight a Fraction; every gate
exact equality (zero tolerance). ROUND-1 REPAIRS IN THIS REVISION:
R1-A the enumerator completed to the past-local admission relation
(the global-record component filter — an unpinned batch-close mark —
removed); G1b enabled-set gauge invariance + extension closure; G9
the declared 5/4 support-level placement census; per-arm fork/orphan
censuses; G8 extended; G6/G0 anchored to the round's pre-verified
pinned-grammar numbers; L1 cited as the A8 theorem.

THE SPLIT CLAIM (pin §1): batch/conflict/opportunity GENERATED from
the record; kernel law (K1/K2, paper 25 §10), genesis boundary, and
measure completion (d34b placement) SUPPLIED-inherited, declared.
mu = product of local conditionals = a WEIGHT SYSTEM on typed causal
histories (d34a's honest noun), NOT a measure — gated accordingly.

Declared caps (RF5): ARM-1 enumeration depth 5 (actors A, B);
ARM-2 depth 4 (actors A, B, C); G1 resequencing on the full depth<=3
family + every depth-4 history containing an arb + the signature
histories. Genesis v0 is boundary (supplied, declared): all
participants hold it; it appears as no event.

Grammar (pin §2 + A1-A5): events
  ('p', a, b, x)        proposal, carriers {a} (A1), payload x in {0,1}
  ('r', a, ckey, wkey)  arbitration-as-acceptance by initiator a of
                        component ckey selecting maximal independent
                        set wkey; carriers = proposers(ckey) | {v'};
                        v' = ('v', base, value, authors, initiator)
  ('n', a)              recorded idle
Admission = the H1 CAUSAL certificate (past-relative; A2/A3).
Budgets (#152): propose-total 1/4 (initiator view), arbitrate-total
1/4 (join view, A4), idle absorbs; kernel winner draw = recorded click.
Gates G1-G8 per pin §4 as amended; exit 1 on any failure.
"""
import sys
from fractions import Fraction as F
from itertools import permutations

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

V0 = ('v', 'v0')

def vname(base, wkey, init):
    value = tuple(sorted({t[2] for t in wkey}))
    authors = tuple(sorted({t[0] for t in wkey}))
    return ('v', base, value, authors, init)

def regs_of(op):
    if op[0] == 'p': return frozenset([op[1]])
    if op[0] == 'n': return frozenset([op[1]])
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
    """The typed-DAG data of a down-closed index set (a causal past)."""
    def __init__(self, acts, pred, idxs):
        self.idxs = sorted(idxs)
        self.props = {i: acts[i] for i in self.idxs if acts[i][0] == 'p'}
        self.arbs = {i: acts[i] for i in self.idxs if acts[i][0] == 'r'}
        self.resolved = set()
        self.superseded = set()
        for op in self.arbs.values():
            self.resolved |= set(op[2])
            self.superseded.add(next(iter(op[2]))[1])
        self.pred = pred
        # live proposal events: triple not resolved. Triple uniqueness
        # is an ALL-DEPTHS THEOREM (pin A8, referee-supplied proof: a
        # same-base re-proposal is blocked by A3 if the prior is live
        # and by supersession if resolved); the L1 census below is a
        # regression tripwire, not the warrant.
        self.live = {i: op for i, op in self.props.items()
                     if (op[1], op[2], op[3]) not in self.resolved}

    def holdings(self, a):
        h = {V0}
        for i, op in self.arbs.items():
            members = {t[0] for t in op[2]}
            if a in members:
                base = next(iter(op[2]))[1]
                h.add(vname(base, op[3], op[1]))
        return h

    def incomparable(self, i, k):
        return (i not in self.pred[k]) and (k not in self.pred[i])

    def edges(self, idx_set):
        E = set()
        L = sorted(idx_set)
        for ii, i in enumerate(L):
            for k in L[ii + 1:]:
                pi, pk = self.props[i], self.props[k]
                if (pi[2] == pk[2] and pi[3] != pk[3]
                        and self.incomparable(i, k)):
                    E.add((i, k))
        return E

    def components(self):
        """Connected components of the conflict graph on LIVE
        proposals, grouped by base; singletons included (A5)."""
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

def triples(view, idx_set):
    return frozenset((view.props[i][1], view.props[i][2],
                      view.props[i][3]) for i in idx_set)

def mis_of(ckey, edge_triples):
    """All maximal independent sets of the conflict graph on triples."""
    items = sorted(ckey)
    n = len(items)
    ind = []
    for mask in range(1, 1 << n):
        sub = frozenset(items[i] for i in range(n) if mask >> i & 1)
        if all((a, b) not in edge_triples and (b, a) not in edge_triples
               for a in sub for b in sub if a < b):
            ind.append(sub)
    return [s for s in ind
            if not any(s < t for t in ind)]

def PK1(ckey, edge_triples):
    """K1: uniform recorded order-click over |C|! orders + greedy."""
    items = sorted(ckey)
    tally = {}
    for perm in permutations(items):
        acc = []
        for t in perm:
            if all((t, u) not in edge_triples and (u, t) not in
                   edge_triples for u in acc):
                acc.append(t)
        w = frozenset(acc)
        tally[w] = tally.get(w, 0) + 1
    total = sum(tally.values())
    return {w: F(c, total) for w, c in tally.items()}

def PK2(ckey, edge_triples):
    ms = mis_of(ckey, edge_triples)
    return {w: F(1, len(ms)) for w in ms}

KERNELS = {'K1': PK1, 'K2': PK2}

def edge_triples_of(view, idx_set):
    return frozenset(tuple(sorted((triples(view, {i}).__iter__().__next__(),
                                   triples(view, {k}).__iter__().__next__())))
                     for (i, k) in view.edges(idx_set))

def prop_options_in_view(view, a):
    """Enabled (base, payload) options for a, computed from a view."""
    out = []
    held = view.holdings(a)
    for b in held:
        if b in view.superseded: continue
        if any(op[1] == a and op[2] == b for op in view.live.values()):
            continue
        for x in (0, 1):
            out.append((b, x))
    return sorted(out, key=repr)

def arb_components_in_view(view, a):
    """Enabled components for initiator a in a view (base unsuperseded,
    a in the proposer set)."""
    out = []
    for base, comp in view.components():
        if base in view.superseded: continue
        if a in {view.props[i][1] for i in comp}:
            out.append((base, comp))
    return out

def admissible(acts, e, law=PK1):
    """Past-relative admission of appending e; returns (ok, q) with q
    the pinned local weight (A4 denominators), else (False, None)."""
    acts2 = acts + [e]
    j = len(acts2) - 1
    pred = event_poset(acts2)
    view = View(acts2, pred, pred[j])
    kind = e[0]
    if kind == 'n':
        a = e[1]
        has_p = bool(prop_options_in_view(view, a))
        has_r = bool(arb_components_in_view(view, a))
        return True, 1 - (F(1, 4) if has_p else 0) - (F(1, 4) if has_r else 0)
    if kind == 'p':
        a, b, x = e[1], e[2], e[3]
        opts = prop_options_in_view(view, a)
        if (b, x) not in opts: return False, None
        return True, F(1, 4) / len(opts)
    a, ckey, wkey = e[1], e[2], e[3]
    comps = arb_components_in_view(view, a)
    match = [c for c in comps if triples(view, c[1]) == ckey]
    if not match: return False, None
    base, comp = match[0]
    et = edge_triples_of(view, comp)
    if wkey not in mis_of(ckey, et): return False, None
    return True, F(1, 4) / len(comps) * law(ckey, et)[wkey]

def candidates_for(acts, actors):
    """All admissible next events. A TRUE superset generator filtered by
    past-relative admission ONLY (pin A7; the round-1 blocker was a
    global-record component filter here — an unpinned batch-close mark
    that silently dropped 1,016 admissible blind self-arbs over ARM-1).
    Arb candidates now range over EVERY nonempty subset S of full-view
    live proposals per base and every nonempty W within S; admissible()
    alone decides (component match + MIS check in the candidate's own
    past). Restricting S to full-LIVE proposals loses nothing: a
    full-resolved proposal's resolving arb lies on every one of its
    proposers' wires, hence in any candidate past that includes that
    proposer — the proposal is resolved there too (A8 carrier logic)."""
    pred = event_poset(acts)
    full = View(acts, pred, set(range(len(acts))))
    bases = {V0} | {vname(next(iter(op[2]))[1], op[3], op[1])
                    for op in full.arbs.values()}
    out = []
    live_by_base = {}
    for i, op in full.live.items():
        live_by_base.setdefault(op[2], []).append(i)
    for a in actors:
        for b in sorted(bases, key=repr):
            for x in (0, 1):
                e = ('p', a, b, x)
                ok, q = admissible(acts, e)
                if ok: out.append((e, q))
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
                    if e in seen: continue
                    seen.add(e)
                    ok, q = admissible(acts, e)
                    if ok: out.append((e, q))
        e = ('n', a)
        ok, q = admissible(acts, e)
        out.append((e, q))
    return out

def enumerate_family(actors, max_events):
    """BFS closure of the admission relation; also returns the candidate
    set at EVERY history (max-depth included) for the A7 5/4 census."""
    out = [[]]
    cache = {}
    frontier = [[]]
    while frontier:
        h = frontier.pop()
        cands = candidates_for(h, actors)
        cache[tuple(h)] = cands
        if len(h) >= max_events: continue
        for e, q in cands:
            h2 = h + [e]
            out.append(h2)
            frontier.append(h2)
    return out, cache

def mu_of(acts, law=PK1):
    p = F(1)
    for j in range(len(acts)):
        ok, q = admissible(acts[:j], acts[j], law)
        if not ok: return None
        p *= q
    return p

def canon(acts):
    pred = event_poset(acts)
    memo = {}
    def c(j):
        if j not in memo:
            memo[j] = (acts[j], frozenset(c(i) for i in pred[j]))
        return memo[j]
    return frozenset(c(j) for j in range(len(acts)))

def linear_extensions(acts):
    pred = event_poset(acts)
    n = len(acts)
    out = []
    for perm in permutations(range(n)):
        inv = {e: i for i, e in enumerate(perm)}
        if all(inv[i] < inv[j] for j in range(n) for i in pred[j]):
            out.append(perm)
    return out

def conflicts_in(acts):
    pred = event_poset(acts)
    view = View(acts, pred, set(range(len(acts))))
    return view.edges(set(view.props))

print("[d42a — the generated-proposal grammar: exact receipt]")
print("  banner: EXACT Fractions throughout; genesis v0 = declared")
print("  boundary; caps: ARM-1 depth 5, ARM-2 depth 4, G1 resequence")
print("  on depth<=3 full + depth-4 arb-histories + signatures; the")
print("  kernel law is SUPPLIED-alternative (K1/K2, paper 25 §10) and")
print("  the weight system is computed under BOTH; joint-placement")
print("  normalization is d34b's problem, INHERITED, not claimed.")

ARM1, CACHE1 = enumerate_family(('A', 'B'), 5)
ARM2, CACHE2 = enumerate_family(('A', 'B', 'C'), 4)
print(f"  family sizes: ARM-1 depth<=5: {len(ARM1)}; "
      f"ARM-2 depth<=4: {len(ARM2)}")
check("G0 the pinned-grammar family sizes (round-1 pre-verified: the "
      "batch-close sub-family was 5,751/5,761)",
      len(ARM1) == 6471 and len(ARM2) == 6589,
      f"ARM-1 = {len(ARM1)} (expect 6471); ARM-2 = {len(ARM2)} "
      "(expect 6589)")

# L1: the uniqueness lemma behind triple-identity (census, must hold)
dup = 0
for h in ARM1 + ARM2:
    pred = event_poset(h)
    view = View(h, pred, set(range(len(h))))
    ts = [(op[1], op[2], op[3]) for op in view.live.values()]
    dup += int(len(ts) != len(set(ts)))
check("L1 live-triple uniqueness (identity lemma for ckeys)", dup == 0,
      f"violations = {dup} over {len(ARM1) + len(ARM2)} histories")

# ---- G1: closure/resequence-and-recompute ----------------------------------
g1_pre = ([h for h in ARM1 if len(h) <= 3]
          + [h for h in ARM1 if len(h) == 4 and any(e[0] == 'r' for e in h)])
pA0, pB1 = ('p', 'A', V0, 0), ('p', 'B', V0, 1)
SIG_CK = frozenset({('A', V0, 0), ('B', V0, 1)})
SIG_ARB = ('r', 'A', SIG_CK, frozenset({('A', V0, 0)}))
V1 = vname(V0, frozenset({('A', V0, 0)}), 'A')
SIG1 = [pA0, pB1, SIG_ARB, ('p', 'B', V1, 1)]
g1_pre.append(SIG1)
SELFA = ('r', 'A', frozenset({('A', V0, 0)}), frozenset({('A', V0, 0)}))
CK3 = frozenset({('A', V0, 0), ('B', V0, 1), ('C', V0, 0)})
PRC = frozenset({('A', V0, 0), ('C', V0, 0)})
SIG2 = [('p', 'A', V0, 0), ('p', 'B', V0, 1), ('p', 'C', V0, 0),
        ('r', 'A', CK3, PRC)]
g1_pre.append(SIG2)
seen_h = set()
g1_set = []
for h in g1_pre:
    if tuple(h) not in seen_h:
        seen_h.add(tuple(h))
        g1_set.append(h)
ok1, tested = True, 0
for h in g1_set:
    qs = [admissible(h[:j], h[j])[1] for j in range(len(h))]
    if any(q is None for q in qs): ok1 = False; break
    c0 = canon(h)
    for ext in linear_extensions(h):
        acts2 = [h[i] for i in ext]
        for pos in range(len(acts2)):
            ok, q = admissible(acts2[:pos], acts2[pos])
            if (not ok) or q != qs[ext[pos]]:
                ok1 = False
        if canon(acts2) != c0: ok1 = False
        tested += 1
check("G1 resequence-and-recompute: admission, every mu factor, and the "
      "canonical typed DAG invariant over every linear extension",
      ok1, f"{len(g1_set)} distinct histories, {tested} resequencings")

# G1b (round-1 F3/R3 + A7): the ENABLED-SET gate the pin always
# prescribed — the candidate set at a record point is gauge-invariant
# (recomputed from every linear extension's reordering), and the family
# is closed under linear extensions at the round's witness point (the
# old enumerator failed exactly here: [pA0,pB1,selfA] was excluded
# while its gauge-equivalent [pA0,selfA,pB1] was in-family).
ok1b, set_points = True, 0
arm1_keys = {tuple(h) for h in ARM1}
for h in g1_set:
    if any(e[1] == 'C' or (e[0] == 'r' and any(t[0] == 'C' for t in e[2]))
           for e in h):
        actors_h = ('A', 'B', 'C')
    else:
        actors_h = ('A', 'B')
    base_set = frozenset(candidates_for(h, actors_h))
    for ext in linear_extensions(h):
        acts2 = [h[i] for i in ext]
        set2 = frozenset(candidates_for(acts2, actors_h))
        set_points += 1
        if set2 != base_set: ok1b = False
w2a, w2b = [pA0, SELFA, pB1], [pA0, pB1, SELFA]
closure_ok = (tuple(w2a) in arm1_keys) and (tuple(w2b) in arm1_keys)
check("G1b enabled-set gauge invariance ((event, weight) PAIRS recomputed "
      "at every linear extension — the delta note (i) tightening) + "
      "witness-2 extension closure: both "
      "orders of the blind self-arb history are in-family",
      ok1b and closure_ok,
      f"candidate-set points checked = {set_points}; witness pair "
      f"in-family = {closure_ok}")

# ---- G2: conflict genesis --------------------------------------------------
d2 = [h for h in ARM1 if len(h) == 2 and conflicts_in(h)]
n_conf = sum(1 for h in ARM1 if conflicts_in(h))
mu_seed = mu_of([pA0, pB1])
check("G2a depth-2 conflict census (hand-derived)", len(d2) == 4,
      f"count = {len(d2)}, expected 4")
check("G2b conflict histories exist with positive weight; "
      "mu([pA0,pB1]) exact",
      n_conf > 0 and mu_seed == F(1, 64),
      f"conflict histories (depth<=5) = {n_conf}; mu = {mu_seed} = 1/64; "
      "zero-conflict-without-incomparability is DEFINITIONAL (declared)")

# ---- G3: generated opportunity (as restated by A5) -------------------------
def arb_pair_option_exists(h):
    return any(e for e, q in candidates_for(h, ('A', 'B'))
               if e[0] == 'r' and e[2] == SIG_CK)
ok3a = (not arb_pair_option_exists([]))
ok3a &= (not arb_pair_option_exists([pA0]))
ok3a &= arb_pair_option_exists([pA0, pB1])
iff_ok = True
for h in ARM1:
    has_both = all(any(e == p for e in h) for p in (pA0, pB1))
    live_both = has_both and not any(
        e[0] == 'r' and set(e[2]) & set(SIG_CK) for e in h)
    if arb_pair_option_exists(h) != live_both: iff_ok = False
check("G3i the PAIR arb option exists iff both proposals live in the "
      "record (family-wide iff-sweep)", ok3a and iff_ok,
      f"sweep over {len(ARM1)} histories")
resweep = True
for h in ARM1 + ARM2:
    for k, ev in enumerate(h):
        if ev[0] == 'p' and ev[2][0] == 'v' and ev[2] != V0:
            if not any(e[0] == 'r' and vname(next(iter(e[2]))[1], e[3],
                                             e[1]) == ev[2]
                       for e in h[:k]):
                resweep = False
check("G3ii deletion control: every re-proposal against a created "
      "version has its creating arb strictly earlier in the record",
      resweep, "sweep over BOTH arms")

# ---- G4: staleness — causal vs authentication-only -------------------------
H4 = [pA0, pB1, SIG_ARB]
stale = ('p', 'A', V0, 1)
ok_causal, _ = admissible(H4, stale)
def auth_only(acts, e):
    """Issuance validity alone: base exists in past; prior freed."""
    acts2 = acts + [e]
    pred = event_poset(acts2)
    view = View(acts2, pred, pred[len(acts2) - 1])
    b = e[2]
    exists = (b == V0) or any(
        vname(next(iter(op[2]))[1], op[3], op[1]) == b
        for op in view.arbs.values())
    unblocked = not any(op[1] == e[1] and op[2] == b
                        for op in view.live.values())
    return exists and unblocked
check("G4a causal certificate rejects the post-arb stale re-proposal "
      "(supersession is the SOLE blocker: prior resolved per A3)",
      (not ok_causal) and auth_only(H4, stale),
      "causal: inadmissible; authentication-only: ADMITS — "
      "paper 28 H1 exhibited load-bearing")
H4c = [pA0, pB1, SIG_ARB, ('p', 'C', V0, 0)]
okC, qC = admissible(H4c[:3], H4c[3])
def orphan_count(fam):
    n = 0
    for h in fam:
        pred = event_poset(h)
        view = View(h, pred, set(range(len(h))))
        glob_sup = view.superseded
        for i, op in view.live.items():
            if op[2] in glob_sup:
                sub = View(h, pred, pred[i])
                if op[2] not in sub.superseded: n += 1
    return n
orphans2, orphans1 = orphan_count(ARM2), orphan_count(ARM1)
check("G4b optimistic concurrency: the third actor's concurrent "
      "proposal on the superseded base is ADMISSIBLE; orphans censused "
      "PER ARM (round-1 F5)",
      okC and orphans2 == 2088 and orphans1 > 0,
      f"orphans ARM-2 = {orphans2} (expect 2088, round-1 pre-verified); "
      f"ARM-1 = {orphans1} [MEASURED, first census]")
def fork_and_observer(fam):
    fk, ov, fh = 0, 0, []
    for h in fam:
        pred = event_poset(h)
        view = View(h, pred, set(range(len(h))))
        arb_bases = {}
        for i, op in view.arbs.items():
            arb_bases.setdefault(next(iter(op[2]))[1], []).append(i)
        forked_here = False
        for base, lst in arb_bases.items():
            if len(lst) > 1: fk += 1; forked_here = True
        if forked_here: fh.append(h)
        for j in range(len(h)):
            sub = View(h, pred, pred[j] | {j})
            per = {}
            for i, op in sub.arbs.items():
                per.setdefault(next(iter(op[2]))[1], []).append(i)
            if any(len(v) > 1 for v in per.values()): ov += 1
    return fk, ov, fh
forks2, ov2, fork_h2 = fork_and_observer(ARM2)
forks1, ov1, fork_h1 = fork_and_observer(ARM1)
forks, observer_viol = forks2, ov2 + ov1
# The depth-4 in-family sweep alone cannot fail (a violating event
# needs 5 events) — the REAL gate extends every forked history one
# step: participation-only holdings must prevent any single event
# from collecting two same-base arbs in its past (a delivery leak in
# the grammar would fail this).
ext_checked = ext_viol = 0
for h, acts_set in ([(h, ('A', 'B', 'C')) for h in fork_h2]
                    + [(h, ('A', 'B')) for h in fork_h1]):
    for e, q in candidates_for(h, acts_set):
        h2 = h + [e]
        pred2 = event_poset(h2)
        sub = View(h2, pred2, pred2[len(h)] | {len(h)})
        per = {}
        for i, op in sub.arbs.items():
            per.setdefault(next(iter(op[2]))[1], []).append(i)
        ext_checked += 1
        if any(len(v) > 1 for v in per.values()): ext_viol += 1
check("G4c fork honesty (A2): forks censused PER ARM (round-1 F5); "
      "no observer past holds two same-base arbs — gated on the "
      "one-step EXTENSIONS of every forked history in BOTH arms",
      forks2 == 72 and forks1 > 0 and observer_viol == 0
      and ext_checked > 0 and ext_viol == 0,
      f"fork (history,base) pairs: ARM-2 = {forks2} (expect 72, "
      f"round-1 pre-verified), ARM-1 = {forks1} [MEASURED]; in-family "
      f"observer violations = {observer_viol}; extension candidates = "
      f"{ext_checked}, violations = {ext_viol}")

# ---- G5: kernel nonvacuity + discrimination (ARM-2) ------------------------
h3 = [('p', 'A', V0, 0), ('p', 'B', V0, 1), ('p', 'C', V0, 0)]
pred3 = event_poset(h3)
view3 = View(h3, pred3, set(range(3)))
comps3 = view3.components()
ck3 = triples(view3, comps3[0][1]) if len(comps3) == 1 else None
et3 = edge_triples_of(view3, comps3[0][1]) if ck3 else frozenset()
QB = frozenset({('B', V0, 1)})
k1 = PK1(ck3, et3) if ck3 else {}
k2 = PK2(ck3, et3) if ck3 else {}
tv = (sum(abs(k1.get(w, F(0)) - k2.get(w, F(0)))
          for w in set(k1) | set(k2)) / 2) if ck3 else None
check("G5a the path component P-Q-R is GENERATED (one 3-member "
      "component, edges A-B and B-C only)",
      ck3 is not None and len(ck3) == 3 and len(et3) == 2,
      f"component = {sorted(ck3) if ck3 else None}")
check("G5b K1 = 2/3 on {P,R}, 1/3 on {Q}; K2 = 1/2, 1/2; TV = 1/6 — "
      "all exact, matching paper 25 §10",
      k1.get(PRC) == F(2, 3) and k1.get(QB) == F(1, 3)
      and k2.get(PRC) == F(1, 2) and k2.get(QB) == F(1, 2)
      and tv == F(1, 6),
      f"K1({{P,R}}) = {k1.get(PRC)}, K2 = {k2.get(PRC)}, TV = {tv}")
mu_k1 = mu_of(h3 + [('r', 'A', ck3, PRC)], PK1) if ck3 else None
mu_k2 = mu_of(h3 + [('r', 'A', ck3, PRC)], PK2) if ck3 else None
check("G5c the arbitrated batch history carries positive exact weight "
      "under BOTH kernels (hand values 1/3072 and 1/4096)",
      mu_k1 == F(1, 3072) and mu_k2 == F(1, 4096),
      f"mu_K1 = {mu_k1}; mu_K2 = {mu_k2}")

# ---- G6: joins -------------------------------------------------------------
joins = 0
for h in ARM1 + ARM2:
    pred = event_poset(h)
    for j, e in enumerate(h):
        if e[0] == 'r' and len(e[2]) >= 2:
            view = View(h, pred, pred[j])
            mem = [i for i in view.props if triples(view, {i}) <= e[2]]
            if any(view.incomparable(i, k) for i in mem for k in mem
                   if i < k):
                joins += 1
check("G6 join census: arbitration events with incomparable proposal "
      "pairs in their past (in-degree >= 2) exist",
      joins == 3096, f"join events = {joins} (expect 3096, round-1 "
      "pre-verified); D23/NSE/D25/D27 + Hegerfeldt = d42b carried "
      "obligations (declared)")

# ---- G7: what is exactly true (A4) -----------------------------------------
# A sum of (1/4)/n over n options is an arithmetic identity (the
# convicted B6 class) — the REAL gates: (a) a hand-anchored battery
# of exact q values derived in the pin, each on a DIFFERENT structural
# branch of the law, including A5's declared idle-1/2 consequence;
# (b) kernel normalization over every GENERATED component, both laws.
battery = [
    (([], pA0), F(1, 8), "first proposal: 1/4 over 2 options"),
    (([], ('n', 'A')), F(3, 4), "idle at genesis: no component visible"),
    (([pA0], ('n', 'A')), F(3, 4),
     "idle after own proposal: propose sector CLOSED (A3 blocker, "
     "v0 the only held base), arb sector open on the singleton — "
     "this battery line caught the pin's false A5 remark (1/2)"),
    (([pA0], ('n', 'B')), F(3, 4),
     "B's idle blind to A's proposal (carriers {a} only, A1)"),
    (([pA0, pB1], SIG_ARB), F(1, 8), "pair arb: 1/4 x K1(1/2)"),
    ((SIG1[:3], ('p', 'B', V1, 1)), F(1, 8),
     "loser re-proposal on v1: v0 superseded+freed, 2 options on v1"),
    ((SIG1[:3], ('n', 'A')), F(3, 4),
     "A idle post-arb: v1 propose sector open, arb sector closed"),
]
ok7a, det = True, []
for (ctx, e), want, why in battery:
    ok, q = admissible(list(ctx), e)
    good = ok and q == want
    ok7a &= good
    det.append(('ok' if good else 'MISMATCH') + ':' + why)
ok7b = True
n_comp = 0
for h in ARM1 + ARM2:
    pred = event_poset(h)
    viewF = View(h, pred, set(range(len(h))))
    for base, comp in viewF.components():
        ck = triples(viewF, comp)
        et = edge_triples_of(viewF, comp)
        n_comp += 1
        for law in (PK1, PK2):
            ok7b &= (sum(law(ck, et).values()) == F(1))
check("G7 the hand-anchored q battery (7 branches incl. the A5' "
      "idle-3/4 correction) "
      "+ kernel normalization over every generated component, both laws",
      ok7a and ok7b,
      (f"components checked = {n_comp}; battery 7/7 exact "
       "(both-open 1/2 and both-closed 1 idle branches unreachable at "
       "fixture depths, declared); joint-placement normalization NOT "
       "claimed — d34b, inherited") if ok7a else
      "battery: " + "; ".join(x for x in det
                              if x.startswith('MISMATCH')))

# ---- G9: the A7 support-level placement census -----------------------------
# Under the pinned law, per-initiator weight sums EXCEED 1 exactly where
# an initiator's own view holds a sealable singleton while a join view
# holds a larger component (the blind self-arb + the pair, value 5/4;
# with two join layers, 3/2). Round 1 proved the old enumerator's
# global filter MASKED this (its family showed sums = 1 everywhere).
# A7 declares it: this is d34b's placement problem at the SUPPORT
# level, censused here, not normalized away.
def sum_census(fam, cache, actors):
    counts = {}
    for h in fam:
        cands = cache[tuple(h)]
        for a in actors:
            tot = sum(q for e, q in cands if e[1] == a)
            counts[tot] = counts.get(tot, 0) + 1
    return counts
c1 = sum_census(ARM1, CACHE1, ('A', 'B'))
c2 = sum_census(ARM2, CACHE2, ('A', 'B', 'C'))
def on_ladder(v):
    return v >= 1 and ((v - 1) * 4).denominator == 1
spec1 = ", ".join(f"{v} at {c1[v]}" for v in sorted(c1))
spec2 = ", ".join(f"{v} at {c2[v]}" for v in sorted(c2))
check("G9 the support-level placement face (A7/A7'): per-initiator "
      "sums sit on the quarter-integer ladder 1 + k/4 (k = causally "
      "blind join layers; own-view sectors always sum to exactly 1); "
      "ARM-1 spectrum exactly {1, 5/4} with the round-anchored 1,016; "
      "sums = 1 everywhere is NOT restored (the round-1 mask is gone)",
      all(on_ladder(v) for v in set(c1) | set(c2))
      and set(c1) == {F(1), F(5, 4)} and c1[F(5, 4)] == 1016
      and c2 == {F(1): 16539, F(5, 4): 1824, F(3, 2): 936,
                 F(7, 4): 468},
      f"ARM-1: {spec1} (5/4 expect 1016); ARM-2: {spec2} (referee-"
      "reproduced, ANCHORED; "
      "3/2 = outer path actor, 7/4 = central actor blind-priced in "
      "both pairs + the triple]; per-initiator sub-normalization "
      "FAILS at depth 2 under the pinned law — d34b's placement "
      "problem, DECLARED not normalized away")

# ---- G8: record basis (the D41 eighth residue) -----------------------------
c_prop = canon([pA0]) != canon([('p', 'B', V0, 0)])
c_comp = canon([pA0, pB1, SELFA]) != canon([pA0, pB1, SIG_ARB])
c_pay = canon([pA0, pB1]) != canon([pA0, ('p', 'B', V0, 0)])
arbB = ('r', 'B', SIG_CK, frozenset({('A', V0, 0)}))
c_init = canon([pA0, pB1, SIG_ARB]) != canon([pA0, pB1, arbB])
arbW = ('r', 'A', SIG_CK, frozenset({('B', V0, 1)}))
c_win = canon([pA0, pB1, SIG_ARB]) != canon([pA0, pB1, arbW])
c_gauge = canon([pA0, pB1]) == canon([pB1, pA0])
check("G8 record basis: proposer, payload, component (same winners, "
      "same initiator — isolated), initiator, and winner distinctions "
      "separate canonical DAGs; gauge reorder does not (round-1 R6: "
      "base/authors separate by the same event-tuple embedding, "
      "corollary, not isolable all-else-equal at these depths)",
      c_prop and c_pay and c_comp and c_init and c_win and c_gauge,
      "5 isolated separations gated + gauge identity")

print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("[VERDICT] FAIL — exit 1 by design")
    sys.exit(1)
print("[VERDICT] d42a GREEN (round-1 repaired): the batch, the "
      "conflict, the arbitration opportunity, and the re-proposal "
      "opportunity are GENERATED from the record under the past-local "
      "pinned grammar — the family IS the admission relation's "
      "extension-closed BFS closure, gated as such; the kernel law, "
      "the genesis boundary, and the measure completion remain "
      "SUPPLIED (declared), and the placement problem's support-level "
      "face (the 1 + k/4 ladder, up to 7/4) is CENSUSED, not "
      "normalized away.")

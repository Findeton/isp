#!/usr/bin/env python3
"""
d42b1_transport_exact.py — v10 D42b1: the transport-and-reconciliation
grammar (d42b fronts 1-3 as one extension). Pin: note-d42b1 (fda11b2),
on top of the d42a terminal grammar (note-d42a + A1-A8, #289). EXACT:
every weight a Fraction; every gate exact equality (zero tolerance).

PINNED PREDICTIONS UNDER TEST (pin §1, stated before this file ran):
P1 the starvation theorem (delivery-free non-participants never hold
created versions); P2 delivery KILLS per-observer fork-freeness (the
d42a theorem is a starved-sub-grammar artifact); P3 the merge
opportunity is generated exactly at two-fork observer pasts; P4
orphans are informational (delivered supersession kills, delivered
successor rescues — one delivery does both); P5 L1 and the 1+k/4
ladder survive.

Declared caps (RF3/RF5, tuned and printed): ARM-1T (A,B) depth <= 4;
ARM-2T (A,B,C) depth <= 3; the deep physics (P2/P3/P4) rides on the
CONSTRUCTED signature chains SIG-FM (fork->deliver->merge->rescue)
and SIG-KR (orphan kill-and-rescue), every event admission-checked
and priced exactly, every prefix's option set gated. Genesis v0 =
declared boundary. Weight-system level only (RF4): no measure claim;
the placement front (d42b3) owns normalization; the 1+k/4 ladder is
censused per A7/A7'.

New grammar (pin §2; d42a events unchanged):
  ('d', s, r, v)   delivery; carriers {s, r} — a JOIN of knowledge;
                   re-delivery admissible and physical; r holds v
                   after; supersessions travel with the join.
  ('m', a, pk, w)  merge by the holder of both versions of pk (sorted
                   pair), carriers {a, v_m}; same-base arb/merge-
                   created, incomparable creations, neither superseded;
                   value conflict -> w in pk at the 1/2 pair click;
                   equal values -> canonical union, single option;
                   v_m = ('v','m',pk,value,a) supersedes both members.
Budgets: propose 1/4 | arb-and-merge 1/4 (components join-view +
pairs initiator-view) | deliver 1/4 (sender-view) | idle absorbs.
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

def mname(pk, value, init):
    return ('v', 'm', pk, value, init)

def value_of(v):
    if v == V0: return None
    return v[3] if v[1] == 'm' else v[2]

def base_of(v):
    """The original base lineage of a created version (recursive
    through merges); None for genesis."""
    if v == V0: return None
    if v[1] == 'm': return base_of(v[2][0])
    return v[1]

def regs_of(op):
    k = op[0]
    if k == 'p' or k == 'n': return frozenset([op[1]])
    if k == 'd': return frozenset([op[1], op[2]])
    if k == 'm': return frozenset([op[1], mname(op[2], None, op[1])[:2]
                                   + (op[2],)])
    props = {t[0] for t in op[2]}
    base = next(iter(op[2]))[1]
    return frozenset(props | {vname(base, op[3], op[1])})

def regs_of(op):
    k = op[0]
    if k == 'p' or k == 'n': return frozenset([op[1]])
    if k == 'd': return frozenset([op[1], op[2]])
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
    """Typed-DAG data of a down-closed index set (a causal past)."""
    def __init__(self, acts, pred, idxs):
        self.idxs = sorted(idxs)
        self.pred = pred
        self.props = {i: acts[i] for i in self.idxs if acts[i][0] == 'p'}
        self.arbs = {i: acts[i] for i in self.idxs if acts[i][0] == 'r'}
        self.dels = {i: acts[i] for i in self.idxs if acts[i][0] == 'd'}
        self.mrgs = {i: acts[i] for i in self.idxs if acts[i][0] == 'm'}
        self.resolved = set()
        self.superseded = set()
        self.created = {}         # version -> creating event index
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
        # live proposal events: triple not resolved. Uniqueness of live
        # triples is the A8 all-depths THEOREM (delivery only ADDS
        # knowledge; blocking is monotone in knowledge — pin P5); the
        # L1 census below is a regression tripwire, not the warrant.
        self.live = {i: op for i, op in self.props.items()
                     if (op[1], op[2], op[3]) not in self.resolved}

    def holdings(self, a):
        h = {V0}
        for i, op in self.arbs.items():
            if a in {t[0] for t in op[2]}:
                base = next(iter(op[2]))[1]
                h.add(vname(base, op[3], op[1]))
        for i, op in self.dels.items():
            if op[2] == a: h.add(op[3])
        for i, op in self.mrgs.items():
            if op[1] == a:
                pk, w = op[2], op[3]
                val = value_of(pk[0]) if w == 'both' else value_of(w)
                h.add(mname(pk, val, op[1]))
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
        """Enabled merge pairs for holder a IN THIS VIEW: both held,
        both created here, same base lineage, incomparable creations,
        neither superseded."""
        held = [v for v in self.holdings(a)
                if v in self.created and v not in self.superseded]
        out = []
        for ii, v1 in enumerate(sorted(held, key=repr)):
            for v2 in sorted(held, key=repr)[ii + 1:]:
                if base_of(v1) != base_of(v2): continue
                c1, c2 = self.created[v1], self.created[v2]
                if not self.incomparable(c1, c2): continue
                out.append(tuple(sorted((v1, v2), key=repr)))
        return out

def triples(view, idx_set):
    return frozenset((view.props[i][1], view.props[i][2],
                      view.props[i][3]) for i in idx_set)

def mis_of(ckey, edge_triples):
    items = sorted(ckey)
    n = len(items)
    ind = []
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
            if all((t, u) not in edge_triples and (u, t) not in
                   edge_triples for u in acc):
                acc.append(t)
        w = frozenset(acc)
        tally[w] = tally.get(w, 0) + 1
    total = sum(tally.values())
    return {w: F(c, total) for w, c in tally.items()}

def edge_triples_of(view, idx_set):
    def tri(i): return next(iter(triples(view, {i})))
    return frozenset(tuple(sorted((tri(i), tri(k))))
                     for (i, k) in view.edges(idx_set))

def prop_options_in_view(view, a):
    out = []
    for b in view.holdings(a):
        if b in view.superseded: continue
        if any(op[1] == a and op[2] == b for op in view.live.values()):
            continue
        for x in (0, 1):
            out.append((b, x))
    return sorted(out, key=repr)

def arb_components_in_view(view, a):
    out = []
    for base, comp in view.components():
        if base in view.superseded: continue
        if a in {view.props[i][1] for i in comp}:
            out.append((base, comp))
    return out

def deliver_options_in_view(view, a, actors):
    return sorted(((r, v) for r in actors if r != a
                   for v in view.holdings(a)), key=repr)

def own_view(acts, a):
    """The single-wire causal past of participant a (the initiator
    view): the past of a hypothetical next idle of a."""
    acts2 = acts + [('n', a)]
    pred = event_poset(acts2)
    return View(acts2, pred, pred[len(acts2) - 1])

def admissible(acts, e, actors, law=PK1):
    """Past-relative admission + the pinned local weight."""
    acts2 = acts + [e]
    j = len(acts2) - 1
    pred = event_poset(acts2)
    view = View(acts2, pred, pred[j])
    kind = e[0]
    if kind == 'n':
        a = e[1]
        has_p = bool(prop_options_in_view(view, a))
        has_am = bool(arb_components_in_view(view, a)
                      or view.merge_pairs(a))
        has_d = bool(deliver_options_in_view(view, a, actors))
        return True, (1 - (F(1, 4) if has_p else 0)
                      - (F(1, 4) if has_am else 0)
                      - (F(1, 4) if has_d else 0))
    if kind == 'p':
        a, b, x = e[1], e[2], e[3]
        opts = prop_options_in_view(view, a)
        if (b, x) not in opts: return False, None
        return True, F(1, 4) / len(opts)
    if kind == 'd':
        s, r, v = e[1], e[2], e[3]
        if r == s or r not in actors: return False, None
        sv = own_view(acts, s)
        opts = deliver_options_in_view(sv, s, actors)
        if (r, v) not in opts: return False, None
        return True, F(1, 4) / len(opts)
    if kind == 'm':
        a, pk, w = e[1], e[2], e[3]
        D = len(arb_components_in_view(view, a)) + len(view.merge_pairs(a))
        if pk not in view.merge_pairs(a): return False, None
        v1, v2 = pk
        if value_of(v1) != value_of(v2):
            if w not in pk: return False, None
            return True, F(1, 4) / D * F(1, 2)
        if w != 'both': return False, None
        return True, F(1, 4) / D
    a, ckey, wkey = e[1], e[2], e[3]
    comps = arb_components_in_view(view, a)
    match = [c for c in comps if triples(view, c[1]) == ckey]
    if not match: return False, None
    base, comp = match[0]
    et = edge_triples_of(view, comp)
    if wkey not in mis_of(ckey, et): return False, None
    D = len(comps) + len(view.merge_pairs(a))
    return True, F(1, 4) / D * law(ckey, et)[wkey]

def candidates_for(acts, actors):
    """TRUE superset generation (pin A7): proposals over all seen
    versions; arbs over every subset of full-live proposals per base x
    every winner subset; merges over every held created-version pair x
    winners; deliveries over holdings x receivers; idle. admissible()
    alone decides."""
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
                    ok, q = admissible(acts, e, actors)
                    if ok: out.append((e, q))
        held = sorted(full.holdings(a), key=repr)
        for ii, v1 in enumerate(held):
            for v2 in held[ii + 1:]:
                pk = tuple(sorted((v1, v2), key=repr))
                for w in (pk[0], pk[1], 'both'):
                    e = ('m', a, pk, w)
                    ok, q = admissible(acts, e, actors)
                    if ok: out.append((e, q))
        for r in actors:
            if r == a: continue
            for v in held:
                e = ('d', a, r, v)
                ok, q = admissible(acts, e, actors)
                if ok: out.append((e, q))
        e = ('n', a)
        ok, q = admissible(acts, e, actors)
        out.append((e, q))
    return out

def enumerate_family(actors, max_events):
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

def full_view(acts):
    pred = event_poset(acts)
    return View(acts, pred, set(range(len(acts))))

print("[d42b1 — transport and reconciliation: exact receipt]")
print("  banner: EXACT Fractions; genesis v0 = declared boundary;")
print("  caps (RF3/RF5, tuned + printed): ARM-1T (A,B) depth<=4,")
print("  ARM-2T (A,B,C) depth<=3; deep gates on constructed chains")
print("  SIG-FM and SIG-KR (admission-exact at every prefix); weight-")
print("  system level only — placement is d42b3's; ladder per A7/A7'.")

AB = ('A', 'B'); ABC = ('A', 'B', 'C')
ARM1, CACHE1 = enumerate_family(AB, 4)
ARM2, CACHE2 = enumerate_family(ABC, 3)
print(f"  family sizes [MEASURED, first run — round to anchor]: "
      f"ARM-1T = {len(ARM1)}; ARM-2T = {len(ARM2)}")

# ---- L1 tripwire ------------------------------------------------------------
dup = 0
for h in ARM1 + ARM2:
    view = full_view(h)
    ts = [(op[1], op[2], op[3]) for op in view.live.values()]
    dup += int(len(ts) != len(set(ts)))
check("L1 live-triple uniqueness tripwire (the A8 theorem extends: "
      "delivery only adds knowledge, blocking is monotone — pin P5)",
      dup == 0, f"violations = {dup} over {len(ARM1) + len(ARM2)}")

# ---- signature chains -------------------------------------------------------
pA0 = ('p', 'A', V0, 0)
pC1 = ('p', 'C', V0, 1)
tA = ('A', V0, 0); tC = ('C', V0, 1)
rA = ('r', 'A', frozenset({tA}), frozenset({tA}))
rC = ('r', 'C', frozenset({tC}), frozenset({tC}))
v1 = vname(V0, frozenset({tA}), 'A')
vC = vname(V0, frozenset({tC}), 'C')
dA = ('d', 'A', 'B', v1)
dC = ('d', 'C', 'B', vC)
PK = tuple(sorted((v1, vC), key=repr))
mB = ('m', 'B', PK, v1)
vm = mname(PK, value_of(v1), 'B')
SIG_FM = [pA0, pC1, rA, rC, dA, dC, mB, ('p', 'B', vm, 1)]

ok_chain = True
qs_fm = []
for j in range(len(SIG_FM)):
    ok, q = admissible(SIG_FM[:j], SIG_FM[j], ABC)
    ok_chain &= ok
    qs_fm.append(q)
check("SIG-FM admissible end-to-end (fork via blind self-arbs of a "
      "CONFLICTING pair; two deliveries; merge; rescue re-proposal)",
      ok_chain, "8 events, every admission past-relative")

# P2: the two-arb observer past
viewFM = full_view(SIG_FM)
pred_fm = event_poset(SIG_FM)
obs_two = 0
for j in range(len(SIG_FM)):
    sub = View(SIG_FM, pred_fm, pred_fm[j] | {j})
    per = {}
    for i, op in sub.arbs.items():
        per.setdefault(next(iter(op[2]))[1], []).append(i)
    if any(len(v) > 1 for v in per.values()): obs_two += 1
del_free_viol = 0
for h in ARM1 + ARM2:
    if any(e[0] == 'd' for e in h): continue
    pred = event_poset(h)
    for j in range(len(h)):
        sub = View(h, pred, pred[j] | {j})
        per = {}
        for i, op in sub.arbs.items():
            per.setdefault(next(iter(op[2]))[1], []).append(i)
        if any(len(v) > 1 for v in per.values()): del_free_viol += 1
check("P2 fork-freeness is a STARVATION ARTIFACT: the SIG-FM observer "
      "(B, post-deliveries) holds TWO same-base arbs in its past; the "
      "delivery-free sub-family stays at exact zero",
      obs_two > 0 and del_free_viol == 0,
      f"two-arb observer pasts on SIG-FM = {obs_two}; delivery-free "
      f"violations in-family = {del_free_viol} — the d42a G4c theorem "
      "is the delivery-free special case (pin P1/P2)")

# P3: the merge opportunity iff
def merge_opts_at(h, actors):
    return [e for e, q in candidates_for(h, actors) if e[0] == 'm']
m_before = merge_opts_at(SIG_FM[:5], ABC)   # only dA delivered
m_after = merge_opts_at(SIG_FM[:6], ABC)    # both delivered
iff_m = True
for k in range(len(SIG_FM)):
    opts = merge_opts_at(SIG_FM[:k], ABC)
    should = (k >= 6 and k < 7)  # exactly after both deliveries, before mB
    if k >= 7: should = False    # pair superseded by the merge itself
    if bool(opts) != should: iff_m = False
check("P3 the merge opportunity is GENERATED exactly at the two-fork "
      "observer past: absent before the second delivery, present "
      "after, gone once merged (prefix-exact iff on SIG-FM)",
      (not m_before) and len(m_after) == 2 and iff_m,
      f"options after both deliveries = {len(m_after)} (the two "
      "winner choices of the value-conflicted pair); merge q = "
      f"{[admissible(SIG_FM[:6], e, ABC)[1] for e in m_after]}")

# P4: one delivery kills the orphan AND rescues the proposer
pB1v0 = ('p', 'B', V0, 1)
SIG_KR = [pA0, rA, pB1v0, dA]
ok_kr = all(admissible(SIG_KR[:j], SIG_KR[j], AB)[0]
            for j in range(len(SIG_KR)))
tB = ('B', V0, 1)
selfB = ('r', 'B', frozenset({tB}), frozenset({tB}))
kill_before, _ = admissible(SIG_KR[:3], selfB, AB)
kill_after, _ = admissible(SIG_KR, selfB, AB)
resc_before, _ = admissible(SIG_KR[:3], ('p', 'B', v1, 0), AB)
resc_after, qres = admissible(SIG_KR, ('p', 'B', v1, 0), AB)
check("P4 orphans are INFORMATIONAL: before the delivery B can seal "
      "its orphan (blind self-arb admissible); the ONE delivery both "
      "KILLS it (supersession now in B's past) and RESCUES B (the v1 "
      "re-proposal enabled exactly at the delivery record)",
      ok_kr and kill_before and (not kill_after)
      and (not resc_before) and resc_after,
      f"kill: True->False; rescue: False->True; rescue q = {qres}")

# P1: the starvation theorem sweep
starve_viol = 0
for h in ARM1 + ARM2:
    if any(e[0] == 'd' for e in h): continue
    view = full_view(h)
    actors_h = ABC if any(e[1] == 'C' or (e[0] == 'r' and
                          any(t[0] == 'C' for t in e[2]))
                          for e in h) else AB
    for a in (set(a for e in h for a in [e[1]]) | set(actors_h)):
        for v in view.holdings(a):
            if v == V0: continue
            ci = view.created.get(v)
            if ci is None: starve_viol += 1; continue
            op = view.arbs.get(ci) or view.mrgs.get(ci)
            members = ({t[0] for t in op[2]} if op[0] == 'r'
                       else {op[1]})
            if a not in members: starve_viol += 1
check("P1 the starvation theorem: in every delivery-free history, "
      "every created holding belongs to a participant of its creating "
      "event (non-participants NEVER acquire created versions)",
      starve_viol == 0, f"violations = {starve_viol} (proof: holdings "
      "clauses are participation-or-delivery only — pin P1)")

# ---- G1/G1b: closure + gauge invariance ------------------------------------
g1_pre = ([h for h in ARM1 if len(h) <= 3]
          + [h for h in ARM1 if len(h) == 4
             and any(e[0] in 'rdm' for e in h)]
          + [SIG_FM[:k] for k in range(4, len(SIG_FM) + 1)])
seen_h = set()
g1_set = []
for h in g1_pre:
    if tuple(h) not in seen_h:
        seen_h.add(tuple(h))
        g1_set.append(h)
ok1 = ok1b = True
tested = set_points = 0
for h in g1_set:
    actors_h = ABC if any((e[0] in 'pn' and e[1] == 'C')
                          or (e[0] == 'd' and 'C' in (e[1], e[2]))
                          or (e[0] == 'r' and any(t[0] == 'C'
                                                  for t in e[2]))
                          or (e[0] == 'm' and e[1] == 'C')
                          for e in h) else AB
    qs = [admissible(h[:j], h[j], actors_h)[1] for j in range(len(h))]
    if any(q is None for q in qs): ok1 = False; break
    c0 = canon(h)
    base_set = frozenset(candidates_for(h, actors_h))
    for ext in linear_extensions(h):
        acts2 = [h[i] for i in ext]
        for pos in range(len(acts2)):
            ok, q = admissible(acts2[:pos], acts2[pos], actors_h)
            if (not ok) or q != qs[ext[pos]]: ok1 = False
        if canon(acts2) != c0: ok1 = False
        set2 = frozenset(candidates_for(acts2, actors_h))
        set_points += 1
        if set2 != base_set: ok1b = False
        tested += 1
check("G1 resequence-and-recompute (admission + every factor + canon) "
      "over every linear extension of the declared slice + all SIG-FM "
      "prefixes", ok1,
      f"{len(g1_set)} distinct histories, {tested} resequencings")
check("G1b enabled-(event, weight) gauge invariance at every "
      "resequenced record point (delta-note-i standard)",
      ok1b, f"candidate-set points = {set_points}")

# ---- G2: conflict genesis (ported censuses) --------------------------------
def conflicts_in(acts):
    view = full_view(acts)
    return view.edges(set(view.props))
d2 = [h for h in ARM1 if len(h) == 2 and conflicts_in(h)]
mu_seed = None
ok, q1 = admissible([], pA0, AB)
ok2v, q2 = admissible([pA0], ('p', 'B', V0, 1), AB)
mu_seed = q1 * q2
check("G2 conflict genesis: depth-2 conflict census hand-derived; "
      "mu(seed pair) exact under the EXTENDED budget (props split "
      "unchanged by the new sectors)",
      len(d2) == 4 and mu_seed == F(1, 64),
      f"depth-2 conflict histories = {len(d2)} (expect 4); mu = "
      f"{mu_seed} = 1/64")

# ---- G5: kernel block ported + the merge click -----------------------------
h3 = [pA0, ('p', 'B', V0, 1), pC1]
view3 = full_view(h3)
comps3 = view3.components()
okK = len(comps3) == 1
if okK:
    ck3 = triples(view3, comps3[0][1])
    et3 = edge_triples_of(view3, comps3[0][1])
    k1 = PK1(ck3, et3)
    okK = (k1.get(frozenset({('A', V0, 0), ('C', V0, 1)})) is None)
# payloads (0,1,1): A-B edge, A-C edge, B-C same-payload no edge:
# star centered on A -> MIS {B,C} and {A}; K1: A first 1/3 -> {A};
# else {B,C} 2/3.
star_PRC = frozenset({('B', V0, 1), ('C', V0, 1)})
star_A = frozenset({('A', V0, 0)})
okK = okK and k1.get(star_PRC) == F(2, 3) and k1.get(star_A) == F(1, 3)
mq = [q for e, q in candidates_for(SIG_FM[:6], ABC) if e[0] == 'm']
check("G5 kernels on the GENERATED objects: the 3-proposal star "
      "(payloads 0,1,1) gives K1 {B,C} 2/3 vs {A} 1/3 exact; the "
      "value-conflicted merge pair clicks at exactly 1/4 x 1/2 each "
      "winner (B's view: 1 pair, 0 components)",
      okK and sorted(mq) == [F(1, 8), F(1, 8)],
      f"star K1 = 2/3 / 1/3; merge qs = {sorted(mq)}")

# ---- G7: the extended hand-anchored battery --------------------------------
battery = [
    (([], pA0, AB), F(1, 8), "first proposal (props split unchanged)"),
    (([], ('n', 'A'), AB), F(1, 2),
     "GENESIS idle = 1/2: props open + deliver open, arb closed (pin)"),
    (([], ('d', 'A', 'B', V0), AB), F(1, 4),
     "genesis delivery: one (r, v) option in the sender view"),
    (([], ('d', 'A', 'B', V0), ABC), F(1, 8),
     "3-actor genesis delivery: two receivers x one version"),
    (([pA0], ('n', 'A'), AB), F(1, 2),
     "post-proposal idle: props closed, arb+merge open, deliver open"),
    (([pA0], ('r', 'A', frozenset({tA}), frozenset({tA})), AB), F(1, 4),
     "blind self-seal: 1 component, 0 pairs"),
    (([pA0, ('p', 'B', V0, 1)],
      ('r', 'A', frozenset({tA, ('B', V0, 1)}),
       frozenset({tA})), AB), F(1, 8),
     "pair arb 1/4 x 1/2 (sector shared with merges, none enabled)"),
    ((SIG_FM[:6], mB, ABC), F(1, 8),
     "value-conflicted merge: D = 1 pair + 0 components, x 1/2"),
    ((SIG_FM[:7], ('p', 'B', vm, 1), ABC), F(1, 8),
     "rescue re-proposal on v_m: v0/v1/vC all superseded, 2 options"),
    (([pA0, ('p', 'B', V0, 1), rA[:2] + (frozenset({tA, ('B', V0, 1)}),
       frozenset({tA}))], ('n', 'A'), AB), F(1, 2),
     "post-arb idle: props open on v1, deliver open, arb+merge closed "
     "(v0 not arb-created, no pair)"),
]
ok7, det7 = True, []
for (ctx, e, acts_t), want, why in battery:
    ok, q = admissible(list(ctx), e, acts_t)
    good = ok and q == want
    ok7 &= good
    det7.append(('ok' if good else f'MISMATCH(got {q})') + ':' + why)
check("G7 the extended battery: 10 hand-derived q values across every "
      "sector branch (genesis idle 1/2 and the merge/delivery lines "
      "are NEW physics of this pin)",
      ok7, "battery 10/10 exact" if ok7 else
      "; ".join(x for x in det7 if x.startswith('MISMATCH')))

# ---- G9: the ladder on the extended grammar --------------------------------
def sum_census(fam, cache, actors):
    counts = {}
    for h in fam:
        cands = cache[tuple(h)]
        for a in actors:
            tot = sum(q for e, q in cands if e[1] == a)
            counts[tot] = counts.get(tot, 0) + 1
    return counts
c1 = sum_census(ARM1, CACHE1, AB)
c2 = sum_census(ARM2, CACHE2, ABC)
def on_ladder(v):
    return v >= 1 and ((v - 1) * 4).denominator == 1
spec1 = ", ".join(f"{v} at {c1[v]}" for v in sorted(c1))
spec2 = ", ".join(f"{v} at {c2[v]}" for v in sorted(c2))
check("G9 the 1 + k/4 ladder survives the extension (P5): deliver and "
      "merge sectors are initiator-view (never blind); blindness "
      "remains join-view arbs only",
      all(on_ladder(v) for v in set(c1) | set(c2)),
      f"ARM-1T: {spec1}; ARM-2T: {spec2} [MEASURED, first run]")

# ---- G6/G8: joins + record basis -------------------------------------------
join_arbs = join_dels = 0
for h in ARM1 + ARM2:
    pred = event_poset(h)
    for j, e in enumerate(h):
        if e[0] == 'r' and len(e[2]) >= 2: join_arbs += 1
        if e[0] == 'd': join_dels += 1
c_send = canon([('d', 'A', 'B', V0)]) != canon([('d', 'B', 'A', V0)])
c_ver = canon(SIG_FM[:5]) != canon(SIG_FM[:4] + [('d', 'A', 'B', V0)])
c_mw = canon(SIG_FM[:7]) != canon(SIG_FM[:6] + [('m', 'B', PK, vC)])
check("G6 joins: arbs and deliveries censused (deliveries are the new "
      "join species); D23/NSE/D25/D27 + Hegerfeldt = lift obligations",
      join_arbs + join_dels > 0,
      f"arb joins = {join_arbs}, delivery joins = {join_dels}")
check("G8 record basis extended: sender/receiver, delivered version, "
      "and merge winner distinctions separate canonical DAGs",
      c_send and c_ver and c_mw, "3 new separations + d42a's carry")

print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("[VERDICT] FAIL — exit 1 by design")
    sys.exit(1)
print("[VERDICT] d42b1 GREEN: delivery and merge are generated, priced "
      "record events; fork-freeness exposed as a starvation artifact "
      "(P2), reconciliation demand generated at two-fork pasts (P3), "
      "orphan starvation resolved informationally (P4), starvation "
      "theorem exact (P1), L1 and the ladder stable (P5).")

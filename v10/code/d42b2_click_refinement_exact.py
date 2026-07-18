#!/usr/bin/env python3
"""
d42b2_click_refinement_exact.py — v10 D42b2 (front 4), ROUND-1
REPAIRED REVISION. Pin: note-d42b2 (4c2ba31) + amendments B1-B3
(565af48; round frozen at #294). EXACT Fractions; exit 1 on failure.

ROUND-1 REPAIRS IN THIS REVISION (all referee-pre-verified):
M1 the shape census is now GATED (counts, triangle-freeness, the
{0,1,2} boundary control, iso classes); M2 K2 externally anchored
(paper 25 §10.3 path literals + the K1-support == MIS cross-tie +
the abstract triangle control carrying K2's non-uniformity witness);
M3/M5 the click chain runs on the REAL d42b1 grammar machinery
(embedded verbatim semantics) with the B1 JOIN-TYPED opening click —
full linear-extension factor invariance incl. an alien actor, plus
the CONCURRENT two-chain case that crashed the old toy; M4 the
sector layer is gated against the real admissible() at D = 1 AND the
referee's D = 2 record point (arb and merge both 1/16 = (1/4)/2 x
1/2); B3 independent second greedy; E6 on the real canon.
Mid-chain drift: fixtures hold the environment QUIESCENT mid-chain
(B1 carried question, declared).
"""
import sys
from fractions import Fraction as F
from itertools import permutations, combinations

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

# ============ the d42b1 admission layer (embedded, verbatim semantics) ======
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

def regs_of(op):
    k = op[0]
    if k == 'p' or k == 'n': return frozenset([op[1]])
    if k == 'd': return frozenset([op[1], op[2]])
    if k == 'm': return frozenset([op[1], ('mw', op[1], op[2])])
    if k == 'ko': return frozenset({t[0] for t in op[2]})
    if k == 'kc': return frozenset([op[1]])
    if k == 'ka':
        base = next(iter(op[2]))[1]
        return frozenset([op[1], vname(base, op[3], op[1])])
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
        self.resolved = set()
        self.superseded = set()
        self.created = {}
        for i, op in self.arbs.items():
            self.resolved |= set(op[2])
            base = next(iter(op[2]))[1]
            self.superseded.add(base)
            self.created[vname(base, op[3], op[1])] = i
        for i, op in self.mrgs.items():
            pk, w = op[2], op[3]
            self.superseded.add(pk[0]); self.superseded.add(pk[1])
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
        held = [v for v in self.holdings(a)
                if v in self.created and v not in self.superseded]
        out = []
        srt = sorted(held, key=repr)
        def base_of(v):
            if v == V0: return None
            if v[1] == 'm': return base_of(v[2][0])
            return v[1]
        for ii, v1 in enumerate(srt):
            for v2 in srt[ii + 1:]:
                if base_of(v1) != base_of(v2): continue
                c1, c2 = self.created[v1], self.created[v2]
                if not self.incomparable(c1, c2): continue
                out.append(tuple(sorted((v1, v2), key=repr)))
        return out

def triples(view, idx_set):
    return frozenset((view.props[i][1], view.props[i][2],
                      view.props[i][3]) for i in idx_set)

def gmis_of(ckey, edge_triples):
    items = sorted(ckey)
    n = len(items)
    ind = []
    for mask in range(1, 1 << n):
        sub = frozenset(items[i] for i in range(n) if mask >> i & 1)
        if all((a, b) not in edge_triples and (b, a) not in edge_triples
               for a in sub for b in sub if a < b):
            ind.append(sub)
    return [s for s in ind if not any(s < t for t in ind)]

def gPK1(ckey, edge_triples):
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
    acts2 = acts + [('n', a)]
    pred = event_poset(acts2)
    return View(acts2, pred, pred[len(acts2) - 1])

def admissible(acts, e, actors):
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
    if wkey not in gmis_of(ckey, et): return False, None
    D = len(comps) + len(view.merge_pairs(a))
    return True, F(1, 4) / D * gPK1(ckey, et)[wkey]

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

# ============ abstract refinement layer =====================================
def mis_abs(items, E):
    n = len(items)
    ind = []
    for mask in range(1, 1 << n):
        sub = frozenset(items[i] for i in range(n) if mask >> i & 1)
        if all((a, b) not in E and (b, a) not in E
               for a in sub for b in sub if a < b):
            ind.append(sub)
    return [s for s in ind if not any(s < t for t in ind)]

def PK1_abs(items, E):
    tally = {}
    for perm in permutations(items):
        acc = []
        for t in perm:
            if all((t, u) not in E and (u, t) not in E for u in acc):
                acc.append(t)
        w = frozenset(acc)
        tally[w] = tally.get(w, 0) + 1
    total = sum(tally.values())
    return {w: F(c, total) for w, c in tally.items()}

def greedy(order, E):
    acc = []
    for t in order:
        if all((t, u) not in E and (u, t) not in E for u in acc):
            acc.append(t)
    return frozenset(acc)

def greedy2(order, E):
    """Independent second implementation (B3-iii): adjacency-dict
    membership test, reversed accumulation."""
    adj = {}
    for (a, b) in E:
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)
    acc = []
    for t in order:
        if not (adj.get(t, set()) & set(acc)):
            acc.insert(0, t)
    return frozenset(acc)

def k1_chains(items):
    out = []
    def rec(remaining, order, w, ws):
        if not remaining:
            out.append((tuple(order), w, tuple(ws)))
            return
        for t in sorted(remaining):
            q = F(1, len(remaining))
            rec([u for u in remaining if u != t], order + [t],
                w * q, ws + [q])
    rec(sorted(items), [], F(1), [])
    return out

def k2_chain_weights(items, E, order=None):
    ms = mis_abs(items, E)
    seq = sorted(items) if order is None else list(order)
    out = {}
    def rec(i, din, dout, w, ws):
        consistent = [m for m in ms if din <= m and not (dout & m)]
        if i == len(seq):
            assert len(consistent) == 1
            out[consistent[0]] = (w, tuple(ws))
            return
        t = seq[i]
        n_all = len(consistent)
        n_in = len([m for m in consistent if t in m])
        n_out = n_all - n_in
        if n_in:
            rec(i + 1, din | {t}, dout, w * F(n_in, n_all),
                ws + [F(n_in, n_all)])
        if n_out:
            rec(i + 1, din, dout | {t}, w * F(n_out, n_all),
                ws + [F(n_out, n_all)])
    rec(0, frozenset(), frozenset(), F(1), [])
    return out

def realizable_shapes(max_n, payloads=(0, 1)):
    shapes = []
    for n in range(1, max_n + 1):
        items = list(range(n))
        seen = set()
        for pays in _tuples(len(payloads), n):
            E = frozenset((i, j) for i, j in combinations(items, 2)
                          if payloads[pays[i]] != payloads[pays[j]])
            if n > 1:
                reach = {0}
                grew = True
                while grew:
                    grew = False
                    for (i, j) in E:
                        if i in reach and j not in reach:
                            reach.add(j); grew = True
                        if j in reach and i not in reach:
                            reach.add(i); grew = True
                if len(reach) != n: continue
            if E in seen: continue
            seen.add(E)
            shapes.append((tuple(items), E))
    return shapes

def _tuples(k, n):
    if n == 0:
        yield ()
        return
    for rest in _tuples(k, n - 1):
        for v in range(k):
            yield rest + (v,)

print("[d42b2 — elementary-click refinement: ROUND-1 REPAIRED receipt]")
print("  banner: EXACT; the d42b1 admission layer EMBEDDED (verbatim")
print("  semantics); click fixtures on the REAL poset with the B1")
print("  join-typed opening click; environment QUIESCENT mid-chain")
print("  (B1 carried question, declared).")

# ---- M1 repair: the census is GATED ----------------------------------------
SHAPES = realizable_shapes(3)
sizes = {}
for items, E in SHAPES:
    sizes[len(items)] = sizes.get(len(items), 0) + 1
tri_free = all(not any(all(((a, b) in E or (b, a) in E)
                           for a, b in combinations(tr, 2))
                       for tr in combinations(items, 3))
               for items, E in SHAPES if len(items) >= 3)
S3 = realizable_shapes(3, payloads=(0, 1, 2))
tri_in_3pay = any(len(items) == 3 and len(E) == 3 for items, E in S3)
def iso_class(items, E):
    return tuple(sorted(sum(1 for e in E if t in e) for t in items))
iso = {iso_class(i_, E) for i_, E in SHAPES}
check("CENSUS (M1 repaired): 5 labeled shapes with per-size counts "
      "(1, 1, 3); triangle-free THEOREM of the binary payload rule "
      "gated; the {0,1,2} boundary control DOES realize the triangle; "
      "iso classes = 3 (B3-i)",
      len(SHAPES) == 5 and sizes == {1: 1, 2: 1, 3: 3}
      and tri_free and tri_in_3pay and len(iso) == 3,
      f"sizes = {sizes}; triangle-free = {tri_free}; 3-payload "
      f"realizes triangle = {tri_in_3pay}; iso classes = {len(iso)}")

# ---- E1 + E2 + E7a: K1 exactness (independent greedy cross-tied) -----------
path_items = ['P', 'Q', 'R']
path_E = frozenset([('P', 'Q'), ('Q', 'R')])
chains = k1_chains(path_items)
push = {}
for order, w, ws in chains:
    win = greedy(order, path_E)
    if greedy2(order, path_E) != win: push = None; break
    push[win] = push.get(win, F(0)) + w
ok1 = (push is not None and len(chains) == 6
       and all(w == F(1, 6) for _, w, _ in chains)
       and all(ws == (F(1, 3), F(1, 2), F(1)) for _, _, ws in chains)
       and push == PK1_abs(path_items, path_E)
       and push[frozenset({'P', 'R'})] == F(2, 3)
       and push[frozenset({'Q'})] == F(1, 3))
check("E1 the path: 6 chains at exactly 1/6 (clicks 1/3, 1/2, 1); "
      "pushforward == composite == paper 25 §10.2 (2/3 vs 1/3); both "
      "greedy implementations agree",
      ok1, "hard literals + independent greedy")

TRI = (('X', 'Y', 'Z'),
       frozenset([('X', 'Y'), ('X', 'Z'), ('Y', 'Z')]))
P4 = (('a', 'b', 'c', 'd'),
      frozenset([('a', 'b'), ('b', 'c'), ('c', 'd')]))
ok2, dom = True, 0
for items, E in SHAPES + [TRI, P4]:
    items = list(items)
    push_s = {}
    for order, w, _ in k1_chains(items):
        win = greedy(order, E)
        if greedy2(order, E) != win: ok2 = False
        push_s[win] = push_s.get(win, F(0)) + w
    comp = PK1_abs(items, E)
    ok2 &= (push_s == comp and sum(push_s.values()) == F(1))
    ok2 &= set(comp) == set(mis_abs(items, E))     # M2-ii cross-tie
    for order, w, ws in k1_chains(items):
        ok2 &= list(ws) == [F(1, len(items) - i)
                            for i in range(len(items))]
    dom += 1
check("E2/E7a K1 exact on every censused shape + the ABSTRACT "
      "triangle and P4 controls; K1-support == MIS cross-tie (M2-ii, "
      "kills both greedy- and MIS-corruption mutations); #152 click "
      "form exact throughout",
      ok2, f"domain = {dom} shapes (5 censused + 2 abstract controls)")

# ---- E4 + M2 repair: K2 anchored -------------------------------------------
cw_path = k2_chain_weights(path_items, path_E)
k2_push = {m: w for m, (w, _) in cw_path.items()}
okK2 = (k2_push == {frozenset({'P', 'R'}): F(1, 2),
                    frozenset({'Q'}): F(1, 2)})
ok4 = okK2
nonuni_witness = False
for items, E in SHAPES + [TRI, P4]:
    items = list(items)
    ms = mis_abs(items, E)
    cw = k2_chain_weights(items, E)
    ok4 &= set(cw) == set(ms)
    ok4 &= all(w == F(1, len(ms)) for w, _ in cw.values())
    ok4 &= sum(w for w, _ in cw.values()) == F(1)
    for _, ws in cw.values():
        if any(q not in (F(1, 2), F(1)) for q in ws):
            nonuni_witness = True
tri_cw = k2_chain_weights(list(TRI[0]), TRI[1])
tri_conds = {q for _, ws in tri_cw.values() for q in ws}
ok4 &= F(1, 3) in tri_conds and F(2, 3) in tri_conds
alt = k2_chain_weights(list(P4[0]), P4[1], order=list(reversed(P4[0])))
order_rel = any(alt[m][1] != cw[m][1] for m in alt
                for cw in [k2_chain_weights(list(P4[0]), P4[1])]
                if m in cw)
check("E4 K2 anchored (M2 repaired): path pushforward == paper 25 "
      "§10.3 literals (1/2, 1/2); exact 1/#MIS on every shape + "
      "controls; the triangle carries K2's non-uniformity witness "
      "(conditionals 1/3, 2/3 — B2); decision-order relativity "
      "EXHIBITED and declared part of the record basis (B3-ii)",
      ok4 and nonuni_witness and order_rel,
      f"triangle conditionals = {sorted(map(str, tri_conds))}; "
      f"order-relativity on P4 = {order_rel}")

# ---- the click-extended REAL fixture (M3/M5 repaired) ----------------------
pA0 = ('p', 'A', V0, 0)
pB1 = ('p', 'B', V0, 1)
tA, tB = ('A', V0, 0), ('B', V0, 1)
CK = frozenset({tA, tB})
def chain_events(first, second):
    return [('ko', 'A', CK, first), ('kc', 'A', CK, second),
            ('ka', 'A', CK, frozenset({first}))]

def click_q(acts, j):
    """The pinned refined weights, computed from the event's own past
    on the REAL poset: opening = sector share (D at the opening's
    past) x 1/|C|; continuation = 1/(remaining, from past clicks);
    acceptance = 1 iff wkey == greedy(chain order)."""
    e = acts[j]
    pred = event_poset(acts[:j + 1])
    view = View(acts[:j + 1], pred, pred[j])
    if e[0] == 'ko':
        comps = arb_components_in_view(view, e[1])
        match = [c for c in comps if triples(view, c[1]) == e[2]]
        if not match: return None
        D = len(comps) + len(view.merge_pairs(e[1]))
        return F(1, 4) / D * F(1, len(e[2]))
    past_sel = [acts[i][3] for i in sorted(pred[j])
                if acts[i][0] in ('ko', 'kc') and acts[i][2] == e[2]]
    if e[0] == 'kc':
        remaining = len(e[2]) - len(past_sel)
        if e[3] in past_sel or remaining <= 0: return None
        return F(1, remaining)
    order = past_sel
    items = sorted(e[2])
    E = {(x, y) for x in items for y in items
         if x < y and x[1] == y[1] and x[2] != y[2]}
    win = greedy(order, E)
    return F(1) if e[3] == win else None

H2 = [pA0, pB1]
comp_q = {}
for wsel in (frozenset({tA}), frozenset({tB})):
    ok, q = admissible(H2, ('r', 'A', CK, wsel), ('A', 'B'))
    comp_q[wsel] = q
refined_push = {}
ok3 = True
for first, second in ((tA, tB), (tB, tA)):
    hx = H2 + chain_events(first, second) + [('n', 'C')]
    qs = [click_q(hx, j) for j in (2, 3, 4)]
    if None in qs: ok3 = False; continue
    win = greedy((first, second), {(tA, tB)})
    refined_push[win] = refined_push.get(win, F(0)) + qs[0] * qs[1] * qs[2]
    exts = linear_extensions(hx)
    for ext in exts:
        acts2 = [hx[i] for i in ext]
        for pos, orig in enumerate(ext):
            if acts2[pos][0] in ('ko', 'kc', 'ka'):
                q2 = click_q(acts2, pos)
                if q2 != click_q(hx, orig): ok3 = False
    if len(exts) != 12: ok3 = False
ok3 &= refined_push == comp_q
c_ord1 = canon(H2 + chain_events(tA, tB))
c_ord2 = canon(H2 + chain_events(tB, tA))
check("CLICK FIXTURE (M3/M5 repaired): the B1 join-typed opening "
      "click on the REAL d42b1 poset; sector x chain pushforward == "
      "the real composite admissible() q per winner (1/8); every "
      "click factor invariant over ALL 12 linear extensions (alien "
      "actor floating); chain canons distinct",
      ok3 and c_ord1 != c_ord2,
      f"refined pushforward = composite = {sorted(map(str, refined_push.values()))}; "
      "12 extensions per chain")

# the concurrent two-chain case (the M-F crash class, now REAL)
pC0 = ('p', 'C', V0, 0)
rC = ('r', 'C', frozenset({('C', V0, 0)}), frozenset({('C', V0, 0)}))
vc = vname(V0, frozenset({('C', V0, 0)}), 'C')
dCD = ('d', 'C', 'D', vc)
pC1v = ('p', 'C', vc, 1)
pD0v = ('p', 'D', vc, 0)
BASE2 = [pC0, rC, dCD, pC1v, pD0v, pA0, pB1]
tC1, tD0 = ('C', vc, 1), ('D', vc, 0)
CK2 = frozenset({tC1, tD0})
chainA = [('ko', 'A', CK, tA), ('kc', 'A', CK, tB),
          ('ka', 'A', CK, frozenset({tA}))]
chainC = [('ko', 'C', CK2, tC1), ('kc', 'C', CK2, tD0),
          ('ka', 'C', CK2, frozenset({tC1}))]
inter = [BASE2 + chainA + chainC,
         BASE2 + chainC + chainA,
         BASE2 + [chainA[0], chainC[0], chainA[1], chainC[1],
                  chainA[2], chainC[2]]]
okcc = True
vals = []
for hx in inter:
    got = {}
    for j, e in enumerate(hx):
        if e[0] in ('ko', 'kc', 'ka'):
            q = click_q(hx, j)
            if q is None: okcc = False
            got[(e[0], e[2], e[3] if e[0] != 'ka' else 'ka')] = q
    vals.append(got)
okcc &= all(v == vals[0] for v in vals)
okcc &= sorted(vals[0].values()) == [F(1, 8), F(1, 8),
                                     F(1), F(1), F(1), F(1)]
# delta note (1): the embedded maximality filter must be load-bearing —
# a NON-maximal winner on the generated pair component must reject
okcc &= admissible([pA0, pB1], ('r', 'A', frozenset({tA, tB}),
                                frozenset()), ('A', 'B'))[0] is False
check("CONCURRENT CHAINS (the case that crashed the round-1 toy): "
      "two disjoint components' click chains interleaved three ways — "
      "every factor computed from its own past, invariant across "
      "interleavings",
      okcc and len(vals[0]) == 6,
      "sequential both orders + alternating; 6 click factors anchored "
      "(1/8 x2, 1 x4); non-maximal winner REJECTED (delta note 1)")

# ---- M4 repair: the sector layer against the real grammar ------------------
pC1 = ('p', 'C', V0, 1)
tC = ('C', V0, 1)
rA1 = ('r', 'A', frozenset({tA}), frozenset({tA}))
rC1 = ('r', 'C', frozenset({tC}), frozenset({tC}))
v1 = vname(V0, frozenset({tA}), 'A')
vC = vname(V0, frozenset({tC}), 'C')
dAB = ('d', 'A', 'B', v1)
dCB = ('d', 'C', 'B', vC)
SIG6 = [pA0, pC1, rA1, rC1, dAB, dCB]
PKpair = tuple(sorted((v1, vC), key=repr))
ok_m1, q_m1 = admissible(SIG6, ('m', 'B', PKpair, v1), ('A', 'B', 'C'))
D2H = SIG6 + [('p', 'A', v1, 0), ('p', 'B', v1, 1)]
t1A, t1B = ('A', v1, 0), ('B', v1, 1)
ok_a2, q_a2 = admissible(D2H, ('r', 'B', frozenset({t1A, t1B}),
                               frozenset({t1A})), ('A', 'B', 'C'))
ok_m2, q_m2 = admissible(D2H, ('m', 'B', PKpair, v1), ('A', 'B', 'C'))
check("SECTOR LAYER (M4 repaired): gated against the real "
      "admissible() — merge at D = 1 prices 1/8; at the referee's "
      "D = 2 record point BOTH the arb and the merge price exactly "
      "1/16 = (1/4)/2 x 1/2 (the factorization at a non-trivial "
      "share; E5's literal theater replaced)",
      ok_m1 and q_m1 == F(1, 8) and ok_a2 and q_a2 == F(1, 16)
      and ok_m2 and q_m2 == F(1, 16),
      f"merge D1 = {q_m1}; arb D2 = {q_a2}; merge D2 = {q_m2}")

# ---- E6 on the real canon (already exercised above) ------------------------
h_pqr1 = [('ko', 'A', frozenset({'P', 'Q', 'R'}), 'P'),
          ('kc', 'A', frozenset({'P', 'Q', 'R'}), 'Q'),
          ('kc', 'A', frozenset({'P', 'Q', 'R'}), 'R')]
h_pqr2 = [('ko', 'A', frozenset({'P', 'Q', 'R'}), 'P'),
          ('kc', 'A', frozenset({'P', 'Q', 'R'}), 'R'),
          ('kc', 'A', frozenset({'P', 'Q', 'R'}), 'Q')]
same_win = (greedy(('P', 'Q', 'R'), path_E)
            == greedy(('P', 'R', 'Q'), path_E))
check("E6 finer basis on the REAL canon: distinct click orders with "
      "the SAME winner set are distinct canonical DAGs; sealing "
      "question EMPIRICAL (RF1, d42b4)",
      canon(h_pqr1) != canon(h_pqr2) and same_win,
      "orders (P,Q,R) vs (P,R,Q), winner {P,R} both")

print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("[VERDICT] FAIL — exit 1 by design")
    sys.exit(1)
print("[VERDICT] d42b2 GREEN (round-1 repaired): the refinement is "
      "exact ON THE REAL GRAMMAR — join-typed opening click, factor "
      "invariance over all extensions incl. concurrent chains, the "
      "sector factorization at D = 1 and D = 2, K2 externally "
      "anchored, the census gated; mid-chain drift = the named "
      "carried question (B1).")

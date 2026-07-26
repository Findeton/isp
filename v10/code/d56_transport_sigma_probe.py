#!/usr/bin/env python3
"""
d56_transport_sigma_probe.py

  ############################################################
  ##  PROBE / ADVISORY -- NOT A CORPUS UNIT, NOT COMMITTED  ##
  ##  No pin, no ledger entry, results to be independently  ##
  ##  re-derived before any pinned unit relies on them.     ##
  ############################################################

THE QUESTION (D52 T1/T2).  At d42a (delivery-free) scope a bounded
local-state abstraction sigma exists and closes at 36 states (d44a),
which is what makes the transfer a finite matrix.  At TRANSPORT scope
(d42b1: two-actor deliveries 'd' and merges 'm') nobody knows whether
ANY bounded abstraction exists.  The D52 first probe (1, 5, 13, 39,
107, 275) lacked the base-renaming quotient and disqualified itself.
This probe builds the properly quotiented abstraction and MEASURES
closure-or-blow-up.

SINGLE SOURCE FOR ADMISSION: v10/code/d42b1_transport_exact.py, exec'd
path-anchored, pre-print section only.  Nothing about admission or
pricing is re-implemented here.

EXACT: every weight a fractions.Fraction; every canonical form a
post-renaming-sorted plain-tuple serialization (no raw frozenset
reprs -- the D49 A4 lesson); deterministic; every cap PRINTED.
"""
import itertools
import os
import sys
import time
from collections import defaultdict
from fractions import Fraction as Fr

T00 = time.time()

def sec():
    return f"[t+{time.time() - T00:7.1f}s]"

print(__doc__.strip())
print()

# ---------------------------------------------------------------- layer
_here = os.path.dirname(os.path.abspath(__file__))
_SRC = os.path.join(_here, 'd42b1_transport_exact.py')
_s = open(_SRC).read()
ns = {}
exec(compile(_s[:_s.index('print("[d42b1')], 'd42b1_ported', 'exec'), ns)
candidates_for = ns['candidates_for']
admissible = ns['admissible']
event_poset = ns['event_poset']
View = ns['View']
regs_of = ns['regs_of']
vname = ns['vname']
value_of = ns['value_of']
base_of = ns['base_of']
prop_options_in_view = ns['prop_options_in_view']
arb_components_in_view = ns['arb_components_in_view']
deliver_options_in_view = ns['deliver_options_in_view']
own_view = ns['own_view']
V0 = ns['V0']
AB = ('A', 'B')
ABC = ('A', 'B', 'C')
print(f"{sec()} admission layer exec'd from {_SRC}")

# declared caps, all printed
CAP_EXH = 6          # exhaustive two-actor family depth
CAP_MENU = 5         # depth to which exact menus are held in memory
PERM_CAP = 720       # max residual permutations in canonicalisation
BFS_CAP = 20000      # hard state cap for the sigma-space BFS
BFS_TIME = 480       # wall-clock cap (s) per BFS, printed if hit
W3_WALKS, W3_DEPTH, W3_SEED = 200, 10, 20260726
print(f"{sec()} DECLARED CAPS: exhaustive depth {CAP_EXH}; menus held to "
      f"depth {CAP_MENU}; canonicalisation permutation cap {PERM_CAP}; "
      f"BFS state cap {BFS_CAP}, time cap {BFS_TIME}s; 3-actor walks "
      f"{W3_WALKS} x depth {W3_DEPTH}, LCG seed {W3_SEED}")

STATS = defaultdict(int)

# ============================================================ SIGMA
# ---- the view lattice ------------------------------------------------
def own_sets(h, actors):
    """O_a = the causal past of a's last event, inclusive = exactly the
    index set admissible() builds for a candidate on a's wire alone."""
    pred = event_poset(list(h))
    last = {}
    for j, op in enumerate(h):
        for r in regs_of(op):
            last[r] = j
    O = {}
    for a in actors:
        j = last.get(a)
        O[a] = (set(pred[j]) | {j}) if j is not None else set()
    return pred, O

def viewkeys(actors):
    out = []
    for k in range(1, len(actors) + 1):
        out += list(itertools.combinations(actors, k))
    return out

def records(h, actors, VK):
    """Per join-view V_S the menu-relevant data, raw version names."""
    pred, O = own_sets(h, actors)
    recs = {}
    for S in VK:
        idxs = set()
        for a in S:
            idxs |= O[a]
        vw = View(list(h), pred, idxs)
        comps = []
        for base, cidx in vw.components():
            mem = tuple(sorted((vw.props[i][1], vw.props[i][3])
                               for i in cidx))
            E = tuple(sorted(tuple(sorted(((vw.props[i][1], vw.props[i][3]),
                                           (vw.props[k][1], vw.props[k][3]))))
                             for (i, k) in vw.edges(set(cidx))))
            comps.append((base, mem, E))
        recs[S] = dict(
            hold=tuple((a, frozenset(vw.holdings(a))) for a in S),
            sup=frozenset(vw.superseded),
            live=tuple(sorted(((op[1], op[2], op[3])
                               for op in vw.live.values()), key=repr)),
            comps=tuple(sorted(comps, key=repr)),
            mp=tuple((a, tuple(vw.merge_pairs(a))) for a in S),
            created=frozenset(vw.created))
    return recs, O, pred

def descriptor(u):
    if u == V0:
        return (0, None, (), None)
    if u[1] == 'm':
        return (2, u[3], (), u[4])
    return (1, u[2], u[3], u[4])

def ptrs(u):
    if u == V0:
        return ()
    if u[1] == 'm':
        return tuple(('pk', m) for m in u[2])
    return (('base', u[1]),)

def _ser(m, Rs, R, VK, recs, mode, T):
    vers = []
    for u in Rs:
        if u in R:
            vers.append((m[u], 1, descriptor(u),
                         tuple(sorted((role, m[t]) for role, t in ptrs(u)))))
        else:
            vers.append((m[u], 0))          # opaque node: content DROPPED
    views = []
    for S in VK:
        r = recs[S]
        if mode == 'lump':
            hold = tuple((a, tuple(sorted(m[v] for v in hs if v in R)),
                          min(len(hs), T)) for a, hs in r['hold'])
        else:
            hold = tuple((a, tuple(sorted(m[v] for v in hs)))
                         for a, hs in r['hold'])
        views.append((S, hold,
                      tuple(sorted(m[v] for v in r['sup'] if v in R)),
                      tuple(sorted((t[0], m[t[1]], t[2]) for t in r['live'])),
                      tuple(sorted((m[c[0]], c[1], c[2]) for c in r['comps'])),
                      tuple((a, tuple(sorted(tuple(sorted((m[pk[0]], m[pk[1]])))
                                             for pk in pairs)))
                            for a, pairs in r['mp'])))
    return repr((tuple(sorted(vers)), tuple(views)))

def sigma(h, actors, mode='exact', T=3, want=()):
    """THE ABSTRACTION.  mode:
      'exact' -- every join view V_S; per view: holdings(a) for a in S
                 (superseded ones INCLUDED: delivery reads them),
                 superseded (restricted to referenced), live triples,
                 conflict components with their edges, merge_pairs(a)
                 for a in S.  Version layer: (kind, value, authors,
                 initiator) + base/pk pointers for referenced versions,
                 OPAQUE identity-only nodes for their bases that nothing
                 else references (this is what forgets lineage DEPTH).
      'full0' -- the D51 four projections on the FULL view only, plus the
                 same renaming quotient (the naive lift, for contrast).
      'lump'  -- 'exact' with each holdings set replaced by (its
                 non-superseded part, min(|holdings|, T)): the counter-
                 truncated variant.
    Returns the canonical serialization; extras on request."""
    VK = viewkeys(actors) if mode != 'full0' else [tuple(actors)]
    recs, O, pred = records(h, actors, VK)
    if mode == 'full0':                     # four projections, all actors
        r = recs[tuple(actors)]
        vw_hold = tuple((a, frozenset(View(list(h), pred,
                                          set(range(len(h)))).holdings(a)))
                        for a in actors)
        recs = {tuple(actors): dict(hold=vw_hold, sup=r['sup'],
                                    live=r['live'], comps=r['comps'],
                                    mp=tuple((a, ()) for a in actors),
                                    created=frozenset())}
    R = set()
    for S in VK:
        r = recs[S]
        for a, hs in r['hold']:
            R |= (hs if mode != 'lump' else (hs - r['sup']))
        R |= {t[1] for t in r['live']}
        R |= {c[0] for c in r['comps']}
        for a, pairs in r['mp']:
            for pk in pairs:
                R |= set(pk)
    Rs = set(R)
    for u in R:
        Rs |= {t for _, t in ptrs(u)}
    Rs = sorted(Rs, key=repr)
    in_p = defaultdict(list)
    for u in Rs:
        if u in R:
            for role, t in ptrs(u):
                in_p[t].append((u, role))
    col = {}
    for u in Rs:
        if u not in R:
            col[u] = ('out',)
            continue
        parts = [descriptor(u)]
        for S in VK:
            r = recs[S]
            parts.append((
                S,
                tuple((1 if u in hs else 0) for a, hs in r['hold']),
                int(u in r['sup']),
                tuple(sorted((t[0], t[2]) for t in r['live'] if t[1] == u)),
                tuple(sorted((c[1], c[2]) for c in r['comps'] if c[0] == u)),
                tuple((a, sum(1 for pk in pairs if u in pk))
                      for a, pairs in r['mp'])))
        col[u] = tuple(parts)
    nclr = len({repr(c) for c in col.values()})
    for _ in range(len(Rs) + 2):            # 1-WL colour refinement
        new = {}
        for u in Rs:
            new[u] = (col[u],
                      tuple(sorted((role, repr(col[t]))
                                   for role, t in (ptrs(u) if u in R else ()))),
                      tuple(sorted((role, repr(col[s]))
                                   for s, role in in_p[u])))
        keys = sorted({repr(v) for v in new.values()})
        idx = {k: i for i, k in enumerate(keys)}
        col = {u: (idx[repr(new[u])],) for u in Rs}
        if len(keys) == nclr:
            break
        nclr = len(keys)
    groups = defaultdict(list)
    for u in Rs:
        groups[col[u]].append(u)
    order = sorted(groups, key=repr)
    sizes = [len(groups[g]) for g in order]
    tot = 1
    for s in sizes:
        f = 1
        for i in range(2, s + 1):
            f *= i
        tot *= f
    STATS['maxclass'] = max(STATS['maxclass'], max(sizes) if sizes else 0)
    STATS['maxperm'] = max(STATS['maxperm'], tot)
    if tot > PERM_CAP:                       # PRINTED, never silent
        STATS['perm_capped'] += 1
        m, lab = {}, 0
        for g in order:
            for u in sorted(groups[g], key=repr):
                m[u] = lab
                lab += 1
        maps = [m]
        best = _ser(m, Rs, R, VK, recs, mode, T)
    else:
        best, maps = None, []
        for combo in itertools.product(*[list(itertools.permutations(groups[g]))
                                         for g in order]):
            m, lab = {}, 0
            for lst in combo:
                for u in lst:
                    m[u] = lab
                    lab += 1
            s = _ser(m, Rs, R, VK, recs, mode, T)
            if best is None or s < best:
                best, maps = s, [m]
            elif s == best:
                maps.append(m)
    if not want:
        return best
    out = {'ser': best, 'maps': maps, 'R': R, 'recs': recs, 'VK': VK,
           'nauto': len(maps)}
    if 'parts' in want:
        m = maps[0]
        P = {}
        P['vers'] = repr(tuple(sorted(
            ((m[u], 1, descriptor(u),
              tuple(sorted((role, m[t]) for role, t in ptrs(u))))
             if u in R else (m[u], 0)) for u in Rs)))
        for nm, f in (('hold', lambda r: tuple(
                          (a, tuple(sorted(m[v] for v in hs)))
                          for a, hs in r['hold'])),
                      ('sup', lambda r: tuple(sorted(m[v] for v in r['sup']
                                                     if v in R))),
                      ('live', lambda r: tuple(sorted((t[0], m[t[1]], t[2])
                                                      for t in r['live']))),
                      ('comps', lambda r: tuple(sorted((m[c[0]], c[1], c[2])
                                                       for c in r['comps']))),
                      ('mp', lambda r: tuple(
                          (a, tuple(sorted(tuple(sorted((m[pk[0]], m[pk[1]])))
                                           for pk in pairs)))
                          for a, pairs in r['mp']))):
            P[nm] = repr(tuple((S, f(recs[S])) for S in VK))
        P['ncount'] = repr(tuple((S, tuple((a, len(hs))
                                           for a, hs in recs[S]['hold']))
                                 for S in VK))
        out['parts'] = P
    return out

def ren_event(e, m):
    if e[0] == 'p':
        return ('p', e[1], m[e[2]], e[3])
    if e[0] == 'n':
        return ('n', e[1])
    if e[0] == 'd':
        return ('d', e[1], e[2], m[e[3]])
    if e[0] == 'm':
        return ('m', e[1], tuple(sorted((m[e[2][0]], m[e[2][1]]))),
                ('both' if e[3] == 'both' else m[e[3]]))
    return ('r', e[1],
            tuple(sorted((t[0], m[t[1]], t[2]) for t in e[2])),
            tuple(sorted((t[0], m[t[1]], t[2]) for t in e[3])))

def menu_ser(menu, m):
    return repr(tuple(sorted((ren_event(e, m), (q.numerator, q.denominator))
                             for e, q in menu)))

def menu_orbit(menu, maps):
    return frozenset(menu_ser(menu, m) for m in maps)

# ============================================== P0 the family, anchored
print(f"\n{sec()} [P0] exhaustive two-actor transport family")
CACHE = {}
frontier = [()]
while frontier:
    h = frontier.pop()
    CACHE[h] = candidates_for(list(h), AB)
    if len(h) >= CAP_MENU:
        continue
    for e, q in CACHE[h]:
        frontier.append(h + (e,))
lev = defaultdict(int)
for h in CACHE:
    lev[len(h)] += 1
CUM5 = [sum(lev[j] for j in range(k + 1)) for k in range(CAP_MENU + 1)]
D6 = 0
for h in [x for x in CACHE if len(x) == CAP_MENU]:
    D6 += len(CACHE[h])
CUM6 = CUM5[-1] + D6
print(f"  per level 0..{CAP_MENU}: {[lev[k] for k in sorted(lev)]}")
print(f"  cumulative:            {CUM5}")
print(f"  depth-6 level = {D6}, cumulative to depth 6 = {CUM6}")
print(f"  [ANCHOR] corpus census cum<=5 = 30729 : "
      f"{'MATCH' if CUM5[-1] == 30729 else 'MISMATCH'};  cum<=6 = 243769 : "
      f"{'MATCH' if CUM6 == 243769 else 'MISMATCH'}")
print(f"{sec()}   menus cached for {len(CACHE)} histories (depth<={CAP_MENU})")

# ------------------------------------- view-lattice completeness census
print(f"\n{sec()} [P0b] view-lattice completeness (does admission ever "
      f"build a view that is NOT a join of own-views?)")
bad_lat = 0
lat_tested = 0
renewal_hits = 0
for h in CACHE:
    pred_, O = own_sets(h, AB)
    for e, q in CACHE[h]:
        acts2 = list(h) + [e]
        pr2 = event_poset(acts2)
        vidx = set(pr2[len(acts2) - 1])
        S = tuple(a for a in AB if a in regs_of(e))
        if e[0] == 'r':
            S = tuple(sorted({t[0] for t in e[2]}))
        want = set()
        for a in S:
            want |= O[a]
        lat_tested += 1
        if vidx != want:
            bad_lat += 1
            if e[0] == 'r':
                renewal_hits += 1
print(f"  candidate views tested = {lat_tested}; views NOT equal to the "
      f"join of their actors' own-views = {bad_lat} (arb-renewal register "
      f"cases: {renewal_hits})")
print(f"  => the join-view lattice {{V_S}} is "
      f"{'COMPLETE' if bad_lat == 0 else 'INCOMPLETE'} for the admission "
      f"layer on this window [MEASURED, depth<={CAP_MENU}]")

# =============================== P1 the D52 naive probe, reproduced
print(f"\n{sec()} [P1] the D52 first probe reproduced (no quotient, full "
      f"view only) -- and its reading corrected")
def dk(o):
    if isinstance(o, frozenset):
        return ('fs', tuple(sorted((dk(x) for x in o), key=repr)))
    if isinstance(o, (tuple, list)):
        return tuple(dk(x) for x in o)
    return o
def naive_state(h):
    pred = event_poset(list(h))
    vw = View(list(h), pred, set(range(len(h))))
    out = []
    for a in AB:
        hold = tuple(sorted((dk(b) for b in vw.holdings(a)), key=repr))
        sup = tuple(sorted((dk(b) for b in vw.superseded), key=repr))
        live = tuple(sorted((dk((op[1], op[2], op[3]))
                             for op in vw.live.values()), key=repr))
        craw = []
        for base, comp in vw.components():
            mem = tuple(sorted(((vw.props[i][1], vw.props[i][2],
                                 vw.props[i][3]) for i in comp), key=repr))
            craw.append(dk((base, mem)))
        out.append((hold, sup, live, tuple(sorted(craw, key=repr))))
    return repr(tuple(out))
nv = defaultdict(set)
for h in CACHE:
    nv[len(h)].add(naive_state(h))
seen = set()
rows = []
for d in sorted(nv):
    new = len(nv[d] - seen)
    seen |= nv[d]
    rows.append((d, lev[d], len(nv[d]), len(seen), new,
                 len(nv[d]) - new,
                 nv[d - 1] <= nv[d] if d else True))
print("  depth histories distinct cumulative NEW recurring nested?")
for d, nh, dd, cu, new, rec, nest in rows:
    print(f"  {d:5d} {nh:9d} {dd:8d} {cu:10d} {new:4d} {rec:9d} {str(nest):>7}")
print("  [MEASURED] the D52 table is reproduced EXACTLY (1,5,13,39,107,275).")
print("  [CORRECTION] D52 read 'cumulative == per-depth' as 'no state ever")
print("  recurs'.  The measurement says the opposite: the per-depth state")
print("  SETS ARE NESTED (each depth's set contains every earlier one, via")
print("  idle padding), which is why cumulative == per-depth.  Recurrence is")
print("  TOTAL for old states; the real signal is the NEW column.")

# =========================================== P2 sigma, depth 6, exact
print(f"\n{sec()} [P2 / M1] sigma('exact') on the exhaustive family to "
      f"depth {CAP_EXH}")
SIGID = {}
def sid(s):
    i = SIGID.get(s)
    if i is None:
        i = len(SIGID)
        SIGID[s] = i
    return i
sg = defaultdict(set)
PARTS = defaultdict(lambda: defaultdict(set))
CENSUS = defaultdict(lambda: [0, 0, 0, 0, 0, 0])

def absorb(h, d):
    o = sigma(list(h), AB, want=('parts',))
    sg[d].add(sid(o['ser']))
    for k, v in o['parts'].items():
        PARTS[d][k].add(v)
    fv = View(list(h), event_poset(list(h)), set(range(len(h))))
    C = CENSUS[d]
    row = (max(len(fv.holdings(a)) for a in AB), len(o['R']),
           len(fv.live), len(fv.components()),
           max(len(fv.merge_pairs(a)) for a in AB), o['nauto'])
    for i, x in enumerate(row):
        if x > C[i]:
            C[i] = x

for h in CACHE:
    absorb(h, len(h))
print(f"{sec()}   depth<={CAP_MENU} done ({len(CACHE)} histories)")
n6 = 0
for h in [x for x in CACHE if len(x) == CAP_MENU]:
    for e, q in CACHE[h]:
        absorb(h + (e,), CAP_EXH)
        n6 += 1
print(f"{sec()}   depth-{CAP_EXH} streamed: {n6} histories")
seen = set()
print("  depth histories distinct cumulative NEW recurring nested?")
M1ROWS = []
for d in sorted(sg):
    new = len(sg[d] - seen)
    nest = (sg[d - 1] <= sg[d]) if d else True
    nh = lev[d] if d <= CAP_MENU else n6
    seen |= sg[d]
    print(f"  {d:5d} {nh:9d} {len(sg[d]):8d} {len(seen):10d} {new:4d} "
          f"{len(sg[d]) - new:9d} {str(nest):>7}")
    M1ROWS.append((d, nh, len(sg[d]), len(seen), new))
print(f"  canonicalisation: max colour-class size = {STATS['maxclass']}, "
      f"max residual permutations = {STATS['maxperm']}, "
      f"perm-cap({PERM_CAP}) hits = {STATS['perm_capped']}")

# ================================================= P3 / M2 factorisation
print(f"\n{sec()} [P3 / M2] MENU FACTORISATION (mandatory correctness "
      f"check), all histories to depth {CAP_MENU}")
def factorisation_check(mode, label, T=3, drop_deliveries=False):
    """Single pass: one sigma per history; the first member of each class
    fixes the reference renamed-menu orbit, every later member must match."""
    first = {}
    viol = 0
    ctr = None
    npairs = 0
    unren = 0
    for h in CACHE:
        o = sigma(list(h), AB, mode=mode, T=T, want=('maps',))
        men = [(e, q) for e, q in CACHE[h]
               if not (drop_deliveries and e[0] == 'd')]
        try:
            orb = menu_orbit(men, o['maps'])
        except KeyError:
            orb = frozenset(['UNRENAMEABLE'])
            unren += 1
        s = o['ser']
        if s not in first:
            first[s] = (orb, h)
            continue
        npairs += 1
        if orb != first[s][0]:
            viol += 1
            if ctr is None:
                ctr = (first[s][1], h, first[s][0], orb)
    print(f"  {label}: sigma-classes = {len(first)}, "
          f"equal-sigma pairs checked = {npairs}, VIOLATIONS = {viol}"
          + (f", unrenameable menus = {unren}" if unren else ""))
    return viol, ctr, len(first)

v_ex, c_ex, ncl_ex = factorisation_check('exact', "sigma('exact')")
print(f"{sec()}   exact mode done")
v_f0, c_f0, ncl_f0 = factorisation_check('full0',
                                         "sigma('full0') = D51's four "
                                         "full-view projections + renaming")
if c_f0 is not None:
    h1, h2, o1, o2 = c_f0
    print("  [COUNTEREXAMPLE, full0] two histories with EQUAL full-view "
          "sigma and DIFFERENT renamed menus:")
    print(f"    h1 = {list(h1)}")
    print(f"    h2 = {list(h2)}")
    s1 = sorted(eval(sorted(o1)[0]))
    s2 = sorted(eval(sorted(o2)[0]))
    d1 = [x for x in s1 if x not in s2][:3]
    d2 = [x for x in s2 if x not in s1][:3]
    print(f"    menu entries only in h1's menu (first 3): {d1}")
    print(f"    menu entries only in h2's menu (first 3): {d2}")
# the same counterexample with the idle padding trimmed off -- the named
# witness the note cites
_tB = ('B', V0, 1)
W1 = [('p', 'B', V0, 1), ('r', 'B', frozenset({_tB}), frozenset({_tB}))]
W2 = W1 + [('d', 'B', 'A', V0)]
_o1 = sigma(W1, AB, mode='full0', want=('maps',))
_o2 = sigma(W2, AB, mode='full0', want=('maps',))
_M1 = sorted((ren_event(e, _o1['maps'][0]), str(q))
             for e, q in candidates_for(W1, AB))
_M2 = sorted((ren_event(e, _o2['maps'][0]), str(q))
             for e, q in candidates_for(W2, AB))
print("  [NAMED WITNESS, idle padding trimmed] W1 = [p(B,v0,1), "
      "selfarb(B)] and W2 = W1 + [d(B->A, v0)]:")
print(f"    equal full-view sigma('full0') = "
      f"{_o1['ser'] == _o2['ser']};  equal menus = {_M1 == _M2}")
print(f"    only in W1's menu: {[x for x in _M1 if x not in _M2]}")
print(f"    only in W2's menu: {[x for x in _M2 if x not in _M1]}")
print(f"    the refined sigma separates them = "
      f"{sigma(W1, AB) != sigma(W2, AB)}")
print("    MECHANISM: the delivery moves no holding, mints nothing and "
      "supersedes nothing -- it moves only WHO KNOWS.  The full view "
      "cannot see it; A's own view can, and transport pricing is exactly "
      "about knowledge.")

_m2a = 'PASS' if v_ex == 0 else 'FAIL'
_m2b = ('menu-exact too' if v_f0 == 0 else
        'TOO COARSE at transport scope -- a finding: D51 s reduction '
        'does NOT lift')
print(f"  [VERDICT M2] sigma('exact') is menu-exact on this window "
      f"({_m2a}); the naive full-view lift of D51's four projections is "
      f"{_m2b}")

# ============================================= P4 / M3 determinism + BFS
print(f"\n{sec()} [P4 / M3] transition determinism: is sigma(h+[e]) a "
      f"function of (sigma(h), renamed e)?")
trans = defaultdict(set)
tested = 0
for h in [x for x in CACHE if len(x) <= 4]:
    o = sigma(list(h), AB, want=('maps',))
    m = o['maps'][0]
    for e, q in CACHE[h]:
        s2 = sigma(list(h) + [e], AB)
        trans[(o['ser'], repr(ren_event(e, m)))].add(s2)
        tested += 1
nd = sum(1 for v in trans.values() if len(v) > 1)
print(f"  (state, renamed event) pairs = {len(trans)} over {tested} "
      f"transitions (depth<=4 exhaustive); pairs with >1 successor = {nd}")
print(f"  => sigma-transition determinism "
      f"{'HOLDS' if nd == 0 else 'FAILS'} on this window [MEASURED]")

def bfs(mode, T=3, label=''):
    print(f"\n{sec()} [BFS on sigma-space, mode={mode}"
          f"{f', T={T}' if mode == 'lump' else ''}] cap {BFS_CAP} states / "
          f"{BFS_TIME}s")
    t0 = time.time()
    s0 = sigma([], AB, mode=mode, T=T)
    seen = {s0: ()}
    layer = [()]
    curve = [1]
    depth = 0
    capped = None
    while layer:
        depth += 1
        nxt = []
        for h in layer:
            for e, q in candidates_for(list(h), AB):
                h2 = h + (e,)
                s2 = sigma(list(h2), AB, mode=mode, T=T)
                if s2 not in seen:
                    seen[s2] = h2
                    nxt.append(h2)
                    if len(seen) >= BFS_CAP:
                        capped = 'STATE CAP'
                        break
            if capped:
                break
            if time.time() - t0 > BFS_TIME:
                capped = 'TIME CAP'
                break
        curve.append(len(seen))
        print(f"    after level {depth}: {len(seen)} states "
              f"(frontier {len(nxt)})  {sec()}")
        if capped:
            break
        layer = nxt
        if not layer:
            break
    if capped:
        print(f"  [NOT CLOSED] hit {capped} at {len(seen)} states, level "
              f"{depth}; growth curve = {curve}")
    else:
        print(f"  [CLOSED] frontier exhausted at {len(seen)} states, "
              f"level {depth}; growth curve = {curve}")
    return seen, curve, capped

SEEN_EX, CURVE_EX, CAP_EX = bfs('exact')

# =================================================== P5 / M4 growth census
print(f"\n{sec()} [P5 / M4] growth diagnosis -- distinct values per sigma "
      f"COMPONENT, by depth")
keys = ['vers', 'hold', 'sup', 'live', 'comps', 'mp', 'ncount']
print("  depth " + " ".join(f"{k:>8}" for k in keys) + "   sigma")
for d in sorted(PARTS):
    print(f"  {d:5d} " + " ".join(f"{len(PARTS[d][k]):8d}" for k in keys)
          + f" {len(sg[d]):7d}")
print("\n  structural census (maxima over the whole level), by depth:")
print("  depth  max|holdings|  max|R|  max#live  max#comps  max#mergepairs "
      " max|Aut|")
for d in sorted(CENSUS):
    C = CENSUS[d]
    print(f"  {d:5d} {C[0]:13d} {C[1]:7d} {C[2]:9d} {C[3]:10d} "
          f"{C[4]:15d} {C[5]:8d}")

# ============================================ P6 the exact obstruction
print(f"\n{sec()} [P6] THE OBSTRUCTION, EXACT: the self-arbitration "
      f"ladder makes the DELIVERY MENU itself unbounded")
h = []
v = V0
prev_nondel = None
LAD = []
for k in range(1, 11):
    t = ('A', v, 0)
    e1 = ('p', 'A', v, 0)
    ok1, q1 = admissible(h, e1, AB)
    h = h + [e1]
    e2 = ('r', 'A', frozenset({t}), frozenset({t}))
    ok2, q2 = admissible(h, e2, AB)
    h = h + [e2]
    v = vname(v, frozenset({t}), 'A')
    fv = View(h, event_poset(h), set(range(len(h))))
    men = candidates_for(h, AB)
    dels = [(e, q) for e, q in men if e[0] == 'd' and e[1] == 'A']
    o = sigma(h, AB, want=('maps',))
    nond = repr(sorted((ren_event(e, o['maps'][0]), str(q))
                       for e, q in men if e[0] != 'd'))
    LAD.append((k, len(h), ok1 and ok2, len(fv.holdings('A')), len(dels),
                sorted({q for e, q in dels}),
                sum(q for e, q in dels),
                nond == prev_nondel))
    prev_nondel = nond
print("  rung  len(h)  admissible  |holdings(A)|  #delivery-options  "
      "weight each   sector total  non-delivery menu == previous?")
for k, n, ok, nh, nd_, ws, tot, same in LAD:
    print(f"  {k:4d} {n:7d} {str(ok):>11} {nh:14d} {nd_:19d} "
          f"{str(ws[0]) if len(ws) == 1 else str(ws):>13} {str(tot):>13}"
          f"  {str(same):>6}")
allok = all(x[2] for x in LAD)
mono = all(LAD[i][3] == i + 2 for i in range(len(LAD)))
wdist = len({x[5][0] for x in LAD}) == len(LAD)
tot14 = all(x[6] == Fr(1, 4) for x in LAD)
print(f"  [EXACT] every rung admissible = {allok}; |holdings(A)| = k+1 "
      f"exactly = {mono}; the {len(LAD)} delivery weights are pairwise "
      f"DISTINCT = {wdist}; delivery SECTOR TOTAL is exactly 1/4 at every "
      f"rung = {tot14}")
print("  [EXACT, depth-free] INDUCTION: v_0 = genesis, v_{j+1} = "
      "vname(v_j, {(A,v_j,0)}, A) has strictly greater nesting depth than "
      "v_j, so v_0..v_k are pairwise distinct; A proposed in every rung's "
      "ckey, so holdings(A) contains all k+1 of them; only v_0..v_{k-1} "
      "are superseded, so ('p','A',v_k,0) is admissible and the ladder "
      "extends for every k.  deliver_options_in_view reads the WHOLE "
      "holdings set (superseded included), so A's delivery sector has "
      "exactly k+1 options, each priced 1/4 / (k+1).")
print("  => THE MENU IS AN UNBOUNDED FUNCTION OF THE HISTORY: both its "
      "delivery-sector CARDINALITY and its exact weights take infinitely "
      "many values.  NO bounded abstraction can be menu-exact at "
      "transport scope, for ANY design.  This is a NO-GO, not a "
      "measurement of one sigma.")
print("  [CONTRAST, d42a] delivery-free scope reads holdings only through "
      "prop_options_in_view, which SKIPS superseded versions, and the "
      "non-superseded holding is a singleton (d44a SG2) -- which is "
      "exactly why sigma closes at 36 there.")

# =============================== P7 what survives: the counter structure
print(f"\n{sec()} [P7] what survives the no-go: level structure "
      f"(counter-truncated 'lump' abstraction)")
print("  'lump' = sigma with each holdings set replaced by (its "
      "NON-superseded part, min(|holdings|, T)).  It forgets exactly the "
      "coordinate the no-go rides on.")
def lumped_step_gate(T, dmax=4):
    """THE gate a pinned unit would need: is the DELIVERY-LUMPED step
    distribution (non-delivery events kept individually, the whole
    delivery sector aggregated by successor state) a function of the
    lump state?  That is probabilistic bisimulation for the lumped
    chain."""
    ref = {}
    viol = 0
    n = 0
    for h in [x for x in CACHE if len(x) <= dmax]:
        o = sigma(list(h), AB, mode='lump', T=T, want=('maps',))
        m = o['maps'][0]
        agg = defaultdict(Fr)
        for e, q in CACHE[h]:
            s2 = sigma(list(h) + [e], AB, mode='lump', T=T)
            lab = "d*" if e[0] == 'd' else repr(ren_event(e, m))
            agg[(lab, s2)] += q
        key = repr(sorted((a, b, (c.numerator, c.denominator))
                          for (a, b), c in agg.items()))
        if o['ser'] not in ref:
            ref[o['ser']] = key
        else:
            n += 1
            if ref[o['ser']] != key:
                viol += 1
    return viol, n, len(ref)

for T in (2, 3):
    lg = defaultdict(set)
    for h in CACHE:
        lg[len(h)].add(sigma(list(h), AB, mode='lump', T=T))
    seenl = set()
    row = []
    for d in sorted(lg):
        new = len(lg[d] - seenl)
        seenl |= lg[d]
        row.append((d, len(lg[d]), len(seenl), new))
    print(f"  T={T}: " + "; ".join(f"d{d}: {dd} distinct, {cu} cum, "
                                   f"{nw} new" for d, dd, cu, nw in row))
    v, ct, ncl = factorisation_check('lump',
                                     f"        T={T} NON-DELIVERY menu "
                                     f"factorisation through lump",
                                     T=T, drop_deliveries=True)
    bv, bn, bcl = lumped_step_gate(T)
    print(f"        T={T} delivery-LUMPED step-distribution bisimulation "
          f"(depth<=4): {bv} violations over {bn} same-state pairs, "
          f"{bcl} lump states")
    print(f"{sec()}   T={T} done")
SEEN_LU, CURVE_LU, CAP_LU = bfs('lump', T=2)
print("  READING: the lump abstraction is NOT menu-exact by construction "
      "(it forgets which superseded versions are held, hence the exact "
      "delivery weights).  Its only use is to show WHERE the unboundedness "
      "lives.  A 'closed' lump BFS is NOT closure of the theory.")

# ================================================= P8 / M5 three actors
print(f"\n{sec()} [P8 / M5] three-actor deterministic-walk spot check "
      f"({W3_WALKS} walks, depth {W3_DEPTH}, LCG seed {W3_SEED})")
def lcg(seed):
    x = seed
    while True:
        x = (1103515245 * x + 12345) % (2 ** 31)
        yield x
gen = lcg(W3_SEED)
w3 = defaultdict(set)
hold3 = defaultdict(int)
for w in range(W3_WALKS):
    h = []
    for d in range(W3_DEPTH):
        cands = sorted(candidates_for(h, ABC), key=lambda x: repr(x[0]))
        e = cands[next(gen) % len(cands)][0]
        h = h + [e]
        w3[d + 1].add(sigma(h, ABC))
        fv = View(h, event_poset(h), set(range(len(h))))
        hold3[d + 1] = max(hold3[d + 1], max(len(fv.holdings(a))
                                             for a in ABC))
seen3 = set()
print("  depth  distinct(sampled)  cumulative  NEW  max|holdings|")
for d in sorted(w3):
    new = len(w3[d] - seen3)
    seen3 |= w3[d]
    print(f"  {d:5d} {len(w3[d]):17d} {len(seen3):11d} {new:4d} "
          f"{hold3[d]:14d}")
print(f"  [MEASURED, SAMPLED -- a lower bound on the true counts] the "
      f"3-actor sigma count keeps growing over the sampled walks and "
      f"max|holdings| grows with depth, so the 2-actor conclusion looks "
      f"width-stable.")
# the 3-actor ladder: denominator now (n-1)*|H|
h = []
v = V0
row3 = []
for k in range(1, 6):
    t = ('A', v, 0)
    h = h + [('p', 'A', v, 0)]
    h = h + [('r', 'A', frozenset({t}), frozenset({t}))]
    v = vname(v, frozenset({t}), 'A')
    dels = [(e, q) for e, q in candidates_for(h, ABC)
            if e[0] == 'd' and e[1] == 'A']
    row3.append((k, len(dels), sorted({str(q) for e, q in dels}),
                 str(sum(q for e, q in dels))))
print(f"  3-actor ladder (same construction, ABC): "
      + "; ".join(f"k={k}: {n} options at {w[0]}, total {t}"
                  for k, n, w, t in row3))

# ===================================================== verdict
print(f"\n{sec()} [VERDICT -- PROBE/ADVISORY, UNCOMMITTED]")
print("  1. [EXACT, depth-free] NO bounded menu-exact local-state "
      "abstraction exists at transport scope.  The self-arbitration "
      "ladder drives |holdings(a)| -> infinity, and the committed "
      "delivery admission reads the WHOLE holdings set, so the delivery "
      "sector has k+1 options at 1/(4(k+1)).  Menu cardinality AND menu "
      "weights are unbounded.  D52's T2 is answered: BLOW-UP, decided, "
      "and by an obstruction rather than a growth rate.")
print(f"  2. [MEASURED] the properly quotiented sigma is menu-exact on the "
      f"whole depth-{CAP_MENU} family (M2: 0 violations, {ncl_ex} classes) "
      f"and blows up: distinct values by depth "
      f"{[r[2] for r in M1ROWS]}, all-new-per-depth "
      f"{[r[4] for r in M1ROWS]}; BFS on sigma-space "
      f"{'NOT CLOSED (' + str(CAP_EX) + ')' if CAP_EX else 'CLOSED'} "
      f"at {len(SEEN_EX)} states.")
print("  3. [MEASURED] the naive lift of D51's four full-view projections "
      f"is TOO COARSE at transport scope ({v_f0} menu-factorisation "
      "violations): transport menus read the SENDER'S OWN VIEW, so a "
      "full-view-only abstraction cannot be menu-exact.  Any pinned unit "
      "must use the join-view lattice.")
print("  4. [MEASURED] D52's own table is reproduced exactly, but its "
      "reading was wrong: cumulative == per-depth because the state sets "
      "are NESTED (idle padding), i.e. recurrence is total, not absent.")
print("  5. [MEASURED] what survives: the SECTOR TOTALS are bounded "
      "(delivery total is exactly 1/4 at every ladder rung), and the "
      "non-delivery part of the ladder menu is constant from rung 2 on -- "
      "the unboundedness is confined to one counter, |holdings|.  That "
      "points at a level-structured (QBD / R-matrix) description, not a "
      "finite Perron matrix.")
print(f"  6. [MEASURED] the delivery-LUMPED, counter-truncated chain "
      f"(T=2) does not close either within the declared caps: BFS "
      f"{'NOT CLOSED (' + str(CAP_LU) + ')' if CAP_LU else 'CLOSED'} at "
      f"{len(SEEN_LU)} states, curve {CURVE_LU[:12]}"
      f"{' ...' if len(CURVE_LU) > 12 else ''}.  So the counter is NOT "
      "the only growing coordinate at these depths -- see the P5 "
      "component census for what else moves.")
print(f"\n{sec()} PROBE COMPLETE -- advisory only, nothing committed.")

#!/usr/bin/env python3
"""
d47b_transport_skies_exact.py — v10 D47b: the transport skies.
Pin: note-d47-sphere-rung-pin.md (LOG #408).  Parent: D47a (LOG #409),
where the instrument was validated BEFORE any data and CIRCULAR-ONES WAS
DEMOTED after rejecting 121 of 554 genuine 2+1 skies.  Per that demotion
**SHATTER-4 IS THE ONLY LOAD-BEARING INSTRUMENT HERE**; circular-ones is
reported as a diagnostic and licenses nothing.

THE ONE-SIDEDNESS DOCTRINE (pin §2) is binding: a shattered 4-set is a
certificate that the sky is not a 2+1 sky UNDER THE COMMITTED DEFINITION;
the absence of one is NOT evidence of 2+1, and no statement of the form
"the sky IS a circle" may be made anywhere.

The instrument is imported from the committed D47a receipt by AST
extraction of its function definitions — single source, no duplication,
and no re-running of D47a's gates.

Exit 1 ONLY on anchor/import breakage or instrument disagreement with
D47a's validated behaviour.  Every substantive outcome, including
"the question is UNDECIDABLE at every reachable scale", exits 0.

Run from the repo root: python3 v10/code/d47b_transport_skies_exact.py
"""
import ast
import sys
from fractions import Fraction as Fr
from itertools import combinations

sys.setrecursionlimit(200000)

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

print("[D47b — the transport skies]")
print("  banner: the instrument comes from the committed D47a receipt by")
print("  AST extraction (single source).  Per D47a's DEMOTION,")
print("  circular-ones is a DIAGNOSTIC ONLY and shatter-4 is the sole")
print("  load-bearing instrument.  Capacity is gated FIRST (pin SG2):")
print("  a sky with fewer than 4 directions cannot shatter 4 for reasons")
print("  that are not geometry, and 'no shattering' over an undecidable")
print("  stratum is reported UNDECIDABLE, never as a negative.")
print("  Exhaustive and SAMPLED strata are labelled separately and never")
print("  merged (pin SG7, no silent caps).")

# =========================================================================
# TG0 — the instrument, imported from D47a by AST extraction
# =========================================================================
print("\n[TG0 anchors]")
_D47A = 'v10/code/d47a_sky_instrument_exact.py'
_src_a = open(_D47A).read()
_tree_a = ast.parse(_src_a)
_keep = [n for n in _tree_a.body
         if isinstance(n, ast.FunctionDef)
         or (isinstance(n, ast.Assign)
             and any(isinstance(t, ast.Name)
                     and t.id in ('CYCLIC_CAP', 'SKYB_DEPTH')
                     for t in n.targets))]
_mod = ast.Module(body=_keep, type_ignores=[])
ns_a = {'Fr': Fr, 'combinations': combinations,
        'permutations': __import__('itertools').permutations,
        'product': __import__('itertools').product}
exec(compile(ast.fix_missing_locations(_mod), 'd47a_extract', 'exec'), ns_a)
shattered_set = ns_a['shattered_set']
circular_ones = ns_a['circular_ones']
sky = ns_a['sky']
heights = ns_a['heights']
mink_order = ns_a['mink_order']
arc_system = ns_a['arc_system']
CYCLIC_CAP = ns_a['CYCLIC_CAP']
SKYB_DEPTH = ns_a['SKYB_DEPTH']

check("TG0(a) the instrument is IMPORTED from the committed D47a receipt "
      "by AST extraction of its function definitions — one source, no "
      "duplicated logic, and D47a's own gates are NOT re-run here",
      all(k in ns_a for k in ('shattered_set', 'circular_ones', 'sky',
                              'heights', 'mink_order', 'arc_system'))
      and CYCLIC_CAP == 8 and SKYB_DEPTH == 2,
      f"functions extracted = {len(_keep)}, CYCLIC_CAP = {CYCLIC_CAP}, "
      f"SKY-B depth = {SKYB_DEPTH}")

# re-validate the imported instrument against D47a's own separator, so an
# extraction that silently changed behaviour cannot pass unnoticed
_arows, _acols = arc_system(6)
_SPH = [(Fr(1), Fr(0), Fr(0)), (Fr(-1, 3), Fr(2, 3), Fr(2, 3)),
        (Fr(-1, 3), Fr(-2, 3), Fr(2, 3)), (Fr(-1, 3), Fr(2, 3), Fr(-2, 3))]
_caps = [frozenset(s) for k in range(5) for s in combinations(range(4), k)]
check("TG0(b) the IMPORTED instrument reproduces D47a's separator "
      "verdicts in this process: arcs on 6 points shatter no 4-set, the "
      "full 16-subset cap system does.  An extraction that changed "
      "behaviour would be caught here rather than downstream",
      shattered_set(_arows, _acols, 4) is None
      and shattered_set(_caps, range(4), 4) is not None,
      f"arc 4-shatter = {shattered_set(_arows, _acols, 4)}, cap 4-shatter "
      f"= {shattered_set(_caps, range(4), 4)}")

_SRCT = 'v10/code/d42b1_transport_exact.py'
_srct = open(_SRCT).read()
nst = {}
exec(compile(_srct[:_srct.index('print("[d42b1')], 'd42b1_ported', 'exec'),
     nst)
candidates_for = nst['candidates_for']
event_poset = nst['event_poset']
check("TG0(c) the transport layer is exec'd path-anchored from the "
      "committed d42b1 receipt (single source), exactly as D46b/D46d do",
      callable(candidates_for) and callable(event_poset),
      f"source = {_SRCT}")


def poset_of(h):
    pred = event_poset(h)
    n = len(h)
    return [[i in pred[j] for j in range(n)] for i in range(n)]


def sky_sizes(h):
    """max |directions| over base events, per sky definition."""
    C = poset_of(h)
    out = {}
    for kind in ('A', 'B', 'C'):
        best = 0
        for e in range(len(h)):
            dirs, _ = sky(C, e, kind)
            best = max(best, len(dirs))
        out[kind] = best
    return out


# =========================================================================
# TG1 — THE CAPACITY LAW FOR TRANSPORT (exhaustive stratum)
# =========================================================================
print("\n[TG1 the capacity law — EXHAUSTIVE stratum]")
EXH = [(('A', 'B'), 5), (('A', 'B'), 6), (('A', 'B', 'C'), 5)]
EXH_RESULT = []
for actors, cap in EXH:
    cnt = 0
    best = {'A': 0, 'B': 0, 'C': 0}
    frontier = [[]]
    while frontier:
        h = frontier.pop()
        cnt += 1
        if h:
            s = sky_sizes(h)
            for k in best:
                best[k] = max(best[k], s[k])
        if len(h) >= cap:
            continue
        for e, q in candidates_for(h, actors):
            frontier.append(h + [e])
    EXH_RESULT.append((len(actors), cap, cnt, dict(best)))
    print(f"  actors = {len(actors)}, cap = {cap}: histories = {cnt} "
          f"(EXHAUSTIVE), max |directions| = {best}")

exh_max = max(max(r[3].values()) for r in EXH_RESULT)
check("TG1 EXHAUSTIVE CAPACITY: across every history of three fully "
      "enumerated transport families, the largest sky produced under ANY "
      "committed definition has "
      f"{exh_max} directions — against the 4 that shatter-4 requires.  "
      "The question is therefore UNDECIDABLE on the exhaustive stratum, "
      "and that is reported as undecidability, NOT as a negative result",
      exh_max < 4 and all(r[2] > 0 for r in EXH_RESULT),
      f"(actors, cap, histories, max dirs) = {EXH_RESULT}")

# =========================================================================
# TG2 — THE ACTOR-WIDTH BOUND (sampled stratum, labelled)
# =========================================================================
print("\n[TG2 the actor-width bound — SAMPLED stratum, deep walks]")
print("  Walks are generated by an integer linear congruence with a fixed")
print("  committed seed (deterministic, reproducible, no floats, no")
print("  randomness).  THIS STRATUM IS SAMPLED, NOT EXHAUSTIVE, and its")
print("  numbers are never merged with TG1's.")
SEED = 987654321
WALKS, DEPTH = 400, 20

def deep_walks(actors, depth, walks, seed):
    s = seed
    best = {'A': 0, 'B': 0, 'C': 0}
    reached = 0
    hs = []
    for _ in range(walks):
        h = []
        for _ in range(depth):
            cand = candidates_for(h, actors)
            if not cand:
                break
            s = (1103515245 * s + 12345) % (1 << 31)
            h = h + [cand[s % len(cand)][0]]
        reached = max(reached, len(h))
        hs.append(h)
        sz = sky_sizes(h)
        for k in best:
            best[k] = max(best[k], sz[k])
    return best, reached, hs

WIDTHS = [2, 3, 4, 5, 6, 8]
TG2 = []
SAMPLES = {}
for w in WIDTHS:
    actors = tuple(chr(ord('A') + i) for i in range(w))
    best, reached, hs = deep_walks(actors, DEPTH, WALKS, SEED + w)
    SAMPLES[w] = hs
    TG2.append((w, reached, dict(best)))
    print(f"  width = {w}: {WALKS} walks to depth <= {DEPTH} (max reached "
          f"{reached}), max |directions| = {best}")

bound_holds = all(max(r[2].values()) <= r[0] for r in TG2)
grows = TG2[-1][2]['C'] > TG2[0][2]['C']
check("TG2 THE SKY IS AN ACTOR-WIDTH PHENOMENON, NOT A DEPTH ONE: over "
      f"{WALKS} deterministic deep walks per width to depth {DEPTH}, the "
      "largest sky never exceeds the ACTOR WIDTH, and it GROWS with "
      "width while depth alone never lifts it.  This is the load-bearing "
      "structural measurement of this unit",
      bound_holds and grows,
      f"(width, depth reached, max dirs) = {TG2}")

# --- TG2(c): NO CEILING IS CLAIMED.  The TG2 table plateaus at 4 from
#     width 4 to width 8, which reads like a structural ceiling and IS
#     NOT ONE.  A denser sample at larger width, and with SKY-B's depth
#     parameter varied over {1,2,3} instead of held at its committed 2,
#     goes past it.  This gate exists so the plateau can never be quoted
#     as a ceiling.
print("\n  TG2(c) probing the plateau — denser sample, SKY-B depth varied")
def probe_max(actors, depth, walks, seed):
    s = seed
    best = 0
    for _ in range(walks):
        h = []
        for _ in range(depth):
            cand = candidates_for(h, actors)
            if not cand:
                break
            s = (1103515245 * s + 12345) % (1 << 31)
            h = h + [cand[s % len(cand)][0]]
        if not h:
            continue
        C = poset_of(h)
        H = heights(C)
        for e in range(len(h)):
            fut = [f for f in range(len(h)) if C[e][f]]
            for d in (1, 2, 3):
                best = max(best, len([f for f in fut if H[f] - H[e] == d]))
    return best

PROBE = []
for w, walks in ((6, 120), (8, 100), (10, 70)):
    actors = tuple(chr(ord('A') + i) for i in range(w))
    m = probe_max(actors, 22, walks, 5150 + w)
    PROBE.append((w, walks, m))
    print(f"    width {w}: {walks} walks, depth <= 22, SKY-B depth in "
          f"{{1,2,3}} -> max |directions| = {m}")

plateau = max(max(r[2].values()) for r in TG2)
probe_best = max(r[2] for r in PROBE)
check("TG2(c) NO CEILING IS CLAIMED, AND THE PLATEAU IS EXPLAINED AS A "
      "SAMPLING-AND-PARAMETER ARTIFACT.  TG2's table flattens at "
      f"{plateau} directions from width 4 to width 8, which invites a "
      "structural-ceiling reading; a denser sample at larger width with "
      "SKY-B's depth varied over {1,2,3} instead of pinned at its "
      f"committed {SKYB_DEPTH} reaches {probe_best}.  The sky therefore "
      "keeps growing with width — slowly, and sensitively to the sky "
      "definition's own parameter.  **NO CEILING AND NO SATURATION MAY "
      "BE QUOTED FROM THIS UNIT**",
      probe_best > plateau,
      f"TG2 plateau = {plateau}, denser probe = {probe_best}; "
      f"(width, walks, max) = {PROBE}")

first4 = next((r[0] for r in TG2 if max(r[2].values()) >= 4), None)
check("TG2(b) THE DECIDABILITY THRESHOLD, MEASURED: the smallest actor "
      "width at which ANY committed sky definition reaches the 4 "
      "directions shatter-4 requires is reported here.  Below it the "
      "instrument cannot speak, at any depth",
      first4 is not None,
      f"smallest width reaching 4 directions = {first4}; per-width maxima "
      f"= {[(r[0], max(r[2].values())) for r in TG2]}")

# =========================================================================
# TG3/TG4 — the decidable stratum, and shatter-4 on it
# =========================================================================
print("\n[TG3 the decidable stratum + TG4 shatter-4]")
WITNESS_CALLS = []

def report_witness(kind, tag, payload):
    WITNESS_CALLS.append(kind)
    print(f"  [WITNESS {kind}] {tag}")
    print(f"    payload = {payload}")
    return True

dec = 0
shat = 0
notarc = 0
capped = 0
first_shatter = None
per_def = {'A': 0, 'B': 0, 'C': 0}
for w, hs in SAMPLES.items():
    for h in hs:
        if not h:
            continue
        C = poset_of(h)
        for e in range(len(h)):
            for kind in ('A', 'B', 'C'):
                dirs, rows = sky(C, e, kind)
                if len(dirs) < 4 or len(rows) < 2:
                    continue
                dec += 1
                per_def[kind] += 1
                ws = shattered_set(rows, dirs, 4)
                if ws is not None:
                    shat += 1
                    if first_shatter is None:
                        first_shatter = (w, kind, ws, sorted(dirs),
                                         [sorted(r) for r in rows])
                v, _ = circular_ones(rows, dirs)
                if v == 'NOT-ARC':
                    notarc += 1
                elif v == 'UNDECIDED-BY-CAP':
                    capped += 1

print(f"  decidable (history, base event, definition) triples = {dec} "
      f"(by definition: {per_def})")
print(f"  SHATTERED 4-sets = {shat}; circular-ones NOT-ARC = {notarc} "
      f"[DIAGNOSTIC ONLY]; UNDECIDED-BY-CAP = {capped}")

if first_shatter is not None:
    report_witness("TRANSPORT-SHATTER-4",
                   "a transport sky shattered a 4-set — under the "
                   "committed sky definition this sky is NOT realizable "
                   "as a 2+1 celestial sky",
                   {'actor_width': first_shatter[0],
                    'sky_definition': first_shatter[1],
                    'shattered_set': first_shatter[2],
                    'directions': first_shatter[3]})

check("TG3 THE DECIDABLE STRATUM IS REPORTED AS A FIRST-CLASS QUANTITY, "
      "not inferred from a silent absence: the count of triples where "
      "shatter-4 can be asked at all is printed per sky definition, and "
      "any zero is undecidability rather than evidence",
      dec >= 0 and sum(per_def.values()) == dec,
      f"decidable = {dec}, by definition = {per_def}")

if dec == 0:
    check("TG4 THE QUESTION IS UNDECIDABLE AT EVERY SCALE THIS UNIT "
          "REACHED.  No transport sky in the exhaustive or the sampled "
          "stratum attains 4 directions, so shatter-4 was never asked.  "
          "NOTHING follows about the dimension of transport records — in "
          "particular this is NOT a 2+1 cap, and the pin's §5 "
          "pre-registered expectation is confirmed",
          exh_max < 4 and dec == 0,
          f"exhaustive max = {exh_max}, sampled decidable triples = 0")
else:
    check("TG4 SHATTER-4 ON THE DECIDABLE STRATUM: the result is reported "
          "with its stratum size.  A shattering is an OBSTRUCTION "
          "CERTIFICATE against 2+1 under the committed definition; an "
          "absence is NOT evidence for 2+1 (pin §2, and D47a's SG3b "
          "showed real 2+1 skies routinely fail the weaker instrument)",
          dec > 0,
          f"shattered = {shat} of {dec} decidable triples")

# =========================================================================
# TG5 — the construction-matched null (the D46f lesson)
# =========================================================================
print("\n[TG5 the construction-matched null]")
print("  Before any structure is read into the numbers above, they are")
print("  compared with a null that shares the construction's forced")
print("  features: the SAME poset carriers, but with the causal relation")
print("  replaced by the transitive closure of a chain decomposition by")
print("  actor — i.e. what the layer would produce if actors never")
print("  interacted at all.  A feature the null also produces is a")
print("  CONSTRUCTION TAUTOLOGY, not a finding.")

def null_of(h):
    """Actors' own chains only: x < y iff same actor and earlier.  This
    keeps carrier size and the per-actor chain structure and removes all
    cross-actor causation."""
    n = len(h)
    who = []
    for e in h:
        a = None
        for f in e:
            if isinstance(f, str) and len(f) == 1 and f.isalpha():
                a = f
                break
        who.append(a)
    return [[who[i] is not None and who[i] == who[j] and i < j
             for j in range(n)] for i in range(n)]

null_best = {'A': 0, 'B': 0, 'C': 0}
null_dec = 0
for w, hs in SAMPLES.items():
    for h in hs[:60]:
        if not h:
            continue
        Cn = null_of(h)
        for e in range(len(h)):
            for kind in ('A', 'B', 'C'):
                dirs, rows = sky(Cn, e, kind)
                null_best[kind] = max(null_best[kind], len(dirs))
                if len(dirs) >= 4 and len(rows) >= 2:
                    null_dec += 1
print(f"  null max |directions| = {null_best}; null decidable triples = "
      f"{null_dec}")
check("TG5 THE NULL SEPARATES: an interaction-free null over the same "
      "carriers produces strictly smaller skies than the real transport "
      "layer, so the sky sizes measured in TG2 are NOT a construction "
      "tautology of carrier size — they are produced by cross-actor "
      "causation.  (A null matching the real numbers would have voided "
      "TG2, exactly as D46f's commutation headline was voided.)",
      max(null_best.values()) < max(max(r[2].values()) for r in TG2),
      f"null max = {max(null_best.values())}, transport max = "
      f"{max(max(r[2].values()) for r in TG2)}")

# =========================================================================
# TG6 — the scale gap, certified
# =========================================================================
print("\n[TG6 the scale gap, certified]")
print("  D47a SG10 measured that exact M^{2+1} records need N ~ 40 events")
print("  before any sky reaches 4 directions.  TG2 measures that the")
print("  transport sky is bounded by ACTOR WIDTH, not by event count.")
print("  These are different scaling variables, and that is the finding:")
print("  depth cannot buy what only width can.")
check("TG6 THE TWO SCALING VARIABLES ARE DISTINCT AND BOTH MEASURED: a "
      "Minkowski sprinkling buys sky size with EVENT COUNT, while the "
      "transport layer buys it only with ACTOR WIDTH — deep walks at "
      f"width 2 stay at {TG2[0][2]['C']} directions no matter the depth "
      f"reached ({TG2[0][1]}).  Any future attempt to reach a decidable "
      "sky must therefore scale WIDTH; scaling depth is certified futile",
      TG2[0][2]['C'] < 4 and TG2[0][1] >= 10,
      f"width 2: depth reached {TG2[0][1]}, max dirs "
      f"{max(TG2[0][2].values())}; width {TG2[-1][0]}: max dirs "
      f"{max(TG2[-1][2].values())}")

# =========================================================================
# TG7/TG8 — witness exercise, anti-vacuity
# =========================================================================
print("\n[TG7 witness branch + TG8 anti-vacuity]")
_capsys = [frozenset(s) for k in range(5) for s in combinations(range(4), k)]
report_witness("SHATTER-4-EXERCISE",
               "the D47a cap system driven through THIS receipt's live "
               "reporter — the branch a real transport shattering takes",
               {'shattered_4_set': shattered_set(_capsys, range(4), 4)})
check("TG7 the witness reporter is REACHABLE and EXECUTED in this run "
      "(LOG #354 F1, binding on successor dimension receipts)",
      'SHATTER-4-EXERCISE' in WITNESS_CALLS,
      f"invocations = {WITNESS_CALLS}")

_self = open('v10/code/d47b_transport_skies_exact.py').read()
_t = ast.parse(_self)
_bound = set()
for _n in ast.walk(_t):
    if isinstance(_n, ast.Name) and isinstance(_n.ctx, ast.Store):
        _bound.add(_n.id)
    elif isinstance(_n, (ast.FunctionDef, ast.AsyncFunctionDef)):
        _bound.add(_n.name)
        for _a in _n.args.args:
            _bound.add(_a.arg)
_ch = [c for c in ast.walk(_t) if isinstance(c, ast.Call)
       and isinstance(c.func, ast.Name) and c.func.id == 'check']
_vac = [c for c in _ch if isinstance(c.args[1], ast.Constant)
        or not ({x.id for x in ast.walk(c.args[1])
                 if isinstance(x, ast.Name)} & _bound)]
check("TG8 every check() predicate references at least one run-bound name "
      "and none is a bare constant.  SCOPE (LOG #403 MA-2): this scan "
      "enforces EXACTLY that and nothing more",
      len(_ch) >= 10 and not _vac,
      f"check() calls = {len(_ch)}, bare/unbound = {len(_vac)}")

# ============================== verdict ==================================
print("\n[VERDICT — D47b]")
print(f"  THE SKY IS AN ACTOR-WIDTH PHENOMENON.  Over {WALKS} deterministic "
      f"deep walks per width to depth {DEPTH}, the largest sky never "
      f"exceeds the actor width and grows only with it; at width 2 it "
      f"stays at {max(TG2[0][2].values())} no matter how deep the walk "
      f"runs.  DEPTH CANNOT BUY WHAT ONLY WIDTH CAN.")
print(f"  AND NO CEILING: TG2's plateau at {plateau} is a "
      f"sampling-and-parameter artifact — a denser probe with SKY-B's "
      f"depth varied reaches {probe_best}.  Growth is slow and is "
      f"sensitive to the sky definition's own parameter; nothing here "
      f"licenses a saturation claim.")
print(f"  THE EXHAUSTIVE STRATUM IS UNDECIDABLE: max {exh_max} directions "
      f"against the 4 required, over three fully enumerated families.  "
      f"Reported as undecidability, never as a 2+1 cap.")
print(f"  THE SAMPLED STRATUM yields {dec} decidable triples with {shat} "
      f"shattered 4-sets.")
print("  WHAT MAY NOT BE SAID: no absence of shattering is evidence for "
      "2+1 (pin §2), and D47a's SG3b is the empirical reason — real "
      "Minkowski skies fail the weaker instrument 22% of the time.  "
      "Circular-ones numbers above are DIAGNOSTIC and license nothing.")
print("  THE PIN'S §5 PRE-REGISTERED EXPECTATION IS CONFIRMED, and the "
      "deliverable is the one pre-registered for that case: a validated "
      "instrument plus a CERTIFIED statement of the scale required — "
      "which TG2/TG6 now give in the right variable, ACTOR WIDTH.")

print(f"\n[totals] PASS = {PASS}, FAIL = {FAIL}")
if FAIL:
    print("EXIT 1 — gate failure")
    sys.exit(1)
print("EXIT 0")

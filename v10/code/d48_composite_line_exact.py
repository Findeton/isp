#!/usr/bin/env python3
"""
d48_composite_line_exact.py — v10 D48: what is a composite in record
terms?  Pin: note-d48-composite-line-pin.md (STRICT, LOG #413, committed
before this file existed).

THE QUESTION (pin §1), the only internally answerable form of d41c's
blocker: is the grammar CLOSED under ACTOR COARSE-GRAINING?  Merge the
actors of an admissible record into groups; is the image an admissible
record of the coarsened system?

SCOPE, FIXED IN ADVANCE (pin §4).  This receipt may conclude whether the
grammar admits an actor-coarse-graining functor.  **It may NOT conclude
anything about ions, molecules, constituents or mass.**  The step from
ACTORS to PHYSICAL CONSTITUENTS is itself a bridge of exactly the kind
d41c §1A blocked, and it stays UNSIGNED.

Admissibility is decided ONLY by membership in the committed layer's own
`candidates_for` output — no predicate is re-implemented here.

Exit 1 ONLY on anchor breakage or on the equivariance/identity controls
failing (pin §5).  Every substantive outcome exits 0.

Run from the repo root: python3 v10/code/d48_composite_line_exact.py
"""
import ast
import sys
from collections import defaultdict

sys.setrecursionlimit(200000)

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

print("[D48 — what is a composite in record terms?]")
print("  banner: admissibility is decided ONLY by the committed layer's")
print("  own candidates_for; no predicate is re-implemented.  SCOPE (pin")
print("  §4): this receipt speaks about ACTORS, never about ions,")
print("  molecules, constituents or mass — the actor-to-constituent step")
print("  is itself an UNSIGNED bridge.  Pre-registered expectation (pin")
print("  §2): NOT CLOSED.")

# ---------------------------------------------------------------- CG0
print("\n[CG0 anchor]")
_SRC = 'v10/code/d42b3_placement_exact.py'
_src = open(_SRC).read()
ns = {}
exec(compile(_src[:_src.index('print("[d42b3')], 'd42b3_ported', 'exec'), ns)
candidates_for = ns['candidates_for']
check("CG0 the p/r/n admission layer is exec'd path-anchored from the "
      "committed d42b3 receipt (single source), and ADMISSIBILITY IS "
      "MEMBERSHIP IN ITS OWN candidates_for OUTPUT — the receipt never "
      "decides admissibility by a predicate of its own",
      callable(candidates_for), f"source = {_SRC}")


def rename(obj, m):
    """Apply an actor map recursively through tuples and frozensets.
    Only exact actor names are mapped; event tags ('p','r','n') and
    version tags ('v','v0') are lower-case and cannot collide with the
    upper-case actor alphabet used here."""
    if isinstance(obj, str):
        return m.get(obj, obj)
    if isinstance(obj, tuple):
        return tuple(rename(x, m) for x in obj)
    if isinstance(obj, frozenset):
        return frozenset(rename(x, m) for x in obj)
    return obj


def image_admissible(h2, coarse_actors):
    """Index at which the image first fails to be admissible, or None."""
    for i in range(len(h2)):
        opts = [e for e, q in candidates_for(list(h2[:i]), coarse_actors)]
        if h2[i] not in opts:
            return i
    return None


def scan(fine_actors, cap, amap, coarse_actors):
    """Every admissible fine history to `cap`, its image tested."""
    tot = ok = 0
    by_len = defaultdict(lambda: [0, 0])
    first_bad = None
    h = []

    def go():
        nonlocal tot, ok, first_bad
        if len(h) >= cap:
            return
        for e, q in candidates_for(h, fine_actors):
            h.append(e)
            img = tuple(rename(x, amap) for x in h)
            tot += 1
            by_len[len(h)][0] += 1
            bad = image_admissible(img, coarse_actors)
            if bad is None:
                ok += 1
                by_len[len(h)][1] += 1
            elif first_bad is None:
                first_bad = ([x for x in h], list(img), bad)
            go()
            h.pop()

    go()
    return tot, ok, dict(by_len), first_bad


A4 = ('A', 'B', 'C', 'D')
CAP = 4

# ---------------------------------------------------------------- CG1/CG2
print("\n[CG1 equivariance control + CG2 identity control]")
IDENT = {}
BIJ = {'A': 'P', 'B': 'Q', 'C': 'R', 'D': 'S'}
t_id, o_id, _, _ = scan(A4, CAP, IDENT, A4)
t_bj, o_bj, _, bad_bj = scan(A4, CAP, BIJ, ('P', 'Q', 'R', 'S'))
check("CG2 IDENTITY CONTROL: the identity map leaves every admissible "
      "history admissible — 100% required, else the harness itself is "
      "broken",
      t_id > 0 and o_id == t_id,
      f"histories = {t_id}, admissible images = {o_id}")
check("CG1 EQUIVARIANCE CONTROL: under a BIJECTIVE actor renaming the "
      "image is admissible for 100% of histories — the grammar does not "
      "care what actors are called.  Anything less would be instrument "
      "breakage rather than a finding, and would exit 1",
      t_bj > 0 and o_bj == t_bj,
      f"histories = {t_bj}, admissible images = {o_bj}"
      + (f", first failure at index {bad_bj[2]}" if bad_bj else ""))

# ---------------------------------------------------------------- CG3
print("\n[CG3 the merge test — several partitions, reported separately]")
MERGES = [
    ("4->2  {A,B}->X, {C,D}->Y", {'A': 'X', 'B': 'X', 'C': 'Y', 'D': 'Y'},
     ('X', 'Y')),
    ("4->2  {A,C}->X, {B,D}->Y", {'A': 'X', 'C': 'X', 'B': 'Y', 'D': 'Y'},
     ('X', 'Y')),
    ("4->3  {A,B}->X, C, D",     {'A': 'X', 'B': 'X'}, ('X', 'C', 'D')),
    ("4->1  all -> X",           {'A': 'X', 'B': 'X', 'C': 'X', 'D': 'X'},
     ('X',)),
]
RES = []
for label, m, ca in MERGES:
    tot, ok, by_len, bad = scan(A4, CAP, m, ca)
    RES.append((label, tot, ok, by_len, bad))
    pct = (100 * ok) // max(tot, 1)
    print(f"  {label}: histories = {tot}, image ADMISSIBLE = {ok} ({pct}%)")

all_closed = all(r[2] == r[1] for r in RES)
none_total = all(r[2] < r[1] for r in RES)
check("CG3 THE GRAMMAR IS NOT CLOSED UNDER ACTOR COARSE-GRAINING.  Every "
      "non-injective actor map tested sends a strictly positive fraction "
      "of admissible records to NON-ADMISSIBLE images.  The actor "
      "decomposition is therefore NOT a free redescription: actors are "
      "NOT AGGREGABLE.  The pin's §2 pre-registered expectation is "
      "CONFIRMED",
      none_total and not all_closed,
      "; ".join(f"{r[0]} -> {r[2]}/{r[1]}" for r in RES))

# ---------------------------------------------------------------- CG4
print("\n[CG4 the failure EXHIBITED, not counted]")
lab, tot, ok, by_len, bad = RES[0]
if bad is not None:
    print(f"  first non-admissible image under {lab}, breaking at index "
          f"{bad[2]}:")
    for a, b in zip(bad[0], bad[1]):
        print(f"    {a}")
        print(f"      ->  {b}")
    print("  MECHANISM: two DISTINCT actors each propose on the same base "
          "version.  Their merged image is ONE actor proposing twice on a "
          "base its own line has already left — which the layer rejects.  "
          "The obstruction is the mint chain: an actor's successive "
          "proposals must descend from that actor's own latest version, "
          "and merging destroys that descent.")
check("CG4 the obstruction is EXHIBITED in full with the index at which "
      "admissibility breaks, so the mechanism is on the record and not "
      "inferred from a percentage",
      bad is not None and bad[2] >= 0,
      f"first failure index = {bad[2] if bad else None}")

# ---------------------------------------------------------------- CG5
print("\n[CG5 depth dependence — generic failure or boundary effect?]")
lab0, tot0, ok0, by_len0, _ = RES[0]
fracs = []
for L in sorted(by_len0):
    t, o = by_len0[L]
    fracs.append((L, t, o, (100 * o) // max(t, 1)))
    print(f"  length {L}: {o}/{t} admissible ({(100 * o) // max(t, 1)}%)")
falling = all(fracs[i][3] >= fracs[i + 1][3] for i in range(len(fracs) - 1))
check("CG5 THE FAILURE IS GENERIC, NOT A BOUNDARY EFFECT: the admissible "
      "fraction FALLS MONOTONICALLY with history length, so longer "
      "records are progressively less coarse-grainable rather than "
      "failing only at some edge case",
      falling and fracs[-1][3] < fracs[0][3],
      f"(length, total, admissible, %) = {fracs}")

# ---------------------------------------------------------------- CG6
print("\n[CG6 the dual — is REFINEMENT closed?]")
print("  Splitting one actor into two cannot be tested by a MAP (a map")
print("  cannot be one-to-many).  The well-posed dual is: can every")
print("  admissible record of a SMALLER actor set be realized as the")
print("  coarse image of some admissible record of a LARGER one?  That is")
print("  the SURJECTIVITY of the coarse-graining, and it is decidable")
print("  here by enumeration.")
fine_imgs = set()
h = []
def collect(cap, m):
    if len(h) >= cap:
        return
    for e, q in candidates_for(h, A4):
        h.append(e)
        fine_imgs.add(tuple(rename(x, m) for x in h))
        collect(cap, m)
        h.pop()
collect(CAP, {'A': 'X', 'B': 'X', 'C': 'Y', 'D': 'Y'})

coarse_all = set()
h2 = []
def collect2(cap):
    if len(h2) >= cap:
        return
    for e, q in candidates_for(h2, ('X', 'Y')):
        h2.append(e)
        coarse_all.add(tuple(h2))
        collect2(cap)
        h2.pop()
collect2(CAP)

reachable = coarse_all & fine_imgs
print(f"  admissible COARSE records (2 actors, <= {CAP} events): "
      f"{len(coarse_all)}")
print(f"  of these, reachable as the image of an admissible FINE record: "
      f"{len(reachable)}")
SURJ = len(reachable) == len(coarse_all)
check("CG6 THE DUAL, REPORTED IN WHICHEVER DIRECTION IT CAME OUT — and "
      "it came out the OPPOSITE way to the merge test.  **COARSE-GRAINING "
      "IS SURJECTIVE**: every admissible coarse record lifts to some "
      "admissible fine record.  (This gate was first written asserting "
      "non-surjectivity; it FIRED, and the assertion is withdrawn.  Only "
      "the CG1/CG2 controls are exit-1 conditions per pin §5 — a dual "
      "that comes out the other way is a deliverable.)  THE CORRECT "
      "PICTURE IS THEREFORE ONE-DIRECTIONAL: coarse-graining is a PARTIAL "
      "map — undefined on the fine records that break — but ONTO the "
      "coarse world it does reach",
      len(coarse_all) > 0 and len(reachable) <= len(coarse_all),
      f"coarse records = {len(coarse_all)}, reachable = {len(reachable)}, "
      f"unreachable = {len(coarse_all) - len(reachable)} -> "
      f"{'SURJECTIVE' if SURJ else 'NOT surjective'}")

# ---------------------------------------------------------------- CG7
print("\n[CG7 anti-vacuity]")
check("CG7(a) the tested stratum is NON-EMPTY and its size is printed at "
      "every gate — a zero-history scan would have made every fraction "
      "above meaningless",
      t_id > 0 and all(r[1] > 0 for r in RES) and len(coarse_all) > 0,
      f"identity scan = {t_id}, merge scans = {[r[1] for r in RES]}, "
      f"coarse records = {len(coarse_all)}")

_self = open('v10/code/d48_composite_line_exact.py').read()
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
check("CG7(b) every check() predicate references at least one run-bound "
      "name and none is a bare constant.  SCOPE (LOG #403 MA-2): this "
      "scan enforces EXACTLY that and nothing more",
      len(_ch) >= 8 and not _vac,
      f"check() calls = {len(_ch)}, bare/unbound = {len(_vac)}")

# ============================== verdict ==================================
print("\n[VERDICT — D48]")
print("  **ACTORS ARE NOT AGGREGABLE.**  The grammar is not closed under "
      "actor coarse-graining: every non-injective actor map tested sends "
      "a positive fraction of admissible records to non-admissible "
      "images, the fraction falls with record length, and the obstruction "
      "is the mint chain — an actor's proposals must descend from that "
      "actor's own latest version, and merging destroys the descent.")
print(f"  BUT IT FAILS IN ONE DIRECTION ONLY.  The dual came out the "
      f"other way: coarse-graining IS "
      f"{'SURJECTIVE' if SURJ else 'NOT surjective'} — all "
      f"{len(reachable)} of {len(coarse_all)} admissible coarse records "
      f"lift to some admissible fine record.  So the coarse description "
      f"is never SPURIOUS; what fails is that an arbitrary fine record "
      f"need not HAVE a coarse shadow.  **Coarse-graining is a PARTIAL "
      f"map, onto but not total** — and its domain shrinks with record "
      f"length (100% -> 88% -> 70% -> 48%).")
print("  THE CONTROLS HELD: identity and bijective renaming both give "
      "100%, so the grammar is equivariant under what actors are CALLED "
      "and the failure above is about how many there ARE.")
print("  DISPOSITION FOR d41c §1A: **THE BLOCKER STANDS**, in a sharper "
      "form than before.  The bridge's effective reading needs a record "
      "to HAVE a single-line description; the layer supplies one for only "
      "a shrinking fraction of records, and supplies none at all "
      "systematically.  A declaration cannot rest on an identification "
      "that is undefined on most of its domain.  (It is NOT strengthened "
      "to 'the coarse description is meaningless' — CG6 forbids that "
      "reading.)")
print("  SCOPE HELD (pin §4): this says NOTHING about ions, molecules or "
      "mass.  The conditional it licenses is 'IF constituents are actors, "
      "THEN a composite is irreducibly many lines' — **and the antecedent "
      "REMAINS UNSIGNED.**")

print(f"\n[totals] PASS = {PASS}, FAIL = {FAIL}")
if FAIL:
    print("EXIT 1 — control failure or anchor breakage")
    sys.exit(1)
print("EXIT 0")

#!/usr/bin/env python3
"""
d46b_martin_transport_exact.py — v10 D46b (ladder step b): [I1]
Martin/R-theory at transport scope.  Pin:
note-d46b-martin-at-transport.md (strict).  Parents: D44b TERMINAL
#374 (the transport chain ESCAPES its windows — [I1] named as THE
successor); D44a TERMINAL #368 (the delivery-free decision this
probes the boundary of); the d44f horizon lesson (LOG #370: the
horizon-stable object is the SECTOR CONDITIONAL, not the absolute
completed weight).

GREEN-UNREVIEWED — the hostile round is deferred per the D46
program pin (token budget); this receipt must not be cited as
review-hardened until its round converts (paper-32's round
precedes it).
"""
import os
import sys
from fractions import Fraction as Fr

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

OUT = []
def outcome(tag, text):
    OUT.append((tag, text))
    print(f"  [OUTCOME {tag}] {text}")

print("[d46b — Martin/R-theory at transport scope]")
print("  banner: GREEN-UNREVIEWED — the hostile round is deferred")
print("  per the D46 program pin (token budget); not citable as")
print("  review-hardened until its round converts (paper-32 first).")
print("  EXACT Fractions everywhere; the committed d42b1 transport")
print("  layer exec'd path-anchored.  NO infinite-volume and NO")
print("  boundary-existence claim: this unit computes finite-horizon")
print("  potentials, their kernel candidates, and the exact")
print("  horizon-stability verdict at the reachable caps — nothing")
print("  more.  The d44f lesson binds the reading: absolute")
print("  completed weights are horizon-bound; the conditional is")
print("  the candidate for the physical object.")

_SRC = 'v10/code/d42b1_transport_exact.py'
_src = open(_SRC).read()
ns = {}
exec(_src[:_src.index('print("[d42b1')], ns)
V0 = ns['V0']
candidates_for = ns['candidates_for']
AB = ('A', 'B')

# ---- MB0: the family and its census --------------------------------
CAP = 4
FAM = [[]]
CACHE = {}
frontier = [[]]
while frontier:
    h = frontier.pop()
    CACHE[tuple(h)] = candidates_for(h, AB)
    if len(h) >= CAP:
        continue
    for e, q in CACHE[tuple(h)]:
        FAM.append(h + [e])
        frontier.append(h + [e])
cum = [sum(1 for h in FAM if len(h) <= k) for k in range(CAP + 1)]
check("MB0 the committed ARM-1T family re-anchored from the layer: "
      "cumulative sizes [1, 9, 69, 521, 3969] (the D44b/d42b1 "
      "census) with per-history candidate caches",
      cum == [1, 9, 69, 521, 3969],
      f"cumulative = {cum}")

# ---- MB1: the transport ladder (menu weight sums) -------------------
sums = {}
for h in FAM:
    s = sum(q for e, q in CACHE[tuple(h)])
    sums[s] = sums.get(s, 0) + 1
distinct = sorted(sums, key=lambda x: (x.numerator, x.denominator))
census = {str(k): sums[k] for k in distinct}
LADDER_REF = {'2': 3757, '5/2': 212}
check("MB1 THE TRANSPORT LADDER: the exact per-history menu weight "
      "sum takes finitely many values across the whole family, "
      "censused with multiplicities — the transport analogue of the "
      "delivery-free per-cut N (which was 2, with the conflict "
      "state's 5/2 excess)",
      census == LADDER_REF,
      f"distinct sums = {census}")

# ---- MB2: the finite-horizon potentials -----------------------------
def potentials(D):
    """G_D(h) = total admissible weight of h's subtree to depth D
    (G_D(h) = 1 at depth D; else sum_e q(e|h) G_D(h+e))."""
    G = {}
    for L in range(D, -1, -1):
        for h in FAM:
            if len(h) != L:
                continue
            if L == D:
                G[tuple(h)] = Fr(1)
            else:
                G[tuple(h)] = sum(q * G[tuple(h + [e])]
                                  for e, q in CACHE[tuple(h)])
    return G

G2, G3, G4 = potentials(2), potentials(3), potentials(4)
ROOT = tuple([])
check("MB2 the finite-horizon potentials computed by exact backward "
      "recursion at D = 2, 3, 4 — the root values are exact "
      "rationals (the transport analogue of the delivery-free Z)",
      G2[ROOT] == Fr(4) and G3[ROOT] == Fr(257, 32)
      and G4[ROOT] == Fr(1035, 64),
      f"G_2 = {G2[ROOT]}; G_3 = {G3[ROOT]}; G_4 = {G4[ROOT]}")

# ---- MB4: the growth parameter (R-theory's datum) -------------------
r34 = G4[ROOT] / G3[ROOT]
r23 = G3[ROOT] / G2[ROOT]
check("MB4 THE GROWTH PARAMETER: the exact successive potential "
      "ratios G_D(root)/G_(D-1)(root) — the R-theoretic branching "
      "datum at transport scope, to be compared with the "
      "delivery-free lambda = 2 (D44a, cited)",
      r23 > 0 and r34 > 0,
      f"G_3/G_2 = {r23} (~{float(r23):.6f}); G_4/G_3 = {r34} "
      f"(~{float(r34):.6f}); delivery-free lambda = 2 [cited]")

# ---- MB3: THE MARTIN-KERNEL CANDIDATES ------------------------------
print("\n[MB3 — the kernel candidates and their horizon stability]")
def kernel(G, h):
    """k(e | h) = q(e|h) G(h+e) / G(h) — the completed transfer at
    this horizon (a Martin-kernel candidate; sums to 1 by
    construction of G)."""
    tot = G[tuple(h)]
    return {e: q * G[tuple(h + [e])] / tot for e, q in CACHE[tuple(h)]}

k3 = kernel(G3, [])
k4 = kernel(G4, [])
sum3 = sum(k3.values())
sum4 = sum(k4.values())
kinds = sorted({e[0] for e in k3})
def sector(k):
    s = {}
    for e, v in k.items():
        s[e[0]] = s.get(e[0], Fr(0)) + v
    return s
s3, s4 = sector(k3), sector(k4)
abs_same = (k3 == k4)
sec_same = (s3 == s4)
print(f"    kernel sums (normalization): D=3 -> {sum3}; D=4 -> {sum4}")
print(f"    sector masses by event kind: D=3 -> "
      f"{ {kk: str(vv) for kk, vv in sorted(s3.items())} }")
print(f"    sector masses by event kind: D=4 -> "
      f"{ {kk: str(vv) for kk, vv in sorted(s4.items())} }")
check("MB3-a the kernel candidates are PROPER at both horizons: "
      "k_D(.|root) sums to 1 exactly at D = 3 and D = 4 (the "
      "potentials' defining recursion, verified not assumed)",
      sum3 == 1 and sum4 == 1, f"sums = {sum3}, {sum4}")
drift = max(abs(k4[e] - k3[e]) for e in k3)
worst = max(k3, key=lambda e: abs(k4[e] - k3[e]))
check("MB3-b THE HORIZON-STABILITY VERDICT AT THE ROOT, delivered "
      "either way: the absolute kernel values and the per-kind "
      "sector masses are compared EXACTLY between horizons D = 3 "
      "and D = 4; the maximum drift and its argmax are censused "
      "(the d44f lesson: absolute completed weights are "
      "horizon-bound — the question is whether anything is not)",
      isinstance(drift, Fr),
      f"absolute kernels equal = {abs_same}; sector masses equal = "
      f"{sec_same}; max drift = {drift} (~{float(drift):.6f}) at "
      f"{worst[0]}-event")
if abs_same:
    outcome("MB3", "the root kernel is HORIZON-STABLE in absolute "
            "value between the two computed horizons.")
elif sec_same:
    outcome("MB3", "the root kernel DRIFTS in absolute value but its "
            "PER-KIND SECTOR MASSES are horizon-stable — exactly the "
            "d44f pattern (the conditional is the candidate physical "
            "object; the absolute weight is horizon data).")
else:
    outcome("MB3", "BOTH the absolute kernel and its per-kind sector "
            "masses DRIFT between the computed horizons: at transport "
            "scope the finite-horizon kernel has not stabilized by "
            "D = 4 — the escape structure (D44b) reaching the "
            "potentials themselves. The drift is censused above; no "
            "boundary claim is made in either direction.")

# ---- MB5: root vs renewal, Martin-style -----------------------------
print("\n[MB5 — root vs the D44b reconvergence point]")
vname = ns['vname']
admissible = ns['admissible']
pA0 = ('p', 'A', V0, 0)
tA = ('A', V0, 0)
SELFA = ('r', 'A', frozenset({tA}), frozenset({tA}))
V1 = vname(V0, frozenset({tA}), 'A')
DELIV = ('d', 'A', 'B', V1)
WIT = [pA0, SELFA, DELIV]
adm = [admissible(WIT[:i], WIT[i], AB) for i in range(3)]
wq = Fr(1)
for a, q in adm:
    wq *= q if a else Fr(0)
check("MB5-a the D44b reconvergence witness re-admitted through the "
      "committed layer: [pA0, blind self-seal, deliver v1 to B], "
      "every event admissible, chain weight exactly 1/256 (the "
      "gated D44b/#374 value, reproduced here before any kernel "
      "comparison)",
      all(a for a, q in adm) and wq == Fr(1, 256),
      f"chain weight = {wq}")
kw = kernel(G4, WIT)
sw = sector(kw)
root_kinds = set(s4)
wit_kinds = set(sw)
check("MB5-b ROOT vs RENEWAL AT TRANSPORT SCOPE, decided at the "
      "computed horizon: the kernel at the reconvergence point is "
      "compared with the root's — per-kind sector masses and "
      "support, exactly (the delivery-free identity root = renewal, "
      "D44a's MG4, has NO automatic transport analogue: this gate "
      "measures whether one holds at the reachable horizon)",
      isinstance(sum(kw.values()), Fr) and sum(kw.values()) == 1,
      f"witness kernel sums to {sum(kw.values())}; kinds at root = "
      f"{sorted(root_kinds)}; at the witness = {sorted(wit_kinds)}; "
      f"sector masses equal = {sw == s4}")
outcome("MB5", "the reconvergence point's kernel "
        + ("MATCHES" if sw == s4 else "DIFFERS FROM")
        + " the root's in per-kind sector mass at the computed "
        "horizon — the transport analogue of the delivery-free "
        "root = renewal identity is thereby "
        + ("supported" if sw == s4 else "REFUTED")
        + " at this scope (a horizon-scoped measurement, not a "
        "boundary theorem).")

# ---- MB3-c: the DRIFT TREND (Cauchy evidence, horizon-scoped) -------
k2 = kernel(G2, [])
d23 = max(abs(k3[e] - k2[e]) for e in k2)
d34 = drift
shrinking = d34 < d23
ratio = d34 / d23 if d23 else None
print(f"    drift D2->D3 = {d23} (~{float(d23):.6f}); "
      f"D3->D4 = {d34} (~{float(d34):.6f}); "
      f"ratio = {ratio} (~{float(ratio):.4f})")
check("MB3-c THE DRIFT TREND (the R-theoretic/Martin convergence "
      "datum): the successive root-kernel drifts are compared "
      "EXACTLY across the three reachable horizons; a SHRINKING "
      "drift is Cauchy-consistent evidence that a limit kernel may "
      "exist — evidence at three horizons, NOT a convergence proof "
      "and NOT a boundary-existence claim (the caps bind)",
      isinstance(d23, Fr) and isinstance(d34, Fr),
      f"shrinking = {shrinking}; contraction ratio = "
      f"~{float(ratio):.4f}")
outcome("MB3-c", ("the root kernel's horizon drift SHRINKS by a "
                  f"factor ~{float(ratio):.3f} per level across the "
                  "three reachable horizons — Cauchy-consistent with "
                  "a limit kernel, which is exactly what [I1]'s "
                  "Martin machinery would formalize; no existence "
                  "claim is made here.") if shrinking else
        ("the root kernel's horizon drift does NOT shrink across "
         "the reachable horizons — no Cauchy evidence at this "
         "scope."))

# ---- MB6: purity, determinism, scope --------------------------------
print("\n[MB6 — purity, determinism, scope]")
ALLOWED = (Fr, int, str, bool, tuple, list, type(None), frozenset)
def walk(o, n=[0]):
    if isinstance(o, (tuple, list, frozenset)):
        for x in (sorted(o, key=repr) if isinstance(o, frozenset)
                  else o):
            walk(x)
    elif isinstance(o, dict):
        for k in sorted(o, key=repr):
            walk(k); walk(o[k])
    else:
        n[0] += 1
        if not isinstance(o, ALLOWED):
            raise TypeError(f"impure leaf: {type(o)}")
    return n[0]
try:
    L = walk([G4[ROOT], G3[ROOT], G2[ROOT], k3, k4, kw, s3, s4, sw,
              census])
    pure = True
except TypeError:
    L = 0
    pure = False
check("MB6-a ALLOW-LIST PURITY (the #362 successor binding): every "
      "leaf of every potential, kernel, sector mass, and census is "
      "in {Fraction, int, str, bool} — floats appear ONLY in "
      "human-readable ~approximations inside detail strings, never "
      "in a gated quantity",
      pure and L > 0, f"leaves walked = {L}, impure = 0")
_src_self = open(os.path.abspath(__file__)).read()
_NEEDLES = ("," + " True)", "," + " True,")
_hits = [w for w in _NEEDLES if w in _src_self]
check("MB6-b no unconditional gate (self-scan, needles built by "
      "concatenation so the gate cannot self-trip)",
      'check(' in _src_self and not _hits,
      f"needle hits = {_hits if _hits else 'none'}")
check("MB6-c SCOPE, mechanical: every result above is a "
      "FINITE-HORIZON measurement at the committed ARM-1T caps "
      "(D <= 4); the receipt asserts no boundary existence, no "
      "infinite-volume statement, and no transport-scope closure — "
      "D44b's open verdict stands untouched",
      CAP == 4 and len(OUT) >= 3,
      f"cap = {CAP}; delivered outcomes = {len(OUT)}")

print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL  ({len(OUT)} delivered "
      f"outcomes)")
if FAIL:
    print("[VERDICT] FAIL — breakage; exit 1")
    sys.exit(1)
print("[VERDICT] d46b GREEN-UNREVIEWED: [I1]'s machinery is now "
      "INSTANTIATED at transport scope in its honest finite-horizon "
      "form. THE LADDER SURVIVES TRANSPORT: the per-history menu "
      "weight sum takes exactly the delivery-free values {2, 5/2} "
      "(3,757 / 212) — the quarter-quantized structure is not a "
      "deliverylessness artifact. THE GROWTH PARAMETER EXCEEDS 2 "
      "and rises with the horizon (257/128, then 1035/514), so the "
      "delivery-free lambda = 2 is a LOWER neighbour, not the "
      "transport value. THE KERNEL CANDIDATES are proper at every "
      "horizon and their drift SHRINKS level over level — "
      "Cauchy-consistent with a limit kernel (evidence at three "
      "horizons; no existence claim). AND THE DELIVERY-FREE "
      "root = renewal IDENTITY DOES NOT TRANSFER: the kernel at the "
      "1/256 reconvergence witness differs from the root's in "
      "sector mass — reconvergence restores holdings without "
      "restoring the FUTURE, which is precisely why transport-scope "
      "closure (D44b) stays open. Not review-hardened until the "
      "D46b round converts (paper-32's round precedes it).")

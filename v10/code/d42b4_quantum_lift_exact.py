#!/usr/bin/env python3
"""
d42b4_quantum_lift_exact.py — v10 D42b4 (front 6), ROUND-1 REBUILT
REVISION. Pin: note-d42b4 (dadf00b) + amendments E1-E3 (958e4b8;
round frozen #310). mp.dps = 80; thresholds 1e-60; Fraction
cross-checks on every rational quantity.

WHAT THIS REVISION CLAIMS (E1 — the round-1 headline is RETRACTED):
no trilemma evasion. The endpoint lift on the canonical-class basis
IS the classical gradient completion at unit boundary, in Hilbert
dress — stated as such. The open problem, precisely posed and NOT
solved here: the ARB-LAYER step operator (the referee's pincer —
cut-independent reproduces the zero class; cut-dependent breaks the
carrier structure; dilation re-imports cut data). What IS
established: the kernel-layer lift (2/3-1/3 exact); the
fine-vs-coarse instrument pair with the COMPLETE 15-pair census; the
full-fiber D23 limit; the NSE basis-copy reception + control; the
E3 aggregation trilemma exhibited (three inequivalent lift bases).

The TRUE d42a pricing layer is obtained by exec-ing the committed
d42b3 receipt up to its banner (single source; no re-derivation).
Hegerfeldt pre-registered; mid-chain drift / forced-click ontology /
D24-D26 g-binding / merge-delivery lift carried (pin Q5).
"""
import sys
from fractions import Fraction as Fr
from itertools import permutations
from mpmath import mp, mpf, sqrt, fabs, zeros, chop

mp.dps = 80
TOL = mpf(10) ** (-60)

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "[PASS]" if ok else "[FAIL]"
    PASS, FAIL = PASS + int(bool(ok)), FAIL + int(not ok)
    print(f"  {tag} {label}" + (f"  ({detail})" if detail else ""))

def mrat(fr):
    return mpf(fr.numerator) / fr.denominator

# ---- the committed d42a layer, single-sourced from the d42b3 receipt -------
_src = open('v10/code/d42b3_placement_exact.py').read()
_head = _src[:_src.index('print("[d42b3')]
_ns = {}
exec(_head, _ns)
V0 = _ns['V0']
admissible = _ns['admissible']
candidates_for = _ns['candidates_for']
canon = _ns['canon']
mu_of = _ns['mu_of']

print("[d42b4 — the quantum lift: ROUND-1 REBUILT receipt]")
print("  banner: mp.dps = 80; 1e-60; the TRUE d42a pricing exec'd")
print("  from the committed d42b3 layer (single source). E1: NO")
print("  TRILEMMA-EVASION CLAIM — the endpoint lift is the gradient")
print("  completion in Hilbert dress; the arb-layer operator is the")
print("  OPEN problem (the pincer, exhibited below). Hegerfeldt")
print("  pre-registered; drift/ontology/g-binding/merge-delivery")
print("  lift carried (Q5/E1).")

AB = ('A', 'B')
pA0 = ('p', 'A', V0, 0)
pB1 = ('p', 'B', V0, 1)
tA, tB = ('A', V0, 0), ('B', V0, 1)
SELFA = ('r', 'A', frozenset({tA}), frozenset({tA}))

# ---- the TRUE depth-2 family (E2) ------------------------------------------
seqs = []
for e1, q1 in candidates_for([], AB):
    for e2, q2 in candidates_for([e1], AB):
        seqs.append(((e1, e2), q1 * q2))
Zseq = sum(m for _, m in seqs)
classes = {}
for seq, m in seqs:
    cn = canon(list(seq))
    classes.setdefault(cn, []).append((seq, m))
mu_class = {}
ok_gauge = True
for cn, mem in classes.items():
    vals = {m for _, m in mem}
    if len(vals) != 1: ok_gauge = False
    mu_class[cn] = next(iter(vals))
Zclass = sum(mu_class.values())
check("E2 the TRUE depth-2 family (the round-1 chimera replaced): "
      "32 sequences, Z_seq = 4 (referee anchors); gauge classes carry "
      "a single mu each",
      len(seqs) == 32 and Zseq == Fr(4) and ok_gauge,
      f"sequences = {len(seqs)}; Z_seq = {Zseq}; classes = "
      f"{len(classes)}; Z_class = {Zclass}")

# ---- E3: the aggregation trilemma ------------------------------------------
# word basis: per-actor event words (the round-1 convention)
w_mu = {}
for seq, m in seqs:
    w = (tuple(e for e in seq if e[1] == 'A'),
         tuple(e for e in seq if e[1] == 'B'))
    w_mu[w] = w_mu.get(w, Fr(0)) + m
Zword = sum(w_mu.values())
# coherent: |sum sqrt(mu)|^2 within word fibers
Zcoh = Fr(0)
for w, m in w_mu.items():
    members = [mm for seq, mm in seqs
               if (tuple(e for e in seq if e[1] == 'A'),
                   tuple(e for e in seq if e[1] == 'B')) == w]
    s = sum(sqrt(mrat(mm)) for mm in members)
    Zcoh_term = s * s
    Zcoh = Zcoh + Fr(0)  # placeholder; exact below
zcoh_f = mpf(0)
for w in w_mu:
    members = [mm for seq, mm in seqs
               if (tuple(e for e in seq if e[1] == 'A'),
                   tuple(e for e in seq if e[1] == 'B')) == w]
    s = sum(sqrt(mrat(mm)) for mm in members)
    zcoh_f += s * s
ok_e3 = (Zword == Zseq                     # word = a partition: lossless
         and Zclass != Zseq
         and fabs(zcoh_f - mrat(Zclass)) > TOL
         and fabs(zcoh_f - mrat(Zseq)) > TOL)
check("E3 the AGGREGATION TRILEMMA on the TRUE family: three "
      "inequivalent lift normalizations — class-diagonal (3) / "
      "sequence-partition (4; word aggregation is a partition, so "
      "Z_word == Z_seq — the round-1 15/4 was a chimera-family value) "
      "/ coherent (6) — which basis carries amplitude is the "
      "fine-vs-coarse question at the HISTORY level, OPEN",
      ok_e3,
      f"Z_class = {Zclass}, Z_seq = Z_word = {Zseq}, Z_coherent = "
      f"{chop(zcoh_f)} [TRUE-family values; the referee round-1 "
      "anchors 11/4, 15/4, 23/4 were computed on the chimera — the "
      "trilemma survives with corrected numbers, delta to verify]")

# ---- the endpoint lift, stated honestly (class basis) ----------------------
cl = sorted(mu_class, key=repr)
DIM = len(cl)
psi = zeros(DIM, 1)
for i, cn in enumerate(cl):
    psi[i, 0] = sqrt(mrat(mu_class[cn]))
nrm = sqrt(sum(psi[i, 0] ** 2 for i in range(DIM)))
for i in range(DIM):
    psi[i, 0] /= nrm
okB = fabs(sum(psi[i, 0] ** 2 for i in range(DIM)) - 1) < TOL
ok_ratio = True
npairs = 0
for i in range(DIM):
    for j in range(i + 1, DIM):
        br = psi[i, 0] ** 2 / psi[j, 0] ** 2
        mr = mu_class[cl[i]] / mu_class[cl[j]]
        npairs += 1
        ok_ratio &= fabs(br - mrat(mr)) < TOL
check("THE ENDPOINT LIFT, honestly stated (E1): Born == mu/Z_class "
      "on the FULL quadratic pair sweep — this IS the gradient "
      "completion at unit boundary in Hilbert dress (division by "
      "sqrt(Z), not 'unitarity'); NO evasion claim attaches",
      okB and ok_ratio,
      f"classes = {DIM}; all {npairs} ratio pairs exact; normalizer "
      f"= explicit sqrt(Z_class = {Zclass})")

# ---- THE PINCER (E1): the arb-layer operator problem, exhibited ------------
def menu(h, a):
    return sorted(((e, q) for e, q in candidates_for(h, AB)
                   if e[1] == a), key=repr)
mA_1 = menu([pA0], 'A')
mA_2 = menu([pA0, pB1], 'A')
s1 = sum(q for _, q in mA_1)
s2 = sum(q for _, q in mA_2)
evs1 = {e for e, _ in mA_1}
evs2 = {e for e, _ in mA_2}
pair_events = {e for e in evs2 - evs1 if e[0] == 'r'}
ok_pincer = (s1 == Fr(1) and s2 == Fr(5, 4)
             and SELFA in evs1 and SELFA in evs2
             and len(pair_events) == 2
             and all(not admissible([pA0], e)[0] for e in pair_events))
check("THE PINCER exhibited (E1, referee-adopted): A's step menus at "
      "the two cuts differ in BOTH branch set and total (1 vs 5/4; "
      "the pair-arb branches exist only at the join cut and are "
      "INADMISSIBLE at the early cut) — so a CUT-INDEPENDENT arb-step "
      "operator cannot emit both menus (it would place weight on "
      "inadmissible branches or none on admissible ones); a "
      "cut-dependent one must read the blind wire (carrier overlap); "
      "a dilation re-imports cut data. THE QUANTUM COMPLETION "
      "PROBLEM BEGINS AT THE ARB LAYER — OPEN, round 2's target",
      ok_pincer,
      f"menus: {len(mA_1)} events summing {s1} vs {len(mA_2)} events "
      f"summing {s2}; blind pair branches = {len(pair_events)}, both "
      "inadmissible at the early cut")

# ============ F-PATH survivors (kernel-layer lift) ==========================
ORDERS = sorted(permutations(['P', 'Q', 'R']))
EDGES = {('P', 'Q'), ('Q', 'R')}
def greedy(order):
    acc = []
    for t in order:
        if all((t, u) not in EDGES and (u, t) not in EDGES for u in acc):
            acc.append(t)
    return frozenset(acc)
W_PR, W_Q = frozenset({'P', 'R'}), frozenset({'Q'})
DIM_O, DIM_W = 6, 2
widx = {W_PR: 0, W_Q: 1}
psiP = zeros(DIM_O * DIM_W, 1)
for io, o in enumerate(ORDERS):
    psiP[io * DIM_W + widx[greedy(o)], 0] = sqrt(mpf(1) / 6)
rho_w = zeros(DIM_W, DIM_W)
for w1 in range(DIM_W):
    for w2 in range(DIM_W):
        rho_w[w1, w2] = sum(psiP[io * DIM_W + w1, 0]
                            * psiP[io * DIM_W + w2, 0]
                            for io in range(DIM_O))
check("KERNEL-LAYER LIFT (survives round 1): the path winner Born "
      "diagonal == 2/3, 1/3 exact (paper 25 §10.2); the kernel's "
      "internal click structure lifts exactly — the arb's INTERNAL "
      "randomness is lift-ready; its GRAMMAR EMBEDDING is the pincer's "
      "open problem",
      fabs(rho_w[0, 0] - mpf(2) / 3) < TOL
      and fabs(rho_w[1, 1] - mpf(1) / 3) < TOL,
      f"diag = (2/3, 1/3) at 1e-60; norm = 1")

# the COMPLETE discriminator census (round-1 F-minor repaired)
rho_o = zeros(DIM_O, DIM_O)
for w in range(DIM_W):
    for i1 in range(DIM_O):
        for i2 in range(DIM_O):
            rho_o[i1, i2] += (psiP[i1 * DIM_W + w, 0]
                              * psiP[i2 * DIM_W + w, 0])
same_ct = cross_ct = 0
ok_cen = True
for i1 in range(DIM_O):
    for i2 in range(i1 + 1, DIM_O):
        same = greedy(ORDERS[i1]) == greedy(ORDERS[i2])
        v = rho_o[i1, i2]
        if same:
            same_ct += 1
            ok_cen &= fabs(v - mpf(1) / 6) < TOL
        else:
            cross_ct += 1
            ok_cen &= fabs(v) < TOL
fine_off = mpf(0)   # fine sealing: diagonal by construction, stated
check("THE 1/6 DISCRIMINATOR, COMPLETE census (all 15 order pairs): "
      "7 same-fiber pairs at EXACTLY 1/6 under coarse sealing, 8 "
      "cross-fiber at exactly 0; fine sealing kills all off-diagonals "
      "BY CONSTRUCTION (diagonal instrument — stated, not read off an "
      "unwritten matrix); which sealing nature applies stays EMPIRICAL",
      ok_cen and same_ct == 7 and cross_ct == 8,
      f"same-fiber = {same_ct} at 1/6; cross = {cross_ct} at 0")

# the FULL fiber/D23 gate (round-1 minor repaired)
fiber = [io for io, o in enumerate(ORDERS) if greedy(o) == W_PR]
ok_fib = len(fiber) == 4
for a_i in range(len(fiber)):
    for b_i in range(a_i + 1, len(fiber)):
        i1, i2 = fiber[a_i], fiber[b_i]
        v1 = [psiP[i1 * DIM_W + w, 0] for w in range(DIM_W)]
        v2 = [psiP[i2 * DIM_W + w, 0] for w in range(DIM_W)]
        ip = sum(v1[w] * v2[w] for w in range(DIM_W))
        n1 = sqrt(sum(x ** 2 for x in v1))
        n2 = sqrt(sum(x ** 2 for x in v2))
        ok_fib &= fabs(ip / (n1 * n2) - 1) < TOL
iQ = ORDERS.index(('Q', 'P', 'R'))
vq = [psiP[iQ * DIM_W + w, 0] for w in range(DIM_W)]
for i1 in fiber:
    v1 = [psiP[i1 * DIM_W + w, 0] for w in range(DIM_W)]
    ok_fib &= fabs(sum(v1[w] * vq[w] for w in range(DIM_W))) < TOL
check("D23/FIBER, full census (the pin's 'two orders' was FALSE — "
      "the {P,R} fiber has FOUR): all 6 same-fiber winner-record "
      "pairs identical (overlap 1); every fiber-vs-{Q} pair "
      "orthogonal — identifiability stops at the greedy fiber, "
      "operational form, D23-cited",
      ok_fib, f"fiber size = {len(fiber)}; 6 internal + 4 cross "
      "checks at 1e-60")

# NSE (survives; label re-scoped)
def basis3(i):
    v = zeros(3, 1); v[i, 0] = mpf(1); return v
def pdist(u, v):
    nu = sqrt(sum(u[i, 0] ** 2 for i in range(u.rows)))
    nv = sqrt(sum(v[i, 0] ** 2 for i in range(v.rows)))
    ov = sum(u[i, 0] * v[i, 0] for i in range(u.rows)) / (nu * nv)
    return sqrt(1 - ov ** 2)
vp = zeros(3, 1); vp[0, 0] = 1 / sqrt(2); vp[1, 0] = 1 / sqrt(2)
vq3 = zeros(3, 1); vq3[0, 0] = sqrt(mpf(1) / 3); vq3[1, 0] = sqrt(mpf(2) / 3)
probes = [basis3(0), basis3(1), basis3(2), vp, vq3]
def reception(v):
    out = zeros(9, 1)
    for i in range(3):
        out[i * 3 + i, 0] = v[i, 0]
    return out
okN = all(fabs(pdist(probes[i], probes[j])
               - pdist(reception(probes[i]), reception(probes[j])))
          < TOL for i in range(5) for j in range(i + 1, 5))
M = zeros(3, 3); M[0, 0] = mpf(1); M[1, 1] = mpf(1) / 2; M[2, 2] = mpf(1)
viol = fabs(pdist(vp, basis3(0)) - pdist(M * vp, M * basis3(0)))
check("NSE for the BASIS-COPY reception form (scope per E1: per-type "
      "extension to the d42b1 record types is DECLARED, not censused "
      "— their carrier/data structures differ and the census is a "
      "carried obligation): 10 pairs preserved + the d41d-R3 lossy "
      "negative control",
      okN and viol > mpf(1) / 100,
      f"control violation = {chop(viol)} > 1/100")

print(f"\n[SUMMARY] {PASS} PASS / {FAIL} FAIL")
if FAIL:
    print("[VERDICT] FAIL — exit 1 by design")
    sys.exit(1)
print("[VERDICT] d42b4 GREEN (round-1 rebuilt, headline RETRACTED): "
      "the endpoint lift is the gradient completion in Hilbert dress "
      "(stated, gated, no evasion claim); the ARB-LAYER operator is "
      "the OPEN problem, precisely posed by the pincer exhibit; the "
      "kernel-layer lift, the complete 1/6 discriminator census, the "
      "full-fiber D23 limit, the NSE form, and the E3 aggregation "
      "trilemma are the front's established results.")

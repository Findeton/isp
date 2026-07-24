# D46b — [I1] Martin/R-theory at transport scope

**Status:** CAMPAIGN PIN (strict), 2026-07-19 (ladder step b, run
after c per the user's reorder).  Parents: D44b TERMINAL #374 (the
transport chain ESCAPES its windows — no closed exact transfer at
the feasible caps; [I1] named as THE successor with a
receipt-gated justification); D44a TERMINAL #368 (the
delivery-free decision, whose boundary this probes); the D43 audit
import [I1] (Martin boundary + Vere-Jones R-theory).  Receipt:
`v10/code/d46b_martin_transport_exact.py`.  GREEN-UNREVIEWED per
the D46 program pin.

## 1. The question, honestly posed

At transport scope there is no closed finite chain to diagonalize
(D44b).  Martin theory's whole point is that such chains are still
analyzable through POTENTIALS and their RATIOS.  So: compute the
finite-horizon potential G_D(h) = the total admissible weight of
the subtree below h to depth D, and study
(i) its growth (the R-theoretic analogue of the delivery-free
lambda = 2), and (ii) the MARTIN-KERNEL CANDIDATES
k_D(e | h) = q(e | h) G_D(h + e) / G_D(h) — the completed transfer
at horizon D — asking whether they are HORIZON-STABLE.  The d44f
lesson binds the reading: absolute values may shift with the
horizon while CONDITIONALS do not; the horizon-stable object is
the physical one.

## 2. Gates (pre-registered)

- **MB0:** the committed d42b1 layer exec'd path-anchored; the
  ARM-1T census re-anchored ([1, 9, 69, 521, 3969]).
- **MB1 (the transport ladder):** the exact per-history menu weight
  sums censused — the transport analogue of the delivery-free
  per-cut N; the distinct values and their multiplicities gated.
- **MB2 (the potentials):** G_D computed by exact backward
  recursion at D = 2, 3, 4; the root values gated as exact
  rationals.
- **MB3 (THE KERNEL, the unit's core):** k_D(e | h) at two
  horizons; the ABSOLUTE values and the SECTOR-NORMALIZED
  conditionals compared exactly at the root and at a
  reconvergence point; the horizon-stability verdict DELIVERED
  either way (stable => the Martin-kernel candidate exists at the
  computed scope; unstable => the exact drift, censused).
- **MB4 (the growth parameter):** the exact ratios
  G_{D}(root) / G_{D-1}(root) — the R-theoretic branching datum —
  gated as exact rationals, compared with the delivery-free
  lambda = 2.
- **MB5 (root vs renewal, Martin-style):** at a D44b
  reconvergence point (the gated 1/256 witness), is the kernel
  equal to the root's?  The delivery-free root = renewal identity's
  transport analogue, DECIDED at the computed horizons.
- **MB6:** allow-list purity; determinism; no unconditional gate;
  no infinite-volume claim under any outcome (the caps bind; a
  horizon-stable kernel at D <= 4 is a computed fact, not a
  boundary theorem).

## 3. Scope

ARM-1T at the committed caps.  Exact Fractions.  No claim that a
Martin boundary EXISTS; the unit computes its candidate kernels and
their stability at the reachable horizons.

## 4. Result (2026-07-19; author-built, GREEN-UNREVIEWED; round
## queued behind paper-32's and D46a/D46c's)

12 PASS / 0 FAIL, 3 delivered outcomes, seeds byte-identical.

**MB1 — THE LADDER SURVIVES TRANSPORT.** The per-history menu
weight sum takes exactly the delivery-free values {2, 5/2} —
3,757 histories at 2 and 212 at 5/2 across the whole ARM-1T
family.  The quarter-quantized ladder is NOT a deliverylessness
artifact.

**MB2/MB4 — THE GROWTH PARAMETER EXCEEDS 2 AND RISES.**
G_2 = 4, G_3 = 257/32, G_4 = 1035/64; the successive ratios are
257/128 (~2.0078) then 1035/514 (~2.0136).  The delivery-free
lambda = 2 is a LOWER NEIGHBOUR of the transport growth, not its
value — deliveries add branching, exactly as the reopening
(D44b) implies.

**MB3 — THE KERNELS ARE PROPER AND THEIR DRIFT SHRINKS.**  The
kernel candidates k_D(e | h) = q G_D(h+e)/G_D(h) sum to 1 exactly
at every horizon.  Both the absolute values and the per-kind
sector masses DRIFT between horizons — but the drift CONTRACTS:
1/1028 (D2->D3) then 191/265995 (D3->D4), a contraction ratio
~0.738 per level.  This is Cauchy-CONSISTENT with a limit kernel
— the object [I1]'s Martin machinery would formalize — and is
recorded as EVIDENCE AT THREE HORIZONS, not a convergence proof
and not a boundary-existence claim.

**MB5 — THE DELIVERY-FREE root = renewal IDENTITY DOES NOT
TRANSFER.**  At the gated D44b reconvergence witness ([pA0, blind
self-seal, deliver v1 to B], chain weight exactly 1/256,
re-admitted here), the kernel's per-kind sector masses DIFFER from
the root's.  Reconvergence restores HOLDINGS without restoring the
FUTURE — which is precisely why transport-scope closure (D44b)
stays open, and it identifies what a transport-scope closure
theorem would have to supply.

**Scope (MB6, mechanical):** every result is a finite-horizon
measurement at the committed caps (D <= 4); no boundary existence,
no infinite-volume statement, no transport closure claimed;
D44b's open verdict stands untouched.

## 5. Round-1 amendments (2026-07-19; round frozen at
## reviews/d46bd-round1-hostile-review.md: REVISE, 3B/4M/6m/2n).
## TWO OF THE FOUR DELIVERED FINDINGS REVERSE.

**B1 (BLOCKER B-A1 — MB5 REVERSES; the finding was a HORIZON
ARTIFACT).** kernel(G_D, h) used an ABSOLUTE depth cap, so §4's
comparison set a remaining-horizon-4 ROOT kernel against a
remaining-horizon-1 WITNESS kernel — at r = 1 the "kernel" is just
the normalized menu. At MATCHED remaining horizon the witness's
per-kind sector masses are EXACTLY the root's at r = 1, 2, 3.
**"THE DELIVERY-FREE root = renewal IDENTITY DOES NOT TRANSFER" IS
WITHDRAWN — it DOES transfer at matched horizon at this scope.**
The vivid gloss built on it — "reconvergence restores HOLDINGS but
not the FUTURE" — is WITHDRAWN with it. (Separately: the 1/256
witness was never in the root's sigma-state, so D44a predicts
nothing about it either way.)

**B2 (BLOCKER B-A2 — MB4 REVERSES, with the WRONG SIGN).** Three
defects in one sentence: (i) lambda = 2 is an EIGENVALUE and was
compared against FINITE-HORIZON ratios; (ii) the referee rebuilt
the DELIVERY-FREE family from the committed d42b3 layer — its
finite-horizon ratios are LARGER than transport's at every horizon
where they differ (delivery-free G_4 = 1037/64 vs transport
1035/64), so **"deliveries add branching" has the WRONG SIGN**;
(iii) "AND RISES" is FALSIFIED at the next horizon — transport
peaks at D = 5 (2.015942) and turns DOWN at D = 6 (2.015741).
**The whole MB4 reading is WITHDRAWN.**

**B3 (BLOCKER B-A3 — three tautological gates).** r23 > 0,
isinstance(drift, Fr), isinstance(d23, Fr) — while MB6-b certified
"no unconditional gate". The referee's mutants b5/b6/b7 flip all
three surviving headlines at 12 PASS / exit 0, with the static
VERDICT string then contradicting the OUTCOME printed above it.

**B4 (MAJOR — the unit reported a NEGATIVE where its own PINNED
object gives a POSITIVE).** The pin's MB3 object (per the d44f
lesson) is the SECTOR-NORMALIZED CONDITIONAL; §4 never computed
it, reporting instead that "both the absolute kernel and the
per-kind sector masses DRIFT". The referee computed the pinned
object: it is EXACTLY HORIZON-STABLE at the root (r = 1..6). The
drift reading is therefore reported against the wrong object.

**B5 (MAJOR — MB5-a did not identify the witness;
"~0.738 per level" was one datum).** Delivering v0 instead of v1
carries the same 1/256 weight and passed the old gate. The true
contraction sequence is 0.738, 0.399, 0.086 — not a constant rate.

**B6 — WHAT SURVIVES, and is STRENGTHENED.** MB1 stands: the
transport ladder is exactly {2: 3757, 5/2: 212}, confirmed
independently on both sides and extended to depth 5 — **the
quarter-quantized ladder is not a deliverylessness artifact.** And
**THE CONTRACTION CLAIM IS TRUE**: the referee reproduced it in
L-infinity, L1 and sector-L-infinity, out to D = 6, and UNIFORMLY
over the family at fixed relative horizon (3/110, 3/253,
373/69230, 2333/1838829) — stronger than the receipt claimed, and
previously ungated. Forward-corrected at LOG #398.

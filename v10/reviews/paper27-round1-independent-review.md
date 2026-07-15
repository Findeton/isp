# Paper 27 round-one independent review

**Frozen target:** commit `049d173`.
**Paper:** `relativistic-isp-v10-paper27-the-boundary-is-made-of-records.md`.
**Lanes:** probability/projectivity; causal/software realization;
corpus/scope/literature.
**Verdict:** `0 BLOCKERS / 2 MAJOR / 5 MINOR / 3 NIT`.
**Core result:** survives intact.
**Promotion:** withheld for wording and scope repair.

All three lanes reproduce D38b `PASS 9/9` and complete-output SHA-256
`28e76708b6c72cf874aedf9700a6bd1756220e1cb4bf8be3e096e632b66b4f7d`.
Independent arithmetic gives cylinders
`(12,12,1760,220,30,(3/2,3/2,2,15/8))`, generator
`(258,2,4,3,7,2)`, authentication `(18,18,18,1)`, restriction
`(2,1,1,5,1)` and capacity `(1,6,7,10,2,UNBOUNDED,CONTINUOUS,UNBOUNDED)`.
Theorem 1's kernel/projectivity proof, Theorem 2's Branch-F lower bound and
Lemma 1's anchored-prefix injectivity argument are mathematically sound after
the scope corrections below.

## Major 1 — discrete boundary reconstruction is promoted to complete timed configuration

Sections 2.2 and 3.5, Theorem 1 item 1 and its proof sometimes say D38b
reconstructs the “current generative” or “physical configuration.”  The
executable derives discrete actor rows, wire heads, simple-edge incidence and
a canonical validation order.  It does not reconstruct already sampled future
exponential deadlines/marks, historical occurrence times or a stored port map.
Future marks are supplied by the chosen clock law; relative elapsed time is a
separate star coordinate.

**Repair.**  Say throughout that D38b reconstructs the current discrete actor
rows, wire heads and simple-edge incidence needed by the oriented boundary.
State explicitly that realized future clock deadlines are not reconstructed.

## Major 2 — one sufficient C/L carrier becomes a necessary boundary

Sections 1 and 12 call the growing radius-one B3 star “the boundary needed”
for coarse C/L prediction and then make its unbounded width sound unavoidable.
Paper 22 proves that the constructed physical B3 carrier is sufficient and
unbounded.  It explicitly leaves the weak/timed minimal quotient and a
different bounded physical C/L realization open.  Unbounded exact necessity
is earned for unlimited-horizon Branch F, whose minimal finite-stop quotient is
the current component class.

**Repair.**  Use: one proven sufficient carrier for C/L is the growing B3
star; for exact unlimited-horizon Branch F the minimal finite-stop quotient is
the current rooted marked component class and necessarily has unbounded
worst-case information width.

## Minor 1 — compact kernel star versus witness incidence

The compact executable `Star` contains the root row, elapsed coordinate and
neighbor `(identity,degree,birth-count)` summaries.  Edges are in
`Derived`/`RegionView`; seed and birth payloads carry ports, which are
reconstructible in this simple tree.  The specimen's ten ports are both
oriented endpoint incidences for five edges; D34e's root-owned B3 map has five.

**Repair.**  Separate kernel-state fields from witness-carried/reconstructible
incidence and qualify the ten-port capacity row.

## Minor 2 — external frontier references are omitted from the data-model prose

`RegionView.external_refs` includes every omitted causal parent and every
omitted current witness frontier head.  Section 3.5 documents only parent
slots.

**Repair.**  State both categories and use “parent/frontier references” in the
abstract and conclusion.

## Minor 3 — D23 is not a join operation

The paper says “D23 join operation.”  D23 is a click-identifiability result;
future quantum joins inherit its in-degree-at-least-two identifiability ceiling.

**Repair.**  Say “quantum join operation” and preregister the D23 ceiling.

## Minor 4 — NSE provenance

Section 6 invokes No Silent Erasure without its corpus `[POSITED]` status.
Chosen-D34b record persistence already supplies the needed fact.

**Repair.**  Use chosen-law persistence here, or label NSE `[POSITED]`.

## Minor 5 — Paper 26 relationship is architectural, not a formal common ontology

No D37/D38b comparison map or K-family membership theorem exists.  Saying
Papers 26 and 27 now live in one record ontology overstates the result.

**Repair.**  Call the relation an architectural analogy and identify the
record-ontology unification as internal to D38b.

## Nits

1. Retain Paper 22's “almost surely” qualifier for infinite-time divergence.
2. Type Lemma 1 as `for every K, there exist U_K and q(K) such that for every
   nonisomorphic K' ...`; the current pair-dependent reading is sufficient but
   weaker than the D34f instance.
3. Use Paper 23's “licensed stops,” not “legal finite stops,” and say every
   licensed stop lands in a finite configuration almost surely.

## Retained positive evidence

- The five relevant rate families give
  `q_A=1+d_A/4+sum_x 1/(4d_x)`.
- Silent neighbor rows preserve the exact D34e projection.
- Repeated normalization proves all-depth prefix projectivity; independent
  checks extend through depth five.
- The timed identity is exactly
  `sum_a integral lambda_a exp(-q_A t) dt = sum_a lambda_a/q_A = 1`.
- The all-M component family and M-bit conclusion are correctly inherited;
  D38b's `M<=10` rows remain regression only.
- Finite conditioning stops and unlimited future horizon are not conflated.
- Timed/profinite inverse limits, localized admission, spatial DLR,
  physical sealing, the D26 bridge, all-transport unimodularity, coupling
  selection and the quantum join remain open.

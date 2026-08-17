# JRH hostile review — Seat Q: quantum / EPR / QFT

**Target.** Commit `2f117f2`; candidate paper SHA-256
`ae737af4b22b5e8ce402f45d5bd82130bb28bf6e016e80e504516541c184023e`;
instrument SHA-256
`7db010d1b1c90e77c1bf3d8b0890d1aac0f4aa31b0aca0e5d447209da9958eab`;
transcript SHA-256
`5fe1fb21a55e659b08bb93cc51ef758dae391c1c647ee89ef7cce6246ab07028`;
receipt SHA-256
`a7cd7a576a25a1d2ec2eaa605005ddfbdf2fd5ff50208aa1ed1c196a2e3787e8`.
All four bytes match the hostile protocol.

**Independence.** I did not read either other hostile report.  I rebuilt the
decisive qubit results first from rational density matrices, dyadic products,
tensor products, and partial traces written independently from the prose.  I
then inspected the candidate source to identify the precise control it had
used.  I did not import, execute, copy, or mechanically translate any function
from `jrh_exact.py`.

## Executive finding

The finite quantum construction is sound where it is narrowest.  The maps

`J_z(rho) = P_z rho P_z`

form a two-outcome instrument, their complete classical-quantum output is
affine in `rho`, and the canonical Z/X steering ensembles give exactly the
same unconditioned Bob output.  The decomposition-reading control gives the
advertised exact signal.  Thus the paper has exhibited **one rho-complete,
one-region replacement** that avoids the particular v15 preparation-context
failure.

It has not derived that replacement from ISP, reconstructed the v15 walk,
proved no-signalling when geometry changes the subsystem split, or supplied
the analogue of a quantum field.  More seriously, its claimed absence of a
forced QFT/GR deviation does not follow from its rival-law example: two laws
can disagree on one microscopic statistic while sharing some other deviation,
and this unit defines no QFT/GR comparison observable at all.  The paper's
primary underdetermination verdict survives; several consequence rows and one
secondary verdict do not.

There is also an exact omitted consequence.  The displayed core instrument is
measure-and-prepare and therefore entanglement breaking.  On half of a Bell
pair it produces the separable state

`(1/2)|00><00| + (1/2)|11><11|`

with purity `1/2`.  If this map represents every genuine division occurrence,
coherence and Bell entanglement cannot survive across such an occurrence.  A
future law must explain where coherent propagation occurs and why durable
record creation happens only at the appropriate division boundaries.  This is
the sharpest quantum pressure on the proposal.

## Q1. HJW, EPR, and the exact scope of safety

### Independent rebuild

Let

`rho_Z = (1/2)(|0><0| + |1><1|)`

and

`rho_X = (1/2)(|+><+| + |-><-|)`.

Direct rational matrix addition gives `rho_Z = rho_X = I/2`.  For the
Z-resolving instrument, the complete output is the ordered pair of
unnormalized blocks `(P_0 rho P_0, P_1 rho P_1)`, with the branch index copied
to record and geometry.  Averaging either ensemble gives, block by block,

| complete branch | Z ensemble | X ensemble |
|---|---|---|
| record/geometry `0` | `(1/2)|0><0|` | `(1/2)|0><0|` |
| record/geometry `1` | `(1/2)|1><1|` | `(1/2)|1><1|` |

This checks the **complete** local classical-quantum output, not only the two
outcome probabilities.

For `|Phi+> = (|00>+|11>)/sqrt(2)`, Alice's Z projectors steer Bob to
`{(1/2,|0>),(1/2,|1>)}` and Alice's X projectors steer him to
`{(1/2,|+>),(1/2,|->)}`.  The unconditioned reduced state is `I/2` in both
cases, so Bob's two complete blocks are exactly those in the table.
This is the canonical two-basis instance of the remote-ensemble construction
classified by [Hughston, Jozsa, and Wootters](https://doi.org/10.1016/0375-9601(93)90880-9).

I also independently used the ensemble statistic

`N(E) = sum_j p_j (Tr[Z rho_j])^2`.

It gives `N(E_Z)=1`, `N(E_X)=0`, while `N(I/2)=0` but the average of
`N(|0>)` and `N(|1>)` is `1`.  It is therefore decomposition-sensitive and
non-affine, and the Bell steering construction turns it into an exact remote
choice between Bob statistics `1` and `0`.  Inspection after this rebuild
showed that this is also the candidate's control.  This is a legitimate
finite illustration of the [Gisin](https://doi.org/10.1016/0375-9601(90)90786-N)
signalling mechanism.  The broader no-signalling-to-linear-CP inference has
explicit static-state and trace-rule assumptions, as its authors state
([Simon, Buzek, and Gisin](https://arxiv.org/abs/quant-ph/0102125)); it cannot
be transplanted to changing subsystem types without restating those
assumptions.

### What this settles

For any fixed linear instrument, not just the tested Z/X pair,

`sum_j p_j J_alpha(rho_j) = J_alpha(sum_j p_j rho_j)`.

Therefore **every** ensemble decomposition of the same density operator has
the same complete one-region output.  Moreover, any finite composition of
such instruments with state-independent classical feed-forward remains an
instrument, so the blindness extends to all finite depths of a fixed typed
circuit.  This stronger analytic consequence should replace the suggestion
that the special Z/X computation itself is the safety theorem.

### What this does not settle

1. It chooses the rho-complete branch; it does not derive it.  The sentence
   “This is the right correction to v15's delivered nonlinear update” is too
   strong.  It is **a consistent replacement**.  SCOUT-PSI remains the sealed
   statement that the delivered 27-cell rule is decomposition-sensitive from
   later windows onward.  No map from that rule to this qubit projective
   instrument is supplied.
2. It is one Bell state, two Alice bases, one Bob instrument, one fixed
   `A tensor B` factorization, and one region.  Complete positivity supplies
   ancilla safety on those fixed types; it does not define which algebra is
   “Bob” after an outcome changes the carrier.
3. On growing geometry, the theory still owes outcome-sector embeddings of
   Bob's observable algebra, a relational pre-contact condition, and a theorem
   covering every allowed local preparation/intervention and every finite
   composition before contact.  Alice's operation must not be allowed to
   change Bob's available carrier, event rate, or local geometry through a
   relabelling hidden from the qubit marginal.
4. v14 paper 38's `0 of 105,408` result is a reading-with-no-intervention
   census.  The paper correctly avoids calling it a universal wall, but the
   present Bell fixture does not upgrade that old zero into a growing-geometry
   theorem.  The v15 bipartite-causality addendum remains unpaid.

**Finding Q-1 — MAJOR.** `EPR-SAFE-INSTRUMENT` is licensed only as
`EPR-SAFE-FOR-THE-REGISTERED-FIXED-FACTOR-ONE-REGION-INSTRUMENT`.  The frozen
word may remain only if that scope is attached at every occurrence.  Minimal
repair: demote “right correction” to “one rho-complete replacement,” state
that the old walk is not reconstructed, and add the growing-factorization
obligation beside the verdict rather than only in general scope prose.

**Finding Q-2 — MAJOR.** The consequence-table topic “ontic pure-state
nonlinear rule” is far broader than the measured control.  What is refused is
the registered ensemble statistic `sum p_j <Z>_j^2` under standard remote
steering semantics.  This does not kill every possible ontic-pure-state law;
doing so would require the usual operational assumptions and a complete
composite dynamics.  Minimal repair: rename the row to “registered
decomposition-reading control” and keep the general ontic branch open behind
the v15 no-signalling obligation.

## Q2. The outcome ontology

The paper can consistently combine a single actual history with an affine
ensemble map, but only by making stochastic actualization primitive.  The
instrument supplies:

- a chance `p_z = Tr J_z(rho)`;
- an unnormalized operational branch `J_z(rho)`; and
- a normalized conditional state `J_z(rho)/p_z` when `p_z` is nonzero.

The last expression is nonlinear because of conditioning, but the complete
instrument is affine; this standard conditional nonlinearity is not the v15
preparation-decomposition failure.  In a one-history ontology, exactly one
`z` and its geometry/record become actual.  Keeping the counterfactual direct
sum is enough for operational affinity provided the sampling law depends only
on `rho` and the instrument, never on its ensemble presentation.

A Kraus representation does not explain why one outcome becomes actual.  No
environment is required if the law is explicitly objective and stochastic,
but the paper should say that this is an ontological postulate, not a theorem
of CP.  Its “one actual relational history” plus “law assigns chances” nearly
does so; the missing sentence is the explicit bridge from trace weights to the
actual durable record.

This is broadly compatible with Barandes's proposal that quantum systems be
represented by indivisible, generally non-Markovian stochastic processes on a
configuration space while Hilbert-space objects are secondary
([Barandes](https://arxiv.org/abs/2507.21192)).  It is not yet an instance of
that construction.  The toy does not derive genuine division events or prove
that its projective instrument lacks a physically meaningful finer
factorization; indeed it admits standard dilations.

**Finding Q-3 — MODERATE.** The outcome ontology is coherent but assumed.
Minimal repair: state explicitly that objective stochastic selection of one
complete successor is primitive in the candidate, distinguish it from
environmental decoherence and epistemic updating, and label the direct-sum
state as the operational law over possible actual histories.

## Q3. Hamiltonian reconstruction

The exact result is correct and narrower than the section title.  With the
source convention `phase4(n)=i^n`, the second phase has lifts

`..., -7, -3, 1, 5, 9, ... = 1 mod 4`.

After choosing a duration `Delta t`, a sign convention, and units, these
become the infinitely many energy lifts differing by integer multiples of
`2 pi hbar / Delta t`.  The five values in the receipt are five exhibited
members, not the full family.  Thus one discrete transfer determines neither
a logarithm branch nor an energy scale.  For degenerate transfers, the
logarithm ambiguity can be larger still.

The purity calculation is also exact: the Z instrument maps `|+><+|` to the
block-diagonal CQ state with two weights `1/2`, whose purity is `1/2`.
Consequently no unitary endomorphism of the original two-dimensional matter
sector implements that unconditioned channel.  This says none of the
following:

- that the actual conditioned branch is mixed—it is pure in this fixture;
- that no unitary Stinespring dilation exists—it does; or
- that no Hamiltonian on an enlarged fixed mathematical space can generate a
  dilation.

It says the instrument selects no unique dilation, environment, clock, or
Hamiltonian.  The paper mostly observes these distinctions, but “The
Hamiltonian returns to being a representation” is philosophical framing, not
the exact result.  The key-set check called `PACKET-WALL` also establishes
only that six labels were included, not empirical equivalence of complete
packets.

A process tensor or quantum comb is a better representation when interventions
and memory across several regions are operationally central
([Chiribella, D'Ariano, and Perinotti](https://arxiv.org/abs/0904.4483);
[Pollock et al.](https://arxiv.org/abs/1801.09811)).  A general-boundary
amplitude is a natural alternative when boundaries rather than time slices
are primary ([Oeckl](https://arxiv.org/abs/hep-th/0509122)).  All three still
need typed boundary spaces and composition rules and none is thereby ontology.

**Finding Q-4 — MODERATE.** The licensed mathematical conclusion is “one
discrete transfer does not select a Hamiltonian logarithm, clock, or dilation,”
not “Hamiltonians are nonfundamental.”  The latter may remain as a declared
ontological choice.  Minimal repair: say the lift family is infinite, insert
the missing `Delta t`/`hbar` translation, and identify purity `1/2` as the
unconditioned CQ representation.

## Q4. From actors to fields and species

The field analogy is presently only an analogy of **regional jointness**.  A
compatible regional instrument is not yet the equivalent of a field.  At
minimum a QFT reconstruction needs:

1. a local observable algebra (or carrier Hilbert space) for each relational
   region and consistent inclusion/overlap maps;
2. a causal relation and microcausality/commutation rule for separated local
   algebras;
3. a vacuum or reference phase, a spectrum/positivity condition, and a
   continuum/coarse-graining limit;
4. an excitation-number construction or scattering sectors, not merely a
   finite transfer spectrum;
5. symmetric, antisymmetric, or more general exchange structure—equivalently
   a permutation/braid action or CCR/CAR-like algebra—and the constraints
   tying it to locality; and
6. cluster decomposition and an all-region gluing law, including changing
   carriers.

The local-algebra and sector route is not decorative: Haag and Kastler make
the regional observable algebra central to QFT
([Haag–Kastler](https://doi.org/10.1063/1.1704187)), and the DHR analysis shows
how particle statistics and charges require superselection/localization
structure well beyond normal modes
([Doplicher–Haag–Roberts](https://doi.org/10.1007/BF01877742)).

The identity-versus-shift calculation is correct.  The identity on the
four-cycle has one eigenvalue with multiplicity four; the cyclic shift has
four one-dimensional phase eigenspaces.  This proves only that the spectral
partition depends on an unspecified transfer law.  It does not turn either
partition into particles, and it does not show species are impossible to
derive once a law, vacuum, symmetry, stability criterion, and scattering map
are supplied.  `SPECIES-UNSELECTED` is nevertheless licensed for this unit
because all of those selectors are absent.

Pair-record ontology neither entails nor forbids bosons or fermions.  The
question is completely open until histories with exchanged indistinguishable
excitations carry a consistent symmetric-group/braid representation and the
observable algebra supplies the corresponding superselection sectors.

**Finding Q-5 — MAJOR.** “This is the relational analogue of what a field
accomplishes in QFT” invites an identification the construction does not
support, and the QFT-limit row should be `OPEN`, not `CONDITIONAL`: the listed
ingredients are necessary debts, not a sufficient condition under which a QFT
limit has been proven.  Minimal repair: call the instrument a candidate
regional-process container, add the six missing structures above, and retain
normal modes only as species candidates.

## Q5. Consequences, deviations, and the next discriminating test

### Reclassified quantum consequences

| claim | hostile classification | reason |
|---|---|---|
| one-region preparation blindness | **FORCED** | Blockwise linearity gives it for every decomposition of one `rho`, not only Z/X. |
| fixed-factor Bell no-signalling | **FORCED** | Exact for the registered Bell state and, analytically, for arbitrary local CPTP maps on a fixed tensor factor. |
| growing-geometry no-signalling | **OPEN** | Bob's algebra/factorization and pre-contact composition are not defined across output geometries. |
| repair of the v15 walk | **OPEN** | The safe qubit instrument is a replacement fixture, not a reconstruction. |
| persistence of quantum coherence through the core occurrence | **REFUSED** | The displayed Z instrument is entanglement breaking. |
| a QFT limit | **OPEN** | No local net, vacuum, statistics, continuum map, or scattering reconstruction exists. |
| particle species | **OPEN** | Only law-relative finite eigenspaces were computed; no species is selected. |
| metric noise or modified dispersion | **OPEN** | Neither a metric observable nor a particle dispersion observable is typed. |
| forced QFT/GR deviation | **OPEN** | No comparison observable or surviving-law-family enumeration exists, so the question is untyped. |

The entanglement-breaking statement follows both directly from the displayed
output and from the measure-and-prepare characterization of such channels
([Horodecki, Shor, and Ruskai](https://arxiv.org/abs/quant-ph/0302031)).  It is
an exact indirect consequence the paper missed.  It is not a universal
no-go against outcome-resolved backreaction: less destructive instruments are
possible.  It is a no-go against using **this** core projective occurrence
where coherent propagation or entanglement must cross the division boundary.

**Finding Q-6 — MAJOR.** The machine claim
`NO-FORCED-QFT-GR-DEVIATION-IN-REGISTERED-FAMILY` is not established.  In the
source, the relevant predicate is just that the Z and X rivals have different
microscopic record statistics.  Formally, from `f(L1) != f(L2)` one cannot
infer that no other observable `d` has `d(L1)=d(L2)` and differs from QFT/GR.
Worse, `d` is not defined and the surviving family is not enumerated.  Minimal
repair: remove the machine claim and secondary verdict, classify the question
`OPEN/UNTYPED`, or preregister dimensionless comparison observables and prove
their non-invariance over a genuinely exhaustive surviving family.

**Finding Q-7 — MAJOR, protocol.** Section 9 of the pin requires exactly one
of `FORCED`, `CONDITIONAL`, `PERMITTED`, `REFUSED`, or `OPEN` for every
consequence row.  The paper instead emits compounds such as
`FORCED-BY-ADMISSIBILITY-GATE`, `OPEN-AND-UNSELECTED`, and
`REFUSED-IN-REGISTERED-FAMILY`.  This is not merely style because the compounds
hide the distinction between an assumed admission rule and a derived result.
Minimal repair: rewrite every row using the frozen five-word vocabulary and
put scope/selection qualifications in the reason column.

### The next quantum test

The most discriminating successor is not an all-`n` census.  It is a
**changing-factorization overlap/comb test** on the smallest four-actor causal
diamond:

1. begin with an entangled preparation across two relationally separated
   subalgebras;
2. define two inequivalent cuts/refinements of one overlapping region;
3. let at least one complete outcome create/delete a relation so that the
   output factorization genuinely changes;
4. construct the complete boundary instrument independently on both cuts and
   require equality of their boundary Choi/process operators;
5. identify Bob's local algebra in every output sector and test an
   informationally complete set of Alice instruments, summing over her
   outcomes, at every pre-contact continuation; and
6. include a registered interference or Bell witness that must survive, so an
   entanglement-breaking projective placeholder cannot pass by being safely
   classical.

This one fixture attacks refinement independence, overlap gluing,
compositional no-signalling, changing subsystem identity, and preservation of
the quantum content simultaneously.  If it passes, the next step is to embed
the old 27-cell walk's two-window SCOUT-PSI witness in the same regional
instrument.  If it fails, expanding to arbitrary actor number would only
multiply an already unresolved type error.

## Required repair ledger

| id | object | consequence | severity | minimal repair / kill |
|---|---|---|---|---|
| Q-1 | “right correction” and `EPR-SAFE-INSTRUMENT` | Conflates one safe replacement with a reconstruction and a growing-geometry theorem. | MAJOR | Scope to the registered fixed-factor region; keep the v15 composite-dynamics obligation open. |
| Q-2 | ontic nonlinear-rule consequence row | Refuses a whole ontology branch using one ensemble functional. | MAJOR | Rename to the exact registered control; do not generalize beyond stated operational assumptions. |
| Q-3 | actual outcome bridge | Kraus blocks do not themselves actualize one history. | MODERATE | Declare objective stochastic actualization and its trace-weight bridge explicitly. |
| Q-4 | Hamiltonian interpretation | Logarithm ambiguity is narrated as ontological demotion. | MODERATE | State the infinite lift family, physical units, and reduced/CQ purity scope. |
| Q-5 | field/QFT analogy | A regional operation is mistaken for field structure; QFT conditionality is unsupported. | MAJOR | Demote to process-container analogy; set QFT limit OPEN and list the missing algebraic/Fock/statistics structure. |
| Q-6 | no-forced-deviation gate and secondary | Logical predicate does not test the claimed invariant-family statement. | MAJOR | Remove/refuse the verdict or build typed observables and exhaust the family. |
| Q-7 | consequence vocabulary | Violates the pin's exact five-tag classification. | MAJOR | Normalize all consequence tags and leave qualifiers in reasons. |
| Q-8 | omitted entanglement-breaking consequence | The core law destroys the quantum resource it is supposed eventually to reproduce. | MAJOR | Publish the exact consequence and require a non-entanglement-breaking overlap/reconstruction test. |

## Grade and highest licensed verdicts

**Grade: `ACCEPT-WITH-FIXES` (major repairs required before terminal use).**

Highest licensed primary verdict:

`JRH-CONSISTENT-BUT-UNDERDETERMINED`

The quantum seat licenses that primary because the safe Z instrument exists
and the safe X rival already shows that the architecture does not select a
prediction-equivalent law.  Nothing here licenses calling the architecture
the dynamics.

Highest licensed secondary verdicts, with binding scope:

- `L2-VIABLE` — only as a typed two-actor projective-instrument fixture;
- `TRIANGLE-FIRST-LOOP-NOT-FIRST-EVENT` — no quantum objection to the limited
  graph statement;
- `EPR-SAFE-INSTRUMENT` — only for the registered fixed-factor, one-region Bell
  test and the analytic fixed-circuit extension;
- `HAMILTONIAN-RECOVERABLE-ONLY-RELATIVE-TO-FROZEN-SECTOR-AND-CLOCK` — read as
  a nonunique phase/logarithm reconstruction, not an anti-Hamiltonian theorem;
- `SPECIES-UNSELECTED`;
- `AFFINE-CHANNEL-TERM-UNSELECTED`.

`NO-FORCED-QFT-GR-DEVIATION-IN-REGISTERED-FAMILY` is **not licensed**.  The
highest honest quantum consequence is `QFT/GR-DEVIATION-OPEN-AND-UNTYPED`;
there is no named forced deviation either.

# D11 investigation — complete Bloch–Lorentz SCIR, and why it dies

**Status:** round-1 hostile-review corrected, 2026-07-11. The frozen protocol
is `note-d11-complete-bloch-lorentz-scir-protocol.md`.

> **Correction:** the finite sequential kernel is complete once a global
> enabled-token race is supplied, but the requested decentralized local click
> law is not. Gauge covariance was proved as a separate algebraic template,
> not on a generated multi-frame history; canonical projective pushforward is
> also open. Under the frozen gates the primary verdict is therefore
> `INCOMPLETE-PACKET`, not the pre-review
> `COMPLETE-KINEMATICS/INFLUENCE-ENVELOPE-OPEN`.

## 1. Result in one sentence

The D10 Bloch–Lorentz algebra can be embedded in a fully specified globally
raced sequential packet with incidence-scoped instruments, but the frozen
equal-activity population becomes extinct almost surely. The packet has an
exact algebraic positive-cone shadow and real sibling interaction; it is not
yet a decentralized, relational spacetime law and does not generate a large
universe.

This cleanly separates three questions that earlier papers sometimes allowed
to blur:

1. Is the globally normalized next-history probability fully specified?
   **Yes.**
2. Do generated ancestry and intervention remain inside the Lorentz cone?
   **Yes.**
3. Does the typical history grow enough to occupy that cone? **No.**

## 2. The complete packet actually tested

The event algebra is `Herm_2(C)`. In the root gauge, a state `rho` contributes
the positive increment `Delta Y=2 rho`. Writing

`X=t I+x sigma_x+y sigma_y+z sigma_z`

identifies positive matrices with the future Lorentz cone. Rank-one states
give null increments `(1,r)` with `|r|=1`.

Local frame changes use the full dual rule

`X -> A X A^dagger`, `E,e -> A^{-dagger}(E,e)A^{-1}`,

so `Tr(EX)/Tr(eX)` is invariant even for nonunitary `A in SL(2,C)`. Instrument
legs transform at both endpoints. The exact receipt checks this for a boost,
noncommuting vertex frames, link paths, and diamond holonomy. A control that
transforms the state but not the effect changes the probability, proving that
a physical filter is not being mislabeled as gauge.

The transition grammar is support-local, but the next-event presentation
still enumerates and normalizes over every enabled token in the history:

- `SPLIT`: one carrier becomes a transformed carrier plus a fresh `P0`
  ancilla; an owned sibling-join token is emitted;
- `JOIN`: two still-open siblings interact by partial-iSWAP at `pi/4`, one
  output is measured/discarded, and the other continues at their locally
  recorded common future;
- `SEAL`: one carrier receives a projective durable outcome and terminates;
- all enabled tokens have activity one; the token race and local Born weights
  give every next-history probability.

After review repair, tokens store owners, anchors, activities, and the actual
instrument matrices. Ports carry local order-unit and frame-link fields,
state, position, explicit parent ports, and status; immutable records carry
provenance instead of a growing ancestry word. Consuming a port invalidates
every overlapping token. One tested pair of disjoint SPLIT schedules has the
same state and exact presentation probability; a general canonical
construction-order pushforward is open.

## 3. What the exact calculation closes

`code/d11_complete_bloch_lorentz_exact.py` passes 73 fixed checks in
`Q(sqrt(2),i)` except for the explicitly labeled external finite-sphere
diagnostic.

It closes:

- dual `SL(2,C)` Born gauge, endpoint instrument covariance, link-path and
  diamond covariance;
- completely positive and complete SPLIT/JOIN/SEAL instruments;
- a JOIN output that depends on each input and transmits an intervention into
  a later seal probability;
- root uniqueness, exact token ownership, actual token matrices, typed durable
  outcomes, multi-parent sibling-merge provenance, invalidation, and
  normalized finite prefix laws through exhaustive cutoff three;
- one exact disjoint-SPLIT state/probability commutation cell plus a
  physical-order control for overlap;
- the local common-future identity `Y_c=Y_a+Y_b-Y_o`, ancestry contained in
  positivity, and a deliberately naive join that violates the other leg's
  future;
- an explicit positivity-related but branch-disjoint record with zero
  intervention influence;
- the independent D10 `H/T` orbit counts
  `1,3,8,19,35,64,113` through even depths 0--12 and depth-12 sampled support
  `0.914143429015`.

Therefore the globally raced sequential kernel is complete. The stronger
rulebook target is not: decentralized event selection, integrated multi-frame
generation, canonical truncation pushforward, general bridge birth, and
finite record capacity remain open. The packet is also conditional on the
primitive complex qubit, root, matrices, scale `2`, and unit activities.

## 4. The extinction theorem

Let `P_n=p>0` be the number of open ports after the `n`th committed rewrite,
and let `J_n=j` be the number of enabled sibling joins. Port ownership gives
`0 <= j <= p/2`. There are

- `p` SPLIT tokens, each changing `p -> p+1`;
- `p` SEAL tokens, each changing `p -> p-1`;
- `j` JOIN tokens, each changing `p -> p-1`.

Because every activity is one,

`Pr(up | H_n)=p/(2p+j)`,

`Pr(down | H_n)=(p+j)/(2p+j)`,

and hence

`E[Delta P_n | H_n]=-j/(2p+j) <= 0`.

Thus `P_n` is a nonnegative supermartingale absorbed at zero. Stop it on first
hitting `{0,M}`. Optional stopping gives

`Pr(hit M before 0) <= 1/M`

from the single root. It cannot survive forever inside a bounded positive
population: while `1 <= p <= M`, the total SEAL probability is
`p/(2p+j) >= 2/5`, so there is a uniform positive chance of a run of seals
that reaches zero. Letting `M -> infinity` leaves no positive-probability
escape. Therefore

> **The frozen equal-activity SCIR becomes extinct almost surely.**

The root has exactly `1/2` probability of immediate extinction. The theorem
is stronger than the numerical campaign and explains it without a seed
story.

## 5. Frozen numerical campaign

The required 72 histories used cutoffs `512,1024,2048`, 24 fresh seeds at each
rung, with no survivor conditioning. All 72 became terminal before their
target. Median committed clicks were `1,3,1`; the longest histories at the
three rungs lasted `49,171,47` clicks. No rung had a survivor.

Across the rungs:

| cutoff | longest | histories with JOIN-transmitted influence | rank-four position clouds | median direction support |
|---:|---:|---:|---:|---:|
| 512 | 49 | 1/24 | 3/24 | -1.0000 |
| 1024 | 171 | 4/24 | 5/24 | -0.8516 |
| 2048 | 47 | 5/24 | 4/24 | -1.0000 |

There were exactly zero ancestry-cone and influence-cone violations. Local
JOIN influence is real, but too few histories reach enough joins to meet the
20/24 population-level gate. Direction and covariance gates fail because the
histories terminate, not because a long generated cloud was shown to have the
wrong dimension or shape.

The inherited shape instrument correctly refuses almost all generated
histories for insufficient projections. The physical-time-axis M4 controls
remain valid with means `1.0855,1.0793,1.0785`; the diagonal-axis convention
is invalid on all these M4 controls and is recorded as a convention
systematic. No generated `F` claim is made.

The frozen numerical registry label is `INTERACTION-INERT`, because gate 2 is
checked before the direction/rank gates. The repaired statistic counts a
changed downstream seal distribution, not merely changed state or position;
its prevalence is `1/24,4/24,5/24`. The physical diagnosis is
**interaction-capable but population-extinct / interaction-sparse**.

## 6. What was invented and what was not

Nothing here establishes a broad literature-priority claim.

- The Hermitian-spinor realization of Lorentz vectors and the `SL(2,C)`
  action are standard.
- Kraus instruments, quantum combs, and locally connected memory channels are
  standard quantum-network machinery.
- Intervention-defined quantum causation and process-tensor descriptions of
  multi-time non-Markovian experiments are established frameworks.
- Critical/subcritical branching extinction is standard probability theory.
- Barandes supplies an exact stochastic--quantum correspondence and an
  indivisible, generally non-Markovian full-history dynamics; it does not
  select this variable-record grammar, its token activities, or its
  cosmological birth law.

The SHARD-specific contribution is the synthesis and the refusal: a typed,
globally raced sequential kernel can satisfy a separate Lorentz-covariance
template while still failing cosmogenesis by a simple population theorem. The local
`Y_a+Y_b-Y_o` join placement and the four-way separation of ancestry,
positivity, coordinates, and intervention are internal constructions, not
claimed as unprecedented mathematics.

## 7. The most constrained next correction

Changing the numerical SPLIT rate upward would evade extinction, but that is
only another free constant. The result motivates—not derives—a more
structural candidate: distinguish **forming a durable record** from
**destroying a continuation carrier**.

The record ontology instead suggests a continuing click:

> `COMMIT`: consume one open carrier, seal a finite outcome, and emit one
> successor carrier carrying the post-instrument state.

This uses the same projective Kraus maps already present; the D11 code threw
their outputs away. Retaining the output changes the population increments to

- SPLIT: `+1`;
- COMMIT: `0`;
- JOIN: `-1`, enabled only when `p>=2`.

The empty boundary then becomes unreachable from one root without changing a
rate. With unit activities the conditional drift is

`(p-j)/(2p+j) > 0`, because `j <= p/2`.

This is not accepted as the final law or forced by the record axioms. It is a
candidate because it is motivated by one possible meaning of a record click
and removes the failure by a declared type change rather than a favorable
dial. Terminal observations, separate birth tokens, and other continuation
ontologies remain live alternatives. It must still be
tested for runaway branching, non-Markovian full-history consistency,
JOIN-transmitted influence, cone occupation, roundness, dimension, and the
distinction between observation-terminal records and universe-continuing
records.

## 8. Verdict

The D11 primary verdict under its frozen gates is

`INCOMPLETE-PACKET`.

The globally raced conditional kernel and algebraic containment are complete,
but the decentralized local click law, integrated relational gauge history,
canonical construction pushforward, general joining, and macroscopic
influence envelope are not. The extinction theorem nevertheless narrows one
major issue to a concrete question:

> Does a seal terminate a carrier, or is sealing precisely the event that
> creates its successor record?

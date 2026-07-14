# Paper 21 round 1 — locality/physics terminal hostile review

**Target:** commit `afbd2ba`,
`relativistic-isp-v10-paper21-local-generators-do-not-imply-local-memory.md`.

**Verdict:** **ACCEPT SCIENTIFIC CORE; MINOR TEXTUAL REVISION BEFORE TERMINAL
STAMP — 0 BLOCKER / 0 MAJOR / 4 MINOR / 2 NIT.**

No theorem, exact probability, receipt hash or open-problem disposition is
false. The remaining issues concern the physical meanings of “local,”
“distributed,” “causal,” and “selected,” plus one explicit boundary between
D34d predictive equivalence and the v9 stem spectrum.

## Independent evidence check

Fresh executions reproduce the terminal evidence:

- D34d classical under `PYTHONHASHSEED=112358,314159`:
  `912394a45eb76e3cf3d36ed51310f44f7f51f0e2c0d9162b97d42015feb6b16b`,
  13/13, summary hash
  `9f9e59954bd1710e70c27d1fa6c5b285c50eec096dae21d433c04201092ac282`;
- D34d quantum under both salts:
  `e1990fe3a4dfbc44c83b4b49216df44ad9462dcb410c9c24c19dc4144c3884d1`,
  10/10, summary hash
  `cc496ff94d360c34ffb5f52b2e4ba57f342378d3807198a3a0f5d9ff01c4dce0`;
- terminal D34b exact parent:
  `47993cbcaf3d3a719ef868fd6a4d122b9b2d46e23555133d886185f79358740c`,
  7/7;
- terminal D34b actor parent:
  `59d28bc5db03cca5e30a81eaed09c1c42d7e51541f6ea7c3d078c9d59a75c2a3`,
  8/8.

Paper 21's receipt table reports the internal summary hashes correctly. Its
continuous-time statements are tied to analytic identities; Decimal outputs
are regressions. Its locality theorem consumes the repaired sealed-root,
degree, passive-reception and source-clock gates rather than the superseded
toy analogies.

## Accepted architecture

### Global, distributed and local are not collapsed

The five-level separation in §2 is scientifically correct:

```text
complete past
!= complete current global configuration Z_t
!= predictive-equivalence class
!= candidate regional collar/boundary state
!= durable observer record.
```

In particular, the paper says that `Z_t` is distributed over actor/event
records **and still global**. It does not promote full-configuration Markovity
into a finite state inside one record. Proposition 2 then supplies the actual
D34b obstruction `1/4 -> 1/8`, and the conclusion keeps a bounded all-future
collar open.

### Seals and stopping scopes are correct

The reconstructed grammar uses eligible **unsealed** neighbors, and paper 21
states that sealed actors neither initiate nor receive its events. This agrees
with the literal `R--A--B` receipt: R has no initiator/target row and A-to-B
retains rate `1/4`.

A-own-ring count, A-wire-event count and global event count are separated. The
strong-Markov theorem is stated for stopping times of the complete
construction-time filtration, not for emergent proper time. Fixed `T`, fixed
embedded depth, compensated horizon, nonlinear timestamp relabeling and
relative-rate variation have their correct distinct scopes.

### Record capacity is honestly bounded only where proved

Paper 21 carries the exact D34c bounds—event outcome rank six and incidence
in/out arity at most two—and separately lists every unbounded or unproved
quantity: Ulam identifier length, actor degree, total configuration size,
boundary width, renewal-age-vector dimension and posterior complexity. It
does not infer bounded predictive memory from finite click content.

### The open ledger is complete

The paper retains the important opens: derived rates/operations, dynamic
adjacency and component joining, the timed operator-valued D34b–D34c law,
intrinsic profinite quantum extension, cone/4D implications, proper time and a
bounded predictive collar. No v9 cone or dimension claim is silently imported.

## MINOR findings

### m1 — “support-local generator” needs its read/write support stated in the
headline vocabulary

Each D34b jump writes only the initiator plus one child/target, but its
interaction coefficient `1/(4|E_y|)` reads the initiator's **entire incident
eligible star**. That star is graph-radius one but has no uniform cardinality
bound. Sections 3.2 and 8 together contain both facts, so the theorem is not
false; however the abstract/verdict phrase “support-local actor terms” can be
misread as uniformly bounded read support.

**Exact repair:** add one sentence after §3.2 and echo it in §12:

> “Local” here means bounded touched/write support and graph-star-local rate
> data; the incident star may have unbounded degree, so no uniformly bounded
> read or memory width is proved.

Also state that “distributed” names the factorization of state/source across
actor and event records. It does not assert OS threads, literal hardware
processes, or eliminate the reference simulator's central atomic evaluator for
shared events.

### m2 — “compatible with causal locality” must be scoped to record-graph
locality

Section 8 says the construction is compatible with causal locality. What is
actually established is actor-star dependence, bounded touched support,
disconnected-component factorization and causal wire predecessors. No Lorentz
microcausality, finite propagation speed in emergent spacetime, foliation
independence or proper-time theorem has been proved.

The later open ledger prevents a formal contradiction, but this sentence is
the paper's most likely physical overreading.

**Exact repair:** replace it with:

> This is compatible with the **record-graph locality proved here**. It is not
> yet a theorem of relativistic locality or an identification of graph
> adjacency with a spacetime light cone.

### m3 — the Barandes/SHARD interpretation needs one explicit scope paragraph

The result supplies a useful reconciliation for the **chosen D34b exemplar**:
its complete global classical configuration is Markov, while reduced record
descriptions can retain memory. It does not prove that every Barandes
indivisible stochastic process has a finite, local, or even practically
compressible Markov realization. Full-history Markovization remains a
tautological global construction, and D34d's quantum causal-break example is a
finite system–boundary process, not the still-open timed quantum SHARD law.

Paper 21 implies these limits in §§1, 7 and 9, but because its title is
*Relativistic ISP* the interpretation should be explicit.

**Exact repair:** add a paragraph to §9:

> This does not replace Barandes' complete history law by a fundamental local
> Markov chain. It exhibits one chosen SHARD law with a global Markov
> representation and explains how non-Markov observable records arise by
> projection. Whether nature's complete ISP law itself admits any smaller
> record-carried predictive state remains open.

In the same paragraph, clarify that the “modeled carrier fields” listed in
`Z_t` are optional finite exemplar fields. They are not a claimed timed D34c
carrier evolution; that operator-valued lift remains open.

### m4 — predictive quotient, causal collar and v9 stem spectrum require an
explicit non-identification

The paper's current five-level architecture is correct. The canonical
predictive state is the **law-, query- and instrument-relative equivalence
class of complete marked pasts** under equality of conditional futures. A
whole past/stem is one representative before quotienting. A causal
collar/boundary is a possible physical realization of the quotient only after
a screening/sufficiency theorem. One record is a still narrower projection.

Nothing in D34d earns an identification with v9's profinite stem spectrum.
That spectrum is the dynamics-independent Stone space of the Boolean algebra
generated by unmarked causal-set stem questions; its fibers identify histories
with the same stems. D34d instead uses marked typed actor histories and
identifies pasts with the same **conditional future law** for a chosen
dynamics/query class. Moreover D34b still lacks an intrinsic untimed
inter-`T` restriction/profinite system, and the D34c quantum extension remains
open.

Paper 21 makes no false profinite claim—it lists the extension as open—but the
external opening is important enough to close explicitly.

**Exact repair:** add to §2.4 or §9:

> Predictive equivalence is not stem equivalence. A future investigation may
> ask whether a law-relative predictive quotient factors through marked stem
> data or through an active collar, but neither factorization nor a map to the
> v9 stem spectrum is established here.

## NIT

1. The abstract's phrase **“the selected D34b universe”** can be read as
   selection by physical principle. D34b's coefficients, adjacency and
   operations remain chosen exemplars. Use **“the chosen static-adjacency D34b
   exemplar”**. Likewise qualify §12's final “SHARD has a local generative
   architecture” as a result about that exemplar, not nature's final rule.
2. “Complete construction-time filtration” should be glossed once as the
   **completed natural filtration of revealed actor events/source coordinates
   through `t`**. It must not mean that unrevealed future clock/mark tapes are
   already included; that enlarged filtration would invalidate the independent-
   increments step in the strong-Markov proof.

## Exact terminal disposition

The following paper-level noun is supported and survives unchanged in
substance:

> **D34d GLOBAL-MARKOV / ACTOR-STAR-LOCAL-GENERATOR /
> OBSERVABLE-MEMORY CHARACTERIZATION FOR THE CHOSEN D34b EXEMPLAR.**

It means:

- the complete global Harris configuration is strong Markov;
- its jumps have bounded touched support and rates read graph-local incident
  data, without a universe-wide opportunity denominator;
- a record projection may be Markov or non-Markov according to the declared
  law/instrument sufficiency test;
- no bounded per-record or fixed-collar predictive state follows;
- no relativistic locality, proper-time, profinite-predictive or final-law
  theorem follows.

Apply the four clarification paragraphs and two wording nits, then this
locality/physics stream can return unqualified terminal `CLEAN`. No executable,
receipt, theorem proof or numerical result needs alteration.

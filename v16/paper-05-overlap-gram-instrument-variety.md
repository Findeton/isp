# Overlap Gram/instrument varieties, coherent ports, and arity

Status: **GREEN-UNREVIEWED CANDIDATE**. This paper is generated from the
sealed OVG result object. It is not terminal until the separately authorized
hostile process is complete.

## Result

The machine-selected primary result is `OVG-GRAM-INSTRUMENT-VARIETY-CONSTRUCTED`. Its registered finding
segments are `['OVG-GRAM-INSTRUMENT-VARIETY-CONSTRUCTED', 'SINGLE-PORT-PHASE-CONSTRAINED', 'MULTIPORT-COHERENCE-EXISTS-BUT-PORT-LAW-UNSELECTED', 'LOCAL-FLAG-KINEMATICALLY-PERMITTED-BUT-IMPLEMENTATION-UNSELECTED', 'COMPOSITE-SUPPORT-DOES-NOT-FORCE-PRIMITIVE-ARITY', 'CAUSAL-NONSEPARABILITY-UNTESTED', 'OVERLAP-LAW-UNSELECTED']`.

The proposed “non-scalar order holonomy means record or fuse” rule is false.
The exact overlapping CNOT construction has a non-scalar relative operator,
yet the single class map with weights `['3/5', '4/5i']` is
all-input complete. The same magnitudes with real relative phase fail. The
difference is not a loophole: the complex phase is precisely the variable the
original one-point test omitted.

What survives is a sharper and smaller result. For two unitary histories, the
number of distinct eigenphases of their relative operator decides whether a
nontrivial coherent single-port completion can exist. Multiple complete ports
are less restrictive: the parity construction exists for every common-
boundary isometry pair. Neither fact chooses nature's port law or turns a
binary circuit into a primitive ternary event.

## In ordinary language

Suppose two local changes overlap: first `AB` then `BC`, or in the opposite
order. The two complete routes can lead to the same later kind of state. Their
effects must then be added with complex strengths. Testing only one choice of
strengths is like testing one chord on a musical instrument and concluding
that the instrument cannot play in tune. Here the real-valued chord is out of
tune, but rotating one contribution by a quarter phase makes the total exactly
probability-preserving for every input.

There is therefore no forced choice between writing down which order happened
and declaring one indivisible three-actor event. A later record may distinguish
orders; one complete port may retain them coherently; several ports may sort
different coherent combinations. Which of those mechanisms nature uses is a
law question that this architecture does not yet answer.

## 1. The exact object

For fine histories `h` with a common typed input and output, define

```text
G_hk = V_h^dagger V_k,
K_j  = sum_h c[j,h] V_h.
```

The complete recorded ports obey

```text
sum_j K_j^dagger K_j = I.
```

This is an operator identity, not normalization on one prepared state. It is
the exact implicit polynomial variety in the port coefficients. Its cross
terms are the law's own Gram operators; no extra comparison map is inserted.

For two isometries `A,B`, let `Omega=A^dagger B`,
`S=sum_j(|a_j|^2+|b_j|^2)`, and
`C=sum_j conjugate(a_j)b_j`. The entire condition reduces to

```text
S I + C Omega + conjugate(C) Omega^dagger = I.
```

## 2. The unitary single-port theorem

For one port, write `z=conjugate(a)b` and
`c=1-|a|^2-|b|^2`. If `Omega` is unitary with eigenphases `phi_k`, completeness
is equivalent to

```text
2 Re(z exp(i phi_k)) = c
```

for every distinct eigenphase. In the three real variables
`(Re z, Im z, c)`, the exact solution-space dimension is two for one phase,
one for exactly two phases, and zero for three or more phases.

The proof is geometric but elementary. A nonzero triple defines a straight
line in the plane of `(cos phi,sin phi)`. A line meets the unit circle in at
most two distinct points. Three phase points therefore force the zero triple.
Two distinct rows are independent and leave one direction; one row leaves two.
Any nonzero direction has `z != 0`. Scaling it sufficiently close to zero
makes the quadratic with roots `|a|^2,|b|^2` have two positive roots, proving
that actual complex coefficients exist, not only formal `(z,c)` values.

With exactly two phases, subtracting the two equations gives

```text
arg(conjugate(a)b) = -(phi_1+phi_2)/2 mod pi.
```

This selects a relative phase condition, not the magnitudes. Definite-order
endpoints with `z=0` are excluded from the word “coherent.” Scalar `Omega`
also means the two history maps are projectively proportional; their separate
names need an independent event record or calibration to become physical.

## 3. The refuted no-go and the corrected strata

The CNOT overlap gives `Omega=CNOT(A->C)` exactly, with eigenvalues `+1,-1`.
The real pair `['3/5', '4/5']` has residual
`[['24/25', '0', '0', '0', '0', '0', '0', '0'], ['0', '24/25', '0', '0', '0', '0', '0', '0'], ['0', '0', '24/25', '0', '0', '0', '0', '0'], ['0', '0', '0', '24/25', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '24/25', '0', '0'], ['0', '0', '0', '0', '24/25', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '24/25'], ['0', '0', '0', '0', '0', '0', '24/25', '0']]`. Rotating the second weight gives
`['3/5', '4/5i']` and residual
`[['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0']]`. Thus a non-scalar relative order operator
does not force a record or fusion.

At three distinct phases the registered single-port rational census is empty,
as the theorem requires. But for every isometry pair

```text
K_plus=(A+B)/2,   K_minus=(A-B)/2
```

is complete because the cross terms cancel. The multipport construction
therefore survives even where one coherent single port cannot.

## 4. Growing carriers and more than two histories

The `C^2 -> C^4` control has nonnormal overlap `[['0', '3/5'], ['0', '0']]`. Its direct
real-linear operator constraint has rank `3` and
nullity `0`. Counting eigenphases here would be
invalid; the full operator equation is the classifier. Its parity ports remain
complete.

For the three-history Pauli fixture, the embedded family

```text
K_plus  = p(I+X)/2,
K_minus = p(I-X)/2,
K_Z     = q Z,
p^2+q^2=1
```

is all-input complete. The exact registered rows produce
`2` distinct calibrated probability screens.
This is a constructive positive-dimensional subvariety and a direct law-
nonselection witness.

Two further port decompositions have the same unconditioned channel while
their calibrated first-port maps differ. That is the precise boundary between
Kraus/unravelling freedom and physical record-individuated instruments.

## 5. Rewrite typing and primitive arity

The four rewrite controls are classified as `['disjoint-commuting', 'joinable-overlap', 'dependency', 'divergent-endpoints']`. A delete/use
case is a dependency: one order is not a lawful history. Divergent final
carriers have no coherent sum at that cut unless a common future is supplied.
Neither fact is a durable record; permanence still requires a future census.

Both three-actor CNOT order maps factor into the declared binary generators.
Calling either product a single ternary arrow changes notation, not ontology.
The Toffoli control is nonfactorizable in the CNOT-only grammar because every
CNOT circuit is linear over `F_2` and Toffoli is not. This proves the assay can
recognize fixture-relative irreducibility; it does not establish that ISP's
actual law contains Toffoli or any minimum-arity generator.

No result here extends the binary grammar coherently to arbitrary `n`.

## 6. Records, locality, and causal order

Stacking complete port maps produces an isometric flag dilation. The flag can
be assigned to an enlarged local catalogue at actor `B`, but the frozen event
grammar contains no map of the required type. Kinematic localization is not a
selected local implementation, and no future census establishes that the flag
is durable.

With an entangled idle spectator `D`, the complete overlap instrument leaves
the spectator marginal exactly unchanged; the completeness-violating
amplifier moves it. This is the fixed-factor, unconditioned no-signalling
statement. Conditional steering and a changing definition of the remote
subsystem remain open.

A coherent sum of two fixed circuit orders does not demonstrate a quantum
switch or causal nonseparability. Those notions require a typed higher-order
process and a process-level witness against the causally separable set. Neither
is constructed here. The distinction follows the process-matrix literature,
including Oreshkov, Costa and Brukner (2012), Chiribella et al. (2013), and
Araújo et al. (2015).

## 7. Generated exact claims

- **C1** — The exact overlapping CNOT histories have non-scalar relative operator CNOT(A->C), while weights ['3/5', '4/5i'] give zero all-input completeness residual.

- **C2** — The corresponding real weights ['3/5', '4/5'] fail, so one failed real point cannot support a no-go over complex weights.

- **C3** — Across the five unitary strata, the exact phase-row nullities are [2, 2, 1, 1, 0], matching the one/two/three-or-more eigenphase classifier.

- **C4** — For exactly two distinct eigenphases the relative phase of conjugate(a)b is fixed modulo pi, while coefficient magnitudes remain unselected.

- **C5** — For every registered common-boundary isometry pair, the two parity ports are all-input complete.

- **C6** — The dimension-changing C^2->C^4 pair has nonnormal overlap [['0', '3/5'], ['0', '0']] and direct operator-constraint nullity 0; the unitary spectral shortcut is inapplicable.

- **C7** — The exact three-history family contains 3 registered rational rows and 2 calibrated probability screens, so completeness does not select a port law.

- **C8** — Two port decompositions have the same unconditioned channel but different calibrated first-port maps; record labels, not Kraus syntax alone, distinguish the instruments.

- **C9** — A history difference that is zero at the present cut becomes nonzero after the registered branch-dependent future, so present darkness is not permanence.

- **C10** — Both three-actor order composites have lower-arity factorizations (5 and 5 words), so their joint support does not make them primitive ternary events.

- **C11** — The canonical parity flag is an isometry into a locally enlarged catalogue, but no map of that type exists in the frozen elementary grammar; implementation and durability remain unselected.

- **C12** — The machine-selected registered findings are ['OVG-GRAM-INSTRUMENT-VARIETY-CONSTRUCTED', 'SINGLE-PORT-PHASE-CONSTRAINED', 'MULTIPORT-COHERENCE-EXISTS-BUT-PORT-LAW-UNSELECTED', 'LOCAL-FLAG-KINEMATICALLY-PERMITTED-BUT-IMPLEMENTATION-UNSELECTED', 'COMPOSITE-SUPPORT-DOES-NOT-FORCE-PRIMITIVE-ARITY', 'CAUSAL-NONSEPARABILITY-UNTESTED', 'OVERLAP-LAW-UNSELECTED'].

## 8. Consequence classification

| question | status |
|---|---|
| overlap_instrument | constructed-at-finite-fixtures |
| single_port_phase | constrained-at-two-unitary-eigenphases |
| port_law | unselected |
| elementary_transport_law | unselected |
| minimum_arity | not-forced-by-overlap |
| all_n_composition | not-established |
| order_record_permanence | not-established |
| causal_nonseparability | untested |
| fixed_spectator_no_signalling | verified-at-fixture |
| changing_subsystem_steering | open |
| hamiltonian | not-reconstructed |
| particle_species | not-derived |
| gravity_backreaction | not-established |
| qft_gr_deviation | not-defined |

## 9. What remains

- finite exact fixtures and one frozen lower-arity grammar only
- the coefficient variety is implicit through exact operator polynomials; no physical law selects a point
- local flag kinematics is not local dynamical implementation or durable recording
- no higher-order process or causal-nonseparability witness is constructed
- no arbitrary-n, continuum, Lorentz, gravity, QFT, particle, Hamiltonian, constant, or phenomenology result

The ontology remains one actual relational history plus a law over complete
alternatives. The Hamiltonian is still only a possible representation of a
selected repeated-sector law; no such selection occurs here. Fields,
particles, statistics, gravity, and continuum spacetime are likewise not
derived. The concrete advance is narrower: overlap is now a correctly typed
operator-variety problem, and the false arity inference has been removed.

## References

- v16 Paper 1, *Joint relational-history law*.
- v16 Paper 3, *Contextual pullbacks and permanent records*.
- v16 Paper 4, *Support–rewrite weld and local couplings*.
- O. Oreshkov, F. Costa, and C. Brukner, “Quantum correlations with no causal
  order,” *Nature Communications* 3, 1092 (2012), arXiv:1105.4464.
- G. Chiribella, G. M. D'Ariano, P. Perinotti, and B. Valiron, “Quantum
  computations without definite causal structure,” *Physical Review A* 88,
  022318 (2013), arXiv:0912.0195.
- M. Araújo et al., “Witnessing causal nonseparability,” *New Journal of
  Physics* 17, 102001 (2015), arXiv:1506.03776.

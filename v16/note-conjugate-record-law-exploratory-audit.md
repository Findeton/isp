# Exploratory audit of the conjugate-record-law proposal

**Recorded:** 2026-08-18, v16 ledger #118.

**Status:** exploratory external-proposal audit, not a Paper 10 pin, candidate,
or corpus physics result. QSF remains under hostile review. This note does not
select a QSF completion and does not alter terminal WRC.

## 1. Material audited

The user supplied the external scratch program

```text
/private/tmp/claude-501/-Users-felixrobles-workspace/
dfe37fa3-9f99-4972-adbb-b335c707618d/scratchpad/
conjugate_record_law.py
```

with SHA-256
`23574302b03afcff6c011c1887895252a7fd6cd99ef4fbbb78f6b0f1d3adb961`.

The source replay is green at every check it actually performs. In its
eight-dimensional fixture (`C^2` matter times a `Z_4` record register), the
controlled write `W`, clock-conditioned transport `T`, and `E = TW` are
unitary. The bare record operators obey `CS = iSC`. For the registered real
seed `(3/5,4/5)`, coherent and measured-every-step record-count distributions
agree for three ticks and differ at tick four by the exact fractions printed
in the source. Switching off the clock phase changes the coherent fourth-tick
count distribution. Those are valid internal facts.

The source's prose makes several larger claims that its gates do not test.
The controls below separate the earned nucleus from those promotions.

## 2. What genuinely exists

The proposal instantiates one lawful finite quantum dynamics:

```text
H = H_matter tensor H_memory,
W = |a><a| tensor S + |b><b| tensor I,
T = sum_n R diag(1,i^n) tensor |n><n|,
E = T W.
```

Matter changes the memory through `W`; memory can feed back into later matter
evolution through `T`; and the complete joint state evolves linearly and
unitarily until a measurement is inserted. Unlike literal WRC CELL-HIT, this
joint map is affine on density operators and has no decomposition ambiguity.
It is therefore a serious **candidate dynamical nucleus**.

The conceptual move is useful: replace a classically sampled counter by a
coherent quantum register, and postpone an actual record boundary. This is a
standard lawful way to retain alternatives coherently, but its use as ISP's
backreacting record field is a substantive new hypothesis.

## 3. The full order holonomy is not central and not two-eigenphase

The source proves only two different statements:

```text
C S = i S C
Omega := (WT)^dagger (TW) != I.
```

It never tests that the full `Omega` is central, block-central, or in OVG's
two-eigenphase stratum. Exact reconstruction gives

```text
charpoly(Omega)
 = (x-1)^2
   (x^2 + (14/25)x + 1)
   (x^2 - (18/25)x + 1)^2.
```

Thus `Omega` has five distinct eigenvalues:

```text
1,
-7/25 +/- (24/25)i,
 9/25 +/- (4 sqrt(34)/25)i.
```

It also fails to commute with both law generators. Exact witness entries are

```text
[Omega,W]_(0,4) = -24/25,
[Omega,T]_(0,1) = -48i/125.
```

Therefore the advertised inference

```text
bare Weyl phase -> full central holonomy -> curvature -> lawful
two-eigenphase overlap
```

is false in the exposed fixture. The bare `Z_4` clock/shift relation survives;
the physical promotion does not.

## 4. Duality does not select the coupling law

Once a cyclic register and its Fourier-dual clock are chosen, the Weyl
relation follows. It does not select:

- `q = 4`;
- the powers `S^a` and `C^b`, whose central phase is `i^(ab)` here;
- the matter controls attached to them;
- the `3-4-5` coin `R`;
- the ordering `TW` rather than another local circuit; or
- how one such register is assigned to each relation in a graph.

So `omega` is forced **conditional on the declared representation**, not a
derived gravitational coupling. Finite clock/shift algebras and intrinsically
quantum link variables already occur in quantum-link and lattice-gauge
constructions. Novelty, if earned, must lie in the relational generation,
backreaction, record doctrine, and continuum consequences—not in `CS=omega
SC` alone.

## 5. The measured shadow is lawful and is not WRC

The source's `sampled_step` measures the register after `W`, collapses matter
to `|a>` or `|b>`, and then applies the conditional unitary. This is a lawful
quantum instrument. Writing its outcome into a classical register is also a
lawful classical-quantum channel.

Literal WRC CELL-HIT instead combines the Born probability with an
input-dependent **noncollapsed** successor ray. QSF's nonaffinity theorem is
about that combination. Consequently:

- classical retention is not, by itself, the source of unlawfulness;
- the source's sampled process is not the WRC process;
- the coherent law is not proved to be a limit or completion of WRC; and
- the coherent-versus-sampled difference is ordinary measurement disturbance
  inside this new toy until a corpus observable is calibrated to it.

Likewise, QSF Arm C's zero total variation through tick three belongs to one
registered record-erased screen. It is not a proof that every record-erased
map or observable is affine through that window.

## 6. Tick four is a fixture outcome, not a law-selected prediction

Keeping the same `q=4`, `R`, `W`, and `T` while varying only the normalized
input seed moves the first coherent-versus-sampled count split:

| seed | first split |
|---|---:|
| `(1,0)` | 5 |
| `(0,1)` | 5 |
| `(3/5,4/5)` | 4 |
| `(4/5,3/5)` | 4 |
| `(5/13,12/13)` | 4 |
| `(3/5,4i/5)` | 3 |

The exact fourth-tick fractions are real results for the exposed calibration,
but neither the time of first divergence nor those fractions are invariant
properties of CRL. They are not yet an empirical prediction, a QFT/GR
deviation, or a selected constant.

## 7. Global unitarity does not imply no-signalling

Unitarity proves affinity, complete positivity, and trace preservation of the
joint channel. It does not prove causal locality of subsystems.

The exposed fixture itself is signalling across its declared matter/memory
factorization, as intended for a feedback interaction:

- with matter fixed to `(3/5,4/5)`, changing the memory input from `|0>` to
  `(|0>+|1>)/sqrt(2)` changes the reduced matter output by trace distance
  exactly `6/25`; and
- with memory fixed to `|0>`, changing matter from `|a>` to `|b>` changes the
  record output between orthogonal count states, trace distance `1`.

This is not faster-than-light signalling: the toy has no spatially separated
Alice/Bob factors, locality rule, light cone, or composite graph. It means
only that the source's phrase “non-signalling by construction” is false. A
future graph law must prove that the intended local feedback cannot transmit
outside its causal neighborhood and must separately run the conditional
steering gate.

## 8. No record, geometry, curvature, or growth has yet been built

The register is coherent, erasable quantum memory. In the corpus's stronger
sense it is not yet a durable record: no redundant copies, recoverability
test, division instrument, or actualization is present.

The fixture also has:

- one fixed `2 x 4` carrier;
- no relational graph consumed by the law;
- no multiple links or closed spatial loop;
- no event menu generated from a graph;
- no carrier growth or cell creation;
- no metric, causal, or volume reading; and
- no Hamiltonian, energy/stress coupling, equivalence principle, Lorentz
  limit, or GR/QFT recovery.

Calling the memory “geometry” is therefore an ontology proposal, not a result.
The safe present ontology is a matter degree of freedom coupled to a finite
quantum memory. If a future joint fixture makes one graph-indexed register
serve distance, causal accessibility, loop response, and growth—and survives
family-level eliminability—then the geometric reading may be earned.

## 9. Corrected verdict

```text
CRL-UNITARY-MATTER-MEMORY-NUCLEUS-EXISTS;
WRC-NONAFFINITY-AVOIDED-BY-CHANGING-TO-A-JOINT-UNITARY-LAW;
FULL-HOLONOMY-NONCENTRAL-WITH-FIVE-EIGENVALUES;
SAMPLED-SHADOW-LAWFUL-BUT-NOT-WRC;
TICK-FOUR-DISCRIMINATOR-CALIBRATION-DEPENDENT;
NO-SIGNALLING-GEOMETRY-RECORD-PERMANENCE-AND-GROWTH-UNBUILT.
```

This is more promising than the exposed gamma-successor toy because its
matter-to-memory and memory-to-matter actions are both operationally active
inside one lawful map. It still solves only the quantum seam at type level.
It has not solved the relational/geometric successor problem.

## 10. What a CRL-based successor unit must test

A future pin may adopt CRL only as an **explicit new base-law postulate**. It
must not present it as selected by QSF or derived from WRC. Before any Paper 10
promotion it should require:

1. a pre-frozen graph family with one register per licensed relation and one
   uniform local rule generating every `W_e` and `T_e`;
2. a comparison against alternative powers, coins, event orderings, and
   register dimensions, so “duality-forced” and declared data are separated;
3. an actual closed graph loop whose gauge-invariant transport product—not
   the bare clock/shift commutator—is the curvature witness;
4. a local-circuit or causal-comb theorem plus explicit remote and conditional
   no-signalling tests;
5. a redundant-record construction, recoverability census, complete division
   instrument, and explicit actualization postulate;
6. seed-, coin-, and `q`-robust coherent-versus-measured censuses with the
   comparison grain fixed before results;
7. all nine WRC observable families rerun at a declared division grain, with
   failure to regress accepted as evidence of a new theory rather than hidden;
8. graph-generated event menus, coherent reconvergent growth, and active
   carrier change in the same law;
9. E-37 sufficiency and B0/B1/B2 family-level eliminability on held-out graph
   sizes; and
10. explicit refusals of gravitational, continuum, particle, Hamiltonian, and
    empirical claims until their own calibrated observables exist.

Passing these gates would make CRL a credible microscopic candidate for the
missing joint successor. At present it is a lawful and imaginative quantum
memory model with a promising architectural role, not yet quantum gravity.

## 11. Literature bearings, not anchors

- D. Beckman, D. Gottesman, M. Nielsen, and J. Preskill, “Causal and
  localizable quantum operations,” `quant-ph/0102043`: causality is an extra
  property of multipartite operations, not a consequence of global channel
  lawfulness.
- S. Chandrasekharan and U.-J. Wiese, “Quantum Link Models: A Discrete
  Approach to Gauge Theories,” `hep-lat/9609042`: finite-dimensional,
  noncommuting link degrees of freedom are an established gauge-theory
  construction.
- R. Blume-Kohout and W. Zurek, “Quantum Darwinism: Entanglement, branches,
  and the emergent classicality of redundantly stored quantum information,”
  `quant-ph/0505031`: redundancy is substantive structure in the emergence of
  objective records, not supplied by a single coherent ancilla.

These references type the proposal and its debts. They do not decide ISP's
ontology or select this law.

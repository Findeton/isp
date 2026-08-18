# OVG hostile review — quantum causality, EPR, gravity/QFT, and ontology

Status: **FROZEN INDEPENDENT HOSTILE REPORT**  
Seat: **P — quantum causality, EPR, gravity/QFT, and ontology**  
Target: v16 Paper 5, candidate commit
`bb0f13aedadc354068ea2bcc08478bcd8c43ded1`  
Grade: **ACCEPT-WITH-FIXES**

## 1. Immutable-target and hash audit

I read the complete frozen OVG protocol before substantive work. I then read
the complete pin, core freeze, fixture/refusal/repair freeze, candidate
verification, generic core, repaired scorer, data-only fixture, transcript,
receipt, and generated Paper 5. I did not read, list, request, infer, or
communicate with either other OVG review seat.

All immutable bindings reproduce:

| object | bound SHA-256 | independently observed |
|---|---:|---:|
| pin | `286e681a05b7346226f4f3f381036b2b6bc07d809c93c2ac352d9f71a0f44c40` | equal |
| generic core | `7b17a138dc45f564a5180fca81bdb4620aaa570514d090d8a5c45f0f22d985bf` | equal |
| physical fixture | `7b7658492a49c77f6c9ee3e0a2031d5121c627aad5ae6630e21940a68c92b133` | equal |
| repaired scorer | `75cc0e7279ee93a60bfa520eecb4ea37fcde49b3d9e9f7298d98031396628844` | equal |
| freeze/refusal/repair record | `d44fd66678fe16ce85c2c9780142583a111776108b87788b734833419c9a3b34` | equal |
| transcript | `48cf0fdecc43b1d148c97bac936a879cbbcf14daddfccd6e597014017155fe7f` | equal |
| receipt | `4ba954430acd0772da62c8df16b2c6b08bca9e76fd7b25d3b5b72fcc43ce2852` | equal |
| Paper 5 | `89a6ad8b10b97351d71a499ebbb36b2cf5a89f32d5ec9d005f9b4a68dab16b31` | equal |
| candidate verification | `12774e1a2d9d72d147a67e066679bc6e376e29f4acecc453f3d164ce19ba37e5` | equal |

The chronology is genuine. The generic algebra froze before the physical
fixture. The first physical run refused without artifacts because one anchor
token crossed a Markdown line break. The bounded repair only normalizes
whitespace during anchor-token comparison. It did not change a matrix,
coefficient family, classifier, outcome word, or renderer.

A clean scratch invocation reproduces transcript, receipt, and paper byte for
byte. I independently recomputed all nine payload seals, 32 passing gate rows,
12 one-occurrence claims, and the total 30-name mutation contract. All 30
mutants refuse at a bound gate without writing an artifact. The scorer AST has
zero floating-point literals, and the fixture has no registered forbidden
truth key or text.

## 2. Independent method and tools

My independent exact reconstruction is
`/private/tmp/ovg-physics-review.TEd6vi/independent_check.py`. It imports no OVG
code and reads no OVG artifact. It implements CNOT permutations, Gaussian-
rational matrix algebra, channels, tensor products, and partial traces using
`fractions.Fraction`.

I also checked the candidate's causal-order terminology against primary
sources:

1. Oreshkov, Costa, and Brukner, *Quantum correlations with no causal order*,
   [arXiv:1105.4464](https://arxiv.org/abs/1105.4464), introduce a framework of
   local quantum operations without a predefined global causal order and
   exhibit correlations violating a causal inequality.
2. Chiribella, D'Ariano, Perinotti, and Valiron, *Quantum computations without
   definite causal structure*,
   [arXiv:0912.0195](https://arxiv.org/abs/0912.0195), define the quantum switch
   as a higher-order transformation of input black boxes whose order is
   coherently controlled, not merely a linear combination of two known
   circuit matrices.
3. Araújo et al., *Witnessing causal nonseparability*,
   [arXiv:1506.03776](https://arxiv.org/abs/1506.03776), define causal witnesses
   and show the quantum switch is causally nonseparable even though it does not
   violate a causal inequality.
4. Barandes, *Quantum Systems as Indivisible Stochastic Processes*,
   [arXiv:2507.21192](https://arxiv.org/abs/2507.21192), treats Hilbert-space
   operators as representations of a stochastic law on a fixed configuration
   space. This supports treating OVG's matrices as representational until its
   fine histories are independently individuated by the relational ontology;
   it does not provide the missing changing-spacetime weld.

The candidate's titles, authorship, dates, and narrow causal-nonseparability
refusal are accurate.

## 3. Exact recomputation table

| quantity | candidate | independent reviewer | status |
|---|---|---|---|
| relative CNOT order operator | `A^dagger B = CNOT(A->C)` | exact equality of `8 x 8` permutation matrices | PASS |
| real one-port weights | `(3/5,4/5)` incomplete | residual `=(24/25) Omega != 0` | PASS |
| phase-rotated weights | `(3/5,4i/5)` complete | `K^dagger K=I` exactly | PASS |
| parity ports | complete for common-boundary isometries | cross terms cancel and sum is `I` | PASS |
| phase-row nullities | `(2,2,1,1,0)` | ranks `(1,1,2,2,3)` reconstructed | PASS |
| nonnormal growth overlap | `[[0,3/5],[0,0]]`, nullity `0` | direct real-linear rank `3` | PASS |
| fixed spectator before | `diag(1/2,1/2)` | `diag(1/2,1/2)` | PASS |
| fixed spectator after parity instrument | unchanged | `diag(1/2,1/2)` | PASS |
| amplifier contrast | `diag(2,2)` | `diag(2,2)` | PASS |
| coherent-map erasure control | not run | one history `K` gives exactly the same channel as the named sum `3A/5+4iB/5` on all 64 matrix units | NEW CONTROL |

The no-signalling arithmetic has a general reason. For any all-input complete
instrument acting only on fixed subsystem `ABC`,

```text
Tr_ABC sum_j (K_j tensor I_D) rho (K_j^dagger tensor I_D)
= Tr_ABC rho.
```

The candidate machine verifies one entangled preparation and one failing
amplifier. The theorem covers every joint input at the same fixed tensor
factor. Neither statement covers conditional outcomes or a changing
definition of subsystem `D`.

## 4. Theorem and proof audit

### The exact operator theorem survives

For one port `K=aA+bB`, with unitary `A,B` and
`Omega=A^dagger B`, direct multiplication gives

```text
z Omega + conjugate(z) Omega^dagger = c I,
z = conjugate(a)b,
c = 1-|a|^2-|b|^2.
```

In an eigenbasis of unitary `Omega`, this is

```text
2 Re(z exp(i phi_k)) = c.
```

One distinct unit-circle point imposes one independent real equation, two
distinct points impose two, and three distinct points impose three because a
line intersects the unit circle in at most two points. Nullities `2,1,0`
follow. Subtracting the two-phase equations gives

```text
arg z = -(phi_1+phi_2)/2 mod pi,
```

with the candidate's sign convention. A nonzero formal direction necessarily
has `z != 0`; scaling it sufficiently small makes the quadratic with roots
`|a|^2,|b|^2` have positive roots. Thus the lifting to actual complex
coefficients is valid. The theorem is correctly restricted to unitary
relative operators; the nonnormal row uses the full operator equation.

### The parity identity survives

For common-boundary isometries,

```text
K_+=(A+B)/2,  K_-=(A-B)/2
```

obey

```text
K_+^dagger K_+ + K_-^dagger K_-
=(A^dagger A+B^dagger B)/2=I.
```

This proves mathematical existence of a complete two-port instrument. It
does not prove that the relational event grammar implements or selects it.

### “Variety constructed” needs its existing qualifier made headline-level

The general finite equations define an exact implicit polynomial solution
set, and the Pauli triad supplies a positive-dimensional embedded family with
moving calibrated screens. The candidate does not decompose irreducible
components or classify the full multi-history moduli space. Paper 5 says this
in its limitation. The primary is acceptable only when read as “implicit
operator variety and exact witness families constructed,” not “full overlap
law classified.”

## 5. Representation and ontology audit

### What exists in the candidate ontology

The intended ontology is one actual relational history. Alternative lawful
histories contribute to a history-level probability law until a complete port
records an outcome. The wavefunction, CNOT matrices, class operators, and
Gram operators are representations of that law, not additional worlds or a
fixed spacetime. Actualization remains a separate postulate.

This is coherent in principle. The delivered fixture does not yet instantiate
the key ontological premise.

### The operator orders and relational rewrites are neighboring fixtures

The CNOT event descriptors carry strings `support=[A,B]` and `support=[B,C]`,
but matrix construction ignores those strings. The token-rewrite critical
pairs are separately declared objects with different `requires/adds/deletes`
data. No gate proves that applying a token rewrite creates the carrier on which
the corresponding CNOT acts, that both operator orders reach the rewrite's
common relational future, or that a later relational probe sees their order.

Equal `8 x 8` matrix dimensions are a common vector-space boundary. They are
not, by themselves, an independently typed common *relational* boundary. The
mathematics therefore constructs coherent decompositions of fixed-carrier
circuits. Calling them configuration-individuated ISP histories remains
conditional on a missing support/rewrite/transport weld.

### The one-port sum is operationally just one unitary unless histories are calibrated

The exact counterexample map

```text
K = 3A/5 + 4iB/5
```

is itself unitary. Replacing the named pair of histories by the single history
`K` preserves the complete channel for every input and spectator. No frozen
observable distinguishes “coherent order sum” from “one ordinary three-qubit
unitary.” In a configuration-history theory, that distinction can become real
if the relational grammar independently individuates the two paths and a
calibrated continuation responds to their cross term. OVG does not build that
calibration.

Accordingly, `MULTIPORT-COHERENCE-EXISTS` is a theorem about the mathematical
instrument decomposition. Physical order coherence is permitted, not
constructed.

### Flag, record, and actualization remain separate

Stacking the parity maps gives a `16 x 8` isometry. Calling its two row blocks a
flag is a valid Stinespring-style representation. Assigning that factor to
actor `B` is catalogue metadata. The frozen elementary grammar has only
`8 -> 8` maps, no `8 -> 16` implementation, and no continuation census proving
the flag survives. It is therefore neither a local measuring mechanism nor a
durable order record. The candidate mostly says this correctly; the finding
word “local” should be removed from the positive half.

There is no contradiction with Paper 3's event-algebra doctrine once these
levels are kept separate: mathematical ports may represent possible records,
but record individuation, permanence, and actualization are additional facts.

## 6. Counterexamples and unrun controls

### C1 — decomposition-erasure control

Replace `(A,B;3/5,4i/5)` by `(K;1)`. Exact equality of class maps makes every
channel, screen, ancilla extension, and spectator marginal identical. This is
not a counterexample to the operator theorem. It is a counterexample to any
claim that the theorem alone establishes physical superposition of causal
orders.

### C2 — missing relational feed-forward control

Run the same operator family on two token-rewrite critical pairs with different
spatial adjacency but identical source/final Hilbert dimensions. The current
scorer necessarily returns the same Gram variety because its operator maps do
not read rewrite incidence. Conversely, changing the CNOT matrices does not
change any rewrite classification. This factorization shows that geometry and
operator overlap are not backreacting in the delivered object.

### C3 — flag erasure/permanence control

Append a lawful continuation that uncomputes the formal parity flag, and a
second control that redundantly copies it before erasure. The first would show
that isometric creation is not permanence; the second would test global
recoverability despite local erasure. OVG correctly leaves this unrun, so no
durability result may enter adjudication.

### C4 — steering control

Condition the remote marginal on each port and ask whether a remote choice can
select two decompositions of the same reduced state. OVG has no remote setting,
no conditional record protocol, and no changing Bob algebra, so this test is
currently unphrasable. The fixed-spectator result cannot settle the earlier
decomposition-sensitivity/steering fork.

## 7. Consequence and scope reclassification

| subject | classification after review |
|---|---|
| exact overlap operator equations | **forced** for the declared maps |
| unitary two-history phase classifier | **theorem**, over the stated unitary/complex scope |
| coherent relational event orders | **permitted**, not constructed; missing configuration-history weld |
| port law | **unselected**; several complete instruments survive |
| elementary event law and weights | **unselected** |
| primitive arity | **not forced** by the displayed binary composites; no universal minimum-arity result |
| arbitrary `n` composition | **refused** |
| local order record | formal flag factor **permitted**; implementation and permanence **refused** |
| EPR/steering | no remote steering or conditional protocol; question remains **open** |
| no-signalling | **theorem** only for unconditioned operations on a fixed tensor factor |
| changing Bob algebra | **open/untyped** |
| quantum switch | **refused** — no higher-order transformation of black boxes |
| causal nonseparability | **untested**, correctly refused |
| backreaction | **refused** — operator and rewrite controls remain neighboring fixtures |
| fields/Fock structure | **refused** |
| particles/species | **refused** |
| exchange or spin statistics | **refused**; the relative phase constraint is not statistics |
| coupling constant | **refused**; no recurring calibrated universal parameter |
| Hamiltonian | **refused**; no repeated-sector generator or time parameter reconstructed |
| curvature/gravity | **refused**; order holonomy is not spacetime curvature |
| Lorentz symmetry/continuum | **refused** |
| QFT/GR deviation | **refused**; all displayed maps are ordinary finite quantum instruments |
| empirical novelty | none selected across the surviving law family |

The primary physical result is `OVERLAP-LAW-UNSELECTED`: ordinary quantum
consistency leaves multiple operator/instrument laws. The spectral classifier
is the strongest mathematical subordinate result. It makes no empirical
prediction until the relational histories, implementation, and law point are
selected.

## 8. Grade and proposed adjudicated findings

**Grade: ACCEPT-WITH-FIXES.**

The exact counterexample to the old no-go, parity identity, spectral theorem,
nonnormal control, fixed-factor no-signalling calculation, and arity refusal
survive. The paper is unusually disciplined about causal nonseparability,
fields, gravity, QFT, and Hamiltonians. Its material defect is the missing weld
between the fixed-carrier circuit decomposition and configuration-individuated
relational histories.

Proposed finding list, in order:

1. **`OVG-IMPLICIT-GRAM-INSTRUMENT-VARIETY-AND-WITNESS-FAMILIES-CONSTRUCTED`**
2. **`SINGLE-PORT-PHASE-CONSTRAINED`**
3. **`MULTIPORT-MATHEMATICAL-COHERENCE-EXISTS-BUT-PHYSICAL-PORT-LAW-UNSELECTED`**
4. **`FLAG-DILATION-EXISTS-BUT-LOCAL-IMPLEMENTATION-AND-PERMANENCE-UNSELECTED`**
5. **`COMPOSITE-SUPPORT-DOES-NOT-FORCE-PRIMITIVE-ARITY`**
6. **`CAUSAL-NONSEPARABILITY-UNTESTED`**
7. **`RELATIONAL-ORDER-WELD-AND-OVERLAP-LAW-UNSELECTED`**

## 9. Numbered repairs and kill conditions

1. Replace “the two complete routes can lead to the same later kind of state”
   by an explicit conditional: the matrices share a codomain, while a common
   relational future is not yet welded to them.
2. Add the exact decomposition-erasure control. State that `K` is an ordinary
   unitary channel unless a relational calibration individuates the two fine
   paths.
3. Qualify the primary as an **implicit** variety plus exact witness families;
   do not imply a full irreducible-component or moduli classification.
4. Replace the positive “local flag” wording by “formal flag dilation.” Local
   catalogue assignment, event-grammar implementation, durability, and
   actualization must remain four separate rows.
5. Promote the fixed-factor/unconditioned quantifiers into every no-signalling
   sentence. Add an explicit refusal for conditional steering and changing
   subsystem algebras.
6. Add an explicit sentence that the selected phase is not exchange
   statistics, spin-statistics, a coupling constant, spacetime curvature, or a
   Hamiltonian phase.
7. Preserve the binary-composite arity refusal, but state that the Toffoli row
   only validates the grammar-relative assay and says nothing about ISP's
   selected generators.
8. Kill every physical “coherent causal order” promotion unless a successor
   unit constructs a common relational boundary, an implementation, and a
   calibrated discriminator that fails under the one-history replacement.
9. Kill any quantum-switch or causal-nonseparability promotion unless a typed
   higher-order process and an accepted process-level witness are built.
10. Kill any EPR, gravity, field, particle, Hamiltonian, Lorentz, continuum, or
    QFT/GR-deviation consequence until its separately typed object and
    calibrated observable exist.

## 10. Report SHA-256

Normalized report SHA-256:
`16950436efaeea80a6b835f63393b5d91d2a55a2fea83240205a859ecee31fcc`.

The normalized digest is SHA-256 of this UTF-8 file after replacing only the
64 hexadecimal characters on the preceding line by 64 ASCII zeroes. This
convention makes the in-file self-digest non-circular.

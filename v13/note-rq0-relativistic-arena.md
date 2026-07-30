# v13 RQ0 — the quantum regional factual base

**Status:** GREEN-UNREVIEWED, STRICT, 2026-07-30.
**Pin:** `v13/note-rq0-relativistic-arena-pin.md`, amended and narrowed by
`v13/note-rq0-quantum-substrate-amendment-pin.md` at commit
`307c36f017d9d5587334d3b79421645ee5b54c61`.
**Receipt:** `v13/code/rq0_quantum_regions_exact.py`,
`v13/code/rq0_output.txt`, and `v13/code/rq0_receipt.json`.
**Highest earned rung:** **`RQ0-FACT-DESCENT`.**

> A gauge-typed atlas of three genuinely non-isomorphic finite quantum
> regional instruments has been constructed.  Their stable record facts are
> derived from their own amplitude dynamics and descend coherently on a
> nonvacuous triple overlap certified by an exact common extension.  The same
> instruments retain nonzero cross-sector coherence and nonzero Born
> composition defects under erasing continuations.  Fact descent is
> set-valued.  A redundant-token control has groupoid-valued token descent.
> No causal order, spacetime region, volume, conformal metric, field, or
> gravity structure is claimed.

This is the forward construction required after withdrawal of
`GW2-BLOCKED-AT-1`.  It is neither a census of v10 nor the rejected classical
diamond-and-tail prototype.  No v10 object, code, fixture, event ontology, or
geometry enters the construction.

---

## 1. Claim boundary

This unit constructs the quantum factual base on which a later relativistic
arena may be attempted.  Here “region” means an operational amplitude
instrument, not a spacetime subset.  The unit does **not** define:

- a causal influence relation or cone;
- a spacetime location, coordinate, embedding, or global event set;
- a count/volume measure $\mu$;
- a conformal Lorentzian structure $[g]$;
- a field propagator, Dirac operator, stress tensor, gravity deformation, or
  backreaction law.

The schema rejects causal-order, metric, coordinate, and field-propagator
inputs.  Those guards are controls, not merely prose restrictions.

The exact programme therefore stops at

$$
\boxed{\texttt{RQ0-FACT-DESCENT}.}
$$

Token automorphisms are measured at the record overlap, but they do not earn
`RQ0-GROUPOID-ARENA`: no causal or geometric data exist to descend.

---

## 2. Primitive region and regional gauge

### 2.1 Definition

The new primitive is

$$
D=
\bigl[
X_D,\mathrm{Prep}_D,\mathrm{Amp}_D,U_D^{\mathrm{write}},
\mathrm{Pres}_D,\mathrm{Erase}_D,\mathrm{Ctrl}_D,\mathrm{Obs}_D
\bigr]/G_D.
$$

The exact types in this finite construction are:

- $X_D=\{0,1\}^{q_D}$, a finite configuration carrier;
- $\mathrm{Prep}_D\subseteq X_D$, the admitted basis preparations, with a
  distinguished actual preparation $x_{D,0}$;
- $\mathrm{Amp}_D$, a composable family of unitary amplitude arrows over
  $\mathbb Q(\sqrt2)$;
- $U_D^{\mathrm{write}}:V_0\to V_1$, the record-writing arrow;
- $\mathrm{Pres}_D$ and $\mathrm{Erase}_D$, disjoint families of
  operationally admitted continuation arrows $V_1\to V_2$, and
  $\mathrm{Ctrl}_D$, whose controls carry their own declared source/target
  slot;
- $\mathrm{Obs}_D$, a frozen family of accessible diagonal readouts;
- $G_D$, configuration relabellings together with composition-compatible
  boundary rephasing.

The physical object is the gauge class, not the displayed matrix
representative.  For an arrow $U:V_a\to V_b$ the boundary gauge is

$$
U\sim D_bUD_a^{-1},
$$

with compensated middle-boundary actions across composites.  The executable
checks outer-boundary and compensated-cut gauges separately.  It also checks
that a configuration relabelling preserves the Born shadows, composition
defect, W3 predicates, and derived algebras.

### 2.2 Provisional postulate

**Operational nomological individuation.**  A quantum region is individuated
by the composition law accessible through its admitted preparations,
interventions, and observations, modulo $G_D$.  It is not individuated only by
the history realized from $x_{D,0}$, and permanently inaccessible matrix
structure does not distinguish regions in this pass.

Every basis configuration in the three constructed regions is preparable,
and every final configuration is accessible to the frozen tomography probe.
Consequently, the carrier dimension used below is an operationally accessible
invariant rather than dormant matrix structure.

### 2.3 Why this is not a global-event subset

No ambient set $E$ exists and no inclusion $X_D\subseteq E$ is declared.
The carrier labels are local matrix indices quotiented by configuration
relabeling.  Regional comparison is performed through accessible record
restriction maps and process refinement, not through literal set
intersection.  A shared fact is certified by a common amplitude extension;
that certificate neither merges the three carriers nor declares their record
tokens to be one global occurrence.

---

## 3. Three exact quantum instruments

Let bit 0 be a branch degree of freedom and bit 1 the frozen memory readout.
For $q=2,3,4$, define

$$
U_q^{\mathrm{write}}
=\operatorname{CNOT}_{0\to1}H_0,
$$

$$
V_q^{\mathrm{pres}}
=H_0\!\bigotimes_{a=2}^{q-1}\!H_a,
$$

with the memory bit untouched, and

$$
V_q^{\mathrm{erase}}
=V_q^{\mathrm{pres}}\operatorname{CNOT}_{0\to1}.
$$

The no-write control is $H_0$.  The actual preparation is the all-zero basis
configuration, while the W3 regional scope admits all basis preparations.
All arrows are constructed exactly over $\mathbb Q(\sqrt2)$ and verified
unitary.  Named boundary spaces $V_0,V_1,V_2$ and every arrow's source,
target, and family are explicit in the receipt.  The no-write negative control
has type $V_0\to V_1$; preserve and erase both have type $V_1\to V_2$.

The regions are:

| region | qubits | carrier dimension | admitted preparations | admitted arrows |
|---|---:|---:|---:|---|
| $D_1$ | 2 | 4 | 4 | preserve, erase, no-write control |
| $D_2$ | 3 | 8 | 8 | preserve, erase, no-write control |
| $D_3$ | 4 | 16 | 16 | preserve, erase, no-write control |

The dimensions are pairwise unequal.  Because the full carrier is exposed by
the declared preparation/tomography scope, a regional isomorphism would need
a carrier bijection.  The three bijection domains are empty, proving exact
pairwise non-isomorphism under the declared gauge.  This is an accessible
invariant proof, not a distinction by filenames or prose.

The extra degrees of freedom in $D_2$ and $D_3$ are operationally active under
the continuation; they are not hidden coordinates or a planted causal DAG.
The three regions also form an exact refinement family at the Born-shadow
level (§7).

---

## 4. Records are derived from the same amplitudes

### 4.1 Frozen readout

Before applying any W3 predicate, the candidate is frozen as

$$
r_D(x)=x_1\in\{0,1\}.
$$

The policy string fixes the memory bit, value alphabet, full-configuration
tomography probe, and prohibition on partition search.  Its SHA-256 is
`0402cb35c215bc7d01a86e5b01e9e25c85d6bd69df951549f1265c367ae0ab79`.
The dimension-specific readout-value hashes are printed and locked in the
receipt.  No readout partition is fitted after seeing H-corr or H-avail.

$\mathcal R(D)$ is not a component of $D$.  For each frozen readout,

$$
\mathrm{Occ}_D(r)
=H_{\mathrm{corr}}(U_D^{\mathrm{write}},r),
$$

and, continuation by continuation,

$$
\mathrm{Avail}_D(r;V)=H_{\mathrm{avail}}(V,r).
$$

The executable then derives

$$
\mathcal R_D^{\mathrm{hist}}
=\operatorname{Bool}\{r:\mathrm{Occ}_D(r)=1\},
$$

$$
\mathcal R_D(V)
=\operatorname{Bool}\{r:\mathrm{Occ}_D(r)=1,
\mathrm{Avail}_D(r;V)=1\},
$$

and

$$
\mathcal R_D^{\mathrm{pres}}
=\bigcap_{V\in\mathrm{Pres}_D}\mathcal R_D(V).
$$

### 4.2 Exact result

For all three regions:

- H-corr passes for $U_D^{\mathrm{write}}$ on every admitted basis
  preparation, so the record historically occurs;
- H-avail passes for $V_D^{\mathrm{pres}}$;
- H-avail fails for $V_D^{\mathrm{erase}}$;
- the historical and persistent algebras are both generated by the memory
  proposition at the appropriate scopes;
- replacing the write arrow by the no-write control makes H-corr fail.

Thus erasure removes current availability without rewriting the derived
historical occurrence as “never happened.”  This is the W6 occurrence versus
availability distinction realized inside one amplitude instrument.

---

## 5. The process remains quantum away from the record seam

For a continuation $V$, write the exact cut-coherence entries as

$$
\mathcal C^{ij}_{k\ell}
=V_{ik}(U_D^{\mathrm{write}})_{kj}
\overline{V_{i\ell}(U_D^{\mathrm{write}})_{\ell j}}.
$$

Under the preserving continuation, H-avail removes all cross-sector terms
and H-corr removes the remaining within-sector off-diagonal terms.  In every
region:

$$
\Delta^B(V_D^{\mathrm{pres}},U_D^{\mathrm{write}})=0.
$$

The separately typed coarse record quotient exists and its residual is

$$
D_R(V_D^{\mathrm{pres}})
=\Gamma^R_{20}-\Gamma^R_{21}\Gamma^R_{10}=0.
$$

Under the erasing continuation, H-avail fails and cross-sector coherence is
restored.  The exact nonzero counts are:

| region | nonzero cross-sector $\mathcal C$ pairs | nonzero entries of $\Delta^B$ |
|---|---:|---:|
| $D_1$ | 8 | 8 |
| $D_2$ | 32 | 32 |
| $D_3$ | 128 | 128 |

The eraser has no well-defined quotient kernel on the memory algebra.  Hence
the classical record seam and recoherence arise from alternative
continuations of the **same** record-writing amplitude law.  The record is
not a canned memory witness attached to a classical process, and one-step
Born probabilities do not determine the accessible composite law.

An exact phase control makes this last point independently: an uncompensated
cut sign insertion leaves both one-step Born shadows unchanged but changes
the composite Born law, and exhaustive allowed readout-preserving
relabelings do not identify the two composites.  Compensated cut insertion
is, by contrast, verified gauge.

---

## 6. Common-extension certificate and fact descent

### 6.1 Shared fact, not shared-law inference

Matching binary laws would not prove fact co-reference.  The atlas therefore
uses a fourth, exact, operationally accessible amplitude instrument with one
branch bit and three record bits:

$$
U^{\mathrm{ext}}
=\operatorname{CNOT}_{0\to3}
 \operatorname{CNOT}_{0\to2}
 \operatorname{CNOT}_{0\to1}H_0.
$$

Its preserving continuation is $H_0$, leaving all three record bits
untouched.  At the declared all-zero preparation, the constructed joint
support and law are exactly

$$
\operatorname{supp}(r_1,r_2,r_3)
=\{(0,0,0),(1,1,1)\},
$$

$$
P(0,0,0)=P(1,1,1)=\frac12.
$$

The joint readout passes the scoped H-corr and H-avail tests.  The three
restriction maps are explicitly constructed as

$$
\pi_a(v_1,v_2,v_3)=v_a,
\qquad a=1,2,3,
$$

on the joint support.  Each marginal is exactly the record law derived from
the corresponding regional write arrow.  The common extension therefore
certifies co-reference of one binary fact.  It does **not** identify the full
regional amplitude instruments, carriers, or event tokens.

### 6.2 Coherent triple

All two bijections of the binary fact alphabet are enumerated for every
pair.  Diagonal joint support forces one map—identity—on each pair.  Therefore

$$
\phi_{12}\phi_{23}=\phi_{13}
$$

exactly on the nonvacuous shared fact algebra.  The fact maps consume support
only; a source-level audit rejects phase, amplitude, Born, defect, coordinate,
metric, and field data from the fact-map predicate.

At this rung the regional site is the finite **fact-interface groupoid**:
objects are $D_1,D_2,D_3$; its nine arrows are the unique certified fact maps
for every ordered pair; and $(D_1,D_2,D_3)$ is the declared covering family
with the displayed nonvacuous triple overlap.  The executable checks the three
identities, nine inverse laws, and all 27 composable-triple laws.  This site is
only the accessible fact interface of the quantum regions.  It does not
promote the fact arrows to isomorphisms of the full, non-isomorphic amplitude
instruments.

### 6.3 Token groupoid control

The regional memory tokens retain distinct names and provenance:

$$
t_a=(D_a,\mathrm{write},\mathrm{memory\ readout}).
$$

Swapping the first two record bits is an exact symmetry of both common-
extension amplitude arrows, fixes the preparation, and preserves the diagonal
support.  The two redundant tokens therefore have the full $S_2$ automorphism
family; the receipt retains both maps and selects no representative.

On three presentations of this two-token fibre, identity, identity, and swap
are individually admissible pair maps but have nonidentity loop holonomy.
This is the twisted control: token descent is groupoid-valued while the fact
map remains uniquely forced.  The symmetry is at the certified record-token
layer; it does not assert an isomorphism between the non-isomorphic full
regions.

---

## 7. Refinement

$D_2$ refines $D_1$ by one accessible extra bit, and $D_3$ refines $D_2$ in
the same way.  For each extra-input value, summing the fine Born shadow over
the extra-output fibre exactly recovers the coarse write, preserve, and erase
shadows.  Both refinement comparisons pass for all extra-input values.

The derived memory generator is preserved.  Full quantum information is not
silently identified: the eraser defect support grows from 8 to 32 to 128
nonzero entries and is printed.  These are operational instrument/refinement
maps, not spacetime-resolution maps.

---

## 8. Mandatory controls

| control | exact result |
|---|---|
| C1 relabelled region | Born shadows, defect, W3 status, and derived algebras invariant |
| C2 distinct process | equal one-step Born shadows; uncompensated cut changes accessible composite law; no allowed relabelling identifies it |
| C3 redundant record | one common-extension-certified fact, provenance-distinct tokens |
| C4 erasure | historical occurrence remains; current availability fails; cross-sector coherence returns |
| C5 coherent triple | three non-isomorphic regions, nonvacuous diagonal joint support, unique fact maps, exact triple law |
| C6 twisted triple | pairwise token-fibre maps valid; loop holonomy is the nonidentity swap |
| C7 groupoid symmetry | exact $S_2$ amplitude symmetry; full family retained, no representative selected |
| C8 causal mismatch ceiling | no localized influence instrument; classified `FACT-DESCENT-ONLY` |
| C9 geometry insertion | causal-order, coordinates, and metric inputs rejected at schema boundary |
| C10 refinement | write/preserve/erase shadows and record generator restrict exactly; full-defect changes reported |
| C11 field independence | field-propagator input rejected; no field object appears in reconstruction |

The run has 73 checks, all passing in exact arithmetic.

---

## 9. Four-gate audit of the new objects

### 9.1 Quantum region

- **REFERENT:** an operationally admitted family of preparations, composable
  amplitude arrows, interventions, and accessible readouts.
- **NECESSITY:** fact descent needs local objects without assuming a global
  event set or spacetime region.
- **NO-SMUGGLING:** no coordinates, DAG, causal cone, metric, or field enters
  the type; the schema rejects them.
- **DISCRIMINATOR:** accessible carrier dimension, composite laws, W3 status,
  phase control, and relabel/gauge controls distinguish physical differences
  from presentation changes.

### 9.2 Derived record algebra

- **REFERENT:** frozen accessible readouts passing W3 H-corr/H-avail at their
  declared continuation scope.
- **NECESSITY:** overlaps must concern classical facts available to the
  regions, not arbitrary amplitude labels.
- **NO-SMUGGLING:** the candidate partition is locked before testing and no
  record algebra is primitive.
- **DISCRIMINATOR:** no-write, preserving, and erasing continuations produce
  different exact W3 outcomes.

### 9.3 Physical overlap and fact map

- **REFERENT:** a common record-preserving amplitude extension with diagonal
  joint support and explicit restrictions.
- **NECESSITY:** equal laws do not imply same fact; W6 requires a co-reference
  certificate.
- **NO-SMUGGLING:** only joint record support enters the fact-map predicate;
  phase is excluded.
- **DISCRIMINATOR:** coherent and twisted triples separate unique fact descent
  from ambiguous token descent.

### 9.4 Refinement

- **REFERENT:** exact marginalization maps between operational amplitude
  instruments and their record algebras.
- **NECESSITY:** the later arena requires comparisons across finite
  resolutions.
- **NO-SMUGGLING:** the map uses configuration fibres and Born shadows, not a
  spatial scale or embedding.
- **DISCRIMINATOR:** the record shadow is preserved while changed full
  composition-defect support is reported.

---

## 10. Answers to the RQ0 report questions

1. **What is a finite physical region?**  The gauge class of a finite,
   operationally closed amplitude-instrument family with admitted
   preparations, continuations, controls, and readouts.
2. **Why is it not a subset of a global event set?**  No global carrier is
   defined.  Local labels are gauge, and comparisons use process/refinement
   and record-restriction maps rather than set intersection.
3. **What is its local process object?**  A typed composable family of exact
   unitary amplitude arrows over $\mathbb Q(\sqrt2)$, including one write
   arrow and preserving, erasing, and control continuations.
4. **How are W3-stable records obtained independently?**  A hash-locked
   memory-bit readout is tested against H-corr on the write arrow and H-avail
   separately on each continuation.  The algebras are derived afterward.
5. **What is a physical overlap?**  At this rung, a common accessible stable
   fact certified by a record-preserving amplitude extension with explicit
   restriction maps—not literal carrier intersection.
6. **How do shared facts descend?**  Diagonal common-extension support forces
   unique pair maps, and those maps satisfy the triple law exactly.
7. **When is token descent set- or groupoid-valued?**  The certified fact
   descends in sets.  Redundant, symmetry-related record tokens retain $S_2$,
   so token descent is groupoid-valued in that control.  No arbitrary token
   representative is chosen.
8. **What is the intrinsic causal relation?**  None is constructed.  Process
   composition order is not relabelled as relativistic causal order.
9. **What does $\mu$ count?**  Nothing yet: $\mu$ is not defined in this unit.
10. **How is $[g]$ reconstructed?**  It is not.  No field, planted geometry,
    or order-to-metric estimator is used.
11. **Do causal, volume, and conformal data descend on the triple?**  No such
    data exist.  Stable facts alone descend; the correct classification is
    `FACT-DESCENT-ONLY`.
12. **What is the first unresolved obstruction?**  A typed, gauge-invariant
    referent for an intervention localized to one quantum subinstrument or
    interface.
13. **Which claims have which status?**  See §11.

---

## 11. Claim classification

| statement | status |
|---|---|
| primitive quantum-region type and regional gauge | definition |
| operational nomological individuation | provisional postulate |
| W3 occurrence/availability schema and boundary-gauge reduction | inherited theorem/schema from Paper 1 at its stated scope |
| occurrence, availability, record algebras, coherence counts, $\Delta^B$, and $D_R$ for $D_1,D_2,D_3$ | exact measurements |
| preserving-seam division of labour | inherited theorem instantiated and exactly checked |
| common-extension diagonal support and restrictions | constructed certificate |
| unique fact descent and exact triple law | exact finite theorem/measurement for this atlas |
| accessible-dimension non-isomorphism | exact finite theorem for the declared scope |
| redundant-token $S_2$ and twisted holonomy | exact finite measurement/control at the token layer |
| existence of a quantum-native localized influence relation | open |
| emergence of causal order, $\mu$, $[g]$, fields, or gravity | not claimed |
| extension from these finite fixtures to a general regional theory | conjectural/open |

---

## 12. Exact scope, receipts, and limitations

- Arithmetic: exact $\mathbb Q(\sqrt2)$; no floats or tolerances.
- Random seeds: none.
- Regional preparation search: none; every basis preparation is admitted and
  the actual preparation is 0.
- Common-extension preparation scope: the declared all-zero preparation.
- Readout search: none; one frozen binary memory candidate per region.
- Fact-map search: both bijections of the binary value alphabet.
- Token-map search: both bijections of the two-token redundant fibre.
- Regional isomorphism discriminator: exact accessible carrier dimension.
- Numerical geometry: none.
- Runtime cap recorded in the receipt: 120 seconds.
- Legacy code imported: none.
- v10 and earlier used as ontology, fixture, benchmark, or data: none.

The construction proves a finite existence result, not genericity, a
continuum limit, or Lorentzian kinematics.  The three regions belong to one
deliberately transparent refinement family; their non-isomorphism and shared
fact are exact, but broader atlas classes remain to be constructed.  The
common extension certifies record fact co-reference only.  It is not a global
wavefunction postulate and does not amalgamate all regional process data.

Reproduction:

```bash
PYTHONPYCACHEPREFIX=/tmp/isp-rq0-pycache \
  /opt/homebrew/bin/python3.13 v13/code/rq0_quantum_regions_exact.py

PYTHONPYCACHEPREFIX=/tmp/isp-rq0-pycache \
  /opt/homebrew/bin/python3.13 v13/code/rq0_quantum_regions_exact.py --json

PYTHONPYCACHEPREFIX=/tmp/isp-rq0-pycache \
  /opt/homebrew/bin/python3.13 v13/code/rq0_quantum_regions_exact.py --mutant
```

Two clean text runs and two JSON runs are byte-identical.  The deliberate
anchor mutant exits 1 with exactly one visible failed check.  The committed
text and JSON receipts are regenerated from the same executable.

---

## 13. Required successor and halt

The first missing referent is **localized quantum subinstrument**.  A future,
separately pinned `RQ0-C1 — operational influence between regional record
algebras` may define

$$
A\rightsquigarrow B
$$

only after it can type two interventions as differing solely on the declared
$A$-subinstrument.  It must then test gauge invariance, record screening,
restriction, genuine triple descent, cycles, and refinement stability.
“Later” may not be inserted as a relativistic order merely because amplitude
arrows compose.

No diamond, causal set, hidden DAG, causal estimator, $\mu$, $[g]$, RQ1
field, or gravity dynamics is opened in this run.  Per the amendment pin, the
unit halts here.

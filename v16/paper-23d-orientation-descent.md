# Paper 23d — orientation does not descend through any admissible whole-process weight

## Theorem/no-go under frozen pin #332 (mathematics only)

Date: 2026-08-22

Construction-stage status: built solely from the pin's four frozen
objects, terminal Paper 13D (`3b91766f…`), the #308 disintegration
typing, and the #330 corrected target type. No code; no new primitive
orientation; exact rational arithmetic. Primary disposition:
**`P23D-ORIENTATION-FIBER-INERT`** (universal), with
`P23D-CLEAN` on the smuggling audit and precise failure attributions
in §6.

## 1. Setup from the pin

$\mathsf{Cpx}$: isomorphism classes $[\chi]$ of unmarked process
complexes; $\Sigma_\chi$ the presentation-invariant colimit σ-algebra.
Root variables: finite diagram invariants only (§3 of pin). Admissible
weights: $\mathcal P$ = projective, covariant, normalized,
scheduler-independent measures with finitely supported finite
restrictions; named subfamilies $\mathcal P_{\rm unif},\mathcal
P_{\rm v},\mathcal P_{\rm size}$. Joint law constraint (#308):
$\Gamma_{\rm struct}(d[\chi],dH)=\Pi(d[\chi])\,\Gamma_D(dH\mid[\chi])$
— the regular conditional stays exactly Γ_D. Extractor: admissible
observable valued in exchangeable realizer-pair classes (the #330
target).

**Definition 1.1 (fiber).** For $[\chi]\in\mathsf{Cpx}$, the fiber
$\mathcal F_{[\chi]}$ is the set of exchangeable realizer-pair classes
realizable over that complex — ordered pairs of total orders on its
carrier modulo simultaneous transport and rank swap.

## 2. The fiber-multiplicity lemma

> **Lemma A (within-fiber multiplicity).** For every complex whose
> carrier has $|I|=n\ge2$, the fiber hosts at least two distinct
> exchangeable classes; for the unmarked primitive this number is
> $\frac12\big((n!)^2 + \text{self-swap count}\big)$ restricted to
> transport-orbit classes — computed as $2,5,17$ for $n=2,3,4$
> (exact enumeration). Only $|I|\le1$ fibers are singletons, and those
> carry no nontrivial orientation content (the intersection condition
> is vacuous or forced).
>
> **Proof.** Antiparallel $[(L,\mathrm{rev}\circ L)]$ and parallel
> $[(L,L)]$ are never transport+swap related for $n\ge2$: a transport
> preserves the relative agreement pattern of the two ranks, and these
> two pairs agree nowhere versus everywhere. Both realize over every
> complex (the decoration is not part of the diagram class). ∎

> **Lemma B (weight inertia).** Every $\Pi\in\mathcal P$ is constant on
> fibers by construction: it assigns one mass to $[\chi]$, and no
> member of $\mathcal P$ may condition on anything inside
> $\mathcal F_{[\chi]}$ (root variables are diagram invariants; the
> σ-algebra is presentation-invariant; scheduler independence bars
> trace-level distinctions beyond points of $\mathsf{Cpx}$).
>
> **Proof.** Immediate from pin §§2–4. ∎

## 3. The four-way classification

**(Q1 — orientation already χ-measurable? NO.)**
Suppose a measurable covariant $E:\mathsf{Cpx}\to$ exchangeable
classes realizes the intersection condition nontrivially. Restrict to
the singleton-diagram subcategory (complexes with empty generator set,
free carriers): $E$ becomes an assignment of total orders natural under
all bijections of finite sets — impossible for $|I|\ge2$ by
`P23C-NO-COVARIANT-SINGLE-ORDER` (Prop B), which the restriction
inherits verbatim. Hence **no** such function exists: ∀Π verdict, and
Π is irrelevant because the extractor has nothing to read.

**(Q2 — support selection? NO for every Π∈P except trivial supports.)**
Support restriction can zero complexes but acts *between* fibers;
Lemma A shows the ambiguity lives *inside* every fiber with
$|I|\ge2$. A support of only $|I|\le1$ complexes selects nothing
nontrivial. The sharpest objection — landmark-rigid experiments have
trivial stabilizers — fails twice: marks are forgotten when forming
$[\chi]$ (Paper 17 note §2), so rigidity is invisible at the weight's
own input space; and even granting asymmetric-program complexes
(trivial automorphism groupoid, labeled cells survive), Lemma C
rank-blindness persists field-by-field, so the fiber still hosts all
$n!^2$ labeled decorations — e.g. 21 swap classes over a trivial-
groupoid $n{=}3$ complex. **∀Π: no.**

**(Q3 — distinct orientations within one fiber? YES — the deep form.)**
By Lemmas A+B: the witness classes $[(L,\mathrm{rev}\circ L)]$ and
$[(L,L)]$ sit in one fiber; every joint law of the #308 form gives them
identical mass ($\Pi([\chi])\cdot$ identical conditional) and identical
conditional fields. Two consequences, both proved:

(i) *No well-definedness without fiat*: an extractor distinguishing
them is not a function of any admissible event of the joint space —
its would-be values are invisible to $\Gamma_{\rm struct}$.

(ii) *Even declared by fiat*, its output law under any
$\Pi,\Pi'\in\mathcal P$ is identical: scalar weights cannot create new
measurables. **This is the precise sense in which weights fail because
they cannot create new observables.**

**(Q4 — smuggling audit: CLEAN.)** No rank, label, root field outside
pin §3, support gerrymander, or refined σ-algebra enters the argument;
the only orders ever mentioned appear inside the *target* definition
imported contract-only from Paper 15. The proof works entirely over
the pinned spaces.

## 4. Main theorem

> **Theorem C (no orientation descent).** For every admissible
> $\Pi\in\mathcal P$ and every admissible extractor $\mathcal E$: if
> $\mathcal E$ is well-defined on the joint space of
> $\Gamma_{\rm struct}=\Pi\cdot\Gamma_D$, then $\mathcal E$ is constant
> across each fiber $\mathcal F_{[\chi]}$. Consequently no admissible
> whole-process law of the #308 form determines the exchangeable
> oriented null-realizer class on any carrier of size $\ge2$; the
> orientation observable is not created, selected, or made unique by
> any state weight over process complexes.
>
> **Proof.** Q1 rules out χ-measurable supply; Lemma B makes every Π
> fiber-constant; Lemma A places the ambiguity inside fibers; Q3(i)
–(ii)
> convert this to non-well-definedness and, under fiat declaration, to
> output-law identity across $\mathcal P$. ∎

Outcomes earned:

```text
P23D-ORIENTATION-FIBER-INERT      (primary, universal: ∀Π∈P)
P23D-CLEAN                        (Q4 audit passed)
```

Not earned: `-CHI-MEASURABLE`, `-SUPPORT-SELECTED`,
`-NOT-SELECTED` (superseded by the sharper positive negative:
fiber-inertness is proved, not merely non-selection).

## 5. Quantifier ledger

| clause | quantifier |
|---|---|
| no χ-measurable orientation (Q1) | universal (∀ constructions, Π-free) |
| no support selection with nontrivial content (Q2) | universal (∀Π∈P) |
| fiber multiplicity ≥2 for \|I\|≥2 (Lemma A) | universal |
| weight inertia (Lemma B) | universal (∀Π∈P) |
| named subfamilies cannot distinguish witnesses | existential check on all three pre-registered families — none qualifies |
| what is NOT selected: whether some non-scalar, history-dependent extension could orient | left open by design; such extensions retune the conditional physics (Paper 17 note §3, control 5) |

## 6. Failure attribution (required by pin §7)

Weights fail for **both** pinned reasons, now precisely separated:

1. **Fiber-inertness** (structural): $\Pi$ is constant on fibers while
   the target varies within fibers (Lemmas A+B).
2. **Orientation-blindness of the conditional** (inherited): Γ_D's
   fields carry no occurrence-order datum anywhere — occurrence data
   live in finite sets ($I$, $\binom I2$, orbit cells) and the trace's
   only ordered structures are per-generator source/target kinds, not
   occurrence orders (13D §7.1/§8) — so even a fiber-varying weight
   over histories could not read an order out of H.

Hence the obstruction is not an artifact of scalar weighting alone: it
reflects that the joint space, typed per #308, contains no measurable
copy of the orientation at all. Creating one requires either refining
what a history *is* (new postulate) or breaking symmetry in the
primitive law — the two doors of synthesis §3, both outside this unit's
authorization.

## 7. Scope

Present-$\Gamma_D$ fixtures under the #308 typing; the pinned
$\mathsf{Cpx}$, Σ_χ, root variables, family $\mathcal P$, and target
type. Positive results: none beyond the residual already engraved at
#330/#331. This unit opens neither Paper 17 nor dimension selection;
the ensemble gate remains closed. Walls per pin §8 unchanged. No
automatic successor exists.

## 8. Comparators

Terminal Paper 13D bytes; #308 disintegration record; Paper 17
joint-law note (compatible-extension theorem and its exogeneity
constraint); #330 corrected target; #331 synthesis door distinction.
Barandes fixed-law/standalone-distribution distinction as background
context only. No comparator supplies probability, orientation, or
dimension.

# R1 — OPERATOR-LENS HOSTILE REVIEW, RQ0-L4 BRANCH C

## The 12-orbit theorem re-derived, and the edge it does not cover

**Reviewer:** R1 (operator lens), K1 primary.
**Protocol:** `v13/note-rq0-fingerprint-hostile-protocol.md` (frozen, c120ea3).
**Object:** `v13/paper-rq0-nomological-fingerprint.md` +
`v13/code/rq0_l4_fingerprint_*` at 75e0977. **Pin:** b4fc87c. **Base:**
a5cb096.
**Method:** own exact code, `/opt/homebrew/bin/python3.13`, integers and
`Fraction` only, nothing imported from the unit; every object rebuilt from its
declared definition. 25 independent recomputations. No repo file but this one
was written; no git mutation.

---

## VERDICT: **ACCEPT-WITH-FIXES**

The 12-orbit census, the factoring argument, the 52×52 identification, the
committed triple's three-orbit structure at sizes 6/3/1, the group orders
24/24/24/24/1, and **every numerical value I recomputed** are correct. No
computed number in the paper moved under independent re-derivation, and I found
no false arithmetic anywhere in my object.

The fixes are three, and the first is load-bearing:

1. **The identification `shape = resolution` is NOT exact.** The orbit
   invariant is the level-refined shape profile — **12** classes. Resolution
   data proper (the block-size profile, which is what the pin's gate 2 and the
   paper's own §7.4 name) is strictly coarser — **7** classes. Exactly **5**
   resolution profiles split into two orbits each. So there exist covariant
   statistics that are *not* functions of resolution data, and one of them is
   the unit's own **C4a**.
2. Consequently `RQ0-L4-CLASS-IMPOSSIBILITY` is **reading-dependent**: it holds
   for the unit's strengthened G2b (where it is, once Theorem 7.1 is in hand, an
   immediate tautology), and **fails for the pin's gate 2**, under which the
   corridor at DET — a symmetric law — is inhabited. I exhibit two inhabitants,
   one of them declared by the unit itself.
3. The freeze barrier's claim is **false as worded**: the covariance gate
   evaluates every declared candidate at two of the four committed boundaries,
   **864** times, and the barrier cannot see it.

None of this overturns the unit's substantive result. No fingerprint is
delivered by either inhabitant; the dichotomy of Theorem 8.1 catches both, and
my repair (finding F5) shows Theorem 7.2 and Theorem 8.1 are *the same theorem*
— which is a strengthening, not a retreat. The fixes are to sentences, scope
tags and one instrumentation claim.

---

## FINDINGS, RANKED

### F1 — MAJOR. The orbit invariant is strictly finer than resolution data: 12 against 7, with 5 splittings.

This is the K1 edge, and it is inhabited.

The admitted-isomorphism group at the committed configuration is
Sym{0,1,2,3} — order 24, confirmed elementwise — and it is produced **entirely
by the declared state**: DET, REV and the funnel closure are Sym(5)-invariant
by construction, so the only symmetry-breaking datum is ρ's 4+1 level
structure. Under that group the 52 records fall into 12 orbits and the orbit
invariant is the shape profile, *as the paper says*, where "shape" means the
multiset over atoms of `(|r ∩ {0,1,2,3}|, |r ∩ {4}|)`.

But the paper repeatedly identifies that invariant with **resolution** data —
the sizes of the atoms, the block-size profile, "how much they resolve". That
identification is measurably false:

| invariant | classes on the 52 records |
|---|---|
| ε (the Bayes error) — measured `= (5−\|π\|)/16` at all 52 | **5** |
| the block-size / resolution profile (pin's gate 2, paper §7.4) | **7** |
| the level-refined shape profile = the orbit invariant (G2b) | **12** |
| the full record lattice | 52 |

Exactly **5** of the 7 resolution profiles split into two orbits apiece
(12 = 7 + 5). The splittings, with a representative and the sink-block excess
`s = |block(4)| − 1`:

| atom sizes | orbit A (|orbit|, s) | orbit B (|orbit|, s) |
|---|---|---|
| 1,1,1,2 | `0\|1\|2\|34` (4, s=1) | `0\|1\|23\|4` (6, s=0) |
| 1,1,3 | `0\|1\|234` (6, s=2) | `0\|123\|4` (4, s=0) |
| 1,2,2 | `0\|12\|34` (12, s=1) | `01\|23\|4` (3, s=0) |
| 1,4 | `0\|1234` (4, s=3) | `0123\|4` (1, s=0) |
| 2,3 | `01\|234` (6, s=2) | `012\|34` (4, s=1) |

The datum that separates each pair is *how many success addresses the boundary
merges with the retained sink*. That is not "how much a boundary resolves" — it
is **which** configurations it merges, relative to the one configuration the
declared state marks out. Two boundaries can hide exactly as much of the
carrier and still differ covariantly.

**The control that settles it.** At the *uniform* state the admitted-isomorphism
group is 120, the orbits are **7**, and the orbit invariant is **exactly** the
block-size profile (measured over all 52×52 pairs). The paper's sentence is the
uniform-state theorem, carried unchanged into the committed state, where the
4+1 level structure makes it false.

### F2 — MAJOR. Under the pin's gate 2 the corridor at DET is not empty. C4a inhabits it, and so does a construction that also clears the inherited G1 and refuses total erasure.

The abstract says "corridor gate 2 and corridor gate 5 are jointly
unsatisfiable: no candidate is both covariant and non-resolution at DET, **as
the theorem requires and as the family measures**". The pin's gate 2 is quoted
in Appendix A.1 as *"not Bayes-error-like — must not factor through
partition-size or resolution data"*. Measured on my own routes at DET:

**C4a — the unit's own declared candidate — passes every one of the pinned
corridor gates at DET under that wording.** G3 nondegenerate (3 values off
fixture); monotonicity type **"neither"**, so it clears the pin's G1 *and* the
inherited A16 constraint; not a function of ε; **not a function of the
resolution profile**; covariant under all 24 admitted isomorphisms; and it
separates the committed triple, 0 against 1/4 and 1/4. The explicit witness
that it is non-resolution: `C4a(0123|4) = 0` but `C4a(0124|3) = 1`, and both
boundaries have atom sizes {1,4}. The **only** pinned gate C4a fails is G2b —
the strengthened reading the unit itself introduced in Deviation 1.

I then constructed the maximal attack the protocol asked for, inside the
declared data:

> **C5 := C4c + 1000·(|block(sink)| − 1)**, the negated merged-pair count
> penalised by the sink's block excess.

Measured at DET: G3 ✓ (10 values on the 48 off-fixture records); monotonicity
type **"neither"** — it satisfies the terminal cycle's own §10 successor
constraint that the paper reports nothing satisfies; G2a ✓; **not a function of
the resolution profile** ✓; G5 covariant under all 24 ✓; separates the triple
−12 against −4 and −2 ✓; and — unlike every separator the unit found —
**it does not certify total erasure**: the one-atom boundary sits at 3980,
three thousand nine hundred and ninety-two above the legitimate chart, so the
tolerance that admits the legitimate patch and rejects both forgeries rejects
total forgetting. It fails G2b, and G2b alone.

So the honest statement of the emptiness is: **the corridor is empty at the
committed configuration under G2b, and G2b is strictly stronger than the pin's
gate 2.** The unit never declares that strengthening as a strengthening —
Deviation 1 justifies G2b only by saying G2a "would admit block-profile
statistics that read nothing but resolution", which is an argument for
excluding the 7-class invariant, not the 12-class one.

**What C5 does not do**, stated against my own construction: it delivers no
fingerprint. It is a function of the declared boundary alone, so the terminal
collision defeats it exactly as it defeats everything; and it is *state-reading*
— at the relabelled state ρ′ = (3/4, 1/16, 1/16, 1/16, 1/16) its values on the
triple become 998, 996 and **2988**, and the separation **inverts**. The amnesty
sweep would kill it. The dichotomy holds against my best attempt.

### F3 — MAJOR (instrumentation). The covariance gate evaluates every candidate at two committed boundaries, 864 times, and the freeze barrier cannot see it.

This falls straight out of the orbit census, which is why the operator lens
finds it. `orbit(2+1+1)` has size 6 with **5** members off-fixture;
`orbit(2+2)` has size 3 with **2** off-fixture. G5 is implemented as
`fn(act_part(p, g), …) == vals[p]` for `p` in the 48 off-fixture records and
`g` in the group — so covariance **cannot** be tested without leaving the
off-fixture set, and the images land on the committed boundaries. Measured:

* **36** evaluations of a candidate at a committed boundary per (candidate,
  symmetric law) — 20 landing on the forged 2+1+1, 16 on the forged 2+2;
* **0** at the counter-law (trivial group);
* **144** per candidate over the five laws; **864** over the six declared
  candidates — all inside the corridor stage, all before `L4-FREEZE`.

`_TOUCHED_FIXTURE` is set only by an explicit `touch()` call, and the
covariance loop never makes one. So `L4-FREEZE` passes while its own claim —
"NONE of them evaluated ANY declared candidate at ANY of the four committed
boundaries" — is false, and §3's "Every gate carries a provenance flag
recording whether any committed boundary had been evaluated when it fired" is
false: the flag records whether `touch()` was *called*, not whether a boundary
was *evaluated*. The `freeze-lax` mutant cannot catch this, because it tests
flag-*reading* (it calls `touch` and checks the barrier notices) rather than
flag-*setting*.

**Severity.** The freeze's substance survives: the six definitions were
SHA-256-registered at `L4-00` before any evaluation, no fixture value is
retained or compared against a threshold in G5 (each is equality-tested against
its own off-fixture orbit partner), and no verdict could have been tuned. This
is a false claim about the instrument, not a broken freeze. But the claim is
one of the unit's three advertised freeze devices and it should not be repaired
silently: the fix is to say what is true — *no corridor gate compared a
candidate's fixture value to anything but its own orbit image, and no gate
retained one* — and to declare it as a deviation, because covariance is an
orbit property and the orbits provably meet the fixture.

### F4 — MODERATE. Under G2b the class impossibility is a tautology; all the content is Theorem 7.1.

With Theorem 7.1 in hand the argument is: covariant ⟹ constant on orbits ⟹
constant on shape-classes ⟹ ¬G2b. G2b is *defined* as "not a function of the
covariant shape invariant". So "gate 2 and gate 5 are jointly unsatisfiable" is
`P ∧ ¬P`, and Theorem 7.2 adds nothing to Theorem 7.1. That is not a defect in
the mathematics — Theorem 7.1 is correct and its nontrivial direction ("same
shape ⟹ same orbit"; the converse is free, shape being manifestly covariant)
is a real, if small, combinatorial fact, `#orbits = Σ_{s=0..4} p(4−s) =
5+3+2+1+1 = 12`. It is a defect in the presentation: the impossibility is
announced as a theorem about *statistics* when it is a theorem about *one
finite invariant*, and the reader cannot see from §7 that the gate was chosen
to be the complement of the conclusion.

### F5 — CONSTRUCTIVE. The repair: Theorem 7.2 and Theorem 8.1 are the same theorem.

The whole 12-vs-7 gap is state-derived — at the uniform state it vanishes
identically (F1's control: group 120, orbits 7, orbit invariant = block-size
profile exactly). So at the committed configuration:

> **every admitted-isomorphism-covariant statistic is a function of the
> boundary's resolution profile together with the declared state's level data,
> and of nothing else** — hence every covariant statistic is
> **resolution-reading or state-reading**.

That is exactly the fingerprint dichotomy, and it repairs §7 without weakening
it: the covariant half of the corridor collapses onto resolution (killed by
gate 2 in the pin's own sense) or onto the state (killed by the amnesty sweep,
as C4a is and as my C5 would be). Stated this way the unit gets a *stronger*
result — the two theorems stop being independent and become one — and the false
sentence disappears.

### F6 — MINOR. §9's attribution of the family-level extension.

"Under the terminal cycle's own inherited successor constraint the impossibility
extends to the whole declared family at every committed law: no candidate
survives." The conclusion is right, the attribution is not: the inherited G1
kills only C1 and C4c (both measured anti-monotone by me). C4a is measured
non-monotone — type "neither" — and survives the inherited G1; it dies at G2b
and at the sweep. Reword to "under the inherited constraint C1 and C4c fall
too, and with C4a already dead at G2b and at the sweep, no candidate survives".

### F7 — CLEAN. Paper-vs-receipt, vocabulary, floats, determinism.

Receipt values match the paper exactly on my object: `L4-COV0`
{DET 24, FUNNEL 24, REV 24, FUNNEL-CLOSURE 24, COUNTER-LAW 1}; `L4-COV1`
{stabilizer 24, orbits 12}; `L4-COV2` distinct ✓ / related ✗; `L4-COV3` the
three printed shapes; `L4-COV4` empty. 45 gates, 16 anchors, 0 must-pass
failures, 15 gates before the barrier. The counter-law's
`orbit_invariant_is_the_shape_profile: False` in the receipt is honestly
rendered as "— (vacuous)" in the paper's table. No forbidden vocabulary: the
only hits for spacetime/locality/manifold/causal/gravity/QFT/QCD are inside the
two explicit non-claim sentences. No float on any substantive path (the single
float in the file is the progress-line timestamp, which does not enter the
receipt). Scope tags are present on the impossibility sentences — but see
"sentences to rewrite": the tags scope the *configuration*, and what needs
scoping here is the *reading of gate 2*.

---

## K1 ADJUDICATION

**The census — CONFIRMED, twice, independently.** I generated the 52 records
from restricted growth strings (Bell 1, 2, 5, 15, 52), rebuilt all five
declared laws from their definitions (3125 / 21 / 120 / 3006 / 120), computed
the stabilizer of (state, law setwise, preparation) by brute force over all 120
relabellings (24 / 24 / 24 / 24 / 1), and took orbits (12 / 12 / 12 / 12 / 52).
I then re-derived the census a **second** way with no group action at all: an
orbit is determined by `(s, μ)` where `s = |block(4)| − 1` and `μ` is the
multiset of the remaining block sizes, giving `Σ_s p(4−s) = 12`. The two routes
agree on all 2704 record pairs. The orbit-size census is
`[1,1,1,3,4,4,4,4,6,6,6,12]`, summing to 52 — a number the paper does not print
and which I offer as a check.

**"Covariance ⟹ factors through the orbit invariant" — CONFIRMED, trivially and
correctly.** A statistic invariant under a group is constant on its orbits;
since the admitted isomorphisms fix the state, the law setwise and the
preparation by construction, covariance at the committed configuration reduces
to invariance under the 24 relabellings of the boundary alone. Nothing in the
argument is stretched.

**"The orbit invariant IS the shape profile" — CONFIRMED, 2704/2704, at all
four symmetric laws.** Zero disagreements. There are exactly 12 distinct shape
profiles among the 52 records, so the shape invariant is *complete*.

**"The orbit invariant IS the RESOLUTION profile" — REFUTED.** 12 ≠ 7; five
splittings; the extra datum is the sink-block excess; the witness lives inside
the unit's own family (C4a) and I built a second, sharper one (C5). See F1, F2.

**The committed pairs — CONFIRMED.** Three distinct orbits, sizes **6, 3, 1**;
no admitted isomorphism carries any one to any other (checked over all ordered
pairs × 24 group elements); the three shapes are exactly the ones §7.4 prints.
And the paper's sharp reading of this — that covariance does *not* force them
equal and does *not* block separation — is right.

**Where the impossibility still bites, stated in the unit's favour.** All three
committed boundaries carry the sink in a singleton block (`s = 0`). Restricted
to that sector the shape profile *is* the block-size profile, so the extra
covariant datum is constant on the committed triple and **the application of
Theorem 7.2 to the committed pairs is untouched by F1**. The italic sentence is
true of the triple; it is false of the quotient it is asserted about.

---

## NUMBERS TABLE — 25 independent recomputations

| # | quantity | paper / receipt | R1's own route | ✓ |
|---|---|---|---|---|
| 1 | record-lattice sizes | 1, 2, 5, 15, 52 | 1, 2, 5, 15, 52 | ✓ |
| 2 | \|DET\|, \|FUNNEL\|, \|REV\| | 3125, 21, 120 | 3125, 21, 120 | ✓ |
| 3 | \|FUNNEL-CLOSURE\|, \|COUNTER-LAW\| | 3006, 120 | 3006, 120 | ✓ |
| 4 | admitted isomorphisms per law | 24,24,24,24,1 | 24,24,24,24,1 | ✓ |
| 5 | the 24-group is Sym{0,1,2,3} | asserted | verified elementwise | ✓ |
| 6 | orbits of the 52 records | 12,12,12,12,52 | 12,12,12,12,52 | ✓ |
| 7 | second route `Σ_s p(4−s)` | — | 12, agrees on 2704 pairs | new |
| 8 | orbit-size census | — | [1,1,1,3,4,4,4,4,6,6,6,12] = 52 | new |
| 9 | orbit ⟺ shape, 52×52 | "checked" | 2704 agree, **0** disagree | ✓ |
| 10 | distinct shape profiles | 12 (implied) | 12 | ✓ |
| 11 | committed triple orbit sizes | 6, 3, 1 | 6, 3, 1 | ✓ |
| 12 | related by an isomorphism | no | no | ✓ |
| 13 | the three shape profiles (§7.4) | as printed | identical multisets | ✓ |
| 14 | distinct **resolution** profiles | "the block-size profile" | **7**, not 12 | ✗ |
| 15 | resolution profiles that split | — | **5** (12 − 7) | new |
| 16 | uniform-state control | — | group 120, orbits **7** = resolution | new |
| 17 | distinct ε values; ε = (5−\|π\|)/16 | closed form | 5 values; holds at all 52 | ✓ |
| 18 | \|Pres_DET\| at the four boundaries | 240, 420, 1280, 120 | 240, 420, 1280, 120 | ✓ |
| 19 | ε at 2+1+1, 2+2, tomographic, one-atom | 1/16, 1/8, 3/16, 1/4 | identical | ✓ |
| 20 | C4c at the triple; total erasure | −2, −4, −12; −20 | identical | ✓ |
| 21 | C4a at the triple; total erasure | 1/4, 1/4, 0; 0 | identical | ✓ |
| 22 | C1 at FUNNEL / COUNTER-LAW | 14, 13, 23/2 / 95/8, 93/8, 45/4 | identical | ✓ |
| 23 | C1 constant at DET, REV, FUNNEL-CL. | yes | 1 value each | ✓ |
| 24 | ω vanishes over DET instances | 1612 | 1612, all zero | ✓ |
| 25 | G5 fixture evaluations before the barrier | 0 claimed | **864** (144/candidate) | ✗ |

Supplementary corridor rows measured by me at DET (paper's own gate names):

| candidate | G3 | mono type | G1 pin | G1 inherited | G2a | **G2 pin-wording** | G2b | G5 | separates | erasure |
|---|---|---|---|---|---|---|---|---|---|---|
| C4a | ✓ | neither | ✓ | ✓ | ✓ | **✓ passes** | ✗ | ✓ | ✓ | certifies |
| C4c | ✓ | anti-monotone | ✓ | ✗ | ✓ | ✗ | ✗ | ✓ | ✓ | certifies |
| **C5 (R1)** | ✓ | neither | ✓ | ✓ | ✓ | **✓ passes** | ✗ | ✓ | ✓ | **refuses** |

C1 per law, off-fixture, my routes: DET/REV/FUNNEL-CLOSURE constant (1 value);
FUNNEL 10 values, anti-monotone, G2a ✓, G2b ✗; COUNTER-LAW 25 values,
anti-monotone, G2a ✓, G2b ✓, G5 ✓ at group order **1**. Every per-candidate
claim of §4.2 reproduces.

---

## PER-RUNG CONFIRMATIONS

**(a) CLASS-IMPOSSIBILITY (the 12-orbit theorem) — CONFIRMED WITH CORRECTION.**
Census, factoring and the 52×52 identification are exact and reproduce twice.
The impossibility holds under G2b and is a tautology there; it **fails** under
the pin's gate 2, where the corridor at DET contains C4a and C5. Scope must be
restated as F1/F2 require.

**(b) The freeze discipline — CONFIRMED IN SUBSTANCE, CLAIM FALSE AS WORDED.**
Definitions hashed at `L4-00` before evaluation; gate order in the receipt is
as advertised (15 gates before the barrier); no verdict could have been tuned.
But 864 candidate-at-fixture evaluations occur inside G5 and the barrier's flag
mechanism cannot detect them (F3).

**(c) The per-candidate kills — CONFIRMED for everything I re-ran.** C1's five
per-law rows, C4a's and C4c's full corridor rows, C2's ε spectrum (1/16, 1/8,
3/16 with one-atom 1/4), C4b's collapse at DET (reachability classes trivial;
a function of ε). C3's 2847-law fan-in and the 745-patch side are R3's object
and I did not re-run them.

**(d) The amnesty sweep — CONFIRMED STRUCTURALLY, NOT EXHAUSTIVELY.** I did not
re-run the 4845-state sweep. I confirm the mechanism: my C5, built precisely to
survive everything else, inverts under a state relabelling (998, 996, 2988), and
C4a's level partition moves with the state exactly as §5 says. The claim that an
order-entailed separator cannot be inverted is correct and follows from the
chain (which I verify).

**(e) The C1 disqualification — CONFIRMED on my own routes.** C1 is degenerate
at DET, REV and the funnel closure; at FUNNEL it is nondegenerate but a function
of the shape (G2b fails); at the counter-law it is nondegenerate, anti-monotone,
G2a ✓, G2b ✓, and G5 ✓ **at group order 1**. The vacuous-covariance finding is
correct and is reported by the unit as a finding rather than absorbed, which is
the right call. C1's anti-monotonicity — hence its order-entailment — is
independently measured.

**(f) The fingerprint dichotomy — CONFIRMED, AND IT SURVIVED MY ATTACK.** I
built C5 specifically to be neither order-entailed nor obviously state-reading;
it is non-monotone in both directions, refuses total erasure, and still falls to
the state-reading arm. F5 shows why the dichotomy is not a pattern but a
theorem: at the committed configuration covariance forces resolution data plus
state level data, and those are precisely the two arms.

**(g) The corridor-hole adjudication — CONFIRMED, AND THE HOLE IS WIDER THAN
REPORTED.** §8.2's hole in gate 1 is real and honestly reported. There is a
second, undeclared hole in the *other* direction at gate 2: the delivered G2b is
strictly stronger than the pinned gate 2, and the emptiness result depends on
that strengthening (F2). Deviation 1 declares the two readings but not the fact
that the strong one excludes statistics the pin's wording admits.

---

## SENTENCES TO REWRITE

1. **§7.4** — "The committed configuration's own symmetry collapses the 52
   declared boundaries to 12 distinguishable ones, and the surviving invariant
   is the block-size profile." → *false as measured.* The block-size profile has
   7 classes. Replace: "…and the surviving invariant is the block-size profile
   **refined by the declared state's level classes** — 12 classes against the 7
   of the block-size profile alone, the difference being how many success
   addresses a boundary merges with the retained sink."

2. **Abstract** — "under them the 52 records fall into exactly 12 orbits …
   So every admitted-isomorphism-covariant statistic factors through the shape,
   **which is resolution data**". → replace the final clause with "…factors
   through the shape — resolution data **relative to the declared state's level
   partition**, strictly finer than the atom-size profile."

3. **Abstract and §7.4, the italic** — "*The only thing that distinguishes them
   covariantly is how much they resolve.*" → true of the committed triple, which
   carries the sink in a singleton at all three boundaries; false of the
   quotient. Restrict it: "*The only thing that distinguishes the three
   committed boundaries covariantly is how much they resolve.*"

4. **Abstract** — "corridor gate 2 and corridor gate 5 are jointly
   unsatisfiable: no candidate is both covariant and non-resolution at DET, as
   the theorem requires and as the family measures." → name the reading: "…
   corridor gate **G2b** and corridor gate 5 are jointly unsatisfiable … **G2b
   is strictly stronger than the pin's gate 2; under the pin's wording C4a is
   both covariant and non-resolution at DET**."

5. **§9, first bullet** — "no statistic of the declared patch data is both
   covariant and non-resolution (Theorem 7.2)" → "…both covariant and a
   non-function of the level-refined shape profile", with the same declaration
   of the strengthening, and a scope tag on the *reading of gate 2*, not only on
   the configuration.

6. **Theorem 7.2 (ii)** — "*f is not a function of the boundary's resolution
   profile*" → "*f is not a function of the boundary's shape profile (the atom
   sizes refined by the declared state's level classes)*". As written the
   theorem is false: `f(P) = |block(sink)| − 1` is covariant and is not a
   function of the resolution profile.

7. **§3(3) and the abstract's freeze paragraph** — "a freeze-barrier gate
   certifies from recorded per-gate provenance flags that no corridor gate
   evaluated any candidate at any committed boundary" / "Every gate carries a
   provenance flag recording whether any committed boundary had been evaluated
   when it fired." → false. The covariance gate must leave the off-fixture set,
   because the orbits of the forged 2+1+1 and 2+2 boundaries meet it. Replace
   with the true claim and add it as **Deviation 12**: "the covariance gate
   evaluates each candidate at the orbit images of off-fixture records, 36 of
   which per symmetric law are the committed forged boundaries (864 in all);
   each such value is equality-tested against its own off-fixture partner, none
   is retained, compared to a threshold, or used in any selection. The barrier's
   flag records explicit fixture *reads*, not orbit-image evaluations."

8. **§9, `RQ0-L4-CLASS-IMPOSSIBILITY` bullet** — add F5's repair, which costs
   nothing and gains a theorem: "every covariant statistic is a function of the
   resolution profile together with the declared state's level data; hence
   covariance implies resolution-reading or state-reading, which is the
   dichotomy of §8 — Theorems 7.2 and 8.1 are one theorem." (The uniform-state
   control makes this checkable: at ρ uniform the group is 120, there are 7
   orbits, and the orbit invariant is exactly the block-size profile.)

9. **§9, third-from-last sentence** — reword the attribution as F6 says.

---

## WHAT I DID NOT TEST

C3's 2847-law population and the 874/175/428 census; the 745 identity-free
patches and G6; the 4845-state amnesty sweep; the 21 mutants; the anchors'
verbatim string matches (A14, A16); byte-identical determinism. Those are R3's
object under K4 and R2's under K2/K3. My C5 is offered as a counterexample to
Theorem 7.2's clause (ii) under the plain reading and to the emptiness claim
under the pin's gate 2 — **it is not offered as a surviving candidate of the
hunt**: I did not clear it against G6, and it is killed by the amnesty sweep on
the mechanism I measured.

---

*R1, operator lens. Own exact code, no float, nothing imported from the unit,
no child agents, no git mutation, one repo file written. FROZEN ON DELIVERY.*

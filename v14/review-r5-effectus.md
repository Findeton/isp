# R5 — HOSTILE REVIEW, EFFECTUS LENS (MEANING / SCOPE / MOTIVATION)

**Unit:** R5, the gauge rung — `v14/paper-18-gauge-rung.md`.
**Protocol:** `v14/note-r5-hostile-protocol.md` (`16f86f0eabd2`), K4 decisive.
**Pin:** `v14/note-r5-gauge-pin.md` (`b53adba0eee0`), G1–G7 + the must-nots.
**Lens:** what the measured objects are entitled to mean.

**Hashes re-verified at the start and the end of this review (sha256-12, the
corpus convention):**

| artifact | expected | measured |
|---|---|---|
| `v14/paper-18-gauge-rung.md` | `3800959353b4` | `3800959353b4` ✓ |
| `v14/code/r5_gauge_exact.py` | `37c232de91a6` | `37c232de91a6` ✓ |
| `v14/code/r5_gauge_output.txt` | `e86be9a581a7` | `e86be9a581a7` ✓ |
| `v14/code/r5_gauge_receipt.json` | `1c072956ac7b` | `1c072956ac7b` ✓ |
| `v14/note-r5-gauge-pin.md` | `b53adba0eee0` | `b53adba0eee0` ✓ |
| `v14/note-r5-hostile-protocol.md` | `16f86f0eabd2` | `16f86f0eabd2` ✓ |
| `v14/paper-08-tower-four-wings.md` (CR-D prior) | `602c9ac2ccc4` | `602c9ac2ccc4` ✓ |

Commit `a504243` verified; the working tree is byte-identical to the commit for
all four delivered artifacts. No drift. (The protocol's hashes are sha256 prefixes,
not git blob ids; six-for-six they verify under that convention.)

**Grade: ACCEPT-WITH-FIXES.**

**Recomputations: 178 delivered quantities independently reproduced, 176 exact
matches and 2 findings**, in an independent reimplementation that shares nothing
with the delivery: permutation machinery written from the paper's stated
definition of `W_p`, and Q(ζ₈) rebuilt as 4-tuples of `Fraction`s over
(1, i, √2, i√2) rather than the delivery's integer 5-tuples over
(1, z, z², z³). Heavy blocks inside that count: 4,000 random-permutation trials
of the family-covariance identity with a symbolic coin; 7,200 exact coin pairs
against the single-path lemma; three separate 640-coin censuses; 112 exhaustive
7-subsets for the rank; 21 scramble cells; 24 ladder cells at two lattice sizes.

**The arithmetic is clean.** Every number the paper prints that I could reach, I
reproduced exactly — the 25-element alphabet, 640 coins, the 64/64/512 sector
split, 632 non-flat, 576/640 non-commuting, the whole local ladder
(3, 60, 9, 9, 2520, 20160) at **both** lattice sizes, A₁₆ at order
10,461,394,944,000 and A₆₄, rank 8, all 21 scramble cells, 0-of-1920, 576, 384,
the four plaquette rows, 512-of-512 trace non-integrality, 58 circulants,
0-of-3364, 0-of-52, 4096-of-4096, 120 states, 0-of-18, and all 35 receipt totals.
**In the one place where my numbers and the delivery's disagreed, the delivery was
right and my instrument was wrong** — recorded in §0 below, because a reviewer who
does not publish his own misses has not run a hostile review.

Every finding below is about **meaning**: what the reproduced numbers are
entitled to assert. Two of them (M1, M2) also bear on whether the instrument
enforces what the paper says it enforces.

---

## 0. The reviewer's own miss, recorded first

My first pass at the scramble table disagreed with the delivery in 4 of 21 cells
(S2-EDGE/SCR-TRANSPOSE 360 vs 720; S2-CORNER/SCR-TRANSPOSE 840 vs 5040;
S3-ROW/SCR-TRANSPOSE 20160 vs 40320; S4-BLOCK/SCR-DIRECTION-FLIP 26611200 vs
239500800). The cause was a defect in **my** hand-rolled Schreier–Sims, which
silently under-counts on groups that are not alternating; it happened to be
correct on every alternating case, which is why the physical column agreed. Brute-force
closure reproduced the delivery exactly in all 7 cells I could enumerate, and
Jordan certification handled the rest. **The delivered scramble table is correct
in all 21 cells.** I then re-derived every group order in this review by a route
that does not use my Schreier–Sims: brute-force closure where the order permits,
and otherwise Jordan's theorem (primitive + a prime-length cycle fixing ≥ 3 points
+ every generator even ⇒ the alternating group on the support).

This is worth one further sentence for the ledger: the delivery's certification
route (containment in ∏Alt(orbit) plus equality of orders) and my route (Jordan)
are genuinely independent, and they agree on every finite class the unit reports.
The isomorphism-class claims are as solid as this corpus's standards require.

---

## 1. MAJOR — M1. The paper's quoted verdict is not the verdict the instrument emits

The paper introduces its centrepiece with:

> **The verdict, quoted exactly as the instrument emits it.**

It is not. Segment-wise diff of `paper-18` line 62 against
`r5_gauge_output.txt` line 21 (both one line; the receipt's `/verdict/string`
agrees with the output, not the paper):

| segment | paper | instrument (output **and** receipt) |
|---|---|---|
| `DECLARED-GATE=` | `FAMILY-COVARIANCE-512-OF-512-CHECKS` | `FAMILY-COVARIANCE-4096-OF-4096-CHECKS` |
| `TWO-EXCITATION=` | `EXCLUSIVITY-SURVIVES-0-OF-9-BOTH` | `EXCLUSIVITY-SURVIVES-0-OF-18-BOTH` |

Two false numbers in the delivered paper's verdict block, in a corpus whose
standing meta-record is *zero false numerical results*. The paper's own prose is
**correct** in both places — §4 says "`4096 of the 4096 checks`" and §5 says
"`0 of 18` rows carry both" — so this is a transcription defect in the single
most load-bearing object of the unit, not a measurement error. The measured
physics is unaffected.

**Why it survived: the verdict block is entirely ungated.** `paper_claims(R)`
(instrument §12) renders 48 claim strings that must occur in the paper; the
emitted verdict string is not among them. The numeral-coverage gate then asks
only that every numeral *in* the paper be rendered somewhere by *some* receipt
field — and `512` (balanced coins) and `9` (file-bytes anchors) both are. So the
substitution is invisible. I confirmed this by running the delivery's own
`--verify-paper` (which exits before any write, so this is read-only) on the
committed paper and on five scratch mutants:

| paper under test | result |
|---|---|
| committed paper (carries `512-OF-512`, `0-OF-9`) | **EXIT 0, all three paper gates pass** |
| verdict repaired to `4096-OF-4096`, `0-OF-18` | EXIT 0 (gate cannot tell them apart) |
| verdict falsified to `GLOBAL-A16-TO-A16` | EXIT 0 |
| verdict falsified to `SEPARATES-GLOBAL-2-OF-2` | EXIT 0 |
| verdict ladder falsified to top at `A16` | EXIT 0 |
| `;NO-CONFINEMENT-CLAIM` deleted from the scope segment | EXIT 0 |

For contrast, breaking a *gated* prose claim does fire: replacing §4's
"`4096 of the 4096 checks`" with "512 of the 512" dies at `G-PAPER-CLAIMS ::
missing ['covariance']`. The mechanism works; the verdict block simply is not
wired into it.

**Exact repair (two edits + one gate).**

1. In `v14/paper-18-gauge-rung.md` line 62, replace
   `DECLARED-GATE=FAMILY-COVARIANCE-512-OF-512-CHECKS` with
   `DECLARED-GATE=FAMILY-COVARIANCE-4096-OF-4096-CHECKS`, and
   `TWO-EXCITATION=EXCLUSIVITY-SURVIVES-0-OF-9-BOTH` with
   `TWO-EXCITATION=EXCLUSIVITY-SURVIVES-0-OF-18-BOTH`.
2. In `paper_claims`, add one entry:
   `cl["verdict"] = R["verdict"]["string"]`.
   The whitespace-normalising comparison already in `G-PAPER-CLAIMS` then binds
   the paper's copy of the verdict to the emitted one, character for character;
   the verdict is one line in the paper, so no wrapping issue arises. I verified
   the mechanism fires on a broken claim, so this repair is sound as written.
3. Declare a mutant `MUT-PAPER-VERDICT` that perturbs one character of the
   paper-side verdict and dies at `G-PAPER-CLAIMS`, so the new gate carries its
   own falsifier under #34.

This is a first-class finding but a cheap fix, and it does not touch a single
measured quantity.

---

## 2. MAJOR — M2. The DECLARED gate is a forced identity, not a measurement

This is the finding with the most consequence for what R5 may claim, and for what
the coupling unit may inherit.

The head law (`derive_head`) branches on `declared_gate_admits`:

```
if c["declared_gate_admits"] == 0: return "R5-BLOCKED-AT-THE-GATE"
```

and `declared_gate_admits = family_covariance_checks − family_covariance_failures`.
The unit therefore rests its head on the family-covariance check. §4 presents that
check as measured — "it is measured here, over the extension of order 128 acting
on the link set, at `4096 of the 4096 checks`" — and the gate text says "it is
measured here, not assumed".

**It is assumed.** The check compares `conj_by_perm(link_op(ℓ,U), π)` against
`link_op(π(ℓ), U or XUX)`. That is an identity of how conjugation by a permutation
matrix acts on a matrix supported on two coordinates: it holds for **every** site
permutation and **every** 2×2 coin, whether or not the permutation is a chart
element and whether or not the coin is in the derived alphabet. I verified this on
4,000 random permutations of the 16 sites (essentially none of them chart
elements) with a fully **symbolic** coin (u₀₀,u₀₁,u₁₀,u₁₁ as uninterpreted
symbols): **0 failures**, and the reversed-storage form
`link_op(b′,a′,XUX) = link_op(a′,b′,U)` is a literal identity of the same kind.
The check cannot fail on any arena of link-indexed operators whatever.

Two aggravations. First, the sweep is run at one coin, `ANTI-X` = X, which is its
own swap conjugate — so even the orientation half of the identity is trivialised.
Second, the declared mutant `MUT-FAMILY-COVARIANCE` falsifies the gate by
`fails2 += 1`, i.e. by injecting a failure into the counter rather than by
perturbing the mathematics. The mutant proves the gate is wired; it cannot prove
the gate discriminates, because nothing discriminates.

The only substantive content in that block is the *other* conjunct — `fails == 0`,
the link set being closed under all 5120 chart actions. That is a real (if easy)
property of the arena and should carry the segment.

**The consequence for meaning.** R4's per-generator criterion admits **0 of 52**
here; the replacement admits **4096 of 4096** by identity. So this arena has **no
effective realization gate at all**: one criterion is empty, the other is vacuous,
and neither selects. `R5-NON-ABELIAN` is therefore **not a gate-selected verdict**;
it is the unselected arena's census. That is not a defect in the physics — the pin's
G2 explicitly mandated re-derivation — but it must be said, because the natural
misreading is that the family-level criterion *licensed* the non-abelian family,
and it did no such thing.

**Exact repair.** Apply the paper's own §6 standard, which is already correct
there ("the Wilson trace is invariant under any conjugation whatever, by
cyclicity, so its invariance at every checked loop is a disclosure and not a
measurement"). In §4, replace "and it is measured here, not assumed" with a
forcing disclosure:

> Family covariance is **forced**: conjugating an operator supported on two sites
> by any site permutation returns the same operator on the image sites, with the
> coin swap-conjugated exactly when the endpoints exchange. The 4096 checks are a
> disclosure, not a measurement. What *is* measured beside them is that the link
> set is closed under all 5120 chart actions, with 0 failures — that is the
> arena-dependent half, and it is the half the segment carries.

and change the head segment to
`DECLARED-GATE=FAMILY-COVARIANCE-FORCED(LINK-SET-CLOSED-5120-OF-5120)`.
Register the forcing under #34 alongside the three existing waivers, so the gate
census becomes 57 carrying an injection falsifier + 4 carrying a registered
forcing, still 61 in all.

---

## 3. MAJOR — M3. `LOCAL-STABLE-6-OF-6` is forced by non-wrapping, and two
pre-registered outcomes were unreachable

G6 is the charter's own question — does the class survive one refinement step. The
delivered answer is `LOCAL-STABLE-GLOBAL-EXTENSIVE`, with 6 of 6 local stencils
identical at L = 4 and L = 8.

I reproduced the table exactly. I then asked what it measures. **None of the six
declared stencils wraps at L = 4:**

| stencil | max unwrapped corner | wraps at L=4 | generator maps identical at L=4 and L=8 |
|---|---|---|---|
| S1-ONE | (1,1) | no | yes |
| S2-EDGE | (2,1) | no | yes |
| S2-CORNER | (2,2) | no | yes |
| S2-APART | (3,1) | no | yes |
| S3-ROW | (3,1) | no | yes |
| S4-BLOCK | (2,2) | no | yes |

The plaquette holonomy with the swap coin is the 3-cycle (B D C) on the plaquette's
own corners; for a patch that does not wrap, the generators at L = 4 and at L = 8
are **literally the same maps** on the same relative coordinates. The two groups
are equal by relabelling. So "the class is identical at the two sizes at 6 of 6
declared local stencils" is a theorem about local patches being local, not a
measurement about refinement. It could not have come out otherwise at any L ≥ 4.

That propagates to the head law. Of the four pre-registered outcomes:

| outcome | branch condition | status on this arena |
|---|---|---|
| `R5-BLOCKED-AT-THE-GATE` | `declared_gate_admits == 0` | **unreachable** — forced to 4096 (M2) |
| `R5-NO-STABLE-GROUP` | `local_stable == 0` | **unreachable** — forced to 6 (this finding) |
| `R5-BLOCKED-AT-THE-COMMUTATOR-SUBGROUP` | `noncommuting_configs == 0` | genuinely reachable (measured 576; 0 if the alphabet had been diagonal-only) |
| `R5-BLOCKED-AT-THE-SCRAMBLE-CONTROL` | `separating_stencils == 0` | genuinely reachable (measured 12) |

§1 is headed "**What would have answered the other way**" and says all four
outcomes "are reachable by the one head law, demonstrated on synthetic censuses
inside a gate". The parenthetical *is* honest — the demonstration is synthetic —
but the section title claims falsifiability that two of the four did not have on
this arena. The unit's real falsifiability lives in the commutator census and the
scramble control, and those are strong.

**Exact repair.** In §7, add after the refinement table:

> The local half of this result is forced and is reported as such: none of the six
> declared stencils wraps at L = 4, so their generators are the same maps at both
> sizes and their classes agree by relabelling. What the refinement step measures
> is the global stencil alone.

In §1, retitle to "What could have answered the other way, and what could not",
and name the two branches that were unreachable once the gate and the stencils
were declared. Change the head's refinement segment per M4 below.

---

## 4. MAJOR — M4. `GLOBAL-A16-TO-A64` is entered in the head at the grain where G7 fails

G7 in the pin is unconditional: *the holonomy group must SEPARATE the physical case
from a scrambled control **before any group-theoretic claim is entered**.*

Measured, and reproduced by me in all 21 cells: the local profile separates the
physical connection from both scrambles at 12 of 12 stencil-scramble pairs; the
global class separates at **0 of 2** — both scrambles reach the whole of A₁₆, as
does the physical connection. I confirmed all three global cells independently
(every generator is a product of four transpositions, hence even, so G ≤ A₁₆;
primitivity plus a prime-length cycle fixing ≥ 3 points gives G ⊇ A₁₆).

The paper's defence is real but partial. It is true that the **CLASS** segment
carries only the local ladder, and §7 says so explicitly and well. But the
**REFINEMENT** segment still names two isomorphism classes —
`GLOBAL-A16-TO-A64` — and an isomorphism class in a verdict string is a
group-theoretic claim. The disclosure that it does not discriminate lives two
segments away, in `SCRAMBLE=...;FAILS-GLOBAL-0-OF-2`. Under the corpus's own
declared-arena discipline (RUNBOOK §15, "match every coordinate"), a segment has
to be readable on its own coordinates; a reader who quotes the REFINEMENT segment
alone quotes a non-discriminating measurement as a finding.

**Exact repair.** Mark it in the segment that carries it:

`REFINEMENT=LOCAL-STABLE-BY-NON-WRAPPING-6-OF-6;GLOBAL-SUPPORT-IS-THE-VOLUME(A16-TO-A64-NOT-SCRAMBLE-SEPARATED)`

That one edit discharges both M3 and M4 in the head.

---

## 5. MAJOR — M5. The must-nots: compliant paper, blind gate, one over-reaching successor

**The sweep.** I swept the paper for all three must-nots.

- *No confinement-analog claim.* The delivered paper is **compliant**. Every
  occurrence is either the scope token `NO-CONFINEMENT-CLAIM`, or §8's explicit
  negative ("No confinement-analog claim is entered anywhere… the objects that
  would carry such a claim — an area law, a static potential, a large-N limit —
  are absent from this arena entirely"), which is exemplary, or §10's successor
  item discussed below. The pin forbids the language *before G1 passes*; G1 passed.
- *No curvature ⇒ quantum.* Compliant and gated in substance: §5 states the
  implication negative in both directions, with `G-CURVATURE-DOES-NOT-IMPLY-QUANTUM`
  requiring curvature-without-defect rows in numbers (576 at link grain, 704 at
  plaquette grain) and R4's 588-at-zero-curvature supplying the converse.
- *No matrix-valued holonomy as physics.* Compliant. `G-NO-MATRIX-AS-PHYSICS`
  constrains the published holonomy rows to a declared key set and a row carrying
  a matrix dies. Wording only: §3's "no matrix enters the receipt" is literally
  false — the six named coins are in the receipt as 2×2 field matrices
  (`/named_coins/*`), correctly, as declared inputs. Scope the sentence to
  holonomies (MINOR m4).
- *No silent inheritance of the maximal-transport gate.* Not silent — §4 is the
  opposite of silent, and it is the best section in the paper. See M2 for what the
  replacement is worth.

**The gate is blind to the paper.** `G-NO-CONFINEMENT-LANGUAGE` checks
`"NO-CONFINEMENT-CLAIM" in string` and that no instrument-rendered claim contains
"confinement" — i.e. it sweeps the *instrument's own output*, never the paper's
prose. I proved this by injecting into the paper a paragraph asserting an area
law, positive string tension, a linear static quark potential, confinement on the
record stage, and a flux tube; `--verify-paper` returned **EXIT 0, all three paper
gates passed**. §8's claim that no confinement-analog claim is entered "in the
verdict or in the prose" is enforced for the verdict half only; the prose half is
author discipline. It held here — but it is not gated, and the paper says it is.

**Repair:** extend `G-NO-CONFINEMENT-LANGUAGE` to sweep the paper text for a
declared vocabulary (`confinement`, `area law`, `string tension`, `flux tube`,
`static potential`, `quark`, `large-N`), permitting occurrences only inside a
declared negative-context window — the same window mechanism `paper_polarity`
already implements at 64 characters. Give it a mutant.

**The one over-reach: §10's area-law successor.** It reads:

> **The area law.** With a non-abelian holonomy measured and a scramble control
> that separates locally, the objects a confinement analog would need can now be
> posed. They are not posed here.

"Can now be posed" is not supported, on this unit's own measurements:

1. An area law is an expectation of a Wilson loop under a **measure on
   configurations**. This arena has no measure, no action and no coupling; it
   sweeps 640 uniform configurations out of 640³² and the non-uniform census is
   the unit's own leading open problem. There is nothing to take an expectation
   over.
2. An area law is a **large-loop** statement. The unit's own G7 result is that at
   the global grain the group statistic does **not** separate the physical
   connection from a scramble (0 of 2). Precisely at the scale where an area law
   would live, this instrument is measured to be non-discriminating. The sentence
   cites the local separation as support for a global object; that is the wrong
   grain, and the paper elsewhere is scrupulous about grain.
3. No continuum limit, no N, no matter fields, and — per M3 — one refinement step
   whose local half is forced.

**Repair.** Replace with the honest form:

> **The area law, and what stands between.** A confinement analog would need three
> objects this arena does not have: a measure on configurations (only the uniform
> ones are swept), a family of loops whose size can grow (the global grain is the
> one where the scramble control does *not* separate, 0 of 2), and a coupling to
> vary. Naming them is not posing them, and none is posed here.

---

## 6. The two verdicts, one string: they compose

`R5-NON-ABELIAN` and `R5-BLOCKED-AT-THE-GATE-AT-THAT-READING` sit in the same
string. They **compose coherently**, and the composition is pin-sanctioned:

- They are indexed to two different **readings of one gate**, not two answers to
  one question. Read per generator, the inherited criterion admits 0 of 52; read
  at the family level, it admits everything. Both are stated, and the head keys on
  the declared one.
- G2 did not merely permit the re-derivation, it **required** it: "the
  realization-census gate may NOT be inherited unmodified". Declaring a new gate is
  compliance, not goalpost-moving. The suffix `-AT-THAT-READING` is exactly the
  right device and should be kept.
- The pin's trigger for a first-class `R5-BLOCKED-AT-THE-GATE` was "if the maximal
  level again selects a **commuting sub-family**". That is not what happened. The
  maximal level selects *nothing*: the admissible set is **empty**, not commuting.
  Vacuity is a different and stronger outcome than the pin anticipated, and §4 gets
  this right when it says the gate "empties the family outright".

So: no contradiction. But the composition is **weaker than it reads**, because of
M2 — the reading that carries the head is a tautology, so the string is not
"blocked under one gate, licensed under another"; it is "blocked under the only
gate that could have selected, and unselected under a criterion that selects
nothing".

**What the gate-emptiness means for the programme's instrument lineage (G2).**
This is the unit's most transferable result and the paper is right to call it "a
real result about the programme's own gate rather than about this arena". I would
strengthen it, because the mechanism generalises further than §4 claims:

> A link-indexed family has no translation-invariant generators, ever: conjugating
> a link operator by a translation moves the link, so the stabiliser is trivial for
> every non-identity coin. R4's per-generator realization criterion is therefore
> empty on **any** arena whose generators carry a location — not merely on this
> one. Where the criterion has bitten before, it bit on objects that were already
> location-free. That is a statement about the criterion's domain of applicability,
> and it is the question the corpus should now put to the earlier units' transport
> numbers.

The paper's §10 item "The gate, at the programme level" already poses this; the
generalisation above is what it should say.

---

## 7. The exclusion theorem: the licensed sentence

I verified the single-path lemma three ways: by re-deriving the counting argument
over all nine coin-support-pattern pairs at all three link relations and all four
plaquette relations (31 cases); by exact Q(ζ₈) evaluation of Δᴮ on 7,200 ordered
coin pairs at SHARE-ONE-SITE and DISJOINT (0 nonzero); and by reproducing the
seed's Hadamard witness, which returns the half-and-minus-half matrix exactly.
The theorem and its proof are **correct**, and the proof's scope is wider than the
paper states.

**The mechanism is support overlap, and it explains both grains at once.** The
maximum number of intermediate paths i → k → j between a pair of endpoints, as a
function of how many sites the two operators' supports share:

| overlap | max paths | consequence |
|---|---|---|
| 0 sites | 1 | no defect; operators commute |
| 1 site | 1 | no defect; **this is the only overlap at which two link operators fail to commute** |
| 2 sites | 2 | defect possible **and** non-commutation possible |
| 4 sites | 4 | defect possible; a holonomy commutes with itself, so no curvature |

Every cell of both delivered tables follows from that one column, including the
plaquette table's structure (DISJOINT → neither; SHARE-A-CORNER, overlap 1 →
curvature only, 512; SHARE-AN-EDGE, overlap 2 → all four cells, 384 both;
SAME-PLAQUETTE, overlap 4 → defect only, 512). **The two grains are not opposite
statements and do not need reconciling as such** — the paper's "the grain is a
declared coordinate of the result" is true but under-explains, and §10's open
question "what is the largest support at which the lemma still holds" is already
answered by its own proof.

**The licensed sentence, for the paper to carry:**

> A nonzero composition defect needs two composition paths between one pair of
> endpoints; a nonzero commutator of link operators needs their supports to meet in
> exactly one site; and one shared site admits exactly one path. So at the grain of
> the generators the two cannot occur together — for every coin alphabet, not only
> this one, and in the declared two-excitation sector as well as the single-excitation
> one. The exclusion is a theorem about **support overlap**, and it fails as soon as
> two objects overlap in two sites: plaquette holonomies sharing an edge do, and
> there both occur, in 384 rows. The statement is about two-site generators, not
> about quantum character and geometry in general.

**Over-readings to kill.** "Where the quantum lives, the geometry never closes" is
**not licensed**, on three counts: (i) at plaquette grain they demonstrably coexist,
384 rows; (ii) the exclusion is a combinatorial fact about the support of two-site
operators, with no quantum content on either side — the same count holds for any
2×2 blocks whatever; (iii) it fails even as a sector statement at coin
granularity, per §8 below. The weaker and true form is the boxed sentence above.

**On the infinite-order sector.** I confirmed 512 of 512 balanced coins have a
plaquette-holonomy trace that is not an algebraic integer (so no power is the
identity), and that the diagonal and antidiagonal traces *are* algebraic integers.
The certification route is sound and is a genuine theorem rather than a search cap.
§3's headline sentence, however, over-reaches at coin granularity:

> The sector that carries the composition defect is exactly the sector whose
> holonomy group is infinite…

I measured which coins actually carry a defect at SAME-LINK: **384 of 640, and all
384 are balanced** — so 128 of the 512 infinite-holonomy coins carry **no** defect.
The implication runs one way only.

**Licensed:** *defect ⇒ infinite-order holonomy* (every defect-carrying coin lies
in the balanced sector, and every balanced coin's holonomy has infinite order),
and *finite alternating class ⇒ no defect*. **Not licensed:** the converse, or any
biconditional reading of "exactly". **Repair:** change "exactly the sector" to
"contained in the sector", and add the number: "384 of the 512 balanced coins carry
the defect; the other 128 do not, so the containment is strict."

---

## 8. The CR-D convergence: form, not preference

Verified against the pinned prior (`v14/paper-08-tower-four-wings.md`,
`602c9ac2ccc4` ✓): CR-D reports A₅ on 5 labels, A₁₁ on 11, A₁₅ on 15, each named
verbatim "the FULL alternating group on its own support". R5 returns the same
**form**. The form match is real and is stated verbatim in both units. It is not
numerology.

But the paper's conclusion — "**The alternating-family prior is confirmed on the
gauge rung**" — reads as independent corroboration of a theory-level preference,
and that is not what was measured. The paper itself supplies the reason, in §3:

> with the swap coin the holonomy of a single plaquette is a **three-cycle**… and
> three-cycles whose supports overlap generate the alternating group on the union.

That is Jordan's theorem, and it is why my own certification route worked at every
stencil. A construction whose generators are 3-cycles on overlapping supports
**must** produce the full alternating group; it has no other option. CR-D's
mechanism is the same species — paper-08 derives its groups from wing
transpositions with an evenness lemma, then certifies by containment-plus-order.
Two constructions that both generate even permutations of small overlapping
support agree on the alternating family the way two constructions that both
generate rotations agree on SO(2).

Two further calibrations:

- **A₅ and A₇ carry no independent weight.** Once the shared form is granted, the
  specific groups follow from the support cardinality alone: R5's S2-EDGE has
  support 5, so A₅; S3-ROW has support 7, so A₇. Presenting them as two additional
  corroborations ("with CR-D's own A₅ reappearing… and A₇… appearing here")
  double-counts the form match.
- **G7 argues directly against the family reading.** Both scrambles also reach
  A₁₆. A statistic that a deliberately scrambled connection satisfies just as well
  is not evidence of a structural preference at that grain.

**Licensed sentence:**

> Two units of this corpus, built on different arenas by different routes, return
> the full alternating group on their own supports. In both the generators are even
> permutations of small, overlapping support, and by a classical theorem that
> forces the alternating group. The convergence is therefore evidence about the
> **generator type the two constructions share**, not evidence that the theory
> prefers the alternating family; and at the global grain the same class is reached
> by a scrambled control, so at that grain it discriminates nothing.

**Not licensed:** "the alternating-family prior is confirmed", full stop.
**Also fix (m6):** §7 says "A₇, which CR-D's ladder tops out at". CR-D's four-wing
**tower** tops out at A₁₅; A₇ tops the three-wing **ladder**
(1 < A₄ < GL(3,2) < A₆ < A₇). The sentence is defensible in paper-08's own
vocabulary but sits one line after "CR-D's tower reported… A₁₅ on fifteen".
Disambiguate to "the three-wing ladder".

---

## 9. "The QCD shape": what R5 may say at citable scope

The protocol asks where exactly the line is. Enumerating the candidate readings of
`R5-NON-ABELIAN`, calibrated:

| candidate reading | verdict |
|---|---|
| "The record stage carries a non-abelian gauge structure" | **over-read.** There is no gauge *field* here — no action, no coupling, no dynamics, no matter. |
| "The programme has reached QCD's shape" | **refuted by the unit itself.** Non-abelian holonomy is necessary for a Yang–Mills analogy and nowhere near sufficient. The group here is a finite alternating permutation group on lattice sites, not a compact Lie group; there is no colour space, no representation theory, no continuum. |
| "A non-abelian holonomy group exists on the declared stage" | **licensed**, at the declared scope, and this is the strongest available. |
| "Curvature couples to Δᴮ" | **refuted:** `CURVATURE-DEFECT-INDEPENDENT`, with witnesses in both directions and a theorem in one. |
| "The holonomy group is stable under refinement" | **licensed only for the global support law**, and only trivially for the local stencils (M3). |
| "The theory prefers the alternating family" | **not licensed** (§8). |

**The licensed head sentence, for the paper and for anything that cites it:**

> On the L = 4 record stage, with a coin per link drawn from the alphabet derived
> from R4's 25 coefficients, and over the 640 uniform configurations swept
> exhaustively, the declaration-connection carries a **non-abelian** plaquette
> holonomy: the commutator subgroup is non-trivial at 576 of 640 coins, on an arena
> whose provably flat control returns the trivial group at 0 of 3364. Where the
> holonomy group is finite it is the full alternating group on its own support,
> certified by set equality and reported as an isomorphism class with an
> arena-relative rank; on the interfering sector it is infinite by a theorem about
> traces. **This is a non-abelian holonomy on a finite record lattice. It is not a
> gauge field, it is not QCD, and no confinement-analog object exists on this
> arena.** The uniform-configuration restriction is a declared window and the
> general object — coins varying link to link — is not swept.

Where exactly is the line: **at the word "field"**. R5 has a *connection* in the
holonomy sense (an assignment of unitaries to links and an ordered product around a
loop). It has no field, because it has no configuration measure, no action
functional and no dynamics for the link variables. Everything on the far side of
that word — coupling, running, area laws, confinement, continuum, spectra — remains
untouched, and the paper's §8 "Not decided" list is honest about all of it except
the area law (M5).

---

## 10. G5 declaration segments: audit

The pin requires CONNECTIVE, LINK-SET/STENCIL, SECTOR, SWEPT-RANGE and
INDIVISIBILITY as explicit segments, and that *any quantity not gated invariant
across the declared free axes be entered arena-relative or not at all*.

**First clause: passes.** All five segments are present in the head, plus the
`NON-UNIFORM-CONFIGURATIONS=NOT-SWEPT` disclosure, and `G-DECLARATION-SEGMENTS`
checks their presence. `INDIVISIBILITY=DECLARED-BY-DIVISION-EVENT-TIMES` correctly
says *declared*, never measured. The connective is inherited verbatim with its
forcing named. This is well done.

**Second clause: partially unenforced.** `G-DECLARATION-SEGMENTS` checks only that
the segment *labels* occur in the string; nothing gates invariance across the free
axes. Taking the free axes in turn:

| free axis | varied? | quantity depending on it | entered arena-relative? |
|---|---|---|---|
| the 6 plaquette stencils | yes, all 6 | CLASS, RANK | yes — the ladder is stencil-indexed and RANK says `ARENA-RELATIVE` |
| the 3 gauge handles | yes, all 3 | the untraced-holonomy moves | yes, §6 reports per handle |
| the two-excitation extension | **no** — Λ² run, Sym² not | `TWO-EXCITATION=EXCLUSIVITY-SURVIVES` | disclosed in §5, **absent from the head segment** |
| the division-event times | **no** — one value | the whole G3 matched table | only via `INDIVISIBILITY=` in SCOPE |
| the leg at the cut | **no** — one value | the whole G3 matched table | not marked |

The RANK's explicit `ARENA-RELATIVE` tag is exactly right and is the model the
other segments should follow. Two repairs:

- The two-excitation gap closes by **argument**, not by spending a run: the
  single-path count is a statement about how many intermediate states connect a
  pair of endpoints, and the symmetric square admits no more of them than the
  exterior square. Add one sentence to §5 saying the result is independent of which
  square is taken, and the fibre-2 choice stops being load-bearing.
- The division-event times and the leg at the cut are genuinely un-varied. Either
  vary them once, or mark the segment
  `CURVATURE-DEFECT=...(AT-DECLARED-DIVISION-TIMES-AND-LEG)`. The second is cheap
  and honest.

---

## 11. The choice inventory at the RSQ standard

15 entries, each classed with a fibre, gated at `G-CHOICE-INVENTORY`. Two problems.

**(a) The "fibre" column is not one quantity.** It means at least three different
things:

| entry | fibre | what the number actually is |
|---|---|---|
| the two-excitation extension | 2 | cardinality of the admissible alternatives (Λ² or Sym²) — the intended meaning |
| the global phase | 8 | size of a stabiliser |
| the loop base point and orientation | 4 | size of a stabiliser |
| the plaquette stencils | 6 | **count of declared instances** — there are vastly more than 6 possible stencils |
| the gauge handles | 3 | **count of declared instances** |
| the division-event times | 1 | a free choice with fibre 1 is a contradiction in terms |
| the leg at the cut | 1 | likewise |

Under the RSQ standard a fibre is the cardinality of the admissible alternatives.
Three of the fifteen rows report a declared-instance count instead, and two report
1 for choices the same row calls GENUINELY-FREE. **Repair:** split the column into
`fibre` (admissible alternatives, ∞ where unbounded) and `declared` (instances
run), and re-class the division-event times and the leg at the cut as
`GENUINELY-FREE (fibre unbounded; 1 declared)`.

**(b) The verdict-determining choice is missing.** Absent from the inventory:

- **the declared gate** — inherited per-generator vs family covariance. This is the
  most consequential free choice in the unit: the head law branches on it, and
  declaring the other one would have produced `R5-BLOCKED-AT-THE-GATE` as the head
  rather than as a segment. Fibre 2 (at least), GENUINELY-FREE, verdict-determining.
  It must be inventoried and flagged as such.
- the two scramble controls (declared, fibre free)
- the refinement size L = 8 (the pin calls it "the declared doubling"; the inventory
  lists only "the lattice size" as FORCED-anchored, which is L = 4)
- the projective-period cap of 32
- the six named coins

The first of these is a MAJOR-adjacent omission and is the inventory repair that
matters; the rest are completeness.

---

## 12. Prose ↔ receipt ↔ output sweep

35 receipt totals checked against the paper's prose mechanically: **35 of 35 agree**
(632, 576, 640, 0, 8, 10461394944000, 58, 0, 52, 4096, 0, 0, 1920, 576, 384, 384,
120, 0, 18, 512, 512, 6, 6, 12, 12, 64, 61, 60, 58, 3, 24, 40, 9, 17, 14, 21). The
per-stencil ranks (1, 2, 2, 2, 3, 4 locally, 8 globally) agree with
`/holonomy_rank`. The output file's seven gate lines agree with the receipt.

**The only prose↔artifact deviations are the two in the paper's verdict block
(M1).** Everything else the paper prints, the receipt carries, and I reproduced
independently.

Deviations priced honestly, in the paper's own §11: the three recorded there are
correctly recorded — the uniform-configuration window (declared, carried in three
places), the absence of a finite class on the interfering sector (proof reported
instead of a class), and the two-excitation extension at link grain only (a
negative, so it shelters no positive claim). I add no fourth deviation of that
kind; M1–M5 are findings, not undisclosed scope.

---

## 13. MINOR findings

- **m1.** §3 "no matrix enters the receipt" — literally false; six named coins are
  in the receipt as 2×2 field matrices, correctly, as inputs. Scope the sentence:
  "no holonomy matrix enters the receipt".
- **m2.** §3's "exactly the sector" over-reaches at coin granularity — see §7.
  Repair: "contained in the sector", plus "384 of the 512".
- **m3.** §7 "the global group is an extensive object that grows with the lattice".
  "Extensive" is licensed for the **support** and the plaquette count, both exactly
  L² and therefore literally extensive. It is not licensed for the group:
  log|A_n| ≈ n log n − n is superextensive by a log factor, and "extensive object"
  is not a defined predicate of a group. The measured fact is sharper and should be
  stated as such: **the global class is A_{L²} on the entire site set at both
  sizes — the support is exactly the volume.** Note this inverts the paper's
  framing: the *law* (full alternating on its own support) holds at both grains and
  both sizes; what refines is the support. Suggested segment token in M4:
  `GLOBAL-SUPPORT-IS-THE-VOLUME`.
- **m4.** §7's "CR-D's ladder tops out at A₇" — disambiguate tower (A₁₅) from
  three-wing ladder (A₇). See §8.
- **m5.** §10 successor "The exclusivity's reach" asks a question the unit's own
  theorem answers: the lemma holds exactly when the two supports meet in ≤ 1 site,
  and plaquette grain is indeed the first overlap (2) at which it fails. Convert
  the open item into a stated corollary.
- **m6.** The scramble control is run at one coin (`ANTI-X`) only. The physical
  class is uniform across all 64 antidiagonal coins, so this is harmless, but the
  §7 table should say at which coin it was taken.
- **m7.** §4's table and prose are excellent; add the count `5120` (the chart
  actions under which the link set is gated closed) to the prose, since after the
  M2 repair it becomes the segment's load-bearing number.

---

## 14. THE SUCCESSOR REGISTER

**What an R5-QCD-shaped follow-on may pose,** under the no-confinement discipline:

1. **The non-uniform configuration census** — the unit's own first successor and
   the right one. Until coins may vary link to link, every group statement here is
   about a measure-zero slice of the arena the unit built. Cheap first step as the
   paper says (two-coin or stratum-uniform windows). **This is the gating successor:
   nothing about area laws, couplings or limits should be posed before it.**
2. **The balanced sector's group** — infinite is a floor. Whether its closure is a
   compact group, and whether the alternating law is its finite shadow, is well
   posed and untouched.
3. **A third realization criterion** — the corpus now knows that the per-generator
   criterion is empty on any location-carrying family (M2/§6) and that the
   family-covariance criterion is an identity that selects nothing. Neither can
   serve. Deriving a criterion that actually selects, and re-reading the earlier
   units' transport numbers through it, is the highest-value item on this list and
   is a question about the corpus, not about this rung.
4. **A measure on configurations** — the missing object behind items 1 and 5, and
   the precondition for any expectation-valued statement whatever.
5. **The area law — not yet posable.** See M5. It requires items 1 and 4, and it
   lives at the grain where G7 measured 0-of-2 separation.

**What THE COUPLING UNIT inherits from this rung:**

- *Inheritable as measured:* the existence of a non-abelian plaquette holonomy on
  the declared arena (576 of 640, against a provably flat control at 0 of 3364);
  the exclusion theorem **as a support-overlap law** — coin-alphabet-independent,
  proved, and surviving the declared two-excitation sector; the one-way link
  *defect ⇒ infinite-order holonomy* (with the strictness, 384 of 512); the finite
  classes as isomorphism classes with arena-relative rank, **at the local stencils
  only**; the flat control's provable flatness as a reusable negative control; and
  the gate-lineage finding of §6, which is the most transferable thing R5 produced.
- *Explicitly NOT inheritable:* the family-covariance criterion as a **gate** — it
  selects nothing, and a successor that cites it as having licensed the family will
  be citing an identity (M2); any refinement-**limit** statement — one step, and its
  local half is forced (M3); the global A₁₆/A₆₄ as a **discriminating** fact (G7,
  0 of 2) (M4); the alternating family as a **theory-level preference** (§8); the
  rank 8 as anything but arena-relative; any transport number from R4b (already
  correctly disclaimed and gated to zero anchors); and every confinement-adjacent
  object, which does not exist on this arena.
- *Inheritable only with its scope attached:* every group statement carries
  `SWEPT-RANGE=UNIFORM-CONFIGURATIONS`, and a successor that drops that segment
  changes the claim.

---

## 15. Summary of required repairs

| id | severity | repair | touches |
|---|---|---|---|
| M1 | MAJOR | fix the two misquoted verdict segments; add `cl["verdict"]` to `paper_claims` + a mutant | paper §head, instrument §12 |
| M2 | MAJOR | disclose family covariance as **forced**; re-point the segment at the 5120 link-set closure; register the forcing under #34 | paper §4, head segment, instrument |
| M3 | MAJOR | state that local stability is forced by non-wrapping; retitle §1 and name the two unreachable branches | paper §1, §7, head segment |
| M4 | MAJOR | mark the global refinement segment as not scramble-separated | head segment |
| M5 | MAJOR | extend `G-NO-CONFINEMENT-LANGUAGE` to sweep the paper prose with a declared vocabulary + window; rewrite §10's area-law item | instrument, paper §10 |
| §7 | — | adopt the licensed exclusion sentence; "contained in", not "exactly"; add 384-of-512 | paper §3, §5 |
| §8 | — | adopt the licensed CR-D sentence; drop the A₅/A₇ double-count | paper §7 |
| §10 | — | mark the G3 table as at-declared-times-and-leg; add the Sym²-independence sentence | paper §5, head segment |
| §11 | — | split fibre/declared columns; inventory **the declared gate** as verdict-determining | instrument `CHOICE_INVENTORY`, paper §2 |
| m1–m7 | MINOR | as listed | paper |

**No measured quantity in this unit requires correction.** Every repair above is a
statement about scope, forcing, or transcription. The unit's mathematics survived
178 independent recomputations intact, and the one disagreement was the reviewer's.

*Grade: ACCEPT-WITH-FIXES. Every headline remains a candidate reading until
adjudication.*

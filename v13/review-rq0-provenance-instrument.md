# R3 — INSTRUMENT/SUFFICIENCY HOSTILE REVIEW

## RQ0-L5 branch A, *The Provenance Quintuple* — K4 primary

**Reviewer:** R3 (instrument lens), per `v13/note-rq0-provenance-hostile-protocol.md` (0e1ff17).

**Object, verified at receipt:** paper sha256 `b0eb273fa352…`, code sha256
`eb290aa77675c3c3…` — both match the frozen protocol's registration exactly.
Object commit `6ee172c`; pin `ce18eac` + amendment v2 `a05e3d5`; base `483311c`.
Working tree clean at review time; **no repo file was modified except this one.**

**Method.** Every number below was recomputed in my own exact code, in a
scratchpad, importing **nothing** from the unit or from its inherited modules:
the combinatorial layer was rebuilt from the corpus *definitions* (records as
partitions, futures as sector supports, `comp` as collision-graph components,
`Pres` by image-disjointness, the four Atlas clauses, the obstruction set, the
Bayes error, the state grid), and the amplitude layer was rebuilt in a
**different ring model** — Q(ζ₈) = Q[x]/(x⁴+1) with rational coordinates and
2^(−1/2) = (ζ+ζ⁷)/2 — rather than the unit's bespoke (c, s, e) triples. The
delivered script was executed only in a copy, never in the repo.

**Verdict: ACCEPT-WITH-FIXES.**

No result is reversed. **No false number was found**: 46/46 independent numeric
recomputations agree with the paper and receipt, including all 12 anchors, every
K4 finding, and every amplitude value. Both artifacts reproduce **byte-identically**
from the delivered source, and **15/15 mutants die**. The fixes below are
instrument-scope and prose-scope: three of them (F1, F2, F3) qualify claims the
paper states without qualification, and all three make the unit's own headline
*stronger*, not weaker, once stated correctly.

---

## 1. Findings, ranked

### F1 — the provenance component's own definition names the fixture, and sits outside the freeze's source scan `[moderate]`

`L5-SRC` scans 22 functions: the six quintuple definitions, the nine amplitude
definitions, the six declared statistics and the name-blindness control. **All 22
are clean** — I re-ran the scan textually and confirm 0 fixture references among
them. But `true_histories`, the function that supplies **H itself — the fifth
component of the quintuple** — contains the tokens `DISC5` and `FIXTURE`, and
*would be flagged by the unit's own scan* if it were in the scanned set. It is
not. §10's sentence therefore over-quantifies:

> "the automated **source scan** (`L5-SRC`) verifies that **no definition**
> mentions a committed boundary"

Thirteen unscanned functions name a fixture; twelve are harness (`run_*`,
`render`, `verdict`, `_delta_collision`) and are properly out of scope. The
thirteenth is not harness — it defines the carried datum.

**Adjudication: real, and provably inert.** The special case is
`sup_of_map(id) if part == DISC5 else block_min_idempotent(part, n)`, and I
verified exactly that `block_min_idempotent(δ) = identity`: the branch selects
precisely the operation the general branch would have selected. Deleting it
changes no number in the paper. The *declaration* is disclosed (Deviation 1);
the *scan-scope exception* is not. Fix by scoping the §10 sentence and either
adding `true_histories` to the scan or deleting the inert branch.

### F2 — (P2)-weak is an identity, not a measurement, and has no positive control `[moderate]`

In `adjudicate_quintuple` the carried certificate is built as

```
carried = [certificate_CL(C, law, prep, n) for C in checkpoints_of(word)]
```

and `P2_weak` recomputes literally the same expression against the same
arguments and compares. **It cannot return False for any carry the unit
constructs.** The `p2-break` mutant forces `return False`, which tests that the
gate is wired, not that the predicate can catch anything. Nowhere in the unit is
a *dishonest* carried certificate constructed and shown to be rejected — (P2)
has no positive control anywhere in the delivery.

The paper reports, as the finding (gate `L5-D1-P1`, §4.1, abstract):

> "**(P1) and (P2) pass at every committed patch**, forged and legitimate
> alike … and its checkpoint certificates verify"

**Adjudication: this strengthens the unit's own kill and must be said.** The
reason provenance adds no rejection power is not that four measurements happened
to come out positive; it is that *an honest declarer always verifies, by
construction*. The code knows this — `passing_histories_1`'s docstring says
"(P2) is vacuous for an honestly-carried certificate … which is itself the first
half of the regress" — but the paper never says it, and instead presents a
four-row table of a quantity that has one possible value. Fix: state the vacuity
at Definition 2.2 and in §4.1, and let the discriminating weight of (P2) rest,
as it in fact does, entirely on the strong reading.

### F3 — the freeze's SHA registration cannot survive a mutant repair, and one of the two repairs moved a registered hash `[moderate]`

Five of the seven mutant switches live **inside SHA-registered definitions**:
`P1` (`p1-break`), `P2_weak` (`p2-break`), `matmul` (`amp-cancel-lax`),
`layered_edges` (`acyc-lax`), `cycle_basis_holonomies` (`hol-lax`). `L5-00`
registers `inspect.getsource(f)` — the whole body, mutant branch included.
Therefore the mid-unit repair of `amp-cancel-lax`, which lives in `matmul` (an
`AMP_DEFS` member), **necessarily changed that definition's registered SHA
between the first selftest pass and delivery**. The other repair, `nb-lax`, lives
in `run_discriminator_4`, which is un-registered; it moved no hash.

The registration is a *within-run* ordering guarantee — hashes are computed from
the running source before any fixture verdict — and carries **no cross-run
baseline**: no pre-repair hash exists anywhere in the repo (the receipt first
appears at `6ee172c`), so nothing could detect a definition edit between runs.

**Adjudication: freeze-on-delivery is honored in the only sense the instrument
implements, and §10's disclosure is honest as far as it goes.** No number is
affected — the delivered artifacts reproduce byte-identically from the delivered
source, and `matmul`'s substantive path is untouched by its mutant branch. But
§10 should say (i) that the cancellation repair touched a registered definition,
and (ii) that `L5-00` binds the receipt to the *delivered* source, not across
revisions. As currently written, "SHA-first registration" reads as an
immutability claim the mechanism does not make.

### F4 — `L5-NB`'s declared-statistics clause is never exercised by any mutant `[minor-moderate]`

I re-ran the name-blindness sweep under three groups. All six declared
statistics register **0 violations under every one of them**; only the negative
control's status moves:

| relabelling group | declared-statistic violations | control violations | `L5-NB` |
|---|---|---|---|
| full S₅ (120) — the delivered gate | 0 (all six) | 120 | PASS |
| the state's 24-element stabiliser | 0 (all six) | 12 | **PASS — a mutant here SURVIVES** |
| trivial group (1) — the repaired `nb-lax` | 0 (all six) | 0 | FAIL |

This **substantiates §10's account** of the pre-repair mutant ("too weak to move
statistics that happen to be invariant at the committed state"): I reconstructed
exactly such a mutant and confirmed it survives. It also shows that `nb-lax`
kills the gate *solely* through the self-test clause, and that no mutant in the
suite can make a declared statistic register a violation. The "0 violations over
2,880 tests" half of `L5-NB` is therefore mutation-untested — though it is
**true**: I measured 0/2,880 independently, with the control caught at 120.

### F5 — `A08` (ω's three zeros) is a degenerate anchor at the committed preparation `[minor]`

ω sums the declared mass of blocks disjoint from the reachable set, and the
reachable set always contains the preparation. At `PREP_FULL` no block can miss
it, so ω = 0 identically. I verified ω = 0 at **all 52 records**, not only the
three coarse ones. The anchor is faithful but discriminates nothing at this
preparation; listing it among "twelve terminal values reproduced" reads as more
content than it carries. (`A06` and `A12` are also at `PREP_FULL` and are *not*
degenerate — I re-derived both by sweeping all 52 records.)

### F6 — "exactly n components in every case" is derived, not measured `[minor]`

`run_acyclicity` sets `C = r + V − |E|` with `V` hard-coded to `(m+1)·n`, so
given the measured `rank = 0` and `|E| = m·n`, `C = n` is an arithmetic identity,
not a count. The claim is nonetheless **true**: I counted components directly on
the full layered vertex set (union-find over all (m+1)·n vertices, isolated
upper-layer vertices included) and got exactly n in 720/720 sampled paths. Note
the distinction matters — on the *occupied* subgraph the component count is not
n (a constant step gives 1), and Theorem 3.2's C = n is a statement about the
full graph. The proof as written is correct; the gate text should say C = n
follows by Euler from the measured rank.

### F7 — "2,880 carried paths" counts evaluations, not distinct paths `[minor]`

The sweep is, per law, `for a in pool[:60]: for b in pool[:6]: for w in ([a],[a,b])`,
so each one-step path is evaluated six times. Per law: **720 evaluations of 420
distinct paths**; over four laws, **2,880 evaluations of 1,680 distinct paths**
(240 distinct one-step, 1,440 two-step). The measurement is sound — rank 0 in
every case — but the abstract's and §3.2's "measured over 2,880 carried paths"
should read "path evaluations", or be restated at 1,680.

### F8 — the reported "holonomy phases" are arguments with the modulus dropped `[minor]`

The fundamental-cycle products at the amplitude scope are **not unit modulus**:
the (H₀₁) loop product is exactly **−1/4**, which the table renders as ζ₈⁴. The
unit returns `acc[2]`, the root-of-unity exponent, discarding the `c·2^(−s/2)`
factor; the modulus is carried separately as `certificate_AMP`'s moduli profile.
I reproduced every reported phase in an independent ring model and they are all
correct. But Definition 3.1's "a quantity is gauge-invariant iff it is a product
of edge amplitudes around a closed loop" followed by a column of ζ₈ powers
conflates the loop product with its phase. Fix: say the carried invariant is the
*phase* of the loop product, the modulus travelling in the moduli profile.

### F9 — (i-b) is true by construction in every row of the §4.1 clause table `[minor]`

The unit adjudicates with `fam := Pres_L(part)`, and clause (i-b) asks exactly
whether 𝔉 = Pres_L(A(B)); the ✓ in that column cannot be otherwise. This is
inherited B″ convention, not a defect, but the table presents four measured
clause verdicts where there are three and an identity. One clause of prose fixes
it.

### F10 — the amnesty sweep is measured for one statistic and extrapolated for five, on an ungated declaration `[minor]`

For the five statistics not listed in `READS_RHO`, the sweep computes at the
committed state once and writes `ties = 4845 − s − i`. **The extrapolation is
sound and the result is correct** — I swept all six over all 4,845 states for
real and got 0 separations / 4,845 ties / 0 inversions for each — but `READS_RHO`
is a hand-maintained set with no gate behind it: a future ρ-reading statistic
omitted from it would be silently extrapolated from one state. Fix: gate
ρ-independence (compare values at two states) rather than declare it.

### F11 — the budget overrun is declared in the LOG, not in the delivery's own deviations appendix `[minor]`

Appendix A opens "Per the #121 rule, **every deviation ships with the
delivery**" and then lists ten *analytical* deviations. The two **process**
deviations are handled elsewhere: the mutant repairs in §10 (correctly, and
verified real below), and the budget overrun only in `v13/LOG.md` #171 ("the
~45 min budget exceeded (~2h, selftest-driven) — declared"). The substance is
disclosed; the location contradicts the appendix's own universal claim. Fix:
add it as Deviation 11, or scope Appendix A to analytical deviations and
cross-reference the LOG.

---

## 2. The K4 adjudications

**(a) The discriminator-family-(1) finding — VERIFIED, per patch.** Clause
vectors recomputed independently, both variants bit-identical:

| context | provenance | (i-a) | (i-b) | (ii-a) | (ii-b) | (P1) | (P2)w | (P2)s | L5 |
|---|---|---|---|---|---|---|---|---|---|
| δ address chart | LEGIT | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **yes** |
| forged 2+1+1 | FORGED | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ | no |
| forged 2+2 | FORGED | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ | no |
| legit tomographic min | LEGIT | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ | no |

(P1) and (P2)w pass at all four; the rejection is carried entirely by the
inherited clauses, and the three coarse charts share one failing vector
(i-a ✗, ii-a ✗). Confirmed. **Qualified by F2**: the (P2)w column is an identity,
and by F9: the (i-b) column is an identity.

**(b) The (P2)-strong repair's collapse — VERIFIED.** Re-run independently:
(P2)-strong certifies δ and rejects all three coarse charts including the
legitimate tomographic minimum. It collapses onto B″ rigidity exactly as claimed.

**(c) The backwards fan-in and manufacture-depth ranking — VERIFIED, re-derived.**
Declarable one-step histories 120 / 120 / 60 / 20 against admissibility costs
0 / 120 / 360 / 1260: the forged 2+1+1 is the **more** generable boundary
(120 vs 20 at the legitimate coarse chart), and manufacture depth returns
0 / 1 / 1 / 1, ranking the legitimate coarse chart **with** the forgeries. Both
readings in §4.2 are correct and correctly signed.

**(d) The amnesty sweep's 4,845 ties — VERIFIED AND STRENGTHENED.** I ran the
sweep the unit extrapolates: all six statistics at all 4,845 states, and got
**0 separations, 0 inversions, 4,845 ties for each of the six**. The failure is
prior to amnesty, as claimed. (See F10 for the mechanism caveat.)

**(e) THE FREEZE + MUTANT-REPAIR AUDIT — the repairs are real; freeze-on-delivery
honored in the within-run sense.**

- **15/15 mutants die** (exit 1), re-run from a copy.
- **The two repaired mutants die for the right reason, each on exactly one
  targeted gate**: `amp-cancel-lax` → `L5-AMP-CANCEL` alone (the reimposed
  non-negativity makes the (H₀₁,H₀₁) cancellation invisible again — precisely the
  claim it must falsify); `nb-lax` → `L5-NB` alone, and *through the control-escape
  clause*, which is the clause that makes the gate self-testing (F4).
- **Both negative controls genuinely catch, measured independently**: `TUNE`
  is flagged by the scan on its `PTOMO` reference, and the label-reading control
  registers **120 violations** under the delivered group while all six declared
  statistics register 0.
- **Determinism/freeze**: both artifacts reproduce **byte-identically** from the
  delivered source; no wall-clock value enters either.
- **Qualifications**: F3 (one repair moved a registered hash; registration is
  within-run only) and F1 (the provenance component's own definition is outside
  the scan). Neither touches a number.

**(f) The ten deviations — adjudicated below.** Nine are fix-real disclosures
that a reader needs; one (D10) is bookkeeping. The budget overrun is a missing
eleventh (F11).

**(g) Anchor fidelity — 12/12 reproduced by independent routes.** See the numbers
table. F5 notes that `A08` is degenerate at the committed preparation.

**BLOCKED-AT-THE-DECLARATION as the census instantiation — ACCEPTED as correct
and sharpest, with one qualifier.** The alternatives are excluded by the
measurements, not by preference: it is not *blocked at provenance* (both
predicates are decidable and both **pass**); not *at the carrier* (δ passes, and
the collision the base supplies sits at the carrier's own algebra); not *at the
law* (the law admits the true path and the convenient one alike — I count 120
admitted one-step paths writing δ and 120 writing the forged 2+1+1); and it is
strictly further out than branch C's refinement-order block, since the block
survives after the new component is added and verified. What remains is exactly
the act of declaring — the fifth component is supplied by the same party, from a
set the law fixes but does not narrow, and at the amplitude scope the lift is
free too (512 → 4 classes × 128).

**The qualifier is the slogan.** "Adding a sixth declaration to five cannot bind
the five" is false as a general statement — a sixth declaration whose *admissible
range* were narrowed in a provenance-dependent way would bind them. What the unit
actually proves is the functionality clause: the declarable-history set is a
function of (B, X₀, L), so the range of any statistic on the quintuple is a
quadruple function. The slogan should carry that qualifier, and then it is exact:
*a sixth declaration whose admissible range is a function of the first four
cannot bind them.* This is the one sentence in §8 I would require changed.

---

## 3. Per-rung confirmations

| Rung | Confirmation |
|---|---|
| (a) REGRESS, both variants | **CONFIRMED.** Generation/admissibility decoupling re-derived (fan-in 120 vs cost 120 at the forged 2+1+1; cost 0 at δ); the collision re-derived at 120 histories → 1 certificate in V-CL **and** V-AMP; the declarable-history set verified to depend on (boundary, law) only; the amplitude datum verified free (512 lifts → 4 classes, 128 each). |
| (b) LOSSY, both variants, incl. the V-AMP rank residue | **CONFIRMED.** V-CL: 120 histories, one certificate, identity and deleted rotation (1,2,3,0,4) both in the class. V-AMP committed scope: one amplitude certificate. V-AMP amplitude scope: global cycle rank 3 vs checkpoint-local 2, residue 1; witness exhibited with identical local shadows ([4], [6]) and cross-checkpoint holonomies **(0,4,6) vs (1,4,5)** — reproduced exactly in an independent ring model. |
| (c) The delta-zero theorem | **CONFIRMED.** All four committed laws single-valued; rank 0 and empty holonomy in 720/720 sampled paths; E = m·n; C = n verified **by direct count on the full layered vertex set** (F6). The Euler argument is correct as stated, provided isolated upper-layer vertices are counted — which the theorem's V = (m+1)n does. |
| (d) BLOCKED-AT-THE-DECLARATION as the census instantiation | **CONFIRMED, with the slogan qualified** (§2 above). |
| (e) The scissors disclosure | **HONEST.** Both readings are run; §6.4's table matches the gate value; `L5-LOSSY-READING` is correctly classed `disclosure` and correctly excluded from must-pass, since it asserts nothing measurable. Neither reading escapes a kill, so the verdict is genuinely invariant under the choice. |
| (f) Process deviations (mutant repairs; budget) | **CORRECTLY RECORDED, one gap.** Mutant repairs recorded in §10 and verified real (§2e). Budget overrun declared in LOG #171 but absent from Appendix A, which claims completeness — F11. |

---

## 4. The ten deviations, adjudicated

| # | Subject | Adjudication |
|---|---|---|
| 1 | True histories declared, not inherited | **Fix-real, and the most load-bearing of the ten.** It is why the legitimate coarse chart's history has manufacture-path form. Correctly flagged as load-bearing in the text. Incomplete in one respect: it does not say the declaration is implemented by a fixture-naming function outside the source scan (F1). |
| 2 | (P2) carried in two readings | **Fix-real.** The strong reading is the natural repair and is measured to collapse; running both is correct. Should also say (P2)-weak is vacuous (F2). |
| 3 | The V-CL lossy adversary needed no quantum layer | **Fix-real**, and correctly reported as a *strengthening* rather than a shortfall. Verified: the witness is 120 permutations and one certificate. |
| 4 | Amplitude scope is a declared family, not a law | **Fix-real.** The FUNNEL precedent is the right one, the closure is computed and gated at 7 operations. Honest. |
| 5 | Amplitudes exact in a restricted family | **Fix-real.** I re-derived the whole amplitude layer in a *different* exact model of the same field and every value agrees, so the restriction costs nothing at this scope. |
| 6 | The V-AMP lossy verdict is reading-relative | **Fix-real**, and the single most important disclosure in the appendix — it is the scissors. Correctly stated that the verdict is invariant and the firing kill is not. |
| 7 | Two-step scope is declared, not exhaustive | **Fix-real.** The `[EXH-1]` tagging is applied where it belongs, and Theorem 5.3 is indeed independent of sweep depth. |
| 8 | Six statistics declared where the pin named none | **Fix-real and necessary** — the pin's requirement is vacuous without a family. Two of the six exist only because the quintuple does, which is the right test of good faith. |
| 9 | Verdict tag instantiated at the declaration | **Fix-real.** Adjudicated in §2 above: correct and sharpest, slogan qualified. |
| 10 | Lean none; no new primitive | **Cosmetic** (bookkeeping against the pin), correctly stated. |
| — | **Budget overrun (~45 min → ~2h)** | **Missing from Appendix A**; declared only in LOG #171 — F11. |

---

## 5. Numbers table — 46 independent recomputations, all agreeing

| # | Quantity | Independently computed | Paper / receipt |
|---|---|---|---|
| 1 | Record-lattice sizes, 1..5 configurations (`A01`) | 1, 2, 5, 15, 52 | same |
| 2 | \|DET\|, \|REV\| (`A02`) | 3125, 120 | same |
| 3 | Counter-law size, reversible count (`A03`) | 120, 1 | same |
| 4 | Pres under DET at the four boundaries (`A04`) | 120, 240, 420, 1280 | same |
| 5 | ε at the coarse triple (`A05`) | 1/16, 1/8, 3/16 | same |
| 6 | Rigidity: admissible records under DET/REV/counter (`A06`) | 1, 1, 1 | same |
| 7 | Cost tower, obstruction sizes (`A07`) | 120, 360, 1260, 3120 | same |
| 8 | ω at the three coarse patches (`A08`) | 0, 0, 0 | same |
| 9 | ω over **all 52** records at `PREP_FULL` (F5) | 0 for all 52 | not stated |
| 10 | Admitted isomorphisms; orbits of the 52 records (`A09`) | 24, 12 | same |
| 11 | Declared state grid at denominator 16 (`A10`) | 4845 | same |
| 12 | Single-valuedness of all four committed laws (`A11`) | true ×4 | same |
| 13 | Jointly admissible comparable pairs (`A12`) | 0, 0, 0 | same |
| 14 | Clause vector at δ | (✓,✓,✓,✓), L5 yes | same |
| 15 | Shared clause vector at all three coarse charts | (✗,✓,✗,✓), L5 no | same |
| 16 | (P1) ∧ (P2)w at all four patches | true, true, true, true | same |
| 17 | (P2)-strong verdicts | true, false, false, false | same |
| 18 | Declarable one-step histories (fan-in) | 120, 120, 60, 20 | same |
| 19 | Cost of admissibility per boundary | 0, 120, 360, 1260 | same |
| 20 | Manufacture depth | 0, 1, 1, 1 | same |
| 21 | Intermediate spread / path length | 1,1,1,1 / 1,1,1,1 | same |
| 22 | Coarsest-checkpoint defect | 0, 1/16, 1/8, 3/16 | same |
| 23 | Carried cycle rank at the four patches | 0, 0, 0, 0 | same |
| 24 | Name-blindness violations, six statistics × 4 × 120 | 0 over 2,880 | same |
| 25 | Label-reading control violations (must be caught) | **120** | caught |
| 26 | Amnesty, **all six** statistics × 4,845 states | 0 sep / 4,845 ties / 0 inv each | same (5 extrapolated) |
| 27 | `block_min_idempotent(δ)` vs identity (F1) | equal — branch inert | not stated |
| 28 | Amplitude generators exactly unitary | all five | same |
| 29 | Cycle ranks: (ID),(SW01),(H01),(H01,H23),(F4),(H01,H01) | 0, 0, 1, 2, 9, 3 | same |
| 30 | Holonomy phases at (H01) / (H01,H23) | (4) / (4,4) | ζ₈⁴ / ζ₈⁴,ζ₈⁴ |
| 31 | Holonomy phases at (F4) | 0,2,2,4,4,4,4,6,6 | same |
| 32 | Holonomy phases at (H01,H01) | 0,4,4 | same |
| 33 | (H01) fundamental-cycle **product** (F8) | −1/4 (not unit modulus) | rendered ζ₈⁴ |
| 34 | Records written by (ID),(H01),(H01,H23),(F4) | δ, 2+1+1, 2+2, tomographic min | same |
| 35 | (H01,H01): support vs amplitude record | forged 2+1+1 vs δ | same |
| 36 | Acyclicity: rank 0, empty holonomy | 720/720, 0 violations | same shape |
| 37 | E = m·n and C = n by **direct count**, full vertex set | 720/720 | derived (F6) |
| 38 | Path count: evaluations vs distinct (F7) | 2,880 vs 1,680 | "2,880 paths" |
| 39 | Unitary lifts among **all 4,096** phase quadruples | 512 | 512 ("complete") |
| 40 | The `d = c−(a−b)+4` parametrisation vs the unitary set | exactly equal | asserted |
| 41 | Holonomy classes over the lift family | 4 classes × **128** each | same |
| 42 | LOSSY V-CL: histories → certificates, class size | 120 → 1, class 120 | same |
| 43 | Identity and deleted rotation (1,2,3,0,4) in the class | both present | same |
| 44 | Cross-checkpoint witness: local shadows / globals | ([4],[6]) / (0,4,6) vs (1,4,5) | same |
| 45 | Global vs checkpoint-local rank, residue | 3, 2, 1 | same |
| 46 | Scanned definitions naming a fixture / unscanned ones (F1) | 0 of 22 / 13, incl. `true_histories` | "no definition" |

Process checks: both artifacts **byte-identical** on re-run; **15/15** mutants
exit 1; the two repaired mutants kill exactly `L5-AMP-CANCEL` and `L5-NB`
respectively; a reconstructed pre-repair `nb-lax` (24-element stabiliser group)
**survives**, confirming §10's account.

---

## 6. Sentences to rewrite

1. **§10** — "the automated **source scan** (`L5-SRC`) verifies that **no
   definition** mentions a committed boundary" → *"…verifies that none of the 22
   registered definitions — the quintuple's, the amplitude layer's and the six
   statistics' — mentions a committed boundary. The declared true histories
   (Deviation 1) are supplied outside that set by a function that does name the
   carrier's own algebra; the branch is inert, since the block-minimum idempotent
   of the discrete boundary is the identity."*

2. **§4.1 / abstract** — "**(P1) and (P2) pass at every committed patch**" →
   add: *"(P2)-weak cannot fail on an honestly declared carry: the certificate is
   recomputed by the route that produced it, so honesty verifies by construction.
   That is not a weakness of the measurement but the content of the finding —
   the discriminating weight of (P2) lies entirely in the strong reading, and
   that reading collapses onto rigidity."*

3. **§8** — "Adding a sixth declaration to five cannot bind the five." →
   *"A sixth declaration whose admissible range is a function of the first four
   cannot bind them — which is what Theorem 5.3 proves here, and is the exact
   form of the block."*

4. **§10** — after the mutant-repair paragraph, add: *"The cancellation mutant
   lives inside a SHA-registered definition, so its repair changed that
   definition's registered hash; `L5-00` binds the receipt to the delivered
   source and makes no claim across revisions."*

5. **§3.2 / abstract** — "Measured over **2,880 carried paths**" → *"2,880 path
   evaluations (1,680 distinct paths; each one-step path is evaluated once per
   two-step partner)"*; and "with E = mn and C = n holding in every case" →
   *"with E = mn measured and C = n following by Euler from the measured rank."*

6. **§3.1 / §3.3 table** — the column headed "holonomy phases" carries the
   *phase* of the loop product, not the product: at (H₀₁) the product is −1/4.
   Either rename the column "loop-product phases" or state that the modulus
   travels in the moduli profile.

7. **Appendix A** — add Deviation 11 (budget: ~45 min pinned, ~2h actual,
   selftest-driven), or scope the opening sentence to analytical deviations and
   cross-reference LOG #171.

---

## 7. Verdict

**ACCEPT-WITH-FIXES.**

The unit's four K4 findings are all **verified independently and none is
softened**: (P1)/(P2) pass at every patch forged and legitimate alike, with the
rejection carried entirely by the inherited clauses; (P2)-strong collapses onto
rigidity and rejects the legitimate chart too; the fan-in runs backwards, 120
against 20, and manufacture depth ranks the legitimate coarse chart with the
forgeries; and the amnesty sweep ties at every one of 4,845 states for every one
of the six statistics — I re-swept all six rather than five and it holds. The
freeze and mutant-repair audit passes: the repairs are real and targeted, both
negative controls genuinely catch, 15/15 mutants die, and the delivered artifacts
reproduce byte-identically. `BLOCKED-AT-THE-DECLARATION` is the correct and
sharpest census instantiation available at this scope.

The fixes are precision, not correction. Three of them (F1, F2, F3) are places
where the paper states without qualification something that is true only in a
scoped sense — and in each case the scoped version is the stronger claim. The
one substantive change I would require is the §8 slogan: as written it asserts a
general impossibility the unit does not prove, where the functionality clause it
*does* prove is both exact and sharper.

*Freeze-on-delivery observed: this file is written once and not revised.*

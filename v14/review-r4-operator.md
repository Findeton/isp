# R4 (paper-10, the defect on the stage) — HOSTILE REVIEW, REVIEWER R1 (OPERATOR LENS)

**Grade: ACCEPT-WITH-FIXES.**
**Independent recomputations: 156** (136 numbered in the operator rebuild + 20
out-of-band: 11 sha256 verifications, 4 plain-run reproduction checks, 2
injection runs, 2 paper-claim coverage checks, 1 compliance/waiver audit).

**Object, hashes verified at open and re-verified at close, all unchanged:**
paper `f3e8cc1618f8`, code `b079bb3b8d55`, output `58ec08893526`, receipt
`3214f4da3af2`. Pinned sources: `v12/paper1-composition-defect.md`
`81bdab5673fb`, `v12/paper1_code/exact.py` `8e90f6435922`,
`v13/code/ha_successor_receipt.json` `542b8735daf0` (I7),
`v14/code/r2_manifold_receipt.json` `08b2140f46ae` (the R2 terminal),
`v14/note-r4-qft-pin.md` `1582cea5df51`, `v14/note-gmain-r4-protocols.md`
`a3a39813e5b5`, `RUNBOOK.md` `3781cbce4e42`.

**Method (the operator lens).** Nothing was imported from the unit. The field
was rebuilt in a **different basis**: the unit carries $\mathbb{Q}(\zeta_8)$ as
integer 4-tuples over a denominator reduced mod $\Phi_8$; this review carries it
as $\mathbb{Q}(\sqrt2,i)$, 4-tuples of `Fraction` in the basis
$\{1,\sqrt2,i,i\sqrt2\}$. The census was recomputed by the **definitional route
on dense $16\times16$ Born matrices for all 4,096 ordered pairs** (the unit
spot-checks that route on a stride-5 subset), and then a **second time with no
field arithmetic at all**, from a closed-form parametrisation of the family and
a modulus/phase evaluation of the defect in $\mathbb{Q}(\sqrt2)$. All hostile
runs of the unit's own instrument were made on symlinked scratch mirrors; the
repository was never written except for this one file.

---

## 0. HEADLINE

Every measured number in this unit is correct. All 136 numbered recomputations
reproduce, including the full defect census, and a scratch replay of the
instrument reproduces the **committed output and receipt byte-identically**
(77/77 gates, 82/82 mutants dead on target, exit 0). No false computed number
was found anywhere.

What fails is **scope and registration**, at six places, and one of them is a
false sentence in the paper that is contradicted by the unit's own printed
receipt value and is load-bearing for the title. In addition, an injected false
physics qualifier reaches the delivered verdict string at exit 0 with all 77
gates passing — demonstrated, not argued.

The measured content survives the round intact. The repairs are exact, and the
principal one *strengthens* the unit rather than weakening it.

---

## 1. FINDINGS, RANKED

### MAJOR-1 — THE UNIQUENESS IS MOORE-RELATIVE, AND THE PAPER SAYS OTHERWISE (decisive)

`v14/paper-10-defect-on-the-stage.md` line 177:

> - locality on the stage requires $L\ge 4$ (measured, both connectives, three
>   dimensions);

and line 103, the caption under the §2 locality table whose rows are the Moore
rows only:

> *Scope: exhaustive over $L\in\{2,\dots,9\}$ and $d\in\{1,2,3\}$, both declared
> connectives.*

**Both are false, and the unit's own receipt says so.**
`parity_witness.von_neumann_threshold_d2 = 2`. Measured here independently
(R033/R034): under the ported criterion the locality thresholds are

| connective | d=1 | d=2 | d=3 |
|---|---|---|---|
| Moore (max-norm) | 4 | **4** | 4 |
| von Neumann (sum-norm) | 4 | **2** | **2** |

The bite is not cosmetic. Feeding the **unit's own admissibility predicate**
(locality ∧ a non-monomial local-axis generator ∧ every local axis of order
exactly $L$) with the von Neumann rows returns (R035/R036):

- MOORE → `[4]` (reproduces the unit)
- VON NEUMANN → **`[2, 4]`**

At $L=2$ under von Neumann, $(0,1)$ and $(1,0)$ are local, have order 2, and
carry **16 non-monomial unitary generators** — the unit's own order-2 row. So
under the alternative connective the unit's title claim ("One Lattice Size
Admits an Indivisible Family At All"), its §3.3 conclusion, and the verdict
segment `SCALE=L=4-UNIQUE(LOCALITY-IFF-L>=4;…)` are all false. The `SCOPE`
segment names `D=2;L=4;FIELD;ALPHABET;GENERATORS` and does **not** name the
connective. Worse, the choice inventory classes the connective
`GENUINELY-FREE | 2, both swept` — a free choice whose alternative value flips a
verdict segment, which §15 forbids leaving undisclosed. And with an alphabet
containing the order-3 witness below, von Neumann admits `[2, 3, 4]` (R040).

There is a further internal contradiction: the unit **gates** that the two
connectives disagree (`G-PARITY-WITNESS` requires `delta != 0`, falsifier
`MUT-PARITY-WITNESS` "makes both connectives agree by fiat"). A passing gate
certifies the disagreement while the prose asserts the agreement.

**REPAIR (strengthening).** The connective is not free — it is **forced by the
anchor**. The anchored link set `PV-I7-LINKS = [[1,0],[0,1],[1,1]]` contains
$(1,1)$, whose max-norm is 1 and whose **sum-norm is 2** (R148–R150): the
anchored links lie inside the Moore ball and **not** inside the von Neumann
ball. So:

1. reclassify the choice-inventory row *the neighbourhood connective* from
   `GENUINELY-FREE | fibre 2` to `FORCED (anchored) | fibre 1`;
2. add a gate deriving the exclusion from `PV-I7-LINKS` (falsifier: a mutant
   that admits the von Neumann connective must then die, and it will, because
   `admissible` becomes `[2,4]`);
3. delete both "both connectives" phrases and caption the §2 table
   *Moore connective; the von Neumann threshold is 2 and is excluded by the
   anchored link (1,1)*;
4. add `CONNECTIVE=MOORE(FORCED-BY-PV-I7-LINKS)` to the verdict's `SCOPE`
   segment.

After this repair the headline is **stronger** than delivered: the scale is
unique *and* the connective that makes it unique is anchored, not chosen.

### MAJOR-2 — THE LIGHT-CONE VERDICT SEGMENT IS VACUOUS AT $L=4$

`G-TWOPOINT-LIGHTCONE` asserts
`radius_by_step[n] <= min((n+1)*single_step_radius, L//2)` together with
`radius_by_step[0] == single_step_radius`. On $(\mathbb{Z}_4)^2$ the maximum
possible `torus_absmax` is $2 = L//2$ (R117), so the right-hand side is $2$ for
every $n\ge 1$ and for every generator of radius $\ge 1$. An exhaustive probe
over **all** profiles in $\{0,1,2\}^4$ with `r[0] = r` finds that the only
violating profiles are the 26 with $r=0$ (R116) — i.e. the bound can fail only
for the single radius-0 generator, where it again says something forced. For 57
of the 58 circulants the bound cannot fail for **any** conceivable profile, and
the only clause with content, `radius_by_step[0] == single_step_radius`, is true
by definition of step 1.

The paper nevertheless reports it as a measured physical fact (line 350):
"never grows faster than one neighbourhood per step; the bound holds at every
generator and is not saturated by all of them". The verdict carries
`LIGHTCONE=ONE-NEIGHBOURHOOD-PER-STEP`. This is the #208 class — an
analytically-forced clause registered as a must-pass measurement — on a verdict
segment.

**REPAIR.** Register `G-TWOPOINT-LIGHTCONE` as a DISCLOSURE with its forcing
("$L//2$ is the maximum attainable radius at the working size, so the cone bound
has no content above radius 0"), and either drop the segment from the verdict or
qualify it `LIGHTCONE=BOUND-VACUOUS-AT-L=4`. The measurement that *does* have
content — the six radius profiles and the 33-of-58 half-width saturation — is
already there and reproduces (R112–R114); promote that in the segment's place.

### MAJOR-3 — `STATE=BACKGROUND-COEFFICIENT` IS FORCED BY LINEARITY

§8: "the matrix reconstructed from the sixteen point-mass responses equals the
coefficient matrix $\Delta^{B}$ exactly" and "A mutant that makes the
reconstruction state-dependent dies."

$\delta(p) = \Delta^{B}p$ is linear, so probing with the 16 point masses returns
the 16 **columns** of $\Delta^{B}$, which reassemble $\Delta^{B}$ by definition.
Verified against arbitrary matrices: the reconstruction identity holds for 50/50
random coefficient matrices (R132). No family, and no mutant that keeps the law
linear, can fail it; `MUT-STATE-BACKGROUND` kills only by zeroing the
reconstruction directly. #208 recurrence, on a verdict segment.

The companion half is a genuine measurement and does reproduce: 18 distinct
responses over 18 declared states (R129/R130), which could have collapsed and
did not.

**REPAIR.** Split the gate: DISCLOSURE for the reconstruction with the linearity
forcing registered; MEASURED for the 18 distinct responses. Re-word §8's "Two
facts, measured together" to *one forced by the linearity of the declared law,
one measured*.

### MAJOR-4 — "TRANSLATIONS ACT TRIVIALLY … MEASURED, NOT ASSUMED" IS ASSUMED

§6: "The translation group acts trivially on the whole circulant family … That
is measured, not assumed: a mutant that misreports the translation action dies."

A coefficient-map matrix $M_{x+o,x} = c_o$ commutes with every lattice
translation **by construction**. Verified as an algebraic identity on 200
arbitrary coefficient maps (random support, random non-unitary rational entries)
across 800 conjugations, 0 failures (R105); and the unit itself declares the
family as "58 translation-covariant circulants (the declared family)" in §4.2.
`G-CLASS-TRANSLATION-TRIVIAL`'s circulant clause is forced; `MUT-TRANS-TRIVIAL`
kills only by overwriting the computed count. #208 recurrence.

The gate's second clause — that the controls have non-trivial translation orbits
— **is** a measurement and reproduces (4 control orbits with more than one key,
R128; control stabilisers `[1,2,8,8,8,8]`, R104).

**REPAIR.** Register the circulant clause as forced, keep the control clause
measured, and re-word §6 to: *forced by the circulant construction; the
classification is therefore carried entirely by the point symmetries.* The
consequence (point symmetries carry the whole classification) is a real reading
and survives.

### MAJOR-5 — THE COMPLIANCE SWEEP IS UNGATED AND ONE OF ITS ROWS IS FALSE

`compliance_sweep()` returns 19 `(rule, status)` **literal strings**. No
`LD.gate` evaluates any status against the object; the statuses are typed prose
with a few `%d` interpolations. §10 nevertheless says the sweep "enumerates each
engraved rule with a **computed** status".

One row is false. The #20 row reads:

> APPLIED -- every numeric claim of the paper is emitted here as
> paper_claims.rendered and checked verbatim by --verify-paper

`paper_claims.rendered` carries **13** strings. The paper body carries **66
distinct numeric tokens** (321 occurrences). The uncovered set includes the
eight-value defect table with its cell counts, the order-census table, the §2
locality table, `216-of-576`, `372-of-1188`, `616-of-1024`, `33 of 58`,
`34,925`/`121`, `42`, `48`, `15`, the transformation-class table and the radius
profiles. This is the #20 engraving's own disease — *compliance claims are gate
claims; a compliance gate whose comparator cannot disagree with the object under
test is vacuous by construction* — and it is the exact surface through which
MAJOR-1 entered: the false "both connectives" sentence lives in the uncovered
region.

**REPAIR.** Make every compliance status a computed predicate with a declared
injection-falsifier; extend `paper_claims.rendered` to cover every numeric claim
(or mark the residue derived-in-text at its derivation site) and run
`--verify-paper` inside the plain run as a gate rather than as an optional flag.

### MAJOR-6 (K5) — THE VERDICT'S TYPED QUALIFIERS ARE UNGUARDED; A FALSE QUALIFIER SURVIVES AT EXIT 0

`build_segments()` and the independent comparator
`reconstruct_verdict_from_receipt()` each carry the **same typed literals**:
`-UNIQUE(LOCALITY-IFF-L>=4;NON-MONOMIAL-LOCAL-AXIS-IFF-L<=4)`,
`LIGHTCONE=ONE-NEIGHBOURHOOD-PER-STEP`, `STATE=BACKGROUND-COEFFICIENT`. The
complete-string comparator therefore cannot disagree about them, and
`G-VERDICT-SEGMENTS-FLIPPABLE` probes exactly one numeric key per segment.

**Demonstrated on a scratch copy.** Changing `LOCALITY-IFF-L>=4` to
`LOCALITY-IFF-L>=3` in **both** paths (2 occurrences, no other edit):

```
mutants: 82 declared, 82 killed, 82 killed by their declared target
ALL GATES PASSED (77/77); ALL MUTANTS DEAD (82/82)
EXIT=0
SCALE=L=4-UNIQUE(LOCALITY-IFF-L>=3;NON-MONOMIAL-LOCAL-AXIS-IFF-L<=4)
```

A false physics qualifier reached the delivered verdict string, the receipt and
the printed report at exit 0. The control run (the same edit in the comparator
only) died correctly at `G-VERDICT-STRING-EQUALITY`, which shows the comparator
guards only the fields it re-derives.

**REPAIR.** Derive every qualifier from a measured row —
`LOCALITY-IFF-L>=<S["locality_thresholds"]["2"]>`, `UNIQUE` from
`len(admissible)==1`, the lightcone token from the cone measurement — and add a
flippable probe per qualifier, not per segment.

### MINOR-1 — "three genuinely different computations" are one identity in four bases

§4.1 calls DENSE / CONV / FT "genuinely different computations", and the #219
compliance row repeats it. For a circulant, $B(VU)_s = |\sum_t v_t u_{s-t}|^2$
*is* the convolution route, and the character route is its Fourier transform;
the unit itself demotes the cross-term route to `FORCED` for exactly this
reason. The same holds for `G-FAMILY-UNITARY-THREE-ROUTES`: $U^\dagger U = I$,
$A(m)=\delta_{m,0}$ and $|\chi|=1$ are one identity in three bases (confirmed
here: the matrix route and the autocorrelation route agree on all 15,625
order-4 candidates, R022 — they cannot disagree except through a coding error).
These are implementation cross-checks, valuable as such; they are not
independent measurements (#234). Re-word and re-register.

### MINOR-2 — the gauge self-test tests one factor, the paper claims two

§5.3: "multiplying **either** factor by a global phase leaves the defect
fixed at every one of the checked pairs." `G-GAUGE-SELFTEST` computes only
`defect_dense(D·U2, U1)`. The untested direction is true but unmeasured. Test
both or re-word.

### MINOR-3 — "the raw order moves" is 27 of 42, and the number is neither printed nor gated

Measured here: the projective period is invariant at **42/42** and the raw order
moves at **27/42** (R121). The gate requires only `raw_moves > 0`. Print and
render the number.

### MINOR-4 — `G-DEFECT-COLUMN-SUMS` samples 64 of 4,096 rows, and the property is forced

Both composites are column-stochastic ($|U|^{\circ2}$ is doubly stochastic for
unitary $U$), so the column sums vanish identically — the paper says so ("as it
must"). Verified here on **all 3,364 circulant rows and all 4,096 dense rows**
(R083/R084). Register as a disclosure, or widen the sample so the claim and the
evidence match.

### MINOR-5 — "34,925 nodes visited" is a search-order artifact, not a property

The same five-point sweep with a different offset ordering visits **63,725**
nodes and reaches the same **121** surviving assignments and the same 0
non-monomial solutions (R146/R147). Report leaves, or name the ordering.

### MINOR-6 — `FULL` transport is forced for every circulant

The point group maps the declared axis set into itself, and
$\mathrm{gens}(f(a)) = f(\mathrm{gens}(a))$ for all 9 axes and all 8 point
elements, 0 mismatches (R151/R152). Because the axis set is exhaustive, every
circulant's point-group image is automatically a pool member up to gauge — so
"58 at FULL" is forced by the construction, and the realization census
discriminates only the 6 declared controls. The paper discloses the mechanism
("The brickwork controls are the substance of that exclusion", §7), so this is a
registration point rather than a claim failure: no member of the family under
study was excluded by the gate that is said to bite.

---

## 2. K1 — THE DEFECT CENSUS, AND THE DERIVABILITY QUESTION

**The census reproduces exactly, twice, by two routes that share no arithmetic.**

| quantity | unit | operator rebuild |
|---|---|---|
| ordered pairs | 4096 | 4096 (R075) |
| pairs at maximal transport | 3364 | 3364 (R076) |
| nonzero at maximal transport | **588** | **588** (R077, R096) |
| nonzero excluded below maximal | 150 | 150 (R078) |
| distinct exact values | 8 | 8 (R080) |
| all-rational nonzero rows | 588 / 588 | 588 / 588 (R082, R097) |
| Markovian pairs / nonzero | 1792 / 0 | 1792 / 0 (R085) |
| free pairs / nonzero | 2304 / 738 | 2304 / 738 (R086) |
| local / non-local | 216-of-576, 372-of-1188 | identical (R087/R088) |
| matched coordinates | 616 of 1024 | 616 of 1024 (R141) |
| separations, max defect radius | 16, 2 | 16, 2 (R089/R090) |
| column sums | zero | zero on all 4096 rows (R083/R084) |

The eight values with cell counts reproduce exactly:
$+5/8\times24$, $+1/2\times108$, $+1/4\times336$, $+1/8\times144$,
$-1/8\times192$, $-1/4\times336$, $-1/2\times108$, $-3/8\times24$
(R081 by the field route, R098 by the phase route; 1,272 cells, signed sum 0).

**THE DERIVABILITY ANSWER: the census is analytic, and this review derives it
end to end. What remains measured is one thing only, and it is named.**

**(a) The family is closed-form.** Solving $A(0)=1$, $A(2a)=0$, $A(a)=0$ by hand
over the declared moduli gives, for an order-4 axis, exactly five shapes —
three monomial families ($8$ each), a support-$\{a,-a\}$ family
$c_{\pm a} = \zeta^{B},\zeta^{C}/\sqrt2$ with $B-C\equiv\pm2$ ($16$), and a
full-support family $c_0=\zeta^A/\sqrt2$, $c_{\pm a}=\zeta^{B},\zeta^{C}/2$ with
$B-C\equiv\pm2$ and $2A\equiv B+C+4 \pmod 8$ ($32$) — total
$8\cdot3+16+32 = 72$, of which 24 monomial and 48 not. For an order-2 axis,
$8\cdot2+16 = 32$, 16 monomial. **The closed-form sets equal the swept sets
exactly at all nine axes, 0 mismatches (R092/R093)**, and the whole pool rebuilds
from the parametrisation alone with no alphabet sweep (R094). The pool size is a
closed-form count, $58 = 6\cdot9 + 3\cdot4 - 8$ (six order-4 axes at 9 gauge
classes, three order-2 axes at 4, minus the 8 duplicate copies of the shared
identity class) — R067/R068; the monomial count is $16 = 1 + 2\cdot6 + 3$
(R070/R071).

**(b) The defect is closed-form.** With every coefficient written as
$(m,\theta)$, $m\in\{1,1/\sqrt2,1/2\}$, $\theta\in\mathbb{Z}_8$ (R091: all 24
non-zero alphabet elements admit these coordinates),
$$\Delta(s) \;=\; 2\sum_{k<l} m_k m_l \cos\!\big((\theta_k-\theta_l)\tfrac{\pi}{4}\big),$$
evaluated in $\mathbb{Q}(\sqrt2)$. Computed this way — **with no field
arithmetic whatever** — it reproduces the entire 3,364-pair census cell for
cell, **0 disagreements** with the definitional route (R095), and returns the
same 588 and the same eight values (R096–R098).

**(c) The count 588 is pure support combinatorics.** A cell is nonzero only at a
*collision*, $t_1+r_1 = t_2+r_2$, i.e. only when the difference sets
$D^*(v), D^*(u)$ intersect. The classified shapes have exactly three difference
types: $\{2a\}$ (support-2 on an order-4 axis), $\{a\}$ (support-2 on an
order-2 axis), $\{a,-a,2a\}$ (full support). $2a$ is 2-torsion, so the 18
generators with $D^*$ a single 2-torsion element split 6 per torsion class, and
the 24 full-support generators sit 4 per order-4 axis. Counting the intersecting
ordered pairs:
$$\underbrace{3\cdot6\cdot6}_{108}\;+\;\underbrace{2\cdot(6\cdot4)\cdot6}_{288}\;+\;\underbrace{6\cdot16+3\cdot2\cdot16}_{192}\;=\;588 .$$
Verified: pairs whose difference sets intersect $=$ 588 $=$ pairs with a measured
nonzero defect (R134–R136, R139).

**(d) The value set is closed-form, split by collision multiplicity.** The
maximal multiplicity per pair is 1 for 2,776 pairs, 2 for 492 and 3 for 96
(R099); $492+96 = 588$. Multiplicity 2 yields exactly the symmetric six values
$\pm1/2 (108)$, $\pm1/4 (336)$, $\pm1/8 (144)$; multiplicity 3 — which occurs
only at $s=0$ for same-axis full-support pairs, $6\cdot4\cdot4 = 96$ — yields
$+5/8 (24)$, $-1/8 (48)$, $-3/8 (24)$, corresponding to
$|\sum w|^2 \in \{1, 1/4, 0\}$ against $\sum|w|^2 = 3/8$ (R133). **This is the
whole account of the paper's asymmetry**: $+1/8$ has 144 cells and $-1/8$ has
$144+48 = 192$ because the extra 48 are multiplicity-3 cells.

**WHAT REMAINS MEASURED, exactly.** One fact: *no collision-bearing pair
cancels identically*. The combinatorics predicts which pairs *can* be nonzero;
that every one of them *is* nonzero — 588 predicted, 588 measured, 0 accidental
cancellations (R136) — is not forced, and individual cells do vanish. Everything
else in §4.2 is a finite closed-form enumeration.

**Recommendation.** The paper should say this. A census presented as
measurement, when it is a theorem plus one measured non-degeneracy, understates
the unit. §4.2 should carry the closed form of the family, the $588 = 108+288+192$
count, the multiplicity-2/multiplicity-3 value split, and the single measured
residual.

---

## 3. K2 — THE $L=4$ THEOREM, BOTH HALVES, AND THE STENCIL SCOPE

**Half one, the order collapse: TRUE, and more alphabet-independent than
claimed.** Re-proved independently: for $\mathrm{ord}(a)=n\ge5$ the offsets
$0,\pm a,\pm2a$ are distinct, so $A(2a)$ has the single term
$c_{-a}\overline{c_a}$, forcing $c_ac_{-a}=0$; $A(a) = c_0\overline{c_a} +
c_{-a}\overline{c_0}$ then kills a second coefficient. Both identities verified
mechanically on 400 random field triples, 0 failures (R031/R032), and the
collapse verified over a **215-element rich alphabet** containing $1/3$, $2/3$,
$3/5$, $4/5$ and $\sqrt2$-bearing entries at orders 5, 6, 7, 9 — 0 non-monomial
solutions at every order (R024–R028). The theorem is sound and its
alphabet-independence is real.

**The order-3 emptiness is alphabet-relative, as declared — and the paper is
conservative about it.** Exhibited: $c = (1/3,\,-2/3,\,-2/3)$ on $\mathbb{Z}_3$
is unitary, non-monomial, and **rational**, hence inside $\mathbb{Q}(\zeta_8)$
(R037/R038). So the emptiness is not even field-relative; it is purely a
property of the declared 25-element modulus set. The declaration in §9 is
honest.

**Half two, locality: TRUE ONLY FOR THE DECLARED CONNECTIVE.** See MAJOR-1. Note
that under Moore the order-3 alphabet-relativity does *no* work — $L=3$ is
excluded by locality anyway — so the Moore-relative uniqueness is fully
alphabet-independent given one exhibited $L=4$ witness. The paper *understates*
here ("theorem above, plus the exhaustive alphabet sweep"): the sweep is needed
only for non-emptiness at $L=4$, not for uniqueness. Under von Neumann the
order-3 relativity becomes load-bearing and the admissible set grows to
$[2,3,4]$ (R040).

**Do 5-point or Moore stencils reopen the window? Analysed, not swept.**

*The 5-point (von Neumann) stencil at $L\ge5$ collapses, and it is a theorem —
the unit reports only a sweep at one size.* With
$O=\{0,\pm e_1,\pm e_2\}$ and $L\ge5$: $A(2e_1)=c_{-e_1}\overline{c_{e_1}}=0$
and $A(2e_2)=c_{-e_2}\overline{c_{e_2}}=0$ each kill one arm; the mixed lags
$A(e_1\pm e_2)$ then kill a second, and $A(e_1)$, $A(e_2)$ finish it. Every
branch ends monomial, with no property of the coefficients used beyond the field
operations. Machine-confirmed at $L=5$, $6$ and $7$: 121 surviving assignments,
0 non-monomial at each (R041/R044/R045). **The unit's "at one lattice size above
the collapse threshold" caveat can be discharged into a second theorem.**

*The window is genuinely open at $L=4$.* The 5-point stencil at $L=4$ yields
1,561 surviving assignments and **160 non-monomial unitary generators** (R042),
because $2e_1 \neq 0$ but $-e_1 = 3e_1$ makes $A(2e_1)$ a two-term real
condition instead of a single product. This does not disturb the uniqueness
verdict — $L=4$ is already the admitted size — but it shows the family at $L=4$
is substantially larger than the 3-term stencil censused, and that the paper's
"the 5-point stencil (at one size above the collapse threshold)" scope line is
doing real work.

*The 9-point Moore stencil is the honest open.* Here the single-term structure
disappears: $A(2e_1)$ acquires three terms
($c_{-e_1}\overline{c_{e_1}} + c_{-e_1+e_2}\overline{c_{e_1+e_2}} +
c_{-e_1-e_2}\overline{c_{e_1-e_2}}$), so the collapse argument does not run,
while the pure-diagonal lags $A(\pm2e_1\pm2e_2)$ remain single-term and still
force $c_{e_1+e_2}c_{-e_1-e_2}=0$ and $c_{e_1-e_2}c_{-e_1+e_2}=0$. The question
is therefore **undecided by the present argument at every $L\ge5$**, and the
unit's `not_executed` line is correct to name it. A successor should sweep the
9-point stencil at $L=5$ with the diagonal offsets assigned first (the two
single-term lags prune at depth 2) before any claim that $L=4$ is unique for
*all* local stencils. As delivered, the theorem's honest scope is: **the 3-term
axis stencil (all $L$, all alphabets) and the 5-point stencil ($L\ge5$, all
alphabets, by the theorem above)**.

---

## 4. K3 — TRANSLATIONS-TRIVIAL IS FORCED, AND THE CHARGE-WITHOUT-MOMENTUM TENSION

**Forced. Derived and machine-confirmed.** For any coefficient map whatever,
$T_w M T_w^{-1} = M$ (R105: 200 arbitrary maps, 800 conjugations, 0 failures);
all 58 circulants have translation stabiliser $16 = |X|$ (R103), and the class
census under translations alone gives 58 singleton orbits out of 58 circulants
(R127). Reclassify per #208 — see MAJOR-4.

**The tension is real, and it is the unit's most interesting negative result.**
The transformation-type census (22 extended, 38 anchored, sizes $\{1,2,4\}$, all
reproduced — R122–R126) is carried entirely by the point symmetries, and the
class invariants (support, radius, transport level, projective period) are
constant on every orbit. But the translation group — the only part of the arena
that could carry a *momentum* label — acts with a single orbit type: trivially.
The census therefore produces **charge-like** invariants (internal, discrete,
constant on orbits) and **no momentum-like** invariant whatever. That is not a
defect of the measurement; it is forced by the decision to build the family from
translation-covariant circulants, which is the same decision that made the
two-point tables separation-indexed.

**What a successor needs for motion-carrying types.** The family must contain
generators that are *not* translation-invariant but whose translates are again
family members — i.e. the arena must act with non-trivial orbits *inside* the
family. Two routes are visible from this unit's own artifacts:

1. **Promote the brickwork controls to family members.** They already have
   stabiliser 8 (index-two, R104), so translations act with orbit size 2, and
   they carry nonzero defects (they are the substance of the 150 excluded). The
   obstruction is the realization gate, which currently admits only `FULL`. A
   successor that declares `OCC` a legitimate transport level gets
   motion-carrying types immediately — and the unit's §9 already flags this as
   "a question for a successor".
2. **Index the family by the character label.** Since every circulant is
   simultaneously diagonalised by the lattice characters, the momentum label
   lives on the *symbol* $\hat c(k)$, not on the generator's orbit. A
   transformation-type census taken on the symbol rather than on the matrix
   would recover a momentum grading without leaving the circulant family.

Either route also dissolves the tension with MAJOR-1's unique scale: the scale
is unique for *this* stencil class, not for the arena.

---

## 5. K4 — THE GATES

**The realization gate.** Levels reproduce exactly: NONE 1, OCC 5, OCC+AXIS 0,
FULL 58 (R073); 150 nonzero defects excluded below maximal (R078); total nonzero
738 $=$ 588 + 150 (R079). The classifications are correct. Two qualifications:
`FULL` is forced for every circulant (MINOR-6), and the exclusion set is exactly
the 6 declared controls — the gate excluded no member of the family under study.
The unit discloses the second point in §7; it should disclose the first.

**State motion.** 18 declared states, 18 distinct responses (R129/R130) — a real
measurement. The reconstruction half is forced (MAJOR-3).

**Two-point tables.** Equal-time $15/256$ at zero separation and $-1/256$
elsewhere reproduce as exact arithmetic on the uniform state (R106/R107). All 58
circulant transition tables are separation tables under the strict test (whole
class present with one value, not merely foldable) — 58/58 (R108). The scramble
control breaks it exactly as claimed: 0 of 2 scrambled transition tables are
separation tables (R109), both lose the full stabiliser (R111), and of 48
scrambled-vs-probe defect tables, 32 are nonzero and every one fails to be a
separation table while 16 are identically zero (R110). The composed-time split
$B(U_2U_1) = B(U_2)B(U_1) + \Delta^B$ holds identically; the coherence law holds
on 48 triples with 0 violations (R144) and is correctly registered FORCED.

**Light cone.** Vacuous — MAJOR-2. The radius profiles that replace it do
reproduce: six profiles, $(1,1,1,0)\times16$, $(1,2,1,0)\times8$,
$(2,2,2,0)\times18$, and 33 of 58 attaining the half-width (R112–R114).

**Projective-period gauge self-test.** Projective periods $\{1,2,4\}$, raw
orders $\{2,4\}$ (R118/R119), the period divides the raw order everywhere
(R120), and the self-test gives projective invariance at 42/42 with the raw
order moving at 27/42 (R121 — see MINOR-3). The raw-order *set* $\{2,4\}$ is
itself an artifact of the arbitrary gauge representative (`min` of the orbit
selects $-I$ for the identity class, raw order 2), which is exactly the point
the section makes; it is correctly labelled non-invariant.

---

## 6. K5 — THE INSTRUMENT

**What is genuinely strong.** A scratch replay of the unmodified instrument in a
symlinked mirror reproduces the **committed output and receipt byte-identically**
— 77/77 gates, 82/82 mutants killed by their declared target, exit 0. The
anchoring is real: 5 byte anchors, 10 path-value anchors each naming its JSON
path and expected value, 9 verbatim context windows each bound to a named
consumer. The `R3 Y1` lesson is properly learned — the defect gates are bound to
exact values, and `MUT-DEFECT-CENSUS-ZERO` (zero the censused cells, keep every
count) dies at `G-DEFECT-VALUE-CENSUS`. The AST guards (`G-SELF-COMPARE-GUARD`,
`G-NO-MUTANT-IDENTITY-IN-GATES`, `G-NO-FLOAT-AST`) are non-trivial and correct.
The verdict comparator genuinely shares no helper with the builder, and it does
catch asymmetric corruption — my first injection died at
`G-VERDICT-STRING-EQUALITY` precisely as designed.

**Where it does not reach.**

1. **Typed verdict qualifiers survive (MAJOR-6, demonstrated at exit 0).**
2. **The never-falsified census is under-counted.** Two waivers are registered
   (`G-DEFECT-DEFINITION-SHAPE`, `G-WAIVERS-VERIFIED`), both verified and both
   legitimate. But at least five further gates are analytically forced and are
   registered `MEASURED` with declared falsifiers that kill only by direct
   tampering: `G-TWOPOINT-LIGHTCONE` (vacuous above radius 0),
   `G-STATE-COEFFICIENT-BACKGROUND` (linearity),
   `G-CLASS-TRANSLATION-TRIVIAL` (circulant clause),
   `G-DEFECT-COLUMN-SUMS` (both composites stochastic),
   `G-TWOPOINT-STOCHASTIC` ($|U|^{\circ2}$ doubly stochastic for unitary $U$);
   and `G-DEFECT-NORMALIZATION`, `G-DEFECT-EQUIVARIANCE`, `G-DEFECT-REVERSAL`
   are identities of the Born map under permutation conjugation and transpose.
   The true never-falsified count is closer to **10** than to 2. Every one of
   them is *true*; the defect is registration, not arithmetic.
3. **The compliance sweep is prose (MAJOR-5).**
4. **Sampling.** `G-DEFECT-COLUMN-SUMS` reads 64 of 4,096 rows; the route-agreement
   gates read stride subsets; `G-DEFECT-NORMALIZATION` reads 20 generators;
   `G-DEFECT-EQUIVARIANCE` reads 2 shifts $\times$ 16 pairs. All the sampled
   claims hold on the full population — I checked (R083/R084, R143, R145) — so
   nothing is wrong; but the gates evidence less than the paper asserts.

**Repo integrity.** All 11 tracked hashes re-verified at close, unchanged. No
git operation was performed. Exactly one repository file was written: this one.

---

## 7. REPRODUCTION LEDGER (136 numbered)

- **R001–R022** — field, alphabet (25 elements, moduli $\{1,1/2,1/4\}$ by
  squared modulus, 8 each), locality sweep over $L\in\{2..9\}\times d\in\{1,2,3\}
  \times$ 2 connectives, the parity delta $-2$, the full order census
  $8/32/24/72/24/24/24/24/24$, and the matrix-vs-autocorrelation agreement on all
  15,625 order-4 candidates.
- **R023–R045** (21) — the collapse theorem's two algebraic identities on random
  triples; the 215-element rich-alphabet collapse at orders 5, 6, 7, 9; the
  Moore/von Neumann thresholds; admissible $=[4]$ vs $[2,4]$ vs $[2,3,4]$; the
  rational $\mathbb{Z}_3$ witness; the 5-point stencil at $L = 5,4,6,7$.
- **R061–R090** (30) — axes, per-axis generator counts, free gauge action, the
  58-circulant pool and its closed-form prediction, the 64-generator pool,
  dense-route unitarity, transport levels, and the full 4,096-row census with
  every headline count.
- **R091–R102** (12) — the closed-form family equals the swept family at all 9
  axes; the pool rebuilt from the parametrisation alone; the phase-route census
  with 0 disagreements; the collision-multiplicity distribution; the reachable
  two-term value set.
- **R103–R133** (31) — the translation forcing on arbitrary maps; equal-time
  correlators; separation tables and the scramble control; radius profiles and
  the light-cone vacuity probe; periods and the gauge self-test; the class
  censuses at both groups; state motion and the reconstruction forcing; the K1
  value-by-multiplicity split.
- **R134–R147** (14) — the 588 combinatorial derivation and its closed form; the
  matched-coordinate table 616/1024; max defect radius on both sides; the defect
  algebra (identity, coherence on 48 triples, gauge invariance); the five-point
  node count under both offset orderings.
- **R148–R150** — the anchored link $(1,1)$ inside the Moore ball, outside the
  von Neumann ball (the MAJOR-1 repair).
- **R151–R153** — the point group closes on the axis set and
  $\mathrm{gens}(f(a)) = f(\mathrm{gens}(a))$, 0 mismatches (the FULL forcing).

Out-of-band (20): 11 sha256 verifications (re-run at close, all unchanged); the
scratch plain run reproducing the committed output and receipt byte-identically
with 77/77 gates and 82/82 on-target kills (4); the two injection runs (2); the
paper-claim coverage audit, 13 rendered against 66 distinct numeric tokens (2);
the compliance/waiver-ledger audit (1).

**Numbers that moved under attack: none.** Numbers that were *understated*: the
census's derivability (K1), the collapse theorem's reach to the 5-point stencil
(K2), and the alphabet-independence of the Moore-relative uniqueness (K2).

---

## 8. VERDICT

**ACCEPT-WITH-FIXES.** The unit's measured content is correct and reproduces
from scratch by primitives it does not share. Its central object — a nonzero
composition defect on a spatially structured indivisible family, 588 of 3,364
pairs at maximal transport with eight exact rational values — is not merely
confirmed but **derived**, and the derivation makes the result stronger and
sharper than delivered.

Six repairs are required before the unit leaves GREEN-UNREVIEWED:

1. **MAJOR-1** — delete both "both connectives" claims; reclassify the
   connective as FORCED by `PV-I7-LINKS`; gate the von Neumann exclusion; add
   `CONNECTIVE=MOORE` to `SCOPE`. *(This is the one false sentence in the paper;
   its repair strengthens the headline.)*
2. **MAJOR-2** — register the light-cone gate as a disclosure and remove or
   qualify its verdict segment.
3. **MAJOR-3** — split the state-motion gate; forced half disclosed, measured
   half kept.
4. **MAJOR-4** — reclassify the translations-trivial clause as forced; keep the
   control clause measured; re-word §6.
5. **MAJOR-5** — make the compliance statuses computed predicates with
   falsifiers; correct the false #20 row; extend `paper_claims` coverage.
6. **MAJOR-6** — derive the verdict's qualifiers from measured rows and add a
   per-qualifier flip probe.

Recommended, not required: fold the K1 derivation into §4.2; promote the 5-point
$L\ge5$ collapse to a stated theorem; state the 9-point stencil as the named
open; and record the charge-without-momentum reading of §6 as a finding in its
own right, with the two successor routes named in §4 above.

**Single-file write confirmed:** `v14/review-r4-operator.md` is the only
repository file this review created or modified. No git operation was performed.
All hostile execution took place on symlinked scratch mirrors under
`scratchpad/r4op/`.

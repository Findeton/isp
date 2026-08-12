# ACT (paper-34) — K1 OPERATOR-LENS REVIEW

**Seat:** K1, the operator lens — the mathematics itself, rebuilt from the
parents' definitions with code sharing nothing with `v14/code/act_exact.py`.
**Stance:** hostile; every number assumed wrong until independently rebuilt.
**All rulings below are candidate until adjudication.**

**Objects, sha256-12, verified at open AND at close (all five match):**

| object | sha256-12 |
|---|---|
| `v14/paper-34-act.md` | `3fbf109f0d9b` |
| `v14/code/act_exact.py` | `02df3f00f788` |
| `v14/code/act_output.txt` | `9299f80db2d8` |
| `v14/code/act_receipt.json` | `f0617d1687a0` |
| `v14/note-act-pin.md` (pin) | `766c603c6dbc` |

Parents re-hashed against the paper's own claims, all matching: paper-27-smu
`6df0db523d32`, smu_exact `126912ae7142`, smu_receipt `0d6fbadd756d`,
paper-23-measure `79cc67b4f6cd`, r5m_measure_exact `faf353385905`,
r5m_measure_receipt `c9edf97a5533`, paper-18-gauge-rung `62cfe5689d2c`,
r5_gauge_exact `0d98de793b79`, r5_gauge_receipt `0c02b7684e5b`,
giter_receipt `42255f50328a`.

---

## GRADE: **AWF** (accept with fixes)

The census is sound and its numbers are right. I rebuilt all six rows of the
form census from the R5/SMU/paper-23 definitions on primitives that share
nothing with the instrument, and **every one of the six coupling counts, six
orbit counts, six Burnside sums, six gauge-image orders, six chart-stabiliser
orders and six acting-group orders reproduced exactly**, along with the two
gauge-only counts by an independently derived character route. I additionally
derived two exact closed forms the unit does not have, which reproduce the two
*full* anchored counts at full size — a genuine second route where the paper
discloses it has only a reduced-arena validation of the machinery. No computed
number in this unit was found to be wrong. Every one of the 87 distinct
numerals in the paper (403 occurrences) is backed by the receipt.

Two **majors** stand, both of the same species and neither of them a wrong
number: a headline claim whose *own definitional second leg is never measured
and fails when measured*, and a verdict-level claim contradicted by the unit's
own measured exponent. Both have cheap, headline-preserving repairs; neither
touches a single published figure.

---

## 0. What I did, and how independent it is

**Independent primitives.** My rebuild carries $\mathbb{Q}(\zeta_8)$ as integer
4-tuples over $(1,z,z^2,z^3)$ with an *explicit positive integer denominator*
(the instrument uses a different representation); enumerates the coin family
exhaustively over the alphabet's fourth power **factorised by columns**
($U^\dagger U=I \iff$ the two columns are orthonormal), a different route from
the instrument's; represents a stencil-group element as a *(slot permutation,
per-slot coin permutation)* pair and counts fixed points by cycle decomposition;
and computes orbits by union-find over generators. Nothing is imported from
`act_exact.py`, no literal is copied from it, and no product of it is re-read.

**Honesty note on blindness.** The rebuild is *code-independent but not blind*:
I read the receipt before writing it. The independence is in the primitives and
the routes, not in ignorance of the targets. Both majors below were found by
running measurements the unit does not make — not by comparing numbers.

**What is out of reach, and at what reduction.** At the plaquette and site
grains the datum space is $640^4 = 167{,}772{,}160{,}000$ and I did **not**
enumerate its orbits at full size. What I did verify at those grains:

1. the acting group built from generators and its order confirmed by closure
   (1024 / 4096 / 8192 / 32768 distinct actions);
2. Burnside by exact cycle-decomposition fixed-point counting over **every**
   group element, with divisibility of the sum by the group order required;
3. my Burnside machinery validated against exhaustive brute-force union-find on
   **my own 18-coin reduced arena** (closed under twist and swap; $18^4 =
   104{,}976$ tuples) at all six rows — a different reduced arena from the
   unit's declared 19-coin one;
4. two independent **closed forms in exact integers** (see §4.2), which
   reproduce both large *anchored* counts at full size.

---

## 1. MAJORS

### MAJOR-1 — The Wilson-shape membership claim is established against only one of the two legs of the allowed space's own definition, and it fails on the other.

**What the paper claims.** §3 defines the allowed space as *"the set of
positive-rational functions on that grain's stencil datum that are constant on
the orbits of the **stencil group**"* — and the census's own `acting group`
column is that group: the gauge image **and** the chart stabiliser (order
$512\times2 = 1024$ at PLAQUETTE-ANCHORED, $512\times8=4096$ at
PLAQUETTE-EXTENSION). §5.1 then claims:

> The trace is invariant under conjugation by the corner phases, so any
> positive-rational function of it is an admissible weight system at the
> plaquette grain: 8192 checks against every one of the plaquette's gauge
> elements, 0 failures.

and the verdict carries
`(a)WILSON-SHAPE=IN-THE-ALLOWED-SPACE-AT-EXACTLY-1-OF-3-DECLARED-GRAINS`.

**The measurement.** The 8192 checks are $512$ gauge elements $\times$ 16
declared plaquette data (I confirmed in source at `act_exact.py:2049–2061` that
the data are genuine non-uniform 4-tuples, so the gauge leg is honestly
measured — that arm is clean, and my own 512 × 60 = 30,720-check rerun on my own
data found **0 failures** too). **No chart element is ever applied to the
trace.** When I apply them:

| reading | acting group | (datum, group element) checks | trace NOT constant |
|---|---|---|---|
| PLAQUETTE-ANCHORED | 1024 | 61,440 | **29,184** |
| PLAQUETTE-EXTENSION | 4096 | 245,760 | **193,536** |

The anchored case is the cleanest possible witness, and it is exact. The
anchored chart stabiliser is $\{1,\sigma\}$ with $\sigma$ the diagonal
reflection $A=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$,
$v=(0,0)$; it carries **no** link reversal, so it acts on the stencil datum as
the bare permutation $(U_b,U_r,U_t,U_l)\mapsto(U_l,U_t,U_r,U_b)$. Over 300
declared plaquette data:

```
A=((1,0),(0,1)) v=(0,0):  equal 300   conjugate   0   neither   0
A=((0,1),(1,0)) v=(0,0):  equal  21   conjugate 279   neither   0
```

The mechanism is exact and provable, not statistical: $\sigma$ reverses the
boundary loop, so $W \mapsto (PWP^{-1})^{-1}$ and
$\operatorname{tr}W \mapsto \overline{\operatorname{tr}W}$. That differs from
$\operatorname{tr}W$ whenever the trace is not real — and the trace is real only
on the carrier: **376 of 400** random plaquette data have a trace outside the
real subfield $\mathbb{Q}(\sqrt2)$. At the extension reading it is worse: five
of the eight stabiliser elements send the trace to **neither** the trace nor its
conjugate on the large majority of data (e.g. `A=((0,1),(-1,0)) v=(0,1)`:
equal 5, conjugate 9, **neither 286** of 300).

**Consequence.** A non-constant positive-rational function of the trace is
*not* constant on the stencil group's orbits, so it is **not** a member of the
allowed space as this paper defines it. The sentence "any positive-rational
function of it is an admissible weight system at the plaquette grain" is false
as written, and the same false inference is engraved in the gate's own claim
text at `act_exact.py:2064–2072` ("...which is what makes any positive-rational
function of it an admissible weight system"). Compounding it, the positive arm
is not computed at all: `grains_admitting = ["PLAQUETTE"]` is a **typed
literal** (`act_exact.py:2102`), and the gate's `len(grains_admitting) == 1`
clause is therefore vacuous. Only the two *exclusions* are measured, by the
witness pairs — and those I confirm (see §4.5).

**What survives, measured.** Everything downstream. The trace is constant on
the induced classes at **both** readings (0 of 136 and 0 of 80 classes fail),
because the constant-datum locus is where $\sigma$ acts trivially. So the 11
distinct values, the span of 10 of 135, the three published expectations and
the whole falsifier section are untouched. And a non-trivial Wilson family does
survive inside the allowed space: at the anchored reading the orbit relation on
trace values is *exactly* "identify $t$ with $\bar t$" (0 of 300 "neither"), so
the admissible Wilson weights are exactly the **conjugation-symmetric**
positive-rational functions of the trace — and on the carrier, where the trace
is real, that restriction costs nothing.

**Severity.** Major: a headline row whose positive arm is asserted rather than
measured, justified by an inference that measurement refutes. Not a wrong
number.

**R-ACT-OP-1 (binding repair, exact licensed replacement for §5.1's sentence):**

> The trace is invariant under conjugation by the corner phases, so any
> positive-rational function of it is invariant under the plaquette's whole
> gauge image: 8192 checks against every one of the plaquette's gauge elements
> at 16 declared plaquette data, 0 failures. It is *not* invariant under the
> plaquette's chart stabiliser: the anchored stabiliser's one non-identity
> element reverses the boundary loop and carries the trace to its complex
> conjugate, which differs from it on 279 of 300 declared plaquette data,
> because the trace is real only on the carrier. The admissible Wilson weights
> are therefore exactly the conjugation-symmetric positive-rational functions
> of the trace, and on the carrier the restriction costs nothing: the family
> still spans 10 of the 135 couplings the carrier admits, at 11 distinct trace
> values.

**R-ACT-OP-2:** make `grains_admitting` a computed object — measure membership
at all six (grain, reading) rows against the **full acting group**, not the
gauge image, and publish the row at 6 rows like every other census row.
Licensed verdict segment:
`(a)WILSON-SHAPE=GAUGE-ADMISSIBLE-AT-EXACTLY-1-OF-3-DECLARED-GRAINS-THE-PLAQUETTE-ONE-AT-8192-CHECKS-0-FAILURES-AND-COVARIANT-ONLY-IN-ITS-CONJUGATION-SYMMETRIC-PART;...`
(remainder of the segment unchanged).

---

### MAJOR-2 — "The reachable measures are not grain-relative" / "the entire difference sits in the fibre" is false, and is contradicted by the unit's own measured exponent $e = 32/16/16$.

**What is claimed.** The receipt seals
`grain_degeneracy.verdict = "THE-COUPLING-COUNT-IS-GRAIN-RELATIVE-THE-REACHABLE-MEASURES-ARE-NOT"`,
its gate's claim text (`act_exact.py:1975–1979`) says *"the measures the three
grains can reach on this carrier are the SAME set"*, and the paper renders it
at §6:

> The partition is the same 136 classes at all three grains while the coupling
> counts differ by six orders of magnitude. **The entire difference sits in the
> fibre**, and the carrier cannot see one number of it.

**Why it is false.** The unit itself measures and publishes
`GIBBS=...WITH-E=32/16/16-AT-THE-THREE-GRAINS`, and it characterises the image
correctly as *the $e$-th power sublattice of the class-constant measures*.
$32$nd powers are a **proper** subset of $16$th powers, so the images differ as
sets. Exhibited witness, computed exactly:

> Take the class-constant, full-support probability measure that raises one
> class of size 8 by $2^{16}$ and leaves the other 135 classes at 1
> ($Z = 8\cdot2^{16} + 632 = 524{,}920$). Its class ratio is $2^{16}$.
> $2^{16}$ **is** an exact 16th power ($=2^{16}$) and **is not** an exact 32nd
> power ($2^{1/2}\notin\mathbb{Q}$). So this measure is in the image at the
> plaquette and site grains and **not** in the image at the link grain.

The reachable *set* is therefore grain-relative; what is not grain-relative is
the reachable **dimension** (135/79) and the **induced partition** (136/80) —
both of which I confirm at all six rows. The gate's predicate tests only that
the induced class counts coincide and the coupling counts are distinct; it
never tests set equality of the images, so the false half of its claim text is
un-gated. This is the #87 species (a gate whose claim exceeds its predicate)
with a #34 reachability face (the falsifiable half is never reached).

**Severity.** Major: a sealed verdict string and a bolded paper sentence, both
false, both refuted by the unit's own published number.

**R-ACT-OP-3 (binding, exact licensed replacement for the §6 sentence):**

> The partition is the same 136 classes at all three grains while the coupling
> counts differ by six orders of magnitude. The entire difference in the
> **count** sits in the fibre, which the carrier cannot see. The reachable sets
> themselves are not identical: the exponent is 32 at the link grain and 16 at
> the other two, so the link grain's image is the proper subset of the others'
> cut out by one further square root — the measure that raises one class by
> $2^{16}$ is reachable at the plaquette and site grains and not at the link
> grain. What is grain-independent is the reachable **dimension** and the
> induced partition, not the reachable set.

**R-ACT-OP-4 (binding):** change the sealed verdict to
`THE-COUPLING-COUNT-IS-GRAIN-RELATIVE-THE-REACHABLE-DIMENSION-AND-THE-INDUCED-PARTITION-ARE-NOT`,
amend the gate's claim text to match its own predicate, and add a
per-object gate that *measures* the image inclusion (the exhibited witness
above reaches it, so the gate is reachable and the falsifier is real).

---

## 2. MINORS

**MINOR-1 — "free module ... of rank the orbit count" is not the right algebra.**
§3: *"the allowed space is a free module over the multiplicative positive
rationals, of rank the orbit count."* $\mathbb{Q}_{>0}$ is a group, not a ring;
a module over it is undefined, and as an abstract abelian group
$(\mathbb{Q}_{>0})^{136}$ has infinite rank. The operative claim — the number of
free multiplicative parameters modulo the global scalar is $\text{orbits}-1$ —
is exactly right. Licensed: *"the allowed space is the direct power of the
multiplicative positive rationals with one factor per orbit, and its number of
free multiplicative parameters modulo normalisation is the coupling count."*
The same word does double duty in the fibre column, where "rank $-$ dimension"
subtracts a parameter count from a simplex dimension; both count free
parameters, and the fibre numbers are right ($265{,}121{,}343-135 =
265{,}121{,}208 = 265{,}121{,}344-136$, verified at all six rows), but the
mixed vocabulary should be named once.

**MINOR-2 — the generator-exhibition argument proves less than it claims.**
§3: 135 generators *"every one of them measured non-constant, so none is a
scalar and none is redundant with the normalisation, and they are pairwise
distinct as functions."* Non-constancy and pairwise distinctness do not
establish independence modulo normalisation; the coordinate structure does
(the 136 orbit coordinates are free, so any 135 of them generate the quotient
by the diagonal). The fact is true; the stated reason does not carry it. One
added clause fixes it.

**MINOR-3 — §4 covers two of the three grains.** The section is titled "what
product-invariance costs at each grain" and measures the link grain (equality,
exhausted: 576 of 576 detected, 0 of 64 false — I reproduce both) and the
plaquette grain (strictly weaker, coboundary exhibited — I reproduce the
identity at 640 of 640 carrier and 64 of 64 declared non-uniform
configurations). The **site** grain is neither measured nor named. It admits
the identical construction: every link lies in exactly 2 stars, so the same
$\pm1$ role assignment gives a product-one coboundary. One row, one sentence.

**MINOR-4 — chart transitivity is published for links and plaquettes but not
for sites,** though the site-grain census leans on it exactly as the other two
do (`chart.link_orbits_anchored = 1`, `chart.plaquette_orbits_anchored = 1`, no
site key). It is true and cheap — the 16 translations act simply transitively
on the 16 sites, which I confirmed — but by this unit's own "measured, not
argued" standard it should be a published count.

**MINOR-5 — the Wilson membership row is reported per grain while the census is
per (grain, reading).** `in_the_allowed_space_at_grains: ["PLAQUETTE"]` and
"1 of 3 declared grains" collapse the reading axis that every other row keeps
at 6. Once MAJOR-1's covariance leg is applied the membership genuinely differs
by reading (at the anchored reading the obstruction is exactly conjugation; at
the extension it is not), so the collapse is not merely cosmetic.

**MINOR-6 — the two large *full* counts have no second route at full size.**
§13 discloses this honestly (the reduced arena validates the machinery, the
character route covers only the gauge-only counts). I can remove the gap rather
than merely note it, and offer both closed forms as a strengthening (§4.2):
$N_{\text{site,anch}} = (136^4 + 136^2)/2$ and
$N_{\text{plaq,anch}} = (136^4 + 7\cdot 72^4 + 23{,}680)/2$, both exact, both in
the same two constants the character route already uses, both covering the
**full** acting group.

**MINOR-7 (observation, not my seat) — `waiver_ledger` arithmetic reads
oddly:** `gates_closed: 37`, `covered_by_a_declared_falsifier: 37`,
`under_a_registered_forcing: 1`, `uncovered: []`, and `the_forcings` carries 2
entries. It resolves if the forcing attaches to a *late* gate outside the 37,
but the denominators should be made explicit. Flagged for K3.

---

## 3. WHAT I ATTACKED AND COULD NOT BREAK

- The **§4 link-grain theorem** (product-invariance $=$ local invariance) is a
  correct theorem, including the step that carries it: each per-link ratio is
  constant by varying one link at a time, the twist has order 8, so the ratio
  is a positive rational 8th root of unity and hence 1. Crucially the argument
  forces invariance under the **full** $\mathbb{Z}_8$ twist including the odd
  one, even though the *constant* odd twist is not globally realisable — which
  is precisely the unit's mechanism, and it is sound.
- The **odd-twist prohibition**: a constant twist $c$ is realisable iff
  $Lc\equiv0 \pmod 8$, so exactly $\{0,2,4,6\}$; the odd twist is a bijection of
  the 640-coin carrier and is not a gauge transformation of this torus. Every
  consequence I checked holds: 72 (anchored) and 40 (extension) classes hold
  exactly 2 gauge orbits each; no orbit straddles a class at either reading;
  $207-135=72$ and $119-79=40$.
- The **falsifier**. The off-diagonal quartic sign is a genuine gauge
  observable at both readings, and its class averages are 0 on *every* class —
  the odd twist negates it on classes of size $>1$, and singleton classes are
  the diagonal coins where it is 0 outright. Range $[-2,2] \to [0,0]$, exactly
  as published. Its "not a blanket verdict" companion also holds: the loop
  trace's extreme values ($0$ and $4$, and both surd extremes) sit on
  **singleton** classes, so its range is unchanged — I verified the class sizes.
- The **arithmetic obstruction**. $3/2$ is not an exact 16th or 32nd power (in
  lowest terms $p^n=3, q^n=2$ forces $n=1$). The closure witness is not merely
  reproducible — my own integer bisection at denominator $10^5$, run without
  reading theirs, returned **the same numerator 101275**, with
  $|(101275/10^5)^{32} - 3/2| \approx 6.63\times10^{-5} < 10^{-4}$, exact, no
  float anywhere.
- The **price frame** against SMU's committed bytes: 207 / 119 / 639 and the
  208 / 120 orbit counts are SMU's own published values (verified in
  `smu_receipt.json` and in SMU's verdict string), and the law-native sector law
  $15/38,\,5/19,\,13/38$ likewise — from which the required per-coin
  diagonal:antidiagonal ratio $3/2$ falls out on recomputation.
- **Numeral sweep, digests, verdict.** All 87 distinct numerals (403
  occurrences) in the paper appear in the receipt; 0 unbacked. The paper's
  single fenced block is byte-equal to the output's last line and to
  `receipt.verdict`; `verdict_head` is a true prefix of it. `paper_sha256_12`,
  `code_sha256_12` and `pin_sha256_prefix` all match the tree.

---

## 4. THE RECOMPUTATION RECORD

### 4.1 The form census — six rows, all exact, my own routes

| grain | reading | gauge image | chart stab | acting group | Burnside sum | orbits | couplings | verdict |
|---|---|---|---|---|---|---|---|---|
| LINK | ANCHORED | 8 | 1 | 8 | 1,088 | 136 | 135 | reproduced |
| LINK | EXTENSION | 8 | 4 | **16** | 1,280 | 80 | 79 | reproduced |
| PLAQUETTE | ANCHORED | 512 | 2 | 1,024 | 271,484,256,256 | 265,121,344 | 265,121,343 | reproduced |
| PLAQUETTE | EXTENSION | 512 | 8 | 4,096 | 271,610,019,840 | 66,311,040 | 66,311,039 | reproduced |
| SITE | ANCHORED | 4,096 | 2 | 8,192 | 1,401,325,617,152 | 171,060,256 | 171,060,255 | reproduced |
| SITE | EXTENSION | 4,096 | 8 | 32,768 | 1,422,084,866,048 | 43,398,586 | 43,398,585 | reproduced |

Every Burnside sum divides its group order. The "half the naive product"
disclosure is confirmed: at LINK-EXTENSION the chart stabiliser has order 4
(identity, the along-link reflection, and two direction-reversing elements) but
its image in the coin-map group is $\{1,S\}$, so $8\times2 = 16$ distinct
actions, not $8\times4 = 32$.

### 4.2 Second and third routes — including two the unit does not have

- LINK-ANCHORED: BRUTE-FORCE-UNION-FIND **136** = BURNSIDE **136** =
  ORBIT-STABILIZER-SUM **136**; profile $[(1,64),(8,72)]$.
- LINK-EXTENSION: **80 / 80 / 80**; profile $[(1,8),(2,28),(8,16),(16,28)]$.
- Character route, rebuilt in $\mathbb{Q}(\zeta_8)$ from
  $F(k)=\sum_t \omega^{kt} f(t)$ with $f = [640,64,\dots,64]$, giving
  $F(0)=1088$, $F(k\neq0)=576$:
  - plaquette gauge-only $= \tfrac18\sum_k F(k)^2F(-k)^2 = 271{,}472{,}132{,}096$,
    $/512 = \mathbf{530{,}219{,}008} = 136^4 + 7\cdot72^4$;
  - site gauge-only $= 1088^4/4096 = \mathbf{342{,}102{,}016} = 136^4$.
  The one linear relation is confirmed structurally: the plaquette's four
  twists satisfy $s_1+s_2=s_3+s_4$ (image of order $8^3$), the site star's four
  do not (full $\mathbb{Z}_8^4$).
- **New — closed forms for the two full anchored counts** (offered as a
  strengthening, MINOR-6). Under the anchored stabiliser $\sigma$ (two 2-cycles
  on the stencil slots), averaging $|\mathrm{Fix}(h\sigma)|$ gives:
  - site: $(136^4 + 136^2)/2 = (342{,}102{,}016 + 18{,}496)/2 = \mathbf{171{,}060{,}256}$;
  - plaquette: $\sum_{h\in H} f(s_1{+}s_4)f(s_2{+}s_3) = 12{,}124{,}160$,
    $/512 = 23{,}680$, so $(530{,}219{,}008 + 23{,}680)/2 = \mathbf{265{,}121{,}344}$.
- Reduced arena, **mine** (18 coins, closed under twist and swap, distinct from
  the unit's 19): Burnside vs exhaustive brute force agree at all six rows —
  18/18, 13/13, 52,650/52,650, 13,536/13,536, 52,650/52,650, 14,706/14,706.

### 4.3 The arena, the carrier, the classes

Alphabet 25; coins **640** (exhaustive over $25^4$), sectors 64 DIAGONAL / 64
ANTIDIAGONAL / 512 BALANCED, unitary by the second route $UU^\dagger=I$ on all
640; 17 of the 25 alphabet elements used; 80 admissible normalised rows; 16
sites, 32 links, 16 plaquettes, every link in exactly 2 plaquettes; chart order
32 / 128, transitive on links (32 of 32) and plaquettes (16 of 16).

Residual gauge on the carrier: order 4, **208** orbits, profile
$[(1,64),(4,144)]$, simplex dimension 207; order 8, **120** orbits, profile
$[(1,8),(2,28),(4,24),(8,60)]$, dimension 119. Induced classes **136** and
**80**, profiles $[(1,64),(8,72)]$ and $[(1,8),(2,28),(8,16),(16,28)]$ — and the
same 136 / 80 at **all three grains**, with exponents 32 / 16 / 16. Extreme
points 64 vertices $+$ 72 edge-midpoints (anchored), 40 $+$ 40 (extension).

### 4.4 Wilson, on the carrier

Trace in $\mathbb{Q}(\sqrt2)$; **11** distinct values, reproduced verbatim
against the receipt's list: $0,\ \tfrac14,\ 1,\ \tfrac54-\tfrac{\sqrt2}2,\
\tfrac54,\ \tfrac54+\tfrac{\sqrt2}2,\ 2-\sqrt2,\ 2,\ 2+\sqrt2,\ \tfrac94,\ 4$.
Rational parts range $[0,4]$, surd parts $[-1,1]$, $\sum = 832 \Rightarrow
13/10$. Plaquette-independent, verified with **full 16-site operators** at 16
plaquettes on 10 declared carrier configurations. Flat coins 8, non-flat **632**
— matching R5's own published figure — and 8 coins at the top value 4.
Class-constant at both readings. Family dimension $11-1 = 10$ inside 135.

### 4.5 Exclusions, falsifier, expectations, targets

Witness pairs confirmed: two configurations agreeing on a link's own datum, and
two agreeing on the whole star of $(0,0)$ (the plaquette links $((1,0),1)$ and
$((0,1),0)$ lie outside that star), carry different loop traces.

All twelve falsifier rows reproduced exactly — six observables $\times$ two
readings, each confirmed a genuine gauge observable, with both ranges matching:
trace-rational $[0,4]\to[0,4]$, trace-surd $[-1,1]\to[-1,1]$, **quartic sign
$[-2,2]\to[0,0]$ PINNED**, and the three indicators $[0,1]\to[0,1]$. The defect
indicator was rebuilt from the seed's own formula
$\Delta^B(U_2,U_1)=B(U_2U_1)-B(U_2)B(U_1)$ at SAME-LINK and returns **384**
defect-carrying coins, all balanced — R5's published number. Orbit indicators:
208 observables, **144** pinned, 64 unpinned, pinned top exactly $1/2$;
extension 120, **80**, 40, top $1/2$.

Expectations, all three exact: $13/10$ (null, $e=32$);
$4294967399/4294967375$ (2 on one size-8 class whose trace rational part is 1 —
there are 8 such classes — with $Z = 8\cdot2^{32}+632 = 34{,}359{,}739{,}000$,
masses $536870912/4294967375$ and $1/34359739000$, summing to 1);
$262244/65615$ (2 at the top trace value, $e=16$, $Z = 8\cdot2^{16}+632 =
524{,}920$). Target census: 1 of 6 reachable, at both exponents, with all three
obstruction species reproduced (ARITHMETIC / SUPPORT / SYMMETRY).

### 4.6 Recomputation count

**187 independently recomputed quantities**, counting each measured value once:
21 arena and group-structure quantities; 36 census-row quantities (6 rows ×
6 columns); 2 gauge-only counts; 4 additional routes at the link grain; 5
character-route and closed-form evaluations; 6 reduced-arena agreements; 14
carrier/class/orbit-profile quantities; 6 induced-partition rows and 3
exponents; 6 locality quantities; 17 Wilson quantities; 12 falsifier rows plus
2 orbit-indicator families; 3 expectations plus 4 supporting constants; 4
arithmetic-obstruction quantities; 12 target-census verdicts; 6 fibre rows; 19
hostile-probe measurements (probes 1–6 and M1–M4); 5 digest/verdict/numeral
checks. **Zero false computed numbers found.** Both majors are prose- and
verdict-level claims, not numbers.

---

## 5. THE LICENSED SENTENCES, COLLECTED

Anything I re-rule, in the exact words that may be lifted:

1. **§5.1, replacing the membership sentence** — R-ACT-OP-1, quoted in full in
   MAJOR-1 above.
2. **The verdict's (a) segment** — R-ACT-OP-2:
   `(a)WILSON-SHAPE=GAUGE-ADMISSIBLE-AT-EXACTLY-1-OF-3-DECLARED-GRAINS-THE-PLAQUETTE-ONE-AT-8192-CHECKS-0-FAILURES-AND-COVARIANT-ONLY-IN-ITS-CONJUGATION-SYMMETRIC-PART`
   (remainder unchanged).
3. **§6, replacing "The entire difference sits in the fibre..."** —
   R-ACT-OP-3, quoted in full in MAJOR-2 above.
4. **The sealed `grain_degeneracy.verdict`** — R-ACT-OP-4:
   `THE-COUPLING-COUNT-IS-GRAIN-RELATIVE-THE-REACHABLE-DIMENSION-AND-THE-INDUCED-PARTITION-ARE-NOT`.
5. **§3, replacing "a free module over the multiplicative positive rationals,
   of rank the orbit count"** — MINOR-1: *"the direct power of the
   multiplicative positive rationals with one factor per orbit, whose number of
   free multiplicative parameters modulo normalisation is the coupling count."*

## 6. WHAT THIS SEAT AFFIRMS

The heart of the unit — the characterisation of the allowed space as the
orbit-constant positive-rational functions on the stencil datum, the six
coupling counts, the grain-relativity of the count, the odd-twist prohibition
and the price reduction 207→135 / 119→79, the Gibbs image and its fibre, and
the falsifier hit — is **correct as measured**, and I could not move a single
published number. The two majors are claims that outran the measurements
behind them; both repairs preserve every figure in the paper.

---

*Reviewer: K1, the operator lens. Single repo write: this file. Git read-only.
Object hashes re-verified at close: paper `3fbf109f0d9b`, code `02df3f00f788`,
output `9299f80db2d8`, receipt `f0617d1687a0`, pin `766c603c6dbc` — all five
unchanged from open.*

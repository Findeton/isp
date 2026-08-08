# COC — HOSTILE REVIEW R2 (EFFECTUS / CATEGORICAL LENS)

**Reviewer:** R2, structural/conceptual lens.
**Date:** 2026-08-08.
**Protocol:** `v13/note-coc-hostile-protocol.md` (FROZEN, v13 #230), kill-shots
K1–K5 binding.
**Objects reviewed, SHA-256 verified before and after all work:**

| file | sha256-12 | verified |
|---|---|---|
| `v13/paper-coc-cocycle.md` | `3ecd933ad1d9` | yes |
| `v13/code/coc_cocycle_exact.py` | `0c0592a15d2e` | yes |
| `v13/code/coc_cocycle_output.txt` | `cbbece149650` | yes |
| `v13/code/coc_cocycle_receipt.json` | `6f99d790e021` | yes |

**Independence.** Base G and the whole COC atlas were rebuilt from the
**published prose only** — GEN §§2.1–2.5 (carrier, quaternions, ψ, `V = H·Q`,
settings, frames, checkpoints, the 162/216 scopes) and COC §§2–6 (chart orbit,
four-clause predicate, triangle, defect, bigon comparator). Nothing was
imported from `v13/code/`. Own scripts: `r2_base.py`, `r2_check1.py`,
`r2_check2.py`, `r2_attack1.py`, `r2_attack2.py`, `r2_attack3.py`,
`r2_attack4.py`, `r2_check5.py` in the session scratchpad. The instrument
itself was additionally executed **read-only** (no `--falsification-selftest`,
so no artifact is written) and three mutants were run; the four frozen SHAs
were re-verified afterwards and are unchanged.

**Recomputation count: 118 independent recomputations.** Every load-bearing
number in the paper was recomputed from scratch. **Numerical mismatches: 0.**
No number in this paper is wrong. The findings below are all about what the
numbers *mean*.

---

## 0. The numbers table (claimed vs. mine)

| quantity | claimed | mine |
|---|---|---|
| relabelling / extension scope | 162 / 216 | 162 / 216 |
| admitted after $j_0$ / at the extension | 2 / 8 | 2 / 8 |
| $D$: order, fixed configurations | 2, 45 | 2, 45 |
| chart family, distinct at every setting | 4, 4×6 | 4, 4×6 |
| read-time comparisons / collisions | 144 / 0 | 144 / 0 |
| FULL / REAL drawn over all ordered pairs | 240 / 160 | 240 / 160 |
| committed pair $F_2\to F_1$ | 18 / 8 | 18 / 8 |
| multiplicity histogram | 32 / 208 / 48 | 32 / 208 / 48 |
| GP-E@$t{=}0$ six-row table | as printed | identical |
| admissible triangles | 1,824 | 1,824 |
| independent-route census size | 1,824 | 1,824 |
| per-cell census (all 24 cells) | as printed | identical |
| defect set | 1: 1,248 / $W$: 576 | 1: 1,248 / $W$: 576 |
| bigon group: links/rank/closed/order | 9/2/8/1 and 13/6/364/4 | identical |
| element fixed points at GP-E/F | 81, 9, 45, 9 | 81, 9, 45, 9 |
| defects outside the group | 0 of 1,824 | 0 of 1,824 |
| §6 iff: both clauses | 0 / 0 violations | 0 / 0 |
| coordinates with / without a bigon | 6 / 18 | 6 / 18 |
| degenerate triangles; self-map failures | 152; 0 | 152; 0 |
| R1 candidate maps; admitted | 32; 0 | 32; 0 |
| equivariant completion: charts, triangles | 4,4,4,4,2,2; …,0,0 | identical |
| completion family: total / collapse / support | 40,320 / 96 / 40,224 | identical |
| extension: drawn maps; coords changed | 400; 0 | 400; 0 |
| receipt totals | 19 anchors, 29 gates, 25 must-pass, 4 disclosures | identical |
| read-only instrument run | — | 19 anchors, 28 gates, 0 failures |
| mutants spot-checked | 3 named gate-kills | identical |

---

## 1. THE FORCING THEOREM (the finding everything else hangs on)

I derived, and then verified exhaustively, a structure theorem the paper does
not have. It is short.

**Lemma (equivariance).** For $\sigma,\tau$ in the declared admitted set $S$
and committed frames $X, Y$, the four-clause predicate satisfies

$$\mathrm{Adm}(\sigma.X,\ \tau.Y)\;=\;\tau\cdot\mathrm{Adm}(X,Y)\cdot\sigma^{-1}$$

at every coordinate and under every rule. *Reason:* each clause is stated on
conjugated legs and pushed-forward laws, and $M\mapsto\tau M\tau^{-1}$ is a
bijection that preserves Born-key equality and multiset equality; $\sigma$ fixes
$j_0$, so clause 1 transports too. Uniqueness therefore transports as well.
**Measured: 576 of 576 (ordered pair) × (rule) × (coordinate) cases, 0
violations.**

**Theorem (the defect telescopes).** For a triangle $A=\sigma.X$, $B=\tau.Y$,
$C=\upsilon.Z$ with rules $r_1,r_2,r_3$,

$$\delta \;=\; g_{CA}g_{BC}g_{AB}\;=\;\sigma\,\bigl(\rho^{r_3}_{ZX}\rho^{r_2}_{YZ}\rho^{r_1}_{XY}\bigr)\,\sigma^{-1}$$

— every relabelling except the first cancels identically. The chart family has
**two seeds**, so any three pairwise-distinct charts repeat a seed; on the
repeated pair the seed-level map is the self-map, measured uniquely the
identity (§7.1, 192/192 — I reproduce it), so

$$\delta \;=\; \sigma\,\bigl(\rho^{r_3}_{XZ}\bigr)^{-1}\rho^{r_2}_{XZ}\,\sigma^{-1}.$$

$S=\{1,W\}$ is **abelian of exponent two** — which the paper itself measures and
prints in §7.3 — so the conjugation is trivial and

$$\boxed{\ \delta \;\in\; \{\,\mathbf{1}\,\}\ \cup\ \{\text{the multiplicity bigon at that coordinate}\,\}\ }$$

**for every input, at every setting, at every completion, whatever the pair
table says.** And every multiplicity bigon *is by definition a closed loop of
the committed two-chart graph*, hence an element of the bigon-generated
holonomy group at that setting.

**Consequence: `COC-MEMBERSHIP` cannot fail on any admissible input.** Not "is
confined to $S$" — *cannot fail*. I checked the conclusion row by row: rows
whose defect lies outside $\{\mathbf 1\}\cup\{\text{bigons at that coordinate}\}$:
**0 of 1,824**.

Corollaries, all verified:

- **Single-rule triangles: 624 of 1,824, non-identity defects 0.** Forced (the
  per-rule edge map is a coboundary at all 48 (coordinate, rule) cells —
  measured, 0 exceptions).
- **Flat settings: multiplicity is 1 everywhere** (measured), so the edge map is
  a function of the endpoints and $\delta=\mathbf 1$ is forced for all **576**
  triangles there.
- **$D$ and $WD$ can never be triangle defects**: products of three $S$-elements
  form exactly $\{1,W\}$ (computed), and $D\notin S$.
- **§6's if-and-only-if is an algebraic identity of the construction**, not a
  discovery.

### 1.1 What this does to the paper's central honesty claim

The paper states, in four places, that the zero at the four flat settings is
**free**:

> Abstract: "each of the **576** triangles there could have carried a defect
> that no bigon generates — a pure level-2 obstruction at a flat setting — and
> the gate measures that none does."
> §5.4: "Every one of the **576** triangles there could have carried the wing
> exchange … The gate measures that none does."
> §11.4: "The free content of the membership gate is the four flat settings, and
> it is named and counted (576 triangles)."
> D4: "the free half is what the verdict rests on."

**These are false.** Given the same run's own pair table — computed and gated in
§3, *before* the census — not one of those 576 triangles could have carried
anything. The paper is one inferential step from knowing this: §5.4's own last
sentence says "those coordinates carry no multiplicity at all, so the three
edges' maps cannot be mixed", and §7.3 measures the abelian-exponent-two fact
that closes the argument. It uses that fact to retire the wrong-order control as
toothless and does not notice it retires the membership gate on the same
grounds.

**Severity: MAJOR.** This is RUNBOOK §4 / #36 at the unit's centre — "a gate
that restates its own constructor arguments", "every gate must be a measurement
that could have come out otherwise". The unit's headline must-pass gate is the
sin the catalogue names. It is not FATAL only because (i) every number is
correct, (ii) the verdict `COC-COCYCLE-CLOSES-AT-THE-DECLARED-TRIPLE-STRUCTURE`
is *true*, and (iii) the house already has the right instrument for this
situation and applied it correctly one section earlier (§7.3/D2: disclose,
do not delete). **If the repair does not re-classify `COC-MEMBERSHIP`, this
finding is FATAL** — the paper would then be certifying as a free measurement a
gate that provably cannot fail.

**Repair.** (a) Add the theorem to §5 as a derived proposition. (b) Re-class
`COC-MEMBERSHIP` from `measurement` to `disclosure`, exactly as
`COC-MISCOMPOSITION` is classed, with `COC-PAIR-TABLE` named as where the teeth
are. (c) Replace the four sentences. Verbatim replacements:

> **Abstract** — replace the last sentence of the "forced and free" paragraph
> with: "At the four settings whose connection is measured flat the admitted set
> is measured **not** contained in the trivial group, so those **576** triangles
> are the ones a naive reading would call free. They are not: the orbit
> construction telescopes the defect to a product of two committed-frame maps on
> one unordered pair, and at multiplicity one those two maps coincide, so the
> identity is forced there by the pair table alone. The free measurement of this
> unit is the **pair table** — which coordinates carry multiplicity — and the
> membership zero is its arithmetic consequence."

> **§5.4, Free** — replace with: "**Free — and where.** The defect telescopes:
> for charts $\sigma.X$, $\tau.Y$, $\upsilon.Z$ every relabelling cancels except
> the first, and since $S$ is abelian of exponent two that one cancels too, so
> $\delta$ is a product of two committed-frame maps on one unordered pair. At a
> coordinate of multiplicity one those two maps are equal and $\delta=\mathbf 1$
> is forced; at a coordinate of multiplicity two $\delta$ is the multiplicity
> bigon, which is a closed loop of the two-chart graph and therefore an element
> of its group. **Membership is therefore forced at every setting, not only at
> the two symmetric ones, and this gate is entered as a disclosure.** What was
> genuinely free, and is measured in §3, is the pair table: the 48 coordinates
> that carry multiplicity, and the 240 that do not."

> **§11.4** — replace with: "**The membership zero is analytically forced in
> full**, not only confined to the admitted set: the telescoping identity of
> §5.4 makes every defect either the identity or the multiplicity bigon at its
> own coordinate. It is reported as a disclosure. The unit's free measurement is
> the pair table of §3."

> **D4** — replace the last clause with: "…and the unit does not present its
> membership zero as free: the forced and the free are separated, and what the
> verdict rests on is the **pair table**, whose multiplicity pattern was
> available to come out otherwise and did not."

---

## 2. K1 — DOES THE VERDICT LICENSE "AT THIS BASE" OR ONLY "AT THIS ATLAS"?

**Only at this atlas — and I can show the difference is real, not hypothetical.**

### 2.1 The atlas-completeness sweep PASSES (a point for the paper)

K1 asks for a sweep for admissible charts outside the $S$-orbit. I ran it and
the unit survives, with a clean structural reason it does not state:

- The orbit of the committed frames under the **whole 162-element scope** is 324
  charts realising all **81** initial configurations; exactly **4** carry
  $j_0=0$ — precisely the declared family.
- Clause 1 of the predicate requires $p(j_X)=j_Y$ with $p\in S$, and every
  element of $S$ fixes $j_0$. **Therefore no chart outside the $S$-orbit can be
  glued to $F_1$ or $F_2$ at all.** The four-chart atlas is *closed*, not merely
  chosen.
- The other 80 initial-configuration classes were probed for triangles of their
  own: **0**.

**This argument belongs in §2.2 or §11.2** and is the strongest defence the
paper has; supply it. (MINOR, additive.)

### 2.2 But the base's own declared extension carries a genuine higher obstruction

§9.3 searches the 216-element extension as a **wider admission scope for maps
between the same four charts** and reports no change (I reproduce: 400 drawn
maps, 0 coordinates changed). It never builds **the extension's own chart
orbit** — the object its own admitted set of 8 generates. I built it.

| measured on the extension-orbit atlas | value |
|---|---|
| the 8-element admitted extension | a group, **NON-ABELIAN**, element orders $\{1,2,4\}$ |
| elements centralising $W$ | **4 of 8** |
| chart family (orbit of $F_1,F_2$ under those 8) | **16**, distinct at every setting |
| admissible triangles (same four-clause predicate) | **333,312** |
| **defects OUTSIDE the bigon-generated group** | **32,256** |
| where | **GP-E 16,128 and GP-F 16,128** — the two geometry-bearing settings |
| the escaping defect | a single permutation, 9 fixed points, order 2 |
| what it is | a **conjugate of $W$** by a non-centralising extension element |
| where it lives | inside the declared 216-scope, **outside** the 162-scope |

The mechanism is my telescoping identity read the other way: with a
non-abelian chart group the conjugation $\sigma(\cdot)\sigma^{-1}$ no longer
cancels, and $\sigma W\sigma^{-1}\notin\{1,W,D,WD\}$ for exactly the four
non-centralising $\sigma$. **Closure is therefore not a property of the
connection at all — it is the statement that the chart-generating group
centralises the level-1 holonomy.**

This refutes a specific sentence of §10 outright:

> "…this unit measures one necessary ingredient: an admitted set whose
> composites leave the holonomy group, at a coordinate where an admissible
> triangle can realise them. **The declared extension supplies the first half
> and is measured not to supply the second.**"

The declared extension supplies **both** halves, 16,128 times at each symmetric
setting, on base G, at the pinned completion, under the base's own two gluing
rules and its own four-clause predicate. What §9.3 measured is the much weaker
"the extension draws no new map *between the four $S$-orbit charts*".

**Severity: MAJOR.** The verdict itself survives — its qualifier "at the
declared triple structure" and §11.2 ("another declared third chart could give
another census") are doing exactly the work they should. What does not survive
is §10's diagnosis of what an obstruction would require, and the unqualified
"There is no gerbe-like residue".

**Repair.** Replace §10's closing paragraph:

> "**And what it does not mean.** The closure has a measured mechanism, and the
> mechanism is the chart group's, not the connection's. The defect telescopes to
> a conjugate, by the first chart's relabelling, of a product of committed-frame
> maps; the declared relabelling group is abelian of exponent two, so the
> conjugation is trivial and the defect is confined to that group before any
> geometry is consulted. The necessary ingredient for an obstruction is
> therefore **a chart-generating group that fails to centralise the level-1
> holonomy** — and base G declares one: the eight maps its 216-element extension
> admits form a non-abelian group of order eight, only half of whose elements
> centralise the wing exchange. The atlas that group generates is not this
> unit's declared triple structure and is not censused here; what this unit
> establishes is that the *abelian* atlas closes, and why."

And in §9.3, add the datum whose absence hides the whole issue: after "is
measured to be a group that is NOT contained in the bigon-generated holonomy
group", insert "— and is measured **non-abelian**, of element orders 1, 2 and 4,
with only four of its eight elements centralising the wing exchange."

Delete or scope "There is no gerbe-like residue" (§10). Suggested: "There is no
gerbe-like residue **at this atlas**".

---

## 3. K1b — WHY $D$ IS NEVER A TRIANGLE DEFECT: THEOREM, AND THE RIGHT CONTRAST

**Derived, not an artifact.** Every admissible identification lies in $S$; $S$
is a group; a defect is a product of three of its elements; the set of such
products is exactly $\{1,W\}$ (computed); $D\notin S$ (GEN P5, reproduced: $D$
lies outside both the 162- and the 216-scope). So $D$ is excluded before any map
is drawn. **This is the *same* disclosure §5.4 already makes** — yet the paper
reports it three times as a measurement:

> Abstract: "the completion's own defect is measured never to be a triangle
> defect."
> §5.2: "$D$ and $WD$ … are measured never to be triangle defects."
> §10: "$D$ and $WD$ … are measured to be **invisible to the triple
> structure**."

The word "measured" is unearned, and "invisible to the triple structure" reads
as a discovery about triple structure when it is a restatement of the chart
group's membership. **Severity: MINOR** (it is a disclosure-classification
error, not a wrong claim). Replacement for §5.2's second sentence:

> "At the symmetric settings that is a **proper** subgroup of the order-4
> holonomy group. That $D$ and $WD$ are not triangle defects is **forced** by
> the same containment that confines the defect to $S$: they lie outside every
> declared relabelling collection, so no product of admitted identifications can
> reach them. It is recorded as a disclosure."

**The structural statement the paper is reaching for, and gets wrong.** The
paper frames the contrast as *bigons see the completion's defect, triangles do
not* — i.e. as a statement about **loop shape**. It is not. Both objects are
loops; what separates them is **link kind**:

- A triangle defect is a composite of **identification links only, all read at
  one checkpoint** — a checkpoint-local loop in the chart direction. Its value
  lies in the group generated by the drawn identifications there, i.e. in $S$.
- $D$ is only reachable by a loop that **traverses leg links**: the unit's own
  `defect_loop` crosses at $t{=}0$, runs the preparation leg in $F_2$, crosses
  back at $t{=}1$ and returns in $F_1$. GEN §6.5 measures that leg links are
  *not* transports the base admits at all.
- The decisive check: the **multiplicity bigon is also checkpoint-local**, and
  its holonomy is measured to be $W$, never $D$ (§6 table, reproduced).

So the correct statement is: **checkpoint-local loops of any shape — bigon or
triangle — see only the admitted group; the completion's defect is visible only
to checkpoint-crossing loops.** Shape is irrelevant; the checkpoint is the
divide. This also shows that §5's headline comparison (a checkpoint-local defect
against a setting-level group of order 4) is not like-for-like in the RUNBOOK
§15-addendum sense; D3 discloses the mismatch and §6 supplies the matched
comparator, so the disclosure discipline is met — but the *conceptual* reading
should be stated at the matched coordinate, where it is exactly "level two is
level one" and nothing more. **Severity of the mis-framing: MINOR.** Suggested
insertion at the end of §6:

> "The divide is not between loop shapes but between link kinds. A triangle
> defect composes identification links only, all read at one checkpoint, so it
> is confined to the admitted group; the completion's defect is carried by a
> loop that traverses a preparation leg, and leg links are not transports the
> base admits. The multiplicity bigon is checkpoint-local too, and its holonomy
> is measured to be the wing exchange, never $D$. Checkpoint-local loops of
> either shape see the same thing."

---

## 4. K3 — COMPLETION-DEPENDENCE OF THE ATLAS

### 4.1 The measurements hold, including the one I expected to break

Verified independently:

- $W\!.F_1 \ne F_2$ by $D$ alone at the symmetric settings: confirmed. $D$ has
  45 fixed configurations, order 2, and is not the identity.
- Bare-Householder rebuild: $D$ = identity (81 fixed points); charts per
  setting **4,4,4,4,2,2**; admissible triangles **144,144,144,144,0,0**. Exact
  match, including the printed-not-smoothed half (the four flat settings keep a
  four-chart atlas).
- **The sweep's identification is sound.** The 40,320-member sweep does not
  recompute an atlas; it evaluates the 9×9 criterion
  $\Sigma Q^{\mathsf T}\Sigma Q = \mathbf 1$ and reads GEN's committed
  $D$-triviality census. That is only the *collapse* criterion if
  $D=\mathbf 1$ is equivalent to the Born-level chart identity collapsing —
  the "$\Leftarrow$" is structural, the "$\Rightarrow$" is not obvious, because
  chart identity is a **Born-level** object and $D$ is a **signed**
  permutation whose signs are invisible to it. I therefore swept the honest
  Born-level criterion independently: **members whose $\lvert V\rvert$ is
  $\Sigma$-symmetric = 96, disagreements with the $D$-triviality criterion = 0
  of 40,320.** The identification holds exactly on this family. Good.
- The number itself is a group-theoretic identity: 96 = the order of the
  centraliser of $\Sigma$ (an involution with 3 fixed points and 3
  transpositions) among permutations fixing index 0, $2\times(2^3\cdot 3!)=96$.

### 4.2 "The chart count is declaration-dependent" — carried at the right strength?

**Yes, and with unusual care** — §2.6, §9.2, §11.5, D7 all fence it, the sweep
is folded into no verdict, and §9.2 explicitly refuses to recompute a census
elsewhere. I find nothing to correct. One improvement is available and worth
taking: the paper says the chart count depends on the *completion*; my §1
theorem says it depends on the **relabelling group** too, and much more
sharply — 4 charts under $S$, **16** under the extension, at the very same
completion. The ontological claim should be stated over both coordinates.

### 4.3 Is the closure itself completion-scoped?

**No — and the paper is over-cautious here, in the one direction that costs it
nothing.** By the telescoping theorem the defect lies in $\{1,W\}$ at *every*
completion (because $S$ comes from the $j_0$ filter on the 162-scope, in which
$V$ does not appear), and it is either the identity or the multiplicity bigon,
which is always a loop of the two-chart graph. **So the cocycle closes at the
declared triple structure at every member of the completion family, provably.**
I confirmed the second endpoint by full rebuild: at the bare Householder,
non-identity defects = **0**, and GEN measures the holonomy group there as
order 1 at every setting — so any non-identity defect would have been a higher
obstruction, and there is none.

The closure is scoped by the **relabelling group**, not by the completion.
Suggested amendment to §11.5, added as a second sentence:

> "The closure verdict is nevertheless completion-**independent** at this triple
> structure: the admitted set is the $j_0$-filtered relabelling scope, in which
> the completion does not appear, so the telescoping identity of §5.4 holds at
> every member of the declared family. What the completion moves is whether the
> triple structure *exists*, not whether it closes. What moves the closure is
> the relabelling group."

---

## 5. K2 — THE CONTROLS

### 5.1 The wrong-order disclosure is honest, and is the model

§7.3, D2 and §11.8 are exemplary: measured inert (0 of 1,824), the reason
measured beside it (abelian, exponent two), entered as a disclosure, teeth moved
to a declared non-abelian witness. I verified the mechanism and the numbers. The
replacement witness is real: orders (3,2,3), fixed points (0,9,0), gated against
a direct index expression, reversed order measured to differ, reverse traversal
measured to be the inverse matrix; `compose-order` and `orient-flip` die there.
**Adequate.** Its only limitation is correctly disclosed (§11.8): it certifies
the *routine*, not the census's own order convention, which cannot be certified
on this base.

**The finding is not that this disclosure is wrong — it is that the identical
treatment is owed to two further controls and is not given.**

### 5.2 The $D$-injection control's counterfactual is impossible

> §7.2: "The first shows the census's defect set is a **proper** part of what
> the group contains, so a defect-set reading could have failed."

It could not. $D$ is not a product of three $S$-elements — computed: the set of
such products is exactly $\{1,W\}$ — so no census triangle can ever produce it,
at any coordinate, any setting, any completion. The injection is a **positive
control on the membership predicate's TRUE branch** (it verifies `in_group`
returns yes for a group element outside the defect set). That is a legitimate
and useful instrument control; it is not evidence that a defect-set gate could
have failed. **Severity: MINOR.** Replacement:

> "The first is a positive control on the membership predicate's affirmative
> branch: an element inside the group and outside the defect set is measured
> to be reported inside. It is an instrument control — no census triangle can
> produce $D$, since the products of three admitted maps are exactly the
> admitted set — and it is entered as one."

### 5.3 Do the two probes bracket the predicate's failure modes?

**Yes, as instrument controls; no, as census controls.** The two injections do
bracket the predicate: one input in-group/out-of-defect-set, one input
out-of-group; the predicate answers yes and no respectively, so it is neither
constant-yes (killed by `membership-lax`) nor secretly a defect-set test. That
is the right two-point bracket for a set-membership routine and I find it sound.

What the bracket does **not** establish, and §7.2 claims it does, is that "the
zero it reports **on the census** is not the only answer it can give". Both
injected maps lie outside $S$; both bypass `drawn_map` and are handed straight
to the composition; neither is reachable by the admission pipeline. The census
zero *is* the only answer the census can give. The `edge-perturb` mutant does
route through `drawn_map` and does kill `COC-MEMBERSHIP` — I confirmed it
(exit 1, kills `COC-PAIR-TABLE`, `COC-MEMBERSHIP`,
`COC-DEFECT-IS-A-BIGON-HOLONOMY`) — but it kills it by implanting a permutation
outside the admitted set, i.e. by violating the very closure premise that makes
the gate forced. So `COC-MEMBERSHIP`'s "falsified by a computation mutant"
status is earned only by a mutation no admissible input can imitate. **This is
the same finding as §1, seen from the mutant table**, and it is why the
re-classification there is the right repair. Replacement for §7.2's last two
sentences:

> "The second shows the membership **predicate** can fire: on an injected map
> outside the admitted set it answers no. Both injections are instrument
> controls — the admission pipeline cannot produce either map — so what they
> certify is the predicate, not the census. Why the census's own zero could not
> have been otherwise is derived in §5.4."

---

## 6. K4 — ADMISSION (lower depth, as directed)

- The generalised predicate reproduces the committed table: I recomputed the
  committed row from my own rebuild and get **18 FULL / 8 REAL**, matching cell
  by cell.
- **The four-chart pair table is arithmetically determined by the committed
  one.** By the equivariance lemma, the 12 ordered chart pairs decompose as
  $2\times(F_1,F_1) + 2\times(F_2,F_2) + 4\times(F_1,F_2) + 4\times(F_2,F_1)$;
  measured seed-pair draw counts are 24/24 (self, both rules) and 18/8 (cross).
  Predicted totals: $2(24)+2(24)+4(18)+4(18) = 240$ FULL and
  $2(24)+2(24)+4(8)+4(8) = 160$ REAL — **exactly the measured 240/160**. The
  paper is entitled to say the atlas is glued by the base's own rule; it should
  not leave the impression that 240/160 is 400 new measurements. It is GEN's
  18/8 replayed four times plus 96 self-map cells. Worth one sentence in §3.
  (MINOR.)
- **R1's one-setting scope is sufficient.** The killing clause compares leg-list
  *sizes* as multisets, 5 against 3; the leg count is fixed by construction at
  every setting (verified: 3 committed legs / 5 split legs / 4 vs 6 checkpoints
  at all six settings), so the clause cannot depend on the setting. D6 states
  this correctly. I also verified the factorisation R1 rests on:
  $U_X(g) = (R_g\otimes I)\,C_X\,(R_g^{\mathsf T}\otimes I)$ holds exactly for
  $R_0$ and $R_1$ on wing A. Candidate count $4\times2\times2\times2 = 32$
  confirmed. **No finding.**
- The 216-extension "draws the same map everywhere" claim: **400 drawn maps, 0
  coordinates changed** — reproduced exactly. The claim is true *as stated*; see
  §2.2 for what it does not establish.

---

## 7. K5 — INSTRUMENT (lower depth, as directed)

Verified, no findings of substance:

- Receipt totals: 19 anchors (all pass), 29 gates, 25 must-pass, 4 disclosures;
  must-pass denominator 24 = 25 − `COC-FALSIFICATION`, arithmetic consistent.
- `never_falsified` EMPTY at denominator 24; both denominators printed
  (23 computation / 5 waiver); the three waiver-only gates named.
- Fresh-eval gating satisfies both halves of the §14 addendum: 8 entries
  written, 8 priming reads returned stored values, 8 self-test requests for
  present keys, 0 hits, 64 misses. Not a zero-of-zero.
- AST no-mutant-exemption: 49 gate/anchor call sites, 0 reaching the mutant
  flag; the single `MUTANT not in ...` occurrence is argparse validation at line
  3447, outside every call site. Legitimate.
- Mutants: 3 spot-run (`membership-lax`, `edge-perturb`, `triangle-drop`), each
  exits 1 and kills exactly the gates the receipt names. The full 28 were not
  re-run (wall-clock).
- The mid-build self-correction: the per-setting reading is the correct one —
  4,4,4,4,**2**,**2** charts and 144,144,144,144,**0**,**0** triangles, verified
  by full independent rebuild. The gate's collapse clause is per-setting and
  would have caught a collapse-everywhere claim.
- Read-only instrument run: 19 anchors, 28 gates, 0 must-pass failures; the four
  frozen SHAs unchanged afterwards.

**One NOTE on the census's "two independent routes."** The comparator sums
$\prod$(rules that draw on each edge) over the same triples and coordinates.
This equals the enumerated count **by distributivity, for any pair table
whatever**; both routes call the same memoised `drawn_map` inside the same loop
nest. It is a real check on the enumerator's filter (it kills `triangle-drop`)
but it is an arithmetic restatement, not an independent computation, and §4's
"The comparator does not walk triangles at all … a count built from the pair
table and not from the census" oversells it. Suggested: "…a count built by
distributivity from the same pair table, which is a check on the enumerator's
keep-condition rather than an independent route to the census."

---

## 8. FINDINGS, RANKED

| # | severity | finding |
|---|---|---|
| F1 | **MAJOR** | The membership zero is forced in full, not merely confined: the telescoping theorem makes every defect either the identity or the coordinate's multiplicity bigon, and the bigon is always a loop of the two-chart graph. `COC-MEMBERSHIP` cannot fail on any admissible input. The four "free" claims (abstract, §5.4, §11.4, D4) are false. **FATAL if the gate is not re-classified as a disclosure.** |
| F2 | **MAJOR** | §10's "The declared extension supplies the first half and is measured not to supply the second" is refuted on base G: the extension's own 8-element admitted group (measured non-abelian, orders 1/2/4) generates a 16-chart atlas whose census carries **32,256 defects outside the bigon-generated holonomy group**, 16,128 at each geometry-bearing setting. The verdict survives on its qualifier; the diagnosis does not. Closure ⟺ the chart group centralises the level-1 holonomy. |
| F3 | MINOR | "$D$ and $WD$ are **measured** never to be triangle defects / invisible to the triple structure" (abstract, §5.2, §10) is forced by the same containment §5.4 already discloses; reported three times as a measurement. |
| F4 | MINOR | §7.2's "a defect-set reading could have failed" states an impossible counterfactual; and "the zero it reports on the census is not the only answer it can give" is true of the predicate, false of the census. Both injections are instrument controls only. |
| F5 | MINOR | The bigon/triangle framing of the $D$-blindness is the wrong contrast; the divide is link kind (checkpoint-local vs. checkpoint-crossing), not loop shape. The multiplicity bigon is checkpoint-local and also never sees $D$. |
| F6 | MINOR | §9.3 omits the one datum that hides F2: that the admitted extension is **non-abelian**. |
| F7 | MINOR | The atlas-completeness argument the paper is entitled to (clause 1 + $S$ fixes $j_0$ ⟹ no chart outside the $S$-orbit can be glued to a committed frame; 4 of 324; 0 triangles in the other 80 classes) is missing. It is the paper's strongest defence. |
| F8 | MINOR | §3's 240/160 is GEN's 18/8 replayed by the orbit action plus 96 self-map cells; state it. |
| F9 | NOTE | The census's "independent route" is a distributive-law restatement sharing the whole admission pipeline. |
| F10 | NOTE | §11.5's completion caution is one step too weak in the harmless direction: the closure is provably completion-**independent** at this triple structure; what moves it is the relabelling group. |

**Not findings — checked and clean:** all 118 numbers; the freeze and
declaration-order discipline; the read-time coordinate (144/0); the chart
identity and its `chart-merge` mutant; the anchoring of the comparator against
GEN by hash; the completion sweep's 96/40,224 and its Born-level soundness; the
equivariant-completion rebuild including the printed-not-smoothed flat half;
R1's absence and its one-setting scope; the switching sweep and its forced-clause
disclosure; the fresh-eval double gating; the flip-test's forced/unforced split;
exactness; the verdict derivation and vocabulary; the deviations appendix D1–D8,
which is candid and, apart from D4, accurate.

---

## 9. THE SHAPE OF THE VERDICT, IN ONE PARAGRAPH

`COC-COCYCLE-CLOSES-AT-THE-DECLARED-TRIPLE-STRUCTURE` is **true**, and its
qualifier list is doing real work — I could not break it. But the sentence it
licenses is narrower than the one the prose reaches for. It does **not** license
"the connection is the whole geometric story at this base": the same base, same
legs, same laws, same completion and same two gluing rules, with the base's own
declared 8-element admitted extension as the chart-generating group, carries a
triple structure with 32,256 defects outside the holonomy group. It licenses
"**at this atlas**" — and, more sharply than the paper says, "**because this
atlas's generating group is abelian of exponent two.**" What the unit has
actually established is not that base G's connection is complete at level two,
but that **an atlas generated by a group centralising the level-1 holonomy
cannot see anything new** — which is a theorem about the construction, is worth
stating as one, and comes with its own converse ready to hand on the same base.
The unit is 1,824 correct numbers in service of a sentence that needs to be
rewritten.

---

## GRADE

# ACCEPT-WITH-FIXES

Zero numerical errors in 118 independent recomputations; the verdict is true and
correctly qualified; the instrument is sound. The fixes are F1 (re-class
`COC-MEMBERSHIP` as a disclosure and replace the four freedom sentences — this
one is mandatory, and the grade is REJECT without it), F2 (replace §10's
extension diagnosis and add the non-abelian datum to §9.3), and the seven
MINOR/NOTE items, all of which are supplied above as verbatim replacements. No
number may move.

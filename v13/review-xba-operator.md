# XBA — HOSTILE REVIEW, R1 (OPERATOR / ALGEBRAIC LENS)

**Reviewer:** R1, operator/algebraic lens.
**Protocol:** `v13/note-xba-hostile-protocol.md` (frozen, v13 #238), kill-shots K1–K5.
**Mode:** repo read-only. Nothing imported from the unit. All recomputation in
the session scratchpad on my own instrument.
**Recomputations:** **174** independent (itemised in §9).
**Grade:** stated last (§10).

---

## 0. Hash verification of the frozen object

Verified before reading anything, and re-verified after a mid-run restart.
Both times identical.

| artifact | declared sha256-12 | measured | match |
|---|---|---|---|
| `v13/paper-xba-crossbase.md` | `284a51e88e6f` | `284a51e88e6f` | yes |
| `v13/code/xba_crossbase_exact.py` | `91677df8bbc7` | `91677df8bbc7` | yes |
| `v13/code/xba_crossbase_output.txt` | `603a6eab18cf` | `603a6eab18cf` | yes |
| `v13/code/xba_crossbase_receipt.json` | `1945dbb12eb1` | `1945dbb12eb1` | yes |

Background sources read and hash-checked: `nt_transport_receipt.json`
(`d256891b479a`), `gen_generality_receipt.json` (`e0b2f444f6a9`),
`v13/review-gen-operator.md` (`1d17534ef9f4`) — each agrees with the value the
instrument pins at `PIN_SHA`/`NT_RECEIPT_SHA`/`GEN_RECEIPT_SHA`/`REVIEW_SHA`.

---

## 1. My instrument, and why it is independent

I did not import, read-for-reuse, or copy any object of
`xba_crossbase_exact.py` into my own code. Three deliberate divergences make the
agreement meaningful:

1. **No spanning tree.** The unit gauge-fixes on a cotree. I obtained the cycle
   space as the $\mathbb{F}_2$-span of the 364 walks' own **edge-parity vectors**
   in $\mathbb{F}_2^{13}$, row-reduced to an echelon basis, then changed
   coordinates into the declared-cycle basis. No tree, no cotree, no gauge
   section enters my census at any point.
2. **A different field.** The unit carries base 1 in the quartic
   $\mathbb{Q}(\cos\pi/8)$ as 4-tuples reduced by $x^4 = x^2 - \tfrac18$. I
   carried it in the **cyclotomic field $\mathbb{Q}(\zeta_{16})$** as 8-tuples of
   `Fraction` reduced mod $x^8+1$, with $\cos(k\pi/8) = (\zeta^k - \zeta^{8-k})/2$.
   Different field, different reduction, different code path.
3. **A different search order.** My walk enumerator is a recursive DFS; the
   unit's is an explicit stack. My automorphism lifter and my violator builder
   were written from the paper's prose, not from the source.

Two heavier cross-checks were run on the delivered code itself, in a scratch
mirror (never in the repository): a full regeneration and a source-corruption
test. Both are reported in §7.

---

## 2. K1 — THE CHAIN

### 2.1 The arena, rebuilt

Built from the two terminal receipts' own admission tables, at setting index 4
(SP-E / GP-E), by my own graph constructor.

| quantity | paper | mine |
|---|---|---|
| admission cells compared | 24 | **24** |
| cells agreeing on rule and permutation | 24 | **24** |
| nodes | 8 | **8** |
| links | 13 | **13** |
| identification links | 7 | **7** |
| components | 1 | **1** |
| cycle rank | 6 | **6** |
| reduced walks, all base points, length 0 included | 16,168 | **16,168** |
| closed walks, length 0 excluded | 2,820 | **2,820** |
| closed walks based at $F_1@t{=}0$ | 364 | **364** |
| distinct cycle classes over those 364 | 27 | **27** |
| FULL-only closed walks | 8 | **8** |
| REAL-only closed walks | 18 | **18** |
| dim of the $\mathbb{F}_2$-span of the walks' parity vectors | (6) | **6** |

The six declared cycles: I checked first that each declared edge set **is** a
cycle (every node degree even) — a check the paper does not state and the
instrument does not gate directly, though `XBA-BASIS-INVERTIBLE` would catch a
non-cycle indirectly. All six pass; their rank over $\mathbb{F}_2$ is **6**.

### 2.2 The 4,096 census

| quantity | paper | mine |
|---|---|---|
| connection space | 4,096 | **4,096** |
| distinct class-count profiles | 89 | **89** |
| the realized profile | 82 / 86 / 90 / 106 | **(82, 86, 90, 106)** |
| reproducing it as a multiset | 96 | **96** |
| reproducing it element by element | 16 | **16** |
| labels generating the whole group | 3,906 | **3,906** |
| of those, reproducing the profile | 96 | **96** |
| most common profile | $(78,90,94,102)$ at 384 | **[78, 90, 94, 102] at 384** |

The 3,906 also comes out of a wholly independent analytic route: the number of
surjective linear maps $\mathbb{F}_2^6 \to \mathbb{F}_2^2$ is
$4^6 - (3\cdot 2^6 - 2) = 3906$. Agreement confirms both the count and the
basis-independence of the "generated group" predicate.

### 2.3 The species-clause chain, on my own predicates

| clause added | paper survivors | mine | paper hits | mine | element-wise hits (mine) |
|---|---|---|---|---|---|
| — | 4,096 | **4,096** | 96 | **96** | 16 |
| **E0** | 3,072 | **3,072** | 96 | **96** | 16 |
| **E1** | 768 | **768** | 24 | **24** | 4 |
| **E2** | 192 | **192** | 12 | **12** | 2 |
| **E3** | 12 | **12** | 6 | **6** | 1 |
| **E4** | 6 | **6** | 6 | **6** | 1 |

**All six survivors carry 82/86/90/106 as a multiset — confirmed.** Exactly one
carries it element by element, which is the realized point. The six are

$(\mathbf 1,\mathbf 1,W,\mathbf 1,\mathbf 1,D)$, $(\mathbf 1,\mathbf 1,W,\mathbf 1,\mathbf 1,WD)$,
$(\mathbf 1,\mathbf 1,D,\mathbf 1,\mathbf 1,W)$, $(\mathbf 1,\mathbf 1,D,\mathbf 1,\mathbf 1,WD)$,
$(\mathbf 1,\mathbf 1,WD,\mathbf 1,\mathbf 1,W)$, $(\mathbf 1,\mathbf 1,WD,\mathbf 1,\mathbf 1,D)$,

and I verified they form **one simply-transitive orbit** of the six Klein-group
relabellings. Consequences are recorded as findings F6, F7.

### 2.4 The twelve candidates

Every cell recomputed with predicates I wrote from the paper's prose. My
automorphism computation is my own (node permutations preserving the edge
multiset; typed refinement; link-level lifts; induced action read off the six
declared cycles' image edge sets).

| candidate | membership (paper / mine) | subset (paper / mine) | hits (paper / mine) | violators-still-hitting (paper / mine) |
|---|---|---|---|---|
| C1 source-split | yes / **yes** | 42 / **42** | 6 / **6** | 90 / **90** |
| C2a equivariance, rule-preserving | yes / **yes** | 4,096 / **4,096** | 96 / **96** | — / **0** |
| C2b equivariance, full | no / **no** | 64 / **64** | 0 / **0** | 96 / **96** |
| C2c equivariance up to naming | no / **no** | 136 / **136** | 0 / **0** | 96 / **96** |
| C3 admission pattern | yes / **yes** | 1,728 / **1,728** | 96 / **96** | 0 / **0** |
| C4 species-split, named | yes / **yes** | 1 / **1** | 1 / **1** | 95 / **95** |
| C5 species-split, naming-closed | yes / **yes** | 6 / **6** | 6 / **6** | 90 / **90** |
| C6 common preparation leg | yes / **yes** | 1,024 / **1,024** | 24 / **24** | 72 / **72** |
| C7 commuting local legs | yes / **yes** | 1,024 / **1,024** | 24 / **24** | 72 / **72** |
| C8 intertwined local legs | yes / **yes** | 256 / **256** | 24 / **24** | 72 / **72** |
| C9 unintertwined preparation leg | yes / **yes** | 2,304 / **2,304** | 48 / **48** | 48 / **48** |
| C10 group of order four | yes / **yes** | 3,906 / **3,906** | 96 / **96** | 0 / **0** |

**Zero mismatches, 12 of 12.** Automorphisms: rule-preserving link maps **2**,
full multigraph **16**, induced actions on $H_1$ **1** and **8** — all four match.

C1's residual sentence in §5 is exactly right: the 6 hits inside C1 are precisely
those with $(\texttt{SQ\_REAL\_1},\texttt{SQ\_REAL\_2},\texttt{SQ\_REAL\_3}) = (d,\mathbf 1,\mathbf 1)$
— "the preparation square alone" — and the 36 misses carry $d$ in one of eighteen
other patterns. I tabulated all 21 patterns; the correspondence is exact.

### 2.5 C4's subset-size-1 forcing — is the scoping carried everywhere?

Yes, in the places that matter. §5 ("As a statement about subsets, forcing at
size one is trivial, and this paper says so rather than trading on it"), §11.4,
and D2 all state it plainly, and the verdict is stated at C5 rather than C4. The
paper is honest here and I bring no complaint against the disclosure.

What the disclosure does **not** say is the sharp form of the residual — see F3.

---

## 3. K2 — THE PREDICTION

### 3.1 The third instance and the control reproduce

Rebuilt from scratch in my own arithmetic, gauge-free route (raw matrix product
along each of the 364 walks, permutation part taken):

| instance | carrier | $W$ fixed | $D$ fixed | $D$ order | distinct holonomies | class counts |
|---|---|---|---|---|---|---|
| base 1 @ SP-E | 36 | **6** | **18** | **2** | **4** | **82/86/90/106** |
| base 1 @ SP-F | 36 | **6** | **18** | **2** | **4** | **82/86/90/106** |
| base G @ GP-E | 81 | **9** | **45** | **2** | **4** | **82/86/90/106** |
| base G @ GP-F | 81 | **9** | **45** | **2** | **4** | **82/86/90/106** |
| **base S (third instance)** | 81 | **9** | **45** | **2** | **4** | **82/86/90/106** |
| **base S' (equivariant control)** | 81 | **9** | **81** | **1** | **2** | **172 / 192** |

All 13 gauge-fixed labels come out $\mathbf 1$ on the six legs and on
`FULL@0`, `FULL@1`, `FULL@3`; $W$ on `REAL@0`; $WD$ on `REAL@1`, `REAL@2`,
`REAL@3` — at every one of the five non-degenerate readings. The paper's §3
table, §7.2 table and §7.3 control all reproduce exactly.

The derivation of §7.1 I also verified by hand, link by link, and it is correct.

### 3.2 The attack via D4/D5/D6: can the varied parameters reach the connection?

The protocol asks whether the label-level scope weakens the prediction. It does,
and more sharply than D5 states. I measured each of the three declared
variations:

**(a) The preparation vector is inert.** For **all 36** transpositions of the
nine system-pair labels, $\psi_G$ (Schmidt rank 3) and $\psi_S$ (Schmidt rank 2)
produce the **identical defect operator** $D$ — not merely the same order or the
same fixed-point count, the same matrix. So "a different preparation vector of
Schmidt rank two" cannot change $D$, cannot change any label, and cannot change
the profile.

**(b) The measurement rotation is inert.** Six quaternions — including base G's
$(1,0,0,0)$, $(2,1,0,0)$, $(3,0,0,2)$ and the third instance's $(5,1,2,3)$ —
give $D$ of order 2 and class counts 82/86/90/106 in every case.

**(c) Two of the four clauses are structural, not contingent.** $E2$ (the two
local legs commute) holds for **64 of 64** rotation pairs, because the two wings
act on disjoint tensor factors. $E3$ ($W$ intertwines the local legs) holds for
**8 of 8** symmetric settings and **0 of 56** asymmetric ones — so $E3$ is a
restatement of "the setting is symmetric", which the arena already declares.
$E1$ is weaker still: in the instrument it is
`legs["F1"][0] == legs["F2"][0]` where `prep2 = Uprep` is *the same object*, so
the comparison is an object against itself and can only fail under `prep-lax`.

**(d) Seven of the thirteen labels are forced by the bookkeeping.** I built a
base satisfying **no** species clause (frames deliberately given different
preparations and different rotations) and measured its labels: all **7 of 7**
spanning-tree links (the six legs and `FULL@0`) still carry the identity, and
**0 of 6** cotree links do. The tree labels are a property of the gauge-fixing
convention, not of any base.

**(e) The only live parameter is the completion transposition**, and its only
effect is to select $D$'s order:

| $D$ order | transpositions (of 36) | meaning |
|---|---|---|
| 1 | **6** | the equivariant control: $E4$ fails |
| 2 | **12** | the Klein case — the declared 4,096 |
| 3 | **18** | $E1$–$E4$ all hold, but the connection is outside the arena |

Base G draws $(1,2)$ and the third instance draws $(1,5)$; both land in the
12. **So the third instance's "prediction" reduces to a single bit: that the
drawn transposition falls in the order-2 third of the family.** Everything else
about it — the preparation, the rotation, and (see F12) the carrier shape — is
provably incapable of moving the answer. This is the substance of F2.

### 3.3 What a full admission-recomputation on the third instance would show

D5 declines to recompute the third instance's admission table. Within budget I
determined what it would show, from the structure rather than by
re-implementing two terminal instruments:

The admission table's content, as the paper itself scopes it in §2, is (i) which
links exist and (ii) which permutation each rule draws. For base S the two
gluing rules are the *same operators* as base G's — the full-leg rule draws the
identity and the realized rule draws $P_W = $ `wing_swap(3,3)`, which is
**literally the same matrix** for base S as for base G, since $P_W$ depends only
on the carrier shape $(3,3,3,3)$ and not on $\psi$, $R$, or the transposition.
The admission verdicts therefore cannot differ from base G's at any cell where
admissibility is a property of the drawn permutation alone. What *could* differ
is a cell where admissibility depends on the preparation — and the generality
unit's own flip-test (cited at D6) is the precedent: with the bare Householder
the full-leg rule admits **two** permutations at the symmetric settings and the
links are refused. That is the one mechanism by which a recomputation could
change the graph, and it is exactly the equivariant case ($D = \mathbf 1$),
which base S is not.

**Conclusion on K2:** the label-level scope does weaken the prediction, and the
paper claims it at very nearly the right strength — D4 and D5 are honest — but
D5's "test of the labels, on a declared graph" understates by one level. It is a
test of the transposition's commutator class, on a declared graph, with the
other two declared variations provably inert. The replacement wording is in F2.

---

## 4. K3 — THE RESIDUAL OPEN

**The admission-table scoping is honest everywhere.** I read every one of the
nineteen sentences in the paper that touch the admission table. Each treats it as
read, measured, or used — never as explained:

- abstract: "that agreement … is an input here, not a result";
- §1.1: "The arena is not assumed … measures the agreement itself";
- §5: "the 24-cell table is load-bearing; it is simply not enough";
- §10: "together with the admission table's datum";
- §11.2: "this unit measures that agreement and uses it, and does not explain
  it … leaves the admission-table one exactly where it was".

**No sentence claims the graph commonality is explained.** K3's first limb
passes without a finding.

**C2a's vacuity and its missing violator.** Legitimate, and not repairable as a
violator: a predicate satisfied by all 4,096 connections has no violator, and
constructing one is impossible rather than merely omitted. §8 and D7 both name
it. One thing is missing and *is* repairable: the paper never says that the
equivariance machinery has a positive control anyway — C2b and C2c run through
the identical `apply_action` code path and return **False** on the realized
connection, with subsets 64 and 136. That is the demonstration that the
machinery can fire, and it should be cited where the control gap is named. See
F13.

---

## 5. K4 — THE FREEZE (steering audit)

The freeze gate is real and measures what it says: zero profiles evaluated at
the declaration point, and every constrained-subset gate strictly later in the
receipt's gate order. `freeze-lax` dies at it (I ran it: exit 1,
`FAILED: XBA-CANDIDATE-FREEZE`).

But the freeze protects the wrong thing, and D1 records the residual without
stating its sharp form. Which candidate definitions could have been
reverse-engineered from the known answer?

- **C4** is the realized answer written as a predicate.
- **C5** is C4 quotiented by naming.
- **C6, C7, C8, C9** are each a statement that one declared coordinate of the
  realized point is (or is not) the identity.
- C1, C2a/b/c, C3, C10 come from the pin or the prior unit and are not steered.

The vehicle is not the candidate list. It is **the declared cycle basis**. And
here is the sharp form: I measured that **3,906 of the 4,096 connections admit
the C5 shape $(\mathbf 1,\mathbf 1,d,\mathbf 1,\mathbf 1,w)$ on *some* basis of
the cycle space** — exactly the order-4 connections, as the kernel-dimension
argument predicts, and I confirmed it by exhibiting an explicit basis for every
sampled member. So "the six declared cycles take the values
$(\mathbf 1,\mathbf 1,d,\mathbf 1,\mathbf 1,w)$" is, as a property of a
connection with the basis free to vary, satisfied by 95.4% of the space.

All of C4/C5's force therefore lives in the *choice of the six cycles*, which was
made after the realized labels were computed. **The paper's defence is the right
one** — the E0–E4 correspondence and the derivation of §7.1 are what carry it,
and both are independent of the answer. The freeze gate is not what carries it,
and D1 should say so in those terms. See F3.

Does the third-instance prediction answer the concern? Given §3.2 above: no, not
materially. It re-runs the same template with parameters that cannot move the
answer. What would answer it is a genuinely different species — see F12, where I
built one.

**The paper's choice to record D1 rather than argue it away is correct and should
be preserved.** My complaint is only that the record understates the residual.

---

## 6. K5 — INSTRUMENT

Every item on the protocol's list was checked.

**The hash pins.** There are **four**, not three (the protocol says three; the
paper's §12 correctly says four). I corrupted each source file by one byte in a
scratch mirror of the repository and re-ran. All four fire, exit 1, with the
anchor named:

| corrupted source | anchor that fired | rc |
|---|---|---|
| `note-xba-crossbase-pin.md` | `A01 pin sha256` | 1 |
| `nt_transport_receipt.json` | `A02 NT terminal receipt sha256` | 1 |
| `gen_generality_receipt.json` | `A03 GEN terminal receipt sha256` | 1 |
| `review-gen-operator.md` | `A04 frozen operator review sha256` | 1 |

Note that only three of the four have a mutant (`anchor-review-hash`,
`anchor-nt-hash`, `anchor-gen-hash`); `A01` has none. My source-corruption test
supplies the missing falsifier and it passes.

**Anchors.** 36 total, all `ok`. Grouping recomputed: 4 hash pins / 7
frozen-review construction / 10 rebuilt arena / 7 rebuilt bases / 8 census —
exactly the 4/7/10/7/8 breakdown §12 claims.

**Mutants.** I ran **15** independently in the scratch mirror — every mutant that
perturbs a computation load-bearing for K1/K2. **All 15 died**, each at a gate or
anchor consistent with its declared perturbation, and each named kill is the
right one:

| mutant | rc | falsified |
|---|---|---|
| `field-lax` | 1 | anchor A23 |
| `wingswap-lax` | 1 | anchor A22 |
| `prep-lax` | 1 | `XBA-SPECIES-CLAUSES-MEASURED`, `XBA-LABELS-IN-THE-KLEIN-GROUP` |
| `base1-angle` | 1 | anchor A36 + 4 gates |
| `species-lax` | 1 | `XBA-CLAUSE-CHAIN`, `-CANDIDATE-CHAIN-CONSISTENCY`, `-DERIVATION-MATCHES-THE-BASES`, `-THIRD-INSTANCE-PREDICTED` |
| `memo-lax` | 1 | `XBA-GAUGE-SELFTEST-HAS-TEETH` |
| `gauge-head` | 1 | `XBA-GAUGE-SELFTEST-HAS-TEETH` |
| `violator-lax` | 1 | `XBA-NEGATIVE-CONTROLS` |
| `freeze-lax` | 1 | `XBA-CANDIDATE-FREEZE` |
| `candidate-lax` | 1 | `XBA-CANDIDATE-CHAIN-CONSISTENCY` |
| `direct-order` | 1 | anchor A36, `XBA-DIRECT-COMPARATOR` |
| `reverse-lax` | 1 | anchor A36, `XBA-DIRECT-COMPARATOR` |
| `admission-lax` | 1 | anchor A10, `XBA-ADMISSION-AGREEMENT` |
| `basis-lax` | 1 | `XBA-BASIS-INDEPENDENT`, `XBA-BASIS-INVERTIBLE` |
| `control-completion` | 1 | `XBA-EQUIVARIANT-CONTROL-BREAKS-IT` |

**Three reconstructed from prose alone**, implemented in my own instrument and
measured to break what the prose says they break:

- `direct-order` ("composes the link matrices in the wrong order") — my base-G
  rebuild then returns `{1: 82, W: 86, OUTSIDE: 196}`, profile broken;
- `reverse-lax` ("traverses a link backwards without transposing") — returns
  `{OUTSIDE: 356, W: 4, 1: 4}`, profile broken;
- `gauge-head` ("head-only action") — I computed the head-only action
  independently and it moves the profile at **12,288 of 16,384** gauge
  elements, so `deviations == 0` fails.

**`never_falsified` EMPTY at 23, with both denominators.** Confirmed from the
receipt: `must_pass` 23 (the 24th, `XBA-FALSIFICATION-CENSUS`, is excluded
because it does not exist inside a mutant run), `falsified_by_some` 23,
`falsified_by_computation` 19, `never_falsified` `[]`,
`falsified_only_by_a_waiver` = the four gates §12 names. Both denominators are
printed. The disclosure is accurate and unusually candid. One reason is not
disclosed — see F11.

**The cache gating.** The refusal mechanism is real, not cosmetic. The cache is
primed with `("selftest", mask)` keys before the sweep; the sweep's normal path
tests `if key in HOLCACHE` purely to *count* the refusal and then recomputes from
the link variables. I verified the arithmetic independently: **27** distinct
edge-parity masks over the 364 walks $\times$ **16,384** gauge elements =
**442,368** — matching the receipt's `fresh_evaluations`, `refused_lookups`, and
`primed`/`reserved_returns` at 27/27. `memo-lax` (which reads the cache) dies.

**The gauge sweep.** Recomputed from the raw 13 link labels with my own action:

| quantity | paper | mine |
|---|---|---|
| gauge elements swept | 16,384 | **16,384** |
| profiles that move | 0 | **0** |
| mis-conventioned (head-only) control that moves | 12,288 | **12,288** |
| fresh evaluations | 442,368 | **442,368** |

**The eleven declared violators.** I rebuilt the lex-first single-coordinate
constructor from the prose and reproduced **all eleven descriptions and all
eleven profiles**, plus the one declared absence (C2a). Zero mismatches. No seed
enters; the construction is deterministic, as claimed.

**Exactness and hygiene.** My own AST sweep: **0** float literals, **0** calls to
`float`, no numpy, no tolerance construct (the single `sqrt` token is inside a
comment). Gate/anchor call sites: **64**, of which **0** reach the mutant flag;
`MUTANT`-inequality comparisons: **0**. The §14 addendum from v13 #208 is
satisfied.

**Determinism and regeneration.** Two `--delivery` runs in the mirror produce
**byte-identical** `output.txt` and `receipt.json`, with zero wall-clock or
timestamp tokens in either. And my run of the frozen code reproduces the
delivered `xba_crossbase_output.txt` **byte-for-byte in all 147 lines** outside
the mutant-census block, which `--no-census` skips by construction.

---

## 7. Findings, ranked

### F1 — MAJOR. The four-clause mechanism is incomplete; I have an explicit counterinstance.

**Evidence.** Take an exchange-invariant preparation, the quaternion $(5,1,2,3)$,
and the completion transposition $(0,1)$. Measured on my instrument:

| clause, in its prose form | holds? |
|---|---|
| E1 the preparation leg is common to the two frames | **yes** |
| E2 the two local legs commute | **yes** |
| E3 the wing exchange intertwines both local legs | **yes** |
| E4 the wing exchange does not intertwine the preparation leg | **yes** |

and yet $D$ has **order 3**, $\lvert\langle W,D\rangle\rvert = \mathbf{6}$, the
364 walks carry **six** distinct holonomies, and the class counts are
**[42, 46, 46, 72, 78, 80]** — not the profile. **18 of the 36** transpositions
behave this way. A fifth condition is doing silent work: $D^2 = \mathbf 1$,
equivalently the connection is Klein-valued, equivalently it lies in the
declared 4,096 at all.

The instrument **does** gate this (`D_is_an_involution` inside
`XBA-SPECIES-CLAUSES-MEASURED`), §3's per-instance table **does** carry the row,
and §11.3 **does** scope the arena. So no measured number is wrong. What is wrong
is the headline: the abstract, §7.1's derivation, §7.2's prediction and §10's
verdict paragraph all present **four** clauses as the mechanism, and D4 reasons
explicitly about involutivity without promoting it to a clause. A reader
applying the stated mechanism to a new instance gets the wrong answer 18 times
out of 36.

**Repair.** Promote the arena condition to a fifth clause in the §2 table and
carry it in the headline sentences. Suggested replacement for the abstract
sentence (currently "…and that point is forced, cycle by cycle, by four clauses
both bases satisfy for reasons that have nothing to do with holonomy:"):

> …and that point is forced, cycle by cycle, by four clauses both bases satisfy
> for reasons that have nothing to do with holonomy — given the arena's own
> condition, measured separately on each instance, that the preparation defect
> is an involution, so that the connection is Klein-valued at all:

and add to the §2 clause table:

> | **E5** the preparation defect is an involution | measured on both bases, and on the third instance | the connection lies in the declared Klein-four arena |

with a sentence in §7.2: "Of the thirty-six completion transpositions available
at this carrier, twelve give an involutive defect, six give the identity, and
eighteen give a defect of order three whose connection is not Klein-valued and
therefore not in this arena; E5 is what selects the first twelve."

### F2 — MAJOR. The third instance's three declared variations are provably inert; the prediction risked one bit.

**Evidence.** §3.2 above, in full. In summary: the preparation vector cannot
change the defect (identical defect operator for $\psi_G$ and $\psi_S$ at **all
36** transpositions); the measurement rotation cannot change the class counts
(**6 of 6** quaternions give 82/86/90/106); E2 holds for **64 of 64** rotation
pairs and E3 for **8 of 8** symmetric settings (both structural, from the
disjoint tensor factors and the symmetric setting respectively); E1 is a
comparison of one object with itself; and **7 of the 13** labels are identically
$\mathbf 1$ for any base whatsoever, verified on a base satisfying no clause.
The single live parameter is the transposition, whose only effect is to select
$D$'s order.

This does not make the third instance worthless — it is a real consistency
check and it passed. It makes the *rhetoric* around it too strong. The abstract
says "A **third instance** was constructed for the purpose — a fresh integer
quaternion, a different preparation vector of Schmidt rank two, a different
completion transposition — and its class counts were measured afterwards", which
invites the reader to count three independent risks where there is one.

**Repair.** Replace the abstract sentence with:

> A third instance was constructed for the purpose — a fresh integer quaternion,
> a different preparation vector of Schmidt rank two, and a different completion
> transposition — and its class counts were measured afterwards: 82 / 86 / 90 /
> 106. Of those three variations only the transposition can reach the
> connection: the rotation and the preparation are measured inert, and what the
> instance tests is that its defect is a non-trivial involution.

and extend D5 with: "What the third instance tests is not the labels in general
but the commutator class of its completion transposition with the wing
exchange; the rotation and the preparation vector are measured not to reach the
connection at all."

### F3 — MINOR. D1's steering residual is recorded but understated; its sharp form is measurable.

**Evidence.** **3,906 of the 4,096** connections admit the C5 shape
$(\mathbf 1,\mathbf 1,d,\mathbf 1,\mathbf 1,w)$ on *some* basis of the cycle
space — exactly the order-4 connections. So C4/C5's force is carried entirely by
the choice of the six declared cycles, made after the realized labels were
known, and not at all by the freeze gate (which measures zero profiles, a
different thing).

**Repair.** Append to D1:

> The sharp form of the residual is measurable and is this: on a freely chosen
> basis of the cycle space, 3,906 of the 4,096 connections — every one whose
> labels generate the group — take the shape $(\mathbf 1,\mathbf 1,d,\mathbf
> 1,\mathbf 1,w)$. The declared basis is therefore the whole of what C4 and C5
> assert, and the freeze gate does not protect it. What protects it is the
> one-to-one correspondence of §2 between the six cycles and five facts both
> terminal papers state without reference to holonomy, together with the
> derivation of §7.1 — and those, not the freeze, are where a reader should
> press.

### F4 — MINOR. §2 gives a factually wrong reason for C2a's vacuity.

**Evidence.** §2 states: "The rule-preserving group is generated by the frame
swap, **which carries every link to itself** and therefore acts trivially on
cycles." I computed the non-identity rule-preserving link map explicitly: it
carries `LEG_F1_1 → LEG_F2_1`, `LEG_F1_2 → LEG_F2_2`, `LEG_F1_3 → LEG_F2_3` and
back, and fixes only the seven identification links. **7 of 13**, not 13 of 13.
The conclusion (one induced action, C2a vacuous) is correct; the stated
mechanism is not. This is the #38→#40 lesson — "describe mechanisms as measured,
not as intended".

**Repair.** Replace with:

> The rule-preserving group is generated by the frame swap, which fixes each of
> the seven identification links and exchanges the six leg links in matching
> pairs; because every declared cycle contains the matching pair of legs, each
> cycle's edge set is fixed and the induced action on $H_1$ is trivial.

### F5 — MINOR. §12 attributes the second fail-closed branch to the wrong mutant.

**Evidence.** §12 says: "Both paths are exercised — by the `basis-lax` and
`base1-angle` mutants respectively." I ran both and grepped their output for the
refusal messages. `basis-lax` does fire the first path ("the declared cycle basis
is not a basis; every downstream measurement is refused"), once. `base1-angle`
fires the second path **zero** times — it dies at anchor A36 with four gate
failures, having left base G readable. The mutant that *does* exercise the second
path is **`prep-lax`**, which makes all four readings unreadable and fires "no
base yields a readable connection" exactly once.

The branch is therefore covered — the claim is simply attached to the wrong
mutant.

**Repair.** "Both paths are exercised — by the `basis-lax` and `prep-lax`
mutants respectively — and both exit 1 with the failed gate named."

### F6 — NOTE. The chain's survivor counts are analytically forced.

Given that the six declared cycles are a basis, each clause pins coordinates and
the survivor counts follow with no measurement: $4^6 = 4096$, $3\cdot 4^5 =
3072$, $3\cdot 4^4 = 768$, $3\cdot 4^3 = 192$, $3\cdot 4 = 12$, $3\cdot 2 = 6$.
§6's remark that "The heavy cut is E3 — 192 to 12 — and it is the clause that
says the wing exchange is a symmetry of the *local* legs and of nothing else"
attributes significance to a factor of 16 that records only that E3 pins two of
six coordinates. Suggested addition: "The survivor counts in this column are
forced once the six declared cycles are a basis — each clause pins coordinates,
and the factor records how many. The measurement is in the second column."

### F7 — NOTE. The last chain row is equivalent to the positive control.

The six survivors are one simply-transitive orbit of the six Klein relabellings
(verified), and the multiset profile is relabelling-invariant. So "every survivor
carries 82/86/90/106" is logically equivalent to "the realized one does" — which
is the positive control. §6 calls this row "the result". The abstract does
disclose the orbit structure ("the six survivors are one relabelling orbit"),
which mitigates; the consequence is not drawn. Suggested addition to §6: "Because
those six are a single relabelling orbit and the multiset profile is
relabelling-invariant, this last row carries the same content as the positive
control; the work is done by the rows above it."

### F8 — NOTE. C10's necessity is analytic; C3's is a genuine measurement.

The target profile has four nonzero counts, so any connection reproducing it
attains all four group elements and is surjective. I measured that the set of
connections with all four counts nonzero has size **3,906** — identical to the
order-4 set. So the row "C10 group of order four | **0** of 190 | **necessary**"
could not have come out otherwise. C3's necessity ("**0** of 2,368") has no such
argument and is a real measurement — I confirmed all 96 hits satisfy C3.
Suggested: mark the C10 row a disclosure, as §12 does for the two
analytically-forced gates.

### F9 — NOTE. E4's marginal content is exactly C10, restricted.

On the twelve E3-survivors, I measured that E4 holds **if and only if** the
connection generates the full group. So the fourth species clause's entire
contribution at the last step is the generality unit's own "group of order four"
explanation, which §5 reports as not forcing. This is not a contradiction — C10
does not force globally and E4 does not either — but the contrast the paper
draws would read more honestly with: "On the twelve survivors of E3, E4 coincides
with the requirement that the connection generate the whole group; what the
species account adds over the generality unit's is the four clauses above it,
not this one."

### F10 — NOTE. The violator-census column is an algebraic identity, not a second route.

Every entry of §5's "violators reproducing the profile anyway" column equals
$96 - (\text{hits in subset})$: 90, 96, 96, 0, 95, 90, 72, 72, 72, 48, 0. My
recomputation reproduces all of them, and also confirms the identity. The
instrument does iterate the complement rather than subtract, so this is not a
false claim; but per the RUNBOOK §13 addendum from v13 #234 the two columns are
one route, and the table should not be read as independent corroboration.

### F11 — NOTE. The reason the positive control is waiver-only is not disclosed.

§12 names the four gates falsified only by a waiver, including
`XBA-POSITIVE-CONTROL`. The reason is architectural: every mutant that perturbs a
base (`rot-lax`, `completion-lax`, `field-lax`, `wingswap-lax`) trips anchors
A19–A25 first and exits before the positive control is evaluated — I observed
exactly this for `field-lax` (A23) and `wingswap-lax` (A22). Worth one sentence,
because as written a reader may infer the gate is weak when it is merely
unreachable behind exit-1 anchors.

### F12 — NOTE, and a constructive contribution: a third *species* is cheap, and it agrees.

D4 scopes the third instance as "a third instance of the species, not a third
species" because an involutive defect needs system dimension $\geq 3$. That
constraint does not force dimension exactly 3. I built a genuine third species —
**wings of dimension 4, pointers of dimension 4, carrier $4^4 = 256$**, an
exchange-invariant preparation of Schmidt rank two, and a completion
transposition of the sixteen pair labels — in about a minute of compute. Results:

| measured on the new species | value |
|---|---|
| four species clauses + the involution | all **yes** |
| $W$ fixes | **16 of 256** |
| $D$ fixes | **192 of 256** |
| the 13 gauge-fixed labels | $\mathbf 1^{\times 9}$, $W$, $WD$, $WD$, $WD$ — identical |
| distinct holonomies over the 364 walks | **4** |
| **class counts** | **82 / 86 / 90 / 106** |

(Its transposition family splits 12 / 60 / 48 across defect orders 1 / 2 / 3,
the same three-way structure as at dimension 3.)

This **confirms** the paper's mechanism at a carrier that shares nothing with
either base, and it simultaneously shows that the carrier shape is a fourth
inert parameter (F2). If the unit is reopened for repair, this instance costs
little and answers D4 directly. I offer it as a round contribution in the sense
of RUNBOOK §6.

### F13 — NOTE. C2a's control gap has an unstated positive control.

§8 and D7 name C2a's missing violator honestly. Neither says that the
equivariance machinery is nevertheless exercised: C2b and C2c run the identical
`apply_action` path and return False on the realized connection, with subsets 64
and 136 (both reproduced). Suggested addition to §8: "The machinery is not
untested: C2b and C2c evaluate through the same induced-action code and both
return False on the realized connection, so the path that would report a failure
of invariance is exercised."

---

## 8. What survived the attack

Stated plainly, because it is the larger part of the report.

- **Every load-bearing number in the paper reproduced on an independent
  instrument.** The arena (13 quantities), the census (8), the chain (11), the
  twelve candidates in four columns each (48), the eleven violators and their
  profiles (22), the gauge layer (4), the six base readings (21). **Zero
  numerical discrepancies.**
- **The central claim is correct.** The two bases do realize one and the same
  point of the 4,096; I obtained it from a tree-free construction of the cycle
  space and a different number field, and it is the same point.
- **The derivation of §7.1 is correct**, link by link, and I re-derived it by
  hand as well as by machine.
- **C1's residual sentence is exactly right** — the 6 hits inside C1 are precisely
  the "preparation square alone" pattern.
- **The scoping of the admission-table residual (K3) is honest in all nineteen
  places it appears.** So is the subset-size-1 disclosure (K1).
- **The instrument is strong.** Exact arithmetic throughout with zero floats and
  zero tolerances; no gate predicate reaches the mutant flag; four hash pins that
  fire on genuine source corruption; a cache-refusal mechanism that is real and
  correctly counted; byte-level determinism; and byte-for-byte regeneration of
  the delivered output.
- **The mutant census's disclosures are unusually candid** — both denominators
  printed, the four waiver-only gates named, the analytically-forced clauses
  marked as disclosures rather than evidence.

No finding in §7 shows a false number. All five substantive findings (F1–F5) are
claims broader than their gate, or a reason attached to the wrong mechanism.

---

## 9. Recomputation count

**174 independent recomputations**, none importing the unit:

| block | count |
|---|---|
| arena and path space (graph, walks, cycle space, declared cycles) | 16 |
| the 4,096 census and the five-clause chain | 23 |
| automorphisms, twelve candidates, violator census, necessity claims | 56 |
| both bases and the third instance rebuilt in $\mathbb{Q}(\zeta_{16})$ | 21 |
| K2 parameter attack (inertness, transposition family, the escape) | 8 |
| the new-species dimension-4 instance | 4 |
| gauge sweep, cache arithmetic, eleven violators | 16 |
| instrument audit (4 hash pins, 15 mutants, 3 prose reconstructions, AST, determinism, regeneration) | 27 |
| steering audit and C1's residual | 3 |
| **total** | **174** |

Scripts: `r1_graph.py`, `r1_census.py`, `r1_cand.py`, `r1_bases.py`,
`r1_k2attack.py`, `r1_k2sweep.py`, `r1_dim4.py`, `r1_k5.py`, `r1_k4.py`,
`r1_recon.py`, all in the session scratchpad. No repository file was modified;
the delivered code was executed only inside a scratch mirror.

---

## 10. Grade

The unit's arithmetic is sound and its central result is correct: the two bases'
profiles agree because their connections are one point of the 4,096, and within
the declared arena the species clauses do force that point up to naming. I could
not break a single number, and I tried on my own instrument in a different field
with a tree-free construction of the cycle space.

Two claims are broader than their gates. The four-clause mechanism is incomplete
— I exhibit an instance satisfying all four clauses whose profile is
[42, 46, 46, 72, 78, 80], because the arena's involution condition is a fifth,
unlisted clause (F1). And the third instance's prediction risked one bit rather
than three, because two of its three declared variations are provably incapable
of reaching the connection (F2). Both are repairable by wording plus one added
clause row; neither disturbs a measured value, and both are already half-conceded
in §11.3, D4 and D5.

The pre-registered outcome **XBA-SHARED-STRUCTURE-IDENTIFIED** stands at the
declared scope, provided F1's fifth clause is carried in the statement of the
property. `SPECIES-FORCED-SPLIT` should be named as five clauses, not four.

> ### **ACCEPT-WITH-FIXES**
>
> Blocking: **F1**, **F2**. Required before terminal: **F3**, **F4**, **F5**.
> Recommended: F6–F13, of which F12 is a constructive contribution the repair
> may adopt with credit.

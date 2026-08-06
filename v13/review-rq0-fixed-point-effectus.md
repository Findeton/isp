# CYCLE B HOSTILE REVIEW — R2, THE EFFECTUS / ORDER LENS

**Reviewer:** R2 (effectus/order lens; primary kill-shot **K3**).
**Protocol:** `v13/note-rq0-fixed-point-hostile-protocol.md` at commit
`6effc7a`, followed exactly; this review is judged against that protocol only.
**Object under review:** commit `6fab072`. All four pinned SHA-256 prefixes
**verified by me before reading**:
`paper-rq0-task-record-fixed-point.md` → `9afc0ad8578e` ✓;
`rq0_l0_fixed_point_exact.py` → `c77e94561d14` ✓;
`_output.txt` → `1d93073ff1e3` ✓; `_receipt.json` → `eef553549a38` ✓.
**Pin:** `7a80e39`. **Immutable base:** `6c2d7b8`.

**Discipline statement.** All rebuilds are my own exact code in the session
scratchpad (`r2_core.py`, `r2_k3.py`, `r2_exact.py`); nothing is imported
from the unit's code; interpreter `/opt/homebrew/bin/python3.13`; integer and
`Fraction` arithmetic only, no float in any path; no child agents; no git
mutations; this is the single repo file I write.

**Disclosure (protocol-relevant).** While searching the permitted artifacts
for the authoritative list of "worker deviations (1)–(8)" required by the
common gates, I read past my assigned LOG window (#97–#115) and saw the
LOG #118 summary of another reviewer's frozen verdict. I stopped at once and
read no review file. Every finding below was already established in my
scratchpad code before that read — specifically F2 (the `cl_of` tautology,
established while first reading `run_g1`/`run_g2`), F1 (the Proposition 4.1
refutation) and the whole K3 result. Where my F2 overlaps another lens's
"one self-comparing gate", the overlap is convergent, not derived. I flag
this so the adjudicator can discount the overlap rather than double-count it.

---

## 0. Verdict

> ## **ACCEPT-WITH-FIXES**

**Zero numerical disagreements.** Every number I recomputed — thirty of them,
listed in §2 — agrees exactly with the unit. I found no false computed
value anywhere in the paper, the receipt or the output.

**But one theorem is false as stated** (Proposition 4.1, the "only if"
direction — F1), and it is banked in §6 under "What is nevertheless earned".
And the evidence architecture behind the central headline is weaker than it
appears: **six gates cannot fail by construction** (F2), so the `cl = id`
stratum table is asserted at atom counts 1 and 5 rather than measured. I
supplied the missing measurement myself and **the headline is true** — the
mathematics survives; it is the gating that must be repaired.

**K3, my primary kill-shot, fails to kill — decisively, and in the paper's
favour.** The degeneracy is not an artifact of an overly generous future
class. It survives on four independently motivated law families including
the minimal irreversible one (§3). The paper may therefore *strengthen*
Theorem 4.2, not defend it.

The registered outcome `RQ0-L0-BLOCKED-AT-DE-SMUGGLING` is correct and is
**reinforced** by my findings, not threatened by them.

---

## 1. K3 ADJUDICATION (primary kill-shot) — THE DEGENERACY IS NOT AN ARTIFACT

**The attack as specified.** "`cl = identity` is proved UNDER REPREPARE
CLOSURE. Recompute `cl` on the committed law families withOUT reprepares. If
`cl` is selective for a physically motivated admitted family, the
'degenerate closure' headline is an artifact of an overly generous future
class. Decide, with the family declared."

### 1.1 The structure theorem that decides it

Working in the paper's order (`π ⊑ σ` means "σ refines π"; ⊥ = trivial
record, ⊤ = the atom instrument `Cl_op(S)`), for **any** admitted family 𝔽,
write `C(𝔽) = {comp(F) : F ∈ 𝔽}`. Then

- `Pres_𝔽(π) = {F ∈ 𝔽 : π ⊑ comp(F)}`, so
- `cl_𝔽(π) = ⊓ { c ∈ C(𝔽) : π ⊑ c }`, the empty meet being ⊤.

Hence:

> **R2-Theorem A (Moore family).** `Fix(cl_𝔽)` is exactly the set of meets of
> subsets of `C(𝔽)`, together with ⊤. In particular `Fix(cl_𝔽)` is always a
> meet-subsemilattice of the record lattice containing ⊤.

Verified against direct computation on **1,500 pseudo-random families** at
n = 3, 4: **0 mismatches**. This is the general statement the paper is
missing; every K3 question is a corollary of it.

> **R2-Theorem B (the top is always fixed).** For **every** admitted family
> 𝔽 whatsoever — including 𝔽 = ∅ — `cl_𝔽(⊤) = ⊤`.
> *Proof.* Extensivity gives ⊤ ⊑ cl(⊤); ⊤ is the greatest element of the
> record lattice; hence equality. ∎
> Checked on 4,000 pseudo-random families: **0 violations**.

> **R2-Theorem C (the deciding sufficient condition).** `cl_𝔽 = id` as soon
> as 𝔽 contains, for each ordered pair of atoms k ≠ l, the elementary
> **sector merge** `f_{k→l}` (map sector k into sector l, act as the identity
> on every other sector). *Proof.* `comp(f_{k→l})` is the partition whose
> only non-singleton block is {k,l}; every partition is the meet of the
> two-block partitions it contains; apply Theorem A. ∎

Theorem C matters because **`f_{k→l}` discards nothing and reprepares
nothing inside a kept sector** — it is strictly weaker than the paper's
condition R, which discards the whole state on every block.

### 1.2 The declared families and the recomputation

Every family below contains the identity and is declared with its laboratory
reading. `|Fix(cl_𝔽)|` out of Bell(n) records:

| declared family | laboratory reading | n=1 | n=2 | n=3 | n=4 | n=5 |
|---|---|---|---|---|---|---|
| **ALL** — every left-total sector relation | the unit's implicit class | 1/1 | 2/2 | 5/5 | 15/15 | — |
| **DET** — every deterministic sector map [n]→[n] (a monoid) | classical relabel-and-merge postprocessing of the flag; **no quantum reprepare of any kind** | 1/1 | 2/2 | 5/5 | 15/15 | **52/52** |
| **FUNNEL** — identity + the n(n−1) elementary sector merges (3, 7, 13, 21 futures) | the minimal irreversible law; nothing discarded, nothing reprepared in a kept sector | 1/1 | 2/2 | 5/5 | 15/15 | **52/52** |
| **NOREP** — ALL minus *every* sector reprepare R_π (the literal K3 instruction) | the committed class with reprepares deleted | 1/1 | 2/2 | 5/5 | 15/15 | — |
| **UNITAL** — total-support relations (= supports of doubly stochastic sector maps, Birkhoff) | noise that never increases purity; no measure-and-reprepare | 1/1 | 2/2 | 5/5 | 15/15 | — |
| **REV** — atom permutations only (a group) | the reversible law — the maps K1/Theorem 4.6 must admit | 1/1 | **1**/2 | **1**/5 | **1**/15 | **1**/52 |

### 1.3 The decision

**K3 FAILS TO KILL. The degeneracy headline is not an artifact of the
admitted class.** Four physically motivated families that contain no
reprepare at all — DET, FUNNEL, NOREP, UNITAL — each give `cl = id` exactly.
FUNNEL does it with **seven futures at n = 3 and twenty-one at n = 5**. The
degeneracy is therefore not bought with a generous future class; it is
forced by the presence of *any* pairwise sector merge, i.e. by the mere
existence of irreversible operations.

**The single escape is REV, and it makes the smuggling worse.** Under a
reversible-only law `C(𝔽) = {⊤}`, so `cl` is *constant at ⊤* and
`Fix = {⊤}` — one fixed point out of Bell(n). That is "selective", but what
it selects is exactly ⊤ = `Cl_op(S)` = **the manufactured record**. So the
one family for which the closure is selective is the family for which the
manufactured measure is the *unique* fixed point.

**And no family escapes at all**, by Theorem B: the manufactured record is
the top of its own record lattice, so it is fixed under *every* admitted
law. **There is no law family, generous or restricted, on which this closure
rejects the manufactured record.** K3 is closed.

---

## 2. INDEPENDENT NUMBERS TABLE

All recomputed with my own code, exact arithmetic, nothing imported.
"Unit" = the paper/receipt value. **Disagreements: none.**

| # | quantity | my value | unit | how I got it independently |
|---|---|---|---|---|
| 1 | record strata, n=1..5 | 1, 2, 5, 15, 52 | 1,2,5,15,52 | restricted-growth-string enumerator **and** the binomial recurrence B(n+1)=Σ C(n,k)B(k) (neither is the unit's Bell triangle) |
| 2 | strictly-refining record pairs, n=2..5 | 1, 7, 45, 306 → **359** | 359 | direct count, **and** closed form Σ_π Π_B Bell(\|B\|) − Bell(n) |
| 3 | left-total relations (2ⁿ−1)ⁿ | 9; 343; 50,625 | same | enumeration |
| 4 | declared n=5 subfamily size | **84,375** = 3125 + 5·26·625 | 84,375 | reconstructed "at most one multi-valued atom" from scratch |
| 5 | Lemma 3.2 membership tests n≤4 | 18 + 1,715 + 759,375 = **761,108** | 761,108 | exhaustive rerun, 0 mismatches |
| 6 | Lemma 3.2 tests at n=5 | 84,375 × 52 = **4,387,500** | 4,387,500 | arithmetic + rerun |
| 7 | Prop 3.3 test total | 1·9 + 7·343 + 45·50,625 + 306·4,000 = **3,504,535** | 3,504,535 | reconstructed term by term — **this exposes the n=5 prefix, see F5** |
| 8 | join-closure tests | **6,087** | 6,087 | direct, **and** closed form Σ_π Bell(#blocks π)² over n=2..5 |
| 9 | distinct preserved-record sets | 2, 5, 15, 52 | same | direct |
| 10 | Prop 3.5 family pairs | 3·C(250,2) = **93,375** | 93,375 | reconstructed |
| 11 | adjunction tests | Σ(381+Bell n)·Bell n = **30,422** | 30,422 | reconstructed from the unit's family recipe |
| 12 | fixed points from the **exhaustive** future family, n=2,3,4 | 2/2, 5/5, 15/15 | same | my own Core∘Pres over all 9 / 343 / 50,625 relations |
| 13 | fixed points from the **full** declared n=5 family | **52/52** | 52/52 (asserted) | **the unit never computes this; I did** — see F2 |
| 14 | dual order-isomorphism, n≤4 | Pres(p)⊆Pres(q) ⟺ p refines q | same | exhaustive |
| 15 | centre dim: C², M₂, M₂⊕ℂ, ℂ⁵, M₄⊕ℂ, ℂ, PVM211, PVM22 | 2, 1, 2, 5, 2, 1, **4**, **3** | same | my own exact commutant solve over the matrix-unit basis |
| 16 | fixed-point counts per fixture | 2, 2, 52, 2, 15, 5 | same | Bell(centre dim) |
| 17 | branch-memory minima (preserving / eraser / bundle) | **1 / 5 / 5** | 1 / 5 / 5 | my own minimal-sufficient-statistic routine on the committed likelihoods |
| 18 | TV(p₀,p₁) | **1/2** | 1/2 | exact |
| 19 | optimal recovery deficit | **1/4** at d=(1/2,1/2) | 1/4 | exact rational min-max over a 1001-point grid; attains the bound TV/2 |
| 20 | squared coherence loss | 4·(3/16) = **3/4** | 3/4 | exact |
| 21 | inherited seams | 6 (2+1+1) + 3 (2+2) = **9** | 9 | enumeration of partitions of a 4-set by type |
| 22 | ℂ⁵ core restricted to branch labels | discrete; **not** among the nine | same | direct |
| 23 | s₂² | (I, **5**I) | (I,5I) | exact: (2X+Z)² = 5I |
| 24 | squared norms s₂ / −3s₁+s₂ | **5→1**, **10→8** | 5→1, 10→8 | exact, from B² = cI (no root extraction needed) |
| 25 | dim(S ∩ Z(C*_e(S))) | **1** | 1 | exact rank of the scalarity conditions |
| 26 | sharpness grid: tested / sharp / violations | 25/4/0, 125/8/0, 3375/27/0 | same | exact rational grid |
| 27 | impossibility witness V = (1,2,3,4,0) | VᵀV = VVᵀ = I over ℤ; atom map [4,0,1,2,3], a bijection | same | exact |
| 28 | Lemma 3.2 **beyond the unit's scope**, n=5, all \|sup\|≤2 relations | 759,375 relations × 52 = **39,487,500 tests, 0 mismatches** | not attempted | 9× the unit's n=5 family, and unlike it every atom may be multi-valued at once |
| 29 | Lemma 3.2 at **n=6 and n=7** | 4,060,000 + 4,385,000 tests, **0 mismatches** | not attempted | fixed-seed integer LCG sweeps |
| 30 | antitonicity over the **full** declared n=5 family | **25,818,750 tests, holds** | 1,224,000 (prefix) | closes F5 in the unit's favour |
| 31 | adjunction over **all** 1-, 2- and 3-element families at n=3 | **33,629,435 tests**, holds | 30,422 total | plus 1,191,015 strided pairs at n=4 |

**Reproduction, determinism, mutants (common gate).** I copied the pinned
source into my scratchpad and ran it there (never in the repo). It exits 0
and regenerates the committed `_receipt.json` and `_output.txt`
**byte-identically** — a stronger determinism check than the paper's
"two consecutive runs", since it ties the *committed* artifacts to the
*pinned* source. `git status` clean throughout. I also ran
`--falsification-selftest`: **6/6 mutants killed**, each exiting 1 with a
printed anchor failure. See F9 for what this does *not* cover.

---

## 3. FINDINGS, RANKED

### F1 — MAJOR, fix-real. **Proposition 4.1's "only if" direction is false.**

The paper states: the trivial record is a fixed point of `cl` **iff** the
admitted future family contains a future that preserves no nontrivial record
(i.e. some F with `comp(F) = ⊥`). The proof reads:

> "…which by Proposition 3.4 says the generated partition of the comp(F) is
> the one-block partition, **that is, some F has comp(F) trivial**."

The clause after "that is" is a non sequitur. `cl(⊥) = ⊓ C(𝔽)`, and a meet
of partitions can be trivial with **no single term trivial**.

**Explicit counterexample, composition-closed, with admitted operations
only.** On a three-atom classical boundary take the deterministic sector
maps `a = (0,1,2) ↦ (0,0,2)` and `b = (0,1,2) ↦ (0,2,2)`. I verified by
closure that ⟨id, a, b⟩ = {id, a, b} — a genuine monoid, closed under
composition. Then

- `C = { discrete , {01|2} , {0|12} }`, meet = `⊥` → **the trivial record IS
  a fixed point** (`cl(⊥) = ⊥`, computed);
- **no** admitted future has `comp(F) = ⊥`: `a` preserves the nontrivial
  record {01\|2}, `b` preserves {0\|12};
- `Fix(cl) = { ⊤, {0|12}, {01|2}, ⊥ }` — 4 of 5, so `cl` is genuinely
  selective here, and the paper's stated criterion gives the wrong answer.

**Scope of the counterexample, stated against myself.** The law is closed
under composition but not under atom relabelling. I checked the repair
hypothesis: at n = 3 and n = 4, ⟨S_n, one non-injective map⟩ *does* contain
a constant map (27 and 256 elements respectively), so under
composition-**and**-relabelling closure the two conditions do coincide. This
creates a visible tension with Theorem 4.6/K1, which needs relabellings to
be admitted — so the paper can repair either way, but it must repair.

**Why this matters beyond the local error.** Proposition 4.1 is banked in §6
as earned, and it is the unit's *correction* of the pin's own false premise
("the trivial instrument is always fixed"). A correction of a false premise
that is itself false must not be carried forward silently.

**Recommended repair (hypothesis-free, and it is what my code computes):**

> The trivial record is a fixed point of `cl` if and only if the meet of the
> collision partitions of all admitted futures is trivial — equivalently, iff
> the admitted futures' collisions jointly connect the atom set. A single
> record-erasing future is sufficient (and is what condition R supplies), but
> it is not necessary.

Neither direction of the stated biconditional is tested by the receipt:
G2-01 is a tautology (F2) and G2-02 tests only the identity-only law.

---

### F2 — MAJOR, fix-real. **Six gates cannot fail: `cl_of` returns its own argument.**

Both `run_g1` and `run_g2` compute the closure as

```python
def cl_of(part, n):
    gens = [tuple(frozenset({k}) for k in range(n)), reprepare_support(part, n)]
    return core_avail(gens)
```

`comp(identity) = discrete` and `comp(R_π) = π`, so this is
`meet(discrete, π) = π` — **identically, for every π, every n, and every
law**, including laws where condition R fails. I verified `cl_of(p,n) == p`
for all records at n = 1..5. Consequently these gates compare `p` with `p`:

| gate | claim it appears to test | what it actually evaluates |
|---|---|---|
| G1-05 | `cl` is extensive | `refines(p, p)` — always true |
| G1-06 | `cl` is monotone | trivial |
| G1-07 | `cl` is idempotent | trivial |
| G2-01 | trivial record fixed under R | `p == p` |
| G2-03 | **cl = id; strata 1,2,5,15,52** | `p == p`, Bell(n) times |
| G2-10 | **THE DISCRIMINATOR: manufactured record survives** | `discrete(n) == discrete(n)` |
| G1-09 | closed records ↔ closed families | records side is Bell(n) by construction (the *families* side is real, and their equality is a genuine injectivity test) |

The non-circular checks are **G2-03b and G2-05 only, and only at n ≤ 4**.
So the two extreme strata of the headline table — n = 1 and **n = 5, the
52/52 that carries the ℂ⁵ eraser fixture** — are asserted, never measured.
G2-06/G2-07 likewise *report* `bell(core_size(alg))` rather than computing a
fixed-point set.

**This is not a claim that the headline is wrong.** I computed `cl` at n = 5
from the full 84,375-relation declared family, non-circularly: **52/52
fixed**. The theorem is true. What fails is the gating: the unit's own
evidence for its central result is, at two strata, a tautology.

**Aggravating factor.** All six falsification mutants break inherited
*anchors* (A07, A12, A14, A16, A26, A28). **No mutant breaks any G1 or G2
gate** — and the six gates above could not have detected one if it did.
The falsification self-test therefore certifies the anchor plumbing, not the
unit's own new results.

**Repair:** replace `cl_of` at n = 5 (and n = 1) with the family-based
computation, or state plainly in §4.2 that at n = 5 the strata number is the
theorem's consequence rather than an independent check, and add one mutant
that perturbs `comp` or `images_disjoint` so a G1/G2 gate can fail.

---

### F3 — MAJOR, fix-real (and it strengthens the paper). **The discriminator was structurally unable to reject the manufactured record, for a reason far more elementary than Theorem 4.6.**

The manufactured record is the atom instrument of `A_P` — i.e. **the top of
its own record lattice** (the code sets `manufactured = discrete(n)`
precisely because of this). By R2-Theorem B, every closure operator on a
poset with a greatest element fixes that element. Therefore:

- **Theorem 4.5 clause 1 is vacuous.** "The manufactured measure is a fixed
  point" holds for *every* admitted law, *every* definition of `Pres` that
  yields a closure operator, and independently of condition R, of Theorem
  4.2, and of the availability repair. It could not have come out otherwise.
- **Theorem 4.5 clause 2** ("under the composite reading the manufactured
  record is the *unique* fixed point") is a restatement of #103's result
  that the manufactured boundary's core is the manufactured PVM, routed
  through Theorem 4.4.
- **The pre-registered outcome `RQ0-L0-NO-NONTRIVIAL-FIXED-POINT` was
  unreachable a priori.** ⊤ is always fixed and is nontrivial whenever the
  core has ≥ 2 atoms, so Corollary 4.3's biconditional holds for every law,
  with or without R. The outcome was not refuted by the computation; it was
  refuted by the record lattice having a greatest element.

The paper's instinct is right ("existence is not evidence of selection; it
is evidence of vacuity") but it under-diagnoses: the vacuity is not that
*every* record is fixed, it is that *this particular record* is the one
record that is fixed no matter what. Theorem 4.6's covariance obstruction
remains the deeper and more interesting statement — but it is not what
settles the discriminator, and the paper currently reads as though the
discriminator's failure needed it.

---

### F4 — MODERATE, fix-real. **Condition R is far stronger than the theorem needs; record the K3 robustness.**

Theorem 4.2 is stated "under condition R" — read the block label, **discard
the rest**, reprepare a fixed state. By R2-Theorem C the conclusion already
follows from the elementary sector merges, which discard nothing in a kept
sector; and it holds on DET, NOREP and UNITAL as well (§1.2). A reader is
entitled to conclude from the present text that `cl = id` is an artifact of
a strong laboratory postulate. It is not, and the paper should say so — this
is the K3 answer and it belongs in §4.2.

---

### F5 — MODERATE, fix-real. **Proposition 3.3's 3,504,535 mixes exhaustive and prefix-sampled scopes without disclosure.**

The paper says only "Verified on 3,504,535 strict-refinement tests." I
reconstructed the total term by term: 1·9 + 7·343 + 45·50,625 + 306·**4,000**.
The last term is **1,224,000 tests — 34.9 % of the advertised total** — and
it runs over `fam5[:4000]`, a *lexicographic prefix* of the declared n = 5
family consisting of all 3,125 single-valued (functional) relations plus 875
others, all of which have their one multi-valued support on atom 0. The
receipt discloses this ("first 4000 declared futures at n=5"); the paper does
not, and the result's tags (`[FIN]`, `[EXH-4]`) do not cover it.

**Closed in the unit's favour:** I ran antitonicity over the **entire**
84,375-relation declared family — 25,818,750 tests — and it holds.

---

### F6 — MODERATE, fix-real. **The "declared subfamily at atom count 5" is never declared in the paper, and it is the structurally easiest family.**

The scope box and Lemma 3.2 both say "a declared subfamily of 84,375
relations at atom count 5". *Which* subfamily appears only in the receipt
(`at most one multi-valued atom`). A reader cannot audit the scope tag from
the paper. Worse, that family is close to the best case for the component
lemma: with at most one branching atom the collision graph is essentially a
disjoint union of fibres, so the chained-overlap configurations that make
Lemma 3.2 non-obvious barely occur.

**Closed in the unit's favour, at my own expense:** I re-verified Lemma 3.2
at n = 5 over **all 759,375 relations with |sup(k)| ≤ 2 for every k** (9×
larger; every atom may branch simultaneously) — 39,487,500 tests, **zero
mismatches** — and over fixed-seed sweeps at **n = 6 and n = 7** (8.4 M
further tests, zero mismatches). Lemma 3.2 is sound well beyond the declared
scope. The paper should name its family in one clause.

---

### F7 — MINOR, fix-cosmetic. **Proposition 3.5 carries the wrong scope tag.**

Tagged `[FIN]`, `[FIX]`; `[FIX]` is defined in the scope box as "verified on
the committed fixture set only". It was verified on 93,375 abstract declared
*family pairs* at n = 3, 4, 5 — not on the committed fixtures at all. The
tag should be the declared-subfamily tag, not `[FIX]`.

Related, and worth one sentence: the test is also nearly content-free.
`Core(G ∪ {x}) = Core(G) ⊓ comp(x)` is coarser than `Core(G)` by inspection,
so 93,375 instances of the same one-line fact add no assurance. That is not
an error, only inflated evidence.

---

### F8 — MINOR, fix-real. **Three receipt rows carry no value, so a paper sentence is unbacked.**

G1-05, G1-06 and G1-07 all have `"value": null`. The paper asserts
"extensivity, monotonicity and idempotence were verified for all records at
atom counts 1 to 5" — a scope claim with no receipt-backed number behind it.
(Given F2, what those gates verified was in any case a tautology.) Similarly
G2-05's row records a scope string but not the 50,625 the paper quotes.

---

### F9 — MINOR, fix-real. **Mutants and determinism are claimed in §8 but carried by no committed artifact.**

The receipt has no mutant section and no determinism record; the falsification
self-test writes to stdout only and its result is not persisted anywhere in
the four whitelisted files. The common gate asks reviewers to re-confirm
determinism and mutants "from the receipt", which is not currently possible.
I confirmed both independently (byte-identical regeneration; 6/6 killed), so
the claims are **true** — but they should be receipt rows.

---

### F10 — MINOR, fix-cosmetic. **`Core(∅)` is never defined, and the adjunction needs it.**

Theorem 3.6 quantifies over "every future family 𝒢". At 𝒢 = ∅ the left side
of the adjunction is vacuously true, so soundness requires
`Core(∅) = Cl_op(S)` (the empty meet = ⊤). Proposition 3.4's construction
("the partition generated by the union of the comp(F)") is undefined on the
empty union, and the unit's `core_avail` would raise on an empty list. No
computation is affected — the identity is always admitted, so the case never
arises in the runs — but the convention is exactly what R2-Theorem A needs,
and one clause fixes it.

---

### F11 — MINOR, under-claim. **Corollary 4.3 is law-independent.**

Stated under condition R; by R2-Theorem B it holds for every admitted law.
Free strengthening.

---

## 4. COMMON GATES

| gate | disposition |
|---|---|
| **Paper vs receipt** (spot ≥10) | **PASS with F8.** I traced 30 paper numbers to receipt rows (308; 16; 1/4; 1/2; 16 triples; 9-in/7-out; 25/125/3375; 9/343/50,625; 761,108; 84,375; 4,387,500; 3,504,535; 2,5,15,52; 93,375; 30,422; 2,5,15 bijection; 1-atom/5-atom; 359; 1,2,5,15,52; the six fixture counts; centres 4 and 3; centres 2,2,5,2,4,3; Choi rank 1; −1/2; 5,1,10,8; dim 1; 3/7; 3/16, 3/4; nine seams; (1,2,3,4,0); 57/57; 34/34). All present and matching **except** the three null-valued closure rows and the 50,625 in G2-05 (F8), and the mutant/determinism claims (F9). |
| **Scope tags on every result** | **PASS with F5, F6, F7.** All 19 numbered results carry a tag. Two tags misdescribe their evidence (F7), and two sentences carry numbers that exceed their tags (F5, and the n=5 stratum of Theorem 4.2 under F2). |
| **Forbidden vocabulary** | **PASS.** Swept the paper for tensor / locality / overlap / topology / causality / spacetime / QFT / gravity / manifold / Lorentz / region: the single hit is the disclaimer sentence itself ("carries no spacetime meaning"). "Markov" occurs only in the pre-registered outcome name and in its disclaimer paragraph, as the paper states. Every "composite/composition" is either the outcome-forgetting composite `D_M`, the declared Reading-B composite, or the inherited *sequential flagged composition* postulate — no two-boundary combination claim anywhere. |
| **Prose vs gates** | **PASS with F3.** No claim is broader than its measurement except Theorem 4.5's "survives", which is broader than the paper realises *in the paper's own favour* (F3). The degenerate-satisfaction disclosure in §5.1 is kept ("all 52 records on the five-atom core are equally fixed, so the closure prefers none of them") — that sentence is the honest one and must survive editing. |
| **Deviations (1)–(8)** | **CANNOT BE DISCHARGED AS SPECIFIED.** The authoritative list is not in any artifact I am permitted to read; it lived in the worker's delivery message, and LOG #115 records only its acceptance and one member. I adjudicate what I can reconstruct from pin-vs-paper: (i) *the pin's ambiguous target closure read both ways* (Reading A availability-adjoint, Reading B #111-core) — **fix-real, correctly handled**; the split verdict is the honest result and both readings are gated. (ii) *the pin's instruction "prove [the trivial fixed point] is always fixed" was refuted rather than executed* — **fix-real, correctly handled in intent, but the replacement is itself false (F1)**. (iii) *the G3.1 negative control is satisfied degenerately* ("nothing is promoted because everything is fixed") — **fix-cosmetic**, since §5.1 discloses it in the same paragraph. **Request to the adjudicator:** supply the (1)–(8) list to the panel or drop the gate; a reviewer cannot certify a list he cannot see. |
| **Anchors vs committed #103/#111 values** | **PASS.** 34/34, exit-1-only. I independently recomputed the parent values I could reach from the committed artifacts: the two dephasing laws, the reset outputs, TV 1/2, deficit 1/4, coherence 3/16 → 3/4, minima 1/5/5, centres 4 and 3, centres 2/2/5/2, nine seams, s₂²=(I,5I), norms 5→1 and 10→8, dim 1, the 5-cycle. All agree. |
| **Determinism / mutants / floats** | **PASS (re-derived, not from the receipt — F9).** Byte-identical regeneration from the pinned source; 6/6 mutants killed; the receipt's AST float sweep reports zero float literals and zero float-producing calls and I confirm the sweep is structural (AST-based, not substring), with `anchor_type_violations: []`. My own rebuilds are float-free by construction. |

---

## 5. PER-RUNG CONFIRMATION LINES

**(a) The G0 collapse — CONFIRMED** (at order-lens depth; the 308
instrument–effect pairs are R3's assignment). `D_M = Σ_r m_r = I_S` is
clause (3) of the inherited instrument definition, so `Pres_lit` is the
constant map at `Fut(S)`, and any composite with a constant map is constant:
the literal fixed-point equation carries no information about M. I
independently confirm the collapse *witness*: the no-write reset has optimal
recovery deficit exactly **1/4**, attaining the analytic bound TV(p₀,p₁)/2,
so a record-destroying future genuinely sits inside the literal family.

**(b) The Galois connection for the availability reading — CONFIRMED, and
strengthened.** Antitonicity of `Pres`, well-definedness and antitonicity of
`Core`, and the two-sided adjunction all hold. My verification exceeds the
unit's: the adjunction over **all 1-, 2- and 3-element families at n = 3**
(33,629,435 tests) plus 1,191,015 strided pairs at n = 4, against the unit's
30,422 total; antitonicity over the **full** declared n = 5 family
(25,818,750 tests) against the unit's 4,000-relation prefix. Lemma 3.2 — the
collision-partition lemma — I re-derived and re-proved (both directions turn
only on the fact that distinct connected components have disjoint
image-unions, which is immediate from non-adjacency), and verified beyond
the unit's scope at n = 5 (39.5 M tests, richer family), n = 6 and n = 7.
The dual order-isomorphism `Pres(p) ⊆ Pres(q) ⟺ p refines q` holds
exhaustively at n ≤ 4. **The Galois core is sound.**

**(c) The cl = identity degeneracy — CONFIRMED as a fact; NOT confirmed as
gated at two strata.** `cl = id` is true: I recomputed it from the
exhaustive future family at n = 2, 3, 4 and from the full declared family at
n = 5 (**52/52**, which the unit never computes). The strata table
1,2,5,15,52 is correct. But at n = 1 and n = 5 the unit's own evidence is
the tautological `cl_of` (F2), and the degeneracy is *far more robust than
the paper claims* — it survives on every law family admitting elementary
sector merges (F4, §1).

**(d) The discriminator failure — CONFIRMED, and it is stronger and more
elementary than the paper states.** The manufactured measure survives. But
it survives under *every* admitted law, because it is the top of its own
record lattice and every closure operator fixes the top (F3). The
discriminator as posed in the pin asked whether a closure operator rejects
the greatest element of its lattice; the answer was fixed before any
physics entered.

**(e) The one-boundary impossibility theorem — CONFIRMED at the level my
lens can reach.** The witness is exact: V = the 5-cycle (1,2,3,4,0) is
unitary over ℤ (VᵀV = VVᵀ = I, verified) and induces the atom bijection
[4,0,1,2,3] on the five central projections of ℂ⁵. The covariance step
rests on #111 Cor 5.6 and on the permutation being *admitted* — K1 and K4,
which are R1's and R3's assignments, not mine. I add one order-lens remark:
Theorem 4.6 is not what defeats the discriminator (F3 does that
law-independently and without any covariance premise), so if K1 or K4 forces
Theorem 4.6 to be rescoped, **the verdict does not move**. That is a
robustness property of the paper worth stating explicitly.

**(f) `RQ0-L0-BLOCKED-AT-DE-SMUGGLING` as the correct pre-registered
instantiation — CONFIRMED.** The un-typed object — a task-independent
selector on the fixed-point set — is exactly what is missing, and my K3
result sharpens *why*: no restriction of the admitted future class supplies
one, because the manufactured record is fixed under every law (Theorem B),
and the only class for which the closure is selective at all (REV) makes the
manufactured record its **unique** fixed point. The two dispositioned
outcomes are also correct, with one refinement:
`RQ0-L0-NO-NONTRIVIAL-FIXED-POINT` was **structurally unreachable**, not
refuted by measurement (F3).

---

## 6. SENTENCES TO REWRITE

1. **§4.1, Proposition 4.1 statement.** Replace "if and only if the admitted
   future family contains a future that preserves no nontrivial record" with:
   *"if and only if the meet of the collision partitions of the admitted
   futures is trivial — equivalently, iff the admitted futures' collisions
   jointly connect the atom set. A single record-erasing future is
   sufficient, and condition R supplies one; it is not necessary."* Delete
   the "that is, some F has comp(F) trivial" clause from the proof, and add
   the ⟨id, a, b⟩ counterexample or the relabelling hypothesis. **(F1)**

2. **§4.2, after Theorem 4.2.** Add: *"Condition R is stronger than needed.
   The conclusion already follows if, for every pair of atoms, the law
   admits the elementary sector merge that maps one sector into the other
   and acts as the identity elsewhere — a future that discards nothing in a
   kept sector. The degeneracy is therefore not an artifact of a generous
   admitted class: it holds equally for the deterministic classical
   postprocessings, for the unital futures, and for the admitted class with
   every reprepare removed."* **(F4, K3)**

3. **§4.2, the strata sentence.** "Fixed-point counts are 1,2,5,15,52 out of
   1,2,5,15,52 records" → say which strata are measured from the future
   family (n = 2,3,4 exhaustively; n = 5 from the declared family) and which
   follow from the theorem. **(F2)**

4. **§4.4, Theorem 4.5 / §4.5 opening.** Add before the covariance argument:
   *"The manufactured record is the atom instrument of its own boundary,
   hence the greatest element of that boundary's record lattice; and every
   closure operator fixes the greatest element. Clause 1 therefore holds for
   any admitted law and any closure — the discriminator could not have
   rejected it. The covariance obstruction below explains something
   stronger: why no criterion, closure-shaped or not, can separate the two
   boundaries."* And in §4.2/§6, note that
   `RQ0-L0-NO-NONTRIVIAL-FIXED-POINT` was unreachable a priori rather than
   refuted. **(F3)**

5. **§3.2, Proposition 3.3's verification sentence.** "Verified on 3,504,535
   strict-refinement tests" → *"…of which 2,280,535 are exhaustive at atom
   counts 2–4 and 1,224,000 range over the first 4,000 relations of the
   declared atom-count-5 family."* **(F5)**

6. **Scope box + §3.1, Lemma 3.2's verification sentence.** Name the
   declared n = 5 family: *"the 84,375 relations in which at most one atom
   has a multi-valued sector support."* **(F6)**

7. **§3.2, Proposition 3.5's tag.** `[FIX]` → the declared-subfamily tag.
   **(F7)**

8. **§3.1, Proposition 3.4.** Add the empty-family convention
   `Core(∅) = Cl_op(S)`. **(F10)**

9. **§8, Reproduction.** Either persist the mutant table and the determinism
   result into the receipt, or state in §8 that both are stdout-only and not
   receipt-backed. **(F9)**

---

## 7. WHAT I ATTACKED AND FAILED TO BREAK

Recorded so the adjudicator can weigh the negatives as evidence:

- **K3 itself** — five declared no-reprepare families, all still degenerate
  (§1). The headline is robust.
- **Lemma 3.2, the collision-partition lemma** — re-derived by hand, then
  attacked computationally at 9× the unit's n = 5 scope, at a structurally
  harder family shape, and at n = 6 and n = 7. **Zero mismatches in
  52.3 million tests.** It is a theorem, and the paper is right to lean on it.
- **The adjunction** — attacked with all small families at n = 3 rather than
  the unit's hand-picked list. Holds.
- **`cl = id` at n = 5** — the one stratum the unit never computes. I
  computed it from the full declared family. **It is true.**
- **Every anchor and every load-bearing exact number** — thirty
  recomputations, **zero disagreements**.
- **Theorem 3.7's non-antitonicity** — recomputed the three minima (1, 5, 5)
  from the committed likelihoods with my own minimal-sufficient routine. The
  refutation stands: the larger task family gives the strictly finer core.

---

## 8. FINAL

> ## **ACCEPT-WITH-FIXES**

Nine fixes, of which three are structural (F1 the false biconditional, F2
the six unfailable gates, F3 the under-diagnosed discriminator) and none
disturbs the registered outcome. The Galois core is sound and, where I could
extend it, it extends. The degeneracy headline survives its primary
kill-shot and should be stated more strongly than it currently is. The
verdict `RQ0-L0-BLOCKED-AT-DE-SMUGGLING` is correct, and after these fixes
it rests on a broader base: **no admitted law family, however restricted,
yields a closure that rejects the smuggled record.**

*Freeze-on-delivery: this file is my last act on this unit.*

# R5-GAUGE (paper-18) — OPERATOR-LENS HOSTILE REVIEW

**Reviewer lens:** the from-scratch rebuild, importing nothing.
**Object:** commit a504243 — paper `3800959353b4`, code `37c232de91a6`,
output `e86be9a581a7`, receipt `1c072956ac7b`, pin `b53adba0eee0`.
**Protocol:** `v14/note-r5-hostile-protocol.md` (`16f86f0eabd2`, b215e6c).
**Grade:** **AWF** — accept with fixes.
**Recomputations:** 60 (≈48 full independent rebuilds, 12 paper↔receipt
cross-checks). **False numbers found in the receipt: zero.**
**False numbers found in the paper: two, both in the headline verdict block.**

---

## 0. Verification of the object

All five pinned digests match at HEAD **and** at a504243:
paper `3800959353b4`, code `37c232de91a6`, output `e86be9a581a7`,
receipt `1c072956ac7b`, pin `b53adba0eee0`. All eight parent-source
digests match their in-code pins (`1063401c7bb5`, `2959c5a6a84b`,
`ffd069ff3eb4`, `3dc1393b0df8`, `89c636906061`, `562e2a3d4d85`,
`f54fa11dfd07`, `602c9ac2ccc4`).

**Byte-identity: PASSES.** I mirrored only the nine pinned sources plus the
paper into a scratch tree with **no `.git` and no repo ancestry**, ran the
plain delivery run there, and both artifacts came out byte-identical to the
committed ones (`e86be9a581a7`, `1c072956ac7b`). That is #91 re-tested at my
own hands, off-tree and git-less, and it passed. The repo was not written to;
the only tracked change I made is this file.

## 1. What I rebuilt differently

Nothing was imported from the unit. Deliberately divergent routes:

| object | the unit's route | my route |
|---|---|---|
| field $\mathbb{Q}(\zeta_8)$ | integer 5-tuples, gcd-normalised | `Fraction` 4-tuples over $(1,z,z^2,z^3)$, no normalisation |
| group order | deterministic Schreier–Sims | full element enumeration (small); **none at all** for $A_{16}$ |
| class certificate | even-on-every-orbit **+ order equality** | **Jordan's theorem**: primitive + a 3-cycle $\Rightarrow \supseteq A_n$; all-even $\Rightarrow \subseteq A_n$ |
| primitivity | not computed | minimal-block union-find seeded at every pair |
| flat control | R5's reimplementation of R4 | rebuilt from **R4's paper prose only** (autocorrelation criterion, 9 axes, phase quotient) |
| coin unitarity | $U^\dagger U = I$ | $UU^\dagger = I$ |

The point of the Jordan route is that it certifies $A_{16}$ **without ever
computing an order**, so it is not a re-run of the unit's own risk.

## 2. K1 — THE GROUP. Every number reproduces.

Rebuilt from R4's 25-element alphabet upward:

- alphabet **25**; coins **640**; sectors **64 / 64 / 512**; all 640 unitary
  by the second route.
- the four parity strata are **perfect matchings** (8 disjoint dominoes
  covering all 16 sites, each).
- the plaquette holonomy is the identity off the four corners — checked in
  the full $16\times16$, not assumed.
- curvature census: **632 of 640 non-flat**, **576 of 640 non-commuting**;
  rows `DIAG 64/56/0`, `ANTI 64/64/64`, `BAL 512/512/512`. Exact match.
- the ladder, on the swap coin, every class independently certified:
  `A3` (sup 3), `A5` (sup 5), `A3×A3` (sup 6), `A3×A3` (sup 6), `A7` (sup 7),
  `A8` (sup 8) — and **identical at all 64 antidiagonal coins**.
- global: single orbit of 16, **transitive, primitive, 16 generators each a
  bare 3-cycle, all even** ⟹ $A_{16}$ by Jordan; $16!/2 = 10461394944000$
  agrees with the unit's Schreier–Sims to the digit.
- **rank 8 of 16** confirmed by exhaustive ascent — no 7-subset generates;
  witness `{(0,0),(0,1),(0,2),(0,3),(1,0),(1,2),(2,0),(2,2)}`. Local ranks
  1, 2, 2, 2, 3, 4 confirmed.
- diagonal sector: position permutation trivial in **1024 of 1024** checks.
  Balanced sector: **512 of 512** base holonomies non-monomial.

### Is set-equality certification sound? YES — and no proper subgroup can pass.

The protocol asks for a proof or a hole. Here is the proof.

Let $G=\langle S\rangle\le\mathrm{Sym}(\Omega)$, let $O_1,\dots,O_k$ be its
orbits of size $>1$, and let $H=\prod_i \mathrm{Alt}(O_i)$.

1. Each $O_i$ is $G$-invariant *by definition of orbit*, so restriction gives
   homomorphisms $\rho_i:G\to\mathrm{Sym}(O_i)$ and $G\le\prod_i\mathrm{Sym}(O_i)$.
2. $\mathrm{sgn}\circ\rho_i : G\to\{\pm1\}$ is a **homomorphism**, so it is
   trivial on $G$ iff it is trivial on the generating set $S$. The unit checks
   exactly that. Hence $G\le H$.
3. $H$ is finite and $|G|=|H|$ is measured. A subgroup of a finite group with
   equal cardinality **is** that group.

The conclusion is an identity of finite sets, not an inference from an
invariant, so a proper subgroup passing is impossible *by construction*: any
proper subgroup has strictly smaller order and fails step 3. The only failure
modes are computational — a wrong order or a wrong orbit — and I closed both
by a route that computes no order at all. The certificate is **sound**, the
`target > 1` guard is conservative-correct, and $|O_i|=2$ contributing
$2!/2=1$ is right. **No hole.**

**But the LABEL is wrong at two stencils (MAJOR-7 below).** `certified` proves
$G=\prod_i\mathrm{Alt}(O_i)$ — "the full alternating group on **each of its
orbits**". At `S2-CORNER` and `S2-APART` that is $A_3\times A_3$ on a 6-point
support, a subgroup of $\mathrm{Alt}(6)$ of **index 40**. The paper's title and
the verdict tag `CLASS=ALTERNATING-ON-ITS-OWN-SUPPORT` assert the stronger,
false thing at 2 of the 6 local stencils. §3 carries the correct qualifier;
the headline does not.

### The flat control — rebuilt from R4's prose, and the 58 is *explained*

From the autocorrelation criterion alone I get **66 gauge classes** over the 9
declared axes (9 each on the six axes whose stencil $\{0,a,-a\}$ has three
points; 4 each on the three axes with $2a\equiv 0$, whose stencil has two).
Deduplicating **on the matrix** collapses this to exactly **58** — and the
mechanism is a single circulant, the identity $\delta_0$, which solves the
criterion on **all nine axes at once** ($66-8=58$). Then: **3364** ordered
pairs, **0** non-commuting, and every assembled plaquette holonomy the
identity (**0 of 144**), so the holonomy group is **trivial**. The control is
provably flat and independently reproduced, including the de-duplication step
the unit inherits without stating.

## 3. K3 — THE EXCLUSION THEOREM. The lemma is true; the headline exceeds it.

**The lemma is correct.** I verified the proof by hand: for links sharing at
most one site, the set $\{k : (U_2)_{ik}\neq0 \text{ and } (U_1)_{kj}\neq0\}$
has at most one element for every $(i,j)$; that same set indexes the surviving
terms on **both** sides of $B(U_2U_1)$ vs $B(U_2)B(U_1)$, so a one-term sum
matches a one-term sum. And I verified it *computationally at the stated
generality* — "for any coins whatever": over **61,504 independent-coin pairs**
at SHARE-ONE-SITE and **61,504** at DISJOINT, the defect is zero **every
time**. The theorem holds exactly as stated.

**The census reproduces.** Hadamard witness $[[1/2,-1/2],[-1/2,1/2]]$ exact.
Link grain: SAME-LINK `256/384/0/0`, SHARE-ONE-SITE `64/0/576/0`, DISJOINT
`640/0/0/0`; **0 of 1920** both; **576** curvature-only, **384** defect-only.
Two-excitation: **120** states, 18 rows, `neither 12 / defect-only 2 /
curvature-only 4 / both 0`. Plaquette grain cross-checks against the receipt
in all four relations, 384 both.

**The infinite-order certification is sound.** Finite order ⟹ diagonalisable
with root-of-unity eigenvalues ⟹ trace a sum of roots of unity ⟹ an algebraic
integer; $\mathbb{Z}[\zeta_8]$ is the full ring of integers of
$\mathbb{Q}(\zeta_8)$, so "denominator 1" is the right test. I recomputed
independently: **512 of 512** balanced traces are non-integral (they are
*rational* non-integers — e.g. $53/4$, $49/4$ — which makes the argument
airtight, since a rational algebraic integer is a rational integer), and
**64 of 64** antidiagonal traces are integral, as finite order requires. Route
verified.

**The over-claim (MAJOR-4).** The theorem covers links sharing **at most one**
site. The SAME-LINK relation — **640 of the 1920 rows** — shares *two* sites
and is **not covered**. Its `both` cell is empty only because the uniform
restriction puts the *same* coin on both legs, so the two operators are the
same operator and commute for free. The paper's bridging sentence,

> "Two link operators fail to commute only when their links share exactly one
> site."

is **false without the uniform-configuration scope**. My exhaustive scope test:

| SAME-LINK, coins allowed to differ | pairs | neither | defect only | curvature only | **both** |
|---|---|---|---|---|---|
| exhaustive $640\times640$ | 409,600 | 15,872 | 6,656 | 197,120 | **189,952** |

**46.4% of the uncovered relation carries both.** The same holds one dimension
up: in the declared $\Lambda^2$ sector, 2 of just 36 named-coin SAME-LINK pairs
carry both. So `MUTUALLY-EXCLUSIVE-BY-THEOREM` is a theorem on two of three
relations and a *declaration artifact* on the third. This also answers §10's
own successor question in the negative: the plaquette grain is **not** the
first support at which exclusivity fails — it already fails at support 2.

## 4. The CR-D comparison: NUMEROLOGICAL, not structural

Against the pinned CR-D artifact `602c9ac2ccc4`:

- **CR-D's own four-wing tower** realises `{trivial, A5, A11, A15}`, top
  $A_{15}$. Its supports are **Hamming weight classes** of the $2^4-1$ system
  labels (`11:weight≥2, 5:weight≥3, 15:all nonzero`), and its ceiling law is
  $(2^n-1)!/2\times n!$.
- **R5's** supports are lattice-geometric (3, 5, 6, 7, 8, 16) and its mechanism
  is "overlapping 3-cycles generate the alternating group on the union".

No shared support law, no shared generating mechanism, no shared ceiling. The
common content is that a permutation group generated by enough even elements
with overlapping supports is $A_n$ — which is the **generic** outcome, not a
signature. CR-D's own paper sets the discipline: it refuses to call the
two-wing agreement an instance of its theorem and reports it as "numerical".
R5 should meet that standard and does not — it says the comparison "is closer
than a family resemblance" and that "the alternating-family prior is
confirmed".

**The unit's own scramble control refutes the form claim (MAJOR-6).** Read off
`scramble_control`: the scrambles — deliberately unphysical assemblies —
return `A8, A8, A10, A10, A12` at **5 of the 12 local cells**, and $A_{16}$ at
**both** global cells. The full-alternating *form* therefore arises from
assemblies the unit built to be wrong. What separates at 12/12 is the
**(order, support) profile**, not the form. The paper's separation paragraph
and its CR-D paragraph sit in the same section and pull opposite ways.

**And the A₇ sentence misattributes (MAJOR-5).** Paper-18 §7: "$A_7$, which
CR-D's ladder tops out at". In `602c9ac2ccc4`, $A_7$ tops the **three-wing**
ladder `1 < A_4 < GL(3,2) < A_6 < A_7` that CR-D *inherits* — CR-D's stated
purpose is to take "the tower's first step **past** three wings", and its own
tower tops out at $A_{15}$. Worse, that three-wing ladder contains
$\mathrm{GL}(3,2)$ (order 168 on 7 points), which is **not** the full
alternating group on its support — so the same sentence's premise, that CR-D
reported the full alternating group "at every realised rung", is false for the
ladder it then quotes. The sentence draws universality from one object and its
$A_7$ from another, and the second falsifies the first.

## 5. The verdict block does not match the instrument (MAJOR-1 / MAJOR-2)

The paper introduces its verdict as "**quoted exactly as the instrument
emits it**". It is not. Two segments differ from `r5_gauge_output.txt`:

| | paper | instrument |
|---|---|---|
| declared gate | `FAMILY-COVARIANCE-512-OF-512-CHECKS` | `FAMILY-COVARIANCE-4096-OF-4096-CHECKS` |
| two-excitation | `EXCLUSIVITY-SURVIVES-0-OF-9-BOTH` | `EXCLUSIVITY-SURVIVES-0-OF-18-BOTH` |

Both prose sections are **right** (§4 "4096 of the 4096 checks", §5 "0 of 18",
receipt `family_covariance_checks: 4096`, `two_rows: 18`), so this is a
transcription fault confined to the single most load-bearing block in the
paper — and `512-OF-512` looks copied from the `INTERFERING-SECTOR` segment.

**Why nothing caught it.** No gate compares the paper's quoted verdict against
the emitted one. And the numeral-coverage gate **structurally cannot** see it:
`NUMERAL_RE = (?<![\w./-])(\d+…)(?![\w.-])` excludes any numeral adjacent to a
hyphen, so of the whole quoted verdict line the gate sees only
`['2','4','25','640','32','16','1','1']` — every numeral inside a hyphenated
segment (`576-OF-640`, `0-OF-52`, `512-OF-512`, `0-OF-9`, `0-OF-1920`,
`6-OF-6`, `12-OF-12`, …) is invisible. A broader sweep would not have helped
either: `512` and `9` both occur legitimately elsewhere in the receipt, so
*only* string equality catches this class of error.

## 6. Findings, ranked, with exact repairs

### MAJOR

1. **Paper's headline verdict ≠ emitted verdict.** Repair: replace the quoted
   block with the exact bytes of the `R5-NON-ABELIAN-<…>` line from
   `r5_gauge_output.txt` (`4096-OF-4096`, `0-OF-18`).
2. **The quoted verdict is ungated.** Repair: add one gate —
   `flat(verdict_string) in flat(paper_text)` — bound as a consumer of the
   verdict seal, with a declared mutant that perturbs one character of the
   emitted verdict and must die there. This is the gate whose absence produced
   MAJOR-1, and it is two lines.
3. **The "ladder" asserts false relations.** `A3 < A5 < A3×A3 < A3×A3 < A7 <
   A8` has orders 3, 60, 9, 9, 2520, 20160. $A_5\not<A_3\times A_3$ (60 > 9),
   and $A_3\times A_3 < A_3\times A_3$ is not proper. The corpus's own
   convention is genuine containment — CR-D's `1 < A_4 < GL(3,2) < A_6 < A_7`
   *is* an ascending chain that embeds. Repair: change the separator in
   `counts/local_ladder` and everywhere it renders from `<` to `;` or `|`, and
   call it the *stencil profile*, not a ladder; or state and prove the chain
   actually intended. This is a verdict-string change.
4. **`MUTUALLY-EXCLUSIVE-BY-THEOREM` exceeds its theorem.** Repair: (a) scope
   the bridging sentence — "*Under the declared uniform-configuration
   restriction*, two link operators fail to commute only when their links
   share exactly one site"; (b) segment the verdict, e.g.
   `LINK-GRAIN=MUTUALLY-EXCLUSIVE-0-OF-1920-BOTH(BY-THEOREM-AT-SHARE-ONE-SITE-AND-DISJOINT;BY-THE-UNIFORM-RESTRICTION-AT-SAME-LINK)`;
   (c) enter the measured counterexample — 189,952 of 409,600 SAME-LINK pairs
   carry both once coins may differ — as the scope's own witness.
5. **CR-D $A_7$ misattribution.** Repair: delete "which CR-D's ladder tops out
   at" or replace with "which tops the three-wing ladder CR-D inherits and
   passes"; and drop or qualify "at every realised rung", which the same
   three-wing ladder falsifies via $\mathrm{GL}(3,2)$.
6. **The alternating form is not discriminating, by the unit's own control.**
   Repair: replace "The alternating-family prior is confirmed on the gauge
   rung" with the measured statement — the *form* recurs under both scrambles
   (5 of 12 local cells and both global cells are full alternating groups), so
   what separates is the (order, support) profile; report the CR-D agreement
   as a **form coincidence with no shared mechanism**, on CR-D's own
   "numerical, not an instance of the theorem" precedent.
7. **The title over-states at 2 of 6 stencils.** $A_3\times A_3$ is not the
   full alternating group on its 6-point support. Repair: "the full
   alternating group on **each of its orbits**" in the title, the `CLASS` tag
   and the G1 output line.

### MINOR

8. **Eight of the 25 alphabet elements are inert.** No coin uses any
   modulus-$\tfrac12$ element: a row of squared moduli from
   $\{0,\tfrac14,\tfrac12,1\}$ summing to 1 excludes $\tfrac14$ outright, so
   the 640 coins are built from **17** of the 25. The derivation is still
   FORCED with fibre 1, but the family is insensitive to a third of its
   declared input. Repair: one sentence in §2 stating it — it strengthens the
   forcing rather than weakening it.
9. **"0 of 18" is not exhaustive.** The 18 rows are **6 named coins × 3
   relations**, while the neighbouring 1920 rows *are* exhaustive over 640
   coins. Repair: say "at the six declared named coins" in §5 and in §11's
   third scope note.
10. **The proof's "five admissible $(i,j)$ shapes" undercounts.** There are
    more nonzero shapes than five (all diagonal entries outside $\{a,b,c\}$,
    plus $(a,a),(a,b),(b,a),(b,b),(b,c),(c,a),(c,b),(c,c)$). The conclusion is
    unaffected — every one of them has at most one surviving $k$. Repair:
    "every admissible $(i,j)$ shape".
11. **§10's exclusivity question is already answered.** "Is the
    plaquette-grain co-occurrence simply the first support at which it fails?"
    — no: it fails at support 2 as soon as the coins may differ. Repair: fold
    the measurement in and re-pose the successor as the *non-uniform* census.

## 7. What I could not fault

The receipt contains **no false number**. Every group-theoretic claim survived
a certification route that shares nothing with the unit's — including
$A_{16}$, certified with no order computed. The flat control is genuinely
flat and its 58 is reconstructible from the parent's prose alone. The
single-path lemma is a true theorem and holds at exactly the generality it
claims. The infinite-order route is valid and its 512/512 is right. The
declared-gate re-derivation (per-generator NONE at 0/52; family covariance at
4096/4096) is the honest reading, and both readings are in the verdict — that
segmentation is the unit's best work. Byte-identity holds off-tree and
git-less.

The unit's defects are **all in the presentation layer**: a mistyped verdict,
a separator that asserts containment, a theorem quoted past its premise, and a
comparison to CR-D that the unit's own scramble table undercuts. None of them
requires re-running the physics. That is why this is AWF and not R.

*Every reading above is a reviewer's reading until adjudication.*

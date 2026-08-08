# LCB — HOSTILE REVIEW R2 (EFFECTUS / CATEGORICAL LENS)

**Reviewer:** R2, structural/conceptual lens. **Date:** 2026-08-08.
**Protocol:** `v13/note-lcb-hostile-protocol.md` (FROZEN, K1–K5 binding).
**Object under review (frozen):**

| artifact | sha256-12 dispatched | sha256-12 measured | verified |
|---|---|---|---|
| `v13/paper-lcb-livecell.md` | `9b081a1e72af` | `9b081a1e72af` | ✅ |
| `v13/code/lcb_livecell_exact.py` | `57d3072b1031` | `57d3072b1031` | ✅ |
| `v13/code/lcb_livecell_output.txt` | `50dad82e0637` | `50dad82e0637` | ✅ |
| `v13/code/lcb_livecell_receipt.json` | `2ffe123e16cf` | `2ffe123e16cf` | ✅ |

Re-verified unchanged at the end of the review. No repository file was mutated;
no git operation was performed; the delivery was rerun in
`--falsification-selftest` mode, which does not write artifacts.

**Independent recomputations performed: 55**, in
`…/scratchpad/` (`r2_recompute_A.py`, `_B.py`, `_C.py`, `_D.py`,
`r2_selftest_probe.py`). Nothing was imported from the delivery module: the
permutation kernel, Σ, the defect law, the completion family, HA's readout, the
census (both routes), the held-out protocol, the controls and the Open-1 table
were all rebuilt from the declared laws.

**Reproduction.** `/opt/homebrew/bin/python3.13 v13/code/lcb_livecell_exact.py
--falsification-selftest`: exit 0, 30 anchors, 34 gates, 55 mutants, 0
survivors, `never_falsified` empty. Stdout **byte-identical** to the frozen
`lcb_livecell_output.txt` (`diff` clean).

---

## Headline

**Every number in this paper reproduced.** 55 of 55 independent recomputations
agree with the delivery — the census (0/48/0/48 by two routes of my own), the
100-of-125 S1c violation count, the 6,336 / 6,144 / 192 held-out split, the
124/124 predictions, the 99/99 teeth, BREAK-HOM's 0/125 and 6,000/15,625, the
224 / 32 / 4 / 0 grid, the {5:48, 7:96} anti-invariant counts, the 41,665
enumeration, the four encoding cells' determinants, spectra and mod-5 matrices,
the 40/40 squaring identity (and 240/240 at the full sweep), and the SYNTH
control's 192 pairs / 48 maps. **I found no false computed number anywhere.**
Both verdicts — `LCB-BRIDGE-EMPTY-AT-STRENGTHENED-STANDARD` and
`LCB-PRIME-DECLARED` — are **correct**.

What I did find is that the paper **understates and mis-locates its own
result**, and that the parts of the verdict a reader will lean on hardest are
carried by clauses and classifications that are not measured to the standard the
rest of the unit meets.

Three things, in order of weight.

1. **The obstruction is arena-free, and the paper says it is arena-relative.**
   Two of BRG's *registered* clauses — S1's square and S3's injectivity horn —
   are **jointly unsatisfiable at every arena, every prime, every $d$, both
   directions and both identifications**, by a two-line argument the unit's own
   data supports (F-1). This answers K4's central question decisively in the
   paper's favour: **no verdict depends on S1c or S1d, or on S1b.** It also
   makes §16 Open 1's "the first place where all of S1, S2 and S3 could in
   principle be met at once" **false**, and closes X07 in the negative.
2. **S1b is an undeclared addition, and at the registered direction it is the
   only thing producing the 0.** With S1 read as BRG registered it — a commuting
   square, no homomorphism clause — the census at the registered direction is
   **not empty**: it has $189^{25} \approx 8.16\times10^{56}$ solutions, which I
   enumerated structurally (F-2). Deviation 2 declares S1c and S1d as this
   unit's additions and says nothing about S1b.
3. **The Open-1 column that carries the verdict is typed, not measured** (F-4),
   and the one candidate whose value gives §12 its most quotable sentence — P8,
   "the intertwining determines $p = 3$" — is **mis-classified by the code's own
   criterion** (F-3): its answer is not invariant under the unit's own declared
   direction sweep ({3} registered, all 17 primes below 60 reversed).

None of this overturns anything. All of it is repairable in the paper plus one
modest code addition. Details, evidence and repairs below.

---

## F-1 — MAJOR. The obstruction is arena-free; the paper locates it in the arena, and one Open is false as a consequence

**Claims attacked.** §6: "*its failure is forced at this carrier* … *what
forbids it here is the nine-label arena*"; §13: "*because the arena is too small
to hold the record space at all*"; X07: "*Whether any injective candidate there
satisfies the square is not tested*"; §16 Open 1: "*it is the first place where
all of S1, S2 and S3 could in principle be met at once*".

**What I measured.** The transport side's encoding is
$\delta(x) = \sigma(x)^{-1}x$. Therefore

$$\delta(x) = x \iff \sigma(x)^{-1}x = x \iff \sigma(x) = e \iff x = e,$$

because $\sigma$ (conjugation by $\Sigma$) is injective. **$\delta$ has exactly
one fixed point, at every arena, with no hypothesis on the arena at all.**
Measured: 1 fixed point at the 4-label arena ($|G_C| = 6$), 1 at the 9-label
arena ($|G_C| = 40{,}320$), and 1 inside the very order-125 subgroup G15 builds
at sixteen labels.

The deformation side's re-encoding $E$ has a non-trivial fixed space. Measured
$|\mathrm{fix}(E)|$ at all four declared cells and $p\in\{3,5,7,11,13,23\}$:
$p^2$ at both **natural** cells, $p$ at both **index** cells — never 1. (For the
natural identification this is provable at every $d$: $E-I$ has rank
$d(d-1)/2$, so $\dim\ker(E-I) = d$.)

The commuting square forces $\alpha(\mathrm{fix}\,E) \subseteq
\mathrm{fix}\,\delta = \{e\}$. So **every** candidate satisfying S1a collapses at
least $p \ge 3$ distinct record cells onto the identity, and is therefore not
injective. Hence:

> **S1a (BRG's registered square) ∧ S3 (BRG's registered injectivity horn) are
> jointly unsatisfiable — at every completion arena, every odd prime, every $d$,
> both directions and both identifications.** No S1b, no S1c, no S1d, no
> $p$-part bound, no cardinality argument.

I verified the same conclusion a second, independent way under the homomorphism
clause. With S1b in force the square reads $\alpha\circ E = (I-S)\circ\alpha$
with $S = \sigma|_{\mathrm{image}}$ a linear map of finite order; injectivity
makes $\alpha$ an isomorphism onto its image, so $E \sim I-S$. But $1$ is an
eigenvalue of $E$ at every cell and every prime tested (measured), and $1$ is
never an eigenvalue of $I-S$ for invertible $S$ ($(I-S)v = v \iff Sv = 0$).
Exhaustively over $\mathbb F_5$: all **1,552** matrices with $S^2 = I$ give
exactly **4** characteristic polynomials for $I-S$, and **none** matches any of
the four $E$ cells. (The invertible case is $S = -I$, i.e. $E = 2\cdot\mathrm{Id}$
— which HA's readout never is, since it is not scalar.)

**Why this matters, and why it is not a nitpick.**

- **It settles K4.** The paper's answer to "does any verdict depend on the added
  clauses alone" is "read §5's table". A reader who does that finds 48 surviving
  candidates in two of four cells at S1a+S1b+S1d, killed only by S1c — the added
  clause. They must then find §6 separately and combine it. With F-1 the answer
  is one sentence: **the verdict holds at BRG's registered clauses alone.** The
  paper is entitled to that sentence and does not claim it.
- **It makes the verdict's NAME true.** See F-9.
- **§16 Open 1 is false.** At sixteen labels $\mathrm{fix}(\delta)$ is still
  $\{e\}$ (measured inside G15's own witness subgroup) and $\mathrm{fix}(E)$
  still has $p^2$ elements, so S1 ∧ S3 fails there too. Sixteen labels is not
  "the first place where all of S1, S2 and S3 could in principle be met at
  once"; there is no such place for HA's readout.
- **X07 closes in the negative.** "Whether any injective candidate there
  satisfies the square" — none does, and the reason needs no computation at
  sixteen labels.

**Repair.** (i) Add the two-line lemma (`fix δ = {e}`; `fix E ≠ {0}`) as its own
numbered result, gated by a measurement of both fixed-point sets — both are
cheap and both are already computed in adjacent code. (ii) Restate §6's "what
forbids it here is the nine-label arena" as: the *cardinality* obstruction is
arena-relative, the *square* obstruction is not. (iii) Withdraw Open 1's
"could in principle be met at once" and replace it with the sixteen-label
question that remains open (S1 ∧ S2 without S3). (iv) Convert X07 from an open
to a measured negative.

---

## F-2 — MAJOR (K4). S1b is a third undeclared addition, and it is what produces the 0 at the registered direction

**Claim attacked.** Deviation 2: "*BRG's S1 names the commuting square and the
two encodings; it does not name the involution clause or the base-point
clause*" — and §4.2's box, "**S1a+S1b at the REGISTERED direction: 0
candidates**".

**The categorical point.** BRG's S1 registers *a commuting square at the
encoding layer*. A square needs a category. It cannot be **Grp** or any category
of $\mathbb F_p$-modules, because the horizontal arrow $\delta$ is **not** a
homomorphism — the paper's own §2.4 states the twisted-cocycle identity
$\delta(QQ') = \sigma(Q')^{-1}\delta(Q)\,Q'$. The only category in which BRG's
square literally lives is **Set**. So S1b is a genuine additional structural
demand on the vertical arrow, of exactly the same logical type as S1c and S1d —
and one the square itself cannot motivate, because the edge it would have to be
compatible with is not a morphism of the structure S1b imposes.

**What I measured.** I posed the set-level census (S1a alone) at the registered
direction and enumerated it exactly. $E$ acts on $V = \mathbb F_5^3$ with orbit
spectrum $\{1{:}25,\ 4{:}25\}$; $\delta$ has 1 point of period 1 and 189 of
period dividing 4; the square determines $\alpha$ on each $E$-orbit from its
value at a representative subject to $\delta^{L} = \mathrm{id}$. Census size:

$$1^{25}\cdot 189^{25} \;=\; 815{,}727{,}501{,}386{,}186{,}588{,}190{,}430{,}395{,}382{,}342{,}267{,}781{,}393{,}000{,}859{,}545{,}374{,}749 \;\approx\; 8.16\times10^{56}.$$

**Not empty.** The constant-identity map alone is a witness (and it satisfies
S1c too). So the boxed "0 candidates at the REGISTERED direction" is produced
**entirely by S1b**, a clause BRG did not register and the paper does not
declare as an addition.

Two consequences the paper should carry:

- **The negative control's teeth are supplied by the undeclared clause.**
  BREAK-HOM is "rejected by S1b alone, with the rejecting clause named" (§10,
  G24) — I reproduce S1a 0/125, S1b 6,000/15,625 exactly. The unit's declared
  negative-with-teeth is therefore defeated by a clause outside BRG's registry.
- **The stated justification for S1b does not hold.** One might defend S1b as
  necessary to make the census finite. It is not: as above, the set-level census
  is finite, enumerable, and I enumerated it in seconds.

**What survives the attack.** S1b is *reasonable* — a candidate morphism of
encodings that ignores the record datum's additive structure carries almost no
information, and S2's "determined" clause has no content without it. I am not
asking for it to be dropped. I am asking for it to be **declared**, as S1c and
S1d are, and for its load to be visible.

**Repair.** Add S1b to deviation 2 as this unit's third addition, with the
categorical reason (δ is a twisted cocycle, so the square is a Set-level
statement). Add one row to §5's clause table giving the **set-level** count at
each cell, so the clause-by-clause table genuinely lets a reader who rejects an
addition recompute the verdict. Then state F-1's lemma so the reader who rejects
*all three* additions still lands on EMPTY.

---

## F-3 — MODERATE (K3). P8 is mis-classified as declaration-free by the unit's own criterion; the sentence it carries is untagged

**Claim attacked.** §12, P8 row: `declaration-free: yes`, `unique: yes — and the
prime is 3`; and the summary sentence, "*the one declaration-free candidate that
does determine a unique prime — the intertwining condition itself — determines
$p = 3$*".

**The criterion, quoted from the instrument.** `declaration_free`'s own
docstring: "*it must take no declared prime **and no declared choice of this
unit** among its inputs*." The **direction** is a declared choice of this unit —
§2.1 lists "the DIRECTION sweep" as an arena action, §2.4 registers `counts→q`,
and deviation 1 says in terms that "the identification and the direction are
declarations". P8's implementation restricts to it explicitly
(`if dr != "counts->q": continue`).

**What I measured.** P8's admitted set under each declared re-declaration:

| re-declaration | P8's admitted primes | invariant? |
|---|---|---|
| $p := 7$, rule $\mathrm{ord}(D) := 7$ | $\{3\}$ vs $\{3\}$ | **yes** |
| direction $:=$ reversed | $\{3\}$ vs **all 17 primes below 60** | **NO** |

So P8 is invariant under the prime declaration and **not** invariant under the
direction declaration. By the instrument's own criterion it takes a declared
choice of this unit among its inputs, and should read `declaration-free: no` —
as should P9 (= P7 ∧ P8, which inherits it).

**Effect on the verdict: none.** P8 and P9 have role `NO-ADMISSIBLE-PRIME`, so
they are excluded from `unique_forced` and from P12's intersection either way.
`LCB-PRIME-DECLARED` stands, and P12 stays $\{5,7\}$. I checked both.

**Effect on §12's text: real.** "Three declaration-free candidates admit no
admissible prime whatever" becomes **one** (P11). And the headline sentence —
the one that carries the paper's most quotable framing, *the square wants
$p=3$* — must be direction-tagged. The **receipt** does tag it ("*solvable at
exactly one prime **in the registered direction***"); the paper's §12 table row
and §12 summary do not. That is precisely the failure the RUNBOOK catalogue
records at #40 F1/F2: **scope tags at the claim, not just the receipt.**

**On the framing itself (K-framing).** Tagged, "the square wants $p = 3$" is a
*measured* statement of real content, not poetry, and I verified its mechanism
independently: $\delta$ acts as squaring on the anti-invariant locus (40/40 at
the declared cells, 240/240 at the full sweep), the sign is forced by
$c^2 \equiv 1$ (I re-derived this, and confirmed the $c=+1$ branch is empty:
0 Σ-invariant order-5 elements against 48 anti-invariant), so the square reads
$\lambda\circ E = 2\lambda$, and $2 \in \mathrm{spec}(E) \iff 4 \equiv 1
\pmod p \iff p = 3$ — swept to 60, exactly $\{3\}$. The honest one-line
statement is: *the transport side doubles, the deformation side halves, and they
agree only where $4 = 1$*. That is strong, and it is a two-wing, rank-1-image,
registered-direction statement. It should be said with those three tags. Note
also that F-1 relegates it: under S3 it is not the binding constraint at any
prime.

**Repair.** Reclassify P8 and P9 (or, better, adopt F-4's measurement, which
reclassifies them automatically); tag the P8 row and the §12 summary sentence
with the registered direction; correct "three" to "one".

---

## F-4 — MODERATE (K3). The declaration-free column is typed, not measured — and one typed boolean carries the Open-1 verdict

**Evidence.** `declaration_free(pid, computed)` returns its second argument
unchanged; the second argument is a per-candidate literal in the twelve `add(…)`
calls (P1 `False`, P2 `False`, P3 `False`, P4–P12 `True`). G29's predicate is

```
len(open1) == 12  and  any(not free)  and  any(free)
```

— it tests the table's *shape*, not any classification. The only mutant aimed at
it, `open1-lax`, sets **all twelve** to `True`; it dies on `any(not free)`. This
is the wholesale-replacement failure RUNBOOK §14 names in terms: *"A
wholesale-replacement mutant does not test that the RIGHT invariant is
computed."* **A single-entry mis-classification is invisible to G29** — as F-3
demonstrates, since P8 is mis-classified and every gate passes.

**Why it is load-bearing.** `unique_forced` requires
`unique ∧ declaration_free ∧ role == NARROWING ∧ admits ⊆ ADMISS`. Exactly one
candidate satisfies all but the second: **P1** (admits $\{5\}$, unique `True`,
role `NARROWING`). Typing P1's boolean `True` flips `derive_prime_verdict` to
`LCB-PRIME-DERIVED`. So the Open-1 verdict string — correctly derived in-gate
per §13's #234 addendum — bottoms out in **one hand-typed boolean**. The
addendum's point is that a verdict must not be "a typo away from fiction"; here
the derivation is sound but its input is typed.

**The repair is available and cheap, and I ran it.** Declaration-freeness *can*
be measured, as invariance of the candidate's admitted set under the unit's own
declared arena action (RUNBOOK §14/§15 — exactly the discipline the unit already
applies to $\dim\ker(E^{\mathsf T}-2I)$):

| candidate | $p:=5$ | $p:=7$, rule $\mathrm{ord}(D):=7$ | invariant | measured verdict |
|---|---|---|---|---|
| P1 | $\{5\}$ | $\{7\}$ | **no** | declaration-carrying ✔ (agrees with the typed value) |
| P3 | $\{2,5\}$ | $\{2,7\}$ | **no** | declaration-carrying ✔ |
| P4 | $\{2,3,5,7\}$ | $\{2,3,5,7\}$ | yes | declaration-free ✔ |
| P5 | $\{2,3,5,7\}$ | $\{2,3,5,7\}$ | yes | declaration-free ✔ |
| P8 | $\{3\}$ | $\{3\}$ | yes (prime) / **no** (direction) | **declaration-carrying ✘ — disagrees** |

(The counterfactual base is constructible: the lex-first completion with
$\mathrm{ord}(D) = 7$ is $[0,1,2,4,5,3,7,6,8]$, and the ord-7 class is
non-empty — 9,216 members.)

This measurement is falsifiable one entry at a time, kills a targeted mutant
(flip any single classification), and reproduces the correct verdict for the
right reason.

**Repair.** Replace the typed column by the invariance measurement; add a
targeted mutant that flips exactly one entry; re-state G29's predicate over the
measured column.

---

## F-5 — MODERATE (RUNBOOK §14 compliance). Both symmetry self-tests are analytically forced

**Claims attacked.** §11: "*the defect map is measured equivariant at all 40,320
cells inside the relabelled arena, and the anti-invariant element count
recounted there is 48*" (G25); "*the census's own decision quantity … recomputed
inside the new basis is unchanged*" (G26).

**Evidence.** G25 transports Σ along with the completions
(`SIGr = conj_by(pi, SIG)`), so the identity it checks,

$$\delta_{\pi\Sigma\pi^{-1}}(\pi q\pi^{-1}) \;=\; \pi\,\delta_\Sigma(q)\,\pi^{-1},$$

is true for **every** $\pi$ and every $q$ — conjugation is an automorphism. I
ran it at the declared $\pi$ and at six random relabellings:

| $\pi$ | commutes with Σ | equivariance | anti count |
|---|---|---|---|
| declared `[0,2,3,4,1,5,6,7,8]` | **no** | 40,320/40,320 | 48 |
| 6 random $\pi$ | no (6/6) | 40,320/40,320 (6/6) | 48 (6/6) |

Both measured quantities are constant across the whole relabelling group. The
gate's only teeth are `pi != identity` and `pmoved(pi) > 0` — properties of the
declared $\pi$, not of the transported quantity — and that is exactly what
`relabel-lax` (π := identity) dies on. RUNBOOK §14 addendum #208:
*"Analytically-forced clauses (true by algebra for every input) are disclosures,
not must-pass gates."* Addendum #219: *"a gate clause that compares an object
against a copy of itself routed through the very component under test verifies
nothing."* G26 is the same shape: $\ker((BEB^{-1})^{\mathsf T}-2I)$ has the
dimension of $\ker(E^{\mathsf T}-2I)$ for every invertible $B$, because
similarity preserves eigenspace dimension.

**The informative version exists and has real teeth.** Σ is declared *structure*
(the label exchange), not a coordinate. Hold Σ fixed and relabel only the
completions: equivariance then holds only for $\pi$ in the centraliser of Σ.
Measured, same seven $\pi$: **7 to 36 of 40,320** — and the declared
$\pi = [0,2,3,4,1,5,6,7,8]$ **does not commute with Σ**, so it would fail. That
is a self-test that reads its arena.

**No number moves.** The census, the verdicts and the qualifiers are untouched.
This is a gate-quality finding, and it costs the unit two of its 34 must-pass
gates.

**Repair.** Either reclassify G25/G26 as disclosures (and re-check the
`never_falsified` accounting for the two gates thereby freed), or run the
Σ-fixed / τ-fixed versions and report the centraliser condition as the measured
content.

---

## F-6 — MINOR (K3, §15). The $\{5,7\}$ narrowing is a nine-label-arena artifact, presented untagged

$\{5,7\}$ is the intersection of P4, P5 and P10, and all three read off the
**nine-label** completion group: $|G_C| = 8! = 2^7\cdot3^2\cdot5\cdot7$ has no
element of order 11 or 13. At the sixteen-label arena — which the unit itself
nominates as the successor and whose $p$-part it measures in G15 — $15!$ has
11-part and 13-part $1$, so P5 (and with it P4, P10) admits $\{5,7,11,13\}$ and
the "tightest declaration-free narrowing" **widens**. §15's rule is that
arena-artifacts may serve as instruments but never as conclusions; the boxed
narrowing and the verdict qualifier row carry no arena tag.

**Verdict-safe, and in the safe direction:** a wider narrowing is a weaker
determination, so `LCB-PRIME-DECLARED` only strengthens. I also hunted for a
*missed* candidate that would narrow to $\{5\}$ declaration-freely — the orbit
count 125, the class size 4,608, the strata count 7, the record count 9, the
link count 3, $\rho$'s denominator, the determinant — and found none. The
candidate list is a fair frame.

**Repair.** One scope tag: "$\{5,7\}$ **at the nine-label completion arena**".

---

## F-7 — MINOR (K3). P11's admitted set is typed, and its note states a false universal

`add("P11", …, [], True, …)` types the empty list where the computed value is
$\{2\}$: the 2-part of $8! = 2^7 \ge 2^3$, so an injective candidate is
*cardinality*-admissible at $p = 2$ (an elementary abelian $2^3$ does sit in
$S_8$). P11's `unique` column would then read `True`, not `False`. The
admissible part is $\varnothing$ either way (2 is inadmissible), so **no verdict
moves** — but this is a typed count where a computed one belongs (catalogue
#24), in the one section whose whole point is that quantities are measured
rather than argued.

Its note, which ships in the receipt, reads: "*the $p$-part of the completion
group's order is $p^1$ at every prime*". That is **false** at $p=2$ ($2^7$) and
$p=3$ ($3^2$). The true statement is "at every **admissible** prime".

**Repair.** Compute the set; fix the note.

---

## F-8 — MINOR (K3). One word in the standing-interpretation sentence adjudicates

The sentence is otherwise exemplary: it states the declaration-relative reading,
attributes no consequence, and does not choose a horn of BRG's dichotomy —
compliant with the pin's "*stated as the standing interpretation … NOT
adjudicated*". The leak is one modal word:

> "With $p$ **irreducibly** a declaration at this pairing …"

*Irreducibly* asserts exhaustion. What was measured is that **no declared
candidate structure** derives $p$ — and §16 Open 4 says so explicitly:
"*nothing measured here forbids a corpus-internal fixing of $p$ from some
structure this unit did not declare. The candidate list is the frame, not the
exhaustion.*" §12 and §16 contradict each other on this word.

**Repair.** "With $p$ not derived by any declared candidate structure at this
pairing …". The rest of the sentence stands as written.

---

## F-9 — MINOR (K4, naming). `EMPTY-AT-STRENGTHENED-STANDARD` is honest only once F-1 is stated

BRG's §2.6 is *the* "strengthened standard" in this arc's vocabulary, so the
verdict name reads as emptiness against **BRG's registered** S1–S6. As
delivered, two of the four encoding cells are emptied only by S1c (an admitted
addition) and two only by S1b (an unadmitted one, F-2). On that reading the name
over-reaches, and the pre-registered alternative — renaming to something like
`EMPTY-AT-THE-EXTENDED-STANDARD` — would be the conservative fix.

I recommend **against** renaming, because F-1 makes the name true: at BRG's
registered clauses alone (S1a ∧ S3) the census is empty at every cell. The
correct repair is therefore to *earn* the name rather than weaken it — one
sentence in §13, backed by F-1's lemma. Absent F-1, the name should change.

---

## F-10 — THE SUCCESSOR QUESTION (asked for explicitly). What the three-wing version of this test would need

TB3's three wings are not a bigger version of this arena; they change three of
the four things this test is made of. Measured requirements, honestly:

**(a) The transport arena shrinks, and the sub-object obstruction survives
untouched.** TB3's completions are permutations of **eight** system-triple
labels fixing label 0, so $G_C \cong S_7$, $|G_C| = 5{,}040 = 2^4\cdot3^2\cdot
5\cdot7$ — $p$-parts $5^1$ and $7^1$, exactly as at nine labels. The cardinality
obstruction reproduces verbatim, and **F-1 applies unchanged** ($\mathrm{fix}
\,\delta = \{e\}$ is arena-free). A three-wing run would re-derive EMPTY without
learning anything new, unless the arena is grown: injectivity at $d = 2$ needs
$p^3 \mid |G_C|$, i.e. $\ge 3p+1$ labels (16 at $p=5$, 22 at $p=7$); at $d = 3$,
$\ge 6p+1$ (31 at $p=5$).

**(b) The parity clause has no three-wing analogue as stated — it becomes a
representation condition.** At two wings the symmetry group is $\mathbb Z/2$,
whose only non-trivial character is the sign; "equivariant vs anti-equivariant"
exhausts the possibilities, and that dichotomy is the whole content of the
CHART-PARITY obstruction. At three wings the symmetry is $S_3$, which also has a
2-dimensional standard representation. S1c must be restated as *"$\alpha$
intertwines the $S_3$-action on the record datum space with the wing action on
the image"* — an $\mathbb F_p[S_3]$-module condition, not a sign. There is no
"opposite signs" statement to make.

**(c) The spectral obstruction does NOT transport — and it is satisfiable at
$p=7$.** For a wing symmetry $g$ of order 3, $\delta_g|_A = I - S$ with
$S^3 = I$, so the demanded eigenvalues are $1-\omega$ for $\omega^3 = 1$,
$\omega \ne 1$, instead of $2$. Measured:

| $p$ | cube roots of 1 | demanded $1-\omega$ | HA's $1/2 \bmod p$ | collision |
|---|---|---|---|---|
| 5 | $\{1\}$ | — | 3 | no |
| **7** | $\{1,2,4\}$ | $\{4,6\}$ | **4** | **YES** |
| 13 | $\{1,3,9\}$ | $\{5,11\}$ | 7 | no |
| 31 | $\{1,5,25\}$ | $\{7,27\}$ | 16 | no |

So at $p = 7$ with an order-3 wing symmetry, the registered-direction spectral
condition **is** solvable — the two-wing "only at $p=3$" result is a
$\mathbb Z/2$ fact and dies at three wings. This is the single most interesting
thing a successor would find, and it is one line of arithmetic away from the
present unit. (S3 still closes it, by F-1; but the *spectral* wall genuinely
moves.)

**(d) The deformation side must be rebuilt at $d = 3$, and its spectrum
changes.** Matching an $S_3$ chart symmetry requires HA's general-$d$ extension
at $d = 3$ (HA §9: 27 sites, 6 links, records like `G3-FLAT` $(1,1,1,2,2,2)$).
Measured: the readout becomes $6\times6$ with $\det = 8 = 2^3$ and spectrum
$\{1,1,1,2,2,2\}$ in the $q\to$counts direction ($\{1^d, 2^{d(d-1)/2}\}$ in
general; $d=4$: $10\times10$, $\det = 64$). So $|V| = p^6$, and the registered
direction still demands $4 \equiv 1$: **the paper's Open 3 ("whether a different
admissible readout … puts 2 in the spectrum at an admissible prime") is answered
NO for the whole $d$-family**, since the $q\to$counts spectrum is always
$\{1,2\}$ and the counts$\to q$ spectrum always $\{1, 1/2\}$. Open 3 should be
narrowed to genuinely different link sets, not different $d$.

**(e) And the defect law itself is not yet known at $S_3$.** TB3 §4 (A2)
measured that the two readings of $D = Pu^{-1}Pu$ come apart at three wings, and
TB3 §3 measured that the dihedral law $|\mathrm{Hol}| = 2\,\mathrm{ord}$ fails
at 4 of 4 targets (1008 vs 4, 72 vs 6, 15120 vs 12). **The three-wing successor
cannot pose S1 until the three-wing $\delta$ is decided**, because everything
above assumes the twisted-cocycle form $\delta_g(Q) = \sigma_g(Q)^{-1}Q$. That
is the first requirement, and it is TB3's business, not this pin's.

**Summary of the successor pin's honest requirements:** decide $\delta$ at $S_3$
(TB3 A2) → rebuild HA at $d=3$ → grow the transport arena to $\ge 6p+1$ labels
if S3 is to be more than forced → restate S1c as a module condition → expect the
SPECTRAL form to vanish (satisfiable at $p=7$), the PARITY form to be replaced,
and the SUB-OBJECT form (F-1) to survive intact.

---

## Kill-shot ledger

| | disposition |
|---|---|
| **K1 SPECTRAL** | **Verified.** Squaring-forcing re-derived independently ($c^2\equiv1$ from $\Sigma^2=e$; $c=+1$ branch measured empty — 0 Σ-invariant order-5 elements vs 48 anti-invariant; hence $\lambda\circ E = 2\lambda$). $\mathrm{spec}(E)$ recomputed at all four cells over $\mathbb Q$ and $\mathbb F_p$. $p$-sweep to 60: registered direction $\{3\}$, reversed direction all 17 primes. The forcing is **not** an artifact of one cell — it is uniform across both counts$\to q$ cells. Declaration-relativity of S1c in the index cells is honestly carried in deviation 1 (I confirmed the slot permutations $(1,0,2)$ vs $(2,1,0)$ exactly). Obstruction survives all four readings. **Sub-findings: F-3** (the $p=3$ sentence needs its direction tag). |
| **K2 PARITY / SUB-OBJECT** | **Verified.** 2-eigencovector $(1,1,1)$ measured chart-symmetric, not antisymmetric, in both reversed cells; 100-of-125 violation count reproduced exactly and explained ($\lambda(r)\ne0$ on 100 of 125). 16-label positive control reproduced (witness subgroup of order 125). **Are the three forms independent? Partly not, and better than claimed:** SPECTRAL and CHART-PARITY are the same fact read at two directions (they never both bind at one cell); SUB-OBJECT is genuinely independent — and by **F-1** it is *strictly stronger than both* and subsumes them. The paper's "measured in two forms" is right; its ranking of the three is wrong. |
| **K3 PRIME-DECLARED** | **Verdict correct; two mis-classifications and one typed column.** P1–P12 all recomputed. $\{5,7\}$ narrowing verified (and shown arena-relative, F-6). Intertwining-picks-$p=3$ verified (and shown direction-relative, F-3). **Mis-classified: P8, P9** (free → carrying, by the code's own criterion). **Typed: the whole free column** (F-4) and P11's set (F-7). Standing-interpretation sentence: states rather than decides, **except** for "irreducibly" (F-8). |
| **K4 S1c/S1d LEGITIMACY** | **Answered decisively in the paper's favour, but not by the paper.** Necessity: neither S1c nor S1d is needed to *pose* S1 — nor, it turns out, is S1b (F-2). Smuggling: S1d is the **weak** base-point form (order + fixed count, not $\delta(\alpha(r_0)) = D$), passes 48/48, and rejects nothing — it smuggles no strength into the census; its "forces $\mathrm{ord}(D)=p$" corollary is a genuine theorem *given* the clause, and the clause is a choice, honestly labelled. S1c **is** the sole killer in 2 of 4 cells. Does any verdict depend on the additions alone? **No — by F-1, S1a ∧ S3 (both registered) empty every cell.** Does the clause table let a reader recompute? **Only if they combine §5 and §6, and only if they accept S1b**; F-2's set-level row and F-1's lemma would make it genuinely self-contained. Naming: **F-9**. |
| **K5 INSTRUMENT** (lower depth) | 30 anchors, 34 gates, 55 mutants, 0 survivors, `never_falsified` empty — all reproduced; delivery run byte-identical. 41,665 enumeration reproduced by my own construction *and* by the independent closed form $336\times124+1$; the two delivered routes are genuinely different computations over shared data (honestly disclosed as such at X09). Cell-completeness: 224 grid cells and the 4 encoding cells both recomputed from the declared sets. S5 **is** genuinely held out — I re-implemented the fit at the single cell $e_1$ with no reference to HELD and got 6,336 / 6,144 / 192 exactly, plus 124/124 and 99/99. BREAK-HOM reproduced (0/125, 6,000/15,625). Synthetic FOUND/EMPTY both reachable (192 pairs / 48 maps at my own synthetic $\tilde E$). No sampling anywhere: confirmed, and the two sub-total sweeps are named — I also ran §4.3's squaring identity at the **full** 240 cells (240/240), so the 40-cell restriction loses nothing. **Only instrument findings: F-4** (typed column with a wholesale-only mutant) **and F-5** (two analytically-forced self-tests). |

---

## What I attacked and could not break

- The census, by two routes of my own construction (structural enumeration over
  all $(g,\lambda)$ pairs at all 125 record cells, and Gaussian elimination):
  0/48/0/48, kernel dims 0/1/0/1. No disagreement.
- The selection rule: lex-first over all 40,320, landing on
  $[0,1,2,3,4,5,7,8,6]$ moving exactly 3 labels — BRG's own witness, as claimed.
  The ord-5 class is 4,608 and the whole fix$_{81}$ spectrum matches the anchor
  member-for-member.
- The direction sweep's honesty. HA's prose and HA's code really do put the
  determinant-2 matrix on opposite sides of the arrow; I rebuilt HA's G28 matrix
  ($\det = 2$, coefficient matrix of $q\to$counts) and confirm X03 is an
  accurate disclosure, not a convenient one.
- The chart-carriage measurement (G09): the natural identification induces slot
  permutation $(1,0,2)$ on both sides, the index one $(1,0,2)$ vs $(2,1,0)$.
  Exactly as stated, including the deviation-1 consequence.
- Both FOUND branches and the negative-with-teeth.
- Every arithmetic claim in §§2–11, 13–14.

**Positive-headline mortality note.** This unit's headline is negative and it
survived. The three *positive* framings inside it — "the square wants $p=3$",
"the wall moved up a level", "what forbids it here is the nine-label arena" —
fared as the arc's pattern predicts: the first needs two scope tags (F-3), the
second is **true and understated** (the spectral condition $4\equiv1$ is genuinely
new relative to BRG's order-coprimality — disjoint prime sets, $\{3\}$ against
$\{5,7\}$ — and F-1 moves the wall a further level the paper did not claim), and
the third is **wrong in the direction that matters** (F-1).

---

## Required before TERMINAL

**F-1** (state the lemma; correct §6; withdraw Open 1's possibility claim; close
X07), **F-2** (declare S1b; add the set-level row), **F-3** (reclassify P8/P9;
tag the $p=3$ sentence), **F-7** (compute P11's set; fix the false universal in
its note).

**Strongly recommended:** **F-4** (measure the declaration-free column — it is
the difference between a typed verdict and a derived one, and it costs one
counterfactual re-declaration the unit can already build), **F-5** (reclassify
or repair the two self-tests), **F-9** (one sentence, once F-1 is in).

**Adjudicable as wording/scope:** F-6, F-8. **F-10** is not a fix to this paper;
it is the successor pin's content, handed over measured.

# **ACCEPT-WITH-FIXES**

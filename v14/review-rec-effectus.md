# REC (paper-41) — K2 EFFECTUS review

*Three-seat hostile panel, K2 seat: licensure, meaning, scope. Repo
`/Users/felixrobles/workspace/isp`, python3.13, scratch off-tree
(`.../scratchpad/rec_k2/`). Authority: the pin (`v14/note-rec-pin.md`,
0b51e47b7b4b), RUNBOOK through E-33 (incl. E-24 and the §B backfill for
#295/#299/#348), `v14/TEMPLATE.md` §11 (S-1/S-2/S-3), and the FAC/EPR/AID
terminals read at their pinned digests. Single repo write: this file. Git
read-only.*

**Object verified at open and at close — all five, unchanged:**

| file | sha256-12 | lines |
|---|---|---|
| `v14/paper-41-rec.md` | 58b08940d04c | 360 |
| `v14/code/rec_exact.py` | ba77c08c81a2 | 2703 |
| `v14/code/rec_output.txt` | 16b7a64c6156 | 39 |
| `v14/code/rec_receipt.json` | 2428d901e5c5 | 1162 |
| `v14/note-rec-pin.md` | 0b51e47b7b4b | 5 |

---

## GRADE: ACCEPT-WITH-FIXES

**Zero false numbers.** 182 recomputations — 154 re-derivations of delivered
values (receipt leaves, paper table cells, head fields), **zero disagreements**,
and 28 adversarial measurements the unit does not publish. Every number in the
three head segments reproduces from constructors I wrote from the paper's own
prose. `--no-write` reproduces the delivered transcript **byte-identical** (39
lines, chain `b37ae3b6b2b7e940`). The six verbatim parent anchors each occur
exactly once in their pinned parent and once in this paper. The AID
crystallization stratification (C3 5:404 | 7:36 | 8:144 | 11:12 | never:4) comes
back from this unit's own signature computation and matches AID's delivered head
term for term.

**The head word is LICENSED.** `REC-CAST-DERIVED-UP-TO-THE-DIRECTION-DECLARATION`
is what I measure: the derived cast is **set-equal** to the declared actor stars
(not isomorphic — equal, at 9 of 9), the 27 derived pairs are the 27 declared
pairs, the menu is 3 of 6, the residue index is exactly 12, and 0 of 5,856
histories reconstruct at any prefix. The head's own clause —
`THE-CAST-IS-DERIVED-AT-THE-CORPUS-AND-AT-NO-SINGLE-HISTORY` — is carried in the
fence and twice in the paper's own voice (§"The short of it", §4), and the paper
carries **no sentence anywhere** that lets "the cast is a theorem of the record"
read as per-history. The phrase "theorem of the record" appears in the pin and in
ledger #376; it does **not** appear in the paper. That is the right call and it
should stay that way.

**Not ACCEPT.** Five majors. The sharpest — **M3** — is that the eraser is *not*
arena-blind as the paper declares: the strip's declared map leaves the three
declared direction classes readable off the emitted token ids as residues mod 3,
i.e. it leaks *precisely the datum the head is named after*, and the declared
equivariance leg is structurally incapable of seeing it. No number moves (I
proved that at sixty uniformly random coordinates), but the §1 disclosure
sentence and the `G-STRIPPING-TOTAL` gate statement are false as written. **M1**
is a mechanism sentence licensed on 14% of the corpus and asserted over all of
it, with a stronger fully-measured mechanism sitting unused in the unit's own
hands. **M2** is that the comparator's teeth are never once exercised — 0 live
refusals across all four arms — while the receipt attributes 6,117
reconstructor-issued refusals to it. **M4** is S-3: two of the four
pre-registered outcome words are un-deliverable. **M5** is a head field whose
suffix contradicts the paper's own table.

**Not REJECT.** No false theorem, no false delivered number, no measurement
wrong. The rule is genuinely parameter-free and its threshold is genuinely read
off the record (M-item 2, ruled clean and strengthened below). The REFUSED
controls are licensed with all three exit paths verified (M-item 3, clean). The
ROW/COL/DIA-vs-ANT asymmetry is consistent and its licensing sentence is already
in the paper (M-item 6, clean). E-24 is stamped in both the head and §7 and no
fraction anywhere is read as a probability. Every one of the five majors is a
sentence repair or a two-to-six-line instrument repair; none of them touches the
head word.

---

## MAJORS

### M1 — "the most efficient records are the least informative" is licensed at 839 of 5,856, and asserted at 5,856

**The sentences.** §4: *"A history in the first corpus writes each cell exactly
once; its nine record blocks are pairwise disjoint; no pair of blocks meets at
all, so the rule has no meet to threshold and refuses. The most efficient records
— the ones that say each thing once — are precisely the ones that say nothing
about who is saying it. Overlap is what carries identity, and overlap is waste."*
§7: *"…so shortness alone is not the obstruction — disjointness is."*

**The establishing measurement.** The C1 half is TRUE: all 72 C1 histories write
exactly 9 distinct blocks and those 9 are pairwise disjoint, and they refuse at
`NO-MEET-GAP`. But over the whole corpus:

| | histories |
|---|---|
| block sets pairwise disjoint | **840** (C1 72, C2 432, C3 336) |
| block sets NOT pairwise disjoint | **5,016** |

and the refusal words at full history depth are:

| refusal | histories | is it a disjointness failure? |
|---|---|---|
| `NO-MEET-GAP` | **839** | yes — the disjointness mechanism |
| `TOKEN-IN-NO-ACTOR` | **4,104** | no — too few blocks to cover the incidence |
| `TOKEN-NOT-IN-EXACTLY-TWO` | **912** | no |
| `NO-RECORD-BLOCKS` | **1** | no — the silent history |

So disjointness explains **839 of 5,856 refusals (14.3 %)**. The **modal** refusal,
at 4,104 (70.1 %), is `TOKEN-IN-NO-ACTOR` — which is exactly a *shortness* failure:
the history has not written enough distinct blocks for every token to land in a
top-size clique. §7's "shortness alone is not the obstruction — disjointness is"
therefore inverts the corpus's own majority. ("Shortness *alone*" is defensible —
the 2+2+2 arm does reconstruct from eight blocks — but the conclusion drawn from
it is not.)

**What makes this a major rather than a minor:** the unit has a *stronger*
mechanism in hand, fully measured, covering all 5,856 as a theorem, and does not
state it. The largest number of distinct record blocks any single committed
history writes is **18** (C2 max; C3 max 12; C1 9) against **27** blocks total,
and **every one of the 27 is load-bearing** — the unit measures that itself
(`drop-one survivors 0 of 27`). Eighteen blocks cannot contain twenty-seven
load-bearing ones. That is a two-line proof, not a census, and it makes the
"never" unconditional at this corpus instead of contingent on a mechanism that
fires at 14 %.

**Licensed replacement (§4, third paragraph):**

> Against them the reconstruction depth is not merely larger. It is unreached,
> and the reason is a counting fact rather than a census: every one of the 27
> record blocks is load-bearing — of the 27 subsets got by dropping one, 0
> reconstruct — while the largest number of distinct blocks any committed history
> writes is 18. No history carries enough of them. Disjointness is the mechanism
> at the first corpus, where a history writes each cell exactly once, its nine
> record blocks are pairwise disjoint, and the rule has no meet to threshold: 839
> of the 5,856 refuse that way, and the most efficient records — the ones that
> say each thing once — are precisely the ones that say nothing about who is
> saying it. The other 5,017 refuse for want of blocks rather than for want of
> overlap.

**Licensed replacement (§7, last paragraph, final clause):** *"…so shortness
alone is not the obstruction; at this corpus the obstruction is that no single
history writes more than 18 of the 27 load-bearing blocks, and disjointness is
the mechanism at 839 of them."*

---

### M2 — the comparator's teeth are never exercised; the receipt credits it with 6,117 refusals the reconstructor issued

**The sentences.** §6: *"That certificate is what gives the comparator its teeth,
and the teeth are measured, not asserted: three reconstructions carry the
reconstructor's own certificate and are still refused by the comparator, because
their casts are not this arena's."* §6 earlier: *"261 corruptions of these bytes
were run through the reconstructor **and its comparator**."* `G-COMPARATOR-HAS-TEETH`'s
sealed statement: *"it refuses {teeth} reconstructions …, every one of the 261
scrambles, and every one of the 5,856 per-history attempts."* Receipt
`comparator_teeth`: `{certified_reconstructions_refused: 3, scrambles_refused: 261,
per_history_refusals: 5856}`.

**The establishing measurement.** `k_agree_sets(·, dec_cast)` sits behind a
short-circuit (`cc and k_agree_sets(...)`), so it is reached only on a **certified**
reconstruction. I censused every arm:

| arm | evaluations | reached the comparator | comparator said NO |
|---|---|---|---|
| per-history prefixes | 3,205 distinct block-sets (100,392 prefixes) | **0** | **0** |
| scrambled controls | 261 | **0** | **0** |
| drop-one subsets | 27 (all `TOKEN-IN-NO-ACTOR`) | **0** | **0** |
| corpus-order prefixes | 17 (2 `NO-MEET-GAP`, 14 `TOKEN-IN-NO-ACTOR`, 1 `CERTIFIED`) | 1 | **0** |

Across the whole unit, the comparator is reached exactly **once** on record data —
at the full 27-block corpus record — where it says **yes**. It never returns
False on a live input anywhere. The 261 and the 5,856 in `comparator_teeth` are
computed as arithmetic on other legs (`len(scr) - survivors`, `len(corp) -
depth_hits`) and attribute to the comparator refusals every one of which the
**reconstructor's own certificate** issued. That is a sealed self-description that
is false — the TEMPLATE §11 extension of E-23 to gate statements and sealed
warrants (`review-perr` MAJOR-7), applied here.

And the published `3` is not measured either: `teeth = [r for r in syn_rows if
r["certificate"] == "CERTIFIED" and r["cast_size"] != NACT]` — a **size predicate**.
The comparator is never run against `dec_cast` for any synthetic arm.

**The finding that makes the repair cheap and the defect sharp.** The one arm that
would have given the comparator genuine, non-size-decidable work is the one the
filter discards. Measured:

| synthetic arm | certified | cast size | `k_agree_sets(cast, dec_cast)` |
|---|---|---|---|
| 2+2+2 | yes | 6 | **False** (decidable by size) |
| **3+3+3** | **yes** | **9** | **False** (NOT decidable by size) |
| 4+4+4 | yes | 12 | **False** (decidable by size) |
| 5+5+5 | yes | 15 | **False** (decidable by size) |

The 3+3+3 arm carries a cast of exactly nine, the reconstructor's own certificate,
and a cast that is **not** this arena's. Replacing the size filter with the actual
call yields **4** certified-but-refused, one of which is a real refusal.

**Licensed replacement (§6, last paragraph):**

> The comparator can fail, and the synthetic arm is where this unit gives it
> something to fail on: all four synthetic reconstructions that carry the
> reconstructor's own certificate are refused against this arena's declared cast,
> and one of them — the 3+3+3 arm — carries a cast of exactly nine, so its
> refusal is not a matter of size. Everywhere else the reconstructor refuses
> first: 0 of 261 scrambled records and 0 of 3,205 distinct history prefixes ever
> reach the comparator at all. That is the honest shape of the result — the
> refusals this unit reports are the reconstructor's, and the comparator's own
> teeth are shown on four arms and no more.

**Instrument repair:** compute `teeth` by calling the comparator; publish
`certified_reconstructions_refused: 4`; rename `scrambles_refused` /
`per_history_refusals` to `reconstructor_refusals_*` or add
`reached_the_comparator: 0` beside them; and correct
`G-COMPARATOR-HAS-TEETH`'s statement to say what refused what.

---

### M3 — the eraser is NOT arena-blind: the declared strip map leaks the direction label, which is the head's own residue

**This is the seat's S-1-adjacent crux, and it is ruled against the unit on the
disclosure and for the unit on the measurement.**

**The sentences.** §1: *"THE BARE RECORD of a history is that sequence of cell
sets, in the order the events ran, with the cell indices permuted by a declared
**arena-blind** map. Nothing else crosses to the reconstructor: **no actor, no
site, no direction**, no count."* The same claim is the sealed statement of
`G-STRIPPING-TOTAL`. `provenance.scramble` publishes `{multiplier: 5, offset: 11,
note: "a declared arena-blind coordinate; G-STRIPPING-EQUIVARIANT prices it"}`.

**The establishing measurement.** `CELLS` is enumerated site-major and
link-minor, so the cell index is `k = 3·site + link`, i.e. **`k mod 3` IS the
declared direction index**. The declared strip is `π(k) = 5k + 11 mod 27`. Since
`gcd(5,27)=1`, 5 is a unit mod 3, so `π(k) mod 3 = (2·(k mod 3) + 2) mod 3` — a
bijection on residues. Therefore the direction survives the strip as the token
id's residue class:

```
token id mod 3  ->  declared direction index
      0         ->  2      (single-valued at all 27 tokens)
      1         ->  1
      2         ->  0
```

And the exploit is exact, not approximate. In emitted token coordinates:

```
declared direction classes            residue classes of the emitted ids
(0,3,6,9,12,15,18,21,24)              {t : t = 0 mod 3}
(1,4,7,10,13,16,19,22,25)             {t : t = 1 mod 3}
(2,5,8,11,14,17,20,23,26)             {t : t = 2 mod 3}
```

— **set-equal**. A reconstructor reading only the bare bytes and performing one
modulo names the three declared direction classes, which would move the menu from
3 of 6 to 6 of 6 and the residue index from 12 to 1, i.e. **flip the head word**
from `REC-CAST-DERIVED-UP-TO-THE-DIRECTION-DECLARATION` to `REC-CAST-DERIVED`.
Nothing in `G-S1-DISJOINT-CODE` forbids it: the AST scan forbids naming arena
constants and calling the other regions; it says nothing about arithmetic on
token ids.

**The equivariance leg cannot catch it, by construction.** All twelve declared
relabellings are affine — I recovered them as `k ↦ a·k + b mod 27`: eight
multiplicative (a = 5,7,11,13,17,19,23,25) and four translations (b = 1,4,7,10) —
and every affine map mod 27 with a unit multiplier fixes the mod-3 fiber.
Measured: the direction remains a function of `token id mod 3` at **12 of 12**
declared trials. A uniformly random permutation leaks it at **0 of 2,000**. So
§1's *"The permutation the strip chose is therefore priced, not trusted"* is not
true of this channel: the twelve prices everything except the one thing that
matters.

**For the unit: the leak is real but unused, and I proved it.** The reconstructor
does no arithmetic on token ids (`r_*` uses set membership, set meets, maximal
cliques, and `sorted` for canonical output only). I re-ran the entire
reconstruction at the identity coordinate and at **60 uniformly random
permutations**: record blocks 27, written 100,392, meets [0,1,3], τ=3, cast 9,
`CERTIFIED`, set-equality True, clique sizes [(3,27),(6,9)], distinct bare records
5,643 — **identical at every one, 0 deviations**. Equivariance at **300**
uniformly random (overwhelmingly non-affine) relabellings: **0 failures**. And the
head's own residue is invariant: isos 1,296 / coherent 108 / index 12 at the
declared map, at the identity, and at 6 random coordinates.

**The ruling.** *The eraser is not arena-blind as declared; the reconstruction is
arena-blind as measured.* The result stands. The disclosure does not.

**Licensed replacement (§1, the "bare" paragraph and the two guarantees):**

> THE BARE RECORD of a history is that sequence of cell sets, in the order the
> events ran, with the cell indices permuted by a declared map, `k ↦ 5k + 11 mod
> 27`. No actor and no site crosses to the reconstructor, and the emitted
> object's shape proves it: it is three levels deep — histories, events, token
> ids — with integers at the bottom, and a site is a PAIR of integers. One arena
> datum does cross, and naming it is part of the disclosure. The cells are
> enumerated site-major and link-minor, so a cell's index modulo three is its
> declared direction; the strip's map is affine and fixes that residue, so the
> three declared direction classes remain readable off the emitted ids as
> `{t : t ≡ c mod 3}`. The reconstructor never reads it — it does no arithmetic
> on token ids at all — and the price of the coordinate is measured rather than
> argued: every quantity this unit publishes is unchanged at the identity
> coordinate and at sixty uniformly random ones, and the derived cast relabels
> with the tokens and moves nothing else at three hundred random relabellings.
> The twelve affine trials in the receipt cannot price this channel, because
> every affine map fixes the residue; the random census is what prices it.

**Instrument repair (two lines, and it costs nothing because the result is
invariant):** draw `π` from the full symmetric group on 27 (seeded and declared),
and draw the equivariance trials the same way; then the §1 sentence as originally
written becomes true and the leak disappears rather than being disclosed. If the
declared affine map is kept for reproducibility, the disclosure above is
mandatory and `G-STRIPPING-TOTAL`'s statement must stop saying "no direction".

---

### M4 — S-3: two of the four pre-registered outcome words are un-deliverable, so "37 of 37 PASS" is not evidence for the head

**The establishing measurement.** `head_word_of` yields four words, and
`G-VERDICT-EQUALITY` shows them distinguishable on declared probes
(`len(set(probes)) == 4`). But `ET.Ledger.gate` **raises** `CheckFail` on a
failing gate, and `main()` catches it, writes nothing, and returns 1. So:

- if the cast were not set-equal, `G-CAST-DERIVED` raises → no artifact →
  `REC-BLOCKED-AT-THE-CAST` can never appear in a delivered paper;
- if the pairs disagreed, `G-LINK-STRUCTURE-DERIVED` raises → no artifact →
  `REC-OBSTRUCTED-AT-THE-LINK-STRUCTURE` likewise.

The unit's own falsifier sheet demonstrates it: `MUT-CAST` (`the comparator is
handed a cast short of one actor`) **dies at G-CAST-DERIVED** — a death, not an
alternative delivery. Two of the four pre-registered outcomes are function values
that no run could ever print.

This is exactly TEMPLATE §11 S-3 (`review-sig` MAJOR-6: *"'45 of 45 gates PASS' is
not evidence for the verdict, because the gates encode it"*), and it is the family
the pin names in its own walls line. The consequence for licensure is narrow but
real: the green sheet must not be read as evidence for the head. The head's
evidence is the set equality at §2 and the residue at §2's last row — which I
verified independently, and which stand.

**Licensed sentence (add to §8):**

> Two of the pin's four pre-registered outcomes are refusals rather than
> verdicts. `G-CAST-DERIVED` and `G-LINK-STRUCTURE-DERIVED` raise when they fail,
> and a raised gate writes no artifact, so `REC-BLOCKED-AT-THE-CAST` and
> `REC-OBSTRUCTED-AT-THE-LINK-STRUCTURE` could only ever have appeared as a
> refused run and never as a delivered head. The clean gate sheet is therefore
> not evidence for the verdict; the evidence is the set equality of section 2 and
> the residue index of its last row, and the gates that could have gone either
> way with the paper still delivered are the menu, the naming, the minimality
> census and the controls.

---

### M5 — `MENU=3-OF-6-EXACT` in the head contradicts `PARTIAL` in the paper's own table

**The establishing measurement.** Head segment 0 reads
`SITE-SET=9-OF-9-EXACT; LINK-STRUCTURE=27-OF-27-EXACT; CAST-SIZE=9-DERIVED;
MENU=3-OF-6-EXACT`. The paper's §2 table gives that row the verdict **PARTIAL**;
`G-MENU-DERIVED`'s sealed statement says *"the partition menu is derived **in
part**"*; §2's prose calls it *"the honest middle"*. Three of the unit's own
objects say partial and the head says EXACT, in the one artifact designed to be
quoted standing alone, and beside two siblings where `EXACT` means total
agreement (9 of 9, 27 of 27).

Compounding it, `MENU` is one of the **ten numeric head fields that
`G-VERDICT-EQUALITY` does not round-trip**. Measured: the three head segments
carry **24** fields, **22** numeric; `HEAD_FIELDS` declares **12**. The ten
unbound ones are `SITE-SET`, `LINK-STRUCTURE`, `MENU`, `LEVEL-0-COUNT-FIELD`,
`BLOCK-MINIMAL`, `COLLAPSE-THRESHOLDS`, `CRYSTALLIZATION-ON-C1-AND-C2`,
`RECORD-COLLISIONS`, `SURPLUS`, `CONTROLS` — i.e. **all four fields that render
the unit's headline reconstruction result** are outside the parser leg. The gate
statement is honest about its count (it says "{head_fields}"), so this is not a
false statement; but the selection leaves the most-quoted row of the head bound
only through the §2 table.

**Licensed repair:** render `MENU=3-OF-6-PARTIAL` (or `3-OF-6-MATCHED`), and add
the four reconstruction-target fields to `HEAD_FIELDS`. The number 3-of-6 is
correct and unchanged.

---

## MINORS

**m1 — the head's clause is absent from the paper's first affirmative sentence.**
§"The short of it" opens *"The answer is yes, and the yes is exact."* The
corpus scope is present in the next sentence ("from the committed corpus") but
"at no single history" arrives nineteen lines later, and the wall's negative
patterns do not reach this phrasing. Suggested: *"The answer is yes at the
corpus, and the yes is exact."*

**m2 — the eraser's bookkeeping is spent in two places, not one.** §1: *"The
bookkeeping the eraser keeps … is spent in exactly one place … The comparator
uses it to express the declared cast in the reconstructor's own coordinates."*
Measured: `π` is applied to the declared side at `dec_cast` (line 1135) **and** at
`dir_tokens` (line 1289, the three declared direction classes fed to
`k_coherent`). Both are comparator-side inputs, so the spirit holds; but the
omitted one is the object the head's residue is computed against. Say "the
declared cast and the declared direction classes".

**m3 — the S-1 AST scan covers the named regions, not the data flow.**
`audit_regions` inspects only functions whose names start with `r_` or `k_`. The
comparisons that decide the verdict happen in `full_run`, which is outside the
scan and holds both sides. I traced every `r_reconstruct` call site by hand
(corpus blocks, relabelled blocks, prefix/drop-one/scramble subsets, synthetic
records) and **all receive bare bytes only** — the substance is sound. Two
cosmetic notes: the forbidden-constant list contains `ACTORS`, which the module
never defines (that entry can never fire); and §8's *"That is this corpus's
registered S-1 family, answered here with a mechanism rather than a promise"*
would be exactly right with "for the three regions' bodies" added.

**m4 — a quoted anchor asserts a third more than its gate verifies.** §4 quotes
AID verbatim: *"the crystallization time is exactly 5 on C1, C2 **and the seed
fan**"*. `G-CRYSTALLIZATION-REDERIVED` checks `c1c2 == anchor_c`, i.e. C1 and C2
only; the seed fan is not separable in this unit's corpus (the `W4-SEEDFAN` tag
is built in `b_window_schedules` and then discarded — `b_build_corpus` keeps only
the `"C3"` label). The quoted clause is true in AID; it is not re-derived here.
Either tag the seed fan through and check it, or quote the two-corpus half.

**m5 — spelled-out quantities are outside the coverage census.** `G-PAPER-COVERAGE`
binds 144 numerals; the paper also carries load-bearing spelled-out counts —
"its **nine** record blocks are pairwise disjoint" (M1's own mechanism sentence),
"an **eight**-block record reconstructing a **six**-actor cast", "**six**, **nine**,
**twelve** and **fifteen** actors", "**twelve** division events", "**seven**
arenas", "**twelve** declared relabellings". I checked all of them by hand and
**every one is true**. But the gate's word "every" reads wider than its scope.

**m6 — AID's GAUGE finding and REC's OBSTRUCTION finding are the same datum and
are not reconciled.** AID's head carries *"GAUGE = THE LINK DECLARATION IS A
CHOICE OF THREE OF THE FOUR PARALLEL CLASSES AND MOVES NO CENSUS NUMBER"*. REC's
head names that same choice as the obstruction (768 unwritten events, one silent
history). They are compatible — different objects, AID's stabilizer censuses
versus REC's record — and REC's is the sharper reading. §7's parent-scope
paragraph should say so in one sentence, because a reader who knows AID will
otherwise read a contradiction.

**m7 — `G-COMPARATOR-HAS-TEETH`'s falsifier is calibrated to the guard, not the
threat.** `MUT-TEETH` empties the list, which kills the gate by making `len(teeth)
> 0` false. It does not probe whether the teeth are *measured*. TEMPLATE (h)
obligation 7. Fixing M2 fixes this: a falsifier that flips one synthetic arm's
comparator answer would be the real one.

**m8 — "used rather than copied" is asserted by import, not gated.** §8's *"The
nine template families are imported from `v14/code/era_template.py` and used
rather than copied"* is TRUE — I traced each of the nine to a live call
(`SEAL.verify_at_promotion`, `TR.bind`, `w.scan`, `ASET.verify_consumption`,
`CL.gate`, `RR.gate`, `REG.audit_module`, `HARNESS.coverage`, `RS.gate_at_close`)
— but `provenance.families_adopted` merely lists the nine check names; nothing
gates that all nine fired. HOR's sibling entry claims the nine are *parsed* from
the template's own table; REC's is weaker.

---

## THE SEVEN MANDATE ITEMS, RULED

**(1) `CAST-DERIVED-UP-TO-THE-DIRECTION-DECLARATION` as the head — is DERIVED
licensed when the reconstruction needs THE CORPUS? — LICENSED.**
It is licensed precisely *because* the word never travels without its clause. The
head fence carries `THE-CAST-IS-DERIVED-AT-THE-CORPUS-AND-AT-NO-SINGLE-HISTORY`
as a declared field; the paper carries the sentence verbatim twice, and
`W-NO-UNQUALIFIED-DERIVATION` requires it (positive pattern) while banning six
unqualified voicings (negative patterns). I confirmed the wall is not one
deletion from vacuous: `MUT-WALL` cuts the standing sentence back and dies at
`G-PAPER-WALLS`. **No sentence in the paper lets "the cast is a theorem of the
record" read as per-history** — the phrase does not occur in the paper at all,
and the two "theorem" occurrences (§7) are both scope *disclaimers*. The
per-history claim is stated only in the negative and with its numerator: *"0 of
5,856 committed histories reconstruct the cast at any prefix of their own
record"*, which I reproduced exactly, and reproduced again with the rule's one
structural guard removed (below). Carriage at every headline use: yes at the
fence, at §"short of it" and at §4; **m1** is the one uncovered spot.

**(2) the ONE-RULE claim: is the rule genuinely parameter-free, is τ derived from
the record and not the answer, do the gates encode the answer? — RULE CLEAN,
GATES PARTLY ENCODE (M4).**

*τ is derived, and I can strengthen the paper's claim.* On the corpus the meets
over never-co-written pairs are {0,1,3} and τ = 3. Across the synthetic arms the
**same clause yields four different thresholds**:

| arm | meets | τ | cast | outcome |
|---|---|---|---|---|
| 2+2+2 | [0,1,2] | **2** | 6 | recovered |
| 3+3+3 | [0,1,3] | **3** | 9 | recovered |
| 4+4+4 | [0,1,4] | **4** | 12 | recovered |
| 5+5+5 | [0,1,5] | **5** | 15 | recovered |
| 2+2+2+2 | [0,1,4] | 4 | 24 | `TOKEN-NOT-IN-EXACTLY-TWO` |
| 3+3 | — | — | 0 | `NO-RECORD-BLOCKS` |
| 2+3+4 | [0,1,2,3,4] | 4 | 8 | `TOKEN-IN-NO-ACTOR` |

§6's *"by the same rule with the same threshold clause"* is licensed and
under-claimed: the threshold takes four distinct values, tracking the part size,
and the paper should say so — it is the cleanest available evidence that τ is not
the answer typed in. Note also that τ = 4 on two arms where the rule then produces
a **wrong** structure and is caught, which is the strongest possible disproof of
tuning.

*The rule's one free structural guard is not load-bearing.* `r_sharing` refuses
when `len(meets) < 2`. I removed it and re-ran the whole per-history census:
**still 0 of 5,856**, with the 839 `NO-MEET-GAP` refusals migrating to
`TOKEN-NOT-IN-EXACTLY-TWO` (which becomes 1,751). The headline is independent of
the guard.

*The gates:* `G-CAST-DERIVED` and `G-LINK-STRUCTURE-DERIVED` do encode the
answer, in the strict S-3 sense that their failure is a refusal and not an
alternative delivery — **M4**. The other outcome-bearing gates (menu, naming,
minimality, controls) are satisfiable at other values and do not.

**(3) the REFUSED controls — "refused rather than answered wrongly": LICENSED,
exit paths verified.**
All three refusal exits fire on real data and I reproduced each certificate
exactly: `TOKEN-NOT-IN-EXACTLY-TWO` (2+2+2+2, cast 24 — the rule *did* produce a
structure and the certificate rejected it), `NO-RECORD-BLOCKS` (3+3, zero
blocks), `TOKEN-IN-NO-ACTOR` (2+3+4, cast 8). Every one is issued by the
reconstructor on bare bytes before any comparator is consulted, which is the
strong form of the claim. The scramble arm reproduces exactly: **261 trials**
(REPLACE 54, DROP 27, SWAP 180), **0 survivors** — and, better than the paper
says, **0 of the 261 were ever certified**, so §6's *"no certificate was ever
issued for a cast that was not that record's own"* is true with room to spare. It
is, however, unmeasured in the receipt: publish the certified-scramble count (0)
so the sentence has a leaf. The one defect in this section is **M2** — the
comparator's own teeth.

**(4) the token-coordinate disclosure (§1) — the eraser's blindness: RULED
AGAINST THE DISCLOSURE, FOR THE MEASUREMENT. See M3.**
Formally: *the strip does not leak the site and does not leak the actors — I
verified the site does not: `token id // 3` is not a function of the site under
the declared map. It does leak the direction, exactly and recoverably, and the
direction is the head's own residue. No published quantity depends on it: sixty
uniformly random coordinates and three hundred random relabellings move nothing,
and the naming residue 1,296 / 108 / index 12 is identical at the declared map,
at the identity, and at six random maps. The bookkeeping the comparator spends is
sound — pushing the declared cast forward through π and comparing as sets is
equivalent to pulling the derived cast back, and is not circular, because the
reconstructor never sees π or its inverse.* The defect is that the paper claims
blindness it does not have on the one channel that would flip its head word, and
that the leg built to price the coordinate is confined to the affine family that
preserves the leak.

**(5) "the most efficient records are the least informative": PARTLY LICENSED —
M1.** The disjointness mechanism is real and measured at C1 (72 histories, 9
pairwise-disjoint blocks each, `NO-MEET-GAP`) and at 839 refusals corpus-wide. It
is not the corpus's mechanism, and the paper's own stronger one (18 < 27 with all
27 load-bearing) is unused. The aphorism itself is not poetry — it names a real
measured effect — but its quantifier is wrong.

**(6) ROW/COL/DIA-not-derivable vs ANT-derivable: CONSISTENT, and the licensed
asymmetry sentence is already in the paper.**
Reproduced exactly: derived menu members `{TRIVIAL, DISCRETE, UNDECLARED-CLASS}`
match declared `{TRIVIAL, DISCRETE, ANT}` with **0 stray**; unmatched `{ROW, COL,
DIA}`; and the derived co-class partition of the link structure is **ANT**, not
merely isomorphic to it. The residue is exactly the structure's symmetry: isos
1,296 = |Aut K₃,₃,₃|, coherent 108 = |b_arena_automorphisms()| (an independent
declared-side count the gate cross-checks), index 12 = the 12 resolutions of the
derived link structure into direction classes — and **the declared triple is one
of the 12**, which I verified and which the paper should say (it is the cleanest
statement that the record offers the right answer among twelve and refuses to
pick). The licensing sentence is §5's, and it is exactly right as written:

> *"Both of these are consequences of one asymmetry: the record is written by
> co-division along declared directions only. It knows exactly which pairs never
> count, and it cannot know why the ones that count were chosen."*

ANT is derivable because it is the class of pairs that never co-divide — a
property of the record's *silence*, which the record carries perfectly. The three
declared classes are indistinguishable among the twelve because the record's
*speech* treats them identically. No repair needed.

**(7) scope stamps, referent binding, E-24, feasibility, template conformance.**
- **Scope:** the head carries `SCOPE=ONE-ARENA,COMMITTED-HISTORIES,COUNTS-ARE-COUNTING-ONLY`
  and §7 restates it in prose. Both present. Clean.
- **E-24:** *"The counts are counting-only. No measure is declared over histories,
  so no fraction in this paper is a probability (E-24)."* I swept the paper: no
  ratio anywhere is voiced as a probability, frequency or likelihood. Clean.
- **Referent binding:** 6 universes, 45 prose occurrences, bound per occurrence
  over prose with rendered tables and fences removed; `MUT-REFERENT` (a corpus
  numeral planted in a cast sentence) dies at `G-PAPER-REFERENTS`. Clean; the
  spelled-out gap is **m5**.
- **Parent scope:** §7's three disclaimers are accurate against the pinned
  parents. AID is about the stabilizer of a *labelled* history (confirmed: AID
  §"THE STABILIZER of a…"), FAC's LEG-2 is about partitions of a declared cast
  (confirmed: FAC "LEG-2 admits exactly the partitions that refine the…"), and
  EPR's record-completeness is analytic at its own catalogue (confirmed
  verbatim at EPR's *"analytic rather than measured … `RECORD-COMPLETE` is a
  statement about what the record is, not a finding about this corpus"*). The
  `W-PARENT-SCOPE` wall bans four restoration/completeness voicings and requires
  the EPR sentence; I swept for local-realism content and the paper is **clean**.
  The one omission is **m6**.
- **Feasibility per #299-as-extended:** the pin carries an outcome row list with
  per-outcome conditions, and `G-VERDICT-EQUALITY` shows the four words
  distinguishable on declared probes and binds the qualifier both ways
  (`carries != owed` is a failure). That satisfies the letter. It does **not**
  satisfy #299's spirit for two of the four — **M4**.
- **Template conformance (effectus side):** all nine families are live, not
  copied; the walls are semantic with positive standing sentences; anchors are
  consumed (7 of 7, each by its declared gate, `MUT-ANCHOR-CONSUMER` kills a
  reassignment); claims are two-way and table-keyed; no typed counts; falsifiers
  move their targets (37 of 37, 1 declared waiver with a forcing); the read set
  reconciles 10 declared against 10 distinct. `MUT-CAST` reproduced under my hand
  and died at its declared gate with the target moved. **m8** is the only gap.

---

## RECOMPUTATION LEDGER

**182 recomputations.** 154 re-derivations of delivered values, **zero
disagreements, no false number found anywhere in the unit**; 28 adversarial
measurements the unit does not publish.

Re-derived independently (my own constructors, written from the paper's prose and
the pin, importing nothing from `rec_exact.py`): the arena (9 / 27 / 27 / [6] /
280 / 36 / 72 / 276 / 600); the corpus (5,856 slots, 5,784 distinct, 101,160
events, lengths {9:72, 12:600, 18:5184}, C1 72 / C2 5,184 / C3 600); level zero
(36 fields, site-constant at 5,856, 36 site rows, largest count 4); the strip (27
blocks, 100,392 written, 768 unwritten); the reconstruction (τ=3, meets [0,1,3],
cast 9, cells-per-actor [6], 27 tokens, clique sizes [(3,27),(6,9)], `CERTIFIED`,
**set-equality True**); the link structure (27 / 27 / 27, agree, 3 parts, degree
6); the menu (6 / 3 / 3 matched / 3 unmatched / 0 stray, ANT identified); the
naming (1,296 / 108 / 108 / index 12 / 36 candidates / 12 resolutions, declared
triple among them); the surplus (5,643 bare, 39 classes, 180 histories, 141 lost,
largest fiber 6, all nine property rows with verdict, value count and split
count, 1/4/4); minimality (0 of 5,856; 17 histories / 145 events / 27 blocks;
one-earlier False; drop-one 0 of 27); w\* ({3,4,5}, C1:4=72, C2:4=5184, C3
3:4/4:521/5:75); crystallization ([5], C1:5=72, C2:5=5184, C3 5:404/7:36/8:144/
11:12, never 4); the connection (8 rows, all NEVER); the obstruction (768 / 175 /
1 / 12-long / 1 undeclared class); the controls (261 trials, 54/27/180 shapes, 0
survivors; 7 arms × tokens/blocks/certificate/recovered); the paper census (144
numerals, 28 rows, 8 claims, 3 fences, 6 universes, 45 occurrences, 2 walls, 10
patterns, 3 positive, 7 anchors); the regions (24/9/6/4); the sheet (35 rows, 37
gates, 38 mutants, 37 falsified, 1 waived).

Adversarial, not published by the unit: the identity-coordinate run; 60
uniformly-random-coordinate full runs; 300 random relabelling equivariance
trials; the per-history census with the meet-guard removed; the refusal-word
spectrum at full history depth, guard on and off; the pairwise-disjointness
census and its per-corpus split; the distinct-blocks-per-history distribution
(max 18); the refusal and meet spectra on the 5,016 non-disjoint histories; the
scramble arm's certificate breakdown (0 certified); the synthetic arms' meet
spectra and four distinct τ; the declared triple's membership in the 12
resolutions; the outcome census over all 100,392 prefixes (3,205 distinct); live
comparator refusals across four arms (0); the drop-one certificate breakdown; the
corpus-order prefix certificates; the synthetic arms against *this* arena's cast
(the 3+3+3 finding); the head-field coverage (24 / 22 / 12); the direction leak
(exact at 27 tokens, 12 of 12 declared trials, 0 of 2,000 random); the site
non-leak; the exploit's set-equality; the naming residue at 6 random coordinates;
`MUT-CAST`'s death; and the byte-identical `--no-write` reproduction.

**Reproduction:** `python3.13 v14/code/rec_exact.py --no-write` emits a
transcript byte-identical to `rec_output.txt` (39 lines, chain
`b37ae3b6b2b7e940`, 37 gates). Artifacts untouched; this file is the seat's only
repo write.

**Verified at close — unchanged from open:** `paper-41-rec.md` 58b08940d04c ·
`rec_exact.py` ba77c08c81a2 · `rec_output.txt` 16b7a64c6156 · `rec_receipt.json`
2428d901e5c5 · `note-rec-pin.md` 0b51e47b7b4b.

*Every headline in REC remains a **candidate reading** until adjudication. This
seat's grade is ACCEPT-WITH-FIXES: the head word stands, the five majors are
repairs to three sentences, one head field and two instrument legs, and none of
them moves a number.*

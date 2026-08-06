# Independent hostile review R2 — effectus / order lens

**Review status:** `ACCEPT-WITH-FIXES`

**Reviewer role:** the descent order and the top-of-lattice guard; kill-shot K3
(overlap neutrality and the next-level smuggling), per
`v13/note-rq0-composite-hostile-protocol.md` (frozen `612b149`)

**Repository mode:** read-only; no repository file edited except this one; no
commits created; no child agents.

## Frozen evidence

| Artifact | SHA-256 | Protocol prefix | Match |
|---|---|---|---|
| `v13/paper-rq0-composite-boundaries.md` | `fc94524d6ef2b8e9281135af70ef127688e8f8ed4c7cd6e91f052dffc0757f0c` | `fc94524d6ef2` | yes |
| `v13/code/rq0_l1_composite_exact.py` | `52809c24034542b231b372f79533dc30ba08b439b2343b32cc1a6339f8fcd5ca` | `52809c240345` | yes |
| `v13/code/rq0_l1_composite_output.txt` | `cb520b01c1dfadde50aab6ab90b82598d8b23a3886032bc067f318c3f6d531d6` | `cb520b01c1df` | yes |
| `v13/code/rq0_l1_composite_receipt.json` | `73dbdc4a1d5f70ff873c82b2d6cac85cdaba21407fff1ef92097ddd12244bbf3` | `73dbdc4a1d5f` | yes |

Object commit `e0216c0`; pin `62cdf68`; protocol `612b149`. All four pinned
digests verify. Every number below was recomputed in my own exact-rational
code (`Fraction` only, no float, no import from the unit under review); the
manufactured boundaries, the Givens rotation, the incidence relation, the
partition lattice, the descent clauses, the closure and the counter-law were
rebuilt from the paper's stated definitions and from the construction recipe
read off the source. I did not read either concurrent review.

## Executive verdict

**No computed number in my remit is wrong.** Every one of the fourteen `H2`
gates reproduces, and the four certified counts, the descent carrier, the
covariance atom map, the moved-projection count, the counter-law triple and
the lattice sizes all come out exactly as printed. The top-of-lattice guard is
sound, and I verified its premise **exhaustively** rather than by the unit's
160 samples. The discriminator fires in both directions as claimed. `REJECT`
is not warranted, and `RQ0-L1-SMUGGLING-SURVIVES-DESCENT` genuinely does not
occur for the three constructed manufactured records.

**What must be fixed is the account of *why* it works.** Three measured facts,
none of them disclosed in the paper, jointly show that at the declared arena
the selector is *not* doing the work the prose attributes to it:

1. the two contexts of the arena are **the same object**, and both are equal
   to the declared overlap (F-1);
2. consequently clause **(D2) is vacuous** at the declared arena — it excludes
   nothing, and the certified set is exactly `(D1) ∧ (D3)` (F-2);
3. the independence certificate is carried by a **family-cardinality
   mismatch**, so the 120-relabelling search could not have returned a witness
   (F-3).

And the K3(ii) adversarial pair **exists**: I construct it below (F-4). It is a
short step from the paper's own §7.6 aligned control, it passes the paper's own
independence gate, and its forged record descends. The paper does not foreclose
it, but it does not name it either, and the "next obstruction, named" paragraph
names the wrong one.

The rungs survive as *scoped*; the escape mechanism must be restated. Hence
`ACCEPT-WITH-FIXES`.

---

## Findings, ranked

### F-1 (MAJOR, disclosure). The arena's two contexts are the same object, and both are the overlap.

`ctx["ERASER"]` and `ctx["ADDRESS"]` are both `boundary_from_blocks(·,
(1,1,1,1,1))`; and `overlap_atoms_diagonal(5)` returns the same five
projections again. I checked all three elementwise:

```
ERASER.atoms == ADDRESS.atoms elementwise : True
declared overlap W == ERASER.atoms        : True
iota(ERASER) == iota(ADDRESS) == identity : True
```

So the "independently declared second context" against which the legitimate
record co-refers has the *identical* boundary, the *identical* core and the
*identical* incidence as the candidate's own context, and the declared overlap
is that same algebra a third time. §5.2's table shows the two identical
incidence rows but the paper never says the objects coincide, and §1.4's
no-smuggling gate asserts the opposite (see S-1).

This is not gerrymandering — the corrected eraser minimum *is* the committed
address algebra, which is legitimate laboratory data. It is a reporting
failure, and a load-bearing one, because everything in F-2 follows from it.

### F-2 (MAJOR). Clause (D2) is vacuous at the declared arena; the certified set is `(D1) ∧ (D3)`.

Because the second context's atoms are the overlap atoms, it realizes **every
one of the 52 partitions of the overlap**:

```
facts realized by ADDRESS = 52 ;  partitions of the 5 overlap atoms = 52 ;  equal: True
```

Therefore any record satisfying (D1) and (D3) satisfies (D2) automatically. I
confirmed extensionally on all five contexts that the certified set equals the
`(D1) ∧ (D3)` set exactly (1/1, 1/1, 1/1, 51/51, 14/14). **The second context
imposes no constraint whatsoever at the declared arena.**

The consequences are precise and they matter:

- The escape from the predecessor's obstruction is carried by **posing
  availability at an externally declared algebra** — a *different carrier for
  the availability test* — and **not** by comparing two contexts. The pair
  structure of §6.2 is definitionally present and extensionally inert here.
- §7.1's "positive control, the identity overlap" is **numerically the same
  computation** as §6.4's direction two: `self_inc == inc["ERASER"]` and
  `self_facts == addr_facts` identically, so `H2-09`'s 51 and `H2-07`'s 51 are
  one number reported twice. I verified the two certified sets are equal as
  sets. A control that is the same computation as the result it controls is
  not a control.
- (D2) does bite in exactly one place in the unit: the coarser `TOMO` arena,
  where only 2 of 52 facts are realized. There it is purely restrictive
  (51 → 1). So across the whole paper, co-reference either does nothing or
  only withdraws certificates; it never certifies anything that (D1) ∧ (D3)
  did not already certify.

The guard is **not** damaged by this: (D1) alone already rejects ⊤ for the
three manufactured contexts, and (D1) at a foreign algebra is not a closure on
the candidate's lattice. But the paper's stated reason for the escape ("its
carrier is the pair-plus-overlap structure") is, at the declared arena, carried
entirely by the *overlap* half of that phrase.

### F-3 (MAJOR). The independence certificate is carried by a cardinality mismatch, not by the relabelling search.

The declared families are `|𝔉_eraser| = 2` and `|𝔉_address| = 6`. A relabelling
acts bijectively on a family, so the image of a 2-element family has 2 elements
and can never equal a 6-element set. **The 120-element search is structurally
incapable of returning a witness**, for a reason that has nothing to do with
the contexts' operational content. The same holds for the manufactured family
(`|𝔉_man| = 2` against 6).

The control (`H2-03`) is genuinely informative — there the sizes match, and the
gate correctly names six carrying isomorphisms with the cyclic shift among them
(recomputed: 6, shift present). But Proposition 5.4's positive certificate
rests on `2 ≠ 6`. As stated — "Searching all one hundred and twenty admitted
address relabellings … none carries the declared eraser family onto the
declared address family" — the sentence is true and the emphasis is misleading.

This is what makes F-4 cheap.

### F-4 (MAJOR — the K3(ii) answer). The adversarial pair exists. Construction supplied.

**Claim.** Under the committed laws, an adversary who declares *both* contexts
can pass the independence gate and have a forged record descend.

**Construction** (all objects built by the unit's own recipes; verified in my
code):

- **Context 1** = the manufacturing construction at rank multiset (2,1,1) with
  the rotation deleted — i.e. the paper's own `ALIGNED211`, a measure *chosen*
  to match a preselected PVM, aligned with the declared addresses.
  ι = ({0,1},{2},{3},{4}).
- **Context 2** = the same manufacturing construction at rank multiset
  (1,1,1,1) with the rotation deleted — again a *chosen* measure, not an earned
  boundary. ι = ({0},{1},{2},{3},{4}).
- **Forged record** = ⊤ of context 1, its atom instrument — exactly the object
  the predecessor proved no one-boundary closure can reject.

**Result.** (D1) holds (images {0,1},{2},{3},{4} pairwise disjoint); (D3) holds;
(D2) holds — context 2 realizes that fact content. The forged record
**descends**; 14 of context 1's 15 records are certified. Running the unit's own
`independence()` over all 120 relabellings on the adversary's two declared
families returns **independent, empty witness list**. Both contexts are
manufactured, the pair passes the gate, and the forged record is certified.

**Why the gate cannot stop it.** Independence is measured on declared future
families; descent is measured on incidence. An adversary who controls both
declarations controls both, and needs only (i) two families of different
cardinality (F-3), and (ii) a chosen measure aligned with the declared overlap.
Declaring the overlap *first* (deviation 6) blocks fitting the overlap to a
preselected context; it does **not** block fitting contexts to a declared
overlap, which is all this construction does.

**Adjudication of the protocol's requirement.** The paper does **not**
foreclose this — §7.6 and §8 both say plainly that descent "does not certify
that a boundary was not chosen to match a measure", and by symmetry that covers
both slots. So no false claim is made. But the paper does not *name* the pair
case either, and §8's "The next obstruction, named" names arena-relativity
instead — which is the weaker of the two open problems now on the table. Given
that the discriminator is the verdict-level object of this cycle, the omission
is material. **Required fix:** name the adversarial pair explicitly in §8 and
add it to the non-claims; the construction above may be cited or reproduced.

### F-5 (MODERATE). "Fails for exactly the feature that manufactured it" is the wrong diagnosis as written — and the right one is a provable theorem the paper does not state.

§6.4's bolded sentence invites the reading *manufacture ⇒ failure*, which the
paper's own §7.6 refutes. The true statement is sharper, and I prove it:

> **At this overlap, ⊤ transports without collision ⟺ every atom of the measure
> is a coordinate (address) projection.**
> (⇐) trivial. (⇒) If the atoms' address supports are pairwise disjoint they
> partition the addresses, so for each atom `P_r` and each `j ∉ S_r` we have
> `(P_r)_{jj} = 0`, and `P_r ⪰ 0` forces row and column `j` to vanish; hence
> `P_r ⪯ Q_r`, the coordinate projection onto `S_r`. Since `Σ P_r = Σ Q_r = I`
> and each `Q_r − P_r ⪰ 0`, every `Q_r − P_r = 0`. ∎

I verified the biconditional on all six contexts in play (six for six, no
mismatch). So the discriminator's negative direction separates **rotated from
address-aligned**, exactly and analytically — not manufactured from earned. The
manufactured records were built by rotating the coordinate basis and the
overlap was declared to *be* the coordinate algebra, so their rejection is
guaranteed by construction. The paper says the right thing at §7.6 and the
wrong thing at §6.4; the two should be reconciled, and the lemma is worth
stating because it is what actually makes the negative direction robust.

### F-6 (MINOR). The 160-family sweep is attached to a claim it does not support, and is weaker than an available exhaustive check.

Theorem 6.2 says "Every closure operator on the same record lattice fixes that
greatest record — re-verified natively here on one hundred and sixty declared
admitted families…". The universal claim is proved one line later by
extensivity and needs no sampling; the 160 families verify only that the
predecessor's *availability* closure is extensive on those families. The
em-dash makes a decoration look like the evidence.

Moreover the sampled check is strictly weaker than what is cheaply available. I
swept **every** left-total relation at n = 2, 3, 4 — 9, 343 and 50 625
relations — and confirmed that no relation available at ⊤ has a non-discrete
collision partition. Hence `cl_𝔽(⊤) = ⊤` for **every** family over those
relations, not 160 of them. Recommend reporting the exhaustive form.

### F-7 (MINOR). Theorem 6.3 proves less than its title, and could prove more.

The theorem exhibits *one* map (the predecessor's witness) and shows it moves
the overlap; that does not show no overlap-preserving carrying map exists. But
the stronger statement is free here and follows from F-1: the overlap atoms
*are* the eraser atoms, so **any** reversible map carrying the legitimate
boundary onto the manufactured one sends the overlap atoms to the manufactured
atoms, four of which are non-diagonal. The obstruction therefore fails to
transfer for *every* carrying map, not just the committed one. Recommend
upgrading the theorem; as written it is a witness, not a non-transfer proof.

### F-8 (MINOR). Two undisclosed deviations from the pin.

Appendix A is otherwise complete and honest, but it omits:

- (a) that the two declared contexts are instantiated by the *same* boundary
  object, and that the declared overlap is that object too. The pin asks for
  two families "each with its own earned boundary and core" and for the overlap
  to be "a common subsystem … reachable from both"; here it is not a common
  *sub*structure but the whole of both. This is exactly the F-1 disclosure and
  belongs in the appendix as a declared deviation.
- (b) that the pin's control 1 ("every factor record descends trivially along
  the identity overlap") is satisfied by the same computation as the main
  positive direction (F-2), rather than by an independent configuration.

### F-9 (MINOR, no action required). The exhibited "descent order" is a one-point poset.

The carrier for `MAN211` against `ADDRESS` has exactly one element (recomputed:
1, components `{{0,1,2},{3}}` and `{{0,1,2,3},{4}}`), so "ordered by refinement
in each component" orders nothing. The paper states the size honestly and the
absence claim is correct and is stronger than the pin's requirement
(non-maximality); I note only that the word *order* is doing no work. I also
checked the guard is order-convention-robust: for all three manufactured
contexts the certified set omits both the discrete and the indiscrete
partition, so the argument survives either reading of "top".

---

## K3 adjudication

**K3(i) — is every de-smuggling sentence scoped to the declared arena?**
*Substantially yes, with one exception that is false as instantiated and two
that leak.* The scope box, the ten-item non-claims list, §8's "no
arena-independent selector", and §7.6's two measured limits are all correct and
correctly scoped; the forbidden vocabulary appears only inside the scope box and
the negations, which the protocol permits; all fifteen numbered results carry
scope tags; there is no review-round language anywhere (single-threaded). The
exception and the leaks are S-1, S-2, S-3 below.

**K3(ii) — the adversarial-pair question.** **Answered affirmatively: the
construction exists** (F-4). Under the committed laws an adversary who declares
both contexts passes the independence gate — by cardinality alone — and has a
forged record descend, provided only that the chosen measure is aligned with
the declared overlap. The paper leaves the question open honestly (it makes no
claim the pair case is blocked) but does not name it, and names a weaker
obstruction in its place. That is the principal required fix.

---

## Numbers table (paper / receipt / my independent recomputation)

| # | Quantity | Paper | Receipt | R2 recomputation | Verdict |
|---|---|---|---|---|---|
| 1 | `MAN211` incidence | {0,1,2},{0,1,2,3},{0,1,2,3},{4} | `TABLES.incidence` | identical | ✅ |
| 2 | `MAN22` incidence | {0,1,2},{0,1,2,3},{4} | idem | identical | ✅ |
| 3 | `MAN1111` incidence | {0,1},{0,1,2},{0,1,2,3},{0,1,2,3},{4} | idem | identical | ✅ |
| 4 | `ERASER` / `ADDRESS` incidence | {0},{1},{2},{3},{4} (both) | idem | identical (**and the same object**, F-1) | ✅ |
| 5 | `TOMO` incidence | {0,1,2,3},{4} | idem | identical | ✅ |
| 6 | `ALIGNED211` incidence | {0,1},{2},{3},{4} | idem | identical | ✅ |
| 7 | manufactured centre dimensions | 4, 3, 5 | anchors L10/L11/L12 | 4, 3, 5 | ✅ |
| 8 | PVM rank multisets | (2,1,1), (2,2), (1,1,1,1) | anchors L10r/L11r/L12r | identical | ✅ |
| 9 | certified of `MAN211` | 1 of 15 | `H2-05b` 1 / 15 | 1 of 15, record `{{0,1,2},{3}}` | ✅ |
| 10 | certified of `MAN22` | 1 of 5 | `H2-05b` 1 / 5 | 1 of 5, record `{{0,1},{2}}` | ✅ |
| 11 | certified of `MAN1111` | 1 of 52 | `H2-05b` 1 / 52 | 1 of 52, record `{{0,1,2,3},{4}}` | ✅ |
| 12 | certified of `ERASER` | 51 of 52 | `H2-07` [51, 52] | 51 of 52 | ✅ |
| 13 | ⊤ passes (D1)? (three manufactured) | no (all three) | `H2-06` false ×3 | false, false, false | ✅ |
| 14 | descent carrier size | exactly 1 | `H2-05c` 1 | 1 | ✅ |
| 15 | carrier's components | `{{0,1,2},{3}}` / `{{0,1,2,3},{4}}` | `H2-05c` idem | identical | ✅ |
| 16 | candidate present in carrier | no | `H2-05c` false | absent | ✅ |
| 17 | covariance atom map | (4,0,1,2,3) | anchor L13 | (4,0,1,2,3) | ✅ |
| 18 | overlap projections moved | four of five | `H2-04` [F,T,T,T,T] | 4 of 5 | ✅ |
| 19 | closure families swept | 160 | `H2-05a` 160 | 160 sampled; **exhaustive 9 + 343 + 50 625** | ✅ (F-6) |
| 20 | relabellings searched | 120 | `H2-02` 120 | 120; certificate carried by 2 ≠ 6 (F-3) | ✅ (F-3) |
| 21 | carrying isomorphisms in control | six, shift among them | `H2-03` 6, shift first | 6, shift present | ✅ |
| 22 | counter-law admitted sector maps | 120 | anchor L20 | 120 | ✅ |
| 23 | counter-law reversible maps | exactly 1 | anchor L21 | 1 | ✅ |
| 24 | counter-law records fixed | 52 | anchor L22 | 52 | ✅ |
| 25 | eraser certificate under `TOMO` | 51 → 1 | `H2-08b` 1 | 1 | ✅ |
| 26 | identity-overlap control | 51 of 52 | `H2-09` 51 / 52 | 51 — **same computation as #12** (F-2) | ✅ (F-2) |
| 27 | fact/token split atom counts | 4 vs 5 | `H2-10` 4, 5 | 4 vs 5, co-referring record exhibited | ✅ |
| 28 | record-lattice sizes | 1, 2, 5, 15, 52 | anchors L08-1…5 | 1, 2, 5, 15, 52 | ✅ |
| 29 | facts realized by second context | — (unreported) | — | **52 = all partitions** (F-2) | new |
| 30 | `ALIGNED211` certified count | — (unreported) | `H2-08b` 14 | 14 of 15 | ✅ |
| 31 | gates / anchors / mutants | 25 / 31 / 9 | 25 / 31 / 6+3 | consistent | ✅ |

Zero discrepancies. Rows 29 and 30 are quantities the receipt or my run
produces that the paper does not report and, in the case of row 29, should.

---

## Per-rung confirmations (protocol §"Verdict vocabulary")

- **(a) factorization / support-space lemma, carrier ≤ 20 and lemma-carried
  scope — CONFIRMED as scoped.** Not my primary (R1 holds it). Within my lens I
  confirm the bookkeeping is consistent: 9 fixtures give 81 ordered pairs, 65
  at composite carrier dimension ≤ 20 and 16 above it, the cap is printed in
  the receipt and restated at the claim and in deviation 9, and the
  lemma-carried remainder is flagged at the verdict. No arithmetic objection.
- **(b) corrected witness (gap = joint readability; gap + atom classification =
  entanglement), incl. the parity refutation — CONFIRMED as scoped.** Not my
  primary. The correction is carried consistently through abstract, §4.3, the
  verdict, deviation 1 and the receipt's `corrections` field; the naive
  pre-registered form is recorded as refuted by its own control rather than
  quietly dropped. No leak into an unqualified entanglement claim anywhere.
- **(c) the discriminator both ways at the declared arena — CONFIRMED, with
  F-5's re-diagnosis.** Negative direction: all three manufactured ⊤ records
  fail (D1) and are certified against neither second context — recomputed, three
  for three. Positive direction: the eraser ⊤ record transports, is non-vacuous
  and has an exhibited co-referring record — recomputed. The mechanism is
  rotated-vs-address-aligned, not manufactured-vs-earned (F-5).
- **(d) the top-of-lattice guard escape — CONFIRMED, and stronger than
  claimed.** The certified set omits ⊤ for all three manufactured contexts;
  every closure fixes ⊤ by extensivity; the sets are therefore distinct. I
  verified the premise exhaustively (F-6) and checked order-convention
  robustness (F-9). The escape is genuine and is not a renaming. **But** the
  carrier that delivers it is the declared overlap, not the pair (F-2).
- **(e) the measured limits honestly framed — CONFIRMED for the two limits
  stated; INCOMPLETE.** Aligned manufacture descends (recomputed: certified,
  14/15) and the coarser context withdraws the certificate (51 → 1): both are
  in §7.6 *and* in the verdict, which is the right discipline. The third limit —
  the adversarial pair (F-4) — is missing and must join them.
- **(f) the verdict rungs as the correct pre-registered instantiations —
  CONFIRMED with one scope amendment.** `RQ0-L1-COMPOSITE-BOUNDARY` and
  `RQ0-L1-ENTANGLEMENT-WITNESS (corrected)` are correctly instantiated.
  `RQ0-L1-DESCENT-SELECTOR` is earned at the declared arena, but its scope line
  must record that at that arena the second context realizes every partition of
  the overlap, so the co-reference clause excludes nothing and the rejection is
  carried by transport at the declared overlap.
  `RQ0-L1-SMUGGLING-SURVIVES-DESCENT` correctly does not occur: the escalation
  condition is the *constructed* manufactured record descending, and it does
  not. F-4 is a different and weaker object — an adversary permitted to declare
  both contexts — and does **not** trigger the escalation as pre-registered.

---

## Sentences to rewrite

- **S-1 (required; false as instantiated).** §1.4, Object 2, No-smuggling gate:
  "the overlap is declared **before** either context and independently of both
  candidates". The declared overlap *is* the legitimate candidate's own core
  algebra, atom for atom (F-1). Rewrite to state the coincidence and defend it
  on its merits — the corrected eraser minimum is the committed address
  algebra, which is laboratory data — rather than claiming an independence that
  does not hold.
- **S-2 (required).** §6.4: "**The manufactured record fails for exactly the
  feature that manufactured it.** The measure was chosen in a rotated basis…"
  Replace with the biconditional of F-5 and its proof, and say plainly that the
  separation is rotated-vs-address-aligned. As written it contradicts §7.6.
- **S-3 (required).** §6.2: "Its carrier is the pair-plus-overlap structure".
  True definitionally, misleading extensionally. Add: at the declared arena the
  second context realizes all 52 partitions of the overlap, so the certified set
  coincides with the records that transport without collision and are
  non-vacuous; the escape is carried by posing availability at the declared
  overlap. Same amendment to the abstract's paragraph beginning "The selector
  escapes the predecessor's obstruction".
- **S-4 (required).** §7.1: "For the selector, when the declared overlap is a
  context's own core and the second context is a copy, fifty-one of the
  fifty-two records descend". Disclose that this is the same computation as
  §6.4's direction two, not an independent control.
- **S-5 (required).** §8, "The next obstruction, named": add the adversarial
  pair (F-4) — an adversary who declares both contexts passes the independence
  gate and has a forged record descend — and add a matching non-claim. Keep
  arena-relativity; it is real but it is not the nearest obstruction.
- **S-6 (recommended).** §5.4 / Proposition 5.4: state that the two declared
  families have different cardinalities (2 and 6), so no relabelling could
  carry either onto the other, and that the search is confirmatory rather than
  decisive. The control at §5.4's second paragraph is where the gate is shown
  to bite, and that is the right place for the emphasis.
- **S-7 (recommended).** Theorem 6.2: separate the extensivity proof from the
  160-family sweep, and report the exhaustive sweep (F-6) instead.
- **S-8 (recommended).** Theorem 6.3: upgrade from one witness to all carrying
  maps (F-7), which the coincidence of overlap atoms with eraser atoms gives
  for free.
- **S-9 (recommended).** Appendix A: add deviations (a) and (b) of F-8.

---

## Common gates

| Gate | Disposition |
|---|---|
| Paper-vs-receipt number sweep (≥ 10) | 31 rows swept, zero discrepancies |
| Scope tags | all 15 numbered results tagged; §3.1, §4.1 and §7.x carry measured claims in untagged prose (minor) |
| Carrier caps printed | yes — 65 of 81, cap 20, in claim, verdict, deviation 9 and receipt |
| Forbidden vocabulary | clean; `locality/topology/causal/spacetime/gravity` occur only in the scope box and the negated non-claims, which the protocol permits; "local" occurs only in the tensor-factor sense |
| Arena-independent selector claim | none; §8 explicitly denies one. Two indefinite-article formulations ("at *an* independently declared overlap") read more generally than the arena warrants — see S-3 |
| Prose vs gates | one load-bearing claim in ungated prose: §6.4's rotation diagnosis (F-5/S-2) |
| Deviations appendix | present, ten items, honest; two omissions (F-8) |
| Mutants / determinism / floats | 9 mutants (6 anchor, 3 derivation) incl. `descent-lax` and `fact-coarse` which hit the discriminator's own clauses; determinism statement present, no wall-clock in receipt or rendered output; arithmetic declared exact with an AST float sweep — consistent with my float-free reproduction |
| Single-threaded | yes; no round, referee, revision or "initially" language anywhere |

---

## Verdict

`ACCEPT-WITH-FIXES`

The order-theoretic content is correct and every number in my remit
reproduces exactly. The top-of-lattice guard genuinely escapes the
predecessor's obstruction, and I verified its premise more strongly than the
unit does. The discriminator fires in both directions, and the escalation
outcome correctly does not occur.

The required fixes are S-1 through S-5: the paper must disclose that the two
arena contexts and the declared overlap are one object, that the co-reference
clause is therefore vacuous at the declared arena, that the escape is carried
by the overlap rather than by the pair, that §7.1 is not an independent
control, and that the adversarial pair — both contexts manufactured, gate
passed, forged record descending — is the nearest open obstruction. None of
these overturns a rung as scoped; all of them change what the rung is
understood to have shown.

**FREEZE-ON-DELIVERY.** This file is the review of record and is not amended
after delivery.

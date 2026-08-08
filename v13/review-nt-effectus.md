# NT — HOSTILE REVIEW R2 (EFFECTUS / CATEGORICAL LENS)

**Reviewer:** R2, structural/conceptual lens — what the verdicts MEAN and
whether the constructions carry them.
**Object:** `v13/paper-nt-nomological-transport.md` + `v13/code/nt_transport_exact.py`
+ `_output.txt` + `_receipt.json`, frozen per `v13/note-nt-hostile-protocol.md`.
**Protocol:** frozen kill-shots K1–K5; primary weight on K2 (the mechanism) and
on the K3 weld claim.
**Date:** 2026-08-07. **Lean:** none. **Git:** none. **Child agents:** none.

---

## 0. SHA verification (done first)

| artifact | claimed | computed | |
|---|---|---|---|
| `v13/paper-nt-nomological-transport.md` | `730679a896de` | `730679a896de` | ✓ |
| `v13/code/nt_transport_exact.py` | `76fb081b124f` | `76fb081b124f` | ✓ |
| `v13/code/nt_transport_output.txt` | `e0dca9e00d34` | `e0dca9e00d34` | ✓ |
| `v13/code/nt_transport_receipt.json` | `b0f6482be448` | `b0f6482be448` | ✓ |

All four match. Review proceeds.

## 0.1 Method and recomputation count

Every quantity below was recomputed in my own scripts
(`/private/tmp/.../scratchpad/r2_recompute.py`, `r2_mechanism.py`,
`r2_singlerule.py`, `r2_group_id.py`, `r2_gauge.py`, `r2_probes.py`,
`r2_crossing.py`), importing **only** the committed base
(`v12/paper1_code/model_composite.py`, `v12/code/w6_coreference_exact.py`) —
my own sparse linear algebra, my own graph, my own path walker, my own pair
counter, my own holonomy. Nothing was imported from `nt_transport_exact.py`.

**Recomputation count: 45 independent recomputations** (enumerated in §1 and
§2). In addition the frozen instrument was re-run unmutated (`--quiet`, no
artifact write) and under two mutants, as a reproducibility check only.

Interpreter `/opt/homebrew/bin/python3.13`. Exact arithmetic throughout
(the committed field; no float anywhere in my scripts either).

---

## 1. What reproduces (the verification ledger)

Everything in this list reproduced **exactly**, entry by entry, from my own
construction. Where the paper prints a number, my number is the same number.

1. Declared permutation scope: 72 base / 96 extension / **2** admitted after
   the $j_0$ filter / **8** admitted extension.
2. Prefix-alignment profile, 18 cells (multiset-of-canonical-keys route).
3. **Cross-check of the K4 independence claim:** the same 18 cells recomputed
   by an *explicit permutation search over leg orders* (O4's route) — identical
   cell for cell.
4. Transport profile, 18 cells, from my own four-clause admissibility predicate.
5. Residual profile $\lVert r\rVert_0$, 18 cells.
6. **18/18** prefix agreement.
7. **12/18** residual agreement.
8. The **six** equal-residual/opposite-transport witnesses, all six, by setting.
9. Admitted-permutation counts per (rule, checkpoint, setting) — 48 cells:
   FULL $=1,1,0,1$ at $t=0,1,2,3$ everywhere; REAL $=0$ at SP-A…SP-D and
   $=1,1,1,1$ at SP-E/SP-F.
10. The 26 identification links of §3.2, with their permutation names and
    prefix-alignment flags.
11. Links / cycle rank per setting: 9/2 at SP-A…SP-D, **13/6** at SP-E/SP-F.
12. Reduced-path enumeration: 422 × 4 + 16,168 × 2 = **34,024**.
13. Closed paths **56 / 2,820** (my raw counts 64 / 2,828 include the eight
    length-0 paths the instrument correctly excludes).
14. Path pairs sharing both endpoints: **4,972,096**.
15. The **entire** matched pair table of §6 — all 18 cells (3 objects × 2
    corridors × {agree, disagree}) — identical to the last digit, plus
    obstructed $=0$ everywhere.
16. **Brute-force cross-check:** at SP-A every pair enumerated literally
    (not by multiplicity closed form) agrees with the closed-form counting.
17. The 48-node posability/weld table: `both_factors_declared`,
    `amplitude_composition_exact`, `defect == W5 residual`, nnz, $j_0$ weight.
18. Defect-weight profile: 0 at $t\in\{0,3\}$ everywhere; 0 at all four
    checkpoints at SP-A/SP-B/SP-E; **288** nonzero with **16** in the $j_0$
    column at $t\in\{1,2\}$ at SP-C/SP-D/SP-F.
19. Identification multiplicity per (setting, checkpoint), 24 coordinates.
20. Holonomy class of **every** closed path at **every** base node (5,928 loops).
21. The eight K1 witnesses: six aligned-prefix bigons ($t\in\{0,1,3\}$ ×
    SP-E/SP-F) → **the wing exchange**, sign orbit $\{+1\}$; two
    prefix-crossing loops → **the identity**.
22. The bigons are genuine closed loops: both links join $(F_2,t)\to(F_1,t)$,
    both flagged prefix-aligned. Confirmed link by link.
23. The canonical loop at all six settings: **the identity matrix on the nose**
    (not merely identity permutation part).
24. The twisted comparator: not a signed permutation at SP-A…SP-D; another
    permutation with sign orbit $\{-1,+1\}$ at SP-E/SP-F.
25. The **full §5 probe table**, 20 rows, including both asymmetric cells:
    SP-F bigon at $t=1$ does **not** return T2; SP-F crossing loop does **not**
    return T1 while SP-E's does.
26. Per-object distinct transported values **223 / 5 / 186**.
27. Per-object per-setting loop value-set sizes, all 18 numbers
    (T1 11,11,17,17,14,58; T2 1,1,2,2,1,3; T3 1,1,1,1,14,14).
28. T2's wing-conjugation motion at all 48 nodes: moves exactly at
    SP-C, SP-D, SP-F at $t\in\{1,2\}$ (both frames) — so §5 reading 5's
    "SP-F only, because there alone is the defect nonzero *and* the wing
    exchange certified" is correct.
29. Leg commutation $[L_2,L_3]=0$ at all six settings (anchor A14's content).
30. The intertwining relations $P_W L^{F_2} P_W$ vs $L^{F_1}$, 3 legs × 6
    settings.
31. T1's stated cause: the transposed one-step Born matrix fails to invert the
    forward one at **leg 1 (the prep leg) at every setting** — so the canonical
    loop cannot return T1 anywhere. Verified, 36 checks.
32. §7's sweep instance count: 6 settings × (1 or 3 declared roles) ×
    $(512+128)$ = **6,400**, matching the receipt's 6,400 misses / 0 hits.
33. Receipt bookkeeping: 15 gates (1 disclosure), 22 anchors all passing,
    21 mutants, **21 died**, split **17 computation / 4 waiver**
    (`posability-lax`, `control-lax`, `flip-lax`, `verdict-lax`),
    `never_falsified` **empty** at denominator 13 — the 14th must-pass gate
    being `NT-FALSIFICATION`, the census's own gate, correctly excluded and
    correctly disclosed in §10.
34. Frozen instrument re-run unmutated: `KILL-JSON {"failed_anchors": [],
    "failed_gates": []}`.
35. Mutants `defect-order` and `gauge-sign` re-run: both die on exactly the
    gates/anchors the receipt declares.

Nine further recomputations appear as evidence under the findings (§2):
the single-rule sub-connections, the value-set-by-permutation, the group
identification and its scope membership, the Klein-four structure, the
global-scalar switching action, the checkpoint telescoping, the
comparator-dependence of the flat crossing, the crossing/aligned holonomy
distributions, and the clause-2 ⟹ clause-3 entailment test. **45 total.**

**Nothing in the pair table, the probe table, the prefix re-derivation, the
weld table or the per-object verdicts is wrong.** The unit's four
pre-registered verdicts — `NT-HOLONOMY-⟨T1⟩`, `NT-HOLONOMY-⟨T2⟩`,
`NT-HOLONOMY-⟨T3⟩`, `NT-PREFIX-FLATNESS-REFUTED` — survive every attack I
mounted. I could not refute the refutation: twisted corridors and flat
crossings both genuinely exist on this base.

The findings below are about **what the paper says the measurements mean**.

---

## 2. Findings

### F1 [CRITICAL] §8.2's holonomy value set is 4, not 3. The instrument counts *names*, not permutations.

**Claim under attack.** §8.2: "SP-E, SP-F | **3** — the identity, **the wing
exchange**, and one further permutation | **order 4**, computed by closure",
together with D5: "The value set is enumerated at the declared length bound
and need not be closed under composition there, so the group it generates is
computed separately by closure rather than read off the count — the two are
different objects and the receipt carries both."

**Measured.** Enumerating every closed path based at $F_1@t{=}0$ and taking
the permutation part exactly, the realized value set at **SP-E** and at
**SP-F** contains **four distinct permutations**, and the group they generate
has order **4**. The value set **is** the group, exactly, at every setting:

| setting | distinct permutations realized | distinct *names* realized | generated group |
|---|---|---|---|
| SP-A…SP-D | 1 | 1 | 1 |
| **SP-E** | **4** | 3 | 4 |
| **SP-F** | **4** | 3 | 4 |

**Mechanism of the error.** `nt_transport_exact.py:2249` accumulates
`els.add(PERM_NAME.get(canon(...), "another permutation"))` — a set of
**strings**, with every permutation that is neither the identity nor the wing
exchange collapsed onto the single label `"another permutation"`. `len(els)`
is then reported as `value_set_size`. The generated group is computed from the
actual tuples (`perms_seen`), which is why the receipt's own
`group_elements` field prints **`["another permutation", "another
permutation", "the identity", "the wing exchange"]`** — four entries, two
bearing the same label. The receipt therefore contradicts its own
`value_set_size: 3` on the adjacent line, and the paper carried the 3.

This is a computed number, but computed **of the wrong object**. It is the
`#24` failure in the RUNBOOK's own catalogue in a new dress: the count did not
have to be typed to be wrong.

**Consequence beyond the digit.** D5's careful-sounding distinction — value set
vs generated group, "the two are different objects" — is on this base an
*artifact of the naming collapse*. Once counted correctly the value set equals
the group at every one of the six settings, and D5's caution has nothing to
caution about here. The paper's rhetorical care is spent defending a gap that
its own bug created.

**Repair.** Count canonical permutation tuples, not names. Restate §8.2 as
"**4** — the identity, the wing exchange, and **two** further permutations",
add that the value set is measured to *be* the generated group at the declared
bound at every setting, and rewrite D5 to record that fact rather than the
hypothetical.

---

### F2 [CRITICAL] K2's mechanism is false in the "and only there" direction. Holonomy occurs at coordinates of multiplicity **one**, under a **single** rule.

**Claim under attack.** §6: "holonomy appears **exactly where** the base admits
**two different certified identifications at one coordinate**, and the two
differ by the base's own **wing exchange**." The protocol asks me to confirm
holonomy occurs *there and only there* against the full path-pair table.

**Multiplicity map (recomputed, 24 coordinates).** Identification-multiplicity
$\ge 2$ occurs at exactly six coordinates: SP-E and SP-F at $t\in\{0,1,3\}$
(FULL supplies the identity, REALIZED supplies the wing exchange). At
SP-E/SP-F $t=2$ multiplicity is **1** (REALIZED only). At SP-A…SP-D it is 1 at
$t\in\{0,1,3\}$ and 0 at $t=2$.

**Sufficiency holds.** At every one of those six coordinates the bigon fires
with holonomy the wing exchange. Confirmed, 6/6.

**Necessity fails, decisively.** Three independent measurements:

**(a) The REALIZED rule *alone* is not flat.** Build the sub-connection using
only the REALIZED rule's identifications — a connection in which *every*
coordinate has multiplicity exactly one:

| setting / rules | links | rank | closed paths at $F_1@t0$ | classes | group |
|---|---|---|---|---|---|
| SP-E / FULL only | 9 | 2 | 8 | identity ×8 | 1 |
| **SP-E / REAL only** | 10 | 3 | 18 | **identity ×10, other ×8** | **2** |
| SP-E / FULL+REAL | 13 | 6 | 364 | id 82, wing 86, other 196 | 4 |
| SP-F / FULL only | 9 | 2 | 8 | identity ×8 | 1 |
| **SP-F / REAL only** | 10 | 3 | 18 | **identity ×10, other ×8** | **2** |
| SP-F / FULL+REAL | 13 | 6 | 364 | id 82, wing 86, other 196 | 4 |

Eight of eighteen closed paths in the single-rule REALIZED connection carry
**non-identity** holonomy. No coordinate in that connection admits two maps.

**(b) In the delivered graph, 348 closed paths per setting are non-flat
without ever traversing two maps at one coordinate.** Cross-tabulating every
closed path by (holonomy class, parity of REALIZED links used, whether any one
checkpoint was traversed by both rules):

| SP-E, "both maps at one coordinate" = **False** | count |
|---|---|
| identity | 228 |
| **the wing exchange** | **120** |
| **another permutation** | **128** (20 at even REAL-parity, 108 at odd) |
| **not a signed permutation** | **100** |

Non-identity total **348** (SP-F: also 348). Minimal witnesses include the loop
using FULL@$t{=}3$ and REAL@$t{=}0$ — two identifications at *different*
coordinates — with holonomy the wing exchange, and the loop using REAL@$t{=}3$
and REAL@$t{=}0$ — one rule, two coordinates — with holonomy a further
permutation. It is not even a parity law: 20 loops with **even** REALIZED
parity and no shared coordinate are non-flat.

**(c) The proximate cause, measured.** $P_W\,L_1^{F_2}\,P_W \neq L_1^{F_1}$ at
**every one of the six settings** — the wing exchange does **not** intertwine
the prep leg (while it *does* intertwine legs 2 and 3 at SP-E/SP-F, which is
what makes the crossing loop flat). Any loop that crosses between the frames
by the wing exchange at $t=0$ and returns at $t=1$ therefore picks up
$P_W U_{\text{prep}}^{-1} P_W U_{\text{prep}}$, which I verify is exactly the
first of the two "further permutations" of F1.

**Verdict on K2.** The mechanism statement is **correct as a sufficient
condition** and **false as the biconditional the paper writes**. What actually
generates the holonomy is two things, not one: (i) the two declared
co-reference rules differ by $W$, and (ii) $W$ fails to intertwine the prep
leg. The paper reports only (i), and reports it with "exactly where".

**Repair.** (1) Downgrade §6 to "holonomy appears **wherever** the base admits
two different admitted identifications at one coordinate — and also
elsewhere". (2) Add the three-row single-rule sub-connection table above: it
costs three lines of code, is the decisive diagnostic for the mechanism
question, and would have caught this before delivery. (3) State (ii) as the
second generator, with the measured non-intertwining of the prep leg.

---

### F3 [MAJOR] The earned holonomy group is a Klein four-group **half of which lies outside the base's declared permutation scope**, and §8.3 reports it as "two-element".

**Measured.** At SP-E and SP-F the based holonomy group at $F_1@t{=}0$ is
abelian of exponent 2 and order 4: $\{1,\;W,\;X,\;WX\}$ where

- $W$ = the base's wing exchange (swaps the qubit pair **and** the pointer
  pair), 12 fixed points among the 36 configurations;
- $X = P_W U_{\text{prep}}^{-1} P_W U_{\text{prep}}$ = the **qubit-only** wing
  swap ($q_A\!\leftrightarrow\! q_B$, pointers fixed), 18 fixed points;
- $WX$ = the **pointer-only** wing swap ($p_A\!\leftrightarrow\! p_B$, qubits
  fixed), 12 fixed points.

**Scope membership, checked element by element against the base's own
generators:**

| element | in the admitted 2 | in the declared 72 | in the declared 96 | in the admitted extension 8 |
|---|---|---|---|---|
| identity | yes | yes | yes | yes |
| wing exchange | yes | yes | yes | yes |
| **$X$ (qubit-only swap)** | **no** | **no** | **no** | **no** |
| **$WX$ (pointer-only swap)** | **no** | **no** | **no** | **no** |

The declared scope's `swap` flag always exchanges the qubit pair **and** the
pointer pair together (`build_perm`/`build_perm_tr`: `idx(qb2,qa2,pb2,pa2)`),
so the two factors of $W$ are individually outside it.

**Why this matters structurally, and it is the deepest finding of my lens.**
The unit's connection is built from links the base certifies, but the *group
those links generate around loops* is **not a subgroup of the base's certified
isomorphisms**. The connection is not principal for the base's own structure
group. A theory that claims to *earn* a geometric structure has, on this
measurement, earned a structure group half of whose elements the base does not
recognise as isomorphisms of anything. That is a genuinely interesting
result — arguably more interesting than the one the paper states — and it is
entirely absent from the paper.

It also puts §9 clause 9 ("The permutation scopes are declared and every
negative is a negative at the stated scope: 72 elements admitting 2 after the
$j_0$ filter, 96 admitting 8") in tension with §8.2: the *positive* object the
unit reports lives outside both declared scopes.

**And §8.3 understates by a factor of two.** "The geometric structure the
theory earns here is small and exactly named — **a two-element wing-exchange
holonomy** at the two symmetric settings" contradicts §8.2's own
`generated_group_order: 4` on the previous page, and contradicts the measured
value set of 4.

**Repair.** Name the group: $\mathbb{Z}_2\times\mathbb{Z}_2 =
\{1, W, X, WX\}$, identify $X$ and $WX$ concretely, print their scope
membership, withdraw "two-element" from §8.3, and add a scope clause stating
that the holonomy group is **not** contained in the declared admitted
isomorphism group.

---

### F4 [MAJOR] The weld (K3) is **entailed by the gate's own preceding clause**, is an instance of paper 1's engraved *exemption*, and was already committed at v12 by W5. The identity itself is exact — the claim strength is wrong.

**The identity is real.** I confirm, at all **48** nodes, independently:
$\Delta^{B}(\Theta(N{\leftarrow}t),\Theta(t{\leftarrow}0)) =
\Gamma(N{\leftarrow}0) - \Gamma(N{\leftarrow}t)\Gamma(t{\leftarrow}0)$,
entry by entry, with the defect weight profile 0/288/16 as printed. K3's
factual clause passes.

**But it cannot fail.** Write $D = B(U_2U_1) - B(U_2)B(U_1)$ and
$r = B(\Theta(N{\leftarrow}0)) - B(U_2)B(U_1)$. The second terms are literally
the same expression in the same code. Hence
$D - r = B(U_2U_1) - B(\Theta(N{\leftarrow}0))$, which vanishes **identically**
the moment clause 2 (`amplitude_composition_exact`:
$U_2U_1 = \Theta(N{\leftarrow}0)$ *on the nose*) holds, because $B$ is a
function of the matrix. I verified the entailment at all 48 nodes and it is
also two lines of algebra. **Clause 3 of `NT-T2-POSABILITY` carries zero
information beyond clause 2 in the unmutated instrument.** (The gate as a
conjunction is still falsifiable — `defect-order` breaks it by perturbing the
*defect*, and I ran that mutant and watched it die — but no possible state of
the world consistent with clause 2 makes clause 3 fail.)

**It is paper 1's own exemption, not a discovery against it.** Paper 1
§2.4, in the very subsection whose item (iv) NT cites for T2's action, engraves:

> "$\Delta^{B}$ is an amplitude-level coherence measure. It is not a
> divisibility measure, not a witness of indivisibility, and **not the residual
> of any declared stochastic law unless that law is declared to be $B(U_2)$**."

NT's construction declares the law to be exactly $\Gamma = B(\Theta)$ — i.e. it
lands precisely inside the single exemption paper 1 wrote down. The weld is
therefore not a cross-corpus surprise; it is the instantiation of a clause
paper 1 committed in advance. The paper cites neither the engraved sentence
nor the exemption.

**And W5 already measured it, in these words.** `v12/code/w5_ltp_lemma_exact.py`,
check **M4**:

> "THE AMPLITUDE PROPAGATORS COMPOSE EXACTLY: $\Theta(3{\leftarrow}0) =
> \Theta(3{\leftarrow}2)\Theta(2{\leftarrow}0)$ at all 1296 entries, in both
> frames at all six setting pairs. **This is what makes the declared residual
> $D_{210}$ EQUAL to the Born-shadow defect $\Delta^{B}(\Theta(3{\leftarrow}2),
> \Theta(2{\leftarrow}0))$** of [p0]'s T2' on this model — **the two objects are
> distinct in general and coincide here**."

W5 states the identity, states its cause (exact amplitude composition — NT's
clause 2), and carries the general/local scope caveat. NT's contribution is the
extension from the one cut $t=2$ to all four cuts and both frames — real, but
small, and not what the abstract advertises.

**What the paper claims.** Abstract: "behind an exact-posability gate that also
measures it to be *identical* to W5's declared-law residual". §4.1 clause 3:
"**the weld.** … Paper 1's composition defect and W5's divisibility residual
are **one object** on this base, not two." No citation to W5 M4; no citation to
paper 1's engraved clause; no statement that clause 3 follows from clause 2.
Read cold, this is presented as a fresh cross-corpus identification of
ontological weight. It is not. It is a re-measurement, at wider scope, of a
committed v12 result that is definitional given the model's own dictionary.

Note also that the residual NT compares against is **re-typed inline** in
`t2_posability` (lines 958–959), not imported from W5's committed
implementation. For a unit whose whole discipline is exit-1 anchoring against
committed receipts, the one place a genuine cross-corpus check was available
is the one place it was hand-transcribed.

**Repair.** (1) Demote clause 3 from "measurement" to an **anchor** against
W5 M4 and paper 1 §2.4's exemption clause, and cite both. (2) State plainly
that clause 3 follows from clause 2, so that the reader is not sold an
independent measurement. (3) Rewrite the abstract's and §4.1's weld sentence to
"the declared law on this base *is* $B(\Theta)$, which is the sole case in
which paper 1's $\Delta^{B}$ is a divisibility residual (paper 1 §2.4); W5
recorded this at the $t=2$ cut and it is here extended to all four cuts in both
frames". That claim is true, correctly attributed, and still worth making.

---

### F5 [MODERATE] The §14 gauge sweep's headline clause cannot fail. The declared switching acts by a **global scalar** on every closed loop.

**Measured.** For every closed loop and every switching $\varepsilon$, the
switched loop matrix is exactly $\left(\prod_{\text{edges}}
\varepsilon_{\ell}\right)\cdot H$ — verified on 12 loops × 20 random
switchings, exactly, with no exception. Consequently:

- **"The permutation part takes exactly one value under every switching swept"**
  is an algebraic identity: negating a matrix does not move its permutation
  part. No switching, sampled or complete, could ever move it.
- **"The checkpoint subgroup leaves even the loop's sign fixed"** is the
  telescoping identity $\prod_{\text{edges}} s_a s_b = 1$ around a closed
  loop — verified on 12 loops × 30 checkpoint switchings, always $+1$.

Only the third clause (the raw sign *moves* under the full link-sign group) has
content, and that too is forced whenever a loop traverses some link an odd
number of times.

§7 asserts: "the sweep is **built so that a wrong invariant would show**." On
this construction no wrong invariant of the relevant kind *can* show, because
the declared gauge action is by scalars and every scalar-blind functional is
automatically invariant. RUNBOOK §14 exists because branch A "exhibited the
gauge orbit as physics" and no mutant could catch it; this sweep formally
satisfies §14 while leaving exactly that failure mode untested.

**One point in the unit's favour, which the paper does not make.** The same
scalar structure **settles K3's D2 attack outright**: the unswept 7,680
elements of the 8,192-element group at SP-E/SP-F cannot hide switching-variance
of the permutation part, because there is none to hide, at any switching. The
`[SAMP]` disclosure is honest but unnecessary, and the correct argument is
structural, not statistical.

**Repair.** Say what the sweep establishes (the reported invariant is
scalar-blind, and the gauge orbit is the overall sign) and what it does not
(that the permutation part is the *right* content). Add a mutant that computes a
genuinely switching-variant functional and must die. Replace D2's sampling
caveat with the scalar argument.

---

### F6 [MODERATE] "Certified" is used, throughout, for transports the base's own certificate **refuses**; and D3's disclosure omits the SP-E case.

The word carries the paper's headline: §5 reading 2, "the base admits a second
**certified** identification"; §6, "two different **certified** identifications
at one coordinate"; §8.3, "the coordinates where the base admits two
**certified** co-reference rules at once"; and the abstract.

**The base says otherwise.** The O4 terminal paper's certificate table:

| | $t=1$ | $t=2$ | $t=3$ |
|---|---|---|---|
| F-CFG | VACUOUS ×6 | **DISAGREEMENT ×6** | True ×5, **VACUOUS at SP-E** |

and its derived sentence: "**no cell of the matched table reaches a certified,
unique, covariant transport, for any fact-class**" at the intermediate read
times; and, specifically about the object NT uses, "**the realized-only rule's
two transports there are refused by the certificate**."

D3 discloses the criterion swap (FORCED, not CERT) and §8.4 prints both
readings — that part is honest, and I record it as such. But:

1. the body of the paper never repairs the vocabulary, so every headline
   sentence uses an adjective the immutable base denies at those coordinates;
2. D3 says the CERT reading "would admit links only at the final division event
   and would empty the loop space" — it omits that at **SP-E** the certificate
   is VACUOUS at $t=3$ as well, so under CERT the loop space at SP-E would be
   empty *outright*. SP-E is one of the two settings carrying the entire
   headline.

**Repair.** Replace "certified" with "admitted (the discriminator's FORCED)"
everywhere outside D3/§8.4; add the SP-E $t=3$ VACUOUS fact to D3.

---

### F7 [MODERATE] The $t=0$ rows of §3.1 are **not** O4 re-derivations, and the two $t=0$ witnesses sit at a coordinate where the two "contexts" are the same object.

§3.1: "This table is the whole geometry of what follows, and **every row of it
is a re-derivation of an O4-terminal measurement**", glossed by the O4 counts
"$1,0,1$ at $t=1,2,3$" and "$0,0,0,0,1,1$".

O4's `READ_TIMES = tuple(range(1, NLEGS+1))` — **$t=0$ is outside the O4
instrument entirely**. The four $t=0$ rows are this unit's own extension, and
the paper's own gloss (which covers $t=1,2,3$) shows it. Two of the six
twisted-corridor witnesses — the $t=0$ bigons at SP-E and SP-F — live there.

Worse conceptually: at $t=0$ no leg has been applied, so $(F_1,0)$ and
$(F_2,0)$ are two graph nodes for **one and the same context**
($p = \delta_{j_0}$, identical law, identical support). The "identification"
there is a map from a context to itself, and the set of admitted such maps is
that context's **stabiliser**, not a co-reference between frames. That a
coarser rule (REALIZED) admits a larger stabiliser than a finer rule (FULL) is
not a discovery about transport; and the bigon holonomy is then, by
construction, the *ratio of the two admitted maps* — $a^{-1}b = I^{-1}W = W$ —
an algebraic identity, not a measurement. (The same construction remark applies
to the $t=1$ and $t=3$ bigons: once §3.1's table is fixed, every bigon's
holonomy is forced. The genuine measurement is the §3.1 table itself, which is
O4-inherited at $t\in\{1,2,3\}$.)

**Repair.** Mark the $t=0$ rows as this unit's own extension; state the witness
count as "four at O4 coordinates, two at a coordinate O4 did not evaluate";
state explicitly that a bigon's holonomy is the ratio of the two admitted maps,
so that the reader sees the §3.1 table, and not the bigon, as the measurement.
The refutation survives on the $t=1$ and $t=3$ witnesses alone, so nothing is
lost.

---

### F8 [MODERATE] The "flat crossing" is **comparator-dependent**, and §5 reading 3 states more than existence.

The instrument builds the crossing loop by pairing the divergent REAL link at
$t=2$ with a link **of the same rule** at $t=1$
(`nt_transport_exact.py:1233-1235`). Recomputing the alternatives through the
same divergent checkpoint:

| loop through the $t=2$ divergent link | SP-E | SP-F |
|---|---|---|
| closed by **REAL**@$t{=}1$ (the instrument's choice) | identity | identity |
| closed by **FULL**@$t{=}1$ | **the wing exchange** | **the wing exchange** |
| closed by **REAL**@$t{=}3$ | identity | identity |
| closed by **FULL**@$t{=}3$ | **another permutation** | **not a signed permutation** |

And over the whole enumerated space, closed paths that cross divergence:

| | identity | wing | other | not a signed perm | total |
|---|---|---|---|---|---|
| SP-E crossing | **480** | 316 | 256 | 216 | 1,268 |
| SP-F crossing | **480** | 316 | 100 | 372 | 1,268 |

The *existence* claim that refutes the hypothesis is sound — 480 flat crossing
loops per setting is not a fluke, and §6's careful sentence ("Crossing
divergence costs nothing **when the crossing is made by the symmetry that the
divergence is a divergence of**") is exactly right. But §5 reading 3 —
"**the loop** through the divergent checkpoint $t=2$ is measured flat" — and
the abstract's "a loop that crosses the prefix-divergent checkpoint has
holonomy exactly the identity" read as properties of crossing. They are
properties of *that* comparator. Symmetrically, aligned closed paths are mostly
**not** flat (SP-E: 444 identity of 1,552).

**Repair.** Print the two distributions above; restate reading 3 as "a crossing
loop exists whose holonomy is exactly the identity — the one whose two crossing
legs are made by the same rule — while other crossing loops through the same
checkpoint carry the wing exchange and beyond."

---

### F9 [MINOR-MODERATE] The instrument silently discards closed loops that are not signed permutations; §8.2's "every closed path" is not what the code does.

`nt_transport_exact.py:2247-2248` does `if p is None: continue`, with no tally
anywhere in the receipt. Measured over all base points:

| setting | closed paths | **holonomy is not a signed permutation** |
|---|---|---|
| SP-A…SP-D | 56 | 0 |
| **SP-E** | 2,820 | **600 (21%)** |
| **SP-F** | 2,820 | **820 (29%)** |

At the paper's declared base point $F_1@t{=}0$ the count is **0** at every
setting, so **no reported number is wrong**. But §8.2's description —
"enumerated over **every closed path of the committed path space**" — is not
accurate as written, and the declared "gauge-invariant content" (the
permutation part) is simply **undefined** on a fifth to a third of the loop
space at exactly the two settings that carry the result. That is a fact about
the connection, not a bookkeeping detail, and a base point one node away would
have silently dropped it.

**Repair.** Tally and print the `p is None` count; re-word §8.2 to "every closed
path based at $F_1@t{=}0$"; and report the non-signed-permutation fraction as
the finding it is.

---

### F10 [MINOR] The equivariance citation for T2's action is loose.

T2's identification action conjugates $\Delta^B \mapsto P\Delta^B P^{-1}$,
cited to "paper 1 equivariance (iv)". Paper 1's (iv) is
$\Delta^{B}(PU_2, U_1P) = P\,\Delta^{B}(U_2,U_1)\,P$ — a statement about
inserting $P$ at the two **outer** slots, not about conjugating both cut
factors. The two coincide here because both admitted maps ($I$ and $W$) are
involutions, so $P = P^{-1}$; the citation does not license the action in
general.

**Repair.** Either derive the conjugation action directly (the identification is
an isomorphism of contexts intertwining the declared laws) or state the
involutive-$P$ caveat.

---

## 3. Kill-shot disposition

**K1 — the refutation witnesses. SURVIVES, with F8.** All eight recomputed
independently: six bigons → the wing exchange, sign orbit $\{+1\}$; two
crossings → the identity. The bigons are genuine closed loops with both
endpoints at $(F_2,t)\to(F_1,t)$ and both links flagged prefix-aligned. The
L5-disease attack **fails**: the wing exchange is a permutation part, invariant
under the declared switching action, hence gauge-invariant content and not an
orbit relabelled — though see F5 for how cheaply that invariance comes. The
flat crossing's identity is *genuine* (it follows from the measured
intertwining $P_W L_2^{F_2} P_W = L_2^{F_1}$ at SP-E/SP-F, not from the
construction of the links) but the choice of comparator matters (F8). Two of the
six twisted witnesses sit at a coordinate O4 never evaluated (F7).

**K2 — the mechanism. KILLED on the "only there" clause (F2),** with the
"certified" clause separately compromised (F6) and the $t=0$ instances
compromised (F7). Sufficiency verified 6/6; necessity refuted by the
single-rule REALIZED sub-connection (8 of 18 loops non-flat with multiplicity 1
everywhere), by 348 counterexample loops per setting in the delivered graph,
and by the measured failure of $W$ to intertwine the prep leg at every setting.
The D3 demotion (FORCED not CERT) is *disclosed* but not *repaired*: the
adjective "certified" continues to do headline work for transports the base's
certificate refuses.

**K3 — the holonomy computations.** T1: 223 values, nontrivial at all six,
cause verified by construction (the transposed one-step Born matrix fails to
invert the forward one at the prep leg at every setting). T2: 5 values, weld
exact at all 48 nodes — **but entailed by clause 2, engraved as paper 1's
exemption, and already committed by W5 M4 (F4)**. T3: value set is **4, not
3 (F1)**; the group is order 4 — a Klein four-group — and **half its elements
lie outside the declared 72- and 96-element scopes (F3)**. D2 is answered
outright by the scalar structure of the switching action (F5).

**K4 — PREFIX-DECIDES re-derivation. REPRODUCES; the independence is
algorithmic only.** 18/18, 12/18 and all six witnesses reproduce from my own
predicate, and anchors A01–A07 pass. But O4's `prefix_alignment` computes
`any(all(leg_match(...)) for sg in permutations(...))` and NT computes multiset
equality of the same canonical keys: these are two implementations of **one
mathematical predicate**, and I confirm they agree cell for cell precisely
because they are the same predicate. §2's "The route is different from O4's,
deliberately … needs no permutation search at all" is true of the algorithm and
overstated as *derivational* independence. The genuinely independent parts are
the four-clause admissibility predicate and the residual-as-$j_0$-column route,
and those are the ones worth advertising.

**K5 — instrument. LARGELY CLEAN.** D1's scoping is legitimate: the canonical
loop's failure to return T1 is reported as the finding it is (§8.1), the cause
is verified by construction, and the layer contrast is stated rather than
reconciled away — this is not an instrument defect in the reverse-leg
construction, since `minv` is the transpose and the legs are exactly orthogonal
(anchored). D8's fix audits clean: 21 mutants, 21 died, 17 computation / 4
waiver counted from the declarations, and the waiver convention (overwrite the
predicate to `False`) now does what a waiver is for. `never_falsified` is empty
at denominator 13; the exempt 14th is `NT-FALSIFICATION`, the census's own gate
— correctly self-excluded and correctly disclosed. Path counts (9/13 links,
rank 2/6, 34,024 paths, 4,972,096 pairs) all recomputed, including a
brute-force pair enumeration at SP-A that validates the closed-form
multiplicity counting. Fresh-eval verified: 6,400 misses is exactly
$\sum_{\text{settings}} (\text{roles}) \times (512+128)$, and 0 hits. All 22
anchors pass on re-run. The one instrument defect I found is F1's
count-by-name, plus F9's silent filter.

---

## 4. The conceptual assessment (my lens)

**Does the existence/uniqueness split overclaim what a finite base shows?**
The split itself — §6's "Prefix alignment governs *whether an identification
exists*. It does not govern *whether the identifications that exist agree with
each other*" — is the paper's best sentence and it is earned. It is a clean
conceptual separation, it is what the measurement actually supports, and it
correctly demotes the pre-registered hypothesis. §9 clause 10's disclaimer
(no continuum, no curvature, operational vocabulary only) is exactly right and
I have no quarrel with it.

**But the "earned geometry" framing does overclaim, in three specific ways.**

1. **The connection is a superposition of two mutually inconsistent
   conventions.** The graph contains links from the FULL-declared-leg rule and
   the REALIZED-only rule simultaneously. These are two different declarations
   of what co-reference *means*. A connection is a choice; putting two
   incompatible choices into one graph guarantees non-flatness wherever they
   differ, and the "curvature" so obtained is the *difference between two
   conventions*, not a property of the base. §6 half-says this; §8.3's "the
   geometric structure the theory earns here" does not.

2. **The bigon witnesses are algebraic identities given §3.1.** A bigon whose
   two edges are the two admitted maps at one coordinate has holonomy
   $a^{-1}b$ by construction; with $a=I$ and $b=W$ the answer is $W$ and no
   computation could return anything else. The measurement is the §3.1
   admission table (inherited from O4 at $t\in\{1,2,3\}$, this unit's own at
   $t=0$); the bigon is its restatement. The paper honestly says the links are
   not manufactured here; it does not say the *value* is forced.

3. **The structure group is not the base's.** F3: half the earned group is
   outside the declared 72- and 96-element scopes. A geometric structure whose
   structure group the base does not certify is not a structure the base has
   earned; it is a structure the *chart bookkeeping* generates. This is, to me,
   the most interesting thing the unit measured and did not notice.

**What I think the unit actually shows,** stated at the strength the
measurements carry: *On this finite base, two declared co-reference rules that
the discriminator admits uniquely disagree by the wing exchange; a graph
connection built from both is non-flat, with holonomy group
$\mathbb{Z}_2\times\mathbb{Z}_2$ generated by that disagreement and by the wing
exchange's failure to intertwine the preparation leg; the pin's own canonical
loop is exactly flat because the two frames' legs commute; and the prefix
criterion governs existence of identifications, not their agreement — so the
pre-registered flatness criterion is refuted in both directions.* That is a
real, publishable, correctly-scoped result. It is not "the first geometric
structure this programme could earn rather than assume", and the paper would be
stronger for saying so.

**On the weld's ontological weight (the protocol's second primary).** The
identity is exact and I verify it at all 48 nodes. Its weight is small and the
paper claims it large. Paper 1 wrote down in advance the one condition under
which $\Delta^{B}$ *is* a declared-law residual; this model satisfies that
condition by construction; W5 already recorded the coincidence and its cause at
the $t=2$ cut. The honest claim is *instantiation at wider scope*, and that is
still worth stating — a genuine weld would require a model where the declared
law is **not** $B(\Theta)$, and this base cannot supply one. §9 should say so.

---

## 5. Findings ranked

| # | severity | finding | blocking? |
|---|---|---|---|
| F1 | **CRITICAL** | §8.2's value set is 4, not 3; the instrument counts names, and the receipt's own `group_elements` contradicts it | **yes** |
| F2 | **CRITICAL** | K2's mechanism false as stated: the REALIZED rule alone is non-flat; 348 counterexample loops per setting; prep leg not intertwined | **yes** |
| F3 | MAJOR | the holonomy group is Klein four with half its elements outside the declared scope; §8.3's "two-element" is wrong | **yes** |
| F4 | MAJOR | the weld is entailed by clause 2, is paper 1's engraved exemption, and was committed by W5 M4 | yes (claim strength) |
| F5 | MODERATE | the §14 sweep's headline clause cannot fail (switching acts by a global scalar); D2 answered structurally | no |
| F6 | MODERATE | "certified" used for transports the base's certificate refuses; D3 omits SP-E $t{=}3$ VACUOUS | no |
| F7 | MODERATE | $t=0$ rows are not O4 re-derivations; the $t=0$ "identification" is a stabiliser of one context | no |
| F8 | MODERATE | the flat crossing is comparator-dependent; only 480 of 1,268 crossing loops are flat | no |
| F9 | MINOR-MOD | 600/820 of 2,820 closed loops are not signed permutations and are silently dropped; §8.2's "every closed path" | no |
| F10 | MINOR | paper 1 (iv) is an outer-slot law, not conjugation; correct here only because both maps are involutions | no |

---

## 6. Grade

Every pre-registered verdict survived my attempt to break it. The prefix
re-derivation, the path space, the entire matched pair table, the probe table,
the weld table and the per-object verdicts reproduce **exactly** under an
independent construction — 45 recomputations, one false number. The unit is
honest about its deviations, its controls have teeth where teeth are possible,
and its central conceptual separation (existence vs agreement) is earned.

But the protocol's primary target — K2's mechanism — is **false as written**,
and I refuted it three independent ways; §8.2 carries a **wrong count**
produced by counting labels instead of values, with the receipt contradicting
itself on the adjacent line; the earned structure group is **twice the size
the summary states and half outside the base's own scope**; and the weld is
advertised at a strength the algebra, paper 1's engraved clause and W5's
committed M4 all deny. None of these require a new campaign — each is a
bounded repair against measurements already in hand, and F2's decisive
diagnostic (the single-rule sub-connection table) is three lines of code.

> **ACCEPT-WITH-FIXES.**
>
> Blocking: **F1** (recount the value set by permutation; correct §8.2 and D5),
> **F2** (restate the mechanism as sufficient-not-necessary; add the
> single-rule sub-connection table and the prep-leg non-intertwining),
> **F3** (name the Klein four-group, identify $X$ and $WX$, print their scope
> membership, withdraw "two-element" from §8.3), **F4** (re-scope the weld to
> instantiation; anchor it to W5 M4 and paper 1 §2.4).
>
> Non-blocking but recommended before terminal: F5–F10.

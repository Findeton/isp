# GEN — HOSTILE REVIEW R2 (EFFECTUS / CATEGORICAL LENS)

**Reviewer:** R2, structural/conceptual lens — what the verdict MEANS and
whether the construction carries it.
**Object:** `v13/paper-gen-generality-check.md` + `v13/code/gen_generality_exact.py`
+ `_output.txt` + `_receipt.json`, frozen per `v13/note-gen-hostile-protocol.md`
(commit `de695e9`, pin `0da6205815a6` @ `5e8bc58`).
**Protocol:** frozen kill-shots K1–K5; primary weight on **K1, the completion
question**, plus K3's steering audit and the cross-base sentence.
**Date:** 2026-08-08. **Lean:** none. **Git:** none. **Child agents:** none.

---

## 0. SHA verification (done first)

| artifact | claimed | computed | |
|---|---|---|---|
| `v13/paper-gen-generality-check.md` | `4baf4e22c1aa` | `4baf4e22c1aa` | ✓ |
| `v13/code/gen_generality_exact.py` | `78baf5eb3ef6` | `78baf5eb3ef6` | ✓ |
| `v13/code/gen_generality_output.txt` | `9dc0ff7ed387` | `9dc0ff7ed387` | ✓ |
| `v13/code/gen_generality_receipt.json` | `af0c41c573ee` | `af0c41c573ee` | ✓ |

All four match. Review proceeds.

## 0.1 Method and recomputation count

Base G was **rebuilt from the prose of §§2–6** in my own scripts in the session
scratchpad (`r2_base.py`, `r2_check1.py`, `r2_completions.py`,
`r2_general_comp.py`, `r2_mech.py`, `r2_dihedral.py`, `r2_species.py`) — my own
Euler–Rodrigues, my own Householder, my own sparse exact linear algebra, my own
supports and node laws, my own four-clause admission predicate, my own graph,
my own reduced-path walker, my own holonomy reader, my own scope generators.
Nothing was imported from `gen_generality_exact.py`; I read the source only to
resolve two conventions the prose leaves implicit (the column convention of
`V = H·Q`, and which link the twisted comparator overwrites), and both are
recorded as such below. Exact `fractions.Fraction` throughout; no float
anywhere in my scripts either.

**Recomputation count: 96 independent recomputations** — 40 reproducing the
paper's own quantities (§1), 5 verifying the external anchors against the NT
terminal receipt, 44 constructing and measuring **alternative completions of
the same preparation vector** (§3), and 7 instrument/AST/arithmetic checks. In
addition the frozen instrument was re-run end-to-end unmutated (170 s, 12
anchors, 27 gates, **0 must-pass failures**) and a delivery-mode run with the
26-mutant census was started; of the mutants it completed, `gauge-subsample`,
`memo-lax` and `id-lax` each exited 1 with the **same falsified-gate list** the
delivered receipt records for them, entry for entry. These are reproducibility
checks only and no finding rests on them.

Interpreter `/opt/homebrew/bin/python3.13`.

---

## 1. What reproduces (the verification ledger)

Every quantity below came out **exactly** on my own instrument, at the first
attempt, with no tuning:

| object | paper | mine |
|---|---|---|
| the pinned $9\times9$ completion $V$, all 81 entries (A03) | §2.3 matrix | identical, 0 mismatches |
| column 0 of $V$ is $\psi$; $V$ exactly orthogonal over $\mathbb{Q}$ | yes | yes |
| $R_0,R_1,R_2$ from the integer quaternions (A01) | §2.2 matrices | identical, 0 mismatches |
| $\psi$: unit, Schmidt rank, exchange-invariance | 3, invariant | 3, invariant |
| declared scope / extension / admitted / admitted-ext | 162 / 216 / 2 / 8 | 162 / 216 / 2 / 8 |
| admitted set is $\{\mathbf 1, W\}$; scope closed; $W = X_S X_P$ | yes | yes |
| legs commute at all 9 rotation pairs (A05); 36 orthogonality cells | yes | yes |
| admission table, all 24 cells × 2 rules | §3 table | identical |
| cells where FULL / REAL draw | 18 / 8 | 18 / 8 |
| links, id-links, cycle rank per setting | 9/3/2 and 13/7/6 | identical |
| reduced paths per setting; total; matched pairs | 422, 16,168; 34,024; 4,972,096 | identical |
| closed paths per setting | 56 / 2,820 | identical |
| P1 non-flat closed paths (all base points) | 0/56 and 1,896/2,820 | identical |
| holonomies not signed permutations, all base points | 600 (GP-E), 820 (GP-F) | 600, 820 |
| based closed paths; dropped at the base point | 8 / 364; 0 | 8 / 364; 0 |
| group order, closure at the bound, abelian, orders | 4, closed, abelian, [1,2] | identical |
| element fixed points $81 / 9 / 45 / 9$ | §6.2 | identical |
| group $= \{\mathbf 1, W, D, WD\}$; $D \neq W, X_S, X_P$ | yes | yes |
| P5 membership, all 4 elements × 4 collections | §6.5 table | identical |
| $X_S, X_P$ outside the 162 and not in the group | yes | yes |
| based class counts at GP-E | 82 / 86 / 90 / 106 | identical |
| single-rule sub-connections, all five rows | §6.3 table | identical |
| REAL-only at GP-E: 10 links, rank 3, 18 closed, $\{\mathbf 1{:}10, D{:}8\}$, max mult 1 | yes | yes |
| $W$ fails to intertwine the prep leg at every setting | yes | yes |
| probes: canonical loop = identity ×6; bigons = $W$ ×6 | §5 | identical |
| negative control: not a signed permutation at GP-A…D | §5 | identical |
| switching group orders $2^9, 2^{13}$; checkpoint $2^{7}$ | 512 / 8192 / 128 | identical |
| the five external anchors A08–A12 | 4; [4,True]; [2,2]; [34024, 4972096]; [18,2] | all five match the NT terminal receipt's own values |
| §7.2 flip-test: group order per setting | 1,1,1,1,1,1 | identical |
| §7.2 flip-test: id links per setting | 3/3/3/3/5/5 | identical |
| §7.2 flip-test: the defect is the identity, 81 fixed | yes | yes |
| exactness: float literals / `float()` calls | 0 / 0 | 0 / 0 |
| falsification census: `never_falsified` at denominator 24 | EMPTY | EMPTY |
| §4 pair-table rows sum to the matched total | — | $1{,}707{,}000 + 3{,}265{,}096 = 4{,}972{,}096$ ✓ both objects |
| §7.1's 85,760 comparisons | 85,760 | $4(512)+2(8192)+6(8192)+2(8192) + 14(128) = 83{,}968 + 1{,}792$ ✓ |
| §8's coordinate census | 9 different / 12 same of 21 | 9 / 12 of 21 |

**Not one number moved.** The instrument is exact, the enumeration is honest,
the disclosures (600/820 non-signed-permutation holonomies; the un-flip-tested
negative control; the analytically-forced switching clause) are real
disclosures and I could not find a hidden one. Everything that follows is about
**sentences, the species definition, and the verdict's scope** — not about the
arithmetic.

---

## 2. K1(a) — the flip-test, verified

Rebuilt independently on the bare Householder $H$ (the declared completion with
$Q$ removed, same first column $\psi$):

| measured | mine |
|---|---|
| Born shadow of the completion exchange-symmetric | **yes** |
| $V$ exchange-**equivariant** ($\sigma V \sigma = V$) | **yes** |
| holonomy group order per setting | **1, 1, 1, 1, 1, 1** |
| the preparation's swap-defect | **the identity**, 81 fixed points |
| identification links per setting | 3 / 3 / 3 / 3 / **5** / **5** |

The flip-test is real, correctly executed, and correctly reported. §7.2's table
is exactly right. **K1(a) passes.**

But the same run answers a question §7.2 does not ask, and the answer matters
for K1(d) — see F2: the 5 links at each symmetric setting are **1 FULL + 4
REAL**, not 0 + 5. The instrument's own receipt already contains this
(`completion_flip_test.admission_counts_per_cell`: `GP-E/t2 {FULL:1, REAL:1}`),
and `cells_where_a_link_is_drawn = 22` — i.e. **14 full-leg identification
links survive the flip**, twelve at the asymmetric settings and two at the
symmetric ones.

---

## 3. K1(b) — the completion-dependence map

### 3.1 A structural law for the defect (a construction this round contributes)

$U_{\text{prep}} = V \otimes I_9$ and $P_W = \sigma_S \otimes \sigma_P$ with
$\sigma_P^2 = 1$, so the pointer factor cancels identically and

$$D \;=\; P_W\,U_{\text{prep}}^{-1}\,P_W\,U_{\text{prep}} \;=\; \bigl(\sigma\,V^{\mathsf T}\sigma\,V\bigr)\otimes I_9 \;=\; (\sigma V\sigma)^{-1}V \otimes I_9 .$$

Verified exactly against the enumeration on both completions and on 13 others.
Three consequences follow, and each is measured:

1. **$D$ is a function of the completion alone.** It does not depend on the
   measurement family, the settings, the frames, the checkpoints, the scopes or
   the gluing rules. It is the completion's failure to commute with the system
   exchange, and nothing else.
2. **$D = \mathbf 1$ iff $V$ is exchange-equivariant.** The bare Householder
   built from an exchange-invariant $\psi$ is equivariant, so the flip-test's
   null is forced by algebra — it is the equivariant point of the completion
   family, not a generic alternative.
3. **$\sigma D \sigma = D^{-1}$**, hence $W D W^{-1} = D^{-1}$: $W$ and $D$
   commute **iff** $D$ is an involution.

For the natural declared subfamily $V = H\!\cdot\!M$ ($M$ a permutation of the
nine system-pair labels fixing $(0,0)$, so column 0 is the **same** $\psi$ in
every member), the law specialises to $D = (\sigma M \sigma)^{-1}M$, and
$|H|^2$ is measured to have nine distinct columns, so within that family
*Born-symmetric $\iff$ $M$ commutes with $\sigma$ $\iff$ $D = \mathbf 1$*.

### 3.2 The census

I built the **complete** family of $8! = 40{,}320$ permutation completions of
the same $\psi$ and computed $\mathrm{ord}(D)$ for every one:

| $\mathrm{ord}(D)$ | completions | share | holonomy group | $D$ outside the declared 162 |
|---|---|---|---|---|
| 1 | 96 | 0.238% | order 2 (trivial geometry) | 0 of 96 |
| **2** | **1,440** | **3.571%** | **order 4 — the Klein four-group** | 1,440 of 1,440 |
| 3 | 4,224 | 10.476% | order 6 | all |
| 4 | 4,608 | 11.429% | order 8 | all |
| 5 | 4,608 | 11.429% | order 10 | all |
| 6 | 6,912 | 17.143% | order 12 | all |
| 7 | 9,216 | 22.857% | order 14 | all |
| 15 | 9,216 | 22.857% | order 30 | all |

The group column is not extrapolated. I ran the **full path enumeration** at
GP-E on completions with $\mathrm{ord}(D) = 2, 3, 5, 7$ and measured the group
to be $\langle W, D\rangle$ of order $2\,\mathrm{ord}(D)$ in every case, with
$WDW = D^{-1}$ measured, abelian exactly when $\mathrm{ord}(D)\le 2$:

| completion | $\mathrm{ord}(D)$ | $|{\rm grp}|$ | $\langle W,D\rangle = $ grp | $WDW = D^{-1}$ | value set closed at $L_{\max}$ |
|---|---|---|---|---|---|
| $M=(1\,2)$ **the declared $Q$** | 2 | 4 | yes | yes | **yes** |
| $M=(2\,5)$ | 2 | 4 | yes | yes | yes |
| $M=(1\,4)$ | 3 | 6 | yes | yes | yes |
| $M=(1\,2\,4)$ | 5 | 10 | yes | yes | **no** |
| $M=(1\,2\,5)(3\,4)$ | 7 | 14 | yes | yes | **no** |

Outside the permutation family the picture is thinner still. Seven exactly
orthogonal rational completions of the same $\psi$ built from Givens rotations
at the 3-4-5 and 5-12-13 angles (the unit's own rational-angle stock) give a
defect that is **not a signed permutation at all**, and at GP-E **206 of the
364** based closed paths then carry a holonomy the unit's invariant cannot
read; the permutation-valued group collapses to $\{\mathbf 1, W\}$ and **P4
fails** (the defect is not an element because it is not an element of anything
the invariant sees). One of them, $V = H\cdot G(2,6)$, is Born-**symmetric**
with a **non-trivial** defect — so outside the permutation family the paper's
two symmetry facts come apart.

### 3.3 What the census establishes

- **P1 is generic, and the flip-test's null is the degenerate point.** Geometry
  is absent on exactly 96 of 40,320 permutation completions — precisely the
  centraliser of the exchange. This is a *positive* result for the unit and it
  is stronger than anything the paper claims: the bare Householder is not a
  representative alternative, it is the symmetry-degenerate one.
- **P2's Klein four-group is not generic.** Holding $\psi$, the rotations, the
  family, the frames, both gluing rules and both scopes fixed, and moving only
  the free completion, the group takes the values $2,4,6,8,10,12,14,30$. Klein
  four is a **3.571%** event over the whole permutation family, and 12 of 28
  (42.9%) even within the "smallest possible" reference class of single
  transpositions — the other 12 give the dihedral group of order 6 and 4 give
  the trivial one.
- **P3, P4, P5 are robust within the permutation family** — $D$ is a generator
  by construction, and $D$ lies outside the declared 162-element scope in
  **40,224 of 40,224** geometry-bearing cases.

---

## 4. K1(c) — the decision

**`GEN-STRUCTURE-REPRODUCES` unqualified is not the honest verdict.
`GEN-STRUCTURE-REPRODUCES-AT-DECLARED-COMPLETION` is.**

The argument is the programme's own rules, not my taste.

1. **The completion is declared arena data.** The pin says so in terms: "a
   DIFFERENT preparation with its completion DECLARED EXPLICITLY as data (the
   completion-relativity lesson: no silent orthogonal completions — *the
   completion is part of the arena declaration*)".
2. **RUNBOOK §15 then binds.** "Claims of physical significance are entered
   only for quantities GATED as invariant across the unit's admissible arenas;
   arena-artifacts may serve as instruments but never as conclusions." The
   *existence* of the geometry is measured **not** invariant across the
   admissible arenas (§7.2: order 1 at every setting), and the *isomorphism
   type* is measured to take eight different values across them (§3.2). Both
   the P1 headline and the Klein-four headline are therefore entered at a
   declared arena, and the arena must be named where the claim is made.
3. **The vocabulary permits it.** RUNBOOK §10: "Unit verdicts: pre-registered
   names only, **of the form `UNIT-OUTCOME(-QUALIFIER)`**". The outcome name is
   pre-registered; the qualifier states scope. The pin's own
   `GEN-STRUCTURE-VARIES-⟨list⟩` shows the bracket slot is intended. No verdict
   is invented, and the pin's prohibition ("the worker may not invent a verdict
   name") is not engaged.
4. **The paper already knows this and says it in the wrong place.** §10.3: "The
   completion is a declaration, and it is load-bearing… Every result here
   stands at the declared completion." But the verdict line at §9 carries three
   scope clauses — "at the committed finite scope, at the declared admission
   scope, per coordinate" — and the completion, the one parameter that flips
   the outcome to another **pre-registered verdict**, is the one omitted. A
   verdict whose scope list omits its only outcome-flipping parameter is not
   scoped.

Is the existence of geometry therefore "arena-relative"? **Yes as a matter of
logic, and the census says how much.** It is relative to a declaration; but the
locus on which it fails is the exchange-equivariant one, of relative size
$96/40{,}320$. That is the honest pair of sentences, and it is stronger for the
unit than what the paper currently writes, because it converts a bare
scope-caveat into a measured genericity statement.

---

## 5. K1(d) — D2's honesty

**D2 does not survive.** Two independent attacks, both decided by the unit's
own committed data.

**(i) The alternative base IS of the declared species.** The species has four
clauses in the pin ("two wings, a preparation, commuting local legs, records at
the final division event"), the same four in §1, and the same four in the
instrument's own must-pass `GEN-SPECIES` gate (locality + commuting legs;
preparation common to both frames, orthogonal, entangled; projector⊗shift
decomposition with an injective shift; exact orthogonality everywhere). I
re-measured **all four on the bare-Householder base**: locality ✓, commuting at
all 9 rotation pairs ✓, preparation common to both frames and orthogonal with
Schmidt rank 3 ✓, projector⊗shift decomposition with injective shift ✓, all 36
declared operators exactly orthogonal ✓. Not one clause of the species mentions
admission, and not one of them can, because the completion enters none of them.
So D2's "The declared completion $V = H\cdot Q$ satisfies the species
requirement; the bare Householder does not" is **false at the unit's own
criterion**.

**(ii) Repairing D2 by adding the clause would violate the pin's own
No-smuggling gate.** To make D2 true one must add to "the species" a clause
like *the full-leg rule must admit uniquely*. RUNBOOK §2's four-gate rule
requires of every newly introduced object that "the definition must not contain
what it is meant to explain", and §10.7 declares the species to be exactly such
an object ("The species is a declaration of this unit"). A species clause
demanding unique admission **contains source (i) of the curvature** — the
identification multiplicity of §6.3 is nothing but the difference between the
two rules' admissions. Defining the species so that only geometry-bearing
completions are "of the species", and then reporting that the species bears
geometry, is the circularity the rule exists to forbid.

So the answer to K1(d) as posed — legitimate scoping or verdict-steering? — is:
**neither, as currently written; it is a scoping move whose stated ground is
false.** The choice itself is defensible and easy to defend honestly: the
census of §3.2 shows the declared completion is *generic* and the alternative
*degenerate*. What is not defensible is the sentence that presents a free
choice as a species requirement. The repair is to say what happened.

---

## 6. K3 — the steering audit and the cross-base sentence

**Which choices were forced.** (a) The two wings must be **isomorphic**, else
the wing exchange does not exist and every pattern is unposable. The pin's
illustrative phrase — "different wing dimensions (one wing enlarged, e.g.
qutrit-or-higher system side or enlarged pointer side)" — reads either as
"enlarge one of the two wings" or as "enlarge one side, system or pointer". On
the first reading it would have produced `GEN-BLOCKED-AT-⟨the wing exchange⟩`;
the unit took the second and enlarged both sides of both wings. That is the
right call, but it is an undisclosed constraint on what a second base may be,
and it belongs in §10 rather than in a reviewer's note. (b) $\psi$'s Born shadow
must be exchange-invariant, else $W$ is excluded at the outset — the paper
states this and gates it. (c) The family must contain at least one symmetric
setting, else P1 is vacuous — the paper states this.

**Which were free, and what they decide.** The completion decides
**everything**: whether there is geometry, and which group. The measurement
family decides **nothing**: I added a symmetric setting at $(R_2,R_2)$ and one
at a fresh integer quaternion $(4,1,2,0)$ and measured group order 4 with class
counts 106/90/86/82 at all four symmetric settings — the group at a symmetric
setting is independent of which rotation the two wings share. With it, the
"arithmetic is the rationals" coordinate is also inert for the headline.

This bears directly on §8's warrant. Of the nine coordinates measured
different, **seven are inert** for the result (carrier size, system dimension,
outcome count, arithmetic, Schmidt rank, scope size, and the derived
defect-name row); the two that carry it are $\psi$'s symmetry type (posability)
and the completion (everything else). §8's closing — "The differences are the
flesh; the agreements are the geometry" — is a good sentence attached to a
census that does not support it at that strength.

**The cross-base sentence.** §9: "The pattern is the theory's; the elements are
the base's." The evidence does not carry it. What varies across the free
completion at **one and the same base** is not only the elements but the
**group**: $\mathbb{Z}_2$, $K_4$, $D_3$, $D_4$, $D_5$, $D_6$, $D_7$, $D_{15}$.
What *is* invariant across the whole permutation family, and what both bases
instantiate, is a **presentation**:

$$\text{Hol} \;=\; \langle\, W,\, D \;\mid\; W^2 = D^{\,n} = 1,\; WDW = D^{-1} \,\rangle,\qquad n = \mathrm{ord}(D),$$

with $W$ the wing exchange the base admits, $D$ the preparation's swap-defect,
and both bases the case $n = 2$. That is a cross-base pattern, it is measured,
and it is the level at which the unit's own evidence speaks. Stated there, the
finding survives; stated as "it is the Klein four-group", it is an
arena-artifact promoted to a conclusion, which §15 forbids in terms.

**On D5.** D5's claim that the agreeing path counts and class counts are
combinatorial is **correct**, and I strengthened it rather than broke it: every
Klein-four completion I built ($M = (1\,2), (1\,5), (2\,5), (1\,2)(5\,7)$)
returns the same 82/86/90/106, and base G's realized-rule sub-connection
(10 links, rank 3, 18 closed, $\{\mathbf 1{:}10, X{:}8\}$) matches the NT
receipt's SP-E/REAL row entry for entry. The shared graph is itself forced by
the shared species plus a geometry-bearing completion, which is worth one more
clause but changes nothing D5 says.

---

## 7. K2, K4, K5 at the protocol's lower depth

**K2.** Everything recomputed; see §1. On the specific asks: the 1,896/2,820
and 0/56 both-ways gate is genuine and reproduces; the Klein four is closed
under composition at the bound as claimed, counted by tuples on my own
instrument. **What $D$ is structurally** — the protocol's open question — is
answered in §3.1: $D = (\sigma V^{\mathsf T}\sigma V)\otimes I_9$, the
completion's exchange defect, acting **only on the system pair** and trivially
on the pointer pair; its 45 fixed configurations are $5\times 9$, the five
system-pair labels fixed by $(1\,2)(3\,6)$ times the nine untouched pointer
pairs. That is why it is neither half of $W$ (each half moves one of the two
pairs wholesale) and why it commutes with $W$ exactly because it is an
involution. The admitted set being only $\{\mathbf 1, W\}$ does **not**
trivialise P5: the escaping elements $D, WD$ are outside the 162 and the 216 as
well, and I measured the escape to hold for all 40,224 geometry-bearing
completions.

**K4.** The $9\times9$ completion verified entry by entry against the paper's
printed matrix (0 mismatches) and derived independently from
$H = I - ww^{\mathsf T}$, $w = \psi - e_{(0,0)}$, $w\!\cdot\!w = 2$; exact
orthogonality over $\mathbb{Q}$ confirmed for $V$ and for all 36 declared
(setting, frame) legs; the pointer shift is injective and the projector⊗shift
decomposition holds; 162/216/2/8, 512/8192/128, 34,024 and 4,972,096 all
recomputed. **No defect found in the base declaration.**

**K5.** AST sweep: **0** float literals, **0** `float()` calls — confirmed
independently. Census: `never_falsified` is EMPTY at denominator 24, and
`GEN-VOCABULARY` is correctly named as the one gate carried only by a waiver.
The 85,760 decomposes exactly as $83{,}968 + 1{,}792$. The direction flip-test's
14 loops match the declared-probe count exactly, and the negative control's
exclusion is disclosed. Two small things are recorded as F9 and F10. D3's
omission of the composition defect is pin-compliant: the five patterns live at
the amplitude layer and no result rests on it.

---

## 8. Findings

### F1 — MAJOR. D2's "species requirement" is false at the unit's own species gate, and repairing it would smuggle the conclusion into the definition.

**Evidence.** §5 above: all four measured clauses of `GEN-SPECIES` hold on the
bare-Householder base. The pin, §1 and the gate agree on the four clauses; none
mentions admission. Adding an admission-uniqueness clause would place source
(i) of the curvature inside the definition of the species, against the
four-gate rule's No-smuggling clause with §10.7 declaring the species a
declaration of this unit.

**Repair.** Replace D2's second and fourth sentences with:

> The alternative completion is measured to satisfy every clause of the
> declared species — the four clauses of §1 hold on it entry for entry — so the
> choice between them is not a species question. It is a free declaration, and
> the unit declares the geometry-bearing one: the exchange-equivariant
> completions form the degenerate locus of the completion family, on which the
> preparation manufactures no defect and every loop is flat. The choice is
> disclosed as a choice, its alternative is rebuilt and measured (§7.2), and
> every verdict is scoped to the declared completion.

### F2 — MAJOR. The flip-test's stated mechanism is wrong, and the unit's own receipt contains the refutation.

**Evidence.** D2: "such a base has no full-leg identifications and no canonical
loop, and the five patterns cannot be posed on it at all." §2.3: "That single
declared choice is what makes the base's full-leg identifications exist at
all." Measured, by me and by the delivered receipt
(`completion_flip_test.admission_counts_per_cell`, `cells_where_a_link_is_drawn
= 22`): at the alternative completion the FULL rule still draws **14**
identification links — three at each of GP-A…GP-D at $t = 0,1,3$ carrying the
identity, and one at each of GP-E, GP-F at $t = 2$ carrying the wing exchange.
The **declared canonical loop exists unchanged at all four asymmetric
settings**. And the five patterns are not unposable: §7.2 poses P1 and P2 on
the alternative and measures group order 1 — that is the pre-registered outcome
`GEN-STRUCTURE-ABSENT`, computed, not blocked.

What actually vanishes is different and cleaner: at the bare Householder $W$
**intertwines the preparation leg at every setting** (measured false at all six
settings for the declared completion, true at all six for the alternative), so
at the symmetric settings $W$ intertwines the whole leg sequence and every
loop, by whichever rule its links are drawn, is flat. The operative property is
the completion's exchange-**equivariance**, not the FULL rule's refusal;
Born-symmetry and equivariance happen to coincide on the permutation family and
come apart outside it ($V = H\cdot G(2,6)$: Born-symmetric, defect non-trivial).

**Repair.** Replace §2.3's "That single declared choice is what makes the
full-leg gluing rule of §3 admit **one** permutation rather than two, and hence
what makes the base's full-leg identifications exist at all" with:

> That single declared choice is what makes the full-leg rule admit one
> permutation rather than two at the two symmetric settings, where the wing
> exchange would otherwise compete; at the four asymmetric settings the full
> rule's identifications do not depend on it. Its deeper role is measured in
> §7.2: an exchange-equivariant completion makes the wing exchange intertwine
> the preparation leg, and with it the whole leg sequence, so that every loop
> is flat.

and replace D2's first sentence with:

> The completion was chosen to be geometry-bearing, and the alternative is
> rebuilt in full and measured rather than hidden. At the bare Householder the
> wing exchange intertwines the preparation leg at every setting, so the
> preparation manufactures no defect; the full-leg rule then admits two
> permutations at the symmetric settings where it had admitted one, and draws
> the wing exchange at $t = 2$ instead. Fourteen full-leg identifications
> survive, the canonical loop survives at the four asymmetric settings, and the
> five patterns are posed on that base and measured: the holonomy group has
> order 1 at every setting, which is the pre-registered outcome
> `GEN-STRUCTURE-ABSENT`.

### F3 — MAJOR. The verdict omits the one declared parameter that flips it; §15 makes the qualifier mandatory.

**Evidence and argument.** §4 above. The verdict's scope list names three
scopes and omits the completion, while §10.3 concedes the completion is
load-bearing and §7.2 measures that a different declared completion of the same
$\psi$ yields a different pre-registered outcome.

One more piece of evidence, from the instrument's own census: the mutant
`completion-Q` **is** the alternative completion, and the receipt records it
killing `GEN-BASE-PINNED`, `GEN-COMPLETION-IS-LOAD-BEARING`,
`GEN-ADMISSION-TABLE`, both controls, `GEN-P1-NONTRIVIAL-HOLONOMY`,
`GEN-P3`, `GEN-P4`, `GEN-P5` and `GEN-COMPARISON`. The same object is a
*declared admissible alternative arena* in §7.2 and a *must-die mutant* in §11.
Both roles are defensible — it dies first at the pinned-matrix anchor, which is
the intended constructor-drift test — but a unit in which changing one declared
arena coordinate falsifies four of its five pattern gates has, by its own
instrument, measured that coordinate into the verdict's scope.

**Repair.** Set the verdict to

> **`GEN-STRUCTURE-REPRODUCES-AT-DECLARED-COMPLETION`**, at the committed
> finite scope, at the declared admission scope, at the declared completion,
> per coordinate.

and add, immediately after it:

> The qualifier is not decoration. The completion is declared arena data by the
> pin's own terms, and at another declared orthogonal completion of the very
> same preparation vector — the exchange-equivariant one — the same five gates
> return `GEN-STRUCTURE-ABSENT`. What the unit measures is that the geometry
> exists at the declared completion and is absent exactly on the equivariant
> locus of the completion family.

### F4 — MAJOR. "The pattern is the theory's; the elements are the base's" is refuted by holding the base fixed and moving only the completion.

**Evidence.** §3.2: complete census of the $8!$ permutation completions of the
same $\psi$; group order $2\,\mathrm{ord}(D)$ with the eight measured values
$2,4,6,8,10,12,14,30$; Klein four at 3.571%; full path enumeration confirming
orders 4, 6, 10, 14 at $\mathrm{ord}(D)=2,3,5,7$ with
$\langle W,D\rangle$ = the group and $WDW = D^{-1}$ in every case. The
abstract's own last two clauses contradict each other: "rebuilt on the bare
Householder … the geometry vanishes. … the geometry is a property of the
species" — the bare-Householder base *is* of the species (F1).

**Repair.** Replace the abstract's "The group is a function of the base's
declared data, completion included; the geometry is a property of the species"
with:

> The group is a function of the base's declared data, completion included: the
> geometry is a property of the species **together with a geometry-bearing
> completion**, and the completions that bear none are the exchange-equivariant
> ones.

and replace §9's "The pattern is the theory's; the elements are the base's"
with:

> What recurs across the two bases is the presentation — a wing exchange the
> base admits, a preparation defect it does not, and the relation
> $W D W = D^{-1}$ that makes them generate a dihedral group of order twice the
> defect's order. Both bases realise the case where the defect is an involution
> and the group is the Klein four-group. The isomorphism type is a function of
> the declared completion and is not claimed to be a property of the theory.

### F5 — MAJOR. Seven of §8's nine "measured different" coordinates are inert for the result.

**Evidence.** §6 above: the holonomy group at a symmetric setting is
independent of the shared rotation — measured at $(R_0,R_0)$, $(R_1,R_1)$,
$(R_2,R_2)$ and at a fresh integer quaternion $(4,1,2,0)$, group order 4 and
class counts 106/90/86/82 in all four. $D$ depends on the completion alone
(§3.1). The carrier size, outcome count and Schmidt rank enter only the
fixed-point labels.

**Repair.** Add to §8, after the 9/12 count:

> Of the nine differing coordinates, two do the work: the preparation's
> symmetry type, which decides whether the wing exchange can be a co-reference
> at all, and the declared completion, which decides the defect and with it the
> group. The measurement family is measured inert — the holonomy group at a
> symmetric setting is the same for every shared rotation — and the remaining
> coordinates enter the elements' fixed-point counts and nothing else. The
> agreements are therefore evidence that the two bases share a mechanism, not
> that they share it despite nine independent differences.

Add to §10 a new non-claim:

> **The two wings must be isomorphic.** A base with wings of different
> dimensions has no wing exchange and none of the five patterns can be posed on
> it; the second base enlarges both wings for that reason.

### F6 — MINOR. P5's significance is a function of the declared scope's size, and should say so.

Measured: $D$ lies outside the declared 162 in **40,224 of 40,224**
geometry-bearing permutation completions. The escape is real and robust — but
the declared scope is a 162-element group inside $S_{81}$, generated only by
cyclic relabellings and a wing flag, so a defect that is a non-cyclic
permutation of the nine system-pair labels can scarcely lie in it. Add one
clause to §6.5: "the escape is robust — measured for every geometry-bearing
completion of this preparation — and its strength is bounded by how small the
declared scope is; the scope is a declaration and a wider one is searched in
§7.3."

### F7 — MINOR. D4's closure at the bound is itself completion-contingent.

At $\mathrm{ord}(D) = 5$ and $7$ the value set at the same $L_{\max} = 8$ is
measured **not** closed while the group is order 10 and 14. D4 and §10.6 are
correct as written; they deserve the added clause that the measured closure is
a fact about the involutive case and not about the construction.

### F8 — MINOR. The negative control has teeth only at the four flat settings.

Rebuilt as declared (the $t = 3$ full-leg link overwritten by $W$ in place):
not a signed permutation at GP-A…GP-D, and at GP-E, GP-F the value is exactly
$W\!\cdot\!D$ — an **element of the genuine holonomy group**. §5 is correctly
scoped ("the flatness readings above are therefore not vacuous"), but the
table's cell should read "$W\!\cdot\!D$, an element of the group — so the
control does not discriminate at the two settings whose loops are already
non-flat".

### F9 — NOTE. The no-mutant-exemption sweep counts a narrower pattern than the addendum states.

The gate counts `ast.NotEq` comparisons touching `MUTANT` and measures zero; my
sweep confirms zero, and finds one `MUTANT not in MUTANTS` (`ast.NotIn`, line
3491) in `main()`'s CLI validation — outside any gate and incapable of
exempting one — plus 29 `MUTANT == "…"` guards, all at computation sites, and
exactly two `gate()` calls whose arguments mention `MUTANT` (the exemption
gate's own injection and the census gate). The §14 addendum's principle is met.
Widen the swept pattern to `NotEq | NotIn` so the claim and the measurement
coincide.

### F10 — NOTE. `exempt-lax` is counted as a computation mutant but injects into the gate's own evidence list.

It appends a synthetic line number to `found` rather than introducing a real
`MUTANT != …` comparison into the source, so it tests that the predicate
carries the exit code, not that the sweep would find a real exemption. Either
reclassify it with the three waivers or state what it does, exactly as the
paper already does for the waiver denominator.

---

## 9. What I attacked and could not break

- Every number in §§2–8, and the five external anchors against the NT terminal
  receipt. **No false number, no arithmetic defect, no circular gate.**
- The flip-test itself: real, correctly executed, correctly tabulated.
- P1's both-ways gate, the admission table, the path space, the class counts,
  the sub-connection isolation of source (ii), the read-time coordinate, the
  85,760 decomposition, the census honesty (`never_falsified` EMPTY at 24 with
  the waiver-carried gate named), exactness (0 floats).
- D3 and D5 — both correct as written; D5 I strengthened.
- The genericity of the declared completion, which the paper does not claim but
  is entitled to: it is the alternative, not the declared one, that is special.

---

## 10. Grade

The instrument is exact and the enumeration is honest; a full independent
rebuild from the prose reproduced every committed quantity of this unit at the
first attempt, and the five external anchors match the first base's terminal
receipt. Nothing here is a numerical failure.

What fails is the sentence layer at exactly the place the protocol pre-named as
hardest. The completion is a **free declaration** that decides whether there is
any geometry and which group there is; the paper knows this, measures it,
discloses it in §10.3 — and then omits it from the verdict's scope list,
justifies the choice by a **species requirement its own species gate refutes**,
and states a mechanism for the flip-test that its **own receipt table
contradicts**. The repairs are bounded: four sentences, one verdict qualifier,
one added census. None requires new physics, and the census this round
contributes ($D = (\sigma V^{\mathsf T}\sigma V)\otimes I_9$; the dihedral
presentation; the 40,320-completion sweep) makes the unit's position stronger
than the one it currently argues — the declared completion is generic, and the
flip-test's null is the symmetry-degenerate point.

> **ACCEPT-WITH-FIXES.**
>
> Blocking: **F1** (withdraw D2's species claim; say the choice was a choice),
> **F2** (correct the flip-test mechanism in §2.3 and D2 against the receipt's
> own per-cell table), **F3** (verdict →
> `GEN-STRUCTURE-REPRODUCES-AT-DECLARED-COMPLETION`, with the alternative's
> pre-registered outcome named at the verdict), **F4** (withdraw "the pattern
> is the theory's" and the abstract's "property of the species"; state the
> dihedral presentation as the cross-base invariant and report the completion
> census).
>
> Non-blocking but recommended before terminal: **F5**–**F10**.
>
> The completion census of §3.2 and the defect law of §3.1 are offered to the
> repair as this round's constructions; if adopted they should be gated
> natively and credited as the hostile round's, per RUNBOOK §6.

# GEN — HOSTILE REVIEW R1 (OPERATOR / ALGEBRAIC LENS)

**Reviewer:** R1, operator-system lens.
**Object under review (SHA-256 verified before reading):**

| artifact | sha256-12 declared | sha256-12 measured | match |
|---|---|---|---|
| `v13/paper-gen-generality-check.md` | `4baf4e22c1aa` | `4baf4e22c1aa` | yes |
| `v13/code/gen_generality_exact.py` | `78baf5eb3ef6` | `78baf5eb3ef6` | yes |
| `v13/code/gen_generality_output.txt` | `9dc0ff7ed387` | `9dc0ff7ed387` | yes |
| `v13/code/gen_generality_receipt.json` | `af0c41c573ee` | `af0c41c573ee` | yes |

The receipt's own `source_sha256` field also matches the frozen instrument byte
for byte (`78baf5eb3ef6cc0f…`), and its `pin_sha256_prefix` / `pin_commit` /
`base_commit` are `0da6205815a6` / `5e8bc58` / `fceb614` as the protocol states.

**Method.** I built an independent instrument in
`/private/tmp/.../scratchpad/` (`r1_base.py`, `r1_core.py`, `r1_k4.py`,
`r1_hol.py`, `r1_p3p5.py`, `r1_pairs.py`, `r1_d5.py`, `r1_sweep.py`) from the
paper's §2 base declaration and §3 rule prose, with the four-clause predicate's
precise form read from the frozen source and then **re-implemented**, not
called. No function, constant or fixture of `gen_generality_exact.py` is
imported anywhere in my instrument. Every count below is my own. Separately,
and only as a reproduction check, I copied the frozen instrument into a clean
scratch directory and ran it there (§ "Reproduction", last).

**Recomputation count: 587 paper-stated quantities recomputed independently,
0 mismatches.** In addition I performed **44,545 model evaluations the unit does
not carry** (a 40,320-point complete completion sweep, a 28-point complete
sub-family sweep with full holonomy, a 101-point systematic sample, and a
4,096-point connection sweep), which produced the three MAJOR findings below.

---

## 0. Summary

Every number in this paper is right. I could not move a single one. The
81-entry completion matrix, the 27 rotation entries, 162/216/2/8,
512/8192/128, the 18/8 admission split, 34,024, 4,972,096, the eight
pair-table cells, 1,896-of-2,820, 0-of-56, 600/820, 364, 82/86/90/106, the
eighteen sub-connection rows, 45 fixed points, the sixteen P5 cells, the
twenty-two census cells and 85,760 all reproduce exactly on an instrument that
shares no code with the delivered one.

What I can move is the **meaning** of the headline. The unit's sharpest claim
is that the Klein four-group *reproduces* on a base with none of the first
base's flesh. I measured the family of alternative completions of the *same*
preparation vector and found that the isomorphism type of the holonomy group is
**selected by the declared completion**: within the pinned completion's own
declared form (a single basis transposition), 12 of 28 choices give the Klein
four-group and 12 give the **non-abelian group of order 6**; over the wider
permutation family only 2 of 101 sampled choices give Klein-four, with orders up
to 30 observed. The completion flip-test the unit does carry looks only at the
one alternative on which the geometry *vanishes* — which my complete sweep shows
is the rare case (96 of 40,320), not the representative one. The paper's own
defence of that choice (D2) is, moreover, factually wrong about the base it
tested. And D5's claim that the cross-base class-count agreement is
"combinatorial" is refuted by direct enumeration: only 96 of 4,096 Klein
connections on that graph reproduce the profile.

None of this falsifies a gate or the verdict — the pin's P2 explicitly does not
require Klein-four, so `GEN-STRUCTURE-REPRODUCES` follows from the
pre-registered decision rule on gates that genuinely pass. It does mean the
paper's interpretive frame, its scope statement, and two of its eight deviations
must change. **Grade: ACCEPT-WITH-FIXES.**

---

## 1. K4 — THE BASE DECLARATION (primary weight)

I rebuilt every declared object from §2 with my own constructors and compared
against the matrices *printed in the paper* (not against the instrument's
`PINNED_*` tables, which is a different and weaker check).

### 1.1 Entry-by-entry

| checked | my result |
|---|---|
| $R_0,R_1,R_2$ from the quaternions $(1,0,0,0),(2,1,0,0),(3,0,0,2)$ by my own Euler–Rodrigues, vs the 27 entries printed in §2.2 | **27/27 identical, 0 mismatches** |
| the $9\times9$ completion $V=H\cdot Q$ built from my own Householder and transposition, vs the 81 entries printed in §2.3 | **81/81 identical, 0 mismatches** |
| $V$ column 0 $=\psi$ | yes |
| exact orthogonality over $\mathbb{Q}$: $R_0,R_1,R_2$, $H$, $V$ | 5/5 exact |
| $H$ symmetric, $H$ col 0 $=\psi$, $w^{\mathsf T}w = 2$ | all confirmed |

The paper's arithmetic here is clean. I also confirm the "two different planes"
claim structurally: $R_1$ fixes axis 0 and $R_2$ fixes axis 2, so the family is
not one plane rotation with a spectator.

### 1.2 The preparation

$\psi$ is a unit vector; its coefficient matrix is symmetric (exchange-invariant,
confirmed); $MM^{\mathsf T}$ is diagonal with entries $4/9,4/9,1/9$, so the
**Schmidt rank is 3** with coefficients $(2/3,2/3,1/3)$ — exactly as declared.

### 1.3 Operators, orthogonality, record, commutation

| checked | my result |
|---|---|
| $U_{\text{prep}}$, $U_A(R_g)$, $U_B(R_g)$ exactly orthogonal over $\mathbb{Q}$ | 7/7 exact |
| every declared leg orthogonal at every (setting, frame) | 12/12 cells |
| $U_X(g)=\sum_o \Pi^g_o\otimes\mathrm{Sh}^{\,o}$ entry by entry, built by an independent Kronecker route | 6/6 operators identical |
| projector columns orthonormal | 3 rotations, all exact |
| the pointer-shift map injective; the record from the ready state bijective | both yes |
| the two wings commute at every declared pair of rotations | **9/9 pairs** |

The injective-pointer-shift record claim is correct as stated. I note for the
record that orthogonality of $U_X(g)$ does **not** test injectivity —
$U^{\mathsf T}U=\sum_o\Pi_o\otimes I=I$ holds for any shift map, injective or
not — so `A06` is carrying real independent weight and is not redundant with
`A04`. Good.

### 1.4 Scope computations

| quantity | paper | mine |
|---|---|---|
| declared relabelling scope, generated | 162 | **162** |
| … after deduplication | 162 | **162** |
| declared extension scope | 216 | **216** |
| admitted after the $j_0$ filter | 2 | **2**, and it is exactly $\{\mathbf 1, W\}$ |
| admitted at the extension | 8 | **8** |
| switching group per setting | 512 / 8192 | **512 / 8192** |
| checkpoint subgroup | 128 | **128** |
| $W = X_S\cdot X_P$ | measured | confirmed both orders |
| $X_S, X_P$ in the declared 162 | no | **no** (§6.5's remark is right) |
| the 162 closed under composition | yes | **yes** |

### 1.5 Path space

| quantity | paper | mine |
|---|---|---|
| nodes / links / id-links / cycle rank, GP-A…GP-D | 8/9/3/2 | identical |
| nodes / links / id-links / cycle rank, GP-E, GP-F | 8/13/7/6 | identical |
| reduced paths per setting | 422 / 16,168 | identical |
| closed paths per setting | 56 / 2,820 | identical |
| **total reduced paths** | 34,024 | **34,024** |
| **path pairs sharing both endpoints** | 4,972,096 | **4,972,096** |
| FULL draws / REAL draws | 18 / 8 | **18 / 8** |
| leg-prefix alignment profile, 18 cells | aligned at $t{=}1,3$; divergent at $t{=}2$ | identical |
| the full 24-cell × 2-rule admission table | as §3 | identical cell for cell |

### 1.6 K4 finding

**MINOR-11 — the declared 216-element extension scope is not closed under
composition.** §2.5 says "The scope is measured **closed under composition**, so
it is a group and not a list", immediately after the sentence introducing the
extension. I measure the **162 closed** (true) and the **216 not closed**
(false): it is the union of the 162-element group with 72 pointer-transposition
elements, and products leave the union. No result depends on the extension being
a group — membership is a set test — and the paper never explicitly claims it,
but the placement invites the wrong reading. *Repair: one clause naming which
scope the closure measurement covers.*

---

## 2. K2 — THE FIVE PATTERNS (primary weight)

All five recomputed on my own instrument, permutation tuples throughout, never
labels.

### 2.1 P1 — the gate's both-ways claim

| setting | paper | mine |
|---|---|---|
| GP-A…GP-D, non-flat closed paths (all base points) | **0 of 56** | **0 of 56** |
| GP-E, non-flat closed paths | **1,896 of 2,820** | **1,896 of 2,820** |
| GP-F, non-flat closed paths | **1,896 of 2,820** | **1,896 of 2,820** |
| closed paths at the base point, symmetric | 364 | **364** |
| at the base point, holonomies that are not signed permutations | 0 | **0** |
| over all base points, not signed permutations, GP-E / GP-F | 600 / 820 | **600 / 820** |

P1 holds and the gate really does come out both ways on one base. This is the
strongest single piece of anti-fixture evidence in the unit and I want it on the
record as such. The 600/820 disclosure is honest and would have been easy to
suppress.

### 2.2 P2 — the group, by permutation tuples with closure measured

| quantity | paper | mine |
|---|---|---|
| value set size (symmetric settings) | 4 | **4** |
| value set already closed at the bound | yes | **yes** |
| generated group order | 4 | **4** |
| abelian, every element of order dividing 2 | yes | **yes**, orders $\{1,2\}$ |
| fixed configurations: $\mathbf 1$ / $W$ / $D$ / $WD$ | 81 / 9 / 45 / 9 | **81 / 9 / 45 / 9** |
| based class counts | 82 / 86 / 90 / 106 | **82 / 86 / 90 / 106** |
| $D \ne X_S$ (27 fp), $\ne X_P$ (27), $\ne W$ (9) | yes | **yes** |
| GP-A…GP-D group order | 1 | **1** |

The value set at the declared base point is genuinely closed, so the paper is
entitled to call it the group rather than a generating set; D4's caution is
correctly stated.

### 2.3 WHAT $D$ IS, STRUCTURALLY — a closed form the paper does not give

The kill-shot asks what the 45-fixed-point generator actually does. I derived it
and verified the derivation two independent ways (closed form vs direct
$81\times81$ matrix computation, plus a 31-point sample across the permutation
family — 31/31 agreement).

Write $S$ for the system-pair exchange on the 9 system-pair indices, $\sigma =
(1\,3)(2\,6)(5\,7)$ in the §2.3 basis ordering, fixing $0,4,8$. Then:

1. $\psi$ is exchange-**invariant**, so $w=\psi-e_{(0,0)}$ is $S$-invariant, so
   the Householder is exchange-**equivariant**: $S H S = H$ — **measured**.
2. Therefore, for $V = H\cdot Q$ with *any* orthogonal $Q$,
   $$\boxed{\;D \;=\; \bigl(S\,Q^{\mathsf T} S\,Q\bigr)\otimes I_9\;}$$
   The Householder cancels identically. $D$ **does not depend on $\psi$ at all.**
3. For the declared $Q=(1\,2)$ this is $Q'\!\cdot\!Q$ with $Q'=SQS=(3\,6)$ — two
   **disjoint** transpositions of the system-pair basis, fixing $\{0,4,5,7,8\}$,
   five of nine. Tensored with $I_9$ on the pointer pair: $5\times 9 = 45$ fixed
   configurations. **That is where the paper's 45 comes from.**
4. $D$ acts trivially on the pointer pair (measured on all 81 configurations),
   which is why it is neither half of the wing exchange.
5. $D$ is an unsigned permutation (all signs $+1$, measured), order 2.
6. The flip-test result falls out: for $Q=I$ (the bare Householder),
   $D=(S\,I\,S\,I)\otimes I_9 = \mathbf 1$. §7.2's "the identity, 81 fixed
   points" is analytically forced, not a coincidence.
7. In general $D$ is trivial **iff $Q$ commutes with $\sigma$**. Over basis
   permutations that is the centraliser of $\sigma$, of order
   $2^3\cdot 3!\cdot 2! = 96$ — and my complete sweep found exactly **96 of
   40,320**.

**MODERATE-6 — "the preparation's own swap-defect" misnames its own object.**
The paper calls $D$ the preparation's defect and says the completion
"manufactures" it. The second half is exactly right; the first half is not.
$D$ is the exchange-defect of the **declared transposition $Q$** and is
provably independent of the preparation vector. On this base, P4's headline
("the preparation manufactures a generator") is really "the free completion
choice manufactures a generator" — which matters for §3 below. *Repair: print
the closed form; it is two lines and it strengthens §7.2 rather than weakening
it.*

### 2.4 P3 — two curvature sources

All eighteen sub-connection rows recomputed (6 settings × 3 rule subsets),
including links, identification links, connected components, cycle rank, closed
paths at the base point, holonomy classes, generated group order and maximum
identification multiplicity. **Every row identical to §6.3.** In particular:

| row | paper | mine |
|---|---|---|
| GP-E/GP-F, REAL only: links / rank / closed at base | 10 / 3 / **18** | 10 / 3 / **18** |
| … its classes | identity ×10, $D$ ×8 | **identity ×10, $D$ ×8** |
| … its group order, max multiplicity | 2, 1 | **2, 1** |
| GP-A…GP-D, REAL only | 6 links, 0 closed | 6 links, 2 components, rank 0, 0 closed |
| coordinates carrying two admitted maps | 6 | **6** |

The single-rule isolation is sound: at multiplicity exactly one the realized-rule
sub-connection is already non-flat and the element it carries is $D$. The
claim "multiplicity is sufficient and measured not necessary" is earned.

The prep-defect computation reproduces exactly: signed permutation, order 2, 45
fixed points, not the identity, not $W$, not either half. $W$ is measured not to
intertwine the preparation leg at any setting (my 18-cell intertwining table has
4 true entries — legs 2 and 3 at the two symmetric settings — and leg 1 false
everywhere).

### 2.5 P4

$D$ is an element of the group at GP-E and GP-F and is measured **not** an
element at GP-A…GP-D. Confirmed. The second row is what makes the first a
measurement, and the paper is right to say so.

### 2.6 P5 — non-principality, and whether $\{\mathbf 1, W\}$ trivialises it

The sixteen-cell table reproduces exactly: $\mathbf 1$ and $W$ in all four
collections; $D$ and $W\!D$ in none. $X_S$ and $X_P$ also outside all four
(§6.5's "for the record" remark). So the *numbers* are right.

The kill-shot asks whether the tiny admitted group trivialises the claim. My
answer is **it does not trivialise it, but the table is far less independent
than it reads, and one sentence around it is wrong.** Two findings:

**MODERATE-4 — the 16-cell P5 table is one independent measurement plus fifteen
forced cells, and the forcedness is not disclosed.** I measured:

* all four collections are **$W$-invariant** ($W\!\cdot\!S = S$) and contain
  both $\mathbf 1$ and $W$;
* the inclusions $\text{admitted-2}\subseteq 162 \subseteq 216
  \supseteq \text{admitted-8}$ hold.

Consequently the $\mathbf 1$ and $W$ rows are forced "yes" everywhere by
construction (the scope is *generated by* the wing flag); $D\notin 216$ forces
$D\notin 162$, $D\notin$ admitted-2 and $D\notin$ admitted-8; and $W$-invariance
forces the entire $W\!D$ row from the $D$ row. **The whole table reduces to the
single free measurement $D\notin$ the 216-element extension.** §6.5 presents it
as "membership of **every** holonomy element in **every** declared and admitted
collection, computed" and concludes "two of the four … outside the 162, outside
the 216, and outside both admitted sets" — which reads as eight independent
escapes. Under the RUNBOOK §14 addendum ("analytically-forced clauses are
disclosures, not must-pass gates") this belongs beside the §7.1 disclosure, and
it is not there. *Repair: print the $W$-invariance and the inclusions, and name
the one free cell.*

**MODERATE-5 — "Every link of this connection is a transport the base admits"
conflates two senses of "admits".** Measured on the 13 links of a symmetric
setting:

| link kind | in admitted-2 | in the 162 | in the 216 |
|---|---|---|---|
| the 7 identification links ($\mathbf 1$ or $W$) | yes | yes | yes |
| $U_{\text{prep}}$ | — it is **not even a signed permutation** | no | no |
| $U_A(R_0), U_B(R_0)$ | **are** genuine permutations of the 81 configurations, but **no** | **no** | **no** |
| $U_A(R_1), U_A(R_2)$ | not permutations at all | no | no |

So "the group those links generate around loops" is generated in part by
transports that were never in any declared scope. With a structure group of
order 2, the escape is close to structurally forced once anything outside the
scope enters the product. P5 is **not** vacuous — the gate does come out both
ways ($\mathbf 1$ and $W$ inside, $D$ and $W\!D$ outside) — but the quoted
sentence overstates. *Repair: "every **identification** link is a transport the
base admits", plus the leg-membership row above.*

---

## 3. K1 — THE COMPLETION QUESTION (the kill-shot, and where the paper moves)

### 3.1 The flip-test itself: verified

I rebuilt the **entire base** on the bare Householder with my own instrument:

| measured | paper | mine |
|---|---|---|
| Born shadow of the completion exchange-symmetric | yes | **yes** |
| identification links per setting | 3/3/3/3/**5**/**5** | **3/3/3/3/5/5** |
| holonomy group order per setting | 1,1,1,1,1,1 | **1,1,1,1,1,1** |
| the preparation's swap-defect | the identity, 81 fp | **the identity, 81 fp** |

The flip-test is real and its numbers are right.

### 3.2 MAJOR-2 — D2 is factually wrong about the base it tested

D2 says: *"a preparation whose completion has an exchange-symmetric Born shadow
admits two permutations and its links are refused: **such a base has no full-leg
identifications and no canonical loop, and the five patterns cannot be posed on
it at all.**"* This is the paper's defence against the steering charge. I
measured that base's admission table cell by cell:

```
BARE-HOUSEHOLDER base, (FULL, REAL) admitted counts
  GP-A..GP-D   t0 (1,0)   t1 (1,0)   t2 (0,0)   t3 (1,0)
  GP-E, GP-F   t0 (2,1)   t1 (2,1)   t2 (1,1)   t3 (2,1)
```

* The FULL rule **draws at 14 cells** — twelve at the four asymmetric settings
  at $t\in\{0,1,3\}$, plus **one at $t=2$ at each symmetric setting, a link the
  declared base does not have**.
* The **canonical loop exists at four of the six settings** (FULL links at $t=0$
  and $t=3$ both present at GP-A…GP-D).
* The five patterns **are** posed on it — §7.2 poses and answers them (group
  order 1 everywhere, defect the identity). That is a `GEN-STRUCTURE-ABSENT`-shaped
  answer, not an unposable question.

What is true is narrower: at the **two symmetric settings** the FULL rule's
$t\in\{0,1,3\}$ links are refused. §7.2's own prose is correctly hedged; D2
overreaches, and it overreaches in the exact direction that makes the free
choice look forced. *Repair: replace D2's sentence with the measured statement
above; and note in §7.2 the new $t=2$ FULL link (the count 5 already discloses
it numerically, the prose does not — **MINOR-12**).*

### 3.3 MAJOR-1 — the completion selects the *group*, and the sweep the protocol asked for was not done

K1 asks: *"sweep completions of $\psi$ (as feasible, declared) — is the pinned
completion generic or special among geometry-bearing ones?"* The unit does not
do this. I did.

**Declared family (mine).** $V = H\cdot P_q$ where $P_q$ is a permutation of the
nine system-pair basis vectors fixing $e_{(0,0)}$, i.e. $q\in \mathrm{Sym}\{1..8\}$,
$8! = 40{,}320$ completions. This family is the natural one: it contains the
pinned $V$ ($q$ = the transposition $(1\,2)$) **and** the bare Householder
($q = \mathrm{id}$), so both of the paper's own completions live in it.

**Tier 1 — complete, all 40,320 (defect by exact algebra, form verified against
direct matrix computation on 31 samples, 31/31):**

| defect fixed points (of 81) | 9 | 18 | 27 | 36 | **45** | 54 | 81 |
|---|---|---|---|---|---|---|---|
| completions | 16,704 | 11,520 | 5,376 | 4,608 | **864** | 1,152 | **96** |

Only **96 of 40,320** (0.24%) give a trivial defect — exactly the centraliser of
$\sigma$, as the closed form predicts. **The bare Householder the paper tests is
one of those 96.** The overwhelmingly typical completion carries a defect.

**Tier 2 — complete, all 28 transpositions (the pinned completion's own declared
form), each a full six-setting rebuild with full holonomy:**

| outcome | count of 28 | which |
|---|---|---|
| flat at every setting (group order 1) | **4** | exactly $(1\,3),(2\,6),(5\,7),(4\,8)$ — the transpositions commuting with $\sigma$ |
| **the Klein four-group** at both symmetric settings | **12** | both indices among $\sigma$'s moved points, not an $\sigma$-cycle |
| **the non-abelian group of order 6** at both symmetric settings | **12** | one index among $\sigma$'s moved points, one among its fixed points $\{4,8\}$ |

I verified two of the order-6 cases directly: group order 6, **non-abelian**,
element orders $\{1,2,3\}$ (so $S_3$), value set of size 6 measured closed at the
declared bound, 364 closed paths at the base point, 0 non-signed-permutations —
i.e. a perfectly well-formed instance of the same species, with a **different
and non-abelian** holonomy group.

**Tier 3 — a declared systematic sample of the 8! family (every 401st in
lexicographic order, 101 completions, full GP-E holonomy):**

| GP-E group order | 1 | 4 | 6 | 8 | 10 | 12 | 14 | 30 |
|---|---|---|---|---|---|---|---|---|
| completions | 1 | **2** | 8 | 9 | 14 | 15 | 24 | 28 |

**100 of 101 carry nontrivial geometry. Only 2 of 101 give the Klein four-group.**

**What this does to the paper.**

1. **The existence of geometry is generic, not arena-relative.** The paper's
   §7.2 headline ("The geometry vanishes"), D2, and scope item 10.3 ("the same
   preparation vector with a different orthogonal completion carries no geometry
   at all") all frame completion-dependence as being about *existence*. My
   complete sweep says existence is the rule (99.76% carry a defect; 100/101
   sampled carry geometry) and vanishing is the rare exception (96/40,320) —
   and the paper tested precisely that exception.
2. **What the completion actually selects is the isomorphism type.** That is the
   paper's headline quantity. §6.2 calls the reproduction of the type "the
   unit's sharpest single finding"; the abstract says "the same isomorphism type
   the first base earns, on a base that shares none of its flesh". Within the
   pinned completion's own declared form it is a 12-of-28 coin flip against
   $S_3$; over the wider family it is ~2%.
3. **The choice was free.** No clause of the pin, of the species, or of §2
   selects $(1\,2)$ over $(1\,4)$. Both satisfy the uniqueness requirement D2
   invokes (both give 7 identification links at the symmetric settings). The
   selection rule is transparent and has nothing to do with the first base: a
   transposition of two $\sigma$-moved indices gives Klein-four, a transposition
   mixing a moved and a fixed index gives $S_3$.
4. **This is exactly the risk K3 names** — "audit which design choices were
   FORCED by the pin's species requirement vs free, and whether any free choice
   predetermines a pattern." Here a free choice predetermines P2's answer, and
   the designer had read the first base.

I want to be precise about what this does and does not do. It does **not**
falsify a gate: the pin's P2 says in terms that "Klein-four reproduction is NOT
required — a different group is a DISCOVERY", so P2 passes on any group, and
`GEN-STRUCTURE-REPRODUCES` follows correctly from the pre-registered rule. It
does mean the unit's most quoted sentence is conditioned on an unmeasured free
choice, and that the one disclosure the paper offers on this axis points away
from the question.

**Repair (what would satisfy me).** (i) Carry Tier 2 in the receipt — 28
complete rebuilds, cheap, and it is the sweep the protocol asked for. (ii)
Restate §7.2, §10.3 and D2 so the scope tag is about the **group**, not about
existence. (iii) Add one sentence beside the verdict: *"the isomorphism type is
selected by the declared completion — within the completion's own declared form,
12 of 28 choices give the Klein four-group and 12 give the non-abelian group of
order 6; the pattern that survives the change of base is the existence of a
nontrivial group with two sources, one of them a completion-manufactured
generator lying outside the declared scopes, and not the isomorphism type."*
That sentence is, in my view, the honest and still-interesting headline; it is
also closer to what the pin's P2 anticipated.

**Do I demand `REPRODUCES-AT-DECLARED-COMPLETION`?** No — that tag would say the
*existence* is completion-relative, and my sweep says the opposite. The correct
qualification is on P2's element/type content, which the paper already gestures
at ("the group's elements are a function of the base's declared data") but does
not measure. It needs measuring, and then the existing tag stands.

---

## 4. K3 — CROSS-BASE INTEGRITY

### 4.1 The five external anchors: genuine

`A08`–`A12` are real reads of `v13/code/nt_transport_receipt.json`
(`nt["findings"]["holonomy_group"]["per_setting"]["SP-E"]`,
`nt["tables"]["structure_group"]`, `["path_space"]`,
`["mechanism"]["single_rule_subconnections"]["SP-E/REAL"]`), not typed
constants dressed as reads. I re-read each field from the NT receipt myself:
group order 4; value-set size 4 and closed True; elements outside every declared
scope 2 at SP-E and 2 at SP-F; total paths 34,024 and pairs 4,972,096;
SP-E/REAL closed paths 18 and group order 2. **All five match.** §10.11's claim
that nothing of the first base's model is imported holds — I found no fixture,
operator or permutation of the first base anywhere in the instrument.

### 4.2 MAJOR-3 — D5's "combinatorial" explanation is refuted by measurement

D5 and §8 say the class counts "82 / 86 / 90 / 106 agree because the two bases'
path graphs are isomorphic and both groups are Klein-four", and explicitly
downgrade the agreement to "a consequence of the graph, not an independent
confirmation". I tested that directly.

**Step 1 — gauge-fix.** I chose a spanning tree of the GP-E graph from the base
node and set $T_n$ = the tree transport to each node; then for each link
$\ell:a\to b$ I formed $g_\ell = T_b^{-1} M_\ell T_a$. Measured: **every one of
the 13 links lands in the Klein four-group** $\{\mathbf 1,W,D,W\!D\}$ (the seven
tree links at the identity, and the six cotree links at
$W\!D,\ \mathbf 1,\ W\!D,\ W,\ W\!D,\ \mathbf 1$). Re-counting the 364 closed
paths purely combinatorially from that labelling reproduces
**82 / 86 / 90 / 106 exactly**, which validates the gauge-fixing.

**Step 2 — enumerate every alternative.** I then enumerated **all $4^6 = 4{,}096$**
gauge-inequivalent Klein-four connections on that same graph:

| measured | value |
|---|---|
| distinct class-count profiles produced | **89** |
| connections reproducing $(106,90,86,82)$ | **96 of 4,096** (2.3%) |
| connections whose generated group has order 4 | 3,906 |
| of those, reproducing the profile | **96 of 3,906** (2.5%) |
| most common profile | $(102,94,90,78)$, 384 connections |

So "isomorphic graph + Klein-four group" determines the profile only 2.5% of the
time. The agreement between the two bases records something stronger: **the same
gauge (cohomology) class of connection on the same graph** — a substantive
structural coincidence that the unit neither measures nor claims.

The direction here is *under*-claiming, not over-claiming, so the verdict is
untouched. But it is a mechanism asserted as fact and measured false, which is
the exact failure the RUNBOOK catalogue records at #38→#40 ("describe mechanisms
as measured, not as intended"). The **path-count** half of D5 (34,024 /
4,972,096) is genuinely combinatorial and correctly explained; only the
class-count half fails. *Repair: restate D5 with the 96/4,096 figure, and either
measure the cross-base labelling agreement or record it as an unexplained
agreement.*

### 4.3 MINOR-10 — the §8 comparison table is less anchored than its heading says

§8 opens *"The first base's numbers are read from its committed terminal receipt
and **anchored exit-1** (A08–A12)."* In fact, of the 21 rows, **7** read the NT
receipt and **14 are typed literals** in `run_comparison`: carrier 36, system
dimension 2, outcomes 2, the arithmetic string, "ANTI-invariant (the singlet)",
Schmidt rank 2, declared scope 72, settings 6, symmetric settings 2, admitted 2,
admitted extension 8, "the Klein four-group", "the qubit-only wing swap", and
"the defect is one half of the wing exchange: True".

**5 of the 12 claimed agreements** rest on typed constants (settings, symmetric
settings, admitted-2, admitted-8, group structure).

I verified every typed value against the NT receipt and **all 14 are correct**:
carrier 36 (the identity's `fixed_points` is 36), scope 72 and admitted 2 / 8
(the receipt's own field names `in_the_declared_72`, `in_the_admitted_2`,
`in_the_admitted_extension_8`), "Klein four-group {1, W, X, WX}" (in the
receipt's prose), the defect "the qubit-only wing swap" at all six settings, six
settings SP-A…SP-F with SP-E/SP-F symmetric. **So there is no numerical error.**
But "counts computed, never typed" is the RUNBOOK rule that exists because of
ledger #24, and the heading claims more anchoring than the table carries. *Repair:
read the remaining values from the NT receipt, or split the table into an
anchored block and a declared block.*

### 4.4 The design choices: forced vs free

| choice | forced by the pin/species? | can it predetermine a pattern? |
|---|---|---|
| qutrit wings, 81 configurations | free (pin asks for "different flesh") | no — patterns hold across my whole sweep |
| rational arithmetic, quaternion rotations | free | no |
| six settings, two symmetric | free; the symmetric/asymmetric split is what makes P1 two-way | no, and it earns the both-ways gate |
| $\psi$ exchange-**invariant** | needed for the Born-shadow clause the species uses | it fixes $H$'s equivariance, hence the closed form for $D$ — but not the group |
| **the completion transposition $Q=(1\,2)$** | **free** — D2's justification covers *some* non-symmetric completion, not this one | **yes — it selects the group (§3.3)** |
| the four-clause admission predicate, uniqueness | inherited from the first base's design | shapes the graph; the graph is shared, which is what D5 leans on |

One free choice, one predetermined pattern. That is MAJOR-1.

---

## 5. K5 — INSTRUMENT (lower depth, but checked)

Verified on my own AST scan of the frozen source and my own arithmetic:

| claim | my result |
|---|---|
| `MUTANT != …` comparisons anywhere in the source | **0** (one `MUTANT not in MUTANTS`, in argument validation) |
| `gate()` calls whose OK-predicate subtree mentions `MUTANT` | **0** |
| float literals / `float()` calls | **0 / 0** |
| the 28 `MUTANT ==` injection sites | all inside computation functions; none inside a gate predicate |
| census denominator / `never_falsified` | 24 / **empty**; the 25th must-pass is the census's own gate, correctly excluded |
| mutants | 26 declared, 23 "computation" + 3 "waiver" |
| the complete sweep, recomputed from the graph | $4\!\times\!512\!\times\!1 + 2\!\times\!8192\!\times\!5 = 83{,}968$, plus $128\!\times\!14 = 1{,}792$, **= 85,760** |
| cache hits / misses during the self-test | 0 / 85,760 |
| deviations from the scalar action; swept non-signed-permutations; loops moving under the checkpoint subgroup | 0 / 0 / 0 |
| raw sign moves at all 14 loops (so the sweep can certify anything) | 14/14 |

**Two mutants reconstructed from the receipt's prose, on my own instrument**
(the protocol asks for two; I did three):

* `defect-order` — composing $P_W U P_W U^{-1}$ then $\times P_WP_W$: the result
  is **not even a signed permutation**, so it cannot be in the group and P4 reads
  false. Dies.
* `hol-basepoint` — reading closed paths at every base point: the value set grows
  from **4 to 6**, 600 holonomies are not signed permutations, and the value set
  is **not closed** under composition, so P2's closure clause reads false. Dies.
* `label-collapse` — counting names drawn from $\{\mathbf 1, W\}$: 4 distinct
  tuples collapse to **3 distinct labels**, miscounting the group order. Dies.

All three die exactly where the receipt says they do.

### 5.1 MODERATE-8 — two of the 23 "computation" mutants are structurally waivers

`float-lax` is declared "a float literal introduced" and `exempt-lax` "a
mutant-identity exemption registered in a gate predicate". Neither does that.
Both append a sentinel to the gate's own evidence list *after* the AST sweep has
run (`lits.append(0)` at line 3004; `found.append(0)` at line 2974). The source
text is never changed, so the sweep never sees a float literal or a `MUTANT !=`
node. By the paper's own definition — *"A waiver overwrites a gate's computed
predicate after the fact"* — these are waivers. §11's "**23** perturb a
computation and **3** are waivers" is therefore overstated by two: GEN-EXACT and
GEN-NO-MUTANT-EXEMPTION are, strictly, falsified only by sentinel injection, and
the honest split is 21/5.

**Mitigation I accept:** for a gate whose input is the instrument's own source
text, no mutant *flag* can perturb the computation without editing the file,
which freeze-on-delivery forbids. Sentinel injection may be the only mechanism
available. That makes this a disclosure item, not a defect of the gate — and I
independently confirmed both gates' **substance** (0 `MUTANT !=`, 0 gate
predicates touching MUTANT, 0 float literals, 0 `float()` calls). *Repair:
reclassify, or disclose the sentinel mechanism at the claim and at the mutant's
declaration.*

### 5.2 MODERATE-7 — the read-time coordinate is analytically inert here

RUNBOOK §15's addendum is satisfied in form. It is inert in substance on this
base, and that is not disclosed. Measured:

* On **all 16,590 paths I inspected** (GP-A and GP-E, every start node, full
  reduced enumeration), the L datum's `read_time` **always equals the endpoint's
  checkpoint** — legs move it by $\pm1$ together with the node, identifications
  leave it fixed. So `read_time` is a *function of the endpoint*.
* The matched table pairs only paths sharing **both** endpoints. Therefore the
  read-time coordinate **can never differ inside a compared pair**, and §4's
  count "gated at zero" cannot be nonzero for any input.
* Independently: **dropping the coordinate entirely** from the node data still
  leaves **0** collisions (168 node pairs compared per configuration). So it is
  not separating anything at the node level either.
* The `readtime-conflate` mutant does kill the gate — but by replacing every node
  law with the *final* checkpoint's law. It perturbs law **content**, not the
  coordinate. The gate's teeth are against law-conflation, not against dropping
  the read-time tag.

*Repair: one sentence in §4 or §10.5 disclosing that on this base the coordinate
is determined by the endpoint and the gate is therefore forced.*

### 5.3 MINOR-9 — the direction flip-test is analytically forced and is not disclosed as such

I recomputed all 14 flip tests: **14/14 pass**. But the result is forced. Every
link variable is orthogonal (separately gated) and the reverse direction is
implemented as the transpose, so a reversed loop's matrix is exactly
$(L_n\cdots L_1)^{\mathsf T} = (L_n\cdots L_1)^{-1}$; the permutation part is the
inverse permutation for **any** input. And every element of this holonomy group
is an involution, so "the inverse permutation" is "the same permutation" at all
14 loops. The test retains narrow teeth (it kills `orient-flip`, which drops the
transposition), so it is a live instrument-integrity check — but its positive
content is forced, exactly like §7.1's permutation-part clause, **which the paper
does disclose**. The discipline is applied to one forced clause and not the
other. *Repair: name it a disclosure with the `orient-flip` teeth stated
separately.*

### 5.4 D3 and D6

**D3** (two transported objects, the composition defect not carried) is
pin-compliant in my reading: the pin's five patterns are properties of the
holonomy, which lives at the amplitude layer, and the L datum exists to satisfy
the matched-coordinate discipline. No result of the unit rests on the third
object, and §10 does not claim one. I have no finding. (§5.2 above does bear on
whether the L datum is doing work — but that is a §15 disclosure point, not a
pin violation.)

**D6** (memoisation) checks out in substance: `mm_memo` memoises $+$ and
$\times$ in $\mathbb{Q}$, never a transported value, and the transported-value
cache is bypassed in the self-test with its hit count measured at 0 against
85,760 misses. One narrow hole worth naming: the gate compares each switched
holonomy (built by `mm_memo`) against $\pm$ the unswitched holonomy (built by
`mm`), so a `mm_memo` defect that happened to produce a $\pm$ multiple of the
correct matrix would pass. The all-positive switching is a clean equality test
and does exist in the sweep, so the hole is small. No finding.

### 5.5 Census honesty

`never_falsified` is genuinely empty at denominator 24; the waiver-carried gate
(`GEN-VOCABULARY`) is named at the claim, and both denominators are printed. I
have no complaint about the census's honesty beyond §5.1.

---

## 6. Reproduction of the delivered artifacts

As a check independent of my own instrument, I copied
`gen_generality_exact.py` and `nt_transport_receipt.json` into a clean scratch
directory and ran the frozen instrument there. A single non-mutant run completes
in ~170 s with **12 anchors, 27 gates, 0 must-pass failures**, and
`KILL-JSON {"failed_anchors": [], "failed_gates": []}`.

A full `--falsification-selftest` delivery run was launched in the same clean
directory and was still sweeping mutants when I closed this review. Of the
mutants it had reached, **every kill-set matched the frozen receipt gate for
gate**:

| mutant | my clean-room run | frozen receipt |
|---|---|---|
| `gauge-subsample` | exit 1, kills GAUGE-COVARIANCE, GAUGE-CONTROL-MOVES | identical (2 gates) |
| `memo-lax` | exit 1, kills FRESH-EVAL | identical (1 gate) |
| `id-lax` | exit 1, kills 12 gates | identical, same 12, same order |
| `scope-lax` | exit 1, kills ADMISSION-TABLE, P1, P3, P4, P5 | identical (5 gates) |

I saw nothing in that partial sweep inconsistent with the receipt. I therefore
cannot personally certify the byte-identity of a *complete* delivery run, and I
flag that as the one delivered claim I did not finish checking — but nothing I
challenge or confirm above depends on it: every quantity is from my own
instrument.

I did not write to any repo path other than this review file.

---

## 7. Findings, ranked

| # | severity | finding | repair |
|---|---|---|---|
| 1 | **MAJOR** | The declared completion **selects the holonomy group's isomorphism type**, and the unit never measures this. Complete sweeps: 96 of 40,320 completions of the same $\psi$ are flat (the bare Householder is one of them); **12 of 28** transposition completions give Klein-four and **12 give non-abelian $S_3$**; 2 of 101 sampled give Klein-four, orders up to 30. The choice of $(1\,2)$ was free. | Carry the 28-point Tier-2 sweep; restate §7.2/§10.3/D2 so the scope tag is about the **group**, not existence; add the selection sentence beside the verdict. |
| 2 | **MAJOR** | **D2 is factually wrong about its own flip-test base.** The bare-Householder base has **14** full-leg identifications, a canonical loop at **four** of six settings, and the five patterns are posed and answered on it. | Replace with the measured statement; note the new $t{=}2$ FULL link. |
| 3 | **MAJOR** | **D5's "combinatorial" explanation is refuted.** Only **96 of 4,096** Klein connections on the shared graph reproduce 82/86/90/106 (89 distinct profiles; 96 of 3,906 order-4 connections). The agreement records a shared gauge class, not the graph. | Restate D5 with the 96/4,096 figure; measure the cross-base labelling or record it as unexplained. |
| 4 | MODERATE | **P5's 16 cells are 1 free measurement + 15 forced.** All four collections are $W$-invariant and contain $\mathbf 1, W$; the inclusions collapse the rest. The table reduces to $D\notin 216$. | Print the forcedness; name the one free cell. |
| 5 | MODERATE | §6.5's "**Every** link … is a transport the base admits" is false for the 6 leg links: $U_{\text{prep}}$ is not a signed permutation; $U_A(R_0),U_B(R_0)$ are permutations but outside all four collections. | "every **identification** link"; add the leg-membership row. |
| 6 | MODERATE | $D$ is **not** the preparation's defect: $D=(S Q^{\mathsf T} S Q)\otimes I_9$, independent of $\psi$; the Householder cancels identically. The 45 is $5\times9$ from $Q'\!\cdot\!Q$ = two disjoint transpositions. | Print the closed form (two lines; it strengthens §7.2). |
| 7 | MODERATE | The **read-time coordinate is inert**: it equals the endpoint checkpoint on all 16,590 paths inspected, and the table pairs only endpoint-sharing paths, so the zero count is forced. Dropping it entirely also gives 0 collisions. | One disclosure sentence. |
| 8 | MODERATE | **`float-lax` and `exempt-lax` are structurally waivers** (sentinel appends at lines 3004 / 2974), not computation mutants; §11's 23/3 split should be 21/5. Both gates' substance verified independently. | Reclassify or disclose the sentinel mechanism. |
| 9 | MINOR | The **direction flip-test is analytically forced** (orthogonal link variables + transpose convention; every element an involution) but not disclosed as such, while §7.1's forced clause is. | Name it a disclosure; state the `orient-flip` teeth separately. |
| 10 | MINOR | **14 of 21 §8 rows carry typed first-base constants** under a heading claiming receipt-anchoring; 5 of the 12 claimed agreements are typed. All 14 verified correct against the NT receipt. | Read from the receipt, or split anchored/typed. |
| 11 | MINOR | The **216-element extension is not closed** under composition (the 162 is); §2.5's closure sentence sits where it reads as covering both. | One clause. |
| 12 | MINOR | §7.2's prose omits the **new FULL link at $t{=}2$** the alternative completion creates (the count 5 discloses it, the prose does not). | One clause. |

**No finding of mine changes a single number in the paper, and none falsifies a
gate or the pre-registered decision rule.** Findings 1–3 change what the paper is
entitled to say about its own headline; 4–8 are disclosure-discipline items the
RUNBOOK's own §14/§15 addenda require; 9–12 are corrections.

---

## 8. What I could not break

For the record, since a hostile review that only lists complaints is not a
measurement either:

* **587 independently recomputed quantities, 0 mismatches.** Including the
  hardest ones to get right by accident: 1,896/2,820 and 0/56 both ways; the
  600/820 non-signed-permutation disclosure; 82/86/90/106; the 18-closed-path
  realized-rule sub-connection with identity ×10 and $D$ ×8; the eight
  matched-pair cells summing correctly to 4,972,096; the 22-cell closed-path
  census including the GP-E/GP-F asymmetry (220 "another permutation" at GP-E,
  0 at GP-F).
* **P1 genuinely comes out both ways on one base.** That is the single strongest
  anti-fixture datum in the unit and it survives independent recomputation.
* **The negative control has real teeth.** Not a signed permutation at the four
  flat settings; at the symmetric settings my instrument identifies it as
  exactly $W\!D$ (the paper says only "another permutation" — accurate, if
  under-informative).
* **The positive control agrees at all six settings** and the paper is candid
  that its discriminating power is small.
* **The instrument's discipline claims are true**, verified on my own AST scans,
  not merely on the instrument's self-report.
* **The freeze/gate-order discipline holds**: the base declaration's gates
  precede every transport gate in the receipt's own order.
* **Nothing of the first base's model is imported.** I looked.

---

## GRADE

# ACCEPT-WITH-FIXES

The unit's arithmetic is impeccable and its verdict follows correctly from its
pre-registered decision rule on gates that genuinely pass. But the single
question the hostile protocol named as hardest — *is the pinned completion
generic or special among geometry-bearing ones?* — was not asked, and the answer
is that it is special in exactly the way that matters: it selects the
isomorphism type that the first base has. The paper's defence of that choice
(D2) misdescribes its own test base, its one disclosure on the axis (§7.2)
measures the rare vanishing case rather than the generic varying one, and D5
further under-claims the cross-base agreement on a mechanism I measured false.
Findings 1–3 must be repaired in the paper's text and 1 must be repaired in the
receipt (a 28-point sweep). With those in, `GEN-STRUCTURE-REPRODUCES` stands —
scoped, as it should be, to the existence of a nontrivial group with two sources
and a scope-escaping completion-manufactured generator, and **not** to the
isomorphism type.

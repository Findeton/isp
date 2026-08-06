# CYCLE B HOSTILE REVIEW — R3, SUFFICIENCY / INSTRUMENT LENS

**Reviewer:** R3 (sufficiency/instrument lens).  **Protocol:**
`v13/note-rq0-fixed-point-hostile-protocol.md` at commit `6effc7a`, FROZEN
before dispatch; this review is judged against that protocol only.
**Object under review** (commit `6fab072`), SHA-256 prefixes recomputed by
me and **all four match the protocol's pin**:

| artifact | protocol | recomputed |
|---|---|---|
| `paper-rq0-task-record-fixed-point.md` | `9afc0ad8578e` | `9afc0ad8578ea29f` ✓ |
| `rq0_l0_fixed_point_exact.py` | `c77e94561d14` | `c77e94561d148cb2` ✓ |
| `rq0_l0_fixed_point_output.txt` | `1d93073ff1e3` | `1d93073ff1e393f0` ✓ |
| `rq0_l0_fixed_point_receipt.json` | `eef553549a38` | `eef553549a3821cc` ✓ |

**Discipline observed.** Exact arithmetic only (`fractions.Fraction`;
no float anywhere in my rebuild); interpreter `/opt/homebrew/bin/python3.13`;
own code in the session scratchpad only; **nothing imported from the unit's
code** — my linear algebra, commutant solve, partition lattice, union-find,
channel Kraus families, availability search and support relation are all
rebuilt from the paper's prose; repo read-only; this is the single file I
write; no child agents; freeze-on-delivery.

---

## VERDICT

\[
\boxed{\texttt{ACCEPT-WITH-FIXES}}
\]

**No computed number moved.** Every load-bearing quantity I re-derived
independently reproduced the paper's value exactly — 20 recomputations,
zero numerical disagreements (table in §6). The collapse survives K2, the
(H-avail) coincidence survives verbatim, the fixed-point characterization
survives an exhaustive rebuild from *all* left-total relations at atom
count ≤ 4, and the registered verdict name is the correct pre-registered
instantiation.

The fixes are three: **one theorem sentence is stated more broadly than it
is proved (K4 bites — F1)**; **the de-smuggling discriminator's evidence is
weaker than its presentation (F2, F3)**; and **the K2 adjudication, which
the paper never attempts, must be recorded because it is the first thing a
referee will ask (F4 — and it comes out in the paper's favour)**. None of
these changes the verdict `RQ0-L0-BLOCKED-AT-DE-SMUGGLING`.

---

## 1. Per-rung confirmation lines (protocol §"Verdict vocabulary")

- **(a) the G0 collapse — CONFIRMED, independently and with its reason.**
  $D_M(b)=\sum_r z_rbz_r=b$ on all **308** instrument–effect pairs of the
  committed battery (0 violations), and $F^\sharp\circ D_M=F^\sharp$ on all
  **16** future–instrument pairs (0 violations). I add the algebraic reason
  the paper leaves implicit: the $z_r$ are *central* and sum to $1$, so
  $\sum_r z_rbz_r=\sum_r z_rb=b$ identically — the collapse is not a
  fixture accident, it is forced by Lemma 3.1's identification of records
  with partitions of the centre. Theorem 2.1 is correct and unevadable.
- **(b) the Galois connection for the availability reading — CONFIRMED at
  this lens's depth.** I rebuilt `comp` (connected components of the
  collision graph) and the join of preserved partitions, and verified
  Lemma 3.2 and Proposition 3.4's join-closure exhaustively over all
  left-total relations at atom counts 2, 3, 4. The 30,422-test two-sided
  adjunction sweep is R2's assignment and I did not duplicate it.
- **(c) the cl = identity degeneracy — CONFIRMED, exhaustively and from a
  stronger starting point than the paper's generators.** Computing
  $\operatorname{cl}(\pi)$ from the **exhaustive** future family (all
  $(2^n-1)^n$ left-total relations) rather than from the reprepare
  generators: $\operatorname{cl}(\pi)=\pi$ for **2/2** records at $n=2$,
  **5/5** at $n=3$, **15/15** at $n=4$. The fixed-point strata
  $1,2,5,15,52$ reproduce.
- **(d) the discriminator failure — CONFIRMED as a fact, with its evidence
  downgraded.** The manufactured record is a fixed point under Reading A
  (it must be — $\operatorname{cl}=\operatorname{id}$ holds for *every*
  finite boundary, so the manufactured boundary contributes nothing) and is
  the unique fixed point under Reading B. The *finding* is right. Its
  gating is weak: see F2 (the boundary is typed, not manufactured) and F3
  (gate G2-11 is a tautology).
- **(e) the one-boundary impossibility theorem — CONFIRMED ONLY AS
  ISOMORPHISM-COVARIANCE, NOT AS STATED.** The proof establishes that every
  object *this paper constructs* is covariant under admitted reversible
  operational equivalences, hence cannot separate $A_P$ from $A_Q$. The
  paper's sentence quantifies over *all* criteria definable from
  one-boundary data. That larger class is not defined and is not covariant
  in general. K4 bites; see F1.
- **(f) `RQ0-L0-BLOCKED-AT-DE-SMUGGLING` as the correct pre-registered
  instantiation — CONFIRMED.** The pin (`7a80e39`) registers exactly three
  outcomes. `NO-NONTRIVIAL-FIXED-POINT` is refuted by computation
  (nontrivial fixed points exist wherever the core has ≥ 2 atoms);
  `W3-OPERATIONAL-MARKOV-BOUNDARY` requires smuggling rejection, which
  measurably fails; `BLOCKED-AT-⟨object⟩` with object = *a task-independent
  selector on the fixed-point set* is the honest remainder. The un-typed
  object is genuinely un-typed: a closure operator equal to the identity
  supplies no selector at all.

---

## 2. K2 — THE ALTERNATIVE $D_M$ READING (my primary kill-shot)

**Attack as posed.** G0 kills the literal formula via $D_M=\sum_r m_r=I$.
Read $D_M$ instead as **measure-AND-BROADCAST** (the flag is retained), so
that $F\circ D_M$ acts on system + flag. Does the literal formula become
nondegenerate under that reading, and does it then differ from the adopted
availability form?

**Adjudication: THE COLLAPSE CLAIM SURVIVES INTACT. The broadcast reading
does not rescue the literal formula and does not compete with the adopted
form — in its only nondegenerate, type-correct version it is *equivalent*
to Definition 2.3.**

Write $\widehat D_M:\rho\mapsto\sum_r m_r^*(\rho)\otimes|r\rangle\langle r|$
for the flag-retaining instrument, $S\to S\otimes\mathbb C^\Omega$. The
literal formula $\lVert F-F\circ D_M\rVert_{\mathrm{Test}}=0$ is then
**type-ill-formed**: the left side is $S\to S'$, the right side is
$S\to S'\otimes\mathbb C^\Omega$. There are exactly three ways to repair the
type, and I ran all three.

- **B1 — trace the flag out before comparing.** The $S'$-marginal of
  $(F\otimes\mathrm{id})\widehat D_M(\rho)$ is $F(\sum_rm_r^*(\rho))=F(\rho)$.
  **Re-collapses on 16/16 battery pairs** (computed). Retaining the flag and
  then discarding it returns Theorem 2.1 exactly. No rescue.
- **B4 — keep the flag, demand no later readout.** Compare
  $F\otimes\mathrm{id}$ with $(F\otimes\mathrm{id})\circ\widehat D_M$ as maps
  on $S\otimes\mathbb C^\Omega$, where the broadcast overwrites the flag.
  The broadcast always rewrites the flag marginal, so the test **fails for
  every nontrivial record** and holds only for the one-outcome record
  (computed on $\mathbb C^2$: `{((0,),(1,)): False, ((0,1),): True}`).
  Nondegenerate, but degenerate in the *opposite* direction — it empties
  $\operatorname{Pres}$ instead of filling it. No rescue.
- **B3 — keep the flag and demand the record be readable after $F$ as it
  was before it.** $F\in\operatorname{Pres}_{\mathrm{bcast}}(M)$ iff there is
  an admitted later instrument $M'$ with
  $(F\otimes\mathrm{id})\circ\widehat D_M=\widehat D'_{M'}\circ F$, i.e.
  $m_s\circ\Phi=\Phi\circ m'_s$ for every $s$ — "measure then evolve" and
  "evolve then measure" agree on the full flag-joint statistics, not merely
  on the flag marginal. This **is** nondegenerate.

**B3 is equivalent to Definition 2.3, and the paper's own Lemma 2.4 is the
proof.** ($\Rightarrow$) Take $b=1_{S'}$: $z_s\Phi(1)=z_s=\Phi(q'_s)$, which
is the adopted criterion. ($\Leftarrow$) Given $\Phi(q'_s)=z_s$, the
projection $q'_s$ has projection image, so by Lemma 2.4 it lies in the
multiplicative domain and $\Phi(q'_sb)=\Phi(q'_s)\Phi(b)=z_s\Phi(b)$ for
every $b$ — which is B3. I confirmed this computationally as well:
**B3 membership over the whole 16-triple battery gives 9 inside / 7 outside
with 0 disagreements against Definition 2.3.**

**Consequence for the paper (favourable, and it should be claimed).** The
adoption of Definition 2.3 in §2.2 is currently justified only *negatively*
— the literal form collapsed, so something else was needed, and non-claim
§7 concedes "no claim that the availability form is the only possible
repair". The K2 analysis upgrades that: among the flag-retaining repairs of
the literal formula, B1 re-collapses, B4 empties, and B3 — the only
survivor — **is** Definition 2.3. That is a uniqueness statement at the
scope of the broadcast family, and it costs one paragraph. Its absence is
the single biggest missed opportunity in §2 (F4).

**One correction inside the reduction.** Definition 2.3's reduction to
$\Phi(q'_s)=q_s$ is justified in the paper (line ~288) by "$\Phi$ is unital
and $\sum_sq'_s=1$". That is not the operative ingredient. Summing
$m_r(\Phi(q'_s))=\delta_{rs}q_r$ over $r$ and using **completeness of $M$**,
$\sum_rz_r=1_S$, gives $\Phi(q'_s)=q_s$. Unitality of $\Phi$ and
$\sum_sq'_s=1$ deliver only the consistency check
$\sum_s\Phi(q'_s)=1$. The equivalence is true; the reason cited is the wrong
one — and the right one is pointed: **the very identity $\sum_rm_r=I_S$ that
destroys the literal formula is what makes the availability form reduce to a
computable criterion.**

---

## 3. The claimed literal coincidence with v12's (H-avail) — VERDICT: EXACT

I read `v12/paper1-composition-defect.md` §4 and
`v12/note-w6-record-coreference.md` and checked the correspondence at three
levels. **It is literal, not analogical.**

1. **The quotation is verbatim.** v12 §4.1: *"(H-avail) availability. For
   every later configuration $i$, all cut configurations $k$ with
   $(U_2)_{ik}\ne0$ lie in one sector."* The v13 paper's §2.2 Antecedent
   reproduces that sentence word for word. ✓
2. **The transported statement is the same statement.** v13's criterion
   contrapositive — "for every later atom, all earlier atoms reaching it lie
   in one block" — maps onto (H-avail) under the dictionary *later atom ↔
   later configuration*, *earlier atom ↔ cut configuration*, *block ↔
   sector*, *$l\in\operatorname{sup}(k)$ ↔ $(U_2)_{ik}\ne0$*. I verified the
   equivalence exhaustively over **all $2^9=512$ support patterns at $n=3$
   against all 5 partitions — 1,715 comparisons, 0 mismatches.**
3. **The dictionary's one soft joint is sound.** v13's support is a *trace*
   support, $\operatorname{tr}(z_lF(z_k))\neq0$, where v12's is an
   *amplitude* support. Trace supports could in principle lose entries to
   cancellation. They cannot here: $F(z_k)\succeq0$ and $z_l$ is a
   projection, so $\operatorname{tr}(z_lF(z_k))\ge0$ always. **I computed
   every sector weight on the battery: 0 negative weights.** For a unitary
   future the trace weight is $\sum_{i\in l,m\in k}|(U_2)_{im}|^2$, a sum of
   non-negative terms — so the two supports coincide entry by entry, and the
   extension from unitaries to CP futures is the only substantive
   generalization, exactly as the paper says.

**Bonus coincidence the paper under-claims.** v13's `comp(F)` (connected
components of the collision graph) is *the same object* as v12 Theorem 4.5's
$M(U_2)$, the transitive closure of the co-merge relation. I verified this
over all 512 support patterns at $n=3$: **0 mismatches.** So Lemma 3.2 is
not merely consistent with the predecessor's decision procedure, it *is*
it. Worth one sentence.

**Where the coincidence must be fenced, and where the LOG oversteps.** v12's
record notion is $(\mathrm{H\text{-}orth})\wedge(\mathrm{H\text{-}corr})
\wedge(\mathrm{H\text{-}avail})$; v13 transports **(H-avail) alone**, and it
transports it into a *different role* — in v12 it is a clause in the
definition of a record structure, in v13 it defines *preservation of an
already-given record by a future*. The paper is careful about this (it says
"the availability hypothesis", singular). **LOG #115 is not**: "the two
programmes' record notions coincide exactly" is an overclaim — (H-corr) is
not transported at all. That sentence should be corrected at adjudication.

---

## 4. Fidelity of the discriminator to #103's manufactured-PVM example

**Verdict: the committed *numbers* are faithful and correctly sourced to the
superseding artifact; the committed *construction* is not re-run, and the
paper does not say so.**

**What is right, and it is the harder half.** #103's *paper* §9.5 records a
$2{+}1{+}1$ PVM giving block algebra $M_2\oplus\mathbb C\oplus\mathbb C$
with centre $\mathbb C^3$, and a $2{+}2$ PVM giving $M_2\oplus M_2$ with
centre $\mathbb C^2$. #103's *adjudication* §6 corrects this: the matched
success algebra **acquires an additional sink summand**, giving centres
$\mathbb C^4$ and $\mathbb C^3$. The unit uses **4 and 3** and sources
anchors A10/A11 to "#103 sec 6.2" — i.e. it tracks the adjudication, which
supersedes the paper. I rebuilt $A_P=\bigoplus_rP_rB(H)P_r$ from the rank
multisets and confirmed by my own commutant solve: without sink 3 and 2,
with sink **4 and 3**. Using the superseded values would have been the easy
error; the unit did not make it.

**What is not right.** `FIXTURES["PVM211"]` is
`CStar("… manufactured 2+1+1 with sink", (2,1,1,1))` — the block structure
is **declared**. No PVM $P$ is ever exhibited; the matched dephasing
$\mathcal D_P$ is never built; $A_P=\bigoplus_rP_rB(H)P_r$ is never computed
from projections; the affine-separating state family of #103 §7.1 is never
exhibited; the minimal-boundary construction is never run. `centre_dimension()`
performs a genuine exact commutant solve — but on an algebra whose answer is
fixed by the tuple it was typed with. Anchors A10/A11 therefore cannot fail
unless someone mistypes four integers, and **neither A10 nor A11 appears in
the six-mutant falsification table** (the mutants hit A07, A16, A12, A26,
A14, A28 — the discriminator's own anchors are never mutation-tested).

**Why this is a wording defect and not a fatal one.** $A_P$ for a rank-$(2,1,1)$
PVM genuinely *is* $\cong M_2\oplus\mathbb C\oplus\mathbb C$, so the
isomorphism class is correct; and Theorem 4.6 says the whole construction is
covariant, so the isomorphism class is *all that can matter*. The typing is
therefore legitimate — but it is legitimate *because of Theorem 4.6*, and the
paper must say so instead of leaving §5.3's "computed for each fixture by an
exact commutant solve, never typed" to imply an end-to-end reconstruction.
The claim is true of the computation and misleading about the object.

---

## 5. K4 (secondary) — the criterion-class quantifier

**The paper's sentence does not match what is proved.** Theorem 4.6 concludes
"no criterion definable from one-boundary data can accept one boundary and
reject the other"; the abstract repeats it. The proof supplies: (i) a unitary
$V$ with $VP_rV^*=Q_r$; (ii) conjugation by $V$ is an admitted reversible map
carrying the triple onto the triple; (iii) *"every object constructed in this
paper is defined from the triple … therefore every such object is covariant"*;
(iv) a covariant predicate takes the same value on isomorphic arguments.

Steps (i)–(iv) prove: **no isomorphism-covariant criterion on (boundary,
admitted law, admitted instruments) can separate $A_P$ from $A_Q$.** They do
not prove the unrestricted claim, because "definable from one-boundary data"
is nowhere defined and, read literally, includes non-covariant criteria — a
criterion reading matrix entries in a chosen basis, or the atom labels, or a
declared generating set, is definable from one-boundary data and is not
covariant. The gap between the two statements is exactly the unproved premise
*"operational one-boundary data = isomorphism-invariant data"*, which is
plausible and is arguably the content of #111 Cor 5.6, but is not stated as a
hypothesis and is not gated.

The sound narrower theorem is enough for the verdict: the paper's own
constructions are covariant, so *this* closure could not have de-smuggled,
which is what `BLOCKED-AT-DE-SMUGGLING` records. The fix is a rescope, not a
retraction.

---

## 6. Independent numbers table

All values below are mine, from a rebuild that imports nothing from the
unit. Exact arithmetic throughout.

| # | quantity | my value | paper | agree |
|---|---|---|---|---|
| N1 | $D_M(b)=\sum_rz_rbz_r=b$: instrument–effect pairs / violations | 308 / 0 | 308 / 0 | ✓ |
| N2 | literal formula $F\circ D_M=F$: future–instrument pairs / violations | 16 / 0 | 16 / 0 | ✓ |
| N3 | $\operatorname{TV}(p_0,p_1)$; $\min_d\max_i\operatorname{TV}(p_i,d)$ | 1/2 ; **1/4** at $d=1/2$ | 1/2 ; 1/4 | ✓ |
| N4 | availability membership on the battery: inside / outside | **9 / 7** | 9 / 7 | ✓ |
| N4b | the five non-identity preservers | bit-flip; $X\oplus1$; sector-keeping reprepare; eraser-core reprepare; success/failure keeping | same five | ✓ |
| N4c | the seven non-preservers | no-write reset; reprepare-0; reset into sector 0; sector-merging reprepare; merge{0,1}; total erasure ($\mathbb C^5$); total erasure ($M_4\oplus\mathbb C$) | same seven | ✓ |
| N5 | Def 2.3 vs sector criterion: triples / disagreements | 16 / 0 | 16 / 0 | ✓ |
| N5b | negative sector weights $\operatorname{tr}(z_lF(z_k))<0$ | 0 | (implicit) | ✓ |
| N6 | **K2**: B3 broadcast reading vs Def 2.3, disagreements | **0** (9 in / 7 out) | not attempted | new |
| N6b | K2 reading B1 (flag traced out): re-collapse | 16/16 | not attempted | new |
| N6c | K2 reading B4 (flag kept, no readout): holds only for trivial record | confirmed | not attempted | new |
| N7 | (H-avail) vs v13 criterion, all $3\times3$ support patterns | 1,715 comparisons / **0 mismatches** | "verbatim" | ✓ |
| N7b | `comp(F)` vs v12 Thm 4.5's $M(U_2)$, 512 patterns | **0 mismatches** | not claimed | new |
| N8 | minimal sufficient classical experiment: eraser / preserving / bundle | 5 / 1 / 5 | 5 / 1 / 5 | ✓ |
| N9 | centre dims (own commutant solve) C2,M2,M2+C,C5,M4+C,C1,PVM211,PVM22 | 2,1,2,5,2,1,**4**,**3** | 2,1,2,5,2,1,4,3 | ✓ |
| N10 | $|\mathrm{Part}(n)|$, $n=1..5$ | 1,2,5,15,52 | 1,2,5,15,52 | ✓ |
| N10b | $\operatorname{cl}=\operatorname{id}$ from the **exhaustive** relation family | 2/2, 5/5, 15/15 at $n=2,3,4$ | all fixed | ✓ |
| N10c | membership tests at $n\le4$: $9{\cdot}2+343{\cdot}5+50625{\cdot}15$ | 761,108 | 761,108 | ✓ |
| N10d | declared $n=5$ subfamily: $84{,}375\times52$ | 4,387,500 | 4,387,500 | ✓ |
| N11 | strictly-refining record pairs, $n=2..5$ | 1+7+45+306 = **359** | 359 | ✓ |
| N11b | inherited coarse seams of a 4-element branch set | 9 (6 of type 2+1+1, 3 of type 2+2) | 9 | ✓ |
| N11c | **records on $\mathbb C^5$ whose branch restriction IS one of the nine seams** | **33 of 52** (verified combinatorially: $6\times4+3\times3$) | not reported | new |
| N12 | $s_2^2=(I,5I)$; squared norms $\lVert X\rVert^2,\lVert2X{+}Z\rVert^2,\lVert X{-}3Z\rVert^2,\lVert2X{-}2Z\rVert^2$ | (I,5I); 1,5,10,8 | (I,5I); 5,1,10,8 | ✓ |
| N13 | $A_P$ centre dim, $2{+}1{+}1$ / $2{+}2$, without and with sink | 3→**4** / 2→**3** | 4 / 3 | ✓ |
| N14 | squared coherence loss from off-diagonal $3/16$ | $4\cdot3/16=3/4$ | 3/4 | ✓ |

**Zero disagreements.** Three rows are new information rather than checks
(N6, N7b, N11c) and one row (N13) separates the superseded #103 paper value
from the corrected adjudication value.

---

## 7. Findings, ranked

### F1 — MODERATE (fix-real). Theorem 4.6 is stated as unrestricted impossibility but proved as isomorphism-covariance.
K4 bites. The class of "criteria definable from one-boundary data" is never
defined and is not covariant in general; the proof only reaches covariant
predicates. Because Theorem 4.6 is the load-bearing explanation for the
verdict — §6 leans on it ("could not have been rejected at this scope") —
the sentence must be brought back to what is proved, in the abstract, in
§4.5 and in §6. Rescoping weakens the *explanation* but not the *verdict*:
the discriminator's failure is a computed fact (Theorem 4.5), independent of
4.6.

### F2 — MODERATE (fix-real). The manufactured boundary is typed, not manufactured; §5.3's "never typed" is misleading about the object.
See §4. The isomorphism class is correct and — by Theorem 4.6 — sufficient,
so the practice is defensible; but it must be *declared* as running on the
isomorphism class, and §5.3's blanket "computed …, never typed" must be
restricted to the centre-dimension computation. Additionally: A10/A11 are
the discriminator's only #103 anchors and are the only committed anchors
outside the mutant table, so the falsification self-test never exercises the
discriminator's provenance.

### F3 — MODERATE (fix-real, code/receipt). Gate G2-11 is a tautology.
In `run_g2` the manufactured record is `discrete(core_size(alg))` and
Reading B's unique fixed point is computed as `discrete(core_size(alg))` —
literally the same expression. `readingB_unique == manufactured` is `True`
for any algebra whatsoever and cannot fail. The *claim* it certifies
(Theorem 4.4's uniqueness) is separately proved and true; the gate is not
evidence for it. G2-10 is a real computation but is a special case of the
already-verified $\operatorname{cl}=\operatorname{id}$ at $n=4,3$ and carries
no manufactured-specific content. The receipt's "57/57" should not be read
as 57 independent discriminating tests.

### F4 — MODERATE (fix-real, additive; favourable to the paper). The K2 broadcast reading is never considered, and it strengthens the adoption.
See §2. B1 re-collapses, B4 empties, B3 ≡ Definition 2.3 via Lemma 2.4. One
paragraph converts §2.2's purely negative justification into a uniqueness
claim at the scope of the flag-retaining repairs, and pre-empts the most
obvious referee objection to Theorem 2.1.

### F5 — LOW-MODERATE (fix-real, honesty). The $\mathbb C^5$ negative control's degenerate satisfaction should be quantified.
§5.1 argues the five-atom eraser core "is not promoted to a record seam"
because *the core's* restriction to the branch labels is the discrete
partition, which is none of the nine seams — true, but it is not a seam
because it is **too fine**, not because anything rejected it. I computed
that **33 of the 52 records on $\mathbb C^5$ restrict to one of the nine
inherited seams, and every one of them is a fixed point.** The paper's
mitigating sentence ("all 52 records … are equally fixed, so the closure
prefers none of them") is present and honest, but the number makes the point
unambiguous: the control's negative direction is *"the closure selects
nothing"*, not *"the closure excludes seams"*.

### F6 — LOW (fix-cosmetic). Definition 2.3's reduction cites the wrong ingredient.
"Because $\Phi$ is unital and $\sum_sq'_s=1$" should be "because $M$ is
complete, $\sum_rz_r=1_S$". The equivalence is correct; only the justification
is misattributed. The correct ingredient is also the more interesting one
(§2 above).

### F7 — LOW (fix-cosmetic, code). The deficit gate is a grid minimum, not an optimum.
`G0-03` computes $\min$ over the 13-point grid $d=k/12$. The paper's Prop 2.2
supplies the *analytic* lower bound $\max_i\operatorname{TV}(p_i,d)\ge
\operatorname{TV}(p_0,p_1)/2=1/4$ with equality at $d=(1/2,1/2)$, so the
paper's claim "the optimal recovery deficit is exactly $1/4$" is fully
earned — by the proof, not by the gate. I confirmed the optimum
independently (exact scan at denominator 1200 plus the analytic argument:
$\max(a,b)\ge(a+b)/2$). The receipt row should not be read as an optimality
certificate.

### F8 — LOW (process). The deviations (1)–(8) are not recoverable from the frozen artifacts.
The protocol's common gates require each of the eight worker deviations to be
adjudicated fix-real/fix-cosmetic. They are referenced only in LOG #115
("Worker deviations (1)-(8) accepted") and appear nowhere in the paper, the
code, the output, the receipt or any dispatch note; only one is described
(the pin's ambiguous closure read both ways). **I can adjudicate that one:
fix-real, and correctly handled** — reading the pin's ambiguous target both
ways (A: the availability adjoint, Galois-sound; B: #111's core-of-boundary,
physical-sided) and reporting the split verdict is the honest resolution, and
both readings are separately gated. The other seven cannot be adjudicated by
any reviewer from the frozen record. The adjudicator should either publish the
list or drop the gate.

### F9 — LOW (correction to the committed LOG, not the paper). LOG #115 overclaims the v12 coincidence.
"the two programmes' record notions coincide exactly" — only the availability
clause is transported; (H-corr) is not, and the transported clause plays a
different role (preservation of a given record, not definition of a record).
The paper itself is careful. Correct the LOG line at adjudication.

### F10 — LOW (disclosure). The 9-in/7-out stability table is asymmetric in evidence.
The 9 memberships carry *exhibited* zero-deficit readouts (I re-derived all
nine assignments and verified $\Phi(q'_s)=q_s$ exactly). The 7 exclusions
carry an *argument* (two blocks reach a common sector, so no later readout
separates them) plus **one** computed number, the reset's $1/4$. §5.4's
wording is accurate, but §1.4's Discriminator gate row — "the exact positive
recovery deficit that separates them" — suggests seven numbers where there
is one.

---

## 8. Common gates (protocol §"Common gates")

- **Paper-vs-receipt, ≥10 spot checks:** 17 performed (N1–N14 above map onto
  gate G0-01/02/03/05/06/07 and anchors A01–A05, A06–A08, A09-1..5, A10–A14,
  A15–A19, A27, A28). Every number in the paper that I checked is carried by
  a receipt row, and every receipt row I checked is reproduced by my own
  arithmetic. **No number moved.**
- **Scope tags:** present on every numbered result — `[FIN]`, `[EXH-4]`,
  `[FIX]` used consistently; §"Scope box" declares finite / one boundary /
  exhaustive-at-≤4 / declared-subfamily-at-5 / general case by proved lemma;
  the law family (complete admitted nondisturbing repeatable classical
  instruments; admitted deterministic futures; condition R where used) is
  named at each use. Theorem 4.2 is correctly tagged `[EXH-4]` and not
  `[EXH-5]`. **PASS.**
- **Forbidden vocabulary:** swept. No composition/tensor claim, no locality,
  overlap, topology, causality, spacetime, QFT or gravity claim. The only
  hits are inside §7 Non-claims (denials) and one occurrence of "sequential
  flagged composition", which is the declared inherited *one-boundary*
  postulate about composing instruments in time and is explicitly fenced
  ("Neither is a statement about how two boundaries combine"). "Markov"
  appears only inside the pre-registered outcome name and carries its
  disclaimer at §"Scope box". **PASS.**
- **Prose vs gates:** one failure — F1 (Theorem 4.6's quantifier) — plus two
  presentational overreaches, F2 (§5.3 "never typed") and F10 (§1.4's
  "exact positive recovery deficit"). The degenerate-satisfaction disclosures
  are kept: the paper states plainly that a closure equal to the identity
  "partitions nothing", that "existence here is not evidence of selection; it
  is evidence of vacuity", and that the closure "prefers none" of the 52
  records. That honesty is the paper's strongest feature and should not be
  edited down. **PASS WITH FIXES.**
- **Deviations (1)–(8):** cannot be discharged as specified — see F8. One
  adjudicated fix-real; seven unrecoverable.
- **Anchors' parent values against #103/#111:** checked. A10/A11 correctly
  follow the #103 **adjudication** (4, 3) and not the superseded #103 paper
  §9.5 (3, 2) — the trap was avoided. A01–A04, A27, A28 match #103 §7.2.
  A06–A08 match the adjudication's corrected minima $\mathbb C$, $\mathbb C^5$,
  $M_4\oplus\mathbb C$. A14's nine seams reproduce (6 + 3). **PASS.**
- **Determinism / mutants / floats:** receipt records 57/57 gates, 34/34
  anchors, `anchor_type_violations: []`, arithmetic declared
  "exact (fractions.Fraction and Q(i)); no float in any substantive path",
  `source_sha256` matching the pinned file, `pin_commit 7a80e39`,
  `immutable_base_commit 6c2d7b8`. Six mutants each break exactly one anchor
  (A07, A16, A12, A26, A14, A28) and each is required to exit 1. **PASS**,
  with F2's caveat that the discriminator's anchors are outside the mutant
  set and F3's caveat that one gate cannot fail.

---

## 9. Sentences to rewrite

1. **Abstract, ~line 59** — "No criterion definable from one-boundary data
   can accept one and reject the other." → *"No isomorphism-covariant
   criterion — and every object constructed here is one — can accept one and
   reject the other."*
2. **Theorem 4.6 statement, ~line 713** — same substitution; and add the
   hypothesis explicitly: *"for criteria that are covariant under admitted
   reversible operational equivalences (as every object of this paper is, by
   #111 Cor 5.6)."* If the unrestricted form is wanted, the class of
   admissible criteria must be defined and the premise "operational
   one-boundary data = isomorphism-invariant data" must be stated and gated.
3. **§6, ~line 872** — "Theorem 4.6 shows it could not have been rejected at
   this scope" → "…could not have been rejected by any covariant criterion at
   this scope, and every criterion this construction can express is covariant."
4. **§5.3, ~line 808** — "The centre dimension is computed for each fixture by
   an exact commutant solve, never typed" → *"For each fixture the centre
   dimension is computed by an exact commutant solve rather than read off the
   declared block structure; the fixtures themselves are declared
   representatives of the committed isomorphism classes, which by Theorem 4.6
   is all the construction can see."*
5. **Theorem 4.5, ~line 674** — "so that the manufactured record is the atom
   instrument of $A_P$" → note the sink: the computed instance is the atom
   instrument of $A_P\oplus\mathbb C_{\text{sink}}$ (4 atoms for $2{+}1{+}1$,
   3 for $2{+}2$), per the #103 adjudication's correction. As written, the
   theorem statement's object (3 atoms) and the reported instance (4 atoms)
   are different records.
6. **§2.2, ~line 288** — "because $\Phi$ is unital and $\sum_sq'_s=1$" →
   *"because $M$ is complete, $\sum_rz_r=1_S$"* (F6).
7. **§2.2, new paragraph after Definition 2.3** — record the K2 adjudication:
   the flag-retaining ("measure-and-broadcast") readings of the literal
   formula are B1 (re-collapses), B4 (empties), and B3 (read-before =
   read-after), and B3 is equivalent to Definition 2.3 by Lemma 2.4. State the
   consequent uniqueness at that scope, and soften §7's non-claim accordingly.
8. **§2.3, ~line 354** — "That is (H-avail) verbatim." → keep the claim but
   name the dictionary in one clause (*later atom ↔ later configuration,
   trace support ↔ amplitude support — equal here because
   $\operatorname{tr}(z_lF(z_k))\ge0$ admits no cancellation, CP future ↔
   unitary*), and add that `comp(F)` coincides with v12 Theorem 4.5's
   $M(U_2)$.
9. **§5.1, ~line 767** — after "all 52 records on the five-atom core are
   equally fixed", add the number: *"— including the 33 whose restriction to
   the branch labels is one of the nine inherited seams. The control's
   negative direction is that the closure selects nothing, not that it
   excludes seams."*
10. **§1.4, Discriminator gate row** — "Section 5.4 gives the exact positive
    recovery deficit that separates them" → *"…gives one exact positive
    recovery deficit ($1/4$, the no-write reset) and a block-collision
    certificate covering the remaining six."*

---

## 10. What I could not shake

Three attacks failed outright and should be recorded as such, because they
were the ones most likely to kill the unit:

- **Theorem 2.1 is not evadable.** The collapse is forced by centrality of
  the branch projections, and every flag-retaining rescue either re-collapses,
  empties, or lands back on Definition 2.3.
- **The (H-avail) identification is real.** 1,715 exhaustive comparisons, 0
  mismatches, no cancellation loophole, and the decision procedures coincide
  too.
- **$\operatorname{cl}=\operatorname{id}$ is not an artifact of the reprepare
  generators.** Recomputing the closure from the *exhaustive* family of all
  left-total sector relations at $n=2,3,4$ gives 2/2, 5/5, 15/15 fixed —
  identical to the generator computation. (The law-family question — whether
  the degeneracy is an artifact of an over-generous *admitted* class — is
  K3 and belongs to R2; I note only that my exhaustive rebuild removes the
  weaker "generators" objection.)

The unit's central honesty — that it found the answer it did not want, named
it, and proved the obstruction rather than working around it — holds up under
this lens.

---

\[
\boxed{\texttt{ACCEPT-WITH-FIXES}}
\]

**Per-rung:** (a) CONFIRMED · (b) CONFIRMED at this lens's depth ·
(c) CONFIRMED, exhaustively and from a stronger base ·
(d) CONFIRMED as a fact, evidence downgraded (F2, F3) ·
(e) CONFIRMED **only as isomorphism-covariance** (F1) · (f) CONFIRMED.

**K2 adjudication:** the collapse claim **SURVIVES**; the broadcast reading is
nondegenerate only in the form B3, and B3 **does not differ** from the adopted
availability form — it is equivalent to it.

**(H-avail) coincidence:** **EXACT**, literal not analogical, with the
dictionary verified and the cancellation loophole closed; fence it to the
availability clause and correct LOG #115.

**#103 fidelity:** **numbers faithful and correctly sourced to the superseding
adjudication; construction not re-run and not declared as such.**

*R3, frozen on delivery.*

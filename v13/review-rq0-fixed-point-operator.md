# CYCLE B HOSTILE REVIEW — R1, OPERATOR-SYSTEM LENS

**Reviewer:** R1 (operator-system lens; primary kill-shot K1).
**Protocol:** `v13/note-rq0-fixed-point-hostile-protocol.md`, commit `6effc7a`,
FROZEN before dispatch. This review is judged against that protocol only.
**Object under review:** commit `6fab072`.
**Date:** 2026-08-06.

**SHA verification (performed first, before reading the object).** All four
pinned prefixes reproduce:

| artifact | pinned prefix | recomputed sha256 | |
|---|---|---|---|
| `paper-rq0-task-record-fixed-point.md` | `9afc0ad8578e` | `9afc0ad8578ea29f6cf5cb1e49c97dd6…` | MATCH |
| `code/rq0_l0_fixed_point_exact.py` | `c77e94561d14` | `c77e94561d148cb23589a0dce69b8e0d…` | MATCH |
| `code/rq0_l0_fixed_point_output.txt` | `1d93073ff1e3` | `1d93073ff1e393f00c22a0c7bbc6c6a5…` | MATCH |
| `code/rq0_l0_fixed_point_receipt.json` | `eef553549a38` | `eef553549a3821cc035574538cfc56e4…` | MATCH |

The two output artifacts carry a filesystem mtime later than the paper yet
hash to the pinned values. That is an unplanned corroboration of the
determinism claim of §8: the run was repeated and reproduced byte-identical
outputs. I did **not** execute the unit's code (it writes into the repo, and
the repo is read-only to me); the determinism claim is therefore confirmed by
hash identity rather than by my own re-run, and I flag that as the basis.

**Discipline statement.** All my arithmetic is exact (`fractions.Fraction`
and a hand-rolled Gaussian-rational class), interpreter
`/opt/homebrew/bin/python3.13`, own code in the session scratchpad only
(`…/scratchpad/r1cb/`: `qc.py`, `r1_operator.py`, `r1_combinat.py`,
`r1_k1.py`). **I imported nothing from the unit's code**; every structure —
partition lattice, sector criterion, collision components, `Pres`, `Core`,
`cl`, the operator systems, the Choi matrices, the commutant solves — was
rebuilt from the paper's prose definitions. No child agents. No git
mutations. This file is the only file I have written in the repo.

**Self-correction disclosed.** My first `Core` implementation took the
*coarsest* rather than the *finest* preserved record, and produced 10 spurious
mismatches against the paper (`G2-03b`, `G1-09`, `Prop 4.1`). The bug was
mine; the paper was right. After correction all 10 agree. I record this
because a reviewer who reported those as findings would have manufactured
four false negatives against a correct unit.

---

## 0. Verdict

**ACCEPT-WITH-FIXES.**

Every load-bearing number in the paper reproduced under independent exact
recomputation: **78 of 78 comparisons match, zero numerical errors.** The G0
collapse, the Galois machinery, the `cl = id` characterization, the
discriminator failure and the verdict name all survive my attack. The
registered outcome `RQ0-L0-BLOCKED-AT-DE-SMUGGLING` is correct and correctly
instantiated.

The fixes are not numerical. They are **one high-severity scope defect and one
high-severity measurement defect, both located in §4.5 — the one-boundary
impossibility theorem and the gate that certifies it.** Theorem 4.6 asserts an
admissibility premise that it does not measure, that #111 does not supply, and
that is *false under a law the paper itself constructs two sections earlier*;
and gate `G2-12`, the sole computational support for the headline finding
`G2_one_boundary_desmuggling_impossible`, computes something strictly weaker
than its own description and cannot fail. Neither defect touches the verdict,
because the verdict rests on Theorem 4.5 (the manufactured measure survives),
which is computed and which I confirm. Theorem 4.6 is the *explanation*, not
the *ground*. It must be rescoped, not retracted.

---

## 1. K1 — THE ADMITTED-MAP PREMISE (primary kill-shot): **PREMISE FAILS AS STATED; THEOREM RESCOPED, NOT KILLED**

K1 asks: is the relabelling permutation genuinely inside the admitted class of
the committed law, not merely unitary over ℤ? And: can admissibility be
consistently restricted to exclude it *without* breaking the earned #111
rungs? K1 requires me to decide. **I decide: yes, it can. The premise is a
genuine, unmeasured, law-relative hypothesis, and the theorem's stated scope
collapses.**

### 1.1 What the proof actually asserts

Theorem 4.6's proof (paper lines 717–721):

> "Choose a unitary \(V\) with \(VP_rV^*=Q_r\); it exists precisely because
> the rank multisets agree. Conjugation by \(V\) is an admitted reversible map
> carrying \(A_P\) onto \(A_Q\), the admitted law onto the admitted law, and
> the core atoms bijectively onto the core atoms."

The first sentence is linear algebra and is true: equal rank multisets give a
unitary intertwiner. The second sentence contains **three** distinct claims,
of which only the third is licensed:

1. conjugation by \(V\) is **admitted** — asserted, never measured;
2. it carries **the admitted law onto the admitted law** — asserted, never
   measured, and strictly stronger than (1);
3. it permutes the core atoms — true, and the only part `G2-12` checks.

Claims (1) and (2) are exactly the inference that #111 forbids. #111 §9.1
("Algebraically available but physically unavailable") exhibits \(A=\mathbb
C^2\) under a law whose coordinate filters are not admitted, so that
\(\mathfrak B_{\mathrm{op}}(A)=\{0,I\}\) while the algebraic centre has
dimension 2, and concludes verbatim: *"Thus admission is measured rather than
inferred from algebraic existence."* **This paper re-runs that very control as
its own §5.3 and gate `G3-3c`,** reporting `restricted_law_core_atoms: 1`
against `algebraic_centre_dim: 2`, and writes in its own §5.3: *"Admission is
measured, not inferred from algebraic existence."* Theorem 4.6 then performs
precisely the inference its own control forbids.

Nor does the cited authority supply the premise. #111 Cor 5.6 reads in full:

> "Every **admitted** reversible complete-order automorphism \(g:S\to S\) acts
> by \(P\mapsto gPg^{-1}\) on \(\mathfrak B_{\mathrm{op}}(S)\) and therefore
> permutes its atoms."

Its hypothesis *is* admission. Citing it to establish admission is circular.
And #111 §9.3 states its own symmetry control as "For \(\mathbb C\oplus\mathbb
C\) **with the full standard law**" — #111 itself flags that the swap's
admission is law-relative. A second, subtler point: Cor 5.6 concerns
automorphisms \(g:S\to S\) of **one** boundary, whereas Theorem 4.6 needs an
isomorphism between **two** boundaries \(A_P\) and \(A_Q\). The citation is a
scope stretch even before admissibility is raised.

### 1.2 My construction: a law that excludes the permutation and breaks nothing

Take the boundary \(S=\mathbb C^5\) — the paper's own corrected eraser minimum
and the very fixture used in its §4.5 witness. Define the committed future law
\(L_R\) to be the composition closure of the reprepare channels
\(\{R_\pi\}\) that the paper's **own condition R** demands, one per record.
Computed exactly:

| quantity | value |
|---|---|
| records on \(\mathbb C^5\) | 52 |
| reprepare futures supplied by condition R | 52 |
| composition-closed admitted law \(L_R\) | **120** sector maps |
| admitted **reversible** futures in \(L_R\) | **1** — the identity alone |
| nontrivial admitted atom permutations | **0** |
| Theorem 4.6's \(V=(1,2,3,4,0)\) admitted? | **False** |
| records fixed by \(\operatorname{cl}\) under \(L_R\) | **52 / 52** |

The reason is structural, not numerical: \(R_\pi\) is injective on sectors iff
\(\pi\) is discrete, in which case \(R_\pi=\mathrm{id}\); every other generator
is non-injective, and any composite involving a non-injective map is
non-injective. So \(L_R\) contains no nontrivial permutation, ever.

Now check that nothing earned is broken:

- **Condition R** holds by construction, so **Theorem 4.2 is untouched** — I
  recomputed `cl` under \(L_R\) and got 52/52 records fixed, exactly the
  paper's result.
- **#111 Thm 5.4 (finite atomic operational core) and Cor 5.5 (sharpness)**
  require closure of the admitted **instruments** under sequential composition
  and retained classical coarse-graining (#111 §9.2). \(L_R\) restricts
  **futures** only. The five-atom core and the sharpness corollary survive
  verbatim.
- **#111 Cor 5.6** holds vacuously: its hypothesis has only the identity as an
  instance under \(L_R\), and the identity permutes atoms trivially.

So admissibility *is* consistently restrictable, and the earned #111 rungs
survive intact. Per K1's own criterion, **the theorem's scope collapses.**

### 1.3 The paper refutes its own premise, two sections earlier

The construction above is not even necessary. **Proposition 4.1 and gate
`G2-02` of this very paper compute with "a law admitting only the identity
future."** Under that law the admitted reversible futures are exactly
\(\{\mathrm{id}\}\) and \(V=(1,2,3,4,0)\) is not admitted — I confirmed both.
Theorem 4.6 is tagged `[FIN]` (the full finite one-boundary earned scope) with
no law hypothesis, and is therefore asserted over a law the paper itself
constructs, runs, and gates, and in which its premise is false.

Under a law with trivial admitted automorphism group, covariance constrains
nothing, so the theorem's *conclusion* — "no criterion definable from
one-boundary data can accept one and reject the other" — also fails, not
merely its proof: a label-dependent predicate is then "definable from
one-boundary data" in the theorem's own sense (the triple (boundary, admitted
law, admitted instruments)). Such a predicate is of course physically
objectionable, and #111 §9.3 warns against breaking symmetry "by a lexical
label" — but that objection is an *additional* argument the paper does not
make, not something Theorem 4.6 establishes.

### 1.4 Decision

**The theorem does not die; it rescopes.** On the committed fixtures the law
is the standard finite channel law, which contains every unitary conjugation,
so the premise is satisfied and Theorem 4.6 is *true where it is run*. What is
wrong is the `[FIN]` tag and the unrestricted sentence. The theorem must carry
its admissibility hypothesis explicitly, and the hypothesis must be named as a
measured property of the committed law — the same standard the paper applies
to itself in §5.3.

---

## 2. Findings, ranked by severity

### F1 — HIGH — Theorem 4.6 asserts an unmeasured, law-relative admissibility premise (K1)

As adjudicated in §1. The premise "conjugation by \(V\) is an admitted
reversible map carrying the admitted law onto the admitted law" is asserted
from the existence of \(V\) as a unitary. #111 §9.1 forbids that inference;
#111 Cor 5.6 presupposes rather than supplies it; the paper's own §5.3/`G3-3c`
control states the prohibition; and the paper's own Prop 4.1/`G2-02` law
falsifies the premise. **Fix: add the hypothesis, retag, and disclose the
exception.** Replacement text in §5.

### F2 — HIGH — Gate `G2-12` does not measure its own claim and cannot fail

The gate's description (code lines 1715–1719, reproduced verbatim in the
receipt) asserts a **two-boundary** statement: "the corrected eraser boundary
C^5 (a legitimately derived record) and a manufactured 5-outcome PVM boundary
are carried onto each other by an admitted reversible map". Its computation
(code lines 1699–1723) is:

```
n5 = 5 ; perm = [1, 2, 3, 4, 0] ; V = permutation matrix
unitary_ok = meq(mmul(madj(V), V), mid(n5)) and meq(mmul(V, madj(V)), mid(n5))
legit = FIXTURES["C5"]
for k in range(n5):
    img = mmul(mmul(V, legit.central_projection([k])), madj(V))
    hit = [l for l in range(n5) if meq(img, legit.central_projection([l]))]
```

Three defects, each independently sufficient:

1. **No manufactured boundary is ever constructed.** `FIXTURES["C5"]` — the
   legitimate eraser minimum — is the only algebra in the gate. The second
   object of the claim does not appear in the computation at all.
2. **The map exhibited is an automorphism of one boundary, not an isomorphism
   between two.** Conjugation by a permutation matrix carries the diagonal
   algebra onto itself. If the "manufactured 5-outcome boundary" is literally
   \(\mathbb C^5\), then the permutation is decorative — the identity map
   would witness the claim equally well — and the load-bearing content is the
   coincidence of sector type, not the permutation.
3. **The gate cannot fail.** `unitary_ok` and `bijection` are unconditionally
   true for *every* permutation matrix; I ran six and all pass trivially. The
   gate has zero discriminating power. And no mutant targets it: `MUTANT_TABLE`
   covers `A07, A16, A12, A26, A14, A28` — **6 of 34 anchors and 0 of 57
   gates**. So the paper's single load-bearing new theorem carries no
   falsification coverage whatsoever.

This is a **prose-vs-gate violation**, a declared common gate of the protocol
("no claim broader than its measurement"). It matters more than usual because
`G2-12` is the sole support for `FINDINGS["G2_one_boundary_desmuggling_impossible"]
= true`, one of the seven headline findings in the receipt, and for the
paper's §4.5 sentence "The concrete witness recorded here is the sharpest
available" — which is not supported by anything computed.

Note also that the gate verifies "unitary over ℤ", which is precisely the
predicate K1 identifies as the wrong one. The code checks the mathematical
existence of \(V\); the claim needs its *admission*.

### F3 — MEDIUM — the `cl = id` degeneracy tracks the admitted future class continuously; only the endpoints are reported (K3, attempted)

I attacked K3 as the protocol requires of every reviewer. The paper's proved
direction is sound and I confirm it: **\(R_\pi\) admitted \(\Rightarrow\)
\(\pi\) fixed**, hence R \(\Rightarrow\) `cl = id`. I tested the inclusion
\(\{\pi: R_\pi \text{ admitted}\}\subseteq \operatorname{fixed}(\operatorname{cl})\)
on **600** randomly drawn admitted-reprepare families at \(n=2,3,4\):
**0 violations**. The converse is **false** — the inclusion is strict in
**185/600** trials (witness at \(n=3\): admitted futures
\(\{(0,0,2),(0,1,0),(0,1,2)\}\) give predicted fixed set
\(\{(0)(1)(2),\,(01)(2),\,(02)(1)\}\) but actual fixed set additionally
contains the trivial record \((012)\)).

I initially conjectured exact equality and **it was refuted by my own test**;
I record the refutation rather than the conjecture.

Measured family-sensitivity at \(n=4\) (15 records): full reprepare closure
15/15 fixed; identity-only law 1/15; with \(k\) reprepares admitted the fixed
count is \(\geq k\) and interpolates. So "every admitted record is a fixed
point" is a **restatement of the generosity of condition R**, not a discovery
about records. The paper does disclose the far endpoint (Prop 4.1, `G2-02`)
and deserves credit for it, but it frames the degeneracy as a property of the
closure rather than as a measurement of the admitted class. This
**strengthens** the verdict — the vacuity is worse than reported — and costs
the paper nothing to say.

### F4 — MEDIUM — the scope box claims one boundary; Definition 2.3 and Prop 2.5 quantify over a second

The scope box states "Boundaries | exactly one, fixed in advance". But
Definition 2.3 requires "an admitted complete instrument \(M'=\{m'_s\}\) on
\(S'\)", and Prop 2.5's converse direction reasons over "the later atoms" and
silently uses #111's classification of admitted instruments (records =
partitions of the core atoms, #111 Thm 5.4/Cor 5.5) **on \(S'\)**. That
classification is only available if \(S'\) is itself inside the earned #111
ancilla-saturated, instrument-complete scope, which the scope box never
declares. The implementation sidesteps this by giving \(S'\) the same atom set
as \(S\) (sector relations are on \([n]\times[n]\)). Fix: declare \(S'\) and
inherit the #111 scope for it, or state that admitted futures are
endomorphisms of \(S\). No number moves either way.

### F5 — LOW — §5.2 reports the dimension but §111 Thm 8.2 needs "only the scalars"

The paper writes: "The intersection \(S\cap Z(C^*_e(S))\) is computed by exact
linear solve to have dimension 1." #111 Thm 8.2 requires the strictly stronger
"That intersection contains only scalar multiples of the unit." The inference
is valid — \(s_0=(I,I)\) is central and lies in \(S\), so dimension 1 forces
the intersection to be exactly \(\mathbb C\cdot 1\) — but the paper leaves the
step implicit. I verified both facts independently: the solve has kernel
dimension 1, and the solution space satisfies \(b=c=0\), i.e. the intersection
is exactly \(\mathbb C\,s_0\). The receipt (`G3-2c`) is already more precise
than the paper; import its wording.

### F6 — LOW — 761,108 is stated in the paper with no receipt row

The paper's §3.1 states "761,108 membership tests in total". This string
appears nowhere in the receipt or the output. It is the sum
\(18+1{,}715+759{,}375\) of three receipt rows (`G1-00-n2/n3/n4`); I verified
the arithmetic. The protocol's common gate is "every number in the paper
carried by a receipt row". Either add the total to the receipt or mark it in
the paper as a stated sum of the three rows. Cosmetic.

### F7 — LOW — falsification coverage should be disclosed, not enlarged

`c = MUTANT_OVERRIDE.get(aid, computed) if MUTANT else computed` (line 658):
the mutants substitute the *reported* value at the anchor comparison site;
they do not perturb any derivation. The paper's §8 describes this accurately
("Six mutants each break exactly one committed anchor … each exits 1 with a
printed anchor failure") and I record **no misstatement**. But the reader
should be told what the self-test does and does not cover: it certifies the
anchor harness is live; it exercises 6 of 34 anchors and **no gate at all**,
including the discriminator gates `G2-10/G2-11` and the impossibility gate
`G2-12`. One sentence of disclosure.

### K2 and K4 — attempted (other reviewers' primaries), briefly

**K2 (measure-and-broadcast reading of \(D_M\)) — the collapse survives, not
rescoped.** Under the broadcast reading \(D_M^{\mathrm{bc}}(\rho)=\sum_r
m_r(\rho)\otimes|r\rangle\langle r|\) is not an endomorphism of \(S\), so
\(\lVert F-F\circ D_M\rVert_{\mathrm{Test}}\) does not typecheck unless \(F\)
is extended to system-plus-flag — and that extension requires a tensor
factorization, which the scope box explicitly forbids ("no
composition/tensor"). Granting the extension anyway, the formula does become
nondegenerate, but it then expresses *"\(F\) cannot see the record"*
(blindness), not *"\(F\) preserves the record"* (availability) — a different
condition, and one that would exclude the intra-block unitary the paper
correctly wants inside. The literal formula **as the paper defines it** —
\(D_M\) is "the outcome-forgetting composite" — collapses exactly as claimed,
because #111 Def 4.1 clause (3) *is* \(\sum_r m_r = I_S\). I read that clause
directly. Theorem 2.1 is a one-line consequence of an inherited axiom and is
correct.

**K4 (criterion-class quantifier) — real defect, confirmed.** The paper's
sentence is an unrestricted impossibility ("No criterion definable from
one-boundary data can accept one and reject the other"); what the proof
delivers is isomorphism-covariance ("every object constructed in this paper is
defined from the triple … A covariant predicate takes the same value on
isomorphic arguments"). The class of criteria is never defined, and no
quantifier over it is discharged. Combined with F1 this makes the §4.5
sentence doubly overstated. My replacement in §5 fixes both at once.

---

## 3. Independent numbers — claimed vs mine

Every row rebuilt from the paper's prose, exact arithmetic, nothing imported
from the unit. **78 comparisons, 78 matches, 0 mismatches.** Load-bearing
selection below (full logs in the scratchpad).

### 3.1 Operator-system core (my assigned lens) — 36/36

| # | quantity | claimed | mine | |
|---|---|---|---|---|
| 1 | \(s_2^2\) second-block coefficient (A15) | 5 | 5 | ✓ |
| 2 | \(s_2^2\) first block \(=I\) | \(I\) | \(I\) | ✓ |
| 3 | \(z_1=(5s_0-s_2^2)/4\) | \((I,0)\) | \((I,0)\) | ✓ |
| 4 | \(z_2=(s_2^2-s_0)/4\) | \((0,I)\) | \((0,I)\) | ✓ |
| 5 | \(\lVert s_2\rVert^2\) full (A16) | 5 | 5 (blocks 1, 5) | ✓ |
| 6 | \(\lVert s_2\rVert^2\) block-1 only (A17) | 1 | 1 | ✓ |
| 7 | \(\lVert -3s_1+s_2\rVert^2\) full (A18) | 10 | 10 (blocks 10, 8) | ✓ |
| 8 | \(\lVert -3s_1+s_2\rVert^2\) block-2 only (A19) | 8 | 8 | ✓ |
| 9 | \(\dim(S\cap Z(C^*_e(S)))\) (A20) | 1 | 1 | ✓ |
| 10 | that intersection \(=\mathbb C(I,I)\) | scalars | \(b=c=0\) ⟹ scalars | ✓ (F5) |
| 11 | \(\varphi_\lambda(s_0),\varphi_\lambda(s_1),\varphi_\lambda(s_2)\) (A21–23) | 1, 0, 0 | 1, 0, 0 | ✓ |
| 12 | \(\varphi_\lambda(z_1)\) at \(\lambda=3/7\) (A24) | 3/7 | 3/7 | ✓ |
| 13 | \(\varphi_\lambda\) constant on \(S\), varies on \(z_1\) | yes / yes | yes / yes (4 weights) | ✓ |
| 14 | centre dim \(\mathbb C^2\) | 2 | 2 | ✓ |
| 15 | centre dim \(\mathbb C^5\) | 5 | 5 | ✓ |
| 16 | centre dim \(M_2\oplus\mathbb C\) | 2 | 2 | ✓ |
| 17 | centre dim \(M_4\oplus\mathbb C\) | 2 | 2 | ✓ |
| 18 | centre dim manufactured 2+1+1 + sink (A10) | **4** | **4** | ✓ |
| 19 | centre dim manufactured 2+2 + sink (A11) | **3** | **3** | ✓ |
| 20 | rank \(J(\mathrm{id})\) on \(M_2,M_3,M_4\) (A25) | 1, 1, 1 | 1, 1, 1 | ✓ |
| 21 | \(\langle\psi^-|J(P)|\psi^-\rangle\) (A26) | \(-1/2\) | \(-1/2\) | ✓ |
| 22 | eraser minimum atom count (A07) | 5 | 5 | ✓ |
| 23 | preserving minimum atom count (A06) | 1 | 1 | ✓ |
| 24 | bundled/tagged minimum (A08) | 5 | 5 | ✓ |
| 25 | Thm 3.7 antitonicity refutation | 1 → 5 | 1 → 5 | ✓ |
| 26 | tomographic core distribution (A12) | (1/4, 3/4) | (1/4, 3/4) | ✓ |
| 27 | \(\mathrm{TV}(p_0,p_1)\) (A27) | 1/2 | 1/2 | ✓ |
| 28 | optimal recovery deficit (A05) | 1/4 | 1/4 (= bound, tight) | ✓ |
| 29 | off-diagonal modulus squared | 3/16 | 3/16 | ✓ |
| 30 | squared trace-norm coherence loss (A28) | 3/4 | 3/4 | ✓ |

Centre dimensions were obtained by an exact commutant solve over the Gaussian
rationals (solve \([x,b]=0\) for \(x\) in the algebra, nullity by exact
elimination), never typed from the block structure — the same standard the
paper sets for itself.

### 3.2 Combinatorial / closure layer — 42/42

| # | quantity | claimed | mine | |
|---|---|---|---|---|
| 31 | Bell 1..5 by enumeration | 1,2,5,15,52 | 1,2,5,15,52 | ✓ |
| 32 | Bell 1..5 by Bell triangle (independent) | 1,2,5,15,52 | 1,2,5,15,52 | ✓ |
| 33 | left-total relations \(n=2,3,4\) | 9, 343, 50625 | 9, 343, 50625 | ✓ |
| 34 | lemma-soundness tests \(n=2,3,4\) | 18, 1715, 759375 | 18, 1715, 759375 | ✓ |
| 35 | lemma mismatches \(n=2,3,4\) | 0, 0, 0 | 0, 0, 0 | ✓ |
| 36 | total membership tests \(n\le4\) | 761,108 | 761,108 | ✓ (F6) |
| 37 | \(n=5\) declared subfamily size | 84,375 | 84,375 | ✓ |
| 38 | \(n=5\) tests | 4,387,500 | 4,387,500 | ✓ |
| 39 | distinct preserved sets \(n=2..5\) | 2, 5, 15, 52 | 2, 5, 15, 52 | ✓ |
| 40 | `cl = id` from **exhaustive** futures \(n=2,3,4\) | 2/2, 5/5, 15/15 | 2/2, 5/5, 15/15 | ✓ |
| 41 | strict refinement pairs \(n\le5\) | 359 | 359 | ✓ |
| 42 | \(R_\pi\) witness valid on all of them | 359 | 359 | ✓ |
| 43 | closed records \(n=2,3,4\) | 2, 5, 15 | 2, 5, 15 | ✓ |
| 44 | closed families \(n=2,3,4\) | 2, 5, 15 | 2, 5, 15 | ✓ |
| 45 | inherited coarse seams (A14) | 9 | 9 (6 of 2+1+1, 3 of 2+2) | ✓ |
| 46 | discrete partition is one of the nine | false | false | ✓ |
| 47 | Prop 4.1, cl(trivial) under R, \(n=1..5\) | trivial | trivial | ✓ |
| 48 | Prop 4.1, identity-only law, \(n=1..5\) | full core | discrete = full core | ✓ |

The \(n=5\) subfamily size is *derivable*: with at most one multi-valued atom,
\(5^5 + 5\cdot 26\cdot 5^4 = 3{,}125 + 81{,}250 = 84{,}375\). The declared
scope tag is honest.

### 3.3 Exactness / receipt integrity (independent AST scan)

| quantity | claimed | mine | |
|---|---|---|---|
| float literals in the source | 0 | **0** | ✓ |
| float-producing calls | 0 | **0** | ✓ |
| imports | exact/stdlib only | `__future__, argparse, ast, fractions, hashlib, itertools, json, pathlib, subprocess, sys, time` | ✓ |
| gates | 57/57, 0 failed | 57 entries, 57 passed, `failed: []` | ✓ |
| anchors | 34/34 | 34 entries, 34 passed | ✓ |
| anchor type violations | 0 | `[]` | ✓ |
| paper-vs-receipt spot check | — | 26 headline numbers checked; all present bar the derived 761,108 (F6) | ✓ |

I ran my own AST walk over the unit's source rather than trusting its
self-audit; the sweep is clean.

### 3.4 Common gates

- **Scope tags:** present on every numbered result (`[FIN]`, `[EXH-4]`,
  `[FIX]`). **One is wrong:** Theorem 4.6 carries `[FIN]` but requires an
  undeclared law hypothesis (F1).
- **Forbidden vocabulary:** clean. `tensor` 0 hits; `locality`, `overlap`,
  `topology`, `manifold` appear only inside the non-claims list (line 908);
  `causal`, `spacetime`, `Lorentz` only in the non-claims (line 909) and the
  Markov disclaimer (line 92); `gravity`/`QCD` only in the non-claims (line
  910); `QFT` 0 hits. "Markov" appears 4 times, always as the pre-registered
  outcome name, and carries its disclaimer at lines 90–93. "Composition"
  occurs only as *sequential flagged composition* (a declared inherited
  postulate) and *the composite reading* (of a map) — neither is a
  two-boundary combination claim.
- **Degenerate-satisfaction disclosures:** kept and honest. §4.2/§4.3 state
  the closure "partitions nothing" and "Existence here is not evidence of
  selection; it is evidence of vacuity"; §5.1's negative direction discloses
  that all 52 records are equally fixed so the closure prefers none. The paper
  does not hide its own emptiness. Credit where due.
- **Deviations (1)–(8):** the LOG records them only in aggregate ("the pin's
  ambiguous closure read BOTH ways (A: availability adjoint; B: #111 core)
  with the split verdict the honest result"). Both readings are in fact
  carried through the paper (§4.2 and §4.3) and both are gated, so the
  substantive deviation is **fix-real and already repaired in place**. I
  cannot itemize (1)–(8) individually because no enumerated list exists in the
  frozen artifacts; I flag that as a process gap for the adjudicator, not a
  defect of the unit.
- **Anchors' parent values:** A15–A26 trace to #111 §8.1/§8.3/§6.1/§3.3;
  A06–A08, A10–A11, A14, A27–A28 to #103. I re-derived the #111-side values
  from #111's own text (S's generators, Thm 8.2, Cor 5.5, Cor 5.6, Def 4.1)
  and the #103-side values from the committed likelihoods, and they agree.
- **Determinism:** confirmed by hash identity of re-written artifacts (see
  header), not by my own execution.

---

## 4. Per-rung confirmation lines

Required by the protocol; exactly one disposition each.

**(a) The G0 collapse — CONFIRMED.** \(D_M=\sum_r m_r=I_S\) is literally
clause (3) of #111 Def 4.1, which I read directly ("forgetting the flag is
nondisturbing: \(\sum_r m_r = I_S\)"). Theorem 2.1 is a substitution from an
inherited axiom and is correct. The collapse is not formal only: the no-write
reset sits inside the literal family with optimal recovery deficit exactly
\(1/4\), which I recomputed independently (exhaustive exact search over a
rational grid, meeting the analytic bound \(\mathrm{TV}(p_0,p_1)/2\) with
equality at \(d=(1/2,1/2)\)). The literal formula is correctly discarded.

**(b) The Galois connection for the availability reading — CONFIRMED.** I
rebuilt the sector criterion from Definition 2.3's prose and verified Lemma
3.2 exhaustively over all left-total relations at \(n=2,3,4\) (9 / 343 /
50,625 relations; 761,108 tests; **zero mismatches**, matching the claim
row-for-row). Antitonicity of `Pres`, well-definedness and antitonicity of
`Core`, the two-sided adjunction, and the closure laws all reproduce; closed
records and closed families are in bijection with matching counts 2, 5, 15.
The operator-theoretic scaffolding is sound on my own check: Lemma 2.4 is
exactly Choi's multiplicative-domain criterion for a unital CP map
(\(\Phi(p^*p)=\Phi(p)=\Phi(p)^2=\Phi(p)^*\Phi(p)\)), and Prop 3.4's use of it
is legitimate because the later outcome effects commute by #111 Thm 5.2 and
their products are admitted by the declared sequential-closure postulate. I
also checked Prop 2.5's ⟸ direction more carefully than the paper writes it:
for \(\rho\) supported in sector \(k\) one has \(\rho\le z_k\), hence
\(\mathrm{tr}(z_l F(\rho))\le \mathrm{tr}(z_l F(z_k))=0\) off the support, and
an effect with expectation 1 on \(z_B\) and 0 on \(1-z_B\) is \(z_B\). The
proof is terse but correct.

**(c) The `cl = identity` degeneracy — CONFIRMED, with F3 attached.** Verified
two independent ways as the paper claims: from the \(R_\pi\) witness on all
359 strictly-refining pairs at \(n\le5\), and from the **exhaustive** future
family at \(n=2,3,4\) (2/2, 5/5, 15/15). Fixed-point counts 1, 2, 5, 15, 52
out of 1, 2, 5, 15, 52 reproduce. The degeneracy is real. F3 adds that it is
exactly as generous as condition R and interpolates with the admitted class.

**(d) The discriminator failure — CONFIRMED.** The manufactured record is the
atom instrument of the manufactured boundary; centre dimensions 4 and 3 (which
I recomputed by exact commutant solve) give four-atom and three-atom
manufactured records among 15 and 5 records, all fixed. Under reading A it is
a fixed point because `cl` is the identity; under reading B it is the unique
fixed point because the identity future preserves every record, forcing
\(B_{\operatorname{Pres}(M)}=S\). Theorem 4.4's argument is correct and needs
no admissibility premise. **The closure does not de-smuggle, and the paper
reports this as its finding rather than working around it. That is the right
call and the paper deserves credit for making it.**

**(e) The one-boundary impossibility theorem — NOT CONFIRMED AS STATED.**
Confirmed only in the rescoped form of §5's replacement. The premise is
unmeasured and law-relative (F1); the certifying gate does not measure the
claim and cannot fail (F2); the criterion class is never defined (K4). The
mathematical kernel — a covariant predicate takes equal values on isomorphic
arguments — is trivially true and survives; everything the theorem adds beyond
it is unearned at `[FIN]` scope.

**(f) The verdict name `RQ0-L0-BLOCKED-AT-DE-SMUGGLING` — CONFIRMED as the
correct pre-registered instantiation.** It instantiates
`RQ0-L0-BLOCKED-AT-⟨object⟩` from the pin, with the un-typed object being a
task-independent selector on the fixed-point set. That object genuinely cannot
be typed at this scope: `cl` is the identity, so the fixed-point condition
induces no selection, and this is established by Theorems 4.2 and 4.5, neither
of which depends on Theorem 4.6. The two sibling outcomes are correctly
dispositioned — `NO-NONTRIVIAL-FIXED-POINT` **refuted** (nontrivial fixed
points exist wherever the core has ≥2 atoms; I confirmed the fixture counts),
and `W3-OPERATIONAL-MARKOV-BOUNDARY` **not earned** (its third condition
fails). Registering a blocked outcome rather than dressing vacuous existence
as a positive result is the honest disposition, and I endorse it. **The
verdict stands under all my attacks.**

---

## 5. Sentences to rewrite, with replacements

**(1) §4.5, Theorem 4.6 statement — the last sentence.** Replace

> "Hence no criterion definable from one-boundary data can accept one boundary
> and reject the other."

with

> "Hence no criterion that is covariant under the admitted reversible
> operational equivalences can accept one boundary and reject the other,
> whenever the committed law admits such an equivalence carrying one
> boundary's triple (boundary, admitted law, admitted instruments) onto the
> other's. This hypothesis is a measured property of the committed law, not a
> consequence of the rank multisets agreeing; it holds for the standard finite
> channel law of every committed fixture, and it fails, for instance, under
> the identity-only law of Proposition 4.1."

**(2) §4.5, Theorem 4.6 scope tag.** Replace `[FIN]` with

> `[FIN]`, `[LAW-HOM]` — additionally requiring that the committed law admit
> the atom-permuting reversible equivalence; see the hypothesis above.

**(3) §4.5, proof, second sentence.** Replace

> "Conjugation by \(V\) is an admitted reversible map carrying \(A_P\) onto
> \(A_Q\), the admitted law onto the admitted law, and the core atoms
> bijectively onto the core atoms."

with

> "Conjugation by \(V\) is a reversible complete-order isomorphism carrying
> \(A_P\) onto \(A_Q\) and the core atoms bijectively onto the core atoms.
> Whether it is *admitted*, and whether it carries the admitted law onto the
> admitted law, is a further condition on the committed law and is assumed
> here as hypothesis `[LAW-HOM]`; by §5.3 and #111 §9.1 admission is measured,
> not inferred from algebraic existence, so this cannot be read off from the
> existence of \(V\)."

**(4) §4.5, the witness paragraph.** Replace

> "The concrete witness recorded here is the sharpest available: the corrected
> eraser minimum \(\mathbb C^5\) … is carried onto a manufactured five-outcome
> boundary by the exact permutation \(V\) of the cyclic shift \((1,2,3,4,0)\),
> verified unitary over the integers, whose induced map on core atoms is a
> bijection. The two boundaries are operationally the same object."

with

> "The concrete witness recorded here is a sector-type coincidence, not an
> independent construction: the corrected eraser minimum \(\mathbb C^5\) and a
> manufactured five-outcome boundary have the same sector type, so any
> permutation of the five atoms — we record the cyclic shift \((1,2,3,4,0)\),
> verified unitary over the integers — is a complete-order isomorphism between
> them. What is computed is that \(V\) is unitary and that conjugation by it
> permutes \(\mathbb C^5\)'s central projections; the manufactured boundary is
> not separately constructed, and \(V\)'s admission is not measured."

**(5) §4.5, closing.** Replace

> "A closure that rejected the manufactured one would have to reject the
> legitimate one."

with

> "Under `[LAW-HOM]`, a covariant closure that rejected the manufactured one
> would have to reject the legitimate one."

**(6) §5.2, the intersection sentence.** Replace

> "The intersection \(S\cap Z(C^*_e(S))\) is computed by exact linear solve to
> have dimension \(1\)."

with

> "The intersection \(S\cap Z(C^*_e(S))\) is computed by exact linear solve to
> have dimension \(1\); since the unit \(s_0=(I,I)\) is central and lies in
> \(S\), the intersection is therefore exactly \(\mathbb C\,s_0\), which is
> the hypothesis #111 Theorem 8.2 requires."

**(7) §4.2, after Theorem 4.2.** Add

> Condition R is doing the whole of the work. The reprepare future \(R_\pi\)
> being admitted already forces \(\pi\) to be fixed, so the fixed-point set
> grows with the admitted future family and shrinks to the operational core
> alone under the identity-only law of Proposition 4.1; intermediate laws give
> intermediate fixed-point sets. "Every admitted record is a fixed point" is
> therefore a restatement of the generosity of R rather than a property of
> records. (The converse fails: fixed points can exist whose reprepare is not
> admitted.)

**(8) §8, after the falsification paragraph.** Add

> The mutants substitute the reported value at the anchor comparison site;
> they certify that the anchor harness is live and exits 1. They exercise six
> of the thirty-four anchors and none of the fifty-seven gates, so gate-level
> results — including the discriminator and impossibility gates — carry no
> falsification coverage.

**(9) Scope box, Boundaries row.** Replace "exactly one, fixed in advance"
with

> exactly one source boundary, fixed in advance; admitted futures land on a
> later boundary \(S'\), which is assumed to lie in the same declared #111
> ancilla-saturated, instrument-complete scope so that its admitted
> instruments are classified by #111 Theorem 5.4.

**(10) §3.1.** Either add a receipt row for the 761,108 total, or replace
"761,108 membership tests in total" with "761,108 membership tests in total,
the sum of the three receipted counts 18, 1,715 and 759,375."

**(11) Gate `G2-12` (code).** The gate should either construct the
manufactured boundary and exhibit the isomorphism between two independently
built objects, or be renamed and re-described to match what it computes —
e.g. "`G2-12 [SECTOR-TYPE]`: a five-outcome sector type admits a transitive
atom-relabelling group; conjugation by the cyclic shift permutes \(\mathbb
C^5\)'s central projections" — with the finding key renamed from
`G2_one_boundary_desmuggling_impossible` to something it measures. As it
stands the finding name asserts an impossibility the gate never tests.

---

## 6. What the unit got right

Recorded because a hostile review that reports only defects misrepresents the
object.

- **Zero numerical errors in 78 independent exact recomputations**, spanning
  operator norms, commutant solves, Choi ranks and expectations, minimal
  sufficient experiments, exhaustive relation sweeps and the full closure
  lattice. The exactness discipline is real: my own AST scan of the source
  found zero float literals and zero float-producing calls.
- **The G0 repair is the right move, and correctly justified.** Discovering
  that the inherited literal formula is vacuous because \(\sum_r m_r = I_S\),
  proving it, and replacing the definition with a gated nondegenerate one
  (9 in / 7 out, with the intra-block unitary specifically exhibited so that
  membership is visibly not "is the identity") is exactly the discipline the
  pin demanded.
- **Proposition 4.1 corrects the pin's and the adjudicator's own stated
  premise** that the trivial instrument is always fixed. Owning an upstream
  error inside the paper that inherits it is the behaviour one wants.
- **The verdict is the honest one.** The unit had every opportunity to
  announce "nontrivial fixed points exist" as a positive result. It instead
  reports that existence is vacuous, that the discriminator failed, and
  registers a blocked outcome. §4.2's "Existence here is not evidence of
  selection; it is evidence of vacuity" is the sentence a weaker paper would
  not have written.
- **The next obstruction is named correctly.** De-smuggling requires a scope
  in which the boundary is not given in advance. My K1 analysis independently
  supports that conclusion by a different route: at one-boundary scope the
  question of which criteria are available is itself a choice of admitted law,
  and nothing inside the boundary fixes it.

---

## 7. Verdict

**ACCEPT-WITH-FIXES.**

Fixes required before the unit's status changes: F1 and F2 (both HIGH) —
rewrites (1)–(5) and (11). Fixes recommended: F3–F7 — rewrites (6)–(10).

No number in the paper moved under my attack. The registered outcome
`RQ0-L0-BLOCKED-AT-DE-SMUGGLING` survives, because it rests on Theorem 4.5 and
Theorem 4.2, which I confirm independently, and not on Theorem 4.6, which I do
not. The unit's one load-bearing *new* theorem is over-scoped and
under-measured; the unit's *verdict* is correct, honestly reached, and should
stand.

*Frozen on delivery. No edits after this file was written.*

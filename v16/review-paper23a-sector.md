# Paper 23a blind review — Seat C (sector/category)

Date: 2026-08-22

Reviewer seat: category/sector structure. Repo read-only; this report
was produced solely from the frozen pin (#309), the candidate
(#310, SHA-256 `9cab8d2e78ee5365b0facc86ff059074f482091bbb3621cfd328939b9e247a5a`,
606 LF), the construction note
(`cc157c793cca620b680dca1d93b83a6726dee1e3b7e044647a9cffde889ea10c`),
and terminal Paper 13D (`3b91766f…`). No other seat's report was seen;
findings below were derived by rebuilding the candidate's objects from
Paper 13D prose.

Verdict: **REJECT**

Stages 1–2 are close to sound (two repairs below). Stage 3 is
structurally unsound: its central identifications contradict the
candidate's own congruence separation, and the contradiction cannot be
removed by prose substitution — one cannot simultaneously hold
Proposition A.2 (trace-shape separation) and Theorems C/D (collapse of
fusion complexes onto primitive classes). Findings most severe first;
replacement sentences verbatim where repair is possible.

## F-C1 (CRITICAL) — Theorems C/D identify fusion-complex classes with primitive classes, contradicting Proposition A.2

Defect. Theorem C asserts $a_m\otimes a_{m'}=a_{m+m'}$ where $a_n$ is
the class of the *primitive* fixture $U_{\varnothing}(n)$, proving it
by "determinism of $\Phi_s$ at unbonded sorts." But Paper 13D §7.1
defines a fusion history to *retain its tensor source value and fused
target value*: the fused complex
$\Phi_s(U_m\boxtimes U_{m'})$ traverses tensor and fusion boundaries
that the primitive $U_{\varnothing}(m+m')$ does not. By precisely the
separation mechanism the candidate itself proves in Proposition A.2
(complete reader sees every traversed boundary and intermediate
frontier; §8 vertex-tagged addresses expose them), the two complexes
are **incongruent**. Determinism of a generator never erases the
boundary it traverses — that is the same reason $U_J\ne D\circ Q_J^0$
in Paper 13D §5.1. Consequently:

1. the product of two primitive classes is not a primitive class;
   multiplication escapes the displayed class set outright;
2. "the fused class is unique for every pair" (Thm C) is false —
   the fused complex's class is a fusion-complex class, distinct from
   every $a_k$;
3. Theorem D inherits the same error at the bonded sorts;
4. the classification-table rows 3a–3e and the earned-outcome
   declaration (`P23A-FUSION-CLOSURE-FAILS`,
   `P23A-COMMON-POSITIVE-CHARACTER-NONUNIQUE`) rest on the false
   identification.

This is not a wording defect: repairing it requires either (i)
retracting Proposition A.2's trace-shape separation — destroying
stage 1's computed quotient — or (ii) rebuilding stage 3 on the
actual class set (which contains fusion- and tensor-complex classes,
staged-bracketing classes, etc.). Both exceed bounded prose repair.

## F-C2 (CRITICAL) — Class-level associativity fails under the candidate's own congruence

Defect. Even on the enlarged class set, the product
$[\chi]\otimes[\chi']= [\Phi_s(\chi\boxtimes\chi')]$ is not
associative. Compare
$L=\Phi(\Phi(\chi_1\boxtimes\chi_2)\boxtimes\chi_3)$ and
$R=\Phi(\chi_1\boxtimes\Phi(\chi_2\boxtimes\chi_3))$: the first
intermediate fused boundary of $L$ has occurrence carrier
$\{1,2\}$, that of $R$ has $\{2,3\}$; both are retained in the
respective histories (§7.1) and are separated by the complete reader
exactly as in Proposition A.2. So $[L]\ne[R]$:
coefficient associativity of $N_{xy}^z$ — invoked by Corollary C.1
("union of finite sets is associative"), Theorems C/D clause 2–3, and
Proposition E's character recursion — is unavailable at class level.
Union-of-carriers associativity holds only at the level of final
target *values*, which the candidate's own §4.4 concedes is too coarse
to be a sector statement. The semiring conclusion
($\cong(\mathbb N,+)$, indecomposable) and the continuum-of-characters
conclusion therefore stand on no proved structure.

## F-C3 (MAJOR) — Definition 2.1's aligned-pair quantification is degenerate exactly where separation is needed

Defect. Definition 2.1 quantifies over "aligned pairs"
$(f,f'=gfg^{-1})$ and $(R,R'=gRg^{-1})$. A reader on $\chi$ is a map
on $\chi$'s outcome fiber (Paper 13D §9.2); when the two complexes'
diagnostic data differ, $gRg^{-1}=R'$ cannot hold as literal map
equality across distinct fibers, so the aligned-pair set is empty and
the defining equality holds vacuously. Taken literally the definition
would merge complexes that Propositions A.1/A.2 (correctly) separate —
the congruence does not prove what stage 1 claims. The intended
relation is the Paper 13D §15 comparison pattern: push both presented
laws onto the diagonal stabilizer orbits of the shared typed
comparison object and demand equality of the pushed laws.

Replacement sentences for Definition 2.1, verbatim:

> Complexes $\chi,\chi'$ are predictively equivalent, written
> $\chi\sim\chi'$, when they are alignable by some $g$ and the
> following comparison is exact: form the ordered aligned pair
> $(\chi,\chi')$, push both presented laws onto the common
> stabilizer orbits of the shared typed comparison space exactly as
> in Paper 13D Section 15, and require equality of the two pushed
> laws on every comparison cell. Equivalently: for every legal future
> $f$ of $\chi$ with transported counterpart $f^{g}$ of $\chi'$, and
> every equivariant reader $R$ of $\chi$ with transported counterpart
> $R^{g}$ of $\chi'$ — counterparts declared by the groupoid action on
> the comparison object, not by map identity — the transported laws
> agree.

With this repair, Propositions A.1/A.2 follow (mass sits in disjoint
orbit components whenever trace shapes differ), and Lemma 2.2 and
Theorem A(1),(2),(3),(5) hold with unchanged proofs *mutatis
mutandis*; A(4) additionally needs F-C5.

## F-C4 (MAJOR) — §4.4's class-equality bullet contradicts Proposition A.2 and parent-pin control 7

Defect. §4.4 asserts "sector-class equality: yes (both land in
$[b_3]$)" for simultaneous versus staged triple fusion. Under the
candidate's own separation principle the staged and simultaneous
complexes are incongruent (distinct retained boundaries); under any
congruence coarse enough to merge them, Proposition A.2 fails. Either
way the sentence is false, and control-matrix row 1's "only
class-level equality claimed" misdeclares the disposition of parent
control 7 (simultaneous equated with staged).

No replacement sentence is offered: the correct statement is a
retraction pending the stage-3 rebuild (see F-C1/F-C2).

## F-C5 (MODERATE) — Theorem A(4) deletion clause conflates auxiliary choice with paired operation

Replacement sentence, verbatim:

> 4. *(restriction/deletion)* if $\chi\sim\chi'$ are aligned by $g$,
>    then for each occurrence $i$ of $\chi$, the deletions at $i$ and
>    at $g(i)$ give congruent complexes; consequently the uniformly
>    selected unmarked deletion laws correspond as well;

## F-C6 (MINOR) — False arithmetic sentence in §3.2

Defect. "$2^7\times 625=128$ positive traces" is false as written
($2^7\cdot625=8000$). The correct census: sixteen source tuples
$(q_0,h,c,e^0)$, four packet values compatible with each $(c,e^0)$,
two endpoints — $16\times4\times2=128$ positive labeled traces, drawn
from $16\times625$ seed combinations. Replacement sentence, verbatim:

> the labeled support has $16\times4\times2=128$ positive traces
> (sixteen source tuples, four packets compatible with each
> $(c,e^0)$, two endpoints), drawn from $16\times625$ seed
> combinations, and normalization is exact.

## Mandatory regressions (controls 3, 14, 15, 16, 17)

- Control 3 (automorphism orbit size as channel): Definitions 3.1/§4.1
  exclude orbit sizes from $N$; masses are full-orbit sums. PASS at
  stage 2; moot for stage 3 pending rebuild.
- Control 14 (representative mass): every printed mass is an orbit
  sum; tables independently recomputed (below). PASS.
- Control 15 (semiring from nonnegativity alone): FAIL — not because
  nonnegativity was abused, but because the semiring itself was not
  proved (F-C2); the control's discipline cannot rescue an unproved
  structure.
- Control 16 (character uniqueness assumed): Prop E's recursion
  presumes the failed associativity; after rebuild the character
  question is `NOT-APPLICABLE` unless an associative structure is
  first proved. CONDITIONAL-FAIL as printed.
- Control 17 (FP dimensions as odds): Cor E.1 blocks the route;
  survives. PASS.

## Independent verification performed

Recomputed exactly (rationals) from Paper 13D §§6–7: β and κ seed
censuses reproduce $B$, $C$ per column; $B^2$ recomputed; $n=1$
reachable packets = 16; $U_{\varnothing}(1)$: 128 labeled traces /
96 cells / 64 swap-fixed / six distinct masses — matching the
candidate's table elementwise, summing to 1;
$D\circ Q^0_{\varnothing}(1)$: 256 / 192 / 128 / eight masses,
matching, summing to 1; endpoint conditional $=B^2$ entrywise;
$P(\ell_{ij}{=}1)=1/2$; $(\ell_{12},\ell_{13})$ pattern uniform on
four outcomes; set-level orbit reference $2176$. Stages 1–2 verified
sound up to F-C3/F-C5/F-C6. Stage 3 refuted as described in F-C1/F-C2
by direct construction of the distinguishing complete readers.

## Verdict

**REJECT** as constructed. Grounds: stage 3's Theorems C/D,
Corollary C.1, Proposition E, the §4.4 bullets, the §4.5 table rows
3a–3e, and the earned-outcome block are unsound (F-C1, F-C2, F-C4),
and the unsoundness is structural — no bounded prose repair can hold
both Proposition A.2 and stage 3. Salvage statement: stages 1–2 are
salvageable with repairs F-C3, F-C5, F-C6; a successor version should
rebuild stage 3 over the honest class set (including fusion-complex
and bracketing-distinct classes), where finite closure fails a
fortiori and the pre-registered outcome names may be re-earned with
correct proofs. Per pin §10 this terminates the present candidate,
not the unit's investigability; the one-strike rule is a Paper 22-line
rule and is not triggered here.

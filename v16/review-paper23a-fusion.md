# Paper 23a blind review — Seat F (fusion-algebra/representation)

Date: 2026-08-22

Reviewer seat: fusion algebra, semiring/fusion-ring axioms, and
representation-theoretic consequences. Repo read-only; produced solely
from the frozen pin (#309), the candidate (#310, SHA-256
`9cab8d2e78ee5365b0facc86ff059074f482091bbb3621cfd328939b9e247a5a`,
606 LF), the construction note
(`cc157c793cca620b680dca1d93b83a6726dee1e3b7e044647a9cffde889ea10c`),
and terminal Paper 13D (`3b91766f…`). No other seat's report seen.

Verdict: **REJECT**

The stage-3 classification is unsound at its foundation. The defects
below are structural: they cannot be repaired by substituting
sentences, because the candidate must choose between retracting its
own Proposition A.2 and retracting Theorems C/D — it cannot keep
both.

## F-F1 (CRITICAL) — The multiplication is not well defined on the printed class set

Defect. The candidate defines $[\chi]\otimes[\chi'] =
[\Phi_s(\chi\boxtimes\chi')]$ and then evaluates this product *as if*
it landed in the displayed fixture-class set
$\{[U(n)]_s,[DQ(n)]_s,\dots\}$ (Theorems C/D:
$a_m\otimes a_{m'}=a_{m+m'}$). It does not. Paper 13D §7.1 retains, in
every fusion history, both the tensor source value and the fused
target value; §10.2 makes staged sequences distinct traces; and the
candidate's own Proposition A.2 proves that trace shape is
congruence-visible. Therefore $\Phi_s(U_m\boxtimes U_{m'})$ is a
fusion-complex class distinct from every primitive class $a_k$, and
distinct from every tensor-complex class. The honest class set is
closed under neither of the printed computations:

1. products of primitives leave the primitive ladder (so the printed
   tower $\{a_n\}$ is not closed under the derived product);
2. bracketing matters at class level:
   $[\Phi(\Phi(\chi_1\boxtimes\chi_2)\boxtimes\chi_3)]$ carries an
   intermediate fused frontier on carriers $\{1,2\}$, while the right-
   bracketed class carries one on $\{2,3\}$; the complete reader
   separates them exactly as in Proposition A.2. So even over the
   enlarged class set, associativity of $\otimes$ fails;
3. commutativity likewise fails at class level whenever the two
   factors are incongruent complexes: swapping the components swaps
   which sub-carrier is fused first in the retained tensor source,
   and the complete reader sees the difference.

Theorem C's proof ("determinism … makes the fused complex a function
of the component complexes") proves determinism, not congruence with
the target; the inference is a non sequitur.

## F-F2 (CRITICAL) — The semiring conclusion is unproved, so Proposition E's character analysis stands on nothing

Defect. Corollary C.1 and Theorem D assert "associative" by appeal to
union-of-carriers associativity — an identity of final target values,
which §4.4 itself concedes is coarser than any sector statement. With
associativity unavailable (F-F1(2)), there is no semiring, hence no
character equation $d_xd_y=\sum_zN_{xy}^zd_z$ to solve, and
Proposition E's exponential-family recursion
$d_{a_{m+1}}=d_{a_m}d_{a_1}$ is vacuous. The declared outcomes
`P23A-COMMON-POSITIVE-CHARACTER-NONUNIQUE` and
`P23A-FUSION-CLOSURE-FAILS` were earned only against the unproved
$(\mathbb N,+)$ structure.

Note for the record what *does* survive, since adjudication will ask:
the failure of **finite** closure is robust — whatever the true class
set is, occurrence-carrier cardinality strictly increases along any
product chain (the union of carriers is monotone and unbounded), so
no finite nontrivial subcollection closes. A corrected successor can
re-earn `P23A-FUSION-CLOSURE-FAILS` (finite-closure sense) with a
proof that never identifies classes across trace shapes. What cannot
be re-earned without new structure is anything about characters,
involution, or semiring classification — those predicates presuppose
an associative product.

## F-F3 (MAJOR) — The involution refutation (Thm D clause 4) inherits the false identification

Defect. The dual argument uses $N_{a_1,y}^{a_0}=0$, computed inside
the $(\mathbb N,+)$ model. On the honest class set the unit $a_0$
(the one-occurrence... more precisely zero-occurrence primitive
class) could conceivably appear inside products involving
zero-occurrence components in ways the model forbids; the refutation
must be redone after F-F1/F-F2. As printed it proves a property of a
fictional algebra. (This seat expects a corrected no-dual statement
to survive on the enlarged set — the unit element has empty carrier
and appears in no product with a positive-carrier factor unless the
other factor already has empty carrier — but expectation is not a
proof, and the proof as printed is void.)

## F-F4 (MAJOR) — §4.1's definition of operational channel multiplicity is circular where it matters

Defect. $N_{\chi,\chi'}^{\psi}$ counts "the number of distinct
$\sim$-classes of fused complexes landing in $[\psi]$." For this to be
a multiplicity (not merely 0 or 1), several fused complexes must land
in one class while being inequivalent as component maps. But under
Definition 2.1-as-printed (vacuous aligned-pair quantification; see
category-seat domain), class equality is close to trivially easy to
satisfy, making multiplicities unstable under the repair Definition
2.1 will need. The multiplicity notion and the congruence must be
co-repaired; as printed, $N$ is not invariant under the admissible
repair space.

No replacement sentence offered: co-repair is design work for a
successor version, beyond bounded prose repair.

## F-F5 (MINOR) — §4.4 bullet "sector-class equality: yes" contradicts Proposition A.2

Staged versus simultaneous triple fusion have different retained
boundaries; the candidate's own separation principle makes them
incongruent. The bullet asserts the opposite. Void without repair;
belongs with F-F1(2).

## Mandatory regressions (controls 3, 14, 15, 16, 17)

- Control 3 (automorphism orbit size as channel): Def 3.1/§4.1 keep
  orbit sizes out of $N$. PASS at stage 2; moot for stage 3.
- Control 14 (representative mass): full-orbit sums throughout;
  tables independently recomputed and confirmed. PASS.
- Control 15 (semiring conclusion from nonnegativity alone): FAIL —
  the deeper form of this failure: the semiring was concluded without
  proving associativity at all. The control's letter (don't conclude
  from nonnegativity) was obeyed; its spirit (earn the algebra before
  using it) was violated.
- Control 16 (character uniqueness assumed): worse than assumed —
  asserted against an unproved structure; the constructive
  nonuniqueness argument (Prop E) is correct *in form* but has no
  subject matter until associativity is proved. CONDITIONAL-FAIL.
- Control 17 (FP dimensions as odds/physical states): Cor E.1 blocks
  FP odds explicitly, and no dimensions are claimed anywhere. PASS —
  this wall held.

## Independent verification performed

Exact rational recomputation of stages 1–2 fixtures (seed censuses,
orbit partitions, mass tables, endpoint conditionals, bond pattern
laws) confirming all printed values; see also the seat-independent
note that §3.2 contains the false sentence "$2^7\times625=128$"
(correct census $16\times4\times2=128$ over $16\times625$ seeds).
For stage 3 this seat verified the *negative* claims that matter:
(i) the retained-boundary reading of §7.1/§10.2 that grounds F-F1,
by direct inspection of the trace-type clauses; (ii) that no
subcollection of the honest class set closed under the derived
product can be finite (carrier-monotonicity); (iii) that the printed
tower identification fails for the smallest case
($a_1\otimes a_1$: the fused complex retains a two-component tensor
source value; the primitive $U(2)$ has none; their outcome fibers
differ).

## Verdict

**REJECT** as constructed. Stage 3 (Theorems C/D, Corollary C.1,
Proposition E, §4.4 bullets, §4.5 rows 3a–3e, earned-outcome block)
is unsound per F-F1–F-F5, structurally so. Salvage path for a
successor version, at pin-compatible scope: rebuild stage 3 over the
honest class set (primitive/tensor/fusion/staged-bracketing classes
all distinct); prove finite-closure failure by carrier monotonicity;
record the associative-product question as `NOT-APPLICABLE` /
`BLOCKED` rather than asserting either answer; drop all character and
involution conclusions until an associative product is proved.
Stages 1–2 fall outside this seat's mandate except where cited above;
their fixture arithmetic checked clean.

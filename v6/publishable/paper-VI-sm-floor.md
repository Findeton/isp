# The Standard-Model floor: uniqueness of the minimal chiral matter content on a derived charge lattice

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** preprint, not peer reviewed, version 2026-06-11.

## Abstract

Within the sealed-records program (Parts I–II), we present the
selection of Standard-Model matter content as a sequence of
exhaustive, machine-verified searches under derived constraints —
with every input named and graded.  Derivations of this kind
carry a well-known circularity risk (constraints read off the
answer and fed back as selection principles); our discipline is to
make every constraint's provenance explicit, and where a residue of
target-calibration remains — it does, and we say where — to grade
it as input rather than claim it as output.  Results: (i) **hypercharge is
the relative determinant character** of the reconstructed
$U(3)\times U(2)$ fiber tower, $Y_6 = 3b - 2a$: with the $U(d)$
linkages $a \equiv \tau \ (\mathrm{mod}\ 3)$, $b \equiv \sigma\
(\mathrm{mod}\ 2)$ this renders the empirical
$\mathbb Z_6$ congruence $2\tau + 3\sigma + Y_6 \equiv 0$ an
*identity*, and the correspondence is sharp — of the thirty-six
residue classes of determinant-character combinations exactly one
yields the congruence; (ii) the selection *mechanism* is a
charge-screening theorem: sealed, fermion-even, gauge-singlet
records collapse superselection classes (a collapse lemma whose
exclusion clauses are carried by univalence superselection and the
centrality of the recorded gradings), the ledger's baryon–lepton seal at charge $(3,2)$
screens exactly one direction, and a rank bound from the program's
screen-$U(1)$ forbids more — the bare-baryon direction is blocked
precisely by the fermionic-intertwiner exclusion; (iii) given only
the representation shells, the Yukawa seam system plus the three
$Y$-linear anomaly conditions has a one-dimensional kernel whose
minimal integer point is exactly the Standard-Model hypercharge
assignment — and the gauge-squared anomaly coefficients themselves
are *lattice-grounded at abelianized scope* by a four-dimensional
record index theorem
(overlap index $= c^2 f_1 f_2$, exact in all sectors; $T(R)$ as
summed Cartan indices; the full nonabelian rows remain imports
pending instanton-sector receipts); (iv) the **floor theorem**: exhaustive
search over the lattice — derived modulo the two named empirical
inputs of (ii), which is what "derived" means everywhere in this
paper — finds the Standard-Model generation
as the unique minimal genuinely chiral anomaly-free content (15
Weyl fermions; nothing at $\le 14$; only the conjugate at 15), and a
tower-exclusion search shows the $(3,2)$ fiber tower has the
strictly smallest chiral floor among alternatives, which either cost
more than double or admit no floor at all in bounds.  Falsifiable
consequences include the absence of fractionally charged color
singlets.  The honest negatives and the named inputs are printed
with equal prominence, and the input list is complete: the seam
system fixes the hypercharge ray but not the residue class
(screening does); the minimality principle selecting the cheapest
tower is a named input, as are the tower-uniformity premise of the
exclusion comparison and the gauged-family premise of Section 6;
the generation count is observational;
**the existence of sealed fermionic records in the specific
composite fibers needed to write the baryon–lepton seal (Q-type
$(3,2)$ and L-type $(1,2)$ carriers) is an empirical input about
nature's ledger, not an output** — it is the largest single input
of the paper and Honest negative 3.5 discusses it; the surviving continuous
charge functional (the screen-$U(1)$) and the weak-doublet scalar
seam carrier (the Higgs representation) are likewise named inputs
(Sections 3 and 7).

## 1. Introduction

Attempts to "derive the Standard Model" founder on two reefs:
hidden circularity (constraints read off the answer and fed back as
selection principles) and unfalsifiability (enough freedom to fit
anything).  This paper's discipline is aimed at both: every
constraint used by the searches is either derived inside the
program with receipts, or named as an input and graded; and the
output is accompanied by falsifiers.

The structural inputs from Parts I–II: a fiber tower whose gauge
structure is the *full* unitary group of each fiber (determinant
slots included — the commutant reconstruction), univalence
superselection, and the records-are-relations ontology.  The new
content here: the hypercharge derivation, its screening mechanism,
the anomaly-row grounding, and the exhaustive floor searches.

## 2. Hypercharge as the relative determinant character

$U(d)$ representation theory links the determinant charge to the
center: $a \equiv \tau \ (\mathrm{mod}\ 3)$ for $U(3)$ (triality
$\tau$), $b \equiv \sigma\ (\mathrm{mod}\ 2)$ for $U(2)$ (duality
$\sigma$).  Define hypercharge as a determinant-character
combination $Y_6 = \alpha a + \beta b$.

**Theorem 2.1 (equivalence, sharp).**  The empirical congruence
$2\tau + 3\sigma + Y_6 \equiv 0 \ (\mathrm{mod}\ 6)$ — satisfied by
all six multiplets of the $\nu_R$-completed Standard-Model
generation — holds *identically in $(a,b)$*
iff $(\alpha, \beta) \equiv (-2, 3) \ (\mathrm{mod}\ 6)$, i.e. iff
$Y_6 = 3b - 2a$ is the relative determinant character; then it is
the identity $2a + 3b + (3b - 2a) = 6b$.  Of the thirty-six residue
classes, exactly one survives; every congruence-allowed charge
triple is realized; and the minimal $(a,b)$ representatives
reproduce the Standard-Model table exactly
($Q(1,1)\mapsto +1$, $L(0,-1)\mapsto -3$, $u^c(2,0)\mapsto -4$,
$d^c(-1,0)\mapsto +2$, $e^c(0,2)\mapsto +6$, $\nu^c(0,0)\mapsto 0$).

Receipts: the 36-class scan and the zero-unrealized-triples check
do real work; the $[-9,9]^2$ identity scan is a sanity check of an
algebraic identity and is labeled as such, not as evidence.
Equivalently, at the
global level, the gauge group is $S(U(3)\times U(2)) \cong
(SU(3)\times SU(2)\times U(1))/\mathbb Z_6$ — the "true gauge
group" structure documented by O'Raifeartaigh, Hucks, and Tong
[1, 11, 2], here arrived at from the fiber side.

## 3. The mechanism: charge screening by sealed singlets

Why is hypercharge *that* character?  The mechanism is a screening
theorem with three clauses, each carried by a previously-established
result:

**Lemma 3.1 (collapse).**  A sealed, fermion-even, gauge-singlet
record with charge displacement $c$ collapses the superselection
classes $[q]$ and $[q + c]$.  *Exclusions*: fermionic intertwiners
cannot collapse (univalence is superselected — Part II);
gauge-charged ones cannot (they shift recorded labels); the
centrality of the recorded gradings — by which we mean precisely
that the $(-1)^F$ and determinant-charge gradings commute with
every record-algebra element (the Part II superselection theorems;
"code centrality" in earlier program vocabulary, retired here) —
makes both statements one commutator computation (receipts: the
even seal commutes exactly with the grading, the odd bare-baryon
seal anticommutes exactly).
*Membership*: sealed records are ledger morphisms by axiom R.
*Collapse*: the GNS argument — the seal's nonvanishing action
places a charge-$(q{+}c)$ module inside the charge-$q$
representation.

**Lemma 3.2 (the seal, stated fiber-theoretically — and its input
content).**  In the fiber tower there exists an invariant tensor of
type $\varepsilon^{(3)} \otimes \varepsilon^{(2)}$ coupling three
color-fiber strands carrying weak-fiber indices to one bare
weak-fiber strand (invariant-tensor dimensions $1$ and $2$,
receipted); a sealed, fermion-even ($F = 4$) record built on it
carries determinant charge exactly $(3, 2)$.  **The input, stated
where the lemma is used and in the abstract**: that nature's ledger
contains *fermionic* records in those composite fibers — Q-type
$(3,2)$ and L-type $(1,2)$ carriers — sufficient to instantiate
this tensor.  The familiar name of the resulting record is $QQQL$,
and we are explicit that using it before the floor search outputs
Q and L is not circular *only because* the lemma needs existence of
the carriers, not their uniqueness or the rest of the generation —
but that existence is itself an empirical fact, the single largest
input of the paper.

**Lemma 3.3 (rank bound; its premise graded).**  Screening two
independent directions would annihilate every continuous charge
functional.  The premise that one continuous charge functional must
survive — the program's screen-$U(1)$, whose derivation is
corpus-bound **[P]** (Part I's tag for dependencies whose proofs
live in the program corpus, not in this batch) — is **graded here
as a named input co-equal with the seal**: it is, in effect, the
requirement that a long-range abelian charge (electromagnetism)
exists.  Granting it, the screening lattice has rank $\le 1$, and
containing the primitive $(3,2)$ it is exactly $\mathbb Z(3,2)$.

**Theorem 3.4.**  The recordable charge data is $(a,b)$ modulo
$(3,2)\mathbb Z$, whose complete invariants are exactly
$(\tau, \sigma, Y_6 = 3b - 2a)$ — the $S(U(3)\times U(2))$
structure, hence Theorem 2.1's lattice, *derived modulo the graded
inputs of Lemmas 3.2–3.3*.  (Remark: $Y_6$ alone is already a
complete invariant — $\tau \equiv Y_6 \bmod 3$ and $\sigma
\equiv Y_6 \bmod 2$ — so the triple is stated for readability,
not necessity.)  Nonvanishing of
the seal on arbitrary backgrounds holds by per-sector clustering
(the transfer is self-adjoint by reflection positivity, so
$T^n \to P_1$ needs no gap — an engine theorem valid at every rank;
proof corpus-bound **[P]**, flagged as a stated dependency of this
batch),
with a wrong-sector zero control showing the per-sector
qualifier is exactly right.

**Honest negative 3.5.**  The Yukawa-seam system (Section 4) does
*not* select the residue class — the Standard-Model values also fit
a wrong-class formula at residue level.  The class selection rests
on the screening mechanism; an alternative world whose ledger sealed
a lepton-pair direction instead would have hypercharge proportional
to the pure color determinant — consistent mathematics, excluded by
*which seals nature's ledger contains*, an empirical fact we flag
rather than bury.

## 4. The seam system and the anomaly rows, grounded

**The input, named first.**  That hypercharge is fixed by anomaly
cancellation *plus the Standard-Model Yukawa structure* is a known
result, established by Geng–Marshak, Babu–Mohapatra, Foot et al.,
and Minahan–Ramond–Warner [3, 6, 7]; we claim no priority for the
linear algebra of this section.  The *existence of the four Yukawa
seams and the Majorana seal* — i.e., which couplings the ledger
contains — is itself structure: in the program it is carried by the
records-are-relations axiom (every gauge-invariant fermion bilinear
admits a sealing record), which is weaker than assuming the SM
Yukawa matrix but is an input nonetheless, and we grade it as such.
What this section adds beyond the classical result is (i) the
provenance of the anomaly rows themselves (Theorem 4.1) and (ii)
the division of labor established in Section 3: the seam system
fixes the *ray*, screening fixes the *residue class*.

Given only the representation shells, impose the four Yukawa seams,
the Majorana seal, and three $Y$-linear anomaly rows (gravitational,
$SU(3)^2$–$Y$, $SU(2)^2$–$Y$): the system has rank 6 with a
one-dimensional kernel whose minimal integer generator is
$(y_Q, y_u, y_d, y_L, y_e, y_\nu \,|\, y_H) =
(1, -4, 2, -3, 6, 0 \,|\, -3)$ — the Standard Model exactly.
Without the gauge-squared rows the kernel is two-dimensional: they
are load-bearing.  Their provenance is *partially* upgraded by the
following — precisely: the abelianized coefficients become lattice
observables, while the full nonabelian rows remain continuum
imports pending the instanton-sector receipt:

**Theorem 4.1 (4d record index, abelianized scope).**  On the
four-torus record lattice with overlap fermions [8] and $U(1)$
fluxes $f_1, f_2$ in two planes, the index equals $c^2 f_1 f_2$ —
exact in six sectors including sign flips and charge two; with two
independent $U(1)$s, the index is $q_a q_b f_1 f_2$; and
Cartan-abelianized $SU(2)$ weight sums reproduce $T(R)\,m_1 m_2$
exactly (adjoint $+2.0$; fundamental at even fluxes $+2.0$ — the
half-integer weights demanding even fluxes is the quotient
structure of Section 2 reappearing from the lattice side).  The
quadratic anomaly coefficient, invisible to two-dimensional index
theorems, is thereby a lattice observable, and the anomaly rows are
sums of measured indices.  The mathematical foundation — that the
overlap construction carries an exact index on the lattice tied to
the topological charge — is the Hasenfratz–Laliena–Niedermayer /
Lüscher index theory [9]; our contribution is the *use*: measuring
the gauge-squared coefficients as index data on record lattices,
so the seam-system rows have lattice provenance instead of being
continuum imports.  (Full nonabelian backgrounds — instanton
sectors — are the named next receipt.)

## 5. The floor theorems

**Theorem 5.1 (uniqueness on the derived lattice; bounds stated).**
Exhaustive search over multiplets — color $\in \{1, 3, \bar 3\}$,
weak $\in \{1, 2\}$, hypercharges on the derived lattice with
$|Y_6| \le 12$ (i.e. $|Y| \le 2NM$ for the $(3,2)$ tower), at most
five distinct multiplets, each with multiplicity, counted in Weyl
fermions — under the anomaly predicates ($SU(3)^3$, $SU(3)^2$–$Y$,
$SU(2)^2$–$Y$, $Y^3$, gravitational), the Witten condition [5] on
pseudoreal doublets, and genuine chirality (no vector-like pairing
of the full content): **zero** solutions below 15 Weyl fermions,
and at 15 exactly the Standard-Model generation and its conjugate.
Robustness: widening the hypercharge window and the representation
zoo (color sextets and octets, weak triplets) at $\le 16$ Weyl
admits no competitor below 16, with the first exotic alternative
appearing at 16 Weyl in 6 multiplets.  These are *search* results:
their scope is exactly the stated pool and bounds, no more.  The
genre has prior art — systematic classifications of anomaly-free
chiral matter (e.g. the Allanach–Gripaios–Tooby-Smith program [12])
— and the distinguishing feature here is not the search machinery
but the *derived lattice* it runs on; we engage that literature as
Section 4 engages the anomaly-quantization literature.

**Theorem 5.2 (tower exclusion; same bounds, applied uniformly).**
Running the same machinery on alternative fiber towers $(N, M)$ —
each with *its own* derived lattice $Y = Nb - Ma$, its own residue
linkages, $|Y| \le 2NM$, $\le 5$ multiplets, and the corresponding
$SU(N)^3$ predicate — yields: $(3,2)$ floor $= 15$ Weyl; $(4,2)$,
$(5,2)$, $(4,3)$: none within bounds; $(3,3)$: $36$ Weyl.  The
$(3,2)$ tower is strictly minimal among probed alternatives;
combined with the program's exhaustion theorem (no genuinely chiral
record content below stack size three), the fiber dimensions are
*minimality-selected*, with the minimality principle itself the
named remaining input.  One further premise of the comparison is
named: for the $(3,2)$ tower the lattice is derived from a seal
whose existence is empirical (Honest negative 3.5), while for the
counterfactual towers the analogous baryon-like seal is
*stipulated* — the comparison therefore assumes **uniformity**
(every tower's ledger seals its own primitive direction), and that
assumption stands beside minimality in the input list.

## 6. Predictions and falsifiers

- **No fractionally charged color singlets** (the quotient
  structure): a confirmed millicharged particle falsifies the
  derivation outright.
- **The sixteenth state, honestly graded** — an earlier draft
  listed "right-handed neutrinos exist" as a forced prediction;
  review showed that is partially circular: the seam system of
  Section 4 already includes $\nu^c$-bearing seams among its
  inputs (bilinears involving $\nu^c$ exist only if $\nu^c$
  does), so the state's *existence* is an input of the
  seam-existence premise, not an output.  What IS derived,
  conditional on existence and on the *gauged-family premise*
  (defined here, since it carries this row: the seam system,
  including the Majorana seal, holds uniformly across the
  family/generation index): the sixteenth state's only bare mass
  term is $\nu^c\nu^c$ — Majorana structure is forced, Dirac-only
  neutrinos are excluded.  The corollary
  "neutrinoless double-beta decay at *some* level" is a
  **consequence, not a falsifier** — with no rate floor no
  experiment can refute it, and we list it outside the falsifier
  set.
- **Baryon-number violation, if seen, is $B{-}L$-conserving** at
  leading order (the operator ledger admits $p \to e^+\pi^0$-class
  channels; $\Delta(B{-}L) \neq 0$ first at dimension 9).
- Scope of the millicharge falsifier, stated: a confirmed
  fractionally charged color singlet kills *this derivation* (the
  $\mathbb Z_6$ quotient structure), not the record ontology as a
  whole — Honest negative 3.5's alternative-seal worlds are exactly the
  survival route, and we say so rather than let the falsifier
  appear to cover more than it does.
- Separate registration documents record the program's
  *quantitative* confrontations: the undressed spectrum-point
  registration (the note's earlier exponent and band forms are
  withdrawn within it) and the mechanism paper's four-member
  dressed menu, two members live against today's data — with
  tolerances, pre-committed outcome bands,
  and named resolving experiments.

## 7. What is input, restated

The complete input list: (1) the generation count (three) is
observational; (2) the minimality principle (nature populates the
cheapest chiral tower) is named, not derived — its dynamical origin
is the program's open dynamics layer; (3) the seal's existence —
fermionic carriers in the $(3,2)$ and $(1,2)$ composite fibers —
is an empirical fact about the ledger (Lemma 3.2, Honest negative
3.5); (4) the
screen-$U(1)$ (a surviving continuous charge) is a named input
co-equal with the seal (Lemma 3.3); (5) the tower-uniformity
premise of the exclusion comparison (Section 5.2); (6) the Yukawa
seam existence premise with the **Higgs representation** — the
seam carrier is a single weak-doublet, color-singlet scalar, which
the graded seam-existence input does not by itself produce and
which we name as input here; (7) the gauged-family premise
(Section 6); (8) the **global-to-local gauge promotion** — Part
II reconstructs each fiber's symmetry as a *global* group (the
commutant of exchange) and grades its promotion to a local gauge
symmetry with connection and dynamics as an additional input
where this paper uses it; the anomaly predicates of Sections 4–5
presuppose the gauged form, so the promotion is counted here as
a named input, honoring Part II's grading.  Everything else used by the
searches is derived with receipts or imported and named
(Stone–von Neumann, Schur–Weyl, the Witten condition's topological
input).  We believe this is the correct standard for claims of this
kind, and we commend hostile referees to the audit.

**Relation to other derivation programs.**  The closest structural
relative is the noncommutative-geometry program of Connes and
Chamseddine [10], which also obtains the Standard-Model fiber
structure $\mathbb C \oplus \mathbb H \oplus M_3(\mathbb C)$ and
hypercharge assignments from an axiomatic selection principle
(spectral triples and the spectral action) rather than from
phenomenological fitting.  The comparison is instructive in both
directions: there, the algebra is selected by classification of
finite spectral triples and the fermion content sits in a fixed
Hilbert space; here, the fibers are selected by a chirality
exhaustion theorem plus measured minimality (Theorem 5.2), and the
content is the output of an anomaly-constrained search on a derived
lattice.  Both programs face the same honest residue — a named
selection principle (the spectral action's algebra axioms there,
the minimality principle here) that the program motivates but does
not derive — and both forbid fractionally charged color singlets.
The group-theoretic uniqueness literature for the SM gauge quotient
[1, 2, 4] is the common backdrop.

## Reproducibility

Integer-exact lattice receipts; the seam-system kernel; the 4d
index sectors; the floor and tower searches with stated pools and
bounds — all regenerate from fixed-seed scripts with bit-identical
reruns.

## References

[1] L. O'Raifeartaigh, *Group Structure of Gauge Theories*, CUP
(1986).

[2] D. Tong, Line operators in the Standard Model, *JHEP* **07**
(2017) 104.

[3] C. Q. Geng, R. E. Marshak, *Phys. Rev. D* **39** (1989) 693;
R. Foot, G. C. Joshi, H. Lew, R. R. Volkas, *Mod. Phys. Lett. A*
**5** (1990) 2721 — hypercharge quantization from anomalies.

[4] J. Baez, J. Huerta, The algebra of grand unified theories,
*Bull. AMS* **47** (2010) 483.

[5] E. Witten, An SU(2) anomaly, *Phys. Lett. B* **117** (1982)
324.

[6] K. S. Babu, R. N. Mohapatra, Is there a connection between
quantization of electric charge and a Majorana neutrino?, *Phys.
Rev. Lett.* **63** (1989) 938; *Phys. Rev. D* **41** (1990) 271.

[7] J. A. Minahan, P. Ramond, R. C. Warner, Comment on anomaly
cancellation in the standard model, *Phys. Rev. D* **41** (1990)
715.

[8] H. Neuberger, Exactly massless quarks on the lattice, *Phys.
Lett. B* **417** (1998) 141.

[9] P. Hasenfratz, V. Laliena, F. Niedermayer, The index theorem in
QCD with a finite cut-off, *Phys. Lett. B* **427** (1998) 125;
M. Lüscher, Exact chiral symmetry, topological charge and related
topics in lattice QCD, *Nucl. Phys. B Proc. Suppl.* **83** (2000)
34.

[10] A. H. Chamseddine, A. Connes, The spectral action principle,
*Commun. Math. Phys.* **186** (1997) 731; A. H. Chamseddine,
A. Connes, M. Marcolli, Gravity and the standard model with
neutrino mixing, *Adv. Theor. Math. Phys.* **11** (2007) 991.

[11] J. Hucks, Global structure of the standard model, anomalies,
and charge quantization, *Phys. Rev. D* **43** (1991) 2709.

[12] B. C. Allanach, B. Gripaios, J. Tooby-Smith, Anomaly
cancellation with an extra gauge boson, *Phys. Rev. Lett.* **125**
(2020) 161601; Solving local anomaly equations in gauge-rank
extensions of the Standard Model, *Phys. Rev. D* **101** (2020)
075015.

**Parts I–II:** *Quantum theory from sealed records I–II* (same
author).

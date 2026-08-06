# The Task–Record Fixed Point

## Record Availability, a Galois Connection on One Process Boundary, and the Limits of De-Smuggling

**Status:** `GREEN-UNREVIEWED`

**Date:** 2026-08-02

**Frozen analytical pin:** `7a80e39`

**Immutable base:** `6c2d7b8`

---

## Abstract

The operational classical core of a minimal sufficient process boundary is
relative to a chosen future task, and a task matched to a preselected
projection-valued measure can manufacture that measure as the core. This
paper asks whether a record and its preserving future family can determine
each other, so that a record would be a fixed point rather than a
task-relative artifact.

The literal preserving-family formula collapses. For a complete admitted
nondisturbing repeatable instrument the outcome-forgetting composite is
exactly the identity, so every admitted future preserves every record in
the literal sense, including futures that provably destroy the record. We
prove the collapse and replace the definition by an availability form: a
future preserves a record when an admitted later readout reproduces the
record's flag-joint statistics exactly. This is the operational transport of
the availability hypothesis used for unitary supports in the predecessor
record work. On a finite direct sum it reduces to an exact sector criterion:
the future may scramble arbitrarily inside a record block but must never
send two distinct blocks to a common sector.

With that definition the intended machinery works. The preserving family is
antitone in record refinement, the induced core is antitone in future-family
inclusion, and the two form an antitone Galois connection whose closure
operators have the closed records as fixed points. We also refute the
alternative reading: the predecessor construction that sends a task family
to the core of its minimal sufficient boundary is not antitone, since
enlarging a preserving task family by an eraser task takes a one-atom core
to a five-atom core.

The fixed points are then computed exactly, and they are degenerate in a new
way. Under the admitted reprepare closure the closure operator is the
identity: every admitted record is a fixed point. The trivial record is
fixed precisely when a record-erasing future is admitted, which refines the
expectation that it is always fixed. Under the composite reading the map is
constant, because the identity future preserves every record; its unique
fixed point is the operational core itself.

Consequently the de-smuggling discriminator fails: the manufactured measure
survives as a fixed point under the first reading and as the unique fixed
point under the second. We prove this is not an artifact of the definition.
A legitimately derived boundary and a manufactured boundary of the same
sector type are carried onto each other by an admitted reversible map that
permutes the core atoms, and the whole construction is covariant under
exactly such maps. No criterion definable from one-boundary data can accept
one and reject the other.

The registered outcome is therefore `RQ0-L0-BLOCKED-AT-DE-SMUGGLING`, an
instance of the pre-registered blocked outcome whose un-typed object is a
task-independent selector on the fixed-point set. Nontrivial fixed points
exist in abundance, so the no-nontrivial-fixed-point outcome is refuted; but
existence carries no selective content, so the positive outcome is not
earned.

---

## Scope box

| Item | Value |
|---|---|
| Dimension | finite throughout |
| Boundaries | exactly one, fixed in advance |
| Inherited scope | the declared #103 compact-convex Karoubi scope and the declared #111 ancilla-saturated, instrument-complete scope, unchanged |
| Records | complete admitted nondisturbing repeatable classical instruments only |
| Futures | admitted deterministic process transformations out of that one boundary |
| Arithmetic | exact throughout; no float in any substantive path |
| Verification | exhaustive over all left-total sector relations at atom count $\leq 4$; declared subfamily at atom count $5$; the general case carried by a proved lemma |
| Lean | none |
| Not decided here | how boundaries combine, and every later object |

Every numbered result below carries a scope tag. `[FIN]` means finite
one-boundary earned scope. `[EXH-4]` means additionally verified
exhaustively at atom count at most four. `[FIX]` means verified on the
committed fixture set only.

The word "Markov" appears in this paper only inside the pre-registered
outcome name `RQ0-L0-W3-OPERATIONAL-MARKOV-BOUNDARY`, where it abbreviates
operational screening-off inside one boundary. It carries no spacetime
meaning of any kind.

Two inherited postulates are used by name and are not re-derived here:
closure of the admitted instruments under sequential flagged composition,
and closure under finite classical coarse-graining of retained flags. Both
are one-boundary laboratory postulates from the predecessor cycle. Neither
is a statement about how two boundaries combine; that question is not
touched.

---

## 1. The question and the result

### 1.1 What is inherited

The predecessor cycles earn two objects. First, for a fixed compatible
future-task family \(\mathfrak F\), a minimal sufficient process boundary

\[
B_{\mathfrak F}=(X,e)\in\operatorname{Kar}(\mathsf{Proc}_D),
\]

unique up to reversible operational equivalence. Second, at
ancilla-saturated instrument-complete scope, its matrix-ordered effect
system \(S=\mathcal E(B_{\mathfrak F})\) carries a canonical finest admitted
nondisturbing repeatable classical instrument

\[
\operatorname{Cl}_{\mathrm{op}}(S)=\{A_1,\ldots,A_N\},
\]

the operational classical core, whose branches are the atoms of the Boolean
algebra of admitted split projections.

Both objects are relative to \(\mathfrak F\). The predecessor adjudication
proves this is not a cosmetic relativity: for any chosen finite
projection-valued measure \(P=\{P_r\}\), the matched dephasing has range

\[
A_P=\bigoplus_r P_rB(H)P_r,
\]

and with an independently affine-separating state family on that range the
minimal boundary's centre is exactly \(C^*(P_1,\ldots,P_m)\). Choosing the
task using the desired measure manufactures that measure as the core.

### 1.2 The question

Can the record and its preserving future family determine each other? The
target is a closure

\[
M\ \simeq\ \operatorname{Core}(\operatorname{Pres}(M)),
\]

with both sides independently physical: complete admitted futures on one
side, complete nondisturbing repeatable classical instruments on the other.
If nontrivial solutions existed and rejected the manufactured measure, a
record would be a fixed point rather than an artifact.

### 1.3 The result, in one paragraph

The literal preserving-family definition collapses to triviality and is
replaced by an availability form (Section 2). With that repair the Galois
machinery genuinely works (Section 3). The fixed points are then computed
exactly and are degenerate: under the admitted reprepare closure every
record is fixed, so the fixed-point condition selects nothing; under the
composite reading the map is constant (Section 4). The manufactured measure
survives both, and we prove that no one-boundary criterion could have
rejected it (Section 4.5). The controls behave as required (Section 5).

The registered outcome is

\[
\boxed{\texttt{RQ0-L0-BLOCKED-AT-DE-SMUGGLING}}
\]

with `RQ0-L0-NO-NONTRIVIAL-FIXED-POINT` refuted and
`RQ0-L0-W3-OPERATIONAL-MARKOV-BOUNDARY` not earned.

### 1.4 Four-gate audit of the one new object

The single new object is the preserving family \(\operatorname{Pres}(M)\).

| Gate | Disposition |
|---|---|
| Referent | a set of admitted deterministic futures, membership decided by exhibiting an admitted later instrument whose flag-joint statistics reproduce the record; both are laboratory data |
| Necessity | the fixed-point question cannot be posed without it, and its literal predecessor form is proved degenerate in Section 2.1 |
| No-smuggling | the definition mentions no candidate record algebra, no measure, and no task; it quantifies over the admitted law fixed beforehand |
| Discriminator | Section 2.4 exhibits admitted futures inside and outside on the earned fixtures, and Section 5.4 gives the exact positive recovery deficit that separates them |

---

## 2. The definition gate

### 2.1 The literal formula collapses

The predecessor proposal defines the preserving family by

\[
\operatorname{Pres}_{\mathrm{lit}}(M)
=\{F:\lVert F-F\circ D_M\rVert_{\mathrm{Test}}=0\},
\]

where \(D_M\) is the outcome-forgetting composite of the instrument
\(M=\{m_r\}_{r\in\Omega}\).

### Theorem 2.1 — the literal preserving family is everything `[FIN]`

Let \(M\) be any complete admitted nondisturbing repeatable classical
instrument on \(S\). Then

\[
D_M=\sum_{r}m_r=I_S,
\]

hence \(F\circ D_M=F\) and \(\lVert F-F\circ D_M\rVert_{\mathrm{Test}}=0\)
for every admitted future \(F\). Consequently

\[
\operatorname{Pres}_{\mathrm{lit}}(M)=\operatorname{Fut}(S)
\quad\text{for every }M,
\]

so \(\operatorname{Pres}_{\mathrm{lit}}\) is a constant map,
\(\operatorname{Core}\circ\operatorname{Pres}_{\mathrm{lit}}\) is constant,
and the literal fixed-point equation contains no information about \(M\).

**Proof.** The displayed identity is clause (3) of the inherited definition
of a complete classical instrument: forgetting the flag is nondisturbing,
\(\sum_r m_r=I_S\). Everything else is substitution. \(\square\)

The identity was checked on every instrument of every committed fixture, as
a map on effects rather than as a multiplier: \(D_M(b)=\sum_r z_rbz_r=b\) for
all \(308\) instrument–effect pairs, and
\(F^\sharp(b)=F^\sharp(D_M(b))\) for all \(16\) future–instrument pairs of the
concrete battery.

The collapse is not merely formal. The literal family contains futures that
demonstrably destroy the record.

### Proposition 2.2 — a record-destroying future inside the literal family `[FIX]`

Take the inherited one-step control: two written settings whose preserving
dephasing laws are \(p_0=(3/4,1/4)\) and \(p_1=(1/4,3/4)\), and the no-write
reset, which returns \((1/2,1/2)\) for both settings. The reset lies in
\(\operatorname{Pres}_{\mathrm{lit}}(M)\) for the two-outcome record \(M\).
Yet after the reset the output law is independent of the setting, so any
later readout returns one fixed distribution \(d\) and incurs

\[
\max_i\operatorname{TV}(p_i,d)
\ \geq\ \tfrac12\bigl(\operatorname{TV}(p_0,d)+\operatorname{TV}(p_1,d)\bigr)
\ \geq\ \tfrac12\operatorname{TV}(p_0,p_1)
=\tfrac14,
\]

with equality at \(d=(1/2,1/2)\). The optimal recovery deficit is exactly
\(1/4\).

A definition under which a future that erases the record still counts as
preserving it is not usable. The literal formula is therefore discarded.

### 2.2 The availability form, adopted

The replacement asks for the record to remain *recoverable*.

### Definition 2.3 — record availability `[FIN]`

Let \(M=\{m_r\}_{r\in\Omega}\) be a complete admitted nondisturbing
repeatable classical instrument on \(S\) with outcome effects
\(q_r=m_r(1_S)\), and let \(F\) be an admitted deterministic future with
Heisenberg action \(\Phi=F^\sharp\) on the effects of the later boundary
\(S'\). Say \(F\) **preserves the record of** \(M\), written
\(F\in\operatorname{Pres}(M)\), when there is an admitted complete
instrument \(M'=\{m'_s\}_{s\in\Omega}\) on \(S'\) such that for every
admitted state \(\rho\) and all \(r,s\in\Omega\),

\[
\Pr(r\ \text{first},\,s\ \text{second}\mid\rho)
=\rho\bigl(m_r(\Phi(m'_s(1_{S'})))\bigr)
=\delta_{rs}\,\rho(q_r).
\]

The record is available after \(F\) exactly when some admitted later readout
reproduces it token by token, not merely in distribution.

Since the admitted states separate the effects of the boundary, the
condition is equivalent to the operator identity

\[
m_r\bigl(\Phi(q'_s)\bigr)=\delta_{rs}\,q_r
\qquad\text{for all }r,s,
\]

and, because \(\Phi\) is unital and \(\sum_s q'_s=1\), to
\(\Phi(q'_s)=q_s\) for all \(s\) whenever the branches are the central
filters \(m_r(a)=z_ra\). We use the latter form computationally.

**Antecedent.** This is the operational transport of the availability
hypothesis of the predecessor record work, where for unitary supports
(H-avail) reads: for every later configuration \(i\), all cut configurations
\(k\) with \((U_2)_{ik}\neq0\) lie in one sector. Proposition 2.5 below shows
the transported condition is literally the same support statement, with
admitted completely positive futures in place of unitaries. The predecessor
statement is an antecedent, not a citation of authority: it is re-proved
here in the form used.

### 2.3 The exact sector criterion

Write \(\mathcal A(S)=\{A_1,\ldots,A_N\}\) for the core atoms. For an
admitted future \(F\) define its **sector support**

\[
\operatorname{sup}(k)
=\{\,l:\operatorname{tr}\bigl(z_l\,F(z_k)\bigr)\neq0\,\},
\]

the set of later atoms reachable from atom \(k\).

### Lemma 2.4 — multiplicative domain `[FIN]`

If \(\Phi\) is unital completely positive and \(p\) is a projection with
\(\Phi(p)\) a projection, then \(p\) lies in the multiplicative domain of
\(\Phi\), so \(\Phi(pq)=\Phi(p)\Phi(q)\) for every \(q\).

**Proof.** \(\Phi(p^*p)=\Phi(p)=\Phi(p)^2=\Phi(p)^*\Phi(p)\), and likewise
for \(pp^*\); this is the defining condition of the multiplicative domain,
over which a unital completely positive map is a bimodule map. \(\square\)

### Proposition 2.5 — the sector criterion `[FIN]`, `[EXH-4]`

Let \(M\) correspond to a partition \(\pi\) of \(\mathcal A(S)\) with central
outcome projections \(z_B\), \(B\in\pi\). Then

\[
F\in\operatorname{Pres}(M)
\iff
\text{the sets }\operatorname{sup}(B)=\bigcup_{k\in B}\operatorname{sup}(k),
\ B\in\pi,\ \text{are pairwise disjoint.}
\]

The future may scramble arbitrarily inside a block; it may never send two
distinct blocks into a common later sector.

**Proof.** If the images are pairwise disjoint, choose any partition
\(\{C_B\}\) of the later atoms with \(\operatorname{sup}(B)\subseteq C_B\);
then \(\Phi(z_{C_B})=z_B\) and \(M'=\{z_{C_B}\}\) is an admitted readout, so
\(F\in\operatorname{Pres}(M)\). Conversely, if some later atom \(l\) is
reachable from \(k\in B\) and \(k'\in B'\) with \(B\neq B'\), then any
admitted readout assigns \(l\) to at most one outcome, so one of
\(\Phi(q'_B)=z_B\), \(\Phi(q'_{B'})=z_{B'}\) fails on the corresponding
sector. \(\square\)

The criterion and the literal Definition 2.3 were compared directly on the
whole concrete battery of \(16\) algebra–record–future triples, computing
\(\Phi(q'_s)\) as exact matrices on one side and the support relation on the
other, with zero disagreements.

Contrapositively, "the images of distinct blocks are pairwise disjoint"
says: for every later atom, all earlier atoms reaching it lie in one block.
That is (H-avail) verbatim.

### 2.4 Nondegeneracy of the adopted definition

### Theorem 2.6 — the availability form does not collapse `[FIX]`

On the earned fixtures the adopted family is a proper nonempty subset of the
admitted futures. Of the \(16\) triples of the concrete battery, \(9\) lie
inside and \(7\) lie outside. Inside, and not the identity, are: the
bit-flip on the classical bit; the intra-block unitary \(X\oplus1\) on
\(M_2\oplus\mathbb C\); the sector-keeping reprepare on
\(M_2\oplus\mathbb C\); the eraser-core reprepare on \(\mathbb C^5\); and
the success/failure keeping channel on \(M_4\oplus\mathbb C\). Outside are
the no-write reset and the reprepare-to-a-point channel on the classical
bit; the sector-merging reprepare and the reset into sector zero on
\(M_2\oplus\mathbb C\); the merge of two eraser outcomes and total erasure
on \(\mathbb C^5\); and total erasure on \(M_4\oplus\mathbb C\).

The intra-block unitary matters: it is a nontrivial admitted future that
changes the boundary and still preserves the record, so membership is not
secretly "is the identity."

Every future inside recovers the record with deficit exactly zero, by an
exhibited readout rather than an estimate; every future outside collides two
record blocks and therefore carries a strictly positive tester-visible
deficit (Section 5.4).

**The definition adopted for the rest of this paper is Definition 2.3.**
This adoption, with Theorem 2.1 as its justification and Theorem 2.6 as its
nondegeneracy certificate, is the first theorem-grade deliverable of the
unit.

---

## 3. The Galois connection

### 3.1 The two posets

Let \(\mathbb I(S)\) be the set of complete admitted nondisturbing
repeatable classical instruments on \(S\) modulo outcome relabelling,
ordered by refinement: \(M\sqsubseteq M'\) when \(M'\) refines \(M\). Let
\(\mathbb F(S)\) be the powerset of the admitted futures out of \(S\),
ordered by inclusion.

### Lemma 3.1 — records are partitions `[FIN]`

At the earned scope \(\mathbb I(S)\) is isomorphic to the partition lattice
of \(\mathcal A(S)\), with the trivial one-outcome record as least element
and \(\operatorname{Cl}_{\mathrm{op}}(S)\) as greatest.

This is the inherited finest-instrument theorem together with the inherited
sharpness corollary. The corollary was recomputed here on an exact rational
grid: over \(25\), \(125\) and \(3375\) candidate stochastic
postprocessings at two and three atoms, every exclusive repeatable one has
coefficients in \(\{0,1\}\), with zero non-sharp violations. The record
poset used below is therefore the earned one, not an assumption.

### Lemma 3.2 — the finest preserved record `[FIN]`, `[EXH-4]`

For an admitted future \(F\), let \(\operatorname{comp}(F)\) be the partition
of \(\mathcal A(S)\) into connected components of the collision graph
\(k\sim l\) iff \(\operatorname{sup}(k)\cap\operatorname{sup}(l)\neq\emptyset\).
Then \(\operatorname{comp}(F)\) is the finest record \(F\) preserves, and

\[
F\in\operatorname{Pres}(\pi)\iff\operatorname{comp}(F)\ \text{refines}\ \pi.
\]

**Proof.** Atoms whose images collide must share a block, or their images
collide; and distinct components have disjoint image-unions by construction.
So \(\operatorname{comp}(F)\) satisfies the criterion of Proposition 2.5 and
every partition satisfying it is coarser. \(\square\)

Lemma 3.2 was checked against Definition 2.3's criterion exhaustively over
all left-total sector relations at atom counts \(2\), \(3\) and \(4\) — that
is \(9\), \(343\) and \(50{,}625\) relations, \(761{,}108\) membership tests
in total — and over a declared subfamily of \(84{,}375\) relations at atom
count \(5\) (\(4{,}387{,}500\) tests), with zero mismatches.

### 3.2 Antitone monotonicity, both ways

### Proposition 3.3 — Pres is antitone `[FIN]`, `[EXH-4]`

If \(M\sqsubseteq M'\) then \(\operatorname{Pres}(M')\subseteq\operatorname{Pres}(M)\).

**Proof.** A block of the coarser record is a union of blocks of the finer
one, so its image is the corresponding union of images; unions of pairwise
disjoint families indexed by disjoint index sets stay disjoint. The
recovering instrument is the matching coarse-graining of \(M'\)'s, admitted
by the inherited coarse-graining closure. \(\square\)

Verified on \(3{,}504{,}535\) strict-refinement tests.

### Proposition 3.4 — Core is well defined `[FIN]`

For a future family \(\mathcal G\), the set
\(\{\,M:\mathcal G\subseteq\operatorname{Pres}(M)\,\}\) is nonempty and
closed under common refinement, hence has a greatest element

\[
\operatorname{Core}(\mathcal G)
=\text{the finest record preserved by every }F\in\mathcal G,
\]

equal to the partition generated by the union of the equivalence relations
\(\operatorname{comp}(F)\), \(F\in\mathcal G\).

**Proof.** The trivial record is always preserved, since \(\Phi(1)=1\). For
closure, let \(M,N\) both be preserved by \(F\), with readouts \(M',N'\).
Their outcome effects are split projections on the later boundary and
therefore commute; by the inherited sequential closure their products are
the outcome effects of an admitted instrument. By Lemma 2.4 each \(q'\) lies
in the multiplicative domain of \(\Phi\), so
\(\Phi(q'^M_rq'^N_t)=\Phi(q'^M_r)\Phi(q'^N_t)=z^M_rz^N_t\), which is the
outcome effect of the common refinement. Finiteness then gives a greatest
element. \(\square\)

Join-closure was verified on all \(2,5,15,52\) distinct preserved-record
sets at atom counts \(2\) to \(5\), which by Lemma 3.2 is exhaustive since
the preserved set depends on \(F\) only through \(\operatorname{comp}(F)\).

### Proposition 3.5 — Core is antitone `[FIN]`, `[FIX]`

If \(\mathcal G\subseteq\mathcal H\) then
\(\operatorname{Core}(\mathcal H)\sqsubseteq\operatorname{Core}(\mathcal G)\).
Immediate from Proposition 3.4; verified on \(93{,}375\) declared family
pairs at atom counts \(3\), \(4\) and \(5\).

### Theorem 3.6 — the antitone Galois connection `[FIN]`

For every record \(M\) and every future family \(\mathcal G\),

\[
\mathcal G\subseteq\operatorname{Pres}(M)
\iff
M\sqsubseteq\operatorname{Core}(\mathcal G).
\]

Hence \(\operatorname{Core}\circ\operatorname{Pres}\) is a closure operator
on records and \(\operatorname{Pres}\circ\operatorname{Core}\) is a closure
operator on future families; the two closed posets are dually isomorphic,
and the fixed points of the first are exactly the closed records.

**Proof.** Left to right: \(M\) belongs to the set whose greatest element is
\(\operatorname{Core}(\mathcal G)\). Right to left: \(\mathcal G\subseteq
\operatorname{Pres}(\operatorname{Core}(\mathcal G))\subseteq
\operatorname{Pres}(M)\) by Proposition 3.3. The closure-operator and duality
statements are the standard consequences of an antitone Galois connection
between posets. \(\square\)

The adjunction was verified as a two-sided equivalence on \(30{,}422\) tests
over declared families at atom counts \(2\) to \(5\); extensivity,
monotonicity and idempotence were verified for all records at atom counts
\(1\) to \(5\); the dual closure and the bijection of closed records with
closed families were verified exhaustively at atom counts \(2\), \(3\) and
\(4\), giving matching counts \(2,5,15\) on both sides.

### 3.3 The alternative reading is not a Galois connection

One might instead take the right adjoint to be the predecessor
construction: send a task family to the operational core of its minimal
sufficient boundary. That map is not antitone.

### Theorem 3.7 — the minimal-boundary core is not antitone `[FIX]`

Let \(\mathfrak F_1\) be the preserving branch-memory task and
\(\mathfrak F_2\) the eraser task. Then
\(\mathfrak F_1\subseteq\mathfrak F_1\cup\mathfrak F_2\), while

\[
\operatorname{Cl}_{\mathrm{op}}(B_{\mathfrak F_1})
\ \text{has}\ 1\ \text{atom},
\qquad
\operatorname{Cl}_{\mathrm{op}}(B_{\mathfrak F_1\cup\mathfrak F_2})
\ \text{has}\ 5\ \text{atoms}.
\]

Antitonicity would require the larger family to give the coarser core; it
gives the strictly finer one.

**Proof.** The corrected minima are recomputed here rather than quoted. For
the preserving task all four source branches give the same complete
distribution, so no two likelihood columns are separated and the minimal
sufficient classical experiment is \(\mathbb C\). For the eraser task the
complete distributions are \(q_j(\bot)=3/4\) and \(q_j(k)=(1/4)\delta_{jk}\)
on \(\{\bot,0,1,2,3\}\); the sink column is constant in \(j\) and the four
success columns are pairwise non-proportional, so no letters merge and the
minimal sufficient classical experiment is \(\mathbb C^5\). For the tagged
bundle with a parameter-independent fair selector the constant columns merge
with one another and the four success columns stay separate, giving five
classes again. \(\square\)

The Galois machinery of Theorem 3.6 therefore belongs to the availability
relation, not to the minimal-boundary construction. This is a definitional
consequence, and it is recorded because the two are easily conflated.

---

## 4. Fixed points

Write \(\operatorname{cl}=\operatorname{Core}\circ\operatorname{Pres}\).

Call the admitted law **reprepare-closed** (condition R) when for every
admitted record \(\pi\) the channel "read the block label of \(\pi\),
discard the rest, reprepare a fixed state inside the image block" is
admitted. This is a laboratory condition on the fixed one-boundary law; it
holds for the standard finite channel law of every committed fixture.

### 4.1 The trivial fixed point, and its exact condition

### Proposition 4.1 — when the trivial record is fixed `[FIN]`

The trivial one-outcome record is a fixed point of \(\operatorname{cl}\) if
and only if the admitted future family contains a future that preserves no
nontrivial record. Under condition R the total-erasure channel is such a
future, so the trivial record is fixed. Under a law admitting only the
identity future it is not: there \(\operatorname{cl}\) is constant at
\(\operatorname{Cl}_{\mathrm{op}}(S)\), so the trivial record fails to be
closed whenever the core has at least two atoms.

**Proof.** By extensivity the trivial record is fixed exactly when
\(\operatorname{Core}(\operatorname{Fut}(S))\) is trivial, which by
Proposition 3.4 says the generated partition of the
\(\operatorname{comp}(F)\) is the one-block partition, that is, some \(F\)
has \(\operatorname{comp}(F)\) trivial. For the identity future
\(\operatorname{comp}\) is the discrete partition, so an identity-only law
gives \(\operatorname{Core}=\operatorname{Cl}_{\mathrm{op}}(S)\). \(\square\)

This refines the expectation that the trivial instrument is always a fixed
point. It is always fixed under R, which is the case of interest, but the
unqualified statement is false: a law with no erasing future has the
operational core as its only fixed point. Both directions were verified at
atom counts \(1\) to \(5\).

### 4.2 The characterization: the closure is the identity

### Theorem 4.2 — every record is a fixed point `[FIN]`, `[EXH-4]`

Under condition R, \(\operatorname{cl}=\operatorname{id}\) on
\(\mathbb I(S)\). The fixed-point set is the entire record lattice.

**Proof.** Extensivity gives \(\pi\sqsubseteq\operatorname{cl}(\pi)\). For
the converse, let \(R_\pi\) be the reprepare future of \(\pi\), with
\(\operatorname{sup}(k)=\{\min B\}\) for \(k\in B\in\pi\). Its images are the
singletons \(\{\min B\}\), pairwise disjoint, so
\(R_\pi\in\operatorname{Pres}(\pi)\). If \(\sigma\) strictly refines \(\pi\),
some block \(B\in\pi\) splits, and the two parts have the same image
\(\{\min B\}\), so \(R_\pi\notin\operatorname{Pres}(\sigma)\). Hence no
record strictly finer than \(\pi\) is preserved by all of
\(\operatorname{Pres}(\pi)\), and \(\operatorname{cl}(\pi)=\pi\).
\(\square\)

The witness was constructed and checked for all \(359\) strictly-refining
record pairs at atom counts \(2\) to \(5\). Independently,
\(\operatorname{cl}(\pi)\) was recomputed from the *exhaustive* future family
rather than from generators at atom counts \(2\), \(3\) and \(4\), and the
inclusion lattice of the preserving families was compared with the
refinement order over all \(50{,}625\) relations at atom count \(4\): the two
agree exactly. Fixed-point counts are \(1,2,5,15,52\) out of \(1,2,5,15,52\)
records.

### Corollary 4.3 — existence, and its emptiness `[FIN]`

Nontrivial fixed points exist exactly when
\(\operatorname{Cl}_{\mathrm{op}}(S)\) has at least two atoms. On the
committed fixtures the counts are: classical bit \(2\) of \(2\); the mixed
control \(M_2\oplus\mathbb C\) \(2\) of \(2\); the corrected eraser minimum
\(\mathbb C^5\) \(52\) of \(52\); the corrected tomographic minimum
\(M_4\oplus\mathbb C\) \(2\) of \(2\); the manufactured \(2{+}1{+}1\)
boundary \(15\) of \(15\); the manufactured \(2{+}2\) boundary \(5\) of
\(5\). Where the core is trivial — the full matrix factor \(M_2\), the
corrected preserving minimum \(\mathbb C\) — the only fixed point is the
trivial record.

So `RQ0-L0-NO-NONTRIVIAL-FIXED-POINT` is refuted. But a closure operator
that is the identity partitions nothing: the fixed-point condition is
satisfied by every record and therefore distinguishes none. Existence here
is not evidence of selection; it is evidence of vacuity.

### 4.3 The composite reading collapses to a constant

The other reading of the target closure keeps the predecessor's right-hand
side: send a record \(M\) to the operational core of the minimal sufficient
boundary of its preserving family,

\[
M\ \longmapsto\ \operatorname{Cl}_{\mathrm{op}}\bigl(B_{\operatorname{Pres}(M)}\bigr).
\]

Here \(B_{\mathcal G}\) is the inherited minimum-rank stabilizing idempotent
of the family \(\mathcal G\): the smallest admitted retract through which
every member factors.

### Theorem 4.4 — the composite map is constant `[FIN]`

The identity future lies in \(\operatorname{Pres}(M)\) for every admitted
record \(M\). Hence \(\operatorname{Stab}(\operatorname{Pres}(M))=\{\mathrm{id}\}\),
\(B_{\operatorname{Pres}(M)}=S\), and the composite map is the constant map
at \(\operatorname{Cl}_{\mathrm{op}}(S)\). Its unique fixed point is
\(\operatorname{Cl}_{\mathrm{op}}(S)\) itself.

**Proof.** The identity's sector support is the discrete partition, whose
block images are singletons, so it preserves every record by Proposition
2.5, with \(M'=M\). A stabilizing idempotent \(e\) must satisfy
\(\mathrm{id}\circ e=\mathrm{id}\), so \(e=\mathrm{id}\) and the minimum-rank
stabilizer is the identity. A constant map has exactly its value as its only
fixed point. \(\square\)

The unique fixed point is the object the predecessor cycle already
constructed. This reading therefore re-derives the operational core and adds
nothing; it cannot couple the record to the task, because the family
\(\operatorname{Pres}(M)\) is always rich enough to force the whole
boundary.

### 4.4 The de-smuggling discriminator

The discriminator is mandatory: the manufactured measure must not survive as
a nontrivial fixed point.

### Theorem 4.5 — the manufactured measure survives `[FIX]`

Let \(P\) be a chosen finite projection-valued measure and \(A_P\) the range
of its matched dephasing, so that the manufactured record is the atom
instrument of \(A_P\). Then:

1. under the availability closure, the manufactured record is a fixed point,
   because \(\operatorname{cl}\) is the identity (Theorem 4.2);
2. under the composite reading, the manufactured record is the *unique*
   fixed point, because it equals \(\operatorname{Cl}_{\mathrm{op}}(A_P)\)
   (Theorem 4.4).

Both were run on the two committed rank types. For the matched
\(2{+}1{+}1\) success algebra with its retained sink the centre dimension is
computed to be \(4\), giving a four-atom manufactured record among \(15\)
records, all fixed; for the matched \(2{+}2\) success algebra with sink the
centre dimension is \(3\), giving a three-atom manufactured record among
\(5\) records, all fixed. In both cases the manufactured record equals the
closure's image of itself, and equals the composite reading's unique fixed
point.

**The closure does not de-smuggle.** This is reported as the finding, not
worked around.

### 4.5 Why: the one-boundary covariance obstruction

The failure is not a defect of Definition 2.3 or of the closure. It is
structural.

### Theorem 4.6 — no one-boundary criterion can de-smuggle `[FIN]`

Let \(P\) and \(Q\) be projection-valued measures with the same rank
multiset. The manufactured boundaries \(A_P\) and \(A_Q\) are carried onto
each other by an admitted reversible operational equivalence, which permutes
the core atoms. The same holds between a manufactured boundary and any
legitimately derived boundary of the same sector type. Since every object
constructed in this paper is defined from the triple (boundary, admitted
law, admitted instruments), and since admitted reversible complete-order
automorphisms act on the split-projection algebra by conjugation and
therefore permute its atoms, every such object is covariant under exactly
these maps. Hence no criterion definable from one-boundary data can accept
one boundary and reject the other.

**Proof.** Choose a unitary \(V\) with \(VP_rV^*=Q_r\); it exists precisely
because the rank multisets agree. Conjugation by \(V\) is an admitted
reversible map carrying \(A_P\) onto \(A_Q\), the admitted law onto the
admitted law, and the core atoms bijectively onto the core atoms. The
covariance statement is the inherited symmetry corollary. A covariant
predicate takes the same value on isomorphic arguments. \(\square\)

The concrete witness recorded here is the sharpest available: the corrected
eraser minimum \(\mathbb C^5\), which is a *legitimately derived* record —
it comes from an independently declared eraser task, not from a chosen
measure — is carried onto a manufactured five-outcome boundary by the exact
permutation \(V\) of the cyclic shift \((1,2,3,4,0)\), verified unitary over
the integers, whose induced map on core atoms is a bijection. The two
boundaries are operationally the same object. A closure that rejected the
manufactured one would have to reject the legitimate one.

The smuggling does not happen inside the boundary. It happens in the choice
of boundary. A fixed-point condition posed inside one boundary cannot see
it, because the carrier of the condition is itself the smuggled object.

This is what changes the programme's route. De-smuggling cannot be a
one-boundary test; it requires a scope in which the boundary is not given in
advance — where several independently declared tasks and their boundaries
are compared. That scope is not opened here.

---

## 5. Controls

All four carried control families are run in both directions.

### 5.1 The branch-memory triple

The corrected minima are recomputed from the committed complete
distributions rather than quoted.

| Task | Minimum | Core atoms | Records | Fixed |
|---|---|---|---|---|
| preserving | $\mathbb C$ | 1 | 1 | 1 |
| eraser | $\mathbb C^5$ | 5 | 52 | 52 |
| retained tomographic | $M_4\oplus\mathbb C$ | 2 | 2 | 2 |

**Positive direction.** Every admitted record on each of the three minima is
a fixed point. The tomographic core has exactly two atoms and its
distribution is \((1/4,3/4)\) for every source label, so the only
nondisturbing classical label says whether the preparation succeeded and
carries no branch information.

**Negative direction — the required one.** The five-atom eraser core is
*not* promoted to a record seam. Its restriction to the four branch labels
is the discrete partition, which is none of the nine inherited coarse
partition seams; those nine were computed, not typed, as the six
\(2{+}1{+}1\) partitions and the three \(2{+}2\) partitions of a four-element
set. Moreover all \(52\) records on the five-atom core are equally fixed, so
the closure prefers none of them. The additional complex rank-two seam is
excluded by type: it is not a partition of the branch set.

### 5.2 The hostile operator system

Let

\[
S=\operatorname{span}_{\mathbb C}\{(I,I),(Z,Z),(X,2X+Z)\}\subset M_2\oplus M_2.
\]

All of the following are recomputed exactly. \(s_2^2=(I,5I)\), so the
generated algebra contains \(z_1=(5s_0-s_2^2)/4=(I,0)\) and
\(z_2=(s_2^2-s_0)/4=(0,I)\), giving \(C^*(S)=M_2\oplus M_2\). Neither summand
can be removed by a boundary quotient: the squared norms drop from \(5\) to
\(1\) for \(s_2\) and from \(10\) to \(8\) for \(-3s_1+s_2\), so
\(C^*_e(S)=M_2\oplus M_2\). The intersection \(S\cap Z(C^*_e(S))\) is
computed by exact linear solve to have dimension \(1\). The state witness
confirms the point operationally: every \(\varphi_\lambda\) restricts to the
same state on \(S\), with values \(1,0,0\) on the generators, while
\(\varphi_\lambda(z_1)=\lambda\); at the sampled weight \(\lambda=3/7\) the
computed value is \(3/7\).

**Negative direction.** Because a nontrivial split would place a nontrivial
central projection of the envelope inside \(S\), and the computed
intersection dimension is \(1\), the only admitted split is trivial. The
core has one atom and the fixed-point set is the singleton \(\{\text{trivial
record}\}\): no nontrivial fixed point exists there.

**Positive direction.** The readable direct sum \(M_2\oplus M_2\) itself,
with both central branches admitted, has a two-atom core and two fixed
points. The machinery fires when the split is physically readable and stays
silent when it is not.

### 5.3 Ordinary finite $C^*$-controls

**Positive.** Where the central-sector branches are physically readable the
fixed points recover exactly the minimal central projections. The centre
dimension is computed for each fixture by an exact commutant solve, never
typed: \(\mathbb C^2\) gives \(2\); \(M_2\oplus\mathbb C\) gives \(2\);
\(\mathbb C^5\) gives \(5\); \(M_4\oplus\mathbb C\) gives \(2\); the
manufactured \(2{+}1{+}1\) with sink gives \(4\); the manufactured
\(2{+}2\) with sink gives \(3\).

**Negative, factor.** On a full matrix factor the Choi operator of the
identity channel has computed rank \(1\) at dimensions \(2\), \(3\) and
\(4\); a completely positive map dominated by it is a scalar multiple of the
identity, and idempotence forces the scalar to be \(0\) or \(1\). The core is
trivial and the only fixed point is the trivial record.

**Negative, unadmitted filters.** Under the restricted law in which the two
coordinate filters are not admitted operations, the admitted splits are
\(\{\emptyset,\{0,1\}\}\) and the computed core has \(1\) atom, although the
algebraic centre of the same algebra \(\mathbb C^2\) has computed dimension
\(2\). Enlarging the law to admit both coordinate branches returns a core
with \(2\) atoms. Admission is measured, not inferred from algebraic
existence.

**Negative, scalar positivity.** The transpose symmetrizer
\(P=\tfrac12(\mathrm{id}+\tau)\) is positive, unital and idempotent, but its
Choi expectation on the normalized antisymmetric vector is computed to be
exactly \(-1/2\). Scalar positivity does not supply an admitted branch.

### 5.4 No-write control and tester-visible stability

**Positive.** The no-write reset lies outside \(\operatorname{Pres}(M)\) for
the two-atom record, and its failure is measured, not definitional: the two
written settings are distinguishable at total variation \(1/2\), and the
optimal recovery deficit after the reset is exactly \(1/4\), matching the
analytic lower bound \(\operatorname{TV}(p_0,p_1)/2\). The exact coherence
loss of the preserving dephasing is recomputed from the purity invariant:
the off-diagonal modulus squared is \(3/16\) and the squared trace norm is
\(3/4\), that is the committed \(\sqrt3/2\).

**Negative.** The same reset lies *inside* \(\operatorname{Pres}\) of the
trivial record with deficit exactly zero. The criterion does not reject
futures indiscriminately.

**Stability, both directions.** Across the concrete battery, all \(9\)
futures inside the preserving family recover the record with deficit exactly
zero by an exhibited readout, and all \(7\) futures outside collide two
record blocks, which certifies a strictly positive tester-visible deficit
because no later readout can separate two blocks that reach a common sector.

---

## 6. Verdict

\[
\boxed{\texttt{RQ0-L0-BLOCKED-AT-DE-SMUGGLING}}
\]

registered as an instance of the pre-registered outcome
`RQ0-L0-BLOCKED-AT-⟨object⟩`, with the un-typed object being **a
task-independent selector on the fixed-point set**.

The other two pre-registered outcomes are dispositioned explicitly.

- `RQ0-L0-W3-OPERATIONAL-MARKOV-BOUNDARY` — **not earned.** Two of its three
  conditions hold: nontrivial fixed points exist (Corollary 4.3) and are
  fully characterized (Theorem 4.2). The third fails: smuggling is not
  rejected (Theorem 4.5), and Theorem 4.6 shows it could not have been
  rejected at this scope.
- `RQ0-L0-NO-NONTRIVIAL-FIXED-POINT` — **refuted.** Under the availability
  closure every admitted record is a fixed point; under the composite
  reading the unique fixed point is the operational core, which is
  nontrivial whenever the boundary is a genuine readable direct sum.

**Scope of the verdict.** Finite dimension; one boundary; one admitted
process law; the earned #103 and #111 fixtures. Exhaustive over all
left-total sector relations at atom count at most \(4\); a declared
subfamily at atom count \(5\); the general case carried by Lemma 3.2, which
is proved, not sampled.

**What is nevertheless earned.** The definitional repair and its
nondegeneracy certificate (Theorem 2.1, Definition 2.3, Theorem 2.6); the
sector criterion and its identification with the predecessor availability
hypothesis (Proposition 2.5); the Galois connection and its closure
operators (Theorem 3.6); the non-antitonicity of the minimal-boundary core
(Theorem 3.7); the exact characterization of the fixed points (Theorem 4.2)
and of the composite reading (Theorem 4.4); the exact condition for the
trivial record to be fixed (Proposition 4.1); and the one-boundary
covariance obstruction (Theorem 4.6).

**The next obstruction, named.** De-smuggling is not a property of a
boundary. It requires comparing several independently declared tasks and the
boundaries they induce, in a setting where the boundary is not supplied in
advance. Until such a scope is constructed and typed, a record remains
task-relative.

---

## 7. Non-claims

This paper claims none of the following.

- No task-independent record, and no W3 rung of any kind.
- No claim about how two boundaries combine; that question is untouched.
- No locality, region, overlap, atlas, topology or manifold structure.
- No influence, causal order, spacetime or Lorentzian object.
- No field, QCD or gravity object.
- No actual outcome selection, no fact co-reference, no event-token
  identity.
- No autonomous subsystem or intrinsic chart.
- No claim that the availability form is the only possible repair; it is the
  one adopted, justified and gated here.
- No claim beyond the declared verification scope: the general-atom-count
  statements rest on Lemma 3.2 and Theorem 4.2 as proved, with the
  computations serving as independent checks.

The word "boundary" means one task-relative process interface. The word
"classical" means a retained outcome of a complete nondisturbing repeatable
instrument. The word "record" means such an instrument, up to outcome
relabelling.

---

## 8. Reproduction

Single file, exact arithmetic, no external dependencies:

```
v13/code/rq0_l0_fixed_point_exact.py
```

Outputs, both written deterministically by the run itself:

```
v13/code/rq0_l0_fixed_point_output.txt
v13/code/rq0_l0_fixed_point_receipt.json
```

Commands:

```
python3.13 v13/code/rq0_l0_fixed_point_exact.py
python3.13 v13/code/rq0_l0_fixed_point_exact.py --falsification-selftest
```

**Totals.** 57 gates, 57 passed, none failed. 34 anchors, 34 passed;
anchors are exit-1-only, so any mismatch with a committed value kills the
run before a receipt is written. Runtime approximately 60 seconds; the
declared cap is 45 minutes.

**Determinism.** Two consecutive full runs produce byte-identical output and
receipt files. No wall-clock value enters either file; timings appear only
on the progress stream.

**Exactness.** The run begins by auditing its own source: zero float
literals and zero float-producing calls, detected structurally on the
abstract syntax tree rather than by substring. Every anchor value is
required to be an exact type; the receipt records zero type violations. All
arithmetic is over the rationals or over the Gaussian rationals, with rank
and nullity computed by exact elimination.

**Falsification self-test.** Six mutants each break exactly one committed
anchor — the corrected eraser minimum, a hostile-system squared norm, the
tomographic core distribution, the transpose-symmetrizer Choi value, the
count of inherited seams, and the squared coherence loss. All six are
killed: each exits 1 with a printed anchor failure.

**Anchors reused.** From the minimal-boundaries cycle: the preserving
dephasing laws \((3/4,1/4)\) and \((1/4,3/4)\); the no-write reset outputs
\((1/2,1/2)\); the squared coherence loss \(3/4\); the corrected minima
\(\mathbb C\), \(\mathbb C^5\) and \(M_4\oplus\mathbb C\); the matched
\(2{+}1{+}1\)-with-sink centre dimension \(4\) and the matched
\(2{+}2\)-with-sink centre dimension \(3\); the nine inherited seams. From
the classical-core cycle: the instrument axioms; \(s_2^2=(I,5I)\); the
squared norms \(5,1,10,8\); \(\dim(S\cap Z(C^*_e(S)))=1\); the state values
\(1,0,0\) and \(\varphi_\lambda(z_1)=\lambda\); the Choi rank \(1\); the
transpose-symmetrizer value \(-1/2\); the core atom counts \(1,5,2\); the
success/failure distribution \((1/4,3/4)\).

**Independent cross-checks.** Record-lattice sizes are compared between the
partition enumerator and the Bell triangle recurrence, never against
themselves. Relation-family sizes are compared with the closed-form count.
The sector criterion is compared with the matrix-level definition on the
whole concrete battery. The closure is computed both from generators and
from the exhaustive future family.

---

## References

1. M.-D. Choi, "A Schwarz inequality for positive linear maps on
   \(C^*\)-algebras," *Illinois Journal of Mathematics* **18** (1974),
   565–574. https://doi.org/10.1215/ijm/1256051007
2. M.-D. Choi and E. G. Effros, "Injectivity and operator spaces,"
   *Journal of Functional Analysis* **24** (1977), 156–209.
   https://doi.org/10.1016/0022-1236(77)90052-0
3. B. A. Davey and H. A. Priestley, *Introduction to Lattices and Order*,
   2nd ed., Cambridge University Press, 2002.
4. M. Erné, J. Koslowski, A. Melton and G. E. Strecker, "A primer on Galois
   connections," *Annals of the New York Academy of Sciences* **704**
   (1993), 103–125. https://doi.org/10.1111/j.1749-6632.1993.tb52513.x
5. M. Koashi and N. Imoto, "Operations that do not disturb partially known
   quantum states," *Physical Review A* **66** (2002), 022318.
   https://arxiv.org/abs/quant-ph/0101144
6. Y. Kuramochi, "Minimal sufficient statistical experiments on von Neumann
   algebras," *Journal of Mathematical Physics* **58** (2017), 062203.
   https://doi.org/10.1063/1.4986247
7. Y. Kuramochi, "Accessible information without disturbing partially known
   quantum states on a von Neumann algebra," *International Journal of
   Theoretical Physics* **57** (2018), 2249–2266.
   https://doi.org/10.1007/s10773-018-3749-8
8. V. I. Paulsen, *Completely Bounded Maps and Operator Algebras*,
   Cambridge University Press, 2002.
9. D. Blackwell, "Equivalent comparisons of experiments," *Annals of
   Mathematical Statistics* **24** (1953), 265–272.
   https://doi.org/10.1214/aoms/1177729032

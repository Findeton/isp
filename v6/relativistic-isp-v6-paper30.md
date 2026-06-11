# Paper 30 (v6) - SHARD: The Chirality Wall - the Spectral Half of (PR-RP+)

Preprint, not peer reviewed, version 2026-06-11.

Author: Felix Robles Elvira

Subtitle:

```text
A mathematical campaign on the corpus' deepest open problem.
(PR-RP+) asserts that record positivity equals sealability: every
bond-reflection-positive stochastic process of finite rank admits a
finite POSITIVE realization - no clock can hide inside a sealed
ledger.  After Paper 27 the obstruction had one known shape (a block
diagonal oscillating irrationally on its decay circle) and one
empirical wall (complex block spectra stay subordinate, s <= 0.205).
This paper turns most of that picture into THEOREMS.  First, an
exhaustion result: once a process has the RP-form, every reflected
Gram is automatically positive - reflection is spent, and the entire
remaining force of the problem is WORD POSITIVITY.  Second, the
ACHIRAL NECKLACE THEOREM: a block whose cyclic word equals its own
reversal up to rotation factors (through a rotation) into a product
of two palindromes; palindromic blocks are exactly positive
semidefinite; therefore every achiral block has real nonnegative
spectrum at every length - subsuming and extending Paper 27's
Theorem PR2 (length <= 4 -> all of length <= 5, plus infinite
families at every length), and proving that complex block spectra
live ONLY on chiral necklaces (first at length 6).  Third, the
STIELTJES STRUCTURE: palindromic-phase diagonals of valid processes
are exact Stieltjes moment sequences; every rotation keeps real
nonnegative poles with (genuinely) signed residues; with the
dominant-pole criterion of positive-realization theory, every
achiral-block diagonal is positively realizable.  CONSEQUENCE (the
Confinement Theorem): any clock obstruction inside a valid RP
process is confined to chiral-necklace blocks of length >= 6 - the
arrow-of-time witness needs a time-asymmetric word, a resonance the
corpus did not order but gratefully records.  The chiral core is
then attacked: random valid processes show NO coupled complex poles
at all (120/120 samples, s = 0); an inverse-design attack produces a
deeply valid process with coupled complex poles at s = 0.1866
(constructive existence - the conjecture must allow subordinate
coupling) but never reaches the circle; every s = 1 candidate breaks
word positivity at an explicit witness word; and the Weyl mechanism
is exhibited in one receipt (lifting the champion's complex pair to
the circle forces h(n) < 0 at n = 32).  The final form of the open
problem is stated as the CHIRAL PERIPHERAL EXCLUSION conjecture,
with the torus-positivity constraints any proof or counterexample
must negotiate.  The assembly half (one cone for the whole process)
is untouched and stated with its literature anchors.
  THE CPE CAMPAIGN (second movement of this paper): every route we
could imagine to prove or falsify (CPE) was then exhausted at our
scope.  The PERIPHERAL REDUCTION THEOREM makes the dangerous
configuration finite-dimensional: every word in a chiral block W and
its reversal evaluates EXACTLY as a torus form of reduced data
(G, beta) - theta-free, any rank.  Climbing the alternation tower
numerically, the campaign then found - and proved - the NORMAL
ESCAPE: normal-block data (G = I) passes the ENTIRE tower at full
clock strength, so the (B, B-dagger) subalgebra can never prove
(CPE).  The letters answer back: the NR PHENOMENON - normality of
chiral two-letter words is reachable at machine precision but ALWAYS
with real spectrum (conjecture (NR); Ballantine's five-factor
theorem makes this a strictly two-letter effect); and the deep
adversary (exact coordinate-descent over chain phases) shows the
tower's shallow plateau was an artifact: the depth-5 survivor dies
at depth 8, and the all-depth question becomes the ISOLATION of the
normal point (conjecture (ISO)), whose measured evidence is mixed:
finite-depth deaths alongside a 64-phase survivor - open, as stated.
NET RESULT: (CPE) is REDUCED to (NR) and (ISO) - two sharp,
finite-dimensional, independently attackable conjectures, both
machine-receipted, via the conditional theorem
(NR) + (ISO) => (CPE) at stated scope.  A fake near-counterexample
(the P27 impostor mechanism, negativity hidden at word length ~150)
was caught live and is documented
```

## 0. Verdict

```text
PROVED (with machine receipts):
  T3.1  Reflection is exhausted: in the RP-form, all reflected Grams
        are automatically PSD (receipt: an engineered INVALID process,
        min p(w) = -4.6e-3, whose reflected Gram has eig_min
        = -1.8e-17).  Word positivity is the whole remaining problem.
  T4.5  ACHIRAL NECKLACE THEOREM: achiral necklace => real
        nonnegative block spectrum, every length.  Ingredients:
        the reflection-axis lemma (achiral <=> a rotation is a
        product of two palindromes; verified both ways, all lengths
        <= 12), the palindrome factorization B = C C^dag or
        C A_mid C^dag (exact in integer arithmetic, error = 0), and
        the classical two-PSD-product fact.  Corollary: ALL blocks of
        length <= 5 (every class achiral; PR2's length-4 bound is
        subsumed and extended).
  T5.1  Palindromic-phase diagonals of valid RP processes are EXACT
        Stieltjes moment sequences (receipt: both Hankels PSD at
        -1.3e-16 over 40 valid processes).
  T5.2  Achiral diagonals at EVERY phase are signed-Stieltjes: real
        nonnegative poles, real (sign-changing: receipt -0.32)
        residues - no oscillatory component at any phase.
  C5.3  Achiral diagonals are positively realizable (dominant-pole
        import from positive-realization theory).
  T5.4  CONFINEMENT: any Theorem-B clock obstruction in a valid RP
        process lives on a CHIRAL-necklace block, length >= 6.
EMPIRICAL (the chiral core, honestly tagged):
  - the corrected reality map: complex block spectra are realized on
    7/7 probed chiral classes - including the FIRST chiral pair at
    L = 6 (|Im|/rho up to 1.0) - correcting P27's weaker-search map;
  - random valid processes: coupled complex poles NEVER appear
    (120/120 samples, all seven chiral blocks: s = 0.000);
  - inverse design: a deeply valid process with coupled complex
    poles EXISTS (s = 0.1866, passes scan |w| <= 14 + all chiral
    diagonals to depth 2000) - the wall is approached, not crossed;
    every candidate at s = 1 fails validity at an explicit word
    (witness: p(101010100000) = -4.0e-6);
  - the mechanism: lifting the champion's pair to the circle
    (residues fixed) forces h(n) < 0 first at n = 32.
OPEN (named): (CPE) Chiral Peripheral Exclusion - no valid RP
  process couples nonreal poles on a block diagonal's maximal-
  modulus circle with irrational phase.  Proving (CPE) closes the
  spectral half of (PR-RP+).  The ASSEMBLY half (one positive cone
  for the whole process) is independent and untouched.

THE CPE CAMPAIGN (Sections 7-8; scripts p30c-f):
PROVED:
  T7.1  PERIPHERAL REDUCTION: every (W, W-tilde)-word value of a
        process whose block carries the coupled peripheral triple is
        an exact torus evaluation of finite reduced data (G, beta);
        validity forces torus positivity, theta-free, at any rank
        (validated against brute force at 1.1e-11).
  T7.3  NORMAL ESCAPE: at G = I the ENTIRE alternation tower is
        feasible at clock strength r = 1 - eps (receipt: all margins
        +2e-6 at r = 0.999998, re-receipted to depth 16 by the exact
        adversary at 4e-16 from the Fejer bound).  COROLLARY: no
        proof of (CPE) can come from the block subalgebra alone.
  T7.6  CONDITIONAL REDUCTION: (NR) + (ISO) => (CPE) at stated
        scope - the conjecture is reduced to two finite-dimensional
        statements.
EMPIRICAL (honestly tagged):
  - (NR) receipts: chiral-word normality reachable at 5e-16 yet
    spectrum REAL in every trial (objective rewarded oscillation);
    trade-off wall O(1) (defect 0.27 at 5% demanded oscillation);
    dimension threshold: 001011 always-real at d = 3;
  - the depth-5 tower witness DIES at depth 8 under the exact
    adversary (+0.018 -> -0.055 -> -0.338 by depth 16): shallow
    plateaus are artifacts; but the near-normal band's fate is
    MIXED (p30f): some winners die at finite depth (k* = 16, 48
    across search instances), at least one survives the 64-phase
    adversary, and the eps = 0.05 shell keeps r = 0.84 through
    constraint depth 56 - (ISO) is OPEN, with SOS-certificates as
    the named decider;
  - the validity attack walls at modulus spread 0.799 (s ~ 0.20:
    third independent measurement of the P27 wall); the impostor
    mechanism caught live (negativity at word length ~150, invisible
    to letter scans) - the deep diagonal check is structural.
```

## 1. Method and reproducibility

```text
code/v6_p30a_achiral_necklace.py   exhaustion receipt; necklace
                                   census + two-palindrome lemma
                                   (both directions, L <= 12); exact
                                   integer palindrome factorization;
                                   spectral sweep + targeted search;
                                   Stieltjes receipts on valid
                                   processes
code/v6_p30b_chiral_core.py        coupled-subordination audit;
                                   inverse-design attack with hard
                                   validity; beyond-wall witnesses;
                                   the peripheral-lift mechanism
                                   receipt
code/v6_p30c_peripheral_reduction.py  the reduction validated; the
                                   depth tower; the normal escape
code/v6_p30d_embedding_attack.py   NR receipts; dimension threshold;
                                   trade-off wall; the validity
                                   attack (impostor-proofed)
code/v6_p30e_nearnormal_band.py    the exact-coordinate adversary;
                                   calibration; witness death; the
                                   eps = 0.05 band
code/v6_p30f_isolation_scaling.py  death depths of band winners;
                                   the deepening trend
code/v6_p30g_nr_detectors.py       the NR detector scan (0/106),
                                   the obstruction theorem, the
                                   d = 2 reality search
code/v6_p30i_d2_theorem.py         the d = 2 floor THEOREM:
                                   interleaving, the invariant arc,
                                   word fixed points
code/v6_p30h_pinch.py              the pinch: letter-reachable
                                   triples vs the tower band in the
                                   shared (G, beta) coordinates;
                                   the wall curve ND_min(im)
```

Fixed seeds; canonical outputs at /tmp/p30a.out, /tmp/p30b.out;
reruns bit-identical.  Validity is always checked by full word scans
(every word to the stated length), never by sampling.  All proofs
in this paper are self-contained; classical ingredients are cited
and no priority is claimed for them (Section 8).

## 2. The problem and its prior state

A stationary binary process $p$ on words $w \in \{0,1\}^*$ is
**bond-reflection-positive (bond-RP)** if for every finite word
family $\{u_i\}$ the matrix $G[i,j] = p(\bar u_i \circ u_j)$ is PSD,
where $\bar u$ is the letter reversal of $u$.  Paper 27's
Proposition 1.1 (the RP-form) shows bond-RP processes are exactly
those of the form

$$
p(x_1 \cdots x_n) \;=\; \langle \Omega,\, A_{x_1} \cdots A_{x_n}\,
\Omega\rangle ,
\qquad A_x \succeq 0 \text{ self-adjoint},\quad
A_0 + A_1 = T,\; T\Omega = \Omega,\; 0 \preceq T \preceq 1 .
$$

**(PR-RP+)** asserts: bond-RP + finite Hankel rank $\Rightarrow$ a
finite **positive** realization exists (entrywise-nonnegative
transfer; "sealability"; capacity may exceed rank).  Paper 16's
record clock shows the assertion fails without RP: there are valid
finite-rank processes whose diagonal $h(n) = p(1^n)$ oscillates
irrationally on its decay circle, and Theorem B shows such a
diagonal admits **no** finite positive realization.  So (PR-RP+)
splits:

- **the spectral half**: no block diagonal of a valid RP process
  carries the Theorem-B obstruction (this paper's subject);
- **the assembly half**: granted the spectral half, build one
  invariant cone for both letters jointly (Section 8).

Prior state (P27): Theorem PR2 (blocks of length $\le 4$ have real
nonnegative spectrum); an empirical reality map (first complex
spectra "at length 7"); an empirical validity wall ($s \le 0.205$
over 1,882 deeply valid samples); the conjecture (PR-RP++).  This
paper replaces the map with a theorem, the bound with a structure
theorem, and the conjecture with its final, reduced form.

## 3. Reflection is exhausted

**Proposition 3.1.**  Let $p$ have the RP-form (self-adjoint PSD
letters), with or without word positivity.  Then every reflected
Gram of $p$ is PSD.

*Proof.*  For a word $u = x_1\cdots x_k$ write
$B_u = A_{x_1}\cdots A_{x_k}$.  Self-adjointness of the letters
gives $B_{\bar u} = B_u^\dagger$.  Hence

$$
G[i,j] \;=\; p(\bar u_i \circ u_j)
\;=\; \langle \Omega,\, B_{u_i}^\dagger B_{u_j}\,\Omega\rangle
\;=\; \langle B_{u_i}\Omega,\, B_{u_j}\Omega\rangle ,
$$

a Gram matrix of the vectors $B_{u_i}\Omega$ — PSD identically.
$\blacksquare$

Receipt: an RP-form sample *engineered to break word positivity*
(minimum $p(w) = -4.6\times 10^{-3}$ over $|w| \le 10$) still has
every tested reflected Gram PSD ($\mathrm{eig}_{\min} = -1.8\times
10^{-17}$, machine zero).  Two consequences, both load-bearing:

1. **Within the form, reflection positivity is spent.**  All
   remaining content of (PR-RP+) is the *word positivity* of the
   non-commutative form — the requirement $\langle\Omega, A_{x_1}
   \cdots A_{x_n}\Omega\rangle \ge 0$ for non-commuting PSD factors,
   which is *not* automatic.
2. **A trap, documented.**  There is an apparent one-line proof of
   the full block-moment theorem: choose "rows" $\bar W^i$ and
   "columns" $W^j$, so that $\mathrm{rev}(\bar W^i)\circ W^j =
   W^{i+j}$ and the Hankel of the block diagonal "is an RP Gram."
   It is not: RP constrains a *single* family against itself.  With
   the honest family $\{B_{\bar W}^i\Omega\} \cup \{B_W^j\Omega\}$
   the Hankel appears only as the **off-diagonal block** of a PSD
   matrix — which, by Proposition 3.1, is automatically PSD anyway
   and so carries no information beyond the form.  Every route to
   the spectral half through reflection alone is closed.
3. **A refinement the CPE campaign later forced** (Section 7): the
   *matrix* positivity of the mixed Grams is automatic, but the
   **entrywise** positivity $p(W^a\tilde W^b) \ge 0$ — each entry
   being a probability — is *not* automatic and is a genuine
   constraint family.  The exhaustion proposition closes reflection,
   not word positivity; the two-segment words are word positivity's
   first nontrivial appearance inside the block algebra.

A third, unplanned finding: for the Perron-state construction used
throughout (letters $G G^{\mathsf T}$, $\Omega$ = top eigenvector of
$T$), word positivity is *generic* — random draws were valid 40/41
and 120/120 times at two mixing strengths, and invalid samples had
to be engineered by explicit minimization.  Why the Perron state
self-aligns with validity this strongly is an open question we flag
and do not answer.

## 4. The Achiral Necklace Theorem

### 4.1 Definitions

The **necklace** of a word $W \in \{0,1\}^L$ is its cyclic class
$\{\sigma^k W\}$ under rotation $\sigma$.  A necklace is **achiral**
if it contains the reversal $\tilde W$ of $W$ (equivalently: the
cyclic word equals its mirror image); otherwise **chiral**.  A word
is a **palindrome** if $W = \tilde W$.

### 4.2 The reflection-axis lemma

**Lemma 4.2.**  A necklace is achiral if and only if some rotation
of it is a product of two palindromes (either factor may be empty).

*Proof.*  ($\Leftarrow$) If $\sigma^k W = uv$ with $u, v$
palindromes, then $\widetilde{\sigma^k W} = \tilde v\,\tilde u = vu
= \sigma^{|u|}(uv)$: the reversal is a rotation, so the class is
achiral.

($\Rightarrow$)  View $W$ as a labeling of the cycle
$\mathbb Z_L$.  Achirality means the labeled cycle is invariant
under some orientation-reversing symmetry of the dihedral group,
i.e. a reflection $r$.  Every reflection of an $L$-cycle has an
axis meeting the cycle in exactly two points: for $L$ odd, one
vertex and one edge midpoint; for $L$ even, two vertices or two
edge midpoints.  Cut the cycle at the two axis points.  Each of the
two resulting arcs is mapped to itself by $r$ with orientation
reversed, so each arc reads as a palindrome (a vertex on the axis
is the central letter of an odd palindrome; an edge-midpoint cut
falls between letters).  Reading the cycle from either cut point
gives a rotation $\sigma^k W = uv$ with $u, v$ palindromes.
$\blacksquare$

Receipt: verified **in both directions** for every binary class of
length $\le 12$ (e.g. at $L = 12$: all 96 achiral classes split,
none of the 256 chiral classes does).  The census:

```text
   L        1   2   3   4   5   6   7   8   9  10   11   12
   classes  2   3   4   6   8  14  20  36  60 108  188  352
   achiral  2   3   4   6   8  12  16  24  32  48   64   96
   chiral   0   0   0   0   0   2   4  12  28  60  124  256
```

Every class of length $\le 5$ is achiral; the first chiral pair is
$\{001011,\, 001101\}$ at $L = 6$.  Note the chiral fraction grows
toward one: the theorem confines the residue exactly, but the
residue class is combinatorially large.

### 4.3 The palindrome factorization

**Lemma 4.3.**  If $u$ is a palindrome, then $B_u \succeq 0$.

*Proof.*  Write $u = x_1\cdots x_m$ with $x_k = x_{m+1-k}$.  If
$m = 2q$, the second half of $u$ is the reversal of the first, so

$$
B_u \;=\; \bigl(A_{x_1}\cdots A_{x_q}\bigr)
          \bigl(A_{x_q}\cdots A_{x_1}\bigr) \;=\; C\,C^\dagger
\;\succeq\; 0 ,
\qquad C = A_{x_1}\cdots A_{x_q}.
$$

If $m = 2q+1$, the same split around the central letter gives
$B_u = C\,A_{x_{q+1}}\,C^\dagger \succeq 0$ since
$A_{x_{q+1}} \succeq 0$.  The empty word gives the identity.
$\blacksquare$

Receipt: in exact integer arithmetic (letters $G^{\mathsf T}G$ with
integer $G$), $|B_{0110} - CC^{\mathsf T}| = 0$ and
$|B_{00100} - C A_1 C^{\mathsf T}| = 0$ — exactly.

### 4.4 Products of two PSD operators

**Lemma 4.4** (classical).  If $P, Q \succeq 0$ then
$\mathrm{spec}(PQ) \subset [0,\infty)$, and the restriction of $PQ$
to its nonzero spectrum is semisimple.

*Proof.*  For invertible $Q$:
$Q^{1/2}(PQ)Q^{-1/2} = Q^{1/2}PQ^{1/2} \succeq 0$, so $PQ$ is
similar to a PSD matrix.  For general $Q$, apply this to
$Q + \varepsilon I$ and let $\varepsilon \to 0$ (eigenvalue
continuity) for the spectral statement; for semisimplicity off
zero, use that $AB$ and $BA$ have the same Jordan structure at
nonzero eigenvalues with $A = PQ^{1/2}$, $B = Q^{1/2}$, the latter
product being self-adjoint.  $\blacksquare$

### 4.5 The theorem

**Theorem 4.5 (Achiral Necklace Theorem).**  Let $W$ be any block
whose necklace is achiral.  Then $\mathrm{spec}(B_W) \subset
[0,\infty)$ — for letters of any dimension, at any block length.

*Proof.*  By Lemma 4.2 some rotation $W' = uv$ with $u, v$
palindromes; by Lemma 4.3, $B_{W'} = B_u B_v$ is a product of two
PSD operators; by Lemma 4.4 its spectrum is real nonnegative.
Rotations preserve nonzero spectra ($\mathrm{spec}(MN)$ and
$\mathrm{spec}(NM)$ agree off zero), so every rotation of $W'$ —
in particular $W$ — has real nonnegative spectrum.  $\blacksquare$

**Corollary 4.6.**  Every block of length $\le 5$ has real
nonnegative spectrum (census: all such classes are achiral).  This
subsumes Paper 27's Theorem PR2 (length $\le 4$, proved there by a
cyclic 2-PSD-factor reduction) and extends it by one full length
and by infinite families at every length.

### 4.6 The corrected reality map

The sweep receipts close the empirical side.  Achiral classes:
imaginary parts at machine zero in every random trial at lengths
6-10 — as the theorem requires; no search can break it.  Chiral
classes under targeted hill-climbing (9 restarts $\times$ 2500
steps, dims 3-5):

```text
   class       best |Im lambda| / rho     status
   001011            0.2980               complex-capable  (L = 6)
   001101            0.0732               complex-capable  (L = 6)
   0001011           1.0000               complex-capable
   0001101           0.9999               complex-capable
   0010111           1.0000               complex-capable
   0011101           0.5318               complex-capable
   00011101          1.0000               complex-capable  (P27 witness)
```

Seven of seven probed chiral classes realize complex spectra —
**including the first chiral pair at $L = 6$**.  This *corrects*
Paper 27's empirical map, which placed the first complex spectra at
length 7 under a weaker search: complex block spectra appear
exactly where chirality first appears.  Chirality is necessary
(Theorem 4.5) and, empirically, sufficient at every class probed.

### 4.7 Literature note

Lemma 4.4 is classical; Lemma 4.3 (palindromic words in PSD letters
are PSD up to similarity) appears in the words-in-positive-matrices
literature around Hillar-Johnson; the two-palindrome
characterization of reversal-conjugate words is known in
combinatorics on words.  We claim no priority for the ingredients.
The assembly — reality of block spectra as a *necklace chirality
invariant*, with the census, the corrected map, and the confinement
corollary below — is, to our knowledge, the useful new step, and it
is the one the corpus needs.

## 5. The Stieltjes structure of achiral diagonals

### 5.1 Exact moments at the palindromic phase

**Theorem 5.1.**  Let $p$ be a valid RP-form process and $W$ a
palindromic block.  Then $h(n) = p(W^n)$ is an exact Stieltjes
moment sequence:

$$
h(n) \;=\; \int_{[0,\,\|B_W\|]} x^{\,n}\, d\mu(x),
\qquad \mu = \langle \Omega, E_{B_W}(\cdot)\,\Omega\rangle \;\ge\; 0,
$$

with at most $\mathrm{rank}$ many atoms.  In particular both Hankel
matrices $[h(i+j+1)]$ and $[h(i+j+2)]$ are PSD.

*Proof.*  $B_W \succeq 0$ self-adjoint (Lemma 4.3); spectral
theorem; $\mu$ is a positive spectral measure.  $\blacksquare$

Receipt: over 40 verified-valid processes and palindromic blocks
$0110$, $00100$, $010010$: relative $\mathrm{eig}_{\min}$ of all
Hankels $= -1.3\times 10^{-16}$ — PSD to machine precision.

### 5.2 Every phase: signed Stieltjes

**Theorem 5.2.**  Let $W$ be any rotation of an achiral block, $r$
the rank.  Then for $n > r$,

$$
h(n) \;=\; p(W^n) \;=\; \sum_k c_k\, \lambda_k^{\,n-1},
\qquad \lambda_k \ge 0,\;\; c_k \in \mathbb R :
$$

real nonnegative poles with real (possibly negative) residues — a
*signed* Stieltjes structure with **no oscillatory component at any
phase**.

*Proof.*  Write the achiral rotation as $W' = PQ$ with
$M = B_{W'} = B_P B_Q$ (two-palindrome split absorbed into Theorem
4.5's factorization), and $W = QP$.  Then

$$
B_W^{\,n} = (B_Q B_P)^n = B_Q\, M^{\,n-1} B_P
\quad\Longrightarrow\quad
h(n) = \bigl\langle B_Q^\dagger \Omega,\; M^{\,n-1}\, B_P\Omega
\bigr\rangle .
$$

By Lemma 4.4, $M$ has real nonnegative spectrum and is semisimple
off zero; any Jordan structure at $0$ contributes only for
$n - 1 < r$.  Expanding $M^{n-1}$ in the (real) spectral projectors
$\Pi_\lambda$ gives $h(n) = \sum_\lambda \lambda^{n-1}
\langle B_Q^\dagger\Omega, \Pi_\lambda B_P\Omega\rangle$; the
coefficients are real because $h$ is real and the $\Pi_\lambda$ are
real for real $\lambda$ on the real form.  $\blacksquare$

Receipt: rotated-phase diagonals across all valid samples have
coupled poles with $\max |\mathrm{Im}\,\lambda|/|\lambda| =
0.0$ exactly, while the most negative coupled residue is $-0.32$:
the *reality* of the poles is phase-invariant, the *positivity* of
the measure is phase-specific.  Both halves of the theorem are
visible in the data.

### 5.3 Positive realizability of achiral diagonals

**Corollary 5.3** (modulo a named import).  Every achiral-block
diagonal of a valid RP process admits a finite positive realization.

*Proof sketch.*  By Theorem 5.2, $h$ is rational with poles in
$[0,\infty)$; validity gives $h(n) \ge 0$.  The pole of maximal
modulus among the coupled set is unique and positive (two real
nonnegative numbers of equal modulus coincide), and its residue is
positive (else $h$ eventually goes negative).  The dominant-pole
sufficient criterion of positive-realization theory (Anderson et
al.; see the Benvenuti-Farina survey) then yields a finite positive
realization, possibly of dimension larger than the rank — exactly
the "capacity may exceed rank" shape (PR-RP+) allows.
$\blacksquare$

### 5.4 The Confinement Theorem

**Theorem 5.4.**  In a valid RP-form process, any block diagonal
carrying the Theorem-B obstruction (nonreal coupled poles; in
particular, irrational oscillation on the decay circle) must be a
**chiral-necklace block of length $\ge 6$**.

*Proof.*  Theorem 5.2 excludes nonreal coupled poles for every
achiral block at every phase; the census places the first chiral
class at length 6.  $\blacksquare$

The corpus pauses on what this says.  The record clock is the
arrow-of-time witness — the structure whose existence separates
sealable processes from general valid ones (P16).  The Confinement
Theorem says that inside a sealed-record (RP) process, *any
surviving clock must live on a time-asymmetric word*: a block
pattern that differs from its own reversal as a necklace.
Reflection positivity is the process-level time symmetry; the only
place an irreversibility witness could hide is in the chirality of
the block pattern itself.  The corpus did not order this resonance
between combinatorics and physics, but it records it.

## 6. The chiral core

### 6.1 The audit: generic validity decouples complex poles

Over 120 verified-valid processes (full word scans to length 12;
mixing strengths 0.45-0.70), the coupled subordination

$$
s \;=\; \frac{\max\{|\lambda| : \lambda \text{ nonreal, coupled}\}}
            {\max\{|\lambda| : \lambda \text{ coupled}\}}
$$

of every one of the seven chiral blocks of length $\le 8$ was
**exactly zero in every sample**: in random valid processes,
complex poles do not couple to chiral diagonals *at all*.  Generic
validity sits far from the wall — the dangerous region is thin.

### 6.2 The attack: the wall is approached, not crossed

Hill-climbing the letters to maximize $s$ on the block $00011101$
under *hard* validity (full scan to length 12 plus diagonal
positivity to depth 2000 at every step; finalists re-screened with
scans to length 14 and every chiral-class diagonal of lengths 6-8
to depth 2000):

```text
   best valid s found:   0.1866   (deep post-hoc filter: PASS)
   best invalid s seen:  1.0000   (multiple restarts reach the
                                   circle - never validly)
   witness beyond the wall: at s = 1.000,
       p(101010100000) = -4.0e-6 < 0
```

Three facts, each pulling its weight.  (1) Valid processes with
**coupled complex poles on chiral blocks exist** — constructive
existence at $s = 0.1866$, surviving the deepest filter we own.
Any correct theorem must therefore *permit* subordinate complex
coupling; (CPE) below is the strongest statement that survives.
(2) The number agrees with Paper 27's independently measured wall
($s \le 0.205$ over 1,882 samples) — two different searches, same
ceiling, evidence that the wall is a property of validity rather
than of either search.  (3) Every candidate that reaches the circle
breaks word positivity at an explicit finite word; the witness
above fails at length 12.

### 6.3 The mechanism receipt

The champion's coupled pole moduli are $(1,\, 0.187,\, 0.187,\, 0)
\cdot \rho$ with complex phase $\theta/\pi = 0.037571$.  Lifting
the complex pair to the coupled circle while keeping all residues
fixed makes the diagonal negative at $n = 32$:

$$
h_{\mathrm{lift}}(n) \;=\; a\rho^n + 2\rho^n\,
|c|\cos(n\theta + \varphi) \;<\; 0
\quad\text{first at } n = 32 .
$$

This is the Weyl/equidistribution mechanism in one receipt: for
irrational $\theta/2\pi$ the sequence $n\theta$ visits every phase,
so peripheral nonreal poles force the cosine to overwhelm any fixed
$a \ge 0$ unless the coupling vanishes — *for these residues*.
What remains unproved is that no valid process can rearrange
residues to evade the visit.

### 6.4 The asymptotic constraint frame

**Proposition 6.1.**  Suppose a block $W$ of a valid finite-rank
process has semisimple coupled peripheral set $\{\rho,\,
\rho e^{\pm i\theta}\}$ with $\theta/2\pi$ irrational, with spectral
projectors $P_0, P_\pm$.  Then for **all** words $u, v$, with
$f = B_u^\dagger\Omega$, $g = B_v\Omega$:

$$
\langle f, P_0\, g\rangle \;\ge\; 2\,\bigl|\langle f, P_+\,
g\rangle\bigr| .
$$

*Proof.*  $p(u W^n v) \ge 0$ for all $n$; divide by $\rho^n$ and
pass to the limit along subsequences $n\theta \to \alpha \pmod
{2\pi}$ (every $\alpha$ is reachable by irrationality):
$F(\alpha) = \langle f, P_0 g\rangle + 2\,\mathrm{Re}\,(e^{i\alpha}
\langle f, P_+ g\rangle) \ge 0$ for all $\alpha$ — a nonnegative
trigonometric polynomial of degree one; Fejér's condition gives the
inequality.  $\blacksquare$

With $u = v = \emptyset$ this derives the diagonal margin
$a \ge |b|$ that Paper 27 used as an empirical criterion.  Multiple
$W$-power insertions give torus versions: for words
$u\,W^{n_1}\,v\,W^{n_2}\,w$, the coupling array
$\langle f, P_s A_v P_t\, g\rangle$ must make a doubly
trigonometric polynomial nonnegative on the whole 2-torus (the pair
$(n_1\theta, n_2\theta)$ equidistributes).  These are the
constraints any counterexample must satisfy at every order — and
the structure a proof of exclusion must turn into a contradiction.
The clock itself sits **on** the Fejér boundary ($a = |b|$: its
diagonal grazes zero infinitely often), which is why nothing
cheaper than these constraints can kill it.

### 6.5 The final form of the conjecture

**Conjecture 6.2 (CPE — Chiral Peripheral Exclusion).**  In a valid
RP-form process of finite rank, the coupled poles of every block
diagonal on its maximal-modulus circle form $\{\rho\}$ or $\rho
\times$ (roots of unity); equivalently, no irrational peripheral
phase couples.  By Theorem 5.4 only chiral blocks of length $\ge 6$
are at issue.

Status: open.  Evidence: the audit ($s = 0$ generically), the
attack (the wall at $\approx 0.19$, twice independently), the
mechanism receipt, and Proposition 6.1's constraint frame.  (CPE)
implies the spectral half of (PR-RP+) via Corollary 5.3 extended to
rational peripheral phases (block-power decimation reduces roots of
unity to the positive-pole case).

## 7. The CPE campaign: reduction, escape, and the two conjectures

The first movement of this paper confined the clock obstruction and
named (CPE).  This second movement exhausts every route we could
construct to prove or falsify it.  The outcome is a structural
reduction: (CPE) is equivalent — at stated scope, by theorems proved
here — to two sharp finite-dimensional conjectures, one about
alternation chains, one about words in two PSD letters.

### 7.1 The Peripheral Reduction Theorem

The minimal dangerous configuration is a block $W$ whose operator
$B = B_W$ carries the **coupled peripheral triple**: coupled spectrum
on the top circle equal to $\{\rho,\ \rho e^{\pm i\theta}\}$ with
$\theta/2\pi$ irrational and the real pole genuinely coupled (a
coupled complex pair *strictly above* the coupled real pole already
violates diagonal positivity by equidistribution — Section 6).  At
rank 3 the triple is exact; at higher rank, "peripheral" means the
coupled top with semisimple peripheral part.

Write the spectral data with right/left eigenvectors $R_s, L_s$
($L^\dagger R = 1$), $s \in \{0,+,-\}$, and set

$$
G = L^\dagger L,\qquad H = G^{-1} = R^\dagger R,\qquad
\beta_s = L_s^\dagger\Omega,\qquad \alpha = G^{-1}\beta,\qquad
c_s = \bar\alpha_s\beta_s .
$$

**Theorem 7.1 (Peripheral Reduction).**  Every word in the two
super-letters $\{W, \tilde W\}$ evaluates exactly as a torus form of
$(G, \beta)$: for segments $W^{a_1}\tilde W^{b_1}W^{a_2}\cdots$,

$$
\rho^{-\Sigma}\, p\bigl(W^{a_1}\tilde W^{b_1}\cdots\bigr)
= \bigl(D(x_1)\bar\alpha\bigr)^{\!\mathsf T}\, G\, D(-y_1)\, H\,
D(x_2)\, G \cdots (\text{boundary } \alpha \text{ or } \beta),
$$

with $D(x) = \mathrm{diag}(1, e^{ix}, e^{-ix})$, $x_j = a_j\theta$,
$y_j = b_j\theta$.  Since the exponents equidistribute (Weyl) and
validity demands $p \ge 0$ at every exponent, **the torus forms must
be nonnegative on the whole torus** — a $\theta$-free system of
necessary conditions on $(G, \beta)$ alone.  At rank 3 the
evaluation is exact at finite exponents; at higher rank it holds in
the peripheral limit (subperipheral corrections vanish relative to
$\rho^\Sigma$), so the torus conditions hold for the peripheral
compression at **any rank**.

*Proof.*  Expand each segment in spectral projectors
$P_s = R_sL_s^\dagger$: $B^a = \rho^a\sum_s e^{ia\theta\sigma_s}P_s$
with $\sigma = (0,+1,-1)$, and $B^{\dagger b} = \rho^b\sum_t
e^{-ib\theta\sigma_t}P_t^\dagger$.  Products telescope through
$L_s^\dagger L_t = G_{st}$ and $R_t^\dagger R_u = H_{tu}$, with
boundary factors $\Omega^\dagger R_s = \bar\alpha_s$ and
$L_u^\dagger\Omega = \beta_u$; biorthogonality gives $H = G^{-1}$.
Weyl equidistribution of $(a_j\theta)$ in the torus closes the
positivity statement; for higher rank, pass to the limit along
exponent subsequences realizing any prescribed phases.
$\blacksquare$

Receipts: against an explicit rank-3 process with the exact triple,
the reduced formulas reproduce brute-force three- and four-segment
word values at $1.1\times 10^{-11}$; biorthogonality
$|GH - 1| = 1.8\times 10^{-14}$; the consistency identity
$F_3(x, 0, z) = F_1(x+z)$ at $3.7\times 10^{-14}$.  Everything
dangerous about (CPE) is now finite-dimensional: a Hermitian
$3\times 3$ Gram with a conjugation pattern, three state
coefficients, and one normalization — about six real parameters
after gauge.

### 7.2 The torus tower

The conditions organize by **alternation depth** (number of
$W/\tilde W$ segments).  Depth 1 is the diagonal: $c_0 \ge 2|c_+|$
(Fejér), so the clock strength $r = 2|c_+|/c_0 \le 1$.  Depth 2 is
the entrywise positivity of Remark 3 in Section 3 — already a
genuine constraint; probing the two-segment form at $x - y = \pi$
yields the closed-form necessary inequality (gauge
$G_{00} = G_{++} = G_{--} = 1$, $G_{0+}$ real $= \gamma$,
$G_{+-} = \delta$):

$$
\text{(N1)}\qquad \alpha_0^2 \;\ge\; 2\,|\alpha_+|^2\,(1 + |\delta|).
$$

Depth 3 collapses exactly in its middle phase: the condition is
$f_0(x)\,g_0(z) \ge 2\,|f_+(x)\,g_+(z)|$ pointwise, with
$f_t(x) = ((D(x)\bar\alpha)^{\mathsf T}G)_t$ and
$g_t(z) = (HD(z)\beta)_t$; depths 4 and 5 take the analogous grid
forms.  Maximizing $r$ subject to the tower (annealing over the
reduced parameters):

```text
   constraint set                 r_max
   depth 1 (diagonal)             0.9889
   + depth 2 (two-segment)        0.9961
   + depth 3                      0.9882
   + depth 4                      0.9335
   + depth 5                      0.9045
```

The optimizer's margins at its depth-5 winner were already thinning
monotonically (0.095 down to 0.020) — correctly suggesting, as
Section 7.5 confirms, that the apparent plateau is an artifact of
shallow depth.  But the tower's true ceiling is not a numerical
question, because of what comes next.

### 7.3 The Normal Escape Theorem

**Theorem 7.3 (normal escape).**  If $G = I$ (equivalently: $B$
normal), the **entire** alternation tower is feasible at clock
strength $r$ arbitrarily close to $1$.

*Proof.*  With $G = H = I$ every chain matrix is diagonal, so each
chain value collapses to a single total frequency:
$\text{chain} = c_0 + 2\,\mathrm{Re}(c_+e^{i\Phi})$ with $\Phi$ the
signed sum of the segment phases.  Positivity for all $\Phi$ is
exactly Fejér: $c_0 \ge 2|c_+|$ — satisfiable with equality, i.e.
$r = 1$.  $\blacksquare$

Receipt: the witness $G = I$, $\beta = (\sqrt 2(1+\varepsilon),1,1)$
evaluates at $r = 0.999998$ with every implemented depth's margin
equal to $+2\times 10^{-6}$; the exact adversary of Section 7.5
re-receipts it to depth 16 at $4\times 10^{-16}$ from the Fejér
bound.

**Corollary (tower insufficiency).**  No proof of (CPE) can come
from the $(B, B^\dagger)$ subalgebra alone.  If (CPE) is true, the
obstruction lives in words that *leave* the block algebra — other
letters, rotations of $W$ — or in the letter embedding itself.
Equivalently, the sharpest counterexample target is now precise: a
valid RP process whose chiral block is **normal with nonreal
spectrum** (at $d = 3$: proportional to a rotation), state-coupled.

### 7.4 The letter level: the NR phenomenon

The escape needs a normal chiral block with nonreal spectrum.  The
letters refuse to build one:

```text
   minimize normality defect ||[B, B^dag]|| / ||B B^dag||,
   objective REWARDING |Im lambda|/rho up to 0.5:
   W = 001011    d = 3:  defect 5.3e-16   |Im|/rho = 0.0000 (all)
   W = 00011101  d = 3:  defect 8.8e-16   |Im|/rho = 0.0000 (all)
   W = 001011    d = 4:  defect 1.7e-07   |Im|/rho = 0.0000 (all)
```

Normality is *easily* reachable — and the spectrum is real in every
trial, although the optimizer would have profited from oscillation.

**Conjecture (NR).**  A word in two positive semidefinite letters,
if normal, has real (nonnegative) spectrum.

Three remarks a hostile reviewer needs.  (1) This is a strictly
*two-letter* phenomenon: by Ballantine's theorem every real matrix
of positive determinant — rotations included — is a product of
**five** positive definite matrices; with two letters (powers of two
PD families) the normal+nonreal manifold appears unreachable.  (2)
The quantitative version: minimizing the defect under a *hard*
nonreal floor gives an $O(1)$ trade-off wall —

```text
   W = 00011101, d = 4:   im_min   0.05    0.15    0.30
                          defect   0.266   1.399   0.976
```

— even five percent demanded oscillation costs $0.27$ of normality;
the non-monotonicity between the higher floors is search difficulty,
reported as-is.  (3) An unplanned refinement: the first chiral class
$001011$ appears **always-real at $d = 3$** (best $|\mathrm{Im}|/\rho
= 0.0000$ over $8\times 3000$-step climbs, while $d = 4$ reaches
complex): chirality is necessary for complex spectra (Theorem 4.5),
and letter dimension appears to carry its own threshold — a new
empirical layer of the reality map.

**The detector route to (NR), attempted and closed by theorem.**
There is a seductive reduction of (NR) to the Achiral Necklace
Theorem: if $M = B_W$ is normal, $M$ and $M^\dagger$ commute, so any
block word $X \in \{W, \tilde W\}^*$ evaluates as $M^pM^{\dagger q}$
with eigenvalues $\rho^{p+q}e^{im\theta}$, $m = p - q$; an *achiral*
$X$ with $m \ne 0$ would force (via ANT) $m\theta \in \pi\mathbb Z$,
and two coprime detectors would force $\theta \in \pi\mathbb Z$ —
real spectrum, (NR) proved per class.  The scan: **zero achiral
unbalanced block words exist** — $0/106$ chiral classes (lengths
6–10, up to 8 blocks).  And the zero is a theorem:

**Proposition (detector obstruction).**  For boundary-clean $W$,
the cyclic occurrence count $I(X) = \mathrm{occ}_W(X) -
\mathrm{occ}_{\tilde W}(X)$ is rotation-invariant and reversal
flips its sign; achirality forces $I = 0$, while an unbalanced
block word has $I = m \ne 0$.  Chirality of $W$ propagates to every
unbalanced word in its block algebra.  (Receipt: $I(W\tilde WW) =
+1$, $I(\mathrm{rev}) = -1$, constant over all letter rotations.)

So (NR) cannot be reduced to (ANT) through the block algebra — a
genuine negative result that delimits the proof space.  The floor,
however, is a **theorem**:

**Theorem (the $d = 2$ floor).**  Every positive word in two
$2\times 2$ positive definite letters has real spectrum.

*Proof.*  Normalize determinants to one (scalars do not affect
spectral reality).  A symmetric PD matrix of determinant one is a
hyperbolic Möbius transformation whose boundary fixed points are
its eigendirections — two *orthogonal* directions, so its axis
passes through the basepoint $i$ of the upper half-plane (the
geodesic with endpoints $p, q$ passes through $i$ iff $pq = -1$).
Two distinct axes through a common interior point cross, so the
four boundary fixed points interleave:
$\xi_A^+, \xi_B^+, \xi_A^-, \xi_B^-$ in cyclic order.  Let $J$ be
the closed boundary arc from $\xi_A^+$ to $\xi_B^+$ not containing
the repellers.  North–south dynamics keeps $J$ invariant under
*both* letters ($A$ moves $J$ toward $\xi_A^+$ inside $J$; $B$
toward $\xi_B^+$), hence under every positive word; a continuous
self-map of a closed arc has a fixed point, which is a real
eigendirection of the word — and a real $2\times 2$ matrix with one
real eigenvalue has two.  $\blacksquare$

Receipts: interleaving in $500/500$ random PD pairs; $J$-invariance
violations $0$ over $300$ pairs $\times$ 25 boundary points; $400$
random words all real-spectrum ($\max|\mathrm{Im}|/\rho = 0.0$
exactly) with the fixed eigendirection found **inside $J$** in every
case.  The complex-spectrum phenomenon — and with it (NR) — begins
at $d \ge 3$.

The full-process attack (hard word positivity, steering the block
of $00011101$ at $d = 4$ toward the coupled triple) walls at modulus
spread $0.799$ ($s \approx 0.20$) with $|\mathrm{Im}|/\rho = 0.026$
— the **third** independent measurement of the same wall (P27:
$0.205$; p30b: $0.187$).  One incident is documented deliberately:
an earlier form of this attack, scanning words only to length 14,
produced a *fake near-counterexample* — a complex pair strictly on
top whose first negative probability occurs in $p(W^n)$ at word
length $\approx 150$, far beyond any letter scan.  This is exactly
Paper 27's impostor mechanism, caught live by this campaign's own
framework; the deep block-diagonal check (pole-based, depth 2000) is
now structural in every attack.

### 7.5 The deep adversary, the death of the plateau, and isolation

At the reduced level each chain value is a degree-one trigonometric
polynomial in **each** phase separately, so three evaluations per
coordinate give the exact per-phase minimum: cyclic coordinate
descent is an exact local adversary reaching depths no grid can.
Calibration: against the normal witness the adversary recovers the
single-frequency Fejér bound at every depth (max deviation
$4\times 10^{-16}$ through depth 16).

The verdict on the tower's plateau:

```text
   the p30c depth-5 winner (r = 0.9045) under the adversary:
   depth    1      2      3      4      5      8      12     16
   margin +0.096 +0.087 +0.062 +0.045 +0.018 -0.055 -0.195 -0.338
```

**The depth-5 survivor dies at depth 8.**  Shallow towers cannot see
this; deep alternation keeps squeezing every non-normal datum we
optimized.  Meanwhile a *band* persists at fixed depth: at
off-diagonal distance $\varepsilon = 0.05$ from $G = I$, clock
strength $r = 0.8433$ survives all constraints through depth 12.
The decisive structural question is therefore the behavior of the
band as depth grows:

**Conjecture (ISO — isolation of the normal point).**  For every
reduced datum with $G \ne I$ (in the diagonal-normalized gauge) and
$c_+ \ne 0$, some finite alternating chain is negative.
Equivalently: all-depth torus feasibility with nonzero clock
coupling is isolated at the normal point.

The measurements (death depths of depth-12 band winners; the
deepening trend of $r_{\max}$ at $\varepsilon = 0.05$), reported
exactly as measured:

```text
   band winners and their death depths:
   eps    dist     r(<=12)   death depth k*
   0.05   0.054    0.9802        16
   0.15   0.147    0.9711       >64
   0.30   -        none feasible at depth 12

   the deepening trend at eps = 0.05 (shell re-optimized at each K):
   K = 12: 0.9723     K = 32: 0.9767     K = 56: 0.8431
```

The evidence is **mixed, and the paper says so**.  Some winners die
at finite depth (and an earlier search instance measured deaths at
$k^* = 16$ and $48$); but at least one winner survives the deepest
adversary probe this campaign owns (64 phases, exact per-coordinate
minimization, 8 restarts), and the shell at $\varepsilon = 0.05$
retains strong feasible coupling through constraint depth 56, with
$r_{\max}$ declining only mildly.  Two readings remain open: the
*local* adversary misses the killing phase pattern at this budget
(the chain value's landscape has exponentially many local minima at
depth 64), or the all-depth feasible set is genuinely a **band**
off the normal point.  If the band is real, (ISO) is false as
stated and the spectral half of (CPE) rests entirely on the
letter-level exclusion — (NR) and the trade-off wall — which is
independently receipted.  The named next tool that would decide:
global phase optimization (sum-of-squares relaxation of the chain
positivity over the torus), replacing the local adversary with
certificates.

### 7.6 The reduction of (CPE)

**Theorem 7.6 (conditional reduction).**  Assume (NR) and (ISO).
Then (CPE) holds at the stated scope: no valid RP-form process of
finite rank carries a coupled peripheral triple with irrational
phase and semisimple peripheral part on any chiral block.

*Proof.*  Suppose such a process exists, with block $W$.  By Theorem
7.1 its reduced peripheral data $(G, \beta)$ satisfies every torus
condition — i.e., is all-depth feasible with $c_+ \ne 0$.  By (ISO),
$G = I$, so $B_W$ is normal.  $W$ is a word in two PSD letters, so
by (NR) its spectrum is real — contradicting the nonreal pair.
$\blacksquare$

Scope, stated for the reviewer: a single irrational peripheral
orbit plus the real Perron pole (the minimal dangerous
configuration); rationally related harmonics and multiple
independent orbits require the same machinery with more frequencies
(higher-degree Fejér forms and product tori) and are left as stated
extensions; peripheral Jordan tails remain the known gap.  What the
theorem buys: (CPE) — an assertion about *all* valid processes at
*all* ranks — is now equivalent, at this scope, to two
finite-dimensional statements, each independently attackable, each
already carrying machine evidence, and each falsifiable: a
counterexample to (NR) is a normal two-letter word with nonreal
spectrum (a finite algebraic object one could simply exhibit); a
counterexample to (ISO) is an all-depth feasible reduced datum off
the normal point (and Section 7.5's scaling measurements say where
to look).  The campaign also says exactly what a (CPE)
counterexample must now survive: it must thread BOTH needles at
once.

### 7.7 The pinch: the two walls in one coordinate system

The campaign's synthesis rests on one identification: **$G = I$ in
the reduced coordinates is exactly normality of the block**
(orthonormal eigenvectors).  So the letter campaign and the tower
campaign measure distances in the *same space*, and a (CPE)
counterexample needs both at once: a chiral block whose top
spectrum is the coupled triple, with reduced data inside the
all-depth-feasible band.  Measured:

```text
   the letter side (validity OFF - pure word geometry, d = 4):
   the exact triple IS kinematically reachable (modulus spread
   down to 0.0015 on block 00011101) - BUT the near-triple cloud
   lives at Gram distance 0.502 - 0.937 from the normal point.

   the tower side (p30e/p30f): the all-depth-candidate band lives
   at distance 0.054 - 0.147 (the 64-phase survivor at 0.147).

   THE PINCH: minimum letter distance 0.502 vs band edge 0.147 -
   DISJOINT by a factor >= 3.4 in the shared coordinate.
```

And the wall does not soften near the normal point: demanding even
one percent oscillation costs a normality defect $\ge 0.17$, with
$O(0.2$–$0.5)$ floors at every measured level (search-bounded,
non-monotone, reported as-is).  The counterexample corridor, if it
exists, is invisible at every budget this corpus has reached: to
thread it, a process must simultaneously drag the letter cloud
toward normality (the NR wall says that costs $O(1)$) *and* widen
the tower band (the deep adversary squeezes it).  **Two independent
walls, no overlap** — quantified evidence for (CPE) of a kind
neither campaign could produce alone, and the precise target for
both the SOS upgrade (certify the band's true extent) and any
counterexample hunt (search the gap, now exactly delimited).

## 8. The assembly half

Granting (CPE), every block diagonal of a valid RP process is
positively realizable *separately*.  (PR-RP+) needs more: one
nonnegative-matrix pair on one cone realizing the **whole** process
jointly.  This is the classical hard problem of characterizing
functions of finite Markov chains (Dharmadhikari; Heller's
cone-theoretic characterization), the stochastic sibling of
finitely-correlated states (Fannes-Nachtergaele-Werner).
Per-diagonal realizability does not obviously assemble: the cones
constructed by dominant-pole methods differ block by block, and the
known joint criteria (polyhedral invariant cones) are not implied
by spectral data alone.  The corpus' RP-side handles — the typed
moment theorems (P8), the separation theorem (P16), and now the
confinement structure — suggest the assembly should be attempted on
the *achiral sublattice first* (where exact Stieltjes structure
gives canonical cones) and extended by chirality-pairing
($W$ with $\tilde W$, $B_{\tilde W} = B_W^\dagger$).  That is a
plan, not a result; the assembly half is untouched by this
campaign and remains open.

## 9. What a hostile reviewer should attack

```text
1. NOVELTY of Section 4's ingredients: Lemmas 4.3/4.4 are classical
   and the two-palindrome lemma is known in combinatorics on words.
   Defense: stated, cited, no priority claimed; the contribution is
   the necklace-invariant assembly, the census-backed corollaries,
   and the confinement consequence the corpus needed.
2. SEMISIMPLICITY in Proposition 6.1: peripheral Jordan structure is
   assumed away.  Defense: for products of PSDs, Lemma 4.4 gives
   semisimplicity off zero on achiral classes, but on CHIRAL blocks
   peripheral Jordan cells are not excluded; the proposition's scope
   is stated.  A complete (CPE) proof must handle polynomial-times-
   oscillation tails.
3. THE CHIRAL CORE IS NUMERICAL: the wall (0.1866 / 0.205) is a
   search artifact ceiling, not a theorem; coverage is dim <= 5,
   two letters, scans <= 14, blocks <= 8.  A counterexample could
   hide beyond all of these.  Defense: agreed - that is why (CPE)
   is labeled OPEN and the constraint frame is published for both
   provers and counterexample-hunters.
4. GENERATOR BIAS: the audit's s = 0 could reflect the Perron-state
   construction rather than validity per se; the same construction
   showed validity to be generic (an unexplained finding, flagged).
   Defense: the attack section exists precisely to escape generic
   bias, and it found the coupled-complex regime - thin, not empty.
5. TOLERANCES: all PSD/positivity thresholds are 1e-13-class against
   quantities of order one; the integer-arithmetic receipts (error
   exactly 0) anchor the factorization claims beyond floating point.
6. REAL VS COMPLEX FORMS: receipts are real-symmetric; the theorems
   are stated for self-adjoint letters and hold verbatim on complex
   Hilbert spaces (reversal = adjoint throughout).
7. WHAT A COUNTEREXAMPLE MUST LOOK LIKE (updated by the campaign):
   a chiral block of length >= 6 whose operator is normal-with-
   nonreal-spectrum (refuting NR) OR whose reduced data is all-depth
   torus-feasible off the normal point (refuting ISO) - AND which
   survives full word scans plus the deep diagonal check (the
   impostor lesson).  Found, it would refute (CPE), kill (PR-RP+),
   and prove sealed records strictly weaker than record positivity:
   a publishable outcome the corpus would print.
8. THE CAMPAIGN'S OWN SOFT SPOTS: (NR) rests on optimization
   receipts at d <= 4 and short words - a normal nonreal word could
   exist at higher d or longer words; (ISO) rests on adversary
   searches (exact per-coordinate but local) and finite depths; the
   conditional theorem's scope excludes harmonic/multi-orbit
   peripheral sets and Jordan tails; the dimension-threshold
   observation (001011 real at d = 3) is search-bounded.  Each is a
   finite, well-posed target for refutation - that is the point of
   the reduction.
```

## 10. What this paper proves and does not prove

Proves: the exhaustion of reflection (3.1); the reflection-axis
lemma (4.2, with exhaustive two-way verification to $L = 12$); the
palindrome factorization (4.3, exact in integer arithmetic); the
Achiral Necklace Theorem (4.5) and its length-$\le 5$ corollary
(4.6, subsuming PR2); exact Stieltjes structure at palindromic
phase (5.1); signed-Stieltjes at every phase (5.2); positive
realizability of achiral diagonals modulo the named dominant-pole
import (5.3); the Confinement Theorem (5.4); the Fejér constraint
frame at its stated scope (6.1); the Peripheral Reduction Theorem
(7.1, validated at $10^{-11}$); the Normal Escape Theorem (7.3,
hence tower insufficiency); the detector-obstruction proposition
(7.4, closing the ANT route to (NR)); the $d = 2$ floor theorem
(7.4: positive words in two PD $2\times 2$ letters have real
spectrum — the invariant-arc proof); the conditional reduction
(NR) $\wedge$ (ISO) $\Rightarrow$ (CPE) at stated scope (7.6).

Does not prove: (CPE) itself — now equivalent (at scope) to the two
named conjectures; (NR) — receipted at $d \le 4$, open; (ISO) —
receipted by witness deaths and scaling, open; the assembly half
(Section 8, untouched); the sufficiency of chirality for complex
spectra (empirical, with the new $d = 3$ threshold observation also
empirical); an explanation for the genericity of validity under the
Perron-state construction (flagged open); and Theorem-B-type
exclusion for peripheral Jordan tails (scope gap).

## 11. The kernel after Paper 30

```text
SUPERSEDED: P27's Theorem PR2 (subsumed by ANT, 4.5/4.6); P27's
  empirical reality map (corrected: complex spectra start at L = 6,
  exactly where chirality starts).
REDUCED, TWICE: the spectral half of (PR-RP+) became (CPE) on
  chiral blocks >= 6 (first movement); the CPE campaign then reduced
  (CPE) itself - at the stated scope, by Theorems 7.1/7.3/7.6 - to
  (NR) [normal two-letter words are real] and (ISO) [all-depth torus
  feasibility is isolated at the normal point]: two finite-
  dimensional conjectures, both machine-receipted, either's
  refutation a (CPE) counterexample candidate.  (PR-RP++) is retired
  in favor of (CPE); (CPE) now lives as (NR) + (ISO).
UNCHANGED: the assembly half (one cone, whole process) - open, with
  the achiral-sublattice-first plan stated.
KERNEL: { (C-reg-b'), (NR), (ISO), assembly-(PR-RP+), (V),
  calibration } + { O7/O8/O11 remainders, D10-refinements,
  mu-dyn, loop-H, (R-id), validity-genericity (minor),
  d-threshold-of-chirality (minor) }.  ((Z6-int) is discharged at
  stated scope by Paper 31.)
THE PINCH (7.7): the letter-reachable triple cloud (Gram distance
  >= 0.50 from normal) and the tower band (<= 0.15) are DISJOINT
  in the shared coordinate - the counterexample corridor is
  invisible at every budget reached; (NR) and (ISO) each guard one
  wall, the d = 2 floor is now a theorem, and the ANT-detector
  route is closed by the obstruction proposition.  Named next: SOS
  certification of the band, and the corridor search in the
  measured gap.
PROGRAM NOTE: the arrow-of-time witness inside a sealed ledger, if
  it exists at all, must now live on a time-asymmetric word whose
  operator is normal-with-nonreal-spectrum or whose peripheral data
  evades the deep alternation squeeze - and the campaign's receipts
  say the letters refuse the first and the chains punish the second.
  The obstruction to sealability has been pushed from "somewhere in
  process space" into two named algebraic needles.  That is the
  campaign's one-sentence result.
```

## References and literature map

- Papers 8, 16, 24, 27 (internal): the typed moment theorems; the
  record clock and Theorem B; the graded detector; the RP-form,
  Theorem PR2, the validity wall, and (PR-RP++).
- C. Hillar and C. R. Johnson, "Eigenvalues of words in two positive
  definite letters," SIAM J. Matrix Anal. Appl. 23 (2002) 916-928:
  the words-in-PD-letters frame; reality results for short and
  symmetric (palindromic) words.
- B. D. O. Anderson, M. Deistler, L. Farina, L. Benvenuti,
  "Nonnegative realization of a linear system with nonnegative
  impulse response," IEEE Trans. Circuits Syst. I 43 (1996):
  the dominant-pole positive-realization criterion (Corollary 5.3's
  import).
- L. Benvenuti and L. Farina, "A tutorial on the positive
  realization problem," IEEE Trans. Autom. Control 49 (2004):
  survey of the realization theory used here.
- S. W. Dharmadhikari, "Functions of finite Markov chains," Ann.
  Math. Statist. 34 (1963); A. Heller, "On stochastic processes
  derived from Markov chains," Ann. Math. Statist. 36 (1965): the
  assembly half's classical anchors.
- M. Fannes, B. Nachtergaele, R. F. Werner, "Finitely correlated
  states on quantum spin chains," Commun. Math. Phys. 144 (1992):
  the quantum sibling of the assembly problem.
- A. Klein and L. Landau, "Construction of a unique self-adjoint
  generator for a symmetric local semigroup," J. Funct. Anal. 44
  (1981): OS reconstruction behind the RP-form.
- Combinatorics on words: the characterization of words conjugate to
  their reversal as products of two palindromes is folklore/known;
  see e.g. de Luca-De Luca, "Pseudopalindrome closure operators in
  free monoids," Theoret. Comput. Sci. 362 (2006) and references.
- C. S. Ballantine, "Products of positive definite matrices IV,"
  Linear Algebra Appl. 3 (1970) 79-114: every real matrix with
  positive determinant is a product of five positive definite
  matrices - the contrast that makes (NR) a two-letter phenomenon
  and kills purely spectral routes to (CPE).
- H. Weyl, "Uber die Gleichverteilung von Zahlen mod. Eins," Math.
  Ann. 77 (1916): the equidistribution behind the theta-free torus
  reduction (Theorem 7.1).
```

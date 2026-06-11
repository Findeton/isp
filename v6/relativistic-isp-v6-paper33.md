# Paper 33 (v6) - SHARD: The Tame Frontier - Rank Uniformity, Finite Sections, and What Survives the Limit

Preprint, not peer reviewed, version 2026-06-11.

Author: Felix Robles Elvira

Subtitle:

```text
Every theorem in this corpus carries the same caveat: 'at stated
scope' - proved and receipted at finite rank, with portability to
the full (infinite-rank) record category left as the shared
boundary.  This paper stops gesturing at that boundary and
STRUCTURES it.  Three results.  THE RANK-FREE CATALOG: a large
class of corpus theorems have proofs that never use the rank - the
Achiral Necklace chain, the Stieltjes structure, the collapse
lemma's centrality argument, the normal escape, the exhaustion of
reflection - and these port verbatim to any rank; receipts at
d = 8, 16, 32 confirm what the proofs already say.  THE SOT ENGINE
THEOREM (proved, all ranks including infinite): a self-adjoint
transfer 0 <= T <= 1 with a stationary state converges T^n -> P_1
STRONGLY by the spectral theorem alone - no spectral gap, no
aperiodicity, no rank bound; (E-bg)'s clustering engine, and with
it the background-reaching arguments of the (E) chain, is
rank-blind (receipts: a 0.9990-mode ledger clusters slowly but
completely; a 400-dimensional mock with eigenvalues packed against
1 at 1e-5 spacing converges through the packed spectrum).  FINITE
SECTIONS: large ledgers are reached from finite rank through the
word subspaces - word values converge geometrically in the section
(9.9e-6 at dimension 2 down to 4e-17 at dimension 32, on a
240-dimensional ledger), sections can remain exactly valid, and
ATOMIC SECTORS survive: a two-sector ledger's double Perron
eigenvalue is recovered by deepening sections (0.933 -> 0.985 ->
0.998 with the third eigenvalue staying away).  And the campaign
locates where the frontier genuinely begins: a ledger with FIFTY
near-degenerate Perron directions has no tolerance-stable sector
count (50 / 33 / 17 / 1 as the threshold tightens) - the atomic
formalism ends where the Perron spectrum stops being discrete.
That open is NAMED: (T-cont), the direct-integral sector theory of
record ledgers with continuous Perron spectrum - symmetry-breaking
families, (V)-adjacent.  Below (T-cont), the frontier is now
structured ground with citable theorems; above it, one named
problem
```

## 0. Verdict

```text
PROVED:
  T4.1  THE SOT ENGINE: T self-adjoint, 0 <= T <= 1, T Omega =
        Omega  =>  T^n -> P_1 strongly, at ANY rank including
        infinite - spectral theorem, no gap, no aperiodicity
        (receipts: 0.9990-mode decay completes by n ~ 1e4;
        dense-packed spectrum converges by n ~ 1e7).
        COROLLARY: (E-bg) and the (E) chain's clustering arguments
        are rank-blind; their 'stated scope' caveat reduces to the
        sector-formalization question, not the rank.
  P3.1  THE RANK-FREE CATALOG (a portability principle with
        receipts): proofs functorial in rank port verbatim - the
        ANT chain receipted exact at d = 8, 16, 32 (palindrome
        factorization 7.1e-17 ... 3.8e-16; achiral reality 0.0;
        chiral capability persists).
ESTABLISHED (receipts):
  T5.x  FINITE SECTIONS: word-subspace compressions of a d = 240
        ledger converge geometrically (sup error over |w| <= 8:
        9.9e-6 / 4.3e-7 / 3.6e-8 / 3.5e-10 / 4.1e-17 at section
        dims 2 / 4 / 8 / 16 / 32); sections can stay exactly valid
        (min p = +9.6e-4 at every section); atomic two-sector
        structure recovered asymptotically (second Perron
        eigenvalue 0.933 -> 0.985 -> 0.998; third stays at 0.86).
  T6.1  THE CONTINUOUS BOUNDARY: 50 near-degenerate Perron
        directions admit NO tolerance-stable sector count
        (50/49/33/17/1 across tau = 1e-1 ... 1e-10): the atomic
        sector formalism provably cannot describe this regime.
NAMED: (T-cont) - direct-integral sectors for continuous Perron
  spectrum: THE genuine tame-frontier item.  Everything below it
  is now citable structure.
```

## 1. Method and reproducibility

```text
code/v6_p33a_rank_uniformity.py   the rank-free receipts; the SOT
                                  engine (near-gapless + packed
                                  spectrum); the frontier map
code/v6_p33b_finite_sections.py   section convergence; validity of
                                  sections; sector recovery; the
                                  continuous boundary
```

Fixed seeds; canonical outputs /tmp/p33a.out, /tmp/p33b.out; reruns
bit-identical.

## 2. The frontier, stated honestly

### 2.1 Where the caveat comes from

"At stated scope" appears in every corpus theorem since Paper 4,
and it does not always mean the same thing.  Its genealogy:

- **The tame class** (P11): the L3 reconstruction — Gaussian
  towers, the Weyl/CCR algebra, the Schrödinger representation by
  Stone–von Neumann — was proved for processes whose record towers
  satisfy the tame growth and self-adjointness conditions; P12's
  O10 classification (limit-point/limit-circle = boundary records)
  marked exactly where "beyond tame" begins for *reconstruction*.
- **Finite rank** (P16 onward): the sealability circle — Heller
  cones, the clock, (PR-RP+), the whole of Papers 27 and 30 — is
  natively finite-rank: finite Hankel rank is the *subject*, not a
  simplification.  There the caveat is not a gap at all, and part
  of this paper's work is to say so cleanly.
- **Finite-dimensional receipts for infinite-dimensional claims**
  (P31): the (E) chain's collapse lemma and clustering were proved
  with arguments that *should* hold at any rank but were receipted
  on toy ledgers; the caveat there was a genuine IOU.
- **The dynamics layer** (P22, P26): Monte-Carlo and engineering
  receipts at fixed volume — measurements, never portability
  claims.

Four different epistemic situations wearing one phrase.  The audit
question this paper answers: *which results port by their proofs,
which port by a theorem, which are honest finite-rank measurements,
and where does the gap have actual content?*

### 2.2 The taxonomy

We will sort every load-bearing result into four bins:

1. **Rank-free**: the proof never invokes the rank — it
   manipulates letters (self-adjointness, positivity, words),
   combinatorics, or the spectral theorem.  Such theorems hold
   verbatim on any Hilbert space; "stated scope" was never a
   restriction for them, and saying so requires only reading the
   proof (Section 3 does, entry by entry).
2. **SOT-uniform**: the proof needs a convergence statement
   ($T^n \to P_1$) that classically requires spectral gaps or
   aperiodicity — obstructions that genuinely can occur for
   positive maps.  Section 4 proves they *cannot* occur for
   reflection-positive ledgers, at any rank: one theorem ports the
   whole class.
3. **Rank-receipted**: finite-rank *measurements* (walls,
   searches, bands, exclusion bounds).  No porting claim is made
   or needed; the bin exists so that nobody mistakes a wall for a
   theorem.
4. **(T-cont)-bound**: results whose statements presuppose
   *atomic* sector structure (isolated Perron directions).
   Section 6 shows this presupposition has a sharp failure
   boundary, names the open problem, and assigns the corpus items
   that live behind it.

## 3. The rank-free catalog

**Principle 3.1.**  A theorem whose proof never invokes the rank —
only the algebraic structure of the letters (self-adjointness,
positivity, words) and the spectral theorem — holds verbatim at
every rank, including on infinite-dimensional Hilbert spaces, with
the standard replacements: matrices $\to$ bounded self-adjoint
operators, PSD $\to$ positive operators, eigendecompositions $\to$
spectral measures, limits $\to$ strong operator limits.

This is not a meta-theorem; it is a *methodology* — each entry
below is certified by walking its proof.  The catalog, entry by
entry, with the walk:

**Reflection exhaustion (P30, 3.1).**  The proof is one line:
$p(\bar u \circ v) = \langle B_u\Omega, B_v\Omega\rangle$ because
$B_{\bar u} = B_u^\dagger$ — a Gram identity.  Nothing in it counts
dimensions; on an infinite-dimensional space the $B_w\Omega$ are
vectors and the Gram is PSD exactly as before.  *Rank-free.*

**The reflection-axis lemma (P30, 4.2).**  Pure combinatorics on
words — cyclic sequences and dihedral reflections.  There is no
Hilbert space in the statement at all.  *Rank-free.*

**Palindrome factorization (P30, 4.3).**  $B_u = CC^\dagger$ or
$CA_{\mathrm{mid}}C^\dagger$ by reading the palindrome — products
and adjoints of bounded operators.  *Rank-free.*

**The Achiral Necklace Theorem (P30, 4.5).**  Assembles the two
previous entries with the classical fact that $PQ$ ($P, Q \ge 0$)
has spectrum in $[0,\infty)$.  The classical fact holds for bounded
positive operators ($PQ$ is similar to
$Q^{1/2}PQ^{1/2} \ge 0$ on the closure of the range, with the
boundary handled by approximation exactly as in the
finite-dimensional proof).  *Rank-free* — and with it the entire
confinement consequence: clock obstructions live on chiral blocks
at any rank.

**The Stieltjes structure (P30, 5.1–5.2).**  Palindromic phase:
$h(n) = \langle\Omega, B^n\Omega\rangle$ with $B \ge 0$ —
the spectral theorem gives $h(n) = \int x^n d\mu$ with $\mu$ the
(now possibly non-atomic) positive spectral measure: *still an
exact Stieltjes moment sequence*; only the "finitely many atoms"
clause is dropped.  Rotated phases: the semisimplicity-off-zero
argument becomes the statement that $B_uB_v$ is similar to a
positive operator off its kernel — same conclusion, signed real
measure on $[0,\infty)$.  *Rank-free, with the atomic clause
correctly weakened.*

**The normal escape (P30, 7.3).**  $G = I$ collapses every chain
to a single-frequency Fejér form — an identity in the letters'
algebra.  *Rank-free.*

**The peripheral reduction (P30, 7.1).**  Already stated per rank
with the higher-rank case handled by limits along exponent
subsequences; the limit argument needs only boundedness of the
subperipheral part relative to $\rho^\Sigma$.  *Rank-free in its
own stated form.*

**The collapse lemma (P31, 5.3).**  Centrality (an algebraic
commutation statement) plus axiom-R membership plus GNS — the GNS
construction is the infinite-dimensional tool *par excellence*.
*Rank-free.*

**DR-invisibility (P31, 4.2).**  Character lattices of compact
groups; dimension of the ledger never enters.  *Rank-free.*

Receipts — tripwires, not proofs (the proofs are the proofs): at
$d = 8, 16, 32$ the palindrome factorization is exact
($7.1\times 10^{-17}$ to $3.8\times 10^{-16}$ relative), achiral
spectra are real at machine zero, and chiral classes remain
complex-capable.  If a hidden rank dependence existed anywhere in
the chain, growing $d$ is where it would trip.

**What is *not* in the catalog, deliberately**: the validity walls
($s \approx 0.2$), the (NR) optimization receipts ($d \le 5$), the
band/isolation measurements, the pinch coordinates, the
tower-exclusion bounds.  These are finite-rank *measurements*; the
corpus never claimed more, and bin 3 of the taxonomy exists so the
distinction is structural rather than scattered through honesty
clauses.  One subtlety worth recording: for the sealability circle
(P16/P27/P30) finite rank is the *subject* — "(PR-RP+) at infinite
rank" is vacuous, since an infinite-rank process trivially has no
finite realization.  The caveat there was never a debt; it is now
filed as such.

## 4. The SOT engine theorem

### 4.1 The theorem and its proof

**Theorem 4.1.**  Let $T$ be self-adjoint with $0 \le T \le 1$ on a
Hilbert space of any dimension, and $T\Omega = \Omega$.  Then
$T^n \to P_1$ strongly, where $P_1 = E(\{1\})$ projects onto the
fixed space — with **no spectral gap and no aperiodicity
assumption**.

*Proof.*  By the spectral theorem $T = \int_{[0,1]} t\, dE(t)$, so
for any vector $v$,

$$
\|T^n v - E(\{1\})v\|^2
\;=\; \int_{[0,1)} t^{2n}\, d\langle v, E(t) v\rangle .
$$

The integrand $t^{2n} \to 0$ pointwise on $[0,1)$ and is dominated
by $1$, which is integrable against the finite measure
$d\langle v, Ev\rangle$; dominated convergence gives the limit
$0$.  $\blacksquare$

### 4.2 Why this is not a triviality

For *general* positive maps (transfer matrices of arbitrary
processes) the conclusion is **false** without extra hypotheses,
and the obstructions are classical Perron–Frobenius pathologies:

- **Periodicity**: a cyclic transfer ($T$ permuting sectors) has
  $T^n$ oscillating forever — the textbook reason finite-Markov
  clustering demands *aperiodicity*.
- **Peripheral rotation**: a complex dominant pair makes two-point
  functions oscillate and even pass through zero.  Paper 31's
  campaign exhibited exactly this: a non-RP counterpoint whose
  separated two-point value changes sign **eleven times** —
  "background eclipses," separations at which a seal momentarily
  cannot be placed.

The theorem says these obstructions are **structurally impossible
for reflection-positive ledgers**: RP *is* self-adjointness of the
transfer (the RP-form), self-adjointness makes the spectrum real,
and a real subunital spectrum admits neither cycles nor eclipses.
The ledger's time symmetry is not a convenience here — it is the
load-bearing hypothesis.  This is the same structural fact that
appeared twice before in the corpus (the typed moment theorems of
P8; the eclipse receipt of P31) now stated once, at full
generality, with its three-line proof.

What the theorem does **not** give: rates.  Strong convergence
without a gap can be arbitrarily slow (the receipts below make
this vivid), so any future argument needing *quantitative*
clustering — none in the (E) chain does — would re-encounter the
gap question.  Stated here so no reader over-reads the corollary.

### 4.3 The corollary that discharges the (E) chain's rank caveat

**Corollary 4.2.**  (E-bg)'s clustering — and with it every
background-reaching argument in Paper 31's (E) chain — holds at any
rank, including infinite.

*Proof.*  Walk P31's Theorem 5.6 substituting Theorem 4.1 for the
finite-rank convergence step: within a sector, $T^n \to
|\Omega\rangle\langle\Omega|$ strongly (simplicity of the fixed
space *is* the sector hypothesis); hence
$p(u\,\mathrm{gap}^n\,w) = \langle A_u^\dagger... \to
p(u)p(w) > 0$ for every background with $p(u) > 0$ and the sealed
word with $p(w) > 0$; the GNS collapse then applies as before.  No
step used the rank.  $\blacksquare$

The "stated scope" caveat on the (E) chain therefore reduces to the
*sector-formalization* question — when is the fixed space atomic so
that "sector" means what the collapse lemma needs — which is
Section 6's subject, shared with $(V)$, and not a rank issue at
all.

### 4.4 Receipts

Two demonstrations chosen to stress exactly the hypotheses the
theorem does *not* make:

- **No gap to speak of**: a ledger with a $0.9990$ mode, probe
  loading it at $0.5$: the two-point value decays $1.2475 \to
  1.0919 \to 1.0000$ over $n = 10 \to 10^3 \to 10^4$ — the slow
  mode persists for thousands of steps and then dies, exactly as
  $0.999^n$ says; nothing else is needed.
- **Spectrum packed against 1**: $d = 400$ with eigenvalues
  approaching $1$ at spacings down to $10^{-5}$ — a finite
  imitation of continuous spectrum: $\langle u, T^n w\rangle =
  1.2433 \to 0.8458 \to 0.7450$ (the exact limit
  $\langle u,\Omega\rangle\langle\Omega,w\rangle$) by $n = 10^7$.
  The engine marches through packed spectrum at the pace the
  spectral measure dictates — and completes.

## 5. Finite sections: how the limit is reached

### 5.1 The construction

The constructive face of the frontier: large ledgers are
approximated by **word-subspace sections**.  For a ledger
$(A_0, A_1, \Omega)$ define the word filtration

$$
V_m \;=\; \mathrm{span}\{A_w\Omega : |w| \le m\},
$$

orthonormalize ($Q_m$, rank-truncated), and compress:
$\tilde A_x = Q_m^\dagger A_x Q_m$, $\tilde\Omega =
Q_m^\dagger\Omega$.  This is precisely the **finite-section
method** of operator theory (Böttcher–Silbermann), applied to the
GNS representation of the word functional — the canonical way an
infinite-rank ledger is reached from finite data, because $V_m$ is
exactly what $m$ steps of record formation can populate.  Two
properties make it the *right* compression for this corpus:
the compressed letters remain self-adjoint and PSD (compressions
of positive operators are positive — the RP-form survives
sectioning *by construction*), and the compressed word values
$p_m(w) = \langle\tilde\Omega, \tilde A_w\tilde\Omega\rangle$ are
exact for $|w| \le$ the filtration's reach.

### 5.2 Convergence

Measured on a $d = 240$ ledger with verified PSD letters (minimum
letter eigenvalue $+0.0706$ — the splitting $T/2 \pm S$ requires
$\|S\|$ controlled *relative to $\sqrt d$*, a scaling trap the
campaign hit and documents):

```text
   section m   dim    sup |p_m - p| over |w| <= 8
      1          2       9.89e-06
      2          4       4.26e-07
      3          8       3.55e-08
      4         16       3.49e-10
      5         32       4.08e-17
```

Geometric in the section, with the rate set by the spectral tail
of the transfer (each additional word layer captures another power
of the subdominant spectrum).  This is a measured behavior, not a
theorem with constants — bin 3 of the taxonomy, said plainly.

### 5.3 Validity of sections

Compression *can* bend word positivity in principle: $p_m$ is a
quadratic form in compressed non-commuting letters, and cutting a
positive operator's off-section blocks has no general positivity
guarantee for *words* (only for each letter).  Measured: in this
ledger the sections remain **exactly valid** — min $p_m =
+9.6\times 10^{-4}$ over $|w| \le 10$ at every section — and since
$p_m \to p$ pointwise, any bending that does occur in other
ledgers dies with the section.  "Approximate processhood" is
thereby a quantified notion: a section is a finite-rank RP-form
whose word values and validity margins both converge to the
ledger's.  This is what "the record category is reached from
finite rank" *means*, operationally.

### 5.4 Sectors survive sections — asymptotically, with a mechanism

A two-sector ledger (block letters, sectors of dimension 60 each)
probed from a single sector-**mixed** cyclic state: the section's
transfer shows the **double Perron eigenvalue emerging with
depth** —

```text
   section m = 2 (dim  4): top eigenvalues 1.000000, 0.933229
   section m = 4 (dim 16): top eigenvalues 1.000000, 0.984880
   section m = 6 (dim 58): top eigenvalues 1.000000, 0.997888
   (third eigenvalue stays at ~0.86 throughout)
```

The mechanism is worth stating because it is *physics*: the
cyclic vector populates both sectors coherently, and the section
can only distinguish them through their **dynamical
distinguishability** — the rate at which the two sectors' word
statistics diverge.  The antisymmetric Perron direction therefore
enters the filtration gradually (its overlap with $V_m$ grows with
the accumulated statistical distance), and the superselection
structure is recovered in the limit — never lost, and exact at
*any* depth if the section is seeded per-sector (seed vectors in
each block: the double Perron is then present from $m = 0$).  A
record-keeping observer reconstructing the ledger from finitely
many words sees superselection emerge exactly this way.

## 6. Where the frontier genuinely begins

### 6.1 The continuous boundary, made visible

Every sector statement in the corpus — the collapse lemma, the
clustering theorem, the GNS = Frobenius identification — presumes
**atomic** sector structure: the fixed space of the transfer is
spanned by isolated, countable Perron directions, one per sector.
The boundary of that presumption is sharp, and a mock makes it
visible.  A ledger with fifty Perron directions spread across
$[1 - 10^{-3}, 1]$ (eigenvalue gaps down to $10^{-9}$):

```text
   tolerance tau:   1e-1   1e-3   1e-5   1e-7   1e-10
   'sector count':   50     49     33     17      1
```

There is **no tolerance-stable sector count**.  At coarse
resolution the ledger has fifty superselection sectors; at machine
resolution, one; in between, every intermediate answer.  The
question "how many sectors?" — the *first* question the atomic
formalism asks — has no answer here.  This is not a deficiency of
receipts or of rank; it is a deficiency of the **category**: the
atomic formalism ends where the Perron spectrum stops being
discrete.

### 6.2 What lives there, and what (T-cont) must be

The regime is not exotic — it is where some of the corpus' most
important physics is waiting:

- **symmetry-breaking families**: continuously many degenerate
  vacua (the record-SSB structures of P10's coordination law, at
  the thermodynamic boundary) are exactly a continuum of Perron
  directions;
- **the $(V)$ question** — the cosmological state — has always
  been $(V)$-adjacent to this: selecting "a vacuum" from a
  continuous family is a measure-theoretic act, not an eigenvalue
  count;
- **theta-vacuum-like structures**: families parametrized by a
  circle, where the physical sectors are direct integrals, not
  direct sums.

The mathematics that must replace the atomic formalism is known in
outline — **direct-integral decompositions** (the central
decomposition of the word functional over the spectrum of the
center, Bratteli–Robinson II) — and the corpus-specific work is to
rebuild the three sector-using theorems on it: the collapse lemma
(does a sealed even singlet collapse *fibers* of the integral?),
the clustering theorem ($T^n \to P_1$ still holds by Theorem 4.1 —
but $P_1$ is now a projection onto a direct integral, and
"per-sector simplicity" becomes "almost-every-fiber simplicity"),
and the GNS = Frobenius identification (fiber-wise).  A first
theorem would be: *for ledgers whose center has purely atomic
spectrum plus one continuous family, the (E) chain holds
fiber-almost-everywhere.*  That is a well-posed target, and it is
the only road on the frontier map not yet built:

**(T-cont)**: the direct-integral sector theory of record ledgers
with continuous Perron spectrum.

Everything below (T-cont) — the rank-free catalog, the SOT engine,
finite sections, atomic sectors — is structured, citable ground.

## 7. What this paper does not do

It does not extend the L3/tame *reconstruction* (P11/P12) beyond
the tame class — that is analysis of unbounded operators, untouched
here.  It does not turn finite-rank measurements (walls, searches)
into theorems — they remain measurements.  It does not build
(T-cont) — it isolates it.  And it does not claim the physical
record category is an inductive limit of finite ledgers — it shows
word-pointwise reachability, which is the operational notion, and
says so.

## 8. What a hostile reviewer should attack

```text
1. THE CATALOG'S "FUNCTORIAL IN RANK" is checked by reading proofs,
   not by a meta-theorem: a subtle rank dependence could hide in a
   proof.  Defense: each entry lists its reason; the receipts at
   growing d are tripwires, not proofs - and they are exact.
2. SOT IS WEAKER THAN NORM convergence: T^n -> P_1 strongly does
   not give uniform rates; clustering statements that need RATES
   (none in the (E) chain does) would need the gap after all.
3. SECTIONS WERE BUILT FROM ONE LEDGER FAMILY (random + structured
   spectra); pathological ledgers could section badly.  The
   geometric rate is the measured behavior, not a theorem with
   constants.
4. THE CONTINUOUS MOCK is finite (50 directions imitating a
   continuum): it demonstrates the FAILURE MODE of the atomic
   formalism, not the structure of the true continuous theory.
5. WORD-POINTWISE convergence is weak (no uniformity over word
   length); for diagonals at depth ~ rank, sections and truth can
   differ - exactly where the clock questions live, so P30's
   finite-rank framing remains the right one there.
```

## 9. What this paper proves and does not prove

Proves: the SOT engine theorem (4.1, complete proof) and its
corollary for the (E) chain (4.2); the rank-free portability
principle with its catalog and tripwire receipts (3.1).
Establishes by receipts: geometric section convergence; exact
validity of sections in the probed family; asymptotic sector
recovery; the tolerance-instability of sector counts at the
continuous boundary.

Does not prove: section convergence rates as a theorem; (T-cont)
in any form; the L3 extension; uniformity over word length.

## 10. The kernel after Paper 33

```text
STRUCTURED: the tame frontier.  'At stated scope' now decomposes,
  per result, into: rank-free (port verbatim - the catalog) /
  SOT-uniform (port by Theorem 4.1) / rank-receipted (measurements,
  no porting claim) / (T-cont)-bound (the named open).
UPGRADED: the (E) chain (P31) - its rank caveat is discharged by
  Corollary 4.2; what remains for it is sector formalization at the
  continuous boundary, i.e. (T-cont), shared with (V).
NEW NAMED: (T-cont) - direct-integral sectors for continuous Perron
  spectrum.
KERNEL: { (C-reg-rig), (NR), (ISO), assembly-(PR-RP+), (V),
  calibration, (T-cont) } + { O7/O8/O11 remainders,
  D10-refinements, mu-dyn, loop-H, (R-id), validity-genericity,
  d-threshold-of-chirality, minimality-principle (P31 7.1) }.
PROGRAM NOTE: the corpus' most-repeated caveat is no longer a
  gesture.  It is a map with one road not yet built, and the road
  has a name.
```

## References and literature map

- Papers 11, 12, 16, 30, 31 (internal): the tame class and L3; the
  Heller cone frame; the theorems catalogued; the (E) chain.
- M. Reed and B. Simon, "Methods of Modern Mathematical Physics I":
  the spectral theorem and strong convergence (Theorem 4.1's
  machinery).
- A. Bottcher and B. Silbermann, "Introduction to Large Truncated
  Toeplitz Matrices": the finite-section method - the classical
  home of Section 5's construction.
- O. Bratteli and D. W. Robinson, "Operator Algebras and Quantum
  Statistical Mechanics": direct integrals and sector
  decompositions - the frame (T-cont) must be built in.
```

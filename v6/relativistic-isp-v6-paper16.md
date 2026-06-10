# Paper 16 (v6) - SHARD: Process-O6 - The Separation Theorem

Author: Felix Robles Elvira

Subtitle:

```text
Process-O6 resolved as a SEPARATION.  Theorem A (Heller, restated in
record terms): a stationary process is a finite record law iff a finite
invariant cone exists - the ledger IS the cone, its rays the sealed
states.  Theorem B (proved here, via Frobenius peripheral-spectrum
theory): no process whose normalized diagonal sequence oscillates at an
irrational frequency ON its decay circle admits ANY finite positive
realization.  The witness - the RECORD CLOCK, a 3-dimensional renewal
construction with ANALYTIC validity (margin 0.3165 at all orders),
record rank EXACTLY 3 (fourth singular value 4.6e-16), exact
oscillation p(1^n)/kappa^n = a + b cos(n theta + c) at theta = 1 rad
(residual 3.3e-16, b = 0.0595), and machine-exact REVERSIBILITY
(8.3e-17 to word length 12) - is therefore a reversible, valid,
finite-record-rank process that is NOT a record law at any finite
ledger capacity:

   { finite record laws }  STRICTLY INSIDE
   { reversible, valid, finite-record-rank processes }.

And the unplanned finding: the clock FAILS reflection positivity
(Gram -4.1e-2; diagonal Hankel -1.0e-2), exactly as P8's typed moment
theorem demands - RP forces a real spectrum on the diagonal, and the
clock's mechanism is oscillation.  So the separation witness lives in
the reversible-but-not-RP stratum, P10 T4's Markov-presentation
hypothesis is sharp, and the question for the RP class is a NEW NAMED
RESIDUE (PR-RP): whether RP + finite rank implies a finite record law -
the clock mechanism is excluded there by the moment theorem itself
```

This paper executes item three of the standing plan.  Process-O6 was
located by Paper 11 as the positive-realization question; here it is
resolved as a classification with a proved separation theorem, an
explicit fully-analytic witness, and a sharp named residue.

## 0. Verdict

```text
THEOREM A (record-law characterization; named import, Heller 1965 /
positive-realization theory, restated in record terms).  A stationary
finite-valued process p is a FINITE RECORD LAW - a function of a
finite-capacity sealed Markov ledger; equivalently p(w) = pi M_{x_1}
... M_{x_n} 1 with everything entrywise nonnegative - if and only if
there exists a polyhedral cone K with finitely many rays such that
  (a) tau_x K is contained in K for every symbol x   (sealed update),
  (b) the stationary state lies in K,
  (c) the evaluation functional is nonnegative on K.
THE LEDGER IS THE CONE: rays = sealed states, capacity = ray count.
Direction "law => cone": the image of the probability simplex.
Direction "cone => law": the update matrices in the ray basis are
entrywise nonnegative - the chain on rays.  [Import status: classical;
both directions elementary; stated here because the corpus needs the
CONE reading, not just the HMM reading.]

THEOREM B (the obstruction; PROVED).  Let p be any stationary process
such that
    p(1^n) = kappa^n (a + b cos(n theta + c)),  a > |b| > 0,
    theta / 2 pi irrational.
Then p admits NO finite positive realization, of any dimension.
Proof sketch (full proof in Section 3): a positive realization gives
p(1^n) = pi M_1^n 1 with M_1 entrywise nonnegative.  The minimal
linear recurrence of the sequence has characteristic roots
{kappa, kappa e^{+i theta}, kappa e^{-i theta}}, all of modulus kappa,
and every realization's M_1 contains these among its eigenvalues.
Since a > |b| > 0 the sequence is exactly of order kappa^n, so kappa
is the spectral radius of the part of M_1 accessible from (pi, 1), and
kappa e^{+-i theta} are PERIPHERAL eigenvalues of an accessible block.
By Frobenius normal-form theory the peripheral spectrum of every
nonnegative block is its radius times a set of ROOTS OF UNITY; the
accessible contribution to p(1^n)/kappa^n is therefore asymptotically
periodic with a RATIONAL period, while a + b cos(n theta + c) with
theta/2pi irrational is almost periodic with no rational period.
Contradiction.

THE WITNESS (the record clock; constructed, validity ANALYTIC).
3-dimensional renewal OOM: tau_1 = kappa diag(R(theta), 1) with
kappa = 1/2, theta = 1; reset operator tau_0 = v (1^T - 1^T tau_1),
v = (0.07, 0, 0.93).  Lemma W (proved): the run-survival sequence
g(n) = 1^T tau_1^n v satisfies g(n) - g(n+1) >= kappa^n [v3(1 - kappa)
- A(1 + kappa)] = kappa^n * 0.3165 > 0, so every word probability is a
product of nonnegative renewal factors: the clock is a VALID stationary
process at all orders - no scope-limited premise.  Machine receipts:
  validity scan: min p(w) over ALL 2^16 words to length 16 = 7.3e-6;
  record rank exactly 3 (Hankel SVD: 1.97, 0.043, 0.014, then 4.6e-16);
  p(1^n)/kappa^n fits a + b cos(n + c) at 3.3e-16, |b| = 0.0595, and
    fits NO rational period P <= 12 (deviation >= 0.0168);
  reversibility: max |p(w) - p(reverse w)| = 8.3e-17 to length 12
    (stationary renewal: iid blocks - reversible by structure).
By Theorem B: NOT a record law at any finite capacity.  SEPARATION:
finite record laws are STRICTLY inside reversible, valid, finite-rank
processes.  Record rank is NOT record realizability.

THE UNPLANNED FINDING (the typed-theorem alignment).  The clock FAILS
reflection positivity: reflection Gram min eigenvalue -4.1e-2, diagonal
Hankel min eigenvalue -1.0e-2.  This is exactly P8's typed moment
theorem operating: site-RP forces the diagonal p(1^n) to be a Hamburger
moment sequence (real spectrum), and the clock's whole mechanism is a
complex pair on the decay circle.  Consequences:
  - reversibility does NOT imply RP without a Markov presentation:
    P10 T4's hypothesis is SHARP, witnessed;
  - the separation witness lives in the reversible-non-RP stratum;
  - for the RP class the question is OPEN and NEWLY NAMED:
    (PR-RP): does RP + finite record rank imply a finite record law?
    The clock mechanism is unavailable there (moment theorem); the
    positive-realization literature (Anderson: strictly dominant real
    pole implies realizability at possibly higher dimension) suggests
    the answer may be YES with a capacity gap - making RP not just
    necessary but nearly SUFFICIENT for sealability.  That would be a
    profound closure; it is NOT claimed.

THE POSITIVE SIDE (p16b).  A genuinely non-Markov reversible process
(2-symbol function of a hidden reversible 4-state chain): order-1/2
Markov fits fail (0.0123 / 0.00013), record rank 4, RP PASSES
(-3.7e-16), moment test PASSES, and the EXPLICIT Heller cone (the
simplex image) certifies it as a record law at capacity 4.  The
boundary in action: cone geometry, not rank, is the content.

PROCESS-O6 AFTER THIS PAPER: RESOLVED AS A CLASSIFICATION -
  sealable   = cone-finite   (Theorem A: the ledger is the cone);
  the strict gap to finite-rank consistency is PROVED (Theorem B +
    witness), so "approximable but not sealable" sectors EXIST;
  the RP-restricted question is the named residue (PR-RP).
```

## 1. Method and reproducibility

```text
code/v6_p16a_record_clock_campaign.py    the witness: validity, rank,
                                         oscillation, reversibility,
                                         RP failure + moment test
code/v6_p16b_heller_boundary_campaign.py the positive side: Heller
                                         cone certificate, RP pass,
                                         the boundary stated
```

Named imports: Heller's characterization (Theorem A; also Benvenuti-
Farina's positive-realization survey and Vidyasagar's treatment);
Frobenius normal form and Perron-Frobenius peripheral-spectrum theory
(the engine of Theorem B); Anderson's positive-realization existence
theorem (the (PR-RP) outlook; cited, not used).  Corpus inputs: the
process-O6 location and F1-F4 receipts (P11 4.4), the typed moment
theorems (P8 6), the reversibility/RP theorem and its Markov-
presentation hypothesis (P10 T2/T4).

## 2. Theorem A: the ledger is the cone

(Statement in Section 0.)  The corpus reading is the contribution: a
sealed record law of capacity m is EXACTLY an invariant polyhedral cone
with m rays.  Sealing a sector = exhibiting its cone; capacity = ray
count; the update operators act as nonnegative matrices on rays - the
relation code of the ledger.  Realizability questions about matter
sectors are CONE-GEOMETRY questions, and rank (the linear invariant)
is blind to them - as Theorem B now proves.

## 3. Theorem B: the proof

Let (pi, {M_x}, 1) be a positive realization of p, all data entrywise
nonnegative, and let h(n) := p(1^n) = pi M_1^n 1 = kappa^n (a +
b cos(n theta + c)) with a > |b| > 0 and theta/2pi irrational.

1. (Recurrence roots.)  h satisfies the minimal linear recurrence with
   characteristic roots {kappa, kappa e^{i theta}, kappa e^{-i theta}}
   (distinct, all of modulus kappa; minimality from b != 0, a != 0).
   For any realization, h(n) = pi M_1^n 1 implies every root of h's
   minimal recurrence is an eigenvalue of M_1 (standard: the Krylov
   space of (pi, M_1, 1) carries the recurrence).
2. (Accessibility reduction.)  Let I be the set of indices i such that
   pi reaches i and i reaches 1 through nonnegative powers of M_1
   (the accessible part).  Replacing M_1 by its principal submatrix on
   I changes no h(n); discard the rest.  On the accessible part,
   h(n) = Theta(kappa^n) (since a > |b|), so the spectral radius of
   the accessible M_1 is exactly kappa.
3. (Frobenius normal form.)  Permute the accessible M_1 to block upper
   triangular form with irreducible (or zero) diagonal blocks B_1..B_r.
   Each B_j is nonnegative irreducible with some period p_j; by the
   Perron-Frobenius/Frobenius theorem its peripheral spectrum is
   rho(B_j) times the p_j-th roots of unity.  All eigenvalues of M_1
   are eigenvalues of the diagonal blocks; in particular
   kappa e^{+-i theta} is a peripheral eigenvalue of some block with
   rho(B_j) = kappa - forcing e^{i theta} to be a p_j-th root of
   unity, i.e. theta/2pi rational... UNLESS no block has radius kappa
   carrying it.  But step 1 says kappa e^{i theta} IS an eigenvalue of
   the accessible M_1, hence of some diagonal block B_j, and
   |kappa e^{i theta}| = kappa <= rho(B_j) <= rho(M_1) = kappa forces
   rho(B_j) = kappa and peripherality.  Contradiction with theta/2pi
   irrational.                                                   QED

Remark (why the witness needs the oscillation ON the decay circle): if
the complex pair sits strictly below the dominant real eigenvalue, the
peripheral theorem says nothing - and indeed such sequences can be
positively realizable.  The clock construction places the rotation and
the survival weight at the SAME modulus by design (tau_1 = kappa
diag(R, 1)); validity then has to be re-won, which is what Lemma W's
margin 0.3165 does.

## 4. The witness and its receipts (p16a)

(Construction and numbers in Section 0.)  Three structural notes:

1. **Validity is analytic, not scanned.**  The renewal structure makes
   every word probability a product of run factors g(n) - g(n+1) and
   tail factors g(n), all bounded below by Lemma W.  The exhaustive
   2^16-word scan (min 7.3e-6) and the stationary-state check are
   AUDITS of the lemma, not its source.
2. **Reversibility is structural.**  A stationary renewal process is a
   stationary sequence of iid blocks; reversal permutes block order
   and fixes the law.  The machine receipt (8.3e-17 over 8000+ words)
   audits this.
3. **Rank 3 is exact.**  The fourth Hankel singular value is 4.6e-16
   against a third of 1.4e-2: the process is as finite-dimensional as
   a process can be - and still not sealable.  Record rank does not
   measure ledger capacity; the cone does.

## 5. The RP stratum and the residue (PR-RP)

The clock's RP failure is forced: by P8's typed theorem, site-RP makes
p(1^n) a Hamburger moment sequence - real spectrum, no oscillation.
Receipts: reflection Gram -4.1e-2; diagonal Hankel -1.0e-2 (the moment
test failing is the SAME fact at first invariant level).  Therefore:

```text
- P10 T4's "admits a reversible MARKOV presentation" hypothesis is
  sharp: reversibility alone does not give RP (witnessed).
- The separation of Section 0 lives in the reversible-non-RP stratum.
- (PR-RP) [NEW NAMED RESIDUE]: does RP + finite record rank imply a
  finite record law (possibly at higher capacity than the rank)?
  The clock mechanism is excluded from that class by the moment
  theorem; Anderson-type results (strictly dominant real pole =>
  positive realizability at some finite dimension) suggest YES with a
  capacity gap.  If (PR-RP) holds, RP - already a THEOREM for
  eventless presentable sectors (P10) - would be essentially
  EQUIVALENT to sealability at the process level: the arrow of record
  positivity and the existence of a finite ledger would be one
  condition.  Not claimed; named.
```

## 6. What this paper proves and does not prove

Proves: Theorem B in full (modulo textbook Perron-Frobenius theory,
named); Lemma W (analytic validity of the witness at all orders); the
witness' properties at machine precision (rank exactly 3, exact
oscillation form, reversibility, RP failure, moment-test failure); the
strict separation {finite record laws} inside {reversible, valid,
finite-rank}; the positive-side certificate (explicit Heller cone for
a non-Markov RP process, with RP and moment receipts passing).

Does not prove: (PR-RP) (the named residue); Theorem A internally (a
classical import, both directions elementary and restated); minimal-
capacity gaps (how much larger than the rank a ledger must be - the
literature has examples; not pursued); any continuum statement (this
is the process level by design; the continuum face of matter coupling
remains with (M) and the L3 residues).

## 7. The kernel after Paper 16

```text
process-O6  RESOLVED AS A CLASSIFICATION:
    sealable = cone-finite (Theorem A: ledger = invariant cone);
    sealable is STRICTLY smaller than finite-rank + reversible + valid
    (Theorem B + the record clock witness);
    "approximable but not sealable" matter sectors EXIST - P11's
    sharpened O6 now has a proved interior wall.
NEW NAMED RESIDUE:
    (PR-RP): RP + finite rank => record law?  (If yes: record
    positivity ~ sealability at process level.)
KERNEL: { (C-reg-b), (M), (V), (PR-RP) } +
        { D10, O7, O8-remainder, O11-remainder }.
        [process-O6 leaves the kernel as a named open; (PR-RP) enters
        as its sharpened successor.]
```

## 8. Status

```text
Theorem A:  record law <=> finite invariant cone (import, restated:
            the ledger IS the cone).
Theorem B:  irrational oscillation on the decay circle => no finite
            positive realization (PROVED, Frobenius peripheral).
Witness:    record clock - valid (analytic, margin 0.3165; scan
            7.3e-6 over 2^16 words), rank exactly 3 (4.6e-16),
            oscillation exact (3.3e-16, b = 0.0595, no period <= 12),
            reversible (8.3e-17).  NOT a record law.
Finding:    clock fails RP (-4.1e-2) and the moment test (-1.0e-2),
            exactly per P8's typed theorem; P10 T4's hypothesis sharp.
Positive:   non-Markov RP function-of-Markov: explicit Heller cone,
            RP -3.7e-16, moment test passes: record law at capacity 4.
Residue:    (PR-RP), named and bounded by the moment-theorem exclusion
            and the Anderson outlook.
```

## References and literature map

- Papers 8, 10, 11 (internal): typed moment theorems (P8 6 - the RP/
  moment alignment), reversibility/RP and the Markov-presentation
  hypothesis (P10 T2/T4), the process-O6 location and F1-F4 (P11 4.4).
- A. Heller, Ann. Math. Statist. 36, 1286 (1965): the cone
  characterization (Theorem A).
- M. Fox and H. Rubin, Ann. Math. Statist. 39 (1968); H. Jaeger,
  Neural Computation 12, 1371 (2000) (the "probability clock"): the
  classical irrational-rotation obstruction this paper's witness
  re-engineers as a renewal construction with analytic validity.
- L. Benvenuti and L. Farina, IEEE Trans. Autom. Control 49, 651
  (2004): the positive-realization survey.
- B. D. O. Anderson et al., IEEE Trans. Circuits Syst. (1996-99):
  existence of positive realizations under dominant-pole conditions
  (the (PR-RP) outlook).
- M. Vidyasagar, Hidden Markov Processes (2014): the modern treatment.
- F. R. Gantmacher, The Theory of Matrices, vol. II: Frobenius normal
  form and peripheral spectrum (the engine of Theorem B).
```

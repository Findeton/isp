# Paper 16 (v6) - SHARD: Process-O6 - The Separation Theorem

Preprint, not peer reviewed, version 2026-06-10.

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

THEOREM B (the obstruction; PROVED, Section 3).  Let p be any
stationary process such that
    p(1^n) = kappa^n (a + b cos(n theta + c)),  a > |b| > 0,
    theta / 2 pi irrational.
Then p admits NO finite positive realization, of any dimension.

THE WITNESS (the record clock; constructed, validity ANALYTIC,
Section 4): 3-dim renewal OOM with tau_1 = kappa diag(R(theta), 1),
kappa = 1/2, theta = 1; reset tau_0 = v (1^T - 1^T tau_1),
v = (0.07, 0, 0.93).  Valid at ALL orders (Lemma W: run margin
0.3165 > 0); record rank EXACTLY 3; oscillation exact (b = 0.0595,
fit residual 3.3e-16, no rational period P <= 12 within 0.0168);
REVERSIBLE to 8.3e-17.  By Theorem B: NOT a record law at any finite
capacity.  SEPARATION: finite record laws are STRICTLY inside
reversible, valid, finite-rank processes.  Record rank is NOT record
realizability.

THE UNPLANNED FINDING (the typed-theorem alignment, Section 5): the
clock FAILS reflection positivity (Gram -4.1e-2, diagonal Hankel
-1.0e-2) - P8's typed moment theorem in action: site-RP forces the
diagonal into the Hamburger moment class (real spectrum), and the
clock's whole mechanism is a complex pair on the decay circle.
Consequences: reversibility does NOT imply RP without a Markov
presentation (P10 T4's hypothesis is SHARP, witnessed); the separation
witness lives in the reversible-non-RP stratum; and the RP-restricted
question is OPEN and NEWLY NAMED:
  (PR-RP): does RP + finite record rank imply a finite record law?
The clock mechanism is unavailable there (moment theorem); Anderson's
dominant-pole realizability suggests YES with a capacity gap.  If true,
record positivity ~ sealability at process level.  NOT claimed; named.

THE POSITIVE SIDE (Section 6): a genuinely non-Markov reversible
process (2-symbol function of a hidden reversible 4-state chain):
order-1/2 Markov fits fail (0.0123 / 0.00013), record rank 4, RP
PASSES (-3.7e-16), moment test PASSES, and the EXPLICIT Heller cone
(the simplex image) certifies it as a record law at capacity 4.

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

Both scripts rerun bit-identically.  Named imports: Heller's
characterization (Theorem A; also Benvenuti-Farina's positive-
realization survey and Vidyasagar's treatment); Frobenius normal form
and Perron-Frobenius peripheral-spectrum theory (the engine of Theorem
B); Anderson's positive-realization existence theorem (the (PR-RP)
outlook; cited, not used).  Corpus inputs: the process-O6 location and
F1-F4 receipts (P11 4.4), the typed moment theorems (P8 6), the
reversibility/RP theorem and its Markov-presentation hypothesis
(P10 T2/T4).

## 2. Theorem A: the ledger is the cone

**Statement** as in Section 0.  **Proof sketch, both directions.**

(law => cone): given a positive realization (pi, {M_x}, 1) of
dimension m, take K = the image of the nonnegative orthant under the
realization's state map.  K is polyhedral with at most m rays;
nonnegativity of the M_x makes (a) hold; pi >= 0 gives (b); 1 >= 0
gives (c).

(cone => law): given K with rays r_1..r_m satisfying (a)-(c), expand
tau_x r_i = sum_j M_x[j, i] r_j with M_x[j, i] >= 0 (possible because
tau_x K is inside K and the r_j generate); the stationary state's
cone coordinates give pi >= 0 and the evaluation functional's values
on rays give the nonnegative output vector.  The triple is a positive
realization of capacity m.                                       QED

**The corpus reading is the contribution:** a sealed record law of
capacity m is EXACTLY an invariant polyhedral cone with m rays.
Sealing a sector = exhibiting its cone; capacity = ray count; the
update operators act as nonnegative matrices on rays - the relation
code of the ledger.  Realizability questions about matter sectors are
CONE-GEOMETRY questions, and rank (the linear invariant) is blind to
them - as Theorem B now proves.

## 3. Theorem B: the proof

Let (pi, {M_x}, 1) be a positive realization of p, all data entrywise
nonnegative, and let h(n) := p(1^n) = pi M_1^n 1 = kappa^n (a +
b cos(n theta + c)) with a > |b| > 0 and theta/2pi irrational.

**Step 1 (recurrence roots).**  h satisfies the minimal linear
recurrence with characteristic roots {kappa, kappa e^{i theta},
kappa e^{-i theta}} - distinct, all of modulus kappa; minimality from
a != 0, b != 0.  For any realization, h(n) = pi M_1^n 1 lives in the
Krylov space of (pi, M_1, 1), so every root of h's minimal recurrence
is an eigenvalue of M_1.

**Step 2 (accessibility reduction).**  Let I be the set of indices i
such that pi reaches i and i reaches the output through nonnegative
powers of M_1.  Restricting M_1 to I changes no h(n); discard the
rest.  On the accessible part, h(n) = Theta(kappa^n) (because
a > |b|), so the spectral radius of the accessible M_1 is exactly
kappa.

**Step 3 (Frobenius normal form).**  Permute the accessible M_1 to
block upper-triangular form with irreducible (or zero) diagonal blocks
B_1..B_r.  Each B_j is nonnegative irreducible with some period p_j;
by the Frobenius theorem its peripheral spectrum is rho(B_j) times the
p_j-th roots of unity.  All eigenvalues of M_1 are eigenvalues of the
diagonal blocks; in particular kappa e^{+-i theta} (Step 1) is an
eigenvalue of some block B_j, and |kappa e^{i theta}| = kappa <=
rho(B_j) <= rho(M_1) = kappa forces rho(B_j) = kappa and
PERIPHERALITY.  Hence e^{i theta} is a p_j-th root of unity, i.e.
theta/2pi is rational.  Contradiction.                            QED

**Remark (why the witness needs the oscillation ON the decay
circle).**  If the complex pair sits strictly below the dominant real
eigenvalue, the peripheral theorem says nothing - and such sequences
can indeed be positively realizable.  The clock construction places
the rotation and the survival weight at the SAME modulus by design
(tau_1 = kappa diag(R, 1)); validity then has to be re-won, which is
Lemma W's job.

## 4. The witness: the record clock

### 4.1 Construction and Lemma W

State space R^3; tau_1 = kappa diag(R(theta), 1) with kappa = 1/2,
theta = 1 rad (theta/2pi irrational since pi is irrational);
tau_0 = v (1^T - 1^T tau_1) with v = (v_1, 0, v_3) = (0.07, 0, 0.93):
every 0-symbol RESETS the state to v - a renewal process whose runs of
1s have survival sequence g(n) = 1^T tau_1^n v.

**Lemma W (validity at all orders).**  g(n) = kappa^n (v_3 +
v_1 (cos n theta + sin n theta)), and every word probability is a
product of run factors g(n) - g(n+1) >= 0 and tail factors g(n) >= 0.
*Proof.*  The renewal structure factorizes word probabilities by
construction.  For the run factors:

```text
 g(n) - g(n+1) >= kappa^n [ v_3 (1 - kappa) - A (1 + kappa) ],
 A = sqrt(2) v_1 = 0.0990:
 margin = 0.93 * 0.5 - 0.099 * 1.5 = 0.3165 > 0,
```

uniformly in n.  Hence all word probabilities are nonnegative and sum
correctly (sum of run probabilities telescopes to g(0) = 1): the
clock is a VALID stationary process - no scope-limited premise.   QED

**Reversibility (structural).**  A stationary renewal process is a
stationary sequence of iid blocks (a 0 followed by a run of 1s);
reversal permutes block order and fixes the law.  Machine audit:
max |p(w) - p(reverse w)| = 8.3e-17 over all words to length 12.

### 4.2 Receipts (p16a)

```text
validity:     analytic margin 0.3165 (Lemma W); exhaustive scan of
              ALL 2^16 words to length 16: min p(w) = 7.3e-6 >= 0;
              stationary state omega = (0.036, 0.021, 0.942) >= 0
record rank:  Hankel (63x63, words to length 5) singular values
              1.9705, 0.0433, 0.0142, then 4.6e-16: rank EXACTLY 3
oscillation:  p(1^n)/kappa^n fits a + b cos(n theta + c) at residual
              3.3e-16 with a = 0.9425, |b| = 0.0595; best rational
              period P <= 12 deviates by >= 0.0168
reversibility: 8.3e-17 (above)
```

### 4.3 Three structural notes

1. **Validity is analytic, not scanned.**  The scan and the
   stationary-state check are AUDITS of Lemma W, not its source - the
   witness needs no finite-scope premise.
2. **Rank 3 is exact.**  The fourth Hankel singular value is 4.6e-16
   against a third of 1.4e-2: the process is as finite-dimensional as
   a process can be - and still not sealable.  Record rank does not
   measure ledger capacity; the cone does.
3. **The cone picture of the failure:** the predictive states
   tau_1^n omega rotate by the irrational angle theta in a 2-plane;
   any finite invariant polyhedral cone would have to absorb a dense
   set of directions on a circle while staying finitely generated AND
   compatible with positivity of every output - Theorem B is the
   rigorous form of this geometric obstruction.

## 5. The RP stratum and the residue (PR-RP)

The clock's RP failure is forced, not accidental: by P8's typed moment
theorem, site-RP makes p(1^n) a Hamburger moment sequence - real
spectrum, no oscillation.  Receipts:

```text
reflection Gram (words to length 4, 31 x 31): min eig = -4.137e-2
   (FAILS PSD)
diagonal Hankel [p(1^(i+j))], 8 x 8:          min eig = -9.958e-3
   (FAILS the moment test - the SAME fact at first-invariant level)
```

Therefore:

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

## 6. The positive side: the Heller boundary in action (p16b)

A 2-symbol function of a hidden reversible 4-state chain (random
symmetric generator, lazy mixing, emission partition {1,2}|{3,4}):

```text
non-Markovianity:  |P(1|x,1) - P(1|y,1)| = 0.0123 (order 1),
                   0.00013 (order 2): genuinely non-Markov
record rank:       4  (singular values 2.113, 0.424, 1.95e-3,
                   2.06e-5, then 5.5e-16)
Heller cone:       the simplex image: tau_x(rays) >= 0 entrywise
                   TRUE; omega in K; 1^T >= 0 on K - certificate
                   complete at capacity 4
RP:                reflection Gram min eig = -3.7e-16 (PASSES, as
                   P10 T4 demands for a reversible presentation)
moment test:       diagonal Hankel min eig = -3.8e-18 (PASSES)
```

The boundary in one table: the clock (rank 3, reversible, valid) fails
the moment test and has NO cone at any dimension; this process (rank
4, non-Markov, RP) carries an explicit cone at capacity 4.
Process-O6's content is CONE GEOMETRY, not rank: the ledger is the
cone, and matter sectors divide into cone-finite (sealable) and
cone-infinite (approximable only).

## 7. What this paper proves and does not prove

Proves: Theorem B in full (Section 3; modulo textbook Perron-Frobenius
theory, named); Lemma W (analytic validity of the witness at all
orders); the witness' properties at machine precision (rank exactly 3,
exact oscillation form, reversibility, RP failure, moment-test
failure); the strict separation {finite record laws} inside
{reversible, valid, finite-rank}; the positive-side certificate
(explicit Heller cone for a non-Markov RP process, with RP and moment
receipts passing); Theorem A's two directions at the sketch level of
Section 2 (elementary; the statement is a classical import restated).

Does not prove: (PR-RP) (the named residue); minimal-capacity gaps
(how much larger than the rank a ledger must be - the literature has
examples; not pursued); any continuum statement (this is the process
level by design; the continuum face of matter coupling remains with
(M) and the L3 residues).

## 8. The kernel after Paper 16

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
[Paper 26 update: the clock became an INSTRUMENT - the signed-Hankel
        "clock test" on quantum-processor syndrome streams (a
        structural no-go for finite-state noise models, with a
        numbered hardware protocol), and the Heller cone became the
        classical-simulability boundary (advantage = cone violation,
        the (QC-adv) conjecture).  See Paper 26, Sections 6 and 8.3.]
```

## 9. Status

```text
Theorem A:  record law <=> finite invariant cone (import, restated
            with both directions sketched: the ledger IS the cone).
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

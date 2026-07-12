# D6 hostile review, round 1: independent reconstruction and reproducibility

**Referee:** independent clean-room reconstruction

**Date:** 2026-07-11

**Verdict:** **MAJOR REVISION of the receipt, with the central supplied-change/not-proposal boundary independently confirmed**

The core result is correct and important. Given two strictly positive ordered
laws on one already supplied finite history space, their RN field is
canonical and supplies a conditional factor value, relative orientation,
essential coordinate dependence, and directed KL evidence. The v6 equations
then supply a conditional commitment coefficient for an already supplied
primitive mode and a conditional survival law for already supplied evidence.
None of these operations constructs an extension opportunity, null mass,
primitive mode set, physical ownership, or accepted birth. The paper states
that boundary honestly.

All 60 registered Boolean conditions reproduce independently, including the
high-precision root, Walsh reconstruction, hidden-lift values, proposal and
h-transform controls, determinants, and projective towers.

The receipt nevertheless contains several overgraded or missing gates:

1. it has no fixed `EXPECTED_CHECKS=60` assertion and prints
   `CHECKS/CHECKS`, which would report success after silent check deletion;
2. the preregistered additive survival identity is not executed;
3. scope nonselection is tested by comparing dictionaries with different key
   lengths, not by constructing two commitment-root modes;
4. primitive-token ownership nonuniqueness is “tested” by the literal
   assertion `1 != 2`;
5. the h-transform and generic normalization helpers do not enforce their
   claimed positive-probability input types; and
6. the hidden-lift “future” is a static hidden-coordinate readout unless an
   explicit common future kernel is added.

These are receipt and claim-support defects, not a refutation of the central
refusal. They require another review round.

## 1. Frozen snapshot and deterministic execution

```text
daf14e0ea008509e106fd6419ee463b964b5b1a15a9d61ed6e6842a432434c20  v10/note-d6-sealed-holonomy-factor-token.md
7de6f94a4cf77eb780da245e26a60d6677be1c59fd6233a3dfd1e8f18d8c0388  v10/code/d6_sealed_holonomy_token_exact.py
63ad2759c4355143fc2f0f66658294a01a0b56b16ba992143be67e8983ecc9d0  v10/relativistic-isp-v10-paper7-sealed-holonomy-reconstructs-change-not-birth.md
```

Production command:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 v10/code/d6_sealed_holonomy_token_exact.py
```

Two sequential executions exited zero and produced byte-identical stdout:

```text
fa513bd65bf6f674a2b203e4e35192b58b8ecdec0018637a3a9528c63f375a4c
```

The internal payload digest is:

```text
58b0963297c57f78e401731fbf6fe93e338dfdb5e51d59c7699962a0788453f7
```

The final self-containment audit reports 4/4:

```text
PASS: all v10 investigation executables reside in v10/code
PASS: no duplicate investigation source exists outside v10/code
PASS: every investigation executable imports only the Python standard library
PASS: no .pyc cache artifact exists under v10
```

## 2. Independent implementation

I wrote a separate Ruby implementation using exact `Rational` arithmetic and
`BigDecimal/BigMath` at 150-digit precision. It imports no production code.
Its SHA-256 is:

```text
8575c32b7a1e5357de5a6f2de3068ea2e83142fb1141a2800c60a3b9b4146d4f
```

It independently reconstructs:

1. RN fields, KL, products, relabeling, and essential scope;
2. parity laws, all proper marginals, and hidden lifts;
3. exact Walsh matrices/ranks and high-precision log-density inversion;
4. the commitment root, oriented mode probabilities, and survival;
5. proposal/null distributions and h-transforms;
6. one-token versus two-token extensional representations;
7. reducible and irreducible cross determinants; and
8. both Bernoulli projective towers.

The registered check distribution is independently:

```text
RN block          12
history/ledger    24
commitment/seal    8
proposal/token    11
profinite          5
total             60
```

Independent numerical output:

```text
RN ratio=[1/3,3]
directed KL=0.549306144334054845697622618461262852323745278911...
Walsh reconstruction gap≈1E-149 at independent precision 150
top parity log coefficient=0.5493061443340548456976226184612628523...
hidden readout=7/12 versus 5/12
commitment root=0.6093778634360062315368033711683986954...
root residual≈4E-150
survival at symmetric KL=0.5773502691896257645091487805019574556...
proposal null masses=1/3 versus 1/2
h-transforms={a:1/3,b:2/3} versus {a:1/2,b:1/2}
irreducible/product determinants=2/0
projective tower levels=5/5, distinct at level one
```

The production `1E-110` Walsh gap is a working-precision floor; the
independent higher-precision result is consistent with exact Fourier
inversion.

## 3. RN reconstruction — pass

For

$$
P=(1/4,3/4),\qquad Q=(3/4,1/4),
$$

the clean-room RN field is `(1/3,3)`. Exact arithmetic verifies:

$$
E_QR=1,
\quad E_PR^{-1}=1,
\quad P=QR,
\quad R_{Q/P}=R^{-1}.
$$

`P=Q` gives exactly `R=1` and zero KL. Product laws give product RN
fields, and joint atom relabeling transports the field correctly. A different
pair on the same support gives a different field, so support alone does not
select it.

The swapped witness has

$$
D(P\Vert Q)=D(Q\Vert P)=\tfrac12\log3,
$$

while its oriented RN fields are inverse. Scalar KL therefore does not retain
orientation. These claims are definition-level but correctly executed.

The theorem is explicitly conditional on `P,Q` and their common atom space.
It does not reconstruct either law from a pre-law record snapshot.

## 4. Whole-history shadows and complete-ledger reconstruction — pass with the stated circularity ceiling

For three-bit parity twins at `theta=±1/2`, all six one- and two-coordinate
marginals agree exactly. The full laws differ and their triple expectations
are `+1/2` and `-1/2`. Relative to uniform, the positive twin's RN field has
essential coordinates `(0,1,2)`.

Independent exact ranks of the complete Walsh character matrices are
`2,4,8,16` for `n=1,...,4`. Removing the constant gives `2^n-1`, matching
the binary simplex dimension. The complete log-density transform reconstructs
the supplied positive parity law, while the top parity coefficient is
load-bearing. The parity twins supply the nontrivial fiber after that top
coordinate is discarded.

The paper handles the circularity correctly:

- a complete separating cochain identifies a supplied finite law;
- it has as many nonconstant free coordinates as that law;
- Fourier inversion does not construct the physical primitive contrasts,
  their orientation, or their coefficient values.

The phrase “complete closed-holonomy ledger” is therefore a supplied full
coordinate system in this audit, not a newly derived birth mechanism.

## 5. Hidden-lift witness — exact arithmetic passes; the dynamical wording needs one more object

The two lifts preserve both endpoint laws and the complete RN field. The RN
ratio depends only on the endpoint coordinate. Their hidden `H=+1` marginals
are nevertheless `7/12` and `5/12`.

This proves that the supplied endpoint atom space/RN action can omit a
future-relevant hidden distinction. It does not, by itself, execute a temporal
future transition: `future_a` and `future_b` are sums over the already
constructed hidden coordinate. The paper can make the claim literal by
attaching one common future kernel, for example deterministic `Y=H`, and then
computing `P(Y=+1)` for both lifts. Alternatively it should consistently call
the existing quantities hidden readouts rather than future probabilities.

The conceptual lesson survives either repair.

## 6. Commitment and survival — root passes; two registered controls are missing or tautological

Independent bisection gives

$$
h_*=0.6093778634360062315368033711683986954\ldots
$$

with `tanh h_*=exp(-h_*)` to more than 125 digits. Opposite logistic
orientations normalize and differ. At the symmetric directed KL, survival is
`1/sqrt(3)`, strictly between zero and one, and is the same for the reverse
orientation.

The v6 corpus really does state the conditional equations

$$
S(I)=e^{-I},
\qquad \nabla\psi(h)=e^{-h},
$$

on a supplied complete primitive oriented ledger. D6 is faithful in treating
them as conditional rather than as a mode/proposal generator.

### Missing C1 gluing gate

The preregistration requires

$$
S(I+J)=S(I)S(J).
$$

Production never evaluates this identity. It checks only `S(0)=1`, positivity
at one evidence value, and reversal blindness. The clean-room control at
independent `I=0.37`, `J=0.22` gives a gap below `1E-149`, but the production
receipt must add an exact/high-precision multiplicativity gate and explicitly
check the division probability `1-S(I)`.

### Tautological C4 scope gate

Production checks:

```python
parity_law(1, 1/2) != parity_law(2, 1/2)
```

The dictionaries have keys of different lengths and therefore must be
unequal. This does not apply the commitment root to either mode, verify that
both satisfy the same fixed-point equation, or audit their essential scopes.

**Required repair:** construct the one-body and two-body parity exponential
families at `theta=tanh(h_*)`, verify normalization/positivity, show essential
scopes `(0)` and `(0,1)`, and check the same root equation for both. Do the
analogous explicit mirror construction for orientation reversal.

The paper's scope/orientation nonselection argument is correct; the current
receipt does not meaningfully test it.

## 7. Proposal and h-transform — central nonselection passes, input validation remains weak

The two null-inclusive laws

$$
(1/3,1/3,1/3),
\qquad(1/2,1/4,1/4)
$$

are normalized, treat forward/reverse symmetrically, and have different null
mass. Thus candidate symmetry and fixed comparison evidence do not determine
proposal intensity.

The h-transform controls reproduce:

```text
h1 -> (a:1/3,b:2/3)
h2 -> (a:1/2,b:1/2)
add c -> a changes from 1/3 to 1/4.
```

This is faithful to v7 Paper 31, which supplies deletion multiplicities,
candidate domains, and teacher-dependent positive shadow weights only in an
audited finite sector and explicitly refuses universal intrinsic uniqueness.
D6 correctly treats the h-transform as a normalizer/compiler, not a generator
of its own domain or weights.

The helper does not validate that `domain` is duplicate-free, every `h` value
is positive, or every resulting multiplicity-weight is nonnegative. With
signed inputs and positive total it can return negative “probabilities.” The
generic `normalize` helper has the same total-only validation defect.

**Required repair:** validate a unique finite domain, positive `h`,
nonnegative multiplicities, and positive total; add explicit signed-input
refusals. This matters because positivity is a named premise of the imported
h-transform.

## 8. Primitive ownership — mathematical counterexample exists, production gate is a literal tautology

The product RN field satisfies

$$
R(x,y)=R_1(x)R_2(y).
$$

It can be represented extensionally by:

1. one composite two-coordinate token carrying `R`; or
2. two one-coordinate tokens carrying `R_1` and `R_2`.

The clean-room reconstruction builds both representations, confirms their
product fields agree, and confirms token counts one and two.

Production verifies the field equality and then uses:

```python
check(1 != 2, "joint law does not encode primitive token census")
```

That second condition cannot fail and contains no token, scope, identity,
ownership map, or decomposition.

**Required repair:** represent the one-token and two-token decompositions as
typed records with distinct scopes/IDs, contract both to the same joint field,
and compare their primitive census/ownership explicitly. This is load-bearing
because missing physical ownership is one of the final verdict's named
nonselection fields.

## 9. Cross-component factor control — pass at the RN-field level

For the two-bit parity RN field, independent reconstruction gives cross
determinant

$$
R_{--}R_{++}-R_{-+}R_{+-}=2.
$$

The product RN field has determinant zero. Thus independent component laws
cannot yield an irreducible cross RN factor; an irreducible field requires a
joint law/factor already crossing the cut.

The paper draws the correct ceiling. RN arithmetic detects and compiles the
joint field after it is supplied. It does not propose or nucleate the first
cross-component carrier.

## 10. Token census — honest prose, illustrative executable

The five conditional statuses and four missing statuses are entered as string
literals and counted. This is not a derivation, but unlike the ownership gate
the manuscript presents it as a logical accounting table. The exact witnesses
elsewhere support most entries.

One terminology distinction should remain explicit: `essential_scope(R)` is
relative coordinate dependence. It is not yet D5's primitive listed token
scope, because D5 showed that listed scope, essential scope, separability,
and primitive incidence differ. Likewise an RN factor **value** is suitable
for D5 arithmetic only after a unique physical token identity/ownership is
supplied. The D6 object is therefore an incomplete conditional RN factor
field, not a complete D5 primitive factor token.

## 11. Profinite towers — pass

Both Bernoulli families, `p=1/3` and `p=2/3`, normalize and marginalize exactly
under deletion through five levels. They differ at level one. Their product
formulas extend to every finite level and determine distinct inverse-limit
measures by the standard projective theorem.

The conclusion is properly limited: profinite compatibility hosts both laws
and selects neither parameter, proposal rate, or interaction sector.

## 12. Receipt integrity defect — `60/60` is not frozen

`check()` increments `CHECKS` after each assertion, but the executable never
asserts that the final count equals the preregistered 60. It prints:

```python
f"RECEIPT: {CHECKS}/{CHECKS} ... passed"
```

If one or several check calls were accidentally deleted, the receipt would
silently report `59/59` or `58/58` as a complete pass. The internal payload
would change, but no expected digest is gated either.

**Required repair:** define `EXPECTED_CHECKS=60`, use explicit exception-based
checks rather than optimization-sensitive Python `assert`, and fail unless
`CHECKS==EXPECTED_CHECKS` before printing `CHECKS/EXPECTED_CHECKS`.

## 13. Corpus fidelity and supplied-law/proposal distinction — pass

The necessary older sources support D6's corrected reading:

- v6 supplies `S(I)=exp(-I)` and `grad psi(h)=exp(-h)` only after a complete
  primitive oriented RN/KL ledger is in place;
- v7 Paper 31's finite h-transform receives a candidate set, deletion
  multiplicities, a center, and positive teacher-calibrated weights; it marks
  intrinsic center/weight construction and projective uniqueness as open.

D6 does not claim that likelihood comparison creates its compared laws. It
does not call conditional normalization proposal generation. It does not call
seal probability accepted birth. It correctly identifies the remaining
law-level object as a null-inclusive extension-opportunity measure or the
corresponding conditional part of a primitive path measure.

This central distinction is not circular. The complete-ledger reconstruction
would become circular only if presented as selection; the paper explicitly
calls it identifiability of supplied coordinates.

## 14. Editorial issues

The manuscript contains several duplicated lines/paragraph openings:

- the binary witness repeats the `Q=(3/4,1/4)` line;
- the Section 7 heading/opening appears twice; and
- Section 12.1 repeats the sentence ending “derived descriptions or
  consistency checks of that law.”

These are not mathematical blockers but should be removed before final
review.

## 15. Numbered openings and repairs before round 2

1. **Freeze receipt cardinality.** Add `EXPECTED_CHECKS=60`, explicit failure
   exceptions, a final equality gate, and a non-tautological denominator.
2. **Execute survival gluing.** Test `S(I+J)=S(I)S(J)` at independent positive
   evidence values and test `1-S(I)` as the conditional division probability.
3. **Replace the scope tautology.** Build one- and two-body commitment-root
   modes, verify the same root equation, and audit their distinct essential
   scopes and mirrored orientations.
4. **Replace `1 != 2`.** Encode one-composite-token and two-primitive-token
   decompositions with scopes and unique IDs, then verify extensional equality
   and census/ownership inequality.
5. **Type the h-transform.** Refuse duplicate domains, missing keys, signed or
   zero `h`, negative multiplicities, and nonpositive totals.
6. **Make the future witness temporal.** Add one explicit common future kernel
   driven by hidden `H`, or downgrade all labels to hidden-readout rather than
   future prediction.
7. **Separate RN scope from primitive scope.** Call the reconstructed object an
   RN factor field/value until listed scope and exactly-once ownership are
   physically supplied.
8. **Strengthen the token census.** Derive each status from constructed data
   or label the string table explicitly as a prose ledger rather than a
   theorem gate.
9. **Clean manuscript duplication.** Remove the repeated witness, Section 7
   opening, and Section 12.1 sentence.

## 16. Final determination

The strongest independently supported statement is:

$$
\boxed{
\text{sealed holonomy reconstructs and conditionally commits a supplied
ordered change; it does not propose the next record birth.}
}
$$

That boundary is fair and survives hostile reconstruction. The receipt does
not yet deserve final PASS because several named nonselection fields are
supported by tautological or absent gates and the check-count/type validators
are not robust.

**Round-1 independent-rebuild verdict: MAJOR REVISION.**

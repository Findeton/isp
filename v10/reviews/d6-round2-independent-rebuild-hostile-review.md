# D6 hostile review, round 2: independent reconstruction and reproducibility

**Referee:** independent clean-room reconstruction  
**Date:** 2026-07-11  
**Verdict:** **PASS — the repaired 84-condition receipt and the narrowed theorem boundary reproduce independently**

The round-1 defects assigned to this stream are closed. I independently
rebuilt the finite RN, Walsh, hidden-lift, commitment, survival,
h-transform, ownership, determinant, and projective-tower calculations
without importing the production executable. The independent result has the
same check distribution as production:

```text
RN reconstruction       12
history/ledger           28
commitment/survival      17
proposal/token           18
profinite                 9
total                    84
```

The production program passes both ordinary and optimized Python execution,
with byte-identical output. The final `EXPECTED_CHECKS=84` gate is explicit
and cannot disappear under `python -O`. More importantly, the newly added
conditions are substantive reconstructions rather than replacements by a
larger self-reported number.

The paper's positive result remains conditional: supplied ordered laws
determine their RN field; a supplied normalized oriented mode admits the v6
coefficient; supplied additive evidence admits numerical survival/division
weights. The paper does not promote those calculations to a typed diamond,
physical holonomy measurement, proposal opportunity, evidence carrier,
physical ownership, realized seal, or record birth.

## 1. Frozen round-2 snapshot and execution

```text
4addff806650f5286f567565f2369fb1014ae625116c45af215c098024287983  v10/code/d6_sealed_holonomy_token_exact.py
e1980919ee128dc2ae9d34b90df3095b0877be92fbdb35360aecf7ab5ce061f3  v10/note-d6-sealed-holonomy-factor-token.md
93af04e284258cb8008ef3933aa4b608893e0c8da520d1eb6effebd2dedfc8c8  v10/relativistic-isp-v10-paper7-sealed-holonomy-reconstructs-change-not-birth.md
```

Both commands exited zero:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 v10/code/d6_sealed_holonomy_token_exact.py

PYTHONDONTWRITEBYTECODE=1 \
  python3 -O v10/code/d6_sealed_holonomy_token_exact.py
```

Their complete standard output has the same SHA-256:

```text
7c1940601bad3a570b25afc2cab605e4e4d1926d2efb2e6708465d00c133f10c
```

The reported internal payload digest is:

```text
dbd7446345106df64878b6181cdb24ce6b76f761a42fe274b2c13aa0ca6f7365
```

There is no use of Python's optimization-sensitive `assert` statement.
`check()` raises `AssertionError` explicitly, and a separate final branch
raises if `CHECKS != EXPECTED_CHECKS` before the receipt is printed.

## 2. Independent implementation

I revised the round-1 clean-room Ruby implementation rather than importing or
transliterating the production module at runtime. It uses exact `Rational`
arithmetic for finite laws, marginals, ranks, factorization, determinants,
and projectivity, and `BigDecimal/BigMath` at 150 digits for logarithms,
exponentials, Walsh inversion, and the commitment root. Its round-2 SHA-256
is:

```text
8da7e14a1d550ad8849cb940236bdbbf832fd916c62bad4499da0b54776b0653
```

Independent output includes:

```text
checks                         84
group counts                   R=12, H=28, C=17, P=18, F=9
RN field                       (1/3, 3)
directed KL                    0.5493061443340548456976226184612628523...
Walsh reconstruction gap       about 1E-149
top parity log coefficient     0.5493061443340548456976226184612628523...
hidden/future probabilities    7/12 and 5/12
commitment root                0.6093778634360062315368033711683986954...
root residual                  about 4E-150
survival multiplicative gap    about 7E-150
commitment mode scopes         (0) and (0,1)
ownership representations      extensionally equal, census 1 and 2
cross/product determinants     2 and 0
projective tower levels        5 for each of three towers
```

The production Walsh gap `1E-110` is its Decimal working-precision floor,
not evidence of a mathematical reconstruction error. The higher-precision
independent result is consistent with exact finite Walsh inversion.

## 3. Opening 1 — fixed receipt cardinality and `-O`: closed

Production now declares `EXPECTED_CHECKS = 84`, increments only after a
condition succeeds, and checks equality with the fixed expectation before
printing `84/84`. A deleted check therefore produces cardinality drift rather
than a smaller self-congratulatory `N/N` receipt. Ordinary and optimized runs
are byte-identical.

A fixed count alone cannot certify that the right propositions were tested;
that is why the remaining sections reconstruct the semantics of the 84
conditions. On that stronger audit, the added conditions correspond to the
advertised repairs.

## 4. Opening 2 — survival gluing: closed

At independently chosen positive evidence values `I=0.37` and `J=0.22`, both
implementations verify at high precision

$$
e^{-(I+J)}=e^{-I}e^{-J}.
$$

The clean-room gap is about `7E-150`. Production also verifies `S(0)=1`,
`0<S(I)<1` at positive evidence, reversal blindness of the scalar for the
swapped witness, and the complementary numerical weight

$$
(1-S)+S=1.
$$

The manuscript correctly calls these numerical weights conditional on actual
additive evidence. It does not call the expected KL itself a realized carrier
or call `1-S` a sampled physical seal.

## 5. Opening 3 — commitment scope and mirror modes: closed

The old dictionary-arity inequality is gone. Production and the independent
rebuild construct

$$
P_n(x)\propto \exp(h_*\,\chi_{1\cdots n}(x))
$$

for one- and two-coordinate parity modes at the same positive root. Both
families normalize, are strictly positive, and have presentation-relative
essential coordinate sets `(0)` and `(0,1)`. Their mean parity is
`tanh(h_*)=exp(-h_*)`. Reversing the two-body orientation produces the
coordinate-flipped mirror law.

This now supports the exact claim being made: the scalar equation selects a
coefficient after a normalized oriented mode has been supplied, but it does
not select that mode's scope or orientation. The paper also preserves the
normalization/unit qualification and the unresolved v6-to-v7 bridge
`h_commitment ?= h_effective`.

## 6. Opening 4 — explicit token decomposition and ownership: closed

The literal `1 != 2` condition has been replaced. The executable constructs:

1. one token with ID `xy`, scope `(0,1)`, and the composite RN table; and
2. two tokens with IDs `x,y`, unary scopes, and unary RN tables.

An evaluator contracts each representation on the same two-bit atom space.
Both give the same product RN field, while their token counts and ID
partitions differ. A duplicated ID is explicitly refused. The clean-room
implementation obtains the same extensional equality and census `1` versus
`2`.

This is a valid non-identifiability counterexample: the extensional joint
field does not choose a primitive token decomposition. It does not pretend
that the sample IDs themselves derive physical ownership. The manuscript
correctly leaves the physical primitive decomposition open.

## 7. Opening 5 — typed h-transform refusals: closed

The repaired h-transform requires:

- a finite, nonempty, duplicate-free supplied candidate tuple;
- an `h` value and multiplicity for every candidate;
- strictly positive `h` values;
- nonnegative multiplicities; and
- a positive normalization total.

Production and the clean-room rebuild both refuse duplicate candidates, zero
`h`, a negative multiplicity, and missing multiplicity data. On valid input,
different supplied `h` fields produce different transitions, and changing
the candidate domain changes the normalization. This supports the compiler,
not generator, reading of the v7 h-transform.

## 8. Opening 6 — common future kernel: closed at the stated finite level

The two lifts have identical endpoint marginals and identical full RN action,
which depends only on the endpoint coordinate. Production then declares the
same deterministic readout kernel `Y=H` on both lifts. Applying that common
kernel gives

$$
P_a(Y=+1)=7/12,
\qquad
P_b(Y=+1)=5/12.
$$

The added kernel check is arithmetically close to the preceding hidden
marginal check, but it supplies the missing temporal interpretation rather
than changing the numbers. The paper limits the result appropriately: an RN
comparison is complete only relative to its supplied atom space and cannot
certify that every future-relevant distinction was already represented.

## 9. Opening 7 — RN coordinate dependence versus primitive scope: closed

The note and paper now consistently call `essential_scope(R)`
**presentation-relative essential coordinate dependence**. They explicitly
deny that this is physical incidence, primitive D5 scope, a unique token ID,
or a complete-cover allocation. They also deny that supplied `AB/BA`
orientation establishes a construction-order gauge.

This is the necessary ontology correction. The arithmetic identifies which
listed coordinates a supplied table varies with. It does not tell the theory
which physical records participated in producing the table.

## 10. Opening 8 — token census status: honestly sustained

The executable's `token_fields` dictionary remains a string-valued status
ledger, and its count of five `missing` values remains bookkeeping rather
than an independent theorem. Round 2 does not disguise this. The opening
ledger explicitly records R8 as sustained, and the manuscript supplies the
real arguments before presenting the census:

- proposal/null freedom is witnessed by two symmetric proposal laws;
- physical ownership freedom is witnessed by equal one-/two-token fields;
- physical scope is separated from coordinate dependence;
- expected evidence and numerical weights are separated from a carrier,
  sampled commitment, and seal; and
- accepted birth is absent because no history-extension kernel is built.

Thus the string census is a summary of proved counterexamples and declared
missing constructors, not an alleged derivation by counting labels. That is
an acceptable disposition and matches the narrowed prose.

One presentational limitation remains worth recording: the executable ledger
does not list `physical_scope`, `token_ID`, and `null_mass` as separate keys,
although its final verdict names their nonselection. The paper's fuller table
does list the distinction, and independent witnesses establish it. This is
not a mathematical or receipt blocker because the code does not claim its
string dictionary is exhaustive or derivational.

## 11. Opening 9 — prose cleanup: closed

The repeated binary-witness line, duplicated Section 7 opening, and repeated
Section 12.1 sentence reported in round 1 are absent. The current paper has
one proof heading for the RN theorem, one h-transform discussion in Section
8, and one path-measure consequence paragraph in Section 12.1.

## 12. Remaining mathematical blocks reproduce

The unaffected and extended parts also pass independent reconstruction:

- exact RN normalization, reversal, product, and relabeling identities;
- equal scalar KL but inverse RN fields for the swapped witness;
- six equal proper shadows and opposite triple moments for parity twins;
- exact Walsh ranks `2,4,8,16` and complete supplied-law identifiability;
- equality of all lower log-Walsh coefficients and opposite nonzero top
  coefficients for the twins;
- a nonproduct two-bit RN determinant `2` versus product determinant `0`;
- three exact end-deletion Bernoulli towers through five audited levels; and
- a third `p=1/2` tower outside the sign-mirror pair.

I additionally checked the `p=1/3` to `p=2/3` global-sign mirror through all
five constructed levels, not just level one. Analytically it holds for every
level because flipping all bits interchanges the counts of plus and minus
outcomes in the Bernoulli product formula. The production receipt checks the
mirror only at level one, but the manuscript's all-level statement follows
directly from its displayed family, so this creates no new opening.

## 13. Corpus fidelity and circularity boundary

The repaired manuscript preserves the older corpus at its actual strength.
V6's survival and commitment equations are conditional on supplied evidence
and a supplied primitive oriented ledger/mode. V7's finite h-transform is
conditional on a candidate domain, multiplicities, center/shadow, and
effective weights. D6 does not use either construction to manufacture its
own premises.

The complete Walsh/log-density ledger has exactly as many nonconstant
coordinates as the positive finite law has degrees of freedom. Its inversion
is therefore identifiability of supplied full coordinates, not physical
selection of their loop provenance, primitive units, orientation, or measured
values. The paper explicitly identifies the circularity in defining the
primitive quotient from “all future-relevant” contrasts before a future
response law has been derived.

Likewise, the executable contains no typed diamond, exchange loop, screen,
cocycle provenance, or sealed record. The title, abstract, theorem, receipt,
and conclusion now consistently call the executed result conditional
ordered-law RN reconstruction. “Sealed holonomy” remains a corpus motivation,
not an executable theorem.

## 14. Search for new openings

I found no new blocking mathematical, reproducibility, or scope opening.
Three limitations are real but already disclosed or harmless at this claim
ceiling:

1. a fixed check cardinality is receipt integrity, not proof that each check
   is meaningful; the clean-room semantic reconstruction supplies that audit;
2. the common deterministic future-kernel condition repeats the hidden
   marginal numerically, but now makes the claimed readout map explicit; and
3. production checks the Bernoulli sign mirror at level one, while the
   all-level result follows analytically from the stated product family and
   was independently checked through all five executable levels.

None licenses a stronger physical claim. In particular, D6 still does not
derive a proposal opportunity, bridge carrier, realized evidence process,
seal, or null-inclusive interacting click law.

## 15. Final determination

Every round-1 independent-rebuild opening is either substantively repaired or,
for the string token census, explicitly and correctly sustained as a logical
ledger rather than a theorem. The 84 conditions reproduce in an independent
language and arithmetic implementation. The production program is
deterministic and optimization-safe. The paper follows from the finite
witnesses and stays below their physical ceiling.

The independently supported boundary is:

$$
\boxed{
\begin{aligned}
&\text{supplied ordered laws determine a relative RN field;}\\
&\text{supplied mode/evidence determine conditional numerical weights;}\\
&\text{none of these supplies the next physical record-birth law.}
\end{aligned}
}
$$

**Round-2 independent-rebuild verdict: PASS.**

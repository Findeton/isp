# D5 hostile review, round 2: independent rebuild and reproducibility

**Referee:** independent hostile rebuild

**Date:** 2026-07-11

**Verdict:** **PASS at the stated supplied-factor-partition scope**

All round-1 executable defects are repaired. A clean-room implementation
reproduces every original and new finite cell: strict table kinds, negative
refusal, explicit rational weak distributions, both chain
parenthesizations, schedule validation, branching contraction, exactly-once
separator ownership, nested reuse refusal, scope ontology, canonical ray
growth, compatible and incompatible structural-zero controls, projective
towers, and scope/value nonselection.

The revised manuscript also narrows its nouns correctly. It proves exact
composition for a **supplied complete finite factor partition with supplied
unique-ID ownership**. It does not claim a physical construction-order gauge,
distributed boundary implementation, complete support calculus, candidate
proposal measure, seal law, or derived factor scope/value.

No independent-rebuild blocker remains.

## 1. Frozen snapshot and reproducibility

```text
883f27535ab82e60a49f896b82a3910113291661f1706b5fe1bde652ba48f147  v10/note-d5-typed-collar-message-algebra.md
efbe43a452784ccf8e78db6404826adcfe1d554cc5dfe875689b2a1cf7340c85  v10/code/d5_typed_collar_exact.py
f2d31845a97379f36f8c01acc065d36a73c1336d7843954a06cb6658e7626005  v10/relativistic-isp-v10-paper6-typed-collar-composition.md
```

Production command:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 v10/code/d5_typed_collar_exact.py
```

Two sequential executions exited zero and produced byte-identical stdout:

```text
e7e8e345314e852552c63bc61a8fbecfb5f2af3d85140507dd22db42277118a8
```

The executable reports **34/34 exact checks passed** and internal payload
digest:

```text
6de789f77c7b77d2cfb55ae0d21c42b4f7a3650fe28a56d99222e72ec502f83a
```

The final sequential self-containment audit reports 4/4:

```text
PASS: all v10 investigation executables reside in v10/code
PASS: no duplicate investigation source exists outside v10/code
PASS: every investigation executable imports only the Python standard library
PASS: no .pyc cache artifact exists under v10
```

## 2. Independent reconstruction

The round-1 Ruby implementation was extended rather than replaced with calls
to production. It uses semantic assignment hashes, independent exact
`Rational` elimination/rank routines, and a separate table-kind validator. It
imports no production source. Its SHA-256 is:

```text
70ebf1956a385b61f3db676b629a833eedfc1065a8339de1a172b5f3eaf8263e
```

Independent output relevant to the repaired gates:

```text
R ranks=[1,3,7] duplicate=2 original/swap/single=2/2/1
R product trace endpoints=(1,3/4),(6,9/2)
R explicit weak TV=true chi-square=true terminal TV=1/514
R weak upper partial 16=1431655765/17179869184 < 1/12
C chain=[29,25,31,35]
C direct/reverse/left/right/relabel=true
C branch direct=nested=true entries=16 endpoints=319/319
C ownership direct=left=right=true values=[15,12,13,20]
C nested reuse refused=true duplicate factor refused=true
C loop=[20,6,6,20] one-site product=[1/4,1/4,1/4,1/4]
S messages=[2,4],[2,4],[4,2]
S predictions=[5/12,7/12],[5/12,7/12],[7/12,5/12]
B components base/local/joined=2/2/1; subsets local/spanning=6/9
B scope dummy=[A2]; separable essential=[A2,B2], irreducible=false
B irreducible pair=true; ancestry message=[10,6,6,10], direct AB=false
K width-eight table=256/255; distinct width-one rays=32
K recurrence=true primitive bits=2->45 normalized bits=3->46
K primitive/normalized bit sequences strictly increase=true
K projective Bernoulli towers=true
Z negative refused=true positive-zero refused=true support accepted=true
Z equality message=[1,0,0,1]; incompatible message=[0,0,0,0]
Z all-zero normalization refused=true
L candidates=[2/5,3/5],[4/9,5/9]
L invariant scope families=4, nonempty=3
```

Every finite comparison uses integers or exact rationals.

## 3. Table kinds and probability boundary — repaired and passed

Production now distinguishes four kinds:

1. strictly positive primitive factor;
2. nonnegative support-control factor with nonempty support;
3. nonnegative derived message; and
4. the provenance-free scalar identity one.

The constructor enforces:

- unique variables and exact table size;
- no negative entry for any kind;
- nonempty primitive scope;
- exactly one supplied provenance ID for a primitive token;
- strict positivity for positive factors;
- at least one positive entry for support factors; and
- the exact empty-scope/value/provenance triple for identity.

Multiplication and marginalization return derived messages. The final
hardening also makes `effective_message` return kind `message` even when a
region contains one primitive token and requires no elimination, so a
primitive token cannot masquerade as a derived separator message.

The clean-room kind validator independently refuses:

- message values `(-1,2)`;
- a positive factor containing zero;
- empty primitive scopes or invalid identity data;

while accepting a typed nonnegative support table `(0,1)` and the exact
identity. The round-1 negative-probability blocker is closed.

## 4. State ordering, keys, and elimination schedules — pass

Binary table order remains lexicographic with `-1` as bit zero and `+1` as bit
one. Clean-room lookup is semantic by variable assignment; conversion to raw
arrays occurs only for reporting. It reproduces:

```text
(A,B)=(-,-),(-,+),(+,-),(+,+)
chain message = (29,25,31,35)
loop message  = (20,6,6,20)
zero message  = (1,0,0,1).
```

Variable names and ordered scope remain explicit, and reorder reconstructs
the semantic table. Joint variable/factor relabeling preserves the physical
message. No state-key or scope-order collision was found.

The elimination validator now requires the schedule to have the same length,
unique entries, and exactly the interior-variable set. A duplicate schedule
is refused rather than treated as a harmless repeated no-op.

## 5. Channel rank and weak distributions — repaired and passed

The independent covariance reconstruction reproduces:

- complete parity ranks `1,3,7`;
- duplicated ledger `(1,2,1)` rank two;
- original and whole-model-swapped two-channel ledgers rank two;
- a single coordinate rank one;
- a single collective parity channel rank one through arity ten; and
- independent `P(+)=3/4` coordinate rank `n`, trace `3n/4` through six.

The revised language correctly calls these screen-relative covariance/Gram
ranks, with a Fisher interpretation only after choosing the corresponding
exponential family and natural parameters.

Production now builds the weak binary distributions explicitly. Clean-room
TV and chi-square calculations reproduce:

$$
\operatorname{TV}(P_m,U)=\frac1{2(2m+1)},
$$

ending at `1/514`, and

$$
\chi^2(P_i\Vert U)=4\delta_i^2,
\qquad \delta_i=2^{-(i+3)}.
$$

The finite partial sums increase and remain below `1/12`; the all-width bound
is the analytic geometric sum. The verdict is now explicitly
`BOUNDED-KL-NO-RANK/ARITY-BOUND`, not a claim about identity metadata, scope
description, exact rational encoding, or every possible content functional.

## 6. Chain associativity, branching, and schedule invariance — pass

Independent direct elimination, both nested parenthesizations, and reverse
schedule all give:

$$
(29,25,31,35).
$$

The missing right-associated production cell is present and passes.

The registered branching tree contains six factors with interior
`R,H,K` and boundary `A,B,C,D`. Clean-room direct elimination and leaf-to-root
contraction agree on all 16 boundary entries; the first and last are both
`319`. This closes the missing branching adversarial cell.

The paper correctly calls the equality elimination-schedule invariance for
one fixed identified factor multiset. It no longer promotes it to physical
construction-order gauge between different record-birth histories.

## 7. Exactly-once ownership and provenance — passed at supplied scope

For the unary separator factor and two adjacent edges, clean-room contraction
gives:

$$
(15,12,13,20)
$$

whether the separator token is assigned directly, owned by the left region,
or owned by the right region—provided it appears exactly once. A derived left
message retains the separator token's ID, so multiplying the primitive token
again is refused. Literal duplicate identity after relabeling is also refused.

This proves assignment independence under a supplied factor partition and
opaque unique IDs. It does not solve semantic duplication under fresh IDs,
discover a complete factor registry, or derive physical ownership. Those
limits are stated explicitly and are not blockers to the conditional theorem.

The multiplication helper retains an internal `reject_duplicate` override,
but all public receipt paths and composition helpers use the refusing default.
Exactly-once ownership remains a theorem premise, not an unbypassable physical
security boundary.

## 8. Loop and predictive sufficiency — pass

The exact loop message normalizes to

$$
(5/13,3/26,3/26,5/13),
$$

whereas the product of its uniform one-site marginals is uniform on four
states. The manuscript infers only that one-site products can be insufficient,
not a universal exponential lower bound.

The two histories with message `(2,4)` predict `(5/12,7/12)` against the same
proposal factors; `(4,2)` predicts `(7/12,5/12)` and an unmarked boundary
predicts `(1/2,1/2)`. Scaling `(2,4)` to `(1,2)` changes no prediction.

The universal positive-ray theorem is independently sound under the paper's
stated test class: arbitrary strictly positive full-separator proposal
factors. The paper now calls this a factorization-relative universal
diagnostic ray and does not claim it is minimal for an unknown restricted
physical proposal class.

## 9. Component and scope ontology — repaired and passed

The clean-room hypergraph reproduces:

```text
base components                  2
after one-component proposal     2
after explicit Z-A and Z-C legs  1
one-component parent subsets     6
cross-component subsets          9
connected sparse growth          1 component.
```

Shared ancestry creates `(10,6,6,10)` without primitive `A-B` factor
incidence.

The new scope controls distinguish:

- a listed two-variable dummy scope with essential set `{A2}`;
- a table essential in `{A2,B2}` but exactly separable into unary factors;
- a primitive irreducible pair interaction; and
- a derived correlated two-variable message whose primitive inputs contain no
  `A-B` hyperedge.

Thus listed scope, essential dependence, irreducible statistical interaction,
primitive factor incidence, derived correlation, and directed transport are
not conflated. Directed physical carrier/transport remains absent by claim.

The connected result is correctly renamed
`CONNECTED-DOMAIN-CLOSURE-GIVEN-SEED`: the proposal domain and seed are
supplied; neither is selected by composition.

## 10. Canonical separator-state growth — repaired and passed

The width-one recurrence is

$$
(a_{n+1},b_{n+1})=(a_n+b_n,a_n+2b_n),
\qquad(a_0,b_0)=(1,1).
$$

Clean-room reconstruction verifies it at every one of 32 steps and confirms
`gcd(a_n,b_n)=1`. The primitive integer rays are all distinct, and their
maximum bit length grows strictly from `2` to `45`. After normalization, the
maximum numerator/denominator bit length grows strictly from `3` to `46`.
The final primitive pair is:

$$
(17167680177565,27777890035288).
$$

The paper supplies the all-depth proof: the recurrence preserves gcd one and
`b_n` increases without bound. It correctly describes table-coordinate growth,
not an optimal algorithmic encoding lower bound or physical information
capacity. The verdict is correspondingly renamed
`EXACT-SEPARATOR-STATE-GROWTH`; no distributed carrier construction is
claimed.

## 11. Structural-zero and support controls — repaired and passed

The typed equality-support chain composes to `(1,0,0,1)` and normalizes to
`(1/2,0,0,1/2)`. The entries are nonnegative, the primitive support tokens
have nonempty support, and the derived message has positive total.

An explicit negative table is rejected at construction. An all-zero derived
message refuses normalization. Multiplying equality and inequality support
tokens yields exactly `(0,0,0,0)` and the impossible result is refused.

These are sound controls. The paper expressly leaves a general fiberwise
support/conditional-version calculus open.

## 12. Projective towers and nonselection — pass

The `p=2/3` and `p=3/4` Bernoulli families marginalize exactly through width
eight and differ already at width one. Their product formulas extend
analytically to every finite width. The manuscript concludes only that finite
projective compatibility hosts multiple laws; it does not derive factor
values, provenance towers, physical update, or an infinite sealed-record
encoder.

Against one common message, positive proposal factors `(4,1)` and `(2,1)`
give `(2/5,3/5)` and `(4/9,5/9)`. The frozen symmetric scope arena contains
four swap-invariant families, three nonempty. Composition and covariance
therefore select neither value nor one unique eligibility family.

## 13. Claim ceiling — pass

The revised verdict is supported exactly as written:

```text
CONDITIONAL-FACTOR-PARTITION-COMPOSITION
+ EXACT-SEPARATOR-STATE-GROWTH
+ CONNECTED-DOMAIN-CLOSURE-GIVEN-SEED
+ BOUNDED-KL-NO-RANK/ARITY-BOUND
+ SCOPE/VALUE-NONSELECTION
```

Still-supplied data are named: complete factor cover, unique-ID ownership,
factor scopes and values, candidate proposal measure, evidence/seal/no-birth
rule, and first cross-component token. No physical interface, distributed
bounded-capacity encoding, universal support theory, final interacting click
law, geometry, cone, dimension, limiting speed, horizon, or quantum result is
inferred.

## 14. Final determination

The repaired production source enforces its probability/type arena, every new
finite control reproduces independently, state ordering and key identity are
sound, stdout is byte-deterministic, and the final self-containment audit
passes 4/4.

The remaining limitations are scientific inputs explicitly outside the
conditional factor-partition theorem, not hidden implementation failures.

**Round-2 independent-rebuild verdict: PASS.**

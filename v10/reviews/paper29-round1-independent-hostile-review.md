# Paper 29 round-one independent hostile review

**Verdict:** `0 BLOCKERS / 1 MAJOR / 3 MINOR / 1 NIT`; promotion withheld.  
**Frozen authorship commit:** `e14bf4f4de18ac4fac29c990679068984acfa63b`.  
**Paper SHA-256:**
`b00ae422aa0ff39715fa7c65e03dcfc7e3fdd0ca971fad3a5194cae35344afce`.  
**Date:** 2026-07-15.

The paper's central result survives: the action ladder is correctly typed,
the two D38b probability spaces are kept separate, and Paper 28's flat-action
nonmembership is not confused with probability inconsistency.  One theorem
hypothesis is nevertheless missing from the printed statement, and three
scope clarifications are required before promotion.

## 1. Independent mathematical checks

I re-derived the central numbers and identities:

```text
1/18 + 2/33 = 23/198;
1/32 + 1/48 = 5/96;
E = (+1/sqrt2,+1/sqrt2,+1/sqrt2,-1/sqrt2);
CHSH = 2sqrt2;
P(b=+|x=1,a=+,y=0/1) = 1/2 +/- sqrt2/4;
sqrt(1-9/25) = 4/5;
(4/5)^3 = 64/125.
```

The D40/D40b/D40c receipts support every headline census: 1,024 positive
classical cylinder controls, 28-to-17 star pushforward, 44-to-40 global
pushforward with four merges, 320 Bell quadratic-form controls, twelve
transitive locks and seven typed levels.  The fixed-depth and no-new-data
qualifiers are present.

## 2. MAJOR — Theorem 1 omits two positive denominators

Theorem 1 assumes only `mu([H])>0`, then divides by `mu([Ha])` and
`mu([Hb])`.  A nonnegative measure can give either intermediate cylinder zero.
The proof's sentence “Positivity makes every displayed conditional
well-defined” is therefore false as printed.

The receipt itself is stronger than the paper: R1 uses strictly positive atom
weights, and R3 explicitly gates sixteen positive queried denominators.  The
repair is authorship-only but load-bearing:

```text
mu([H])>0,
mu([Ha])>0,
mu([Hb])>0,
[Hab]=[Hba].
```

Alternatively, the theorem could state an undivided chain-rule identity and
define conditionals only on positive rows.  The paper should use the explicit
three-denominator hypothesis because that is what the receipt carries.  The
abstract and five-item load-bearing list should say “all displayed
conditioning cylinders are positive,” not a singular denominator.

## 3. MINOR — Theorem 4 switches between a tree and reconvergent paths

Section 7 starts with a completion tree, where a node has one path from the
root, then claims that two paths to the same refined prefix telescope equally
and cites D39's commuting squares.  The intended theorem is correct on either
of two precise objects:

1. the path-unrolled completion tree, where path identity is retained; or
2. a finite acyclic directed multigraph with a positive harmonic state
   potential

```text
h(x) = sum_{e:x->y} h(y),
K(e|x)=h(y)/h(x),
```

where outgoing edge multiplicity is counted.

Use the second formulation for the square theorem, then explain that terminal
weights define `h` by summing weighted continuation paths.  Products along
any two paths with the same endpoints telescope to `h(y)/h(x)`.  This removes
the tree/reconvergence ambiguity and exactly matches D39's recurrence.

## 4. MINOR — Theorem 5 must remain an absence-of-construction result

The title correctly says “does not yet imply,” and the proof ultimately says
no corpus theorem constructs the map.  The first sentence, however, says the
D15 action “does not uniquely determine” an instrument or grammar.  D34c's
toy instrument pair proves generic action-to-record nonselection, not two
fully specified D15 instruments.

Retitle the result **“record-closure of the identified action is not
established”** and phrase its theorem as a current-corpus nonconstruction:
the required state/instrument/grammar data remain supplied, and no comparison
map has been built.  Keep actual D15 nonuniqueness open unless two D15-level
completions are constructed.

## 5. MINOR — quotient additivity requires a declared quotient map

The type ledger currently makes “sum of serial preimage masses” look like an
intrinsic law of every `CAUSAL_DAG_ATOM`.  It is the law only after a measurable
quotient `q` has been declared.  The body later states this correctly with
“If `q` forgets construction order.”

Repair the ledger row and Theorem 3 wording to say “under the declared
star/global quotient.”  For the complete global fixture, record IDs and parent
references ground the quotient physically.  For the star fixture, the
unordered-action map is a registered mathematical projection; do not promote
it to a derived physical gauge.

## 6. NIT — no-signalling count label

“Sixteen no-signalling marginals” can read as sixteen independent equations.
The executable counts sixteen registered marginal checks, with repetitions
across setting pairs.  Use that exact label.

## 7. Surviving paper surface

The following need no scientific change:

- the operator/functional/record/boundary type ladder;
- finite fibre sufficiency;
- D34c interference versus path-record control;
- separate `23/198` and `5/96` pushforwards;
- Paper 28 nonmembership without stochastic inconsistency;
- K-flat as a general positive h-ratio rather than a Born fingerprint;
- exact Bell correlators, no-signalling, click cocycles and boundary negative;
- the correction that joins are not necessary for entanglement and D23 is an
  identifiability ceiling;
- the eight-slot D15 dictionary audit;
- the row-by-row claim ledger;
- record-native versus SI-clock scale;
- the conditional D26 BORN/TOKEN laboratory handoff;
- the generated quantum content bridge as the next constructive object.

All findings are theorem wording or scope repairs.  No receipt number changes.
Independent closing paper review is required after authorship repair.


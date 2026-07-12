# D4 hostile review, round 1: independent rebuild and reproducibility

**Referee:** independent hostile rebuild

**Date:** 2026-07-11

**Verdict:** **MAJOR REVISION of the receipt and message census, with the core collapse theorem independently confirmed**

The principal mathematics survives. An independent implementation reproduces
the finite-poset census, exact linear ranks, positivity consequences,
global-shock naturality, completion messages, law-relative witness, and
chain-capacity lower bound. The proof that all-subset unmarked naturality
leaves only the empty/full mixture is correct and genuinely uses positivity.

The production receipt nevertheless overgrades four controls. Its proper-
ideal “certificate” checks a condition already guaranteed by the definition
of ideal without executable linkage to the previously certified zero pair
marginals. Its completion-message equality computes both sides from the same
weight and projection helpers. Its capacity checks insert `n/(n+1)` instead
of recovering it from chain down-sets, and the purported provenance flag is
never represented. Its profinite convergence check is an eight-step finite
diagonal plus a nonzero rational, not a convergence test.

More importantly, the reported `756` predictive classes and maximum `66`
messages for one retained structure are presentation-dependent. The receipt
keys retained structures by raw labeled relation strings and never quotients
the probability vector together with the poset under relabeling. An
independent canonical orbit pushforward gives **199** physical predictive
classes and a maximum of **42** for one unlabeled retained structure. The
`756/66` values may remain as explicitly labeled-cover diagnostics, but they
cannot be advertised as unmarked physical class counts.

These defects do not refute
`UNMARKED-GLOBAL-COLLAPSE + LAW-RELATIVE-UNBOUNDED-DETERMINISTIC-MESSAGE`.
They require a repaired, less coupled receipt and corrected finite quotient
statistics before acceptance.

## 1. Frozen snapshot and deterministic execution

```text
ff785c56b8c95dd9843e77b548951aedc9f8496f7938272de2ac73006ac8fdf9  v10/note-d4-no-silent-boundary-sufficiency.md
7c87e81f333d75814ec508023c7a21a01b0a25142415819288da3aaac1137481  v10/code/d4_boundary_sufficiency_exact.py
5dde07f57a6b8098d6f464ee686457981448e0d0dd26f3c31ccaac770b181c6b  v10/relativistic-isp-v10-paper5-restriction-naturality-global-shock.md
```

Production command:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 v10/code/d4_boundary_sufficiency_exact.py
```

Two executions exited zero and produced byte-identical stdout:

```text
3a7ee070b7fc6a359cd33512cda4329055b4aaeab8ec2343121db2c4dcc7af8d
```

The receipt reports **17/17 exact checks passed**. The separate v10
self-containment audit reports 4/4: production investigation sources are
under `v10/code`, no duplicate investigation source exists outside that
directory, imports are standard-library only, and no cache artifact exists
under `v10`.

## 2. Independent implementation

I wrote a separate Ruby implementation using integer adjacency bitsets and
`Rational` sparse elimination. It imports no production module and does not
call a production helper. Its final SHA-256 is:

```text
e339d590f704ba0e320d118597cfea849f090a66e15a9b3142c9ba9b29d758b4
```

It independently implements:

1. enumeration of every labeled strict order through four vertices;
2. down-set enumeration, induced orders, subset projection, and relabeling;
3. construction of all normalization, covariance, and restriction equations;
4. exact sparse rank of the coefficient and augmented systems;
5. the empty/full solution line and the three base positivity consequences;
6. the arbitrary-proper-ideal pair certificate through four vertices;
7. global-shock restriction pushforwards;
8. D3 raw weights and normalized completion messages;
9. canonical joint orbits of retained posets and probability vectors;
10. actual prefix ideals of chains through depth 64; and
11. residue and factorial-sequence controls.

Independent output:

```text
POSETS [1, 1, 3, 19, 219]
LINEAR variables=111 equations=1087 rank=108 augmented=108 affine=3
LINEAR shock_line=true
PROOF base_ideal_counts=[2, 3, 5, 4]
PROOF affine_consequences chain=true vee=true,true
PROOF proper_ideals=1304/1304
SHOCK natural=true cuts=3671
MESSAGE exact=true contexts=7342 classes=756 max_per_structure=66
MESSAGE physical_classes=199 physical_max_per_structure=42
MESSAGE quotient_duplicate_labeled_keys=2
MESSAGE witness=1/2,9/14
CAPACITY states=64 bits=6 first=1/2 last=64/65
CAPACITY flag_collision=true values=2/3,3/4
PROFINITE residue=true factorial_diagonal=true f8=40320/40321
```

Every theorem-critical finite computation uses integers or exact rationals.

## 3. Posets, down-sets, and state identity — pass

The independent directed-relation census reproduces the labeled-poset counts

$$
1,1,3,19,219
$$

through four vertices. It filters all directed-pair bitsets by irreflexivity,
antisymmetry, and transitivity rather than using the production relation
objects.

Down-set counts for the structural proof cells reproduce exactly:

```text
point / two-chain / V / two-antichain = 2 / 3 / 5 / 4.
```

No state-size collision was found. Production linear variables use
`(n, relation, ideal)`, so the empty relation at different cardinalities is
not conflated. The labeled message-class key likewise includes retained
cardinality. The problem found below is not a cross-size collision; it is the
opposite problem—failure to identify different labeled presentations of the
same physical unmarked state.

## 4. Exact linear classification — pass, including the failed preregistered expectation

Independent construction gives:

```text
variables = 111
equations = 1087
coefficient rank = 108
augmented rank = 108
signed affine dimension = 3
```

Thus the signed rational system is consistent but is not the affine line
predicted in the preregistration. The note and paper disclose this failure
instead of silently changing the target. That is correct protocol.

The three tested empty/full mixtures `p=0,1,2/5` satisfy every equation
independently. More importantly, the full formula

$$
q_P(\varnothing)=1-p,qquad q_P(P)=p
$$

obviously supplies one affine direction for arbitrary `p`; the remaining two
signed directions must be removed by positivity rather than by equality rank.

## 5. Positivity proof — theorem passes; production proper-ideal gate is overgraded

Independent row-span checks reproduce the load-bearing affine consequences:

- the proper singleton ideal of the two-chain has mass zero;
- in the three-point `V`, `q_a+q_{ab}=0`; and
- in the same `V`, `q_b+q_{ab}=0`.

For nonnegative probabilities, the last two equations kill all three terms.
Restriction to the lower antichain therefore kills both antichain singleton
masses. This is the correct place where the positive cone removes the two
extra signed directions.

The all-size proof is also sound. For any proper nonempty ideal `D`, choose
`x in D` and `y outside D`. Downward closure forbids `y<x`; hence the induced
pair is either a chain with `x` as its forbidden bottom singleton or an
antichain with a forbidden singleton. The zero pair marginal is a sum of
nonnegative full-poset masses containing `q_P(D)`, so `q_P(D)=0`.

Production check 06 does not execute that whole certificate. Its condition

```python
if (y, x) not in relation:
    certified = True
```

is automatically true for every chosen inside/outside pair because `D` is
already known to be a down-set. It does not record whether the pair is a
chain or antichain, map the projected singleton to the corresponding base
zero marginal, or verify that `D` occurs in that pushforward fiber. The count
`1304/1304` therefore certifies down-set closure again, not the stated
zero-marginal implication.

The independent reconstruction verifies all 1,304 cases with the full pair
classification, and the paper proof is sufficient mathematically. The
production gate should nevertheless be repaired so its label matches its
work.

## 6. Global-shock naturality — pass

For `p=2/5`, independent pushforward of the empty and full ideals passes all
3,671 labeled parent/cut cases through four vertices. On an empty retained
set, the two masses correctly merge to one; otherwise they remain the empty
and full retained ideals with masses `1-p` and `p`.

The infinite theorem does not depend on extrapolating these 3,671 cases. The
paper's pair argument proves that every proper ideal has zero mass at every
finite size, and direct restriction of the empty/full mixture proves
naturality for arbitrary size. The cutoff is presented as an audit, not as
the source of the all-size quantifier.

The survivor is correctly described as global rather than local: on its full
branch the new event contains every old event in its past. The parameter `p`
remains free.

## 7. Completion-message sufficiency — value passes; control is coupled

Independent reconstruction reproduces all 7,342 labeled
parent/cut/law contexts for the two D3 laws. Direct normalization of every
full ideal followed by projection agrees exactly with normalization of the
completion sums. The three-antichain/one-point witness is:

$$
P_{b=1}(\text{included})=\frac12,
\qquad
P_{b=2}(\text{included})=\frac9{14}.
$$

The second value follows from total weight `14` and included weight `9`:
one included singleton contributes `1`, two included pairs contribute `4`,
and the triple contributes `4`.

Production check 09 is algebraically coupled. `direct_pushforward` and
`completion_message` call the same `downsets`, `project_mask`, and
`registered_weight` helpers. Their only difference is whether normalization
occurs before or after grouping, so equality is distributivity of division by
one common total. That proposition is correct by definition, but the check
cannot expose a shared projection or weight bug.

**Required repair:** obtain one side from independently reconstructed full
kernel states or use a separately implemented grouping path. At minimum,
rename the gate as a definitional identity and rely on explicit numeric
witnesses for implementation coverage.

## 8. Major finding — message classes are not quotiented by relabeling

Production classifies a context with

```python
key = (len(keep), relation_code(len(keep), subrelation), message)
```

and classifies a retained structure with the first two entries. Raw relation
codes change under relabeling. The message's visible bitmasks also change
under the same relabeling. Consequently physically identical unmarked
poset/message pairs can be counted several times.

The independent control transported the retained relation and every visible
precursor probability together through all permutations, selected a
canonical joint representative, and then summed equality classes. It finds:

```text
labeled-cover classes                    756
canonical unmarked predictive classes   199

maximum labeled messages for one raw relation code  66
maximum physical messages for one unlabeled order   42
```

At least one physical class contains multiple production keys, so this is not
a merely hypothetical distinction.

The exact sufficiency and law-relativity results survive. The numerical class
statistics do not. The manuscript must either call `756/66` labeled-cover
diagnostics or replace them with a genuine canonical pushforward. Given v9's
construction-order gauge and D3's repaired orbit discipline, the physical
counts should be the canonical ones.

## 9. Fixed deterministic capacity — theorem passes; executable gates are formula-only

The lower-bound theorem is correct. The `n`-chain has exactly the prefix
ideals

$$
\varnothing,\{0\},\{0,1\},\ldots,\{0,\ldots,n-1\}.
$$

Under the uniform law, exactly `n` of the `n+1` ideals include the retained
minimal point, giving `n/(n+1)`. These rationals are strictly increasing, so
an exact deterministic sufficient mark through depth `N` needs at least `N`
states and `ceil(log2 N)` bits. The independent implementation explicitly
constructs the prefix ideals through depth 64 and obtains 64 states, six
bits, and endpoints `1/2` and `64/65`.

Production does not construct a chain or any ideal in checks 12–14. It sets

```python
chain_predictions = tuple(Fraction(n, n + 1) ...)
```

and checks that those inserted fractions are distinct. Check 14 merely tests
`2/3 != 3/4`; no flag or context is represented. This is a proof illustration,
not an independent receipt for the chain law.

There is also a naming problem. When the retained record is the minimal point
of a chain, the discarded chain vertices lie above it, so they are not
external parents of that retained record. If `external-parent-present` is
intended to refer to the candidate new event, its truth varies across the
precursor completions being averaged and is not one constant context flag.
A valid constant coarse control would be `discarded-chain-context-present`,
or the manuscript must define precisely which carrier owns the flag.

**Required repair:** derive the 64 predictions from explicitly generated
chain ideals, and replace the unmodeled provenance assertion with an actual
defined mark collision.

## 10. Profinite controls — mathematical argument passes; executable convergence label does not

The residue obstruction is elementary and correct. For any fixed `m>0`, the
depths `n` and `n+m` have the same residue but different predictions. The
production gate exhibits only `m=7`, `n=5,12`; it should be labeled an example
rather than a classification of all fixed residue stages.

The standard profinite-integer discontinuity argument is also correct when
stated as a theorem. For each fixed modulus `m`, `j!` is eventually zero
modulo `m`, so `j! -> 0` in the profinite integers. Meanwhile

$$
\frac{j!}{j!+1}\longrightarrow 1
$$

in the reals, whereas the depth-zero value is `0`. No continuous real-valued
extension on the standard profinite completion can agree with all finite
depth predictions.

Production check 16 establishes much less. It verifies divisibility only for
`2<=j<=8` and `m<=j`, then checks only that `40320/40321` is nonzero. It does
not test convergence to one, the value at zero, or continuity. No finite
executable can prove a topological limit by sampling, but it can exactly
verify the symbolic identities used in the proof and label the finite values
honestly.

The manuscript appropriately refuses a theorem against every compact mark
topology. Its one-point-compactification counterexample is enough to show why
the conclusion must remain specific to the standard profinite-integer
completion and fixed finite residue readouts.

## 11. Scope audit — pass

The manuscript correctly states the load-bearing qualifications:

- all-subset unmarked autonomy is an imposed axiom, not a consequence of
  Barandes ISP;
- positivity, not equality rank alone, produces the probability collapse;
- completion messages summarize a supplied law and do not derive it;
- the capacity theorem concerns deterministic, exact, uniformly bounded
  alphabets;
- stochastic marks, expanding boundaries, unbounded integer/rational marks,
  approximation, and specially factorized laws remain open;
- a full inverse-limit point is not one finite record readout;
- the global-shock survivor is not a local interaction law; and
- no cone, dimension, continuum, quantum, or absolute-scale result follows.

No cutoff overclaim was found in the all-size collapse or capacity theorem
prose because both are accompanied by elementary all-size proofs. The
overclaims are confined to executable gate labels and the finite message
class statistics.

## 12. Required openings before round 2

1. **Canonical message quotient.** Canonicalize the retained poset and its
   probability vector jointly under every relabeling. Reconcile the
   independently obtained `199` physical classes and maximum `42` with the
   current `756/66` labeled counts.
2. **Executable proper-ideal certificate.** For every proper ideal, identify
   an inside/outside pair, classify its induced order, map the projected
   singleton to the already certified chain or antichain zero marginal, and
   verify membership in the pushforward fiber.
3. **Decouple completion sufficiency.** Reconstruct the direct full kernel and
   projected child probabilities independently of the completion-message
   helper, or explicitly downgrade the gate to a definitional check.
4. **Build the chain controls.** Generate the actual prefix ideals through 64
   depths and recover the messages rather than inserting `n/(n+1)`.
5. **Define the coarse mark.** Replace the uninstantiated
   `external-parent-present` phrase with a typed, executable context mark and
   exhibit the exact collision.
6. **Repair profinite gate labels.** Separate the finite residue/factorial
   examples from the all-modulus and convergence proofs. Execute exact
   symbolic identities where useful; do not label eight samples a convergence
   test.

## 13. Final determination

The independently supported core is:

$$
\boxed{
\text{all-subset unmarked naturality + positivity}
\Longrightarrow
(1-p)\delta_\varnothing+p\delta_P.
}
$$

For the two registered D3 controls, exact completion messages are
law-relative and require arbitrarily many deterministic states along growing
chains. Neither route selects a bounded record-local interaction law.

The paper's central verdict therefore survives. The current receipt and the
`756/66` physical reading do not yet survive hostile review.

**Round-1 independent-rebuild verdict: MAJOR REVISION.**

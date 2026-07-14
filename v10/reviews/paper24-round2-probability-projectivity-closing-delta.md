# Paper 24 round 2 — probability/projectivity closing delta

**Frozen target:** commit
`63ea1863bde134923bb04a5644ae4f10024e9012`
**Comparison:** Paper 24 round-1 probability/mathematics review at frozen
commit `a680c06749c2c25bbd6ce28098c4afdae6c1e51a`
**Lane:** degree-dependent probability, exact Q1/Q2 laws, generic reach
conditional, cylinders/projectivity, Ionescu--Tulcea completion and the
proposed regional kernel-composition/finite-cover architecture
**Verdict:** **PASS — ALL ROUND-1 PROBABILITY/MATHEMATICS FINDINGS ARE
CLOSED, THE EXACT ROOTED HISTORY LAW IS UNCHANGED, AND NO NEW OPENING WAS
FOUND.**

**Count:** **0 blockers / 0 majors / 0 minors / 0 nits.**

The repair is terminal in this lane.  Paper 24 now distinguishes three things
that its first draft had conflated:

1. the exact, already executable D35 rooted law;
2. a finite realized call/stopping region, which is not claimed to be a
   minimal predictive state; and
3. a proposed regional specification architecture whose spaces, embeddings,
   conditional composition, coherent finite-cover extensions and global
   completion remain future work.

No code-level D35 theorem has been changed.  The paper's probability formulas
now describe the law the code actually executes.

## 1. Fresh reproduction and hygiene

The frozen hashes are:

```text
paper
83096d5285b81b9a8374509380516e61941c887357efb7fbba1624e28b7f5809

terminal D35d source
9ef590992e04beec0672a3772d41e1e01cde8315b65b7cd0aaa207a649c56e28

committed D35d stdout
2150ddecfe92d3d0f2db6505a3e3ccc1c5c8685a4a2ea5a0497280939a023574

terminal note
8a01ee2b766b483e94b5c15aadc8df0a381472e2221db11243564c5443858571
```

I ran:

```text
PYTHONHASHSEED=271828182 python3 v10/code/d35d_typed_identity_terminal_exact.py
PYTHONHASHSEED=161803398 python3 v10/code/d35d_typed_identity_terminal_exact.py
PYTHONHASHSEED=271828182 python3 v10/code/d35d_typed_identity_terminal_exact.py | shasum -a 256
git diff --check 63ea186^..63ea186 -- <changed D35/Paper-24 artifacts>
```

Both executable runs exited zero, were byte-identical to each other and
printed `PASS 18/18`.  The fresh stdout digest was exactly

```text
2150ddecfe92d3d0f2db6505a3e3ccc1c5c8685a4a2ea5a0497280939a023574.
```

The focused repair diff is whitespace-clean.  The unrelated trailing spaces
reported by a broader base-to-target `diff --check` occur in the frozen
round-1 review header, not in the repaired paper or D35 artifacts.

## 2. Corrected local menu and branch product — pass

Let `d` be the number of eligible child ports when an actor is queried.  The
revised section 4.4 now gives exactly the effective menu implemented by
`local_options`:

```text
p(idle)       = q_idle + 1[d=0] q_visit + 1[d<2] q_fork
p(birth)      = q_birth
p(visit j)    = q_visit/d                       for d >= 1
p(fork {j,k}) = q_fork/binomial(d,2)            for d >= 2.
```

The normalization check is all-size and has three cases:

```text
d=0:  p(idle)+p(birth)
    = q_idle+q_visit+q_fork+q_birth = 1;

d=1:  p(idle)+p(birth)+p(visit child)
    = q_idle+q_fork+q_birth+q_visit = 1;

d>=2: p(idle)+p(birth)
       + sum_j p(visit j) + sum_{j<k} p(fork {j,k})
    = q_idle+q_birth
       + d(q_visit/d)
       + binomial(d,2)(q_fork/binomial(d,2))
    = 1.
```

Unavailable alternatives are absent and their mass is folded into idle at the
menu stage; there is no later global renormalization.  Consequently the
completed marked call probability is correctly stated as

```text
P(D | H,A1) = product over queried actors v of p_v(o_v | local state at v).
```

Each queried actor makes exactly one marked local choice.  In the strict
ownership-tree grammar, incomparable subcalls use the same factor multiset in
every fair serializer, so reordering only permutes scalar factors and
commuting carrier maps.  This is the probability identity needed by the
scheduler theorem.  The repair does not extend that theorem to peer overlap,
cycles or shared-tip contention.

## 3. Q1/Q2 exact arithmetic — pass

The printed low-degree examples are correct:

```text
Q1 = (q_idle,q_birth,q_visit,q_fork) = (3/8,1/4,1/4,1/8)

leaf:       idle 3/4, birth 1/4
degree one: idle 1/2, birth 1/4, visit 1/4

Q2 = (2/5,1/5,3/10,1/10)

leaf:       idle 4/5, birth 1/5
degree one: idle 1/2, birth 1/5, visit 3/10.
```

At the initial degree-two root every action class is available.  Its aggregate
kind marginals therefore remain

```text
Q1: idle 3/8, birth 1/4, visit 1/4, fork 1/8
Q2: idle 2/5, birth 1/5, visit 3/10, fork 1/10.
```

The 16 support histories still decompose as

```text
root idle                                      1
root birth                                     1
root visit B                                   4
root visit C                                   2
root fork B,C                                  8
                                               --
                                               16.
```

D is queried in two visit-B histories and four fork histories.  Their exact
total weights are

```text
P(D reaches A2)
 = [q_visit(A)/2 + q_fork(A)] q_visit(B)

Q1 = [1/8+1/8](1/4)       = 1/16
Q2 = [3/20+1/10](3/10)    = 3/40.
```

Thus the six-versus-ten support count, `1/16`, `3/40`, and the distinct
Q1/Q2 birth/visit marginals all survive.  No receipt number needed revision.

## 4. Generic reach conditional and cemetery case — pass

The revised section 3.4 now explicitly assumes positive conditioning mass:

```text
mu([H0]) > 0.
```

It adjoins `A2=bottom` when A has no strict successor and declares reach false
there.  The displayed ratio is therefore well-defined:

```text
P(e reaches A2 | H0)
 = mu({H in [H0]: A2 != bottom and e enters A2 by a licensed path})
   / mu([H0]).
```

This closes both round-1 edge cases without silently conditioning on A2's
existence.  In D35 itself the cemetery outcome has probability zero because
each selected finite root call terminates and seals A2; retaining it in the
generic formula is nevertheless the correct wider convention.

## 5. Projectivity and completed rooted measure — pass

The finite exact witness remains:

```text
first physical atoms                           16
second-call refinements                       408
event/payload persistence checks              408
first-cylinder marginal mismatches              0.
```

For a first rooted state `s` and normalized second-call kernel `K_Q(s,dt)`,
the two-call law is

```text
P_2(ds,dt) = P_1(ds) K_Q(s,dt).
```

Hence forgetting the second call gives

```text
integral P_2(ds,dt) over t
 = P_1(ds) integral K_Q(s,dt)
 = P_1(ds).
```

The `16/408/408` gate checks this identity on every first atom, not merely in
aggregate.  The all-size extension has the premises the paper states:

1. strict child descent makes each call finite;
2. each reachable finite rooted state has a finite normalized next-call
   kernel;
3. from the fixed finite typed seed and fixed Q cell, the reachable-state
   union is countable and discrete; and
4. typed ordinal/path identities remain fresh at every finite stage.

Ionescu--Tulcea therefore supplies a measure on infinite sequences of
completed rooted-call states for each fixed Q cell.  Persistent finite
additions map such a sequence to the declared locally finite event DAG.  The
revised paper continues to call this an infinite **classical supplied-rooted
history measure**.  It does not promote it to a root-free measure, a quantum
history functional or the v9 profinite stem spectrum.

The Markov statement is equally scoped: the complete typed simulator state is
sufficient by construction; a bounded record projection may discard relevant
state and become non-Markov.  No claim that every observable process must be
non-Markov has appeared.

## 6. Regional kernel-composition and finite-cover architecture — pass as an explicit open target

Round 1 rejected the claim that the missing overlap object was already
precise.  The revision now calls it a **candidate architecture** and says that
it is not yet a defined SHARD object.  It names the missing data:

```text
oriented finite-region category and embeddings;
incoming, generated/upper and lateral interfaces;
boundary spaces B_D and regional history/output spaces Omega_D;
boundary extraction beta_D;
restriction/transport maps r_E,D;
normalized kernels gamma_D;
induced boundary transport kernels nu_E->D;
coherent joint extensions on every finite cover;
and a global completion theorem.
```

The proposed nested composition law is now correctly conditional rather than
a naive direct marginal identity:

```text
(r_E,D)_* gamma_E(. | b_E)
 = integral gamma_D(. | b_D) nu_E->D(db_D | b_E).
```

This formula is explicitly schematic pending domains, measurability and
orientation.  Read as a future requirement, it correctly says that the
smaller boundary may be random under the larger region and that the smaller
interior law conditioned on that boundary must be `gamma_D`.

The revision also incorporates the round-1 obstruction to pairwise overlap.
Its three-binary-variable example is correct: the three pair distributions
can each be uniform on unequal bit pairs and agree on every singleton
marginal, while no three-bit joint assignment makes every pair unequal.
Accordingly the paper now requires actual coherent joint extensions on every
finite cover, higher-overlap compatibility and positivity, followed by global
existence.  It does not claim that pairwise equality, finite-cover coherence
or the present D35 checks already prove that completion.

Finally, D35 is described only as a motivating laminar finite model.  The
paper expressly says it is not yet a proved special case of the regional
architecture because the region category, boundary extraction and embedding
have not been defined.  This is exactly the ceiling required by round 1.

No new regional-specification theorem is being claimed, so no theorem proof is
missing from the present paper.  The next investigation must supply these
objects before it can claim a root-free local law.

## 7. Disposition of every round-1 finding

```text
M1  false degree-independent diamond product
    CLOSED — replaced by the exact effective menu and local-option product.

M2a unsupported predictive-boundary inference
    CLOSED — finite realized stopping region only; full pre-call state remains.

M2b underspecified pairwise overlap rule
    CLOSED AS PAPER SCOPE — downgraded to an open architecture with conditional
    transport, coherent finite-cover coupling and completion obligations.

m1  zero cylinder mass / absent A2 not handled
    CLOSED — positive cylinder hypothesis plus cemetery A2=bottom.

m2  alpha/collision wording broader than the quotient theorem
    CLOSED — six-event supplied seed, reachable rooted grammar and registered
    cross-domain collision classes are now explicit; no general canonization.

m3  normalization incorrectly credited with termination/covariance
    CLOSED — menu normalization, strict-descent termination and commutation/
    authenticated-return covariance have separate premises.

n1  three four-entry zero verdicts called “nine zeroes”
    CLOSED — now described as three clean lane verdicts.
```

I also searched the repaired sections for a replacement overclaim—for example,
calling the regional architecture solved, calling the call boundary minimal,
identifying the rooted tower with v9, extending scheduler covariance to peer
overlap, or omitting fixed-Q/supplied-root scope.  None remains.

## 8. Final tally

```text
B  blockers  0
M  majors    0
m  minors    0
n  nits      0
```

**Final recommendation:** accept the round-1 probability/mathematics repair
and close this lane.  Paper 24 is mathematically honest at its declared
scope: an exact supplied A-rooted nested-call law and completed classical
rooted measure are proved; a root-free regional diamond specification is
identified only as the next unsolved architecture.

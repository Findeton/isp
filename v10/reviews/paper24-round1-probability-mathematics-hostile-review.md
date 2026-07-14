# Paper 24 round 1 — probability/mathematics hostile review

**Frozen target:** commit
`a680c06749c2c25bbd6ce28098c4afdae6c1e51a`  
**Manuscript:**
`relativistic-isp-v10-paper24-the-next-click-is-a-causal-diamond-not-a-clock-race.md`  
**Comparison base:** terminal D35 commit
`2a6d7d2`, terminal implementation commit `d414c56`, the frozen D35 note,
receipt and hostile reviews  
**Review lane:** exact probability, cylinders, projectivity, scheduler
covariance, Ionescu--Tulcea completion, Markov scope, typed alpha quotient,
causal-diamond specification and profinite scope  
**Verdict:** **MAJOR REPAIR — THE EXECUTABLE D35 RESULT SURVIVES, BUT THE
PAPER'S GENERAL BRANCH-WEIGHT FORMULA IS FALSE AND ITS CLAIMED PREDICTIVE
BOUNDARY/OVERLAP SPECIFICATION IS NOT YET MATHEMATICALLY DEFINED.**

**Count:** **0 blockers / 2 majors / 3 minors / 1 nit.**

The numerical receipt is sound.  I reproduced the terminal executable and
independently recomputed the 16 histories, the six D-reaching histories, both
reach probabilities, the root-kind marginals and the instrument dimensions.
The two majors are manuscript-level theorem/scope defects.  They do not reopen
the accepted terminal noun

```text
TIMELESS ROOTED NESTED-CALL FAMILY / EXECUTABLE.
```

They do prevent Paper 24 from being accepted as written.  In particular, the
paper's exact executable does **not** implement the displayed formula in
section 4.4: it implements a degree-dependent effective local menu in which
unavailable query mass is folded into idle.  Separately, D35 constructs a
finite realized stopping region while conditioning on the complete pre-call
typed state.  It does not prove that a smaller object called the “completed
call boundary” is a sufficient predictive state, and equality on pairwise
overlaps is not by itself an extension theorem.

## 1. Frozen-artifact reproduction

The frozen artifacts have SHA-256:

```text
paper
f2b4450410c6a8886b40955fb27e5aa3acbd75a13df16a9ebd38856faa1602bd

terminal source
9ef590992e04beec0672a3772d41e1e01cde8315b65b7cd0aaa207a649c56e28

committed stdout
2150ddecfe92d3d0f2db6505a3e3ccc1c5c8685a4a2ea5a0497280939a023574

internal science
79e29b8fd5f5a294b3c2faf438ffcca45434ec78af55b4150324b9939a03f26c
```

A fresh run with `PYTHONHASHSEED=314159265` exited zero and reproduced
`PASS 18/18` and the committed receipt.  `git diff --check
2a6d7d2..a680c06` is clean.

The manuscript accurately transcribes these terminal quantities for each Q
cell:

```text
FIFO/LIFO/canonical histories                  16 / 16 / 16
physical atoms                                           16
total probability                                           1
complete first/second/persistence                 16/408/408
ordinary renamed first/second/persistence          16/408/408
collision first/second/persistence                 16/408/408
late collision continuation                              6/6
common input / output dimensions                         8/48
cross Grams                                             10/10
D queried / unqueried histories                          6/10
return hops                                                18
grown scheduler checks                                     32
multi-call replay / root causal ordinal                    8/8
```

The review provenance sentence is also substantively right: there are four
D35 rounds and three clean terminal round-4 lane reviews.  Only the arithmetic
word “nine” at the end of the paper is wrong; see n1.

## 2. Independent finite probability reconstruction

### 2.1 Sixteen support histories

At the initial root, all actions are available.  The support count decomposes
without using the printed receipt:

```text
root idle                                      1
root birth                                     1
root visit B: B idle/birth, or B visits D
              and D idles/births               4
root visit C: C idle/birth                     2
root fork B,C: four B branches times two C      8
                                                --
                                                16
```

D is queried in two `visit B` histories and four `fork B,C` histories, hence
six queried and ten unqueried support histories.  These are support counts,
not equiprobable counts.

### 2.2 Root marginals and reach probability

Because the degree-two root has both visits and the unique fork available,
its kind marginal is the supplied Q cell itself:

```text
Q1: idle 3/8, birth 1/4, visit 1/4, fork 1/8
Q2: idle 2/5, birth 1/5, visit 3/10, fork 1/10.
```

The reach calculation in section 7.3 is exact.  D is reached through either
the root visit-B branch or the root fork branch, and B must then visit D:

```text
P(D reaches A2)
 = [q_visit(A)/2 + q_fork(A)] q_visit(B).

Q1: [1/8 + 1/8](1/4) = 1/16.
Q2: [3/20 + 1/10](3/10) = 3/40.
```

Thus the paper's `1/16` and `3/40` are right.  The fact that six support
histories realize the event in both cells does not make their probability the
same; the manuscript correctly keeps those statements separate.

### 2.3 Instrument arithmetic

The common-input arithmetic is also right.  Three input qubits give dimension
eight.  Birth adds one fresh qubit and therefore has a 16-dimensional output
sector; idle, two visits and fork each have an eight-dimensional sector:

```text
16 + 4(8) = 48.
```

Orthogonal classical sector injections make all ten unordered cross Grams
zero.  Since every branch map is an isometry and the five root-alternative
weights sum to one, the weighted self-Gram sum is `I_8`.  This proves the
declared classical-output instrument, not a coherent sum over support graphs;
the paper preserves that ceiling.

## 3. MAJOR M1 — the displayed completed-diamond probability is false

Sections 4.2 and 4.4 contradict one another.  Lines 263--265 correctly say
that unavailable visit or fork mass is assigned to idle.  Lines 288--300 then
define the unfurled four-vector `q` and claim

```text
P(D | H,A1)
 = product_v q(action at v) / number of selected v-local port sets.
```

That is not the law used by the terminal executable.  Let `d_v` be the number
of children owned by `v` at the start of its call.  The implemented local
option probabilities are

```text
p_v(idle)
 = q_idle + 1[d_v=0] q_visit + 1[d_v<2] q_fork;

p_v(birth) = q_birth;

p_v(visit j) = q_visit/d_v                         if d_v >= 1;

p_v(fork {j,k}) = q_fork/binomial(d_v,2)           if d_v >= 2.
```

Unavailable options are absent.  Therefore the exact branch law is

```text
P(D | H,A1) = product over queried actors v of p_v(o_v | local state at v).
```

The error is exposed already at one leaf.  In Q1 the executable leaf menu is

```text
p(idle) = 3/8 + 2/8 + 1/8 = 3/4,
p(birth) = 1/4.
```

The displayed formula instead assigns `3/8` and `1/4`, whose sum is `5/8`,
not one.  In Q2 the true leaf idle probability is
`4/10+3/10+1/10=4/5`, whereas the displayed formula gives `2/5`.
At a degree-one actor, fork mass alone is folded into idle; that case is also
misweighted by the displayed formula.

This is not a cosmetic notation issue.  Section 4.4 is titled “Exact local
probability,” and Theorem 2 appeals to its local factors.  The executable,
the root marginals and the reach probabilities remain correct because the
code uses `LocalOption.probability`, including the folded idle mass.

**Required repair:** replace the displayed law by the degree-dependent menu
above, call the denominator the number of **admissible target-port sets**
rather than “selected port sets,” and state Theorem 2 in terms of the resulting
`p_v` factors.  Add the Q1/Q2 leaf normalization as a receipt-level example.
No terminal code or headline reach number needs to change.

## 4. MAJOR M2 — a finite stopping diamond is not yet a predictive-boundary theorem, and the overlap rule is underspecified

### 4.1 D35 conditions on the complete state

Section 9.2 says the correct thing: given the **complete typed simulator
state** and fixed Q cell, the next rooted call is a Markov kernel.  Section 9.3
then says:

> The predictive boundary is therefore the completed call boundary for this
> conditional query.

The conclusion does not follow.  D35 proves that one realized root call has a
finite recursively generated interior and closes at A2.  Before that call is
sampled, its kernel is evaluated from the complete pre-call network state:
the ownership subtree, tips, ports, capabilities, evidence state and joint
carrier.  The “completed call boundary” contains returns and the upper seal
only after the outcome is known.  Conditioning on that post-call object is
not a proof that a smaller pre-call boundary statistic is sufficient, and no
minimality theorem was run.

The safe consequence relative to Paper 23 is narrower: D35 supplies a finite
causal **stopping region** for the selected A2 under a different, return-limited
law.  It does not establish a predictive quotient smaller than the complete
current D35 state.

### 4.2 `gamma_D` needs actual boundary and restriction maps

The abstract calls the missing object “now precise,” and section 11.3 writes

```text
gamma_D(interior marked history | boundary b)
```

followed by prose restriction and pairwise-overlap conditions.  This is a
good research direction, but it is not yet a mathematical specification.
At minimum the paper must define:

```text
Omega_D       the marked variable-support configuration space in D;
B_D           the admissible boundary-state space;
beta_D        the boundary-extraction map;
r_E,D         the restriction map for D subset E;
gamma_D       a measurable probability kernel B_D -> Prob(Omega_D).
```

For nested `D subset E`, the marginal of `gamma_E(.|b_E)` on D generally is
not one fixed `gamma_D(.|b_D)`: the smaller boundary `b_D` can itself be random
under the larger diamond.  The required identity must be a DLR/kernel
composition law, or explicitly a mixture over the boundary induced by E,
schematically

```text
(r_E,D)_* gamma_E(. | b_E)
 = integral gamma_D(. | b_D) nu_E->D(db_D | b_E),
```

with the compatibility conditions on `b_E`, `b_D` and the variable support
spelled out.

Nor does equality of two laws on their pairwise intersection guarantee a law
on their union.  A finite counterexample uses three binary variables.  Give
each pair a uniform law supported on unequal values.  All three pair laws have
the same uniform singleton marginals on overlaps, but no joint law exists
because three binary variables cannot be pairwise unequal.  Thus pairwise
overlap equality is necessary, not sufficient.  The target needs actual union
couplings/coherent finite-cover marginals, followed by a stated extension
theorem on the chosen measurable/projective spaces.  Listing “completion” as
an obligation does not supply those missing maps.

**Required repair:** replace the unsupported predictive-boundary sentence by:

> D35 provides a finite realized stopping diamond for this query.  Its
> pre-call law is presently conditioned on the complete typed rooted state;
> identifying a smaller sufficient boundary statistic remains open.

Then present the `gamma_D` paragraph explicitly as a proposed architecture,
define the spaces and maps above, require coherent union couplings rather than
pairwise overlap marginals alone, and reserve “solved laminar special case” for
the reachable D35 call kernels.  Do not say D35 proved a minimal/sufficient
boundary or a root-free overlap specification.

## 5. MINOR m1 — the general reach conditional needs an existence/support clause

Lines 190--191 define A2 inside a completed history, but section 3.1 also
allows terminal completed histories.  A terminal history need not contain a
successor of A1.  Lines 221--227 additionally divide by the H0 cylinder mass
without assuming that mass is positive.

The formula is valid for the D35 law because every root call closes and the
registered initial cylinder has positive mass.  As a statement for a general
completed-history law `mu`, it needs either

```text
mu([H0]) > 0
```

and conditioning on the event that A2 exists, or a specified regular
conditional probability.  If nonoccurrence is allowed, the paper must say
whether “e reaches A2” is false there or whether the probability is conditional
on A2's existence.

**Required repair:** add “for `mu([H0])>0` and with A2 defined (or conditional
on its existence)” before the ratio.  State the chosen nonoccurrence
convention.

## 6. MINOR m2 — alpha/collision language exceeds the declared quotient scope

Lines 532--536 say that ordinary actor/event alpha renaming and “all collision
cases” preserve the physical law.  The receipt proves complete ordinary
renaming for the declared six-event supplied seed presentation and tests three
registered display adversaries: immediate generated-event display, delayed
call-five event display, and future root-newborn actor display.  Disjoint typed
domains prove that supplied/generated storage identities cannot collide at
any reachable finite ordinal/path.  They do not constitute a general
canonicalization theorem for every root-free marked graph or every malformed
same-domain collision.

The terminal note states the correct ceiling explicitly: canonicalization is
for the declared finite supplied seed class, not a general graph-isomorphism
algorithm.

**Required repair:** replace “all collision cases” with “the registered
cross-domain display-collision classes,” state the six-event supplied-seed and
reachable rooted-grammar scope, and repeat that no general root-free graph
canonicalization has been proved.  The typed freshness and completed rooted
measure remain accepted.

## 7. MINOR m3 — normalization does not prove termination

The abstract says “Exact local normalization proves finite termination and
construction-order covariance.”  Normalization alone proves neither.
Termination follows from strict descent on a finite ownership tree plus the
rule that a newborn is not recursively queried in the call that creates it.
Scheduler covariance then uses termination, authenticated joins and
commutation of incomparable local factors/operations.

**Required repair:** attribute each result to its actual premise:

> Degree-dependent local menus normalize exactly; strict child descent proves
> finite termination; commutation and authenticated return slots prove
> construction-order covariance within the laminar grammar.

## 8. NIT n1 — three four-entry zero tallies are twelve, not nine

Lines 799--805 say “nine zeroes” and then print three instances of
`0B/0M/0m/0n`.  That is twelve category-zero entries, or more naturally three
clean four-category lane verdicts.

**Required repair:** write “three clean `0B/0M/0m/0n` lane verdicts” and avoid
counting the glyphs.

## 9. Claims that survive hostile review

The following probability/mathematics claims are supported once M1's formula
is repaired:

1. strict child descent makes each call finite on every finite supplied
   ownership tree;
2. every reachable finite rooted state has a finite normalized next-call
   kernel;
3. FIFO, LIFO and canonical service produce the same 16 physical first-call
   atoms, and the commutation proof extends this within the declared laminar
   grammar—not to overlapping peer calls;
4. all 16 first cylinders are exact marginals of 408 second-call refinements,
   with persistence;
5. for fixed Q and fixed supplied seed grammar, the reachable typed state
   space is countable and discrete, so Ionescu--Tulcea yields a measure on
   infinite sequences of completed rooted-call states;
6. persistent finite additions push this sequence to a causal-order locally
   finite event DAG at the declared rooted scope;
7. the full typed state is Markov by construction, while a bounded one-record
   projection may lose predictive information and become non-Markov; the paper
   correctly does not prove that every observable projection must be
   non-Markov;
8. the finite call-sequence cylinders are projective under forgetting later
   calls;
9. this classical rooted tower is related to but not identified with the v9
   profinite stem spectrum, and inverse limits do not select Q1 over Q2; and
10. neither the Ionescu--Tulcea completion nor typed alpha safety removes the
    supplied root, selects Q or g, solves overlap, supplies coherent
    variable-support amplitudes or identifies nature's law.

The completion theorem should continue to be phrased as an **infinite
classical rooted-history measure for each fixed Q cell and supplied grammar**.
It is not a root-free universe measure, a quantum history functional or the v9
profinite bridge.

## 10. Final tally and disposition

```text
B  blockers  0
M  majors    2
m  minors    3
n  nits      1
```

**Disposition:** return Paper 24 for one focused repair.  Correct the local
option law; withdraw the unproved predictive-boundary inference; define the
conditional restriction/overlap architecture with actual spaces, maps and
union couplings; add the small scope repairs above; and rerun a paper-level
delta.  The terminal D35 code, receipt, Q1/Q2 nonselection result, exact reach
experiment, rooted Markov completion and stated v9 ceiling do not need to be
reopened.

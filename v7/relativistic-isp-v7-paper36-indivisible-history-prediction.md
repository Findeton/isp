# Relativistic ISP v7 Paper XXXVI: Indivisible History Prediction and Effective Stochastic Residuals

**Status:** campaign note, not peer reviewed, version 2026-06-29.

This paper follows the opening from Paper XXXV:

> `Pr(W_{N+1}\mid W_N)` is not enough.

That objection is not a technical nuisance. It is the right conceptual
correction. If the Barandes/ISP lesson is taken seriously, the primitive object
should not be a Markov transition from a present control panel to the next
control panel. The primitive object should be a finite indivisible record
cylinder, and Markov-looking laws should appear only after projecting that
cylinder onto a smaller panel.

Receipt:

```text
isp/v7/code/p36_indivisible_history_prediction_campaign.py
isp/v7/code/p36_n9_history_bound_campaign.py
```

The receipts passed:

```text
p36_indivisible_history_prediction_campaign.py: CHECKS PASSED: 14/14
p36_n9_history_bound_campaign.py: CHECKS PASSED: 7/7
```

All combinatorial probabilities and total-variation distances are exact
`Fraction` calculations. Decimal precision for reporting is `140`, above the
requested 80-bit threshold.

## 1. Executive Result

The finite audited result is:

$$
\boxed{
\Pr(S_8\mid W_7)
\ne
\Pr(S_8\mid W_6,W_7)
\ne
\Pr(S_8\mid W_5,W_6,W_7)
}
$$

and also:

$$
\boxed{
\Pr(S_8\mid W_4,W_5,W_6,W_7)
=
\Pr(S_8\mid W_5,W_6,W_7)
}
$$

Here:

- `N` is the number of committed records.
- `R_N` is a committed unlabeled record order with `N` records.
- `S_N` is the selected positive shadow from Papers XXXIV-XXXV.
- `W_N` is the scalar-work control panel from Paper XXXV.
- `S_8` is the selected-shadow state of the `N=8` parent record.
- `W_7`, `W_6`, `W_5`, and `W_4` are scalar-work summaries of records reached
  by deleting one, two, three, and four records from the `N=8` parent.

The exact finite cylinder is:

$$
R_8 \to R_7 \to R_6 \to R_5 \to R_4.
$$

After projecting `R_7,R_6,R_5,R_4` to `W_7,W_6,W_5,W_4`, the receipt found:

```text
E TV[P(S8|W6,W7), P(S8|W7)]       = 0.119693946444318468127991937516
E TV[P(S8|W5,W6,W7), P(S8|W6,W7)] = 0.0285727703504241202653901066599
E TV[P(S8|W4..W7), P(S8|W5..W7)]  = 0
E TV[P(S8|W4..W7), P(S8|W7)]      = 0.144299269627934948229732810232
```

So the current panel `W_N` is not Markov in the audited window. Older boundary
history changes the forward law until the finite window saturates at
`W_5,W_6,W_7`.

The practical consequence is:

$$
\boxed{
\text{the click law should be a projective history law, not a one-step Markov law.}
}
$$

## 2. What `W_N` Contains

Paper XXXV found that the exact h-transform weights at `N=6,7` are determined
by a compact scalar-work packet:

$$
W_N(A)
=
\left(
M(A),
|A|,
\operatorname{DelScal}(A),
\operatorname{InsScal}(A)
\right).
$$

The terms are:

- `A` is an atom of the selected positive shadow. In plain language, it is a
  bucket of records that look the same to the selected diamond/sector
  observables.
- `M(A)` is the selected odd quadratic metric channel of that atom.
- `|A|` is the number of committed records inside the atom.
- `DelScal(A)` is a scalar summary of how atom `A` deletes into smaller atoms.
- `InsScal(A)` is a scalar summary of how larger atoms insert into atom `A`.

This packet is a control panel. It is not the whole record. It remembers enough
to compute the audited effective h-weight at `N=6,7`, but it does not remember
every possible older boundary circumstance.

That is exactly why `Pr(W_{N+1}\mid W_N)` should fail: `W_N` is useful, but not
indivisible.

## 3. The Exact Cylinder Audited Here

The receipt builds the exact deletion cylinder:

$$
R_8 \xrightarrow{d} R_7 \xrightarrow{d} R_6 \xrightarrow{d} R_5 \xrightarrow{d} R_4.
$$

The symbol `d` means deletion of one record followed by forgetting labels and
keeping the committed unlabeled order.

The exact projected joint law is:

$$
\mathbb P(W_4,W_5,W_6,W_7,S_8).
$$

This is not fitted. It is obtained by exact enumeration of the audited
permutation-order universe:

```text
N=3: records=5     permutations=6
N=4: records=16    permutations=24
N=5: records=63    permutations=120
N=6: records=315   permutations=720
N=7: records=1956  permutations=5040
N=8: records=14794 permutations=40320
```

The resulting projected cylinder has:

```text
cylinder atoms = 2794705
total_mass     = 1
```

The total mass is exactly `1`.

## 4. Why One-Step Markov Prediction Fails

A one-step control-panel law would say:

$$
\Pr(S_8\mid W_7)
$$

is the right effective future law.

But the exact cylinder lets us ask whether adding the previous panel changes
that future law:

$$
\Pr(S_8\mid W_6,W_7).
$$

It does. The expected total-variation distance is:

$$
\mathbb E\,TV
\left[
\Pr(S_8\mid W_6,W_7),
\Pr(S_8\mid W_7)
\right]
=
0.119693946444318468127991937516\ldots
$$

This is too large to call noise.

Then the receipt asks whether an even older panel still matters:

$$
\Pr(S_8\mid W_5,W_6,W_7).
$$

It still matters:

$$
\mathbb E\,TV
\left[
\Pr(S_8\mid W_5,W_6,W_7),
\Pr(S_8\mid W_6,W_7)
\right]
=
0.0285727703504241202653901066599\ldots
$$

Then the receipt asks whether one more older panel matters:

$$
\Pr(S_8\mid W_4,W_5,W_6,W_7).
$$

At this audited level it does not. The expected distance is exactly:

$$
\mathbb E\,TV
\left[
\Pr(S_8\mid W_4,W_5,W_6,W_7),
\Pr(S_8\mid W_5,W_6,W_7)
\right]
=
0.
$$

So the correct finite slogan is:

$$
\boxed{
W_N \text{ is not Markov, but finite history can become sufficient for a chosen projection.}
}
$$

## 5. Effective Stochastic Residuals

The campaign then measures how uncertain the best prediction remains when we
condition on longer histories.

```text
current W7           contexts=748   multi=748   avg_support=85.7609126984126984 max_support=409 bayes_residual=0.948400297619047619047619047619
history W6,W7        contexts=4157  multi=4157  avg_support=64.9577380952380952 max_support=367 bayes_residual=0.943323058390022675736961451247
history W5,W6,W7     contexts=16842 multi=16842 avg_support=61.0575491307634165 max_support=295 bayes_residual=0.941957199546485260770975056689
history W4,W5,W6,W7  contexts=51065 multi=51065 avg_support=61.0575491307634165 max_support=295 bayes_residual=0.941957199546485260770975056689
```

The words mean:

- `contexts` is the number of distinct observed conditioning states.
- `multi` is the number of contexts that still allow more than one possible
  future `S_8`.
- `avg_support` is the average number of possible future `S_8` states per
  context.
- `max_support` is the largest future support found for one context.
- `bayes_residual` is the probability of being wrong if, for each context, we
  always guess the most likely future.

Longer history improves prediction until exact finite saturation:

$$
0.941957199546485260770975056689
=
0.941957199546485260770975056689
<
0.943323058390022675736961451247
<
0.948400297619047619047619047619.
$$

The first value is the residual for `W_4,W_5,W_6,W_7`; the second equal value is
the residual for `W_5,W_6,W_7`. Thus `W_4` refines the context count but does
not refine the future law for `S_8`.

Finite history suffices for this projection at this audited size, but it does
not eliminate uncertainty.

This is the right place to use stochastic modelling:

$$
\boxed{
\text{randomness models what the chosen record panel has not calculated.}
}
$$

It should not be read as fundamental dice in the records.

## 6. The Asymptotic Prediction Program

For a history window of length `k`, define:

$$
H_{N,k}
=
(W_{N-k},W_{N-k+1},\ldots,W_N).
$$

Here:

- `N` is the current record count;
- `k` is the lookback range;
- `H_{N,k}` is the projected scalar-work history ending at `N`.

Define the effective predictive kernel:

$$
K_{N,k}
=
\Pr(S_{N+1}\mid H_{N,k}).
$$

This is not assumed to be fundamental. It is the exact conditional law after
projecting the larger indivisible record cylinder onto the computable panel
history.

The key memory diagnostic is:

$$
\epsilon_k(N)
=
\mathbb E\,TV(K_{N,k},K_{N,k-1}).
$$

The terms are:

- `TV` is total-variation distance, a measure of how different two probability
  laws are.
- `K_{N,k}` is the prediction using `k` steps of panel history.
- `K_{N,k-1}` is the prediction using one fewer step.
- `\epsilon_k(N)` measures how much the newly included older panel changes the
  predicted future.

The audited values are:

```text
epsilon_1(7) = 0.119693946444318468127991937516
epsilon_2(7) = 0.0285727703504241202653901066599
epsilon_3(7) = 0
```

The asymptotic question is whether the sequence decays or saturates:

$$
\epsilon_k(N)\to 0
$$

as the history range `k` grows, perhaps with `k=k(N)`, or whether:

$$
\epsilon_k(N)=0
$$

after some finite predictive range.

If either happens in the physical filtration, then increasing history windows
give asymptotically full predictions. If neither happens, then the right state
is not a finite panel window; it is an infinite or projective predictive state.

## 7. Random Processes as Compression, Not Ontology

Let `Z_{N,k}` denote all the older or finer record information not included in
the chosen panel history `H_{N,k}`.

The full finite object is:

$$
\Pr(S_{N+1},Z_{N,k}\mid H_{N,k}).
$$

If we do not calculate `Z_{N,k}`, the visible model becomes:

$$
K_{N,k}
=
\sum_z
\Pr(S_{N+1}\mid H_{N,k},Z_{N,k}=z)
\Pr(Z_{N,k}=z\mid H_{N,k}).
$$

This is the mathematical form of effective randomness.

The randomness is not saying:

> the record itself rolls a die.

It is saying:

> the panel did not include every boundary circumstance, so we average over the
> uncomputed compatible circumstances.

That is compatible with indivisibility. The stochastic process is a language
for the shadow of the indivisible history, not a replacement for it.

## 8. What a Full Predictive Law Would Need

The law should provide three linked objects.

First, a record-intrinsic panel:

$$
\mathcal W_N.
$$

This is the admissible information extracted from `N` records. Paper XXXV found
one finite candidate: scalar-work `W_N`.

Second, a projective history law:

$$
\mathbb P(\mathcal W_{N-k},\ldots,\mathcal W_N,S_{N+1}).
$$

This is the object that replaces a naive one-step Markov transition.

Third, a controlled residual process:

$$
\Xi_{N,k}
=
\Pr(Z_{N,k}\mid H_{N,k}).
$$

This represents the uncomputed part of the record cylinder. It must obey
projective consistency:

$$
\mathbb E[
\mathbb E[f(S_{N+1})\mid H_{N,k}]
\mid H_{N,k-1}
]
=
\mathbb E[f(S_{N+1})\mid H_{N,k-1}].
$$

Here:

- `f` is any test function of the next selected shadow;
- the equation is the tower property of conditional expectation;
- physically, it says that coarser predictions must be the average of finer
  predictions.

This is the stochastic version of deletion/insertion consistency.

## 9. Hostile Review

### Objection 1: This still uses a hidden permutation-order ensemble.

Yes. The receipt is an audit environment. It does not claim that hidden
presentations are physical ontology. The important result is not the hidden
ensemble itself; it is the failure of a one-panel Markov closure after
record-projection.

The law target remains record-intrinsic:

$$
\Pr(S_{N+1}\mid W_N)
\quad \text{is rejected, while} \quad
\Pr(S_{N+1}\mid W_{N-k:N})
\quad \text{is tested as a projected record law.}
$$

### Objection 2: The Bayes residual is huge, so the panel is weak.

Correct. At this small finite size, the panel is not enough for near-complete
prediction. That is not a failure of the campaign; it is the campaign result.

The panel is already strong enough to carry exact h-transform weights at
`N=6,7`, but not strong enough to make future selected shadows nearly
deterministic from a short history.

### Objection 3: Maybe longer history helps only because the receipt is using
deletion chains, not physical time.

Deletion is not physical time here. It is the exact projective probe available
on finite records. The lesson is not "time runs backward." The lesson is that
future effective weights must be consistent with how records project across
sizes.

This is the same reason backward-then-forward audits were useful in Paper XXX:
they expose the boundary information a forward law would have to preserve.

### Objection 4: A stochastic residual sounds like returning to ordinary
stochastic processes.

Only if it is promoted to ontology. The proposed role is narrower:

$$
\text{stochastic process}
=
\text{compressed description of unresolved record-cylinder information}.
$$

That is compatible with non-Markovian ISP. The stochastic object is a projected
effective model, not a primitive Markov chain on present states.

### Objection 5: The result is finite and tiny.

Yes. The finite receipt proves only the audited statement:

```text
R8 -> R7 -> R6 -> R5 -> R4, projected to W4,W5,W6,W7, is non-Markov at W7,
improves through W5,W6,W7, and saturates exactly when W4 is added.
```

The asymptotic theorem is still open.

## 10. Campaign Verdict

The campaign proves the finite version of the conceptual correction:

$$
\boxed{
\Pr(W_{N+1}\mid W_N)
\text{ is the wrong kind of primitive object.}
}
$$

The right object is closer to:

$$
\boxed{
\Pr(S_{N+1}\mid W_{N-k},\ldots,W_N)
\quad
\text{with controlled } k\to\infty \text{ projective residual.}
}
$$

The click law should therefore be sought as:

> a record-intrinsic projective history law whose finite stochastic kernels are
> effective shadows of unresolved boundary history.

The next exact target is:

$$
\boxed{
\text{prove or falsify }
\epsilon_k(N)\to0
\text{ or finite } \epsilon_k(N)=0
\text{ for the admissible diamond/scalar-work filtration.}
}
$$

If `\epsilon_k(N)` decays or reaches exact finite saturation, the control panel
can deliver asymptotically full predictions by increasing the history range. If
it does neither, then the click law needs a stronger predictive state than any
finite scalar-work history.

## 11. Four Follow-Up Campaigns

The four conceptual openings were then tested in the same receipt:

1. the history bound may grow with system size;
2. randomness should be bounded to an experiment-plus-instrument region;
3. the finite law looks like a path-sum over compatible record histories;
4. the selector looks like a least-boundary-work principle.

The extended receipt passed:

```text
CHECKS PASSED: 14/14
```

### 11.1 Campaign A: The History Bound

The finite result at `N=8` is not:

> the memory length is universally three.

It is:

> for the audited prediction `S_8` from scalar-work histories
> `W_4,W_5,W_6,W_7`, the shortest sufficient causal suffix is
> `W_5,W_6,W_7`.

The exact suffix losses against the full audited history were:

```text
suffix W7             loss_vs_full = 0.144299269627934948229732810232
suffix W6,W7          loss_vs_full = 0.0285727703504241202653901066599
suffix W5,W6,W7       loss_vs_full = 0
suffix W4,W5,W6,W7    loss_vs_full = 0
```

The all-subset sufficiency scan also found:

```text
all-subset sufficient contexts min_size=3: W5,W6,W7
```

So `W_5,W_6,W_7` is not merely the shortest causal suffix. In this audited
panel family it is also the unique shortest sufficient context among all
subsets of `W_4,W_5,W_6,W_7`.

Define the finite memory range:

$$
m_N(\mathcal P,S)
=
\min\left\{
k:
\Pr(S_{N+1}\mid W_{N-k},\ldots,W_N)
=
\Pr(S_{N+1}\mid W_{N-k-1},\ldots,W_N)
\right\}.
$$

Here:

- `N` is the current record count;
- `\mathcal P` is the chosen record panel/filtration;
- `S_{N+1}` is the future projected shadow being predicted;
- `m_N(\mathcal P,S)` is the first history length after which adding one more
  older panel changes nothing for that prediction.

The receipt shows:

$$
m_7(\mathcal W,S_8)=2
$$

if `k=2` means the suffix `W_5,W_6,W_7`.

For larger systems, the real theorem may be:

$$
m_N(\mathcal P,S)
\text{ is bounded,}
$$

or:

$$
m_N(\mathcal P,S)
\text{ grows with } N,
$$

or:

$$
m_N(\mathcal P,S)
\text{ grows with the size of the bounded experiment diamond.}
$$

The finite campaign supports finite sufficiency, but it does not prove a
universal constant memory length.

### 11.2 Campaign B: Randomness Bounded to an Experiment

The second idea is that realistic stochastic modelling should not describe the
whole universe. It should describe a bounded record region containing:

- the system being tested;
- the instrument measuring it;
- enough surrounding record history to make the predicted event well-defined.

Everything outside that bounded region is represented by a calibrated residual.

The receipt tested the calibration condition by exact tower identities:

```text
tower TV full -> W5,W6,W7 = 0
tower TV W5,W6,W7 -> W6,W7 = 0
tower TV W6,W7 -> W7       = 0
```

This means the coarser stochastic kernels are exactly the averages of finer
stochastic kernels. In symbols:

$$
\Pr(S_8\mid W_6,W_7)
=
\mathbb E[
\Pr(S_8\mid W_5,W_6,W_7)
\mid W_6,W_7
].
$$

The terms are:

- `S_8` is the future selected shadow;
- `W_5,W_6,W_7` is the finer bounded history panel;
- `W_6,W_7` is the coarser bounded history panel;
- the expectation averages over the unresolved `W_5` information compatible
  with the coarser panel.

The residual remains nontrivial even after the sufficient history:

```text
residual       = 0.941957199546485260770975
average support = 61.05754913076342
```

This should not be read as ontic randomness. It says that `W_5,W_6,W_7` is
sufficient relative to the audited full `W_4..W_7` panel, but many possible
`S_8` shadows still remain compatible with that panel. The stochastic object is
therefore a calibrated experiment-bounded compression.

### 11.3 Campaign C: Path-Sum / Path-Integral Shadow

The exact finite object is a sum over compatible deletion histories:

$$
R_8\to R_7\to R_6\to R_5\to R_4.
$$

For a visible history panel `H`, define:

$$
K(S_8\mid H)
=
\frac{
\sum_{\gamma:\,\rho(\gamma)=H,\;S(\gamma)=S_8}
w(\gamma)
}{
\sum_{\gamma:\,\rho(\gamma)=H}
w(\gamma)
}.
$$

Here:

- `\gamma` is a compatible finite record history/path through the deletion
  cylinder;
- `\rho(\gamma)=H` means the path projects to the visible panel history `H`;
- `S(\gamma)=S_8` means the parent of the path has selected shadow `S_8`;
- `w(\gamma)` is the exact rational path weight induced by the audited
  permutation-order measure and deletion multiplicities;
- `K(S_8\mid H)` is the effective predicted law after summing compatible paths.

The receipt verified exact normalization:

```text
max normalization error K(S8|W7)      = 0
max normalization error K(S8|W5..W7)  = 0
max normalization error K(S8|W4..W7)  = 0
```

and exact path-sum coarse graining:

```text
coarse kernels are exact sums of finer history kernels
```

This is the precise sense in which the analogy with Feynman's path integral is
useful:

```text
Feynman: sum over compatible paths, then get observable predictions.
SHARD:   sum/project over compatible record histories, then get record-panel predictions.
```

But the finite receipt is still a positive path-sum. It does not prove that
the click law uses complex amplitudes. The safe statement is narrower:

> the record law has a path-sum architecture before it has a one-step
> transition architecture.

### 11.4 Campaign D: Least Boundary Work

The fourth idea is that the law should resemble least action:

> choose the smallest admissible history law whose boundary variation no longer
> changes the prediction.

The receipt tested the finite action:

$$
\mathcal A(H)
=
\operatorname{Loss}(H)
+ \lambda\,\operatorname{Cost}(H),
$$

where:

- `H` is a causal suffix such as `W_7`, `W_6,W_7`, or `W_5,W_6,W_7`;
- `Loss(H)` is the exact total-variation loss against the full audited
  `W_4..W_7` history;
- `Cost(H)` is the suffix length;
- `\lambda` is taken only as an ordering device after exact zero-loss
  sufficiency is reached.

The exact table was:

```text
suffix W7             cost=1 exact=no  loss=0.144299269627934948229732810232 residual=0.948400297619047619047619047619
suffix W6,W7          cost=2 exact=no  loss=0.0285727703504241202653901066599 residual=0.943323058390022675736961451247
suffix W5,W6,W7       cost=3 exact=yes loss=0                                  residual=0.941957199546485260770975056689
suffix W4,W5,W6,W7    cost=4 exact=yes loss=0                                  residual=0.941957199546485260770975056689
```

Thus the least exact causal suffix is:

$$
\boxed{
W_5,W_6,W_7.
}
$$

This is not a proof of the physical least-action principle. It is a finite
model of the principle:

> do not keep adding boundary history once adding it performs no predictive
> work.

The least-action analogue is therefore scoped to prediction, not ontology. The
selected suffix has zero loss against the audited full panel, but it still has
large residual uncertainty. It is the least sufficient boundary description,
not a deterministic hidden state.

### 11.5 Hostile Review of the Four Campaigns

The campaigns support the four ideas, but only in a scoped form.

First, `W_5,W_6,W_7` being sufficient for `S_8` does not imply that three
panels are always enough. The memory range may grow with `N`, with the
experiment diamond, or with the richness of the future observable.

Second, bounded randomness is legitimate only when the boundary of the
experiment-plus-instrument diamond is explicitly named. Otherwise the residual
can hide arbitrary ignorance.

Third, the path-integral analogy is structural, not yet quantum. The receipt
proves a positive sum over record histories. Complex amplitudes, phases, and
interference require extra admissibility conditions.

Fourth, the least-action analogy currently selects a minimal sufficient
projection, not a physical action functional. The missing theorem must derive
the action/cost from record-intrinsic boundary work, not impose suffix length by
hand.

The sharpened theorem target is therefore:

$$
\boxed{
\text{derive the admissible panel } \mathcal P_N
\text{ and its boundary-work action so that }
m_N(\mathcal P,S)
\text{ is controlled for bounded experiment diamonds.}
}
$$

## 12. Exact `N=9` Follow-Up: The Three-Panel Rule Fails

The immediate objection to the `N=8` result is:

> maybe `W_5,W_6,W_7` is sufficient only because `N=8` is small.

The next receipt tests exactly that:

```text
isp/v7/code/p36_n9_history_bound_campaign.py
```

It builds the exact cylinder:

$$
R_9\to R_8\to R_7\to R_6\to R_5,
$$

projects the child records to:

$$
W_5,W_6,W_7,W_8,
$$

and predicts the parent selected shadow:

$$
S_9.
$$

The receipt passed:

```text
CHECKS PASSED: 7/7
```

The exact enumeration sizes were:

```text
N=9 records       = 131526
N=9 permutations  = 362880
S9 shadow atoms   = 65521
W8 scalar cells   = 4698
```

The exact path-cylinder check was:

```text
total path weight    = 1097349120
expected path weight = 1097349120
```

So the finite history cylinder was exactly normalized at the integer-count
level.

### 12.1 The Result

The suffix sufficiency table was:

```text
suffix W8           contexts=4698    exact=False conflict_cells=1502 avg_support=160.278819444444444 max_support=1129 bayes_residual=0.965103554281795022535763276504
suffix W7,W8        contexts=35786   exact=False conflict_cells=3937 avg_support=104.341889880952381 max_support=1017 bayes_residual=0.959294930678032529884381736234
suffix W6,W7,W8     contexts=189275  exact=False conflict_cells=5545 avg_support=94.1086220946712018 max_support=713 bayes_residual=0.957667102334761064919795078525
suffix W5,W6,W7,W8  contexts=773576  exact=True  conflict_cells=0    avg_support=91.0702351426681784 max_support=713 bayes_residual=0.957066010131761895430325765423
```

The important line is:

$$
\boxed{
W_6,W_7,W_8
\text{ is not sufficient for } S_9.
}
$$

The least exact suffix in this audited projection is:

$$
\boxed{
W_5,W_6,W_7,W_8.
}
$$

So the three-panel pattern from `S_8` fails one exact size higher.

### 12.2 What This Means

The memory rule is not:

$$
\text{always use three panels.}
$$

The finite data now says:

```text
S8: W5,W6,W7 is sufficient relative to W4..W7.
S9: W5,W6,W7,W8 is sufficient relative to W5..W8, while W6,W7,W8 is not.
```

Thus the relevant object is really:

$$
m_N(\mathcal P,S),
$$

the least sufficient memory range for panel `\mathcal P` and future observable
`S`.

In this audited scalar-work projection:

$$
m_7(\mathcal W,S_8)=2,
$$

using the convention that `m=2` means `W_5,W_6,W_7`, while:

$$
m_8(\mathcal W,S_9)=3,
$$

meaning `W_5,W_6,W_7,W_8`.

This is the first direct finite evidence that the memory range can grow with
the size of the predicted record.

### 12.3 Calibration Still Holds

Even though the memory range grows, the bounded residual kernels remain exactly
calibrated:

```text
tower count mismatches W5..W8 -> W6..W8 = 0
tower count mismatches W6..W8 -> W7,W8  = 0
tower count mismatches W7,W8 -> W8      = 0
```

So the stochastic-residual interpretation survives. Coarser predictions are
still exact sums of finer bounded-history kernels.

### 12.4 Why `N=10` Was Not Brute-Forced Here

The receipt also records the feasibility boundary:

```text
9!  = 362880
10! = 3628800
```

Exact `N=10` brute force would begin with `3,628,800` hidden presentations
before canonical aggregation and before the multi-step history cylinder. That
is not impossible in principle, but it is beyond the safe brute-force style of
this receipt. `N=10` needs one of:

- dynamic generation without materializing the full universe;
- Monte Carlo/splitting estimates with exact spot checks;
- a theorem for the memory-range function;
- a bounded-diamond version that avoids whole-universe enumeration.

The honest next theorem target is therefore sharper:

$$
\boxed{
\text{derive or bound } m_N(\mathcal P,S)
\text{ without enumerating the full } R_{N+1}\to\cdots\text{ cylinder.}
}
$$

### 12.5 Updated Verdict

The `N=9` follow-up changes the interpretation of Paper XXXVI.

The old tempting reading was:

> three histories are enough.

That is false.

The surviving reading is:

> finite sufficient histories exist in the audited windows, but the least
> sufficient history length is itself dynamical and must be selected by the
> boundary-work principle.

This strengthens the reason to connect the record law with least action:
least action is not choosing a fixed number of past panels. It is choosing the
shortest admissible boundary history that performs all predictive work for the
bounded record problem being asked.

## 13. Formula Campaign: History Bounds and Partial Experimental Panels

The `N=9` follow-up makes the next correction unavoidable:

> the point is not to brute-force larger cylinders. The point is to derive a
> formula or bound for the required history, and a formula for probabilities
> when the experiment sees only part of the required history.

This section states the formula-level target.

### 13.1 Full Panel Histories

Let:

$$
H_{N,k}
=
(W_{N-k},W_{N-k+1},\ldots,W_N)
$$

be the full admissible panel history of range `k`.

Here:

- `N` is the current record size;
- `k` is the number of earlier panels included;
- `W_j` is the full admissible control panel at size `j`;
- `H_{N,k}` is the history window available to the prediction law.

Let `S_{N+1}` be the future record event or projected shadow being predicted.
Define the kernel:

$$
K_{N,k}(s)
=
\Pr(S_{N+1}=s\mid H_{N,k}).
$$

This is the exact prediction if the full panel history `H_{N,k}` is known.

The history increment is:

$$
\Delta_{N,k}
=
\mathbb E\,TV(K_{N,k+1},K_{N,k}).
$$

The terms are:

- `TV` is total-variation distance;
- `K_{N,k+1}` is the prediction after adding one older panel;
- `K_{N,k}` is the prediction without that older panel;
- `\Delta_{N,k}` measures the predictive value of the newly added boundary
  history.

The finite receipts measured examples of this object:

```text
S8: Delta_7,0 = 0.119693946444318468127991937516
S8: Delta_7,1 = 0.0285727703504241202653901066599
S8: Delta_7,2 = 0
S9: Delta_8,2 is not zero; W6,W7,W8 has 5545 conflict cells.
```

### 13.2 Tail Bound for Unknown Required History

Suppose the correct prediction would use a larger range `L`, but we compute only
range `k<L`.

Then the triangle inequality gives the formula:

$$
\mathbb E\,TV(K_{N,L},K_{N,k})
\le
\sum_{j=k}^{L-1}\Delta_{N,j}.
$$

This is the first non-brute-force history bound. It says:

> the prediction error from truncating history is bounded by the sum of the
> omitted history increments.

If a theorem gives:

$$
\Delta_{N,j}
\le
C_N e^{-j/\xi_N},
$$

then:

$$
\mathbb E\,TV(K_{N,\infty},K_{N,k})
\le
\frac{C_N e^{-k/\xi_N}}{1-e^{-1/\xi_N}}.
$$

So a sufficient history range at tolerance `\epsilon` is:

$$
m_N^\epsilon
\le
\min\left\{
k:
\frac{C_N e^{-k/\xi_N}}{1-e^{-1/\xi_N}}
\le
\epsilon
\right\}.
$$

If instead the influence decays polynomially:

$$
\Delta_{N,j}
\le
C_N(1+j)^{-p},
\quad p>1,
$$

then:

$$
\mathbb E\,TV(K_{N,\infty},K_{N,k})
\le
\frac{C_N}{p-1}(k+1)^{1-p}.
$$

Thus the general formula is:

$$
\boxed{
m_N^\epsilon
=
\min\left\{
k:
\sum_{j=k}^{\infty}\Delta_{N,j}
\le
\epsilon
\right\}.
}
$$

This is the replacement for brute force. The real missing theorem is a bound on
`\Delta_{N,j}` from record-intrinsic boundary work.

### 13.3 Partial Experimental Panels

In an actual experiment, we do not know the full `W_N`, and we certainly do not
know the full required history `H_{N,k}`. We know a partial observation:

$$
O_{N,k}
=
\Phi(H_{N,k}).
$$

Here:

- `O_{N,k}` is what the experiment and instrument actually record;
- `\Phi` is the coarse observation map;
- many full histories `H_{N,k}` may be compatible with the same observation
  `O_{N,k}`.

The correct prediction from partial information is:

$$
\boxed{
\Pr(S_{N+1}=s\mid O_{N,k})
=
\sum_h
\Pr(S_{N+1}=s\mid H_{N,k}=h)
\Pr(H_{N,k}=h\mid O_{N,k}).
}
$$

This is the formula for experimental probabilities.

It says:

> average the full-history prediction over all required histories compatible
> with the partial observed panel.

This is not optional stochasticity. It is the tower property of conditional
expectation:

$$
\Pr(S_{N+1}=s\mid O_{N,k})
=
\mathbb E[
K_{N,k}(s)
\mid O_{N,k}
].
$$

So the probability from partial `W_N` has a precise source: unresolved compatible
full histories.

### 13.4 Total Error Bound: History Tail Plus Partial Observation

Let:

$$
K^O_{N,k}(s)
=
\Pr(S_{N+1}=s\mid O_{N,k})
$$

be the experimentally available prediction.

Define the partial-panel residual:

$$
A_{N,k}(O)
=
\mathbb E\,TV(K_{N,k},K^O_{N,k}).
$$

This measures how much predictive information is lost because the experiment
sees only `O_{N,k}` instead of the full required panel history `H_{N,k}`.

Combining partial observation with history truncation gives:

$$
\boxed{
\mathbb E\,TV(K_{N,L},K^O_{N,k})
\le
\sum_{j=k}^{L-1}\Delta_{N,j}
+
A_{N,k}(O).
}
$$

This is the main formula of the campaign.

It separates two effects:

1. **History-tail error:** the required history was longer than the history
   included.
2. **Partial-panel error:** the experiment did not observe the whole included
   history.

For a bounded experiment-plus-instrument diamond `B`, write this as:

$$
\eta_B
=
\underbrace{
\sum_{j=k}^{L-1}\Delta_{B,j}
}_{\text{uncomputed older boundary}}
+
\underbrace{
A_{B,k}(O_B)
}_{\text{partial observed panel}}.
$$

Then for any event `E` about the experiment:

$$
\left|
\Pr(E\mid\text{full required record history})
-
\Pr(E\mid O_B)
\right|
\le
\eta_B.
$$

That is the experimentally useful probability statement.

### 13.5 Derivation of the Main Bound

The main bound uses only two facts.

First, history kernels are nested:

$$
H_{N,k}
\subset
H_{N,k+1}
\subset
\cdots
\subset
H_{N,L}.
$$

Second, total variation obeys the triangle inequality.

For one realized full history path:

$$
TV(K_{N,L},K^O_{N,k})
\le
TV(K_{N,L},K_{N,k})
+
TV(K_{N,k},K^O_{N,k}).
$$

The first term telescopes:

$$
TV(K_{N,L},K_{N,k})
\le
\sum_{j=k}^{L-1}
TV(K_{N,j+1},K_{N,j}).
$$

Taking expectations gives:

$$
\mathbb E\,TV(K_{N,L},K_{N,k})
\le
\sum_{j=k}^{L-1}
\mathbb E\,TV(K_{N,j+1},K_{N,j})
=
\sum_{j=k}^{L-1}\Delta_{N,j}.
$$

The second term is exactly:

$$
\mathbb E\,TV(K_{N,k},K^O_{N,k})
=
A_{N,k}(O).
$$

Therefore:

$$
\mathbb E\,TV(K_{N,L},K^O_{N,k})
\le
\sum_{j=k}^{L-1}\Delta_{N,j}
+
A_{N,k}(O).
$$

No Markov assumption is used. This is why the formula is compatible with the
Barandes/ISP objection to one-step stochastic dynamics.

### 13.6 Information Form of the Partial-Panel Bound

The partial-panel residual can also be bounded by conditional information.

Let:

$$
I(S_{N+1};H_{N,k}\mid O_{N,k})
$$

be the conditional mutual information between the future event and the full
history, after the partial observation is known.

Then Pinsker's inequality gives:

$$
A_{N,k}(O)
\le
\sqrt{
\frac{1}{2}
I(S_{N+1};H_{N,k}\mid O_{N,k})
}.
$$

This is useful because it turns the partial observation problem into a
compression problem:

> choose experimental observables `O` that make the future nearly independent
> of the unobserved parts of `H`.

Equivalently, the instrument should be designed so that:

$$
I(S_{N+1};H_{N,k}\mid O_{N,k})
$$

is small.

### 13.7 Least Boundary Work as an Optimization Formula

The least-boundary-work principle can now be stated without brute force.

For an experiment diamond `B`, define:

$$
\mathcal A_B(k,O)
=
\sum_{j=k}^{\infty}\Delta_{B,j}
+
A_{B,k}(O)
+
\lambda\,C_B(k,O).
$$

Here:

- `\sum_{j=k}^{\infty}\Delta_{B,j}` is the history-tail cost;
- `A_{B,k}(O)` is the partial-panel cost;
- `C_B(k,O)` is the complexity or reconstruction cost of using that much
  history and that rich an observation panel;
- `\lambda` controls how strongly we penalize over-rich, reconstructive
  descriptions.

The formula-level click-law target is:

$$
\boxed{
(k_B^*,O_B^*)
=
\arg\min_{k,O\ \text{admissible}}
\mathcal A_B(k,O).
}
$$

Then the experimental prediction is:

$$
\boxed{
\Pr(S_B=s\mid O_B^*)
=
\sum_h
\Pr(S_B=s\mid H_{B,k_B^*}=h)
\Pr(H_{B,k_B^*}=h\mid O_B^*).
}
$$

This is the formula version of the current frontier.

The law is not:

$$
\Pr(W_{N+1}\mid W_N).
$$

The law is:

> choose the smallest admissible bounded history/observation pair whose
> history-tail and partial-panel residuals are controlled, then predict by
> averaging over compatible full histories.

### 13.8 Relation to Bounded Experiments

For a realistic experiment, the universe is not the conditioning object.

The conditioning object should be a bounded record diamond:

$$
B
=
\text{system}+\text{instrument}+\text{relevant boundary history}.
$$

The outside universe enters only through the residual term:

$$
\sum_{j=k}^{\infty}\Delta_{B,j}.
$$

If the boundary influence of the outside decays, then the experiment has stable
probabilities. If it does not decay, the experiment is not isolated enough, and
the formula says exactly why.

This is the SHARD version of experimental closure:

> a laboratory probability is valid when the record-boundary tail and
> partial-panel residual are both small.

### 13.9 Hostile Review

This formula campaign is progress, but it does not yet prove the click law.

First, the key missing theorem is still a bound on `\Delta_{B,j}`. Without that
bound, `m_N^\epsilon` is a definition, not a predictive law.

Second, the admissible observation maps `O=\Phi(H)` must be derived from
record-intrinsic diamond structure. Otherwise the formula can hide arbitrary
choices in `O`.

Third, the complexity/reconstruction penalty `C_B(k,O)` must not be a human
regularizer. It must come from the no-hidden-presentation/no-lookup principle
already exposed in Papers XXIX-XXXV.

Fourth, the formula is positive/probabilistic after projection. If complex
amplitudes are real in the deeper theory, they must appear before this projected
positive kernel, not by replacing the experimental probability formula.

The sharpened missing theorem is now:

$$
\boxed{
\text{derive } \Delta_{B,j},\ A_{B,k}(O),\ C_B(k,O)
\text{ from the record diamond, and prove a bound on }
\mathcal A_B(k,O).
}
$$

That would turn the current control panel into a law:

$$
\boxed{
\text{bounded-history sufficiency}
+
\text{partial-panel averaging}
+
\text{non-reconstructive least boundary work}.
}
$$

## 14. Einstein-Reconstruction Import: Histories as the Definition of Spacetime

The previous Einstein-reconstruction papers change the interpretation of the
history problem.

The useful import is not "assume a metric."  The useful import is:

> spacetime is the stable large-scale readout of a finite record history.

The old GR line did not reconstruct Einstein geometry from a single isolated
record.  It reconstructed an effective geometry from finite record invariants,
then demanded that the readout survive changes of presentation, refinement,
local frame, and cofinal extension.

That is exactly the structure now needed for Paper 36.  A bounded history is not
just extra memory for predicting the next click.  A bounded history is also the
object from which the local spacetime packet is read.

### 14.1 What the GR Papers Supply

The relevant imports are:

- v4 Paper 25: finite descent invariants `Q`, `C`, edge action, corner
  holonomy, metric readout, transport, curvature, and source/stress gates;
- v4 Paper 32: same-actual covariance, finite actual domain, Ward/Bianchi
  closure, cofinal stability, and the separation between internal GR closure
  and external continuum comparison;
- v4 Paper 35: low-energy Einstein coupling uniqueness after the metric,
  curvature, and stress readouts already exist;
- v6 Paper 1 and v7 Paper 11: order plus number gives geometry, but only after
  the manifoldlikeness gate;
- v6 Papers 56 and 57: sealed histories supply thermodynamic/Einstein form, but
  not the absolute scale `G`, and genuine indivisibility lives between sparse
  commitments, not in a continuously refined trajectory.

The combined message is:

$$
\boxed{
\text{finite record history}
\longrightarrow
\text{stable GR readout packet}
\longrightarrow
\text{Einstein form, if the low-energy gates pass}.
}
$$

This is not yet the click law.  It is a way to say what it would mean for a
history to define a spacetime.

### 14.2 The History GR Packet

Let `B` be a bounded record diamond.  In experimental language, `B` is the
system, the instrument, and the relevant boundary history that can influence
the experiment.

Let

$$
H_{B,k}
=
(W_{B,N-k},W_{B,N-k+1},\ldots,W_{B,N})
$$

be the last `k+1` visible work panels inside `B`.

Here:

- `H_{B,k}` is the history panel we keep;
- `B` is the bounded record diamond;
- `k` is the history depth;
- `W_{B,n}` is the control-panel readout at size or stage `n` inside `B`;
- `N` is the current boundary size/stage.

Define the finite geometric readout packet:

$$
\mathcal G_{B,k}
=
I_{GR}(H_{B,k})
=
(R/{\sim},g,e,U,F,\nabla F,\Theta,D_{\rm src},r).
$$

The symbols mean:

- `R/~` is the same-actual record quotient: different presentations that say
  the same physical thing are identified;
- `g` is the finite metric readout;
- `e` is the local frame or clock/ruler readout;
- `U` is finite transport between nearby frames;
- `F` is closed-loop curvature/holonomy;
- `\nabla F` is the finite curvature-difference data;
- `\Theta` is the stress/source readout;
- `D_src` is the source dictionary that says which record residues count as
  typed matter/source terms;
- `r` is the refinement map relating the packet to coarser or finer packets.

Then a history defines a spacetime only if the packets stabilize as more
history is included:

$$
\Delta^{GR}_{B,j}
=
\mathbb E\,
d_{GR}\!\left(
\mathcal G_{B,j+1},
\mathcal G_{B,j}
\right).
$$

Here `d_GR` is a distance between finite GR packets: it compares metric
readout, causal order, volume/count, curvature, Ward/Bianchi residue, typed
source residue, and refinement drift.  It is not a continuum distance assumed
in advance; it is a score on the finite readouts.

If

$$
\sum_{j=k}^{\infty}\Delta^{GR}_{B,j}
$$

is small, then the omitted older history has little effect on the spacetime
packet seen by the experiment.  If it is large, then the experiment does not yet
have a stable spacetime description at that boundary depth.

### 14.3 Partial Experimental Spacetime

Real experiments do not see the whole `H_{B,k}`.  They see a partial panel:

$$
O_{B,k}=\Phi(H_{B,k}).
$$

Here:

- `O_{B,k}` is what the instrument actually records;
- `\Phi` is the record-intrinsic observation map;
- the hidden part is not metaphysical extra reality, but the part of the
  bounded history not included in the panel.

The experiment therefore has a distribution over compatible GR packets:

$$
\mu^{O}_{B,k}
=
\operatorname{Law}(\mathcal G_{B,k}\mid O_{B,k}).
$$

This means: given the panel `O`, what finite geometries are still compatible
with the unobserved bounded histories?

The partial-panel geometric error is:

$$
A^{GR}_{B,k}(O)
=
\mathbb E\,
d_{GR}\!\left(
\mathcal G_{B,k},
\mu^{O}_{B,k}
\right).
$$

Informally, `A^{GR}_{B,k}(O)` asks how wide the remaining cloud of possible
geometries is after seeing the actual instrument panel.  If the cloud is tight,
the experiment sees an effectively classical spacetime.  If the cloud is wide,
the experiment is still averaging over distinct compatible spacetime readouts.

Thus the prediction formula should be upgraded from a click-only average to a
history-and-geometry average:

$$
\Pr(S_B=s\mid O_{B,k})
=
\int
\Pr(S_B=s\mid H,\mathcal G(H))
\,
d\Pr(H\mid O_{B,k}).
$$

The formula says: average the future click over all compatible bounded
histories, each carrying its own finite spacetime packet.

### 14.4 The Einstein Equation as a Late Stability Theorem

The old GR reconstruction says that, once the finite packet exists and passes
the gates, the low-energy untyped source-curvature law has the Einstein form.

For a history packet this becomes:

$$
G[\mathcal G_{B,k}]
+
\Lambda_{B,k}g_{B,k}
=
\kappa_{B,k}\Theta_{B,k}
+
\delta^{Ward}_{B,k}
+
\delta^{typed}_{B,k}
+
\delta^{tail}_{B,k}.
$$

Here:

- `G[\mathcal G_{B,k}]` is the finite Einstein-tensor readout from closed-loop
  curvature in the packet;
- `\Lambda_{B,k}g_{B,k}` is the cosmological/integration-constant term;
- `\kappa_{B,k}\Theta_{B,k}` is the source/stress side;
- `\delta^{Ward}` is a same-actual/presentation residue;
- `\delta^{typed}` is higher-curvature, torsion, boundary, or matter-sector
  residue that must be printed rather than hidden;
- `\delta^{tail}` is the error from truncating the older history.

The continuum Einstein equation is not the starting assumption.  It is the
limit case:

$$
\delta^{Ward}_{B,k},
\delta^{typed}_{B,k},
\delta^{tail}_{B,k}
\longrightarrow 0.
$$

Then:

$$
\boxed{
G[g]+\Lambda g=\kappa\Theta.
}
$$

The scale warning remains exactly as in v6 Paper 57: this can give the form of
the equation, not the absolute value of Newton's constant.  `G` still closes the
length/area scale from outside the record-intrinsic data.

### 14.5 Manifoldlikeness as a History Condition

The v7 order-and-number paper says that a single order is not enough.  Generic
orders are non-manifoldlike, and some non-manifold orders fool simple dimension
estimators.

In the history formulation, manifoldlikeness should therefore be tested as a
stability property of the whole history packet:

$$
\mathcal M_B(k)
=
M_{\rm order}(H_{B,k})
+
M_{\rm count}(H_{B,k})
+
M_{\rm interval}(H_{B,k})
+
M_{\rm deletion}(H_{B,k})
+
M_{\rm Ward}(H_{B,k}).
$$

Here:

- `M_order` checks order-only conformal data, dimension, height, links, and
  interval profiles;
- `M_count` checks whether counts behave like a stable volume measure;
- `M_interval` checks whether Alexandrov/diamond subintervals look recursively
  manifoldlike;
- `M_deletion` checks whether deleting bounded record sets causes controlled,
  non-reconstructive drift;
- `M_Ward` checks finite conservation/Bianchi residues.

The point is not that this exact sum is final.  The point is that
manifoldlikeness is no longer a static label on `W_N`.  It becomes a
history-stability condition:

$$
\boxed{
\text{spacetime exists for }B
\quad\text{when}\quad
\mathcal M_B(k)
\text{ and }
\sum_{j=k}^{\infty}\Delta^{GR}_{B,j}
\text{ are small.}
}
$$

That is a better SHARD statement than "the world is a manifold."  The world is
a record history whose bounded experiments admit stable manifoldlike readout
packets.

### 14.6 The Combined Least-Boundary-Work Principle

The click-only action from Section 13 should now have a geometric partner.

Define:

$$
\mathcal A^{total}_B(k,O)
=
\mathcal A^{click}_B(k,O)
+
\mu\,\mathcal A^{GR}_B(k,O)
+
\nu\,\mathcal M_B(k)
+
\eta\,C_B(k,O).
$$

The terms mean:

- `\mathcal A^{click}` is the future-click prediction residual from Section 13;
- `\mathcal A^{GR}` is the spacetime-packet residual;
- `\mathcal M_B` is the manifoldlikeness/stability residue;
- `C_B` is the non-reconstructive complexity penalty;
- `\mu,\nu,\eta` set the relative penalties.

The new target law is:

$$
\boxed{
(k_B^*,O_B^*)
=
\arg\min_{k,O\ \mathrm{admissible}}
\mathcal A^{total}_B(k,O).
}
$$

In nontechnical terms:

> choose the smallest bounded history and instrument panel that predicts the
> next records while also making the local spacetime readout stable,
> manifoldlike, and non-reconstructive.

This is where the Einstein-reconstruction papers help.  They supply the
geometric part of the control panel.  They do not replace the click law; they
say which history data must stabilize before the phrase "spacetime around the
experiment" is licensed.

### 14.7 What This Opens

This import gives a concrete way to use histories for spacetime:

1. Compute or define `\mathcal G_{B,k}` from diamond histories, not from a
   single snapshot.
2. Measure `\Delta^{GR}_{B,j}`: how much the GR packet changes when one more
   layer of history is included.
3. Define partial experimental geometry by `\mu^O_{B,k}`, the distribution of
   compatible GR packets after the real instrument panel is known.
4. Demand bounded least boundary work, not exact reconstruction.
5. Let Einstein form appear only after the history packet passes the finite
   GR gates and typed residues vanish.

The most important conceptual upgrade is:

$$
\boxed{
\text{histories do not merely predict events inside spacetime;}
\quad
\text{histories define the spacetime readout itself.}
}
$$

### 14.8 Hostile Review

This section is promising but not a closure.

First, it moves the problem from click prediction to joint click-plus-geometry
prediction.  That is correct, but harder.

Second, `d_GR`, `\Delta^{GR}`, `A^{GR}`, and `\mathcal M_B` must be derived from
record diamonds.  If they are hand-chosen by continuum intuition, the program
has smuggled GR back in.

Third, the Einstein equation appears only after the finite GR packet passes
the same-actual, Ward/Bianchi, low-energy, and cofinal gates.  The section does
not prove those gates for the actual click law.

Fourth, the scale no-go remains.  Histories may define conformal/relative
spacetime and the Einstein form, but the absolute `G`/`l_step` scale is still
not record-intrinsic.

Fifth, manifoldlikeness remains the shared causal-set wall.  The history
formulation gives better tests, but not yet a theorem that the click law
selects manifoldlike histories.

The sharpened theorem target is therefore:

$$
\boxed{
\text{derive }I_{GR}(H_{B,k}),\ d_{GR},\ \Delta^{GR}_{B,j},
\text{ and }\mathcal M_B(k)
\text{ intrinsically from record diamonds,}
}
$$

and prove:

$$
\boxed{
\inf_{k,O}\mathcal A^{total}_B(k,O)
\text{ is small exactly on bounded histories with stable spacetime readouts.}
}
$$

If that theorem holds, the click law and the emergence of spacetime become the
same problem rather than two separate problems.

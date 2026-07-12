# D4 — no-silent boundary sufficiency and the local-law obstruction

**Status:** preregistered before the D4 executable was written or run,
2026-07-11. Reviews ON. All production code and receipts must remain under
`v10/`. Theorem gates use exact integers and rational arithmetic. No fitted
floating-point threshold may decide a verdict.

## 1. Question

D3 proved that one-event incidence restricts naturally while its two positive
global-prefix kernels do not. The retained unmarked subsystem forgets how
many full-history precursors collapse to each visible precursor.

D4 asks:

> Can no-silent boundary marks make the retained history sufficient for an
> exact, nontrivial, restriction-natural next-extension law without encoding
> an unbounded or law-dependent summary of the discarded universe?

This separates three questions:

1. what unmarked all-restriction naturality forces;
2. what exact boundary message repairs a supplied non-natural law;
3. whether that message fits a uniform finite record capacity and whether a
   profinite mark tower changes the answer.

## 2. Frozen objects

For every finite poset `P`, let `J(P)` be its finite set of down-sets. An
unmarked extension kernel is a probability distribution

$$
\kappa_P:J(P)\to[0,1].
$$

For a retained vertex subset `K`, the deterministic restriction sends

$$
D\longmapsto D\cap K
$$

and regards the result as a down-set of the induced order `P|K`.

### Strong unmarked naturality

The family is restriction-natural when, for every finite `P`, every retained
subset `K`, and every `A in J(P|K)`,

$$
\kappa_{P|K}(A)
=
\sum_{D\in J(P):D\cap K=A}\kappa_P(D).
$$

The family must also be covariant under every relabeling. This is an
**autonomous unmarked subsystem axiom**. D4 does not preregister it as forced
by Barandes ISP; it audits its consequences.

### Boundary-sufficient marked repair

For a supplied raw positive weight law `w_P(D)`, define the completion weight
seen at cut `K`:

$$
W_{P,K}(A)
=
\sum_{D\cap K=A}w_P(D).
$$

The normalized vector `[W_{P,K}]` is the exact predictive message for the
visible precursor. Two contexts are predictively equivalent exactly when
their normalized vectors agree. Calling this vector a boundary mark repairs
the probability square by construction; D4 must grade that repair as
**law-relative** unless it is derived independently of `w`.

## 3. Preregistered theorem targets

### T1 — unmarked naturality-collapse theorem

The leading theorem candidate is:

> Every covariant probability family on down-sets of all finite unmarked
> posets that is natural under every induced-subposet restriction has the form
> $$
> \kappa_P=(1-p)\,\delta_\varnothing+p\,\delta_P
> $$
> for one constant `p in [0,1]` independent of `P`.

The proof route is frozen:

1. the one-point law defines `p`;
2. restriction of the two-chain to its bottom and top forbids its proper
   nonempty ideal;
3. a three-point `V` order transfers that refusal to the two-antichain;
4. every pair in an arbitrary finite poset is either a chain or antichain, so
   unequal inclusion of any pair has probability zero.

This result, if correct, is an **all-or-nothing universal-precursor family**, not a
local interacting click law. The parameter `p` remains unselected.

### T2 — independent exact linear classification

Do not accept T1 from prose alone. Enumerate every labeled strict finite poset
through at least three vertices, every down-set probability variable, and the
complete rational linear system consisting of:

- one normalization equation per poset;
- every induced-subset pushforward equation;
- every relabeling covariance equation.

Exact Gaussian elimination must find an affine solution space of dimension
one, and the empty/full mixture line must satisfy every equation. Any extra
dimension or inconsistency kills T1 at the registered scope.

### T3 — D3 witness failure

Reproduce the D3 chain restriction exactly:

$$
(1/3,2/3)\ne(1/2,1/2).
$$

This verifies that the positive `(a,b)` controls lie outside T1's strong
naturality class.

## 4. Boundary-message gates

### M1 — exact completion-message sufficiency

For all audited posets/cuts and both D3 positive weight laws, construct
`W_{P,K}`, normalize it exactly, and verify equality with the direct
pushforward distribution. This proves sufficiency for a **supplied** law only.

### M2 — law-relative refusal

Find one fixed structural parent/cut whose normalized completion message
differs between the two D3 laws. The registered minimal witness is the
three-antichain retained to one point; the expected inclusion probabilities
are `1/2` and `9/14`. If the values do not differ, the witness fails and a new
opening must be investigated before review.

### M3 — minimal predictive equivalence

Within the audited family, two cut contexts may share one exact predictive
mark iff their normalized visible-precursor distributions agree. The receipt
must classify messages by exact rational tuples, not display strings or
floating tolerances.

## 5. Uniform finite-capacity gates

Use the D3 uniform down-set law on an `n`-point chain and retain its minimal
point. There are `n+1` ideals, only one of which omits the retained point, so

$$
P_n(\text{included})=\frac{n}{n+1}.
$$

### C1 — distinct-message lower bound

For chain depths `1,...,N`, these probabilities are pairwise distinct. Any
exact deterministic boundary mark through depth `N` therefore needs at least
`N` states and

$$
\lceil\log_2 N\rceil
$$
bits. Across unbounded depth, no fixed finite alphabet suffices.

This is conditional on a **uniform fixed record-capacity** interpretation. If
each finite cut may use an unbounded integer mark or an expanding family of
records, exact sufficiency is possible but the total boundary memory is not
uniformly bounded.

### C2 — coarse provenance refusal

A single flag such as `external-parent-present` is constant for every chain
with `n>=2` but the exact probabilities remain different. Such a projected
provenance bit is necessary in some cuts but not sufficient in general.

### C3 — trivial-law control

The empty/full universal-precursor family requires no environment message and passes
restriction naturality. This is the control proving that the capacity no-go
is about nontrivial proper-precursor structure, not probability itself.

## 6. Profinite scope

A profinite tower of finite boundary partitions can retain successively more
information. D4 must distinguish:

- every fixed finite quotient, which identifies some distinct chain depths
  and therefore cannot determine all exact `n/(n+1)` values;
- the full inverse-limit point, which can encode unbounded information but is
  not one finite record readout;
- approximation, which may converge without being exact at any fixed stage.

The receipt will test the simplest residue marks: `n mod m` cannot determine
`n/(n+1)` because `n` and `n+m` share the residue and have different exact
probabilities. No theorem against every alternative compact mark topology is
claimed.

## 7. Ontology and Barandes/diamond gates

1. A completion message is a sufficient statistic for a supplied law, not a
   derivation of that law.
2. Barandes-style full-history conditioning permits subsystem memory; it does
   not promise a bounded sufficient statistic or select one.
3. No-silent boundary discipline says relevant residue cannot be discarded.
   It may require an expanding boundary or new sector; it does not guarantee
   a unique bounded center.
4. A real/rational exact message carries unbounded distinguishability unless
   operationally partitioned. It is not silently called one finite record.
5. The empty/full survivor is universe-global: when full fires, the new event
   has every old event in its past. Restriction naturality alone therefore
   does not imply locality.
6. No cone, dimension, quantum, continuum, or absolute-scale conclusion is
   licensed.

## 8. Verdict gates

- `SELECTED-LOCAL-LAW`: the audited principles uniquely determine a
  nontrivial bounded-message local kernel.
- `UNMARKED-GLOBAL-COLLAPSE`: T1 holds but leaves the universal-precursor parameter
  free.
- `LAW-RELATIVE-UNBOUNDED-MESSAGE`: exact marked repair exists only relative
  to a supplied law and requires unboundedly many message states on the chain
  family.
- `THEOREM-FAILURE`: the exact census refutes T1 or the claimed message lower
  bound.

Multiple verdict labels may apply. None is the final interacting click law.

## 9. Hostile-review protocol

After the receipt, results note, and Paper 5 are complete, independent streams
will audit:

1. exact linear algebra and theorem proof;
2. independent reconstruction, message counts, and reproducibility;
3. ontology/locality, no-silent scope, Barandes, diamonds, finite capacity,
   and profinite interpretation.

Every concrete opening must be investigated before the next round. Final
acceptance requires all streams to reproduce the result and accept the claim
ceiling.

## 10. Initial execution and preregistration correction

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 v10/code/d4_boundary_sufficiency_exact.py
```

Initial repaired result: **17/17 exact checks passed**.

The first implementation run failed because identity covariance overwrote a
coefficient instead of cancelling it. After that coding repair, the registered
linear-dimension gate still failed for a substantive reason:

```text
variables = 111
equations = 1087
rank = 108
signed affine dimension = 3
```

The preregistration expected affine dimension one. That expectation was too
strong because Gaussian elimination solves the equations over signed
rationals, while T1 concerns nonnegative probabilities. The two extra signed
directions cancel positive and negative masses. They are not probability
laws.

The campaign therefore did not promote the failed linear gate. It added an
exact positivity certificate:

1. the two-chain singleton mass is a linear consequence equal to zero;
2. the `V`-order chain restrictions give nonnegative zero sums, forcing each
   term to vanish and thereby killing antichain singleton mass;
3. every proper nonempty ideal has a convex boundary-pair restriction of one
   of those two types: an incomparable pair, or a cover relation obtained at
   the first exit from the ideal along a saturated chain.

The executable certifies all 1,304 proper ideals through four vertices. The
probability face is the one-dimensional empty/full mixture even though the
signed affine relaxation is three-dimensional. Positivity is load-bearing.

## 11. Exact results

### 11.1 Unmarked naturality collapses to an empty/full precursor mixture

For every finite unmarked poset `P`, covariance plus naturality under every
induced subset forces

$$
\kappa_P=(1-p)\delta_\varnothing+p\delta_P
$$

with one common `p`. The receipt independently checks the complete rational
system through three vertices and verifies the survivor through all 3,671
cuts of every labeled poset through four vertices.

This law has no proper precursor. Conditional on the full branch, the new
event has every old event in its past. This is global incidence, not a proved
physical outcome, transport process, or local interaction. `p` remains free.

### 11.2 Completion quotients diagnose a supplied law exactly

For both positive D3 weight laws, all 7,342 audited parent/cut/law contexts
satisfy

$$
P(D\cap K=A)
=
\frac{W_{P,K}(A)}{\sum_B W_{P,K}(B)}.
$$

After joint relabeling quotient, the pooled finite audit has 199 canonical
unmarked predictive classes and at most 42 targets for one retained unmarked
structure. Fixed-law canonical counts are `144/30` and `168/36`; the old
`756/66` values are labeled-cover pooled diagnostics only.

The decoder target is law-relative. On the same three-antichain cut to one point,

$$
P(\text{included})=\frac12
\quad\text{for }b=1,
\qquad
P(\text{included})=\frac9{14}
\quad\text{for }b=2.
$$

No-silent accounting can insist that this difference remain visible. It does
not derive which vector is correct before the law is supplied.

### 11.3 Fixed deterministic record capacity fails on growing chains

For the uniform D3 law on an `n`-chain retained to its minimal point,

$$
P_n(\text{included})=\frac{n}{n+1}.
$$

The 64 audited depths give 64 distinct exact deterministic token targets and
require at least six
bits. Nine depths already exceed a three-bit alphabet. Across unbounded depth,
no fixed finite deterministic mark alphabet is exactly sufficient.

A single `external-parent-present` flag fails immediately: the two-chain and
three-chain share the flag but require `2/3` and `3/4`.

This result does not forbid:

- an unbounded integer/rational mark at each finite cut;
- an expanding set of boundary records;
- approximate rather than exact prediction;
- a stochastic boundary channel whose context-dependent mixing weights carry
  the missing law;
- or a specially factorized law with a different finite sufficient state.

It says that a fixed deterministic finite alphabet cannot exactly repair the
registered D3 family on all chain depths.

### 11.4 Profinite marks relocate rather than erase the information

For every fixed modulus, two depths with the same residue have different
`n/(n+1)`. The full compatible residue tower can encode an unbounded integer,
but that inverse-limit point is not one finite record readout.

There is also a sharp standard-topology obstruction. The sequence `j!`
converges to zero in the profinite integers because it is eventually zero
modulo every fixed integer, while

$$
\frac{j!}{j!+1}\longrightarrow1
$$

rather than the depth-zero value `0`. Hence the exact chain prediction has no
continuous extension from the natural numbers to the standard profinite
integer completion. This does not rule out a different compact topology—for
example, one adapted to the ordinary large-`n` limit—or finite-stage
approximation.

## 12. Initial verdict

```text
ALL-SUBSET-UNMARKED-COLLAPSE
+ LAW-RELATIVE-UNBOUNDED-DETERMINISTIC-TARGET
```

No bounded record-local interacting extension law is selected. Strong
unmarked autonomy is too restrictive and leaves only global empty/full incidence;
the exact marked repair is circular with respect to law selection and exceeds
fixed deterministic capacity on the chain family.

## 13. Openings pinned before hostile round 1

1. verify the positivity certificate independently rather than equating
   signed affine dimension with probability dimension;
2. determine whether the `V`-order argument really transfers the chain refusal
   to every antichain pair;
3. audit all-subset naturality versus only embeddings/cuts physically licensed
   by marked diamonds;
4. test whether the completion vector is merely a renamed output law and state
   its minimal-sufficiency sense precisely;
5. attack the deterministic finite-alphabet assumption with stochastic marks,
   distributed boundaries, and unbounded but finite values;
6. check whether finite evidence implies a finite alphabet in the corpus or
   whether that is an additional operational assumption;
7. verify the factorial/profinite continuity argument and identify alternative
   compact topologies it does not exclude;
8. prevent the universal-precursor survivor from being called local merely because it
   is restriction-natural;
9. keep Barandes memory, no-silent boundary residue, and law derivation
   separate;
10. retain the complete refusal of cone, dimension, scale, continuum, and
    quantum promotion.

## 14. Hostile round 1 and opening dispositions

All three independent streams returned **MAJOR REVISION** while reproducing
the core empty/full collapse, positivity proof, law-relative witness, chain
lower bound, and standard profinite-integer discontinuity.

After every opening below was executed, the repaired receipt passes **23/23**
exact checks.

### O1 — restriction categories: classified where the unmarked arena is typed

The repaired receipt now distinguishes:

1. **all induced subsets:** signed affine dimension 3; positivity collapses
   to the empty/full universal-precursor mixture;
2. **convex subsets:** the same signed dimension 3 and the same positivity
   proof, because the point/chain/`V` cuts and every final
   cover-or-incomparable ideal-boundary pair are convex;
3. **ancestor-closed stems:** signed dimension 8; the deterministic
   `minimal-layer` ideal is a proper nontrivial natural law across all 1,789
   audited stem cuts;
4. **causal intervals:** signed dimension 8; independent Bernoulli mixtures on
   comparability components form a nontrivial family across all 2,210 audited
   interval cuts and fail the convex `V`-minima cut.

Thus the collapse is a theorem about silent all-subset or convex autonomy,
not locality in general. Causal intervals here mean empty/full identity,
singletons, and closed order intervals with comparable endpoints.

Collar-complete and typed direct-carrier cuts are not objects of the unmarked
poset category. D4 refuses to fabricate their classification; they require a
marked diamond proposal.

### O2 — no-silent trichotomy: frozen

Every proposed physical cut must be typed as one of:

- **autonomous:** the retained state alone obeys a proved natural kernel;
- **boundary-conditional:** an explicit retained carrier `m` is supplied and
  the decoder uses `(law L, retained state S, m)`;
- **refused:** no permitted sufficient retained state exists, so the cut is
  not a complete local experiment.

The empty/full theorem concerns the first sector with no marks. The completion
quotient diagnoses the second but does not build its carrier. Arbitrary cuts
may belong to the third.

### O3 — completion vector: downgraded to a decoder target

The normalized completion vector `q` is no longer called a born boundary
record. For fixed supplied law `L`, retained structure `S`, and visible
precursor alphabet, it is a canonical representative of the coarsest exact
deterministic predictive partition:

$$
F_L(S,m(c))=q_c.
$$

This does not give a carrier, provenance, encoder, update rule, nested-cut
composition, or sufficiency for outcomes/rates/holonomy. Those are mandatory
future construction gates.

The repaired receipt independently rebuilds the direct pushforward and
completion aggregation. It also separates presentations:

```text
fixed-law labeled-cover classes/max:  b=1 -> 564/42; b=2 -> 601/45
fixed-law canonical classes/max:      b=1 -> 144/30; b=2 -> 168/36
pooled labeled union:                 756/66
pooled canonical unmarked union:      199/42
```

Only the fixed-law, fixed-retained-structure equality classes support the
minimality statement. Pooled counts are diagnostics of law dependence.

### O4 — positivity and executable decoupling: repaired

Every proper ideal now records a convex inside/outside boundary pair, its
induced chain/antichain type, and the projected singleton fiber. The 1,304
certificates split exactly 616 cover-chain / 688 antichain. Completion
pushforwards are rebuilt through an
independent enumeration/component/projection path. Chain predictions are
recovered from explicit prefix ideals rather than inserted as `n/(n+1)`.

### O5 — operational capacity axiom: explicit and additional

The fixed-alphabet theorem now assumes:

1. one pre-sampling boundary token;
2. deterministic encoding from the complete cut context;
3. one uniform finite alphabet over all depths;
4. a decoder that knows the fixed law and retained state but receives no
   depth, global clock, or other context except through the token;
5. exact zero-error precursor prediction.

This is a worst-case per-token capacity axiom. It is not derived from finite
KL/evidence weight, Shannon entropy, or the v6 binary event capacity.

### O6 — loophole models: formalized, not dismissed

The repaired receipt exhibits four escapes:

- a binary stochastic mark with context-dependent mixing probability `q_n`;
- a distributed six-bit encoding of depths 1–64;
- an unbounded integer mark `n`, finite at every finite depth;
- an approximate tail bin: predicting one beyond depth 99 has error at most
  one percent.

Each evades the exact fixed-token count by relocating the global dependence,
growing total capacity, allowing an unbounded alphabet, or weakening exactness.
None is thereby a local compositional law.

### O7 — profinite ceiling: repaired

The receipt now labels its factorial calculation a finite shadow: exact
divisibility and strictly decreasing errors through `8!`, terminal error
`1/40321`. The all-modulus convergence and discontinuity conclusion come from
the analytic proof. Claims remain restricted to the standard profinite
integer completion and continuous real readouts. No conclusion is drawn for
the v9 stem spectrum or every compact/Stone topology.

### O8 — terminology and geometry: repaired/preserved

The theorem object is the **empty/full universal-precursor mixture** or
**global-incidence branch**. No physical process is inferred from incidence
alone. No geometry, quantum, continuum, dimension, cone, or scale promotion
is made.

## 15. Round-2 claim submitted for review

```text
STRONG UNMARKED ALL-SUBSET/CONVEX AUTONOMY
    -> EMPTY/FULL UNIVERSAL-PRECURSOR MIXTURE
STEM/INTERVAL RESTRICTIONS
    -> NONTRIVIAL FAMILIES SURVIVE
SUPPLIED NON-NATURAL LAW
    -> LAW-RELATIVE PREDICTIVE DECODER TARGET
FIXED DETERMINISTIC TOKEN
    -> UNBOUNDED EXACT STATE REQUIREMENT ON CHAINS
```

No carrier-producing update or final interacting click law is claimed.

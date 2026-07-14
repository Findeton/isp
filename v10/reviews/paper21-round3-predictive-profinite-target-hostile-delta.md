# Paper 21 round 3 — predictive/profinite target hostile delta

**Frozen target:** commit `caaba6e`, restricted to the new section 10,
renumbered sections 11–13, and their status/verdict cross-references in
`relativistic-isp-v10-paper21-local-generators-do-not-imply-local-memory.md`.

**Verdict:** **D34d CORE UNCHANGED; NEW D34e TARGET REQUIRES MAJOR REVISION —
0 BLOCKER / 3 MAJOR / 3 MINOR / 0 NIT.**

The accepted D34d theorem, exact probabilities, receipt hashes and terminal
noun are unchanged.  I did not rerun the frozen executables because the delta
modifies only paper prose and contains no changed numerical claim.  The new
target has the right hierarchy and the correct sufficiency/minimality
implication directions.  Three load-bearing interfaces are nevertheless not
yet exact: a passive history measure does not specify interventional response
laws; a current prefix does not determine a point of v9's completed-history
stem spectrum; and a finite enumeration does not prove bounded-future
sufficiency over unbounded current pasts.

## 1. What survives hostile audit

### 1.1 Predictive quotient and carrier directions

At a fixed law/query/scope, the relation “same conditional law for every
licensed future” is an equivalence relation.  The carrier directions in
section 10.2 are correct:

```text
B(h)=B(h')  =>  h ~pred h'
```

is sufficiency, because the boundary partition refines the predictive
partition.  The converse is not needed for sufficiency; requiring it makes the
two partitions coincide and removes carrier redundancy.  Thus the paper does
not reverse minimality, and it correctly says a sufficient carrier may retain
extra information.

The physical anti-cheating clauses also survive.  A real-valued Gödel code of
the whole past is not silently treated as a finite record; continuous and
unbounded fields must be disclosed; finite click rank is not promoted to a
uniform boundary-memory bound; and sealed data may be discarded only after
its future-relevant influence is represented at the boundary.

### 1.2 Desired carrier theorem

Screening, recursive closure, construction covariance, typed composition,
minimality and physical capacity are the right six distinct gates.  A
same-carrier/different-future pair is the right form of obstruction.  The
D34d `1/4 -> 1/8` specimen really does refute A's private one-record state for
a query class containing A's next wire event.

### 1.3 The two inverse structures are correctly distinguished

The prose correctly says that:

- the labeled committed-prefix system concerns sequential online pasts;
- v9 covtree levels resolve completed histories by their exact-rank stem
  theories;
- covtree rank is not a click count;
- topology alone selects neither `mu` nor an encoder;
- continuous/unbounded marks do not become profinite without finite
  quotients or a separately declared compact marked topology.

Those refusals are important and correct.  The major finding below is that the
proposed *bridge gates* do not yet respect the same distinction.

### 1.4 Finite-horizon ceiling and status bookkeeping

The section correctly says that finite-horizon observations cannot simply be
extrapolated to all licensed futures, and that D34e is a pinned target rather
than a D34d result.  Sections 11–13 are renumbered consistently.  The status
line and final verdict preserve all three clean round-2 deltas and do not
claim that D34e has run.

## 2. MAJOR findings

### M1 — one passive history measure does not define intervention-indexed laws

Section 10.1 fixes a complete marked history measure `mu`, then lets `Q_A`
contain future **interventions** and defines `Law_mu(q | h)`.  A single passive
measure supplies regular conditional laws for future *events or random
variables under that same measure*.  It does not in general say what happens
under a counterfactual intervention that changes the transition or quantum
instrument.  The probability that an intervention label happens to occur
under `mu` is not the outcome law conditional on deliberately applying that
intervention.

This distinction is load-bearing in section 10.5: operational quantum
predictive equivalence is defined by outcome statistics for every licensed
instrument sequence, which requires a process tensor/comb or an equivalent
intervention-indexed causal family.  The classical analogue likewise needs a
controlled transition family if D34e is to vary interventions rather than
merely inspect passive future events.

**Required repair:** choose and state one of two exact scopes.

1. **Passive scope:** let `Q_A` be a measure-determining class of future events
   under `mu`, and define equality of the regular conditional kernels
   `K_t(h,.)=mu(future in . | F_t)(h)` restricted to those events.
2. **Operational scope:** supply a causal family
   `{K_t^I(h,.) : I in I_A}` indexed by licensed intervention policies or
   instruments, and define

   ```text
   h ~ h' iff K_t^I(h,.) = K_t^I(h',.) for every I in I_A.
   ```

   In the quantum branch this family is the process object whose existence is
   presently open; it cannot be derived from the classical D34b `mu` by
   notation.

Separate the passive D34b campaign from any operational/quantum extension,
or declare the controlled law as additional input.  Until then the displayed
equivalence is ill-typed for the intervention reading advertised by the text.

### M2 — a finite online past is not a point of the v9 stem spectrum

V9's evaluation map has the form

```text
phi : completed causal histories -> X_stem,
```

where `X_stem` records the complete history's answers to stem-occurrence
questions.  Section 10.1's predictive kernel instead has a **current complete
past/prefix** as its argument.  A finite prefix has many possible completions
and therefore does not canonically determine one `phi`-value.  In particular,
absence of a stem is not certified by any finite prefix: a later growth can
create it.  Reading a completed-history spectrum point as a current boundary
state would leak future information.

Consequently section 10.4 gate 3—future laws constant on “the stem-spectrum
fibers being identified”—is not yet a well-typed condition on the predictive
quotient of finite pasts.  Stem-spectrum fibers compare completed histories;
predictive equivalence compares present pasts by their distributions over
possible futures.  Rogue fibers matter to a completed-history lift, but they
do not by themselves supply an adapted state at time `t`.

For a supplied completed marked-history measure and an explicit forgetful map
to the unmarked v9 arena, the canonical online object is instead a conditional
**measure** on the spectrum,

```text
nu_t(h) = phi_* mu(completion in . | F_t)(h),
```

when the relevant regular conditional kernel exists.  At covtree level `n`,
the adapted datum is generally the probability vector
`nu_(t,n)=(pi_n)_*nu_t`, not a single covtree node.  These vectors obey the
finite-level pushforward compatibility maps by construction.  Whether they
screen the declared regional futures is an additional sufficiency theorem.

**Required repair:** replace the present bridge list by an explicit commuting
diagram with separately typed domains:

- completed marked history space and its natural prefix filtration;
- an explicit mark-forgetting/causet map;
- v9's Borel evaluation map `phi` to the completed-history stem spectrum;
- the predictive conditional kernels on prefix histories;
- either the posterior kernel `h -> nu_t(h)` into probability measures on
  `X_stem`, or a separately proved **adapted** map from current records to a
  new finite/profinite predictive carrier.

Then distinguish three different possible claims:

1. a future observable factors through completed stem data;
2. an online predictive kernel factors through the posterior `nu_t`;
3. an online boundary state itself has a compatible finite/profinite
   realization.

They are not equivalent.  A projective family of new predictive partitions
creates its own inverse limit; identifying it with v9 `X_stem` requires
commuting finite-level maps and an adaptedness/no-future-leakage proof.

The continuity clause also needs typing.  The v9 `phi` is Borel but generally
not continuous.  Measurable `mu`-almost-sure factorization requires
sigma(`phi`)-measurability/sufficiency, not “cylinder continuity.”  A stronger
continuous profinite realization may be requested separately.  Even a
continuous `[0,1]`-valued conditional probability on a Cantor/profinite space
need not factor **exactly** through one finite level; finite-level locally
constant functions may only approximate it.  No existence, continuity or
finite-factor claim should be inferred merely from compatible finite tests.

### M3 — the finite campaign's sufficiency claim omits the current-past bound

Section 10.6 correctly refuses promotion from finite future horizons to all
futures, but its final paragraph still says the finite campaign can establish
“bounded-horizon sufficiency.”  Exhaustive enumeration at a finite current
web size proves sufficiency only on that registered finite domain.  A future
horizon of one or two events does not make the set of possible **current
pasts** finite when the grown web is unbounded.

The asymmetry is important:

- one reachable same-carrier/different-future witness refutes a proposed
  carrier globally at the declared query scope;
- failure to find a witness through current size `N` does not prove the
  carrier sufficient for larger current histories, even when the future
  horizon `H` is fixed;
- recursive update and composition of a survivor do not alone prove
  screening unless an induction shows the predictive law factors through the
  state at every reachable size.

**Required repair:** preregister a finite audit domain
`D(N,H,Q,I)` containing a maximum current-past size `N`, future horizon `H`,
query set and, if applicable, intervention set.  State that enumeration earns
only `D(N,H,Q,I)`-sufficiency.  Promotion in either direction needs a theorem:

- arbitrary current size: an induction/closure proof of screening on all
  reachable histories;
- arbitrary future horizon: compatible finite-horizon kernels plus a theorem
  identifying the limiting law, or exact stabilization with proved closure.

Also require the horizon/query families to be nested before saying that their
equivalence partitions “refine” as the horizon grows.

## 3. MINOR findings

### m1 — “canonical” must be almost-sure or pointwise-kernel scoped

The paper correctly notes that null histories require a declared conditional
version, but it then calls the resulting class canonical.  Regular conditional
probabilities are unique only `mu`-almost surely.  Changing a version on a
null set can change pointwise predictive classes there; in continuous time,
individual exact histories typically have probability zero.

**Required repair:** state either that predictive equivalence and sufficiency
are `mu`-almost-sure notions, or supply a canonical pointwise generator/
controlled kernel on all declared legal states.  Exact obstruction witnesses
must be reachable/positive-cylinder witnesses, or be evaluated by that
declared pointwise kernel—not manufactured by arbitrary values of a regular
conditional version on unsupported histories.

### m2 — setwise recoverability needs a measurable physical decoder

The implication in section 10.2 is set-theoretically correct, but
“equivalently, the predictive quotient must be recoverable” is stronger if
recoverable means a physical random state.  Constancy on fibers defines a set
function from boundary messages to predictive classes; it does not by itself
prove that the decoder or quotient realization is measurable.

**Required repair:** formulate screening directly as measurable kernel
factorization,

```text
K_t^I(h,.) = Kbar_t^I(B_A(h),.)    mu-a.s. for every licensed I,
```

with measurable encoder and decoder on declared standard-Borel/finite carrier
spaces.  Exact minimality then additionally requires equality of the two
fiber relations and a measurable relabeling/gauge-respecting isomorphism on
their realized images.

### m3 — restriction maps are not “strongly positive” objects

Section 10.5 asks whether quantum restriction maps “remain strongly
positive.”  Strong positivity is a property of a decoherence functional (all
finite event matrices are positive semidefinite), not normally a property of
a restriction map.  Quantum process restriction/coarse-graining maps instead
need the appropriate linearity, complete positivity, causal normalization and
projective compatibility; the induced finite decoherence functionals must
remain strongly positive.

**Required repair:** assign complete positivity/normalization/compatibility to
the maps and strong positivity to the restricted functionals or process
matrices.

## 4. Exact revised ceiling

The new section can become a rigorous D34e pin after the three major domain
repairs and three minor typing repairs.  The supported target is:

> For a declared passive or controlled history-law family, compute finite
> law-relative predictive partitions on an explicitly bounded audit domain;
> refute candidate record carriers by reachable exact witnesses; and seek a
> measurable, recursively closed, typed boundary factorization valid on all
> reachable histories.  Separately determine whether the online past induces
> a sufficient posterior or adapted carrier over a marked extension of v9's
> completed-history stem spectrum.  No profinite bridge, continuity,
> projective limit, all-size sufficiency or quantum boundary process is
> presumed.

This revision does not reopen Paper 21's accepted D34d scientific core.

**Final count: 0B / 3M / 3m / 0n.**

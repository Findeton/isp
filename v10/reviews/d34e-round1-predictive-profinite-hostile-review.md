# D34e round 1 — predictive/probability/profinite hostile review

**Frozen target:** commit `a880e62`:

- `note-d34e-predictive-record-dag-boundary.md`;
- `code/d34e_predictive_boundary_exact.py`;
- `data/d34e_predictive_boundary_exact.out`.

**Verdict:** **MAJOR REVISION — 0 BLOCKER / 2 MAJOR / 1 MINOR / 1 NIT.**

The central structural discovery survives: for the chosen static D34b law, the
coarse degree histogram and the role-labeled incident star have exact generator
rows independent of hidden remote configuration, and the B0/B1 obstructions
are arithmetically correct.  The finite v9 experiment also stays within its
declared nonclaim.  The provisional `11/11` cannot yet be terminal, however.
The all-future carrier omits the current construction-time coordinate required
by its own absolute-time readout at random regional stops, and E4's purported
finite predictive signatures bake raw successor states into the signature and
are not predictive-equivalence classes on the registered `D(N,H)` domain.

## 1. Reproduction and independent attacks

### 1.1 Fresh-salt reproduction

Fresh runs under `PYTHONHASHSEED=79,99991` both exit zero and are byte-identical
to the committed output.  The reproduced hashes are:

```text
code SHA-256   53205d8a412b63bc0382f6ee6f7e2c3d2570105ecd54b684c66b1e02afa20f47
output SHA-256 81dc0a289631f97961a661fda9ce3b3aed36b40e298024173cbc693998eb2586
summary digest 48d83ba568052d4822278f43efe0c3a268e268e6372e642219b6b400c027d3fd
```

All printed fractions and the 100-decimal exponential regression reproduce.

### 1.2 Beyond-depth-four regression

I extended the executable's literal full-state enumeration by one global
embedded event and re-ran both projected-row comparisons on every state.  The
level counts are

```text
(1, 6, 40, 304, 2576, 23800),
```

or `26,727` states cumulatively through depth five.  Both tests remain true:

```text
global projected histogram row = analytic histogram row,
global projected labeled-star row = analytic labeled-star row.
```

This is not the all-depth proof, but it is a genuine fresh attack beyond the
frozen receipt's `N=4` and found no hidden transition.

### 1.3 Independent arbitrary-depth row exhaustion

The analytic partition itself survives re-derivation.  For any finite legal
D34b configuration, an event can alter A's coarse state `(c,h)` only in the
following exhaustive cases:

1. A births: rate `1/4`, add one degree-one neighbor;
2. A idles: rate `1/2`, emit the idle mark;
3. A interacts outward: aggregate rate `1/4`, toggle A's carrier;
4. one current degree-`k` neighbor births: aggregate rate `n_k/4`, move one
   count from `k` to `k+1`;
5. one degree-`k` neighbor interacts into A: aggregate rate `n_k/(4k)`, toggle
   A's carrier.

Births elsewhere do not change the degree of an A-neighbor; interactions do
not change adjacency; and neighbor carrier/tip changes are deliberately absent
from C/L.  Thus every other global row is silent for these queries.  The same
argument with persistent incident identities gives the labeled-star rows.

The projected relevant intensity satisfies

```text
q(c,h) = 1 + d/4 + sum_k n_k/(4k) <= 1 + d/2,
```

where A's incident count `d` increases only through A's rate-`1/4` birth
process.  Hence the projected row system is nonexplosive directly; inherited
D34b nonexplosion is consistent with, but not the only route to, uniqueness.
This validates the strong-lumping promotion for the **relative-time marked
boundary process**, subject to M1's missing scope coordinate.

## 2. B0/B1 probability audit — pass

### 2.1 One-record obstruction

When B has only A as neighbor,

```text
rate(B -> A) = 1/4.
```

After B births one child, A's private actor row and A tip are unchanged while
B's degree is two, so

```text
rate(B -> A) = 1/8.
```

The receipt constructs exactly this pair.  B0 is refuted for any future query
containing the next A-wire event.

### 2.2 Equal current rate, unequal future law

For

```text
H  = {2,3,6},
H' = {2,4,4},
```

both A degree and current aggregate incoming rate agree:

```text
sum_(k in H) 1/k = sum_(k in H') 1/k = 1,
f(H)=f(H')=1/4.
```

Only A births and neighbor births change `f`.  Therefore

```text
L f = 1/16 - sum_k n_k/[16 k(k+1)],
L f(H)  = 61/1344,
L f(H') = 11/240,
L f(H')-L f(H) = 1/2240.
```

For the incoming counting process,

```text
E_h[N_in(t)] = f(h)t + (L f)(h)t^2/2 + o(t^2),
```

so the two conditional future laws differ no later than the quadratic term;
the coefficient gap is `1/4480`.  Equality of the entire future law would
force equality of this expectation.  Both constructed histories have positive
exact embedded cylinder mass, and their A-local counters/tip can be chosen
identically.  This is a valid all-future obstruction to B1, not merely a
numerical difference between presentations.

**Disposition:** E3's fractions, reachability and interpretation pass.

## 3. MAJOR findings

### M1 — absolute construction time is in the query but absent from the carrier

Branch C explicitly retains **construction time** on every future A-wire
record.  The theorem is claimed at three stopping scopes: fixed `T`, A-own-ring
stops and A-wire-event stops.  Yet the states actually proved lumpable are

```text
(A carrier, neighbor-degree histogram)
```

and

```text
(A carrier, A birth ordinal, labeled neighbor degrees).
```

Neither contains the current construction time `tau`.  The executable has no
event timestamps, and E4 checks only one relative waiting-time survival value
plus a hand-written counter-update dictionary.  The unused
`boundary_scoped()` helper also returns the wire count twice and does not test
the declared scoped state.

For a fixed deterministic `T`, the omitted coordinate is harmless because all
compared histories share the same external parameter.  It is not harmless at
the `m`th A-own or A-wire stop.  Two stopped histories can have the same
histogram/star and counters but different realized stop times `tau != tau'`.
Time homogeneity makes their future **increments** identically distributed,
but their future absolute timestamps are shifted by `tau` and `tau'`.
Therefore they are not predictively equivalent for the query as frozen.

The same seam affects the capacity statement.  The continuous-time branch
either carries one exact continuous coordinate or declares time-translation
gauge/elapsed-time output.  It cannot both retain absolute construction time
and report only the embedded discrete carrier.

E4's formula

```text
P(no relevant boundary transition in Delta t | B)=exp[-q(B) Delta t]
```

is correct: silent remote rings leave both `B` and `q(B)` unchanged.  It is the
survival to the next **boundary transition**, not by itself the distribution
to the next A-wire event, because intervening neighbor births change the
future A-wire hazard.  The complete boundary CTMC can handle that stopping
time, but the receipt does not currently carry the stopped-process argument.

**Required repair:** choose and gate one exact convention for each stopping
branch.

1. If future records carry absolute construction times, augment B2/B3 by the
   current `tau` (or prove it is physically read from a declared A-tip record),
   include the continuous coordinate in the capacity ledger, and compare
   stopped histories only with that coordinate present.
2. Alternatively define the future time readout as elapsed increments from
   the stop and state the time-translation identification explicitly.
3. Append A-own and A-wire counters to the projected states used by the
   theorem, repair/use the scoped projection, and prove their deterministic
   update rows rather than only printing a dictionary.
4. Invoke the strong-Markov/hitting-time theorem for A-own and A-wire stopping
   scopes and state that the simple exponential is for the next full boundary
   transition; derive other stopped laws from the CTMC.

Until then, E6 earns an all-future strong-lumping theorem for the embedded or
relative-time C/L process, not the complete timestamped query at every frozen
stopping scope.

### M2 — E4's “signature classes” are state-labeled fingerprints, not finite predictive classes

The finite protocol freezes `D(N=4,H=3,...)` and says finite signatures are
only bounded-domain predictive evidence.  The implementation does not compute
that object.  Its recursion stores

```text
(output label, rate, raw successor boundary, successor signature).
```

Including the raw successor boundary before quotienting makes distinct carrier
states distinct even when their future output laws agree at the audited
horizon.  The reported `(110,110,110)` therefore cannot test predictive
merging or horizon refinement.  It is a labeled transition-tree fingerprint.

An independent coinductive calculation on the same 110 synthetic boundaries,
starting with all states equivalent at horizon zero and aggregating rates only
by

```text
(output label, previous-horizon successor class),
```

gives

```text
predictive class counts at H=1,2,3: (106,110,110).
```

In particular the registered B1 pair is equal at horizon one and splits at
horizon two, exactly as its `Lf` witness predicts.  The current routine misses
that diagnostic because it inserts `after` directly.

There is a second domain mismatch.  `audit_boundaries` includes synthetic
stars with up to three neighbors and degrees up to five—many require more than
four past events—while it omits other states reachable in the declared global
`N=4` domain.  It is neither the set of histories nor the set of projected
states of the registered `D(N=4,...)` cell.  The genuinely reachable depth-0
through depth-4 enumeration has 29 distinct coarse dynamic boundaries before
stopping counters are appended.

**Required repair:** either:

1. implement the actual finite predictive partition on a precisely registered
   `D(N,H,Q,S)` history/state domain, using output/rate plus successor **class**
   and aggregating rows that enter the same class; or
2. relabel E4 as a synthetic state-labeled transition fingerprint, remove the
   predictive-class/refinement reading and do not attach `D(N=4)` to it.

Because D34e's stated task is to find the predictive quotient, the first route
is preferred.  The code, output hash, summary digest and provisional `11/11`
must be regenerated.  This does not refute the analytic strong-lumping proof,
but it does make one frozen exact receipt gate false as described.

## 4. Continuous-time and stopping audit beyond M1

The current no-boundary-event calculation is otherwise correct.  For both B1
witnesses,

```text
d=3, f=1/4, q=1+d/4+f=2,
P(no boundary transition for 1.375)=exp(-2.75)
 = 0.063927861206707572702430025557951749308634...
```

Exponential memorylessness means no residual ring-age vector is needed for
the chosen law.  This conclusion would fail for the renewal-clock control from
D34d, but D34e does not import that control into its theorem.

The counter increments printed in E4 are also arithmetically correct:

```text
A birth/idle/outgoing: (own-ring,wire) += (1,1),
incoming-to-A:         (own-ring,wire) += (0,1),
neighbor birth:        (own-ring,wire) += (0,0).
```

They need integration into the actual lumped state and stopping proof under
M1; they do not require a different generator.

## 5. Finite `u`, stem spectrum and profinite ceiling — pass with m1

E9 proves only the finite diagram it actually constructs:

- finite marked event prefixes forget to finite past-finite event orders;
- the depth-four **labeled-prefix truncation**, followed by unmarked
  pushforward, reproduces the depth-three unmarked marginal;
- the one-event unmarked order does not determine the marked A-carrier output.

The path counts `400/4440` and unmarked-class counts `4/10` reproduce.  Nothing
in the executable constructs a completed-history map, an adapted posterior
`nu_tau`, a covtree filtration, a marked profinite topology or a
posterior-sufficiency theorem.  The note and output explicitly refuse all of
those promotions.  This ceiling is scientifically correct.

### m1 — state the finite pushforward diagram rather than implying an unmarked restriction map

An unlabeled four-event isomorphism class does not in general remember which
maximal event was the committed last event, so there is no canonical map from
the ten printed unmarked depth-four classes to the four depth-three classes.
The code does the correct operation pathwise:

```text
(u_3 o r_(4->3))_* mu_4 = (u_3)_* mu_3,
```

where `r_(4->3)` acts on the labeled committed prefix before `u_3` forgets the
labels.  It does **not** test `rho_* (u_4)_*mu_4` for an unmarked restriction
map `rho`.

**Required repair:** print/name this commuting labeled-truncation pushforward
diagram in E9 and section 15.4.  Retain the existing statement that it is not a
v9 posterior/profinite theorem.

## 6. Remaining claim audit

### 6.1 Branch F

The radii `0..3` witnesses reproduce, and the all-`r` construction is sound.
At radius `r`, the outside actor and its leaf give two identical radius-`r`
views; `r+1` inward interactions carry the immutable differing predecessor to
A.  With `r+3` active actors and every inward initiator of degree two, the
embedded future-cylinder mass is

```text
[1/(8(r+3))]^(r+1) > 0.
```

The result refutes the fixed-radius candidate class for full ancestry.  It
does not prove whole-component necessity, and the note correctly keeps only a
whole-component sufficient upper bound.

### 6.2 Capacity

A's rate-one rings thinned by the birth mark give a rate-`1/4` Poisson birth
process.  Consequently A's incident-port count has unbounded support at every
positive `T` and diverges almost surely as `T` tends to infinity.  B3 is an
unbounded-width physical realization.  This does not exclude every clever
bounded carrier, and the note does not claim such a universal no-go.

### 6.3 Quantum

The intrinsic operational branch correctly returns `REFUSAL/UNDEFINED`.
Finite D34c functionals and the auxiliary `P,E` diagnostic do not supply a
timed intervention-indexed D34b–D34c process, and no SHARD quantum width is
assigned.

## 7. NIT

### n1 — the top status is stale historical-pin prose

The note still opens with “preregistration before D34e receipt code” and says
the executable/receipts do not exist, while section 15 contains their current
provisional result.  Preserve the historical pin, but label it explicitly and
put the present status at the top, e.g. “historical preregistration through
section 14; provisional 11/11 receipt in section 15; hostile round 1 pending.”

## 8. Opening ledger

| Opening | Round-1 disposition | Required next action |
|---|---|---|
| O-D34e-1 — does the generator projection fail just beyond `N=4`? | **Investigated; survived.** Both projections pass on 23,800 depth-five states. | Keep the depth-five audit as an independent review receipt; the analytic proof remains load-bearing. |
| O-D34e-2 — can an omitted remote event alter the C/L row later? | **Investigated; no.** Static adjacency and degree-only targeting exhaust the five row types. | State the arbitrary-state strong-lumping proof formally and include the direct nonexplosion bound `q<=1+d/2`. |
| O-D34e-3 — absolute versus elapsed construction time | **Opened and failed as written (M1).** | Add `tau`/tip time or quotient by time translation; then prove the regional stopped kernels. |
| O-D34e-4 — finite predictive partition | **Opened and failed as implemented (M2).** Correct synthetic counts are `106,110,110`, not the receipt's predictive reading of `110,110,110`. | Replace raw successor states by previous-horizon equivalence classes and use a registered domain. |
| O-D34e-5 — is B2 minimal for Branch C? | **Still open and correctly unclaimed.** | After M2, test whether distinct histograms remain equivalent at every horizon; prove or refute infinite-horizon injectivity. |
| O-D34e-6 — can any uniformly bounded physical carrier replace unbounded B3? | **Still open and correctly unclaimed.** | Define the admitted finite record-carrier class before attempting a no-go; unbounded B3 alone is not one. |
| O-D34e-7 — finite `u` to v9 posterior | **Finite prefix gate passes; completed bridge open.** | Construct/gate completed `u`, Borel coding and `nu_tau`; then test posterior sufficiency separately. |
| O-D34e-8 — stopped A-own/A-wire laws | **Not established by E4's counter table.** | Derive them from the repaired marked CTMC and its strong-Markov hitting times. |

## 9. Exact revised ceiling

The evidence presently supports:

> For the chosen static D34b law, the histogram and role-labeled distributed
> star are exact nonexplosive strong-lumpings of the coarse **relative-time**
> marked boundary generator, at arbitrary finite global configurations.  B0
> and the instantaneous B1 rate summary fail exactly.  The physical star has
> unbounded width.  Full ancestry defeats every fixed actor radius.  Only a
> finite labeled-prefix-to-unmarked pushforward has been built; no v9 posterior
> factorization or intrinsic quantum boundary exists.

Promotion back to the frozen absolute-timestamp, all-stopping-scope C/L noun
requires M1.  The finite `D(N,H)` evidence and `11/11` receipt require M2.

**Final count: 0B / 2M / 1m / 1n.**

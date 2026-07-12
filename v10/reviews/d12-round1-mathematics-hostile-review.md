# D12 hostile round-1 mathematics / probability review

**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION**  
**Protocol verdict supported by the present artifacts:** `INCOMPLETE-INVESTIGATION`  
**Finite counterexample algebra:** confirmed  
**Claim that the frozen U0–U8 investigation has been executed:** not confirmed

## Bottom line

D12's central negative insight is mathematically sound: neither complete
finite-history bookkeeping, unitarity, exchange symmetry, number conservation,
least action without a specified action, nor maximum entropy without physical
constraints selects a unique interaction law.  The exact `P_r` and iSWAP
calculations support that statement.

The paper nevertheless grades itself one level too highly.  Its protocol says
`INCOMPLETE-INVESTIGATION` whenever a promised object, alternative class, or
decisive gate has not been executed.  The restored-process executable does not
instantiate the protocol's minimum diamond packet, does not construct a
multi-diamond projective process, does not implement the canonical-fiber
construction gauge, does not perform independent vertex-frame transport, and
does not run 256 physical commits.  It checks exact but small algebraic cells
and then assigns those cells the names of the full gates.  Theorem 3 consequently
asserts that its two models satisfy more premises than the artifacts establish.

This is repairable without abandoning the strongest result.  Narrow the theorem
to the actually shared, actually implemented premises, or construct two complete
U0–U7 models and execute U8.  Until one of those repairs is made, the final
verdict must be `INCOMPLETE-INVESTIGATION`, not
`UNIVERSAL-FORM/PRIMITIVE-PROCESS-REMAINS`.

## Frozen sources and independent reproduction

I reviewed the following frozen artifacts and independently matched their
SHA-256 hashes:

```text
e5a8a50ffe03459cf62ca5b5168fd48079c6309fb3ae7ac2d7310203c1669b1f  code/d12_diamond_law_nonuniqueness_exact.py
34215f2605f68029e4bce59c9e471d8af5892269d6b4b0ee7ac0193f67fe55dc  code/d12_symmetric_interaction_family_exact.py
0cfd533c70d29b3f82107927cb7d96b9333af185de57d3161e36800cdb4118fa  code/d12_restored_diamond_process_exact.py
88142db43046b729bb88b4d5fd2fe345384d2431a6c239e91419a02b748de5b8  note-d12-diamond-restoration-uniqueness-protocol.md
a2f4feca2e2b689979c7794e2547c041890dac1f50d6dfaf73da79dc900aa8a5  note-d12-v6-v10-compatibility-ledger.md
a367cf1bc613fb68db39c872579da4dc7d9e0f85ed9df1aa0614d118c8219c74  note-d12-extension-law-characterization.md
f902092529a458c46e04cc0fb1249f9b3eb17b2f612a7444063fb59266d9b567  note-d12-selection-principle-audit.md
357f8d2e9320e91a5847dfd3c7a3036c9c724ffc5d3de15e2016cb9d4e04e399  note-d12-geometry-consequence-gate.md
ed40587879c7cdbd6259bb65a84cf63e77aed382021ad1530655aea601c8980d  relativistic-isp-v10-paper13-the-click-law-is-the-whole-history-process.md
```

All three executables were run under ordinary Python and `python -O`.  Each
normal/optimized pair was byte-identical, with independently reproduced stdout
hashes:

```text
nonuniqueness: checks=42
  ffaf1bb6bb8125ca4f4d08d048d8828f6c48b81eb5e99f14ba6b0b3f8621ff7d

symmetric interaction family: checks=18
  a2da06a85371f83de4b22047f734747a988254cfce887039563b34161b3ba73f

restored process: checks=25
  7d97f74d547ca13aab6d4978a69732afe27caf0568a2394b512da2e000237586
```

The three semantic receipts also match the pre-review receipt exactly.  This
confirms deterministic execution and faithful hashing.  It does not establish
that a check bearing the name of a protocol gate implements the quantified
content of that gate.

## 1. The classical `P_r` witness

For

$$
P_r(x,y,z)=\frac{1+rxyz}{8},\qquad x,y,z\in\{-1,+1\},
$$

strict positivity holds for `|r|<1`; normalization follows because the triple
character sums to zero.  Every one- and two-coordinate marginal is uniform.
But

$$
P_r(z=1\mid x,y)=\frac{1+rxy}{2},
$$

so the law is not first-order Markov in the order `x,y,z` whenever `r != 0`.
For `r=1/2` and `r=1/3`, the probability at `x=y=z=1` is respectively `3/16`
and `1/6`, and the corresponding conditional probabilities are `3/4` and
`2/3`.  The production results are exact.

### Opening M1 — a three-variable law is not yet a whole-history process

The script constructs one law on three variables, its subset marginals, an
independent neutral-bit refinement, and an independent product gluing.  This is
a finite projective diagram.  It is not by itself a compatible family on all
finite time cylinders, much less a continuing typed-diamond history process.
The receipt's `whole_history_projective_twins=PASS` and Paper 13's phrase
"complete projective non-Markov history structure" therefore outrun the
witness.

The distinction is not pedantic.  Egri et al.,
[arXiv:2602.23491](https://arxiv.org/abs/2602.23491), distinguish a trajectory
of one-time probabilities from a probability measure on trajectories and show
that implementations are generically nonunique.  D12 conceptually chooses the
right category when it treats the process measure as primitive and obtains
next-click kernels by disintegration; it does **not** make the category error of
reconstructing joint histories from a mere sequence of marginals.  But the
`P_r` executable still supplies only one finite history law, not the advertised
projective process family.

**Required repair:** give explicit spaces `Omega_n`, truncations
`pi_{n+1,n}`, and laws `P_r^(n)` for every `n`, and prove
`(pi_{n+1,n})_*P_r^(n+1)=P_r^(n)`.  A minimal existence witness is an infinite
product of independent three-click `P_r` blocks, with prefix marginals used for
arbitrary `n`.  If time homogeneity, connected diamond continuation, or a
nontrivial long-memory tail is intended, those stronger properties require a
less artificial construction and separate checks.

The neutral refinement currently checked is mathematically valid but weak: any
finite law can be extended by an unrelated fair bit.  It does not prove
projectivity under the physically allowed diamond truncations.

## 2. The iSWAP family

For

$$
U_\theta=
\begin{pmatrix}
1&0&0&0\\
0&\cos\theta&i\sin\theta&0\\
0&i\sin\theta&\cos\theta&0\\
0&0&0&1
\end{pmatrix},
$$

the executable correctly proves unitarity, commutation with leg exchange, and
conservation of total excitation.  On `|++>` the output coefficient determinant
is `1-e^{2i theta}` up to a nonzero common factor, so the gate is entangling
except at `theta in pi Z`.  From input `|01>`, the probability that the second
leg remains `1` is `cos^2(theta)`: `1/2` at `pi/4` and `0` at `pi/2`.

These different probabilities under the same fixed preparation and readout
make the two interactions operationally, not merely syntactically,
inequivalent.  This is D12's strongest exact counterexample.  It establishes
that the listed symmetry conditions do not select the angle.

### Opening M2 — interaction nonuniqueness is not yet full-model nonuniqueness

Theorem 3 needs two models of all the premises in `A_SHARD`, not merely two
matrices satisfying a subset of local algebraic constraints.  The two matrices
are excellent candidates for insertion into a common complete construction,
but that insertion is not supplied.  In particular, the executable does not
show that each angle participates in the complete history ledger, RN evidence
composition, fixed-ledger commitment, full construction quotient, independent
vertex gauge, and arbitrary projective restriction stated by the theorem.

**Required repair:** either (a) narrow `A_SHARD` and Theorem 3 to the common
premises that are actually constructed, which is already enough for a useful
nonselection theorem, or (b) state and prove an extension lemma showing that
every `U_theta` in the admitted family can be inserted into the same full typed
projective diamond model while preserving each named axiom.  The present proof
simply says the models satisfy the shared premises.

## 3. Action, Gibbs form, and maximum entropy

The negative selection arguments are sound.

For a supplied exchange Hamiltonian `H_J=-J X_ex`, evolution depends on the
undetermined dimensionless product `J tau / hbar`.  Stationary action selects a
history only after the action, boundary data, and field content have been
specified.  It does not choose `J` or the action itself.

Likewise every strictly positive finite law `P` relative to a positive
reference `mu` has the tautological Gibbs representation

$$
A(omega)=-\log\frac{P(omega)}{\mu(omega)},\qquad
P(omega)=\mu(omega)e^{-A(omega)}.
$$

Thus exponential form alone has no selecting power.  For the triple family,
the Shannon entropy derivative is

$$
H'(r)=\frac12\log\frac{1-r}{1+r},\qquad
H''(r)=-\frac1{1-r^2},
$$

so unconstrained maximum entropy uniquely returns `r=0`.  A nonzero triple
correlation must be supplied as physical information rather than extracted
from entropy.

### Opening M3 — state the hypotheses of the advertised universal form

The normalized exponential expression in the protocol is universal only for a
finite support (or under convergence/integrability hypotheses), a reference
measure positive on the selected support, and a sufficiently complete feature
family.  Zeros require support restriction or extended/infinite coefficients.
The current prose often says "general positive conditional law," which is safe
if "positive" means strictly positive on a finite `Ext(B)`, but those hypotheses
should be placed beside the boxed form.

This is a scope repair, not a discovered algebra error.

## 4. Decoherence, disintegration, and projectivity

The finite quantum calculation is correct for what it actually constructs.
After one interaction, two commuting computational-basis pointer projections
give four two-record histories.  Their branch vectors are mutually orthogonal,
their diagonal masses normalize, summing over the later first-leg record gives
the direct second-leg probability, and the two positive quarter-iSWAP branches
have deterministic conditional completions.  Those are exact results in
`Q(sqrt(2),i)`.

### Opening M4 — the minimum U1 packet is absent

The protocol defines the minimum restored object as

```text
D = (Omega_D, mu_D, P_D^hist, C_D, h_D,
     lower_screen, upper_screen, eventless_collar,
     local order_unit, frame links, typed exposed interfaces).
```

The executable's `SealedDiamond` contains only a name, an interaction matrix,
two generic incoming labels, two generic outgoing labels, two owner strings,
and a terminal Boolean.  It has no explicit screens, eventless collar,
history measure field, complete contrast ledger, evidence coefficients, order
unit, frame links, instrument/output maps, durable outcome object, or typed
gluing maps.  The test called `typed seal-and-birth` merely verifies
`incoming == outgoing` and `not terminal`.

**Required repair:** instantiate the declared packet and check type-compatible
gluing, outcome durability, ownership, output birth, and no-silent-field
conditions as data invariants.  Until then U1 is unexecuted.

### Opening M5 — U3 projectivity is reduced to one deletion in one diamond

U3 requires explicit truncation maps from fine/canonical **diamond histories**
to coarse histories and equality of cylinder masses.  The code checks only that
summing one later measurement result in a two-record experiment equals the
Born probability of the earlier pointer result.  This is ordinary finite
marginalization, not a multi-diamond projective family.

**Required repair:** construct at least a bounded multi-diamond family with
named canonical history spaces and truncation maps, then verify all relevant
commuting truncation diagrams.  For the theorem's unrestricted projective
claim, give the general argument or an all-level family.

### Opening M6 — disintegration needs its domain hypotheses

The formula

$$
P(e\mid H)=\frac{D(He,He)}{D(H,H)}
$$

requires `D(H,H)>0`, an exhaustive extension partition, and a consistent
decoherent family or record instrument.  If off-diagonals are merely
"negligible," this is an approximation requiring an error statement; exact
Kolmogorov probabilities do not follow from unquantified approximate
decoherence.  Unresolved alternatives must be combined at the class-operator
level where coherent, not always by summing diagonal weights.

**Required repair:** state the positive-denominator and consistency conditions,
separate exact from approximate decoherence, and give a bound or avoid the
probability claim in the approximate case.

The non-Markov check at the end of the restored-process executable imports the
unrelated classical three-bit formula.  It proves that one API can store a
non-Markov table; it does not show that the restored quantum diamond process is
non-Markov or carries quantum memory.

## 5. Construction-order gauge and frame covariance

### Opening M7 — U4 canonical fibers are not constructed

The construction-order check embeds two matrices on disjoint tensor factors
and verifies that they commute.  Correct, but U4 requires all auxiliary
linearizations of bounded concurrent firings to be grouped into canonical
physical fibers and requires their pushed probability or decoherence weight to
agree.  No auxiliary construction ledger, quotient map, fiber, or pushed
history measure appears in the executable.

**Required repair:** generate the auxiliary linearizations of a bounded
partially ordered multi-diamond history, map them to canonical histories, and
compare the full pushed weights.  Retain physical order for overlapping
operations and test a mixed disjoint/overlapping example.

### Opening M8 — U7 independent vertex gauge is not tested

The frame check performs one simultaneous global conjugation by
`H tensor H` on the initial state, interaction, and two pointer projectors.
That is a valid basis-covariance identity.  U7 is stronger: independently
changed vertex frames must transport states, effects, order units, instruments,
links, anchors, screens, outcomes, and the canonical bounded history.  Most of
those objects do not exist in the executable, and only one common unitary frame
is used.

**Required repair:** use independent invertible frame changes at connected
vertices, explicit link transport between them, dual transport for effects,
and verify the complete bounded history and its probabilities after transport.
If D12 intends only ordinary unitary basis covariance, rename the gate and
remove the U7 claim.

## 6. The claimed 256-commit continuation

### Opening M9 — `continuation_256_commits` is integer bookkeeping

The relevant loop starts with `live=2` and repeats

```python
live -= 2
live += 2
```

256 times.  It does not apply an interaction, sample or branch an outcome,
create a durable record, emit a new owned collar, compose histories, evaluate a
decoherence functional, or test projectivity.  The result `live == 2` follows
solely from equal tuple lengths.  Calling this "the restored universal diamond
process works exactly" is a material overclaim.

**Required repair:** construct 256 typed commits, or a symbolic induction that
actually composes the packet and process maps.  Check ownership conservation,
history growth, output births, normalization, restriction consistency, and the
construction quotient at each step or by proved invariant.

## 7. U8 and Theorem 3

### Opening M10 — the frozen protocol requires the incomplete verdict

U8 says every surviving architecture class A–E must be implemented or killed by
theorem.  The artifacts retain A as a proved negative control and display
finite examples suggestive of C/D, but they do not implement or theorem-kill
every surviving B–E class under U0–U7.  More importantly, U1, U3, U4, and U7
are not executed at their preregistered scope.  The protocol itself therefore
forces:

```text
INCOMPLETE-INVESTIGATION
  a promised object, alternative class, or decisive gate is not executed.
```

Theorem 3's logical schema is valid: two models of an axiom set that disagree
on an observable refute uniqueness.  What is missing is the premise that the
quarter- and half-iSWAP artifacts are models of the full stated `A_SHARD`.
Similarly, the classical pair does not yet provide the claimed complete
projective continuing process.  Therefore the theorem is not established at
its current quantifier scope.

**Required repair:** choose one of two honest endpoints:

1. **Narrow theorem:** prove that the explicitly implemented local structural
   and symmetry principles leave `theta` free.  This conclusion is already
   rigorous and important.
2. **Full theorem:** build two complete U0–U7 models, execute the U8 equivalence
   comparison, and show the fixed intrinsic data are identical while one
   durable record probability differs.

Only the second endpoint licenses
`UNIVERSAL-FORM/PRIMITIVE-PROCESS-REMAINS` under the frozen protocol.

## 8. Receipt assessment

The pre-review receipt is strong about reproducibility: artifact hashes,
normal/optimized stdout hashes, exact-arithmetic domains, check counts, and
semantic hashes all matched independently.  No receipt drift was found.

Its weakness is semantic granularity.  The summary hashes labels such as
`integrated_frame_covariance=PASS` and `continuation_256_commits=PASS`; hashing
a label cannot bridge the gap between the implemented cell and the quantified
protocol gate.  The receipt should distinguish:

```text
single-global-unitary basis covariance
two-disjoint-operator commutation
one two-record marginalization
two-tuple population invariant
```

from full U7, U4, U3, and repeated-process certification.  Exact arithmetic
protects calculations from rounding error, not claims from scope error.

## 9. Claims that should survive unchanged

The following findings withstand hostile review:

- `P_r` is a positive finite non-first-order-Markov witness for `|r|<1`, and
  distinct `r` values share all proper marginals while differing jointly.
- `U_(pi/4)` and `U_(pi/2)` are exact unitary, exchange-symmetric,
  excitation-conserving, entangling interactions with different fixed
  operational predictions.
- The listed structural symmetries do not select the interaction angle.
- Least action cannot select dynamics until the action and its parameters are
  supplied.
- A Gibbs/exponential representation of an already supplied positive law is
  not a derivation of that law.
- Unconstrained maximum entropy selects the uniform member `r=0`; nonzero
  correlation requires additional information.
- A whole-history measure, if supplied, yields admissible next-click
  conditionals by disintegration on positive cylinders.
- Geometry should remain gated until a process and its scale bridge are
  independently derived or selected.
- No finite-record principle exhibited in D12 presently selects the couplings,
  fields, initial state, or process of our universe.

## Exact opening ledger

```text
M1  MAJOR     P_r is a finite projective diagram, not an all-level process.
M2  MAJOR     iSWAP local countermodels are asserted, not shown, to model all A_SHARD premises.
M3  MODERATE  Universal exponential form needs finite/support/positivity or integrability hypotheses.
M4  MAJOR     Restored executable omits the minimum U1 diamond packet.
M5  MAJOR     U3 is represented by one two-record marginalization only.
M6  MODERATE  Decoherent disintegration lacks denominator/consistency/error hypotheses.
M7  MAJOR     U4 canonical construction fibers and pushed weights are absent.
M8  MAJOR     U7 is reduced to one simultaneous global Hadamard basis change.
M9  MAJOR     The 256-commit claim is a tuple-length arithmetic invariant, not process continuation.
M10 FATAL-TO-CURRENT-VERDICT
                U8 is incomplete and Theorem 3 exceeds its constructed premises;
                the frozen protocol therefore requires INCOMPLETE-INVESTIGATION.
```

## Decision

**MAJOR REVISION.**  Preserve the exact nonselection counterexamples and the
geometry refusal.  Retract the present full-gate PASS labels, replace the final
protocol verdict with `INCOMPLETE-INVESTIGATION`, and either narrow Theorem 3 or
construct the two full projective typed models its proof requires.  After those
repairs, the program may well recover its intended no-unique-dynamics result at
full SHARD scope; it has not yet done so in this frozen round.

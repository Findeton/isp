# D10 hostile review, round 2: independent repaired rebuild

**Referee:** independent clean-room reconstruction  
**Date:** 2026-07-11  
**Verdict:** **MINOR REVISION — every load-bearing executable repair passes, but the manuscript's Lorentz-cover sentence is still mathematically reversed**

The repaired package is substantially sound. I independently reproduced the
new check counts `109/99/43`, the frozen ordinary/optimized output hashes, the
rank-two comparison determinant forms, the hull-completeness hypotheses, the
projective pointer seal, the disjoint and overlapping schedule controls, and
the bounded-forest intervention probabilities. The former tautological order
and reachability tests are gone. The executable summaries now stay within
their chosen finite-packet scope.

All central D10 conclusions follow at the repaired ceiling:

```text
conditional complex-qubit/Lorentz-cone isomorphism          confirmed
finite outer directional approximations                     confirmed
finite-alphabet finite-depth H/T refinement                  confirmed
chosen pointer seal and complex-tensor schedules             confirmed
bounded copied-mark forest intervention                      confirmed
complex selection, physical link/seal, capacity              not derived
full SL(2,C) Born gauge and spacetime influence connection    open
```

One explicit old opening was not actually closed in Paper 11. It says
`PSL(2,C)` double-covers the proper orthochronous Lorentz group. The correct
statement is that `SL(2,C)` is the double cover and
`PSL(2,C)=SL(2,C)/{+/-I}` is isomorphic to `SO^+(1,3)`. This is a local prose
correction, not a defect in any receipt or in the boost calculation. It blocks
an unconditional round-2 PASS but warrants only `MINOR REVISION`.

## 1. Frozen repair snapshot

The round-1 repair receipt has SHA-256:

```text
b5ee4792718745285c830c39148882fd7eaebe47015469234798ddde51a031c0
```

All submitted repair hashes reproduce:

```text
fe91dfeb1e95d04b813f59b59c47443df246b8e74ad579ef263796df511ff494  v10/note-d10-round1-opening-repairs.md
0b9040cc8e6d6608b169ed5ff11c290b32768ebbce1fb964c0fb694956a36c88  v10/code/d10_bloch_lorentz_exact.py
595ca56dce92052f0db0ecc3fe28252e2b467dd1eb28b55aead26aa0848650d3  v10/code/d10_finite_clock_convergence.py
09e68cb09301a1706b65f2742f3eb0fb5e4f5a5468bd69b1893374a5d1c1d856  v10/code/d10_relational_scir_packet.py
ed9cf8089f61dc777be4dc436f5df41a30cd4f764e0617a975a0d2e667439d90  v10/code/d10_reproducibility_audit.py
bccb87ca0b05c8882052a388e85974c40ae6dd89fc9a056bc93208686e908942  v10/note-d10-bloch-celestial-investigation.md
1a41f3848095ea524c06035af74c08450108f5d822aa9e73093af290150824ba  v10/relativistic-isp-v10-paper11-many-clocks-few-factors-is-an-exact-kinematic-bridge.md
```

No production artifact was modified during this review.

## 2. Reproduction and receipt integrity

I ran the repaired audit from a clean Python process. Every script completed
normally and under `python -O`; each pair was byte-identical. The audit also
compared the observed output hashes against frozen expected values and
returned:

```text
D10 REPRODUCIBILITY AUDIT
scripts=3
normal_optimized=BYTE_IDENTICAL
frozen_stdout_hashes=PASS
d10_bloch_lorentz_exact.py bytes=4750 stdout_sha256=a05b84aa0a94a4a3086c190045fc56e96eb0fde6a00c179073a23944bbebcd5f
d10_finite_clock_convergence.py bytes=7470 stdout_sha256=f2e8c45e1a224e4f84ebfdd5a11e9973266879723443508d9f04539fdaa3be27
d10_relational_scir_packet.py bytes=3294 stdout_sha256=b5827de1d703ab492563fb1b981a41da477a1627943215ffe4ce660d0feb65eb
audit_sha256=f8c409191f05ee830a6422428517860e1961311b98c6f3b6be1dc5c505e6b596
```

The three executables separately declare `EXPECTED_CHECKS = 109`, `99`, and
`43` and raise before printing their summaries if the observed count differs.
They use explicit exception checks, so optimization does not remove the
conditions. The audit freezes stdout hashes rather than merely reporting new
ones. The repair receipt separately freezes source hashes.

This closes the round-1 receipt-integrity opening. As always, count and hash
gates certify a frozen program, not the meaning of its propositions; the
remaining sections independently reconstruct the new propositions.

## 3. Comparison determinant forms

The repaired exact receipt adds two checks for each of the real, complex,
quaternionic, and octonionic rank-two spin-factor shadows. Independently, let

$$
X=\begin{pmatrix}a&z\\z^*&b\end{pmatrix},
\qquad
t={a+b\over2},\quad s={a-b\over2}.
$$

For a normed division-algebra coordinate `z`,

$$
\det X=ab-|z|^2=t^2-s^2-|z|^2.
$$

If the real dimension of `z` is `q`, the event space has `q+2` real
coordinates and the determinant has signature `1+(q+1)`. Thus

```text
q=1 -> dimension 3  -> 1+2
q=2 -> dimension 4  -> 1+3
q=4 -> dimension 6  -> 1+5
q=8 -> dimension 10 -> 1+9
```

The executable's rational witnesses satisfy the displayed identity exactly.
For `R,C,H`, its chosen diagonal/off-diagonal values have nonnegative
determinant; for the octonionic shadow the selected norm exceeds `ab`, giving
a negative determinant and a correctly rejected positive-cone witness. The
code explicitly limits the octonionic claim to the rank-two ordered
spin-factor determinant and assumes no general associative matrix algebra.

The new positivity equality is close to a definitional wiring check because
`determinant` was just assigned `ab-|z|^2`. The determinant-form identity and
the written universal derivation nevertheless supply the preregistered result.
The receipt no longer claims that a finite witness proves every universal
quantifier.

**Disposition:** closed.

## 4. Hull hypotheses and triple-normal completeness

The finite-geometry script now verifies for every standalone and nested test
set:

1. some triple has nonzero determinant, so the directions span three real
   dimensions; and
2. the equal-weight barycenter is zero to 80-decimal tolerance.

All weights in that barycenter are strictly positive. Hence zero lies in the
relative interior of the convex hull; full three-dimensional span upgrades
this to ordinary hull interior. The centered support minimum is therefore the
distance to a nearest supporting facet. Every three-dimensional facet contains
an affinely independent triple, so its unit normal occurs in the production
enumeration. Additional non-facet triple normals are merely additional unit
test directions and cannot lie below the global minimum.

This supplies the completeness argument missing in round 1. My independent
convex-hull facet calculation from the previous round remains unchanged and
reproduces the reported minima:

```text
tetrahedron  0.333333333333333370
octahedron  0.577350269189625842
cube        0.577350269189625842
icosahedron 0.794654472291766112
dodecahedron 0.794654472291766112
dual union  0.842128148500700280
```

The paper also separates two statements correctly:

- its executed finite point sets are finite outer approximations; and
- convergence is conditional on a nested family having dense union.

The compactness proof is valid: a finite epsilon-net can be chosen from the
dense union and nesting places it inside one finite stage. Applying it to the
positive `H/T` monoid additionally imports Clifford+T density; `H^-1=H` and
`T^-1=T^7` ensure the inverse-generated group introduces no new alphabet.

**Disposition:** hull and convergence-scope openings closed.

## 5. Projective `SEAL` instrument

The repaired packet defines

$$
P_0=|0\rangle\langle0|,
\qquad
P_1=|1\rangle\langle1|.
$$

Independent exact arithmetic gives

$$
P_0^\dagger P_0+P_1^\dagger P_1=I.
$$

For `rho_+=H|0><0|H`,

$$
\operatorname{Tr}(P_0\rho_+P_0)
=\operatorname{Tr}(P_1\rho_+P_1)=1/2,
$$

the two branch weights sum to one, and applying the same pointer projector to
its unnormalized branch again leaves that branch invariant. This is a genuine
complete two-outcome projective instrument with repeatable pointer outcomes,
not the round-1 string placeholder.

The code does not implement a general grammar state machine that rejects all
post-seal continuation tokens. Paper 11 claims an executed pointer instrument
and durable repetition, which are proved; it does not rely on a stronger
absorbing-terminal theorem. Calling the token “terminal” in the packet listing
should continue to be read as declared packet policy rather than an additional
receipt result.

**Disposition:** load-bearing seal opening closed at the stated chosen-
instrument scope.

## 6. Disjoint schedules and overlapping control

The old dictionary-order comparison has been deleted. The repaired program
constructs a two-qubit product state and the actual operators

$$
L=H\otimes I,
\qquad
R=I\otimes T.
$$

Tensor multiplication gives `LR=RL`; both nested pushforwards are evaluated
and produce the same normalized density matrix. On one qubit, the overlapping
control compares

$$
T(H|0\rangle)
\quad\hbox{with}\quad
H(T|0\rangle)=H|0\rangle.
$$

The first has relative phase `exp(i*pi/4)` and the second does not, so their
projectors differ. The control therefore demonstrates that the harness can
detect order dependence when supports overlap.

The selected right-hand `T` happens to fix its local input `|0>`, making the
state-level disjoint example easier than necessary. The separate exact
operator commutator is state-independent and prevents this from becoming a
tautology. A future general instrument-locality theorem would need arbitrary
disjoint CP maps and supplied tensor/incidence typing; the manuscript
explicitly limits this receipt to the imported complex-tensor packet.

**Disposition:** closed at the declared chosen-packet scope.

## 7. Bounded-forest intervention probabilities

The repaired forest has roots `0,7`, branches

```text
0 -> 1 -> {3,4}
0 -> 2 -> {5,6}
7 -> 8
```

Node `1` is a Bernoulli source; every other nonroot node copies its parent's
sealed classical mark. Clean-room propagation gives:

```text
baseline p(source mark)=1/3:
  p1=p3=p4=1/3; all other node mark probabilities=0

intervened p(source mark)=2/3:
  p1=p3=p4=2/3; all other node mark probabilities=0
```

Thus the changed support is exactly `{1,3,4}`. The sibling branch
`{2,5,6}` and disconnected component `{7,8}` are unchanged, and every value
lies in `[0,1]`. Because copied descendants are deterministic conditional on
the one Bernoulli source, these marginals also specify the joint copied-mark
law for this bounded example.

This is no longer global transitive-closure bookkeeping. Each fixed update
reads one parent probability and its local node type. The implementation does
use ascending numeric node IDs as a supplied topological schedule; it is not a
generic forest scheduler or a joining-sector law. Both paper and receipt now
say precisely that joining, ancestry-order comparison, and spacetime
influence remain untested.

The classical forest intervention is separate from the qubit pointer
instrument and from the declared Bloch displacement shadow. The verdict says
“chosen-packet seal/schedule/forest intervention tests,” not that one unified
dynamical law has connected all three. No hidden coupling is being claimed.

**Disposition:** closed at finite bounded-forest scope.

## 8. Finite-depth direction and coverage claims

The exact Bloch-coordinate clean-room rebuild from round 1 still gives:

```text
depth       0  1  2  3  4   5   6   7   8   9  10  11  12
projectors  1  2  3  5  8  13  19  26  35  48  64  85  113
```

The repaired receipt now says explicitly:

```text
generation_external_sphere_sampler=ABSENT
coverage_diagnostic_external_fibonacci_sampler=50000
finite_alphabet_finite_depth_refinement=PASS
per_record_evidence_capacity=NOT_ESTABLISHED
```

That is the correct distinction. Production's depth-12 Fibonacci support
`0.914143429015` remains a sampled upper estimate. The independent hull value
`0.912486956834076` and radial excess `9.5906%` are now stated separately in
the investigation note. No finite-dimensional-state claim is promoted to a
per-record evidence, provenance, or exact-description capacity theorem.

**Disposition:** external-sampler, finite-capacity, and depth-12 coverage
openings closed.

## 9. Supplied connection and physical claim ceiling

The relational calculation is now consistently named covariance of a
**supplied** `SU(2)` connection. The manuscript explicitly leaves open link
birth, values, ownership, calibration, transport instruments, and a physical
holonomy seal. It no longer treats four chosen matrix values as four
independent generic gauges; it says vertex-local basis changes, while the
displayed cancellation identity supplies the general covariance argument.

The normalized qubit/time-scale gap, complex-selection gap, nonunitary boost
gap, and order-versus-spacetime-influence gap remain visible in the abstract,
body, verdict, and exclusions. The result remains `KINEMATICS-ONLY`.

**Disposition:** ontology/locality overclaims closed.

## 10. Closure table

| Round-1 opening | Round-2 finding | Status |
|---|---|---|
| qubit/Lorentz result named as physical derivation | renamed conditional ordered-space isomorphism | closed |
| projective effects called operational clocks | consistently called directional positive/clock-shadow evaluations pending click/time/unit map | closed |
| external sphere sampler called absent | generation and coverage diagnostic reported separately | closed |
| finite Hilbert dimension promoted to record capacity | finite alphabet/depth only; evidence/description capacity open | closed |
| supplied link algebra called physical sealed holonomy | supplied-connection covariance; physical link/seal fields open | closed |
| complex tensor product hidden in locality claim | imported chosen complex-tensor model declared | closed |
| construction-order dictionary tautology | two composed schedules plus noncommuting overlap control | closed |
| graph reachability called instrument influence | exact copied-mark continuation probabilities on a bounded forest | closed at stated finite scope |
| `SEAL` only a string | complete repeatable projective pointer instrument | closed at stated instrument scope |
| comparison determinant gate absent | exact coordinate determinant/positivity witnesses for `R,C,H,O` shadows | closed |
| finite examples called convergence | finite PASS; infinite limit conditional on dense nested union | closed |
| hull hypotheses/completeness absent | span, origin interior, and facet proof added | closed |
| check totals and hashes unfrozen | `109/99/43`, fixed stdout hashes, normal/`-O` gates | closed |
| sampled depth-12 support overgraded | sampled and true hostile hull values separated | closed |
| `SL(2,C)`/Lorentz cover wording imprecise | Paper 11 says `PSL(2,C)` double-covers `SO^+(1,3)` | **not closed** |
| vertex gauges called four independent general choices | wording narrowed; algebraic identity remains general | closed |
| nonexistent final receipt linked | pre-review receipt linked; final deferred until closure | closed |

## 11. Remaining required correction

### Opening R2-1 — **MINOR** — cover versus quotient is reversed

Paper 11 Section 7 currently says:

> The quotient `PSL(2,C)` double-covers the proper orthochronous Lorentz group.

The kernel of the Hermitian-congruence action of `SL(2,C)` is `{+I,-I}`.
Therefore the correct relationships are

$$
SL(2,\mathbb C)\longrightarrow SO^+(1,3)
$$

as a two-to-one covering homomorphism, and

$$
PSL(2,\mathbb C)
=SL(2,\mathbb C)/\{\pm I\}
\cong SO^+(1,3).
$$

The investigation note's weaker sentence—that proper orthochronous Lorentz
transformations are represented by the `SL(2,C)` congruence—is fine. The
repair ledger says this wording was corrected, so the surviving Paper 11 line
must be fixed before final receipt closure.

This opening is editorial/mathematical rather than executable. The exact
diagonal boost, determinant preservation, nonunitarity, and trace-change
receipts are unaffected.

## 12. Search for new wiring defects

I found no new load-bearing wiring defect. Three limitations are worth keeping
visible, and the repaired prose already does so:

1. the disjoint schedule imports a complex tensor product rather than deriving
   composition from records;
2. the bounded forest uses a supplied topological order and has no joining
   sector; and
3. the pointer seal, classical forest, and Bloch displacement are separate
   finite tests, not one derived interacting click law.

The source docstring of the relational packet still says “no external S2
sampler,” even though the file contains an external Fibonacci coverage
diagnostic. Its executable summary and both manuscripts provide the precise
generation-versus-diagnostic distinction, so the docstring is a minor
maintenance ambiguity rather than a new claim defect.

Calling `SEAL` terminal is also policy rather than an executed absorbing-state
test: the receipt proves completeness and repeatability, not that a grammar
engine rejects every future `H/T` token after sealing. The manuscripts rely
only on the instrument and repeated-pointer claims, so no current conclusion
depends on that stronger behavior.

## 13. Final determination

The repaired executable evidence independently supports:

$$
\boxed{
\begin{aligned}
&\text{a conditional complex-qubit/Lorentz-cone isomorphism,}\cr
&\text{finite outer-cone and finite-depth projector refinement,}\cr
&\text{and limited chosen-packet seal, schedule, and forest tests;}\cr
&\text{not a selected, scaled, or influence-wired spacetime dynamics.}
\end{aligned}
}
$$

All round-1 executable and scope openings are closed. Receipt integrity is
now adequate, and no new load-bearing wiring failure was found. Final PASS is
withheld only because a specific Lorentz-group sentence remains false despite
being listed as repaired.

**Round-2 independent-rebuild verdict: MINOR REVISION.**

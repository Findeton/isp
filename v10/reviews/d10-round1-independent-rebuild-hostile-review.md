# D10 hostile review, round 1: independent clean-room reconstruction

**Referee:** independent reconstruction and reproducibility stream  
**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION — the exact kinematic bridge and numerical geometry reproduce, but the receipt overgrades its comparison and local-dynamics wiring**

The central mathematical result is correct. Independently of the production
implementation, `Herm_2(C)_+` is the `3+1` Lorentz cone, its normalized
rank-one boundary is `CP^1 = S^2`, and every directional evaluation depends
on four real coefficients. A separate convex-hull calculation reproduces all
six reported Platonic support minima. A separate exact Bloch-coordinate
enumerator reproduces the complete `H/T` reachable-projector sequence through
depth 12, including the reported count `113`; an independent hull calculation
puts the true depth-12 support minimum at about `0.912486956834076`, consistent
with the production sampler's upper estimate `0.914143429015`.

The negative claim ceiling is also substantially honest: D10 does not derive
complex selection, the physical Bloch/celestial identification, a time scale,
full `SL(2,C)` gauge, or order/influence equivalence.

The submitted receipt nevertheless fails its own hostile standard in four
load-bearing places. None of the three executables freezes its expected check
count. The frozen G1 gate requires determinant-form checks for the comparison
algebras, but the exact executable checks only their dimensions. The claimed
construction-order test compares two dictionaries populated from the same
already-computed data and is therefore tautological. The claimed influence
test is graph reachability, not a counterfactual instrument or continuation-law
test, while `SEAL` is only a string and has no implemented operation. Those
defects do not refute the kinematic theorem, but they block a round-1 PASS.

## 1. Frozen artifacts and ordinary/optimized reproduction

The submitted hashes reproduce exactly:

```text
26e61c146b328b5eae14994594f79bb70421a275a35de464b4245e482dc42a46  v10/note-d10-bloch-celestial-selection-protocol.md
8d9d05f6ea95d4c522f8cf7bde9d05d88e1bb712bf65c3eaf5da21cc8fc155b8  v10/code/d10_bloch_lorentz_exact.py
32b5be41cb73c41d9804c2576c3297aa5ba3d9d044fa6a4283e7a003c708f7ed  v10/code/d10_finite_clock_convergence.py
5417d17efcbfed942701f9cf9512327aaa665bf3ba489d6aec72f4456225290b  v10/code/d10_relational_scir_packet.py
527fd9bbd4cc19f0741b33bfb4812be424fb83f32bcad6a620f1a4e54149bde4  v10/code/d10_reproducibility_audit.py
435a4c183d908a7e2191de455946a78d20287421020adfff5b80c6de4b2feee7  v10/note-d10-literature-audit-bloch-celestial.md
cd3e7109078daa3e7688fa3c5e639ef5094e414a752c7b338cbdf5fdf33ac06e  v10/note-d10-bloch-celestial-investigation.md
500e5e92cb11b6941486350c716a21705d3a2a9f9e3d506fb8d0567756d7fba7  v10/relativistic-isp-v10-paper11-many-clocks-few-factors-is-an-exact-kinematic-bridge.md
```

The pre-review receipt itself has SHA-256:

```text
ed9340af3900c32110084d76e34719923fcafb8cdae8e9693bcd922366b70d1e
```

I reran all three programs normally and under `python -O`. Each pair was
byte-identical, and the independently observed output hashes match the frozen
receipt:

```text
d10_bloch_lorentz_exact.py       aec13fa5e950590a26f318a7f5b3ee13aa4768375ff0aee9cb466c49ca4af484
d10_finite_clock_convergence.py  1aa359956a10b01390ef7150c4db6de841d1ad3c26f004673cf05cf02ad0406b
d10_relational_scir_packet.py    11e38ec6a630ef503ed48bb91ab43eb673b3a150d3d2fed341f78aaa9fcc587c
```

The aggregate audit digest also matches:

```text
379b43354f8bb7137ca98b2d776abac73e5a579d947b167f969c22b9aa190e1a
```

This establishes deterministic reproduction of the submitted programs. It
does not by itself establish that every frozen gate has been implemented;
that question is addressed below.

## 2. Independent derivation of the qubit Lorentz cone

Write a general complex Hermitian two-by-two matrix in real coordinates:

$$
X=
\begin{pmatrix}
t+z & x-iy\\
x+iy & t-z
\end{pmatrix}
=tI+x\sigma_x+y\sigma_y+z\sigma_z.
$$

This is a real-linear bijection: the two real diagonal entries determine
`t,z`, and the real and imaginary parts of the upper off-diagonal entry
determine `x,y`. Direct expansion, without using the production matrix class,
gives

$$
\det X=(t+z)(t-z)-(x-iy)(x+iy)
=t^2-x^2-y^2-z^2.
$$

The characteristic polynomial is

$$
\lambda^2-2t\lambda+(t^2-|\mathbf x|^2),
$$

so the eigenvalues are `t +/- |x|`. Therefore

$$
X\succeq0
\iff t-|\mathbf x|\ge0
\iff t\ge|\mathbf x|.
$$

For a unit vector `u`, direct multiplication of

$$
P_u={1\over2}
\begin{pmatrix}
1+u_z&u_x-iu_y\\
u_x+iu_y&1-u_z
\end{pmatrix}
$$

gives `P_u^2=P_u`, `Tr P_u=1`, and `det P_u=0`. Conversely, a trace-one
Hermitian matrix has the same form with a Bloch vector `r`; positivity gives
`|r|<=1` and rank one gives `|r|=1`. Finally,

$$
\operatorname{Tr}(P_uX)=t+u\cdot x.
$$

Thus all directional questions are linear functions of four real factors,
and requiring their nonnegativity for every `u` recovers the Lorentz cone.
The production witnesses agree with this derivation, but the result does not
depend on those samples.

The diagonal `SL(2,C)` witness also checks independently. For
`A=diag(2,1/2)`,

$$
t'={17\over8}t+{15\over8}z,
\qquad
z'={15\over8}t+{17\over8}z,
$$

while `x,y` are unchanged and `t'^2-z'^2=t^2-z^2`. The map preserves the
determinant but not trace and is not unitary. The paper's rotation/boost
distinction follows.

## 3. Independent finite-direction support calculation

Production minimizes the support by enumerating normals to direction triples.
I used a different dual construction. For each direction set `U`, I formed
the convex hull `conv(U)`, enumerated supporting triangular planes, and took
the least distance of a supporting plane from the origin. That centered
inradius equals

$$
m(U)=\min_{|x|=1}\max_{u\in U}u\cdot x.
$$

The clean-room double-precision results are:

| set | `K` | independent `m(U)` | independent radial excess |
|---|---:|---:|---:|
| tetrahedron | 4 | 0.333333333333333370 | 1.999999999999999556 |
| octahedron | 6 | 0.577350269189625842 | 0.732050807568876971 |
| cube | 8 | 0.577350269189625842 | 0.732050807568876971 |
| icosahedron | 12 | 0.794654472291766112 | 0.258408572364819067 |
| dodecahedron | 20 | 0.794654472291766112 | 0.258408572364819067 |
| dual union | 32 | 0.842128148500700280 | 0.187467728967818159 |

These agree with the 90-decimal production values to the expected floating
precision. The exact controls also follow analytically: a tetrahedral facet
is at centered distance `1/3`, while an octahedral facet
`x+y+z=1` is at distance `1/sqrt(3)`.

The production triple-normal method is complete for these origin-containing
three-dimensional convex hulls: a minimizer of the support is perpendicular
to a nearest supporting facet, and every facet contains an affinely
independent triple included in the enumeration. Non-facet triple normals
cannot lower the result below the global support minimum. I found no hidden
numerical dependence in the reported Platonic table.

The dense Fibonacci values are correctly treated as independent upper
approximations to the true minima, not as the load-bearing minima. The
reported gaps all have the correct sign and lie within the frozen tolerance.

## 4. Independent `H/T` projector enumeration and coverage

I rebuilt the reachable projectors in Bloch coordinates, not with the
production matrix/projector representation. Conjugation acts exactly as

$$
H:(x,y,z)\mapsto(z,-y,x),
$$

and

$$
T:(x,y,z)\mapsto
\left({x-y\over\sqrt2},{x+y\over\sqrt2},z\right).
$$

Starting from `(0,0,1)`, I represented every coordinate exactly as
`a+b*sqrt(2)` with rational `a,b`, applied both maps cumulatively, and
deduplicated Bloch triples. The full independent sequence is:

```text
depth       0  1  2  3  4   5   6   7   8   9  10  11  12
projectors  1  2  3  5  8  13  19  26  35  48  64  85  113
```

This reproduces every count displayed by Paper 11. It also confirms that
projector deduplication, rather than state-vector phase, is the correct
equivalence relation.

As a stronger diagnostic than production's 50,000-point sample, I computed
the centered convex-hull support minimum of the exact reachable direction set
after converting only the final hull geometry to floats:

| depth | projectors | true hull support from independent facets |
|---:|---:|---:|
| 4 | 8 | 0.000000000000000 |
| 6 | 19 | 0.678598344545847 |
| 8 | 35 | 0.678598344545847 |
| 10 | 64 | 0.862856209461017 |
| 12 | 113 | 0.912486956834076 |

At depth 12 the true radial excess is about `0.0959061`. Production's sampled
support `0.914143429015` is larger by about `0.00165647`, exactly as an
unsaturated directional sampler should be; its corresponding `9.392%` radial
figure is explicitly described as being “on that deterministic probe.” The
receipt does not confuse this sampled coverage with an exact hull minimum.

The finite-depth existence and count claims therefore pass. A proof that the
infinite `H/T` orbit is dense relies on the broader Clifford+T universality
result, not on the depth-12 receipt alone; the paper points to that literature
and does not treat `113` points as the continuum.

## 5. Exact gauge algebra: conditional pass

For links transforming as

$$
U_{ba}'=V_bU_{ba}V_a^\dagger,
$$

the internal frame factors cancel on a path. Hence a path from `a` to `d`
transforms as `V_d U_path V_a^dagger`, and a loop based at `a` transforms by
conjugation with `V_a`. Trace, determinant, and spectrum are therefore
invariant. This is a general symbolic consequence, not merely a property of
the production's chosen `iX,iY,iZ` witness.

Likewise, operators on distinct tensor factors commute:

$$
(A\otimes I)(I\otimes B)=A\otimes B=(I\otimes B)(A\otimes I).
$$

These facts justify a relational `SU(2)` frame calculus once the link data
and tensor split are supplied. They do not select those data, implement a
seal, or establish full Lorentz gauge. The paper's stated ceiling here is
correct.

## 6. Numbered hostile openings

### Opening 1 — **MAJOR** — receipt cardinalities and expected hashes are not gated

Each production script initializes `CHECKS = 0`, increments it, and prints the
observed count. None defines `EXPECTED_CHECKS`, none fails if its final count
differs from `101`, `97`, or `32`, and none has an expected receipt digest.
The reproducibility audit checks normal output against optimized output but
does not compare either output hash with a frozen expected hash.

Consequently, deleting one substantive condition from a script would yield
byte-identical normal/optimized runs, a new reported hash, and a successful
audit exit. The human-readable frozen receipt would reveal the change only if
someone manually compared it. This is deterministic reporting, not a sealed
receipt gate.

**Required repair:** freeze `EXPECTED_CHECKS` separately in all three scripts,
fail before printing unless the count matches, and make the reproducibility
audit compare the three stdout hashes with frozen expected values. The audit
should also make clear whether source hashes are merely reported or gated.

### Opening 2 — **MAJOR** — frozen G1 determinant comparison was not executed

Protocol G1 requires the executable to count the real/quaternionic comparison
dimensions **and verify their determinant quadratic forms**. The exact script
only computes

```text
event_dimension = 2 + offdiag_dimension
```

for `R,C,H,O` and labels the results spin-factor dimensions. It constructs no
real, quaternionic, or octonionic rank-two element and checks no comparison
determinant or positivity cone.

The missing mathematics is simple and supports the manuscript rather than
refuting it. For

$$
\begin{pmatrix}a&q\\q^*&b\end{pmatrix},
\qquad
t={a+b\over2},\quad s={a-b\over2},
$$

the rank-two determinant is

$$
ab-|q|^2=t^2-s^2-|q|^2.
$$

If the division algebra has real dimension `d`, this is a Lorentz form on
`d+2` real coordinates. Thus the anti-selection conclusion is correct, but
the submitted 101-check receipt did not satisfy its preregistered wiring gate.

**Required repair:** implement exact determinant/positivity witnesses for at
least `Herm_2(R)`, `Herm_2(C)`, and `Herm_2(H)`, keep the octonionic claim at
the rank-two spin-factor level, and distinguish executed algebra from a
dimension lookup.

### Opening 3 — **MAJOR** — construction-order “gauge” check is tautological

The SCIR script computes every node position before its order test. It then
sets

```python
state_a = {n: positions[n] for n in order_a}
state_b = {n: positions[n] for n in order_b}
check(state_a == state_b, ...)
```

Python dictionary equality ignores insertion order, and both dictionaries
read the same precomputed `positions` values. No instrument is applied in
either order, no mutable collar state is evolved, no random outcome law is
composed, and no shared-boundary effect can expose an order dependence. The
condition is true by construction even if the underlying updates would fail
to commute.

The separate tensor identity in the exact script establishes commutation for
the particular disjoint product operators that it constructs. It does not
repair this purported ancestry/update test or cover overlapping diamond
wiring.

**Required repair:** start from one frozen collar state, apply two explicitly
typed disjoint instruments in both sequential orders, and compare the full
resulting state/continuation law. Include a coupled or overlapping control
which is allowed not to commute, so the test can distinguish locality from a
dictionary artifact.

### Opening 4 — **MAJOR** — `local_influence=PASS` is reachability, not influence

The function `descendants(seed)` computes transitive closure in a hard-coded
parent dictionary. It never changes an instrument, never constructs two
continuation measures, and never compares later seal probabilities. The
claimed mark is membership in a graph-theoretic reached set. Moreover, the
implementation scans the entire `parents.items()` table repeatedly; it is a
global diagnostic of an already supplied graph, not an executed incidence-
local update rule.

Paper 11 correctly says order/influence-cone equivalence remains open, but it
also says the finite packet proves that “a changed local instrument affects
its causal descendants.” The current receipt proves only the definitional
statement that descendants in the supplied parent map remain on descendant
branches.

**Required repair:** rename the current result
`SUPPLIED-GRAPH-REACHABILITY-LOCAL`, or implement the marked-intervention test
named in the paper: two locally differing instruments, two continuation laws,
and an exact comparison of which later sealed distributions change. The
update implementation must consume only incident/recorded data; a global
closure routine may remain as an external verifier.

### Opening 5 — **MAJOR** — the `SEAL` operation is only a string

The claimed grammar is `H,T,SEAL`, but reachable states are generated only by
unitary `H` and `T`. `SEAL` appears solely in

```python
TOKENS_PER_COLLAR = ("APPLY_H", "APPLY_T", "SEAL")
```

followed by checks that the tuple has length three and contains strings. There
is no seal instrument, outcome space, Born probability, durable record, or
termination transition. Therefore the executable demonstrates a finite local
**unitary direction generator**, not yet a finite SCIR packet with sealing.

This does not damage the `H/T` orbit or the kinematic bridge. It does make the
phrases “bounded `H/T/SEAL` SCIR candidate” and “terminal token: SEAL” stronger
than the executed object.

**Required repair:** either narrow the claim to an `H/T` direction-generator
subpacket, or define an exact seal instrument and include its outcomes and
record effect in the locality, gauge, and order tests.

### Opening 6 — **MODERATE** — `external_sphere_sampler=ABSENT` is scoped ambiguously

Direction **generation** uses only exact `H/T` words and therefore passes the
substantive no-oracle gate. However, the same script's `sampled_support()`
explicitly constructs 50,000 Fibonacci directions from trigonometric
coordinates on a globally labelled sphere. The receipt's unqualified line

```text
external_sphere_sampler=ABSENT
```

is literally false for the diagnostic executable, although it is true of the
rewrite grammar.

**Required repair:** report
`generation_external_sphere_sampler=ABSENT` and
`coverage_diagnostic_external_fibonacci_sampler=50000`. Keep the manuscript's
important distinction: an external test probe is permissible; an external
direction oracle in the generative law is not.

### Opening 7 — **MODERATE** — the 101-check receipt does not execute every theorem identity it says it verifies

The exact program checks Pauli anticommutators, determinants on three event
samples, positivity on four rational-norm samples, and five rational
projectors. It does not symbolically execute the general eigenvalue formula,
uniqueness of every Hermitian expansion, or the converse classification of
all normalized rank-one projectors. Paper 11 proves those statements on the
page, so the theorem is sound. The sentence “the exact receipt verifies all
theorem identities” is nevertheless too broad for a finite witness suite.

**Required repair:** say that the receipt verifies exact generating identities
and representative witnesses while the displayed proof supplies the universal
theorem, or add a symbolic coefficient-level derivation to the receipt.

### Opening 8 — **MINOR** — Paper 11 links a nonexistent final receipt

The reproducibility package names
`v10/data/d10-final-receipt.md`, but the frozen artifact is
`v10/data/d10-pre-review-receipt.md`; the named final file does not exist.

**Required repair:** point the pre-review manuscript to the pre-review receipt,
then create and link a final receipt only after hostile openings are resolved.

## 7. Claims that survive the hostile audit

The following conclusions follow independently and should be preserved:

1. `Herm_2(C)_+` is exactly a four-real-dimensional Lorentz cone.
2. Its normalized null rays form `CP^1 = S^2`, and directional evaluations
   are four-factor linear readouts.
3. Finite direction families give outer polyhedral approximations; the six
   reported support minima and radial excesses are correct.
4. Lorentz-cone kinematics alone does not select three spatial dimensions.
   The comparison determinant derivation above confirms the paper's negative
   result even though production omitted the required checks.
5. The real/complex local-tomography counts `3,10` and `4,16` are correct, but
   D10 has not derived local tomography from record data.
6. Exact `H/T` words generate 113 distinct projective directions through
   depth 12 without consulting an external sphere during generation.
7. Supplied local `SU(2)` frames and link transports admit the stated
   relational conjugation calculus.
8. A normalized qubit fixes its trace and therefore does not supply the cone's
   independent temporal scale.
9. General boosts require nonunitary `SL(2,C)` congruences, whose status as
   quantum filters versus frame gauge remains unresolved.
10. No receipt equates the directional order cone with a marked influence
    cone, and no physical metres, seconds, `c`, `G`, or Einstein dynamics
    follows.

The declared `Delta t=1, Delta x=r` edges are null because `|r|=1`; they are
also explicitly packet data rather than a derivation. This is honest and not
an opening.

## 8. Wiring and circularity assessment

I found no hidden numerical coupling between the Platonic support calculation
and the `H/T` orbit. The former receives externally declared polyhedral
directions; the latter generates algebraic projectors from a finite word
grammar. Their coverage routines share the idea of a Fibonacci diagnostic,
but neither uses the other program's output.

The genuine wiring gap is dynamical. The submitted SCIR script has three
parallel objects which never interact:

```text
exact H/T projector orbit
hard-coded ancestry reachability
declared Bloch-coordinate increments
```

No seal outcome from the first object changes a continuation law in the
second, and no influence distribution is compared in the third. Paper 11
mostly acknowledges this by calling the increment map declared and the
order/influence equivalence open. Round 2 must also narrow or implement the
intermediate `local_influence` and `H/T/SEAL packet` claims.

There is no circularity in the exact qubit/Lorentz theorem itself. The
selection question remains circular if one treats choosing a complex qubit as
deriving the desired `S^2`; D10 explicitly refuses that inference. The final
`KINEMATICS-ONLY` ceiling is therefore the right verdict class, subject to the
receipt repairs above.

## 9. Final determination

The best independently supported result is:

$$
\boxed{
\text{complex rank-two positivity is an exact }3+1\text{ kinematic bridge,}
\quad
\text{not a selected or dynamically wired spacetime law.}
}
$$

The algebraic theorem, finite support table, and `H/T` reachable counts are
solid. The receipt does not yet deserve PASS because its cardinality is not
frozen, one preregistered comparison-algebra gate is absent, and its local
SCIR/influence conclusions rest on a tautological order comparison,
graph-reachability bookkeeping, and an unimplemented `SEAL` token.

**Round-1 independent-rebuild verdict: MAJOR REVISION.**

# D10 hostile mathematics review — round 1

**Date:** 2026-07-11  
**Reviewer role:** independent hostile mathematics audit  
**Verdict:** **MAJOR REVISION**

The primary `KINEMATICS-ONLY` verdict is directionally correct and the central
complex rank-two theorem is sound. The revision grade is caused by failures of
the frozen review protocol and by subsidiary PASS labels that outrun their
executed tests. It is not a rejection of the Bloch/Lorentz correspondence.

## 1. Frozen artifacts and reproduction

I verified every SHA-256 in `v10/data/d10-pre-review-receipt.md`. The supplied
reproducibility audit completed successfully and reproduced the three frozen
stdout hashes under both ordinary and optimized Python:

```text
d10_bloch_lorentz_exact.py      aec13fa5e950590a26f318a7f5b3ee13aa4768375ff0aee9cb466c49ca4af484
d10_finite_clock_convergence.py 1aa359956a10b01390ef7150c4db6de841d1ad3c26f004673cf05cf02ad0406b
d10_relational_scir_packet.py   11e38ec6a630ef503ed48bb91ab43eb673b3a150d3d2fed341f78aaa9fcc587c
```

I then rebuilt the decisive mathematics without importing the production
modules.

- Direct Pauli calculation gives
  `det(tI+x.sigma)=t^2-|x|^2`, eigenvalues `t+/-|x|`, positivity
  `t>=|x|`, and `Tr(P_u X)=t+u.x`.
- Independent convex-hull facet enumeration gives the same support minima:

```text
tetrahedron       0.33333333333333337
octahedron        0.5773502691896258
cube              0.5773502691896258
icosahedron       0.7946544722917661
dodecahedron      0.7946544722917661
icosa+dodeca      0.8421281485007003
nested K=14       0.8068982213550735
nested K=26       0.8634489800144580
```

- An independent ordinary-complex enumeration of projectors reachable from
  `|0>` by positive `H/T` words gives the exact same cumulative counts:

```text
1, 2, 3, 5, 8, 13, 19, 26, 35, 48, 64, 85, 113
```

- Independent hull-facet enumeration of the 113 depth-12 directions gives
  true support approximately `0.9124869568340758`, whereas the paper's
  50,000-point diagnostic gives `0.914143429015`. The corresponding true
  radial excess is about `9.5906%`; the sampled diagnostic reports `9.3920%`.
  This does not contradict the paper where the number is explicitly called
  sampled, but it is important when judging what the number certifies.
- For `A=diag(2,1/2)` and `X=3I+sigma_x+2sigma_z`, direct congruence gives
  `AXA^dagger=[[20,1],[1,1/4]]`: both determinants are exactly `4`, while
  the traces are `6` and `81/4`. The SU(2)/SL(2,C) distinction is real.

## 2. Numbered openings

### Opening 1 — the preregistered R/C/H/O determinant gate was not executed

**Severity: MAJOR**

The frozen protocol's G1 requires the executable to both count the real
dimensions of the rank-two real, complex, and quaternionic cases **and verify
their determinant quadratic forms**. The exact script, lines 195–203, only
looks up the dimensions `1,2,4,8`, adds two diagonal coordinates, and checks
the resulting totals. It constructs no real, quaternionic, or octonionic
Hermitian element and performs no determinant, norm, cone, or positivity test
for those alternatives.

The mathematical proposition in Paper 11 is nevertheless correct. For

```text
X = [[a,z],[z*,b]],    z in F,    dim_R(F)=q,
```

one has `dim_R Herm_2(F)=q+2` and

```text
det X = ab-|z|^2 = t^2-s^2-|z|^2,
t=(a+b)/2, s=(a-b)/2.
```

This is the `1+(q+1)` spin-factor quadratic form; at rank two the octonionic
case is safely interpreted as the stated ordered spin-factor shadow. But an
unexecuted true theorem does not satisfy a preregistered executable gate.
Consequently `alternative_spin_factors=EXHIBITED` and the claim that G1 passed
are overgraded.

**Required repair:** add exact coordinate-level R/C/H/O determinant and cone
tests, with the octonionic scope kept at rank-two ordered-space level. Merely
repeating the dimension dictionary is insufficient.

### Opening 2 — Layer B conflates finite examples, sampled H/T coverage, and convergence

**Severity: MAJOR**

Frozen layer B says finite direction sets converge to the round cone with
quantified error, and Paper 11 marks B `PASS`. What is actually executed is:

1. certified-looking 90-decimal minima for a finite list of Platonic sets and
   one finite nested union;
2. a sampled, not certified, support diagnostic for H/T word sets through
   depth 12;
3. a literature appeal to Clifford+T universality.

The Platonic nested sequence stops at 38 directions and therefore proves no
limit. The H/T sequence is the relevant infinite nested family, but its script
checks only that the sampled depth-12 support exceeds the sampled depth-2
support. It neither computes the true covering support nor proves convergence.
The independent depth-12 hull result above shows why this distinction matters:
the sample is an upper bound on `m(U)`, hence it underestimates worst radial
excess.

There is a valid repair theorem: if the union of nested finite sets `U_d` is
dense in `S^2`, compactness gives covering radius tending to zero and hence
`m(U_d)->1`. Clifford+T density plus the fact that `H^-1=H` and `T^-1=T^7`
can supply density of the positive-word orbit from `|0>`. That bridge is not
stated or proved in Paper 11, and the executable's finite sample cannot replace
it.

**Required repair:** split B into `FINITE-OUTER-APPROXIMATION-PASS` and
`GENERATED-SEQUENCE-CONVERGENCE-CONDITIONAL` until the density-to-covering
argument is written. If depth-specific radial errors are claimed, use a
certified hull/Voronoi minimum rather than the Fibonacci sample.

### Opening 3 — the spherical-Voronoi minimum algorithm omits its completeness hypotheses

**Severity: MODERATE**

`covering_support` minimizes over normals to all non-collinear triples and
calls the result the true minimum. This is correct for every tested set, but
not because “triple enumeration” is automatically a universal spherical
optimization method.

The missing proof is convex-geometric. If `0` lies in the interior of the
three-dimensional polytope `conv(U)`, then

```text
min_|x|=1 h_U(x)
```

is its origin-centered inradius. The closest supporting plane is a hull facet,
and every three-dimensional facet contains three affinely independent
vertices. Its unit normal therefore appears among the enumerated triple
normals. Enumerating extra non-facet triples is harmless because every returned
normal is still an actual unit test point and cannot fall below the true
minimum.

The code checks unit normalization and zero directional bias but does not check
rank three or prove origin-interiority. Its generic docstring therefore
overstates the algorithm. The dense probe is corroboration, not a certificate.
My independent supporting-facet enumeration confirms every published value, so
this is a proof/hypothesis gap rather than a numerical retraction.

**Required repair:** state and check the span/interior hypotheses and include
the facet-normal completeness proof, or enumerate supporting hull facets
directly.

### Opening 4 — “external sphere sampler absent” is false without a qualifier

**Severity: MODERATE**

The relational receipt prints

```text
external_sphere_sampler=ABSENT
```

but the same executable's `sampled_support` function explicitly constructs
50,000 Fibonacci-sphere directions using global `(x,y,z)` coordinates. The
finite-clock executable likewise uses 120,000 such directions.

The defensible claim is narrower and valuable: **the H/T rewrite grammar does
not use the sampler to generate its projectors**. The sphere sampler is used
afterward as a coverage diagnostic. Paper 11 usually includes that qualifier;
the machine receipt does not.

**Required repair:** replace the status with, for example,
`generation_sphere_oracle=ABSENT; diagnostic_sphere_probe=PRESENT`.

### Opening 5 — the sibling construction-order test is tautological

**Severity: MAJOR**

In `d10_relational_scir_packet.py`, positions are first computed once. The two
purported orders then form dictionaries from the same already-computed
`positions[n]` values:

```python
state_a = {n: positions[n] for n in order_a}
state_b = {n: positions[n] for n in order_b}
check(state_a == state_b, "disjoint sibling construction order is gauge")
```

Python dictionary equality deliberately ignores insertion order. The check
would pass for any values in `positions`; it never re-executes an update in
either order. It therefore proves no commutation or construction-order gauge.

The separate exact check

```text
(GX tensor I)(I tensor GZ) = (I tensor GZ)(GX tensor I)
```

does genuinely prove commutation for those two disjoint unitary frame changes.
It does not establish the frozen G4 requirement for arbitrary disjoint SCIR
instruments, nor does the static descendant search establish a stochastic
causal test. The local SU(2) link-covariance and diamond-holonomy theorem remains
sound, but the broader subsidiary locality/order PASS is overgraded.

**Required repair:** execute two independently rebuilt compositions of typed
local instruments, compare their complete resulting states/probabilities, and
restrict the verdict to the instrument class actually tested.

### Opening 6 — `SL(2,C)` covers the proper **orthochronous** Lorentz group

**Severity: MINOR**

The SU(2)/SL(2,C) distinction is otherwise correct: SU(2) conjugation preserves
trace and gives rotations, while general SL(2,C) congruence preserves the
Minkowski determinant and includes boosts but is nonunitary on normalized
qubits.

The group statement should be precise. The action has kernel `{+I,-I}` and

```text
PSL(2,C) is isomorphic to SO^+(1,3),
```

the identity-component/proper-orthochronous Lorentz group. Phrases such as
“the proper Lorentz group” or “full proper Lorentz transformations” can be
read as including the other determinant-`+1` component, which SL(2,C) does not
cover. The future-cone context makes the intended component clear, so this is
a terminology repair rather than a failed calculation.

### Opening 7 — the executable did not use four independently chosen frame changes

**Severity: MINOR**

Paper 11 says the receipt used independent basis changes at all four diamond
vertices. The test assigns `V_a=GZ` and `V_d=GZ`, so only three distinct values
are used. The covariance identity is algebraically general and the executed
example is nontrivial, hence the theorem is unaffected. The description of the
specific test should say “vertex-local changes” or use four independently
chosen SU(2) matrices.

### Opening 8 — the paper points to a nonexistent final receipt

**Severity: MINOR**

Paper 11's reproducibility list names `v10/data/d10-final-receipt.md`, but the
frozen receipt is `v10/data/d10-pre-review-receipt.md` and no final-receipt file
exists in the reviewed tree. This does not affect the arithmetic, but it makes
the claimed package incomplete.

## 3. Claims that survived hostile review

The following results do **not** require mathematical revision:

1. `Herm_2(C)_+` is linearly order-isomorphic to the `3+1` future Lorentz
   cone, with normalized rank-one rays `CP^1 ~= S^2`.
2. Directional evaluations are linear functions of four real coefficients;
   normalization removes one scale and therefore does not itself supply time.
3. Every finite direction family gives an outer polyhedral cone and
   `1/m(U)-1` is the correct worst radial excess when `m(U)>0`.
4. All published Platonic and nested-family support values reproduce.
5. The R/C/H/O rank-two dimensions and spin-factor classification are
   mathematically correct, even though the preregistered executable test is
   missing.
6. Generic spin factors prove that Lorentz-cone positivity alone cannot select
   three spatial dimensions.
7. The rebit/qubit parameter counts `(3,10)` and `(4,16)` are correct for the
   unnormalized state spaces used in local-tomography counting.
8. The exact H/T projector counts through depth 12 reproduce. The numbers
   certify finite reachability, not the sampled covering minimum.
9. Link covariance, based-holonomy conjugation, trace invariance, and disjoint
   tensor-factor unitary commutation are correct.
10. The diagonal SL(2,C) example is an exact Lorentz boost and correctly shows
    why SU(2) rotation gauge is not full boost gauge for normalized quantum
    states.
11. The paper correctly refuses complex selection, a physical Bloch/celestial
    identity, an order/influence equivalence, absolute units, Einstein
    dynamics, and Newton's `G`.

## 4. Verdict audit

The final primary label `KINEMATICS-ONLY` is conservative and should remain.
The exact algebraic bridge survives. What must change are subsidiary gate
grades:

```text
A complex rank-two algebra                    PASS
B finite Platonic outer approximations        PASS
B H/T generated-sequence convergence          CONDITIONAL / proof missing
G1 alternative determinant forms              NOT EXECUTED
G3 generation without sphere oracle            PASS, diagnostic sampler present
G4 SU2 link/diamond covariance                 PASS
G4 general disjoint-instrument/order gauge     NOT EXECUTED
full SL2C physical gauge                       OPEN, correctly classified
```

Because a frozen major gate was reported as passed without its required test,
and because the construction-order PASS is supported by a tautology, the
round-1 mathematics verdict is **MAJOR REVISION**. No production artifact was
modified by this review.

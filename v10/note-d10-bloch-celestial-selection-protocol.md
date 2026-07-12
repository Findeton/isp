# D10 — Bloch–celestial selection protocol

**Status:** frozen before D10 executables, numerical outcomes, literature search,
or hostile review, 2026-07-11.

## 1. Question

V9 established the kinematic identity

\[
\ell_u(t,x)=t-u\cdot x,\qquad u\in S^2,
\]

and showed numerically that finite directional nets approach the round
four-dimensional Lorentz cone. D8–D9 established SCIR as a complete local
rulebook architecture and then refuted the identification of its Bell and
geometric transfer couplings.

D10 asks a different question:

> Does the minimal local record algebra selected by SHARD/ISP/SCIR itself
> supply the celestial `S^2` and its `3+1` Lorentz cone, or does choosing a
> complex qubit merely insert the desired dimension?

The proposed bridge is the ordered real vector space of `2 x 2` complex
Hermitian matrices,

\[
X=tI+x\cdot\sigma.
\]

Its positive cone is `t >= |x|`; its normalized rank-one boundary rays are
`CP^1 = S^2`. This algebraic fact is not yet a physical derivation.

## 2. Frozen claim layers

1. **A — exact algebra:** `Herm_2(C)_+` is the `3+1` Lorentz cone and its
   normalized null rays form `S^2`.
2. **B — finite approximation:** finite direction sets reconstruct outer
   polyhedral cones which converge to the round cone with quantified error.
3. **C — selection:** the existing SHARD/ISP/SCIR axioms select the complex
   two-level factor over real, quaternionic, higher-rank, and generic spin
   factors.
4. **D — identification:** the qubit projective sphere is the same physical
   channel object as the celestial clock sphere, without a hidden global
   spatial frame.
5. **E — dynamics:** a finite, incidence-local, gauge-covariant SCIR packet
   preserves the structure and makes finite histories approach the kinematic
   cone.

Passing A does not imply C–E. Passing A–B only earns
`EXACT-KINEMATIC-BRIDGE`. A claim of derived `3+1` requires C–E.

## 3. Frozen comparison class

D10 compares:

- classical simplices;
- `Herm_2(R)`, `Herm_2(C)`, and `Herm_2(H)`;
- the octonionic rank-two spin-factor shadow where only its ordered-space
  statement is used;
- generic Lorentz/spin factors `R \oplus R^n`;
- complex matrix algebras of rank greater than two.

For `Herm_2(F)`, the expected real ordered-space dimensions are respectively
`3, 4, 6` for `F = R, C, H`, yielding Lorentz cones `1+2`, `1+3`, and `1+5`.
This expectation is a wiring target, not a selection result.

## 4. Anti-circularity gates

### G0 — exact wiring

Pauli multiplication, Hermiticity, trace, determinant, eigenvalues,
rank-one projectors, directional evaluation, and `SU(2)` covariance must pass
in exact or at least 80-decimal arithmetic. Normal and optimized execution
must give byte-identical receipts.

### G1 — ordered-space classification

The executable must independently count the real dimensions of the rank-two
real/complex/quaternionic cases and verify their determinant quadratic forms.
It must explicitly exhibit that Lorentz-cone kinematics alone does **not**
select `n=3`: generic spin factors exist for other `n`.

### G2 — finite-clock geometry

For declared deterministic direction nets, calculate the support deficit

\[
\epsilon_K=1-\min_{|x|=1}\max_{u\in U_K}u\cdot x,
\]

and the induced radial excess `1/(1-epsilon_K)-1`. Empirical grid results
must be checked against exact special cases and independent dense probes.
No occupancy-based `F` result may substitute for this geometric error.

### G3 — no external sphere oracle

The dynamical packet fails this gate if it samples a direction from a
pre-existing globally labelled `S^2`, compares absolute directions at
separated records, or stores infinitely many clock readings. Directions must
be local projective states/observables; comparisons must be carried by
incident relative-frame tokens.

### G4 — construction gauge and locality

Spacelike-disjoint rewrites must commute as instruments. Independent local
`SU(2)` basis changes must leave all sealed probabilities and causal tests
unchanged when link transports transform covariantly. No update may inspect
the global record graph.

### G5 — finite information

Every finite record and collar has finite type and finite-dimensional state.
`S^2` denotes the continuum of possible questions/states of a finite algebra,
not infinitely many simultaneously stored classical values.

### G6 — finite-history/continuum honesty

A literal profinite inverse limit of finite discrete spaces is not to be
identified with connected `S^2`. The history space may be profinite. `S^2`
must instead arise as the projective state space/spectrum of the local algebra
or through a separately named metric/operational continuum limit.

### G7 — dynamical influence versus order cone

The order cone reconstructed from directional positivity and the propagation
front of a marked perturbation are measured separately. Equality is not
assumed. An emergent spacetime claim requires a declared relationship between
them.

## 5. Selection tests

The following are tested as possible selectors, without assuming that any
will be sufficient:

1. local tomography under composition;
2. continuous reversible transformations and transitivity on pure states;
3. nonclassical interference and Born instruments;
4. Bell-compatible composites;
5. diamond composition and path independence;
6. nontrivial sealed phase holonomy;
7. finite universal grammar closed under composition.

Each selector receives one of `proved`, `literature-supported conditional`,
`counterexample`, or `open`. D10 may not combine individually insufficient
selectors into a uniqueness claim without an explicit theorem.

## 6. Dynamic packet to be tested

The candidate packet uses finite qubit collars, local `SU(2)` frames, and
incident link transports. A link from record `a` to record `b` carries a
relative transport `U_ba`; under local gauge changes `V_a,V_b`,

\[
U_{ba}\mapsto V_b U_{ba}V_a^\dagger.
\]

Directional projectors transform locally. Loop products are sealed holonomy
tokens. The packet is tested first on finite diamonds and bounded graphs. D10
does not assume that this candidate is uniquely forced by SCIR.

## 7. Prohibited inferences

- Bell saturation does not by itself select complex quantum theory.
- A Bloch sphere is not physical space merely because both are `S^2`.
- Cone kinematics does not derive Einstein dynamics or Newton's `G`.
- More sampled directions do not prove increasing physical record capacity.
- A round order cone does not prove a matching signal/influence cone.
- `SU(2)` covariance may be an imposed symmetry; it is not counted as derived
  unless selected from earlier axioms.

## 8. Frozen verdicts

Exactly one primary verdict is issued:

- `DERIVED-S2-AND-3P1`: A–E pass and the comparison class is uniquely reduced
  to the complex rank-two factor by already-owned principles.
- `CONDITIONAL-ON-COMPLEX-QUBIT`: A–B and the local realization pass, but the
  complex rank-two factor is additional primitive physics.
- `KINEMATICS-ONLY`: A–B pass but the local identification or dynamics fails
  or remains unconstructed.
- `REFUTED-BLOCH-CELESTIAL-IDENTIFICATION`: an exact incompatibility is found
  between the two roles.

Secondary labels record selection, locality, gauge, finite-capacity,
continuum, order-cone, and influence-cone status separately.

## 9. Review protocol

After the note, executables, literature audit, receipt, and paper are frozen,
three independent hostile reviews are commissioned: mathematics; ontology,
locality, and gauge; and clean-room reproduction. Every valid opening is
investigated before a later review round. Production claims are amended rather
than silently overwritten.

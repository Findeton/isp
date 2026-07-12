# D10 literature audit — Bloch spheres, Lorentz cones, and complex selection

**Search date:** 2026-07-11. The D10 protocol was frozen before this search.
Only primary papers or primary publication pages are used for load-bearing
comparisons. The algebraic correspondence and reconstruction ingredients are
not claimed as original.

## 1. The qubit–Lorentz correspondence is established mathematics

Arrighi and Patricot explicitly identify unnormalized qubit states with the
future cone in `R^(1,3)`: `2 x 2` complex Hermitian matrices supply the four
real coordinates, pure states are null, Bloch spheres are constant-time
sections, unitaries give rotations, and positive operations are related to
Lorentz transformations. This is the direct literature precedent for D10's
exact algebraic bridge.

- P. Arrighi and C. Patricot, [A Note on the correspondence between Qubit
  Quantum Operations and Special Relativity](https://arxiv.org/abs/quant-ph/0212135).

D10 therefore claims no originality for

```text
Herm_2(C)_+ = the 3+1 Lorentz cone,
rank-one normalized rays = CP^1 = S^2,
det(tI+x.sigma) = t^2-|x|^2.
```

The contribution under test is narrower: whether this known correspondence can
be attached to SHARD's sealed records and SCIR's local rewrite law without
importing dimension, a global frame, or an external continuum of directions.

## 2. Jordan reconstructions make the selection assumptions visible

Barnum and Wilce show, subject to substantive assumptions on systems and
composites, that homogeneous self-dual/Jordan single systems, local tomography,
and the existence of at least one qubit recover ordinary finite-dimensional
complex quantum theory with superselection sectors. The theorem is important
but conditional: it assumes a qubit and a locally tomographic composite rather
than deriving both from sealed records.

- H. Barnum and A. Wilce, [Local tomography and the Jordan structure of quantum
  theory](https://arxiv.org/abs/1202.4513).

Niestegge gives another route from a formally real Jordan setting to the
self-adjoint part of a complex `C*` algebra by postulating a suitable locally
tomographic composite of two copies. Again, local tomography is the selecting
postulate, not a consequence of a Lorentz cone.

- G. Niestegge, [Local tomography and the role of the complex numbers in
  quantum mechanics](https://arxiv.org/abs/2001.11421).

Barnum, Graydon, and Wilce analyze composites of Euclidean Jordan algebras and
show how real, complex, and quaternionic models can inhabit broader monoidal
constructions when local tomography or purity preservation is relaxed. This is
the relevant warning against treating the complex rank-two algebra as the only
mathematically composable option.

- H. Barnum, M. Graydon, and A. Wilce, [Composites and Categories of Euclidean
  Jordan Algebras](https://arxiv.org/abs/1606.09331).

## 3. The corpus had already found the selecting-bit wall

V8 Paper 2 independently localized the complex-over-real distinction to the
composition/local-tomography layer. In its finite arena:

```text
rebit: K_single=3, K_pair=10, deficit=10-3^2=+1;
qubit: K_single=4, K_pair=16, deficit=16-4^2=0.
```

The sealed degree-`(1,1)` moment data are invariant under the relevant
complex-to-real reduction while the local-tomography deficit changes. Its
verdict was therefore field blindness: the existing record observables do not
select the bit. D10's repaired 109-check exact receipt reproduces the parameter
counts, executes the rank-two comparison determinant forms, and adds the
Lorentz classification.

This prior no-go is directly relevant. A local-tomography axiom can select the
complex theory within the stated reconstruction framework, but the current
SHARD principles do not derive that axiom. Importing it would make `3+1`
conditional on new composition physics.

## 4. Current real-versus-complex status is composition-sensitive

Renou et al. proved a separation between standard complex quantum theory and a
real-Hilbert formulation retaining a specified real tensor-product composition
and source-independence structure, and proposed a network experiment.

- M.-O. Renou et al., [Quantum theory based on real numbers can be
  experimentally falsified](https://www.nature.com/articles/s41586-021-04160-4),
  *Nature* 600, 625–629 (2021).

The interpretation is currently contested. Hoffreumon and Woods argue that the
separation depends on an operationally untestable product-state independence
assumption and construct real simulations for finite operational networks.

- T. Hoffreumon and M. P. Woods, [Quantum theory based on real numbers cannot
  be experimentally falsified](https://arxiv.org/abs/2603.19208) (2026
  preprint).

Maioli, Curado, and Gazeau give a real Kähler representation with a symplectic
composition rule that is explicitly isomorphic to complex quantum mechanics.

- A. C. Maioli, E. M. F. Curado, and J.-P. Gazeau, [Quantum mechanics over real
  numbers fully reproduces standard quantum theory](https://arxiv.org/abs/2604.19482)
  (2026 preprint, v3).

Moradi Kalarde, Xu, and Renou challenge the claimed generality of the
operational-independence postulate by testing it against fermionic information
theory.

- F. Moradi Kalarde, X. Xu, and M.-O. Renou, [Comment on "Quantum theory based
  on real numbers cannot be experimentally falsified"](https://arxiv.org/abs/2604.07425)
  (2026 preprint).

D10 does not adjudicate this active dispute. Its robust lesson is that the
physical content lies in the ordered operational state space and its
composition rule, not in whether a calculation happens to print complex or
real coordinates. A real Kähler representation that carries the same complex
structure does not turn the operational Bloch sphere into a rebit circle. The
true alternative is a different composition/state-space theory, and current
sealed records do not select between those alternatives.

## 5. A finite grammar can expose densely many directions

The Clifford+T synthesis literature establishes that a finite gate alphabet can
generate the exact ring used in D10's finite packet and support approximation
of arbitrary single-qubit operations. It is therefore unnecessary for a finite
record to store an independent scalar for every point of `S^2`.

- V. Kliuchnikov, D. Maslov, and M. Mosca, [Fast and efficient exact synthesis
  of single qubit unitaries generated by Clifford and T
  gates](https://arxiv.org/abs/1206.5236).
- V. Kliuchnikov and J. Yard, [A framework for exact
  synthesis](https://arxiv.org/abs/1504.04350).

D10's local `H/T/SEAL` candidate demonstrates the finite-history side exactly:
113 distinct projective directions are reachable by depth 12, all represented
in `Q(sqrt(2),i)`, with no call to a sphere sampler. The finite-alphabet result
does not select that alphabet as nature's law.

## 6. Rotations are not full Lorentz covariance

The standard matrix correspondence distinguishes:

- `SU(2)` conjugations, which preserve trace and give spatial rotations;
- `SL(2,C)` congruences, which preserve determinant and give the proper
  Lorentz group on the Hermitian four-vector;
- nonunitary filters/positive operations, whose normalized quantum-state
  interpretation changes branch weights.

D10 verifies this distinction exactly with an `SL(2,C)` diagonal boost. It
preserves `det X` but is nonunitary and changes `Tr X`. Consequently a local
`SU(2)` record-frame gauge is sufficient to avoid a preferred spatial axis but
not sufficient to establish boost covariance. Treating a nonunitary quantum
filter as mere gauge would require an additional probability/normalization
law. No searched reconstruction supplies that law from sealing alone.

## 7. Profinite boundary

An inverse limit of finite discrete compact spaces is profinite and therefore
totally disconnected. A connected sphere cannot literally be that inverse
limit. D3's profinite history result can support cylinder measures and
compatible finite histories, but it does not construct the channel sphere.

The mathematically clean options are:

1. `S^2` is already the projective pure-state space of a finite local algebra;
2. finite operational nets converge to it in a metric/Hausdorff sense;
3. finite histories carry increasingly accurate `S^2`-valued observables.

Only the history carrier in option 3 is profinite. D10 adopts option 1 for the
conditional qubit packet and uses option 2 for finite clock approximations.

## 8. Literature verdict

```text
QUBIT-LORENTZ CORRESPONDENCE: established, imported;
FINITE-GRAMMAR DENSE DIRECTIONS: established in synthesis theory, imported;
COMPLEX SELECTION FROM LOCAL TOMOGRAPHY: conditional theorem, imported;
LOCAL TOMOGRAPHY FROM SEALED RECORDS: not found; contradicted in the current
  finite record arena by V8 field blindness;
SU2 FRAME GAUGE -> FULL LORENTZ GAUGE: false without an SL2C extension;
PROFINITE HISTORY -> CONNECTED S2: false if read literally.
```

The D10 synthesis is therefore useful but not a derivation of `3+1`: it
identifies the precise additional structures that would make the v9 slogan a
SCIR mechanism.

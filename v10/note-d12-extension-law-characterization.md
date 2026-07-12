# D12 characterization — the between-diamond generative problem

**Status:** frozen before the D12 nonuniqueness executable, 2026-07-11.

## 1. What must be selected

For every sealed boundary/collar `B` and sealed past `H`, a generative law must
supply a probability or decoherence-functional weight on typed extensions:

```text
Ext(B) = {e: lower screen matches B and every incoming leg is owned}.
```

An extension includes:

```text
new diamond type;
incoming collar owners;
whole-history atom/outcome;
instrument/amplitude;
upper output collars;
new locally emitted opportunities;
frame links and order units;
durable record fields.
```

The law is complete only when it selects both the support `Ext(B)` and the
weight of every element. A conditional formula on an already supplied support
does not solve birth.

## 2. Identifiability is not generation

Let a fixed finite diamond history space have `m` positive atoms and reference
measure `mu`. A complete set of `m-1` independent nonconstant contrasts spans
functions modulo constants. Therefore

```text
positive P on Omega
<->
complete log-RN coefficient vector h
```

is a bijection. This is V6's complete closed-holonomy reconstruction theorem.

It proves that a supplied complete ledger loses no future-relevant history. It
does not select the ledger coefficients: every strictly positive alternative
law has its own complete coefficient vector. Calling the full log-density
“intrinsic holonomy” can only be generative if a separate physical theorem
computes that holonomy before the probabilities are known.

## 3. What the commitment fixed point can and cannot do

For fixed `Omega,mu,chi`, define

```math
psi(h)=log E_mu exp(<h,chi>),
Phi(h)=psi(h)+sum_j exp(-h_j).
```

On a fixed primitive positive orientation, strict convexity can give a unique
critical point

```math
nabla psi(h)=exp(-h).
```

This selects one coefficient vector inside that fixed presentation. It does
not select:

```text
the extension support and number/types of output collars;
the reference measure on inequivalent extension types;
which contrast modes are primitive versus composite;
orientation when no arrow-readout fixes it;
the quantum instrument attached to an extension;
the interaction unitary/coupling;
the entangling joint-content functional;
the complex-rank-two versus other local algebra;
the realized magnitude of physical holonomy increments.
```

Changing any of these changes `psi` itself. Uniqueness of a minimizer of one
`Phi` is not uniqueness among physical `Phi` functionals.

## 4. Frozen countermodel family

The exact executable must construct two packets with all of the following in
common:

```text
one connected typed two-leg collar;
durable commit plus continuing output collars;
no terminal internal rewrite;
the same local RN evidence survival law;
the same projective pointer family;
the same local frames/order units;
the same bounded grammar and opportunity ownership;
the same commitment coefficient on a fixed scalar ledger;
exact endpoint dual-gauge covariance;
exact disjoint construction commutation;
no-signalling at the local quantum-instrument level.
```

They differ only in the two-leg interaction packet:

```text
Packet S: SWAP;
Packet C: controlled-NOT.
```

Both are exact local unitaries with the same input/output dimensions and no
free terminal deletion. On input `|10>`, SWAP gives `|01>` and controlled-NOT
gives `|11>`, so a later second-leg seal differs. If every structural gate
passes for both, locality, covariance, commitment, projectivity, continuation,
and the restored diamond types do not select the interaction.

This is a deliberately elementary witness. One counterexample pair is enough
to refute uniqueness. A later audit must ask whether an independent physical
principle—symmetry representation, observed scattering data, renormalization,
or a specified microscopic Hamiltonian—selects one. Favorable geometry may
not do so post hoc.

## 5. Whole-history countermodel

The executable must also construct the exact family

```math
P_r(x,y,z)={1+r xyz\over8},
```

for rational `|r|<1`. Every member has identical uniform one- and two-record
marginals, exact projective coarse laws, and a future-relevant triple history
contrast. Different `r` values give different continuation conditionals.

The complete ledger identifies `r`; it does not derive it. Pairwise/current
state shadows cannot select it. This is the finite non-Markovian version of
the same no-go.

## 6. Decision rule

If the two interaction packets and at least two `P_r` histories survive the
frozen structural gates, the verdict is

```text
UNIVERSAL-FORM/PRIMITIVE-MEASURE-REMAINS.
```

To overturn that result, a selection principle must be stated independently,
must reject all but one countermodel for a physical—not representational—
reason, and must make a novel holdout prediction.


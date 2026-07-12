# D6 hostile round-1 mathematics / probability / corpus-fidelity review

**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION**  
**Core RN/Walsh/hidden-lift mathematics:** confirmed  
**Core conditional commitment calculation:** confirmed at its stated scalar
primitive-mode scope  
**Reason for grade:** one central ownership gate is vacuous, the profinite
witness is only a relabeling mirror, and several corpus/scope claims need
executable or textual repairs

## Frozen sources reviewed

- `v10/note-d6-sealed-holonomy-factor-token.md`  
  SHA-256 `daf14e0ea008509e106fd6419ee463b964b5b1a15a9d61ed6e6842a432434c20`
- `v10/code/d6_sealed_holonomy_token_exact.py`  
  SHA-256 `7de6f94a4cf77eb780da245e26a60d6677be1c59fd6233a3dfd1e8f18d8c0388`
- `v10/relativistic-isp-v10-paper7-sealed-holonomy-reconstructs-change-not-birth.md`  
  SHA-256 `63ad2759c4355143fc2f0f66658294a01a0b56b16ba992143be67e8983ecc9d0`

The executable was run twice. Both runs reported 60/60 and had byte-identical
stdout SHA-256
`fa513bd65bf6f674a2b203e4e35192b58b8ecdec0018637a3a9528c63f375a4c`.

## Independent reconstruction

I rebuilt the decisive witnesses without importing the production code:

```text
binary RN field:                         1/3, 3
E_Q[R] and E_P[1/R]:                    1, 1
directed KL:                             (1/2) log 3
three-bit proper-shadow equality:        exact
triple moments:                          +1/2, -1/2
lower log-Walsh coefficient equality:    exact analytically
top log-Walsh coefficients:              +(1/2)log3, -(1/2)log3
hidden-lift RN equality:                 exact
hidden future split:                     7/12, 5/12
commitment root:                         0.6093778634360062315368033711...
two-bit parity RN table:                 3/2,1/2,1/2,3/2
cross determinant:                       2
Bernoulli towers:                        exact projectivity
p=1/3 versus p=2/3 under global flip:    exactly the same orbit
```

The headline arithmetic is reproducible. The revision grade concerns what
the receipt actually certifies and the physical/corpus quantifiers attached
to it.

## 1. RN and KL statements

For strictly positive normalized laws `P,Q` on the same finite atom space,

$$
R=\frac PQ,
\quad E_QR=1,
\quad E_P R^{-1}=1,
\quad P=QR
$$

are exact. Reversal inverts `R`; independent products multiply it; joint atom
relabeling relabels it. For the swapped binary witness,

$$
D(P\Vert Q)=D(Q\Vert P)=\frac12\log3,
$$

while the fields are inverse. The Decimal report agrees to its working
precision and no incidence verdict depends on a transcendental tolerance.

The essential-coordinate routine correctly returns the unique minimal set of
listed coordinates on which a function over a full binary product varies.
Paper 7 qualifies this scope as presentation-relative and conditional on the
supplied ordered pair. That qualification is necessary and correct.

### Opening 1 — define the null field unambiguously

The token census writes `null = R == 1`. This must mean `R` is **identically**
one, equivalently `P=Q`, not merely that one atom has unit ratio.

**Repair:** use `R equiv 1` throughout the note, paper, and token schema.

## 2. Walsh dimension and reconstruction

On the full `n`-bit atom cube, the Walsh matrix has rank `2^n`. Modulo the
constant, the log-density has `2^n-1` coefficients, matching the dimension of
the strictly positive simplex. Fourier inversion of `log(P/mu)`, followed by
normalization, reconstructs the supplied positive law. These are correct
finite identifiability statements.

For the parity twins,

$$
\log(1+\theta\chi)=a(\theta)+b(\theta)\chi.
$$

Replacing `theta` by `-theta` preserves `a` and reverses `b`. Therefore all
lower log-Walsh coefficients agree and the omitted top coefficient leaves a
genuine two-law fiber. The production high-precision reconstruction is
consistent with this exact argument.

### Opening 2 — positivity domain is missing from the frozen family

The note defines `P_theta=2^{-3}(1+theta x1x2x3)` “for rational theta” without
stating the probability-law condition. Strict positivity requires

$$
-1<\theta<1.
$$

At the endpoints support is singular; outside that interval some cells are
negative.

**Repair:** add `theta in Q intersect (-1,1)` everywhere the family is called
a positive law. Likewise state `p in Q intersect (0,1)` for positive
Bernoulli towers.

### Opening 3 — H3 is not actually gated

H3 preregisters that dropping the top parity channel leaves a nontrivial
fiber. The executable checks proper marginals, whole-law inequality, and that
the top coefficient of one law is nonzero. It never computes the second law's
log-Walsh vector or verifies equality of every lower coefficient. The theorem
is true, but the advertised exact gate is incomplete.

**Repair:** transform both `+theta` and `-theta`; assert equality of masks
`0,...,6`, opposite nonzero mask-7 coefficients, and unequal reconstructed
laws after choosing opposite top signs.

The paper correctly downgrades “complete closed holonomy” to a supplied
complete separating cochain. Fourier dimension counting does not prove that a
physical diamond constructs that cochain or its primitive modes.

## 3. Hidden-history lift

The hidden-lift witness is exact. Within each lift the same conditional
`P(H|E)=Q(H|E)` cancels from the RN derivative, so both lifted ordered pairs
have the same endpoint field and the same full lifted RN field, depending only
on `E`. Changing that common conditional leaves endpoint laws fixed but moves
`P(H=+1)` from `7/12` to `5/12`.

This proves exactly the stated ceiling: an RN comparison is complete only on
the atom space on which its two laws were supplied. It cannot certify that the
chosen atom space already contains every future-relevant distinction.

## 4. Commitment root, orientation, and sealing

Conditional on additive evidence `I`, continuity and the v6 self-accounting
premise give `S(I)=exp(-I)`. The one-mode equation

$$
\tanh h=e^{-h}
$$

has one positive root because its residual is strictly increasing, negative
at zero, and positive at infinity. The independent root and the reported
110-digit value agree. Reversing a supplied parity statistic mirrors the
exponential-family law; choosing a parity statistic of another arity gives
the same scalar log-partition `log cosh h`. Thus the scalar equation selects
a coefficient only after a primitive oriented balanced mode is supplied.

### Opening 4 — the scope test is too weak

The executable's scope check is only

```python
parity_law(1, 1/2) != parity_law(2, 1/2)
```

which is automatic for laws on different atom spaces and does not audit the
commitment root. The mathematical claim is true because every balanced parity
mode has `psi(h)=log cosh h`, but that proof is absent from the receipt.

**Repair:** construct the root-induced one-body and many-body exponential
families, verify the same root equation for both, verify their different
essential scopes, and then show orientation reversal mirrors each.

### Opening 5 — preserve the v7 Paper 32 bridge gap explicitly

V7 Paper 32 sustains the objection that the v6 commitment root has not been
proved equal to the effective forward `h` required in the Paper 31
h-transform. D6 correctly treats the h-transform domain and weights as
supplied, but it never states this corpus guardrail explicitly.

**Repair:** add

$$
h_{\rm commitment,\mathcal P_N}
\stackrel{?}{=}
h_{\rm effective,\mathcal P_N}
$$

as an open identification. Do not let “conditional commitment coefficient”
be read as recovery of the v7 forward weight.

The seal law is also conditional on actual additive evidence. It is not a
proposal intensity, candidate selector, null mass, or accepted birth law.

## 5. Proposal, h-transform, and ownership

The two null-inclusive symmetric proposal distributions exactly demonstrate
that reversal symmetry leaves null mass free. The finite h-transform example
also correctly shows that normalization compiles a supplied domain and
positive weight field; changing either changes the transition.

### Opening 6 — the ownership receipt gate is vacuous

After verifying extensional factorization, the executable claims to check
that the joint law does not encode primitive token census with

```python
check(1 != 2, "joint law does not encode primitive token census")
```

This condition is independent of every constructed object. It is precisely
the sort of tautological gate earlier hostile rounds rejected.

**Repair:** construct two explicit representations of the same factorized RN
field:

1. one composite two-scope token with one ID;
2. two unary primitive tokens with two distinct IDs.

Assert identical extensional tables, unequal token/ID censuses, distinct
ownership partitions, and exactly-once compatibility with the D5 compiler.
The paper's nonidentifiability argument is valid, but the current receipt does
not certify it.

## 6. Cross-factor irreducibility

The two-bit parity factor is

$$
(3/2,1/2,1/2,3/2)
$$

and its determinant is exactly `2`. Hence it is not a direct product
`R1(x)R2(y)`. A product of independent component RN fields has determinant
zero. The production and independent calculations agree.

This determinant excludes a product across the declared cut; it does not by
itself exclude a representation using a newly supplied shared latent
mediator. Such a mediator would itself be the joining/bridge sector whose
origin remains missing. Paper 7's current wording preserves this distinction.

## 7. Profinite/projective claim

Each rational Bernoulli product family is normalized and projectively
compatible, and its product formula extends beyond the five audited levels.
Finite discrete consistency therefore defines an inverse-limit path measure.
Compatibility plainly does not choose the Bernoulli parameter.

### Opening 7 — the two audited towers are relabeling mirrors

The chosen pair `p=1/3` and `p=2/3` is exchanged by the global outcome flip
`x -> -x` at every level. Thus the code proves dictionary inequality on the
labeled atom presentation, but not inequivalence after quotienting by that
outcome relabeling. Because D6 itself treats orientation as unselected, the
distinction matters.

**Repair:** either:

- explicitly call F2 labeled/oriented nonselection; or
- add a third tower such as `p=1/2`, which is not in the flip orbit of
  `p=1/3`, and gate inequivalence of canonical relabeling orbits.

The broader hosting-not-selection conclusion is true. The receipt does not
construct a typed holonomy-coordinate bonding law, proposal process, or new
general profinite theorem, and the paper should remain at that ceiling.

## 8. Corpus fidelity

### V6 Paper 4 sections 34 and 38

D6 faithfully imports the RN exchange cocycle as canonical only **after** the
two ordered transport laws are supplied. It also faithfully reproduces the
pairwise-parity and fixed-endpoint/action hidden-lift obstructions from the
whole-history determination campaign.

### V6 Paper 4 section 40

The finite Walsh reconstruction is faithful to the mathematical part of the
Complete Closed-Holonomy Whole-History Law. D6 correctly identifies the hard
physical clause: the diamond must intrinsically supply a complete
future-relevant contrast ledger. Dimension matching alone is identifiability,
not selection.

### V6 Paper 4 sections 71--76

The scalar survival and one balanced primitive-mode root are faithful slices
of the commitment program. D6 does **not** execute the coupled-ledger strict
convexity theorem, cofinal primitive quotient, or admissible-cover
independence. It should therefore continue to claim only the audited scalar
conditional coefficient, not the full sections 73--76 closure.

### V7 Papers 31--32

D6 correctly treats the h-transform as a compiler after candidate domain,
deletion multiplicities, and positive weights exist, and correctly retains
Paper 31's finite/teacher-dependent guardrail. Opening 5 above is the one
missing fidelity sentence: Paper 32 explicitly says the commitment root has
not yet been identified with the effective forward h-weight.

## 9. Minor executable/paper issues

1. `normalize()` is unused and checks only positive total, not nonnegative
   cells. Either remove it or make it a valid probability normalizer.
2. The profinite summary sentence is duplicated verbatim in Paper 7 section
   10.
3. The token-field missing-count check validates a hard-coded status table;
   present it as a census print, not an independent derivation.
4. State all positivity/common-support hypotheses beside any RN or KL formula,
   not only at the start of the finite arena.

## Final adjudication

The defensible mathematical result is:

```text
supplied positive ordered laws on a fixed finite atom space
  -> exact RN factor, relative scope, orientation, and directed KL;
supplied complete log-density cochain
  -> finite-law reconstruction, not cochain selection;
supplied primitive balanced oriented mode plus v6 premises
  -> conditional commitment coefficient and evidence-time survival;
none of these
  -> proposal opportunity, null mass, physical ownership, or accepted birth.
```

That core is valuable and correct. The vacuous ownership gate, mirror-only
profinite witness, underexecuted scope/fiber gates, and missing Paper 32 bridge
guardrail require **MAJOR REVISION** before a final receipt can be accepted.

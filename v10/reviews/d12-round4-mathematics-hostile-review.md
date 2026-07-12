# D12 focused hostile round-4 mathematics receipt review

**Date:** 2026-07-11  
**Verdict:** **PASS — ROUND-3 MATHEMATICS CLOSURE CONFIRMED**  
**New opening:** none  
**Scope:** the explicit `A_D12` finite-packet/unitary-frame theorem only

## Frozen receipt reproduction

The reviewed frozen artifacts match the declared hashes:

```text
54c2c6e1f193658924e3ac35e52ca897f95a07dbd4412bf86b4b0f0e0fb2b74b  code/d12_multidiamond_history_exact.py
05ecdc0a99859ea3d2b8cc99e39edfc9d8e84ed8d1c02ab55ba715a16711a21c  relativistic-isp-v10-paper13-the-click-law-is-the-whole-history-process.md
```

I ran the executable under normal and optimized Python.  The outputs were
byte-identical and matched the frozen values:

```text
checks                  = 145
stdout SHA-256 normal   = 466cbfc9dbdfb4432428779b1f4054921a98f3869c3aa665ba723e7e0a623521
stdout SHA-256 -O       = 466cbfc9dbdfb4432428779b1f4054921a98f3869c3aa665ba723e7e0a623521
semantic receipt        = d48f9a161dd3e7f850726225d9ea3faad8433fe35ede0c3957cbbb0963e691c6
```

No floating-point arithmetic enters the audited probability, RN, history, or
frame-domain verdicts.

## 1. Support-relative RN reconstruction

**Confirmed exact.**

For a stored law `P`, reference `mu`, and declared positive support `S`, the
repair computes

$$
R_i=\frac{P_i/P(S)}{\mu_i/\mu(S)},\qquad i\in S,
$$

and stores the `|S|-1` projective coordinates

$$
q_i=\frac{R_i}{R_*}
$$

relative to the last support atom.  Support, restricted reference, and these
ratios uniquely recover the normalized law: the common scale is fixed by
normalization.  Equivalently,

$$
P_i=\frac{q_i\mu_i}{\mu_*+\sum_{j\ne *}q_j\mu_j},
\qquad
P_*=\frac{\mu_*}{\mu_*+\sum_{j\ne *}q_j\mu_j},
$$

with the obvious adjustment if the reference is first normalized on `S`.

For quarter-iSWAP,

```text
S = (1,2)
P|S = (1/2,1/2)
mu|S normalized = (1/2,1/2)
stored RN contrast ratio = 1
```

which is correct.  For half-iSWAP the positive support is the singleton `(2,)`,
so the nonconstant coordinate space has dimension zero and the stored tuple is
correctly empty.

The executable derives the actual support from nonzero law entries before any
division.  A packet with a false support `(0,3)` is rejected immediately.  A
quarter packet with the false ratio `7` is also rejected.  Thus the new PASS is
not another length-only or inequality-only gate; it depends on the stored
probabilities and reference measure.

This repair does not claim that the two interactions have the same positive
support.  They share the ambient pointer carrier, grammar, reference, contrast
ledger, evidence data, screens, and types; their different induced supports
are part of their physically different laws.

## 2. Paper support-domain statement

**Confirmed.**

Paper 13 now explicitly says that when an ambient Born law has exact zeros,
`h_D` is defined after restriction to positive support and has nonconstant
dimension `|support|-1`.  It rejects atomwise `-infinity` as a finite contrast
coordinate and states that the receipt reconstructs support-relative RN ratios
and rejects mutations.

This is the clarification requested in round three.  It aligns the quantum
zero-bearing packets with the strictly positive finite RN theorem rather than
silently applying that theorem outside its domain.

## 3. Lower- and upper-frame domain repair

**Confirmed exact at the declared unitary scope.**

The input-collar eligibility predicate now requires

$$
B_{\rm lower}^\dagger B_{\rm lower}=I,
$$

as well as the correctly transported lower screen and order unit.  The firing
operation separately checks the newly supplied upper frame before constructing
the link:

$$
B_{\rm upper}^\dagger B_{\rm upper}=I.
$$

A concrete nonunitary diagonal frame is rejected in both positions.  The upper
test occurs before link, screen, state, or record construction, so a caller
cannot bypass the declared gauge domain by supplying a valid lower collar and
an invalid destination frame.

Within the admitted domain the earlier transport identity remains unchanged:

$$
L_{j+1,j}=B_{j+1}UB_j^\dagger,
$$

and cylinder probabilities remain invariant.  The code and paper continue to
refuse any claim of full nonunitary Lorentz-frame integration.

## 4. Effect on the final theorem

The repairs strengthen premises already named in `A_D12`; they do not alter
the countermodel logic.  Quarter- and half-iSWAP still enter the same ambient
packet grammar, pass the same typed/projective/construction/unitary-frame
audits, continue at all depths within the proved packet induction, and disagree
on the same durable-record probability `1/2` versus `0`.

Therefore the direct two-model conclusion still follows:

```text
A_D12 does not entail a unique interaction coupling or induced history measure.
```

The support-relative RN repair does not accidentally freeze or select the
interaction; it faithfully identifies each supplied positive-support law.
The upper-frame guard does not enlarge covariance beyond the theorem's stated
unitary domain.

## Closure ledger

```text
support-relative RN coordinates and ratio reconstruction   PASS
false RN-ratio mutation refusal                            PASS
false positive-support mutation refusal                    PASS
support-relative h_D editorial statement                   PASS
lower-frame unitary-domain refusal                         PASS
new upper-frame unitary-domain refusal                     PASS
round-3 arbitrary-n/projective/threshold/poset results      UNCHANGED
final A_D12 two-model theorem                              UNCHANGED AND VALID

new fatal/major/moderate mathematical opening              NONE
```

## Final verdict

**PASS.**  The 145-check receipt is reproducible, the two new negative controls
are semantically connected to the claimed objects, and the paper now states the
support domain correctly.  My round-three conclusion remains in force:
mathematics is closed at the explicit `A_D12` finite-packet/unitary-frame scope.
Nothing in this review upgrades D12 into the universe's selected click law;
the primitive-process and geometry refusals remain essential.

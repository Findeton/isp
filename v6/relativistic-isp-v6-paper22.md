# Paper 22 (v6) - SHARD: The Sign Campaign

Preprint, not peer reviewed, version 2026-06-10.

Author: Felix Robles Elvira

Subtitle:

```text
Tier 2a: the plan's sharpest kill condition, tested at every scope this
campaign reaches - and passed at all of them.  (i) The one-loop sign
arithmetic (named-import formula, p18e-COMPUTED indices, P19 floor
content x 3 + the P20 doublet): SU(3) b0 = +7 (asymptotically free:
QCD confines), SU(2) b0 = +13/4 (free), U(1) b0 < 0 (infrared-free:
QED safe) - THE SIGN STRUCTURE OF THE STANDARD MODEL HOLDS FOR THE
RECONSTRUCTED RECORD CONTENT.  (ii) The record-native flow direction:
vectorized SU(2) record ensembles on 4^4 (plaquette curve matching
literature values, <P>(2.4) = 0.629), gauge-record decimation to 2^4,
and coupling matching: beta_eff = 0.82 from beta = 2.40 - the record
RG moves the nonabelian sector TOWARD STRONG COUPLING (the confining
direction).  (iii) The condensate signal: quenched 2d gauge ensembles
pull the record GW spectrum INTO the free gap (mean first-nonzero
0.32 vs free gap 0.77; 32 sub-gap modes across 6 configs vs 0 free)
with exact topological zeros appearing config by config - the
Banks-Casher signal of chiral symmetry breaking at toy scope.  The
weak-coupling record beta function AT SCALE remains O7's named
remainder (the P10 closure obstruction persists) - stated, not hidden
```

## 0. Verdict

```text
(i) NECESSITY (p22a; import-evaluated, indices computed):
   SU(3): b0 = 11 - (2/3)(3 gen x 2) = +7.00   ASYMPTOTIC FREEDOM
   SU(2): b0 = 22/3 - (2/3)(3 x 2) - 1/12 = +3.25
   U(1):  b0 = -(2/3) sum Y^2 - (1/3) Y_H^2 = -6.83   INFRARED-FREE
   The kill condition (wrong sign) DOES NOT FIRE at one-loop scope
   for the content Papers 17-21 assembled.
(ii) DIRECTION (p22b; record-native, 4^4 SU(2), checkerboard
   Metropolis): single-plaquette curve 0.194 -> 0.702 across beta =
   0.8..2.8 (the beta = 2.4 value 0.629 matches the literature);
   gauge-record decimation (coarse link = transport product, the P14
   blocking) gives coarse plaquette 0.198, matching beta_eff = 0.82
   from beta = 2.40: the record RG runs the nonabelian record sector
   TOWARD CONFINEMENT in the crossover window.
(iii) CONDENSATE (p22a; quenched 2d U(1), record GW): the ensemble
   pulls the spectrum into the free gap (first-nonzero 0.32 vs 0.77;
   32 sub-gap modes vs 0) and populates exact topological zeros (the
   P14 index theorem live in the ensemble): rho(0) > 0 - the chiral-
   symmetry-breaking signal, Banks-Casher-flavored, at toy scope.

HONEST RESIDUE: the continuum-scale record beta function (the genuine
O7) is NOT computed here - P10's obstruction (the Wilson family is not
closed under the series step) stands; what this campaign establishes
is that every scope SHARD can currently reach gives the RIGHT signs
and directions.  A wrong sign anywhere would have killed the route;
none appeared.
```

## 1. Method and reproducibility

```text
code/v6_p22a_sign_necessity_campaign.py  one-loop arithmetic +
                                         Banks-Casher toy (quenched
                                         U(1) 8x8, record GW spectra)
code/v6_p22b_flow_direction_campaign.py  SU(2) 4^4 ensembles,
                                         record decimation, matching
```

Both scripts rerun bit-identically (fixed seeds; statistical errors
printed in place).  Named imports: the one-loop beta-function formula;
the Banks-Casher relation as the continuum frame.  Record-native: the
GW spectra on sampled ensembles (P14 operator), the decimation rule
(P14/P18), the matching method.

## 2. The necessity check: one-loop signs for the reconstructed content

### 2.1 The arithmetic

The one-loop coefficient (named import) for gauge group G with Weyl
fermion and complex-scalar content:
b0 = (11/3) C2(G) - (2/3) sum_Weyl T(R) - (1/6) sum_scalars T(R) - all
T(R) values from p18e's computed tables, the content from P19's floor
(x 3 generations, P21's nu_R neutral) plus P20's doublet:

```text
  SU(3): per generation, color-charged Weyl T-sum = (2 + 1 + 1)(1/2)
         = 2 (Q's two weak components, u^c, d^c):
         b0 = 11 - (2/3)(3 x 2) = +7.0000      ASYMPTOTICALLY FREE
  SU(2): per generation, weak-charged Weyl T-sum = (3 + 1)(1/2) = 2
         (Q's three colors, L); scalar doublet T = 1/2:
         b0 = 22/3 - (2/3)(3 x 2) - (1/6)(1/2) = +3.2500   FREE
  U(1):  b0 = -(2/3) sum_Weyl Y^2 - (1/3) Y_H^2 = -6.8333 < 0
         INFRARED-FREE
```

The Standard Model's sign structure - confining color, free weak,
infrared-safe hypercharge - holds for the content the record ontology
reconstructed and selected.  Status: an import-evaluated NECESSITY
check, honestly labeled: the formula is standard, the content and
indices are the corpus' own.  Had any sign come out wrong, the
candidacy would have ended here.

## 3. The record-native flow direction

### 3.1 Method

SU(2) pure-gauge record ensembles on 4^4 with the Wilson weight,
sampled by vectorized checkerboard Metropolis (links updated in parity
classes so no two simultaneously-updated links share a plaquette;
proposal pool of near-identity SU(2) elements with their inverses).
The record RG acts on gauge sectors by LINK DECIMATION (P14/P18:
coarse link = transport product of two fine links).  The direction
receipt: locate the decimated ensemble on the measured single-
plaquette curve - if the matched coupling beta_eff is SMALLER than
beta, the flow runs toward strong coupling (confinement).

### 3.2 Receipts

```text
the curve:    beta   0.8     1.2     1.6     2.0     2.4     2.8
              <P>   0.1941  0.2913  0.4003  0.5196  0.6293  0.7023
              (+-0.0013..0.0030; <P>(2.4) = 0.629 matches the
              literature value - the external sanity anchor)
the blocked   fine <P>(2.4) = 0.6381 +- 0.0015; coarse plaquette
ensemble:     after record decimation = 0.1979
the match:    beta_eff = 0.82  from  beta = 2.40
```

The record decimation moves the SU(2) gauge sector strongly TOWARD
strong coupling in the crossover window - the confining direction.
Scope, stated: 4^4 -> 2^4, one blocking step, one beta - a DIRECTION
receipt, not a beta function; the large drop reflects the crude
single-step blocking (no smearing), and its SIGN is the claim.

## 4. The condensate signal

### 4.1 Method

Quenched compact U(1) ensembles on 8x8 at beta = 2 (Metropolis on link
phases), probed by the gauge-coupled record GW operator (P14).  The
Banks-Casher relation (named frame) ties the chiral condensate to the
spectral density at zero: the receipt compares the low-lying GW
spectrum on ensemble configurations against the free operator,
EXCLUDING exact zeros (which are index-theorem topology, counted
separately - physics, not noise).

### 4.2 Receipts

```text
free record GW:    2 exact zeros (the k = 0 physical mode); first
                   nonzero level = 0.7654 (the free gap)
ensemble configs:  topological zeros appear config by config (2, 1,
                   0, ... - the index theorem LIVE in the ensemble);
                   first nonzero levels 0.4593, 0.3503, 0.1661, ...
summary:           mean first-nonzero 0.3201 vs free gap 0.7654
                   (ratio 0.42); 32 modes below the free gap across
                   6 configs vs 0 free
```

The gauge medium pulls the record fermion spectrum INTO the free gap -
the accumulation toward zero that rho(0) > 0 requires - and populates
exact topological zeros exactly as P14's index theorem demands.  At
quenched 2d toy scope, the record fermions respond to the gauge
ensemble in the chiral-symmetry-breaking direction.

## 5. What this paper proves and does not prove

Proves/establishes at stated scope: the one-loop sign structure for
the reconstructed content (arithmetic exact given the computed
indices); the strong-coupling-ward flow direction of the decimated
SU(2) record ensemble in the crossover window (with literature-
matching plaquette values as the sanity anchor); the spectral
accumulation and live topological zeros of the record GW operator in
gauge ensembles.

Does not prove: the record beta function at weak coupling/scale (O7
remainder, named; P10's closure obstruction - the Wilson family is
not closed under the series step - stands); confinement as a theorem
(the area-law DYNAMICS); unquenched effects; anything in 4d beyond
the direction receipt.  The honest summary: every reachable scope
gives the right sign; the unreachable scope is named, not hidden.

## 6. The kernel after Paper 22

```text
SIGN KILL-CONDITION: PASSED at all reached scopes (one-loop necessity;
  flow direction; condensate signal).
O7: narrowed to the weak-coupling record beta function at scale
  (named; the obstruction is P10's closure problem, unchanged).
O8-remainder: the interacting flow now has its first gauge-ensemble
  data point (the condensate toy).
KERNEL otherwise unchanged.
```

## References and literature map

- Papers 10, 14, 18-21 (internal): the record RG and its closure
  obstruction, the GW operator and index, the reconstructed content.
- D. J. Gross and F. Wilczek; H. D. Politzer (1973): asymptotic
  freedom (the necessity import).
- T. Banks and A. Casher, Nucl. Phys. B 169, 103 (1980): the
  condensate-density relation (the toy's frame).
- M. Creutz, Phys. Rev. D 21, 2308 (1980): SU(2) lattice ensembles
  (the plaquette curve's literature anchor).
```

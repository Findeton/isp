# Paper 22 (v6) - SHARD: The Sign Campaign

Author: Felix Robles Elvira

Subtitle:

```text
Tier 2a: the plan's sharpest kill condition, tested at every scope this
campaign reaches - and passed at all of them.  (i) The one-loop sign
arithmetic (named-import formula, p18e-COMPUTED indices, P19 floor
content x 3 + the P20 doublet): SU(3) b0 = +7 (asymptotically free:
QCD confines), SU(2) b0 = +13/4 (free), U(1) b0 = -41/6-class (< 0:
infrared-free: QED safe) - THE SIGN STRUCTURE OF THE STANDARD MODEL
HOLDS FOR THE RECONSTRUCTED RECORD CONTENT.  (ii) The record-native
flow direction: vectorized SU(2) record ensembles on 4^4 (plaquette
curve matching literature values), gauge-record decimation to 2^4, and
coupling matching: beta_eff = 0.82 from beta = 2.40 - the record RG
moves the nonabelian sector TOWARD STRONG COUPLING (the confining
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

Named imports: the one-loop beta-function formula; the Banks-Casher
relation as the continuum frame.  Record-native: the GW spectra on
sampled ensembles (P14 operator), the decimation rule (P14/P18), the
matching method.  Statistical errors printed in place; fixed seeds.

## 2. What this paper proves and does not prove

Proves/establishes at stated scope: the one-loop sign structure for
the reconstructed content (arithmetic exact given the computed
indices); the strong-coupling-ward flow direction of the decimated
SU(2) record ensemble in the crossover window (with literature-
matching plaquette values as the sanity anchor); the spectral
accumulation and live topological zeros of the record GW operator in
gauge ensembles.

Does not prove: the record beta function at weak coupling/scale (O7
remainder, named); confinement as a theorem (the area-law DYNAMICS);
unquenched effects; anything in 4d beyond the direction receipt.

## 3. The kernel after Paper 22

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

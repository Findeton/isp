# D4 hostile round-2 mathematics / probability / profinite review

**Date:** 2026-07-11  
**Verdict:** **PASS at the repaired claim ceiling**  
**Blocking findings:** none  
**New openings:** none

## Frozen sources reviewed

- `v10/note-d4-no-silent-boundary-sufficiency.md`  
  SHA-256 `fb5d1c2ff71bc58b82a33a3a04140c0016242756ce070d7cfd36d5d4ff4d4c95`
- `v10/relativistic-isp-v10-paper5-restriction-naturality-global-shock.md`  
  SHA-256 `e216c266f9402cce6a48ebd0d35c94dbcfe630fa5a275c9c7f38bb1bec0d5b93`
- `v10/code/d4_boundary_sufficiency_exact.py`  
  SHA-256 `3e6360c71592ca9a46df2914251fdf59976d24440a1f20333cb8754fe117dd4a`
- `v10/reviews/d4-hostile-round1-opening-ledger.md`  
  SHA-256 `f65467b27a86c010e6aae4aa18fb96776fec5fa58c7f378488c7cad13db67612`

The repaired receipt was run twice. Both runs reported **23/23** and had
byte-identical stdout SHA-256
`f370625dc41046242fea6430e4362dddb66fdb54746b43da65d94c484534f2d1`.

## Independent exact reconstruction

I independently rebuilt the labeled posets using ternary choices on unordered
pairs, generated ideals and each cut system, and performed exact rational
elimination without importing the production executable:

```text
cut mode     variables  equations  rank  augmented rank  signed affine dim
all             111       1087      108       108                 3
convex          111       1069      108       108                 3
stem            111        939      103       103                 8
interval        111        985      103       103                 8
```

The equation counts decompose into 24 normalizations, 611 covariance rows,
and respectively 452, 434, 304, and 350 cut rows. Thus the reported
`3/3/8/8` dimensions are independently exact. These are signed affine
dimensions; probability classification still requires positivity.

## All-subset and convex positivity collapse

The all-subset proof remains sound. Equality kills the bottom-only ideal on a
two-chain. In the V-order, the two chain marginals give nonnegative zero sums;
positivity kills their individual terms and transfers the refusal to both
antichain singleton ideals. Every proper ideal then exposes a forbidden
singleton on an inside/outside pair, so its mass is a term in a nonnegative
zero marginal.

During this review I found that an arbitrary comparable inside/outside pair
need not be convex. The production artifacts were repaired before final
adjudication with the required boundary-pair lemma:

- if an incomparable cross-boundary pair exists, it is convex;
- otherwise a saturated chain crosses the ideal boundary at a cover pair,
  which is convex;
- the ideal projects to the forbidden singleton in either case.

The receipt now gates that full step rather than only the small point/chain/V
cells. My independent audit reproduces

```text
convex proper-ideal certificates: 1304 / 1304
cover-chain certificates:          616
antichain certificates:             688
```

The paper proves the infinite cover-or-incomparable lemma, so the finite gate
is a receipt shadow rather than an extrapolation. Positivity therefore
collapses both all-induced and convex probability families to the same
empty/full universal-precursor mixture. The free parameter `p` is not
selected, and the full branch is correctly described as universe-global
incidence rather than a local pair interaction or physical shock.

## Stem and interval counterfamilies

For an ancestor-closed stem `K`, a retained point is minimal in `P|K` exactly
when it was minimal in `P`. Hence

$$
Min(P)\cap K=Min(P|K),
$$

so the deterministic `D=Min(P)` precursor law is stem-natural and is proper
on a nontrivial chain. It fails the top-only chain cut. The independent audit
reproduces all **1,789** registered stem cuts.

For the registered interval category, a union of comparability components is
an ideal. A nontrivial closed interval with comparable endpoints lies within
one component and is connected, so independent Bernoulli selection of whole
components pushes to the same empty/full Bernoulli law on the interval.
Empty, full, and singleton cuts also commute. The independent audit reproduces
all **2,210** interval cuts.

On the convex V-minima cut, the full V has one component and yields perfectly
correlated minima, while the recomputed antichain selects its two components
independently. This is an exact convex failure. The two counterfamilies
therefore genuinely show that stem-only and the explicitly defined
interval-only naturality do not imply the collapse.

Collar-complete and typed-carrier cuts are correctly left unclassified in the
unmarked poset arena.

## Proper-ideal and signed-system audit

The earlier arbitrary-pair `652/652` split has been superseded by the convex
certificate above. Every selected pair now has projected mask `1`, induced
type bottom-chain or antichain, and is explicitly cover-or-incomparable.

The signed system remains dimension three for all/convex. This does not
contradict the one-parameter probability segment: the two additional signed
directions use positive/negative cancellation in V-order zero fibers, which
nonnegativity forbids. The paper keeps this distinction explicit.

## Fixed-law decoder contract and quotient counts

The repaired predictive proposition fixes the supplied law `L`, retained
structure `S`, visible precursor alphabet, and decoder

$$
F_L(S,m(c))=q_c.
$$

Within fixed `L,S`, equality of `q` is exactly the coarsest deterministic
predictive partition. The vector is called a canonical representative, not a
unique physical carrier or bit-minimal encoding. This fully resolves the
round-1 minimality ambiguity.

The independent rebuild reproduces every count:

```text
fixed b=1, labeled cover:       564 classes / max 42
fixed b=2, labeled cover:       601 classes / max 45
fixed b=1, canonical quotient:  144 classes / max 30
fixed b=2, canonical quotient:  168 classes / max 36
pooled labeled diagnostic:      756 classes / max 66
pooled canonical diagnostic:    199 classes / max 42
```

The quotient jointly relabels the retained order and every visible precursor
mask, so `199/42` is an actual unmarked predictive-orbit count. The text uses
only fixed-law, fixed-structure classes for minimality and labels pooled
counts as law-dependence diagnostics. The fixed-cut `1/2` versus `9/14`
witness is also exact.

The fixed-law canonical `144/30` and `168/36` values are printed rather than
asserted by a dedicated check condition, but the independent reconstruction
confirms them. This is not a claim blocker.

## Explicit chain lower bound and operational premise

The receipt constructs the chain ideals as the prefix masks

$$
0,1,3,\ldots,2^n-1.
$$

Exactly one omits the retained minimum and `n` include it, so
`q_n=n/(n+1)`. The 64 exact targets are distinct, require at least six binary
bits, and nine targets exceed a three-bit alphabet.

The theorem now states the necessary side-information contract: the decoder
knows the fixed law and retained one-point state, but it receives no depth,
global clock, or other full context except through one deterministic
pre-sampling token. It also names the uniform finite alphabet, one-token, and
zero-error assumptions. Under these premises the lower bound is exact. The
text correctly refuses to derive uniform token capacity merely from finite
evidence per record.

## Loophole controls

The four models change explicit premises rather than pretending to violate
the theorem:

- a binary stochastic token moves `q_n` into a context-dependent mixing law;
- six distributed bits encode depths 1--64, while unbounded depth requires a
  growing record collection;
- an integer-valued mark is finite at each depth but lacks a uniform alphabet;
- a tail bin predicting inclusion has total-variation error at most one
  percent from depth 99 onward.

Each is mathematically valid and each is correctly described as an escape
from the fixed deterministic exact-token theorem, not as a derived local
compositional encoder.

## Finite versus analytic profinite claim

The executable now labels its factorial calculation a finite shadow. It
checks divisibility through `8!`, the exact identity

$$
1-\frac{j!}{j!+1}=\frac1{j!+1},
$$

strict error decrease, and terminal error `1/40321`. It explicitly assigns
the universal conclusion to the analytic proof.

That proof is correct. For every fixed modulus `m`, `j!` is eventually zero
modulo `m`, so `j! -> 0` in the standard profinite integers. But
`j!/(j!+1) -> 1`, whereas the depth-zero readout is zero. A continuous real
extension is impossible. The claim is correctly restricted to the standard
profinite-integer topology and continuous real readouts; it is not promoted
to every Stone space, the v9 stem spectrum, measurable decoders, or other
compactifications.

## Final adjudication

**PASS.** The exact supported ceiling is:

```text
all-subset or convex unmarked autonomy -> empty/full universal precursor;
stem-only and registered interval-only autonomy -> nontrivial families;
supplied non-natural law -> law-relative predictive target, not a carrier;
fixed deterministic no-depth token -> unbounded exact chain states;
standard profinite integers -> no continuous real chain readout.
```

No local marked interacting click law, physical boundary carrier, cone,
dimension, continuum, quantum, or absolute-scale result is selected by D4.

# D3 hostile round-2 mathematics / measure / profinite review

**Date:** 2026-07-11  
**Verdict:** **PASS at the repaired claim ceiling**  
**Blocking findings:** none  
**New openings:** none

## Frozen sources reviewed

- `v10/note-d3-profinite-variable-history-extension.md`  
  SHA-256 `a080b9020c3f683e847aa225cdbc9bd0402155843c98a45c0d9b21b03fee7a6a`
- `v10/relativistic-isp-v10-paper4-profinite-growth-preserves-past-not-law.md`  
  SHA-256 `72147070ee3423d940b24a433704cd2dbe6459910a1a6c491d889fe14a07b858`
- `v10/code/d3_profinite_extension_exact.py`  
  SHA-256 `bdc93a27f66ba67d9100d6e76bfa0c5e4b776152373b32c08e97c2046e7b3f64`
- `v10/reviews/d3-hostile-round1-opening-ledger.md`  
  SHA-256 `51e1b16f225215fb3e5ac77558e11dd8666cf577c10c1c98efc03cc9cafd9019`
- imported certificate theorem: `v9/relativistic-isp-v9-paper7-stem-spectrum.md`  
  SHA-256 `0499066ba53d5b1001211d0d81d0d615e8ee1f6d3717022f871011f5acc427dd`

The repaired executable was run twice with byte-identical stdout. Each run
reported **27/27**, canonical payload
`0f2f0ed7157811ec94bfa218b0487c39b3b58422afca1853f79050abb66538ec`,
and complete-stdout SHA-256
`1eb106b568d4800955b8c23d349c66db79c1462b1e1c65d5b60e05aa9718ea21`.

## Independent reconstruction

I rebuilt the finite orders, ideals, extensions, component statistic,
rational kernels, induced restrictions, and finite orbit quotient from
scratch without importing the production executable. The reconstruction
returned

```text
natural-order levels: 1, 1, 2, 7, 40, 357
incidence restriction cases: 6064
kernel-restriction squares: 712 total = 356 per law
restriction failures: b=1 -> 212; b=2 -> 296
controlled-zero covariance cases: 8824
chain witness: (1/3,2/3) pushed; (1/2,1/2) recomputed
three-antichain finite orbit: 1/8 versus 1/10
```

The large census numbers also have independent counting checks. Because each
parent/ideal pair gives one unique next-level naturally labeled order,

$$
\sum_{n=1}^4 2^n|\Omega_{n+1}|
=2(2)+4(7)+8(40)+16(357)=6064,
$$

and the one-law relabeling audit has

$$
\sum_{n=1}^4 n!|\Omega_{n+1}|
=1!(2)+2!(7)+3!(40)+4!(357)=8824.
$$

Excluding the full retained ideal leaves

$$
\sum_{n=1}^4(|\Omega_{n+1}|-|\Omega_n|)=356
$$

restriction squares per law, hence the reported 712 across two laws.

## Round-1 opening audit

### 1. Restriction naturality is now separated correctly

The deterministic incidence identity

$$
C[D]|_{K\cup\{e\}}=(C|_K)[D\cap K]
$$

is valid for every old subset `K`, not only stems. Intersecting a down-set
with `K` is a down-set of the induced order, and both sides retain exactly the
same old-old and old-new pairs. The 6,064-case receipt is a genuine exhaustive
finite audit of this identity.

The stochastic kernels do **not** inherit autonomous restriction naturality.
The chain-to-one-point calculation is exact, and the independent enumeration
reproduced all 212/296 failures. Paper 4 now promotes this counterexample
instead of hiding it and claims only end-deletion prefix consistency. This
fully closes the principal round-1 mathematical blocker.

### 2. Child-driven recovery is no longer circular

The recovery pass traverses actual positive-mass children, deletes the newest
event to recover the parent, reads the new event's ancestry to recover its
precursor, checks unique fibers, and only then compares the cylinder ratio to
the closed-form kernel. For the two positive laws every finite child is on
support, so all audited ratios are defined. Paper 4 separately and correctly
states that zero-mass histories require a chosen conditional version.

### 3. Eligibility and weighting are genuinely separated

The two positive laws have the same support and establish weighting
nonselection. The controlled-zero law sets every `beta>0` precursor to zero;
the empty precursor always has positive weight, so normalization cannot fail.
Its recursive measure is end-deletion consistent. Since `beta` and down-set
membership are invariant under parent isomorphism, the law is one-step
isomorphism-covariant; the strengthened receipt checks all 8,824 mapped
precursor cases. Thus zero bridge mass versus positive bridge mass is a valid
**prefix-level eligibility** nonselection witness.

The note and paper do not promote this control to subsystem naturality,
emergent locality, or a physical law. That refusal is necessary: the law is a
global-prefix control and its support differs from the positive laws.

### 4. The construction-order quotient is now an actual pushforward

At each audited finite level, canonical isomorphism classes partition the
naturally labeled state set, and summing complete fibers therefore preserves
normalization. The independent rebuild found unequal raw masses inside the
one-edge three-event orbit: `1/8,1/8,1/6` for `b=1` and
`1/10,1/10,1/6` for `b=2`. It also independently recovered the antichain
orbit masses `1/8` and `1/10`.

This repairs the former placeholder arithmetic. Crucially, Paper 4 now calls
the result only a **finite canonical pushforward**. It explicitly refuses an
infinite unlabeled-prefix inverse system because an unlabeled causet has no
canonical newest element to delete, and it does not infer covtree consistency.

### 5. The stem certificate is scoped correctly

The chain-plus-isolate has both exact-rank-two stem types. Adding successive
universal tops cannot create a new rank-two stem: any down-set containing a
new top must contain its entire earlier past, already larger than rank two.
The executable checks this continuation through nine events. The infinite
certificate step is not inferred from that cutoff; it is explicitly imported
from v9 Paper 7, whose Theorem 6 gives the finite-certificate/universal-top
construction and the covtree-spectrum inverse-limit identification.

## Measure and profinite verification

The labeled prefix tower has finite discrete levels and surjective
end-deletion maps. Its inverse limit is a closed subspace of a countable
product of finite discrete compact spaces, hence compact and metrizable.
Exactly compatible finite distributions therefore define a unique Borel
probability on that inverse limit, and every Borel probability there is
Radon. Conditional child probabilities are recovered by cylinder ratios only
on positive parent cylinders, exactly as Paper 4 states.

The paper also keeps the second tower distinct. Covtree level records a set
of exact-rank stem types of a completed history, not one committed finite
prefix. A covtree walk may define a stem-observable/spectrum measure, but a
unique completed-history law does not follow across rogue fibers, and a SHARD
next-record dynamics still requires a history lift plus a marked click
filtration. No labeled-prefix kernel is silently identified with a covtree
transition.

The mark-space qualification is also correct: real or rational marks do not
automatically leave finite quotient levels, so no marked profinite completion
is claimed without finite observable partitions or an explicit compact
topology.

## Counterexample search at the repaired ceiling

I specifically tried the failure modes that invalidated round 1:

1. arbitrary induced subsets rather than only end-deletion prefixes;
2. ancestor-closed subsystem kernels rather than deterministic incidence;
3. recovery from children rather than from a forward-loop key;
4. positive-support weighting versus controlled-zero eligibility;
5. unequal scheduler-path weights within one canonical orbit;
6. fixed-level orbit pushforward versus a nonexistent unlabeled deletion
   tower;
7. a finite stem witness versus an infinite certificate theorem;
8. zero-cylinder ambiguity in the measure-to-kernel converse.

No new contradiction or overclaim survived. In particular, the repaired
paper does **not** claim autonomous restriction projectivity, a covtree lift
for the witness kernels, a local marked interaction law, diamond probability
gluing, metric locality, cone rounding, dimension recovery, or absolute
scale.

## Final adjudication

**PASS.** The exact supported result is:

```text
immutable-past common-future extension is coherent;
multiple end-deletion-consistent global-prefix laws survive;
finite canonical pushforward does not remove their nonselection;
unmarked autonomous restriction naturality fails;
no local marked interacting click law is selected.
```

That is the ceiling actually proved, and the revised note, Paper 4, and
receipt remain below it.

# D3 hostile review, round 2: independent rebuild and reproducibility

**Referee:** independent hostile rebuild

**Date:** 2026-07-11

**Verdict:** **PASS — no remaining independent-rebuild blocker**

The round-1 defects were real, and all four have been repaired. The production
receipt now tests actual transition fibers instead of a cardinality tautology,
recovers kernels from actual child states instead of a saved generation table,
forms genuine canonical unlabeled pushforwards instead of adding invented
fractions, and separates weight nonselection from eligibility nonselection by
adding a covariant controlled-zero law.

An independent Ruby reconstruction, importing no production code, reproduces
all theorem-critical finite counts and probabilities. The revised paper also
makes the load-bearing scope distinction correctly: deterministic incidence
commutes with old-subset restriction, while the two positive probability
kernels fail even ancestor-closed autonomous-subsystem restriction. What is
proved is end-deletion prefix projectivity, not record-restriction locality.
No claim in the revised paper crosses that boundary.

## 1. Frozen round-2 snapshot

```text
a080b9020c3f683e847aa225cdbc9bd0402155843c98a45c0d9b21b03fee7a6a  v10/note-d3-profinite-variable-history-extension.md
bdc93a27f66ba67d9100d6e76bfa0c5e4b776152373b32c08e97c2046e7b3f64  v10/code/d3_profinite_extension_exact.py
72147070ee3423d940b24a433704cd2dbe6459910a1a6c491d889fe14a07b858  v10/relativistic-isp-v10-paper4-profinite-growth-preserves-past-not-law.md
```

Production command:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 v10/code/d3_profinite_extension_exact.py
```

Two executions exited zero and produced byte-identical stdout:

```text
1eb106b568d4800955b8c23d349c66db79c1462b1e1c65d5b60e05aa9718ea21
```

The executable reports **27/27 checks passed**, `CONSISTENT-FAMILY`, and
canonical payload digest:

```text
0f2f0ed7157811ec94bfa218b0487c39b3b58422afca1853f79050abb66538ec
```

As noted in round 1, that internal digest covers only the registered level
counts and bridge-probability pair. The external stdout hash above is the
complete-output reproducibility receipt.

The separate self-containment audit also passes 4/4: all v10 investigation
executables are under `v10/code`, no duplicate source exists elsewhere, every
investigation executable imports only the Python standard library, and no
`.pyc` artifact exists under `v10`.

## 2. Independent reconstruction

I extended the round-1 Ruby implementation rather than calling or translating
the production Python at runtime. The resulting scratch implementation has
SHA-256:

```text
bcbd9f136bf07aaae585d5fcfaa7447b3a85ca04cc9bd4cb2c87029f8cf0d950
```

In addition to the original direct order census, down-set growth, deletion,
bridge, rational-measure, child-recovery, covariance, orbit, and stem checks,
the independent rebuild now implements:

1. arbitrary old-subset restriction of deterministic extension incidence;
2. ancestor-closed restriction pushforward of both positive kernels;
3. the controlled-zero no-bridge kernel and its cylinders and covariance;
4. canonical finite orbit pushforwards for both positive laws; and
5. the universal-top stem certificate through nine events.

Independent output:

```text
COUNTS growth=[1, 1, 2, 7, 40, 357] direct=[1, 1, 2, 7, 40, 357]
EXTEND deletion=true immutable=true direct_parents=true
EXTEND unique child-fiber multiplicity=1 at every level
BRIDGE disconnected=203 exists=true reduction=true
MEASURE normalized=true independent_recovery=true cylinders=true
MEASURE same positive support=true unequal measures=true
ANTICHAIN bridge=1/2,5/7 pair=1/8,1/7
COVARIANCE cases=17648 pass=true
RESTRICTION incidence_cases=6064 pass=true
RESTRICTION probability_failures={(1,1)=>212,(1,2)=>296} squares=712
ZERO bridge_mass=0 normalized=true cylinders=true covariance=true cases=8824
ORBIT normalized=true antichain=1/8,1/10 raw_variation=true
STEMS chain-plus-isolate rank-2 types=2
CERTIFICATE universal_top_to_n9=true
```

These are exact integer or rational computations. No float comparison occurs
in a theorem gate.

The printed survival value was separately recomputed with Ruby `BigDecimal`
at 180 digits:

```text
0.332871083698079553288846906431315521612479521569212491793331386750747085412844311612617072700547851966542125284028850074459582182953107851329719203520345948484474039181655026864485
```

Its first 125 significant digits agree with the production `Decimal` print.

## 3. Round-1 repair audit

### A6: actual transition fibers — repaired

The old `len(range(n+1))` check is gone. Production now constructs every
actual child, verifies that deletion recovers a legal parent, reconstructs its
precursor from the child's relations into the new event, and proves that
every child has one `(parent, precursor)` fiber. The independent rebuild finds
maximum fiber multiplicity one at every transition through the cutoff.

State size remains level-typed. This matters because an empty relation can
denote the empty history, a point, or an antichain depending on `n`; neither
implementation treats the bare relation as a cross-level state identifier.

### B3: child-driven recovery — repaired

Production no longer validates a generation table against itself. It walks
the actual positive-mass children at level `n+1`, end-deletes each child,
recovers the precursor from `(old,n)` relations, groups child masses by the
recovered parent, and freshly evaluates the closed-form kernel. Both exact
ratios and all cylinder sums pass independently.

### C2: real quotient pushforward — repaired

The arbitrary `1/4+3/4` illustration is gone. Every finite naturally labeled
state is mapped to a canonical unlabeled order code, and complete fiber masses
are summed. The orbit distributions normalize at every audited level. At
least one orbit contains unequal raw natural-label masses, showing that the
code does not silently assume equal presentation weights.

The two physical finite pushforwards remain inequivalent. For the
three-antichain orbit they give exactly

$$
\frac18\quad\text{and}\quad\frac1{10}.
$$

The paper correctly limits this to finite unmarked quotient nonselection. It
does not claim a canonical deletion map or an infinite projective measure on
unlabeled prefixes.

### Weight versus eligibility — repaired

The original two positive kernels have common support and therefore prove
only weight nonselection. The revised receipt says exactly that. It separately
constructs a controlled-zero law that assigns zero to every bridge precursor
and uniform positive weight to the remaining down-sets.

This third law is normalized because the empty precursor always remains,
obeys exact end-deletion cylinder consistency, and is isomorphism-covariant in
8,824 independent mapped-precursor cases. On the three-antichain its bridge
mass is zero rather than `1/2`. Eligibility nonselection is therefore proved
under the stated weak prefix gates. The paper explicitly refuses to promote
this global control to a local or restriction-natural physical law.

## 4. The restriction/projectivity fault line

This was the most important new hostile opening.

For every old subset `K`, deterministic incidence satisfies

$$
C[D]|_{K\cup\{e\}}=(C|_K)[D\cap K].
$$

Both implementations verify all 6,064 audited squares. This is a purely
structural statement about restricting an already chosen extension.

The probability law is different. For the chain `0<1`, retaining the
ancestor-closed subset `{0}` pushes the uniform full-parent kernel to

$$
(P(\varnothing),P(\{0\}))=(1/3,2/3),
$$

whereas recomputing the same rule on the retained point gives `(1/2,1/2)`.
The independent exhaustive counts reproduce 212 failures for `(1,1)` and 296
for `(1,2)` among 712 tested law/square combinations.

This does not damage Theorem 3.1. The histories and measures are projective
under the chosen temporal bonding map, deletion of the newest labeled event.
It does defeat any claim that the unmarked retained subsystem is sufficient
to run the same law autonomously. The paper now promotes the failure rather
than hiding it and identifies boundary/environment marks as one possible
repair target. That is the correct scientific conclusion.

## 5. Profinite and covtree scope

The revised paper keeps the two inverse systems separate:

- the labeled-prefix tower uses construction-level end-deletion;
- the stem-spectrum/covtree tower uses refinement of exact-rank stem theory.

The chain-plus-isolate causet has two nonisomorphic exact-rank-two stems, so a
single covtree node can encode a set of types rather than one two-event
prefix. Repeated universal-top extension creates no new rank-two stem once
the certificate already has three events; the finite check through nine
events reproduces. The paper does not infer the general infinite
covtree/spectrum theorem from this finite run. It explicitly imports the
all-rank certificate theorem from v9 Paper 7.

The measure claims are also correctly bounded. A covtree walk supplies a
measure on the stem-observable spectrum. Because the history-to-spectrum map
has rogue fibers, that does not select a unique completed-history lift or a
physical next-record filtration. Profinite topology supplies compactness and
consistency conditions, not transition weights.

## 6. Claim audit

I found no overclaim that reverses the executable evidence.

- “Bridge shadow” is defined only as a new common future whose precursor
  meets several comparability components. It is not called old-old
  comparability, signaling, metric adjacency, or a sealed interaction.
- The witness kernels are disclosed as whole-prefix/global controls and are
  not offered as local SHARD physics.
- End-deletion prefix consistency is not confused with arbitrary record
  restriction.
- Finite unlabeled pushforward is not confused with infinite unlabeled
  descent.
- The controlled-zero witness proves eligibility nonselection only in the
  weak global-prefix class.
- The v7 survival law is held fixed while extension placement changes; it is
  not claimed to determine which records participate.
- No cone-roundness, dimension, metric, diamond-gluing, or interacting click
  law is claimed from the unmarked causal-order shadow.

There is one editorial duplication in Section 4 — “whole finite history and
therefore makes an intentionally strong” appears twice — but it changes no
mathematical statement and is not a review blocker.

## 7. Final determination

The following statement survives independent reconstruction:

$$
\boxed{
\text{A new maximal record may preserve all old relations while recording a
common future of previously disconnected old components.}
}
$$

The following nonselection result also survives:

$$
\boxed{
\text{past immutability + local relabeling covariance + end-deletion
consistency do not select bridge eligibility or weight.}
}
$$

The revised artifact does **not** claim that this supplies a local marked
interaction law. On the contrary, its exact restriction failure isolates why
the final law remains open. All round-1 independent-rebuild openings are
closed, the new restriction opening was executed and correctly promoted, and
the production receipt is deterministic and independently reproducible.

**Round-2 independent-rebuild verdict: PASS.**

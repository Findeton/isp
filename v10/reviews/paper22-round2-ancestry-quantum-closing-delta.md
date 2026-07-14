# Paper 22 round 2 — ancestry/quantum closing delta

**Frozen target:** commit `8e820cc2464eeefeabafe49ed64246e98d51ce4a`.

**Comparison base:** Paper 22 at `a34b36e` and
`paper22-round1-ancestry-quantum-hostile-review.md`.

**Exact verdict:** **SCIENTIFIC DELTA CLEAN; ONE BIBLIOGRAPHIC REPAIR STILL
REQUIRED — 0 BLOCKER / 0 MAJOR / 1 MINOR / 0 NIT.**

The four D34e theorems, their carrier-class quantifiers and both refusal rows
survive unchanged.  The Branch-F selector is now named by its actual own-ring
ordinal; the conclusion no longer asserts a smallest carrier; and the new
record-DAG checks close the three coordinated corruptions opened by the
boundary review without promoting the validator into a theorem about all
generatively legal histories.

One source-level defect prevents an unconditional terminal verdict: two of the
newly expanded literature entries contain objectively incorrect metadata.
The citations are used only as background, so no mathematical or physical
claim is damaged.  After the two exact substitutions in section 7 below, this
stream recommends terminal acceptance without another executable run.

## 1. Independent reproduction

The frozen candidate artifacts hash as:

```text
paper  1718dce460c5d1711fa3b02fe8424c9a5b4819abb8b9facd0d64abbff14b92ee
note   af3c9b6fdf7590c6a28db93f0e473691b30c00ae921440156a7e48e8cb19a98c
code   1dd1a69be94a0fb614f909745e7db772ac5e5f134b97cbdcdf10c45a08f606c5
stdout 158c491d7376b165556364fee2f0266447e7f5becfdbda5a8f4ae600114e9fb7
```

I reran the executable under fresh hash salt `740471`.  It exited zero with
`13/13`, reproduced internal digest

```text
9f9cea1886db0c889677fdb735b8cb9fc76ae4d2ba18b501242f58331795e017
```

and produced stdout byte-identical to the committed candidate output.  The
central ledger is:

```text
reachable levels                 1,6,40,304,2576
reachable states                 2927
registered strong classes        111,111,111
B3 row updates                   35898
disjoint swaps                   120276
full regional compositions      159734
malformed messages              9/9 rejected
ancestry interlopers             16/16
radius lower bounds              1/24,1/1024,1/64000,1/5308416
finite unmarked classes          4,10
quantum                          REFUSAL
```

The manuscript's provenance statements are exact: terminal D34e note/reviews
are available at `d10ca52`, the second repaired D34e executable/output at
`6e6676b`, and this commit is explicitly a paper-level candidate pending the
closing deltas.

## 2. Branch-F immutable-event selection — clean

The prior source terminology is repaired correctly.  D34b event identifiers
have the form

```text
actor#r(own initiated ring count).
```

The executable sets

```text
pre_stop_ordinal = idle_branch["actors"][D]["ring"]
selected_id = f"{D}#r{pre_stop_ordinal}".
```

This is D's own-ring ordinal, not its position among all events touching D's
wire.  The abstract, theorem proof, executable label and ledger now say
“own-ring ordinal.”  The paired idle and interaction histories have the same
structural D role and the same selected identifier; only the immutable event
kind differs.

The paper also replaces “already sealed event” by “persistent immutable
event.”  That is the right ontology for this chosen D34b exemplar, which has
no dynamic sealing.

The future predicate continues to name one common event:

> A's future ancestry contains the inward chain and the exact pre-stop D event
> at the selected own-ring ordinal, with kind idle.

Later idles, interactions, births or unrelated events can move D's tip but
cannot change that persistent record.  All 16 registered interloper checks
still observe idle-branch true and interaction-branch false.

## 3. All-finite-radius quantifier and probability — clean

For every finite `r`, D is placed at distance `r+1` from A and is given leaf E.
The differing D event lies outside the complete radius-`r` carrier.  The paired
past masses are positive and the complete `C_r` values are equal.

There are `r+3` active component actors.  Every one of the `r+1` prescribed
inward interactions has a degree-two initiator, so each embedded step has
conditional mass

```text
1/(r+3) * 1/(4*2) = 1/[8(r+3)]
```

and the consecutive subcylinder has exact mass

```text
p_r = [1/(8(r+3))]^(r+1) > 0.
```

The manuscript correctly uses `p_r` as a lower bound on the idle-branch event,
not its total probability.  The interaction branch remains exactly zero by
immutable kind.  The `Delta=1` numbers remain optional Erlang-completion
subcylinder lower bounds.

The quantifier is not widened.  The theorem excludes every member of the
declared family of complete fixed actor-radius carriers
`{C_r:r finite}`.  It does not exclude:

- adaptive non-radius frontiers;
- all bounded carriers;
- all local encodings;
- a different physical realization of the C/L quotient; or
- carriers for a different history law.

The paper's `NO EXACT REALIZATION` row therefore remains exact at its declared
carrier-class scope.

## 4. Component ceiling — clean

The B4 theorem is still one-sided.  Birth attaches inside the parent's
component, interaction follows an existing edge and idle touches one actor.
No chosen-law row joins disconnected components.  Independent Poisson sources
therefore factor across components at continuous construction time and
component-local stops.

The complete component retains the actor rows, adjacency, persistent events,
predecessors and wire tips needed to generate Branch F.  It is an all-future
sufficient growing ceiling.  The paper says explicitly that B4 necessity and
the minimal adaptive full-ancestry frontier remain open.  It never invokes the
stronger `WHOLE-COMPONENT ONLY` outcome.

The repaired conclusion is now faithful:

```text
prediction can live on a sufficient query-relative causal boundary ...
```

It does not claim that the constructed B3 or B4 is the smallest physical
carrier.

## 5. New validator delta — closes the registered opening, changes no theorem

The validator now checks the specific integrity predicates requested by the
round-1 boundary review:

- canonical event ID ownership and initiator ordinals;
- internally owned predecessors must be visible;
- same-initiator predecessors must have earlier ordinals;
- the visible predecessor graph must be acyclic;
- ring, birth and wire counters agree with visible owned history;
- carrier parity agrees with visible interactions;
- actor degree agrees with owned ports; and
- every event touching an owned wire lies in the stored tip's visible ancestry.

The three coordinated new corruptions are independently present and rejected:

```text
internally owned opaque predecessor  rejected
self predecessor cycle               rejected
stale visible wire tip               rejected
```

Together with the six earlier interface attacks, the battery is exactly
`9/9`.  Genuine regional projections still compose to the direct union in
`159734/159734` ordered checks.  The new validation therefore strengthens the
evidence for typed composition and closes the specific paper-level opening.

It does **not** change the theorem's mathematical source.  The arbitrary-region
identity is still typed set union on genuine messages generated by
`region_message` from a legal D34b configuration.  The validator is not a
complete decision procedure for generative reachability or exact predecessor
semantics.  As a beyond-battery scope attack, I inserted a visible predecessor
from an untouched wire into an otherwise consistent two-idle component
message; `validate_message` accepted it:

```text
spurious_untouched_wire_predecessor_accepted True
```

That input satisfies the particular ownership, visibility, acyclicity,
counter and tip predicates while not being generated by `d34b_step`.  This is
not a finding against the paper: the repaired prose lists the exact integrity
checks and does not claim complete D34b-history recognition, authentication or
reachability.  It is a scope guard for later narration.  The executable's
validator hardening is defense in depth, not a new law theorem and not a wider
B4 necessity claim.

## 6. Quantum, profinite and geometry refusals — clean

### 6.1 Quantum

E12 verifies the accepted finite D34c output hash

```text
9ce73a693b41f765eff163749ef769ca0cb4ce856ead66d690a63a20331a731a
```

and then checks that the timed controlled D34b-D34c process and licensed
instrument-indexed kernels are absent.  It assigns no `d_carrier`, `d_op` or
`chi_cut`.  Paper 22 accurately reports the finite D34c artifact as a separate
dependency and the intrinsic timed quantum boundary as `REFUSAL/UNDEFINED`.

No classical B3/B4 carrier is called a quantum carrier.  No quantum Markov
condition is inferred from classical strong Markovity.  The Pollock citation
is explicitly background for the operational, intervention-indexed criterion,
not a proof that the missing SHARD controlled process exists.

### 6.2 Profinite

The only proved bridge remains the finite labeled-truncation/mark-forgetting
diagram

```text
(u_3 o r_(4->3))_* mu_4 = (u_3)_* mu_3.
```

The paper refuses a canonical unmarked restriction, completed marked-history
pushforward, adapted v9 stem-spectrum posterior and predictive screening
factorization.  It does not use the finite diagram to select the growth law or
boundary.

### 6.3 Geometry and law selection

D34b remains an explicitly chosen passive exemplar.  Paper 22 derives the
boundary generator conditional on that law; it does not derive the interactive
law from records, seals, diamonds, covariance or Barandes ISP.

The geometry paragraph is also negative and prospective.  It claims no
Lorentz light cone, round cone, 3+1 dimension, proper-time conversion,
gravitational scale `G` or universe click law.  Any later law must establish
its own predictive carrier before the v9 cone/scale/dimension diagnostics are
rerun.

## 7. MINOR finding

### m1 — two repaired literature entries contain wrong metadata

The new inline citations are now placed at honest claim sites, and their
conceptual scope is correct.  However, two bibliography entries do not match
the primary publication records.

Paper 22 gives Shalizi and Crutchfield DOI

```text
10.1023/A:1010148903217
```

The correct DOI is

```text
10.1023/A:1010388907793.
```

Paper 22 gives Geiger and Temmel as

```text
Journal of Applied Probability 51A, 368–388 (2014).
```

The DOI printed on the same line resolves to

```text
Journal of Applied Probability 51(4), 1114–1132 (2014),
DOI 10.1239/jap/1421763331.
```

Pollock et al., *Physical Review Letters* 120, 040405 (2018), DOI
`10.1103/PhysRevLett.120.040405`, is correct.

This is one bibliographic minor, not a theorem or provenance failure.  None of
the exact SHARD results relies on those papers; they are explicitly labeled
background.

**Required repair:** replace the Shalizi DOI and the Geiger volume/page range
with the two exact strings above.  No code, output, theorem, note or outcome
table needs to change.

## 8. Final disposition

| Audit target | Disposition |
|---|---|
| Fresh receipt and hashes | `13/13`, byte-identical, exact |
| Registered validator battery | `9/9` rejected |
| Branch-F selector | own-ring ordinal, correctly repaired |
| Branch-F all-`r` no-go | exact in declared complete-radius family |
| Component B4 | sufficient growing ceiling; necessity open |
| Universal/bounded carrier no-go | not claimed |
| D34c quantum lift | not smuggled; intrinsic branch refused |
| v9 profinite posterior bridge | not smuggled; refused beyond finite diagram |
| Geometry, dimension, proper time, `G` | not claimed |
| Validator effect | hardening only; no theorem widening |
| Literature claim width | correct |
| Literature metadata | **m1 repair required** |

**Closing count:** **0B / 0M / 1m / 0n.**

**Terminal recommendation:** apply the two bibliography substitutions and
accept Paper 22 as terminal at the declared D34e synthesis width.  Because the
repair changes no executable input, mathematical statement or physical claim,
this ancestry/quantum stream does not require a further calculation round; a
textual hash/diff check is sufficient.

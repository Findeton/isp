# D35 round 3 — probability/covariance final review

**Frozen target:** commit
`8a9bb98da2a37d61f5887fa69d397792ed0f4807`.

**Reviewed artifacts:** `d35c_local_specification_exact.py`, its committed
receipt, D35 section 17, and the inherited D35b completion theorem.

**Lane:** exact probability, seed/event alpha covariance, full projectivity,
completed-history extension, root causal ordinal versus metric time, source
seal identity and hidden label dependence.

**Verdict:** **MAJOR REPAIR — ORDINARY COMPLETE RENAMINGS AND BOTH 16/408
BATTERIES PASS, BUT THE FRESH EVENT/NEWBORN ALLOCATOR STILL DEPENDS ON RAW
NOMINAL STRINGS AND BREAKS UNDER VALID ALPHA RENAMINGS.**

**Count:** **0 blockers / 1 major / 0 minors / 0 nits.**

D35c repairs the exact event key diagnosed in round 2: for every noncolliding
complete renaming I tested, the structural seed identifier forgets all raw
seed names, including the new D-source seal, and both Q cells reproduce the
same complete quotient law.  Original and renamed full projectivity also pass
independent reconstruction.

However, canonicalizing the *reported key* is not enough.  Generated event and
newborn storage identities are still fixed raw strings such as
`EROOT-CAP-0::T1:r` and `NROOT-CAP-0::T0:r`.  A seed-event or actor-display
alpha-renaming may use one of those currently unused strings.  The renamed
first law can remain identical, yet a later call fails because the allocator
mistakes the nominal collision for a physical duplicate.  Thus the transition
kernel itself does not descend to the claimed complete alpha quotient.

## 1. Reproduction and exact identity

I reran D35c under fresh independent hash seeds `141421356` and `173205080`.
Both executions exited zero and were byte-identical to each other and to the
committed receipt.

The frozen identities reproduce as:

```text
source
50f1e710cc04de3576b24bd5e7414764f1dea1ebb86f0b0b5747d2b18109c765

stdout
d8f0ef0c4320ff58badcff6ce6916fe7a3f4adb94b58de8afd95c4aa09bb6f42

internal science
da82ce3ca611fd2e51f0d0e4fd3a36ec74edb895c279e9f6bcd48ac8ceb5aebf

D35 note at the frozen target
f9ea32b0a303fb3e2af3e8dbb480c747c5afc4e1b333e8fe477abc21d6052ac0
```

The executable again prints `PASS 16/16` and the scoped candidate noun
`TIMELESS ROOTED NESTED-CALL FAMILY / EXECUTABLE`.

Both relevant hygiene ranges are clean:

```text
git diff --check 592e102..8a9bb98
git diff --check de51b4e..8a9bb98
```

## 2. Independent normalization and cylinder reconstruction — pass

I independently enumerated the primitive D35c kernel rather than calling its
printed summary gate.  For each Q cell I accumulated the second-call law by
the complete first `physical_key`, compared every retained raw event and
payload, and checked the root wire directly.

The unrenamed result for each of Q1 and Q2 is:

```text
complete first histories                         16
complete physical atoms                          16
first-law total mass                              1
second-call refinements                         408
full first-cylinder marginal mismatches           0
old raw-event equality checks                 3,588
old raw-event mismatches                           0
old provenance/payload mismatches                  0
old A2 below new A2 checks                       408
root-wire failures                                 0
first-call stopping checks                        16
```

For every first history, the only transaction event touching the root actor
is the returned A2 event.  All open calls and mailboxes are closed at A2.  The
probability law remains the product of finite actor-local menus, each summing
exactly to one; D35c's prevalidation and capability ownership reject malformed
operations without renormalizing the valid menu.

The exact root-kind laws remain:

```text
Q1: birth 1/4, fork 1/8, idle 3/8, visit 1/4
Q2: birth 1/5, fork 1/10, idle 2/5, visit 3/10.
```

## 3. Safe complete alpha renamings — pass

I applied three independent complete seed-event bijections and three actor
display-name bijections to each Q cell.  These included:

- fresh short names;
- unrelated long descriptive names; and
- a permutation reusing the old six seed strings, including swapping the raw
  name `D-source-seal` with another seed event.

Each transformation transported all six event dictionary keys, event `name`
fields, predecessor references, collector tips, actor-owned tips, source-event
reference and payload entry.  Every one of the six Q/mapping cases reproduced:

```text
first atoms                  16
first total                   1
second refinements          408
persistence checks          408
full marginal equality      yes
quotient equality           yes
```

This verifies the new recursive `seed_event_id` for ordinary presentations.
It uses kind, actor structural addresses, physical flags and recursively
canonical predecessor structure; it does not use the raw seed dictionary key.
The D-source seal is consequently not a hidden raw label in `physical_key`.
Its bounded bit remains a physical mark, as it should, while its event name is
gauge.

## 4. Completion and causal ordinal — pass on the registered presentation

D35c preserves D35b's completion assumptions for the registered and safe
renamed presentations:

1. every finite rooted state has a finite normalized next-call kernel;
2. every valid call terminates by strict descent on the finite ownership tree;
3. reachable finite states form a countable discrete state space; and
4. persistent union gives a locally finite event DAG.

Ionescu--Tulcea therefore continues to provide a completed classical history
measure for those presentations.  The source seal adds one finite immutable
seed event and one bounded payload field; it does not affect countability,
normalization or local finiteness.

The call integer is now owned by the root actor.  At the first completed A
successor it equals one, at the second it equals two, and the eight-call replay
ends at eight under every serializer.  It is reserved when A opens the next
call and, on the valid always-terminating grammar, equals the ordinal of A's
successive records.  It carries no duration, rate, simultaneity relation,
metric scale or proper-time magnitude.  The model still has a distinguished
root and laminar causal barriers; section 17 states that supplied architecture
openly rather than calling it a root-free universe clock.

## 5. Major finding

### M1 — raw fresh-name collisions break the complete alpha quotient and its completion

`physical_key` is now structurally alpha-invariant, but event creation still
uses raw storage strings.  For the root event of call `k`, the allocator emits

```text
EROOT-CAP-0::Tk:r
```

and the root-birth newborn at call zero uses

```text
NROOT-CAP-0::T0:r.
```

`rename_seed_events` requires only a complete injective map of the six current
seed events.  It does not reserve a disjoint typed domain for future generated
identities.  `prevalidate_event_and_option` later rejects whenever one of the
raw generated strings is already a seed-event key or actor display name.

I constructed three exact counterprobes.

#### Counterprobe A — collision at the second call

Rename seed event `A0` to the presently unused string
`EROOT-CAP-0::T1:r`, and rename the other five seed events injectively.  For
both Q1 and Q2:

```text
renamed first histories                    16
renamed first physical atoms               16
first law equals unrenamed law              yes
second-call kernel                          rejects
rejection text          duplicate generated event identity
```

Thus the new quotient key says the two first histories are physically equal,
but the claimed next kernel is defined on one presentation and not the other.

#### Counterprobe B — failure at an arbitrary later call

Rename `A0` to `EROOT-CAP-0::T5:r`.  A deterministic valid run completes calls
zero through four identically in both Q cells.  The sixth call, whose root
ordinal is five, rejects on the nominal collision.  Hence a finite 16/408
battery can pass while the every-state assumption required for the infinite
Ionescu--Tulcea iteration fails on an alpha-equivalent presentation.

#### Counterprobe C — actor display/newborn collision

Rename actor D's display name to the presently unused future newborn string
`NROOT-CAP-0::T0:r`.  The root birth alternative then rejects with
`duplicate newborn`, although actor display names are absent from the physical
quotient and the ownership/addressed history is unchanged.

These are not collisions between two already existing physical records.  They
are collisions between a nominal name chosen by a valid finite alpha
renaming and a future name chosen by a non-equivariant allocator.  A finite
alpha bijection can always be extended to a permutation of the ambient name
set, so excluding precisely the allocator's future strings would make the
gauge group depend on hidden construction labels.

**Required repair:** put supplied seed identities, generated event identities
and actor identities in structurally disjoint typed storage domains, or use a
genuinely fresh opaque allocator whose alpha action is transported with the
history.  Raw display strings must never be used for physical freshness.
Add exact gates for:

1. a seed rename colliding with the next generated event name;
2. a seed rename colliding only at a later ordinal;
3. an actor display rename colliding with a future newborn name; and
4. original and adversarially renamed full projectivity plus multi-call
   continuation in Q1 and Q2.

This is a major because the round-2 opening required the **complete** supplied
seed event DAG to descend to the physical alpha quotient, and row-2 covariance
requires the next kernel—not only its reporting key—to be presentation
independent.  It is not a blocker because the normalized registered law and
the structural quotient formula are sound; the defect is localized to fresh
storage identity.

## 6. Decision-row disposition

The registered D35c presentation still has a normalized projective infinite
rooted-call measure, so this finding does not turn the scientific object into
row 4's finite trace.  Q1 and Q2 remain inequivalent, excluding selection row
1, and no spacelike-global opportunity normalizer appears.

The supported ceiling remains row 2 in narrowed form:

```text
TIMELESS ROOTED NESTED-CALL FAMILY / EXECUTABLE
```

but commit `8a9bb98` is not terminally covariant because its full alpha claim
fails.  Terminal promotion should wait until fresh identity is alpha-safe and
the adversarial late-collision continuation passes.

## 7. Final tally

```text
B  blockers  0
M  majors    1
m  minors    0
n  nits      0
```

**Final recommendation:** repair typed freshness, rerun original, safe-renamed
and collision-renamed 16/408 batteries plus a late-ordinal continuation, then
submit one narrow final covariance delta.  No probability formula, source-seal
content law or causal-ordinal interpretation otherwise requires repair in
this lane.

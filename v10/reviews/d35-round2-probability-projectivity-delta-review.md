# D35 round 2 — probability/projectivity/completion delta review

**Frozen target:** commit
`592e1028b75cb3052b734bf4d28aac0b8284936c`.

**Comparison:** D35 candidate `b08249c`, frozen replacement protocol
`2bb4fa2`, and
`d35-round1-probability-projectivity-hostile-review.md`.

**Lane:** exact normalization, all-cylinder projectivity, completed-history
measure, alpha quotient, next-A stopping semantics, corpus completeness and
repository hygiene.

**Verdict:** **MAJOR REPAIR — THE COMPLETE 16-CYLINDER/408-REFINEMENT LAW AND
IONESCU--TULCEA COMPLETION PASS, BUT THE PROMISED EVENT-ALPHA QUOTIENT DOES
NOT.**

**Count:** **0 blockers / 1 major / 0 minors / 0 nits.**

The round-1 probability minor and hygiene nit are repaired.  The new
executable now checks the complete first-call distribution rather than its
coarse projection, and the corrected corpus audit is complete and clean.
Independent reconstruction confirms those results exactly.

The remaining failure is narrower but load-bearing.  `physical_key` removes
transaction storage names and actor display names, yet retains raw seed-event
identifiers through `physical_event_id`.  The committed alpha gate renames
actors only.  A consistent alpha-renaming of the seed event identities changes
the alleged quotient distribution.  Therefore the frozen requirement of a
nontrivial **actor/event** alpha quotient has not been met, and the claimed
physical quotient map is not constant on its declared equivalence classes.

## 1. Fresh reproduction and hashes

I reran both the capability executable and corrected corpus audit under fresh
independent seeds `271828183` and `161803399`.  All four processes exited zero.
Each pair was byte-identical across seeds and to its committed receipt.

Exact hashes at the frozen target are:

```text
capability source
fa6d69e6d6b85620d19da8e80899dba4a3a5f976fb6e0b3fcfb7b1224a253c4d

capability stdout
8afc279b5ace76a2c7e043dc043d4b450f14536e262d353333d86c08899e304a

capability internal science
3d6703f6ef4fcc84588bf8927d32621052733b6652c27225553fa97772ed3679

corpus source
49e1de97450a83763aa478bedacc8c13793af7e569bafe79acb9045f858d663a

corpus stdout
fde217caff5e31c670cfc49c98ecea12048a3a2cd28ae1334026999f0f676fc6

D35 note
713c39d37cbf7ff1fd1ade4d226603db82e9f7ea603e670cd19e6855b7fe4e16
```

The capability executable hash-locks the rejected base source at
`06c997a1...3fa26`, prints `PASS 18/18`, and returns the narrowed noun
`TIMELESS ROOTED NESTED-CALL FAMILY / EXECUTABLE`.

## 2. Complete finite law and projectivity — pass

I did not use the printed projectivity summary as evidence.  Starting from the
primitive enumerator, I independently traversed each complete first-call
branch and every second-call branch, accumulated exact `Fraction` masses by
the complete first `physical_key`, and checked retained event records directly.

For **each** of Q1 and Q2 the independent result is:

```text
complete first-call histories                  16
complete first-call physical atoms             16
first-call total mass                           1
second-call refinements                         408
refinements from one first atom, min/max         16 / 56
full-cylinder marginal mismatches                0
old-event equality checks                     3,180
old-event mismatches                              0
old-root-in-new-root-ancestry checks             408
root-wire failures                                 0
```

Every individual second-call kernel sums exactly to one.  Accumulating

```text
P(first=h) K(second | first=h)
```

over every refinement reproduces the complete 16-atom first law exactly.
This closes round 1's E7 finding: the new test no longer hides two histories
behind the old 14-atom next-A projection.  The new receipt's seven-atom coarse
shadow is explicitly separate and is not used as the cylinder theorem.

The finite normalization proof also survives.  A query descends strictly on a
finite ownership tree; a newborn is not queried in the same call; every local
option menu is finite and sums to one; and every call returns after finitely
many actor cells.  Capability validation changes admissibility, not these
normalization facts.

## 3. Next-A stopping and cylinders without time — pass

For every one of the 16 first-call histories in both Q cells I independently
checked:

```text
transaction events touching root actor A before completion     1
that unique A-touching transaction event                        A2
all transaction events contained in Anc(A2)-Anc(A1)             yes
open mailbox/outstanding call after A2                           none
```

Thus A2 is A1's first root-wire successor in the frozen grammar.  Child work
may occur causally inside the call diamond, but it does not update A's wire.
The stopping event is “the current authenticated root call has returned,” not
an elapsed-time threshold.  Its probability is a finite call-cylinder mass.

No seconds, rate, waiting-time distribution or global opportunity denominator
is required.  The root-wire ordinal remains physical causal succession on the
distinguished A wire.  It is not a construction timestamp, although the fact
that every call is rooted and bracketed by A is substantive supplied physics.
The note preserves that ceiling.

## 4. Ionescu--Tulcea and event-DAG completion — pass at labeled/rooted scope

The completion assumptions are present:

1. the root law is supplied;
2. reachable finite rooted actor/provenance states form a countable discrete
   state space;
3. each reachable state has a normalized finite-support next-call kernel; and
4. every finite state admits another finite completed call.

Ionescu--Tulcea therefore gives a probability measure on infinite sequences of
completed rooted-call states for each fixed Q cell.  Every event at finite call
index has finite ancestry, and any causal interval lies in the finite past of
its upper event.  Persistent union is consequently a locally finite event DAG.
Finite labeled event-membership/ancestry questions are determined at finite
call depth, so the union map is measurable on the discrete sequence space.

The 408 direct checks show that old events are neither deleted nor mutated and
that the first root result remains below the second.  Hence the completed
labeled/rooted history measure is not reduced to a finite trace.

The argument does **not**, by itself, repair the alpha quotient below.  It
establishes a completed measure on the structurally addressed presentation;
descent to a physical relabeling quotient requires the kernel and history key
to be constant on the specified alpha classes.

## 5. Major finding

### M1 — the alleged physical key is not invariant under event alpha-renaming

The frozen replacement protocol requires:

> A nontrivial actor/event alpha-renaming must give the same quotient history
> distribution with no nominal name in the quotient key.

The committed gate performs only the actor half.  `renamed_base_world` changes
actor display names but deliberately leaves seed event dictionary keys and
event names unchanged.  That actor-only test passes.

The quotient function contains the defect:

```python
def physical_event_id(network, event):
    if event in network.provenance:
        return ("transaction", prov.tx, prov.event_address)
    return ("seed", event)
```

Transaction storage names are removed, but every unprovenanced seed event is
represented by its raw nominal string.  `physical_key` then uses those values
for actor tips and predecessor rows.

I constructed a second initial presentation by consistently alpha-renaming
the entire seed event DAG:

```text
A0 -> s0
AB -> s1
AC -> s2
BD -> s3
A1 -> s4
```

All event keys, event `name` fields, predecessor references, collector tips
and actor-owned tips were transported together.  The rooted marked history,
ownership tree, operations, carrier state, local probabilities and causal DAG
are otherwise identical.  Both presentations enumerate 16 branches with
total mass one and the same probability multiset.  The result is:

```text
                         Q1       Q2
actor alpha equality     yes      yes
event alpha equality     NO       NO
```

This is an exact counterexample to the advertised actor/event quotient gate.
Because `physical_key` is not constant on one declared alpha-equivalence
class, it is not a function on that quotient and cannot yet be used to claim a
quotient pushforward or quotient-cylinder projectivity.  Measurability on the
labeled discrete space does not cure failure to descend.

**Required repair:** define structural/canonical identities for the supplied
seed event DAG, or canonically quotient the full seed-plus-transaction marked
history.  Extend the alpha test to rename all actor identities, event
identities, predecessor references, tips and any identity-bearing boundary
fields.  Require exact equality of the 16-atom quotient distributions for Q1
and Q2, then repeat full two-call projectivity after the rename.  The receipt
must distinguish physical root boundary data such as the supplied namespace
from nominal event labels.

This is major rather than minor because alpha descent was a frozen repair of a
round-1 physical-quotient opening and is part of construction-order/covariance
qualification for the positive decision row.  It does not destroy the
normalized labeled kernel or its completed-history measure.

## 6. Corpus correction and hygiene — pass

The accidental broad `paper24` exclusion is removed.  The corrected inventory
contains the four previously omitted historical artifacts:

```text
V3 Paper 24
V4 Paper 24
V6 Paper 24
V7 Paper 24
```

It now reproduces:

```text
primary artifacts                   441
category-relevant artifacts         427
corpus stream
b0e4c7e0be1c8587b5f3b35e36a834fa8f485cf4bd7cfbb61331017bcd1541b7
gates                               5/5
```

The title cleaner strips after truncation, so the three round-1 trailing-space
lines are gone.  Both relevant full-range checks are clean:

```text
git diff --check b08249c..592e102
git diff --check de51b4e..592e102
```

I found no remaining corpus-completeness or repository-hygiene finding in this
lane.

## 7. Decision-row ceiling

The mathematical completion result still rules out row 4: a normalized
infinite rooted-call state-sequence measure and persistent labeled event-DAG
pushforward exist.  Q1 and Q2 remain inequivalent, so row 1 is excluded.  No
spacelike-global probability normalization appears, so row 3 is not the right
description.

However, commit `592e102` has not yet earned final promotion to the covariant
row-2 noun because its frozen actor/event alpha-quotient gate is false.  The
proper disposition is:

```text
row-2 ceiling supported on the labeled/rooted completed law;
row-2 terminal promotion withheld pending event-alpha repair.
```

If M1 is repaired without changing the normalized law, the maximum noun
remains exactly:

```text
TIMELESS ROOTED NESTED-CALL FAMILY / EXECUTABLE
```

It does not expand to peers, cycles, mutually initiating calls, disconnected
joins, the v9 stem spectrum, Lorentzian geometry, proper time or nature's law.

## 8. Final tally

```text
B  blockers  0
M  majors    1
m  minors    0
n  nits      0
```

**Final recommendation:** freeze M1, repair the full actor/event alpha
quotient, rerun both Q cells and the 16/408 cylinder battery under the renamed
presentation, then submit a narrow probability/projectivity closing delta.

# D35 round 1 — probability/projectivity/profinite hostile review

**Frozen candidate:** commit
`b08249c71ab42b839d43ec240aa8d0d8f7cfc902`.

**Lane:** exact probability, cylinder projectivity, completed-history measure,
event-DAG pushforward, root-wire/time typing, profinite ceiling, decision row,
hashes and diff hygiene.

**Verdict:** **ROW 2 IS MATHEMATICALLY EARNED AT THE DECLARED ROOTED
NESTED-CALL SCOPE, BUT ONE RECEIPT-COVERAGE MINOR AND ONE HYGIENE NIT REQUIRE
REPAIR BEFORE TERMINAL CLOSURE.**

**Count:** **0 blockers / 0 majors / 1 minor / 1 nit.**

The hostile result is positive on the main question.  D35 does not stop at a
finite table: every finite rooted state has a normalized finite-support call
kernel, every call terminates, the reachable state space is countable, and
Ionescu--Tulcea supplies a probability measure on infinite root-call state
sequences.  Persistent union then pushes that measure to locally finite event
DAG histories.  That is enough to distinguish decision row 2 from row 4.

The exact E7 executable gate is nevertheless weaker than its label: it checks
a 14-atom coarse next-A observable rather than the complete 16-atom first-call
cylinder.  I independently checked the full cylinder and it passes, so this is
not a theorem failure, but the frozen receipt must be made to test what the
note says.  Separately, the corpus receipt contains three trailing-space
lines.

## 1. Exact reproduction and artifact identity

I reran both frozen executables under fresh independent hash seeds
`2026071401` and `314159265`.  All four processes exited zero.  Each fresh
stdout was byte-identical both across seeds and to its committed receipt.

Frozen candidate hashes reproduce as:

```text
corpus inventory source
9347035205c9210ce6cbbbefab7242f3de687624c45098c0f6feb278850c80e6

corpus inventory stdout
49a4bd6a1adc1be8ba247e55cb254b9084bcf03c2ff180e57a1073895d41203f

timeless actor source
06c997a195294991293fdedc9edce005a3f8ad1d23bfd8f73a5a08490163fa26

timeless actor stdout
24a5cdfe35e1a85b25929217def4bede01e57169a14789392e7e5a7947a11656

D35 note
f0ae99fa7c2c484b8a71774bbc9faad2f49d3b2f88d2871df3bbd087565c688b
```

The actor receipt again prints internal science digest

```text
1f7b39ddaea634c1444695e5e536d528be45785e8c9997eba1388ed22cfe8aa6
```

and `PASS 18/18`.

The corpus receipt reproduces:

```text
primary files                    437
category-relevant files          423
corpus stream SHA-256
84d6fb20bf780d268ba825c38120e4754abdfce30e448a6df6ad66993fc27485
gates                            5/5
```

The inventory is correctly used as a forgetting/control ledger rather than a
semantic proof.  Its inherited probability boundary agrees with D3, D7,
D12, D17, D18, Paper 16 and the v9 stem-spectrum work: compatible cylinders
host a supplied law; neither projectivity nor profinite completion selects
that law; and the rooted labeled-prefix measure is not thereby identified
with the covariant v9 stem spectrum.

## 2. Finite normalization — pass

For a finite pre-call rooted tree, queries move strictly to children and a
newborn is not queried in the same call.  Induction on subtree height proves
termination.  At each visited actor, unavailable visit/fork mass is folded
into idle and the remaining exact option masses sum to one.  The product rule
therefore gives a normalized finite distribution on completed call trees.

This proof is all-size within the frozen grammar and does not depend on the
registered specimen.  The specimen independently reproduces:

```text
                         Q1                    Q2
completed branches       16                    16
total mass               1                     1
A2 birth                 1/4                   1/5
A2 fork                  1/8                   1/10
A2 idle                  3/8                   2/5
A2 visit                 1/4                   3/10
P(BD acquired)           1/4                   1/4
E(transaction births)    25/64                 63/200
E(newborn-one sum)       106929/1562500        1080576/9765625
```

All FIFO, LIFO and canonical actor-message runs have 16 branches and the same
16-atom complete history distribution.  Reverse child evaluation and reverse
shared-control evaluation agree exactly.  Thus scheduler order is absent from
the probability law on the tested call DAGs.

## 3. Full two-call projectivity and persistent-DAG pushforward

The analytical projectivity step is valid.  For each complete first-call
history `h`, the next kernel satisfies

```text
sum_h' K(h,h') = 1.
```

Consequently the two-call marginal of the full first-call cylinder is
`P_1(h)`, not merely a separately normalized approximation.  I independently
recomputed this using the complete `local_history_key`, rather than E7's
coarse key.  Results for each of Q1 and Q2 were:

```text
complete first-call atoms                   16
coarse next-A atoms                         14
second-call refinements                     408
complete-cylinder marginal mismatches       0
old-event mutation/deletion mismatches      0 / 408
first A2 absent from second A2 ancestry      0 / 408
```

Thus every first-call event is retained with identical kind, actors,
predecessors and flag through every registered second-call refinement.  The
second A successor also contains the first A successor in its ancestry.  This
is the required finite witness that state-sequence restriction and persistent
event-DAG restriction agree on the tested two-call domain.

The general pushforward is also sound.  After `k` calls the state contains
finitely many events and actors.  An event created in call `k` has finite past,
because its root cause lies on the finite A-wire prefix and its own call is
finite.  Hence every causal interval in the union DAG is finite.  Membership
and marked ancestry of any finite set of named events are decided by a finite
state prefix, so persistent union is measurable on the countable product
history space.

## 4. Completed-history measure: row 2, not row 4

The completion argument has all data Ionescu--Tulcea needs at the declared
scope:

1. a supplied initial finite rooted state;
2. a countable discrete space of finite rooted marked states;
3. a normalized finite-support kernel from every reachable state; and
4. measurable kernels automatically, because the state space is discrete.

Iterating the root-call kernel therefore defines a unique probability measure
for the **supplied Q cell** on infinite sequences of completed root-call
states.  The event-DAG map above gives the corresponding completed classical
history law.  Its finite prefix measures are automatically projectively
consistent.

This is sufficient for:

```text
TIMELESS LOCAL NEXT-CLICK FAMILY / EXECUTABLE
```

rather than `FINITE TRACE LAW ONLY`.  Row 1 is not earned because Q1 and Q2
both pass while giving different birth and next-A predictions; `q`, `g`, the
root and omitted sectors remain primitive data.  Row 3 is also inapplicable:
the probability factors are normalized on each queried actor's own finite
port menu, not over a spacelike universe antichain.

The word “timeless” remains narrowly defensible.  The model has physical
causal succession along A's record wire, and the distinguished root call
causally brackets the component's nested work.  It has no elapsed duration,
Poisson rate, proper-time magnitude or machine-global event counter.  The
rooted ownership/barrier architecture is strong extra physics, but the note
states that limitation explicitly.  It must not later be promoted to a
Lorentzian-local or root-free universe law.

## 5. Profinite ceiling — pass

At each fixed root-call depth only finitely many histories are reachable from
the frozen finite seed: every call has finite branching, and only finitely
many calls have occurred.  Prefix deletion therefore gives a finite rooted
inverse system hosting the classical measure.  That observation does not
identify its elements or bonding maps with v9's stem/covtree spectrum.

D35 correctly leaves open:

- quotienting nominal/construction presentations beyond its scheduler test;
- the map from rooted event-DAG cylinders to the v9 stem-observable algebra;
- a marked compact topology for more general continuous marks;
- continuity or Radon realization on the v9 spectrum; and
- extension of a quantum decoherence functional beyond a classical support
  mixture.

This matches the inherited ceiling.  Profinite organization preserves a
compatible law; it does not select Q1, Q2 or nature's law.

## 6. Findings

### m1 — E7 checks a coarse observable, not the claimed first-call cylinder

The note's E7 gate says “the first-call cylinder is exactly the marginal of
the two-call law.”  But `projectivity_gate` constructs its key with

```python
next_a_observable(branch, "A1")
```

for both the first law and the two-call marginal.  The receipt itself exposes
the compression: there are 16 complete first-call history atoms but only 14
`projective_first_atoms`.  Two physically distinct complete histories are
therefore merged before the equality is tested.

The full equality is true—my independent 16-atom/408-refinement calculation
above has zero mismatch—and the all-size kernel-normalization proof already
supports completed-history projectivity.  This is why the finding is minor,
not major.  Nevertheless an exact gate must test its advertised object.

**Required repair:** retain the coarse next-A check as a separate diagnostic,
but make E7 compare the full first-call marked-history cylinder against the
two-call marginal.  Add persistence/truncation assertions for old events and
the root-wire predecessor.  Print both `full_first_atoms=16` and
`coarse_first_atoms=14`, then regenerate source, stdout and internal hashes
and update the note's receipt paragraph.

### n1 — three trailing spaces make the D35 artifact range fail diff hygiene

`git diff --check 57d66d7^..b08249c` and
`git diff --check de51b4e..b08249c` report trailing whitespace in:

```text
v10/data/d35_corpus_causal_inventory.out:241
v10/data/d35_corpus_causal_inventory.out:317
v10/data/d35_corpus_causal_inventory.out:319
```

The cause is deterministic: `clean_field` truncates a normalized title to 180
characters but does not strip after truncation.  Three titles happen to end on
a space.  The current-commit note-only delta is clean, but the complete D35
artifact range is not.

**Required repair:** strip trailing whitespace after truncation in
`clean_field`, regenerate the corpus receipt and update its source/stdout
hashes.  The 437-file corpus stream hash should remain unchanged because the
underlying corpus bytes do not change.

## 7. Openings retained after repair

These are declared scope boundaries, not findings against row 2:

1. prove or reject an analogous measure for mutually initiating actors,
   cycles, peer calls and joins;
2. decide whether the distinguished A-root barrier is physical or should be
   removed by a broader covariant grammar;
3. construct the explicit construction-order quotient and bonding map to the
   v9 stem spectrum rather than inferring it from a rooted prefix tower;
4. lift the classical support mixture to actor-generated quantum operations
   without inserting an independent subsystem alongside record events; and
5. derive or empirically identify the local opportunity weights and birth
   couplings.

None of these openings demotes the completed rooted-tree family to a finite
trace.  They delimit the family that has actually been constructed.

## 8. Final disposition

```text
B  blockers  0
M  majors    0
m  minors    1
n  nits      1
```

**Final verdict:** **PASS THE ROW-2 THEOREM AT DECLARED SCOPE; REPAIR E7 TO
TEST THE COMPLETE CYLINDER AND CLEAN THE THREE CORPUS-RECEIPT SPACES BEFORE
THE NEXT HOSTILE ROUND.**

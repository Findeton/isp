# Paper 24 round 2 — causal locality repair delta

**Base commit:** `63ea1863bde134923bb04a5644ae4f10024e9012`.

**Reviewed target:** the current unstaged two-file repair diff above that base.

**Verdict:** **CLEAN — ALL PRESCRIBED CAUSAL-LOCALITY REPAIRS ARE EXACT AND
NO SCIENTIFIC OR SCOPE DRIFT IS INTRODUCED.**

**Count:** **0 blockers / 0 majors / 0 minors / 0 nits.**

## 1. Exact diff scope

The tracked repair touches exactly two files:

```text
12  9  v10/relativistic-isp-v10-paper24-the-next-click-is-a-causal-diamond-not-a-clock-race.md
 4  4  v10/reviews/paper24-round1-probability-mathematics-hostile-review.md
```

The complete binary diff SHA-256 is

```text
ce27cac5811b374d28a2028c6fe07908b1674f1c2e0663198f0fd5a50536f339.
```

The Paper 24 changes consist of three hunks only:

1. section 8.3 replaces the actor/owned-port-only capability sentence with an
   explicit division among actor/Q-cell menu inputs, carried call-boundary
   fields, issued-call ownership, adjacent route, requester held tip, shared
   rooted-call registers and the shared joint evaluator;
2. section 9.3 replaces “changes the law by adding” with “uses a different
   supplied, return-limited causal grammar”; and
3. section 14 replaces the obsolete “review remains required” sentence with a
   chronological pointer to round 1 and the focused closing deltas.

The archived probability-review changes remove only four terminal two-space
Markdown hardbreak suffixes from metadata lines. No word, number, verdict,
finding or historical target changes.

The repaired file hashes are:

```text
Paper 24
da097d6d10cf94bb3291a1615b525b35dbce885cea195ba1230b3f3c8fe0301f

archived probability review
b754a34aff6baa8630020ce154d8c5d1b35139b4e28a8930f9cda87a9b4ecac4
```

## 2. Capability-locality minor — closed

The revised section 8.3 no longer says capability admission consults only the
addressed actor's ports. It now states the actual architecture:

```text
menu probabilities and target legs
    addressed actor ports plus supplied Q cell;

capability admission
    carried call-boundary fields;
    target issued set;
    adjacent edge/route;
    requester held tip;
    shared rooted-call registers;

quantum/history evaluation
    shared joint carrier and event-DAG engine.
```

This matches D35d's implementation and terminal locality review. The shared
rooted-call checks are disclosed without being misdescribed as a global
opportunity normalizer. The earned claim remains logical causal locality in a
supplied A-rooted protocol, not target-actor-only validation, distributed
quantum storage or independent operating-system actors.

Round-2 m1 is therefore closed completely.

## 3. Paper 23 wording nit — closed

Section 9.3 now says D35 uses a **different supplied, return-limited causal
grammar**. It no longer suggests that D35 modifies D34b by adding a derived
limiter.

The surrounding accepted comparison is unchanged:

- Paper 23 identifies the minimal exact predictive quotient for its chosen
  D34b law and unlimited-horizon Branch F;
- D35 constructs a finite realized acquisition/stopping region for one
  selected A2 under another supplied law;
- D35's pre-call kernel still conditions on the complete typed rooted state;
  and
- no smaller predictive sufficiency/minimality theorem or cross-law boundary-
  size comparison is claimed.

Round-2 n2 is closed.

## 4. Cumulative whitespace nit — closed

The four archived two-space suffixes identified by the closing delta are gone.
The exact checks are:

```text
git diff --check
worktree_diff_check=0

git diff --check 63ea186 -- \
  v10/relativistic-isp-v10-paper24-the-next-click-is-a-causal-diamond-not-a-clock-race.md \
  v10/reviews/paper24-round1-probability-mathematics-hostile-review.md
scoped_diff_check=0

rg -n " +$" \
  v10/relativistic-isp-v10-paper24-the-next-click-is-a-causal-diamond-not-a-clock-race.md \
  v10/reviews/paper24-round1-probability-mathematics-hostile-review.md
no matches.
```

Round-2 n1 is closed without changing the archived review's meaning.

## 5. Additional chronology hunk — pass

The section 14 sentence is a correct status repair. Paper 24 now records that
round 1 and its repair receipt follow and that focused deltas decide promotion.
This agrees with sections 15--16 and the manuscript status line. It changes no
theorem, receipt, scientific noun or review result.

## 6. Fresh terminal receipt — unchanged

The D35d source and committed receipt remain:

```text
source
9ef590992e04beec0672a3772d41e1e01cde8315b65b7cd0aaa207a649c56e28

committed stdout
2150ddecfe92d3d0f2db6505a3e3ccc1c5c8685a4a2ea5a0497280939a023574.
```

A fresh run under

```text
PYTHONHASHSEED=982451653 \
  python3 v10/code/d35d_typed_identity_terminal_exact.py \
  > /tmp/p24r2.repair.982451653.out
```

exited zero, printed `PASS 18/18`, and produced the identical stdout hash

```text
2150ddecfe92d3d0f2db6505a3e3ccc1c5c8685a4a2ea5a0497280939a023574.
```

No D35 note, code or data file is changed by the repair diff.

## 7. Final disposition

```text
B  blockers  0
M  majors    0
m  minors    0
n  nits      0
```

**Final count:** **0B / 0M / 0m / 0n.**

This focused causal-locality repair delta is terminal-clean. It permits the
unchanged scoped noun:

```text
TIMELESS ROOTED NESTED-CALL FAMILY / EXECUTABLE
```

with the same mandatory ceiling: supplied A-rooted laminar logical actors,
binary licensed reach, actor/Q-cell local menus, explicit rooted-call
capability checks and a shared joint evaluator. It does not define a root-free
overlap law, a Paper 23 predictive-boundary reduction, physical proper time or
nature's interactive click law.

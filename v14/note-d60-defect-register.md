# D60 — THE TIE-BREAK DEFECT, REGISTERED CORPUS-WIDE

**Written:** 2026-08-10, out of the U4b adjudication (`17c31c4ba898`,
v14 #153, repair order 7).  **Status:** a REGISTRATION.  It records a
defect class, names the site, names the two gaps found beside it, and
sets an audit scope.  **It edits nothing and retracts nothing.**  No
committed unit is amended on the strength of this note, no terminal
verdict is disturbed, and no number anywhere in the corpus moves because
of it.  What it creates is an obligation on units that drive the affected
builder: state the immunity or price the exposure.

---

## 1. THE CLASS

**A tie-break over an unordered container is a hash-seed dependence.**

If a program chooses among several candidates by sorting them and taking
one, and the sort key is `repr` (or `str`) of an object that *embeds a
`set` or `frozenset` of strings*, then the chosen candidate is a function
of the interpreter's per-process string hashing and not of the program's
inputs.  That makes the delivery product not a function of the inputs,
which is the #91 class.

The class is narrower than "`key=repr` occurs here", and the difference
matters, because `key=repr` is common: it appears in 65 files under
`v10/`, 14 under `v7/`, 11 under `v14/`, 2 under `v11/`, and one each
under `v13/` and `bc/`.  Sorting strings, integers, or tuples of them by `repr`
is deterministic; the exposure needs a `set`/`frozenset` of strings
inside the sorted object.  A corpus-wide `key=repr` sweep would therefore
generate a false alarm at nearly every site it found.  The audit in §4 is
scoped to the mechanism, not to the idiom.

**Demonstration.**  Sorting three frozensets of `(str, str, int)` tuples
by `repr` under `PYTHONHASHSEED` in {0, 1, 7, 12345, 987654} returns a
different first element at seed 7 than at the other four.  Driving d60's
own `pick` at the committed record's first-arbitration prefix under the
same five seeds returns three distinct winners and four distinct sort
orders — while the *count* of matching candidates is invariantly the
same.  The count is safe; the choice is not.

## 2. THE SITE

`v10/code/d60_crystal_exact.py`, line 131, inside `Builder.pick`:

```python
hits = sorted((e for e, q in menu if spec(e)), key=repr)
```

The menu entries are event tuples that embed frozensets produced by
d42b1's `triples()`.  The line is reached on every pick, but it can only
*decide* anything when more than one candidate matches — that is, when
`maxhits > 1`.  Every unit that drives this builder, d66 included,
inherits the site.

**The immunity clause.**  A unit whose every event is specified by its
FULL TUPLE never consults the tie-break: at most one menu candidate can
match, `maxhits` is 1 at every step, and `sorted` is handed a
one-element list.  Such a unit is immune, and its byte-reproducibility is
a fact rather than a hope.

Two immunities are on the record already.  d60's own `C1` gate asserts
`b1.refusal is None and b1.maxhits == 1` for the 1-D crystal, so that
record is fully specified.  d66 asserts `maxhits == 1` over its sweep and
again in its arbitration-chain gate, and its own source says why: a full
event tuple can match at most one menu entry.  **U4b (paper-17) is immune
and gates it**: every event of every record it builds is specified by its
full tuple, its per-schedule constructibility gate requires `maxhits = 1`
at each of them, and it re-runs off-tree under a random hash seed and
reproduces both artifacts byte for byte.

## 3. THE TWO GAPS FOUND BESIDE IT

**(a) d60's `C2` gate omits the `maxhits` conjunct.**  Where `C1` asserts
`b1.refusal is None and b1.maxhits == 1`, the grid circuit's gate `C2`
(line 275) asserts only

```python
b2.refusal is None
```

So d60's 3 × 3 grid record is gated against refusal but not against
under-specification.  Nothing here says that record *is*
under-specified — the point is that its gate does not exclude it, and if
any of its picks were, the poset profile it publishes would be
hash-seed dependent.  Closing this needs d60 driven, which needs
d47a/d55c/d58; it is registered, not resolved.

**(b) d60 reads a source CWD-relatively.**  Line 70:

```python
_st = open('v10/code/d42b1_transport_exact.py').read()
```

The path is relative to the current working directory rather than to the
file's own location, so the run is correct only when launched from the
repository root.  That is a second, independent #91 residue in the same
file, and it is separate from the tie-break.

## 4. THE AUDIT SCOPE

Seven committed units carry the `pick`/`maxhits` mechanism and are the
scope of this register — **not** a corpus-wide `key=repr` sweep:

| unit | standing |
|---|---|
| `v10/code/d60_crystal_exact.py` | the site; `C1` immune, `C2` ungated (§3a) |
| `v10/code/d63_wide_crystal_exact.py` | to record immunity or exposure |
| `v10/code/d66_arbitration_crystal_exact.py` | asserts `maxhits == 1`; immune |
| `v10/code/d67_k4_double_grid_exact.py` | to record immunity or exposure |
| `v14/code/u4_crystals_exact.py` | to record immunity or exposure |
| `v14/code/w2_census_exact.py` | to record immunity or exposure |
| `v14/code/u4b_schedule_exact.py` | immune, gated, and measured (§2) |

Any successor that drives the same builder inherits the obligation
without being listed here.

**What each unit owes:** one line, either *immune — every event fully
specified, `maxhits == 1` gated* or *exposed — the tie-break is
consulted, and here is what it costs*.  A unit that cannot say which owes
the measurement, not the assumption.

**The standing rule this suggests, for whoever engraves:** a
byte-reproducibility claim by any unit driving a v10 grammar layer must
state the `maxhits == 1` immunity or price the tie-break — and state it
as a GATE, not as a remark.  A `PYTHONHASHSEED`-varied re-run is the
cheap standing check; U4b passes it.

## 5. WHAT THIS NOTE DOES NOT DO

It does not retro-edit d60, d63, d66, d67, `u4_crystals` or `w2_census`.
It does not reopen any terminal verdict.  It does not claim that any
published number is wrong: no number in this corpus is known to be
hash-seed dependent, and the two units that have been checked — d66 by
its own gates, U4b by measurement — are immune.  It records a defect in a
committed constructor, the two gaps beside it, and who owes what.

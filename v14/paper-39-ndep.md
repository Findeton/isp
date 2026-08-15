# IS NINE A PARAMETER? THE n-DEPENDENCE UNIT

**NDEP / paper-39, v14.**  Code `v14/code/ndep_exact.py`; transcript
`v14/code/ndep_output.txt`; receipt `v14/code/ndep_receipt.json`.  Pin
`v14/note-ndep-pin.md`.  Parents: paper-33 (the naming theorem and the
crystallization pair), paper-35 (the coset menu and the division-forcing
census), and the weld ladder the R-rung papers established.

```
NDEP-PORTABLE-3-OF-5<n=4 BUILT AND RUN ENTIRE -- AG(2,2), 48 DRIVEN HISTORIES, ACTOR LATTICE 15 COMPLETE, SYMMETRIC GROUP FILTERED WHOLE; n=16 A DECLARED WINDOW; EVERY ONE OF THE 6 TESTED NUMERALS IS q-CARRIED (6 OF 6), SO WHAT TRANSPORTS ON n ALONE IS THE LAWS AND NEVER THEIR NUMBERS>
```
```
NDEP-LAW-IN-N-NAMING<ROUTES=0 MISMATCHES OVER 53 DISTINCT PREFIXES AT n=4, ELEMENT SET AGAINST ELEMENT SET, THE WHOLE OF S_4 FILTERED PER PREFIX | n=16 21,080 COMPARISONS 0 MISMATCHES ON THE DECLARED PERMUTATION WINDOW, 2,064 POSITIVE | FORCED 45 OF 48, CHART 3 = THE CONSTANT-CLASS HISTORIES, ONE PER PARALLEL CLASS -- THE PARENT'S CHARACTERISATION VERBATIM | THE COUNT IS NEEDS-3>
```
```
NDEP-NEEDS-3-CRYSTALLIZATION<THE PAIR SURVIVES AS A STRUCTURE AND ITS FLOOR FORMULA DOES NOT: SCHEDULE TIME 3|5|7 AT n=4|9|16 = 2q-1 (NEEDS-3) | ATTAINED FLOOR 2|4|6 WHILE THE COUNTING BOUND ceil(log2 n) READS 4 AT n=16 (NEEDS-3) | THE SUCCESSOR FORMULA, IN WHICH THE EVENT SIZE q ENTERS, READS 2|4|6 AND MATCHES ALL THREE | OFFSET ONE AT ALL THREE (LAW-IN-N), ROUND ONE'S LAST EVENT REDUNDANT AT 2 OF 2>
```
```
NDEP-LAW-IN-N-COSET-MENU<SET-EQUAL AT n=4: THE GEOMETRY LEG'S 5 SURVIVORS OVER THE COMPLETE LATTICE OF 15 ARE EXACTLY THE 5 COSET PARTITIONS OF THE 5 TRANSLATION SUBGROUPS | THE COUNT IS q+3 AT PRIME q (NEEDS-3) | THE HYPOTHESIS FAILS AT q=4: THE DECLARED LINKS GENERATE 8 OF 16, SO THE q=4 ROW IS CARRIED UNSCORED AND THE TWO READINGS THERE (67 ABSTRACT SUBGROUPS, 7 F_q-SUBSPACES) ARE NAMED AND NOT CHOSEN>
```
```
NDEP-NEEDS-3-MOD-MOTIF<THE MOTIF SPLITS IN TWO. THE LADDER'S MODULUS IS DERIVED AND IS THE DECLARED LINK COUNT L: AT FIXED n=4 THE SWEEP L=1|2|3 RETURNS ACHIEVABLE BUDGETS {1,2,3,4,5,6,7}|{2,4,6}|{3,6}, SO MOD-3 REAPPEARS AT FOUR ACTORS AND THE MODULUS IS NEITHER sqrt(n) NOR THE CHARACTERISTIC, BOTH FIXED AT 2 THROUGHOUT; n=16 RETURNS {4,8}. THE COIN'S MODULUS IS A FREE DECLARATION: THE RECORD ENTERS EXACTLY MOD m (0 MISMATCHES OVER 144,991 PAIRS AT EACH OF m=2 AND m=3) WHILE THE CENSUS IS BLIND TO m (45 UNIQUE AND 3 NON-UNIQUE AT m=2,3,4,5)>
```
```
NDEP-LAW-IN-N-DIVISION-FORCING<UNIQUE FACTORIZATION 45 OF 48 OVER THE COMPLETE ACTOR LATTICE OF 15, THE DISCRETE PARTITION CHECKED ADMISSIBLE AT EVERY HISTORY SEPARATELY | THE 3 NON-UNIQUE ARE EXACTLY THE CONSTANT-CLASS HISTORIES AND THE PARENT'S THESIS HOLDS VERBATIM | UNION OF ADMISSIBLE PARTITIONS 4 = THE DISCRETE ONE PLUS ONE PER PARALLEL CLASS | THE COUNT IS NEEDS-3 | COUNTING-ONLY>
```
```
SCOPE=n=4 ENTIRE AND COMPLETE; n=16 A DECLARED WINDOW (CLASS TUPLES ONLY -- THE 2,627,625 GROUPINGS OF SIXTEEN SITES ARE OUT OF SCOPE, S_16 IS NOT FILTERED); q=3 ENTERS ONLY AS THE CONSTRUCTOR-FIDELITY LEG AND NO n=9 NUMBER IS RE-DERIVED HERE -- ALL TEN ARE ANCHORED READS OF THE PARENT'S COMMITTED RECEIPT OR FROZEN DECLARED CONSTANTS | SATURATION IS MAXIMAL AT q=2 AND q=3 AND IS NOT AT q=4, WHERE A WITNESS GROUPING REACHES 48 AGAINST THE BUDGET 16 | MEASURE=COUNTING-ONLY (E-24) | LANGUAGE=LAW-IN-N, NEEDS-3 AND BREAKS NAME THE TRANSPORT OF A PUBLISHED LAW AND NOTHING ELSE
```

## 1. THE QUESTION, AND WHY IT HAS AN ANSWER

The corpus works in one arena: the nine-actor plane, with four parallel
classes and three declared link directions.  Five laws were established
there.  Each of them is stated with numerals in it, and every one of those
numerals is either a 3, a 4, a 5 or a 6 -- small numbers in an arena whose own
parameters are 3, 4 and 9.  When the same small number appears in a law and in
the arena, a reader cannot tell from the law alone which of them it belongs
to.

The way to find out is to change the arena and look.  This unit builds
AG(2,2) -- four actors, the Klein-four translation group -- by the parent's
own grammar, and re-runs the five laws on it.  Where a law's numeral is 3, the
n = 4 arena separates the candidates that the nine-actor plane had collapsed:
the square root of the actor count is 2 there, and so is the field
characteristic, and so is the declared link count under the parent's
declaration.  Where those three
still coincide, a second axis is opened: the declared link count L is a free
axis of the arena, and sweeping it at FIXED n = 4 separates it from everything
that is a function of n.  Where the question survives both, the n = 16 window
answers it -- and the q = 4 plane is the first point at which the
characteristic and the square root part company.

Three words are used, with exactly one meaning each.  A law is LAW-IN-N when
the reading of it in which the numeral is a function of the actor count alone
agrees with the measurement at every arena point the unit can reach.  It is
NEEDS-3 when that reading fails and the reading in which the numeral is a
function of the square root -- or of the declared link count, which the sweep
separates -- succeeds.  It is BREAKS when neither does.  Nothing else is
asserted about the actor count anywhere in this paper, and the reading walls
of section 9 scan this text for sentences that would.

## 2. WHAT IS BUILT, AND WHAT IS ONLY CITED

The nine-actor numbers are not recomputed here.  Ten of them enter as anchored
reads of paper-33's committed receipt, at declared JSON paths, so that a path
drift which silently substituted another number would kill the run; six more
enter as frozen declared constants from paper-35, carried with the commit and
the digests at that commit, because that unit's working copies were mid-repair
when this one was built and reading mutable repository state is forbidden.
Every frozen constant is cross-checked against a value this unit computes
independently.

What IS recomputed at q = 3 is the constructor, and only the constructor.  The
parameterised builder is run once at q = 3 and its five substrate counts are
compared, row by row, against the parent's own: 280 groupings of the nine
sites into three triples, 36 of them saturating, 72 strict triples at R = 3,
276 near-flat quadruples, and a driven window of 600 schedules.  All five
agree.  That leg is what licenses the sentence "the same grammar at n = 4"; it
is a fidelity leg and not a finding, and it is stamped as one in the receipt.

### 2.1 The n = 4 arena and its corpus

The grammar transports term by term.  A grouping is a partition of the q^2
sites into q blocks of q; at n = 4 there are 3 of them, and they are exactly
the 3 parallel classes.  A round's incidence vector marks the cell (x, l) when
x and x + l share a block; a grouping is saturating when that vector's weight
reaches the budget n.  At n = 4, with the parent's own declaration of L = q
link directions, 2 of the 3 groupings saturate and the maximum weight is 4,
which is the budget: saturation is maximality here, as it is at q = 3.

The four corpora are the parent's, with 3 replaced by q throughout: the strict
R = L tuples whose summed field covers every cell, the same tuples at every
canonical seed menu, every ordered concatenation of two of them, and the
R = L + 1 driven window -- every class tuple, every near-flat tuple, the
alternating control and the collinear seed fan.

| corpus | schedules | rounds | events per history |
|---|---|---|---|
| C1 | 2 | 2 | 4 |
| C1FAN | 8 | 2 | 4 |
| C2 | 4 | 4 | 8 |
| C3 | 34 | 3 | 6 |

That is 48 driven histories, over 12 distinct event sets.  The corpus is small
and it is ENTIRE: nothing is sampled, and the actor lattice against which the
factorization question is asked is all 15 partitions of the four actors, with
no window in it at all.  Small and complete is a better instrument than large
and windowed, and the n = 16 rows below say plainly which they are.

## 3. LAW 1 -- THE NAMING THEOREM

The parent's theorem says that the stabilizer of a history -- the permutations
of the actors carrying every division event to itself, setwise -- is the Young
subgroup of the participation-signature partition.  The statement contains no
numeral at all, which is already a hint; the measurement is what settles it.

Two routes are run and compared as sets of permutations, per object.  Route A
holds the whole of S_4 and keeps what survives the definition; route B builds
the Young subgroup from the signature blocks and knows nothing of route A.
Over the corpus there are 53 distinct prefixes, and the two routes disagree at
none of them.  At n = 16 the symmetric group has 20,922,789,888,000 elements
and is not filtered; route A is taken instead on a declared permutation window
of all transpositions and all 3-cycles -- 1,240 permutations at every prefix,
21,080 comparisons in all, 0 mismatches, with 2,064 of the comparisons
landing inside the stabilizer and the rest outside it, so the window is
exercised in both directions.

The theorem transports.  Its NUMERAL does not.  At n = 9 the parent found
5,852 of 5,856 histories forcing identity and 4 chart; here 45 of 48 force it
and 3 are chart, and the 3 are not a residue but a characterisation: they are
exactly the histories that repeat a single parallel class in every round, one
for each of the 3 parallel classes.  The two sets are compared as sets, not as
sizes.  The chart count is therefore the parallel-class count q + 1, and the
n-only reading of the parent's 4 fails at n = 4.

| law | word | what the numeral is |
|---|---|---|
| naming | LAW-IN-N | NEEDS-3 |
| crystallization | NEEDS-3 | NEEDS-3 |
| coset menu | LAW-IN-N | NEEDS-3 |
| mod motif | NEEDS-3 | NEEDS-3 |
| division forcing | LAW-IN-N | NEEDS-3 |

## 4. LAW 2 -- THE CRYSTALLIZATION PAIR

The parent published two objects and was careful to name both: a schedule
time, 5, and an information floor, 4, with the floor argued from a counting
bound -- k events supply at most 2^k distinct binary signatures, so no history
can force identity on fewer than ceil(log2 n) events -- and measured to be
reached at n = 9.  The offset between them is one, and one redundant event
explains it.

All three legs are re-measured here.

| n | schedule time | attained floor | counting bound | sharpened bound | offset |
|---|---|---|---|---|---|
| 4 | 3 | 2 | 2 | 2 | 1 |
| 9 | 5 | 4 | 4 | 4 | 1 |
| 16 | 7 | 6 | 4 | 6 | 1 |

The schedule time is 3 at n = 4 -- constant across C1, C1FAN and C2, exactly
as the parent's 5 was constant across its three -- and 7 at n = 16.  Those are
2q - 1: two rounds of q - 1 informative events each, plus the one that closes
the second round.  The n-only reading fails at n = 16.

The floor is where the interesting thing happens.  The counting bound is a
true lower bound at every n, and this unit does not dispute it; what the n = 16
window shows is that it stops being the value REACHED.  At sixteen actors the
bound reads 4, and the smallest event subset that forces identity has size 6 at
every one of the 24 covering class tuples.  The reason is that the counting
bound ignores something the arena fixes: every division event has exactly q
members, so k events distribute total incidence kq, while n distinct binary
k-signatures cost at least the total weight of the n lightest distinct
k-vectors.  Imposing both conditions gives a sharpened floor, and it reads
2, 4 and 6 -- matching the measurement at all three arena points, including the
two where the counting bound also matched.  The parent's statement was correct
where it was made; its n-only generalisation is not, and the successor formula
needs q.

The offset survives everywhere: one at n = 4, one at n = 9, one at n = 16.  Its
mechanism survives with it and is measured rather than inherited.  At every C1
history the last event of round one is dropped and the signature partition is
unchanged -- 2 of 2 -- and when that event is moved to the end of the sequence
the crystallization time falls to 2, which is the attained floor.  The
transport procedure stamps this leg UNDISCRIMINATED, because a constant agrees
with all three candidate readings at once; the stamp is published with the
word rather than quietly dropped.

The pair's word is the weakest leg's: NEEDS-3.  What survives as a structure is
the pair itself -- a schedule time, an information floor beneath it, and one
structurally redundant event between them.

## 5. LAW 3 -- THE COSET MENU

The parent's geometry leg admits a partition of the actors when every declared
link's translation descends to the blocks, and its closed form says the
admissible partitions are exactly the coset partitions of the subgroups of the
translation group -- 6 of them at n = 9.

At n = 4 the leg is evaluated on all 15 partitions of the four actors and the
survivors are compared, element by element, with the coset partitions of every
subgroup of the Klein-four group, each subgroup obtained by closure of a
generator set.  There are 5 survivors and 5 coset partitions and they are the
same 5 partitions: the discrete one, the three parallel classes, and the
one-block partition.  The theorem transports; its count is the subgroup count
of the translation group, which is q + 3 at prime q.

| q | subgroups of T | q + 3 | declared links generate | group order |
|---|---|---|---|---|
| 2 | 5 | 5 | 4 | 4 |
| 3 | 6 | 6 | 9 | 9 |
| 4 | 67 | 7 | 8 | 16 |

The last row is the unit's sharpest scoping result, and it is a measurement.
The closed form needs the declared links to generate the WHOLE translation
group -- only then is every block a single coset.  At prime q the canonical
directions do generate it, and the q = 2 and q = 3 rows say so.  At q = 4 they
do not: every canonical direction representative has its first coordinate in
the prime subfield, so the four declared translations span a subgroup of order
8 inside a group of order 16.  The theorem's hypothesis fails there, and the
count itself becomes ambiguous in a way that only a non-prime q could expose --
the translation group has 67 subgroups as an abstract group and 7 subspaces
over its own field.  The unit names both readings and chooses neither; the
q = 4 row of the transport table is carried and left unscored by the
procedure itself.

## 6. LAW 4 -- THE MOD-3 MOTIF, WHICH SPLITS

The corpus's most-repeated coincidence is a 3.  A weld is motivated exactly at
budgets divisible by 3; the coin of the coupled walk reads the record only
modulo 3; the refinement ladder doubles from a first rung of 3.  All three of
those are cited from their parents, and the first of them is carried into the
transport table as a frozen declared constant, cross-checked against the
parent arena's own link count rather than typed.  The pin posed
a dichotomy -- does the motif become mod-q, or does it stay mod-3? -- and the
measurement dissolves it, because the appearances do not have the same
provenance.

**The ladder's modulus is derived.**  Each round contributes exactly n to the
summed link field, so R rounds contribute nR spread over nL cells; a
homogeneous record needs R/L per cell, and L must divide R.  That is an
argument, so the unit measures it instead: for each declared link count the
achievable budgets are found by exhaustive search over multisets of saturating
groupings, and the achievable set is checked to be exactly the multiples of the
first rung.

| declared links L | cells | saturating groupings | achievable budgets | modulus |
|---|---|---|---|---|
| 1 | 4 | 1 | 1,2,3,4,5,6,7 | 1 |
| 2 | 8 | 2 | 2,4,6 | 2 |
| 3 | 12 | 3 | 3,6 | 3 |

Every row of that table is at n = 4.  The actor count, the square root of the
actor count and the field characteristic are held fixed throughout, and the
modulus moves anyway: it is 1, then 2, then 3.  A quantity that moves while
n, sqrt(n) and the characteristic all stand still is not a function of any of
them.  The modulus is the declared link count -- and at n = 4 with all three
parallel classes declared, mod-3 reappears at four actors, which is as direct
a refutation of the square-root reading as the arena can supply.  At n = 16 the
same sweep at L = 4 returns budgets 4 and 8.

Under the parent's own declaration L = q, so the ladder does become mod-q, and
that is the pre-registered NEEDS-3 branch.  But the carrier is L, and L is a
declaration.

**The coin's modulus is declared, and free.**  The one-step operator's phase
block is diagonal with entries a root of unity raised to the record, and the
order of that root is not fixed by anything in the arena.  Both halves of that
sentence are measured.  Over a declared record family of 539 vectors every one
of the 144,991 unordered pairs is classified twice -- congruent modulo m or
not, carrying identical one-step operators or not -- and the two
classifications agree on every pair at m = 2 and again at m = 3, with 11,928
congruent-and-identical pairs and 133,063 incongruent-and-different at m = 2
and 2,731 and 142,260 at m = 3.  So the record does enter exactly modulo m.
And m is unconstrained: the whole division-forcing census is re-run at m = 2,
3, 4 and 5 and returns 45 unique and 3 non-unique every time.

The motif therefore splits into a derived half whose modulus is the link
count and a declared half that stays wherever it is put.  At n = 9 both were 3,
which is why they looked like a single mechanism.

## 7. LAW 5 -- THE DIVISION-FORCING FRACTION

The parent's census asks, at each history, which partitions of the actors the
committed structure descends along: the geometry, the history, the record and
the one-step dynamics, each a per-object predicate, the last at both declared
coin orders.  The discrete partition -- the n-fold division itself -- is
checked admissible at every history separately, so the count is never zero by
construction and the question is always whether anything joins it.

At n = 4, over the complete lattice of 15 partitions and all 48 histories,
45 histories admit the discrete partition alone.  The 3 that do not are exactly
the constant-class histories, and what joins the discrete partition at each of
them is exactly that history's own parallel class.  The union of everything
admissible anywhere is 4 partitions: the discrete one plus one per parallel
class.  The parent's thesis -- more than one factorization only where the
history repeats a parallel class -- holds verbatim, tested per history rather
than by comparing counts.

The fraction 45 of 48 is stamped COUNTING-ONLY.  No measure over histories is
declared here, so it is a count of this corpus's histories and not a
probability; and the corpus is a multiset, with 48 schedules over 12 distinct
event sets, so the two families are published separately and never crossed.

## 8. THE INSTRUMENT

Every outcome word is emitted by the real tester.  The transport procedure is
a pure function of its rows, and five synthetic laws are pushed through it --
one built to force each of the three words, one whose three candidate readings
coincide at every row (emitting its word with the UNDISCRIMINATED stamp), and
one whose every row is infeasible (refusing rather than defaulting).  Each of
the four criterion legs is then driven to true and to false on declared
objects, so no leg is a branch that never executes.

The n-only reading is fixed by rule and not fitted per law: a single datum at
n = 9 does not determine a function of n, so the n-only reading of every law's
numeral is the corpus's own n-only quantity -- the counting bound -- offset by
whatever constant reproduces the parent's numeral at n = 9.  The same rule is
applied to all five laws, so none of them gets a friendlier reading than
another.

One further scoping fact belongs here rather than in a law.  At q = 2 and
q = 3 a saturating grouping is a maximal one, which is what the parent's word
"saturating" suggests.  At q = 4 it is not: the coset partition of the
non-field subgroup generated by the two first canonical directions reaches
incidence 48 against a budget of 16.  Any successor that carries the grammar to
non-prime q must decide what the word is to mean there, and this unit does not
decide it.

## 9. SCOPE, AND WHAT IS NOT CLAIMED

The n = 4 results are exhaustive: the whole corpus, the whole actor lattice,
the whole symmetric group.  The n = 16 results are a declared window -- only
parallel-class tuples are built, because the saturating census at q = 4 would
need 2,627,625 groupings, and the naming theorem's route A runs on a
permutation window because S_16 is not filterable.  Every n = 16 sentence above
carries that qualification.  The q = 3 substrate counts are a fidelity leg for
the constructor and are not offered as findings; the nine-actor law values are
anchors.

This unit measures the transport of five published laws.  It does not measure
whether the actor count is selected by anything, and no sentence here says it
is or is not; the pin's question is answered in the only form a measurement
can answer it, which is one law at a time.  Nor is any count converted into a
likelihood: no measure over the space of arenas or the space of histories is
declared anywhere in this unit.

What the five words add up to is worth saying plainly, because it is not what
either branch of the pin's dichotomy predicted.  Three of the five laws are
portable -- the naming theorem, the coset-menu theorem and the division-forcing
thesis -- and all three are portable because their STATEMENTS contain no
numeral.  Two are not, and both of those are laws whose statement is a number.
And all 6 numerals tested, including the three belonging to the portable laws,
are carried by the square root or by the declared link count.  The pattern is
sharp enough to state as a candidate reading for the successor: in this corpus,
what survives a change of arena is the shape of a law, and what moves with the
arena is every number in it.

## 10. THE SUCCESSOR REGISTER

Four questions are left open and named.

The saturation clause needs a decision at non-prime q before the grammar can be
carried there at all, and the same is true of the coset menu, whose hypothesis
fails at q = 4 for a reason -- the canonical direction representatives lie in
the prime subfield -- that a different choice of representatives might repair.
Whether it can be repaired is not tested here.

The coin's modulus is free at this arena.  That is a statement about this
census, which is blind to it; a successor that measures something the coin's
modulus does move would convert the freedom into a declaration with
consequences, and until then the parent's 3 should be read as a choice.

The n = 16 window should be closed.  The saturating census at q = 4 is a large
but finite computation, and the division-forcing census there would test the
one law this unit could not carry past four actors.

And the sharpened floor is a formula this unit supplies and verifies at three
points; whether it is attained at every q is a theorem someone should prove or
break.

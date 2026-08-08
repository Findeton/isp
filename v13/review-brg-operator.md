# BRG — HOSTILE REVIEW, R1 (OPERATOR / ALGEBRAIC LENS)

**Reviewer:** R1, operator/algebraic lens.
**Protocol:** `v13/note-brg-hostile-protocol.md` (frozen, v13 #268), kill-shots K1–K5.
**Mode:** repo read-only. Nothing imported from the unit; every number below was
rebuilt from the published prose on my own instrument in the session scratchpad.
**Recomputations:** **92** independent (itemised in §9).
**Grade:** stated last (§10).

---

## 0. Hash verification of the frozen object

Verified before reading anything.

| artifact | declared sha256-12 | measured | match |
|---|---|---|---|
| `v13/paper-brg-bridge.md` | `3191e39da0b1` | `3191e39da0b1` | yes |
| `v13/code/brg_bridge_exact.py` | `6f288deb3ee9` | `6f288deb3ee9` | yes |
| `v13/code/brg_bridge_output.txt` | `e27aae1c48e0` | `e27aae1c48e0` | yes |
| `v13/code/brg_bridge_receipt.json` | `bf1b51d5e806` | `bf1b51d5e806` | yes |

The five hash pins the paper declares in §11 all agree with disk:
`note-brg-bridge-pin.md` `56ce4a7e2dee…`, `ha_successor_receipt.json`
`542b8735daf0…`, `nt_transport_receipt.json` `d256891b479a…`,
`gen_generality_receipt.json` `e0b2f444f6a9…`, `xba_crossbase_receipt.json`
`6015708df2a4…`. Re-verified at the end of the session: all four frozen
artifacts unchanged.

---

## 1. What survived

I record this first because most of the object is sound and the findings below
are all repairs, not demolitions.

- **The verdict is correct at its declared scope.** I rebuilt both sides from
  the prose and counted `hom(Z/p, ⟨W,D⟩)` in the **actual permutation groups on
  81 and 256 points** — not in the abstract dihedral model the unit consumes —
  at all 56 committed-scope cells, in both directions. Non-trivial forward: **0
  of 56**. Non-trivial reverse: **0 of 56**. `BRG-EMPTY-AT-CARRIER` stands.
- **Every load-bearing number reproduces.** The 40,320-member family, both
  spectra, `dihedral_relation_failures = 0`, the 12 classes, all eight committed
  instances, the 140-cell census, 137/3, the 14 morphisms, the abelianisation
  orders `{2,4}`, the dictionary integers to the last digit, the ambiguity sets
  2 and 864, the predicate teeth 10/25 and 2500/3125 and 16, the held-out
  0/234 and 54/234, the functor bit-counts 793 and 97,337, `ρ` non-reducible at
  exactly `{2,3}`. **No computed number in this unit is wrong.**
- **Delivery discipline is real.** A fully sandboxed rerun (the source and the
  four pinned receipts copied into scratch, repo untouched) reproduces
  `brg_bridge_output.txt` and `brg_bridge_receipt.json` **byte-identically** —
  same sha256 as the frozen artifacts. All **47/47** mutants exit 1.
  Corrupt-and-fire: I perturbed one integer inside the GEN receipt in scratch
  and the run died `exit 1` at a named anchor (`ANCHOR FAILURE A01`). My own AST
  sweep finds **zero** float/complex literals, zero `float()`/`complex()` calls
  and zero true divisions. A regex sweep of every integer > 3 in the paper
  against the receipt leaves 8 residues, all of them concatenation artifacts
  (`(1,1)` → `1111`, the prime list, dates, ledger numbers) — the paper's number
  register is clean.

The findings are ranked most-severe-first.

---

## 2. MAJOR — F1. G14, the gate that carries the scope-robustness fallback, is analytically forced

**Where.** §6 ("The exclusion, applied"), gate G14, and Deviation 2.

**The claim.** G14 is registered as a **must-pass** gate: "the arena-invariant
census … is measured EMPTY at every instance of every declared scope",
`instances_admitting_EVERY_declared_prime: 0` of `instances_tested: 20`.
Deviation 2 leans on it as the fallback that makes the verdict independent of
the scope choice: "A reader who prefers to call the twelve classes 'committed
carriers' gets the same verdict, because the arena-invariant intersection is
empty at every one of them too (G14)."

**What I measured.** The intersection test can only be non-empty if
`ord(D)` is divisible by a product of at least two of `{5,7,11,13,17,19,23}`
(all declared primes are odd, so `N | 2·ord(D) ⟺ N | ord(D)` for odd `N`).

| quantity | measured |
|---|---|
| smallest product of two declared primes | **35** |
| product of all seven declared primes | **37,182,145** |
| Landau bound: max order of any permutation of 9 labels | **20** |
| max defect order over the m=3 family | **15** |
| minimum degree for a permutation of order 37,182,145 | **95** labels, i.e. m ≥ 10 |

So on the 9-label arena **no defect whatsoever** — not merely none of the ones
measured — can admit two declared primes, and **no arena with m ≤ 9** can admit
all seven. G14's measurement could not have come out otherwise for any input in
the declared arena. RUNBOOK §14 addendum (v13 #208) is explicit:
"Analytically-forced clauses (true by algebra for every input) are disclosures,
not must-pass gates." The `invariance-lax` mutant kills G14 by changing the
*reading* (intersection → union), not by changing any datum, so no falsifier
touches the measured content.

**Aggravating.** The paper's stated reason does not cover its own instance set.
§6 justifies the result with "…and `ord(D) ≤ 15` over the whole family" — but
"the whole family" is the m=3 40,320-member family, while **species 4**, one of
G14's 20 instances, lives on **16** labels where the Landau bound is **140**. I
sampled 200,000 random 16-label completions in that arena and found defect
orders 21, 35, 42, 70, 105 — **3,057 of 200,000 (1.5%) have `ord(D)` divisible
by 35**, i.e. live at `p = 5` **and** `p = 7` simultaneously. The two-prime
clause is forced only at m = 3; it is false as a general statement about the
instances G14 tests.

**Severity.** MAJOR. No number moves; the scope-1 verdict does not depend on
G14. But the clause that makes the verdict robust to the scope choice is a
theorem about `{5,…,23}` and permutations of 9 points, not a measurement about
this corpus's geometry, and it is presented as the latter.

**Repair.** Demote G14's outcome to a disclosure carrying the structural bound,
and replace §6's paragraph with:

> **The exclusion, applied** (G14). Requirement 4 forbids the prime from
> carrying the verdict either way. Operationally: the morphism question is
> posed over the content invariant under the arena action, i.e. the
> intersection over the declared prime sweep. Measured over all 20 instances of
> both scopes: no instance admits a non-trivial morphism at every declared
> prime, and none admits even two. **This outcome is analytically forced within
> the declared arena and is recorded as a disclosure, not as a measurement:**
> admitting two declared primes requires `ord(D)` divisible by at least 35,
> and no permutation of the nine system-pair labels has order above 20 (the
> measured family maximum is 15); admitting all seven requires `ord(D)`
> divisible by 37,182,145, which needs at least 95 labels. The bound is stated
> for the nine-label arena only: at species 4's sixteen-label arena the Landau
> bound is 140 and defects of order 35 exist, so the two-prime clause there is
> contingent, and species 4's own measured `ord(D) = 2` is what carries it.

and in Deviation 2 replace "gets the same verdict, because the arena-invariant
intersection is empty at every one of them too (G14)" with "gets the same
verdict, because the arena-invariant intersection is empty at every one of them
too — for the structural reason recorded at G14, not for a contingent one."

---

## 3. MAJOR — F2. K2 answered: the 14 live-cell morphisms satisfy the FULL preservation predicate, and §10 reports them as "14"

**Where.** §4, §5, §10 ("What it does not say"), X05, Deviation 1.

**The question the protocol asks.** "Recompute the 14 morphisms at (p=5, ord 5),
(p=5, ord 15), (p=7, ord 7). Are they group-level only, or do they satisfy the
FULL preservation predicate?"

**What I measured.** They are **not** group-level only. I built HA's own source
arena `C_HA(p) = F_p^2 × F_p^2` at `p = 5` and `p = 7` (`ρ mod 5 = (1,1)`,
`ρ mod 7 = (6,6)`), built each live class's `⟨W,D⟩` as permutations on 81
points, picked an element of order `p`, and constructed an explicit
non-degenerate pair `(φ,Φ)`:

| live cell | SP1 | SP2 | SP3 | NT1 | NT2 | accepted |
|---|---|---|---|---|---|---|
| p=5, ord(D)=5 | 25/25 | yes | **3,125 / 3,125**, 0 violations | yes | yes | **YES** |
| p=5, ord(D)=15 | 25/25 | yes | **3,125 / 3,125**, 0 violations | yes | yes | **YES** |
| p=7, ord(D)=7 | 49/49 | yes | **16,807 / 16,807**, 0 violations | yes | yes | **YES** |

This is forced, and the unit's own §5 supplies the reason: the source action is
**free**, so every stabiliser is trivial and an equivariant `Φ` is a free choice
of image per orbit — for *any* `φ`, including the non-trivial ones. By the
unit's own formula the non-degenerate pair counts at the live cells are

`4·(81^125 − 36)`, `4·(81^125 − 36)`, `6·(81^343 − 18)`

— integers of **240, 240 and 656 digits** (I measured `|Fix(φ(R))| = 36, 36,
18` and the orbit counts 125, 125, 343).

**Why this is a finding and not a curiosity.** §2.2 defines a candidate morphism
as a **pair** `(φ,Φ)`. §4 is careful — it says "14 non-trivial **group**
morphisms exist over scope 2". But §10's "What it does not say" — the single
paragraph that bounds the unit's negative claim — says "a non-trivial
**morphism** does exist — **14** of them", dropping the qualifier. At the level
of the object the unit says a morphism *is*, the count is a 656-digit integer,
not 14. And §5's functor-level census is run only at the five rebuilt instances
(35 cells), i.e. **only where the group level is already zero**; Deviation 1
justifies the restriction with "it costs nothing, because the functor-level
count is zero wherever the group-level count is zero" — which is true, and is
exactly why the restriction removes the only cells where the functor level could
have been non-zero. The unit never measures its own headline object at the cells
where it is not zero.

**Severity.** MAJOR. The scope-1 verdict is untouched. But the paper's
self-bounding paragraph understates what exists at the extended scope by ~650
orders of magnitude and by one categorical level.

**Repair.** Run §5's count at the twelve classes as well (it is the same
formula, three extra live rows), and replace the second sentence of §10's
"What it does not say" with:

> Over the extended scopes a non-trivial morphism **does** exist — 14
> non-trivial group maps, at `p ∈ {5,7}` into the defect-order-5, -15 and -7
> classes, and, because the source action is free, each of them extends to
> non-degenerate structure-preserving pairs in the counts `4·(81^125 − 36)`,
> `4·(81^125 − 36)` and `6·(81^343 − 18)` (240, 240 and 656 digits). They
> satisfy the full preservation predicate, not merely its group clause; they are
> measured, reported (X05) and excluded from the verdict by the pin's own
> requirement 4, because their existence is a function of the declared
> reduction prime.

---

## 4. MAJOR — F3. The unit's own predictive held-out machinery passes at ADMISSIBLE primes, and this is not reported

**Where.** §8.1, X04, Deviation 3, §10.

**The claim.** X04: "The FOUND branch is exhibited **only** at a declared
synthetic pair, at `p = 3`, outside the deformation side's admissible primes."
Deviation 3: "The FOUND branch is synthetic … It is not evidence about the
committed arena in either direction."

**What I measured.** I ran the unit's own declared protocol — FIT = orbit 0
alone, extension to every other orbit by the declared source symmetry with the
rotation-valued assignment E-ROT, equivariance then *predicted* on the held
orbits — at the three live cells, which sit at **`p = 5` and `p = 7`: two of
HA's own seven declared primes**, on **GEN's own rebuilt classes**:

| cell | fitted | held-out cells | violations |
|---|---|---|---|
| p=5, ord(D)=5 | 1 orbit / 5 points | **3,100** | **0** |
| p=5, ord(D)=15 | 1 orbit / 5 points | **3,100** | **0** |
| p=7, ord(D)=7 | 1 orbit / 7 points | **16,758** | **0** |

That is precisely the "predictive held-out verification" the pin's requirement 3
demands of `BRG-MORPHISM-FOUND`, satisfied at an admissible prime on a committed
class. The unit's requirement-4 exclusion is a legitimate reason not to let it
carry the verdict. It is not a reason to leave it unreported: as written, X04
and Deviation 3 leave the reader with the impression that the FOUND machinery
has only ever been exercised at an inadmissible prime on an invented pair.

**Severity.** MAJOR — a disclosure gap in the one place a reader checks how
strong the negative is.

**Repair.** Add to X04:

> X04 … Separately, and reported here as an instrument reading excluded from the
> verdict by requirement 4: the same held-out protocol run at the three live
> extended-scope cells — `p = 5` and `p = 7`, both admissible on the deformation
> side, on GEN's own rebuilt classes — passes at 3,100, 3,100 and 16,758
> held-out cells with zero violations. The FOUND machinery is therefore
> exercised at admissible primes; what excludes those cells is requirement 4,
> not a failure of the verification.

---

## 5. MAJOR — F4. TINY-A's source is not a `Z/2`-set, and the count formula is brute-force validated only at orbit-exponent 1

**Where.** §5's tiny-cell table, gate G18, `make_cyclic_arena`, `tinies`.

**The declaration.** "TINY-A: source `Z/2` **acting freely on 4 points**; target
the Klein four group acting regularly on 4 points."

**What is built.** `tinies = [("TINY-A", 2, 4, 2, 4), …]` with
`gen = [(i+1) % npts for i in range(npts)]` — for `npts = 4` that is the
**4-cycle**, an element of order 4 handed to a `p = 2` arena.
`make_cyclic_arena` never checks `ord(gen) | p`, so
`act(1, act(1, x)) = gen²(x) ≠ x = act(0, x)`: **the source is not a `Z/2`-set**,
and the measured orbit count collapses from 2 to 1 (the receipt records
`orbits: 1`, which is impossible for a free `Z/2` action on 4 points).

**What I measured, both readings, from scratch:**

| reading | is an action | orbits | group maps | formula | brute force | non-degenerate |
|---|---|---|---|---|---|---|
| as implemented (4-cycle) | **no** | 1 | 4 | 16 | 16 | 12 |
| **as declared** (free `Z/2`, `(01)(23)`) | yes | **2** | 4 | **64** | **64** | **48** |

The delivered row `4 | 16 | 16 | 12` is what a malformed cell yields; the
declared cell yields `4 | 64 | 64 | 48`. TINY-B (`Z/3` on 3 points) and TINY-C
(`Z/5` on 5 points) are correctly specified — but both have **one** orbit.

**The consequence, which is the real damage.** With TINY-A collapsed, **all
three** delivered validation cells have `#orbits = 1`, so G18's brute-force
route validates `Σ_φ |C_tgt|^{#orbits}` **only at exponent 1**, where the
formula degenerates to `|C_tgt|` and is indistinguishable from any other
expression agreeing there. The census it validates runs at exponents
**125 … 12,167**. TINY-A was the only declared cell that could have exercised
exponent > 1, and it is the one that is broken. §5's own defence of the tiny
set — "The tiny set includes a cell with non-trivial group maps and a cell with
none, so the brute-force route validates the formula on both sides of the
question it is used to answer" — covers the group-map dimension and not the
orbit-exponent dimension, which is the dimension the formula actually asserts.

**Severity.** MAJOR. No headline number moves (I confirmed formula = brute force
under the *correct* reading too, 64 = 64), but a declared validation cell does
not instantiate its own declaration and the formula's exponent is unvalidated.

**Repair.** One character-level fix and one row:

> In `tinies`, build TINY-A's generator as the fixed-point-free involution
> `[1,0,3,2]` rather than the successor cycle, and add an assertion in
> `make_cyclic_arena` that `perm_pow(gen_perm, p) == pident(npts)` — the arena
> constructor must refuse a generator whose order does not divide `p`. TINY-A's
> row in §5 then reads `4 | 64 | 64 | 48`, and the formula is validated at
> orbit-exponent 2 as well as 1.

---

## 6. MINOR findings

### F5. §9's "coextensive … in both directions" is ambiguous, and false on one reading

§9's block quote reads "**The obstruction is order-coprimality**, and it is
measured **coextensive with emptiness in both directions** over every cell of
every declared scope"; eight lines later the paper writes "Stated at its
measured strength, **in the two directions**: **Forward** … **Reverse** …" —
using "directions" first for the two halves of an equivalence and then for the
two census directions.

On the second reading the sentence is **false, and I have the counterexamples**.
The reverse census is empty at **all 140 cells**, including the three where
`gcd(p, |⟨W,D⟩|) = p ≠ 1`:

| cell | gcd(p,|G|) | forward non-trivial | reverse non-trivial |
|---|---|---|---|
| p=5, ord(D)=5 | 5 | 4 | **0** |
| p=5, ord(D)=15 | 5 | 4 | **0** |
| p=7, ord(D)=7 | 7 | 6 | **0** |

The code is right where the prose is loose: G26's receipt text says "the
**forward** census is empty EXACTLY where…", and G27 correctly names "a
**second**, prime-independent" obstruction. But §10's qualifier table carries a
single row `obstruction | order-coprimality`, and §10's closing sentence gives
only the forward reason. The unit has **two** obstructions.

**Repair.** In §9 replace "coextensive with emptiness in both directions" with
"coextensive with the forward census's emptiness, in both directions of the
equivalence", and add to §10's table a row
`obstruction (reverse) | 2-group abelianisation (prime-independent)`.

### F6. §9's forward argument proves one direction of its own "iff"

"`hom(Z/p,⟨W,D⟩)` is trivial **iff** `p ∤ 2·ord(D)`" is stated, and the proof
given is "by Lagrange no such element exists unless `p | 2·ord(D)`" — which is
only `p ∤ 2·ord(D) ⟹ trivial`. The converse is Cauchy's theorem (or, explicitly,
the rotation `D^{ord(D)/p}`). I verified over **114 group × prime cells** across
19 groups — cyclic, dihedral, `S_4`, `A_5`-fragments — that the equivalence
holds with **no dihedral hypothesis whatsoever**: it is Lagrange + Cauchy for
any finite group. The entire geometric content of the "obstruction theorem" is
therefore the **order formula** `|⟨W,D⟩| = 2·ord(D)`, not the hom count.

That order formula is itself stronger than the unit measures it to be. It is
analytically forced: `ΣDΣ = D⁻¹` is an identity, since
`σ(σq⁻¹σq)σ = q⁻¹σqσ = (σq⁻¹σq)⁻¹`; `W² = 1`; and `W ∉ ⟨D⟩` because every power
of `D = (…)⊗I` is trivial on the pointer factor while `W = Σ⊗Σ` is `Σ ≠ 1`
there. I confirmed it numerically at all 12 class representatives by building
`⟨W,D⟩` on 81 points (2, 4, 4, 6, 6, 8, 8, 10, 12, 12, 14, 30 = `2·ord(D)`
throughout) and by checking the three dihedral criteria at each.

**Repair.** Append to §9's Forward paragraph:

> Conversely, if `p | 2·ord(D)` then `⟨W,D⟩` contains an element of order `p`
> (Cauchy; explicitly, for odd `p` the rotation `D^{ord(D)/p}`), so the census
> is non-trivial — the equivalence therefore holds for any finite group of
> order `2·ord(D)`, and the geometric content carried here is the order formula
> `|⟨W,D⟩| = 2·ord(D)`, which follows from `ΣDΣ = D⁻¹` (an identity in `q`),
> `W² = 1`, and `W ∉ ⟨D⟩` because `D` is trivial on the pointer factor and `W`
> is not.

### F7. X01 is false as stated

`|hom(Z/p, D_n)| = gcd(n,p)` fails at `p = 2` for **every** `n` I tested
(`1 ≤ n ≤ 20`): e.g. `n = 3` measures 4 against `gcd = 1`; `n = 1` measures 2
against `gcd = 1`; `n = 4` measures 6 against `gcd = 2`. It is true for every
**odd** prime. All declared primes are odd, so no number moves, but X01 is
stated unqualified and labelled "analytically forced".

**Repair.** X01 → "`|hom(Z/p, D_n)| = gcd(n,p)` **for odd `p`** is analytically
forced (it fails at `p = 2`, which is inadmissible on the deformation side);
recorded, never gated; neither census route invokes it."

### F8. The §14 self-tests measure the verdict of the DEGENERATE functor, which no arena action can change

`base_answer = evaluate_candidate(src0, tgt0, deg_phi, deg_Phi)["accepted"]` —
`deg_phi`/`deg_Phi` are F4-DEGENERATE, which NT1 and NT2 reject by construction.
Each of the four self-tests re-evaluates the same degenerate candidate under the
relabelled/conjugated arena; the receipt records `verdict: false`,
`matches_base: true` four times. There is **no arena action under which this
comparison could come out otherwise** — it compares `False` with `False` on an
object that is rejected before any arena datum is read. The `relabel-lax` and
`conj-lax` mutants die at the *points-moved* precondition, not at the invariance
clause, so no declared falsifier exercises the claim §6 makes ("The predicate's
verdict and the census's counts are measured invariant under the arena's own
action").

**Repair.** Run the self-tests on an **accepted** candidate with a non-trivial
count. The live-cell pair of F2 is available and free: relabel/conjugate at
`(p=5, ord(D)=5)` and check that the accepted verdict survives and that the
count stays 4.

### F9. The generator-change self-test does not read the generator

```
    inv_counts = []
    for j in range(1, p0):
        gen2 = perm_pow(gen0, j, fresh=True)
        arena = make_cyclic_arena(p0, src0["npts"], gen2, fresh=True)
        els, mul, e = dihedral_abstract(2)
        inv_counts.append(homs_route_a(p0, els, mul, e))
```

`arena` is assigned and **never read**. The appended value is
`homs_route_a(p0, dihedral_abstract(2))` — a function of `p0` and the constant
`2` alone. `generator_change_counts: [1,1,1,1]` would be `[1,1,1,1]` for any
generator whatsoever.

I proved this rather than argued it. In a sandboxed copy I replaced
`gen2 = perm_pow(gen0, j, fresh=True)` with a **transposition** — not a power of
`gen0`, not even of order 5 — and reran. Output line 140, unchanged:

```
G15 PASS   4 self-tests, all matching; arena actions move [81, 81, 625] points; generator sweep counts [1, 1, 1, 1]
```

§6 claims "replacing the source generator `R` by `R^j` for every `j ≢ 0`" is one
of the measured symmetry self-tests. It is not measured; the quantity recorded
is independent of the substitution. (The `perm_pow(..., fresh=True)` calls do
real work for the G16 cache-bypass count, which is why the defect is invisible
downstream.)

**Repair.** Pass `arena` into the census — e.g. count the homomorphisms out of
`arena`'s own group into the target and compare across `j` — or delete the
clause from G15 and from §6's sentence. As it stands the clause is dead code
presented as a measurement, which is the §14 addendum #219 disease in a new
place.

### F10. The two forward routes are related by a one-line identity, and both run inside the abstract model

Route A counts `{g : g^p = e}`; route B partitions **that same set** by the
cyclic subgroup each element generates and re-adds the parts. They are two
algorithms for one quantity related by a one-line identity — precisely what
RUNBOOK §13 addendum (v13 #234) warns is "one route". More important for this
lens: **both routes work inside `dihedral_abstract(n)`**, so neither tests
whether the abstract model is the right group. G03's comparator checks the
group **order** only (`comparator_group_order` compares `len(G81)` etc. against
`2*n`); order agreement does not imply isomorphism.

Nothing moves: I supplied the genuinely independent route — counting in the
**actual** permutation group `⟨W,D⟩` on 81/256 points at all 140 cells — and it
agrees at every cell, and I separately verified the dihedral criteria at all 12
class representatives (see F6). Recording it so the repair can cite a route that
is independent rather than merely differently-coded.

**Repair.** State in §4 that both declared routes consume the abstract model,
and add the permutation-group count as the third route (or upgrade G03's
comparator from order-agreement to an isomorphism check).

### F11. The 234 held-out cells test one algebraic bit, and §2.5 does not determine the extension

Two connected points.

(a) I reconstructed E-ROT/E-REF and reproduce **0/234** and **54/234** exactly.
The 54 decomposes as 9 held orbits with `δ₀ = 1`, × 3 points, × 2 non-identity
group elements. But the pass/fail is a single algebraic fact: equivariance holds
iff the extension element `τ` commutes with `φ(R)`. I tested **200 random
rotation-valued extensions** — all pass — and **50 random reflection-valued
extensions** — all fail. "234 held-out cells, 0 violations" reads as 234
independent verifications; it is one bit, verified 234 times.

(b) §2.5 does not contain the extension rule. The left-action convention
`Φ(T_δ S^c y) = τ(δ,c)·Φ(y)`, the assignment `rot = δ₀ + 2δ₁ + c mod ord(D)`,
and "reflection where `δ₀` is odd" appear **only in the code**. My first
reconstruction from §2.5 alone propagated within each orbit by `φ` — a reading
§2.5 permits — and got E-REF **0/234**: the teeth vanish. RUNBOOK §6 requires
witnesses reconstructible from specification.

**Repair.** Print the assignment in §2.5, and state in §8.1 that the held-out
check's content is centraliser membership, verified over 234 cells.

### F12. G23's fit-touch clause is analytically forced

`rot["fit_points"] == len(fit) * p_syn` is an identity whenever every source
orbit has size `p` — I checked at `|FIT| = 1, 2, 27` and it holds in all three.
The falsifiable content of G23 is the `len(fit) == 1` clause (which is what kills
`heldout-leak`). "3 points touched, verified by the fit-touch counter" (§8.1)
overstates it.

### F13. Three of the 77 anchors are typed literals against a source that is not hash-pinned

A14 (`192`), A15 (`16`) and A17 (`{1:12, 2:60, 3:48}`) are typed into the BRG
source and anchored to `v13/paper-xba-crossbase.md §9.4`. I checked: the XBA
**receipt** does not carry those three quantities, so the typed form was
necessary — but `paper-xba-crossbase.md` is **not** among the five sha256 pins,
so those three anchors are not hash-protected. §3.1's table does disclose the
source as "XBA paper" / "XBA §9.4", so this is not hidden. I independently
recomputed all three (species 4: `D` fixes 192 of 256, `W` fixes 16 of 256, the
120 single transpositions split 12/60/48) and they are correct.

**Repair.** Add `v13/paper-xba-crossbase.md` to the hash-pin block, or note in
§11 that three of the 77 anchors carry a paper-sourced committed value that no
hash pin protects.

### F14. Deviation 1's "measured isomorphism type"

For base 1 @ SP-E/F and base S the receipts publish the group **order** (4) and
the defect order (2), not the isomorphism type; the Klein-four type is
*inferred* (two commuting involutions). Immaterial — for odd `p`,
`hom(Z/p, G) = 1` for any group of order 4, and I confirmed both ambiguity sets
(2 candidates for base 1, 864 for base S) give `|⟨W,D⟩| = 4` throughout — but
"by their measured isomorphism type" should read "by their measured group order,
from which the type follows".

---

## 7. NOTES (no repair demanded)

**N1. The emptiness rests on the family's low-order tail.** Every committed
instance has `ord(D) ∈ {1,2,3}`; that band is **5,760 of 40,320 members
(14.29%)** of the declared family, and the seven instances with `ord(D) ≤ 2`
occupy **1,536 members (3.81%)**. Conversely **13,824 members (34.29%)** are
live at `p = 5`, **9,216 (22.86%)** at `p = 7`, and **23,040 (57.14%)** at one
or the other. The paper prints 13,824 and 9,216 in §7 as dictionary counts, so
nothing is concealed — but §10's "this program's spacetime structure is
**alongside** its transport geometry" would read differently beside the sentence
"and 57% of the declared completion family is live at one of the two smallest
declared primes." I would put that sentence in §10.

**N2. Every committed completion is a transposition or the identity.** Base G
and base T are single transpositions; base S′ is the identity. I swept the 28
single-transposition completions on the movable labels: they split **4 / 12 / 12**
across `ord(D) = 1 / 2 / 3` — nothing else is reachable by a transposition. The
minimal support of a completion with `ord(D) = 5` is **3** moved labels (a
3-cycle). So the committed instance set is exactly the transposition sector, and
that is *why* it lies in the low-order tail.

**N3. The cache figures in §6 are correct.** §6 quotes 100 lookups / 5 hits "at
that gate"; G16's detail records exactly that, while the end-of-run table reads
118/10. Both are right; the qualifier "at that gate" is doing real work and
should stay.

---

## 8. K2's second half — the honest feasibility of a live-cell base

The protocol asks: "is a completion with `ord(D) = 5` constructible on a carrier
compatible with the `p = 5` deformation arena? give the honest feasibility."

**The transport half is already done, and it is easy.** Completions with
`ord(D) = 5` are abundant — **4,608 of 40,320 (11.43%)**, plus 9,216 at
`ord(D) = 15` — the carrier is unchanged at 81 configurations, and the minimal
witness moves only **3** labels (a single 3-cycle on the movable labels; e.g.
`Q = [0,1,2,3,4,5,7,8,6]`). I built one and paired it with **HA's own**
`C_HA(5) = F_5^2 × F_5^2`: the pair satisfies SP1/SP2/SP3/NT1/NT2 over 3,125
cells and passes the unit's own held-out protocol over 3,100 predicted cells.
There is no carrier-compatibility obstacle — the unit uses no cardinality
criterion, correctly (§13's non-claim).

**What is missing is not constructibility but commitment.** The eight committed
instances are not chosen; they are what NT/GEN/XBA *measured*, and their `Q`s are
the identity or single transpositions (N2). Promoting a live class to a
committed instance requires a physical preparation whose Householder-cancellation
completion is at least a 3-cycle. That is a claim about the corpus's physics,
not about this census, and this unit is right not to make it.

**The decisive blocker is on the other side, and the paper names it correctly.**
The reduction prime is a **declaration** (HA G30: `|⟨R_HH⟩|` equals the declared
prime). Every live cell is prime-dependent by construction, so requirement 4
excludes it no matter how good the transport side gets. Open 1 — "Can the
reduction prime be fixed by anything other than declaration?" — is therefore the
right and only gate on the successor, and it is a deformation-side question. A
successor that builds an `ord(D) = 5` completion without first forcing `p` will
have built the easy half.

**One route the paper does not name, offered as a contribution.** At species 4's
**sixteen**-label arena the Landau bound is 140 and I sampled completions with
`ord(D) = 21, 35, 42, 70, 105`; **3,057 of 200,000 random completions (1.5%)
have `ord(D)` divisible by 35**. Such a completion is live at `p = 5` **and**
`p = 7` simultaneously — the first object in this corpus that would survive a
two-prime arena-invariant intersection, and therefore the first object on which
requirement 4's intersection reading has anything to bite. It does not reach the
seven-prime intersection (that needs `ord(D)` divisible by 37,182,145, hence
≥ 95 labels, m ≥ 10), so it does not overturn the verdict; but it converts F1's
"analytically forced" into "contingent" at m = 4 and is the cheapest available
test of whether the exclusion rule is doing work or doing arithmetic.

---

## 9. Recomputation register — 92 independent quantities

All on my own instrument, nothing imported from the unit.

**Transport side, rebuilt from GEN §8.1's law (25).** `Σ₉`; base G's defect
permutation, its order, its 45 fixed configurations, `W`'s 9, `|⟨W,D⟩| = 4`;
base 1's `W₃₆` fixed 6 and its two factors 18/12; species 4's 192, 16,
`|⟨W,D⟩| = 4`, and the 120-transposition split 12/60/48; base T's 3 and 6; base
S′'s 1 and 2; the 40,320-member sweep; the defect-order spectrum (8 values); the
fixed-configuration spectrum (7 values); dihedral-relation failures 0;
identity-defect 96 / geometry-bearing 40,224; the 12 `(ord,fixed)` classes with
populations; `|⟨W,D⟩| = 2·ord(D)` at all 12 by explicit closure on 81 points;
the three dihedral criteria at all 12.

**Census (11).** Forward counts in the **real permutation groups** at the 5
rebuilt instances × 7 primes and the 12 classes × 7 primes; the cyclic-subgroup
route agreeing at each; reverse counts by explicit commutator-subgroup closure
plus exhaustive quotient sweep at all 140 cells; abelianisation orders `{2,4}`;
56 + 84 = 140 cells; 137 empty / 3 live; 14 = 4+4+6; forward coextensiveness
with `gcd = 1`; the reverse coextensiveness **failure** with its three
counterexample cells; reverse total 0.

**K2, live cells (14).** Source arenas at `p = 5` (625 points, 125 free orbits)
and `p = 7` (2,401 points, 343 orbits); `ρ mod 5 = (1,1)`, `ρ mod 7 = (6,6)`;
elements of order `p` = 4, 4, 6; explicit pairs' SP1 (25, 49 cells), SP2, SP3
(3,125 / 3,125 / 16,807 cells, 0 violations), NT1, NT2; `|Fix(φ(R))| = 36, 36,
18`; non-degenerate pair digit counts 240, 240, 656; the unit's held-out
protocol at all three (3,100 / 3,100 / 16,758 cells, 0 violations).

**K1 / K3 / K4 (19).** X01 counterexample sweep (`1 ≤ n ≤ 20` × 9 primes);
Lagrange+Cauchy equivalence over 114 group × prime cells; Landau `g(4)=4`,
`g(9)=20`, `g(16)=140`; two-prime product 35 and seven-prime product 37,182,145;
`ρ` non-reducible exactly at `{2,3}`; `ρ mod p` at all 7 primes; primes dividing
`2·ord(D)` at the committed instances = `{2,3}`; `40,320⁹` = 42 digits;
per-record admissible 13,824 / 9,216 / 0; the two dictionary integers to the last
digit (38 and 36 digits); 504 spectrum cells; committed-scope per-record 0 at all
7 primes; base S ambiguity 864 with `|⟨W,D⟩| = 4` throughout; base 1 ambiguity
exactly 2 with `|⟨W,D⟩| = 4`; minimal completion support by defect order (8
values); the 28-transposition split 4/12/12; the m=4 sampled spectrum over
200,000 completions.

**K5, teeth and instrument (13).** SP1 10/25; BREAK-A 2,500/3,125; BREAK-A with
`R → R²` accepted 0/3,125; BREAK-B 16; E-ROT 0/234; E-REF 54/234; 200 random
rotation-valued extensions; 50 random reflection-valued extensions; the
fit-touch identity at `|FIT| = 1, 2, 27`; the synthetic arena's 27 orbits of 3;
base T's 2 non-trivial group maps; TINY-A both readings; TINY-B and TINY-C.

**Delivery level (10).** Five hash pins against disk; byte-identical sandboxed
rerun of output and receipt; 47/47 mutants exit 1; corrupt-and-fire exit 1 with a
named anchor; independent AST scan (0 floats, 0 divisions); paper number sweep
(103 integers, 8 regex artifacts); functor-census 793 and 97,337 bits; the
G15 bogus-generator probe; the 77-anchor audit; the family-fraction figures.

---

## 10. Verdict

No finding overturns a computed number, and none overturns the verdict. I
reproduced `BRG-EMPTY-AT-CARRIER` at the committed carriers by routes that do
not share the unit's abstract model, and the delivery is byte-reproducible with
47/47 mutants dying and anchors that fire on corruption. The obstruction theorem
is true; K1 is answered in the unit's favour, with the refinement that its
content is the order formula and that the "iff" needs Cauchy as well as
Lagrange.

But four things must change before this is terminal. The gate that makes the
verdict robust to the scope choice cannot fail inside its own arena and is
presented as a measurement (F1). The functor level — the object §2.2 defines a
morphism to be — is measured only where it is already zero, and the three cells
where it is astronomically non-zero are reported as the integer "14" (F2). The
unit's predictive machinery succeeds at two admissible primes on committed
classes and the paper says the FOUND branch exists only synthetically at an
inadmissible one (F3). And the one validation cell that could have tested the
count formula's exponent is built on a source that is not a group set (F4).

The negative result is real and I would defend it. What needs repair is the
accounting of what sits on the other side of it.

> ### **ACCEPT-WITH-FIXES**
>
> Blocking before terminal: **F1**, **F2**, **F3**, **F4**.
> Required: **F5**, **F6**, **F7**, **F8**, **F9**.
> Recommended: F10–F14, and N1's sentence in §10.
> Offered as contributions the repair may adopt with credit: the explicit
> live-cell pairs and their held-out passes (§3, §4), the Landau/product bounds
> (§2), the corrected TINY-A row `4 | 64 | 64 | 48` (§5), and the m=4
> `ord(D) = 35` route for the successor (§8).

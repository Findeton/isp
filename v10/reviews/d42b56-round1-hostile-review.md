# D42b5/6 round 1 — hostile review (pin + receipt + out; fronts 7-9)

**Reviewer round:** 2026-07-18, against HEAD 6f5e8f0. Objects: the pin
`v10/note-d42b56-rootfree-action-shadows.md` (d66093d, #317), the
receipt `v10/code/d42b56_rootfree_action_exact.py`, the output
`v10/data/d42b56_rootfree_action_exact.out` (#318, 4/4 PASS exit 0).
Read against: note-d42b3 (the decided trilemma D1-D7) and the d42b3
round-1 review's TS-system section (the 202/36/1037-64/1/2074/21-114/
313 anchors and the h-transform telescoping observation), note-d42b4
§4 (E1 the arb-layer pincer; E3' the boundary/basis identifications)
and the d42b4 review D-M1 (the 1/k-boundary identification, computed
both ways there), note-d42 (the double mandate), paper 28 §5.2-5.3
(Theorem 4 uniform rooting; "no stationary infinite kernel"), paper
29 (flat action squares, level-dependence), v6 paper 1 (both residues
verified to exist as named: TS integrability of the interacting
reconstruction; Lorentz-invariant sprinkling of division events;
Hegerfeldt), LOG #317/#318. Method: 3 receipt reruns (PYTHONHASHSEED
0/97/12345) byte-compared to the committed .out; an independent
verifier with its OWN family BFS, OWN diamond enumerator
(sequence-suffix method with explicit degenerate-repeat handling),
OWN memoized Z recursions under FIVE Z regimes (unit, menu-1/k,
class-1/k, arbitrary non-harmonic cut-attached, sequence-dependent),
full q'-menu multisets at the S2 pair under all boundaries, a
menu-shape collision census + bisimulation fixpoint (the A3 state
space), OWN spec-derived recursive relabelers with involution/
commutation/canon-functoriality/menu-equivariance gates, the S3 rank
computation by exact Gaussian elimination, and a three-mutant
battery. Scripts in the session scratchpad (`verify_d42b56.py`,
`followup_d42b56.py`, `mutA/B/C.py`). Nothing in the repo modified
except this file.

## VERDICT: 0 BLOCKER / 3 MAJOR / 2 minor / 1 nit — all CONFIRMED

**Every printed number reproduces exactly, twice over.** Receipt
rerun byte-identical to the committed .out on all three seeds, exit
0 (LOG's "0/97" consistent). My independent rebuild: family 1191
(1/6/32/176/976 by depth), 427 canonical classes (1/6/23/84/313),
202 diamonds by a different enumerator, ladder 0/36/0 with the
36-set SET-IDENTICAL to d42b3 D1(i)'s N-mismatch census, Z_unit([])
= 1037/64 (= the total depth-4 mu mass), S2 witnesses 133/2074 vs
1/16 (unit) and 6055/91816 vs 1/14 (the receipt's second boundary),
S4 0/0 over 1191 with my own relabelers, and the in-build 208 claim
corroborated TWICE (my naive no-base-recursion maps: 208 actor / 208
payload inadmissible; receipt-mutant with the base recursion removed:
exactly 208 actor violations, exit 1). The campaign's zero-false-
number record extends through this receipt. The three MAJORs are all
in the other dimension the campaign polices: what the gates are
CAPABLE of failing on, and whether pinned words name the objects
actually computed.

---

## THE COMMISSIONED COMPUTATIONS (referee-run, offered to the program)

**(1) The telescoping classification of the S1 gradient leg.** For
any Z keyed on histories, the diamond product telescopes:
g = q(e1|h) q(e2|h+e1) · Z(h+e1e2)/Z(h). Hence gradient flatness on
a diamond ⟺ mu-flatness (level 1) AND Z(h+e1e2) = Z(h+e2e1), i.e.
Z class-constancy at the top. Computed on all 202 diamonds:

| Z regime | violations |
|---|---|
| unit-boundary recursion | 0 |
| menu-1/k-boundary recursion (the receipt's) | 0 |
| class-1/k-boundary recursion (d42b4-canonical) | 0 |
| ARBITRARY cut-attached Z, NOT harmonic, no recursion | **0** |
| recursion from a NON-class-constant boundary | 69 |
| arbitrary sequence-dependent Z assignment | 198 |

Both receipt Z's are class-constant by construction (menus are
class-invariant — d42b3's own 764-point gate — so the backward
recursion propagates any class-constant boundary to a class-constant
Z). Given level 1 and that already-gated fact, **the S1 gradient leg
cannot fail**; and the harmonic property (the completion's actual
content) is invisible to it — a non-harmonic cut-attached Z passes
identically.

**(2) The naive-level identity.** Given level-1 flatness, the naive
cut-normalized products violate a diamond ⟺ N(h+e1) ≠ N(h+e2).
Verified as a set identity: the receipt's 36 product-violating
diamonds ARE d42b3 D1(i)'s 36 N-mismatch diamonds, element for
element. "Exactly the 36" is earned arithmetic whose content is this
one-line lemma plus the already-gated census.

**(3) The menu-shape census (A3's state space).** The whole
1191-history family has exactly FOUR menu shapes: sizes 548 / 331
(the root's: {4 p @ 1/8, 2 n @ 3/4}) / 188 / 124. One of the four —
{2 p @ 1/8, 1 r @ 1/4, 2 n @ 3/4}, 100 interior members — has TWO
distinct 1-step transfer profiles: 68 members like [pA0] vs 32
members like [pA0, selfA, ('p','A',v1',0)] differ in the target
shape of a p-branch. **Menu-isomorphic states with different
outgoing (kind, weight, target-shape) data exist, so "the local
transfer on menu-isomorphism state classes" (pin A3) is ill-posed as
literally stated.** The transfer IS well-defined on canonical
classes (0/114 exceptions), and the coarsest transfer-respecting
refinement of the shape partition (bisimulation, depth-4
truncation-absorbing) runs 4 → 9 → 14 → 16 → **17 states** — the
honest minimal state space for the eigenproblem at this depth.

**(4) The S3 rank.** The 114 interior-class harmonic equations on
427 class variables have FULL rank 114 (exact elimination), so the
free-boundary solution space is 313-dimensional — the pin's
"underdetermined" made precise, matching d42b3's 313-parameter
freedom.

**(5) The renewal pair, beyond the gate.** The receipt's shape-
multiset `iso` would pass the root against 330 other histories (the
root's shape class has 331 members, all depths, including every
idle-pad); histories whose menu equals the root's EXACTLY: 31;
histories structurally isomorphic under single-base renaming: 175.
For the PINNED pair the strong facts hold: the event-map v1 ↦ V0 is
a weight-preserving bijection of the full menus (structural, not
just shapes; verified), pv1 = ('p','A',v1,0) is exactly the
sigma-partner of pA0 (V0 is superseded at H3, so all four p's live
on the fresh base — the grab is robust), and non-stationarity is
robust under ALL shape-preserving bijections: the q'-multisets
differ at the pair under every boundary tested, with all four root
p's at one value and all four H3 p's at another (unit: 133/2074 ×4
vs 1/16 ×4; sigma-corresponding items differing 6/6). By the S4 menu
equivariance (below), the same witnesses hold for every
symmetry-image of the pair (all initiator/winner variants).

**(6) The boundary comparison (F1's evidence).**
Z_unit([]) = 1037/64 = total depth-4 mu mass. Receipt's
Z_1k([]) = 11477/3840 (boundary 1/|menu(h)|; depth-4 menu sizes
{4,5,6,8}). Canonical class-1/k Z([]) = **325/64** = the sum of
per-class mu over the 313 depth-4 classes (boundary
1/|class(h)| = 1/#linearizations; depth-4 class sizes {1,2,3,4,6})
— the exact extension of d42b4's Z([]) = 3 = Z_class meaning.
Class-1/k witness pair: **21/325 vs 1/16**, non-stationary,
all-bijection robust (the repair, pre-verified).

**(7) S4, strengthened.** My spec-derived relabelers agree with the
receipt's on all 98 distinct events. Both maps are involutions and
commute (the Z2×Z2 symmetry group); both are bijections of the
family; canon-functorial (gauge classes map to gauge classes, both
maps, 0/427); and the STRONGER property holds family-wide: the maps
intertwine the full candidate menus, (e,q) ↦ (σe,q), 0 violations
over 1191 — a generator-level measure isomorphism, strictly more
than the gated mu equality. Multi-author census: max version-name
author-tuple 1, max wkey 1 — 2-author winner sets do NOT exist at
depth ≤ 4 (same-payload proposals are edgeless and split into
singleton components; conflicting pairs force singleton MIS), so
vmap_actor's multi-author sort path is untested, vacuously correct.
Likewise vmap's self-recursion below one level is unreachable here
(all bases are V0 at this depth): what the family actually tests is
one-level base mapping — which is exactly what the naive maps broke
(208).

---

## F1 — MAJOR (CONFIRMED, computed both ways): the receipt's "1/k"
## is not the canonical 1/k boundary on record; the pinned word
## "canonical" names an object the receipt does not compute

The pin (A2, S1) claims "BOTH canonical boundaries (unit and 1/k)".
The only record fixing a canonical boundary pair is d42b4 D-M1 /
LOG #312: sequence/word basis ↔ unit boundary; class basis ↔ the
1/k boundary with **k = #linearizations of the terminal class**
("boundary Z(top-class) = 1/#linearizations gives Z([]) = 3 =
Z_class", gated in the d42b4 receipt as `Zclass == Fr(3)`). The
d42b56 receipt implements `Fr(1, max(1, len(CACHE[tuple(h)])))` —
**k = menu size**, a different quantity (depth-4 menu sizes {4,5,6,8}
vs class sizes {1,2,3,4,6}; Z([]) = 11477/3840 vs 325/64). The
printed S2 witnesses 6055/91816 and 1/14 are therefore true numbers
of an unpinned boundary wearing the canonical label — the
false-printed-clause class (the D-M1 precedent, ironically in the
same clause family). Aggravators: (i) no gate anchors WHICH boundary
Z_1k is — mutant C (boundary collapsed to `Fr(1)`, i.e. Z_1k ==
Z_unit) passes 4/4 exit 0 SILENTLY, so even total boundary collapse
is unprotected; (ii) the dead `kcount` helper (lines 63-66, computes
the candidate list then returns Fr(1) unconditionally) is a fossil
of exactly this definition churning in-build. What survives: every
gated CLAIM holds under the correct boundary — pre-verified: S1
gradient flat (0/202) and S2 non-stationary with exact witnesses
**21/325 vs 1/16**, all-bijection robust. Repair (pre-verified):
either implement `Fr(1, |class(h)|)` and anchor `Z_1k([]) == 325/64`
in the check, or keep menu-1/k but RENAME it (uniform-continuation
boundary), drop "canonical", and anchor `Z_1k([]) == 11477/3840`.
Either way the boundary anchor kills the mutant-C escape. LOG
forward-correction per the #304 precedent.

## F2 — MAJOR (CONFIRMED): S1's gradient leg is a cannot-fail gate,
## and "the completion RESTORES the action-level check" misattributes
## the restoration; the ladder is a repackaging whose separating
## content is d42b3 D2

By the telescoping classification (commissioned computation 1), the
gradient level is flat for EVERY cut-attached Z — harmonic or not —
and both receipt Z's are cut-attached by construction given the
already-gated menu class-invariance. So conditional on level 1
(itself d42a G1 inherited) the gate could not have failed: the
conviction class, in its subtler form (real numbers computed, but
mathematically forced by previously gated facts). The restoration is
due to the h-transform FORM (gradients telescope — an identity), not
to the completion: the completion's actual content (per-cut
normalization, positivity, the harmonic equation) is invisible to
the diamond check, which a non-harmonic cut-attached Z passes
identically (0/202). What genuinely separates the naive level is
exactly d42b3 D2: N IS cut-attached (class-constant, 0/427) but NOT
a discrete gradient — the per-step divisor q/N is not of telescoping
form, and the 36 diamonds are the certificate. Level 2's content is
the set identity with d42b3's census (commissioned computation 2);
level 1 is inherited; level 3 is an identity. New mathematical
content of the ladder: none — its value is presentational (the
action-level framing of decided facts; paper 29's level lesson,
which the citation carries correctly). Also: the pin's clause "(0
violations, any boundary)" is FALSE under the receipt's own
sequence-keyed representation — a recursion from a non-class-constant
boundary violates 69/202 (d42b3's cut-attached TYPE discipline
covers the charitable reading; the pin sentence as printed does
not). Repair: keep the THEOREM-class label but state the mechanism —
"the gradient level is flat BY TELESCOPING for every cut-attached Z;
the ladder's separating fact is that N is cut-attached but not a
gradient (D2); the diamond check cannot see the completion's
normalization content" — qualify "any boundary" to "any
class-constant (cut-attached) boundary", and either demote the
gradient leg to a stated identity with a Z-class-constancy gate (the
real falsifiable content) or keep the sweep labeled as a consistency
re-derivation.

## F3 — MAJOR (CONFIRMED, with witness): A3's pinned state space is
## ill-posed, its "≡ one open core" is a one-way reduction
## overstated as an identity, and the S3 gate is `check(True and
## iso)` — the conviction class at a pinned front-7 deliverable

Three convictions. (i) **The state space.** "A positive eigenvector
problem for the local transfer on menu-isomorphism state classes" is
not well-defined: menu-isomorphic states with different transfer
data exist (commissioned computation 3's witness — [pA0] vs
[pA0, selfA, p-on-v1'], same shape, different target shapes; 1 of
the 4 family-wide shapes is ambiguous). The honest state space at
depth ≤ 4 is the 17-state bisimulation quotient (or canonical
classes, where the transfer is verified well-defined 0/114); the
eigen-form Z(h) = f(state)·λ^{-depth} must live there. (ii) **The
identification.** Stationary/product-form solutions are a STRICT
SUBCLASS of infinite-volume positive-harmonic Z's: nonexistence of
the d42b3 residue kills front 7, but a positive harmonic Z existing
does NOT settle stationary existence (a Martin-boundary mixture need
not be product-form). "Front 7's root-free question ≡ d42b3's
infinite-volume residue — one open core, not two" is at best a
reduction INTO the residue's theory; the ≡ and the arithmetic of
open cores overstate it. The declared-OPEN status itself is honest
and unaffected. (iii) **The gate.** `check("S3 ...", True and iso)`
computes nothing: `True and iso` re-consumes S2's already-gated
bit, inflating the PASS count with a correlated tautology (if iso
failed, S2 and S3 would both fail on one fact). The pin does scope
S3 as "printed... no existence gate" — which licenses a print, not a
counted PASS. Grade note: this is not the d42b7 BLOCKER pattern (no
pinned COMPUTATION was promised and faked; no false number printed);
it is the wrong-pinned-identification class (D-M1 precedent) plus a
decorative check. Repair (pre-verified): replace the check's content
with (a) class-level transfer well-definedness (0/114), (b) the rank
computation (rank 114 on 427 variables → 313 free), (c) the
menu-shape ambiguity disclosure + the 17-state quotient as the
corrected state space; restate A3 as "front 7 REDUCES to a
distinguished sub-question (positive λ-eigenvector on structural
state classes) of the residue's positive-harmonic theory — one
theory, the stationary question a strict specialization"; keep the
no-existence-claim clause verbatim.

## F4 — minor (CONFIRMED): S2's gate tests a near-information-free
## proxy, and its intended strengthening is dead code

`menu_shape` equality is 4-valued over the whole family; 331
histories share the root's shape (every idle-pad included), so the
gated `iso` bit cannot distinguish the pinned renewal from shape
coincidence — the pin's own stronger phrase ("the renewal structure
of the grammar") is not what the gate checks. The intended witness
binding `v1n` (line 129, the fresh-base version name) is DEAD — the
assert that pv1 lives on the fresh base was never wired. Factually
everything holds and more (commissioned computation 5): the
structural event-map bijection, the robust pv1 identity, the
all-bijection non-stationarity, the 6/6 sigma-sweep. Repair
(pre-verified, three lines): wire `pv1[2] == v1n`, gate the
structural bijection `{(sig(e),q)} == set(root menu)`, and disclose
the shape census (4 classes / 331 sharing the root's) as the
proxy-weakness note.

## F5 — minor (CONFIRMED): fresh dead code and receipt hygiene

(i) `kcount` (63-66): dead AND vacuous — computes `cands`, returns
`Fr(1)` unconditionally; had it ever been used as the boundary it
would have silently collapsed 1/k onto unit (mutant C shows no gate
would have noticed — see F1). (ii) `v1n` (129): dead (F4). (iii)
`from itertools import permutations` (9): unused. (iv) `max(1, ...)`
in the boundary lambda: dead guard (depth-4 menus have ≥ 4 items).
(v) The receipt re-implements the family walk instead of calling the
exec'd, gate-verified `enumerate_family` (behaviorally identical
DFS; needless duplication). (vi) Relative-path exec source: runs
only from repo root; wrong cwd → FileNotFoundError exit 1 —
fail-safe, never false-green (d42b4 D-n2 hazard, unchanged, same
one-line fix available). (vii) Exec-head hygiene otherwise clean:
the slice marker occurs exactly once in the d42b3 source and the
head is definitions-only (no double enumeration, no re-executed
gates). Plumbing verified: mutant A (anchor 36→35) dies exit 1;
mutant B (naive relabeler) dies exit 1 at exactly 208; seeds
byte-identical.

## F6 — nit: two citation loosenesses in A2/A4

(i) "paper 28's uniform-rooting theorem anticipated this": Theorem 4
is a conditional root-LOCATION law (covariant root laws uniform over
vertex orbits within a finite unrooted network); it says nothing
about depth-dependence of truncated completions. The load-bearing
records are the D42 mandate's "stationary or infinite
action-compatible root-free completion attempt" and paper 28 §5.3's
"no stationary infinite kernel is constructed" — cite those; keep
Theorem 4 as atmosphere at most. (ii) A4's sprinkling precursor: the
gated symmetries are the internal Z2×Z2 (actor exchange, payload
flip) plus foliation gauge (Z class-constancy, re-cited) — a
necessary-condition precursor with NO analogue of the Lorentz sector
touched; the pin's hedges ("precursor", "continuum limits NOT
claimed", Hegerfeldt, the d42b4-E1 arb-layer gate — all verified to
carry as cited, and both v6 residues exist as named) keep it honest;
one clause naming the scope ("internal relabeling symmetries and
foliation gauge only") would close it.

---

## WHAT SURVIVES (verified, this round)

- **Every printed number** (family 1191; 202 diamonds; ladder
  0/36/0; Z_unit([]) = 1037/64; 133/2074 vs 1/16; 6055/91816 vs
  1/14 for the boundary as implemented; 0/0 over 1191; the in-build
  208, corroborated twice). Byte-identical reruns, seeds 0/97/12345.
- **A1's mathematical content** — true and THEOREM-class, with the
  corrected attribution: level-relative flatness stands; the
  separating fact is D2 (N cut-attached, not a gradient); the 36 are
  set-identical to d42b3's census; the gradient level is flat by
  telescoping for every cut-attached Z, both boundaries included.
- **A2's exhibit** — genuine and STRONGER than gated: the pinned
  pair is structurally renewal-isomorphic (event-level
  weight-preserving bijection, not just shapes); non-stationarity is
  robust under all menu pairings, all proposal choices, both
  implemented boundaries AND the correct canonical boundary
  (21/325 vs 1/16), and all symmetry-images of the pair.
- **A3's substance** — the reduction survives as a one-way reduction
  on a corrected state space (canonical classes / the 17-state
  quotient); underdetermination is now precise (rank 114, 313 free);
  the OPEN declaration is honest.
- **A4's declarations** — scope-honest throughout: no continuum
  claim; Hegerfeldt and the d42b4-E1 arb-layer gate carried
  correctly; both v6 residues exist as named; the covariance gates
  are exact and my STRONGER menu-equivariance version holds
  family-wide (0/1191), with involutions, commutation,
  canon-functoriality, and family-bijectivity all verified; the
  relabel maps match the spec exactly; the multi-author and deep-
  recursion code paths are unreachable at depth ≤ 4 (declared
  untested, vacuously correct — no 2-author winner sets exist).
- **The plumbing** — exit-1 discipline real (mutants A and B die at
  the designed anchors), seed-independence real, exec-head clean,
  fail-safe under wrong cwd.

## PRESCRIBED REPAIRS (pre-verified where stated)

- **R1 (F1).** Fix or rename the second boundary. Canonical option
  (pre-verified): boundary `Fr(1, |class(h)|)`, anchor `Z_1k([]) ==
  325/64`, new S2 witnesses 21/325 vs 1/16 (robust). Rename option:
  keep menu-1/k as "uniform-continuation boundary", drop "canonical",
  anchor `Z_1k([]) == 11477/3840`. Either kills the mutant-C silent
  collapse. LOG forward-correction per #304.
- **R2 (F2).** Print the telescoping sentence; qualify "any
  boundary" → "any class-constant boundary"; add the Z
  class-constancy gate as the gradient leg's falsifiable content (or
  keep the sweep explicitly labeled a consistency re-derivation);
  attribute the naive/gradient separation to D2.
- **R3 (F3).** Replace `True and iso` with the three computed gates
  (class-level transfer 0/114; rank 114 → 313 free; the shape-
  ambiguity witness + 17-state quotient); restate A3's ≡ as a
  one-way reduction into the positive-harmonic theory. All three
  computations run in ~2 s exact (pre-verified end to end; numbers
  above are anchors).
- **R4 (F4).** Wire `pv1[2] == v1n`; gate the structural menu
  bijection; disclose the 4-shape/331 census.
- **R5 (F5).** Delete `kcount`, the unused import, the dead guard;
  either use the exec'd `enumerate_family` or keep the local walk
  with a one-line note; optionally anchor the exec path absolutely.
- **R6 (F6).** Swap the paper-28 citation to §5.3 + the mandate;
  add the symmetry-scope clause to A4.

## Disposition

The receipt is numerically impeccable and its exhibits are real —
in two places (menu equivariance, structural renewal isomorphism)
the truth is strictly stronger than what was gated. The round's
findings are all in the campaign's second currency: a canonical
label worn by the wrong boundary (F1), a cannot-fail gate sold as
the front-8 check (F2), and a pinned reduction whose state space
does not exist as named plus a decorative check (F3). All three are
repairable at receipt level with the pre-verified computations
above; no result retracts, and the corrected statements are, if
anything, sharper: the ladder becomes a theorem with its mechanism
stated, the renewal exhibit becomes structural, and front 7's
reduction lands on an explicit 17-state quotient with the honest
one-way arrow into the ONE positive-harmonic residue.

---

# DELTA VERIFICATION (2026-07-18, against HEAD 19e9974: pin amendments
# B1-B4 at 9ab4a10, repaired receipt + .out + LOG #319/#320)

**VERDICT: DELTA-CLEAN.** Every repair verified by independent
recomputation; every referee anchor lands; all three MAJORs
discharged; the pre-flagged vestige exists and is recorded below with
four nit-grade notes — none touches a printed number or a gate's
honesty. Method: 8-seed rerun battery (PYTHONHASHSEED 0/97/12345/1/2/
3/4/42 — ALL byte-identical to the committed .out, exit 0; LOG "0/97"
consistent), an independent delta verifier (own linear-extension
counter, own Z recursions, own bijection/bisimulation constructions,
own control-Z counts), an exact replication of the receipt's own
enumeration for the representative-sensitive control, and a
three-mutant battery (D/E/F). Scripts in the session scratchpad
(`delta_verify_d42b56.py`, `mutD/E/F.py`).

## D-1 (F1) — DISCHARGED, computed both ways

The boundary is now the CANONICAL class-1/k. Verified at depth:
`lin_ext_count(h)` == |canonical class(h)| for ALL 1191 histories (0
mismatches — every linear extension of every family poset is itself
generated and admissible, so the receipt's per-history
linear-extension implementation and my round-1 member-count
implementation are THE SAME boundary, and it is class-constant/
gauge-invariant as labeled). My own recursion under it reproduces
Z_1k on every history and Z_1k([]) = 325/64 — now asserted IN-CODE,
and the assert has teeth: mutant D (boundary silently swapped back to
the menu reciprocal) dies at the assert with exit 1, printing exactly
the round-1 wrong-object value 11477/3840 — the round-1 mutant-C
silent-collapse escape is closed. S2's gate now anchors the witnesses
21/325 vs 1/16 in the check condition (my pre-verified anchors; unit
133/2074 vs 1/16 printed). The menu reciprocal is retained relabeled
as a probe inside the S1 sweep only — de-canonized as prescribed.

## D-2 (F2) — DISCHARGED; the conviction class is resolved by
## honest labeling plus a firing control

S1 now states the gradient leg as a TELESCOPING THEOREM and gates
form-generality: my sweep confirms 0/202 under unit, canonical
class-1/k, the menu probe, AND the receipt's arbitrary probe
Z = 1 + depth — which I verified is genuinely class-constant (depth
is a class invariant) and genuinely non-harmonic (the root equation
fails), so the sweep now exhibits exactly the theorem's scope: any
cut-attached Z, harmonic or not. The NEGATIVE CONTROL fires: the
receipt's deterministic sorted-vs-unsorted sequence-Z is a valid
instance of the non-class-constant class (118 classes carry both
Z-values), and mutant E (control neutered to a constant) prints
"sequence-Z failures = 0" and dies through the `v_seq > 0` gate,
exit 1 — the control has teeth. The separating content is credited
to class-constancy (d42b3-D2's lineage) in the check label, the pin
(B2, which also qualifies "any boundary" to cut-attached
class-constant and correctly records my 198/202 instance), and the
verdict line. One representative-dependence note (D-n2 below) on the
printed count.

## D-3 (F3) — DISCHARGED; the quotient verified against my own
## construction, partition-identical

S3 now computes the bisimulation quotient. I replicated the
receipt's algorithm (kind-free successor keys (q, state), string
relabeling, depth-4 absorbing) independently: trajectory
[4, 9, 14, 16, 17, 17], fixpoint 17 — exactly the committed detail.
Separately my round-1 KIND-AWARE construction (successor keys
(kind, q, state)) lands 17 with the IDENTICAL partition
(block-by-block equality verified) — the receipt's kind-free keys
lose nothing at this depth, because its stage-wise states carry the
shape lineage and my refinement provably refines theirs stage-wise,
so equal fixpoint counts force equal partitions. The split witness
([pA0] vs [pA0, selfA, p-on-v1]) is IN the family (the fallback
branch is dead — see D-n4) and the states differ at the fixpoint;
the wd gate holds (canonical classes sit inside bisim states, 0
straddles) and the label's literal claim is true by my direct
recomputation of the outgoing (q, target-class) multisets: 0/114
interior classes (my first delta run flagged this line, but the
defect was in MY checker — repr(frozenset) is not a canonical key;
with stable class ids the receipt's claim verifies cleanly). The
one-way wording (stationary ⊂ positive-harmonic; the residue
CONTAINS front 7) is in the pin (B3), the check label, and the
verdict line; the rank/313 stays a referee anchor cited in the pin —
consistent with the d42b3 precedent (its 313 was likewise
review-carried). Existence remains declared OPEN, no claim either
way.

## D-4 (F4/F6) — DISCHARGED

The multiset proxy is replaced by the STRUCTURAL event-level
bijection: root menu -> H3 menu under v0 -> v1 translation with
equal q at every matched event plus size equality — re-verified in
both directions with my own map; no r-events exist in either menu,
so the translate r-passthrough is unreachable. The 331-share
disclosure is printed (my census: 331 exact), and the pin's B4
records the full 331/175/31 weakness census. Mutant F (translation
broken to identity) dies exit 1 — by IndexError at the q-lookup
before the S2 check line rather than through a clean [FAIL]:
fail-safe, never false-green. Citations switched to paper 28 §5.3 +
the D42 mandate; the sprinkling precursor's scope is named (internal
Z2 x Z2 + foliation gauge, not spacetime symmetry) in pin and
verdict. pv1 is now translate(pA0), the sigma-partner by
construction — the round-1 positional-grab robustness concern is
structurally closed.

## D-5 (F5) — largely discharged; the pre-flagged vestige EXISTS

`kcount` is gone. The coordinator's pre-flag is confirmed: **lines
144-147 carry a dead v1n DOUBLE-ASSIGN plus a dead `v1_pair`** — the
first v1n binding computes vname over `{tA,tB} & {tA}` (= {tA}, the
same value) and is immediately overwritten; all three bindings are
unused. The A6 identity they were meant to carry — that the menu-read
fresh base equals the arb-created name — is factually TRUE (I
re-verified v1_real == vname(V0,{tA},'A')) but remains UNWIRED: one
line (`assert v1_real == v1n`) wires it and two deletions close the
vestige. Also still present: the unused top-level `permutations`
import (line 9; `lin_ext_count` uses its own local import) and the
dead `max(c, 1)` guard (the identity order is always a valid linear
extension). Non-blocking.

## Delta notes (nit grade, recorded for the terminal state)

- **D-n1.** The v1n/v1_pair vestige above — one wire-in line + two
  deletions whenever the file is next touched.
- **D-n2.** The control count 51 is REPRESENTATIVE-DEPENDENT: the
  control Z breaks gauge-invariance by design, so per-diamond
  verdicts depend on which class representative is evaluated. My
  independent enumeration (BFS-suffix representatives) gives 57;
  replicating the receipt's exact enumeration (DFS family order,
  i1<i2 first-seen dedupe) gives exactly 51, seed-stable both ways.
  Unlike the 36 (a class-invariant census), "51" is a property of
  the receipt's evaluated representatives — one clause in the detail
  ("of the evaluated representatives") would prevent misreading; the
  `> 0` gate itself is enumeration-robust and honest.
- **D-n3.** Latent seed hazard, structurally unreachable here: the
  control's `sorted(k, key=repr)` reprs r-events, whose frozensets
  iterate in hash order. It cannot fire at depth <= 4 because
  diamond-evaluated tuples never contain two SAME-INITIATOR
  r-events (per-actor per-base live-proposal uniqueness), so every
  r-vs-r comparison resolves at the initiator character before any
  frozenset — confirmed empirically by the 8-seed byte-identity. If
  the control is ever lifted to deeper families, key it canonically.
- **D-n4.** The split gate's `else True` fallback has inverted
  polarity (witness-not-found would PASS vacuously); the branch is
  dead — I verified the witness IS in the family — but on any future
  edit it should read False.
- **D-n5.** LOG #319 and pin amendments B1-B4 are faithful to the
  round-1 report (numbers, censuses, and attributions all match,
  including my 198/202 instance and the 331/175/31 census).

## Disposition

DELTA-CLEAN. All three MAJORs are discharged with independent
recomputation landing every anchor (325/64; 21/325 vs 1/16; 0/202
across four Z regimes; a firing control with teeth; trajectory
4->9->14->16->17 with partition-identical fixpoints; 0/114; 331);
the two minors are resolved (structural bijection; dead code
removed) up to the pre-flagged vestige and nit notes above, none of
which touches a gated number. The mutant battery kills all three
designed escapes, including the round-1 silent-boundary-collapse
class. On this record d42b56 is TERMINAL-supportable: the ladder
stands as a stated telescoping theorem with class-constancy as the
separating content, the renewal exhibit is structural and
non-stationarity canonical-boundary-anchored, front 7 reduces
one-way onto the 17-state quotient into the ONE infinite-volume
positive-harmonic residue (OPEN, as declared), and the continuum
shadows remain scope-honest declarations with exact discrete
covariance gates. Zero false numbers, nine rounds — the campaign's
receipt phase closes clean.

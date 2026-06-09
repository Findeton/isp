# YM video — Production pack (companion to `youtube-ym-confinement-script.md`)

Two deliverables:
- **PART A — Verbatim voiceover** for the three content-heavy chapters (3, 8, 11), recording-ready, at
  ~150 wpm with running timestamps. Read straight through; `[ ]` markers are *not* spoken.
- **PART B — Animator shot list** for the three keeper frames (#1 the wall, #2 the loop equation,
  #3 the bootstrap bracket), with per-shot timings, motion, overlays, and VO sync cues.

Honesty + motif rules carry over from the main script (✅/🟡/🔶 tags; rubber band = emotional motif;
"the loop" = technical motif; never imply we proved confinement/the mass gap).

---

# PART A — VERBATIM VOICEOVER

## CH 3 (verbatim) — What Yang–Mills actually is (~7.5 min, ~1,150 words)

> **[10:30]** Let's meet the theory. And the good news for you, the engineer in the audience, is that
> you already know a gauge theory — you just might not call it that. It's electromagnetism. So we're
> going to build Yang–Mills out of electromagnetism by changing exactly *one* thing. Watch which thing.
>
> Here's electromagnetism in the geometric language that upgrades cleanly. Imagine that at every point
> in space there's a little dial — think of it as the hand of a clock, an angle. The laws of physics
> don't care where you put the "twelve o'clock," the zero, on that dial. And here's the strong part:
> you're allowed to choose that zero *independently at every single point*. Re-zero the dial here one
> way, over there another way — physics doesn't blink. That freedom, that "you can't pin down the zero,"
> is what we call **gauge symmetry**. [VISUAL: a field of little clock-dials, each re-zeroing freely.]
>
> But now there's a problem, and the electromagnetic field is its solution. If the zero is arbitrary at
> each point, how do you *compare* the dial here with the dial one step over? You need a rule — a
> bookkeeping device — that tells you how to carry the dial from one point to its neighbor so you can
> line them up. That rule *is* the electromagnetic field. Mathematicians call it a **connection**: a
> recipe for parallel transport. [If you've studied general relativity, this is the exact same job a
> Christoffel symbol does for ordinary vectors — but you don't need that to follow me.] [VISUAL:
> carrying a clock-hand along a path, rotating as it goes.]
>
> Now the punchline of electromagnetism, and please *burn this picture into your memory*, because it's
> the star of the whole second half of this video. Take your dial and carry it all the way **around a
> small loop**, back to where it started. Does it come back pointing the same way? In general — no. It
> comes back rotated by some amount. And that failure to return, that little leftover twist after going
> around a loop, *is the electric and magnetic field.* The field is the **curvature** of the connection.
> A loop, and how much an arrow fails to return after going around it. [VISUAL: arrow goes around a loop,
> returns rotated; freeze-frame, label it "★ the loop — remember me."] That loop is going to come back
> with a name — the Wilson loop — and *everything* at the frontier of this problem is a statement about
> it.
>
> Okay. That's electromagnetism. Now the one change, due to Yang and Mills in 1954. [beat]
>
> In electromagnetism the thing at each point was a *single dial* — one angle, a one-dimensional thing.
> The gauge freedom was just "rotate the dial." Yang and Mills asked: what if, instead of a single dial,
> there's a little **arrow living in a higher-dimensional internal space** — and the gauge freedom is
> *rotating that arrow*? For the real strong force the arrow lives in a three-dimensional internal space,
> and physicists gave its three directions a playful name: **colors** — red, green, blue. Nothing to do
> with real color; it's just a label for the three internal directions. The rotations that mix them are
> 3×3 unitary matrices, the group called SU(3). To keep the pictures simple I'll often use the baby
> version, SU(2) — rotations of a 2-component arrow. [VISUAL: the single dial morphs into a little 3-D
> arrow being spun by a matrix.]
>
> The geometry is *identical*. There's still a connection — but now, instead of a single number telling
> you how the dial turns, it's a **matrix** telling you how the internal arrow rotates as you step across.
> There's still curvature — carry the arrow around a loop, see how it fails to return. There's still an
> action, the quantity nature minimizes. [ON SCREEN: EM and YM actions side by side, parallel.]
>
> But here is the one change, and it changes *everything*. In electromagnetism, the order didn't matter.
> With rotations in more than one dimension, **order matters**. Watch. [VISUAL: presenter or animation
> rotates a book 90° about two different axes in one order, then the other order — the book ends up in
> *different* orientations.] Rotate this way then that way, versus that way then this way — you get
> different answers. Rotations don't commute. And when you work out the curvature for something that
> doesn't commute, it picks up an extra piece. The field strength F is no longer just "the change in A" —
> it's the change in A, *plus A times A.* [ON SCREEN: F = dA + **A∧A**, the A∧A pulsing.]
>
> That little "A times A" term is the whole ballgame. It means **the field is charged under itself.**
> In English: gluons — the carriers of the strong force — pull on *other gluons.* And cash that out right
> now, because it is literally why we're all here. That one nonlinear term is why the strong force is
> *strong*; it's why it's *short-ranged*; and it's why this is a million-dollar problem and not a
> homework exercise. Compare: light doesn't shine on light. Two flashlight beams pass right through each
> other — photons ignore each other — so electromagnetism stays tame and solvable. But gluons shine on
> gluons. The force feeds back on itself, that feedback runs away, and *the entire difficulty of the
> strong force lives in those two extra symbols.*
>
> So if we have the equations — and we do, that's the action right there — why isn't it solved? Because
> that self-interaction turns the theory into a violently coupled, infinitely-many-dimensional integral
> with **no small knob to turn** — no little parameter you can expand in. [beat] Almost. Because there
> *is* exactly one place a small knob exists, and it's the reason we believe any of this. That's the
> next chapter.

**[~18:00 out]**

---

## CH 8 (verbatim) — The exact loop equation (~7 min, ~1,070 words)

> **[35:00]** We need something *exact* — a handle on the theory that's true at every coupling at once,
> so it still works at the wall, where every expansion died. It exists. And the beautiful thing is, you
> can reach it with nothing fancier than integration by parts. Let me show you.
>
> Start with a fact you already trust completely. **The integral of a total derivative is zero** — up to
> boundary terms. It's the fundamental theorem of calculus; it's the divergence theorem; it's integration
> by parts with the boundary thrown away. If a function is the derivative of something, and that something
> behaves at the edges, the integral vanishes. You've used this a thousand times. [ON SCREEN: ∫ d/dx[f] dx
> = 0, "the average of a total derivative is zero."]
>
> Now apply that exact same principle to the giant averaging integral that *defines* the quantum theory.
> Remember from a few chapters ago: a quantum average is an integral over *all possible field
> configurations*, each weighted by e-to-the-minus-action — structurally a Boltzmann average. Here's the
> trick, and it has a fancy name, the Schwinger–Dyson identity, but it is *just* "the average of a total
> derivative is zero." We take one little link of the field — one of those rotation matrices — and we
> *shift* it infinitesimally, the way you'd shift a variable to integrate by parts. The key fact is that
> the natural measure on rotations — the Haar measure — doesn't change when you do that shift; it's
> symmetric. So the average of the corresponding derivative *must* vanish. We set it to zero and read off
> what falls out. [VISUAL: a Wilson loop on the grid — our old friend ★ the loop — with one link pulsing
> as we "wiggle" it.]
>
> What's the thing we wiggle inside of? The Wilson loop — the loop from chapter three, grown up. On the
> lattice it's the product of all the rotation matrices around a closed loop, traced and averaged. Its
> whole job, recall, is confinement: if the Wilson loop dies off like e-to-the-minus the *area* it
> encloses, you have confinement, and that string tension is our rubber band.
>
> So we wiggle one link of the loop, we use one standard piece of algebra about how these rotations
> contract — the completeness, or Fierz, relation — and out comes this. [REVEAL the boxed equation,
> large, and hold.] This is the **Makeenko–Migdal loop equation**, the heart of the modern approach.
> Don't read the symbols yet. Read the *story*, which has exactly two sides.
>
> **Left side: deform the loop.** When you wiggled that link, the loop changed shape — it grew by one
> little tile. So the left side is: *take the loop and push it out by one plaquette at that point.* It's
> a derivative in the space of loop *shapes* — how the Wilson loop responds when you wiggle its outline.
> And it carries the coupling, that factor beta, which is just one-over-g-squared. [VISUAL: the left side
> — a single tile inflating off the loop, growing it.]
>
> **Right side: split the loop.** Here's the magic. Whenever the loop *crosses itself* — passes through
> that same point twice — the algebra makes it **pinch apart into two smaller loops.** One loop becomes
> the *product* of two daughter loops. [VISUAL: a figure-eight loop; the crossing point pinches; it
> separates into two independent loops.]
>
> So the entire content of this exact law, in one sentence: **wiggling a loop equals the loop splitting
> wherever it touches itself.** That's it. That's the equation. [ON SCREEN super: "wiggle = split."]
>
> Now — why do we care so much? Because of *what kind* of statement this is. We did **no** Taylor
> series. We never assumed the coupling was small, and we never assumed it was large. We just integrated
> by parts. So this equation is true at coupling 0.1, at coupling 1, at coupling 10 — it is exact *at
> every coupling at once*, **including at the wall.** [VISUAL: the EXACT-vs-EXPANSION tally — the EXACT
> column, empty this whole film, finally gets a green check.] After an hour of tools that only worked on
> one side or the other, this is the first one that works *in the middle*, where the physics actually
> lives. This is the third tool we went hunting for.
>
> So are we done? Do we just solve it? [beat] No — and the reason is as beautiful as it is maddening. Look
> again at the two sides. To know your loop, the left side needs a *bigger* loop — you grew it. And the
> right side needs *products of* loops — you split it. So the equation for one loop refers to bigger loops
> and to pairs of loops. Write down *their* equations, and they refer to bigger-and-more loops still. It
> never stops. [VISUAL: one loop spawning a downward, ever-branching tree of bigger and split loops.] It's
> an infinite tower of exact equations — infinitely many unknowns.
>
> There *is* one famous escape hatch, and it tells you exactly how hard the real problem is. Imagine a
> make-believe world with a *huge* number of colors — not three, but infinity — the so-called large-N
> limit. In that world the splitting term simplifies: the average of a product of two loops becomes just
> the product of their averages, and the whole infinite tower miraculously *closes* into a single,
> solvable equation. That is precisely how the two-dimensional version of this theory was cracked, cleanly.
> But step back to the real world — three colors, four dimensions — and the hatch slams shut. The tower
> stays open. We have the perfect law... and, as it stands, no way to solve it.
>
> The fix for "exact, but won't close" is the most exciting idea in mathematical physics this decade.
> That's next.

**[~42:00 out]**

---

## CH 11 (verbatim) — The ℝ³×S¹ affine-theta cusp (~5 min, ~790 words)

> **[53:00]** There's a second road to the frontier, completely different from the bootstrap, and its
> charm is that *everything becomes computable* — at a price we'll have to pay back at the end.
>
> The idea is the most engineering move imaginable: **if a knob is too big to handle, make it small.**
> Take one of the four dimensions of spacetime and *curl it up into a tiny circle*, of circumference L.
> Spacetime becomes ordinary 3-D space times a little loop. Why on earth does that help? Because of
> asymptotic freedom from earlier: a *small* circle means you're probing *short* distances, and short
> distances mean *weak* coupling. By shrinking the circle, you have deliberately forced the theory into
> the one regime you can actually calculate in. [VISUAL — HERO SHOT: the 4th dimension curling into a
> shrinking circle while the running-coupling curve slides left into the green, computable zone.]
>
> Now, beautiful things happen on that small circle — *as long as we keep one symmetry alive.* And this
> is the subtle, honest part. Left completely to itself, the small-circle theory actually does the *wrong*
> thing: it comes apart, it *deconfines.* So we add a mild extra term that stabilizes a symmetry called
> center symmetry — or, equivalently, we study a supersymmetric cousin of the theory where it happens for
> free. That keeps the *confining* arrangement as the favored one. And hold onto this, because keeping
> that symmetry is *exactly* what will make our final question sharp instead of hopeless. [VISUAL: a
> "clamp" labeled *center stabilizer* snapping the configuration into the confining slot.]
>
> With that in place, here's the payoff. The way the field wraps around the little circle settles at a
> value that breaks the complicated non-abelian theory down to plain **3-D electromagnetism** — and
> 3-D electromagnetism with monopoles is the one case where confinement was *proven*, by Polyakov,
> decades ago. The genuinely non-trivial objects are little lumps called **monopole-instantons**; for our
> baby theory they come in two flavors, and their magnetic charges live on a beautiful lattice called the
> *affine root lattice.* Add up the gas of these lumps and the photon of that 3-D theory gets a mass —
> confinement — with a string tension you can write in *closed form*: it's e-to-the-minus-four-pi-squared-
> over-g-squared. That exponential, the fingerprint of genuinely nonperturbative physics, is now
> *derived*, not assumed. [ON SCREEN: the dual-photon Lagrangian and the fugacity ζ ~ e^{−4π²/g²(L)}.]
>
> And now the new lens — and let me be precise about credit. The semiclassical machinery I just described
> is established: Polyakov, Ünsal and Yaffe, Dunne and Ünsal. What *our* papers add is this observation:
> that monopole sum, living on an affine lattice, is a **theta function** — the same kind of object with
> a hidden inside-out symmetry we met one chapter ago, in Poisson summation. And the *confinement scale*
> turns out to be its leading **cusp** term — the very first coefficient as the circle shrinks. [ON
> SCREEN: √σ_st / Λ = c · [leading cusp of Θ_aff].] Confinement becomes a *calculable cusp statement.*
> Even the famous electric–magnetic duality is, literally, this theta function's inside-out symmetry.
>
> So what's left? The honest open core. [🔶 on screen.] Everything I just said lives at *small* circle.
> The real world is the *large* circle — uncurl it back to full 4-D. The bridge is called **adiabatic
> continuity**: the claim that, *because* we kept that center symmetry alive, we can grow the circle all
> the way to infinity *without* the theory ever undergoing a phase transition — so the confinement we
> *computed* connects smoothly to the confinement we *want.* It's strongly supported — by lattice data,
> and by the supersymmetric cousins — but it is **not proven.** The tool for controlling it is a deep
> rigidity called resurgence. [VISUAL: slider "L: small (calculable) ⟷ large (real world)" with a glowing
> 🔶 gap in the middle, labeled "adiabatic continuity — open."]
>
> So this road, too, takes us to a single, sharp, unsolved question — *does it survive uncurling?* —
> instead of the bare, hopeless 4-D problem. Let's surface and take honest stock of where that leaves us.

**[~58:00 out]**

---

# PART B — ANIMATOR SHOT LIST (the three keeper frames)

**Global style (applies to all three):**
- Palette: deep navy background; weak-coupling = **green**, strong-coupling = **blue**, the wall / danger
  / open = **red/amber**; "exact/proved" = green ✅; "open" = amber 🔶.
- Persistent corner HUD: the **depth gauge** (current notch + question) and, from ch.6 on, the small
  **EXACT | EXPANSION tally**. Keep them in the lower-right, ~8% screen height, never moving.
- Line weight consistent; loops drawn in a warm off-white ("★ the loop" identity color) everywhere they
  appear (ch.3 → 7 → 8 → 9) so the viewer subconsciously tracks the same character.
- Type: one sans family; formulas appear *after* the spoken English, never before.

---

## KEEPER #1 — "THE WALL" (Chapter 6) — total 22 s

Sync: plays under the VO "...picture two zones of control... with a no-man's-land between... the wall
sits in that gap... (teaching picture, not a literal map)."

| # | t (s) | On screen | Motion | Overlay text | VO sync |
|---|---|---|---|---|---|
| 1.1 | 0.0–3.0 | One horizontal axis appears, centered | Axis draws L→R; ticks fade in | left end "weak coupling", right end "strong coupling" | "two zones of control…" |
| 1.2 | 3.0–7.0 | Green disc grows from the **left** end | Disc inflates; inside it a row of bars that visibly *shrink* | "weak-coupling expansion (Feynman) ✓ here" | "one anchored at zero coupling…" |
| 1.3 | 7.0–11.0 | Blue disc grows from the **right** end | mirror of 1.2; bars shrink inward | "strong-coupling / lattice expansion ✓ here" | "one at infinite coupling…" |
| 1.4 | 11.0–15.0 | The two discs stop short; a **red gap** glows between them | gap pulses once | — | "with a no-man's-land between them" |
| 1.5 | 15.0–19.0 | A brick **WALL** drops into the gap | wall falls, small dust; slight screen shake | on the wall: "g_eff ~ 1 — confinement generated here" | "the wall sits in that gap" |
| 1.6 | 19.0–22.0 | Banner spans the gap; everything else dims | banner fades up; hold | "no expansion reaches this — ← the whole problem" + tiny watermark "intuition, not literal" | "(teaching picture, not a literal map)" |

Notes: **single axis only** — do NOT render 2-D complex-plane discs (would overclaim the math). The dust
on the wall-drop is the emotional beat; let it land before the banner.

---

## KEEPER #2 — "DEFORM = SPLIT" / the loop equation (Chapter 8) — total 36 s

Sync: under "...we wiggle one link... out comes this [equation]... left side: deform... right side:
split... wiggling a loop equals the loop splitting wherever it touches itself."

| # | t (s) | On screen | Motion | Overlay text | VO sync |
|---|---|---|---|---|---|
| 2.1 | 0.0–4.0 | Off-white closed loop `C` on a faint grid (callback color) | one link `ℓ` begins to **pulse** | "★ the loop (remember me?)" briefly | "a Wilson loop… one link pulsing" |
| 2.2 | 4.0–7.0 | Camera pushes in on link `ℓ` | gentle zoom | "wiggle this link" | "we wiggle one link…" |
| 2.3 | 7.0–9.0 | Equation **box** fades in, empty/dim, center-top | box outline draws | (empty box) | "out comes this" |
| 2.4 | 9.0–16.0 | **LEFT half:** at `ℓ`, a single square tile inflates outward, growing `C` into a bigger loop; ghost the opposite-orientation tile | tile blooms; bigger loop ghosts in | "DEFORM — grow by a tile — (×β = 1/g²)" | "left side: deform the loop…" |
| 2.5 | 16.0–17.0 | LEFT half of the boxed equation lights under the deform picture | term highlights | `β Σ_p [W(C∪∂p) − W(C∪∂p̄)]` | "…carries the coupling β" |
| 2.6 | 17.0–25.0 | **RIGHT half:** redraw `C` as a figure-eight touching itself at `ℓ`; the crossing **pinches**; it separates into two independent loops `C₁`, `C₂` | pinch + split; the two loops drift apart | "SPLIT — self-touch → two loops → W(C₁)·W(C₂)" | "right side: split the loop…" |
| 2.7 | 25.0–26.0 | RIGHT half of the boxed equation lights | term highlights | `= Σ_crossings [W(C₁)W(C₂) − (1/N)W(C)]` | "…pinch apart into two" |
| 2.8 | 26.0–30.0 | Full equation solid; one-line super sweeps in under it | super wipes L→R | **"wiggle = split — exact, at every coupling"** | "wiggling a loop equals the loop splitting…" |
| 2.9 | 30.0–33.0 | Cut to the **tally**; EXACT column gets its first ✅ with a chime | ✅ stamps; soft chime | EXACT: ✅ "loop equations (all g)" | "the EXACT column… finally gets a check" |
| 2.10 | 33.0–36.0 | Pull back: the deformed loop + the two split loops each sprout their **own** little equations → a downward branching tree begins, and keeps growing as we cut away | tree branches, no end | "…but it never closes" | "an infinite tower… no way, yet, to solve it" |

Notes: shots 2.4 and 2.6 are the heart of the film — give them the most polish. Keep `C` in the loop
identity color throughout so it reads as the same character from ch.3.

---

## KEEPER #3 — "THE BRACKET" / the bootstrap (Chapter 9) — total 28 s

Sync: under "...impose the loop equations as exact rails… positivity clamps… as you add loops the
bracket squeezes… on a solvable case it collapses to the known answer."

| # | t (s) | On screen | Motion | Overlay text | VO sync |
|---|---|---|---|---|---|
| 3.1 | 0.0–4.0 | A vertical number line for **σ**; the true value hidden behind a curtain/blur band | line draws; curtain shimmers | "σ = string tension (true value: unknown)" | "…find the largest and smallest possible σ" |
| 3.2 | 4.0–9.0 | **Loop equations** drop in as rigid horizontal **rails**; **positivity** snaps in as green "⪰ 0" **clamps** | rails lock; clamps snap with a click | "exact rails (loop eqs) + positivity clamps (⪰0)" | "the loop equations as equalities… positivity…" |
| 3.3 | 9.0–12.0 | An **upper-bound** bar and a **lower-bound** bar appear, far apart, bracketing the hidden σ | bars fade in wide | "rigorous bracket: true σ is in here" | "…a rigorous bracket on σ" |
| 3.4 | 12.0–19.0 | A counter `L_max: 4 → 8 → 16 → 32` ticks; with each tick the two bars **squeeze inward** | bars step inward per tick; counter rolls | "add more loops ⇒ bracket tightens" | "as you include more and bigger loops…" |
| 3.5 | 19.0–24.0 | Scene label "solvable check: 2-D"; the band **collapses to a point** landing on a marked value | bars meet at a point; snap | "2-D: bracket → σ = 3/2β ✅ (known answer)" | "…on a solvable case… matches the known answer" |
| 3.6 | 24.0–28.0 | ✅ "validated" stamp; tally gets its 2nd EXACT ✅ ("positivity / bootstrap") | stamp; tally update | "the machine works where we can check it" | "the machine works." |

Notes: the "squeeze" (3.4) should feel mechanical and satisfying (like a clamp/vice), reinforcing
"constrain, don't expand." Reuse the loop identity color for the little loops feeding the counter.

---

## Hand-off checklist for the animator
- 4 hero assets to build well: **rubber-band-snap** (ch.1, not in this pack — see main script), **#1 wall**,
  **#2 deform=split**, **#3 bracket**. Everything else can be simple lower-thirds + formula cards.
- Persistent HUD assets: depth gauge (12 states) + EXACT|EXPANSION tally (fills across ch.4→6→8→9).
- Formula cards (one per on-screen equation) come from the main script's ON SCREEN blocks; render each
  *after* its spoken English.
- Colour-lock "the loop" (warm off-white) across ch.3/7/8/9 — it's a character, treat it like one.

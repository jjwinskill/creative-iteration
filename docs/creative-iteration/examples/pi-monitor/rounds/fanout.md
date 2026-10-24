# Fan-out
Draw (stage `fanout`, excluding the three problem-stage moves): 13 moves, 4 constraints, 1 seed. Assigned in draw order.
- **g1:** rev-edhi-cradle, tanda-take-turns-with-the-pot, eco-canyon-trickle; constraint con-smell-and-touch-only ("It may communicate only through smell and touch, with nothing seen or heard.")
- **g2:** sci-ball-change-the-form, art-eno-seed-and-let-run, rev-arpilleras; constraint four-hours ("The first working version has to exist within four hours.")
- **g3:** infra-taktfahrplan, book-change-what-gets-honoured, book-stay-awake-let-it-commit; constraint con-ages-gracefully ("It must look better after ten years of wear than on its first day.") **Surprise rule:** g3 (by `--pick g1,g2,g3,g4`) was told none of its six may be the obvious kind of thing (a retro arcade or game console with a control panel).
- **g4:** play-rock-paper-scissors, hitchcock-bomb-under-table, ops-who-time-out; constraint con-works-underwater-or-in-rain ("It must work while soaked in heavy rain, or fully underwater.")
- **Wild card:** art-borges-review-the-imaginary; seed "Sonia Ouchene" (a footballer's Wikipedia stub); tension T12 (by `--pick T1..T12`); pool entries 11, 21, 48, 67, 73.
- **Control:** no cards, slice only.
- **Bonus rule:** not used; the intake marks nothing as a bonus.

## Unprompted lists (each agent's 3–4 before its slice, with typicality guesses)
| Agent | Candidates (guess %) |
|---|---|
| g1 | smart mirror / info wall (70), retro arcade / RetroPie (60), digital photo frame or art display (55), media center or second desk monitor, Kodi/Plex (40) |
| g2 | retro arcade, RetroPie + soldered panel (70), smart mirror / MagicMirror (55), Home Assistant or family wall dashboard (50), digital photo frame or Kodi/Plex box (35) |
| g3 | retro arcade / RetroPie console with soldered panel (70), smart mirror or home dashboard (60), Kodi/Plex media centre (40), digital photo frame (30) |
| g4 | retro arcade with RetroPie and soldered panel (85), magic mirror or smart-home/family dashboard (80), digital photo frame or family slideshow (60), Kodi media center or security-camera wall (40) |
| control | retro arcade / RetroPie (60), smart mirror or info dashboard (55), digital photo/art frame (40), media center (Kodi) or Pi-hole with status screen (30) |

All five agents named the same four answers. None of them used one.

## Sketches (filter scores; blind labels from `deal.py --pool 33 --hands A:1 … AG:1`)
Distance 1–5 from the obvious answer. Feasibility fine / risky / dead. Fit yes / partly / no. Forced = bends its precedent.

| Label | Source | Pool # | Sketch (one line) | Group | Dist | Feasible | Fit | Forced | Well |
|---|---|---|---|---|---|---|---|---|---|
| B | g1 (canyon) | 39 | Erosion alarm: gutted monitor shell as a headboard; heat film + citrus scent creep up over 30 min to wake you | B | 5 | risky: unattended 12V heat film in a bed; scent refills | partly | no | |
| Z | g1 (tanda) | 55 | Evening card stage: housemates take turns slotting a scented, textured card; the shell releases scent and warmth | I | 5 | risky: scent hardware, consumables | partly | yes | |
| I | g1 (Edhi) | 12 | Seven-hour line: the Bergen–Oslo route as a workday sequence of scents from the shell behind the desk; terminus ends work | I | 5 | risky: five scents, nose fatigue, refills | partly | yes | |
| W | g1 (canyon) | 18 | Petting lawn: monitor shell as a wall planter of living turf behind cloth, Pi drips water | W | 5 | **dead**: turf needs light, water, cutting | no | yes | |
| AB | g1 (tanda) | 50 | Scent keyboard: eight soldered keys over scent chambers; one scent a week | I | 5 | risky: purging, refills | partly | yes | |
| AG | g1 (Edhi) | 35 | Hush line: a distant person's button press makes the panel pulse warm and exhale a scent | I | 5 | risky: needs a tunnel and a willing sender | partly | yes | |
| M | g2 (Eno) | 19 | Unequal Window: your own slow footage as a living-room window, audio loops of 17 and 23 min | M | 4 | fine: software only | partly | no | **well** |
| V | g2 (arpilleras) | 72 | Patchwork Booth: cigar-box button records 60-s spoken stories; each becomes a quilt patch on the monitor | V | 4 | fine | partly | no | |
| T | g2 (Ball) | 59 | Glow Box: the panel as a backlit evening stage for translucent silhouettes (gel or lithophane), glow follows sunset | S | 4 | fine | partly | no | |
| AA | g2 (Ball) | 51 | Home Machine: instant-on writing computer, no network, dated autosave; hand-wired keyboard is the soldering | K | 4 | fine: continuity-testable matrix | yes, if they write | no | |
| P | g2 (arpilleras) | 44 | Station Map Radio: map of twelve cities, twelve soldered buttons tune each city's live radio | P | 3 | fine: stream URLs need upkeep; speakers | yes | no | |
| C | g2 (Eno) | 86 | Friday Machine: monitor sleeps all week; Friday a 3-minute self-assembling, self-destroying animated machine | C | 4 | fine: software only | partly | no | |
| J | g3 (Taktfahrplan) | 3 | Wall Wash: monitor face-in off the wall in oak, washes the wall in a dawn-to-dusk colour curve | J | 4 | fine | partly | yes | |
| N | g3 (Russell) | 64 | Token Juke: walnut cabinet, drop a printed RFID album token and the Pi plays the whole album, lyrics on the monitor | N | 3 | fine: RC522 module; speakers | yes | no | **well** |
| S | g3 (Russell) | 62 | Lantern Theatre: monitor as lantern behind vellum in a wooden proscenium; backdrops by rotary switch, rod figures | S | 4 | risky: craft and design | partly | no | |
| O | g3 (Beowulf) | 83 | Bench Scope: monitor over the bench; Pi runs a USB logic analyser, sound-card scope and microscope camera | O | 5 | risky: clamp needs know-how; sound card can't see DC | partly | no | |
| L | g3 (Beowulf) | 26 | Room Echo: black framed monitor; each room sound leaves a slowly fading mark; nothing recorded | L | 4 | fine | partly | yes | |
| K | g3 (Taktfahrplan) | 31 | Dated Page: all-in-one desk writing terminal on a wood base, boots into today's dated file | K | 4 | fine | yes, if they write | no | |
| G | g4 (WHO) | 14 | Bird Café Window: sealed Pi camera at a feeder, indoor monitor as a live bird café | G | 4 | risky: outdoor power and sealing | partly | no | |
| A | g4 (RPS) | 54 | Dinner Duel: sealed reed-switch pucks; nightly the monitor duels dinner or movie options and settles it | A | 4 | fine | partly: needs a household | no | |
| Y | g4 (Hitchcock) | 68 | Karaoke Cliff Warning: MIDI karaoke that shows each song's hardest leap before it starts | Y | 3 | fine | partly | no | |
| AE | g4 (Hitchcock) | 85 | Bead Rain: eight servos lower beads in front of the glowing monitor into a faintly pre-shown shape | AE | 4 | risky: tangles, wear | partly | no | |
| AC | g4 (WHO) | 29 | Teletext Art Set: 40×25 teletext mosaic art pages, flipped by sealed reed pads and a magnet fob | AC | 3 | fine | partly: art supply runs out | no | **well** |
| F | g4 (RPS) | 65 | Jam Partner: guitar into USB audio; Pi backing band, huge chord ribbon, reed-switch stomp box | F | 4 | risky: chord/habit detection fiddly | yes, if they play | no | |
| D | control | 80 | Solder-along table: monitor face-up under acrylic shows the layout at true scale, lights the next pad, flags expected voltages | D | 5 | fine: layout file per project | partly: used while building | no | |
| AD | control | 84 | Louvered colour wall: printed angled fins over the monitor, colours shift as you walk past | J | 4 | risky: many big prints | partly | no | |
| R | control | 17 | Dawn lamp: bedroom monitor plays a five-hour near-still sunrise ending at your alarm | B | 4 | fine | yes | yes | |
| Q | control | 22 | Self-watching figure: a printed figure watches its live image, TV-Buddha style | Q | 4 | fine | **no** | no | |
| AF | control | 23 | Monochord: one string along the monitor's edge; the mic hears it and the Pi draws the vibration huge | AF | 4 | fine | partly | no | |
| E | control | 57 | Pull-card story theatre: portrait monitor in a kamishibai frame; pulling a card plays the next picture and narration | E | 3 | risky: frame bigger than the bed | partly | yes | |
| U | wild | 21 (×73) | Sky for a Pothos: monitor face-down over a shelf as a sky for a plant; dry soil clouds it over | U | 5 | risky: needs an ADC; screen light is weak | partly | yes | |
| X | cold A | — | Couch arcade: RetroPie + soldered button-and-joystick panel | X | 1 | fine | partly | no | **well** |
| H | cold B | — | A generic Pi appliance: one service, printed bracket, one perfboard of buttons and LEDs | X | 2 | fine | **no**: no use named | no | |

Filter judge's notes: groups X = X, H; B = B, R; I = I, Z, AB, AG; K = K, AA; S = S, T; J = J, AD. D and O are not grouped but are both bench aids aimed at the debugging gap. Audio ideas (F, N, P, Y) assume speakers, which aren't on hand.

**Wild card's answer (what it reveals):** it dissolves T12 by asking whom the screen is for rather than whether it's the star. It surfaces a tension that isn't on the register: the why-test says "used", and "used" can mean attention (which wears off) or presence (on, and nobody minds). A living part contradicts "complete as is". It suggests moving the what from something to look at toward something that runs in the room. Added to the register as **T13: used means looked at vs. used means present and running.**

## Wells this run
| Well | Why (ledger / 3+ unprompted lists / both cold) |
|---|---|
| Retro arcade / RetroPie with a soldered control panel | 5 of 5 unprompted lists; cold A. (Cold B is the same build shape with no content.) |
| Smart mirror / MagicMirror / info or family dashboard | 5 of 5 unprompted lists (already on the person's no list) |
| Digital photo frame / art display / slideshow | 5 of 5 unprompted lists. Sketches matching it: M (Unequal Window: your own footage as a window), AC (Teletext Art Set: art pages on the screen) |
| Media centre (Kodi/Plex) | 5 of 5 unprompted lists. Sketch matching it: N (Token Juke: a box that plays your albums) |

The ledger had no wells for this kind of brief.

## Menu ordering (mechanical)
Dropped: W (dead), Q and H (no fit). Reference: X. Group representatives were chosen by the same ordering; the ties K/AA and I/Z/AB/AG were broken by `draw.py --pick` (AA, I). Order: distance, then clean before forced at equal distance, then fine before risky, then yes before partly. The five-way tie at distance 4, clean, fine, partly (A, C, T, V, AF) was ordered by `deal.py --pool 5` → T, A, AF, V, C. Wells go to the convergent lane, not the main list.

Main list after ordering: D, B, O, I, U, AA, T, A | then AF, V, C, F, G, AD, AE, R, L, P, Y, E.
Wild slots: everything at distance 5 already made the main list, so the slots take the next two feasible ideas at the highest remaining distance (4), fine and clean first: AF, V.
Convergent lane: N and M (the strongest wells: N is fine and full fit; M is distance 4 and fine; AC is held back).

## Menu (shown at Gate 1)
Grounding dropped M (wrong precedent) from the convergent lane; the next well, AC, took its place. O shows as unverified.
1. Solder-along table (D), distance 5
2. Erosion alarm (B), distance 5
3. Bench Scope (O), distance 5, unverified
4. Seven-hour line (I), distance 5
5. Sky for a Pothos (U), distance 5
6. Home Machine (AA), distance 4
7. Glow Box (T), distance 4
8. Dinner Duel (A), distance 4
Wild slot A: Monochord (AF), distance 4
Wild slot B: Patchwork Booth (V), distance 4
Convergent lane: Token Juke (N), well: media centre, named by all 5 generators; Teletext Art Set (AC), well: picture/art frame, named by all 5 generators
Reference: the obvious answer, a RetroPie couch arcade with a soldered button-and-joystick panel

## Gate 1 (verbatim)
Picks: Patchwork Booth (V, wild slot B), 4 = Seven-hour line (I), 1 = Solder-along table (D) · Vetoes: none · Note: the whole reply, verbatim:

"oh these are starting to get good!!!

Ok, the choices are: Patchwork Booth, 4, 1.

Something interesting - the question answer about the tagboard did seem to modulate our answers, as some of them saw that as a specific problem to be solved, rather than using that story as a basis for color. Does that make sense? I still find the answers delightful, so I'm not sure yet if that's a feature or a bug, but it does look like it pulls the agent."

Lead's count for the person's observation: the "what killed the last one" answer became problem 1 for both problem agents, and the lead's framing turned it into a principle ("hand-built parts whose faults can be found step by step with a multimeter"). Two of 31 sketches take the debugging gap as their subject (D Solder-along table, O Bench Scope), both cold answers lean on it ("continuity mode can find any fault", "build and test in stages with the multimeter"), and most feasibility notes cite multimeter-testability.

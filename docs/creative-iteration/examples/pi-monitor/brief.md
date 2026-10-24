# Pi + old monitor: what to build

## Intake (the person's answers, verbatim)
Intake and Gate 0 were done before this run (the confirmed block is in `../../brief-block.md`). The answers, verbatim:

0. Soldering: "I'm experienced enough with soldering that I've built several electronics projects, including keyboards, guitar pedals, and raspberry pi projects. I'm pretty good with standard thru-hole soldering, not with damaged pcb repair or surface-mounted components."
1. Role (what will you be doing with it day to day; is the build half the point?): "Using it, likely not tinkering it unless it's something that would take some kind of extensions, but the project itself should be considered "complete" as is. The enjoy of the build should be considered but the end product is more important"
2. Where it lives: "Depends on what it is, but living room if related to entertainment, office of productivity, etc. So in other words no real bearing on the project we build"
3. What's on hand (asked to confirm a Raspberry Pi 4, a 24-inch monitor from about 2014 with a dead stand, jumper wires and a cheap USB microphone): "Yes that's a good assumption. I've also got a multimeter (no oscilloscope), bits of wire, breadboards, pots, diodes, resistors, and caps of various sizes. I have a Bambulab H2S 3D printer I could use for enclosures or other parts but no design experience in CAD. I've got solder and an iron, and we'll limit our budget to $100"
4. What killed the last one: "I made a ProCo Rat guitar pedal clone on tag board, and I haven't followed through with it because it didn't work off the bat and I didn't have any clear direction on how to debug using my multimeter (I'm good at soldering but still lacking some electronics fundamentals). This was around 2021 so before AI was integrated into my workflow, I feel confident that with an agent in hand it wouldn't be a problem today."
5. No list: "dashboards for smart home stuff, weather monitoring, family schedule view, fitness tracking"
6. Build time: "up to six months on the weekends, a few hours at a time"

## Brief block (exactly what agents receive; confirmed at Gate 0)
Used verbatim from `brief-block.md` (Their words, the why and why-test, the dials, Assumptions, Unknowns). The lead adds one header line above it in every prompt to state the ask: "The brief: what should this person build with a Raspberry Pi and an old 24-inch monitor?" From Stage 1 on, prompts also say the person asked to be surprised and give the obvious answer; from Stage 2 on, they carry the framing and the tension register.

**Gate 0 reply (verbatim):** "build time: up to six months on the weekends, a few hours at a time, run it gated"

## 0: the situation (held tight)
- **Who:** the person, for their own use ("me"). An experienced through-hole solderer (keyboards, guitar pedals, earlier Pi projects), thin on electronics fundamentals, no CAD.
- **What exists:** a Raspberry Pi 4; a 24-inch monitor from about 2014 with a dead stand; jumper wires; a cheap USB microphone; a multimeter (no oscilloscope); wire, breadboards, pots, diodes, resistors, assorted caps; a Bambu Lab H2S 3D printer; solder and an iron; an AI agent for code and debugging help.
- **What hurts:** the last build (a ProCo Rat clone on tag board) didn't work first time, there was no way to debug it with a multimeter, and it was abandoned. The old monitor and Pi are sitting idle.
- **Hard limits:** $100 for new parts; through-hole only (no SMD, no damaged-board repair, which includes the monitor's own electronics); 3D prints from published models or simple shapes; up to six months of weekends, a few hours at a time; the no list.
- **Unknown on purpose:** the making method. Also not stated: the monitor's inputs and resolution (a 2014 24-inch panel is probably 1080p with HDMI/DVI/VGA, but that's the lead's guess, not a fact, and agents aren't told it).

## The why (fixed)
Make something they'll still use in six months, not a weekend toy that gets unplugged. The end product matters more than the build, though the build should be enjoyable.
**Why-test:** at six months (counted from when the build is finished) it's still plugged in and used, as a finished thing, not an ongoing tinkering project.

## Audience: me
## Drift: surprise (said)
## No list
- dashboards for smart home stuff
- weather monitoring
- family schedule view
- fitness tracking

## Tension register
| # | Pulls this way | Pulls that way |
|---|---|---|
| T1 | "Complete as is": a finished thing, not a tinkering project | Up to six months of enjoyable weekend building, which invites endless scope and tinkering |
| T2 | The end product matters most | The build should be enjoyable, and the person's strength (soldering) is a build skill |
| T3 | The main asset is a big screen | The no list bans the screen's most obvious job: showing information at a glance |
| T4 | A soldered, hands-on build that uses their real skill | Thin fundamentals and only a multimeter: the last circuit died when it didn't work first time |
| T5 | Surprise: a different kind of thing entirely | It must still be in daily use at six months; strange things get unplugged first |
| T6 | A dead stand means the monitor needs a new body or mount | No CAD skill, and $100 total for new parts |
| T7 | "Complete as is" | "Unless it's something that would take some kind of extensions" |
| T8 | The room has "no real bearing" | A thing with no fixed place and no daily trigger is the thing that gets unplugged |
| T9 | Sealed and finished (Stage 1, spirit line + control) | Alive enough to be worth using at month six without being fed |
| T10 | Every cost ($100, six months of weekends) is paid up front (Stage 1, mudaraba) | The only test is about a year away, so failure shows up after everything is spent |
| T11 | The circuits that are fun to build (analog, audio) (Stage 1, Zewail + control) | Are the ones a multimeter can't see into |
| T12 | The monitor as the product (Stage 1, control) | The monitor as just a part, or not used at all |
| T13 | "Used" means looked at, which wears off (Stage 2, wild card) | "Used" means present and running in the room, nobody minding |

## Brief score: 8/10
- **Room to move:** yes. Surprise drift, the room is open, and the making method is open.
- **Nothing missing from 0:** nearly. The making method is open on purpose; the monitor's inputs and resolution aren't stated, and the six-month clock's start is inferred.
- **Audience confirmed:** yes, "me".
- **Four or more real tensions:** yes, eight at intake, twelve after Stage 1.

## The obvious answer (two cold answers)
1. **Cold A (haiku):** a living-room couch arcade. RetroPie on the Pi 4 drives the monitor, which gets a 3D-printed stand or VESA mount; the hand-built part is a control panel of arcade buttons and a microswitch joystick wired to GPIO through perfboard, every switch to ground, so continuity mode finds any fault. Parts about $60–80. "Finished once the controls work." The mic goes unused.
2. **Cold B (haiku):** a generic "Pi-driven appliance": the Pi runs a standard OS with one auto-starting service, the monitor is the display over HDMI on a printed bracket, and one through-hole perfboard carries buttons, status LEDs and a sensor or power header; everything else is off-the-shelf modules; build and test in stages with the multimeter. It never names what the appliance does.

**The obvious answer used as the distance reference:** Cold A, the retro arcade with a soldered control panel. Cold B gives the same build shape (Pi + monitor on a printed mount + one perfboard of buttons) with no content, so the shared well is "the monitor as a screen for the Pi, plus a perfboard of buttons".

## Known wells (from wells.md, this kind of brief)
- None yet. `wells.md` has sections for books to pair with an essay, Halloween costumes and scrap wood; nothing for "what to build with a Pi / old monitor / electronics on hand".

# Idea dossier: Pi + old monitor

## The choice: Patchwork Booth
- **What it is:** a cigar-box guest book with one soldered button and a ring LED, sitting in front of the old 24-inch monitor. Press, talk for up to 60 seconds, and the story becomes a stitched-looking patch on a quilt that grows on screen. Press again and a random old story replays while its patch glows. When idle, the quilt drifts slowly: a thing in the room, not a dashboard.
- **How it works:** one Python script on the Pi. The button is read with [gpiozero's `Button`](https://gpiozero.readthedocs.io/en/stable/api_input.html) (`when_pressed`); recording is `arecord -d 60 -f cd` from the USB mic ([arecord](https://linux.die.net/man/1/arecord)). Each recording becomes a patch with no speech recognition: duration sets its size, loudness its colours, the waveform its stitch pattern. Patches are drawn on a burlap-textured quilt in a browser kiosk.
- **Why it fits:** it is finished as is. The one opening is the stories themselves, and the household supplies them, not the builder. It grows with the family, so there's a reason to press it at month six. At Gate 2 the person said it "has appeal to me and would also be a hit with my kids", which answers the attack's question of who keeps pressing it.
- **Distance from the obvious answer:** 4. A different kind of thing serving the same need: a family's voice archive with the monitor as its quilt, not a game console.
- **What it would take:** an [Adafruit 16 mm LED-ring pushbutton](https://www.adafruit.com/product/559) ($4.95, built-in LED resistor, 3–6 V); a cigar box (not priced); a drilled hole; a printed monitor foot or mount from an existing published model; a cheap speaker if the monitor has no audio out. Well under $100 (unverified: only the button is priced); about two to four weekends. The soldering is one through-hole switch and one LED, checkable with the multimeter.
- **Cheapest first test (within a week):** wire the button to a GPIO pin on a breadboard, run `arecord -d 10` on the real mic, press, speak and play it back. Then draw one fake patch from a WAV file. Then hand it to the kids (the lead's addition, from the Gate 2 reply).
- **Biggest risk:** nobody presses it after the novelty fades. The kids are the answer to that, and also the test: if they've stopped by month two, it fails the why.
- **Scars, labeled:** the build barely uses the soldering skill (one button, one LED), so the build is short and the end product carries it. The idle quilt is something to look at, which is the kind of use that wears off; the pressing is what has to last.
- **Premises it depends on:**
  - the monitor has an input the Pi can drive (check for HDMI, or buy an adapter);
  - the USB mic records clearly enough;
  - everyone being recorded is told so, plainly, on the box;
  - the kids keep pressing it (the person's word at Gate 2).
- **Where it comes from (source fidelity):**
  - **The cloth-story form is significant.** Chilean arpilleras are burlap-backed textile works documenting life under Pinochet, made in church-based workshops and sold for sustenance ([MOLAA](https://www.Molaa.org/arpilleras-online); [CSMonitor, 1985](https://www.csmonitor.com/1985/0221/hchile.html); [Tatter](https://tatter.org/chilean-arpilleras/)).
  - **The political stakes are a stretch,** so the booth doesn't claim to carry silenced or dangerous stories. A living-room guest book is a gentle borrowing; credit the source on the box.
  - **HiperBarrio is a cursory link.** It is a Medellín youth blogging collective using free internet tools to "show the world local stories", and won the 2009 Prix Ars Electronica Digital Communities Golden Nica ([Rising Voices](https://rising.globalvoices.org/blog/2009/06/05/hiperbarrio-winner-of-the-prix-ars-electronica-awards/)). The shared thread is real but loose: local stories told by the people who live them.

## Runners-up

### Seven-hour line
- **What it is:** the gutted monitor becomes a dark desk-side box with six scent chambers and small fans. Press "board" at the start of the workday and the Pi plays the Bergen-to-Oslo rail run in real time as smell (sea salt, wet stone, cold mint for the Hardangervidda plateau, birch, spruce, city air). At the terminus every fan purges and stops: the workday is over.
- **Why it fits:** a daily trigger and a shape for the day, with no screen asking for attention.
- **Distance:** 5. A different need: ending the workday.
- **What it would take:** six 5 V 40 mm fans, six logic-level MOSFETs (pick one rated for 3.3 V gate drive; an IRLZ44N is marginal) with gate resistors, pull-downs and flyback diodes (standard practice, unverified), fragrance oils and pads; perfboard over a few weekends; under $100 is unverified and may be close: six 5 V 40 mm fans alone run about $36–74.
- **Cheapest first test:** one MOSFET and fan, three jars of scent in a cardboard box, a real workday. After hour 3, do you still notice it? Do you leave at the end? Does a pad charge last?
- **Biggest risk (attack: fatal as designed):** it runs on consumables (pads dry out in days), smell adaptation hides it within hours, and it doesn't use the monitor as a monitor. It survives only if the cardboard test shows a pad lasts weeks and the smell is still liked after a full day.
- **Source:** NRK's *Bergensbanen minutt for minutt* (2009, about 7 h 14–16 min) is central to the real-time structure ([SNL](https://snl.no/sakte-TV); [Wikipedia](https://en.wikipedia.org/wiki/Slow_television)). The broadcast was real-time but not content-uncut (it included interviews and archive material). Route order from [Vy](https://www.vy.no/en/train/routes/the-bergen-line) and [Oslo Spirit](https://www.oslo-spirit.com/guides/bergen-railway-scenic/).

### Solder-along table
- **What it is:** the monitor lies flat under acrylic, shows a perfboard layout at true 0.1-inch scale, lights the next pad from below, and shows the voltage the multimeter should read at each test point. A soldered footswitch steps through. Lying flat solves the dead stand.
- **Why it fits:** it aims at what stalled the last build.
- **Distance:** 5. A different need: a bench tool, not entertainment.
- **What it would take:** a footswitch, a 12×12 in acrylic sheet, layouts drawn in [Perfwire](https://www.producthunt.com/products/perfwire), agent-written code; about 6–10 weekends; roughly $25–60 (prices from search snippets only).
- **Cheapest first test ($0):** lay a perfboard on the monitor over a calibrated 0.1" grid and check whether the glow lands on the hole.
- **Biggest risk (attack: fatal for the stated role):** it's a tinkering tool, used only while building, and each build needs a layout file. Parallax through the parts, acrylic and panel glass may shift the glow by a full pad. It would come back if the person builds about monthly; its guaranteed first job is the unfinished Rat.
- **Source:** the Universal Nut Sheller (a hand-cranked, one-moving-part concrete machine; plans were once free to download, but the Full Belly Project dissolved and its design details are now sold; [Wikipedia, Universal Nut Sheller](https://en.wikipedia.org/wiki/Universal_Nut_Sheller); [Engineering for Change](https://www.engineeringforchange.org/?p=12850)) shapes the design stance only.

## Also on the shelf
The full vault is in `vault.md`. The notable ones:
- **Home Machine / Dated Page** (an instant-on writing computer with a hand-wired keyboard): fit "yes, if they write". Comes back if a daily writing habit exists, and it is also the adversary's "journal" rescue for the booth.
- **Token Juke** (drop a printed RFID token in a walnut cabinet and it plays the whole album): a well (the media-centre answer every generator named), but feasible and a full fit. Comes back if the person wants a music object the kids can operate.
- **Monochord** (one string, the mic hears it, the screen draws it huge): comes back if a playable thing is wanted.
- **Bench Scope:** comes back if the Rat is ever reopened.

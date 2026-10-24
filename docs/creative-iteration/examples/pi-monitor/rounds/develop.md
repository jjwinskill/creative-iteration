# Develop
Three developers (sonnet, with web), one per Gate 1 pick, each given the person's note verbatim. The Seven-hour line developer was told it could keep or relax the smell-only constraint the sketch was written under, as long as it said which (it kept it). Then one adversary (sonnet, no web) attacked all three at once, unranked.

## Patchwork Booth
**What it is.** A cigar-box guest book with one soldered button and a ring LED, sitting in front of the old 24-inch monitor. Press, talk for up to 60 seconds, and your story becomes a stitched-looking patch on a growing quilt on screen. Press again and a random old story replays while its patch glows.

**How it works.** One small Python script on the Pi. The button is read with [gpiozero's Button](https://gpiozero.readthedocs.io/en/stable/api_input.html) (`when_pressed`); recording is `arecord -d 60 -f cd` from the USB mic ([arecord](https://linux.die.net/man/1/arecord)). Each recording becomes a patch: duration sets its size, loudness its colours, the waveform its stitch pattern. No speech recognition. Patches are drawn on a burlap-textured quilt in a browser kiosk; when idle the quilt drifts slowly, a thing in the room, not a dashboard.

**Why it fits.** Finished as is; the only growth is stories, and visitors supply them, not the owner. It grows with the household, so there's a reason to press it at month six. The one soldered part is a through-hole switch and LED, multimeter-checkable.

**What it takes.** [Adafruit 16mm LED-ring pushbutton](https://www.adafruit.com/product/559), $4.95 (built-in resistor, 3–6 V); a cigar box (not priced); a drilled hole; a printed monitor foot from an existing model; a cheap speaker if the monitor has no audio out. Well under $100; about two to four weekends.

**Cheapest first test (one week).** Button on a breadboard to a GPIO pin; `arecord -d 10` on the real mic; press, speak, play back. Then draw one fake patch from a WAV file.

**Biggest risk.** Nobody presses it after the novelty fades.

**Premises.** The monitor has an input the Pi can drive (check HDMI, or buy an adapter). The USB mic records clearly enough. Guests accept being recorded (the box should say so). Someone is in the room often enough to feed it stories.

**On the tag-board note (developer):** it did pull; the pedal stays colour, not a task: the build is one switch and one LED.

**Source fidelity.** Cloth-scene form: *significant*. Political stakes: *stretch*. Digital-communities link: *cursory*.
- HiperBarrio ([Rising Voices](https://rising.globalvoices.org/blog/2009/06/05/hiperbarrio-winner-of-the-prix-ars-electronica-awards/)): young bloggers in Medellín using free internet tools to "show the world local stories"; 2009 Digital Communities Golden Nica, €10,000. About blogging and video workshops, not voice recording, quilts or guest books. The shared thread (local stories told by the people who live them) is real but loose.
- Arpilleras ([MOLAA](https://www.Molaa.org/arpilleras-online); [CSMonitor, 1985](https://www.csmonitor.com/1985/0221/hchile.html); [Tatter](https://tatter.org/chilean-arpilleras/)): burlap-backed textile works documenting life under Pinochet, made in church workshops, sold for sustenance, called "tapestries of defamation" by the regime; the disappearances "have gone officially unrecorded", so women re-created their histories in cloth. Stitched scenes as testimony for unrecorded stories is central to the form.
- Unverified: "scrap cloth" (fetched pages say burlap base with "bright solids and prints"); loved ones' clothing sewn in (search summary only); the Ars Electronica jury text (PDF unreadable).
- Reshape: don't claim the box carries silenced or dangerous stories; a living-room guest book is a gentle borrowing. Keep the burlap and appliqué look and guests as storytellers; credit both sources on the box.

**Attack:** it only works if other people keep pressing the button, and the brief gives no evidence they will. The brief describes one person "using it" and never mentions guests, a household or hosting. Without visitors, month six is an empty quilt drifting on a screen: the "looked at" novelty that wears off (T13). The developer carries this as a risk, but here it is the why-test itself. Smaller: one button and one LED barely use the soldering skill (T2). **FATAL as written**; a scar only if the person hosts about weekly. The only rescue the adversary sees is the owner's own daily 60-second end-of-day press, which is a different concept (a journal).

## Seven-hour line
**What it is.** A desk-side "train" made from the gutted monitor shell, holding six scent chambers and small fans. Smell-only (the developer kept the constraint): the shell stays dark, so nothing on the desk asks for your eyes. One concession: fans hum, so use quiet ones.

**How it works.** Press a button when you sit down ("board"). The Pi steps through the Bergen-to-Oslo run in real time: sea salt, wet stone (fjord and lake shores), cold mint (the Hardangervidda summit), birch, spruce, city air. At the terminus every fan runs a purge, then stops. No prompt, no log: work ends without a question. GPIO ([about 16 mA a pin, about 50 mA total, per secondary sources](https://zbotic.in/raspberry-pi-gpio-pinout-complete-reference-guide/)) drives one [IRLZ44N-class MOSFET](https://wiki.adom.inc/ray/irlz44) per fan, each with a 100 Ω gate resistor, a pull-down and a flyback diode. A 3.3 V gate may only partly switch it (resistance [specified at 4–5 V](https://www.vishay.com/en/product/91328/)), so test one before building six.

**Why it fits.** A finished object that earns its place daily with no tinkering; a shape for the day rather than a gadget.

**What it takes.** 6 × [5 V 40 mm fans](https://pro.maplin.co.uk/products/eb40100s2-999-5v-dc-brushless-axial-fan-40-x-40-x-10mm) (about £5 each), 6 MOSFETs ([about €0.50 each](https://store.comet.bg/en/Catalogue/Product/21765)), essential oils and pads; perfboard and through-hole soldering over a few weekends; every channel multimeter-checkable; printed boxes from existing models; well under $100 (estimate).

**Cheapest first test (one week).** One MOSFET and fan on a breadboard, three jars of scent in a cardboard box; run a real workday. After hour 3, do you still notice the changes? Do you leave at the end?

**Biggest risk.** Smell adaptation: [perceived intensity falls fast, then levels off](https://fis.tu-dresden.de/portal/en/publications/habituation-and-adaptation-to-odors-in-humans(0991ecaa-8188-4fbd-8e93-3b00f36f3fe4).html) (time-course from a search summary). Odorless gaps help; pulse the fans.

**Premises.** Scents are tolerable for 7 hours a day, for the user and anyone sharing the room. The user is willing to leave at the terminus. Scent differences read as distinct places. 3.3 V gate switching works. The Pi's job is only timing.

**Source fidelity.** *Bergensbanen minutt for minutt*: **central** to the real-time structure. [Wikipedia](https://en.wikipedia.org/wiki/Slow_television): NRK's first slow-TV production, four cameras, timed to match the journey, archive clips during the 182 tunnels. [SNL](https://snl.no/sakte-TV): 7 h 16 min, nearly 1.2 million viewers. [ACMI](https://www.acmi.net.au/works/61989--bergensbanen/): 7 h 14 min. Conflicts: 27 or 29 Nov 2009; 7:14 or 7:16. Correction: "uncut" holds for the real-time journey, not the content (it included interviews and archive material). Scent timeline comes from line-level descriptions, not footage; plan to take timestamps from the actual video. Route ([Oslo Spirit](https://www.oslo-spirit.com/guides/bergen-railway-scenic/), [Vy](https://www.vy.no/en/train/routes/the-bergen-line), [Bergen Line](https://en.wikipedia.org/wiki/Bergen_Line)): fjordland near Bergen, tunnels down from Myrdal, the treeless Hardangervidda plateau with Finse at 1,222 m, then birch and spruce forest and river valleys, then the Oslo suburbs. Correction: the sketch's "birch before the summit" is not supported; birch and spruce come after the plateau. *Edhi cradles*: **cursory, close to a stretch** ([Dawn](https://www.dawn.com/news/1551962): about 300 cradles, "no questions asked"); overwork is not comparable to infant abandonment; keep only the structural angle (an exit where the act happens, asking nothing).

**Attack:** it isn't "complete as is": it runs on consumables, and the person can't tell whether it's working. Six oil pads under fans for about 7 hours a day dry out in days, so re-dosing is the feeding chore the why rules out. Adaptation means that after the first hours nothing is noticed; strong enough to beat adaptation, a shared room wants it off. "Sea salt", "wet stone" and "city air" aren't essential oils and need synthetic fragrance oils that may smell cheap. It guts the monitor, so the asked-about asset does no work (T12), and the Pi is only a timer. The gate-switching worry isn't the real risk. **FATAL as designed**, but settled by a cheap weekend test: if one pad charge lasts weeks at low fan duty and the person still notices and likes it after a full workday, the leftover refill is a scar to label ("refill the oils monthly").

## Solder-along table
**What it is.** The 24-inch monitor lies flat, face-up, with a clear acrylic window over the work area and a soldered footswitch on the floor. One job: it guides every perfboard build from now on.

**How it works.** You draw the build in [Perfwire](https://www.producthunt.com/products/perfwire), a free, Apache-2.0 browser perfboard planner. A Pi script (Python, [gpiozero](https://gpiozero.readthedocs.io/en/stable/api_input.html) reading the footswitch) draws the layout at true 0.1-inch pitch (the developer's arithmetic: a 24" 1080p panel gives about 9.2 px per 0.1", 1920×1200 about 9.4 px). The next pad glows through its hole from below; test steps show the voltage the multimeter should read; the footswitch advances. The Pi 4 has [micro-HDMI and a 40-pin GPIO header](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/).

**Why it fits.** Finished as is; the one opening is new build files. Used on every future build, not looked at. Debugging becomes "does the meter match the screen?", the gap that stalled the Rat.

**What it takes.** About 6–10 weekends; one footswitch and a wire, plus agent-written code; a simple printed rectangle frame. Roughly $25–60: a [momentary stomp switch](https://www.taydaelectronics.com/4-pins-spst-momentary-soft-touch-push-button-stomp-foots-pedal-switch.html) (~$2.49, snippet only) and a [12×12 in, 1/8 in acrylic sheet](https://homedepot.com/p/Falken-Design-12-in-x-12-in-x-1-8-in-Thick-Acrylic-Clear-Sheet-Falken-Design-ACRYLIC-CL-1-8-1212/308669852) (~$14, snippet only); neither price confirmed.

**Cheapest first test (one week, $0).** Lay a perfboard directly on the monitor, draw a calibrated 0.1" grid in a browser page, and check whether a lit pixel blob shows through a hole.

**Biggest risk.** Parts stand off the board and parallax shifts the glow; components under the board stop it lying flat on the acrylic.

**Premises.** The 2014 monitor works lying flat and its matte coating doesn't wash out the glow. Its pixel pitch is close to 9 px per 0.1". There's a suitable input cable. A hot iron near acrylic is tolerable. Test voltages come from simulation or a verified build, not memory.

**Source fidelity (Universal Nut Sheller).** [Wikipedia, Full Belly Project](https://en.wikipedia.org/wiki/Full_Belly_Project); [VOA Learning English](https://learningenglish.voanews.com/a/a-23-2008-03-09-voa1-83136017/128297.html); [Afrigadget](https://www.afrigadget.com/tag/nut/). A hand-cranked concrete cone-in-cone machine with one moving part; 50 kg/h vs 1.5 kg/h by hand; under $50 to make from fiberglass molds; plans "free and downloadable"; the Full Belly Project dissolved in December 2020. Rating: *significant* for the design stance (one job, one moving part, locally buildable, shared plans), *cursory* for the mechanics; inspiration, not derivation. Unverified: Brandis "refused to patent" (search summary only). Prior art: no existing "light the next hole" perfboard table found; Perfwire is a layout checker, not a guide.

**Attack:** it's a tool for tinkering, and the person said the opposite is what they want ("using it, likely not tinkering"; the end product matters more than the build). It's only used while soldering a new project, and the brief establishes no build cadence; the only build it names stalled in 2021. Each new build also needs a Perfwire plan turned into a file, so the "one opening" is a recurring chore that gates every use. The $0 test checks the physics, not whether it gets used. The physics may be a second killer: the solder side faces up, so parts hold the board off the glass, and with the acrylic and panel glass the glow could shift by about a full 0.1" pad, breaking "this pad next". In its favour, lying flat solves the dead stand. **FATAL for the stated role** unless the person starts a new build about monthly; a guaranteed first use would be debugging the unfinished Rat with the voltages the table shows.

## Gate 2 (verbatim)
"We choose patchwork booth - it works well because it has appeal to me and would also be a hit with my kids"

The reply answers the premise the attack rested on (who keeps pressing it): the person has kids, which the brief never said. No combination was asked for, so nothing went back to the adversary. The lead made no change to the concept.

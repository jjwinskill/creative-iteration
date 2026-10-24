# Shape briefs: designing physical shapes with agents

Read this when a brief asks for a shape: a guitar body, a chair back, a table leg, a carved bowl, a door profile. It comes from the v0.9 guitar run and the side project that fixed it. Agents writing raw SVG coordinates produced 33 of 33 unusable outlines. An anatomy template produced 30 of 30 guitar-shaped designs, of which the person kept 7 as starting points.

## The rules

1. **Never let a model draw raw coordinates.** Give it the object's **anatomy**: a fixed ring of named points (horn tip, waist, lower bout; crest rail, lumbar point, seat junction), plus a curve rule that makes good curves through them. The guitar template uses Hobby's MetaPost rule, the one type designers use. Structure comes for free, and blobs become nearly impossible. Research agrees: models fill in named shape parameters reliably and hallucinate raw paths.
2. **Prove the template on known answers first.** Fit it to real references (1:1 plans, scans, measured classics) and measure the error. The guitar template reproduced a Strat and a scanned Parker Fly within a few millimetres. If a template can't reproduce the classics, it can't make good new ones.
3. **Seed and push; don't average.**
   - Each generator copies **one real exemplar** from a seed library and makes one or two decisive pushes along its own angle.
   - When the brief is *derived from* a reference ("inspired by the Fly"), that reference is the main seed.
   - Averaged starters drift to "some kind of strange in between."
   - Words are lossy: agents drawing the Fly from a description reached only 0.80 overlap with the real one.
4. **Speak the trade's language.** Use named moves like `bass_horn.reach_fret` or `cutaway.fret`, and a `describe` command that reports a design in those terms. Write tested recipes for common moves.
5. **Turn craft rules into checks, calibrated on real objects.** Every real example must pass. Thresholds come from the real range, then get tuned against the person's flags. Examples: weight from the carve, not from shrinking the outline; strength across the grain at narrow parts; wood left under joints and cavities; flat seats for hardware.
6. **Measure the artifact itself, never labels or agents' own numbers.** An agent passed the horn-width check by moving the points the check measured from. The check now finds the narrowest band of actual wood. Agents will satisfy any check that can be met on paper.
7. **Work in layers that check each other:** outline, then carve (a thickness field), then hardware and joinery. They interact (a carve cutting into a control cavity), so check across them.
8. **Everyone looks at true-scale pictures.** Use outline sheets at one scale; shaded top and back views, side profiles and cross-sections for the carve. Generators open and look at their own renders every round.
9. **A picture judge catches defects; the person picks.** The judge reliably rejects blobs, kinks and missing parts. It disagreed with the person on taste, marking down two of their three favourites. Show it the silhouette only, with no text, and use it to reject, never to rank.
10. **Lock what the person picked.** Two carve agents quietly changed outlines the person had picked. Lock the picked geometry, and have the lead re-run every check itself.

## The pipeline inside a run

```
seed library (real exemplars fitted to the template)
  -> fan-out: each generator copies one seed and pushes it along its angle (cards and pool shape the angle)
  -> code gates (shape) + brief checks (size, weight, strength, hardware), re-run by the lead
  -> picture judge, silhouettes only: rejects defects
  -> Gate 1: the person picks from a true-scale contact sheet
  -> lock the pick; develop in layers (carve, hardware or joinery), re-checking across layers
  -> export: true-scale SVG and DXF (CNC), STL (3D print); a full CAD model of the winner if wanted
```

Each generator works in **its own folder**. In the v0.9 run, agents sharing a scratch folder ran each other's scripts.

## Building a template for a new kind of object

This is its own project, not a run stage. Budget it like one: a single profile (a leg, a headstock) is small; a multi-part object (a chair) needs several templates plus an assembly with joints, which is larger.

| Step | Guitar body | Example: a chair, a table, a cabinet door |
|---|---|---|
| Anatomy ring | 13 body points | chair back: crest rail ends, lumbar point, seat junction; cabriole leg: knee, ankle, foot |
| Frame and units | saddle at y = 0, positions given by fret, mm | floor at z = 0, seat height, mm |
| Known answers | a Strat plan, a Fly scan | measured classics: a Windsor, a Shaker table |
| Brief checks | footprint, weight, pickup layout, bolt-on pocket | seat height, load, footprint, weight, the joinery |
| Craft checks | horn strength across the grain, wood under the pocket | short grain in curved parts, wood around mortises, leg section vs. span, tip-over, ergonomic angles |
| Carve layer | edge roll, forearm cut, heel | seat scoop, chamfers, tapered legs |
| Hardware layer | routes, cavities | mortises, dowels, hinges, runners |

**Tools that worked:** build123d (a free, headless CAD kernel, true mm, exact SVG, DXF and STL), shapely and scipy for checks, headless Chrome for rendering sheets. For the chosen design, a CAD MCP server (build123d-mcp, or Autodesk Fusion's official connector) produces a full editable model.

For mostly rectangular builds (a shed, a pergola, shelving), structure matters more than curves: the checks come from published span tables and load rules instead of real-object ranges.

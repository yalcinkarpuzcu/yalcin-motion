# Storyboard: ESS'26 · sponsor ve paydaş filmi (v2: Vibe to Venture, duyuru + paydaşlık)

Theme: 056 Workflow Canvas · Format: 1080×1920 · Length: 23 s · Sound: music (120 BPM, D minor, half-time feel) + warm SFX

## Message & tone
- **Sentence:** I want to say "at ESS'26 your brand doesn't just get seen, it makes measurable contact with the right people" in a trustworthy, confident tone, so the viewer feels this is a network to plug into, not a banner to buy.
- **Tone arc:** mysterious → bold → trustworthy → technical → warm
- accent: lime `#C9FF5F`, saved for the brand node and the single branch that ends in the call to action
- **Motif:** the "MARKANIZ" node (`motif:brand-node`). It sits alone in the hook, becomes the hub of the network, opens up into the patch bay, and finally feeds the lime cable that becomes the CTA horizon.

## Ledger

| # | start | dur | beat | tone | entrance | transition_out | ease | direction | palette | camera | components | new_component | sfx | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0:00 | 4.0 | hook | mysterious | typewriter-mask | beat-cut-hold | power2.out | top-down | ink+lavender | slow push-in | motif:brand-node, dot-grid, headline | | low-hum | surprise: freeze + half a beat of silence at 3.5 s; a lone dashed MARKANIZ node on the dot grid; "VIBE TO VENTURE." then "ARADAKİ BAĞ: MARKANIZ." |
| 2 | 0:04 | 2.5 | reveal | bold | cable-snap | dolly-out-reveal | expo.out | radial | violet+ink | pull-back from hub | motif:brand-node, node-ring, bezier-cables | | snap-stab | hard cut on the drop: seven cables snap out from the hub to seven stakeholder nodes, rings ignite lavender |
| 3 | 0:06.5 | 5.5 | proof | trustworthy | packet-hop | split-stack | power1.inOut | left-to-right | ink+violet | locked (after the pull-back settles) | motif:brand-node, packets, stat-strip | | packet-blip | packets hop hub ↔ node one per beat; each arrival pulses the ring; the stat strip counts 83 · 121 · 62 · 17 under "GEÇMİŞ ZİRVELERDE" |
| 4 | 0:12 | 5.5 | proof | technical | patch-plug | line-to-horizon | steps(6) | right-to-left | panel+lavender | locked, macro on the hub | motif:brand-node, port-rows | patch-bay-hub | jack-click ×6 | surprise: change of scale, macro into the hub; three strips stack in and the hub opens into a patch bay: six touchpoint ports, a cable plugs in on each beat and its LED lights |
| 5 | 0:17.5 | 5.5 | cta | warm | horizon-draw | end | power3.out | bottom-up | ink+lime | locked | motif:brand-node, cta-lockup, logos | | warm-chord | the last cable turns lime and straightens into a horizon; above it "BİRLİKTE TASARLAYALIM."; below it info@letscaleup.org, date, venue and logos; the last 1 s is held |

## The seven questions (answer before you build)
1. **What do I want to say, and in what tone?** The sentence above. Trustworthy means even beats, a locked camera, clear sans type and numbers in tabular figures.
2. **Is anything repeating?** Five entrances, five eases and four transition families (cut, camera, mask, carry). None of these transitions was used in the invite film.
3. **What does each transition mean?**
   - hook → reveal, **beat cut with hold-frame**: the question freezes in silence, and the drop answers it with the whole network.
   - reveal → proof, **dolly-out reveal**: one node turns out to be the centre of seven groups. That is the scale.
   - network → patch bay, **split stack**: three strips, an editorial "here is what's inside", from the overview into the list of touchpoints.
   - patch bay → CTA, **line-to-horizon**: the last cable you plug in is the one that leads to us. It straightens into the CTA's horizon.
4. **What are the colours doing over time?** Ink and lavender, with the hub's dashed border the only lime trace. Violet cables at the reveal. Lime appears on the LEDs one by one in the patch bay, then floods the final cable and the e-mail address (the colour event).
5. **Which component have I never made before?** The **patch-bay hub** (Frame 4).
6. **Where is the surprise?** 3.5 s (freeze plus silence), 12 s (split stack), 17.5 s (cable to horizon).
7. **Did this repeat my last film?** Audited against `~/.motion-ledger.json` (ess26-davet).

## Frames

### Frame 1 · Hook (0–4 s)
- key visual: a dot grid, one dashed rounded square in the centre labelled MARKANIZ, a grey ring.
- on-screen words: VIBE TO VENTURE. / ARADAKİ BAĞ: MARKANIZ.

### Frame 2 · Reveal (4–6.5 s)
- key visual: seven nodes in a ring around the hub, with cables snapping out on the drop. Title: EURASIA STARTUP SUMMIT'26 · 24 EKİM 2026 · ÇORLU.

### Frame 3 · Proof: the network (6.5–12 s)
- key visual: packets hopping along the cables; the stat strip below.
- on-screen words: VIBE'DAN VENTURE'A TEK SALONDA. · 83 STARTUP · 121 MENTOR · 62 PARTNER · 17 ÜLKE

### Frame 4 · Proof: patch bay (12–17.5 s)
- new component: **patch-bay hub**. Verb: *connects*. Metaphor: a studio patch bay. Primitive: node ports. Twist: each port is a real touchpoint from the privileges table, and its LED only lights when a cable is plugged in. Motion signature: the cable plugs in with a 6-step jack movement (`steps(6)`) and a click; the LED snaps on in one frame.
- on-screen words: TEMAS NOKTALARI · Sahne & backdrop · B2B eşleştirme · Girişimci sunumları · Yaka kartı & foyer stant · Basın & sosyal medya · VIP akşam yemeği

### Frame 5 · CTA (17.5–23 s)
- key visual: a lime horizon line; above it ESS'26 İŞ BİRLİĞİNİ / BİRLİKTE TASARLAYALIM.; below it info@letscaleup.org, 24 EKİM 2026 · Çorlu Sanayi ve Ticaret Odası, and the logos.

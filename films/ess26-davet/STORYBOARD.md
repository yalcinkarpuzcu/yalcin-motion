# Storyboard: ESS'26 · Instagram davet filmi (v2: Vine to Venture, duyuru + paydaşlık)

> v2: the dot is the *vine* in the hook and the full stop of *VENTURE* in the CTA, so the film itself travels vine → venture. Frame notes below describe v1 where not updated in the ledger.

Theme: 094 Match Cut · Format: 1080×1920 · Length: 22.5 s · Sound: music (120 BPM, 1 bar = 2 s) + warm SFX

## Message & tone
- **Sentence:** I want to say "24 Ekim'de girişim ekosistemi Çorlu'da buluşuyor, yerini al" in a bold, warm tone, so the viewer feels they would miss the room everyone else will be in.
- **Tone arc:** mysterious → bold → warm → celebratory → playful → bold
- accent: lime `#C9FF5F` (violet `#6C35D2` and lavender `#A98BF0` are supporting tones, not accents)
- **Motif:** the lime dot (`motif:lime-dot`). It always sits at the same point in the frame, **R = (800, 1010)**. It is the idea (hook), the lens onto the stage (reveal), the traveller on the route (proof), the colour flood (numbers), the badge's punch hole (invite) and the full stop of ÇORLU (CTA). Each time it comes back it carries more meaning.

## Ledger

| # | start | dur | beat | tone | entrance | transition_out | ease | direction | palette | camera | components | new_component | sfx | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0:00 | 4.0 | hook | mysterious | word-clip-up | focal-iris | expo.out | left-to-right | ink+lime | locked | motif:lime-dot, headline | | soft-tick | "HER GİRİŞİM BİR / VINE●": the full stop is the lime dot at R (the vine); the words dim away and the dot stays alone for half a beat |
| 2 | 0:04 | 2.5 | reveal | bold | iris-from-dot | speed-ramp | power4.out | radial | violet+ink | push-in | motif:lime-dot, stage-photo, title-lockup | | stab | surprise: on the drop the dot opens into an iris onto a real past summit stage; EURASIA STARTUP SUMMIT'26 lands in three lines under the lime VINE TO VENTURE kicker, with the date line below |
| 3 | 0:06.5 | 4.5 | proof | warm | stamp-press | graphic-match-color | power2.inOut | bottom-up | ink+lavender | tracking (world scrolls, dot locked at R) | motif:lime-dot, dotted-route, past-photos | route-stamp-passport | stamp-thud ×5 | the dot stays still while the route scrolls up under it; each city lands a stamp ring (2021 İSTANBUL … 2025 ESKİŞEHİR) and two stops flash a real photo inside the dot |
| 4 | 0:11 | 3.5 | proof | celebratory | count-up | object-carry | power3.out | center | lime+ink | locked | motif:lime-dot, number-stack | | tick-run | surprise: colour event, the dot floods the whole frame lime; 83 STARTUP · 121 MENTOR · 62 PARTNER · 17 ÜLKE count up in ink, one per beat |
| 5 | 0:14.5 | 4.0 | invite | playful | lanyard-drop | match-cut-shape | sine.inOut | top-down | panel+lavender | locked | motif:lime-dot, program-chips | lanyard-badge | cloth-swish | the flood shrinks back to the dot, which becomes the badge's punch hole; the badge drops (role cycles GİRİŞİMCİ → YATIRIMCI → PARTNER) on its lanyard and settles with a damped swing (physics on a non-UI object, no bounce ease) |
| 6 | 0:18.5 | 4.0 | cta | bold | slide-from-left | end | power2.out | right-to-left | ink+lime | locked | motif:lime-dot, cta-lockup, logos | | warm-chord | hard cut on the bar: the punch hole is now the full stop of VINE TO / VENTURE●; date + ÇORLU, venue, YERİNİ AL + PARTNER OL, info@letscaleup.org and the three official logos; the last 1 s is held |

## The seven questions (answer before you build)
1. **What do I want to say, and in what tone?** The sentence above. Bold and warm: big type, hard bar-locked cuts and real photos of real people.
2. **Is anything repeating?** Six different entrances, six eases (expo.out, power4.out, power2.inOut, power3.out, sine.inOut, power2.out), five transitions from four families (mask, time, cut, carry). The only repeat is the dot, which is a declared motif.
3. **What does each transition mean?**
   - hook → reveal, **focal iris from the dot**: the lonely idea opens onto a hall full of people, so the answer to "doesn't grow alone" is the room.
   - reveal → route, **speed ramp**: five years in one breath. The title accelerates up and out, and the route arrives.
   - route → numbers, **graphic match: colour**: the dot that travelled every year swells into a lime field, and what those years added up to sits on it.
   - numbers → badge, **object carry**: the whole flood collapses back into one dot, which becomes the hole in *your* badge, so the numbers turn into your seat.
   - badge → CTA, **match cut: shape**: punch hole = full stop, the same circle in the same place. The invitation becomes a statement.
4. **What are the colours doing over time?** Ink with a single lime dot until 0:11. Violet light in the stage photo at the reveal. Lavender stamps on the route. One lime flood at 0:11 (the colour event), then lime retreats to the dot, and finally to ÇORLU● and the YERİNİ AL chip.
5. **Which component have I never made before?** **Route-stamp passport** (Frame 3) and **lanyard badge** (Frame 5).
6. **Where is the surprise?** 0:04, a hall bursts out of a single dot; 0:11, the full-frame lime flood. The gap is 7 s.
7. **Did this repeat my last film?** The ledger is empty (`~/.motion-ledger.json` does not exist yet), so this is the first recorded film.

## Frames

### Frame 1 · Hook (0:00–4:00)
- key visual: near-black ink; three lines of heavy type on the left; the full stop is a lime dot at R.
- moves first: the words clip up one by one (expo.out, an eighth apart), then the dot pops at the downbeat (2.0 s). At 3.2 s the words dim to 0 and the dot breathes once.
- on-screen words: HER GİRİŞİM BİR / VINE.

### Frame 2 · Reveal (0:04–6:50)
- key visual: an iris grows from R and reveals a past summit stage (Şanlıurfa 2024 photo, violet-lit). EURASIA / STARTUP / SUMMIT'26 slams in at the top left; a small lime ring stays at R.
- moves first: the iris on the drop (4.0 s, power4.out), with a slow push-in on the photo.
- on-screen words: EURASIA STARTUP SUMMIT'26 · LET'S SCALE UP FİNAL ZİRVESİ

### Frame 3 · Proof: the route (0:06.5–11:00)
- key visual: a vertical dotted route scrolls up through the frame while the dot stays locked at R. Each time a city reaches the dot, a lavender stamp ring is pressed (year + city). At Bodrum and Eskişehir the dot briefly fills with a real photo.
- new component: **route-stamp passport**. Verb: *gathers, every year in a new city*. Metaphor: passport stamps. Primitive: timeline. Twist: the traveller never moves, the country moves under it. Motion signature: each stamp lands with scale 1.25 → 1, a 4° rotation settle and a 2-frame ink-darken (`steps(2)`).
- on-screen words: 2021 İSTANBUL · 2022 BODRUM · 2023 İSTANBUL · 2024 ŞANLIURFA · 2025 ESKİŞEHİR

### Frame 4 · Proof: the numbers (0:11–14:50)
- key visual: a full-frame lime flood; four huge numerals stacked in ink, left-aligned, each with a small label.
- moves first: the flood from R (power3.out), then the numbers count up on consecutive beats.
- on-screen words: 83 STARTUP · 121 KONUŞMACI & MENTOR · 62 PARTNER · 17 ÜLKE (labelled "geçmiş zirvelerde" in a small caption)

### Frame 5 · Invite: your badge (0:14.5–18:50)
- key visual: a lanyard drops from the top; the KATILIMCI badge hangs from it with the lime dot as its punch hole. On the badge: ESS'26, KATILIMCI, 24.10.2026 · ÇORLU, and four chips: Keynote · Girişimci Sunumları · B2B Matchmaking · Networking.
- new component: **lanyard badge**. Damped swing: angle = 9°·e^(−1.4t)·cos(5.2t), computed from t.
- on-screen words: KATILIMCI · 24.10.2026 · ÇORLU · four chips

### Frame 6 · CTA (0:18.5–22:50)
- key visual: "SIRADAKİ DURAK" small; ÇORLU● huge with the dot at R as its full stop; 24 EKİM 2026 · Çorlu Sanayi ve Ticaret Odası; a lime YERİNİ AL chip; JCI Avrasya · Let's Scale Up · Çorlu TSO logos.
- loop note: not a loop; hold the last 1 s.

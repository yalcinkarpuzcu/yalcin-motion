# Storyboard: Satış Yolculuğu · Satışın Yeni Tanımı

Theme: 087 Cut-Paper Title Sequence (in the Satış Yolculuğu brand) · Format: 1920×1080 · Length: 8:26.4 · Sound: the host's own voice recording (no added music)

## Message & tone
- **Sentence:** I want to say "sen para avcısı değilsin, sen değer yaratıcısısın" in a warm but bold tone, like a friend who talks straight, so the viewer feels proud to say "ben satışçıyım".
- **Tone arc:** warm/awkward (the dinner) → playful-ugly (the sticky salesman) → bold (the tear, Season 2) → urgent (the money-hunter, the alarm) → trustworthy (the bridge, the value example, the doctor) → warm (mindset) → celebratory (the one message) → mysterious/warm outro (next: keşif).
- accent: rust
- **Motifs:**
  - `motif:cut`: the quiet base. Most in-chapter beats are plain hard cuts on the speaker's pauses; narrative transitions are spent where the story turns.
  - `motif:sting-wipe`: the paper road strip that wipes the frame on each of the three music stings in the recording (2:08, 6:12, 8:03), with the official logo. It carries the "yolculuk" idea and changes direction each time.
  - `motif:morning`: the same paper alarm clock rings twice. At 1:34 it wakes the money-hunter ("whose money can I move today?"). At 6:20 it wakes the value creator ("Ben bugün kime yardım edeceğim?").
  - `motif:road`: in the homework (7:34) the road comes back as the customer's own road: DÜNYASI → SORUNU → UMUTLU GELECEK.
- **Colour events (rust):** 1) the fight-or-flight alarm (2:01), 2) BLA BLA BLA → PARA VER (4:19), 3) the net tears and yellow floods for the one message (7:57).

## Ledger

Generated from `tools/ledger.py` (start times come from the recording's word timings in `source/words.json`).

<!--LEDGER-->
| # | start | dur | beat | tone | entrance | transition_out | ease | direction | palette | camera | components | new_component | sfx | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0:00.0 | 5.3 | hook | warm | eyelid-bars-open | motif:cut | power2.inOut | out | yellow+ink | locked | eyelid strips, credit caption |  |  | the frame opens like an eye: 'gözünün önüne getir' |
| 2 | 0:05.3 | 5.4 | hook | warm | slide-snap-left | push-down | power2.out | right | yellow+ink+cream | top-down | paper dinner table, plate discs, head discs |  |  | AİLE YEMEĞİ · YILLAR SONRA credits |
| 3 | 0:10.7 | 7.7 | hook | playful | mask-flip-row | T05 object-carry | back.out(1.4) | up | cream+ink | locked | head discs | başardım maskesi |  | surprise: every head flips a 'BEN BAŞARDIM' mask on the same word |
| 4 | 0:18.4 | 3.7 | hook | bold | bubble-pop | T09 push-through | expo.out | in | ink+yellow | push-in | speech bubble, jaunty words |  |  | the question slams in word by word |
| 5 | 0:22.1 | 5.0 | hook | mysterious | breath-scale | motif:cut | sine.inOut | radial | yellow+ink | slow push | chest disc, BEN SATIŞÇIYIM |  |  | surprise: the big word holds still for a breath before 'diyebiliyor musun?' |
| 6 | 0:27.1 | 13.6 | hook | playful | strip-cover-stack | T06 type-carry | power3.out | left | cream+ink | locked | euphemism strips covering SATIŞ | süslü örtü şeritleri |  | the three euphemisms slide over the word; surprise: the strips grow frilly scalloped edges on 'süslü' |
| 7 | 0:40.7 | 6.1 | problem | warm | knot-tie | motif:cut | power1.inOut | radial | yellow+ink | locked | SATIŞ strip tied in a knot, many small discs |  |  | 'boğazında düğümleniyorsa' → 'yalnız değilsin': discs gather round; surprise: the word SATIŞ ties itself into a knot |
| 8 | 0:46.8 | 3.3 | problem | mysterious | book-open | slide-push | power2.out | left | ink+cream | locked | paper storybook cover |  |  | YANLIŞ BİR HİKÂYE |
| 9 | 0:50.1 | 10.6 | problem | playful | puppet-build | tear-tumble | steps(6) | down | rust+ink+cream | locked | sticky-salesman puppet, label tags | yapışkan satıcı kuklası |  | surprise: kicked out of the door, he drops back in down the chimney |
| 10 | 1:00.7 | 4.7 | turn | bold | tear-tumble | T13 product-shape-mask | power2.in | down | yellow+ink | shake | torn poster halves |  |  | surprise: the whole poster tears in two and tumbles off: 'yırtıp atıyoruz' |
| 11 | 1:05.4 | 7.1 | reveal | bold | logo-mask-open | T03 graphic-match-color | expo.out | in | yellow+ink | locked | official logo, SEZON 2 credit, wallet→head swap |  |  | the logo opens through its own shape; 'cüzdanı değil, zihniyeti' |
| 12 | 1:12.5 | 5.7 | reveal | trustworthy | card-flip | motif:cut | power2.inOut | up | cream+ink | locked | OLDUĞU / OLMASI GEREKEN cards |  |  | strike-through on 'olduğu' |
| 13 | 1:18.2 | 4.6 | reveal | warm | title-card-jaunty | T16 split-stack | power4.out | left | yellow+ink | locked | SATIŞIN YENİ TANIMI title card |  |  | surprise: full title card, the episode name, holds for 'Tekrar hoş geldin' |
| 14 | 1:22.8 | 7.4 | chapter | bold | split-strips-in | motif:cut | expo.inOut | right | ink+yellow | locked | DEĞİŞKEN DENKLEM card, SATIŞ = ? equation |  |  | dark ground: honest talk |
| 15 | 1:30.2 | 3.9 | problem | technical | coin-drop | T02 match-cut-motion | power4.out | down | ink+yellow+rust | locked | equation, paper coin |  |  | the ? becomes a coin: SATIŞ = PARA ALMAK; surprise: the ? drops as a coin |
| 16 | 1:34.1 | 8.0 | problem | playful | alarm-ring | motif:cut | steps(8) | right | yellow+ink | locked | alarm clock disc, tie strip, pocket→safe dotted transfer |  |  | motif:morning (first time: whose money can I move?) |
| 17 | 1:42.1 | 8.8 | problem | bold | hand-cup-rise | T17 paper-fold | power3.inOut | up | ink+cream | locked | cupped paper hand, MODERN DİLENCİ |  |  | surprise: the handkerchief folds into a brochure: 'mendil yerine broşür' |
| 18 | 1:50.9 | 4.5 | problem | bold | type-slam | T10 whip-pan | expo.out | left | cream+ink | locked | İNSANLAR APTAL DEĞİL |  |  |  |
| 19 | 1:55.4 | 5.8 | problem | mysterious | eye-dollar-blink | motif:cut | power2.in | radial | ink+cream | slow push | dollar eyes, invisible dashed wall bricks | görünmez duvar |  | bricks appear as dashed outlines, one per beat; surprise: dollar signs blink into both eyes |
| 20 | 2:01.2 | 6.4 | problem | urgent | alarm-flood | T04 beat-cut-hold | steps(2) | out | rust+ink | shake | siren discs, SAVAŞ YA DA KAÇ |  |  | surprise: colour event 1, rust floods the frame and flashes |
| 21 | 2:07.6 | 3.1 | sting | bold | road-wipe | motif:sting-wipe | power2.inOut | right | yellow+ink | locked | official logo, paper road strip |  |  | music sting: the road strip wipes the frame; surprise: medium change, the road strip wipes the screen |
| 22 | 2:10.7 | 7.2 | turn | calm | credit-type-on | motif:cut | power1.out | left | yellow+ink | locked | GERÇEK ŞU credit, SEZON 1 tag |  |  |  |
| 23 | 2:17.9 | 6.7 | turn | playful | split-halves | T05 object-carry | power2.out | left | cream+ink+yellow | locked | NEFRET EDER / BAYILIR halves |  |  | surprise: the frame splits in two |
| 24 | 2:24.6 | 3.7 | turn | bold | puzzle-snap | motif:cut | back.out(1.6) | in | yellow+ink | locked | paradox halves snapping together |  |  | surprise: the two halves lock like puzzle pieces |
| 25 | 2:28.3 | 4.3 | proof | playful | drill-slide | T09 push-through | power3.in | right | yellow+ink | locked | cut-paper drill, cross-out strip |  |  |  |
| 26 | 2:32.6 | 6.1 | proof | warm | frame-hang | motif:cut | sine.out | down | cream+ink+yellow | push-in | wall, framed family photo, house |  |  | we come out through the drilled hole onto the wall |
| 27 | 2:38.7 | 3.7 | proof | calm | shrink-to-label | T06 type-carry | power2.inOut | out | yellow+ink | pull-back | drill shrinks to an ARAÇ tag |  |  |  |
| 28 | 2:42.4 | 3.3 | proof | bold | title-callback | motif:cut | expo.out | in | yellow+ink | locked | SATIŞIN YENİ TANIMI tag |  |  | surprise: the episode title returns, now as the answer |
| 29 | 2:45.7 | 6.0 | proof | bold | arrows-tear | T14 text-mask | power3.out | left | ink+yellow | locked | takas arrows torn, DÖNÜŞÜM sanatı |  |  |  |
| 30 | 2:51.7 | 7.8 | proof | trustworthy | cliffs-rise | motif:cut | power2.out | up | yellow+ink+cream | locked | left cliff with MEVCUT DURUM labels (acı/problem/eksiklik) | kesik kâğıt köprü |  | the proof moment begins |
| 31 | 2:59.5 | 8.0 | proof | trustworthy | cliff-pan | motif:cut | power3.inOut | left | yellow+ink+cream | pan right | right cliff with ARZULANAN DURUM labels (kâr/verimlilik/ciro) |  |  | surprise: the camera pans across the gap to the other shore |
| 32 | 3:07.5 | 1.9 | proof | bold | road-unroll-bridge | motif:cut | expo.out | right | yellow+ink | pull-back | road strip unrolls between the cliffs |  |  | surprise: on 'köprü kurmak' the bridge unrolls in one move |
| 33 | 3:09.4 | 5.5 | proof | trustworthy | label-pin | motif:cut | power2.inOut | right | yellow+ink | locked | bridge label ÜRÜN / HİZMET, set-square, MİMAR: SEN credit |  |  |  |
| 34 | 3:14.9 | 11.1 | proof | warm | toll-drop | coin-carry | back.out(1.3) | down | yellow+ink+rust | locked | toll booth ₺, customer disc crossing |  |  | surprise: the customer disc rolls across and drops a coin happily ('seve seve') |
| 35 | 3:26.0 | 8.3 | proof | mysterious | crumble-down | T21 freeze-rewind | power2.in | down | cream+ink | tilt down | cement sack, TEKNİK ÖZELLİKLER strips, closed ear |  |  | surprise: the frame freezes and rewinds, then sinks below the bridge into the cement |
| 36 | 3:34.3 | 8.5 | proof | mysterious | ear-fold | motif:cut | power2.inOut | in | cream+ink | locked | spec strips pile up, the listener's paper ear folds shut |  |  | surprise: the ear folds shut |
| 37 | 3:42.8 | 6.1 | chapter | playful | gum-stretch | motif:cut | sine.inOut | right | cream+ink+yellow | locked | DEĞER stretched like chewing gum |  |  | surprise: the gum bubble pops on 'laf' |
| 38 | 3:48.9 | 11.9 | problem | bold | trophy-pile | T11 dolly-out | power2.out | up | cream+ink | locked | trophies, KURULUŞ plaque, office window, swept away |  |  |  |
| 39 | 4:00.8 | 4.1 | turn | trustworthy | serif-swap | motif:cut | power3.out | left | yellow+ink | locked | DEĞİŞTİRDİĞİN line |  |  | surprise: the serif word swaps in the middle of the sentence |
| 40 | 4:04.9 | 6.3 | proof | calm | split-open | T12 parallax-slide | power1.inOut | right | cream+ink | locked | ESKİ KAFA / DEĞER ODAKLI split |  |  | surprise: the frame splits into old vs new |
| 41 | 4:11.2 | 7.8 | proof | playful | feature-pour | motif:cut | power4.out | down | cream+ink | locked | feature strips pouring from a mouth |  |  |  |
| 42 | 4:19.0 | 8.8 | proof | playful | bla-flip | T04 beat-cut-hold | steps(3) | radial | rust+cream | shake | BLA BLA BLA strips, PARA VER |  |  | surprise: colour event 2, every feature turns into 'bla' and then one rust PARA VER |
| 43 | 4:27.8 | 8.9 | proof | trustworthy | calendar-unfold | motif:cut | power2.out | left | cream+ink+yellow | locked | month strip, 3 overtime day blocks, tired team discs | takvim sıkıştırma |  |  |
| 44 | 4:36.7 | 3.7 | proof | warm | team-droop | motif:cut | sine.inOut | down | cream+ink+rust | locked | tired team discs droop, maliyet coin |  |  | surprise: the whole team droops at once |
| 45 | 4:40.4 | 3.6 | proof | bold | squeeze | T02 match-cut-motion | expo.inOut | in | yellow+ink | locked | 3 days squeezed into 3 hours |  |  | surprise: three day blocks squeeze into one thin 3-hour sliver |
| 46 | 4:44.0 | 8.5 | proof | warm | give-back | motif:cut | back.out(1.2) | up | cream+ink+yellow | locked | day blocks fly back to the team, scissors cut budget strip %80 |  |  |  |
| 47 | 4:52.5 | 2.3 | proof | mysterious | question-hold | T18 ink-bleed | power2.inOut | radial | ink+cream | locked | BU SİZİN İÇİN NE İFADE EDER? |  |  | surprise: the question holds alone on ink |
| 48 | 4:54.8 | 7.6 | proof | trustworthy | table-set | motif:cut | power2.out | right | cream+ink+yellow | locked | ÜRÜN vs ZAMAN · PARA · HUZUR, table strip, SONUÇ card |  |  | the product box slides off, SONUÇ is set on the table |
| 49 | 5:02.4 | 8.0 | proof | trustworthy | box-slide-off | motif:cut | power2.in | right | yellow+ink | locked | product box slides off the table, SONUÇ set down |  |  | surprise: the product leaves the table |
| 50 | 5:10.4 | 7.2 | chapter | playful | disc-mirror | T15 focal-iris | power2.out | left | yellow+ink | locked | discs pointing at themselves: BENCİL |  |  | surprise: a crowd of discs all point at themselves |
| 51 | 5:17.6 | 5.1 | problem | bold | push-off | motif:cut | power4.in | right | cream+ink | locked | HEDEF / KOTA / AY SONU papers pushed off |  |  |  |
| 52 | 5:22.7 | 6.9 | problem | warm | zigzag-throb | T08 line-to-horizon | sine.inOut | radial | yellow+ink+rust | locked | head disc with zigzag headache strip, two-tone capsule |  |  | surprise: the capsule lands and the zigzag relaxes into a flat line |
| 53 | 5:29.6 | 6.2 | problem | urgent | noise-jitter | motif:cut | steps(12) | out | ink+cream | shake | jittering noise strips, GÜRÜLTÜ |  |  | surprise: the whole frame turns to jittering noise |
| 54 | 5:35.8 | 8.6 | turn | trustworthy | tray-cross | T19 grid-dissolve | power2.inOut | left | cream+ink | locked | tray crossed out, ÇARE key |  |  |  |
| 55 | 5:44.4 | 7.7 | proof | playful | stetho-draw | motif:cut | power3.out | down | cream+ink+rust | locked | stethoscope strip, strawberry pill gag crossed |  |  | surprise: 'tadı çilekli' pill pops up and gets crossed |
| 56 | 5:52.1 | 7.0 | proof | trustworthy | question-cards | T05 object-carry | power2.out | right | cream+ink | locked | question cards → TEŞHİS stamp → reçete pad | reçete defteri |  | surprise: TEŞHİS stamp slams onto the pad |
| 57 | 5:59.1 | 6.2 | proof | bold | step-numbers | motif:cut | expo.out | up | yellow+ink | locked | 1 TEŞHİS → 2 TEDAVİ |  |  |  |
| 58 | 6:05.3 | 6.5 | proof | playful | rx-tear | tear-tumble | power2.in | down | cream+ink+rust | locked | reçete without teşhis torn, AYAKÇI |  |  | surprise: the prescription tears itself in half |
| 59 | 6:11.8 | 3.4 | sting | bold | road-wipe-2 | motif:sting-wipe | power2.inOut | left | yellow+ink | locked | official logo, paper road strip |  |  | music sting (runs the other way) |
| 60 | 6:15.2 | 5.5 | chapter | calm | toolbox-slide | motif:cut | power1.inOut | right | cream+ink | locked | toolbox crossed, ZİHNİYET head profile |  |  |  |
| 61 | 6:20.7 | 6.2 | turn | warm | sunrise | T06 type-carry | sine.out | up | yellow+ink | locked | motif:morning alarm clock, sun disc, KİME YARDIM EDECEĞİM? |  |  | motif:morning returns changed: same clock, new question; surprise: the clock from 1:34 rings again |
| 62 | 6:26.9 | 4.6 | turn | playful | heart-pop | motif:cut | back.out(1.8) | radial | cream+rust | locked | small paper hearts, POLLYANNA, wink |  |  | surprise: hearts pop out on 'Pollyanna' |
| 63 | 6:31.5 | 7.3 | proof | trustworthy | bars-rise | T11 dolly-out | power3.out | up | cream+ink+yellow | locked | paper bars: problems solved vs money (no numbers) |  |  |  |
| 64 | 6:38.8 | 8.3 | proof | calm | car-to-horizon | motif:cut | power1.inOut | right | yellow+ink | pull-back | paper car strip → horizon, VİZYON |  |  | surprise: the car drives into a sunrise horizon |
| 65 | 6:47.1 | 9.4 | proof | bold | coil-tense | T10 whip-pan | expo.in | left | ink+rust | shake | coiled spring, RED stamp, PARAMI ALAMADIM |  |  |  |
| 66 | 6:56.5 | 12.7 | proof | calm | stamp-bounce | motif:cut | power2.out | right | cream+ink+yellow | locked | RED stamp bounces off, patient queue moves on |  |  | surprise: the RED stamp bounces off and the queue just moves |
| 67 | 7:09.2 | 15.3 | proof | bold | posture-snap | T20 glass-refraction | power4.out | up | yellow+ink | locked | hunched paper figure → upright İŞ ORTAĞI |  |  | surprise: the figure straightens up in one snap |
| 68 | 7:24.5 | 8.1 | cta | warm | envelope-slide | motif:cut | power2.out | left | cream+ink | locked | ÖDEV credit, phone + mail paper icons |  |  | surprise: an ÖDEV stamp lands |
| 69 | 7:32.6 | 1.8 | cta | bold | hard-stop | T15 focal-iris | expo.out | in | ink+yellow | locked | ÜRÜNÜNDEN HİÇ BAHSETME, taped box |  |  | surprise: hard stop, one line on ink |
| 70 | 7:34.4 | 7.3 | cta | warm | road-unroll | motif:cut | power2.inOut | right | yellow+ink | locked | motif:road DÜNYASI → SORUNU → UMUTLU GELECEK |  |  |  |
| 71 | 7:41.7 | 5.9 | cta | calm | shield-lower | T12 parallax-slide | sine.inOut | down | cream+ink | locked | paper shield lowering |  |  | surprise: the shield drops |
| 72 | 7:47.6 | 9.5 | cta | trustworthy | tabs-rise | motif:cut | power3.out | up | yellow+ink | locked | CESARET · SEBEP · ARAÇ tabs |  |  |  |
| 73 | 7:57.1 | 5.6 | cta | celebratory | net-tear-flood | T03 graphic-match-color | expo.out | out | yellow+ink+rust | push-in | PARA AVCISI net torn, DEĞER YARATICISI credits |  |  | surprise: colour event 3, the net tears and yellow floods: the one message |
| 74 | 8:02.7 | 3.4 | sting | bold | road-wipe-3 | motif:sting-wipe | power2.inOut | right | yellow+ink | locked | official logo, paper road strip |  |  |  |
| 75 | 8:06.1 | 6.6 | outro | celebratory | brick-stack | motif:cut | steps(10) | up | cream+ink+yellow | locked | bricks stacking into a castle | tuğla kale |  | surprise: the castle completes in stop-motion |
| 76 | 8:12.7 | 7.8 | outro | mysterious | scalpel-cut | T01 match-cut-shape | power3.inOut | right | ink+cream | locked | SIRADA: KEŞİF, scalpel line |  |  | surprise: the scalpel cuts one clean line |
| 77 | 8:20.5 | 5.9 | outro | warm | logo-settle | end | power2.out | in | yellow+ink | locked | official logo, SATIŞTA KAL · ZİNDE KAL |  |  | last 1.5 s holds still |
<!--/LEDGER-->

## The seven questions (answered)
1. **What and how:** the sentence above. Cut paper in the brand's yellow and ink: hand-made, bold and slightly funny, which suits a host talking straight to one person.
2. **Repeats:** see the audit run below. Deliberate repeats are the four motifs above.
3. **Transition meaning:** *tear-tumble*: the old story is literally torn up. *product-shape mask*: Season 2 opens through the logo. *push-through*: we go into the drilled hole and come out on the wall with the family photo (the result, not the drill). *coin-carry*: the coin travels into the toll booth, so the price is paid willingly. *freeze & rewind*: the speaker stops the bridge story to dig into its cement. *line-to-horizon*: the headache zigzag calms into a flat line. *graphic-match colour*: the yellow of the torn net floods into the message.
4. **Colour over time:** yellow chapters (warm, the show's own colour) alternate with an ink chapter (honest talk, "Değişken Denklem") and cream chapters (examples, the doctor). Rust appears only for money pressure and alarm, and leads in exactly three colour events.
5. **New components:** *başardım maskesi* (paper masks that flip on together), *süslü örtü şeritleri* (euphemism strips that grow frills while covering the word SATIŞ), *yapışkan satıcı kuklası* (a cut-paper puppet that comes back down the chimney), *görünmez duvar* (dashed-outline bricks), *kesik kâğıt köprü* (the proof moment: two cliffs, a road strip unrolling, a toll booth), *takvim sıkıştırma* (three overtime days squeezed into a three-hour sliver), *reçete defteri* (a diagnosis-first prescription pad), *tuğla kale* (a stop-motion brick castle).
6. **Surprise:** about every 10–18 s (rows marked `surprise:`), and always tied to a word the speaker says.
7. **Last film:** no history file yet (`~/.motion-ledger.json` is empty); this is the first film in the ledger.

## Frames (one key frame per chapter, see `sketches/`)

### 1 · Aile yemeği (0:00–0:40)
- key visual: a top-down cut-paper dinner table; every head disc flips a "BEN BAŞARDIM" mask on.
- words: "Eee, sen ne iştesin şimdi?" · "BEN SATIŞÇIYIM" · the three euphemisms.

### 2 · Yanlış hikâye (0:40–1:23)
- key visual: the sticky-salesman puppet with labels, then the poster tears; the official logo opens Season 2.
- words: YANLIŞ BİR HİKÂYE · YIRTIP ATIYORUZ · SATIŞIN YENİ TANIMI.

### 3 · Değişken Denklem (1:23–2:10)
- key visual: SATIŞ = PARA ALMAK on ink; dollar eyes and the invisible wall; the rust alarm.

### 4 · Matkap & köprü (2:10–3:43) · proof moment
- key visual: **the bridge**. MEVCUT DURUM (acı · problem · eksiklik) → road strip unrolls → ARZULANAN DURUM (kâr · verimlilik · ciro). MİMAR: SEN, toll booth ₺ = fiyat.

### 5 · Değer (3:43–5:10)
- key visual: the split. ESKİ KAFA pours feature strips that become BLA BLA BLA / PARA VER; DEĞER ODAKLI squeezes 3 GÜN into 3 SAAT and gives the days back.

### 6 · Satışın doktoru (5:10–6:15)
- key visual: headache zigzag + capsule; question cards → TEŞHİS → reçete. ÖNCE TEŞHİS, SONRA TEDAVİ.

### 7 · Zihniyet (6:15–7:24)
- key visual: the morning clock again with "BEN BUGÜN KİME YARDIM EDECEĞİM?"; the hunched figure straightens into an İŞ ORTAĞI.

### 8 · Ödev (7:24–8:06)
- key visual: ÜRÜNÜNDEN HİÇ BAHSETME; CESARET · SEBEP · ARAÇ; **SEN PARA AVCISI DEĞİLSİN, SEN DEĞER YARATICISISIN.**

### 9 · Kapanış (8:06–8:26)
- key visual: a brick castle built in stop-motion; SIRADA: KEŞİF; the official logo with "Satışta kal, zinde kal."

# Source of truth for the shot ledger. Writes the ledger table into STORYBOARD.md.
# (start, beat, tone, entrance, transition_out, ease, direction, palette, camera, components, new_component, sfx, notes)
R = [
# --- 1 · Aile yemeği (yellow) ---
(0.0,  "hook","warm","eyelid-bars-open","motif:cut","power2.inOut","out","yellow+ink","locked","eyelid strips, credit caption","","","the frame opens like an eye: 'gözünün önüne getir'"),
(5.3,  "hook","warm","slide-snap-left","push-down","power2.out","right","yellow+ink+cream","top-down","paper dinner table, plate discs, head discs","","","AİLE YEMEĞİ · YILLAR SONRA credits"),
(10.7, "hook","playful","mask-flip-row","T05 object-carry","back.out(1.4)","up","cream+ink","locked","head discs","başardım maskesi","","surprise: every head flips a 'BEN BAŞARDIM' mask on the same word"),
(18.4, "hook","bold","bubble-pop","T09 push-through","expo.out","in","ink+yellow","push-in","speech bubble, jaunty words","","","the question slams in word by word"),
(22.1, "hook","mysterious","breath-scale","motif:cut","sine.inOut","radial","yellow+ink","slow push","chest disc, BEN SATIŞÇIYIM","","","surprise: the big word holds still for a breath before 'diyebiliyor musun?'"),
(27.1, "hook","playful","strip-cover-stack","T06 type-carry","power3.out","left","cream+ink","locked","euphemism strips covering SATIŞ","süslü örtü şeritleri","","the three euphemisms slide over the word; surprise: the strips grow frilly scalloped edges on 'süslü'"),
# --- 2 · Yanlış hikâye ---
(40.7, "problem","warm","knot-tie","motif:cut","power1.inOut","radial","yellow+ink","locked","SATIŞ strip tied in a knot, many small discs","","","'boğazında düğümleniyorsa' → 'yalnız değilsin': discs gather round; surprise: the word SATIŞ ties itself into a knot"),
(46.8, "problem","mysterious","book-open","slide-push","power2.out","left","ink+cream","locked","paper storybook cover","","","YANLIŞ BİR HİKÂYE"),
(50.1, "problem","playful","puppet-build","tear-tumble","steps(6)","down","rust+ink+cream","locked","sticky-salesman puppet, label tags","yapışkan satıcı kuklası","","surprise: kicked out of the door, he drops back in down the chimney"),
(60.7, "turn","bold","tear-tumble","T13 product-shape-mask","power2.in","down","yellow+ink","shake","torn poster halves","","","surprise: the whole poster tears in two and tumbles off: 'yırtıp atıyoruz'"),
(65.4, "reveal","bold","logo-mask-open","T03 graphic-match-color","expo.out","in","yellow+ink","locked","official logo, SEZON 2 credit, wallet→head swap","","","the logo opens through its own shape; 'cüzdanı değil, zihniyeti'"),
(72.5, "reveal","trustworthy","card-flip","motif:cut","power2.inOut","up","cream+ink","locked","OLDUĞU / OLMASI GEREKEN cards","","","strike-through on 'olduğu'"),
(78.2, "reveal","warm","title-card-jaunty","T16 split-stack","power4.out","left","yellow+ink","locked","SATIŞIN YENİ TANIMI title card","","","surprise: full title card, the episode name, holds for 'Tekrar hoş geldin'"),
# --- 3 · Değişken Denklem (ink) ---
(82.8, "chapter","bold","split-strips-in","motif:cut","expo.inOut","right","ink+yellow","locked","DEĞİŞKEN DENKLEM card, SATIŞ = ? equation","","","dark ground: honest talk"),
(90.2, "problem","technical","coin-drop","T02 match-cut-motion","power4.out","down","ink+yellow+rust","locked","equation, paper coin","","","the ? becomes a coin: SATIŞ = PARA ALMAK; surprise: the ? drops as a coin"),
(94.1, "problem","playful","alarm-ring","motif:cut","steps(8)","right","yellow+ink","locked","alarm clock disc, tie strip, pocket→safe dotted transfer","","","motif:morning (first time: whose money can I move?)"),
(102.1,"problem","bold","hand-cup-rise","T17 paper-fold","power3.inOut","up","ink+cream","locked","cupped paper hand, MODERN DİLENCİ","","","surprise: the handkerchief folds into a brochure: 'mendil yerine broşür'"),
(110.9, "problem","bold","type-slam","T10 whip-pan","expo.out","left","cream+ink","locked","İNSANLAR APTAL DEĞİL","","",""),
(115.4,"problem","mysterious","eye-dollar-blink","motif:cut","power2.in","radial","ink+cream","slow push","dollar eyes, invisible dashed wall bricks","görünmez duvar","","bricks appear as dashed outlines, one per beat; surprise: dollar signs blink into both eyes"),
(121.2,"problem","urgent","alarm-flood","T04 beat-cut-hold","steps(2)","out","rust+ink","shake","siren discs, SAVAŞ YA DA KAÇ","","","surprise: colour event 1, rust floods the frame and flashes"),
(127.6,"sting","bold","road-wipe","motif:sting-wipe","power2.inOut","right","yellow+ink","locked","official logo, paper road strip","","","music sting: the road strip wipes the frame; surprise: medium change, the road strip wipes the screen"),
# --- 4 · Matkap & köprü (yellow) ---
(130.7,"turn","calm","credit-type-on","motif:cut","power1.out","left","yellow+ink","locked","GERÇEK ŞU credit, SEZON 1 tag","","",""),
(137.9,"turn","playful","split-halves","T05 object-carry","power2.out","left","cream+ink+yellow","locked","NEFRET EDER / BAYILIR halves","","","surprise: the frame splits in two"),
(144.6,"turn","bold","puzzle-snap","motif:cut","back.out(1.6)","in","yellow+ink","locked","paradox halves snapping together","","","surprise: the two halves lock like puzzle pieces"),
(148.3,"proof","playful","drill-slide","T09 push-through","power3.in","right","yellow+ink","locked","cut-paper drill, cross-out strip","","",""),
(152.6,"proof","warm","frame-hang","motif:cut","sine.out","down","cream+ink+yellow","push-in","wall, framed family photo, house","","","we come out through the drilled hole onto the wall"),
(158.7,"proof","calm","shrink-to-label","T06 type-carry","power2.inOut","out","yellow+ink","pull-back","drill shrinks to an ARAÇ tag","","",""),
(162.4,"proof","bold","title-callback","motif:cut","expo.out","in","yellow+ink","locked","SATIŞIN YENİ TANIMI tag","","","surprise: the episode title returns, now as the answer"),
(165.7,"proof","bold","arrows-tear","T14 text-mask","power3.out","left","ink+yellow","locked","takas arrows torn, DÖNÜŞÜM sanatı","","",""),
(171.7,"proof","trustworthy","cliffs-rise","motif:cut","power2.out","up","yellow+ink+cream","locked","left cliff with MEVCUT DURUM labels (acı/problem/eksiklik)","kesik kâğıt köprü","","the proof moment begins"),
(179.5,"proof","trustworthy","cliff-pan","motif:cut","power3.inOut","left","yellow+ink+cream","pan right","right cliff with ARZULANAN DURUM labels (kâr/verimlilik/ciro)","","","surprise: the camera pans across the gap to the other shore"),
(187.5,"proof","bold","road-unroll-bridge","motif:cut","expo.out","right","yellow+ink","pull-back","road strip unrolls between the cliffs","","","surprise: on 'köprü kurmak' the bridge unrolls in one move"),
(189.4,"proof","trustworthy","label-pin","motif:cut","power2.inOut","right","yellow+ink","locked","bridge label ÜRÜN / HİZMET, set-square, MİMAR: SEN credit","","",""),
(194.9,"proof","warm","toll-drop","coin-carry","back.out(1.3)","down","yellow+ink+rust","locked","toll booth ₺, customer disc crossing","","","surprise: the customer disc rolls across and drops a coin happily ('seve seve')"),
(206.0,"proof","mysterious","crumble-down","T21 freeze-rewind","power2.in","down","cream+ink","tilt down","cement sack, TEKNİK ÖZELLİKLER strips, closed ear","","","surprise: the frame freezes and rewinds, then sinks below the bridge into the cement"),
(214.3,"proof","mysterious","ear-fold","motif:cut","power2.inOut","in","cream+ink","locked","spec strips pile up, the listener's paper ear folds shut","","","surprise: the ear folds shut"),
# --- 5 · Değer (cream) ---
(222.8,"chapter","playful","gum-stretch","motif:cut","sine.inOut","right","cream+ink+yellow","locked","DEĞER stretched like chewing gum","","","surprise: the gum bubble pops on 'laf'"),
(228.9,"problem","bold","trophy-pile","T11 dolly-out","power2.out","up","cream+ink","locked","trophies, KURULUŞ plaque, office window, swept away","","",""),
(240.8,"turn","trustworthy","serif-swap","motif:cut","power3.out","left","yellow+ink","locked","DEĞİŞTİRDİĞİN line","","","surprise: the serif word swaps in the middle of the sentence"),
(244.9,"proof","calm","split-open","T12 parallax-slide","power1.inOut","right","cream+ink","locked","ESKİ KAFA / DEĞER ODAKLI split","","","surprise: the frame splits into old vs new"),
(251.2, "proof","playful","feature-pour","motif:cut","power4.out","down","cream+ink","locked","feature strips pouring from a mouth","","",""),
(259.0,"proof","playful","bla-flip","T04 beat-cut-hold","steps(3)","radial","rust+cream","shake","BLA BLA BLA strips, PARA VER","","","surprise: colour event 2, every feature turns into 'bla' and then one rust PARA VER"),
(267.8,"proof","trustworthy","calendar-unfold","motif:cut","power2.out","left","cream+ink+yellow","locked","month strip, 3 overtime day blocks, tired team discs","takvim sıkıştırma","",""),
(276.7,"proof","warm","team-droop","motif:cut","sine.inOut","down","cream+ink+rust","locked","tired team discs droop, maliyet coin","","","surprise: the whole team droops at once"),
(280.4,"proof","bold","squeeze","T02 match-cut-motion","expo.inOut","in","yellow+ink","locked","3 days squeezed into 3 hours","","","surprise: three day blocks squeeze into one thin 3-hour sliver"),
(284.0,"proof","warm","give-back","motif:cut","back.out(1.2)","up","cream+ink+yellow","locked","day blocks fly back to the team, scissors cut budget strip %80","","",""),
(292.5,"proof","mysterious","question-hold","T18 ink-bleed","power2.inOut","radial","ink+cream","locked","BU SİZİN İÇİN NE İFADE EDER?","","","surprise: the question holds alone on ink"),
(294.8,"proof","trustworthy","table-set","motif:cut","power2.out","right","cream+ink+yellow","locked","ÜRÜN vs ZAMAN · PARA · HUZUR, table strip, SONUÇ card","","","the product box slides off, SONUÇ is set on the table"),
(302.4,"proof","trustworthy","box-slide-off","motif:cut","power2.in","right","yellow+ink","locked","product box slides off the table, SONUÇ set down","","","surprise: the product leaves the table"),
# --- 6 · Doktor ---
(310.4,"chapter","playful","disc-mirror","T15 focal-iris","power2.out","left","yellow+ink","locked","discs pointing at themselves: BENCİL","","","surprise: a crowd of discs all point at themselves"),
(317.6, "problem","bold","push-off","motif:cut","power4.in","right","cream+ink","locked","HEDEF / KOTA / AY SONU papers pushed off","","",""),
(322.7,"problem","warm","zigzag-throb","T08 line-to-horizon","sine.inOut","radial","yellow+ink+rust","locked","head disc with zigzag headache strip, two-tone capsule","","","surprise: the capsule lands and the zigzag relaxes into a flat line"),
(329.6,"problem","urgent","noise-jitter","motif:cut","steps(12)","out","ink+cream","shake","jittering noise strips, GÜRÜLTÜ","","","surprise: the whole frame turns to jittering noise"),
(335.8,"turn","trustworthy","tray-cross","T19 grid-dissolve","power2.inOut","left","cream+ink","locked","tray crossed out, ÇARE key","","",""),
(344.4,"proof","playful","stetho-draw","motif:cut","power3.out","down","cream+ink+rust","locked","stethoscope strip, strawberry pill gag crossed","","","surprise: 'tadı çilekli' pill pops up and gets crossed"),
(352.1,"proof","trustworthy","question-cards","T05 object-carry","power2.out","right","cream+ink","locked","question cards → TEŞHİS stamp → reçete pad","reçete defteri","","surprise: TEŞHİS stamp slams onto the pad"),
(359.1,"proof","bold","step-numbers","motif:cut","expo.out","up","yellow+ink","locked","1 TEŞHİS → 2 TEDAVİ","","",""),
(365.3,"proof","playful","rx-tear","tear-tumble","power2.in","down","cream+ink+rust","locked","reçete without teşhis torn, AYAKÇI","","","surprise: the prescription tears itself in half"),
(371.8,"sting","bold","road-wipe-2","motif:sting-wipe","power2.inOut","left","yellow+ink","locked","official logo, paper road strip","","","music sting (runs the other way)"),
# --- 7 · Zihniyet ---
(375.2,"chapter","calm","toolbox-slide","motif:cut","power1.inOut","right","cream+ink","locked","toolbox crossed, ZİHNİYET head profile","","",""),
(380.7,"turn","warm","sunrise","T06 type-carry","sine.out","up","yellow+ink","locked","motif:morning alarm clock, sun disc, KİME YARDIM EDECEĞİM?","","","motif:morning returns changed: same clock, new question; surprise: the clock from 1:34 rings again"),
(386.9,"turn","playful","heart-pop","motif:cut","back.out(1.8)","radial","cream+rust","locked","small paper hearts, POLLYANNA, wink","","","surprise: hearts pop out on 'Pollyanna'"),
(391.5,"proof","trustworthy","bars-rise","T11 dolly-out","power3.out","up","cream+ink+yellow","locked","paper bars: problems solved vs money (no numbers)","","",""),
(398.8,"proof","calm","car-to-horizon","motif:cut","power1.inOut","right","yellow+ink","pull-back","paper car strip → horizon, VİZYON","","","surprise: the car drives into a sunrise horizon"),
(407.1, "proof","bold","coil-tense","T10 whip-pan","expo.in","left","ink+rust","shake","coiled spring, RED stamp, PARAMI ALAMADIM","","",""),
(416.5,"proof","calm","stamp-bounce","motif:cut","power2.out","right","cream+ink+yellow","locked","RED stamp bounces off, patient queue moves on","","","surprise: the RED stamp bounces off and the queue just moves"),
(429.2,"proof","bold","posture-snap","T20 glass-refraction","power4.out","up","yellow+ink","locked","hunched paper figure → upright İŞ ORTAĞI","","","surprise: the figure straightens up in one snap"),
# --- 8 · Ödev ---
(444.5,"cta","warm","envelope-slide","motif:cut","power2.out","left","cream+ink","locked","ÖDEV credit, phone + mail paper icons","","","surprise: an ÖDEV stamp lands"),
(452.6,"cta","bold","hard-stop","T15 focal-iris","expo.out","in","ink+yellow","locked","ÜRÜNÜNDEN HİÇ BAHSETME, taped box","","","surprise: hard stop, one line on ink"),
(454.4,"cta","warm","road-unroll","motif:cut","power2.inOut","right","yellow+ink","locked","motif:road DÜNYASI → SORUNU → UMUTLU GELECEK","","",""),
(461.7,"cta","calm","shield-lower","T12 parallax-slide","sine.inOut","down","cream+ink","locked","paper shield lowering","","","surprise: the shield drops"),
(467.6,"cta","trustworthy","tabs-rise","motif:cut","power3.out","up","yellow+ink","locked","CESARET · SEBEP · ARAÇ tabs","","",""),
(477.1,"cta","celebratory","net-tear-flood","T03 graphic-match-color","expo.out","out","yellow+ink+rust","push-in","PARA AVCISI net torn, DEĞER YARATICISI credits","","","surprise: colour event 3, the net tears and yellow floods: the one message"),
(482.7,"sting","bold","road-wipe-3","motif:sting-wipe","power2.inOut","right","yellow+ink","locked","official logo, paper road strip","","",""),
# --- 9 · Kapanış ---
(486.1,"outro","celebratory","brick-stack","motif:cut","steps(10)","up","cream+ink+yellow","locked","bricks stacking into a castle","tuğla kale","","surprise: the castle completes in stop-motion"),
(492.7,"outro","mysterious","scalpel-cut","T01 match-cut-shape","power3.inOut","right","ink+cream","locked","SIRADA: KEŞİF, scalpel line","","","surprise: the scalpel cuts one clean line"),
(500.5,"outro","warm","logo-settle","end","power2.out","in","yellow+ink","locked","official logo, SATIŞTA KAL · ZİNDE KAL","","","last 1.5 s holds still"),
]
END = 506.4
cols = ["#","start","dur","beat","tone","entrance","transition_out","ease","direction","palette","camera","components","new_component","sfx","notes"]
def mmss(t): return f"{int(t//60)}:{t%60:04.1f}"
lines = ["| " + " | ".join(cols) + " |", "|" + "---|"*len(cols)]
for i,r in enumerate(R):
    st = r[0]; en = R[i+1][0] if i+1 < len(R) else END
    lines.append("| " + " | ".join([str(i+1), mmss(st), f"{en-st:.1f}"] + [x for x in r[1:]]) + " |")
if __name__ == "__main__":
    import sys
    p = sys.argv[1]; txt = open(p).read()
    a = txt.index("<!--LEDGER-->"); b = txt.index("<!--/LEDGER-->")
    open(p,"w").write(txt[:a] + "<!--LEDGER-->\n" + "\n".join(lines) + "\n" + txt[b:])

---
workflow: general-video        # long narrated companion piece, the user's own VO drives the timing
format: 1920x1080
duration: 506.4s               # = length of the voice recording (8:26.4)
audio: voice                   # the user's own recording, assets/audio/bolum-ses.mp3
loop: false
theme: "087 Cut-Paper Title Sequence"
---

# Satış Yolculuğu: Satışın Yeni Tanımı

**One message:** "Sen para avcısı değilsin, sen değer yaratıcısısın."

**Audience & channel:** salespeople and people who are embarrassed to say "satışçıyım". YouTube, 16:9, sound on (the voice carries the episode). The graphics run alongside the narration for the whole 8:26.

**Truth source:** the episode's transcript (`source/transcript.txt`) and recording. Every on-screen sentence is a quote or a shortened quote from the narration. The only numbers on screen are the ones in the narration (256-bit, 3 days → 3 hours, %80), shown as an example scenario.

**Proof moment:** the bridge. Mevcut durum (acı, problem) → köprü (ürün/hizmet) → arzulanan durum (kâr, verimlilik, ciro). Sen köprünün mimarısın; geçiş ücreti fiyat.

**Chapter map** (aligned to the recording, `source/words.json`)
| # | time | chapter | key image |
|---|---|---|---|
| 1 | 0:00–0:41 | Aile yemeği | "Eee, sen ne iş yapıyorsun?" · masks · the euphemisms |
| 2 | 0:41–1:23 | Yanlış hikâye | the sticky salesman is torn up · Sezon 2 logo reveal |
| 3 | 1:23–2:08 | Değişken Denklem | money transfer · "modern dilenci" · the invisible wall + alarm |
| – | 2:08–2:10 | music sting | |
| 4 | 2:10–3:43 | Matkap & köprü | paradox · drill → family photo · **the bridge** · cement |
| 5 | 3:43–5:10 | Değer nedir? | old salesperson vs value-led salesperson · 3 days → 3 hours |
| 6 | 5:10–6:12 | Satışın doktoru | headache · pill · diagnosis before prescription |
| – | 6:12–6:15 | music sting | |
| 7 | 6:15–7:24 | Zihniyet | "Ben bugün kime yardım edeceğim?" · rejection · posture |
| 8 | 7:24–8:03 | Ödev | don't mention the product · **para avcısı → değer yaratıcısı** |
| – | 8:03–8:06 | music sting | |
| 9 | 8:06–8:26 | Kapanış | brick by brick: the sales castle · next: keşif · logo |

**Components:** all imaginary (no product UI). Brand: the official logo only, never redrawn.

**Brand:** logo `assets/img/logo-official.png` (+ ink cut-outs made from the same file) · yellow #FFFF00 (exactly the logo ground), ink #151413, cream #F4EEDC, one warm accent (rust #D9452B) for "danger/money" moments · Montserrat (latin-ext, local) as in the logo.

**Do / Don't:** Turkish uppercase is typed by hand (SATIŞ, İ), never CSS `text-transform`. No progress bars, no gradient text, no pure #000/#fff. No real people's likeness (Elon Musk is mentioned as words only). Fewer words: keywords, not subtitles.

**Deliverables:** `renders/satis-yolculugu-s2b1.mp4`, 1920×1080, with the original voice track.

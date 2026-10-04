---
workflow: general-video        # bir URL değil, bir bölüm metni sürüyor
format: 1080x1920              # dikey 9:16 · Reels / Shorts / TikTok
duration: 70s                  # 60–75 sn aralığı; kesin süre storyboard'da müziğe göre
audio: music                   # müzik + sıcak SFX, seslendirme yok
loop: false
theme: "085 Constructivist Agitprop"
---

# Satış Yolculuğu — bölüm fragmanı ("Satış bir köprüdür")

**One message:** Satış birinden para almak değil; dönüşüm yaratmaktır.

**Audience & channel:** Satışta çalışan ama "satışçıyım" demekte zorlanan profesyoneller, girişimciler, B2B ekipler. Dikey sosyal akış (Reels / Shorts / TikTok). Müzikli ama çoğu kişi sessiz izleyecek; hikâye müziksiz, sadece kısa kelimelerle de okunmalı.

**Truth source:** Satış Yolculuğu Sezon 2 açılış bölümünün transkripti (kullanıcının mesajı). Bütün cümleler, örnekler ve rakamlar (3 gün → 3 saat, %80) yalnızca buradan alınır. Bölümde geçmeyen hiçbir iddia, rakam ya da tanıklık eklenmez.

**Proof moment:** Köprü. Sol kıyıda müşterinin mevcut durumu (acı, problem, eksik), sağ kıyıda arzulanan durumu (kâr, verim, ciro). Aralarına köprü kurulur: köprü = ürün/hizmet, sen = mimar, geçiş ücreti = fiyat. Köprü kurulduğu an logodaki yola dönüşür; marka bu anda gelir.

**Beat taslağı (≈70 sn)**
| süre | beat | ekranda (az kelime) |
|---|---|---|
| 0–11 | Kanca: aile yemeği | "Eee, sen ne iş yapıyorsun?" → kaçamak cevaplar ("Pazarlama tarafındayım", "Müşteri ilişkileri…", "Ticari operasyonlar…"); "SATIŞÇIYIM" kelimesi boğazda düğümlenir |
| 11–22 | Eski hikâye | "kapıdan kovsan bacadan giren" satışçı afişi → yırtılır: "BU HİKÂYEYİ YIRTIYORUZ." |
| 22–33 | Dönüm | "Kimse matkap almak istemez." Matkap → duvardaki aile fotoğrafı |
| 33–52 | Kanıt: köprü | MEVCUT DURUM ↔ ARZULANAN DURUM, köprü kurulur; "Ürün = köprü · Sen = mimar · Fiyat = geçiş ücreti" |
| 52–62 | Sonuç | "Para avcısı değilsin. DEĞER YARATICISISIN." |
| 62–70 | Kapanış | Bölümün ödevi: "İLK GÖRÜŞMEDE ÜRÜNDEN HİÇ BAHSETME." + logo · son ~1 sn sabit |

**Components** (gerçek ürün arayüzü yok; hepsi hayali, bölümün metaforlarını çizer)
| Component | Real or imaginary | Notes |
|---|---|---|
| Yemek masası + konuşma balonu | imaginary | kanca; soru masanın öbür ucundan gelir |
| Kaçamak cevap kartları | imaginary | transkriptteki üç süslü cümle, birebir |
| "Satışçı" afişi | imaginary | eski hikâye; yırtılarak çıkar |
| Matkap → aile fotoğrafı | imaginary | araç vs sonuç |
| Köprü (iki kıyı) | imaginary | kanıt anı; logodaki yola dönüşür |
| Logo | real | yalnızca verilen resmi logo dosyası, yeniden çizilmez |

**Brand:** logo `assets/brand/satis-yolculugu-logo.png` (sarı zemin, siyah yol, SATIŞ / YOLCULUĞU) · renkler: sarı `#FFFF00` (logodan), mürekkep `#151412`, kâğıt `#F4EFE3` · font: Montserrat 400/600/800/900, `latin-ext` yerel olarak `assets/fonts/` içinde.

**Do / Don't:**
- Büyük harfli metin elle yazılır (SATIŞÇIYIM, DEĞER, İ/ı korunur); CSS `text-transform` yok.
- Logo çizilmez, değiştirilmez; sadece verilen dosya.
- İlerleme çubuğu, gradient yazı, saf #000/#fff yok (logo dosyası hariç).
- Her karede bir fikir; okunması gereken paragraf yok.

**Deliverables:** `renders/satis-yolculugu-s2-fragman-1080x1920.mp4` (4K'dan küçültülmüş), ayrıca 4K master.

**Kararlar:** "Sezon 2" ya da yayın bilgisi yazılmaz; ekrandaki her şey bölümün içeriğinden gelir. Ses: lisanslı parça yok, 120 BPM perküsif ritim + sıcak SFX.

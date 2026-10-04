# Satış Yolculuğu · SPIN Tekniği

Satış Yolculuğu podcast'inin SPIN tekniği bölümü için 1920×1080, 293,9 sn'lik video. Görsel, bölüm kaydını (`assets/voice.mp3`) takip eder.

- `BRIEF.md`: mesaj, kanal, bileşenler, marka
- `STORYBOARD.md`: ton cümlesi, ledger, geçişlerin anlamı
- `index.html`: kompozisyonun tamamı (tek GSAP timeline, seek-safe)

## Yol motifi
Markanın logosundaki S-yol filmin omurgası: açılışta logo, SPIN haritasında dört durağı taşıyan rota, CRM örneğinde müşterinin yürüdüğü yol, kapanışta maske olarak geri döner. Logo yeniden çizilmedi; resmî PNG'nin yalnızca sarı zemini şeffaflaştırıldı (`logo-ink.png`, `road-ink.png`).

## Yeni bileşenler
- **SPIN yol haritası**: logonun yolu, S → P → I → N durakları
- **Acı merceği**: mercek altında küçük bir nokta "SORUN"dan "KRİZ"e büyür
- **Eleme kapısı**: acı noktası olmayan fırsatlar I kapısında yoldan düşer, kalanlar Forecast kutusuna dizilir

## Zamanlama
Sahne zamanları bölüm kaydının otomatik transkripsiyonundan (Whisper small, cümle düzeyi) ve sessizlik analizinden alındı. Bir cümle birkaç yüz ms erken veya geç düşüyorsa `index.html` içindeki ilgili `IN(…, t, …)` saatini değiştirin.

## Komutlar
```bash
npx hyperframes@0.8.75 check
npx hyperframes@0.8.75 preview
npx hyperframes@0.8.75 render --quality high -o renders/spin-teknigi-1080-raw.mp4
../../tools/deliver.sh renders/spin-teknigi-1080-raw.mp4 1920x1080 renders/spin-teknigi-1920x1080.mp4
```

Fontlar: Montserrat, Instrument Serif, JetBrains Mono (SIL OFL 1.1). GSAP 3.14.2 yerel olarak `assets/js` altında.

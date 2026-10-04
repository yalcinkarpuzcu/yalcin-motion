# Satış Yolculuğu · Satışın Yeni Tanımı

Motion graphics for the whole 8:26 episode, 16:9, synced to the host's own recording. Theme 087 Cut-Paper Title Sequence in the Satış Yolculuğu brand (logo yellow `#FFFF00`, ink, cream, one rust accent).

- `BRIEF.md`: the brief and the chapter map
- `STORYBOARD.md`: message & tone, the 77-shot ledger (clean `variety_audit.py` run) and the seven questions
- `sketches/sheet.png`: the approved sketch sheet; `theme-stills/`: the three theme candidates
- `source/transcript.txt`: the script; `source/words.json`: word timings aligned to the recording
- `src/chN.html`: the nine chapters, with cue tokens like `{{w:köprü@188.4}}` (the start of a spoken word)
- `compositions/chN.html`: generated from `src/` by `python3 tools/build.py` (do not edit by hand)
- `tools/ledger.py`: writes the ledger into `STORYBOARD.md`; `tools/sfx.py`: synthesises the paper SFX track

## Rebuild and render

```bash
python3 tools/build.py          # resolve word cues → compositions/
python3 tools/sfx.py            # assets/audio/sfx.wav (git-ignored, regenerate)
npx hyperframes check
npx hyperframes render -o renders/raw-1080p.mp4 --quality delivery
```

Then normalise the mix to −14 LUFS for YouTube (see the deliver step in the kit's `tools/deliver.sh`).

The word timings came from Whisper (small) on silence-split chunks, aligned to the script with a sequence match (95 % of the words matched directly, and the rest were interpolated).

"""Workiom × Ali Raif İlaç: 45 s music + SFX mix, 120 BPM (beat 0.5 s, bar 2 s), C major / A minor.
Synthesised from scratch (no samples, no licences). Deterministic. Usage: python audio/build_mix.py"""
import os, sys
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools"))
import warm_sfx as W
SR = W.SR; DUR = 45.0; N = int(SR * DUR); BEAT = 0.5
F = {"C2":65.41,"G2":98.0,"A2":110.0,"F2":87.31,"C3":130.81,"E3":164.81,"G3":196.0,"A3":220.0,"F3":174.61,"B3":246.94,
     "C4":261.63,"D4":293.66,"E4":329.63,"F4":349.23,"G4":392.0,"A4":440.0,"B4":493.88,"C5":523.25,"D5":587.33,"E5":659.25,"G5":783.99,"C6":1046.5}
def put(buf, t, sig, gain=1.0):
    i = int(t * SR)
    if i >= len(buf): return
    s = sig[: len(buf) - i]; buf[i:i + len(s)] += s * gain
def pad(freqs, dur, gain=1.0, attack=0.6, release=0.8):
    n = int(SR * dur); t = np.arange(n) / SR; x = np.zeros(n)
    for k, f in enumerate(freqs):
        for d in (-0.15, 0.15):                       # slight detune = warmth, no beating hiss
            x += np.sin(2 * np.pi * (f + d) * t + k) + 0.25 * np.sin(2 * np.pi * 2 * (f + d) * t)
    e = np.clip(t / attack, 0, 1) * np.clip((dur - t) / release, 0, 1)
    return x * e / (len(freqs) * 4) * gain
def bass(f, dur=0.45):
    n = int(SR * dur); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * 2 * f * t)) * W.env(n, 0.006, dur / 2.2)

mus = np.zeros(N)
# chord per bar: C - Am - F - G (cycle), bar = 2 s
CH = {"C": (["C3","E3","G3"], "C2"), "Am": (["A3","C4","E4"], "A2"), "F": (["F3","A3","C4"], "F2"), "G": (["G3","B3","D4"], "G2")}
ARP = {"C": ["C5","E5","G5","E5"], "Am": ["A4","C5","E5","C5"], "F": ["F4","A4","C5","A4"], "G": ["G4","B4","D5","B4"]}
cyc = ["C", "Am", "F", "G"]
# --- 0-5 s: pain. low drone, sparse ticks, rising. 5-6 s: hold-frame = silence
put(mus, 0.0, pad(["C2" and F["C2"], F["G2"]], 5.0, 0.7, 0.4), 1.0)
for k, t in enumerate(np.arange(0.5, 5.0, 0.5)):
    put(mus, t, W.woodblock(800 + 40 * k, 0.1), 0.25 + 0.03 * k)
# --- 6-36 s: confident, trustworthy. bass on beats 1&3, arp on 8ths from 9 s, pad per bar
def bars(t0, t1, arp_from, arp_gain=0.35, pad_gain=0.9, bass_gain=0.8):
    t = t0; b = 0
    while t < t1 - 1e-6:
        c = cyc[b % 4]; fr, bs = CH[c]
        put(mus, t, pad([F[x] for x in fr], 2.2, pad_gain, 0.25, 0.9))
        for q in (0, 2): put(mus, t + q * BEAT, bass(F[bs]), bass_gain * (1 if q == 0 else 0.7))
        if t >= arp_from:
            for j in range(4):
                put(mus, t + j * BEAT, W.marimba(F[ARP[c][j]], 0.5, 0.3), arp_gain * (0.9 if j % 2 == 0 else 0.6))
        b += 1; t += 4 * BEAT
bars(6.0, 36.0, 9.0)
# the drop at 6.0: bright C major stab + sub
put(mus, 6.0, pad([F["C3"], F["E3"], F["G3"], F["C4"]], 2.4, 1.2, 0.02, 1.2))
# --- 36.0-36.5 s: one beat of silence (scale jump). cut everything after 36.0
mus[int(36.0 * SR):int(36.5 * SR)] *= 0
# --- 36.5-45 s: calm resolve, softer, arp thins out
bars(36.5, 45.0, 99, 0.0, 0.75, 0.5)
put(mus, 40.4, pad([F["C3"], F["E3"], F["G3"], F["C4"], F["E4"]], 4.6, 1.0, 0.05, 3.0))
# gentle ducking is done by the mix levels; fade the end
mus[int(43.3 * SR):] *= np.linspace(1, 0, N - int(43.3 * SR))
mus[:int(0.5*SR)] *= np.linspace(0, 1, int(0.5*SR))
mus = mus / np.abs(mus).max() * 0.55
# a pure silence in 5.0-6.0 (hold frame)
sil = slice(int(5.0 * SR), int(6.0 * SR)); mus[sil] *= np.linspace(1, 0, int(1.0 * SR)) ** 0.2 * 0  # hard cut, stays silent

# --- SFX (warm_sfx timbres) ---
sfx = np.zeros(N)
S = {"pop": W.marimba(F["G5"], .3, .5), "tick": W.woodblock(1100), "low": W.woodblock(760, .14),
     "confirm": W.seq((0, W.marimba(F["E5"], .4)), (.09, W.marimba(F["G5"], .5))),
     "reveal": W.seq((0, W.marimba(F["C5"], .6)), (.07, W.marimba(F["E5"], .6)), (.14, W.marimba(F["G5"], .7)), (.21, W.marimba(F["C6"], .9)))}
n = int(SR * 0.6); rng = np.random.default_rng(11)
nz = np.convolve(rng.standard_normal(n), np.ones(40) / 40, mode="same"); S["whoosh"] = nz * np.sin(np.pi * np.arange(n) / n) ** 2 * 1.6
for k, t in enumerate([0.1, 0.28, 0.46, 0.64]): put(sfx, t, S["tick"], 0.5)          # hook nodes
put(sfx, 3.2, S["pop"], 0.5)                                                           # packet dot
put(sfx, 6.02, S["reveal"], 0.9)                                                       # reveal
put(sfx, 8.4, S["whoosh"], 0.5)                                                        # push-through
for t in (10.4, 11.3, 12.2, 13.1): put(sfx, t, S["tick"], 0.5)                        # fields
put(sfx, 9.5, S["pop"], 0.45); put(sfx, 12.3, S["pop"], 0.4)                           # card, Mila
put(sfx, 17.3, S["whoosh"], 0.5)                                                       # object carry
for k in range(12): put(sfx, 19.0 + k * (2.6 / 12), S["tick"], 0.4)                    # counter steps
put(sfx, 22.0, S["whoosh"], 0.45); put(sfx, 22.0, S["pop"], 0.6)                        # 128 fills the frame
put(sfx, 23.4, S["pop"], 0.45); put(sfx, 23.6, S["pop"], 0.4)                          # 61 / 67
put(sfx, 25.5, S["whoosh"], 0.55)                                                      # focal iris
for k in range(12): put(sfx, 27.5 + k * (4.0 / 12), S["low"], 0.4)                     # clock hand 12 steps
put(sfx, 29.7, S["confirm"], 0.7)                                                      # row refuses to dim
put(sfx, 30.5, S["pop"], 0.45); put(sfx, 31.7, S["confirm"], 0.6)                      # record, human
put(sfx, 35.3, S["whoosh"], 0.6)                                                       # dolly-out
put(sfx, 38.5, S["whoosh"], 0.45)                                                      # type carry
put(sfx, 40.4, S["reveal"], 0.85)                                                      # the full stop (motif)
put(sfx, 41.6, S["confirm"], 0.55)                                                     # CTA button
sfx = W.room(sfx, 0.10)[:N]; sfx = sfx / np.abs(sfx).max() * 0.8

mix = mus * 0.6 + sfx * 0.7
mix = mix / np.abs(mix).max() * 0.89
os.makedirs(os.path.join(os.path.dirname(__file__), "..", "assets", "audio"), exist_ok=True)
out = os.path.join(os.path.dirname(__file__), "..", "assets", "audio", "mix.wav")
sf.write(out, np.stack([mix, mix], 1).astype(np.float32), SR)
sf.write(out.replace("mix.wav", "music.wav"), mus.astype(np.float32), SR)
print("wrote", out, len(mix) / SR, "s")

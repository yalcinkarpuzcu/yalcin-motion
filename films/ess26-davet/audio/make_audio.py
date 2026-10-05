"""Original 120 BPM bed + warm SFX for the ESS'26 invite film (synthesised, no samples, no licences).

Usage: python audio/make_audio.py audio/mix.wav
Deterministic: every noise source is seeded. Bars are 2 s; the drop is on 4.0 s.
Needs numpy + scipy.
"""
import sys
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

SR = 48000
LEN = 22.5
BEAT = 0.5
N = int(SR * LEN)


def hz(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def lp(x, f, order=2):
    return sosfilt(butter(order, f, "low", fs=SR, output="sos"), x)


def hp(x, f, order=2):
    return sosfilt(butter(order, f, "high", fs=SR, output="sos"), x)


def place(buf, t, sig, gain=1.0):
    i = int(t * SR)
    j = min(len(buf), i + len(sig))
    if i < len(buf):
        buf[i:j] += sig[: j - i] * gain


def tt(d):
    return np.arange(int(SR * d)) / SR


# ---------- instruments ----------
def kick(d=0.42):
    t = tt(d)
    f = 45 + 95 * np.exp(-t / 0.045)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * np.exp(-t / 0.16) + 0.25 * np.sin(ph * 2) * np.exp(-t / 0.02)


def hat(seed, d=0.08, open_=False):
    rng = np.random.default_rng(seed)
    t = tt(d if not open_ else 0.22)
    return hp(rng.standard_normal(len(t)), 7000) * np.exp(-t / (0.018 if not open_ else 0.07))


def clap(seed):
    rng = np.random.default_rng(seed)
    t = tt(0.25)
    n = hp(lp(rng.standard_normal(len(t)), 3500), 900)
    e = np.exp(-t / 0.06) + 0.6 * np.exp(-np.maximum(t - 0.012, 0) / 0.01) * (t > 0.012)
    return n * e


def bass(m, d):
    t = tt(d)
    f = hz(m)
    x = sum(np.sin(2 * np.pi * f * k * t) / k for k in range(1, 7))
    env = np.clip(t / 0.005, 0, 1) * np.exp(-t / (d * 0.9))
    return lp(x * env, 420)


def pad(notes, d):
    t = tt(d)
    x = np.zeros(len(t))
    for m in notes:
        for det in (-0.08, 0.0, 0.08):
            f = hz(m + det)
            x += np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * 2 * f * t)
    env = np.clip(t / 0.35, 0, 1) * np.clip((d - t) / 0.3, 0, 1)
    return lp(x * env, 1800) / (len(notes) * 3)


def pluck(m, d=0.35, bright=0.4):
    t = tt(d)
    f = hz(m)
    x = np.sin(2 * np.pi * f * t) + bright * np.sin(2 * np.pi * 4 * f * t) * np.exp(-t / 0.03)
    return x * np.clip(t / 0.002, 0, 1) * np.exp(-t / (d / 3.5))


def whoosh(seed, d, rise=True):
    rng = np.random.default_rng(seed)
    t = tt(d)
    n = lp(rng.standard_normal(len(t)), 2500)
    shape = (t / d) ** 2 if rise else np.sin(np.pi * t / d) ** 2
    return hp(n, 200) * shape


def thud(m=40):
    t = tt(0.3)
    f = hz(m) * (1 + 0.6 * np.exp(-t / 0.02))
    ph = 2 * np.pi * np.cumsum(f) / SR
    return (np.sin(ph) + 0.4 * np.sin(ph * 2.7) * np.exp(-t / 0.03)) * np.exp(-t / 0.09)


def room(x, mix=0.16, size=0.12):
    rng = np.random.default_rng(3)
    ir_n = int(SR * size * 4)
    ir = rng.standard_normal(ir_n) * np.exp(-np.arange(ir_n) / (SR * size))
    wet = np.convolve(x, ir)[: len(x)]
    return x + mix * wet / (np.abs(wet).max() + 1e-9) * np.abs(x).max()


# ---------- arrangement ----------
# A minor → F → C → G; one chord per bar (2 s)
CH = {"Am": [57, 60, 64], "F": [53, 57, 60], "C": [55, 60, 64], "G": [55, 59, 62], "Dm": [57, 62, 65]}
ROOT = {"Am": 33, "F": 29, "C": 36, "G": 31, "Dm": 38}
BARS = ["Am", "F", "Am", "F", "C", "G", "Am", "F", "C", "G", "C", "C"]

music = np.zeros(N)
drums = np.zeros(N)
sfx = np.zeros(N)

for b, c in enumerate(BARS):
    t0 = b * 2.0
    d = min(2.0, LEN - t0)
    if d <= 0:
        break
    gain = 0.55 if t0 < 4 else 0.8
    if t0 >= 20:
        d = LEN - t0
    place(music, t0, pad(CH[c], d + 0.2), gain)
    # arp of eighths from the drop, sixteenth-free and sparse in the intro
    arp = CH[c] + [CH[c][0] + 12]
    step = BEAT / 2 if t0 >= 4 else BEAT
    k = 0
    t = t0
    while t < t0 + d - 1e-6 and t < 21.0:
        place(music, t, pluck(arp[k % 4] + 12, 0.3, 0.35), 0.16 if t0 >= 4 else 0.12)
        k += 1
        t += step
    if t0 >= 4:
        for i in range(4):
            place(music, t0 + i * BEAT, bass(ROOT[c] + 12, 0.42), 0.55)
            place(music, t0 + i * BEAT + 0.25, bass(ROOT[c] + 12, 0.2), 0.3)

# drums: intro has a soft tick only; groove from the drop to 20 s; out on 20.5
for i in range(int(LEN / BEAT)):
    t = i * BEAT
    if t < 4.0:
        if t < 3.75:
            place(drums, t, hat(100 + i), 0.12)
        continue
    if t <= 20.0:
        place(drums, t, kick(), 0.95)
        place(drums, t + 0.25, hat(200 + i, open_=(i % 2 == 1)), 0.22)
        if i % 2 == 1:
            place(drums, t, clap(300 + i), 0.35)

# riser into the drop, then a beat of silence-ish before it
place(sfx, 2.6, whoosh(1, 1.25), 0.45)
music[int(3.85 * SR): int(4.0 * SR)] *= np.linspace(1, 0.15, int(0.15 * SR))

# SFX on the picture
place(sfx, 2.0, pluck(76, 0.5, 0.5), 0.5)                           # the dot pops
place(sfx, 4.0, room(pad([57, 64, 69, 72], 1.2)) * 1.4, 0.9)          # stab on the iris
place(sfx, 4.0, kick(0.6), 0.6)
place(sfx, 6.0, whoosh(2, 0.55), 0.55)                              # speed ramp
for t in [7.0, 7.75, 8.5, 9.25, 10.0]:                              # stamps
    place(sfx, t, room(thud(43)), 0.55)
place(sfx, 10.45, whoosh(3, 0.55), 0.5)                             # flood
for i, t in enumerate([11.1, 11.6, 12.1, 12.6]):                    # numbers
    place(sfx, t, pluck([72, 76, 79, 84][i], 0.4, 0.5), 0.35)
place(sfx, 14.0, whoosh(4, 0.5, rise=False), 0.45)                  # collapse
place(sfx, 15.0, room(thud(36)), 0.6)                               # badge lands
for i, t in enumerate([15.5, 16.0, 16.5, 17.0]):                    # chips
    place(sfx, t, pluck([79, 81, 84, 88][i], 0.25, 0.3), 0.22)
place(sfx, 18.5, room(pad([48, 55, 60, 64, 67], 3.6)) * 1.3, 0.8)   # warm chord on the match cut
for i, m in enumerate([72, 76, 79, 84]):
    place(sfx, 18.5 + i * 0.07, pluck(m, 0.7, 0.4), 0.3)
place(sfx, 20.5, pluck(84, 0.6, 0.5), 0.35)                         # the full stop breathes

mix = 0.8 * music + 0.75 * drums + 0.9 * sfx
mix = lp(mix, 15000)
fade = np.ones(N)
fo = int(1.5 * SR)
fade[-fo:] = np.linspace(1, 0, fo) ** 1.5
mix *= fade
mix = mix / (np.abs(mix).max() + 1e-9) * 0.89
stereo = np.stack([mix, mix], axis=1)
wavfile.write(sys.argv[1] if len(sys.argv) > 1 else "mix.wav", SR, (stereo * 32767).astype(np.int16))
print("wrote", sys.argv[1] if len(sys.argv) > 1 else "mix.wav", f"{LEN}s")

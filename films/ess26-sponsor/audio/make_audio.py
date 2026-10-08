"""Original 120 BPM half-time bed + warm SFX for the ESS'26 sponsor film (synthesised, no samples, no licences).

Usage: python audio/make_audio.py audio/mix.wav
Deterministic: every noise source is seeded. Bars are 2 s; the drop is on 4.0 s, after a held half-beat of silence.
Needs numpy + scipy.
"""
import sys
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

SR = 48000
LEN = 23.0
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
# D minor → B♭ → F → C; one chord per bar (2 s); half-time groove (kick on 1, snare on 3)


def epiano(m, d=0.9):
    t = tt(d)
    f = hz(m)
    mod = 1.4 * np.exp(-t / 0.25) * np.sin(2 * np.pi * f * t)
    x = np.sin(2 * np.pi * f * t + mod) + 0.15 * np.sin(2 * np.pi * 3 * f * t) * np.exp(-t / 0.1)
    return x * np.clip(t / 0.004, 0, 1) * np.exp(-t / (d / 2.5))


CH = {"Dm": [62, 65, 69], "Bb": [58, 62, 65], "F": [57, 60, 65], "C": [55, 60, 64], "Gm": [55, 58, 62]}
ROOT = {"Dm": 38, "Bb": 34, "F": 41, "C": 36, "Gm": 43}
BARS = ["Dm", "Dm", "Dm", "Bb", "F", "C", "Dm", "Bb", "Gm", "C", "F", "F"]

music = np.zeros(N)
drums = np.zeros(N)
sfx = np.zeros(N)

for b, c in enumerate(BARS):
    t0 = b * 2.0
    if t0 >= LEN:
        break
    d = min(2.0, LEN - t0) if t0 < 20 else LEN - t0
    place(music, t0, pad([n - 12 for n in CH[c]], d + 0.2), 0.5 if t0 < 4 else 0.7)
    if t0 >= 4:
        for k, off in enumerate([0, 0.75, 1.25]):            # syncopated e-piano comp
            if t0 + off < 21.5:
                for m in CH[c]:
                    place(music, t0 + off, epiano(m, 0.8), 0.12)
        for off, dur in [(0, 0.6), (0.75, 0.3), (1.5, 0.4)]:
            if t0 + off < 21:
                place(music, t0 + off, bass(ROOT[c], dur), 0.6)

for i in range(int(LEN / BEAT)):
    t = i * BEAT
    if t < 4.0:
        if t < 3.5 and i % 2 == 0:
            place(drums, t, hat(500 + i), 0.08)
        continue
    if t > 20.0:
        continue
    if i % 4 == 0:
        place(drums, t, kick(), 0.95)
    if i % 4 == 2:
        place(drums, t, clap(600 + i), 0.45)
    place(drums, t + 0.25, hat(700 + i), 0.15)
    place(drums, t, hat(800 + i), 0.1)

# hold-frame: everything stops for half a beat before the drop
music[int(3.5 * SR): int(4.0 * SR)] = 0
drums[int(3.5 * SR): int(4.0 * SR)] = 0

# SFX on the picture
for i, t in enumerate(np.arange(0.5, 1.3, 0.05)):                   # typewriter line 1
    place(sfx, t, hat(900 + i, 0.03), 0.05)
for i, t in enumerate(np.arange(1.55, 2.1, 0.05)):                  # typewriter line 2
    place(sfx, t, hat(950 + i, 0.03), 0.05)
for i, t in enumerate(np.arange(2.3, 2.75, 0.05)):                  # typewriter line 3
    place(sfx, t, hat(980 + i, 0.03), 0.05)
place(sfx, 4.0, room(pad([50, 57, 62, 65, 69], 1.4)) * 1.4, 0.9)    # the snap stab
place(sfx, 4.0, kick(0.6), 0.7)
for i in range(7):
    place(sfx, 4.0 + i * 0.03, pluck(74 + [0, 3, 7, 10, 12, 15, 19][i], 0.25, 0.5), 0.08)
for i in range(10):                                                 # packet blips
    place(sfx, 6.9 + i * 0.5, pluck([81, 77, 84, 81, 86, 84, 81, 77, 84, 89][i], 0.22, 0.3), 0.14)
place(sfx, 12.0, whoosh(21, 0.45), 0.5)                             # split stack
for i in range(6):                                                  # jack clicks
    place(sfx, 12.75 + i * 0.5 + 0.3, room(thud(60 + i)), 0.35)
    place(sfx, 12.75 + i * 0.5 + 0.3, hat(1000 + i, 0.04), 0.3)
place(sfx, 16.6, whoosh(22, 0.9), 0.4)                              # cable to horizon
place(sfx, 17.5, room(pad([41, 53, 57, 60, 65, 69], 4.5)) * 1.3, 0.8)  # warm F chord
for i, m in enumerate([65, 69, 72, 77]):
    place(sfx, 17.5 + i * 0.08, epiano(m, 1.2), 0.25)

mix = 0.8 * music + 0.75 * drums + 0.9 * sfx
mix = lp(mix, 15000)
fade = np.ones(N)
fo = int(1.5 * SR)
fade[-fo:] = np.linspace(1, 0, fo) ** 1.5
mix *= fade
mix = mix / (np.abs(mix).max() + 1e-9) * 0.89
stereo = np.stack([mix, mix], axis=1)
out = sys.argv[1] if len(sys.argv) > 1 else "mix.wav"
wavfile.write(out, SR, (stereo * 32767).astype(np.int16))
print("wrote", out, f"{LEN}s")

"""Synthesise the paper SFX track for the episode (no samples, seeded, deterministic).

Usage: python tools/sfx.py  →  assets/audio/sfx.wav (48 kHz mono, full episode length)
Sounds: slide (paper slides in), snap (a cut-out lands), tap (a label sticks),
tear (paper rips), stamp (a rubber stamp), rustle, tick (wood block), and warm
marimba pop / confirm / reveal from the kit's tools/warm_sfx.py. Kept low under the voice.
"""
import os, sys
import numpy as np
import soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__)); P = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(P, "..", "..", "tools"))
from warm_sfx import marimba, woodblock, room, seq, NOTE, SR  # noqa: E402

END = 506.4
rng = np.random.default_rng(2026)

def lp(x, a):  # one-pole low-pass, a in (0,1): smaller = darker
    y = np.empty_like(x); s = 0.0
    for i, v in enumerate(x):
        s += a * (v - s); y[i] = s
    return y

def hp(x, a):
    return x - lp(x, a)

def noise(d):
    return rng.standard_normal(int(SR * d))

def envelope(n, att, rel):
    t = np.arange(n) / SR
    up = np.clip(t / max(att, 1e-4), 0, 1)
    down = np.clip((n / SR - t) / max(rel, 1e-4), 0, 1)
    return up * down

def slide(d=0.24):
    x = hp(lp(noise(d), 0.25), 0.02)
    return x * envelope(len(x), d * 0.55, d * 0.45) ** 1.5 * 0.5

def snap():
    click = hp(noise(0.018), 0.3) * np.exp(-np.arange(int(SR * 0.018)) / (SR * 0.004))
    t = np.arange(int(SR * 0.09)) / SR
    thump = np.sin(2 * np.pi * 150 * t) * np.exp(-t / 0.025)
    return seq((0, click * 0.9), (0, thump * 0.6))

def tap():
    c = lp(noise(0.012), 0.35) * np.exp(-np.arange(int(SR * 0.012)) / (SR * 0.003))
    return c * 0.7

def tear(d=0.5):
    n = int(SR * d); x = hp(noise(d), 0.12)
    crack = np.zeros(n)
    for i in rng.integers(0, n - 400, 70):
        crack[i:i + 300] += np.exp(-np.arange(300) / 60.0) * rng.uniform(0.4, 1.0)
    return x * (0.25 + crack) * envelope(n, 0.02, 0.15) * 0.6

def stamp():
    t = np.arange(int(SR * 0.16)) / SR
    thud = np.sin(2 * np.pi * 85 * t) * np.exp(-t / 0.05)
    return seq((0, thud), (0, snap() * 0.8))

def rustle(d=0.8):
    x = hp(lp(noise(d), 0.3), 0.05)
    flutter = 0.5 + 0.5 * np.abs(np.sin(np.arange(len(x)) / SR * 2 * np.pi * 7))
    return x * flutter * envelope(len(x), 0.1, 0.3) * 0.35

def ticks(k=8, gap=0.08):
    return seq(*[(i * gap, woodblock(1000 + (i % 2) * 180, 0.08)) for i in range(k)])

SOUND = {
    "slide": lambda: slide(), "slideL": lambda: slide(0.5), "slideS": lambda: slide(0.14),
    "snap": snap, "tap": tap, "tear": lambda: tear(), "stamp": stamp,
    "rustle": lambda: rustle(), "rustleL": lambda: rustle(1.6), "ticks": lambda: ticks(),
    "pop": lambda: marimba(NOTE["G5"], 0.3, 0.5),
    "confirm": lambda: seq((0, marimba(NOTE["E5"], 0.4)), (0.09, marimba(NOTE["G5"], 0.5))),
    "reveal": lambda: seq((0, marimba(NOTE["C5"], 0.6)), (0.07, marimba(NOTE["E5"], 0.6)), (0.14, marimba(NOTE["G5"], 0.7)), (0.21, marimba(NOTE["C6"], 0.9))),
}
GAIN = {"slide": 0.30, "slideL": 0.30, "slideS": 0.25, "snap": 0.30, "tap": 0.22, "tear": 0.42, "stamp": 0.45,
        "rustle": 0.22, "rustleL": 0.20, "ticks": 0.16, "pop": 0.12, "confirm": 0.13, "reveal": 0.14}

CUES = """
slide 0.35; snap 3.94; slide 5.31; snap 7.62; snap 12.93; pop 18.79; stamp 24.82; slide 28.12; slide 29.76; slide 32.44; rustle 34.49
slideL 41.6; pop 43.91; slide 46.78; snap 50.14; tap 51.51; tap 53.97; slide 54.72; slideS 55.6; tap 56.91; tap 57.74; tear 64.25
reveal 65.42; stamp 66.45; slideS 70.04; snap 70.8; slide 72.5; snap 76.09; slide 78.26; tap 78.96; slide 82.2
slide 84.37; slide 85.03; pop 91.64; ticks 94.12; snap 95.31; slide 99.66; slide 109.25; stamp 113.52; slide 115.15; pop 117.82; rustle 119.33
stamp 124.85; stamp 125.4; slideL 127.6; slide 128.2
tap 133.36; slide 137.88; slide 141.49; snap 144.84; slide 148.29; slideS 150.52; slideL 152.13; slide 152.58; tap 154.71; tap 156.13; tap 157.03
tap 163.36; tear 167.48; reveal 169.21; slide 171.73; tap 174.86; tap 175.37; tap 176.1; slideL 178.87; tap 182.68; tap 183.73; tap 185.27
slide 188.42; reveal 188.42; tap 192.06; stamp 194.92; tap 197.77; confirm 204.37; tap 204.88; ticks 206.04; slideL 207.68; tap 211.07; snap 219.5
pop 228.56; snap 233.52; snap 235.65; snap 237.71; slide 238.75; stamp 239.46; tap 242.81; slideL 244.9; tap 252.42; tap 253.65; tap 255.57; tap 258.21; tap 258.67
tap 262.39; tap 262.77; tap 263.15; stamp 264.9; slideL 267.81; rustle 270.6; tap 275.61; slide 281.97; confirm 282.58; pop 286.6; tear 291.04; slideL 292.49
tap 299.97; tap 300.4; tap 300.97; slide 304.52; snap 305.9
slide 310.4; pop 312.05; snap 318.59; snap 319.54; snap 319.96; slide 321.43; slide 327.21; confirm 328.07; tap 328.66; rustleL 329.62; stamp 335.02
slide 338.15; slideS 340.28; slide 341.85; rustle 343.85; slideL 344.94; pop 349.0; pop 350.6; snap 351.6; slide 352.06; stamp 356.21; slideS 357.87
tap 363.31; tap 364.22; tear 368.48; stamp 370.73; slideL 371.8; slide 372.4
slide 377.57; snap 378.84; tap 379.5; ticks 380.72; pop 388.24; slideL 395.28; slideL 397.08; tap 397.97; slide 400.74; slideS 402.15; tap 402.8; slideL 403.72
stamp 413.42; stamp 421.21; slide 421.46; tap 423.55; slide 427.45; slide 433.48; slide 434.11; tap 435.17; slide 436.92; snap 437.89; confirm 442.08; slide 443.8
stamp 446.25; slide 449.49; slide 451.28; slide 452.65; slideL 454.45; tap 455.85; tap 457.26; tap 459.88; slide 466.53; slideS 469.86
snap 474.57; snap 475.22; snap 475.86; rustle 477.4; tear 478.26; reveal 478.71; tap 481.24; slideL 482.7; slide 483.3
slide 487.0; tap 488.74; tap 488.99; tap 489.24; tap 489.49; tap 489.74; tap 489.99; tap 490.24; tap 490.49; tap 490.74; tap 490.99; confirm 492.0
slideL 497.4; tap 499.19; reveal 500.69
"""

def main():
    out = np.zeros(int(SR * (END + 2)))
    n = 0
    for item in CUES.replace("\n", ";").split(";"):
        item = item.strip()
        if not item:
            continue
        kind, t = item.split()
        s = room(SOUND[kind](), mix=0.08, size=0.05)
        s = s / (np.abs(s).max() + 1e-9) * GAIN[kind]
        i = int(float(t) * SR)
        out[i:i + len(s)] += s[: len(out) - i]
        n += 1
    out = out[: int(SR * END)]
    path = os.path.join(P, "assets/audio/sfx.wav")
    sf.write(path, out.astype(np.float32), SR)
    print(f"{n} cues → {path}, peak {20*np.log10(np.abs(out).max()):.1f} dBFS")

if __name__ == "__main__":
    main()

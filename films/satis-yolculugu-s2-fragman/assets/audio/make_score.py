"""Synthesise the film's score: a 120 BPM percussive bed plus warm, tuned hits on the cuts.

Usage: python assets/audio/make_score.py   (writes assets/audio/score.wav, 70 s, 48 kHz stereo)
No samples and no licences: kick, wood block, marimba and a soft bass, all synthesised and seeded.
The cue times match the GSAP timeline in index.html. 1 bar = 2 s.
"""
import os
import numpy as np
import soundfile as sf

SR = 48000
DUR = 70.0
N = int(SR * DUR)
rng = np.random.default_rng(85)
L = np.zeros(N)
R = np.zeros(N)


def hz(note):
    names = {"C": 0, "C#": 1, "D": 2, "Eb": 3, "E": 4, "F": 5, "F#": 6, "G": 7, "Ab": 8, "A": 9, "Bb": 10, "B": 11}
    n, o = note[:-1], int(note[-1])
    return 440.0 * 2 ** ((names[n] + 12 * (o + 1) - 69) / 12)


def env(n, a, d):
    t = np.arange(n) / SR
    return np.clip(t / max(a, 1e-4), 0, 1) * np.exp(-t / d)


def kick(gain=1.0):
    n = int(SR * .45); t = np.arange(n) / SR
    f = 45 + 95 * np.exp(-t / .045)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return gain * np.sin(ph) * env(n, .002, .16)


def wood(f=880, gain=.35):
    n = int(SR * .12); t = np.arange(n) / SR
    return gain * (np.sin(2 * np.pi * f * t) + .5 * np.sin(2 * np.pi * f * 2.7 * t)) * env(n, .001, .025)


def marimba(f, dur=.9, gain=.5, bright=.35):
    n = int(SR * dur); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) + bright * np.sin(2 * np.pi * f * 4 * t) * np.exp(-t / .03) + .2 * np.sin(2 * np.pi * f * 10 * t) * np.exp(-t / .008)
    return gain * x * env(n, .002, dur / 3.5)


def bass(f, dur=.45, gain=.42):
    n = int(SR * dur); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * f * t) + .3 * np.sin(2 * np.pi * 2 * f * t) + .12 * np.sin(2 * np.pi * 3 * f * t)
    return gain * np.tanh(1.6 * x) * env(n, .006, dur / 2.2)


def thud(gain=.9):
    n = int(SR * .35); t = np.arange(n) / SR
    body = np.sin(2 * np.pi * (70 + 60 * np.exp(-t / .02)) * t) * env(n, .001, .09)
    tick = rng.standard_normal(n) * env(n, .0005, .006) * .25
    return gain * (body + tick)


def rip(dur=.38, gain=.5):
    n = int(SR * dur); t = np.arange(n) / SR
    noise = rng.standard_normal(n)
    # crude band-pass sweep: difference of two moving averages whose width shrinks over time
    out = np.zeros(n); acc = 0.0
    for i in range(n):
        k = .55 - .45 * (i / n)
        acc = k * acc + (1 - k) * noise[i]
        out[i] = noise[i] - acc
    crackle = (rng.random(n) > .985) * rng.standard_normal(n) * 1.5
    return gain * (out * .6 + crackle) * np.clip(t / .01, 0, 1) * np.exp(-t / (dur / 2.5))


def chord(notes, dur=1.6, gain=.32, spread=.018):
    parts = [(i * spread, marimba(hz(nm), dur, gain)) for i, nm in enumerate(notes)]
    end = max(int(o * SR) + len(s) for o, s in parts)
    out = np.zeros(end)
    for o, s in parts:
        i = int(o * SR); out[i:i + len(s)] += s
    return out


def put(t, sig, pan=0.0):
    i = int(t * SR)
    if i >= N:
        return
    s = sig[: N - i]
    L[i:i + len(s)] += s * (1 - max(pan, 0))
    R[i:i + len(s)] += s * (1 + min(pan, 0))


def silent(t0, t1):
    return any(a <= t0 < b for a, b in SILENCE)


# the beat drops out on purpose: the word clamp and the hard stop before "DEĞER"
SILENCE = [(8.5, 11.0), (52.0, 52.5), (66.5, 70.0)]
BASSLINE = ["C2", "C2", "G1", "Bb1"]          # one note per bar, C minor-ish, bold

# ---------- groove ----------
for b in range(int(DUR * 2)):                  # beats at 120 BPM
    t = b * .5
    if silent(t, t) or t >= 66.5:
        continue
    bar, beat = divmod(b, 4)
    full = (15.0 <= t < 52.0) or (53.0 <= t < 62.0)
    if beat in (0, 2) or (full and beat in (1, 3) and 36.0 <= t < 44.0):
        put(t, kick(.95 if beat == 0 else .75))
    if full or t < 8.5 or 11.0 <= t < 15.0:
        put(t + .25, wood(1175 if beat % 2 else 880, .16), pan=.35 if beat % 2 else -.35)
    if beat == 0 and (t < 8.5 or full) and t < 62.0:
        put(t, bass(hz(BASSLINE[bar % 4]), 1.2, .38))
    if full and beat == 3 and bar % 2 == 1:
        put(t + .25, bass(hz(BASSLINE[bar % 4]) * 1.5, .25, .22))

# ---------- cues (seconds, matching index.html) ----------
put(.9, marimba(hz("G4"), .6, .3)); put(1.25, marimba(hz("G4"), .6, .3)); put(1.75, chord(["C4", "Eb4", "G4"], 1.0, .26))
for t in (4.5, 5.5, 6.5):                      # three evasive answers slam
    put(t, chord(["C3", "G3"], .5, .45)); put(t, thud(.6))
# word clamp: a low marimba tremolo that tightens, then a knot
for i in range(22):
    tt = 8.75 + 1.7 * (1 - (1 - i / 22) ** 1.6)
    put(tt, marimba(hz("C3") * (1 + i * .012), .25, .10 + i * .006, .15))
put(10.45, thud(.8))
for t in (11.05, 12.0, 12.55, 13.1):           # poster drop + three stamps
    put(t, thud(.85))
put(14.8, rip(.25, .25)); put(15.0, rip(.45, .55)); put(15.0, kick(1.0)); put(15.0, chord(["C3", "G3", "C4", "Eb4"], 2.0, .3))
put(16.0, chord(["G3", "C4", "Eb4"], .8, .22))
for i in range(8):                             # bricks
    put(21.9 + i * .2, wood(700 + i * 40, .2), pan=-.2 + .05 * i)
put(23.2, thud(.6))
for i in range(22):                            # drill: a fast wood-block roll
    put(25.8 + i * .05, wood(1400 + (i % 2) * 120, .12))
put(26.2, thud(.4)); put(27.6, rip(.7, .18))
put(28.5, chord(["C4", "E4", "G4", "C5"], 2.2, .3, .06))   # the photo: the first major chord
put(31.9, marimba(hz("G4"), 1.0, .2)); put(32.55, thud(.7))
put(36.4, kick(1.0)); put(36.4, thud(1.0)); put(36.4, chord(["C3", "G3", "C4", "E4", "G4"], 2.4, .32))
for t in (37.0, 37.25, 37.5):
    put(t, marimba(hz("E4"), .4, .25))
put(38.6, chord(["F3", "C4", "A4"], .9, .24)); put(39.6, chord(["G3", "D4", "B4"], .9, .24))
put(43.5, rip(.5, .12))
for i in range(4):                             # 3 GÜN → 3 SAAT: tick-tock
    put(44.6 + i * .25, wood(1500 if i % 2 else 1100, .2))
put(45.5, thud(.7)); put(46.3, chord(["C5", "E5", "G5"], 1.2, .26, .05))
put(48.0, marimba(hz("C4"), .6, .25)); put(48.25, marimba(hz("G4"), .6, .25))
put(50.0, chord(["C3", "Eb3", "G3"], .8, .32)); put(51.6, thud(.8))
put(52.5, kick(1.0)); put(53.0, chord(["C3", "G3", "C4", "E4", "G4", "C5"], 2.6, .32)); put(53.0, thud(.9))
for i in range(6):                             # flood: a rising marimba run into the logo
    put(56.2 + i * .13, marimba(hz(["C4", "E4", "G4", "C5", "E5", "G5"][i]), .5, .2))
put(57.3, chord(["C3", "G3", "C4", "E4", "G4"], 3.0, .3, .03)); put(58.4, marimba(hz("C5"), 1.2, .22))
for i, nm in enumerate(["E4", "G4", "C5"]):    # homework lines type on
    put(62.9 + i * .7, marimba(hz(nm), .9, .22))
put(64.9, chord(["C3", "G3", "C4", "E4", "G4", "C5"], 4.5, .3, .04))   # resolve, rings into the held end

# ---------- room + master ----------
ir_n = int(SR * .5)
ir = rng.standard_normal(ir_n) * np.exp(-np.arange(ir_n) / (SR * .09))
ir /= np.abs(ir).sum() / 6
mix = []
for ch in (L, R):
    wet = np.convolve(ch, ir)[:N]
    y = ch + .12 * wet
    y = np.tanh(1.1 * y) / np.tanh(1.1)
    mix.append(y)
st = np.stack(mix, axis=1)
fade = int(SR * 1.5); st[-fade:] *= np.linspace(1, 0, fade)[:, None]
st = st / (np.abs(st).max() + 1e-9) * 10 ** (-1.5 / 20)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "score.wav")
sf.write(out, st.astype(np.float32), SR)
print("wrote", out, f"{DUR:.0f}s")

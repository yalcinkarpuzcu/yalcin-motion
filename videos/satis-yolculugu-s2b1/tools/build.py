"""Resolve word-synced cue tokens in src/chN.html → compositions/chN.html and write index.html slots.
Tokens:  {{w:kelime@12.3}}  local start time of the spoken word nearest 12.3 s (absolute) that starts with 'kelime'
         {{we:kelime@12.3}} same, but the word's end time
         {{a:12.3}}         absolute seconds → chapter-local seconds
         {{dur}}            chapter duration
"""
import json, re, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = os.path.dirname(HERE)
W = json.load(open(os.path.join(P, "source/words.json")))
CH = [(0.0, 40.7), (40.7, 82.8), (82.8, 130.7), (130.7, 222.8), (222.8, 310.4),
      (310.4, 375.2), (375.2, 444.5), (444.5, 486.1), (486.1, 506.4)]
END = 506.4
def norm(w):
    w = w.replace("I", "ı").replace("İ", "i").lower()
    return re.sub(r"[^\wçğıöşüâî%]", "", w)
def find(word, approx, key):
    n = norm(word); cands = [x for x in W if norm(x["w"]).startswith(n)]
    if not cands: sys.exit(f"word not found: {word}")
    best = min(cands, key=lambda x: abs(x["s"] - approx))
    if abs(best["s"] - approx) > 4: sys.exit(f"'{word}' nearest {best['s']} far from {approx}")
    return best[key]
def resolve(txt, st, en):
    def rep(m):
        kind, body = m.group(1), m.group(2)
        if kind == "dur": return f"{en-st:.2f}"
        if kind == "a": return f"{float(body)-st:.2f}"
        w, a = body.rsplit("@", 1)
        return f"{find(w, float(a), 's' if kind=='w' else 'e') - st:.2f}"
    return re.sub(r"\{\{(w|we|a|dur):?([^}]*)\}\}", rep, txt)
for i, (st, en) in enumerate(CH, 1):
    s = os.path.join(P, f"src/ch{i}.html")
    if not os.path.exists(s): continue
    out = resolve(open(s).read(), st, en)
    open(os.path.join(P, f"compositions/ch{i}.html"), "w").write(out)
    print(f"ch{i}: {st}–{en}")

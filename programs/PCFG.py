g = {
    "S": [(["NP", "VP"], 1.0)],
    "NP": [(["Det", "N"], 1.0)],
    "VP": [(["V", "NP"], 1.0)],
    "Det": [(["the"], 1.0)],
    "N": [(["cat"], 0.5), (["dog"], 0.5)],
    "V": [(["sees"], 0.5), (["likes"], 0.5)]
}
def parse(x, w, i):
    if x not in g:
        if i < len(w) and x == w[i]:
            return i + 1, 1.0
        return -1, 0
    for r, p in g[x]:
        j = i
        pr = p
        ok = True
        for y in r:
            j, q = parse(y, w, j)
            if j == -1:
                ok = False
                break
            pr = pr * q
        if ok:
            return j, pr
    return -1, 0
w = "the cat sees the dog".split()
i, p = parse("S", w, 0)
if i == len(w):
    print("Sentence Accepted")
    print("Probability:", p)
else:
    print("Sentence Rejected")
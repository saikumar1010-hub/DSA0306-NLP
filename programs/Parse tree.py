g = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["sees"], ["likes"]]
}
def parse(x, w, i):
    if x not in g:
        if i < len(w) and x == w[i]:
            return [x, w[i]], i + 1
        return None, i
    for r in g[x]:
        j = i
        t = [x]
        ok = True
        for y in r:
            a, j = parse(y, w, j)
            if a is None:
                ok = False
                break
            t.append(a)
        if ok:
            return t, j
    return None, i
def show(t, n=0):
    print("  " * n + t[0])
    for x in t[1:]:
        if isinstance(x, list):
            show(x, n + 1)
w = "the cat sees the dog".split()
t, i = parse("S", w, 0)
if t is not None and i == len(w):
    print("Sentence Accepted")
    print("\nParse Tree:")
    show(t)
else:
    print("Sentence Rejected")
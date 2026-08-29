def earley(w, g):
    c = [set() for i in range(len(w) + 1)]

    c[0].add(("S", ["S"], 0, 0))
    for i in range(len(w) + 1):
        change = True
        while change:
            change = False
            for a in list(c[i]):
                x, y, p, q = a
                if p < len(y):
                    z = y[p]
                    if z in g:
                        for r in g[z]:
                            n = (z, r, 0, i)
                            if n not in c[i]:
                                c[i].add(n)
                                change = True
                    elif i < len(w):
                        if z == w[i]:
                            n = (x, y, p + 1, q)
                            c[i + 1].add(n)
                else:
                    for b in list(c[q]):
                        m, n, o, r = b
                        if o < len(n) and n[o] == x:
                            t = (m, n, o + 1, r)
                            if t not in c[i]:
                                c[i].add(t)
                                change = True
    return ("S", ["S"], 1, 0) in c[len(w)]
g = {
    "S": [["NP", "VP"]],
    "NP": [["D", "N"]],
    "VP": [["V", "NP"]],
    "D": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["sees"], ["likes"]]
}
w = "the cat sees the dog".split()
if earley(w, g):
    print("Accepted")
else:
    print("Rejected")
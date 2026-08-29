def fopc(x):
    x = x.strip()
    if x.startswith("FORALL "):
        q = "FORALL"
        x = x[7:]
    elif x.startswith("EXISTS "):
        q = "EXISTS"
        x = x[7:]
    else:
        return False
    if ":" not in x:
        return False
    v, p = x.split(":", 1)
    v = v.strip()
    p = p.strip()
    if len(v) != 1:
        return False
    if not v.isalpha():
        return False
    if "(" not in p or ")" not in p:
        return False
    a = p.index("(")
    b = p.rindex(")")
    if a == 0 or b <= a:
        return False
    name = p[:a]
    values = p[a + 1:b]
    if not name.isalpha():
        return False
    if values == "":
        return False
    return True
x = input("Enter FOPC expression: ")
if fopc(x):
    print("Valid FOPC expression")
else:
    print("Invalid FOPC expression")
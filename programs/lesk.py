import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
nltk.download('omw-1.4')
def lesk(s, w):
    a = set(s.lower().split())
    best = None
    max = 0
    for x in wordnet.synsets(w):
        b = set(x.definition().lower().split())
        common = len(a & b)
        if common > max:
            max = common
            best = x
    return best
s = "He went to the bank to deposit money."
x = lesk(s, "bank")
if x:
    print("Best Sense:", x.name())
    print("Meaning:", x.definition())
else:
    print("No sense found")
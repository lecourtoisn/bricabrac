from collections import Counter
from itertools import product

nb_dice = 2
hits = [max(rolls) for rolls in product(range(1, 11), repeat=nb_dice)]
counter = Counter(hits)
proba = {key: 100 * nb / len(hits) for key, nb in counter.items()}
formatted = {key: "{}%".format(value) for key, value in proba.items()}
for key in sorted(formatted.keys(), reverse=True):
    print("{:>2} => {:>{max_width}}".format(key, formatted[key], max_width=max(map(len, formatted.values()))))

from collections import Counter
from itertools import product

nb_dice = 2
skill = 49
focus = True

array = [sum(a) + (nb_dice if focus and r < skill else 0) for a in product(range(1, 11), repeat=nb_dice) for r in
         range(100)]
counts = Counter(array)
proba = {key: 100 * sum([value for k, value in counts.items() if k >= key]) / len(array) for key, v in
         counts.items()}
formatted = {key: "{:.2f}%".format(value) for key, value in proba.items()}
for i in sorted(proba.keys()):
    print("{:>2} => {:>{max_width}}".format(i, formatted[i], max_width=max(map(len, formatted.values()))))

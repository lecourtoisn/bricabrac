from collections import Counter
from itertools import product

nb_dice = 2
skill = 49
focus = True

array = [sum(a) + (nb_dice if focus and r < skill else 0) for a in product(range(1, 11), repeat=nb_dice) for r in
         range(100)]
counts = Counter(array)
true_count = {key: 100 * sum([value for k, value in counts.items() if k >= key]) / len(array) for key, v in
              counts.items()}
max_width = max([len(str(round(a, 2))) for a in true_count.values()]) + 1
for i in sorted(true_count.keys()):
    print("{:>2} => {:>{max_width}.2f}%".format(i, true_count[i], max_width=max_width))
print(counts.most_common())

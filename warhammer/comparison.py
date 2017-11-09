from itertools import product
from collections import Counter
from pprint import pprint

BF = 6
BE = 4
NB_DICE = 4


def tsf(rolls, limit=10):
    return [0 if i < limit else 1 for i in rolls]


def avg(rolls):
    print("{:>3}%".format(round(100 * sum(rolls) / len(rolls))))


rolls_a = [max(i) + BF - BE for i in product(range(1, 11), repeat=NB_DICE)]
rolls_b = [i + BF - BE for i in range(1, 11)]
ARBITRARY_BONUS = sum(rolls_a) / len(rolls_a) - sum(rolls_b) / len(rolls_b)
rolls_b = [i + ARBITRARY_BONUS for i in rolls_b]
pprint(Counter(rolls_a))
pprint(Counter(rolls_b))
# for i in range(min([*rolls_a, *rolls_b]), max([*rolls_a, *rolls_b])+1):
for i in range(min(rolls_a), max(*rolls_a) + 1):
    print("{}:".format(i))
    print("\t", end="")
    avg(tsf(rolls_a, limit=i))
    print("\t", end="")
    avg(tsf(rolls_b, limit=i))

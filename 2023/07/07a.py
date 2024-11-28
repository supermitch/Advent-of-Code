from itertools import groupby
from dataclasses import dataclass
from pprint import pp

cards = '23456789TJQKA'
values = {k: cards.index(k) for k in cards}


@dataclass
class Hand:
    cards: str
    order: int  # Highest kind count, e.g 'QQQ23' = 3
    kinds: int  # Numbers of groups, e.g. 'AA224' = 2


bids = {}
hands = []
with open('07_in.txt') as f:
    for line in f:
        hand, bid = line.split()
        bids[hand] = int(bid)
        order = 0
        kinds = 0
        for k, g in groupby(sorted(hand, key=lambda x: values[x])):
            order = max(len(list(g)), order)
            kinds += 1
        hands.append(Hand(hand, order, kinds))
print('Hands:')
pp(hands)

ranked = []
for new in hands:
    for i, old in enumerate(ranked[:]):
        if old.kinds > new.kinds:  # e.g. 5-of-a-kind beats 4-of-a-kind
            ranked.insert(i, new)
            break
        elif old.order < new.order:
            ranked.insert(i, new)
            break

    else:
        ranked.append(new)
print('Ranked:')
pp(ranked)

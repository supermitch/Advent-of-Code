import re
from collections import defaultdict

with open('04a_test.txt') as f:
    lines = [x.strip() for x in f]

score = 0
cards = defaultdict(int)
matches = defaultdict(int)

for line in lines:
    if m := re.match(r'Card(.*):(.*)\|(.*)', line):
        card_no = int(m[1])
        winning = [int(x) for x in m[2].split()]
        nums = [int(x) for x in m[3].split()]

    wins = sum(1 for x in nums if x in winning)
    score += 2 ** (wins - 1) if wins else 0
    cards[card_no] = 1
    matches[card_no] = wins

for card_no in range(1, len(cards) + 1):
    print(card_no)
    for i in range(1, matches[card_no] + 1):
        print(card_no + 1)
        cards[card_no + 1] += 1

print(cards)
print(f'Part a: {score}')
print(f'Part b: {sum(x for x in cards.values())}')

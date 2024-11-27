from math import prod

with open('06_input.txt') as f:
    times = [int(x) for x in next(f).split(':')[1].split()]
    recs = [int(x) for x in next(f).split(':')[1].split()]

races = list(zip(times, recs))

ways = []
for time, record in races:
    wins = 0
    for charge in range(time):
        if charge * (time - charge) > record:
            wins += 1
    ways.append(wins)

print(f'Part a: {prod(ways)} ways product')

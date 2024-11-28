from math import prod

with open('06_input.txt') as f:
    times = [int(x) for x in next(f).split(':')[1].split()]
    recs = [int(x) for x in next(f).split(':')[1].split()]

races = list(zip(times, recs))


def calculate_wins(time, record):
    wins = 0
    for charge in range(time):
        if charge * (time - charge) > record:
            wins += 1
    return wins


ways = []
for time, record in races:
    wins = calculate_wins(time, record)
    ways.append(wins)

print(f'Part a: {prod(ways)} ways product')


time = int(''.join(str(x) for x in times))
record = int(''.join(str(x) for x in recs))
wins = calculate_wins(time, record)

print(f'Part b: {wins} ways to win')

with open('02_input.txt') as f:
    lines = [x.strip() for x in f]

limit = {'red': 12, 'green': 13, 'blue': 14}

games = {}
for line in lines:
    i = int(line.split(':')[0].split()[1])
    sets = line.split(':')[1].split(';')
    games[i] = []
    for set in sets:
        pulls = set.split(',')
        batch = {}
        for cubes in pulls:
            count = int(cubes.split()[0])
            colour = cubes.split()[1]
            batch[colour] = count
        games[i].append(batch)

ids = []
for i, sets in games.items():
    possible = True
    for set in sets:
        for colour, count in set.items():
            if count > limit[colour]:
                possible = False
    if possible:
        ids.append(i)

print(f'Part a: {sum(ids)}')

powers = 0
for i, sets in games.items():
    mins = {'red': 0, 'green': 0, 'blue': 0}
    for set in sets:
        for colour, count in set.items():
            mins[colour] = max(count, mins[colour])
    powers += mins['red'] * mins['green'] * mins['blue']

print(f'Part b: {powers}')

with open('2021/02_input.txt') as f:
    data = [x.strip().split() for x in f]
    data = [(x, int(y)) for x, y in data]

x, depth = 0, 0
for move, d in data:
    if move == 'forward':
        x += d
    elif move == 'down':
        depth += d
    else:  # Move up
        depth -= d

print(f'Part 1: X * depth = {x * depth}')

x, depth, aim = 0, 0, 0
for move, d in data:
    if move == 'forward':
        x += d
        depth += aim * d
    elif move == 'down':
        aim += d
    else:  # Move up
        aim -= d

print(f'Part 2: X * depth = {x * depth}')

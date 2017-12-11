#Part A

def part_a():
    with open('11.input', 'r') as f:
        steps = f.read().strip().split(',')

    col = 0
    row = 0

    dirori = {
        'n': (1, 0),
        's': (-1, 0),
        'ne': (0.5, 1),
        'nw': (0.5, -1),
        'se': (-0.5, 1),
        'sw': (-0.5, -1),
    }
    for step in steps:
        dr, dc = dirori[step]
        row += dr
        col += dc

    print(row, col)
    print(calculate_distance(row, col))

    count = 0
    if col > 0:
        dir = 'w'
    elif col == 0:
        dir = None
    else:
        dir = 'e'
    if row > 0:
        ori = 'n'
    elif row == 0:
        ori = None
    else:
        ori = 's'

    for _ in range(abs(col)):
        count += 1
        # move nw
        row += 0.5
        col -= 1
    print(row, col)

    for _ in range(548):
        row += 1
    print(row, col)

    print('Part A: ', 329 + 548)

def calculate_distance(row, col):
    import math
    dc = abs(col)
    dr = max(abs(row) - abs(col) * 0.5, 0)
    return dr + dc

# Part B
def part_b(steps):

    dirori = {
        'n': (1, 0),
        's': (-1, 0),
        'ne': (0.5, 1),
        'nw': (0.5, -1),
        'se': (-0.5, 1),
        'sw': (-0.5, -1),
    }

    row, col = 0, 0
    max_dist = 0
    for step in steps:
        dr, dc = dirori[step]
        row += dr
        col += dc

        dist = calculate_distance(row, col)
        max_dist = max(dist, max_dist)

    print(max_dist)


def main():
    # Part A:
    part_a()
    print('Part A: {} - '.format(None))

    # Part B:
    # assert part_b(['se','sw','se','sw','sw']) == 3
    with open('11.input', 'r') as f:
        steps = f.read().strip().split(',')
    part_b(steps)
    print('Part B: {} - '.format(None))


if __name__ == '__main__':
    main()

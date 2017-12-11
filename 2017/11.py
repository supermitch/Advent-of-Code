def calculate_distance(row, col):
    dc = abs(col)
    dr = max(abs(row) - abs(col) * 0.5, 0)
    return int(dr + dc)


def main():
    with open('11.input', 'r') as f:
        steps = f.read().strip().split(',')

    deltas = {
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
        dr, dc = deltas[step]
        row += dr
        col += dc

        dist = calculate_distance(row, col)  # Part A
        max_dist = max(dist, max_dist)  # Part B

    print('Part A: {} - End position distance'.format(dist))
    print('Part B: {} - Further distance'.format(max_dist))


if __name__ == '__main__':
    main()

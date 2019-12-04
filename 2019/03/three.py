#!/usr/bin/env python


deltas = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}


def get_steps(moves, grid, junctions):
    """ Calculate the steps it takes to get to each junction. """
    x, y = 0, 0
    steps = 0
    taken = {}
    for d, dist in moves:
        dx, dy = deltas[d]
        for i in range(1, dist + 1):
            steps += 1
            coord = (x + dx * i, y + dy * i)
            if coord in junctions:
                taken[coord] = steps
        x = x + dx * i
        y = y + dy * i
    return taken


def trace_path(moves):
    """ Follow the path and populate coordinates in a grid. """
    x, y = 0, 0
    grid = {(x, y): 'o'}
    for d, dist in moves:
        dx, dy = deltas[d]
        for i in range(1, dist + 1):
            grid[(x + dx * i, y + dy * i)] = '.'
        x = x + dx * i
        y = y + dy * i
    return grid


def main():
    with open('input.txt') as f:
        one = [(x[0], int(x[1:])) for x in next(f).split(',')]
        two = [(x[0], int(x[1:])) for x in next(f).split(',')]

    g_one = trace_path(one)
    g_two = trace_path(two)

    junctions = []
    max_manhattan = float('inf')
    for coord in g_one:
        if coord == (0, 0):
            continue
        if coord in g_two:
            junctions.append(coord)
            manhattan = abs(coord[0]) + abs(coord[1])
            max_manhattan = min(max_manhattan, manhattan)

    print(f'Part A: {max_manhattan} - Distance to nearest intersection')

    steps_one = get_steps(one, g_one, junctions)
    steps_two = get_steps(two, g_two, junctions)

    min_steps = float('inf')
    for coord, steps in steps_one.items():
        total = steps + steps_two[coord]
        min_steps = min(total, min_steps)
    print(f'Part B: {min_steps} - Minimum steps to an intersection')


if __name__ == '__main__':
    main()

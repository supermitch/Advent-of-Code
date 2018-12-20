#!/usr/bin/env python
from itertools import takewhile

def extract(data):
    return list(takewhile(lambda x: x not in '(|)', data))


def make_map(start, grid, seq):
    x, y = start
    for c in seq:
        dx, dy = {
            'N': (-1, 0),
            'E': (0, 1),
            'S': (1, 0),
            'W': (0, -1),
        }[c]
        x, y = x + dx, y + dy
        if c in 'EW':
            door = '|'
        else:
            door = '-'
        grid[(x, y)] = door
        x, y = x + dx, y + dy
        grid[(x, y)] = '.'
    return x, y


def draw(grid):
    xmin = min(x for x, y in grid)
    xmax = max(x for x, y in grid)
    ymin = min(y for x, y in grid)
    ymax = max(y for x, y in grid)
    for x in range(xmin, xmax + 1):
        line = ''
        for y in range(ymin, ymax + 1):
            try:
                line += grid[(x, y)]
            except KeyError:
                line += '?'
        print(line)


def main():
    with open('input.txt') as f:
        data = f.readline().strip()[1:-1]

    data = 'ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN'
    coord = (0, 0)
    grid = {coord: 'X'}

    graph = {data[0]: []}

    while data:
        seq = extract(data)
        end = make_map(coord, grid, seq)
        draw(grid)
        data = data[len(seq):]
        print(data)

    for c in data:
        if node in 'NESW':


if __name__ == '__main__':
    main()


#!/usr/bin/env python
#from itertools import combinations
#from collections import OrderedDict
from collections import defaultdict


def parse(line):
    parts = line.split()
    n = int(parts[0][1:])
    x, y = parts[2].split(',')
    x, y = int(x), int(y[:-1])
    w, h = parts[3].split('x')
    w, h = int(w), int(h)
    return n, x, y, w, h


def read_input():
    with open('input.txt', 'r') as f:
        return [parse(l.strip()) for l in f]


def build_grid(data):
    coords = defaultdict(list)
    for n, x, y, w, h in data:
        for i in range(x, x + w):
            for j in range(y, y + h):
                coords[(i, j)].append(n)
    return coords


def part_a(coords):
    overlap = 0
    for k, v in coords.items():
        if len(v) > 1:
            overlap += 1
    return overlap


def part_b(coords):
    claims = set(list(range(1, 1310)))
    for coord, no in coords.items():
        if len(no) > 1:
            for x in no:
                if x in claims:
                    claims.remove(x)
    return claims.pop()  # Only one should remain


def main():
    data = read_input()

    test = [
        (1, 1, 3, 4, 4),
        (2, 3, 1, 4, 4),
        (3, 5, 5, 2, 2),
    ]
    coords = build_grid(test)
    overlap = part_a(coords)
    assert overlap == 4
    claim = part_b(coords)
    assert claim == 3

    coords = build_grid(data)
    overlap = part_a(coords)
    print('Part A: {} - No of overlapping claim coords'.format(overlap))

    claim = part_b(coords)
    print('Part B: {} - The claim with no overlap'.format(claim))


if __name__ == '__main__':
    main()

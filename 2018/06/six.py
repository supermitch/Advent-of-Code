#!/usr/bin/env python
from collections import defaultdict


def parse(l):
    x, y = [int(val) for val in l.split(',')]
    return x, y


def read_input():
    with open('input.txt') as f:
        return [parse(l.strip()) for l in f]


def find_closest(x, y, data):
    dists = defaultdict(int)
    for i, (m, n) in enumerate(data, start=1):
        dists[i] = abs(n - y) + abs(m - x)
    sort = sorted(dists.values())
    if sort[0] == sort[1]:
        return None
    else:
        return sorted(dists, key=lambda k:dists[k])[0]


def is_safe(x, y, data):
    return sum(abs(n - y) + abs(m - x) for m, n in data) < 10000


def safe_region(data, limits):
    x1, y1, x2, y2 = limits
    count = 0
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            count += is_safe(x, y, data)
    return count


def main():
    data = read_input()
    min_x = min(x for x, y in data)
    min_y = min(y for x, y in data)
    max_x = max(x for x, y in data)
    max_y = max(y for x, y in data)

    x1, y1 = (min_x, min_y)
    x2, y2 = (max_x, max_y)
    limits = x1, y1, x2, y2

    closes = defaultdict(int)
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            closest = find_closest(x, y, data)
            closes[(x, y)] = closest

    edges = set()
    edges.add(None)
    for x in range(x1, x2 + 1):
        edges.add(closes[(x, min_y)])
        edges.add(closes[(x, max_y)])
    for y in range(y1, y2 + 1):
        edges.add(closes[(min_x, y)])
        edges.add(closes[(max_x, y)])

    counts = defaultdict(int)
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            close = closes[(x, y)]
            if close not in edges:  # Would be infinite
                counts[close] += 1

    # part_a
    print(sorted(counts.items(), key=lambda k: counts[k[0]])[-1][1])

    # part_b
    print(safe_region(data, limits))  # 35928 wrong


if __name__ == '__main__':
    main()

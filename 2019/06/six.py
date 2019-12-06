#!/usr/bin/env python
from collections import defaultdict


def main():
    with open('input.txt') as f:
        data = [l.strip().split(')') for l in f]
    orbits = {b: a for a, b in data}

    paths = defaultdict(list)
    for o in orbits.keys():
        k = o
        while k != 'COM':
            paths[o].append(k)
            k = orbits[k]
    total = sum(len(path) for path in paths.values())
    print(f'Part A: {total} - Total no. of direct & indirect orbits')

    for obj in paths['YOU']:
        if obj in paths['SAN']:
            break
    transfers = paths['YOU'].index(obj) + paths['SAN'].index(obj) - 2
    print(f'Part B: {transfers} - Minimum orbital transfers to reach SAN')


if __name__ == '__main__':
    main()

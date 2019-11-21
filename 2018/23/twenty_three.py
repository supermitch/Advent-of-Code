#!/usr/bin/env python
from collections import defaultdict
from itertools import permutations
from pprint import pprint
from re import sub


def read_input():
    data = []
    with open('input.txt') as f:
        for l in f:
            data.append(tuple([int(x) for x in sub(r'[^0-9-]', ' ', l).split()]))
    return data


def in_range(a, b):
    """ Is b's location within range of a's signal radius? """
    return manhattan(a, b) <= a[3]


def manhattan(a, b):
    """ How far between a & b? """
    xa, ya, za, _ = a
    xb, yb, zb, _ = b
    return abs(xa - xb) + abs(ya - yb) + abs(za - zb)


def signal_overlap(a, b):
    if manhattan(a, b) <= abs(a[3] - b[3]):
        return True


def coord_limit(bots):
    xmin, ymin, zmin, rmin = float('inf'), float('inf'), float('inf'), float('inf')
    xmax, ymax, zmax, rmax = 0, 0, 0, 0
    for x, y, z, r in bots:
        xmin = min(x, xmin)
        xmax = max(x, xmax)
        ymin = min(y, ymin)
        ymax = max(y, ymax)
        zmin = min(z, zmin)
        zmax = max(z, zmax)
        rmin = min(r, rmin)
        rmax = max(r, rmax)
    return xmin, xmax, ymin, ymax, zmin, zmax, rmin, rmax
    # x: -140775920 to 233422174
    # y: -100772319 to 135708693
    # z: -111867275 to 148871027
    # r:   49994454 to  99869513


def next_value(_dict):
    return max(_dict.values()) + 1 if _dict else 1


def group_by_value(overlaps):
    new = defaultdict(list)
    for k, v in overlaps.items():
        new[v].append(k)
    return new


def find_overlaps(bots):
    overlaps = {}
    for a, b in permutations(bots, 2):
        if signal_overlap(a, b):
            if a not in overlaps and b not in overlaps:
                new_region = next_value(overlaps)
                overlaps[a] = new_region
                overlaps[b] = new_region
            elif a not in overlaps:
                overlaps[a] = overlaps[b]
            elif b not in overlaps:
                overlaps[b] = overlaps[a]
            else:  # Merge all of overlaps X into Y
                new = min(overlaps[b], overlaps[a])
                old = max(overlaps[b], overlaps[a])
                for k, v in overlaps.items():
                    if v == old:
                        overlaps[k] = new
    grouped = group_by_value(overlaps)
    pprint(len(grouped[1]))


def main():
    bots = read_input()
    ordered = sorted(bots, key=lambda x:x[3])
    strongest = ordered[-1]

    count = sum(in_range(strongest, other) for other in ordered)
    print(f'Part A: {count} - Number of nanobots in range of the strongest')

    find_overlaps(bots)

if __name__ == '__main__':
    main()

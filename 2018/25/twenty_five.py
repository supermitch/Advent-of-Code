#!/usr/bin/env python
from collections import defaultdict
from itertools import permutations


def read_input(path):
    with open(path) as f:
        data = [l.strip() for l in f]
        return [tuple(int(x) for x in coord.split(',')) for coord in data]


def manhattan(x, y):
    return sum(abs(y[axis] - x[axis]) for axis in range(4))


def calc_dists(stars):
    dists = defaultdict(lambda: defaultdict(int))
    for a, b in permutations(stars, 2):
        dists[a][b] = manhattan(a, b)
    return dists


def next_val(consts):
    return max(consts.values()) + 1 if consts else 1


def count_constellations(stars):
    dists = calc_dists(stars)
    consts = {}
    for a, pairs in dists.items():
        for b, dist in pairs.items():
            if dist <= 3:
                if a not in consts and b not in consts:
                    consts[a] = next_val(consts)
                    consts[b] = consts[a]
                elif a not in consts:
                    consts[a] = consts[b]
                elif b not in consts:
                    consts[b] = consts[a]
                else:  # Merge all of constellation X into Y
                    new = min(consts[b], consts[a])
                    old = max(consts[b], consts[a])
                    for k, v in consts.items():
                        if v == old:
                            consts[k] = new
    single_count = len([x for x in stars if x not in consts])
    const_count = len(set(consts.values()))
    return single_count + const_count


def main():
    stars = read_input('input.txt')
    total = count_constellations(stars)
    print(f'Part A: {total} - Total number of constellations')


if __name__ == '__main__':
    main()

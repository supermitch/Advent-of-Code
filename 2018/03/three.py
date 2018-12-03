#!/usr/bin/env python
"""
Day 3: No Matter How You Slice It
A. Find all cells that overlap, given several numbered areas
B. Find the only numbered area with no overlapping
"""
import re
from collections import defaultdict


def read_input():
    data = []
    with open('input.txt', 'r') as f:
        for line in f:
            data.append([int(x) for x in re.split('[#@, x:]', line) if x])
    return data


def build_grid(data):
    coords = defaultdict(list)
    for n, x, y, w, h in data:
        for i in range(x, x + w):
            for j in range(y, y + h):
                coords[(i, j)].append(n)
    return coords


def find_claim(coords):
    claims = set(list(range(1, 1310)))
    for nos in coords.values():
        if len(nos) > 1:
            for n in nos:
                if n in claims:
                    claims.remove(n)
    return claims.pop()  # Only one should remain


def main():
    data = read_input()
    coords = build_grid(data)
    overlaps = sum(len(v) > 1 for v in coords.values())
    print('Part A: {} - No of overlapping claim coords'.format(overlaps))
    claim = find_claim(coords)
    print('Part B: {} - The claim with no overlap'.format(claim))


if __name__ == '__main__':
    main()

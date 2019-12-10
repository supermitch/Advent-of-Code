#!/usr/bin/env python
import itertools as it
import collections as co
import math
from pprint import pprint

def read_input(path):
    data = {}
    with open(path) as f:
        for j, line in enumerate(f):
            for i, char in enumerate(list(line.strip())):
                if char == '#':
                    data[(i, j)] = '#'
    return data

def next_angle(theta, bangles):
    if theta > 180:
        for angle in bangles:
            if angle < theta:
                return angle
        theta = 180
    for angle in bangles:
        if angle < theta:
            return angle

def dist(a, b):
    ax, ay = a
    bx, by = b
    return math.sqrt((abs(ax - bx)**2) + (abs(ay - by)**2))

def nearest(booms, x):
    return sorted(booms, key=lambda b: dist(b, x))

def main():
    path = 'input.txt'
    #path = 'test_a.txt'
    #path = 'test_b.txt'
    #
    data = read_input(path)

    angles = co.defaultdict(list)
    for a, b in it.permutations(data.keys(), 2):
        ax, ay = a
        bx, by = b
        opp = by - ay
        adj = bx - ax
        if adj == 0 and opp > 0:
            theta = 90
        elif adj == 0 and opp < 0:
            theta = 270
        else:
            theta = math.degrees(math.atan2(opp, adj))
        angles[a].append(theta)
    maxi = 0
    for k, v in angles.items():
        print(k, len(set(v)))
        maxi = max(maxi, len(set(v)))
    print(maxi)

    base = (19, 11)
    # base = (8, 3)
    # base = (11, 13)

    bangles = co.defaultdict(list)
    total = 0
    for b in data.keys():
        if b == base:
            continue
        ax, ay = base
        bx, by = b
        opp = ay - by
        adj = bx - ax
        if adj == 0 and opp > 0:
            theta = 90
        elif adj == 0 and opp < 0:
            theta = 270
        else:
            theta = math.degrees(math.atan2(opp, adj))
        bangles[theta].append((bx, by))
        total += 1

    keys = co.deque(sorted(bangles, reverse=True))
    while keys[0] != 90:
        keys.rotate()

    theta = 90
    asters = []
    while True:
        print(theta)
        if theta in bangles:
            if bangles[theta]:
                booms = bangles[theta]
                booms = nearest(booms, base)
                asters.append(booms[0])
                bangles[theta] = booms[1:]
            keys.rotate(-1)
            theta = keys[0]
        if len(asters) == total:
            break
    print(asters)

    print(asters[199])




if __name__ == '__main__':
    main()

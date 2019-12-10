#!/usr/bin/env python
from itertools import permutations
import collections
import math


def read_input(path):
    data = []
    with open(path) as f:
        for y, line in enumerate(f):
            for x, char in enumerate(list(line.strip())):
                if char == '#':
                    data.append((x, y))
    return data


def calc_angle(a, b):
    ax, ay = a
    bx, by = b
    opp = ay - by
    adj = bx - ax
    if adj == 0 and opp > 0:
        theta = 90
    elif adj == 0 and opp < 0:
        theta = 270
    else:
        theta = math.degrees(math.atan2(opp, adj))
    return theta


def distance(a, b):
    return math.sqrt((abs(a[0] - b[0])**2) + (abs(a[1] - b[1])**2))


def nearest(booms, x):
    return sorted(booms, key=lambda b: distance(b, x))


def get_target_angles(base, data):
    angles = collections.defaultdict(list)
    for b in data:
        if b == base:
            continue
        theta = calc_angle(base, b)
        angles[theta].append(b)
    return angles


def shoot_asteroids(base, data):
    angles = get_target_angles(base, data)

    positions = collections.deque(sorted(angles, reverse=True))
    while positions[0] != 90:  # Align the laser
        positions.rotate()

    asteroids = []
    while len(asteroids) < len(data) - 1:
        theta = positions[0]
        if angles[theta]:
            targets = nearest(angles[theta], base)
            asteroids.append(targets.pop(0))
        positions.rotate(-1)
    return asteroids

def main():
    data = read_input('input.txt')

    angles = collections.defaultdict(set)
    for a, b in permutations(data, 2):
        angles[a].add(calc_angle(a, b))
    base, visible = sorted(angles.items(), key=lambda kv: len(kv[1]))[-1]
    print(f'Part A: {len(visible)} - Max visible asteroids from base {base}')

    asteroids = shoot_asteroids(base, data)
    x, y = asteroids[199]
    print(f'Part B: {x * 100 + y} - Code for 200th asteroid ({x}, {y})')




if __name__ == '__main__':
    main()

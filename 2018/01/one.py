#!/usr/bin/env python
"""
Day 1: Chronal Calibration

A. Sum a list of values, e.g. +1, -2
B. Find the first calculated value that repeats. Repeat input as required.
"""

def find_repeat(data):
    freq = 0
    seen = set()
    while True:
        for val in data:
            freq += val
            if freq in seen:
                return freq
            seen.add(freq)


def main():
    with open('input.txt', 'r') as f:
        data = [int(l.strip()) for l in f]

    print('Part A: {} - Resulting frequency'.format(sum(data)))
    print('Part B: {} - First duplicate frequency'.format(find_repeat(data)))


if __name__ == '__main__':
    main()

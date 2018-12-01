#!/usr/bin/env python
"""
Day 1: Chronal Calibration

A. Sum a list of values, e.g. +1, -2
B. Find the first calculated value that repeats. Repeat input as required.
"""

def main():
    with open('input.txt', 'r') as f:
        data = [l.strip() for l in f]

    freq = 0
    seen = set()
    duplicate = None
    result = None
    while True:
        for val in data:
            freq += int(val)
            if freq in seen:
                duplicate = freq
                break
            seen.add(freq)
        else:
            if not result:
                result = freq
        if duplicate:
            break

    print('Part A: {} - Resulting frequency'.format(result))
    print('Part B: {} - First duplicate frequency'.format(duplicate))


if __name__ == '__main__':
    main()

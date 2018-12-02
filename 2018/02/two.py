#!/usr/bin/env python
"""
Day 2: Inventory Management System

A. Multiply the counts of words with 2 and 3 character repeats
B. Find two words with only exactly 1 differing character
"""
from collections import Counter
from itertools import combinations


def two_three_checksum(data):
    twos = 0
    threes = 0
    for line in data:
        c = Counter(line)  # Count the chars
        if 2 in c.values():
            twos += 1
        if 3 in c.values():
            threes += 1
    return twos * threes


def find_boxes(data):
    for a, b in combinations(data, 2):
        matching = ''  # construct the matching word
        for i, c in enumerate(a):
            if c == b[i]:  # Compare the two strings
                matching += c
        if len(matching) == len(a) - 1:  # Only one wrong char
            return matching


def main():
    with open('input.txt', 'r') as f:
        data = [l.strip() for l in f]

    checksum = two_three_checksum(data)
    print('A: {} - The 2 x 3 checksum'.format(checksum))

    matching = find_boxes(data)
    print('B: {} - The matching box characters'.format(matching))


if __name__ == '__main__':
    main()

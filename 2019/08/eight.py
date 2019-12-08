#!/usr/bin/env python
import re
import itertools as it
import collections

def parse(l):
    return [int(x) for x in l.split()]

def main():
    with open('input.txt') as f:
        data = list(str(next(f).strip()))

    layers = []
    for i in range(100):
        lay_dat = data[(0 + i) * 150: (i + 1) * 150]
        rows = []
        for j in range(6):
            rows.append(lay_dat[(0 + j) * 25: (j + 1) * 25])
        layers.append(rows)

    for i, layer in enumerate(layers):
        total = 0
        for rows in layer:
            for row in rows:
                count = sum(x == '0' for x in row)
                total += count

    layer = layers[15]
    ones = 0
    twos = 0
    for rows in layer:
        for row in rows:
            one = sum(x == '1' for x in row)
            two = sum(x == '2' for x in row)
            ones += one
            twos += two
    print(f"Part A: {ones * twos} - Count of 1's x no. of 2's")

    arr = [[' ' for x in range(25)] for y in range(6)]
    for rows in layers[::-1]:
        for i, row in enumerate(rows):
            for j, char in enumerate(row):
                if char == '1':
                    arr[i][j] = ' '
                elif char == '0':
                    arr[i][j] = '█'

    print('█' * 27)
    for row in arr:
        print(''.join(['█'] + row + ['█']))
    print('█' * 27)

    print('Part B: CJZHR - Decoded message')


if __name__ == '__main__':
    main()

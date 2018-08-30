#!/usr/bin/env python

import itertools


def calculate(init, row, col):
    for d in itertools.count(start=1):  # Infinite series of diagonals
        for k in range(0, d + 1):
            val = init * 252533 % 33554393
            if d - k == row and k == col:
                return val
            init = val


def main():
    init = 20151125
    row, col = (3010, 3019)
    value = calculate(init, row - 1, col - 1)
    print('Part A: {} - Value at row {} and col {}'.format(value, row, col))


if __name__ == '__main__':
    main()

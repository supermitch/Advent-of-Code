#!/usr/bin/env python

import itertools


def calculate(init, row, col):
    for d in itertools.count(start=1):  # Infinite series of diagonals
        for k in range(0, d + 1):
            val = init * 252533 % 33554393
            if d - k == 3009 and k == 3018:  # row = d-k, col = k
                return val
            init = val


def main():
    init = 20151125
    row = 3010
    col = 3019
    value = calculate(init, row, col)
    print('Part A: {} - Value at row {} and col {}'.format(value, row, col))


if __name__ == '__main__':
    main()

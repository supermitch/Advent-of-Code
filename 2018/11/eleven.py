#!/usr/bin/env python
from collections import defaultdict


def calc_power(x, y, serial):
    power = ((x + 10) * y + serial) * (x + 10)
    return ((power // 100) % 10) - 5


def main():
    serial = 1133

    assert calc_power(3, 5, 8) == 4
    assert calc_power(122, 79, 57) == -5
    assert calc_power(217, 196, 39) == 0

    powers = {}
    for x in range(1, 301):
        for y in range(1, 301):
            powers[(x, y)] = calc_power(x, y, serial)

    totals = defaultdict(int)
    max_power = 0
    squares = {}
    for size in range(1, 301):
        print('Size: {}'.format(size))
        for x in range(1, 301 - size):
            for y in range(1, 301 - size):
                total = 0
                if (x, y) not in squares:
                    squares[(x, y)] = powers[(x, y)]
                for dx in range(size):
                    for dy in range(size):
                        x2, y2 = x + dx, y + dy
                        total += powers[(x2, y2)]
                squares[(x, y)] = total
                nx = x + size - 1
                for ny in range(y, y + size - 1):
                    squares[(x, y)] += powers[(nx, ny)]
                ny = t + size - 1
                for nx in range(x, x + size - 1):
                    squares[(x, y)] += powers[(nx, ny)]

                if total > max_power:
                    max_dims = (x, y)
                    max_power = total
                    max_size = size

    print(max_dims, max_power, size)



if __name__ == '__main__':
    main()

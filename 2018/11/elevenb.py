#!/usr/bin/env python
from collections import defaultdict


def calc_power(x, y, serial):
    power = ((x + 10) * y + serial) * (x + 10)
    return ((power // 100) % 10) - 5


def main():
    import time
    tic = time.clock()
    serial = 1133

    assert calc_power(3, 5, 8) == 4
    assert calc_power(122, 79, 57) == -5
    assert calc_power(217, 196, 39) == 0

    n = 300
    powers = [[0 for _ in range(n)] for _ in range(n)]
    squares = [[0 for _ in range(n)] for _ in range(n)]

    for x in range(0, 300):
        for y in range(0, 300):
            powers[x][y] = calc_power(x+1, y+1, serial)
            squares[x][y] = powers[x][y]

    max_power = 0
    for size in range(2, 301):
        print('Size: {}'.format(size))
        for x in range(0, 300 - size):
            for y in range(0, 300 - size):
                nx = x + size
                ny = y + size
                squares[x][y] += sum(powers[nx-1][y:ny])
                squares[x][y] += sum(powers[i][ny-1] for i in range(x, nx))
                squares[x][y] -= powers[nx-1][ny-1]

                if squares[x][y] > max_power:
                    max_dims = (x + 1, y + 1)
                    max_power = squares[x][y]
                    max_size = size

    print('{},{},{}'.format(max_dims[0], max_dims[1], max_size))
    # Not 236,227,15 or 14
    print('elapsed', time.clock() - tic)



if __name__ == '__main__':
    main()

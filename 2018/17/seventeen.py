#!/usr/bin/env python
import re

def parse(l):
    a, b, c = [int(x) for x in re.sub('[^0-9]', ' ', l).split()]
    if l[0] == 'x':
        span = [(a, x) for x in range(b, c + 1)]
    else:
        span = [(x, a) for x in range(b, c + 1)]
    return span

def is_bounded(grid, x, y):
    if grid[y + 1][x] != '#':
        return False
    while True:
        x += 1
        if grid[y][x] == '#':
            break
        else:
            if grid[y + 1][x] != '#':
                return False
    while True:
        x -= 1
        if grid[y][x] == '#':
            break
        else:
            if grid[y + 1][x] != '#':
                return False

def draw(water, grid, xmin):
    for y, row in enumerate(grid):
        line = ''
        for x, col in enumerate(row[xmin - 5:], start=xmin - 5):
            flow = water[y][x]
            line += flow if flow else col
        print(line)

class Drop:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.settle = False

    def update(self, grid, water):
        # try to move down
        nx, ny = self.x, self.y + 1
            if grid[ny][nx] in ('.', '|'):
                self.x = nx, self.y = ny
                grid[ny][nx] == '|'
                continue
            elif grid[ny][nx] in ('#', '~'):
                while True:
                    nx, ny = self.x + 1, self.y
                    if grid[ny][nx] in ('.', '|'):
                        grid[ny][nx] = '|'
                        self.x, self.y = nx, ny
                    elif grid[ny][nx] in ('#', '~'):


def main():
    with open('input.txt') as f:
        data = [parse(l.strip()) for l in f]
    print(data[0])

    xmax = 0
    xmin = 99999
    ymax = 0
    ymin = 99999
    for span in data:
        for x, y in span:
            if x < xmin:
                xmin = x
            if x > xmax:
                xmax = x
            if y > ymax:
                ymax = y
            if y < ymin:
                ymin = y
    print('Limits:', xmin, xmax, ymin, ymax)

    grid = [['.' for x in range(xmax + 1)] for y in range(ymax + 1)]
    grid[0][500] = '+'
    water = [[None for x in range(xmax + 1)] for y in range(ymax + 1)]

    for span in data:
        for x, y in span:
            grid[y][x] = '#'


    draw(water, grid, xmin)

    while True:
        drop = Drop(500, 0)
        while not drop.settle:
            drop.update(grid)

if __name__ == '__main__':
    main()

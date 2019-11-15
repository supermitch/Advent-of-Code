#!/usr/bin/env python
import re


def parse(l):
    a, b, c = [int(x) for x in re.sub('[^0-9]', ' ', l).split()]
    if l[0] == 'x':
        span = [(a, x) for x in range(b, c + 1)]
    else:
        span = [(x, a) for x in range(b, c + 1)]
    return span


def find_limits(data):
    xmin, xmax, ymin, ymax = float('inf'), 0, float('inf'), 0
    for span in data:
        for x, y in span:
            xmin = min(x, xmin)
            xmax = max(x, xmax)
            ymax = max(y, ymax)
            ymin = min(y, ymin)
    return xmin, xmax, ymin, ymax


def generate_grid(data, xmax, ymax):
    grid = [[' ' for x in range(xmax + 1)] for y in range(ymax+ 1)]
    for span in data:
        for x, y in span:
            grid[y][x] = '#'
    grid[0][500] = '+'  # Original source
    return grid


def is_bounded(grid, xi, y):
    """ Is a floor bounded on both sides by walls? Return bounded coords. """
    assert grid[y + 1][xi] in '~#'
    coords = []
    x = xi
    while grid[y + 1][x] in '~#' and grid[y][x] not in '~#':
        coords.append((x, y))
        x += 1
    if grid[y][x] not in '~#':
        return False
    x = xi
    while grid[y + 1][x] in '~#' and grid[y][x] not in '~#':
        coords.append((x, y))
        x -= 1
    if grid[y][x] not in '~#':
        return False
    for x, y in coords:
        grid[y][x] = '~'
    return True


def flow_grid(grid, xi, y):
    x = xi
    new_drops = []
    while grid[y + 1][x] in '~#' and grid[y][x] not in '~#':
        grid[y][x] = '|'
        x += 1
    if grid[y][x] not in '~#':
        grid[y][x] = '|'
        new_drops.append((x, y))
    x = xi
    while grid[y + 1][x] in '~#' and grid[y][x] not in '~#':
        grid[y][x] = '|'
        x -= 1
    if grid[y][x] not in '~#':
        grid[y][x] = '|'
        new_drops.append((x, y))
    return new_drops


def draw(grid, xmin):
    string_grid = ''
    for row in grid:
        line = ''
        for col in row[xmin - 5:]:
            line += col
        string_grid += line + '\n'
    print(string_grid)


class Drop:
    def __init__(self, x, y, grid):
        self.x = x
        self.y = y
        self.grid = grid

    def flow(self):
        while True:
            try:
                if self.grid[self.y + 1][self.x] in '~#':
                    break
                elif self.grid[self.y + 1][self.x] in '|':
                    return []
            except IndexError:
                return []
            self.y += 1
            self.grid[self.y][self.x] = '|'
        if is_bounded(self.grid, self.x, self.y):
            return [(self.x, self.y - 1)]
        else:
            return flow_grid(self.grid, self.x, self.y)


def count_water(grid, ymin, ymax):
    flow = 0
    flood = 0
    for row in grid[ymin:ymax + 1]:
        for cell in row:
            if cell == '|':
                flow += 1
            elif cell in '~':
                flood += 1
    return flow, flood


def main():
    with open('input.txt') as f:
        data = [parse(l.strip()) for l in f]

    _, xmax, ymin, ymax = find_limits(data)

    grid = generate_grid(data, xmax, ymax)

    drops = [Drop(500, 0, grid)]
    while drops:
        new_drops = []
        for drop in drops:
            res = drop.flow()
            new_drops.extend([Drop(d[0], d[1], grid) for d in res])
        drops = new_drops

    flow, flood = count_water(grid, ymin, ymax)
    print(f'Part A: {flow + flood} - Total water in sand')
    print(f'Part B: {flood} - Retained water after spring dries up')


if __name__ == '__main__':
    main()

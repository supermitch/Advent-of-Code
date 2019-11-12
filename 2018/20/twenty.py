#!/usr/bin/env python
def add_map_step(start, grid, step):
    x, y = start
    dx, dy = {
        'N': (-1, 0),
        'E': (0, 1),
        'S': (1, 0),
        'W': (0, -1),
    }[step]
    x, y = x + dx, y + dy
    if step in 'EW':
        door = '|'
    else:
        door = '-'
    grid[(x, y)] = door
    x, y = x + dx, y + dy
    grid[(x, y)] = '.'
    return (x, y), grid


def draw(grid):
    xmin = min(x for x, y in grid)
    xmax = max(x for x, y in grid)
    ymin = min(y for x, y in grid)
    ymax = max(y for x, y in grid)
    for x in range(xmin, xmax + 1):
        line = ''
        for y in range(ymin, ymax + 1):
            try:
                line += grid[(x, y)]
            except KeyError:
                line += '?'
        print(line)


def extract_options(data):
    options = []
    left = 0
    leg = []
    for c in data:
        if c == '(':
            left += 1
        elif c == ')':
            left -= 1
        elif c == '|':
            if left == 0:
                options.append(leg)
                leg = []
                continue
        leg.append(c)
    if leg:
        options.append(leg)
    return options


def extract_path(data):
    new = []
    left = 1
    for c in data[1:]:
        if c == '(':
            left += 1
        elif c == ')':
            left -= 1
            if left == 0:
                new_data = ''.join(new)
                return ''.join(new), data[len(new_data) + 2:]
        new.append(c)


def cheapest(costs, unvisited):
    for coord, _ in sorted(costs.items(), key=lambda x: x[1]):
        if coord in unvisited:
            return coord


def dijkstras(grid):
    x, y = (0, 0)
    costs = {k: float('Inf') for k, v in grid.items() if v in 'X.'}
    unvisited = set([k for k, v in grid.items() if v in 'X.'])
    coord = (x, y)
    costs[coord] = 0
    route = {coord: None}
    while True:
        current_cost = costs[coord]
        x, y = coord
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            door = (x + dx, y + dy)
            if door in grid and grid[door] in '|-':
                nxt = (x + dx * 2, y + dy * 2)
                if nxt in unvisited:
                    tentative_cost = current_cost + 1
                    if tentative_cost < costs[nxt]:
                        costs[nxt] = tentative_cost
                        route[nxt] = coord
        unvisited.remove(coord)
        if not unvisited:
            return costs
        coord = cheapest(costs, unvisited)


def main():
    with open('input.txt') as f:
        data = f.readline().strip()[1:-1]
    grid = {(0, 0): 'X'}
    graph = [((0,0), data)]
    while graph:
        coord, data = graph.pop()
        while data:
            step = data[0]
            if step == '(':
                leg, data = extract_path(data)
                for option in extract_options(leg):
                    graph.append((coord, option))
            else:
                coord, grid = add_map_step(coord, grid, step)
                data = data[1:]
    costs = dijkstras(grid)
    costs = sorted(costs.items(), key=lambda x: x[1])
    longest = costs[-1][1]
    print(f'Part A: {longest} - Longest shortest path')
    rooms = sum(1 for k, v in costs if v >= 1000)
    print(f'Part B: {rooms} - Rooms over 1000 doors from start')


if __name__ == '__main__':
    main()

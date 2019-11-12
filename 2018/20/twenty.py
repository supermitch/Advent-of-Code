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
                print('new data', new_data, data[len(new_data) + 2:])
                return ''.join(new), data[len(new_data) + 2:]
        new.append(c)
    raise ValueError('Did not found matching bracket')


def main():
    with open('input.txt') as f:
        data = f.readline().strip()[1:-1]

    data = 'ENWWW(NEEE|SSE(EE|N)|W)'
    # data = 'ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN'
    coord = (0, 0)
    grid = {coord: 'X'}

    graph = [((0,0), data)]
    while graph:
        coord, data = graph.pop()
        while data:
            print(coord, data)
            draw(grid)
            step = data[0]
            if step == '(':
                leg, data = extract_path(data)
                for option in extract_options(leg):
                    graph.append((coord, option))
                print('graph:', graph)
            else:
                coord, grid = add_map_step(coord, grid, step)
                data = data[1:]


if __name__ == '__main__':
    main()

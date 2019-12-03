#!/usr/bin/env python


def get_steps(moves, grid, junctions):
    x, y = 0, 0
    steps = 0
    taken = {}
    for move in moves:
        d = move[0]
        dist = int(move[1:])

        if d == 'R':
            for i in range(1, dist + 1):
                steps += 1
                coord = (x + i, y)
                if coord in junctions:
                    taken[coord] = steps
            x = x + i
        elif d == 'L':
            for i in range(1, dist + 1):
                steps += 1
                coord = (x - i, y)
                if coord in junctions:
                    taken[coord] = steps
            x = x - i
        elif d == 'U':
            for i in range(1, dist + 1):
                steps += 1
                coord = (x, y + i)
                if coord in junctions:
                    taken[coord] = steps
            y = y + i
        elif d == 'D':
            for i in range(1, dist + 1):
                steps += 1
                coord = (x, y - i)
                if coord in junctions:
                    taken[coord] = steps
            y = y - i
    return taken


def main():
    with open('input.txt') as f:
        one = [x for x in next(f).split(',')]
        two = [x for x in next(f).split(',')]

    g_one = {}
    x, y = 0, 0
    g_one[(0, 0)] = 'o'
    for move in one:
        d = move[0]
        dist = int(move[1:])

        if d == 'R':
            for i in range(dist):
                g_one[(x + i + 1, y)] = '-'
            x = x + i + 1
        elif d == 'L':
            for i in range(dist):
                g_one[(x - (i + 1), y)] = '-'
            x = x - i - 1
        elif d == 'U':
            for i in range(dist):
                g_one[(x, y + i + 1)] = '|'
            y = y + i + 1
        elif d == 'D':
            for i in range(dist):
                g_one[(x, y - (i + 1))] = '|'
            y = y - i - 1

    g_two = {}
    x, y = 0, 0
    g_two[(0, 0)] = 'o'
    for move in two:
        d = move[0]
        dist = int(move[1:])

        if d == 'R':
            for i in range(dist):
                g_two[(x + i + 1, y)] = '-'
            x = x + i + 1
        elif d == 'L':
            for i in range(dist):
                g_two[(x - (i + 1), y)] = '-'
            x = x - i - 1
        elif d == 'U':
            for i in range(dist):
                g_two[(x, y + i + 1)] = '|'
            y = y + i + 1
        elif d == 'D':
            for i in range(dist):
                g_two[(x, y - (i + 1))] = '|'
            y = y - i - 1

    junctions = []
    max_man = float('inf')
    max_coord = None
    for coord in g_one:
        if coord == (0, 0):
            continue
        if coord in g_two:
            junctions.append(coord)
            man = abs(coord[0]) + abs(coord[1])
            if man < max_man:
                max_man = man
                max_coord = coord

    print(max_coord, max_man)

    steps_one = get_steps(one, g_one, junctions)
    steps_two = get_steps(two, g_two, junctions)

    for coord, steps in steps_one.items():
        print(coord, steps, steps_two[coord], steps + steps_two[coord])

if __name__ == '__main__':
    main()

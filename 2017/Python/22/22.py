def rotate(v, rotation):
    return (-v[1], v[0]) if rotation == 'L' else (v[1], -v[0])


def part_a(data, x, y, limit):
    dir = -1, 0  # Up
    infected = 0
    for _ in range(limit):
        cell = data.get((x, y), '.')
        if cell == '.':
            data[x, y] = '#'
            infected += 1
            dir = rotate(dir, 'L')
        elif cell == '#':
            data[x, y] = '.'
            dir = rotate(dir, 'R')
        x, y = x + dir[0], y + dir[1]
    return infected


def part_b(data, x, y, limit):
    dir = -1, 0  # Up
    infected = 0
    for _ in range(limit):
        cell = data.get((x, y), '.')
        if cell == '.':
            data[x, y] = 'W'
            dir = rotate(dir, 'L')
        elif cell == 'W':
            data[x, y] = '#'
            infected += 1
        elif cell == '#':
            data[x, y] = 'F'
            dir = rotate(dir, 'R')
        elif cell == 'F':
            data[x, y] = '.'
            dir = rotate(rotate(dir, 'R'), 'R')
        x, y = x + dir[0], y + dir[1]
    return infected


def main():
    test = {(0,2): '#', (1,0): '#'}
    assert part_a(test.copy(), 1, 1, 70) == 41
    assert part_b(test.copy(), 1, 1, 100) == 26

    data = {}
    with open('22.input', 'r') as f:
        for x, line in enumerate(f):
            for y, char in enumerate(line.strip()):
                data[(x, y)] = char

    infected_a = part_a(data.copy(), 12, 12, 10000)
    print('Part A: {} - No. of infected nodes'.format(infected_a))

    infected_b = part_b(data.copy(), 12, 12, 10000000)
    print('Part B: {} - Evolved virus infections'.format(infected_b))


if __name__ == '__main__':
    main()

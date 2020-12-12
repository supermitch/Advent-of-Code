def rotate(a, b, rotation):
    """ 90 deg vector rotation. """
    return (-b, a) if rotation == 'L' else (b, -a)


def part_a(data, waypoint=False):
    x, y = 0, 0
    if waypoint:
        vx, vy = 10, 1
    else:
        vx, vy = 1, 0
    for mv, val in data:
        if mv == 'F':
            x += vx * val
            y += vy * val
        elif mv == 'N':
            if waypoint:
                vy += val
            else:
                y += val
        elif mv == 'S':
            if waypoint:
                vy -= val
            else:
                y -= val
        elif mv == 'E':
            if waypoint:
                vx += val
            else:
                x += val
        elif mv == 'W':
            if waypoint:
                vx -= val
            else:
                x -= val
        if mv in 'LR':
            for _ in range(val // 90):
                vx, vy = rotate(vx, vy, mv)
    return abs(x) + abs(y)


def main():
    with open('input.txt') as f:
        data = [(x[0], int(x[1:])) for x in f]

    print(f'Part A: {part_a(data)}')
    print(f'Part B: {part_a(data, waypoint=True)}')


if __name__ == '__main__':
    main()

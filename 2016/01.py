def rotate(v, rotation):
    """ 90 deg vector rotation. """
    if rotation == 'L':
        return -v[1], v[0]
    elif rotation == 'R':
        return v[1], -v[0]
    else:
        print(f'Uhm... {rotation}')


def run_steps(steps):
    x, y = (0, 0)
    v = (0, 1)
    visited = set([(x, y)])
    found = False
    for step in steps:
        o = step[0]  # L or R
        d = int(step[1:])  # Distance
        v = rotate(v, o)
        for _ in range(d):
            x += v[0]
            y += v[1]
            if (x, y) in visited and not found:
                print('Part B: Saw {} twice'.format((x, y)))
                found = True  # Only print this once
            visited.add((x, y))
    return x, y


def main():
    assert run_steps(['R2', 'R2', 'R2']) == (0, -2)

    with open('01.input', 'r') as f:
        steps = f.read().strip().split(', ')

    x, y = run_steps(steps)
    dist = abs(x) + abs(y)
    print('Part A: {} - End position {} distance'.format(dist, (x, y)))

    (x, y) = (123, 3)  # First repeat coordinate
    dist = abs(x) + abs(y)
    print('Part B: {} - Distance to first repeat {}'.format(dist, (x, y)))


if __name__ == '__main__':
    main()

#!/usr/bin/env python
def read_lights(f):
    return [line.strip() for line in f]


def neighbours_on(r, c, lights):
    count = 0
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            nr, nc = r + dr, c + dc
            if nr < 0 or nc < 0:  # Don't go below bounds
                continue
            if nr == r and nc == c:  # Ignore our current coord
                continue
            try:
                count += 1 if lights[nr][nc] == '#' else 0
            except IndexError:  # Out of bounds
                continue
    return count


def get_bulb(r, c, lights):
    if lights[r][c] == '#' and neighbours_on(r, c, lights) in (2, 3):
        return '#'
    elif lights[r][c] == '.' and neighbours_on(r, c, lights) == 3:
        return '#'
    else:
        return '.'


def animate(lights, stuck_corners=False):
    new_lights = []
    n = len(lights)
    for r in range(n):
        new_row = []
        for c in range(n):
            if stuck_corners and (r, c) in [(0, 0), (0, n - 1), (n - 1, 0), (n - 1, n - 1)]:  # Four corners
                new_row.append('#')  # Always on
            else:
                new_row.append(get_bulb(r, c, lights))
        new_lights.append(new_row)
    return new_lights


def count_on(lights):
    return sum(bulb == '#' for row in lights for bulb in row)


def main():
    test = [
        '.#.#.#',
        '...##.',
        '#....#',
        '..#...',
        '#.#..#',
        '####..',
    ]
    lights = read_lights(test)
    assert neighbours_on(2, 4, lights) == 3
    assert neighbours_on(2, 0, lights) == 0
    assert neighbours_on(0, 2, lights) == 3
    assert count_on(test) == 15
    assert get_bulb(0, 2, lights) == '#'
    assert get_bulb(2, 0, lights) == '.'
    for _ in range(4):
        lights = animate(lights)
    assert count_on(lights) == 4

    with open('input.txt', 'r') as f:
        lights = read_lights(f)
    for _ in range(100):
        lights = animate(lights)
    print('Part A: {} - Lights on after 100 frames'.format(count_on(lights)))

    with open('input.txt', 'r') as f:
        lights = read_lights(f)
        n = len(lights) - 1
        lights[0] = '#' + lights[0][1:-1] + '#'  # Turn on four corners
        lights[n] = '#' + lights[n][1:-1] + '#'
    for _ in range(100):
        lights = animate(lights, stuck_corners=True)
    print('Part B: {} - Lights on after 100 frames w/ stuck corners'.format(count_on(lights)))


if __name__ == '__main__':
    main()

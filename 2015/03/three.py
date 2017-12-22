from collections import defaultdict


def go(p, move):
    dx, dy = {
        '>': (1, 0),
        'v': (0, -1),
        '<': (-1, 0),
        '^': (0, 1),
    }[move]
    return p[0] + dx, p[1] + dy


def part_a(moves):
    x, y = 0, 0
    delivered = defaultdict(int)
    for move in moves:
        delivered[(x, y)] += 1
        x, y = go((x, y), move)
    return len(delivered)


def part_b(moves):
    santa = 0, 0
    robot = 0, 0
    x, y = santa
    delivered = defaultdict(int)
    for i, move in enumerate(moves):
        delivered[(x, y)] += 1
        if not i % 2:
            santa = go(santa, move)
            x, y = santa
        else:
            robot = go(robot, move)
            x, y = robot
    return len(delivered)


def main():
    with open('input.txt', 'r') as f:
        moves = list(f.readline().strip())

    print('Part A: {} - Visits by Santa only'.format(part_a(moves)))
    print('Part B: {} - Visits by Santa + Robo-Santa'.format(part_b(moves)))


if __name__ == '__main__':
    main()

from collections import deque
import re


def parse(line):
    if 'rect' in line:
        m = re.match(r".* ([0-9]+)x([0-9]+)", line)
        move, a, b = 'rect', int(m[1]), int(m[2])
    else:
        m = re.match(r".*(row|column) .*=([0-9]+) by ([0-9]+)", line)
        move, a, b = m[1], int(m[2]), int(m[3])
    return move, a, b


def execute(screen, moves):
    screen = screen[:]
    for move, a, b in moves:
        if move == 'rect':
            for row in range(b):
                for col in range(a):
                    screen[row][col] = '#'
        elif move == 'row':
            d = deque(screen[a])
            d.rotate(b)
            screen[a] = list(d)
        elif move == 'column':
            d = deque([row[a] for row in screen])
            d.rotate(b)
            for row, elem in zip(screen, d):
                row[a] = elem
    return screen


def main():
    with open('input.txt', 'r') as f:
        moves = [parse(line) for line in f]

    w, h = 50, 6
    screen = [[' '] * w for x in range(h)]

    screen = execute(screen, moves)

    lit = sum(x == '#' for row in screen for x in row)

    print('Part A: {} - No. of lit lights'.format(lit))

    print('Part B:')
    for row in screen:
        print(''.join(row))


if __name__ == '__main__':
    main()

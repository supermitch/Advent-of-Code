def find_code(lines, keypad, start):
    deltas = {
        'L': (-1, 0),
        'R': (1, 0),
        'U': (0, -1),  # +y axis is down
        'D': (0, 1),
    }
    x, y = start
    code = []
    for line in lines:
        for move in line:
            dx, dy = deltas[move]
            x2, y2 = x + dx, y + dy
            if 0 <= x2 < len(keypad) and 0 <= y2 < len(keypad[0]) and keypad[x2][y2] is not None:
                x, y = x2, y2
            else:
                x, y = x, y
            val = keypad[x][y]
        code.append(val)
    return ''.join(str(x) for x in code)


def main():
    keypad = [  # (0, 0) is # 1
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
    ]
    test = ['ULL', 'RRDDD', 'LURDL', 'UUUUD']
    assert find_code(test, keypad, (1, 1)) == '1985'

    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f]

    part_a = find_code(lines, keypad, (1, 1))
    print('Part A: {} - Bathroom code'.format(part_a))

    diamond = [
        [None, None, 5, None, None],
        [None, 2, 6, 'A', None],
        [1, 3, 7, 'B', 'D'],
        [None, 4, 8, 'C', None],
        [None, None, 9, None, None],
    ]
    part_b = find_code(lines, diamond, (0, 2))
    print('Part B: {} - Diamond code'.format(part_b))


if __name__ == '__main__':
    main()

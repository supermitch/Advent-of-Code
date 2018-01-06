import math


def parse_line(line):
    parts = line.split(' => ')
    input = [list(s) for s in parts[0].split('/')]
    output = [list(s) for s in parts[1].split('/')]
    return input, output


def cat(s):
    lines = [''.join(row) for row in s]
    return '/'.join(lines)


def rotate(p):
    """ Rotate a 2x2 or 3x3 matrix to the right. """
    if len(p) == 2:
        return [
            [p[1][0], p[0][0]],
            [p[1][1], p[0][1]],
        ]
    elif len(p) == 3:
        return [
            [p[2][0], p[1][0], p[0][0]],
            [p[2][1], p[1][1], p[0][1]],
            [p[2][2], p[1][2], p[0][2]],
        ]


def flip(p):
    """ Left to right array mirroring. """
    new_arr = []
    for row in p:
        new_r = row[:]
        new_r.reverse()
        new_arr.append(new_r)
    return new_arr


def find_rule(rules, part):
    rules = {cat(input): output for input, output in rules}
    for _ in range(4):  # Four options for orientation
        if cat(part) in rules:
            output = rules[cat(part)]
            return output
        elif cat(flip(part)) in rules:  # Alternatively try mirror
            output = rules[cat(flip(part))]
            return output
        else:
            part = rotate(part)


def divide(arr):
    """ Break big matrix into smaller 2x2 or 3x3 matrices. """
    parts = []
    if not len(arr) % 2:
        for r in range(0, len(arr), 2):
            for c in range(0, len(arr), 2):
                new = [
                    arr[r + 0][c: c + 2],
                    arr[r + 1][c: c + 2],
                ]
                parts.append(new)
        return parts
    elif not len(arr) % 3:
        for r in range(0, len(arr), 3):
            for c in range(0, len(arr), 3):
                new = [
                    arr[r][c: c + 3],
                    arr[r + 1][c: c + 3],
                    arr[r + 2][c: c + 3],
                ]
                parts.append(new)
        return parts


def reassemble(parts):
    """ Reassemble many small parts into one big (square) array. """
    n = len(parts)  # no of parts
    s = len(parts[0])  # part size
    size = int(n ** 0.50)  # e.g. 9 parts is a 3 x 3 arrangement
    rows = s * size
    new = [[] for _ in range(rows)]
    for i, part in enumerate(parts):
        set = math.floor(i/size)
        for j, row in enumerate(part):
            new[set * s + j].extend(row)
    return new


def enhance_art(rules, iterations):
    arr = [
        list('.#.'),
        list('..#'),
        list('###'),
    ]
    for _ in range(iterations):
        parts = divide(arr)
        new_parts = []
        for part in parts:
            output = find_rule(rules, part)
            new_parts.append(output)
        arr = reassemble(new_parts)
    return sum(c == '#' for c in cat(arr))


def main():
    with open('input.txt', 'r') as f:
        rules = [parse_line(line.strip()) for line in f]

    print('Part A: {} - No. of pixels after 5 iterations'.format(enhance_art(rules, 5)))
    print('Part B: {} - No. of pixels after 18 iterations'.format(enhance_art(rules, 18)))


if __name__ == '__main__':
    main()

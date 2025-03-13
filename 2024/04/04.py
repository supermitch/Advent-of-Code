with open('04_input.txt') as f:
    lines = [x.strip() for x in f]


def check_deltas(lines, x, y, dx, dy):
    y_max = len(lines)
    x_max = len(lines[0])
    for i, letter in enumerate(['M', 'A', 'S'], start=1):
        x2, y2 = x + i * dx, y + i * dy
        if x2 < 0 or x2 >= x_max or y2 < 0 or y2 >= y_max:
            return False
        if lines[y2][x2] != letter:
            return False
    return True


count = 0
for y, row in enumerate(lines):
    for x, char in enumerate(row):
        if char == 'X':
            for i, (dx, dy) in enumerate(
                [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)],
                start=1,
            ):
                if check_deltas(lines, x, y, dx, dy):
                    count += 1

print(count)

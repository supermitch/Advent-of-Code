with open('03_input.txt') as f:
    lines = [x.strip() for x in f]

nums = []
for y, line in enumerate(lines):
    num = ''
    coords = []
    for x, c in enumerate(line):
        if c.isnumeric():
            num += c
            coords.append((x, y))
        else:
            if num:
                nums.append((int(num), coords))
            num = ''
            coords = []
    if num:  # On a number when line ends
        nums.append((int(num), coords))


valid = []
for num, coords in nums:
    added = False
    for x, y in coords:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                x2, y2 = x + dx, y + dy
                if (
                    (dx == 0 and dy == 0)
                    or x2 < 0 or x2 >= len(lines[0])
                    or y2 < 0 or y2 >= len(lines)
                ):
                    continue
                if lines[y2][x2] not in '0123456789.':
                    if not added:
                        valid.append(num)
                    added = True

print(f'Part a: {sum(valid)}')

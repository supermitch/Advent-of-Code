with open('03a_test.txt') as f:
    lines = [x.strip() for x in f]

nums = {}
for y, line in enumerate(lines):
    num = ''
    coords = []
    for x, c in enumerate(line):
        if c.isnumeric():
            num += c
            coords.append((x, y))
        else:
            if num:
                nums[int(num)] = coords
            num = ''
            coords = []

symbols = ('*', '#', '+', '$')
valid = set()
for num, coords in nums.items():
    for x, y in coords:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                x2, y2 = x + dx, y + dy
                if (
                    dx == 0 and dy == 0
                    or x2 < 0 or x2 >= len(lines[0])
                    or y2 < 0 or y2 >= len(lines)
                ):
                    continue
                if lines[y2][x2] in symbols:
                    valid.add(num)

print(f'Part a: {sum(valid)}')

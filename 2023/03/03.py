from collections import defaultdict

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
stars = defaultdict(list)
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
                char = lines[y2][x2]
                if char not in '0123456789.':
                    if char == '*' and not added:
                        stars[(x2, y2)].append(num)
                    if not added:
                        valid.append(num)
                    added = True

print(f'Part a: {sum(valid)}')

ratios = 0
for coords, nums in stars.items():
    if len(nums) == 2:
        ratios += (nums[0] * nums[1])

print(f'Part b: {ratios}')

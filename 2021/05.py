from collections import defaultdict

with open('05_input.txt') as f:
    data = []
    for line in f:
        start, end = line.replace(' ->', '').strip().split()
        x1, y1 = [int(x.strip()) for x in start.split(',')]
        x2, y2 = [int(x.strip()) for x in end.split(',')]
        data.append(((x1, y1), (x2, y2)))

perps = [(p1, p2) for p1, p2 in data if p1[0] == p2[0] or p1[1] == p2[1]]


def map_vents(data):
    coords = defaultdict(int)
    for (x1, y1), (x2, y2) in data[:]:
        dx = x2 - x1
        dy = y2 - y1
        if dx == 0:
            xstep = 0
        else:
            xstep = 1 if dx > 0 else -1
        if dy == 0:
            ystep = 0
        else:
            ystep = 1 if dy > 0 else -1
        for i in range(max(abs(dx), abs(dy)) + 1):
            coords[(x1 + i * xstep, y1 + i * ystep)] += 1
    return coords


def count_overlaps(coords):
    return sum(1 for v in coords.values() if v > 1)


print(f'Part A: {count_overlaps(map_vents(perps))} perpendicular overlaps')
print(f'Part B: {count_overlaps(map_vents(data))} total overlaps')

def parse_line(line):
    parts = line.split(',')  # Input was modified
    p = [int(x) for x in parts[:3]]
    v = [int(x) for x in parts[3:6]]
    a = [int(x) for x in parts[6:]]
    return p, v, a


def add(v1, v2):
    """ Add two 3D vectors. """
    return v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2]


def sum_abs(p):
    """ Get absolute sum of a 3D vector. """
    return abs(p[0]) + abs(p[1]) + abs(p[2])


def part_a(data):
    last_min = None
    n = 0
    while True:
        dist = {}
        for i, (p, v, a) in enumerate(data):
            v = add(v, a)
            p = add(p, v)
            data[i] = p, v, a
            dist[i] = sum_abs(p)
        closest = min(dist, key=dist.get)
        if closest == last_min:
            n += 1
            if n > 500:
                return closest
        last_min = closest


def part_b(data):
    last_count = None
    n = 0
    while True:
        to_delete = []
        seen = {}
        for i, (p, v, a) in enumerate(data):
            v = add(v, a)
            p = add(p, v)
            data[i] = p, v, a
            if p in seen:
                to_delete.append(i)
                to_delete.append(seen[p])
            seen[p] = i
        data = [d for i, d in enumerate(data) if i not in to_delete]
        if len(data) == last_count:
            n += 1
            if n > 100:
                return last_count
        last_count = len(data)


def main():
    with open('20.input', 'r') as f:
        data = [parse_line(line.strip()) for line in f]

    print('Part A: {} - Particle nearest to (0, 0)'.format(part_a(data[:])))
    print('Part B: {} - No. of surviving particles'.format(part_b(data[:])))


if __name__ == '__main__':
    main()

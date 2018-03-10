def parse(l):
    parts = l.split('-')
    return int(parts[0]), int(parts[1])


def main():
    with open('input.txt', 'r') as f:
        ranges = [parse(l.strip()) for l in f]

    ranges = sorted(ranges, key=lambda x: x[0])  # Sort by start of range

    # Of course the 1st range is (0, n) else solution would be 0...
    allowed = []
    upper = 0
    for i in range(len(ranges) - 1):
        curr = ranges[i]
        next = ranges[i + 1]
        upper = max(upper, curr[1])  # Always retain the max upper limit
        if upper < next[0] - 1:  # The next range is > 1 away; there's a gap
            allowed.append((upper + 1, next[0]))

    part_a = allowed[0]
    print('Part A: {} - Lowest allowed IP'.format(part_a[0]))

    # Our input data only has 1 IP missing every time! e.g.
    # (2, 5) (7, 10) -> Missing only 6: works, but
    # (2, 4) (7, 10) -> Missing only 5, 6: len(allowed) would be wrong
    part_b = len(allowed)
    print('Part B: {} - Total no. of allowed IPs'.format(part_b))


if __name__ == '__main__':
    main()

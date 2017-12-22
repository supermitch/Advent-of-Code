def part_a(line):
    ups = sum(c == '(' for c in line)
    downs = len(line) - ups
    return ups - downs


def part_b(line):
    floor = 0
    for idx, c in enumerate(line, start=1):
        floor += 1 if c == '(' else -1
        if floor == -1:
            return idx


def main():
    with open('01.input', 'r') as f:
        line = f.read().strip()

    print('Part A: {} - Final floor'.format(part_a(line)))
    print('Part B: {} - Index of first entry to basement'.format(part_b(line)))


if __name__ == '__main__':
    main()

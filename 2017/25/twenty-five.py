from collections import defaultdict


def part_a():
    state = 'A'  # Starting state
    pos = 0  # Starting pos
    values = defaultdict(int)
    values[0] = 0  # Starting value

    for i in range(12317297):
        if state == 'A':
            if values[pos] == 0:
                values[pos] = 1
                pos += 1
                state = 'B'
            else:
                values[pos] = 0
                pos += -1
                state = 'D'
        elif state == 'B':
            if values[pos] == 0:
                values[pos] = 1
                pos += 1
                state = 'C'
            else:
                values[pos] = 0
                pos += 1
                state = 'F'
        elif state == 'C':
            if values[pos] == 0:
                values[pos] = 1
                pos += -1
                state = 'C'
            else:
                values[pos] = 1
                pos += -1
                state = 'A'
        elif state == 'D':
            if values[pos] == 0:
                values[pos] = 0
                pos += -1
                state = 'E'
            else:
                values[pos] = 1
                pos += 1
                state = 'A'
        elif state == 'E':
            if values[pos] == 0:
                values[pos] = 1
                pos += -1
                state = 'A'
            else:
                values[pos] = 0
                pos += 1
                state = 'B'
        elif state == 'F':
            if values[pos] == 0:
                values[pos] = 0
                pos += 1
                state = 'C'
            else:
                values[pos] = 0
                pos += 1
                state = 'E'
        else:
            print(f'Bad state {state}')

    return sum(v for v in values.values())


def part_b():
    return None


def main():
    checksum = part_a()
    print('Part A: {} - Diagnostic checksum'.format(checksum))

    sum = part_b()


if __name__ == '__main__':
    main()

def part_a(jumps):
    count = 0
    i = 0
    while True:
        try:
            move = jumps[i]
            jumps[i] += 1
            i += move
            count += 1
        except IndexError:
            return count


def part_b(jumps):
    count = 0
    i = 0
    while True:
        try:
            move = jumps[i]
            increment = -1 if move >= 3 else 1
            jumps[i] += increment
            i += move
            count += 1
        except IndexError:
            return count


def main():
    with open('five.txt', 'r') as f:
        jumps = [int(x.strip()) for x in f.readlines()]

    print('Part A: {}'.format(part_a(jumps[:])))
    print('Part B: {}'.format(part_b(jumps[:])))


if __name__ == '__main__':
    main()

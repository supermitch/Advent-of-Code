def area(rect):
    x, y, z = rect
    return 2 * x * z + 2 * x * y + 2 * z * y


def slack(rect):
    x, y, z = rect
    return min([x * z, x * y, z * y])


def part_a(rects):
    total = 0
    for rect in rects:
        total += area(rect) + slack(rect)
    return total


def wrap(rect):
    x, y, z = rect
    perimeters = [2 * x + 2 * z, 2 * x + 2 * y, 2 * z + 2 * y]
    return min(perimeters)


def bow(rect):
    x, y, z = rect
    return x * y * z


def part_b(rects):
    total = 0
    for rect in rects:
        total += wrap(rect) + bow(rect)
    return total


def main():
    with open('input.txt', 'r') as f:
        rects = [[int(d) for d in line.strip().split('x')] for line in f]

    print('Part A: {} - Total square feet of wrapping paper'.format(part_a(rects)))
    print('Part B: {} - Total length of ribbon'.format(part_b(rects)))


if __name__ == '__main__':
    main()

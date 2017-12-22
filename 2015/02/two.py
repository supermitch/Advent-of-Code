def area(x, y, z):
    return (2 * x * z) + (2 * x * y) + (2 * z * y)


def slack(x, y, z):
    return min([x * z, x * y, z * y])


def part_a(rects):
    return sum(area(*r) + slack(*r) for r in rects)


def wrap(x, y, z):
    return min([2 * x + 2 * z, 2 * x + 2 * y, 2 * z + 2 * y])


def bow(x, y, z):
    return x * y * z


def part_b(rects):
    return sum(wrap(*r) + bow(*r) for r in rects)


def main():
    with open('input.txt', 'r') as f:
        rects = [[int(d) for d in line.strip().split('x')] for line in f]

    print('Part A: {} - Total square feet of wrapping paper'.format(part_a(rects)))
    print('Part B: {} - Total length of ribbon'.format(part_b(rects)))


if __name__ == '__main__':
    main()

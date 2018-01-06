def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b


def check_cols(sides):
    count = 0
    i = 0
    while i < len(sides):
        for col in range(3):
            edges = []
            for dr in range(3):
                edges.append(sides[i + dr][col])
            if is_triangle(*edges):
                count += 1
        i += 3
    return count


def main():
    with open('input.txt', 'r') as f:
        sides = [[int(s) for s in line.strip().split()] for line in f]

    part_a = sum(is_triangle(a, b, c) for a, b, c in sides)
    print('Part A: {} - No. of valid triangles, by row'.format(part_a))

    part_b = check_cols(sides)
    print('Part B: {} - No. of valid triangles by column'.format(part_b))


if __name__ == '__main__':
    main()

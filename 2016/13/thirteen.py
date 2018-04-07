def get_tile(x, y, input):
    z = (x * x) + (3 * x) + (2 * x * y) + (y) + (y * y)
    total = z + input
    binary = format(total, 'b')
    bit_sum = sum(b == '1' for b in binary)
    if not bit_sum % 2:
        return '.'
    else:
        return '#'


def main():
    input = 1352
    for y in range(100):
        row = ''
        for x in range(100):
            row += get_tile(x, y, input)
        print(row)


if __name__ == '__main__':
    main()

def count_safe_tiles(map):
    return sum(tile == '.' for row in map for tile in row)


def next_tile(row, i):
    """ New tiles are traps if certain conditions are met. """
    left = '.' if i - 1 < 0 else row[i - 1]  # Safe if out of bounds
    right = '.' if i + 1 >= len(row) else row[i + 1]  # Safe if out of bounds
    three = left + row[i] + right  # Concat the tiles for easy comparison
    return '^' if three in ['^^.', '.^^', '^..', '..^'] else '.'


def expand_map(map, n):
    """ Expand a map to a total of n rows high. """
    while len(map) < n:
        prev = map[-1]  # Next row is based on the previous one
        new = ''.join(next_tile(prev, i) for i in range(len(prev)))
        map.append(new)
    return map


def main():
    with open('input.txt', 'r') as f:
        map = [line.strip() for line in f]

    part_a = count_safe_tiles(expand_map(map, 40))
    print('Part A: {} - Number of safe tiles in a 40 row map'.format(part_a))

    part_b = count_safe_tiles(expand_map(map, 4e5))
    print('Part B: {} - Number of safe tiles in 40k row map'.format(part_b))


if __name__ == '__main__':
    main()

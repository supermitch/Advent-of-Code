def find_square(n):
    # Squares are sized 1, 3, 5, 7, 9
    i = 1
    while True:
        total = i * i
        if n <= total:
            return i
        i += 2


def manhattan(n):
    if n == 1:
        return 0
    size = find_square(n)  # Which size square we on, e.g. 1, 3, 5, 7
    ring = (size + 1) / 2  # which ring on we on, e.g. 1, 2, 3, 4

    x_start = max(ring - 1, 0)  # How far right
    y_start = -1 * max(ring - 2, 0)  # How far down

    inner_total = (size - 2) ** 2
    total = size ** 2
    start = inner_total + 1

    steps = n - start  # Along this ring, from start

    right = size - 2  # Length of right size to top right corner
    top = left = size - 1  # Length of other sides

    if steps <= right:  # Right
        x = x_start
        y = y_start + steps
    elif steps <= right + top:  # Top
        dist = steps - right
        x = x_start - dist
        y = y_start + right
    elif steps <= right + top + left:  # Left
        dist = steps - right - top
        x = x_start - top
        y = y_start + right - dist
    else:  # Bottom
        x = x_start - (total - n)
        y = y_start - 1

    return abs(x) + abs(y)


if __name__ == '__main__':

    assert manhattan(1) == 0
    assert manhattan(3) == 2
    assert manhattan(4) == 1
    assert manhattan(12) == 3
    assert manhattan(20) == 3
    assert manhattan(23) == 2
    assert manhattan(17) == 4
    assert manhattan(1024) == 31

    print('Part A: {}'.format(manhattan(347991)))

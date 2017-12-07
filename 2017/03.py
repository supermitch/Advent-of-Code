# Part A:
def find_square(n):
    # Squares are sized 1, 3, 5, 7, 9
    i = 1
    while True:
        total = i * i
        if n <= total:
            return i
        i += 2


def manhattan(n):
    size = find_square(n)  # Which size square we on, e.g. 1, 3, 5, 7
    ring = (size + 1) / 2  # which ring on we on, e.g. 1, 2, 3, 4

    x_start = max(ring - 1, 0)  # How far right
    y_start = -1 * max(ring - 2, 0)  # How far down

    start = max(size - 2, 0) ** 2 + 1  # Start val for this ring
    end = size ** 2  # End val

    steps = n - start  # Along this ring, from start

    right = max(size - 2, 1)  # Length of right size to top right corner
    top = left = max(size - 1, 1)  # Length of other sides

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
        x = x_start - (end - n)
        y = y_start - 1

    return abs(x) + abs(y)


# Part B:
def sum_neighbours(arr, coord):
    """ Sum 9 nearest neighbours. """
    x, y = coord
    total = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if (dx, dy) != (0, 0):
                try:
                    total += arr[(x + dx, y + dy)]
                except KeyError:
                    continue
    return total


def spiral_offsets():
    """ Generate spiral step (dx, dy) values. """
    size = 3
    while True:
        yield 1, 0   # right
        for _ in range(size - 2):
            yield 0, 1  # up
        for _ in range(size - 1):
            yield -1, 0  # left
        for _ in range(size - 1):
            yield 0, -1  # down
        for _ in range(size - 1):
            yield 1, 0  # right
        size += 2


def spiral_series(n):
    x, y = (0, 0)
    arr = {(x, y): 1}  # A dict is like an array but easy?
    offsets = spiral_offsets()
    while True:
        dx, dy = next(offsets)
        x, y = x + dx, y + dy
        new_value = sum_neighbours(arr, (x, y))
        if new_value > n:
            return new_value
        arr[(x, y)] = new_value


if __name__ == '__main__':
    assert manhattan(1) == 0
    assert manhattan(4) == 1
    assert manhattan(12) == 3
    assert manhattan(23) == 2
    assert manhattan(17) == 4
    assert manhattan(1024) == 31
    print('Part A: {}'.format(manhattan(347991)))

    assert spiral_series(6) == 10
    assert spiral_series(800) == 806
    print('Part B: {}'.format(spiral_series(347991)))

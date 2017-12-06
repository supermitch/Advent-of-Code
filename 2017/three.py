def find_square(n):
    # square are sized 1, 3, 5, 7, 9
    i = 1
    while True:
        total = i * i
        if n <= total:
            return i
        i += 2


def manhattan(n):
    dim = find_square(n)  # Which size square we on?
    if dim == 1:
        return 0
    else:
        layer = (dim + 1) / 2  # which layer on we on (1, 2, 3, 4, etc.)
        total = dim ** 2 - (dim - 2) ** 2
        print('Total {}'.format(total))
        edge = dim ** 2 / 4
        print(edge)
        side = n / edge
        print(side)
        return side


if __name__ == '__main__':
    assert manhattan(1) == 0
    assert manhattan(3) == 2
    assert manhattan(4) == 1
    assert manhattan(13) == 3
    assert manhattan(23) == 2
    assert manhattan(1024) == 31
    print(manhattan(347991))

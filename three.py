def find_square(n):
    # square are sized 1, 3, 5, 7, 9
    i = 1
    while True:
        total = i * i
        if n <= total:
            return i
        i += 2


def manhattan(n):
    i = find_square(n)  # Which size square we on?
    layer = (i + 1) / 2
    if layer == 1:
        return 0
    else:

    print(i)


if __name__ == '__main__':
    assert manhattan(1) == 0
    assert manhattan(12) == 3
    assert manhattan(23) == 2
    assert manhattan(1024) == 31
    print(manhattan(347991))

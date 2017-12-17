import time


def part_a():
    arr = [0]
    pos = 0
    for i in range(1, 2017 + 1):
        idx = (pos + 301) % i
        arr.insert(idx + 1, i)
        pos = idx + 1
    return arr[pos + 1]


def part_b():
    new_val = None
    pos = 0
    for i in range(50000000):
        idx = (pos + 301) % (i + 1)  # len(arr) == i + 1
        if idx == 0:
            new_val = i + 1  # insert new val
        pos = idx + 1
    return new_val


def main():
    tic = time.time()
    print('Part A: {} - '.format(part_a()))
    print('Elapsed: {}'.format(time.time() - tic))

    print('\n')

    tic = time.time()
    print('Part B: {} - '.format(part_b()))
    print('Elapsed: {}'.format(time.time() - tic))


if __name__ == '__main__':
    main()

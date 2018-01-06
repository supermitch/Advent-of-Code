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
    for i in range(1, 50000000 + 1):
        idx = (pos + 301) % i  # "len(arr)" == i
        if idx == 0:
            new_val = i  # "insert" new val
        pos = idx + 1
    return new_val


def main():
    tic = time.time()
    print('Part A: {} - Value after 2017 in circular buffer'.format(part_a()))
    print('Elapsed: {:0.3f} s'.format(time.time() - tic))

    print('\n')

    tic = time.time()
    print('Part B: {} - Value after 0, after 5e6 insertions'.format(part_b()))
    print('Elapsed: {:0.3f} s'.format(time.time() - tic))


if __name__ == '__main__':
    main()

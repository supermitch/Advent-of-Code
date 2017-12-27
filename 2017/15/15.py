import time


def part_a():
    count = 0
    val_a = 883
    val_b = 879
    for i in range(int(4e7)):
        a_val = val_a * 16807 % 2147483647
        b_val = val_b * 48271 % 2147483647

        count += format(a_val, '016b')[-16:] == format(b_val, '016b')[-16:]

        val_a, val_b = a_val, b_val
    return count


def part_b():
    count = 0
    val_a = 883
    val_b = 879
    for i in range(int(5e6)):
        while True:
            a_val = val_a * 16807 % 2147483647
            if a_val % 4 == 0:
                break
            val_a = a_val
        while True:
            b_val = val_b * 48271 % 2147483647
            if b_val % 8 == 0:
                break
            val_b = b_val

        count += format(a_val, '016b')[-16:] == format(b_val, '016b')[-16:]
        val_a = a_val
        val_b = b_val
    return count


def main():
    tic = time.time()
    count_a = part_a()
    print(f'Part A: {count_a} - Matching count')
    print('Elapsed: {:0.2f} s'.format(time.time() - tic))

    print('\n')

    tic = time.time()
    count_b = part_b()
    print(f'Part B: {count_b} - Matching count for divisible')
    print('Elapsed: {:0.2f} s'.format(time.time() - tic))


if __name__ == '__main__':
    main()

from itertools import permutations


def main():
    with open('input.txt') as f:
        data = [int(x.strip()) for x in f]

    LEN = 25
    for i, num in enumerate(data[LEN:], start=LEN):
        found = False
        for a, b in permutations(data[i - LEN:i], 2):
            if a + b == num:
                found = True
                break
        if not found:
            break

    lo, hi = 0, 1
    while True:
        vals = data[lo: hi]
        tot = sum(vals)
        if tot == num:
            break
        elif tot > num:
            lo += 1
            hi = lo + 1
        else:
            hi += 1

    print(f'Part A: {num}')
    print(f'Part B: {min(vals) + max(vals)}')


if __name__ == '__main__':
    main()

#!/usr/bin/env python


def not_prime(n):
    for i in range(2, n):  # Ignoring 1 * n
        if n % i == 0:
            return True
    return False


def run(debug=True):
    if debug:
        b = 65
        c = 65
        return (b - 2) * (c - 2)
    else:
        return sum(not_prime(b) for b in range(106500, 123500 + 1, 17))


def main():
    print('Part A: {} - `Mul` count w/ debug on'.format(run(True)))
    print('Part B: {} - Register h w/ debug off'.format(run(False)))


if __name__ == '__main__':
    main()

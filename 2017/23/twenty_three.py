#!/usr/bin/env python
from collections import defaultdict


def parse_line(line):
    d = line.strip().split()
    reg = d[1] if d[1].isalpha() else int(d[1])  # Sometimes register is an int!
    try:
        v = d[2] if d[2].isalpha() else int(d[2])  # Sometimes value is a register!
    except IndexError:
        v = None
    return d[0], reg, v  # Nominally: Type, register, value | None


def get_val(regs, val):
    return val if isinstance(val, int) else regs[val]


def run(a=0):
    mul_count = 0
    a = 0
    b = 65
    c = b
    d, e, f, g, h = 0, 0, 0, 0, 0
    if a != 0: # jnz a 2
        b *= 100
        mul_count += 1
        b -= -100000
        c = b
        c -= -17000

    while True:
        f = 1
        d = 2
        while True:
            e = 2
            while True:
                g = d
                g *= e
                mul_count += 1
                g -= b
                if g == 0:
                    f = 0
                e -= -1
                g = e
                g -= b
                if g == 0:
                    break
            d -= -1
            g = d
            g -= b
            if g == 0:
                break
        if f == 0:
            h -= -1
        g = b
        g -= c
        if g == 0:
            break
        b -= -17
    return mul_count


def run_code(data, debug=False):
    registers = defaultdict(int)
    if not debug:
        registers['a'] = 1
    skip = None
    i = 0
    mul_count = 0
    while True:
        if not debug:
            print(registers)
        if i >= len(data) or i < 0:
            break
        d, r, v = data[i]

        if d == 'set':
            registers[r] = get_val(registers, v)
        elif d == 'sub':
            registers[r] -= get_val(registers, v)
        elif d == 'mul':
            registers[r] *= get_val(registers, v)
            mul_count += 1
        elif d == 'jnz':
            if get_val(registers, r) != 0:  # r could be an int!
                skip = get_val(registers, v)

        i += 1 if skip is None else skip
        skip = None
    return mul_count


def main():
    with open('input.txt', 'r') as f:
        data = [parse_line(line) for line in f]

    print('Part A: {} - Multiplications, debug on'.format(run_code(data, True)))
    print(run(a=0))
    # print(run(a=1))
    # print('Part B: {} - `mul` count'.format(run_code(data)))


if __name__ == '__main__':
    main()

#!/usr/bin/env python
from collections import defaultdict


def get(regs, val):
    try:
        return int(val)
    except ValueError:
        return regs[val]


def toggle(step):
    if len(step) == 2:
        if 'inc' in step:
            return ('dec', step[1])
        else:
            return ('inc', step[1])
    elif len(step) == 3:
        if 'jnz' in step:
            return ('cpy', *step[1:])
        else:
            return ('jnz', *step[1:])


def run(steps, init):
    regs = defaultdict(int)
    regs['a'] = init
    i = 0
    while True:
        jump = 1
        step = steps[i]
        if 'cpy' in step:
            _, a, b = step
            try:
                regs[b] = get(regs, a)
            except KeyError:  # Invalid step, e.g. cpy 1 3
                pass
        elif 'inc' in step:
            _, a = step
            try:
                regs[a] += 1
            except KeyError:  # Invalid step, e.g. inc 1 2
                pass
        elif 'dec' in step:
            _, a = step
            try:
                regs[a] -= 1
            except KeyError:
                pass
        elif 'jnz' in step:
            _, a, b = step
            if get(regs, a) != 0:
                jump = get(regs, b)
        elif 'tgl' in step:
            _, a = step
            a = get(regs, a)
            if i + a >= len(steps):
                pass
            else:
                steps[i + a] = toggle(steps[i + a])

        i += jump
        if i >= len(steps):
            return regs


def part_b():
    import pdb
    pdb.set_trace()
    a = 12
    b = a
    b -= 1  # b == 11
    d = a  # d == 12
    a = 0
    while True:
        c = b  # c == 11
        while True:
            a += 1  # 12 + 1
            c -= 1
            if c == 0:
                break
        d -= 1
        if d == 0:
            break
    b -= 1
    c = b
    d = c
    while True:
        d -= 1
        c += 1
        if d == 0:
            break
    print('tgl c', c)
    c = -16
    print('jnz 1 c', c)
    c = 84
    print('jnz 75 d', d)
    while True:
        a += 1
        d += 1
        if d == 0:
            break
    c += 1
    print('jnz c -5', c)


def main():
    with open('input.txt', 'r') as f:
        steps = [l.strip().split() for l in f]

    regs = run(steps[:], 7)
    print("Part A: {} - Value of register 'a'".format(regs['a']))

    part_b()
    # print('Part B: {} - Value of register \'a\''.format(regs['a']))


if __name__ == '__main__':
    main()

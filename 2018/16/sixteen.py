#!/usr/bin/env python
import re


def read_input():
    samples = []
    with open('input_a.txt') as f:
        while True:
            sample = {}
            sample['b'] = [int(x) for x in re.sub('[^0-9]', ' ', f.readline()).split()]
            sample['op'] = [int(x) for x in f.readline().split()]
            sample['a'] = [int(x) for x in re.sub('[^0-9]', ' ', f.readline()).split()]
            if not f.readline():
                break
            samples.append(sample)
    return samples


def addr(a, b, c, regs):
    name = 'addr'
    regs[c] = regs[a] + regs[b]
    return regs, name

def addi(a, b, c, regs):
    name = 'addi'
    regs[c] = regs[a] + b
    return regs, name

def mulr(a, b, c, regs):
    name = 'mulr'
    regs[c] = regs[a] * regs[b]
    return regs, name

def muli(a, b, c, regs):
    name = 'muli'
    regs[c] = regs[a] * b
    return regs, name

def banr(a, b, c, regs):
    name = 'banr'
    regs[c] = regs[a] & regs[b]
    return regs, name

def bani(a, b, c, regs):
    name = 'bani'
    regs[c] = regs[a] & b
    return regs, name

def borr(a, b, c, regs):
    name = 'borr'
    regs[c] = regs[a] | regs[b]
    return regs, name

def bori(a, b, c, regs):
    name = 'bori'
    regs[c] = regs[a] | b
    return regs, name

def setr(a, b, c, regs):
    name = 'setr'
    regs[c] = regs[a]
    return regs, name

def seti(a, b, c, regs):
    name = 'seti'
    regs[c] = a
    return regs, name

def gtir(a, b, c, regs):
    name = 'gtir'
    regs[c] = 1 if a > regs[b] else 0
    return regs, name

def gtri(a, b, c, regs):
    name = 'gtri'
    regs[c] = 1 if regs[a] > b else 0
    return regs, name

def gtrr(a, b, c, regs):
    name = 'gtrr'
    regs[c] = 1 if regs[a] > regs[b] else 0
    return regs, name

def eqir(a, b, c, regs):
    name = 'eqir'
    regs[c] = 1 if a == regs[b] else 0
    return regs, name

def eqri(a, b, c, regs):
    name = 'eqri'
    regs[c] = 1 if regs[a] == b else 0
    return regs, name

def eqrr(a, b, c, regs):
    name = 'eqrr'
    regs[c] = 1 if regs[a] == regs[b] else 0
    return regs, name


def count_ops(samples, funcs, opcodes):
    total = 0
    for sample in samples:
        matches = []
        for func in funcs:
            code, a, b, c = sample['op']
            result, name = func(a, b, c, sample['b'][:])
            if result == sample['a']:
                matches.append([code, name])
        if [code, opcodes[code]] not in matches:
            print('Horrible bug', code, opcodes[code])
            return
        if len(matches) >= 3:
            total += 1
    print('Total:', total)  # Not 554
    return total

def validate(samples, opers):
    for sample in samples:
        regs = sample['b']  # before
        code, a, b, c = sample['op']
        result, name = globals()[opers[code]](a, b, c, regs)
        if result != sample['a']:  # After should match
            print('Horrible bug', sample)
            return False
    return True

def execute(operations, opcodes):
    regs = [0, 0, 0, 0]
    for row in operations:
        code, a, b, c = row
        regs, _ = globals()[opcodes[code]](a, b, c, regs)
    print('Register 0:', regs[0])


def main():
    samples = read_input()
    # samples = [{'b': [3, 2, 1, 1], 'op': [9, 2, 1, 2], 'a':  [3, 2, 2, 1]}]
    funcs = [
        addr, addi, mulr, muli, banr, bani, borr, bori,
        setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr
    ]
    opers = {
        0: 'addi',
        1: 'eqrr',
        2: 'borr',
        3: 'gtri',
        4: 'addr',
        5: 'seti',
        6: 'muli',
        7: 'bani',
        8: 'banr',
        9: 'gtrr',
        10: 'setr',
        11: 'gtri',
        12: 'bori',
        13: 'eqri',
        14: 'eqir',
        15: 'mulr',
    }
    count_ops(samples, funcs, opers)

    assert validate(samples, opers)

    operations = []
    with open('input_b.txt') as f:
        for l in f:
            operations.append([int(x) for x in l.split()])

    execute(operations, opers)


if __name__ == '__main__':
    main()

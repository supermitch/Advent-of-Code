#!/usr/bin/env python
import re


def read_input_a():
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


def read_input_b():
    operations = []
    with open('input_b.txt') as f:
        for l in f:
            operations.append([int(x) for x in l.split()])
    return operations


def addr(a, b, c, regs):
    regs[c] = regs[a] + regs[b]
    return regs

def addi(a, b, c, regs):
    regs[c] = regs[a] + b
    return regs

def mulr(a, b, c, regs):
    regs[c] = regs[a] * regs[b]
    return regs

def muli(a, b, c, regs):
    regs[c] = regs[a] * b
    return regs

def banr(a, b, c, regs):
    regs[c] = regs[a] & regs[b]
    return regs

def bani(a, b, c, regs):
    regs[c] = regs[a] & b
    return regs

def borr(a, b, c, regs):
    regs[c] = regs[a] | regs[b]
    return regs

def bori(a, b, c, regs):
    regs[c] = regs[a] | b
    return regs

def setr(a, _, c, regs):
    regs[c] = regs[a]
    return regs

def seti(a, _, c, regs):
    regs[c] = a
    return regs

def gtir(a, b, c, regs):
    regs[c] = 1 if a > regs[b] else 0
    return regs

def gtri(a, b, c, regs):
    regs[c] = 1 if regs[a] > b else 0
    return regs

def gtrr(a, b, c, regs):
    regs[c] = 1 if regs[a] > regs[b] else 0
    return regs

def eqir(a, b, c, regs):
    regs[c] = 1 if a == regs[b] else 0
    return regs

def eqri(a, b, c, regs):
    regs[c] = 1 if regs[a] == b else 0
    return regs

def eqrr(a, b, c, regs):
    regs[c] = 1 if regs[a] == regs[b] else 0
    return regs


def count_ops(samples, opcodes):
    total = 0
    for sample in samples:
        matches = []
        for opcode in opcodes.values():
            code, a, b, c = sample['op']
            if opcode(a, b, c, sample['b'][:]) == sample['a']:
                matches.append([code, opcode.__name__])
        if len(matches) >= 3:
            total += 1
    return total


def execute(operations, opcodes):
    regs = [0, 0, 0, 0]
    for row in operations:
        code, a, b, c = row
        regs = opcodes[code](a, b, c, regs)
    return regs[0]


def main():
    opcodes = {
        0: addi,
        1: eqrr,
        2: borr,
        3: gtri,
        4: addr,
        5: seti,
        6: muli,
        7: bani,
        8: banr,
        9: gtrr,
        10: setr,
        11: gtir,
        12: bori,
        13: eqri,
        14: eqir,
        15: mulr,
    }
    samples = read_input_a()
    count = count_ops(samples, opcodes)
    print('Part A: {} - No. of samples w/ >= 3 options'.format(count))

    operations = read_input_b()
    reg_a = execute(operations, opcodes)
    print('Part B: {} - The value in register 0'.format(reg_a))


if __name__ == '__main__':
    main()

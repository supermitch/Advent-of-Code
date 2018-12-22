#!/usr/bin/env python

def read_input(fname='input.txt'):
    with open(fname) as f:
        ip = int(f.readline().strip().split()[1])
        ops = []
        for l in f:
            parts = l.strip().split()
            op = parts[0]
            a, b, c = [int(x) for x in parts[1:]]
            ops.append((op, a, b, c))
    return ip, ops

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

def main():
    ip_reg, ops = read_input('input.txt')
    regs = [0] * 6
    ip = 0
    regs[0] = 1
    while True:
        # print('ip={}'.format(ip))
        # print(regs)
        regs[ip_reg] = ip
        try:
            op, a, b, c = ops[ip]
            # print(op, a, b, c)
        except IndexError:
            break
        func = globals()[op]
        regs = func(a, b, c, regs)
        # print(regs)
        # print('\n')
        ip = regs[ip_reg] + 1
    print(regs)





if __name__ == '__main__':
    main()

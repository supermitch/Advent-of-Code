from collections import defaultdict


def get(regs, val):
    try:
        return int(val)
    except ValueError:
        return regs[val]


def run(steps):
    regs = defaultdict(int)
    i = 0
    while True:
        jump = 1
        step = steps[i]
        if 'cpy' in step:
            _, a, b = step
            regs[b] = get(regs, a)
        elif 'inc' in step:
            _, a = step
            regs[a] += 1
        elif 'dec' in step:
            _, a = step
            regs[a] -= 1
        elif 'jnz' in step:
            _, a, b = step
            if get(regs, a) != 0:
                jump = get(regs, b)
        i += jump
        if i >= len(steps):
            return regs


def main():
    # test = ['cpy 41 a', 'inc a', 'inc a', 'dec a', 'jnz a 2', 'dec a']
    # steps = [l.strip().split() for l in test]
    # regs = run(steps)
    # assert regs['a'] == 42

    with open('input.txt', 'r') as f:
        steps = [l.strip().split() for l in f]

    regs = run(steps)
    print('Part A: {} - Final value of register a'.format(regs['a']))

    steps.insert(0, ['cpy', 1, 'c'])
    regs = run(steps)
    print('Part B: {} - Register a after initializing c'.format(regs['a']))


if __name__ == '__main__':
    main()

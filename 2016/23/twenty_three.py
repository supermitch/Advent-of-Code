from collections import defaultdict


def parse(line):
    parts = line.split()
    return parts


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
        print('{}. {}: {}'.format(i, step, regs))
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
            print('Toggle!')
            _, a = step
            a = get(regs, a)
            if i + a >= len(steps):
                pass
            else:
                steps[i + a] = toggle(steps[i + a])

        i += jump
        if i >= len(steps):
            return regs


def main():
    with open('input.txt', 'r') as f:
        steps = [parse(l.strip()) for l in f]

    # regs = run(steps[:], 7)
    # print('Part A: {} - Value of register \'a\''.format(regs['a']))

    regs = run(steps[:], 12)
    print('Part B: {} - Value of register \'a\''.format(regs['a']))


if __name__ == '__main__':
    main()

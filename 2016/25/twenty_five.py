from collections import defaultdict


def parse(line):
    parts = line.split()
    return parts


def get(regs, val):
    try:
        return int(val)
    except ValueError:
        return regs[val]


def run(steps, init):
    regs = defaultdict(int)
    regs['a'] = init
    i = 0
    result = []
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
        elif 'out' in step:
            _, a = step
            result.append(regs[a])

        i += jump
        if i >= len(steps):  # Means we aren't an infinite sequence
            return []
        if len(result) > 100:  # 100 should be enough to prove a point
            return result
        elif len(result) >= 2:  # If any of these are True, it isn't a 0-1 infinite sequence
            if len(result) % 2 == 0 and sum(result) != len(result) / 2:  # Half of items should be 1's
                return []
            if any(x == 1 for i, x in enumerate(result) if i % 2 == 0):  # All evens should be 0's
                return []
            if any(x == 0 for i, x in enumerate(result) if i % 2 != 0):  # All odds shoudl be 1's
                return []


def main():
    with open('input.txt', 'r') as f:
        steps = [parse(l.strip()) for l in f]

    for init in range(200):
        if run(steps[:], init):
            break
    print('Part A: {} - Value of register \'a\' to generate clock signal'.format(init))


if __name__ == '__main__':
    main()

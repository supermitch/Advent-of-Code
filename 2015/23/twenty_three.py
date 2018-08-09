def read_input():
    with open('input.txt', 'r') as f:
        return [line.strip().replace(',', '').split() for line in f]


def parse_instructions(instructions, regs):
    i = 0
    while i >= 0 and i < len(instructions):
        com = instructions[i]
        act = com[0]  # Action
        reg = com[1]  # Register (usually)

        jump = 1
        if act == 'hlf':
            regs[reg] /= 2
        elif act == 'tpl':
            regs[reg] *= 3
        elif act == 'inc':
            regs[reg] += 1
        elif act == 'jmp':
            jump = int(reg)  # reg is an offset in this case
        elif act == 'jie' and regs[reg] % 2 == 0:
            jump = int(com[2])
        elif act == 'jio' and regs[reg] == 1:
            jump = int(com[2])
        i += jump

    return regs


def main():
    test = [('inc', 'a'), ('jio', 'a', '+2'), ('tpl', 'a'), ('inc', 'a')]
    assert parse_instructions(test, {'a': 0, 'b': 0})['a'] == 2

    instructions = read_input()

    regs = parse_instructions(instructions, {'a': 0, 'b': 0})
    print('Part A: {} - Contents of register b'.format(regs['b']))

    regs = parse_instructions(instructions, {'a': 1, 'b': 0})
    print('Part B: {} - Contents of register b w/ a = 1'.format(regs['b']))


if __name__ == '__main__':
    main()

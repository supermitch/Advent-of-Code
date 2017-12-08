import operator

class Op():
    def __init__(self, reg_a, op, val, reg_b, comp, comp_val):
        self.reg_a = reg_a
        self.op = operator.add if op == 'inc' else operator.sub
        self.val = val
        self.reg_b = reg_b
        self.comp = {
            '>': operator.gt,
            '>=': operator.ge,
            '<': operator.lt,
            '<=': operator.le,
            '==': operator.eq,
            '!=': operator.ne,
        }[comp]
        self.comp_val = comp_val


def parse_line(line):
    p = line.strip().split()
    return Op(p[0], p[1], int(p[2]), p[4], p[5], int(p[6]))


def init_registers(ops):
    registers = {}
    for op in ops:
        registers[op.reg_a] = 0
        registers[op.reg_b] = 0
    return registers


def main():
    ops = []
    with open('08.input', 'r') as f:
        for line in f:
            ops.append(parse_line(line))

    registers = init_registers(ops)

    true_max = 0
    for op in ops:
        if op.comp(registers[op.reg_b], op.comp_val):
            registers[op.reg_a] = op.op(registers[op.reg_a], op.val)

            true_max = max(max(registers.values()), true_max)
    final_max = max(registers.values())

    print('Part A: {} - Max final register value'.format(final_max))
    print('Part B: {} - Peak value throughout calcs'.format(true_max))


if __name__ == '__main__':
    main()

import operator

class Operation():
    def __init__(self, reg_a, op, op_val, _, reg_b, comp, comp_val):
        self.reg_a = reg_a
        self.op = operator.add if op == 'inc' else operator.sub
        self.op_val = int(op_val)
        self.reg_b = reg_b
        self.comp = {
            '>': operator.gt,
            '>=': operator.ge,
            '<': operator.lt,
            '<=': operator.le,
            '==': operator.eq,
            '!=': operator.ne,
        }[comp]
        self.comp_val = int(comp_val)


def init_registers(registers, a, b):
    if a not in registers:
        registers[a] = 0
    if b not in registers:
        registers[b] = 0


def main():
    registers = {}
    true_max = 0
    with open('input.txt', 'r') as f:
        for line in f:
            op = Operation(*line.strip().split())

            init_registers(registers, op.reg_a, op.reg_b)

            if op.comp(registers[op.reg_b], op.comp_val):
                registers[op.reg_a] = op.op(registers[op.reg_a], op.op_val)
                true_max = max(registers[op.reg_a], true_max)

    final_max = max(registers.values())

    print('Part A: {} - Max final register value'.format(final_max))
    print('Part B: {} - Peak value throughout calcs'.format(true_max))


if __name__ == '__main__':
    main()

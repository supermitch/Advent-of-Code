#!/usr/bin/env python
import itertools


def parse_opcode(param):
    param = str(param).zfill(5)  # 0 padded
    op = int(param[-2:])
    modes = [int(x) for x in list(param[:-2])]
    return op, modes


class Computer:
    def __init__(self, data, phase):
        self.data = data.copy()
        self.phase = phase
        self.inval = None
        self.output = self.compute()
        self.started = False

    def compute(self):
        i = 0
        while True:
            op, (_, mode_b, mode_a) = parse_opcode(self.data[i])

            if op == 1:  # Add
                a, b, c = self.data[i + 1: i + 4]
                val_a = self.data[a] if not mode_a else a
                val_b = self.data[b] if not mode_b else b
                self.data[c] = val_a + val_b
                i += 4
            elif op == 2:  # Multiply
                a, b, c = self.data[i + 1: i + 4]
                val_a = self.data[a] if not mode_a else a
                val_b = self.data[b] if not mode_b else b
                self.data[c] = val_a * val_b
                i += 4
            elif op == 3:  # Input
                a = self.data[i + 1]
                in_val = self.inval if self.started else self.phase
                self.data[a] = in_val
                self.started = True
                i += 2
            elif op == 4:  # Output
                a = self.data[i + 1]
                val_a = self.data[a] if not mode_a else a
                output = val_a
                yield output
                i += 2
            elif op == 5:  # Jump if False
                a, b = self.data[i + 1: i + 3]
                val_a = self.data[a] if not mode_a else a
                val_b = self.data[b] if not mode_b else b
                i = val_b if val_a != 0 else i + 3
            elif op == 6:  # Jump if True
                a, b = self.data[i + 1: i + 3]
                val_a = self.data[a] if not mode_a else a
                val_b = self.data[b] if not mode_b else b
                i = val_b if val_a == 0 else i + 3
            elif op == 7:  # Less than
                a, b, c = self.data[i + 1: i + 4]
                val_a = self.data[a] if not mode_a else a
                val_b = self.data[b] if not mode_b else b
                self.data[c] = 1 if val_a < val_b else 0
                i += 4
            elif op == 8:  # Greater than
                a, b, c = self.data[i + 1: i + 4]
                val_a = self.data[a] if not mode_a else a
                val_b = self.data[b] if not mode_b else b
                self.data[c] = 1 if val_a == val_b else 0
                i += 4
            elif op == 99:
                return output


def feedback_loop(compies):
    output = 0
    while True:
        for compie in compies:
            compie.inval = output
            try:
                output = next(compie.output)
            except StopIteration:
                return output


def main():
    with open('input.txt') as f:
        data = [int(x) for x in next(f).split(',')]

    part_b = 0
    for phases in itertools.permutations(range(5, 10)):
        compies = [Computer(data, phase) for phase in phases]
        output = feedback_loop(compies)
        part_b = max(output, part_b)

    print(f'Part B: {part_b} - Max thruster signal w/ feedback loop')


if __name__ == '__main__':
    main()

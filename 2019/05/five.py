#!/usr/bin/env python


def parse_opcode(param):
    param = str(param).zfill(5)  # 0 padded
    op = int(param[-2:])
    modes = [int(x) for x in list(param[:-2])]
    return op, modes


def compute(data, in_value):
        i = 0
        output = []
        while True:
            op, (_, mode_b, mode_a) = parse_opcode(data[i])

            if op == 1:  # Add
                a, b, c = data[i + 1: i + 4]
                val_a = data[a] if not mode_a else a
                val_b = data[b] if not mode_b else b
                data[c] = val_a + val_b
                i += 4
            elif op == 2:  # Multiply
                a, b, c = data[i + 1: i + 4]
                val_a = data[a] if not mode_a else a
                val_b = data[b] if not mode_b else b
                data[c] = val_a * val_b
                i += 4
            elif op == 3:  # Input
                a = data[i + 1]
                data[a] = in_value
                i += 2
            elif op == 4:  # Output
                a = data[i + 1]
                val_a = data[a] if not mode_a else a
                output.append(val_a)
                i += 2
            elif op == 5:  # Jump if False
                a, b = data[i + 1: i + 3]
                val_a = data[a] if not mode_a else a
                val_b = data[b] if not mode_b else b
                i = val_b if val_a != 0 else i + 3
            elif op == 6:  # Jump if True
                a, b = data[i + 1: i + 3]
                val_a = data[a] if not mode_a else a
                val_b = data[b] if not mode_b else b
                i = val_b if val_a == 0 else i + 3
            elif op == 7:  # Less than
                a, b, c = data[i + 1: i + 4]
                val_a = data[a] if not mode_a else a
                val_b = data[b] if not mode_b else b
                data[c] = 1 if val_a < val_b else 0
                i += 4
            elif op == 8:  # Greater than
                a, b, c = data[i + 1: i + 4]
                val_a = data[a] if not mode_a else a
                val_b = data[b] if not mode_b else b
                data[c] = 1 if val_a == val_b else 0
                i += 4
            elif op == 99:
                return output


def main():
    with open('input.txt') as f:
        data = [int(x) for x in next(f).split(',')]

    part_a = compute(data.copy(), 1)[-1]
    print(f'Part A: {part_a} - Diagnostic code for system ID 1')

    part_b = compute(data.copy(), 5)[-1]
    print(f'Part B: {part_b} - Diagnostic code for system ID 5')


if __name__ == '__main__':
    main()

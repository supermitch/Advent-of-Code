#!/usr/bin/env python


def get_params(data):
    inst = str(data)
    op = int(inst[-2:])
    param_a = inst[-3:-2]
    param_a = int(param_a) if param_a else 0
    param_b = inst[-4:-3]
    param_b = int(param_b) if param_b else 0
    param_c = inst[-5:-4]
    param_c = int(param_c) if param_c else 0
    return op, param_a, param_b, param_c


def compute(data, in_value):
        i = 0
        output = []
        while True:
            op, mode_a, mode_b, mode_c = get_params(data[i])

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

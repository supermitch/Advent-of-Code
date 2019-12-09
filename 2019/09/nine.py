#!/usr/bin/env python


def parse_opcode(param):
    param = str(param).zfill(5)  # 0 padded
    op = int(param[-2:])
    modes = [int(x) for x in list(param[:-2])]
    return op, modes


def extend(data, n):
    if n >= len(data):
        data += [0] * (n - len(data) + 1)


def get_val(data, x, rel, mode):
    if mode == 1:  # Immediate
        return x
    if mode == 2:  # Relative
        x += rel
    extend(data, x)
    return data[x]  # Position or Relative modes


def set_val(data, value, x, rel, mode):
    if mode == 2:
        x += rel
    extend(data, x)
    data[x] = value  # Position or Relative modes


def compute(data, in_value):
        i = 0
        rel = 0  # Relative base
        output = []
        while True:
            op, (mode_c, mode_b, mode_a) = parse_opcode(data[i])

            if op == 1:  # Add
                a, b, c = data[i + 1: i + 4]
                val_a = get_val(data, a, rel, mode_a)
                val_b = get_val(data, b, rel, mode_b)
                set_val(data, val_a + val_b, c, rel, mode_c)
                i += 4
            elif op == 2:  # Multiply
                a, b, c = data[i + 1: i + 4]
                val_a = get_val(data, a, rel, mode_a)
                val_b = get_val(data, b, rel, mode_b)
                set_val(data, val_a * val_b, c, rel, mode_c)
                i += 4
            elif op == 3:  # Input
                a = data[i + 1]
                set_val(data, in_value, a, rel, mode_a)
                i += 2
            elif op == 4:  # Output
                a = data[i + 1]
                val_a = get_val(data, a, rel, mode_a)
                output.append(val_a)
                i += 2
            elif op == 5:  # Jump if False
                a, b = data[i + 1: i + 3]
                val_a = get_val(data, a, rel, mode_a)
                val_b = get_val(data, b, rel, mode_b)
                i = val_b if val_a != 0 else i + 3
            elif op == 6:  # Jump if True
                a, b = data[i + 1: i + 3]
                val_a = get_val(data, a, rel, mode_a)
                val_b = get_val(data, b, rel, mode_b)
                i = val_b if val_a == 0 else i + 3
            elif op == 7:  # Less than
                a, b, c = data[i + 1: i + 4]
                val_a = get_val(data, a, rel, mode_a)
                val_b = get_val(data, b, rel, mode_b)
                result = 1 if val_a < val_b else 0
                set_val(data, result, c, rel, mode_c)
                i += 4
            elif op == 8:  # Equal to
                a, b, c = data[i + 1: i + 4]
                val_a = get_val(data, a, rel, mode_a)
                val_b = get_val(data, b, rel, mode_b)
                result = 1 if val_a == val_b else 0
                set_val(data, result, c, rel, mode_c)
                i += 4
            elif op == 9:  # Adjust relative base
                a = data[i + 1]
                rel += get_val(data, a, rel, mode_a)
                i += 2
            elif op == 99:
                return output


def main():
    test_a = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    assert compute(test_a.copy(), 1) == test_a
    test_b = [1102,34915192,34915192,7,4,7,99,0]
    assert len(str(compute(test_b, 1)[0])) == 16
    test_c = [104,1125899906842624,99]
    assert compute(test_c, 1) == [1125899906842624]

    with open('input.txt') as f:
        data = [int(x) for x in next(f).split(',')]
    part_a = compute(data.copy(), 1)
    print(f'Part A: {part_a[0]} - BOOST keycode')
    part_b = compute(data.copy(), 2)
    print(f'Part B: {part_b[0]} - Distress signal coordinates')


if __name__ == '__main__':
    main()

from collections import defaultdict


def parse_line(line):
    d = line.strip().split()
    reg = d[1] if d[1].isalpha() else int(d[1])  # Sometimes register is an int
    try:
        v = d[2] if d[2].isalpha() else int(d[2])  # Sometimes value is a register
    except IndexError:
        v = None
    return d[0], reg, v  # Nominally: Type, register, value | None


def get_val(regs, val):
    return val if isinstance(val, int) else regs[val]


def part_a(data):
    registers = defaultdict(int)
    skip = None
    i = 0
    mul_count = 0
    while True:
        if i >= len(data) or i < 0:
            break
        d, r, v = data[i]

        if d == 'set':
            registers[r] = get_val(registers, v)
        elif d == 'sub':
            registers[r] -= get_val(registers, v)
        elif d == 'mul':
            registers[r] *= get_val(registers, v)
            mul_count += 1
        elif d == 'jnz':
            if get_val(registers, r) != 0:  # r could be an int!
                skip = get_val(registers, v)

        i += 1 if skip is None else skip
        skip = None
    return mul_count


def part_b(data):
    registers = defaultdict(int)
    registers['a'] = 1
    skip = None
    i = 0
    mul_count = 0
    while True:
        if i >= len(data) or i < 0:
            break
        d, r, v = data[i]
        print(registers)

        if d == 'set':
            registers[r] = get_val(registers, v)
        elif d == 'sub':
            registers[r] -= get_val(registers, v)
        elif d == 'mul':
            registers[r] *= get_val(registers, v)
            mul_count += 1
        elif d == 'jnz':
            if get_val(registers, r) != 0:  # r could be an int!
                skip = get_val(registers, v)

        i += 1 if skip is None else skip
        skip = None
    return mul_count



def main():
    with open('input.txt', 'r') as f:
        data = [parse_line(line) for line in f]

    mul_count = part_a(data)
    print('Part A: {} - No. of mul instructions'.format(mul_count))

    mul_count = part_b(data)
    print('Part B: {} - No. of mul instructions'.format(mul_count))

if __name__ == '__main__':
    main()


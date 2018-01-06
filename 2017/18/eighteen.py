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
    while True:
        if i >= len(data) or i < 0:
            break
        d, r, v = data[i]

        if d == 'set':
            registers[r] = get_val(registers, v)
        elif d == 'add':
            registers[r] += get_val(registers, v)
        elif d == 'mul':
            registers[r] *= get_val(registers, v)
        elif d == 'mod':
            registers[r] %= get_val(registers, v)
        elif d == 'snd':
            sound = registers[r]
        elif d == 'rcv':
            if registers[r] > 0:
                return sound
        elif d == 'jgz':
            if get_val(registers, r) > 0:  # r could be an int!
                skip = get_val(registers, v)

        i += 1 if skip is None else skip
        skip = None


def run_commands(name, registers, data, i, sent, received, send_count):
    skip = None
    while True:
        if i >= len(data) or i < 0:
            break
        d, r, v = data[i]

        if d == 'set':
            registers[r] = get_val(registers, v)
        elif d == 'add':
            registers[r] += get_val(registers, v)
        elif d == 'mul':
            registers[r] *= get_val(registers, v)
        elif d == 'mod':
            registers[r] %= get_val(registers, v)
        elif d == 'snd':
            sent.append(registers[r])
            send_count += 1
        elif d == 'rcv':
            if not received:
                break  # Wait for messages
            registers[r] = received.pop(0)
        elif d == 'jgz':
            if get_val(registers, r) > 0:  # r could be an int!
                skip = get_val(registers, v)

        i += 1 if skip is None else skip
        skip = None

    return i, sent, send_count, received, registers


def main():
    data = []
    with open('input.txt', 'r') as f:
        for line in f:
            data.append(parse_line(line))


    recovered = part_a(data)
    print('Part A: {} - First recovered frequency'.format(recovered))

    regs_a = defaultdict(int)
    regs_a['p'] = 0

    regs_b = defaultdict(int)
    regs_b['p'] = 1

    pos_a, count_a, msg_a = 0, 0, []
    pos_b, count_b, msg_b = 0, 0, []

    while True:  # Run "concurrent" programs, each writing to a message queue
        pos_a, msg_a, count_a, msg_b, regs_a = run_commands('Prog A', regs_a, data, pos_a, msg_a, msg_b, count_a)
        pos_b, msg_b, count_b, msg_a, regs_b = run_commands('Prog B', regs_b, data, pos_b, msg_b, msg_a, count_b)

        if pos_a >= len(data) and pos_b >= len(data):  # Ran out of instructions
            break
        if not msg_b and not msg_a:  # Deadlocked
            break

    print('Part B: {} - Messages sent by Program 1'.format(count_b))

if __name__ == '__main__':
    main()

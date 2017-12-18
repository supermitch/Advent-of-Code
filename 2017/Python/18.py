from collections import defaultdict


def parse_line(line):
    d = line.strip().split()

    try:
        reg = int(d[1])  # Sometimes register is an int
    except ValueError:
        reg = d[1]

    try:
        v = int(d[2])
    except ValueError:
        v = d[2]  # Sometimes value is a register
    except IndexError:
        v = None

    return d[0], reg, v  # Nominally: Type, register, value


def get_val(regs, val):
    if isinstance(val, int):
        return val
    else:
        return regs[val]


def run_commands(name, registers, data, pos, sent, received, send_count):
    skip = None
    i = pos
    waiting = False
    while True:
        if i >= len(data) or i < 0:
            break

        d, reg, val = data[i]

        if d == 'set':
            registers[reg] = get_val(registers, val)
        elif d == 'add':
            registers[reg] += get_val(registers, val)
        elif d == 'mul':
            registers[reg] *= get_val(registers, val)
        elif d == 'mod':
            registers[reg] %= get_val(registers, val)
        elif d == 'snd':
            sent.append(registers[reg])
            send_count += 1
        elif d == 'rcv':
            if not received:
                waiting = True
                break
            registers[reg] = received.pop(0)
        elif d == 'jgz':
            if isinstance(reg, int):
                if reg > 0:
                    skip = val
            else:
                if registers[reg] > 0:
                    if isinstance(val, int):
                        skip = val
                    else:
                        skip = registers[val]

        i += 1 if skip is None else skip
        skip = None

    return i, sent, send_count, received, registers, waiting


def main():
    data = []
    with open('18.input', 'r') as f:
        for line in f:
            data.append(parse_line(line))

    regs_a = defaultdict(int)
    regs_a['p'] = 0

    regs_b = defaultdict(int)
    regs_b['p'] = 1

    pos_a, count_a, msg_a = 0, 0, []
    pos_b, count_b, msg_b = 0, 0, []

    while True:
        if pos_a <= len(data):
            pos_a, msg_a, count_a, msg_b, regs_a, waiting_a = run_commands('Prog A', regs_a, data, pos_a, msg_a, msg_b, count_a)
        if pos_b <= len(data):
            pos_b, msg_b, count_b, msg_a, regs_b, waiting_b = run_commands('Prog B', regs_b, data, pos_b, msg_b, msg_a, count_b)

        if pos_a >= len(data) and pos_b >= len(data):  # Ran out of instructions
            break
        if waiting_a and waiting_b and not msg_b and not msg_a:  # Deadlocked
            break

    print('Part B: {} - Messages sent by Program 1'.format(count_b))

if __name__ == '__main__':
    main()

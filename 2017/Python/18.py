from collections import namedtuple, defaultdict, OrderedDict


class Obj:
    def __init__(self, val):
        self.val = val


def parse_line(line):
    d = line.strip().split()
    t = d[0]

    try:
        reg = int(d[1])
    except ValueError:
        reg = d[1]

    try:
        v = int(d[2])
    except ValueError:
        v = d[2]
    except IndexError:
        v = None

    return t, reg, v


def main():
    data = []
    with open('18.input', 'r') as f:
        for line in f:
            data.append(parse_line(line))
    print(data)

    test = [
        'set a 1',
        'add a 2',
        'mul a a',
        'mod a 5',
        'snd a',
        'set a 0',
        'rcv a',
        'jgz a -1',
        'set a 1',
        'jgz a -2',
    ]

    play_sound = None
    recovered_sound = None
    skip = None

    registers = defaultdict(int)
    for d, reg, v in data:
        if isinstance(reg, int):
            continue
        registers[reg] = 0

    i = 0
    while True:
        if i >= len(data) or i < 0:
            break
        d, reg, val = data[i]
        print(d, reg, val)

        if isinstance(reg, int):
            pass
        else:
            if reg not in registers:
                registers[reg] = 0

        try:
            val = int(val)
        except (TypeError, ValueError):
            if val not in registers:
                registers[val] = 0

        if d == 'set':
            if isinstance(val, int):
                registers[reg] = val
            else:
                registers[reg] = registers[val]
        elif d == 'add':
            if isinstance(val, int):
                registers[reg] += val
            else:
                registers[reg] += registers[val]
        elif d == 'mul':
            if isinstance(val, int):
                registers[reg] *= val
            else:
                registers[reg] *= registers[val]
        elif d == 'mod':
            try:
                if isinstance(val, int):
                    registers[reg] %= val
                else:
                    registers[reg] %= registers[val]
            except ZeroDivisionError:
                print('Zero division')
                registers[reg] = 0
        elif d == 'snd':
            play_sound = registers[reg]
        elif d == 'rcv':
            if registers[reg] > 0:
                recovered_sound = play_sound if play_sound is not None else None
                print('Recovered: ', recovered_sound)
                break
        elif d == 'jgz':
            try:
                reg = int(reg)
            except ValueError:
                if registers[reg] > 0:
                    skip = val
            else:
                if reg > 0:
                    skip = val
        if skip:
            i += skip
            skip = None
        else:
            i += 1
        print(registers)



if __name__ == '__main__':
    main()

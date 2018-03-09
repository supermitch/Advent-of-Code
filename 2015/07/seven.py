def parse(line):
    parts = line.split()
    if 'AND' in parts:
        return ('and', parts[0], parts[2], parts[4])
    elif 'OR' in parts:
        return ('or', parts[0], parts[2], parts[4])
    elif 'LSHIFT' in parts:
        return ('lshift', parts[0], parts[2], parts[4])
    elif 'RSHIFT' in parts:
        return ('rshift', parts[0], parts[2], parts[4])
    elif 'NOT' in parts:
        return ('not', parts[1], 999, parts[3])  # 999 is unused
    else:
        return ('set', parts[0], 999, parts[2])


def get(circuit, val):
    """
    'val' can be an int, or a str wire name.
    A wire may not have a value yet: In that case, just return None.
    """
    try:
        return int(val)
    except ValueError:  # Not an integer
        if val in circuit:
            return int(circuit[val])
        else:
            return None


def run_circuit(rules):
    circuit = {}
    seen = set()
    while len(seen) < len(rules):
        for rule in rules:
            d, a, b, o = rule  # b is None for 'set' & 'not'
            a = get(circuit, a)
            b = get(circuit, b)
            if None in (a, b):
                continue

            if d == 'set':
                circuit[o] = a
            elif d == 'not':  # not
                circuit[o] = ~ a & 0xffff  # 16-bit unsigned
            elif d in ('lshift', 'rshift'):
                circuit[o] = a << b if d == 'lshift' else a >> b
            elif d in ('and', 'or'):
                circuit[o] = a & b if d == 'and' else a | b

            seen.add(rule)  # Rule was completed if we didn't continue
    return circuit


def main():
    test_rules = [
        '123 -> x',
        '456 -> y',
        'x AND y -> d',
        'x OR y -> e',
        'x LSHIFT 2 -> f',
        'y RSHIFT 2 -> g',
        'NOT x -> h',
        'NOT y -> i',
    ]
    rules = [parse(l) for l in test_rules]
    results = run_circuit(rules)
    expected = {'d': 72, 'e': 507, 'f': 492, 'g': 114, 'h': 65412, 'i': 65079, 'x': 123, 'y': 456}
    assert results == expected

    with open('input.txt', 'r') as f:
        rules = [parse(l) for l in f]

    part_a = run_circuit(rules)['a']
    print('Part A: {} - Value of wire a'.format(part_a))

    # Part B: Let's override wire 'b' w/ the last result
    for i in range(len(rules)):
        if rules[i][0] == 'set' and rules[i][3] == 'b':
            rules[i] = ('set', part_a, 999, 'b')

    part_b = run_circuit(rules)['a']
    print('Part B: {} - Value of wire a w/ new wire b'.format(part_b))


if __name__ == '__main__':
    main()

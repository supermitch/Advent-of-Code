from pprint import pprint


def parse(line):
    parts = line.split()

    if 'AND' in parts:
        rule = ('and', parts[0], parts[2], parts[4])
    elif 'OR' in parts:
        rule = ('or', parts[0], parts[2], parts[4])
    elif 'LSHIFT' in parts:
        rule = ('lshift', parts[0], int(parts[2]), parts[4])  # (LSHIFT x, 2 -> f)
    elif 'RSHIFT' in parts:
        rule = ('rshift', parts[0], int(parts[2]), parts[4])
    elif 'NOT' in parts:
        rule = ('not', parts[1], parts[3])
    else:
        rule = ('set', parts[2], parts[0])  # Parts 0 could be a wire name

    return rule


def run_circuit(rules):
    circuit = {}
    seen = set()
    while len(seen) < len(rules):
        for rule in rules:
            if rule[0] == 'set':
                _, wire, val = rule
                try:
                    val = int(val)
                except ValueError:  # Val is a string
                    if val in circuit:
                        val = int(circuit[val])
                    else:
                        continue
                circuit[wire] = val
                seen.add(rule)
            elif rule[0] == 'not':
                _, i, o = rule
                if i in circuit:
                    circuit[o] = ~ circuit[i] & 0xffff
                    seen.add(rule)
            elif rule[0] in ['lshift', 'rshift']:
                d, i, val, o = rule
                if i not in circuit:
                    continue
                if d == 'lshift':
                    circuit[o] = circuit[i] << val
                else:
                    circuit[o] = circuit[i] >> val
                seen.add(rule)
            elif rule[0] in ['and', 'or']:
                d, a, b, o = rule
                if a not in circuit or b not in circuit:
                    continue
                if d == 'and':
                    circuit[o] = circuit[a] & circuit[b]
                else:
                    circuit[o] = circuit[a] | circuit[b]
                seen.add(rule)
    return circuit


def main():
    test = [
        '123 -> x',
        '456 -> y',
        'x AND y -> d',
        'x OR y -> e',
        'x LSHIFT 2 -> f',
        'y RSHIFT 2 -> g',
        'NOT x -> h',
        'NOT y -> i',
    ]
    rules = [parse(l) for l in test]
    pprint(rules)
    results = run_circuit(rules)
    expected = {
        'd': 72,
        'e': 507,
        'f': 492,
        'g': 114,
        'h': 65412,
        'i': 65079,
        'x': 123,
        'y': 456,
    }
    assert results == expected

    with open('input.txt', 'r') as f:
        rules = [parse(l) for l in f]
    circuit = run_circuit(rules)
    print(circuit['a'])


if __name__ == '__main__':
    main()

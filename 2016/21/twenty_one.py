from collections import deque


def parse(line):
    parts = line.split()
    if 'move' in parts:
        return ('move', int(parts[2]), int(parts[5]))
    elif 'swap letter' in line:
        return ('swap', parts[2], parts[5])
    elif 'swap position' in line:
        return ('swap_pos', int(parts[2]), int(parts[5]))
    elif 'reverse' in parts:
        return ('rev', int(parts[2]), int(parts[4]))
    elif parts[1] in ('left', 'right'):
        return (parts[1], int(parts[2]), None)
    elif 'on' in parts:  # 'rotate based on...'
        return ('rot', parts[-1], None)


def run(rule, input, reverse=False):
    act, a, b = rule
    d = deque(input)
    if act == 'move':
        l = list(input)
        char_a = l.pop(a)  # Can't pop(index) a deque!
        l.insert(b, char_a)
        d = deque(l)
    elif act == 'swap':  # Same when reversed
        idx_a = d.index(a)
        idx_b = d.index(b)
        d[idx_a], d[idx_b] = d[idx_b], d[idx_a]
    elif act == 'swap_pos':  # Same when reversed
        d[a], d[b] = d[b], d[a]
    elif act == 'rev':  # Same when reversed
        b += 1  # Range is inclusive
        l = input[:a] + input[a:b][::-1] + input[b:]
        d = deque(l)  # Can't slice a deque!
    elif act == 'left':
        d.rotate(a if reverse else -a)
    elif act == 'right':
        d.rotate(-a if reverse else a)
    elif act == 'rot':
        idx_a = d.index(a)
        if reverse:  # For an 8 char string only!
            n = {  # Each end position had only 1 possible starting point
                0: -1,
                1: -1,
                2: 2,
                3: -2,
                4: 1,
                5: -3,
                6: 0,
                7: -4,
            }[idx_a]
            d.rotate(n)
        else:  # To scramble we can calculate result
            n = 1 + idx_a + (1 if idx_a >= 4 else 0)
            d.rotate(n)
    return ''.join(d)


def main():
    input = 'abcde'
    test = [
        'swap position 4 with position 0',
        'swap letter d with letter b',
        'reverse positions 0 through 4',
        'rotate left 1 step',
        'move position 1 to position 4',
        'move position 3 to position 0',
        'rotate based on position of letter b',
        'rotate based on position of letter d',
    ]
    test_rules = [parse(l.strip()) for l in test]
    assert run(test_rules[0], 'abcde') == 'ebcda'
    assert run(test_rules[1], 'ebcda') == 'edcba'
    assert run(test_rules[2], 'edcba') == 'abcde'
    assert run(test_rules[3], 'abcde') == 'bcdea'
    assert run(test_rules[4], 'bcdea') == 'bdeac'
    assert run(test_rules[5], 'bdeac') == 'abdec'
    assert run(test_rules[6], 'abdec') == 'ecabd'
    assert run(test_rules[7], 'ecabd') == 'decab'


    with open('input.txt', 'r') as f:
        rules = [parse(l.strip()) for l in f]

    password = 'abcdefgh'
    for rule in rules:
        password = run(rule, password)
    print('Part A: {} - Scrambled password'.format(password))

    password = 'fbgdceah'
    for rule in rules[::-1]:
        password = run(rule, password, reverse=True)
    print('Part B: {} - Unscrambled password'.format(password))


if __name__ == '__main__':
    main()

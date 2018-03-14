from collections import deque
from pprint import pprint


def parse(line):
    parts = line.split()
    if 'move' in parts:
        return ('mov', int(parts[2]), int(parts[5]))
    elif 'swap letter' in line:
        return ('swp', parts[2], parts[5])
    elif 'swap position' in line:
        return ('swp_pos', int(parts[2]), int(parts[5]))
    elif 'reverse' in parts:
        return ('rev', int(parts[2]), int(parts[4]))
    elif parts[1] in ('left', 'right'):
        return (parts[1], int(parts[2]), None)
    elif 'on' in parts:  # 'rotate based on...'
        return ('rot', parts[-1], None)


def run(rule, input, reverse=False):
    act, a, b = rule
    if act == 'mov':
        if reverse:
            a, b = b, a
        l = list(input)
        char_a = l.pop(a)
        l.insert(b, char_a)
        input = ''.join(l)
    elif act == 'swp':
        idx_a = input.find(a)
        idx_b = input.find(b)
        l = list(input)
        l[idx_a], l[idx_b] = l[idx_b], l[idx_a]
        input = ''.join(l)
    elif act == 'swp_pos':
        l = list(input)
        l[a], l[b] = l[b], l[a]
        input = ''.join(l)
    elif act == 'rev':
        b += 1  # Range is inclusive
        mid = input[a:b]
        input = input[:a] + mid[::-1] + input[b:]
    elif act == 'left':
        d = deque(input)
        if reverse:
            d.rotate(a)
        else:
            d.rotate(-a)
        input = ''.join(d)
    elif act == 'right':
        d = deque(input)
        if reverse:
            d.rotate(-a)
        else:
            d.rotate(a)
        input = ''.join(d)
    elif act == 'rot':
        idx_a = input.find(a)
        d = deque(input)
        if reverse:
            n = {
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
        else:
            n = 1 + idx_a + (1 if idx_a >= 4 else 0)
            d.rotate(n)
        input = ''.join(d)
    return input


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

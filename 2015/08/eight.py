#!/usr/bin/env python


def memory_diff(strings):
    diff = 0
    for string in strings:
        diff += 2  # Surrounding quotes
        i = 0
        while i < len(string) - 2:
            i += 1
            piece = string[i:i + 2]
            if piece == r'\\' or piece == r'\"':
                diff += 1
                i += 1
            elif piece == r'\x':
                diff += 3  # Two hex chars
                i += 3
    return diff


def encoded_diff(strings):
    return sum(s.count('"') + s.count('\\') + 2 for s in strings)


def main():
    test = [r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"']
    assert memory_diff(test) == 12
    assert encoded_diff(test) == 19

    with open('input.txt', 'r') as f:
        strings = [l.strip() for l in f]

    diff = memory_diff(strings)
    print('Part A: {} - Difference between chars and literals'.format(diff))

    encoded = encoded_diff(strings)
    print('Part B: {} - Difference between encoded strings'.format(encoded))


if __name__ == '__main__':
    main()

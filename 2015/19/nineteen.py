#!/usr/bin/env python
from collections import defaultdict


def read_input():
    replacements = defaultdict(list)
    with open('input.txt', 'r') as f:
        for line in f:
            parts = line.strip().split()
            if '=>' in parts:
                replacements[parts[0]].append(parts[2])
            else:
                if parts:  # Skip blank line
                    molecule = parts[0]
    return replacements, molecule


def find_all(replacements, start):
    return options


def find_distinct(replacements, start):
    options = find_all(replacements, start)
    return set(options)


def main():
    test_replacements = {'H': ['HO', 'OH'], 'O': ['HH']}
    assert len(find_all(test_replacements, 'HOH')) == 5
    assert len(find_all(test_replacements, 'HOHOHO')) == 9
    assert len(find_distinct(test_replacements, 'HOH')) == 4
    assert len(find_distinct(test_replacements, 'HOHOHO')) == 7

    replacements, molecule = read_input()
    print(replacements)
    print(molecule)


if __name__ == '__main__':
    main()

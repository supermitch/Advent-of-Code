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
    options = []
    for sub, elements in replacements.items():
        for element in elements:
            idx = 0
            while True:
                idx = start.find(sub, idx)
                if idx != -1:  # If found
                    options.append(start[:idx] + element + start[idx + len(sub):])
                    idx += 1
                else:
                    break
    return options


def find_distinct(replacements, start):
    options = find_all(replacements, start)
    return set(options)


def fabricate_molecule(replacements, molecule):
    options = ['e']  # Starting molecule
    count = 0
    while True:
        count += 1
        print(count)
        new_options = set()
        for option in options:
            new = find_all(replacements, option)
            if molecule in new:
                return count
            new_options.update(new)
        options = new_options.copy()


def main():
    test_replacements = {'H': ['HO', 'OH'], 'O': ['HH']}
    assert len(find_all(test_replacements, 'HOH')) == 5
    assert len(find_all(test_replacements, 'HOHOHO')) == 9
    assert len(find_distinct(test_replacements, 'HOH')) == 4
    assert len(find_distinct(test_replacements, 'HOHOHO')) == 7

    replacements, molecule = read_input()
    distinct = find_distinct(replacements, molecule)
    print('Part A: {} - Distinct molecules after all single replacements'.format(len(distinct)))

    test_replacements = {'e': ['H', 'O'], 'H': ['HO', 'OH'], 'O': ['HH']}
    assert fabricate_molecule(test_replacements, 'HOH') == 3
    assert fabricate_molecule(test_replacements, 'HOHOHO') == 6

    count = fabricate_molecule(replacements, molecule)
    print('Part B: {} - Steps until medicine is fabricated'.format(count))


if __name__ == '__main__':
    main()

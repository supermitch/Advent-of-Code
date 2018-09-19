#!/usr/bin/env python
import collections


def read_input():
    replacements = collections.defaultdict(list)
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
    opts = []
    for sub, elements in replacements.items():
        for elem in elements:
            idx = 0
            while True:
                idx = start.find(sub, idx)
                if idx != -1:  # If found
                    opts.append(start[:idx] + elem + start[idx + len(sub):])
                    idx += 1
                else:
                    break
    return opts


def order_replacements_by_output(replacements):
    arr = [(v, k) for k, vs in replacements.items() for v in vs]
    return sorted(arr, key=lambda x: len(x[0]), reverse=True)


def fabricate_molecule(replacements, goal):
    options = ['e']  # Starting molecule
    count = 0
    while True:
        count += 1
        if not count % 10000:
            print(count)
        new_options = set()
        for option in options:
            new = find_all(replacements, option)
            if goal in new:
                return count
            new_options.update(new)
        options = new_options.copy()


def revert(mol, rep):
    new, old = rep  # e.g. ('ORnFAr', 'H')
    idx = mol.find(new)
    return mol[:idx] + old + mol[idx + len(new):]


def defab(reps, start, goal='e'):
    molecule = start
    count = 0
    blocked = False
    while not blocked:
        blocked = True
        for new, old in reps:
            if new in molecule:
                blocked = False
                molecule = revert(molecule, (new, old))
                count += 1
                if molecule == goal:
                    return count
    return count



def main():
    test_replacements = {'H': ['HO', 'OH'], 'O': ['HH']}
    assert len(find_all(test_replacements, 'HOH')) == 5
    assert len(find_all(test_replacements, 'HOHOHO')) == 9
    assert len(set(find_all(test_replacements, 'HOH'))) == 4
    assert len(set(find_all(test_replacements, 'HOHOHO'))) == 7

    replacements, molecule = read_input()
    count = len(set(find_all(replacements, molecule)))
    print('Part A: {} - Distinct molecules'.format(count))

    test_replacements = {'e': ['H', 'O'], 'H': ['HO', 'OH'], 'O': ['HH']}
    test_ordered = order_replacements_by_output(test_replacements)
    assert fabricate_molecule(test_replacements, 'HOH') == 3
    assert fabricate_molecule(test_replacements, 'HOHOHO') == 6

    assert revert('Hello there', ('o t', 'cat')) == 'Hellcathere'

    assert defab(test_ordered, 'HOH') == 3
    assert defab(test_ordered, 'HOHOHO') == 6

    print('asserts passed')
    reps = order_replacements_by_output(replacements)
    count = defab(reps, molecule)
    # count = fabricate_molecule(replacements, molecule)
    print('Part B: {} - Steps until medicine is fabricated'.format(count))


if __name__ == '__main__':
    main()

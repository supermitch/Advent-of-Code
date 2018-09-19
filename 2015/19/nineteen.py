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


def order_by_len(replacements):
    arr = [(v, k) for k, vs in replacements.items() for v in vs]
    return sorted(arr, key=lambda x: len(x[0]), reverse=True)


def revert(mol, rep):
    new, old = rep  # e.g. ('ORnFAr', 'H')
    idx = mol.find(new)
    return mol[:idx] + old + mol[idx + len(new):]


def defabricate(reps, start, goal='e'):
    molecule = start
    count = 0
    while True:
        blocked = True
        for new, old in reps:
            if new in molecule:
                blocked = False
                molecule = revert(molecule, (new, old))
                count += 1
                if molecule == goal:
                    return count
        if blocked:
            print('Could not converge!')
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
    test_ordered = order_by_len(test_replacements)
    assert defabricate(test_ordered, 'HOH') == 3
    assert defabricate(test_ordered, 'HOHOHO') == 6  # Fails to converge

    count = defabricate(order_by_len(replacements), molecule)
    print('Part B: {} - Steps until medicine is fabricated'.format(count))


if __name__ == '__main__':
    main()

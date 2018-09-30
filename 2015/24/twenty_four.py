#!/usr/bin/env python

from itertools import combinations


def product(iter):
    acc = 1
    for i in iter:
        acc *= i
    return acc


def find_arrangements(weights):
    target = sum(weights) / 3
    n = len(weights)
    lowest_entanglement = 999999999999999
    best_arrangement = None
    seen = set()
    found_g1_size = None
    for n1 in range(1, n - 2):
        for n2 in range(1, n - n1 - 1):
            n3 = n - n1 - n2
            print('n: {}, {}, {}'.format(n1, n2, n3))

            sizes = tuple(sorted([n1, n2, n3]))
            if sizes in seen:  # No repeat sizes, e.g. 2,2,4 = 2,4,2 = 4,2,2
                continue
            seen.add(sizes)

            for g1 in combinations(weights, n1):
                if sum(g1) != target:
                    continue

                g2_weights = weights - set(g1)
                for g2 in combinations(g2_weights, n2):
                    if sum(g2) != target:
                        continue

                    g3 = g2_weights - set(g2)  # Group 3 order is unimportant

                    if found_g1_size is None:
                        found_g1_size = n1
                    elif n1 > found_g1_size:  # We already found all the smallest group 1s
                        return lowest_entanglement

                    if n1 < n2 and n1 < n3:
                        entanglement = product(g1)
                        if entanglement < lowest_entanglement:
                            lowest_entanglement = entanglement
                    elif n2 < n3:
                        entanglement = product(g2)
                        if entanglement < lowest_entanglement:
                            lowest_entanglement = entanglement
                    else:
                        entanglement = product(g3)
                        if entanglement < lowest_entanglement:
                            lowest_entanglement = entanglement


def main():
    test_weights = {1, 2, 3, 4, 5, 7, 8, 9, 10, 11}
    lowest_entanglement = find_arrangements(test_weights)
    print(lowest_entanglement)

    with open('input.txt', 'r') as f:
        weights = {int(l.strip()) for l in f}

    lowest_entanglement = find_arrangements(weights)
    print(lowest_entanglement)


if __name__ == '__main__':
    main()

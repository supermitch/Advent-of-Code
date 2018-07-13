#!/usr/bin/env python

from itertools import combinations


def product(iter):
    acc = 1
    for i in iter:
        acc *= i
    return acc


def find_arrangements(weights, n_groups=3):
    n = len(weights)
    arrangements = []
    seen = set()
    found_g1_size = None
    for n1 in range(1, n - 2):
        for n2 in range(1, n - n1 - 1):
            n3 = n - n1 - n2
            print('n: {}, {}, {}'.format(n1, n2, n3))

            sizes = tuple(sorted([n1, n2, n3]))
            if sizes in seen:  # No repeat sizes, e.g. 2,2,4 = 2,4,2 = 4,2,2
                continue
            else:
                seen.add(sizes)

            for g1 in combinations(weights, n1):
                s1 = sum(g1)
                g2_weights = weights - set(g1)
                for g2 in combinations(g2_weights, n2):
                    s2 = sum(g2)
                    if s1 != s2:
                        continue
                    p1 = product(g1)
                    p2 = product(g2)
                    g3 = g2_weights - set(g2)  # Group 3 order is unimportant
                    if s2 == sum(g3):  # We already know g1 matches g2
                        if found_g1_size is None:
                            found_g1_size = n1
                        elif n1 > found_g1_size:  # We already found all the smallest group 1s
                            return arrangements
                        if n1 < n2 and n1 < n3:
                            entanglement = p1
                            # arrangements.append((n1, entanglement, g1, g2, g3))
                            arrangements.append((n1, g1))
                        elif n2 < n3:
                            entanglement = p2
                            # arrangements.append((n2, entanglement, g2, g2, g3))
                            arrangements.append((n2, g2))
                        else:
                            entanglement = product(g3)
                            # arrangements.append((n3, entanglement, g2, g2, g3))
                            arrangements.append((n3, g3))
    return arrangements


def main():
    test_weights = {1, 2, 3, 4, 5, 7, 8, 9, 10, 11}
    # arrangements = find_arrangements(test_weights)

    with open('input.txt', 'r') as f:
        weights = {int(l.strip()) for l in f}

    print('Found {} weights'.format(len(weights)))

    for groups in find_arrangements(weights):
        print(groups)


if __name__ == '__main__':
    main()

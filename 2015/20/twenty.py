import itertools


def factors(n):
    """ Find the non-zero natural factors of n. """
    factors = set()
    for f in range(1, n):
        if f * f > n:
            return factors
        if n % f == 0:
            factors.update({f, n//f})
    return factors


def infinite_houses(goal):
    """ A: Elves deliver 10 gifts to infinite houses. """
    goal = goal / 10  # Each elf delivers 10 gifts, so we can just count elves
    for i in itertools.count():
        if sum(factors(i)) >= goal:
            return i


def fifty_houses(goal):
    """ B: Elves deliver 11 gifts to a max of 50 houses. """
    goal = goal / 11
    for i in itertools.count():
        remaining = {x for x in factors(i) if x > i // 50}
        if sum(remaining) >= goal:
            return i


def main():
    assert factors(9) == {1, 3, 9}
    assert factors(14) == {1, 2, 7, 14}

    goal = 36_000_000

    i = infinite_houses(goal)
    print('Part A: {} - 1st house to 36M gifts w/ infinite visits'.format(i))

    i = fifty_houses(goal)
    print('Part B: {} - 1st house to 36M gifts w/ 50-house limit'.format(i))


if __name__ == '__main__':
    main()

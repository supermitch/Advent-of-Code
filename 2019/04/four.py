#!/usr/bin/env python
import itertools
import operator


def adj(i, strict=False):
    func = operator.eq if strict else operator.ge
    return any(func(len(list(g)), 2) for _, g in itertools.groupby(str(i)))


def sorter(i):
    return ''.join(sorted(str(i))) == str(i)


def main():
    a, b = 156218, 652527
    part_a = sum(sorter(i) and adj(i) for i in range(a, b + 1))
    part_b = sum(sorter(i) and adj(i, strict=True) for i in range(a, b + 1))

    print(f'Part A: {part_a} - No. of potential passwords')
    print(f'Part B: {part_b} - No. of potential passwords with strict batches')


if __name__ == '__main__':
    main()

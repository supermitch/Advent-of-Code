#!/usr/bin/env python
import itertools
import operator


def adj(string, strict=False):
    func = operator.eq if strict else operator.ge
    return any(func(len(list(g)), 2) for _, g in itertools.groupby(string))


def sorter(string):
    return ''.join(sorted(string)) == string


def main():
    count = 0
    strict = 0
    for i in range(156218, 652527 + 1):
        string = str(i)
        if sorter(string):
            if adj(string):
                count += 1
            if adj(string, strict=True):
                strict += 1

    print(f'Part A: {count} - No. of potential passwords')
    print(f'Part B: {strict} - No. of potential passwords with strict batches')


if __name__ == '__main__':
    main()

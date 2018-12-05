#!/usr/bin/env python
from collections import defaultdict, OrderedDict, Counter
from itertools import permutations

def parse(line):
    return line

def read_input():
    with open('input.txt', 'r') as f:
        return [l.strip() for l in f][0]

def main():
    print('\nHello2')
    data = read_input()

    def cancel(data):
        found = False
        for i in range(len(data) - 1):
            x = data[i]
            y = data[i + 1]

            if x.lower() == y.lower() and x != y:
                new = data[:i] + data[i + 2:]
                return new, True
        return data, False

    def part_b(data):
        while True:
            data, found = cancel(data)
            if found:
                continue
            else:
                return data, len(data)

    # data, length = part_b(data)
    # with open('a.txt', 'w') as f:
    #     f.write(data)

    with open('a.txt', 'r') as f:
        for l in f:
            data = l.strip()

    import string
    def part_c(data):
        mini = 999999999
        for letter in string.ascii_lowercase:
            print(letter)
            dat = data[:]
            dat = dat.replace(letter, '')
            dat = dat.replace(letter.upper(), '')
            dat, length = part_b(dat)
            print(length)
            if length < mini:
                mini = length

        print(mini)

    part_c(data)
if __name__ == '__main__':
    main()

#!/usr/bin/env python
import itertools


def compute(data, noun, verb):
        data[1] = noun
        data[2] = verb
        i = 0
        while True:
            if data[i] == 1:
                a, b, c = data[i + 1: i + 4]
                data[c] = data[a] + data[b]
            elif data[i] == 2:
                a, b, c = data[i + 1: i + 4]
                data[c] = data[a] * data[b]
            elif data[i] == 99:
                return data[0]
            i += 4


def main():
    with open('input.txt') as f:
        l = next(f)
        data = [int(x) for x in l.split(',')]

    part_a = compute(data.copy(), 12, 2)
    print(f'Part A: {part_a} - Result in pos. 0 for noun 12, verb 2')

    for noun, verb in itertools.product(range(100), range(100)):
        if compute(data.copy(), noun, verb) == 19690720:
            part_b = 100 * noun + verb
            break
    print(f'Part B: {part_b} - Calculated input for result 19690720')


if __name__ == '__main__':
    main()

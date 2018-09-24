#!/usr/bin/env python
from itertools import groupby


def look_and_say(seq, n):
    for _ in range(n):
        seq = ''.join(str(len(list(g))) + k for k, g in groupby(seq))
    return len(seq)


def main():
    assert look_and_say('1', 1) == 2  # '11'
    assert look_and_say('21', 1) == 4  # '2111'
    assert look_and_say('111221', 1) == 6  # '312211'

    _input = '1113222113'
    print('Part A: {} - Len after 40 iters'.format(look_and_say(_input, 40)))
    print('Part B: {} - Len after 50 iters'.format(look_and_say(_input, 50)))


if __name__ == '__main__':
    main()

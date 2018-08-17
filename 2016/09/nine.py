#!/usr/bin/env python
import re


def decomp(data, recurse=False):
    m = re.search(r'\(([0-9]+)x([0-9]+)\)', data)  # Search for a valid marker, e.g. (12x8)
    if m:
        chars, mult = int(m[1]), int(m[2])  # Char count and multiplier
        start, end = m.span()  # i.e. 'start' normal chars before match
        repeated = data[end:end + chars]  # Compressed data
        tail = data[end + chars:]  # Remainder of the data

        if recurse:
            return start + mult * decomp(repeated, True) + decomp(tail, True)
        else:
            return start + mult * len(repeated) + decomp(tail)
    else:  # No compression in this data
        return len(data)


def main():
    with open('input.txt', 'r') as f:
        comp = f.read().strip()

    # Single pass decompression
    assert decomp('ADVENT') == len('ADVENT')
    assert decomp('A(1x5)BC') == len('ABBBBBC')
    assert decomp('(3x3)XYZ') == len('XYZXYZXYZ')
    assert decomp('(6x1)(1x3)A') == len('(1x3)A')
    assert decomp('X(8x2)(3x3)ABCY') == len('X(3x3)ABC(3x3)ABCY')
    # Recursive decompression
    assert decomp('(3x3)XYZ', True) == len('XYZXYZXYZ')
    assert decomp('X(8x2)(3x3)ABCY', True) == len('XABCABCABCABCABCABCY')
    assert decomp('(27x12)(20x12)(13x14)(7x10)(1x12)A', True) == 241920
    assert decomp('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', True) == 445

    print('Part A: {} - Decompressed length'.format(decomp(comp)))
    print('Part B: {} - Recursive decompressed length'.format(decomp(comp, True)))


if __name__ == '__main__':
    main()

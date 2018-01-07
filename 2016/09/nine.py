import re


def decompress(comp):
    decomp = ''
    i = 0
    while i < len(comp):
        if comp[i] == '(':  # Found a marker?
            m = re.match(r'\(([0-9]+)x([0-9]+)\)', comp[i:])  # Extract a valid marker, e.g. (12x8)
            count, repeat = int(m[1]), int(m[2])
            i += comp[i:].find(')') + 1  # Skip past our marker
            expanded = comp[i:i + count] * repeat  # Decompress our chunk
            decomp += expanded  # Add it to output
            i += count  # Skip the compressed chars before continuing
        else:
            decomp += comp[i]
            i += 1
    return decomp


def main():
    with open('input.txt', 'r') as f:
        comp = f.read().strip()

    assert decompress('ADVENT') == 'ADVENT'
    assert decompress('A(1x5)BC') == 'ABBBBBC'
    assert decompress('(3x3)XYZ') == 'XYZXYZXYZ'
    assert decompress('(6x1)(1x3)A') == '(1x3)A'
    assert decompress('X(8x2)(3x3)ABCY') == 'X(3x3)ABC(3x3)ABCY'

    part_a = len(decompress(comp))
    print('Part A: {} - Decompressed length'.format(part_a))

    print('Part B: {} - '.format(None))


if __name__ == '__main__':
    main()

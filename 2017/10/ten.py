from functools import reduce
from operator import xor

# Part A
def twist_round(arr, lengths, pos=0, skip=0):
    n = len(arr)
    for length in lengths:
        extract = [arr[(pos + i) % n] for i in range(length)]
        extract.reverse()

        for i in range(length):
            arr[(pos + i) % n] = extract[i]  # Write back into arr

        pos = (pos + length + skip) % n
        skip += 1
    return arr, pos, skip

# Part B
def to_hex(ints):
    return [format(x, '02x') for x in ints]


def make_hash(string_input):
    input = [ord(str(c)) for c in string_input]
    length = input + [17, 31, 73, 47, 23]  # Add hardcoded suffix

    sparse = list(range(0, 256))
    pos = 0
    skip = 0
    for _ in range(64):
        sparse, pos, skip = twist_round(sparse, length, pos, skip)

    dense = []
    for i in range(16):
        b = sparse[i * 16:(i + 1) * 16]  # Chunk by 16
        dense.append(reduce(xor, b))  # Reduce each chunk

    hex_hash = to_hex(dense)
    return ''.join(hex_hash)


def main():
    # Part A:
    result, _, _ = twist_round(list(range(5)), [3, 4, 1, 5])
    assert result[0] * result[1] == 12

    input = [46, 41, 212, 83, 1, 255, 157, 65, 139, 52, 39, 254, 2, 86, 0, 204]
    result, _, _ = twist_round(list(range(0, 256)), input)
    print('Part A: {} - Single round knot twisting'.format(result[0] * result[1]))

    # Part B:
    assert reduce(xor, [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]) == 64
    assert to_hex([64, 7, 255]) == ['40', '07', 'ff']

    assert make_hash('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
    assert make_hash('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'

    input = [46, 41, 212, 83, 1, 255, 157, 65, 139, 52, 39, 254, 2, 86, 0, 204]
    string_input = ','.join(str(x) for x in input)
    knot_hash = make_hash(string_input)
    print('Part B: {} - Knot Hash'.format(knot_hash))


if __name__ == '__main__':
    main()

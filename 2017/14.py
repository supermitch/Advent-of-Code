import time

# Day 10 Code ===============
from functools import reduce
from operator import xor

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
# ===========================

def to_bin(my_hexdata):  # From Stackoverflow
    scale = 16  # equals to hexadecimal
    num_of_bits = 4
    return bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)


def knot_hash_to_bits():
    assert to_bin('0') == '0000'
    assert to_bin('1') == '0001'
    assert to_bin('e') == '1110'
    assert to_bin('a0c2017') == '1010000011000010000000010111'

    keys = ['stpzcrnm-'+ str(i) for i in range(128)]

    hashes = [make_hash(k) for k in keys]

    bits = []
    for hash in hashes:
        bit = ''
        for c in hash:
            bit += to_bin(c)
        bits.append(bit)
    return bits


def find_neighbours(arr, coord, group, skip):
    x, y = coord
    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in offsets:
        x2 = x + dx
        y2 = y + dy
        if (x2, y2) in skip or (x2, y2) in group:
            continue
        if 0 <= x2 < 128 and 0 <= y2 < 128:
            if arr[x2][y2]:
                if (x2, y2) not in group:
                    group.add((x2, y2))
                    new, skip = find_neighbours(arr, (x2, y2), group, skip)
                    group = group.union(set(new))
            else:
                skip.add((x2, y2))
    return group, skip


def find_groups(bits):
    arr= [[int(x) for x in row] for row in bits]  # Convert to numeric array

    x, y = 0, 0
    skip = set()
    groups = []
    for x in range(128):
        for y in range(128):
            if (x, y) in skip:  # Skip empty cells visited during neighbour searches
                continue
            if arr[x][y] == 0:  # Ignore all empty cells
                skip.add((x,y))
                continue
            all_seen = set([coord for group in groups for coord in group])
            all_seen = skip.union(all_seen)
            if (x, y) not in all_seen:
                if arr[x][y]:
                    group, skip = find_neighbours(arr, (x, y), set(), skip)
                    groups.append(group)
    return groups


def main():
    tic = time.clock()
    bits = knot_hash_to_bits()
    used = 0
    for bit in bits:
        used += sum(int(b) for b in bit)

    print(f'Part A: {used} - Number of used memory cells')

    groups = find_groups(bits)
    print(f'Part B: {len(groups)} - Number of contiguous memory blocks')

    print('Elapsed: {:0.3f} s'.format(time.clock() - tic))

if __name__ == '__main__':
    main()

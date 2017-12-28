import hashlib
import itertools


def find_suffix(input, zeroes):
    match = '0' * zeroes
    for i in itertools.count(0, 1):
        bytestring = (input + str(i)).encode()
        if hashlib.md5(bytestring).hexdigest()[:zeroes] == match:
            return i


def main():
    assert find_suffix('abcdef', 5) == 609043
    assert find_suffix('pqrstuv', 5) == 1048970

    part_a = find_suffix('iwrupvqb', 5)
    print('Part A: {} - First suffix with 5 leading zeroes'.format(part_a))
    part_b = find_suffix('iwrupvqb', 6)
    print('Part B: {} - First suffix with 6 leading zeroes'.format(part_b))


if __name__ == '__main__':
    main()

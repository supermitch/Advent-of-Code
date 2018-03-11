def expand(a):
    b = ''
    for char in a[::-1]:
        b += '1' if char == '0' else '0'
    return a + '0' + b


def gen_data(input, size):
    curr = input
    while len(curr) < size:
        curr = expand(curr)
    return curr[:size]


def checksum(input):
    out = ''
    for i in range(0, len(input) - 1, 2):
        out += '1' if input[i] == input[i + 1] else '0'
    return out


def odd_check(input):
    curr = checksum(input)
    while len(curr) % 2 == 0:
        curr = checksum(curr)
    return curr


def dragon_checksum(input, size):
    data = gen_data(input, size)
    checksum = odd_check(data)
    return checksum


def main():
    assert expand('111100001010') == '1111000010100101011110000'
    assert gen_data('10000', 20) == '10000011110010000111'

    assert checksum('10000011110010000111') == '0111110101'
    assert odd_check('10000011110010000111') == '01100'
    assert dragon_checksum('10000', 20) == '01100'

    input = '10001110011110000'
    size = 272

    result = dragon_checksum(input, size)
    print('Part A: {} - Checksum for size of {}'.format(result, size))

    size = 35651584
    result = dragon_checksum(input, size)
    print('Part B: {} - Checksum for size of {}'.format(result, size))


if __name__ == '__main__':
    main()

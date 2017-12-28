import hashlib


def part_a(input='abbhdwsy'):
    code = ''
    i = 0
    while True:
        hash = hashlib.md5((input + str(i)).encode()).hexdigest()
        if hash[:5] == '00000':
            code += hash[5]
            print(code)
        if len(code) >= 8:
            return code
        i += 1


def part_b(input='abbhdwsy'):
    code = ['_'] * 8
    i = 0
    while True:
        hash = hashlib.md5((input + str(i)).encode()).hexdigest()
        if hash[:5] == '00000':
            try:
                pos = int(hash[5])
                val = hash[6]
                if code[pos] == '_':
                    code[pos] = val
                else:
                    raise ValueError
            except (IndexError, ValueError):
                pass
            else:
                print(''.join(code))
        if not '_' in code:
            return ''.join(code)
        i += 1


def main():
    result_a = part_a()
    print('Part A: {} - Door password'.format(result_a))

    result_b = part_b()
    print('Part B: {} - Door password'.format(result_b))


if __name__ == '__main__':
    main()

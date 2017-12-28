import collections


def is_abba(chars):
    if chars[0] != chars[1] and chars[0:2] == chars[3:1:-1]:
        return True
    else:
        return False


def in_brackets(ip):
    return in_chars, out_chars


def main():
    with open('input.txt', 'r') as f:
        ips = [line.strip() for line in f]

    assert not is_abba('aaaa')
    assert is_abba('oxxo')

    for ip in ips:
        print(ip)
        in_chars, out_chars = in_brackets(ip)
        print(in_chars, out_chars)
    #most_common = correct(messages, 0)
    #print('Part A: {} - Most-common corrected message'.format(most_common))

    #least_common = correct(messages, -1)
    #print('Part B: {} - Least-common corrected message'.format(least_common))


if __name__ == '__main__':
    main()

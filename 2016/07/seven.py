import re


def is_abba(chars):
    return chars[0] != chars[1] and chars[0:2] == chars[3:1:-1]  # e.g. abba


def contains_abba(string):
    for i in range(len(string) - 3):
        if is_abba(string[i:i+4]):
            return True
    else:
        return False


def break_apart(ip):
    matches = re.findall("([a-z]*)?(\[[a-z]*\])?", ip)
    outside = [m[0] for m in matches if m[0] != '']
    within = [m[1] for m in matches if m[1] != '']
    return outside, within


def is_tls(ip):
    outside, within = break_apart(ip)
    for string in within:
        if contains_abba(string):
            return False

    for string in outside:
        if contains_abba(string):
            return True
    else:
        return False


def is_aba(chars):
    if chars[0] != chars[1] and chars[0] == chars[2]:  # e.g. aba
        return chars[1] + chars[0] + chars[1]  # e.g. bab
    else:
        return ''


def contains_aba(string):
    babs = []
    for i in range(len(string) - 2):
        bab = is_aba(string[i:i + 3])
        if bab:
            babs.append(bab)
    return babs


def is_ssl(ip):
    outside, within = break_apart(ip)

    for string in outside:
        babs = contains_aba(string)
        if not babs:
            continue
        for string in within:
            if any(bab in string for bab in babs):
                return True
    else:
        return False


def main():
    with open('input.txt', 'r') as f:
        ips = [line.strip() for line in f]

    assert not is_abba('aaaa')
    assert is_abba('oxxo')

    assert not contains_abba('ioaxojasdgg')
    assert contains_abba('ioxxoabcj')

    assert break_apart('abba[mnop]qrst') == (['abba', 'qrst'], ['[mnop]'])

    assert not is_tls('abcd[bddb]xyyx')
    assert is_tls('ioxxoj[asdfgh]zxcvbn')

    tls = [ip for ip in ips if is_tls(ip)]
    print('Part A: {} - No. of IPs that support TLS'.format(len(tls)))

    assert not is_ssl('xyx[xyx]xyx')
    assert is_ssl('aba[bab]xyz')
    assert is_ssl('aaa[kek]eke')
    assert is_ssl('zazbz[bzb]cdb')

    ssl = [ip for ip in ips if is_ssl(ip)]
    print('Part B: {} - No. of IPs that support SSL'.format(len(ssl)))


if __name__ == '__main__':
    main()

import string


def has_bads(word):
    return any(bad in word for bad in ['ab', 'cd', 'pq', 'xy'])


def has_vowels(word):
    return sum([char in 'aeiou' for char in word]) >= 3


def has_doubles(word):
    return any(c + c in word for c in string.ascii_lowercase)


def is_nice(word):
    return not has_bads(word) and has_vowels(word) and has_doubles(word)


def has_pairs(word):
    for i in range(len(word) - 1):
        pair = word[i:i + 2]
        if pair in word[i + 2:]:
            return True
    return False


def has_aba(word):
    for i in range(len(word) - 2):
        part = word[i:i + 3]
        if part[0] == part[2]:
            return True
    return False


def is_new_nice(word):
    return has_pairs(word) and has_aba(word)


def main():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f]

    nice = [word for word in lines if is_nice(word)]
    print('Part A: {} - No. of nice words'.format(len(nice)))

    assert has_pairs('xdwduffwgcptfwad')
    assert has_pairs('xyxy')
    assert not has_pairs('ieodomkazucvgmuy')
    assert not has_pairs('aaa')
    assert not has_pairs('aa')
    assert not has_pairs('aabb')

    assert has_aba('xyx')
    assert has_aba('abcdefeghi')
    assert has_aba('aaa')
    assert has_aba('ieodomkazucvgmuy')
    assert not has_aba('uurcxstgmygtbstg')
    assert not has_aba('abc')

    assert is_new_nice('qjhvhtzxzqqjkmpb')
    assert is_new_nice('xxyxx')
    assert not is_new_nice('uurcxstgmygtbstg')
    assert not is_new_nice('ieodomkazucvgmuy')

    new_nice = [word for word in lines if is_new_nice(word)]
    print('Part A: {} - No. of nice words'.format(len(new_nice)))


if __name__ == '__main__':
    main()

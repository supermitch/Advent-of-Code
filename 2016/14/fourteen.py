from collections import OrderedDict
import hashlib
import re



def repeats(string, n):
    """ Find the first char repeated n times in a string. """
    match = re.search(r'(.)\1{' + str(n - 1) + '}', string)
    return match.group(0) if match else ''


def drop_old(i, potential):
    """ Get rid of entries older than 1000 iterations ago. """
    new = OrderedDict()
    for k, v in potential.items():
        if i <= (k + 1000):
            new[k] = v
    return new


def do_hash(input, stretch=1):
    """ Rehash the hash n times. """
    for i in range(stretch):
        input = hashlib.md5(input.encode()).hexdigest()
    return input


def find_match(i, five, potential):
    matches = []
    for idx, (three, hash) in potential.items():
        if three in five:
            matches.append(idx)
    return matches


def generate(salt, stretch=1):
    potential = OrderedDict()
    found = []
    for i in range(50000):
        potential = drop_old(i, potential)

        input = salt + str(i)
        hash = do_hash(input, stretch)

        five = repeats(hash, 5)
        if five:
            matches = find_match(i, five, potential)
        else:
            matches = []
        if matches:
            for idx in matches:
                found.append((idx, potential[idx]))
                del potential[idx]
                if len(found) == 64:
                    return idx

        three = repeats(hash, 3)
        if three:
            potential[i] = (three, hash)


def main():
    assert repeats('abcdddddefg', 5) == 'ddddd'
    assert not repeats('abcdefg', 3)

    assert do_hash('abc18') == '0034e0923cc38887a57bd7b1d4f953df'
    assert repeats(do_hash('abc816'), 5) == 'eeeee'

    assert generate('abc') == 22728

    assert do_hash('abc0', 2017) == 'a107ff634856bb300138cac6568c0f24'

    salt = 'zpqevtbw'
    part_a = generate(salt)
    print('Part A: {} - Index for 64 hashes'.format(part_a))

    part_b = generate(salt, stretch=2017)
    print('Part B: {} - Index for 64 stretched hashes'.format(part_b))


if __name__ == '__main__':
    main()

from collections import defaultdict
import hashlib
import re
import time


def repeats(string, n):
    """ Find the first char repeated n times in a string. """
    pattern = r'(.)\1{2}' if n == 3 else r'(.)\1{4}'
    match = re.search(pattern, string)
    return match.group(0) if match else ''


def do_hash(input, stretch=1):
    """ Rehash the hash n times. """
    for i in range(stretch):
        input = hashlib.md5(input.encode()).hexdigest()
    return input


def generate(salt, stretch=1):
    potential = defaultdict(list)
    found = 0
    i = 0
    while True:
        input = salt + str(i)
        hash = do_hash(input, stretch)

        five = repeats(hash, 5)  # Could be an empty string ''
        matches = potential.pop(five[:3], [])  # Could be an empty list
        for idx in matches:
            if (idx + 1000) >= i:  # Only the next 1000 hashes are matched
                found += 1
                if found == 64:
                    return idx

        three = repeats(hash, 3)
        if three:
            potential[three].append(i)  # Potentials are keyed by 3 chars
        i += 1


def main():
    assert repeats('abcdddddefg', 5) == 'ddddd'
    assert not repeats('abcdefg', 3)

    assert do_hash('abc18') == '0034e0923cc38887a57bd7b1d4f953df'
    assert repeats(do_hash('abc816'), 5) == 'eeeee'

    assert generate('abc') == 22728

    assert do_hash('abc0', 2017) == 'a107ff634856bb300138cac6568c0f24'

    salt = 'zpqevtbw'

    tic = time.time()
    part_a = generate(salt)
    print('Part A: {} - Index for 64 hashes'.format(part_a))
    print('Elapsed: {:0.2f} s'.format(time.time() - tic))

    tic = time.time()
    part_b = generate(salt, stretch=2017)
    print('Part B: {} - Index for 64 stretched hashes'.format(part_b))
    print('Elapsed: {:0.2f} s'.format(time.time() - tic))


if __name__ == '__main__':
    main()

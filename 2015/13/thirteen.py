from itertools import permutations
import pprint


def parse_rules(line):
    parts = line.strip().strip('.').split()
    guest_a, guest_b = parts[0], parts[-1]
    sign = 1 if parts[2] == 'gain' else -1
    value = sign * int(parts[3])
    return (guest_a + ':' + guest_b, value)


def find_happiness(guests, rules):
    total = 0
    for i in range(len(guests)):
        try:
            k = guests[i] + ':' + guests[i + 1]  # Last one will fail
        except IndexError:
            k = guests[i] + ':' + guests[0]  # Loop around
        total += rules[k]
        # And other neighbour
        try:
            k = guests[i] + ':' + guests[i - 1]  # First one will fail
        except IndexError:
            k = guests[i] + ':' + guests[-1]  # Loop around
        total += rules[k]
    return total


def main():
    rules = {}
    with open('input.txt', 'r') as f:
        for l in f:
            key, value = parse_rules(l)
            rules[key] = value

    guests = set([k.split(':')[0] for k in rules])

    max = 0
    for i, perm in enumerate(permutations(guests, len(guests)), start=1):
        value = find_happiness(perm, rules)
        if value > max:
            max = value
        print(i, perm, value)

    part_a = max
    print('Part A: {} - Optimum happiness'.format(part_a))


if __name__ == '__main__':
    main()

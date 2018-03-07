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


def find_max_happiness(guests, rules):
    max_happy = 0
    for perm in permutations(guests, len(guests)):
        value = find_happiness(perm, rules)
        max_happy = max(value, max_happy)
    return max_happy


def main():
    rules = {}
    with open('input.txt', 'r') as f:
        for l in f:
            key, value = parse_rules(l)
            rules[key] = value

    guests = set([k.split(':')[0] for k in rules])

    part_a = find_max_happiness(guests, rules)
    print('Part A: {} - Optimum happiness'.format(part_a))

    # Part B
    for guest in guests:
        rules['Me:' + guest] = 0
        rules[guest + ':Me'] = 0
    guests.add('Me')
    part_b = find_max_happiness(guests, rules)
    print('Part B: {} - Optimum happiness inc. me'.format(part_b))


if __name__ == '__main__':
    main()

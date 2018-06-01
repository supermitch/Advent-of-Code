def parse_line(line):
    p = line.replace(':', '').replace(',', '').split()
    assert len(p) == 8
    return {p[2]: int(p[3]), p[4]: int(p[5]), p[6]: int(p[7])}


def find_aunt(aunts, facts, use_ranges=False):
    for i, aunt in enumerate(aunts, start=1):
        checks = []
        for k, v in facts.items():
            try:
                if use_ranges:
                    if k in ('cats', 'trees'):
                        checks.append(aunt[k] > v)
                    elif k in ('pomeranians', 'goldfish'):
                        checks.append(aunt[k] < v)
                    else:
                        checks.append(aunt[k] == v)
                else:
                    checks.append(aunt[k] == v)
            except KeyError:
                continue
        if all(checks):
            return i


def main():
    with open('input.txt', 'r') as f:
        aunts = [parse_line(line.strip()) for line in f]

    facts = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
    }

    aunt = find_aunt(aunts, facts)
    print('Part A: {} - Aunt who gave the gift'.format(aunt))
    aunt = find_aunt(aunts, facts, use_ranges=True)
    print('Part B: {} - Aunt who actually gave the gift'.format(aunt))


if __name__ == '__main__':
    main()

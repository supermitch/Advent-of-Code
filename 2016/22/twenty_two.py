from itertools import groupby
import re


class Disk:
    def __init__(self, x, y, total, used):
        self.x = x
        self.y = y
        self.total = total
        self.used = used
        self.avail = total - used

    def __repr__(self):
        return 'Disk({}, {}, {}/{}: {})'.format(self.x, self.y, self.used, self.total, self.avail)


def parse(line):
    match = re.match(r'^.*\-x([0-9]+)\-y([0-9]+) +([0-9]+)T +([0-9]+)T.*$', line)
    if match:
        return Disk(*[int(x) for x in match.groups()])


def group_by(data, attribute):
    keyfunc = lambda x: getattr(x, attribute)
    sorted_by = sorted(data, key=keyfunc)
    return {k: list(g) for k, g in groupby(sorted_by, keyfunc)}


def main():
    with open('input.txt', 'r') as f:
        data = [parse(l.strip()) for l in f if 'node' in l]

    use_groups = group_by(data, 'used')
    avail_groups = group_by(data, 'avail')

    pairs_count = 0
    for used in use_groups.keys():
        if used == 0:  # Skip this one
            continue
        for avail in avail_groups.keys():
            if used <= avail:
                pairs_count += len(use_groups[used]) * len(avail_groups[avail])
    print('Part A: {} - Number of available pairs'.format(pairs_count))


if __name__ == '__main__':
    main()

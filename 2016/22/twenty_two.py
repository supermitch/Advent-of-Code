#!/usr/bin/env python
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
        return 'Disk({}-{}={})'.format(self.total, self.used, self.avail)

def parse(line):
    match = re.match(r'.*-x([0-9]+)\-y([0-9]+) +([0-9]+)T +([0-9]+).*', line)
    if match:
        return Disk(*[int(x) for x in match.groups()])


def group_by(data, attribute):
    def keyfunc(x):
        return getattr(x, attribute)
    sorted_by = sorted(data, key=keyfunc)
    return {k: list(g) for k, g in groupby(sorted_by, keyfunc)}


def main():
    with open('input.txt', 'r') as f:
        data = [parse(l.strip()) for l in f if 'node' in l]

    used_groups = group_by(data, 'used')
    avail_groups = group_by(data, 'avail')

    pairs_count = 0
    for used in used_groups.keys():
        if used == 0:  # Skip this one
            continue
        for avail in avail_groups.keys():
            if used <= avail:
                pairs_count += len(used_groups[used]) * len(avail_groups[avail])
    print('Part A: {} - Number of available pairs'.format(pairs_count))

    from pprint import pprint
    grid = {}
    for disk in data:
        grid[(disk.x, disk.y)] = disk

    for y in range(30):
        print(''.join(str(grid[(x,y)]) for x in range(34)))

    grid = [[]]

    for disk in data:
        grid[disc.x][disc.y] = disk


if __name__ == '__main__':
    main()

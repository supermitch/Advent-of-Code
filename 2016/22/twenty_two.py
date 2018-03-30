from pprint import pprint
import re


class Disk:
    def __init__(self, x, y, total, used):
        self.x = x
        self.y = y
        self.total = total
        self.used = used
        self.avail = total - used

    def __repr__(self):
        return 'Disk({}, {}, {}/{})'.format(self.x, self.y, self.used, self.total)


def parse(line):
    match = re.match(r'^.*\-x([0-9]+)\-y([0-9]+) +([0-9]+)T +([0-9]+)T.*$', line)
    if match:
        return Disk(*[int(x) for x in match.groups()])


def main():
    with open('input.txt', 'r') as f:
        data = [parse(l.strip()) for l in f if 'node' in l]

    sorted_by_avail = sorted(data, key=lambda x: x.avail, reverse=True)
    print('Avail:')
    pprint(sorted_by_avail)

    sorted_by_used = sorted(data, key=lambda x: x.used)
    print('Used:')
    pprint(sorted_by_used)


if __name__ == '__main__':
    main()

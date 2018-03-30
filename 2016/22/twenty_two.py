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
        data = [parse(l.strip()) for l in f]
    print(data)


if __name__ == '__main__':
    main()

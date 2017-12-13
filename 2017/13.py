class Scanner:
    def __init__(self, range):
        self.range = range
        self.pos = 0
        self.dir = +1

    def update(self):
        self.pos += self.dir
        if self.pos == self.range - 1 or self.pos == 0:
            self.dir *= -1

    def __repr__(self):
        return '{} of {}'.format(self.pos, self.range)

    def reset(self):
        self.pos = 0
        self.dir = +1


def reset(scanners):
    for s in scanners.values():
        s.reset()


def update(scanners):
    for s in scanners.values():
        s.update()


def main():
    data = []
    with open('13.input', 'r') as f:
        for line in f:
            x, y = line.strip().split(': ')
            data.append((int(x), int(y)))  # Pos, range

    scanners = {d[0]: Scanner(d[1]) for d in data}

    end = max(scanners.keys())

    for delay in range(20000):
        reset(scanners)
        damage = 0
        caught = False

        for _ in range(delay):
            update(scanners)

        x = 0
        while x <= end:
            if x in scanners:
                s = scanners[x]
                if s.pos == 0:  # contact
                    damage += x * s.range
                    caught = True
            update(scanners)
            x += 1
        if not caught:
            print('Found delay of {}'.format(i))
            break


if __name__ == '__main__':
    main()

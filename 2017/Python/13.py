class Scanner:
    def __init__(self, range):
        self.range = range
        self.len = self.range * 2 - 2

    def calc_pos(self, time):
        return time % self.len


def main():
    data = []
    with open('13.input', 'r') as f:
        for line in f:
            x, y = line.strip().split(': ')
            data.append((int(x), int(y)))  # Pos, range

    scanners = {d[0]: Scanner(d[1]) for d in data}

    end = max(scanners.keys())

    delay = 0
    while True:
        damage = 0
        caught = False
        x = 0
        while x <= end:
            if x in scanners:
                s = scanners[x]
                if s.calc_pos(x + delay) == 0:  # contact
                    damage += x * s.range
                    caught = True
                    break
            x += 1
        if not caught:
            print(f'Found delay of {delay} ps')
            break
        delay += 1


if __name__ == '__main__':
    main()

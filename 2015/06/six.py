from collections import defaultdict


def parse(line):
    parts = line.strip().split()
    br = tuple([int(x) for x in parts[-1].split(',')])
    if parts[0] == 'turn':
        action = parts[1]
        ul = tuple([int(x) for x in parts[2].split(',')])
    else:
        action = 'toggle'
        ul = tuple([int(x) for x in parts[1].split(',')])
    return (action, ul, br)


def part_a(actions):
    arr = defaultdict(int)
    for act, ul, br in actions:
        for x in range(ul[0], br[0] + 1):
            for y in range(ul[1], br[1] + 1):
                if act == 'toggle':
                    arr[(x, y)] = 0 if arr[(x, y)] == 1 else 1
                else:
                    arr[(x, y)] = 0 if act == 'off' else 1

    return sum(cell for cell in arr.values())


def part_b(actions):
    arr = defaultdict(int)
    for act, ul, br in actions:
        for x in range(ul[0], br[0] + 1):
            for y in range(ul[1], br[1] + 1):
                if act == 'off':
                    arr[(x, y)] = max(0, arr[(x, y)] - 1)
                else:
                    arr[(x, y)] += 1 if act == 'on' else 2

    return sum(cell for cell in arr.values())


def main():
    with open('input.txt', 'r') as f:
        actions = [parse(line) for line in f]

    lit = part_a(actions)
    print('Part A: {} - No. of lit lights'.format(lit))

    brightness = part_b(actions)
    print('Part B: {} - Total brightness of dimmable lights'.format(brightness))


if __name__ == '__main__':
    main()

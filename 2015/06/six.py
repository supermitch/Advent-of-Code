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


def main():
    pass
    with open('input.txt', 'r') as f:
        actions = [parse(line) for line in f]

    arr = defaultdict(int)

    for act, ul, br in actions:

        x_range = range(ul[0], br[0] + 1)
        y_range = range(ul[1], br[1] + 1)

        for x in x_range:
            for y in y_range:
                if act == 'on':
                    arr[(x, y)] = 1
                elif act == 'off':
                    arr[(x, y)] = 0
                else:
                    arr[(x, y)] = 0 if arr[(x, y)] == 1 else 1

    total = sum(cell for cell in arr.values())
    print('Part A: {} - No. of lit lights'.format(total))

    arr = defaultdict(int)
    for act, ul, br in actions:

        x_range = range(ul[0], br[0] + 1)
        y_range = range(ul[1], br[1] + 1)

        for x in x_range:
            for y in y_range:
                if act == 'on':
                    arr[(x, y)] += 1
                elif act == 'off':
                    arr[(x, y)] = max(0, arr[(x, y)] - 1)
                else:
                    arr[(x, y)] += 2

    total = sum(cell for cell in arr.values())
    print('Part B: {} - Total brightness of dimmable lights'.format(total))


if __name__ == '__main__':
    main()

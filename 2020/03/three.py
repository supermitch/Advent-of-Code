import operator
import functools


def main():
    grid = {}
    with open('input.txt', 'r') as f:
        for y, line in enumerate(f):
            grid_width = len(line.strip())
            for x, c in enumerate(line.strip()):
                grid[(x, y)] = c

    deltas = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    total = []
    for delta in deltas:
        x, y = 0, 0
        trees = 0
        while True:
            x, y = x + delta[0], y + delta[1]
            x = x % grid_width  # Grid repeats in x axis
            try:
                trees += grid[(x, y)] == '#'
            except KeyError:
                break
        total.append(trees)

    mult = functools.reduce(operator.mul, total, 1)
    print(f'Part A: {total[1]} - Tree count')
    print(f'Part B: {mult} - Tree counts, multiplied')


if __name__ == '__main__':
    main()

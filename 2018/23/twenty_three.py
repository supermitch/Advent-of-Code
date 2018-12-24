import re

def read_input():
    data = []
    with open('input.txt') as f:
        for l in f:
            data.append([int(x) for x in re.sub(r'[^0-9-]', ' ', l).split()])
    return data

def in_range(strongest, other):
    x, y, z, r = strongest
    a, b, c, _ = other
    return abs(x - a) + abs(y - b) + abs(z - c) <= r

def range_finder(bots):
    pass


def main():
    data = read_input()
    ordered = sorted(data, key=lambda x:x[3])
    strongest = ordered[-1]

    count = 0
    for other in ordered:  # Includes strongest
        count += in_range(strongest, other)

    print('in range:', count)

if __name__ == '__main__':
    main()

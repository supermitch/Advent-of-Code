import re


def main():
    data = []
    with open('input.txt', 'r') as f:
        for line in f:
            m = re.match(r'(\d+)-(\d+) (\w+): (\w+)$', line)
            data.append(m.groups())

    part_a = 0
    part_b = 0
    for lo, hi, c, pwd in data:
        if int(lo) <= sum(x == c for x in pwd) <= int(hi):
            part_a += 1
        if (pwd[int(lo) - 1] == c) ^ (pwd[int(hi) - 1] == c):
            part_b += 1
    print(f'Part A: {part_a} - Valid passwords')
    print(f'Part B: {part_b} - Valid passwords')


if __name__ == '__main__':
    main()

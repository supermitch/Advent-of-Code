import re


def main():
    data = []
    with open('input.txt', 'r') as f:
        for line in f:
            m = re.match(r'(\d+)-(\d+) (\w+): (\w+)$', line)
            data.append((int(m[1]), int(m[2]), m[3], m[4]))

    part_a = 0
    part_b = 0
    for lo, hi, c, pwd in data:
        part_a += lo <= pwd.count(c) <= hi
        part_b += (pwd[lo - 1] == c) ^ (pwd[hi - 1] == c)  # XOR
    print(f'Part A: {part_a} - Valid passwords')
    print(f'Part B: {part_b} - Valid passwords')


if __name__ == '__main__':
    main()

from itertools import permutations


def main():
    with open('input.txt', 'r') as f:
        data = [int(x.strip()) for x in f]

    for a, b in permutations(data, 2):
        if a + b == 2020:
            break
    print(f'Part A: {a * b} - 2 entries multiplied')

    for a, b, c in permutations(data, 3):
        if a + b + c == 2020:
            break
    print(f'Part B: {a * b * c} - 3 entries multiplied')


if __name__ == '__main__':
    main()

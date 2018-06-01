from itertools import combinations


def main():
    with open('input.txt', 'r') as f:
        containers = [int(l.strip()) for l in f]

    number = 0
    min_container_count = 999
    for count in range(1, len(containers)):
        for comb in combinations(containers, count):
            if sum(comb) == 150:
                number += 1
                if len(comb) <= min_container_count:
                    min_container_count = len(comb)
    print('Part A: {} - Number of container combinations totalling 150 L'.format(number))

    min_number = 0
    for comb in combinations(containers, min_container_count):
        if sum(comb) == 150:
            min_number += 1
    print('Part B: {} - Number of combinations to 150 L using minimum count'.format(min_number))

if __name__ == '__main__':
    main()

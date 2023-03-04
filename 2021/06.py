with open('06_input.txt') as f:
    fishes = [int(x) for x in f.readline().strip().split(',')]

test = [3, 4, 3, 1, 2]


def calc_spawn(days, fishes):
    for _ in range(days):
        add = 0
        for i in range(len(fishes)):
            val = fishes[i] - 1
            if val == -1:
                add += 1
                val = 6
            fishes[i] = val
        fishes.extend([8] * add)
    return len(fishes)


def count_fish(fishes):
    counts = {}
    for i in range(9):
        counts[i] = sum(1 for x in fishes if x == i)
    return counts


print(count_fish(fishes))

print(f'Test: {calc_spawn(18, test)} lanternfish after 18 days')
# print(f'Part A: {calc_spawn(80, fishes)} lanternfish after 80 days')

with open('2021/01_input.txt', 'r') as f:
    data = [int(x.strip()) for x in f.readlines()]

part_1 = 0
for i in range(1, len(data)):
    if data[i] > data[i - 1]:
        part_1 += 1
print(f'Part 1: Incremented {part_1} times')

part_2 = 0
for i in range(0, len(data)):
    a_sum = sum(data[i:i + 3])
    try:
        b_sum = sum(data[i + 1:i + 4])
    except IndexError:
        break
    if b_sum > a_sum:
        part_2 += 1
print(f'Part 2: Incremented {part_2} times')

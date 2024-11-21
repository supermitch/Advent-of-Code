with open('01_input.txt') as f:
    lines = [x.strip() for x in f]

nums = []
for row in lines:
    nums.append([x for x in row if 48 <= ord(x) <= 57])

total = sum(int(x[0] + x[-1]) for x in nums)
print(f'Part a: {total}')

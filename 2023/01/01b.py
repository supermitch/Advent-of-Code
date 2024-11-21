with open('01_input.txt') as f:
    lines = [x.strip() for x in f]

words = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

rows = []
for line in lines:
    nums = []
    while line:
        for word, val in words.items():
            if line.startswith(word):
                nums.append(str(val))
                break
        else:  # Did not start with a word
            if 49 <= ord(line[0]) <= 57:  # Starts with a digit
                nums.append(line[0])
        line = line[1:]  # Pop first char
    rows.append(nums)

total = sum(int(x[0] + x[-1]) for x in rows)
print(f'Part b: {total}')

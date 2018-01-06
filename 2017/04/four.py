with open('input.txt', 'r') as f:

    a, b = 0, 0
    for line in f:
        words = line.strip().split()

        if len(set(words)) == len(words):
            a += 1

        ordered = [''.join(sorted(x)) for x in words]
        if len(set(ordered)) == len(words):
            b += 1

    print('Part A: {}'.format(a))
    print('Part B: {}'.format(b))

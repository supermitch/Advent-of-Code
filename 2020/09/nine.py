def calc(data):
    i = 0
    acc = 0
    seen = set()
    while True:
        if i in seen:
            return 'loop', acc
        else:
            seen.add(i)
        op, val = data[i]
        if op == 'acc':
            acc += val
            i += 1
        elif op == 'nop':
            i += 1
        elif op == 'jmp':
            i += val
        if i == len(data):  # Beyond last op
            return 'exit', acc


def main():
    data = []
    with open('input.txt') as f:
        for line in f:
            parts = line.strip().split()
            data.append((parts[0], int(parts[1])))

    _, part_a = calc(data)

    for i in range(len(data)):
        copy = data[:]
        op, val = copy[i]
        if op == 'nop':
            copy[i] = 'jmp', val
        elif op == 'jmp':
            copy[i] = 'nop', val

        code, val = calc(copy)
        if code == 'exit':
            part_b = val
            break

    print(f'Part A: {part_a} - Acc before infinite loop')
    print(f'Part B: {part_b} - Acc before routine exits')


if __name__ == "__main__":
    main()

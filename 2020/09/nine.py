import sys


def main():
    data = []
    with open('input.txt') as f:
        for line in f:
            parts = line.strip().split()
            data.append((parts[0], int(parts[1])))

    i = 0
    acc = 0
    seen = set()
    while True:
        if i in seen:
            part_a = acc
            break
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

    found = False
    for idx in range(len(data)):
        copy = data[:]
        op, val = copy[idx]
        if op == 'nop':
            copy[idx] = 'jmp', val
        elif op == 'jmp':
            copy[idx] = 'nop', val

        i = 0
        acc = 0
        seen = set()
        while True:
            if i in seen:  # Infinite loop re-starts
                break
            else:
                seen.add(i)
            op, val = copy[i]
            if op == 'acc':
                acc += val
                i += 1
            elif op == 'nop':
                i += 1
            elif op == 'jmp':
                i += val
            if i == len(copy):
                part_b = acc
                found = True
                break
        if found:
            break

    print(f'Part A: {part_a} - Acc before infinite loop')
    print(f'Part B: {part_b} - Acc before routine terminates')

if __name__ == "__main__":
    main()

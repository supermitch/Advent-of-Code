def perform_dance(p, data):
    for m, d in data:
        if m == 'x':
            x, y = d
            p[x], p[y] = p[y], p[x]
        elif m == 'p':
            n, m = d
            x = p.index(n)
            y = p.index(m)
            p[x], p[y] = p[y], p[x]
        elif m == 's':
            d = d % 16
            p = p[16 - d:] + p[:16 - d]
    return p


def main():
    with open('16.input', 'r') as f:
        data = []
        moves = f.readline().strip().split(',')
        for move in moves:
            type = move[0]
            if type == 'x':
                pos = [int(x) for x in move[1:].split('/')]
            elif type == 'p':
                pos = [x for x in move[1:].split('/')]
            else:
                pos = int(move[1:])
            data.append((type, pos))

    p = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    part_a = ''.join(perform_dance(p[:], data))
    print('Part A {} - Program order after one dance'.format(part_a))

    seen = []
    for i in range(0, 100):
        p = perform_dance(p, data)
        if ''.join(p) not in seen:
            seen.append(''.join(p))

    idx = 1000000000 % len(seen)
    part_b = ''.join(seen[idx - 1])
    print('Part B {} - Program order after 1B dances'.format(part_b))


if __name__ == '__main__':
    main()

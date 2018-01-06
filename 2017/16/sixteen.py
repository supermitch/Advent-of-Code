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


def cat(p):
    return ''.join(p)


def find_repeats(p, moves):
    seen = []
    while True:
        p = perform_dance(p, moves)
        if cat(p) not in seen:
            seen.append(cat(p))
        else:
            return seen


def main():
    with open('input.txt', 'r') as f:
        moves = []
        for move in f.readline().strip().split(','):
            type = move[0]
            if type == 'x':
                pos = [int(x) for x in move[1:].split('/')]
            elif type == 'p':
                pos = move[1:].split('/')
            else:
                pos = int(move[1:])
            moves.append((type, pos))

    p = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

    part_a = cat(perform_dance(p[:], moves))
    print('Part A {} - Order after 1 dance'.format(part_a))

    seen = find_repeats(p, moves)
    idx = int(1e10) % len(seen) - 1
    part_b = cat(seen[idx])
    print('Part B {} - Order after 1e10 dances'.format(part_b))


if __name__ == '__main__':
    main()

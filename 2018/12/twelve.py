#!/usr/bin/env python

def read_input():
    with open('input.txt') as f:
        pots = f.readline().strip().split(':')[1].strip()
        f.readline()
        rules = {}
        for line in f:
            k, v = line.strip().split(' => ')
            rules[k] = v
        return pots, rules


def main():
    print('\ntwelve')
    init, rules = read_input()

    left = 5
    pots = ['.'] * left + [x for x in init] + ['.'] * 20
    g = 0
    gens = 102
    while g < gens:
        print(g, ''.join(pots))
        print(pots.index('#'))
        nxt = ['.' for x in pots]
        for i in range(0, len(pots) - 4):
            span = ''.join(pots[i:i + 5])
            if span in rules:
                nxt[i+2] = rules.get(span, '.')
            else:
                nxt[i+2] = '.'
        g += 1
        pots = nxt[:]
        if any(x == '#' for x in pots[:5]):
            pots = ['.'] * 5 + pots
            left += 5
        if any(x == '#' for x in pots[-5:]):
            pots = pots + ['.'] * 5
        if g == 20:
            break
        if g == 102:
            final = pots[:]
            break

    # print(final.index('#') - 5)
    delta = 50000000000 - 102

    total = [i - left if x == '#' else 0 for i, x in enumerate(pots[left:], start=left)]
    sub = [i - left for i, x in enumerate(pots[:left + 1]) if x == '#']
    print(total, sub)
    print(sum(total) + sum(sub))

    # 6906 too low
    # 7090

if __name__ == '__main__':
    main()

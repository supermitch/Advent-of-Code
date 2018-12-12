#!/usr/bin/env python

rules = {
    '#.##.': '.',
    '#.#..': '.',
    '###.#': '.',
    '..#.#': '.',
    '....#': '.',
    '.####': '.',
    '##.##': '#',
    '###..': '#',
    '.###.': '#',
    '...#.': '.',
    '.....': '.',
    '##..#': '.',
    '.#.#.': '#',
    '.#.##': '#',
    '##.#.': '.',
    '##...': '.',
    '#####': '#',
    '#...#': '.',
    '..##.': '.',
    '..###': '.',
    '.#...': '#',
    '.##.#': '.',
    '#....': '.',
    '.#..#': '.',
    '.##..': '#',
    '...##': '#',
    '#.###': '.',
    '#..#.': '.',
    '..#..': '#',
    '#.#.#': '#',
    '####.': '#',
    '#..##': '.',
}

ruless = {
'...##': '#',
'..#..': '#',
'.#...': '#',
'.#.#.': '#',
'.#.##': '#',
'.##..': '#',
'.####': '#',
'#.#.#': '#',
'#.###': '#',
'##.#.': '#',
'##.##': '#',
'###..': '#',
'###.#': '#',
'####.': '#',

}
def main():
    print('\ntwelve')
    init = '..#..####.##.####...#....#######..#.#..#..#.#.#####.######..#.#.#.#..##.###.#....####.#.#....#.#####'
    # init = '#..#.#..##......###...###'
    add = 25
    pots = ['.'] * add + [x for x in init] + ['.'] * add
    g = 0
    gens = 50000000000
    while g < gens:
        if not (g % 100):
            print(g)
        nxt = ['.' for x in pots]
        for i in range(0, len(pots) - 4):
            span = ''.join(pots[i:i + 5])
            if span in rules:
                nxt[i+2] = rules.get(span, '.')
            else:
                nxt[i+2] = '.'
        g += 1
        pots = nxt[:]
        if any(x == '#' for x in pots[:5]) or any(x == '#' for x in pots[-5:]):
            pots = ['.'] * 5 + pots
            pots = pots + ['.'] * 5
            add += 5

    print(''.join(pots))
    total = [i - add if x == '#' else 0 for i, x in enumerate(pots[add:], start=add)]
    sub = [i - add for i, x in enumerate(pots[:add + 1]) if x == '#']
    print(total, sum(total))
    print(sub, sum(sub))
    print(sum(total) + sum(sub))
    # 758 wrong

if __name__ == '__main__':
    main()

#!/usr/bin/env python


def parse(l):
    return [x for x in l.split(')')]


def main():
    with open('input.txt') as f:
        data = [parse(l.strip()) for l in f]

    graph = {}
    for a, b in data:
        graph[b] = a

    total = 0
    for k in graph.keys():
        path = [k]
        nxt = k
        while True:
            nxt = graph[nxt]
            path.append(nxt)
            if nxt == 'COM':
                break
        total += len(path) - 1
        if path[0] == 'YOU':
            you = path.copy()
        elif path[0] == 'SAN':
            san = path.copy()
    print(f'Part A: {total} - Total no. of direct & indirect orbits')

    count = 0
    for o in you:
        count += 1
        if o in san:
            break
    steps = 0
    for x in san:
        steps += 1
        if x == o:
            break
    transers = count + steps - 4
    print(f'Part B: {transers} - Minimum orbital transfers to reach SAN')


if __name__ == '__main__':
    main()

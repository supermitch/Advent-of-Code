#!/usr/bin/env python


def main():
    with open('input.txt') as f:
        data = [l.strip().split(')') for l in f]

    orbits = {b: a for a, b in data}

    total = 0
    for k in orbits.keys():
        path = [k]
        while True:
            k = orbits[k]
            if k == 'COM':  # Don't include COM
                break
            path.append(k)
        total += len(path)
        if path[0] == 'YOU':
            you = path.copy()
        elif path[0] == 'SAN':
            san = path.copy()
    print(f'Part A: {total} - Total no. of direct & indirect orbits')

    for obj in you:
        if obj in san:
            break

    transfers = you.index(obj) + san.index(obj) - 2  # Ignore YOU & SAN
    print(f'Part B: {transfers} - Minimum orbital transfers to reach SAN')


if __name__ == '__main__':
    main()

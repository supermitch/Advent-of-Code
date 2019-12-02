#!/usr/bin/env python


def main():
    with open('input.txt') as f:
        data = [int(l) for l in f]

    fuels = [x // 3 - 2 for x in data]
    grand_total = 0
    for fuel in fuels:
        total = fuel
        while True:
            fuel = fuel // 3 - 2
            if fuel <= 0:
                break
            total += fuel
        grand_total += total

    print(f'Part A: {sum(fuels)} - Sum of fuel requirements')
    print(f'Part B: {grand_total} - Fuel requirements inc. fuel mass')


if __name__ == '__main__':
    main()

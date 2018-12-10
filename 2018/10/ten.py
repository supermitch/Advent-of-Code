#!/usr/bin/env python
"""
Day 10: The Stars Align
A: Find a hidden message that appears when a set of moving points align.
B: Determine at what time the hidden message appears
"""
import re


def parse(l):
    return [int(x) for x in re.sub('[^0-9-]', ' ', l).split()]


class Point:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def update(self):
        self.x += self.vx
        self.y += self.vy


def draw(points, max_x, min_x):
    min_y = min(p.y for p in points)
    max_y = max(p.y for p in points)
    for j in range(min_y, max_y + 1):
        line = ''
        for i in range(min_x, max_x + 1):
            for p in points:
                if p.x == i and p.y == j:
                    line += '█'
                    break
            else:  # Not points here
                line += ' '
        print(line)


def main():
    with open('input.txt') as f:
        data = [parse(l) for l in f]
    points = [Point(*d) for d in data]

    converged = False
    t = 0
    while True:
        t += 1
        [p.update() for p in points]

        max_x = max(p.x for p in points)
        min_x = min(p.x for p in points)

        if (max_x - min_x) <= 65:  # Start drawing when points get close
            print('Time: {} s\n'.format(t))
            draw(points, max_x, min_x)
            print('\n')
            converged = True
        else:
            if converged:  # Quit when points separate again
                break

    print('Part A: BHPJGLPE - The navigation message')
    print('Part B: 10831 s - The time at which the message appears')


if __name__ == '__main__':
    main()

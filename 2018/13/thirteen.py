#!/usr/bin/env python
"""
Day 13: Mine Cart Madness
A. Find the coordinates of the first cart collision
B. Find the location of the last surviving cart
"""
def load_map():
    carts = []
    grid = {}
    with open('input.txt') as f:
        for y, line in enumerate(f):
            for x, char in enumerate(line[:-1]):
                if char in ('/|+-\\'):
                    grid[(y, x)] = char
                elif char in 'v^':
                    carts.append(Cart(y, x, char))
                    grid[(y, x)] = '|'
                elif char in '<>':
                    carts.append(Cart(y, x, char))
                    grid[(y, x)] = '-'
    return grid, carts


class Cart:
    def __init__(self, y, x, char):
        self.y = y
        self.x = x
        self.dir = char
        self.move = {
            '>': (0, 1),
            '<': (0, -1),
            'v': (1, 0),
            '^': (-1, 0),
        }[char]
        self.turns = 0
        self.dead = False

    def update(self, grid):
        path = grid[(self.y, self.x)]
        if self.dir == '>':
            if path == '\\':
                self.dir = 'v'
                self.y += 1
            elif path == '-':
                self.x += 1
            elif path == '/':
                self.dir = '^'
                self.y -= 1
            elif path == '+':
                if self.turns == 0:
                    self.dir = '^'
                    self.y -= 1
                elif self.turns == 1:
                    self.x += 1
                else:
                    self.dir = 'v'
                    self.y += 1
                self.turns += 1
                self.turns = self.turns % 3
        elif self.dir == '<':
            if path == '\\':
                self.dir = '^'
                self.y -= 1
            elif path == '-':
                self.x -= 1
            elif path == '/':
                self.dir = 'v'
                self.y += 1
            elif path == '+':
                if self.turns == 0:
                    self.dir = 'v'
                    self.y += 1
                elif self.turns == 1:
                    self.x -= 1
                else:
                    self.dir = '^'
                    self.y -= 1
                self.turns += 1
                self.turns = self.turns % 3
        elif self.dir == '^':
            if path == '\\':
                self.dir = '<'
                self.x -= 1
            elif path == '|':
                self.y -= 1
            elif path == '/':
                self.dir = '>'
                self.x += 1
            elif path == '+':
                if self.turns == 0:
                    self.dir = '<'
                    self.x -= 1
                elif self.turns == 1:
                    self.y -= 1
                else:
                    self.dir = '>'
                    self.x += 1
                self.turns += 1
                self.turns = self.turns % 3
        elif self.dir == 'v':
            if path == '\\':
                self.dir = '>'
                self.x += 1
            elif path == '|':
                self.y += 1
            elif path == '/':
                self.dir = '<'
                self.x -= 1
            elif path == '+':
                if self.turns == 0:
                    self.dir = '>'
                    self.x += 1
                elif self.turns == 1:
                    self.y += 1
                else:
                    self.dir = '<'
                    self.x -= 1
                self.turns += 1
                self.turns = self.turns % 3


def main():
    grid, carts = load_map()
    part_a = False
    while True:
        carts = sorted(carts, key=lambda c: c.y)  # Second sort by y-coord
        carts = sorted(carts, key=lambda c: c.x)  # First sort by x-coord
        carts = [c for c in carts if not c.dead]
        if len(carts) == 1:
            survivor = carts[0]
            print('Part B: {},{} - Coord of sole survivor'.format(survivor.x, survivor.y))
            return
        for i in range(len(carts)):
            cart = carts[i]
            cart.update(grid)
            for j in range(len(carts)):
                if i == j:
                    continue
                other = carts[j]
                if other.y == cart.y and other.x == cart.x:  # Collision
                    cart.dead = True
                    other.dead = True
                    if part_a == False:
                        print('Part A: {},{} - Coord of first collision'.format(cart.x, cart.y))
                        part_a = True


if __name__ == '__main__':
    main()

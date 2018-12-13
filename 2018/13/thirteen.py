#!/usr/bin/env python

class Cart:
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
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
        path = grid[(self.x, self.y)]
        if self.dir == '>':
            if path == '\\':
                self.dir = 'v'
                self.x += 1
            elif path == '-':
                self.y += 1
            elif path == '/':
                self.dir = '^'
                self.x -= 1
            elif path == '+':
                if self.turns == 0:
                    self.dir = '^'
                    self.x -= 1
                elif self.turns == 1:
                    self.y += 1
                else:
                    self.dir = 'v'
                    self.x += 1
                self.turns += 1
                self.turns = self.turns % 3
        elif self.dir == '<':
            if path == '\\':
                self.dir = '^'
                self.x -= 1
            elif path == '-':
                self.y -= 1
            elif path == '/':
                self.dir = 'v'
                self.x += 1
            elif path == '+':
                if self.turns == 0:
                    self.dir = 'v'
                    self.x += 1
                elif self.turns == 1:
                    self.y -= 1
                else:
                    self.dir = '^'
                    self.x -= 1
                self.turns += 1
                self.turns = self.turns % 3
        elif self.dir == '^':
            if path == '\\':
                self.dir = '<'
                self.y -= 1
            elif path == '|':
                self.x -= 1
            elif path == '/':
                self.dir = '>'
                self.y += 1
            elif path == '+':
                if self.turns == 0:
                    self.dir = '<'
                    self.y -= 1
                elif self.turns == 1:
                    self.x -= 1
                else:
                    self.dir = '>'
                    self.y += 1
                self.turns += 1
                self.turns = self.turns % 3
        elif self.dir == 'v':
            if path == '\\':
                self.dir = '>'
                self.y += 1
            elif path == '|':
                self.x += 1
            elif path == '/':
                self.dir = '<'
                self.y -= 1
            elif path == '+':
                if self.turns == 0:
                    self.dir = '>'
                    self.y += 1
                elif self.turns == 1:
                    self.x += 1
                else:
                    self.dir = '<'
                    self.y -= 1
                self.turns += 1
                self.turns = self.turns % 3

def draw(grid, carts):
    for x in range(150):
        line = ''
        for y in range(150):
            for cart in carts:
                if cart.dead:
                    continue
                if cart.x == x and cart.y == y:
                    line += cart.dir
                    break
            else:
                if (x, y) in grid:
                    line += grid[(x,y)]
                else:
                    line += ' '
        print(line)

def main():
    carts = []
    with open('input.txt') as f:
        grid = {}
        for x, line in enumerate(f):
            for y, char in enumerate(line[:-1]):
                if char in ('/|+-\\'):
                    grid[(x, y)] = char
                elif char in 'v^':
                    carts.append(Cart(x, y, char))
                    grid[(x, y)] = '|'
                elif char in '<>':
                    carts.append(Cart(x, y, char))
                    grid[(x, y)] = '-'

    part_a = False
    while True:
        carts = sorted(carts, key=lambda c: c.x)
        carts = sorted(carts, key=lambda c: c.y)
        carts = [c for c in carts if not c.dead]
        if len(carts) == 1:
            left = carts[0]
            print('Part B: {},{} - Coord of sole survivor'.format(left.y, left.x))
            return
        for i in range(len(carts)):
            cart = carts[i]
            cart.update(grid)
            for j in range(len(carts)):
                if i != j:
                    other = carts[j]
                    if other.x == cart.x and other.y == cart.y:
                        cart.dead = True
                        other.dead = True
                        if part_a == False:
                            print('Part A: {},{} - Coord of first collision'.format(cart.y, cart.x))
                            part_a = True



if __name__ == '__main__':
    main()

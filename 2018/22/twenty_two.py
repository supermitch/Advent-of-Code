def draw(grid, tx, ty, equip=None):
    for y in range(0, ty + 1):  # y downward
        line = ''
        for x in range(0, tx + 51):  # x to the right
            if (x, y) == (0, 0):
                line += 'M'
            elif (x, y) == (tx, ty):
                line += 'T'
            else:
                if equip == 't':
                    if grid[(x, y)] in ('.', '|'):
                        line += ' '
                    else:
                        line += '█'
                elif equip == 'c':
                    if grid[(x, y)] in ('.', '='):
                        line += ' '
                    else:
                        line += '█'
                elif equip == 'n':
                    if grid[(x, y)] in ('=', '|'):
                        line += ' '
                    else:
                        line += '█'
                else:
                    line += grid[(x, y)]
        print(line)

def add(grid, tx, ty):
    total = 0
    for x in range(0, tx + 1):
        for y in range(0, ty + 1):
            total += {'.': 0, '=': 1, '|': 2}[grid[(x, y)]]
    return total

def main():
    depth = 11739
    tx, ty = 11, 718  # x to right, y downward

    # depth = 510
    # tx, ty = 10, 10

    grid = {}
    erosion = {}
    for x in range(0, tx + 51):
        for y in range(0, ty + 1):
            coord = x, y
            if (x, y) == (0, 0) or (x, y) == (tx, ty):
                idx = 0
            elif y == 0:
                idx = x * 16807
            elif x == 0:
                idx = y * 48271
            else:
                idx = erosion[(x - 1, y)] * erosion[(x, y - 1)]

            erosion[(x, y)] = (idx + depth) % 20183
            if erosion[(x, y)] % 3 == 0:
                kind = '.'  # rocky
            elif erosion[(x, y)] % 3 == 1:
                kind = '='  # wet
            elif erosion[(x, y)] % 3 == 2:
                kind = '|'  # narrow
            grid[(x, y)] = kind
    total = add(grid, tx, ty)
    print('Part A: {} - Total risk'.format(total))

    # Rocky: climbing gear, 'c', or torch, 't'
    # Wet: climbing gear or none, 'n'
    # narrow: torch or none

    draw(grid, tx, ty, equip='c')

if __name__ == '__main__':
    main()

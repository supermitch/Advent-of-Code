import copy

def adjacent(coord, grid):
    row, col = coord
    trees = 0
    lumber = 0
    deltas = [
        (-1, -1), (-1, 0), (-1, +1),
        (0, -1), (0, +1), (+1, -1), (+1, 0),
        (+1, +1),
    ]
    for dx, dy in deltas:
        nx, ny = row + dx, col + dy
        if (nx, ny) in grid:
            if grid[(nx, ny)] == '|':
                trees += 1
            elif grid[(nx, ny)] == '#':
                lumber += 1
    return trees, lumber


def count_total(grid):
    trees = 0
    lumber = 0
    for row in range(50):
        for col in range(50):
            if grid[(row, col)] =='|':
                trees += 1
            elif grid[(row, col)] =='#':
                lumber += 1
    return trees * lumber

def draw(grid):
    for row in range(50):
        line = ''
        for col in range(50):
            line += grid[(row, col)]
        print(line)
    print('')

def stringify(grid):
    line = ''
    for row in range(50):
        for col in range(50):
            line += grid[(row, col)]
    return line

def main():
    grid = dict()
    with open('input.txt') as f:
        for row, l in enumerate(f):
            for col, char in enumerate(l.strip()):
                grid[(row, col)] = char
    t = 0
    known_grid = {}
    seen = set()
    first_repeat = None
    while True:
        t += 1
        new_grid = copy.deepcopy(grid)
        for row in range(50):
            for col in range(50):
                coord = row, col
                trees, lumber = adjacent(coord, grid)
                if grid[coord] == '.':
                    if trees >= 3:
                        new_grid[coord] = '|'
                elif grid[coord] == '|':
                    if lumber >= 3:
                        new_grid[coord] = '#'
                elif grid[coord] == '#':
                    if lumber < 1 or trees < 1:
                        new_grid[coord] = '.'
        grid = copy.deepcopy(new_grid)
        line = stringify(grid)
        if line in known_grid:
            if first_repeat is None:
                first_repeat = t
                first_total = count_total(grid)
            else:
                if count_total(t) == first_total:
                    delta_t = t - first_repeat
                    offset = (1000000000 - first_repeat) % delta_t
                    equiv = first_repeat + offset
                    for line, (t, grid) in known_grid:
                        if t == equiv:
                            print(count_total(grid))
                            return

        else:
            known_grid[line] = (t, grid)



if __name__ == '__main__':
    main()


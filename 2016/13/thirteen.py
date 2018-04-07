from collections import deque


def get_tile(x, y, input):
    z = (x * x) + (3 * x) + (2 * x * y) + (y) + (y * y)
    total = z + input
    binary = format(total, 'b')
    bit_sum = sum(b == '1' for b in binary)
    if not bit_sum % 2:
        return '.'
    else:
        return '#'


def parse_input(map):
    """ Turn our text map into a coordinate list. """
    coords = {}
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char == '.':  # A path
                coords[(x, y)] = '.'
    return coords


def get_options(map, coord):
    """ Find possible movements in four directions. """
    x, y = coord
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # +x, -x, +y, -y
    options = []
    for dx, dy in deltas:
        x2, y2 = x + dx, y + dy
        if (x2, y2) in map:  # Our map *only* contains valid coords
            options.append((x2, y2))
    return options


def extract_path(coord, path):
    """ Extract a human-readable path from a DSF route. """
    route = []
    while coord:
        route.insert(0, coord)
        coord = path[coord]
    return route


def dfs(map, start, goal):
    """ Classic DFS, with early exit on finding a goal. """
    route = []
    path = {start: None}
    seen = set()
    queue = deque([start])
    while queue:
        coord = queue.popleft()
        seen.add(coord)
        options = get_options(map, coord)
        path.update({x: coord for x in options if x not in seen})
        queue.extend([x for x in options if x not in seen and x not in queue])
        if coord == goal:
            break
    return extract_path(goal, path)


def limited_dfs(map, start, n):
    """ Classic DFS, with early exit on finding a goal. """
    route = []
    path = {start: None}
    seen = set()
    queue = deque([start])
    while queue:
        coord = queue.popleft()
        seen.add(coord)
        options = get_options(map, coord)
        path.update({x: coord for x in options if x not in seen})
        queue.extend([x for x in options if x not in seen and x not in queue])

        parents = {v for k, v in path.items()}
        if len(parents) >= n:
            print(len(parents))
            break

    return len(parents)


def main():
    input = 1352

    map = []
    for y in range(100):
        row = ''.join(get_tile(x, y, input) for x in range(100))
        map.append(row)

    coords = parse_input(map)

    start = (1, 1)
    goal = (31, 39)

    path = dfs(coords, start, goal)
    steps = len(path) - 1
    print('Part A: {} - Number of steps to reach {}'.format(steps, goal))

    no_of_positions = limited_dfs(coords, start, 50)
    print('Part B: {} - Unique coords within 50 steps'.format(no_of_positions))


if __name__ == '__main__':
    main()

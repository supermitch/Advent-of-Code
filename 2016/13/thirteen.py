from collections import deque


def get_tile(x, y, input):
    """ Calculate whether a coordinate is a path '.' or a wall '#'. """
    z = (x * x) + (3 * x) + (2 * x * y) + (y) + (y * y) + input
    binary = format(z, 'b')
    bit_sum = sum(b == '1' for b in binary)
    return '#' if bit_sum % 2 else '.'


def convert_string_map_to_coords(map):
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


def depth_dfs(map, start):
    """ DFS, but record tree depth, with no early exit. """
    seen = {}  #{coord: depth} entries
    queue = deque([(start, 0)])  # level is depth of DFS search
    while queue:
        coord, level = queue.popleft()
        seen[coord] = level
        options = get_options(map, coord)
        queue.extend([(x, level + 1) for x in options if x not in seen and x not in queue])
    return seen


def main():
    input = 1352

    map_size = 100  # Abritrary
    map = []
    for y in range(map_size):
        row = ''.join(get_tile(x, y, input) for x in range(map_size))
        map.append(row)
    coords = convert_string_map_to_coords(map)

    start = (1, 1)
    goal = (31, 39)

    path = dfs(coords, start, goal)
    steps = len(path) - 1
    print('Part A: {} - Number of steps to reach {}'.format(steps, goal))

    seen = depth_dfs(coords, start)
    unique_coords = len([x for x, level in seen.items() if level <= 50])
    print('Part B: {} - Unique coords within 50 steps of {}'.format(unique_coords, start))


if __name__ == '__main__':
    main()

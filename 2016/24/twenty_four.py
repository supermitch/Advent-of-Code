from collections import deque
from itertools import permutations, combinations


class Map:
    def __init__(self, map):
        self.map = map  # coordinate dictionary

    def get_coord(self, goal):
        for coord, number in self.map.items():
            if number == goal:
                return coord

    def get_options(self, coord):
        x, y = coord
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # +x, -x, +y, -y
        options = []
        for dx, dy in deltas:
            x2, y2 = x + dx, y + dy
            if (x2, y2) in self.map:  # Our map *only* contains valid coords
                options.append((x2, y2))
        return options

    def extract_path(self, coord, path):
        route = []
        while coord:
            route.insert(0, coord)
            coord = path[coord]
        return route

    def dfs(self, start, goal):
        route = []
        path = {start: None}
        seen = set()
        queue = deque([start])
        while queue:
            coord = queue.popleft()
            seen.add(coord)
            options = self.get_options(coord)
            path.update({x: coord for x in options if x not in seen})
            queue.extend([x for x in options if x not in seen and x not in queue])
            if coord == goal:
                break
        return self.extract_path(goal, path)


def generate_routes(goals, back_to_start=False):
    possible_routes = []
    for p in permutations(goals, len(goals)):
        full_path = [0] + list(p) + ([0] if back_to_start else [])
        possible_routes.append(full_path)  # All routes start at 0
    return possible_routes


def parse_input():
    coords = {}
    with open('input.txt', 'r') as f:
        for y, line in enumerate(f):
            for x, char in enumerate(line.strip()):
                if char == '.':  # A path
                    coords[(x, y)] = '.'
                elif char == '#':  # A wall
                    continue  # *Not* included in dict of coords, aka map
                else:  # An integer goal
                    coords[(x, y)] = int(char)
    return Map(coords)


def generate_edges(map, nodes):
    pairs = {}
    vertices = combinations(nodes, 2)
    for start, goal in vertices:
        start_coord = map.get_coord(start)
        goal_coord = map.get_coord(goal)
        path = map.dfs(start_coord, goal_coord)
        key = tuple(sorted([start, goal]))
        pairs[key] = path
    return pairs


def find_cheapest_route(routes, pairs):
    cheapest_cost = float("inf")
    cheapest_route = None
    for route in routes:
        total_cost = 0
        for i in range(len(route) - 1):
            key = tuple(sorted([route[i], route[i + 1]]))
            edge_path = pairs[key]
            edge_cost = len(edge_path) - 1  # Don't include the start node
            total_cost += edge_cost
        if total_cost < cheapest_cost:
            cheapest_cost = total_cost
            cheapest_route = route
    return cheapest_route, cheapest_cost


def main():
    map = parse_input()

    assert map.get_options((3, 1)) == [(4, 1), (2, 1), (3, 2)]
    assert map.get_coord(5) == (9, 17)

    nodes = range(0, 8)
    pairs = generate_edges(map, nodes)

    goals = range(1, 8)
    routes = generate_routes(goals)
    route, cost = find_cheapest_route(routes, pairs)
    print('Part A: {} - Shortest route through all nodes'.format(cost))

    routes = generate_routes(goals, back_to_start=True)
    route, cost = find_cheapest_route(routes, pairs)
    print('Part B: {} - Shortest route through all nodes & back to start'.format(cost))


if __name__ == '__main__':
    main()

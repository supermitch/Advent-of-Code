from collections import deque
from itertools import permutations, combinations
from pprint import pprint


class Map:
    def __init__(self, map):
        self.map = map  # coordinate dictionary

    def get_coord(self, goal):
        for coord, number in self.map.items():
            if number == goal:
                return coord

    def get_options(self, coord):
        if coord not in self.map:
            raise ValueError('Invalid coordinate!?')
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


def generate_routes(goals):
    possible_routes = []
    for p in permutations(goals, len(goals)):
        possible_routes.append([0] + list(p))  # All routes start at 0
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


def main():
    map = parse_input()

    assert map.get_options((3, 1)) == [(4, 1), (2, 1), (3, 2)]
    assert map.get_coord(5) == (9, 17)

    goals = range(1, 8)
    routes = generate_routes(goals)
    print(routes)

    start = map.get_coord(0)
    targets = [map.get_coord(x) for x in goals]

    pairs = {}
    vertices = combinations(range(0, 8), 2)
    for start, goal in vertices:
        start_coord = map.get_coord(start)
        goal_coord = map.get_coord(goal)
        path = map.dfs(start_coord, goal_coord)
        print('Start: {}: {}, Goal: {}: {}, Len: {}'.format(start, start_coord, goal, goal_coord, len(path)))
        key = tuple(sorted([start, goal]))
        pairs[key] = path


    cheapest_cost = float("inf")
    cheapest_route = None
    for route in routes:
        total_cost = 0
        for i in range(len(route) - 1):
            start = route[i]
            end = route[i + 1]
            key = tuple(sorted([start, end]))
            edge_path = pairs[key]
            edge_cost = len(edge_path)
            total_cost += edge_cost
        if total_cost < cheapest_cost:
            cheapest_cost = total_cost
            cheapest_route = route
    print(cheapest_route)
    print(cheapest_cost)



if __name__ == '__main__':
    main()

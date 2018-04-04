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

    def dfs(self, start, goal):
        start = self.get_coord(start)
        goal = self.get_coord(goal)
        route = []
        path = {}
        seen = set()
        queue = deque([start])
        while queue:
            coord = queue.pop()
            if coord == goal:
                return path
            seen.add(coord)
            options = self.get_options(coord)
            path.update({x:coord for x in options if x not in seen})
            queue.extend(x for x in options if x not in seen)


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
    perms = list(permutations(goals, len(goals)))

    start = map.get_coord(0)
    targets = [map.get_coord(x) for x in goals]

    print(start)
    print(targets)

    vertices = combinations(range(1, 8), 2)
    for start, goal in vertices:
        path = map.dfs(start, goal)
        print(start, goal, path)





if __name__ == '__main__':
    main()

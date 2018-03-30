import collections
import hashlib


class MapBoundsException(Exception):
    pass


class Node:
    def __init__(self, coord, path, exit=False):
        self.coord = coord
        self.path = path
        self.children = []

    def add(self, child):
        self.children.append(child)


def get_open_doors(path):
    hash = hashlib.md5(path.encode()).hexdigest()
    return [dir for dir, char in zip('UDLR', hash[:4]) if char in 'bcdef']


def delta(dir):
    return {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}[dir]


def move(curr, d):
    """ return (x + dx, y + dy). """
    x = curr[0] + d[0]
    y = curr[1] + d[1]
    if 0 <= x < 4 and 0 <= y < 4:
        return x, y
    else:
        raise MapBoundsException('Cannot move off map')


def traverse_map(node):
    for dir in get_open_doors(node.path):
        try:
            next_pos = move(node.coord, delta(dir))
        except MapBoundsException:
            continue
        child = Node(next_pos, node.path + dir)
        if next_pos != (3, 3):  # If it is not an exit we keep searching
            child = traverse_map(child)
        node.add(child)
    return node


def bfs(tree):
    queue = collections.deque([tree])
    longest = ''
    shortest = '-' * 1000
    while queue:
        node = queue.popleft()
        if node.coord == (3, 3):
            if len(node.path) < len(shortest):
                shortest = node.path
            if len(node.path) > len(longest):
                longest = node.path
        queue.extend(node.children)
    return shortest, longest


def main():

    #########
    #x| | | #
    #-#-#-#-#
    # | | | #
    #-#-#-#-#
    # | | | #
    #-#-#-#-#
    # | | |o#
    #########

    assert get_open_doors('hijkl') == ['U', 'D', 'L']
    assert get_open_doors('hijklDR') == []

    salt = 'yjjvjgan'
    start = Node((0, 0), salt)
    tree = traverse_map(start)
    shortest, longest = bfs(tree)

    shortest_path, longest_path = shortest.strip(salt), longest.strip(salt)

    print('Part A: {} - Shortest path to exit'.format(shortest_path))

    print('Part B: {} - Length of longest path to exit'.format(len(longest_path)))


if __name__ == '__main__':
    main()

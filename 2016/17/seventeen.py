import hashlib


class MapBoundsException(Exception):
    pass


class Node:
    def __init__(self, coord, path):
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


def traverse(node):
    for dir in get_open_doors(node.path):
        try:
            next_pos = move(node.coord, delta(dir))
        except MapBoundsException:
            continue
        child = Node(next_pos, node.path + dir)
        if next_pos == (3, 3):  # Our exit
            print(node.path + dir)
        else:
            child = traverse(child)
        node.add(child)
    return node


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

    start = Node((0, 0), 'ihgpwlah')
    tree = traverse(start)

    start = Node((0, 0), 'yjjvjgan')
    tree = traverse(start)

if __name__ == '__main__':
    main()

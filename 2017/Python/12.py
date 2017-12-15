class Node:
    def __init__(self, name, branches=None):
        self.name = name
        if branches == None:
            self.branches = []
        else:
            self.branches = [Node(x) for x in branches]


def find_pipes(ref, node, piped):
    if any(n.name == ref for n in node.branches) or node.name in piped:
        return [n.name for n in node.branches]
    else:
        return []


def build_group(ref, nodes):
    """ Build a group from a reference node. """
    piped = set([ref])
    last_size = 0
    size = 1
    while size > last_size:  # Scan list until piped stops growing
        for n in nodes.values():
            [piped.add(x) for x in find_pipes(ref, n, piped)]
        last_size = size
        size = len(piped)
    return piped


def main():
    with open('12.input', 'r') as f:
        data = [[int(x) for x in line.split(',')] for line in f]

    nodes = {d[0]:Node(d[0], d[1:]) for d in data}

    # Part A
    part_a = len(build_group(0, nodes))
    print(f'Part A: {part_a} - Size of the 0 piped group')

    # Part B
    groups = set()
    for n in nodes.values():
        known = [int(x) for s in groups for x in s.split(':')]
        if n.name not in known:
            piped = build_group(n.name, nodes)
            groups.add(':'.join(str(x) for x in piped))

    print(f'Part B: {len(groups)} - Total number of groups')


if __name__ == '__main__':
    main()

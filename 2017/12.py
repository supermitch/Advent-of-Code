class Node:
    def __init__(self, name, branches=None):
        self.name = name
        if branches == None:
            self.branches = []
        else:
            self.branches = [Node(x) for x in branches]

    def __repr__(self):
        return f'{self.name}'

def main():
    with open('12.input', 'r') as f:
        data = []
        for line in f:
            data.append([int(x) for x in line.split(', ')])

    nodes = {}
    for d in data:
        try:
            nodes[d[0]] = Node(d[0], d[1:])
        except TypeError:
            nodes[d[0]] = Node(d[0])
    print(nodes[0].name, nodes[0].branches)


    def find_zero(ref, node, piped):
        new_piped = []
        if any(n.name == ref for n in node.branches) or node.name in piped:
            new_piped = [n.name for n in node.branches]
        return new_piped

    piped = set([0])
    last_size = 0
    size = 1
    while size > last_size:
        for n in nodes.values():
            [piped.add(x) for x in find_zero(0, n, piped)]
        last_size = size
        size = len(piped)
        print(f'Group size: {size}')

    groups = set([':'.join(str(x) for x in piped)])
    for n in nodes.values():
        known = [int(x) for s in groups for x in s.split(':')]
        if n.name in known:
            continue
        else:
            piped = set([n.name])
            last_size = 0
            size = 1
            while size > last_size:
                for no in nodes.values():
                    [piped.add(x) for x in find_zero(n.name, no, piped)]
                last_size = size
                size = len(piped)
                print(f'Group size: {size}')
            groups.add(':'.join(str(x) for x in piped))
    print(len(groups))

    print('Part A: {} - '.format(None))
    print('Part B: {} - '.format(None))


if __name__ == '__main__':
    main()

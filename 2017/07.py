def parse_line(line):
    parts = line.strip().split()
    name = parts[0]
    weight = int(parts[1][1:-1])
    total = None  # Total weight including branches
    raw_branches = parts[3:]
    branches = []
    for b in raw_branches:
        branches.append(b.strip(','))
    return {'n': name, 'w': weight, 'b': branches, 't': total}


# Part A
def find_base(data):
    all_nodes = set([n for n in data.keys()])
    all_branches = set([branch for node in data.values() for branch in node['b']])
    return all_nodes.difference(all_branches).pop()


# Part B
def find_children(nodes, n):
    branches = nodes[n]['b']
    if not branches:
        nodes[n]['t'] = nodes[n]['w']  # Total weight
        return nodes[n]['n'], nodes[n]['w']  # Weight
    weights = []
    for node in branches:
        weights.append(find_children(nodes, node))
    if len(set([x[1] for x in weights])) > 1:
        print('{} is unbalanced: {}'.format(n, weights))
    weight = sum([x[1] for x in weights])
    nodes[n]['t'] = nodes[n]['w'] + weight
    return nodes[n]['n'], nodes[n]['t']


def print_branch_weights(nodes, n):
    branches = nodes[n]['b']
    if not branches:
        nodes[n]['t'] = nodes[n]['w']  # Total weight
        return nodes[n]['n'], nodes[n]['w']  # Weight
    weights = []
    for node in branches:
        weights.append(find_children(nodes, node))
    print('{} branches: {}'.format(n, weights))
    weight = sum([x[1] for x in weights])
    nodes[n]['t'] = nodes[n]['w'] + weight
    return nodes[n]['n'], nodes[n]['t']


def part_b(data, base):
    answer = find_children(data, base)

    print_branch_weights(data, 'marnqj')
    print('marnqj weight: {}'.format(data['marnqj']['w']))

    return answer


def main():
    data = {}
    with open('07.input', 'r') as f:
        for line in f:
            node = parse_line(line)
            data[node['n']] = node  # Keyed by name

    base = find_base(data.copy())
    print('Part A: {}'.format(base))

    result_b = part_b(data.copy(), base)
    print('Part B: {}'.format(result_b))


if __name__ == '__main__':
    main()

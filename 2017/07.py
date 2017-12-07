def parse_line(line):
    parts = line.strip().split()
    name = parts[0]
    weight = int(parts[1][1:-1])
    raw_holding = parts[3:]
    holding = []
    for h in raw_holding:
        holding.append(h.strip(','))
    return (name, weight, holding)


# Part A
def find_base(data):
    all_nodes = set([x[0] for x in data])
    all_branches = set([h for x in data for h in x[2]])
    return all_nodes.difference(all_branches)


# Part B
def find_children(nodes, n):
    #  TODO: Actually finish this one
    branches = nodes[n]['h']
    if not branches:
        nodes[n]['t'] = nodes[n]['w']  # Total weight
        return nodes[n]['w']  # Weight

    weights = []
    if n == 'marnqj':
        print(branches)
    for node in branches:
        weights.append(find_children(nodes, node))
    if n == 'marnqj':
        print(weights)
        print(nodes[n]['w'])
    if len(set(weights)) > 1:
        print(n, weights)
    weight = sum(weights)
    nodes[n]['t'] = nodes[n]['w'] + weight
    return nodes[n]['t']


def print_children(nodes, n, depth):
    branches = nodes[n]['h']
    if branches:
        depth += 1
        print('{}{}: {}'.format('\t' * depth, n, branches))
        for branch in branches:
            print_children(nodes, branch, depth)


def part_b(data):
    nodes = {x[0]: {'n': x[0], 'w': x[1], 'h': x[2], 't': None} for x in data}

    base = 'dgoocsw'
    print_children(nodes, base, -1)

    answer = find_children(nodes, base)
    return answer


def main():
    data = []
    with open('07.input', 'r') as f:
        for line in f:
            data.append(parse_line(line))

    base = find_base(data[:])
    print('Part A: {}'.format(base))

    result_b = part_b(data[:])
    print('Part B: {}'.format(result_b))


if __name__ == '__main__':
    main()

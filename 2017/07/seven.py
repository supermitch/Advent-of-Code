class Node():
    def __init__(self, name, weight, branches):
        self.name = name
        self.weight = weight
        self.branches = branches
        self.total = None  # Total weight including children


def parse_line(line):
    parts = line.strip().split()
    name = parts[0]
    weight = int(parts[1][1:-1])
    branches = [b.strip(',') for b in parts[3:]]
    return Node(name, weight, branches)


# Part A
def find_base(data):
    all_nodes = set([n for n in data.keys()])
    all_branches = set([b for node in data.values() for b in node.branches])
    return all_nodes.difference(all_branches).pop()


# Part B
def unbalanced(iter):
    return len(set(iter)) != 1


def find_unbalanced(nodes, n):
    curr = nodes[n]
    if not curr.branches:
        curr.total = curr.weight  # Own weight
        return curr.total

    weights = [find_unbalanced(nodes, child) for child in curr.branches]

    if unbalanced(weights):
        children = zip(curr.branches, weights)
        print('{} is unbalanced: {}'.format(curr.name, list(children)))

    curr.total = curr.weight + sum(weights)
    return curr.total


def print_branch_weights(nodes, n):
    curr = nodes[n]
    if not curr.branches:
        curr.total = curr.weight  # Total weight
        return curr.weight  # Weight

    weights = [find_unbalanced(nodes, node) for node in curr.branches]

    print('{} branches: {}'.format(n, weights))

    curr.total = curr.weight + sum(weights)
    return curr.total


def part_b(data, base):
    answer = find_unbalanced(data, base)

    print_branch_weights(data, 'marnqj')
    print('marnqj weight: {}'.format(data['marnqj'].weight))

    return answer


def main():
    data = {}
    with open('input.txt', 'r') as f:
        for line in f:
            node = parse_line(line)
            data[node.name] = node

    base = find_base(data.copy())
    print('Part A: {}'.format(base))

    result_b = part_b(data.copy(), base)
    print('Part B: {}'.format(result_b))


if __name__ == '__main__':
    main()

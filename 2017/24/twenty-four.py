import copy


def parse_line(line):
    return [int(x) for x in line.strip().split('/')]


class Bridge:
    def __init__(self, path):
        self.seen = set()
        self.path = path
        self.complete = False

    def __repr__(self):
        return 'Bridge({})'.format(self.path)


def part_a(components):
    start_bridge = Bridge([(0, 0)])

    bridges = [start_bridge]
    final_bridges = []
    while any(not b.complete for b in bridges):
        new_bridges = []
        for bridge in bridges[:]:
            # print('\nNext bridge: ', bridge)
            added = False
            for comp_id, comp in components.items():
                # print('comp', comp)
                if comp_id in bridge.seen:
                    # print('seen')
                    continue
                a, b = comp
                port = bridge.path[-1][1]  # Free port
                # print('port', port)

                new_bridge = copy.deepcopy(bridge)
                if port == a:
                    # print('match!')
                    added = True
                    new_bridge.path.append([a, b])
                elif port == b:
                    # print('match!')
                    added = True
                    new_bridge.path.append([b, a])
                else:
                    # print('no')
                    continue
                new_bridge.seen.add(comp_id)
                new_bridges.append(new_bridge)
            if not added:  # We checked every component and found nothing
                new_bridge = copy.deepcopy(bridge)
                new_bridge.complete = True
                final_bridges.append(new_bridge)
        bridges = new_bridges[:]
    print('Final bridges: ', final_bridges)

    max_bridge = None
    max_strength = 0
    longest = None
    max_length = 0
    for bridge in final_bridges:
        total = sum(sum(p) for p in bridge.path)
        if total > max_strength:
            max_strength = total
            max_bridge = bridge.path
        length = len(bridge.path)
        if length >= max_length:
            if longest is None:
                longest = bridge.path
                max_length = len(bridge.path)
            else:
                if sum(sum(p) for p in bridge.path) > sum(sum(p) for p in longest):
                    longest = bridge.path
                    max_length = len(bridge.path)
                else:
                    continue

    print('Longest', longest)
    print('Length', max_length)
    print('Max strength', max_strength)
    print(max_bridge)
    return max_strength


def part_b(data):
    return


def main():
    with open('input.txt', 'r') as f:
        comps = {i: parse_line(x) for i, x in enumerate(f)}

    test = {
        1: [0, 2],
        2: [2, 2],
        3: [2, 3],
        4: [3, 4],
        5: [3, 5],
        6: [0, 1],
        7: [1, 10],
        8: [9, 10],
    }
    assert part_a(test) == 31

    strength = part_a(comps)
    print('Part A: {} - Maximum possible bridge strength'.format(strength))


if __name__ == '__main__':
    main()


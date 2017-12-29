import copy


def parse_line(line):
    return [int(x) for x in line.strip().split('/')]


class Bridge:
    def __init__(self, path):
        self.seen = set()
        self.path = path

    def __repr__(self):
        return 'Bridge({})'.format(self.path)


def part_a(components):

    import time
    tic = time.time()
    bridges = [Bridge([(0, 0)])]
    final_bridges = []
    while bridges:
        new_bridges = []
        for bridge in bridges[:]:
            # print('\nNext bridge: ', bridge)
            added = False
            for comp_id, comp in components.items():
                # print('comp', comp)
                if comp_id in bridge.seen:
                    continue

                a, b = comp
                port = bridge.path[-1][1]  # Free port
                # print('port', port)

                new_bridge = copy.deepcopy(bridge)
                if port == a:
                    added = True
                    new_bridge.path.append([a, b])
                elif port == b:
                    added = True
                    new_bridge.path.append([b, a])
                else:
                    continue
                new_bridge.seen.add(comp_id)
                new_bridges.append(new_bridge)
            if not added:  # We checked every component and found nothing
                final_bridges.append(copy.deepcopy(bridge))
        bridges = new_bridges[:]

    print('No. final bridges: ', len(final_bridges))

    strongest = None
    max_strength = 0
    longest_strength = 0

    longest = None
    max_length = 0
    for bridge in final_bridges:
        total = sum(sum(p) for p in bridge.path)
        if total > max_strength:
            max_strength = total
            strongest = bridge

        length = len(bridge.path)
        if length > max_length:
            longest = bridge
            longest_strength = total
            max_length = length
        elif length == max_length:
            if total > longest_strength:
                longest = bridge
                longest_strength = total
                max_length = length


    print('Longest', longest)
    print('Max length', max_length)
    print('Longest strength', sum(sum(p) for p in longest.path))
    print('\nStrongest', strongest)
    print('Max strength', max_strength)
    print('Elapsed {}'.format(time.time() - tic))

    return max_strength


def main():
    with open('input.txt', 'r') as f:
        comps = {i: parse_line(x) for i, x in enumerate(f)}

    test = {
        1: [0, 2],
        2: [2, 100],
        3: [2, 3],
        4: [3, 4],
        5: [4, 5],
        6: [1, 10],
        7: [10, 20],
        8: [10, 1],
        9: [6, 5],
        10: [6, 7],
        11: [7, 8],
    }
    part_a(test)

    strength = part_a(comps)
    print('Part A: {} - Maximum possible bridge strength'.format(strength))


if __name__ == '__main__':
    main()

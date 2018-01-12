from collections import defaultdict


def main():
    bots = defaultdict(list)
    output = defaultdict(list)
    moves = {}
    with open('input.txt', 'r') as f:
        for line in f:
            parts = line.strip().split()
            if 'value' in parts:
                val = int(parts[1])
                id = parts[-1]
                bots[id].append(val)
            else:
                id = parts[1]
                low_dest, low = parts[5:7]
                high_dest, high = parts[10:12]
                moves[id] = (low_dest, low, high_dest, high)

    while any(len(chips) == 2 for chips in bots.values()):
        for bot, chips in list(bots.items()):  # Copy dict so we can edit
            if len(chips) == 2:
                if sorted(chips) == [17, 61]:
                    part_a = bot

                low_dest, low, high_dest, high = moves[bot]

                if low_dest == 'bot':
                    bots[low].append(min(chips))
                else:
                    output[low].append(min(chips))

                if high_dest == 'bot':
                    bots[high].append(max(chips))
                else:
                    output[high].append(max(chips))

                bots[bot] = []

    part_b = output['0'][0] * output['1'][0] * output['2'][0]

    print('Part A: {} - Bot who compared 17 & 61'.format(part_a))
    print('Part B: {} - Multiple of chip in outputs 0, 1 & 2'.format(part_b))


if __name__ == '__main__':
    main()

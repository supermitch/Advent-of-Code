def repr(memory):
    return '[' + ','.join([str(x) for x in memory]) + ']'


def redistribute(memory):
    n = len(memory)
    count = 0
    seen = set()
    while True:
        seen.add(repr(memory))
        high = max(memory)
        i = memory.index(high)  # Returns first high bank
        blocks = high
        memory[i] = 0  # Reset current bank
        j = i
        while blocks > 0:
            memory[(j + 1) % n] += 1
            blocks -= 1
            j += 1
        count += 1
        if repr(memory) in seen:
            return count, memory


def main():
    memory = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]

    count_a, state = redistribute(memory)
    print('Part A: {}'.format(count_a))
    count_b, _ = redistribute(state)
    print('Part B: {}'.format(count_b))


if __name__ == '__main__':
    main()

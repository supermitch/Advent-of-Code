def reallocate(memory):
    n = len(memory)
    blocks = max(memory)
    i = memory.index(blocks)  # Returns first high bank
    memory[i] = 0  # Reset current bank
    while blocks > 0:
        memory[(i + 1) % n] += 1
        blocks -= 1
        i += 1
    return memory


def redistribute(memory):
    count = 0
    seen = set()
    while True:
        seen.add(memory.__str__())
        memory = reallocate(memory)
        count += 1
        if memory.__str__() in seen:
            return count, memory


def main():
    memory = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]

    count_a, state = redistribute(memory)
    print('Part A: {}'.format(count_a))

    count_b, _ = redistribute(state)
    print('Part B: {}'.format(count_b))


if __name__ == '__main__':
    main()

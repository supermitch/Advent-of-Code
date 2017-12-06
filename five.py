def exit_count(jumps, incrementor):
    count = 0
    i = 0
    while True:
        try:
            move = jumps[i]
            jumps[i] += incrementor(move)
            i += move
            count += 1
        except IndexError:
            return count


def main():
    with open('five.txt', 'r') as f:
        jumps = [int(x.strip()) for x in f.readlines()]

    print('Part A: {}'.format(exit_count(jumps[:], lambda x: 1)))
    print('Part B: {}'.format(exit_count(jumps[:], lambda x: -1 if x >= 3 else 1)))


if __name__ == '__main__':
    main()

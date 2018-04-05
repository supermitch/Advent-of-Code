def parse_input():
    """ Turn our input into a coordinate list. Goal nodes are integers. """
    data = []
    with open('input.txt', 'r') as f:
        for line in f:
            data.append(line.strip())
    return data


def main():
    data = parse_input()

    print('Part A: {} - Number of safe tiles'.format(None))

    print('Part B: {} - '.format(None))


if __name__ == '__main__':
    main()

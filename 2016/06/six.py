import collections


def correct(messages, idx):
    message = ''
    for col in zip(*messages):
        c = collections.Counter(col)
        message += c.most_common()[idx][0]
    return message


def main():
    with open('input.txt', 'r') as f:
        messages = [list(line.strip()) for line in f]

    most_common = correct(messages, 0)
    print('Part A: {} - Most-common corrected message'.format(most_common))

    least_common = correct(messages, -1)
    print('Part B: {} - Least-common corrected message'.format(least_common))


if __name__ == '__main__':
    main()

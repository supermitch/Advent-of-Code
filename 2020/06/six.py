def main():
    groups = []
    with open('input.txt') as f:
        for group in f.read().strip().split('\n\n'):
            groups.append(group.split('\n'))

    part_a = 0
    part_b = 0
    for group in groups:
        part_a += len(set().union(*group))
        part_b += len(set(group[0]).intersection(*group))

    print(f'Part A: {part_a} - Sum of anyone answered yes')
    print(f'Part B: {part_b} - Sum of everyone answered yes')


if __name__ == '__main__':
    main()

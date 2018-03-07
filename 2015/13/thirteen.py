def find_optimum_happiness(guests)
    return 10


def main():
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f]

    guests = extract_guests(lines)

    part_a = find_optimum_happiness(guests)
    print('Part A: {} - Optimum happiness'.format(part_a))


if __name__ == '__main__':
    main()

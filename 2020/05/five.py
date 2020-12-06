def seat_id(seat):
    rows = list(range(128))
    for k in seat[:7]:
        n = len(rows)
        if k == 'F':
            rows = rows[:n // 2]
        elif k == 'B':
            rows = rows[n // 2:]
    cols = list(range(8))
    for k in seat[7:]:
        n = len(cols)
        if k == 'L':
            cols = cols[:n // 2]
        elif k == 'R':
            cols = cols[n // 2:]
    return rows[0] * 8 + cols[0]


def main():
    with open('input.txt') as f:
        data = [x.strip() for x in f]

    part_a = max(seat_id(x) for x in data)

    all_seats = sorted([seat_id(x) for x in data])
    missing = set(range(all_seats[0], all_seats[-1])) - set(all_seats)
    part_b = missing.pop()

    print(f'Part A: {part_a} - Maximum seat ID')
    print(f'Part B: {part_b} - My seat ID')


if __name__ == '__main__':
    main()

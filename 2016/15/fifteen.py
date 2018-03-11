def parse(l):
    parts = l.strip('.').split()
    positions = int(parts[3])
    start = int(parts[-1])
    return positions, start


def is_open(disc, time):
    """ At a given time, is the disc at position 0? """
    positions, start = disc
    step = time % positions
    pos = (start + step) % positions
    return pos == 0  # "0" is open


def all_open(discs, time):
    """ For a given drop time, will all discs be open at the right time? """
    for dt, disc in enumerate(discs, start=1):  # 1st disc is 1 s after drop
        if not is_open(disc, time + dt):  # Each disc is 1 s further away
            return False
    return True


def find_open_time(discs):
    time = 0
    while True:
        if all_open(discs, time):
            return time
        time += 1


def main():
    f = [
        'Disc #1 has 5 positions; at time=0, it is at position 4.',
        'Disc #2 has 2 positions; at time=0, it is at position 1.',
    ]
    discs = [parse(l.strip()) for l in f]
    assert is_open(discs[0], 1)
    assert is_open(discs[0], 6)
    assert is_open(discs[1], 7)
    assert not is_open(discs[1], 2)
    assert find_open_time(discs) == 5

    with open('input.txt', 'r') as f:
        discs = [parse(l.strip()) for l in f]

    time = find_open_time(discs)
    print('Part A: {} - First time to get a dropped capsule'.format(time))

    discs.append((11, 0))  # Add a new 11th disc for Part B
    time = find_open_time(discs)
    print('Part B: {} - Time to get a capsule w/ 11 discs'.format(time))


if __name__ == '__main__':
    main()

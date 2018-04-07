def next_elf(id, playing, no_of_elves):
    while True:
        id += 1
        id = id % (no_of_elves + 1)
        id = max(id, 1)  # Elf indices start at 1
        if id in playing:  # This elf in the game?
            return id


def part_a(playing, no_of_elves):
    id = 1  # Starts at elf 1
    while True:
        next_id = next_elf(id, playing, no_of_elves)
        if next_id == id:
            return id
        playing.remove(next_id)  # Next elf loses all presents: they're out
        id = next_elf(next_id, playing, no_of_elves)


def main():
    no_of_elves = 3012210
    playing = set(range(1, no_of_elves + 1))

    part_a_elf = part_a(playing, no_of_elves)
    print('Part A: {} - The winning elf'.format(part_a_elf))


if __name__ == '__main__':
    main()

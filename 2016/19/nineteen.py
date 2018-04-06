def next_elf(id, playing, no_of_elves):
    while True:
        id += 1
        id = id % (no_of_elves + 1)
        id = max(id, 1)
        if id in playing:
            return id


def main():
    # 1830115 -> too low
    no_of_elves = 3012210
    circle = [1] * no_of_elves
    elf_ids = range(1, no_of_elves + 1)

    playing = set(elf_ids)
    gifts = {x: 1 for x in elf_ids}

    id = 1  # Starts at elf 1
    while True:
        # print('Elf {}'.format(id))
        next_id = next_elf(id, playing, no_of_elves)
        # print('Next elf {}'.format(next_id))
        if next_id == id:
            print('Only elf <{}> remains!'.format(id))
            return id
        else:
            gifts[id] += gifts[next_id]  # Takes next elf's gifts
            gifts[next_id] = 0
            playing.remove(next_id)  # No presents? You're out!
        id = next_elf(next_id, playing, no_of_elves)


if __name__ == '__main__':
    main()

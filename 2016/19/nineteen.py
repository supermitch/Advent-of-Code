import collections
import itertools


def game_a(no_of_elves):
    players = collections.deque(range(1, no_of_elves + 1))
    while len(players) > 1:
        players.rotate(-1)
        players.popleft()  # The next elf lost their presents
    return players.pop()


def game_b(no_of_elves):
    players = collections.deque(range(1, no_of_elves + 1))
    players.rotate(-len(players) // 2)
    for step in itertools.cycle([0, 1]):  # Repeats forever
        players.popleft()
        players.rotate(-step)
        if len(players) == 1:
            return players.pop()


def main():
    no_of_elves = 3012210

    winner_a = game_a(no_of_elves)
    print('Part A: {} - The winning elf of game A'.format(winner_a))

    winner_b = game_b(no_of_elves)
    print('Part B: {} - The winning elf of game B'.format(winner_b))


if __name__ == '__main__':
    main()

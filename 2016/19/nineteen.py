from collections import deque


def game_a(no_of_elves):
    players = deque(range(1, no_of_elves + 1))
    while True:
        players.rotate(-1)
        players.popleft()
        if len(players) == 1:
            return players.popleft()


def main():
    no_of_elves = 3012210

    winner_a = game_a(no_of_elves)
    print('Part A: {} - The winning elf'.format(winner_a))


if __name__ == '__main__':
    main()

import math


def parse_rules(line):
    parts = line.strip().split()
    deer = parts[0]
    speed = int(parts[3])
    fly = int(parts[6])
    rest = int(parts[13])
    return (deer, speed, fly, rest)


def timed_race(rules, time):
    distances = {}
    for rule in rules:
        deer, speed, fly, rest = rule
        distance = 0
        rep = fly + rest  # Total rep time
        reps = math.floor(time / rep)  # How many reps completed?
        distance = reps * fly * speed

        remainder = time % rep  # How much time remained?
        if remainder >= fly:  # If they made it to the rest phase
            distance += fly * speed
        else:
            distance += speed * remainder  # We're still flying

        distances[deer] = distance
    return distances


def points_race(rules, time):
    points = {deer: 0 for deer, _, _, _ in rules}
    for t in range(1, time + 1):
        distances = timed_race(rules, t)
        furthest = max(distances.values())
        for deer in points:
            if distances[deer] == furthest:
                points[deer] += 1
    return points


def main():
    test = [
        'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
        'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.',
    ]
    rules = [parse_rules(l) for l in test]
    distances = timed_race(rules, 1000)
    points = points_race(rules, 1000)
    assert max(distances.values()) == 1120
    assert max(points.values()) == 689

    with open('input.txt', 'r') as f:
        rules = [parse_rules(l) for l in f]

    race_length = 2503

    distances = timed_race(rules, race_length)
    part_a = max(distances.values())
    print('Part A: {} - Winning distance after {} s'.format(part_a, race_length))

    points = points_race(rules, race_length)
    part_b = max(points.values())
    print('Part B: {} - Winning points after {} s'.format(part_b, race_length))


if __name__ == '__main__':
    main()

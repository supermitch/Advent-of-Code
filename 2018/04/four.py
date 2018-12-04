#!/usr/bin/env python
from collections import defaultdict

def parse(line):  # e.g. [1518-03-27 00:02] Guard #2789 begins shift
    date = line[1:17]
    id = int(line.split('#')[1].split()[0]) if '#' in line else None
    return date, id


def read_input():
    with open('input.txt', 'r') as f:
        return [parse(l.strip()) for l in f]


def group_by_id(data):
    guards = defaultdict(list)
    for date, id in data:
        if id:  # Starts shift (time irrelevant)
            current_id = id
        else:  # Falls sleep or wakes up
            guards[current_id].append(date)
    return guards


def calculate_schedule(guard_data):
    guard_mins = {}
    for id, stamps in guard_data.items():
        guard_total = 0
        mins = defaultdict(int)
        for i in range(0, len(stamps) - 1, 2):
            sleep, wake = stamps[i], stamps[i + 1]
            start = int(sleep.split(':')[1])  # Minutes
            end = int(wake.split(':')[1])  # Minutes
            for j in range(start, end):  # The clock minutes
                mins[j] += 1
            guard_total += end - start
        guard_mins[id] = mins
    return guard_mins


def worst_guard(guard_mins):  # Part A
    worst_id = max(guard_mins, key=lambda k: sum(guard_mins[k].values()))
    sleep_mins = guard_mins[worst_id]
    worst_minute = max(sleep_mins, key=lambda k: sleep_mins[k])
    return worst_id * worst_minute


def most_consistent(guard_mins):  # Part B
    max_duration = 0
    max_time = None
    max_id = None
    for id, mins in guard_mins.items():
        for k, v in mins.items():
            if v > max_duration:
                max_duration = v
                max_time = k
                max_id = id
    return max_time * max_id


def main():
    raw = read_input()
    data = sorted(raw, key=lambda x:x[0])  # Sort by timestamp
    guard_data = group_by_id(data)
    guard_mins = calculate_schedule(guard_data)

    part_a = worst_guard(guard_mins)
    print("Part A: {} - Sleepiest guard's worst Guard-Minute".format(part_a))

    part_b = most_consistent(guard_mins)
    print('Part B: {} - Most consistently slept Guard-Minute'.format(part_b))


if __name__ == '__main__':
    main()

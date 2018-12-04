#!/usr/bin/env python
from collections import defaultdict
import re
from pprint import pprint

def parse(line):
    # e.g. [1518-03-27 00:02] Guard #2789 begins shift
    date = line[1:17]

    id = None
    if '#' in line:
        id = int(line.split('#')[1].split()[0])
    act = None
    if 'up' in line:
        act = 'up'
    elif 'asleep' in line:
        act = 'sleep'
    return (date, id, act)

def read_input():
    with open('input.txt', 'r') as f:
        return [parse(l.strip()) for l in f]

def part_a(data):
    return None

def part_b(data):
    return None

def main():
    print('\n')
    data = read_input()
    sort = sorted(data, key=lambda x:x[0])  # Sort by timestamp

    guards = defaultdict(list)
    current_id = None
    for date, id, act in sort:
        if id:
            current_id = id
        if act:
            guards[current_id].append((date, act))

    longest = 0
    max_guard = None
    guard_mins = {}
    for id, stamps in guards.items():
        print('Guard: ', id)
        id_total = 0
        mins = defaultdict(int)
        for i in range(0, len(stamps) - 1, 2):
            sleep, act = stamps[i]
            start = int(sleep.split(':')[1])
            wake, act = stamps[i + 1]
            end = int(wake.split(':')[1])
            for j in range(start, end):
                mins[j] += 1
            asleep = end - start
            print(stamps[i], stamps[i + 1], asleep)
            id_total += asleep
            if id_total > longest:
                longest = id_total
                max_guard = id
        print(id, id_total)
        guard_mins[id] = mins

    print('guard', max_guard, 'total: ', longest)
    max_mins = None
    most = 0
    for k, v in guard_mins[max_guard].items():
        if v > most:
            most = v
            max_mins = k
    print('max mins', max_mins)
    print('Part A', max_guard * max_mins)


    max_duration = 0
    max_time = None
    max_id = None
    for id, mins in guard_mins.items():
        for k, v in mins.items():
            if v > max_duration:
                max_duration = v
                max_time = k
                max_id = id
    print(max_duration, max_time, max_id)
    print('Part B', max_time * max_id)

    ans_a = part_a(data)
    print('Part A: {} - '.format(ans_a))
    ans_b = part_b(data)
    print('Part B: {} - '.format(ans_b))

if __name__ == '__main__':
    main()

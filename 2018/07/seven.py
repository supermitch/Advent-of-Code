#!/usr/bin/env python
from collections import defaultdict
from itertools import permutations
import string

def parse(l):
    l = l.split()
    return l[1], l[7]

def read_input():
    with open('input.txt') as f:
        return [parse(l.strip()) for l in f]

def main():
    data = read_input()
    ADD = 60
    WORKERS = 5
    test = [
        ('C', 'A'),
        ('C', 'F'),
        ('A', 'B'),
        ('A', 'D'),
        ('B', 'E'),
        ('D', 'E'),
        ('F', 'E'),
    ]
    reqs = defaultdict(list)
    for x, y in data:
        reqs[y].append(x)

    alphabet = set()
    befores = set()
    for x, y in data:
        alphabet.add(x)
        alphabet.add(y)
        befores.add(y)

    # Step A must be finished before step G can begin.
    starts = alphabet - befores
    starts = sorted(starts)
    print(starts)
    steps = []
    queue = sorted(starts)

    time = 0
    times = {k: i for i, k in enumerate(string.ascii_uppercase, start=1)}
    complete = {k: False for k in string.ascii_uppercase}
    work_queue = [None] * WORKERS
    while True:
        print('\ntime: ', time)
        for k, req in reqs.items():
            if all(x in steps for x in req):
                if k not in queue and k not in steps:
                    if not any(wq['char'] == k for wq in work_queue if wq):
                        queue.append(k)

        queue = sorted(queue)
        print('queue 1', queue)
        next_work = work_queue[:]
        for i, wq in enumerate(work_queue):
            if wq is not None and time - wq['start'] >= times[wq['char']] + ADD:
                print('work complete')
                steps.append(wq['char'])
                wq = None
                next_work[i] = wq
        work_queue = next_work[:]
        for k, req in reqs.items():
            if all(x in steps for x in req):
                if k not in queue and k not in steps:
                    if not any(wq['char'] == k for wq in work_queue if wq):
                        queue.append(k)

        queue = sorted(queue)
        next_work = work_queue[:]
        for i, wq in enumerate(work_queue):
            if wq is None:  # Can pick up a job
                if queue:
                    worker = {'char': queue[0], 'start': time}  # Start work
                    next_work[i] = worker
                    del queue[0]
        work_queue = next_work[:]
        print(work_queue)
        print('steps', steps)
        print('queue 2', queue)

        if len(steps) == len(alphabet):
            print('done', ''.join(steps))
            break
        time += 1
    print('total time', time)  # 943 High, 930 Low, 938, 942, 932

if __name__ == '__main__':
    main()

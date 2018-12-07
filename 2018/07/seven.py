#!/usr/bin/env python
import itertools
from collections import defaultdict
from string import ascii_uppercase

def parse(l):
    l = l.split()
    return l[1], l[7]

def read_input():
    with open('input.txt') as f:
        return [parse(l.strip()) for l in f]

def main():
    data = read_input()
    TIME = 60
    WORKER_COUNT = 5
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
    for x, y in data:  # e.g. Step A must be finished before step G can begin
        reqs[y].append(x)  # e.g. {G: [A, I, K]} - Lists requirements for G

    all_chars = set([x for x, y in data] + [y for x, y in data])
    blocked = set([y for _, y in data])

    queue = list(sorted(all_chars - blocked))
    steps = []

    times = {c: TIME + ord(c) - ord('A') + 1 for c in ascii_uppercase}
    jobs = [None] * WORKER_COUNT
    for t in itertools.count():
        for i, wq in enumerate(jobs):
            if wq and t - wq['start'] >= times[wq['char']]:
                steps.append(wq['char'])
                jobs[i] = None  # Complete jobs

        to_del = []
        for k, req in reqs.items():
            if all(x in steps for x in req):  # All requirements met
                queue.append(k)  # Add to queue
                to_del.append(k)
        reqs = {k: req for k, req in reqs.items() if k not in to_del}

        queue = sorted(queue)
        for i, wq in enumerate(jobs):
            if wq is None and queue:  # Can pick up a job, and jobs exist
                worker = {'char': queue[0], 'start': t}  # Start work
                jobs[i] = worker  # Start next job
                del queue[0]

        if len(steps) == len(all_chars):
            print('Done: {}'.format(''.join(steps)))
            break
    print('Part B: {} - Total time for 5 workers to complete'.format(t))


if __name__ == '__main__':
    main()

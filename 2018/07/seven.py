#!/usr/bin/env python
import itertools
from collections import defaultdict
from string import ascii_uppercase


def complete(data, times, workers=1):
    reqs = defaultdict(list)
    for x, y in data:  # e.g. Step A must be finished before step G can begin
        reqs[y].append(x)  # e.g. {G: [A, I, K]} - Lists requirements for G

    all_chars = set([x for x, y in data] + [y for x, y in data])
    blocked = set([y for _, y in data])

    queue = list(sorted(all_chars - blocked))

    steps = []
    jobs = [None] * workers
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
            return ''.join(steps), t

def main():
    data = []
    with open('input.txt') as f:
        for l in f:
            p = l.strip().split()
            data.append((p[1], p[7]))

    times = {c: 1 for c in ascii_uppercase}  # Times to complete each node
    part_a, _ = complete(data, times, workers=1)
    print('Part A: {} - Sorted step order'.format(part_a))

    times = {c: 60 + ord(c) - ord('A') + 1 for c in ascii_uppercase}
    _, part_b = complete(data, times, workers=5)
    print('Part B: {} - Time for 5 workers to build the sleigh'.format(part_b))


if __name__ == '__main__':
    main()

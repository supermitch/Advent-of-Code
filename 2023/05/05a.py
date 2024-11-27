from collections import defaultdict
from pprint import pp  # noqa
from math import inf

with open('05_input.txt') as f:
    seeds = [int(x) for x in next(f).split(':')[1].split()]
    maps = defaultdict(list)
    for line in [x.strip() for x in f if x.strip()]:
        if ':' in line:
            key = line.split()[0]
        else:
            maps[key].append([int(x) for x in line.split()])

seed_path = {}
for seed in seeds:
    print(seed)
    seed_path[seed] = [seed]
    for name, ranges in maps.items():
        step_id = seed_path[seed][-1]
        for dest, start, length in ranges:
            if start <= step_id <= start + length:
                out = dest + step_id - start
                seed_path[seed].append(out)
                break
        else:  # Isn't mapped
            out = step_id
        print(name, out)

lowest = inf
for path in seed_path.values():
    lowest = min(path[-1], lowest)

print(f'Part a: {lowest} lowest location number')

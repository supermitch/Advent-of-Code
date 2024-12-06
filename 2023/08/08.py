import itertools
import re

with open('08_input.txt') as f:
    lines = [x.strip() for x in f]

elements = {}
steps = lines[0]
for line in lines[1:]:
    if m := re.match(r'([\w]{3}) = \(([\w]{3}), ([\w]{3})\)', line.strip()):
        elements[m[1]] = {'L': m[2], 'R': m[3]}

key = 'AAA'
for i in itertools.count():
    side = steps[i % len(steps)]
    key = elements[key][side]
    if key == 'ZZZ':
        break

print(f'Part a: {i + 1} steps')

nodes = {x: x for x in elements.keys() if x.endswith('A')}
step_counts = {x: 0 for x in nodes.keys()}
for i in itertools.count():
    side = steps[i % len(steps)]
    for start, key in nodes.items():
        key = elements[key][side]
        nodes[start] = elements[key][side]
        if key.endswith('Z'):
            step_counts[start] = i
            print(step_counts)
    if all(x.endswith('Z') for x in nodes.values()):
        break

print(f'Part b: {i + 1} steps')

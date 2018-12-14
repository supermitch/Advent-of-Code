#!/usr/bin/env python
from collections import deque


def gen_recipes(goal_b):
    goal_a = 84601
    elf_a = 0
    elf_b = 1
    recipes = deque([3, 7])
    last_six = deque(maxlen=len(goal_b))
    count = 2
    while True:
        a, b = recipes[elf_a], recipes[elf_b]
        nxt = a + b
        recipes.extend(int(x) for x in str(nxt))
        last_six.extend(int(x) for x in str(nxt))
        count += 2 if nxt >= 10 else 1
        if not count % 10000:
            print(count)
        if last_six == goal_b:
            return count - len(goal_b)
        elf_a = (elf_a + 1 + a) % count
        elf_b = (elf_b + 1 + b) % count

        #if len(recipes) == goal_a + 10:
        #    print('Part A: ', ''.join(str(r) for r in recipes[goal_a:]))


def main():
    goal_a = 84601
    goal_b = deque([8, 4, 6, 0, 1])

    assert gen_recipes(deque([5,1,5,8,9])) == 9
    assert gen_recipes(deque([0,1,2,4,5])) == 5
    assert gen_recipes(deque([9,2,5,1,0])) == 18
    assert gen_recipes(deque([5,9,4,1,4])) == 2018

    print('Running...')
    print('Part B: {} - '.format(gen_recipes(goal_b)))


if __name__ == '__main__':
    main()

#!/usr/bin/env python
from collections import deque


def gen_recipes(goal_b):
    goal_a = 84601
    elf_a = 0
    a_s = deque([])
    elf_b = 1
    recipes = [3, 7]
    last_six = deque(maxlen=len(goal_b))
    count = 2
    while True:
        a, b = recipes[elf_a], recipes[elf_b]
        a_s.append(a)
        nxt = a + b
        if nxt > 9:
            recipes.append( nxt // 10)
            last_six.append( nxt // 10)
            count += 1
            if 8 in last_six and 4 in last_six and 6 in last_six and 1 in last_six and 0 in last_six:
                print(last_six)
            if last_six == goal_b:
                return count - len(goal_b)
        recipes.append(nxt % 10)
        last_six.append(nxt % 10)
        count += 1
        if last_six == goal_b:
            return count - len(goal_b)
        if not count % 100000:
            print(count)
        elf_a = (elf_a + 1 + a) % count
        elf_b = (elf_b + 1 + b) % count

        #if len(recipes) == goal_a + 10:
        #    print('Part A: ', ''.join(str(r) for r in recipes[goal_a:]))


def main():
    goal_a = 84601
    goal_b = deque([0, 8, 4, 6, 0, 1])

    assert gen_recipes(deque([1,0,1,0])) == 2
    assert gen_recipes(deque([4,5,1,5,8,9])) == 8
    assert gen_recipes(deque([5,1,5,8,9])) == 9
    assert gen_recipes(deque([1,5,8,9])) == 10
    assert gen_recipes(deque([9,2,5,1,0])) == 18
    assert gen_recipes(deque([5,9,4,1,4])) == 2018

    print('Running...')
    print('Part B: {} - '.format(gen_recipes(goal_b)))


if __name__ == '__main__':
    main()

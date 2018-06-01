#!/usr/bin/env python
from collections import namedtuple
from pprint import pprint
from random import randint


def read_ingredients(f):
    Ingredient = namedtuple('Ingredient', 'capacity, durability, flavor, texture, calories')
    ingredients = []
    for line in f:
        parts = line.replace(':', '').replace(',', '').split()
        values = [int(parts[i]) for i in (2, 4, 6, 8, 10)]
        ingredients.append(Ingredient(*values))
    return ingredients


def score(recipe):
    cap = max(sum(qty * x.capacity for x, qty in recipe), 0)
    dur = max(sum(qty * x.durability for x, qty in recipe), 0)
    flv = max(sum(qty * x.flavor for x, qty in recipe), 0)
    txt = max(sum(qty * x.texture for x, qty in recipe), 0)

    cal = max(sum(qty * x.calories for x, qty in recipe), 0)

    return (cap * dur * flv * txt, cal)


def random_parts(t=100, k=4):
    """
    Produce a partition of t into k values,
    e.g. t=10, k=4 could yield [1, 1, 3, 5]
    """
    rs = [0] + sorted([randint(1, t - 1) for i in range(k - 1)]) + [t]
    out = []
    for i in range(len(rs) - 1):
        out.append(rs[i + 1] - rs[i])
    assert sum(out) == 100, "Sum of parts was not 100!"
    return out


def main():
    test = [
        "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
        "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3",
    ]
    butterscotch, cinnamon = read_ingredients(test)
    recipe = [(butterscotch, 44), (cinnamon, 56)]
    assert score(recipe)[0] == 62842880

    with open('input.txt', 'r') as f:
        sugar, sprinkles, candy, chocolate = read_ingredients(f)

    # Part A
    max = 0
    max_recipe = None
    sums = []
    for i in range(30000):
        qtys = random_parts()
        recipe = [(sugar, qtys[0]), (sprinkles, qtys[1]), (candy, qtys[2]), (chocolate, qtys[3])]
        total, cals = score(recipe)
        if total > 0:
            sums.append((total, qtys))
            if total > max:
                max = total
                max_recipe = recipe
    pprint(sorted(sums)[-5:])
    print('Max: ', max_recipe)

    # Part B
    max = 0
    max_recipe = None
    sums = []
    for i in range(30000):
        qtys = random_parts()
        recipe = [(sugar, qtys[0]), (sprinkles, qtys[1]), (candy, qtys[2]), (chocolate, qtys[3])]
        total, cals = score(recipe)
        if total > 0 and cals == 500:
            sums.append((total, qtys))
            if total > max:
                max = total
                max_recipe = recipe
    pprint(sorted(sums)[-5:])
    print('Max: ', max_recipe)


if __name__ == '__main__':
    main()

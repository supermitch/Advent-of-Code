#!/usr/bin/env python
from collections import namedtuple


def read_ingredients(f):
    Ingredient = namedtuple('Ingredient', 'capacity, durability, flavor, texture, calories')
    ingredients = []
    for line in f:
        parts = line.replace(':', '').replace(',', '').split()
        values = [int(parts[x]) for x in (2, 4, 6, 8, 10)]
        ingredients.append(Ingredient(*values))
    return ingredients


def score(recipe):
    cap = max(sum(qty * x.capacity for x, qty in recipe), 0)
    dur = max(sum(qty * x.durability for x, qty in recipe), 0)
    flv = max(sum(qty * x.flavor for x, qty in recipe), 0)
    txt = max(sum(qty * x.texture for x, qty in recipe), 0)
    cal = max(sum(qty * x.calories for x, qty in recipe), 0)
    return (cap * dur * flv * txt, cal)  # Return calories separately


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

    max_score = 0  # Part A: Best cookie possible
    max_score_calories = 0  # Part B
    for q1 in range(0, 101):
        for q2 in range(0, 101 - q1):
            for q3 in range(0, 101 - q1 - q2):
                q4 = 100 - q1 - q2 - q3
                recipe = [(sugar, q1), (sprinkles, q2), (candy, q3), (chocolate, q4)]
                total, calories = score(recipe)
                if total > max_score:
                    max_score = total
                if total > max_score_calories and calories == 500:
                    max_score_calories = total
    print('Part A: {} - Max score of best cookie possible'.format(max_score))
    print('Part B: {} - Max score for 500 calorie cookie'.format(max_score_calories))


if __name__ == '__main__':
    main()

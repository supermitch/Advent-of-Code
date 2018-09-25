#!/usr/bin/env python
import itertools


def calc_stats(hero, items):
    hero = hero.copy()
    hero['damage'] += sum(x[2] for x in items)
    hero['armor'] += sum(x[3] for x in items)
    return hero


def hero_wins(boss, hero):
    boss, hero = boss.copy(), hero.copy()
    while True:
        # Hero attacks first
        boss['hp'] -= max(hero['damage'] - boss['armor'], 1)  # Min damage = 1
        if boss['hp'] <= 0:
            return True
        hero['hp'] -= max(boss['damage'] - hero['armor'], 1)  # Min damage = 1
        if hero['hp'] <= 0:
            return False


def cost(plan):
    costs = {
        'missile': 53, 'drain': 73, 'shield': 113,
        'poison': 173, 'recharge': 229
    }
    return sum(costs[spell] for spell in plan)


def wizard_simulator(spells, boss, hero):
    for i in itertools.count():
        plan = itertools.product(spells, repeat=i)
        if hero_wins(plan, boss.copy(), hero.copy()):  # First victory
            return cost(plan)


def main():
    boss = {'hp': 51, 'damage': 9, 'armor': 0}  # puzzle input
    hero = {'hp': 50, 'damage': 0, 'armor': 0, 'mana': 500}

    # sorted by mana cost
    spells = ['missile', 'drain', 'shield', 'poison', 'recharge']

    cheapest = wizard_simulator(spells, boss, hero)
    print('Part A: {} - Minimum mana to win'.format(cheapest))


if __name__ == '__main__':
    main()

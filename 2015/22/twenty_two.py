#!/usr/bin/env python
import collections
import itertools


def calc_stats(hero, items):
    hero = hero.copy()
    hero['damage'] += sum(x[2] for x in items)
    hero['armor'] += sum(x[3] for x in items)
    return hero


def hero_wins(plan, boss, hero):
    boss, hero = boss.copy(), hero.copy()
    effects = collections.defaultdict(int)
    for spell in plan:
        print('Casting {}'.format(spell))
        print('stats:\n{}\n{}'.format(boss, hero))

        if spell == 'missile':
            boss['hp'] -= 4
            hero['mana'] -= 53
        elif spell == 'drain':
            boss['hp'] -= 2
            hero['mana'] -= 73
            hero['hp'] += 2
        elif spell == 'shield':
            if effects['shield'] > 0:
                return False  # Can't recast an effect
            hero['mana'] -= 113
            effects['shield'] = 6
        elif spell == 'poison':
            if effects['poison'] > 0:
                return False  # Can't recast an effect
            hero['mana'] -= 173
            effects['poison'] = 6
        elif spell == 'recharge':
            if effects['recharge'] > 0:
                return False  # Can't recast an effect
            hero['mana'] -= 229
            effects['recharge'] = 5

        for key, value in effects.items():
            if value > 0:
                if key == 'shield':
                    hero['armor'] = 7
                elif key == 'poison':
                    boss['hp'] -= 3
                elif key =='recharge':
                    hero['mana'] += 101
            effects[key] -= 1

        if boss['hp'] <= 0:
            return True

        hero['hp'] -= max(boss['damage'] - hero['armor'], 1)  # Min dmg is 1
        if hero['hp'] <= 0 or hero['mana'] < 53:
            return False


def cost(plan):
    costs = {
        'missile': 53, 'drain': 73, 'shield': 113,
        'poison': 173, 'recharge': 229
    }
    return sum(costs[spell] for spell in plan)


def wizard_simulator(spells, boss, hero):
    for i in itertools.count():
        plans = itertools.product(spells, repeat=i)
        print('Repeat {}'.format(i))
        for j, plan in enumerate(plans, start=1):
            if not j % 10000:
                print('Plan {}'.format(j))
            if hero_wins(plan, boss.copy(), hero.copy()):  # First victory
                return cost(plan)


def main():
    # sorted by mana cost
    spells = ['missile', 'drain', 'shield', 'poison', 'recharge']

    boss = {'hp': 13, 'damage': 8, 'armor': 0}
    hero = {'hp': 10, 'armor': 0, 'mana': 250}
    assert wizard_simulator(spells, boss, hero) == 173 + 53

    boss = {'hp': 14, 'damage': 8, 'armor': 0}
    hero = {'hp': 10, 'armor': 0, 'mana': 250}
    assert wizard_simulator(spells, boss, hero) == 229 + 113 + 73 + 173 + 53

    boss = {'hp': 51, 'damage': 9, 'armor': 0}  # puzzle input
    hero = {'hp': 50, 'damage': 0, 'armor': 0, 'mana': 500}

    cheapest = wizard_simulator(spells, boss, hero)
    print('Part A: {} - Minimum mana to win'.format(cheapest))


if __name__ == '__main__':
    main()

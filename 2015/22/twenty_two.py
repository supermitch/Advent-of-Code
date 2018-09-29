#!/usr/bin/env python
import collections
import itertools


def apply_effects(effects, hero, boss):
    hero['armor'] = 0  # Reset armor in case effect is inactive
    for key, value in effects.items():
        if value > 0:
            if key == 'shield':
                hero['armor'] = 7
            elif key == 'poison':
                boss['hp'] -= 3
            elif key =='recharge':
                hero['mana'] += 101
            effects[key] -= 1
    return hero, boss


def hero_wins(plan, boss, hero, mode='easy'):
    boss, hero = boss.copy(), hero.copy()
    effects = collections.defaultdict(int)
    for spell in plan:
        if mode == 'hard':  # Hard mode 1st
            hero['hp'] -= 1
            if hero['hp'] <= 0:
                return False

        hero, boss = apply_effects(effects, hero, boss)  # Hero's turn effect

        if effects[spell] > 0:
            return False  # Can't recast an effect, must not be optimum

        if spell == 'missile':  # Play move 3rd
            boss['hp'] -= 4
            hero['mana'] -= 53
        elif spell == 'drain':
            boss['hp'] -= 2
            hero['mana'] -= 73
            hero['hp'] += 2
        elif spell == 'shield':
            hero['mana'] -= 113
            effects['shield'] = 6
        elif spell == 'poison':
            hero['mana'] -= 173
            effects['poison'] = 6
        elif spell == 'recharge':
            hero['mana'] -= 229
            effects['recharge'] = 5

        hero, boss = apply_effects(effects, hero, boss)  # Boss's turn effect

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


def wizard_simulator(spells, boss, hero, start=0, mode='easy'):
    for i in itertools.count(start=start):
        plans = itertools.product(spells, repeat=i)
        for j, plan in enumerate(plans, start=1):
            if hero_wins(plan, boss.copy(), hero.copy(), mode=mode):
                return cost(plan)  # Return 1st victory


def main():
    # Sorted by mana cost!
    spells = ['missile', 'drain', 'shield', 'poison', 'recharge']

    boss = {'hp': 13, 'damage': 8, 'armor': 0}
    hero = {'hp': 10, 'armor': 0, 'mana': 250}
    plan = ['poison', 'missile']
    assert hero_wins(plan, boss, hero)

    boss = {'hp': 14, 'damage': 8, 'armor': 0}
    hero = {'hp': 10, 'armor': 0, 'mana': 250}
    plan = ['recharge', 'shield', 'drain', 'poison', 'missile']
    assert hero_wins(plan, boss, hero)

    boss = {'hp': 51, 'damage': 9, 'armor': 0}  # Puzzle input
    hero = {'hp': 50, 'damage': 0, 'armor': 0, 'mana': 500}

    cheapest = wizard_simulator(spells, boss, hero, start=8)
    print('Part A: {} - Minimum mana to win, Easy mode'.format(cheapest))

    cheapest = wizard_simulator(spells, boss, hero, start=8, mode='hard')
    print('Part B: {} - Minimum mana to win, Hard mode'.format(cheapest))


if __name__ == '__main__':
    main()

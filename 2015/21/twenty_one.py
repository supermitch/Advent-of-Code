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


def main():
    boss = {'hp': 103, 'damage': 9, 'armor': 2}
    hero = {'hp': 100, 'damage': 0, 'armor': 0}

    # Items: (Name, cost, damage, armor)
    weapons = [
        ('Dagger', 8, 4, 0),
        ('Shortsword', 10, 5, 0),
        ('Warhammer', 25, 6, 0),
        ('Longsword', 40, 7, 0),
        ('Greataxe', 74, 8, 0),
    ]
    armor = [
        ('No armour', 0, 0, 0),
        ('Leather', 13, 0, 1),
        ('Chainmail', 31, 0, 2),
        ('Splintmail', 53, 0, 3),
        ('Bandedmail', 75, 0, 4),
        ('Platemail', 102, 0, 5),
    ]
    rings = [
        ('No ring', 0, 0, 0),
        ('Damage+1', 25, 1, 0),
        ('Damage+2', 50, 2, 0),
        ('Damage+3', 100, 3, 0),
        ('Defense+1', 20, 0, 1),
        ('Defense+2', 40, 0, 2),
        ('Defense+3', 80, 0, 3),
    ]
    left_ring = rings[:]
    right_ring = rings[:]

    equipment = itertools.product(weapons, armor, left_ring, right_ring)

    cheapest = 999
    expensive = 0
    for items in equipment:
        if items[2][0] != 'No ring' and items[2][1] == items[3][1]:
            continue  # Can't have two of the same ring

        cost = sum(item[1] for item in items)

        hero_stats = calc_stats(hero, items)

        if hero_wins(boss, hero_stats) and cost <= cheapest:
            cheapest = cost
        elif not hero_wins(boss, hero_stats) and cost >= expensive:
            expensive = cost

    print('Part A: {} - Minimum cost to win'.format(cheapest))
    print('Part B: {} - Maximum cost and still lose'.format(expensive))


if __name__ == '__main__':
    main()

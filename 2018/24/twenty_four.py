#!/usr/bin/env python
class Group:
    def __init__(
        self, side, id, units, hp, immunes, weaks, attack, kind, initiative
        ):
        self.side = side
        self.id = id
        self.units = units
        self.hp = hp
        self.immunes = immunes
        self.weaks = weaks
        self.attack = attack
        self.kind = kind
        self.initiative = initiative
        self.attacker = None
        self.target = None
        self.damage = None

    def __str__(self):
        return f'{self.side}-{self.id}: {self.units} units, {self.hp} hp)'

    @property
    def power(self):
        return self.units * self.attack

def parse_army(f, side, lines, offset=0):
    army = []
    for g in range(lines):
        line = f.readline().replace('(', ' ').split()
        immunes = []
        if 'immune' in line:
            for i in range(line.index('immune') + 2, len(line)):
                immunes.append(line[i].replace(')', '').replace(';', '').replace(',', ''))
                if ';' in line[i] or ')' in line[i]:
                    break
        weaks = []
        if 'weak' in line:
            for i in range(line.index('weak') + 2, len(line)):
                weaks.append(line[i].replace(')', '').replace(';', '').replace(',', ''))
                if ';' in line[i] or ')' in line[i]:
                    break
        army.append(Group(
            side,
            offset + g + 1,
            int(line[0]),
            int(line[4]),
            immunes,
            weaks,
            int(line[line.index('does') + 1]),
            line[line.index('does') + 2],
            int(line[-1]),
        ))
    return army


def read_input(path):
    lines = -2
    with open(path) as f:
        for line in f:
            lines += 1
            if not line.strip():
                break

    with open(path) as f:
        f.readline()  # Header
        immune = parse_army(f, 'immune', lines=lines)
        f.readline()
        f.readline()  # Header
        infection = parse_army(f, 'infection', lines=lines, offset=lines)
    return immune, infection


def find_target(groups, target):
    for group in groups:
        if group.id == target:
            return group


def calc_damage(defender, attacker):
    if attacker.kind in defender.immunes:
        return 0
    elif attacker.kind in defender.weaks:
        return attacker.power * 2
    else:
        return attacker.power


def boost(groups, value):
    for g in groups:
        g.attack += value


def fight_battle(path, boost_value=0):
    immune, infection = read_input(path)
    boost(immune, boost_value)  # Apply attack boost to immune groups
    groups = immune + infection

    while True:
        groups = [g for g in groups if g.units > 0]

        # Select phase
        for group in groups:
            group.target = None
            group.attacker = None
            group.damage = None
        groups = sorted(groups, key=lambda x: x.initiative, reverse=True)
        groups = sorted(groups, key=lambda x: x.power, reverse=True)

        for attacker in groups:
            targets = [g for g in groups if g.side != attacker.side and g.attacker is None]
            for defender in targets:
                if defender.attacker is None:  # Not spoken for
                    defender.damage = calc_damage(defender, attacker)
            targets = sorted(targets, key=lambda x: x.initiative, reverse=True)
            targets = sorted(targets, key=lambda x: x.power, reverse=True)
            targets = sorted(targets, key=lambda x: x.damage, reverse=True)
            targets = [t for t in targets if t.damage > 0]
            #print('attacker', attacker.side, attacker.id)
            #print([(t.side, t.id, t.damage) for t in targets])
            if targets:
                target = targets[0]
                attacker.target = target.id
                target.attacker = attacker.id

        # Attack phase
        total_loss = 0
        groups = sorted(groups, key=lambda x: x.initiative, reverse=True)
        for attacker in groups:
            if attacker.units <= 0:  # Can't attack
                continue
            #print('Attacker:', attacker)
            target = find_target(groups, attacker.target)
            if target:
                #print('Target:', target)
                damage = calc_damage(target, attacker)
                #print(f'Attacker units: {attacker.units}')
                loss = min(damage // target.hp, target.units)
                #print(f'Damage: {damage} target.hp: {target.hp} Loss: {loss}')
                target.units -= loss
                total_loss += loss
            sides = set([g.side for g in groups])
            if len(sides) == 1:
                winner = sides.pop()
                army = sum(g.units for g in groups \
                        if g.units >= 0 and g.side == winner)
                return army, winner == 'immune'
        if total_loss <= 0:
            return None, False  # Deadlocked battlw


def main():
    # Part A b
    units, healthy = fight_battle('input.txt')
    print(f'Part A {units} - Number of winning units remaining after battle')
    # Part B is easy but the battle deadlocks.
    boost = 0
    while True:
        units, healthy = fight_battle('input.txt', boost)
        if healthy:
            break
        boost += 1
    print(f'Part B {boost} - Boost required for immune system to win')


if __name__ == '__main__':
    main()

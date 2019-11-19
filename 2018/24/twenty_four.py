#!/usr/bin/env python
import itertools


class Group:
    def __init__(
        self,
        side, _id, units, hp, immunes, weaks, attack, kind, initiative, boost
        ):
        self.side = side
        self.id = _id
        self.units = units
        self.hp = hp
        self.immunes = immunes
        self.weaks = weaks
        self.attack = attack + boost
        self.kind = kind
        self.initiative = initiative
        self.targeted = False
        self.target = None
        self.damage = None

    @property
    def power(self):
        return self.units * self.attack

    def calc_damage(self, defender):
        """ How much damage would occur if we attacked this defender? """
        if self.kind in defender.immunes:
            return 0
        elif self.kind in defender.weaks:
            return self.power * 2
        else:
            return self.power


def parse_effects(parts, kind):
    """ Parse immunities and weaknesses. """
    if not kind in parts:
        return []
    effects = []
    for i in range(parts.index(kind) + 2, len(parts)):
        effects.append(parts[i].replace(')', '').replace(';', '').replace(',', ''))
        if ';' in parts[i] or ')' in parts[i]:
            return effects


def parse_army(f, side, boost, offset=0):
    army = []
    for i in itertools.count(offset):
        line = f.readline().strip()
        if not line:
            return army
        if not 'units' in line:
            continue
        parts = line.replace('(', '').split()
        immunes = parse_effects(parts, 'immune')
        weaks = parse_effects(parts, 'weak')
        army.append(Group(side, i + 1,
            int(parts[0]),
            int(parts[4]),
            immunes,
            weaks,
            int(parts[parts.index('does') + 1]),
            parts[parts.index('does') + 2],
            int(parts[-1]),
            boost
        ))
    return army


def read_input(path, boost):
    with open(path) as f:
        immune = parse_army(f, 'immune', boost)
        infection = parse_army(f, 'infection', 0, offset=len(immune))
    return immune + infection


def fight_battle(path, boost):
    groups = read_input(path, boost)

    while True:
        groups = [g for g in groups if g.units > 0]

        # Select phase
        for group in groups:
            group.target = None
            group.targeted = False
            group.damage = None
        groups = sorted(
            groups, key=lambda x: (x.power, x.initiative), reverse=True
        )
        for attacker in groups:
            targets = [g for g in groups if g.side != attacker.side and not g.targeted]
            for defender in targets:
                if not defender.targeted:
                    defender.damage = attacker.calc_damage(defender)
            targets = sorted(
                targets,
                key=lambda x: (x.damage, x.power, x.initiative),
                reverse=True
            )
            targets = [t for t in targets if t.damage > 0]
            if targets:
                target = targets[0]
                attacker.target = target
                target.targeted = True

        # Attack phase
        total_loss = 0
        groups = sorted(groups, key=lambda x: x.initiative, reverse=True)
        for attacker in groups:
            if attacker.units <= 0:  # Lost units during this battle
                continue
            target = attacker.target
            if target:
                damage = attacker.calc_damage(target)
                loss = min(damage // target.hp, target.units)
                target.units -= loss
                total_loss += loss
            sides = set([g.side for g in groups])
            if len(sides) == 1:
                winner = sides.pop()
                army = sum(g.units for g in groups if g.side == winner)
                return army, winner == 'immune'
        if total_loss <= 0:  # Deadlocked battle
            return None, False


def main():
    for boost in itertools.count():
        units, healthy = fight_battle('input.txt', boost)
        if boost == 0:
            print(f'Part A {units} - Units remaining after battle')
        if healthy:
            print(f'Part B {boost} - Boost required for immune system to win')
            return


if __name__ == '__main__':
    main()

#!/usr/bin/env python
def parse_army(f, side, lines=10, offset=0):
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
        army.append({
            'side': side,
            'id': offset + g + 1,
            'units': int(line[0]),
            'hp': int(line[4]),
            'immunes': immunes,
            'weaks': weaks,
            'damage': int(line[line.index('does') + 1]),
            'kind': line[line.index('does') + 2],
            'initiative': int(line[-1]),
        })
    return army

def read_input():
    fname = 'test.txt'
    lines = 2
    with open(fname) as f:
        f.readline()  # Header
        immune = parse_army(f, 'immune', lines=lines)
        f.readline()
        f.readline()  # Header
        infection = parse_army(f, 'infection', lines=lines, offset=lines)
    return immune, infection

def set_attacker(groups, target, attacker):
    for group in groups:
        if group['id'] == target:
            group['attacker'] == attacker
            return

def find_target(groups, target):
    for group in groups:
        if group['id'] == target:
            return group

def calc_damage(defender, attacker):
    attacker['power'] = attacker['units'] * attacker['damage']
    if attacker['kind'] in defender['immunes']:
        print('immune!')
        return 0
    elif attacker['kind'] in defender['weaks']:
        print('weakness!')
        return attacker['power'] * 2
    else:
        print('regular')
        return attacker['power']

def army_won(groups):
    i = set([g['side'] for g in groups])

def main():
    immune, infection = read_input()
    groups = immune + infection
    i = 0
    game_over = False
    while True:
        if game_over:
            break
        i += 1

        groups = [g for g in groups if g['units'] >= 0]

        print(i, len(groups))
        # Select phase
        for group in groups:
            group['power'] = group['units'] * group['damage']
            group['target'] = None
            group['attacker'] = None
            group['dmg'] = None
        groups = sorted(groups, key=lambda x: x['initiative'], reverse=True)
        groups = sorted(groups, key=lambda x: x['power'], reverse=True)

        for curr in groups:
            targets = [g for g in groups if g['side'] != curr['side'] and g['attacker'] is None]
            for group in targets:
                if group['attacker'] is None:  # Not spoken for
                    group['dmg'] = calc_damage(group, curr)
            targets = sorted(targets, key=lambda x: x['initiative'], reverse=True)
            targets = sorted(targets, key=lambda x: x['power'], reverse=True)
            targets = sorted(targets, key=lambda x: x['dmg'], reverse=True)
            targets = [t for t in targets if t['dmg'] > 0]
            print('curr', curr['side'], curr['id'])
            print([(t['side'], t['id'], t['dmg']) for t in targets])
            if targets:
                target = targets[0]
                curr['target'] = target['id']
                set_attacker(groups, target['id'], curr['id'])

        # Attack phase
        groups = sorted(groups, key=lambda x: x['initiative'], reverse=True)
        for group in groups:
            if group['units'] <= 0:  # Can't attack
                continue
            print('attacker:', group)
            target = find_target(groups, group['target'])
            if target:
                print('target:', target)
                damage = calc_damage(target, group)
                loss = damage // target['hp']
                target['units'] -= loss
                print('damage:', damage, 'loss:', loss)
            sides = set([g['side'] for g in groups])
            print(sides)
            if len(sides) == 1:
                winner = sides.pop()
                army = sum(g['units'] for g in groups \
                        if g['units'] >= 0 and g['side'] == winner)
                print(army)
                game_over = True
                break







if __name__ == '__main__':
    main()

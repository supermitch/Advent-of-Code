#!/usr/bin/env python
from collections import defaultdict
from itertools import permutations

class Obj:
    def __init__(self, x, y, kind, power=3):
        self.x = x
        self.y = y
        self.hp = 200
        self.power = power
        self.dead = False
        self.kind = kind
        self.acted = False


def reading(arr):
    arr = [c for c in arr if not c.dead]
    arr = sorted(arr, key=lambda c: c.y)
    arr = sorted(arr, key=lambda c: c.x)
    return arr

def sort_goals(arr):
    arr = sorted(arr, key=lambda c: c[1])
    arr = sorted(arr, key=lambda c: c[0])
    return arr


def adjacent(p, xs):
    adj = []
    for x in xs:
        if x.dead: continue
        if p.kind == x.kind: continue
        if x.x == p.x and x.y == p.y: continue  # Self
        if x.x == p.x:
            if x.y == p.y + 1 or x.y == p.y - 1:
                adj.append(x)
        elif x.y == p.y:
            if x.x == p.x + 1 or x.x == p.x - 1:
                adj.append(x)
    return adj

def neighbors(coord, grid):
    x, y = coord
    nb = []
    ds = [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]
    for d in ds:
        if grid[d] == '.':
            nb.append(d)
    return nb

def occupied(c, players):
    return any(p.x == c[0] and p.y == c[1] for p in players if not p.dead)

def parse(data, power):
    grid = {}
    objs = []
    for x, l in enumerate(data):
        for y, c in enumerate(l):
            grid[(x,y)] = c
            if c == 'E':
                grid[(x,y)] = '.'
                objs.append(Obj(x, y, c, power))
            elif c == 'G':
                grid[(x,y)] = '.'
                objs.append(Obj(x, y, c))
    return grid, objs

def read_input(fname, power):
    with open(fname + '.txt') as f:
        return parse([l.strip() for l in f], power)

def find_goals(grid, i, players):
    goals = []
    for x in players:
        if x.dead: continue
        if i.kind == x.kind: continue
        if x.x == i.x and x.y == i.y: continue
        targets = [(x.x - 1, x.y), (x.x, x.y - 1), (x.x, x.y + 1), (x.x + 1, x.y)]
        for t in targets:
            if grid[t] == '#': continue
            if occupied(t, players): continue
            goals.append(t)
    return goals

def find_move(grid, i, players):
    initial = i.x, i.y
    visited = {initial: 0}
    path = {}
    nodes = set([k for k, v in grid.items() if v == '.'])

    while nodes:
        min_node = None
        for node in sort_goals(nodes):
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        opts = [c for c in neighbors(min_node, grid) if not occupied(c, players)]
        for edge in sort_goals(opts):
            weight = current_weight + 1
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return path

def draw(grid, players):
    size = 32
    size = 6
    for x in range(size + 1):
        line = ''
        for y in range(size + 1):
            for p in players:
                if p.dead:
                    continue
                if p.x == x and p.y == y:
                    line += p.kind
                    break
            else:
                if (x, y) in grid:
                    line += grid[(x,y)]
                else:
                    line += ' '
        print(line)

def extract_steps(curr, g, path):
    if g not in path:
        return []
    steps = [g]
    while True:
        steps.append(path[g])
        g = path[g]
        if g == curr:
            break
    return steps

def main():
    print('\nFifteen')
    power = 19
    grid, objs = read_input('input', power)

    game_over = False
    t = 0
    while True:
        players = reading(objs)

        for player in players:
            player.acted = False
            if player.dead: continue
            adj = adjacent(player, players)
            if adj:  # attack
                adj = reading(adj)  # Second sort by reading coord
                adj = sorted(adj, key=lambda a: a.hp)  # First sort by hp
                adj[0].hp -= player.power
                if adj[0].hp <= 0:
                    adj[0].dead = True
            else:  # move
                goals = sort_goals(find_goals(grid, player, players))
                min_path = 999999
                min_step = None
                for g in goals:
                    path = find_move(grid, player, players)
                    curr = player.x, player.y
                    steps = extract_steps(curr, g, path)
                    if not steps:
                        continue
                    if len(steps) < min_path:
                        min_path = len(steps)
                        min_step = steps[-2]
                if min_step is None:
                    continue
                player.x = min_step[0]
                player.y = min_step[1]
                adj = adjacent(player, players)
                if adj:  # attack
                    adj = reading(adj)  # Second sort by reading coord
                    adj = sorted(adj, key=lambda a: a.hp)  # First sort by hp
                    adj[0].hp -= player.power
                    if adj[0].hp <= 0:
                        adj[0].dead = True
            player.acted = True
            if any(p for p in players if p.kind == 'E' and p.dead):
                print('Elf died w/ power ', power)
                game_over = True
                return

            if len([p for p in players if p.kind == 'E' and not p.dead]) == 0 \
                    or len([p for p in players if p.kind == 'G' and not p.dead]) == 0:
                print('Game over')
                game_over = True
        if all(p.acted for p in players if not p.dead):
            full_round = True
        else:
            full_round = False
        t += 1
        if game_over:
            break

    if not full_round:
        t -= 1
    print('Round:', t)
    print('Full round:', full_round)
    total_hp = sum(p.hp for p in players if p.hp > 0)
    print('total hp', total_hp)
    # 223641 too high (81 * 2761)
    # 220880 too high (80 * 2761)

if __name__ == '__main__':
    main()

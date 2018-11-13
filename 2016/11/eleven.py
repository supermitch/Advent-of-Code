#!/usr/bin/env python


class Facility:
    def __init__(self, layout):
        self.count = 0  # Initialize total part count
        self.parse(layout)

    def parse(self, layout):
        self.floors = []
        for i, parts in enumerate(layout):
            floor = Floor()
            for part in parts:
                if part == 'E':
                    self.elevator = i  # Current Elevator position
                else:
                    obj = Part(part)
                    floor.add(obj)
                    self.count += 1  # Total number of parts
            self.floors.append(floor)

    def complete(self):
        """ Are all parts on the top floor? """
        return len(self.floors[-1].parts) == self.count

    def operate(self):
        steps = 0
        return steps

    def __str__(self):
        contents = []
        for i, floor in enumerate(self.floors):
            contents.append(str(floor))
            if self.elevator == i:
                contents[-1] = 'E ' + contents[-1]
        return '\n'.join(contents)


class Floor:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def has_pair(self):
        """ Does this floor have a matching Generator & Microchip? """
        seen = set()
        for part in self.parts:
            if part.element in seen:
                return True
            seen.add(part.element)
        return False

    def __str__(self):
        return ' '.join(str(p) for p in self.parts)


class Part:
    """ A Generator, or a Microchip. """
    def __init__(self, part):
        self.parse(part)

    def parse(self, part):  # e.g. 'G-Pr'
        self.kind = part[0]  # e.g. 'G'
        self.element = part.strip()[2:]  # e.g. 'Pr'

    def __str__(self):
        return '{}-{}'.format(self.kind, self.element)


def main():
    """
    Goal: Get everything to 4th floor
    Rules:
    - Two objects max in elevator
    - One object min in elevator
    - Generators (G) will fry Microchips (M) unless they are the same type
    - Gx + Mx of same type means Mx is shielded from other G's
    - G has no effect on other G
    - M has no effect on other M
    """
    test = [
        ['E', 'M-H', 'M-L'],  # Ground floor
        ['G-H'],
        ['G-L'],
        [],
    ]
    facility = Facility(test)
    print(facility)
    return
    assert facility.operate() == 11

    layout = [
        ['E', 'G-Pr', 'M-Pr'],  # Ground floor
        ['G-Co', 'G-Cu', 'G-Ru', 'G-Pl'],
        ['M-Co', 'M-Cu', 'M-Ru'],
        [],
    ]
    facility = Facility(layout)
    print(facility)
    steps = facility.operate()

    print('Part A: {} - '.format(steps))
    print('Part B: {} - '.format(None))


if __name__ == '__main__':
    main()

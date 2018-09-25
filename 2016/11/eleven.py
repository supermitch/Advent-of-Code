#!/usr/bin/env python


def find_elevator(layout):
    for i, floor in enumerate(layout):
        if 'E' in floor:
            return i


def complete(layout):
    return not any(floor for floor in layout[:-1])  # All items on floor 4


def operate(layout):
    steps = 0
    e = find_elevator(layout)
    print(e)

    return steps


def main():
    """
    Goal: Get everything to 4th floor

    Rules:
    - Two objects max in elevator
    - One object min in elevator
    - Generators (G) will fry Micorchips (M) unless they are the same type
    - Gx + Mx of same type means Mx is shielded from other G's
    - G has no effect on other G
    - M has no effect on other M

    """
    test = [
        ['E', 'Mh', 'Ml'],
        ['Gh'],
        ['Gl'],
        [],
    ]

    steps = operate(test)

    layout = [
        ['E', 'Gpr', 'Mpr'],  # 0 is ground floor
        ['Gco', 'Gcu', 'Gru', 'Gpl'],
        ['Mco', 'Mcu', 'Mru'],
        [],
    ]
    print('Part A: {} - '.format(None))
    print('Part B: {} - '.format(None))


if __name__ == '__main__':
    main()

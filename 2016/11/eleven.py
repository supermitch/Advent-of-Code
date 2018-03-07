def main():
    """
    Goal: Get everything to 4th floor

    Rules:
    - Two objects max in elevator
    - One object min in elevator
    - G will fry M unless they are the same type
    - G + matching M means M is shielded from other G
    - G has no effect on other G
    - M has no effect on other M

    """
    layout = {
        4: [],
        3: ['Mco', 'Mcu', 'Mru'],
        2: ['Gco', 'Gcu', 'Gru', 'Gpl'],
        1: ['E',   'Gpr', 'Mpr'],
    }
    test = {
        4: [],
        3: ['LG'],
        2: ['HG'],
        1: ['E', 'HM', 'LM'],
    }
    print('Part A: {} - '.format(None))
    print('Part B: {} - '.format(None))


if __name__ == '__main__':
    main()

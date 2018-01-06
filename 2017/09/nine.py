def main():
    with open('input.txt', 'r') as f:
        data = f.read().strip()

    garbage_stack = 0
    group_stack = 0
    ignore = False
    group_count = 0
    garbage_count = 0
    for c in data:
        if ignore:
            ignore = False
            continue  # Skip this char

        if garbage_stack:
            if c == '>':
                garbage_stack -= 1  # Pop
            elif c == '!':
                ignore = True
            else:
                garbage_count += 1  # Found garbage char
        else:
            if c == '<':
                garbage_stack += 1
            elif c == '{':
                group_stack += 1
            elif c == '}' and group_stack:
                group_count += group_stack
                group_stack -= 1  # Pop
            elif c == '!':
                ignore = True
            else:
                print('Bad c: <{}>'.format(c))

    print('Part A: {} - No. of closed groups'.format(group_count))
    print('Part B: {} - No. of garbage chars'.format(garbage_count))


if __name__ == '__main__':
    main()

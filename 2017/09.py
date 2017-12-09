def main():
    with open('09.input', 'r') as f:
        data = f.read().strip()

    count = 0
    garbage = 0
    group = 0
    ignore = False
    garbage_count = 0
    for c in data:
        if ignore:
            ignore = False
            continue

        if garbage:
            if c == '>':
                garbage -= 1
            elif c == '!':
                ignore = True
            else:
                garbage_count += 1
        else:
            if c == '<':
                garbage += 1
            elif c == '{':
                group += 1
            elif c == '}' and group:
                count += group
                group -= 1
            elif c == '!':
                ignore = True
            else:
                print('Bad c: <{}>'.format(c))

    print('Part A: {} - No. of closed groups'.format(count))
    print('Part B: {} - No. of garbage chars'.format(garbage_count))


if __name__ == '__main__':
    main()

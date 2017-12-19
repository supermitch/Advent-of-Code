import string


def rotate(v, rotation):
    if rotation == 'L':  # Positive 90 deg
        return -v[1], v[0]
    else:
        return v[1], -v[0]


def make_turn(data, pos, dir):
    x, y = pos
    new_dir = rotate(dir, 'L')  # Try left
    dx, dy = new_dir
    nx, ny = x + dx, y + dy
    if data[nx][ny] in '|-' + string.ascii_letters:
        return new_dir
    else:
        return rotate(dir, 'R')


def main():
    data = []
    with open('19.input', 'r') as f:
        for line in f:
            data.append(list(line.strip('\n')))

    x, y = 0, data[0].index('|')
    dir = (1, 0)  # Starting dir is downwards

    seen = ''  # Seen alphabetical chars
    steps = 0  # Step count
    while True:
        char = data[x][y]
        if char == '+':
            dir = make_turn(data, (x, y), dir)
        elif char in '|-':
            pass  # Just keep swimming
        elif char in string.ascii_letters:
            seen += char
        elif char == ' ':
            break
        dx, dy = dir
        x, y = x + dx, y + dy
        steps += 1

    print('Part A: {} - Letters seen'.format(seen))
    print('Part B: {} - No. of steps'.format(steps))


if __name__ == '__main__':
    main()

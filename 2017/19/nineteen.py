import string


def rotate(v, rotation):
    return (-v[1], v[0]) if rotation == 'L' else (v[1], -v[0])


def make_turn(data, x, y, dir):
    dx, dy = rotate(dir, 'L')  # Try left first
    new_x, new_y = x + dx, y + dy
    if data[new_x][new_y] in '|-' + string.ascii_letters:  # Valid path
        return dx, dy
    else:
        return rotate(dir, 'R')


def main():
    with open('input.txt', 'r') as f:
        data = [list(line.strip('\n')) for line in f]

    x, y = 0, data[0].index('|')  # Start position
    dir = (1, 0)  # Starting dir is downwards, call it +ve x-axis

    seen = ''  # Seen letters
    steps = 0  # Step count
    while True:
        char = data[x][y]
        if char == '+':
            dir = make_turn(data, x, y, dir)
        elif char in string.ascii_letters:  # Includes uppercase
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

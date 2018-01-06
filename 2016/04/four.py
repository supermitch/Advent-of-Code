from collections import Counter


def parse(line):
    room, check = line.strip().strip(']').split('[')
    sector = int(room.split('-')[-1])
    string = [c for c in room if c not in '-1234567890']
    return string, check, sector, room


def find_rooms(data):
    rooms = []
    for string, check, sector, room in data:
        c = Counter(string)
        top = sorted(c.most_common(), key=lambda x:x[0])  # Second sort by letter
        top = sorted(top, key=lambda x:x[1], reverse=True)  # First sort by count
        if ''.join(x[0] for x in top[:5]) == check:
            rooms.append((string, sector, room))
    return rooms


def decrypt_name(words, sector):
    out = []
    for word in words:
        new = []
        for c in word:
            o = ord(c) - ord('a')
            o = (o + sector) % 26  # Rotate each char by 'sector'
            new.append(chr(o + ord('a')))
        out.append(''.join(new))
    return out


def main():
    with open('input.txt', 'r') as f:
        data = [parse(line) for line in f]

    rooms = find_rooms(data)
    sector_sum = sum(sector for _, sector, _ in rooms)
    print('Part A: {} - Sector sum'.format(sector_sum))

    for _, sector, room in rooms:
        parts = room.split('-')[:-1]
        if 'northpole' in decrypt_name(parts, sector):
            print('Part B: {} - North Pole room sector ID'.format(sector))


if __name__ == '__main__':
    main()

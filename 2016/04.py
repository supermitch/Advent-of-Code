from collections import Counter


def find_rooms(data):
    rooms = []
    for string, check, sector, room in data:
        c = Counter(string)
        top = sorted(c.most_common(), key=lambda x:x[0])  # Second sort by letter
        top = sorted(top, key=lambda x:x[1], reverse=True)  # First sort by count
        if ''.join(x[0] for x in top[:5]) == check:
            rooms.append((string, sector, room))
    return rooms


def decrypt_name(room, sector):
    out = []
    for c in room:
        if c == '-':
            out.append(' ')
            continue
        o = ord(c)
        o += sector
        o = o % 26
        out.append(chr(o))

    return ''.join(out)

def main():
    with open('04.input', 'r') as f:
        data = []
        for line in f:
            room, check = line.strip().split('[')
            sector = int(room.split('-')[-1])
            string = [c for c in room if c not in '-1234567890']
            check = check[:-1]
            data.append((string, check, sector, room))


    rooms = find_rooms(data)
    sector_sum = sum(sector for _, sector, _ in rooms)
    print('Part A: {} - Sector sum'.format(sector_sum))

    for string, sector, room in rooms:
        print(decrypt_name(room, sector))

    print('Part B: {} - No. of valid triangles by column'.format(None))


if __name__ == '__main__':
    main()

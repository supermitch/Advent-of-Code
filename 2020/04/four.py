#!/usr/bin/env python


def main():
    data = []
    with open('input.txt', 'r') as f:
        ppt = []
        for line in f:
            ppt.extend(line.strip().split())
            if line == '\n':
                data.append(ppt)
                ppt = []
        ppt.extend(line.strip().split())
        data.append(ppt)

    part_a = 0
    part_b = 0
    REQUIRED = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

    for ppt in data:
        fields = [x.split(':')[0] for x in ppt]
        if not all(x in fields for x in REQUIRED):
            continue

        part_a += 1

        valid = True
        for key in ppt:
            val = key.split(':')[1]
            if key.startswith('byr'):
                if int(val) < 1920 or int(val) > 2002:
                    valid = False
            elif key.startswith('iyr'):
                if int(val) < 2010 or int(val) > 2020:
                    valid = False
            elif key.startswith('eyr'):
                if int(val) < 2020 or int(val) > 2030:
                    valid = False
            elif key.startswith('hgt'):
                units = val[-2:]
                val = val[:-2]
                if units == 'cm':
                    if int(val) < 150 or int(val) > 193:
                        valid = False
                elif units == 'in':
                    if int(val) < 59 or int(val) > 76:
                        valid = False
                else:  # Bad entry
                    valid = False
            elif key.startswith('hcl'):
                if not len(val) == 7:
                    valid = False
                if not val.startswith('#'):
                    valid = False
                if not all(x in ('0123456789abcdef') for x in val[1:]):
                    valid = False
            elif key.startswith('ecl'):
                if val not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                    valid = False
            elif key.startswith('pid'):
                if len(val) != 9 or not val.isnumeric():
                    valid = False
            if not valid:
                break
        if valid:
            part_b += 1

    print(f'Part A: {part_a} - Passports w/ valid fields')
    print(f'Part B: {part_b} - Valid passports')


if __name__ == '__main__':
    main()

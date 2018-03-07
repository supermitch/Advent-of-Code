import json


def traverse(obj, total, red_is_bad):
    if isinstance(obj, str):
        return 0
    elif isinstance(obj, int):
        return obj
    elif isinstance(obj, list):
        for o in obj:
            total += traverse(o, 0, red_is_bad)
        return total
    else:  # dict
        if red_is_bad and 'red' in obj.values():
            return 0  # This obj & children are not counted
        else:
            for k, o in obj.items():
                total += traverse(o, 0, red_is_bad)
        return total


def main():
    test = {'j': {'a': 'orange', 'b': 'blue', 'c': {'t': 'red', 'j': 55}, 'd': 'violet', 'e': 133}, 'b': [1, 'cat', 2], 'c': 23}
    assert(traverse(test, 0, False) == 214)
    assert(traverse(test, 0, True) == 159)

    with open('input.txt', 'r') as f:
        contents = list(f)
    obj = json.loads(''.join(contents))

    part_a = traverse(obj, 0, False)
    print('Part A: {} - Sum of all number values'.format(part_a))

    part_b = traverse(obj, 0, True)
    print('Part B: {} - Sum w/o red properties'.format(part_b))


if __name__ == '__main__':
    main()

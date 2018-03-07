import json


def traverse(obj, red_is_bad):
    if isinstance(obj, str):
        return 0
    elif isinstance(obj, int):
        return obj
    elif isinstance(obj, list):
        return sum(traverse(o, red_is_bad) for o in obj)
    else:  # dict
        if red_is_bad and 'red' in obj.values():
            return 0  # This obj & children are not counted
        else:
            return sum(traverse(o, red_is_bad) for o in obj.values())


def main():
    test = {
        'j': {
            'a': 'orange',
            'b': 'blue',
            'c': {
                't': 'red', 'j': 55
            },
            'd': 'violet',
            'e': 133},
        'b': [1, 'cat', 2],
        'c': 23
    }
    assert(traverse(test, False) == 214)
    assert(traverse(test, True) == 159)

    with open('input.txt', 'r') as f:
        obj = json.loads(f.read())

    part_a = traverse(obj, False)
    print('Part A: {} - Sum of all number values'.format(part_a))

    part_b = traverse(obj, True)
    print('Part B: {} - Sum w/o red properties'.format(part_b))


if __name__ == '__main__':
    main()

import hashlib


def get_doors(input):
    doors = {'U': False, 'D': False, 'R': False, 'L': False}
    hash = hashlib.md5(input.encode()).hexdigest()
    for dir, char in zip('UDLR', hash[:4]):
        if char in 'bcdef':
            doors[dir] = True
    return doors


def main():
    maze = """
        #########
        #S| | | #
        #-#-#-#-#
        # | | | #
        #-#-#-#-#
        # | | | #
        #-#-#-#-#
        # | | |
        ####### V
    """
    assert get_doors('hijkl') == {'U': True, 'D': True, 'L': True, 'R': False}
    assert get_doors('hijklDR') == {'U': False, 'D': False, 'R': False, 'L': False}

    input = 'yjjvjgan'
    print(input)



if __name__ == '__main__':
    main()

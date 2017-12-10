def part_a():
    pass

def run_round(pos, skip, arr, input):
    for l in input:
        end = pos + l
        if end > len(arr):
            suf_len = len(arr) - pos
            end = end % len(arr)
            pre_len = end

            suffix = arr[pos:]
            prefix = arr[:end]
            sub = suffix + prefix
            sub.reverse()
            arr = sub[suf_len:] + arr[end:pos] + sub[:suf_len]
        else:
            sub = arr[pos:end]
            sub.reverse()
            arr = arr[:pos] + sub + arr[end:]

        pos += l + skip
        pos = pos % len(arr)
        skip += 1
    return arr, pos, skip

def main(arr, input):


    pos = 0
    skip = 0

    out, pos, skip = run_round(pos, skip, arr, input)

    print('Part A: {} - '.format(arr[0] * arr[1]))


def xor(l):
    a = l[0]
    for b in l[1:]:
        a = a ^ b
    return a

def to_hex(res):
    h = [hex(x)[2:] for x in res]
    return h

if __name__ == '__main__':
    arr = list(range(5))
    input = [3,4,1,5]
    main(arr, input)

    arr = list(range(0,256))
    input = [46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204]
    main(arr, input)


    def max_hash(input):
        input = [ord(str(l)) for l in input]
        print(input)
        length = input + [17,31,73,47,23]
        print(length)

        arr = list(range(0,256))
        pos = 0
        skip = 0
        sparse = arr[:]
        for _ in range(64):
            sparse, pos, skip = run_round(pos, skip, sparse, length)
        print('Sparse hash:', sparse)
        print('Length: {}'.format(len(sparse)))

        dense = []
        for i in range(16):
            b = sparse[i * 16 :(i + 1) * 16]
            a = xor(b)
            dense.append(a)
        print('dense hash: ', dense)
        print('Length: {}'.format(len(dense)))

        h = to_hex(dense)
        padded = []
        for i in h:
            if len(i) < 2:
                padded.append('0' + i)
            else:
                padded.append(i)
        return ''.join(padded)

    print(max_hash('AoC 2017'))
    print(max_hash('1,2,3'))
    print(max_hash('46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204'))
    #print('Part B: {} - '.format())

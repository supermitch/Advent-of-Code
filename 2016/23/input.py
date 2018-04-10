b = a  # cpy a b
b -= 1  # dec b
d = a  # cpy a d
a = 0  # copy 0 a
while True: c = b  # copy b c
    while True: a += 1  # inc a
        c -= 1  # dec c
        if c <= 0: break  # jnz c -2
    d -= 1  # dec d
    if d <= 0: break  # jnz d -5
b -= 1  # dec b
c = b  # copy b c
d = c  # cpy c d
while True: d -= 1  # dec d
    c += 1  # inc c
    if d <= 0: break  # jnz d -2  d = 0
tgl c
c = -16  # cpy -16 c
pass # jnz 1 c
c = 84  # cpy 84 c
while True: jnz 75 d
    while True: a += 1  # inc a
        d += 1  # inc d
        if d <= 0: break  # jnz d -2
    c += 1  # inc c
    if c <= 0: break  # jnz c -5

# a = 12
b = a: 12  # cpy a b
b -= 1: 11  # dec b
d = a: 12  # cpy a d
a = 0  # copy 0 a
while True:
    c = b: 11  # copy b c
    while True:
        a += 1  # inc a
        c -= 1  # dec c
        if c <= 0:
            break  # jnz c -2
    : a = 11 * 12 = 121
    c = 0
    d -= 1  # dec d
    if d <= 0: break  # jnz d -5
    a = 121
    : c = 0
    : d = 0
b -= 1: 10  # dec b
c = b: 10  # copy b c
d = c: 10  # cpy c d
while True:
    d -= 1  # dec d
    c += 1  # inc c
    if d <= 0:
        break  # jnz d -2  d = 0
: c 20
: d 0
tgl c
c = -16  # cpy -16 c
pass # jnz 1 c
c = 84  # cpy 84 c
while True:
    jnz 75 d
    while True:
        a += 1  # inc a
        d += 1  # inc d
        if d <= 0:
            break  # jnz d -2
    c += 1  # inc c
    if c <= 0:
        break  # jnz c -5

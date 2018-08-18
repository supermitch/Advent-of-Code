def run(a=0):
    b = 65
    c = b
    if a != 0: # jnz a 2
        b *= 100
        b -= -100000
        c = b
        c -= -17000

    while True:
        f = 1
        d = 2
        while True:
            e = 2
            while True:
                g = d
                g *= e
                g -= b
                if g != 0:
                    f = 0
                e -= -1
                g = e
                g -= b
                if g == 0:
                    break
            d -= -1
            g = d
            g -= b
            if g == 0:
                break
        if f == 0:
            h -= -1
        g = b
        g -= c
        if g == 0:
            break
        b -= -17
    return

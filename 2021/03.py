with open('03_input.txt') as f:
    data = [x.strip() for x in f]

    common = []
    for i in range(len(data[0])):
        total = sum(int(x[i]) for x in data)
        if total > len(data) / 2:
            common.append('1')
        else:
            common.append('0')
    gamma = ''.join(common)
    print(gamma)
    gamma = int(gamma, 2)
    print(gamma)
    epsilon = ~gamma
    print(epsilon)
    print(gamma * epsilon)

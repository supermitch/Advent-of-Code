with open('2021/03_input.txt') as f:
    data = [x.strip() for x in f]

    gamma, epsilon = [], []
    for i in range(len(data[0])):
        if sum(int(x[i]) for x in data) > len(data) / 2:  # 1 most common
            gamma.append('1')
            epsilon.append('0')
        else:
            gamma.append('0')
            epsilon.append('1')

    gamma, epsilon = ''.join(gamma), ''.join(epsilon)
    gamma, epsilon = int(gamma, 2), int(epsilon, 2)
    print(f'Part 1: gamma * epsilon = {gamma * epsilon}')

    def calc_rating(data, on_bit):
        off_bit = '0' if on_bit == '1' else '1'
        i = 0
        while len(data) > 1:
            if sum(int(x[i]) for x in data) >= len(data) / 2:  # 1 most common, or equal counts
                common = on_bit
            else:
                common = off_bit
            data = [x for x in data if x[i] == common]
            i += 1
        return int(data[0], 2)
    oxygen = calc_rating(data, '1')
    co2 = calc_rating(data, '0')
    print(f'Part 2: oxygen_rating * co2_rating = {oxygen * co2}')

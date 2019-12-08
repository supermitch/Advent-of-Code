#!/usr/bin/env python


def chunk_data(data, width, height):
    layer_size = width * height
    layer_count = len(data) // layer_size
    layers = []
    for i in range(layer_count):
        layer_data = data[i * layer_size: (i + 1) * layer_size]
        layer = []
        for j in range(height):
            layer.append(layer_data[j * width: (j + 1) * width])
        layers.append(layer)
    return layers


def find_zero_layer(layers, width, height):
    zero_count = width * height  # Worst case
    for i, layer in enumerate(layers):
        total = sum(x == '0' for row in layer for x in row)
        if total < zero_count:
            zero_layer = i
            zero_count = total
    return zero_layer


def decode_image(layers, width, height):
    img = [[' ' for x in range(width)] for y in range(height)]
    for layer in layers[::-1]:
        for i, row in enumerate(layer):
            for j, char in enumerate(row):
                if char == '0':
                    img[i][j] = ' '  # Black
                elif char == '1':
                    img[i][j] = '█'  # White
    return img


def draw_image(image):
    for row in image:
        print(''.join(row))


def main():
    with open('input.txt') as f:
        data = list(str(next(f).strip()))

    width = 25
    height = 6
    layers = chunk_data(data, width, height)

    zero_layer = find_zero_layer(layers, width, height)
    ones = sum(x == '1' for row in layers[zero_layer] for x in row)
    twos = sum(x == '2' for row in layers[zero_layer] for x in row)
    print(f"Part A: {ones * twos} - No. of 1's x no. of 2's")

    draw_image(decode_image(layers, width, height))
    print('Part B: CJZHR - Decoded message')


if __name__ == '__main__':
    main()

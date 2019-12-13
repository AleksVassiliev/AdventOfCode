import sys
import copy
import collections


def process_layer(layer):
    d = collections.defaultdict(int)
    for num in layer:
        d[num] += 1
    return d


def apply_layer(src, trg):
    for i in range(len(src)):
        if src[i] == 2:
            src[i] = trg[i]


def print_layer(layer, w, h):
    pixel = { 0: ' ', 1: '#' }
    msg = ''
    for idx, e in enumerate(layer):
        if idx % w == 0:
            msg += '\n'
        msg += pixel[e]
    print(msg)


def main():
    data = [ int(x) for x in open('input08').read().rstrip('\n') ]
    
    width = 25
    height = 6
    layer_size = width * height
    slc = len(data) // layer_size

    digits0 = sys.maxsize
    res = 0
    for i in range(0, slc):
        d = process_layer(data[layer_size*i:layer_size*(i+1)])
        if d[0] < digits0:
            digits0 = d[0]
            res = d[1] * d[2]
    print(res)

    layer = copy.copy(data[0:layer_size])
    for i in range(1, slc):
        apply_layer(layer, data[layer_size*i:layer_size*(i+1)])
    print_layer(layer, width, height)


if __name__ == '__main__':
    main()
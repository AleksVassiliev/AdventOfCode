from collections import defaultdict


def modify_bit(num, pos, bit):
    mask = 1 << pos
    return (num & ~mask) | ((bit << pos) & mask)


def calculate_v1(data):
    memory = defaultdict(int)
    cur_mask = []
    for line in data:
        if line.startswith('mask'):
            cur_mask.clear()
            mask = line.split(' = ')[1]
            for idx, ch in enumerate(reversed(mask)):
                if ch != 'X':
                    cur_mask.append((idx, int(ch)))
        elif line.startswith('mem'):
            index, value = line.split(' = ')
            index = index[4:-1]
            value = int(value)
            for mask in cur_mask:
                value = modify_bit(value, *mask)
            memory[index] = value
    result = 0
    for key in memory:
        result += memory[key]
    return result


def expand_mask(masks):
    result = []
    for mask in masks:
        idx = mask.find('X')
        if idx != -1:
            mask0 = f'{mask[:idx]}0{mask[idx+1:]}'
            mask1 = f'{mask[:idx]}1{mask[idx+1:]}'
            result.append(mask0)
            result.append(mask1)
        else:
            result.append(mask)
    if len(result) != len(masks):
        return expand_mask(result)
    else:
        return result


def apply_mask(addr, mask):
    result = []
    for (a, m) in list(zip(addr, mask)):
        if m == '0':
            result.append(a)
        else:
            result.append(m)
    return expand_mask([''.join(result)])
        

def calculate_v2(data):
    memory = defaultdict(int)
    cur_mask = [0] * 36
    for line in data:
        if line.startswith('mask'):
            cur_mask = list(line.split(' = ')[1])
        elif line.startswith('mem'):
            addr, value = line.split(' = ')
            addr = f'{int(addr[4:-1]):0>36b}'
            value = int(value)
            addrs = apply_mask(list(addr), cur_mask)
            for addr in addrs:
                memory[int(addr, 2)] = value
    result = 0
    for key in memory:
        result += memory[key]
    return result


def main():
    data = [line.strip() for line in open('./input14.txt')]
    result_v1 = calculate_v1(data)
    print(result_v1)
    result_v2 = calculate_v2(data)
    print(result_v2)


if __name__ == '__main__':
    main()

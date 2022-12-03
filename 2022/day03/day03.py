def get_priority(chr):
    value = ord(chr)
    if 65 <= value <= 90:
        return (value - 65 + 27)
    if 97 <= value <= 122:
        return (value - 97 + 1)
    return None 


def calculate_priorities_v1(data):
    res = 0
    for line in data:
        comp1 = line[:len(line)//2]
        comp2 = line[len(line)//2:]
        item = set(comp1) & set(comp2)
        res += get_priority(item.pop())
    return res


def calculate_priorities_v2(data):
    res = 0
    it = iter(data)
    for x, y, z in zip(it, it, it):
        item = set(x) & set(y) & set(z)
        res += get_priority(item.pop())
    return res


def main():
    data = [line.strip() for line in open('./input.txt')]
    result_v1 = calculate_priorities_v1(data)
    print(result_v1)
    result_v2 = calculate_priorities_v2(data)
    print(result_v2)


if __name__ == '__main__':
    main()

def get_ranges_v1(data):
    res = 0
    for line in data:
        item1, item2 = line.split(',')
        (s1, e1) = [int(value) for value in item1.split('-')]
        (s2, e2) = [int(value) for value in item2.split('-')]
        if ((s2 <= s1 <= e2) and (s2 <= e1 <= e2)) or ((s1 <= s2 <= e1) and (s1 <= e2 <= e1)):
            res += 1
    return res


def get_ranges_v2(data):
    res = 0
    for line in data:
        item1, item2 = line.split(',')
        (s1, e1) = [int(value) for value in item1.split('-')]
        (s2, e2) = [int(value) for value in item2.split('-')]
        if ((s2 <= s1 <= e2) or (s2 <= e1 <= e2)) or ((s1 <= s2 <= e1) or (s1 <= e2 <= e1)):
            res += 1
    return res


def main():
    data = [line.strip() for line in open('./input.txt')]
    result_v1 = get_ranges_v1(data)
    print(result_v1)
    result_v2 = get_ranges_v2(data)
    print(result_v2)


if __name__ == '__main__':
    main()

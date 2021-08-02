from collections import defaultdict


def check_declaration_v1(data):
    result = 0
    group = set()
    for line in data:
        if line == '':
            result += len(group)
            group.clear()
        else:
            for ch in line:
                group.add(ch)
    result += len(group)
    return result


def analyze_declaration(group, persons):
    result = 0
    for key in group:
        if group[key] == persons:
            result += 1
    return result


def check_declaration_v2(data):
    result = 0
    group = defaultdict(int)
    persons = 0
    for line in data:
        if line == '':
            result += analyze_declaration(group, persons)
            group.clear()
            persons = 0
        else:
            persons += 1
            for ch in line:
                group[ch] += 1
    result += analyze_declaration(group, persons)
    return result


def main():
    with open('./input06.txt') as fi:
        data = fi.read().splitlines()
    result_v1 = check_declaration_v1(data)
    print(result_v1)
    result_v2 = check_declaration_v2(data)
    print(result_v2)


if __name__ == '__main__':
    main()

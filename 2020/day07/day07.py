from collections import defaultdict


def parse_rules(data):
    rules = {}
    for line in data:
        name, hold = line[:-1].split(' bags contain ')
        rules[name] = {}
        if hold != 'no other bags':
            lst = hold.split(', ')
            for item in lst:
                elem = item.split(' ')
                rules[name][f'{elem[1]} {elem[2]}'] = int(elem[0])
    return rules


def find_bag(bags, name):
    result = []
    for bag in bags:
        if name in bags[bag]:
            result.append(bag)
    return result


def check_package(rules):
    bags = parse_rules(rules)
    result = set()
    names = set()
    names.add('shiny gold')
    while True:
        name = names.pop()
        found = find_bag(bags, name)
        for item in found:
            result.add(item)
            names.add(item)
        if not names:
            break 
    return len(result)


def count(bags, name):
    if not bags[name]:
        return 0
    result = 0
    for bag in bags[name]:
        result += (bags[name][bag] * count(bags, bag))
        result += bags[name][bag]
    return result


def count_package(rules):
    bags = parse_rules(rules)
    return count(bags, 'shiny gold')


def main():
    rules = [line.strip() for line in open('./input07.txt')]
    result_v1 = check_package(rules)
    print(result_v1)
    result_v2 = count_package(rules)
    print(result_v2)


if __name__ == '__main__':
    main()

import re
import math

from functools import reduce


def parse_data(data):
    monkeys = []
    monkey = {'cnt': 0}
    for line in data:
        if line == '':
            monkeys.append(monkey)
            monkey = {'cnt': 0}
        else:
            if line.startswith('Monkey'):
                monkey['id'] = int(re.findall('[0-9]+', line)[0])
            elif line.startswith('Starting items'):
                monkey['items'] = [x for x in re.findall('[0-9]+', line)]
            elif line.startswith('Operation'):
                monkey['op'] = line.split('= ')[1]
            elif line.startswith('Test'):
                monkey['div'] = int(re.findall('[0-9]+', line)[0])
            elif line.startswith('If true'):
                monkey['idt'] = int(re.findall('[0-9]+', line)[0])
            elif line.startswith('If false'):
                monkey['idf'] = int(re.findall('[0-9]+', line)[0])
    monkeys.append(monkey)
    return monkeys


def make_round_v1(monkeys):
    for monkey in monkeys:
        while monkey['items']:
            value = monkey['items'].pop(0)
            lvl = eval(monkey['op'].replace('old', value)) // 3
            dst = monkey['idt'] if lvl % monkey['div'] == 0 else monkey['idf']
            monkeys[dst]['items'].append(str(lvl))
            monkey['cnt'] += 1
    return monkeys


def calculate_level_v1(data):
    monkeys = parse_data(data)
    for _ in range(20):
        monkeys = make_round_v1(monkeys)
    res = [x['cnt'] for x in monkeys]
    res.sort(reverse=True)
    return (res[0] * res[1])


def make_round_v2(monkeys, mod_lcm):
    for monkey in monkeys:
        while monkey['items']:
            value = monkey['items'].pop(0)
            lvl = eval(monkey['op'].replace('old', value)) % mod_lcm
            dst = monkey['idt'] if lvl % monkey['div'] == 0 else monkey['idf']
            monkeys[dst]['items'].append(str(lvl))
            monkey['cnt'] += 1
    return monkeys


def lcm(arr):
    return reduce(lambda x, y : (x * y) // math.gcd(x, y), arr)


def calculate_level_v2(data):
    monkeys = parse_data(data)
    mod_lcm = lcm([x['div'] for x in monkeys])
    for _ in range(10000):
        monkeys = make_round_v2(monkeys, mod_lcm)
    res = [x['cnt'] for x in monkeys]
    res.sort(reverse=True)
    return (res[0] * res[1])


def main():
    data = [line.strip() for line in open('./input.txt')]
    result_v1 = calculate_level_v1(data)
    print(result_v1)
    result_v2 = calculate_level_v2(data)
    print(result_v2)


if __name__ == '__main__':
    main()

import itertools


def parse_input(content):
    persons = set()
    happiness = {}
    for line in content:
        item = line.split(" ")
        name1 = item[0]
        name2 = item[-1]
        persons.add(name1)
        persons.add(name2)
        value = int(item[3])
        if item[2] == "lose":
            value *= -1
        key = "{}-{}".format(name1, name2)
        happiness[key] = value
    return persons, happiness


def expand_input(persons, happiness):
    for p in persons:
        key1 = "{}-Me".format(p)
        key2 = "Me-{}".format(p)
        happiness[key1] = 0
        happiness[key2] = 0
    persons.add("Me")
    return persons, happiness


def get_variants(persons):
    return itertools.permutations(persons)


def calculate(variants, happiness):
    res = 0
    for item in variants:
        value = 0
        for idx in range(0, len(item)-1):
            key1 = "{}-{}".format(item[idx], item[idx+1])
            key2 = "{}-{}".format(item[idx+1], item[idx])
            value += (happiness[key1] + happiness[key2])
        key1 = "{}-{}".format(item[0], item[-1])
        key2 = "{}-{}".format(item[-1], item[0])
        value += (happiness[key1] + happiness[key2])
        res = max(res, value)
    return res


def main():
    content = [ line.rstrip(".\n") for line in open("input13") ]

    p, h = parse_input(content)
    var = get_variants(p)
    res = calculate(var, h)
    print(res)

    p, h = expand_input(p, h)
    var = get_variants(p)
    res = calculate(var, h)
    print(res)

    '''
    max_route = None
    min_route = None
    all_routes = itertools.permutations(cities)
    for p in all_routes:
        distance = 0
        for i in range(len(p)-1):
            key = "{}-{}".format(p[i], p[i+1])
            distance += routes[key] 
        if max_route is None:
            max_route = distance
        else:
            max_route = max(max_route, distance)
        if min_route is None:
            min_route = distance
        else:
            min_route = min(min_route, distance)

    print(min_route, max_route)
    '''

if __name__ == "__main__":
    main()

import itertools


def main():
    content = [ line.rstrip("\n") for line in open("input09") ]

    cities = set()
    routes = {}
    for line in content:
        c, d = line.split(" = ")
        src, dst = c.split(" to ")
        cities.add(src)
        cities.add(dst)
        key1 = "{}-{}".format(src, dst)
        key2 = "{}-{}".format(dst, src)
        routes[key1] = int(d)
        routes[key2] = int(d)


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


if __name__ == "__main__":
    main()

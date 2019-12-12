def direct_orbits(data, name):
    return 1 if data[name] is not None else 0

def indirect_orbits(data, name):
    cnt = 0
    parent = data[name]
    if parent is not None:
        parent = data[parent]
    while parent is not None:
        parent = data[parent]
        cnt += 1
    return cnt

def orbits(data, name):
    return direct_orbits(data, name) + indirect_orbits(data, name)


def get_path(data, name):
    path = []
    parent = data[name]
    while parent is not None:
        path.append(parent)
        parent = data[parent]
    return path


def get_distance(path, intersect):
    cnt = 0
    for item in path:
        if item == intersect:
            break
        cnt += 1
    return cnt


def main():
    data = [ x.rstrip('\n') for x in open('input06') ]

    omap = {}
    for item in data:
        parent, name = item.split(')')
        if parent not in omap:
            omap[parent] = None
        omap[name] = parent

    cnt = 0
    for k in omap:
        cnt += orbits(omap, k)
    print(cnt)


    pathY = get_path(omap, 'YOU')
    pathS = get_path(omap, 'SAN')

    intersect = None
    for item in pathY:
        if item in pathS:
            intersect = item
            break

    cntY = get_distance(pathY, intersect)
    cntS = get_distance(pathS, intersect)
    print(cntY + cntS)


if __name__ == '__main__':
    main()

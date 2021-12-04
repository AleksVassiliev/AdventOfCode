def get_cells(data):
    cells = set()
    for y, line in enumerate(data):
        for x, cell in enumerate(line):
            if cell == '#':
                cells.add((x, y, 0, 0))
    return cells


def get_bounds(cells, dim):
    res = []
    for i in range(dim):
        res.append(min(cells, key=lambda x: x[i])[i] - 1)
        res.append(max(cells, key=lambda x: x[i])[i] + 2)
    return res


def get_neighbors(x, y, z, w, cells, dim):
    res = 0
    if dim == 3:
        wrange = [0]
    elif dim == 4:
        wrange = [-1, 0, 1]
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                for dw in wrange:
                    if not (dx == 0 and dy == 0 and dz == 0 and dw == 0):
                        if (x + dx, y + dy, z + dz, w + dw) in cells:
                            res += 1
    return res


def step(cells, dim):
    bounds = get_bounds(cells, dim)
    next_cells = set()
    if dim == 3:
        wrange = [0]
    elif dim == 4:
        wrange = range(bounds[6], bounds[7])
    for x in range(bounds[0], bounds[1]):
        for y in range(bounds[2], bounds[3]):
            for z in range(bounds[4], bounds[5]):
                for w in wrange:
                    ns = get_neighbors(x, y, z, w, cells, dim)
                    if (x, y, z, w) in cells and ns in [2, 3]:
                        next_cells.add((x, y, z, w))
                    elif (x, y, z, w) not in cells and ns == 3:
                        next_cells.add((x, y, z, w))
    return next_cells


def simulate(data, dim):
    cells = get_cells(data)
    p1 = cells.copy()
    for _ in range(6):
        p1 = step(p1, dim)
    return len(p1)


def main():
    data = [line.strip() for line in open('input17.txt')]
    result_v1 = simulate(data, 3)
    print(result_v1)
    result_v2 = simulate(data, 4)
    print(result_v2)


if __name__ == '__main__':
    main()

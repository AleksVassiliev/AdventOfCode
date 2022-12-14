def parse_data(data):
    grid = set()
    for line in data:
        coords = [[int(x) for x in values.split(',')] for values in line.split(' -> ')]
        xs, ys = coords.pop(0)
        while len(coords):
            xe, ye = coords.pop(0)
            if xs == xe:
                for y in range(min(ys, ye), max(ys, ye)+1):
                    grid.add((xs, y))
            elif ys == ye:
                for x in range(min(xs, xe), max(xs, xe)+1):
                    grid.add((x, ys))
            xs, ys = xe, ye
    return grid


def get_borders(grid):
    ly = 0
    lx = 10000
    rx = 0
    for x, y in grid:
        ly = max(ly, y)
        lx = min(lx, x)
        rx = max(rx, x)
    return (lx, rx, ly)


def drop_sand_v1(grid, lx, rx, ly):
    pos = (500, 0)
    while (pos[1] <= ly) and (lx <= pos[0] <= rx):
        posd = (pos[0], pos[1] + 1)
        if posd in grid:
            posl = (pos[0] - 1, pos[1] + 1)
            if posl in grid:
                posr = (pos[0] + 1, pos[1] + 1)
                if posr in grid:
                    return pos
                else:
                    pos = posr
            else:
                pos = posl
        else:
            pos = posd
    return None


def count_sands_v1(data):
    grid = parse_data(data)
    borders = get_borders(grid)
    res = 0
    while True:
        pos = drop_sand_v1(grid, *borders)
        if pos is None:
            return res
        else:
            grid.add(pos)
            res += 1


def get_lower_y(grid):
    ly = 0
    for _, y in grid:
        ly = max(ly, y)
    return (ly + 2)


def drop_sand_v2(grid, lowery):
    pos = (500, 0)
    while pos not in grid:
        posd = (pos[0], pos[1] + 1)
        if (posd in grid) or (posd[1] == lowery):
            posl = (pos[0] - 1, pos[1] + 1)
            if (posl in grid) or (posl[1] == lowery):
                posr = (pos[0] + 1, pos[1] + 1)
                if (posr in grid) or (posr[1] == lowery):
                    return pos
                else:
                    pos = posr
            else:
                pos = posl
        else:
            pos = posd
    return None


def count_sands_v2(data):
    grid = parse_data(data)
    lowery = get_lower_y(grid)
    res = 0
    while True:
        pos = drop_sand_v2(grid, lowery)
        if pos is None:
            return res
        else:
            grid.add(pos)
            res += 1


def main():
    data = [line.strip() for line in open('./input.txt')]
    result_v1 = count_sands_v1(data)
    print(result_v1)
    result_v2 = count_sands_v2(data)
    print(result_v2)


if __name__ == '__main__':
    main()

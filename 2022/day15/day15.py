import re
import functools

import shapely


def parse_data(data):
    grid = []
    for line in data:
        (sx, sy, bx, by) = [int(x) for x in re.findall('-?[0-9]+', line)]
        d = abs(sx - bx) + abs(sy - by)
        grid.append(((sx, sy), (bx, by), d))
    return grid


def apply_signal(S, _, dist, row):
    (sx, sy) = S
    shift = abs(sy - row)
    return ((sx - dist + shift, sx + dist - shift))


def check_row(data, row):
    grid = parse_data(data)
    lines = []
    for item in grid:
        lines.append(apply_signal(*item, row))
    slines = sorted(lines, key=lambda x: x[0])
    line = functools.reduce(lambda la, lb: (min(la[0], lb[0]), max(la[1], lb[1])), slines)
    return (line[1] - line[0])


def find_position(data, size):
    grid = parse_data(data)
    coverage = []
    for S, _, dist in grid:
        x, y = S
        coverage.append(shapely.Polygon([(x + dist, y), (x, y - dist), (x - dist, y), (x, y + dist)]))
    area = shapely.clip_by_rect(shapely.unary_union(coverage), 0, 0, size, size).interiors[0]
    x, y = tuple(map(round, area.centroid.coords[:][0]))
    return (x * 4000000 + y)


def main():
    data = [line.strip() for line in open('./input.txt')]
    result_v1 = check_row(data, 2000000)
    print(result_v1)
    result_v2 = find_position(data, 4000000)
    print(result_v2)


if __name__ == '__main__':
    main()

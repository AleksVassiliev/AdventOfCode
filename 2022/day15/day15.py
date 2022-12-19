import re
import functools


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


def check_row_v1(data, row):
    grid = parse_data(data)
    lines = []
    for item in grid:
        lines.append(apply_signal(*item, row))
    slines = sorted(lines, key=lambda x: x[0])
    line = functools.reduce(lambda la, lb: (min(la[0], lb[0]), max(la[1], lb[1])), slines)
    return (line[1] - line[0])

def main():
    data = [line.strip() for line in open('./input.txt')]
    result_v1 = check_row_v1(data, 2000000)
    print(result_v1)
    #result_v2 = find_position(data)
    #print(result_v2)


if __name__ == '__main__':
    main()

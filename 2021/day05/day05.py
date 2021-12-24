from collections import defaultdict


def parse_input(data):
    lines = []
    for item in data:
        start, end = item.split(' -> ')
        x1, y1 = start.split(',')
        x2, y2 = end.split(',')
        lines.append(((int(x1), int(y1)), (int(x2), int(y2))))
    return lines


def process_line(grid, line, ignore_diagonal=True):
        x1, y1 = line[0]
        x2, y2 = line[1]
        if y1 == y2:
            x1, x2 = min(x1, x2), max(x1, x2)
            for x in range(x1, x2 + 1):
                grid[(x, y1)] += 1
        elif x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            for y in range(y1, y2 + 1):
                grid[(x1, y)] += 1
        elif not ignore_diagonal:
            modx = 1 if x1 < x2 else -1
            mody = 1 if y1 < y2 else -1
            len = abs(x1 - x2)
            for i in range(len + 1):
                grid[(x1 + modx * i, y1 + mody * i)] += 1


def count_points(grid):
    result = 0
    for key in grid:
        if grid[key] > 1:
            result +=1 
    return result


def calculate_points_v1(lines):
    lines = parse_input(lines)
    grid = defaultdict(int)
    for line in lines:
        process_line(grid, line)
    return count_points(grid)


def calculate_points_v2(lines):
    lines = parse_input(lines)
    grid = defaultdict(int)
    for line in lines:
        process_line(grid, line, ignore_diagonal=False)
    return count_points(grid)


def main():
    data = [line.strip() for line in open('./input05.txt')]
    result_v1 = calculate_points_v1(data)
    print(result_v1)
    result_v2 = calculate_points_v2(data)
    print(result_v2)


if __name__ == '__main__':
    main()

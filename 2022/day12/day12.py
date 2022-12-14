def parse_data(data):
    values = 'SabcdefghijklmnopqrstuvwxyzE'
    vdata = [[values.index(c) for c in row] for row in data]
    for col in range(len(vdata)):
        for row in range(len(vdata[col])):
            if vdata[col][row] == 0:
                return (row, col), vdata
    
     
def variants(grid, x, y):
    variants  = []
    coords = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    for r, c in coords:
        if (0 <= r < len(grid[0])) and (0 <= c < len(grid)):
            if (grid[c][r] - grid[y][x]) <= 1:
                variants.append((r, c))
    return variants



def find_path(grid, S, E=27):
    visited = []
    paths = [[S]]
    while len(paths):
        path = paths.pop(0)
        for v in variants(grid, *path[-1]):
            if (v not in path) and (v not in visited):
                newpath = list(path)
                newpath.append(v)
                x, y = v
                if grid[y][x] == E:
                    return newpath
                else:
                    paths.append(newpath)
                    visited.append(v)
    return []


def find_path_v1(data):
    s, grid = parse_data(data)
    res = find_path(grid, s)
    return (len(res) - 1)


def find_starting_points(grid):  
    points = set()  
    for col in range(len(grid)):
        for row in range(len(grid[col])):
            if grid[col][row] == 1:
                if 2 in [grid[y][x] for x, y in variants(grid, row, col)]:
                    points.add((row, col))
    return points
                

def find_path_v2(data, check_point=5):              # check_point is a cell from which all paths are the same (it's 'e' in example, and 'd' in puzzle input)
    _, grid = parse_data(data)
    points = find_starting_points(grid)             # find all valid starting point which value is 'a' and near cell is 'b'
    paths = []
    for p in points:
        path = find_path(grid, p, check_point)
        paths.append(path)
    min_path = paths[0]                             # find the shortest way to checkpoint
    for p in paths:
        if len(p) < len(min_path):
            min_path = p
    path = find_path(grid, min_path[-1])            # find path from checkpoint to E
    return (len(min_path) + len(path) - 2)


def main():
    data = [line.strip() for line in open('./input.txt')]
    result_v1 = find_path_v1(data)
    print(result_v1)
    result_v2 = find_path_v2(data, 4)
    print(result_v2)


if __name__ == '__main__':
    main()

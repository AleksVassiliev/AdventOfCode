def is_tree_visible(map, x, y):
    height = map[y][x]
    row = [elem for elem in map[y]]
    col = [elem[x] for elem in map]
    row_left = row[:x]
    row_right = row[x+1:]
    col_top = col[:y]
    col_bottom = col[y+1:]
    return ((height > max(row_left)) or (height > max(row_right)) or (height > max(col_top)) or (height > max(col_bottom)))


def count_trees(map):
    res = 2 * len(map)
    for y in range(1, len(map)-1):
        res += 2
        for x in range(1, len(map[y])-1):
            if is_tree_visible(map, x, y):
                res += 1
    return res


def scenic_score(map, x, y):
    def distance(height, data):
        dist = 0
        for item in data:
            dist += 1
            if item >= height:
                return dist
        return dist

    height = map[y][x]
    row = [elem for elem in map[y]]
    col = [elem[x] for elem in map]
    dist_left = distance(height, reversed(row[:x]))
    dist_right = distance(height, row[x+1:])
    dist_up = distance(height, reversed(col[:y]))
    dist_down = distance(height, col[y+1:])
    return (dist_up * dist_left * dist_down * dist_right)
    

def count_score(map):
    res = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            res = max(res, scenic_score(map, x, y))
    return res


def main():
    with open('./input.txt') as fi:
        data = fi.readlines();
        map = []
        for line in data:
            map.append([int(item) for item in line.strip('\n')])
        result_v1 = count_trees(map)
        print(result_v1)
        result_v2 = count_score(map)
        print(result_v2)


if __name__ == '__main__':
    main()

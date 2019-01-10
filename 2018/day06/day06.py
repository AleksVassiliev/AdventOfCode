import collections


def part1(lines):
    coords = []
    max_r = max_c = 0
    min_r = min_c = 1000
    for line in lines:
        r, c = map(int, line.split(", "))
        coords.append((r, c))
        max_r = max(max_r, r)
        max_c = max(max_c, c)
        min_r = min(min_r, r)
        min_c = min(min_c, c)

    region_sizes = collections.defaultdict(int)
    infinite = set()

    for i in range(min_r, max_r + 1):
        for j in range(min_c, max_c + 1):
            min_dists = []
            for idx, coord in enumerate(coords):
                dist = abs(coord[0] - i) + abs(coord[1] - j)
                min_dists.append((dist, idx))
            min_dists = sorted(min_dists)

            if min_dists[0][0] != min_dists[1][0]:
                coord_id = min_dists[0][1]
                region_sizes[coord_id] += 1

                if (i == min_r) or (i == max_r) or (j == min_c) or (j == max_c):
                    infinite.add(coord_id)

    max_region = 0
    for key in region_sizes:
        if key not in infinite:
            max_region = max(max_region, region_sizes[key])

    return max_region



def part2(lines, manhattan_limit=10000):
    coords = []
    max_r = max_c = 0
    min_r = min_c = 1000
    for line in lines:
        r, c = map(int, line.split(", "))
        coords.append((r, c))
        max_r = max(max_r, r)
        max_c = max(max_c, c)
        min_r = min(min_r, r)
        min_c = min(min_c, c)

    size_shared_region = 0
    for i in range(min_r, max_r + 1):
        for j in range(min_c, max_c + 1):
            region_size = 0
            for coord in coords:
                region_size += abs(coord[0] - i) + abs(coord[1] - j)
            if region_size < manhattan_limit:
                size_shared_region += 1
                
    return size_shared_region




def main():
    content = [ x.rstrip('\n') for x in open('input06') ]

    print(part1(content))
    print(part2(content))


if __name__ == '__main__':
    main()

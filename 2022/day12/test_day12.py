import day12


data = [
    'Sabqponm',
    'abcryxxl',
    'accszExk',
    'acctuvwj',
    'abdefghi'
]


def test_part1():
    assert(day12.find_path_v1(data) == 31)


def test_part2():
    assert(day12.find_path_v2(data) == 29)

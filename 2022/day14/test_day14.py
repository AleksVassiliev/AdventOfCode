import day14


data = [
    '498,4 -> 498,6 -> 496,6',
    '503,4 -> 502,4 -> 502,9 -> 494,9'
]


def test_part1():
    assert(day14.count_sands_v1(data) == 24)


def test_part2():
    assert(day14.count_sands_v2(data) == 93)

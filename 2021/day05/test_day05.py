import pytest

import day05


lines = [
    '0,9 -> 5,9',
    '8,0 -> 0,8',
    '9,4 -> 3,4',
    '2,2 -> 2,1',
    '7,0 -> 7,4',
    '6,4 -> 2,0',
    '0,9 -> 2,9',
    '3,4 -> 1,4',
    '0,0 -> 8,8',
    '5,5 -> 8,2'
]


@pytest.mark.parametrize('lines, result', [(lines, 5)])
def test_part1(lines, result):
    assert(day05.calculate_points_v1(lines) == result)


@pytest.mark.parametrize('lines, result', [(lines, 12)])
def test_part2(lines, result):
    assert(day05.calculate_points_v2(lines) == result)

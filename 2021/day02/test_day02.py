import pytest

import day02


course = [
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2'
]


@pytest.mark.parametrize('course, result', [(course, 150)])
def test_part1(course, result):
    assert(day02.calculate_position_v1(course) == result)


@pytest.mark.parametrize('course, result', [(course, 900)])
def test_part2(course, result):
    assert(day02.calculate_position_v2(course) == result)

import pytest

import day06


data = [3, 4, 3, 1, 2]


@pytest.mark.parametrize('data, result', [(data, 5934)])
def test_part1(data, result):
    assert(day06.calculate_v1(data) == result)


@pytest.mark.parametrize('data, result', [(data, 26984457539)])
def test_part2(data, result):
    assert(day06.calculate_v2(data) == result)

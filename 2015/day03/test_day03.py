import pytest

import day03


@pytest.mark.parametrize('moves, result', [('>', 2), ('^>v<', 4), ('^v^v^v^v^v', 2)])
def test_part1(moves, result):
    assert(day03.count_houses_v1(moves) == result)


@pytest.mark.parametrize('moves, result', [('^v', 3), ('^>v<', 3), ('^v^v^v^v^v', 11)])
def test_part2(moves, result):
    assert(day03.count_houses_v2(moves) == result)

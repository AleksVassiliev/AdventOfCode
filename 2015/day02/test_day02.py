import pytest

import day02


@pytest.mark.parametrize('dimensions, result', [('2x3x4', 58), ('1x1x10', 43)])
def test_part1(dimensions, result):
    assert(day02.calculate_papper(dimensions) == result)


@pytest.mark.parametrize('dimensions, result', [('2x3x4', 34), ('1x1x10', 14)])
def test_part2(dimensions, result):
    assert(day02.calculate_ribbon(dimensions) == result)

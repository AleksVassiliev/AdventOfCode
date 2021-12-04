import pytest

import day17


cube = [
    '.#.',
    '..#',
    '###'
]


@pytest.mark.parametrize('data, result', [(cube, 112)])
def test_part1(data, result):
    assert(day17.simulate(data, 3) == result)


@pytest.mark.parametrize('data, result', [(cube, 848)])
def test_part2(data, result):
    assert(day17.simulate(data, 4) == result)

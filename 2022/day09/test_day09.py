import pytest

import day09


moves1 = [
    'R 4',
    'U 4',
    'L 3',
    'D 1',
    'R 4',
    'D 1',
    'L 5',
    'R 2'
]


def test_part1():
    assert(day09.count_positions_v1(moves1) == 13)


moves2 = [
    'R 5',
    'U 8',
    'L 8',
    'D 3',
    'R 17',
    'D 10',
    'L 25',
    'U 20'
]

@pytest.mark.parametrize('moves, result', [(moves1, 1), (moves2, 36)])
def test_part2(moves, result):
    assert(day09.count_positions_v2(moves) == result)

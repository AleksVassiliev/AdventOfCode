import pytest

import day11


layout = [
    'L.LL.LL.LL',
    'LLLLLLL.LL',
    'L.L.L..L..',
    'LLLL.LL.LL',
    'L.LL.LL.LL',
    'L.LLLLL.LL',
    '..L.L.....',
    'LLLLLLLLLL',
    'L.LLLLLL.L',
    'L.LLLLL.LL'
]


@pytest.mark.parametrize('layout, result', [(layout, 37)])
def test_layout_v1(layout, result):
    assert(day11.calculate_seats(layout) == result)


@pytest.mark.parametrize('layout, result', [(layout, 26)])
def test_layout_v2(layout, result):
    assert(day11.calculate_seats(layout, True) == result)

import pytest

import day04


data = [
    '2-4,6-8',
    '2-3,4-5',
    '5-7,7-9',
    '2-8,3-7',
    '6-6,4-6',
    '2-6,4-8'
]


def test_part1():
    assert(day04.get_ranges_v1(data) == 2)


def test_part2():
    assert(day04.get_ranges_v2(data) == 4)

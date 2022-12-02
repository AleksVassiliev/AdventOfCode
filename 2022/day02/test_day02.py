import pytest

import day02


data = [
    'A Y',
    'B X',
    'C Z'
]


def test_part1():
    assert(day02.calculate_score_v1(data) == 15)


def test_part2():
    assert(day02.calculate_score_v2(data) == 12)

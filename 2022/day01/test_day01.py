import pytest

import day01


data = [
    '1000',
    '2000',
    '3000',
    '',
    '4000',
    '',
    '5000',
    '6000',
    '',
    '7000',
    '8000',
    '9000',
    '',
    '10000'
]


def test_part1():
    assert(day01.calculate_calories_v1(data) == 24000)


def test_part2():
    assert(day01.calculate_calories_v2(data) == 45000)

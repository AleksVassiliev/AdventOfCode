import pytest

import day07


data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


@pytest.mark.parametrize('data, position, result', [(data, 2, 37), (data, 1, 41), (data, 3, 39), (data, 10, 71)])
def test_calculate_fuel_v1(data, position, result):
    assert(day07.calculate_fuel_v1(data, position) == result)


@pytest.mark.parametrize('data, result', [(data, 37)])
def test_part1(data, result):
    assert(day07.find_position_v1(data) == result)


@pytest.mark.parametrize('data, position, result', [(data, 5, 168), (data, 2, 206)])
def test_calculate_fuel_v2(data, position, result):
    assert(day07.calculate_fuel_v2(data, position) == result)


@pytest.mark.parametrize('data, result', [(data, 168)])
def test_part1(data, result):
    assert(day07.find_position_v2(data) == result)

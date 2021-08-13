import pytest

import day09


preamble = [x for x in range(1, 26)]

data = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576
]


@pytest.mark.parametrize('preamble, value, result', [(preamble, 26, True), (preamble, 49, True), (preamble, 100, False), (preamble, 50, False)])
def test_preamble(preamble, value, result):
    assert(day09.check_value(preamble, value) == result)


@pytest.mark.parametrize('data, result', [(data, 127)])
def test_sequence(data, result):
    assert(day09.check_sequence(data, 5) == result)


@pytest.mark.parametrize('data, value, result', [(data, 127, 62)])
def test_weakness(data, value, result):
    assert(day09.calculate_weakness(data, 127) == result)
    
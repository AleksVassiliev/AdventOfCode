import pytest

import day03


report = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010'
]


@pytest.mark.parametrize('report, result', [(report, 198)])
def test_part1(report, result):
    assert(day03.calculate_report_v1(report) == result)


@pytest.mark.parametrize('report, result', [(report, 230)])
def test_part2(report, result):
    assert(day03.calculate_report_v2(report) == result)

import pytest

import day01


report = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


@pytest.mark.parametrize('report, result', [(report, 7)])
def test_part1(report, result):
    assert(day01.calculate_report_v1(report) == result)


@pytest.mark.parametrize('report, result', [(report, 5)])
def test_part2(report, result):
    assert(day01.calculate_report_v2(report) == result)

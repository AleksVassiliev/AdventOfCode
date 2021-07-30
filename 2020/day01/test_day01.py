import pytest

import day01


@pytest.mark.parametrize('report, result', [([1721, 979, 366, 299, 675, 1456], 514579)])
def test_part1(report, result):
    assert(day01.calculate_report_v1(report) == result)


@pytest.mark.parametrize('report, result', [([1721, 979, 366, 299, 675, 1456], 241861950)])
def test_part2(report, result):
    assert(day01.calculate_report_v2(report) == result)

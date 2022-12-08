import pytest

import day05


@pytest.mark.parametrize('text, result', [('ugknbfddgicrmopn', True), ('aaa', True), ('jchzalrnumimnmhp', False), ('haegwjzuvuyypxyu', False), ('dvszwmarrgswjxmb', False)])
def test_part1(text, result):
    assert(day05.is_nice_string_v1(text) == result)


@pytest.mark.parametrize('text, result', [('qjhvhtzxzqqjkmpb', True), ('xxyxx', True), ('uurcxstgmygtbstg', False), ('ieodomkazucvgmuy', False)])
def test_part1(text, result):
    assert(day05.is_nice_string_v2(text) == result)

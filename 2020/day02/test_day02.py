import pytest

import day02


@pytest.mark.parametrize('policy, password, result', [('1-3 a', 'abcde', True), ('1-3 b', 'cdefg', False), ('2-9 c', 'ccccccccc', True)])
def test_part1(policy, password, result):
    assert(day02.check_password_v1(policy, password) == result)


@pytest.mark.parametrize('policy, password, result', [('1-3 a', 'abcde', True), ('1-3 b', 'cdefg', False), ('2-9 c', 'ccccccccc', False)])
def test_part2(policy, password, result):
    assert(day02.check_password_v2(policy, password) == result)

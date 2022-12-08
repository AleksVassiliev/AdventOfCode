import pytest

import day04


@pytest.mark.parametrize('key, result', [('abcdef', 609043), ('pqrstuv', 1048970)])
def test_part1(key, result):
    assert(day04.calculate_hash_v1(key) == result)

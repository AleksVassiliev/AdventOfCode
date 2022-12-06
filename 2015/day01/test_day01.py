import pytest

import day01


@pytest.mark.parametrize('instructions, result', [('(())', 0), ('()()', 0), ('(((', 3), ('(()(()(', 3), ('))(((((', 3), ('())', -1), ('))(', -1), (')))', -3), (')())())', -3)])
def test_part1(instructions, result):
    assert(day01.solve_v1(instructions) == result)


@pytest.mark.parametrize('instructions, result', [(')', 1), ('()())', 5)])
def test_part2(instructions, result):
    assert(day01.solve_v2(instructions) == result)

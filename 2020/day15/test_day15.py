import pytest

import day15


@pytest.mark.parametrize('numbers, result', [([0, 3, 6], 436), ([1, 3, 2], 1), ([2, 1, 3], 10), ([1, 2, 3], 27), ([2, 3, 1], 78), ([3, 2, 1], 438), ([3, 1, 2], 1836)])
def test_program_v1(numbers, result):
    assert(day15.get_number(numbers, 2020) == result)


@pytest.mark.parametrize('numbers, result', [([0, 3, 6], 175594), ([1, 3, 2], 2578), ([2, 1, 3], 3544142), 
                                             ([1, 2, 3], 261214), ([2, 3, 1], 6895259), ([3, 2, 1], 18), ([3, 1, 2], 362)])
def test_program_v2(numbers, result):
    assert(day15.get_number(numbers, 30000000) == result)

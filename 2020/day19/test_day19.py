import pytest

import day19


data = [
    '0: 1 2',
    '1: "a"',
    '2: 1 3 | 3 1',
    '3: "b"',
]
'''
data = [
    '0: 4 1 5',
    '1: 2 3 | 3 2',
    '2: 4 4 | 5 5',
    '3: 4 5 | 5 4',
    '4: "a"',
    '5: "b"',
]
'''


def test():
    day19.analyze(data)
    assert False


'''
@pytest.mark.parametrize('expression, result', examples_part1)
def test_part1(expression, result):
    assert(day18.evaluate_v1(expression) == result)


@pytest.mark.parametrize('expression, result', examples_part2)
def test_part2(expression, result):
    assert(day18.evaluate_v2(expression) == result)
'''
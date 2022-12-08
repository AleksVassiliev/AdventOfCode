import pytest

import day08


map = [
    [3, 0, 3, 7, 3],
    [2, 5, 5, 1, 2],
    [6, 5, 3, 3, 2],
    [3, 3, 5, 4, 9],
    [3, 5, 3, 9, 0]
]


@pytest.mark.parametrize('x, y, result', [(1, 1, True), (2, 1, True), (3, 1, False), (1, 2, True), (2, 2, False), (3, 2, True), (1, 3, False), (2, 3, True), (3, 3, False)])
def test_visible(x, y, result):
    assert(day08.is_tree_visible(map, x, y) == result)


def test_part1():
    assert(day08.count_trees(map) == 21)


@pytest.mark.parametrize('x, y, result', [(2, 1, 4), (2, 3, 8)])
def test_score(x, y, result):
    assert(day08.scenic_score(map, x, y) == result)


def test_part2():
    assert(day08.count_score(map) == 8)

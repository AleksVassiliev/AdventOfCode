import pytest

import day03


pattern = [
    '..##.......',
    '#...#...#..',
    '.#....#..#.',
    '..#.#...#.#',
    '.#...##..#.',
    '..#.##.....',
    '.#.#.#....#',
    '.#........#',
    '#.##...#...',
    '#...##....#',
    '.#..#...#.#'
]


@pytest.mark.parametrize('pattern, trees', [(pattern, 7)])
def test_part1(pattern, trees):
    assert(day03.make_path(pattern, 3, 1) == trees)


@pytest.mark.parametrize('pattern, result', [(pattern, 336)])
def test_part2(pattern, result):
    assert(day03.count_slopes(pattern) == result)

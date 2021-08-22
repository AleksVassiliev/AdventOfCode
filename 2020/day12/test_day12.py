import pytest

import day12


path = [
    'F10',
    'N3',
    'F7',
    'R90',
    'F11'
]


@pytest.mark.parametrize('path, result', [(path, 25)])
def test_path_v1(path, result):
    assert(day12.calculate_distance_v1(path) == result)


@pytest.mark.parametrize('path, result', [(path, 286)])
def test_path_v2(path, result):
    assert(day12.calculate_distance_v2(path) == result)

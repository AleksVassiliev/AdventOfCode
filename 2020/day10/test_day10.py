import pytest

import day10


adapters_v1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
diff_v1 = {'1': 7, '3': 5}

adapters_v2 = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
diff_v2 = {'1': 22, '3': 10}


@pytest.mark.parametrize('adapters, result', [(adapters_v1, diff_v1), (adapters_v2, diff_v2)])
def test_differences(adapters, result):
    diff = day10.calculate_difference(adapters)
    assert(diff['1'] == result['1'])
    assert(diff['3'] == result['3'])


@pytest.mark.parametrize('adapters, result', [(adapters_v1, 8), (adapters_v2, 19208)])
def test_tree(adapters, result):
    assert(day10.calculate_variants(adapters) == result)
     
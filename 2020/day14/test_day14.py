import pytest

import day14


program_v1 = [
    'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
    'mem[8] = 11',
    'mem[7] = 101',
    'mem[8] = 0',
]


program_v2 = [
    'mask = 000000000000000000000000000000X1001X',
    'mem[42] = 100',
    'mask = 00000000000000000000000000000000X0XX',
    'mem[26] = 1',
]


@pytest.mark.parametrize('program, result', [(program_v1, 165)])
def test_program_v1(program, result):
    assert(day14.calculate_v1(program) == result)


@pytest.mark.parametrize('program, result', [(program_v2, 208)])
def test_program_v2(program, result):
    assert(day14.calculate_v2(program) == result)

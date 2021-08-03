import pytest

import day08


program = [
    'nop +0',
    'acc +1',
    'jmp +4',
    'acc +3',
    'jmp -3',
    'acc -99',
    'acc +1',
    'jmp -4',
    'acc +6'
]


@pytest.mark.parametrize('program, result', [(program, 5)])
def test_program_v1(program, result):
    assert(day08.execute(program) == result)


@pytest.mark.parametrize('program, result', [(program, 8)])
def test_program_v2(program, result):
    assert(day08.safe_execute(program) == result)

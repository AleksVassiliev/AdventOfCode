import pytest

import day06


answers_raw = [
    'abc',
    '',
    'a',
    'b',
    'c',
    '',
    'ab',
    'ac',
    '',
    'a',
    'a',
    'a',
    'a',
    '',
    'b'
]


@pytest.mark.parametrize('answers, result', [(answers_raw, 11)])
def test_declaration_v1(answers, result):
    assert(day06.check_declaration_v1(answers) == result)


@pytest.mark.parametrize('answers, result', [(answers_raw, 6)])
def test_declaration_v2(answers, result):
    assert(day06.check_declaration_v2(answers) == result)

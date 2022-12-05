import day05

data = [
    '    [D]    ',    
    '[N] [C]    ',    
    '[Z] [M] [P]',
    ' 1   2   3 ',
    '',
    'move 1 from 2 to 1',
    'move 3 from 1 to 3',
    'move 2 from 2 to 1',
    'move 1 from 1 to 2'
]


def test_part1():
    assert(day05.rearrange_v1(data) == 'CMZ')


def test_part2():
    assert(day05.rearrange_v2(data) == 'MCD')

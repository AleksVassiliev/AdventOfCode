import day10


instr = [
    'noop',
    'addx 3',
    'addx -5'
]

def test_calculate():
    assert(day10.calculate_x(instr) == -1)


def test_strength():
    data = [line.strip() for line in open('./test_input.txt')]
    assert(day10.calculate_strength(data) == 13140)


image = [
    '##..##..##..##..##..##..##..##..##..##..',
    '###...###...###...###...###...###...###.',
    '####....####....####....####....####....',
    '#####.....#####.....#####.....#####.....',
    '######......######......######......####',
    '#######.......#######.......#######.....'
]


def test_image():
    data = [line.strip() for line in open('./test_input.txt')]
    assert(day10.draw_image(data) == image)

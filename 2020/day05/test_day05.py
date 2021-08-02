import pytest

import day05


@pytest.mark.parametrize('seat, row, column, seat_id', [('FBFBBFFRLR', 44, 5, 357), ('BFFFBBFRRR', 70, 7, 567), ('FFFBBBFRRR', 14, 7, 119), ('BBFFBBFRLL', 102, 4, 820)])
def test_boarding_pass(seat, row, column, seat_id):
    assert(day05.calculate_seat(seat) == (row, column, seat_id))

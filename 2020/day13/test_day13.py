import pytest

import day13


@pytest.mark.parametrize('timestamp, schedule, result', [(939, '7,13,x,x,59,x,31,19', 295)])
def test_schedule_v1(timestamp, schedule, result):
    assert(day13.calculate_delay(timestamp, schedule) == result)


@pytest.mark.parametrize('schedule, result', [('7,13,x,x,59,x,31,19', 295), ('17,x,13,19', 3417), ('67,7,59,61', 754018), ('67,x,7,59,61', 779210),
                                              ('67,7,x,59,61', 1261476), ('1789,37,47,1889', 1202161486)])
def test_schedule_v2(schedule, result):
    assert(day13.calculate_timestamp(schedule) == result)

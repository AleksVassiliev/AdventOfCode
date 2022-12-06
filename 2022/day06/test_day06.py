import pytest

import day06


@pytest.mark.parametrize('sequence, result', [('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7), 
                                              ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5), 
                                              ('nppdvjthqldpwncqszvftbrmjlhg', 6),
                                              ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
                                              ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11)])
def test_part1(sequence, result):
    assert(day06.find_marker_v1(sequence) == result)

@pytest.mark.parametrize('sequence, result', [('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19), 
                                              ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23), 
                                              ('nppdvjthqldpwncqszvftbrmjlhg', 23),
                                              ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
                                              ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26)])
def test_part2(sequence, result):
    assert(day06.find_marker_v2(sequence) == result)

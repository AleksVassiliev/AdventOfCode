import pytest

import day04


passports_parsed = [
    ({'ecl':'gry', 'pid':'860033327', 'eyr':'2020', 'hcl':'#fffffd', 'byr':'1937', 'iyr':'2017', 'cid':'147', 'hgt':'183cm'}, True),
    ({'iyr':'2013', 'ecl':'amb', 'cid':'350', 'eyr':'2023', 'pid':'028048884', 'hcl':'#cfa07d', 'byr':'1929'}, False),
    ({'hcl':'#ae17e1', 'iyr':'2013', 'eyr':'2024', 'ecl':'brn', 'pid':'760753108', 'byr':'1931', 'hgt':'179cm'}, True),
    ({'hcl':'#cfa07d', 'eyr':'2025', 'pid':'166559648', 'iyr':'2011', 'ecl':'brn', 'hgt':'59in'}, False)
]


passports_raw = [
    'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
    'byr:1937 iyr:2017 cid:147 hgt:183cm',
    '',
    'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
    'hcl:#cfa07d byr:1929',
    '',
    'hcl:#ae17e1 iyr:2013',
    'eyr:2024',
    'ecl:brn pid:760753108 byr:1931',
    'hgt:179cm',
    '',
    'hcl:#cfa07d eyr:2025 pid:166559648',
    'iyr:2011 ecl:brn hgt:59in',
]


passports_invalid = [
    'eyr:1972 cid:100',
    'hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926'
    '',
    'iyr:2019',
    'hcl:#602927 eyr:1967 hgt:170cm',
    'ecl:grn pid:012533040 byr:1946',
    '',
    'hcl:dab227 iyr:2012',
    'ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277',
    '',
    'hgt:59cm ecl:zzz',
    'eyr:2038 hcl:74454a iyr:2023',
    'pid:3556412378 byr:2007'
]


passports_valid = [
    'pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980',
    'hcl:#623a2f',
    '',
    'eyr:2029 ecl:blu cid:129 byr:1989',
    'iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm',
    '',
    'hcl:#888785',
    'hgt:164cm byr:2001 iyr:2015 cid:88',
    'pid:545766238 ecl:hzl',
    'eyr:2022',
    '',
    'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'
]


@pytest.mark.parametrize('passport, result', passports_parsed)
def test_passport(passport, result):
    assert(day04.check_passport(passport) == result)


@pytest.mark.parametrize('passports', [passports_raw])
def test_part1(passports):
    assert(day04.check_file_v1(passports) == 2)


@pytest.mark.parametrize('value, result', [('2002', True), ('2003', False)])
def test_check_byr(value, result):
    assert(day04.check_byr(value) == result)


@pytest.mark.parametrize('value, result', [('60in', True), ('190cm', True), ('190in', False), ('190', False)])
def test_check_hgt(value, result):
    assert(day04.check_hgt(value) == result)


@pytest.mark.parametrize('value, result', [('#123abc', True), ('#123abz', False), ('123abc', False)])
def test_check_hcl(value, result):
    assert(day04.check_hcl(value) == result)


@pytest.mark.parametrize('value, result', [('brn', True), ('wat', False)])
def test_check_ecl(value, result):
    assert(day04.check_ecl(value) == result)


@pytest.mark.parametrize('value, result', [('000000001', True), ('0123456789', False)])
def test_check_pid(value, result):
    assert(day04.check_pid(value) == result)


@pytest.mark.parametrize('passports, result', [(passports_invalid, 0), (passports_valid, 4)])
def test_part2(passports, result):
    assert(day04.check_file_v2(passports) == result)

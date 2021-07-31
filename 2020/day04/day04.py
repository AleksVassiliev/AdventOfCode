def check_passport(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return all(field in passport for field in required_fields)


def check_file_v1(data):
    result = 0
    passport = {}
    for line in data:
        if line == '':
            if check_passport(passport) is True:
                result += 1
            passport.clear()
        else:
            fields = line.split(' ')
            for item in fields:
                key, value = item.split(':')
                passport[key] = value
    if check_passport(passport) is True:
        result += 1
    return result


def check_byr(byr):
    byr = int(byr)
    return 1920 <= byr <= 2002


def check_iyr(iyr):
    iyr = int(iyr)
    return 2010 <= iyr <= 2020


def check_eyr(eyr):
    eyr = int(eyr)
    return 2020 <= eyr <= 2030


def check_hcl(hcl):
    if hcl[0] != '#':
        return False
    for ch in hcl[1:]:
        if ch not in '0123456789abcdef':
            return False
    return True


def check_hgt(hgt):
    dim = hgt[-2:]
    if dim not in ['cm', 'in']:
        return False
    hgt = int(hgt[:-2])
    if dim == 'cm':
        return 150 <= hgt <= 193
    if dim == 'in':
        return 59 <= hgt <= 76


def check_ecl(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def check_pid(pid):
    return len(pid) == 9 


def check_fields(passport):
    return all([
        check_byr(passport['byr']),
        check_iyr(passport['iyr']),
        check_eyr(passport['eyr']),
        check_hcl(passport['hcl']),
        check_hgt(passport['hgt']),
        check_ecl(passport['ecl']),
        check_pid(passport['pid'])
    ])


def check_file_v2(data):
    result = 0
    passport = {}
    for line in data:
        if line == '':
            if (check_passport(passport) and check_fields(passport)) is True:
                result += 1
            passport.clear()
        else:
            fields = line.split(' ')
            for item in fields:
                key, value = item.split(':')
                passport[key] = value
    if (check_passport(passport) and check_fields(passport)) is True:
        result += 1
    return result


def main():
    with open('./input04.txt') as fi:
        data = fi.read().splitlines()
    result_v1 = check_file_v1(data)
    print(result_v1)
    result_v2 = check_file_v2(data)
    print(result_v2)


if __name__ == '__main__':
    main()

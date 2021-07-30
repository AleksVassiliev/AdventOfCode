import itertools


def check_password_v1(policy: str, password: str):
    numbers, letter = policy.split(' ')
    min_num, max_num = numbers.split('-')
    count = 0
    for ch in password:
        if ch == letter:
            count += 1
    return int(min_num) <= count <= int(max_num)


def check_password_v2(policy: str, password: str):
    numbers, letter = policy.split(' ')
    pos = numbers.split('-')
    pos1 = int(pos[0]) - 1
    pos2 = int(pos[1]) - 1
    return (password[pos1] == letter) ^ (password[pos2] == letter)


def check_passwords(passwords: list, check_func):
    result = 0
    for line in passwords:
        policy, password = line.split(': ')
        if check_func(policy, password) is True:
            result += 1
    return result


def main():
    passwords = [line.strip() for line in open('./input.txt')]
    result_v1 = check_passwords(passwords, check_password_v1)
    print(result_v1)
    result_v2 = check_passwords(passwords, check_password_v2)
    print(result_v2)


if __name__ == '__main__':
    main()

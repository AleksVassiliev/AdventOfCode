from functools import reduce


def calculate_delay(timestamp, schedule):
    ids = [int(x) for x in schedule.split(',') if x != 'x']
    result = []
    for value in ids:
        res = timestamp // value
        if timestamp % value != 0:
            res += 1
        res_timestamp = res * value
        result.append((res_timestamp, value))
    result.sort(key=lambda x:x[0])
    return (result[0][0] - timestamp) * result[0][1]


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda x, y: x * y, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def calculate_timestamp(schedule):
    schedule = schedule.split(',')
    buses = [int(b) for b in schedule if b != 'x']
    offsets = [int(b) - i for i, b in enumerate(schedule) if b != 'x']
    return chinese_remainder(buses, offsets)


def main():
    with open('input13.txt') as fi:
        timestamp = int(fi.readline())
        schedule = fi.readline()
    result_v1 = calculate_delay(timestamp, schedule)
    print(result_v1)
    result_v2 = calculate_timestamp(schedule)
    print(result_v2)


if __name__ == '__main__':
    main()

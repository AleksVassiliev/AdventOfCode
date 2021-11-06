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


def calculate_timestamp(schedule):
    pass


def main():
    timestamp = 1005162
    schedule = '19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,823,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,443,x,x,x,x,x,37,x,x,x,x,x,x,13'
    result_v1 = calculate_delay(timestamp, schedule)
    print(result_v1)
    result_v2 = calculate_timestamp(schedule)
    print(result_v2)


if __name__ == '__main__':
    main()

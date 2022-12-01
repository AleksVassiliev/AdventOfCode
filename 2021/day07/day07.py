def calculate_fuel_v1(data, position):
    result = 0
    for el in data:
        result += abs(el - position)
    return result


def calculate_fuel_v2(data, position):
    result = 0
    for el in data:
        cost = abs(el - position)
        result += ((cost + 1) * cost) / 2
    return int(result)


def find_position_v1(data):
    result = None
    for idx, _ in enumerate(data):
        fuel = calculate_fuel_v1(data, idx)
        if result is None:
            result = fuel
        elif result > fuel:
            result = fuel
    return result


def find_position_v2(data):
    result = None
    for idx, _ in enumerate(data):
        fuel = calculate_fuel_v2(data, idx)
        if result is None:
            result = fuel
        elif result > fuel:
            result = fuel
    return result


def main():
    data = [int(x) for x in open('./input07.txt').readline().split(',')]
    result_v1 = find_position_v1(data)
    print(result_v1)
    result_v2 = find_position_v2(data)
    print(result_v2)


if __name__ == '__main__':
    main()

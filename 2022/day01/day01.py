def calculate_calories_v1(data):
    max_value = 0
    cur_value = 0
    for item in data:
        if item != '':
            cur_value += int(item)
        else:
            max_value = max(max_value, cur_value)
            cur_value = 0
    max_value = max(max_value, cur_value)
    return max_value


def calculate_calories_v2(data):
    values = []
    cur_value = 0
    for item in data:
        if item != '':
            cur_value += int(item)
        else:
            values.append(cur_value)
            cur_value = 0
    values.append(cur_value)
    values.sort(reverse=True)
    return (values[0] + values[1] + values[2])


def main():
    data = [line.strip() for line in open('./input.txt')]
    result_v1 = calculate_calories_v1(data)
    print(result_v1)
    result_v2 = calculate_calories_v2(data)
    print(result_v2)


if __name__ == '__main__':
    main()

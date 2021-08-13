def check_value(preamble, value):
    for idx1 in range(0, len(preamble) - 1):
        val2 = value - preamble[idx1]
        if val2 in preamble[idx1 + 1:]:
            return True
    return False


def check_sequence(data, preamble_length):
    for idx in range(preamble_length, len(data)):
        preamble = data[idx - preamble_length: idx]
        value = data[idx]
        if not check_value(preamble, value):
            return value
    return None


def find_range(data, value):
    result = 0
    for val in data:
        result += val
        if result == value:
            idx = data.index(val)
            return sorted(data[:idx + 1])
        if result > value:
            return None
    return None


def calculate_weakness(data, value):
    val_idx = data.index(value)
    for idx in range(0, val_idx):
        cont_range = find_range(data[idx:val_idx], value)
        if cont_range:
            return cont_range[0] + cont_range[-1]
    return None


def main():
    data = [int(line) for line in open('./input09.txt')]
    result_v1 = check_sequence(data, 25)
    print(result_v1)
    result_v2 = calculate_weakness(data, result_v1)
    print(result_v2)


if __name__ == '__main__':
    main()

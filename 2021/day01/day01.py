def calculate_report_v1(report: list):
    prev_value = report[0]
    measurements = 0
    for item in report:
        if item > prev_value:
            measurements += 1
        prev_value = item
    return measurements


def calculate_report_v2(report: list):
    prev_sum = 0
    measurements = -1
    for idx in range(len(report) - 2):
        cur_sum = sum(report[idx:idx+3])
        if cur_sum > prev_sum:
            measurements += 1
        prev_sum = cur_sum
    return measurements


def main():
    report = [int(line) for line in open('./input01.txt')]
    result_v1 = calculate_report_v1(report)
    print(result_v1)
    result_v2 = calculate_report_v2(report)
    print(result_v2)


if __name__ == '__main__':
    main()

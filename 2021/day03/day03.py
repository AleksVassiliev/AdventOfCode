import operator


def calculate_report_v1(report: list):
    gamma_rate = []
    epsilon_rate = []
    scores_0 = [0] * len(report[0])
    scores_1 = [0] * len(report[0])
    for item in report:
        for idx in range(len(item)):
            if item[idx] == '0':
                scores_0[idx] += 1
            elif item[idx] == '1':
                scores_1[idx] += 1
    for (a, b) in list(zip(scores_0, scores_1)):
        if a > b:
            gamma_rate.append('0')
            epsilon_rate.append('1')
        else:
            gamma_rate.append('1')
            epsilon_rate.append('0')
    return (int(''.join(gamma_rate), 2)) * (int(''.join(epsilon_rate), 2))


def reduce_list(report: list, pos: int, ops):
    report_0 = []
    report_1 = []
    for item in report:
        if item[pos] == '0':
            report_0.append(item)
        elif item[pos] == '1':
            report_1.append(item)
    if ops(len(report_0), len(report_1)):
        return report_0
    else:
        return report_1


def calculate_report_v2(report: list):
    pos = 0
    o2 = report
    while len(o2) > 1:
        o2 = reduce_list(o2, pos, operator.gt)
        pos += 1
    o2 = int(''.join(o2), 2)
    pos = 0
    co2 = report
    while len(co2) > 1:
        co2 = reduce_list(co2, pos, operator.le)
        pos += 1
    co2 = int(''.join(co2), 2)
    return o2 * co2


def main():
    report = [line.strip() for line in open('./input03.txt')]
    result_v1 = calculate_report_v1(report)
    print(result_v1)
    result_v2 = calculate_report_v2(report)
    print(result_v2)


if __name__ == '__main__':
    main()

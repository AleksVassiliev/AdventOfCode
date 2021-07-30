import itertools


def calculate_report_v1(report: list):
    variants = list(itertools.permutations(report, 2))
    for a, b in variants:
        if sum([a, b]) == 2020:
            return a * b


def calculate_report_v2(report: list):
    variants = list(itertools.permutations(report, 3))
    for a, b, c in variants:
        if sum([a, b, c]) == 2020:
            return a * b * c


def main():
    report = [int(line) for line in open('./input01.txt')]
    result_v1 = calculate_report_v1(report)
    print(result_v1)
    result_v2 = calculate_report_v2(report)
    print(result_v2)


if __name__ == '__main__':
    main()

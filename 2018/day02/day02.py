import collections
import itertools


def checksum(data):
    crc2 = 0
    crc3 = 0
    filtered_list = []

    for item in data:
        letters = collections.Counter(item)
        flag2 = False
        flag3 = False
        for key in letters:
            if letters[key] == 2:
                flag2 = True
            if letters[key] == 3:
                flag3 = True
        if flag2:
            crc2 += 1
        if flag3:
            crc3 += 1
        if flag2 or flag3:
            filtered_list.append(item)

    return (crc2 * crc3), filtered_list


def difference(data):
    comb = itertools.combinations(data, 2)
    for item in comb:
        diff = []
        res = []
        for i in range(len(item[0])):
            if item[0][i] != item[1][i]:
                diff.append(item[0][i])
            else:
                res.append(item[0][i])
        if len(diff) == 1:
            return "".join(res)


def main():
    data = [ line.rstrip("\n") for line in open("input02") ]

    crc, filtered = checksum(data)
    print(crc)

    res = difference(filtered)
    print(res)


if __name__ == "__main__":
    main()

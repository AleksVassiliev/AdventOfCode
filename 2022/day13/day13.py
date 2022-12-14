import json
import functools


def parse_data(data):
    pairs = []
    for i in range(0, len(data), 3):
        lhs = json.loads(data[i])
        rhs = json.loads(data[i+1])
        pairs.append((lhs, rhs))
    return pairs


def compare_lists(lhs, rhs):
    sz = min(len(lhs), len(rhs))
    res = 0
    for i in range(sz):
        if res != 0:
            break
        vall = lhs[i]
        valr = rhs[i]
        if type(vall) == type(valr):
            if isinstance(vall, int):
                if vall > valr:
                    res = -1
                elif vall < valr:
                    res = 1
                else:
                    res = 0
            elif isinstance(vall, list):
                res = compare_lists(vall, valr)
        else:
            if isinstance(vall, int):
                vall = [ vall ]
            if isinstance(valr, int):
                valr = [ valr ]
            res = compare_lists(vall, valr)
    if res == 0:
        if len(lhs) < len(rhs):
            res = 1
        elif len(lhs) > len(rhs):
            res = -1
    return res


def compare_pairs(pairs):
    res = 0
    for i in range(len(pairs)):
        res += (i + 1) if compare_lists(*pairs[i]) == 1 else 0
    return res


def count_pairs(data):
    pairs = parse_data(data)
    return compare_pairs(pairs)


def restore_order(data):
    signals = [[[2]], [[6]]]
    for line in data:
        if line != '':
            signals.append(json.loads(line))
    sorted_signals = sorted(signals, reverse=True, key=functools.cmp_to_key(compare_lists))
    val1 = sorted_signals.index([[2]]) + 1
    val2 = sorted_signals.index([[6]]) + 1
    return (val1 * val2)


def main():
    data = [line.strip() for line in open('./input.txt')]
    result_v1 = count_pairs(data)
    print(result_v1)
    result_v2 = restore_order(data)
    print(result_v2)


if __name__ == '__main__':
    main()

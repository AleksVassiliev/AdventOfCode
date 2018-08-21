import sys


def test_runTestA():
    table = "5\t1\t9\t5\n7\t5\t3\n2\t4\t6\t8\n"
    assert(calculateA(table) == 18)


def test_runTestB():
    table = "5\t9\t2\t8\n9\t4\t7\t3\n3\t8\t6\t5\n"
    assert(calculateB(table) == 9)


def calculateA(seq):
    rows = seq.split('\n')
    crc = 0
    for r in rows:
        if len(r) > 0:
            values = r.split('\t')
            valMin = int(values[0])
            valMax = int(values[0])
            for v in values:
                value = int(v)
                if valMin > value:
                    valMin = value
                if valMax < value:
                    valMax = value
            crc += (valMax - valMin)
    return crc


def sortFunc(str):
    return int(str)


def checkDivision(a, b):
    if a % b == 0:
        return int(a / b)
    return 0


def calculateB(seq):
    rows = seq.split('\n')
    crc = 0
    for r in rows:
        if len(r) > 0:
            values = r.split('\t')
            values.sort(key=sortFunc, reverse=True)
            for a in range(0, len(values) - 1):
                for b in range(a + 1, len(values)):
                    crc += checkDivision(int(values[a]), int(values[b]))
    return crc
    

def main(argv):
    with open("input", 'r') as f:
        data = f.read()
        res = calculateA(data)
        print("Result A = {}".format(res))
        res = calculateB(data)
        print("Result B = {}".format(res))


if __name__ == "__main__":
    main(sys.argv)

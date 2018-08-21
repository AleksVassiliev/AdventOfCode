import sys


def test_runTestA():
    assert(calculateA("1122") == 3)
    assert(calculateA("1111") == 4)
    assert(calculateA("1234") == 0)
    assert(calculateA("91212129") == 9)


def test_runTestB():
    assert(calculateB("1212") == 6)
    assert(calculateB("1221") == 0)
    assert(calculateB("123425") == 4)
    assert(calculateB("123123") == 12)
    assert(calculateB("12131415") == 4)



class CircularList:
    def __init__(self):
        self.data = list()
        self.size = 0


    def length(self):
        return self.size


    def value(self, idx):
        while idx >= self.size:
            idx -= self.size
        return self.data[idx]


    @staticmethod
    def fromString(seq):
        lst = CircularList()
        lst.data = [x for x in seq]
        lst.size = len(lst.data)
        return lst



def countSum(data, step):
    res = 0
    for i in range(0, data.length()):
        cur = int(data.value(i))
        nxt = int(data.value(i + step))
        if cur == nxt:
            res += cur
    return res


def calculateA(seq):
    lst = CircularList.fromString(seq)
    step = 1
    return countSum(lst, step)


def calculateB(seq):
    lst = CircularList.fromString(seq)
    step = int(lst.length() / 2)
    return countSum(lst, step)



def main(argv):
    with open("input", 'r') as f:
        data = f.read()
        res = calculateA(data)
        print("Result A = {}".format(res))
        res = calculateB(data)
        print("Result B = {}".format(res))


if __name__ == "__main__":
    main(sys.argv)

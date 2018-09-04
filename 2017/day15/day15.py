def test_partA():
    A = GeneratorA(65)
    B = GeneratorB(8921)

    pairs = 0
    for i in range(0, 40000000):
        resA = A.generate() & 0xFFFF
        resB = B.generate() & 0xFFFF
        if resA == resB:
            pairs += 1

    assert(pairs == 588)


def test_partB():
    A = GeneratorA(65)
    B = GeneratorB(8921)

    pairs = 0
    for i in range(0, 5000000):
        resA = A.generateMult() & 0xFFFF
        resB = B.generateMult() & 0xFFFF
        if resA == resB:
            pairs += 1

    assert(pairs == 309)


class Generator:
    def __init__(self, value, factor, mult):
        self.value = value
        self.factor = factor
        self.multiplies = mult


    def generate(self):
        res = self.value * self.factor
        res = res % 2147483647
        self.value = res
        return res


    def generateMult(self):
        while True:
            res = self.generate()
            if res % self.multiplies == 0:
                return res



class GeneratorA(Generator):
    def __init__(self, value):
        super().__init__(value, 16807, 4)


class GeneratorB(Generator):
    def __init__(self, value):
        super().__init__(value, 48271, 8)



def main():
    A = GeneratorA(703)
    B = GeneratorB(516)

    pairs = 0
    for i in range(0, 40000000):
        resA = A.generate() & 0xFFFF
        resB = B.generate() & 0xFFFF
        if resA == resB:
            pairs += 1

    print(pairs)


    C = GeneratorA(703)
    D = GeneratorB(516)

    pairs = 0
    for i in range(0, 5000000):
        resA = C.generateMult() & 0xFFFF
        resB = D.generateMult() & 0xFFFF
        if resA == resB:
            pairs += 1

    print(pairs)


if __name__ == "__main__":
    main()
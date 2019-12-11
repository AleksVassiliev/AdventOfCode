class PasswordA:
    def __init__(self, value):
        self.value = [ int(x) for x in str(value) ]

    def __str__(self):
        return '{}'.format(self.value)

    def is_valid(self):
        return self.increased() and self.adjacent()

    def increased(self):
        prev = self.value[0]
        for v in self.value[1:]:
            if v < prev:
                return False
            prev = v
        return True

    def adjacent(self):
        prev = self.value[0]
        for v in self.value[1:]:
            if v == prev:
                return True
            prev = v
        return False


class PasswordB:
    def __init__(self, value):
        self.value = [ int(x) for x in str(value) ]

    def __str__(self):
        return '{}'.format(self.value)

    def is_valid(self):
        return self.increased() and self.adjacent()

    def increased(self):
        prev = self.value[0]
        for v in self.value[1:]:
            if v < prev:
                return False
            prev = v
        return True

    def adjacent(self):
        cnt = 1
        prev = self.value[0]
        for v in self.value[1:]:
            if v == prev:
                cnt += 1
            else:
                if cnt == 2:
                    return True
                cnt = 1
            prev = v
        if cnt == 2:
            return True
        return False


def main():
    cntA = 0
    cntB = 0
    for i in range(123257, 647015):
        if PasswordA(i).is_valid():
            cntA += 1
        if PasswordB(i).is_valid():
            cntB += 1
    print(cntA, cntB)

if __name__ == '__main__':
    main()

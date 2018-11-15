def calculateA(data):
    res = 0
    for c in data:
        if c == '(':
            res += 1
        elif c == ')':
            res -= 1
    return res


def calculateB(data):
    res = 0
    for idx, c in enumerate(data):
        if c == '(':
            res += 1
        elif c == ')':
            res -= 1
        if res == -1:
            return (idx+1)
    return 0


def main():
    with open("input01", "r") as f:
        data = f.read()
        res1 = calculateA(data)
        res2 = calculateB(data)
        print(res1, res2)


if __name__ == "__main__":
    main()

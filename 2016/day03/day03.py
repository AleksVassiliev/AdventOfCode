def checkTriangle(sides):
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
        return True
    return False


def getTrianglesRow(data):
    r = []
    for item in data:
        r.append(list(map(int, item.split())))
    return r


def getTrianglesCol(data):
    c1 = []
    c2 = []
    c3 = []
    for item in data:
        sides = list(map(int, item.split()))
        c1.append(sides[0])
        c2.append(sides[1])
        c3.append(sides[2])
    return (c1 + c2 + c3)


def solution1(data):
    res = 0
    triangles = getTrianglesRow(data)
    for item in triangles:
        if checkTriangle(item) == True:
            res += 1
    return res


def solution2(data):
    res = 0
    triangles = getTrianglesCol(data)
    for i in range(0, len(triangles), 3):
        if checkTriangle(triangles[i:i+3]) == True:
            res += 1
    return res


def main():
    data = [ line.rstrip("\n") for line in open("input03") ]

    print(solution1(data))
    print(solution2(data))


if __name__ == "__main__":
    main()
